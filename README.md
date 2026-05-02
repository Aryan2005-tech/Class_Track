# 🚀 Class Track  
### AI-Powered Classroom Attendance System  

<div align="center">
  <img src="https://i.ibb.co/YTYGn5qV/logo.png" alt="Class Track Logo" width="120" />

  <p><strong>Smart attendance using Face & Voice Recognition</strong></p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/Streamlit-1.x-FF4B4B?logo=streamlit&logoColor=white" />
    <img src="https://img.shields.io/badge/Supabase-Database-3FCF8E?logo=supabase&logoColor=white" />
    <img src="https://img.shields.io/badge/dlib-Face_Recognition-008080" />
  </p>
</div>

---

## 📌 About  

**Class Track** is an intelligent attendance system that automates classroom attendance using **facial recognition** and **voice identification**.

Built with **Streamlit**, it provides a modern UI with separate portals for teachers and students.

### 👨‍🏫 Teachers can:
- Create subjects  
- Upload classroom images or record audio  
- Automatically mark attendance using AI  

### 👨‍🎓 Students can:
- Login using FaceID (no passwords)  
- Enroll in subjects via codes or QR  
- Track attendance in real time  

---

## ✨ Features  

### 🎓 Teacher Portal  

| Feature | Description |
|--------|------------|
| Account Management | Secure login with bcrypt password hashing |
| Subject Management | Create & manage subjects |
| Face Attendance | Detect & identify students from images |
| Voice Attendance | Identify students from audio |
| QR Sharing | Share subject via QR/link |
| Attendance Records | View logs & statistics |

---

### 🧑‍🎓 Student Portal  

| Feature | Description |
|--------|------------|
| FaceID Login | Password-free authentication |
| Voice Enrollment | Optional voice registration |
| Subject Join | Join via code or QR |
| Auto Enrollment | Join instantly via link |
| Dashboard | View attendance stats |
| Unenroll | Leave subjects anytime |

---

### 🤖 AI Pipelines  

- **Face Recognition**
  - dlib face detector  
  - 128-d embeddings  
  - SVM classifier  

- **Voice Recognition**
  - resemblyzer embeddings  
  - cosine similarity matching  

---

## 🛠️ Tech Stack  

| Layer | Technology |
|------|-----------|
| Frontend | Streamlit + custom CSS |
| Backend | Python |
| Database | Supabase (PostgreSQL) |
| Face Recognition | dlib, sklearn |
| Voice Recognition | resemblyzer, librosa |
| Authentication | bcrypt + FaceID |
| QR Codes | segno |

---

## 📂 Project Structure  

```bash
class_track/
├── app.py
├── requirements.txt
├── .streamlit/
│   └── config.toml
├── src/
│   ├── screens/
│   ├── components/
│   ├── pipelines/
│   ├── database/
│   └── ui/
