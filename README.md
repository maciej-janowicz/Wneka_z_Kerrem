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
latexmk -pdf manuscript/manuscript.tex
```

Kanonicznym wynikiem tego polecenia jest plik `manuscript.pdf` w katalogu
głównym repozytorium. Plik `manuscript/manuscript.pdf`, jeśli istnieje, nie
jest kanonicznym wynikiem tej procedury i może być nieaktualny.

Pliki pomocnicze generowane przez LaTeX są ignorowane przez Git.
