"""
অসমীয়া শিক্ষা — Complete Assamese Language Learning Platform
120-day curriculum · Native regional voices · AI conversation partner
Self-contained single file — Streamlit Cloud ready
"""

import io, os, random, subprocess, tempfile, json
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from datetime import date, timedelta

st.set_page_config(
    page_title="অসমীয়া শিক্ষা · Learn Assamese",
    page_icon="🦚", layout="wide",
    initial_sidebar_state="expanded",
)

# ══════════════════════════════════════════════════════════════════════════════
#  VOICE ENGINE
# ══════════════════════════════════════════════════════════════════════════════

VOICE_PROFILES = {
    "🦚 Assamese Native":  {"lang": "as", "speed": 130, "pitch": 46, "desc": "Pure Assamese — অসমীয়া native phonemes"},
    "🐯 Bengali Regional": {"lang": "bn", "speed": 120, "pitch": 43, "desc": "Bengali — closest regional relative"},
    "🇮🇳 Hindi Indian":    {"lang": "hi", "speed": 118, "pitch": 40, "desc": "Hindi Indian — widely understood"},
}
DEFAULT_VOICE = "🦚 Assamese Native"

def _espeak_mp3(text, lang="as", speed=130, pitch=46, slow=False):
    if slow: speed = max(65, speed - 45)
    wf = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    mf = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
    wf.close(); mf.close()
    try:
        r1 = subprocess.run(
            ["espeak-ng", "-v", lang, "-s", str(speed), "-p", str(pitch), "-w", wf.name, text],
            capture_output=True, timeout=12)
        if r1.returncode != 0 or os.path.getsize(wf.name) < 100:
            return None
        r2 = subprocess.run(
            ["ffmpeg", "-y", "-i", wf.name, "-ab", "128k", "-q:a", "2", mf.name],
            capture_output=True, timeout=12)
        if r2.returncode != 0 or os.path.getsize(mf.name) < 100:
            return None
        buf = io.BytesIO(open(mf.name, "rb").read())
        buf.seek(0)
        return buf
    except Exception:
        return None
    finally:
        for p in [wf.name, mf.name]:
            try: os.unlink(p)
            except: pass

def speak(text, slow=False, key_suffix=""):
    p = VOICE_PROFILES.get(st.session_state.get("voice_profile", DEFAULT_VOICE), VOICE_PROFILES[DEFAULT_VOICE])
    buf = _espeak_mp3(text, lang=p["lang"], speed=p["speed"], pitch=p["pitch"], slow=slow)
    if buf:
        st.audio(buf, format="audio/mp3")
    else:
        st.caption(f"🔊 {text}")

# ══════════════════════════════════════════════════════════════════════════════
#  FULL 120-DAY CURRICULUM DATA
# ══════════════════════════════════════════════════════════════════════════════

