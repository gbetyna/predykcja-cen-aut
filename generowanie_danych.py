# Import bibliotek
import pandas as pd     # Praca z danymi w tabelach (DataFrame)
import numpy as np      # Obliczenia numeryczne
import random           # Losowanie wartości

# Ustawienie losowości dla powtarzalnych wyników
random.seed(42)         # Seed do random — gwarantuje powtarzalność losowań
np.random.seed(42)      # Seed do numpy — to samo dla funkcji numpy

# Lista marek i modeli samochodów
marki = ['Opel', 'BMW', 'Ford', 'Toyota', 'Audi']
modele = {
    'Opel': ['Astra', 'Corsa'],
    'BMW': ['X5', '320i'],
    'Ford': ['Focus', 'Mondeo'],
    'Toyota': ['Corolla', 'Yaris'],
    'Audi': ['A3', 'A4']
}

# Rodzaje paliwa i skrzyń biegów
paliwa = ['Benzyna', 'Diesel']
skrzynie = ['Manualna', 'Automat']

# Generowanie danych (100 rekordów)
samochody = []

for _ in range(100):
    marka = random.choice(marki)                          # Losowy wybór marki
    model = random.choice(modele[marka])                  # Losowy wybór modelu
    rok = random.randint(2005, 2022)                      # Losowy rok produkcji
    przebieg = random.randint(50000, 300000)              # Losowy przebieg
    paliwo = random.choice(paliwa)                        # Losowe paliwo
    skrzynia = random.choice(skrzynie)                    # Losowa skrzynia
    moc = random.randint(70, 250)                         # Losowa moc silnika (KM)

    # Obliczenie ceny auta na podstawie wzoru:
    bazowa_cena = 50000 - (2023 - rok) * 2000 - przebieg * 0.05 + moc * 100
    cena = int(np.clip(bazowa_cena + np.random.normal(0, 5000), 5000, 120000))
    # np.clip - ogranicza wartość ceny od 5000 zł do 120000 zł
    # np.random.normal - dodaje losowy "szum" do ceny (rozrzut +- 5000 zł)

    # Dodanie rekordu auta do listy
    samochody.append([marka, model, rok, przebieg, paliwo, skrzynia, moc, cena])

# Przekształcenie listy do tabeli pandas (DataFrame)
df = pd.DataFrame(samochody, columns=[
    'Marka', 'Model', 'Rok', 'Przebieg_km', 'Paliwo', 'Skrzynia', 'Moc_KM', 'Cena'
])

# Zapis pliku do formatu CSV.
df.to_csv('dane.csv', index=False)