# Prompt 11e — jawna konwencja kanałów dolnych dla \(N=0\)

Pracujesz w repozytorium:

~/Dokumenty/Prace_i_dnie/Wnęka_z_Kerrem

na gałęzi master.

Zachowaj wszystkie niezatwierdzone zmiany etapów 11a–11d. Nie wykonuj git commit ani git push.

## Cel

Etap 11d potwierdził:

- poprawność pierwszego multiplikatywnego kroku Bendera–Bettencourta;
- poprawną reprezentację wariacji stałych;
- poprawność warunków rozwiązalności dla \(N=0\), \(N=1\) i \(N\ge2\);
- zgodność z \(e_N^{(4)}\).

Pozostała jedna lokalna niejednoznaczność w manuskrypcie. W równaniach energii występują formalne ilorazy

\[
\frac{N}{N-1+\delta},
\qquad
\frac{N}{(N-1+\delta)^2}.
\]

Dla regularnego, niedegenerowanego przypadku \(N=0,\delta=1\) zapisane dosłownie dają one \(0/0\), chociaż odpowiadają nieistniejącemu kanałowi dolnemu i powinny zostać usunięte przed wykonaniem dzielenia.

## Zadanie

1. W manuscript/manuscript.tex, bez zmiany wzorów dla ogólnego \(N\), doprecyzuj bezpośrednio po równaniu na \(e_N^{(4)}\), że:

   - pierwszy człon w \(e_N^{(4)}\) jest nieobecny dla \(N<2\);
   - dla \(N=0\) wszystkie wkłady kanału dolnego proporcjonalne do \(N\), w szczególności
     \[
     \frac{N}{N-1+\delta},
     \qquad
     \frac{N}{(N-1+\delta)^2},
     \]
     usuwa się przed dzieleniem;
   - dlatego
     \[
     e_0^{(2)}=-\frac1\delta,
     \qquad
     e_0^{(4)}=\frac{1}{\delta^3(1+2\delta)},
     \]
     a dla \(\delta=1\) otrzymuje się \(e_0^{(4)}=1/3\).

2. Użyj zwięzłego zdania. Preferowana treść:

   > The first term in (153) is absent for \(N<2\); for \(N=0\), every lower-channel contribution proportional to \(N\) is omitted before division. Thus \(e_0^{(2)}=-1/\delta\) and \(e_0^{(4)}=1/[\delta^3(1+2\delta)]\).

   Dostosuj numer równania przez odsyłacz LaTeX, nie wpisuj numeru na sztywno w źródle.

3. Sprawdź symbolicznie wartość \(e_0^{(4)}\) bez tworzenia pośrednich ilorazów \(0/0\), w szczególności dla \(\delta=1\).

4. Upewnij się, że dokumentacja audytowa i skrypty 11a–11d pozostają zgodne z tym zdaniem. Nie wykonuj żadnych nowych rachunków podprzekątnych.

5. Nie rozpoczynaj jeszcze sumowania drugiej podprzekątnej. Będzie ono osobnym etapem.

## Weryfikacja

Uruchom:

- testy 11a–11d;
- pełny zestaw testów;
- właściwe skrypty weryfikacyjne;
- git diff --check;
- kompilację LaTeX z bibliografią;
- kontrolę ostrzeżeń i odsyłaczy;
- pdftotext dla strony zawierającej równania energii;
- wizualną kontrolę zmienionej strony PDF.

Manuskrypt ma pozostać na 31 stronach lub mniej.

## Obowiązkowe, niezależne artefakty

Utwórz nowe pliki:

- prompt_11e_clarify_n0_lower_channel_convention.diff;
- prompt_11e_clarify_n0_lower_channel_convention.log.

Plik .diff ma zawierać wyłącznie zmiany etapu 11e względem dokładnego stanu po 11d. Nie dołączaj zmian 11a–11d. Przed edycją wykonaj migawkę wszystkich plików, które zamierzasz zmienić, i wygeneruj różnicę względem tej migawki.

Plik .log ma zawierać:

1. początkowy git status --short;
2. opis wykrytej niejednoznaczności \(0/0\);
3. ostateczne zdanie wprowadzone do manuskryptu;
4. niezależne sprawdzenie
   \[
   e_0^{(2)}=-\frac1\delta,\qquad
   e_0^{(4)}=\frac{1}{\delta^3(1+2\delta)};
   \]
5. wynik dla \(\delta=1\);
6. listę zmienionych plików;
7. wyniki testów, kompilacji, pdftotext i kontroli wizualnej;
8. liczbę stron przed i po zmianie;
9. końcowy git status --short;
10. końcowy werdykt.

Raport zakończ dokładnie werdyktem:

N=0 LOWER-CHANNEL CONVENTION EXPLICIT; STAGES 11A–11D VERIFIED

## Zasady końcowe

- Nie wykonuj commitów ani pushów.
- Nie zmieniaj poprawnego rdzenia 11c–11d.
- Nie dodawaj nowej podsekcji.
- Nie zwiększaj liczby stron.
- Nie rozpoczynaj etapu drugiej podprzekątnej.

