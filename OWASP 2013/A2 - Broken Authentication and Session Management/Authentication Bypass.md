
## Nazwa podatności: Authentication Bypass (Bruteforce)

**Istotność:** Niska/Średnia

---

**Opis:**
Podatność Authentication Bypass (Bruteforce) występuje, gdy aplikacja internetowa nie wprowadza odpowiednich mechanizmów zabezpieczeń, które uniemożliwiłyby atakującemu próby złamania uwierzytelnienia poprzez bruteforce. Atakujący może wielokrotnie próbować logować się do systemu, testując różne kombinacje haseł, aż znajdzie prawidłowe. Jest to szczególnie niebezpieczne, gdy aplikacja nie implementuje ograniczeń dotyczących liczby prób logowania, lub gdy hasła są słabe lub łatwo odgadnialne.

---

**Technika eksploitacji:**
W systemie multidae na potrzeby testów ochrony przed atakami bruteforce został utworzony testowy użytkownik o nazwie użytkownika `Dawid` i słabym haśle `dawidszymanski58`.


Następnie utworzony został skrypt umożliwiający atak bruteforce na stronę logowania, która wygląda tak jak zaprezentowano poniżej:
![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/28838004/17b59acf-e8d8-4949-a90c-a2cf3958fda2)

Skrypt przyjmuje 2 argumenty:
- nazwę użytkownika
- wordlistę haseł do przetestowania

Jako wordlistę (liste potencjalnych haseł) wykorzystano popularną listę - rockyou.txt.

Wywołano skrypt z argumentami `Dawid` oraz `rockyou.txt`
![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/28838004/165f013f-27c5-4bf1-845a-176b45c9bda2)
output polecenia:
![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/28838004/8efaf7b3-6389-436c-aea6-25c86a7eb8ac)
...




---

**Mitygacja podatności:**
Aby skutecznie zabezpieczyć aplikację przed atakami Authentication Bypass (Bruteforce), konieczne jest wdrożenie odpowiednich środków bezpieczeństwa. Po pierwsze, zaleca się stosowanie silnych haseł oraz zachęcanie użytkowników do korzystania z długich kombinacji liter, cyfr i znaków specjalnych. Dodatkowo, ważne jest wprowadzenie mechanizmów ograniczających liczbę prób logowania, takich jak blokowanie konta po przekroczeniu określonej liczby nieudanych prób lub wprowadzenie opóźnienia odpowiedzi po kilku kolejnych błędnych próbach.

Monitorowanie aktywności logowania może również być skutecznym środkiem obrony, umożliwiając szybkie wykrycie podejrzanych wzorców, takich jak wielokrotne próby logowania z różnych adresów IP. Wprowadzenie wielopoziomowej weryfikacji tożsamości, na przykład poprzez wysyłanie kodów weryfikacyjnych na telefon użytkownika, dodatkowo zwiększa poziom bezpieczeństwa.

Ostatecznie, regularne aktualizacje aplikacji i narzędzi związanych z uwierzytelnianiem są kluczowe w zapewnieniu ochrony przed znanymi lukami bezpieczeństwa. Poprawna implementacja tych środków pozwala zwiększyć odporność aplikacji na ataki bruteforce i chroni prywatność użytkowników.
