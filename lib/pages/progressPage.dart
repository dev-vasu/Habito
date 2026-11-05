import 'package:flutter/material.dart';
import '../models/habit.dart';
import '../services/habit_service.dart';
import '../services/lists.dart';

class ProgressPage extends StatefulWidget {
  const ProgressPage({Key? key}) : super(key: key);

  @override
  State<ProgressPage> createState() => _ProgressPageState();
}

class _ProgressPageState extends State<ProgressPage> {
  @override
  Widget build(BuildContext context) {
    final service = HabitScope.of(context);
    final topHabits = service.topHabitsThisWeek;
    final worstHabits = service.worstHabitsThisWeek;
    final overallPct = service.overallWeeklyPercentage;
    final total = service.totalHabits;

    int highestStreak = 0;
    for (final h in service.habits) {
      if (h.currentStreak > highestStreak) highestStreak = h.currentStreak;
    }

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
                    color: NeoBrutalism.purple,
                    radius: 8,
                  ),
                  child: const Text(
                    'INTELLIGENCE',
                    style: TextStyle(
                      color: Colors.white,
                      fontWeight: FontWeight.w900,
                      fontSize: 11,
                      letterSpacing: 0.5,
                    ),
                  ),
                ),
                Text(
                  'OVERALL: $overallPct%',
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
              'EFFORT AUDIT.',
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
              'Real data. Zero excuses. Track your momentum.',
              style: TextStyle(
                fontSize: 13,
                fontWeight: FontWeight.w700,
                color: Color(0xFF666666),
              ),
            ),
            const SizedBox(height: 20),

            // 3 Stat Boxes
            Row(
              children: [
                Expanded(
                  child: _buildBrutalStat(
                    title: 'WEEKLY RATE',
                    value: '$overallPct%',
                    color: NeoBrutalism.green,
                  ),
                ),
                const SizedBox(width: 10),
                Expanded(
                  child: _buildBrutalStat(
                    title: 'BEST STREAK',
                    value: '${highestStreak}d',
                    color: NeoBrutalism.orange,
                  ),
                ),
                const SizedBox(width: 10),
                Expanded(
                  child: _buildBrutalStat(
                    title: 'COMPLETED',
                    value: '${service.completedTodayCount}/$total',
                    color: NeoBrutalism.blue,
                  ),
                ),
              ],
            ),
            const SizedBox(height: 24),

            // Top Habits Section
            const Text(
              'TOP PROTOCOLS',
              style: TextStyle(
                fontSize: 14,
                fontWeight: FontWeight.w900,
                letterSpacing: 0.5,
                color: NeoBrutalism.black,
              ),
            ),
            const SizedBox(height: 12),

            if (topHabits.isEmpty)
              Container(
                padding: const EdgeInsets.all(24),
                decoration: NeoBrutalism.box(
                  backgroundColor: Colors.white,
                  radius: 18,
                ),
                child: const Center(
                  child: Text(
                    'NO LOGS RECORDED YET',
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
                itemCount: topHabits.length > 3 ? 3 : topHabits.length,
                itemBuilder: (context, index) {
                  final habit = topHabits[index];
                  final pct = (habit.weeklyCompletionRate * 100).round();

                  return Container(
                    margin: const EdgeInsets.only(bottom: 10),
                    padding: const EdgeInsets.symmetric(
                        horizontal: 14, vertical: 12),
                    decoration: NeoBrutalism.box(
                      backgroundColor: Colors.white,
                      radius: 16,
                      borderWidth: 2.5,
                      shadowOffset: const Offset(3, 3),
                    ),
                    child: Row(
                      children: [
                        Container(
                          width: 44,
                          height: 44,
                          decoration: BoxDecoration(
                            color: habit.color,
                            borderRadius: BorderRadius.circular(12),
                            border: Border.all(
                                color: NeoBrutalism.black, width: 2),
                          ),
                          child: Center(
                            child: Text(
                              '$pct%',
                              style: const TextStyle(
                                fontSize: 13,
                                fontWeight: FontWeight.w900,
                                color: NeoBrutalism.black,
                              ),
                            ),
                          ),
                        ),
                        const SizedBox(width: 14),
                        Expanded(
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text(
                                habit.title,
                                style: const TextStyle(
                                  fontSize: 15,
                                  fontWeight: FontWeight.w900,
                                  color: NeoBrutalism.black,
                                ),
                              ),
                              Text(
                                '${habit.currentStreak} day streak • 7-day consistency',
                                style: const TextStyle(
                                  fontSize: 11,
                                  fontWeight: FontWeight.w700,
                                  color: Color(0xFF777777),
                                ),
                              ),
                            ],
                          ),
                        ),
                        Icon(habit.icon,
                            color: NeoBrutalism.black, size: 22),
                      ],
                    ),
                  );
                },
              ),
            const SizedBox(height: 20),

            // Focus Section
            const Text(
              'NEEDS REINFORCEMENT',
              style: TextStyle(
                fontSize: 14,
                fontWeight: FontWeight.w900,
                letterSpacing: 0.5,
                color: NeoBrutalism.black,
              ),
            ),
            const SizedBox(height: 12),

            if (worstHabits.isNotEmpty)
              ListView.builder(
                shrinkWrap: true,
                physics: const NeverScrollableScrollPhysics(),
                itemCount: worstHabits.length > 2 ? 2 : worstHabits.length,
                itemBuilder: (context, index) {
                  final habit = worstHabits[index];
                  final pct = (habit.weeklyCompletionRate * 100).round();

                  return Container(
                    margin: const EdgeInsets.only(bottom: 10),
                    padding: const EdgeInsets.symmetric(
                        horizontal: 14, vertical: 12),
                    decoration: NeoBrutalism.box(
                      backgroundColor: NeoBrutalism.yellow,
                      radius: 16,
                      borderWidth: 2.5,
                      shadowOffset: const Offset(3, 3),
                    ),
                    child: Row(
                      children: [
                        Container(
                          width: 44,
                          height: 44,
                          decoration: BoxDecoration(
                            color: Colors.white,
                            borderRadius: BorderRadius.circular(12),
                            border: Border.all(
                                color: NeoBrutalism.black, width: 2),
                          ),
                          child: Center(
                            child: Text(
                              '$pct%',
                              style: const TextStyle(
                                fontSize: 13,
                                fontWeight: FontWeight.w900,
                                color: NeoBrutalism.black,
                              ),
                            ),
                          ),
                        ),
                        const SizedBox(width: 14),
                        Expanded(
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text(
                                habit.title,
                                style: const TextStyle(
                                  fontSize: 15,
                                  fontWeight: FontWeight.w900,
                                  color: NeoBrutalism.black,
                                ),
                              ),
                              const Text(
                                'Log today to break the friction barrier',
                                style: TextStyle(
                                  fontSize: 11,
                                  fontWeight: FontWeight.w800,
                                  color: NeoBrutalism.black,
                                ),
                              ),
                            ],
                          ),
                        ),
                        const Icon(Icons.arrow_forward,
                            color: NeoBrutalism.black, size: 20),
                      ],
                    ),
                  );
                },
              ),
          ],
        ),
      ),
    );
  }

  Widget _buildBrutalStat({
    required String title,
    required String value,
    required Color color,
  }) {
    return Container(
      padding: const EdgeInsets.symmetric(vertical: 14, horizontal: 8),
      decoration: NeoBrutalism.box(
        backgroundColor: color,
        radius: 16,
        borderWidth: 2.5,
        shadowOffset: const Offset(3, 3),
      ),
      child: Column(
        children: [
          Text(
            value,
            style: const TextStyle(
              fontSize: 20,
              fontWeight: FontWeight.w900,
              color: NeoBrutalism.black,
            ),
          ),
          const SizedBox(height: 2),
          Text(
            title,
            textAlign: TextAlign.center,
            style: const TextStyle(
              fontSize: 9,
              fontWeight: FontWeight.w900,
              color: NeoBrutalism.black,
              letterSpacing: 0.5,
            ),
          ),
        ],
      ),
    );
  }
}
