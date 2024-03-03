from fastapi.testclient import TestClient  # подключаем TestClient — клиент для тестирования API из FastAPI
from main import app

client = TestClient(app)  # создается клиент для тестирования


# тест проверяет доступность приложения при обращении к корню сервера
def test_main():
    # клиент запускает запрос HTTP GET к корню сервера (путь "/") и записывает результат в переменную response
    response = client.get("/")

    # затем выполняются два теста с помощью оператора assert. Первый проверяет код ответа HTTP 200
    assert response.status_code == 200
    # код ответа 200 означает, что запрос выполнен успешно. Другие коды свидетельствуют об ошибке

    # второй тест проверяет содержание ответа
    assert response.json() == {"message": "Курс Программная инженерия, 2023г. Группа 2.11"}


# провереем отвечает ли в принципе модель ИИ на запрос пользователя, т.е. скор должен быть больше 0
def test_predict():
    response = client.post("/predict/",
                           json={"text": "Какой продукт предлагает компания своим клиентам?", "num": 0}
                           )
    json_data = response.json()
    assert response.status_code == 200
    assert float(json_data['score']) > 0


# тест проверяет запрос sqnum
def test_sqnum():
    response = client.post("/sqnum/",
                           json={"num": 5, "text": ""}
                           )
    json_data = response.json()
    assert response.status_code == 200
    assert int(json_data['message']) == 25
