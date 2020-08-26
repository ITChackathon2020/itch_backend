import os
import uvicorn
from fastapi import FastAPI, Depends, Header, File, UploadFile
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException
from app_data import users
from data import predictions_handler

# Initiate app instance
app = FastAPI(title='ReArt', version='1.0',
              description='NN Image classification of recyclables')
manager = LoginManager(os.getenv("SECRET_KEY"), tokenUrl='/auth/token')
security = HTTPBasic()


# unprotected

@app.post("/send_image_predict/")
async def send_image_predict(file: UploadFile = File(...)):
    contents = await file.read()
    return {"pred": predictions_handler.get_prediction(contents)}


# protected


@manager.user_loader
def load_user(user_name: str, password: str):
    user = users.find_one({'username': user_name, "password": password})
    return user


@app.post('/auth/token')
def login(credentials: HTTPBasicCredentials = Depends(security)):
    user_name = credentials.username
    password = credentials.password
    user = load_user(user_name, password)
    if not user:
        raise InvalidCredentialsException  # you can also use your own HTTPException
    elif password != user['password']:
        raise InvalidCredentialsException
    access_token = manager.create_access_token(
        data=dict(sub=str(user["_id"]))
    )
    return {'access_token': access_token, 'token_type': 'bearer'}
