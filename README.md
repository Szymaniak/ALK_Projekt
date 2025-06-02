
# Zautomatyzowane testy UI aplikacji sklepu internetowego

## Opis projektu

Projekt zawiera zestaw testów automatycznych interfejsu użytkownika (UI) dla aplikacji sklepu internetowego. Testy zostały przygotowane przy użyciu biblioteki **Selenium** w języku **Python** oraz bazują na strukturze **Page Object Model (POM)**.

Testy obejmują najważniejsze funkcjonalności z punktu widzenia użytkownika końcowego: rejestrację, logowanie, dodawanie produktów do koszyka, usuwanie produktów, weryfikację cen oraz walidację formularzy.

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
├── screenshots/        # Zrzuty ekranu z testów (generowane automatycznie)
├── README.md           # Dokumentacja projektu
└── requirements.txt    # Lista wymaganych bibliotek (opcjonalnie)
```

---

## Lista przypadków testowych

| ID   | Tytuł                                                                                     | Opis                                                                                      |
|------|--------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| 001  | Ładowanie strony startowej https://inpost.pl/                                              | Sprawdzenie, czy strona główna ładuje się poprawnie.                                     |
| 002  | Rejestracja nowego użytkownika i logowanie                                                 | Rejestracja użytkownika, a następnie logowanie i weryfikacja komunikatu powitalnego.     |
| 003  | Walidacja formularza logowania – brak danych oraz poprawne logowanie                      | Test logowania bez danych oraz z poprawnymi danymi użytkownika.                          |
| 004  | Dodanie losowego produktu do koszyka z poziomu strony głównej                              | Dodanie jednego losowo wybranego telefonu do koszyka i weryfikacja poprawności dodania.  |
| 005  | Dodanie produktu „Samsung galaxy s6” do koszyka i jego usunięcie                          | Dodanie konkretnego produktu, zapis zrzutów ekranu przed i po usunięciu z koszyka.       |
| 006  | Dodanie losowej liczby produktów do koszyka i weryfikacja sumy cen                        | Dodanie od 1 do 4 produktów, zliczenie cen i porównanie z wartością podaną w koszyku.     |

---

## Uruchamianie testów

1. Upewnij się, że masz zainstalowanego **Pythona 3** oraz bibliotekę `selenium`.
2. Uruchom testy za pomocą polecenia:

```bash
python -m unittest discover tests/
```

---

## Uwagi

- Testy generują zrzuty ekranu do katalogu `screenshots/` przy usuwaniu produktów.
- Część danych (np. użytkownicy testowi) jest generowana dynamicznie z użyciem biblioteki `Faker`.
- Testy mogą wymagać dostosowania do konkretnego adresu URL aplikacji.

---

## Autor

Zespół QA
