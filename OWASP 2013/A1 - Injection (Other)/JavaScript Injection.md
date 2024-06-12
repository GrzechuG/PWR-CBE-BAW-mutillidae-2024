## Nazwa podatności: JavaScript Injection

**Istotność:** Wysoka

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

SeleniumTester:
```
python SeleniumTester.py --url <ciąg znaków, zawierający adres ip lub nazwę domeny> --javascript
```

 **Mitygacja:**
Aby skutecznie zmitygować podatność JavaScript Injection, konieczne jest wdrożenie kilku kluczowych praktyk programistycznych i zabezpieczeń. Przede wszystkim, wszystkie dane wejściowe użytkowników muszą być rygorystycznie walidowane i filtrowane. Oznacza to akceptowanie tylko tych danych, które są niezbędne i zgodne z oczekiwanym formatem. Należy unikać bezpośredniego używania niezaufanych danych wejściowych w kontekście JavaScript, takich jak wstawianie danych użytkownika bezpośrednio do skryptów JavaScript w HTML.

Zamiast tego, dane wejściowe powinny być odpowiednio kodowane przed ich wstawieniem w jakikolwiek kontekst HTML lub JavaScript. W przypadku dynamicznego generowania skryptów JavaScript, zaleca się używanie funkcji kodujących, które zapobiegają interpretacji wstrzykniętego kodu jako prawidłowego JavaScriptu. Dodatkowo, korzystanie z bibliotek i frameworków, które automatycznie zajmują się kodowaniem i filtrowaniem danych wejściowych, może znacząco zmniejszyć ryzyko wystąpienia tej podatności.

Regularne aktualizowanie oprogramowania oraz korzystanie z narzędzi do analizy i testowania bezpieczeństwa, takich jak skanery podatności, jest również kluczowe. Przeprowadzanie regularnych audytów bezpieczeństwa oraz testów penetracyjnych pomaga w identyfikacji i naprawie potencjalnych luk w zabezpieczeniach.

Stosowanie polityki Content Security Policy (CSP) może dodatkowo zabezpieczyć aplikację, ograniczając możliwość wykonywania nieautoryzowanego kodu JavaScript. CSP pozwala definiować, jakie źródła skryptów są dozwolone, co może zapobiec wykonaniu złośliwego kodu wstrzykniętego przez atakującego.

Implementacja tych praktyk i mechanizmów zabezpieczeń pozwala znacząco zredukować ryzyko wystąpienia podatności JavaScript Injection, chroniąc aplikację oraz jej użytkowników przed potencjalnymi atakami i kompromitacją danych.
