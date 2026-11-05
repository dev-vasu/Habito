import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../models/habit.dart';

class HabitService extends ChangeNotifier {
  static const String _storageKey = 'habito_user_habits_v2';
  List<Habit> _habits = [];
  bool _isLoaded = false;

  List<Habit> get habits => List.unmodifiable(_habits);
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
    } catch (e) {
      debugPrint('Error saving habits: $e');
    }
  }

  Future<void> addHabit({
    required String title,
    required String description,
    required IconData icon,
    Color color = Colors.deepPurpleAccent,
  }) async {
    final newHabit = Habit(
      id: DateTime.now().millisecondsSinceEpoch.toString(),
      title: title.trim(),
      description: description.trim(),
      iconCodePoint: icon.codePoint,
      iconFontFamily: icon.fontFamily,
      colorValue: color.value,
      createdAt: DateTime.now(),
      history: {},
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
  }) async {
    final index = _habits.indexWhere((h) => h.id == id);
    if (index != -1) {
      _habits[index].title = title.trim();
      _habits[index].description = description.trim();
      _habits[index].iconCodePoint = icon.codePoint;
      _habits[index].iconFontFamily = icon.fontFamily;
      _habits[index].colorValue = color.value;
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
    final habit = _habits.firstWhere((h) => h.id == id, orElse: () => throw Exception('Habit not found'));
    habit.toggleCompletion(date);
    notifyListeners();
    await saveHabits();
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

  /// Habits ranked highest by weekly completion rate
  List<Habit> get topHabitsThisWeek {
    final list = List<Habit>.from(_habits);
    list.sort((a, b) => b.weeklyCompletionRate.compareTo(a.weeklyCompletionRate));
    return list;
  }

  /// Habits ranked lowest by weekly completion rate
  List<Habit> get worstHabitsThisWeek {
    final list = List<Habit>.from(_habits);
    list.sort((a, b) => a.weeklyCompletionRate.compareTo(b.weeklyCompletionRate));
    return list;
  }

  /// Total consistency rate across all habits over the last 7 days (0% - 100%)
  int get overallWeeklyPercentage {
    if (_habits.isEmpty) return 0;
    final totalSum = _habits.fold<double>(
      0.0,
      (acc, h) => acc + h.weeklyCompletionRate,
    );
    return ((totalSum / _habits.length) * 100).round();
  }

  /// Seed initial habits with some recent activity so new installs have an engaging starting point
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
        title: 'Drink Water',
        description: 'Drink at least 8 cups of water daily',
        iconCodePoint: Icons.local_drink.codePoint,
        iconFontFamily: Icons.local_drink.fontFamily,
        colorValue: Colors.blueAccent.value,
        history: makeHistory([0, 1, 2, 3, 4, 5, 6]), // 100% week
      ),
      Habit(
        id: '2',
        title: 'Read Books',
        description: 'Read at least 25 pages of a book',
        iconCodePoint: Icons.menu_book.codePoint,
        iconFontFamily: Icons.menu_book.fontFamily,
        colorValue: Colors.orangeAccent.value,
        history: makeHistory([0, 1, 2, 3, 5]), // 71% week
      ),
      Habit(
        id: '3',
        title: 'Work on Code',
        description: 'Practice programming or work on projects',
        iconCodePoint: Icons.code.codePoint,
        iconFontFamily: Icons.code.fontFamily,
        colorValue: Colors.deepPurpleAccent.value,
        history: makeHistory([1, 2, 4, 6]), // 57% week
      ),
      Habit(
        id: '4',
        title: 'Exercise & Cardio',
        description: 'Go to the gym or do 30 mins cardio',
        iconCodePoint: Icons.fitness_center.codePoint,
        iconFontFamily: Icons.fitness_center.fontFamily,
        colorValue: Colors.teal.value,
        history: makeHistory([2, 5]), // 28% week
      ),
    ];
  }
}

/// An InheritedNotifier so any widget in the tree can access HabitService easily via HabitScope.of(context)
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
