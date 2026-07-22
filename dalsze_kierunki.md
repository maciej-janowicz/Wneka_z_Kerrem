# Dalsze kierunki badań

## Status dokumentu

Niniejszy plik jest roboczą mapą dalszych kierunków projektu, o statusie
podobnym do `zarys.md`. Nie stanowi części manuskryptu ani deklaracji nowości.
Twierdzenia o pierwszeństwie wymagają pełnego przeglądu literatury i kontroli
źródeł pierwotnych.

## Fizyczny prior art: właściwe pytanie

Badany hamiltonian

\[
H=\frac{V}{2}a^{\dagger 2}a^2+\hbar\omega_0a^\dagger a
  +Fa^\dagger+\overline F\,a
\]

jest hamiltonianem koherentnie, jednofotonowo wzbudzanego rezonatora Kerra w
układzie obracającym się. W obrazie laboratoryjnym jego wartości własne należy
interpretować jako quasienergie. Zamkniętego problemu spektralnego nie wolno
utożsamiać ze stanem ustalonym równania Lindblada, rozwiązaniem complex-P,
rezonansem operatora niehermitowskiego ani rozwiązaniem półklasycznym.

Literatura fizyczna obejmuje badania quasienergii, rezonansów wielofotonowych,
unikanych przecięć, stanów Floqueta, tunelowania dynamicznego i ich
półklasycznej interpretacji. W szczególności trzeba uwzględnić prace z linii:

- Dykman--Fistul: rezonanse i antyrezonanse wielofotonowe;
- Peano--Thorwart oraz Leyton--Peano--Thorwart: widmo Floqueta, dublety
  wielofotonowe i dynamika oscylatora Duffinga;
- Maslova--Anikin--Gippius--Sokolov: ten sam hamiltonian w układzie obracającym
  się, numeryczna diagonalizacja oraz obrazy wybranych stanów w płaszczyźnie
  amplitudy koherentnej.

Nie możemy zatem przedstawiać jako nowych:

- samego badania quasienergii tego hamiltonianu;
- rezonansów wielofotonowych i mieszania stanów;
- półklasycznej interpretacji stanów przez klasyczne trajektorie;
- numerycznych wykresów wybranych stanów w płaszczyźnie amplitudy
  koherentnej.

Właściwe, węższe pytanie przeglądu brzmi:

> Czy globalny problem Bargmanna--Focka dla zamkniętego, jednofotonowo
> wzbudzanego oscylatora Kerra został rozwiązany analitycznie lub
> quasi-analitycznie, bez diagonalizacji hamiltonianu?

W dotychczas sprawdzonych materiałach takiego rozwiązania nie znaleziono. Nie
jest to jeszcze dowód jego nieistnienia.

Potencjalnie wartościowe pozostają:

- warunek widmowy wynikający z analityczności i normowalności
  Bargmanna--Focka, zapisany przez rozwiązanie minimalne, ułamek łańcuchowy,
  dane połączeniowe lub dane Stokesa;
- globalny wzrost sektorowy funkcji własnych;
- geometria ich zer i poziomic modułu w całej płaszczyźnie zespolonej;
- zależność tej geometrii od parametrów fizycznych i numeru stanu;
- systematyczne porównanie funkcji Bargmanna z klasycznymi obszarami
  quasienergii.

## Analiza asymptotyczna w płaszczyźnie zespolonej

Do projektu należy dodać analizę asymptotyczną w duchu Olvera i Fedoryuka.
Jej naturalnym początkiem będzie zespolona metoda WKB, w szczególności w
ujęciu Vorosa znanym z pracy w *Physical Review A*.

Planowane zagadnienia:

1. Wyznaczenie formalnych rozwiązań WKB równania w postaci Liouville'a.
2. Określenie punktów zwrotnych, krzywych Stokesa i anty-Stokesa oraz
   właściwych dziedzin kanonicznych.
3. Konstrukcja rozwiązań sektorowych i ich asymptotycznych rozwinięć przy
   osobliwościach w zerze i w nieskończoności.
4. Wyznaczenie lub przybliżenie mnożników Stokesa i współczynników
   połączeniowych.
5. Zbadanie, czy warunek Bargmanna--Focka można przełożyć na zanik określonej
   składowej wykładniczej albo na warunek połączeniowy.
6. Powiązanie geometrii Stokesa z rozmieszczeniem zer i globalnymi mapami
   \(|\Psi(z)|\).
7. Porównanie warunku WKB z warunkiem otrzymanym z rekurencji Taylora lub
   ułamka łańcuchowego.

Trzeba ustalić dokładną pracę Vorosa w *Physical Review A* i sprawdzić, które
jej twierdzenia stosują się bezpośrednio, a które wymagają adaptacji do naszej
zdegenerowanej postaci DCHE z \(\epsilon_D=0\).

## Pseudo-czas: obrazy Laplace'a i Borela

Załóżmy, że znana jest funkcja własna \(\Psi(z)\). Można formalnie pytać, czy
jest ona transformatą Laplace'a obiektu zależnego od pseudo-czasu \(\tau\):

\[
\Psi(z)=\int_0^\infty e^{-z\tau}G(\tau)\,d\tau.
\]

