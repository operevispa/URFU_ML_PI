import requests

from PIL import Image
from transformers import pipeline
from typing import List
from pydantic import BaseModel


class ClipUrlDataTemplate(BaseModel):
    image_url: str
    labels: List[str]

class ClipClassifier:
    def __init__(self) -> None:
        self.classifier = pipeline(model="openai/clip-vit-large-patch14")

    def predict(self, image: Image, labels: List[str]):
        predictions = self.classifier(image, candidate_labels=labels)
        return predictions[0]['label'], predictions[0]['score']
    
    def predict_by_url_data_template(self, data: ClipUrlDataTemplate):
        image = Image.open(requests.get(data.image_url, stream=True).raw)
        labels = data.labels
        return self.predict(image, labels)