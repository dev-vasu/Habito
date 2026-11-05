import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:habito/main.dart';
import 'package:habito/services/habit_service.dart';

void main() {
  testWidgets('Habito app smoke test', (WidgetTester tester) async {
    final habitService = HabitService();

    await tester.pumpWidget(
      HabitScope(
        service: habitService,
        child: const MyApp(),
      ),
    );

    // Verify bottom navigation bar items
    expect(find.text('Home'), findsOneWidget);
    expect(find.text('Progress'), findsOneWidget);
    expect(find.text('Trends'), findsOneWidget);

    // Verify Add Habit FAB is present
    expect(find.byType(FloatingActionButton), findsOneWidget);
  });
}
