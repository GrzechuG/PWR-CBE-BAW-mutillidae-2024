## Nazwa podatności: JSON Injection - Reflective XSS Attack

**Istotność:** Wysoka

---

**Opis:**
Podatność JSON Injection polega na możliwości modyfikacji struktury danych JSON przez wstrzyknięcie nieautoryzowanego kodu, zwykle JavaScript. Jest to rodzaj ataku, który wykorzystuje brak odpowiedniej walidacji danych wejściowych w aplikacjach, które generują lub przetwarzają JSON. W zależności od kontekstu, JSON Injection może prowadzić do różnych form eksploatacji, w tym Cross-Site Scripting (XSS) lub manipulacji danymi przesyłanymi między klientem a serwerem.

---

**Technika eksploitacji:**
Eksploitacja rozpoczyna się od stworzenia payloadu. W tym przypadku jest to ciąg:
```
  "}});alert(1);//
```
Ten fragment kodu jest zaprojektowany tak, aby zakończyć aktualnie trwający blok JSON, zamknąć funkcję JavaScript i wstawić własny skrypt (tutaj **alert(1)**), a następnie skomentować resztę linii, aby zapobiec błędom składniowym z powodu pozostałego oryginalnego kodu.

Atakujący może przekazać złośliwy payload poprzez metody HTTP, które akceptują dane wejściowe od użytkownika, takie jak POST, GET, PUT itp. W opisanym przypadku, payload jest wysyłany jako część żądania POST:

```
  POST /mutillidae/index.php?page=pen-test-tool-lookup.php HTTP/1.1
  ...
  Content-Type: application/x-www-form-urlencoded
  ...
  ToolID=1&pen-test-tool-lookup-php-submit-button=Lookup+Tool
```
  
Zakładając, że wartość ToolID jest następnie używana do generowania odpowiedzi JSON na stronie, złośliwy kod JavaScript może być wstrzyknięty i wykonany w przeglądarce ofiary.

![2 2](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/56219452/c99185ec-6698-4fd1-89f2-6f8b21a42155)

Gdy złośliwe dane są przetworzone przez serwer i nieodpowiednio zabezpieczone przed wyjściem, struktura JSON zostaje zmodyfikowana, a złośliwy skrypt JavaScript jest wykonywany. To może prowadzić do wykonania dowolnych działań JavaScript w kontekście przeglądarki użytkownika, co może obejmować kradzież cookies (jeśli nie są zabezpieczone flagą HttpOnly), manipulację treścią strony, przekierowania na złośliwe strony, a nawet wykonanie działań w imieniu użytkownika.

**Mitygacja:**
Mitygacja podatności powinna obejmować walidację i sanityzację danych wejściowych, aby upewnić się, że wszystkie dane są sprawdzane i filtrowane zgodnie z oczekiwanymi formatami i typami. Należy również kodować wszystkie dane wyjściowe, które mogą zawierać dane użytkownika, używając odpowiednich funkcji do kodowania HTML, takich jak htmlspecialchars() w PHP czy HtmlUtils.htmlEscape() w Javie. Warto skorzystać z bibliotek i narzędzi przeznaczonych do zabezpieczania aplikacji przed XSS, takich jak OWASP Java Encoder lub Microsoft AntiXSS. Unikanie dynamicznego generowania HTML przy użyciu niezaufanych danych użytkownika oraz regularne przeprowadzanie testów bezpieczeństwa, w tym testów penetracyjnych, pomaga wykrywać i naprawiać podatności XSS. Dodatkowo, należy zachęcać użytkowników do korzystania z przeglądarek, które mają wbudowane mechanizmy ochrony przed XSS, takie jak Content Security Policy (CSP).
