from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Form
from app.api import endpoints

app = FastAPI(title="Мой Pet-проект", version="1.0.0")

# Подключаем статические файлы
app.mount("/static", StaticFiles(directory="static"), name="static")

# Инициализируем шаблонизатор
templates = Jinja2Templates(directory="templates")

# Подключаем маршруты из модуля endpoints
app.include_router(endpoints.router)

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/dashboard")
async def dashboard(request: Request):
    # Заглушка: список отзывов
    reviews = [
        {"marketplace": "Wildberries", "text": "Отличный товар, быстрая доставка!", "date": "2025-02-10"},
        {"marketplace": "Ozon", "text": "Качество не очень, размер не подошел", "date": "2025-02-09"},
        {"marketplace": "Wildberries", "text": "Все понравилось, рекомендую!", "date": "2025-02-08"},
    ]
    return templates.TemplateResponse("dashboard.html", {"request": request, "reviews": reviews})

@app.get("/settings")
async def settings(request: Request):
    return templates.TemplateResponse("settings.html", {"request": request})

@app.post("/save_keys")
async def save_keys(wb_key: str = Form(...), ozon_client_id: str = Form(...), ozon_key: str = Form(...)):
    # Здесь позже будет сохранение в БД (зашифрованно)
    print(f"WB key: {wb_key}, Ozon client: {ozon_client_id}, Ozon key: {ozon_key}")
    return {"status": "ok", "message": "Ключи сохранены (временно в консоль)"}

@app.get("/fonts")
async def fonts_example(request: Request):
    return templates.TemplateResponse("fonts.html", {"request": request})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)