## Nazwa podatności: XSS Persistent (Second Order)

**Istotność:** Wysoka

---

**Opis:**
Podatność XSS Persistent (Second Order) jest szczególnym rodzajem ataku XSS, który występuje, gdy aplikacja internetowa przechowuje dane użytkownika zawierające skrypty XSS w bazie danych lub innym miejscu pamięci, a następnie wyświetla te dane na stronie internetowej lub innych stronach aplikacji. Atakujący może wprowadzić złośliwy skrypt poprzez interakcję z aplikacją, na przykład poprzez formularz, co prowadzi do zapisania tego skryptu w bazie danych. Gdy dane te są później wyświetlane dla innych użytkowników, atakujący może wykorzystać te skrypty do przechwycenia sesji użytkowników, kierowania ich na złośliwe strony internetowe, kradzieży ciasteczek sesji lub wykonywania innych złośliwych działań w kontekście ich sesji.

---

**Technika eksploitacji:**
Strona która zawiera podatność wygląda następująco;
![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/28838004/86bf509f-d4d8-4cad-af76-9e88f095fd9f)

Polega ona na podaniu treści bloga i umowzliwia jego zapostowanie (post zapisywany jest w bazie danych, a następnie po odwiedzeniu strony zawięrającej blog jest odtwarzany i wyświetlany przez przeglądarkę).

Poniższy zrzut ekranu przedstawia przykład użytkowy --- dodano nowy post:
![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/28838004/9fddc56b-9169-4ee8-9f04-61ba39960db5)

Jeśli natomiast treścią postu będzie kod JavaScript, zostanie on wykonany. Przykłądowo utworzono post o treści: `<script>alert(1);</script>`:
![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/28838004/e7bc909c-6fd3-41b0-9799-a969b6ed688e)

Zapisanie blogu i otworzenie strony z jego zawartością powoduje wywołanie się kodu JavaScript:
![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/28838004/39fb0aeb-0fe8-4064-b394-3449a54eca6a)

SeleniumTester:
```
python SeleniumTester.py --url <ciąg znaków, zawierający adres ip lub nazwę domeny> --xss-persistent
```

---

**Mitygacja podatności:**
Ważne jest, aby wdrożyć odpowiednie środki bezpieczeństwa w celu zapobieżenia atakom XSS Persistent (Second Order). Należy prawidłowo walidować i oczyszczać dane wejściowe przed zapisaniem ich w bazie danych, zastosować mechanizmy ucieczki (escaping) danych przed ich wyświetleniem na stronie internetowej, aby zapobiec interpretacji danych jako kodu HTML lub JavaScript, ograniczyć dostęp do danych przechowywanych w bazie danych i unikać przechowywania potencjalnie złośliwych skryptów. Ponadto, regularne przeprowadzanie audytów bezpieczeństwa, w tym testów penetracyjnych, jest kluczowe w celu wykrycia potencjalnych podatności XSS Persistent (Second Order) oraz szybkiego ich naprawienia.

**Mitygacja w kodzie:**
Ogólny kod dodający zawartość bloga wygląda następująco:
![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/28838004/867b9dc1-fbdf-44f8-a824-c12cfcd389d7)

Natomiast kod wewnątrz zaprezentowanej funkcji wygląda następująco:
![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/28838004/8a0c1403-2371-43e1-ae58-bb717cd706d0)

Pomijając oczywisty problem SQL Injection, widać tutaj, iż po drodze znaki specjalne nie były w żaden sposób escapeowane.

To samo tyczy się funkcji, która potem jest odpowiedzialna za pobranie zawartości z bloga:
![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/28838004/fa651161-ce77-4887-9662-b72a04f2ae90)

W kodzie odpowiedzialnym za pobranie i wyświetlenie zawartości blogu na żadnym z kolejnych etapów nie następuje encoding symboli html:
![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/28838004/65bc65d3-a379-4402-a296-64edc2a91d1d)
![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/28838004/0be4377b-4050-4d4c-8fda-5fd16185b655)

Aby zmitygować problem, należałoby użyć funkcji takiej jak `htmlspecialchars`, jak pokazano poniżej:
```php
$lBloggerName = htmlspecialchars($lRecord->blogger_name, ENT_QUOTES, 'UTF-8');
$lDate = htmlspecialchars($lRecord->date, ENT_QUOTES, 'UTF-8');
$lComment = htmlspecialchars($lRecord->comment, ENT_QUOTES, 'UTF-8');
```



