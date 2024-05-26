import re

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

class PasswordModel(BaseModel):
    password:str

app = FastAPI()

@app.post('/check_password',tags=['Login'])
async def check_passwords(password:PasswordModel):
    regex = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@#$%])[A-Za-z\d@#$%]{4,8}$'
    alertMsg = "密碼必須包含4到8個字符，並且只能包含英文字母、數字和以下特殊字符之一：@#$%"

    if not re.match(regex, password.password):
        return {"message": alertMsg}
    return {"message":"Password is valid"}

if __name__ == '__main__':
    uvicorn.run('main:app',reload=True)


