import os
import sys
import math
import asyncio
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BASE_DIR = Path(r"C:\Users\dvasu\.gemini\antigravity\scratch\Habito")
MEDIA_DIR = BASE_DIR / "media"
TEX_DIR = MEDIA_DIR / "textures"
TEMP_DIR = MEDIA_DIR / "cinematic_temp"
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
COLOR_YELLOW = "#FFE66D"
COLOR_LIME = "#A3E635"
COLOR_PURPLE = "#DDD6FE"
COLOR_BLUE = "#93C5FD"
COLOR_DARK = "#09090B"

SCENES = [
    {
        "id": "scene1_intro",
        "chapter": "01 / 05 • OVERVIEW",
        "title": "Habito v2.0: High-Craft Neo-Brutalist Routine",
        "speech": "Welcome to Habito version two. Engineered with an authentic neo-brutalist identity and dynamic mobile experience, Habito turns daily routine into unstoppable momentum.",
        "type": "intro"
    },
    {
        "id": "scene2_checkin",
        "chapter": "02 / 05 • TACTILE CHECK-IN",
        "title": "12-Segment Tachometer & Dynamic Island Pulse",
        "speech": "Complete your daily protocols with satisfying tactile micro-interactions. As you check off habits, your live fuel meter surges in real time, and the Dynamic Island celebrates your streak momentum.",
        "type": "checkin"
    },
    {
        "id": "scene3_audit",
        "chapter": "03 / 05 • EFFORT AUDIT",
        "title": "7-Day Consistency Curves & Freeze Shields",
        "speech": "Tap into the Effort Audit tab to inspect your true consistency. With zero fake data, Habito calculates your seven-day momentum curves and protects long streaks with active freeze shields.",
        "type": "audit"
    },
    {
        "id": "scene4_vault",
        "chapter": "04 / 05 • MIGRATION VAULT",
        "title": "Collision-Proof Token & PIN Double-Lock",
        "speech": "Switching phones? Switch to the Sync tab. Habito generates an eight-character collision-proof key with 2.8 trillion combinations. Double-lock it with an optional four-digit PIN for instant, private cross-device migration.",
        "type": "vault"
    },
    {
        "id": "scene5_outro",
        "chapter": "05 / 05 • PRODUCTION RELEASE",
        "title": "Open Source & Local First • Download Today",
        "speech": "Habito version two is live, open source, and available today. Download the APK directly from GitHub Releases and master your daily routine.",
        "type": "outro"
    }
]

# Load phone textures and resize to target height (770px)
target_phone_h = 770
def load_and_scale_phone(filename):
    im = Image.open(TEX_DIR / filename).convert("RGBA")
    w, h = im.size
    target_w = int(w * (target_phone_h / h))
    return im.resize((target_w, target_phone_h), Image.Resampling.LANCZOS)

tex_home_init = load_and_scale_phone("phone_home_initial.png")
tex_home_done = load_and_scale_phone("phone_home_checked.png")
tex_audit = load_and_scale_phone("phone_audit.png")
tex_vault = load_and_scale_phone("phone_vault.png")
phone_w, phone_h = tex_home_init.size

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

