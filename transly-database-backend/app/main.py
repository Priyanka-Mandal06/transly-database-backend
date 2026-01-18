from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from app.db import connect_to_mongo, close_mongo_connection
from app.routes.auth_routes import router as auth_router
from app.routes.translation_routes import router as translation_router
from app.routes.user_routes import router as user_router
from app.routes.ocr_routes import router as ocr_router
from app.routes.speech_routes import router as speech_router
from app.routes.chatbot_routes import router as chatbot_router


app = FastAPI(
    title="Transly API",
    description="Translation Backend with MongoDB Authentication",
    version="1.0.0"
)

# ---------------- CORS ENABLED ---------------- #
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------- Custom OpenAPI for JWT Auth ----------- #
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )

    # Add Bearer JWT security scheme
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }

    # Apply security globally (Swagger adds Authorization automatically)
    openapi_schema["security"] = [{"BearerAuth": []}]

    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi


# ------------ ROUTES REGISTERED HERE ------------ #
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(translation_router)
app.include_router(ocr_router)
app.include_router(speech_router)
app.include_router(chatbot_router)


# ------------ MongoDB Connection Events ------------ #
@app.on_event("startup")
async def startup_event():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_event():
    await close_mongo_connection()


@app.get("/")
async def root():
    return {"message": "Transly Backend Running!"}
