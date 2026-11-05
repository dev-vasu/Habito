import 'dart:convert';
import 'package:flutter/foundation.dart';
import '../models/habit.dart';

class VaultBackupPayload {
  final String version;
  final String exportedAt;
  final int streakShields;
  final List<Habit> habits;

  VaultBackupPayload({
    required this.version,
    required this.exportedAt,
    required this.streakShields,
    required this.habits,
  });

  Map<String, dynamic> toJson() => {
        'version': version,
        'app': 'Habito',
        'exportedAt': exportedAt,
        'streakShields': streakShields,
        'habits': habits.map((h) => h.toJson()).toList(),
      };

  factory VaultBackupPayload.fromJson(Map<String, dynamic> json) {
    final habitsList = (json['habits'] as List<dynamic>? ?? [])
        .map((item) => Habit.fromJson(Map<String, dynamic>.from(item)))
        .toList();

    return VaultBackupPayload(
      version: json['version'] as String? ?? '2.1',
      exportedAt: json['exportedAt'] as String? ?? DateTime.now().toIso8601String(),
      streakShields: json['streakShields'] as int? ?? 2,
      habits: habitsList,
    );
  }
}

class BackupService {
  static const String currentVaultVersion = '2.1.0';

  /// Generates human-friendly 6-digit sync code based on vault hash
  static String generateSyncCode(List<Habit> habits) {
    int hash = 17;
    for (final h in habits) {
      hash = 37 * hash + h.id.hashCode;
    }
    final positive = hash.abs() % 9000 + 1000;
    return 'HAB-$positive';
  }

  /// Exports entire user progress into a portable JSON string
  static String exportToJson({
    required List<Habit> habits,
    required int streakShields,
  }) {
    final payload = VaultBackupPayload(
      version: currentVaultVersion,
      exportedAt: DateTime.now().toIso8601String(),
      streakShields: streakShields,
      habits: habits,
    );
    return const JsonEncoder.withIndent('  ').convert(payload.toJson());
  }

  /// Imports and validates a vault backup JSON string
  static VaultBackupPayload? parseBackup(String rawContent) {
    try {
      final trimmed = rawContent.trim();
      final Map<String, dynamic> decoded = jsonDecode(trimmed);
      return VaultBackupPayload.fromJson(decoded);
    } catch (e) {
      debugPrint('Error parsing vault backup: $e');
      return null;
    }
  }
}
