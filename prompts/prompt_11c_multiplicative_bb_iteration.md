# Prompt 11c — właściwa multiplikatywna iteracja Bendera–Bettencourta

Pracujesz w repozytorium:

`~/Dokumenty/Prace_i_dnie/Wnęka_z_Kerrem`

na gałęzi `master`.

Etapy 11a i 11b pozostawiły niezatwierdzone zmiany w drzewie roboczym. Zachowaj je i popraw na miejscu. Nie cofaj poprawnych wyników wcześniejszych etapów.

Nie wykonuj `git commit` ani `git push`.

## Główny cel

Etap 11b poprawnie zsumował:

1. monotoniczną górną krawędź pierwotnego szeregu Rayleigha–Schrödingera,
   \[
   Y_0(x)={}_0F_1(;b;x),
   \qquad b=2N+2\delta,
   \qquad x=-2\lambda z;
   \]
2. pierwszą górną podprzekątną jako addytywną poprawkę
   \[
   \frac{\Psi_N}{z^N/\sqrt{N!}}
   =Y_0(x)+\lambda^2Y_1(x)+O(\lambda^4).
   \]

To nie jest jeszcze właściwy drugi krok metody Bendera–Bettencourta. U BB wysumowany szereg z poprzedniego poziomu staje się **czynnikiem** nowego przybliżenia, a kolejny rachunek zaburzeń wykonuje się już względem funkcji zawierającej ten czynnik.

Zbadaj, czy dla wzbudzanego modu Kerra można zbudować rzeczywistą multiplikatywną hierarchię BB, zaczynając od

\[
\Psi_N(z;\lambda)
=\frac{z^N}{\sqrt{N!}}\,Y_0(x)\,Z(x;\lambda),
\qquad
Z=1+\lambda^2Z_1+\lambda^4Z_2+\cdots,
\]

albo równoważnie, lokalnie poza zerami \(Y_0\),

\[
\Psi_N(z;\lambda)
=\frac{z^N}{\sqrt{N!}}\,Y_0(x)
\exp\!\left[
 \lambda^2S_1(x)+\lambda^4S_2(x)+\cdots
\right].
\]

Nie zakładaj z góry, że hierarchia się domyka. Rzetelny wynik negatywny lub częściowy jest dopuszczalny, ale trzeba dokładnie wskazać przeszkodę.

## 1. Audyt punktu wyjścia

Przeczytaj w całości:

- sekcje IV i V `BB.pdf`;
- aktualną sekcję weak-drive w manuskrypcie;
- `docs/bender_bettencourt_weak_drive_resummation.md`;
- skrypty i testy 11a–11b;
- raporty `.log` z etapów 11a–11b.

Najpierw opisz krótko, lecz precyzyjnie, czym różnią się:

1. sumowanie kolejnej przekątnej pierwotnego szeregu perturbacyjnego;
2. wtórne algebraiczne wyłączenie \(Y_0\) przed nawias;
3. właściwa iteracja BB, w której \(Y_0\) od początku należy do operatora zerowego lub funkcji zerowego przybliżenia dla następnego rachunku.

Nie nazywaj wyniku 11b „iteracyjną hierarchią BB”, dopóki nie zostanie to rzeczywiście wykazane.

## 2. Wyprowadzenie dokładnego równania ubranego

Punktem wyjścia ma być dokładne równanie Bargmanna po wyłączeniu
\(z^N/\sqrt{N!}\) i przejściu do \(x=-2\lambda z\). Użyj

\[
\mathcal L_b
=\frac{x^2}{2}\partial_x^2
 +\frac{bx}{2}\partial_x
 -\frac{x}{2},
\qquad
\mathcal L_bY_0=0.
\]

Wyprowadź bez pomijania członów dokładne równanie dla \(Z\) z podstawienia
\(Y=Y_0Z\). W szczególności jawnie oblicz operator sprzężony/ubrany

