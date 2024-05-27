## Nazwa podatności: Cross-Site Scripting (XSS)

**Istotność:** 8

---

**Opis:**
Manipulacja wartościami nagłówków HTTP, które są następnie odbijane (reflected) na stronie bez odpowiedniej sanacji lub kodowania, co pozwala na wstrzyknięcie i wykonanie kodu HTML/JavaScript.

---

**Technika eksploitacji:**
Złośliwy użytkownik modyfikuje wartość ciasteczka PHPSESSID (lub innego parametru wykorzystywanego przez aplikację) w żądaniu GET, wstawiając tag HTML:

  `<meta http-equiv="refresh" content=*5; URL=https://www.google.com* />`
  
Gdy serwer odbije zmodyfikowane ciasteczko w odpowiedzi HTTP i ta odpowiedź zostanie wyświetlona jako część strony HTML, meta tag zostaje zinterpretowany przez przeglądarkę. Tag ten może przekierować użytkownika na zewnętrzną, potencjalnie złośliwą stronę po upływie określonego czasu (tutaj 5 sekund).

![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/56219452/23a272ec-8a11-46e0-bd12-c4b273ec8015)
