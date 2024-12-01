from typing import Optional

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
# from pydantic import BaseModel
from mongodb_file import mongo_get, mongo_get_image_by_id
import starlette.status as status
from main import connect_to_webcam


app = FastAPI()


@app.post('/webcam')
def post_data():
    if connect_to_webcam():
        return {"message": "Данные отправлены на сервер"}
    return {"message": "Какие то проблемы"}

@app.get('/get_all_images')
def get_all_data():
    result = mongo_get()
    datas = [{"id": data['_id'], "link": data['link']} for data in result]
    return datas


@app.get('/get_image/<id>')
def get_image(id):
    return RedirectResponse(url=mongo_get_image_by_id(id), status_code=status.HTTP_302_FOUND)