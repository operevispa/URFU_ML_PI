from transformers import pipeline

classifier = pipeline("sentiment-analysis",
			"blanchefort/rubert-base-cased-sentiment")

classifier("I love learnin in hight school")
