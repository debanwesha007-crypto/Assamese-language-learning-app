"""
Assamese Language Learning Data
Contains vocabulary, phrases, grammar rules organized by difficulty level
"""

# ===================== ALPHABETS =====================
ASSAMESE_VOWELS = [
    {"assamese": "অ", "transliteration": "o", "bengali": "অ", "english": "a (as in about)", "example": "অসম (Assam)"},
    {"assamese": "আ", "transliteration": "aa", "bengali": "আ", "english": "aa (long a)", "example": "আম (mango)"},
    {"assamese": "ই", "transliteration": "i", "bengali": "ই", "english": "i (short)", "example": "ইলিচ (ilish fish)"},
    {"assamese": "ঈ", "transliteration": "ii", "bengali": "ঈ", "english": "ee (long i)", "example": "ঈশ্বৰ (God)"},
    {"assamese": "উ", "transliteration": "u", "bengali": "উ", "english": "u (short)", "example": "উট (camel)"},
    {"assamese": "ঊ", "transliteration": "uu", "bengali": "ঊ", "english": "oo (long u)", "example": "ঊষা (dawn)"},
    {"assamese": "ঋ", "transliteration": "ri", "bengali": "ঋ", "english": "ri", "example": "ঋতু (season)"},
    {"assamese": "এ", "transliteration": "e", "bengali": "এ", "english": "e (as in egg)", "example": "এখন (one)"},
    {"assamese": "ঐ", "transliteration": "oi", "bengali": "ঐ", "english": "oi", "example": "ঐতিহ্য (tradition)"},
    {"assamese": "ও", "transliteration": "o", "bengali": "ও", "english": "o (as in so)", "example": "ওপৰ (above)"},
    {"assamese": "ঔ", "transliteration": "ou", "bengali": "ঔ", "english": "ou", "example": "ঔষধ (medicine)"},
]

ASSAMESE_CONSONANTS = [
    {"assamese": "ক", "transliteration": "k/ko", "bengali": "ক", "english": "k"},
    {"assamese": "খ", "transliteration": "kh/kho", "bengali": "খ", "english": "kh (aspirated k)"},
    {"assamese": "গ", "transliteration": "g/go", "bengali": "গ", "english": "g"},
    {"assamese": "ঘ", "transliteration": "gh/gho", "bengali": "ঘ", "english": "gh (aspirated g)"},
    {"assamese": "ঙ", "transliteration": "ng/ngo", "bengali": "ঙ", "english": "ng"},
    {"assamese": "চ", "transliteration": "s/so", "bengali": "চ", "english": "s/ch"},
    {"assamese": "ছ", "transliteration": "ss/sso", "bengali": "ছ", "english": "sh (aspirated)"},
    {"assamese": "জ", "transliteration": "j/jo", "bengali": "জ", "english": "j/z"},
    {"assamese": "ঝ", "transliteration": "jh/jho", "bengali": "ঝ", "english": "jh (aspirated j)"},
    {"assamese": "ট", "transliteration": "t/to", "bengali": "ট", "english": "t (retroflex)"},
    {"assamese": "ড", "transliteration": "d/do", "bengali": "ড", "english": "d (retroflex)"},
    {"assamese": "ত", "transliteration": "t/to", "bengali": "ত", "english": "t (dental)"},
    {"assamese": "দ", "transliteration": "d/do", "bengali": "দ", "english": "d (dental)"},
    {"assamese": "ন", "transliteration": "n/no", "bengali": "ন", "english": "n"},
    {"assamese": "প", "transliteration": "p/po", "bengali": "প", "english": "p"},
    {"assamese": "ফ", "transliteration": "ph/pho", "bengali": "ফ", "english": "ph/f"},
    {"assamese": "ব", "transliteration": "b/bo", "bengali": "ব", "english": "b"},
    {"assamese": "ম", "transliteration": "m/mo", "bengali": "ম", "english": "m"},
    {"assamese": "য", "transliteration": "j/jo", "bengali": "য", "english": "y/j"},
    {"assamese": "ৰ", "transliteration": "r/ro", "bengali": "র", "english": "r (unique to Assamese)"},
    {"assamese": "ল", "transliteration": "l/lo", "bengali": "ল", "english": "l"},
    {"assamese": "ৱ", "transliteration": "w/wo", "bengali": "ব", "english": "w (unique to Assamese)"},
    {"assamese": "শ", "transliteration": "x/xo", "bengali": "শ", "english": "x/sh (unique Assamese sound)"},
    {"assamese": "হ", "transliteration": "h/ho", "bengali": "হ", "english": "h"},
]

