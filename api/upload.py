from fastapi import APIRouter
from fastapi import UploadFile

router = APIRouter()


@router.post("/upload")
async def upload_document(
    file: UploadFile
):

    path = f"uploads/{file.filename}"

    with open(path, "wb") as f:
        f.write(await file.read())

    return {
        "message": "uploaded"
    }