import 'package:flutter/material.dart';

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
  HabitIconOption('Tasks', Icons.check_circle_outline),
];

/// Curated color palette for habits
const List<Color> availableHabitColors = [
  Colors.deepPurpleAccent,
  Colors.blueAccent,
  Colors.teal,
  Colors.green,
  Colors.orangeAccent,
  Colors.pinkAccent,
  Colors.indigoAccent,
  Colors.deepOrange,
  Colors.cyan,
  Colors.amber,
];
