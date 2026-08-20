# Prompt 10a — pełna relacja Webera i nietautologiczna redukcja globalna

Pracujesz w repozytorium:

`~/Dokumenty/Prace_i_dnie/Wnęka_z_Kerrem`

na gałęzi `master`.

Etap 10 pozostawił niezatwierdzone zmiany w drzewie roboczym. Zachowaj je i popraw na miejscu. Nie cofaj wcześniejszych zmian i nie rozpoczynaj analizy od nowa.

Nie wykonuj `git commit` ani `git push`.

## Cel

Skoryguj dwa problemy wykryte podczas recenzji etapu 10:

1. macierz \(M_W\) została dopełniona do macierzy unimodularnej bez pełnego wyprowadzenia obu jej wierszy w jawnie określonych bazach;
2. „Minimalny lemat połączeniowy Fedoryuka–Bargmanna” zawierał w założeniach znaczną część poszukiwanego wniosku: wybór orientacji urojonej, postać współczynnika z funkcją gamma, rozwinięcie \(\nu_{\mathrm{eff}}\) oraz równoważność z warunkiem Bargmanna.

Celem 10a nie jest udowodnienie brakującego globalnego twierdzenia. Celem jest uzyskanie matematycznie ścisłej, nietautologicznej redukcji warunkowej.

## 1. Stan początkowy i zakres zmian

Przeczytaj w całości:

- `docs/fedoryuk_global_connection_and_quantization.md`;
- odpowiednią część `manuscript/manuscript.tex`;
- `scripts/10_verify_fedoryuk_global_reduction.py`;
- `tests/test_10_fedoryuk_global_reduction.py`;
- raport i diff etapu 10;
- dokumentację etapów 09c–09e dotyczącą redukcji Webera.

Sprawdź bieżący `git status --short`. Nie usuwaj ani nie nadpisuj niezwiązanych zmian.

W raporcie 10a rozpocznij od krótkiego zestawienia:

- co w etapie 10 było poprawne;
- co wymaga korekty;
- które twierdzenia pozostają lokalne;
- czego nadal nie udowodniono globalnie.

## 2. Jawne bazy rozwiązań Webera

Dla równania

\[
w''(Z)+\left(\nu+\frac12-\frac{Z^2}{4}\right)w(Z)=0
\]

zdefiniuj jawnie dwie uporządkowane bazy rozwiązań, pomiędzy którymi ma działać macierz połączeniowa.

Bazy muszą być określone przez konkretne funkcje, argumenty i normalizacje, na przykład przez odpowiednio wybrane elementy spośród

\[
D_\nu(Z),\qquad D_\nu(-Z),\qquad
D_{-\nu-1}(iZ),\qquad D_{-\nu-1}(-iZ),
\]

ale nie zakładaj z góry, że dowolna para z tej listy jest właściwą bazą w wymaganym sektorze.

Dla każdej bazy podaj:

- kolejność wektorów bazowych;
- sektory, w których odpowiadają rozwiązaniom dominującym i subdominującym;
- przyjęte gałęzie argumentów;
- Wronskian;
- zakres wartości \(\nu\), dla którego para jest liniowo niezależna;
- zachowanie w granicy \(\nu\to n\in\mathbb N_0\).

Jeżeli wybrana baza degeneruje się przy \(\nu=n\), zastosuj normalizację analityczną w \(\nu\) albo wyraźnie oddziel macierz dla ogólnego \(\nu\) od granicznego warunku \(c_W(n)=0\).

## 3. Pełne wyprowadzenie relacji połączeniowej

Rozpocznij od dokładnych wzorów DLMF, w szczególności 12.2.17–12.2.20, oraz relacji

\[
D_\nu(Z)=U\!\left(-\nu-\frac12,Z\right).
\]

Nie wyprowadzaj macierzy \(2\times2\) z pojedynczej relacji skalarnej.

Wykonaj kolejno:

1. wyprowadzenie pierwszej relacji pomiędzy wybranymi rozwiązaniami;
2. wyprowadzenie niezależnej drugiej relacji;
3. zapis obu relacji w jednej ustalonej konwencji macierzowej;
4. obliczenie macierzy odwrotnej;
5. bezpośrednie sprawdzenie iloczynu obu macierzy;
6. sprawdzenie wyznacznika za pomocą stosunku Wronskianów.

Każdy współczynnik fazowy ma wynikać jawnie z wybranego znaku we wzorze DLMF i podstawienia \(a=-\nu-\tfrac12\).

Nie narzucaj \(\det M_W=1\) przez arbitralne dobranie drugiego elementu diagonalnego. Jeżeli po naturalnym wyborze baz wyznacznik nie wynosi jeden, podaj jego poprawną wartość. Następnie możesz, opcjonalnie, wprowadzić bazy Wronskianowo znormalizowane i wykazać, że odpowiadająca im macierz jest unimodularna.

