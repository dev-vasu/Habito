import asyncio
from pathlib import Path
import edge_tts

BASE_DIR = Path(r"C:\Users\dvasu\.gemini\antigravity\scratch\Habito")
TEMP_DIR = BASE_DIR / "media" / "cinematic_temp"
TEMP_DIR.mkdir(parents=True, exist_ok=True)

SCENES = [
    {
        "id": "scene1_intro",
        "speech": "Welcome to Habito version two. Engineered with an authentic neo-brutalist identity and dynamic mobile experience, Habito turns daily routine into unstoppable momentum."
    },
    {
        "id": "scene2_checkin",
        "speech": "Complete your daily protocols with satisfying tactile micro-interactions. As you check off habits, your live fuel meter surges in real time, and the Dynamic Island celebrates your streak momentum."
    },
    {
        "id": "scene3_audit",
        "speech": "Tap into the Effort Audit tab to inspect your true consistency. With zero fake data, Habito calculates your seven-day momentum curves and protects long streaks with active freeze shields."
    },
    {
        "id": "scene4_vault",
        "speech": "Switching phones? Switch to the Sync tab. Habito generates an eight-character collision-proof key with 2.8 trillion combinations. Double-lock it with an optional four-digit PIN for instant, private cross-device migration."
    },
    {
        "id": "scene5_outro",
        "speech": "Habito version two is live, open source, and available today. Download the APK directly from GitHub Releases and master your daily routine."
    }
]

async def main():
    print("Generating TTS voice tracks...")
    for s in SCENES:
        mp3_path = TEMP_DIR / f"{s['id']}.mp3"
        print(f"Synthesizing {s['id']} -> {mp3_path.name}")
        communicate = edge_tts.Communicate(s["speech"], voice="en-US-ChristopherNeural", rate="+0%")
        await communicate.save(str(mp3_path))
    print("[SUCCESS] All voice tracks synthesized.")

if __name__ == "__main__":
    asyncio.run(main())
