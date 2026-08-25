# Prompt 11f_1 — domknięcie sekcji Bendera–Bettencourta i audyt przed commitem

Pracujesz w repozytorium:

    ~/Dokumenty/Prace_i_dnie/Wnęka_z_Kerrem

na gałęzi master. Zachowaj wszystkie dotychczasowe zmiany z etapów 11a–11f. Nie wykonuj żadnego commitu ani pushu.

## Cel

Domknij etap dotyczący metody Bendera–Bettencourta krótką, ściśle dyskusyjną uwagą o możliwych dalszych kierunkach. Nie wykonuj nowych rachunków. Przy okazji usuń dwie drobne nieścisłości językowe wskazane poniżej i przeprowadź końcowy audyt całej sekcji przed commitem.

## 1. Dwie obowiązkowe korekty sformułowań

1. Jeżeli tekst mówi, że iloraz Rayleigha stanu przybliżonego jest „exact through orders…”, zastąp to precyzyjnym stwierdzeniem w rodzaju:

   “The perturbative expansion of its Rayleigh quotient agrees with the exact Rayleigh–Schrödinger series through orders …”

   Zachowaj już wykazane rzędy zgodności, bez ich wzmacniania.

2. Jeżeli dokumentacja lub manuskrypt mówi o „complete order-λ⁴ logarithmic WKB terms”, złagodź to do:

   “the displayed order-λ⁴ logarithmic WKB terms in a fixed dominant sector”

   albo do równoważnego, równie ostrożnego sformułowania. Nie sugeruj kompletności globalnego rozwinięcia, jeśli nie została udowodniona.

## 2. Krótka dyskusja końcowa — bez nowych obliczeń

Włącz do istniejącej sekcji Bendera–Bettencourta, najlepiej przez kondensację lub zastąpienie fragmentu obecnego akapitu Outlook/Discussion, jeden krótki akapit omawiający trzy powiązane możliwości:

1. Pełna multiplikatywna reorganizacja

   Ψ = Y₀ exp(λ²S₁ + λ⁴S₂ + ⋯)

   może w zasadzie prowadzić do globalnego stanu z przestrzeni Bargmanna dopiero po uwzględnieniu całego szeregu oraz właściwego opisu zer. Skończone obcięcie eksponentu nie daje takiego wyniku: lokalne kumulanty mają bieguny w zerach Y₀, a ich wykładnicze obcięcie wytwarza osobliwości istotne. Ponadto sama eksponenta funkcji całkowitej jest bezzerowa, podczas gdy zera dokładnego stanu na ogół się przemieszczają. Globalna reprezentacja musiałaby więc najpewniej rozdzielać czynnik opisujący zera — np. iloczyn kanoniczny Weierstrassa — od części wykładniczej oraz kontrolować wzrost Bargmannowski. Przedstaw to jako motywację i otwarty problem, nie jako wynik.

2. Metoda wielu skal zastosowana bezpośrednio do równania Riccatiego dla pochodnej logarytmicznej mogłaby formalnie wytwarzać sumę pod eksponentem, analogicznie do mechanizmu Bendera–Bettencourta. Zaznacz jednak, że realistycznie byłaby to konstrukcja lokalna lub sektorowa; ruchome bieguny związane z zerami, dane Stokesa i warunek globalnej przynależności do przestrzeni Bargmanna czynią jej praktyczne domknięcie trudnym.

3. Kwazilinearyzacja równania Riccatiego w duchu prac Mandelzweiga i Kriveca może stanowić alternatywny przyszły kierunek, lecz nie jest tu rozwijana ani testowana. Zweryfikuj dokładną pisownię nazwisk i pełne dane bibliograficzne w źródle pierwotnym przed dodaniem cytowania. Dodaj najwyżej jedną pozycję bibliograficzną i tylko wtedy, gdy jej metadane zostały wiarygodnie sprawdzone. W przeciwnym razie nie zgaduj danych bibliograficznych i sformułuj wzmiankę jeszcze ostrożniej.

Ton akapitu ma odpowiadać hipotezie roboczej: odpowiedź na pytania o globalne wysumowanie oraz bezpośrednią konstrukcję wielu skal jest twierdząca w zasadzie, lecz obecnie przecząca w praktyce.

