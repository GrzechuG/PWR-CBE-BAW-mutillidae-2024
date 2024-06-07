## Nazwa podatności: HTML/CSS Injection

**Istotność:** 5

---

**Opis:**
CSS Injection to podatność, która pozwala atakującemu wstrzyknąć złośliwy kod CSS do strony internetowej. Może to prowadzić do zmiany wyglądu strony, ukrywania treści lub kradzieży danych użytkowników poprzez manipulację stylami.
HTML Injection to podatność, która pozwala atakującemu na wstrzyknięcie złośliwego kodu HTML do strony internetowej. Atakujący może wykorzystać tę podatność do zmiany zawartości strony, kradzieży danych użytkowników lub wykonywania innych złośliwych działań. HTML Injection różni się od Cross-Site Scripting (XSS) tym, że XSS zazwyczaj umożliwia wstrzykiwanie skryptów (JavaScript), podczas gdy HTML Injection koncentruje się na wstrzykiwaniu tagów HTML.

Podstrona z funkcją, która pozwala użytkownikowi na personalizację wyglądu poprzez ustawienie koloru tła (Background color) nie sanitarizuje ani nie koduje wprowadzonych danych, pozwalając na wstrzyknięcie tagów html.

---

**Technika eksploitacji:**
Atakujący wprowadza payload HTML jako wartość koloru tła, np.:

`<h1>infected</h1>`

Taki są odczytywane jako taki, a nie zwykły tekst i wypisuje większą czcionką tekst "infected".
![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/56219452/2441eb84-dbf6-45d8-b0ae-e1e55c454ce7)


**Mitygacja:**
1. Walidacja i Sanityzacja Wprowadzanych Danych: Upewnij się, że wszelkie dane wejściowe są dokładnie sprawdzane przed ich przetworzeniem. Odrzuć wszelkie dane, które zawierają tagi HTML lub CSS.
2. Kodowanie Wprowadzanych Danych: Zastosuj odpowiednie kodowanie, takie jak HTML entity encoding, aby wszystkie specjalne znaki w danych wejściowych były traktowane jako zwykły tekst, a nie jako kod HTML/CSS.
3. Użycie Whitelistingu: Ogranicz dozwolone wartości dla danych wejściowych tylko do tych, które są bezpieczne i oczekiwane, np. tylko dozwolone kolory w formacie HEX.
4. Nagłówki HTTP: Użyj nagłówków HTTP takich jak Content-Security-Policy (CSP), aby ograniczyć możliwość wstrzykiwania złośliwego kodu.
5. Bezpieczne Frameworki i Biblioteki: Użyj frameworków i bibliotek, które automatycznie sanitizują dane wejściowe, np. ORM dla bazy danych, czy też biblioteki do renderowania HTML.
