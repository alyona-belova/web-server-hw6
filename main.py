from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse, PlainTextResponse
from PIL import Image
import io

app = FastAPI()


@app.middleware("http")
async def add_cors_headers(request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET,POST,PUT,DELETE,OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = (
        "Content-Type,Accept,Access-Control-Allow-Headers"
    )
    return response


@app.get("/login/")
async def login():
    return PlainTextResponse("alyona_belova")


@app.post("/size2json/")
async def size2json(image: UploadFile = File(...)):
    contents = await image.read()
    img = Image.open(io.BytesIO(contents))
    width, height = img.size
    return JSONResponse({"width": width, "height": height})
