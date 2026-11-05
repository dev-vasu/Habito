import os
import sys
import asyncio
import subprocess
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# Set up paths
BASE_DIR = Path(r"C:\Users\dvasu\.gemini\antigravity\scratch\Habito")
MEDIA_DIR = BASE_DIR / "media"
MEDIA_DIR.mkdir(parents=True, exist_ok=True)
TEMP_DIR = MEDIA_DIR / "temp"
TEMP_DIR.mkdir(parents=True, exist_ok=True)

# Fonts
FONT_BOLD = r"C:\Windows\Fonts\arialbd.ttf"
FONT_REGULAR = r"C:\Windows\Fonts\arial.ttf"
FONT_SEGOE_BOLD = r"C:\Windows\Fonts\segoeuib.ttf"
FONT_SEGOE = r"C:\Windows\Fonts\segoeui.ttf"

def get_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except:
        return ImageFont.load_default()

# Neo-Brutalism Colors
CANVAS_BG = "#FFFDF0"     # Warm cream butter canvas
TEXT_DARK = "#1E1E1E"     # Solid deep ink
BORDER_DARK = "#1E1E1E"   # Crisp black outline
SHADOW_DARK = "#1E1E1E"   # Hard offset drop shadow

COLOR_YELLOW = "#FEF08A"   # Butter yellow
COLOR_BLUE = "#93C5FD"     # Electric sky
COLOR_GREEN = "#86EFAC"    # Neon lime
COLOR_PURPLE = "#DDD6FE"   # Pastel lavender
COLOR_ORANGE = "#FDBA74"   # Coral amber
COLOR_PINK = "#F472B6"     # Hot pink
COLOR_WHITE = "#FFFFFF"

