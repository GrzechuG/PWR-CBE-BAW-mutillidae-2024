## Nazwa podatności: Directory browsing

**Istotność:** Niska

---

**Opis:**
Możliwa jest enumeracja podstron "http://192.168.64.141/mutillidae/", co może pozwolić na uzyskanie dostępu do podstrony z wrażliwymi danymi lub panelu administracyjnego.
![obraz](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/93217316/4c07c157-76c2-4fda-acc6-49e48b561651)

---

**Technika eksploitacji:**
Możliwa jest enumeracja podstron przy pomocy dowolnego oprogramowania lub skryptu lub przez ręczne umieszczenie tekstu. Do wylistowania podstron został wykorzystany prosty skrypt, którego wynik widać poniżej: 
![obraz](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/93217316/d5220eaf-d634-4940-9eaa-20011c26510f)

Program
```
python SecretAdminitrativePagesEnumeration.py --url "http://<adres IP>/mutillidae/" --list lista_url_directory.txt --klucz "Validation Error: 404 - Page Not Found"
```

---

**Mitygacja:**
Aby zabezpieczyć aplikację przed enumeracją podstron, należy wykorzystać autoryzację, aby ograniczyć dostęp do wrażliwych podstron. Upewnij się, że aplikacja zawsze zwraca tę samą odpowiedź HTTP, niezależnie od tego, czy zasób istnieje czy nie. Unikaj specjalnych odpowiedzi dla nieistniejących zasobów, które mogą ujawnić informacje o strukturze aplikacji.



