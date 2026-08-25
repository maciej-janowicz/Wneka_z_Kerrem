# Prompt 11a — sumowanie Bendera–Bettencourta w przybliżeniu silnego Kerra

Pracujesz w repozytorium `~/Dokumenty/Prace_i_dnie/Wnęka_z_Kerrem`, na gałęzi `master`, zsynchronizowanej z `origin/master`. W głównym katalogu projektu znajduje się artykuł Bendera i Bettencourta: `BB.pdf`.

Nie wykonuj `git commit` ani `git push`.

## Cel

Przeczytaj uważnie i w całości sekcje IV i V artykułu `BB.pdf`. Zrekonstruuj zastosowaną tam metodę przegrupowania i sumowania szeregu perturbacyjnego dla energii oraz funkcji falowej oscylatora anharmonicznego, a następnie przeprowadź analogiczny rachunek dla wzbudzanego modu we wnęce Kerra w reżimie

\[
\lambda:=\frac{|F|}{V}\ll1.
\]

Jest to przybliżenie silnego Kerra albo silnego sprzężenia nieliniowego względem wzbudzenia, równoważnie rachunek słabego wzbudzenia. Nie myl go z analizą silnego wzbudzenia \(\eta=|F|/V\gg1\) z wcześniejszych sekcji Olvera i Fedoryuka.

Kluczowe wymagania:

- wyraz proporcjonalny do \(z\,d/dz\) ma należeć do Hamiltonianu zerowego;
- zerowa funkcja własna ma być jednomianem \(\Psi_N^{(0)}(z)=z^N/\sqrt{N!}\), \(N\in\mathbb N_0\), albo \(z^N\) w nienormalizowanej konwencji Bargmanna;
- rozróżnij formalny szereg perturbacyjny od jego BB-owskiego przegrupowania lub sumowania;
- nie zakładaj z góry, że wynik musi być funkcją Webera.

## 1. Audyt artykułu Bendera–Bettencourta

Przeczytaj sekcje IV i V `BB.pdf` bez polegania na streszczeniach wtórnych. Podaj:

1. pełne dane bibliograficzne artykułu;
2. tytuły i zakres sekcji IV i V;
3. równanie i Hamiltonian analizowane przez autorów;
4. parametr perturbacyjny i skalowanie;
5. zwykłe rozwinięcia energii i funkcji falowej;
6. organizację wielomianów w kolejnych rzędach;
7. dokładny mechanizm sumowania lub przegrupowania;
8. sposób wyłonienia struktury wykładniczej;
9. związek wyniku z rozwinięciem WKB;
10. rolę metody wielu skal, jeżeli sekcje IV–V się do niej odwołują.

Wyraźnie oddziel zwykłą teorię perturbacji, wzorzec wyrazów dominujących, częściowe sumowanie nieskończonej rodziny wyrazów, wynik asymptotyczny oraz porównanie z WKB. Cytuj numery równań i strony PDF-u, ale nie przytaczaj długich fragmentów.

Jeżeli `BB.pdf` nie jest właściwym artykułem albo sekcje IV–V mają inną zawartość, zatrzymaj zmiany merytoryczne, opisz rozbieżność i nie dopasowuj obcego rachunku na siłę.

## 2. Hamiltonian zerowy dla wnęki Kerra

Zacznij od Hamiltonianu z zachowaniem czynnika \(V/2\):

\[
H=\frac{V}{2}a^{\dagger2}a^2+\hbar\omega_0a^\dagger a+Fa^\dagger+F^*a.
\]

W reprezentacji Bargmanna:

\[
H=\frac{V}{2}z^2\frac{d^2}{dz^2}+\hbar\omega_0z\frac{d}{dz}+Fz+F^*\frac{d}{dz}.
\]

Wprowadź

\[
\delta=\frac{\hbar\omega_0}{V},\qquad f=\frac FV,\qquad
\lambda=|f|=\frac{|F|}{V}
\]

i podziel Hamiltonian przez \(V\):

\[
h:=\frac HV=h_0+h_1,
\]

\[
h_0=\frac12z^2\frac{d^2}{dz^2}+\delta z\frac{d}{dz},
\qquad h_1=fz+f^*\frac{d}{dz}.
\]

Wyraz \(\delta z\,d/dz\) należy w całości do \(h_0\). Po obrocie fazy można przyjąć \(f=\lambda>0\), ale podaj sposób odtworzenia wyniku dla zespolonego \(F\).

## 3. Problem zerowego rzędu

Zweryfikuj

