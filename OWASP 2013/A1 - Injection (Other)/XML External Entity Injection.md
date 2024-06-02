## Nazwa podatności: XML External Entity Injection

**Istotność:** Wysoka

---

**Opis:**
Możliwe jest w programie 'XML Validator' na wykonanie dowolnego kodu jak wyświetlenie zawartości krytycznych plików na systemie przez spreparowanie odpowiedniego kodu w XML.
![obraz](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/93217316/7d1c4e9b-ab51-4e25-bf8d-c10ee82af982)

---

**Technika eksploitacji:**
W tym przypadku kiedy parser XML natrafi na '&xxe;' wewnątrz '<foo>', zastąpi to fragmentem tekstu wskazywanym przez zdefiniowaną encję(specjalny typ konstrukcji, która reprezentuje pewien zestaw znaków lub ciąg znaków) xxe (encja, która odnosi się do zasobów zewnętrznych, takich jak pliki tekstowe). W tym przypadku xxe wskazuje na zawartość pliku /etc/passwd.

Główną częścią eksploitacji jest zewnętrzna xxe, która wskazuje na plik /etc/passwd.
```
<!ENTITY xxe SYSTEM "file:///etc/passwd" >
```
Po zdefiniowaniu encji, tworzony jest nowy element foo z zawartością pliku /etc/passwd i wyświetlany przez validator.
```
<foo>&xxe;</foo>
```

Źródło: https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/XXE%20Injection/README.md

---

**Mitygacja:**
Należy wyłączyć możliwość przetwarzania zewnętrznych encji w parserach XML, na przykład ustawiając opcje takie jak XMLParser.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true). Należy także walidować i sanityzować wszystkie dane wejściowe, aby upewnić się, że nie zawierają niebezpiecznych konstrukcji XML, takich jak DTD. 
