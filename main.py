# main.py

from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import shutil
import os

from app.feature_extraction import extract_features  

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/analyze/")
async def analyze(file: UploadFile = File(...)):
    try:
        
        file_location = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        
        result = extract_features(file_location)

        return JSONResponse(content=result)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
