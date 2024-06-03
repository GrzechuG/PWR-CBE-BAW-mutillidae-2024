## Nazwa podatności: XSS Against JSON

**Istotność:** Niska

---

**Opis:**
Podatność XSS Against JSON polega na niepoprawnej obsłudze danych JSON przez aplikację internetową, co umożliwia atakującemu wstrzyknięcie złośliwego kodu JavaScript do przesyłanych danych. Atakujący może manipulować danymi JSON przekazywanymi między serwerem a klientem, dodając do nich złośliwe skrypty. Gdy te dane są następnie przetwarzane po stronie klienta, na przykład przez framework JavaScript, atakujący może wykorzystać tę lukę, aby przeprowadzić ataki XSS.

---

**Technika eksploitacji:**
Podatna storna pozwala na wybranie narzędzia z listy, a następnie wyświetla o nim informacje:
![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/28838004/9876a676-33b0-4948-b4f8-650e6a473f40)

Podatny fragment kodu wygląda następująco:
![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/28838004/97d0ed65-bc4f-42d2-bb71-5659d2cdf5bd)

Możliwe jest zmodyfikowanie parametru toolIDRequested w  dowolny sposób. Jeśli pod odpowiedni parametr poda się paylod postaci:
```javascript
&quot;}}&#39;;alert(1);let temp =&#39;
```
![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/28838004/c1679f82-0ac6-40ad-a947-b3bfd20fb451)
Nastąpi ucieczka formatu JSON, oraz wykonanie kodu javascript.

![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/28838004/06cc1d94-3706-402b-87a4-56a6c527dd6a)

Kod podatnej części wygląda wtedy następująco:
![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/28838004/94bc74f7-7935-4b6e-acdb-dc9e2a25bb35)


---

**Mitygacja podatności:**
Aby zabezpieczyć aplikację przed atakami XSS Against JSON, konieczne jest podjęcie szeregu działań. Przede wszystkim należy zapewnić, że aplikacja poprawnie parsuje i obsługuje dane JSON, unikając niebezpiecznych operacji na tych danych. Należy również stosować bezpieczne metody przekazywania danych JSON między serwerem a klientem, takie jak zaszyfrowane kanały komunikacji, aby zmniejszyć ryzyko manipulacji danych przez atakujących.
Kolejnym ważnym krokiem jest staranna walidacja danych po stronie serwera, aby upewnić się, że przekazywane dane JSON są zgodne z oczekiwanymi formatami i nie zawierają złośliwego kodu. Jeśli dane JSON mają być wyświetlane na stronie internetowej, należy użyć odpowiednich mechanizmów ucieczki (escaping) danych, aby zapobiec interpretacji danych jako kodu JavaScript.
Ostatecznie, regularne przeprowadzanie audytów bezpieczeństwa aplikacji, w tym testów penetracyjnych, jest kluczowe w celu wykrycia potencjalnych luki związanych z obsługą danych JSON i szybkiego ich naprawienia. Dzięki tym środkom można skutecznie zabezpieczyć aplikację przed atakami XSS Against JSON.
