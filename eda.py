# eda.py
# Eksploracyjna analiza danych (EDA)

import pandas as pd
import matplotlib.pyplot as plt

# Wczytanie danych z pliku csv lub bezpośrednio z kodu
# Jeśli dane masz zapisane do pliku csv:
# df = pd.read_csv('dane.csv')

# Jeżeli na razie pracujesz tylko w model_trening.py — to tam tworzyłeś df
# Tu zakładamy, że masz już DataFrame df

# Dla testu możesz wkleić sobie ten fragment z poprzedniej części
# (Ale docelowo EDA działa na gotowym df np. wczytanym z pliku)

# Wyczytanie danych z pliku model_trening.py

df = pd.read_csv('dane.csv')

# Wizualizacja nr 1 — Cena vs Przebieg
plt.figure(figsize=(8, 5))
plt.scatter(df['Przebieg_km'], df['Cena'], alpha=0.7)
plt.xlabel('Przebieg (km)')
plt.ylabel('Cena (zł)')
plt.title('Cena vs Przebieg')
plt.grid(True)
plt.show()

# Wizualizacja nr 2 — Cena vs Rok produkcji
plt.figure(figsize=(8, 5))
plt.scatter(df['Rok'], df['Cena'], alpha=0.7, color='orange')
plt.xlabel('Rok produkcji')
plt.ylabel('Cena (zł)')
plt.title('Cena vs Rok produkcji')
plt.grid(True)
plt.show()

# Wizualizacja nr 3 — Średnia cena wg marki
plt.figure(figsize=(8, 5))
df.groupby('Marka')['Cena'].mean().plot(kind='bar', color='green')
plt.ylabel('Średnia cena (zł)')
plt.title('Średnia cena wg marki')
plt.grid(True)
plt.tight_layout()
plt.show()
