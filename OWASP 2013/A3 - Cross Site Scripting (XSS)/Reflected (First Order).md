## Nazwa podatności: XSS Reflected (First Order)

**Istotność:** Średnia

---

**Opis:**
XSS Reflected (First Order) to rodzaj ataku typu Cross-Site Scripting, który ma miejsce, gdy aplikacja internetowa natychmiastowo odbija dane wejściowe dostarczone przez użytkownika bez ich odpowiedniego przetworzenia i wyświetla je na stronie internetowej. Atakujący może wstrzyknąć złośliwy kod JavaScript do formularza lub parametru URL, który następnie zostanie wyświetlony i wykonany w przeglądarce ofiary. 
Może to prowadzić do kradzieży ciasteczek sesyjnych, przechwytywania danych użytkowników, a nawet przejęcia konta.

---

**Technika eksploitacji:**
Strona przedstawia się nastepująco:
![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/28838004/9173b5e0-7bda-449c-a5d5-6c50e30b4bf4)

Po wpisaniu wartości jest ona wyświetlana na stronie:
![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/28838004/633c4c87-b66f-40f5-9e3f-816788a5c90c)


Kontekst HTML:
```html
<div class="report-header" reflectedxssexecutionpoint="1" title="">Results for google.com</div>
```

Po podaniu na wejściu payloadu postaci:
`<script>alert(1);</script>`, w następujący sposób:
![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/28838004/21f2c3b8-812b-4e9f-8ab5-16a0113286d8)

Jak widać na poniższym zrzucie ekranu, atak powiódł się, a kod JavaScript został wykonany przez stronę:
![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/28838004/fe058079-9f5d-42e1-9a8e-3bc941d6c11a)

SeleniumTester:
```
python SeleniumTester.py --url <ciąg znaków, zawierający adres ip lub nazwę domeny> --xss-reflected-1
```

---

**Mitygacja podatności:**
Mitygacja podatności powinna obejmować walidację danych wejściowych, aby upewnić się, że wszystkie dane są sprawdzane i filtrowane zgodnie z oczekiwanymi formatami i typami. Należy również kodować wszystkie dane wyjściowe, które mogą zawierać dane użytkownika, używając odpowiednich funkcji do kodowania HTML, takich jak `htmlspecialchars()` w PHP czy `HtmlUtils.htmlEscape()` w Javie. Warto skorzystać z bibliotek i narzędzi przeznaczonych do zabezpieczania aplikacji przed XSS, takich jak OWASP Java Encoder lub Microsoft AntiXSS. Unikanie dynamicznego generowania HTML przy użyciu niezaufanych danych użytkownika oraz regularne przeprowadzanie testów bezpieczeństwa, w tym testów penetracyjnych, pomaga wykrywać i naprawiać podatności XSS. Dodatkowo, należy zachęcać użytkowników do korzystania z przeglądarek, które mają wbudowane mechanizmy ochrony przed XSS, takie jak Content Security Policy (CSP).
