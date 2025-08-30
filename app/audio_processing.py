import librosa
import numpy as np
import logging

def load_audio(file_path, sr=16000):
    """
    Load audio file and resample to 16kHz
    """
    try:
        audio, sample_rate = librosa.load(file_path, sr=sr)
        return audio, sample_rate
    except Exception as e:
        logging.error(f"Failed to load audio: {e}", exc_info=True)
        raise

def get_duration(audio, sr):
    return librosa.get_duration(y=audio, sr=sr)

def extract_pitch(audio, sr):
    """
    Extract average pitch from audio using librosa
    """
    try:
        pitches, magnitudes = librosa.piptrack(y=audio, sr=sr)
        pitch_values = pitches[magnitudes > np.median(magnitudes)]
        if len(pitch_values) == 0:
            return 0.0
        mean_pitch = np.mean(pitch_values)
        return float(mean_pitch) if not np.isnan(mean_pitch) else 0.0
    except Exception as e:
        logging.warning(f"Pitch extraction failed: {e}")
        return 0.0