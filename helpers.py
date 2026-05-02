"""Utility helpers for Assamese Language Learning App."""
import io
import streamlit as st
from datetime import date, timedelta


def init_session_state():
    defaults = {
        "registered": False,
        "user_name": "",
        "native_language": "Bengali",
        "current_day": 1,
        "completed_lessons": [],
        "quiz_scores": [],
        "streak": 0,
        "last_login": "",
        "total_xp": 0,
        "badges": [],
        "weekly_test_scores": [],
        "show_transliteration": True,
        "show_native": True,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


def update_streak():
    today = str(date.today())
    last = st.session_state.get("last_login", "")
    if last == today:
        return
    yesterday = str(date.today() - timedelta(days=1))
    st.session_state.streak = (st.session_state.streak + 1) if last == yesterday else 1
    st.session_state.last_login = today


def add_xp(points):
    st.session_state.total_xp = st.session_state.get("total_xp", 0) + points
    _check_badges()


def _check_badges():
    badges = st.session_state.badges
    xp = st.session_state.total_xp
    streak = st.session_state.streak
    lessons = len(st.session_state.completed_lessons)
    checks = [
        ("first_lesson",  lessons >= 1,  "📚 First Steps",      "Completed your first lesson!"),
        ("five_lessons",  lessons >= 5,  "🏅 Dedicated",        "Completed 5 lessons!"),
        ("first_century", xp >= 100,     "🌟 Century Learner",  "Earned 100 XP!"),
        ("streak_3",      streak >= 3,   "🔥 On Fire!",         "3-day streak!"),
        ("streak_7",      streak >= 7,   "⚡ Week Warrior",     "7-day streak!"),
        ("scholar",       xp >= 500,     "🎓 Scholar",          "Earned 500 XP!"),
    ]
    for bid, cond, name, desc in checks:
        if cond and bid not in badges:
            badges.append(bid)
            st.toast(f"🎉 Badge unlocked: {name} — {desc}", icon="🏆")


def get_level(xp):
    levels = [
        (1, "নতুন শিক্ষাৰ্থী",      "Beginner",       100),
        (2, "উদীয়মান শিক্ষাৰ্থী", "Rising Learner", 300),
        (3, "মধ্যবৰ্তী",            "Intermediate",   600),
        (4, "দক্ষ শিক্ষাৰ্থী",     "Skilled",        1000),
        (5, "অসমীয়া বিশেষজ্ঞ",    "Expert",         9999),
    ]
    thresholds = [100, 300, 600, 1000, 9999]
    for i, (lvl, ass, en, nxt) in enumerate(levels):
        if xp < thresholds[i]:
            return lvl, ass, en, nxt
    return 5, "অসমীয়া বিশেষজ্ঞ", "Expert", 9999


def speak_word(text: str):
    try:
        from gtts import gTTS
        tts = gTTS(text=text, lang="hi", slow=False)
        buf = io.BytesIO()
        tts.write_to_fp(buf)
        buf.seek(0)
        st.audio(buf, format="audio/mp3")
    except Exception:
        st.info(f"🔊 {text}")


def inject_custom_css():
    st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@400;600;700&family=Nunito:wght@400;600;700;800;900&family=Space+Grotesk:wght@400;500;600;700&display=swap');

:root{
  --primary:#FF6B35;--primary-dim:rgba(255,107,53,.15);
  --success:#2EC4B6;--warn:#FFD166;--danger:#EF233C;
  --bg:#0F0E17;--card:#1A1A2E;--card2:#16213E;
  --text:#FFFFFE;--muted:#a7a9be;
  --grad:linear-gradient(135deg,#FF6B35,#F7C59F);
}

.stApp{background:var(--bg)!important;font-family:'Nunito',sans-serif;color:var(--text)!important;}
h1,h2,h3,h4{color:var(--text)!important;}
p,li,label,span{color:var(--text);}
.main .block-container{padding-top:1.2rem;max-width:1100px;}
#MainMenu,footer,header{visibility:hidden;}
::-webkit-scrollbar{width:5px;}
::-webkit-scrollbar-thumb{background:var(--primary);border-radius:3px;}

section[data-testid="stSidebar"]{background:var(--card)!important;border-right:1px solid rgba(255,107,53,.2);}
section[data-testid="stSidebar"] *{color:var(--text)!important;}

.stButton>button{background:var(--grad)!important;color:#fff!important;border:none!important;border-radius:12px!important;font-weight:700!important;transition:all .2s!important;}
.stButton>button:hover{transform:translateY(-2px)!important;box-shadow:0 6px 20px rgba(255,107,53,.4)!important;}

.stTabs [data-baseweb="tab-list"]{background:var(--card)!important;border-radius:12px!important;padding:4px!important;}
.stTabs [data-baseweb="tab"]{color:var(--muted)!important;border-radius:8px!important;}
.stTabs [aria-selected="true"]{background:var(--primary)!important;color:#fff!important;}

.vocab-card{background:var(--card);border:1px solid rgba(255,107,53,.25);border-radius:16px;padding:16px 20px;margin:8px 0;position:relative;overflow:hidden;transition:all .3s;}
.vocab-card::before{content:'';position:absolute;top:0;left:0;width:4px;height:100%;background:var(--grad);}
.vocab-card:hover{border-color:var(--primary);transform:translateY(-2px);box-shadow:0 8px 28px rgba(255,107,53,.18);}

.lesson-card{background:var(--card);border:1px solid rgba(255,107,53,.2);border-radius:18px;padding:22px;margin:12px 0;transition:all .3s;}
.lesson-card:hover{border-color:var(--primary);box-shadow:0 8px 28px rgba(255,107,53,.18);transform:translateY(-3px);}
.lesson-card.done{border-color:var(--success);}

.metric-card{background:var(--card);border:1px solid rgba(255,107,53,.2);border-radius:16px;padding:18px;text-align:center;}
.metric-value{font-size:2.4em;font-weight:900;color:var(--primary);font-family:'Space Grotesk',sans-serif;line-height:1.1;}
.metric-label{color:var(--muted);font-size:.78em;text-transform:uppercase;letter-spacing:1px;margin-top:4px;}

.hero{background:linear-gradient(135deg,rgba(255,107,53,.12),rgba(26,26,46,.95));border:1px solid rgba(255,107,53,.3);border-radius:22px;padding:36px;text-align:center;margin-bottom:24px;}

.ass-text{font-family:'Hind Siliguri','Nunito',serif;font-size:2em;color:var(--primary);font-weight:700;line-height:1.3;}
.translit{font-family:'Space Grotesk',monospace;color:#F7C59F;font-size:.95em;font-style:italic;}
.bn-text{color:var(--success);font-size:1.1em;}
.en-text{color:var(--muted);font-size:.9em;}

.info-box{background:rgba(46,196,182,.1);border:1px solid rgba(46,196,182,.3);border-radius:12px;padding:14px;margin:8px 0;}
.warn-box{background:rgba(255,209,102,.1);border:1px solid rgba(255,209,102,.3);border-radius:12px;padding:14px;margin:8px 0;font-style:italic;}

.prog-wrap{background:rgba(255,255,255,.08);border-radius:20px;height:10px;margin:6px 0;overflow:hidden;}
.prog-fill{height:100%;border-radius:20px;background:var(--grad);transition:width .5s ease;}

.xp-badge{display:inline-block;background:var(--grad);color:#fff;font-weight:800;padding:3px 13px;border-radius:20px;font-size:.82em;letter-spacing:.8px;}

.streak{font-size:2.2em;text-align:center;animation:pulse 2s infinite;}
@keyframes pulse{0%,100%{transform:scale(1);}50%{transform:scale(1.12);}}

.alpha-cell{background:var(--card);border:1px solid rgba(255,107,53,.2);border-radius:10px;padding:12px 8px;text-align:center;transition:all .2s;}
.alpha-cell:hover{border-color:var(--primary);background:var(--primary-dim);}

.stSelectbox>div>div{background:var(--card)!important;color:var(--text)!important;border-color:rgba(255,107,53,.3)!important;}
.stTextInput>div>div>input{background:var(--card)!important;color:var(--text)!important;border-color:rgba(255,107,53,.3)!important;}
</style>
""", unsafe_allow_html=True)
