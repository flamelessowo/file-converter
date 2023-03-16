from typing import List
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse, StreamingResponse
from fastapi.requests import Request
from fastapi.middleware.cors import CORSMiddleware
import io

from backend.apps.converter.services.converter_service import ConverterService

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload/")
async def resolve_convert_files(request: Request, files: List[UploadFile] = File(...)):
    zipped_files: io.BytesIO = await ConverterService(files, request.headers['x-user-uuid'], request.headers['x-from-format'], request.headers['x-to-format']).convert()
    return StreamingResponse(iter([zipped_files.getvalue()]),
                             media_type="application/x-zip-compressed",
                             headers={"Content-Disposition": "attachment; filename=upload.zip"})