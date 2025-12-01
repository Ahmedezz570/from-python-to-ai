from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import os

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")


model = tf.keras.models.load_model("model.keras")



@app.get("/")
def home():
    return FileResponse(os.path.join("static", "index.html"))



@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = Image.open(io.BytesIO(await file.read())).convert("L")
    image = image.resize((28, 28))
    image_array = np.array(image) / 255.0
    image_array = image_array.reshape(1, 28, 28)

    prediction = model.predict(image_array)
    predicted_digit = int(np.argmax(prediction, axis=1)[0])

    return {"predicted_digit": predicted_digit}
