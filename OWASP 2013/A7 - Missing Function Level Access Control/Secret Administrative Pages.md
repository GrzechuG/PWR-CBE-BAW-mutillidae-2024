## Nazwa podatności: Dostęp do wrażliwych stron oraz plików przez parametr 'page'

**Istotność:** 10

---

**Opis:**
Możliwe jest wyeksploitowanie parametru page na stronie "http://192.168.64.141/mutillidae/index.php?page=" przez wpisanie dowolnej podstrony lub odpowiedniej ściezki do pliku na systemie, aby uzyskać dostęp do dowolnej domyślnej administracyjnej podstrony z wrażliwymi danymi lub pliku na systemie takim jak lista użytkowników na systemie.
![obraz](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/93217316/e0d1e7b0-f2a0-4fdd-9a5d-1bb7412d0946)

---

**Technika eksploatacji:**
Możliwa jest enumeracja podstron przez parametr 'page=' przy pomocy dowolnego oprogramowania lub skryptu lub przez ręczne umieszczenie tekstu. Aby móc spróbować wyeksportować pliki systemowe trzeba użyć w parametrze poprzedzić to przez wyrażenie "file:///". Do wylistowania podstron został wykorzystany prosty skrypt, którego wynik widać poniżej:
![obraz](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/93217316/fa89cdd2-95ec-4702-88b7-cde0ca9884a4)

Źródło listy z licencją MIT:
https://github.com/danielmiessler/SecLists/tree/master
