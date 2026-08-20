# Prompt 10 — globalne połączenie Fedoryuka i warunek kwantyzacji

Pracujesz w repozytorium:

`~/Dokumenty/Prace_i_dnie/Wnęka_z_Kerrem`

na gałęzi `master`, zsynchronizowanej z `origin/master`.

Nie wykonuj `git commit` ani `git push`.

## Cel

Dokończ analizę Fedoryuka dla silnie wzbudzanego oscylatora Kerra. Zbadaj, czy można zbudować kontrolowany globalny łańcuch kontynuacji od rozwiązania Bargmanna analitycznego przy \(z=0\), poprzez krytyczną parę punktów zwrotnych opisaną lokalnie funkcjami Webera, aż do odpowiednich sektorów przy nieskończoności, i na tej podstawie wyprowadzić asymptotyczny warunek kwantyzacji.

Nie zakładaj z góry, że takie domknięcie jest możliwe na podstawie już przywołanych twierdzeń Fedoryuka. Wynik ma przyjąć jedną z dwóch postaci:

1. **Twierdzenie warunkowe lub bezwarunkowe o połączeniu**, jeżeli wszystkie hipotezy właściwego twierdzenia Fedoryuka można jawnie zweryfikować; albo
2. **Precyzyjne twierdzenie redukcyjne**, wskazujące jeden minimalny brakujący lemat globalny oraz pokazujące, że z tego lematu wynika warunek kwantyzacji i wybór właściwej gałęzi energii.

Nie wolno zastępować brakującego argumentu określeniami typu „standard matching”, „usual continuation” lub „by Fedoryuk theory”.

## 1. Audyt stanu wyjściowego

Przeczytaj w całości co najmniej:

- `manuscript/manuscript.tex`;
- `docs/fedoryuk_applicability_and_geometry.md`;
- `docs/fedoryuk_weber_wavefunction_and_energy.md`;
- dokumentację analizy Olvera dla silnego wzbudzenia;
- prompty i raporty 09a–09e;
- odpowiednie skrypty oraz testy.

Na początku raportu zapisz dokładnie:

- bieżącą postać równania Fedoryuka;
- definicje \(y,\varepsilon,\eta,\delta,e\);
- wielomian
  \[
  P(y;e)=1+2ey^2-2y^3;
  \]
- położenia i krotności punktów zwrotnych w konfiguracji krytycznej;
- lokalne zmienne Webera;
- dwie lokalne gałęzie energii;
- która z nich zgadza się ze znakiem współczynnika otrzymanym niezależnie metodą Bogoliubowa;
- dokładny status hipotezy orientacji Fedoryuka–Bargmanna po etapie 09.

Sprawdź wszystkie skale, znaki, gałęzie pierwiastków i orientacje krzywych Stokesa niezależnie, zamiast kopiować je bez kontroli.

## 2. Właściwe twierdzenie Fedoryuka

Zidentyfikuj dokładne twierdzenie lub zestaw twierdzeń Fedoryuka potrzebnych do globalnej kontynuacji dla równania z:

- dużym parametrem zespolonym lub rzeczywistym;
- współczynnikiem meromorficznym;
- biegunem czwartego rzędu w \(y=0\);
- parą zlewających się punktów zwrotnych;
- pozostałym prostym punktem zwrotnym;
- wielowartościowym czynnikiem cechowania i nietrywialną monodromią.

Dla każdego używanego twierdzenia podaj:

- pełne dane bibliograficzne;
- rozdział, sekcję i numer twierdzenia, a jeżeli numeru nie ma — dokładne miejsce;
- wierną, lecz zwięzłą parafrazę tezy;
- listę hipotez;
- tabelę: „hipoteza — sposób weryfikacji — status”.

Nie przypisuj Fedoryukowi twierdzenia szerszego niż rzeczywiście sformułowane. Jeśli dostępne źródło nie pozwala potwierdzić numeru lub zakresu twierdzenia, zaznacz to jawnie.

## 3. Globalna geometria

Dla wartości \(e\) w otoczeniu \(-3/2\):

1. Wyznacz wszystkie punkty zwrotne i ich rozwinięcia asymptotyczne.
2. Ustal powierzchnię Riemanna
   \[
   p(y;e)=\sqrt{P(y;e)/y^4}.
   \]
