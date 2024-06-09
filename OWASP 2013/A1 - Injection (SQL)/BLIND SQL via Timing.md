## Nazwa podatności: BLIND SQL via TIMING

**Istotność:** Wysoka

---

**Opis:**
Ze względu na brak sanytyzacji danych wejściowych formularzu na podstronie znajdującej pod następującym się URL "http://192.168.28.131/mutillidae/index.php?page=user-info.php" możliwy jest atak na poufność danych, przez wykonanie eksploitacji BLIND SQL przez użycie funkcji czasowej. Użycie tej techniki pozwala na nieautoryzowany dostęp do danych przechowywanych w bazie danych lub poznanie struktury systemu przez charakterystyczne oczekiwanie na wykonanie zapytania. Funkcja SLEEP(n) jest charakterystyczna dla bazy danych mysql i pozwala na opóźnienie zapytania o określony czas(n). Na podanej stronie uzyskujemy bezpośredni dostęp do danych logowania użytkownika, a dokładniej do nazwy użytkownika oraz hasła. 
![obraz](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/93217316/7ab2f724-c576-4fa6-af5e-c7fb06431638)


---

**Technika eksploitacji:**
Ze względu na brak zabezpieczenia formularza, możliwe jest wprowadzenie dodatkowych danych przez atakującego, które całkowicie modyfikuje bezpośrednio zapytanie w języku SQL, doprowadzając do zwrócenia większej ilości informacji, niż jest to planowane. Umieszcznie wyrażenia "'-SLEEP(1) -- " w polu formularza związengo z wprowadzeniem nazwy użytkownika przekształca zapytanie SQL z |SELECT * FROM accounts WHERE username='admin' AND password='password'| na |SELECT * FROM accounts WHERE username=''-SLEEP(1) -- 'AND password=''|. Dodanie wyrażenia |'-SLEEP(1) -- | pozwala na stworzenie zapytania, które w normalnych okolicznościach przy pomocy takich funkcji jak IF pozwala na dowiedzenie się więcej o strukturze bazy, jednakże w tym przypadku pozwoliło to na wyświetlenie całej bazy użytkowników.
Metodologia ataku: https://www.sqlinjection.net/time-based/

Polecenie testera:
```
python Tester.py --url http://192.168.64.145/mutillidae/index.php?page=user-info.php --sqli Timing
```

---

**Mitygacja:**
Należy używać prepared statements z parameter binding do wszystkich operacji bazodanowych, aby uniknąć bezpośredniego wstrzykiwania danych wejściowych do zapytań SQL. Należy walidować wszystkie dane wejściowe, upewniając się, że są zgodne z oczekiwanym formatem i typem danych. Należy minimalizować uprawnienia kont bazy danych używanych przez aplikację, aby ograniczyć potencjalne szkody wynikające z udanych ataków SQL Injection. 
