import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../models/habit.dart';
import '../models/user_profile.dart';
import 'backup_service.dart';

class HabitService extends ChangeNotifier {
  static const String _storageKey = 'habito_user_habits_v2';
  static const String _shieldStorageKey = 'habito_streak_shields_v2';
  static const String _profileStorageKey = 'habito_user_profile_v2';

  List<Habit> _habits = [];
  UserProfile _profile = UserProfile();
  int _streakShields = 2;
  String _currentSyncKey = BackupService.generateCollisionProofSyncCode();
  bool _isLoaded = false;

  List<Habit> get habits => List.unmodifiable(_habits);
  UserProfile get profile => _profile;
  int get streakShields => _streakShields;
  String get currentSyncKey => _currentSyncKey;
  bool get isLoaded => _isLoaded;

  HabitService() {
    _init();
  }

  Future<void> _init() async {
    await loadHabits();
  }

  Future<void> loadHabits() async {
    try {
      final prefs = await SharedPreferences.getInstance();
      _streakShields = prefs.getInt(_shieldStorageKey) ?? 2;

      // Load Profile
      final profileString = prefs.getString(_profileStorageKey);
      if (profileString != null && profileString.isNotEmpty) {
        _profile = UserProfile.fromJson(jsonDecode(profileString));
      }

      // Load Habits
      final jsonString = prefs.getString(_storageKey);
      if (jsonString != null && jsonString.isNotEmpty) {
        final List<dynamic> decoded = jsonDecode(jsonString);
        _habits = decoded
            .map((item) => Habit.fromJson(Map<String, dynamic>.from(item)))
            .toList();
      } else {
        _habits = _generateDefaultHabits();
        await saveHabits();
      }
    } catch (e) {
      debugPrint('Error loading habits: $e');
      if (_habits.isEmpty) {
        _habits = _generateDefaultHabits();
      }
    } finally {
      _isLoaded = true;
      notifyListeners();
    }
  }

  Future<void> saveHabits() async {
    try {
      final prefs = await SharedPreferences.getInstance();
      final encoded = jsonEncode(_habits.map((h) => h.toJson()).toList());
      await prefs.setString(_storageKey, encoded);
      await prefs.setInt(_shieldStorageKey, _streakShields);
      await prefs.setString(_profileStorageKey, jsonEncode(_profile.toJson()));
    } catch (e) {
      debugPrint('Error saving habits: $e');
    }
  }

  Future<void> updateProfile({
    String? name,
    String? personalMotto,
    String? avatarEmoji,
    Color? accentColor,
  }) async {
    _profile = _profile.copyWith(
      name: name?.trim(),
      personalMotto: personalMotto?.trim(),
      avatarEmoji: avatarEmoji,
      accentColorValue: accentColor?.value,
    );
    notifyListeners();
    await saveHabits();
  }

  Future<void> addHabit({
    required String title,
    required String description,
    required IconData icon,
    Color color = const Color(0xFF4D96FF),
    HabitFrequency frequency = HabitFrequency.daily,
  }) async {
    final newHabit = Habit(
      id: DateTime.now().millisecondsSinceEpoch.toString(),
      title: title.trim(),
      description: description.trim(),
      iconCodePoint: icon.codePoint,
      iconFontFamily: icon.fontFamily,
      colorValue: color.value,
      frequency: frequency,
      createdAt: DateTime.now(),
      history: {},
      frozenDates: {},
    );

    _habits.add(newHabit);
    notifyListeners();
    await saveHabits();
  }

  Future<void> updateHabit({
    required String id,
    required String title,
    required String description,
    required IconData icon,
    required Color color,
    required HabitFrequency frequency,
  }) async {
    final index = _habits.indexWhere((h) => h.id == id);
    if (index != -1) {
      _habits[index].title = title.trim();
      _habits[index].description = description.trim();
      _habits[index].iconCodePoint = icon.codePoint;
      _habits[index].iconFontFamily = icon.fontFamily;
      _habits[index].colorValue = color.value;
      _habits[index].frequency = frequency;
      notifyListeners();
      await saveHabits();
    }
  }

  Future<void> deleteHabit(String id) async {
    _habits.removeWhere((h) => h.id == id);
    notifyListeners();
    await saveHabits();
  }

  Future<void> toggleHabit(String id, [DateTime? date]) async {
    final habit = _habits.firstWhere((h) => h.id == id);
    habit.toggleCompletion(date);
    notifyListeners();
    await saveHabits();
  }

