## Nazwa podatności: Cross-Site Scripting (XSS)

**Istotność:** 8

---

**Opis:**
Cross-Site Scripting (XSS) to typ podatności, który pozwala atakującemu wstrzyknąć złośliwy kod JavaScript do stron, które są następnie wyświetlane innym użytkownikom. Skrypt jest wykonany przez przeglądarkę użytkownika jako część strony HTML. Ataki XSS są szczególnie niebezpieczne, ponieważ pozwalają na wykonywanie skryptów w kontekście domeny ofiary, co może prowadzić do kradzieży danych sesji, manipulacji treścią strony, przekierowania na złośliwe strony, i innych złośliwych działań.

Podstrona z funkcją, która pozwala użytkownikowi na personalizację wyglądu poprzez ustawienie koloru tła (Background color) nie sanitarizuje ani nie koduje wprowadzonych danych, pozwalając na wstrzyknięcie kodu.

---

**Technika eksploatacji:**
Atakujący wprowadza payload JavaScript jako wartość koloru tła, np.:

`"><script>alert(document.cookie);</script>`

Gdy wartość ta jest osadzona bezpośrednio w atrybucie stylu HTML, zamyka ona atrybut i otwiera tag skryptu.

Kiedy strona jest ładowana lub odświeżana, przeglądarka interpretuje i wykonuje złośliwy skrypt. To pozwala na wykonanie działań z uprawnieniami użytkownika, takich jak dostęp do ciasteczek, które mogą zawierać tokeny sesji lub inne dane uwierzytelniające.

![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/56219452/d3a9b93b-dbd5-4a1b-b52a-546beffbdff1)

