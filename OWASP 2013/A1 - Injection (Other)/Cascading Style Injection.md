## Nazwa podatności: CSS Injection

**Istotność:** 5

---

**Opis:**
HTML Injection to podatność, która pozwala atakującemu na wstrzyknięcie złośliwego kodu HTML do strony internetowej. Atakujący może wykorzystać tę podatność do zmiany zawartości strony, kradzieży danych użytkowników lub wykonywania innych złośliwych działań. HTML Injection różni się od Cross-Site Scripting (XSS) tym, że XSS zazwyczaj umożliwia wstrzykiwanie skryptów (JavaScript), podczas gdy HTML Injection koncentruje się na wstrzykiwaniu tagów HTML.

Podstrona z funkcją, która pozwala użytkownikowi na personalizację wyglądu poprzez ustawienie koloru tła (Background color) nie sanitarizuje ani nie koduje wprowadzonych danych, pozwalając na wstrzyknięcie tagów html.

---

**Technika eksploitacji:**
Atakujący wprowadza payload HTML jako wartość koloru tła, np.:

`<h1>infected</h1>`

Taki są odczytywane jako taki, a nie zwykły tekst i wypisuje większą czcionką tekst "infected".
![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/56219452/2441eb84-dbf6-45d8-b0ae-e1e55c454ce7)

