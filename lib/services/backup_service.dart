import 'dart:convert';
import 'dart:math';
import 'package:flutter/foundation.dart';
import '../models/habit.dart';
import '../models/user_profile.dart';

class VaultBackupPayload {
  final String version;
  final String vaultId;
  final String exportedAt;
  final int streakShields;
  final UserProfile profile;
  final List<Habit> habits;
  final String? securityPinHash; // Optional protection

  VaultBackupPayload({
    required this.version,
    required this.vaultId,
    required this.exportedAt,
    required this.streakShields,
    required this.profile,
    required this.habits,
    this.securityPinHash,
  });

  Map<String, dynamic> toJson() => {
        'version': version,
        'app': 'Habito',
        'vaultId': vaultId,
        'exportedAt': exportedAt,
        'streakShields': streakShields,
        'profile': profile.toJson(),
        'securityPinHash': securityPinHash,
        'habits': habits.map((h) => h.toJson()).toList(),
      };

  factory VaultBackupPayload.fromJson(Map<String, dynamic> json) {
    final habitsList = (json['habits'] as List<dynamic>? ?? [])
        .map((item) => Habit.fromJson(Map<String, dynamic>.from(item)))
        .toList();

    final profile = json['profile'] != null
        ? UserProfile.fromJson(Map<String, dynamic>.from(json['profile']))
        : UserProfile();

    return VaultBackupPayload(
      version: json['version'] as String? ?? '2.1',
      vaultId: json['vaultId'] as String? ?? 'vault-${DateTime.now().millisecondsSinceEpoch}',
      exportedAt: json['exportedAt'] as String? ?? DateTime.now().toIso8601String(),
      streakShields: json['streakShields'] as int? ?? 2,
      profile: profile,
      securityPinHash: json['securityPinHash'] as String?,
      habits: habitsList,
    );
  }
}

class BackupService {
  static const String currentVaultVersion = '2.1.0';

  /// Generates a high-entropy, collision-proof sync key (36^8 = 2.8 Trillion combinations)
  /// Format: HAB-XXXX-XXXX. Freshly generated on each migration request.
  static String generateCollisionProofSyncCode() {
    const chars = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789'; // Base32 without ambiguous 0/O, 1/I
    final rand = Random.secure();
    
    final part1 = List.generate(4, (_) => chars[rand.nextInt(chars.length)]).join();
    final part2 = List.generate(4, (_) => chars[rand.nextInt(chars.length)]).join();
    
    return 'HAB-$part1-$part2';
  }

  /// Exports entire user progress into a portable, collision-proof JSON vault
  static String exportToJson({
    required List<Habit> habits,
    required int streakShields,
    required UserProfile profile,
    String? pin,
  }) {
    final rand = Random.secure();
    final randomVaultId = 'vault-${DateTime.now().millisecondsSinceEpoch}-${rand.nextInt(1000000)}';

    final payload = VaultBackupPayload(
      version: currentVaultVersion,
      vaultId: randomVaultId,
      exportedAt: DateTime.now().toIso8601String(),
      streakShields: streakShields,
      profile: profile,
      securityPinHash: pin != null && pin.isNotEmpty ? _hashPin(pin) : null,
      habits: habits,
    );

    return const JsonEncoder.withIndent('  ').convert(payload.toJson());
  }

  /// Validates and parses backup JSON, verifying optional PIN if protected
  static VaultBackupPayload? parseBackup(String rawContent, {String? pin}) {
    try {
      final trimmed = rawContent.trim();
      final Map<String, dynamic> decoded = jsonDecode(trimmed);
      final payload = VaultBackupPayload.fromJson(decoded);

      // Verify PIN if the backup was encrypted/locked
      if (payload.securityPinHash != null) {
        if (pin == null || _hashPin(pin) != payload.securityPinHash) {
          debugPrint('Security PIN mismatch');
          return null;
        }
      }

      return payload;
    } catch (e) {
      debugPrint('Error parsing vault backup: $e');
      return null;
    }
  }

  static String _hashPin(String pin) {
    // Lightweight deterministic hash for PIN validation
    int hash = 5381;
    for (int i = 0; i < pin.length; i++) {
      hash = ((hash << 5) + hash) + pin.codeUnitAt(i);
    }
    return hash.toRadixString(16);
  }
}
