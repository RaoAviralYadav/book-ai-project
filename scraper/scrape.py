from playwright.sync_api import sync_playwright
import time

def fetch_chapter_content(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        
        # Wait a bit for content to load
        time.sleep(2)
        
        content = page.inner_text("body")
        page.screenshot(path="chapter1.png", full_page=True)
        browser.close()
    return content

if __name__ == "__main__":
    url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
    text = fetch_chapter_content(url)
    with open("chapter1.txt", "w", encoding='utf-8') as f:
        f.write(text)
    print("Chapter content and screenshot saved.")

# scraper/scrape.py
# import os
# from playwright.sync_api import sync_playwright
# import time

# # Create folders if they don't exist
# os.makedirs("output/screenshots", exist_ok=True)
# os.makedirs("output/chapters", exist_ok=True)

# def fetch_chapter_content(url, chapter_name="chapter1"):
#     with sync_playwright() as p:
#         browser = p.chromium.launch()
#         page = browser.new_page()
#         page.goto(url)
        
#         time.sleep(2)
        
#         content = page.inner_text("body")
#         page.screenshot(path=f"output/screenshots/{chapter_name}.png", full_page=True)
#         browser.close()

#     with open(f"output/chapters/{chapter_name}.txt", "w", encoding='utf-8') as f:
#         f.write(content)

#     return content
