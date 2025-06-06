Wprowadzenie
CLASSMATE to proste rozwiązanie informatyczne dedykowane placówkom edukacyjnym, mające na celu usprawnienie procesów komunikacyjnych oraz administracyjnych w środowisku szkolnym. Aplikacja została opracowana w ramach realizacji projektu na zajęcia z Aplikacji Sieciowych przez czteroosobowy zespół studentów.

Technologie
Frontend: HTML, CSS, JavaScript 
Backend: Python Flask
Baza danych: SQLite

Charakterystyka projektu
System został zaprojektowany z uwzględnieniem potrzeb czterech grup użytkowników:

-Administracji szkolnej – kompleksowe narzędzia do zarządzania strukturą organizacyjną szkoły
-Nauczycieli – moduły wspierające proces dydaktyczny i wychowawczy
-Uczniów – intuicyjny dostęp do informacji edukacyjnych
-Rodziców – narzędzia do monitorowania postępów dzieci

Szczegółowy opis funkcjonalności wraz z wizualizacją interfejsu użytkownika dostępny jest w załączonym pliku.

Aplikacja oferuje szereg funkcjonalności wspierających codzienne życie szkolne. W zakresie komunikacji dostępne są czaty w czasie rzeczywistym, umożliwiające tworzenie pokoi rozmów oraz wyszukiwanie użytkowników po imieniu, nazwisku i profesji. System ocen pozwala na przegląd wyników podzielonych na kategorie, takie jak sprawdziany, prace klasowe, zadania domowe czy aktywność. Każda ocena zawiera szczegóły takie jak waga, data, rodzaj i opis. Rodzice mają możliwość przeglądania ocen wszystkich swoich dzieci.
Funkcja frekwencji umożliwia nauczycielowi wprowadzanie obecności z możliwością zmiany statusu ucznia na obecny, nieobecny, spóźniony lub usprawiedliwiony. Uczniowie mają dostęp do kolorowego widoku swojej frekwencji, natomiast rodzice mogą usprawiedliwiać nieobecności dzieci, wskazując powód – zmiany te są widoczne dla nauczycieli.
Moduł zachowania pozwala nauczycielowi na wystawianie uwag oraz przyznawanie osiągnięć uczniom, a uczniowie i rodzice mogą przeglądać historię zachowania.
Administratorzy szkoły mają dostęp do narzędzi zarządzania, takich jak dodawanie przedmiotów i przypisywanie ich nauczycielom, tworzenie planu lekcji (jednorazowego lub cyklicznego), zarządzanie klasami (w tym zmiana wychowawcy i dodawanie uczniów) oraz przeglądanie listy użytkowników z możliwością filtrowania według typu konta.

Jako członek zespołu projektowego, byłam odpowiedzialny za kompleksowe opracowanie i wdrożenie modułu frekwencji, który stanowił kluczowy komponent całego systemu zarządzania szkołą. Moje obowiązki obejmowały następujące obszary:

Opracowałam trzy dedykowane widoki frekwencji dla różnych ról systemowych:

Dla nauczycieli:

-Stworzyłam interaktywną siatkę obecności z możliwością filtrowania po przedmiotach i klasach
-Zaznaczania statusu (obecny, nieobecny, spóźniony, usprawiedliwiony)
-Efektywnej nawigacji za pomocą klawiatury
-Podglądu historii frekwencji dla każdego ucznia
-Zaimplementowałam mechanizm przypinania kolumny z listą uczniów podczas przewijania planu lekcji
-Dodałam walidację danych przed wysłaniem do systemu

Dla uczniów:

-Zaprojektowałam czytelny widok kalendarza z wizualizacją frekwencji
-Kolorowe oznaczenia statusów (zielony - obecny, czerwony - nieobecny itd.)
-Szczegółowy podgląd pojedynczej nieobecności

Dla rodziców:

-Rozbudowałam system o funkcjonalność usprawiedliwień
-Możliwość podglądu frekwencji wielu dzieci rodzica

Projekt stanowił cenne doświadczenie w zakresie pracy zespołowej przy rozwijaniu złożonych systemów informatycznych, szczególnie w kontekście:

-Koordynacji pracy w zespole developerskim
-Stosowania dobrych praktyk w zakresie kontroli wersji
-Implementacji wymagań biznesowych w rozwiązania techniczne
-Testowania i weryfikacji poprawności działania systemu