SCENES = [
    {
        "id": "scene1_intro",
        "step_tag": "WELCOME TO HABITO v2",
        "title": "Habito: Neo-Brutalist\nHabit Protocol",
        "subtitle": "Human-crafted, local-first daily discipline tracker with zero cloud lock-in.",
        "badges": ["v2.0.0 RELEASE", "GOOGLE PLAY AAB", "OFFLINE FIRST"],
        "bullets": [
            "High-contrast Neo-Brutalist visual identity",
            "Dynamic daily fuel gauge & streak shields",
            "Cryptographic cross-device vault migration",
            "Production-ready store packaging & direct APK"
        ],
        "speech": "Welcome to Habito version two, the human-crafted, neo-brutalist habit tracker engineered for daily discipline. In this walkthrough, you'll learn how to download, install, customize, and transfer your data seamlessly across devices.",
        "phone_type": "home_hero"
    },
    {
        "id": "scene2_download",
        "step_tag": "STEP 01 OF 05 • DOWNLOAD",
        "title": "Download from Official\nGitHub Releases",
        "subtitle": "Get direct access to production-verified build artifacts with zero ads or tracking.",
        "badges": ["GITHUB RELEASES", "INSTANT APK", "VERIFIED BUILD"],
        "bullets": [
            "Visit github.com/dev-vasu/Habito/releases",
            "Select app-release.apk for direct phone install",
            "Download app-release.aab for Google Play Console",
            "Automated CI/CD signed & verified binaries"
        ],
        "speech": "Step one: Downloading Habito. Navigate to the official GitHub releases page. For direct phone installation, tap on app-release.apk. For Google Play publishing, download the official app-release.aab bundle.",
        "phone_type": "download_ui"
    },
    {
        "id": "scene3_install",
        "step_tag": "STEP 02 OF 05 • INSTALLATION",
        "title": "Fast One-Tap Android\nPackage Install",
        "subtitle": "Install in seconds with standard Android package security verification.",
        "badges": ["ANDROID 8.0+", "ZERO SIGN-UP", "INSTANT READY"],
        "bullets": [
            "Tap downloaded APK in your notifications or files",
            "Allow installation from your browser or file manager",
            "Tap Install — zero permissions or sign-up needed",
            "App is immediately accessible on your home screen"
        ],
        "speech": "Step two: Installing on Android. Open the downloaded APK on your device. If prompted, allow installation from this source. Tap Install, and launch Habito directly to your home screen with zero setup delay.",
        "phone_type": "install_ui"
    },
    {
        "id": "scene4_profile",
        "step_tag": "STEP 03 OF 05 • CUSTOMIZATION",
        "title": "Profile Identity &\nLive Fuel Meter",
        "subtitle": "Configure your daily protocol parameters and fuel up your momentum.",
        "badges": ["COMMANDER PROFILE", "LIVE FUEL GAUDGE", "CUSTOM MOTTO"],
        "bullets": [
            "Tap your profile badge to customize your name & motto",
            "Select your active persona avatar badge",
            "Watch your daily Fuel Gauge recalculate in real time",
            "Target frequency goals: 7/7, 5/7, or custom intervals"
        ],
        "speech": "Step three: Personalizing your journey. Tap your profile badge to set your name, personal motto, and warrior avatar. Check your daily Fuel Meter, which dynamically calculates your completion rate in real time.",
        "phone_type": "profile_ui"
    },
    {
        "id": "scene5_streaks",
        "step_tag": "STEP 04 OF 05 • PROTOCOLS",
        "title": "Tactile Protocols &\nStreak Shield Defense",
        "subtitle": "Build unbreakable streaks with built-in freeze shields when life happens.",
        "badges": ["TACTILE CHECK-IN", "STREAK FREEZE", "7-DAY AUDIT"],
        "bullets": [
            "Single tap check-in with tactile micro-interactions",
            "Earn streak shields to protect hard-earned progress",
            "Dynamic Effort Audit ranked by consistency",
            "Zero artificial filler — 100% computed local analytics"
        ],
        "speech": "Step four: Tracking protocols and streaks. Check off your habits with satisfying tactile feedback. Earn freeze shields when life happens, and review the Effort Audit page for seven-day consistency graphs and streak trends.",
        "phone_type": "streaks_ui"
    },
    {
        "id": "scene6_migration",
        "step_tag": "STEP 05 OF 05 • MIGRATION",
        "title": "Collision-Proof Vault\nCross-Device Sync",
        "subtitle": "Switch phones without losing a single day of progress or your streak history.",
        "badges": ["8-CHAR KEY", "OPTIONAL PIN", "BURN ON REDEEM"],
        "bullets": [
            "Open Settings > Device Migration Vault",
            "Set optional 4-digit PIN for payload encryption",
            "Generate high-entropy 8-character token (HAB-XXXX)",
            "Enter key on new phone — instant full state restore"
        ],
        "speech": "Step five: Seamless device migration. Switching phones? Navigate to the Sync page, set an optional PIN, and generate an eight-character cryptographic vault key. On your new device, enter the code to instantly restore all habits, history, and shields with zero data collision.",
        "phone_type": "vault_ui"
    },
    {
        "id": "scene7_outro",
        "step_tag": "GET STARTED TODAY • v2.0",
        "title": "Build Relentless\nDaily Momentum",
        "subtitle": "Habito v2 is 100% open source, privacy-first, and ready for your phone.",
        "badges": ["GITHUB OPEN SOURCE", "PRODUCTION v2.0.0", "COMMUNITY DRIVEN"],
        "bullets": [
            "Download APK or AAB today from GitHub Releases",
            "Star the repository on dev-vasu/Habito",
            "Contribute new protocols or open pull requests",
            "Master your discipline one day at a time"
        ],
        "speech": "Habito version two is live, open source, and ready to elevate your daily discipline. Check out the GitHub repository, grab your release APK today, and build habits that stick.",
        "phone_type": "outro_ui"
    }
]

def draw_neo_box(draw, xy, fill_color, border_color=BORDER_DARK, shadow_color=SHADOW_DARK, offset=6, border_width=3, radius=12):
    x0, y0, x1, y1 = xy
    # Shadow
    draw.rounded_rectangle([x0 + offset, y0 + offset, x1 + offset, y1 + offset], radius=radius, fill=shadow_color)
    # Main Box
    draw.rounded_rectangle([x0, y0, x1, y1], radius=radius, fill=fill_color, outline=border_color, width=border_width)