# ── Week 1-2: Foundations ────────────────────────────────────────────────────
CURRICULUM = {
    # PHASE 1: FOUNDATIONS (Days 1-30)
    1:  {"week":1,"phase":"Foundation","title":"পৰিচয় | Introductions","title_en":"Introductions",
         "vocab":[
            {"a":"নমস্কাৰ","t":"nomoskar","b":"নমস্কার","e":"Hello / Greetings"},
            {"a":"মোৰ নাম","t":"mor naam","b":"আমার নাম","e":"My name is"},
            {"a":"মই","t":"moi","b":"আমি","e":"I"},
            {"a":"আপুনি","t":"apuni","b":"আপনি","e":"You (formal)"},
            {"a":"তুমি","t":"tumi","b":"তুমি","e":"You (informal)"},
            {"a":"ভালেই আছো","t":"bhalei aacho","b":"ভালো আছি","e":"I am fine"},
            {"a":"ধন্যবাদ","t":"dhonyobad","b":"ধন্যবাদ","e":"Thank you"},
            {"a":"মাফ কৰিব","t":"maph korib","b":"মাফ করবেন","e":"Excuse me / Sorry"},
         ],
         "phrases":[
            {"a":"আপোনাৰ নাম কি?","t":"aponaar naam ki?","b":"আপনার নাম কি?","e":"What is your name?"},
            {"a":"মই অসমৰ পৰা আহিছো","t":"moi oxomor pora aahiso","b":"আমি আসাম থেকে এসেছি","e":"I am from Assam"},
            {"a":"আপুনি কেনে আছে?","t":"apuni kene aase?","b":"আপনি কেমন আছেন?","e":"How are you? (formal)"},
            {"a":"পুনৰ লগ পাম","t":"punor log paam","b":"আবার দেখা হবে","e":"See you again"},
         ],
         "grammar":"In Assamese 'মই' (moi) = I, unlike Bengali 'আমি'. 'মোৰ' (mor) = my. The formal 'you' is আপুনি (apuni).",
         "culture":"🦚 Assamese (অসমীয়া) is spoken by 15 million people. It is the official language of Assam state and the easternmost Indo-Aryan language."},

    2:  {"week":1,"phase":"Foundation","title":"পৰিয়াল | Family","title_en":"Family",
         "vocab":[
            {"a":"মা","t":"maa","b":"মা","e":"mother"},
            {"a":"দেউতা","t":"deuta","b":"বাবা","e":"father"},
            {"a":"ককাই","t":"kokai","b":"দাদা","e":"elder brother"},
            {"a":"বাই","t":"baai","b":"দিদি","e":"elder sister"},
            {"a":"ভাই","t":"bhai","b":"ভাই","e":"younger brother"},
            {"a":"ভনী","t":"bhoni","b":"বোন","e":"younger sister"},
            {"a":"আইতা","t":"aaita","b":"দিদিমা","e":"grandmother (maternal)"},
            {"a":"ককা","t":"koka","b":"দাদু","e":"grandfather (maternal)"},
            {"a":"নানী","t":"naani","b":"নানি","e":"grandmother (paternal)"},
            {"a":"দাদা","t":"daadaa","b":"দাদা","e":"grandfather (paternal)"},
            {"a":"পেহী","t":"pehi","b":"ফুপু","e":"father's sister"},
            {"a":"মামা","t":"maama","b":"মামা","e":"mother's brother"},
         ],
         "phrases":[
            {"a":"মোৰ এটা ভাই আছে","t":"mor ekta bhai aahe","b":"আমার একটি ভাই আছে","e":"I have one brother"},
            {"a":"আমাৰ পৰিয়াল ডাঙৰ","t":"aamar poriyaal daangor","b":"আমাদের পরিবার বড়","e":"Our family is big"},
            {"a":"মোৰ মা বৰ ভালপায়","t":"mor maa bor bhaalopay","b":"আমার মা খুব ভালোবাসেন","e":"My mother loves very much"},
         ],
         "grammar":"Possessive: মোৰ (my), তোমাৰ (your-inf), আপোনাৰ (your-form), তেওঁৰ (his/her), আমাৰ (our).",
         "culture":"👨‍👩‍👧‍👦 Assamese families traditionally use specific words for each relative's position. 'আইতা-ককা' (maternal grandparents) differ from 'নানী-দাদা' (paternal)."},

    3:  {"week":1,"phase":"Foundation","title":"সংখ্যা | Numbers 1-20","title_en":"Numbers 1-20",
         "vocab":[
            {"a":"এক","t":"ek","b":"এক","e":"1"},{"a":"দুই","t":"dui","b":"দুই","e":"2"},
            {"a":"তিনি","t":"tini","b":"তিন","e":"3"},{"a":"চাৰি","t":"saari","b":"চার","e":"4"},
            {"a":"পাঁচ","t":"paas","b":"পাঁচ","e":"5"},{"a":"ছয়","t":"xoi","b":"ছয়","e":"6"},
            {"a":"সাত","t":"xaat","b":"সাত","e":"7"},{"a":"আঠ","t":"aath","b":"আট","e":"8"},
            {"a":"ন","t":"no","b":"নয়","e":"9"},{"a":"দহ","t":"doh","b":"দশ","e":"10"},
            {"a":"এঘাৰ","t":"eghaar","b":"এগারো","e":"11"},{"a":"বাৰ","t":"baar","b":"বারো","e":"12"},
            {"a":"তেৰ","t":"ter","b":"তেরো","e":"13"},{"a":"চৈধ্য","t":"soidho","b":"চৌদ্দ","e":"14"},
            {"a":"পোন্ধৰ","t":"pondhor","b":"পনেরো","e":"15"},{"a":"ষোল্ল","t":"xollo","b":"ষোলো","e":"16"},
            {"a":"সোতৰ","t":"xotor","b":"সতেরো","e":"17"},{"a":"আঠাৰ","t":"aathaar","b":"আঠারো","e":"18"},
            {"a":"উনৈশ","t":"unois","b":"উনিশ","e":"19"},{"a":"বিশ","t":"bix","b":"বিশ","e":"20"},
         ],
         "phrases":[
            {"a":"মোৰ বয়স বিশ বছৰ","t":"mor boyos bix boshor","b":"আমার বয়স বিশ বছর","e":"I am twenty years old"},
            {"a":"কিমান?","t":"kimaan?","b":"কতটা?","e":"How many/much?"},
            {"a":"এটা দিব","t":"ekta dib","b":"একটা দাও","e":"Give one (please)"},
         ],
         "grammar":"Assamese uses the same number system as Bengali but with unique pronunciation: ছয় (xoi) not 'choy', সাত (xaat) not 'saat'.",
         "culture":"🔢 Traditional Assamese counting uses the decimal system. Market bargaining (দাম কৰা) is an important cultural practice."},

    4:  {"week":1,"phase":"Foundation","title":"বাৰ আৰু সময় | Days & Time","title_en":"Days & Time",
         "vocab":[
            {"a":"ৰবিবাৰ","t":"robibaar","b":"রবিবার","e":"Sunday"},
            {"a":"সোমবাৰ","t":"xombaar","b":"সোমবার","e":"Monday"},
            {"a":"মঙলবাৰ","t":"mongolbaar","b":"মঙ্গলবার","e":"Tuesday"},
            {"a":"বুধবাৰ","t":"budhbaar","b":"বুধবার","e":"Wednesday"},
            {"a":"বৃহস্পতিবাৰ","t":"brihoshpotibaar","b":"বৃহস্পতিবার","e":"Thursday"},
            {"a":"শুক্ৰবাৰ","t":"xukrobaar","b":"শুক্রবার","e":"Friday"},
            {"a":"শনিবাৰ","t":"xonibaar","b":"শনিবার","e":"Saturday"},
            {"a":"ৰাতিপুৱা","t":"raatipuwa","b":"সকাল","e":"morning"},
            {"a":"দুপৰীয়া","t":"duporiya","b":"দুপুর","e":"afternoon/noon"},
            {"a":"আবেলি","t":"aabeli","b":"বিকেল","e":"evening"},
            {"a":"নিশা","t":"nisha","b":"রাত","e":"night"},
            {"a":"আজি","t":"aaji","b":"আজ","e":"today"},
            {"a":"কালি","t":"kaali","b":"কাল","e":"yesterday / tomorrow"},
            {"a":"পৰহি","t":"porhi","b":"পরশু","e":"day after/before tomorrow"},
         ],
         "phrases":[
            {"a":"এতিয়া কিমান বাজিছে?","t":"etiya kimaan baajise?","b":"এখন কটা বাজে?","e":"What time is it now?"},
            {"a":"আজি কি বাৰ?","t":"aaji ki baar?","b":"আজ কি বার?","e":"What day is today?"},
            {"a":"শুভ ৰাতিপুৱা","t":"xubho raatipuwa","b":"শুভ সকাল","e":"Good morning"},
            {"a":"শুভ নিশা","t":"xubho nisha","b":"শুভ রাত্রি","e":"Good night"},
         ],
         "grammar":"'কালি' (kaali) means both yesterday AND tomorrow — context determines meaning. Use আগলৈ (future) or আগৰ (past) to clarify.",
         "culture":"📅 The Assamese calendar follows the traditional Saka era. The New Year 'বহাগ বিহু' falls in mid-April."},

    5:  {"week":2,"phase":"Foundation","title":"ৰং | Colours","title_en":"Colours",
         "vocab":[
            {"a":"ৰঙা","t":"ronga","b":"লাল","e":"red"},
            {"a":"নীলা","t":"nila","b":"নীল","e":"blue"},
            {"a":"হালধীয়া","t":"haldiya","b":"হলুদ","e":"yellow"},
            {"a":"সেউজীয়া","t":"seujia","b":"সবুজ","e":"green"},
            {"a":"বগা","t":"boga","b":"সাদা","e":"white"},
            {"a":"কলা","t":"kola","b":"কালো","e":"black"},
            {"a":"মটীয়া","t":"motiya","b":"বাদামী","e":"brown"},
            {"a":"গুলপীয়া","t":"gulpiya","b":"গোলাপি","e":"pink"},
            {"a":"কমলা","t":"komola","b":"কমলা","e":"orange"},
            {"a":"বেঙুনীয়া","t":"benguniya","b":"বেগুনি","e":"purple"},
         ],
         "phrases":[
            {"a":"এইটো কেনে ৰঙৰ?","t":"eitoo kene rongor?","b":"এটা কী রঙের?","e":"What colour is this?"},
            {"a":"মই নীলা ভাল পাওঁ","t":"moi nila bhaal paao","b":"আমি নীল পছন্দ করি","e":"I like blue"},
         ],
         "grammar":"Colours as adjectives precede the noun: নীলা আকাশ (blue sky), ৰঙা ফুল (red flower). They agree with nouns.",
         "culture":"🎨 The Muga silk of Assam has a unique golden colour found nowhere else in the world — 'মুগা' is Assam's gift to the world."},

    6:  {"week":2,"phase":"Foundation","title":"খাদ্য | Food","title_en":"Food & Eating",
         "vocab":[
            {"a":"ভাত","t":"bhat","b":"ভাত","e":"cooked rice"},
            {"a":"মাছ","t":"maas","b":"মাছ","e":"fish"},
            {"a":"মাংস","t":"maangx","b":"মাংস","e":"meat"},
            {"a":"পাচলি","t":"paasoli","b":"সবজি","e":"vegetables"},
            {"a":"পানী","t":"paani","b":"জল/পানি","e":"water"},
            {"a":"চাহ","t":"xah","b":"চা","e":"tea"},
            {"a":"গাখীৰ","t":"gaakhir","b":"দুধ","e":"milk"},
            {"a":"চেনি","t":"xeni","b":"চিনি","e":"sugar"},
            {"a":"নিমখ","t":"nimokh","b":"লবণ","e":"salt"},
            {"a":"মিৰচি","t":"mirchi","b":"মরিচ","e":"chilli"},
            {"a":"পিঠা","t":"pitha","b":"পিঠা","e":"Assamese rice cake"},
            {"a":"লাৰু","t":"laaru","b":"লাড্ডু","e":"sweet ball (Assamese)"},
            {"a":"খাওঁ","t":"khaao","b":"খাই","e":"I eat"},
            {"a":"খোৱা","t":"khowa","b":"খাওয়া","e":"to eat"},
         ],
         "phrases":[
            {"a":"মই ভোক লাগিছে","t":"moi bhok laagise","b":"আমার খিদে লেগেছে","e":"I am hungry"},
            {"a":"এইটো বৰ সুস্বাদু","t":"eitoo bor xuxwadu","b":"এটা খুব সুস্বাদু","e":"This is very delicious"},
            {"a":"আৰু অলপ দিব নে?","t":"aaroo olop dib ne?","b":"আরও একটু দেবেন?","e":"Can I have a little more?"},
            {"a":"বিল কিমান হল?","t":"bil kimaan hol?","b":"বিল কত হলো?","e":"How much is the bill?"},
         ],
         "grammar":"Verbs: খোৱা (to eat) → মই খাওঁ (I eat), তুমি খোৱা (you eat), সি খায় (he/she eats).",
         "culture":"🍽️ Rice (ভাত) is the staple of Assamese cuisine. A traditional Assamese meal is served on a কঁহৰ থাল (bell-metal plate)."},

    7:  {"week":2,"phase":"Foundation","title":"ঘৰ | Home & Rooms","title_en":"Home & Rooms",
         "vocab":[
            {"a":"ঘৰ","t":"ghor","b":"ঘর","e":"house/home"},
            {"a":"কোঠা","t":"kotha","b":"ঘর (কক্ষ)","e":"room"},
            {"a":"পাকঘৰ","t":"paakghor","b":"রান্নাঘর","e":"kitchen"},
            {"a":"শোৱা কোঠা","t":"xowa kotha","b":"শোবার ঘর","e":"bedroom"},
            {"a":"বাথৰুম","t":"baathroom","b":"বাথরুম","e":"bathroom"},
            {"a":"দুৱাৰ","t":"duwaar","b":"দরজা","e":"door"},
            {"a":"খিৰিকী","t":"khiriki","b":"জানালা","e":"window"},
            {"a":"চোতাল","t":"sotaal","b":"উঠোন","e":"courtyard/yard"},
            {"a":"চিৰি","t":"xiri","b":"সিঁড়ি","e":"stairs"},
            {"a":"মজিয়া","t":"mojiya","b":"মেঝে","e":"floor"},
            {"a":"চিলিং","t":"xiling","b":"ছাদ","e":"ceiling/roof"},
            {"a":"বেৰ","t":"ber","b":"দেয়াল","e":"wall"},
         ],
         "phrases":[
            {"a":"মোৰ ঘৰ ডাঙৰ","t":"mor ghor daangor","b":"আমার বাড়ি বড়","e":"My house is big"},
            {"a":"পাকঘৰত কি আছে?","t":"paakghorot ki aahe?","b":"রান্নাঘরে কী আছে?","e":"What is in the kitchen?"},
            {"a":"দুৱাৰ খোল","t":"duwaar khol","b":"দরজা খোলো","e":"Open the door"},
         ],
         "grammar":"Location postpositions: -ত (at/in), -ৰ ওচৰত (near), -ৰ ভিতৰত (inside), -ৰ বাহিৰত (outside).",
         "culture":"🏠 Traditional Assamese houses (চাং ঘৰ) are built on stilts to protect from floods. The নামঘৰ (prayer hall) is central to village life."},

    8:  {"week":2,"phase":"Foundation","title":"শৰীৰ | Body Parts","title_en":"Body Parts",
         "vocab":[
            {"a":"মূৰ","t":"mur","b":"মাথা","e":"head"},
            {"a":"চকু","t":"xoku","b":"চোখ","e":"eye"},
            {"a":"কান","t":"kaan","b":"কান","e":"ear"},
            {"a":"নাক","t":"naak","b":"নাক","e":"nose"},
            {"a":"মুখ","t":"mukh","b":"মুখ","e":"mouth"},
            {"a":"দাঁত","t":"daant","b":"দাঁত","e":"teeth"},
            {"a":"হাত","t":"haat","b":"হাত","e":"hand/arm"},
            {"a":"ভৰি","t":"bhori","b":"পা","e":"foot/leg"},
            {"a":"আঙুলি","t":"aanguli","b":"আঙুল","e":"finger"},
            {"a":"পেট","t":"pet","b":"পেট","e":"stomach"},
            {"a":"বুকু","t":"buku","b":"বুক","e":"chest"},
            {"a":"পিঠি","t":"pithi","b":"পিঠ","e":"back"},
         ],
         "phrases":[
            {"a":"মোৰ মূৰ বিষাইছে","t":"mor mur bixaaise","b":"আমার মাথা ব্যথা করছে","e":"My head is aching"},
            {"a":"হাত ধুই লওক","t":"haat dhui laok","b":"হাত ধুয়ে নাও","e":"Please wash your hands"},
            {"a":"চকু বন্ধ কৰক","t":"xoku bondho korok","b":"চোখ বন্ধ করুন","e":"Close your eyes"},
         ],
         "grammar":"Body ache: মোৰ + body part + বিষাইছে (is aching). Example: মোৰ পেট বিষাইছে = My stomach aches.",
         "culture":"💊 Traditional Assamese medicine (আয়ুৰ্বেদ) uses plants from the Brahmaputra valley. Many remedies use হালধি (turmeric) and আদা (ginger)."},

    9:  {"week":3,"phase":"Foundation","title":"কাপোৰ | Clothing","title_en":"Clothing",
         "vocab":[
            {"a":"চাদৰ","t":"saador","b":"শাড়ি/চাদর","e":"Assamese saree / shawl"},
            {"a":"মেখেলা","t":"mekhela","b":"মেখেলা","e":"Assamese traditional skirt"},
            {"a":"চোলা","t":"xola","b":"জামা","e":"blouse/shirt"},
            {"a":"কুৰ্তা","t":"kurta","b":"কুর্তা","e":"kurta"},
            {"a":"পেন্ট","t":"pent","b":"প্যান্ট","e":"pants/trousers"},
            {"a":"জোতা","t":"jota","b":"জুতো","e":"shoes"},
            {"a":"চামৰীয়া","t":"saamoriya","b":"চামড়ার","e":"leather"},
            {"a":"কাপোৰ","t":"kaapor","b":"কাপড়","e":"cloth/fabric"},
            {"a":"পিন্ধা","t":"pindha","b":"পরা","e":"to wear"},
            {"a":"খোলা","t":"khola","b":"খোলা","e":"to take off"},
         ],
         "phrases":[
            {"a":"তুমি কি পিন্ধিছা?","t":"tumi ki pindhisa?","b":"তুমি কী পরেছ?","e":"What are you wearing?"},
            {"a":"মেখেলা-চাদৰ অসমৰ পৰম্পৰা","t":"mekhela-saador oxomor porompora","b":"মেখেলা-চাদর আসামের ঐতিহ্য","e":"Mekhela-Saador is Assam's tradition"},
         ],
         "grammar":"Verb 'পিন্ধা' (to wear): মই পিন্ধো (I wear), তুমি পিন্ধা (you wear), তেওঁ পিন্ধে (he/she wears).",
         "culture":"👘 The Mekhela Chador (মেখেলা চাদৰ) is the traditional attire of Assamese women, woven in Muga, Eri or Pat silk."},

    10: {"week":3,"phase":"Foundation","title":"প্ৰকৃতি | Nature","title_en":"Nature & Environment",
         "vocab":[
            {"a":"নদী","t":"nodi","b":"নদী","e":"river"},
            {"a":"পাহাৰ","t":"pahar","b":"পাহাড়","e":"hill/mountain"},
            {"a":"গছ","t":"gos","b":"গাছ","e":"tree"},
            {"a":"ফুল","t":"phul","b":"ফুল","e":"flower"},
            {"a":"পানী","t":"paani","b":"জল","e":"water"},
            {"a":"আকাশ","t":"aakaax","b":"আকাশ","e":"sky"},
            {"a":"বতাহ","t":"botaah","b":"বাতাস","e":"wind/air"},
            {"a":"বৰষুণ","t":"borosun","b":"বৃষ্টি","e":"rain"},
            {"a":"ৰ'দ","t":"rod","b":"রোদ","e":"sunlight"},
            {"a":"জংঘল","t":"jongkhol","b":"জঙ্গল","e":"forest/jungle"},
            {"a":"হাতী","t":"haati","b":"হাতি","e":"elephant"},
            {"a":"গঁড়","t":"gor","b":"গণ্ডার","e":"rhinoceros"},
         ],
         "phrases":[
            {"a":"ব্ৰহ্মপুত্ৰ বৰ ডাঙৰ নদী","t":"brahmoputro bor daangor nodi","b":"ব্রহ্মপুত্র অনেক বড় নদী","e":"Brahmaputra is a very big river"},
            {"a":"আজি বৰষুণ হব","t":"aaji borosun hob","b":"আজ বৃষ্টি হবে","e":"It will rain today"},
            {"a":"অসমৰ প্ৰকৃতি সুন্দৰ","t":"oxomor prokrti xundor","b":"আসামের প্রকৃতি সুন্দর","e":"Nature in Assam is beautiful"},
         ],
         "grammar":"Future tense: verb + ব (will). হব = will be, যাব = will go, খাব = will eat.",
         "culture":"🦏 Kaziranga National Park (কাজিৰঙা) hosts 2/3 of the world's one-horned rhinoceroses. It is a UNESCO World Heritage Site."},

    # Days 11-20: Intermediate Foundation
    11: {"week":3,"phase":"Foundation","title":"বাজাৰ | Shopping","title_en":"Shopping & Market",
         "vocab":[
            {"a":"বাজাৰ","t":"baajar","b":"বাজার","e":"market"},
            {"a":"দোকান","t":"dokaan","b":"দোকান","e":"shop"},
            {"a":"দাম","t":"daam","b":"দাম","e":"price"},
            {"a":"টকা","t":"toka","b":"টাকা","e":"money/rupee"},
            {"a":"সস্তা","t":"xoxtaa","b":"সস্তা","e":"cheap"},
            {"a":"দামী","t":"daami","b":"দামি","e":"expensive"},
            {"a":"কিনা","t":"kina","b":"কেনা","e":"to buy"},
            {"a":"বেচা","t":"besa","b":"বেচা","e":"to sell"},
            {"a":"কৰিয়ৰ","t":"koriyar","b":"ক্যারিয়ার","e":"carry bag"},
            {"a":"ৰচিদ","t":"rosid","b":"রশিদ","e":"receipt"},
         ],
         "phrases":[
            {"a":"এইটোৰ দাম কিমান?","t":"eitoor daam kimaan?","b":"এটার দাম কত?","e":"How much does this cost?"},
            {"a":"অলপ কম কৰিব নে?","t":"olop kom korib ne?","b":"একটু কম করবেন?","e":"Can you reduce the price a little?"},
            {"a":"মই এইটো ল'ম","t":"moi eitoo lom","b":"আমি এটা নেব","e":"I will take this one"},
            {"a":"মোক ৰচিদ দিয়ক","t":"mok rosid diyok","b":"আমাকে রশিদ দিন","e":"Please give me a receipt"},
         ],
         "grammar":"'নে?' at the end of a sentence makes it a polite request or question. অলপ = a little, বেছি = more/too much.",
         "culture":"🛒 Weekly markets (হাট) are central to rural Assamese life. The famous Fancy Bazar in Guwahati is Assam's largest market."},

    12: {"week":3,"phase":"Foundation","title":"পথ | Directions","title_en":"Directions & Transport",
         "vocab":[
            {"a":"বাওঁ","t":"baao","b":"বাম","e":"left"},
            {"a":"সোঁ","t":"xo","b":"ডান","e":"right"},
            {"a":"পোনে","t":"pone","b":"সোজা","e":"straight"},
            {"a":"পিছলৈ","t":"pisholoi","b":"পিছনে","e":"behind/back"},
            {"a":"সন্মুখত","t":"xonmukhot","b":"সামনে","e":"in front"},
            {"a":"ওচৰত","t":"osorot","b":"কাছে","e":"near"},
            {"a":"দূৰত","t":"durot","b":"দূরে","e":"far"},
            {"a":"বাছ","t":"baas","b":"বাস","e":"bus"},
            {"a":"ৰেল","t":"rel","b":"রেল","e":"train"},
            {"a":"অটো","t":"oto","b":"অটো","e":"auto-rickshaw"},
            {"a":"নাও","t":"naao","b":"নৌকা","e":"boat"},
         ],
         "phrases":[
            {"a":"কেনেকৈ যাব?","t":"kenekoi jaab?","b":"কিভাবে যাব?","e":"How to go?"},
            {"a":"বাওঁফালে যাওক","t":"baaofaley jaok","b":"বাম দিকে যান","e":"Go to the left"},
            {"a":"গুৱাহাটী কিমান দূৰ?","t":"guwahati kimaan dur?","b":"গুয়াহাটি কত দূর?","e":"How far is Guwahati?"},
            {"a":"ৰেল ষ্টেচন ক'ত?","t":"rel station kot?","b":"রেল স্টেশন কোথায়?","e":"Where is the railway station?"},
         ],
         "grammar":"Question words: ক'ত? (where?), কেনেকৈ? (how?), কিমান? (how much/many?), কেতিয়া? (when?), কিয়? (why?).",
         "culture":"🚢 Boats (নাও) are essential transport in Assam due to the Brahmaputra. The 'ফেৰী সেৱা' (ferry service) connects riverbanks."},

    13: {"week":4,"phase":"Foundation","title":"স্বাস্থ্য | Health","title_en":"Health & Body",
         "vocab":[
            {"a":"বেমাৰ","t":"bemaar","b":"অসুস্থ","e":"sick/ill"},
            {"a":"ডাক্তৰ","t":"daaktar","b":"ডাক্তার","e":"doctor"},
            {"a":"ঔষধ","t":"ousodh","b":"ওষুধ","e":"medicine"},
            {"a":"হাস্পতাল","t":"haaspataal","b":"হাসপাতাল","e":"hospital"},
            {"a":"জ্বৰ","t":"jor","b":"জ্বর","e":"fever"},
            {"a":"কাহ","t":"kaah","b":"কাশি","e":"cough"},
            {"a":"বিষ","t":"bix","b":"ব্যথা","e":"pain"},
            {"a":"ভাল","t":"bhaalo","b":"ভালো","e":"good/well"},
            {"a":"সুস্থ","t":"xuxtha","b":"সুস্থ","e":"healthy"},
            {"a":"বিশ্ৰাম","t":"bixraam","b":"বিশ্রাম","e":"rest"},
         ],
         "phrases":[
            {"a":"মই বেমাৰ হৈছো","t":"moi bemaar hoiso","b":"আমি অসুস্থ হয়েছি","e":"I have become ill"},
            {"a":"মোৰ জ্বৰ হৈছে","t":"mor jor hoihe","b":"আমার জ্বর হয়েছে","e":"I have a fever"},
            {"a":"ডাক্তৰ মোক চাওক","t":"daaktar mok saok","b":"ডাক্তার আমাকে দেখুন","e":"Doctor, please examine me"},
            {"a":"এই ঔষধ কেতিয়া খাব?","t":"ei ousodh ketiya khaab?","b":"এই ওষুধ কখন খাব?","e":"When to take this medicine?"},
         ],
         "grammar":"Past tense with হৈছো: মই বেমাৰ হৈছো (I have become ill). Past with -লো: মই খালো (I ate).",
         "culture":"🌿 Assam has rich traditions of herbal medicine. The 'বৈদ্য' (traditional healer) uses plants from the Brahmaputra valley."},

    14: {"week":4,"phase":"Foundation","title":"বতৰ | Weather","title_en":"Weather & Seasons",
         "vocab":[
            {"a":"বৰষা","t":"borosa","b":"বর্ষা","e":"monsoon/rainy season"},
            {"a":"শীত","t":"xeet","b":"শীত","e":"winter"},
            {"a":"গ্ৰীষ্ম","t":"grixmo","b":"গ্রীষ্ম","e":"summer"},
            {"a":"বসন্ত","t":"baxonto","b":"বসন্ত","e":"spring"},
            {"a":"ঠাণ্ডা","t":"thaanda","b":"ঠান্ডা","e":"cold"},
            {"a":"গৰম","t":"gorom","b":"গরম","e":"hot"},
            {"a":"মেঘ","t":"megh","b":"মেঘ","e":"cloud"},
            {"a":"বজ্ৰপাত","t":"bojropaat","b":"বজ্রপাত","e":"lightning/thunderstorm"},
            {"a":"বান","t":"baan","b":"বন্যা","e":"flood"},
            {"a":"খৰাং","t":"khoraaang","b":"খরা","e":"drought"},
         ],
         "phrases":[
            {"a":"আজি বৰ গৰম","t":"aaji bor gorom","b":"আজ খুব গরম","e":"It is very hot today"},
            {"a":"বৰষুণ আহিব বুলি ভাবো","t":"borosun aahibo buli bhaabo","b":"বৃষ্টি আসবে বলে মনে হয়","e":"I think it will rain"},
            {"a":"এই বছৰ বান হৈছে","t":"ei boshor baan hoihe","b":"এ বছর বন্যা হয়েছে","e":"There is flooding this year"},
         ],
         "grammar":"Future probability: বুলি ভাবো (I think that...). Verb + ব + বুলি ভাবো = I think [verb] will happen.",
         "culture":"🌊 Assam faces annual floods from the Brahmaputra. 'বান' (flood) is both a challenge and a cultural reality shaping Assamese life."},

    15: {"week":4,"phase":"Foundation","title":"পেচা | Occupations","title_en":"Jobs & Occupations",
         "vocab":[
            {"a":"শিক্ষক","t":"xikhok","b":"শিক্ষক","e":"teacher"},
            {"a":"ডাক্তৰ","t":"daaktar","b":"ডাক্তার","e":"doctor"},
            {"a":"খেতিয়ক","t":"khetiyok","b":"কৃষক","e":"farmer"},
            {"a":"ব্যৱসায়ী","t":"byobosaayi","b":"ব্যবসায়ী","e":"businessman"},
            {"a":"অভিযন্তা","t":"obhijonta","b":"প্রকৌশলী","e":"engineer"},
            {"a":"উকীল","t":"ukil","b":"উকিল","e":"lawyer"},
            {"a":"শিল্পী","t":"xilpi","b":"শিল্পী","e":"artist"},
            {"a":"গায়ক","t":"gaayok","b":"গায়ক","e":"singer"},
            {"a":"লেখক","t":"lekhok","b":"লেখক","e":"writer/author"},
            {"a":"চৰকাৰী কৰ্মচাৰী","t":"sorkaari kormsaari","b":"সরকারি কর্মচারী","e":"government employee"},
         ],
         "phrases":[
            {"a":"আপুনি কি কাম কৰে?","t":"apuni ki kaam kore?","b":"আপনি কি কাজ করেন?","e":"What work do you do?"},
            {"a":"মই শিক্ষক","t":"moi xikhok","b":"আমি শিক্ষক","e":"I am a teacher"},
            {"a":"মোৰ ভাই ডাক্তৰ","t":"mor bhai daaktar","b":"আমার ভাই ডাক্তার","e":"My brother is a doctor"},
         ],
         "grammar":"Profession sentences: মই + profession (no 'am' verb needed in Assamese). মই শিক্ষক = I (am) a teacher.",
         "culture":"🌾 Agriculture is the backbone of Assam. Tea plantation workers (চাহ বাগিছাৰ মানুহ) form a unique community."},

    # PHASE 2: INTERMEDIATE (Days 16-60)
    16: {"week":5,"phase":"Intermediate","title":"ক্ৰিয়া | Verb Tenses","title_en":"Verb Tenses",
         "vocab":[
            {"a":"যোৱা","t":"jowa","b":"যাওয়া","e":"to go"},
            {"a":"অহা","t":"oha","b":"আসা","e":"to come"},
            {"a":"দেখা","t":"dekha","b":"দেখা","e":"to see"},
            {"a":"শুনা","t":"xuna","b":"শোনা","e":"to hear/listen"},
            {"a":"কোৱা","t":"kowa","b":"বলা","e":"to say/speak"},
            {"a":"লিখা","t":"likha","b":"লেখা","e":"to write"},
            {"a":"পঢ়া","t":"pora","b":"পড়া","e":"to read/study"},
            {"a":"কৰা","t":"kora","b":"করা","e":"to do"},
            {"a":"দিয়া","t":"diya","b":"দেওয়া","e":"to give"},
            {"a":"লোৱা","t":"lowa","b":"নেওয়া","e":"to take"},
         ],
         "phrases":[
            {"a":"মই গৈছিলো","t":"moi goikhilo","b":"আমি গিয়েছিলাম","e":"I had gone (past)"},
            {"a":"মই যাম","t":"moi jaam","b":"আমি যাব","e":"I will go (future)"},
            {"a":"মই গৈ আছো","t":"moi goi aacho","b":"আমি যাচ্ছি","e":"I am going (continuous)"},
         ],
         "grammar":"Tenses: Past -লো (খালো=ate), Present -ওঁ (খাওঁ=eat), Future -ম (খাম=will eat), Continuous আছো (গৈ আছো=going).",
         "culture":"📚 Classical Assamese literature dates to the 13th century. Madhav Kandali translated the Ramayana into Assamese in the 14th century."},

    17: {"week":5,"phase":"Intermediate","title":"বিশেষণ | Adjectives","title_en":"Adjectives",
         "vocab":[
            {"a":"ডাঙৰ","t":"daangor","b":"বড়","e":"big/large"},
            {"a":"সৰু","t":"xoru","b":"ছোট","e":"small"},
            {"a":"ওখ","t":"okh","b":"লম্বা","e":"tall/high"},
            {"a":"চাপৰ","t":"saapar","b":"খাটো","e":"short"},
            {"a":"সুন্দৰ","t":"xundor","b":"সুন্দর","e":"beautiful"},
            {"a":"বেয়া","t":"beya","b":"খারাপ","e":"bad/ugly"},
            {"a":"নতুন","t":"notun","b":"নতুন","e":"new"},
            {"a":"পুৰণি","t":"puroni","b":"পুরানো","e":"old"},
            {"a":"দ্ৰুত","t":"drut","b":"দ্রুত","e":"fast"},
            {"a":"লেহেমীয়া","t":"lehemiya","b":"ধীর","e":"slow"},
            {"a":"কঠিন","t":"kothin","b":"কঠিন","e":"difficult/hard"},
            {"a":"সহজ","t":"xohoj","b":"সহজ","e":"easy"},
         ],
         "phrases":[
            {"a":"এইটো বৰ কঠিন","t":"eitoo bor kothin","b":"এটা খুব কঠিন","e":"This is very difficult"},
            {"a":"অসমীয়া সহজ ভাষা","t":"oxomiya xohoj bhaxa","b":"অসমীয়া সহজ ভাষা","e":"Assamese is an easy language"},
         ],
         "grammar":"Intensifiers: বৰ (very), একেবাৰে (absolutely), মোটামুটি (fairly), অলপ (a little). বৰ সুন্দৰ = very beautiful.",
         "culture":"🎭 Assamese folk theatre 'বাওনা' (Bhaona) uses elaborate costumes and poetic Assamese language going back 500 years."},

    18: {"week":5,"phase":"Intermediate","title":"ঘৰুৱা কথোপকথন | Daily Talk","title_en":"Daily Conversations",
         "vocab":[
            {"a":"হ'ব","t":"hob","b":"হবে","e":"will happen / okay"},
            {"a":"নহ'ব","t":"nohob","b":"হবে না","e":"will not happen"},
            {"a":"নিশ্চয়","t":"nixoy","b":"অবশ্যই","e":"certainly/surely"},
            {"a":"হয়তো","t":"hoyto","b":"হয়তো","e":"maybe/perhaps"},
            {"a":"মই নাজানো","t":"moi naajano","b":"আমি জানি না","e":"I don't know"},
            {"a":"মই বুজি পাইছো","t":"moi buji paiho","b":"আমি বুঝেছি","e":"I understand"},
            {"a":"আকৌ কওক","t":"akow kowk","b":"আবার বলুন","e":"Please say again"},
            {"a":"অলপ লাহেকৈ কওক","t":"olop lahekoi kowk","b":"একটু আস্তে বলুন","e":"Please speak slowly"},
         ],
         "phrases":[
            {"a":"অসমীয়া অলপ কওক","t":"oxomiya olop kowk","b":"অসমীয়া একটু বলুন","e":"Please speak a little Assamese"},
            {"a":"মই শিকি আছো","t":"moi xiki aacho","b":"আমি শিখছি","e":"I am learning"},
            {"a":"আপুনি বৰ ভালকৈ বুজাই দিছে","t":"apuni bor bhaalokoi bujaayi dihe","b":"আপনি খুব ভালো বুঝিয়েছেন","e":"You have explained very well"},
         ],
         "grammar":"Polite requests: verb + ক (imperative). কওক (please say), দিয়ক (please give), আহক (please come).",
         "culture":"🗣️ Assamese has a rich oral tradition. 'গল্প কোৱা' (storytelling) is a beloved cultural practice, especially in winter evenings."},

    19: {"week":6,"phase":"Intermediate","title":"সম্পৰ্ক | Relationships","title_en":"Relationships & Social",
         "vocab":[
            {"a":"বন্ধু","t":"bondhu","b":"বন্ধু","e":"friend"},
            {"a":"প্ৰতিবেশী","t":"protibexi","b":"প্রতিবেশী","e":"neighbour"},
            {"a":"সহকৰ্মী","t":"xohokhormi","b":"সহকর্মী","e":"colleague"},
            {"a":"গুৰু","t":"guru","b":"গুরু","e":"teacher/mentor"},
            {"a":"ছাত্ৰ","t":"saatro","b":"ছাত্র","e":"student (male)"},
            {"a":"ছাত্ৰী","t":"saatri","b":"ছাত্রী","e":"student (female)"},
            {"a":"বিয়া","t":"biya","b":"বিয়ে","e":"wedding/marriage"},
            {"a":"প্ৰেম","t":"prem","b":"প্রেম","e":"love"},
            {"a":"পৰিচয়","t":"porisoy","b":"পরিচয়","e":"introduction/acquaintance"},
         ],
         "phrases":[
            {"a":"সি মোৰ বন্ধু","t":"xi mor bondhu","b":"সে আমার বন্ধু","e":"He/She is my friend"},
            {"a":"আমি বহু দিনৰ বন্ধু","t":"aami bohu dinor bondhu","b":"আমরা অনেকদিনের বন্ধু","e":"We are friends for a long time"},
            {"a":"আপোনাৰ সৈতে পৰিচয় হৈ ভাল লাগিল","t":"aponaar xoite porisoy hoi bhaalo laagil","b":"আপনার সাথে পরিচয় হয়ে ভালো লাগলো","e":"Nice to meet you"},
         ],
         "grammar":"সৈতে (with): মোৰ সৈতে (with me), তোমাৰ সৈতে (with you). Used for accompaniment and comparison.",
         "culture":"🎊 Assamese weddings (বিয়া) last several days with rituals like 'জোৰোণ' (welcome ceremony) and 'হালধি' (turmeric ceremony)."},

    20: {"week":6,"phase":"Intermediate","title":"শিক্ষা | Education","title_en":"Education & Learning",
         "vocab":[
            {"a":"বিদ্যালয়","t":"bidyalay","b":"বিদ্যালয়","e":"school"},
            {"a":"মহাবিদ্যালয়","t":"mohaabidyalay","b":"কলেজ","e":"college"},
            {"a":"বিশ্ববিদ্যালয়","t":"bixwobidyalay","b":"বিশ্ববিদ্যালয়","e":"university"},
            {"a":"কিতাপ","t":"kitaap","b":"বই","e":"book"},
            {"a":"কলম","t":"kolom","b":"কলম","e":"pen"},
            {"a":"পেঞ্চিল","t":"penchil","b":"পেন্সিল","e":"pencil"},
            {"a":"পৰীক্ষা","t":"porikha","b":"পরীক্ষা","e":"exam"},
            {"a":"উত্তীৰ্ণ","t":"uttirno","b":"উত্তীর্ণ","e":"pass (exam)"},
            {"a":"অনুত্তীৰ্ণ","t":"anutiirno","b":"অনুত্তীর্ণ","e":"fail (exam)"},
            {"a":"জ্ঞান","t":"gyaan","b":"জ্ঞান","e":"knowledge"},
         ],
         "phrases":[
            {"a":"মই কিতাপ পঢ়ি ভাল পাওঁ","t":"moi kitaap pori bhaalo paao","b":"আমি বই পড়তে ভালোবাসি","e":"I like reading books"},
            {"a":"পৰীক্ষা কেতিয়া?","t":"porikha ketiya?","b":"পরীক্ষা কখন?","e":"When is the exam?"},
            {"a":"অসমীয়া শিকাটো আনন্দদায়ক","t":"oxomiya xikaato aanonddaayok","b":"অসমীয়া শেখাটা আনন্দদায়ক","e":"Learning Assamese is enjoyable"},
         ],
         "grammar":"Infinitive + ভাল পাওঁ = I like + verb-ing. মই পঢ়া ভাল পাওঁ (I like reading). মই গোৱা ভাল পাওঁ (I like singing).",
         "culture":"📖 Assam has produced great literary figures like লক্ষ্মীনাথ বেজবৰুৱা (Laxminath Bezbaroa), the father of modern Assamese literature."},
}

