## Nazwa podatności: XSS Reflected (First Order)

**Istotność:** 9

---

**Opis:**
XSS Reflected (First Order) to rodzaj ataku typu Cross-Site Scripting, który ma miejsce, gdy aplikacja internetowa natychmiastowo odbija dane wejściowe dostarczone przez użytkownika bez ich odpowiedniego przetworzenia i wyświetla je na stronie internetowej. Atakujący może wstrzyknąć złośliwy kod JavaScript do formularza lub parametru URL, który następnie zostanie wyświetlony i wykonany w przeglądarce ofiary. 
Może to prowadzić do kradzieży ciasteczek sesyjnych, przechwytywania danych użytkowników, a nawet przejęcia konta.

---

**Technika eksploitacji:**
Strona przedstawia się nastepująco:
![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/28838004/9173b5e0-7bda-449c-a5d5-6c50e30b4bf4)

Po wpisaniu wartości jest ona wyświetlana na stronie:
![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/28838004/7c3a0623-fa3f-42df-a272-9c2927bf37db)

Kontekst HTML:
![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/28838004/6c7cedac-2326-4dbb-9b63-4b01bce68063)

Po podaniu na wejściu payloadu postaci:
`<script>alert(1);</script>`, w następujący sposób:
![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/28838004/21f2c3b8-812b-4e9f-8ab5-16a0113286d8)


---

**Mitygacja podatności:**
Mitygacja podatności powinna obejmować walidację danych wejściowych, aby upewnić się, że wszystkie dane są sprawdzane i filtrowane zgodnie z oczekiwanymi formatami i typami. Należy również kodować wszystkie dane wyjściowe, które mogą zawierać dane użytkownika, używając odpowiednich funkcji do kodowania HTML, takich jak `htmlspecialchars()` w PHP czy `HtmlUtils.htmlEscape()` w Javie. Warto skorzystać z bibliotek i narzędzi przeznaczonych do zabezpieczania aplikacji przed XSS, takich jak OWASP Java Encoder lub Microsoft AntiXSS. Unikanie dynamicznego generowania HTML przy użyciu niezaufanych danych użytkownika oraz regularne przeprowadzanie testów bezpieczeństwa, w tym testów penetracyjnych, pomaga wykrywać i naprawiać podatności XSS. Dodatkowo, należy zachęcać użytkowników do korzystania z przeglądarek, które mają wbudowane mechanizmy ochrony przed XSS, takie jak Content Security Policy (CSP).
