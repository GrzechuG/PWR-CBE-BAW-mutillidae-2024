# PWR-CBE-BAW-mutillidae

Projekt realizowany na przedmiot "Bezpieczeństwo aplikacji webowych", termin: Piątek 13:15 — 15:00.
Realizowany przez:
- Patryk Duniak 
- Grzegorz Gajewski
- Tomasz Słowik

## Wprowadzenie

Celem projektu było znalezienie oraz eksploitacja jak największej liczby podatności w aplikacji Mutillidae. Dla każdej podatności przygotowano jej opis, technikę eksploitacji i sposoby mitygacji. Dodatkowo, tam gdzie to możliwe, stworzono skrypty automatyzujące wykorzystanie podatności. W tym celu utworzono 2 skrypty: **Tester** oraz **SeleniumTester**, które w różny sposób podchodzą do zadania automatyzacji.

Testowana aplikacja została pobrana ze strony [https://sourceforge.net/projects/owaspbwa/files/1.2/](https://sourceforge.net/projects/owaspbwa/files/1.2/) i zaimportowana do wybranego oprogramowania wirtualizacyjnego, obsługującego pliki _.ova_.

## Kryteria przyznawania istotności dla podatności

Przyznawanie istotności podatności dla aplikacji webowych jest kluczowym elementem zarządzania bezpieczeństwem. Podczas testowania aplikacji Mutilldae zdecydowano się na przyznywanie istotności w 3 skalach, które zostały opisane poniżej:
- Wysoki - Podatności te mają wysoki wpływ na bezpieczeństwo aplikacji i mogą prowadzić do poważnych naruszeń danych, eskalacji uprawnień lub innych krytycznych incydentów. Podczas przeprowadzania testów, wpływ znalezionych podatności na system był zazwyczaj znaczący. Dodatokowo te podatności mogą prowadzić do kompromitacji systemu lub jego awarii.
- Niski - Podatności nie wpływają na ciągłość działania aplikacji, ale mogą wywołać nieprawidłowe działanie lub prowadzić do obciążenia systemu. Podatności te nie pozwalają na kompromitację systemu lub na utrate bezpieczeństwa danych

## Wykorzystane oprogramowania i skrypty

[comment]: <> (Spis wszystkich wykorzystywanych narzędzi wraz z linkami oraz opisem)

Stworzono skrypty, napisane w pythonie, do automatyzacji wykorzystywania podatności:
- SeleniumTester
- Tester
- SecretAdminitrativePagesEnumeration

### Selenium Tester

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

Wykorzystanie pliku konfiguracyjnego i domyślnych ustawień (payload i czas uśpienia) pozwala na skrócenie komendy do:
```
python SeleniumTester.py <flaga odpowiedzialna za atak>
```

Za pomocą komendy ```python SeleniumTester.py --help``` można wyszukać flagę do wykorzystania wybranego typu ataku.

### Tester

**Tester** to skrypt zapewniający częsciową automatyzacje, pozwalający na uniwersalne weryfikowanie podatności na różnych stronach. Oprogramowania pozwala przez parametr '--autoforms' wypełniać formularze i umieszczać złośliwy kod w odpowiednie miejsca.
Program jest oparty bibliotece request, co nie pozwoliło na weryfikacje podatności typu XSS, jednakże zapewniło uniwersalność oraz zgodność z podstawowymi bibliotekami Python.
Program posiada następujące parametry do wykonania:
- --url <adres_url> (Adres URL strony (wraz z parametrem jeżeli http_polution)
- --http_pollution (Wykonanie ataku http pollution)
- --parameter "parametr1=wartosc1" "parametr2=wartosc2" ... (Parametry do ataku http_pollution)
- --sqli <Normal/Insert/Timing> (Wykonanie ataku sqli injection przez POST. Aktualne jest wspierane zwykłe sqli injection, przez wykonanie insert, oraz używania funkcji czasowej)
- --comminj <AND/DoubleAND/OR> (Wykonanie ataku command injection przez POST. Aktualne są wspierane różne łączniki poleceń jak AND(&), DoubleAND(&&), oraz OR(||))
- --xmleei (Wykonanie ataku XML External Enityty Injection)
- --htmli <Onsite/Header/Cookie> (Wykonanie ataku HTML injection. Aktualne są wspierane zwykły atak na strone przez POST, wysłanie ataku przez header nagłówka HTTP, oraz same Ciastko)
- --autoforms (Funkcjonalność automatycznego wypełniania formularzy)
- --postdata "nazwa1: wartosc1" "nazwa2: wartosc2" ... (Funkcjonalność ręcznego wypełniania formularzy)

### SecretAdminitrativePagesEnumeration

***SecretAdminitrativePagesEnumeration*** to prosty skrypt pozwalający na wyszukiwanie wszystkich stron gdzie nie występuje wprowadzony string. Pozwala to znaleźć strony z unikalną zawortością, a wszystkie pozostałe strony do który aplikacja nie ma dostępu lub nie istnieją odpowiednio pominąć, nawet jeżeli aplikacja przekierowuje zapytanie na oryginalną stronę.
Program posiada następujące parametry do wykonania:
- --url <adres_url> (Adres URL strony, jeżeli chce się iterować podstrony to należy zakończyć url znakiem '/', a po parametrze należy podać 'parametr='
- --list <nazwa_listy> (Nazwa pliku zawierającego liste (musi znajdować się na tym samym poziomie w systemie co plik wykonywalny))
- --klucz <string_ze_słowem_kluczowym> (Słowo kluczowe np. '404 Not Found')

## Opis znalezionych podatności

SQL Injection - 

HTML Injection - 

XML External Entity Injection

RCE - 

Frame Source Injection - 

HTTP pollution - 

XSS -

Insecure Direct Object References -

Directory Browsing -

### Spis wszystkich znalezionych podatności

### Injection (SQL) (A1)

| Numer | Nazwa Podatności | Istotność | Link |
|-------|------------------|-----------|------|
| 1 | BLIND SQL via TIMING | Wysoka | [Opis podatności](OWASP%202013/A1%20-%20Injection%20(SQL)/BLIND%20SQL%20via%20Timing.md) |
| 2 | SQLMAP Practice | Wysoka | [Opis podatności](OWASP%202013/A1%20-%20Injection%20(SQL)/SQLMAP%20Practice.md) |
| 3 | SQLi - Bypass Authentication | Wysoka | [Opis podatności](OWASP%202013/A1%20-%20Injection%20(SQL)/SQLi%20-%20Bypass%20Authentication.md) |
| 4 | SQL Injection - Extract Data | Wysoka | [Opis podatności](OWASP%202013/A1%20-%20Injection%20(SQL)/SQLi%20-%20Extract%20Data.md) |
| 5 | SQL Injection - Insert Injection | Wysoka | [Opis podatności](OWASP%202013/A1%20-%20Injection%20(SQL)/SQLi%20-%20Insert%20Injection.md) |
| 6 | JSON Injection - Reflective XSS Attack | Wysoka | [Opis podatności](OWASP%202013/A1%20-%20Injection%20(SQL)/XSS%20JSON%20injection%20-%20Pen%20Test%20Tool%20Lookup.md) |

### Injection (Other) (A1)

| Numer | Nazwa Podatności | Istotność | Link |
|-------|------------------|-----------|------|
| 1 | RCE przez aplikacje 'DNS Lookup' | Wysoka | [Opis podatności](OWASP%202013/A1%20-%20Injection%20(Other)/Command%20Injection.md) |
| 2 | XML External Entity Injection | Wysoka | [Opis podatności](OWASP%202013/A1%20-%20Injection%20(Other)/XML%20External%20Entity%20Injection.md) |
| 3 | XSS: HTMLi via HTTP Header | Wysoka| [Opis podatności](OWASP%202013/A1%20-%20Injection%20(Other)/XSS%20HTMLi%20via%20HTTP%20Header.md) |
| 4 | JavaScript Injection | Wysoka | [Opis podatności](OWASP%202013/A1%20-%20Injection%20(Other)/JavaScript%20Injection.md) |
| 5 | HTMLi Via DOM Injection | Wysoka | [Opis podatności](OWASP%202013/A1%20-%20Injection%20(Other)/HTMLi%20Via%20DOM%20Injection.md) |
| 6 | HTML/CSS Injection | Niska | [Opis podatności](OWASP%202013/A1%20-%20Injection%20(Other)/Cascading%20Style%20Injection.md) |
| 7 | Frame Source Injection | Niska | [Opis podatności](OWASP%202013/A1%20-%20Injection%20(Other)/Frame%20Source%20Injection.md) |
| 8 | HTML Injection (HTMLi) | Niska | [Opis podatności](OWASP%202013/A1%20-%20Injection%20(Other)/HTML%20Injection%20(HTMLi).md) |
| 9 | HTML Injection przez pliki Cookie | Niska | [Opis podatności](OWASP%202013/A1%20-%20Injection%20(Other)/HTMLi%20Via%20Cookie%20Injection.md) |
| 10 | Buffer Overflow | Niska | [Opis podatności](OWASP%202013/A1%20-%20Injection%20(Other)/Buffer%20Overflow.md) |
| 11 | HTTP Parameter Pollution | Niska | [Opis podatności](OWASP%202013/A1%20-%20Injection%20(Other)/HTTP%20Parameter%20Pollution.md) |

### Broken Authentication and Session Management (A2)

| Numer | Nazwa Podatności | Istotność | Link |
|-------|------------------|-----------|------|
| 1 | Privilege Escalation - via Cookies | Wysoka | [Opis podatności](OWASP%202013/A2%20-%20Broken%20Authentication%20and%20Session%20Management/Privilege%20Escalation%20Via%20Cookies.md) |
| 2 | Authentication Bypass (Bruteforce) | Niska | [Opis podatności](OWASP%202013/A2%20-%20Broken%20Authentication%20and%20Session%20Management/Authentication%20Bypass.md) |


### Cross Site Scripting (XSS) (A3)

| Numer | Nazwa Podatności | Istotność | Link |
|-------|------------------|-----------|------|
| 1 | XSS Persistent (Second Order) | Wysoka | [Opis podatności](OWASP%202013/A3%20-%20Cross%20Site%20Scripting%20(XSS)/Persistent%20(Second%20Order).md) |
| 2 | XSS Reflected - Capture Data Page | Wysoka | [Opis podatności](OWASP%202013/A3%20-%20Cross%20Site%20Scripting%20(XSS)/Reflected%20(First%20Order)%20-%20Capture%20Data%20Page.md) |
| 3 | XSS Reflected - Set Background Colour Page | Wysoka | [Opis podatności](OWASP%202013/A3%20-%20Cross%20Site%20Scripting%20(XSS)/Reflected%20(First%20order)%20-%20Set%20Background%20colour.md) |
| 4 | XSS Reflected - Via Cookie Injection | Wysoka | [Opis podatności](OWASP%202013/A3%20-%20Cross%20Site%20Scripting%20(XSS)/XSS%20Via%20Cookie%20Injection%20-%20Capture%20Data.md) |
| 5 | XSS Reflected - via HTML attribute | Wysoka | [Opis podatności](OWASP%202013/A3%20-%20Cross%20Site%20Scripting%20(XSS)/XSS%20Via%20HTML%20Attribute.md) |
| 6 | XSS Reflected - via HTTP headers | Wysoka | [Opis podatności](OWASP%202013/A3%20-%20Cross%20Site%20Scripting%20(XSS)/XSS%20Via%20HTTP%20Headers.md) |
| 7 | XSS Reflected - DNS Lookup Page | Wysoka | [Opis podatności](OWASP%202013/A3%20-%20Cross%20Site%20Scripting%20(XSS)/Reflected%20(First%20Order).md) |
| 8 | XSS Against JSON | Wysoka | [Opis podatności](OWASP%202013/A3%20-%20Cross%20Site%20Scripting%20(XSS)/Against%20JSON.md) |

### Insecure Direct Object References (A4)

| Numer | Nazwa Podatności | Istotność | Link |
|-------|------------------|-----------|------|
| 1 | IDOR - Insecure Direct Object Reference | Wysoka | [Opis podatności](OWASP%202013/A4%20-%20Insecure%20Direct%20Object%20References/IDOR%20-%20Text%20File%20Viewer.md) |

### Security Misconfiguration (A5)

| Numer | Nazwa Podatności | Istotność | Link |
|-------|------------------|-----------|------|
| 1 | Zdalne wykonanie kodu przez wysłanie pliku | Wysoka | [Opis podatności](OWASP%202013/A5%20-%20Security%20Misconfiguration/Unrestricted%20File%20Upload.md) |
| 2 | Directory browsing | Niska | [Opis podatności](OWASP%202013/A5%20-%20Security%20Misconfiguration/Directory%20Browsing.md) |

### Missing Function Level Access Control (A7)

| Numer | Nazwa Podatności | Istotność | Link |
|-------|------------------|-----------|------|
| 1 | Dostęp do wrażliwych stron oraz plików przez parametr 'page' | Wysoka | [Opis podatności](OWASP%202013/A7%20-%20Missing%20Function%20Level%20Access%20Control/Secret%20Administrative%20Pages.md) |

## Podsumowanie