# ===================== DAILY LESSONS =====================
DAILY_LESSONS = {
    1: {
        "title": "গৃহ আৰু পৰিয়াল | Home and Family",
        "title_en": "Home and Family",
        "description": "Learn words related to home and family members",
        "vocabulary": [
            {"assamese": "ঘৰ", "transliteration": "ghor", "bengali": "ঘর", "english": "home/house"},
            {"assamese": "মা", "transliteration": "maa", "bengali": "মা", "english": "mother"},
            {"assamese": "দেউতা", "transliteration": "deuta", "bengali": "বাবা", "english": "father"},
            {"assamese": "ককাই", "transliteration": "kokai", "bengali": "দাদা", "english": "elder brother"},
            {"assamese": "বাই", "transliteration": "baai", "bengali": "দিদি", "english": "elder sister"},
            {"assamese": "ভাই", "transliteration": "bhai", "bengali": "ভাই", "english": "younger brother"},
            {"assamese": "ভনী", "transliteration": "bhoni", "bengali": "বোন", "english": "younger sister"},
            {"assamese": "আইতা", "transliteration": "aaita", "bengali": "দিদিমা", "english": "grandmother"},
            {"assamese": "ককা", "transliteration": "koka", "bengali": "দাদু", "english": "grandfather"},
        ],
        "phrases": [
            {"assamese": "মোৰ নাম ... ।", "transliteration": "mor naam ...", "bengali": "আমার নাম ... ।", "english": "My name is ..."},
            {"assamese": "আপোনাৰ নাম কি?", "transliteration": "aponaar naam ki?", "bengali": "আপনার নাম কি?", "english": "What is your name?"},
            {"assamese": "মই ... ত থাকো।", "transliteration": "moi ... t thako", "bengali": "আমি ... এ থাকি।", "english": "I live in ..."},
        ],
        "grammar_note": "In Assamese, 'মই' (moi) means 'I' and 'মোৰ' (mor) means 'my'. Unlike Bengali 'আমি', Assamese uses 'মই'.",
        "fun_fact": "🎵 Assamese is known as the 'Language of the East' and has a rich literary tradition dating back to the 13th century!"
    },
    2: {
        "title": "সম্ভাষণ আৰু বিদায় | Greetings & Farewells",
        "title_en": "Greetings & Farewells",
        "description": "Common greetings and polite expressions in Assamese",
        "vocabulary": [
            {"assamese": "নমস্কাৰ", "transliteration": "nomoskar", "bengali": "নমস্কার", "english": "Hello/Greetings"},
            {"assamese": "আদাব", "transliteration": "adab", "bengali": "আদাব", "english": "Salutation (Islamic)"},
            {"assamese": "আপোনাক ধন্যবাদ", "transliteration": "aponake dhonyobad", "bengali": "আপনাকে ধন্যবাদ", "english": "Thank you"},
            {"assamese": "মাফ কৰিব", "transliteration": "maph korib", "bengali": "মাফ করবেন", "english": "Excuse me / Sorry"},
            {"assamese": "হয়", "transliteration": "hoy", "bengali": "হ্যাঁ", "english": "Yes"},
            {"assamese": "নহয়", "transliteration": "nohoy", "bengali": "না", "english": "No"},
            {"assamese": "ভালেই আছো", "transliteration": "bhalei aaso", "bengali": "ভালো আছি", "english": "I am fine"},
            {"assamese": "পুনৰ লগ পাম", "transliteration": "punor log paam", "bengali": "আবার দেখা হবে", "english": "See you again"},
        ],
        "phrases": [
            {"assamese": "আপুনি কেনে আছে?", "transliteration": "apuni kene aase?", "bengali": "আপনি কেমন আছেন?", "english": "How are you? (formal)"},
            {"assamese": "তুমি কেনে আছা?", "transliteration": "tumi kene aasa?", "bengali": "তুমি কেমন আছ?", "english": "How are you? (informal)"},
            {"assamese": "শুভ ৰাতিপুৱা", "transliteration": "xubho raatipuwa", "bengali": "শুভ সকাল", "english": "Good morning"},
            {"assamese": "শুভ নিশা", "transliteration": "xubho nisha", "bengali": "শুভ রাত্রি", "english": "Good night"},
        ],
        "grammar_note": "Assamese uses 'আপুনি' (apuni) for formal 'you' and 'তুমি' (tumi) for informal. Similar to Bengali আপনি/তুমি.",
        "fun_fact": "🦋 The word 'নমস্কাৰ' (nomoskar) is shared with Bengali but has a unique Assamese pronunciation with the 'র' sound!"
    },
    3: {
        "title": "খাদ্য আৰু পানীয় | Food and Drinks",
        "title_en": "Food and Drinks",
        "description": "Essential vocabulary for food, eating, and dining",
        "vocabulary": [
            {"assamese": "ভাত", "transliteration": "bhat", "bengali": "ভাত", "english": "rice (cooked)"},
            {"assamese": "মাছ", "transliteration": "maas", "bengali": "মাছ", "english": "fish"},
            {"assamese": "মাংস", "transliteration": "maangx", "bengali": "মাংস", "english": "meat"},
            {"assamese": "পাচলি", "transliteration": "paasoli", "bengali": "সবজি", "english": "vegetables"},
            {"assamese": "পানী", "transliteration": "paani", "bengali": "জল/পানি", "english": "water"},
            {"assamese": "চাহ", "transliteration": "xah", "bengali": "চা", "english": "tea"},
            {"assamese": "আম", "transliteration": "aam", "bengali": "আম", "english": "mango"},
            {"assamese": "কল", "transliteration": "kol", "bengali": "কলা", "english": "banana"},
            {"assamese": "লেতেকু", "transliteration": "leteku", "bengali": "সবেদা", "english": "sapodilla (unique Assamese fruit)"},
            {"assamese": "খাওঁ", "transliteration": "khaao", "bengali": "খাই", "english": "I eat"},
        ],
        "phrases": [
            {"assamese": "মই ভোক লাগিছে", "transliteration": "moi bhok laagise", "bengali": "আমার খিদে লেগেছে", "english": "I am hungry"},
            {"assamese": "এইটো বৰ সুস্বাদু", "transliteration": "eitoo bor suxwadu", "bengali": "এটা খুব সুস্বাদু", "english": "This is very delicious"},
            {"assamese": "আৰু অলপ দিব নে?", "transliteration": "aaroo olop dib ne?", "bengali": "আরও একটু দেবেন?", "english": "Can you give me a little more?"},
        ],
        "grammar_note": "Notice 'চাহ' (xah) for tea - Assam is famous for tea! The 'x' in Assamese makes a 'sh' sound, unique from Bengali.",
        "fun_fact": "🍵 Assam produces over 50% of India's tea! The word for tea 'চাহ' is central to Assamese culture."
    },
    4: {
        "title": "সংখ্যা আৰু সময় | Numbers and Time",
        "title_en": "Numbers and Time",
        "description": "Count in Assamese and tell the time",
        "vocabulary": [
            {"assamese": "এক", "transliteration": "ek", "bengali": "এক", "english": "one (1)"},
            {"assamese": "দুই", "transliteration": "dui", "bengali": "দুই", "english": "two (2)"},
            {"assamese": "তিনি", "transliteration": "tini", "bengali": "তিন", "english": "three (3)"},
            {"assamese": "চাৰি", "transliteration": "saari", "bengali": "চার", "english": "four (4)"},
            {"assamese": "পাঁচ", "transliteration": "paas", "bengali": "পাঁচ", "english": "five (5)"},
            {"assamese": "ছয়", "transliteration": "xoi", "bengali": "ছয়", "english": "six (6)"},
            {"assamese": "সাত", "transliteration": "xaat", "bengali": "সাত", "english": "seven (7)"},
            {"assamese": "আঠ", "transliteration": "aath", "bengali": "আট", "english": "eight (8)"},
            {"assamese": "ন", "transliteration": "no", "bengali": "নয়", "english": "nine (9)"},
            {"assamese": "দহ", "transliteration": "doh", "bengali": "দশ", "english": "ten (10)"},
        ],
        "phrases": [
            {"assamese": "এতিয়া কিমান বাজিছে?", "transliteration": "etiya kiman baajise?", "bengali": "এখন কটা বাজে?", "english": "What time is it now?"},
            {"assamese": "আজি কি বাৰ?", "transliteration": "aaji ki bar?", "bengali": "আজ কি বার?", "english": "What day is today?"},
            {"assamese": "কাইলৈ দেখা হব", "transliteration": "kailoi dekha hob", "bengali": "কাল দেখা হবে", "english": "See you tomorrow"},
        ],
        "grammar_note": "Assamese numbers are similar to Bengali but with unique pronunciations. Note 'সাত' (xaat) vs Bengali 'সাত' (saat).",
        "fun_fact": "📅 The Assamese calendar 'বহাগ' (Bohag) marks the new year with the festival of Bihu in April!"
    },
    5: {
        "title": "ৰং আৰু প্ৰকৃতি | Colors and Nature",
        "title_en": "Colors and Nature",
        "description": "Describe the world around you in Assamese",
        "vocabulary": [
            {"assamese": "ৰঙা", "transliteration": "ronga", "bengali": "লাল", "english": "red"},
            {"assamese": "নীলা", "transliteration": "nila", "bengali": "নীল", "english": "blue"},
            {"assamese": "হালধীয়া", "transliteration": "haldiya", "bengali": "হলুদ", "english": "yellow"},
            {"assamese": "সেউজীয়া", "transliteration": "seujia", "bengali": "সবুজ", "english": "green"},
            {"assamese": "বগা", "transliteration": "boga", "bengali": "সাদা", "english": "white"},
            {"assamese": "কলা", "transliteration": "kola", "bengali": "কালো", "english": "black"},
            {"assamese": "নদী", "transliteration": "nodi", "bengali": "নদী", "english": "river"},
            {"assamese": "পাহাৰ", "transliteration": "pahar", "bengali": "পাহাড়", "english": "hill/mountain"},
            {"assamese": "ব্ৰহ্মপুত্ৰ", "transliteration": "brahmoputro", "bengali": "ব্রহ্মপুত্র", "english": "Brahmaputra (river)"},
            {"assamese": "হাতী", "transliteration": "haati", "bengali": "হাতি", "english": "elephant"},
        ],
        "phrases": [
            {"assamese": "অসম বৰ সুন্দৰ", "transliteration": "oxom bor xundor", "bengali": "আসাম খুব সুন্দর", "english": "Assam is very beautiful"},
            {"assamese": "ব্ৰহ্মপুত্ৰ এখন ডাঙৰ নদী", "transliteration": "brahmoputro ekhan daangor nodi", "bengali": "ব্রহ্মপুত্র একটা বড় নদী", "english": "Brahmaputra is a big river"},
        ],
        "grammar_note": "Color words in Assamese often end in '-া' (aa). Notice ৰঙা (red), নীলা (blue), হালধীয়া (yellow).",
        "fun_fact": "🐘 Assam is home to the famous Kaziranga National Park with the world's largest population of one-horned rhinoceroses!"
    },
    6: {
        "title": "দৈনন্দিন কাৰ্যকলাপ | Daily Activities",
        "title_en": "Daily Activities",
        "description": "Talk about everyday routines and activities",
        "vocabulary": [
            {"assamese": "উঠা", "transliteration": "utha", "bengali": "ওঠা", "english": "to wake up / get up"},
            {"assamese": "খোৱা", "transliteration": "khowa", "bengali": "খাওয়া", "english": "to eat"},
            {"assamese": "পঢ়া", "transliteration": "pora", "bengali": "পড়া", "english": "to read/study"},
            {"assamese": "লিখা", "transliteration": "likha", "bengali": "লেখা", "english": "to write"},
            {"assamese": "খেলা", "transliteration": "khela", "bengali": "খেলা", "english": "to play"},
            {"assamese": "শোৱা", "transliteration": "xowa", "bengali": "ঘুমানো", "english": "to sleep"},
            {"assamese": "যোৱা", "transliteration": "jowa", "bengali": "যাওয়া", "english": "to go"},
            {"assamese": "অহা", "transliteration": "oha", "bengali": "আসা", "english": "to come"},
            {"assamese": "কাম কৰা", "transliteration": "kaam kora", "bengali": "কাজ করা", "english": "to work"},
            {"assamese": "গোৱা", "transliteration": "guwa", "bengali": "গাওয়া", "english": "to sing"},
        ],
        "phrases": [
            {"assamese": "মই ৰাতিপুৱা সোনকালে উঠো", "transliteration": "moi raatipuwa xonkale utho", "bengali": "আমি সকালে তাড়াতাড়ি উঠি", "english": "I wake up early in the morning"},
            {"assamese": "মই প্ৰতিদিন পঢ়ো", "transliteration": "moi protidin poro", "bengali": "আমি প্রতিদিন পড়ি", "english": "I study every day"},
        ],
        "grammar_note": "Assamese verbs end in '-া' in infinitive form. 'মই' (I) + verb root + 'ো' for present tense (মই পঢ়ো = I read).",
        "fun_fact": "🎭 Assamese has a rich tradition of 'Bhaona' - traditional theatre that combines dance, music and drama!"
    },
    7: {
        "title": "সাপ্তাহিক পুনৰীক্ষণ | Weekly Review",
        "title_en": "Weekly Review & Test",
        "description": "Review all lessons from the week and take the weekly test",
        "vocabulary": [],
        "phrases": [],
        "grammar_note": "Great job completing your first week! Review all previous lessons before taking the weekly test.",
        "fun_fact": "🏆 You've completed your first week of Assamese learning! The Assamese script is based on the Kamrupi script and is closely related to Bengali script."
    }
}

