
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt

router = APIRouter()

SECRET_KEY = "my-secret-key"
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

users = {
    "admin":
    { 
        "username": "admin",
        "password": "1234"
    }
}

@router.post("/login")
async def login( form_data: OAuth2PasswordRequestForm = Depends()):
    print(form_data.username)
    print(form_data.password)
    user = users.get(form_data.username)

    print(user["password"])

    if not user or not user["password"] == form_data.password:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
   
    print(user)

    token = jwt.encode( {
        "sub": user["username"]
    }, 
    SECRET_KEY, algorithm=ALGORITHM
    )

    return {
        "access_token" : token,
        "token_type": "bearer"
    }

def get_current_user(token: str = Depends(oauth2_scheme) ): 

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")

        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        print(f"username: =  {username}")

        return username
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")