# 🦚 অসমীয়া শিক্ষা — Learn Assamese

An interactive Assamese language learning app built with Streamlit.  
Learn Assamese from **Bengali** and **English** with daily lessons, voice practice, exercises, and weekly tests.

---

## ✨ Features

| Feature | Details |
|---|---|
| 📅 Daily Lessons | 7 themed lessons — family, greetings, food, numbers, colours, daily activities |
| 🔤 Alphabet | Full vowel & consonant grid with audio |
| 🗣️ Voice Practice | Listen to every word and phrase |
| 🃏 Flashcards | Flip-card vocabulary practice |
| 🔗 Matching | Match Assamese words to meanings |
| ✍️ Fill-in-the-blank | Sentence completion exercises |
| 📝 Weekly Test | 10-question quiz with detailed results |
| 📊 Progress | XP, streaks, level, badges, charts |
| ℹ️ Culture | Assam facts, festivals, tea culture |

---

## 🚀 Deploy on Streamlit Cloud (3 steps)

### Step 1 — Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit — Assamese learning app"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/assamese-app.git
git push -u origin main
```

### Step 2 — Deploy on Streamlit Cloud

1. Go to **[share.streamlit.io](https://share.streamlit.io)**
2. Click **"New app"**
3. Select your GitHub repo and branch (`main`)
4. Set **Main file path** to: `app.py`
5. Click **"Deploy!"**

### Step 3 — (Optional) Add API key for AI features

In Streamlit Cloud → your app → **Settings → Secrets**, add:

```toml
ANTHROPIC_API_KEY = "sk-ant-..."
```

---

## 🖥️ Run locally

```bash
# Clone / enter the folder
cd assamese_app

# Install dependencies
pip install -r requirements.txt

# Run
streamlit run app.py
```

---

## 📁 Project Structure

```
assamese_app/
├── app.py                  ← Main Streamlit app (all pages)
├── requirements.txt        ← Python dependencies
├── .streamlit/
│   ├── config.toml         ← Theme & server config
│   └── secrets.toml        ← API keys (not committed)
├── data/
│   ├── __init__.py
│   └── language_data.py    ← Vocabulary, lessons, quiz data
└── utils/
    ├── __init__.py
    └── helpers.py          ← Session state, XP, CSS, TTS
```

---

## 🌿 Language Notes

- Assamese script is closely related to Bengali but has **unique characters**: `ৰ` (ro) and `ৱ` (wo)
- The sounds `শ / ষ / স` are all pronounced **"x"** (like "sh") in Assamese
- Assamese uses `মই` (moi) for "I", unlike Bengali `আমি` (ami)
- Voice audio uses Hindi TTS as the closest available approximation

---

*Made with ❤️ for learners of Assamese — অসম · আসাম · Assam*
