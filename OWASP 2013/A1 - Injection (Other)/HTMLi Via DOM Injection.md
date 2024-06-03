## Nazwa podatności: HTMLi Via DOM Injection

**Istotność:** Medium

---

**Opis:**
HTML Injection via DOM (Document Object Model) jest rodzajem podatności, która pozwala atakującemu wstrzyknąć złośliwy kod HTML do dokumentu HTML za pomocą manipulacji DOM. DOM jest reprezentacją dokumentu HTML jako drzewa obiektów, które przeglądarka internetowa interpretuje i wyświetla. Atakujący może wykorzystać tę podatność, aby osadzić złośliwy kod HTML w dokumentach, które następnie mogą być wyświetlane dla użytkowników końcowych.

Konsekwencje HTML Injection via DOM mogą być poważne. Atakujący może osadzić linki do phishingu, fałszywe formularze logowania, złośliwe skrypty JavaScript lub inne złośliwe treści w stronie internetowej. To może prowadzić do kradzieży danych użytkowników, przechwycenia sesji, ataków XSS (Cross-Site Scripting) i innych groźnych scenariuszy.

Aby uniknąć HTML Injection via DOM, należy zawsze dokładnie walidować i filtrować wszelkie dane wejściowe, które mogą być wstrzykiwane do dokumentu HTML. Warto również korzystać z bezpiecznych praktyk programistycznych, takich jak użycie bezpiecznych metod manipulacji DOM, aby ograniczyć ryzyko wystąpienia tej podatności. Regularne audyty bezpieczeństwa mogą również pomóc w wykryciu i naprawie podatności związanych z HTML Injection via DOM.

---

**Technika eksploatacji:**

![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/28838004/94726784-5909-4be7-b26e-36979fcf3f8e)
Analiza zapytania GET pokazuje iż wartość parametru username jest wyświetlana na stronie.

Podatny kod HTML wygląda następująco:

![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/28838004/455d2650-9487-4feb-8845-14fc45559294)

Po zbadaniu poniższego adresu URL:
```http://192.168.198.128/mutillidae/index.php?page=password-generator.php&username=";alert(%27Hacked!%27);a="```

(Payload ```";alert(%27Hacked!%27);a="```) uzyskano poniższy rezultat:

![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/28838004/40e287a3-596f-4d36-b9a7-c1037e10d001)


Alert został wywołany, co pokazuje udany atak HTML/XSS DOM injection.
Kod HTML strony wygląda następująco:
![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/28838004/c4d06bfb-2504-43be-a478-b4d308799dad)



**Mitygacja podatności:**
Aby skutecznie zmitygować podatność HTML DOM Injection, kluczowe jest wdrożenie kilku istotnych praktyk programistycznych i zabezpieczeń. Przede wszystkim, należy rygorystycznie walidować i filtrować wszystkie dane wejściowe, które mogą być wstrzykiwane do dokumentu HTML. Dane wejściowe muszą być zgodne z oczekiwanym formatem i nie mogą zawierać niebezpiecznych elementów HTML lub JavaScript. Unikaj bezpośredniego używania niebezpiecznych metod manipulacji DOM, takich jak `innerHTML`, `outerHTML` czy `document.write`. Zamiast tego, preferuj bezpieczne metody, takie jak `textContent` lub `innerText`, które automatycznie kodują wprowadzone dane, eliminując ryzyko wykonania złośliwego kodu. Regularne audyty bezpieczeństwa są również kluczowe, aby identyfikować i naprawiać potencjalne luki w zabezpieczeniach. Stosowanie technik takich jak Content Security Policy (CSP) może dodatkowo zwiększyć poziom ochrony przed atakami HTML DOM Injection, ograniczając możliwość wykonania nieautoryzowanego kodu na stronie. Implementacja tych praktyk pozwala znacząco zredukować ryzyko wystąpienia podatności i zabezpieczyć aplikację przed potencjalnymi atakami.
