"""
অসমীয়া শিক্ষা — Assamese Language Learning App
Learn Assamese from Bengali & English  |  Streamlit Cloud ready
"""

import random
import streamlit as st
import plotly.graph_objects as go

# ── page config (must be first Streamlit call) ─────────────────────────────────
st.set_page_config(
    page_title="অসমীয়া শিক্ষা · Learn Assamese",
    page_icon="🦚",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── local imports (after set_page_config) ──────────────────────────────────────
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from utils.helpers import (
    init_session_state, update_streak, add_xp,
    get_level, speak_word, inject_custom_css,
)
from data.language_data import (
    ASSAMESE_VOWELS, ASSAMESE_CONSONANTS,
    DAILY_LESSONS, QUIZ_QUESTIONS,
    GRAMMAR_RULES, CULTURAL_FACTS, MOTIVATIONAL_MESSAGES,
)

# ── bootstrap ──────────────────────────────────────────────────────────────────
init_session_state()
update_streak()
inject_custom_css()

# ══════════════════════════════════════════════════════════════════════════════
#  SIDEBAR
# ══════════════════════════════════════════════════════════════════════════════
def sidebar():
    with st.sidebar:
        st.markdown("""
        <div style='text-align:center;padding:16px 0 8px'>
          <div style='font-size:2.8em'>🦚</div>
          <div style='font-size:1.4em;font-weight:900;color:#FF6B35'>অসমীয়া শিক্ষা</div>
          <div style='font-size:.75em;color:#a7a9be;letter-spacing:1px'>LEARN ASSAMESE</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")

        if st.session_state.registered:
            name = st.session_state.user_name or "Learner"
            xp   = st.session_state.total_xp
            lvl, ass_title, en_title, nxt = get_level(xp)
            pct  = min(int(xp / nxt * 100), 100)

            st.markdown(f"<div style='font-weight:800;font-size:1.1em'>👤 {name}</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='color:#a7a9be;font-size:.85em'>Level {lvl} · {en_title}</div>", unsafe_allow_html=True)
            st.markdown(f"""
            <div class='prog-wrap'><div class='prog-fill' style='width:{pct}%'></div></div>
            <div style='font-size:.75em;color:#a7a9be'>{xp} / {nxt} XP</div>
            """, unsafe_allow_html=True)

            streak = st.session_state.streak
            st.markdown(f"""
            <div style='margin:12px 0;background:#1A1A2E;border-radius:12px;padding:10px;text-align:center'>
              <span style='font-size:1.6em'>{'🔥' if streak>0 else '💤'}</span>
              <span style='font-weight:800;font-size:1.1em;color:#FF6B35'> {streak}</span>
              <span style='color:#a7a9be;font-size:.8em'> day streak</span>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("---")

        pages = {
            "🏠 Home":          "home",
            "📅 Daily Lessons": "lessons",
            "🔤 Alphabet":      "alphabet",
            "🗣️ Voice Practice": "voice",
            "✏️ Practice":      "practice",
            "📝 Weekly Test":   "weekly_test",
            "📊 Progress":      "progress",
            "ℹ️ About Assam":   "culture",
        }

        current = st.session_state.get("page", "home")
        for label, key in pages.items():
            active = "background:rgba(255,107,53,.18);border-radius:10px;" if key == current else ""
            if st.button(label, key=f"nav_{key}", use_container_width=True):
                st.session_state.page = key
                st.rerun()

        st.markdown("---")
        st.markdown(
            f"<div style='text-align:center;font-size:.75em;color:#a7a9be'>"
            f"Made with ❤️ for Assamese Learners<br>"
            f"<span style='color:#FF6B35'>অসম · Assam</span></div>",
            unsafe_allow_html=True,
        )

# ══════════════════════════════════════════════════════════════════════════════
#  PAGE: HOME / ONBOARDING
# ══════════════════════════════════════════════════════════════════════════════
def page_home():
    if not st.session_state.registered:
        # ── Welcome / register ──
        st.markdown("""
        <div class='hero'>
          <div style='font-size:3.5em'>🦚</div>
          <h1 style='font-size:2.6em;margin:10px 0 6px'>অসমীয়া শিকক!</h1>
          <p style='font-size:1.15em;color:#a7a9be;max-width:520px;margin:auto'>
            Learn Assamese from Bengali &amp; English — daily lessons, voice practice,
            interactive exercises and weekly tests.
          </p>
        </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("### 👋 Let's get started!")
            name = st.text_input("Your name", placeholder="Enter your name...")
            lang = st.selectbox("Your native language", ["Bengali", "English", "Both"])
            if st.button("🚀 Start Learning Assamese!", use_container_width=True):
                if name.strip():
                    st.session_state.registered    = True
                    st.session_state.user_name     = name.strip()
                    st.session_state.native_language = lang
                    add_xp(10)
                    st.success("Welcome! আপোনাকে স্বাগতম! 🎉")
                    st.rerun()
                else:
                    st.warning("Please enter your name to continue.")

        # ── Feature highlights ──
        st.markdown("---")
        st.markdown("### ✨ What you'll get")
        fc1, fc2, fc3, fc4 = st.columns(4)
        for col, icon, title, desc in [
            (fc1, "📅", "Daily Lessons", "7 themed daily lessons with vocab & phrases"),
            (fc2, "🗣️", "Voice Practice", "Hear Assamese pronunciation live"),
            (fc3, "✏️", "Exercises",      "Flashcards, matching & fill-in-the-blank"),
            (fc4, "📝", "Weekly Tests",   "Test yourself every week & track progress"),
        ]:
            col.markdown(f"""
            <div class='metric-card'>
              <div style='font-size:2em'>{icon}</div>
              <div style='font-weight:800;margin:6px 0'>{title}</div>
              <div style='color:#a7a9be;font-size:.85em'>{desc}</div>
            </div>""", unsafe_allow_html=True)
        return

    # ── Dashboard (logged in) ──
    name = st.session_state.user_name
    fact = random.choice(CULTURAL_FACTS)
    mot  = random.choice(MOTIVATIONAL_MESSAGES)

    st.markdown(f"""
    <div class='hero'>
      <h1>নমস্কাৰ, {name}! 🦚</h1>
      <p style='color:#a7a9be;font-size:1.05em'>{mot}</p>
    </div>
    """, unsafe_allow_html=True)

    # ── Stats row ──
    xp    = st.session_state.total_xp
    lvl, _, en_title, nxt = get_level(xp)
    done  = len(st.session_state.completed_lessons)
    streak = st.session_state.streak
    badges = len(st.session_state.badges)

    m1, m2, m3, m4 = st.columns(4)
    for col, val, label in [
        (m1, f"🔥 {streak}", "Day Streak"),
        (m2, f"⭐ {xp}",     "Total XP"),
        (m3, f"📚 {done}",   "Lessons Done"),
        (m4, f"🏅 {badges}", "Badges Earned"),
    ]:
        col.markdown(f"""
        <div class='metric-card'>
          <div class='metric-value'>{val}</div>
          <div class='metric-label'>{label}</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Today's lesson CTA ──
    day    = st.session_state.current_day
    lesson = DAILY_LESSONS.get(day, DAILY_LESSONS[1])
    col_a, col_b = st.columns([2, 1])

    with col_a:
        st.markdown(f"""
        <div class='lesson-card'>
          <div style='color:#a7a9be;font-size:.8em;text-transform:uppercase;letter-spacing:1px'>Today · Day {day}</div>
          <h3 style='margin:8px 0 4px'>{lesson['title']}</h3>
          <p style='color:#a7a9be;margin:0'>{lesson['description']}</p>
          <div class='warn-box' style='margin-top:12px'>
            {fact['emoji']} <strong>Did you know?</strong> {fact['fact']}
          </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("▶️ Start Today's Lesson", use_container_width=True):
            st.session_state.page = "lessons"
            st.rerun()

    with col_b:
        st.markdown("#### 📆 Your Plan")
        for d in range(1, 8):
            les = DAILY_LESSONS.get(d, {})
            done_mark = "✅" if d in st.session_state.completed_lessons else ("▶️" if d == day else "🔒")
            color = "#FF6B35" if d == day else ("#2EC4B6" if d in st.session_state.completed_lessons else "#a7a9be")
            st.markdown(f"<div style='color:{color};font-size:.9em;padding:3px 0'>{done_mark} Day {d}: {les.get('title_en','Review')}</div>", unsafe_allow_html=True)

    # ── Quick vocab ──
    st.markdown("---")
    st.markdown("### 🃏 Quick Vocab — Today's Words")
    words = lesson.get("vocabulary", [])[:4]
    if words:
        cols = st.columns(len(words))
        for col, w in zip(cols, words):
            col.markdown(f"""
            <div class='vocab-card'>
              <div class='ass-text'>{w['assamese']}</div>
              <div class='translit'>/{w['transliteration']}/</div>
              <div class='bn-text'>{w['bengali']}</div>
              <div class='en-text'>{w['english']}</div>
            </div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  PAGE: DAILY LESSONS
# ══════════════════════════════════════════════════════════════════════════════
def page_lessons():
    st.markdown("## 📅 Daily Lessons")
    st.markdown("<p style='color:#a7a9be'>Complete each day's lesson to unlock the next. Earn XP and badges!</p>", unsafe_allow_html=True)

    day = st.session_state.current_day

    # Day selector
    day_options = [f"Day {d}: {DAILY_LESSONS[d]['title_en']}" for d in range(1, 8)]
    chosen = st.selectbox("Choose a lesson day:", day_options, index=day - 1)
    chosen_day = int(chosen.split(":")[0].replace("Day", "").strip())
    lesson = DAILY_LESSONS[chosen_day]

    is_done = chosen_day in st.session_state.completed_lessons
    badge_txt = "✅ Completed" if is_done else "🔓 In Progress"

    st.markdown(f"""
    <div class='lesson-card {"done" if is_done else ""}'>
      <div style='display:flex;justify-content:space-between;align-items:center'>
        <div>
          <div style='color:#a7a9be;font-size:.8em'>DAY {chosen_day} · {badge_txt}</div>
          <h2 style='margin:6px 0'>{lesson['title']}</h2>
          <p style='color:#a7a9be;margin:0'>{lesson['description']}</p>
        </div>
        <div style='font-size:3em'>{'✅' if is_done else '📖'}</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    tabs = st.tabs(["📖 Vocabulary", "💬 Phrases", "📐 Grammar", "🎯 Fun Fact"])

    # ── Vocabulary tab ──
    with tabs[0]:
        if not lesson["vocabulary"]:
            st.info("This is a review day — revisit all previous lessons and then take the Weekly Test!")
        else:
            st.markdown("#### 🔤 Today's Vocabulary")
            show_t = st.checkbox("Show transliteration", value=st.session_state.show_transliteration, key="lt_chk")
            show_n = st.checkbox("Show native language", value=st.session_state.show_native, key="ln_chk")

            for w in lesson["vocabulary"]:
                col1, col2 = st.columns([3, 1])
                with col1:
                    html = f"<div class='vocab-card'><div class='ass-text'>{w['assamese']}</div>"
                    if show_t:
                        html += f"<div class='translit'>/{w['transliteration']}/</div>"
                    if show_n and st.session_state.native_language in ("Bengali", "Both"):
                        html += f"<div class='bn-text'>বাংলা: {w['bengali']}</div>"
                    html += f"<div class='en-text'>English: {w['english']}</div></div>"
                    st.markdown(html, unsafe_allow_html=True)
                with col2:
                    st.markdown("<br><br>", unsafe_allow_html=True)
                    if st.button(f"🔊", key=f"spk_{w['assamese']}", help="Listen"):
                        speak_word(w['assamese'])

    # ── Phrases tab ──
    with tabs[1]:
        st.markdown("#### 💬 Key Phrases")
        for i, p in enumerate(lesson.get("phrases", [])):
            st.markdown(f"""
            <div class='vocab-card'>
              <div class='ass-text' style='font-size:1.5em'>{p['assamese']}</div>
              <div class='translit'>/{p['transliteration']}/</div>
              <div class='bn-text'>{p['bengali']}</div>
              <div class='en-text'>{p['english']}</div>
            </div>""", unsafe_allow_html=True)
            if st.button("🔊 Listen", key=f"phrase_spk_{i}"):
                speak_word(p['assamese'])

    # ── Grammar tab ──
    with tabs[2]:
        st.markdown("#### 📐 Grammar Note")
        st.markdown(f"""
        <div class='info-box'>
          <strong>💡 Note:</strong> {lesson['grammar_note']}
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("#### 📚 Grammar Reference — Pronouns")
        rule = GRAMMAR_RULES[0]
        cols = st.columns(4)
        headers = ["Assamese", "Transliteration", "Bengali", "English"]
        for col, h in zip(cols, headers):
            col.markdown(f"**{h}**")
        for entry in rule["rules"]:
            c1, c2, c3, c4 = st.columns(4)
            c1.markdown(f"<span class='ass-text' style='font-size:1.2em'>{entry['assamese']}</span>", unsafe_allow_html=True)
            c2.markdown(f"<span class='translit'>{entry['transliteration']}</span>", unsafe_allow_html=True)
            c3.markdown(f"<span class='bn-text'>{entry['bengali']}</span>", unsafe_allow_html=True)
            c4.markdown(entry["english"])

    # ── Fun Fact tab ──
    with tabs[3]:
        st.markdown(f"""
        <div class='warn-box' style='font-size:1.1em;padding:20px'>
          🌟 <strong>Fun Fact!</strong><br><br>
          {lesson['fun_fact']}
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        fact = random.choice(CULTURAL_FACTS)
        st.markdown(f"<div class='info-box'>{fact['emoji']} {fact['fact']}</div>", unsafe_allow_html=True)

    # ── Mark complete ──
    st.markdown("---")
    col_a, col_b = st.columns(2)
    with col_a:
        if not is_done:
            if st.button("✅ Mark Lesson Complete  (+20 XP)", use_container_width=True):
                if chosen_day not in st.session_state.completed_lessons:
                    st.session_state.completed_lessons.append(chosen_day)
                add_xp(20)
                if chosen_day == st.session_state.current_day and chosen_day < 7:
                    st.session_state.current_day += 1
                st.success("🎉 Lesson complete! +20 XP earned!")
                st.rerun()
        else:
            st.success("✅ You've already completed this lesson!")
    with col_b:
        if st.button("✏️ Go to Practice Exercises", use_container_width=True):
            st.session_state.page = "practice"
            st.rerun()

# ══════════════════════════════════════════════════════════════════════════════
#  PAGE: ALPHABET
# ══════════════════════════════════════════════════════════════════════════════
def page_alphabet():
    st.markdown("## 🔤 Assamese Alphabet")
    st.markdown("<p style='color:#a7a9be'>The Assamese script is closely related to the Bengali script but has unique characters like ৰ and ৱ.</p>", unsafe_allow_html=True)

    tab_v, tab_c = st.tabs(["🅰️ Vowels (স্বৰবৰ্ণ)", "🔡 Consonants (ব্যঞ্জনবৰ্ণ)"])

    def render_alpha_grid(items, key_prefix):
        cols = st.columns(5)
        for i, item in enumerate(items):
            with cols[i % 5]:
                st.markdown(f"""
                <div class='alpha-cell'>
                  <div class='ass-text' style='font-size:2.2em'>{item['assamese']}</div>
                  <div class='translit'>{item['transliteration']}</div>
                  <div class='bn-text' style='font-size:.95em'>{item.get('bengali','')}</div>
                  <div class='en-text'>{item['english']}</div>
                </div>""", unsafe_allow_html=True)
                if st.button("🔊", key=f"{key_prefix}_{i}", help=f"Hear {item['assamese']}"):
                    speak_word(item['assamese'])

    with tab_v:
        st.markdown("### স্বৰবৰ্ণ — Vowels")
        st.markdown("<div class='info-box'>Assamese has 11 vowels. They sound similar to Bengali vowels but with subtle differences.</div>", unsafe_allow_html=True)
        render_alpha_grid(ASSAMESE_VOWELS, "vowel")

    with tab_c:
        st.markdown("### ব্যঞ্জনবৰ্ণ — Consonants")
        st.markdown("""<div class='info-box'>
        🌟 <strong>Unique to Assamese:</strong><br>
        • <strong>ৰ</strong> (ro) — a unique rolled 'r', different from Bengali র<br>
        • <strong>ৱ</strong> (wo) — a 'w' sound, not present in Bengali<br>
        • <strong>শ/ষ/স</strong> are all pronounced as 'x' (like 'sh') in Assamese!
        </div>""", unsafe_allow_html=True)
        render_alpha_grid(ASSAMESE_CONSONANTS, "cons")

# ══════════════════════════════════════════════════════════════════════════════
#  PAGE: VOICE PRACTICE
# ══════════════════════════════════════════════════════════════════════════════
def page_voice():
    st.markdown("## 🗣️ Voice Practice")
    st.markdown("<p style='color:#a7a9be'>Listen to Assamese words and phrases. Repeat after the audio to improve your pronunciation.</p>", unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["🔤 Words", "💬 Phrases", "🔡 Alphabet Sounds"])

    with tab1:
        st.markdown("#### 🎧 Listen & Repeat — Vocabulary")
        day = st.session_state.current_day
        lesson = DAILY_LESSONS.get(day, DAILY_LESSONS[1])
        words = lesson.get("vocabulary", [])

        if not words:
            st.info("Complete Day 7 — Weekly Review. Switch to an earlier day for vocabulary.")
        else:
            sel = st.selectbox("Pick a word to hear:", [f"{w['assamese']} ({w['english']})" for w in words])
            idx = next((i for i, w in enumerate(words) if f"{w['assamese']} ({w['english']})" == sel), 0)
            w = words[idx]
            st.markdown(f"""
            <div class='vocab-card' style='text-align:center;padding:30px'>
              <div class='ass-text' style='font-size:3em'>{w['assamese']}</div>
              <div class='translit' style='font-size:1.2em'>/{w['transliteration']}/</div>
              <div class='bn-text' style='margin-top:8px'>{w['bengali']}</div>
              <div class='en-text'>{w['english']}</div>
            </div>""", unsafe_allow_html=True)

            col_a, col_b = st.columns(2)
            with col_a:
                if st.button("🔊 Listen to Word", use_container_width=True):
                    speak_word(w['assamese'])
            with col_b:
                if st.button("🔊 Listen Slowly", use_container_width=True):
                    try:
                        from gtts import gTTS
                        import io
                        tts = gTTS(text=w['assamese'], lang="hi", slow=True)
                        buf = io.BytesIO()
                        tts.write_to_fp(buf)
                        buf.seek(0)
                        st.audio(buf, format="audio/mp3")
                    except Exception:
                        speak_word(w['assamese'])

            st.markdown(f"""
            <div class='info-box' style='margin-top:16px'>
              <strong>🗣️ Pronunciation tip:</strong><br>
              In Assamese, '{w['transliteration']}' — try to say it just like the transliteration suggests.
              The 'x' sound in Assamese is like 'sh' in English.
            </div>""", unsafe_allow_html=True)

    with tab2:
        st.markdown("#### 💬 Phrase Pronunciation")
        all_phrases = []
        for d, les in DAILY_LESSONS.items():
            for p in les.get("phrases", []):
                all_phrases.append(p)

        if all_phrases:
            sel_p = st.selectbox("Pick a phrase:", [p['english'] for p in all_phrases])
            phrase = next(p for p in all_phrases if p['english'] == sel_p)
            st.markdown(f"""
            <div class='vocab-card' style='text-align:center;padding:28px'>
              <div class='ass-text' style='font-size:1.8em'>{phrase['assamese']}</div>
              <div class='translit'>/{phrase['transliteration']}/</div>
              <div class='bn-text'>{phrase['bengali']}</div>
              <div class='en-text'>{phrase['english']}</div>
            </div>""", unsafe_allow_html=True)
            if st.button("🔊 Listen to Phrase", use_container_width=True):
                speak_word(phrase['assamese'])

    with tab3:
        st.markdown("#### 🔡 Hear Each Letter")
        all_alpha = ASSAMESE_VOWELS + ASSAMESE_CONSONANTS
        cols = st.columns(6)
        for i, ch in enumerate(all_alpha):
            with cols[i % 6]:
                st.markdown(f"<div class='ass-text' style='font-size:1.8em;text-align:center'>{ch['assamese']}</div>", unsafe_allow_html=True)
                if st.button("▶", key=f"alpha_v_{i}", use_container_width=True):
                    speak_word(ch['assamese'])

# ══════════════════════════════════════════════════════════════════════════════
#  PAGE: PRACTICE EXERCISES
# ══════════════════════════════════════════════════════════════════════════════
def page_practice():
    st.markdown("## ✏️ Practice Exercises")

    tab_flash, tab_match, tab_fill = st.tabs(["🃏 Flashcards", "🔗 Matching", "✍️ Fill in the Blank"])

    # ── Flashcards ──
    with tab_flash:
        st.markdown("#### 🃏 Vocabulary Flashcards")
        st.markdown("<p style='color:#a7a9be'>Click the card to flip it and reveal the answer.</p>", unsafe_allow_html=True)

        day = st.session_state.current_day
        lesson = DAILY_LESSONS.get(day, DAILY_LESSONS[1])
        words = lesson.get("vocabulary", [])
        if not words:
            words = DAILY_LESSONS[1]["vocabulary"]

        if "fc_idx" not in st.session_state:
            st.session_state.fc_idx = 0
        if "fc_flipped" not in st.session_state:
            st.session_state.fc_flipped = False

        idx = st.session_state.fc_idx % len(words)
        w = words[idx]

        if not st.session_state.fc_flipped:
            st.markdown(f"""
            <div class='vocab-card' style='text-align:center;padding:50px 20px;min-height:180px'>
              <div class='ass-text' style='font-size:3.5em'>{w['assamese']}</div>
              <div class='translit' style='margin-top:8px'>/{w['transliteration']}/</div>
              <div style='color:#a7a9be;margin-top:16px;font-size:.9em'>Click "Flip" to see meaning</div>
            </div>""", unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class='vocab-card' style='text-align:center;padding:50px 20px;min-height:180px;border-color:#2EC4B6'>
              <div class='bn-text' style='font-size:1.8em'>{w['bengali']}</div>
              <div class='en-text' style='font-size:1.4em;margin-top:6px'>{w['english']}</div>
              <div style='color:#a7a9be;margin-top:16px;font-size:.9em'>
                Assamese: <strong style='color:#FF6B35'>{w['assamese']}</strong>
              </div>
            </div>""", unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("🔄 Flip Card", use_container_width=True):
                st.session_state.fc_flipped = not st.session_state.fc_flipped
                st.rerun()
        with col2:
            if st.button("⬅️ Previous", use_container_width=True):
                st.session_state.fc_idx = (idx - 1) % len(words)
                st.session_state.fc_flipped = False
                st.rerun()
        with col3:
            if st.button("➡️ Next", use_container_width=True):
                st.session_state.fc_idx = (idx + 1) % len(words)
                st.session_state.fc_flipped = False
                st.rerun()

        st.markdown(f"<div style='text-align:center;color:#a7a9be;margin-top:8px'>Card {idx+1} of {len(words)}</div>", unsafe_allow_html=True)
        if st.button("🔊 Hear this word", use_container_width=True):
            speak_word(w["assamese"])

    # ── Matching ──
    with tab_match:
        st.markdown("#### 🔗 Match the Word")
        st.markdown("<p style='color:#a7a9be'>Select the correct meaning for each Assamese word. Earn 5 XP per correct answer!</p>", unsafe_allow_html=True)

        day = st.session_state.current_day
        lesson = DAILY_LESSONS.get(day, DAILY_LESSONS[1])
        all_words = lesson.get("vocabulary", [])
        if not all_words:
            all_words = DAILY_LESSONS[1]["vocabulary"]

        if "match_words" not in st.session_state or st.button("🔀 New Round", key="new_match"):
            sample = random.sample(all_words, min(4, len(all_words)))
            st.session_state.match_words = sample
            st.session_state.match_answers = {}
            st.session_state.match_submitted = False

        sample = st.session_state.match_words
        all_en  = [w["english"] for w in all_words]

        for i, w in enumerate(sample):
            wrong = random.sample([e for e in all_en if e != w["english"]], min(3, len(all_en)-1))
            options = wrong + [w["english"]]
            random.shuffle(options)
            chosen = st.selectbox(
                f"{w['assamese']} ({w['transliteration']}) — {w['bengali']}",
                ["— select —"] + options,
                key=f"match_{i}_{w['assamese']}",
            )
            st.session_state.match_answers[i] = (chosen, w["english"])

        if st.button("✅ Check Answers", use_container_width=True, key="check_match"):
            score = 0
            for i, (chosen, correct) in st.session_state.match_answers.items():
                if chosen == correct:
                    st.success(f"✅ {sample[i]['assamese']} = {correct}")
                    score += 1
                else:
                    st.error(f"❌ {sample[i]['assamese']} — Correct: {correct}, You chose: {chosen}")
            add_xp(score * 5)
            st.info(f"Score: {score}/{len(sample)}  |  +{score*5} XP earned!")

    # ── Fill in the Blank ──
    with tab_fill:
        st.markdown("#### ✍️ Fill in the Blank")
        st.markdown("<p style='color:#a7a9be'>Complete the Assamese sentence. Earn 10 XP per correct answer!</p>", unsafe_allow_html=True)

        fill_exercises = [
            {"sentence": "মোৰ ___ মা।",         "blank": "মা",    "hint": "family member", "en": "My ___ is mother."},
            {"sentence": "আপোনাক ___।",          "blank": "ধন্যবাদ","hint": "gratitude",    "en": "Thank ___ to you."},
            {"sentence": "মই ভাত ___।",           "blank": "খাওঁ",  "hint": "I eat...",      "en": "I ___ rice."},
            {"sentence": "ব্ৰহ্মপুত্ৰ এখন ___ নদী।","blank": "ডাঙৰ","hint": "size",         "en": "Brahmaputra is a ___ river."},
            {"sentence": "অসম বৰ ___।",           "blank": "সুন্দৰ","hint": "appearance",    "en": "Assam is very ___."},
        ]

        if "fill_idx" not in st.session_state:
            st.session_state.fill_idx = 0
        if "fill_submitted" not in st.session_state:
            st.session_state.fill_submitted = False

        ex = fill_exercises[st.session_state.fill_idx % len(fill_exercises)]

        st.markdown(f"""
        <div class='lesson-card'>
          <div class='ass-text' style='font-size:1.6em'>{ex['sentence']}</div>
          <div class='en-text' style='margin-top:4px'>{ex['en']}</div>
          <div class='translit'>Hint: {ex['hint']}</div>
        </div>""", unsafe_allow_html=True)

        user_ans = st.text_input("Your answer (in Assamese or transliteration):", key=f"fill_{st.session_state.fill_idx}")

        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("✅ Submit Answer", use_container_width=True):
                if user_ans.strip() == ex["blank"]:
                    st.success(f"🎉 Correct! The answer is: {ex['blank']}")
                    add_xp(10)
                else:
                    st.error(f"❌ Not quite. The answer is: **{ex['blank']}**")
        with col_b:
            if st.button("➡️ Next Question", use_container_width=True):
                st.session_state.fill_idx = (st.session_state.fill_idx + 1) % len(fill_exercises)
                st.rerun()

# ══════════════════════════════════════════════════════════════════════════════
#  PAGE: WEEKLY TEST
# ══════════════════════════════════════════════════════════════════════════════
def page_weekly_test():
    st.markdown("## 📝 Weekly Test")
    st.markdown("<p style='color:#a7a9be'>Test your knowledge from the week's lessons. 10 questions — 5 XP per correct answer!</p>", unsafe_allow_html=True)

    if "wt_started" not in st.session_state:
        st.session_state.wt_started = False
    if "wt_questions" not in st.session_state:
        st.session_state.wt_questions = []
    if "wt_answers" not in st.session_state:
        st.session_state.wt_answers = {}
    if "wt_submitted" not in st.session_state:
        st.session_state.wt_submitted = False

    if not st.session_state.wt_started:
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
            <div class='lesson-card'>
              <h3>📝 Weekly Assessment</h3>
              <p style='color:#a7a9be'>
                This test covers vocabulary, greetings, grammar, and cultural knowledge
                from all 7 days of lessons. Take your time and do your best!
              </p>
              <div class='info-box'>
                ⏱️ No time limit &nbsp;|&nbsp; 10 questions &nbsp;|&nbsp; Max 50 XP
              </div>
            </div>""", unsafe_allow_html=True)
        with col2:
            past = st.session_state.weekly_test_scores
            if past:
                st.markdown("#### 📊 Past Scores")
                for i, s in enumerate(past[-5:], 1):
                    st.markdown(f"Attempt {i}: **{s}/10**")

        if st.button("🚀 Start Weekly Test", use_container_width=True):
            pool = QUIZ_QUESTIONS["beginner"] + QUIZ_QUESTIONS["intermediate"]
            st.session_state.wt_questions = random.sample(pool, min(10, len(pool)))
            st.session_state.wt_answers   = {}
            st.session_state.wt_submitted = False
            st.session_state.wt_started   = True
            st.rerun()
        return

    questions = st.session_state.wt_questions

    if not st.session_state.wt_submitted:
        st.markdown(f"<div style='color:#a7a9be;margin-bottom:16px'>Answered: {len(st.session_state.wt_answers)} / {len(questions)}</div>", unsafe_allow_html=True)

        for qi, q in enumerate(questions):
            st.markdown(f"""
            <div class='lesson-card'>
              <div style='color:#a7a9be;font-size:.8em'>Question {qi+1} of {len(questions)}</div>
              <h4 style='margin:6px 0'>{q['question']}</h4>
              {'<div class="bn-text">' + q.get('question_bn','') + '</div>' if q.get('question_bn') else ''}
            </div>""", unsafe_allow_html=True)

            ans = st.radio(
                f"Q{qi+1}",
                q["options"],
                key=f"wt_q_{qi}",
                label_visibility="collapsed",
            )
            st.session_state.wt_answers[qi] = ans

        col_sub, col_rst = st.columns(2)
        with col_sub:
            if st.button("✅ Submit Test", use_container_width=True):
                st.session_state.wt_submitted = True
                st.rerun()
        with col_rst:
            if st.button("🔄 Restart", use_container_width=True):
                st.session_state.wt_started = False
                st.rerun()

    else:
        # Results
        score = 0
        for qi, q in enumerate(questions):
            chosen = st.session_state.wt_answers.get(qi, "")
            correct_text = q["options"][q["answer"]]
            if chosen == correct_text:
                score += 1

        pct = int(score / len(questions) * 100)
        st.session_state.weekly_test_scores.append(score)
        add_xp(score * 5)

        grade = "🌟 Excellent!" if pct >= 80 else ("👍 Good job!" if pct >= 60 else "📖 Keep practising!")
        color = "#2EC4B6" if pct >= 80 else ("#FFD166" if pct >= 60 else "#EF233C")

        st.markdown(f"""
        <div class='hero'>
          <h2>{grade}</h2>
          <div style='font-size:3.5em;font-weight:900;color:{color}'>{score}/{len(questions)}</div>
          <div style='color:#a7a9be'>{pct}% correct &nbsp;|&nbsp; +{score*5} XP earned</div>
        </div>""", unsafe_allow_html=True)

        # Detailed results
        st.markdown("### 📋 Detailed Results")
        for qi, q in enumerate(questions):
            chosen = st.session_state.wt_answers.get(qi, "")
            correct_text = q["options"][q["answer"]]
            ok = chosen == correct_text
            icon = "✅" if ok else "❌"
            bg = "rgba(46,196,182,.1)" if ok else "rgba(239,35,60,.1)"
            st.markdown(f"""
            <div style='background:{bg};border-radius:12px;padding:14px;margin:6px 0'>
              <strong>{icon} Q{qi+1}: {q['question']}</strong><br>
              <span style='color:#a7a9be'>Your answer: {chosen}</span><br>
              {'<span style="color:#2EC4B6">✓ Correct!</span>' if ok else f'<span style="color:#EF233C">✗ Correct answer: {correct_text}</span>'}<br>
              <span style='color:#FFD166;font-size:.85em'>{q.get("explanation","")}</span>
            </div>""", unsafe_allow_html=True)

        col_r, col_h = st.columns(2)
        with col_r:
            if st.button("🔄 Retake Test", use_container_width=True):
                st.session_state.wt_started = False
                st.rerun()
        with col_h:
            if st.button("📅 Back to Lessons", use_container_width=True):
                st.session_state.page = "lessons"
                st.rerun()

# ══════════════════════════════════════════════════════════════════════════════
#  PAGE: PROGRESS
# ══════════════════════════════════════════════════════════════════════════════
def page_progress():
    st.markdown("## 📊 Your Progress")

    xp     = st.session_state.total_xp
    lvl, ass_title, en_title, nxt = get_level(xp)
    streak = st.session_state.streak
    done   = st.session_state.completed_lessons
    scores = st.session_state.weekly_test_scores
    badges = st.session_state.badges

    # ── Level card ──
    pct = min(int(xp / nxt * 100), 100)
    st.markdown(f"""
    <div class='hero'>
      <div style='font-size:.9em;color:#a7a9be;letter-spacing:1px;text-transform:uppercase'>Level {lvl}</div>
      <h2>{ass_title}</h2>
      <div style='color:#a7a9be'>{en_title}</div>
      <div class='prog-wrap' style='max-width:400px;margin:16px auto 6px'>
        <div class='prog-fill' style='width:{pct}%'></div>
      </div>
      <div style='color:#a7a9be;font-size:.85em'>{xp} / {nxt} XP to next level</div>
    </div>""", unsafe_allow_html=True)

    # ── Stats ──
    m1, m2, m3, m4 = st.columns(4)
    for col, val, lbl in [
        (m1, xp,              "Total XP"),
        (m2, streak,          "Day Streak"),
        (m3, len(done),       "Lessons Done"),
        (m4, len(scores),     "Tests Taken"),
    ]:
        col.markdown(f"""
        <div class='metric-card'>
          <div class='metric-value'>{val}</div>
          <div class='metric-label'>{lbl}</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col_a, col_b = st.columns(2)

    # ── Lesson progress chart ──
    with col_a:
        st.markdown("#### 📅 Lesson Completion")
        lesson_status = []
        for d in range(1, 8):
            lesson_status.append({
                "day": f"Day {d}",
                "done": 1 if d in done else 0,
                "title": DAILY_LESSONS[d]["title_en"],
            })
        days   = [l["day"] for l in lesson_status]
        values = [l["done"] for l in lesson_status]
        colors = ["#2EC4B6" if v else "#1A1A2E" for v in values]

        fig = go.Figure(go.Bar(
            x=days, y=values,
            marker_color=colors,
            text=["✅" if v else "🔒" for v in values],
            textposition="outside",
        ))
        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font_color="#FFFFFE",
            yaxis=dict(showticklabels=False, showgrid=False),
            xaxis=dict(showgrid=False),
            margin=dict(t=20, b=20),
            height=280,
            showlegend=False,
        )
        st.plotly_chart(fig, use_container_width=True)

    # ── Weekly test scores ──
    with col_b:
        st.markdown("#### 📝 Weekly Test Scores")
        if scores:
            fig2 = go.Figure(go.Scatter(
                x=[f"Test {i+1}" for i in range(len(scores))],
                y=scores,
                mode="lines+markers",
                line=dict(color="#FF6B35", width=3),
                marker=dict(size=10, color="#FF6B35"),
                fill="tozeroy",
                fillcolor="rgba(255,107,53,0.1)",
            ))
            fig2.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font_color="#FFFFFE",
                yaxis=dict(range=[0, 10], gridcolor="rgba(255,255,255,0.1)"),
                xaxis=dict(showgrid=False),
                margin=dict(t=20, b=20),
                height=280,
            )
            st.plotly_chart(fig2, use_container_width=True)
        else:
            st.markdown("""
            <div class='info-box' style='text-align:center;padding:60px'>
              <div style='font-size:2em'>📝</div>
              <p>No test scores yet.<br>Take your first weekly test!</p>
            </div>""", unsafe_allow_html=True)

    # ── Badges ──
    st.markdown("---")
    st.markdown("#### 🏅 Badges & Achievements")
    badge_meta = {
        "first_lesson":  ("📚", "First Steps",      "Completed your first lesson"),
        "five_lessons":  ("🏅", "Dedicated Learner", "Completed 5 lessons"),
        "first_century": ("🌟", "Century Learner",   "Earned 100 XP"),
        "streak_3":      ("🔥", "On Fire!",          "3-day streak"),
        "streak_7":      ("⚡", "Week Warrior",      "7-day streak"),
        "scholar":       ("🎓", "Scholar",           "Earned 500 XP"),
    }
    bcols = st.columns(6)
    for i, (bid, (icon, name, desc)) in enumerate(badge_meta.items()):
        earned = bid in badges
        alpha  = "1" if earned else "0.25"
        bcols[i % 6].markdown(f"""
        <div class='metric-card' style='opacity:{alpha}'>
          <div style='font-size:2em'>{icon}</div>
          <div style='font-weight:700;font-size:.85em'>{name}</div>
          <div style='color:#a7a9be;font-size:.7em'>{desc}</div>
        </div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  PAGE: CULTURE / ABOUT ASSAM
# ══════════════════════════════════════════════════════════════════════════════
def page_culture():
    st.markdown("## ℹ️ About Assam & Assamese Culture")

    st.markdown("""
    <div class='hero'>
      <div style='font-size:3em'>🦚</div>
      <h2>অসম — The Land of Red River and Blue Hills</h2>
      <p style='color:#a7a9be;max-width:600px;margin:auto'>
        Assam is a northeastern state of India known for its rich biodiversity,
        tea gardens, silk, and vibrant culture.
      </p>
    </div>""", unsafe_allow_html=True)

    tabs = st.tabs(["🌿 Facts", "🎊 Festivals", "🗣️ Language Differences", "🍵 Tea Culture"])

    with tabs[0]:
        st.markdown("#### 🌿 Fascinating Facts about Assam")
        for fact in CULTURAL_FACTS:
            st.markdown(f"""
            <div class='vocab-card'>
              <span style='font-size:1.5em'>{fact['emoji']}</span>
              <span style='margin-left:10px'>{fact['fact']}</span>
            </div>""", unsafe_allow_html=True)

    with tabs[1]:
        st.markdown("#### 🎊 Major Festivals")
        festivals = [
            ("Bohag Bihu", "বহাগ বিহু", "বহাগ বিহু", "April", "Assamese New Year — the most important festival, celebrated with dance and music"),
            ("Kati Bihu",  "কাতি বিহু",  "কাতি বিহু",  "October","Harvest festival with lamps and prayers for good crops"),
            ("Magh Bihu",  "মাঘ বিহু",  "মাঘ বিহু",  "January", "Winter harvest festival with bonfires and traditional feasts"),
            ("Durga Puja", "দুৰ্গা পূজা","দুর্গা পূজা","October", "Celebrated across Assam with great enthusiasm"),
            ("Eid",        "ইদ",         "ঈদ",          "Islamic Calendar", "Major Muslim festival widely celebrated in Assam"),
        ]
        for name, ass, bn, month, desc in festivals:
            st.markdown(f"""
            <div class='vocab-card'>
              <div style='display:flex;justify-content:space-between'>
                <div>
                  <strong style='color:#FF6B35;font-size:1.1em'>{name}</strong>
                  <span class='ass-text' style='font-size:1em;margin-left:10px'>{ass}</span>
                  <span class='bn-text' style='margin-left:8px'>({bn})</span>
                </div>
                <div style='color:#FFD166'>{month}</div>
              </div>
              <div style='color:#a7a9be;margin-top:6px'>{desc}</div>
            </div>""", unsafe_allow_html=True)

    with tabs[2]:
        st.markdown("#### 🗣️ Key Differences: Assamese vs Bengali")
        differences = [
            ("Pronoun for 'I'",       "মই (moi)",      "আমি (ami)"),
            ("Pronoun for 'We'",      "আমি (aami)",    "আমরা (amra)"),
            ("'র' sound",            "ৰ (unique rolled r)", "র (standard r)"),
            ("'ব' / 'ওয়' sound",   "ৱ (w sound)",   "No equivalent"),
            ("শ/ষ/স sound",         "All → x (sh)",  "Distinct sounds"),
            ("Word for 'father'",    "দেউতা (deuta)", "বাবা (baba)"),
            ("Word for 'elder bro'","ককাই (kokai)",  "দাদা (dada)"),
            ("Verb ending (I go)",  "মই যাওঁ",       "আমি যাই"),
            ("'cha' (tea)",         "চাহ (xah)",      "চা (cha)"),
            ("Script unique chars", "ৰ, ৱ",           "Not present"),
        ]
        col1, col2, col3 = st.columns(3)
        col1.markdown("**Feature**")
        col2.markdown("**Assamese 🦚**")
        col3.markdown("**Bengali 🐯**")
        st.markdown("<hr style='margin:6px 0'>", unsafe_allow_html=True)
        for feat, ass, bn in differences:
            c1, c2, c3 = st.columns(3)
            c1.markdown(f"<span style='color:#a7a9be'>{feat}</span>", unsafe_allow_html=True)
            c2.markdown(f"<span class='ass-text' style='font-size:1em;color:#FF6B35'>{ass}</span>", unsafe_allow_html=True)
            c3.markdown(f"<span class='bn-text'>{bn}</span>", unsafe_allow_html=True)

    with tabs[3]:
        st.markdown("#### 🍵 Assam Tea Culture")
        st.markdown("""
        <div class='warn-box' style='font-size:1.05em;padding:20px'>
          <strong>🍵 Assam Tea — চাহ (Xah)</strong><br><br>
          Assam is the world's largest tea-growing region. Assam tea is known for its bold,
          brisk, malty flavour. The Brahmaputra valley provides the perfect conditions —
          rich alluvial soil and heavy rainfall.<br><br>
          In Assamese culture, offering tea (চাহ) to a guest is a sign of hospitality and respect.
          Traditional Assamese tea is often served with <strong>jolpan</strong> — rice-based snacks.
        </div>

        <div class='info-box' style='margin-top:12px'>
          <strong>Key tea vocabulary:</strong><br>
          চাহ (xah) = tea &nbsp;|&nbsp;
          গাখীৰ (gaakhir) = milk &nbsp;|&nbsp;
          চেনি (xeni) = sugar &nbsp;|&nbsp;
          চাহৰ বাগান (xahor baagan) = tea garden
        </div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  ROUTER
# ══════════════════════════════════════════════════════════════════════════════
sidebar()

page = st.session_state.get("page", "home")

if   page == "home":        page_home()
elif page == "lessons":     page_lessons()
elif page == "alphabet":    page_alphabet()
elif page == "voice":       page_voice()
elif page == "practice":    page_practice()
elif page == "weekly_test": page_weekly_test()
elif page == "progress":    page_progress()
elif page == "culture":     page_culture()
else:                       page_home()
