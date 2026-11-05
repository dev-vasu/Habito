import 'package:flutter/material.dart';

class UserProfile {
  String name;
  String personalMotto;
  String avatarEmoji;
  int accentColorValue;

  UserProfile({
    this.name = 'Vasudev',
    this.personalMotto = 'Relentless consistency. Zero excuses.',
    this.avatarEmoji = '⚡',
    this.accentColorValue = 0xFF6BCB77, // Mint green default
  });

  Color get accentColor => Color(accentColorValue);

  Map<String, dynamic> toJson() => {
        'name': name,
        'personalMotto': personalMotto,
        'avatarEmoji': avatarEmoji,
        'accentColorValue': accentColorValue,
      };

  factory UserProfile.fromJson(Map<String, dynamic> json) => UserProfile(
        name: json['name'] as String? ?? 'Vasudev',
        personalMotto: json['personalMotto'] as String? ??
            'Relentless consistency. Zero excuses.',
        avatarEmoji: json['avatarEmoji'] as String? ?? '⚡',
        accentColorValue: json['accentColorValue'] as int? ?? 0xFF6BCB77,
      );

  UserProfile copyWith({
    String? name,
    String? personalMotto,
    String? avatarEmoji,
    int? accentColorValue,
  }) {
    return UserProfile(
      name: name ?? this.name,
      personalMotto: personalMotto ?? this.personalMotto,
      avatarEmoji: avatarEmoji ?? this.avatarEmoji,
      accentColorValue: accentColorValue ?? this.accentColorValue,
    );
  }
}
