## Nazwa podatności: JSON Injection - Reflective XSS Attack

**Istotność:** 8

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
1. Walidacja i sanityzacja danych wejściowych: Waliduj i sanityzuj wszystkie dane wejściowe zanim zostaną przetworzone i umieszczone w strukturze JSON. Upewnij się, że akceptowane są tylko dozwolone znaki i formaty danych.
2. Kodowanie danych wyjściowych: Zawsze koduj dane, które mają być wyświetlone na stronie lub przetworzone przez przeglądarkę. Użyj odpowiednich metod kodowania, takich jak JavaScript encoding i HTML encoding, aby zapobiec wstrzyknięciu złośliwego kodu.
3. Używanie bibliotek do przetwarzania JSON: Korzystaj z bezpiecznych bibliotek do parsowania i generowania JSON, które automatycznie zabezpieczają dane przed wstrzyknięciem kodu.
4. Content Security Policy (CSP): Wdróż nagłówki Content Security Policy, aby ograniczyć wykonanie nieautoryzowanego JavaScript na stronie. CSP może pomóc w ograniczeniu miejsc, z których może być wykonywany JavaScript.
5. Nagłówki HTTP: Upewnij się, że używasz odpowiednich nagłówków HTTP, takich jak X-Content-Type-Options: nosniff, aby zapobiec błędnej interpretacji typu zawartości przez przeglądarkę.
6. Bezpieczne generowanie JSON: Upewnij się, że serwer poprawnie generuje odpowiedzi JSON, unikając interpolacji danych wejściowych bez odpowiedniej walidacji i kodowania.
7. Bezpieczne zarządzanie sesjami: Używaj flagi HttpOnly dla ciasteczek sesji, aby zapobiec ich odczytowi przez skrypty JavaScript w przypadku skutecznego ataku XSS.
