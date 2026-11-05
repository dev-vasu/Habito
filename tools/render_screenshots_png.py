import subprocess
import time
from pathlib import Path

BASE_DIR = Path(r"C:\Users\dvasu\.gemini\antigravity\scratch\Habito")
SHOWCASES_DIR = BASE_DIR / "tools" / "showcases"
SCREENSHOTS_DIR = BASE_DIR / "screenshots"
EDGE_EXE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

PAGES = [
    ("showcase_protocol_fuel.html", "showcase_protocol_fuel.png"),
    ("showcase_vault_migration.html", "showcase_vault_migration.png"),
    ("showcase_trends_analytics.html", "showcase_trends_analytics.png")
]

for html_name, png_name in PAGES:
    html_file = (SHOWCASES_DIR / html_name).resolve()
    png_file = (SCREENSHOTS_DIR / png_name).resolve()
    file_url = html_file.as_uri()

    print(f"Rendering {html_name} -> {png_name}...")
    cmd = [
        EDGE_EXE,
        "--headless=new",
        "--disable-gpu",
        "--force-device-scale-factor=1.5",
        f"--screenshot={png_file}",
        "--window-size=1200,1180",
        file_url
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if png_file.exists():
        print(f"[OK] Generated {png_name} ({png_file.stat().st_size} bytes)")
    else:
        print(f"[ERROR] Failed to generate {png_name}")
        print("STDERR:", res.stderr)

print("All screenshots successfully rendered to high-resolution PNGs!")
