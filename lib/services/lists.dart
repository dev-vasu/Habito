import 'package:flutter/material.dart';

/// Neo-Brutalist design tokens
class NeoBrutalism {
  static const Color background = Color(0xFFFFFDF0); // Cream butter
  static const Color black = Color(0xFF1E1E1E);      // Solid outline black
  static const Color surface = Color(0xFFFFFFFF);    // Card surface
  static const Color yellow = Color(0xFFFFE66D);     // Fuel Yellow
  static const Color green = Color(0xFF6BCB77);      // Mint Green
  static const Color blue = Color(0xFF4D96FF);       // Cobalt Blue
  static const Color red = Color(0xFFFF6B6B);        // Paprika Red
  static const Color purple = Color(0xFF9D4EDD);     // Violet
  static const Color orange = Color(0xFFFF9F43);     // Hot Coral

  static BoxDecoration box({
    Color backgroundColor = surface,
    double radius = 18,
    double borderWidth = 2.5,
    Offset shadowOffset = const Offset(4, 4),
  }) {
    return BoxDecoration(
      color: backgroundColor,
      borderRadius: BorderRadius.circular(radius),
      border: Border.all(color: black, width: borderWidth),
      boxShadow: [
        BoxShadow(
          color: black,
          offset: shadowOffset,
          blurRadius: 0, // Hard shadow
        ),
      ],
    );
  }

  static BoxDecoration badge({
    required Color color,
    double radius = 8,
  }) {
    return BoxDecoration(
      color: color,
      borderRadius: BorderRadius.circular(radius),
      border: Border.all(color: black, width: 2),
      boxShadow: const [
        BoxShadow(
          color: black,
          offset: Offset(2, 2),
          blurRadius: 0,
        ),
      ],
    );
  }
}

/// Available icons for user habit selection
class HabitIconOption {
  final String label;
  final IconData icon;

  const HabitIconOption(this.label, this.icon);
}

const List<HabitIconOption> availableHabitIcons = [
  HabitIconOption('Water', Icons.local_drink),
  HabitIconOption('Reading', Icons.menu_book),
  HabitIconOption('Coding', Icons.code),
  HabitIconOption('Fitness', Icons.fitness_center),
  HabitIconOption('Running', Icons.directions_run),
  HabitIconOption('Meditation', Icons.self_improvement),
  HabitIconOption('Sleep', Icons.bedtime),
  HabitIconOption('Diet', Icons.restaurant),
  HabitIconOption('Music', Icons.music_note),
  HabitIconOption('Journal', Icons.edit_note),
  HabitIconOption('Study', Icons.school),
  HabitIconOption('Walk', Icons.nordic_walking),
  HabitIconOption('Cycling', Icons.directions_bike),
  HabitIconOption('Focus', Icons.bolt),
];

/// Curated Neo-Brutalist color palette
const List<Color> availableHabitColors = [
  NeoBrutalism.green,
  NeoBrutalism.blue,
  NeoBrutalism.red,
  NeoBrutalism.purple,
  NeoBrutalism.orange,
  Color(0xFF2EC4B6), // Turquoise
  Color(0xFFFF99C8), // Bubblegum Pink
  Color(0xFFFCBF49), // Marigold
];