Jeżeli pełna macierz nie jest potrzebna do lokalnego warunku

\[
c_W(\nu)=
\frac{\sqrt{2\pi}\,e^{-i\pi(\nu+1)/2}}{\Gamma(-\nu)},
\qquad c_W(n)=0,
\]

napisz to wprost. Nie przedstawiaj wygodnego algebraicznego dopełnienia jako dokładnej macierzy połączeniowej.

## 4. Niezależna weryfikacja macierzy

Rozbuduj skrypt etapu 10 tak, aby testował rzeczywiste tożsamości funkcyjne, a nie tylko własności macierzy zdefiniowanej w tym samym skrypcie.

Weryfikacja ma obejmować:

- symboliczne sprawdzenie współczynników wynikających ze wzorów DLMF;
- sprawdzenie Wronskianów;
- sprawdzenie macierzy odwrotnej;
- numeryczne sprawdzenie obu relacji funkcyjnych dla kilku niecałkowitych wartości \(\nu\) i kilku zespolonych wartości \(Z\);
- sprawdzenie stabilności przy \(\nu\) zbliżającym się do \(n=0,1,2,\ldots\);
- potwierdzenie, że zera \(1/\Gamma(-\nu)\) są proste;
- wyraźne odróżnienie zera modelowego współczynnika Webera od globalnego warunku spektralnego.

Użyj wystarczającej precyzji arytmetycznej i podaj tolerancje. Test nie może sprowadzać się do sprawdzenia wyznacznika macierzy skonstruowanej z założonym odwrotnym elementem diagonalnym.

## 5. Rozdzielenie brakującej hipotezy od jej konsekwencji

Usuń lub zastąp dotychczasową „Minimal Fedoryuk–Bargmann connection lemma”.

Nie nazywaj hipotezy lematem, skoro nie została udowodniona. Użyj nazwy:

**Global Fedoryuk–Bargmann connection hypothesis**

albo równoważnej, jednoznacznie warunkowej nazwy.

Rozbij dotychczasową hipotezę na trzy logiczne poziomy.

### H1. Hipoteza geometryczno-transportowa

H1 może zakładać wyłącznie:

- istnienie skończonego łańcucha odpowiednich domen kanonicznych;
- uniformność liczby domen i stałych na nakładkach;
- istnienie dróg progresywnych;
- kontrolowane przejścia WKB–Weber i, jeżeli potrzebne, WKB–Airy;
- kontrolę przejścia przy biegunie;
- zgodność arkuszy oraz realizację wymaganej monodromii;
- identyfikację początkowego rozwiązania z cechowanym analitycznym zarodkiem Bargmanna.

H1 nie może z góry wskazywać:

- pary Webera na osi urojonej;
- zera \(1/\Gamma(-\nu)\);
- wartości \(e_{1,n}\) ani \(e_{2,n}\);
- postaci energii;
- równoważności z warunkiem entireness.

### H2. Hipoteza skalarnej redukcji końcowej

Jeżeli sama H1 nie wystarcza do otrzymania jednego współczynnika skalarnego, sformułuj osobno minimalne H2.

H2 może zakładać, że po wykonaniu transportu warunek zaniku niedopuszczalnego rozwiązania przy końcu łańcucha jest zadany przez jeden element, minor albo wyznacznik globalnej macierzy transferu, z kontrolowaną resztą.

H2 nie może zakładać z góry, że tym skalarem jest

\[
\Gamma(-\nu_{\mathrm{eff}})^{-1}+O(\varepsilon^3).
\]

Zbadaj natomiast, co wynika z ogólnego iloczynu macierzy. W szczególności sprawdź, czy nieznane macierze otaczające \(M_W\) mogą mieszać jego elementy w taki sposób, że zero \(c_W(n)=0\) przestaje być zerem końcowego współczynnika.

To jest kluczowy test nietautologiczności.

### Wniosek warunkowy

Dopiero po H1 i ewentualnej H2 wyprowadź:

- jaki dodatkowy warunek strukturalny na macierze otaczające \(M_W\) jest potrzebny, aby globalny skalar faktoryzował się przez \(c_W(\nu)\);
- czy ten warunek jest konsekwencją geometrii i dominacji/subdominacji, czy osobną hipotezą;
- kiedy z globalnego warunku wynika wybór orientacji urojonej;
- kiedy można zastosować twierdzenie o funkcji uwikłanej albo twierdzenie Rouchégo;
- które współczynniki energii są wtedy konsekwencją lokalnej analizy Webera.

Nie umieszczaj rozwinięcia energii w założeniach hipotezy, której ma ono być wnioskiem.

## 6. Algebra ogólnej macierzy globalnej

Dla schematu

\[
M_{\mathrm{glob}}
=
B_{\mathrm{out}}
M_A^{\chi_A}
B_2M_WB_1G_0
\]

