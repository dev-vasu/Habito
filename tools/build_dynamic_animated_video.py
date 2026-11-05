import os
import sys
import math
import asyncio
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = Path(r"C:\Users\dvasu\.gemini\antigravity\scratch\Habito")
MEDIA_DIR = BASE_DIR / "media"
MEDIA_DIR.mkdir(parents=True, exist_ok=True)
TEMP_DIR = MEDIA_DIR / "dynamic_temp"
TEMP_DIR.mkdir(parents=True, exist_ok=True)

# Fonts
FONT_BOLD = r"C:\Windows\Fonts\segoeuib.ttf"
FONT_REGULAR = r"C:\Windows\Fonts\segoeui.ttf"
FONT_MONO = r"C:\Windows\Fonts\consola.ttf"

def get_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except:
        return ImageFont.load_default()

# Colors
BG_STUDIO = "#090D16"      # Deep studio slate
CANVAS_BG = "#FFFDF0"      # Neo-Brutalist butter cream
TEXT_DARK = "#09090B"      # Deep black ink
BORDER_DARK = "#09090B"    # Solid outline
SHADOW_DARK = "#09090B"    # Hard shadow

COLOR_YELLOW = "#FFE66D"   # Yellow
COLOR_LIME = "#A3E635"     # Acid Lime
COLOR_GREEN = "#6BCB77"    # Mint green
COLOR_BLUE = "#93C5FD"     # Sky blue
COLOR_PURPLE = "#DDD6FE"   # Lavender
COLOR_ORANGE = "#FF9F43"   # Orange
COLOR_WHITE = "#FFFFFF"

SCENES_DEF = [
    {
        "id": "scene1_intro",
        "step_tag": "OVERVIEW • HABITO v2.0",
        "headline": "Dynamic iPhone Experience\n& Neo-Brutalism",
        "subtitle": "Human-crafted habit protocol with live Dynamic Island momentum alerts.",
        "badges": ["DYNAMIC ISLAND", "NEO-BRUTALIST", "OFFLINE FIRST"],
        "speech": "Welcome to Habito version two. Engineered with an authentic neo-brutalist identity and dynamic mobile experience, Habito turns daily routine into unstoppable momentum.",
        "tab": "protocols",
        "action": "intro",
        "island_state": "welcome",
        "fuel_val": 0.50
    },
    {
        "id": "scene2_checkin",
        "step_tag": "INTERACTIVE CHECK-IN • FUEL GAUGE",
        "headline": "Tactile Micro-Actions &\nReal-Time Fuel Surge",
        "subtitle": "Tap to check habits. Watch your 12-segment tachometer charge and Dynamic Island pulse.",
        "badges": ["TACTILE CHECK", "TACHOMETER", "LIVE STREAK"],
        "speech": "Complete your daily protocols with satisfying tactile micro-interactions. As you check off habits, your live fuel meter surges in real time, and the Dynamic Island celebrates your streak momentum.",
        "tab": "protocols",
        "action": "check_habit",
        "island_state": "streak_pulse",
        "fuel_val": 0.75
    },
    {
        "id": "scene3_audit",
        "step_tag": "EFFORT AUDIT • 7-DAY CURVES",
        "headline": "Effort Audit &\nMomentum Analytics",
        "subtitle": "Zero fake data. Real 7-day angular FL consistency curves and streak shields.",
        "badges": ["7-DAY CHARTS", "14D STREAK", "FREEZE SHIELDS"],
        "speech": "Tap into the Effort Audit tab to inspect your true consistency. With zero fake data, Habito calculates your seven-day momentum curves and protects long streaks with active freeze shields.",
        "tab": "audit",
        "action": "animate_bars",
        "island_state": "audit_active",
        "fuel_val": 0.75
    },
    {
        "id": "scene4_vault",
        "step_tag": "MIGRATION VAULT • ZERO COLLISION",
        "headline": "Collision-Proof Vault &\nPIN Double-Lock",
        "subtitle": "Switch phones seamlessly with high-entropy 8-char tokens and 4-digit PIN encryption.",
        "badges": ["8-CHAR TOKEN", "2.8T COMBOS", "PIN LOCK"],
        "speech": "Switching phones? Switch to the Sync tab. Habito generates an eight-character collision-proof key with 2.8 trillion combinations. Double-lock it with an optional four-digit PIN for instant, private cross-device migration.",
        "tab": "sync",
        "action": "type_pin",
        "island_state": "vault_locked",
        "fuel_val": 0.75
    },
    {
        "id": "scene5_outro",
        "step_tag": "GET STARTED • DEV-VASU/HABITO",
        "headline": "Build Relentless Routine.\nDownload Today.",
        "subtitle": "Production APK for Android phones and AAB for Google Play Store.",
        "badges": ["GITHUB RELEASE", "DIRECT APK", "OPEN SOURCE"],
        "speech": "Habito version two is live, open source, and available today. Download the APK directly from GitHub Releases and master your daily routine.",
        "tab": "protocols",
        "action": "outro",
        "island_state": "ready",
        "fuel_val": 1.00
    }
]

