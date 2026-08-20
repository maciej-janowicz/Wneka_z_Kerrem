# Prompt 10b — przywrócenie pełnego audytu globalnego bez regresji matematycznej

Pracujesz w repozytorium:

`~/Dokumenty/Prace_i_dnie/Wnęka_z_Kerrem`

na gałęzi `master`.

Etapy 10 i 10a pozostawiły niezatwierdzone zmiany w drzewie roboczym. Zachowaj je i popraw na miejscu. Nie wykonuj `git commit` ani `git push`.

## Cel

Etap 10a poprawnie:

- wyprowadził pełną macierz Webera z dwóch niezależnych relacji funkcyjnych;
- wykazał \(M_W^{-1}=M_W\) oraz \(\det M_W=-1\) dla jawnie określonych baz;
- zastąpił tautologiczną „minimalną hipotezę” rozdzieleniem na H1, H2 i dodatkową hipotezę strukturalną H3;
- wykazał, że lokalne zero \(c_W(n)=0\) nie jest na ogół zerem globalnego współczynnika;
- pozostawił globalne połączenie i fizyczny wybór orientacji jako problemy otwarte.

Tych wyników nie wolno cofnąć ani osłabić.

Jednocześnie podczas skracania pliku

`docs/fedoryuk_global_connection_and_quantization.md`

usunięto poprawne i użyteczne części audytu etapu 10, w szczególności:

- dokładne dane normalnej postaci Fedoryuka i skalowania;
- audyt źródłowy książki Fedoryuka;
- tabelę hipotez stosowalności;
- opis powierzchni pędu, arkuszy, cięć i kandydackiej geometrii globalnej;
- inwentarz potrzebnych domen WKB, Webera, Airy’ego i sektorów przy biegunie;
- listę brakujących elementów globalnego dowodu;
- realistyczny szkic dalszej drogi dowodowej.

Celem 10b jest przywrócenie tych poprawnych informacji, bez przywracania błędnej macierzy z etapu 10 ani tautologicznego „minimalnego lematu”. Jest to korekta dokumentacyjna i redakcyjna, nie nowa próba udowodnienia globalnego twierdzenia.

## 1. Audyt stanu początkowego

Przeczytaj w całości:

- `docs/fedoryuk_global_connection_and_quantization.md` w stanie po 10a;
- `manuscript/manuscript.tex`;
- raporty i diffy etapów 10 oraz 10a;
- `docs/fedoryuk_applicability_and_geometry.md`;
- `docs/fedoryuk_weber_wavefunction_and_energy.md`;
- skrypt i testy etapu 10a.

Sprawdź `git status --short`. Nie zmieniaj niezwiązanych plików.

Porównaj dokument pomocniczy po 10a z wersją pozostawioną przez etap 10. Sporządź listę fragmentów:

1. poprawnych i wymagających przywrócenia;
2. błędnych lub zbyt mocnych i niewymagających przywrócenia;
3. zastąpionych poprawniejszą treścią w 10a.

## 2. Treści, które należy przywrócić

Rozbuduj `docs/fedoryuk_global_connection_and_quantization.md`, przywracając — po ponownej kontroli — następujące elementy.

### 2.1. Dane wyjściowe

Zapisz w jednym miejscu:

\[
\Psi=z^{-\delta}e^{\eta/z}u,
\qquad
\varepsilon^2u_{yy}=(Q_0+\varepsilon Q_1+\varepsilon^2Q_2)u,
\]

\[
Q_0=\frac{P(y;e)}{y^4},\qquad
Q_1=\frac{2(\delta-1)}{y^3},\qquad
Q_2=\frac{\delta(\delta-1)}{y^2},
\]

wraz z definicjami \(y,\varepsilon,\eta,\delta,e\), wielomianem

\[
P(y;e)=1+2ey^2-2y^3
\]

oraz położeniami i rozwinięciami punktów zwrotnych w pobliżu \(e=-3/2\).

Nie powtarzaj zbędnie długich rachunków dostępnych w innych dokumentach; podaj jednak komplet danych potrzebnych do samodzielnego odczytania audytu globalnego.

### 2.2. Audyt źródłowy Fedoryuka

Przywróć dokładne dane bibliograficzne i kontrolowaną informację o odpowiednich częściach książki Fedoryuka:

