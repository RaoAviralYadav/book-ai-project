import os, sys, subprocess
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import streamlit as st
from ai_modules.writer import spin_chapter
from ai_modules.reviewer import review_text
from storage.version_store import load_versions, save_version

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

st.set_page_config(page_title="Book AI Workflow", layout="wide")
st.title("📖 Automated Book Publication Workflow")

# Sidebar inputs
url = st.sidebar.text_input(
    "Chapter URL",
    "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
)
if st.sidebar.button("Fetch & Spin"):
    # Run scraper script externally to avoid async issues
    with st.spinner("Scraping content..."):
        result = subprocess.run(
            [sys.executable, os.path.join(PROJECT_ROOT, 'scraper', 'scrape.py'), url],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            st.error(f"Scraping failed: {result.stderr}")
        else:
            # scraper writes chapter1.txt and chapter1.png in project root
            with open(os.path.join(PROJECT_ROOT, 'chapter1.txt'), 'r', encoding='utf-8') as f:
                original = f.read()
            st.session_state['original'] = original
            st.image(os.path.join(PROJECT_ROOT, 'chapter1.png'), caption="Screenshot of Chapter")
    if 'original' in st.session_state:
        with st.spinner("Spinning with AI..."):
            spun = spin_chapter(st.session_state['original'])
            st.session_state['spun'] = spun
            review = review_text(st.session_state['original'], spun)
            st.session_state['review'] = review

# Display original and AI-spun text
if 'original' in st.session_state and 'spun' in st.session_state:
    col1, col2 = st.columns(2)
    with col1:
        st.header("📝 Original Chapter")
        st.text_area("", value=st.session_state['original'], height=400)
    with col2:
        st.header("✍️ AI-Spun Chapter")
        edited = st.text_area("Edit or refine this version:", value=st.session_state['spun'], height=400)

    # Show reviewer feedback
    review = st.session_state.get('review')
    st.markdown(f"**Reviewer Feedback:** {review['feedback']}")
    st.markdown(f"- Original Score: {review['original_score']:.1f}")
    st.markdown(f"- Spun Score: {review['spun_score']:.1f}")
    st.markdown(f"- Improvement: {review['improvement']:.1f}")

    # Save version
    if st.button("Save Version"):
        save_version(edited)
        st.success("Version saved!")
        st.experimental_rerun()

# Display version history
st.sidebar.header("Version History")
versions = load_versions()
for entry in reversed(versions[-5:]):  # show last 5
    st.sidebar.markdown(f"**{entry['timestamp']}**")
    st.sidebar.write(entry['content'][:100] + '...')


