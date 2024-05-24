
## Nazwa podatności: SQLi - Bypass Authentication

**Istotność:** 10

---

**Opis:**
SQL Injection (SQLi) to rodzaj podatności, która pozwala atakującemu wstrzyknąć złośliwy kod SQL do zapytań, które są przetwarzane przez aplikację internetową. W przypadku tej konkretnej podatności, formularz logowania akceptuje dane użytkownika i hasło, które są następnie wykorzystywane do tworzenia zapytań SQL w celu weryfikacji tożsamości użytkownika. Jednak aplikacja nie odpowiednio waliduje lub zabezpiecza te dane, co prowadzi do możliwości manipulacji zapytaniami SQL i tym samym spowodowania, iż bez podania hasła dla użytkownika nastąpi pomyślne uwierzytelnienie.



---

**Technika eksploitacji:**
Atakujący może wykorzystać podatność SQL Injection, wprowadzając w pola formularza specjalnie spreparowane dane, które zawierają złośliwy kod SQL. W przypadku tej konkretnej podatności, atakujący wprowadza w polu hasła wartość `' or 'a'='a`, co zmienia generowane zapytanie SQL w taki sposób, że zawsze zwraca ono prawdę (true).


Kroki konieczne do eksploatacji tej podatności obejmują:

1. Zidentyfikowanie formularza lub elementu aplikacji internetowej, który komunikuje się z bazą danych i gdzie można wprowadzić dane logowania.
2. Wprowadzenie spreparowanych danych, zawierających złośliwy kod SQL, w tym przypadku `' or 'a'='a`, w pola formularza.
   ![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/28838004/f134d794-bf05-46ef-92b1-671885912e6b)

4. Wysłanie danych do serwera, który następnie generuje zapytanie SQL, które zostaje zmodyfikowane przez złośliwe dane.
5. Otrzymanie dostępu do systemu, omijając proces uwierzytelniania.

Atakujący może wykorzystać narzędzia automatyzujące proces wstrzykiwania SQL, takie jak SQLMap, lub ręcznie manipulować danymi wysyłanymi do serwera poprzez narzędzia do przeglądania sieci, takie jak Burp Suite. Opanowanie podatności SQL Injection może umożliwić atakującemu zdobycie dostępu do systemu, kradzież danych, uszkodzenie bazy danych lub nawet przejęcie kontroli nad serwerem.
