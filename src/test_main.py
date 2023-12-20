from fastapi.testclient import TestClient           # подключаем TestClient — клиент для тестрования API из FastAPI
from qa_fapi import app                                
                                                    
client = TestClient(app)                            # создается клиент для тестирования, которому при создании передается объект API app, тестирование которого необходимо выполнить

# тест проверяет доступность приложения при обращении к корню сервера
def test_main():
    response = client.get("/")                      # клиент запускает запрос HTTP GET к корню сервера (путь "/") и записывает результат в переменную response
    # затем выполняются два теста с помощью оператора assert. Первый проверяет код ответа HTTP 200
    assert response.status_code == 200              # код ответа 200 означает, что запрос выполнен успешно. Другие коды свидетельствуют о том, что произошла ошибка при обработке запроса
    assert response.json() == {"message": "Курс Программная инженреия, 2023г. Группа 2.11"}  # второй тест проверяет содержание ответа


# тест проверяет отвечает ли в принципе модель ИИ на запрос пользоваеля, т.е. скор должен быть больше 0
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