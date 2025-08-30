# 🎤 Speech Pattern Analyzer (AIML Project)

This project is a **FastAPI-based web application** for analyzing speech/audio patterns using Python. It extracts useful audio features like duration, pitch, energy, and zero-crossing rate from uploaded audio files.

---

## 🚀 Tech Stack

- **Python 3.9+**
- **FastAPI** – for building the API
- **Uvicorn** – ASGI server
- **Librosa** – audio processing
- **NumPy, Soundfile** – supporting audio analysis

---

## ⚙️ Features Extracted

When an audio file is sent to the `/analyze/` endpoint, the API returns:

| Feature              | Description                                |
|----------------------|--------------------------------------------|
| `duration_sec`       | Total length of the audio (in seconds)     |
| `pitch`              | Estimated fundamental frequency            |
| `rms_energy`         | Root mean square energy (loudness measure) |
| `zero_crossing_rate` | Frequency of signal sign changes           |

---

## ▶️ How to Run the Project

1. **Clone the repository** (or download it):

git clone https://github.com/yourusername/speech-pattern-analyzer.git
cd speech-pattern-analyzer
Install dependencies:

pip install -r requirements.txt


Start the FastAPI server using Uvicorn:

uvicorn app.main:app --reload


Open browser and test:
Go to:

http://127.0.0.1:8000/docs


Use the /analyze/ endpoint to upload an audio file and receive extracted features.