def draw_neo_box(draw, xy, fill_color, border_color=BORDER_DARK, shadow_color=SHADOW_DARK, offset=5, border_width=2.5, radius=14):
    x0, y0, x1, y1 = xy
    if offset > 0:
        draw.rounded_rectangle([x0 + offset, y0 + offset, x1 + offset, y1 + offset], radius=radius, fill=shadow_color)
    draw.rounded_rectangle([x0, y0, x1, y1], radius=radius, fill=fill_color, outline=border_color, width=int(border_width))

def draw_phone_chassis(draw, px, py, pw, ph):
    # Outer device drop-shadow
    draw.rounded_rectangle([px + 14, py + 18, px + pw + 14, py + ph + 18], radius=54, fill="#020617")
    # Outer titanium bezel
    draw.rounded_rectangle([px, py, px + pw, py + ph], radius=54, fill="#18181B", outline="#27272A", width=4)
    # Inner bezel
    draw.rounded_rectangle([px + 4, py + 4, px + pw - 4, py + ph - 4], radius=50, fill="#09090B")
    # Screen boundary
    sx, sy, sw, sh = px + 12, py + 12, pw - 24, ph - 24
    draw.rounded_rectangle([sx, sy, sx + sw, sy + sh], radius=40, fill=CANVAS_BG, outline=BORDER_DARK, width=3)
    # Metallic edge highlight
    draw.rounded_rectangle([px + 2, py + 2, px + pw - 2, py + ph - 2], radius=52, outline="#52525B", width=1)
    return (sx, sy, sw, sh)

