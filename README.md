# PWR-CBE-BAW-mutillidae

Projekt realizowany na przedmiot "Bezpieczeństwo aplikacji webowych", termin: Piątek 13:15 — 15:00.
Realizowany przez:
- Patryk Duniak 
- Grzegorz Gajewski
- Tomasz Słowik

## Wprowadzenie

Celem projektu było znalezienie oraz eksploitacja jak największej liczby podatności w aplikacji Mutillidae. Dla każdej podatności przygotowano jej opis, technikę eksploitacji i sposoby mitygacji. Dodatkowo, tam gdzie to możliwe, stworzono skrypty automatyzujące wykorzystanie podatności. W tym celu utworzono 2 skrypty: **Tester** oraz **SeleniumTester**, które w różny sposób podchodzą do zadania automatyzacji.

Testowana aplikacja została pobrana ze strony [https://sourceforge.net/projects/owaspbwa/files/1.2/](https://sourceforge.net/projects/owaspbwa/files/1.2/) i zaimportowana do wybranego oprogramowania wirtualizacyjnego, obsługującego pliki _.ova_.

## Wykorzystane oprogramowania i skrypty

Spis wszystkich wykorzystywanych narzędzi wraz z linkami oraz opisem

Stworzono skrypty, napisane w pythonie, do automatyzacji wykorzystywania podatności:
- SeleniumTester
- Tester

**SeleniumTester** to skrypt wykorzystujący biblioteki: argparse, os, re, json, time, selenium, seleniumwire.
Struktura **SeleniumTester** opiera się na:
- **SeleniumTester.py** - jest to plik, parsujący dane podane na wejściu i wykonujący funkcje odpowiedzialne za automatyzację podatności. Dodatkową funkcjonalnością jest funkcja _extract_ip_, która pobiera ip, ip z numerem portu lub nazwę domeny albo pobiera ip z pliku konfiguracyjnego _config.json_ i podaje tę wartość do wykonywanych funkcji automatyzujących.
- **SeleniumDrivers.py** - jest to plik, zawierający klasy _FirefoxBrowser_ oraz _FirefoxBrowserSeleniumWire_, które umożliwiają wykorzystanie selenium oraz selenium-wire.
- Pliki **MutillidaeAxxx.py** - są to pliki, zawierające funkcje, automatyzujące wykorzystanie podatności z odpowiednich zakładek w aplikacji _Mutillidae_.

Struktura większości funkcji automatyzujących nie różni się od siebie i wygląda w sposób następujący:
- Podawane wartości na wejściu:
  - _ip_ - adres ip, adres ip z numerem portu lub nazwa domeny
  - _sleep\_time_ - czas, na który metoda usypia wykonanie eksploitacji, zaraz po jej wykorzystaniu, w celu obserwacji efektów działania przez użytkownika.
  - _payload_ - wykorzystany payload. Wykorzystanie autorskiego payloadu oznacza brak sprawdzenia przez funkcję, czy atak się udał. Należy wtedy wykorzystać argument _sleep\_time_ i obserwować efekty eksploitacji.
  - _verify\_default\_payload_ - flaga wykorzystywana w przypadku użycia autorskiego payloadu.
- Uruchomienie przeglądarki
- Wypisanie payloadu w cmd
- Załadowanie strony
- Uruchomienie payloadu
- Uśpienie działania - domyślnie 0 sekund
- Wypisanie wyniku działania payloadu w cmd (nie wszystkie funkcje/podatności na to pozwalają)
- Zweryfikowanie udanego ataku (w przypadku wykorzystania domyślnego payloadu)
- Wypisanie w cmd informacji o statusie ataku - sukces, porażka, wypisanie błędów podczas uruchomienia

Sposób wykorzystania skryptu **SeleniumTester.py** wygląda podobnie dla każdej podatności. Tam, gdzie to możliwe, w plikach markdown znajdują się komendy potrzebne do uruchomienia eksploitacji danej podatności. Ogólna komenda wygląda tak, jak poniżej:

```
python SeleniumTester.py --url <ciąg znaków, zawierający adres ip lub nazwę domeny> --sleep <czas uśpienia w sekundach> --payload <autorski payload> <flaga odpowiedzialna za atak>
```

Za pomocą komendy ```python SeleniumTester.py --help``` można wyszukać flagę do wykorzystania wybranego typu ataku.

## Opis znalezionych podatności

Opis teoretyczny podatności per kategoria jak Injection (SQL)

### Spis wszystkich znalezionych podatności

### Injection (SQL) (A1)

| Numer | Nazwa Podatności | Istotność | Link |
|-------|------------------|-----------|------|
| 1 | BLIND SQL via TIMING | <span style="color:red">Wysoka</span> | [Opis podatności](OWASP%202013/A1%20-%20Injection%20(SQL)/BLIND%20SQL%20via%20Timing.md) |
| 2 | SQLMAP Practice | <span style="color:red">Wysoka</span> | [Opis podatności](OWASP%202013/A1%20-%20Injection%20(SQL)/SQLMAP%20Practice.md) |
| 3 | SQLi - Bypass Authentication | <span style="color:red">Wysoka</span> | [Opis podatności](OWASP%202013/A1%20-%20Injection%20(SQL)/SQLi%20-%20Bypass%20Authentication.md) |
| 4 | SQL Injection - Extract Data | <span style="color:red">Wysoka</span> | [Opis podatności](OWASP%202013/A1%20-%20Injection%20(SQL)/SQLi%20-%20Extract%20Data.md) |
| 5 | SQL Injection - Insert Injection | <span style="color:red">Wysoka</span> | [Opis podatności](OWASP%202013/A1%20-%20Injection%20(SQL)/SQLi%20-%20Insert%20Injection.md) |
| 6 | JSON Injection - Reflective XSS Attack | <span style="color:red">Wysoka</span> | [Opis podatności](OWASP%202013/A1%20-%20Injection%20(SQL)/XSS%20JSON%20injection%20-%20Pen%20Test%20Tool%20Lookup.md) |

### Injection (Other) (A1)

| Numer | Nazwa Podatności | Istotność | Link |
|-------|------------------|-----------|------|
| 1 | RCE przez aplikacje 'DNS Lookup' | <span style="color:red">Wysoka</span> | [Opis podatności](OWASP%202013/A1%20-%20Injection%20(Other)/Command%20Injection.md) |
| 2 | XML External Entity Injection | <span style="color:red">Wysoka</span> | [Opis podatności](OWASP%202013/A1%20-%20Injection%20(Other)/XML%20External%20Entity%20Injection.md) |
| 3 | XSS: HTMLi via HTTP Header | <span style="color:red">Wysoka</span> | [Opis podatności](OWASP%202013/A1%20-%20Injection%20(Other)/XSS%20HTMLi%20via%20HTTP%20Header.md) |
| 4 | JavaScript Injection | <span style="color:orange">Średnia</span> | [Opis podatności](OWASP%202013/A1%20-%20Injection%20(Other)/JavaScript%20Injection.md) |
| 5 | HTML/CSS Injection | <span style="color:orange">Średnia</span> | [Opis podatności](OWASP%202013/A1%20-%20Injection%20(Other)/Cascading%20Style%20Injection.md) |
| 6 | Frame Source Injection | <span style="color:orange">Średnia</span> | [Opis podatności](OWASP%202013/A1%20-%20Injection%20(Other)/Frame%20Source%20Injection.md) |
| 7 | HTML Injection (HTMLi) | <span style="color:orange">Średnia</span> | [Opis podatności](OWASP%202013/A1%20-%20Injection%20(Other)/HTML%20Injection%20(HTMLi).md) |
| 8 | HTML Injection przez pliki Cookie | <span style="color:orange">Średnia</span> | [Opis podatności](OWASP%202013/A1%20-%20Injection%20(Other)/HTMLi%20Via%20Cookie%20Injection.md) |
| 9 | HTMLi Via DOM Injection | <span style="color:orange">Średnia</span> | [Opis podatności](OWASP%202013/A1%20-%20Injection%20(Other)/HTMLi%20Via%20DOM%20Injection.md) |
| 10 | Buffer Overflow | <span style="color:green">Niska</span> | [Opis podatności](OWASP%202013/A1%20-%20Injection%20(Other)/Buffer%20Overflow.md) |
| 11 | HTTP Parameter Pollution | <span style="color:green">Niska</span> | [Opis podatności](OWASP%202013/A1%20-%20Injection%20(Other)/HTTP%20Parameter%20Pollution.md) |

### Broken Authentication and Session Management (A2)

| Numer | Nazwa Podatności | Istotność | Link |
|-------|------------------|-----------|------|
| 1 | Privilege Escalation - via Cookies | <span style="color:red">Wysoka</span> | [Opis podatności](OWASP%202013/A2%20-%20Broken%20Authentication%20and%20Session%20Management/Privilege%20Escalation%20Via%20Cookies.md) |
| 2 | Authentication Bypass (Bruteforce) | <span style="color:orange">Niska/Średnia</span> | [Opis podatności](OWASP%202013/A2%20-%20Broken%20Authentication%20and%20Session%20Management/Authentication%20Bypass.md) |


### Cross Site Scripting (XSS) (A3)

| Numer | Nazwa Podatności | Istotność | Link |
|-------|------------------|-----------|------|
| 1 | XSS Persistent (Second Order) | <span style="color:red">Wysoka</span> | [Opis podatności](OWASP%202013/A3%20-%20Cross%20Site%20Scripting%20(XSS)/Persistent%20(Second%20Order).md) |
| 2 | XSS Reflected - Capture Data Page | <span style="color:red">Wysoka</span> | [Opis podatności](OWASP%202013/A3%20-%20Cross%20Site%20Scripting%20(XSS)/Reflected%20(First%20Order)%20-%20Capture%20Data%20Page.md) |
| 3 | XSS Reflected - Set Background Colour Page | <span style="color:red">Wysoka</span> | [Opis podatności](OWASP%202013/A3%20-%20Cross%20Site%20Scripting%20(XSS)/Reflected%20(First%20order)%20-%20Set%20Background%20colour.md) |
| 4 | XSS Reflected - Via Cookie Injection | <span style="color:red">Wysoka</span> | [Opis podatności](OWASP%202013/A3%20-%20Cross%20Site%20Scripting%20(XSS)/XSS%20Via%20Cookie%20Injection%20-%20Capture%20Data.md) |
| 5 | XSS Reflected - via HTML attribute | <span style="color:red">Wysoka</span> | [Opis podatności](OWASP%202013/A3%20-%20Cross%20Site%20Scripting%20(XSS)/XSS%20Via%20HTML%20Attribute.md) |
| 6 | XSS Reflected - via HTTP headers | <span style="color:red">Wysoka</span> | [Opis podatności](OWASP%202013/A3%20-%20Cross%20Site%20Scripting%20(XSS)/XSS%20Via%20HTTP%20Headers.md) |
| 7 | XSS Reflected - DNS Lookup Page | <span style="color:orange">Średnia</span> | [Opis podatności](OWASP%202013/A3%20-%20Cross%20Site%20Scripting%20(XSS)/Reflected%20(First%20Order).md) |
| 8 | XSS Against JSON | <span style="color:green">Niska</span> | [Opis podatności](OWASP%202013/A3%20-%20Cross%20Site%20Scripting%20(XSS)/Against%20JSON.md) |

### Insecure Direct Object References (A4)

| Numer | Nazwa Podatności | Istotność | Link |
|-------|------------------|-----------|------|
| 1 | IDOR - Insecure Direct Object Reference | <span style="color:red">Wysoka</span> | [Opis podatności](OWASP%202013/A4%20-%20Insecure%20Direct%20Object%20References/IDOR%20-%20Text%20File%20Viewer.md) |

### Security Misconfiguration (A5)

| Numer | Nazwa Podatności | Istotność | Link |
|-------|------------------|-----------|------|
| 1 | Zdalne wykonanie kodu przez wysłanie pliku | <span style="color:red">Wysoka</span> | [Opis podatności](OWASP%202013/A5%20-%20Security%20Misconfiguration/Unrestricted%20File%20Upload.md) |
| 2 | Directory browsing | <span style="color:orange">Średnia</span> | [Opis podatności](OWASP%202013/A5%20-%20Security%20Misconfiguration/Directory%20Browsing.md) |

### Missing Function Level Access Control (A7)

| Numer | Nazwa Podatności | Istotność | Link |
|-------|------------------|-----------|------|
| 1 | Dostęp do wrażliwych stron oraz plików przez parametr 'page' | <span style="color:red">Wysoka</span> | [Opis podatności](OWASP%202013/A7%20-%20Missing%20Function%20Level%20Access%20Control/Secret%20Administrative%20Pages.md) |

## Podsumowanie

