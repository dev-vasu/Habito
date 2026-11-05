import 'package:flutter/material.dart';

class Habit {
  final String id;
  String title;
  String description;
  int iconCodePoint;
  String? iconFontFamily;
  int colorValue;
  final DateTime createdAt;
  Map<String, bool> history; // key: 'yyyy-MM-dd'

  Habit({
    required this.id,
    required this.title,
    required this.description,
    required this.iconCodePoint,
    this.iconFontFamily = 'MaterialIcons',
    this.colorValue = 0xFF7C4DFF, // deepPurpleAccent default
    DateTime? createdAt,
    Map<String, bool>? history,
  })  : createdAt = createdAt ?? DateTime.now(),
        history = history ?? {};

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

  void toggleCompletion([DateTime? date]) {
    final targetDate = date ?? DateTime.now();
    final key = dateKey(targetDate);
    final current = history[key] ?? false;
    history[key] = !current;
  }

  void setCompleted(DateTime date, bool completed) {
    history[dateKey(date)] = completed;
  }

  /// Calculates current consecutive streak up to today or yesterday
  int get currentStreak {
    final now = DateTime.now();
    final today = DateTime(now.year, now.month, now.day);
    int streak = 0;

    // Check today: if completed, start counting from today; otherwise start from yesterday
    DateTime checkDate = today;
    if (!isCompletedOn(today)) {
      checkDate = today.subtract(const Duration(days: 1));
      if (!isCompletedOn(checkDate)) {
        return 0;
      }
    }

    while (isCompletedOn(checkDate)) {
      streak++;
      checkDate = checkDate.subtract(const Duration(days: 1));
    }

    return streak;
  }

  /// Calculates the best streak ever achieved
  int get bestStreak {
    if (history.isEmpty) return 0;

    final sortedDates = history.entries
        .where((e) => e.value)
        .map((e) {
          final parts = e.key.split('-');
          if (parts.length == 3) {
            return DateTime(
                int.parse(parts[0]), int.parse(parts[1]), int.parse(parts[2]));
          }
          return null;
        })
        .whereType<DateTime>()
        .toList()
      ..sort();

    if (sortedDates.isEmpty) return 0;

    int maxStreak = 1;
    int currentRun = 1;

    for (int i = 1; i < sortedDates.length; i++) {
      final diff = sortedDates[i].difference(sortedDates[i - 1]).inDays;
      if (diff == 1) {
        currentRun++;
        if (currentRun > maxStreak) {
          maxStreak = currentRun;
        }
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

    for (int i = 0; i < 7; i++) {
      final date = today.subtract(Duration(days: i));
      if (isCompletedOn(date)) {
        completedCount++;
      }
    }

    return completedCount / 7.0;
  }

  /// Returns completion status for the last 7 days in chronological order [oldest ... today]
  List<double> get last7DaysData {
    final now = DateTime.now();
    final today = DateTime(now.year, now.month, now.day);
    final List<double> result = [];

    for (int i = 6; i >= 0; i--) {
      final date = today.subtract(Duration(days: i));
      result.add(isCompletedOn(date) ? 1.0 : 0.0);
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
      'createdAt': createdAt.toIso8601String(),
      'history': history,
    };
  }

  factory Habit.fromJson(Map<String, dynamic> json) {
    return Habit(
      id: json['id'] as String,
      title: json['title'] as String,
      description: json['description'] as String,
      iconCodePoint: json['iconCodePoint'] as int,
      iconFontFamily: json['iconFontFamily'] as String?,
      colorValue: json['colorValue'] as int? ?? 0xFF7C4DFF,
      createdAt: json['createdAt'] != null
          ? DateTime.tryParse(json['createdAt'] as String) ?? DateTime.now()
          : DateTime.now(),
      history: json['history'] != null
          ? Map<String, bool>.from(json['history'] as Map)
          : {},
    );
  }
}
