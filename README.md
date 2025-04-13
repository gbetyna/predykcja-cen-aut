# Predykcja cen aut 🚗

Projekt Machine Learning służący do przewidywania cen samochodów na podstawie ich parametrów.

## Cel projektu
Celem projektu jest stworzenie modelu ML, który na podstawie danych wejściowych o samochodzie (marka, model, rok, przebieg, paliwo, skrzynia biegów, moc) przewiduje jego cenę.

Dodatkowo przygotowana została aplikacja webowa w Streamlit umożliwiająca interaktywną predykcję ceny auta.

---

## Technologie użyte w projekcie:
- Python
- Pandas
- Numpy
- Scikit-learn
- Matplotlib
- Streamlit
- Joblib

---

## Struktura projektu:

## Struktura projektu:

```
predykcja-cen-aut/
│
├── model_generowanie_danych.py        # Generowanie danych (dane.csv)
├── model_trening.py                   # Trenowanie modelu ML
├── eda.py                             # Eksploracyjna analiza danych
├── app.py                             # Aplikacja webowa Streamlit
├── dane.csv                           # Wygenerowane dane
├── model_random_forest.pkl            # Zapisany model ML
├── transformer.pkl                    # Zapisany transformer
├── requirements.txt                   # Lista bibliotek
└── README.md                          # Opis projektu
```


