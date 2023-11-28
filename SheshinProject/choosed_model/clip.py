import requests

from PIL import Image
from transformers import pipeline

classifier = pipeline(model="openai/clip-vit-large-patch14")

url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image = Image.open(requests.get(url, stream=True).raw)

labels =["a photo of a cat", "a photo of a dog"]

predictions = classifier(image, candidate_labels=labels)
print(predictions)