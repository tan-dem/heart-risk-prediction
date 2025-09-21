import joblib
import pandas as pd

from data_preprocessing import DataPreprocessor
from feature_engineering import FeatureEngineer


def main():
    # загрузка данных
    test = pd.read_csv(
        '../datasets/heart_test.csv', sep=',', decimal='.', index_col='id'
    ).copy()

    # предобработка данных
    x_test = DataPreprocessor(test).preprocess()

    # добавляем признаки
    x_test = FeatureEngineer(x_test).add_features()

    # загружаем модель
    model = joblib.load('../models/catboost_model.pkl')

    # делаем предсказания
    predictions = pd.DataFrame({
        'id': x_test.index,
        'prediction': model.predict(x_test).astype(int),
    })

    # сохраняем в CSV
    predictions.to_csv('../predictions_new.csv')


if __name__ == "__main__":
    main()
