## Nazwa podatności: Frame Source Injection

**Istotność:** Średnia

---

**Opis:**
Podczas wyświetlania zawartości na stronie innych podstron przez funkcjonalność iframe, możliwe jest wykonanie iframe src injection, które pozwala na wyświetlenie dowolnej strony.  Atakujący dla przykładu mogą wstrzyknąć adres URL do złośliwej strony internetowej z odpowiednio spreparowanym formularzem, a następnie nakłonić użytkownika do przekazania swoich poświadczeń.
![obraz](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/93217316/af00cdf2-1e50-4980-be2f-d9aadc33bd67)


---

**Technika eksploitacji:**
Atakujący po analizie URI i użyciu zmiennej "PathToDocument=" jest w stanie wstrzyknąć dowolny kod na stronie, jednakże nie jest możliwe wyświetlenie plików systemowych. Możliwe jest wykonanie wspomnianej podatności iframe src injection na umieszczenie dowolnej podstrony, na dodatek pozwalając na formatowanie okna w obrębie danego DIV, aby zwiększyć potencjlną wiarygodność okna. W przypadku omawianej podatności została wyświetlona strona eporta.pwr.edu.pl
```
<iframe src=https://eportal.pwr.edu.pl/>
```

**Mitygacja:**
Należy upewnić się, że elementy iframe ładowane są tylko z zaufanych źródeł, unikając dynamicznego ustawiania źródeł iframe na podstawie danych wejściowych użytkownika bez odpowiedniej walidacji i sanityzacji.  Należy skonfigurować Content Security Policy (CSP), aby ograniczyć źródła treści, które mogą być załadowane do iframe. Należy używać nagłówków takich jak X-Frame-Options (np. DENY lub SAMEORIGIN), aby ograniczyć możliwość osadzania treści w iframe przez nieautoryzowane źródła.
