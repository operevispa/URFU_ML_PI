# URFU_ML_PI, group 2.11
## students: Sheshin N.A., Ivanov S.A., Perevispa O.V., Ovchar E.A.

## Перевиспа О.В. 
### Задание 1: Выбор модели предобученной модели МО и реализация скрипта
Выбран тип модели question-answering, модель timpal0l/mdeberta-v3-base-squad2. 
Пример работы модели [в скрипте qa.py](https://github.com/nasheshin01/URFU_ML_PI/blob/master/qa.py)

### Задание 2: Создание web-приложения МО на локальном компьютере
Ранее выбранная модель перенесена в приложение streamlit. Скриншоты работы приложения в scshots. Скрипт с приложением на streamlit [в файле qa_stlit.py](https://github.com/nasheshin01/URFU_ML_PI/blob/master/qa_stlit.py)

### Задание 3: Создание API-интерфейса для модели МО на локальном компьютере
Ранее выбранная модель пренесена в скрипт qa_fapi.py для работы с моделью через запросы API. Реализовано:
- метод GET на главную страницу, который возвращает просто текст, 
- метод POST по адресу /predict/ отрабатывает модель МО
- метод POST по адресу /sqnum/ возвращается квадрат переданного числа. 
Несколько методов созданы для тестирования функционала автоматического создания документация FastAPI. Скриншоты работы в scshots (в том числе скриншот cгенерированной документации). Реализация работы модели через запросы API [в файле qa_fapi.py](https://github.com/nasheshin01/URFU_ML_PI/blob/master/qa_fapi.py)
_____
## Шешин Н.А. 
### Задание 1: Выбран тип модели Zero-Shot Image Classification. Модель - openai/clip-vit-large-patch14. В скрипте sheshin_clip.py представлен пример запуска данной модели.


