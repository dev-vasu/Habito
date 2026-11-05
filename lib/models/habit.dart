import 'package:flutter/material.dart';

enum HabitFrequency {
  daily,
  weekdays,
  threePerWeek,
  fourPerWeek,
}

extension HabitFrequencyExtension on HabitFrequency {
  String get label {
    switch (this) {
      case HabitFrequency.daily:
        return 'Daily (7/7)';
      case HabitFrequency.weekdays:
        return 'Weekdays (5/7)';
      case HabitFrequency.threePerWeek:
        return '3x / week';
      case HabitFrequency.fourPerWeek:
        return '4x / week';
    }
  }

  String get tag {
    switch (this) {
      case HabitFrequency.daily:
        return '7/7';
      case HabitFrequency.weekdays:
        return '5/7';
      case HabitFrequency.threePerWeek:
        return '3/7';
      case HabitFrequency.fourPerWeek:
        return '4/7';
    }
  }

  int get targetDaysPerWeek {
    switch (this) {
      case HabitFrequency.daily:
        return 7;
      case HabitFrequency.weekdays:
        return 5;
      case HabitFrequency.threePerWeek:
        return 3;
      case HabitFrequency.fourPerWeek:
        return 4;
    }
  }
}

class Habit {
  final String id;
  String title;
  String description;
  int iconCodePoint;
  String? iconFontFamily;
  int colorValue;
  final DateTime createdAt;
  HabitFrequency frequency;
  Map<String, bool> history; // key: 'yyyy-MM-dd'
  Map<String, bool> frozenDates; // dates protected by streak shield

  Habit({
    required this.id,
    required this.title,
    required this.description,
    required this.iconCodePoint,
    this.iconFontFamily = 'MaterialIcons',
    this.colorValue = 0xFF4D96FF,
    this.frequency = HabitFrequency.daily,
    DateTime? createdAt,
    Map<String, bool>? history,
    Map<String, bool>? frozenDates,
  })  : createdAt = createdAt ?? DateTime.now(),
        history = history ?? {},
        frozenDates = frozenDates ?? {};

  IconData get icon => IconData(
        iconCodePoint,
        fontFamily: iconFontFamily ?? 'MaterialIcons',
      );

  Color get color => Color(colorValue);

  static String dateKey(DateTime date) {
    final year = date.year.toString().padLeft(4, '0');
    final month = date.month.toString().padLeft(2, '0');
    final day = date.day.toString().padLeft(2, '0');
    return '$year-$month-$day';
  }

  bool isCompletedToday() {
    return isCompletedOn(DateTime.now());
  }

  bool isCompletedOn(DateTime date) {
    return history[dateKey(date)] == true;
  }

  bool isFrozenOn(DateTime date) {
    return frozenDates[dateKey(date)] == true;
  }

  bool isScheduledOn(DateTime date) {
    if (frequency == HabitFrequency.weekdays) {
      return date.weekday >= DateTime.monday && date.weekday <= DateTime.friday;
    }
    return true;
  }

  void toggleCompletion([DateTime? date]) {
    final targetDate = date ?? DateTime.now();
    final key = dateKey(targetDate);
    final current = history[key] ?? false;
    history[key] = !current;
  }

  void setCompleted(DateTime date, bool completed) {
    history[dateKey(date)] = completed;
  }

  void freezeDate(DateTime date) {
    frozenDates[dateKey(date)] = true;
  }

  /// Calculates current streak factoring in completed days and streak freeze shields
  int get currentStreak {
    final now = DateTime.now();
    final today = DateTime(now.year, now.month, now.day);
    int streak = 0;

    DateTime checkDate = today;
    final bool completedToday = isCompletedOn(today) || isFrozenOn(today);

    if (!completedToday) {
      checkDate = today.subtract(const Duration(days: 1));
      // If yesterday wasn't scheduled (e.g. weekend on weekdays habit), skip back
      while (!isScheduledOn(checkDate)) {
        checkDate = checkDate.subtract(const Duration(days: 1));
      }
      if (!isCompletedOn(checkDate) && !isFrozenOn(checkDate)) {
        return 0;
      }
    }

    while (true) {
      if (!isScheduledOn(checkDate)) {
        checkDate = checkDate.subtract(const Duration(days: 1));
        continue;
      }

      if (isCompletedOn(checkDate) || isFrozenOn(checkDate)) {
        streak++;
        checkDate = checkDate.subtract(const Duration(days: 1));
      } else {
        break;
      }
    }

    return streak;
  }

