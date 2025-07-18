import os
import sys
import subprocess
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from datetime import datetime
import streamlit as st
from scraper.scrape import fetch_chapter_content
from ai_modules.writer import spin_chapter
from ai_modules.reviewer import review_text
from rl.reward_engine import compute_reward
from storage.version_store import load_versions, save_version
from storage.semantic_store import store_semantic_version, query_semantic_versions


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

st.set_page_config(page_title="Book AI Workflow", layout="wide")
st.title("📖 Automated Book Publication Workflow")


url = st.sidebar.text_input(
    "Chapter URL", 
    "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
)
if st.sidebar.button("Fetch & Spin"):
    with st.spinner("Scraping content..."):
        result = subprocess.run(
            [sys.executable, os.path.join(os.path.dirname(__file__), '..', 'scraper', 'scrape.py'), url],
            capture_output=True, text=True
        )
        if result.returncode != 0:
            st.error(f"Scraping failed: {result.stderr}")
        else:
            base = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
            with open(os.path.join(base, 'chapter1.txt'), 'r', encoding='utf-8') as f:
                original = f.read()
            st.session_state['original'] = original
            st.image(os.path.join(base, 'chapter1.png'), caption="Screenshot of Chapter")
    if 'original' in st.session_state:
        with st.spinner("Spinning with AI..."):
            spun = spin_chapter(st.session_state['original'])
            st.session_state['spun'] = spun
            st.session_state['review'] = review_text(st.session_state['original'], spun)


if 'original' in st.session_state and 'spun' in st.session_state:
    col1, col2 = st.columns(2)
    with col1:
        st.header("📝 Original Chapter")
        st.text_area("", st.session_state['original'], height=300)
    with col2:
        st.header("✍️ AI-Spun Chapter")
        edited = st.text_area("Edit this version:", st.session_state['spun'], height=300)

    
    review = st.session_state['review']
    st.subheader("Reviewer Feedback")
    st.write(review)
    reward = compute_reward(st.session_state['original'], edited)
    st.markdown(f"**Reward Score:** {reward:.1f}")

    
    if st.button("Save Version"):
        vid = datetime.utcnow().isoformat()
        save_version(edited)
        store_semantic_version(vid, edited)
        st.success("Version saved to history and semantic DB!")
        st.experimental_rerun()

st.sidebar.subheader("Semantic Search")
query = st.sidebar.text_input("Find similar versions:")
if query:
    results = query_semantic_versions(query)
    for vid, doc in zip(results['ids'], results['documents']):
        st.sidebar.markdown(f"**{vid}**: {doc[:100]}...")

