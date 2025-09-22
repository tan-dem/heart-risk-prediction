# Приложение для предсказания рисков сердечного приступа

## Описание

Сервис на базе FastAPI для предсказания рисков сердечного приступа (высокий/низкий) по данным, загруженным из CSV-файла, с использованием обученной модели (`catboost_model.pkl`).

---

## Как запустить проект:

1. Клонируйте репозиторий:

```
git clone git@github.com:tan-dem/heart-risk-prediction.git
cd heart-risk-prediction
```

2. Создайте и активируйте виртуальное окружение:

```
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

3. Установите зависимости из файла `requirements.txt`:

```
pip install -r requirements.txt
```

4. Запустите сервер (из корневой папки проекта):

```bash
uvicorn app.main:app --reload
```

Сервер будет доступен по адресу `http://127.0.0.1:8000`

---

## Как получить предсказания:

### Через веб-форму

1. На главной странице (`/`) введите путь к CSV-файлу.
2. Нажмите «Предсказать».
3. Таблица с предсказаниями отобразится на странице.

### Через POST-запрос

```
import requests

url = "http://127.0.0.1:8000/predict"
data = {"file_path": "datasets/heart_test.csv"}

response = requests.post(url, data=data)
print(response.json())
```

Пример ответа:

```
[
  {'id': 1, 'prediction': 0}, 
  {'id': 2, 'prediction': 1},
  ...
]
```

