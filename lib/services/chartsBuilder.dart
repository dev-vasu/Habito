import 'package:fl_chart/fl_chart.dart';
import 'package:flutter/material.dart';
import '../models/habit.dart';
import 'lists.dart';

class HabitChartCard extends StatelessWidget {
  final Habit habit;

  const HabitChartCard({
    Key? key,
    required this.habit,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final last7Days = habit.last7DaysData;
    final completionPct = (habit.weeklyCompletionRate * 100).round();
    final streak = habit.currentStreak;
    final primaryColor = habit.color;

    final now = DateTime.now();
    final List<String> dayLabels = [];
    final weekDayNames = ['M', 'T', 'W', 'T', 'F', 'S', 'S'];
    for (int i = 6; i >= 0; i--) {
      final d = now.subtract(Duration(days: i));
      dayLabels.add(weekDayNames[d.weekday - 1]);
    }

    final List<FlSpot> spots = [];
    double runningSum = 0;
    for (int i = 0; i < last7Days.length; i++) {
      runningSum += last7Days[i];
      final double score = ((runningSum / (i + 1)) * 100).clamp(0.0, 100.0);
      spots.add(FlSpot(i.toDouble(), score));
    }

    return Container(
      margin: const EdgeInsets.only(bottom: 16),
      padding: const EdgeInsets.all(16),
      decoration: NeoBrutalism.box(
        backgroundColor: Colors.white,
        radius: 20,
        borderWidth: 2.5,
        shadowOffset: const Offset(4, 4),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Header Row
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Row(
                children: [
                  Container(
                    padding: const EdgeInsets.all(8),
                    decoration: NeoBrutalism.badge(
                      color: primaryColor,
                      radius: 10,
                    ),
                    child: Icon(habit.icon, size: 20, color: NeoBrutalism.black),
                  ),
                  const SizedBox(width: 12),
                  Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        habit.title,
                        style: const TextStyle(
                          fontSize: 16,
                          fontWeight: FontWeight.w900,
                          color: NeoBrutalism.black,
                        ),
                      ),
                      Text(
                        habit.description.isNotEmpty
                            ? habit.description
                            : 'Daily protocol',
                        style: const TextStyle(
                          fontSize: 11,
                          fontWeight: FontWeight.w700,
                          color: Color(0xFF777777),
                        ),
                      ),
                    ],
                  ),
                ],
              ),
              Container(
                padding:
                    const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                decoration: NeoBrutalism.badge(
                  color: NeoBrutalism.yellow,
                  radius: 8,
                ),
                child: Text(
                  '$completionPct%',
                  style: const TextStyle(
                    fontSize: 13,
                    fontWeight: FontWeight.w900,
                    color: NeoBrutalism.black,
                  ),
                ),
              ),
            ],
          ),
          const SizedBox(height: 16),

          // Chart Frame
          Container(
            height: 140,
            padding: const EdgeInsets.fromLTRB(10, 12, 10, 4),
            decoration: BoxDecoration(
              color: NeoBrutalism.background,
              borderRadius: BorderRadius.circular(14),
              border: Border.all(color: NeoBrutalism.black, width: 2),
            ),
            child: LineChart(
              LineChartData(
                minX: 0,
                maxX: 6,
                minY: 0,
                maxY: 100,
                gridData: FlGridData(
                  show: true,
                  drawVerticalLine: false,
                  horizontalInterval: 50,
                  getDrawingHorizontalLine: (value) => const FlLine(
                    color: Color(0xFFDDDDDD),
                    strokeWidth: 1.5,
                    dashArray: [4, 4],
                  ),
                ),
                titlesData: FlTitlesData(
                  topTitles: const AxisTitles(
                    sideTitles: SideTitles(showTitles: false),
                  ),
                  rightTitles: const AxisTitles(
                    sideTitles: SideTitles(showTitles: false),
                  ),
                  leftTitles: AxisTitles(
                    sideTitles: SideTitles(
                      showTitles: true,
                      reservedSize: 32,
                      interval: 50,
                      getTitlesWidget: (value, meta) {
                        return Text(
                          '${value.toInt()}%',
                          style: const TextStyle(
                            fontSize: 10,
                            color: NeoBrutalism.black,
                            fontWeight: FontWeight.w900,
                          ),
                        );
                      },
                    ),
                  ),
                  bottomTitles: AxisTitles(
                    sideTitles: SideTitles(
                      showTitles: true,
                      reservedSize: 22,
                      interval: 1,
                      getTitlesWidget: (value, meta) {
                        final index = value.toInt();
                        if (index >= 0 && index < dayLabels.length) {
                          return Text(
                            dayLabels[index],
                            style: const TextStyle(
                              fontSize: 11,
                              fontWeight: FontWeight.w900,
                              color: NeoBrutalism.black,
                            ),
                          );
                        }
                        return const SizedBox.shrink();
                      },
                    ),
                  ),
                ),
                borderData: FlBorderData(show: false),
                lineBarsData: [
                  LineChartBarData(
                    isCurved: false, // Angular, brutalist lines!
                    color: NeoBrutalism.black,
                    barWidth: 3.5,
                    isStrokeCapRound: true,
                    dotData: FlDotData(
                      show: true,
                      getDotPainter: (spot, percent, barData, index) {
                        final isCompleted =
                            index < last7Days.length && last7Days[index] > 0;
                        return FlDotCirclePainter(
                          radius: isCompleted ? 5 : 3,
                          color: isCompleted ? primaryColor : Colors.white,
                          strokeWidth: 2,
                          strokeColor: NeoBrutalism.black,
                        );
                      },
                    ),
                    spots: spots,
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}
