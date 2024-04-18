## Nazwa podatności: XSS: HTMLi via HTTP Header

**Istotność:** 10

---

**Opis:**
Ze względu na brak sanytyzacji danych wejściowych formularzu na podstronie znajdującej pod następującym się URL "http://192.168.28.131/mutillidae/index.php?page=user-info.php" możliwy jest atak na poufność danych, przez wykonanie eksploitacji SQL INJECTION pozwalając na nieautoryzowany dostęp do danych przechowywanych w bazie danych. Na podanej stronie uzyskujemy bezpośredni dostęp do danych logowania użytkownika, a dokładniej do nazwy użytkownika oraz hasła. 



---

**Technika eksploatacji:**
Ze względu na brak zabezpieczenia formularza, możliwe jest wprowadzenie dodatkowych danych przez atakującego, które całkowicie modyfikuje bezpośrednio zapytanie w języku SQL, doprowadzając do zwrócenia większej ilości informacji, niż jest to planowane. Umieszcznie wyrażenia "' or 1=1 -- " w polu formularza związengo z wprowadzeniem nazwy użytkownika przekształca zapytanie SQL z |SELECT * FROM accounts WHERE username='admin' AND password='password'| na |SELECT * FROM accounts WHERE username='' or 1=1 -- 'AND password=''|. Dodanie wyrażenia |' or 1=1 -- | pozwala na stworzenie zapytania, który zawsze będzie prawdą (1=1) a dopisek '--' umieszcza dalszą część zapytania jako komentarz, przez co atakujący nie potrzebuje znać hasła a dodatkowo nie generuje w ten sposób błędu.
Metodologia ataku: https://www.sqlinjection.net/string-parameters/