# ===================== QUIZ QUESTIONS =====================
QUIZ_QUESTIONS = {
    "beginner": [
        {
            "question": "What does 'নমস্কাৰ' (nomoskar) mean?",
            "question_bn": "'নমস্কাৰ' (nomoskar) মানে কি?",
            "options": ["Goodbye", "Hello/Greetings", "Thank you", "Sorry"],
            "answer": 1,
            "explanation": "নমস্কাৰ (nomoskar) is the standard greeting in Assamese, equivalent to Bengali নমস্কার"
        },
        {
            "question": "How do you say 'mother' in Assamese?",
            "question_bn": "অসমীয়াত 'মা'-কে কি বোলে?",
            "options": ["দেউতা", "ককাই", "মা", "আইতা"],
            "answer": 2,
            "explanation": "মা (maa) means mother in Assamese, same as Bengali!"
        },
        {
            "question": "Which of these means 'water' in Assamese?",
            "question_bn": "এইবোৰৰ কোনটো অসমীয়াত 'জল' বোজায়?",
            "options": ["চাহ", "পানী", "ভাত", "মাছ"],
            "answer": 1,
            "explanation": "পানী (paani) means water in Assamese, while Bengali uses জল or পানি"
        },
        {
            "question": "What is 'five' in Assamese?",
            "question_bn": "অসমীয়াত 'পাঁচ' কি?",
            "options": ["এক", "তিনি", "পাঁচ", "দহ"],
            "answer": 2,
            "explanation": "পাঁচ (paas) means five in Assamese, similar to Bengali পাঁচ"
        },
        {
            "question": "How do you say 'Yes' in Assamese?",
            "question_bn": "অসমীয়াত 'হ্যাঁ' মানে কি?",
            "options": ["নহয়", "হয়", "মাফ", "ধন্যবাদ"],
            "answer": 1,
            "explanation": "হয় (hoy) means Yes in Assamese, while No is নহয় (nohoy)"
        },
        {
            "question": "What does 'দেউতা' (deuta) mean?",
            "question_bn": "'দেউতা' (deuta) মানে কি?",
            "options": ["Mother", "Brother", "Father", "Grandfather"],
            "answer": 2,
            "explanation": "দেউতা (deuta) means father in Assamese. Unlike Bengali বাবা, Assamese uses the unique word দেউতা"
        },
        {
            "question": "Which word is unique to Assamese (not found in Bengali)?",
            "question_bn": "কোন শব্দটো কেৱল অসমীয়াত পোৱা যায়?",
            "options": ["মাছ", "ভাত", "লেতেকু", "আম"],
            "answer": 2,
            "explanation": "লেতেকু (leteku) is a fruit unique to Assamese vocabulary. It's the sapodilla fruit!"
        },
        {
            "question": "How do you say 'I am fine' in Assamese?",
            "question_bn": "অসমীয়াত 'আমি ভালো আছি' কিদৰে কব?",
            "options": ["মই ভোক লাগিছে", "ভালেই আছো", "মাফ কৰিব", "পুনৰ লগ পাম"],
            "answer": 1,
            "explanation": "ভালেই আছো (bhalei aaso) means 'I am fine' in Assamese"
        },
    ],
    "intermediate": [
        {
            "question": "Complete: 'মোৰ নাম ___' means:",
            "question_bn": "'মোৰ নাম ___' মানে কি?",
            "options": ["Your name is...", "My name is...", "His name is...", "What is the name?"],
            "answer": 1,
            "explanation": "মোৰ (mor) = my in Assamese. মোৰ নাম = My name is..."
        },
        {
            "question": "The Assamese letter 'ৰ' is unique because:",
            "question_bn": "অসমীয়া আখৰ 'ৰ' অনন্য কাৰণ:",
            "options": ["It doesn't exist in Bengali", "It sounds like 'z'", "It is silent", "It replaces 'ক'"],
            "answer": 0,
            "explanation": "ৰ (ro) is a unique Assamese letter not found in standard Bengali script!"
        },
        {
            "question": "আপুনি কেনে আছে? This is:",
            "question_bn": "'আপুনি কেনে আছে?' এইটো কি?",
            "options": ["Informal greeting", "Formal way of asking 'how are you'", "A farewell", "An apology"],
            "answer": 1,
            "explanation": "আপুনি (apuni) is the formal 'you' in Assamese, like Bengali আপনি"
        },
    ]
}