\[
\Psi_N^{(0)}(z)=\frac{z^N}{\sqrt{N!}},\qquad
\epsilon_N^{(0)}:=\frac{E_N^{(0)}}V=\frac12N(N-1)+\delta N.
\]

Podaj warunki niedegeneracji. W szczególności:

\[
\epsilon_N^{(0)}-\epsilon_{N-1}^{(0)}=N-1+\delta,
\qquad
\epsilon_N^{(0)}-\epsilon_{N+1}^{(0)}=-(N+\delta).
\]

Zidentyfikuj rezonansowe wartości \(\delta\), dla których rachunek niedegenerowany przestaje obowiązywać. Osobno potraktuj \(N=0\). Nie dziel przez zerujące się mianowniki; teorię zdegenerowaną jedynie zasygnalizuj.

## 4. Zwykły rachunek perturbacyjny

Przeprowadź niezależnie teorię Rayleigha–Schrödingera dla ustalonego \(N\), przy pośredniej normalizacji \(\langle N|\Psi_N\rangle=1\), używając

\[
a^\dagger|n\rangle=\sqrt{n+1}|n+1\rangle,
\qquad a|n\rangle=\sqrt n|n-1\rangle.
\]

Wyznacz co najmniej:

- energię do rzędu \(\lambda^4\);
- funkcję własną do rzędu \(\lambda^3\), a jeśli rachunek jest stabilny — do \(\lambda^4\);
- wszystkie współczynniki w bazie jednomianów Bargmanna;
- reguły parzystości rzędów energii;
- maksymalny zakres indeksów w każdym rzędzie funkcji falowej.

Wyprowadź z elementów macierzowych znikanie poprawki pierwszego rzędu oraz

\[
\epsilon_N^{(2)}=\lambda^2\left[
\frac{N}{N-1+\delta}-\frac{N+1}{N+\delta}
\right].
\]

Uprość współczynnik, sprawdź jego znak i przypadek \(N=0\). Porównaj wyniki z: (1) ortonormalnej bazy Focka, (2) równania Bargmanna, (3) dokładnej rekurencji współczynników. Wszystkie trzy rachunki muszą być zgodne po uwzględnieniu normalizacji.

## 5. Dokładna rekurencja Bargmanna

Dla

\[
\Psi(z)=\sum_{n=0}^{\infty}c_n\frac{z^n}{\sqrt{n!}}
\]

wyprowadź dokładną trójdiagonalną rekurencję z \(h\Psi=\epsilon\Psi\), zarówno dla zespolonego \(f\), jak i po obrocie fazy \(f=\lambda>0\).

Następnie:

- rozwiń \(c_n\) i \(\epsilon\) w potęgach \(\lambda\);
- odtwórz współczynniki Rayleigha–Schrödingera;
- sprawdź, jak daleko od \(n=N\) sięga rząd \(k\);
- ustal, które rodziny skrajnych współczynników mogą być sumowane analogicznie do BB.

## 6. Analog sumowania Bendera–Bettencourta

Zastosuj rzeczywistą metodę z sekcji IV–V `BB.pdf`, a nie ogólną sugestię „wykładniczmy szereg”. Rozważ co najmniej

\[
\Psi_N(z;\lambda)=\frac{z^N}{\sqrt{N!}}
\left[1+\lambda P_{N,1}(z)+\lambda^2P_{N,2}(z)+\cdots\right]
\]

oraz, na domenie wykluczającej zero,

\[
\Psi_N(z;\lambda)=\frac{z^N}{\sqrt{N!}}
\exp\!\left[\lambda S_{N,1}(z)+\lambda^2S_{N,2}(z)
+\lambda^3S_{N,3}(z)+\cdots\right].
\]

Ponieważ poprawki zawierają stany o indeksach mniejszych niż \(N\), iloraz \(\Psi_N/z^N\) może zawierać ujemne potęgi \(z\). Traktuj logarytm wyłącznie lokalnie na domenie z ustaloną gałęzią. Nie przedstawiaj jego czynników jako całkowitych funkcji Bargmanna.

Ustal:

1. najwyższe i najniższe potęgi \(z\) w \(P_{N,k}\);
2. czy skrajne współczynniki tworzą szeregi dające się zsumować;
3. czy powstaje wykładnik zawierający \(z\), \(1/z\), logarytm lub inną strukturę;
4. jak pozorne bieguny w \(\Psi_N/z^N\) znoszą się w pełnej funkcji całkowitej;
5. dla jakiego zakresu \(z\) reorganizacja poprawia przybliżenie;
6. jaki złożony parametr skalowany powinien pozostać \(O(1)\), analogicznie do BB;
7. czy suma prowadzi do znanej funkcji specjalnej.

