# model_trening.py

import pandas as pd
import numpy as np
import random
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

# Ustawienie losowości
random.seed(42)
np.random.seed(42)

# Wczytanie danych
df = pd.read_csv('dane.csv')

# Przygotowanie zmiennych X (cechy) i y (zmienna docelowa)
X = df.drop(columns=['Cena'])
y = df['Cena']

# Kolumny tekstowe do zakodowania
kategorie = ['Marka', 'Model', 'Paliwo', 'Skrzynia']

# Przekształcanie zmiennych tekstowych na liczbowe
column_transformer = ColumnTransformer(
    transformers=[
        ('onehot', OneHotEncoder(drop='first'), kategorie)
    ],
    remainder='passthrough'  # Pozostałe kolumny bez zmian
)

# Transformacja danych
X_encoded = column_transformer.fit_transform(X)

# Podział na zbiór treningowy i testowy
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Trenowanie modelu regresji liniowej
model_lin = LinearRegression()
model_lin.fit(X_train, y_train)

# Trenowanie modelu Random Forest
model_rf = RandomForestRegressor(n_estimators=100, random_state=42)
model_rf.fit(X_train, y_train)

# Predykcja na zbiorze testowym
y_pred_lin = model_lin.predict(X_test)
y_pred_rf = model_rf.predict(X_test)

# Ewaluacja modeli
print("\nRegresja liniowa:")
print("MAE:", mean_absolute_error(y_test, y_pred_lin))
print("MSE:", mean_squared_error(y_test, y_pred_lin))
print("R2:", r2_score(y_test, y_pred_lin))

print("\nRandom Forest:")
print("MAE:", mean_absolute_error(y_test, y_pred_rf))
print("MSE:", mean_squared_error(y_test, y_pred_rf))
print("R2:", r2_score(y_test, y_pred_rf))

# Zapis najlepszego modelu
joblib.dump(model_rf, 'model_random_forest.pkl')
joblib.dump(column_transformer, 'transformer.pkl')
print("✅ Zapisano model Random Forest do pliku 'model_random_forest.pkl'")
