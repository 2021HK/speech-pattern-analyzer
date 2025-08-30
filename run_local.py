# run_local.py

import os
from app.feature_extraction import extract_features


AUDIO_FOLDER = "audio_samples"


for filename in os.listdir(AUDIO_FOLDER):
    if filename.endswith(".wav") or filename.endswith(".wav.wav"):
        file_path = os.path.join(AUDIO_FOLDER, filename)
        print(f"\n🎧 Features for {filename}:")
        features = extract_features(file_path)
        for key, value in features.items():
            print(f"  {key}: {value}")
