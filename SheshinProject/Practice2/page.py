import io
import streamlit as st
from PIL import Image
from clip_classifier import ClipClassifier

@st.cache_data()
def load_clip_classifier():
    return ClipClassifier()

def load_image():
    """Создание формы для загрузки изображения"""
    # Форма для загрузки изображения средствами Streamlit
    uploaded_file = st.file_uploader(
        label='Выберите изображение для распознавания')
    if uploaded_file is not None:
        # Получение загруженного изображения
        image_data = uploaded_file.getvalue()
        # Показ загруженного изображения на Web-странице средствами Streamlit
        st.image(image_data)
        # Возврат изображения в формате PIL
        return Image.open(io.BytesIO(image_data))
    else:
        return None
    
def main():    
    st.title('Классификация изображений')
    img = load_image()
    labels_input = st.text_input('Впишите классы через запятую (на английском):')
    labels = labels_input.split(',')
    run_button = st.button("Запустить классификацию")
    if run_button:
        if len(labels) <= 0 or labels[0] == '':
            st.error("Не были прописаны классы для определения")
            return
        
        if img is None:
            st.error("Не было выбрано изображение")
            return

        model = load_clip_classifier()
        with st.spinner("waiting"):
            label, score = model.predict(img, labels)
        st.write(f'Класс: {label} с вероятностью {int(score * 100)}%')

if __name__ == "__main__":
    main()

    
        