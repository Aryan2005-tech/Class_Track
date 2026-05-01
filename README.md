<![CDATA[<div align="center">
  <img src="https://i.ibb.co/YTYGn5qV/logo.png" alt="Class Track Logo" width="120" />
  <h1>Class Track</h1>
  <p><strong>AI-Powered Classroom Attendance System</strong></p>
  <p>
    <img src="https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/Streamlit-1.x-FF4B4B?logo=streamlit&logoColor=white" alt="Streamlit" />
    <img src="https://img.shields.io/badge/Supabase-Database-3FCF8E?logo=supabase&logoColor=white" alt="Supabase" />
    <img src="https://img.shields.io/badge/dlib-Face_Recognition-008080" alt="dlib" />
  </p>
</div>

---

## 📌 About

**Class Track** is a smart attendance management system that uses **facial recognition** and **voice identification** to automate the attendance process in classrooms. Built with [Streamlit](https://streamlit.io/), it provides separate portals for teachers and students with a modern, polished UI.

- **Teachers** register with a username and password, create subjects, upload classroom photos or record audio, and let AI mark attendance automatically.
- **Students** register and log in using their face (FaceID), optionally enroll their voice, and join subjects via codes or shareable QR links.

---

## ✨ Features

### 🎓 Teacher Portal
| Feature | Description |
|---|---|
| **Account Management** | Register & login with username/password (bcrypt-hashed) |
| **Subject Management** | Create subjects with name, code & section |
| **Face-Based Attendance** | Upload classroom photos → AI detects & identifies enrolled students |
| **Voice-Based Attendance** | Record classroom audio → AI identifies students by voice |
| **QR Code Sharing** | Generate shareable QR codes & links for students to join a subject |
| **Attendance Records** | View historical attendance logs with present/total stats |

### 🧑‍🎓 Student Portal
| Feature | Description |
|---|---|
| **FaceID Login** | Register & log in using facial recognition (no passwords) |
| **Voice Enrollment** | Optionally record a voice sample during registration for voice attendance |
| **Subject Enrollment** | Join subjects using a code or a shared QR link |
| **Auto-Enrollment** | Click a join link → automatically enroll after login |
| **Attendance Dashboard** | View enrolled subjects with attendance stats (attended / total) |
| **Unenroll** | Leave a subject at any time |

### 🤖 AI Pipelines
- **Face Recognition Pipeline** — Uses `dlib` frontal face detector + 128-dim face embeddings + SVM classifier to identify students from classroom photos.
- **Voice Recognition Pipeline** — Uses `resemblyzer` VoiceEncoder to generate voice embeddings and cosine similarity matching to identify speakers from audio recordings.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | Streamlit (custom CSS theming with glassmorphism & gradient design) |
| **Backend** | Python |
| **Database** | Supabase (PostgreSQL) |
| **Face Recognition** | dlib, face_recognition_models, scikit-learn (SVM) |
| **Voice Recognition** | resemblyzer, librosa |
| **Authentication** | bcrypt (teacher passwords), FaceID (students) |
| **QR Codes** | segno |

---

## 📂 Project Structure

```
class_track/
├── app.py                          # Application entry point
├── requirements.txt                # Python dependencies
├── .streamlit/
│   └── config.toml                 # Streamlit theme configuration
├── src/
│   ├── screens/
│   │   ├── home_screen.py          # Landing page with Student/Teacher portals
│   │   ├── teacher_screen.py       # Teacher login, register & dashboard
│   │   └── student_screen.py       # Student FaceID login & dashboard
│   ├── components/
│   │   ├── header.py               # App header/logo component
│   │   ├── footer.py               # Footer component
│   │   ├── subject_card.py         # Reusable subject card widget
│   │   ├── dialog_create_subject.py    # Create new subject dialog
│   │   ├── dialog_share_subject.py     # Share subject via QR code dialog
│   │   ├── dialog_add_photo.py         # Upload classroom photos dialog
│   │   ├── dialog_enroll.py            # Manual enrollment dialog
│   │   ├── dialog_auto_enroll.py       # Auto-enroll via join link dialog
│   │   ├── dialog_attendance_results.py # Attendance results display dialog
│   │   └── dialog_voice_attendance.py  # Voice attendance dialog
│   ├── pipelines/
│   │   ├── face_pipeline.py        # Face detection, embedding & SVM classification
│   │   └── voice_pipeline.py       # Voice embedding & speaker identification
│   ├── database/
│   │   ├── config.py               # Supabase client initialization
│   │   └── db.py                   # All database CRUD operations
│   └── ui/
│       └── base_layout.py          # Global CSS styles & theming
```

---

## 🗄️ Database Schema (Supabase)

```
teachers
├── teacher_id (PK)
├── username (unique)
├── password (bcrypt hash)
└── name

students
├── student_id (PK)
├── name
├── face_embedding (float[128])
└── voice_embedding (float[256])

subjects
├── subject_id (PK)
├── subject_code (unique)
├── name
├── section
└── teacher_id (FK → teachers)

subject_students
├── student_id (FK → students)
└── subject_id (FK → subjects)

attendance_logs
├── student_id (FK → students)
├── subject_id (FK → subjects)
├── timestamp
└── is_present (boolean)
```

---

## Getting Started

### Prerequisites
- Python 3.10+
- A [Supabase](https://supabase.com/) project with the tables described above
- CMake (required for dlib compilation)

### 1. Clone the Repository

```bash
git clone https://github.com/Aryan2005-tech/Class_Track.git
cd Class_Track
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Supabase Secrets

Create a `.streamlit/secrets.toml` file:

```toml
SUPABASE_URL = "https://your-project.supabase.co"
SUPABASE_KEY = "your-anon-or-service-key"
```

> ⚠️ **Do not commit this file.** It is already included in `.gitignore`.

### 5. Run the Application

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`.

---

## 🔄 How It Works

### Face Attendance Flow
```
Teacher uploads classroom photos
        ↓
dlib detects all faces in each photo
        ↓
128-dim face embeddings are extracted
        ↓
SVM classifier predicts student IDs
        ↓
Euclidean distance check (threshold ≤ 0.6)
        ↓
Matched students marked as ✅ Present
```

### Voice Attendance Flow
```
Teacher records classroom audio
        ↓
librosa splits audio into speech segments
        ↓
resemblyzer generates voice embeddings per segment
        ↓
Cosine similarity matching against enrolled voices
        ↓
Matches above threshold (≥ 0.65) marked as ✅ Present
```

---

## 📸 Screenshots

> _Add screenshots of the home page, teacher dashboard, and student dashboard here._

---

## 📄 License

This project is for educational purposes.

---

<div align="center">
  <p>Built with ❤️ using Streamlit + AI</p>
</div>
]]>
