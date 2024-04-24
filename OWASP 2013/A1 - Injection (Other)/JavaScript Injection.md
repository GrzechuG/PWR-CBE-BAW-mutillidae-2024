## Nazwa podatności: JavaScript Injection

**Istotność:** 9

---

**Opis:**
JavaScript Injection to rodzaj ataku, który polega na wstrzykiwaniu złośliwego kodu JavaScript na stronie internetowej w celu osiągnięcia nieautoryzowanego dostępu, kradzieży danych lub wykonania innych złośliwych działań. Atakujący wykorzystuje tę podatność, aby umieścić kod JavaScript w miejscach, gdzie normalnie występuje kod JavaScript, np. w polach formularzy, parametrach URL lub nawet w bazie danych.

Konsekwencje JavaScript Injection mogą być poważne, obejmując kradzież sesji, ataki typu XSS (Cross-Site Scripting), przejęcie kontroli nad sesją użytkownika, przechwytywanie poufnych danych, a nawet pełną kompromitację serwera lub aplikacji internetowej.

---

**Technika eksploatacji:**

Generator haseł "password generator" wyświetla na stronie wartość podaną w URL jako parametr username. Poprzez odpowiednie  spreparowanie tej wartości można umieścić kod Javascript na stronie. przykładowo:  
```http://192.168.198.128/mutillidae/index.php?page=password-generator.php&username=";alert(1);a="```

Zmienna `username` musi zaczynać się od zakończenia poprzednio definiowanego stringa `";` oraz kończyć naprawieniem pozostawionej części natywnego kodu Javascript zamykając osamotniony znak `"` na końcu linii.

Wynik działania eksploita:
![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/28838004/73f2436c-1da8-43dd-904d-f39bc7f79113)
 Po wstrzyknięciu kodu Javascript kod strony wygląda on następująco:
 ![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/28838004/7065ea74-c062-448b-8a9b-5c9d7e7a6a77)

