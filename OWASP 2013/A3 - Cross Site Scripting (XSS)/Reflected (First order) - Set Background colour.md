## Nazwa podatności: Cross-Site Scripting (XSS)

**Istotność:** 8

---

**Opis:**
Cross-Site Scripting (XSS) to typ podatności, który pozwala atakującemu wstrzyknąć złośliwy kod JavaScript do stron, które są następnie wyświetlane innym użytkownikom. Skrypt jest wykonany przez przeglądarkę użytkownika jako część strony HTML. Ataki XSS są szczególnie niebezpieczne, ponieważ pozwalają na wykonywanie skryptów w kontekście domeny ofiary, co może prowadzić do kradzieży danych sesji, manipulacji treścią strony, przekierowania na złośliwe strony, i innych złośliwych działań.

Podstrona z funkcją, która pozwala użytkownikowi na personalizację wyglądu poprzez ustawienie koloru tła (Background color) nie sanitarizuje ani nie koduje wprowadzonych danych, pozwalając na wstrzyknięcie kodu.

---

**Technika eksploitacji:**
Atakujący wprowadza payload JavaScript jako wartość koloru tła, np.:

`"><script>alert(document.cookie);</script>`

Gdy wartość ta jest osadzona bezpośrednio w atrybucie stylu HTML, zamyka ona atrybut i otwiera tag skryptu.

Kiedy strona jest ładowana lub odświeżana, przeglądarka interpretuje i wykonuje złośliwy skrypt. To pozwala na wykonanie działań z uprawnieniami użytkownika, takich jak dostęp do ciasteczek, które mogą zawierać tokeny sesji lub inne dane uwierzytelniające.

![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/56219452/d3a9b93b-dbd5-4a1b-b52a-546beffbdff1)

**Mitygacja:**
1. Kodowanie danych wejściowych: Upewnij się, że wszelkie dane wprowadzane przez użytkownika są odpowiednio kodowane przed osadzeniem w atrybutach HTML lub jako wartości w stylach CSS. Użyj odpowiednich metod kodowania, takich jak HTML entity encoding i JavaScript encoding.
1. Walidacja i sanityzacja danych wejściowych: Waliduj wszystkie dane wejściowe, aby upewnić się, że zawierają tylko dozwolone wartości. Dla pól związanych z wyglądem, takich jak kolor tła, akceptuj tylko wartości, które spełniają oczekiwany format (np. wartości HEX, RGB).
1. Użycie whitelistingu: Stosuj whitelisting dla danych wejściowych, aby ograniczyć możliwe wartości tylko do tych, które są bezpieczne i oczekiwane. Na przykład, do wyboru koloru tła, dostarcz listę predefiniowanych, bezpiecznych kolorów zamiast pozwalać na dowolne wprowadzanie danych.
1. Content Security Policy (CSP): Wdróż Content Security Policy, aby ograniczyć możliwość wykonania nieautoryzowanego kodu JavaScript. CSP może pomóc w ochronie przed XSS, kontrolując, skąd mogą być ładowane i wykonywane skrypty.
1. HttpOnly i Secure Cookies: Ustaw flagi HttpOnly i Secure dla ciasteczek, aby zapobiec ich odczytowi i modyfikacji przez skrypty JavaScript oraz zapewnić, że są przesyłane tylko przez bezpieczne połączenia HTTPS.
1. Bezpieczne frameworki: Korzystaj z frameworków i bibliotek webowych, które automatycznie sanityzują dane wejściowe i kodują dane wyjściowe, minimalizując ryzyko XSS.
1. Separacja danych i logiki: Unikaj bezpośredniego wstawiania danych wejściowych użytkownika do HTML. Korzystaj z bezpiecznych metod renderowania szablonów, które oddzielają dane od logiki prezentacji.
1. Wykrywanie i monitorowanie: Implementuj mechanizmy wykrywania i monitorowania prób ataków XSS, aby szybko reagować na potencjalne zagrożenia i incydenty.
