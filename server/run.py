from typing import List
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.requests import Request
from fastapi.middleware.cors import CORSMiddleware

#DELETE
from backend.apps.converter.pdf2word import Pdf2Word 

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
    print(request.headers)
    print(files)
    return True