## 3. Ścisłe ograniczenie zakresu

Nie wykonuj:

- obliczenia S₃ ani dalszych subdiagonali;
- nowego rozwinięcia Riccatiego lub rachunku wielu skal;
- iteracji kwazilinearyzacyjnych ani eksperymentów numerycznych;
- konstrukcji iloczynu Weierstrassa;
- nowych wykresów, tabel lub rysunków;
- nowej sekcji lub podsekcji;
- zmian w części Fedoryuka;
- commitu ani pushu.

Nie zwiększaj objętości manuskryptu ponad obecne 31 stron. Preferuj redakcję i kondensację istniejącego tekstu. Nowa dyskusja powinna zajmować najwyżej jeden krótki akapit; nie dodawaj rozbudowanych nowych wzorów.

## 4. Audyt merytoryczny i redakcyjny

Sprawdź po zmianach, że:

- S₁ i S₂ są konsekwentnie traktowane jako kolejne składniki logarytmu, z potęgami odpowiednio λ² i λ⁴;
- nigdzie nie pomylono addytywnego przybliżenia Y₀ + λ²Y₁ + λ⁴Y₂ z obciętą postacią wykładniczą;
- stwierdzenia o całkowitości, przestrzeni Bargmanna, biegunach i osobliwościach istotnych są zgodne z wynikami 11c–11f;
- zakres zgodności szeregu energii nie został rozszerzony ponad to, co rzeczywiście sprawdzono;
- wszystkie nowe twierdzenia są jawnie oznaczone jako perspektywa, możliwość lub problem otwarty;
- terminologia i notacja są jednolite w manuskrypcie oraz dokumentacji projektu.

## 5. Weryfikacja

Wykonaj wszystkie dostępne, adekwatne testy i kontrole, w szczególności:

- pełną kompilację LaTeX;
- testy i skrypty kontrolne etapów 11a–11f oraz pełny zestaw testów projektu, jeśli istnieje;
- git diff --check;
- kontrolę odwołań i bibliografii;
- pdftotext lub równoważną kontrolę tekstu wynikowego;
- wizualny przegląd stron obejmujących sekcję Bendera–Bettencourta, bibliografię i miejsca łamania stron;
- potwierdzenie, że PDF nadal ma 31 stron;
- końcowe git status -sb.

Jeżeli ujawnisz problem merytoryczny wymagający nowych rachunków, nie próbuj go maskować ani rozszerzać zakresu zadania. Opisz go w logu jako przeszkodę przed commitem.

## 6. Niezależne artefakty etapu 11f_1

Utwórz nowe, samodzielne pliki — nie dopisuj do artefaktów 11f:

- prompt_11f_1_finalize_bb_discussion.diff
- prompt_11f_1_finalize_bb_discussion.log

Plik .diff ma zawierać wyłącznie zmiany wykonane w etapie 11f_1, względem stanu zastanego bezpośrednio po 11f, a nie skumulowany diff etapów 11a–11f_1. Jeśli repozytorium jest już brudne, najpierw bezpiecznie zapisz migawkę bieżącego diffu i na jej podstawie wyodrębnij tylko nowy przyrost. Nie cofaj cudzych ani wcześniejszych zmian.

Plik .log powinien zawierać:

- listę zmienionych plików;
- dokładny opis obu korekt językowych;
- ostateczny tekst lub wierne streszczenie nowego akapitu dyskusyjnego;
- informację, czy i jak zweryfikowano ewentualne cytowanie Mandelzweiga–Kriveca;
- wyniki wszystkich testów, kompilacji, kontroli PDF i liczby stron;
- wynik git diff --check oraz git status -sb;
- jawną informację, że nie wykonano commitu ani pushu;
- końcowy werdykt, najlepiej dokładnie jeden z następujących:

  - BB SECTION FINALIZED; READY FOR COMMIT
  - BB DISCUSSION FINALIZED; MINOR ISSUE REMAINS
  - STAGE 11F REQUIRES REVISION BEFORE COMMIT

Na końcu odpowiedzi podaj krótkie podsumowanie, ścieżki do PDF, plików .diff i .log oraz werdykt. Nie wykonuj commitu ani pushu.
