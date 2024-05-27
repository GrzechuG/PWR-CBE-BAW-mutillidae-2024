## Nazwa podatności: Buffer Overflow

**Istotność:** Niska

---

**Opis:**
Buffer Overflow (przepełnienie bufora) jest podatnością, która występuje, gdy dane przekraczają zaalokowaną przestrzeń pamięci (bufor). Może to prowadzić do nadpisania i zmiany danych w sąsiednich adresach pamięci, co umożliwia wykonanie dowolnego kodu lub uszkodzenie danych. W kontekście aplikacji webowej, takie przepełnienie może być wykorzystane do omijania zabezpieczeń, wykonania złośliwego kodu na serwerze, czy nawet prowadzić do awarii systemu.

Aplikacja webowa zawiera formularz, który pozwala użytkownikom wprowadzić ciąg znaków do powtórzenia oraz liczbę powtórzeń. Nie ma walidacji ani ograniczeń na maksymalną wartość liczby powtórzeń.

Użytkownik może wpisać normalny tekst w polu na ciąg znaków, ale w polu na liczbę powtórzeń wpisuje znacznie przekraczającą dopuszczalne wartości liczbę (np. 20000000000). Jeśli aplikacja nie ma ustawionego mechanizmu obronnego na takie duża liczby, może dojść do przepełnienia bufora.

Jeśli dane są przetwarzane przez funkcję lub komponent, który nie jest przygotowany na tak dużą liczbę, możliwe jest przepełnienie bufora. Zależnie od architektury systemu i kontekstu wykonania, może to prowadzić do wykonania złośliwego kodu, awarii systemu, lub innych nieprzewidzianych zachowań aplikacji.

---

**Technika eksploitacji:**
Na stronie http://192.168.255.133/mutillidae/index.php?page=repeater.php wpisać przykładowy tekst w polu **String to repeat**: `hello` oraz dużej liczby (np. `20000000000`) w polu **Number of times to repeat** i zatwierdzenie przyciskiem **Repeat string**

Powoduje to awarię aplikacji i uniemożliwia dalsze korzystanie z niej.

