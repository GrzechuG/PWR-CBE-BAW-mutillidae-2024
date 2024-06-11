## Nazwa podatności: Dostęp do wrażliwych stron oraz plików przez parametr 'page'

**Istotność:** Wysoka

---

**Opis:**
Możliwe jest wyeksploitowanie parametru page na stronie "http://192.168.64.141/mutillidae/index.php?page=" przez wpisanie dowolnej podstrony lub odpowiedniej ściezki do pliku na systemie, aby uzyskać dostęp do dowolnej domyślnej administracyjnej podstrony z wrażliwymi danymi lub pliku na systemie takim jak lista użytkowników na systemie.
![obraz](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/93217316/e0d1e7b0-f2a0-4fdd-9a5d-1bb7412d0946)

---

**Technika eksploitacji:**
Możliwa jest enumeracja podstron przez parametr 'page=' przy pomocy dowolnego oprogramowania lub skryptu lub przez ręczne umieszczenie tekstu. Aby móc spróbować wyeksportować pliki systemowe trzeba użyć w parametrze poprzedzić to przez wyrażenie "file:///". Do wylistowania podstron został wykorzystany prosty skrypt, którego wynik widać poniżej:
![obraz](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/93217316/4756da36-9019-4799-b809-c0e0c3451d3e)

Program:
```
python SecretAdminitrativePagesEnumeration.py --url "http://<adres IP>/mutillidae/index.php?page=" --list lista_url_php.txt --klucz "404 Not Found"
```


Źródło danych z licencją MIT:
https://github.com/danielmiessler/SecLists/tree/master

---

**Mitygacja:**
Należy ścisłe walidować parametr 'page', upewniając się, że zawiera on tylko poprawne wartości. Warto również stosować mechanizmy kontroli dostępu, aby upewnić się, że użytkownicy mają tylko dostęp do stron i plików, do których są uprawnieni. W przypadku serwera Apache możliwe jest użycie odpowiednich reguł w konfiguracji serwera, takich jak .htaccess, aby ograniczyć dostęp do określonych katalogów lub plików.
