import pandas as pd
import numpy as np
import streamlit as st
import joblib

# Wczytanie modelu ML i transformera
model = joblib.load('model_random_forest.pkl')
transformer = joblib.load('transformer.pkl')

# Słownik modeli samochodów
modele = {
    'Opel': ['Astra', 'Corsa'],
    'BMW': ['X5', '320i'],
    'Ford': ['Focus', 'Mondeo'],
    'Toyota': ['Corolla', 'Yaris'],
    'Audi': ['A3', 'A4']
}

st.title('Predykcja cen aut 🚗')

st.write("Wprowadź dane auta:")

# Marka
marka = st.selectbox('Marka', list(modele.keys()))

# Model zależny od marki
model_samochodu = st.selectbox('Model', modele[marka])

rok = st.slider('Rok produkcji', 2005, 2022, 2015)
przebieg = st.slider('Przebieg (km)', 50000, 300000, 100000)
paliwo = st.selectbox('Paliwo', ['Benzyna', 'Diesel'])
skrzynia = st.selectbox('Skrzynia biegów', ['Manualna', 'Automat'])
moc = st.slider('Moc silnika (KM)', 70, 250, 120)

# Przycisk
if st.button('Oblicz cenę'):
    dane = pd.DataFrame({
        'Marka': [marka],
        'Model': [model_samochodu],
        'Rok': [rok],
        'Przebieg_km': [przebieg],
        'Paliwo': [paliwo],
        'Skrzynia': [skrzynia],
        'Moc_KM': [moc]
    })

    dane_przetworzone = transformer.transform(dane)
    predykcja = model.predict(dane_przetworzone)

    st.subheader(f'Przewidywana cena auta: {int(predykcja[0])} zł')


