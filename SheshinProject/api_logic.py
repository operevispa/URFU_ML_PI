from fastapi import FastAPI
from clip_classifier import ClipClassifier, ClipUrlDataTemplate


app = FastAPI()
classifier = ClipClassifier()

@app.get("/")
def root():
    """Корневая страница API"""
    return {"message": "Добро пожаловать! " +
                       "Для использования классификатора изображений используйте запрос /predict " + 
                       "Чтобы получить документацию используйте запрос /docs "}

@app.post("/predict/")
def predict(clip_data: ClipUrlDataTemplate):
    """Запрос для предсказания классификатором."""
    result = classifier.predict_by_url_data_template(clip_data)
    dict_result = {'label': result[0],
                   'confidence': result[1]}
    return dict_result