---
title: Complexité Temporelle – Notation Big O
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-08-10T13:12:34.000Z'
originalURL: https://freecodecamp.org/news/learn-big-o-notation
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/BIGO2.png
tags:
- name: '#big o notation'
  slug: big-o-notation
- name: youtube
  slug: youtube
seo_title: Complexité Temporelle – Notation Big O
seo_desc: 'Big O notation is an important tools for computer scientists to analyze
  the cost of an algorithm. Most software engineers should have an understanding of
  it.

  We just published a course on the freeCodeCamp.org YouTube channel that will help
  you unders...'
---

La notation Big O est un outil important pour les informaticiens afin d'analyser le coût d'un algorithme. La plupart des ingénieurs logiciels devraient en avoir une compréhension.

Nous venons de publier un cours sur la chaîne YouTube freeCodeCamp.org qui vous aidera à comprendre la notation Big O.

Georgio Tunson, alias selikapro, a créé ce cours. Il fait un excellent travail en expliquant les concepts complexes avec des diagrammes et du code.

La notation Big O est une manière de décrire combien de temps un algorithme prend pour s'exécuter ou combien de mémoire est utilisée par un algorithme.

Voici les sections couvertes dans ce cours :

* Qu'est-ce que le Big O ?
* Explication O(n^2)
* Explication O(n^3)
* Explication récursive O(log n)
* Explication itérative O(log n)
* Qu'est-ce que la recherche binaire O(log n) ?
* Codage de la recherche binaire O(log n)
* Explication O(n log n)
* Codage du tri fusion O(n log n)
* Analyse approfondie de la complexité du tri fusion O(n log n)
* Explication avec Fibonacci O(2^n)
* Explication O(n!)
* Complexité spatiale et erreurs courantes

