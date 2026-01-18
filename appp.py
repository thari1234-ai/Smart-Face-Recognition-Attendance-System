import streamlit as st
from PIL import Image
import pandas as pd
from datetime import datetime
import os
import random
st.markdown(
    """
    <style>
    /* Background */
    .stApp {
        background-image: url("https://images.template.net/356848/White-Cloud-Background-Aesthetic-edit-online-2.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* TRANSPARENT GLASS CARD */
    .block-container {
        background-color: rgba(255, 245, 235, 0.55);
        backdrop-filter: blur(10px);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.15);
    }

    /* MAIN TEXT COLORS */
    html, body, [class*="css"] {
        color: #4b0f1b !important;
    }

    h1, h2, h3, h4 {
        color: #6a1b2d !important;
        font-weight: 700;
    }

    /* Subtitle text */
    .subtitle {
        color: #6a1b2d;
        font-size: 18px;
        font-weight: 600;
        margin-bottom: 1rem;
    }

    label {
        color: #4b0f1b !important;
        font-weight: 600;
    }

    /* INPUT BOXES – BEIGE */
    input {
        background-color: #f6e7d8 !important;
        color: #4b0f1b !important;
        border-radius: 10px !important;
        border: 1px solid #c9a27d !important;
        padding: 0.5em;
        font-weight: 600;
    }

    /* CAMERA FRAME */
    video {
        border-radius: 14px;
        border: 3px solid #7b1e3a;
    }

    /* BUTTONS */
    .stButton > button {
        background-color: #7b1e3a;
        color: white;
        border-radius: 12px;
        border: none;
        padding: 0.6em 1.4em;
        font-size: 16px;
        font-weight: 600;
    }
    /* Attendance record text */
.attendance-text {
    color: #6a1b2d;              /* Burgundy */
    font-size: 16px;
    font-weight: 600;
    background-color: rgba(245, 225, 210, 0.65);
    padding: 10px 14px;
    border-radius: 14px;
    margin-bottom: 10px;
    border-left: 4px solid #7b1e3a;
}

/* Quote styling */
.quote-box {
    color: #5b1022;                 /* Dark burgundy */
    font-size: 17px;
    font-style: italic;
    font-weight: 600;
    background-color: rgba(245, 225, 210, 0.7);
    padding: 14px 18px;
    margin-top: 12px;
    border-radius: 16px;
    text-align: center;
    border: 1px solid #7b1e3a;
}

    .stButton > button:hover {
        background-color: #4b0f1b;
        transform: scale(1.03);
        transition: 0.2s ease-in-out;
    }

    /* QUOTE BOX (INFO) */
    .stAlert-info {
        background-color: rgba(246, 231, 216, 0.85);
        color: #4b0f1b !important;
        font-weight: 600;
        border-left: 6px solid #7b1e3a;
    }

    /* SUCCESS MESSAGE */
    .stAlert-success {
        background-color: rgba(246, 231, 216, 0.85);
        color: #4b0f1b !important;
        border-left: 6px solid #7b1e3a;
    }

    /* ERROR MESSAGE */
    .stAlert-error {
        background-color: rgba(180, 60, 60, 0.2);
        color: #4b0f1b !important;
        border-left: 6px solid #7b1e3a;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# CONFIG
# -----------------------------
CSV_FILE = "attendance.csv"
CAPTURE_FOLDER = "captures"
QUOTES = [
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "Do something today that your future self will thank you for.",
    "Small steps every day lead to big results.",
    "Your only limit is your mind."
]

os.makedirs(CAPTURE_FOLDER, exist_ok=True)

# -----------------------------
# UI
# -----------------------------
st.title("📸 Face Attendance System")
st.markdown(
    "<p class='subtitle'>Enter your Name and Roll Number, click Capture, and your attendance will be marked!</p>",
    unsafe_allow_html=True
)


name = st.text_input("Enter Name")
roll_no = st.text_input("Enter Roll Number")

img_file_buffer = st.camera_input("Take your photo")
# -----------------------------
# CAPTURE LOGIC
# -----------------------------
if st.button("Capture Attendance"):
    if name.strip() == "" or roll_no.strip() == "":
        st.error("Please enter both Name and Roll Number!")
    elif img_file_buffer is None:
        st.error("Please take a photo!")
    else:
        # Load existing CSV
        if os.path.exists(CSV_FILE):
            df = pd.read_csv(CSV_FILE)
        else:
            df = pd.DataFrame(columns=["Name", "Roll No", "Date", "Time", "Image"])

        # Check if this Name + Roll No already exists today
        today_date = datetime.now().strftime("%Y-%m-%d")
        if ((df["Name"] == name) & (df["Roll No"] == roll_no) & (df["Date"] == today_date)).any():
            st.markdown(
                f"""
                <div style="
                    color: #b00000;        
                    font-weight: 700;
                    background-color: rgba(255, 235, 235, 0.6);  
                    padding: 10px 15px;
                    border-radius: 10px;
                    border: 2px solid #b00000;
                ">
                    Attendance for <b>{name}</b> (Roll No: <b>{roll_no}</b>) is already marked today!
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            # Save image
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            img_filename = f"{CAPTURE_FOLDER}/{name}_{roll_no}_{timestamp}.png"
            img = Image.open(img_file_buffer)
            img.save(img_filename)

            # Add new record
            new_record = {
                "Name": name,
                "Roll No": roll_no,
                "Date": today_date,
                "Time": datetime.now().strftime("%H:%M:%S"),
                "Image": img_filename
            }
            df = pd.concat([df, pd.DataFrame([new_record])], ignore_index=True)
            df.to_csv(CSV_FILE, index=False)

            st.success(f"Attendance marked for {name} at {new_record['Time']} on {new_record['Date']}!")
            st.image(img, width=400)
            st.markdown(
                f"""
                <div class="quote-box">
                    “{random.choice(QUOTES)}”
                </div>
                """,
                unsafe_allow_html=True
            )

# -----------------------------
# SHOW RECORDS
# -----------------------------
st.markdown("### 📋 Attendance Records")

if os.path.exists(CSV_FILE):
    df = pd.read_csv(CSV_FILE)
    if not df.empty:
        for _, row in df.iterrows():
            img_path = row.get("Image", "")
            if isinstance(img_path, str) and os.path.exists(img_path):
                st.image(Image.open(img_path), width=200)
            st.markdown(
    f"""
    <div class="attendance-text">
        <b>Name:</b> {row['Name']} &nbsp; | &nbsp;
        <b>Roll No:</b> {row['Roll No']} &nbsp; | &nbsp;
        <b>Date:</b> {row['Date']} &nbsp; | &nbsp;
        <b>Time:</b> {row['Time']}
    </div>
    """,
    unsafe_allow_html=True
)
            st.markdown("---")  
    else:
        st.write("No attendance recorded yet.")
else:
    st.write("No attendance recorded yet.")
# Load existing CSV
# -----------------------------
# Load existing CSV and handle old records
# -----------------------------
if os.path.exists(CSV_FILE):
    df = pd.read_csv(CSV_FILE)
    if 'Date' not in df.columns:
        df['Date'] = ""  # add Date column for old records
else:
    df = pd.DataFrame(columns=["Name", "Roll No", "Date", "Time", "Image"])
