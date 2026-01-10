---
title: 'Comment penser en graphes : Une introduction illustrative à la théorie des
  graphes et ses applications'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-21T18:11:38.000Z'
originalURL: https://freecodecamp.org/news/i-dont-understand-graph-theory-1c96572a1401
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Z6qfDmoZcZheiTxEcPOQJQ.png
tags:
- name: algorithms
  slug: algorithms
- name: data
  slug: data
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Comment penser en graphes : Une introduction illustrative à la théorie
  des graphes et ses applications'
seo_desc: 'By Vardan Grigoryan (vardanator)

  Graph theory represents one of the most important and interesting areas in computer
  science. But at the same time it’s one of the most misunderstood (at least it was
  to me).

  Understanding, using and thinking in graphs...'
---

Par Vardan Grigoryan (vardanator)

La théorie des graphes représente l'un des domaines les plus importants et intéressants en informatique. Mais en même temps, c'est l'un des plus mal compris (du moins, c'était le cas pour moi).

Comprendre, utiliser et penser en graphes nous rend meilleurs programmeurs. Du moins, c'est ainsi que nous devons penser. Un graphe est un ensemble de sommets V et un ensemble d'arêtes E, formant une paire ordonnée G=(V, E).

En essayant d'étudier la théorie des graphes et en implémentant certains algorithmes, je restais régulièrement bloqué, simplement parce que c'était **si** ennuyeux.

La meilleure façon de comprendre quelque chose est de comprendre ses applications. Dans cet article, nous allons démontrer diverses applications de la théorie des graphes. Mais plus important encore, ces applications contiendront des illustrations détaillées. Alors, commençons et plongeons-nous dans le sujet.

Bien que cette approche puisse sembler trop détaillée (pour les programmeurs expérimentés), croyez-moi, en tant que personne qui a déjà été là et essayé de comprendre la théorie des graphes, les explications détaillées sont toujours préférables aux définitions succinctes.

Donc, si vous avez cherché un « tutoriel sur la théorie des graphes et tout ce qui s'y rapporte pour les débutants absolus et incroyables », alors vous êtes au bon endroit. Ou du moins, je l'espère. Alors, commençons et plongeons-nous dans le sujet.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Oq1WosxCfpi8N8tIRhSlWQ.png)
_Il voulait dire Monte Cristo_

### Table des matières

