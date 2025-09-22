import joblib
import pandas as pd
from fastapi import FastAPI, Form, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

from src.data_preprocessing import DataPreprocessor
from src.feature_engineering import FeatureEngineer

app = FastAPI()
templates = Jinja2Templates(directory='templates')

# загружаем модель при старте приложения
model = joblib.load('models/catboost_model.pkl')


def process_file(file_path):
    df = pd.read_csv(file_path, sep=',', decimal='.', index_col='id').copy()
    df = DataPreprocessor(df).preprocess()
    df = FeatureEngineer(df).add_features()

    return pd.DataFrame({
        'id': df.index,
        'prediction': model.predict(df).astype(int)
    })


@app.post('/predict')
def predict(file_path: str = Form(...)):
    predictions = process_file(file_path)
    return JSONResponse(content=predictions.to_dict(orient='records'))


@app.get('/', response_class=HTMLResponse)
def form_get(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.post('/', response_class=HTMLResponse)
def form_post(request: Request, file_path: str = Form(...)):
    predictions = process_file(file_path)
    return templates.TemplateResponse(
        'index.html',
        {
            'request': request,
            'predictions': predictions.to_dict(orient='records')
        }
    )
