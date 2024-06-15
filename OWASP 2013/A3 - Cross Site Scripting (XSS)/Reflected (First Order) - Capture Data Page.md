## Nazwa podatności: XSS Reflected - Capture Data page

**Istotność:** Wysoka

---

**Opis:**
Manipulacja wartościami nagłówków HTTP, które są następnie odbijane (reflected) na stronie bez odpowiedniej sanacji lub kodowania, co pozwala na wstrzyknięcie i wykonanie kodu HTML/JavaScript.

---

**Technika eksploitacji:**
Złośliwy użytkownik modyfikuje wartość ciasteczka PHPSESSID (lub innego parametru wykorzystywanego przez aplikację) w żądaniu GET, wstawiając tag HTML:

  `<meta http-equiv="refresh" content=*5; URL=https://www.google.com* />`

Gdy serwer odbije zmodyfikowane ciasteczko w odpowiedzi HTTP i ta odpowiedź zostanie wyświetlona jako część strony HTML, meta tag zostaje zinterpretowany przez przeglądarkę. Tag ten może przekierować użytkownika na zewnętrzną, potencjalnie złośliwą stronę po upływie określonego czasu (tutaj 5 sekund).

![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/56219452/23a272ec-8a11-46e0-bd12-c4b273ec8015)

**Mitygacja:**
Mitygacja podatności powinna obejmować walidację i sanityzację danych wejściowych, aby upewnić się, że wszystkie dane są sprawdzane i filtrowane zgodnie z oczekiwanymi formatami i typami. Należy również kodować wszystkie dane wejściowe, używając odpowiednich funkcji do kodowania HTML, takich jak htmlspecialchars() w PHP czy HtmlUtils.htmlEscape() w Javie. Warto skorzystać z bibliotek i narzędzi przeznaczonych do zabezpieczania aplikacji przed XSS, takich jak OWASP Java Encoder lub Microsoft AntiXSS. Unikanie dynamicznego generowania HTML przy użyciu niezaufanych danych użytkownika oraz regularne przeprowadzanie testów bezpieczeństwa, w tym testów penetracyjnych, pomaga wykrywać i naprawiać podatności XSS. Dodatkowo, należy zachęcać użytkowników do korzystania z przeglądarek, które mają wbudowane mechanizmy ochrony przed XSS, takie jak Content Security Policy (CSP).
Wdrożenie nagłówków CSP pozwoli ograniczyć możliwość wykonania nieautoryzowanego kodu JavaScript.
