## Nazwa podatności: XSS: HTMLi via HTTP Header

**Istotność:** 10

---

**Opis:**

Możliwe jest wykonanie dowolnego kodu na stronie, ze względu na wdrożoną funkcjonalność, pokazywania aktualnej wersji przeglądarki w stopce strony, która bierze informacje bezpośrednio z nagłówka zapytania HTTP.
![obraz](https://github.com/GrzechuG/PWR-CBE-BAW-mutillidae-2024/assets/93217316/9749f1db-7eb0-4890-8332-7b1b0e1de1c0)



---

**Technika eksploatacji:**

Przy pomocy takiego oprogramowania jak BurpSuite lub zwykłego zapytania przy pomocy domyślnej aplikacji 'curl', możliwa jest manipulacja nagłówkiem zapytania HTTP co pozwala eksploitacje wdrożonej funkcji w języku javascript na stronie na wywołanie dowolnego kodu. 

Przekazane parametry funkcji są bezpośrednio dostarczane do <div ReflectedXSSExecutionPoint="1" class="footer"> co przez przykładowe wyrażenie '<a href=javascript:alert(1)>xss</a>' pozwala na urchomienie funkcji alert(1) w języku javascript przez uruchomienie hiperłącza co zostało pokazane na obrazku w sekcji OPIS

Funkcja:
```
$(function() {
		$('[ReflectedXSSExecutionPoint]').attr("title", "");
		$('[ReflectedXSSExecutionPoint]').balloon();
	});
```
 
Wyeksploitowany DIV:
```
<div style="border: 1px solid black;">
<div ReflectedXSSExecutionPoint="1" class="footer">Browser: <a href=javascript:alert(1)>xss</a></div>
<div class="footer">PHP Version: 5.3.2-1ubuntu4.30</div>"
</div>
```
 
Źródło: https://security.stackexchange.com/questions/24908/is-it-possible-to-make-an-xss-with-only-html-tags
