import 'package:flutter/material.dart';
import '../models/habit.dart';
import '../services/habit_service.dart';
import '../services/lists.dart';

class HomePage extends StatefulWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  void _showAddHabitDialog(BuildContext context, HabitService service) {
    final titleController = TextEditingController();
    final descController = TextEditingController();
    IconData selectedIcon = availableHabitIcons.first.icon;
    Color selectedColor = availableHabitColors.first;

    showDialog(
      context: context,
      builder: (ctx) {
        return StatefulBuilder(
          builder: (dialogContext, setDialogState) {
            return AlertDialog(
              backgroundColor: NeoBrutalism.background,
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(24),
                side: const BorderSide(color: NeoBrutalism.black, width: 3),
              ),
              title: const Text(
                'NEW HABIT PROTOCOL',
                style: TextStyle(
                  fontWeight: FontWeight.w900,
                  fontSize: 18,
                  letterSpacing: 0.5,
                  color: NeoBrutalism.black,
                ),
              ),
              content: SingleChildScrollView(
                child: Column(
                  mainAxisSize: MainAxisSize.min,
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    TextField(
                      controller: titleController,
                      autofocus: true,
                      style: const TextStyle(fontWeight: FontWeight.w700),
                      decoration: InputDecoration(
                        filled: true,
                        fillColor: Colors.white,
                        labelText: 'Habit Title',
                        hintText: 'e.g. Read 20 pages',
                        labelStyle: const TextStyle(
                          color: NeoBrutalism.black,
                          fontWeight: FontWeight.bold,
                        ),
                        enabledBorder: OutlineInputBorder(
                          borderRadius: BorderRadius.circular(14),
                          borderSide: const BorderSide(
                              color: NeoBrutalism.black, width: 2),
                        ),
                        focusedBorder: OutlineInputBorder(
                          borderRadius: BorderRadius.circular(14),
                          borderSide: const BorderSide(
                              color: NeoBrutalism.black, width: 2.5),
                        ),
                      ),
                    ),
                    const SizedBox(height: 14),
                    TextField(
                      controller: descController,
                      style: const TextStyle(fontWeight: FontWeight.w600),
                      decoration: InputDecoration(
                        filled: true,
                        fillColor: Colors.white,
                        labelText: 'Rule / Target (Optional)',
                        hintText: 'e.g. No phone in bedroom',
                        labelStyle: const TextStyle(
                          color: NeoBrutalism.black,
                          fontWeight: FontWeight.bold,
                        ),
                        enabledBorder: OutlineInputBorder(
                          borderRadius: BorderRadius.circular(14),
                          borderSide: const BorderSide(
                              color: NeoBrutalism.black, width: 2),
                        ),
                        focusedBorder: OutlineInputBorder(
                          borderRadius: BorderRadius.circular(14),
                          borderSide: const BorderSide(
                              color: NeoBrutalism.black, width: 2.5),
                        ),
                      ),
                    ),
                    const SizedBox(height: 16),
                    const Text(
                      'ICON BADGE',
                      style: TextStyle(
                        fontSize: 11,
                        fontWeight: FontWeight.w900,
                        letterSpacing: 0.5,
                        color: NeoBrutalism.black,
                      ),
                    ),
                    const SizedBox(height: 8),
                    SizedBox(
                      height: 52,
                      child: ListView.builder(
                        scrollDirection: Axis.horizontal,
                        itemCount: availableHabitIcons.length,
                        itemBuilder: (context, index) {
                          final item = availableHabitIcons[index];
                          final isSelected =
                              selectedIcon.codePoint == item.icon.codePoint;
                          return GestureDetector(
                            onTap: () {
                              setDialogState(() {
                                selectedIcon = item.icon;
                              });
                            },
                            child: Container(
                              margin: const EdgeInsets.only(right: 8),
                              padding: const EdgeInsets.all(10),
                              decoration: BoxDecoration(
                                color: isSelected
                                    ? selectedColor
                                    : Colors.white,
                                borderRadius: BorderRadius.circular(12),
                                border: Border.all(
                                  color: NeoBrutalism.black,
                                  width: 2,
                                ),
                                boxShadow: isSelected
                                    ? const [
                                        BoxShadow(
                                          color: NeoBrutalism.black,
                                          offset: Offset(2, 2),
                                          blurRadius: 0,
                                        )
                                      ]
                                    : null,
                              ),
                              child: Icon(
                                item.icon,
                                color: NeoBrutalism.black,
                                size: 22,
                              ),
                            ),
                          );
                        },
                      ),
                    ),
                    const SizedBox(height: 16),
                    const Text(
                      'CHIP COLOR',
                      style: TextStyle(
                        fontSize: 11,
                        fontWeight: FontWeight.w900,
                        letterSpacing: 0.5,
                        color: NeoBrutalism.black,
                      ),
                    ),
                    const SizedBox(height: 8),
                    SizedBox(
                      height: 40,
                      child: ListView.builder(
                        scrollDirection: Axis.horizontal,
                        itemCount: availableHabitColors.length,
                        itemBuilder: (context, index) {
                          final color = availableHabitColors[index];
                          final isSelected = selectedColor.value == color.value;
                          return GestureDetector(
                            onTap: () {
                              setDialogState(() {
                                selectedColor = color;
                              });
                            },
                            child: Container(
                              margin: const EdgeInsets.only(right: 8),
                              width: 36,
                              height: 36,
                              decoration: BoxDecoration(
                                color: color,
                                borderRadius: BorderRadius.circular(10),
                                border: Border.all(
                                  color: NeoBrutalism.black,
                                  width: 2,
                                ),
                                boxShadow: isSelected
                                    ? const [
                                        BoxShadow(
                                          color: NeoBrutalism.black,
                                          offset: Offset(2, 2),
                                          blurRadius: 0,
                                        )
                                      ]
                                    : null,
                              ),
                              child: isSelected
                                  ? const Icon(Icons.check,
                                      color: NeoBrutalism.black, size: 20)
                                  : null,
                            ),
                          );
                        },
                      ),
                    ),
                  ],
                ),
              ),
              actions: [
                TextButton(
                  onPressed: () => Navigator.pop(ctx),
                  child: const Text(
                    'DISCARD',
                    style: TextStyle(
                      color: NeoBrutalism.black,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ),
                GestureDetector(
                  onTap: () {
                    final title = titleController.text.trim();
                    if (title.isEmpty) return;

                    service.addHabit(
                      title: title,
                      description: descController.text.trim(),
                      icon: selectedIcon,
                      color: selectedColor,
                    );
                    Navigator.pop(ctx);
                  },
                  child: Container(
                    padding: const EdgeInsets.symmetric(
                        horizontal: 18, vertical: 10),
                    decoration: NeoBrutalism.box(
                      backgroundColor: NeoBrutalism.green,
                      radius: 12,
                      borderWidth: 2,
                      shadowOffset: const Offset(2, 2),
                    ),
                    child: const Text(
                      'SAVE HABIT',
                      style: TextStyle(
                        fontWeight: FontWeight.w900,
                        fontSize: 13,
                        color: NeoBrutalism.black,
                      ),
                    ),
                  ),
                ),
              ],
            );
          },
        );
      },
    );
  }

  void _showDeleteDialog(
      BuildContext context, HabitService service, Habit habit) {
    showDialog(
      context: context,
      builder: (ctx) => AlertDialog(
        backgroundColor: NeoBrutalism.background,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(20),
          side: const BorderSide(color: NeoBrutalism.black, width: 2.5),
        ),
        title: const Text(
          'REMOVE HABIT?',
          style: TextStyle(
            fontWeight: FontWeight.w900,
            color: NeoBrutalism.black,
          ),
        ),
        content: Text(
          'Delete "${habit.title}" from your active protocols?',
          style: const TextStyle(fontWeight: FontWeight.w600),
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(ctx),
            child: const Text('CANCEL',
                style: TextStyle(
                    color: NeoBrutalism.black, fontWeight: FontWeight.bold)),
          ),
          GestureDetector(
            onTap: () {
              service.deleteHabit(habit.id);
              Navigator.pop(ctx);
            },
            child: Container(
              padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
              decoration: NeoBrutalism.box(
                backgroundColor: NeoBrutalism.red,
                radius: 10,
                borderWidth: 2,
                shadowOffset: const Offset(2, 2),
              ),
              child: const Text(
                'DELETE',
                style: TextStyle(
                  fontWeight: FontWeight.w900,
                  color: Colors.white,
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final service = HabitScope.of(context);
    final habits = service.habits;
    final total = service.totalHabits;
    final remaining = service.remainingTodayCount;
    final progress = service.todayProgressPercentage;
    final pct = (progress * 100).round();

    // Find best streak
    int highestStreak = 0;
    for (final h in habits) {
      if (h.currentStreak > highestStreak) highestStreak = h.currentStreak;
    }

    return Scaffold(
      floatingActionButton: FloatingActionButton(
        elevation: 0,
        backgroundColor: NeoBrutalism.black,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(18),
          side: const BorderSide(color: NeoBrutalism.black, width: 2),
        ),
        child: Container(
          decoration: const BoxDecoration(
            boxShadow: [
              BoxShadow(
                color: NeoBrutalism.yellow,
                offset: Offset(2, 2),
                blurRadius: 0,
              )
            ],
          ),
          child: const Icon(Icons.add, color: Colors.white, size: 28),
        ),
        onPressed: () => _showAddHabitDialog(context, service),
      ),
      backgroundColor: NeoBrutalism.background,
      body: SafeArea(
        child: ListView(
          padding: const EdgeInsets.fromLTRB(16, 16, 16, 80),
          children: [
            // Neo-Brutalist Header
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Container(
                  padding:
                      const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                  decoration: NeoBrutalism.badge(
                    color: NeoBrutalism.red,
                    radius: 8,
                  ),
                  child: const Text(
                    'TODAY',
                    style: TextStyle(
                      color: Colors.white,
                      fontWeight: FontWeight.w900,
                      fontSize: 11,
                      letterSpacing: 0.5,
                    ),
                  ),
                ),
                Container(
                  padding:
                      const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                  decoration: NeoBrutalism.badge(
                    color: NeoBrutalism.blue,
                    radius: 8,
                  ),
                  child: Row(
                    children: [
                      const Icon(Icons.local_fire_department,
                          color: Colors.white, size: 14),
                      const SizedBox(width: 4),
                      Text(
                        '$highestStreak STREAK',
                        style: const TextStyle(
                          color: Colors.white,
                          fontWeight: FontWeight.w900,
                          fontSize: 11,
                          letterSpacing: 0.5,
                        ),
                      ),
                    ],
                  ),
                ),
              ],
            ),
            const SizedBox(height: 16),

            // Big Bold Title
            const Text(
              'DO THE THING.',
              style: TextStyle(
                fontSize: 34,
                fontWeight: FontWeight.w900,
                color: NeoBrutalism.black,
                letterSpacing: -1,
                height: 1.1,
              ),
            ),
            const SizedBox(height: 4),
            Text(
              total == 0
                  ? 'Add your first target protocol below.'
                  : remaining == 0
                      ? 'Target crushed. 100% completed today!'
                      : 'Show up, check the box, conquer the day.',
              style: const TextStyle(
                fontSize: 13,
                fontWeight: FontWeight.w700,
                color: Color(0xFF666666),
              ),
            ),
            const SizedBox(height: 20),

            // Fuel / Progress Box
            Container(
              padding: const EdgeInsets.all(16),
              decoration: NeoBrutalism.box(
                backgroundColor: NeoBrutalism.yellow,
                radius: 20,
                borderWidth: 2.5,
                shadowOffset: const Offset(4, 4),
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      const Text(
                        "TODAY'S FUEL",
                        style: TextStyle(
                          fontSize: 13,
                          fontWeight: FontWeight.w900,
                          color: NeoBrutalism.black,
                          letterSpacing: 0.5,
                        ),
                      ),
                      Text(
                        '$pct%',
                        style: const TextStyle(
                          fontSize: 18,
                          fontWeight: FontWeight.w900,
                          color: NeoBrutalism.black,
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(height: 10),
                  // Chunky fuel meter
                  Container(
                    height: 18,
                    padding: const EdgeInsets.all(2),
                    decoration: BoxDecoration(
                      color: Colors.white,
                      borderRadius: BorderRadius.circular(8),
                      border:
                          Border.all(color: NeoBrutalism.black, width: 2),
                    ),
                    child: ClipRRect(
                      borderRadius: BorderRadius.circular(5),
                      child: LinearProgressIndicator(
                        value: progress.clamp(0.0, 1.0),
                        backgroundColor: Colors.transparent,
                        color: NeoBrutalism.black,
                      ),
                    ),
                  ),
                  const SizedBox(height: 8),
                  Text(
                    remaining == 0 && total > 0
                        ? 'All systems green. Great job!'
                        : '$remaining protocol${remaining == 1 ? '' : 's'} remaining today',
                    style: const TextStyle(
                      fontSize: 11,
                      fontWeight: FontWeight.w800,
                      color: NeoBrutalism.black,
                    ),
                  ),
                ],
              ),
            ),
            const SizedBox(height: 24),

            // Section Label
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                const Text(
                  'PROTOCOLS',
                  style: TextStyle(
                    fontSize: 14,
                    fontWeight: FontWeight.w900,
                    letterSpacing: 0.5,
                    color: NeoBrutalism.black,
                  ),
                ),
                Text(
                  '$total ACTIVE',
                  style: const TextStyle(
                    fontSize: 12,
                    fontWeight: FontWeight.w800,
                    color: Color(0xFF888888),
                  ),
                ),
              ],
            ),
            const SizedBox(height: 12),

            // Habits List
            if (habits.isEmpty)
              Container(
                padding: const EdgeInsets.all(32),
                decoration: NeoBrutalism.box(
                  backgroundColor: Colors.white,
                  radius: 20,
                  shadowOffset: const Offset(4, 4),
                ),
                child: Column(
                  children: [
                    const Icon(Icons.bolt,
                        size: 48, color: NeoBrutalism.black),
                    const SizedBox(height: 12),
                    const Text(
                      'ZERO ACTIVE HABITS',
                      style: TextStyle(
                        fontSize: 16,
                        fontWeight: FontWeight.w900,
                        color: NeoBrutalism.black,
                      ),
                    ),
                    const SizedBox(height: 6),
                    const Text(
                      'Tap the + button to initiate your daily routine.',
                      textAlign: TextAlign.center,
                      style: TextStyle(
                        fontSize: 12,
                        fontWeight: FontWeight.w600,
                        color: Color(0xFF666666),
                      ),
                    ),
                  ],
                ),
              )
            else
              ListView.builder(
                shrinkWrap: true,
                physics: const NeverScrollableScrollPhysics(),
                itemCount: habits.length,
                itemBuilder: (context, index) {
                  final habit = habits[index];
                  final isDone = habit.isCompletedToday();
                  final streak = habit.currentStreak;

                  return Container(
                    margin: const EdgeInsets.only(bottom: 12),
                    padding: const EdgeInsets.symmetric(
                        horizontal: 14, vertical: 12),
                    decoration: NeoBrutalism.box(
                      backgroundColor: Colors.white,
                      radius: 18,
                      borderWidth: 2.5,
                      shadowOffset: const Offset(4, 4),
                    ),
                    child: Row(
                      children: [
                        // Custom Brutalist Checkbox Button
                        GestureDetector(
                          onTap: () => service.toggleHabit(habit.id),
                          child: AnimatedContainer(
                            duration: const Duration(milliseconds: 150),
                            width: 32,
                            height: 32,
                            decoration: BoxDecoration(
                              color: isDone
                                  ? NeoBrutalism.green
                                  : Colors.white,
                              borderRadius: BorderRadius.circular(10),
                              border: Border.all(
                                color: NeoBrutalism.black,
                                width: 2,
                              ),
                              boxShadow: isDone
                                  ? null
                                  : const [
                                      BoxShadow(
                                        color: NeoBrutalism.black,
                                        offset: Offset(2, 2),
                                        blurRadius: 0,
                                      )
                                    ],
                            ),
                            child: isDone
                                ? const Icon(Icons.check,
                                    size: 20, color: NeoBrutalism.black)
                                : null,
                          ),
                        ),
                        const SizedBox(width: 14),

                        // Title & Subtitle
                        Expanded(
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text(
                                habit.title,
                                style: TextStyle(
                                  fontSize: 16,
                                  fontWeight: FontWeight.w900,
                                  color: NeoBrutalism.black,
                                  decoration: isDone
                                      ? TextDecoration.lineThrough
                                      : null,
                                ),
                              ),
                              const SizedBox(height: 2),
                              Text(
                                habit.description.isNotEmpty
                                    ? habit.description
                                    : 'Daily protocol',
                                maxLines: 1,
                                overflow: TextOverflow.ellipsis,
                                style: const TextStyle(
                                  fontSize: 12,
                                  fontWeight: FontWeight.w600,
                                  color: Color(0xFF777777),
                                ),
                              ),
                            ],
                          ),
                        ),

                        // Streak / Icon Chip
                        Container(
                          padding: const EdgeInsets.symmetric(
                              horizontal: 8, vertical: 4),
                          decoration: NeoBrutalism.badge(
                            color: habit.color,
                            radius: 8,
                          ),
                          child: Row(
                            mainAxisSize: MainAxisSize.min,
                            children: [
                              Icon(habit.icon,
                                  size: 14, color: NeoBrutalism.black),
                              if (streak > 0) ...[
                                const SizedBox(width: 4),
                                Text(
                                  '${streak}d',
                                  style: const TextStyle(
                                    fontSize: 10,
                                    fontWeight: FontWeight.w900,
                                    color: NeoBrutalism.black,
                                  ),
                                ),
                              ],
                            ],
                          ),
                        ),

                        // Actions menu
                        PopupMenuButton<String>(
                          icon: const Icon(Icons.more_vert,
                              color: NeoBrutalism.black),
                          shape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(14),
                            side: const BorderSide(
                                color: NeoBrutalism.black, width: 2),
                          ),
                          onSelected: (action) {
                            if (action == 'delete') {
                              _showDeleteDialog(context, service, habit);
                            }
                          },
                          itemBuilder: (context) => [
                            const PopupMenuItem(
                              value: 'delete',
                              child: Text(
                                'DELETE',
                                style: TextStyle(
                                  fontWeight: FontWeight.w900,
                                  color: NeoBrutalism.red,
                                ),
                              ),
                            ),
                          ],
                        ),
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
}