- rozdział III, sekcje dotyczące oszacowań WKB w płaszczyźnie zespolonej oraz współczynników całkowitych lub meromorficznych;
- rozdział IV, sekcje dotyczące prostych, wielokrotnych i dwóch bliskich punktów zwrotnych.

Nie wymyślaj numerów twierdzeń ani tez, których nie udało się sprawdzić. Wyraźnie oddziel:

- informacje potwierdzone w dostępnym źródle;
- wierną ograniczoną parafrazę;
- zakres, którego źródło nie pokrywa albo którego nie udało się potwierdzić.

### 2.3. Tabela stosowalności

Przywróć tabelę w formacie:

`hipoteza | weryfikacja dla problemu Kerra | status`.

Powinna ona obejmować co najmniej:

- duży parametr;
- meromorficzność współczynników;
- lokalne niezerowanie \(Q_0\);
- jednoznaczność pędu i działania na domenie z cięciami;
- prosty punkt zwrotny;
- parę bliskich punktów zwrotnych;
- lokalną analityczność przy parze;
- drogi progresywne;
- skończony globalny łańcuch domen;
- przejście przy biegunie czwartego rzędu;
- jednolite oszacowania na nakładkach;
- monodromię arkuszy i cechowania;
- identyfikację z całkowitym zarodkiem Bargmanna;
- hipotezę strukturalnej faktoryzacji H3.

Statusy muszą odpowiadać wynikowi 10a. W szczególności H3 pozostaje nieudowodniona.

### 2.4. Powierzchnia pędu i geometria kandydacka

Przywróć opis

\[
\mathcal R_e=\{(y,w):w^2=P(y;e)\},
\qquad p=w/y^2,
\]

wraz z:

- liczbą arkuszy i punktami rozgałęzienia;
- zachowaniem przy zlewaniu dwóch punktów zwrotnych;
- statusem bieguna \(y=0\);
- koniecznością wyboru cięć i gałęzi działania;
- konwencją linii Stokesa i anty-Stokesa;
- rolą separatrys;
- ostrożnym opisem kandydackiego łańcucha domen.

Nie przedstawiaj numerycznie śledzonych krzywych jako dowodu globalnej łączności.

### 2.5. Inwentarz brakujących elementów

Zapisz wyraźnie, że nie udowodniono:

- istnienia globalnego łańcucha H1;
- uniformności dróg progresywnych i nakładek;
- kontrolowanego przejścia przy biegunie;
- konieczności lub zbędności przejścia Airy’ego;
- pełnej realizacji monodromii;
- identyfikacji końcowego skalara z dokładnym warunkiem \(\Delta_{\mathrm{WI}}=0\);
- strukturalnej faktoryzacji H3;
- wyboru orientacji urojonej przez rzeczywistą drogę globalną.

Nie wolno sugerować, że H1 albo H2 implikuje H3.

### 2.6. Realistyczna droga dalszego dowodu

Przywróć krótki, konkretny program dalszej pracy:

1. skonstruowanie krytycznego grafu na powierzchni pędu;
2. wskazanie fizycznego cyklu kontynuacji;
3. pokrycie go skończoną rodziną domen o kontrolowanych nakładkach;
4. uzyskanie oszacowań Volterry przy skompensowanym końcu biegunowym;
5. wstawienie parametryksów Webera i ewentualnie Airy’ego;
6. transport baz z kontrolą Wronskianów, arkuszy i logarytmu;
7. obliczenie rzeczywistych wektorów brzegowych \(\ell,r\);
8. sprawdzenie albo obalenie warunku H3;
9. dopiero potem porównanie globalnego skalara z \(\Delta_{\mathrm{WI}}\) i zastosowanie argumentu Rouchégo.

Program ten ma być przedstawiony jako plan dowodu, nie jako dowód wykonany.

## 3. Treści, których nie wolno przywrócić

Nie przywracaj:

- sztucznie dopełnionej trójkątnej macierzy o wyznaczniku jeden;
- twierdzenia, że pojedyncza relacja DLMF wyznacza pełną macierz;
- określenia faktoryzacji globalnej jako „unambiguous”;
- dawnego „Minimal Fedoryuk–Bargmann connection lemma”;
- hipotezy zawierającej z góry orientację urojoną;
- hipotezy zawierającej z góry czynnik \(1/\Gamma(-\nu_{\mathrm{eff}})\), rozwinięcie energii albo równoważność z entireness;
- twierdzenia, że \(c_W(n)=0\) jest samo przez się globalnym warunkiem spektralnym;
- przypisania wyrazu \(K_n(\delta)\eta^{-2/3}\) analizie Fedoryuka.