3. Określ cięcia, arkusze i gałęzie całek działania.
4. Zidentyfikuj domeny kanoniczne potrzebne do połączenia:
   - otoczenia rozwiązania regularnego przy \(y=0\);
   - domeny krytycznej pary Webera;
   - ewentualnej domeny Airy’ego przy pozostałym prostym punkcie zwrotnym;
   - sektorów asymptotycznych prowadzących do dopuszczalnego zachowania Bargmanna.
5. Sprawdź, czy istnieje skończony łańcuch nakładających się domen kanonicznych o stałych niezależnych od \(\varepsilon\) dla ustalonego \(n\).
6. Uwzględnij monodromię czynnika \(z^{-\delta}\) i wykaż, jak kompensuje się ona — lub nie kompensuje — z monodromią rozwiązania równania przekształconego.

Rozróżniaj konsekwentnie linie Stokesa, anty-Stokesa i separatrysy zgodnie z przyjętą konwencją Fedoryuka. Po polsku używaj słowa „separatrysa”, nigdy „separatrix”.

Jeśli potrzebna jest poprawiona ilustracja globalnej geometrii, zmodyfikuj istniejący skrypt zamiast tworzyć niepowiązany rysunek. Krzywe numeryczne przedstawiaj wyłącznie jako dane pomocnicze, nie jako dowód istnienia globalnego połączenia.

## 4. Macierze połączeniowe

Zapisz jawnie, w jednej ustalonej bazie:

- lokalną macierz połączeniową Webera dla krytycznej pary;
- macierz lub mnożnik przejścia przez pozostały prosty punkt zwrotny, jeżeli jest potrzebny;
- zmiany baz WKB pomiędzy kolejnymi domenami;
- czynniki fazowe wynikające z wyboru arkusza;
- wpływ cechowania Bargmanna;
- wynikową globalną macierz transferu.

Każdy czynnik fazowy i znak musi mieć podane źródło: orientację drogi, zmianę arkusza, konwencję funkcji Webera albo monodromię.

Nie utożsamiaj lokalnego zerowania współczynnika połączeniowego Webera z globalnym warunkiem Bargmanna, dopóki pełna macierz transferu nie zostanie skonstruowana.

## 5. Warunek kwantyzacji

Jeśli globalny łańcuch zostanie uzasadniony, wyprowadź warunek zaniku współczynnika niedopuszczalnej gałęzi przy końcu łańcucha. Zapisz go najpierw jako:

\[
\mathcal C_{\mathrm{Fed}}(E,\eta,\delta)=0,
\]

a następnie rozwiń dla ustalonego \(n\) i \(\eta\to\infty\).

Sprawdź, czy warunek wybiera gałąź z parą punktów zwrotnych położoną — w zastosowanej zmiennej Webera — na osi urojonej i czy prowadzi do:

\[
\frac{E_n}{V}
=
-\frac32\eta^{4/3}
+
\left[
\delta+\sqrt3\left(n+\frac12\right)-1
\right]\eta^{2/3}
+
\left[
\frac{\delta(1-2\delta)}6
-\frac{6n^2+6n+1}{72}
\right]
+
O(\eta^{-2/3}).
\]

Jeżeli kontrola pozwala, zachowaj także znany współczynnik rzędu \(\eta^{-2/3}\). Nie przepisuj go jednak jako konsekwencji Fedoryuka, jeśli globalne połączenie nie zostało udowodnione.

Porównaj wynik, rząd po rzędzie, z:

- formalnym rozwinięciem Rayleigha–Schrödingera;
- wynikiem Bogoliubowa;
- konstrukcją Olvera;
- lokalną konstrukcją Webera z etapu 09.

Wyraźnie rozdziel:

- zgodność współczynników;
- lokalny warunek rozwiązalności;
- globalny warunek spektralny;
- formalne rozwinięcie;
- rozwinięcie z kontrolowanym oszacowaniem reszty.

## 6. Bramka uczciwości

Jeżeli nie da się rygorystycznie skonstruować pełnego łańcucha, nie ogłaszaj warunku kwantyzacji jako twierdzenia.

W takim przypadku:

