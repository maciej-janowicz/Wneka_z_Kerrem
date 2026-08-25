# Prompt 11b — asymptotyka Bessela, zgodność z WKB i następna przekątna BB

Pracujesz w repozytorium:

`~/Dokumenty/Prace_i_dnie/Wnęka_z_Kerrem`

na gałęzi `master`.

Etap 11a pozostawił niezatwierdzone zmiany w drzewie roboczym. Zachowaj je i popraw na miejscu. Nie cofaj poprawnych wyników 11a i nie rozpoczynaj rachunku od nowa.

Nie wykonuj `git commit` ani `git push`.

## Cel

Etap 11a poprawnie uzyskał:

- Hamiltonian zerowy zawierający cały wyraz \(\delta z\partial_z\);
- zerową funkcję własną \(z^N/\sqrt{N!}\);
- niedegenerowany rachunek energii przez rząd \(\lambda^4\);
- funkcję falową przez rząd \(\lambda^4\) w skrypcie;
- dokładną trójdiagonalną rekurencję Bargmanna;
- sumę monotonicznej górnej krawędzi w postaci
  \[
  {}_0F_1(;2N+2\delta;-2\lambda z);
  \]
- terminującą sumę dolnej krawędzi w postaci \({}_1F_1\);
- stwierdzenie, że bezpośrednio nie pojawia się funkcja Webera.

Nie zmieniaj tych wyników bez wykazania konkretnego błędu.

Etap 11b ma:

1. zbadać i poprawnie opisać związek górnej sumy \({}_0F_1\) z formalnym zachowaniem WKB dokładnego równania dla dużego \(z\);
2. wyznaczyć i, jeśli to możliwe, zsumować pierwszą podskrajną przekątną perturbacyjnego trójkąta, analogicznie do kolejnego kroku Bendera–Bettencourta;
3. ustalić, czy powstaje hierarchia prefaktora lub wykładnika;
4. usunąć dwie wykryte usterki typograficzne;
5. zachować uczciwe rozróżnienie między formalnym dopasowaniem WKB a globalnym twierdzeniem asymptotycznym.

## 1. Audyt stanu 11a

Przeczytaj w całości:

- `BB.pdf`, zwłaszcza sekcje IV i V;
- `docs/bender_bettencourt_weak_drive_resummation.md`;
- nową sekcję słabego wzbudzenia w `manuscript/manuscript.tex`;
- `scripts/11a_verify_weak_drive.py`;
- `tests/test_11a_weak_drive.py`;
- prompt, diff i raport 11a.

Sprawdź `git status --short`. Nie usuwaj ani nie nadpisuj niezwiązanych zmian.

Na początku raportu podaj:

- które wyniki 11a zachowano;
- które zdanie o WKB wymagało korekty;
- co dokładnie oznacza „górna krawędź” i „pierwsza podskrajna przekątna” w tym problemie.

## 2. Równanie dla sumy górnej krawędzi

Nie ograniczaj się do identyfikacji współczynników szeregu. Dla

\[
Y_0(z;\lambda)={}_0F_1(;b;-2\lambda z),
\qquad b=2N+2\delta,
\]

wyprowadź bezpośrednio równanie różniczkowe

\[
zY_0''+bY_0'+2\lambda Y_0=0.
\]

Następnie podstaw

\[
\Psi_{mathrm{edge}}(z)=\frac{z^N}{\sqrt{N!}}Y_0(z;\lambda)
\]

do dokładnego równania Bargmanna. Oblicz jawną resztę i wskaż, które wyrazy dokładnego równania zostały uchwycone przez równanie krawędziowe, a które odpowiadają:

- dolnemu przejściu \(F^*\partial_z\);
- poprawkom energii;
- ścieżkom z powrotami;
- kolejnym przekątnym perturbacyjnego trójkąta.

Określ rząd reszty w podwójnym skalowaniu

\[
\lambda\to0,
\qquad |z|\to\infty,
\qquad x:=-2\lambda z=O(1),
\]

dla ustalonego \(N\) i niedegenerowanego \(\delta\).

Nie nazywaj tego przybliżenia globalnym, dopóki nie zostaną określone sektory, gałęzie i jednolite oszacowanie błędu.

## 3. Reprezentacja Bessela i jej asymptotyka

Wyprowadź właściwą relację pomiędzy \({}_0F_1\) a funkcją Bessela lub zmodyfikowaną funkcją Bessela. Dla odpowiedniej gałęzi \(x^{1/2}\) użyj i sprawdź relację typu

\[
{}_0F_1(;b;x)
=
\Gamma(b)x^{(1-b)/2}I_{b-1}(2\sqrt{x}),
\]

z uwzględnieniem właściwej kontynuacji do zespolonego

\[
x=-2\lambda z.
\]

Podaj:

- warunki na parametr \(b\);
- wybór gałęzi \(\sqrt{x}\) i \(x^{(1-b)/2}\);
- odpowiednie sektory asymptotyczne;
- dominującą i subdominującą składową;
- wykładnik i prefaktor potęgowy.

Wykaż jawnie, czy asymptotyka zawiera