Nie zakładaj funkcji Webera. Jeżeli wynika inna funkcja specjalna, wyprowadź jej równanie i parametry; nie identyfikuj jej na podstawie kilku współczynników.

## 7. Związek z WKB i wcześniejszymi sekcjami

Zbadaj, czy sumowanie BB dla \(\lambda\ll1\):

- odtwarza lokalne zachowanie WKB dokładnego równania Bargmanna;
- opisuje inną dziedzinę niż analiza \(\eta\gg1\);
- ma obszar nakładania z Olverem lub Fedoryukiem;
- może prowadzić do Webera po dodatkowym skalowaniu przy zlewających się punktach zwrotnych;
- czy pozostaje rozwinięciem słabowzbudzeniowym wokół \(z^N\).

Oddziel bezpośredni wynik, formalne sumowanie podrodziny wyrazów, domniemany obszar ważności, porównanie strukturalne z BB i ewentualną hipotezę o Weberze. Nie przenoś wyników \(\eta\gg1\) do \(\lambda\ll1\) bez wykazania wspólnego skalowania.

## 8. Weryfikacja symboliczna i numeryczna

Utwórz skrypt, który:

- generuje współczynniki dla symbolicznego \(N,\delta\), o ile to wykonalne;
- sprawdza rzędy do \(\lambda^4\);
- porównuje rachunek operatorowy z rekurencją Bargmanna;
- weryfikuje energię drugiego i czwartego rzędu;
- sprawdza resztę równania dla przybliżonej funkcji falowej;
- testuje kilka niedegenerowanych wartości \(N,\delta\);
- porównuje szereg surowy i przegrupowany dla małego \(\lambda\);
- nie używa diagonalizacji jako metody wyprowadzenia.

Mała macierz obcięta jest dopuszczalna tylko jako niezależny test numeryczny, ze sprawdzeniem stabilności względem obcięcia. Dodaj testy regresyjne; wszystkie wcześniejsze testy muszą przechodzić.

## 9. Dokumentacja i manuskrypt

Utwórz:

- `docs/bender_bettencourt_weak_drive_resummation.md`;
- odpowiedni skrypt weryfikacyjny;
- odpowiednie testy.

Dodaj do manuskryptu zwięzłą sekcję po analizie Fedoryuka. Ma ona:

- wyjaśniać reżim \(|F|/V\ll1\);
- definiować \(h_0\) wraz z \(\delta z\,d/dz\);
- podawać jednomianową funkcję zerowego rzędu;
- przedstawiać zweryfikowane poprawki energii i funkcji falowej;
- wyjaśniać analogię i różnicę względem BB;
- podawać tylko rzeczywiście uzyskane sumowanie i jego obszar ważności;
- nie sugerować globalnego twierdzenia WKB ani pojawienia się Webera bez dowodu.

Nie zmieniaj wyników Olvera i Fedoryuka poza minimalnymi odsyłaczami porównawczymi.

## 10. Kontrola końcowa

Uruchom:

- pełny zestaw testów i nowe testy 11a;
- właściwe skrypty etapów 08–10;
- `git diff --check`;
- pełną kompilację LaTeX z bibliografią;
- kontrolę niezdefiniowanych cytowań, odwołań, `Overfull` i `Underfull`;
- renderowanie i wizualną inspekcję wszystkich zmienionych stron;
- sprawdzenie zgodności kanonicznej i wynikowej kopii PDF-u.

## 11. Artefakty

Zapisz prompt jako:

- `prompts/prompt_11a_bender_bettencourt_weak_drive_resummation.md`.

Utwórz:

- `prompt_11a_bender_bettencourt_weak_drive_resummation.diff`;
- `prompt_11a_bender_bettencourt_weak_drive_resummation.log`.

Raport `.log` ma zawierać:

1. identyfikację artykułu i streszczenie sekcji IV–V;
2. definicję rachunku zerowego;
3. warunki niedegeneracji;
4. energię przez rząd \(\lambda^4\);
5. funkcję falową przez osiągnięty rząd;
6. dokładną rekurencję Bargmanna;
7. opis sumowania BB;
8. obszar jego ważności;
9. odpowiedź, czy pojawia się Weber albo inna funkcja specjalna;
10. porównanie z WKB, Olverem i Fedoryukiem;
11. wykaz zmienionych plików;
12. wyniki testów i kompilacji;
13. początkowy i końcowy `git status --short`.

Nie wykonuj commitów ani pushów.
