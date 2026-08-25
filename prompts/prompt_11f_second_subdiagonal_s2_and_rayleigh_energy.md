# Prompt 11f — druga podprzekątna \(Y_2\), czynnik \(S_2\) i energia Rayleigha

Pracujesz w repozytorium:

~/Dokumenty/Prace_i_dnie/Wnęka_z_Kerrem

na gałęzi master.

Zachowaj wszystkie niezatwierdzone zmiany etapów 11a–11e. Nie wykonuj git commit ani git push.

## Główne cele

Etapy 11a–11e ustaliły:

\[
\frac{\Psi_N}{z^N/\sqrt{N!}}
=Y_0+\lambda^2Y_1+\lambda^4Y_2+\cdots,
\qquad
Y_0={}_0F_1(;b;x),
\]

\[
b=2N+2\delta,\qquad x=-2\lambda z,
\]

oraz lokalną postać multiplikatywną

\[
\frac{\Psi_N}{z^N/\sqrt{N!}}
=Y_0\exp\!\left(\lambda^2S_1+\lambda^4S_2+\cdots\right).
\]

Pierwszy prawdziwy krok Bendera–Bettencourta został potwierdzony:

\[
S_1=\frac{Y_1}{Y_0},
\qquad
\mathcal A_bS_1
=2\left(\frac{Y_0'}{Y_0}+\frac Nx\right)+e_N^{(2)}.
\]

W etapie 11f:

1. wyprowadź i spróbuj wysumować drugą surową podprzekątną \(Y_2\);
2. skonstruuj drugi skumulowany czynnik
   \[
   S_2=\frac{Y_2}{Y_0}-\frac12\left(\frac{Y_1}{Y_0}\right)^2;
   \]
3. zbadaj, czy odtworzony globalnie regularny stan przybliżony daje użyteczny analityczny lub szybko zbieżny wzór na energię przez iloraz Rayleigha;
4. określ rzeczywisty rząd dokładności tej energii, zamiast zakładać go z góry.

Nie próbuj jeszcze konstruować \(S_3\), chyba że jest to niezbędne wyłącznie do wykazania granicy dokładności. Nie rozpoczynaj nowego podejścia silnego sprzężenia.

## 1. Dokładne równanie i rekurencja dla \(Y_2\)

Z równania ubranego wyprowadź niezależnie, a następnie sprawdź:

\[
\mathcal L_bY_2
=2Y_1'+\frac{2N}{x}Y_1
+e_N^{(2)}Y_1+e_N^{(4)}Y_0,
\]

\[
\mathcal L_b
=\frac{x^2}{2}\partial_x^2+\frac{bx}{2}\partial_x-\frac{x}{2}.
\]

Przyjmij

\[
Y_2(x)=\sum_m q_mx^m,
\qquad
Y_1(x)=\sum_m d_mx^m,
\qquad
Y_0(x)=\sum_{m\ge0}a_mx^m.
\]

Wyprowadź pełną rekurencję \(q_m\), w tym:

- właściwy warunek rozwiązalności w \(m=0\);
- osobne dolne granice dla \(N=0\), \(N=1\) i \(N\ge2\);
- normalizację pośrednią;
- dokładne odtworzenie \(e_N^{(4)}\);
- brak współczynników odpowiadających ujemnym stanom Focka.

Sprawdź współczynniki względem niezależnej rekurencji Rayleigha–Schrödingera do możliwie wysokiego rzędu, co najmniej przez \(\lambda^8\), jeśli czas obliczeń na to pozwala.

## 2. Próba wysumowania \(Y_2\)

Nie poprzestawaj na formalnej rekurencji. Spróbuj uzyskać jedną lub kilka z następujących reprezentacji:

1. pełną funkcję tworzącą;
2. reprezentację wariacji stałych z jawnymi całkami, Wrońskianem i normalizacją;
3. wyrażenie przez \(Y_0\), \(Y_1\), ich pochodne i przesunięte funkcje \({}_0F_1\);
4. zbieżny szereg hipergeometryczny lub kombinację takich szeregów;
5. dobrze określony operator Greenowski działający na źródło drugiego poziomu.

Każdą formułę całkową sprawdź przez bezpośrednie różniczkowanie. Nie nazywaj samego równania różniczkowego „wysumowaniem”, jeżeli nie uzyskano reprezentacji rozwiązania z ustaloną normalizacją.

Zbadaj:

- zachowanie przy \(x=0\);
- regularność \(z^NY_2\) jako funkcji Bargmanna;
- asymptotykę w dominujących sektorach Bessela;
- zachowanie przy zerach \(Y_0\);
- możliwość kontynuacji między kartami.

## 3. Konstrukcja \(S_2\)

Wyprowadź bezpośrednio z postaci wykładniczej:

\[
\mathcal A_bS_2
=2S_1'+e_N^{(4)}
-\frac{x^2}{2}(S_1')^2,
\]

\[
\mathcal A_b
=\frac{x^2}{2}\partial_x^2
+\left(x^2\frac{Y_0'}{Y_0}+\frac{bx}{2}\right)\partial_x.
\]

Następnie wykaż, z właściwą normalizacją, że

\[
S_2
=\frac{Y_2}{Y_0}
-\frac12\left(\frac{Y_1}{Y_0}\right)^2.
\]

Uzyskaj możliwie jawną lokalną reprezentację \(S_2\). W szczególności ustal:

- rząd i współczynniki biegunów \(S_2\) w zerach \(Y_0\);
- czy kombinacja skumulowana usuwa część silniejszych osobliwości;
- jak odtwarza się regularny składnik addytywny
  \[
  Y_2=Y_0\left(S_2+\frac12S_1^2\right);
  \]
- czy drugi krok daje nową strukturę, której nie widać w surowej podprzekątnej.

Nie traktuj lokalnie obciętej funkcji

\[
Y_0\exp(\lambda^2S_1+\lambda^4S_2)
\]

jako automatycznie całkowitej funkcji Bargmanna. Sprawdź jej zachowanie w zerach \(Y_0\).

## 4. Następny poziom formalnego WKB

Wyprowadź sektorową asymptotykę \(Y_2\) oraz \(S_2\) dla

\[
1\ll |x|,
\]

w sektorze z wybranym dominującym składnikiem Bessela. Porównaj ją z formalnym rozwinięciem WKB dokładnego równania normalnego.

Oddziel:

- drugi człon poprawki energetycznej;
- poprawki pochodzące z cechowania \(e^{\lambda/z}\);
- drugi człon transportowy;
- nieliniowy składnik \(-x^2(S_1')^2/2\);
- zależność od gałęzi i sektora.

Stwierdź dokładnie, czy \(S_2\) odtwarza następny pełny poziom WKB, tylko jego część, czy też asymptotyka wymaga jeszcze następnej podprzekątnej.

## 5. Globalnie dopuszczalny stan do wartości oczekiwanej

Do obliczania normy i energii nie używaj bezpośrednio lokalnej postaci wykładniczej, jeżeli ma bieguny lub osobliwości w zerach \(Y_0\).

Zbuduj globalnie regularny stan przybliżony w jednej z równoważnych postaci:

\[
\widetilde\Psi_N(z;\lambda)
=\frac{z^N}{\sqrt{N!}}
\left[Y_0(x)+\lambda^2Y_1(x)+\lambda^4Y_2(x)\right],
\]

z poprawnym nawiasowaniem, albo przez jego współczynniki Focka

\[
\widetilde\Psi_N=\sum_{n\ge0}\widetilde c_n|n\rangle.
\]

Stan ma być dokładnie tym, który wynika z dotychczasowej konwencji
\(\Psi_N/(z^N/\sqrt{N!})=Y_0+\lambda^2Y_1+\lambda^4Y_2\).

Wymagane są:

- dowód lub test całkowitości w \(z\);
- sprawdzenie normy Bargmanna–Focka;
- jawne lub szybko zbieżne współczynniki \(\widetilde c_n\);
- kontrola ogona szeregu normy;
- normalizacja stanu.

## 6. Iloraz Rayleigha

Dla znormalizowanego stanu oblicz

\[
\mathcal E_N^{\rm R}(\lambda)
=\frac{\langle\widetilde\Psi_N,h\widetilde\Psi_N\rangle}
{\langle\widetilde\Psi_N,\widetilde\Psi_N\rangle},
\qquad
h=\frac HV.
\]

W bazie Focka użyj dokładnie

\[
\langle h\rangle
=\frac{
\sum_{n\ge0}e_n|\widetilde c_n|^2
+2\lambda\,\Re\sum_{n\ge0}
\sqrt{n+1}\,\widetilde c_n^*\widetilde c_{n+1}}
{\sum_{n\ge0}|\widetilde c_n|^2},
\]

po wykonaniu obrotu fazowego sprowadzającego wzbudzenie do \(\lambda>0\).

Spróbuj otrzymać:

1. wyrażenie analityczne przez funkcje hipergeometryczne;
2. jeśli to niemożliwe, jednoznaczny zbieżny szereg z kontrolą ogona;
3. stabilny algorytm numeryczny niewymagający diagonalizacji macierzy Hamiltonianu.

Rozwiń \(\mathcal E_N^{\rm R}\) w potęgach \(\lambda\) i sprawdź:

- czy dokładnie odtwarza \(e_N\), \(e_N^{(2)}\) i \(e_N^{(4)}\);
- czy wyznacza kandydat na \(e_N^{(6)}\);
- do którego rzędu współczynnik jest niezależny od jeszcze nieznanych podprzekątnych;
- czy działa zasada stacjonarności ilorazu Rayleigha lub odpowiednik reguły \(2n+1\) dla tej reorganizacji.

Nie zakładaj z góry, że stan zawierający \(Y_2\) daje energię dokładną do \(\lambda^{10}\), \(\lambda^{12}\) ani innego rzędu. Wyprowadź rząd błędu w normie Hilberta lub przez bezpośrednie rozwinięcie.

## 7. Reszta, wariancja i znaczenie wariacyjne

Oblicz

\[
\rho_N=(h-\mathcal E_N^{\rm R})\widetilde\Psi_N,
\qquad
\sigma_N^2
=\frac{\|\rho_N\|^2}{\|\widetilde\Psi_N\|^2}
=\langle h^2\rangle-(\mathcal E_N^{\rm R})^2.
\]

Zbadaj, czy można uzyskać:

- analityczne lub szybko zbieżne wyrażenie na \(\sigma_N\);
- a posteriori oszacowanie odległości od widma;
- oszacowanie błędu energii przy założeniu kontrolowanej luki spektralnej.

Nie nazywaj ilorazu Rayleigha górnym ograniczeniem dla wzbudzonego poziomu \(N>0\) bez dodatkowych warunków min–max i ortogonalności. Dla stanu podstawowego wyraźnie oddziel zwykłe ograniczenie wariacyjne od ostrzejszego oszacowania wymagającego informacji o luce.

Bezpośrednia diagonalizacja macierzy nie może być metodą wyprowadzenia. Jeżeli użyjesz jej wyłącznie jako testu pomocniczego, oznacz to jawnie i sprawdź stabilność względem rozmiaru obcięcia. Preferuj rekurencję Bargmanna, resztę i oszacowania operatorowe.

## 8. Wynik dla manuskryptu

Szczegółowy rachunek umieść w dokumencie audytowym i skryptach. Do manuskryptu dodaj wynik tylko wtedy, gdy uzyskano co najmniej jedno z poniższych:

- jawną reprezentację \(Y_2\) lub \(S_2\);
- nowe, sprawdzone dopasowanie następnego poziomu WKB;
- użyteczne analityczne albo kontrolowane szeregowe wyrażenie na energię Rayleigha;
- wiarygodne oszacowanie reszty.

Nie zwiększaj manuskryptu o więcej niż około pół strony i zachowaj 31 stron, jeśli jest to możliwe przez zastąpienie obecnego tekstu. Nie przedstawiaj lokalnego czynnika wykładniczego jako globalnej funkcji falowej.

## 9. Testy

Dodaj skrypt i testy 11f obejmujące co najmniej:

1. rekurencję \(Y_2\) i jej dolne granice;
2. zgodność z RS dla \(N=0,1\) i kilku \(N\ge2\);
3. bezpośrednią weryfikację reprezentacji całkowej lub funkcji tworzącej;
4. tożsamość między \(Y_2\) i \(S_2\);
5. zachowanie w zerach \(Y_0\);
6. całkowitość odtworzonego stanu addytywnego;
7. zbieżność normy Bargmanna;
8. iloraz Rayleigha i jego rozwinięcie;
9. zgodność znanych współczynników energii;
10. resztę i wariancję;
11. brak regresji etapów 11a–11e.

Uruchom testy etapów 11a–11f, pełny zestaw testów, właściwe skrypty, git diff --check, kompilację LaTeX, kontrolę bibliografii i ostrzeżeń, pdftotext oraz wizualną kontrolę zmienionych stron.

## 10. Obowiązkowe niezależne artefakty

Utwórz:

- prompt_11f_second_subdiagonal_s2_and_rayleigh_energy.diff;
- prompt_11f_second_subdiagonal_s2_and_rayleigh_energy.log.

Plik .diff ma zawierać wyłącznie zmiany 11f względem dokładnego stanu po 11e. Przed edycją wykonaj migawkę wszystkich plików, które zamierzasz zmienić.

Plik .log ma zawierać:

1. początkowy git status --short;
2. pełne równanie i rekurencję \(Y_2\);
3. obsługę \(N=0,1,N\ge2\);
4. reprezentację sumującą \(Y_2\) albo precyzyjnie opisaną przeszkodę;
5. równanie, reprezentację i osobliwości \(S_2\);
6. porównanie z następnym poziomem WKB;
7. konstrukcję globalnie regularnego stanu przybliżonego;
8. dowód lub test jego przynależności do przestrzeni Bargmanna–Focka;
9. wzór na iloraz Rayleigha;
10. jego rozwinięcie perturbacyjne i najwyższy wiarygodny rząd;
11. informację, czy otrzymano kandydat na \(e_N^{(6)}\);
12. normę reszty i wariancję albo precyzyjną przeszkodę;
13. znaczenie wariacyjne dla \(N=0\) oraz \(N>0\);
14. listę zmienionych plików;
15. wyniki testów i kompilacji;
16. liczbę stron przed i po zmianie;
17. końcowy git status --short;
18. końcowy werdykt.

Raport zakończ dokładnie jednym z werdyktów:

- SECOND SUBDIAGONAL SUMMED; S2 AND CONTROLLED RAYLEIGH ENERGY OBTAINED
- SECOND SUBDIAGONAL SUMMED; S2 VERIFIED; RAYLEIGH ENERGY PARTIAL
- Y2 AND S2 REPRESENTATIONS VERIFIED; ENERGY CONTROL REMAINS OPEN
- SECOND SUBDIAGONAL RECURRENCE VERIFIED; CLOSED SUM NOT OBTAINED
- STAGE 11F REVEALS A FAILURE OF THE MULTIPLICATIVE BB ITERATION

## 11. Zasady końcowe

- Nie wykonuj commitów ani pushów.
- Nie ukrywaj rozbieżności między lokalnym \(S_2\) a globalnym stanem addytywnym.
- Nie przedstawiaj obciętej postaci wykładniczej jako całkowitej bez sprawdzenia.
- Nie deklaruj ograniczenia wariacyjnego dla stanu wzbudzonego bez hipotez min–max.
- Nie deklaruj nowego współczynnika energii bez niezależnego sprawdzenia.
- Nie rozpoczynaj jeszcze pełnego etapu \(S_3\).
