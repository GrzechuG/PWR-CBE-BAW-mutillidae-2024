## Nazwa podatności: HTML Injection

**Istotność:** 5

---

**Opis:**
HTML Injection to podatność, która pozwala atakującemu na wstrzyknięcie złośliwego kodu HTML do strony internetowej. Atakujący może wykorzystać tę podatność do zmiany zawartości strony, kradzieży danych użytkowników lub wykonywania innych złośliwych działań. HTML Injection różni się od Cross-Site Scripting (XSS) tym, że XSS zazwyczaj umożliwia wstrzykiwanie skryptów (JavaScript), podczas gdy HTML Injection koncentruje się na wstrzykiwaniu tagów HTML.
---

**Technika eksploitacji:**
Złośliwy użytkownik modyfikuje wartość ciasteczka PHPSESSID (lub innego parametru wykorzystywanego przez aplikację) w żądaniu GET, wstawiając tag HTML:

  `<h1>infected</h1>`
  

![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/56219452/9d373304-4664-47df-b620-6bce721e3c60)


![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/56219452/00312398-fdc0-4bd1-9f18-2064a178fe5d)

