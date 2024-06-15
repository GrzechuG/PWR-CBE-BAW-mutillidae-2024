## Nazwa podatności: XSS Reflected - Set Background Colour page

**Istotność:** Wysoka

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

SeleniumTester:
```
python SeleniumTester.py --url <ciąg znaków, zawierający adres ip lub nazwę domeny> --xss-reflected-2
```

**Mitygacja:**
Mitygacja podatności powinna obejmować walidację i sanityzację danych wejściowych, aby upewnić się, że wszystkie dane są sprawdzane i filtrowane zgodnie z oczekiwanymi formatami i typami. Należy również kodować wszystkie dane wejściowe, używając odpowiednich funkcji do kodowania HTML, takich jak htmlspecialchars() w PHP czy HtmlUtils.htmlEscape() w Javie. Warto skorzystać z bibliotek i narzędzi przeznaczonych do zabezpieczania aplikacji przed XSS, takich jak OWASP Java Encoder lub Microsoft AntiXSS. Unikanie dynamicznego generowania HTML przy użyciu niezaufanych danych użytkownika oraz regularne przeprowadzanie testów bezpieczeństwa, w tym testów penetracyjnych, pomaga wykrywać i naprawiać podatności XSS. Dodatkowo, należy zachęcać użytkowników do korzystania z przeglądarek, które mają wbudowane mechanizmy ochrony przed XSS, takie jak Content Security Policy (CSP).
Wdrożenie nagłówków CSP pozwoli ograniczyć możliwość wykonania nieautoryzowanego kodu JavaScript.
