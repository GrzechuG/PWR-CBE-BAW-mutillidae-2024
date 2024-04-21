## Nazwa podatności: [Nazwa podatności]

**Istotność:** 6

---

**Opis:**
Podczas wyświetlania zawartości na stronie innych podstron przez funkcjonalność iframe, możliwe jest wykonanie iframe src injection, które pozwala na wyświetlenie dowolnej strony.  Atakujący dla przykładu mogą wstrzyknąć adres URL do złośliwej strony internetowej z odpowiednio spreparowanym formularzem, a następnie nakłonić użytkownika do przekazania swoich poświadczeń.
![obraz](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/93217316/af00cdf2-1e50-4980-be2f-d9aadc33bd67)


---

**Technika eksploatacji:**
Atakujący po analizie URI i użyciu zmiennej "PathToDocument=" jest w stanie wstrzyknąć dowolny kod na stronie, jednakże nie jest możliwe wyświetlenie plików systemowych. Możliwe jest wykonanie wspomnianej podatności iframe src injection na umieszczenie dowolnej podstrony, na dodatek pozwalając na formatowanie okna w obrębie danego DIV, aby zwiększyć potencjlną wiarygodność okna. W przypadku omawianej podatności została wyświetlona strona eporta.pwr.edu.pl
```
<iframe src=https://eportal.pwr.edu.pl/>
```
