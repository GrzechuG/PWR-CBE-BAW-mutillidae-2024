
## Nazwa podatności: SQLi - Bypass Authentication

**Istotność:** Wysoka

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

**Mitygacja:**
Aby skutecznie zabezpieczyć się przed podatnością SQL Injection i uniknąć omijania uwierzytelniania, istotne jest wdrożenie odpowiednich środków bezpieczeństwa. Przede wszystkim, aplikacja powinna wykorzystywać przygotowane zapytania (prepared statements) lub procedury przechowywane (stored procedures) do wykonywania operacji na bazie danych. Te techniki automatycznie escapują dane wejściowe, eliminując ryzyko wstrzyknięcia złośliwego kodu SQL.

Dodatkowo, konieczne jest dokładne walidowanie i filtracja danych wejściowych, które są używane do tworzenia zapytań SQL. Aplikacja powinna akceptować tylko dane oczekiwane w określonym formacie i odrzucać wszelkie nieprawidłowe lub podejrzane wartości. Szczególną uwagę należy zwrócić na dane pochodzące z formularzy logowania i innych miejsc, gdzie użytkownik może wprowadzać dane uwierzytelniające.

Ponadto, stosowanie mechanizmów kontroli dostępu, takich jak autoryzacja wielopoziomowa (multi-factor authentication) lub zastosowanie silnych haseł i ich szyfrowanie, może dodatkowo zabezpieczyć system przed próbami omijania uwierzytelniania.

Regularne przeglądy kodu aplikacji, testy penetracyjne oraz audyty bezpieczeństwa są kluczowe dla identyfikacji i naprawy potencjalnych luk w zabezpieczeniach. W przypadku wykrycia podatności SQL Injection, należy jak najszybciej wprowadzić odpowiednie poprawki i zaktualizować aplikację.

Wdrażanie tych praktyk i środków bezpieczeństwa pozwoli zredukować ryzyko wystąpienia podatności SQL Injection oraz skutecznie chronić system przed próbami omijania uwierzytelniania i innymi atakami.
