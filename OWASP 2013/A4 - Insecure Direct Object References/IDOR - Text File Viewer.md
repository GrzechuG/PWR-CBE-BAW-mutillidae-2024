## Nazwa podatności: IDOR - Insecure Direct Object Reference

**Istotność:** Wysoka

---

**Opis:**
Podatność IDOR (Insecure Direct Object Reference) to podatność, która pozwala atakującemu uzyskać dostęp do zasobów bez odpowiedniej autoryzacji, poprzez manipulację identyfikatorami w żądaniach.

---

**Technika eksploitacji:**
Eksploitacja rozpoczyna się od stworzenia payloadu. W tym przypadku jest to ścieżka do pliku passwd:
```
  /etc/passwd
```
Ten fragment kodu jest następnie wklejany w miejsce adresu URL jednego z podglądanych plików.

![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/56219452/b465efa4-6598-4de7-a1b6-1f525b86cb8c)


Po wybraniu i zatwierdzeniu wyświetlany jest plik /etc/passwd

![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/56219452/30716f2c-7a21-44ae-a27b-a6cf98880d49)

SeleniumTester:
```
python SeleniumTester.py --url <ciąg znaków, zawierający adres ip lub nazwę domeny> --idor
```

**Mitygacja:**
Mitygacja podatności powinna obejmować walidację i sanityzację danych wejściowych, aby upewnić się, że wszystkie dane są sprawdzane i filtrowane zgodnie z oczekiwanymi formatami i typami. Stosowanie zasady minimalnych uprawnień pozwoli na dodatkowe zabezpieczenie systemu. Należy zabezpieczyć aplikację webową, aby nie miała dostępu do plików systemowych takich jak /etc/passwd. Serwer powinien sprawdzać, czy użytkownik ma uprawnienia dostępu do danego zasobu.
