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
  final TextEditingController _pinController = TextEditingController();
  final TextEditingController _exportPinController = TextEditingController();

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

    final pin = _pinController.text.trim();
    final success = await service.restoreVault(input, pin: pin.isNotEmpty ? pin : null);
    if (!mounted) return;

    if (success) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          backgroundColor: NeoBrutalism.green,
          content: Text(
            '🎉 ALL PROTOCOLS, PROFILE & STREAKS RESTORED SUCCESSFULLY!',
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
            'INVALID DATA OR INCORRECT PIN. PLEASE VERIFY BACKUP.',
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
    final syncKey = service.currentSyncKey;
    final vaultJson = service.exportVaultJson(
      pin: _exportPinController.text.trim().isNotEmpty
          ? _exportPinController.text.trim()
          : null,
    );

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
          'VAULT MIGRATION & SYNC',
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
            const SizedBox(height: 16),

            // Collision-Proof Guarantee Badge
            Container(
              padding: const EdgeInsets.all(12),
              decoration: BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.circular(14),
                border: Border.all(color: NeoBrutalism.black, width: 2),
                boxShadow: const [
                  BoxShadow(
                    color: NeoBrutalism.black,
                    offset: Offset(2, 2),
                    blurRadius: 0,
                  )
                ],
              ),
              child: const Row(
                children: [
                  Icon(Icons.verified_user,
                      color: NeoBrutalism.green, size: 22),
                  SizedBox(width: 10),
                  Expanded(
                    child: Text(
                      'COLLISION-PROOF VAULT: 2.8 Trillion combinations with unique device UUID. Data cannot mix between users.',
                      style: TextStyle(
                        fontSize: 10,
                        fontWeight: FontWeight.w800,
                        color: NeoBrutalism.black,
                      ),
                    ),
                  ),
                ],
              ),
            ),
            const SizedBox(height: 16),

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
                    Row(
                      mainAxisAlignment: MainAxisAlignment.spaceBetween,
                      children: [
                        Container(
                          padding: const EdgeInsets.symmetric(
                              horizontal: 8, vertical: 3),
                          decoration: NeoBrutalism.badge(
                              color: NeoBrutalism.red, radius: 6),
                          child: const Text(
                            'DYNAMIC SYNC TOKEN',
                            style: TextStyle(
                              fontSize: 9,
                              fontWeight: FontWeight.w900,
                              color: Colors.white,
                            ),
                          ),
                        ),
                        GestureDetector(
                          onTap: () {
                            service.regenerateSyncKey();
                            setState(() {});
                          },
                          child: const Row(
                            children: [
                              Icon(Icons.refresh,
                                  size: 14, color: NeoBrutalism.black),
                              SizedBox(width: 2),
                              Text(
                                'NEW CODE',
                                style: TextStyle(
                                  fontSize: 10,
                                  fontWeight: FontWeight.w900,
                                  color: NeoBrutalism.black,
                                ),
                              ),
                            ],
                          ),
                        ),
                      ],
                    ),
                    const SizedBox(height: 8),
                    const Text(
                      'High-Entropy Sync Key',
                      style: TextStyle(
                        fontSize: 16,
                        fontWeight: FontWeight.w900,
                        color: NeoBrutalism.black,
                      ),
                    ),
                    const SizedBox(height: 2),
                    const Text(
                      'Generated uniquely for this session. Safe from collisions.',
                      style: TextStyle(
                        fontSize: 11,
                        fontWeight: FontWeight.w700,
                        color: Color(0xFF666666),
                      ),
                    ),
                    const SizedBox(height: 12),

                    // Code Display Box
                    Container(
                      padding: const EdgeInsets.symmetric(
                          horizontal: 14, vertical: 12),
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
                              fontSize: 18,
                              fontWeight: FontWeight.w900,
                              color: NeoBrutalism.black,
                              letterSpacing: 1.5,
                            ),
                          ),
                          GestureDetector(
                            onTap: () => _copyToClipboard(
                                syncKey, 'Sync Key copied!'),
                            child: Container(
                              padding: const EdgeInsets.symmetric(
                                  horizontal: 12, vertical: 6),
                              decoration: NeoBrutalism.box(
                                backgroundColor: NeoBrutalism.yellow,
                                radius: 8,
                                borderWidth: 1.5,
                                shadowOffset: const Offset(2, 2),
                              ),
                              child: const Text(
                                'COPY',
                                style: TextStyle(
                                  fontSize: 10,
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

              // Full Vault JSON Export with Optional PIN
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
                          color: NeoBrutalism.blue, radius: 6),
                      child: const Text(
                        'ZERO-CLOUD DIRECT VAULT FILE',
                        style: TextStyle(
                          fontSize: 9,
                          fontWeight: FontWeight.w900,
                          color: Colors.white,
                        ),
                      ),
                    ),
                    const SizedBox(height: 8),
                    const Text(
                      'Export Encrypted Payload',
                      style: TextStyle(
                        fontSize: 16,
                        fontWeight: FontWeight.w900,
                        color: NeoBrutalism.black,
                      ),
                    ),
                    const SizedBox(height: 2),
                    const Text(
                      'Optional: Lock backup with a 4-digit PIN for double security.',
                      style: TextStyle(
                        fontSize: 11,
                        fontWeight: FontWeight.w700,
                        color: Color(0xFF666666),
                      ),
                    ),
                    const SizedBox(height: 10),

                    TextField(
                      controller: _exportPinController,
                      keyboardType: TextInputType.number,
                      maxLength: 4,
                      obscureText: true,
                      decoration: InputDecoration(
                        counterText: '',
                        filled: true,
                        fillColor: NeoBrutalism.background,
                        labelText: 'Optional 4-Digit Security PIN',
                        labelStyle: const TextStyle(
                            fontSize: 11, fontWeight: FontWeight.bold),
                        enabledBorder: OutlineInputBorder(
                          borderRadius: BorderRadius.circular(10),
                          borderSide: const BorderSide(
                              color: NeoBrutalism.black, width: 1.5),
                        ),
                        focusedBorder: OutlineInputBorder(
                          borderRadius: BorderRadius.circular(10),
                          borderSide: const BorderSide(
                              color: NeoBrutalism.black, width: 2),
                        ),
                      ),
                      onChanged: (_) => setState(() {}),
                    ),
                    const SizedBox(height: 10),

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
                          'COPY SECURE VAULT PAYLOAD',
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
                        'RESTORE PROGRESS ON NEW DEVICE',
                        style: TextStyle(
                          fontSize: 9,
                          fontWeight: FontWeight.w900,
                          color: NeoBrutalism.black,
                        ),
                      ),
                    ),
                    const SizedBox(height: 8),
                    const Text(
                      'Paste Vault Backup Payload',
                      style: TextStyle(
                        fontSize: 16,
                        fontWeight: FontWeight.w900,
                        color: NeoBrutalism.black,
                      ),
                    ),
                    const SizedBox(height: 2),
                    const Text(
                      'Paste the exported JSON backup from your previous phone.',
                      style: TextStyle(
                        fontSize: 11,
                        fontWeight: FontWeight.w700,
                        color: Color(0xFF666666),
                      ),
                    ),
                    const SizedBox(height: 12),

                    TextField(
                      controller: _restoreInputController,
                      maxLines: 4,
                      style: const TextStyle(
                        fontFamily: 'monospace',
                        fontSize: 11,
                        fontWeight: FontWeight.bold,
                      ),
                      decoration: InputDecoration(
                        filled: true,
                        fillColor: NeoBrutalism.background,
                        hintText: 'Paste Vault JSON content here...',
                        enabledBorder: OutlineInputBorder(
                          borderRadius: BorderRadius.circular(12),
                          borderSide: const BorderSide(
                              color: NeoBrutalism.black, width: 2),
                        ),
                        focusedBorder: OutlineInputBorder(
                          borderRadius: BorderRadius.circular(12),
                          borderSide: const BorderSide(
                              color: NeoBrutalism.black, width: 2.5),
                        ),
                      ),
                    ),
                    const SizedBox(height: 12),

                    TextField(
                      controller: _pinController,
                      keyboardType: TextInputType.number,
                      maxLength: 4,
                      obscureText: true,
                      decoration: InputDecoration(
                        counterText: '',
                        filled: true,
                        fillColor: NeoBrutalism.background,
                        labelText: 'PIN (Leave blank if none was set)',
                        labelStyle: const TextStyle(
                            fontSize: 11, fontWeight: FontWeight.bold),
                        enabledBorder: OutlineInputBorder(
                          borderRadius: BorderRadius.circular(10),
                          borderSide: const BorderSide(
                              color: NeoBrutalism.black, width: 1.5),
                        ),
                        focusedBorder: OutlineInputBorder(
                          borderRadius: BorderRadius.circular(10),
                          borderSide: const BorderSide(
                              color: NeoBrutalism.black, width: 2),
                        ),
                      ),
                    ),
                    const SizedBox(height: 14),

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
                          'RESTORE MY HABITS & MOMENTUM',
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
          ],
        ),
      ),
    );
  }
}