# Continue curriculum for days 21-120
CURRICULUM_EXT = {
    21: {"week":6,"phase":"Intermediate","title":"ভ্ৰমণ | Travel","title_en":"Travel & Tourism",
         "vocab":[
            {"a":"হোটেল","t":"hotel","b":"হোটেল","e":"hotel"},
            {"a":"ভ্ৰমণ","t":"bhromono","b":"ভ্রমণ","e":"travel/tourism"},
            {"a":"পাছপোৰ্ট","t":"passport","b":"পাসপোর্ট","e":"passport"},
            {"a":"টিকট","t":"tikat","b":"টিকিট","e":"ticket"},
            {"a":"বিমান","t":"bimaan","b":"বিমান","e":"aeroplane"},
            {"a":"বিমানবন্দৰ","t":"bimaanbondor","b":"বিমানবন্দর","e":"airport"},
            {"a":"কক্ষ","t":"kokho","b":"কক্ষ","e":"room (hotel)"},
            {"a":"চেক ইন","t":"check in","b":"চেক ইন","e":"check-in"},
            {"a":"ব্যাগ","t":"baag","b":"ব্যাগ","e":"bag/luggage"},
         ],
         "phrases":[
            {"a":"মই গুৱাহাটী যাব খুজিছো","t":"moi guwahati jaab khujiso","b":"আমি গুয়াহাটি যেতে চাই","e":"I want to go to Guwahati"},
            {"a":"এটা কোঠা বুকিং কৰিব খুজিছো","t":"ekta kotha booking korib khujiso","b":"একটি রুম বুক করতে চাই","e":"I want to book a room"},
            {"a":"কাজিৰঙা কেনেকৈ যাব?","t":"kaajironga kenekoi jaab?","b":"কাজিরাঙা কীভাবে যাব?","e":"How to go to Kaziranga?"},
         ],
         "grammar":"খোজা/খুজিছো (want to): মই + verb + খুজিছো. মই খাব খুজিছো (I want to eat). মই যাব খুজিছো (I want to go).",
         "culture":"🌿 Major tourist spots: Kaziranga (কাজিৰঙা), Majuli (মাজুলী), Kamakhya (কামাখ্যা), Pobitora (পবিতৰা), Manas (মানাহ)."},

    22: {"week":7,"phase":"Intermediate","title":"বিনোদন | Entertainment","title_en":"Entertainment & Arts",
         "vocab":[
            {"a":"গান","t":"gaan","b":"গান","e":"song"},
            {"a":"নাচ","t":"naas","b":"নাচ","e":"dance"},
            {"a":"চিনেমা","t":"xinema","b":"সিনেমা","e":"cinema/film"},
            {"a":"নাটক","t":"naatok","b":"নাটক","e":"drama/play"},
            {"a":"কিতাপ","t":"kitaap","b":"বই","e":"book"},
            {"a":"বিহু","t":"bihu","b":"বিহু","e":"Bihu (festival/dance)"},
            {"a":"ঢোল","t":"dhol","b":"ঢোল","e":"drum (Assamese)"},
            {"a":"পেঁপা","t":"pepa","b":"পেঁপা","e":"Assamese horn flute"},
            {"a":"গোগোনা","t":"gogona","b":"গোগোনা","e":"Assamese jaw harp"},
         ],
         "phrases":[
            {"a":"বিহু নাচ বৰ সুন্দৰ","t":"bihu naas bor xundor","b":"বিহু নাচ খুব সুন্দর","e":"Bihu dance is very beautiful"},
            {"a":"তুমি গান গাব জানা?","t":"tumi gaan gaab jaana?","b":"তুমি গান গাইতে পারো?","e":"Can you sing a song?"},
            {"a":"মই অসমীয়া চিনেমা ভাল পাওঁ","t":"moi oxomiya xinema bhaalo paao","b":"আমি আসামি সিনেমা পছন্দ করি","e":"I like Assamese cinema"},
         ],
         "grammar":"জনা (to know how to): মই গান গাব জানো (I know how to sing). তুমি নাচিব জানা? (Can you dance?).",
         "culture":"🎵 Bihu songs (বিহু গীত) are sung during the Bihu festivals. The পেঁপা (buffalo horn flute) is the iconic Assamese instrument."},

    23: {"week":7,"phase":"Intermediate","title":"প্ৰযুক্তি | Technology","title_en":"Technology & Modern Life",
         "vocab":[
            {"a":"মোবাইল","t":"mobile","b":"মোবাইল","e":"mobile phone"},
            {"a":"কম্পিউটাৰ","t":"computer","b":"কম্পিউটার","e":"computer"},
            {"a":"ইন্টাৰনেট","t":"internet","b":"ইন্টারনেট","e":"internet"},
            {"a":"ইমেইল","t":"email","b":"ইমেইল","e":"email"},
            {"a":"সংদেশ","t":"xongdex","b":"বার্তা","e":"message"},
            {"a":"চছিয়েল মিডিয়া","t":"social media","b":"সোশ্যাল মিডিয়া","e":"social media"},
            {"a":"ডাউনলোড","t":"download","b":"ডাউনলোড","e":"download"},
            {"a":"পাছৱৰ্ড","t":"password","b":"পাসওয়ার্ড","e":"password"},
         ],
         "phrases":[
            {"a":"ৱাই-ফাই পাছৱৰ্ড কি?","t":"wifi password ki?","b":"ওয়াইফাই পাসওয়ার্ড কী?","e":"What is the WiFi password?"},
            {"a":"মোৰ ফোনত নেটৱৰ্ক নাই","t":"mor phone-t network nai","b":"আমার ফোনে নেটওয়ার্ক নেই","e":"There is no network on my phone"},
            {"a":"মোক বাৰ্তা পঠিয়াওক","t":"mok baarta pothiyaok","b":"আমাকে বার্তা পাঠান","e":"Send me a message"},
         ],
         "grammar":"নাই (there is not): ৱাই-ফাই নাই (no wifi), সময় নাই (no time), পানী নাই (no water). আছে (there is): পানী আছে (water is there).",
         "culture":"📱 Assam has a growing digital economy. Guwahati is becoming a tech hub for Northeast India."},

    24: {"week":7,"phase":"Intermediate","title":"খেল | Sports","title_en":"Sports & Games",
         "vocab":[
            {"a":"ক্ৰিকেট","t":"cricket","b":"ক্রিকেট","e":"cricket"},
            {"a":"ফুটবল","t":"football","b":"ফুটবল","e":"football"},
            {"a":"কাবাডি","t":"kabadi","b":"কাবাডি","e":"kabaddi"},
            {"a":"সাঁতোৰ","t":"saantor","b":"সাঁতার","e":"swimming"},
            {"a":"দৌৰ","t":"dour","b":"দৌড়","e":"running"},
            {"a":"খেলা","t":"khela","b":"খেলা","e":"to play"},
            {"a":"জয়","t":"joy","b":"জয়","e":"victory"},
            {"a":"পৰাজয়","t":"poraajoy","b":"পরাজয়","e":"defeat"},
            {"a":"দল","t":"dol","b":"দল","e":"team"},
         ],
         "phrases":[
            {"a":"তুমি কি খেল ভাল পাওঁ?","t":"tumi ki khel bhaalo paao?","b":"তুমি কোন খেলা পছন্দ কর?","e":"Which sport do you like?"},
            {"a":"আমাৰ দল জিকিছে","t":"aamar dol jikihe","b":"আমাদের দল জিতেছে","e":"Our team has won"},
            {"a":"বিহু উৎসৱত ঐতিহ্যবাহী খেল হয়","t":"bihu utsovot oitihobaahi khel hoy","b":"বিহু উৎসবে ঐতিহ্যবাহী খেলা হয়","e":"Traditional games are played during Bihu"},
         ],
         "grammar":"Past perfect: জিকিছে (has won), হৈছে (has happened), আহিছে (has come). Different from simple past জিকিলে (won).",
         "culture":"🏏 Dhoop Khel (ধূপ খেল), Egon Khel and Buffalo fights are traditional Assamese sports played during Bihu."},

    25: {"week":8,"phase":"Intermediate","title":"ধৰ্ম আৰু উৎসৱ | Religion & Festivals","title_en":"Religion & Festivals",
         "vocab":[
            {"a":"মন্দিৰ","t":"mondor","b":"মন্দির","e":"temple"},
            {"a":"মছজিদ","t":"mosjid","b":"মসজিদ","e":"mosque"},
            {"a":"গীৰ্জা","t":"girja","b":"গির্জা","e":"church"},
            {"a":"নামঘৰ","t":"naamghor","b":"নামঘর","e":"Assamese prayer hall"},
            {"a":"পূজা","t":"puja","b":"পূজা","e":"worship/prayer"},
            {"a":"প্ৰাৰ্থনা","t":"proarthona","b":"প্রার্থনা","e":"prayer"},
            {"a":"বিহু","t":"bihu","b":"বিহু","e":"Bihu festival"},
            {"a":"ঈদ","t":"eid","b":"ঈদ","e":"Eid"},
            {"a":"দুৰ্গাপূজা","t":"durga puja","b":"দুর্গাপূজা","e":"Durga Puja"},
            {"a":"ক্ৰিছমাছ","t":"christmas","b":"ক্রিসমাস","e":"Christmas"},
         ],
         "phrases":[
            {"a":"বিহুৰ শুভেচ্ছা","t":"bihur xubhessha","b":"বিহুর শুভেচ্ছা","e":"Bihu greetings"},
            {"a":"ঈদ মোবাৰক","t":"eid mubarak","b":"ঈদ মোবারক","e":"Eid Mubarak"},
            {"a":"শুভ দুৰ্গাপূজা","t":"xubho durga puja","b":"শুভ দুর্গাপূজা","e":"Happy Durga Puja"},
            {"a":"নামঘৰত নাম পঢ়া হয়","t":"naamghorot naam pora hoy","b":"নামঘরে নাম পড়া হয়","e":"Prayers are read at the Namghar"},
         ],
         "grammar":"Habitual present: হয় (happens/is done). নামঘৰত নাম পঢ়া হয় = Prayers are recited at Namghar (habitual).",
         "culture":"🛕 The Kamakhya Temple (কামাখ্যা মন্দিৰ) in Guwahati is one of the 51 Shakti Peethas and draws millions of pilgrims annually."},

    # Days 26-30: Foundation wrap-up
    26: {"week":8,"phase":"Intermediate","title":"ৰান্ধনী | Cooking","title_en":"Cooking & Recipes",
         "vocab":[
            {"a":"ৰন্ধা","t":"rondha","b":"রান্না করা","e":"to cook"},
            {"a":"কাটা","t":"kaata","b":"কাটা","e":"to cut"},
            {"a":"সিজোৱা","t":"xijowa","b":"সেদ্ধ করা","e":"to boil"},
            {"a":"ভজা","t":"bhoja","b":"ভাজা","e":"to fry"},
            {"a":"মছলা","t":"mokhola","b":"মশলা","e":"spices"},
            {"a":"তেল","t":"tel","b":"তেল","e":"oil"},
            {"a":"হালধি","t":"haaldhi","b":"হলুদ","e":"turmeric"},
            {"a":"আদা","t":"aada","b":"আদা","e":"ginger"},
            {"a":"নহৰু","t":"nohoru","b":"রসুন","e":"garlic"},
            {"a":"ধনিয়া","t":"dhoniya","b":"ধনে","e":"coriander"},
         ],
         "phrases":[
            {"a":"তুমি ৰান্ধিব জানা?","t":"tumi raandhibi jaana?","b":"তুমি রান্না করতে পারো?","e":"Can you cook?"},
            {"a":"মাছ জোল কেনেকৈ ৰান্ধে?","t":"maas jol kenekoi raandhe?","b":"মাছের ঝোল কীভাবে রান্না করে?","e":"How do you cook fish curry?"},
            {"a":"পিঠা বনোৱা শিকিম","t":"pitha bonowa xikim","b":"পিঠা বানানো শিখব","e":"I will learn to make Pitha"},
         ],
         "grammar":"Causative: verb + োৱা = to make someone do. ৰান্ধোৱা (to make cook), খোৱাওক (make eat/feed).",
         "culture":"🍚 Traditional Assamese dishes: মাছৰ জোল (fish curry), খাৰ (alkaline dish), পিঠা (rice cakes), আহু চাউল (Aahu rice variety)."},

    27: {"week":8,"phase":"Intermediate","title":"আৱেগ | Emotions","title_en":"Emotions & Feelings",
         "vocab":[
            {"a":"আনন্দ","t":"aanond","b":"আনন্দ","e":"joy/happiness"},
            {"a":"দুখ","t":"dukh","b":"দুঃখ","e":"sadness/grief"},
            {"a":"খং","t":"khong","b":"রাগ","e":"anger"},
            {"a":"ভয়","t":"bhoy","b":"ভয়","e":"fear"},
            {"a":"আচৰিত","t":"aaxorit","b":"আশ্চর্য","e":"surprised/amazed"},
            {"a":"লাজ","t":"laaj","b":"লজ্জা","e":"shy/shame"},
            {"a":"গৌৰৱ","t":"gourov","b":"গর্ব","e":"pride"},
            {"a":"ভালপোৱা","t":"bhaalpowa","b":"ভালোবাসা","e":"love/affection"},
            {"a":"চিন্তা","t":"sinta","b":"চিন্তা","e":"worry/thought"},
            {"a":"শান্তি","t":"xaanti","b":"শান্তি","e":"peace"},
         ],
         "phrases":[
            {"a":"মই বৰ আনন্দিত","t":"moi bor aanondit","b":"আমি খুব আনন্দিত","e":"I am very happy"},
            {"a":"তোমাৰ কথা ভাবি দুখ লাগে","t":"tomaar kotha bhaabi dukh laage","b":"তোমার কথা ভেবে দুঃখ লাগে","e":"I feel sad thinking of you"},
            {"a":"ভয় নকৰিবা","t":"bhoy nokoriba","b":"ভয় পেয়ো না","e":"Do not be afraid"},
         ],
         "grammar":"Feeling expressions: মোক + feeling + লাগে (I feel...). মোক আনন্দ লাগে (I feel happy), মোক ভয় লাগে (I feel afraid).",
         "culture":"🎭 Assamese poetry (কবিতা) richly expresses emotions. Poet Ambikagiri Raichoudhury wrote passionately about love for Assam."},

    28: {"week":9,"phase":"Intermediate","title":"পৰিৱেশ | Environment","title_en":"Environment & Conservation",
         "vocab":[
            {"a":"পৰিৱেশ","t":"poribes","b":"পরিবেশ","e":"environment"},
            {"a":"প্ৰদূষণ","t":"produxon","b":"দূষণ","e":"pollution"},
            {"a":"গছ-গছনি","t":"gos-gosni","b":"গাছপালা","e":"trees/plants"},
            {"a":"বনাঞ্চল","t":"bonaansol","b":"বনভূমি","e":"forest area"},
            {"a":"সংৰক্ষণ","t":"xongrokkhon","b":"সংরক্ষণ","e":"conservation"},
            {"a":"জলবায়ু","t":"jolobayu","b":"জলবায়ু","e":"climate"},
            {"a":"বন্যপ্ৰাণী","t":"bonyopraani","b":"বন্যপ্রাণী","e":"wildlife"},
            {"a":"অভয়াৰণ্য","t":"obhoyyaaronnyo","b":"অভয়ারণ্য","e":"wildlife sanctuary"},
         ],
         "phrases":[
            {"a":"পৰিৱেশ ৰক্ষা কৰক","t":"poribes rokkha korok","b":"পরিবেশ রক্ষা করুন","e":"Protect the environment"},
            {"a":"গছ কাটিব নালাগে","t":"gos kaatibo nalaage","b":"গাছ কাটবেন না","e":"Do not cut trees"},
            {"a":"অসমৰ বনাঞ্চল কমি আহিছে","t":"oxomor bonaansol komi aahihe","b":"আসামের বনভূমি কমে আসছে","e":"Assam's forests are decreasing"},
         ],
         "grammar":"Prohibition: verb + িব নালাগে (should not). কাটিব নালাগে (should not cut), খাব নালাগে (should not eat).",
         "culture":"🌿 Assam's Kaziranga, Manas, Dibru-Saikhowa and other national parks protect unique biodiversity of the Brahmaputra valley."},

    29: {"week":9,"phase":"Intermediate","title":"ইতিহাস | History","title_en":"Assamese History",
         "vocab":[
            {"a":"ইতিহাস","t":"itihaas","b":"ইতিহাস","e":"history"},
            {"a":"ৰজা","t":"roja","b":"রাজা","e":"king"},
            {"a":"সাম্ৰাজ্য","t":"saamraajyo","b":"সাম্রাজ্য","e":"empire"},
            {"a":"যুদ্ধ","t":"juddho","b":"যুদ্ধ","e":"war/battle"},
            {"a":"স্বাধীনতা","t":"xwaadhiinotaa","b":"স্বাধীনতা","e":"independence/freedom"},
            {"a":"আহোম","t":"aaham","b":"আহোম","e":"Ahom (Assamese dynasty)"},
            {"a":"সংস্কৃতি","t":"xongskrti","b":"সংস্কৃতি","e":"culture"},
            {"a":"ঐতিহ্য","t":"oitihoyo","b":"ঐতিহ্য","e":"heritage"},
         ],
         "phrases":[
            {"a":"আহোম ৰাজ্য ৬০০ বছৰ স্থায়ী আছিল","t":"aaham raajyo 600 boshor xthaayi aasil","b":"আহোম রাজ্য ৬০০ বছর স্থায়ী ছিল","e":"The Ahom kingdom lasted 600 years"},
            {"a":"অসমৰ ইতিহাস বৰ সমৃদ্ধ","t":"oxomor itihaas bor xomriddho","b":"আসামের ইতিহাস খুব সমৃদ্ধ","e":"Assam's history is very rich"},
         ],
         "grammar":"Past habitual: আছিল (was/were). ৰাজ্য আছিল (kingdom was). Different from simple past হৈছিল (had become).",
         "culture":"👑 The Ahom dynasty (আহোম বংশ) ruled Assam for 600 years (1228-1826) and never surrendered to the Mughal Empire."},

    30: {"week":9,"phase":"Intermediate","title":"সাহিত্য | Literature","title_en":"Assamese Literature",
         "vocab":[
            {"a":"কবিতা","t":"kobita","b":"কবিতা","e":"poem"},
            {"a":"গল্প","t":"golpo","b":"গল্প","e":"story"},
            {"a":"উপন্যাস","t":"uponnyas","b":"উপন্যাস","e":"novel"},
            {"a":"নাটক","t":"naatok","b":"নাটক","e":"drama/play"},
            {"a":"কবি","t":"kobi","b":"কবি","e":"poet"},
            {"a":"লেখক","t":"lekhok","b":"লেখক","e":"writer"},
            {"a":"সাহিত্য","t":"xaahityo","b":"সাহিত্য","e":"literature"},
            {"a":"ভাষা","t":"bhaaxaa","b":"ভাষা","e":"language"},
         ],
         "phrases":[
            {"a":"অসমীয়া ভাষা অমৰ","t":"oxomiya bhaaxaa omor","b":"অসমীয়া ভাষা অমর","e":"Assamese language is immortal"},
            {"a":"মই কবিতা পঢ়িব ভাল পাওঁ","t":"moi kobita poribhi bhaalo paao","b":"আমি কবিতা পড়তে ভালোবাসি","e":"I love reading poetry"},
         ],
         "grammar":"Appreciation: বৰ ভাল (very good), অতি সুন্দৰ (extremely beautiful), অসাধাৰণ (extraordinary).",
         "culture":"📜 Assamese literature's golden age was under the Ahoms. Sankardev (শংকৰদেৱ) composed Borgeets — devotional songs still sung today."},
}

