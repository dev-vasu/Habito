import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:habito/main.dart';
import 'package:habito/services/habit_service.dart';

void main() {
  testWidgets('Habito Neo-Brutalist app smoke test', (WidgetTester tester) async {
    final habitService = HabitService();

    await tester.pumpWidget(
      HabitScope(
        service: habitService,
        child: const MyApp(),
      ),
    );

    // Verify bottom navigation bar items
    expect(find.text('HOME'), findsOneWidget);

    // Verify Add Habit FAB is present
    expect(find.byType(FloatingActionButton), findsOneWidget);
  });
}
