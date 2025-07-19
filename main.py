import os
import sys
from scraper.scrape import fetch_chapter_content
from ai_modules.writer import spin_chapter
from ai_modules.reviewer import review_text
from rl.reward_engine import compute_reward
from storage.version_store import save_version
from storage.semantic_store import store_semantic_version


if len(sys.argv) > 1:
    URL = sys.argv[1]
else:
    URL = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"

if __name__ == "__main__":
    print("Fetching original content...")
    original = fetch_chapter_content(URL)

    print("Spinning chapter with AI...")
    spun = spin_chapter(original)

    print("Reviewing spun chapter...")
    review = review_text(original, spun)

    print("Calculating reward...")
    reward = compute_reward(original, spun)

    print("Scores:")
    print(f"  Original Score: {review['original_score']:.1f}")
    print(f"  Spun Score: {review['spun_score']:.1f}")
    print(f"  Improvement: {review['improvement']:.1f}")
    print(f"  Feedback: {review['feedback']}")
    print(f"  Reward Score: {reward:.1f}")

    
    chapter_name = URL.rstrip('/').split('/')[-1]

    
    filename = save_version(spun, reward, chapter_name=chapter_name)
    print(f"Saved version file: {filename}")

    
    store_semantic_version(filename, spun, metadata={'reward': reward, 'url': URL})
    print("Indexed semantic version.")