Zachowaj pełną macierz 10a:

\[
M_W=
\begin{pmatrix}
e^{i\pi\nu}&-e^{i\pi\nu}c_W\\
d_W&-e^{i\pi\nu}
\end{pmatrix},
\qquad
M_W^{-1}=M_W,
\qquad
\det M_W=-1,
\]

oraz analizę ogólnej kontrakcji \(\ell^TM_Wr\).

## 4. Zgodność z manuskryptem

Sprawdź zdanie w `manuscript/manuscript.tex`, według którego pełne hipotezy i proponowana droga dowodu znajdują się w dokumencie pomocniczym.

Po zmianach zdanie to musi być literalnie prawdziwe. Jeżeli przywrócony dokument zawiera rzeczywiście pełny audyt i program dowodu, pozostaw zdanie bez zmian. W przeciwnym razie popraw je w sposób minimalny.

Nie rozbudowuj sekcji manuskryptu. Nie zmieniaj wzorów, statusu H1–H3 ani rozwinięcia energii, chyba że znajdziesz konkretną niespójność wymagającą korekty. Każdą taką korektę opisz osobno w raporcie.

## 5. Testy i kontrola regresji

Ponieważ 10b jest głównie zmianą dokumentacyjną:

- nie twórz nowych skryptów matematycznych bez rzeczywistej potrzeby;
- nie osłabiaj testów 10a;
- uruchom pełny zestaw testów;
- uruchom skrypt weryfikacyjny 10a;
- uruchom właściwe skrypty etapów 08–09;
- wykonaj `git diff --check`;
- skompiluj pełny manuskrypt z bibliografią;
- sprawdź niezdefiniowane cytowania i odwołania oraz `Overfull` i `Underfull`;
- wyrenderuj i obejrzyj strony zmienione przez 10b;
- sprawdź zgodność kanonicznej i wynikowej kopii PDF-u.

Sprawdź także automatycznie, że dokument pomocniczy zawiera:

- nagłówki audytu źródłowego, tabeli stosowalności, geometrii globalnej, brakujących kroków i programu dowodu;
- symbole H1, H2 i H3;
- poprawne \(\det M_W=-1\);
- ostrzeżenie, że \(c_W(n)=0\) nie jest samodzielnym warunkiem spektralnym;
- brak starego sformułowania „Minimal Fedoryuk–Bargmann connection lemma”.

## 6. Artefakty 10b

Zapisz prompt jako:

- `prompts/prompt_10b_restore_global_audit_without_regression.md`.

Utwórz nowe, odrębne artefakty:

- `prompt_10b_restore_global_audit_without_regression.diff`;
- `prompt_10b_restore_global_audit_without_regression.log`.

Plik `.diff` ma zawierać wyłącznie zmiany wykonane przez 10b względem stanu pozostawionego przez 10a, a nie cały skumulowany diff etapów 10–10b. W razie potrzeby zapisz stan początkowy w katalogu tymczasowym poza repozytorium. Nie modyfikuj historii Git.

Plik `.log` ma zawierać:

1. streszczenie wykonanej korekty;
2. listę przywróconych poprawnych fragmentów;
3. listę fragmentów celowo nieprzywróconych;
4. potwierdzenie zachowania pełnej macierzy Webera z 10a;
5. potwierdzenie zachowania struktury H1–H3;
6. ocenę zgodności dokumentu pomocniczego z obietnicą manuskryptu;
7. wykaz zmienionych plików;
8. wyniki testów, kompilacji i kontroli wizualnej;
9. początkowy i końcowy `git status --short`.

## 7. Werdykt końcowy

Raport zakończ jednym z werdyktów:

- `GLOBAL AUDIT RESTORED WITHOUT MATHEMATICAL REGRESSION`;
- `GLOBAL AUDIT PARTIALLY RESTORED — FURTHER EDIT NEEDED`;
- `MATHEMATICAL REGRESSION DETECTED — DO NOT COMMIT`.

Nie wykonuj commitów ani pushów.
