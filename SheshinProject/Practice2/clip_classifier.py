from PIL import Image
import requests

from transformers import pipeline
from typing import List


class ClipClassifier:
    def __init__(self) -> None:
        self.classifier = pipeline(model="openai/clip-vit-large-patch14")

    def predict(self, image: Image, labels: List[str]):
        predictions = self.classifier(image, candidate_labels=labels)
        return predictions[0]['label'], predictions[0]['score']