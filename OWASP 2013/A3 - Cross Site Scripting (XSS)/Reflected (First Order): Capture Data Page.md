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

**Mitygacja:**
1. Kodowanie danych wejściowych: Zawsze koduj dane wejściowe, zanim zostaną one umieszczone w odpowiedzi HTML. Użyj odpowiedniego kodowania, takiego jak HTML entity encoding, aby zapobiec wykonaniu wstrzykniętego kodu.
1. Walidacja i sanityzacja danych wejściowych: Waliduj wszystkie dane wejściowe, w tym wartości nagłówków HTTP i ciasteczek. Upewnij się, że zawierają tylko dozwolone znaki i formaty.
1. HttpOnly i Secure Cookies: Ustaw flagi HttpOnly i Secure dla ciasteczek, aby uniemożliwić ich modyfikację przez JavaScript i ograniczyć ich przesyłanie, aby było możliwe tylko przez bezpieczne połączenia HTTPS.
1. Content Security Policy (CSP): Wdróż nagłówki Content Security Policy, aby ograniczyć możliwość wykonania nieautoryzowanego kodu JavaScript. CSP może pomóc w ograniczeniu miejsc, z których JavaScript może być ładowany i wykonywany.
1. Bezpieczne parsowanie nagłówków: Unikaj bezpośredniego odbijania wartości nagłówków HTTP w odpowiedziach HTML. Zamiast tego przetwarzaj i parsuj je w sposób bezpieczny, który uniemożliwia wstrzyknięcie kodu.
1. Bezpieczne frameworki: Korzystaj z frameworków webowych, które automatycznie sanitizują dane wejściowe i kodują dane wyjściowe, minimalizując ryzyko XSS.
1. Wykrywanie i monitorowanie: Implementuj mechanizmy wykrywania i monitorowania prób ataków XSS, aby szybko reagować na potencjalne zagrożenia.
1. Unikanie dynamicznego HTML: Unikaj generowania dynamicznego HTML na podstawie danych wejściowych użytkownika bez odpowiedniego kodowania i walidacji.
