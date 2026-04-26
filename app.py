import streamlit as st
import random
import os
from PIL import Image
import base64
import time

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Arpana's OS 💖",
    page_icon="💖",
    layout="centered"
)

# ------------------ CUSTOM MOBILE STYLING ------------------
st.markdown("""
    <style>
    .stButton button {
        width: 100%;
        border-radius: 12px;
        height: 3em;
        font-size: 16px;
    }
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------ MUSIC PLAYER ------------------
st.subheader("🎧 Play something nice")

music_folder = "music"

def autoplay_audio(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        audio_html = f"""
        <audio controls autoplay loop style="width:100%;">
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """
        st.markdown(audio_html, unsafe_allow_html=True)

if os.path.exists(music_folder):
    tracks = [f for f in os.listdir(music_folder) if f.endswith(".mp3")]

    if tracks:
        selected_track = st.selectbox("Choose a song 💖", tracks)
        if st.button("▶️ Play"):
            autoplay_audio(os.path.join(music_folder, selected_track))
    else:
        st.write("No music found 🎶")
else:
    st.write("Add a 'music/' folder with mp3 files")

st.divider()

# ------------------ HEADER ------------------
st.title("💖 Arpana's OS")
st.caption("Running smoothly since you walked in 😌")

# Smooth 3-second loading bar
progress_bar = st.progress(0)

for i in range(101):
    progress_bar.progress(i)
    time.sleep(0.03)  # 0.03 * 100 ≈ 3 seconds

st.success("Happiness loaded: 100%")
st.divider()


# ------------------ SYSTEM STATS ------------------
st.subheader("📊 System Status")
st.write("**Happiness Level:** 100%")
st.write("**Annoyance Tolerance:** Infinite (for you only)")
st.write("**Favorite Person:** You 😄")

st.divider()

# ------------------ MOOD CONTROL ------------------
st.subheader("🎮 Mood Control Panel")

responses = {
    "laugh": [
        "Why did I fall for you? Because gravity is strong, but you're stronger 😌",
        "System update: You are officially too cute 😤",
        "Mood boosted instantly because of you"
    ],
    "calm": [
        "Calm mode 🌙 Everything feels better when you're around.",
        "Peace + you = perfect combination 😌"
    ],
    "angry": [
        "⚠️ cutiepie angry detected\nInitiating apology.exe...\nStep 1: Say sorry\nStep 2: Offer chocolate 🍫",
        "Even now… still cute 😤💖"
    ],
    "attention": [
        "⚠️ Love needs attention\nAll tasks paused. Priority: YOU 💖",
        "Reminder: You deserve attention always 😌"
    ],
    "sleepy": [
        "Sleepy mode 😴 Time to rest",
        "Low battery… recharge with naps 💖"
    ]
}

if st.button("😄 Make me laugh"):
    st.info(random.choice(responses["laugh"]))

if st.button("😌 Calm mode"):
    st.success(random.choice(responses["calm"]))

if st.button("😡 Angry mode"):
    st.warning(random.choice(responses["angry"]))

if st.button("🥺 Need attention"):
    st.info(random.choice(responses["attention"]))

if st.button("😴 Sleepy mode"):
    st.write(random.choice(responses["sleepy"]))

st.divider()

# ------------------ COMPLIMENT ------------------
st.subheader("💌 Tap for something nice")

compliments = [
    "You're illegally cute 😤",
    "You make normal days feel better ✨",
    "You're my favorite notification",
    "Everything feels lighter with you around",
    "You're special. Simple as that."
]

if st.button("💖 Give me a compliment"):
    st.success(random.choice(compliments))

st.divider()

# ------------------ POEM GALLERY ------------------
st.subheader("📸 Something I made for you")

if st.button("Open poetry archive 👀"):
    folder = "poems"

    if os.path.exists(folder):
        images = sorted([f for f in os.listdir(folder) if f.endswith((".jpg", ".jpeg", ".png"))])

        if images:
            for img_file in images:
                img_path = os.path.join(folder, img_file)
                image = Image.open(img_path)
                st.image(image, use_container_width=True)
        else:
            st.write("No poems found 😅")
    else:
        st.write("Poems folder missing")

st.divider()

# ------------------ HIDDEN MESSAGE ------------------
st.subheader("🚫 Don't click this")

if st.button("👀 Don't click"):
    st.markdown("""
    Okay you clicked...

    I don't always say things properly,  
    but I really love having you in my life.  

    That's it. 😄
    """)