\[
\exp\!\left(\pm2\sqrt{-2\lambda z}\right).
\]

Nie pomijaj mnożników potęgowych ani faz Stokesa. Jeśli w różnych sektorach naturalniejsza jest funkcja \(J\) zamiast \(I\), podaj obie równoważne reprezentacje i ich zakresy.

## 4. Niezależny rachunek WKB dokładnego równania

Wstaw do dokładnego równania Bargmanna ansatz

\[
\Psi(z)=\exp S(z)
\]

albo

\[
\Psi(z)=z^N A(z)e^{S(z)}
\]

i przeprowadź formalny rachunek dużego \(|z|\) w reżimie \(\lambda\ll1\), z \(\lambda z\) odpowiednio skalowanym.

Wyprowadź co najmniej:

1. równanie eikonalne;
2. wiodący wykładnik;
3. pierwszy prefaktor transportowy;
4. rząd wyrazów pochodzących od \(\delta z\partial_z\), \(F^*\partial_z\) i energii.

Sprawdź w szczególności rachunek

\[
\frac12z^2(S')^2+\lambda z\simeq0,
\]

oraz wynikające z niego

\[
S'(z)\simeq\pm\sqrt{-\frac{2\lambda}{z}},
\qquad
S(z)\simeq\pm2\sqrt{-2\lambda z}.
\]

Nie przyjmuj tych wzorów bez kontroli znaków, gałęzi i czynników liczbowych.

Porównaj wynik rząd po rzędzie z asymptotyką Bessela. Rozstrzygnij osobno:

- zgodność wiodącego wykładnika;
- zgodność prefaktora;
- brakujące poprawki;
- sektory, w których porównanie jest ważne.

Jeżeli górna suma odtwarza tylko wiodący wykładnik, napisz dokładnie „formal leading WKB exponent”, a nie „WKB solution” ani „global WKB approximation”.

## 5. Pierwsza podskrajna przekątna

Zdefiniuj perturbacyjny trójkąt jednoznacznie. Górna monotoniczna krawędź odpowiada współczynnikom prowadzącym z \(|N\rangle\) do \(|N+k\rangle\) w rzędzie \(k\), bez kroków w dół.

Pierwsza podskrajna rodzina powinna obejmować współczynniki o najmniejszej liczbie kroków wstecznych, na przykład stany \(|N+k-2\rangle\) w rzędzie \(k\), wraz z wkładami wynikającymi z pierwszej poprawki energii. Ustal precyzyjną definicję na podstawie rekurencji, zamiast zakładać ją intuicyjnie.

Wykonaj następujące kroki:

1. wygeneruj dostatecznie wiele wyrazów symbolicznych dla ogólnego \(N,\delta\);
2. wyprowadź rekurencję dla pierwszej podskrajnej rodziny;
3. oddziel wkłady pojedynczego powrotu od wkładów energii \(e_N^{(2)}\);
4. znajdź funkcję tworzącą tej rodziny;
5. sprawdź, czy można ją zapisać przez \({}_0F_1\), jego pochodne, funkcje o przesuniętym parametrze, całki albo inną funkcję specjalną;
6. sprawdź wynik przez rozwinięcie w \(\lambda\) co najmniej do rzędu dostępnego w 11a;
7. oblicz jej wkład w podwójnym skalowaniu \(\lambda z=O(1)\).

Jeśli pełne symboliczne sumowanie nie jest możliwe, podaj dokładną rekurencję i pierwsze wyrazy oraz sformułuj jasno ograniczony wynik częściowy. Nie dopasowuj funkcji specjalnej tylko na podstawie kilku współczynników.

## 6. Czy zaczyna się hierarchia Bendera–Bettencourta?

Porównaj uzyskaną podskrajną sumę z metodą sekcji IV artykułu BB. Zbadaj, czy można zapisać przybliżenie w jednej z postaci

\[
\Psi_N(z;\lambda)
=
\frac{z^N}{\sqrt{N!}}
Y_0(-2\lambda z)
\left[1+\lambda^p R_1(-2\lambda z)+\cdots\right],
\]

lub

\[
\Psi_N(z;\lambda)
=
\frac{z^N}{\sqrt{N!}}
\exp\!\left[S_0(-2\lambda z)+\lambda^pS_1(-2\lambda z)+\cdots\right].
\]

Ustal właściwą potęgę \(p\). Rozstrzygnij, czy następna przekątna:

- koryguje wyłącznie prefaktor;
- koryguje wykładnik;
- przesuwa parametr funkcji Bessela;
- tworzy kombinację niezależnych rozwiązań;
- albo nie daje zamkniętej reorganizacji.

Nie twierdź, że odtworzono pełną iterację BB, jeśli wykonano tylko jeden dodatkowy poziom. Podaj dokładnie, ile przekątnych zsumowano.

## 7. Poprawki typograficzne

Usuń dwa stwierdzone błędy:

1. W `docs/bender_bettencourt_weak_drive_resummation.md` popraw rekurencję zawierającą przecinki:
   \[
   f\sqrt n,c_{n-1}+f^*\sqrt{n+1},c_{n+1}
   \]
   na poprawny iloczyn, na przykład
   \[
   f\sqrt n\,c_{n-1}+f^*\sqrt{n+1}\,c_{n+1}.
   \]
2. Na stronie z równaniem zerowego rzędu w PDF-ie pojawił się literalny tekst `qquad` przed \(N\in\mathbb N_0\). Znajdź rzeczywistą przyczynę w źródle LaTeX i popraw ją. Nie maskuj błędu zmianą ekstrakcji tekstu.

Po kompilacji sprawdź tę stronę zarówno wizualnie, jak i przez `pdftotext`.

## 8. Aktualizacja dokumentacji i manuskryptu

Popraw na miejscu:

- `docs/bender_bettencourt_weak_drive_resummation.md`;
- `manuscript/manuscript.tex`;
- `scripts/11a_verify_weak_drive.py`;
- `tests/test_11a_weak_drive.py`;

albo dodaj odrębny skrypt/test 11b, jeżeli poprawi to przejrzystość.

W manuskrypcie:

- zastąp zbyt mocne zaprzeczenie związku z WKB poprawnym stwierdzeniem o formalnej zgodności wiodącego wykładnika, jeśli zostanie potwierdzona;
- podaj relację \({}_0F_1\)–Bessel i wynik porównania WKB zwięźle;
- dodaj pierwszy wynik podskrajny tylko wtedy, gdy został analitycznie wyprowadzony i zweryfikowany;
- zachowaj ostrzeżenie, że nie jest to globalne twierdzenie WKB ani suma pełnego szeregu;
- nie zmieniaj sekcji Olvera i Fedoryuka poza minimalnym odsyłaczem, jeśli okaże się konieczny.

## 9. Weryfikacja

Rozbuduj testy tak, aby sprawdzały:

- równanie różniczkowe spełniane przez \({}_0F_1\);
- dokładną resztę po podstawieniu \(z^NY_0\) do równania Bargmanna;
- relację \({}_0F_1\) z funkcją Bessela dla kilku zespolonych argumentów i niedegenerowanych parametrów;
- zgodność asymptotyczną wykładnika w wybranych sektorach;
- rekurencję i sumę pierwszej podskrajnej przekątnej;
- odtworzenie współczynników 11a do \(\lambda^4\);
- brak regresji w energii \(e_N^{(2)}\) i \(e_N^{(4)}\).

Testy numeryczne powinny podawać precyzję, tolerancje, argumenty i użyte gałęzie. Nie używaj diagonalizacji jako dowodu; jest dopuszczalna jedynie jako dodatkowa kontrola.

## 10. Kontrola końcowa

Uruchom:

- pełny zestaw testów;
- testy skupione 11a–11b;
- skrypty weryfikacyjne 08–11b;
- `git diff --check`;
- pełną kompilację LaTeX z bibliografią;
- kontrolę niezdefiniowanych cytowań i odwołań;
- kontrolę `Overfull` i `Underfull`;
- renderowanie i wizualną kontrolę wszystkich zmienionych stron;
- `pdftotext` dla równania, w którym wystąpiło `qquad`;
- zgodność bajtową kanonicznej i wynikowej kopii PDF-u.

## 11. Artefakty 11b

Zapisz prompt jako:

- `prompts/prompt_11b_bessel_wkb_and_next_diagonal.md`.

Utwórz nowe, odrębne pliki:

- `prompt_11b_bessel_wkb_and_next_diagonal.diff`;
- `prompt_11b_bessel_wkb_and_next_diagonal.log`.

Plik `.diff` ma zawierać wyłącznie zmiany wykonane przez 11b względem stanu pozostawionego przez 11a, a nie cały skumulowany diff od ostatniego commita. W razie potrzeby zapisz stan początkowy w katalogu tymczasowym poza repozytorium. Nie modyfikuj historii Git.

Raport `.log` ma zawierać:

1. listę zachowanych wyników 11a;
2. wyprowadzenie równania górnej krawędzi;
3. dokładną resztę względem równania Bargmanna;
4. relację \({}_0F_1\)–Bessel wraz z gałęziami i sektorami;
5. niezależny rachunek WKB;
6. werdykt o zgodności wykładnika i prefaktora;
7. definicję i rekurencję pierwszej podskrajnej przekątnej;
8. jej funkcję tworzącą albo precyzyjny wynik częściowy;
9. ocenę, czy rozpoczyna się iteracyjna hierarchia BB;
10. opis obu poprawek typograficznych;
11. zmienione i utworzone pliki;
12. wyniki testów, kompilacji, `pdftotext` i kontroli wizualnej;
13. początkowy i końcowy `git status --short`.

Raport zakończ jednym z werdyktów:

- `LEADING BESSEL–WKB MATCH VERIFIED; NEXT DIAGONAL SUMMED`;
- `LEADING BESSEL–WKB MATCH VERIFIED; NEXT DIAGONAL PARTIAL`;
- `BESSEL–WKB MATCH REQUIRES CORRECTION`;
- `STAGE 11A CLAIMS REQUIRE SUBSTANTIAL REVISION`.

Nie wykonuj commitów ani pushów.
