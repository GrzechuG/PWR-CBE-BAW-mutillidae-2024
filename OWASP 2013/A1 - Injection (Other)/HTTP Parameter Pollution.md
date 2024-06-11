## Nazwa podatności: HTTP Parameter Pollution

**Istotność:** Niska

---

**Opis:**
Możliwe jest umieszczenie wielu parametrów w kodzie URI co może pozwolić na wywołanie nieobsłużonego błędu lub wybranie przez użytkownika wielu opcji. Zgodnie z tym co zostało pokazane na obrazie poniżej została wybrana opcja 'nmap' jednak została przekazana opcja 'netcat'.
![obraz](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/93217316/e53c793d-7d84-4346-9d9e-dd8610b062ec)


---

**Technika eksploitacji:**
Atakujący może w kodzie URI umieścić wiele parametrów doprowadzając do przekazania wielu parametrów naraz co może doprowadzić do wywołania nieobsłużonego błędu, jednakże podczas testów nie udało się znaleźć krytycznego błędu. Może to jednak doprowadzić do nieprawidłowego działania aplikacji. Adwersarz na podstawie wyświetlonych parametrów może je skopiować a następnie umieścić ponownie w innym miejscu tak jak to miało miejsce w przypadku parametru 'choice'. Pełny kod do ponowienia podatności: 
```
http://192.168.64.141/mutillidae/index.php?page=user-poll.php&csrf-token=&choice=nmap&initials=test&choice=netcat&user-poll-php-submit-button=Submit+Vote&
```

Tester:
```
python Tester.py --url "http://<adres IP>/mutillidae/index.php?page=user-poll.php&csrf-token=&choice=nmap&initials=&user-poll-php-submit-button=Submit+Vote" --http-polution --parameter "choice=Paros"
```

SeleniumTester:
```
python SeleniumTester.py --url <ciąg znaków, zawierający adres ip lub nazwę domeny> --http-pollution
```

---

**Mitygacja:**
Należy przekonfigurować aplikację tak, aby akceptowała tylko jedno wystąpienie danego parametru i odrzucała pozostałe, używając bibliotek lub frameworków automatycznie zarządzających parametrami w bezpieczny sposób.
