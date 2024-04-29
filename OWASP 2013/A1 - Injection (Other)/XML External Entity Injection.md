## Nazwa podatności: XML External Entity Injection

**Istotność:** 10

---

**Opis:**
Możliwe jest w programie 'XML Validator' na wykonanie dowolnego kodu jak wyświetlenie zawartości krytycznych plików na systemie przez spreparowanie odpowiedniego kodu w XML.
![obraz](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/93217316/7d1c4e9b-ab51-4e25-bf8d-c10ee82af982)

---

**Technika eksploatacji:**
W tym przypadku kiedy parser XML natrafi na '&xxe;' wewnątrz '<foo>', zastąpi to fragmentem tekstu wskazywanym przez zdefiniowaną encję(specjalny typ konstrukcji, która reprezentuje pewien zestaw znaków lub ciąg znaków) xxe (encja, która odnosi się do zasobów zewnętrznych, takich jak pliki tekstowe). W tym przypadku xxe wskazuje na zawartość pliku /etc/passwd.

Źródło: https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/XXE%20Injection/README.md
