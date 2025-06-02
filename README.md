
# Zautomatyzowane testy UI aplikacji sklepu internetowego

## Opis projektu

Projekt zawiera zestaw testów automatycznych interfejsu użytkownika (UI) dla aplikacji sklepu internetowego, służącej do ćwiczenia testów automatycznych https://demoblaze.com/. Testy zostały przygotowane przy użyciu biblioteki **Selenium** w języku **Python** oraz bazują na strukturze **Page Object Model (POM)**.

Testy obejmują najważniejsze funkcjonalności z punktu widzenia użytkownika końcowego: rejestrację, logowanie, dodawanie produktów do koszyka, usuwanie produktów oraz weryfikację cen.

W testach została wykorzystana biblioteka Faker do generowania danych (Przypadek testowy 001 - Rejestracja nowego użytkownika). Zapisywanie zrzutów ekranu wraz z datą ich wykonania (Przypadek testowy 004 - Dodanie produktu do koszyka i jego usunięcie)

---

## Środowisko testowe

- **Przeglądarka:** Chrome (136.0.7103.114)  
- **System operacyjny:** Windows 10 (10.0.19045)  
- **Język:** Python 3  
- **Framework:** unittest + Selenium  

---

## Struktura katalogów

```
.
├── pages/              # Obiekty stron (Page Object Model)
├── tests/              # Przypadki testowe
├── screenshots/        # Zrzuty ekranu z testów 
├── README.md           # Dokumentacja projektu
└── requirements.txt    # Lista wymaganych bibliotek 
```

---

## Lista przypadków testowych

| ID  | Tytuł                                                              | Opis                                                                                                                                                       |
|-----|--------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 001 | Rejestracja nowego użytkownika                                     | Rejestracja użytkownika, a następnie weryfikacja czy konto zostało poprawnie założone poprzez zalogowanie się na nie i weryfikację komunikatu powitalnego. |
| 002 | Walidacja formularza logowania                                     | Test logowania bez danych oraz z poprawnymi danymi użytkownika.                                                                                            |
| 003 | Dodanie losowego produktu do koszyka                               | Dodanie jednego losowo wybranego telefonu do koszyka i weryfikacja poprawności dodania.                                                                    |
| 004 | Dodanie produktu do koszyka i jego usunięcie                       | Dodanie konkretnego produktu, zapis zrzutów ekranu przed i po usunięciu produktu z koszyka.                                                                |
| 005 | Dodanie losowej liczby produktów do koszyka i weryfikacja sumy cen | Dodanie od 1 do 4 produktów, zliczenie cen i porównanie z wartością podaną w koszyku.                                                                      |

---

## Uruchamianie testów

Poszczegulne testy można uruchomić z plików, w których się znajdują. 

Wszystkie testy naraz można włączyć wykonująć plik main.

---

## Autor

Damian Szymański