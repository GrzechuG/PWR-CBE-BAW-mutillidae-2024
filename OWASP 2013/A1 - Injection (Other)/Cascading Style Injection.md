## Nazwa podatności: HTML/CSS Injection

**Istotność:** Niska

---

**Opis:**
CSS Injection to podatność, która pozwala atakującemu wstrzyknąć złośliwy kod CSS do strony internetowej. Może to prowadzić do zmiany wyglądu strony, ukrywania treści lub kradzieży danych użytkowników poprzez manipulację stylami.
HTML Injection to podatność, która pozwala atakującemu na wstrzyknięcie złośliwego kodu HTML do strony internetowej. Atakujący może wykorzystać tę podatność do zmiany zawartości strony, kradzieży danych użytkowników lub wykonywania innych złośliwych działań. HTML Injection różni się od Cross-Site Scripting (XSS) tym, że XSS zazwyczaj umożliwia wstrzykiwanie skryptów (JavaScript), podczas gdy HTML Injection koncentruje się na wstrzykiwaniu tagów HTML.

Podstrona z funkcją, która pozwala użytkownikowi na personalizację wyglądu poprzez ustawienie koloru tła (Background color) nie sanitarizuje ani nie koduje wprowadzonych danych, pozwalając na wstrzyknięcie tagów html.

---

**Technika eksploitacji:**
Atakujący wprowadza payload HTML/CSS jako wartość koloru tła, np.:

`<style type="text/css">body { color: #40f4cd }</style>`

Tagi są odczytywane jako tagi, a nie zwykły tekst i tekst na stronie zmienia kolor na zadany w skrypcie.
![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/56219452/35ebe69f-2ca5-4b3d-b322-4613bbf5b0e1)

SeleniumTester:
```
python SeleniumTester.py --url <ciąg znaków, zawierający adres ip lub nazwę domeny> --css
```


**Mitygacja:**
1. Walidacja i sanityzacja wprowadzanych danych: Upewnij się, że wszelkie dane wejściowe są dokładnie sprawdzane przed ich przetworzeniem. Odrzuć wszelkie dane, które zawierają tagi HTML lub CSS.
2. Kodowanie wprowadzanych danych: Zastosuj odpowiednie kodowanie, takie jak HTML entity encoding, aby wszystkie specjalne znaki w danych wejściowych były traktowane jako zwykły tekst, a nie jako kod HTML/CSS.
3. Użycie whitelistingu: Ogranicz dozwolone wartości dla danych wejściowych tylko do tych, które są bezpieczne i oczekiwane, np. tylko dozwolone kolory w formacie HEX.
4. Nagłówki HTTP: Użyj nagłówków HTTP takich jak Content-Security-Policy (CSP), aby ograniczyć możliwość wstrzykiwania złośliwego kodu.
5. Bezpieczne frameworki i biblioteki: Użyj frameworków i bibliotek, które automatycznie sanitizują dane wejściowe, np. ORM dla bazy danych, czy też biblioteki do renderowania HTML.