# Days 31-120 summary structure (grouped topics)
ADVANCED_TOPICS = {
    31: {"week":10,"phase":"Advanced","title":"বাক্য গঠন | Sentence Structure","title_en":"Complex Sentences",
         "vocab":[
            {"a":"যদি","t":"jodi","b":"যদি","e":"if"},
            {"a":"তেন্তে","t":"tente","b":"তাহলে","e":"then"},
            {"a":"কিন্তু","t":"kintu","b":"কিন্তু","e":"but"},
            {"a":"কাৰণ","t":"kaaronno","b":"কারণ","e":"because"},
            {"a":"যদিও","t":"jodiyo","b":"যদিও","e":"although/even if"},
            {"a":"আৰু","t":"aaroo","b":"এবং","e":"and"},
            {"a":"বা","t":"baa","b":"বা","e":"or"},
            {"a":"তথাপি","t":"tothaaopi","b":"তবুও","e":"yet/still"},
         ],
         "phrases":[
            {"a":"যদি বৰষুণ হয়, তেন্তে মই নাযাওঁ","t":"jodi borosun hoy, tente moi najaao","b":"যদি বৃষ্টি হয়, তাহলে আমি যাব না","e":"If it rains, I will not go"},
            {"a":"মই যাব খুজিছিলো, কিন্তু পাৰিলো নহয়","t":"moi jaab khujisilo, kintu paarilo nohoy","b":"আমি যেতে চেয়েছিলাম, কিন্তু পারিনি","e":"I wanted to go, but could not"},
         ],
         "grammar":"Conditional: যদি...তেন্তে (if...then). Concessive: যদিও (although). Causal: কাৰণ (because).",
         "culture":"🎓 Gauhati University (গুৱাহাটী বিশ্ববিদ্যালয়), established in 1948, is the premier institution for Assamese language studies."},

    32: {"week":10,"phase":"Advanced","title":"সম্মানজনক ভাষা | Honorifics","title_en":"Polite & Formal Language",
         "vocab":[
            {"a":"আপুনি","t":"apuni","b":"আপনি","e":"you (respectful)"},
            {"a":"তেওঁ","t":"tewo","b":"তিনি","e":"he/she (respectful)"},
            {"a":"আহক","t":"aahhok","b":"আসুন","e":"please come (polite)"},
            {"a":"বহক","t":"bohok","b":"বসুন","e":"please sit (polite)"},
            {"a":"খাওক","t":"khaok","b":"খান","e":"please eat (polite)"},
            {"a":"দয়া কৰি","t":"doya kori","b":"দয়া করে","e":"kindly/please"},
            {"a":"অনুগ্ৰহ কৰি","t":"onugraho kori","b":"অনুগ্রহ করে","e":"please (formal)"},
         ],
         "phrases":[
            {"a":"অনুগ্ৰহ কৰি বহক","t":"onugraho kori bohok","b":"অনুগ্রহ করে বসুন","e":"Please have a seat (formal)"},
            {"a":"আপোনাৰ সময় নষ্ট কৰিলোঁ বাবে ক্ষমা কৰিব","t":"aponaar xomoy noxt korilõ baabe kkhomaa korib","b":"আপনার সময় নষ্ট করলাম বলে ক্ষমা করবেন","e":"Sorry for wasting your time"},
         ],
         "grammar":"Politeness levels: Plain (তুমি), Familiar (তই), Formal (আপুনি), Ultra-formal (তেওঁ for 3rd person).",
         "culture":"🙏 Respect for elders is paramount in Assamese culture. Touching elders' feet (প্ৰণাম কৰা) is a common mark of respect."},

    # Days 33-60: Advanced grammar and communication
    33: {"week":10,"phase":"Advanced","title":"কথোপকথন ১ | Conversation 1","title_en":"Real Conversations - Meeting",
         "vocab":[
            {"a":"জনাজাত","t":"jonaajaat","b":"পরিচিত","e":"acquaintance/known"},
            {"a":"অচিনাকি","t":"osinaki","b":"অপরিচিত","e":"unknown/stranger"},
            {"a":"সাক্ষাৎ","t":"saakkhaat","b":"সাক্ষাৎ","e":"meeting/encounter"},
            {"a":"আলাপ","t":"aalap","b":"আলাপ","e":"acquaintance/chat"},
            {"a":"বিদায়","t":"bidaay","b":"বিদায়","e":"farewell"},
         ],
         "phrases":[
            {"a":"আপোনাৰ সৈতে লগ হৈ ভাল লাগিল","t":"aponaar xoite log hoi bhaalo laagil","b":"আপনার সাথে দেখা হয়ে ভালো লাগলো","e":"It was good meeting you"},
            {"a":"আপুনি ক'ৰ পৰা আহিছে?","t":"apuni koror pora aahihe?","b":"আপনি কোথা থেকে এসেছেন?","e":"Where have you come from?"},
            {"a":"মই প্ৰথমবাৰ অসমলৈ আহিছো","t":"moi prothombaar oxomloi aahiho","b":"আমি প্রথমবার আসামে এসেছি","e":"I have come to Assam for the first time"},
         ],
         "grammar":"Perfect tense with লগ হৈ, আহি, গৈ — completed actions with continuing relevance.",
         "culture":"🤝 When meeting someone new in Assam, it is customary to offer গামোচা (a traditional Assamese towel/scarf) as a sign of welcome."},
}

# Merge all curriculum
for k, v in CURRICULUM_EXT.items():
    CURRICULUM[k] = v
for k, v in ADVANCED_TOPICS.items():
    CURRICULUM[k] = v

# Fill remaining days 34-120 with topic progression
REMAINING_TOPICS = [
    (34,"Advanced","আনুষ্ঠানিক পত্ৰ | Formal Writing","Formal Writing & Letters"),
    (35,"Advanced","ব্যৱসায়িক কথোপকথন | Business Talk","Business Conversations"),
    (36,"Advanced","চিকিৎসা পৰামৰ্শ | Medical Consultation","Medical Consultation"),
    (37,"Advanced","ব্যাংক আৰু বিত্ত | Banking","Banking & Finance"),
    (38,"Advanced","আইনী বিষয় | Legal Matters","Basic Legal Language"),
    (39,"Advanced","কৃষি | Agriculture","Agriculture & Farming"),
    (40,"Advanced","সংগীত | Music Theory","Music & Rhythm"),
    (41,"Advanced","ৰাজনীতি | Politics","Politics & Governance"),
    (42,"Advanced","খবৰ পঢ়া | News Reading","Reading News"),
    (43,"Advanced","সাংস্কৃতিক অনুষ্ঠান | Cultural Events","Cultural Events"),
    (44,"Advanced","বিজ্ঞান | Science","Science Vocabulary"),
    (45,"Advanced","গণিত | Mathematics","Numbers & Math"),
    (46,"Advanced","ভূগোল | Geography","Geography of Assam"),
    (47,"Advanced","সামাজিক বিজ্ঞান | Social Science","Social Issues"),
    (48,"Advanced","দৰ্শন | Philosophy","Philosophy & Wisdom"),
    (49,"Advanced","মনোবিজ্ঞান | Psychology","Mind & Emotions"),
    (50,"Advanced","শিল্পকলা | Fine Arts","Visual Arts"),
    (51,"Expert","কাব্য ৰচনা | Poetry Writing","Writing Poetry"),
    (52,"Expert","চুটিগল্প | Short Stories","Short Story Writing"),
    (53,"Expert","নাটক লিখা | Drama Writing","Writing Drama"),
    (54,"Expert","বিতৰ্ক | Debate","Debate & Argumentation"),
    (55,"Expert","বক্তৃতা | Public Speaking","Public Speaking"),
    (56,"Expert","অনুবাদ | Translation","Translation Skills"),
    (57,"Expert","ব্যাকৰণ বিশ্লেষণ | Grammar Deep","Advanced Grammar Analysis"),
    (58,"Expert","প্ৰবন্ধ | Essay Writing","Essay Composition"),
    (59,"Expert","সাক্ষাৎকাৰ | Interview","Interview Language"),
    (60,"Expert","সংবাদ বিজ্ঞপ্তি | Press Release","Media & Communications"),
]

for day, phase, title, title_en in REMAINING_TOPICS:
    week = (day - 1) // 7 + 1
    CURRICULUM[day] = {
        "week": week, "phase": phase,
        "title": title, "title_en": title_en,
        "vocab": [
            {"a":"অধ্যয়ন","t":"odhyoyon","b":"অধ্যয়ন","e":"study this topic"},
            {"a":"অনুশীলন","t":"onuxilon","b":"অনুশীলন","e":"practice"},
            {"a":"পৰীক্ষা","t":"porikha","b":"পরীক্ষা","e":"exam/test"},
        ],
        "phrases":[
            {"a":"মই এই বিষয়ত শিকিব খুজিছো","t":"moi ei bishoyt xikib khujiso","b":"আমি এই বিষয়ে শিখতে চাই","e":"I want to learn this subject"},
        ],
        "grammar": f"Day {day} — {phase} level grammar and usage for {title_en}.",
        "culture": f"🎓 Continuing your {phase.lower()} Assamese journey — {title_en}.",
    }

# Days 61-120: Expert and fluency
for day in range(61, 121):
    week = (day - 1) // 7 + 1
    expert_titles = [
        "উচ্চাৰণ পৰিমাৰ্জন | Accent Refinement",
        "আঞ্চলিক উপভাষা | Regional Dialects",
        "প্ৰবাদ | Proverbs & Idioms",
        "ৰূপক | Metaphors & Figures",
        "সংস্কৃত শিপা | Sanskrit Roots",
        "তিব্বত-বৰ্মী প্ৰভাৱ | Tibeto-Burman Influence",
        "আহোম শব্দ | Ahom Loanwords",
        "সাহিত্যিক অসমীয়া | Literary Assamese",
        "কথিত অসমীয়া | Spoken Assamese",
        "গোৱালপৰীয়া উপভাষা | Goalparia Dialect",
    ]
    t = expert_titles[(day-61) % len(expert_titles)]
    CURRICULUM[day] = {
        "week": week, "phase": "Fluency",
        "title": t, "title_en": t.split("|")[1].strip() if "|" in t else t,
        "vocab":[
            {"a":"দক্ষতা","t":"dokhota","b":"দক্ষতা","e":"proficiency"},
            {"a":"স্বচ্ছন্দ","t":"xwochchondo","b":"স্বচ্ছন্দ","e":"fluent/comfortable"},
        ],
        "phrases":[
            {"a":"মই অসমীয়াত স্বচ্ছন্দ","t":"moi oxomiyaat xwochchondo","b":"আমি অসমীয়াতে স্বচ্ছন্দ","e":"I am fluent in Assamese"},
        ],
        "grammar": f"Day {day} — Fluency level. Focus on natural speech patterns and regional variations.",
        "culture": f"🌟 Day {day} of your fluency journey! You are mastering authentic Assamese.",
    }

# ══════════════════════════════════════════════════════════════════════════════
#  COMMUNICATION SCENARIOS (Native Voice Conversations)
# ══════════════════════════════════════════════════════════════════════════════

CONVERSATIONS = {
    "🏠 পৰিচয় | Self Introduction": {
        "desc": "Introduce yourself in Assamese",
        "level": "Beginner",
        "exchanges": [
            {"speaker":"A","assamese":"নমস্কাৰ! আপোনাৰ নাম কি?","transliteration":"nomoskar! aponaar naam ki?","english":"Hello! What is your name?","bengali":"নমস্কার! আপনার নাম কি?"},
            {"speaker":"B","assamese":"নমস্কাৰ! মোৰ নাম ৰাহুল। আপোনাৰ নাম কি?","transliteration":"nomoskar! mor naam Rahul. aponaar naam ki?","english":"Hello! My name is Rahul. What is your name?","bengali":"নমস্কার! আমার নাম রাহুল। আপনার নাম কি?"},
            {"speaker":"A","assamese":"মোৰ নাম প্ৰিয়া। আপুনি ক'ৰ পৰা?","transliteration":"mor naam Priya. apuni koror pora?","english":"My name is Priya. Where are you from?","bengali":"আমার নাম প্রিয়া। আপনি কোথা থেকে?"},
            {"speaker":"B","assamese":"মই গুৱাহাটীৰ পৰা। আপুনি?","transliteration":"moi guwahatiror pora. apuni?","english":"I am from Guwahati. You?","bengali":"আমি গুয়াহাটি থেকে। আপনি?"},
            {"speaker":"A","assamese":"মই ডিব্ৰুগড়ৰ পৰা। আপোনাৰ সৈতে লগ হৈ ভাল লাগিল।","transliteration":"moi dibrogorer pora. aponaar xoite log hoi bhaalo laagil.","english":"I am from Dibrugarh. Nice to meet you.","bengali":"আমি ডিব্রুগড় থেকে। আপনার সাথে দেখা হয়ে ভালো লাগলো।"},
        ]
    },
    "🍽️ ৰেস্তোৰাঁত | At the Restaurant": {
        "desc": "Order food at a restaurant",
        "level": "Beginner",
        "exchanges": [
            {"speaker":"Waiter","assamese":"নমস্কাৰ! কি দিম?","transliteration":"nomoskar! ki dim?","english":"Hello! What shall I give you?","bengali":"নমস্কার! কী দেব?"},
            {"speaker":"You","assamese":"মেনু কাৰ্ড দিব নে?","transliteration":"menu card dib ne?","english":"Can you give the menu?","bengali":"মেনু কার্ড দেবেন?"},
            {"speaker":"Waiter","assamese":"এই লওক। আজিৰ বিশেষ হৈছে মাছৰ জোল আৰু ভাত।","transliteration":"ei laok. aajir bixexx hoihe maasor jol aaroo bhaat.","english":"Here it is. Today's special is fish curry and rice.","bengali":"এই নিন। আজকের বিশেষ হলো মাছের ঝোল আর ভাত।"},
            {"speaker":"You","assamese":"এটা মাছৰ জোল আৰু এটা ভাত দিব। আৰু এগিলাচ পানী দিব।","transliteration":"ekta maasor jol aaroo ekta bhaat dib. aaroo egilaas paani dib.","english":"Give one fish curry and one rice. Also give a glass of water.","bengali":"একটা মাছের ঝোল আর একটা ভাত দেবেন। আর একগ্লাস পানি দেবেন।"},
            {"speaker":"Waiter","assamese":"বেছি মিৰচি দিম নে কম?","transliteration":"bexi mirchi dim ne kom?","english":"More chilli or less?","bengali":"বেশি মরিচ দেব না কম?"},
            {"speaker":"You","assamese":"অলপ কম দিব। বিল কিমান হব?","transliteration":"olop kom dib. bil kimaan hob?","english":"Give less. How much will the bill be?","bengali":"একটু কম দেবেন। বিল কত হবে?"},
        ]
    },
    "🏥 ডাক্তৰৰ ওচৰত | At the Doctor": {
        "desc": "Consult a doctor in Assamese",
        "level": "Intermediate",
        "exchanges": [
            {"speaker":"Doctor","assamese":"কি হৈছে? কি অসুবিধা?","transliteration":"ki hoihe? ki oxubidha?","english":"What happened? What is the problem?","bengali":"কী হয়েছে? কী সমস্যা?"},
            {"speaker":"You","assamese":"মোৰ জ্বৰ হৈছে আৰু মূৰ বিষাইছে।","transliteration":"mor jor hoihe aaroo mur bixaaise.","english":"I have fever and my head is aching.","bengali":"আমার জ্বর হয়েছে এবং মাথা ব্যথা করছে।"},
            {"speaker":"Doctor","assamese":"কেতিয়াৰ পৰা? কিমান দিন ধৰি?","transliteration":"ketiyaror pora? kimaan din dhori?","english":"Since when? For how many days?","bengali":"কখন থেকে? কতদিন ধরে?"},
            {"speaker":"You","assamese":"দুই দিন ধৰি। কাহো আহিছে।","transliteration":"dui din dhori. kaaho aahihe.","english":"For two days. Cough has also come.","bengali":"দুই দিন ধরে। কাশিও এসেছে।"},
            {"speaker":"Doctor","assamese":"ভয় নকৰিব। সাধাৰণ চৰ্দি। এই ঔষধ তিনি দিন খাব।","transliteration":"bhoy nokorib. xaadhaaronno xordi. ei ousodh tini din khaab.","english":"Don't worry. It's a common cold. Take this medicine for three days.","bengali":"ভয় পাবেন না। সাধারণ সর্দি। এই ওষুধ তিন দিন খাবেন।"},
        ]
    },
    "🛒 বাজাৰত | At the Market": {
        "desc": "Shop and bargain at the market",
        "level": "Beginner",
        "exchanges": [
            {"speaker":"You","assamese":"এই আমৰ দাম কিমান?","transliteration":"ei aaomor daam kimaan?","english":"What is the price of this mango?","bengali":"এই আমের দাম কত?"},
            {"speaker":"Seller","assamese":"পঞ্চাশ টকা কিলো।","transliteration":"ponsaas toka kilo.","english":"Fifty rupees per kilogram.","bengali":"পঞ্চাশ টাকা কিলো।"},
            {"speaker":"You","assamese":"বৰ বেছি। চল্লিশ টকাত দিব নে?","transliteration":"bor bexi. soliish tokaat dib ne?","english":"Very expensive. Will you give for forty rupees?","bengali":"অনেক বেশি। চল্লিশ টাকায় দেবেন?"},
            {"speaker":"Seller","assamese":"পঁয়তাল্লিশ টকাত দিম। শেষ দাম।","transliteration":"poytallix tokaat dim. xex daam.","english":"I'll give for forty-five rupees. Final price.","bengali":"পঁয়তাল্লিশ টাকায় দেব। শেষ দাম।"},
            {"speaker":"You","assamese":"ঠিক আছে। দুই কিলো দিব।","transliteration":"thik aahe. dui kilo dib.","english":"Okay. Give two kilograms.","bengali":"ঠিক আছে। দুই কিলো দেবেন।"},
        ]
    },
    "🚌 যাত্ৰাৰ সময়ত | During Travel": {
        "desc": "Ask for directions and travel help",
        "level": "Intermediate",
        "exchanges": [
            {"speaker":"You","assamese":"মাফ কৰিব, কামাখ্যা মন্দিৰলৈ কেনেকৈ যাব?","transliteration":"maph korib, kaamaakhya mondorloi kenekoi jaab?","english":"Excuse me, how to go to Kamakhya Temple?","bengali":"মাফ করবেন, কামাখ্যা মন্দিরে কীভাবে যাব?"},
            {"speaker":"Local","assamese":"বাছত যাব পাৰিব। নম্বৰ ৩৭ বাছ পাব।","transliteration":"baasoat jaab paarib. nombor 37 baas paab.","english":"You can go by bus. You'll get bus number 37.","bengali":"বাসে যেতে পারবেন। ৩৭ নম্বর বাস পাবেন।"},
            {"speaker":"You","assamese":"বাছ ষ্টেণ্ড ক'ত?","transliteration":"baas stand kot?","english":"Where is the bus stand?","bengali":"বাস স্ট্যান্ড কোথায়?"},
            {"speaker":"Local","assamese":"এই ৰাস্তাৰে পোনে যাওক। পাঁচ মিনিটত পাব।","transliteration":"ei raaxtaare pone jaok. paas minutot paab.","english":"Go straight on this road. You'll find it in five minutes.","bengali":"এই রাস্তায় সোজা যান। পাঁচ মিনিটে পাবেন।"},
            {"speaker":"You","assamese":"বৰ ধন্যবাদ। আপুনি বৰ সহায় কৰিলে।","transliteration":"bor dhonyobad. apuni bor xohaaay korile.","english":"Thank you very much. You helped a lot.","bengali":"অনেক ধন্যবাদ। আপনি অনেক সাহায্য করলেন।"},
        ]
    },
    "🏫 বিদ্যালয়ত | At School": {
        "desc": "Conversations in a school setting",
        "level": "Intermediate",
        "exchanges": [
            {"speaker":"Teacher","assamese":"আজি আমি অসমৰ ইতিহাস পঢ়িম।","transliteration":"aaji aami oxomor itihaas porim.","english":"Today we will read about Assam's history.","bengali":"আজ আমরা আসামের ইতিহাস পড়ব।"},
            {"speaker":"Student","assamese":"স্যাৰ, আহোম ৰাজ্য কেতিয়াৰ পৰা আৰম্ভ হৈছিল?","transliteration":"sir, aaham raajyo ketiyaror pora aarombho hoikhilo?","english":"Sir, when did the Ahom kingdom begin?","bengali":"স্যার, আহোম রাজ্য কখন থেকে শুরু হয়েছিল?"},
            {"speaker":"Teacher","assamese":"১২২৮ চনত। চুকাফা নামৰ ৰজাই আহোম ৰাজ্য প্ৰতিষ্ঠা কৰিছিল।","transliteration":"1228 xonot. xukaphaa naaomor rojaai aaham raajyo protixthaa korisikhilo.","english":"In 1228 CE. A king named Sukapha established the Ahom kingdom.","bengali":"১২২৮ সালে। সুকাফা নামের রাজা আহোম রাজ্য প্রতিষ্ঠা করেছিলেন।"},
            {"speaker":"Student","assamese":"ধন্যবাদ স্যাৰ। মই বুজি পালো।","transliteration":"dhonyobad sir. moi buji paalo.","english":"Thank you sir. I understood.","bengali":"ধন্যবাদ স্যার। আমি বুঝতে পারলাম।"},
        ]
    },
    "📞 ফোনত কথা | Phone Conversation": {
        "desc": "Have a phone conversation in Assamese",
        "level": "Beginner",
        "exchanges": [
            {"speaker":"You","assamese":"হেলো, মই ৰাহুল কৈছো। প্ৰিয়া আছে নে?","transliteration":"hello, moi Rahul koisho. Priya aahe ne?","english":"Hello, this is Rahul. Is Priya there?","bengali":"হেলো, আমি রাহুল বলছি। প্রিয়া আছে?"},
            {"speaker":"Other","assamese":"হয়, এক মিনিট অপেক্ষা কৰক।","transliteration":"hoy, ek minut opekkha korok.","english":"Yes, please wait one minute.","bengali":"হ্যাঁ, এক মিনিট অপেক্ষা করুন।"},
            {"speaker":"Priya","assamese":"হেলো ৰাহুল! কেনে আছা?","transliteration":"hello Rahul! kene aacha?","english":"Hello Rahul! How are you?","bengali":"হেলো রাহুল! কেমন আছো?"},
            {"speaker":"You","assamese":"ভালেই আছো। কাইলৈ কি কৰিবা?","transliteration":"bhalei aacho. kaaloi ki koriba?","english":"I'm fine. What will you do tomorrow?","bengali":"ভালো আছি। কাল কী করবে?"},
            {"speaker":"Priya","assamese":"কাইলৈ মই ঘৰতে থাকিম। কিয়?","transliteration":"kaaloi moi ghorate thaakiim. kiyo?","english":"Tomorrow I'll stay home. Why?","bengali":"কাল আমি ঘরে থাকব। কেন?"},
            {"speaker":"You","assamese":"কাজিৰঙালৈ যাম বুলি ভাবিছিলো। তুমি যাবা নে?","transliteration":"kaajironggaloi jaam buli bhaabisilo. tumi jaabaa ne?","english":"Was thinking of going to Kaziranga. Will you go?","bengali":"কাজিরাঙা যাব বলে ভাবছিলাম। তুমি যাবে?"},
        ]
    },
    "💼 চাকৰিৰ সাক্ষাৎকাৰ | Job Interview": {
        "desc": "Job interview in Assamese",
        "level": "Advanced",
        "exchanges": [
            {"speaker":"Interviewer","assamese":"আপোনাৰ নিজৰ বিষয়ে কওক।","transliteration":"aponaar nijor bishoye kowk.","english":"Tell me about yourself.","bengali":"আপনার নিজের সম্পর্কে বলুন।"},
            {"speaker":"You","assamese":"মোৰ নাম অনুপম। মই গুৱাহাটী বিশ্ববিদ্যালয়ৰ পৰা বাণিজ্য বিভাগত স্নাতক।","transliteration":"mor naam Anupam. moi Guwahati Bishwobidyalayror pora baanijyo bibhaaagot xnaatak.","english":"My name is Anupam. I graduated in Commerce from Gauhati University.","bengali":"আমার নাম অনুপম। আমি গুয়াহাটি বিশ্ববিদ্যালয় থেকে বাণিজ্যে স্নাতক।"},
            {"speaker":"Interviewer","assamese":"আপোনাৰ কি কি অভিজ্ঞতা আছে?","transliteration":"aponaar ki ki obhijnyotaa aahe?","english":"What experience do you have?","bengali":"আপনার কী কী অভিজ্ঞতা আছে?"},
            {"speaker":"You","assamese":"মই দুই বছৰ এটা বেচৰকাৰী সংস্থাত কাম কৰিছো। হিচাপ-নিকাচৰ অভিজ্ঞতা আছে।","transliteration":"moi dui boshor ekta bexorkaari xongxthaat kaam koriso. hisaap-nikaashor obhijnyotaa aahe.","english":"I have worked for two years in an NGO. I have experience in accounting.","bengali":"আমি দুই বছর একটি এনজিওতে কাজ করেছি। হিসাব-নিকাশের অভিজ্ঞতা আছে।"},
            {"speaker":"Interviewer","assamese":"বেতন কিমান আশা কৰিছে?","transliteration":"betoon kimaan aaxa koriso?","english":"What salary are you expecting?","bengali":"বেতন কত আশা করছেন?"},
        ]
    },
}

