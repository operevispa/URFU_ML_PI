from fastapi.testclient import TestClient
from api_logic import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Добро пожаловать! " +
                               "Для использования классификатора изображений используйте запрос /predict " + 
                               "Чтобы получить документацию используйте запрос /docs "}
    
def test_predict():
    img_urls = [
        "http://images.cocodataset.org/val2017/000000039769.jpg",
        "https://imgupscaler.com/images/samples/animal-before.webp",
        "https://d27p2a3djqwgnt.cloudfront.net/wp-content/uploads/2018/01/09060054/cow-354428_1280.jpg",
        "https://news.harvard.edu/wp-content/uploads/2023/11/dog_brains_2500-1600x900.jpg"
    ]

    true_labels = [
        "cats",
        "birds",
        "cows",
        "dogs"
    ]

    request_labels = ["cats", "dogs", "cows", "birds"]

    for i, url in enumerate(img_urls):
        print(i)
        response = client.post("/predict/",
            json={
                "image_url": url, 
                "labels": request_labels
                }
        )
        json_data = response.json() 

        assert response.status_code == 200
        assert json_data['label'] == true_labels[i]
        assert json_data['confidence'] > 0.99