Regardez le cours complet ci-dessous ou sur [la chaîne YouTube freeCodeCamp.org](https://www.youtube.com/watch?v=Mo4vesaut8g) (2 heures de visionnage).

%[https://www.youtube.com/watch?v=Mo4vesaut8g]

## Transcription

(générée automatiquement)

La notation Big O est utilisée pour classer les algorithmes en fonction de leur croissance ou de leur déclin.

Il est très important de la comprendre pour de nombreux types de programmation. Giorgio Thompson fait un excellent travail en décomposant la notation Big O dans ce cours.

Hey, tout le monde, bienvenue dans ma mini-série sur la notation Big O.

Dans cette mini-série, vous apprendrez tout ce que vous devez savoir sur la notation Big O et comment vous pouvez l'utiliser pour améliorer votre capacité à créer des algorithmes efficaces.

J'utiliserai des illustrations sur tableau blanc pour vous aider à visualiser et à comprendre les concepts, suivies de tutoriels de codage que vous pourrez suivre pour solidifier votre compréhension des concepts. Nous répondrons à la question : qu'est-ce que la notation Big O ? Et pourquoi est-elle utile ? Alors, qu'est-ce que la notation Big O ? La notation Big O est utilisée pour analyser l'efficacité d'un algorithme lorsque son entrée approche l'infini, ce qui signifie que lorsque la taille de l'entrée de l'algorithme augmente, à quel point les exigences en termes d'espace ou de temps augmentent-elles avec elle.

Par exemple, supposons que nous avons un dentiste et qu'elle prend 30 minutes pour traiter un patient.

À mesure que sa file de patients augmente, le temps qu'il lui faut pour traiter tous les patients augmentera linéairement avec le nombre de patients attendant dans la file.

C'est parce qu'il lui faut toujours un temps constant pour traiter chaque patient individuel, soit 30 minutes.

Cela nous donne une compréhension générale de combien de temps notre dentiste prendrait pour traiter 10 patients, 20 patients ou même 100 000 patients.

C'est parce que, puisque nous savons que le dentiste prend un temps constant, soit 30 minutes pour traiter chaque patient, nous pouvons toujours calculer le temps qu'il lui faudrait pour traiter un nombre quelconque de patients en multipliant le nombre de patients par 30 minutes.

Avec cela à l'esprit, nous pouvons catégoriser son efficacité comme étant linéaire.

Ou comme nous le dirions en termes de Big O, big O de n, où n est égal au nombre de patients. Le temps qu'il lui faut pour terminer son travail augmente linéairement ou proportionnellement avec le nombre de patients. Nous utilisons la même technique pour déterminer l'efficacité des algorithmes. Nous pouvons nous faire une idée générale de la manière dont l'efficacité temporelle des fonctions augmente en catégorisant l'efficacité d'une fonction donnée de la même manière que nous catégorisons l'efficacité du dentiste.

Créons une fonction facilement compréhensible qui augmente de manière similaire au dentiste.

Donc, cette fonction est dans la même catégorie linéaire que notre dentiste. Passons en revue et découvrons pourquoi.

Pour commencer, l'entrée de notre fonction est un tableau avec sept éléments à l'intérieur.

Pour chacun de ces éléments, nous allons enregistrer cette expression qui multiplie 1000 fois 100 000.

Maintenant, ne vous laissez pas intimider par ces grands nombres. Il faudra toujours le même temps pour multiplier 1000 fois 100 000.

Par conséquent, cette ligne de code prend un temps constant.

Ce qui m'amène à un point très important : lors de la considération de l'efficacité d'une fonction.

Ces lignes qui prennent un temps constant n'ont pas d'importance.

Eh bien, au moins pour nos besoins, elles n'en ont pas.

C'est parce que si notre tableau avait une longueur folle, comme 200 millions, changer cette expression en quelque chose de plus simple, comme un plus un, aurait un effet négligeable sur l'efficacité de la fonction dans son ensemble. Nous devrions toujours itérer à travers 200 millions d'éléments dans un tableau.

En fait, même si la fonction ressemblait à ceci, nous ignorerions toujours toutes ces constantes et dirions que cette fonction augmente linéairement ou est big O de n.

De même, si nous repensons à notre exemple de dentiste, nous voyons qu'elle prenait 30 minutes par patient.

Mais même si elle prenait trois heures par patient, le temps qu'il lui faut pour voir tous ses patients augmentera toujours linéairement.

Cela peut être difficile à comprendre au début, mais cela commence à avoir du sens avec le temps.

Dans la dernière diapositive, il y avait beaucoup de discussions sur l'ignorance des constantes.

Mais qu'est-ce qu'une constante exactement ? Une constante est toute étape qui ne s'adapte pas à l'entrée de la fonction.

Par exemple, le temps pour évaluer cette expression ne change pas avec l'entrée car 101 000 sont des constantes.

C'est-à-dire que ces valeurs sont toujours les mêmes, cette expression donne toujours le même résultat.

Et il faut toujours le même temps ou un temps constant pour retourner le même résultat.

Tout comme nous utilisons big O de n pour décrire les fonctions linéaires.

Nous avons aussi un nom big O pour les algorithmes constants, qui est big O de un.

Une bonne façon d'y penser est que chaque ligne de code est en fait une fonction en soi, ce qui est en fait vrai.

Par exemple, réintroduisons cette fonction.

Donc, cette ligne de code est la raison pour laquelle toute la fonction linear func est O de n, car comme vous pouvez le voir, à mesure que la taille de n augmente, le nombre d'itérations que la boucle for doit parcourir augmente également.

Mais prenons en considération cette deuxième ligne.

Faisons semblant, pour une seconde, que nous avons une fonction qui ne contient que cette ligne.

Maintenant, comme vous pouvez le voir, avec cette fonction, nous passons un tableau, mais la fonction ne fait rien avec le tableau.

La seule opération dans la fonction est constante car elle ne s'adapte pas à une entrée.

Donc, peu importe la taille du tableau passé à cette fonction, cette ligne produit toujours le même résultat.

Et c'est la seule ligne dans la fonction.

Donc, par conséquent, toute cette fonction est sur un.

Mais attendez.

Dans cette fonction, nous avons plusieurs lignes qui sont sur un, mais nous priorisons toujours la ligne qui est O de n et ignorons les opérations O de un.

Pourquoi est-ce le cas ? Eh bien, cela nous amène à notre dernière note importante, en bego, nous avons une hiérarchie de croissance, qui ressemble à ceci.

Maintenant, ne paniquez pas, vous n'avez pas besoin de tout comprendre pour l'instant.

Donc, concentrons-nous uniquement sur ceux qui sont pertinents pour cette vidéo, ou même un ancien.

Nous apprendrons les autres dans les vidéos suivantes de cette série.

Ce graphique montre les catégories d'efficacité par ordre du meilleur au pire.

C'est-à-dire que ce premier cas de un est le meilleur cas.

Et ce dernier est le pire cas.

En notation Big O, lors de la détermination de l'efficacité d'un algorithme, nous ne nous intéressons qu'au pire cas.

Cela signifie que le pire cas où l'opération de l'ordre le plus élevé prime sur les opérations qui ont de meilleures performances.

Donc, si nous additionnons les performances de toutes ces lignes, comme ceci, toutes les lignes de code qui sont o de un sont annulées car oh Vin est la partie la plus mal performante ou de l'ordre le plus élevé de la fonction.

Et cela, mesdames et messieurs, est pourquoi nous ignorons les constantes, car nous éliminons en fait les éléments non dominants.

Parce que, lorsque l'entrée d'une fonction tend vers l'infini, les constantes deviennent de moins en moins significatives.

Donc, pour récapituler, lors de l'évaluation de l'efficacité d'un algorithme, nous devons prendre en considération l'efficacité de chaque étape de l'algorithme, nous trouvons ensuite l'étape de l'ordre le plus élevé, ou l'étape qui a la pire performance, et nous la priorisons par rapport à toutes les étapes mieux performantes, les étapes qui sont constantes, ou qui sont sur un ou aussi bonnes que possible en termes d'efficacité.

Donc, nous les ignorons toujours, sauf si la totalité de la fonction est constante, ou o de un.

Et dans ce cas, nous catégoriserions toute la fonction comme constante ou o de un.

Et cela, mesdames et messieurs, est votre réponse à la question : qu'est-ce que la notation Big O.

D'accord, donc pour comprendre O de n carré, nous allons devoir prendre en considération la fonction qui ressemblera à ceci.

Donc, ce que fait cette fonction, c'est qu'elle prend un nombre et qu'elle itère à travers cette boucle for en commençant par le nombre zéro jusqu'au nombre n, et pour chaque itération de cette boucle for supérieure, nous allons également parcourir cette boucle for imbriquée.

Et cette boucle for imbriquée fait exactement la même chose que cette boucle for.

Elle itère à travers chaque nombre, en commençant par zéro jusqu'au nombre n, et dans cette boucle for imbriquée, nous enregistrons les coordonnées d'une cellule dans une matrice.

Mais pour simplifier les choses, au lieu d'illustrer une journalisation de la console de l'index i et j, je vais simplement dessiner un carré où ces coordonnées devraient être pour chaque itération de cette boucle for imbriquée.

Donc, si cela semble confus, essayez de rester avec moi, je promets que cela deviendra clair.

D'accord, donc disons par exemple que nous appelons la fonction carré avec le nombre quatre.

Donc, cela signifie que nous allons itérer à travers cette boucle for supérieure en commençant par zéro, puis nous allons itérer jusqu'à ce que I ne soit plus inférieur à quatre, une fois que I devient égal à quatre, alors nous arrêterons l'itération.

Et ce n'est que pour cette boucle for supérieure. Pour chaque itération de cette boucle for réelle, nous allons parcourir l'intégralité de cette boucle for imbriquée et faire cette journalisation de la console.

Et au lieu d'enregistrer les coordonnées, comme je l'ai dit, nous dessinerons un carré où les coordonnées seraient, afin que vous puissiez mieux visualiser cela.

Donc, allons-y et commençons.

Donc, pour la première itération, i va être égal à zéro, et ensuite nous passons à cette boucle for imbriquée.

Et ensuite, nous allons itérer à travers l'intégralité de cette boucle for imbriquée.

Donc, maintenant, i et j sont à zéro, donc i et j sont tous les deux à zéro.

Donc, nous sommes actuellement à la première itération de cette boucle for et à la première itération de cette boucle for, et nous dessinerons un carré, puis nous passerons à une itération de cette boucle for, donc j devient un et nous dessinerons un autre carré.

Et ensuite, j devient deux, il dessine un autre carré, puis j devient trois, et nous dessinerons un autre carré, et maintenant j est quatre.

Et puisque j est quatre, cela signifie que j n'est plus inférieur à n, car n est quatre, et j est quatre, et n est quatre.

Donc, j et n sont maintenant égaux, donc nous n'itérerons plus à travers cette boucle for.

Donc, maintenant, nous retournons à cette boucle for.

Et maintenant, i est égal à un, donc i est égal à un, et j est égal à zéro, donc nous dessinerons un carré, puis i est égal à un et j est égal à un, donc nous dessinerons un carré, puis i est égal à un et j est égal à deux.

Donc, nous dessinerons un carré et i est égal à un et j est égal à trois, il dessine un carré.

Et maintenant, nous revenons à cette boucle for supérieure, car j et n sont maintenant égaux, nous sommes de retour à cette boucle for supérieure, maintenant i est égal à deux, donc i est égal à deux, et j est égal à zéro, donc nous dessinerons un carré, puis i est égal à deux, et j est égal à un, donc nous dessinerons un carré, et i est égal à deux, et j est égal à deux.

Donc, nous dessinerons un carré, et i est égal à deux, et j est égal à trois, donc nous dessinerons un carré, et maintenant j est égal à quatre, qui est notre n, donc nous n'itérerons plus à travers cette boucle for imbriquée, et nous remonterons au sommet de cette boucle for, maintenant, i est égal à trois, i est égal à trois à ce stade, et j est égal à zéro à nouveau, donc nous dessinerons un carré égal à trois et j est égal à un.

Donc, nous dessinerons un carré, j est égal à deux, j est égal à trois.

Et ensuite, j est égal à quatre.

Donc, nous n'itérerons plus à travers cette boucle for imbriquée.

Et à ce stade, notre i est maintenant égal à quatre et notre n est également égal à quatre.

Et nous n'itérons à travers cette boucle for supérieure que tant que r est inférieur à n, mais nos yeux sont maintenant égaux à notre n.

Donc, maintenant, nous arrêtons d'itérer à travers cette boucle for supérieure.

Et ce qui nous reste est cette matrice ici.

Et la raison pour laquelle j'ai dit que ce sont les coordonnées des cellules dans une matrice est parce que ceci est une matrice.

Et ce sont des lignes.

Et ce sont des colonnes.

Donc, nous pouvons considérer AI comme étant notre colonne.

Et ensuite, nous pouvons considérer j comme étant la ligne.

Donc, pour chaque itération 0123 de notre colonne, nous avons également une itération pour la ligne 0123.

Donc, les coordonnées étant zéro et zéro, étaient les coordonnées de ce carré, puis zéro et un sont les coordonnées de ce carré, et zéro et deux sont les coordonnées de ce carré, et ainsi de suite.

Donc, qu'est-ce que tout cela a à voir avec oben square ? Eh bien, hey, juste une rapide interruption.

Si vous trouvez cette vidéo utile, ou qu'elle vous apporte une certaine compréhension, prenez le temps de liker et de vous abonner.

Si nous y réfléchissons, il s'agit d'une matrice carrée, c'est-à-dire que chaque côté aura la même longueur.

Et par longueur, je veux dire 1234.

Cela a une longueur de quatre, et 1234.

Et cela a une longueur de quatre, et pour trouver l'aire d'un carré, nous devons simplement multiplier la longueur d'un côté par elle-même, car chaque côté d'un carré a la même longueur.

Donc, si c'était un rectangle, nous multiplierions la largeur par la hauteur, mais pour un carré, nous pouvons simplement multiplier par lui-même car la largeur et la hauteur auront la même longueur.

Donc, pour obtenir l'aire de ce carré, nous allons simplement multiplier quatre fois quatre, quatre fois quatre.

Et cela va être égal au nombre de cellules dans cette matrice, ce qui se trouve être également le nombre de fois que nous avons dû exécuter ce code, qui est quatre fois quatre, soit 16.

Et quatre fois quatre est la même chose que quatre au carré.

Donc, O de n au carré, notre n est en fait quatre.

Et c'est pourquoi généralement les fonctions avec des boucles for imbriquées, comme une boucle for et une boucle for imbriquée à l'intérieur comme cette fonction est considérée comme O de n au carré.

J'espère que cela a du sens.

D'accord, donc pour comprendre O de n cube, prenons une fonction en considération.

Cette fonction cube prend un argument n qui est un nombre.

Et elle va itérer à travers cette boucle for et pour chaque itération de cette boucle for, elle va itérer à travers l'intégralité de cette boucle for.

Et pour chaque itération de cette boucle for, nous devrons itérer à travers l'intégralité de cette boucle for.

Et je dois m'excuser à l'avance pour mes compétences en dessin décevantes.

Mais pour illustrer cela, je vais en fait devoir dessiner des formes tridimensionnelles, ce qui n'est pas quelque chose que je maîtrise entièrement. Mais en tout cas, pour l'instant, ignorons cette image.

Pour l'instant.

Concentrons-nous sur cette fonction.

Donc, pour la boucle for de niveau supérieur, nous allons itérer jusqu'à n.

Donc, si nous passons le nombre quatre à notre fonction cube, nous allons finir ici à cette première boucle for.

Et nous allons itérer en commençant par zéro jusqu'à n, qui est quatre.

Donc, commençons.

Donc, pour notre première itération de cette boucle for de niveau supérieur, i va être zéro.

Maintenant, pour tout le cube, nous ajoutons une boucle for imbriquée supplémentaire.

Donc, il n'y a plus seulement une ligne et une colonne.

Maintenant, nous avons des lignes, des colonnes.

Et nous avons aussi cette troisième dimension ici, que nous appellerons simplement hauteur.

Donc, nous avons les colonnes qui vont dans cette direction, les lignes qui vont dans cette direction, et la hauteur qui va dans cette direction.

À ce stade, nous travaillons avec un tableau tridimensionnel, ce n'est plus un tableau bidimensionnel.

Et c'est le même concept.

Donc, ce n'est pas aussi difficile qu'il y paraît, nous allons le dessiner maintenant.

Donc, nous commencerions avec cette boucle for initiale, et n va commencer à zéro, n'est-ce pas.

Et nous pourrions dire que cette boucle for initiale est représentative de nos colonnes.

Donc, nous pouvons en fait aller de l'avant et écrire ces nombres juste pour que vous puissiez voir.

Donc, nous dirons que lorsque i est zéro, cette colonne est zéro.

Lorsque i est un, nous parlons de cette colonne.

Lorsque i est deux, nous parlons de cette colonne, et lorsque i est trois, nous parlons de cette colonne.

Et bien sûr, une fois que i devient quatre, nous n'allons plus itérer à travers cette boucle for car i n'est alors plus inférieur à n, qui est quatre, il sera égal à quatre.

Et nous pouvons dire la même chose pour les lignes.

Donc, nous dirions que la ligne zéro serait ici, la ligne un serait ici, la ligne deux serait ici, et la ligne trois serait ici.

Maintenant, je m'excuse si cela est difficile pour vous à voir, c'est en trois dimensions.

Donc, ce n'est pas vraiment facile à dessiner, mais j'espère que vous pouvez visualiser ce que j'essaie de dire.

Et puis la même chose pour la hauteur, la hauteur serait représentée par cette boucle for ici.

Donc, d'accord, et voyons en fait, je suis désolé, je devrais, je devrais en fait juste nommer celles-ci par la lettre que nous utilisons dans la fonction réelle.

Donc, au lieu d'appeler cela hauteur, nous appellerons cela K.

Parce que c'est représentatif, cette boucle for est représentée comme représentant k ici, donc nous l'appellerons simplement k aussi.

Et au lieu d'appeler cela colonnes, nous l'appellerons AI.

Et au lieu d'appeler cela rose, nous l'appellerons J.

Donc, pour chaque itération de cette boucle for, nous allons nous déplacer vers le haut de cet axe k.

Donc, si nous devions écrire ce qu'est l'index pour K, cela serait un peu difficile à voir maintenant.

Mais ce sera 012.

Et trois, donc essayons de dessiner cela.

Donc, faisons cela étape par étape pendant un petit moment pour que vous compreniez ce qui se passe.

Donc, pour cette première itération de cette boucle for de niveau supérieur, i va être égal à zéro.

Donc, cela signifie que I, cette ligne, nous allons être ici à l'index zéro de I.

Et ensuite, pour cette boucle for imbriquée, J va également être égal à zéro.

Donc, j est ici.

Et nous allons être à zéro ici.

Donc, nous allons toujours être ici.

Et pour K aussi, cette boucle for ici.

Cette x est ici, nous allons également être à zéro, qui est ici.

Donc, nous allons toujours être ici.

Donc, au lieu de journaliser ces coordonnées, nous allons simplement dessiner un carré pour cette coordonnée.

Donc, cette coordonnée est 00, et zéro, et 00, et zéro, donc nous allons simplement dessiner un carré ici.

Et encore une fois, vous allez devoir excuser ma mauvaise maîtrise du dessin de carrés.

Et puisque nous continuons avec K jusqu'à ce que K ne soit plus inférieur à n, nous allons continuer à itérer à travers cette boucle for.

Donc, pour vous aider, je peux juste dire, je peux juste écrire I maintenant est égal à zéro, J maintenant est égal à zéro et K.

Il était égal à zéro, mais nous venons de faire le carré pour K à zéro.

Donc, maintenant K va itérer, il va incrémenter de un.

Donc, K va maintenant être égal à un.

Donc, lorsque k est à un, et j est à zéro, et est à zéro, donc i j.

k est à un, alors nous allons monter d'un autre carré et cela va être un peu difficile à voir parce que je dessine littéralement un espace tridimensionnel alors que je suis ici et je suis juste nul en dessin, je ferai de mon mieux.

Donnez-lui une autre chance.

D'accord, donc une fois que nous faisons cela, k incrémente de un, donc K est maintenant deux, deux est ici, et ensuite i et j sont toujours zéro, donc nous allons toujours être à j ici.

Donc, nous allons toujours être dans cette section.

Donc, nous dessinerons un autre carré bidimensionnel ici.

Je veux dire, un cube bidimensionnel, excusez-moi, si j'appelle un cube carré, ce n'est définitivement pas correct.

Donc, il y a un autre cube.

Et bien sûr, K va incrémenter à nouveau.

Donc, K va devenir trois.

Et ensuite à trois ici, nous dessinerons un autre carré, je veux dire, un cube, désolé.

Et à ce stade, K va incrémenter.

Et ensuite, il va être égal à quatre.

Et une fois que k est égal à 4, k n'est plus inférieur à n, car n est aussi quatre.

Donc, maintenant k est égal à n.

Donc, ce monde est terminé.

Et maintenant, nous passons à cette boucle for.

Et cette boucle for va incrémenter de un et j sera alors égal à un, car pour chaque itération de cette boucle for, nous passons par l'intégralité de cette boucle for.

Donc, nous avons passé par l'intégralité de cette boucle for.

Donc, maintenant, nous pouvons passer à une itération dans cette boucle for.

Et nous ne pouvons pas remonter à cette boucle for jusqu'à ce que nous ayons itéré à travers tout ce qui se trouve dans cette boucle for.

Donc, nous sommes toujours sur, donc nous n'incrémentons que la ligne et ensuite nous revenons à l'itération de K.

Donc, maintenant que j est égal à un, i est toujours zéro, donc nous sommes toujours ici, nous sommes toujours ici, car c'est la colonne et ensuite i est toujours zéro, c'est I et i est toujours zéro.

Et nous sommes toujours ici, mais j est passé de zéro à un.

Donc, maintenant nous sommes ici.

Donc, nous sommes de retour dans k, et k va commencer à zéro à nouveau.

Donc, à I étant zéro, J étant un et K étant zéro, car zéro, d'accord, c'est K, et c'est zéro.

Et nous sommes ici, nous dessinerons un carré.

Désolé, encore une fois, j'ai dit carré, oui, nous dessinerons un cube.

Et ensuite k incrémente, et nous dessinerons un autre cube.

Et ensuite k incrémente.

Un autre cube, car une fois que k atteint quatre, donc oui, K, d'accord, nous incrémenterons une fois de plus, et il atteindra quatre.

Et maintenant K n'est plus inférieur à n.

Donc, nous remontons à la boucle for RJ, et celle-ci incrémentera de un.

Donc, celle-ci deviendra maintenant deux.

Et c'est à peu près la même chose.

Tout au long de la fonction entière, et il devient difficile de voir les cubes que je dessine ici.

Mais finalement, nous arriverons à un point où le cube entier est rempli, ce qui ressemblera à ceci.

Donc, nous arriverons à un point où la totalité de ce cube serait rempli avec ces cubes miniatures, qui sont juste les itérations de ces quatre boucles.

Donc, une fois que nous arrivons à ce point, et merci, le cube est complètement rempli.

À ce stade, cela signifie que nous avons itéré à travers l'intégralité de cette boucle for de niveau supérieur.

Et n'hésitez pas à prendre le temps d'essayer de dessiner cela par vous-même.

Mais j'ai essentiellement parcouru autant que possible avec le temps que j'ai dans cette vidéo, mais c'est à peu près la même chose jusqu'à ce que la totalité du cube soit remplie.

Donc, une fois que toutes ces quatre boucles sont terminées, vous serez laissé avec le cube qui ressemble à ceci.

Et puisque ceci est un cube, cela signifie que sa hauteur, sa longueur et sa largeur seront toutes de la même longueur.

Et cela signifie qu'elles seront toutes égales à n, car si vous regardez ici, nous avons parcouru n itérations de J.

Nous avons parcouru des itérations de AI et nous avons parcouru n itérations de K.

Et encore une fois, je suis désolé pour mon mauvais dessin, j'espère que vous comprenez l'idée.

Donc, si n est quatre, cela va être quatre, cela va être quatre, et cela va être quatre.

Et pour obtenir le volume de ce cube, pour obtenir le volume, l'espace à l'intérieur de ce cube, puisque nous savons que tous ceux-ci vont être les mêmes, nous n'avons besoin de connaître qu'un seul d'entre eux.

Et l'un d'entre eux pour obtenir le volume, nous faisons simplement pour ce cas, pour le cube, et quatre cubé est 64.

Et ce sera le volume de ce cube, ce qui signifie simplement qu'il y a 64 de ces cubes miniatures dans ce cube plus grand.

Et c'est le volume.

Donc, O de n cubé, r n est quatre.

Donc, o de quatre cube, ce qui est égal à 64, ce qui est le volume de ce cube.

Ce qui se trouve également être le nombre de fois où nous aurions exécuté cette fonction de journalisation des coordonnées, mais dans notre cas, nous avons simplement fait les carrés.

Et c'est pourquoi cette fonction est O de n cube doit d'abord comprendre ce qu'est un logarithme.

Simplement dit, un logarithme est la puissance à laquelle un nombre doit être élevé pour obtenir un autre nombre.

Je sais que cela n'a pas beaucoup de sens hors contexte, mais ne vous inquiétez pas, je vous ai couvert.

Prenons le nombre huit en considération.

Donc, nous voulons élever un nombre à une certaine puissance pour obtenir un PhD.

En informatique, sauf indication contraire, nous pouvons toujours supposer que le nombre que nous voulons élever à une certaine puissance est deux.

Donc, réécrivons cela.

Donc, nous voulons élever deux à une certaine puissance pour obtenir huit.

Donc, cette même équation peut être écrite comme ceci, ou ce deux ici est appelé la base.

Et n'oublions pas qu'en informatique, la base est toujours deux.

Donc, pour trouver la réponse à cela, nous devons simplement trouver la réponse à cela.

Avec cela à l'esprit, nous pouvons voir que si nous élevons deux à la puissance de trois, nous obtenons le nombre que nous cherchons, huit, donc log base deux de huit est trois.

Donc, avec tout cela à l'esprit, passons à la signification de Oh login.

Pour cette partie, nous utiliserons une fonction récursive très basique pour visualiser Oh login, mais ne vous inquiétez pas, je vous guiderai à travers chaque étape.

Restez avec moi.

Donc, nous commencerons avec un nombre et nous utiliserons huit afin que vous puissiez facilement voir comment cela se rapporte à notre explication des logarithmes dans la diapositive précédente.

Donc, cette variable in, nous allons la passer à notre fonction récursive qui ressemble à ceci.

Donc, la complexité temporelle de cette fonction est Oh, log in, creusons plus profondément pour découvrir pourquoi.

Pour l'instant, ignorons simplement cette première ligne et concentrons-nous sur ce que la fonction fait réellement.

Donc, lorsque nous passons un nombre dans cette fonction, elle divise in par deux ou le divise en deux, puis s'appelle elle-même avec la nouvelle moitié ou le nombre divisé.

Visualisons cela à l'aide du graphique.

Donc, nous appelons d'abord la fonction avec la valeur huit, ce huit est ensuite divisé par deux.

La fonction prend alors le résultat de la division et le passe récursivement à elle-même comme nouvelle valeur pour n, ce qui entraîne que nous descendons d'un niveau.

Nous faisons ensuite la même chose avec notre nouvelle valeur pour n qui est quatre, ce quatre est divisé par deux, ce qui donne un nouveau n.

Et la fonction passe ensuite notre nouvelle valeur pour n à un appel récursif à elle-même à nouveau, ce qui entraîne que nous descendons d'un niveau supplémentaire.

Nous faisons ensuite la même chose avec notre valeur la plus récente pour n qui est deux, nous le divisons par deux et la fonction s'appelle à nouveau récursivement à ce niveau, nous allons nous arrêter car nous ne pouvons plus diviser in sans obtenir des fractions comme résultat.

Maintenant, nous sommes arrivés au début du secret pour comprendre Oh login, alors regardez attentivement.

Si vous regardez notre graphique, vous verrez que nous sommes allés un à trois niveaux de profondeur.

Si vous vous souvenez de notre diapositive précédente, le log base deux de huit est trois.

Notre entrée in est huit et nous sommes allés trois niveaux de profondeur.

Vous remarquerez également que nous devons élever deux à la puissance de trois ou multiplier deux fois deux fois deux pour obtenir huit.

Et puisque la division est simplement l'inverse de la multiplication, nous pouvons voir que lorsque nous faisons quelque chose comme ceci.

Donc, cela signifie que cette fonction a une complexité temporelle de Oh, login.

Pourquoi ? Parce que notre n est huit.

Et en informatique, notre base est toujours deux.

Et nous devons avoir notre n trois fois ou aller trois niveaux de profondeur dans notre fonction récursive pour arriver à un point où nous ne pouvons plus raisonnablement avoir notre entrée in, ce qui est une autre façon de dire que log base deux de huit est égal à trois.

Et cela, mesdames et messieurs, est le secret pour comprendre la complexité temporelle Oh, login.

Et en tant que note rapide, cela ne s'applique pas seulement aux fonctions récursives.

Et si vous êtes curieux à propos de cette ligne de code que nous avons couverte plus tôt, tout ce qu'elle fait est de s'assurer que nous avons arrêté de diviser in lorsque n devient un, sinon la fonction continuerait à diviser fraction après fraction jusqu'à ce que nous dépassions éventuellement la taille maximale de la pile d'appels.

Donc, nous allons commencer avec une fonction très simple, qui ne contient qu'une boucle while qui attribue une nouvelle valeur à la variable in pour chaque itération.

Et pour cet exemple, imaginons que nous passons la valeur huit à notre fonction in.

Donc, cela signifie que nous allons itérer à travers cette boucle while tant que huit est supérieur à un.

Et pour chaque itération de cette boucle while, nous allons diviser notre n par deux et le réattribuer à n.

Donc, notre n va être divisé par deux pour chaque itération.

Donc, actuellement, notre n est égal à huit, car nous avons passé huit comme in et tant que n est supérieur à un, nous allons itérer.

Donc, maintenant, c'est huit, ce qui est supérieur à un.

Donc, nous allons faire ce math dot floor n divisé par deux pour notre première itération, ce qui définirait notre n égal à huit divisé par deux, ce qui est quatre.

Et ce math dot floor, tout ce qu'il fait, c'est qu'il arrondit le résultat de notre division.

Par exemple, si nous avons math dot floor, cinq divisé par deux, nous obtiendrions deux ici, au lieu de 2,5.

Donc, après cette première itération, notre in est maintenant égal à quatre.

Donc, tant que n est supérieur à un, nous allons faire une autre itération.

Donc, quatre est supérieur à un, donc nous allons faire cela à nouveau.

Et n va être égal à quatre divisé par deux, ce qui va être égal à deux.

Donc, maintenant, notre n est égal à deux.

Et tant que n est supérieur à un, nous allons faire cela à nouveau.

Donc, in est actuellement supérieur à un, deux est supérieur à un.

Donc, nous allons le faire à nouveau pour la troisième itération.

Donc, in va être égal à deux divisé par deux, ce qui va être égal à un.

Donc, à ce stade, notre n est égal à un.

Et nous allons revenir à cette condition ici à nouveau.

Donc, tant que in est supérieur à un, nous allons faire cela.

Mais maintenant, n est égal à un, il n'est plus supérieur à un.

Donc, nous n'allons pas continuer avec cette boucle while.

Donc, pourquoi cette fonction est-elle de login ? Donc, notre n est huit.

Donc, cela signifie que cette fonction devrait être o de log huit.

Et si vous vous souvenez de la vidéo précédente sur la complexité old login, c'est la même chose que o de log base deux, huit, ce qui signifie simplement quelle puissance devons-nous élever pour acheter huit.

Et si nous écrivons cela, quelle puissance devons-nous élever pour acheter huit, nous voyons que nous devons élever deux à la troisième puissance pour obtenir huit, car deux fois deux fois deux est égal à huit.

Donc, ce trois est ce qui est important, car la division est simplement l'inverse de la multiplication.

Donc, si nous devons multiplier deux fois deux fois deux pour obtenir huit, alors nous devrions également pouvoir diviser huit par deux trois fois pour obtenir un.

Donc, il y a 123.

Donc, cela signifie que pour cette fonction, lorsque nous passons une valeur pour n, nous allons toujours devoir diviser cette valeur in par deux log in fois avant de pouvoir obtenir un, ce qui est simplement une autre façon de dire que lorsque nous passons dans cette fonction, nous allons itérer à travers cette boucle while, log in itérations, avant d'obtenir la valeur un.

Donc, si vous voyez ici, nous avons une itération, deux itérations, trois itérations.

Donc, il y a trois itérations ici.

Donc, ce trois est log in itérations.

Parce que encore une fois, oh, tout log in, signifie simplement Oh, log base deux de huit.

Parce que notre n est un, n, log base deux de huit est trois, parce que deux à la puissance de trois est égal à huit, ce qui est notre n.

Et c'est pourquoi cette fonction non récursive est oh log in, parce qu'il y aura log in itérations 123.

Avant que cette boucle while ne se termine.

J'espère que cela a du sens.

Pour commencer, nous devrions comprendre que pour que la recherche binaire fonctionne, le tableau que vous recherchez doit être un tableau ordonné, à la fois en ordre croissant et décroissant, deux tableaux fonctionneront.

Commençons par visualiser notre tableau.

En pratique, cela est beaucoup plus utile à mesure que la taille d'un tableau devient beaucoup plus grande, mais nous allons nous en tenir à un tableau contenant neuf éléments pour nous aider à comprendre le concept plus clairement.

Donc, supposons que nous voulons vérifier notre tableau pour voir si la valeur 100 existe à l'intérieur du tableau.

La solution naïve serait d'itérer à travers chaque élément du tableau en vérifiant si la valeur est égale à 100, comme ceci.

Mais pour cette méthode, nous devons itérer à travers chaque élément du tableau jusqu'à la valeur que nous recherchons.

Et si nous devons faire cela pour un tableau contenant 1000, ou 100 000, ou même un million d'éléments.

C'est là que quelque chose comme la recherche binaire peut être utile.

Donc, essayons à nouveau.

Donc, ici, nous voulons toujours vérifier si la valeur 100 est dans notre tableau.

Mais cette fois, nous utiliserons la recherche binaire pour le découvrir.

Pour commencer, nous devons trouver le point médian de notre tableau, qui est simplement l'élément au milieu de notre tableau, notre point médian est ici.

Maintenant, puisque notre tableau est en ordre croissant, nous savons que tout ce qui se trouve à droite de notre point médian sera une valeur supérieure à notre point médian.

Et tout ce qui se trouve à gauche de notre point médian sera une valeur inférieure à notre point médian.

Donc, nous devons déterminer si ce nombre 100, que nous recherchons, est supérieur ou inférieur à notre point médian.

Cela nous indiquera de quel côté de notre tableau se trouve notre nombre.

Donc, si nous écrivons simplement 43 est inférieur à 100, nous pouvons en fait voir que le côté du tableau où se trouve notre nombre est ce côté.

Pour brosser un tableau complet, faisons semblant pendant une seconde que le nombre que nous recherchons est deux et non 100.

Dans ce cas, deux serait inférieur à notre point médian 43.

Par conséquent, il sera du côté gauche.

Et cela, mesdames et messieurs, est pourquoi la recherche binaire ne fonctionnera que sur des tableaux ordonnés.

Car sans l'ordre, il n'y aurait aucun moyen de savoir de quel côté se trouve le nombre que nous recherchons en le comparant au point médian.

Maintenant, revenons au nombre original que nous utilisions pour notre exemple.

Donc, maintenant que nous savons que 100 sera du côté droit de notre point médian, nous pouvons complètement nous débarrasser de tout ce qui se trouve à gauche du point médian, y compris le point médian.

Donc, ce qui nous reste est ceci, ce que nous avons fait, c'est que nous avons essentiellement coupé le tableau en deux.

Pour mettre cela en perspective, imaginons que nous avons un tableau avec 1 million d'éléments et que nous le divisons par deux.

En une seule étape, nous aurons réduit le nombre d'éléments que nous devrions rechercher de 500 000 éléments, par opposition à l'itération à travers tous les 1 million d'éléments et à la recherche de cette manière.

Et cela ne s'arrête pas là.

Nous allons maintenant faire exactement la même chose avec cette moitié du tableau.

Rappelons que nous recherchons pour voir si le nombre 100 existe dans notre tableau, nous devrons d'abord trouver notre point médian.

Maintenant, ne soyez pas confus par le nombre pair d'éléments dans ce tableau.

Bien qu'il n'y ait pas un nombre pair d'éléments de chaque côté de notre point médian, cela n'a en fait pas d'importance car nous devons en fait simplement diviser le tableau approximativement en deux.

Par exemple, pour trouver le milieu et le code, nous ferions quelque chose comme diviser la longueur du tableau, qui est quatre, par deux.

Ce deux résultant que nous utiliserions comme l'index de notre milieu.

Donc, écrivons les index de ce tableau en nous souvenant que les tableaux sont zéro, ce qui signifie que l'index de départ sera zéro.

Et si nous prenons ce deux résultant et voyons à quelle valeur il pointe, nous voyons que notre milieu est 100, qui est le nombre que nous recherchons.

Donc, dans ce cas, nous aurions terminé, nous avons trouvé notre nombre.

Mais pour prouver que celui que nous choisissons d'utiliser n'a en fait pas d'importance, explorons ce qui se passerait si le milieu 54 était utilisé. Est-ce que le nombre que nous recherchons est supérieur ou inférieur à notre milieu 54.

Notre nombre est supérieur à 54.

Donc, cela signifie que nous pouvons nous débarrasser du côté gauche.

Et ce qui nous reste est un tableau contenant seulement deux éléments, qui est à nouveau un tableau pair.

Donc, nous n'avons aucun moyen de déterminer lequel nous devrions choisir comme notre milieu. Voyons ce qui se passerait si nous utilisions 124 comme notre servante. Est-ce que 124 est supérieur ou inférieur à 100.

Il est supérieur, donc nous pouvons ignorer la moitié droite de ce tableau.

Maintenant, nous sommes laissés avec un tableau contenant seulement un élément.

Donc, notre soi-disant point médian ne peut être que cet élément.

Et cet élément est le nombre que nous recherchons.

Donc, nous avons terminé ici.

Donc, comme vous pouvez le voir, que vous ayez un tableau auto ou un tableau pair, tant qu'il est ordonné, la recherche de l'élément sera trouvée s'il existe dans le tableau.

Et cela, mesdames et messieurs, est comment la recherche binaire fonctionne réellement et pourquoi elle est utile.

Donc, commençons par créer un fichier et nous pouvons l'appeler log in dot j s.

Pour que la recherche binaire fonctionne, le tableau que nous recherchons doit être en ordre croissant ou décroissant.

Donc, vous ne pouvez pas simplement avoir un tableau ordonné aléatoirement et utiliser la recherche binaire dessus.

Donc, c'est juste quelque chose à garder à l'esprit tout au long du reste de ce tutoriel, notre fonction de recherche binaire va prendre quatre arguments, elle va prendre un tableau, et le tableau va simplement contenir des valeurs entières, qui devront être ordonnées, donc nous allons simplement faire de un à huit, nous devrons également passer le premier index de notre tableau à la fonction, nous allons simplement l'appeler start.

Et ce sera simplement zéro.

Et nous devrons prendre le dernier index de notre tableau, que nous appellerons simplement end.

Et nous pouvons l'obtenir en obtenant la longueur du tableau et en soustrayant un de celle-ci.

La raison pour laquelle nous devons soustraire un de la longueur du tableau est parce que les index du tableau sont en fait basés sur zéro, mais le tableau lui-même, la longueur n'est en fait pas basée sur zéro, elle sera simplement le nombre d'éléments dans le tableau.

Donc, la longueur du tableau sera de huit, mais le dernier index du tableau de longueur huit sera sept.

Donc, c'est pourquoi nous soustrayons le un.

Et enfin, mais non des moindres, nous devrons prendre une valeur cible, qui est la valeur que nous recherchons.

Et nous allons simplement rechercher huit.

Et ensuite, nous pouvons commencer à construire notre fonction.

Et nous allons simplement l'appeler recherche binaire.

Et elle prendra le tableau, le début, la fin et la cible.

Et cette fonction sera en fait une fonction récursive.

Donc, pour commencer cette fonction, nous devons trouver l'index du milieu de notre tableau.

Donc, vous remarquerez que nous utilisons une fonction intégrée math dot floor ici.

Et la raison pour laquelle nous utilisons cela est que si nous allons à la définition, elle dit qu'elle retourne le plus grand entier inférieur ou égal à son argument numérique, ce qui signifie simplement que si cette expression de division dans nos parenthèses, dans nos parenthèses de fonction, retourne quelque chose comme 5.5, la valeur assignée à MIT ne serait que cinq, car nous ne voulons pas prendre en considération quoi que ce soit après le point décimal car nous voulons simplement trouver un index, ce qui, bien sûr, n'aurait pas d'index 5.5.

Donc, par conséquent, notre mid serait simplement cinq.

Et la prochaine chose que nous voudrions faire est de vérifier si notre point médian est en fait le nombre que nous recherchons, qui est notre cible.

Donc, cela retournerait vrai si la valeur médiane de notre tableau est en fait la cible que nous recherchons.

Donc, nous retournons vrai car cela signifie que la valeur que nous recherchons existe dans le tableau, et nous aurions terminé ici.

Et en fait, je viens de réaliser que je pourrais en fait vous confondre en faisant référence à notre mid et à notre valeur mid de manière interchangeable.

Donc, ce mid ici est en fait l'index de notre mid que nous essayons d'obtenir, nous essayons d'obtenir l'index.

Donc, ici, nous pouvons simplement ajouter index également.

Donc, lorsque je dis notre mid, je fais en fait référence à la vallée. Donc, nous voulons en fait retourner vrai si la valeur qui se trouve à notre index mid est égale à notre valeur cible.

Donc, si la valeur à notre index mid n'est pas égale à notre cible, nous voulons ensuite vérifier si la valeur à notre index mid est supérieure ou inférieure à notre cible réelle.

Donc, en fait, cela devrait être fait index.

Désolé pour cela.

Et en fait, nous avons une autre erreur ici.

Donc, nous allons commencer et ensuite la cible devrait être ici.

Cela devrait fonctionner.

Donc, oui, prenons le temps de comprendre ce qui se passe dans cette ligne de code ici.

Donc, si la valeur à mid est supérieure à notre cible, cela signifie que notre cible est en fait du côté gauche du tableau.

Parce que si nous regardons ici, et que nous prenons en considération que cinq va être notre mid dans cette situation, dans la première exécution de cette fonction, cinq va être notre mid.

Et si cinq est supérieur au nombre que nous recherchons, alors cela signifie que le nombre que nous recherchons va être du côté gauche, car si cinq était, si le nombre que nous recherchons était supérieur à cinq, alors il serait du côté droit du tableau, car notre tableau est en ordre croissant.

Donc, cela est pour vérifier si l'élément que nous recherchons est du côté gauche du tableau.

Et si c'est le cas, ce que nous allons faire, c'est que nous allons passer notre start, qui va rester le même.

Donc, nous allons garder le même start, qui va être dans ce cas, il va être l'index zéro, et ensuite notre end va être mid moins un moins un, car nous allons en fait nous débarrasser de notre mid actuel et en fait, bien, cela devrait être nid index également.

Nous devons seulement attribuer le mid actuel moins un à notre variable in, car notre prochaine exécution de la fonction aurait cela comme notre end, et ensuite cela comme notre start, et donc nous ne rechercherions que 1234, ce que nous trouverions ensuite à son tour le mid pour 1234.

Et ensuite, nous ferions la même chose.

Donc, maintenant, que se passerait-il si la valeur cible que nous recherchons est supérieure à notre valeur mid ? Eh bien, voyons voir.

Donc, dans ce cas particulier, la valeur cible serait inférieure ou égale à mid.

Donc, cela signifierait que la valeur cible serait dans le côté gauche de notre droite.

Mais si ce n'était pas le cas, alors si notre cible est plus grande que notre point médian, alors nous ferions quelque chose comme else return.

Donc, la fonction va toujours s'appeler elle-même, bien sûr, mais cette fois, nous allons passer le tableau, le tableau, et au lieu de passer le point de départ original, nous allons passer l'index du point médian plus un.

Et cela va être notre nouveau point de départ.

Et c'est parce que nous commençons à partir du point médian jusqu'au côté droit du tableau, car la valeur réelle que nous recherchons se trouve du côté droit du tableau, et à ce stade, notre fin peut simplement rester la même, car la fin est simplement la fin du tableau.

Donc, regardons cela à nouveau.

Donc, faisons semblant que pour cette exécution, notre mid est cinq, mais cette fois, la valeur réelle que nous recherchons est supérieure à notre point médian.

Donc, cela signifie qu'il ne peut pas être de ce côté gauche, car tout ce qui se trouve à gauche de notre point médian va être inférieur à, car notre tableau est en ordre croissant.

Donc, il va être de ce côté droit.

Et s'il est supérieur à notre point médian, alors bien sûr, nous n'avons pas besoin de prendre cinq en considération, c'est pourquoi au lieu de faire mid index, et dans au lieu de retourner mid index et end à la fonction, nous n'avons besoin de retourner que mid index plus un, ce qui va être cet index ici, il va être index, il va être cette valeur six à l'index un index au-dessus de notre mid réel.

Maintenant, à ce stade, nous ne recherchons que notre fin et notre mid plus un.

Et nous ne recherchons que ces trois éléments dans le tableau.

C'est ce que ces deux conditions couvrent.

Donc, cette première condition couvre si l'élément est à gauche de notre méthode, qui est ici.

Et la seconde couvre si l'élément que nous recherchons est dans l'environnement de droite.

Et c'est ainsi que fonctionne la recherche binaire.

C'est pourquoi la recherche binaire est plus efficace que, disons, la recherche linéaire.

Parce que nous n'avons pas besoin de vérifier chaque élément dans le tableau, nous pouvons en fait essentiellement éliminer la moitié du tableau en sachant si l'élément que nous recherchons est inférieur ou supérieur au point médian.

Donc, allons-y et voyons si nous pouvons réellement exécuter cette fonction et la faire fonctionner.

Et je vais vous dire tout de suite, nous allons essayer de l'exécuter deux fois, nous allons essayer de l'exécuter en recherchant la valeur réelle que nous savons être dans le tableau.

Et nous allons essayer de l'exécuter en recherchant une valeur qui n'est pas dans le tableau.

Et vous verrez qu'il manque quelque chose dans cette fonction.

Donc, allons-y et essayons de l'exécuter.

Maintenant, pour l'exécuter.

Évidemment, nous devons invoquer la fonction.

Donc, nous allons faire une recherche binaire.

Et nous allons passer le tableau, le début et la fin, la cible.

Et nous allons sauvegarder cela.

Donc, nous allons essayer de l'écrire en utilisant simplement node, login dot j s.

Et nous l'avons cassé.

Bien.

Il faut ajouter la cible ici.

Cela a fait échouer toute la fonction.

Voir cela à nouveau.

D'accord, donc voyons ce qui se passe si nous retournons en fait la valeur, je veux dire, console log la valeur de retour de la fonction.

Et nous obtenons vrai car huit est trouvé dans le tableau.

Mais ce que vous verrez ici, c'est que si nous recherchons quelque chose qui n'existe pas dans le tableau, nous allons le casser à nouveau.

Donc, 10 n'existe pas.

Donc, essayons à nouveau.

Et nous avons obtenu une taille maximale de la pile d'appels dépassée, car laissez-moi vous montrer ce que cela signifie : taille maximale de la pile d'appels dépassée.

Donc, ce que nous faisons, c'est que chaque fois que nous ne remplissons pas cette condition vraie, nous allons appeler à nouveau binary search, ce qui signifie que nous appelons la fonction de manière récursive.

Et si nous recherchons un nombre qui n'existe pas dans le tableau, binary search va essentiellement continuer à s'appeler elle-même de manière récursive.

Et il n'y aura jamais un moment où elle s'arrête.

Même si elle ne trouve pas l'élément dans le tableau, elle va continuer à s'appeler elle-même de manière récursive jusqu'à ce que nous atteignions éventuellement la taille maximale de la pile d'appels, ce qui signifie essentiellement que vous avez dépassé la quantité de mémoire allouée à cette application particulière.

Donc, pour résoudre ce problème, ce que nous voulons faire, c'est ajouter une condition de base qui empêchera la fonction de s'appeler elle-même de manière récursive après avoir vérifié l'intégralité du tableau.

Donc, nous pouvons faire si le début est supérieur à la fin, alors retourner faux.

Donc, la raison pour laquelle cela fonctionne est que si la cible n'est pas dans notre tableau, cela signifie soit que la cible est plus grande que la plus grande valeur dans notre tableau, soit qu'elle est plus petite que la plus petite valeur dans notre tableau.

Donc, cela signifie que notre fonction continuera à vérifier notre tableau jusqu'à ce que nous arrivions finalement soit au plus grand élément si la cible est plus grande que la plus grande valeur dans le tableau, soit au plus petit élément si la cible est plus petite que le plus petit élément dans le tableau.

Et à ce moment-là, les valeurs de début et de fin seront égales et au point où les valeurs de début et de fin sont égales, passer notre début dans notre dans l'une ou l'autre de ces lignes, aura en effet pour effet de rendre le début supérieur à la fin.

Et maintenant, nous pouvons exécuter cela à nouveau en utilisant ce tin qui n'existe pas dans notre tableau.

Et comme vous pouvez le voir, nous obtenons faux.

Et si nous avons même ajouté négatif ici, négatif 10 n'existe pas.

Donc, nous obtenons également faux.

Et voyons, que pouvons-nous essayer d'autre.

Nous avons juste essayé de savoir que deux existe.

Et puis et nous obtenons vrai.

Donc, changeons cela pour revenir à un pour avoir une idée de pourquoi cette fonction est oh log in, essayons de créer un tableau plus long ici.

Actuellement, notre tableau ne contient que ces huit éléments.

Et il sera un peu difficile d'avoir une compréhension générale de la manière dont notre entrée évolue avec un tableau aussi petit, donc nous pouvons aller de l'avant et simplement vider notre tableau, et nous allons simplement créer notre propre tableau.

Donc, voyons, le commerce de notre propre tableau, nous pouvons simplement faire pour i égal zéro, i est inférieur à 1024 i plus plus.

Et ensuite ici pour chaque itération de AI, nous pouvons simplement faire grade up, push high.

Et réfléchissons, faisons en fait i égal à un.

Et ensuite, nous allons faire cela inférieur ou égal à.

Et après cela, nous pouvons console.

log notre tableau.

Et pour l'instant, commentons simplement cela.

Et voyons.

D'accord, donc à ce stade, nous avons un tableau plus long, ce qui, espérons-le, aidera à visualiser comment l'entrée évolue lorsque je fais quelques astuces de console log ici.

Donc, oui, donc nous n'avons plus besoin de logger cela.

Supprimez simplement cela, en fait.

Donc, nous créons un nouveau tableau ici.

Et il va être un tableau qui a des éléments de un à 1024.

Et pour les besoins de cet exemple, je ne veux pas que nous trouvions l'élément, je veux dire, l'élément dans le tableau, donc nous allons simplement le changer en quelque chose qui n'existe pas dans le tableau.

Donc, nous allons simplement le mettre comme 100 000 qui n'existe pas dans notre tableau, et aussi la fin, et cela obtient la fin de ce tableau actuel.

Donc, nous allons devoir descendre cela après avoir créé notre tableau complet.

Donc, ce tableau est vide ici, et ensuite nous ajoutons toutes les valeurs dans cette boucle for et ensuite nous obtenons la fin du tableau.

Et le début, bien sûr, peut toujours être zéro car il est zéro.

Et aussi, nous pouvons descendre ici et supprimer jusqu'à, nous n'avons plus besoin de logger cela, car nous allons faire un autre console log.

Donc, nous allons exécuter la fonction ici.

Et ici, c'est là que nous allons essayer de faire de la magie.

Donc, pour chaque appel à la recherche binaire, comme le premier appel, et chaque appel récursif, nous voulons ne pas simplement appeler de manière récursive le premier appel.

Et chaque appel récursif, nous voulons logger à quoi ressemble le tableau que nous recherchons.

Donc, au début, c'est le tableau complet, que nous venons de montrer lorsque nous avons loggé plus tôt.

Et ensuite, à chaque appel de la fonction, le taux va être essentiellement divisé par deux.

Donc, cela va ressembler à quelque chose comme, voyons, console dot log va faire array dot slice.

Et nous allons faire le début et la fin.

Donc, ce que cela fait, c'est qu'il ne va montrer que les parties de la course du début à la fin, il ne va plus montrer le tableau complet.

Et voyons si cela fonctionne.

Donc, ici, nous pouvons faire node, log in. 

D'accord, et oui, cela a fonctionné.

Donc, peut-être que je peux le rendre plus petit.

Donc, vous pouvez voir, donc quand je le rends plus petit comme ceci, c'est un peu facile pour vous de voir comme, bien, à ce stade, il est trop long pour montrer son intégralité.

Mais vous pouvez toujours voir ce qui se passe ici.

Donc, comme la valeur est supérieure au côté gauche du tableau, vous pouvez voir que toutes ces valeurs inférieures vont être essentiellement éliminées, et cela continue à être divisé par deux et à être divisé par deux.

Et voici où vous pouvez commencer à voir visuellement ce qui se passe ici, comme je peux voir que le rayon continue à devenir de plus en plus petit.

Pour comprendre ovan login, nous allons prendre cette petite fonction en considération.

Cette fonction a une complexité de ovan login.

Passons en revue ce code ligne par ligne afin que nous puissions comprendre ce qui se passe ici.

Cette fonction prend un argument in qui, pour l'exemple, sera pour nous, nous déclarons ensuite une autre variable y que nous allons définir égale à n, nous en viendrons à ce que cette variable Y est pour plus tard.

Et à ce stade, nous avons une boucle while qui itère à travers n jusqu'à ce que n soit égal à un.

Pour chaque itération à travers in ce code à l'intérieur de la boucle while est exécuté.

Visualisons cela.

Pour la première itération de la boucle while in commence à quatre mais nous le divisons par deux, donc n est maintenant égal à deux.

Ensuite, nous arrivons à cette ligne de code qui est le début d'une boucle for.

C'est là que cette variable y intervient.

La raison pour laquelle nous avons déclaré cette variable avant le début de la boucle est que n est divisé par deux à chaque itération.

Cela réduit à son tour la taille de la variable n.

Mais pour cette boucle for interne, nous avions besoin d'itérer à travers la taille originale de notre n original.

Donc, nous avons stocké le n original dans une variable séparée.

D'accord, retour à cette boucle for interne.

Pour chaque itération de cette boucle for jusqu'à la taille de n, nous allons logger ou imprimer la valeur pour I.

Une fois cela terminé, nous passons à l'itération suivante de la boucle while et répétons le processus en entrant dans cette itération In est maintenant deux, nous commençons par diviser in par deux.

Donc, n est maintenant un.

Et une fois de plus, nous itérons à travers notre boucle for interne jusqu'à la taille de y.

Maintenant, à ce stade, vous remarquerez que notre n est maintenant un.

Si nous vérifions la condition de notre boucle while, nous voyons que nous voulons seulement itérer tant que n est supérieur à un.

Donc, la boucle while va maintenant se terminer, et la fonction est terminée.

Maintenant, après tout ce qui est dit et fait, et avec tout écrit, nous pouvons voir qu'il y a une boucle de niveau supérieur ici.

Et il y a une boucle interne pour chaque itération de la boucle de niveau supérieur.

Donc, c'est là que la magie opère.

Donc, faites très attention.

Pour chaque itération à travers la boucle de niveau supérieur, qui itère jusqu'à ce que n soit un, n est divisé par deux.

Cela signifie que cette boucle de niveau supérieur n'itère jamais réellement à travers la taille complète de notre entrée, la valeur de n est divisée en deux à chaque itération, ce qui explique pourquoi nous dirions que cette boucle de niveau supérieur a une complexité de Oh login.

Si vous êtes confus quant à pourquoi cette boucle de niveau supérieur est Oh, log in, prenons un peu de temps pour le prouver en l'écrivant.

Donc, cela est Oh, log in.

Mettons quelques nombres.

Maintenant, si vous avez regardé ma vidéo sur Oh, log in, vous savez qu'en informatique, la base d'un logarithme est toujours deux, sauf indication contraire.

Donc, cela peut être réécrit comme log base deux de quatre, quatre, car nous remplaçons in par notre entrée réelle pour n, qui est quatre.

Et log base deux de quatre est deux, car vous devez élever deux à la puissance de deux pour obtenir quatre.

Et comme vous pouvez le voir, cela a du sens, car pour cette boucle de niveau supérieur, nous n'itérons que deux fois.

Donc, pour cette boucle de niveau supérieur, nous avons log base deux de quatre égal à deux.

Maintenant, nous devons examiner ce qui se passe dans chacune des deux itérations de la boucle de niveau supérieur.

Pour chaque itération, nous parcourons la taille complète de y, qui est la taille originale de n.

Donc, cela signifie que chacune de ces boucles internes a une complexité de O de n, ce qui signifie simplement que le temps de traitement augmente linéairement avec la taille de n.

Maintenant, c'est là que nous rassemblons tout.

O de n log in signifie en fait O de n fois log in.

Et si nous mettons quelques nombres ici, nous obtenons ceci.

Parce que rappelez-vous, log base deux de quatre est égal à deux.

Et si vous regardez notre visualisation, cela a parfaitement du sens, car pour chaque itération de la boucle supérieure, nous parcourons l'intégralité de y, qui est notre valeur originale pour n.

Et cela, mesdames et messieurs, est comment vous visualisez tout de in log in.

Donc, nous pouvons commencer par créer un fichier, appelons-le simplement merge sort, puis créer une fonction, que nous appellerons également merge sort.

L'argument de cette fonction sera le tableau que nous cherchons à trier. Pour la première partie de cette fonction, nous devons nous assurer que le tableau que nous passons a une longueur supérieure à un. Nous devons faire cela car si le tableau n'a qu'une longueur de un et qu'il n'y a qu'un seul élément dans le tableau, alors il est déjà trié.

Cela sera également notre cas de base, car cette fonction merge sort sera une fonction récursive.

Ensuite, nous allons devoir diviser notre tableau en deux.

Pour ce faire, nous devons d'abord trouver l'index du milieu de notre tableau.

Ce que fait ce math dot floor ici, c'est qu'il s'assure que nous ne prenons en considération que le nombre de base du résultat de la division.

Par exemple, si nous divisons un nombre qui donne, je ne sais pas, disons 5.5, nous ne prendrions pas en considération le nombre après le point décimal.

Donc, nous ne retournerions que le nombre cinq à la variable.

Et c'est parce que lorsque nous prenons les index en considération, il n'y a pas d'index 5.5 ou 2.2 ou 1.1, il n'y aurait qu'un index un, cinq ou deux.

Donc, c'est pourquoi nous utilisons math dot floor ici.

Et une fois que nous avons l'index du milieu de notre tableau d'entrée, nous pouvons alors diviser le tableau en deux et créer un tableau séparé pour le côté gauche et un tableau séparé pour le côté droit.

Donc, nous pouvons faire cela en créant simplement un nouveau tableau, left array, puis nous pouvons définir left array égal à input array dot slice, puis les index vont être les arguments que nous avons passés.

Donc, en gros, des tranches de et à.

Donc, nous voulons trancher à partir du premier index de notre tableau d'entrée.

Et nous voulons trancher jusqu'à l'index du milieu que nous venons d'obtenir.

Et c'est parce que nous voulons le côté gauche du tableau.

Donc, disons par exemple que le tableau ressemblait à ceci.

Et nous avons gagné, nous avons obtenu notre index du milieu, qui serait quelque chose comme ce trois ici.

Et ensuite, nous voulons créer un tableau commençant par cet index zéro, jusqu'à notre index du milieu, qui serait la moitié gauche du tableau, puis nous irions de l'avant et ferions la même chose pour la moitié droite du tableau.

Donc, nous allons en fait faire la même chose pour la moitié droite du tableau, nous allons simplement l'appeler right array.

Et nous allons faire array dot slice à nouveau.

Mais cette fois, nous allons simplement faire de l'index du milieu jusqu'à l'index, le dernier index du tableau, et la façon dont nous obtenons le dernier index du tableau est simplement en utilisant array dot length.

Et cela ici peut en fait être un peu déroutant, car nous savons que array dot length nous donne la longueur du tableau, qui est le nombre d'éléments dans le tableau.

Et nous savons également que l'index du tableau est basé sur zéro.

Donc, en gros, si la longueur d'un tableau est cinq, il n'y aura que l'index 0123, et quatre, il n'y aura pas d'index cinq.

Donc, ici, vous pourriez vous demander comment cela fonctionne en réalité.

Et c'est parce qu'en fait, il y a une erreur.

Et cette méthode n'est pas sliceurs, juste slice, mais c'est parce que cette méthode slice coupe jusqu'à in mais sans inclure in.

Donc, en gros, cette valeur de fin, elle n'est pas incluse dans la tranche de tableau réelle, seule la valeur avant sera incluse.

Par exemple, si nous avons un tableau qui ressemble à cela, la fin que nous utiliserions pour ce tableau serait trois, même s'il n'y a que l'index 01.

Et deux, il va trancher jusqu'à la fin sans inclure in, donc c'est pourquoi nous n'avons pas besoin de soustraire un de cela car si nous devions soustraire un de array dot length, et utiliser cela comme le dernier index, ou l'index de fin qui est passé à la méthode slice, alors nous n'obtiendrions en fait pas le tableau complet, nous n'obtiendrions que jusqu'à celui-ci, mais sans inclure celui-ci.

Donc, ils étaient capables de ne ressembler qu'à ceci dans cette tranche.

J'espère que cela a du sens.

C'est un peu déroutant.

Et gardez également à l'esprit qu'avec cet exemple que je viens de donner ci-dessus, je ne prends pas en compte l'index du milieu.

Donc, pour ce tableau en particulier, cela ressemblerait à quelque chose comme array dot slice, bien, slice et il y aurait un index zéro jusqu'à array dot length moins un.

En tout cas, dernier mais non des moindres, pour notre fonction merge cert réelle, ce que nous allons devoir faire, c'est implémenter la partie récursive de la fonction, ce qui signifie que nous allons retourner et supporter avec moi, nous allons retourner une fonction d'assistance que nous n'avons pas encore créée.

Et nous allons l'appeler merge.

Et dans cette fonction d'assistance merge, nous allons accepter deux paramètres, qui seront le tableau de gauche et le tableau de droite.

Et ce que nous allons passer à merge sera l'appel récursif à merge sort.

Et ensuite notre tableau de gauche, et nous allons également passer l'appel récursif à merge sort, et notre tableau de droite.

Cela va sembler un peu déroutant pour l'instant.

Mais restez avec moi, je vais expliquer comment cela fonctionne.

Et je vais essayer de rendre les choses claires pour vous.

Mais pour l'instant, nous n'avons pas cette fonction merge, donc nous devons aller de l'avant et la créer.

Donc, allons-y et créons cette nouvelle fonction d'assistance appelée merge, qui prendra le tableau de gauche et le tableau de droite.

Oh, désolé, et ce n'est pas merger, c'est merge.

Maintenant, cette fonction va être la fonction qui fusionne réellement les deux tableaux.

Donc, la manière dont Merge Sort fonctionne est que nous utilisons une approche de type diviser pour régner dans laquelle le tableau d'entrée est essentiellement divisé en deux jusqu'à ce que nous ayons des tableaux de longueur un, et à ce stade, des tableaux de longueur un, comme mentionné ci-dessus, lorsque nous avons créé cette espace de cas, ici, un tableau de longueur un est déjà trié.

Donc, pour visualiser cela, si nous avons un tableau, qui est un, il n'y a qu'un seul élément dans ce tableau, donc évidemment, ce un va être le premier et le dernier élément du tableau.

Donc, il n'y a pas besoin de le trier car il n'y a rien à comparer avec.

Ce que nous faisons dans cette fonction merge réelle est que nous allons rassembler ces tableaux triés et les comparer puis trier ces tableaux individuels d'un élément.

Donc, une chose à garder à l'esprit tout au long du processus d'écriture de cette fonction merge est que cette fonction merge va toujours prendre en entrée deux tableaux déjà ordonnés, en commençant par les tableaux ordonnés de longueur un.

Donc, pour commencer, nous allons créer une variable, qui sera simplement le tableau de résultats, et il va commencer par être un tableau vide.

Donc, ces tous égaux à un tableau vide.

Et nous allons également définir nos index de base pour le tableau de gauche et le tableau de droite, mais l'index pourrait être égal à zéro.

Maintenant, nous allons faire la même chose pour la droite.

Ensuite, nous allons créer une boucle while qui va comparer les deux tableaux élément par élément.

Et en fait, collons ici, cette longueur.

Donc, dans cette boucle while, nous allons comparer chaque élément des deux tableaux et celui qui est inférieur à l'autre sera ajouté au tableau de résultats, nous allons ensuite incrémenter l'index de l'élément qui a été ajouté au tableau de résultats car cet élément n'a plus besoin d'être comparé.

Si vous êtes un peu confus par cela, restez avec moi, je vais en fait créer une illustration pour que vous compreniez mieux.

Mais pour l'instant, écrivons simplement le code.

Imaginons que les rayons que nous voulons fusionner ressemblent à ceci pour le tableau de gauche et à ceci pour le tableau de droite.

Gardez à l'esprit que la fonction d'assistance merge fusionne des tableaux ordonnés, donc elle ne fonctionnera pas sur des tableaux non ordonnés.

Dans cet exemple, nous fusionnons deux tableaux ordonnés de longueur trois pour montrer l'intégralité de la fonctionnalité de la fonction, mais cela fonctionnera également pour des tableaux naturellement triés de longueur un.

Donc, pour que cette boucle while continue, les index gauche et droit doivent être inférieurs à la longueur de leurs tableaux correspondants.

Comme vous pouvez le voir, ces index sont incrémentés chaque fois que cet élément est poussé vers le tableau de résultats.

Donc, si nous dessinons cela, cela ressemble à quelque chose comme ceci.

Voici les deux tableaux et leurs index.

Dans cette ligne suivante, nous vérifions si l'élément à l'index du tableau de gauche, qui est actuellement zéro, est inférieur à l'élément à l'index du tableau de droite, qui est également zéro.

Donc, est-ce que trois est inférieur à un.

Non.

Donc, cela signifie que nous faisons ce qui est dans notre condition else, qui est de pousser l'élément du tableau de droite à son index actuel vers le tableau de résultats et d'incrémenter l'index du tableau de droite.

Et maintenant, notre index du tableau de droite est un, donc nous pouvons déplacer cela.

Et ensuite, une fois de plus, nous faisons notre comparaison en haut de la boucle for est-ce que trois est inférieur à six ? Oui.

Donc, nous poussons trois sur notre tableau de résultats et incrémentons notre index du tableau de gauche.

Et nous pouvons également déplacer cela.

Et de retour en haut de notre boucle for à nouveau, est-ce que 12 est inférieur à six ? Non.

Donc, nous allons utiliser le code dans notre condition else, qui est de pousser l'élément du tableau de droite six vers le tableau de résultats et d'incrémenter l'index de droite.

Et encore une fois, nous allons déplacer cela et maintenant est-ce que 12 est inférieur à 15.

Oui, donc nous poussons le 12 du tableau de gauche vers le tableau de résultats et ensuite nous incrémentons l'index de gauche ainsi que nous déplaçons cette flèche vers le nouvel index de gauche.

Maintenant, est-ce que 16 est inférieur à 15 ? Non.

Donc, nous passons à notre condition else et poussons le 15 du tableau de droite vers notre tableau de résultats et incrémentons l'index de droite de un.

Maintenant, à ce stade, cette boucle while va se terminer car si vous vous souvenez, cette boucle while ne continuera que si l'index de gauche est inférieur à la longueur du tableau de gauche, et l'index de droite est inférieur à la longueur du tableau de droite.

À ce stade, notre index de droite est égal à la longueur du tableau de droite.

Comme vous l'avez probablement déjà remarqué, il reste un 16 dans le tableau de gauche qui n'a pas encore été poussé vers le tableau de résultats.

Mais la boucle while est déjà terminée.

Donc, que faisons-nous ? Après la boucle while, nous allons ajouter une autre ligne de code qui ressemble à ceci.

Donc, ce retour va retourner un seul tableau qui est une combinaison ou une concaténation de trois tableaux : le tableau de résultats, une tranche du tableau de gauche et une tranche du tableau de droite.

Donc, cette fonction de tranche, si nous ne passons qu'un seul index, il sera utilisé comme le début de la tranche et va trancher jusqu'à la fin du tableau.

Décomposons cela.

Donc, si vous vous souvenez de la dernière diapositive, notre tableau de résultats ressemble actuellement à ceci.

Et nous allons y ajouter une tranche du tableau de gauche commençant par l'index de gauche que nous avons incrémenté, ce qui est deux, ce qui donne un tableau contenant seulement cette partie. Et nous allons ajouter à cela une tranche du tableau de droite commençant par l'index de droite que nous avons incrémenté, ce qui est trois, ce qui donne un tableau vide, car l'index trois serait ici.

Et avec tout cela combiné, le résultat retourné est un tableau ordonné qui ressemble à ceci.

Maintenant, allons-y et ajoutons le retour que nous venons de discuter dans l'illustration.

Et cela complète notre fonction merge.

Et maintenant que la fonction merge est complète, notre fonction merge sort est également complète.

Et maintenant, nous pouvons aller de l'avant et tester cela.

Pour tester cela, nous devrons créer un tableau.

Et ce tableau, nous devrons le passer à notre fonction merge sort.

Et voilà, notre tableau trié.

Et si nous prenons le temps de revenir ici et de jeter un coup d'œil au code, vous verrez que dans cette fonction merge sort, nous divisons le tableau d'entrée de manière récursive, ce qui rend cette partie Merge Sort de la fonction de log in.

Et en fait, cette fonction merge est all event car elle doit toucher chaque élément des deux tableaux pour les trier réellement.

Donc, avec cette fonction merge étant old in et la fonction merge sort récursive réelle étant of login.

Pour chaque niveau jusqu'à la profondeur de cette fonction récursive, nous allons en fait faire ce merge, qui est O de n.

Donc, pour obtenir la complexité temporelle globale, nous devrions simplement multiplier la profondeur de cette fonction récursive par O de n, qui est O de n log in car O de N log N est simplement multiplier in par log in et log in, dans ce cas, sera la profondeur à laquelle cette fonction récursive doit traverser.

Donc, visualisons cette fonction merge sort, nous allons passer en revue le code ligne par ligne.

Donc, imaginons que nous avons un tableau qui ressemble à ceci.

Donc, ce tableau ici sera notre tableau d'entrée.

Donc, c'est le tableau que nous allons passer à notre fonction merge sort ici.

Donc, ce tableau est ce tableau.

Donc, la première partie du code ici, il vérifie simplement si notre tableau est supérieur à la longueur un, car un tableau de longueur un est déjà trié.

Donc, si nous obtenons un tableau de longueur un ici, nous allons simplement retourner ce tableau comme un tableau déjà trié.

Mais si le tableau est supérieur à la longueur un, alors nous allons passer à cette partie du code.

Et cette partie du code est là où l'approche diviser pour régner est implémentée.

Donc, en gros, ici, nous allons diviser notre tableau d'entrée.

En obtenant l'index du milieu du tableau, nous allons le diviser en deux tableaux séparés, qui ressembleront à quelque chose comme ceci.

Et ces tableaux individuels, left array et right array.

Après leur division, ils vont être à nouveau passés à la fonction merge sort.

Encore une fois, nous arrivons à cette partie du code, car ce tableau et ce tableau sont individuellement passés à cette fonction merge sort.

Donc, pour chacun de ceux-ci, nous arrivons à cette partie du code.

Et ces deux tableaux ne sont pas inférieurs à la longueur deux, nous avons un tableau de longueur deux, et nous avons un tableau de longueur trois.

Donc, ils vont passer à cette partie du code dans laquelle nous utilisons à nouveau l'approche diviser pour régner.

Et allons-y et écrivons cela ici en fait, car c'est important.

Donc, encore une fois, nous allons obtenir l'index du milieu de notre tableau et créer un left right et un right array en divisant le tableau unique sur son index du milieu.

Donc, vous remarquerez que ce tableau, ce tableau et ce tableau sont déjà de longueur un.

Et, comme nous l'avons vu ici, nous allons passer ces tableaux de longueur un à merge sort, nous allons passer ces tableaux à merge sort, et ensuite ils vont arriver à cette conditionnelle, et ils sont inférieurs à la longueur deux.

Donc, nous allons simplement retourner ces rayons.

Donc, pour ces tableaux, nous pouvons nous arrêter.

Mais ceci est de longueur deux.

Donc, ce tableau va arriver à cette partie du code à nouveau, et nous allons le diviser.

Et maintenant, ces tableaux sont de longueur un, donc nous pouvons nous arrêter ici aussi.

Donc, ces appels à merge sort, sont les mêmes que ces appels à merge sort.

Mais nous n'avons toujours pas appelé merge.

Et ce que merge va faire, c'est qu'il va prendre deux tableaux déjà triés, et il va les fusionner en un seul tableau trié.

Et à quoi cela va ressembler, c'est qu'il va être appelé ici, ces résultats vont être fusionnés en un seul tableau trié.

Donc, ces deux tableaux triés vont être combinés et retournés ici comme un tableau trié de longueur deux.

Et la même chose sera faite ici.

Nous allons fusionner.

Et ces deux tableaux triés vont être combinés et retournés ici comme un seul tableau trié.

Et nous ferons de même ici.

Fusionner.

Et ces deux tableaux triés vont être combinés et retournés ici comme un seul tableau trié.

Et enfin, mais non des moindres, nous allons fusionner ici.

Et ces deux tableaux triés vont être combinés et retournés ici comme un seul tableau trié.

Et n'oublions pas notre appel initial à merge sort.

Donc, c'est ainsi que nous pouvons visualiser le merge sort récursif.

Mais vous vous demandez probablement toujours ce que cette fonction merge fait réellement.

Donc, comme mentionné précédemment, cette fonction merge prend deux tableaux déjà triés, et elle les combine en un seul tableau trié.

Et cette fonction ressemble à quelque chose comme ceci.

Donc, comme vous pouvez le voir, merge prend un tableau de gauche et un tableau de droite, tous deux triés, et ensuite il retournera ce tableau de résultats, qui est une combinaison des deux tableaux de gauche et de droite triés.

Donc, pour comprendre la complexité temporelle de merge store, nous allons prendre un tableau et un tableau de longueur quatre en considération.

Donc, ce tableau d'entrée sera passé à la fonction merge sort.

Et ce que cet appel à merge sort fera, c'est diviser le tableau approximativement en deux et ces moitiés seront passées à merge sort de manière récursive. À ce stade, nous avons nos tableaux de longueur un.

Donc, nous ne pouvons pas diviser ces rayons davantage.

Et pour comprendre la complexité temporelle de merge sort, nous devons comprendre, oh, log in.

Donc, comme nous le savons, en informatique, donc log in est la même chose que log, base deux in, et dans ce cas, in est la longueur de notre tableau ici, qui est quatre.

Donc, la raison pour laquelle vous devez comprendre login, c'est parce que cette approche de diviser pour régner que nous implémentons ici est login.

C'est-à-dire que log base deux, un quatre, qui est notre in, notre n est quatre, est égal à deux.

Et c'est parce que deux à la puissance de deux est égal à quatre, ce qui signifie que pour un tableau de longueur quatre, il y aura deux niveaux à notre structure d'arbre récursif.

Et nous pouvons le voir ici, vous avez le niveau un, et nous avons le niveau deux.

Donc, c'est un niveau, et c'est un niveau.

Et pour chacun de ces niveaux, ce que nous devons faire, c'est que nous devons toucher chaque élément de n, car nous devons les trier.

Et afin de les trier, si vous vous souvenez de notre illustration de merge, dans cette fonction merge, la boucle while dans cette fonction merge, doit toucher chaque élément pour comparer les éléments et créer le tableau fusionné.

Donc, cela signifie que pour chaque niveau, nous devons fusionner.

Et cette fonction merge doit toucher chaque élément de n.

Donc, cela signifie que chaque niveau est en fait Oh, alors.

Et il y a log n niveaux.

Donc, O de n fois log in signifie en fait Oh, de quatre, car quatre est notre in, in est pour 1234.

Donc, quatre est notre n fois log, base deux, un quatre.

Et comme nous l'avons vu ici, log base deux, un quatre est en fait juste deux fois quatre.

Donc, le nombre d'éléments dans le tableau, et le nombre de niveaux que nous devons parcourir, donc pour chaque niveau, nous devons toucher in éléments dans le tableau, ce qui est deux fois quatre.

Et c'est pourquoi mergesort a une complexité de O de n log in.

Donc, nous allons commencer par examiner cette implémentation récursive de Fibonacci.

Donc, imaginons que nous passons le nombre quatre à notre fonction fib.

Donc, à ce stade, quatre est notre valeur pour n.

Donc, après avoir appelé cette fonction, nous allons finir à notre premier bloc if.

Et ce bloc if retourne simplement zéro si n est égal à zéro, puis nous passons à un deuxième bloc if, le deuxième bloc if retourne simplement un si n est égal à un.

Donc, une fois que nous passons le nombre quatre dans notre fonction, nous allons finir à ce premier bloc if.

Et ces deux blocs if sont des cas de base, car comme nous le savons, avec les fonctions récursives, nous devons avoir un cas de base afin que la fonction ne continue pas à s'appeler elle-même même après avoir terminé.

Donc, nous passons le quatre dans notre fonction fib, et quatre n'est pas égal à zéro, donc nous ne retournons pas zéro, et quatre n'est pas égal à un, donc nous ne retournons pas un.

Donc, nous finissons ici.

Et ce que fait ce retour, c'est qu'il additionne le résultat de deux autres appels à la fonction Fibonacci, cette première fonction Fibonacci, nous allons l'appeler avec notre n moins un, donc quatre moins un, et la seconde, nous allons l'appeler avec notre n moins deux, donc quatre moins deux.

Donc, jetons un coup d'œil à ce à quoi cela ressemble.

Et comme nous pouvons le voir, quatre moins un est simplement égal à trois, donc cela serait en fait juste trois.

Et même pour ici.

Cela serait simplement égal à deux.

Donc, à ce stade, nous avons deux appels à notre fonction favorite, notre fonction Fibonacci.

Un que nous passons trois est notre in et un numérateur passant deux est notre in.

Donc, pour ces deux appels, aucun d'entre eux ne retournera à ces blocs IP.

Donc, nous allons finir par redescendre ici à nouveau, ce qui ressemblera à ceci.

Et encore une fois, nous pouvons simplement faire les calculs dans les parenthèses.

Et laissez-moi simplement rendre cela un peu plus petit.

Donc, à ce stade, pour ces trois appels à la fonction Fibonacci, nous allons atteindre notre cas de base, car nous passons zéro pour cet appel.

Et nous allons simplement retourner zéro à ce moment-là.

Et nous passons un pour ces deux appels.

Et nous allons simplement retourner un à ces points.

Donc, ceux-ci vont être complets.

Ceux-ci sont terminés.

Et pour cette fonction, nous passons deux comme notre n, qui n'est pas égal à zéro et est égal à un.

Donc, à ce stade, nous allons à nouveau descendre à cette partie du code.

Et maintenant, ces deux ont également atteint nos cas de base.

Et une fois de plus, je vais devoir réduire cela.

Donc, maintenant, nous allons entrer dans la raison pour laquelle cette fonction récursive Fibonacci est une fonction exponentielle.

Tout d'abord, commençons par observer cette structure d'arbre récursif.

Donc, comme nous pouvons le voir, ici, nous avons un, deux et trois niveaux à cette structure d'arbre récursif.

Donc, nous pouvons écrire cela niveau un, niveau deux, et niveau trois.

Et pour ce premier niveau, ici, nous appelons la fonction fib deux fois.

Donc, un, deux, et pour ce deuxième niveau, nous appelons notre fonction fib quatre fois 1234.

Donc, ce niveau, nous faisons deux appels à la fonction Fibonacci, ce niveau, nous faisons quatre appels à la fonction Fibonacci.

Et ignorons simplement ce troisième niveau pour l'instant.

Et concentrons-nous simplement sur ces deux niveaux supérieurs.

Donc, deux ici est la même chose que deux à la puissance de un et quatre, ici est la même chose que deux à la puissance de deux.

Et comme vous pouvez le voir, nos exposants correspondent à nos niveaux.

Donc, en fait, si ces trois fonctions devaient faire leurs deux appels supplémentaires à Fibonacci récursif, nous aurions quelque chose qui ressemble à ceci.

Donc, nous avons deux appels ici, deux appels ici, et deux appels ici.

Donc, nous allons simplement écrire cela.

Donc, imaginons que ceux-ci sont également des coûts supplémentaires pour la fonction Fibonacci récursive.

Et imaginons simplement que c'est le cas pendant une seconde, juste pour que nous puissions mieux comprendre pourquoi cette fonction est de complexité temporelle exponentielle.

Donc, maintenant, si nous comptons les appels à ce troisième niveau de notre fonction Fibonacci récursive, et gardez à l'esprit que ces appels ne seront pas réellement effectués, seulement ceux-ci le seront.

Mais nous écrivons simplement cela pour que nous puissions mieux visualiser ce qui se passe ici.

Donc, si nous comptions les appels à la fonction Fibonacci, ce serait 12345678.

Donc, nous aurions huit appels à ce troisième niveau, et huit est la même chose que deux cube ou deux à la puissance de trois.

Et comme vous le voyez, encore une fois, notre exposant correspond à notre niveau.

Donc, cela signifie que si notre n est quatre, nous irions trois niveaux de profondeur.

Et à chaque niveau, le nombre d'appels à notre fonction Fibonacci augmente de manière exponentielle.

Mais vous vous demandez peut-être, puisque notre n est quatre, et que nous nous arrêtons ici, quand c'est deux à la puissance de trois, par opposition à deux à la puissance de quatre, comment cela se traduit-il par le fait que cette fonction est off deux à la fin ? Eh bien, c'est en fait assez simple.

Donc, en réalité, cette fonction Fibonacci est O de deux à la n moins un.

Et si nous écrivons cela, vous pouvez voir qu'il s'agit de o de deux à la quatrième puissance moins un, qui est simplement égal à O de deux à la troisième puissance, ce qui est la même chose que le nombre d'appels effectués à ce troisième niveau, n'est-ce pas.

Et si vous vous souvenez, en bego, nous ignorons les constantes.

Donc, si en réalité, cette fonction est O de deux à la n-ième puissance moins un, et nous ignorons les constantes, cela signifie que nous allons ignorer ce moins un, ce qui entraîne la complexité temporelle de cette fonction étant o de deux à la N.

Et à ce stade, vous vous demandez probablement comment nous sommes capables d'ajouter ces appels de fonction ici.

Et en réalité, je n'ai ajouté ces appels de fonction ici que pour vous donner une meilleure visualisation de ce qui se passe à chaque niveau et pourquoi nous considérons cette fonction comme étant off deux à l'internet.

Parce que c'est plus facile à visualiser si nous écrivons en fait ces fonctions que nous n'appelons pas réellement.

Et nous pouvons faire cela parce qu'avec bego, comme nous l'avons appris, nous cherchons seulement une borne supérieure, comme nous ne cherchons pas une borne serrée, nous ne cherchons pas à être très spécifiques, nous cherchons seulement ce que vous pouvez dire une estimation du pire scénario.

Donc, comme vous pouvez le voir ici, sur cette fonction de gauche, nous appelons fib et ensuite nous soustrayons un de n.

Et sur celle de droite, nous appelons fib et ensuite nous soustrayons deux de n.

Donc, ce côté droit de l'arbre sera toujours plus court que ce côté gauche de l'arbre, il y aura toujours cet espace vide.

Parce que sur ce côté droit de l'arbre, à chaque niveau, nous soustrayons deux.

Et à ce côté de l'arbre, à chaque niveau, nous soustrayons un.

Mais lorsque nous prenons bego en considération, nous n'avons pas besoin de nous en soucier.

Et peu importe le nombre que nous passons dans cette fonction, au niveau le plus bas, il y aura toujours un écart sur ce côté droit.

Mais ce n'est pas grave, car nous cherchons seulement une borne supérieure.

Donc, ceux-ci sont juste ici pour vous aider à visualiser ce qui se passe réellement et pourquoi cette fonction est considérée comme étant de croissance exponentielle.

Et c'est pourquoi la Fibonacci récursive est de complexité temporelle exponentielle, j'espère que cela a du sens.

Nous allons commencer avec la fonction qui appellera F.

Et cette fonction sera une fonction récursive.

Donc, cette première partie du code sera notre cas de base.

Donc, si la valeur de n passée à cette fonction est égale à zéro, alors nous allons imprimer ces étoiles.

Et ensuite, nous allons simplement retourner, mais si nous passons une valeur à n qui n'est pas égale à zéro, alors nous irons à cette boucle for.

Donc, commençons avec un exemple.

Donc, disons que nous passons le nombre trois à notre fonction, ce qui se passera en premier, c'est que nous vérifierons si in, qui est trois dans notre cas, est égal à zéro, ce qui n'est pas le cas.

Et ensuite, nous passerons à cette boucle for.

Et ce que cette boucle for va faire, c'est que pour chaque itération de in, pour chaque itération, jusqu'à trois de zéro jusqu'à trois, qui est notre fin, nous allons appeler récursivement cette fonction à nouveau, cette fois en utilisant notre n moins un.

Donc, essayons de visualiser cela.

Donc, si nous passons à travers cette fonction, et que nous arrivons à cette boucle for, nous pouvons l'écrire comme ceci.

Donc, pour chaque index, jusqu'à trois, mais sans inclure 3012.

Et la raison pour laquelle nous ne faisons que pour chaque index 012 est parce que ici, I commence à zéro, et nous allons itérer à travers notre valeur d'entrée in jusqu'à ce que AI ne soit plus inférieur à in.

Donc, une fois que I devient égal à n, alors nous nous arrêterons.

Donc, si I devait être trois, alors nous ne passerions plus par cette boucle.

Donc, c'est pourquoi c'est 012.

Et pour chacune de ces itérations, 012, nous allons appeler cette fonction à nouveau.

Et cela va ressembler à quelque chose comme ceci.

Donc, si vous regardez ici, nous soustrayons un de in que nous passons à la fonction à chaque itération de cette boucle for.

Donc, si n est trois ici, pour chacune de celles-ci, n va être égal à deux car nous allons soustraire un pour chacune de celles-ci.

Donc, celles-ci vont en fait être f deux.

Et pour chacune de celles-ci, nous allons faire la même chose que nous avons fait pour le premier appel à cette fonction, à cette fonction f.

Mais cette fois, nous n'itérerons que sur les index zéro et un.

Donc, chacune de celles-ci est ses propres appels individuels à cette fonction récursive, n'est-ce pas.

Et chacune de celles-ci a besoin de sa propre boucle for, qui est celle-ci, celle-ci et celle-ci.

Donc, à ce stade, f est deux.

Donc, nous itérons jusqu'à ce que I ne soit plus inférieur à deux.

Donc, nous aurons l'index zéro et un que nous itérons et pour l'index zéro et un, nous allons faire cela et la même chose pour cet appel à la fonction récursive pour l'index zéro et un ou nous allons faire cela et la même chose pour celui-ci.

Et je m'excuse si l'écriture ici devient trop petite.

Mais vous verrez que cet arbre récursif devient très grand très rapidement.

Donc, je vais en fait devoir le réduire un peu.

Donc, que nous puissions avoir plus de place.

Donc, pour chacune de celles-ci, nous allons appeler à nouveau la fonction récursive.

Mais cette fois, la fonction est appelée avec deux moins un, ce qui signifie que notre in va être un.

Rendons cela un peu plus petit, en fait.

Et encore une fois, je m'excuse.

Donc, à ce stade, notre pour chaque ne se produira qu'une seule fois pour l'index zéro.

Mec, cela devient vraiment minuscule.

D'accord, donc à ce stade, notre F est un pour tous ces appels à la fonction récursive, et AI commence à zéro.

Et tant que i est inférieur à n, qui est un, alors nous allons faire ce code.

Et il ne sera inférieur à in que lorsqu'il est zéro, ce qui est cette itération.

Donc, pour chacun de ces appels à la fonction récursive, nous allons appeler cette fonction une seule fois pour cette première itération, qui est zéro.

Maintenant, à ce stade, ce sera f un moins un.

Et f un moins un sera en fait égal à zéro.

Donc, ce sera f zéro.

Donc, nous allons passer zéro comme notre in à la fonction.

Et ce sera un peu difficile à voir car c'est petit.

Mais si nous nous souvenons ici, dans la fonction réelle, notre cas de base est si n est égal à zéro, alors nous allons simplement console log, puis nous allons retourner.

Donc, pour chacun de ces appels à la fonction récursive, nous allons exécuter ce code, ce code de console log.

Et ensuite, après avoir exécuté ce code de console log, nous allons retourner, donc cela va être terminé, cette fonction entière va être terminée, car tous ceux-ci vont retourner, ils vont logger le code, puis ils vont retourner.

Et une fois que tous ceux-ci retournent, cette fonction entière va être complète, elle va se terminer.

Donc, au lieu d'écrire console log, nous allons simplement écrire que chacune de ces fonctions effectue log n après le log, la fonction va retourner.

Donc, cela va s'arrêter.

Donc, pour la dernière fois, je vais devoir rendre cela un peu plus petit.

D'accord, donc ce qui nous reste lorsque cette fonction est terminée, c'est que nous avons cette structure d'arbre.

Et cette structure d'arbre montre combien d'appels récursifs que nous avons dû faire pour atteindre notre cas de base pour chacun de ces appels récursifs.

Et si vous regardez ici, je vais encercler ceux-ci pour que vous puissiez les voir plus clairement.

Si vous regardez ici, pour chacun de ces appels récursifs à la fonction, nous avons dû exécuter ce code, nous avons dû exécuter ce code ici pour chacun de ces appels récursifs à la fonction.

Donc, au niveau final, où notre cas de base était, nous avons dû exécuter ce code.

Et si vous comptez ceux-ci, vous verrez que c'est 123456.

Donc, six fois nous avons dû exécuter ce code, passer trois dans notre fonction nous a causé de devoir rappeler cet appel récursif final à notre fonction six fois et exécuter ce code six fois.

Et ce nombre six est notre clé pour comprendre la complexité temporelle factorielle, car si vous regardez ici, nous avons oh trois factoriel.

Et la raison pour laquelle est parce que notre n est trois, n'est-ce pas ? Donc, c'est, nous substituons simplement donc tous les trois factoriels, n'est-ce pas, et trois facteurs.

Mario est six en fait, car pour obtenir la factorielle d'un nombre, vous multipliez simplement chaque nombre jusqu'à ce nombre.

Et si nous multiplions deux fois un, nous obtenons deux.

Et si nous multiplions ce deux fois trois, nous obtenons six.

Et, encore une fois, nous avons dû exécuter cette console log, ce code, nous devons exécuter 123456 fois.

Et si nous creusons un peu plus, nous verrons que trois factoriels est le résultat de la multiplication de chaque nombre jusqu'à trois, ce qui est également la même chose que multiplier chaque nombre de trois jusqu'à un, ce que nous pouvons voir si nous regardons comment il progresse à travers notre structure d'arbre.

Ici, nous pouvons voir que le premier trois est passé.

Donc, le premier trois est passé.

Et ensuite, trois fois deux est passé, trois fois.

Donc, fois trois fois deux est le meilleur.

Et le résultat de trois fois deux est six, et six fois six fois un est passé.

Donc, six fois 123456 fois un est passé.

Donc, cette boucle for passe d'abord à trois fois, donc passe à trois fois 123, ce qui est la même chose que 333, fois fois deux, trois fois 123, passant deux.

Et lorsque nous avons demandé à la fonction, nous faisons deux itérations, donc trois fois deux itérations.

Donc, nous allons faire cela, nous allons itérer à travers cette boucle for de deux itérations, trois fois trois fois deux, puis trois fois deux va être six, car nous faisons deux itérations pour chacun de ces trois.

Donc, ces itérations plus ces itérations, plus ces itérations est égal à six itérations.

Et pour chacune de ces six itérations, nous allons passer un à la fonction, donc six itérations, donc six fois nous allons passer un à la fonction.

Donc, c'est ici, six fois un, six fois un, et c'est la complexité temporelle factorielle.

J'espère que cela a du sens.

Donc, pour comprendre la complexité spatiale, nous allons prendre cette fonction en considération.

Et c'est une fonction récursive, qui retourne essentiellement un appel à elle-même avec son entrée in moins un, elle va faire cela jusqu'à ce que nous atteignions un cas de base où n est égal à zéro, puis elle va simplement retourner et à ce moment-là, cette fonction sera complète.

Donc, allons-y et dessinons à quoi ressemblerait l'exécution de cette fonction.

Donc, disons que nous avons passé le nombre cinq à cette fonction countdown.

Donc, avec ce premier appel à countdown avec l'argument cinq, nous allons finir à ce cas de base.

Et nous allons voir que notre n cinq n'est pas égal à zéro.

Donc, nous allons passer à cette partie du code, qui est simplement l'appel de cette fonction à nouveau avec cinq moins un.

Et bien sûr, cinq moins un va être quatre.

Et encore une fois, nous allons finir ici, et nous allons appeler la fonction à nouveau avec quatre moins un.

Et nous allons continuer à faire cela jusqu'à ce que nous passions zéro comme notre fin à la fonction.

Et je vais devoir rendre cela un peu plus petit.

Et enfin, nous arrivons à l'appel où nous passons zéro comme notre in à la fonction.

À ce stade, si n est égal à zéro, cette fonction va simplement retourner.

Donc, pour comprendre la complexité spatiale, c'est en fait assez simple.

Donc, puisque c'est une fonction récursive, chacun de ces appels existe sur la pile d'appels simultanément.

Donc, cela signifie que si nous appelons notre fonction countdown avec cinq, elle va ensuite s'appeler elle-même avec quatre et à ce stade, cet appel initial existe toujours sur la pile d'appels.

Et même pour lorsque nous appelons trois.

Ces deux appels existent toujours sur la pile d'appels, et ainsi de suite jusqu'à ce que nous atteignions notre cas de base.

Chacun de ces appels existe toujours sur la pile d'appels.

Et chacun de ces appels prend de la mémoire.

Donc, chacun de ces appels existant sur la pile, ils prennent de la mémoire.

Et c'est ainsi que nous arrivons à une compréhension de la complexité spatiale en utilisant cette fonction récursive comme exemple, car si nous retournons à ce stade, lorsque nous atteignons notre cas de base, cela signifie qu'il y a 123455 appels qui prennent de la place sur notre pile d'appels, et cinq est également notre valeur pour n.

Donc, cela signifierait que cette fonction, sa complexité spatiale est O de n.

Donc, cette fonction a une complexité spatiale de obon.

Donc, la chose la plus importante à retenir ici est que tous ces appels récursifs existent sur la pile d'appels simultanément.

Et chacun d'entre eux prend de la mémoire, c'est pourquoi, si nous avons, si nous passons cinq, deux comme notre n, nous aurons cinq appels existant en mémoire simultanément, ce qui signifie que notre complexité spatiale va être sur alors elle va évoluer linéairement avec la taille de l'entrée.

Donc, si nous augmentons la taille de cette entrée, l'espace requis pour exécuter cette fonction va évoluer proportionnellement avec la taille de cette entrée.

Donc, maintenant que nous avons une compréhension de la complexité spatiale, nous pouvons aborder certaines erreurs courantes que les gens font avec Bingo.

Et la première étant que lorsque vous commencez avec Viggo, vous pourriez voir une fonction qui ressemble à ceci et qui a deux boucles for.

Et vous pourriez instinctivement supposer que cette fonction est de complexité temporelle O de n carré, car vous voyez qu'il y a deux boucles for ici.

Donc, cela doit signifier observer en carré.

Mais en réalité, comme nous l'avons appris, O de n carré signifie en fait que pour chaque itération, jusqu'à la taille de notre entrée, nous allons itérer à travers une boucle for supplémentaire jusqu'à la taille de notre entrée.

Donc, que signifie-t-il si nous avons deux boucles for qui ne sont pas imbriquées et qui ne sont pas O de n carré, c'est en fait assez simple.

Donc, nous avons une boucle for ici, et nous avons une autre boucle for ici.

Et comme nous le savons déjà, cette boucle for serait O de n, complexité temporelle.

Et celle-ci serait également O de n.

Donc, à ce stade, nous avons deux événements, donc cela pourrait facilement être traduit en o de deux in, ce qui est simplement all de deux fois in donc deux fois nous avons all of in.

Mais si nous nous souvenons de nos leçons précédentes, nous ignorons les constantes.

Et dans ce cas, multiplier in par deux, deux est juste une constante.

Donc, nous pouvons en fait simplement supprimer cette constante, auquel cas, cela devient simplement over then.

Mais il y a une chose importante que nous devons reconnaître ici.

C'est all then parce que nous itérons à travers la même entrée pour ces deux boucles for.

Donc, tant que nos boucles agissent sur la même entrée, alors ce serait la complexité résultante.

Mais il y a en fait une autre erreur courante que les gens font lorsqu'ils prennent en considération la complexité temporelle, qui est quelque peu liée à cette erreur.

Et cette erreur courante implique d'avoir deux entrées séparées pour la fonction.

Donc, prenons d'abord en considération cette fonction d'addition à deux entrées.

Donc, si vous vous souvenez de notre dernier exemple, nous n'avions qu'une entrée, nous n'avions qu'une seule entrée, qui était a et les deux boucles for parcourent cette même entrée.

Mais pour celle-ci, vous pouvez voir que nous avons deux entrées séparées ici.

Donc, nous avons une entrée a, qui est parcourue dans cette boucle for supérieure.

Et nous avons une entrée B, qui est parcourue dans cette deuxième boucle for.

Et certaines personnes pourraient faire l'erreur de penser que c'est la même chose que la dernière situation où le résultat serait o de deux in.

Mais cela est en fait faux.

Parce que dans cette situation particulière, nous n'avons aucun moyen de connaître la différence de taille entre ces deux entrées, comme tout ce que nous savons, c'est que ce sont deux entrées séparées.

Donc, ces deux entrées séparées pourraient être soit de tailles complètement différentes, soit de la même taille.

Mais de notre perspective d'analyse, nous n'en avons aucune idée.

Donc, dans cette situation, lorsque nous avons deux entrées, et que nous avons une boucle for séparée pour chaque entrée, nous allons devoir garder une trace des deux entrées.

Donc, dans ce cas, le temps qu'il faudrait pour parcourir ces deux boucles for est O de A plus B, car nous devons d'abord parcourir celle-ci jusqu'à ce que nous atteignions la valeur de a et ensuite nous devons parcourir celle-ci jusqu'à ce que nous atteignions la valeur de V de B et à ce stade, cela ne peut pas être simplifié davantage, nous devons reconnaître le fait que ces deux entrées sont des entrées séparées.

Donc, ce serait over a plus b.

Et ici, nous avons une situation similaire où nous avons deux entrées, mais cette fois, les boucles for sont imbriquées.

Et beaucoup de gens font l'erreur de dire qu'une fonction qui ressemble à ceci est O de n carré.

Mais cela serait en fait faux aussi, car que signifie O de n carré ? O de n carré signifie que pour chaque itération d'une entrée, nous allons itérer à travers cette même entrée exacte.

Mais dans cette situation, lorsque nous avons a, nous avons deux entrées séparées.

Pour chaque itération de l'une des entrées, nous allons itérer à travers l'autre entrée.

Donc, ce que cela signifie, c'est que c'est faux.

En réalité, c'est o de A fois V, car encore une fois, nous devons spécifier que ce sont deux entrées différentes.

Et ces entrées pourraient être de tailles différentes.

Et nous devons rendre cela visible lorsque nous prenons notre complexité en considération.

Donc, c'est la complexité spatiale et quelques erreurs courantes que les gens font avec la notation Big O.

J'espère que cela a du sens.