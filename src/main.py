from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel
from context import context1


# создаем класс на основе класса BaseModel из библиотеки pydantiс
# для контроля вводимых пользователем данных для запроса
class Item(BaseModel):
    text: str
    num: int


# создаем pipeline с выбранной моделью МО
pipl = pipeline("question-answering", model="timpal0l/mdeberta-v3-base-squad2")

# создаем объект fastapi, который реализует взаимодействие приложения по API
app = FastAPI()


# метод срабатывает при обращении по адресу http://127.0.0.1:8000 (локально) и http://158.160.48.28:8000 (если извне)
@app.get("/")
async def root():
    #  вписываем docstring для документации по нашему API
    """ Метод возвращает JSON-объект, содержащий сообщение 'Курс Программная инженерия, 2023г. Группа 2.11'  """
    return {"message": "Курс Программная инженерия, 2023г. Группа 2.11"}


# метод возвращает контекст, который использует модель
@app.get("/cont")
async def root():
    #  вписываем docstring для документации по нашему API
    """ Метод возвращает JSON-объект, содержащий контекстные данные, которые используем модель """
    return {"message": context1}


# в декораторе указываем адрес страницы и что запрос методом POST
@app.post("/predict/")
async def predict(item: Item):
    #  вписываем docstring для документации по нашему API
    """ Метод возвращает результаты работы модели timpal0l/mdeberta-v3-base-squad2 на заданный \
    пользователем вопрос, основываясь на контексте, который скормлен в модель. \
    Метод возвращает JSON объект содержащий ответ модели, а также score ответа. """
    # возвращаем результат работы модели по вопросу, который пользователь ввел в POST запросе (в переменной item.text
    return pipl(question=item.text, context=context1)


# в декораторе указываем адрес страницы и что запрос методом POST
@app.post("/sqnum/")
async def sqnum(item: Item):
    #  вписываем docstring для документации по нашему API
    """ Метод возвращает квадрат введенного числа """
    # возвращаем квадрат введенного числа
    return {"message": item.num ** 2}
