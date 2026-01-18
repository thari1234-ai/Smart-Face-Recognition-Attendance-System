# Smart-Face-Recognition-Attendance-System
---

#  Face-Based Attendance Management System

A **Streamlit-based web application** that captures student photos using a webcam and records attendance with **Name, Roll Number, Date, Time, and Image**.
The system prevents **duplicate attendance for the same student on the same day**.

---

##  Features

*  Capture student photo using webcam
*  Input **Name** and **Roll Number**
*  Automatically stores **Date & Time**
*  Prevents **duplicate attendance on the same day**
*  Aesthetic UI with transparent glassmorphism design
*  Stores captured images locally
*  Saves attendance records in a CSV file
*  Displays motivational quotes after attendance is marked

---

##  Technologies Used

* **Python 3**
* **Streamlit**
* **Pandas**
* **HTML & CSS (via Streamlit markdown)**

---

## 📂 Project Structure

```
attendance_opencv/
│
├── appp.py               # Main Streamlit application
├── attendance.csv        # Attendance records (auto-created)
├── captures/             # Captured images folder
├── README.md             # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Install Python

Make sure Python **3.9 or above** is installed.

Check:

```bash
python --version
```

---

### 2️⃣ Install Required Libraries

Run this in **Command Prompt / PowerShell**:

```bash
pip install streamlit pandas pillow
```

---

### 3️⃣ Run the Application

Navigate to the project folder:

```bash
cd path/to/attendance_opencv
```

Run:

```bash
streamlit run appp.py
```

The app will open automatically in your browser 🌐

---

##  How It Works

1. Enter **Name** and **Roll Number**
2. Capture photo using webcam
3. Click **Capture Attendance**
4. Attendance is recorded with:

   * Name
   * Roll Number
   * Date
   * Time
   * Image
5. If the same student tries again **on the same day**, attendance is blocked

---

##  Attendance Storage Format

Attendance is saved in `attendance.csv` with columns:

```
Name | Roll No | Date | Time | Image
```

---

##  Example Use Case

> Tharini (Roll No: E24AI049) can mark attendance **only once per day**.
> She can mark attendance again **the next day**.

---
##  Developed By

**Tharini**
 Student Project

---
🔗 **Live Application Access:** http://192.168.1.3:8501

