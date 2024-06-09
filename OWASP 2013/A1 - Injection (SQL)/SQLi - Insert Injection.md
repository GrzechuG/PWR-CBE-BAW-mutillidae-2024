## Nazwa podatności: SQL Injection

**Istotność:** 9

---

**Opis:**
Ze względu na brak sanityzacji danych wejściowych z pola **password** pod adresem (http://192.168.255.133/mutillidae/index.php?page=register.php), możliwy jest atak przez wykonanie eksploitacji SQL INSERT INJECTION oraz atak na poufność informacji.


---

**Technika eksploitacji:**
Ze względu na brak zabezpieczenia formularza, możliwe jest wprowadzenie dodatkowych danych przez atakującego, które bezpośrednio modyfikuje zapytanie w języku SQL, doprowadzając do wykonania podzapytania i zwrócenia większej ilości informacji, niż jest to planowane w sposób, który umożliwia uzyskanie tej informacji po zalogowaniu się przez utworzonego użytkownika

![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/56219452/573ce875-fdc1-40e5-ae9e-ff375f2a86a4)


Umieszczenie w pierwszym polu wybranej nazwy użytkownika i 
```
  x', (select version())) -- -
```
w polu z hasłem i potwierdzeniem hasła skutkuje utworzeniem konta użytkownika o wybranej nazwie z wersją serwera SQL obok nazwy użytkownika (widoczne po zalogowaniu).

![insert-register](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/56219452/33892823-de06-44e2-8ff6-0513e7944a48)

Tester:
```
python Tester.py --url http://192.168.64.145/mutillidae/index.php?page=add-to-your-blog.php --sqli Insert
```

---

**Mitygacja:**
1. Używanie parametryzowanych zapytań: Zawsze używaj parametryzowanych zapytań (prepared statements) zamiast dynamicznego generowania zapytań SQL z danymi użytkownika.
2. Sanityzacja i walidacja danych wejściowych: Waliduj i sanityzuj wszystkie dane wejściowe, upewniając się, że zawierają tylko dozwolone znaki. Na przykład, pola przeznaczone na hasło powinny akceptować tylko bezpieczne znaki alfanumeryczne.
3. Użycie ORM (Object-Relational Mapping): Korzystaj z bibliotek ORM, które automatycznie chronią przed atakami SQL Injection poprzez separację danych wejściowych od zapytań SQL.
4. Minimalne uprawnienia: Przyznaj bazie danych minimalne uprawnienia wymagane do działania aplikacji. Unikaj używania użytkowników bazy danych z uprawnieniami administracyjnymi.
5. Wykrywanie i monitorowanie: Implementuj mechanizmy wykrywania i monitorowania nieautoryzowanych działań w bazie danych, takie jak logowanie prób wstrzyknięcia SQL i inne podejrzane aktywności.
6. Zasady bezpieczeństwa: Ustal i egzekwuj zasady bezpiecznego kodowania, które obejmują unikanie bezpośredniego używania danych użytkownika w zapytaniach SQL.
