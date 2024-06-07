## Nazwa podatności: IDOR - Insecure Direct Object Reference

**Istotność:** 9

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

**Mitygacja:**
1. Walidacja Autoryzacji: Upewnij się, że każda żądana operacja na zasobie jest sprawdzana pod kątem odpowiednich uprawnień użytkownika. Wdroż mechanizmy autoryzacji na poziomie zasobów.
2. Ukrywanie Identyfikatorów: Zamiast używać przewidywalnych identyfikatorów (np. numerów ID), stosuj losowe identyfikatory lub tokeny, które są trudniejsze do odgadnięcia przez atakującego.
3. Kontrola Dostępu na Poziomie Serwera: Implementuj kontrolę dostępu bezpośrednio na poziomie serwera, aby zapobiec nieautoryzowanemu dostępowi do plików i zasobów. Upewnij się, że serwer sprawdza, czy użytkownik ma uprawnienia dostępu do danego zasobu.
4. Skanowanie Podatności: Regularnie skanuj aplikację pod kątem podatności IDOR, używając narzędzi do testów bezpieczeństwa aplikacji, aby wykryć i naprawić potencjalne luki.
5. Ograniczanie Ekspozycji Plików Systemowych: Zadbaj o to, aby aplikacja webowa nie miała bezpośredniego dostępu do plików systemowych takich jak /etc/passwd. Używaj mechanizmów chroot lub konteneryzacji, aby ograniczyć dostęp do systemu plików.
6. Bezpieczne Konfiguracje Serwera: Upewnij się, że serwer jest odpowiednio skonfigurowany, aby uniemożliwić dostęp do wrażliwych plików systemowych poprzez HTTP/HTTPS.
