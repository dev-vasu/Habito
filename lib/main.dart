import 'package:flutter/material.dart';
import 'pages/habitsPage.dart';
import 'pages/homePage.dart';
import 'pages/progressPage.dart';
import 'services/habit_service.dart';
import 'services/lists.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  final habitService = HabitService();
  runApp(
    HabitScope(
      service: habitService,
      child: const MyApp(),
    ),
  );
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Habito',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        useMaterial3: true,
        scaffoldBackgroundColor: NeoBrutalism.background,
        colorScheme: const ColorScheme.light(
          primary: NeoBrutalism.black,
          secondary: NeoBrutalism.yellow,
          background: NeoBrutalism.background,
          surface: NeoBrutalism.surface,
          onPrimary: Colors.white,
          onSurface: NeoBrutalism.black,
        ),
        appBarTheme: const AppBarTheme(
          backgroundColor: NeoBrutalism.background,
          elevation: 0,
        ),
      ),
      home: const NavigationScreen(
        initialIndex: 0,
      ),
    );
  }
}

class NavigationScreen extends StatefulWidget {
  final int initialIndex;
  const NavigationScreen({Key? key, this.initialIndex = 0}) : super(key: key);

  @override
  State<NavigationScreen> createState() => _NavigationScreenState();
}

class _NavigationScreenState extends State<NavigationScreen> {
  late int _currentIndex;

  final List<Widget> _screens = const [
    HomePage(),
    ProgressPage(),
    Habitspage(),
  ];

  @override
  void initState() {
    super.initState();
    _currentIndex = widget.initialIndex;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: IndexedStack(
        index: _currentIndex,
        children: _screens,
      ),
      bottomNavigationBar: SafeArea(
        child: Container(
          margin: const EdgeInsets.fromLTRB(16, 0, 16, 12),
          padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
          decoration: NeoBrutalism.box(
            backgroundColor: Colors.white,
            radius: 24,
            borderWidth: 2.5,
            shadowOffset: const Offset(3, 3),
          ),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceAround,
            children: [
              _buildNavItem(0, Icons.bolt, 'HOME'),
              _buildNavItem(1, Icons.pie_chart, 'PROGRESS'),
              _buildNavItem(2, Icons.trending_up, 'TRENDS'),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildNavItem(int index, IconData icon, String label) {
    final isSelected = _currentIndex == index;
    return GestureDetector(
      onTap: () {
        setState(() {
          _currentIndex = index;
        });
      },
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 150),
        padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
        decoration: isSelected
            ? BoxDecoration(
                color: NeoBrutalism.black,
                borderRadius: BorderRadius.circular(16),
                border: Border.all(color: NeoBrutalism.black, width: 2),
                boxShadow: const [
                  BoxShadow(
                    color: NeoBrutalism.yellow,
                    offset: Offset(2, 2),
                    blurRadius: 0,
                  )
                ],
              )
            : BoxDecoration(
                color: Colors.transparent,
                borderRadius: BorderRadius.circular(16),
              ),
        child: Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            Icon(
              icon,
              size: 18,
              color: isSelected ? Colors.white : NeoBrutalism.black,
            ),
            if (isSelected) ...[
              const SizedBox(width: 6),
              Text(
                label,
                style: const TextStyle(
                  color: Colors.white,
                  fontWeight: FontWeight.w900,
                  fontSize: 12,
                  letterSpacing: 0.5,
                ),
              ),
            ],
          ],
        ),
      ),
    );
  }
}
