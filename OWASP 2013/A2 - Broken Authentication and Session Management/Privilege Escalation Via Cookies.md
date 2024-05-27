
## Nazwa podatności: Privilege Escalation

**Istotność:** 10

---

**Opis:**
Privilege Escalation to podatność, która pozwala użytkownikowi uzyskać wyższy poziom uprawnień niż powinien mieć. Może to prowadzić do nieautoryzowanego dostępu do zasobów, danych lub funkcji systemu.

---

**Technika eksploitacji:**
Ekslpoitacja odbywa się poprzez zmianę numeru uid na 1 w żądaniu GET na podstronie http://192.168.255.133/mutillidae/index.php?page=privilege-escalation.php po uprzednim zalogowaniu się na dowolne inne konto.

![1](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/56219452/0c2cf83e-b6b5-42a1-9ab6-5a01938433c7)

![2](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/56219452/0b531ec6-7d9c-4230-8aa8-b2a83e795df2)

