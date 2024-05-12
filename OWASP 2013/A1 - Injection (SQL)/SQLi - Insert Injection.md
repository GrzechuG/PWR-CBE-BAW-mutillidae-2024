## Nazwa podatności: SQL Injection

**Istotność:** 10

---

**Opis:**
Ze względu na brak sanityzacji danych wejściowych z pola **password** pod adresem (http://192.168.255.133/mutillidae/index.php?page=register.php), możliwy jest atak przez wykonanie eksploitacji SQL INSERT INJECTION oraz atak na poufność informacji.


---

**Technika eksploatacji:**
Ze względu na brak zabezpieczenia formularza, możliwe jest wprowadzenie dodatkowych danych przez atakującego, które bezpośrednio modyfikuje zapytanie w języku SQL, doprowadzając do wykonania podzapytania i zwrócenia większej ilości informacji, niż jest to planowane w sposób, który umożliwia uzyskanie tej informacji po zalogowaniu się przez utworzonego użytkownika

![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/56219452/573ce875-fdc1-40e5-ae9e-ff375f2a86a4)


Umieszczenie w pierwszym polu wybranej nazwy użytkownika i 
  x', (select version())) -- -
w polu z hasłem i potwierdzeniem hasła skutkuje utworzeniem konta użytkownika o wybranej nazwie z wersją serwera SQL obok nazwy użytkownika (widoczne po zalogowaniu).

![insert-register](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/56219452/33892823-de06-44e2-8ff6-0513e7944a48)