  /// Best streak ever achieved
  int get bestStreak {
    if (history.isEmpty && frozenDates.isEmpty) return 0;
    final allSuccessful = <DateTime>{};

    for (final e in history.entries) {
      if (e.value) {
        final parts = e.key.split('-');
        if (parts.length == 3) {
          allSuccessful.add(DateTime(int.parse(parts[0]), int.parse(parts[1]), int.parse(parts[2])));
        }
      }
    }
    for (final e in frozenDates.entries) {
      if (e.value) {
        final parts = e.key.split('-');
        if (parts.length == 3) {
          allSuccessful.add(DateTime(int.parse(parts[0]), int.parse(parts[1]), int.parse(parts[2])));
        }
      }
    }

    final sortedDates = allSuccessful.toList()..sort();
    if (sortedDates.isEmpty) return 0;

    int maxStreak = 1;
    int currentRun = 1;

    for (int i = 1; i < sortedDates.length; i++) {
      final diff = sortedDates[i].difference(sortedDates[i - 1]).inDays;
      if (diff == 1) {
        currentRun++;
        if (currentRun > maxStreak) maxStreak = currentRun;
      } else if (diff > 1) {
        currentRun = 1;
      }
    }

    return maxStreak;
  }

  /// Calculates completion rate over the last 7 days (0.0 to 1.0)
  double get weeklyCompletionRate {
    final now = DateTime.now();
    final today = DateTime(now.year, now.month, now.day);
    int completedCount = 0;
    int scheduledCount = 0;

    for (int i = 0; i < 7; i++) {
      final date = today.subtract(Duration(days: i));
      if (isScheduledOn(date)) {
        scheduledCount++;
        if (isCompletedOn(date) || isFrozenOn(date)) {
          completedCount++;
        }
      }
    }

    if (scheduledCount == 0) return 1.0;
    return (completedCount / scheduledCount).clamp(0.0, 1.0);
  }

  /// 7-day chronological data array [oldest ... today]
  List<double> get last7DaysData {
    final now = DateTime.now();
    final today = DateTime(now.year, now.month, now.day);
    final List<double> result = [];

    for (int i = 6; i >= 0; i--) {
      final date = today.subtract(Duration(days: i));
      final completed = isCompletedOn(date) || isFrozenOn(date);
      result.add(completed ? 1.0 : 0.0);
    }

    return result;
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'title': title,
      'description': description,
      'iconCodePoint': iconCodePoint,
      'iconFontFamily': iconFontFamily,
      'colorValue': colorValue,
      'frequency': frequency.name,
      'createdAt': createdAt.toIso8601String(),
      'history': history,
      'frozenDates': frozenDates,
    };
  }

  factory Habit.fromJson(Map<String, dynamic> json) {
    HabitFrequency freq = HabitFrequency.daily;
    if (json['frequency'] != null) {
      try {
        freq = HabitFrequency.values.firstWhere(
          (e) => e.name == json['frequency'],
          orElse: () => HabitFrequency.daily,
        );
      } catch (_) {
        freq = HabitFrequency.daily;
      }
    }

    return Habit(
      id: json['id'] as String,
      title: json['title'] as String,
      description: json['description'] as String,
      iconCodePoint: json['iconCodePoint'] as int,
      iconFontFamily: json['iconFontFamily'] as String?,
      colorValue: json['colorValue'] as int? ?? 0xFF4D96FF,
      frequency: freq,
      createdAt: json['createdAt'] != null
          ? DateTime.tryParse(json['createdAt'] as String) ?? DateTime.now()
          : DateTime.now(),
      history: json['history'] != null
          ? Map<String, bool>.from(json['history'] as Map)
          : {},
      frozenDates: json['frozenDates'] != null
          ? Map<String, bool>.from(json['frozenDates'] as Map)
          : {},
    );
  }
}