# ===================== GRAMMAR RULES =====================
GRAMMAR_RULES = [
    {
        "title": "Personal Pronouns | ব্যক্তিগত সৰ্বনাম",
        "rules": [
            {"assamese": "মই", "transliteration": "moi", "bengali": "আমি", "english": "I"},
            {"assamese": "মোৰ", "transliteration": "mor", "bengali": "আমার", "english": "my"},
            {"assamese": "মোক", "transliteration": "mok", "bengali": "আমাকে", "english": "me (object)"},
            {"assamese": "তুমি", "transliteration": "tumi", "bengali": "তুমি", "english": "you (informal)"},
            {"assamese": "আপুনি", "transliteration": "apuni", "bengali": "আপনি", "english": "you (formal)"},
            {"assamese": "সি / তেওঁ", "transliteration": "xi / tewo", "bengali": "সে / তিনি", "english": "he/she / he/she (formal)"},
            {"assamese": "আমি", "transliteration": "aami", "bengali": "আমরা", "english": "we"},
            {"assamese": "তোমালোক", "transliteration": "tomalok", "bengali": "তোমরা", "english": "you (plural)"},
            {"assamese": "তেওঁলোক", "transliteration": "tewolok", "bengali": "তারা / তাঁরা", "english": "they"},
        ]
    },
    {
        "title": "Verb Conjugation | ক্ৰিয়া বিভক্তি",
        "rules": [
            {"assamese": "মই যাওঁ", "transliteration": "moi jaao", "bengali": "আমি যাই", "english": "I go"},
            {"assamese": "তুমি যোৱা", "transliteration": "tumi jowa", "bengali": "তুমি যাও", "english": "You go (informal)"},
            {"assamese": "আপুনি যাওক", "transliteration": "apuni jaok", "bengali": "আপনি যান", "english": "You go (formal)"},
            {"assamese": "সি যায়", "transliteration": "xi jay", "bengali": "সে যায়", "english": "He/She goes"},
            {"assamese": "আমি যাওঁ", "transliteration": "aami jaao", "bengali": "আমরা যাই", "english": "We go"},
        ]
    }
]