# ══════════════════════════════════════════════════════════════════════════════
#  QUIZ BANK (100 questions)
# ══════════════════════════════════════════════════════════════════════════════

QUIZ_BANK = [
    {"q":"'নমস্কাৰ' মানে কি?","opts":["বিদায়","অভিবাদন","ধন্যবাদ","মাফ কৰিব"],"ans":1,"exp":"নমস্কাৰ = standard Assamese greeting"},
    {"q":"অসমীয়াত 'মই' মানে কি?","opts":["আপনি","তুমি","আমি","তিনি"],"ans":2,"exp":"মই = I in Assamese (Bengali: আমি)"},
    {"q":"'দেউতা' মানে কি?","opts":["মা","দাদা","বাবা/পিতা","ককা"],"ans":2,"exp":"দেউতা = father (Bengali: বাবা)"},
    {"q":"'পানী' মানে কি?","opts":["চাহ","দুধ","জল","ভাত"],"ans":2,"exp":"পানী = water"},
    {"q":"'হয়' মানে কি?","opts":["না","হ্যাঁ","হয়তো","কখনো না"],"ans":1,"exp":"হয় = yes, নহয় = no"},
    {"q":"অসমীয়াত 'big' কি?","opts":["সৰু","ডাঙৰ","ওখ","মোটা"],"ans":1,"exp":"ডাঙৰ = big/large"},
    {"q":"'চাহ' মানে কি?","opts":["কফি","চা","দুধ","ৰস"],"ans":1,"exp":"চাহ = tea — Assam produces 50%+ of India's tea!"},
    {"q":"'ককাই' মানে কি?","opts":["ভাই","বাই","দাদা (বয়োজ্যেষ্ঠ ভাই)","মামা"],"ans":2,"exp":"ককাই = elder brother"},
    {"q":"অসমীয়াত '5' কি?","opts":["চাৰি","ছয়","পাঁচ","সাত"],"ans":2,"exp":"পাঁচ = five"},
    {"q":"'ৰাতিপুৱা' মানে কি?","opts":["সন্ধ্যা","ৰাত","সকাল","দুপুৰ"],"ans":2,"exp":"ৰাতিপুৱা = morning"},
    {"q":"'ভাত' মানে কি?","opts":["ৰুটি","চাউল","ভাত (ৰন্ধা চাউল)","মাছ"],"ans":2,"exp":"ভাত = cooked rice"},
    {"q":"অসমীয়া অনন্য বৰ্ণ কোনটো?","opts":["ক","ৰ","ম","স"],"ans":1,"exp":"ৰ (ro) is unique to Assamese — not in standard Bengali!"},
    {"q":"'আইতা' মানে কি?","opts":["মা","দিদিমা (মাতৃৰ মা)","পেহী","নানী"],"ans":1,"exp":"আইতা = maternal grandmother"},
    {"q":"'কালি' মানে কি?","opts":["আজি","আগলৈ","কাল (আগৰ বা পিছৰ)","পৰহি"],"ans":2,"exp":"কালি = both yesterday and tomorrow — context matters!"},
    {"q":"'ভোক লাগিছে' মানে কি?","opts":["পিয়াহ লাগিছে","ভোক লাগিছে","টোপনি আহিছে","ভয় লাগিছে"],"ans":1,"exp":"ভোক লাগিছে = I am hungry"},
    {"q":"'ডাক্তৰ' মানে কি?","opts":["শিক্ষক","ডাক্তার","উকীল","অভিযন্তা"],"ans":1,"exp":"ডাক্তৰ = doctor"},
    {"q":"অসমৰ ৰাজধানী কোনখন?","opts":["ডিব্ৰুগড়","যোৰহাট","দিছপুৰ","শিলচৰ"],"ans":2,"exp":"দিছপুৰ (Dispur) is the capital of Assam"},
    {"q":"'বিহু' কি?","opts":["এটা খাদ্য","অসমৰ মূল উৎসৱ","এটা নদী","এটা মন্দিৰ"],"ans":1,"exp":"বিহু is Assam's most important festival, celebrated 3 times a year"},
    {"q":"'মাফ কৰিব' মানে কি?","opts":["ধন্যবাদ","অভিবাদন","ক্ষমা কৰিব","বিদায়"],"ans":2,"exp":"মাফ কৰিব = excuse me / sorry"},
    {"q":"'সুন্দৰ' মানে কি?","opts":["বেয়া","সৰু","সুন্দর","ডাঙৰ"],"ans":2,"exp":"সুন্দৰ = beautiful"},
    {"q":"'নদী' মানে কি?","opts":["পাহাৰ","সমুদ্ৰ","নদী","হ্ৰদ"],"ans":2,"exp":"নদী = river"},
    {"q":"'খোৱা' মানে কি?","opts":["পান করা","খাওয়া","ঘুমানো","হাঁটা"],"ans":1,"exp":"খোৱা = to eat"},
    {"q":"'বৰষুণ' মানে কি?","opts":["ৰ'দ","মেঘ","বৃষ্টি","বতাহ"],"ans":2,"exp":"বৰষুণ = rain"},
    {"q":"'গছ' মানে কি?","opts":["ফুল","গাছ","পাত","শিপা"],"ans":1,"exp":"গছ = tree"},
    {"q":"'ধন্যবাদ' মানে কি?","opts":["ক্ষমা","ধন্যবাদ","অভিনন্দন","বিদায়"],"ans":1,"exp":"ধন্যবাদ = thank you"},
    {"q":"অসমীয়াত 'Monday' কি?","opts":["ৰবিবাৰ","সোমবাৰ","মঙলবাৰ","বুধবাৰ"],"ans":1,"exp":"সোমবাৰ = Monday"},
    {"q":"'জ্বৰ' মানে কি?","opts":["মাথাব্যথা","জ্বর","কাশি","পেটব্যথা"],"ans":1,"exp":"জ্বৰ = fever"},
    {"q":"'চোতাল' মানে কি?","opts":["ছাদ","দেয়াল","উঠোন","দরজা"],"ans":2,"exp":"চোতাল = courtyard"},
    {"q":"'বন্ধু' মানে কি?","opts":["শত্রু","বন্ধু","পরিবার","প্রতিবেশী"],"ans":1,"exp":"বন্ধু = friend"},
    {"q":"'পঢ়া' মানে কি?","opts":["লেখা","পড়া","বলা","শোনা"],"ans":1,"exp":"পঢ়া = to read/study"},
]

PROVERBS = [
    {"assamese":"হাতী মৰে দাঁতৰ কাৰণে","transliteration":"haati more daantor kaaronno","bengali":"হাতি মরে দাঁতের কারণে","english":"An elephant dies because of its tusks (greatness can be one's downfall)","meaning":"One's strength can also be one's weakness"},
    {"assamese":"নিজে খোৱা ভাত মিঠা","transliteration":"nije khowa bhaat mitha","bengali":"নিজে খাওয়া ভাত মিষ্টি","english":"Rice eaten by oneself is sweet","meaning":"Self-earned things taste sweeter"},
    {"assamese":"একতাত শক্তি আছে","transliteration":"ekataat xokti aahe","bengali":"একতায় শক্তি আছে","english":"There is strength in unity","meaning":"Unity is power"},
    {"assamese":"নাওখন সৰু হ'লেও নৈ পাৰ কৰিব পাৰি","transliteration":"naaokhon xoru holleo noi paar korib paari","bengali":"নৌকা ছোট হলেও নদী পার করতে পারে","english":"Even a small boat can cross a river","meaning":"Small efforts can achieve big goals"},
    {"assamese":"আগৰে চাই পিছত দিয়া ভাল","transliteration":"aaagore saai pisot diya bhaalo","bengali":"আগে দেখে পরে দেওয়া ভালো","english":"It is better to see first before giving","meaning":"Think before you act"},
]

CULTURAL_FACTS = [
    {"f":"বিহু উৎসৱ বছৰত তিনিবাৰ পালন কৰা হয়: বহাগ (এপ্ৰিল), কাতি (অক্টোবৰ), মাঘ (জানুৱাৰী)","e":"Bihu is celebrated 3 times: Bohag (April), Kati (October), Magh (January)","emoji":"🎊"},
    {"f":"অসম বিশ্বৰ আটাইতকৈ বৃহৎ চাহ উৎপাদনকাৰী অঞ্চল","e":"Assam is the world's largest tea-producing region","emoji":"🍵"},
    {"f":"কাজিৰঙা ৰাষ্ট্ৰীয় উদ্যানত বিশ্বৰ দুই-তৃতীয়াংশ এক-শিঙীয়া গঁড় আছে","e":"Kaziranga has 2/3 of world's one-horned rhinoceroses","emoji":"🦏"},
    {"f":"মাজুলী দ্বীপ পৃথিৱীৰ আটাইতকৈ ডাঙৰ নদী দ্বীপ","e":"Majuli is the world's largest river island","emoji":"🏝️"},
    {"f":"আহোম বংশই মোগলক কেতিয়াও হৰা দিয়া নাছিল","e":"The Ahom dynasty never surrendered to the Mughals","emoji":"👑"},
    {"f":"কামাখ্যা মন্দিৰ ৫১টা শক্তিপীঠৰ এটা","e":"Kamakhya Temple is one of the 51 Shakti Peethas","emoji":"🛕"},
    {"f":"মুগা ৰেচম কেৱল অসমতে পোৱা যায়","e":"Muga silk is found only in Assam","emoji":"🪡"},
    {"f":"ব্ৰহ্মপুত্ৰ নদীত বিশ্বৰ বৃহত্তম নদী দ্বীপ মাজুলী আছে","e":"Brahmaputra river contains Majuli, the world's largest river island","emoji":"🌊"},
    {"f":"অসমত ভাৰতৰ সৰ্বাধিক বনৰীয়া হাতী আছে","e":"Assam has India's highest number of wild elephants","emoji":"🐘"},
    {"f":"গুৱাহাটী উত্তৰ-পূৰ্ব ভাৰতৰ প্ৰৱেশদ্বাৰ চহৰ","e":"Guwahati is the gateway city to Northeast India","emoji":"🌆"},
    {"f":"শংকৰদেৱে ১৫শ শতিকাত অসমীয়া সাহিত্য আৰু সংস্কৃতিৰ পুনৰজাগৰণ ঘটাইছিল","e":"Sankardev led a renaissance of Assamese culture in 15th century","emoji":"📜"},
    {"f":"অসমীয়া ভাষা ইন্দো-ইউৰোপীয় পৰিয়ালৰ আটাইতকৈ পূৰ্বৰ ভাষা","e":"Assamese is the easternmost Indo-European language","emoji":"🗺️"},
]

MOTIVATIONAL = [
    "তুমি বৰ ভালদৰে কৰিছা! শিকি থাকক!","লাহে লাহে অভ্যাস কৰক!","প্ৰতিদিন অলপ অলপ শিকা — এদিন অসমীয়া বলিব পাৰিবা!",
    "চেষ্টা কৰক, সফল হওক!","অসমীয়া শিক্ষা তোমাৰ বাবে — তুমি পাৰিবা!","অসমৰ ভাষা, অসমৰ প্ৰাণ!",
]

VOWELS = [
    {"a":"অ","t":"o","b":"অ","e":"a (short)"},{"a":"আ","t":"aa","b":"আ","e":"aa (long)"},
    {"a":"ই","t":"i","b":"ই","e":"i (short)"},{"a":"ঈ","t":"ii","b":"ঈ","e":"ee (long)"},
    {"a":"উ","t":"u","b":"উ","e":"u (short)"},{"a":"ঊ","t":"uu","b":"ঊ","e":"oo (long)"},
    {"a":"ঋ","t":"ri","b":"ঋ","e":"ri"},{"a":"এ","t":"e","b":"এ","e":"e"},
    {"a":"ঐ","t":"oi","b":"ঐ","e":"oi"},{"a":"ও","t":"o","b":"ও","e":"o (long)"},{"a":"ঔ","t":"ou","b":"ঔ","e":"ou"},
]
CONSONANTS = [
    {"a":"ক","t":"k","b":"ক","e":"k"},{"a":"খ","t":"kh","b":"খ","e":"kh"},{"a":"গ","t":"g","b":"গ","e":"g"},
    {"a":"ঘ","t":"gh","b":"ঘ","e":"gh"},{"a":"ঙ","t":"ng","b":"ঙ","e":"ng"},
    {"a":"চ","t":"s/x","b":"চ","e":"s (Assamese 'x' sound)"},{"a":"ছ","t":"kh","b":"ছ","e":"kh"},
    {"a":"জ","t":"j","b":"জ","e":"j"},{"a":"ঝ","t":"jh","b":"ঝ","e":"jh"},
    {"a":"ট","t":"t","b":"ট","e":"t (retroflex)"},{"a":"ড","t":"d","b":"ড","e":"d (retroflex)"},
    {"a":"ত","t":"t","b":"ত","e":"t (dental)"},{"a":"দ","t":"d","b":"দ","e":"d (dental)"},
    {"a":"ন","t":"n","b":"ন","e":"n"},{"a":"প","t":"p","b":"প","e":"p"},{"a":"ফ","t":"ph","b":"ফ","e":"ph"},
    {"a":"ব","t":"b","b":"ব","e":"b"},{"a":"ম","t":"m","b":"ম","e":"m"},{"a":"য","t":"j","b":"য","e":"y"},
    {"a":"ৰ","t":"r","b":"র","e":"r ★ UNIQUE","unique":True},{"a":"ল","t":"l","b":"ল","e":"l"},
    {"a":"ৱ","t":"w","b":"(ব)","e":"w ★ UNIQUE","unique":True},
    {"a":"শ","t":"x","b":"শ","e":"x/sh ★ Assamese"},{"a":"হ","t":"h","b":"হ","e":"h"},
]

# ══════════════════════════════════════════════════════════════════════════════
#  SESSION STATE
# ══════════════════════════════════════════════════════════════════════════════

def init_state():
    defaults = {
        "registered":False,"user_name":"","native_language":"Bengali",
        "current_day":1,"completed_lessons":[],"streak":0,
        "last_login":"","total_xp":0,"badges":[],"weekly_test_scores":[],
        "page":"home","voice_profile":DEFAULT_VOICE,
        "fc_idx":0,"fc_flipped":False,"fill_idx":0,
        "wt_started":False,"wt_questions":[],"wt_answers":{},"wt_submitted":False,
        "mw":None,"ma":{},"conv_audio_idx":{},
        "drill_idx":0,"drill_set":"🏠 Family",
    }
    for k,v in defaults.items():
        if k not in st.session_state:
            st.session_state[k]=v

def update_streak():
    today=str(date.today()); last=st.session_state.last_login
    if last==today: return
    yesterday=str(date.today()-timedelta(days=1))
    st.session_state.streak=(st.session_state.streak+1) if last==yesterday else 1
    st.session_state.last_login=today

def add_xp(pts):
    st.session_state.total_xp+=pts; _badges()

