import os
from fastapi import FastAPI, Depends, Header, File, UploadFile
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException
from app_data import users
from data import predictions_handler

app = FastAPI()
manager = LoginManager(os.getenv("SECRET_KEY"), tokenUrl='/auth/token')
security = HTTPBasic()


# unprotected

# test route----
@app.get("/test_prediction/{user_input}")
def test_prediction(user_input):
    try:
        return {"prediction_data": predictions_handler.get_prediction(int(user_input))}
    except Exception as e:
        return {"error": str(e)}


# actual route

# @app.post("/send_file/")
# async def create_upload_file(user_uploaded_file: UploadFile = File(...)):
#     contents = await user_uploaded_file.read()
#     predictions = await predictions_handler.get_prediction(user_uploaded_file)
#     return {"prediction_data": predictions }


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
