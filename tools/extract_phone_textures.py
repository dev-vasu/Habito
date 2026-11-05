from PIL import Image
from pathlib import Path

base = Path(r"C:\Users\dvasu\.gemini\antigravity\scratch\Habito")
scr = base / "screenshots"
tex_dir = base / "media" / "textures"
tex_dir.mkdir(parents=True, exist_ok=True)

# 1. State 1 & State 2 from video_states.png
im_states = Image.open(scr / "video_states.png").convert("RGBA")
# State 1 is at top center, State 2 is below
# Let's find bounding boxes of the phones
# Find first phone (State 1)
# Bounding box of phone 1 is approx x: 560 to 1240, y: 40 to 1420
w, h = im_states.size

def find_phone_box(im, start_y, end_y):
    min_x, min_y, max_x, max_y = w, end_y, 0, start_y
    for y in range(start_y, end_y, 4):
        for x in range(0, w, 4):
            r, g, b, a = im.getpixel((x, y))
            # detect the cream background #FFFDF0
            if r > 240 and g > 240 and b > 220:
                if x < min_x: min_x = x
                if x > max_x: max_x = x
                if y < min_y: min_y = y
                if y > max_y: max_y = y
    # expand by 14px to include the titanium bezel
    return (max(0, min_x - 14), max(0, min_y - 14), min(w, max_x + 14), min(end_y, max_y + 14))

box1 = find_phone_box(im_states, 0, 1500)
print("Phone 1 box:", box1)
phone1 = im_states.crop(box1)
phone1.save(tex_dir / "phone_home_initial.png")

box2 = find_phone_box(im_states, 1450, h)
print("Phone 2 box:", box2)
phone2 = im_states.crop(box2)
phone2.save(tex_dir / "phone_home_checked.png")

# 2. Audit Phone from showcase_trends_analytics.png
im_audit = Image.open(scr / "showcase_trends_analytics.png").convert("RGBA")
w_a, h_a = im_audit.size
def find_phone_in_showcase(im):
    w, h = im.size
    min_x, min_y, max_x, max_y = w, h, 0, 0
    for y in range(150, h - 50, 4):
        for x in range(w // 4, 3 * w // 4, 4):
            r, g, b, a = im.getpixel((x, y))
            if r > 240 and g > 240 and b > 220:
                if x < min_x: min_x = x
                if x > max_x: max_x = x
                if y < min_y: min_y = y
                if y > max_y: max_y = y
    return (max(0, min_x - 14), max(0, min_y - 14), min(w, max_x + 14), min(h, max_y + 14))

box_audit = find_phone_in_showcase(im_audit)
print("Audit box:", box_audit)
phone_audit = im_audit.crop(box_audit)
phone_audit.save(tex_dir / "phone_audit.png")

# 3. Vault Phone from showcase_vault_migration.png
im_vault = Image.open(scr / "showcase_vault_migration.png").convert("RGBA")
box_vault = find_phone_in_showcase(im_vault)
print("Vault box:", box_vault)
phone_vault = im_vault.crop(box_vault)
phone_vault.save(tex_dir / "phone_vault.png")

print("All 4 world-class phone textures extracted successfully!")
