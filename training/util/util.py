import base64
from io import BytesIO
from PIL import Image
from fastapi import UploadFile
import numpy as np
import cv2

def load_image_from_upload(file: UploadFile) -> np.ndarray:
    image = Image.open(file.file).convert("RGB")
    return np.array(image)

def load_image_from_base64(base64_str: str) -> np.ndarray:
    header, base64_data = base64_str.split(",", 1)
    image_data = base64.b64decode(base64_data)
    image = Image.open(BytesIO(image_data)).convert("RGB")
    return np.array(image)
