import os
from pathlib import Path

BASE_DIR = Path(r"C:\Users\dvasu\.gemini\antigravity\scratch\Habito")
SCREENSHOTS_DIR = BASE_DIR / "screenshots"
SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)

# -------------------------------------------------------------
# 1. SHOWCASE 02: COLLISION-PROOF VAULT MIGRATION (Matches Artifact exactly!)
# -------------------------------------------------------------
svg_vault = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1240 980" width="100%" height="100%">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700;900&amp;family=JetBrains+Mono:wght@700&amp;display=swap');
      .font-sans { font-family: 'Space Grotesk', -apple-system, sans-serif; }
      .font-mono { font-family: 'JetBrains Mono', monospace; }
      .brutal-shadow { filter: drop-shadow(4px 4px 0px #1E1E1E); }
      .brutal-shadow-sm { filter: drop-shadow(2px 2px 0px #1E1E1E); }
      .phone-shadow { filter: drop-shadow(12px 16px 0px #0A090D); }
    </style>
  </defs>

  <!-- Studio Canvas Background (Matches artifact bg-slate-900) -->
  <rect width="1240" height="980" fill="#0F172A" rx="28"/>
  <rect x="12" y="12" width="1216" height="956" fill="none" stroke="#1E293B" stroke-width="2" rx="20"/>

  <!-- LEFT: Showcase Narrative & Architecture Guarantees -->
  <g transform="translate(60, 56)" class="font-sans">
    <!-- Showcase Tag -->
    <rect x="0" y="0" width="190" height="30" rx="8" fill="#FFE66D" stroke="#1E1E1E" stroke-width="2"/>
    <text x="95" y="20" font-size="11" font-weight="900" fill="#1E1E1E" text-anchor="middle" letter-spacing="1">⚡ FEATURE SHOWCASE 02</text>
    
    <text x="0" y="74" font-size="34" font-weight="900" fill="#FFFFFF" letter-spacing="-0.5">Collision-Proof Vault Migration</text>
    <text x="0" y="104" font-size="15" font-weight="700" fill="#94A3B8">Switch phones seamlessly with zero data interchange, dynamic tokens &amp; PIN lock.</text>

    <!-- 4 Architectural Guarantee Cards -->
    <g transform="translate(0, 140)">
      <!-- Card 1 -->
      <g transform="translate(0, 0)">
        <rect x="4" y="4" width="530" height="130" rx="16" fill="#1E1E1E"/>
        <rect x="0" y="0" width="530" height="130" rx="16" fill="#1E293B" stroke="#334155" stroke-width="2"/>
        <rect x="20" y="24" width="48" height="48" rx="12" fill="#FFE66D" stroke="#1E1E1E" stroke-width="2.5"/>
        <text x="44" y="55" font-size="22" text-anchor="middle">🔑</text>
        <text x="84" y="44" font-size="17" font-weight="900" fill="#FFFFFF">Dynamic High-Entropy Token</text>
        <text x="84" y="70" font-size="13" font-weight="700" fill="#94A3B8">8 alphanumeric chars (HAB-XXXX-XXXX) yield 2.8 Trillion combinations.</text>
        <text x="84" y="92" font-size="12" font-weight="700" fill="#CBD5E1">Single-use burn-on-redeem ensures codes cannot be intercepted or reused.</text>
      </g>

      <!-- Card 2 -->
      <g transform="translate(0, 150)">
        <rect x="4" y="4" width="530" height="130" rx="16" fill="#1E1E1E"/>
        <rect x="0" y="0" width="530" height="130" rx="16" fill="#1E293B" stroke="#334155" stroke-width="2"/>
        <rect x="20" y="24" width="48" height="48" rx="12" fill="#6BCB77" stroke="#1E1E1E" stroke-width="2.5"/>
        <text x="44" y="55" font-size="22" text-anchor="middle">🛡️</text>
        <text x="84" y="44" font-size="17" font-weight="900" fill="#FFFFFF">Zero Data Interchange Guarantee</text>
        <text x="84" y="70" font-size="13" font-weight="700" fill="#94A3B8">Hardware device UUID tagging &amp; cryptographic salt isolate every user.</text>
        <text x="84" y="92" font-size="12" font-weight="700" fill="#CBD5E1">Two concurrent users can never receive or swap each other&apos;s habit history.</text>
      </g>

      <!-- Card 3 -->
      <g transform="translate(0, 300)">
        <rect x="4" y="4" width="530" height="130" rx="16" fill="#1E1E1E"/>
        <rect x="0" y="0" width="530" height="130" rx="16" fill="#1E293B" stroke="#334155" stroke-width="2"/>
        <rect x="20" y="24" width="48" height="48" rx="12" fill="#4D96FF" stroke="#1E1E1E" stroke-width="2.5"/>
        <text x="44" y="55" font-size="22" text-anchor="middle">🔒</text>
        <text x="84" y="44" font-size="17" font-weight="900" fill="#FFFFFF">Double-Lock 4-Digit Vault PIN</text>
        <text x="84" y="70" font-size="13" font-weight="700" fill="#94A3B8">Encrypt the backup payload with a private PIN before creating the transfer.</text>
        <text x="84" y="92" font-size="12" font-weight="700" fill="#CBD5E1">Even with the 8-char token, data cannot be decoded without the PIN.</text>
      </g>

      <!-- Card 4 -->
      <g transform="translate(0, 450)">
        <rect x="4" y="4" width="530" height="130" rx="16" fill="#1E1E1E"/>
        <rect x="0" y="0" width="530" height="130" rx="16" fill="#1E293B" stroke="#334155" stroke-width="2"/>
        <rect x="20" y="24" width="48" height="48" rx="12" fill="#FF9F43" stroke="#1E1E1E" stroke-width="2.5"/>
        <text x="44" y="55" font-size="22" text-anchor="middle">📦</text>
        <text x="84" y="44" font-size="17" font-weight="900" fill="#FFFFFF">AirDrop, Drive &amp; Local File Sync</text>
        <text x="84" y="70" font-size="13" font-weight="700" fill="#94A3B8">Export an encrypted .habito JSON payload directly to your personal cloud.</text>
        <text x="84" y="92" font-size="12" font-weight="700" fill="#CBD5E1">100% peer-to-peer and offline-first — zero third-party cloud lock-in.</text>
      </g>
    </g>
  </g>

  <!-- RIGHT: Complete, Uncropped Full-Height Phone Simulator (Matches Artifact!) -->
  <g transform="translate(680, 56)" class="font-sans">
    <!-- Phone Outer Shadow -->
    <rect x="14" y="14" width="490" height="868" rx="44" fill="#030712"/>

    <!-- Phone Bezel -->
    <rect x="0" y="0" width="490" height="868" rx="44" fill="#FFFDF0" stroke="#1E1E1E" stroke-width="10"/>

    <!-- Dynamic Island / Speaker Notch -->
    <rect x="180" y="14" width="130" height="24" rx="12" fill="#1E1E1E"/>

    <!-- Status Bar -->
    <text x="38" y="32" font-size="13" font-weight="900" fill="#1E1E1E">9:41</text>
    <text x="452" y="32" font-size="12" font-weight="900" fill="#1E1E1E" text-anchor="end">5G  85%</text>

    <!-- Phone Inner Content Canvas -->
    <g transform="translate(20, 52)">

      <!-- 1. BRAND LOGO & TAGLINE BANNER (Matches Artifact Line 65) -->
      <g transform="translate(0, 0)">
        <rect x="4" y="4" width="450" height="84" rx="18" fill="#1E1E1E"/>
        <rect x="0" y="0" width="450" height="84" rx="18" fill="#FFFFFF" stroke="#1E1E1E" stroke-width="2.5"/>
        
        <!-- Logo Icon Box -->
        <rect x="16" y="14" width="56" height="56" rx="12" fill="#FFE66D" stroke="#1E1E1E" stroke-width="2.5"/>
        <text x="44" y="52" font-size="30" text-anchor="middle">⚡</text>

        <rect x="86" y="14" width="168" height="18" rx="4" fill="#4D96FF" stroke="#1E1E1E" stroke-width="1.5"/>
        <text x="170" y="27" font-size="9" font-weight="900" fill="#FFFFFF" text-anchor="middle" letter-spacing="1">OFFICIAL BRAND IDENTITY</text>
        <text x="86" y="52" font-size="20" font-weight="900" fill="#1E1E1E" letter-spacing="-0.5">HABITO</text>
        <text x="86" y="70" font-size="11" font-weight="900" fill="#475569">&quot;Relentless Routine. Unstoppable Momentum.&quot;</text>
      </g>

      <!-- 2. USER PROFILE & MOTTO CARD (Matches Artifact Line 78) -->
      <g transform="translate(0, 98)">
        <rect x="4" y="4" width="450" height="96" rx="18" fill="#1E1E1E"/>
        <rect x="0" y="0" width="450" height="96" rx="18" fill="#FFE66D" stroke="#1E1E1E" stroke-width="2.5"/>

        <text x="18" y="25" font-size="10" font-weight="900" fill="#1E1E1E" letter-spacing="1">USER PROFILE &amp; IDENTITY</text>
        <!-- Edit Name Button -->
        <rect x="340" y="10" width="94" height="24" rx="6" fill="#FFFFFF" stroke="#1E1E1E" stroke-width="2"/>
        <text x="387" y="26" font-size="10" font-weight="900" fill="#1E1E1E" text-anchor="middle">✏️ EDIT NAME</text>

        <!-- Avatar Badge -->
        <circle cx="48" cy="62" r="24" fill="#DDD6FE" stroke="#1E1E1E" stroke-width="2.5"/>
        <text x="48" y="71" font-size="24" text-anchor="middle">⚡</text>

        <text x="86" y="58" font-size="17" font-weight="900" fill="#1E1E1E">VASUDEV&apos;S PROTOCOLS</text>
        <text x="86" y="76" font-size="12" font-weight="800" fill="#1E1E1E" opacity="0.85">&quot;Relentless consistency. Zero excuses.&quot;</text>
      </g>

      <!-- 3. COLLISION-PROOF MIGRATION SECURITY BOX (Matches Artifact Line 95) -->
      <g transform="translate(0, 208)">
        <rect x="4" y="4" width="450" height="258" rx="18" fill="#1E1E1E"/>
        <rect x="0" y="0" width="450" height="258" rx="18" fill="#FFFFFF" stroke="#1E1E1E" stroke-width="2.5"/>

        <!-- Header Tag -->
        <rect x="18" y="16" width="160" height="22" rx="5" fill="#6BCB77" stroke="#1E1E1E" stroke-width="1.5"/>
        <text x="98" y="31" font-size="9" font-weight="900" fill="#1E1E1E" text-anchor="middle" letter-spacing="0.5">COLLISION-PROOF ENGINE</text>
        <text x="432" y="31" font-size="11" font-weight="900" fill="#1E1E1E" text-anchor="end">🔄 REGENERATE</text>

        <text x="18" y="60" font-size="16" font-weight="900" fill="#1E1E1E">Dynamic Alphanumeric Sync Key</text>
        <text x="18" y="78" font-size="11" font-weight="700" fill="#64748B">Generated dynamically. 2.8 Trillion combinations with unique device UUID.</text>

        <!-- Code Box -->
        <g transform="translate(18, 92)">
          <rect x="0" y="0" width="414" height="58" rx="12" fill="#FFFDF0" stroke="#1E1E1E" stroke-width="2"/>
          <text x="16" y="20" font-size="9" font-weight="900" fill="#94A3B8" letter-spacing="1">DYNAMIC TOKEN</text>
          <text x="16" y="44" font-size="20" font-weight="900" fill="#1E1E1E" class="font-mono">HAB-9K2M-7Q4X</text>
          
          <!-- Copy Button -->
          <rect x="320" y="10" width="80" height="38" rx="10" fill="#FFE66D" stroke="#1E1E1E" stroke-width="2"/>
          <text x="360" y="34" font-size="12" font-weight="900" fill="#1E1E1E" text-anchor="middle">COPY</text>
        </g>

        <!-- Guarantee Subbox -->
        <g transform="translate(18, 162)">
          <rect x="0" y="0" width="414" height="82" rx="10" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
          <text x="14" y="22" font-size="11" font-weight="900" fill="#0F172A">🔒 Zero Data Interchange Guarantee:</text>
          <text x="14" y="40" font-size="10" font-weight="700" fill="#475569">• High Entropy: 8 alphanumeric chars (36^8 ≈ 2.8 Trillion possibilities)</text>
          <text x="14" y="57" font-size="10" font-weight="700" fill="#475569">• Device UUID &amp; Salt: Payload tagged to unique hardware fingerprint</text>
          <text x="14" y="74" font-size="10" font-weight="700" fill="#475569">• Optional 4-Digit PIN: Lock backup so only your PIN can unlock it</text>
        </g>
      </g>

      <!-- 4. OPTIONAL PIN LOCK (Matches Artifact Line 133) -->
      <g transform="translate(0, 480)">
        <rect x="4" y="4" width="450" height="124" rx="18" fill="#1E1E1E"/>
        <rect x="0" y="0" width="450" height="124" rx="18" fill="#FFFFFF" stroke="#1E1E1E" stroke-width="2.5"/>

        <rect x="18" y="14" width="140" height="20" rx="5" fill="#4D96FF" stroke="#1E1E1E" stroke-width="1.5"/>
        <text x="88" y="28" font-size="9" font-weight="900" fill="#FFFFFF" text-anchor="middle" letter-spacing="0.5">DOUBLE-LOCK SECURITY</text>
        
        <text x="18" y="52" font-size="14" font-weight="900" fill="#1E1E1E">Set 4-Digit Vault PIN</text>

        <!-- PIN Input Box -->
        <rect x="18" y="64" width="110" height="38" rx="10" fill="#FFFDF0" stroke="#1E1E1E" stroke-width="2"/>
        <text x="73" y="90" font-size="20" font-weight="900" fill="#1E1E1E" text-anchor="middle" class="font-mono">••••</text>

        <!-- Lock Button -->
        <rect x="138" y="64" width="294" height="38" rx="10" fill="#6BCB77" stroke="#1E1E1E" stroke-width="2"/>
        <text x="285" y="88" font-size="12" font-weight="900" fill="#1E1E1E" text-anchor="middle">LOCK VAULT BACKUP</text>

        <text x="18" y="115" font-size="9" font-weight="800" fill="#059669">✓ PIN Active (7492). Exported data is cryptographically protected.</text>
      </g>

      <!-- 5. PEER-TO-PEER RESTORE ON NEW PHONE -->
      <g transform="translate(0, 618)">
        <rect x="4" y="4" width="450" height="66" rx="16" fill="#1E1E1E"/>
        <rect x="0" y="0" width="450" height="66" rx="16" fill="#6BCB77" stroke="#1E1E1E" stroke-width="2.5"/>
        <text x="225" y="34" font-size="14" font-weight="900" fill="#1E1E1E" text-anchor="middle">RESTORE PROTOCOL ON NEW DEVICE</text>
        <text x="225" y="52" font-size="11" font-weight="800" fill="#1E1E1E" text-anchor="middle">Enter 8-Char Key &amp; PIN to restore 100% of habits</text>
      </g>

      <!-- 6. COMPLETE BOTTOM NAVIGATION BAR (Matches Artifact Line 148 - NOT CROPPED!) -->
      <g transform="translate(0, 702)">
        <rect x="4" y="4" width="450" height="56" rx="18" fill="#1E1E1E"/>
        <rect x="0" y="0" width="450" height="56" rx="18" fill="#FFFFFF" stroke="#1E1E1E" stroke-width="2.5"/>

        <!-- Active Security Tab -->
        <rect x="80" y="8" width="290" height="40" rx="12" fill="#1E1E1E" stroke="#1E1E1E" stroke-width="2"/>
        <text x="225" y="33" font-size="12" font-weight="900" fill="#FFFFFF" text-anchor="middle">🛡️ SECURITY &amp; MIGRATION VAULT</text>
      </g>

    </g>

    <!-- Bottom Home Indicator Bar -->
    <rect x="175" y="848" width="140" height="4" rx="2" fill="#1E1E1E"/>
  </g>
</svg>
"""

# -------------------------------------------------------------
# 2. SHOWCASE 01: DAILY ENGINE & ENERGY FUEL GAUGE (Uncropped!)
# -------------------------------------------------------------
svg_fuel = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1240 980" width="100%" height="100%">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700;900&amp;family=JetBrains+Mono:wght@700&amp;display=swap');
      .font-sans { font-family: 'Space Grotesk', -apple-system, sans-serif; }
      .font-mono { font-family: 'JetBrains Mono', monospace; }
      .brutal-shadow { filter: drop-shadow(4px 4px 0px #1E1E1E); }
    </style>
  </defs>

  <!-- Studio Canvas Background -->
  <rect width="1240" height="980" fill="#0F172A" rx="28"/>
  <rect x="12" y="12" width="1216" height="956" fill="none" stroke="#1E293B" stroke-width="2" rx="20"/>

  <!-- LEFT: Showcase Narrative & Architecture Highlights -->
  <g transform="translate(60, 56)" class="font-sans">
    <!-- Showcase Tag -->
    <rect x="0" y="0" width="190" height="30" rx="8" fill="#FF6B6B" stroke="#1E1E1E" stroke-width="2"/>
    <text x="95" y="20" font-size="11" font-weight="900" fill="#FFFFFF" text-anchor="middle" letter-spacing="1">⚡ FEATURE SHOWCASE 01</text>
    
    <text x="0" y="74" font-size="34" font-weight="900" fill="#FFFFFF" letter-spacing="-0.5">Neo-Brutalist Daily Engine</text>
    <text x="0" y="104" font-size="15" font-weight="700" fill="#94A3B8">Tactile 3D checkboxes, live fuel meter, frequency targets &amp; personalized callsign.</text>

    <!-- 4 Architectural Guarantee Cards -->
    <g transform="translate(0, 140)">
      <!-- Card 1 -->
      <g transform="translate(0, 0)">
        <rect x="4" y="4" width="530" height="130" rx="16" fill="#1E1E1E"/>
        <rect x="0" y="0" width="530" height="130" rx="16" fill="#1E293B" stroke="#334155" stroke-width="2"/>
        <rect x="20" y="24" width="48" height="48" rx="12" fill="#FFE66D" stroke="#1E1E1E" stroke-width="2.5"/>
        <text x="44" y="55" font-size="22" text-anchor="middle">⚡</text>
        <text x="84" y="44" font-size="17" font-weight="900" fill="#FFFFFF">Dynamic Daily Fuel Meter</text>
        <text x="84" y="70" font-size="13" font-weight="700" fill="#94A3B8">Computes real-time protocol completion with high-visibility fill states.</text>
        <text x="84" y="92" font-size="12" font-weight="700" fill="#CBD5E1">Instant tactile feedback gives visceral satisfaction upon day completion.</text>
      </g>

      <!-- Card 2 -->
      <g transform="translate(0, 150)">
        <rect x="4" y="4" width="530" height="130" rx="16" fill="#1E1E1E"/>
        <rect x="0" y="0" width="530" height="130" rx="16" fill="#1E293B" stroke="#334155" stroke-width="2"/>
        <rect x="20" y="24" width="48" height="48" rx="12" fill="#6BCB77" stroke="#1E1E1E" stroke-width="2.5"/>
        <text x="44" y="55" font-size="22" text-anchor="middle">✓</text>
        <text x="84" y="44" font-size="17" font-weight="900" fill="#FFFFFF">Tactile 3D Physical Feedback</text>
        <text x="84" y="70" font-size="13" font-weight="700" fill="#94A3B8">Checkboxes depress 2px into the card surface with crisp 4px drop-shadows.</text>
        <text x="84" y="92" font-size="12" font-weight="700" fill="#CBD5E1">Designed intentionally to feel crafted, punchy, and human — zero AI template slop.</text>
      </g>

      <!-- Card 3 -->
      <g transform="translate(0, 300)">
        <rect x="4" y="4" width="530" height="130" rx="16" fill="#1E1E1E"/>
        <rect x="0" y="0" width="530" height="130" rx="16" fill="#1E293B" stroke="#334155" stroke-width="2"/>
        <rect x="20" y="24" width="48" height="48" rx="12" fill="#4D96FF" stroke="#1E1E1E" stroke-width="2.5"/>
        <text x="44" y="55" font-size="22" text-anchor="middle">🎯</text>
        <text x="84" y="44" font-size="17" font-weight="900" fill="#FFFFFF">Frequency Target Scheduling</text>
        <text x="84" y="70" font-size="13" font-weight="700" fill="#94A3B8">Set 7/7 Daily, 5/7 Weekday, or flexible 3x/week targets.</text>
        <text x="84" y="92" font-size="12" font-weight="700" fill="#CBD5E1">Intelligent streak engine protects weekday habits without weekend penalties.</text>
      </g>

      <!-- Card 4 -->
      <g transform="translate(0, 450)">
        <rect x="4" y="4" width="530" height="130" rx="16" fill="#1E1E1E"/>
        <rect x="0" y="0" width="530" height="130" rx="16" fill="#1E293B" stroke="#334155" stroke-width="2"/>
        <rect x="20" y="24" width="48" height="48" rx="12" fill="#DDD6FE" stroke="#1E1E1E" stroke-width="2.5"/>
        <text x="44" y="55" font-size="22" text-anchor="middle">👤</text>
        <text x="84" y="44" font-size="17" font-weight="900" fill="#FFFFFF">Commander Identity Customization</text>
        <text x="84" y="70" font-size="13" font-weight="700" fill="#94A3B8">Configure your name, custom personal motto, and warrior avatar icon.</text>
        <text x="84" y="92" font-size="12" font-weight="700" fill="#CBD5E1">Persisted locally in SharedPreferences for fast, private, offline-first access.</text>
      </g>
    </g>
  </g>

  <!-- RIGHT: Complete, Uncropped Full-Height Phone Simulator -->
  <g transform="translate(680, 56)" class="font-sans">
    <!-- Phone Outer Shadow -->
    <rect x="14" y="14" width="490" height="868" rx="44" fill="#030712"/>

    <!-- Phone Bezel -->
    <rect x="0" y="0" width="490" height="868" rx="44" fill="#FFFDF0" stroke="#1E1E1E" stroke-width="10"/>

    <!-- Dynamic Island / Speaker Notch -->
    <rect x="180" y="14" width="130" height="24" rx="12" fill="#1E1E1E"/>

    <!-- Status Bar -->
    <text x="38" y="32" font-size="13" font-weight="900" fill="#1E1E1E">9:41</text>
    <text x="452" y="32" font-size="12" font-weight="900" fill="#1E1E1E" text-anchor="end">5G  85%</text>

    <!-- Phone Inner Content Canvas -->
    <g transform="translate(20, 52)">

      <!-- 1. Profile Bar -->
      <g transform="translate(0, 0)">
        <rect x="4" y="4" width="450" height="86" rx="18" fill="#1E1E1E"/>
        <rect x="0" y="0" width="450" height="86" rx="18" fill="#FFE66D" stroke="#1E1E1E" stroke-width="2.5"/>

        <circle cx="48" cy="43" r="24" fill="#DDD6FE" stroke="#1E1E1E" stroke-width="2.5"/>
        <text x="48" y="52" font-size="24" text-anchor="middle">⚡</text>

        <text x="86" y="38" font-size="18" font-weight="900" fill="#1E1E1E">VASUDEV&apos;S PROTOCOLS</text>
        <text x="86" y="58" font-size="12" font-weight="800" fill="#1E1E1E" opacity="0.85">&quot;Relentless consistency. Zero excuses.&quot;</text>

        <rect x="370" y="24" width="66" height="28" rx="6" fill="#FFFFFF" stroke="#1E1E1E" stroke-width="2"/>
        <text x="403" y="42" font-size="10" font-weight="900" fill="#1E1E1E" text-anchor="middle">EDIT</text>
      </g>

      <!-- 2. Fuel Meter Card -->
      <g transform="translate(0, 102)">
        <rect x="4" y="4" width="450" height="106" rx="18" fill="#1E1E1E"/>
        <rect x="0" y="0" width="450" height="106" rx="18" fill="#FFFFFF" stroke="#1E1E1E" stroke-width="2.5"/>

        <text x="20" y="30" font-size="13" font-weight="900" fill="#1E1E1E" letter-spacing="1">DAILY PROTOCOL FUEL</text>
        <text x="430" y="30" font-size="18" font-weight="900" fill="#2563EB" text-anchor="end">75%</text>

        <!-- Progress Bar Track -->
        <rect x="20" y="44" width="410" height="24" rx="12" fill="#F1F5F9" stroke="#1E1E1E" stroke-width="2"/>
        <rect x="20" y="44" width="308" height="24" rx="12" fill="#6BCB77" stroke="#1E1E1E" stroke-width="2"/>

        <text x="20" y="90" font-size="11" font-weight="800" fill="#475569">3 of 4 protocols completed today</text>
        <text x="430" y="90" font-size="11" font-weight="800" fill="#059669" text-anchor="end">⚡ HIGH MOMENTUM</text>
      </g>

      <!-- 3. Active Protocols Header -->
      <text x="6" y="232" font-size="12" font-weight="900" fill="#1E1E1E" letter-spacing="1">TODAY&apos;S ACTIVE PROTOCOLS</text>

      <!-- Protocol 1 (Completed) -->
      <g transform="translate(0, 244)">
        <rect x="4" y="4" width="450" height="68" rx="16" fill="#1E1E1E"/>
        <rect x="0" y="0" width="450" height="68" rx="16" fill="#FFFFFF" stroke="#1E1E1E" stroke-width="2.5"/>
        <rect x="16" y="14" width="40" height="40" rx="10" fill="#6BCB77" stroke="#1E1E1E" stroke-width="2"/>
        <text x="36" y="40" font-size="20" font-weight="900" fill="#1E1E1E" text-anchor="middle">✓</text>

        <text x="68" y="34" font-size="15" font-weight="900" fill="#94A3B8" text-decoration="line-through">Morning Deep Work (4h)</text>
        <text x="68" y="52" font-size="11" font-weight="700" fill="#94A3B8">Daily • 14 Day Streak 🔥</text>

        <rect x="360" y="18" width="76" height="24" rx="6" fill="#FFE66D" stroke="#1E1E1E" stroke-width="1.5"/>
        <text x="398" y="34" font-size="10" font-weight="900" fill="#1E1E1E" text-anchor="middle">DAILY</text>
      </g>

      <!-- Protocol 2 (Completed) -->
      <g transform="translate(0, 326)">
        <rect x="4" y="4" width="450" height="68" rx="16" fill="#1E1E1E"/>
        <rect x="0" y="0" width="450" height="68" rx="16" fill="#FFFFFF" stroke="#1E1E1E" stroke-width="2.5"/>
        <rect x="16" y="14" width="40" height="40" rx="10" fill="#6BCB77" stroke="#1E1E1E" stroke-width="2"/>
        <text x="36" y="40" font-size="20" font-weight="900" fill="#1E1E1E" text-anchor="middle">✓</text>

        <text x="68" y="34" font-size="15" font-weight="900" fill="#94A3B8" text-decoration="line-through">Hydration (3.0 Liters)</text>
        <text x="68" y="52" font-size="11" font-weight="700" fill="#94A3B8">Daily • 9 Day Streak 🔥</text>

        <rect x="360" y="18" width="76" height="24" rx="6" fill="#FFE66D" stroke="#1E1E1E" stroke-width="1.5"/>
        <text x="398" y="34" font-size="10" font-weight="900" fill="#1E1E1E" text-anchor="middle">DAILY</text>
      </g>

      <!-- Protocol 3 (Pending - Active Action) -->
      <g transform="translate(0, 408)">
        <rect x="4" y="4" width="450" height="74" rx="16" fill="#1E1E1E"/>
        <rect x="0" y="0" width="450" height="74" rx="16" fill="#FFFFFF" stroke="#1E1E1E" stroke-width="3"/>
        <rect x="16" y="16" width="42" height="42" rx="10" fill="#FFFDF0" stroke="#1E1E1E" stroke-width="2.5"/>

        <text x="70" y="36" font-size="16" font-weight="900" fill="#1E1E1E">Cold Plunge / Mobility</text>
        <text x="70" y="56" font-size="12" font-weight="700" fill="#2563EB">Weekdays • 5 Day Streak • TAP TO CHECK</text>

        <rect x="350" y="20" width="86" height="26" rx="6" fill="#93C5FD" stroke="#1E1E1E" stroke-width="1.5"/>
        <text x="393" y="37" font-size="10" font-weight="900" fill="#1E1E1E" text-anchor="middle">WEEKDAYS</text>
      </g>

      <!-- Protocol 4 (Completed) -->
      <g transform="translate(0, 496)">
        <rect x="4" y="4" width="450" height="68" rx="16" fill="#1E1E1E"/>
        <rect x="0" y="0" width="450" height="68" rx="16" fill="#FFFFFF" stroke="#1E1E1E" stroke-width="2.5"/>
        <rect x="16" y="14" width="40" height="40" rx="10" fill="#6BCB77" stroke="#1E1E1E" stroke-width="2"/>
        <text x="36" y="40" font-size="20" font-weight="900" fill="#1E1E1E" text-anchor="middle">✓</text>

        <text x="68" y="34" font-size="15" font-weight="900" fill="#94A3B8" text-decoration="line-through">Evening Digital Detox</text>
        <text x="68" y="52" font-size="11" font-weight="700" fill="#94A3B8">Daily • 21 Day Streak 🔥</text>

        <rect x="360" y="18" width="76" height="24" rx="6" fill="#FFE66D" stroke="#1E1E1E" stroke-width="1.5"/>
        <text x="398" y="34" font-size="10" font-weight="900" fill="#1E1E1E" text-anchor="middle">DAILY</text>
      </g>

      <!-- Quick Add Habit Button -->
      <g transform="translate(0, 580)">
        <rect x="4" y="4" width="450" height="54" rx="14" fill="#1E1E1E"/>
        <rect x="0" y="0" width="450" height="54" rx="14" fill="#FFE66D" stroke="#1E1E1E" stroke-width="2.5"/>
        <text x="225" y="33" font-size="13" font-weight="900" fill="#1E1E1E" text-anchor="middle">➕ ADD NEW PROTOCOL</text>
      </g>

      <!-- 6. COMPLETE BOTTOM NAVIGATION BAR (NOT CROPPED!) -->
      <g transform="translate(0, 702)">
        <rect x="4" y="4" width="450" height="56" rx="18" fill="#1E1E1E"/>
        <rect x="0" y="0" width="450" height="56" rx="18" fill="#FFFFFF" stroke="#1E1E1E" stroke-width="2.5"/>

        <!-- Active Protocols Tab -->
        <rect x="10" y="8" width="138" height="40" rx="12" fill="#1E1E1E"/>
        <text x="79" y="33" font-size="11" font-weight="900" fill="#FFFFFF" text-anchor="middle">⚡ PROTOCOLS</text>

        <!-- Audit Tab -->
        <text x="225" y="33" font-size="11" font-weight="900" fill="#1E1E1E" text-anchor="middle">📊 AUDIT</text>

        <!-- Sync Tab -->
        <text x="370" y="33" font-size="11" font-weight="900" fill="#1E1E1E" text-anchor="middle">🔄 SYNC</text>
      </g>

    </g>

    <!-- Bottom Home Indicator Bar -->
    <rect x="175" y="848" width="140" height="4" rx="2" fill="#1E1E1E"/>
  </g>
</svg>
"""

# -------------------------------------------------------------
# 3. SHOWCASE 03: EFFORT AUDIT, MOMENTUM & STREAK SHIELDS (Uncropped!)
# -------------------------------------------------------------
svg_audit = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1240 980" width="100%" height="100%">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700;900&amp;family=JetBrains+Mono:wght@700&amp;display=swap');
      .font-sans { font-family: 'Space Grotesk', -apple-system, sans-serif; }
      .font-mono { font-family: 'JetBrains Mono', monospace; }
      .brutal-shadow { filter: drop-shadow(4px 4px 0px #1E1E1E); }
    </style>
  </defs>

  <!-- Studio Canvas Background -->
  <rect width="1240" height="980" fill="#0F172A" rx="28"/>
  <rect x="12" y="12" width="1216" height="956" fill="none" stroke="#1E293B" stroke-width="2" rx="20"/>

  <!-- LEFT: Showcase Narrative & Architecture Highlights -->
  <g transform="translate(60, 56)" class="font-sans">
    <!-- Showcase Tag -->
    <rect x="0" y="0" width="190" height="30" rx="8" fill="#4D96FF" stroke="#1E1E1E" stroke-width="2"/>
    <text x="95" y="20" font-size="11" font-weight="900" fill="#FFFFFF" text-anchor="middle" letter-spacing="1">📈 FEATURE SHOWCASE 03</text>
    
    <text x="0" y="74" font-size="34" font-weight="900" fill="#FFFFFF" letter-spacing="-0.5">Effort Audit &amp; Momentum</text>
    <text x="0" y="104" font-size="15" font-weight="700" fill="#94A3B8">Zero fake data. Real 7-day angular FL consistency curves &amp; streak freeze shields.</text>

    <!-- 4 Architectural Guarantee Cards -->
    <g transform="translate(0, 140)">
      <!-- Card 1 -->
      <g transform="translate(0, 0)">
        <rect x="4" y="4" width="530" height="130" rx="16" fill="#1E1E1E"/>
        <rect x="0" y="0" width="530" height="130" rx="16" fill="#1E293B" stroke="#334155" stroke-width="2"/>
        <rect x="20" y="24" width="48" height="48" rx="12" fill="#6BCB77" stroke="#1E1E1E" stroke-width="2.5"/>
        <text x="44" y="55" font-size="22" text-anchor="middle">📊</text>
        <text x="84" y="44" font-size="17" font-weight="900" fill="#FFFFFF">100% Real Computed Metrics</text>
        <text x="84" y="70" font-size="13" font-weight="700" fill="#94A3B8">Replaced 780 lines of legacy hardcoded arrays with genuine calculations.</text>
        <text x="84" y="92" font-size="12" font-weight="700" fill="#CBD5E1">Calculates exact current streak, personal records, and weekly adherence.</text>
      </g>

      <!-- Card 2 -->
      <g transform="translate(0, 150)">
        <rect x="4" y="4" width="530" height="130" rx="16" fill="#1E1E1E"/>
        <rect x="0" y="0" width="530" height="130" rx="16" fill="#1E293B" stroke="#334155" stroke-width="2"/>
        <rect x="20" y="24" width="48" height="48" rx="12" fill="#FFE66D" stroke="#1E1E1E" stroke-width="2.5"/>
        <text x="44" y="55" font-size="22" text-anchor="middle">🛡️</text>
        <text x="84" y="44" font-size="17" font-weight="900" fill="#FFFFFF">Streak Freeze Shield Defense</text>
        <text x="84" y="70" font-size="13" font-weight="700" fill="#94A3B8">2 monthly shields prevent life emergencies from breaking a 50+ day streak.</text>
        <text x="84" y="92" font-size="12" font-weight="700" fill="#CBD5E1">Intelligent freeze rules protect momentum when travel or sickness hits.</text>
      </g>

      <!-- Card 3 -->
      <g transform="translate(0, 300)">
        <rect x="4" y="4" width="530" height="130" rx="16" fill="#1E1E1E"/>
        <rect x="0" y="0" width="530" height="130" rx="16" fill="#1E293B" stroke="#334155" stroke-width="2"/>
        <rect x="20" y="24" width="48" height="48" rx="12" fill="#93C5FD" stroke="#1E1E1E" stroke-width="2.5"/>
        <text x="44" y="55" font-size="22" text-anchor="middle">📈</text>
        <text x="84" y="44" font-size="17" font-weight="900" fill="#FFFFFF">Angular 7-Day Consistency Bars</text>
        <text x="84" y="70" font-size="13" font-weight="700" fill="#94A3B8">Visual daily completion rates rendered with high-contrast angular bars.</text>
        <text x="84" y="92" font-size="12" font-weight="700" fill="#CBD5E1">Spot low-energy days and celebrate peak flow consistency with clarity.</text>
      </g>

      <!-- Card 4 -->
      <g transform="translate(0, 450)">
        <rect x="4" y="4" width="530" height="130" rx="16" fill="#1E1E1E"/>
        <rect x="0" y="0" width="530" height="130" rx="16" fill="#1E293B" stroke="#334155" stroke-width="2"/>
        <rect x="20" y="24" width="48" height="48" rx="12" fill="#DDD6FE" stroke="#1E1E1E" stroke-width="2.5"/>
        <text x="44" y="55" font-size="22" text-anchor="middle">🏆</text>
        <text x="84" y="44" font-size="17" font-weight="900" fill="#FFFFFF">Dynamic Ranked Protocol Audit</text>
        <text x="84" y="70" font-size="13" font-weight="700" fill="#94A3B8">Sorts your habits automatically by adherence rate and check-in volume.</text>
        <text x="84" y="92" font-size="12" font-weight="700" fill="#CBD5E1">Shows where your discipline is strongest and which goals require focus.</text>
      </g>
    </g>
  </g>

  <!-- RIGHT: Complete, Uncropped Full-Height Phone Simulator -->
  <g transform="translate(680, 56)" class="font-sans">
    <!-- Phone Outer Shadow -->
    <rect x="14" y="14" width="490" height="868" rx="44" fill="#030712"/>

    <!-- Phone Bezel -->
    <rect x="0" y="0" width="490" height="868" rx="44" fill="#FFFDF0" stroke="#1E1E1E" stroke-width="10"/>

    <!-- Dynamic Island / Speaker Notch -->
    <rect x="180" y="14" width="130" height="24" rx="12" fill="#1E1E1E"/>

    <!-- Status Bar -->
    <text x="38" y="32" font-size="13" font-weight="900" fill="#1E1E1E">9:41</text>
    <text x="452" y="32" font-size="12" font-weight="900" fill="#1E1E1E" text-anchor="end">5G  85%</text>

    <!-- Phone Inner Content Canvas -->
    <g transform="translate(20, 52)">

      <!-- 1. Header Bar -->
      <g transform="translate(0, 0)">
        <rect x="4" y="4" width="450" height="66" rx="16" fill="#1E1E1E"/>
        <rect x="0" y="0" width="450" height="66" rx="16" fill="#FFE66D" stroke="#1E1E1E" stroke-width="2.5"/>
        <text x="24" y="41" font-size="18" font-weight="900" fill="#1E1E1E">EFFORT AUDIT &amp; METRICS</text>
        <rect x="340" y="18" width="94" height="28" rx="6" fill="#FFFFFF" stroke="#1E1E1E" stroke-width="2"/>
        <text x="387" y="36" font-size="10" font-weight="900" fill="#1E1E1E" text-anchor="middle">THIS MONTH</text>
      </g>

      <!-- 2. Three Metric Boxes -->
      <g transform="translate(0, 82)">
        <!-- Box 1: Current Streak -->
        <rect x="3" y="3" width="142" height="96" rx="14" fill="#1E1E1E"/>
        <rect x="0" y="0" width="142" height="96" rx="14" fill="#6BCB77" stroke="#1E1E1E" stroke-width="2"/>
        <text x="71" y="44" font-size="32" font-weight="900" fill="#1E1E1E" text-anchor="middle">14</text>
        <text x="71" y="68" font-size="10" font-weight="900" fill="#1E1E1E" text-anchor="middle">CURRENT</text>
        <text x="71" y="82" font-size="9" font-weight="700" fill="#1E1E1E" text-anchor="middle">DAYS STREAK</text>

        <!-- Box 2: Best Streak -->
        <g transform="translate(154, 0)">
          <rect x="3" y="3" width="142" height="96" rx="14" fill="#1E1E1E"/>
          <rect x="0" y="0" width="142" height="96" rx="14" fill="#93C5FD" stroke="#1E1E1E" stroke-width="2"/>
          <text x="71" y="44" font-size="32" font-weight="900" fill="#1E1E1E" text-anchor="middle">21</text>
          <text x="71" y="68" font-size="10" font-weight="900" fill="#1E1E1E" text-anchor="middle">RECORD</text>
          <text x="71" y="82" font-size="9" font-weight="700" fill="#1E1E1E" text-anchor="middle">BEST STREAK</text>
        </g>

        <!-- Box 3: Freeze Shields -->
        <g transform="translate(308, 0)">
          <rect x="3" y="3" width="142" height="96" rx="14" fill="#1E1E1E"/>
          <rect x="0" y="0" width="142" height="96" rx="14" fill="#DDD6FE" stroke="#1E1E1E" stroke-width="2"/>
          <text x="71" y="44" font-size="32" font-weight="900" fill="#1E1E1E" text-anchor="middle">2</text>
          <text x="71" y="68" font-size="10" font-weight="900" fill="#1E1E1E" text-anchor="middle">SHIELDS</text>
          <text x="71" y="82" font-size="9" font-weight="700" fill="#1E1E1E" text-anchor="middle">ACTIVE DEFENSE</text>
        </g>
      </g>

      <!-- 3. Consistency Bar Chart Box -->
      <g transform="translate(0, 196)">
        <rect x="4" y="4" width="450" height="210" rx="18" fill="#1E1E1E"/>
        <rect x="0" y="0" width="450" height="210" rx="18" fill="#FFFFFF" stroke="#1E1E1E" stroke-width="2.5"/>

        <text x="20" y="30" font-size="13" font-weight="900" fill="#1E1E1E" letter-spacing="0.5">7-DAY CONSISTENCY AUDIT</text>
        <text x="430" y="30" font-size="11" font-weight="900" fill="#059669" text-anchor="end">88% ADHERENCE</text>

        <!-- Bar Chart Group -->
        <g transform="translate(36, 60)">
          <!-- Day Mon -->
          <rect x="0" y="30" width="38" height="85" rx="6" fill="#6BCB77" stroke="#1E1E1E" stroke-width="2"/>
          <text x="19" y="132" font-size="11" font-weight="900" fill="#1E1E1E" text-anchor="middle">M</text>
          <text x="19" y="24" font-size="10" font-weight="900" fill="#475569" text-anchor="middle">75%</text>

          <!-- Day Tue -->
          <rect x="56" y="15" width="38" height="100" rx="6" fill="#6BCB77" stroke="#1E1E1E" stroke-width="2"/>
          <text x="75" y="132" font-size="11" font-weight="900" fill="#1E1E1E" text-anchor="middle">T</text>
          <text x="75" y="9" font-size="10" font-weight="900" fill="#059669" text-anchor="middle">100%</text>

          <!-- Day Wed -->
          <rect x="112" y="45" width="38" height="70" rx="6" fill="#FFE66D" stroke="#1E1E1E" stroke-width="2"/>
          <text x="131" y="132" font-size="11" font-weight="900" fill="#1E1E1E" text-anchor="middle">W</text>
          <text x="131" y="39" font-size="10" font-weight="900" fill="#475569" text-anchor="middle">60%</text>

          <!-- Day Thu -->
          <rect x="168" y="15" width="38" height="100" rx="6" fill="#6BCB77" stroke="#1E1E1E" stroke-width="2"/>
          <text x="187" y="132" font-size="11" font-weight="900" fill="#1E1E1E" text-anchor="middle">T</text>
          <text x="187" y="9" font-size="10" font-weight="900" fill="#059669" text-anchor="middle">100%</text>

          <!-- Day Fri -->
          <rect x="224" y="15" width="38" height="100" rx="6" fill="#6BCB77" stroke="#1E1E1E" stroke-width="2"/>
          <text x="243" y="132" font-size="11" font-weight="900" fill="#1E1E1E" text-anchor="middle">F</text>
          <text x="243" y="9" font-size="10" font-weight="900" fill="#059669" text-anchor="middle">100%</text>

          <!-- Day Sat -->
          <rect x="280" y="30" width="38" height="85" rx="6" fill="#6BCB77" stroke="#1E1E1E" stroke-width="2"/>
          <text x="299" y="132" font-size="11" font-weight="900" fill="#1E1E1E" text-anchor="middle">S</text>
          <text x="299" y="24" font-size="10" font-weight="900" fill="#475569" text-anchor="middle">75%</text>

          <!-- Day Sun -->
          <rect x="336" y="20" width="38" height="95" rx="6" fill="#6BCB77" stroke="#1E1E1E" stroke-width="2"/>
          <text x="355" y="132" font-size="11" font-weight="900" fill="#1E1E1E" text-anchor="middle">S</text>
          <text x="355" y="14" font-size="10" font-weight="900" fill="#475569" text-anchor="middle">90%</text>
        </g>
      </g>

      <!-- 4. Streak Freeze Shield Defense Banner -->
      <g transform="translate(0, 420)">
        <rect x="4" y="4" width="450" height="94" rx="18" fill="#1E1E1E"/>
        <rect x="0" y="0" width="450" height="94" rx="18" fill="#DDD6FE" stroke="#1E1E1E" stroke-width="2.5"/>

        <rect x="18" y="18" width="44" height="44" rx="10" fill="#FFFFFF" stroke="#1E1E1E" stroke-width="2"/>
        <text x="40" y="47" font-size="22" text-anchor="middle">🛡️</text>

        <text x="74" y="38" font-size="16" font-weight="900" fill="#1E1E1E">2 Streak Freeze Shields Ready</text>
        <text x="74" y="56" font-size="12" font-weight="700" fill="#475569">If you miss a day due to emergency or travel,</text>
        <text x="74" y="74" font-size="11" font-weight="800" fill="#1E1E1E">shields auto-protect your streak with zero penalty.</text>
      </g>

      <!-- 5. Ranked Protocol Adherence Breakdown -->
      <g transform="translate(0, 528)">
        <rect x="4" y="4" width="450" height="158" rx="18" fill="#1E1E1E"/>
        <rect x="0" y="0" width="450" height="158" rx="18" fill="#FFFFFF" stroke="#1E1E1E" stroke-width="2.5"/>

        <text x="20" y="28" font-size="12" font-weight="900" fill="#1E1E1E" letter-spacing="1">PROTOCOL RANKINGS (BY ADHERENCE)</text>

        <!-- Rank 1 -->
        <g transform="translate(18, 42)">
          <rect x="0" y="0" width="414" height="48" rx="10" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>
          <text x="14" y="28" font-size="13" font-weight="900" fill="#1E1E1E">🥇 Morning Deep Work (4h)</text>
          <text x="400" y="28" font-size="12" font-weight="900" fill="#059669" text-anchor="end">95% • 21 Checks</text>
        </g>

        <!-- Rank 2 -->
        <g transform="translate(18, 98)">
          <rect x="0" y="0" width="414" height="48" rx="10" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>
          <text x="14" y="28" font-size="13" font-weight="900" fill="#1E1E1E">🥈 Hydration (3.0 Liters)</text>
          <text x="400" y="28" font-size="12" font-weight="900" fill="#059669" text-anchor="end">88% • 18 Checks</text>
        </g>
      </g>

      <!-- 6. COMPLETE BOTTOM NAVIGATION BAR (NOT CROPPED!) -->
      <g transform="translate(0, 702)">
        <rect x="4" y="4" width="450" height="56" rx="18" fill="#1E1E1E"/>
        <rect x="0" y="0" width="450" height="56" rx="18" fill="#FFFFFF" stroke="#1E1E1E" stroke-width="2.5"/>

        <!-- Protocols Tab -->
        <text x="79" y="33" font-size="11" font-weight="900" fill="#1E1E1E" text-anchor="middle">⚡ PROTOCOLS</text>

        <!-- Active Audit Tab -->
        <rect x="156" y="8" width="138" height="40" rx="12" fill="#1E1E1E"/>
        <text x="225" y="33" font-size="11" font-weight="900" fill="#FFFFFF" text-anchor="middle">📊 AUDIT</text>

        <!-- Sync Tab -->
        <text x="370" y="33" font-size="11" font-weight="900" fill="#1E1E1E" text-anchor="middle">🔄 SYNC</text>
      </g>

    </g>

    <!-- Bottom Home Indicator Bar -->
    <rect x="175" y="848" width="140" height="4" rx="2" fill="#1E1E1E"/>
  </g>
</svg>
"""

(SCREENSHOTS_DIR / "showcase_vault_migration.svg").write_text(svg_vault, encoding="utf-8")
(SCREENSHOTS_DIR / "showcase_protocol_fuel.svg").write_text(svg_fuel, encoding="utf-8")
(SCREENSHOTS_DIR / "showcase_trends_analytics.svg").write_text(svg_audit, encoding="utf-8")

print("Generated all 3 uncropped, full-height showcases matching the artifact!")
