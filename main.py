"""
DeepCashFlow - Autopilot AI Content System
Jalankan: python main.py
"""
import os
import sys
import json
import traceback
from datetime import datetime

from agents.deepseek_trend import TrendFinder
from agents.claude_writer import ScriptWriter
from agents.media_factory import MediaFactory
from agents.poster import ContentPoster
from utils.sheets_logger import SheetsLogger
from config.settings import Settings

def main():
    print(f"\n{'='*50}")
    print(f"  DeepCashFlow Autopilot - {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"{'='*50}\n")

    settings = Settings()
    logger = SheetsLogger(settings)

    # 1. Temukan trending topic
    print("[1/5] Mencari trending topic...")
    trend_finder = TrendFinder(settings)
    topics = trend_finder.get_trending_topics(count=3)
    if not topics:
        print("  ⚠️ Tidak ada trending topic ditemukan, menggunakan fallback.")
        topics = settings.FALLBACK_TOPICS

    print(f"  ✅ Topik: {', '.join(topics[:3])}")

    # 2. Generate naskah dengan Claude
    print("\n[2/5] Membuat naskah konten...")
    writer = ScriptWriter(settings)
    scripts = []
    for topic in topics[:2]:  # buat 2 konten per hari
        script = writer.generate_script(topic)
        if script:
            scripts.append({"topic": topic, "script": script})
            print(f"  ✅ Naskah untuk: {topic}")

    if not scripts:
        print("  ❌ Gagal membuat naskah. Cek CLAUDE_API_KEY.")
        sys.exit(1)

    # 3. Buat media (gambar/video thumbnail)
    print("\n[3/5] Membuat media visual...")
    media_factory = MediaFactory(settings)
    results = []
    for item in scripts:
        media_path = media_factory.create_thumbnail(item["topic"], item["script"])
        item["media_path"] = media_path
        print(f"  ✅ Media: {media_path}")
        results.append(item)

    # 4. Post ke semua platform
    print("\n[4/5] Memposting ke platform...")
    poster = ContentPoster(settings)
    post_results = []
    for item in results:
        result = poster.post_all(item)
        post_results.append(result)
        logger.log(item["topic"], result)

    # 5. Summary
    print("\n[5/5] Ringkasan:")
    for r in post_results:
        for platform, status in r.items():
            icon = "✅" if status.get("success") else "❌"
            print(f"  {icon} {platform}: {status.get('message', '-')}")

    print(f"\n{'='*50}")
    print("  Autopilot selesai! Sampai besok 🚀")
    print(f"{'='*50}\n")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        traceback.print_exc()
        sys.exit(1)
