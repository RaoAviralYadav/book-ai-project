from scraper.scrape import fetch_chapter_content
from ai_modules.writer import spin_chapter
from ai_modules.reviewer import review_text
from rl.reward_engine import compute_reward
from storage.version_store import load_versions, save_version

URL = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"

if __name__ == "__main__":
    print("📘 Fetching original content...")
    original = fetch_chapter_content(URL)

    print("✍️ Spinning chapter with AI...")
    spun = spin_chapter(original)

    with open("spun_chapter.txt", "w", encoding="utf-8") as f:
        f.write(spun)
    print("✅ Chapter spun and saved to spun_chapter.txt")

    print("🔍 Reviewing spun chapter...")
    review = review_text(original, spun)
    print(f"Original Score: {review['original_score']:.1f}")
    print(f"Spun Score: {review['spun_score']:.1f}")
    print(f"Improvement: {review['improvement']:.1f}")
    print(f"Feedback: {review['feedback']}")

