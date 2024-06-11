## Nazwa podatności: Wykonanie dowolnego kodu w systemie w aplikacji 'DNS Lookup'

**Istotność:** Wysoka

---

**Opis:**

Ze względu na to, że aplikacja używa bezpośreniego polecenia systemowego do wykonania zapytania domenowego, możliwe jest wykonanie dowolnego kodu przez brak sanityzacji wpisywanego tekstu.
![obraz](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/93217316/f8425a5f-3c7a-4225-9599-38af212c9d27)


---

**Technika eksploitacji:**
Atakujący może po wpisaniu dowolnego tekstu, spróbować przy pomocy zarezerwowanych znaków specjalnych (np. '&', '&&', '||') wykonać następne polecenie, które ze względu na brak sanityzacji tekstu są wykonywane bezpośrednio w systemie. Pozwala to adwersarzowi na wyświetlenie dowolnego pliku w obrębie uprawnień użytkownika (np. '127.0.0.1 && cat /etc/passwd') lub wykonanie dowolnej akcji na systemie. 

Tester:
```
python Tester.py --url <ciąg znaków, zawierający adres ip lub nazwę domeny> --comminj AND
```

SeleniumTester:
```
python SeleniumTester.py --url <ciąg znaków, zawierający adres ip lub nazwę domeny> --command
```

---
**Mitygacja:**
Aby zmitigować code injection, kluczowe jest stosowanie ścisłej walidacji wejścia, co oznacza przyjmowanie tylko danych spełniających określone kryteria. W tym przypadku należy wyfiltrować znaki taki jak np. '&', '&&', '||'. Dodatkowo, należy wdrożyć sanityzacje danych wejściowych, która polega na usuwaniu lub kodowaniu specjalnych znaków, które mogą być używane do wstrzykiwania złośliwego kodu, co minimalizuje ryzyko wykonania nieautoryzowanych operacji.
