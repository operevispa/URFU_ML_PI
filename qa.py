# Студент: Oleg Perevispa
# использован тип модели question-answering, модель timpal0l/mdeberta-v3-base-squad2
from transformers import pipeline
import contexts

def textcleaner(st):
  return st.replace("\n","").strip()


qustlist = ["Какие продукты предлагает компания",
"Я физическое лицо. Могу ли я быть клиентом компании",
"Какие требования компания предъявляет к клиентам"]


pipl = pipeline("question-answering", model="timpal0l/mdeberta-v3-base-squad2")

qalist = pipl(question = qustlist, context = contexts.context1)

i = 0
for i in range(len(qalist)):
  print(f"{qustlist[i]}: {textcleaner(qalist[i]['answer'])}  |score: {qalist[i]['score']}|")
