# Prompt 11d — korekta wariacji stałych, niskich poziomów i zapisu audytu BB

Pracujesz w repozytorium:

~/Dokumenty/Prace_i_dnie/Wnęka_z_Kerrem

na gałęzi master.

Etapy 11a–11c pozostawiły niezatwierdzone zmiany w drzewie roboczym. Zachowaj je i popraw na miejscu. Nie cofaj poprawnego głównego wyniku 11c:

- dokładnego równania ubranego dla \(Z\);
- pierwszego autentycznego multiplikatywnego kroku Bendera–Bettencourta;
- równań dla \(S_1\) i \(S_2\);
- sektorowej zgodności \(S_1\) z następnym formalnym poziomem WKB.

Nie wykonuj git commit ani git push.

## Cel

Etap 11c przyniósł ważny i zasadniczo poprawny wynik, ale audyt wykazał trzy problemy wymagające naprawy przed commitami:

1. błędny o jeden czynnik \(x^{-1}\) prawy człon w reprezentacji wariacji stałych dla addytywnej poprawki \(Y_1\);
2. liczne utracone backslashe i uszkodzony zapis matematyczny w docs/bender_bettencourt_weak_drive_resummation.md;
3. niepełne sprawdzenie warunku rozwiązalności dla \(e_N^{(4)}\): testy obejmują \(N=2,3,4\), lecz nie traktują osobno brzegowych przypadków \(N=0,1\).

Etap 11d ma być korektą i audytem, nie nowym rozszerzeniem teorii. Nie rozbudowuj manuskryptu i nie próbuj jeszcze dowodzić zamkniętej globalnej hierarchii BB.

## 1. Poprawna reprezentacja wariacji stałych dla \(Y_1\)

Zacznij od równania

\[
\mathcal L_bY_1
=2Y_0'+\frac{2N}{x}Y_0+e_N^{(2)}Y_0,
\qquad
\mathcal L_b
=\frac{x^2}{2}\partial_x^2+\frac{bx}{2}\partial_x-\frac{x}{2}.
\]

Po podzieleniu przez \(x^2/2\) równanie standardowe powinno mieć postać

\[
Y_1''+\frac{b}{x}Y_1'-\frac1xY_1=h(x),
\]

gdzie sprawdzeniu podlega

