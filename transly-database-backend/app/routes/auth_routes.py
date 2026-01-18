from fastapi import APIRouter, HTTPException
from passlib.context import CryptContext
from app.db import get_db
from app.models.user_model import RegisterUser, LoginUser, UserInDB, UserResponse
from app.auth_utils import create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"]) 
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("/register")
async def register_user(user: RegisterUser):
    database = await get_db()

    existing_user = await database.users.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = pwd_context.hash(user.password)

    new_user = UserInDB(
        username=user.username,
        email=user.email,
        password=hashed_password,
    ).dict()

    result = await database.users.insert_one(new_user)
    user_id = str(result.inserted_id)

    await database.users.update_one({"_id": result.inserted_id}, {"$set": {"id": user_id}})

    return {"message": "User registered successfully", "user_id": user_id}


@router.post("/login")
async def login_user(credentials: LoginUser):
    database = await get_db()

    user = await database.users.find_one({"email": credentials.email})
    if not user or not pwd_context.verify(credentials.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(user["id"])

    safe_user = UserResponse(
        id=user["id"],
        username=user["username"],
        email=user["email"],
        created_at=user["created_at"]
    )

    return {
        "message": "Login success",
        "access_token": token,
        "token_type": "bearer",
        "user": safe_user
    }
