# Candy Crush
# Irinuca a descoperit un nou joc pe calculator.
# Pe ecran sunt plasate pe o linie n bile colorate.
# Culorile bilelor sunt codificate cu numere naturale.
# Un subșir de bile alăturate având toate aceeași culoare se numește secvență.
# O secvență va conține numărul maxim de bile alăturate având aceeași culoare.
# Lungimea unei secvențe este egală cu numărul de bile din care este compusă.
# Irinuca are la dispoziție un arc special.
# Trăgând cu arcul asupra unei bile, dacă aceasta face parte dintr-o secvență de lungime cel
# puțin egală cu 3, întreaga secvență va fi eliminată,
# iar bilele din dreapta secvenței se vor deplasa spre stânga
# pentru a umple “golul” lăsat de bilele eliminate.
# Dacă imediat în stânga și în dreapta secvenței eliminate se găseau două secvențe
# având aceeași culoare și dacă secvența obținută din unirea acestora
# după eliminare are o lungime cel puțin egală cu 3,
# atunci va fi și ea eliminată la rândul ei.
# Procesul continuă până când secvențele din stânga și dreapta unei secvențe
# tocmai eliminate au culori diferite sau până când lungimea secvenței obținute
# prin alăturare este mai mică decât 3 sau până când în stânga ori
# în dreapta unei secvențe eliminate nu se mai găsesc bile sau până sunt
# eliminate toate bilele de pe ecran.
# Scopul jocului este de a elimina cât mai multe bile de pe ecran.
# Cum Irinuca încă nu se pricepe prea bine la acest joc și-a stabilit o strategie.
# Va trage cu arcul întotdeauna asupra unei bile ce face parte din secvența
# de lungime maximă de pe ecran.
# Dacă sunt mai multe astfel de secvențe,
# ea va alege cea mai din stânga secvență de lungime maximă.
# Dacă toate secvențele de pe ecran au lungimi mai mici decât 3,
# Irinuca nu va mai putea elimina nici una din ele și jocul se încheie.
# De exemplu, dacă șirul inițial de bile este:
# 5 1 3 3 2 2 2 2 3 1 1 5 6 4 4 4 4 7
# Irinuca va acționa asupra unei bile de culoare 2.  Prin eliminare se obține șirul de bile
# 5 1 3 3 3 1 1 5 6 4 4 4 4 7
# din care se elimină și secvența de bile de culoare 3 obținându-se șirul de bile
# 5 1 1 1 5 6 4 4 4 4 7
# din care se elimină și secvența de culoare 1.
# 5 5 6 4 4 4 4 7
# Cum secvența de bile de culoare 5 nu este suficient de lungă, aceasta nu se mai elimină. Acum Irinuca trage asupra unei bile de culoare 4 și obține
# 5 5 6 7
# dar cum în stânga și în dreapta secvenței eliminate
# sunt secvențe de culori diferite,
# nu se va mai elimina nici o secvență.
# Jocul se încheie deoarece nu mai există nici o secvență
# de lungime cel puțin 3 asupra căreia să se poată trage.
# Cerință:
# 	Cunoscând numărul de bile și culorile fiecărei bile de pe ecran se
# 	cere să se determine:
# 1. numărul de secvențe de bile care se aflau inițial pe ecran;
# 2. numărul de bile care rămân neeliminate
# de pe ecran și culorile bilelor rămase în ordine pe ecran la finalul jocului.
# Date de intrare:
# 	Se citesc N numere de la tastatură care
# 	reprezinta șirul de bile de la începutul jocului.


# Cool
# Se consideră un șir A format din N elemente naturale nenule.
# Numim secvență de lungime K a șirului A orice succesiune de elemente consecutive
# din șir de forma Ai, Ai+1, ..., Ai+K-1.
# O secvență o numim secvență cool dacă elementele
# care o compun sunt distincte și pot fi rearanjate astfel
# încât să alcătuiască o secvență continuă de numere consecutive.
# De exemplu, considerând șirul
# A = (3, 1, 6, 8, 4, 5, 6, 7, 4, 3, 4), atunci secvența
# (8, 4, 5, 6, 7) este o secvență cool deoarece conține
# elemente distincte ce pot fi rearanjate astfel încât să alcătuiască
# șirul de numere consecutive 4, 5, 6, 7, 8,
# pe când secvențele (4, 3, 4), (6, 7, 4, 3) nu sunt considerate secvențe cool.
# Cerință:
# 	Pentru o valoare dată K să se verifice dacă secvența
# 	A1, A2 ... AK este secvență cool.
# 	Dacă secvența este cool, atunci se va afișa
# 	cea mai mare valoare ce aparține secvenței.
# 	Dacă secvența nu este cool, atunci se va afișa numărul
# 	elementelor distincte din secvența
# A1, A2, ..., AK, adică numărul elementelor care apar o singură dată.
# Date de intrare:
# 	Se citesc N și K de la tastatură c
# 	are vor determina numărul de elemente din sir
# 	respectiv lungimea secvenței cool de verificat.
# Exemple:
# INPUT:
# 7 4
# 6 4 5 7 8 3 5
# OUTPUT:
# 7
# Secvența 6 4 5 7 este cool.
# Valoarea maximă din secvență este 7
# INPUT:
# 7 6
# 6 4 5 7 5 4 3
# OUTPUT:
# 2
# Secvența 6 4 5 7 5 4 nu este secvență cool.
# Numărul valorilor distincte din secvență este 2.
# Valorile distincte sunt: 6, 7
