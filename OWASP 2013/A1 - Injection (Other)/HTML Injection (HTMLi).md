## Nazwa podatności: HTML Injection (HTMLi)

**Istotność:** 6

---

**Opis:**
HTML Injection (HTMLi) to podatność występująca w aplikacjach internetowych, która pozwala atakującemu wstrzyknąć złośliwy kod HTML lub JavaScript do strony internetowej. Podatność ta jest wynikiem niewłaściwego lub braku odpowiedniego filtrowania lub kodowania danych wprowadzanych przez użytkownika przed ich wyświetleniem na stronie internetowej. Atakujący może wykorzystać tę lukę, aby osadzić na stronie internetowej niebezpieczny kod, który może prowadzić do różnych skutków, włączając w to kierowanie użytkownika na fałszywe strony logowania, wyświetlanie fałszywych komunikatów, przechwytywanie danych, ataki typu phishing, infekcję malwarem oraz wiele innych.

Podatność HTML Injection jest szczególnie niebezpieczna, ponieważ atakujący może wpłynąć na wygląd i zachowanie strony internetowej oraz wprowadzić w błąd użytkowników, sprawiając, że uwierzą, iż są na oficjalnej stronie, podczas gdy są na stronie kontrolowanej przez atakującego.

Przykłady sytuacji, które mogą prowadzić do podatności HTML Injection, obejmują:

1. Brak walidacji i filtrowania danych wejściowych: Jeśli aplikacja internetowa nie sprawdza i nie filtrowuje danych wprowadzanych przez użytkowników, atakujący może wprowadzić złośliwy kod HTML lub JavaScript.
2. Wyświetlanie danych bez odpowiedniego kodowania: Jeśli aplikacja wyświetla dane wprowadzone przez użytkowników bez odpowiedniego kodowania, atakujący może wstrzyknąć kod HTML, który zostanie wykonany przez przeglądarkę użytkownika.


---

**Technika eksploatacji:**
![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/28838004/94726784-5909-4be7-b26e-36979fcf3f8e)
Analiza zapytania GET pokazuje iż wartość parametru username jest wyświetlana na stronie.
Po zbadaniu poniższego adresu URL:
```http://192.168.198.128/mutillidae/index.php?page=password-generator.php&username=%3Cu%3Etest%20HTMLi%3Cu%3E```

(Payload <u> test </u>) uzyskano poniższy rezultat:

![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/28838004/69f1e7e4-b505-4dbc-9699-aabd0c82ffda)

Tekst został podkreślony co pokazuje podatność HTML injection.

Możliwe jest także umieszczenie zdjęcia oraz dowolnej innej zawartości HTML:

Payload: `http://192.168.198.128/mutillidae/index.php?page=password-generator.php&username=%3Cimg%20src=%27https://upload.wikimedia.org/wikipedia/commons/2/26/You_Have_Been_Hacked%21.jpg%27%3E`

![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/28838004/5af8ef8c-a05d-4ef6-9613-ca0bf3f65aeb)