def draw_phone_frame(draw, x, y, w, h):
    # Outer device bezel
    draw_neo_box(draw, [x, y, x + w, y + h], fill_color="#121212", border_color="#1E1E1E", shadow_color="#1E1E1E", offset=10, border_width=4, radius=36)
    # Screen inner
    sx, sy, sw, sh = x + 16, y + 16, w - 32, h - 32
    draw.rounded_rectangle([sx, sy, sx + sw, sy + sh], radius=24, fill=CANVAS_BG)
    # Notch / Dynamic Island
    notch_w, notch_h = 120, 24
    draw.rounded_rectangle([sx + (sw - notch_w)//2, sy + 10, sx + (sw + notch_w)//2, sy + 10 + notch_h], radius=12, fill="#121212")
    return (sx, sy, sw, sh)

def render_phone_content(draw, screen_bounds, phone_type):
    sx, sy, sw, sh = screen_bounds
    font_sm_bold = get_font(FONT_SEGOE_BOLD, 14)
    font_base_bold = get_font(FONT_SEGOE_BOLD, 17)
    font_lg_bold = get_font(FONT_SEGOE_BOLD, 22)
    font_xs = get_font(FONT_REGULAR, 12)
    font_sm = get_font(FONT_REGULAR, 14)

    # Status Bar
    draw.text((sx + 24, sy + 12), "9:41", fill=TEXT_DARK, font=font_sm_bold)
    draw.text((sx + sw - 65, sy + 12), "5G  85%", fill=TEXT_DARK, font=font_sm_bold)

    content_top = sy + 48

    if phone_type == "home_hero" or phone_type == "profile_ui":
        # Profile Bar
        draw_neo_box(draw, [sx + 16, content_top, sx + sw - 16, content_top + 76], fill_color=COLOR_YELLOW, offset=4, border_width=2, radius=12)
        # Avatar
        draw.ellipse([sx + 28, content_top + 14, sx + 76, content_top + 62], fill=COLOR_PURPLE, outline=BORDER_DARK, width=2)
        draw.text((sx + 40, content_top + 23), "⚡", fill=TEXT_DARK, font=font_lg_bold)
        draw.text((sx + 88, content_top + 18), "COMMANDER VASU", fill=TEXT_DARK, font=font_base_bold)
        draw.text((sx + 88, content_top + 42), "RELENTLESS DAILY MOMENTUM", fill="#555555", font=font_xs)

        # Fuel Meter Card
        fuel_y = content_top + 94
        draw_neo_box(draw, [sx + 16, fuel_y, sx + sw - 16, fuel_y + 90], fill_color=COLOR_WHITE, offset=4, border_width=2, radius=12)
        draw.text((sx + 28, fuel_y + 14), "DAILY PROTOCOL FUEL", fill=TEXT_DARK, font=font_sm_bold)
        draw.text((sx + sw - 72, fuel_y + 14), "75%", fill="#2563EB", font=font_base_bold)
        # Progress Bar
        bar_x, bar_y, bar_w, bar_h = sx + 28, fuel_y + 46, sw - 56, 18
        draw.rounded_rectangle([bar_x, bar_y, bar_x + bar_w, bar_y + bar_h], radius=9, fill="#E5E7EB", outline=BORDER_DARK, width=2)
        draw.rounded_rectangle([bar_x, bar_y, bar_x + int(bar_w * 0.75), bar_y + bar_h], radius=9, fill=COLOR_GREEN, outline=BORDER_DARK, width=2)

        # Habit Protocols
        habits_y = fuel_y + 108
        draw.text((sx + 20, habits_y), "ACTIVE PROTOCOLS", fill=TEXT_DARK, font=font_sm_bold)
        items = [
            ("Morning Deep Work (4h)", "Daily • 14d Streak", COLOR_GREEN, "✓", True),
            ("Hydration (3 Liters)", "Daily • 9d Streak", COLOR_GREEN, "✓", True),
            ("Cold Plunge / Mobility", "Weekdays • 5d Streak", COLOR_WHITE, "○", False),
            ("Evening Digital Detox", "Daily • 21d Streak", COLOR_GREEN, "✓", True)
        ]
        curr_y = habits_y + 24
        for title, sub, color, mark, checked in items:
            draw_neo_box(draw, [sx + 16, curr_y, sx + sw - 16, curr_y + 60], fill_color=COLOR_WHITE, offset=3, border_width=2, radius=10)
            # Checkbox
            cb_color = COLOR_GREEN if checked else "#F3F4F6"
            draw_neo_box(draw, [sx + 26, curr_y + 14, sx + 58, curr_y + 46], fill_color=cb_color, offset=2, border_width=2, radius=6)
            draw.text((sx + 35, curr_y + 18), mark, fill=TEXT_DARK, font=font_base_bold)
            draw.text((sx + 70, curr_y + 12), title, fill=TEXT_DARK, font=font_sm_bold)
            draw.text((sx + 70, curr_y + 34), sub, fill="#666666", font=font_xs)
            curr_y += 72

    elif phone_type == "download_ui":
        # GitHub Releases UI
        draw_neo_box(draw, [sx + 16, content_top, sx + sw - 16, content_top + 80], fill_color=COLOR_PURPLE, offset=4, border_width=2, radius=12)
        draw.text((sx + 28, content_top + 16), "dev-vasu / Habito", fill=TEXT_DARK, font=font_sm_bold)
        draw.text((sx + 28, content_top + 40), "Release v2.0.0 Production", fill=TEXT_DARK, font=font_lg_bold)

        # Assets Card
        card_y = content_top + 98
        draw_neo_box(draw, [sx + 16, card_y, sx + sw - 16, card_y + 280], fill_color=COLOR_WHITE, offset=4, border_width=2, radius=12)
        draw.text((sx + 28, card_y + 16), "PRODUCTION ASSETS", fill=TEXT_DARK, font=font_sm_bold)

        # Asset 1: APK (Highlighted)
        apk_y = card_y + 50
        draw_neo_box(draw, [sx + 26, apk_y, sx + sw - 26, apk_y + 90], fill_color=COLOR_GREEN, offset=3, border_width=2, radius=10)
        draw.text((sx + 40, apk_y + 14), "📦 app-release.apk", fill=TEXT_DARK, font=font_base_bold)
        draw.text((sx + 40, apk_y + 38), "Direct phone sideload • 84 MB", fill="#333333", font=font_xs)
        draw.text((sx + 40, apk_y + 58), "✓ RECOMMENDED FOR PHONES", fill="#065F46", font=font_xs)

        # Asset 2: AAB
        aab_y = apk_y + 104
        draw_neo_box(draw, [sx + 26, aab_y, sx + sw - 26, aab_y + 80], fill_color=COLOR_YELLOW, offset=3, border_width=2, radius=10)
        draw.text((sx + 40, aab_y + 14), "🏪 app-release.aab", fill=TEXT_DARK, font=font_base_bold)
        draw.text((sx + 40, aab_y + 38), "Google Play Console Bundle • 45 MB", fill="#333333", font=font_xs)
        draw.text((sx + 40, aab_y + 56), "STORE PUBLISHING FORMAT", fill="#78350F", font=font_xs)

        # Direct download pointer
        badge_y = card_y + 300
        draw_neo_box(draw, [sx + 16, badge_y, sx + sw - 16, badge_y + 60], fill_color=COLOR_BLUE, offset=4, border_width=2, radius=10)
        draw.text((sx + 28, badge_y + 18), "⚡ SHA-256 Verified Clean", fill=TEXT_DARK, font=font_base_bold)

    elif phone_type == "install_ui":
        # Android installer mockup
        draw_neo_box(draw, [sx + 16, content_top + 40, sx + sw - 16, content_top + 340], fill_color=COLOR_WHITE, offset=6, border_width=3, radius=16)
        # Logo Icon
        draw_neo_box(draw, [sx + sw//2 - 36, content_top + 70, sx + sw//2 + 36, content_top + 142], fill_color=COLOR_YELLOW, offset=3, border_width=2, radius=16)
        draw.text((sx + sw//2 - 12, content_top + 92), "⚡", fill=TEXT_DARK, font=font_lg_bold)

        draw.text((sx + sw//2 - 45, content_top + 160), "Habito v2.0", fill=TEXT_DARK, font=font_lg_bold)
        draw.text((sx + sw//2 - 95, content_top + 194), "Do you want to install this app?", fill="#555555", font=font_sm)
        draw.text((sx + sw//2 - 80, content_top + 224), "✓ Verified APK • Safe & Clean", fill="#059669", font=font_xs)

        # Buttons
        btn_y = content_top + 280
        draw_neo_box(draw, [sx + 36, btn_y, sx + sw//2 - 10, btn_y + 44], fill_color="#F3F4F6", offset=2, border_width=2, radius=8)
        draw.text((sx + 64, btn_y + 12), "CANCEL", fill="#555555", font=font_sm_bold)

        draw_neo_box(draw, [sx + sw//2 + 10, btn_y, sx + sw - 36, btn_y + 44], fill_color=COLOR_GREEN, offset=3, border_width=2, radius=8)
        draw.text((sx + sw//2 + 42, btn_y + 12), "INSTALL", fill=TEXT_DARK, font=font_sm_bold)

    elif phone_type == "streaks_ui":
        # Effort Audit page
        draw_neo_box(draw, [sx + 16, content_top, sx + sw - 16, content_top + 60], fill_color=COLOR_YELLOW, offset=4, border_width=2, radius=12)
        draw.text((sx + 28, content_top + 18), "EFFORT AUDIT & METRICS", fill=TEXT_DARK, font=font_base_bold)

        # 3 stat boxes
        stats_y = content_top + 74
        box_w = (sw - 48) // 3
        stat_items = [
            ("14", "CURRENT", COLOR_GREEN),
            ("21", "RECORD", COLOR_BLUE),
            ("2", "SHIELDS", COLOR_PURPLE)
        ]
        for i, (val, lbl, col) in enumerate(stat_items):
            bx = sx + 16 + i * (box_w + 8)
            draw_neo_box(draw, [bx, stats_y, bx + box_w, stats_y + 70], fill_color=col, offset=3, border_width=2, radius=10)
            draw.text((bx + box_w//2 - 12, stats_y + 12), val, fill=TEXT_DARK, font=font_lg_bold)
            draw.text((bx + box_w//2 - 24, stats_y + 42), lbl, fill="#444444", font=font_xs)

        # Consistency Chart Box
        chart_y = stats_y + 86
        draw_neo_box(draw, [sx + 16, chart_y, sx + sw - 16, chart_y + 170], fill_color=COLOR_WHITE, offset=4, border_width=2, radius=12)
        draw.text((sx + 28, chart_y + 14), "7-DAY CONSISTENCY", fill=TEXT_DARK, font=font_sm_bold)

        days = ["M", "T", "W", "T", "F", "S", "S"]
        heights = [60, 85, 45, 95, 100, 75, 90]
        bar_spacing = (sw - 72) // 7
        for i, (day, h) in enumerate(zip(days, heights)):
            bx = sx + 28 + i * bar_spacing
            by = chart_y + 140 - h
            draw.rectangle([bx, by, bx + bar_spacing - 6, chart_y + 140], fill=COLOR_GREEN if h > 70 else COLOR_YELLOW, outline=BORDER_DARK, width=2)
            draw.text((bx + (bar_spacing - 6)//2 - 4, chart_y + 146), day, fill=TEXT_DARK, font=font_xs)

        # Shield defense card
        shield_y = chart_y + 184
        draw_neo_box(draw, [sx + 16, shield_y, sx + sw - 16, shield_y + 64], fill_color=COLOR_ORANGE, offset=3, border_width=2, radius=10)
        draw.text((sx + 28, shield_y + 14), "🛡️ 2 Active Freeze Shields", fill=TEXT_DARK, font=font_sm_bold)
        draw.text((sx + 28, shield_y + 36), "Auto-protects streak if a day is skipped", fill="#555555", font=font_xs)

    elif phone_type == "vault_ui":
        # Migration Vault
        draw_neo_box(draw, [sx + 16, content_top, sx + sw - 16, content_top + 60], fill_color=COLOR_PURPLE, offset=4, border_width=2, radius=12)
        draw.text((sx + 28, content_top + 18), "DEVICE MIGRATION VAULT", fill=TEXT_DARK, font=font_base_bold)

        # Token Card
        card_y = content_top + 76
        draw_neo_box(draw, [sx + 16, card_y, sx + sw - 16, card_y + 190], fill_color=COLOR_WHITE, offset=4, border_width=2, radius=12)
        draw.text((sx + 28, card_y + 14), "GENERATED SYNC TOKEN", fill=TEXT_DARK, font=font_sm_bold)

        # Key Box
        key_y = card_y + 44
        draw_neo_box(draw, [sx + 28, key_y, sx + sw - 28, key_y + 54], fill_color=COLOR_YELLOW, offset=3, border_width=2, radius=8)
        draw.text((sx + 45, key_y + 14), "HAB-8X92-K47L", fill=TEXT_DARK, font=font_lg_bold)

        draw.text((sx + 28, card_y + 114), "🔒 Optional 4-Digit PIN: [••••]", fill="#333333", font=font_sm_bold)
        draw.text((sx + 28, card_y + 142), "⚡ Single-Use Burn: Active", fill="#059669", font=font_xs)
        draw.text((sx + 28, card_y + 162), "Zero cloud collision guarantee", fill="#666666", font=font_xs)

        # Restore on new phone button
        rest_y = card_y + 204
        draw_neo_box(draw, [sx + 16, rest_y, sx + sw - 16, rest_y + 60], fill_color=COLOR_GREEN, offset=3, border_width=2, radius=10)
        draw.text((sx + 36, rest_y + 18), "RESTORE PROTOCOL ON NEW DEVICE", fill=TEXT_DARK, font=font_sm_bold)

    elif phone_type == "outro_ui":
        # Summary
        draw_neo_box(draw, [sx + 16, content_top + 30, sx + sw - 16, content_top + 340], fill_color=COLOR_WHITE, offset=6, border_width=3, radius=16)
        draw_neo_box(draw, [sx + sw//2 - 36, content_top + 60, sx + sw//2 + 36, content_top + 132], fill_color=COLOR_YELLOW, offset=3, border_width=2, radius=16)
        draw.text((sx + sw//2 - 12, content_top + 82), "⚡", fill=TEXT_DARK, font=font_lg_bold)

        draw.text((sx + sw//2 - 70, content_top + 150), "HABITO v2.0", fill=TEXT_DARK, font=font_lg_bold)
        draw.text((sx + sw//2 - 105, content_top + 184), "Ready to Take Control?", fill="#555555", font=font_base_bold)

        badges = [
            ("✓ 100% Free & Open Source", COLOR_GREEN),
            ("✓ Zero Login • Full Privacy", COLOR_BLUE),
            ("✓ Instant Cross-Device Sync", COLOR_PURPLE)
        ]
        curr_y = content_top + 224
        for text, col in badges:
            draw_neo_box(draw, [sx + 32, curr_y, sx + sw - 32, curr_y + 36], fill_color=col, offset=2, border_width=2, radius=6)
            draw.text((sx + 44, curr_y + 8), text, fill=TEXT_DARK, font=font_sm_bold)
            curr_y += 44

def render_slide(scene, output_path):
    # Full HD 1920 x 1080
    img = Image.new("RGB", (1920, 1080), CANVAS_BG)
    draw = ImageDraw.Draw(img)

    font_display = get_font(FONT_SEGOE_BOLD, 54)
    font_h2 = get_font(FONT_SEGOE_BOLD, 30)
    font_step = get_font(FONT_SEGOE_BOLD, 18)
    font_bullet = get_font(FONT_REGULAR, 23)
    font_badge = get_font(FONT_SEGOE_BOLD, 15)
    font_sub_label = get_font(FONT_SEGOE_BOLD, 15)
    font_sub_text = get_font(FONT_REGULAR, 18)

    # Top Brand Header Bar
    draw_neo_box(draw, [80, 50, 1840, 110], fill_color=COLOR_WHITE, offset=4, border_width=3, radius=12)
    # Logo
    draw.rounded_rectangle([95, 60, 135, 100], radius=8, fill=COLOR_YELLOW, outline=BORDER_DARK, width=2)
    draw.text((106, 68), "⚡", fill=TEXT_DARK, font=font_h2)
    draw.text((148, 68), "HABITO", fill=TEXT_DARK, font=font_h2)
    draw.text((280, 72), "v2.0 PRODUCTION WALKTHROUGH", fill="#666666", font=font_step)

    # Step tag on top right
    draw_neo_box(draw, [1460, 60, 1820, 100], fill_color=COLOR_YELLOW, offset=2, border_width=2, radius=8)
    draw.text((1480, 70), scene["step_tag"], fill=TEXT_DARK, font=font_step)

    # Left Column: Information Card
    left_x = 80
    left_y = 140
    left_w = 1100
    left_h = 760

    draw_neo_box(draw, [left_x, left_y, left_x + left_w, left_y + left_h], fill_color=COLOR_WHITE, offset=8, border_width=3, radius=16)

    # Step Badge
    draw_neo_box(draw, [left_x + 50, left_y + 40, left_x + 360, left_y + 80], fill_color=COLOR_PURPLE, offset=3, border_width=2, radius=8)
    draw.text((left_x + 68, left_y + 48), scene["step_tag"], fill=TEXT_DARK, font=font_step)

    # Main Headline
    draw.text((left_x + 50, left_y + 104), scene["title"], fill=TEXT_DARK, font=font_display)

    # Subtitle
    draw.text((left_x + 50, left_y + 245), scene["subtitle"], fill="#4B5563", font=font_h2)

    # Action Checklist / Bullets
    bullet_y = left_y + 320
    colors_cycle = [COLOR_YELLOW, COLOR_BLUE, COLOR_GREEN, COLOR_ORANGE]
    for i, bullet in enumerate(scene["bullets"]):
        draw_neo_box(draw, [left_x + 50, bullet_y, left_x + 92, bullet_y + 42], fill_color=colors_cycle[i % 4], offset=2, border_width=2, radius=8)
        draw.text((left_x + 64, bullet_y + 6), f"{i+1}", fill=TEXT_DARK, font=font_step)
        draw.text((left_x + 110, bullet_y + 8), bullet, fill=TEXT_DARK, font=font_bullet)
        bullet_y += 66

    # Bottom Audio Subtitle Bar
    sub_box_y = left_y + 610
    draw_neo_box(draw, [left_x + 50, sub_box_y, left_x + left_w - 50, sub_box_y + 110], fill_color=CANVAS_BG, offset=3, border_width=2, radius=10)
    draw.text((left_x + 70, sub_box_y + 14), "🎙️ VOCAL NARRATION:", fill="#1E40AF", font=font_sub_label)

    # Speech text wrapped
    speech_text = scene["speech"]
    if len(speech_text) > 115:
        line1 = speech_text[:115]
        last_space = line1.rfind(" ")
        line1 = speech_text[:last_space]
        line2 = speech_text[last_space:].strip()
        draw.text((left_x + 70, sub_box_y + 40), f'"{line1}', fill="#1F2937", font=font_sub_text)
        draw.text((left_x + 70, sub_box_y + 68), f'{line2}"', fill="#1F2937", font=font_sub_text)
    else:
        draw.text((left_x + 70, sub_box_y + 44), f'"{speech_text}"', fill="#1F2937", font=font_sub_text)

    # Right Column: Phone Mockup
    phone_x = 1240
    phone_y = 140
    phone_w = 460
    phone_h = 760
    screen_bounds = draw_phone_frame(draw, phone_x, phone_y, phone_w, phone_h)
    render_phone_content(draw, screen_bounds, scene["phone_type"])

    # Bottom Progress Bar / Status
    draw_neo_box(draw, [80, 930, 1840, 1000], fill_color=COLOR_YELLOW, offset=4, border_width=3, radius=12)
    draw.text((110, 948), "HABITO v2.0 • NEO-BRUTALIST ARCHITECTURE • BUILT WITH FLUTTER & DART", fill=TEXT_DARK, font=font_step)
    draw.text((1540, 948), "GITHUB.COM/DEV-VASU/HABITO", fill=TEXT_DARK, font=font_step)

    img.save(output_path, quality=95)
    print(f"Generated slide: {output_path}")

async def generate_speech(text, output_mp3):
    import edge_tts
    communicate = edge_tts.Communicate(text, voice="en-US-ChristopherNeural", rate="+0%")
    await communicate.save(output_mp3)
    print(f"Generated speech: {output_mp3}")

def get_audio_duration(audio_file):
    cmd = [
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", str(audio_file)
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return float(res.stdout.strip())

async def main():
    print("=== HABITO v2 WALKTHROUGH VIDEO GENERATOR ===")
    segment_files = []

    for i, scene in enumerate(SCENES):
        print(f"\n--- Processing Scene {i+1}/{len(SCENES)}: {scene['id']} ---")
        slide_img = TEMP_DIR / f"{scene['id']}.png"
        audio_mp3 = TEMP_DIR / f"{scene['id']}.mp3"
        segment_mp4 = TEMP_DIR / f"{scene['id']}.mp4"

        # 1. Render slide image
        render_slide(scene, slide_img)

        # 2. Generate voiceover speech
        await generate_speech(scene["speech"], audio_mp3)

        # 3. Get exact audio duration
        duration = get_audio_duration(audio_mp3)
        # Pad duration slightly by 0.6 seconds so narration doesn't clip abruptly
        target_duration = duration + 0.6
        print(f"Scene duration: {duration:.2f}s (target: {target_duration:.2f}s)")

        # 4. Create scene video segment with ffmpeg
        # Loop image for duration, merge audio, encode to h264/aac
        cmd = [
            "ffmpeg", "-y",
            "-loop", "1", "-i", str(slide_img),
            "-i", str(audio_mp3),
            "-c:v", "libx264", "-tune", "stillimage", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "192k",
            "-t", str(target_duration),
            "-shortest",
            str(segment_mp4)
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, check=True)
        print(f"Generated segment: {segment_mp4}")
        segment_files.append(segment_mp4)

    # 5. Concatenate all segments into the final video
    print("\n--- Concatenating all scenes into final video ---")
    concat_list_file = TEMP_DIR / "concat_list.txt"
    with open(concat_list_file, "w", encoding="utf-8") as f:
        for seg in segment_files:
            # ffmpeg concat demuxer requires forward slashes or escaped backslashes
            p_str = str(seg).replace("\\", "/")
            f.write(f"file '{p_str}'\n")

    final_mp4 = MEDIA_DIR / "habito_v2_walkthrough.mp4"
    concat_cmd = [
        "ffmpeg", "-y",
        "-f", "concat", "-safe", "0",
        "-i", str(concat_list_file),
        "-c", "copy",
        str(final_mp4)
    ]
    subprocess.run(concat_cmd, check=True)
    print(f"\n🎉 FULL HD VIDEO CREATED: {final_mp4}")

    # 6. Generate optimized GIF preview for GitHub README
    print("\n--- Generating optimized GIF preview for README ---")
    gif_file = MEDIA_DIR / "habito_v2_walkthrough.gif"
    # Create 800x450 animated preview GIF (sample at 4 fps to keep size manageable)
    gif_cmd = [
        "ffmpeg", "-y",
        "-i", str(final_mp4),
        "-vf", "fps=3,scale=800:-1:flags=lanczos,split[s0][s1];[s0]palettegen=max_colors=128[p];[s1][p]paletteuse=dither=bayer",
        str(gif_file)
    ]
    subprocess.run(gif_cmd, check=True)
    print(f"🎉 README GIF PREVIEW CREATED: {gif_file}")

    print("\nAll tasks completed successfully!")

if __name__ == "__main__":
    asyncio.run(main())
