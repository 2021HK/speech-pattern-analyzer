import numpy as np
import librosa
import logging
from app.audio_processing import load_audio, extract_pitch

def extract_features(file_path):
    try:
        logging.debug(f"Loading audio from: {file_path}")
        audio, sr = load_audio(file_path)

        duration = librosa.get_duration(y=audio, sr=sr)
        rms_array = librosa.feature.rms(y=audio)
        rms = np.mean(rms_array) if rms_array.size > 0 else 0.0  
        zcr_array = librosa.feature.zero_crossing_rate(y=audio)
        zcr = np.mean(zcr_array) if zcr_array.size > 0 else 0.0  
        pitch = extract_pitch(audio, sr)

        return {
            "duration_sec": round(duration, 2),
            "pitch": round(pitch, 2),
            "rms_energy": round(float(rms), 5),  
            "zero_crossing_rate": round(float(zcr), 5)  
        }

    except Exception as e:
        logging.error(f"Feature extraction failed: {e}", exc_info=True)
        raise