wykonaj symboliczną analizę z ogólnymi odwracalnymi macierzami \(B_1,B_2,B_{\mathrm{out}},G_0\).

Ustal:

1. który element, minor lub iloczyn z wektorami brzegowymi reprezentuje fizyczny współczynnik niedopuszczalnej gałęzi;
2. jak zależy on od wszystkich czterech elementów \(M_W\);
3. jakie warunki zerowania albo trójkątności macierzy zewnętrznych są konieczne, aby był proporcjonalny do \(c_W(\nu)\);
4. czy warunki te można uzasadnić samą dominacją sektorową;
5. czy nieznane przejście Airy’ego może przesunąć albo usunąć zero Webera.

Jeżeli dla ogólnych macierzy zewnętrznych \(c_W(n)=0\) nie implikuje globalnego warunku spektralnego, pokaż to jawnie, najlepiej przez prosty kontrprzykład macierzowy.

Nie określaj faktoryzacji jako „unambiguous”, dopóki drogi, bazy i macierze przejścia nie zostaną ustalone.

## 7. Poprawiony status wyniku

Na podstawie powyższej analizy wybierz jeden z werdyktów:

- `FULL WEBER MATRIX DERIVED; GLOBAL REDUCTION REMAINS CONDITIONAL`;
- `SCALAR WEBER RELATION SUFFICIENT; GLOBAL REDUCTION REMAINS CONDITIONAL`;
- `GLOBAL REDUCTION REQUIRES AN ADDITIONAL STRUCTURAL HYPOTHESIS`;
- `STAGE 10 CONDITIONAL CLAIM MUST BE WEAKENED`.

Nie wolno użyć werdyktu `GLOBAL CONNECTION PROVED`.

W dokumentacji i manuskrypcie rozróżnij:

- dokładną tożsamość funkcyjną Webera;
- pełną macierz pomiędzy jawnie określonymi bazami;
- lokalne zero współczynnika Webera;
- hipotezę istnienia globalnego łańcucha;
- hipotezę zachowania trójkątnej lub faktoryzującej struktury podczas transportu;
- dokładny warunek Bargmanna \(\Delta_{\mathrm{WI}}=0\);
- warunkową zgodność rozwinięcia energii.

## 8. Zmiany w plikach

Popraw na miejscu:

- `docs/fedoryuk_global_connection_and_quantization.md`;
- `manuscript/manuscript.tex`;
- `scripts/10_verify_fedoryuk_global_reduction.py`;
- `tests/test_10_fedoryuk_global_reduction.py`;
- w razie potrzeby inne pliki utworzone w etapie 10.

Nie twórz nowej dużej sekcji manuskryptu. Korekta powinna raczej skrócić i wyostrzyć istniejący tekst.

Zapisz bieżący prompt jako:

- `prompts/prompt_10a_correct_weber_matrix_and_global_hypothesis.md`.

Utwórz:

- `prompt_10a_correct_weber_matrix_and_global_hypothesis.diff`;
- `prompt_10a_correct_weber_matrix_and_global_hypothesis.log`.

Diff 10a ma dokumentować wyłącznie zmiany względem stanu pozostawionego przez etap 10, a nie cały skumulowany diff od ostatniego commita. Jeżeli wymaga to zapisania stanu początkowego w plikach tymczasowych poza repozytorium, zrób to bez modyfikowania historii Git.

## 9. Kontrola końcowa

Uruchom:

- pełny zestaw testów;
- testy skupione na etapach 09–10a;
- wszystkie właściwe skrypty weryfikacyjne etapów 08–10a;
- `git diff --check`;
- pełną kompilację LaTeX z bibliografią;
- kontrolę niezdefiniowanych cytowań i odwołań;
- kontrolę `Overfull` i `Underfull`;
- renderowanie i wizualną inspekcję wszystkich stron zmienionych przez 10a.

Sprawdź bajtową zgodność kanonicznego i wynikowego PDF-u, jeżeli projekt utrzymuje obie kopie.

## 10. Raport

Raport 10a ma zawierać:

1. końcowy werdykt;
2. jawne definicje obu baz Webera;
3. pełne dwie relacje połączeniowe albo uzasadnienie, dlaczego pozostawiono wyłącznie relację skalarną;
4. macierz, macierz odwrotną, Wronskiany i zakres ważności;
5. wyniki niezależnych testów numerycznych tożsamości funkcyjnych;
6. dokładną treść H1 i ewentualnej H2;
7. analizę ogólnego iloczynu macierzy globalnej;
8. wskazanie, czy i pod jakim dodatkowym warunkiem globalny skalar zawiera czynnik \(1/\Gamma(-\nu)\);
9. status każdego współczynnika energii;
10. wykaz zmienionych plików;
11. wyniki testów i kompilacji;
12. `git status --short`.

Nie wykonuj commitów ani pushów.