* [Avertissements](https://medium.com/p/1c96572a1401#0239)
* [Les sept ponts de Königsberg](https://medium.com/p/1c96572a1401#48f5)
* Représentation des graphes : Introduction
* [Introduction à la représentation des graphes et aux arbres binaires (exemple Airbnb)](https://medium.com/p/1c96572a1401#0374)
* [Représentation des graphes : Conclusion](https://medium.com/p/1c96572a1401#fb0c)
* [Exemple Twitter : problème de livraison de tweets](https://medium.com/p/1c96572a1401#0cd4)
* [Algorithmes de graphes : introduction](https://medium.com/p/1c96572a1401#fb0c)
* [Netflix et Amazon : exemple d'index inversé](https://medium.com/p/1c96572a1401#cdde)
* [Parcours : DFS et BFS](https://medium.com/p/1c96572a1401#45f6)
* [Uber et le problème du plus court chemin (algorithme de Dijkstra)](https://medium.com/p/1c96572a1401#aa4d)

### Avertissements

**AVERTISSEMENT 1 :** _Je ne suis pas un expert en informatique, en algorithmes, en structures de données et surtout en théorie des graphes. Je ne suis impliqué dans aucun projet pour les entreprises discutées dans cet article. Les solutions aux problèmes ne sont pas définitives et pourraient être considérablement améliorées. Si vous trouvez un problème ou quelque chose d'irraisonnable, vous êtes plus que bienvenu pour laisser un commentaire. Si vous travaillez dans l'une des entreprises mentionnées ou êtes impliqué dans des projets logiciels correspondants, veuillez répondre avec la solution réelle (ce sera utile aux autres). À tous les autres, soyez des lecteurs patients, cet article est assez LONG._

**AVERTISSEMENT 2 :** _Cet article est quelque peu différent dans le style de présentation de l'information. Parfois, il peut sembler un peu éloigné du sous-sujet, mais les lecteurs patients finiront par avoir une compréhension complète de la situation globale._

**AVERTISSEMENT 3 :** _Cet article est écrit pour un large public de programmeurs. Bien que les programmeurs juniors soient le public cible, j'espère qu'il sera également intéressant pour les professionnels expérimentés._

### Les sept ponts de Königsberg

Commençons par quelque chose que je rencontrais régulièrement dans les livres de théorie des graphes discutant des « origines de la théorie des graphes », les [Sept ponts de Königsberg](https://en.wikipedia.org/wiki/Seven_Bridges_of_K%C3%B6nigsberg) (je ne suis pas vraiment sûr, mais vous pouvez le prononcer comme « qyonigsberg »). Il y avait sept ponts à [Kaliningrad](https://en.wikipedia.org/wiki/Kaliningrad), reliant deux grandes îles entourées par la rivière Pregolya et deux parties de terres principales divisées par la même rivière.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Yiwa1Lzpj6XHAXW3G9KcqA.png)
_[Notre zone d'intérêt](https://www.google.com.au/maps/@54.7066964,20.5100082,16z" rel="noopener" target="_blank" title=")_

Au 18ème siècle, cela s'appelait Königsberg (partie de la Prusse) et la zone ci-dessus avait beaucoup plus de ponts. Le problème ou simplement un casse-tête avec les ponts de Königsberg était de pouvoir traverser la ville en franchissant les sept ponts une seule fois. Ils n'avaient pas de connexion internet à cette époque, donc cela devait être divertissant. Voici la vue illustrée des sept ponts de Königsberg au 18ème siècle.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_8_S3LGba5fYlF9epPXPAA.png)
_Les sept ponts de Königsberg_

Essayez. Voyez si vous pouvez traverser la ville en franchissant chaque pont une seule fois.

* Il ne doit pas y avoir de pont(s) non franchi(s).
* Chaque pont ne doit pas être franchi plus d'une fois.

Si vous êtes familier avec ce problème, vous savez qu'il est impossible de le faire. Bien que vous ayez essayé suffisamment fort et que vous puissiez essayer encore plus maintenant, vous finirez par abandonner.

![Image](https://cdn-media-1.freecodecamp.org/images/1*c3Vl36-jIeBzQ_rsNYml5A.jpeg)
_Leonhard Euler (photo de Wikipedia)_

Parfois, il est raisonnable d'abandonner rapidement. C'est ainsi qu'Euler a résolu ce problème - il a abandonné assez tôt. Au lieu d'essayer de le résoudre, il a adopté une approche différente en essayant de prouver qu'il n'est pas possible de traverser la ville en franchissant chaque pont une seule fois.

Essayons de comprendre comment Euler réfléchissait et comment il a trouvé la solution (s'il n'y a pas de solution, cela nécessite toujours une preuve). C'est un vrai défi ici, car suivre le processus de pensée d'un mathématicien aussi vénérable est quelque peu malhonnête. (Vénérable au point que [Knuth et ses amis ont dédié leur livre](https://www.amazon.com/Concrete-Mathematics-Foundation-Computer-Science/dp/0201558025/) à [Leonhard Euler](https://en.wikipedia.org/wiki/Leonhard_Euler)). Nous allons plutôt prétendre « penser comme Euler ». Commençons par imaginer l'impossible.

![Image](https://cdn-media-1.freecodecamp.org/images/1*RPIPDVcZbWM0hy519YoZIA.png)

Il y a quatre lieux distincts, deux îles et deux parties de la terre ferme. Et sept ponts. Il est intéressant de découvrir s'il existe un motif concernant le nombre de ponts connectés aux îles ou à la terre ferme (nous utiliserons le terme « terre » pour désigner les quatre lieux distincts).

![Image](https://cdn-media-1.freecodecamp.org/images/1*TQzVW18ZSpYIuOFY5ZJJJg.png)
_Nombre de ponts_

À première vue, il semble y avoir une sorte de motif. Il y a un nombre impair de ponts connectés à chaque terre. Si vous devez franchir chaque pont une fois, alors vous pouvez entrer sur une terre et la quitter si elle a 2 ponts.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jDQ0LcOdE1Ln3_27yVcnJg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*tqshIPv13IkTZIZaFIej_Q.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*Vs7ZeH7lHhAAXGLXH2Lyhw.png)
_Exemples de terres à 2 ponts_

Il est facile de voir dans les illustrations ci-dessus que si vous entrez sur une terre en franchissant un pont, vous pouvez toujours quitter la terre en franchissant son deuxième pont. Chaque fois qu'un troisième pont apparaît, vous ne pourrez pas quitter une terre une fois que vous y êtes entré en franchissant tous ses ponts. Si vous essayez de généraliser ce raisonnement pour un seul morceau de terre, vous pourrez montrer que, dans le cas d'un nombre pair de ponts, il est toujours possible de quitter la terre et dans le cas d'un nombre impair de ponts, ce n'est pas possible. Essayez-le dans votre esprit !

Ajoutons un nouveau pont pour voir comment le nombre total de ponts connectés change et si cela résout le problème.

![Image](https://cdn-media-1.freecodecamp.org/images/1*olODXmFJsEj28jF70Sg9dw.png)
_Remarquez le nouveau pont_

Maintenant que nous avons deux nombres pairs (4 et 4) et deux nombres impairs (3 et 5) de ponts reliant les quatre morceaux de terre, dessinons un nouvel itinéraire avec l'ajout de ce nouveau pont.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0tIgvHoB7uGpedZx1ZnLug.png)
_Wow_

Nous avons vu que le nombre de ponts pairs et impairs jouait un rôle dans la détermination de la possibilité de la solution. Voici une question. Le nombre de ponts résout-il le problème ? Doit-il être pair tout le temps ? Il s'avère que ce n'est **pas** le cas. C'est ce qu'Euler a fait. Il a trouvé un moyen de montrer que le nombre de ponts compte. Et plus intéressant encore, le nombre de morceaux de **terre** avec un nombre impair de ponts connectés compte également. C'est alors qu'Euler a commencé à « convertir » les terres et les ponts en quelque chose que nous connaissons sous le nom de graphes. Voici à quoi pourrait ressembler un graphe représentant le problème des ponts de Königsberg (notez que notre pont « temporairement » ajouté n'y est pas).

![Image](https://cdn-media-1.freecodecamp.org/images/1*DZ0h0t88ZtzLNQhgalPztg.png)
_Les lignes sont un peu tordues_

Une chose importante à noter est la généralisation/abstraction d'un problème. Chaque fois que vous résolvez un problème spécifique, la chose la plus importante est de généraliser la solution pour des problèmes similaires. Dans ce cas particulier, la tâche d'Euler était de généraliser le problème de franchissement des ponts pour pouvoir résoudre des problèmes similaires à l'avenir, c'est-à-dire pour tous les ponts du monde. La visualisation aide également à voir le problème sous un angle différent. Les graphes suivants sont toutes les diverses représentations du même problème des ponts de Königsberg montré ci-dessus.

![Image](https://cdn-media-1.freecodecamp.org/images/1*h8-Y7kfLY81IeZ61y6RhPA.png)

Donc oui, visuellement, les graphes sont un bon choix pour illustrer les problèmes. Mais maintenant, nous devons découvrir comment le problème de Königsberg peut être résolu en utilisant des graphes. Faites attention au nombre de lignes sortant de chaque cercle. Et oui, nommons-les comme le feraient des professionnels expérimentés, à partir de maintenant, nous appellerons les cercles, **sommets** et les lignes qui les relient, **arêtes**. Vous avez peut-être vu des notations de lettres, **V** pour (vendetta ?) sommet, **E** pour arête.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UlIW_fTvf-URBTJHFU-mDg.png)

La chose importante suivante est le soi-disant **degré** d'un **sommet**, le nombre d'arêtes **incidentes** connectées au sommet. Dans notre exemple ci-dessus, le nombre de ponts connectés aux terres peut être exprimé comme les degrés du sommet du graphe.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ESq5g9Vi988AHHXTA1cfLw.png)

Dans son entreprise, Euler a montré que la possibilité d'une marche à travers le graphe (ville) traversant chaque arête (pont) une et une seule fois dépend strictement des degrés des sommets (terres). Le chemin constitué de telles arêtes s'appelle (en son honneur) un chemin d'Euler. La longueur d'un chemin d'Euler est le nombre d'arêtes. Préparez-vous pour un langage strict. ?

> Un chemin d'Euler d'un graphe non orienté fini G(V, E) est un chemin tel que chaque arête de G apparaît une fois. Si G a un chemin d'Euler, alors il est appelé un graphe d'Euler. [1]

> **Théorème**. Un graphe non orienté fini connecté est un graphe d'Euler si et seulement si **exactement deux** sommets sont de **degré impair** ou **tous les sommets** sont de **degré pair**. Dans ce dernier cas, chaque chemin d'Euler du graphe est un circuit, et dans le premier cas, aucun ne l'est. [1]

![Image](https://cdn-media-1.freecodecamp.org/images/1*v-TkQFTU_sNzgKJiyDkkwA.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*mq6Gk_irYP3jwEIk33apqA.png)
_Exactement deux sommets ont un degré impair dans l'illustration de gauche, et tous les sommets sont de degré impair dans l'illustration de droite_

_J'ai utilisé « chemin d'Euler » au lieu de « chemin eulérien » juste pour être cohérent avec la définition des livres référencés [1]. Si vous connaissez quelqu'un qui différencie le chemin d'Euler et le chemin eulérien, et le graphe d'Euler et le graphe eulérien, dites-leur de laisser un commentaire._

Tout d'abord, clarifions les nouveaux termes dans la définition et le théorème ci-dessus.

* **Graphe non orienté** - un graphe qui n'a pas de direction particulière pour les arêtes.
* **Graphe orienté** - un graphe dans lequel les arêtes ont une direction particulière.
* **Graphe connecté** - un graphe où il n'y a pas de sommet inaccessible. Il doit y avoir un chemin entre chaque paire de sommets.
* **Graphe non connecté** - un graphe où il y a des sommets inaccessibles. Il n'y a pas de chemin entre chaque paire de sommets.
* **Graphe fini** - un graphe avec un nombre fini de nœuds et d'arêtes.
* **Graphe infini** - un graphe où une extrémité du graphe dans une ou plusieurs directions s'étend à l'infini.

Nous discuterons de certains de ces termes dans les paragraphes suivants.

Les graphes peuvent être orientés et non orientés, et c'est l'une des propriétés intéressantes des graphes. Vous devez avoir vu un exemple populaire de Facebook vs Twitter pour les graphes orientés et non orientés. Une relation d'amitié Facebook peut être facilement représentée comme un graphe non orienté, car si Alice est amie avec Bob, alors Bob doit être ami avec Alice aussi. Il n'y a pas de direction, les deux sont amis l'un avec l'autre.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NsSbLC2ssMmNIUTBl3jrnQ.png)
_Graphe non orienté_

Remarquez également le sommet étiqueté « Patrick », il est un peu spécial (il n'a pas d'amis), car il n'a aucune arête incidente. Il fait toujours partie du graphe, mais dans ce cas, nous dirons que ce graphe n'est pas connecté, c'est un **graphe non connecté** (même chose pour « John », « Ashot » et « Beth » car ils sont interconnectés entre eux mais séparés des autres). Dans un graphe **connecté**, il n'y a pas de sommet inaccessible, il doit y avoir un chemin entre chaque paire de sommets.

Contrairement à l'exemple de Facebook, si Alice suit Bob sur Twitter, cela n'oblige pas Bob à suivre Alice en retour. Donc une relation de « suivi » doit avoir un indicateur de direction, montrant quel sommet (utilisateur) a une arête dirigée (suit) vers l'autre sommet.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NogzJ2ZbrTrwh43ph-XAIQ.png)

Maintenant, sachant ce qu'est un graphe **fini** **connecté** **non orienté**, revenons au graphe d'Euler :

![Image](https://cdn-media-1.freecodecamp.org/images/1*h_S6hGd0Y1uDl9Pltn8QYw.png)

Alors pourquoi avons-nous discuté du problème des ponts de Königsberg et des graphes d'Euler en premier lieu ? Eh bien, ce n'est pas si ennuyeux et en enquêtant sur le problème et la solution précédente, nous avons abordé les éléments derrière les graphes (sommet, arête, dirigé, non dirigé) en évitant une approche théorique sèche. Et non, nous n'avons pas encore terminé avec les graphes d'Euler et le problème ci-dessus. ?

Nous devons maintenant passer à la représentation informatique des graphes, car c'est le sujet qui nous intéresse en tant que programmeurs. En représentant un graphe dans un programme informatique, nous pourrons concevoir un algorithme pour tracer le(s) chemin(s) du graphe, et ainsi découvrir s'il s'agit d'un chemin d'Euler. Avant cela, essayez de penser à une bonne application pour un graphe d'Euler (en plus de jouer avec les ponts).

### Représentation des graphes : Introduction

Maintenant, c'est une tâche assez fastidieuse, alors soyez patient. Vous vous souvenez du combat entre les tableaux et les listes chaînées ? Utilisez des tableaux si vous avez besoin d'un accès rapide aux éléments, utilisez des listes si vous avez besoin d'une insertion/suppression rapide d'éléments, etc. Je crois à peine que vous ayez jamais eu du mal avec quelque chose comme « comment représenter des listes ». Eh bien, dans le cas des graphes, la représentation réelle est vraiment gênante, car d'abord vous devez décider comment exactement vous allez représenter un graphe. Et croyez-moi, vous n'allez pas aimer ça. Liste d'adjacence, matrice d'adjacence, peut-être des listes d'arêtes ? Lancez une pièce.

Vous auriez dû lancer fort, car nous commençons avec un arbre. Vous devez avoir vu un arbre binaire (ou BT pour faire court) au moins une fois (ce qui suit n'est pas un arbre binaire de **recherche**).

![Image](https://cdn-media-1.freecodecamp.org/images/1*xWoN44k1_pdTG8PwZeutxw.png)
_Juste un exemple_

Juste parce qu'il est composé de sommets et d'arêtes, c'est un graphe. Vous pouvez également vous rappeler comment un arbre binaire est le plus couramment représenté (au moins dans les manuels).

Cela peut sembler trop basique pour les personnes qui sont déjà familières avec les arbres binaires, mais je dois tout de même l'illustrer pour m'assurer que nous sommes sur la même longueur d'onde (notez que nous traitons toujours du pseudocode).

Si vous êtes nouveau dans les arbres, lisez attentivement le pseudocode ci-dessus, puis suivez les étapes dans l'illustration ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*qGSs9H5TJrkC226E1Tr5bA.png)
_Les couleurs sont juste pour une visualisation claire_

Alors qu'un arbre binaire est une simple « collection » de nœuds, chacun ayant des nœuds enfants gauche et droit. Un arbre binaire de recherche est beaucoup plus utile car il applique une règle simple qui permet des recherches rapides de clés. Les arbres binaires de recherche (BST) maintiennent leurs clés dans l'ordre trié. Vous êtes libre d'implémenter votre BT avec n'importe quelle règle que vous voulez (bien que cela puisse changer son nom en fonction de la règle, par exemple, min-heap ou max-heap). L'attente la plus importante pour un BST est qu'il satisfasse la propriété de **recherche binaire** (c'est de là que vient le nom). La clé de chaque nœud doit être **supérieure à** toute clé dans son sous-arbre gauche et **inférieure à** toute clé dans son sous-arbre droit.

J'aimerais souligner un point très intéressant concernant l'énoncé « supérieur à » qui est crucial pour comprendre le fonctionnement des BST. Chaque fois que vous changez la propriété en « supérieur ou égal », votre BST pourra enregistrer des clés en double lors de l'insertion de nouveaux nœuds, sinon il ne conservera que des nœuds avec des clés uniques. Vous pouvez trouver de très bons articles sur le web concernant les arbres binaires de recherche. Nous ne fournirons pas une implémentation complète d'un arbre binaire de recherche, mais pour des raisons de cohérence, nous illustrerons un simple arbre binaire de recherche ici.

![Image](https://cdn-media-1.freecodecamp.org/images/1*gb8tsJ_MOTcIvZlYC2HkmQ.png)

### Introduction à la représentation des graphes et aux arbres binaires (exemple Airbnb)

Les arbres sont des structures de données très utiles. Vous n'avez peut-être pas implémenté un arbre à partir de zéro dans vos projets. Mais vous les avez probablement utilisés même sans vous en rendre compte. Regardons un exemple artificiel mais précieux et essayons de répondre à la question « pourquoi », « Pourquoi utiliser un arbre binaire de recherche en premier lieu ».

Comme vous l'avez remarqué, il y a une « recherche » dans l'arbre binaire de recherche. Donc, en gros, tout ce qui nécessite une recherche rapide, **devrait** être placé dans un arbre binaire de recherche. « Devrait » ne signifie pas doit, la chose la plus importante à garder à l'esprit en programmation est de résoudre un problème avec les bons outils. Il existe de nombreux cas où une simple liste chaînée avec sa recherche O(N) peut être plus préférable qu'un BST avec sa recherche O(logN).

Typiquement, nous utiliserions une implémentation de bibliothèque d'un BST, très probablement std::set ou std::map en C++. Cependant, dans ce tutoriel, nous sommes libres de **réinventer** notre propre roue. Les BST sont implémentés dans presque toutes les bibliothèques de langages de programmation généralistes. Vous pouvez les trouver dans la documentation correspondante de votre langage préféré. En abordant un « exemple de la vie réelle », voici le problème que nous allons essayer de résoudre - la recherche de maisons Airbnb.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2WwX3k9JJHeLX2d8hYz39Q.png)
_Un aperçu de la recherche de maisons Airbnb_

Comment recherchons-nous des maisons en fonction d'une requête avec un ensemble de filtres aussi rapidement que possible. C'est une tâche difficile. Elle devient plus difficile si nous considérons qu'Airbnb stocke [4 millions de logements](https://press.atairbnb.com/app/uploads/2017/08/4-Million-Listings-Announcement-1.pdf).

![Image](https://cdn-media-1.freecodecamp.org/images/1*-FXZCO9EfVU5cpt-UbsK3Q.png)

Donc, lorsque les utilisateurs recherchent des maisons, il y a une chance qu'ils puissent « toucher » 4 millions d'enregistrements stockés dans la base de données. Bien sûr, les résultats sont limités aux « meilleurs logements » affichés sur la page d'accueil du site web et un utilisateur n'est presque jamais assez curieux pour consulter des millions de logements. Je n'ai aucune analyse concernant Airbnb, mais nous pouvons utiliser un outil puissant en programmation appelé « hypothèses ». Donc, nous supposerons qu'un seul utilisateur trouve une bonne maison en consultant au plus ~1K maisons.

Le facteur le plus important ici est le nombre d'utilisateurs en temps réel, car cela fait une différence dans les choix des structures de données et des bases de données et l'architecture globale du projet. Aussi évident que cela puisse paraître, s'il n'y a que 100 utilisateurs au total, alors nous ne nous embêterons pas du tout.

Au contraire, si le nombre total d'utilisateurs et d'utilisateurs en temps réel en particulier est bien au-delà du seuil du million, nous devons réfléchir très judicieusement à chaque décision. « Chaque » est utilisé exactement à bon escient, c'est pourquoi les entreprises embauchent les meilleurs tout en s'efforçant d'exceller dans la fourniture de services.

Google, Facebook, Airbnb, Netflix, Amazon, Twitter et bien d'autres traitent d'énormes quantités de données et le bon choix pour servir des millions d'octets de données chaque seconde à des millions d'utilisateurs en temps réel commence par l'embauche des bons ingénieurs. C'est pourquoi nous, les programmeurs, luttons avec ces structures de données, algorithmes et résolution de problèmes dans les entretiens possibles, car tout ce dont ils ont besoin est l'ingénieur ayant la capacité de résoudre de tels grands problèmes de la manière la plus rapide et la plus efficace possible.

Voici donc un cas d'utilisation. Un utilisateur visite la page d'accueil (nous parlons toujours d'Airbnb) et essaie de filtrer les maisons pour trouver la meilleure correspondance possible. Comment pourrions-nous gérer ce problème ? (Notez que ce problème est plutôt du côté backend, donc nous ne nous soucierons pas du frontend ou du trafic réseau ou du https sur http ou d'Amazon EC2 sur le cluster maison, etc.)

Tout d'abord, comme nous sommes déjà familiers avec l'un des outils les plus puissants dans l'inventaire des programmeurs (en parlant d'hypothèses plutôt que d'abstractions), commençons par quelques hypothèses :

* Nous traitons des données qui tiennent complètement dans la RAM.
* Notre RAM est suffisamment grande.

Assez grande pour contenir, hmm, combien ? Eh bien, c'est une bonne question. Combien de mémoire sera nécessaire pour stocker les données réelles. Si nous traitons 4 millions d'unités de données (encore une fois, une hypothèse), et si nous connaissons probablement la taille de chaque unité, alors nous pouvons facilement déduire la taille de mémoire requise, c'est-à-dire 4M * sizeof(one_unit).

Considérons un objet « maison » et ses propriétés. En fait, considérons au moins celles des propriétés que nous allons traiter en résolvant notre problème (une « maison » est notre unité). Nous allons le représenter comme une structure C++ dans un pseudocode. Vous pouvez facilement le convertir en un objet de schéma MongoDB ou autre chose que vous voulez. Nous discutons simplement des noms et types de propriétés (essayez de penser à utiliser des champs de bits ou des bitsets pour l'économie d'espace).

La structure ci-dessus n'est pas parfaite (évidemment) et il y a beaucoup d'hypothèses et/ou de parties incomplètes. J'ai simplement regardé les filtres d'Airbnb et conçu des listes de propriétés qui devraient exister pour satisfaire les requêtes de recherche. Ce n'est qu'un exemple.

Maintenant, nous devons calculer combien de bytes en mémoire prendra chaque objet `AirbnbHome`.

* **Nom de la maison** - `name` est un `wstring` pour supporter les noms/titres multilingues, ce qui signifie que chaque caractère prendra 2 bytes (nous ne nous embêterons pas avec la taille des caractères si nous utilisions un autre langage, mais en C++ `char` est un caractère de 1-byte et `wchar` est un caractère de 2-byte). Un rapide coup d'œil aux annonces d'Airbnb nous permet de supposer que le nom d'une maison devrait prendre jusqu'à 100 caractères (bien que la plupart du temps, il est autour de 50, plutôt que 100), nous supposerons 100 caractères comme valeur maximale, ce qui conduit à ~200 bytes de mémoire. `uint` est 4 bytes, `uchar` est 1 byte, `ushort` est 2 bytes (encore, dans nos hypothèses).
* **Photos** - Les photos résident dans un service de stockage, comme Amazon S3 (autant que je sache, cette hypothèse est très probablement vraie pour Airbnb, mais encore une fois, Amazon S3 n'est qu'une hypothèse)
* **URL des photos** - Nous avons ces URL de photos, et en tenant compte du fait qu'il n'y a pas de limite de taille standard sur les URL, mais qu'il existe en fait une limite bien connue de **2083** caractères, nous la prendrons comme taille maximale de toute URL. Donc, en tenant compte du fait que chaque maison a 5 photos en moyenne, cela prendrait jusqu'à ~10Kb.
* **ID des photos** - Réfléchissons à nouveau à cela. Habituellement, les services de stockage servent le contenu avec les mêmes URL de base, comme `http(s)://s3.amazonaws.com/<bucket>/&l`t;object>, c'est-à-dire qu'il existe un motif commun pour construire les URL et nous devons stocker uniquement l'ID réel de la photo. Disons que nous utilisons un générateur d'ID unique, qui retourne une chaîne d'ID unique de 20 bytes où les objets photo et le motif d'URL pour une photo particulière `ressemble à https://s3.amazonaws.com/some-know-bucket/<u`nique-photo-id>. Cela nous donne une bonne efficacité d'espace, donc pour stocker les ID de chaîne de cinq photos, nous aurons besoin de seulement 100 bytes de mémoire.
* **ID de l'hôte** - Le même « truc » (ci-dessus) pourrait être fait avec le `host_id`, c'est-à-dire l'ID utilisateur qui héberge la maison, prend 20 bytes de mémoire (_en fait, nous pourrions simplement utiliser des ID entiers pour les utilisateurs, mais en considérant que certains systèmes de base de données comme MongoDB ont un générateur d'ID unique plutôt spécifique, nous supposons une longueur de chaîne d'ID de 20 bytes comme une valeur « médiane » qui s'adapte à presque tous les systèmes de base de données avec un petit changement. La longueur de l'ID de Mongo est de 24 bytes_). Et enfin, nous prendrons un bitset de taille allant jusqu'à 32 bits comme un objet de 4 bytes et un bitset de taille entre 32 et 64 bits, comme un objet de 8 bytes. Gardez à l'esprit les hypothèses. Nous avons utilisé un bitset dans cet exemple pour toute propriété qui exprime une énumération, mais est capable de prendre plus d'une valeur, en d'autres termes, une sorte de case à cocher à choix multiples.

![Image](https://cdn-media-1.freecodecamp.org/images/1*YcTk591Iy-MzQte5jnXfRg.png)
_Équipements de la maison Airbnb_

**Équipements** - Chaque maison Airbnb conserve une liste des équipements disponibles, par exemple, « fer à repasser », « lave-linge », « tv », « wifi », « cintres », « détecteur de fumée » et même « espace de travail convivial pour ordinateur portable » et ainsi de suite. Il peut y avoir plus de 20 équipements, nous nous en tenons à 20 juste parce que c'est le nombre d'équipements filtrables sur la page des filtres Airbnb. Le bitset nous fait économiser un bon espace, si nous gardons un ordre approprié pour les équipements. Par exemple, si une maison a tous les équipements mentionnés ci-dessus (voir ceux cochés dans la capture d'écran), nous allons simplement définir un bit à la position correspondante dans le bitset.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Lj3oDNQ70FdpOT_lKfdD2w.png)
_Le bitset permet de sauvegarder 20 valeurs différentes en utilisant seulement 20 bits_

Par exemple, vérifier si une maison a un « lave-linge » :

Ou un peu plus professionnellement :

Vous pouvez améliorer le code autant que vous le souhaitez (et corriger les erreurs de compilation). Nous voulions simplement souligner l'idée derrière les bitsets dans ce contexte de problème.

* **Règles de la maison, Type de maison** - La même idée (que nous avons implémentée pour le champ des équipements) s'applique aux « règles de la maison », au « type de maison » et autres.
* **Code du pays, Nom de la ville** - Enfin, le code du pays et le nom de la ville. Comme mentionné dans les commentaires du code ci-dessus (voir les remarques), nous ne stockerons pas la latitude et la longitude pour éviter les requêtes géospatiales (_sujet d'un autre article_). Au lieu de cela, nous sauvegardons le code du pays et le nom de la ville pour affiner la recherche par localisation (en omettant les rues pour simplifier, veuillez m'excuser). [Code du pays](https://en.wikipedia.org/wiki/Country_code) pourrait être représenté par 2 caractères, 3 caractères ou 3 chiffres, nous sauvegarderons une représentation numérique et utiliserons un `ushort` pour cela. (Mal)heureusement, il y a beaucoup plus de villes que de pays, donc nous ne pouvons pas utiliser un « code de ville » (bien que nous puissions en créer un pour un usage interne). Au lieu de cela, nous stockerons le nom réel de la ville, en conservant 50 bytes en moyenne pour un nom de ville et pour des cas super-spécifiques comme [Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu](https://en.wikipedia.org/wiki/Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu) (ville de 85 lettres). Nous ferions mieux d'utiliser une variable booléenne supplémentaire qui indique qu'il s'agit de cette ville super-longue spécifique (n'essayez pas de la prononcer). Donc, en gardant à l'esprit le surcoût mémoire des chaînes et des vecteurs. Nous ajouterons 32 bytes supplémentaires (au cas où) à la taille finale de la structure. Nous supposerons également que nous travaillons sur un système 64 bits, bien que nous ayons choisi des valeurs très compactes pour `int` et `short`.

Donc, **420**+ bytes avec un surcoût de **32** bytes, **452** bytes et en tenant compte du fait que certains d'entre vous pourraient être obsédés par le facteur d'alignement, arrondissons à **500 bytes**. Donc chaque objet « maison » prend jusqu'à 500 bytes, et pour toutes les annonces de maisons (_il pourrait y avoir des moments de confusion avec le nombre d'annonces et le nombre réel de maisons, faites-moi simplement savoir si j'ai fait une erreur_), 500 bytes * 4 millions = 1,86GB ~ **2GB**. Cela semble plausible. Nous avons fait beaucoup d'hypothèses lors de la construction de la structure, la rendant moins chère à stocker en mémoire, j'espérais vraiment plus de 2 Gigaoctets et si j'ai fait une erreur dans les calculs, faites-le moi savoir. En tout cas, en avançant, donc quoi que nous fassions avec ces données, nous aurons besoin d'au moins 2 GB de mémoire. Si vous vous êtes ennuyé, faites avec. Nous commençons tout juste.

Maintenant, la partie la plus difficile de la tâche. Choisir la bonne structure de données pour ce problème (filtrer les annonces aussi efficacement que possible) n'est pas la tâche la plus difficile. La tâche la plus difficile est (pour moi) de rechercher des annonces avec un ensemble de filtres. S'il n'y avait qu'une seule clé de recherche (un seul filtre), nous pourrions facilement le résoudre. Supposons que la seule chose qui intéresse les utilisateurs est le prix, donc tout ce dont nous avons besoin est de trouver les objets `AirbnbHome` avec des prix dans la fourchette fournie. Si nous utilisons un arbre binaire de recherche pour cela, voici à quoi cela pourrait ressembler.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6cm5jXJsovsulzqUQNo2ww.png)

Si vous imaginez tous les 4 millions d'objets, cet arbre devient très très grand. Au fait, le surcoût de mémoire augmente également, simplement parce que nous avons utilisé un BST pour stocker les objets. Comme chaque nœud parent de l'arbre a deux pointeurs supplémentaires vers ses enfants gauche et droit, cela ajoute jusqu'à 8 octets supplémentaires pour chaque pointeur enfant (en supposant un système 64 bits). Pour 4 millions de nœuds, cela fait environ **~62 Mb**, ce qui, comparé aux 2Gb de données d'objets, semble assez petit, bien que ce ne soit pas quelque chose que nous pouvons « omettre » facilement.

L'arbre dans la dernière illustration montre jusqu'à présent que tout élément peut être facilement trouvé en O(logN) de complexité. Si vous n'êtes pas familier ou n'êtes pas assez sûr pour discuter en big-ohs, nous allons le clarifier ci-dessous, sinon passez la sous-section de complexité.

**Complexité algorithmique** - Faisons cela rapidement car il y aura une longue et détaillée explication dans un prochain article : « Complexité algorithmique et performance logicielle : Le manuel manquant ». Pour la plupart des cas, trouver la complexité big O pour un algorithme est quelque peu facile. La première chose à noter est que nous considérons toujours le pire cas, c'est-à-dire le nombre maximum d'opérations qu'un algorithme effectue pour produire un résultat positif (pour résoudre le problème).

Supposons qu'un tableau a 100 éléments dans un ordre non trié. Combien de comparaisons faudrait-il pour trouver un élément (en tenant également compte du fait que l'élément requis pourrait être manquant) ? Il faudrait jusqu'à 100 comparaisons car nous devrions comparer la valeur de chaque élément avec la valeur que nous recherchons. Et malgré le fait que l'élément pourrait être le premier élément du tableau (menant à une seule comparaison), nous ne considérerons que le pire cas possible (l'élément est soit manquant, soit réside à la dernière position du tableau).

![Image](https://cdn-media-1.freecodecamp.org/images/1*ty0mOl97RJvfnECai3VxqQ.png)

Le but de « calculer » la complexité algorithmique est de trouver une **dépendance** entre le **nombre d'opérations** et la **taille de l'entrée**, par exemple, le tableau ci-dessus avait 100 éléments et le nombre d'opérations était également de 100, si le nombre d'éléments du tableau (son entrée) augmente à 1423, le nombre d'opérations pour trouver un élément quelconque augmentera également à 1423 (le pire cas). Donc la ligne fine entre l'entrée et le nombre d'opérations est claire dans ce cas, elle est dite **linéaire**, le nombre d'opérations augmente autant que l'entrée du tableau. Croissance. C'est le point clé de la complexité, nous disons que la recherche d'un élément dans un tableau non trié prend O(N) temps pour souligner que le processus de recherche prendra jusqu'à N opérations (ou même jusqu'à N opérations fois une certaine valeur constante telle que 3N). D'un autre côté, l'accès à un élément quelconque dans un tableau prend un temps constant, c'est-à-dire O(1). C'est à cause de la structure d'un tableau. C'est une structure de données contiguë, et contient des éléments du même type (attention aux tableaux JS), donc « sauter » à un élément particulier nécessite uniquement de calculer sa position relative par rapport au premier élément du tableau.

![Image](https://cdn-media-1.freecodecamp.org/images/1*I8cUohRCKnF8FUznv6-dEA.png)

Une chose est très claire. Un arbre binaire de recherche maintient ses nœuds dans l'ordre trié. Donc quelle serait la complexité algorithmique de la recherche d'un élément dans un arbre binaire de recherche ? Nous devons calculer le nombre d'opérations nécessaires pour trouver un élément (dans le pire des cas).

Regardez l'illustration ci-dessus. Lorsque nous commençons notre recherche à la racine, la première comparaison peut mener à trois cas,

1. Le nœud est trouvé.
2. La comparaison se poursuit vers le sous-arbre gauche du nœud si l'élément requis est inférieur à la valeur du nœud
3. La comparaison se poursuit vers le sous-arbre droit du nœud si la valeur que nous recherchons est supérieure à la valeur du nœud.

À chaque étape, nous réduisons de moitié la taille des nœuds à considérer. Le nombre d'opérations (c'est-à-dire de comparaisons) nécessaires pour trouver un élément dans le BST est égal à la hauteur de l'arbre. La hauteur d'un arbre est le nombre de nœuds sur le chemin le plus long. Dans ce cas, c'est 4. Et la hauteur est [base 2] logN + 1, comme indiqué. Donc la complexité de la recherche est O(logN + 1) = O(logN). Cela signifie que la recherche de quelque chose dans 4 millions de nœuds nécessite log4000000 = ~**22** comparaisons dans le pire des cas.

**Retour à l'arbre** - Le temps d'accès aux éléments dans un arbre binaire de recherche est O(logN). Pourquoi ne pas utiliser des tables de hachage ? Les tables de hachage ont un temps d'accès constant, ce qui les rend raisonnables à utiliser presque partout.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MoSZx3_lIQtpkHUQg5A0iw.png)

Dans ce problème, nous devons prendre en compte une exigence importante. Nous devons être capables de faire des recherches par plage, par exemple, des maisons avec des prix de 80 $ à 162 $. Dans le cas d'un BST, il est facile d'obtenir tous les nœuds dans une plage en faisant simplement un parcours inordre de l'arbre et en gardant un compteur. Pour une table de hachage, c'est quelque peu coûteux, ce qui rend raisonnable de rester avec les BST dans ce cas.

Bien qu'il y ait un autre point, qui nous amène à repenser les tables de hachage. La densité. Les prix ne monteront pas « pour toujours », la plupart des maisons se situent dans la même fourchette de prix. Regardez la capture d'écran, l'histogramme nous montre la réalité des prix, des millions de maisons sont dans la même fourchette (+/- 18 $ - 212 $), elles ont le même prix moyen. Les tableaux simples peuvent jouer un bon rôle. En supposant l'index d'un tableau comme le prix et la valeur comme la liste des maisons, nous pourrions accéder à n'importe quelle fourchette de prix en temps constant (bien, presque constant). Voici à quoi cela ressemble (très abstrait) :

![Image](https://cdn-media-1.freecodecamp.org/images/1*GWjOQqisi3Hi5f3Ic5P6_Q.png)

Tout comme une table de hachage, nous accédons à chaque ensemble de maisons par leur prix. Toutes les maisons ayant le même prix sont regroupées sous un BST séparé. Cela nous fera également économiser de l'espace si nous stockons les identifiants des maisons au lieu de l'objet complet défini ci-dessus (la structure `AirbnbHome`). Le scénario le plus probable est de sauvegarder tous les objets complets des maisons dans une table de hachage mappant l'identifiant de la maison à l'objet complet de la maison et de stocker une autre table de hachage (ou mieux, un tableau), qui mappe les prix avec les identifiants des maisons.

Ainsi, lorsque les utilisateurs demandent une fourchette de prix, nous récupérons les identifiants des maisons à partir de la table des prix, nous réduisons les résultats à une taille fixe (c'est-à-dire la pagination, généralement autour de 10 - 30 éléments sont affichés sur une page), nous récupérons les objets complets des maisons en utilisant chaque identifiant de maison.

Gardez simplement une autre chose à l'esprit (pensez-y en arrière-plan). L'équilibrage est crucial pour un BST, car c'est la seule garantie d'avoir des opérations sur l'arbre effectuées en O(logN). Le problème d'un BST non équilibré est évident lorsque vous insérez des éléments dans l'ordre trié. Finalement, l'arbre devient simplement une liste chaînée, ce qui conduit évidemment à des opérations en temps linéaire. Oubliez cela pour l'instant, supposons que tous nos arbres sont parfaitement équilibrés. Jetez un coup d'œil à l'illustration ci-dessus une fois de plus. Chaque élément de tableau représente un grand arbre. Que se passe-t-il si nous changeons l'illustration en quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*CPvsz7H8IuGrFdoa4USKsQ.png)
_Plus comme un graphe_

Cela ressemble à un graphe « plus réaliste ». Cette illustration représente les structures de données et les graphes les plus déguisés, ce qui nous amène à la section suivante.

### Représentation des graphes : Conclusion

La mauvaise nouvelle concernant les graphes est qu'il n'existe pas de définition unique pour la représentation des graphes. C'est pourquoi vous ne pouvez pas trouver un `std::graph` dans la bibliothèque. Nous avons déjà eu l'occasion de représenter un graphe « spécial » appelé BST. Le point est, un arbre est un graphe, mais un graphe n'est pas un arbre. La dernière illustration nous montre que nous avons beaucoup d'arbres sous une seule abstraction, « prix vs maisons » et certains des sommets « diffèrent » dans leur type, les prix sont des nœuds de graphe n'ayant que la valeur de prix et se réfèrent à l'arbre entier des identifiants de maisons (sommets de maisons) qui satisfont le prix particulier. C'est beaucoup plus comme une structure de données hybride, qu'un simple graphe auquel nous sommes habitués dans les exemples de manuels.

C'est le point clé dans la représentation des graphes, il n'y a pas de structure fixe et « de jure » pour la représentation des graphes (contrairement aux BST avec leur représentation basée sur les nœuds spécifiée avec des pointeurs gauche/droit enfant, bien que vous puissiez représenter un BST avec un seul tableau). Vous pouvez représenter un graphe de la manière la plus pratique que vous souhaitez (la plus pratique pour un problème particulier), l'essentiel est que vous le « voyez » comme un graphe. Et par « voir un graphe », nous entendons appliquer des algorithmes spécifiques aux graphes.

Et un arbre N-aire, il est plus susceptible de ressembler à un graphe.

![Image](https://cdn-media-1.freecodecamp.org/images/1*WAGdBjYglJ73UEpOrUh1BA.png)

Et la première chose qui vient à l'esprit pour représenter un nœud d'arbre N-aire est quelque chose comme ceci :

Cette structure représente un seul nœud d'un arbre. L'arbre complet ressemble plus à ceci :

Cette classe est une abstraction autour d'un seul nœud d'arbre nommé `root_`. C'est tout ce dont nous avons besoin pour construire un arbre de n'importe quelle taille. C'est le point de départ de l'arbre. Pour ajouter un nouveau nœud d'arbre, nous devons allouer de la mémoire et ajouter ce nœud à la racine de l'arbre.

Un graphe est très similaire à un arbre N-aire, avec une légère différence. Essayez de la repérer.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Cu05NUgY1SBx3ZzeH8SLgw.png)

Est-ce un graphe ? Non. Je veux dire oui, mais c'est le même arbre N-aire que dans l'illustration précédente, juste un peu tourné. En règle générale, chaque fois que vous voyez un arbre (même s'il s'agit d'un pommier, d'un citronnier ou d'un arbre binaire de recherche), vous pouvez être sûr qu'il s'agit également d'un graphe. Donc, en concevant une structure pour un nœud de graphe (sommet de graphe), nous pouvons proposer la même structure :

Est-ce suffisant pour construire un graphe ? Eh bien, non. Et voici pourquoi. Regardez ces deux graphes des illustrations précédentes, trouvez une différence :

![Image](https://cdn-media-1.freecodecamp.org/images/1*CPvsz7H8IuGrFdoa4USKsQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*Cu05NUgY1SBx3ZzeH8SLgw.png)
_Les deux sont des graphes_

Le graphe dans l'illustration du côté gauche n'a pas de point unique pour « entrer » (c'est plutôt une forêt qu'un seul arbre), au contraire, le graphe dans l'illustration de droite n'a pas de sommets inaccessibles. Cela semble familier.

> Un graphe est **connecté** lorsqu'il existe un chemin entre chaque paire de sommets. [[Wikipedia](https://en.wikipedia.org/wiki/Connectivity_(graph_theory))]

Évidemment, il n'y a pas de chemin entre chaque paire de sommets pour le graphe « prix vs maisons » (si ce n'est pas évident à partir de l'illustration, supposez simplement que les prix ne sont pas connectés les uns aux autres). Autant que ce soit juste un exemple pour montrer que nous ne sommes pas capables de construire un graphe avec une seule structure GraphNode, il y a des cas où nous devons traiter avec des graphes non connectés comme celui-ci. Jetez un coup d'œil à cette classe :

Tout comme un arbre N-aire est construit autour d'un seul nœud (le nœud racine), un graphe connecté peut également être construit autour d'un nœud racine. On dit que les arbres sont « enracinés », c'est-à-dire qu'ils ont un point de départ. Un graphe connecté peut être représenté comme un arbre enraciné (avec quelques propriétés supplémentaires), c'est déjà évident, mais gardez à l'esprit que la représentation réelle peut différer d'un algorithme à l'autre, d'un problème à l'autre même pour un graphe connecté. Cependant, en tenant compte de la nature basée sur les nœuds des graphes, un graphe non connecté peut être représenté comme ceci :

Pour les parcours de graphes comme DFS/BFS, il est naturel d'utiliser une représentation de type arbre. Cela aide beaucoup. Cependant, des cas comme le traçage efficace de chemins nécessitent une représentation différente. Vous vous souvenez du graphe d'Euler ? Pour traquer la « eulérisation » d'un graphe, nous devons tracer un chemin d'Euler à l'intérieur. Cela signifie visiter tous les sommets en traversant chaque arête une seule fois, et lorsque le traçage se termine et que nous avons des arêtes non traversées, alors le graphe n'a pas de chemin d'Euler, et donc n'est pas un graphe d'Euler.

Il existe une méthode encore plus rapide, nous pouvons vérifier les degrés des sommets (supposons que chaque sommet stocke son degré) et comme le dit la définition, si un graphe a des sommets de degré impair et qu'il n'y en a pas exactement deux, alors ce n'est pas un graphe d'Euler. La complexité d'une telle vérification est O(|V|), où |V| est le nombre de sommets du graphe. Nous pouvons suivre les degrés impairs/pairs lors de l'insertion de nouvelles arêtes pour augmenter les vérifications de degré impair/pair à O(1). Éclair rapide. Peu importe, nous allons simplement tracer un graphe, c'est tout. Ci-dessous se trouve à la fois la représentation d'un graphe et la fonction Trace() retournant un chemin.

Attention aux bugs, les bugs sont partout. Ce code contient beaucoup d'hypothèses, par exemple, l'étiquetage, donc par un sommet nous comprenons une étiquette de chaîne. Bien sûr, vous pouvez facilement le mettre à jour pour qu'il soit ce que vous voulez. Cela n'a pas d'importance dans le contexte de cet exemple. Ensuite, le nommage. Comme mentionné dans les commentaires, VELOGraph est pour Vertex Edge Label Only Graph (je l'ai inventé). Le point est, cette représentation de graphe contient une table pour mapper une étiquette de sommet avec les arêtes incidentes à ce sommet, et une liste d'arêtes contenant une paire de sommets (connectés par une arête particulière) et un drapeau qui est utilisé uniquement par la fonction Trace(). Jetez un coup d'œil à l'implémentation de la fonction Trace(). Elle utilise le drapeau de l'arête pour marquer une arête déjà parcourue (les drapeaux doivent être réinitialisés après tout appel à Trace()).

### Exemple Twitter : Problème de livraison de tweets

Voici une autre représentation appelée matrice d'adjacence, qui pourrait être utile dans les graphes orientés, comme celui que nous avons utilisé pour le graphe des abonnés Twitter.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NogzJ2ZbrTrwh43ph-XAIQ.png)
_Graphe orienté_

Il y a 8 sommets dans cet exemple Twitter. Donc tout ce dont nous avons besoin pour représenter ce graphe est une matrice carrée |V|x|V| (|V| nombre de lignes et |V| nombre de colonnes). Si il y a une arête dirigée de **v** à **u**, alors la matrice [v][u] est `true`, sinon elle est `false`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*s--uEeTmQg9f8LhHHGFKtA.png)
_Exemple de Twitter_

Comme vous pouvez le voir, cette matrice est beaucoup trop clairsemée, son compromis est l'accès rapide. Pour voir si Patrick suit Sponge Bob, nous devons simplement vérifier la valeur de `matrix["Patrick"]["Sponge Bob"]`. Pour obtenir la liste des abonnés d'Ann, nous traitons simplement toute la colonne « Ann » (le titre est en jaune). Pour trouver qui est suivi (semble étrange) par Sponge Bob, nous traitons toute la ligne « Sponge Bob ». La matrice d'adjacence pourrait être utilisée pour les graphes non orientés également, et au lieu de définir des 1 si il y a une arête de **v** à **u**, nous devons définir les deux valeurs à 1, par exemple adj_matrix[v][u] = 1, adj_matrix[u][v] = 1. La matrice d'adjacence d'un graphe non orienté est symétrique.

Notez que, au lieu de stocker des uns et des zéros dans une matrice d'adjacence, nous pouvons stocker quelque chose de « plus utile », comme les **poids des arêtes**. L'un des meilleurs exemples pourrait être un graphe de lieux avec des informations de distance.

![Image](https://cdn-media-1.freecodecamp.org/images/1*gMt-tHRL-FeRk-P2-OYprg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*zH3p8q22YGh-UfzsrJ4VDA.png)

Le graphe ci-dessus représente les distances entre les maisons de Patrick, Sponge Bob et autres (également connu sous le nom de **graphe pondéré**). Nous mettons des signes « infini » s'il n'y a pas de route directe entre les sommets. Cela ne signifie pas qu'il n'y a pas de routes du tout, et en même temps, cela ne signifie pas qu'il doit nécessairement y avoir des routes. Cela pourrait être défini lors de l'application d'un algorithme pour trouver une route entre les sommets (il existe même une meilleure façon de stocker les sommets et les arêtes qui leur sont incidentes, appelée matrice d'incidence).

![Image](https://cdn-media-1.freecodecamp.org/images/1*mXDa1tFIZi5ohpamzVz-cQ.jpeg)
_82000Tb. [Source photo](http://www.independent.co.uk/arts-entertainment/tv/news/the-simpsons-death-episode-will-be-bigger-than-game-of-thrones-9304810.html" rel="noopener" target="_blank" title=")_

Alors que la matrice d'adjacence semblait être une bonne utilisation pour le graphe des abonnés de Twitter, maintenir une matrice carrée pour près de 300 millions d'utilisateurs (utilisateurs actifs mensuels) prend 300 * 300 * 1 octets (stockage de valeurs booléennes). Cela fait environ ~82000 Tb (Téraoctets), ce qui équivaut à 1024 * 82000 Gb. Eh bien, je ne sais pas pour votre cluster maison, mon ordinateur portable n'a pas autant de RAM. Des bitsets ? Un [BitBoard](https://github.com/vardanator/ultron/blob/master/src/arrays/bitboard.h) pourrait nous aider un peu, réduisant la taille requise à ~10000 Tb. Toujours beaucoup trop grand. Comme mentionné ci-dessus, une matrice d'adjacence est trop clairsemée. Elle nous oblige à utiliser plus d'espace que nécessaire. C'est pourquoi l'utilisation d'une liste d'arêtes incidentes aux sommets peut être utile. Le point est, une matrice d'adjacence nous permet de conserver à la fois les informations « suit » et « ne suit pas », alors que tout ce dont nous avons besoin est de connaître les informations sur les abonnés, quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*jtt7z3iHFr7xSFSKX95DTA.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*qqTFXXc44_2aqx4dEhPkQw.png)
_Matrice d'adjacence vs liste d'adjacence_

L'illustration du côté droit est appelée une [liste d'adjacence](https://en.wikipedia.org/wiki/Adjacency_list). Chaque liste décrit l'ensemble des voisins d'un sommet dans le graphe. Au fait, l'implémentation réelle de la représentation du graphe sous forme de liste d'adjacence, encore une fois, diffère (faits ridicules). Dans l'illustration, nous avons mis en évidence l'utilisation d'une table de hachage, ce qui est raisonnable, car l'accès à un sommet quelconque sera O(1), et pour la liste des sommets voisins, nous n'avons pas mentionné la structure de données exacte, déviant des listes chaînées aux vecteurs. Le choix vous appartient.

Le point est, pour savoir si Patrick suit Liz, nous devons accéder à la table de hachage (temps constant) et parcourir tous les éléments de la liste en comparant chaque élément avec l'élément « Liz » (temps linéaire). Le temps linéaire n'est pas si mauvais à ce stade, car nous devons parcourir seulement une quantité fixe de sommets adjacents à « Patrick ». Qu'en est-il de la complexité spatiale, est-ce acceptable à utiliser chez Twitter ? Eh bien, nous avons besoin d'au moins 300 millions d'enregistrements de table de hachage, chacun pointant vers un vecteur (choisissant un vecteur pour éviter le surcoût mémoire des pointeurs gauche/droit des listes chaînées) contenant combien ? Pas de statistiques ici, j'ai trouvé juste un nombre moyen d'abonnés Twitter, 707 (googlisé).

Donc si nous considérons que chaque enregistrement de table de hachage pointe vers un tableau de 707 identifiants d'utilisateurs (chacun pesant 8 octets), et supposons que le surcoût de la table de hachage est seulement ses clés, qui sont à nouveau des identifiants d'utilisateurs, donc la table de hachage elle-même prend 300 millions * 8 octets. Globalement, nous avons 300 millions * 8 octets pour la table de hachage + 707 * 8 octets pour chaque clé de table de hachage, soit 300 millions * 8 * 707 * 8 octets = **~12 Tb**. Eh bien, je ne peux pas dire que cela semble mieux, mais oui, cela semble beaucoup mieux que 10 000 Tb.

Honnêtement, je ne sais pas si ce 12Tb est un nombre raisonnable. Mais en tenant compte du fait que je dépense environ 30 $ pour une machine serveur dédiée avec 32 Go de RAM, alors, stocker (partitionné) 12 Tb nécessite au moins 385 de ces serveurs, plus quelques serveurs de contrôle (pour le contrôle de la distribution des données) ce qui fait environ 400. Donc cela me coûtera 12K $ (mensuels).

Eh bien, en tenant compte du fait que les données doivent être répliquées, et que quelque chose peut toujours mal tourner, nous triplerons le nombre de serveurs et ajouterons à nouveau quelques serveurs de contrôle, disons que nous avons besoin d'au moins 1500 serveurs, ce qui nous coûtera 45K $ par mois. Eh bien, définitivement pas bon pour moi car je peux à peine maintenir un serveur, mais cela semble acceptable pour Twitter (ce n'est vraiment rien comparé aux vrais serveurs de Twitter). Supposons que c'est vraiment acceptable pour Twitter.

Maintenant, sommes-nous bien ici ? Pas encore, cela concernait uniquement les données des abonnés. Quelle est la chose principale chez Twitter ? Je veux dire, techniquement, quel est son plus gros problème ? Vous ne serez pas seul si vous dites que c'est la livraison rapide des tweets. Je serai définitivement d'accord avec cela. Et pas rapide, mais ultra-rapide. Supposons que Patrick tweete quelque chose sur ses pensées concernant la nourriture, tous ses abonnés doivent recevoir ce tweet très rapidement. Combien de temps cela prendra-t-il ? Nous sommes libres de faire toute hypothèse ici, et d'utiliser toutes les abstractions que nous voulons, mais nous nous intéressons aux systèmes de production du monde réel, alors, creusons. Voici ce qui se passe généralement lorsque quelqu'un tweete.

![Image](https://cdn-media-1.freecodecamp.org/images/1*rxZGqG1AW6lSlhIl9sQuGA.png)

Encore une fois, je ne sais pas vraiment combien de temps il faut pour qu'un tweet atteigne tous les abonnés, mais les statistiques disponibles publiquement nous disent qu'il y a environ 500 millions de tweets par jour. Par jour ! ?

Donc le processus ci-dessus se produit 500 millions de fois chaque jour. Je ne peux pas vraiment trouver quoi que ce soit sur la vitesse de livraison des tweets. Je me souviens vaguement de quelque chose concernant un maximum de 5 secondes pour qu'un tweet atteigne tous ses abonnés. Et notez également les « cas lourds », les célébrités avec plus d'un million d'abonnés. Ils peuvent tweeter quelque chose sur leur merveilleux petit-déjeuner dans la maison de plage, mais Twitter sue beaucoup pour livrer ce contenu super-utile à des millions d'abonnés.

Pour résoudre le problème de livraison des tweets, nous n'avons pas vraiment besoin du graphe des abonnés, mais plutôt d'un graphe des **abonnés**. Le graphe précédent (avec une table de hachage et un ensemble de listes) nous permet de trouver efficacement tous les utilisateurs suivis par un utilisateur particulier. Mais il ne nous permet pas de trouver efficacement **tous** les utilisateurs qui suivent un utilisateur particulier, pour ce cas, nous devons scanner toutes les clés de la table de hachage. C'est pourquoi nous devons construire un autre graphe, qui est une sorte de symétrique opposé à celui que nous avons construit pour les abonnés. Ce nouveau graphe consistera à nouveau en une table de hachage contenant tous les 300 millions de sommets, chacun pointant vers une liste de sommets adjacents (la structure reste la même), mais cette fois, la liste des sommets adjacents représentera les abonnés.

![Image](https://cdn-media-1.freecodecamp.org/images/1*axs6Z0F87LcnxtHJXoNPKw.png)

Donc, basé sur cette illustration, chaque fois que Liz tweete quelque chose, Sponge Bob et Ann doivent voir ce tweet sur leurs timelines. Une technique courante pour y parvenir est de maintenir des structures séparées pour chaque timeline d'utilisateur. Dans le cas des 300+ millions d'utilisateurs de Twitter, nous pourrions supposer qu'il y a au moins 300+ millions de timelines (pour chaque utilisateur). En gros, chaque fois qu'un utilisateur tweete, nous devons obtenir la liste des abonnés de l'utilisateur et mettre à jour leurs timelines (insérer ce même tweet dans chacune d'elles). Une timeline pourrait être représentée comme une liste chaînée, ou un arbre équilibré (les dates et heures des tweets comme clés de nœud).

Ce n'est qu'une idée de base que nous avons abstraite de la représentation réelle des timelines et bien sûr, nous pouvons rendre la livraison réelle plus rapide si nous utilisons le multithreading. Cela est crucial pour les « cas lourds », car pour des millions d'abonnés, ceux qui résident plus près de la fin sont traités plus tard que ceux qui résident plus près du début de la liste.

Le pseudocode suivant tente d'illuminer cette idée de livraison multithread :

Ainsi, chaque fois que les abonnés actualisent leurs timelines, ils recevront le nouveau tweet.

Il serait juste de dire que nous avons à peine effleuré la surface des problèmes réels chez Airbnb ou Twitter. Cela prend vraiment beaucoup de temps et le travail acharné d'ingénieurs très talentueux pour accomplir de tels grands résultats dans des systèmes complexes comme Twitter, Google, Facebook, Amazon, Airbnb et autres. Gardez cela à l'esprit en lisant cet article.

![Image](https://cdn-media-1.freecodecamp.org/images/1*28Qw4dWbrh3kljvxOuLgjw.png)

Le but de démontrer le problème de livraison de tweets de Twitter est d'embrasser l'utilisation des graphes, même si nous n'avons pas utilisé d'algorithme de graphe, nous avons simplement utilisé une représentation du graphe. Bien sûr, nous avons écrit un pseudocode pour une fonction de livraison de tweets, mais c'est quelque chose que nous avons élaboré pendant le processus de recherche d'une solution.

Ce que je voulais dire par « n'importe quel algorithme de graphe » est n'importe quel algorithme [de cette liste](https://en.wikipedia.org/wiki/List_of_algorithms#Graph_algorithms). Comme quelque chose de suffisamment grand pour faire pleurer les programmeurs, les applications de la théorie des graphes et des algorithmes de graphes sont quelque peu différentes à repérer au premier coup d'œil. Nous discutions des maisons Airbnb et du filtrage efficace avant de terminer avec les représentations de graphes, et la chose évidente principale était l'incapacité à filtrer efficacement les maisons avec plus d'une clé de filtre. Y a-t-il quelque chose qui pourrait être fait en utilisant des algorithmes de graphes ? Eh bien, nous ne pouvons pas en être sûrs, mais au moins nous pouvons essayer. Et si nous représentons chaque filtre comme un sommet séparé ?

Littéralement chaque filtre, même tous les prix de 10 $ à 1000 $+, tous les noms de villes, les codes de pays, les équipements (TV, Wi-Fi, et tous les autres), le nombre d'adultes, et chaque nombre comme un sommet de graphe séparé.

![Image](https://cdn-media-1.freecodecamp.org/images/1*R756x_xP1VA-vlQu6lElJQ.png)
_Extrait des filtres Airbnb_

Nous pouvons même rendre cet ensemble de sommets plus « convivial » si nous ajoutons également des sommets de « type », comme « Équipements » connecté à tous les sommets représentant un filtre d'équipement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*K4SFmofsfg-V2yu6zbwwXw.png)
_Filtres Airbnb avec types_

Maintenant, que se passe-t-il si nous représentons les maisons Airbnb comme des sommets et que nous connectons ensuite chaque maison avec un sommet « filtre » si cette maison supporte le filtre correspondant (Par exemple, connecter « maison 1 » avec « cuisine » si « maison 1 » a « cuisine » dans ses équipements) ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*SozJ2RceNg1CA-hua1324w.png)
_Cela semble désordonné_

Un léger changement de cette illustration la fait ressembler davantage à un type spécial de graphe, appelé **graphe biparti**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*rJDMNi0VK44XoIWIEqem-A.png)
_Le nombre de sommets est plus élevé qu'il n'y paraît_

_Graphe biparti ou simplement bigraphe est un graphe dont les sommets peuvent être divisés en deux ensembles disjoints et indépendants de telle sorte que chaque arête connecte un sommet dans un ensemble à un sommet dans l'autre ensemble. - [Wikipedia](https://en.wikipedia.org/wiki/Bipartite_graph)_.

Dans notre exemple, l'un des ensembles représente les filtres (nous le désignerons par F) et l'autre est un ensemble de maisons (désigné par H). Par exemple, s'il y a 100 mille maisons avec une valeur de prix de 62 $, alors le sommet de prix étiqueté « 62 $ » aura 100 mille arêtes incidentes à chaque sommet de maisons. Si nous mesurons le pire cas de complexité spatiale, c'est-à-dire que chaque maison a toutes les propriétés satisfaisant à tous les filtres, alors la quantité totale d'arêtes à stocker sera de 70 000 * 4 millions. Si nous représentons chaque arête comme une paire de deux identifiants : {filter_id; home_id} et si nous repensons aux identifiants et utilisons un identifiant numérique de 4 octets (int) pour les filtres et un identifiant de 8 octets (long) pour les maisons, alors chaque arête nécessiterait au moins 12 octets. Donc, stocker 70 000 * 4 millions de valeurs de 12 octets nécessiterait environ 3Tb de mémoire. Nous avons fait une petite erreur de calcul, vous voyez.

Le nombre de filtres est d'environ 70 000 en raison des 65 mille villes actives sur Airbnb ([stats](https://press.atairbnb.com/fast-facts/)). Et la bonne nouvelle est que la même maison ne peut pas être située dans plus d'une ville. C'est-à-dire que notre nombre réel d'arêtes appariées avec les villes est de 4 millions (chaque maison située dans une ville). Donc nous calculerons pour 70k - 65k = 5 mille filtres, ce qui signifie que nous avons besoin de 5000 * 4 millions * 12 octets de mémoire, ce qui est moins de 0,3 Tb. Cela semble bien. Mais que nous apporte ce graphe biparti ? Le plus souvent, une requête de site/mobile consistera en plusieurs filtres, par exemple comme ceci :

```
house_type: "entire_place",adults_number: 2,price_range_start: 56,price_range_end: 80,beds_number: 2,amenities: ["tv", "wifi", "laptop friendly workspace"],facilities: ["gym"]
```

Et tout ce dont nous avons besoin est de trouver tous les « sommets de filtre » ci-dessus et de traiter tous les « sommets de maison » qui sont adjacents à ces « sommets de filtre ». Cela nous amène à un sujet effrayant.

### Algorithmes de graphes : Introduction

Tout traitement effectué avec des graphes pourrait être catégorisé comme un « algorithme de graphe ». Vous pouvez littéralement implémenter une fonction imprimant tous les sommets d'un graphe et la nommer « algorithme d'impression de sommets de <votre nom ici> ». La plupart d'entre nous ont peur des algorithmes de graphes listés dans les manuels (voir la liste complète [ici](https://en.wikipedia.org/wiki/List_of_algorithms#Graph_algorithms)). Essayons d'appliquer un algorithme de correspondance de graphe biparti, tel que l'algorithme de Hopcroft-Karp, à notre problème de filtrage des maisons Airbnb :

> Étant donné un graphe biparti des maisons Airbnb (H) et des filtres (F), où chaque élément (sommet) de H peut avoir plus d'un élément adjacent (sommet) de F (partageant une arête commune). Trouver un sous-ensemble de H constitué de sommets qui sont adjacents à des sommets dans un sous-ensemble de F.

Définition de problème confuse, cependant, nous ne pouvons pas être sûrs à ce stade si l'algorithme de Hopcroft-Karp résout notre problème. Mais je vous assure que ce voyage nous enseignera de nombreuses idées cruciales derrière les algorithmes de graphes. Et le voyage n'est pas si court, alors soyez patient.

_L'algorithme de [**Hopcroft**](https://en.wikipedia.org/wiki/John_Hopcroft)**[Karp](https://en.wikipedia.org/wiki/Richard_M._Karp) est un algorithme qui prend en entrée un graphe biparti et produit en sortie une correspondance de cardinalité maximale - un ensemble d'arêtes aussi nombreuses que possible avec la propriété qu'aucune paire d'arêtes ne partage un point final - [Wikipedia](https://en.wikipedia.org/wiki/Hopcroft%E2%80%93Karp_algorithm)_.

Les lecteurs familiers avec cet algorithme sont déjà conscients que cela ne résout pas notre problème, car la correspondance nécessite qu'aucune paire d'arêtes ne partage un sommet commun.

Regardons une illustration d'exemple, où il n'y a que 4 filtres et 8 maisons (pour simplifier).

* Les maisons sont désignées par des lettres de A à H, les filtres sont choisis aléatoirement.
* La maison A a un prix (50 $), et 1 lit, (c'est tout ce que nous avons pour le prix).
* Toutes les maisons de A à H ont une étiquette de prix de 50 $ par nuit et 1 lit, mais quelques-unes d'entre elles ont le « Wi-Fi » et/ou la « TV ».

Donc, l'illustration suivante tente de montrer quelles maisons nous devons « retourner » pour la demande de maisons qui ont les quatre filtres disponibles (par exemple, elles coûtent 50 $ par nuit, elles ont 1 lit et elles ont également le Wi-Fi et la TV).

![Image](https://cdn-media-1.freecodecamp.org/images/1*r2G1A2OoG8KeTmqImr4SXQ.png)

La solution à notre problème nécessite des arêtes avec des sommets communs menant à des sommets de maison distincts qui sont incidents au même sous-ensemble de filtres, tandis que l'algorithme de Hopcroft-Karp élimine de telles arêtes avec des extrémités communes et produit des arêtes incidents à des sommets dans les deux sous-ensembles.

Regardez l'illustration ci-dessus, tout ce dont nous avons besoin sont les maisons D et G, qui satisfont toutes les deux aux quatre valeurs de filtre. Ce dont nous avons vraiment besoin est d'obtenir toutes les arêtes correspondantes qui partagent une extrémité commune.

Nous pourrions concevoir un algorithme pour cette approche, mais son temps de traitement n'est probablement pas pertinent pour les besoins des utilisateurs (besoins des utilisateurs = ultra-rapide, ici et maintenant). Probablement, il serait plus rapide de créer un arbre binaire de recherche équilibré avec plusieurs clés de tri, presque comme un fichier d'index de base de données, qui mappe les clés primaires/étrangères avec un ensemble d'enregistrements satisfaisants.

Les arbres binaires de recherche équilibrés et l'indexation des bases de données seront discutés dans un article séparé, où nous reviendrons au problème de filtrage des maisons Airbnb.

L'algorithme de Hopcroft-Karp (et beaucoup d'autres) sont basés à la fois sur les algorithmes de parcours de graphes **DFS** (Depth-First Search) et **BFS** (Breadth-First Search). Pour être honnête, la raison réelle d'introduire l'algorithme de Hopcroft-Karp ici est de passer subrepticement aux parcours de graphes, ce qui est mieux de commencer par les beaux graphes, les arbres binaires.

Les parcours d'arbres binaires sont vraiment beaux, surtout en raison de leur nature récursive. Il existe trois parcours de base appelés in-order, post-order et pre-order (vous pouvez inventer votre propre algorithme de parcours). Ils sont faciles à comprendre si vous avez déjà parcouru une liste chaînée. Dans les listes chaînées, vous imprimez simplement la valeur du nœud actuel (nommé `item` dans le code ci-dessous) et continuez vers le nœud suivant.

Presque la même chose s'applique aux arbres binaires, vous imprimez la valeur du nœud (ou tout ce que vous devez faire avec) et continuez ensuite vers le nœud suivant, mais dans ce cas, il y a « deux nœuds suivants », gauche et droite. Donc vous devez faire la même chose pour les nœuds gauche et droit. Mais vous avez trois choix différents ici :

* **Imprimer** la valeur du nœud puis aller au nœud **gauche**, puis aller au nœud **droit**, ou
* Aller au nœud **gauche**, **imprimer** la valeur du nœud, puis aller au nœud **droit**, ou
* Aller au nœud **gauche**, puis aller au nœud **droit**, puis **imprimer** la valeur du nœud.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_REEYbWyGAcxUOg91NpfDQ.png)
_Traçage détaillé du parcours pré-ordre_

![Image](https://cdn-media-1.freecodecamp.org/images/1*b8dFEEr0iKEs0ogkCR5mdQ.png)

Évidemment, les fonctions récursives ont l'air très élégantes bien qu'elles soient si coûteuses. Chaque fois que nous appelons une fonction de manière récursive, cela signifie que nous appelons une fonction complètement « nouvelle » (voir l'illustration ci-dessus). Et par « nouvelle », nous entendons qu'un autre espace mémoire de pile doit être « alloué » pour les arguments de la fonction et les variables locales. C'est pourquoi les appels récursifs sont coûteux (les allocations d'espace de pile supplémentaires et les nombreux appels de fonction) et dangereux (attention au débordement de pile) et il est évidemment suggéré d'utiliser des implémentations itératives. Dans la programmation de systèmes critiques (avions, rovers de la NASA, etc.), une récursion est complètement interdite (pas de statistiques, pas d'expérience, je vous raconte simplement les rumeurs).

### Netflix et Amazon : Exemple d'Index Inversé

Supposons que nous voulons stocker tous les films Netflix dans un arbre binaire de recherche avec les titres des films comme clés de tri. Donc, chaque fois qu'un utilisateur tape quelque chose comme « Inter », nous retournerons une liste de films commençant par « Inter » (par exemple, « Interstellar », « Interceptor », « Interrogation de Walter White »).

Maintenant, ce serait génial si nous retournions chaque film qui contient « Inter » dans son titre (pas seulement ceux qui commencent par « Inter »), et la liste serait triée par les notes des films ou quelque chose qui est pertinent pour cet utilisateur particulier (comme les thrillers plus que les drames). Le but de cet exemple est de faire des requêtes de plage efficaces à un BST.

Mais comme d'habitude, nous ne plongerons pas plus profondément dans l'eau froide pour repérer le reste de l'iceberg. En gros, nous avons besoin d'une recherche rapide par mots-clés et ensuite obtenir une liste de résultats triés par une certaine clé, qui devrait probablement être une note de film et/ou un classement interne basé sur les données personnalisées de l'utilisateur. Nous allons essayer de nous en tenir au principe KISK (Keep It Simple, Karl) autant que possible.

> « KISK » ou « gardons cela simple » ou « pour simplifier », une super excuse pour les rédacteurs de tutoriels pour s'abstraire du problème réel et faire des tonnes d'hypothèses en apportant un exemple « abc » facile et sa solution en pseudocode qui fonctionne même sur l'ordinateur portable de votre grand-mère.

Ce problème pourrait être facilement appliqué à la recherche de produits d'Amazon, car nous recherchons le plus souvent quelque chose sur Amazon en tapant un texte décrivant notre intérêt (comme « Graph Algorithms ») et obtenons des résultats triés par les notes des produits. Je n'ai pas expérimenté de résultats personnalisés dans les résultats de recherche d'Amazon. Mais je suis assez sûr qu'Amazon fait aussi ce genre de choses. Donc, il serait juste de changer le titre de ce sous-sujet en...

**Netflix et Amazon**. Netflix sert des films, Amazon sert des produits, nous les appellerons « articles », donc chaque fois que vous lisez un « article », pensez à un film sur Netflix ou à un produit [viable] sur Amazon.

Ce qui est le plus couramment fait avec les articles est l'analyse de leur titre et de leur description (_nous nous en tiendrons au titre uniquement_), donc si un opérateur (généralement un _être humain insérant les données de l'article dans la base de données Netflix/Amazon via un tableau de bord d'administration_) insère un nouvel article dans la base de données, son titre est traité par un certain « ItemTitleProcessor » pour produire des mots-clés.

![Image](https://cdn-media-1.freecodecamp.org/images/1*sHk85QLf7UBbV3fv0tEpqw.png)
_Pas la meilleure illustration, je sais (et elle contient une faute de frappe)_

Chaque article a son identifiant unique, qui est lié au mot-clé trouvé dans son titre. C'est ce que font les moteurs de recherche en parcourant les sites web du monde entier. Ils analysent le contenu de chaque document, le tokenisent (le divisent en entités plus petites appelées mots) et l'ajoutent à une table, qui mappe chaque token (mot) à l'identifiant du document (site web) où le token a été « vu ».

Ainsi, chaque fois que vous recherchez « hello », le moteur de recherche récupère tous les documents mappés au mot-clé « hello » (la réalité est beaucoup plus complexe, car la chose la plus importante est la pertinence de la recherche, c'est pourquoi Google Search est si génial). Donc une table similaire pour Netflix/Amazon pourrait ressembler à ceci (encore une fois, pensez aux Films ou Produits lorsque vous lisez Articles).

![Image](https://cdn-media-1.freecodecamp.org/images/1*fpEI4aYnsQh8weU2sdcOAg.png)
_Index inversé_

Les tables de hachage, encore une fois. Oui, nous allons conserver une table de hachage pour cet **index inversé** (_structure d'index stockant un mappage de contenu - [Wikipedia](https://en.wikipedia.org/wiki/Inverted_index)_). La table de hachage mappera un mot-clé à un BST d'articles. Pourquoi BST ? Parce que nous voulons les garder triés et en même temps les servir (répondre aux requêtes frontend) en portions triées séquentielles, (par exemple, 100 articles par requête en utilisant la pagination). Pas vraiment quelque chose qui montre la puissance des BST. Mais supposons que nous avons également besoin d'une recherche rapide dans le résultat de la recherche, disons que vous voulez tous les films à 3 étoiles avec le mot-clé « machine ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*dInMLLVJp8dFKYJ4iUhGcQ.png)

_Notez qu'il est acceptable d'avoir des articles en double dans différents arbres, car un article peut généralement être trouvé avec plus d'un mot-clé_.

Nous allons manipuler des articles définis comme suit :

Chaque fois qu'un nouvel article est inséré dans une base de données, le titre est traité et ajouté à la grande table d'index, qui mappe un mot-clé à un article. Il peut y avoir de nombreux articles partageant le même mot-clé, donc nous gardons ces articles dans un BST trié par leur note.

Lorsque les utilisateurs recherchent un mot-clé, ils obtiennent une liste d'articles triés par leur note. Comment pouvons-nous obtenir une liste à partir d'un arbre dans un ordre trié ? En effectuant un parcours in-order.

Voici à quoi pourrait ressembler une implémentation de `InOrderProduceVector()` :

Mais, mais... Nous avons besoin des articles les mieux notés en premier, et notre parcours in-order produit les articles les moins bien notés en premier. C'est à cause de sa nature. Le parcours in-order fonctionne « de bas en haut », des articles les moins bien notés aux mieux notés. Pour obtenir ce que nous voulions, c'est-à-dire la liste dans l'ordre décroissant au lieu de croissant, nous devons examiner de plus près l'implémentation du parcours in-order.

Ce que nous faisons est de passer par le nœud gauche, puis d'imprimer la valeur du nœud actuel et ensuite de passer par le nœud droit. Le nœud le plus à gauche est le nœud avec la plus petite valeur. Donc, changer simplement l'implémentation pour passer par le nœud droit en premier nous mènera à un ordre décroissant de la liste. Nous l'appellerons comme les autres le font, un parcours in-order inverse.

Mettons à jour le code ci-dessus (en l'introduisant dans une seule liste). Attention - Bugs en vue !

C'est tout. Nous pouvons servir les résultats de recherche d'articles assez rapidement. Comme mentionné ci-dessus, l'indexation inversée est principalement utilisée dans les moteurs de recherche, comme Google. Bien que Google Search soit un moteur de recherche **très** complexe, il utilise certaines idées simples (bien que trop modernisées) pour faire correspondre les requêtes de recherche aux documents et servir les résultats aussi rapidement que possible.

Nous avons utilisé des parcours d'arbres pour servir les résultats dans l'ordre trié. À ce stade, il peut sembler que les parcours pré/in/post-ordre sont plus que suffisants, mais parfois il y a besoin d'un autre type de parcours.

Abordons cette question d'entretien de programmation bien connue, « Comment imprimeriez-vous un [binaire] arbre niveau par niveau ? ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*N8LEoIDShv0s5jeSdLwccw.png)

### Parcours : DFS et BFS

Si vous n'êtes pas familier avec ce problème, pensez à une structure de données que vous pourriez utiliser pour stocker les nœuds lors du parcours de l'arbre. Si nous comparons le parcours niveau par niveau d'un arbre avec les autres ci-dessus (parcours pré, in, post ordre), nous concevrons finalement deux parcours principaux des graphes, à savoir une recherche en profondeur (DFS) et une recherche en largeur (BFS).

![Image](https://cdn-media-1.freecodecamp.org/images/1*BINJY5Q9c9x0OPchErAqTg.png)

La recherche en profondeur chasse le nœud le plus éloigné, la recherche en largeur explore les nœuds les plus proches en premier.

* **Recherche en profondeur** - plus d'actions, moins de réflexions.
* **Recherche en largeur** - prenez un bon coup d'œil autour de vous avant d'aller plus loin.

![Image](https://cdn-media-1.freecodecamp.org/images/1*wEftMOewfDW2ZLjsenZNUg.png)

Le DFS est très similaire aux parcours pré, in, post-ordre. Alors que le BFS est ce dont nous avons besoin si nous voulons imprimer les nœuds d'un arbre niveau par niveau.

Pour y parvenir, nous aurions besoin d'une file d'attente (structure de données) pour stocker le « niveau » du graphe tout en imprimant (visitant) son « niveau parent ». Dans l'illustration précédente, les nœuds placés dans la file d'attente sont en bleu clair.

En gros, en allant niveau par niveau, les nœuds de chaque niveau sont récupérés de la file d'attente, et tout en visitant chaque nœud récupéré, nous devons également insérer ses enfants dans la file d'attente (pour le niveau suivant). Le code suivant est suffisamment simple pour comprendre l'idée principale du BFS. Il est supposé que le graphe est connecté, bien qu'il puisse être modifié pour s'appliquer aux graphes non connectés.

L'idée de base est facile à montrer sur une représentation de graphe connecté basée sur les nœuds. Gardez simplement à l'esprit que l'implémentation du parcours de graphe diffère d'une représentation à l'autre.

Le BFS et le DFS sont des outils importants pour résoudre les problèmes de recherche de graphes (_mais rappelez-vous qu'il existe des tonnes d'algorithmes de recherche de graphes_). Bien que le DFS ait une implémentation récursive élégante, il est raisonnable de l'implémenter de manière itérative. Pour l'implémentation itérative du BFS, nous avons utilisé une file d'attente, pour le DFS, vous aurez besoin d'une pile. L'un des problèmes les plus populaires dans les graphes et en même temps l'une des raisons les plus probables pour lesquelles vous lisez cet article est le problème de trouver le plus court chemin entre les sommets d'un graphe. Et cela nous amène à notre dernière expérience de pensée.

### Uber et le problème du plus court chemin (algorithme de Dijkstra)

Avec ses 50 millions d'utilisateurs et 7 millions de conducteurs ([source](https://expandedramblings.com/index.php/uber-statistics/)), l'une des choses les plus importantes qui est critique pour le fonctionnement d'Uber est la capacité de faire correspondre les conducteurs avec les passagers de manière efficace. Le problème commence avec les emplacements.

Le backend doit traiter des millions de requêtes utilisateurs, envoyant chacune des requêtes à un ou plusieurs (généralement plusieurs) conducteurs à proximité. Bien qu'il soit plus facile et parfois même plus intelligent d'envoyer la requête utilisateur à tous les conducteurs à proximité, un certain prétraitement pourrait en fait aider.

![Image](https://cdn-media-1.freecodecamp.org/images/1*QPrbZuwR78qZgiZySoWv4Q.png)

En plus de traiter les requêtes entrantes et de trouver la zone de localisation basée sur les coordonnées de l'utilisateur, puis de trouver les conducteurs avec les coordonnées les plus proches, nous devons également trouver le bon conducteur pour le trajet. Pour éviter le traitement des requêtes géospatiales (récupération des voitures à proximité en comparant leurs coordonnées actuelles avec celles de l'utilisateur), disons que nous avons déjà un segment de la carte avec l'utilisateur et plusieurs voitures à proximité.

Quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*6KgEsmbSs6faQPLRLrQ2DA.png)

Les chemins possibles d'une voiture à un utilisateur sont en jaune. Le problème est de calculer la distance minimale requise pour que la voiture atteigne l'utilisateur, en d'autres termes, trouver le chemin le plus court entre eux. Bien que cela relève davantage de Google Maps que d'Uber, nous allons essayer de le résoudre pour ce cas particulier et très simplifié, principalement parce qu'il y a généralement plus d'une voiture de conducteur et qu'Uber pourrait vouloir calculer la voiture la plus proche avec la note la plus élevée pour l'envoyer à l'utilisateur.

Pour cette illustration, cela signifie calculer pour les trois voitures le chemin le plus court pour atteindre l'utilisateur et décider quelle voiture serait la plus optimale à envoyer. Pour simplifier les choses, nous allons discuter du cas avec une seule voiture. Voici quelques itinéraires possibles pour atteindre l'utilisateur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Yv50uskTygpYGN4NbF8CKw.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*fxRxGd8zX4WphcaW9WlKdg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*nyl2FDD3AoBUYD4bP9tijQ.png)
_Variantes possibles pour atteindre l'utilisateur_

Pour aller droit au but, nous allons représenter ce segment comme un graphe :

![Image](https://cdn-media-1.freecodecamp.org/images/1*h8EghvyR-H2rFDClEwF3pA.png)

Il s'agit d'un graphe non orienté pondéré (pondéré par les arêtes, pour être plus précis). Pour trouver le chemin le plus court entre les sommets B (la voiture) et A (l'utilisateur), nous devons trouver un itinéraire entre eux composé d'arêtes avec des poids éventuellement minimaux. Vous êtes libre de concevoir votre propre version de la solution. Nous allons nous en tenir à la [version de Dijkstra](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm). Les étapes suivantes de l'algorithme de Dijkstra sont tirées de [Wikipedia](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm).

_Que le nœud à partir duquel nous commençons soit appelé le **nœud initial**. Que la **distance du nœud Y** soit la distance du **nœud initial** à Y. L'algorithme de Dijkstra attribuera certaines valeurs de distance initiales et essaiera de les améliorer étape par étape._

1. _Marquer tous les nœuds non visités. Créer un ensemble de tous les nœuds non visités appelé l'ensemble non visité._
2. _Attribuer à chaque nœud une valeur de distance provisoire : la mettre à zéro pour notre nœud initial et à l'infini pour tous les autres nœuds. Définir le nœud initial comme courant._
3. _Pour le nœud courant, considérer tous ses voisins non visités et calculer leurs distances provisoires à travers le nœud courant. Comparer la distance provisoire nouvellement calculée à la valeur actuellement attribuée et attribuer la plus petite. Par exemple, si le nœud courant A est marqué avec une distance de 6, et que l'arête le reliant à un voisin B a une longueur de 2, alors la distance à B à travers A sera de 6 + 2 = 8. Si B était précédemment marqué avec une distance supérieure à 8, alors la changer en 8. Sinon, garder la valeur actuelle._
4. _Lorsque nous avons terminé de considérer tous les voisins du nœud courant, marquer le nœud courant comme visité et le retirer de l'ensemble non visité. Un nœud visité ne sera plus jamais vérifié._
5. _Si le nœud de destination a été marqué comme visité (lors de la planification d'un itinéraire entre deux nœuds spécifiques) ou si la plus petite distance provisoire parmi les nœuds de l'ensemble non visité est l'infini (lors de la planification d'un parcours complet ; se produit lorsqu'il n'y a pas de connexion entre le nœud initial et les nœuds non visités restants), alors arrêter. L'algorithme a terminé._
6. _Sinon, sélectionner le nœud non visité qui est marqué avec la plus petite distance provisoire, le définir comme le nouveau « nœud courant », et revenir à l'étape 3._

En appliquant cela à notre exemple, nous commencerons avec le sommet B (la voiture) comme nœud initial. Pour les deux premières étapes :

![Image](https://cdn-media-1.freecodecamp.org/images/1*TJlybxA2sd73xKk_G3zFdg.png)

Notre ensemble non visité se compose de tous les sommets. Remarquez également le tableau du côté gauche de l'illustration. Pour tous les sommets, il contiendra toutes les distances les plus courtes depuis B et le sommet précédent (marqué « Prev ») qui mène au sommet. Par exemple, la distance est de 20 de B à F, et le sommet précédent est B.

![Image](https://cdn-media-1.freecodecamp.org/images/1*nnTYJcutyrQ3owuWfcFsKQ.png)

Nous marquons B comme visité et nous déplaçons vers son voisin F.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-q06mg5A5Yirmu2qHZgL0Q.png)

Maintenant, nous marquons F comme visité et choisissons le prochain nœud non visité avec la plus petite distance provisoire, qui est G. Remarquez également le tableau du côté gauche. Dans l'illustration précédente, les nœuds C, F et G ont déjà leurs distances provisoires définies avec les nœuds précédents qui mènent aux nœuds mentionnés.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8y39ufJ1FEYqjpBJQ9ApcA.png)

Comme indiqué dans l'algorithme, si le nœud de destination a été marqué comme visité (lors de la planification d'un itinéraire entre deux nœuds spécifiques comme dans notre cas), alors nous pouvons nous arrêter. Donc notre prochaine étape arrête l'algorithme avec les valeurs suivantes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*mxxxszr1m82FEtkgcHGHgg.png)

Ainsi, nous avons à la fois la distance la plus courte de B à A et l'itinéraire passant par les nœuds F et G.

C'est vraiment l'exemple le plus simple possible des problèmes potentiels chez Uber, en comparant cela à notre analogie de l'iceberg, nous sommes à la **pointe de la pointe** de l'iceberg. Cependant, c'est un bon premier départ pour explorer le monde réel de la théorie des graphes et ses applications. Je n'ai pas terminé ce que j'avais initialement prévu pour cet article, mais dans un avenir proche, cela sera probablement poursuivi (y compris les internes de l'indexation des bases de données).

Il y a encore tant à dire sur les graphes (il reste encore à étudier). Prenez cet article comme une autre pointe de l'iceberg. Si vous avez lu jusqu'ici, vous méritez définitivement un cookie. N'oubliez pas de cliquer et de partager. Merci.

#### Ressources

[1] [Sh. Even, G. Even, Graph Algorithms](https://www.amazon.com/Graph-Algorithms-Shimon-Even-ebook/dp/B00INYG6O4/)

#### Lectures complémentaires

[R. Sedgewick, K. Wayne, Algorithms](https://www.amazon.com/Algorithms-4th-Robert-Sedgewick/dp/032157351X/)

[T. Cormen, Ch. Leiserson, R. Rivest, C. Stein, Introduction to Algorithms](https://www.amazon.com/Introduction-Algorithms-3rd-MIT-Press/dp/0262033844/)

Airbnb Engineering, [AirbnbEng](https://www.freecodecamp.org/news/i-dont-understand-graph-theory-1c96572a1401/undefined)

Netflix Tech Blog, [Netflix Technology Blog](https://www.freecodecamp.org/news/i-dont-understand-graph-theory-1c96572a1401/undefined)

[Twitter Engineering Blog](https://blog.twitter.com/engineering/en_us.html)

[Uber Engineering Blog](https://eng.uber.com/)