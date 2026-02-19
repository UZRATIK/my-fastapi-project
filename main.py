from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api import endpoints

app = FastAPI(title="Мой Pet-проект", version="1.0.0")

# Подключаем статические файлы (CSS, изображения)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Подключаем маршруты из модуля endpoints
app.include_router(endpoints.router)

@app.get("/")
async def root():
    return {"message": "Добро пожаловать в мой pet-проект!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)