\[
h(x)
=\frac{4Y_0'(x)}{x^2}
+\frac{4N\,Y_0(x)}{x^3}
+\frac{2e_N^{(2)}Y_0(x)}{x^2}.
\]

W etapie 11c użyto błędnie wyrażenia większego o czynnik \(x\):

\[
\frac{4Y_0'}x+\frac{4NY_0}{x^2}
+\frac{2e_N^{(2)}Y_0}{x}.
\]

Napraw definicję \(h\), pełną formułę wariacji stałych dla \(Y_1\), wszystkie potęgi \(x\) w całkach oraz opis Wrońskianu i rozwiązania przez redukcję rzędu.

Jeżeli

\[
u=Y_0,\qquad
v_*(x)=u(x)\int_{x_*}^{x}\frac{dt}{t^b u(t)^2},
\qquad
W(u,v_*)=x^{-b},
\]

to zapisz pełną poprawną formułę wariacji stałych ze wszystkimi znakami, czynnikami \(x\), punktem bazowym \(x_*\) i stałymi jednorodnymi. Dodaj test symboliczny pokazujący, że zróżnicowanie reprezentacji odtwarza dokładnie równanie na \(Y_1\).

Sprawdź niezależnie reprezentację multiplikatywną

\[
(x^bY_0^2Z_1')'
=2x^{b-2}Y_0^2
\left(2\frac{Y_0'}{Y_0}+\frac{2N}{x}+e_N^{(2)}\right).
\]

Ta formuła z 11c wygląda poprawnie, ale ma zostać ponownie wyprowadzona. Wykaż jawnie równoważność obu reprezentacji przez \(Y_1=Y_0Z_1\).

## 2. Dziedziny, punkty bazowe i normalizacja

Doprecyzuj stwierdzenie o stałych całkowania. Normalizacja Laurenta w \(x=0\) może bezpośrednio ustalać stałe tylko w karcie, którą można połączyć z przebitym otoczeniem zera bez przechodzenia przez zero \(Y_0\) i bez naruszenia wybranych gałęzi. Na dalszych kartach stałe należy przenosić przez warunki przejścia lub analityczną kontynuację.

W dokumentacji rozróżnij:

1. kartę bazową związaną z \(x=0\);
2. dowolną lokalną dziedzinę wolną od zer \(Y_0\);
3. przejście między kartami rozdzielonymi zerami \(Y_0\);
4. artefakty biegunowe \(Z_1=Y_1/Y_0\) przy regularnym \(Y_1\).

Nie sugeruj globalnej, jednoznacznej faktoryzacji przez \(Y_0\).

## 3. Przypadki \(N=0\) i \(N=1\) dla drugiego poziomu

Obecny skrypt sprawdza warunek rozwiązalności prowadzący do \(e_N^{(4)}\) tylko dla \(N=2,3,4\). Dla \(N=0,1\) dolna granica przestrzeni Focka usuwa część formalnych ujemnych współczynników Laurenta, dlatego nie wolno bez sprawdzenia stosować tej samej rekurencji.

Wyprowadź osobno drugi poziom dla \(N=0\), \(N=1\) oraz ogólnego \(N\ge2\). Dla każdego przypadku:

1. wskaż najniższą fizycznie dopuszczalną potęgę lub stan;
2. ustaw współczynniki odpowiadające stanom o ujemnym numerze na zero przed tworzeniem ilorazów;
3. wyprowadź właściwy warunek rezonansowy/rozwiązalności;
4. sprawdź, czy odtwarza niezależny wzór \(e_N^{(4)}\) z etapu 11a;
5. porównaj z rekurencją Rayleigha–Schrödingera co najmniej do rzędu \(\lambda^6\);
6. dodaj testy dla kilku niedegenerowanych wartości \(\delta\).

Jeżeli dla \(N=0\) lub \(N=1\) równanie wymaga osobnej postaci, zapisz ją jawnie. Jeżeli twierdzenie o \(e_N^{(4)}\) nie jest prawdziwe w którymś przypadku, popraw manuskrypt i podaj dokładny zakres ważności. Nie maskuj problemu przez podstawienie do wzoru przeznaczonego dla \(N\ge2\).

## 4. Kompletny audyt zapisu matematycznego w Markdownie

Przejrzyj w całości:

- docs/bender_bettencourt_weak_drive_resummation.md;
- prompts/prompt_11c_multiplicative_bb_iteration.md;
- nowe fragmenty raportu i diffu tylko pod kątem ich zgodności ze źródłami.

W dokumencie audytowym występują uszkodzenia takie jak:

- (N=0,delta=1) zamiast poprawnego zapisu LaTeX;
- (lvert-1\rangle) zamiast \(\lvert-1\rangle\);
- nagie tokeny lambda^2, cdots, mathcal L_b;
- left(...) bez backslasha;
- uszkodzone frac12, w tym tabulator przed frac;
- matematyka zamknięta w zwykłych nawiasach zamiast ogranicznikach LaTeX.

Napraw wszystkie takie przypadki, nie tylko przykłady powyżej.

Wymagane kontrole automatyczne:

- wyszukiwanie podejrzanych nagich tokenów lambda, delta, epsilon, mathcal, frac, left, right, lvert, rangle, cdots;
- wyszukiwanie tabulatorów i znaków sterujących;
- kontrola sparowania ograniczników matematycznych inline i display;
- renderowanie Markdownu, jeżeli repo zawiera odpowiednie narzędzie, albo inna udokumentowana kontrola składni matematycznej.

Nie zmieniaj poprawnych wzorów tylko ze względów stylistycznych.

## 5. Manuskrypt

Główny tekst 11c w manuscript/manuscript.tex wygląda poprawnie i nie należy go przepisywać.

Zmień manuskrypt wyłącznie wtedy, gdy:

- analiza \(N=0,1\) wymaga doprecyzowania zakresu zdania o \(e_N^{(4)}\);
- trzeba skorygować odsyłacz do companion audit;
- wykryjesz rzeczywisty błąd matematyczny lub typograficzny.

Nie zwiększaj liczby stron. Preferuj zastąpienie zdania, nie dopisywanie akapitu. Zachowaj zastrzeżenie, że hierarchia jest lokalna i sektorowa, nie globalna.

## 6. Testy i weryfikacja

Zaktualizuj skrypty 11b–11c albo utwórz mały skrypt 11d. Testy muszą obejmować:

1. poprawne \(h(x)\) po sprowadzeniu równania \(Y_1\) do postaci standardowej;
2. symboliczną weryfikację pełnej reprezentacji wariacji stałych;
3. równoważność addytywnej i multiplikatywnej reprezentacji;
4. ponowną kontrolę dokładnego równania ubranego;
5. \(N=0\) i \(N=1\) na drugim poziomie;
6. ogólne \(N\ge2\);
7. zgodność warunku rozwiązalności z \(e_N^{(4)}\);
8. brak regresji dla \(N=0,b=2\);
9. brak regresji w asymptotyce \(S_1\);
10. kontrolę uszkodzonych tokenów i ograniczników matematycznych w Markdownie.

Uruchom testy 11a–11d, pełny zestaw testów, właściwe skrypty weryfikacyjne, git diff --check, kompilację LaTeX z bibliografią, kontrolę odsyłaczy i ostrzeżeń składu, pdftotext oraz wizualną kontrolę zmienionych stron PDF.

## 7. Obowiązkowe artefakty .diff i .log

Utwórz nowe pliki:

- prompt_11d_correct_vop_low_levels_and_audit_markup.diff;
- prompt_11d_correct_vop_low_levels_and_audit_markup.log.

Plik .diff ma zawierać wyłącznie zmiany etapu 11d względem stanu po 11c. Nie mieszaj do niego pełnych zmian 11a–11c. W razie potrzeby wykonaj przed rozpoczęciem prac migawkę plików objętych etapem 11d.

Plik .log ma zawierać:

1. początkowy git status --short;
2. ponowne wyprowadzenie standardowego równania dla \(Y_1\);
3. poprawny wzór \(h(x)\);
4. pełną poprawioną reprezentację wariacji stałych wraz z Wrońskianem;
5. symboliczną weryfikację tej reprezentacji;
6. ponowne wyprowadzenie reprezentacji dla \(Z_1\);
7. dowód równoważności \(Y_1=Y_0Z_1\);
8. doprecyzowanie dziedzin i normalizacji;
9. osobne wyniki dla \(N=0\), \(N=1\) i \(N\ge2\);
10. porównanie warunku rozwiązalności z \(e_N^{(4)}\);
11. listę naprawionych klas błędów Markdownu;
12. informację, czy manuskrypt wymagał zmiany;
13. liczbę stron przed i po etapie;
14. listę zmienionych i utworzonych plików;
15. wyniki testów, skryptów, kompilacji i kontroli PDF;
16. końcowy git status --short;
17. końcowy werdykt.

Raport zakończ dokładnie jednym z werdyktów:

- VOP CORRECTED; LOW LEVELS AND MULTIPLICATIVE BB RESULT VERIFIED
- VOP CORRECTED; LOW-LEVEL QUALIFICATION REQUIRED
- MULTIPLICATIVE BB CORE VERIFIED; AUDIT REPRESENTATION REQUIRES FURTHER WORK
- STAGE 11C REQUIRES SUBSTANTIAL MATHEMATICAL REVISION

## 8. Zasady końcowe

- Nie wykonuj commitów ani pushów.
- Nie rozszerzaj hierarchii do \(S_3\) ani dalej.
- Nie zmieniaj wyniku 11c bez konkretnego rachunku wskazującego błąd.
- Nie deklaruj pełnej globalnej hierarchii BB.
- Nie pozostawiaj w audycie wzorów, których poprawności nie sprawdzono przez różniczkowanie lub podstawienie.
- Nie traktuj przejścia testów jako dowodu poprawności, jeśli test tylko powtarza ten sam błędny wzór.
- Zachowaj manuskrypt na 31 stronach lub krótszy.

