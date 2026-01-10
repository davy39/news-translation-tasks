---
title: Rosetta Code — déverrouiller les mystères des langages de programmation qui
  alimentent notre monde
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-20T21:53:26.000Z'
originalURL: https://freecodecamp.org/news/rosetta-code-unlocking-the-mysteries-of-the-programming-languages-that-power-our-world-300b787d8401
coverImage: null
tags:
- name: Computer Science
  slug: computer-science
- name: history
  slug: history
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Rosetta Code — déverrouiller les mystères des langages de programmation
  qui alimentent notre monde
seo_desc: 'By Peter Gleeson


  _The original Rosetta Stone, via [History.com](http://www.history.com/s3static/video-thumbnails/AETN-History_VMS/21/206/tdih-jul19-HD.jpg"
  rel="noopener" target="blank" title=")

  It’s no secret that the tech world is dominated by a r...'
---

Par Peter Gleeson

![Image](https://cdn-media-1.freecodecamp.org/images/rbIDb6F3Lp6O7Ji5KBjZhXYbWxkadd9CnBib)
_La pierre de Rosette originale, via [History.com](http://www.history.com/s3static/video-thumbnails/AETN-History_VMS/21/206/tdih-jul19-HD.jpg" rel="noopener" target="_blank" title=")_

Ce n'est un secret pour personne que le monde de la technologie est dominé par un nombre relativement restreint de langages de programmation. Bien qu'il soit difficile d'obtenir des chiffres exacts (et qu'ils varient sans doute avec le temps), vous pourriez probablement nommer une poignée de langages qui constituent la grande majorité de toute la production de programmation sur une période donnée.

Deux sites intéressants que j'ai visités lors de la recherche pour cet article vous permettent de visualiser les langages de programmation par popularité. [IEEE Spectrum](http://spectrum.ieee.org/static/interactive-the-top-programming-languages-2016) vous permet d'ajuster interactivement les pondérations de diverses métriques, tandis que [PYPL](http://pypl.github.io/PYPL.html) propose un tableau donnant les parts de marché réelles basées sur les données de Google Trends sur les 12 derniers mois.

Maintenant, je refuse d'être entraîné dans des débats sur ce que pourrait être la meilleure métrique de popularité des langages de programmation (et si c'est une statistique importante de toute façon). Ce qui suit est juste une analyse rapide pour illustrer un point (une excuse pour utiliser [R-Fiddle](http://www.r-fiddle.org/) !).

En utilisant les données de PYPL, nous pouvons voir quelques tendances claires :

![Image](https://cdn-media-1.freecodecamp.org/images/O3MVVdasl8lNpEac83d4luN50kFw0Wk9OCiD)
_Graphique produit sur [R-Fiddle.org](http://www.r-fiddle.org/" rel="noopener" target="_blank" title="">R-Fiddle.org</a>; données de <a href="http://pypl.github.io/PYPL.html" rel="noopener" target="_blank" title=")_

#### 1) — Les 10 langages les plus populaires représentent presque 90 % des données de Google Trends

Dans l'ordre, il s'agit de : Java, Python, PHP, C#, JavaScript, C, C++, Objective-C, R et Swift. Ensemble, ils ont une part de marché de 87,1 % sur Google Trends.

#### 2) — La popularité des langages suit une distribution en loi de puissance

En utilisant mon package R préféré, 'igraph', pour sa fonction fiable power.law.fit(), j'ai découvert que la popularité des langages de programmation suit une distribution en loi de puissance :

```
> pL = power.law.fit(shares)
> pL$KS.p

$KS.p
[1] 0.9873141
```

Cette valeur `$KS.p` de 0,987 est la valeur p associée à une statistique de test de Kolmogorov-Smirnov, qui nous indique que nous pouvons être assez sûrs que la distribution de la popularité (telle que définie par PYPL) suit une distribution en loi de puissance.

Comme [de nombreux autres phénomènes](https://en.wikipedia.org/wiki/Pareto_distribution#Applications), la popularité relative des langages de programmation est distribuée de manière inégale. Cela peut généralement s'expliquer par un mécanisme de rétroaction positive (ou 'effet boule de neige') — une version simplifiée pourrait être que plus un langage est populaire, plus il y a d'emplois disponibles dans ce langage, donc plus de personnes sont incitées à l'apprendre, augmentant ainsi sa popularité.

#### Qu'y a-t-il de nouveau ?

Ce n'est pas vraiment une surprise que certains langages de programmation soient bien plus populaires que d'autres. Tout le monde sait déjà que Java, C, C++, C#, Python, etc., sont de loin les langages les plus utilisés.

Ce qui est _plus_ intéressant, à mon avis, c'est l'observation que pour chaque langage de programmation géant, il doit y avoir des dizaines de langages plus petits et plus spécialisés dans la nature.

Mis à part la simple curiosité, il y a de bonnes raisons de s'y intéresser. Quiconque a expérimenté plus d'une poignée de langages de programmation sait que différents langages conviennent à différents usages. JavaScript est pour le développement web, PHP pour la programmation côté serveur, R pour les statistiques, Matlab pour les mathématiques pures. Avec les langages de programmation, la variété est une bonne chose. Il existe peut-être un langage idéalement adapté pour résoudre ce problème dont vous ne saviez même pas qu'il existait.

Mais où les trouver ? Un endroit où chercher est Rosetta Code.

### Un Safari de Programmation

Je ne me souviens pas exactement comment j'ai découvert Rosetta Code, mais une fois que je l'ai trouvé, j'ai été accro. Il se décrit comme un site de [chrestomathie de programmation](http://en.wikipedia.org/wiki/Chrestomathy) et présente un impressionnant 647 langages de programmation dans ses archives. Allez [jeter un coup d'œil](http://rosettacode.org/wiki/Rosetta_Code).

La chose vraiment géniale est que Rosetta Code va au-delà de la simple fourniture d'un exemple générique 'Hello World!' pour chaque langage. Non, au lieu de cela, il propose une collection de plus de 800 tâches de programmation variées, allant de problèmes aussi simples que 'Pair ou Impair', à des problèmes plus avancés, tels que la résolution de labyrinthes et le web scraping. Chaque page de tâche décrit le problème à résoudre, puis donne des solutions dans une gamme de langages de programmation.

Ici, la réputation n'a pas d'importance. En plus de C, C++, Java, etc., vous trouverez des solutions dans des langages que vous n'avez jamais entendus auparavant. Certains sont rétro, d'autres modernes ; certains semblent familiers, tandis que d'autres sont ésotériques au-delà de toute croyance. Vous pourriez passer plus de temps que vous ne l'admettrez à parcourir tous les exemples — mais pour vous aider à commencer, j'ai compilé une liste de certains des langages moins connus et/ou plus intéressants qui ont attiré mon attention. Activez le mode nerd, et plongez !

### Souvenir du Passé

Certains langages durent éternellement, ou du moins le semblent. En plus de C, les langages descendants de Lisp et Fortran existent depuis des décennies, et d'autres comme BASIC et Pascal peuvent être passés de mode mais vivent dans la mémoire populaire.

Le temps a été moins clément pour d'autres, cependant. Voici une liste de certains langages avec des exemples de code sur Rosetta qui, pour le dire d'une manière, sont peu susceptibles de vous faire embaucher de sitôt.

#### **Code d'Ordre EDSAC**

EDSAC est un célèbre ordinateur des débuts, conçu et construit par l'équipe de [Maurice Wilkes](https://en.wikipedia.org/wiki/Maurice_Wilkes) à l'Université de Cambridge à la fin des années 1940. La construction de l'EDSAC a permis à David Wheeler d'obtenir le premier doctorat en informatique en 1951. Pendant qu'il y était, il a également inventé le 'saut de Wheeler', ou _sous-routine fermée_ — que nous appelons communément aujourd'hui 'fonctions'.

Malgré sa place inébranlable dans l'histoire, EDSAC est hors service depuis 1958, alors ne vous précipitez pas pour apprendre son langage de programmation personnalisé. Voici un [exemple](https://rosettacode.org/wiki/Empty_program#EDSAC_order_code) de Rosetta Code. C'est le 'programme vide', ou le programme légitime le plus court. Il ne fait pas grand-chose du tout.

```
T64K  [ set load point ]
GK    [ set base address ]
ZF    [ stop ]
EZPF  [ begin at load point ]
```

#### GEORGE

Ce langage, inventé en 1957, était un langage qui aurait été entré via une bande perforée dans une machine de la taille d'une pièce. Néanmoins, il était plein de fonctionnalités, y compris des boucles, des instructions conditionnelles, des sous-routines et des structures de données matricielles. Il se lit même un peu comme un langage plus moderne.

Soixante ans plus tard, GEORGE n'est plus parmi nous. Voici comment il aurait été utilisé pour calculer la [somme d'une série](https://rosettacode.org/wiki/Sum_of_a_series#GEORGE) :

```
0 (s)
1, 1000 rep (i)
   s 1 i dup × / + (s) ;
]
P
```

#### BCPL

Le 'Basic Combined Programming Language', ou BCPL, mérite sa place dans l'histoire de l'informatique. En plus d'avoir apparemment donné naissance à la tradition du 'Hello World !', BCPL a eu une influence profonde sur la conception de B, qui était lui-même le précurseur de C. BCPL a été le premier langage à introduire les accolades '{' comme moyen de définir des blocs de code — une convention encore utilisée dans beaucoup des langages les plus importants d'aujourd'hui. Pas mal, en tant qu'héritage.

[Voici](https://rosettacode.org/wiki/Hello_world/Text#BCPL) un programme 'Hello World' écrit en BCPL :

```
GET "libhdr"
 
LET start() = VALOF
{ writef("Hello world!")
  RESULTIS 0
}
```

#### PL/I

Développé par IBM au début des années 1960, PL/I (Programming Language One) était largement utilisé à son apogée, mais n'a jamais tout à fait déplacé ses concurrents Fortran et COBOL. PL/I était principalement un langage de mainframe, et avec l'avènement du PC et la popularité croissante de langages comme C++ et Java, PL/I est tombé en désuétude.

Il y a [de nombreux exemples](https://rosettacode.org/wiki/Category:PL/I) de PL/I sur Rosetta Code ; voici comment il génère une séquence de Fibonacci :

```
/* Form the n-th Fibonacci number, n > 1. */
get list(n);
f1 = 0; f2 = 1;
do i = 2 to n;
   f3 = f1 + f2;
   put skip edit('fibo(',i,')=',f3)(a,f(5),a,f(5));
   f1 = f2;
   f2 = f3;
end;
```

#### SNOBOL4

SNOBOL a été développé au début des années 1960 et est devenu un langage d'enseignement populaire dans la décennie suivante. Cependant, il a perdu de sa popularité tout au long des années 1980 et 1990, mais pas avant d'avoir pu influencer la conception de Lua, qui fait une apparition dans le top 20 des classements PYPL que nous avons vus précédemment.

Voici un programme SNOBOL4 qui affiche la longueur d'une chaîne :

```
         output = "Byte length: " size(trim(input))
end
```

#### FOCAL

FOCAL ('Formulating On-Line Calculations in Algebraic Language', puisque vous demandez) a été introduit en 1968, et était un langage efficace qui pouvait fonctionner sur des systèmes très limités en mémoire. Une particularité du langage était sa phobie apparente des chaînes de caractères. Saisir la chaîne 'HELLO' aurait été interprété comme demander à l'ordinateur de calculer `8 ^ "LLO"`, ce que FOCAL avait du mal à résoudre avant de donner une réponse numérique massive.

Malgré ses excentricités, FOCAL a été suffisamment utilisé pendant les années 70 et 80. Coca-Cola a même utilisé sa propre version, qu'ils ont imaginativement appelée COKE.

[Cet exemple](http://rosettacode.org/wiki/Temperature_conversion#FOCAL) de Rosetta Code montre un programme FOCAL qui convertit les températures entre différentes unités :

```
01.10 ASK "TEMPERATURE IN KELVIN", K
01.20 TYPE "K ", %6.02, K, !
01.30 TYPE "C ", %6.02, K - 273.15, !
01.40 TYPE "F ", %6.02, K * 1.8 - 459.67, !
01.50 TYPE "R ", %6.02, K * 1.8, !
```

#### SETL

SETL a été inventé à la fin des années 1960 et était fortement basé sur la [théorie des ensembles](https://en.wikipedia.org/wiki/Set_theory), la branche des mathématiques qui concerne les collections d'objets. La dernière version stable remonte à 2005, mais malgré son déclin d'utilisation, SETL a quelques revendications à la célébrité.

Le premier compilateur d'Ada, qui a été développé par le Département de la Défense des États-Unis, a été écrit en SETL. De plus, on dit qu'il a influencé ABC — le langage qui a inspiré la conception de Python.

Voici comment SETL calcule le [plus grand diviseur commun](https://rosettacode.org/wiki/Greatest_common_divisor#SETL) de deux entiers. Voyez-vous une ressemblance avec Python ?

```
proc gcd (u, v);
  return if v = 0 then abs u else gcd (v, u mod v) end;
end;
```

#### MUMPS

Ce langage au nom malheureux existe depuis 1966 et est également appelé M. Une caractéristique clé est le système de base de données intégré, qui permet un accès super-efficace aux données stockées.

Bien qu'il ne soit plus d'usage courant, MUMPS vit sous la forme de GT.M et InterSystems_Cache — qui ont une niche dans les hôpitaux et les systèmes de bases de données financières. L'Agence spatiale européenne a également utilisé InterSystems_Cache pour sa récente [mission Gaia](https://en.wikipedia.org/wiki/Gaia_(spacecraft)#Data_processing).

Voici comment MUMPS peut être utilisé pour [inverser une chaîne](https://rosettacode.org/wiki/Reverse_a_string#MUMPS) :

```
REVERSE
 ;Take in a string and reverse it using the built in function $REVERSE
 NEW S
 READ:30 "Enter a string: ",S
 WRITE !,$REVERSE(S)
 QUIT
```

### Délibérément Confus

Quelles sont les caractéristiques d'un langage de programmation réussi ? La vitesse ? La polyvalence ? La lisibilité ? Non, oubliez tout cela — examinons une branche de langages de programmation qui sont intentionnellement difficiles et/ou peu intuitifs à utiliser.

Les langages ésotériques, ou 'esolangs', sont des langages de programmation utilisés parfois pour l'expérimentation, parfois pour un défi, et parfois juste comme la blague interne ultime pour les nerds. Si vous ne comprenez pas tout à fait, ce n'est pas grave — en fait, c'est généralement le but.

Des exemples mieux connus incluent [Brainf***](https://rosettacode.org/wiki/Category:Brainf***), [Befunge](https://rosettacode.org/wiki/Category:Befunge) et le particulièrement migraineux [Malbolge](https://rosettacode.org/wiki/Hello_world/Text#Malbolge). Voici une liste de quelques autres, allant de l'amusant à l'intéressant, en passant par l'obtus.

#### INTERCAL

Le langage de programmation ésotérique original a été inventé en 1972, ce qui le rend aussi ancien que C. Il a été introduit comme une parodie des pratiques de programmation prévalentes à l'époque, mais sa survie continue jusqu'à ce jour suggère qu'il est toujours aussi pertinent que jamais.

En plus d'une syntaxe obtuse, INTERCAL confond encore plus ses utilisateurs en les obligeant à utiliser le mot-clé `PLEASE` de temps en temps, sinon le programme refuse de s'exécuter. Cependant, être trop poli se retourne contre vous — dire 'please' trop fréquemment entraînera également une erreur. Bien sûr, cette excentricité n'était pas officiellement documentée, car cela aurait été trop utile.

Voici une [boucle infinie](https://rosettacode.org/wiki/Loops/Infinite#Intercal), écrite en INTERCAL :

```
NOTE THIS IS INTERCAL
       PLEASE ,1 <- #5
       DO ,1 SUB #1 <- #54
       DO ,1 SUB #2 <- #192
       DO ,1 SUB #3 <- #136
       PLEASE ,1 SUB #4 <- #208
       DO ,1 SUB #5 <- #98
       DO COME FROM (1)
       DO READ OUT ,1
(2)    DO ,1 SUB #1 <- #134
(1)    PLEASE ABSTAIN FROM (2)
```

#### Beeswax

C'est un langage conceptuellement intéressant, qui s'inspire du mouvement des abeilles autour des alvéoles pour le mouvement des pointeurs à travers les instructions.

Beeswax est capable d'arithmétique, de lecture/écriture de fichiers, et même de modifier son propre code source. Ci-dessous se trouve un programme qui calcule le [n-factoriel](https://rosettacode.org/wiki/Factorial#beeswax) (n!) d'un entier saisi par l'utilisateur.

```
       p      <
_1FT"pF>M"p~.~d
     >Pd  >~{;
```

#### Chef

C'est peut-être mon langage préféré parmi ceux que j'ai trouvés sur Rosetta Code. J'en avais déjà lu ailleurs, mais je n'avais pas vu quelque chose comme la gamme d'exemples fournis ici.

Contrairement à la plupart des langages de programmation, Chef se lit presque complètement naturellement, car chaque programme est formaté comme une recette (d'où le nom !). Pour être complet, il fait également référence aux variables, instructions et structures de données avec des noms liés à la cuisine, tels que 'mixing bowl', 'refrigerator', 'mix', 'chop', etc. Pourquoi pas ?

Voici un exemple de programme qui calcule la [somme et le produit](https://rosettacode.org/wiki/Sum_and_product_of_an_array#Chef) d'un tableau de nombres.

```
Sum and Product of Numbers as a Piece of Cake.
 
This recipe sums N given numbers.
 
Ingredients.
1 N
0 sum
1 product
1 number
 
Method.
Put sum into 1st mixing bowl.
Put product into 2nd mixing bowl.
Take N from refrigerator.
Chop N.
Take number from refrigerator.
Add number into 1st mixing bowl.
Combine number into 2nd mixing bowl.
Chop N until choped.
Pour contents of 2nd mixing bowl into the baking dish.
Pour contents of 1st mixing bowl into the baking dish.
 
Serves 1.
```

#### Golfscript

Familier aux fans de [code golf](http://codegolf.stackexchange.com/) (un hobby fantastiquement geek dans lequel les participants essaient de résoudre des énigmes de programmation avec le moins de bytes de code possible), Golfscript est un langage conçu pour faire beaucoup avec peu.

Il atteint certainement cet objectif et permet à ses utilisateurs de résoudre des énigmes complexes de manière très concise. Son [site web](http://www.golfscript.com/golfscript/index.html) nous indique que cette brièveté est atteinte en 'utilisant des symboles uniques pour représenter des opérations de haut niveau'.

L'utiliseriez-vous dans un environnement de production ? Peut-être, si vous étiez un golfeur de code expérimenté _et_ que vous n'aviez aucun égard pour la santé mentale de tout successeur à votre projet. Sinon... probablement pas.

Rosetta Code a plusieurs beaux exemples de Golfscript, et comme il arrive à être si concis, j'en ai inclus trois ici :

```
[2 4 3 1 2]$   #Sort an integer array

[296,{3/)}%-1%["No more"]+[" bottles":b]294*[b-1<]2*+[b]+[" of beer on the wall\n".8<"\nTake one down, pass it around\n"+1$n+]99*]zip    #99 Green Bottles Lyrics

[{"close"}100*]:d;
10,{)2?(.d<\["open"]\)d>++:d;}/
[100,{)"door "\+" is"+}%d]zip
{" "*puts}/    #100 Doors Challenge
```

#### Hoon

Hoon est fascinant en ce sens que, bien que certains le classeraient comme un esolang, il sert en fait un but pratique. Il peut être utilisé pour programmer des services web sur Urbit, qui se décrit comme un 'réseau sécurisé pair-à-pair de serveurs personnels'.

Jetez un coup d'œil à l'exemple du 'plus grand élément' ci-dessous.

Hoon est décrit comme étant de type Lisp, et notez les symboles à deux caractères au début de chaque ligne. Ces 'runes' sont utilisées à la place des mots-clés réservés, ce qui est un concept génial, mais qui affecte la lisibilité pour ceux qui ne sont pas familiers avec sa logique, et qualifie probablement Hoon comme quelque peu ésotérique.

```
:-  %say
|=  [^ [a=(list ,@) ~] ~]
:-  %noun
  (snag 0 (sort a gte))
  
> +max [1 2 3 ~]
3
```

#### Piet

De loin le langage le plus unique que j'ai rencontré était [Piet](http://www.dangermouse.net/esoteric/piet.html), nommé d'après l'artiste néerlandais du 20e siècle, Piet Mondrian.

Il suit un principe de conception très inhabituel : le code du programme doit être sous la forme d'art abstrait. Comment cela est-il réalisé ? La solution n'est rien de moins que géniale.

Les entiers sont représentés par le nombre de 'codels' dans un bloc de couleur contiguë. Le pointeur commence dans le coin supérieur gauche et se déplace autour de l'image. Chaque fois qu'il rencontre un changement de couleur, une instruction est exécutée. L'instruction exacte est spécifiée par les changements de teinte et de luminosité.

Esprit = Soufflé.

![Image](https://cdn-media-1.freecodecamp.org/images/veF-Yp6EL5gAJ745EtNpgfcJiBuACScZyqGa)
_'Hello World' via [Rosetta Code](http://rosettacode.org/wiki/Factorial#Piet" rel="noopener" target="_blank" title=")_

### Jouer avec les Tableaux

Une chose qui a attiré mon attention était le nombre de langages basés sur les tableaux qui existent. La [programmation basée sur les tableaux](https://en.wikipedia.org/wiki/Array_programming) existe depuis le début des années 1960, avec l'invention de APL, et bien qu'ils ne soient pas exactement grand public, il existe de nombreuses ramifications encore utilisées à divers degrés aujourd'hui. Ces langages ont tous beaucoup en commun, alors je vous épargnerai trop de détails, mais ils sont intéressants par leur concision.

#### J

J a été inventé par Kenneth Iverson, qui était également l'inventeur de APL. J est un langage très concis, vous permettant de faire beaucoup avec très peu de lignes de code.

Ci-dessous se trouve un [algorithme de clustering K-means](http://rosettacode.org/wiki/K-means%2B%2B_clustering). Pour comparaison, le même exemple en C s'étend sur 184 lignes.

```
NB.  Selection of initial centroids, per K-means++
   initialCentroids     =:  (] , randomCentroid)^:(<:@:]`(,:@:seedCentroid@:[))~
     seedCentroid       =:  {~ ?@#
     randomCentroid     =:  [ {~ [: wghtProb [: <./ distance/~
       distance         =:  +/&.:*:@:-"1  NB.  Extra credit #3 (N-dimensional is the same as 2-dimensional in J)
       wghtProb         =:  1&$: : ((%{:)@:(+/\)@:] I. [ ?@$ 0:)"0 1 NB.  Due to Roger Hui http://j.mp/lj5Pnt
 
   NB.  Having selected the initial centroids, the standard K-means algo follows
   centroids            =:  ([ mean/.~ closestCentroid)^:(]`_:`initialCentroids)
     closestCentroid    =:  [: (i.<./)"1 distance/
     mean               =:  +/ % #
```

#### K, q

Ces deux langages ont été développés commercialement par [Kx Systems](https://kx.com/). Tous deux sont des langages de type APL, basés sur les tableaux, qui ont des applications en finance et en big data. q est enveloppé autour de K et offre une lisibilité améliorée.

J'ai inclus quelques exemples de chacun ci-dessous. Ce sont des langages super concis et seraient sans doute bons pour une partie de code golf, si c'est ce que vous aimez.

```
/ 1-D Cellular automata in K
f:{2=+/(0,x,0)@(!#x)+/:!3}

/ Anagrams in K
{x@&a=|/a:#:'x}{x g@&1<#:'g:={x@<x}'x}0::`unixdict.txt

/ Pascal's Triangle in q
pascal:{(x-1){0+':x,0}\1}

/ 100 Doors Challenge in q
`closed`open (1+til 100) in `int$xexp[;2] 1+til 10
```

#### Klong

Klong est similaire à K et q, mais son [site web](http://t3x.org/klong/index.html) affirme qu'il est moins ambigu. Jugez par vous-même — ci-dessous se trouve une solution ["Middle Three Digits"](http://rosettacode.org/wiki/Middle_three_digits) écrite en Klong.

```
items::[123 12345 1234567 987654321 10001 -10001 -123 -100 100 -12345 1 2 -1 -10 2002 -2002 0]
 
mid3::{[d k];:[3>k::#$#x;"small":|0=k!2;"even";(-d)_(d::_(k%2)-1)_$#x]}
.p(mid3'items)
```

#### IDL

Un autre langage basé sur les tableaux pour vous. IDL (Interactive Data Language), existant depuis 1977, a été utilisé par des organisations comme la NASA et l'ESA. En fait, IDL s'est trouvé une niche dans la recherche spatiale, et il a déjà été utilisé pour aider les techniciens à réparer le télescope spatial Hubble.

Une application plus terre-à-terre est cette fonction qui génère un [triangle de Sierpinski](http://rosettacode.org/wiki/Sierpinski_triangle).

```
pro sierp,n
  s = (t = bytarr(3+2^(n+1))+32b)
  t[2^n+1] = 42b  
  for lines = 1,2^n do begin
        print,string( (s = t) )
        for i=1,n_elements(t)-2 do if s[i-1] eq s[i+1] then t[i]=32b else t[i]=42b
  end
end
```

### En Plein Essor ?

Bien sûr, certains langages ne voient pas beaucoup d'utilisation simplement parce qu'ils n'existent pas depuis très longtemps. Qu'ils prennent ou non dépend de divers facteurs, et la réalité est que la grande majorité ne verra pas une adoption généralisée. Mais il faut bien commencer quelque part, n'est-ce pas ?

Voici une sélection de langages des archives de Rosetta qui sont tous des nouveaux venus relatifs dans le domaine.

#### Crystal

[Ce projet](https://crystal-lang.org/) est encore en phase de test alpha, alors ne passez pas encore à celui-ci — mais gardez un œil dessus. Influencé par l'efficacité d'écriture de Ruby et l'efficacité d'exécution de C, les auteurs de Crystal semblent déterminés à produire un langage tout-en-un du meilleur des deux mondes. Le temps nous dira s'ils réussissent.

Ci-dessous se trouve un algorithme de 'tri rapide' écrit en Crystal — pourquoi ne pas essayer de [l'exécuter vous-même](https://play.crystal-lang.org/#/cr) ?

```
def quick_sort(a : Array(Int32)) : Array(Int32)
  return a if a.size <= 1
  p = a[0]
  lt, rt = a[1 .. -1].partition { |x| x < p }
  return quick_sort(lt) + [p] + quick_sort(rt)
end
 
a = [7, 6, 5, 9, 8, 4, 3, 1, 2, 0]
puts quick_sort(a)
```

#### Frege

La programmation fonctionnelle est la nouvelle grande tendance, et Frege est un langage purement fonctionnel introduit pour la première fois en 2011. Il a été décrit comme 'Haskell pour la machine virtuelle Java'. Nommé d'après le logicien mathématicien Gottlob Frege, ce langage compile vers Java et est également disponible pour [essayer en ligne](http://try.frege-lang.org/).

Ci-dessous se trouve une solution au défi des ["99 Bouteilles"](http://rosettacode.org/wiki/99_Bottles_of_Beer#Frege). Elle est pratiquement identique à la même solution en Haskell, ce qui est attendu.

```
module Beer where
 
main = mapM_ (putStrLn . beer) [99, 98 .. 0]
beer 1 = "1 bottle of beer on the wall\n1 bottle of beer\nTake one down, pass it around"
beer 0 = "better go to the store and buy some more."
beer v = show v ++ " bottles of beer on the wall\n"
                ++ show v
                ++ " bottles of beer\nTake one down, pass it around\n"
                ++ head (lines $ beer $ v-1) ++ "\n"
```

#### Futhark

Bien qu'il souffre d'un manque de documentation complète, le projet Futhark semble néanmoins être [une ligne de recherche prometteuse](https://futhark-lang.org/). L'objectif est de compiler vers du code de haute performance pour les unités de traitement graphique (GPU) — mais pas pour produire des sorties graphiques.

Au lieu de cela, le but de Futhark est de tirer parti de la puissance du GPU pour effectuer des procédures intensives en calcul qui prendraient autrement beaucoup plus de temps avec un langage plus conventionnel. Ci-dessous se trouve un exemple de fonction utilisée pour calculer une [moyenne géométrique](http://rosettacode.org/wiki/Arithmetic-geometric_mean#Futhark).

```
include futlib.numeric

fun agm(a: f64, g: f64): f64 =
  let eps = 1.0E-16
  loop ((a,g)) = while abs(a-g) > eps do
    ((a+g) / 2.0,
     F64.sqrt (a*g))
  in a
```

#### Sidef

Sidef approche sa quatrième année de développement actif, ayant commencé comme un projet en mars 2013. Il semble bien avancé et [très bien documenté](https://trizen.gitbooks.io/sidef-lang/content/), et compte plus de 600 exemples de solutions de codage sur Rosetta Code.

Sidef est principalement utilisé à des fins de recherche et cherche à explorer à la fois la programmation orientée objet et la programmation fonctionnelle. Personnellement, j'aime vraiment son apparence. L'exemple ci-dessous montre son utilisation pour trouver l'[intersection de deux lignes](http://rosettacode.org/wiki/Find_the_intersection_of_two_lines#Sidef).

```
func det(a, b, c, d) { a*d - b*c }
 
func intersection(ax, ay, bx, by,
                  cx, cy, dx, dy) {
 
    var detAB = det(ax,ay, bx,by)
    var detCD = det(cx,cy, dx,dy)
 
    var ΔxAB = (ax - bx)
    var ΔyAB = (ay - by)
    var ΔxCD = (cx - dx)
    var ΔyCD = (cy - dy)
 
    var x_numerator = det(detAB, ΔxAB, detCD, ΔxCD)
    var y_numerator = det(detAB, ΔyAB, detCD, ΔyCD)
    var denominator = det( ΔxAB, ΔyAB,  ΔxCD, ΔyCD)
 
    denominator == 0 && return 'lines are parallel'
    [x_numerator / denominator, y_numerator / denominator]
}

say ('Intersection point: ', intersection(4,0, 6,10, 0,3, 10,7))

> Intersection point: [5, 5]
```

#### Sparkling

Comme Sidef, ce langage a commencé en 2013. Sa conception a été inspirée par des caractéristiques de C, Python et Lua — et une aversion pour plusieurs caractéristiques de JavaScript.

Il vise à être un langage de script léger et extensible qui fonctionne presque partout. Ci-dessous se trouve un [jeu de devinette de nombres](http://rosettacode.org/wiki/Guess_the_number/With_feedback#Sparkling), que vous pouvez essayer de faire fonctionner dans votre navigateur [ici](https://h2co3.github.io/).

```
printf("Lower bound: ");
let lowerBound = toint(getline());
 
printf("Upper bound: ");
let upperBound = toint(getline());
 
assert(upperBound > lowerBound, "upper bound must be greater than lower bound");
 
seed(time());
let n = floor(random() * (upperBound - lowerBound) + lowerBound);
var guess;
 
print();
 
while true {
    printf("Your guess: ");
    guess = toint(getline());
 
    if guess < n {
        print("too low");
    } else if guess > n {
        print("too high");
    } else {
        print("You guessed it!");
        break;
    }
}
```

### L'Arche de Noé

Une autre catégorie pour vous — il y avait beaucoup de langages potentiels et je n'ai pas pu tous les passer en revue pour en extraire chaque exemple intéressant. Si vous en repérez que j'ai manqués, laissez une réponse ci-dessous !

Une chose que j'ai remarquée était que beaucoup de langages étaient nommés d'après des animaux. Y a-t-il une explication à cela ?!

Je ne vais pas entrer dans les détails, mais voici un rapide aperçu pour finir :

#### Chat, Chatons

Chat est décrit comme un langage fonctionnel, mais semble ne plus exister. Cependant, Kitten semble être actuellement [en développement](http://kittenlang.org/), et se présente comme un successeur de Chat. Fortement influencé par Haskell, mais vise à être plus accessible.

```
"Hello world!" writeln    //Chat

"Hello world!" say     //Kitten
```

#### Cobra

Langage OOP, influencé par Python, C#, Eiffel et Objective-C.

```
class Hello
    def main
        print 'Hello world!'
```

#### ><> ("Fish")

Un autre esolang multidimensionnel, si vous aimez ce genre de choses.

```
!v"Hello world!"r!
 >l?!;o
```

#### Héron

Inspiré par C++, Python et Pascal, mais aucun commit depuis 2012, donc il semble ne plus être en développement actif. Son seul exemple sur Rosetta est une solution détaillée au [problème des N-reines](http://rosettacode.org/wiki/N-queens_problem). Pour la brièveté, j'ai déduit un simple programme "Hello world!" à montrer ici à la place.

```
Main() {
   WriteLine("Hello world!");
}
```

#### Homard

Un langage de programmation de jeux qui vise à être facilement portable sur différentes plateformes. Il semble être en [développement actif](http://strlen.com/lobster).

```
print "Hello world!"
```

#### Panda

Le [site web](http://pandalang.org/) indique que Panda vise à être suffisamment simple pour qu'un Panda puisse le programmer. Je ne sais pas à quel point les Pandas sont bons en codage, donc je suis toujours dans le flou à ce sujet...

```
say("Hello world!")
```

#### Pony

Avec des influences allant de C++ à Erlang, Pony semble être un projet intéressant avec un [tutoriel complet](https://tutorial.ponylang.org/).

```
actor Main
  new create(env: Env) =>
    env.out.print("Hello world!")
```

#### Saumon

[Saumon](http://rosettacode.org/wiki/Category:Salmon) vise à mélanger l'écriture de code à la fois de bas niveau et de haut niveau.

```
"Hello world!"!

print("Hello world!\n");

standard_output.print("Hello world!\n");
```

#### Écureuil

[Écureuil](http://squirrel-lang.org/) est un langage de script léger qui a été intégré dans des jeux comme _Left 4 Dead 2_, _Portal 2_ et _CS:GO_.

```
print("Hello world!");
```

### Ouf !

C'était un tour d'horizon rapide ! Si vous êtes arrivé jusqu'ici et avez apprécié le voyage (ou repéré une erreur flagrante), laissez une réponse ci-dessous — j'essaierai de répondre dès que possible ! Merci d'avoir lu !

#### Si vous voulez approfondir :

* [Rosetta Code](http://rosettacode.org/wiki/Rosetta_Code)
* [PYPL](http://pypl.github.io/PYPL.html)
* [R-Fiddle](http://www.r-fiddle.org/)

Merci d'avoir lu !