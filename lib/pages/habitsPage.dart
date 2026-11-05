import 'package:flutter/material.dart';
import '../services/chartsBuilder.dart';
import '../services/habit_service.dart';
import '../services/lists.dart';

class Habitspage extends StatefulWidget {
  const Habitspage({Key? key}) : super(key: key);

  @override
  State<Habitspage> createState() => _HabitspageState();
}

class _HabitspageState extends State<Habitspage> {
  @override
  Widget build(BuildContext context) {
    final service = HabitScope.of(context);
    final habits = service.habits;

    return Scaffold(
      backgroundColor: NeoBrutalism.background,
      body: SafeArea(
        child: ListView(
          padding: const EdgeInsets.fromLTRB(16, 16, 16, 80),
          children: [
            // Header
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Container(
                  padding:
                      const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                  decoration: NeoBrutalism.badge(
                    color: NeoBrutalism.blue,
                    radius: 8,
                  ),
                  child: const Text(
                    'TRENDS',
                    style: TextStyle(
                      color: Colors.white,
                      fontWeight: FontWeight.w900,
                      fontSize: 11,
                      letterSpacing: 0.5,
                    ),
                  ),
                ),
                Text(
                  '${habits.length} METRICS',
                  style: const TextStyle(
                    fontWeight: FontWeight.w900,
                    fontSize: 13,
                    color: NeoBrutalism.black,
                  ),
                ),
              ],
            ),
            const SizedBox(height: 16),

            const Text(
              'MOMENTUM LOGS.',
              style: TextStyle(
                fontSize: 34,
                fontWeight: FontWeight.w900,
                color: NeoBrutalism.black,
                letterSpacing: -1,
                height: 1.1,
              ),
            ),
            const SizedBox(height: 4),
            const Text(
              '7-day performance charts for each active protocol.',
              style: TextStyle(
                fontSize: 13,
                fontWeight: FontWeight.w700,
                color: Color(0xFF666666),
              ),
            ),
            const SizedBox(height: 20),

            if (habits.isEmpty)
              Container(
                padding: const EdgeInsets.all(32),
                decoration: NeoBrutalism.box(
                  backgroundColor: Colors.white,
                  radius: 20,
                  shadowOffset: const Offset(4, 4),
                ),
                child: const Center(
                  child: Text(
                    'NO ACTIVE PROTOCOLS FOUND',
                    style: TextStyle(
                      fontWeight: FontWeight.w900,
                      color: NeoBrutalism.black,
                    ),
                  ),
                ),
              )
            else
              ListView.builder(
                shrinkWrap: true,
                physics: const NeverScrollableScrollPhysics(),
                itemCount: habits.length,
                itemBuilder: (context, index) {
                  final habit = habits[index];
                  return HabitChartCard(habit: habit);
                },
              ),
          ],
        ),
      ),
    );
  }
}