1. Sformułuj **Minimalny lemat połączeniowy Fedoryuka–Bargmanna**.
2. Podaj wszystkie jego założenia i dokładną tezę.
3. Wykaż szczegółowo, że lemat ten implikuje wybór właściwej gałęzi Webera i podane rozwinięcie energii.
4. Określ, która część lematu nie wynika bezpośrednio z dostępnych twierdzeń Fedoryuka.
5. Oceń, czy brak dotyczy:
   - geometrii domen kanonicznych;
   - uniformizacji zlewających się punktów zwrotnych;
   - przejścia w pobliżu bieguna;
   - monodromii;
   - oszacowań błędu;
   - czy identyfikacji rozwiązania Bargmanna.
6. Zaproponuj najkrótszą realistyczną drogę dowodu tego lematu.

W manuskrypcie wynik warunkowy musi być nazwany hipotezą albo twierdzeniem warunkowym. Żadne porównanie z Bogoliubowem lub Olverem nie może być przedstawione jako dowód globalnego połączenia.

## 7. Weryfikacja symboliczna i numeryczna

Rozbuduj istniejące skrypty, aby automatycznie sprawdzały co najmniej:

- rozwinięcia punktów zwrotnych;
- lokalną redukcję Webera;
- oba znaki pierwszej poprawki energii;
- macierze połączeniowe i ich wyznaczniki;
- rozwinięcie wynikowego warunku kwantyzacji;
- zgodność współczynników energii z wcześniejszym wynikiem;
- zachowanie reszty lokalnej dla kilku ustalonych \(n\).

Jeśli przeprowadzasz eksperyment numeryczny z równaniem różniczkowym, użyj go wyłącznie jako testu lub wskazówki. Podaj drogi całkowania, warunki początkowe, precyzję oraz test stabilności względem zmiany drogi i dokładności.

Dodaj testy regresyjne. Wszystkie dotychczasowe testy muszą nadal przechodzić.

## 8. Zmiany w dokumentacji i manuskrypcie

Utwórz:

- `docs/fedoryuk_global_connection_and_quantization.md`

oraz odpowiednie skrypty i testy.

Zaktualizuj sekcję Fedoryuka w `manuscript/manuscript.tex` tak, aby zawierała:

- jasno opisaną geometrię globalną;
- dokładny status użytych twierdzeń;
- macierzowy schemat połączenia;
- warunek kwantyzacji albo minimalny brakujący lemat;
- porównanie z wynikiem Olvera i Bogoliubowa;
- jednoznaczne rozróżnienie wyniku lokalnego, formalnego, warunkowego i udowodnionego.

Nie rozbudowuj manuskryptu o techniczne szczegóły lepiej pasujące do dokumentu pomocniczego. Tekst główny powinien pozostać czytelny jako artykuł naukowy.

Nie rozpoczynaj jeszcze sekcji o sumowaniu Bendera–Bettencourta. Jest to osobny, późniejszy etap.

## 9. Kontrola końcowa

Uruchom:

- wszystkie testy;
- wszystkie skrypty weryfikacyjne dotyczące etapów 08–10;
- `git diff --check`;
- pełną kompilację LaTeX z bibliografią;
- kontrolę ostrzeżeń i niezdefiniowanych odwołań;
- renderowanie i wizualną kontrolę wszystkich zmienionych stron.

Sprawdź zgodność PDF-u kanonicznego z PDF-em wynikowym.

## 10. Artefakty i raport

Zapisz:

- prompt jako `prompts/prompt_10_fedoryuk_global_connection_and_quantization.md`;
- diff jako `prompt_10_fedoryuk_global_connection_and_quantization.diff`;
- raport jako `prompt_10_fedoryuk_global_connection_and_quantization.log`.

Raport ma zawierać:

1. krótkie streszczenie wyniku;
2. werdykt:
   - `GLOBAL CONNECTION PROVED`,
   - `CONDITIONAL REDUCTION PROVED`,
   - albo `GLOBAL CONNECTION NOT ESTABLISHED`;
3. dokładny wykaz sprawdzonych hipotez Fedoryuka;
4. dokładny wykaz hipotez niesprawdzonych;
5. status warunku kwantyzacji;
6. status każdego współczynnika rozwinięcia energii;
7. zmienione i utworzone pliki;
8. wyniki testów i kompilacji;
9. `git status --short`.

Nie wykonuj commitów ani pushów. Nie dodawaj wygenerowanego PDF-u do repozytorium, jeśli obowiązujące reguły projektu tego zabraniają.