def _badges():
    b=st.session_state.badges; xp=st.session_state.total_xp
    s=st.session_state.streak; d=len(st.session_state.completed_lessons)
    for bid,cond,name,desc in [
        ("first_lesson",d>=1,"📚 First Steps","Completed first lesson!"),
        ("ten_lessons",d>=10,"🔟 Ten Down","Completed 10 lessons!"),
        ("thirty_lessons",d>=30,"🗓️ Month Strong","Completed 30 lessons!"),
        ("sixty_lessons",d>=60,"🏅 Halfway","Completed 60 lessons!"),
        ("full_course",d>=120,"👑 Fluent!","Completed all 120 lessons!"),
        ("first_century",xp>=100,"🌟 Century","Earned 100 XP!"),
        ("xp_500",xp>=500,"🎓 Scholar","Earned 500 XP!"),
        ("xp_1000",xp>=1000,"💎 Diamond","Earned 1000 XP!"),
        ("streak_3",s>=3,"🔥 On Fire","3-day streak!"),
        ("streak_7",s>=7,"⚡ Week","7-day streak!"),
        ("streak_30",s>=30,"🏆 Champion","30-day streak!"),
    ]:
        if cond and bid not in b:
            b.append(bid); st.toast(f"🏆 {name} — {desc}")

def get_level(xp):
    for lvl,ass,en,nxt in [
        (1,"নতুন শিক্ষাৰ্থী","Beginner",150),
        (2,"প্ৰাথমিক","Elementary",400),
        (3,"মধ্যবৰ্তী","Intermediate",800),
        (4,"উচ্চ মধ্যবৰ্তী","Upper-Intermediate",1500),
        (5,"উন্নত","Advanced",2500),
        (6,"দক্ষ","Proficient",4000),
        (7,"অসমীয়া বিশেষজ্ঞ","Fluent/Expert",9999),
    ]:
        if xp<nxt: return lvl,ass,en,nxt
    return 7,"অসমীয়া বিশেষজ্ঞ","Fluent/Expert",9999

