
## Nazwa podatności: Privilege Escalation

**Istotność:** Wysoka

---

**Opis:**
Privilege Escalation to podatność, która pozwala użytkownikowi uzyskać wyższy poziom uprawnień niż powinien mieć. Może to prowadzić do nieautoryzowanego dostępu do zasobów, danych lub funkcji systemu.

---

**Technika eksploitacji:**
Ekslpoitacja odbywa się poprzez zmianę numeru uid na 1 w żądaniu GET na podstronie http://192.168.255.133/mutillidae/index.php?page=privilege-escalation.php po uprzednim zalogowaniu się na dowolne inne konto.

![1](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/56219452/0c2cf83e-b6b5-42a1-9ab6-5a01938433c7)

![2](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/56219452/0b531ec6-7d9c-4230-8aa8-b2a83e795df2)

SeleniumTester:
```
python SeleniumTester.py --url <ciąg znaków, zawierający adres ip lub nazwę domeny> --priv-esc
```

Mitygacja:
1. Silna walidacja autoryzacji: Upewnij się, że każda akcja i zasób jest zabezpieczony przez ścisłą walidację uprawnień użytkownika. Sprawdzaj uprawnienia użytkownika na serwerze przed wykonaniem każdej operacji.
1. Minimalne uprawnienia: Stosuj zasadę minimalnych uprawnień (Principle of Least Privilege). Każdemu użytkownikowi przypisz tylko te uprawnienia, które są niezbędne do wykonania jego obowiązków.
1. Zabezpieczone tokeny sesji: Upewnij się, że tokeny sesji są bezpieczne i trudne do odgadnięcia. Tokeny powinny być przypisane do określonego użytkownika i jego sesji.
1. Walidacja danych wejściowych: Waliduj wszystkie dane wejściowe, w tym parametry przekazywane w żądaniach GET, POST i innych. Upewnij się, że nie można zmieniać krytycznych parametrów, takich jak UID, bez odpowiednich uprawnień.
1. Rozdzielenie uprawnień: Rozdziel uprawnienia na różne role i upewnij się, że jedna rola nie może uzyskać pełnych uprawnień nad systemem bez odpowiedniego procesu autoryzacji.
1. Monitorowanie i audytowanie: Regularnie monitoruj i audytuj logi aktywności użytkowników pod kątem nieautoryzowanych prób eskalacji uprawnień. Wdróż mechanizmy wykrywania nieprawidłowych działań.
1. Bezpieczne API: Upewnij się, że wszystkie interfejsy API są odpowiednio zabezpieczone i wymagają autoryzacji przed wykonaniem działań, które mogą zmienić poziom uprawnień użytkownika.
1. Aktualizacje i łaty: Regularnie aktualizuj oprogramowanie i stosuj poprawki bezpieczeństwa, aby zapobiec znanym podatnościom, które mogą być wykorzystane do eskalacji uprawnień.
