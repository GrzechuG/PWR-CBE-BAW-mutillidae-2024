## Nazwa podatności: Reflected XSS

**Istotność:** 9

---

**Opis:**
Reflected XSS to rodzaj ataku typu Cross-Site Scripting, który ma miejsce, gdy aplikacja internetowa natychmiastowo odbija dane wejściowe dostarczone przez użytkownika bez ich odpowiedniego przetworzenia i wyświetla je na stronie internetowej. Atakujący może wstrzyknąć złośliwy kod JavaScript do formularza lub parametru URL, który następnie zostanie wyświetlony i wykonany w przeglądarce ofiary.
Może to prowadzić do kradzieży ciasteczek sesyjnych, przechwytywania danych użytkowników, a nawet przejęcia konta.

---

**Technika eksploitacji:**
Na stronie http://192.168.255.133/mutillidae/index.php?page=capture-data.php należy do żądania GET wstrzyknąć do ciasteczka ciąg:

```
"><img src='1' onerror='alert(0)' <
```

![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/56219452/4a4c7f2c-e71a-4f3a-8fba-1002f4649235)

Po przesłaniu tak zmodyfikowanego zapytania wywoływane jest powiadomienie z zadaną zawartością.

![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/56219452/d5c4f9ab-e84a-43a2-8c9f-7dce115f1823)

