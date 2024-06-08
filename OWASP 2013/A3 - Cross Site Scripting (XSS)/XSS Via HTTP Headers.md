## Nazwa podatności: Reflected XSS

**Istotność:** 9

---

**Opis:**
Reflected XSS to rodzaj ataku typu Cross-Site Scripting, który ma miejsce, gdy aplikacja internetowa natychmiastowo odbija dane wejściowe dostarczone przez użytkownika bez ich odpowiedniego przetworzenia i wyświetla je na stronie internetowej. Atakujący może wstrzyknąć złośliwy kod JavaScript do formularza lub parametru URL, który następnie zostanie wyświetlony i wykonany w przeglądarce ofiary.
Może to prowadzić do kradzieży ciasteczek sesyjnych, przechwytywania danych użytkowników, a nawet przejęcia konta.

---

**Technika eksploitacji:**
Na stronie http://192.168.255.133/mutillidae/index.php?page=browser-info.php należy do żądania GET wstrzyknąć na koniec User Agenta ciąg

```
"><script>alert("XSS");</script>
```

![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/56219452/67dddf13-bbbd-4311-9e92-5c1e4ec61386)

Po przesłaniu tak zmodyfikowanego zapytania wywoływane jest powiadomienie z zadaną zawartością.

![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/56219452/50e1278b-9081-4941-8718-9799de341146)

**Mitygacja:**
1. Kodowanie danych wejściowych: Zawsze koduj dane wejściowe przed ich wyświetleniem na stronie. Używaj HTML entity encoding, aby zamienić specjalne znaki na ich odpowiedniki HTML (np. > na \&gt;, < na \&lt;, " na \&quot;).
1. Walidacja danych wejściowych: Waliduj wszystkie dane wejściowe, aby upewnić się, że zawierają tylko dozwolone znaki i formaty. Odrzuć dane, które mogą zawierać złośliwy kod. W przypadku nagłówka User-Agent, sprawdź, czy zawiera tylko dozwolone znaki.
1. Content Security Policy (CSP): Wdróż Content Security Policy, aby ograniczyć możliwość wykonania nieautoryzowanego JavaScript. CSP może pomóc w kontrolowaniu, skąd mogą być ładowane i wykonywane skrypty.
1. HttpOnly i Secure Cookies: Ustaw flagi HttpOnly i Secure dla ciasteczek, aby zapobiec ich odczytowi przez skrypty JavaScript oraz zapewnić, że są przesyłane tylko przez bezpieczne połączenia HTTPS.
1. Unikanie dynamicznego HTML: Unikaj bezpośredniego wstawiania danych wejściowych użytkownika do HTML. Zamiast tego, korzystaj z bezpiecznych metod renderowania szablonów, które oddzielają dane od logiki prezentacji.
1. Użycie whitelistingu: Stosuj whitelisting dla danych wejściowych, aby ograniczyć możliwe wartości tylko do tych, które są bezpieczne i oczekiwane.
1. Bezpieczne frameworki: Korzystaj z frameworków i bibliotek webowych, które automatycznie sanityzują dane wejściowe i kodują dane wyjściowe, minimalizując ryzyko XSS.
