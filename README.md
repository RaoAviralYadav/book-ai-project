# 📚 Automated Book Publication Workflow (AI-Powered)

This project is an end-to-end AI system to automate and enhance the book-writing pipeline. It fetches raw book chapters, spins/rephrases them using LLMs, performs quality review, evaluates output with reinforcement-like scoring, and stores semantic versions for future queries — all wrapped in a beautiful Streamlit interface.

<br/>

> 🌐 **Demo Video**: [https://drive.google.com/file/d/1KmI_nz6ejktOL7TaS6NTzbbLmu7lVW_E/view?usp=sharing](https://drive.google.com/file/d/1KmI_nz6ejktOL7TaS6NTzbbLmu7lVW_E/view?usp=sharing)

---

## 🚀 Project Overview

This project streamlines the manual labor of rewriting and editing public domain books. From scraping content to spinning AI-generated drafts, reviewing improvements, scoring quality via reinforcement learning, and storing semantic versions—this system is built to serve researchers, content creators, and automation developers alike.

---

## 🛠️ Tech Stack

| Layer                  | Tools Used |
|-----------------------|------------|
| Web Scraping          | `Playwright` |
| Language Models       | `Gemini 2.5 pro` |
| Feedback Engine       | `LanguageTool`, custom scoring |
| Reinforcement Learning| Custom `reward_model` |
| Vector DB & Search    | `ChromaDB` |
| Interface             | `Streamlit` |
| Backend/API Support   | `FastAPI`, `Langchain` |
| Code Management       | `Python`, `venv` |

---

## 🚀 Features

- 🔍 **Web Scraping with Playwright** – Fetch chapters from web sources
- ✍️ **AI-Based Chapter Spinner** – Rewrite raw text with improved style or tone
- 🧠 **Automated Reviewer** – Simple feedback engine scoring quality
- 🏆 **RL-based Reward Engine** – Rate content with reward scores
- 🧬 **Semantic Versioning (ChromaDB)** – Search past versions by theme, style, etc.
- 🌐 **Streamlit UI** – User-friendly web interface for the complete pipeline
- 💾 **Version Manager** – Save, load, and compare versions of chapters

---

## ⚙️ Setup & Installation

> ✅ Prerequisites: Python 3.10+, Git, Node.js (for Playwright setup)

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/book-ai-project.git
   cd book-ai-project


