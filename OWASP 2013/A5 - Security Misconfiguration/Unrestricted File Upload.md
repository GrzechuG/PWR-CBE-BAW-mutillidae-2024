## Nazwa podatności: Zdalne wykonanie kodu przez wysłanie pliku

**Istotność:** Wysoka
---

**Opis:**
W udostępnionej aplikacji dla użytkowników do wysyłania plików na serwer, możliwe jest wysłanie dowolnego złośliwego pliku, a następnie wykonanie zdalnego kodu do uruchomienia dowolnej akcji na systemie przez parametr 'page'.
![obraz](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/93217316/9662e0cc-70e6-451a-857f-034fdf58150d)
Możliwe jest nawet, nawiązanie zdalnego połączenia przez wykonanie techniki reverse shell, która pozwala na nawiązanie połaczenie ze strony atakowanej maszyny do atakującego, pozwalając na ominiecię podstawowego zabezpieczenia jakim jest translacja adresów NAT. 
![obraz](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/93217316/462bb30a-64ed-4379-bb94-d3f3c5da24d2)

---

**Technika eksploitacji:**

Do przeprowadzenie eksploitacji, należały przygotować odpowiedni złośliwy plik, który po przesłaniu pozwoli na jego wykonanie. W tym przypadku użyto standardowego reverse shella zaprogramowanego przy pomocy języka php. W kodzie skryptu, zedytowano adres IP oraz port docelowy na parametry maszyny atakującej, a następnie przygotowany plik przesłano do systemu.
Po uruchomieniu nasłuchiwania na porcie '1234' na maszynie atakującej przy pomocy narzędzie netcat.
```
nc -nlvp 1234
```
Paremtr 'n' pomija rozwiązanie nazwy domenowej, 'l' uruchamia nasłuchiwanie, 'v' pozwala na zwracanie większej ilości informacji, natomiast 'p' wyszczególnia port.
Następnie uruchomiony złośliwy plik, przez podanie go do podatnego parametru page przez wpisanie lokalizacji pliku:
```
page=/tmp/plik.php
```
Pozwoliło to na zestawienie połączenia z podatną maszyną i wykonanie dowolnego polecenia.


Źródło skryptu: https://github.com/pentestmonkey/php-reverse-shell

---

**Mitygacja podatności:**





