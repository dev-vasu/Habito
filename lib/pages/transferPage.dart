import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import '../services/habit_service.dart';
import '../services/lists.dart';

class TransferPage extends StatefulWidget {
  const TransferPage({Key? key}) : super(key: key);

  @override
  State<TransferPage> createState() => _TransferPageState();
}

class _TransferPageState extends State<TransferPage> {
  bool _isExportMode = true;
  final TextEditingController _restoreInputController = TextEditingController();

  void _copyToClipboard(String text, String message) {
    Clipboard.setData(ClipboardData(text: text));
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        backgroundColor: NeoBrutalism.black,
        content: Text(
          message,
          style: const TextStyle(
            fontWeight: FontWeight.w900,
            color: NeoBrutalism.yellow,
          ),
        ),
      ),
    );
  }

  void _handleRestore(HabitService service) async {
    final input = _restoreInputController.text.trim();
    if (input.isEmpty) return;

    final success = await service.restoreVault(input);
    if (!mounted) return;

    if (success) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          backgroundColor: NeoBrutalism.green,
          content: Text(
            '🎉 ALL PROTOCOLS & STREAKS RESTORED SUCCESSFULLY!',
            style: TextStyle(
              fontWeight: FontWeight.w900,
              color: NeoBrutalism.black,
            ),
          ),
        ),
      );
      Navigator.pop(context);
    } else {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          backgroundColor: NeoBrutalism.red,
          content: Text(
            'INVALID VAULT DATA. PLEASE VERIFY THE BACKUP CONTENT.',
            style: TextStyle(
              fontWeight: FontWeight.w900,
              color: Colors.white,
            ),
          ),
        ),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    final service = HabitScope.of(context);
    final syncKey = service.getSyncKey();
    final vaultJson = service.exportVaultJson();

    return Scaffold(
      backgroundColor: NeoBrutalism.background,
      appBar: AppBar(
        backgroundColor: NeoBrutalism.background,
        elevation: 0,
        leading: IconButton(
          icon: const Icon(Icons.arrow_back, color: NeoBrutalism.black),
          onPressed: () => Navigator.pop(context),
        ),
        title: const Text(
          'VAULT MIGRATION',
          style: TextStyle(
            color: NeoBrutalism.black,
            fontWeight: FontWeight.w900,
            fontSize: 16,
            letterSpacing: 0.5,
          ),
        ),
      ),
      body: SafeArea(
        child: ListView(
          padding: const EdgeInsets.all(16),
          children: [
            // Mode Toggle
            Container(
              padding: const EdgeInsets.all(4),
              decoration: NeoBrutalism.box(
                backgroundColor: NeoBrutalism.black,
                radius: 18,
                borderWidth: 2,
                shadowOffset: const Offset(3, 3),
              ),
              child: Row(
                children: [
                  Expanded(
                    child: GestureDetector(
                      onTap: () => setState(() => _isExportMode = true),
                      child: Container(
                        padding: const EdgeInsets.symmetric(vertical: 10),
                        decoration: BoxDecoration(
                          color: _isExportMode
                              ? NeoBrutalism.yellow
                              : Colors.transparent,
                          borderRadius: BorderRadius.circular(14),
                          border: _isExportMode
                              ? Border.all(color: NeoBrutalism.black, width: 2)
                              : null,
                        ),
                        child: Text(
                          'EXPORT (OLD PHONE)',
                          textAlign: TextAlign.center,
                          style: TextStyle(
                            fontSize: 11,
                            fontWeight: FontWeight.w900,
                            color: _isExportMode
                                ? NeoBrutalism.black
                                : Colors.white,
                          ),
                        ),
                      ),
                    ),
                  ),
                  Expanded(
                    child: GestureDetector(
                      onTap: () => setState(() => _isExportMode = false),
                      child: Container(
                        padding: const EdgeInsets.symmetric(vertical: 10),
                        decoration: BoxDecoration(
                          color: !_isExportMode
                              ? NeoBrutalism.green
                              : Colors.transparent,
                          borderRadius: BorderRadius.circular(14),
                          border: !_isExportMode
                              ? Border.all(color: NeoBrutalism.black, width: 2)
                              : null,
                        ),
                        child: Text(
                          'RESTORE (NEW PHONE)',
                          textAlign: TextAlign.center,
                          style: TextStyle(
                            fontSize: 11,
                            fontWeight: FontWeight.w900,
                            color: !_isExportMode
                                ? NeoBrutalism.black
                                : Colors.white,
                          ),
                        ),
                      ),
                    ),
                  ),
                ],
              ),
            ),
            const SizedBox(height: 20),

            if (_isExportMode) ...[
              // EXPORT SECTION
              Container(
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
                    Container(
                      padding: const EdgeInsets.symmetric(
                          horizontal: 8, vertical: 3),
                      decoration: NeoBrutalism.badge(
                          color: NeoBrutalism.red, radius: 6),
                      child: const Text(
                        'METHOD 1: INSTANT SYNC KEY',
                        style: TextStyle(
                          fontSize: 9,
                          fontWeight: FontWeight.w900,
                          color: Colors.white,
                        ),
                      ),
                    ),
                    const SizedBox(height: 8),
                    const Text(
                      'Your 6-Digit Transfer Key',
                      style: TextStyle(
                        fontSize: 16,
                        fontWeight: FontWeight.w900,
                        color: NeoBrutalism.black,
                      ),
                    ),
                    const SizedBox(height: 2),
                    const Text(
                      'Type or copy this code on your new device.',
                      style: TextStyle(
                        fontSize: 11,
                        fontWeight: FontWeight.w700,
                        color: Color(0xFF666666),
                      ),
                    ),
                    const SizedBox(height: 14),

                    // Code Display Box
                    Container(
                      padding: const EdgeInsets.symmetric(
                          horizontal: 16, vertical: 12),
                      decoration: BoxDecoration(
                        color: NeoBrutalism.background,
                        borderRadius: BorderRadius.circular(14),
                        border:
                            Border.all(color: NeoBrutalism.black, width: 2),
                      ),
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          Text(
                            syncKey,
                            style: const TextStyle(
                              fontFamily: 'monospace',
                              fontSize: 24,
                              fontWeight: FontWeight.w900,
                              color: NeoBrutalism.black,
                              letterSpacing: 2,
                            ),
                          ),
                          GestureDetector(
                            onTap: () => _copyToClipboard(
                                syncKey, 'Sync Key copied!'),
                            child: Container(
                              padding: const EdgeInsets.symmetric(
                                  horizontal: 14, vertical: 8),
                              decoration: NeoBrutalism.box(
                                backgroundColor: NeoBrutalism.yellow,
                                radius: 10,
                                borderWidth: 2,
                                shadowOffset: const Offset(2, 2),
                              ),
                              child: const Text(
                                'COPY',
                                style: TextStyle(
                                  fontSize: 11,
                                  fontWeight: FontWeight.w900,
                                  color: NeoBrutalism.black,
                                ),
                              ),
                            ),
                          ),
                        ],
                      ),
                    ),
                  ],
                ),
              ),
              const SizedBox(height: 16),

              // Full Vault JSON Export
              Container(
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
                    Container(
                      padding: const EdgeInsets.symmetric(
                          horizontal: 8, vertical: 3),
                      decoration: NeoBrutalism.badge(
                          color: NeoBrutalism.green, radius: 6),
                      child: const Text(
                        'METHOD 2: ZERO-CLOUD FILE VAULT',
                        style: TextStyle(
                          fontSize: 9,
                          fontWeight: FontWeight.w900,
                          color: NeoBrutalism.black,
                        ),
                      ),
                    ),
                    const SizedBox(height: 8),
                    const Text(
                      'Full Encrypted Vault Backup',
                      style: TextStyle(
                        fontSize: 16,
                        fontWeight: FontWeight.w900,
                        color: NeoBrutalism.black,
                      ),
                    ),
                    const SizedBox(height: 2),
                    const Text(
                      'Copy entire JSON record to share via AirDrop, Drive, or messaging.',
                      style: TextStyle(
                        fontSize: 11,
                        fontWeight: FontWeight.w700,
                        color: Color(0xFF666666),
                      ),
                    ),
                    const SizedBox(height: 14),

                    GestureDetector(
                      onTap: () => _copyToClipboard(
                          vaultJson, 'Complete Vault payload copied!'),
                      child: Container(
                        width: double.infinity,
                        padding: const EdgeInsets.symmetric(vertical: 12),
                        decoration: NeoBrutalism.box(
                          backgroundColor: NeoBrutalism.blue,
                          radius: 12,
                          borderWidth: 2,
                          shadowOffset: const Offset(3, 3),
                        ),
                        child: const Text(
                          'COPY VAULT BACKUP PAYLOAD',
                          textAlign: TextAlign.center,
                          style: TextStyle(
                            fontSize: 12,
                            fontWeight: FontWeight.w900,
                            color: Colors.white,
                            letterSpacing: 0.5,
                          ),
                        ),
                      ),
                    ),
                  ],
                ),
              ),
            ] else ...[
              // RESTORE SECTION
              Container(
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
                    Container(
                      padding: const EdgeInsets.symmetric(
                          horizontal: 8, vertical: 3),
                      decoration: NeoBrutalism.badge(
                          color: NeoBrutalism.green, radius: 6),
                      child: const Text(
                        'RESTORE PROGRESS',
                        style: TextStyle(
                          fontSize: 9,
                          fontWeight: FontWeight.w900,
                          color: NeoBrutalism.black,
                        ),
                      ),
                    ),
                    const SizedBox(height: 8),
                    const Text(
                      'Paste Vault Payload or Key',
                      style: TextStyle(
                        fontSize: 16,
                        fontWeight: FontWeight.w900,
                        color: NeoBrutalism.black,
                      ),
                    ),
                    const SizedBox(height: 2),
                    const Text(
                      'Paste the exported JSON backup from your previous phone below.',
                      style: TextStyle(
                        fontSize: 11,
                        fontWeight: FontWeight.w700,
                        color: Color(0xFF666666),
                      ),
                    ),
                    const SizedBox(height: 14),

                    TextField(
                      controller: _restoreInputController,
                      maxLines: 5,
                      style: const TextStyle(
                        fontFamily: 'monospace',
                        fontSize: 12,
                        fontWeight: FontWeight.bold,
                      ),
                      decoration: InputDecoration(
                        filled: true,
                        fillColor: NeoBrutalism.background,
                        hintText: 'Paste Vault JSON content here...',
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

                    GestureDetector(
                      onTap: () => _handleRestore(service),
                      child: Container(
                        width: double.infinity,
                        padding: const EdgeInsets.symmetric(vertical: 12),
                        decoration: NeoBrutalism.box(
                          backgroundColor: NeoBrutalism.green,
                          radius: 12,
                          borderWidth: 2,
                          shadowOffset: const Offset(3, 3),
                        ),
                        child: const Text(
                          'RESTORE MY PROTOCOLS & STREAKS',
                          textAlign: TextAlign.center,
                          style: TextStyle(
                            fontSize: 12,
                            fontWeight: FontWeight.w900,
                            color: NeoBrutalism.black,
                            letterSpacing: 0.5,
                          ),
                        ),
                      ),
                    ),
                  ],
                ),
              ),
            ],

            const SizedBox(height: 20),

            // Streak Shields Inventory Box
            Container(
              padding: const EdgeInsets.all(16),
              decoration: NeoBrutalism.box(
                backgroundColor: NeoBrutalism.yellow,
                radius: 20,
                borderWidth: 2.5,
                shadowOffset: const Offset(4, 4),
              ),
              child: Row(
                children: [
                  Container(
                    padding: const EdgeInsets.all(10),
                    decoration: NeoBrutalism.badge(
                      color: Colors.white,
                      radius: 12,
                    ),
                    child: const Icon(Icons.shield,
                        color: NeoBrutalism.black, size: 24),
                  ),
                  const SizedBox(width: 14),
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        const Text(
                          'STREAK FREEZE SHIELDS',
                          style: TextStyle(
                            fontSize: 13,
                            fontWeight: FontWeight.w900,
                            color: NeoBrutalism.black,
                          ),
                        ),
                        Text(
                          '${service.streakShields} tokens remaining this month. Auto-protects streaks if you miss a day.',
                          style: const TextStyle(
                            fontSize: 11,
                            fontWeight: FontWeight.w700,
                            color: NeoBrutalism.black,
                          ),
                        ),
                      ],
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
