# Driven Kerr cavity in Bargmann space

Projekt poświęcony analizie napędzanej wnęki z nieliniowością Kerra w
reprezentacji Bargmanna. Głównym celem jest opis punktowego zachowania
funkcji falowej na płaszczyźnie zespolonej, ze szczególnym uwzględnieniem
jej zer, wzrostu, fazy i struktury amplitudy.

## Zakres

- wyprowadzenie równania Bargmanna i rekurencji dla współczynników;
- konstrukcja warunku spektralnego bez bezpośredniej diagonalizacji
  Hamiltonianu;
- kontrolowana numeryczna ewaluacja funkcji całkowitej;
- wizualizacja $\log|\psi(z)|$, fazy, zer i poziomic;
- eksperymentalne badanie iteracji $z_{n+1}=\psi(z_n)$.

## Struktura repozytorium

- `zarys.md` — pierwotny opis pomysłu i zakresu projektu;
- `manuscript/manuscript.tex` — roboczy manuskrypt LaTeX;
- `figures/` — planowane rysunki (katalog nie jest jeszcze utworzony);
- `src/` i `tests/` — planowany kod obliczeniowy i testy.

## Kompilacja manuskryptu

Z katalogu głównego repozytorium:

```bash
latexmk -pdf -outdir=manuscript manuscript/manuscript.tex
```

Kanonicznym wynikiem tego polecenia jest plik
`manuscript/manuscript.pdf`. Opcja `-outdir=manuscript` zachowuje katalog
główny jako katalog roboczy (co jest wymagane przez ścieżkę bibliografii),
a jednocześnie automatycznie aktualizuje kanoniczny PDF w katalogu
manuskryptu. Ewentualny plik `manuscript.pdf` w katalogu głównym jest
niekanonicznym artefaktem wcześniejszej procedury budowania.

Pliki pomocnicze generowane przez LaTeX są ignorowane przez Git.