Aby nie mylić amplitudy napędu z funkcją pseudo-czasu, w tej części amplitudę
oznaczamy przez \(f\). Równanie Bargmanna ma wtedy postać

\[
\frac V2z^2\Psi''+(\hbar\omega_0z+\overline f)\Psi'
 +(fz-E)\Psi=0.
\]

Przy formalnym odwracaniu transformaty Laplace'a, z pominięciem na tym etapie
członów brzegowych w \(\tau=0\), otrzymuje się kandydackie równanie

\[
\frac V2(\tau^2G)''-\hbar\omega_0(\tau G)'
 +fG'-\overline f\,\tau G-EG=0,
\]

czyli

\[
\frac V2\tau^2G''+
 \bigl[f+(2V-\hbar\omega_0)\tau\bigr]G'
 +\bigl[V-\hbar\omega_0-E-\overline f\,\tau\bigr]G=0.
\]

Ten rachunek wymaga ponownego, rygorystycznego wyprowadzenia wraz ze znakami,
konwencją transformaty, dziedziną całkowania i wszystkimi członami brzegowymi.

### Podstawowa trudność

Jeżeli

\[
\Psi(z)=\sum_{n=0}^{\infty}c_nz^n
\]

jest funkcją całą, to jednostronna odwrotna transformata Laplace'a nie musi
być zwykłą funkcją. Formalna relacja

\[
\mathcal L^{-1}[z^n]=\delta^{(n)}(\tau)
\]

prowadzi do obiektu skoncentrowanego w \(\tau=0\), należącego raczej do klasy
dystrybucji, ultradystrybucji lub analitycznych funkcjonałów. Trzeba przy tym
sprawdzić znaki zależne od przyjętej konwencji Laplace'a. Zwykła funkcja
\(G\in L^1(0,\infty)\) może więc nie być właściwym obiektem.

### Bardziej naturalny kandydat: transformata Borela

Warto zbadać funkcję

\[
\widehat\Psi(\tau)=
\sum_{n=0}^{\infty}\frac{c_n}{n!}\tau^n,
\]

dla której formalnie

\[
\Psi(z)=\int_0^\infty e^{-t}\widehat\Psi(zt)\,dt,
\]

o ile całka istnieje w rozważanym kierunku. Ten obraz może połączyć problem
Bargmanna z analizą WKB, zjawiskiem Stokesa i resurgencją:

- osobliwości w płaszczyźnie Borela mogą kodować asymptotykę \(\Psi\);
- kierunki prowadzące do tych osobliwości mogą wyznaczać kierunki Stokesa;
- boczne sumy Laplace'a mogą odpowiadać rozwiązaniom sektorowym;
- ich skoki mogą kodować mnożniki Stokesa;
- warunek Bargmanna--Focka może przyjąć postać warunku analityczności, wzrostu,
  sumowalności lub doboru kierunku całkowania.

Drugą możliwością jest transformacja konturowa

\[
\Psi(z)=\int_\Gamma e^{z\tau}G(\tau)\,d\tau,
\]

w której wybór konturu \(\Gamma\) jest częścią rozwiązania. Różne kontury
mogą odpowiadać różnym rozwiązaniom sektorowym i różnym danym Stokesa.

## Konkretne pytania badawcze

1. W jakiej przestrzeni funkcji lub funkcjonałów istnieje odwrotna transformata
   Laplace'a funkcji własnej Bargmanna?
2. Jak brzmi dokładne równanie dla obiektu pseudo-czasu po uwzględnieniu
   członów brzegowych?
3. Jak rekurencja współczynników \(c_n\) przekształca się po transformacji
   Borela?
4. Jaki jest promień zbieżności i zbiór osobliwości
   \(\widehat\Psi(\tau)\)?
5. Czy normowalność Bargmanna--Focka jest równoważna warunkowi wzrostu,
   minimalności albo sumowalności w płaszczyźnie Borela?
6. Czy kwantyzację energii można wyrazić przez zanik skoku Stokesa, warunek na
   współczynnik połączeniowy lub dopuszczalny kontur Laplace'a?
7. Czy osobliwości Borela przewidują globalne rozmieszczenie zer
   \(\Psi(z)\)?
8. Jak obrazy Laplace'a--Borela zmieniają się wraz z \(V\), \(f\),
   \(\omega_0\) i numerem stanu?

## Najbliższa kolejność prac

1. Dokończyć wąski przegląd fizycznego prior art dla zamkniętego problemu
   quasienergii.
2. Zweryfikować pełne dane bibliograficzne i treść pracy Vorosa w
   *Physical Review A*.
3. Wyprowadzić zespoloną geometrię WKB dla równania w postaci Liouville'a.
4. Rygorystycznie sprawdzić transformację Laplace'a, w tym człony brzegowe i
   właściwą klasę funkcjonałów.
5. Wyprowadzić równanie lub relację funkcjonalną dla transformaty Borela.
6. Porównać trzy potencjalne warunki widmowe: minimalne rozwiązanie rekurencji,
   dane Stokesa/WKB oraz normowalność Bargmanna--Focka.
7. Dopiero później włączyć zweryfikowane wyniki do manuskryptu.
