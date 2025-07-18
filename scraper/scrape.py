from playwright.sync_api import sync_playwright
import time

def fetch_chapter_content(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        
        
        time.sleep(2)
        
        content = page.inner_text("body")
        page.screenshot(path="chapter1.png", full_page=True)
        browser.close()
    return content

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1" 

    text = fetch_chapter_content(url)
    with open("chapter1.txt", "w", encoding='utf-8') as f:
        f.write(text)
    print("Chapter content and screenshot saved.")