def draw_dynamic_island(draw, sx, sy, sw, state, t):
    cx = sx + sw // 2
    top_y = sy + 10

    if state == "welcome":
        w = 200 + int(15 * math.sin(t * 3))
        h = 34
        pill_box = [cx - w//2, top_y, cx + w//2, top_y + h]
        draw.rounded_rectangle(pill_box, radius=17, fill="#000000")
        font = get_font(FONT_BOLD, 11)
        draw.text((cx - 70, top_y + 9), "⚡ HABITO v2 • ONLINE", fill="#FDE047", font=font)
    elif state == "streak_pulse":
        w = 246 + int(10 * math.sin(t * 4))
        h = 36
        pill_box = [cx - w//2, top_y, cx + w//2, top_y + h]
        draw.rounded_rectangle(pill_box, radius=18, fill="#000000", outline=COLOR_LIME, width=2)
        font = get_font(FONT_BOLD, 11)
        draw.text((cx - 96, top_y + 10), "⚡ 75% FUEL • +1 STREAK 🔥", fill="#4ADE80", font=font)
    elif state == "audit_active":
        w = 224
        h = 34
        pill_box = [cx - w//2, top_y, cx + w//2, top_y + h]
        draw.rounded_rectangle(pill_box, radius=17, fill="#000000", outline="#60A5FA", width=2)
        font = get_font(FONT_BOLD, 11)
        draw.text((cx - 86, top_y + 9), "📊 88% WEEKLY ADHERENCE", fill="#93C5FD", font=font)
    elif state == "vault_locked":
        w = 230 + int(8 * math.sin(t * 3))
        h = 34
        pill_box = [cx - w//2, top_y, cx + w//2, top_y + h]
        draw.rounded_rectangle(pill_box, radius=17, fill="#000000", outline="#C084FC", width=2)
        font = get_font(FONT_BOLD, 11)
        draw.text((cx - 94, top_y + 9), "🔒 VAULT LOCKED & SALTED", fill="#DDD6FE", font=font)
    else:
        w = 126
        h = 30
        pill_box = [cx - w//2, top_y, cx + w//2, top_y + h]
        draw.rounded_rectangle(pill_box, radius=15, fill="#000000")

    # Optical Camera Lens Dot
    draw.ellipse([cx + w//2 - 20, top_y + 10, cx + w//2 - 10, top_y + 20], fill="#1E293B", outline="#0F172A", width=1)
    draw.ellipse([cx + w//2 - 17, top_y + 13, cx + w//2 - 13, top_y + 17], fill="#3B82F6")

    # iOS Status Time & Glyphs
    font_time = get_font(FONT_BOLD, 12)
    draw.text((sx + 24, sy + 14), "9:41", fill=TEXT_DARK, font=font_time)
    draw.text((sx + sw - 60, sy + 14), "5G 85%", fill=TEXT_DARK, font=font_time)

def draw_bottom_nav(draw, sx, sy, sw, sh, active_tab):
    nav_y = sy + sh - 64
    draw_neo_box(draw, [sx + 14, nav_y, sx + sw - 14, nav_y + 48], fill_color=COLOR_WHITE, offset=3, border_width=2, radius=16)
    
    font_nav = get_font(FONT_BOLD, 11)
    tabs = [
        ("protocols", "⚡ PROTOCOLS", sx + 20, 112),
        ("audit", "📊 AUDIT", sx + 140, 94),
        ("sync", "🔄 SYNC", sx + 242, 94)
    ]
    for tid, label, bx, bw in tabs:
        if tid == active_tab:
            draw_neo_box(draw, [bx, nav_y + 5, bx + bw, nav_y + 43], fill_color=BORDER_DARK, offset=0, border_width=1, radius=12)
            draw.text((bx + 12, nav_y + 14), label, fill=COLOR_WHITE, font=font_nav)
        else:
            draw.text((bx + 12, nav_y + 14), label, fill=TEXT_DARK, font=font_nav)

    # Home indicator bar
    draw.rounded_rectangle([sx + sw//2 - 50, sy + sh - 9, sx + sw//2 + 50, sy + sh - 5], radius=2, fill=BORDER_DARK)

def draw_screen_protocols(draw, sx, sy, sw, fuel_val, checked_third):
    font_xs = get_font(FONT_REGULAR, 11)
    font_sm_b = get_font(FONT_BOLD, 13)
    font_base_b = get_font(FONT_BOLD, 15)
    font_title = get_font(FONT_BOLD, 18)

    top_content = sy + 52

    # 1. COMMANDER CALLSIGN PROFILE CARD
    draw_neo_box(draw, [sx + 14, top_content, sx + sw - 14, top_content + 80], fill_color=COLOR_YELLOW, offset=4, border_width=2.5, radius=16)
    # Stamped badge top left
    draw.rounded_rectangle([sx + 24, top_content + 8, sx + 170, top_content + 24], radius=4, fill="#09090B")
    draw.text((sx + 30, top_content + 10), "★ COMMANDER CALLSIGN", fill="#FFE66D", font=get_font(FONT_BOLD, 9))

    # Avatar Badge
    draw_neo_box(draw, [sx + 24, top_content + 28, sx + 68, top_content + 72], fill_color=COLOR_PURPLE, offset=2, border_width=2, radius=12)
    draw.text((sx + 36, top_content + 36), "⚡", fill=TEXT_DARK, font=font_title)
    
    draw.text((sx + 80, top_content + 30), "VASUDEV SINGH", fill=TEXT_DARK, font=font_base_b)
    draw.text((sx + 80, top_content + 48), "\"Relentless routine. Zero excuses.\"", fill="#333333", font=font_xs)
    draw.text((sx + 80, top_content + 64), "LVL 4 DISCIPLINE • 🔥 14D STREAK", fill="#09090B", font=get_font(FONT_BOLD, 9))

    # 2. 12-SEGMENT INDUSTRIAL TACHOMETER FUEL METER
    fuel_y = top_content + 94
    draw_neo_box(draw, [sx + 14, fuel_y, sx + sw - 14, fuel_y + 98], fill_color=COLOR_WHITE, offset=4, border_width=2.5, radius=16)
    draw.text((sx + 26, fuel_y + 12), "DAILY MOMENTUM FUEL", fill=TEXT_DARK, font=font_sm_b)
    
    pct_text = f"{int(fuel_val * 100)}% GAIN"
    draw_neo_box(draw, [sx + sw - 100, fuel_y + 8, sx + sw - 24, fuel_y + 32], fill_color=COLOR_LIME, offset=2, border_width=1.5, radius=7)
    draw.text((sx + sw - 92, fuel_y + 13), pct_text, fill=TEXT_DARK, font=get_font(FONT_BOLD, 11))

    # 12 Segmented LED Blocks
    grid_x, grid_y, grid_w, grid_h = sx + 24, fuel_y + 40, sw - 48, 22
    draw.rounded_rectangle([grid_x, grid_y, grid_x + grid_w, grid_y + grid_h], radius=7, fill="#09090B")
    
    num_lit = int(round(fuel_val * 12))
    seg_w = (grid_w - 24) // 12
    for s in range(12):
        bx = grid_x + 4 + s * (seg_w + 1.5)
        by = grid_y + 3
        col = COLOR_LIME if s < num_lit else "#1E293B"
        draw.rounded_rectangle([bx, by, bx + seg_w, by + grid_h - 6], radius=3, fill=col)

    status_txt = f"{3 if checked_third else 2} OF 4 PROTOCOLS LOGGED"
    draw.text((sx + 26, fuel_y + 72), status_txt, fill="#64748B", font=font_xs)
    draw.text((sx + sw - 150, fuel_y + 72), "🛡️ 2 SHIELDS ACTIVE", fill=TEXT_DARK, font=font_xs)

    # 3. TACTILE ACTIVE PROTOCOLS
    items_y = fuel_y + 110
    draw.text((sx + 20, items_y), "TODAY'S DISCIPLINE PROTOCOL", fill="#475569", font=get_font(FONT_BOLD, 10))

    items = [
        ("Morning Deep Work (4h)", "Daily • 14d Streak", True, "DAILY"),
        ("Hydration (3.0 Liters)", "Daily • 9d Streak", True, "DAILY"),
        ("Cold Plunge / Mobility", "Weekdays • 5d Streak", checked_third, "WEEKDAYS"),
        ("Evening Digital Detox", "Daily • 21d Streak", False, "DAILY")
    ]
    curr_y = items_y + 18
    for name, sub, done, tag in items:
        card_fill = "#FFFDF0" if (not done and name.startswith("Cold")) else COLOR_WHITE
        draw_neo_box(draw, [sx + 14, curr_y, sx + sw - 14, curr_y + 54], fill_color=card_fill, offset=3, border_width=2, radius=12)
        
        # Tactile 3D Box
        cb_col = COLOR_LIME if done else COLOR_WHITE
        draw_neo_box(draw, [sx + 24, curr_y + 10, sx + 56, curr_y + 42], fill_color=cb_col, offset=2, border_width=2, radius=8)
        if done:
            draw.text((sx + 34, curr_y + 13), "✓", fill=TEXT_DARK, font=font_base_b)
        else:
            draw.text((sx + 35, curr_y + 13), "○", fill="#999999", font=font_base_b)

        name_col = "#94A3B8" if done else TEXT_DARK
        draw.text((sx + 66, curr_y + 10), name, fill=name_col, font=font_sm_b)
        draw.text((sx + 66, curr_y + 30), sub, fill="#64748B", font=font_xs)

        # Tag
        draw_neo_box(draw, [sx + sw - 86, curr_y + 15, sx + sw - 24, curr_y + 39], fill_color=COLOR_YELLOW if tag=="DAILY" else COLOR_BLUE, offset=0, border_width=1.5, radius=6)
        draw.text((sx + sw - 80, curr_y + 20), tag, fill=TEXT_DARK, font=font_xs)

        curr_y += 62

    # Add button
    draw_neo_box(draw, [sx + 14, curr_y, sx + sw - 14, curr_y + 38], fill_color=COLOR_YELLOW, offset=2, border_width=2, radius=12)
    draw.text((sx + sw//2 - 65, curr_y + 10), "+ CREATE CUSTOM PROTOCOL", fill=TEXT_DARK, font=font_sm_b)

def draw_screen_audit(draw, sx, sy, sw, progress_anim):
    font_xs = get_font(FONT_REGULAR, 11)
    font_sm_b = get_font(FONT_BOLD, 13)
    font_large = get_font(FONT_BOLD, 26)

    top_content = sy + 52
    draw_neo_box(draw, [sx + 14, top_content, sx + sw - 14, top_content + 56], fill_color=COLOR_YELLOW, offset=3, border_width=2, radius=14)
    draw.text((sx + 26, top_content + 18), "EFFORT AUDIT & METRICS", fill=TEXT_DARK, font=font_sm_b)
    draw_neo_box(draw, [sx + sw - 104, top_content + 14, sx + sw - 24, top_content + 40], fill_color=COLOR_WHITE, offset=1, border_width=1.5, radius=7)
    draw.text((sx + sw - 98, top_content + 20), "THIS MONTH", fill=TEXT_DARK, font=get_font(FONT_BOLD, 9))

    # 3 Stat Boxes
    stats_y = top_content + 68
    bw = (sw - 44) // 3
    stat_items = [
        ("14", "CURRENT", COLOR_LIME),
        ("21", "RECORD", COLOR_BLUE),
        ("2", "SHIELDS", COLOR_PURPLE)
    ]
    for i, (val, lbl, col) in enumerate(stat_items):
        bx = sx + 14 + i * (bw + 8)
        draw_neo_box(draw, [bx, stats_y, bx + bw, stats_y + 76], fill_color=col, offset=3, border_width=2, radius=12)
        draw.text((bx + bw//2 - 14, stats_y + 10), val, fill=TEXT_DARK, font=font_large)
        draw.text((bx + bw//2 - 24, stats_y + 46), lbl, fill="#333333", font=font_xs)

    # 7-Day Chart Box
    chart_y = stats_y + 90
    draw_neo_box(draw, [sx + 14, chart_y, sx + sw - 14, chart_y + 196], fill_color=COLOR_WHITE, offset=4, border_width=2.5, radius=16)
    draw.text((sx + 26, chart_y + 14), "7-DAY CONSISTENCY AUDIT", fill=TEXT_DARK, font=font_sm_b)
    draw.text((sx + sw - 120, chart_y + 14), "88% ADHERENCE", fill="#059669", font=font_xs)

    days = ["M", "T", "W", "T", "F", "S", "S"]
    max_h = [65, 95, 50, 95, 95, 65, 85]
    chart_base_y = chart_y + 155
    spacing = (sw - 60) // 7
    for i, (day, h) in enumerate(zip(days, max_h)):
        actual_h = int(h * progress_anim)
        bx = sx + 26 + i * spacing
        by = chart_base_y - actual_h
        draw.rectangle([bx, by, bx + spacing - 8, chart_base_y], fill=COLOR_LIME if h > 60 else COLOR_YELLOW, outline=BORDER_DARK, width=2)
        draw.text((bx + (spacing - 8)//2 - 4, chart_base_y + 8), day, fill=TEXT_DARK, font=font_xs)

    # Shield Defense Box
    shield_y = chart_y + 210
    draw_neo_box(draw, [sx + 14, shield_y, sx + sw - 14, shield_y + 70], fill_color=COLOR_PURPLE, offset=3, border_width=2, radius=14)
    draw.text((sx + 26, shield_y + 14), "🛡️ 2 Active Streak Freeze Shields", fill=TEXT_DARK, font=font_sm_b)
    draw.text((sx + 26, shield_y + 38), "Auto-protects streak if a day is skipped", fill="#4B5563", font=font_xs)

def draw_screen_sync(draw, sx, sy, sw, pin_chars, is_locked):
    font_xs = get_font(FONT_REGULAR, 11)
    font_sm_b = get_font(FONT_BOLD, 13)
    font_base_b = get_font(FONT_BOLD, 15)
    font_mono_lg = get_font(FONT_MONO, 20)

    top_content = sy + 52

    # Brand Header
    draw_neo_box(draw, [sx + 14, top_content, sx + sw - 14, top_content + 64], fill_color=COLOR_WHITE, offset=3, border_width=2, radius=14)
    draw_neo_box(draw, [sx + 24, top_content + 10, sx + 68, top_content + 54], fill_color=COLOR_YELLOW, offset=1, border_width=2, radius=10)
    draw.text((sx + 38, top_content + 18), "⚡", fill=TEXT_DARK, font=font_base_b)
    draw.text((sx + 78, top_content + 14), "HABITO BRAND VAULT", fill=TEXT_DARK, font=font_sm_b)
    draw.text((sx + 78, top_content + 36), "Relentless Routine. Unstoppable Momentum.", fill="#475569", font=font_xs)

    # Migration Key Card
    key_y = top_content + 76
    draw_neo_box(draw, [sx + 14, key_y, sx + sw - 14, key_y + 170], fill_color=COLOR_WHITE, offset=4, border_width=2.5, radius=16)
    draw.text((sx + 24, key_y + 14), "DYNAMIC ALPHANUMERIC TOKEN", fill=TEXT_DARK, font=font_sm_b)

    draw_neo_box(draw, [sx + 24, key_y + 40, sx + sw - 24, key_y + 92], fill_color=COLOR_YELLOW, offset=2, border_width=2, radius=10)
    draw.text((sx + 36, key_y + 54), "HAB-9K2M-7Q4X", fill=TEXT_DARK, font=font_mono_lg)

    draw.text((sx + 24, key_y + 108), "• 2.8 Trillion combinations (Zero collision)", fill="#475569", font=font_xs)
    draw.text((sx + 24, key_y + 128), "• Hardware device UUID salt & burn on redeem", fill="#475569", font=font_xs)
    draw.text((sx + 24, key_y + 148), "• 100% peer-to-peer offline architecture", fill="#475569", font=font_xs)

    # 4-Digit PIN Card
    pin_y = key_y + 184
    draw_neo_box(draw, [sx + 14, pin_y, sx + sw - 14, pin_y + 110], fill_color=COLOR_WHITE, offset=4, border_width=2.5, radius=16)
    draw.text((sx + 24, pin_y + 14), "DOUBLE-LOCK 4-DIGIT PIN", fill=TEXT_DARK, font=font_sm_b)

    # PIN input box
    draw_neo_box(draw, [sx + 24, pin_y + 40, sx + 120, pin_y + 78], fill_color="#FFFDF0", offset=1, border_width=2, radius=8)
    pin_display = " ".join(pin_chars) + (" " * (4 - len(pin_chars)))
    draw.text((sx + 40, pin_y + 46), pin_display, fill=TEXT_DARK, font=font_mono_lg)

    # Lock button
    lock_col = COLOR_LIME if is_locked else "#E2E8F0"
    draw_neo_box(draw, [sx + 130, pin_y + 40, sx + sw - 24, pin_y + 78], fill_color=lock_col, offset=2, border_width=2, radius=8)
    lock_txt = "✓ VAULT ENCRYPTED" if is_locked else "LOCK VAULT BACKUP"
    draw.text((sx + 144, pin_y + 50), lock_txt, fill=TEXT_DARK, font=font_sm_b)

    status_pin = "✓ AES Salted & Encrypted. Cannot decode without PIN." if is_locked else "Enter 4-digit PIN for double layer protection."
    draw.text((sx + 24, pin_y + 90), status_pin, fill="#059669" if is_locked else "#64748B", font=font_xs)

def draw_cursor(draw, cx, cy, clicking=False):
    r = 18 if not clicking else 14
    outline_col = COLOR_LIME if clicking else "#FFFFFF"
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill="#1E293B", outline=outline_col, width=3)
    if clicking:
        draw.ellipse([cx - 28, cy - 28, cx + 28, cy + 28], outline=COLOR_LIME, width=2)

def render_frame(scene_info, frame_idx, total_frames, output_path):
    img = Image.new("RGB", (1920, 1080), BG_STUDIO)
    draw = ImageDraw.Draw(img)

    t = frame_idx / total_frames if total_frames > 0 else 0

    # Studio Grid Background
    for gx in range(0, 1920, 60):
        draw.line([(gx, 0), (gx, 1080)], fill="#131B2E", width=1)
    for gy in range(0, 1080, 60):
        draw.line([(0, gy), (1920, gy)], fill="#131B2E", width=1)

    font_display = get_font(FONT_BOLD, 46)
    font_h2 = get_font(FONT_BOLD, 22)
    font_step = get_font(FONT_BOLD, 15)
    font_badge = get_font(FONT_BOLD, 13)
    font_sub_label = get_font(FONT_BOLD, 13)
    font_sub_text = get_font(FONT_REGULAR, 17)

    # Top Studio Banner
    draw_neo_box(draw, [70, 40, 1850, 96], fill_color="#0F172A", border_color="#334155", shadow_color="#020617", offset=4, border_width=2, radius=14)
    draw.rounded_rectangle([86, 50, 126, 86], radius=8, fill=COLOR_YELLOW, outline=BORDER_DARK, width=2)
    draw.text((98, 56), "⚡", fill=TEXT_DARK, font=font_h2)
    draw.text((140, 56), "HABITO v2.0", fill=COLOR_WHITE, font=font_h2)
    draw.text((290, 60), "DYNAMIC IPHONE WALKTHROUGH & INTERACTIVE USAGE", fill="#94A3B8", font=font_step)

    # Step Badge top right
    draw_neo_box(draw, [1440, 50, 1830, 86], fill_color=COLOR_YELLOW, offset=2, border_width=2, radius=8)
    draw.text((1460, 60), scene_info["step_tag"], fill=TEXT_DARK, font=font_step)

    # LEFT COLUMN: Narrative Showcase Card
    left_x, left_y, left_w, left_h = 70, 124, 1140, 810
    draw_neo_box(draw, [left_x, left_y, left_x + left_w, left_y + left_h], fill_color="#0F172A", border_color="#334155", shadow_color="#020617", offset=8, border_width=3, radius=20)

    # Step Pill
    draw_neo_box(draw, [left_x + 40, left_y + 36, left_x + 360, left_y + 74], fill_color=COLOR_PURPLE, offset=3, border_width=2, radius=8)
    draw.text((left_x + 56, left_y + 44), scene_info["step_tag"], fill=TEXT_DARK, font=font_step)

    # Headline & Subtitle
    draw.text((left_x + 40, left_y + 96), scene_info["headline"], fill=COLOR_WHITE, font=font_display)
    draw.text((left_x + 40, left_y + 226), scene_info["subtitle"], fill="#94A3B8", font=font_h2)

    # Badges Row
    badge_x = left_x + 40
    badge_colors = [COLOR_YELLOW, COLOR_LIME, COLOR_BLUE]
    for i, btext in enumerate(scene_info["badges"]):
        draw_neo_box(draw, [badge_x, left_y + 276, badge_x + 190, left_y + 312], fill_color=badge_colors[i % 3], offset=2, border_width=2, radius=8)
        draw.text((badge_x + 16, left_y + 284), btext, fill=TEXT_DARK, font=font_badge)
        badge_x += 210

    # Interactive Action Checklist Cards
    cards_data = [
        ("Dynamic Island Micro-Feedback", "Live pills pulse at the notch showing streaks & fuel updates in real-time.", COLOR_YELLOW),
        ("Automotive Tachometer Fuel", "12 industrial LED segments fill with acid lime as momentum builds.", COLOR_LIME),
        ("Collision-Proof Vault", "8-character high entropy token with optional 4-digit PIN prevents data swap.", COLOR_PURPLE),
    ]
    cy = left_y + 346
    for title, desc, col in cards_data:
        draw_neo_box(draw, [left_x + 40, cy, left_x + left_w - 40, cy + 86], fill_color="#1E293B", border_color="#334155", shadow_color="#020617", offset=3, border_width=2, radius=12)
        draw.rounded_rectangle([left_x + 56, cy + 18, left_x + 104, cy + 66], radius=10, fill=col, outline=BORDER_DARK, width=2)
        draw.text((left_x + 72, cy + 30), "✓", fill=TEXT_DARK, font=font_h2)
        draw.text((left_x + 120, cy + 20), title, fill=COLOR_WHITE, font=font_h2)
        draw.text((left_x + 120, cy + 50), desc, fill="#94A3B8", font=font_sub_label)
        cy += 104

    # Bottom Spoken Vocal Subtitle Box
    sub_y = left_y + left_h - 130
    draw_neo_box(draw, [left_x + 40, sub_y, left_x + left_w - 40, sub_y + 96], fill_color="#131D31", border_color="#3B82F6", shadow_color="#020617", offset=3, border_width=2, radius=12)
    draw.text((left_x + 60, sub_y + 14), "🎙️ VOCAL STEPS (SPOKEN NARRATION):", fill="#60A5FA", font=font_sub_label)
    speech_text = scene_info["speech"]
    if len(speech_text) > 110:
        idx_space = speech_text[:110].rfind(" ")
        line1 = speech_text[:idx_space]
        line2 = speech_text[idx_space:].strip()
        draw.text((left_x + 60, sub_y + 38), f'"{line1}', fill="#F1F5F9", font=font_sub_text)
        draw.text((left_x + 60, sub_y + 64), f'{line2}"', fill="#F1F5F9", font=font_sub_text)
    else:
        draw.text((left_x + 60, sub_y + 44), f'"{speech_text}"', fill="#F1F5F9", font=font_sub_text)

    # RIGHT COLUMN: iPhone Chassis with Dynamic Island
    px, py, pw, ph = 1270, 124, 460, 810
    sx, sy, sw, sh = draw_phone_chassis(draw, px, py, pw, ph)

    tab = scene_info["tab"]
    action = scene_info["action"]
    island_state = scene_info["island_state"]

    fuel_val = scene_info["fuel_val"]
    checked_third = False
    pointer_pos = None
    is_clicking = False

    if action == "check_habit":
        if t < 0.4:
            interp = t / 0.4
            pointer_pos = (sx + 40, sy + 380 - int(60 * (1 - interp)))
            fuel_val = 0.50
            checked_third = False
        elif t < 0.6:
            pointer_pos = (sx + 40, sy + 380)
            is_clicking = True
            fuel_val = 0.50 + 0.25 * ((t - 0.4) / 0.2)
            checked_third = True
        else:
            pointer_pos = (sx + 40 + int(80 * (t - 0.6)), sy + 380 + int(40 * (t - 0.6)))
            fuel_val = 0.75
            checked_third = True

    elif action == "animate_bars":
        bar_anim = min(1.0, t * 1.8)
        draw_screen_audit(draw, sx, sy, sw, bar_anim)

    elif action == "type_pin":
        pin_count = min(4, int(t * 5.5))
        pin_chars = ["•"] * pin_count
        is_locked = (pin_count == 4 and t > 0.75)
        draw_screen_sync(draw, sx, sy, sw, pin_chars, is_locked)
        if t < 0.75:
            pointer_pos = (sx + 70 + pin_count * 10, sy + 440)
        else:
            pointer_pos = (sx + 210, sy + 440)
            is_clicking = (t > 0.75 and t < 0.85)

    if action in ["intro", "check_habit", "outro"]:
        draw_screen_protocols(draw, sx, sy, sw, fuel_val, checked_third)

    # Bottom Nav
    draw_bottom_nav(draw, sx, sy, sw, sh, tab)

    # Dynamic Island
    draw_dynamic_island(draw, sx, sy, sw, island_state, t)

    # Cursor
    if pointer_pos:
        draw_cursor(draw, pointer_pos[0], pointer_pos[1], is_clicking)

    # Footer banner
    draw_neo_box(draw, [70, 950, 1850, 1020], fill_color=COLOR_YELLOW, offset=4, border_width=3, radius=12)
    draw.text((96, 970), "HABITO v2.0 • BUILT WITH FLUTTER & DART • NEO-BRUTALIST ARCHITECTURE", fill=TEXT_DARK, font=font_step)
    draw.text((1540, 970), "GITHUB.COM/DEV-VASU/HABITO", fill=TEXT_DARK, font=font_step)

    img.save(output_path, quality=92)

async def generate_speech(text, output_mp3):
    import edge_tts
    communicate = edge_tts.Communicate(text, voice="en-US-ChristopherNeural", rate="+0%")
    await communicate.save(output_mp3)

def get_audio_duration(audio_file):
    cmd = [
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", str(audio_file)
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return float(res.stdout.strip())

async def main():
    print("=== BUILDING HIGH-CRAFT DYNAMIC ANIMATED VIDEO ===")
    segment_mp4s = []
    fps = 24

    for i, scene in enumerate(SCENES_DEF):
        print(f"\n[Scene {i+1}/{len(SCENES_DEF)}]: {scene['id']} ({scene['step_tag']})")
        audio_file = TEMP_DIR / f"{scene['id']}.mp3"
        await generate_speech(scene["speech"], audio_file)

        duration = get_audio_duration(audio_file)
        target_duration = duration + 0.6
        total_frames = int(target_duration * fps)
        print(f"  Duration: {target_duration:.2f}s -> {total_frames} animated frames @ {fps}fps")

        frames_dir = TEMP_DIR / f"frames_{scene['id']}"
        frames_dir.mkdir(parents=True, exist_ok=True)

        for f_idx in range(total_frames):
            frame_img = frames_dir / f"frame_{f_idx:05d}.jpg"
            render_frame(scene, f_idx, total_frames, frame_img)

        segment_mp4 = TEMP_DIR / f"{scene['id']}.mp4"
        cmd = [
            "ffmpeg", "-y",
            "-framerate", str(fps),
            "-i", str(frames_dir / "frame_%05d.jpg"),
            "-i", str(audio_file),
            "-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "fast",
            "-c:a", "aac", "-b:a", "192k",
            "-shortest",
            str(segment_mp4)
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, check=True)
        print(f"  [OK] Encoded segment: {segment_mp4}")
        segment_mp4s.append(segment_mp4)

    # Concat all segments
    print("\n--- Stitching all animated scenes into final video ---")
    concat_txt = TEMP_DIR / "concat_list.txt"
    with open(concat_txt, "w", encoding="utf-8") as f:
        for seg in segment_mp4s:
            p = str(seg).replace("\\", "/")
            f.write(f"file '{p}'\n")

    final_mp4 = MEDIA_DIR / "habito_v2_walkthrough.mp4"
    concat_cmd = [
        "ffmpeg", "-y",
        "-f", "concat", "-safe", "0",
        "-i", str(concat_txt),
        "-c", "copy",
        str(final_mp4)
    ]
    subprocess.run(concat_cmd, check=True)
    print(f"\n[SUCCESS] Generated Full HD Dynamic Video: {final_mp4}")

    # Generate updated animated GIF preview for README
    print("\n--- Generating new animated GIF for README ---")
    gif_file = MEDIA_DIR / "habito_v2_walkthrough.gif"
    gif_cmd = [
        "ffmpeg", "-y",
        "-i", str(final_mp4),
        "-vf", "fps=3,scale=720:-1:flags=lanczos,split[s0][s1];[s0]palettegen=max_colors=128[p];[s1][p]paletteuse=dither=bayer",
        str(gif_file)
    ]
    subprocess.run(gif_cmd, check=True)
    print(f"[SUCCESS] Generated updated GIF: {gif_file}")

    # Extract new poster frame
    poster_png = MEDIA_DIR / "habito_v2_video_poster.png"
    poster_cmd = [
        "ffmpeg", "-y",
        "-i", str(final_mp4),
        "-ss", "00:00:18",
        "-vframes", "1",
        str(poster_png)
    ]
    subprocess.run(poster_cmd, check=True)
    print(f"[SUCCESS] Extracted new poster: {poster_png}")

if __name__ == "__main__":
    asyncio.run(main())
