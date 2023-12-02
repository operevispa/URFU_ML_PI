import streamlit as st
import pandas as pd
from transformers import pipeline
import contexts

@st.cache_resource
def load_model():
  return pipeline("question-answering", model="timpal0l/mdeberta-v3-base-squad2")

def textcleaner(stcl):
  return stcl.replace("\n","").strip()

pipl = load_model()

st.title('Привет! Это компания IVITECH 🎈')
st.header('Давай, мы попробуем ответить на твои вопросы о нашей компании')
st.text('Вот несколько примеров вопросов, который ты можешь задать:')
st.text('?? как называется ваша компания, какие продукты вы предлагаете, кто ваши клиенты ??')

quest = st.text_input('Напиши свой вопрос: ')
if quest:
  result = pipl(question = quest, context = contexts.context1)
  st.write(textcleaner(result['answer']))
  st.write("score is: ", result['score'])