  Future<bool> useStreakShield(String habitId, [DateTime? date]) async {
    if (_streakShields <= 0) return false;
    final habit = _habits.firstWhere((h) => h.id == habitId,
        orElse: () => throw Exception('Habit not found'));

    final targetDate = date ?? DateTime.now();
    habit.freezeDate(targetDate);
    _streakShields--;
    notifyListeners();
    await saveHabits();
    return true;
  }

  // Cross-Device Vault Migration Methods
  String exportVaultJson({String? pin}) {
    return BackupService.exportToJson(
      habits: _habits,
      streakShields: _streakShields,
      profile: _profile,
      pin: pin,
    );
  }

  void regenerateSyncKey() {
    _currentSyncKey = BackupService.generateCollisionProofSyncCode();
    notifyListeners();
  }

  Future<bool> restoreVault(String backupJson, {String? pin}) async {
    final payload = BackupService.parseBackup(backupJson, pin: pin);
    if (payload == null || payload.habits.isEmpty) return false;

    _habits = payload.habits;
    _streakShields = payload.streakShields;
    _profile = payload.profile;
    notifyListeners();
    await saveHabits();
    return true;
  }

  // Analytics & Computed Properties
  int get totalHabits => _habits.length;

  int get completedTodayCount =>
      _habits.where((h) => h.isCompletedToday()).length;

  int get remainingTodayCount => totalHabits - completedTodayCount;

  double get todayProgressPercentage {
    if (totalHabits == 0) return 0.0;
    return completedTodayCount / totalHabits;
  }

  List<Habit> get topHabitsThisWeek {
    final list = List<Habit>.from(_habits);
    list.sort(
        (a, b) => b.weeklyCompletionRate.compareTo(a.weeklyCompletionRate));
    return list;
  }

  List<Habit> get worstHabitsThisWeek {
    final list = List<Habit>.from(_habits);
    list.sort(
        (a, b) => a.weeklyCompletionRate.compareTo(b.weeklyCompletionRate));
    return list;
  }

  int get overallWeeklyPercentage {
    if (_habits.isEmpty) return 0;
    final totalSum = _habits.fold<double>(
      0.0,
      (acc, h) => acc + h.weeklyCompletionRate,
    );
    return ((totalSum / _habits.length) * 100).round();
  }

  List<Habit> _generateDefaultHabits() {
    final now = DateTime.now();
    final today = DateTime(now.year, now.month, now.day);

    Map<String, bool> makeHistory(List<int> daysAgoCompleted) {
      final map = <String, bool>{};
      for (final days in daysAgoCompleted) {
        final d = today.subtract(Duration(days: days));
        map[Habit.dateKey(d)] = true;
      }
      return map;
    }

    return [
      Habit(
        id: '1',
        title: 'Hydrate 2.5L',
        description: 'Drink at least 8 cups of water daily',
        iconCodePoint: Icons.local_drink.codePoint,
        iconFontFamily: Icons.local_drink.fontFamily,
        colorValue: 0xFF4D96FF,
        frequency: HabitFrequency.daily,
        history: makeHistory([0, 1, 2, 3, 4, 5, 6]),
      ),
      Habit(
        id: '2',
        title: 'Deep Reading',
        description: 'Read at least 25 pages without phone',
        iconCodePoint: Icons.menu_book.codePoint,
        iconFontFamily: Icons.menu_book.fontFamily,
        colorValue: 0xFFFF9F43,
        frequency: HabitFrequency.weekdays,
        history: makeHistory([0, 1, 2, 3, 5]),
      ),
      Habit(
        id: '3',
        title: 'Ship Code',
        description: '2 focused commits or feature builds',
        iconCodePoint: Icons.code.codePoint,
        iconFontFamily: Icons.code.fontFamily,
        colorValue: 0xFF9D4EDD,
        frequency: HabitFrequency.weekdays,
        history: makeHistory([1, 2, 4, 6]),
      ),
      Habit(
        id: '4',
        title: 'Cardio / Run',
        description: '5km run or 30 mins cardio session',
        iconCodePoint: Icons.directions_run.codePoint,
        iconFontFamily: Icons.directions_run.fontFamily,
        colorValue: 0xFF6BCB77,
        frequency: HabitFrequency.threePerWeek,
        history: makeHistory([2, 5]),
      ),
    ];
  }
}

class HabitScope extends InheritedNotifier<HabitService> {
  const HabitScope({
    Key? key,
    required HabitService service,
    required Widget child,
  }) : super(key: key, notifier: service, child: child);

  static HabitService of(BuildContext context) {
    final scope = context.dependOnInheritedWidgetOfExactType<HabitScope>();
    assert(scope != null, 'No HabitScope found in context');
    return scope!.notifier!;
  }
}