\[
Y_0^{-1}\mathcal L_b(Y_0Z)
=\frac{x^2}{2}Z''
 +\left(x^2\frac{Y_0'}{Y_0}+\frac{bx}{2}\right)Z'.
\]

Następnie dołącz dokładnie:

- człon pochodzący od opuszczonego działania w dół;
- przesunięcie energii
  \[
  \epsilon-e_N
  =\lambda^2e_N^{(2)}+\lambda^4e_N^{(4)}+\cdots;
  \]
- wszystkie czynniki wynikające z przejścia \(z\mapsto x\).

Zweryfikuj równanie symbolicznie przez bezpośrednie podstawienie do pierwotnego równania Bargmanna.

## 3. Pierwszy rzeczywisty krok multiplikatywny

Podstaw

\[
Z=1+\lambda^2Z_1+O(\lambda^4)
\]

i wyprowadź równanie dla \(Z_1\) bez korzystania z gotowego równania na \(Y_1\). Dopiero potem sprawdź, czy na każdej dziedzinie wolnej od zer \(Y_0\)

\[
Z_1=\frac{Y_1}{Y_0}.
\]

Wymagane są:

- właściwy warunek normalizacji;
- określenie dziedziny ważności;
- analiza zachowania w zerach \(Y_0\);
- ustalenie, czy bieguny \(Z_1\) są jedynie artefaktem faktoryzacji, podczas gdy \(Y_0Z_1=Y_1\) pozostaje poprawną funkcją addytywną;
- jawna reprezentacja \(Z_1\), jeśli jest możliwa: całkowa, przez logarytmiczną pochodną \(Y_0\), funkcje specjalne albo dobrze określony operator odwrotny.

Nie wystarczy napisać, że „variation of parameters can be used”. Jeśli podajesz reprezentację wariacji stałych, zapisz całki, ich granice lub bazowy punkt, Wrońskian oraz warunki normalizujące. Jeżeli nie można tego zrobić globalnie, podaj poprawną reprezentację lokalną i opisz przejścia między dziedzinami.

## 4. Postać wykładnicza i drugi poziom

Na dziedzinie, na której \(Y_0\neq0\), wprowadź

\[
Z=\exp\!\left[
 \lambda^2S_1+\lambda^4S_2+O(\lambda^6)
\right].

Wyprowadź równania dla \(S_1\) i — o ile rachunek pozostaje kontrolowany — dla \(S_2\). Sprawdź relacje

\[
S_1=\frac{Y_1}{Y_0},
\qquad
S_2=\frac{Y_2}{Y_0}
-\frac12\left(\frac{Y_1}{Y_0}\right)^2,

\]

z odpowiednią definicją \(Y_2\).

Rozstrzygnij, czy równanie dla \(S_2\):

- można wyprowadzić bez jawnego sumowania całej drugiej podprzekątnej pierwotnego szeregu;
- ma strukturę pozwalającą na iterację;
- wymaga nowych warunków rozwiązalności, które odtwarzają \(e_N^{(4)}\);
- daje naturalną rekurencję dla kolejnych \(S_j\).

Nie musisz uzyskać zamkniętego wzoru na \(S_2\), aby etap był udany. Wymagane jest natomiast poprawne równanie i uczciwa ocena jego rozwiązywalności.

## 5. Związek z WKB

Zbadaj asymptotykę \(Z_1\) lub \(S_1\) dla

\[
1\ll|x|=2|\lambda z|

\]

w sektorach, w których wybrany składnik asymptotyki Bessela jest dominujący i oddzielony od drugiego siodła.

Porównaj ją z następnymi członami formalnego rozwinięcia WKB dokładnego równania normalnego

\[
u''+K(z)u=0,
\]

uwzględniając:

- czynnik cechowania \(e^{\lambda/z}\);
- pierwszy człon zależny od energii;
- następny człon transportowy;
- gałęzie pierwiastka i sektory Stokesa.

Rozstrzygnij osobno:

1. czy \(Y_0\) daje tylko wiodący wykładnik i potęgę;
2. czy \(S_1\) odtwarza następny, niebanalny człon WKB;
3. czy pojawia się systematyczny wzorzec sugerujący hierarchię BB;
4. czy zgodność jest wyłącznie formalna, lokalna lub sektorowa.

Nie nazywaj wyniku globalnym przybliżeniem WKB bez dowodu błędu i globalnego twierdzenia połączeniowego.

## 6. Trzy obowiązkowe poprawki z audytu 11b

Niezależnie od powodzenia multiplikatywnej iteracji wykonaj wszystkie trzy poprawki.

### 6.1. Regularny przypadek \(N=0, b=2\)

Obecny wzór

\[
d_{-1}=-\frac{4N}{b-2}
\]

daje nieoznaczoność \(0/0\) dla niedegenerowanego przypadku \(N=0,\delta=1\), czyli \(b=2\). Potraktuj ten przypadek osobno. Dla \(N=0\) nie istnieje stan \(\lvert N-1\rangle\), toteż składnik \(x^{-1}\) powinien być nieobecny i należy otrzymać \(d_{-1}=0\).

Popraw dokumentację i manuskrypt oraz dodaj testy obejmujące co najmniej:

- \(N=0,\delta=1\);
- inne niedegenerowane wartości \(\delta\) dla \(N=0\);
- przypadki \(N\ge1\), dla których dotychczasowy wzór pozostaje poprawny.

Nie ukrywaj nieoznaczoności przez mechaniczne upraszczanie symboliczne.

### 6.2. Rzeczywista reprezentacja wariacji stałych

Manuskrypt twierdzi obecnie, że reprezentację wariacji stałych podano w companion audit, podczas gdy audyt wskazuje tylko parę rozwiązań jednorodnych. Albo podaj pełną reprezentację z całkami, Wrońskianem, bazowym punktem i normalizacją, albo osłab to zdanie tak, aby dokładnie odpowiadało temu, co rzeczywiście wyprowadzono.

Uwzględnij przypadki rezonansowe, w których
\(x^{1-b}{}_0F_1(;2-b;x)\) nie może być bezrefleksyjnie użyte jako niezależne rozwiązanie i potrzebne jest rozwiązanie graniczne/logarytmiczne.

### 6.3. Znak i gałąź prefaktora WKB

W równaniu normalnym

\[
K(z)\sim\frac{2\lambda}{z}.

\]

Naturalny prefaktor Liouville’a–Greena ma postać

\[
z^{-\delta}\left(\frac{2\lambda}{z}\right)^{-1/4},

\]

po ustaleniu gałęzi. W dokumentacji wystąpiło
\(z^{-\delta}(-2\lambda/z)^{-1/4}\). Sprawdź znak od początku. Jeśli różnica jest wyłącznie stałą fazą zależną od gałęzi, napisz to jawnie; następnie użyj jednego konsekwentnego zapisu.

## 7. Zakres sukcesu i werdykt

Oceń rezultat według następującej hierarchii:

### Poziom A — minimalny, ale wartościowy

- dokładne równanie ubrane dla \(Z\);
- niezależnie wyprowadzone równanie dla \(Z_1\);
- dowód lokalnej zgodności \(Z_1=Y_1/Y_0\);
- trzy mniejsze poprawki wykonane i przetestowane.

### Poziom B — istotny wynik

- jawna, kontrolowana reprezentacja \(Z_1\);
- analiza jego zer, biegunów i asymptotyki sektorowej;
- wykazanie, że jest to pierwszy autentyczny multiplikatywny krok BB.

### Poziom C — bardzo mocny wynik

- poprawne równanie dla \(S_2\) lub ogólnego \(S_j\);
- warunek rozwiązalności odtwarzający kolejne poprawki energii;
- zgodność \(S_1\) z następnym niebanalnym członem WKB.

### Poziom D — wynik wyjątkowy

- zamknięta lub rekurencyjna multiplikatywna hierarchia BB;
- dowód, że kolejne poziomy systematycznie odtwarzają formalne rozwinięcie WKB.

Nie deklaruj wyższego poziomu, jeśli brakuje któregokolwiek z jego zasadniczych elementów.

## 8. Manuskrypt: rygor i zwięzłość

Manuskrypt ma już około 30 stron. Nie dopisuj obszernego dziennika rachunków. Szczegóły techniczne umieść w dokumencie audytowym, skrypcie i testach.

W samym manuskrypcie:

- popraw fałszywe lub zbyt mocne zdania z 11b;
- dodaj tylko najważniejsze równanie ubrane i najważniejszy wynik;
- jeśli multiplikatywny krok BB się powiedzie, zastąp nim część obecnego opisu addytywnej podprzekątnej zamiast dopisywać niezależną długą podsekcję;
- staraj się nie zwiększyć długości manuskryptu o więcej niż około pół strony;
- jeśli to możliwe, skróć sekcję weak-drive bez utraty treści;
- wyraźnie oddziel formalne dopasowanie WKB od globalnego twierdzenia asymptotycznego;
- nie zmieniaj sekcji Olvera i Fedoryuka poza absolutnie koniecznymi odsyłaczami.

## 9. Dokumentacja, obliczenia i testy

Zaktualizuj odpowiednio:

- `docs/bender_bettencourt_weak_drive_resummation.md`;
- `manuscript/manuscript.tex`;
- skrypty weryfikacyjne 11b albo utwórz osobny skrypt 11c;
- testy 11b albo utwórz osobne testy 11c.

Testy powinny obejmować co najmniej:

1. symboliczną zgodność dokładnego równania dla \(Z\) z równaniem Bargmanna;
2. równanie dla \(Z_1\);
3. zgodność \(Y_0Z_1=Y_1\) na poziomie szeregu do możliwie wysokiego rzędu;
4. przypadek \(N=0,\delta=1\);
5. zgodność z rekurencją Rayleigha–Schrödingera dla kilku \(N\) i symbolicznego lub kilku numerycznych \(\delta\);
6. poprawkę energii \(e_N^{(2)}\), a jeśli pojawi się drugi poziom — także \(e_N^{(4)}\);
7. asymptotykę sektorową \(Z_1\) lub \(S_1\), jeżeli została wyprowadzona;
8. brak regresji w etapach 11a–11b.

Uruchom:

- testy 11a–11c;
- pełny zestaw testów;
- wszystkie właściwe skrypty weryfikacyjne;
- `git diff --check`;
- kompilację LaTeX z bibliografią;
- kontrolę niezdefiniowanych odsyłaczy i ostrzeżeń składu;
- `pdftotext` dla zmienionej sekcji;
- wizualną kontrolę wszystkich zmienionych stron PDF.

## 10. Obowiązkowe artefakty `.diff` i `.log`

Utwórz nowe pliki:

- `prompt_11c_multiplicative_bb_iteration.diff`;
- `prompt_11c_multiplicative_bb_iteration.log`.

Plik `.diff` ma zawierać wyłącznie zmiany etapu 11c względem stanu po 11b. Nie mieszaj do niego pełnego diffu 11a–11b. Jeżeli trzeba, sporządź migawkę stanu początkowego przed rozpoczęciem zmian i wygeneruj różnicę względem tej migawki.

Plik `.log` ma zawierać:

1. początkowy `git status --short`;
2. zwięzły audyt różnicy między addytywnym sumowaniem przekątnej a iteracją BB;
3. dokładne równanie ubrane dla \(Z\);
4. równanie i normalizację \(Z_1\);
5. dowód lub test relacji \(Z_1=Y_1/Y_0\);
6. jawną reprezentację \(Z_1\) albo precyzyjny opis przeszkody;
7. analizę zer \(Y_0\) i lokalności faktoryzacji;
8. równanie dla \(S_1\), a jeśli uzyskano — także dla \(S_2\) lub ogólnego \(S_j\);
9. porównanie z kolejnym członem WKB;
10. wynik poprawki przypadku \(N=0,b=2\);
11. wynik poprawki reprezentacji wariacji stałych;
12. wynik poprawki znaku/gałęzi prefaktora WKB;
13. ocenę przyrostu długości manuskryptu;
14. listę zmienionych i utworzonych plików;
15. wyniki testów, skryptów, kompilacji i inspekcji PDF;
16. końcowy `git status --short`;
17. końcowy werdykt.

Raport zakończ dokładnie jednym z werdyktów:

- `MULTIPLICATIVE BB HIERARCHY ESTABLISHED`;
- `FIRST MULTIPLICATIVE BB STEP AND NEXT WKB TERM VERIFIED`;
- `FIRST MULTIPLICATIVE BB STEP VERIFIED; HIGHER ITERATION OPEN`;
- `DRESSED EQUATION VERIFIED; MULTIPLICATIVE ITERATION PARTIAL`;
- `MULTIPLICATIVE BB ANALOGY FAILS FOR A PRECISELY IDENTIFIED REASON`;
- `STAGE 11B REQUIRES SUBSTANTIAL REVISION`.

## 11. Zasady końcowe

- Nie wykonuj commitów ani pushów.
- Nie ukrywaj niepowodzenia za sformułowaniem „future work”. Podaj dokładne równanie lub dokładną przeszkodę.
- Nie utożsamiaj lokalnej faktoryzacji przez \(Y_0\) z globalnym twierdzeniem.
- Nie utożsamiaj zsumowania kolejnej surowej podprzekątnej z iteracją BB.
- Nie deklaruj zgodności z następnym członem WKB bez jawnego porównania współczynników.
- Zachowaj terminologię projektu i dotychczasowe konwencje parametrów.
