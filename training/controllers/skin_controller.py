from fastapi import APIRouter, File, UploadFile, HTTPException
from training.services.skin_services import predict_skin_from_upload, predict_skin_from_webcam

router = APIRouter()

@router.post("/skin/predict")
async def predict_skin_type(file: UploadFile = File(...)):
    if not file.filename.lower().endswith((".png", ".jpg", ".jpeg")):
        raise HTTPException(status_code=400, detail="Unsupported file format.")
    result = predict_skin_from_upload(file)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result

@router.get("/skin/predict/webcam")
def predict_skin_type_from_webcam():
    result = predict_skin_from_webcam()
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result