def render_cinematic_frame(scene, f_idx, total_frames, output_path):
    # 1920 x 1080 Canvas
    t = f_idx / total_frames if total_frames > 0 else 0
    img = Image.new("RGB", (1920, 1080), "#070A12")
    draw = ImageDraw.Draw(img)

    # 1. Subtle Radial Studio Spotlight
    cx, cy = 960, 520
    for r in range(700, 100, -60):
        alpha = int(22 * (1 - r / 700))
        draw.ellipse([cx - r, cy - int(r*0.7), cx + r, cy + int(r*0.7)], fill=(18 + alpha, 28 + alpha*2, 48 + alpha*3))

    # Studio cyber grid lines
    for gx in range(0, 1920, 80):
        draw.line([(gx, 0), (gx, 1080)], fill="#0D1525", width=1)
    for gy in range(0, 1080, 80):
        draw.line([(0, gy), (1920, gy)], fill="#0D1525", width=1)

    # Floating 3D Geometric Accents in background
    draw.rounded_rectangle([180, 220 + int(10*math.sin(t*4)), 300, 340 + int(10*math.sin(t*4))], radius=24, outline="#1E293B", width=2)
    draw.text((226, 260 + int(10*math.sin(t*4))), "⚡", fill="#334155", font=get_font(FONT_BOLD, 36))
    
    draw.rounded_rectangle([1640, 680 + int(12*math.cos(t*3)), 1760, 800 + int(12*math.cos(t*3))], radius=24, outline="#1E293B", width=2)
    draw.text((1686, 720 + int(12*math.cos(t*3))), "🛡️", fill="#334155", font=get_font(FONT_BOLD, 36))

    # Top Header Banner
    draw.rounded_rectangle([80, 40, 1840, 96], radius=16, fill="#0B1120", outline="#1E293B", width=2)
    draw.rounded_rectangle([96, 50, 136, 86], radius=8, fill=COLOR_YELLOW, outline="#09090B", width=2)
    draw.text((108, 56), "⚡", fill=COLOR_DARK, font=get_font(FONT_BOLD, 22))
    draw.text((150, 56), "HABITO v2.0", fill="#FFFFFF", font=get_font(FONT_BOLD, 22))
    draw.text((310, 60), "OFFICIAL PRODUCTION RELEASE & INTERACTIVE MOBILE WALKTHROUGH", fill="#94A3B8", font=get_font(FONT_BOLD, 14))

    # Chapter badge top right
    draw.rounded_rectangle([1460, 50, 1820, 86], radius=8, fill=COLOR_LIME, outline="#09090B", width=2)
    draw.text((1480, 60), scene["chapter"], fill=COLOR_DARK, font=get_font(FONT_BOLD, 14))

    # 2. Centered Floating iPhone 16 Pro
    # Hover oscillation
    hover_y = int(8 * math.sin(t * 2 * math.pi))
    base_phone_y = 135 + hover_y

    stype = scene["type"]
    curr_phone = tex_home_init
    touch_pointer = None
    pointer_click = False

    if stype == "intro":
        # Centered phone with subtle float
        phone_x = (1920 - phone_w) // 2
        curr_phone = tex_home_init

    elif stype == "checkin":
        phone_x = (1920 - phone_w) // 2
        # Animate pointer movement to checkbox and tap
        check_box_x = phone_x + int(phone_w * 0.12)
        check_box_y = base_phone_y + int(phone_h * 0.62)

        if t < 0.35:
            interp = t / 0.35
            curr_phone = tex_home_init
            touch_pointer = (check_box_x + int(120 * (1 - interp)), check_box_y + int(80 * (1 - interp)))
        elif t < 0.55:
            # Tap state!
            curr_phone = tex_home_done
            touch_pointer = (check_box_x, check_box_y)
            pointer_click = True
        else:
            curr_phone = tex_home_done
            interp = (t - 0.55) / 0.45
            touch_pointer = (check_box_x + int(80 * interp), check_box_y - int(60 * interp))

    elif stype == "audit":
        phone_x = (1920 - phone_w) // 2
        # Smooth transition to Audit
        if t < 0.15:
            # Pointer moves to Audit tab
            interp = t / 0.15
            nav_tab_x = phone_x + int(phone_w * 0.50)
            nav_tab_y = base_phone_y + int(phone_h * 0.94)
            touch_pointer = (nav_tab_x, nav_tab_y)
            pointer_click = (t > 0.08)
            curr_phone = tex_home_done
        else:
            curr_phone = tex_audit

    elif stype == "vault":
        phone_x = (1920 - phone_w) // 2
        if t < 0.15:
            nav_tab_x = phone_x + int(phone_w * 0.82)
            nav_tab_y = base_phone_y + int(phone_h * 0.94)
            touch_pointer = (nav_tab_x, nav_tab_y)
            pointer_click = (t > 0.08)
            curr_phone = tex_audit
        else:
            curr_phone = tex_vault

    elif stype == "outro":
        # Phone glides to the left; Store download card appears on right
        glide_t = min(1.0, t * 2.5)
        phone_x = int(((1920 - phone_w) // 2) - 280 * glide_t)
        curr_phone = tex_home_done

        # Right side Store card
        card_x = phone_x + phone_w + 80
        card_y = base_phone_y + 80
        draw.rounded_rectangle([card_x + 6, card_y + 6, card_x + 580 + 6, card_y + 440 + 6], radius=24, fill="#000000")
        draw.rounded_rectangle([card_x, card_y, card_x + 580, card_y + 440], radius=24, fill="#0F172A", outline="#334155", width=3)

        draw.rounded_rectangle([card_x + 40, card_y + 36, card_x + 240, card_y + 70], radius=8, fill=COLOR_LIME, outline="#09090B", width=2)
        draw.text((card_x + 56, card_y + 44), "★ v2.0.0 READY TO INSTALL", fill=COLOR_DARK, font=get_font(FONT_BOLD, 12))

        draw.text((card_x + 40, card_y + 90), "Download Habito", fill="#FFFFFF", font=get_font(FONT_BOLD, 36))
        draw.text((card_x + 40, card_y + 135), "100% Free • Open Source • Privacy-First", fill="#94A3B8", font=get_font(FONT_BOLD, 16))

        # APK Button
        draw.rounded_rectangle([card_x + 40, card_y + 180, card_x + 540, card_y + 250], radius=16, fill=COLOR_LIME, outline="#09090B", width=2)
        draw.text((card_x + 60, card_y + 200), "📦 Download Universal APK (84 MB)", fill=COLOR_DARK, font=get_font(FONT_BOLD, 18))
        draw.text((card_x + 60, card_y + 226), "Direct install on any Android phone • Zero sign-up", fill="#1E293B", font=get_font(FONT_REGULAR, 12))

        # AAB Button
        draw.rounded_rectangle([card_x + 40, card_y + 270, card_x + 540, card_y + 340], radius=16, fill=COLOR_YELLOW, outline="#09090B", width=2)
        draw.text((card_x + 60, card_y + 290), "🏪 Download Google Play AAB Bundle", fill=COLOR_DARK, font=get_font(FONT_BOLD, 18))
        draw.text((card_x + 60, card_y + 316), "Official Google Play Console Store package", fill="#1E293B", font=get_font(FONT_REGULAR, 12))

        # GitHub Repo Link
        draw.text((card_x + 40, card_y + 380), "github.com/dev-vasu/Habito", fill="#60A5FA", font=get_font(FONT_BOLD, 18))

    # Paste Phone
    img.paste(curr_phone, (phone_x, base_phone_y), curr_phone)

    # Render Pointer Cursor if active
    if touch_pointer:
        px, py = touch_pointer
        r = 16 if not pointer_click else 12
        draw.ellipse([px - r, py - r, px + r, py + r], fill="#09090B", outline=COLOR_LIME if pointer_click else "#FFFFFF", width=3)
        if pointer_click:
            # Tap ripple animation
            draw.ellipse([px - 28, py - 28, px + 28, py + 28], outline=COLOR_LIME, width=2)

    # 3. Floating Lower-Third HUD (Glassmorphism Caption Capsule)
    hud_w, hud_h = 1300, 110
    hud_x = (1920 - hud_w) // 2
    hud_y = 930

    draw.rounded_rectangle([hud_x + 4, hud_y + 4, hud_x + hud_w + 4, hud_y + hud_h + 4], radius=24, fill="#020617")
    draw.rounded_rectangle([hud_x, hud_y, hud_x + hud_w, hud_y + hud_h], radius=24, fill="#0B1120", outline="#1E293B", width=2)

    # Soundwave visualizer bars
    wave_x = hud_x + 40
    wave_y = hud_y + 30
    for wi in range(12):
        wh = int(8 + 24 * abs(math.sin(t * 18 + wi * 0.8)))
        draw.rounded_rectangle([wave_x + wi * 8, wave_y + 24 - wh//2, wave_x + wi * 8 + 4, wave_y + 24 + wh//2], radius=2, fill=COLOR_LIME)

    # Title & Speech
    draw.text((hud_x + 160, hud_y + 20), scene["title"].upper(), fill="#FFFFFF", font=get_font(FONT_BOLD, 17))
    
    # Subtitle speech
    speech_text = scene["speech"]
    if len(speech_text) > 115:
        idx_sp = speech_text[:115].rfind(" ")
        l1 = speech_text[:idx_sp]
        l2 = speech_text[idx_sp:].strip()
        draw.text((hud_x + 160, hud_y + 48), f'"{l1}', fill="#94A3B8", font=get_font(FONT_REGULAR, 15))
        draw.text((hud_x + 160, hud_y + 72), f'{l2}"', fill="#94A3B8", font=get_font(FONT_REGULAR, 15))
    else:
        draw.text((hud_x + 160, hud_y + 54), f'"{speech_text}"', fill="#94A3B8", font=get_font(FONT_REGULAR, 15))

    img.save(output_path, quality=92)

async def main():
    print("=== BUILDING CINEMATIC LAUNCH WALKTHROUGH VIDEO ===")
    segment_mp4s = []
    fps = 30

    for i, scene in enumerate(SCENES):
        print(f"\n[Scene {i+1}/{len(SCENES)}]: {scene['id']} ({scene['chapter']})")
        audio_file = TEMP_DIR / f"{scene['id']}.mp3"
        if not audio_file.exists():
            await generate_speech(scene["speech"], audio_file)

        duration = get_audio_duration(audio_file)
        target_duration = duration + 0.6
        total_frames = int(target_duration * fps)
        print(f"  Duration: {target_duration:.2f}s -> {total_frames} frames @ {fps}fps")

        frames_dir = TEMP_DIR / f"frames_{scene['id']}"
        frames_dir.mkdir(parents=True, exist_ok=True)

        for f_idx in range(total_frames):
            frame_img = frames_dir / f"frame_{f_idx:05d}.jpg"
            render_cinematic_frame(scene, f_idx, total_frames, frame_img)

        # Encode segment with ffmpeg
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
        print(f"  [OK] Encoded: {segment_mp4}")
        segment_mp4s.append(segment_mp4)

    # Concat
    print("\n--- Stitching all scenes into final video ---")
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
    print(f"\n[SUCCESS] Generated Cinematic Launch Video: {final_mp4}")

    # Generate updated README GIF
    print("\n--- Generating updated README preview GIF ---")
    gif_file = MEDIA_DIR / "habito_v2_walkthrough.gif"
    gif_cmd = [
        "ffmpeg", "-y",
        "-i", str(final_mp4),
        "-vf", "fps=3,scale=720:-1:flags=lanczos,split[s0][s1];[s0]palettegen=max_colors=128[p];[s1][p]paletteuse=dither=bayer",
        str(gif_file)
    ]
    subprocess.run(gif_cmd, check=True)
    print(f"[SUCCESS] Generated GIF: {gif_file}")

    # Poster
    poster_png = MEDIA_DIR / "habito_v2_video_poster.png"
    poster_cmd = [
        "ffmpeg", "-y",
        "-i", str(final_mp4),
        "-ss", "00:00:20",
        "-vframes", "1",
        str(poster_png)
    ]
    subprocess.run(poster_cmd, check=True)
    print(f"[SUCCESS] Extracted Poster: {poster_png}")

if __name__ == "__main__":
    asyncio.run(main())
