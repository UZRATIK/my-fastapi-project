from fastapi import APIRouter

router = APIRouter()

@router.get("/info")
async def get_info():
    return {
        "автор": "Ваше Имя",
        "группа": "КСК-2024",
        "версия": "1.0"
    }

@router.get("/students")
async def get_students():
    return {"студенты": ["Иванов Иван", "Петров Петр", "Сидорова Мария"]}

@router.get("/hello/{name}")
async def say_hello(name: str):
    return {
        "приветствие": f"Привет, {name}!",
        "сообщение": "Рад тебя видеть!"
    }