# ===================== CULTURAL FACTS =====================
CULTURAL_FACTS = [
    {"fact": "Bihu is the most important festival of Assam, celebrated three times a year!", "emoji": "🎊"},
    {"fact": "Assam is the largest tea-producing state in India, famous worldwide for Assam Tea!", "emoji": "🍵"},
    {"fact": "Kaziranga National Park in Assam is a UNESCO World Heritage Site!", "emoji": "🦏"},
    {"fact": "The one-horned rhinoceros is the state animal of Assam!", "emoji": "🦏"},
    {"fact": "Majuli in Assam is the world's largest river island!", "emoji": "🏝️"},
    {"fact": "The Kamakhya Temple in Guwahati is one of the most sacred Shakti temples in India!", "emoji": "🛕"},
    {"fact": "Assamese silk (Muga silk) is unique to Assam and is internationally renowned!", "emoji": "🪡"},
    {"fact": "The Assamese film industry is one of the oldest in India!", "emoji": "🎬"},
    {"fact": "Guwahati is the largest city in Assam and the gateway to Northeast India!", "emoji": "🌆"},
    {"fact": "Assam has the largest number of wild elephants in India!", "emoji": "🐘"},
]

MOTIVATIONAL_MESSAGES = [
    "তুমি বৰ ভালদৰে কৰিছা! (You are doing very well!)",
    "লাহে লাহে অভ্যাস কৰক! (Practice slowly, steadily!)",
    "প্ৰতিদিন শিকক, প্ৰতিদিন বাঢ়ক! (Learn every day, grow every day!)",
    "অসমীয়া শিক্ষা তোমাৰ বাবে! (Assamese learning is for you!)",
    "চেষ্টা কৰক, সফল হওক! (Try, succeed!)",
]