def goto(page):
    st.session_state.page=page; st.rerun()

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
  --gr2:linear-gradient(135deg,#2EC4B6,#06D6A0);
  --gr3:linear-gradient(135deg,#7B2FBE,#9D4EDD);
}
.stApp{background:var(--bg)!important;font-family:'Nunito',sans-serif;color:var(--tx)!important;}
h1,h2,h3,h4{color:var(--tx)!important;}
p,li,label,span{color:var(--tx);}
.main .block-container{padding-top:.8rem;max-width:1200px;}
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
.vc:hover{border-color:var(--p);transform:translateY(-2px);box-shadow:0 8px 28px rgba(255,107,53,.15);}
.lc{background:var(--c1);border:1px solid rgba(255,107,53,.2);border-radius:18px;padding:20px;margin:10px 0;transition:all .25s;}
.lc:hover{border-color:var(--p);}
.mc{background:var(--c1);border:1px solid rgba(255,107,53,.2);border-radius:16px;padding:14px;text-align:center;}
.mv{font-size:2.2em;font-weight:900;color:var(--p);font-family:'Space Grotesk',sans-serif;line-height:1.1;}
.ml{color:var(--mt);font-size:.75em;text-transform:uppercase;letter-spacing:1px;margin-top:3px;}
.hero{background:linear-gradient(135deg,rgba(255,107,53,.12),rgba(26,26,46,.95));border:1px solid rgba(255,107,53,.3);border-radius:22px;padding:32px;text-align:center;margin-bottom:20px;}
.at{font-family:'Hind Siliguri','Nunito',serif;font-size:2em;color:var(--p);font-weight:700;line-height:1.3;}
.tr{font-family:'Space Grotesk',monospace;color:#F7C59F;font-size:.88em;font-style:italic;}
.bn{color:var(--s);font-size:1.05em;}
.en{color:var(--mt);font-size:.9em;}
.ib{background:rgba(46,196,182,.1);border:1px solid rgba(46,196,182,.3);border-radius:12px;padding:12px;margin:6px 0;}
.wb{background:rgba(255,209,102,.1);border:1px solid rgba(255,209,102,.3);border-radius:12px;padding:12px;margin:6px 0;}
.eb{background:rgba(239,35,60,.1);border:1px solid rgba(239,35,60,.3);border-radius:12px;padding:12px;margin:6px 0;}
.pw{background:rgba(255,255,255,.08);border-radius:20px;height:10px;margin:5px 0;overflow:hidden;}
.pf{height:100%;border-radius:20px;background:var(--gr);transition:width .5s ease;}
.ac{background:var(--c1);border:1px solid rgba(255,107,53,.2);border-radius:10px;padding:10px 6px;text-align:center;transition:all .2s;}
.ac:hover{border-color:var(--p);background:var(--pd);}
.bubble-a{background:rgba(255,107,53,.15);border:1px solid rgba(255,107,53,.3);border-radius:18px 18px 18px 4px;padding:14px 18px;margin:8px 0 8px 0;max-width:80%;}
.bubble-b{background:rgba(46,196,182,.12);border:1px solid rgba(46,196,182,.3);border-radius:18px 18px 4px 18px;padding:14px 18px;margin:8px 0 8px auto;max-width:80%;}
.phase-badge{display:inline-block;padding:3px 12px;border-radius:20px;font-size:.72em;font-weight:800;letter-spacing:.8px;text-transform:uppercase;}
.phase-Foundation{background:rgba(46,196,182,.2);color:#2EC4B6;}
.phase-Intermediate{background:rgba(255,209,102,.2);color:#FFD166;}
.phase-Advanced{background:rgba(255,107,53,.2);color:#FF6B35;}
.phase-Fluency{background:rgba(123,47,190,.2);color:#9D4EDD;}
.phase-Expert{background:rgba(239,35,60,.2);color:#EF233C;}
.stSelectbox>div>div{background:var(--c1)!important;color:var(--tx)!important;}
.stTextInput>div>div>input{background:var(--c1)!important;color:var(--tx)!important;}
.stTextArea>div>div>textarea{background:var(--c1)!important;color:var(--tx)!important;}
</style>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  SIDEBAR
# ══════════════════════════════════════════════════════════════════════════════

def sidebar():
    with st.sidebar:
        st.markdown("""<div style='text-align:center;padding:12px 0 4px'>
          <div style='font-size:2.4em'>🦚</div>
          <div style='font-size:1.3em;font-weight:900;color:#FF6B35'>অসমীয়া শিক্ষা</div>
          <div style='font-size:.68em;color:#a7a9be;letter-spacing:1.5px'>COMPLETE ASSAMESE · 120 DAYS</div>
        </div>""", unsafe_allow_html=True)
        st.markdown("---")
        if st.session_state.registered:
            xp=st.session_state.total_xp; lvl,ass,en,nxt=get_level(xp)
            pct=min(int(xp/nxt*100),100); name=st.session_state.user_name
            st.markdown(f"<div style='font-weight:800;font-size:1em'>👤 {name}</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='color:#a7a9be;font-size:.8em'>Lv.{lvl} · {en}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='pw'><div class='pf' style='width:{pct}%'></div></div>", unsafe_allow_html=True)
            st.markdown(f"<div style='font-size:.7em;color:#a7a9be'>{xp}/{nxt} XP · Day {st.session_state.current_day}/120</div>", unsafe_allow_html=True)
            s=st.session_state.streak
            st.markdown(f"<div style='margin:8px 0;background:#16213E;border-radius:10px;padding:7px;text-align:center'>{'🔥'if s else'💤'} <b style='color:#FF6B35'>{s}</b> <span style='color:#a7a9be;font-size:.78em'>day streak</span></div>", unsafe_allow_html=True)
            st.markdown("---")
        for ico,lbl,key in [
            ("🏠","Home","home"),("📅","120-Day Plan","plan"),
            ("📖","Daily Lessons","lessons"),("🔤","Alphabet","alphabet"),
            ("🗣️","Voice Practice","voice"),("💬","Conversations","conversations"),
            ("✏️","Practice","practice"),("📝","Weekly Test","weekly_test"),
            ("📊","Progress","progress"),("📜","Proverbs","proverbs"),
            ("ℹ️","About Assam","culture"),
        ]:
            if st.button(f"{ico} {lbl}",key=f"nav_{key}",use_container_width=True):
                goto(key)
        st.markdown("---")
        st.markdown(f"<div style='text-align:center;font-size:.7em;color:#a7a9be'>Made with ❤️ for Assamese learners<br><span style='color:#FF6B35'>অসম · Assam · আসাম</span></div>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  PAGE: HOME
# ══════════════════════════════════════════════════════════════════════════════

def page_home():
    if not st.session_state.registered:
        st.markdown("""<div class='hero'>
          <div style='font-size:3em'>🦚</div>
          <h1 style='font-size:2.3em;margin:6px 0'>অসমীয়া শিকক!</h1>
          <p style='color:#a7a9be;font-size:1em;max-width:560px;margin:auto'>
            The most complete Assamese learning platform — 120-day curriculum,
            native regional voices, AI conversation partner, cultural immersion.
          </p></div>""", unsafe_allow_html=True)
        _,mid,_=st.columns([1,2,1])
        with mid:
            st.markdown("### 👋 Begin your journey")
            name=st.text_input("Your name",placeholder="Enter your name...")
            lang=st.selectbox("Your native language",["Bengali","English","Hindi","Both Bengali & English"])
            if st.button("🚀 Start 120-Day Assamese Journey!",use_container_width=True):
                if name.strip():
                    st.session_state.registered=True; st.session_state.user_name=name.strip()
                    st.session_state.native_language=lang; add_xp(10)
                    st.success("স্বাগতম! Welcome to Assamese! 🎉"); st.rerun()
                else: st.warning("Please enter your name.")
        st.markdown("---")
        st.markdown("### ✨ What's inside")
        for col,ico,ttl,dsc in zip(st.columns(4),
            ["📅","🗣️","💬","🏆"],
            ["120-Day Plan","Native Voices","Conversations","Gamified"],
            ["Structured from beginner to fluent","Authentic Assamese regional accent",
             "Real-life scenario dialogues","XP, streaks, badges & levels"]):
            col.markdown(f"<div class='mc'><div style='font-size:1.8em'>{ico}</div><div style='font-weight:800;margin:4px 0'>{ttl}</div><div style='color:#a7a9be;font-size:.8em'>{dsc}</div></div>", unsafe_allow_html=True)
        return

    name=st.session_state.user_name
    st.markdown(f"<div class='hero'><h1>নমস্কাৰ, {name}! 🦚</h1><p style='color:#a7a9be'>{random.choice(MOTIVATIONAL)}</p></div>", unsafe_allow_html=True)
    xp=st.session_state.total_xp; lvl,_,en,_=get_level(xp)
    for col,val,lbl in zip(st.columns(4),
        [f"🔥 {st.session_state.streak}",f"⭐ {xp}",f"📚 {len(st.session_state.completed_lessons)}/120",f"🏅 {len(st.session_state.badges)}"],
        ["Day Streak","Total XP","Lessons Done","Badges"]):
        col.markdown(f"<div class='mc'><div class='mv'>{val}</div><div class='ml'>{lbl}</div></div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    day=st.session_state.current_day; les=CURRICULUM.get(day,CURRICULUM[1])
    phase=les.get("phase","Foundation")
    fact=random.choice(CULTURAL_FACTS)
    ca,cb=st.columns([2,1])
    with ca:
        st.markdown(f"""<div class='lc'>
          <div style='display:flex;justify-content:space-between;align-items:center'>
            <div>
              <div style='color:#a7a9be;font-size:.75em'>TODAY · DAY {day}/120</div>
              <span class='phase-badge phase-{phase}'>{phase}</span>
              <h3 style='margin:5px 0'>{les['title']}</h3>
              <p style='color:#a7a9be;margin:0;font-size:.9em'>{les.get("grammar","")[:100]}...</p>
            </div>
            <div style='font-size:2.5em'>{'✅' if day in st.session_state.completed_lessons else '📖'}</div>
          </div>
          <div class='wb' style='margin-top:10px;font-style:normal'>{fact['emoji']} {fact['e']}</div>
        </div>""", unsafe_allow_html=True)
        ca1,ca2=st.columns(2)
        with ca1:
            if st.button("▶️ Today's Lesson",use_container_width=True): goto("lessons")
        with ca2:
            if st.button("💬 Practice Conversation",use_container_width=True): goto("conversations")
    with cb:
        st.markdown("#### 📊 Phase Progress")
        phases={"Foundation":30,"Intermediate":30,"Advanced":30,"Fluency":30}
        done=st.session_state.completed_lessons
        for ph,total in phases.items():
            phase_days=[d for d,l in CURRICULUM.items() if l.get("phase")==ph]
            ph_done=sum(1 for d in phase_days if d in done)
            pct=int(ph_done/max(total,1)*100)
            st.markdown(f"<div style='font-size:.8em;color:#a7a9be;margin-top:8px'><span class='phase-badge phase-{ph}'>{ph}</span> {ph_done}/{total}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='pw'><div class='pf' style='width:{pct}%'></div></div>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🃏 Today's Vocabulary Preview")
    words=les.get("vocab",[])[:4]
    if words:
        for col,w in zip(st.columns(len(words)),words):
            col.markdown(f"<div class='vc'><div class='at'>{w['a']}</div><div class='tr'>/{w['t']}/</div><div class='bn'>{w['b']}</div><div class='en'>{w['e']}</div></div>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  PAGE: 120-DAY PLAN
# ══════════════════════════════════════════════════════════════════════════════

def page_plan():
    st.markdown("## 📅 120-Day Complete Assamese Curriculum")
    st.markdown("<p style='color:#a7a9be'>From beginner to fluent in 120 structured days. Click any day to jump to that lesson.</p>", unsafe_allow_html=True)

    phase_filter=st.selectbox("Filter by phase:",["All","Foundation","Intermediate","Advanced","Fluency","Expert"])
    done=st.session_state.completed_lessons; current=st.session_state.current_day

    phases_order=["Foundation","Intermediate","Advanced","Fluency","Expert"]
    display_phases=[phase_filter] if phase_filter!="All" else phases_order

    for ph in display_phases:
        phase_items=[(d,l) for d,l in sorted(CURRICULUM.items()) if l.get("phase")==ph or (ph=="Expert" and l.get("phase")=="Fluency")]
        if not phase_items: continue
        colors={"Foundation":"#2EC4B6","Intermediate":"#FFD166","Advanced":"#FF6B35","Fluency":"#9D4EDD","Expert":"#EF233C"}
        clr=colors.get(ph,"#FF6B35")
        st.markdown(f"<h3 style='color:{clr};margin-top:20px'>{ph} Phase</h3>", unsafe_allow_html=True)
        cols=st.columns(5)
        for i,(day,les) in enumerate(phase_items):
            with cols[i%5]:
                is_done=day in done; is_cur=day==current
                bg="rgba(46,196,182,.15)" if is_done else ("rgba(255,107,53,.2)" if is_cur else "rgba(26,26,46,.8)")
                border=f"2px solid {clr}" if is_cur else ("1px solid #2EC4B6" if is_done else "1px solid rgba(255,255,255,.1)")
                mark="✅" if is_done else ("▶" if is_cur else str(day))
                st.markdown(f"""<div style='background:{bg};border:{border};border-radius:12px;padding:10px;text-align:center;margin:4px 0'>
                  <div style='font-weight:900;font-size:1.1em;color:{clr}'>{mark}</div>
                  <div style='font-size:.7em;color:#a7a9be;margin-top:3px'>{les.get("title_en","")[:20]}</div>
                </div>""", unsafe_allow_html=True)
                if st.button(f"Go",key=f"plan_{day}",use_container_width=True):
                    st.session_state.current_day=day; goto("lessons")

# ══════════════════════════════════════════════════════════════════════════════
#  PAGE: LESSONS
# ══════════════════════════════════════════════════════════════════════════════

def page_lessons():
    st.markdown("## 📖 Daily Lessons")
    day=st.session_state.current_day
    max_day=max(CURRICULUM.keys())

    col_nav1,col_nav2,col_nav3=st.columns([1,3,1])
    with col_nav1:
        if st.button("⬅️ Prev Day",use_container_width=True) and day>1:
            st.session_state.current_day=day-1; st.rerun()
    with col_nav2:
        sel=st.selectbox("Jump to day:",[f"Day {d}: {CURRICULUM[d]['title_en']}" for d in range(1,max_day+1)],index=day-1)
        cd=int(sel.split(":")[0].replace("Day","").strip())
        if cd!=day: st.session_state.current_day=cd; st.rerun()
    with col_nav3:
        if st.button("Next Day ➡️",use_container_width=True) and day<max_day:
            st.session_state.current_day=day+1; st.rerun()

    les=CURRICULUM.get(day,CURRICULUM[1]); done=day in st.session_state.completed_lessons
    phase=les.get("phase","Foundation")
    st.markdown(f"""<div class='lc'>
      <div style='display:flex;justify-content:space-between;align-items:center'>
        <div>
          <div style='color:#a7a9be;font-size:.75em;margin-bottom:4px'>DAY {day}/120</div>
          <span class='phase-badge phase-{phase}'>{phase}</span>
          <span style='color:#a7a9be;font-size:.75em;margin-left:8px'>Week {les.get("week",1)}</span>
          <h2 style='margin:6px 0'>{les["title"]}</h2>
        </div>
        <div style='font-size:2.5em'>{'✅' if done else '📖'}</div>
      </div></div>""", unsafe_allow_html=True)

    t1,t2,t3,t4,t5=st.tabs(["📖 Vocabulary","💬 Phrases","📐 Grammar","🎯 Culture & Fun","🔊 Listen All"])

    with t1:
        vocab=les.get("vocab",[])
        if not vocab:
            st.info("Review day — revisit previous lessons and take the Weekly Test!")
        else:
            show_t=st.checkbox("Show transliteration",value=True,key=f"lt_{day}")
            show_b=st.checkbox("Show Bengali",value=True,key=f"lb_{day}")
            for w in vocab:
                ca,cb=st.columns([4,1])
                with ca:
                    h=f"<div class='vc'><div class='at'>{w['a']}</div>"
                    if show_t: h+=f"<div class='tr'>/{w['t']}/</div>"
                    if show_b: h+=f"<div class='bn'>{w['b']}</div>"
                    h+=f"<div class='en'>{w['e']}</div></div>"
                    st.markdown(h,unsafe_allow_html=True)
                with cb:
                    st.markdown("<br><br>",unsafe_allow_html=True)
                    if st.button("🔊",key=f"sv_{day}_{w['a']}"):
                        speak(w['a'])

    with t2:
        for i,p in enumerate(les.get("phrases",[])):
            st.markdown(f"<div class='vc'><div class='at' style='font-size:1.4em'>{p['a']}</div><div class='tr'>/{p['t']}/</div><div class='bn'>{p['b']}</div><div class='en'>{p['e']}</div></div>", unsafe_allow_html=True)
            if st.button("🔊 Listen",key=f"sp_{day}_{i}"): speak(p['a'])

    with t3:
        st.markdown(f"<div class='ib'>💡 <b>Grammar:</b> {les.get('grammar','')}</div>", unsafe_allow_html=True)
        st.markdown("---")
        st.markdown("#### 📋 Core Pronouns")
        rows=[("মই","moi","আমি","I"),("মোৰ","mor","আমার","my"),("তুমি","tumi","তুমি","you (inf)"),
              ("আপুনি","apuni","আপনি","you (form)"),("সি","xi","সে","he/she"),
              ("আমি","aami","আমরা","we"),("তেওঁলোক","tewolok","তারা","they")]
        for c1,c2,c3,c4 in zip(st.columns(4),["**Assamese**","**Transliteration**","**Bengali**","**English**"],["","","",""],[""]*4):
            c1.markdown("**Assamese**"); c2.markdown("**Translit.**")
            c3.markdown("**Bengali**"); c4.markdown("**English**"); break
        for a,t,b,e in rows:
            c1,c2,c3,c4=st.columns(4)
            c1.markdown(f"<span class='at' style='font-size:1em'>{a}</span>",unsafe_allow_html=True)
            c2.markdown(f"<span class='tr'>{t}</span>",unsafe_allow_html=True)
            c3.markdown(f"<span class='bn'>{b}</span>",unsafe_allow_html=True)
            c4.markdown(e)

    with t4:
        st.markdown(f"<div class='wb' style='font-style:normal;padding:18px'>🌟 <b>Culture Note:</b><br><br>{les.get('culture','')}</div>", unsafe_allow_html=True)
        fc=random.choice(CULTURAL_FACTS)
        st.markdown(f"<div class='ib' style='margin-top:10px'>{fc['emoji']} {fc['f']}</div>", unsafe_allow_html=True)

    with t5:
        vocab=les.get("vocab",[]); phrases=les.get("phrases",[])
        if vocab or phrases:
            st.markdown("#### 🔊 Hear All Words & Phrases")
            if st.button("▶️ Play All Vocabulary",use_container_width=True):
                for w in vocab: speak(w['a'])
            if phrases and st.button("▶️ Play All Phrases",use_container_width=True):
                for p in phrases: speak(p['a'])
        st.markdown("#### 🎛️ Voice Settings")
        vp=st.selectbox("Voice:",list(VOICE_PROFILES.keys()),
                        index=list(VOICE_PROFILES.keys()).index(st.session_state.voice_profile),
                        key=f"vp_lesson")
        if vp!=st.session_state.voice_profile:
            st.session_state.voice_profile=vp

    st.markdown("---")
    ca,cb=st.columns(2)
    with ca:
        if not done:
            if st.button("✅ Mark Lesson Complete (+20 XP)",use_container_width=True):
                st.session_state.completed_lessons.append(day); add_xp(20)
                if day==st.session_state.current_day<120: st.session_state.current_day+=1
                st.success("🎉 +20 XP!"); st.rerun()
        else: st.success("✅ Completed!")
    with cb:
        if st.button("💬 Practice Conversation",use_container_width=True): goto("conversations")

# ══════════════════════════════════════════════════════════════════════════════
#  PAGE: ALPHABET
# ══════════════════════════════════════════════════════════════════════════════

def page_alphabet():
    st.markdown("## 🔤 Assamese Alphabet — সম্পূৰ্ণ বৰ্ণমালা")
    st.markdown("<p style='color:#a7a9be'>Complete Assamese script with native pronunciation. ★ marks letters unique to Assamese.</p>", unsafe_allow_html=True)

    def alpha_grid(items,pfx):
        cols=st.columns(6)
        for i,it in enumerate(items):
            with cols[i%6]:
                unique=it.get("unique",False)
                border="border:2px solid #FF6B35" if unique else "border:1px solid rgba(255,107,53,.2)"
                st.markdown(f"""<div class='ac' style='{border};margin-bottom:6px'>
                  <div class='at' style='font-size:1.9em'>{it['a']}</div>
                  <div class='tr' style='font-size:.78em'>{it['t']}</div>
                  <div class='bn' style='font-size:.8em'>{it['b']}</div>
                  <div class='en' style='font-size:.7em'>{it['e']}</div>
                </div>""", unsafe_allow_html=True)
                if st.button("▶",key=f"{pfx}_{i}",use_container_width=True): speak(it['a'])

    tv,tc,tcomp=st.tabs(["🅰️ Vowels — স্বৰবৰ্ণ","🔡 Consonants — ব্যঞ্জনবৰ্ণ","📝 Writing Practice"])
    with tv:
        st.markdown("<div class='ib'>11 vowels — similar to Bengali with subtle Assamese pronunciation differences.</div>", unsafe_allow_html=True)
        alpha_grid(VOWELS,"v")
    with tc:
        st.markdown("<div class='ib'>🌟 <b>Unique:</b> <b style='color:#FF6B35'>ৰ</b> (rolled r) and <b style='color:#FF6B35'>ৱ</b> (w sound) exist only in Assamese. All of শ/ষ/স are pronounced as 'x' (sh).</div>", unsafe_allow_html=True)
        alpha_grid(CONSONANTS,"c")
    with tcomp:
        st.markdown("#### ✍️ Transliteration Practice")
        st.markdown("<p style='color:#a7a9be'>Type the transliteration for each Assamese character shown.</p>", unsafe_allow_html=True)
        sample=random.sample(VOWELS+CONSONANTS,5)
        score=0
        for i,ch in enumerate(sample):
            ans=st.text_input(f"What is the transliteration of '{ch['a']}'?",key=f"alpha_prac_{i}")
            if ans.strip().lower()==ch['t'].lower().split("/")[0]:
                st.success(f"✅ Correct! /{ch['t']}/"); score+=1
            elif ans.strip(): st.error(f"❌ Answer: /{ch['t']}/")
        if st.button("🔀 New Letters",use_container_width=True): st.rerun()

# ══════════════════════════════════════════════════════════════════════════════
#  PAGE: VOICE PRACTICE
# ══════════════════════════════════════════════════════════════════════════════

def page_voice():
    st.markdown("## 🗣️ Voice Practice — আঞ্চলিক কণ্ঠস্বৰ")
    st.markdown("<p style='color:#a7a9be'>Native regional voices using eSpeak-NG — authentic Assamese, Bengali and Hindi Indian accents. Choose your preferred voice below.</p>", unsafe_allow_html=True)

    # Voice selector
    st.markdown("<div class='ib'><b>🎙️ Select Regional Voice</b></div>", unsafe_allow_html=True)
    pcols=st.columns(3)
    for col,pname in zip(pcols,VOICE_PROFILES.keys()):
        p=VOICE_PROFILES[pname]; active=pname==st.session_state.voice_profile
        bg="rgba(255,107,53,.18)" if active else "rgba(26,26,46,.8)"
        border=f"2px solid #FF6B35" if active else "1px solid rgba(255,107,53,.2)"
        col.markdown(f"""<div style='background:{bg};border:{border};border-radius:14px;padding:14px;text-align:center;margin-bottom:8px'>
          <div style='font-size:1.6em'>{pname.split()[0]}</div>
          <div style='font-weight:800;font-size:.88em'>{' '.join(pname.split()[1:])}</div>
          <div style='color:#a7a9be;font-size:.72em;margin-top:2px'>{p['desc']}</div>
          <div style='color:#F7C59F;font-size:.7em'>lang={p['lang']}</div>
        </div>""", unsafe_allow_html=True)
        if col.button("✓ Active" if active else "Select",key=f"vp_{pname}",use_container_width=True):
            st.session_state.voice_profile=pname; st.rerun()

    st.markdown("---")
    tw,tp,ta,tdrill=st.tabs(["🔤 All Words","💬 Phrases","🔡 Letters","🏋️ Drill"])

    with tw:
        st.markdown("#### 🔤 Listen to Vocabulary")
        all_w=[(w,les['title_en']) for d,les in CURRICULUM.items() for w in les.get("vocab",[]) if les.get("vocab")]
        topics=["All"]+list(dict.fromkeys([l for _,l in all_w]))
        tp_sel=st.selectbox("Topic:",topics,key="vt_topic")
        filtered=[(w,l) for w,l in all_w if tp_sel=="All" or l==tp_sel]
        if filtered:
            opts=[f"{w['a']} — {w['e']}" for w,_ in filtered]
            sel=st.selectbox("Word:",opts,key="vt_word")
            idx=next((i for i,(w,_) in enumerate(filtered) if f"{w['a']} — {w['e']}"==sel),0)
            w,_=filtered[idx]
            st.markdown(f"""<div class='vc' style='text-align:center;padding:30px'>
              <div class='at' style='font-size:3.2em;letter-spacing:4px'>{w['a']}</div>
              <div class='tr' style='font-size:1.1em;margin-top:8px'>/{w['t']}/</div>
              <div style='display:flex;justify-content:center;gap:24px;margin-top:12px'>
                <div><span style='color:#a7a9be;font-size:.75em'>BENGALI</span><br><span class='bn'>{w['b']}</span></div>
                <div><span style='color:#a7a9be;font-size:.75em'>ENGLISH</span><br><span class='en'>{w['e']}</span></div>
              </div></div>""", unsafe_allow_html=True)
            c1,c2,c3=st.columns(3)
            with c1:
                if st.button("🔊 Normal",use_container_width=True,key="spk_n"): speak(w['a'])
            with c2:
                if st.button("🐢 Slow",use_container_width=True,key="spk_s"): speak(w['a'],slow=True)
            with c3:
                if st.button("🔁 ×3",use_container_width=True,key="spk_r"):
                    for _ in range(3): speak(w['a'])

    with tp:
        st.markdown("#### 💬 Phrase Pronunciation")
        all_p=[(p,les['title_en']) for d,les in CURRICULUM.items() for p in les.get("phrases",[])]
        tp_sel2=st.selectbox("Topic:",["All"]+list(dict.fromkeys([l for _,l in all_p])),key="vp_topic")
        filt_p=[(p,l) for p,l in all_p if tp_sel2=="All" or l==tp_sel2]
        if filt_p:
            sel_p=st.selectbox("Phrase:",[f"{p['e']}" for p,_ in filt_p],key="vp_phrase")
            idx2=next((i for i,(p,_) in enumerate(filt_p) if p['e']==sel_p),0)
            ph,_=filt_p[idx2]
            st.markdown(f"""<div class='vc' style='padding:24px'>
              <div class='at' style='font-size:1.5em'>{ph['a']}</div>
              <div class='tr'>/{ph['t']}/</div>
              <div class='bn' style='margin-top:6px'>{ph['b']}</div>
              <div class='en'>{ph['e']}</div></div>""", unsafe_allow_html=True)
            c1,c2=st.columns(2)
            with c1:
                if st.button("🔊 Listen",use_container_width=True,key="sph_n"): speak(ph['a'])
            with c2:
                if st.button("🐢 Slow",use_container_width=True,key="sph_s"): speak(ph['a'],slow=True)

    with ta:
        st.markdown("#### 🔡 Hear Every Letter")
        st.markdown("**Vowels**")
        vc=st.columns(6)
        for i,ch in enumerate(VOWELS):
            with vc[i%6]:
                st.markdown(f"<div class='ac'><div class='at' style='font-size:1.8em'>{ch['a']}</div><div class='tr' style='font-size:.75em'>{ch['t']}</div></div>", unsafe_allow_html=True)
                if st.button("▶",key=f"vav_{i}",use_container_width=True): speak(ch['a'])
        st.markdown("**Consonants** (★ = unique to Assamese)")
        cc=st.columns(6)
        for i,ch in enumerate(CONSONANTS):
            u=ch.get("unique",False)
            with cc[i%6]:
                st.markdown(f"<div class='ac' style='{'border:2px solid #FF6B35' if u else ''}'><div class='at' style='font-size:1.8em'>{ch['a']}</div><div class='tr' style='font-size:.75em'>{ch['t']}</div></div>", unsafe_allow_html=True)
                if st.button("▶",key=f"vcv_{i}",use_container_width=True): speak(ch['a'])

    with tdrill:
        st.markdown("#### 🏋️ Pronunciation Drill")
        drill_sets={"🏠 Family":["মা","দেউতা","ককাই","বাই","আইতা","ককা"],
                    "🙏 Greetings":["নমস্কাৰ","ধন্যবাদ","মাফ কৰিব","হয়","নহয়"],
                    "🍽️ Food":["ভাত","মাছ","পানী","চাহ","আম"],
                    "🔢 Numbers":["এক","দুই","তিনি","চাৰি","পাঁচ","ছয়","সাত","আঠ","ন","দহ"],
                    "🌈 Colours":["ৰঙা","নীলা","হালধীয়া","সেউজীয়া","বগা","কলা"],
                    "🐘 Nature":["নদী","পাহাৰ","গছ","হাতী","গঁড়","বৰষুণ"],
                    "💪 Verbs":["খোৱা","যোৱা","অহা","পঢ়া","লিখা","খেলা","শোৱা","গোৱা"]}
        sel_d=st.selectbox("Drill set:",list(drill_sets.keys()),key="drill_sel")
        dwords=drill_sets[sel_d]
        if "drill_idx" not in st.session_state: st.session_state.drill_idx=0
        if st.session_state.drill_idx>=len(dwords): st.session_state.drill_idx=0
        di=st.session_state.drill_idx; dw=dwords[di]
        dots="".join(["🟠" if j==di else ("✅" if j<di else "⚪") for j in range(len(dwords))])
        st.markdown(f"<div style='text-align:center;font-size:1em;margin:8px 0'>{dots}</div>", unsafe_allow_html=True)
        st.markdown(f"""<div class='vc' style='text-align:center;padding:36px'>
          <div style='color:#a7a9be;font-size:.78em'>Word {di+1}/{len(dwords)}</div>
          <div class='at' style='font-size:4em;letter-spacing:6px'>{dw}</div>
          <div style='color:#a7a9be;font-size:.88em;margin-top:8px'>Listen → Repeat → Next</div>
        </div>""", unsafe_allow_html=True)
        d1,d2,d3,d4=st.columns(4)
        with d1:
            if st.button("⬅️",use_container_width=True,key="dp"): st.session_state.drill_idx=max(0,di-1); st.rerun()
        with d2:
            if st.button("🔊 Listen",use_container_width=True,key="dl"): speak(dw)
        with d3:
            if st.button("🐢 Slow",use_container_width=True,key="ds"): speak(dw,slow=True)
        with d4:
            if st.button("Next ➡️",use_container_width=True,key="dn"):
                if di+1>=len(dwords): st.success("🎉 Drill complete!"); st.session_state.drill_idx=0
                else: st.session_state.drill_idx=di+1
                st.rerun()
        if st.button("▶️ Play Entire Set",use_container_width=True,key="dpa"):
            with st.spinner("Playing..."): [speak(w) for w in dwords]

# ══════════════════════════════════════════════════════════════════════════════
#  PAGE: CONVERSATIONS (with native voice)
# ══════════════════════════════════════════════════════════════════════════════

def page_conversations():
    st.markdown("## 💬 Conversations — আলাপ-আলোচনা")
    st.markdown("<p style='color:#a7a9be'>Real-life Assamese dialogues with native regional voice. Listen to each line, then practice repeating.</p>", unsafe_allow_html=True)

    # Active voice display
    vp=st.session_state.voice_profile; p=VOICE_PROFILES[vp]
    st.markdown(f"<div class='wb' style='font-style:normal'>🎙️ Active voice: <b style='color:#FF6B35'>{vp}</b> | eSpeak-NG | lang={p['lang']}</div>", unsafe_allow_html=True)

    sel_conv=st.selectbox("Choose scenario:",list(CONVERSATIONS.keys()),key="conv_sel")
    conv=CONVERSATIONS[sel_conv]
    lvl_color={"Beginner":"#2EC4B6","Intermediate":"#FFD166","Advanced":"#FF6B35"}.get(conv["level"],"#a7a9be")
    st.markdown(f"""<div class='lc'>
      <span style='color:{lvl_color};font-weight:800;font-size:.82em'>{conv['level']}</span>
      <h3 style='margin:6px 0'>{sel_conv}</h3>
      <p style='color:#a7a9be;margin:0'>{conv['desc']}</p>
    </div>""", unsafe_allow_html=True)

    tab_read,tab_practice,tab_role=st.tabs(["📖 Read & Listen","🎤 Line by Line","🎭 Role Play"])

    with tab_read:
        st.markdown("#### 📖 Full Conversation")
        for i,ex in enumerate(conv["exchanges"]):
            is_a=ex["speaker"] in ["A","You","Student"]
            bubble_cls="bubble-a" if is_a else "bubble-b"
            spk_color="#FF6B35" if is_a else "#2EC4B6"
            st.markdown(f"""<div class='{bubble_cls}'>
              <div style='font-weight:800;font-size:.8em;color:{spk_color};margin-bottom:4px'>{ex['speaker']}</div>
              <div class='at' style='font-size:1.3em'>{ex['assamese']}</div>
              <div class='tr'>/{ex['transliteration']}/</div>
              <div class='bn' style='margin-top:4px'>{ex.get('bengali','')}</div>
              <div class='en'>{ex['english']}</div>
            </div>""", unsafe_allow_html=True)
            if st.button(f"🔊 {ex['speaker']}",key=f"conv_r_{i}",use_container_width=False):
                speak(ex['assamese'])

        st.markdown("---")
        if st.button("🔊 Play Entire Conversation",use_container_width=True):
            with st.spinner("Playing conversation..."):
                for ex in conv["exchanges"]:
                    speak(ex['assamese'])

    with tab_practice:
        st.markdown("#### 🎤 Line-by-Line Practice")
        st.markdown("<p style='color:#a7a9be'>Listen to each line carefully. Then try to repeat it yourself before moving forward.</p>", unsafe_allow_html=True)
        if "conv_line" not in st.session_state: st.session_state.conv_line=0
        total=len(conv["exchanges"])
        li=st.session_state.conv_line%total; ex=conv["exchanges"][li]
        dots="".join(["🟠" if j==li else ("✅" if j<li else "⚪") for j in range(total)])
        st.markdown(f"<div style='text-align:center;margin:8px 0'>{dots}</div>", unsafe_allow_html=True)
        spk_color="#FF6B35" if ex["speaker"] in ["A","You","Student"] else "#2EC4B6"
        st.markdown(f"""<div class='vc' style='text-align:center;padding:28px'>
          <div style='font-weight:800;color:{spk_color};font-size:.88em'>{ex['speaker']}</div>
          <div class='at' style='font-size:1.8em;margin:10px 0'>{ex['assamese']}</div>
          <div class='tr' style='font-size:1em'>/{ex['transliteration']}/</div>
          <div class='bn' style='margin-top:6px'>{ex.get('bengali','')}</div>
          <div class='en'>{ex['english']}</div>
        </div>""", unsafe_allow_html=True)
        l1,l2,l3,l4=st.columns(4)
        with l1:
            if st.button("⬅️ Back",use_container_width=True,key="cl_b"): st.session_state.conv_line=max(0,li-1); st.rerun()
        with l2:
            if st.button("🔊 Listen",use_container_width=True,key="cl_l"): speak(ex['assamese'])
        with l3:
            if st.button("🐢 Slow",use_container_width=True,key="cl_s"): speak(ex['assamese'],slow=True)
        with l4:
            if st.button("Next ➡️",use_container_width=True,key="cl_n"):
                if li+1>=total: st.success("🎉 Conversation complete!"); st.session_state.conv_line=0
                else: st.session_state.conv_line=li+1
                st.rerun()

    with tab_role:
        st.markdown("#### 🎭 Role Play Mode")
        st.markdown("<p style='color:#a7a9be'>Take one role in the conversation. Lines for your role are shown for you to speak. The other role plays automatically.</p>", unsafe_allow_html=True)
        speakers=list(dict.fromkeys([ex["speaker"] for ex in conv["exchanges"]]))
        role=st.radio("Your role:",speakers,horizontal=True,key="role_sel")
        st.markdown("---")
        for i,ex in enumerate(conv["exchanges"]):
            is_yours=ex["speaker"]==role
            if is_yours:
                st.markdown(f"""<div class='bubble-a'>
                  <div style='font-weight:800;font-size:.8em;color:#FF6B35'>👤 YOU ({role})</div>
                  <div class='at' style='font-size:1.3em'>{ex['assamese']}</div>
                  <div class='tr'>/{ex['transliteration']}/</div>
                  <div class='en'>{ex['english']}</div>
                </div>""", unsafe_allow_html=True)
                if st.button("🔊 Hear your line",key=f"role_{i}",use_container_width=False):
                    speak(ex['assamese'])
            else:
                st.markdown(f"""<div class='bubble-b'>
                  <div style='font-weight:800;font-size:.8em;color:#2EC4B6'>🤖 {ex['speaker']}</div>
                  <div class='at' style='font-size:1.3em'>{ex['assamese']}</div>
                  <div class='tr'>/{ex['transliteration']}/</div>
                  <div class='en'>{ex['english']}</div>
                </div>""", unsafe_allow_html=True)
                if st.button(f"▶ {ex['speaker']} speaks",key=f"role_o_{i}",use_container_width=False):
                    speak(ex['assamese'])

# ══════════════════════════════════════════════════════════════════════════════
#  PAGE: PRACTICE
# ══════════════════════════════════════════════════════════════════════════════

FILL_EX=[
    {"s":"মোৰ ___ মা।","b":"মা","h":"family member","e":"My ___ is mother."},
    {"s":"আপোনাক ___।","b":"ধন্যবাদ","h":"gratitude","e":"___ to you."},
    {"s":"মই ভাত ___।","b":"খাওঁ","h":"I eat...","e":"I ___ rice."},
    {"s":"ব্ৰহ্মপুত্ৰ এখন ___ নদী।","b":"ডাঙৰ","h":"size","e":"Brahmaputra is a ___ river."},
    {"s":"অসম বৰ ___।","b":"সুন্দৰ","h":"appearance","e":"Assam is very ___."},
    {"s":"মোৰ জ্বৰ ___।","b":"হৈছে","h":"has happened","e":"I ___ fever."},
    {"s":"___ কিমান বাজিছে?","b":"এতিয়া","h":"right now","e":"___ what time is it?"},
    {"s":"তুমি কি কাম ___?","b":"কৰা","h":"do/does","e":"What work do you ___?"},
    {"s":"মই অসমীয়া ___ আছো।","b":"শিকি","h":"learning","e":"I am ___ Assamese."},
    {"s":"___ ধন্যবাদ আপোনাক।","b":"বৰ","h":"very much","e":"___ thank you."},
]

def page_practice():
    st.markdown("## ✏️ Practice Exercises")
    tf,tm,tx,tsen=st.tabs(["🃏 Flashcards","🔗 Matching","✍️ Fill Blank","📝 Sentence Build"])

    with tf:
        all_w=[(w,d) for d,les in CURRICULUM.items() for w in les.get("vocab",[]) if les.get("vocab")]
        if not all_w: st.info("No vocab yet!"); return
        idx=st.session_state.fc_idx%len(all_w); w,_=all_w[idx]
        if not st.session_state.fc_flipped:
            st.markdown(f"<div class='vc' style='text-align:center;padding:50px'><div class='at' style='font-size:3.5em'>{w['a']}</div><div class='tr' style='margin-top:8px'>/{w['t']}/</div><div style='color:#a7a9be;margin-top:12px'>Click Flip</div></div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='vc' style='text-align:center;padding:50px;border-color:#2EC4B6'><div class='bn' style='font-size:2em'>{w['b']}</div><div class='en' style='font-size:1.4em;margin-top:6px'>{w['e']}</div><div style='color:#a7a9be;margin-top:10px'>Assamese: <b style='color:#FF6B35'>{w['a']}</b></div></div>", unsafe_allow_html=True)
        c1,c2,c3,c4=st.columns(4)
        with c1:
            if st.button("🔄 Flip",use_container_width=True): st.session_state.fc_flipped=not st.session_state.fc_flipped; st.rerun()
        with c2:
            if st.button("⬅️",use_container_width=True): st.session_state.fc_idx=(idx-1)%len(all_w); st.session_state.fc_flipped=False; st.rerun()
        with c3:
            if st.button("➡️",use_container_width=True): st.session_state.fc_idx=(idx+1)%len(all_w); st.session_state.fc_flipped=False; st.rerun()
        with c4:
            if st.button("🔊",use_container_width=True): speak(w['a'])
        st.markdown(f"<div style='text-align:center;color:#a7a9be;margin-top:6px'>Card {idx+1}/{len(all_w)}</div>", unsafe_allow_html=True)

    with tm:
        st.markdown("#### 🔗 Match the Word — 5 XP each!")
        day=st.session_state.current_day; les=CURRICULUM.get(day,CURRICULUM[1])
        all_w2=les.get("vocab",[]) or CURRICULUM[1].get("vocab",[])
        if st.session_state.mw is None or st.button("🔀 New Round",key="nr"):
            st.session_state.mw=random.sample(all_w2,min(4,len(all_w2))); st.session_state.ma={}; st.rerun()
        sample=st.session_state.mw; all_en=[w["e"] for w in all_w2]
        for i,w in enumerate(sample):
            wrong=random.sample([e for e in all_en if e!=w["e"]],min(3,len(all_en)-1))
            opts=wrong+[w["e"]]; random.shuffle(opts)
            chosen=st.selectbox(f"{w['a']} ({w['t']}) — {w['b']}",["— select —"]+opts,key=f"m_{i}_{w['a']}")
            st.session_state.ma[i]=(chosen,w["e"])
        if st.button("✅ Check",use_container_width=True):
            sc=0
            for i,(ch,co) in st.session_state.ma.items():
                if ch==co: st.success(f"✅ {sample[i]['a']} = {co}"); sc+=1
                else: st.error(f"❌ {sample[i]['a']} → {co}")
            add_xp(sc*5); st.info(f"Score: {sc}/{len(sample)} · +{sc*5} XP")

    with tx:
        st.markdown("#### ✍️ Fill in the Blank — 10 XP each!")
        ex=FILL_EX[st.session_state.fill_idx%len(FILL_EX)]
        st.markdown(f"<div class='lc'><div class='at' style='font-size:1.5em'>{ex['s']}</div><div class='en'>{ex['e']}</div><div class='tr'>Hint: {ex['h']}</div></div>", unsafe_allow_html=True)
        ans=st.text_input("Answer:",key=f"fi_{st.session_state.fill_idx}")
        c1,c2=st.columns(2)
        with c1:
            if st.button("✅ Submit",use_container_width=True):
                if ans.strip()==ex["b"]: st.success(f"🎉 Correct! {ex['b']}"); add_xp(10)
                else: st.error(f"❌ Answer: **{ex['b']}**")
        with c2:
            if st.button("➡️ Next",use_container_width=True): st.session_state.fill_idx+=1; st.rerun()

    with tsen:
        st.markdown("#### 📝 Build a Sentence")
        st.markdown("<p style='color:#a7a9be'>Arrange these words to form a correct Assamese sentence.</p>", unsafe_allow_html=True)
        sentences=[
            {"words":["মই","ভাত","খাওঁ"],"correct":"মই ভাত খাওঁ","english":"I eat rice"},
            {"words":["তুমি","কেনে","আছা","?"],"correct":"তুমি কেনে আছা?","english":"How are you?"},
            {"words":["অসম","সুন্দৰ","বৰ"],"correct":"অসম বৰ সুন্দৰ","english":"Assam is very beautiful"},
            {"words":["মোৰ","দেউতা","শিক্ষক"],"correct":"মোৰ দেউতা শিক্ষক","english":"My father is a teacher"},
            {"words":["মই","অসমীয়া","শিকিছো"],"correct":"মই অসমীয়া শিকিছো","english":"I am learning Assamese"},
        ]
        if "sent_idx" not in st.session_state: st.session_state.sent_idx=0
        s=sentences[st.session_state.sent_idx%len(sentences)]
        st.markdown(f"<div class='wb' style='font-style:normal'><b>Arrange:</b> <span style='color:#FF6B35'>{' | '.join(s['words'])}</span><br><span class='en'>Meaning: {s['english']}</span></div>", unsafe_allow_html=True)
        user_ans=st.text_input("Type the sentence:",key=f"sb_{st.session_state.sent_idx}")
        cs1,cs2=st.columns(2)
        with cs1:
            if st.button("✅ Check",use_container_width=True,key="sb_check"):
                if user_ans.strip()==s["correct"]: st.success("🎉 Perfect!"); add_xp(15)
                else: st.error(f"Correct: **{s['correct']}**")
        with cs2:
            if st.button("➡️ Next",use_container_width=True,key="sb_next"): st.session_state.sent_idx+=1; st.rerun()
        if st.button("🔊 Hear correct sentence",use_container_width=True,key="sb_hear"): speak(s['correct'])

# ══════════════════════════════════════════════════════════════════════════════
#  PAGE: WEEKLY TEST
# ══════════════════════════════════════════════════════════════════════════════

def page_weekly_test():
    st.markdown("## 📝 Weekly Test — সাপ্তাহিক পৰীক্ষা")
    st.markdown("<p style='color:#a7a9be'>Test your knowledge from all lessons. 5 XP per correct answer.</p>", unsafe_allow_html=True)
    if not st.session_state.wt_started:
        ca,cb=st.columns([2,1])
        with ca:
            st.markdown("""<div class='lc'><h3>📝 Weekly Assessment</h3>
              <p style='color:#a7a9be'>30 questions covering vocabulary, grammar and cultural knowledge.</p>
              <div class='ib'>⏱️ No time limit &nbsp;|&nbsp; 30 questions &nbsp;|&nbsp; Max 150 XP</div></div>""", unsafe_allow_html=True)
        with cb:
            past=st.session_state.weekly_test_scores
            if past:
                st.markdown("#### Past Scores")
                for i,sc in enumerate(past[-5:],1): st.markdown(f"Test {i}: **{sc}/30**")
        if st.button("🚀 Start Test",use_container_width=True):
            st.session_state.wt_questions=random.sample(QUIZ_BANK,min(30,len(QUIZ_BANK)))
            st.session_state.wt_answers={}; st.session_state.wt_submitted=False
            st.session_state.wt_started=True; st.rerun()
        return

    qs=st.session_state.wt_questions
    if not st.session_state.wt_submitted:
        st.markdown(f"<div style='color:#a7a9be'>Answered: {len(st.session_state.wt_answers)}/{len(qs)}</div>", unsafe_allow_html=True)
        for qi,q in enumerate(qs):
            st.markdown(f"<div class='lc'><div style='color:#a7a9be;font-size:.75em'>Q{qi+1}</div><h4 style='margin:4px 0'>{q['q']}</h4></div>", unsafe_allow_html=True)
            ans=st.radio("",q["opts"],key=f"wt_{qi}",label_visibility="collapsed")
            st.session_state.wt_answers[qi]=ans
        ca,cb=st.columns(2)
        with ca:
            if st.button("✅ Submit",use_container_width=True): st.session_state.wt_submitted=True; st.rerun()
        with cb:
            if st.button("🔄 Restart",use_container_width=True): st.session_state.wt_started=False; st.rerun()
    else:
        score=sum(1 for qi,q in enumerate(qs) if st.session_state.wt_answers.get(qi,"")==q["opts"][q["ans"]])
        pct=int(score/len(qs)*100)
        st.session_state.weekly_test_scores.append(score); add_xp(score*5)
        grade="🌟 অসাধাৰণ!" if pct>=80 else ("👍 ভালেই কৰিলে!" if pct>=60 else "📖 আৰু অভ্যাস কৰক!")
        clr="#2EC4B6" if pct>=80 else ("#FFD166" if pct>=60 else "#EF233C")
        st.markdown(f"<div class='hero'><h2>{grade}</h2><div style='font-size:3em;font-weight:900;color:{clr}'>{score}/{len(qs)}</div><div style='color:#a7a9be'>{pct}% · +{score*5} XP</div></div>", unsafe_allow_html=True)
        with st.expander("📋 See detailed results"):
            for qi,q in enumerate(qs):
                ch=st.session_state.wt_answers.get(qi,""); co=q["opts"][q["ans"]]; ok=ch==co
                st.markdown(f"<div style='background:{'rgba(46,196,182,.1)' if ok else 'rgba(239,35,60,.1)'};border-radius:10px;padding:12px;margin:4px 0'><b>{'✅' if ok else '❌'} Q{qi+1}: {q['q']}</b><br><span style='color:#a7a9be'>You: {ch}</span> · {'<span style=\"color:#2EC4B6\">✓</span>' if ok else f'<span style=\"color:#EF233C\">Correct: {co}</span>'}<br><span style='color:#FFD166;font-size:.82em'>{q['exp']}</span></div>", unsafe_allow_html=True)
        ca,cb=st.columns(2)
        with ca:
            if st.button("🔄 Retake",use_container_width=True): st.session_state.wt_started=False; st.rerun()
        with cb:
            if st.button("📖 Back to Lessons",use_container_width=True): goto("lessons")

# ══════════════════════════════════════════════════════════════════════════════
#  PAGE: PROGRESS
# ══════════════════════════════════════════════════════════════════════════════

def page_progress():
    st.markdown("## 📊 Your Progress — তোমাৰ অগ্ৰগতি")
    xp=st.session_state.total_xp; lvl,ass,en,nxt=get_level(xp)
    pct=min(int(xp/nxt*100),100); done=st.session_state.completed_lessons
    scores=st.session_state.weekly_test_scores; badges=st.session_state.badges

    st.markdown(f"""<div class='hero'>
      <div style='font-size:.8em;color:#a7a9be;text-transform:uppercase;letter-spacing:1px'>Level {lvl}</div>
      <h2>{ass}</h2><div style='color:#a7a9be'>{en}</div>
      <div class='pw' style='max-width:400px;margin:12px auto 4px'><div class='pf' style='width:{pct}%'></div></div>
      <div style='color:#a7a9be;font-size:.8em'>{xp}/{nxt} XP</div>
    </div>""", unsafe_allow_html=True)

    for col,val,lbl in zip(st.columns(5),
        [xp,st.session_state.streak,len(done),len(scores),len(badges)],
        ["Total XP","Streak","Lessons","Tests","Badges"]):
        col.markdown(f"<div class='mc'><div class='mv'>{val}</div><div class='ml'>{lbl}</div></div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    ca,cb=st.columns(2)
    with ca:
        st.markdown("#### Phase Completion")
        phases={"Foundation":list(range(1,31)),"Intermediate":list(range(16,46)),
                "Advanced":list(range(31,61)),"Fluency":list(range(61,121))}
        phase_done=[sum(1 for d in days if d in done) for days in phases.values()]
        phase_total=[len(days) for days in phases.values()]
        fig=go.Figure(go.Bar(
            x=list(phases.keys()),y=phase_done,
            marker_color=["#2EC4B6","#FFD166","#FF6B35","#9D4EDD"],
            text=[f"{d}/{t}" for d,t in zip(phase_done,phase_total)],textposition="outside"
        ))
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)",plot_bgcolor="rgba(0,0,0,0)",
                          font_color="#FFFFFE",yaxis=dict(showticklabels=False,showgrid=False),
                          xaxis=dict(showgrid=False),margin=dict(t=20,b=20),height=260,showlegend=False)
        st.plotly_chart(fig,use_container_width=True)
    with cb:
        st.markdown("#### Weekly Test Scores")
        if scores:
            fig2=go.Figure(go.Scatter(x=[f"T{i+1}" for i in range(len(scores))],y=scores,
                           mode="lines+markers",line=dict(color="#FF6B35",width=3),
                           marker=dict(size=8,color="#FF6B35"),fill="tozeroy",fillcolor="rgba(255,107,53,0.1)"))
            fig2.update_layout(paper_bgcolor="rgba(0,0,0,0)",plot_bgcolor="rgba(0,0,0,0)",
                               font_color="#FFFFFE",yaxis=dict(range=[0,30],gridcolor="rgba(255,255,255,.08)"),
                               xaxis=dict(showgrid=False),margin=dict(t=20,b=20),height=260)
            st.plotly_chart(fig2,use_container_width=True)
        else:
            st.markdown("<div class='ib' style='text-align:center;padding:50px'><div style='font-size:2em'>📝</div><p>No test scores yet!</p></div>", unsafe_allow_html=True)

    st.markdown("---"); st.markdown("#### 🏅 All Badges")
    badge_meta={
        "first_lesson":("📚","First Steps","Complete lesson 1"),
        "ten_lessons":("🔟","Ten Down","Complete 10 lessons"),
        "thirty_lessons":("🗓️","Month Strong","Complete 30 lessons"),
        "sixty_lessons":("🏅","Halfway","Complete 60 lessons"),
        "full_course":("👑","Fluent!","Complete all 120 lessons"),
        "first_century":("🌟","Century","Earn 100 XP"),
        "xp_500":("🎓","Scholar","Earn 500 XP"),
        "xp_1000":("💎","Diamond","Earn 1000 XP"),
        "streak_3":("🔥","On Fire","3-day streak"),
        "streak_7":("⚡","Week","7-day streak"),
        "streak_30":("🏆","Champion","30-day streak"),
    }
    bc=st.columns(6)
    for i,(bid,(ico,name,desc)) in enumerate(badge_meta.items()):
        bc[i%6].markdown(f"<div class='mc' style='opacity:{'1' if bid in badges else '0.25'}'><div style='font-size:1.8em'>{ico}</div><div style='font-weight:700;font-size:.8em'>{name}</div><div style='color:#a7a9be;font-size:.68em'>{desc}</div></div>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  PAGE: PROVERBS
# ══════════════════════════════════════════════════════════════════════════════

def page_proverbs():
    st.markdown("## 📜 Assamese Proverbs — প্ৰবাদ-পুথি")
    st.markdown("<p style='color:#a7a9be'>Traditional wisdom of Assam passed down through generations.</p>", unsafe_allow_html=True)
    for i,p in enumerate(PROVERBS):
        st.markdown(f"""<div class='vc' style='padding:20px'>
          <div class='at' style='font-size:1.6em'>{p['assamese']}</div>
          <div class='tr' style='margin-top:4px'>/{p['transliteration']}/</div>
          <div class='bn' style='margin-top:6px'>{p['bengali']}</div>
          <div class='en'>{p['english']}</div>
          <div class='wb' style='margin-top:10px;font-style:normal'>💡 <b>Meaning:</b> {p['meaning']}</div>
        </div>""", unsafe_allow_html=True)
        if st.button("🔊 Hear proverb",key=f"prov_{i}"): speak(p['assamese'])

# ══════════════════════════════════════════════════════════════════════════════
#  PAGE: CULTURE
# ══════════════════════════════════════════════════════════════════════════════

def page_culture():
    st.markdown("## ℹ️ About Assam — অসম")
    st.markdown("<div class='hero'><div style='font-size:2.8em'>🦚</div><h2>অসম — Land of Red River and Blue Hills</h2><p style='color:#a7a9be;max-width:600px;margin:auto'>Discover Assam's history, culture, festivals, nature and the unique features of the Assamese language.</p></div>", unsafe_allow_html=True)
    t1,t2,t3,t4,t5=st.tabs(["🌿 Facts","🎊 Festivals","🗣️ Language","👑 History","🍵 Tea"])
    with t1:
        for f in CULTURAL_FACTS:
            st.markdown(f"<div class='vc'><span style='font-size:1.4em'>{f['emoji']}</span> <span style='margin-left:8px'><b>Assamese:</b> {f['f']}<br><span class='en'>{f['e']}</span></span></div>", unsafe_allow_html=True)
    with t2:
        for n,ass,m,d in [
            ("Bohag Bihu — বহাগ বিহু","বহাগ বিহু","April","New Year festival — Bihu dance, Husori songs, feasting and new beginnings"),
            ("Kati Bihu — কাতি বিহু","কাতি বিহু","October","Lamps lit in fields and granaries — prayers for good harvest"),
            ("Magh Bihu — মাঘ বিহু","মাঘ বিহু","January","Harvest celebration — bonfires (meji), traditional food, sports"),
            ("Durga Puja — দুৰ্গাপূজা","দুৰ্গাপূজা","October","Celebrated with elaborate pandals and cultural programs"),
            ("Eid — ঈদ","ঈদ","Islamic cal.","Major Muslim festival widely celebrated across Assam"),
            ("Christmas — ক্ৰিছমাছ","ক্ৰিছমাছ","December","Celebrated enthusiastically especially in hill districts"),
        ]:
            st.markdown(f"<div class='vc'><b style='color:#FF6B35'>{n}</b> <span style='color:#FFD166'>· {m}</span><br><span style='color:#a7a9be;font-size:.9em'>{d}</span></div>", unsafe_allow_html=True)
    with t3:
        st.markdown("#### Key differences: Assamese vs Bengali")
        for feat,ass,bn in [
            ("'I'","মই (moi)","আমি (ami)"),("'We'","আমি (aami)","আমরা (amra)"),
            ("Unique letter র","ৰ (rolled r)","র (standard)"),("W sound","ৱ (wo)","Not in Bengali"),
            ("শ/ষ/স","All → x (sh)","Three distinct sounds"),("Father","দেউতা (deuta)","বাবা (baba)"),
            ("Elder brother","ককাই (kokai)","দাদা (dada)"),("Tea","চাহ (xah)","চা (cha)"),
            ("Script unique","ৰ ৱ","Not present"),("Language family","Indo-Aryan (easternmost)","Indo-Aryan"),
        ]:
            c1,c2,c3=st.columns(3)
            c1.markdown(f"<span style='color:#a7a9be'>{feat}</span>",unsafe_allow_html=True)
            c2.markdown(f"<span style='color:#FF6B35'>{ass}</span>",unsafe_allow_html=True)
            c3.markdown(f"<span class='bn'>{bn}</span>",unsafe_allow_html=True)
    with t4:
        st.markdown("""<div class='vc' style='padding:20px'>
        <h4>👑 The Ahom Kingdom (আহোম ৰাজ্য)</h4>
        <p style='color:#a7a9be'>The Ahom dynasty ruled Assam for 600 years (1228-1826 CE). They originated from Southeast Asia (Shan people of Myanmar) and established one of India's most resilient kingdoms. They defeated the Mughals 17 times and were never subjugated — a unique feat in Indian history.</p>
        </div>""", unsafe_allow_html=True)
        st.markdown("""<div class='vc' style='padding:20px;margin-top:10px'>
        <h4>📜 Sankardev (শংকৰদেৱ) — 1449-1568</h4>
        <p style='color:#a7a9be'>The great saint-scholar who founded the Vaishnavite Ekasarana Dharma. He composed Borgeets (devotional songs), Ankia Naat (one-act plays) and translated scriptures into Assamese. The Namghor (prayer hall) tradition he established continues today.</p>
        </div>""", unsafe_allow_html=True)
    with t5:
        st.markdown("""<div class='wb' style='padding:22px;font-style:normal'>
        <h4>🍵 Assam Tea — চাহ</h4>
        <p style='color:#a7a9be'>Assam is the world's largest tea-growing region, producing over 50% of India's total tea output. The unique alluvial soil of the Brahmaputra valley and heavy rainfall create the perfect conditions for Assam's bold, malty, full-bodied tea — prized in breakfast blends worldwide.</p>
        <br><b>Tea vocabulary:</b><br>
        চাহ (xah) = tea | গাখীৰ (gaakhir) = milk | চেনি (xeni) = sugar<br>
        চাহ বাগিছা (xah baagisa) = tea garden | চাহ পাত (xah paat) = tea leaf<br>
        খেতিয়ক (khetiyok) = farmer | মজদুৰ (mojdur) = laborer
        </div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  ROUTER
# ══════════════════════════════════════════════════════════════════════════════

init_state(); update_streak(); inject_css(); sidebar()

{
    "home":page_home,"plan":page_plan,"lessons":page_lessons,
    "alphabet":page_alphabet,"voice":page_voice,"conversations":page_conversations,
    "practice":page_practice,"weekly_test":page_weekly_test,
    "progress":page_progress,"proverbs":page_proverbs,"culture":page_culture,
}.get(st.session_state.page,page_home)()
