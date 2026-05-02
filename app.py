"""
অসমীয়া শিক্ষা — Assamese Language Learning App
100% self-contained single file — zero local imports — Streamlit Cloud safe.
"""

import io
import random
import streamlit as st
import plotly.graph_objects as go
from datetime import date, timedelta

st.set_page_config(
    page_title="অসমীয়া শিক্ষা · Learn Assamese",
    page_icon="🦚",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ══════════════════════════════════════════════════════════════════════════════
#  DATA
# ══════════════════════════════════════════════════════════════════════════════

ASSAMESE_VOWELS = [
    {"assamese": "অ", "transliteration": "o",  "bengali": "অ", "english": "a (as in about)"},
    {"assamese": "আ", "transliteration": "aa", "bengali": "আ", "english": "aa (long a)"},
    {"assamese": "ই", "transliteration": "i",  "bengali": "ই", "english": "i (short)"},
    {"assamese": "ঈ", "transliteration": "ii", "bengali": "ঈ", "english": "ee (long i)"},
    {"assamese": "উ", "transliteration": "u",  "bengali": "উ", "english": "u (short)"},
    {"assamese": "ঊ", "transliteration": "uu", "bengali": "ঊ", "english": "oo (long u)"},
    {"assamese": "ঋ", "transliteration": "ri", "bengali": "ঋ", "english": "ri"},
    {"assamese": "এ", "transliteration": "e",  "bengali": "এ", "english": "e (as in egg)"},
    {"assamese": "ঐ", "transliteration": "oi", "bengali": "ঐ", "english": "oi"},
    {"assamese": "ও", "transliteration": "o",  "bengali": "ও", "english": "o (as in so)"},
    {"assamese": "ঔ", "transliteration": "ou", "bengali": "ঔ", "english": "ou"},
]

ASSAMESE_CONSONANTS = [
    {"assamese": "ক", "transliteration": "k",  "bengali": "ক", "english": "k"},
    {"assamese": "খ", "transliteration": "kh", "bengali": "খ", "english": "kh"},
    {"assamese": "গ", "transliteration": "g",  "bengali": "গ", "english": "g"},
    {"assamese": "ঘ", "transliteration": "gh", "bengali": "ঘ", "english": "gh"},
    {"assamese": "ঙ", "transliteration": "ng", "bengali": "ঙ", "english": "ng"},
    {"assamese": "চ", "transliteration": "s",  "bengali": "চ", "english": "s/ch"},
    {"assamese": "ছ", "transliteration": "ss", "bengali": "ছ", "english": "sh (aspirated)"},
    {"assamese": "জ", "transliteration": "j",  "bengali": "জ", "english": "j/z"},
    {"assamese": "ঝ", "transliteration": "jh", "bengali": "ঝ", "english": "jh"},
    {"assamese": "ট", "transliteration": "t",  "bengali": "ট", "english": "t (retroflex)"},
    {"assamese": "ড", "transliteration": "d",  "bengali": "ড", "english": "d (retroflex)"},
    {"assamese": "ত", "transliteration": "t",  "bengali": "ত", "english": "t (dental)"},
    {"assamese": "দ", "transliteration": "d",  "bengali": "দ", "english": "d (dental)"},
    {"assamese": "ন", "transliteration": "n",  "bengali": "ন", "english": "n"},
    {"assamese": "প", "transliteration": "p",  "bengali": "প", "english": "p"},
    {"assamese": "ফ", "transliteration": "ph", "bengali": "ফ", "english": "ph/f"},
    {"assamese": "ব", "transliteration": "b",  "bengali": "ব", "english": "b"},
    {"assamese": "ম", "transliteration": "m",  "bengali": "ম", "english": "m"},
    {"assamese": "য", "transliteration": "j",  "bengali": "য", "english": "y/j"},
    {"assamese": "ৰ", "transliteration": "r",  "bengali": "র", "english": "r (unique to Assamese)"},
    {"assamese": "ল", "transliteration": "l",  "bengali": "ল", "english": "l"},
    {"assamese": "ৱ", "transliteration": "w",  "bengali": "ব", "english": "w (unique to Assamese)"},
    {"assamese": "শ", "transliteration": "x",  "bengali": "শ", "english": "x/sh (Assamese)"},
    {"assamese": "হ", "transliteration": "h",  "bengali": "হ", "english": "h"},
]

DAILY_LESSONS = {
    1: {
        "title": "গৃহ আৰু পৰিয়াল | Home and Family",
        "title_en": "Home & Family",
        "description": "Learn words related to home and family members",
        "vocabulary": [
            {"assamese": "ঘৰ",    "transliteration": "ghor",  "bengali": "ঘর",    "english": "home/house"},
            {"assamese": "মা",    "transliteration": "maa",   "bengali": "মা",    "english": "mother"},
            {"assamese": "দেউতা","transliteration": "deuta", "bengali": "বাবা",  "english": "father"},
            {"assamese": "ককাই", "transliteration": "kokai", "bengali": "দাদা",  "english": "elder brother"},
            {"assamese": "বাই",  "transliteration": "baai",  "bengali": "দিদি",  "english": "elder sister"},
            {"assamese": "ভাই",  "transliteration": "bhai",  "bengali": "ভাই",   "english": "younger brother"},
            {"assamese": "ভনী",  "transliteration": "bhoni", "bengali": "বোন",   "english": "younger sister"},
            {"assamese": "আইতা", "transliteration": "aaita", "bengali": "দিদিমা","english": "grandmother"},
            {"assamese": "ককা",  "transliteration": "koka",  "bengali": "দাদু",  "english": "grandfather"},
        ],
        "phrases": [
            {"assamese": "মোৰ নাম ... ।",    "transliteration": "mor naam ...",     "bengali": "আমার নাম ... ।",  "english": "My name is ..."},
            {"assamese": "আপোনাৰ নাম কি?", "transliteration": "aponaar naam ki?", "bengali": "আপনার নাম কি?", "english": "What is your name?"},
            {"assamese": "মই ... ত থাকো।",  "transliteration": "moi ... t thako",  "bengali": "আমি ... এ থাকি।","english": "I live in ..."},
        ],
        "grammar_note": "In Assamese 'মই' (moi) means 'I' and 'মোৰ' (mor) means 'my'. Unlike Bengali 'আমি', Assamese uses 'মই'.",
        "fun_fact": "🎵 Assamese is called the 'Language of the East' with a literary tradition dating to the 13th century!",
    },
    2: {
        "title": "সম্ভাষণ | Greetings & Farewells",
        "title_en": "Greetings",
        "description": "Common greetings and polite expressions",
        "vocabulary": [
            {"assamese": "নমস্কাৰ",          "transliteration": "nomoskar",       "bengali": "নমস্কার",       "english": "Hello / Greetings"},
            {"assamese": "আদাব",             "transliteration": "adab",           "bengali": "আদাব",          "english": "Salutation"},
            {"assamese": "আপোনাক ধন্যবাদ",  "transliteration": "aponake dhonyobad","bengali": "আপনাকে ধন্যবাদ","english": "Thank you"},
            {"assamese": "মাফ কৰিব",         "transliteration": "maph korib",     "bengali": "মাফ করবেন",    "english": "Excuse me / Sorry"},
            {"assamese": "হয়",              "transliteration": "hoy",            "bengali": "হ্যাঁ",         "english": "Yes"},
            {"assamese": "নহয়",             "transliteration": "nohoy",          "bengali": "না",            "english": "No"},
            {"assamese": "ভালেই আছো",        "transliteration": "bhalei aaso",    "bengali": "ভালো আছি",     "english": "I am fine"},
            {"assamese": "পুনৰ লগ পাম",      "transliteration": "punor log paam", "bengali": "আবার দেখা হবে","english": "See you again"},
        ],
        "phrases": [
            {"assamese": "আপুনি কেনে আছে?","transliteration": "apuni kene aase?","bengali": "আপনি কেমন আছেন?","english": "How are you? (formal)"},
            {"assamese": "তুমি কেনে আছা?", "transliteration": "tumi kene aasa?", "bengali": "তুমি কেমন আছ?", "english": "How are you? (informal)"},
            {"assamese": "শুভ ৰাতিপুৱা",   "transliteration": "xubho raatipuwa","bengali": "শুভ সকাল",       "english": "Good morning"},
            {"assamese": "শুভ নিশা",        "transliteration": "xubho nisha",    "bengali": "শুভ রাত্রি",    "english": "Good night"},
        ],
        "grammar_note": "Assamese uses 'আপুনি' (apuni) for formal 'you' and 'তুমি' (tumi) for informal — just like Bengali আপনি/তুমি.",
        "fun_fact": "🦋 'নমস্কাৰ' is shared with Bengali but with a unique Assamese 'ৰ' pronunciation!",
    },
    3: {
        "title": "খাদ্য আৰু পানীয় | Food & Drinks",
        "title_en": "Food & Drinks",
        "description": "Essential vocabulary for food, eating and dining",
        "vocabulary": [
            {"assamese": "ভাত",   "transliteration": "bhat",   "bengali": "ভাত",  "english": "rice (cooked)"},
            {"assamese": "মাছ",   "transliteration": "maas",   "bengali": "মাছ",  "english": "fish"},
            {"assamese": "মাংস",  "transliteration": "maangx", "bengali": "মাংস", "english": "meat"},
            {"assamese": "পাচলি", "transliteration": "paasoli","bengali": "সবজি", "english": "vegetables"},
            {"assamese": "পানী",  "transliteration": "paani",  "bengali": "জল",   "english": "water"},
            {"assamese": "চাহ",   "transliteration": "xah",    "bengali": "চা",   "english": "tea"},
            {"assamese": "আম",    "transliteration": "aam",    "bengali": "আম",   "english": "mango"},
            {"assamese": "কল",    "transliteration": "kol",    "bengali": "কলা",  "english": "banana"},
            {"assamese": "লেতেকু","transliteration": "leteku", "bengali": "সবেদা","english": "sapodilla fruit"},
        ],
        "phrases": [
            {"assamese": "মই ভোক লাগিছে",    "transliteration": "moi bhok laagise",  "bengali": "আমার খিদে লেগেছে","english": "I am hungry"},
            {"assamese": "এইটো বৰ সুস্বাদু", "transliteration": "eitoo bor suxwadu", "bengali": "এটা খুব সুস্বাদু","english": "This is very delicious"},
            {"assamese": "আৰু অলপ দিব নে?",  "transliteration": "aaroo olop dib ne?","bengali": "আরও একটু দেবেন?", "english": "Can you give a little more?"},
        ],
        "grammar_note": "Notice 'চাহ' (xah) for tea. The 'x' in Assamese makes a 'sh' sound — unique from Bengali.",
        "fun_fact": "🍵 Assam produces over 50% of India's tea! The word চাহ is central to Assamese identity.",
    },
    4: {
        "title": "সংখ্যা আৰু সময় | Numbers & Time",
        "title_en": "Numbers & Time",
        "description": "Count in Assamese and tell the time",
        "vocabulary": [
            {"assamese": "এক",  "transliteration": "ek",   "bengali": "এক",  "english": "one (1)"},
            {"assamese": "দুই", "transliteration": "dui",  "bengali": "দুই", "english": "two (2)"},
            {"assamese": "তিনি","transliteration": "tini", "bengali": "তিন", "english": "three (3)"},
            {"assamese": "চাৰি","transliteration": "saari","bengali": "চার", "english": "four (4)"},
            {"assamese": "পাঁচ","transliteration": "paas", "bengali": "পাঁচ","english": "five (5)"},
            {"assamese": "ছয়", "transliteration": "xoi",  "bengali": "ছয়", "english": "six (6)"},
            {"assamese": "সাত", "transliteration": "xaat", "bengali": "সাত", "english": "seven (7)"},
            {"assamese": "আঠ",  "transliteration": "aath", "bengali": "আট",  "english": "eight (8)"},
            {"assamese": "ন",   "transliteration": "no",   "bengali": "নয়", "english": "nine (9)"},
            {"assamese": "দহ",  "transliteration": "doh",  "bengali": "দশ",  "english": "ten (10)"},
        ],
        "phrases": [
            {"assamese": "এতিয়া কিমান বাজিছে?","transliteration": "etiya kiman baajise?","bengali": "এখন কটা বাজে?","english": "What time is it?"},
            {"assamese": "আজি কি বাৰ?",         "transliteration": "aaji ki bar?",        "bengali": "আজ কি বার?",   "english": "What day is today?"},
            {"assamese": "কাইলৈ দেখা হব",       "transliteration": "kailoi dekha hob",    "bengali": "কাল দেখা হবে", "english": "See you tomorrow"},
        ],
        "grammar_note": "Assamese numbers are similar to Bengali but with unique sounds. 'সাত' is pronounced 'xaat' not 'saat'.",
        "fun_fact": "📅 The Assamese new year 'বহাগ' (Bohag) is celebrated in April with the Bihu festival!",
    },
    5: {
        "title": "ৰং আৰু প্ৰকৃতি | Colors & Nature",
        "title_en": "Colors & Nature",
        "description": "Describe the world around you in Assamese",
        "vocabulary": [
            {"assamese": "ৰঙা",     "transliteration": "ronga",  "bengali": "লাল",   "english": "red"},
            {"assamese": "নীলা",    "transliteration": "nila",   "bengali": "নীল",   "english": "blue"},
            {"assamese": "হালধীয়া","transliteration": "haldiya","bengali": "হলুদ",  "english": "yellow"},
            {"assamese": "সেউজীয়া","transliteration": "seujia", "bengali": "সবুজ",  "english": "green"},
            {"assamese": "বগা",     "transliteration": "boga",   "bengali": "সাদা",  "english": "white"},
            {"assamese": "কলা",     "transliteration": "kola",   "bengali": "কালো",  "english": "black"},
            {"assamese": "নদী",     "transliteration": "nodi",   "bengali": "নদী",   "english": "river"},
            {"assamese": "পাহাৰ",   "transliteration": "pahar",  "bengali": "পাহাড়","english": "hill/mountain"},
            {"assamese": "হাতী",    "transliteration": "haati",  "bengali": "হাতি",  "english": "elephant"},
        ],
        "phrases": [
            {"assamese": "অসম বৰ সুন্দৰ",               "transliteration": "oxom bor xundor",             "bengali": "আসাম খুব সুন্দর",        "english": "Assam is very beautiful"},
            {"assamese": "ব্ৰহ্মপুত্ৰ এখন ডাঙৰ নদী",  "transliteration": "brahmoputro ekhan daangor nodi","bengali": "ব্রহ্মপুত্র একটা বড় নদী","english": "Brahmaputra is a big river"},
        ],
        "grammar_note": "Colors in Assamese often end in '-া': ৰঙা (red), নীলা (blue), হালধীয়া (yellow).",
        "fun_fact": "🦏 Kaziranga National Park in Assam is a UNESCO World Heritage Site with the world's most one-horned rhinos!",
    },
    6: {
        "title": "দৈনন্দিন কাৰ্যকলাপ | Daily Activities",
        "title_en": "Daily Activities",
        "description": "Talk about everyday routines in Assamese",
        "vocabulary": [
            {"assamese": "উঠা",     "transliteration": "utha",    "bengali": "ওঠা",     "english": "to wake up"},
            {"assamese": "খোৱা",    "transliteration": "khowa",   "bengali": "খাওয়া",  "english": "to eat"},
            {"assamese": "পঢ়া",    "transliteration": "pora",    "bengali": "পড়া",     "english": "to read/study"},
            {"assamese": "লিখা",    "transliteration": "likha",   "bengali": "লেখা",    "english": "to write"},
            {"assamese": "খেলা",    "transliteration": "khela",   "bengali": "খেলা",    "english": "to play"},
            {"assamese": "শোৱা",    "transliteration": "xowa",    "bengali": "ঘুমানো",  "english": "to sleep"},
            {"assamese": "যোৱা",    "transliteration": "jowa",    "bengali": "যাওয়া",  "english": "to go"},
            {"assamese": "অহা",     "transliteration": "oha",     "bengali": "আসা",     "english": "to come"},
            {"assamese": "কাম কৰা", "transliteration": "kaam kora","bengali": "কাজ করা","english": "to work"},
            {"assamese": "গোৱা",    "transliteration": "guwa",    "bengali": "গাওয়া",  "english": "to sing"},
        ],
        "phrases": [
            {"assamese": "মই ৰাতিপুৱা সোনকালে উঠো","transliteration": "moi raatipuwa xonkale utho","bengali": "আমি সকালে তাড়াতাড়ি উঠি","english": "I wake up early in the morning"},
            {"assamese": "মই প্ৰতিদিন পঢ়ো",        "transliteration": "moi protidin poro",         "bengali": "আমি প্রতিদিন পড়ি",        "english": "I study every day"},
        ],
        "grammar_note": "Assamese verbs in infinitive form end in '-া'. Present tense: মই (I) + verb root + 'ও' → মই পঢ়ো (I read).",
        "fun_fact": "🎭 Assam has a rich tradition of 'Bhaona' — traditional theatre combining dance, music and drama!",
    },
    7: {
        "title": "সাপ্তাহিক পুনৰীক্ষণ | Weekly Review",
        "title_en": "Weekly Review",
        "description": "Review all lessons then take the Weekly Test!",
        "vocabulary": [],
        "phrases": [],
        "grammar_note": "Great job completing your first week! Review all previous lessons before the weekly test.",
        "fun_fact": "🏆 Week 1 complete! The Assamese script evolved from the ancient Kamrupi script, closely related to Bengali.",
    },
}

QUIZ_QUESTIONS = [
    {"q": "What does 'নমস্কাৰ' mean?",             "opts": ["Goodbye","Hello/Greetings","Thank you","Sorry"],          "ans": 1, "exp": "নমস্কাৰ (nomoskar) is the standard Assamese greeting."},
    {"q": "How do you say 'mother' in Assamese?",   "opts": ["দেউতা","ককাই","মা","আইতা"],                              "ans": 2, "exp": "মা (maa) means mother — same as Bengali!"},
    {"q": "Which means 'water' in Assamese?",        "opts": ["চাহ","পানী","ভাত","মাছ"],                                "ans": 1, "exp": "পানী (paani) = water. Bengali uses জল or পানি."},
    {"q": "What is 'five' in Assamese?",             "opts": ["এক","তিনি","পাঁচ","দহ"],                                "ans": 2, "exp": "পাঁচ (paas) = five."},
    {"q": "How do you say 'Yes' in Assamese?",       "opts": ["নহয়","হয়","মাফ","ধন্যবাদ"],                             "ans": 1, "exp": "হয় (hoy) = Yes; নহয় (nohoy) = No."},
    {"q": "What does 'দেউতা' mean?",                "opts": ["Mother","Brother","Father","Grandfather"],                "ans": 2, "exp": "দেউতা (deuta) = father. Unlike Bengali বাবা, Assamese uses দেউতা."},
    {"q": "Which word is unique to Assamese?",       "opts": ["মাছ","ভাত","লেতেকু","আম"],                               "ans": 2, "exp": "লেতেকু (leteku) is the sapodilla — unique Assamese vocabulary!"},
    {"q": "How do you say 'I am fine'?",             "opts": ["মই ভোক লাগিছে","ভালেই আছো","মাফ কৰিব","পুনৰ লগ পাম"], "ans": 1, "exp": "ভালেই আছো (bhalei aaso) = I am fine."},
    {"q": "The Assamese letter 'ৰ' is unique because:","opts": ["Not found in Bengali","Sounds like z","Is silent","Replaces ক"],"ans": 0,"exp": "ৰ (ro) is a unique Assamese letter not in standard Bengali!"},
    {"q": "'আপুনি কেনে আছে?' means:",               "opts": ["Goodbye","How are you? (formal)","Good morning","Sorry"], "ans": 1, "exp": "আপুনি (apuni) is the formal 'you' — like Bengali আপনি."},
]

CULTURAL_FACTS = [
    {"fact": "Bihu is celebrated three times a year and is Assam's most important festival!", "emoji": "🎊"},
    {"fact": "Assam produces over 50% of India's tea and is world-famous for Assam Tea!", "emoji": "🍵"},
    {"fact": "Kaziranga National Park is a UNESCO World Heritage Site!", "emoji": "🏞️"},
    {"fact": "The one-horned rhinoceros is the state animal of Assam!", "emoji": "🦏"},
    {"fact": "Majuli in Assam is the world's largest river island!", "emoji": "🏝️"},
    {"fact": "The Kamakhya Temple in Guwahati is one of India's most sacred Shakti temples!", "emoji": "🛕"},
    {"fact": "Assamese Muga silk is unique to Assam and internationally renowned!", "emoji": "🪡"},
    {"fact": "Assam has the largest number of wild elephants in India!", "emoji": "🐘"},
    {"fact": "The Brahmaputra is one of Asia's mightiest rivers, flowing through Assam!", "emoji": "🌊"},
    {"fact": "Guwahati is the gateway city to all of Northeast India!", "emoji": "🌆"},
]

MOTIVATIONAL = [
    "তুমি বৰ ভালদৰে কৰিছা! (You are doing very well!)",
    "লাহে লাহে অভ্যাস কৰক! (Practice slowly, steadily!)",
    "প্ৰতিদিন শিকক! (Learn every day!)",
    "চেষ্টা কৰক, সফল হওক! (Try and succeed!)",
    "অসমীয়া শিক্ষা তোমাৰ বাবে! (Assamese learning is for you!)",
]

GRAMMAR_PRONOUNS = [
    {"assamese": "মই",        "transliteration": "moi",     "bengali": "আমি",   "english": "I"},
    {"assamese": "মোৰ",       "transliteration": "mor",     "bengali": "আমার",  "english": "my"},
    {"assamese": "মোক",       "transliteration": "mok",     "bengali": "আমাকে", "english": "me"},
    {"assamese": "তুমি",      "transliteration": "tumi",    "bengali": "তুমি",  "english": "you (informal)"},
    {"assamese": "আপুনি",     "transliteration": "apuni",   "bengali": "আপনি",  "english": "you (formal)"},
    {"assamese": "সি / তেওঁ", "transliteration": "xi/tewo", "bengali": "সে/তিনি","english": "he/she"},
    {"assamese": "আমি",       "transliteration": "aami",    "bengali": "আমরা",  "english": "we"},
    {"assamese": "তোমালোক",   "transliteration": "tomalok", "bengali": "তোমরা", "english": "you (plural)"},
    {"assamese": "তেওঁলোক",  "transliteration": "tewolok", "bengali": "তারা",  "english": "they"},
]

FILL_EX = [
    {"s": "মোৰ ___ মা।",                 "b": "মা",      "h": "family member", "e": "My ___ is mother."},
    {"s": "আপোনাক ___।",                 "b": "ধন্যবাদ", "h": "gratitude",     "e": "Thank ___ to you."},
    {"s": "মই ভাত ___।",                 "b": "খাওঁ",    "h": "I eat...",      "e": "I ___ rice."},
    {"s": "ব্ৰহ্মপুত্ৰ এখন ___ নদী।",  "b": "ডাঙৰ",    "h": "size (big)",    "e": "Brahmaputra is a ___ river."},
    {"s": "অসম বৰ ___।",                 "b": "সুন্দৰ",  "h": "appearance",   "e": "Assam is very ___."},
]

# ══════════════════════════════════════════════════════════════════════════════
#  SESSION STATE & HELPERS
# ══════════════════════════════════════════════════════════════════════════════

def init_state():
    defaults = {
        "registered": False, "user_name": "", "native_language": "Bengali",
        "current_day": 1, "completed_lessons": [], "streak": 0,
        "last_login": "", "total_xp": 0, "badges": [],
        "weekly_test_scores": [], "page": "home",
        "fc_idx": 0, "fc_flipped": False, "fill_idx": 0,
        "wt_started": False, "wt_questions": [],
        "wt_answers": {}, "wt_submitted": False,
        "mw": None, "ma": {},
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

def update_streak():
    today = str(date.today())
    last  = st.session_state.last_login
    if last == today:
        return
    yesterday = str(date.today() - timedelta(days=1))
    st.session_state.streak    = (st.session_state.streak + 1) if last == yesterday else 1
    st.session_state.last_login = today

def add_xp(pts):
    st.session_state.total_xp += pts
    _check_badges()

def _check_badges():
    b  = st.session_state.badges
    xp = st.session_state.total_xp
    s  = st.session_state.streak
    d  = len(st.session_state.completed_lessons)
    for bid, cond, name, desc in [
        ("first_lesson",  d >= 1,    "📚 First Steps",     "Completed first lesson!"),
        ("five_lessons",  d >= 5,    "🏅 Dedicated",       "Completed 5 lessons!"),
        ("first_century", xp >= 100, "🌟 Century Learner", "Earned 100 XP!"),
        ("streak_3",      s >= 3,    "🔥 On Fire!",        "3-day streak!"),
        ("streak_7",      s >= 7,    "⚡ Week Warrior",    "7-day streak!"),
        ("scholar",       xp >= 500, "🎓 Scholar",         "Earned 500 XP!"),
    ]:
        if cond and bid not in b:
            b.append(bid)
            st.toast(f"🏆 Badge: {name} — {desc}")

def get_level(xp):
    for lvl, ass, en, nxt in [
        (1,"নতুন শিক্ষাৰ্থী","Beginner",100),
        (2,"উদীয়মান","Rising Learner",300),
        (3,"মধ্যবৰ্তী","Intermediate",600),
        (4,"দক্ষ শিক্ষাৰ্থী","Skilled",1000),
        (5,"অসমীয়া বিশেষজ্ঞ","Expert",9999),
    ]:
        if xp < nxt:
            return lvl, ass, en, nxt
    return 5, "অসমীয়া বিশেষজ্ঞ", "Expert", 9999

def speak(text):
    try:
        from gtts import gTTS
        tts = gTTS(text=text, lang="hi", slow=False)
        buf = io.BytesIO()
        tts.write_to_fp(buf)
        buf.seek(0)
        st.audio(buf, format="audio/mp3")
    except Exception:
        st.info(f"🔊 {text}")

def goto(page):
    st.session_state.page = page
    st.rerun()

# ══════════════════════════════════════════════════════════════════════════════
#  CSS
# ══════════════════════════════════════════════════════════════════════════════

def inject_css():
    st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@400;600;700&family=Nunito:wght@400;600;700;800;900&family=Space+Grotesk:wght@400;500;600;700&display=swap');
:root{
  --p:#FF6B35;--pd:rgba(255,107,53,.15);--s:#2EC4B6;--w:#FFD166;--d:#EF233C;
  --bg:#0F0E17;--c1:#1A1A2E;--c2:#16213E;--tx:#FFFFFE;--mt:#a7a9be;
  --gr:linear-gradient(135deg,#FF6B35,#F7C59F);
}
.stApp{background:var(--bg)!important;font-family:'Nunito',sans-serif;color:var(--tx)!important;}
h1,h2,h3,h4{color:var(--tx)!important;}
p,li,label,span{color:var(--tx);}
.main .block-container{padding-top:1rem;max-width:1100px;}
#MainMenu,footer,header{visibility:hidden;}
::-webkit-scrollbar{width:5px;}
::-webkit-scrollbar-thumb{background:var(--p);border-radius:3px;}
section[data-testid="stSidebar"]{background:var(--c1)!important;border-right:1px solid rgba(255,107,53,.2);}
section[data-testid="stSidebar"] *{color:var(--tx)!important;}
.stButton>button{background:var(--gr)!important;color:#fff!important;border:none!important;border-radius:12px!important;font-weight:700!important;transition:all .2s!important;}
.stButton>button:hover{transform:translateY(-2px)!important;box-shadow:0 6px 20px rgba(255,107,53,.4)!important;}
.stTabs [data-baseweb="tab-list"]{background:var(--c1)!important;border-radius:12px!important;padding:4px!important;}
.stTabs [data-baseweb="tab"]{color:var(--mt)!important;border-radius:8px!important;}
.stTabs [aria-selected="true"]{background:var(--p)!important;color:#fff!important;}
.vc{background:var(--c1);border:1px solid rgba(255,107,53,.25);border-radius:16px;padding:16px 20px;margin:8px 0;position:relative;overflow:hidden;transition:all .3s;}
.vc::before{content:'';position:absolute;top:0;left:0;width:4px;height:100%;background:var(--gr);}
.vc:hover{border-color:var(--p);transform:translateY(-2px);box-shadow:0 8px 28px rgba(255,107,53,.18);}
.lc{background:var(--c1);border:1px solid rgba(255,107,53,.2);border-radius:18px;padding:22px;margin:10px 0;transition:all .3s;}
.lc:hover{border-color:var(--p);}
.mc{background:var(--c1);border:1px solid rgba(255,107,53,.2);border-radius:16px;padding:16px;text-align:center;}
.mv{font-size:2.4em;font-weight:900;color:var(--p);font-family:'Space Grotesk',sans-serif;line-height:1.1;}
.ml{color:var(--mt);font-size:.78em;text-transform:uppercase;letter-spacing:1px;margin-top:4px;}
.hero{background:linear-gradient(135deg,rgba(255,107,53,.12),rgba(26,26,46,.95));border:1px solid rgba(255,107,53,.3);border-radius:22px;padding:36px;text-align:center;margin-bottom:24px;}
.at{font-family:'Hind Siliguri','Nunito',serif;font-size:2em;color:var(--p);font-weight:700;line-height:1.3;}
.tr{font-family:'Space Grotesk',monospace;color:#F7C59F;font-size:.9em;font-style:italic;}
.bn{color:var(--s);font-size:1.1em;}
.en{color:var(--mt);font-size:.9em;}
.ib{background:rgba(46,196,182,.1);border:1px solid rgba(46,196,182,.3);border-radius:12px;padding:14px;margin:8px 0;}
.wb{background:rgba(255,209,102,.1);border:1px solid rgba(255,209,102,.3);border-radius:12px;padding:14px;margin:8px 0;font-style:italic;}
.pw{background:rgba(255,255,255,.08);border-radius:20px;height:10px;margin:6px 0;overflow:hidden;}
.pf{height:100%;border-radius:20px;background:var(--gr);transition:width .5s ease;}
.ac{background:var(--c1);border:1px solid rgba(255,107,53,.2);border-radius:10px;padding:12px 8px;text-align:center;transition:all .2s;}
.ac:hover{border-color:var(--p);background:var(--pd);}
.stSelectbox>div>div{background:var(--c1)!important;color:var(--tx)!important;}
.stTextInput>div>div>input{background:var(--c1)!important;color:var(--tx)!important;}
</style>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  SIDEBAR
# ══════════════════════════════════════════════════════════════════════════════

def sidebar():
    with st.sidebar:
        st.markdown("""<div style='text-align:center;padding:14px 0 6px'>
          <div style='font-size:2.6em'>🦚</div>
          <div style='font-size:1.35em;font-weight:900;color:#FF6B35'>অসমীয়া শিক্ষা</div>
          <div style='font-size:.72em;color:#a7a9be;letter-spacing:1.5px'>LEARN ASSAMESE</div>
        </div>""", unsafe_allow_html=True)
        st.markdown("---")

        if st.session_state.registered:
            xp  = st.session_state.total_xp
            lvl, ass, en, nxt = get_level(xp)
            pct = min(int(xp / nxt * 100), 100)
            st.markdown(f"<div style='font-weight:800'>👤 {st.session_state.user_name}</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='color:#a7a9be;font-size:.82em'>Lv.{lvl} · {en}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='pw'><div class='pf' style='width:{pct}%'></div></div>", unsafe_allow_html=True)
            st.markdown(f"<div style='font-size:.72em;color:#a7a9be'>{xp}/{nxt} XP</div>", unsafe_allow_html=True)
            s = st.session_state.streak
            st.markdown(f"<div style='margin:10px 0;background:#16213E;border-radius:10px;padding:8px;text-align:center'>{'🔥' if s else '💤'} <b style='color:#FF6B35'>{s}</b> <span style='color:#a7a9be;font-size:.8em'>day streak</span></div>", unsafe_allow_html=True)
            st.markdown("---")

        for icon, label, key in [
            ("🏠","Home","home"),("📅","Daily Lessons","lessons"),
            ("🔤","Alphabet","alphabet"),("🗣️","Voice Practice","voice"),
            ("✏️","Practice","practice"),("📝","Weekly Test","weekly_test"),
            ("📊","Progress","progress"),("ℹ️","About Assam","culture"),
        ]:
            if st.button(f"{icon} {label}", key=f"nav_{key}", use_container_width=True):
                goto(key)

        st.markdown("---")
        st.markdown("<div style='text-align:center;font-size:.72em;color:#a7a9be'>Made with ❤️ for Assamese learners<br><span style='color:#FF6B35'>অসম · Assam</span></div>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  PAGES
# ══════════════════════════════════════════════════════════════════════════════

def page_home():
    if not st.session_state.registered:
        st.markdown("""<div class='hero'>
          <div style='font-size:3.2em'>🦚</div>
          <h1 style='font-size:2.4em;margin:8px 0'>অসমীয়া শিকক!</h1>
          <p style='color:#a7a9be;font-size:1.05em;max-width:500px;margin:auto'>
            Learn Assamese from Bengali &amp; English — daily lessons, voice practice,
            exercises and weekly tests.
          </p></div>""", unsafe_allow_html=True)
        _, mid, _ = st.columns([1,2,1])
        with mid:
            st.markdown("### 👋 Let's get started!")
            name = st.text_input("Your name", placeholder="Enter your name...")
            lang = st.selectbox("Your native language", ["Bengali","English","Both"])
            if st.button("🚀 Start Learning Assamese!", use_container_width=True):
                if name.strip():
                    st.session_state.registered = True
                    st.session_state.user_name  = name.strip()
                    st.session_state.native_language = lang
                    add_xp(10)
                    st.success("Welcome! আপোনাকে স্বাগতম! 🎉")
                    st.rerun()
                else:
                    st.warning("Please enter your name.")
        st.markdown("---")
        st.markdown("### ✨ What you'll get")
        for col, ico, ttl, dsc in zip(st.columns(4),
            ["📅","🗣️","✏️","📝"],
            ["Daily Lessons","Voice Practice","Exercises","Weekly Tests"],
            ["7 themed lessons with vocab & phrases","Hear Assamese pronunciation live",
             "Flashcards, matching & fill-in-blank","Quiz yourself & track progress"]):
            col.markdown(f"<div class='mc'><div style='font-size:1.8em'>{ico}</div><div style='font-weight:800;margin:5px 0'>{ttl}</div><div style='color:#a7a9be;font-size:.82em'>{dsc}</div></div>", unsafe_allow_html=True)
        return

    st.markdown(f"<div class='hero'><h1>নমস্কাৰ, {st.session_state.user_name}! 🦚</h1><p style='color:#a7a9be'>{random.choice(MOTIVATIONAL)}</p></div>", unsafe_allow_html=True)
    xp = st.session_state.total_xp
    for col, val, lbl in zip(st.columns(4),
        [f"🔥 {st.session_state.streak}", f"⭐ {xp}",
         f"📚 {len(st.session_state.completed_lessons)}", f"🏅 {len(st.session_state.badges)}"],
        ["Day Streak","Total XP","Lessons Done","Badges"]):
        col.markdown(f"<div class='mc'><div class='mv'>{val}</div><div class='ml'>{lbl}</div></div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    day = st.session_state.current_day
    les = DAILY_LESSONS.get(day, DAILY_LESSONS[1])
    fact = random.choice(CULTURAL_FACTS)
    ca, cb = st.columns([2,1])
    with ca:
        st.markdown(f"""<div class='lc'>
          <div style='color:#a7a9be;font-size:.78em'>TODAY · DAY {day}</div>
          <h3 style='margin:6px 0'>{les['title']}</h3>
          <p style='color:#a7a9be;margin:0'>{les['description']}</p>
          <div class='wb' style='margin-top:10px'>{fact['emoji']} <b>Did you know?</b> {fact['fact']}</div>
        </div>""", unsafe_allow_html=True)
        if st.button("▶️ Start Today's Lesson", use_container_width=True):
            goto("lessons")
    with cb:
        st.markdown("#### 📆 Weekly Plan")
        for d in range(1,8):
            done = d in st.session_state.completed_lessons
            mark = "✅" if done else ("▶️" if d==day else "🔒")
            clr  = "#FF6B35" if d==day else ("#2EC4B6" if done else "#a7a9be")
            st.markdown(f"<div style='color:{clr};font-size:.88em;padding:2px 0'>{mark} Day {d}: {DAILY_LESSONS[d]['title_en']}</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🃏 Today's Quick Vocab")
    words = les.get("vocabulary",[])[:4]
    if words:
        for col, w in zip(st.columns(len(words)), words):
            col.markdown(f"<div class='vc'><div class='at'>{w['assamese']}</div><div class='tr'>/{w['transliteration']}/</div><div class='bn'>{w['bengali']}</div><div class='en'>{w['english']}</div></div>", unsafe_allow_html=True)


def page_lessons():
    st.markdown("## 📅 Daily Lessons")
    day  = st.session_state.current_day
    sel  = st.selectbox("Choose lesson:", [f"Day {d}: {DAILY_LESSONS[d]['title_en']}" for d in range(1,8)], index=day-1)
    cd   = int(sel.split(":")[0].replace("Day","").strip())
    les  = DAILY_LESSONS[cd]
    done = cd in st.session_state.completed_lessons

    st.markdown(f"""<div class='lc'>
      <div style='display:flex;justify-content:space-between;align-items:center'>
        <div>
          <div style='color:#a7a9be;font-size:.78em'>DAY {cd} · {'✅ Completed' if done else '📖 In Progress'}</div>
          <h2 style='margin:5px 0'>{les['title']}</h2>
          <p style='color:#a7a9be;margin:0'>{les['description']}</p>
        </div>
        <div style='font-size:2.8em'>{'✅' if done else '📖'}</div>
      </div></div>""", unsafe_allow_html=True)

    t1,t2,t3,t4 = st.tabs(["📖 Vocabulary","💬 Phrases","📐 Grammar","🎯 Fun Fact"])
    with t1:
        if not les["vocabulary"]:
            st.info("Review day — revisit all previous lessons then take the Weekly Test!")
        else:
            show_t = st.checkbox("Show transliteration", value=True)
            for w in les["vocabulary"]:
                ca, cb = st.columns([4,1])
                with ca:
                    h = f"<div class='vc'><div class='at'>{w['assamese']}</div>"
                    if show_t: h += f"<div class='tr'>/{w['transliteration']}/</div>"
                    h += f"<div class='bn'>{w['bengali']}</div><div class='en'>{w['english']}</div></div>"
                    st.markdown(h, unsafe_allow_html=True)
                with cb:
                    st.markdown("<br><br>", unsafe_allow_html=True)
                    if st.button("🔊", key=f"ls_{w['assamese']}_{cd}"):
                        speak(w['assamese'])
    with t2:
        for i,p in enumerate(les.get("phrases",[])):
            st.markdown(f"<div class='vc'><div class='at' style='font-size:1.4em'>{p['assamese']}</div><div class='tr'>/{p['transliteration']}/</div><div class='bn'>{p['bengali']}</div><div class='en'>{p['english']}</div></div>", unsafe_allow_html=True)
            if st.button("🔊 Listen", key=f"lp_{i}_{cd}"):
                speak(p['assamese'])
    with t3:
        st.markdown(f"<div class='ib'>💡 <b>Grammar Note:</b> {les['grammar_note']}</div>", unsafe_allow_html=True)
        st.markdown("---")
        st.markdown("#### Pronouns Reference")
        for col,h in zip(st.columns(4),["Assamese","Transliteration","Bengali","English"]):
            col.markdown(f"**{h}**")
        for row in GRAMMAR_PRONOUNS:
            c1,c2,c3,c4 = st.columns(4)
            c1.markdown(f"<span class='at' style='font-size:1.1em'>{row['assamese']}</span>", unsafe_allow_html=True)
            c2.markdown(f"<span class='tr'>{row['transliteration']}</span>", unsafe_allow_html=True)
            c3.markdown(f"<span class='bn'>{row['bengali']}</span>", unsafe_allow_html=True)
            c4.markdown(row["english"])
    with t4:
        st.markdown(f"<div class='wb' style='font-size:1.05em;padding:20px'>🌟 <b>Fun Fact!</b><br><br>{les['fun_fact']}</div>", unsafe_allow_html=True)
        fc = random.choice(CULTURAL_FACTS)
        st.markdown(f"<div class='ib' style='margin-top:10px'>{fc['emoji']} {fc['fact']}</div>", unsafe_allow_html=True)

    st.markdown("---")
    ca,cb = st.columns(2)
    with ca:
        if not done:
            if st.button("✅ Mark Complete (+20 XP)", use_container_width=True):
                st.session_state.completed_lessons.append(cd)
                add_xp(20)
                if cd == st.session_state.current_day and cd < 7:
                    st.session_state.current_day += 1
                st.success("🎉 Lesson complete! +20 XP!"); st.rerun()
        else:
            st.success("✅ Already completed!")
    with cb:
        if st.button("✏️ Go to Practice", use_container_width=True):
            goto("practice")


def page_alphabet():
    st.markdown("## 🔤 Assamese Alphabet")
    st.markdown("<p style='color:#a7a9be'>Assamese script is closely related to Bengali but has unique characters like ৰ and ৱ.</p>", unsafe_allow_html=True)

    def alpha_grid(items, pfx):
        cols = st.columns(5)
        for i,it in enumerate(items):
            with cols[i%5]:
                st.markdown(f"<div class='ac'><div class='at' style='font-size:2em'>{it['assamese']}</div><div class='tr'>{it['transliteration']}</div><div class='bn' style='font-size:.9em'>{it.get('bengali','')}</div><div class='en'>{it['english']}</div></div>", unsafe_allow_html=True)
                if st.button("🔊", key=f"{pfx}_{i}"):
                    speak(it['assamese'])

    tv, tc = st.tabs(["🅰️ Vowels","🔡 Consonants"])
    with tv:
        st.markdown("<div class='ib'>Assamese has 11 vowels — similar to Bengali with subtle differences.</div>", unsafe_allow_html=True)
        alpha_grid(ASSAMESE_VOWELS, "v")
    with tc:
        st.markdown("<div class='ib'>🌟 <b>Unique to Assamese:</b> ৰ (rolled r), ৱ (w sound). শ/ষ/স are all pronounced 'x' (sh).</div>", unsafe_allow_html=True)
        alpha_grid(ASSAMESE_CONSONANTS, "c")


def page_voice():
    st.markdown("## 🗣️ Voice Practice")
    st.markdown("<p style='color:#a7a9be'>Listen to Assamese words and phrases. Repeat after the audio to build pronunciation.</p>", unsafe_allow_html=True)
    tw, tp, ta = st.tabs(["🔤 Words","💬 Phrases","🔡 Alphabet"])

    with tw:
        day   = st.session_state.current_day
        words = DAILY_LESSONS.get(day, DAILY_LESSONS[1]).get("vocabulary",[]) or DAILY_LESSONS[1]["vocabulary"]
        sel   = st.selectbox("Pick a word:", [f"{w['assamese']} — {w['english']}" for w in words])
        idx   = next((i for i,w in enumerate(words) if f"{w['assamese']} — {w['english']}"==sel), 0)
        w     = words[idx]
        st.markdown(f"<div class='vc' style='text-align:center;padding:30px'><div class='at' style='font-size:3em'>{w['assamese']}</div><div class='tr' style='font-size:1.1em'>/{w['transliteration']}/</div><div class='bn' style='margin-top:6px'>{w['bengali']}</div><div class='en'>{w['english']}</div></div>", unsafe_allow_html=True)
        ca,cb = st.columns(2)
        with ca:
            if st.button("🔊 Normal Speed", use_container_width=True): speak(w['assamese'])
        with cb:
            if st.button("🐢 Slow Speed", use_container_width=True):
                try:
                    from gtts import gTTS
                    tts = gTTS(text=w['assamese'], lang="hi", slow=True)
                    buf = io.BytesIO(); tts.write_to_fp(buf); buf.seek(0)
                    st.audio(buf, format="audio/mp3")
                except Exception: speak(w['assamese'])
        st.markdown("<div class='ib' style='margin-top:12px'>🗣️ <b>Tip:</b> In Assamese 'x' sounds like 'sh' in English.</div>", unsafe_allow_html=True)

    with tp:
        all_p = [p for les in DAILY_LESSONS.values() for p in les.get("phrases",[])]
        sel_p = st.selectbox("Pick a phrase:", [p['english'] for p in all_p])
        phrase = next(p for p in all_p if p['english']==sel_p)
        st.markdown(f"<div class='vc' style='text-align:center;padding:24px'><div class='at' style='font-size:1.6em'>{phrase['assamese']}</div><div class='tr'>/{phrase['transliteration']}/</div><div class='bn'>{phrase['bengali']}</div><div class='en'>{phrase['english']}</div></div>", unsafe_allow_html=True)
        if st.button("🔊 Listen to Phrase", use_container_width=True): speak(phrase['assamese'])

    with ta:
        all_a = ASSAMESE_VOWELS + ASSAMESE_CONSONANTS
        cols  = st.columns(6)
        for i,ch in enumerate(all_a):
            with cols[i%6]:
                st.markdown(f"<div class='at' style='font-size:1.7em;text-align:center'>{ch['assamese']}</div>", unsafe_allow_html=True)
                if st.button("▶", key=f"av_{i}", use_container_width=True): speak(ch['assamese'])


def page_practice():
    st.markdown("## ✏️ Practice Exercises")
    tf, tm, tx = st.tabs(["🃏 Flashcards","🔗 Matching","✍️ Fill in the Blank"])

    with tf:
        day   = st.session_state.current_day
        words = DAILY_LESSONS.get(day, DAILY_LESSONS[1]).get("vocabulary",[]) or DAILY_LESSONS[1]["vocabulary"]
        idx   = st.session_state.fc_idx % len(words)
        w     = words[idx]
        if not st.session_state.fc_flipped:
            st.markdown(f"<div class='vc' style='text-align:center;padding:50px 20px;min-height:180px'><div class='at' style='font-size:3.2em'>{w['assamese']}</div><div class='tr' style='margin-top:8px'>/{w['transliteration']}/</div><div style='color:#a7a9be;margin-top:14px;font-size:.9em'>Click Flip to see meaning</div></div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='vc' style='text-align:center;padding:50px 20px;min-height:180px;border-color:#2EC4B6'><div class='bn' style='font-size:1.8em'>{w['bengali']}</div><div class='en' style='font-size:1.4em;margin-top:6px'>{w['english']}</div><div style='color:#a7a9be;margin-top:14px;font-size:.9em'>Assamese: <b style='color:#FF6B35'>{w['assamese']}</b></div></div>", unsafe_allow_html=True)
        c1,c2,c3 = st.columns(3)
        with c1:
            if st.button("🔄 Flip", use_container_width=True):
                st.session_state.fc_flipped = not st.session_state.fc_flipped; st.rerun()
        with c2:
            if st.button("⬅️ Prev", use_container_width=True):
                st.session_state.fc_idx = (idx-1)%len(words); st.session_state.fc_flipped=False; st.rerun()
        with c3:
            if st.button("➡️ Next", use_container_width=True):
                st.session_state.fc_idx = (idx+1)%len(words); st.session_state.fc_flipped=False; st.rerun()
        st.markdown(f"<div style='text-align:center;color:#a7a9be;margin-top:6px'>Card {idx+1} of {len(words)}</div>", unsafe_allow_html=True)
        if st.button("🔊 Hear word", use_container_width=True): speak(w["assamese"])

    with tm:
        st.markdown("#### 🔗 Match the Word — 5 XP per correct answer!")
        day   = st.session_state.current_day
        all_w = DAILY_LESSONS.get(day, DAILY_LESSONS[1]).get("vocabulary",[]) or DAILY_LESSONS[1]["vocabulary"]
        if st.session_state.mw is None:
            st.session_state.mw = random.sample(all_w, min(4,len(all_w)))
            st.session_state.ma = {}
        if st.button("🔀 New Round", key="new_match"):
            st.session_state.mw = random.sample(all_w, min(4,len(all_w))); st.session_state.ma={}; st.rerun()
        sample = st.session_state.mw
        all_en = [w["english"] for w in all_w]
        for i,w in enumerate(sample):
            wrong  = random.sample([e for e in all_en if e!=w["english"]], min(3,len(all_en)-1))
            opts   = wrong + [w["english"]]; random.shuffle(opts)
            chosen = st.selectbox(f"{w['assamese']} ({w['transliteration']}) — {w['bengali']}", ["— select —"]+opts, key=f"m_{i}_{w['assamese']}")
            st.session_state.ma[i] = (chosen, w["english"])
        if st.button("✅ Check Answers", use_container_width=True):
            score = 0
            for i,(chosen,correct) in st.session_state.ma.items():
                if chosen==correct: st.success(f"✅ {sample[i]['assamese']} = {correct}"); score+=1
                else: st.error(f"❌ {sample[i]['assamese']} — Correct: {correct}")
            add_xp(score*5); st.info(f"Score: {score}/{len(sample)} · +{score*5} XP")

    with tx:
        st.markdown("#### ✍️ Fill in the Blank — 10 XP per correct!")
        ex = FILL_EX[st.session_state.fill_idx % len(FILL_EX)]
        st.markdown(f"<div class='lc'><div class='at' style='font-size:1.5em'>{ex['s']}</div><div class='en'>{ex['e']}</div><div class='tr'>Hint: {ex['h']}</div></div>", unsafe_allow_html=True)
        ans = st.text_input("Your answer:", key=f"fi_{st.session_state.fill_idx}")
        ca,cb = st.columns(2)
        with ca:
            if st.button("✅ Submit", use_container_width=True):
                if ans.strip()==ex["b"]: st.success(f"🎉 Correct! Answer: {ex['b']}"); add_xp(10)
                else: st.error(f"❌ Correct answer: **{ex['b']}**")
        with cb:
            if st.button("➡️ Next Question", use_container_width=True):
                st.session_state.fill_idx=(st.session_state.fill_idx+1)%len(FILL_EX); st.rerun()


def page_weekly_test():
    st.markdown("## 📝 Weekly Test")
    st.markdown("<p style='color:#a7a9be'>10 questions — 5 XP per correct answer — max 50 XP!</p>", unsafe_allow_html=True)

    if not st.session_state.wt_started:
        ca,cb = st.columns([2,1])
        with ca:
            st.markdown("""<div class='lc'><h3>📝 Weekly Assessment</h3>
            <p style='color:#a7a9be'>Covers vocabulary, greetings, grammar and cultural knowledge from all 7 days.</p>
            <div class='ib'>⏱️ No time limit &nbsp;|&nbsp; 10 questions &nbsp;|&nbsp; Max 50 XP</div></div>""", unsafe_allow_html=True)
        with cb:
            past = st.session_state.weekly_test_scores
            if past:
                st.markdown("#### Past Scores")
                for i,sc in enumerate(past[-5:],1): st.markdown(f"Attempt {i}: **{sc}/10**")
        if st.button("🚀 Start Weekly Test", use_container_width=True):
            st.session_state.wt_questions = random.sample(QUIZ_QUESTIONS, min(10,len(QUIZ_QUESTIONS)))
            st.session_state.wt_answers   = {}
            st.session_state.wt_submitted = False
            st.session_state.wt_started   = True
            st.rerun()
        return

    qs = st.session_state.wt_questions
    if not st.session_state.wt_submitted:
        st.markdown(f"<div style='color:#a7a9be'>Answered: {len(st.session_state.wt_answers)}/{len(qs)}</div>", unsafe_allow_html=True)
        for qi,q in enumerate(qs):
            st.markdown(f"<div class='lc'><div style='color:#a7a9be;font-size:.78em'>Question {qi+1}</div><h4 style='margin:5px 0'>{q['q']}</h4></div>", unsafe_allow_html=True)
            ans = st.radio("", q["opts"], key=f"wt_{qi}", label_visibility="collapsed")
            st.session_state.wt_answers[qi] = ans
        ca,cb = st.columns(2)
        with ca:
            if st.button("✅ Submit Test", use_container_width=True):
                st.session_state.wt_submitted=True; st.rerun()
        with cb:
            if st.button("🔄 Restart", use_container_width=True):
                st.session_state.wt_started=False; st.rerun()
    else:
        score = sum(1 for qi,q in enumerate(qs) if st.session_state.wt_answers.get(qi,"")==q["opts"][q["ans"]])
        pct   = int(score/len(qs)*100)
        st.session_state.weekly_test_scores.append(score)
        add_xp(score*5)
        grade = "🌟 Excellent!" if pct>=80 else ("👍 Good job!" if pct>=60 else "📖 Keep practising!")
        clr   = "#2EC4B6" if pct>=80 else ("#FFD166" if pct>=60 else "#EF233C")
        st.markdown(f"<div class='hero'><h2>{grade}</h2><div style='font-size:3.2em;font-weight:900;color:{clr}'>{score}/{len(qs)}</div><div style='color:#a7a9be'>{pct}% correct · +{score*5} XP</div></div>", unsafe_allow_html=True)
        st.markdown("### 📋 Detailed Results")
        for qi,q in enumerate(qs):
            chosen  = st.session_state.wt_answers.get(qi,"")
            correct = q["opts"][q["ans"]]
            ok      = chosen==correct
            bg      = "rgba(46,196,182,.1)" if ok else "rgba(239,35,60,.1)"
            fb      = '<span style="color:#2EC4B6">Correct!</span>' if ok else f'<span style="color:#EF233C">Correct: {correct}</span>'
            st.markdown(f"<div style='background:{bg};border-radius:12px;padding:14px;margin:5px 0'><b>{'✅' if ok else '❌'} Q{qi+1}: {q['q']}</b><br><span style='color:#a7a9be'>Your answer: {chosen}</span><br>{fb}<br><span style='color:#FFD166;font-size:.85em'>{q['exp']}</span></div>", unsafe_allow_html=True)
        ca,cb = st.columns(2)
        with ca:
            if st.button("🔄 Retake Test", use_container_width=True):
                st.session_state.wt_started=False; st.rerun()
        with cb:
            if st.button("📅 Back to Lessons", use_container_width=True): goto("lessons")


def page_progress():
    st.markdown("## 📊 Your Progress")
    xp    = st.session_state.total_xp
    lvl, ass, en, nxt = get_level(xp)
    pct   = min(int(xp/nxt*100),100)
    done  = st.session_state.completed_lessons
    scores= st.session_state.weekly_test_scores
    badges= st.session_state.badges

    st.markdown(f"""<div class='hero'>
      <div style='font-size:.85em;color:#a7a9be;text-transform:uppercase;letter-spacing:1px'>Level {lvl}</div>
      <h2>{ass}</h2><div style='color:#a7a9be'>{en}</div>
      <div class='pw' style='max-width:380px;margin:14px auto 5px'><div class='pf' style='width:{pct}%'></div></div>
      <div style='color:#a7a9be;font-size:.82em'>{xp}/{nxt} XP to next level</div>
    </div>""", unsafe_allow_html=True)

    for col,val,lbl in zip(st.columns(4),
        [xp, st.session_state.streak, len(done), len(scores)],
        ["Total XP","Day Streak","Lessons Done","Tests Taken"]):
        col.markdown(f"<div class='mc'><div class='mv'>{val}</div><div class='ml'>{lbl}</div></div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    ca,cb = st.columns(2)
    with ca:
        st.markdown("#### 📅 Lesson Completion")
        vals   = [1 if d in done else 0 for d in range(1,8)]
        fig    = go.Figure(go.Bar(x=[f"D{d}" for d in range(1,8)], y=vals,
                           marker_color=["#2EC4B6" if v else "#1A1A2E" for v in vals],
                           text=["✅" if v else "🔒" for v in vals], textposition="outside"))
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                          font_color="#FFFFFE", yaxis=dict(showticklabels=False,showgrid=False),
                          xaxis=dict(showgrid=False), margin=dict(t=20,b=20), height=260, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    with cb:
        st.markdown("#### 📝 Weekly Test Scores")
        if scores:
            fig2 = go.Figure(go.Scatter(x=[f"T{i+1}" for i in range(len(scores))], y=scores,
                             mode="lines+markers", line=dict(color="#FF6B35",width=3),
                             marker=dict(size=10,color="#FF6B35"), fill="tozeroy",
                             fillcolor="rgba(255,107,53,0.1)"))
            fig2.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                               font_color="#FFFFFE", yaxis=dict(range=[0,10],gridcolor="rgba(255,255,255,0.1)"),
                               xaxis=dict(showgrid=False), margin=dict(t=20,b=20), height=260)
            st.plotly_chart(fig2, use_container_width=True)
        else:
            st.markdown("<div class='ib' style='text-align:center;padding:60px'><div style='font-size:2em'>📝</div><p>No scores yet — take your first test!</p></div>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### 🏅 Badges & Achievements")
    badge_meta = {
        "first_lesson": ("📚","First Steps","Complete first lesson"),
        "five_lessons": ("🏅","Dedicated","Complete 5 lessons"),
        "first_century":("🌟","Century Learner","Earn 100 XP"),
        "streak_3":     ("🔥","On Fire!","3-day streak"),
        "streak_7":     ("⚡","Week Warrior","7-day streak"),
        "scholar":      ("🎓","Scholar","Earn 500 XP"),
    }
    bc = st.columns(6)
    for i,(bid,(ico,name,desc)) in enumerate(badge_meta.items()):
        bc[i].markdown(f"<div class='mc' style='opacity:{'1' if bid in badges else '0.28'}'><div style='font-size:1.9em'>{ico}</div><div style='font-weight:700;font-size:.82em'>{name}</div><div style='color:#a7a9be;font-size:.7em'>{desc}</div></div>", unsafe_allow_html=True)


def page_culture():
    st.markdown("## ℹ️ About Assam & Assamese Culture")
    st.markdown("<div class='hero'><div style='font-size:3em'>🦚</div><h2>অসম — Land of Red River and Blue Hills</h2><p style='color:#a7a9be;max-width:580px;margin:auto'>Assam is a northeastern state of India known for its rich biodiversity, tea gardens, silk and vibrant cultural heritage.</p></div>", unsafe_allow_html=True)
    t1,t2,t3,t4 = st.tabs(["🌿 Facts","🎊 Festivals","🗣️ Assamese vs Bengali","🍵 Tea Culture"])

    with t1:
        for f in CULTURAL_FACTS:
            st.markdown(f"<div class='vc'><span style='font-size:1.4em'>{f['emoji']}</span> <span style='margin-left:8px'>{f['fact']}</span></div>", unsafe_allow_html=True)

    with t2:
        for n,ass,bn,m,d in [
            ("Bohag Bihu","বহাগ বিহু","বহাগ বিহু","April","Assamese New Year — dance, music and feasting"),
            ("Kati Bihu","কাতি বিহু","কাতি বিহু","October","Harvest festival with lamps and prayers"),
            ("Magh Bihu","মাঘ বিহু","মাঘ বিহু","January","Winter harvest with bonfires and traditional food"),
            ("Durga Puja","দুৰ্গা পূজা","দুর্গা পূজা","October","Celebrated with great enthusiasm across Assam"),
        ]:
            st.markdown(f"<div class='vc'><div style='display:flex;justify-content:space-between'><div><b style='color:#FF6B35'>{n}</b> <span class='at' style='font-size:.95em;margin-left:8px'>{ass}</span> <span class='bn' style='margin-left:6px'>({bn})</span></div><span style='color:#FFD166'>{m}</span></div><div style='color:#a7a9be;margin-top:5px'>{d}</div></div>", unsafe_allow_html=True)

    with t3:
        for col,h in zip(st.columns(3),["**Feature**","**Assamese 🦚**","**Bengali 🐯**"]):
            col.markdown(h)
        st.markdown("<hr style='margin:5px 0'>", unsafe_allow_html=True)
        for feat,ass,bn in [
            ("'I'","মই (moi)","আমি (ami)"),
            ("'We'","আমি (aami)","আমরা (amra)"),
            ("Unique letter","ৰ (rolled r)","র (standard)"),
            ("W sound","ৱ (wo)","Not present"),
            ("শ/ষ/স","All → x (sh)","Distinct sounds"),
            ("Father","দেউতা (deuta)","বাবা (baba)"),
            ("Elder brother","ককাই (kokai)","দাদা (dada)"),
            ("Tea","চাহ (xah)","চা (cha)"),
        ]:
            c1,c2,c3 = st.columns(3)
            c1.markdown(f"<span style='color:#a7a9be'>{feat}</span>", unsafe_allow_html=True)
            c2.markdown(f"<span style='color:#FF6B35'>{ass}</span>", unsafe_allow_html=True)
            c3.markdown(f"<span class='bn'>{bn}</span>", unsafe_allow_html=True)

    with t4:
        st.markdown("""<div class='wb' style='padding:20px;font-size:1.05em;font-style:normal'>
        <b>🍵 Assam Tea — চাহ (Xah)</b><br><br>
        Assam is the world's largest tea-growing region, prized globally for its bold, malty flavour.
        Offering চাহ to a guest is the highest form of Assamese hospitality.<br><br>
        <b>Tea vocabulary:</b> চাহ (xah) = tea &nbsp;|&nbsp; গাখীৰ (gaakhir) = milk &nbsp;|&nbsp;
        চেনি (xeni) = sugar &nbsp;|&nbsp; চাহৰ বাগান (xahor baagan) = tea garden
        </div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  MAIN ROUTER
# ══════════════════════════════════════════════════════════════════════════════

init_state()
update_streak()
inject_css()
sidebar()

{
    "home":        page_home,
    "lessons":     page_lessons,
    "alphabet":    page_alphabet,
    "voice":       page_voice,
    "practice":    page_practice,
    "weekly_test": page_weekly_test,
    "progress":    page_progress,
    "culture":     page_culture,
}.get(st.session_state.page, page_home)()
