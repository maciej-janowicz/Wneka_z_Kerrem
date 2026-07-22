Mamy jeden mod pola we wnęce z nieliniowością Kerra z zewnętrznym wzbudzeniem. Dobrze określony doświadczalnie. Moje/nasze zadania (zaraz otworzę je w osobnym projekcie) jest matematyczne: zbadać dokładnie punktowe zachowanie funkcji falowej w reprezentacji Bargmanna w całej płaszczyźnie zespolonej. Otrzymać quasi-NIEnumeryczne (numeryka mogłaby być ukryta w w jakimś skomplikowanym równaniu algebraicznym na energię, ale nie w diagonalizacji Hamiltonianiu). Otrzymać *prześliczne* obrazki pokazujące, gdzie w płaszczyźnie zespolonej moduł funkcji falowej jest mały, gdzie duży, a gdzie średni, zaleźnie od parametrów. Na artystycznym marginesie, zrobić kilka iteracji funkcji falowe (tzn. z_{n} = \Psi(z_{n-1})) i otrzymać przepiękne pseudo-fraktale. Znaleźć czasopismo do publikacji. I na to wszystko mamy - już Ci mówię - 9.5 godziny, ale w tym 3 godziny przerwy. 
Wiem, że masz mnie dosyć. Ale wybacz jeszcze raz i powiedz, że to się da zrobić. 
 

Maćku — nie mam Cię dosyć. Ani trochę. I tak: to da się zrobić.

Nie da się w 6,5 godziny uczciwie rozwiązać całej matematyki napędzanego oscylatora Kerra, stworzyć pełnej teorii punktowej w przestrzeni Bargmanna i przygotować dojrzałej publikacji. Ale da się zrobić coś znacznie konkretniejszego:

ustalić dokładny model i poprawną postać równania Bargmanna;
wyprowadzić rekurencję dla współczynników funkcji całkowitej;
znaleźć warunek spektralny niewymagający diagonalizacji Hamiltonianu — np. przez ułamki łańcuchowe, rozwiązanie minimalne rekurencji, wyznacznik Hillowskiego albo zera funkcji charakterystycznej;
zbudować kontrolowaną numerykę opartą na tym warunku;
obliczyć Ψ(z) na całej użytecznej części płaszczyzny zespolonej wraz z kontrolą obcięcia;
przygotować naprawdę piękne mapy log∣Ψ(z)∣, fazy, zer i poziomic;
osobno — i jawnie jako eksperyment artystyczno-dynamiczny — zbadać iteracje z
n+1
	​

=Ψ(z
n
	​

);
uzyskać pierwsze pseudo-fraktale;
zbudować repozytorium, programy i szkic manuskryptu;
zrobić rozsądny rekonesans czasopism.

Kluczowe będzie jedno rozróżnienie. „Cała płaszczyzna zespolona” nie może oznaczać jednolitego wykresu numerycznego na nieskończonym obszarze. Możemy natomiast:

analitycznie ustalić, że Ψ jest funkcją całkowitą oraz określić jej wzrost;
numerycznie badać rosnącą rodzinę zwartych obszarów;
oddzielić rzeczywiste zera i strukturę amplitudy od artefaktów obcięcia szeregu.

To już byłby poważny wynik matematyczno-numeryczny.

Mamy 9,5 godziny zegarowe i 6,5 godziny pracy. Zatem żadnego rozrostu zakresu:

najpierw dokładny Hamiltonian i konwencje;
potem równanie Bargmanna i warunek energetyczny;
następnie jeden solidny solver;
potem trzy–cztery znakomite rysunki;
pseudo-fraktale dopiero na końcu;
czasopismo wybieramy na podstawie rzeczywiście uzyskanego wyniku.

Otwórz osobny projekt i przynieś tam przede wszystkim dokładny Hamiltonian, przyjęte jednostki oraz informację, czy interesują nas stany własne autonomicznego Hamiltonianu w obracającej się ramie, czy stan stacjonarny układu otwartego. To rozstrzyga niemal wszystko.

A potem ruszamy. Ty na klawiszach, ja na basie, Codex przy aparaturze — i oscylator Kerra niech się zacznie niepokoić. :-)