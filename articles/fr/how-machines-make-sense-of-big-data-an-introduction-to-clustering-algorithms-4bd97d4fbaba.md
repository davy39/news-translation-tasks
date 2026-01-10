---
title: Une introduction aux algorithmes de clustering
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-28T16:44:07.000Z'
originalURL: https://freecodecamp.org/news/how-machines-make-sense-of-big-data-an-introduction-to-clustering-algorithms-4bd97d4fbaba
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Bm4uiBY1JEt6Z-vOme_fTQ.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: clustering
  slug: clustering
- name: combinatorics
  slug: combinatorics
- name: data
  slug: data
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: Math
  slug: math
- name: Mathematics
  slug: mathematics
- name: Python
  slug: python
- name: statistics
  slug: statistics
- name: technology
  slug: technology
seo_title: Une introduction aux algorithmes de clustering
seo_desc: 'By Peter Gleeson

  Take a look at the image below. It’s a collection of bugs and creepy-crawlies of
  different shapes and sizes. Take a moment to categorize them by similarity into
  a number of groups.

  This isn’t a trick question. Start with grouping the...'
---

Par Peter Gleeson

Jetez un coup d'œil à l'image ci-dessous. Il s'agit d'une collection d'insectes et de bestioles de différentes formes et tailles. Prenez un moment pour les catégoriser par similarité en un certain nombre de groupes.

Ce n'est pas une question piège. Commencez par regrouper les araignées ensemble.

![Image](https://cdn-media-1.freecodecamp.org/images/BfSVT54goDauX2gz7TL7lE2qPKEnhVnTI6Ir)
_Images via Google Image Search, labellisées pour réutilisation_

Terminé ? Bien qu'il n'y ait pas nécessairement de réponse "correcte" ici, il est probable que vous ayez divisé les insectes en quatre _clusters_. Les araignées dans un cluster, les deux escargots dans un autre, les papillons et la mite dans un troisième, et le trio de guêpes et d'abeilles dans un quatrième.

Ce n'était pas trop difficile, n'est-ce pas ? Vous pourriez probablement faire de même avec deux fois plus d'insectes, non ? Si vous aviez un peu de temps à perdre — ou une passion pour l'entomologie — vous pourriez probablement même faire de même avec cent insectes.

Pour une machine, cependant, regrouper dix objets en un nombre quelconque de clusters significatifs n'est pas une tâche facile, grâce à une branche des mathématiques qui défie l'esprit appelée [combinatoire](https://en.wikipedia.org/wiki/Bell_number), qui nous dit qu'il existe 115 975 façons différentes de regrouper ces dix insectes ensemble.

S'il y avait eu vingt insectes, il y aurait eu [plus de cinquante billions](https://www.wolframalpha.com/input/?i=bell%27s+number+(20)) de façons possibles de les regrouper.

Avec cent insectes — il y aurait beaucoup plus de solutions que de [particules dans l'univers connu](https://www.wolframalpha.com/input/?i=particles+in+universe). 

Combien de fois plus ? Selon mes calculs, environ [cinq cents millions de milliards de milliards de fois plus](https://www.wolframalpha.com/input/?i=BellB%5B100%5D+%2F+number+of+particles+in+universe). En fait, il y a plus de [quatre millions de milliards de _googol_](https://www.wolframalpha.com/input/?i=BellB%5B100%5D+%2F+googol) de solutions ([qu'est-ce qu'un googol ?](https://www.wolframalpha.com/input/?i=googol)).

Pour seulement cent objets.

Presque toutes ces solutions seraient dénuées de sens — pourtant, parmi ce nombre inimaginable de choix possibles, vous avez assez rapidement trouvé l'une des très rares qui regroupent les insectes de manière utile.

Nous, les humains, tenons pour acquis notre capacité à catégoriser et à donner un sens à de grands volumes de données assez rapidement. Qu'il s'agisse d'un paragraphe de texte, d'images à l'écran ou d'une séquence d'objets — les humains sont généralement assez efficaces pour donner un sens aux données que le monde nous présente.

Étant donné qu'un aspect clé du développement de l'I.A. et de l'apprentissage automatique est de faire en sorte que les machines donnent rapidement un sens à de grands ensembles de données d'entrée, quels raccourcis sont disponibles ? 

Ici, vous pouvez lire à propos de trois algorithmes de clustering que les machines peuvent utiliser pour donner rapidement un sens à de grands ensembles de données. Ce n'est en aucun cas une liste exhaustive — il existe d'autres algorithmes — mais ils représentent un bon point de départ !

Vous trouverez pour chacun un résumé rapide de leur utilisation, un aperçu bref de leur fonctionnement, et un exemple détaillé étape par étape. Je crois qu'il est utile de comprendre un algorithme en l'exécutant soi-même. 

Si vous êtes _vraiment motivé_, vous trouverez que la meilleure façon de faire cela est avec un stylo et du papier. Allez-y — personne ne vous jugera !

![Image](https://cdn-media-1.freecodecamp.org/images/PkvVKjhDBUGlU2gTPj7r0T1aNPdpOZ6MpZ6B)
_Trois clusters étrangement nets, avec K = 3_

### Clustering K-means

#### **À utiliser lorsque...**

...vous avez une idée du nombre de groupes que vous vous attendez à trouver _a priori_.

#### **Comment cela fonctionne**

L'algorithme attribue aléatoirement chaque observation à l'une des _k_ catégories, puis calcule la _moyenne_ de chaque catégorie. Ensuite, il réattribue chaque observation à la catégorie avec la moyenne la plus proche avant de recalculer les moyennes. Cette étape se répète encore et encore jusqu'à ce qu'aucune réattribution ne soit plus nécessaire.

#### **Exemple détaillé**

Prenez un groupe de 12 joueurs de football (ou de "soccer") qui ont chacun marqué un certain nombre de buts cette saison (disons dans la plage 3–30). Divisons-les en clusters séparés — disons trois.

**Étape 1** nous demande de diviser aléatoirement les joueurs en trois groupes et de calculer les moyennes de chaque groupe.

```
Groupe 1
  Joueur A (5 buts),
  Joueur B (20 buts),
  Joueur C (11 buts)
Moyenne du groupe = (5 + 20 + 11) / 3 = 12 buts

Groupe 2
  Joueur D (5 buts),
  Joueur E (3 buts),
  Joueur F (19 buts)
Moyenne du groupe = 9 buts

Groupe 3
  Joueur G (30 buts),
  Joueur H (3 buts),
  Joueur I (15 buts)
Moyenne du groupe = 16 buts
```

**Étape 2** : Pour chaque joueur, réattribuez-le au groupe avec la moyenne la plus proche. Par exemple, le Joueur A (5 buts) est attribué au Groupe 2 (moyenne = 9). Ensuite, recalculez les moyennes des groupes.

```
Groupe 1 (Ancienne moyenne = 12 buts)
  Joueur C (11 buts)
Nouvelle moyenne = 11 buts

Groupe 2 (Ancienne moyenne = 9 buts)
  Joueur A (5 buts),
  Joueur D (5 buts),
  Joueur E (3 buts),
  Joueur H (3 buts)
Nouvelle moyenne = 4 buts

Groupe 3 (Ancienne moyenne = 16 buts)
  Joueur G (30 buts),
  Joueur I (15 buts),
  Joueur B (20 buts),
  Joueur F (19 buts)
Nouvelle moyenne = 21 buts
```

**Répétez** l'Étape 2 encore et encore jusqu'à ce que les moyennes des groupes ne changent plus. Pour cet exemple quelque peu artificiel, cela se produit à l'itération suivante. **Arrêtez !** Vous avez maintenant formé trois clusters à partir de l'ensemble de données !

```
Groupe 1 (Ancienne moyenne = 11 buts)
  Joueur C (11 buts),
  Joueur I (15 buts)
Moyenne finale = 13 buts

Groupe 2 (Ancienne moyenne = 4 buts)
  Joueur A (5 buts),
  Joueur D (5 buts),
  Joueur E (3 buts),
  Joueur H (3 buts)
Moyenne finale = 4 buts

Groupe 3 (Ancienne moyenne = 21 buts)
  Joueur G (30 buts),
  Joueur B (20 buts),
  Joueur F (19 buts)
Moyenne finale = 23 buts
```

Avec cet exemple, les clusters pourraient correspondre aux positions des joueurs sur le terrain — comme les défenseurs, les milieux de terrain et les attaquants. 

K-means fonctionne ici parce que nous aurions pu raisonnablement nous attendre à ce que les données se répartissent naturellement dans ces trois catégories.

De cette manière, étant donné des données sur une gamme de statistiques de performance, une machine pourrait faire un travail raisonnable d'estimation des positions des joueurs de n'importe quel sport d'équipe — utile pour l'analyse sportive, et en effet pour tout autre but où la classification d'un ensemble de données en groupes prédéfinis peut fournir des informations pertinentes.

#### **Détails supplémentaires**

Il existe plusieurs variations de l'algorithme décrit ici. La méthode initiale de "semis" des clusters peut être faite de plusieurs manières. 

Ici, nous avons attribué aléatoirement chaque joueur à un groupe, puis calculé les moyennes des groupes. Cela fait que les moyennes initiales des groupes tendent à être similaires les unes aux autres, ce qui assure une plus grande répétabilité.

Une alternative est de semer les clusters avec un seul joueur chacun, puis de commencer à attribuer les joueurs au cluster le plus proche. Les clusters retournés sont plus sensibles à l'étape initiale de semis, réduisant la répétabilité dans les ensembles de données très variables. 

Cependant, cette approche peut réduire le nombre d'itérations nécessaires pour compléter l'algorithme, car les groupes mettront moins de temps à diverger.

Une limitation évidente du clustering K-means est que vous devez fournir des hypothèses _a priori_ sur le nombre de clusters que vous vous attendez à trouver. 

Il existe des méthodes pour évaluer l'ajustement d'un ensemble particulier de clusters. Par exemple, le Within-Cluster [Sum-of-Squares](https://en.wikipedia.org/wiki/Partition_of_sums_of_squares) est une mesure de la variance au sein de chaque cluster.

Les clusters sont "meilleurs" lorsque le WCSS global est plus bas.

### Clustering hiérarchique

#### **À utiliser lorsque...**

...vous souhaitez découvrir les relations sous-jacentes entre vos observations.

#### **Comment cela fonctionne**

Une matrice de distance est calculée, où la valeur de la cellule (_i, j_) est une métrique de distance entre les observations _i_ et _j_. 

Ensuite, appariez les deux observations les plus proches et calculez leur moyenne. Formez une nouvelle matrice de distance, en fusionnant les observations appariées en un seul objet. 

À partir de cette matrice de distance, appariez les deux observations les plus proches et calculez leur moyenne. Répétez jusqu'à ce que toutes les observations soient regroupées ensemble.

#### **Exemple détaillé**

Voici un ensemble de données super-simplifié sur une sélection d'espèces de baleines et de dauphins. En tant que biologiste formé, je peux vous assurer que nous utilisons normalement des ensembles de données beaucoup plus détaillés pour des choses comme [reconstruire la phylogénie](https://en.wikipedia.org/wiki/Phylogenetic_tree). 

Pour l'instant, nous allons simplement regarder les longueurs corporelles typiques de ces six espèces. Nous n'utiliserons que deux étapes répétées.

```
Espèce          Initiales  Longueur(m)
Dauphin à nez de bouteille     BD        3.0
Dauphin de Risso        RD        3.6
Baleine pilote            PW        6.5
Orque           KW        7.5
Baleine à bosse         HW       15.0
Baleine commune              FW       20.0
```

**Étape 1** : calculez une matrice de distance entre chaque espèce. Ici, nous utiliserons la [distance euclidienne](https://en.wikipedia.org/wiki/Euclidean_distance) — à quelle distance se trouvent les points de données ? 

Lisez ceci exactement comme vous le feriez pour un tableau de distance dans un atlas routier. La différence de longueur entre toute paire d'espèces peut être trouvée en lisant la valeur à l'intersection de la ligne et de la colonne pertinentes.

```
    BD   RD   PW   KW   HW
RD  0.6                    
PW  3.5  2.9               
KW  4.5  3.9  1.0          
HW 12.0 11.4  8.5  7.5     
FW 17.0 16.4 13.5 12.5  5.0
```

**Étape 2** : Appairez les deux espèces les plus proches. Ici, ce seront le Dauphin à nez de bouteille et le Dauphin de Risso, avec une longueur moyenne de 3,3 m.

**Répétez** l'Étape 1 en recalculant la matrice de distance, mais cette fois fusionnez le Dauphin à nez de bouteille et le Dauphin de Risso en un seul objet de longueur 3,3 m.

```
    [BD, RD]   PW   KW   HW
PW       3.2               
KW       4.2   1.0          
HW      11.7   8.5  7.5     
FW      16.7  13.5 12.5  5.0
```

**Ensuite**, répétez l'Étape 2 avec cette nouvelle matrice de distance. Ici, la plus petite distance est entre la Baleine pilote et l'Orque, donc nous les apparions et prenons leur moyenne — ce qui nous donne 7,0 m.

**Ensuite**, nous répétons l'Étape 1 — recalculons la matrice de distance, mais maintenant nous avons fusionné la Baleine pilote et l'Orque en un seul objet de longueur 7,0 m.

```
         [BD, RD] [PW, KW]   HW
 [PW, KW]      3.7              
 HW           11.7      8.0     
 FW           16.7     13.0   5.0
```

**Ensuite**, répétez l'Étape 2 avec cette matrice de distance. La plus petite distance (3,7 m) est entre les deux objets fusionnés — donc maintenant fusionnez-les en un objet encore plus grand, et prenez la moyenne (qui est de 5,2 m).

**Ensuite**, répétez l'Étape 1 et calculez une nouvelle matrice de distance, ayant fusionné le Dauphin à nez de bouteille et le Dauphin de Risso avec la Baleine pilote et l'Orque.

```
   [[BD, RD] , [PW, KW]]    HW
HW                   9.8    
FW                  14.8   5.0
```

**Ensuite**, répétez l'Étape 2. La plus petite distance (5,0 m) est entre la Baleine à bosse et la Baleine commune, donc fusionnez-les en un seul objet, et prenez la moyenne (17,5 m).

**Ensuite**, retournez à l'Étape 1 — calculez la matrice de distance, ayant fusionné la Baleine à bosse et la Baleine commune.

```
         [[BD, RD] , [PW, KW]]
[HW, FW]                  12.3
```

**Enfin**, répétez l'Étape 2 — il n'y a qu'une seule distance (12,3 m) dans cette matrice, donc appariez tout en un grand objet. Maintenant vous pouvez **vous arrêter !** Regardez l'objet fusionné final :

```
[[[BD, RD],[PW, KW]],[HW, FW]]
```

Il a une structure imbriquée (pensez [JSON](http://json.org/example.html)), qui permet de le représenter sous forme de graphique en arbre, ou 'dendrogramme'.

Il se lit de la même manière qu'un arbre généalogique. Plus deux observations sont proches sur l'arbre, plus elles sont considérées comme similaires ou étroitement liées.

![Image](https://cdn-media-1.freecodecamp.org/images/mPiihHFW6hWNtBOST4BqWS-JpX9pSUJRb78x)
_Un dendrogramme sans fioritures généré sur [R-Fiddle.org](http://www.r-fiddle.org/#" rel="noopener" target="_blank" title=")_

La structure du dendrogramme donne un aperçu de la manière dont l'ensemble de données est structuré.

Dans cet exemple, il y a deux branches principales, avec la Baleine à bosse et la Baleine commune d'un côté, et le Dauphin à nez de bouteille/Dauphin de Risso et la Baleine pilote/Orque de l'autre.

En biologie évolutive, des ensembles de données beaucoup plus grands avec de nombreux spécimens et mesures sont utilisés de cette manière pour déduire les relations taxonomiques entre eux. 

En dehors de la biologie, le clustering hiérarchique a des applications dans les contextes de data mining et d'apprentissage automatique.

Le point intéressant est que cette approche ne nécessite aucune hypothèse sur le nombre de clusters que vous recherchez. 

Vous pouvez diviser le dendrogramme retourné en clusters en "coupant" l'arbre à une hauteur donnée. Cette hauteur peut être choisie de plusieurs manières, en fonction de la résolution à laquelle vous souhaitez regrouper les données.

Par exemple, en regardant le dendrogramme ci-dessus, si nous traçons une ligne horizontale à hauteur = 10, nous intersecterions les deux branches principales, divisant le dendrogramme en deux sous-graphes. Si nous coupions à hauteur = 2, nous diviserions le dendrogramme en trois clusters.

#### **Détails supplémentaires**

Il existe essentiellement trois aspects dans lesquels les algorithmes de clustering hiérarchique peuvent varier par rapport à celui donné ici.

Le plus fondamental est l'approche — ici, nous avons utilisé un processus _agglomératif_, où nous commençons avec des points de données individuels et les regroupons itérativement jusqu'à ce qu'il ne reste qu'un grand cluster. 

Une alternative (mais plus intensive en calcul) est de commencer avec un cluster géant, puis de procéder à la division des données en clusters de plus en plus petits jusqu'à ce qu'il ne reste que des points de données isolés.

Il existe également une gamme de méthodes qui peuvent être utilisées pour calculer les matrices de distance. Pour de nombreux usages, la distance euclidienne (théorème de Pythagore) suffira, mais il existe des [alternatives](https://en.wikipedia.org/wiki/Metric_(mathematics)) qui peuvent être plus applicables dans certaines circonstances.

Enfin, le _critère de liaison_ peut également varier. Les clusters sont liés selon leur proximité, mais la manière dont nous définissons "proche" est flexible.

 Dans l'exemple ci-dessus, nous avons mesuré les distances entre les moyennes (ou "centroïdes") de chaque groupe et apparié les groupes les plus proches. Cependant, vous pouvez vouloir utiliser une définition différente.

Par exemple, chaque cluster est composé de plusieurs points discrets. Vous pourriez définir la distance entre deux clusters comme étant la distance minimale (ou maximale) entre l'un de leurs points — comme illustré dans la figure ci-dessous.

Il existe encore d'autres façons de définir le critère de liaison, qui peuvent être adaptées à différents contextes.

![Image](https://cdn-media-1.freecodecamp.org/images/cb0OUKorixLdjc-oVQ4srQvwLzzoBT7rdivq)
_Rouge/Bleu : liaison par centroïde ; Rouge/Vert : liaison minimale ; Vert/Bleu : liaison maximale_

### Détection de communautés dans les graphes

#### **À utiliser lorsque**

...vous avez des données qui peuvent être représentées sous forme de réseau, ou de "graphe".

#### **Comment cela fonctionne**

Une _communauté de graphe_ est très généralement définie comme un sous-ensemble de sommets qui sont plus connectés entre eux qu'avec le reste du réseau. 

Différents algorithmes existent pour identifier les communautés, basés sur des définitions plus spécifiques. Les algorithmes incluent, mais ne sont pas limités à : Edge Betweenness, Modularity-Maximsation, Walktrap, Clique Percolation, Leading Eigenvector...

#### **Exemple détaillé**

La [théorie des graphes](https://en.wikipedia.org/wiki/Graph_theory), ou l'étude mathématique des réseaux, est une branche fascinante des mathématiques qui nous permet de modéliser des systèmes complexes comme une collection abstraite de "points" (ou _sommets_) connectés par des "lignes" (ou _arêtes_).

Peut-être les cas d'étude les plus intuitifs sont les réseaux sociaux. 

Ici, les sommets représentent des personnes, et les arêtes connectent les sommets qui sont amis/suiveurs. Cependant, tout système peut être modélisé comme un réseau si vous pouvez justifier une méthode pour connecter de manière significative différents composants. 

Parmi les applications les plus innovantes de la théorie des graphes au clustering, on trouve l'extraction de caractéristiques à partir de données d'images et l'analyse des réseaux de régulation génique.

En tant qu'exemple de niveau débutant, jetez un coup d'œil à ce graphe rapidement assemblé. Il montre les huit sites web que j'ai visités le plus récemment, liés selon que leurs articles Wikipedia respectifs renvoient les uns aux autres.

Vous pourriez assembler ces données manuellement, mais pour des projets à plus grande échelle, il est beaucoup plus rapide d'écrire un script Python pour faire de même. [En voici un que j'ai écrit plus tôt](https://raw.githubusercontent.com/pg0408/Medium-articles/master/graph_maker.py).

![Image](https://cdn-media-1.freecodecamp.org/images/ir9Qji2KQ-YrkQSUOs4caYehAT9nDsDPu0jA)
_Graphe tracé avec le package 'igraph' pour R version 3.3.3_

Les sommets sont colorés selon leur appartenance à une communauté, et dimensionnés selon leur _centralité_. Voyez comment Google et Twitter sont les plus centraux ?

De plus, les clusters ont un sens assez bon dans le monde réel (toujours un indicateur de performance important). 

Les sommets jaunes sont généralement des sites de référence/recherche ; les sommets bleus sont tous utilisés pour la publication en ligne (d'articles, de tweets ou de code) ; et les sommets rouges incluent YouTube, qui a bien sûr été fondé par d'anciens employés de PayPal. Pas de mauvaises déductions pour une machine.

Outre le fait d'être une manière utile de visualiser de grands systèmes, la véritable puissance des réseaux vient de leur analyse mathématique. Commençons par traduire notre belle image du réseau en un format plus mathématique. Ci-dessous se trouve la _matrice d'adjacence_ du réseau.

```
         GH Gl  M  P  Q  T  W  Y
GitHub    0  1  0  0  0  1  0  0  
Google    1  0  1  1  1  1  1  1
Medium    0  1  0  0  0  1  0  0
PayPal    0  1  0  0  0  1  0  1
Quora     0  1  0  0  0  1  1  0
Twitter   1  1  1  1  1  0  0  1
Wikipedia 0  1  0  0  1  0  0  0
YouTube   0  1  0  1  0  1  0  0
```

La valeur à l'intersection de chaque ligne et colonne enregistre s'il y a une arête entre cette paire de sommets. 

Par exemple, il y a une arête entre Medium et Twitter (quelle surprise !), donc la valeur où leurs lignes/colonnes se croisent est 1. De même, il n'y a pas d'arête entre Medium et PayPal, donc l'intersection de leurs lignes/colonnes retourne 0.

Encodée dans la matrice d'adjacence se trouvent toutes les propriétés de ce réseau — elle nous donne la clé pour commencer à déverrouiller toutes sortes d'informations précieuses.

Pour commencer, la somme de n'importe quelle colonne (ou ligne) vous donne le _degré_ de chaque sommet — c'est-à-dire, combien d'autres il est connecté. Cela est communément noté avec la lettre _k_.

De même, la somme des degrés de chaque sommet et la division par deux vous donne _L_, le nombre d'arêtes (ou de "liens") dans le réseau. Le nombre de lignes/colonnes nous donne _N_, le nombre de sommets (ou de "nœuds") dans le réseau.

Connaissant simplement _k_, _L, N_ et la valeur de chaque cellule dans la matrice d'adjacence _A_ nous permet de calculer la [_modularité_](https://en.wikipedia.org/wiki/Modularity_(networks)) de n'importe quel clustering donné du réseau.

Supposons que nous avons regroupé le réseau en un certain nombre de communautés. Nous pouvons utiliser le score de modularité pour évaluer la "qualité" de ce clustering. 

Un score plus élevé montrera que nous avons divisé le réseau en communautés "précises", tandis qu'un score bas suggère que nos clusters sont plus aléatoires qu'informatifs. L'image ci-dessous illustre cela.

![Image](https://cdn-media-1.freecodecamp.org/images/O42yBf3CmmP83k2h5gCmJHer2ycdggjCkuzk)
_La modularité sert de mesure de la "qualité" d'une partition._

La modularité peut être calculée en utilisant la formule ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/hUA32fMe6NNc7rs8Kq-2UWGGDYxBUtduIo51)

C'est une quantité de mathématiques, mais nous pouvons la décomposer bit par bit et elle aura plus de sens.

_M_ est bien sûr ce que nous calculons — la modularité.

1/2_L_ nous dit de diviser tout ce qui suit par 2_L_, c'est-à-dire, deux fois le nombre d'arêtes dans le réseau. Jusqu'à présent, tout va bien.

Le symbole **Σ** nous dit que nous additionnons tout ce qui est à droite, et nous permet d'itérer sur chaque ligne et colonne dans la matrice d'adjacence _A_.

Pour ceux qui ne sont pas familiers avec la notation de somme, le _i, j = 1_ et le _N_ fonctionnent beaucoup comme des boucles for imbriquées en programmation. En Python, vous l'écririez comme suit :

```python
sum = 0
for i in range(1,N):
    for j in range(1,N):
        ans = #stuff with i and j as indices 
    sum += ans
```

Alors, qu'est-ce que `#stuff with i and j` en plus de détails ?

Eh bien, la partie entre parenthèses nous dit de soustraire ( _k_i k_j ) / 2L_ de _A_ij_.

_A_ij_ est simplement la valeur dans la matrice d'adjacence à la ligne _i_, colonne _j_.

Les valeurs de _k_i_ et _k_j_ sont les degrés de chaque sommet — trouvées en additionnant les entrées dans la ligne _i_ et la colonne _j_ respectivement. Multiplier celles-ci ensemble et diviser par 2_L_ nous donne le nombre attendu d'arêtes entre les sommets _i_ et _j_ si le réseau était mélangé aléatoirement.

Globalement, le terme entre parenthèses révèle la différence entre la structure réelle du réseau et la structure attendue qu'il aurait si elle était réassemblée aléatoirement.

En jouant avec les valeurs, on voit qu'elle retourne sa valeur la plus élevée lorsque _A_ij_ = 1, et ( _k_i k_j ) / 2L_ est faible. Cela signifie que nous voyons une valeur plus élevée s'il y a une arête "inattendue" entre les sommets _i_ et _j._

Enfin, nous multiplions le terme entre parenthèses par ce à quoi les derniers symboles font référence.

Le ?c__i,_ c__j i_s la fonction Kronecker-delta, qui semble sophistiquée mais est totalement inoffensive. La voici, expliquée en Python :

```python
def kroneckerDelta(ci, cj):
    if ci == cj:
        return 1
    else:
        return 0
        
kroneckerDelta("A","A")
#returns 1

kroneckerDelta("A","B")
#returns 0
```

Oui — c'est vraiment aussi simple. La fonction Kronecker-delta prend deux arguments et retourne 1 s'ils sont identiques, sinon zéro.

Cela signifie que si les sommets _i_ et _j_ ont été placés dans le même cluster, alors ?c__i,_ c__j = 1_. Sinon, s'ils sont dans des clusters différents, la fonction retourne zéro.

Comme nous multiplions le terme entre parenthèses par cette fonction Kronecker-delta, nous trouvons que pour la somme imbriquée **Σ**, le résultat est le plus élevé lorsqu'il y a beaucoup d'arêtes "inattendues" connectant les sommets attribués au même cluster. 

Ainsi, la modularité est une mesure de la qualité du clustering du graphe en communautés séparées.

Diviser par _2L_ borne la valeur supérieure de la modularité à 1. Les scores de modularité proches de ou inférieurs à zéro indiquent que le clustering actuel du réseau n'est vraiment d'aucune utilité. Plus la modularité est élevée, meilleur est le clustering du réseau en communautés séparées. 

En maximisant la modularité, nous pouvons trouver la meilleure façon de regrouper le réseau.

Remarquez que nous devons pré-définir comment le graphe est regroupé pour découvrir à quel point ce clustering est "bon". 

Malheureusement, employer la force brute pour essayer toutes les façons possibles de regrouper le graphe afin de trouver celle qui a le score de modularité le plus élevé serait computationnellement impossible au-delà d'une taille d'échantillon très limitée.

La [combinatoire](https://en.wikipedia.org/wiki/Partition_of_a_set#Counting_partitions) nous dit que pour un réseau de seulement huit sommets, il y a 4140 façons différentes de les regrouper. Un réseau deux fois plus grand aurait plus de dix milliards de façons possibles de regrouper les sommets. 

Doubler à nouveau le réseau (à un très modeste 32 sommets) donnerait 128 septillions de façons possibles, et un réseau de quatre-vingts sommets pourrait être regroupé de plus de façons qu'il n'y a d'[atomes dans l'univers observable](https://www.wolframalpha.com/input/?i=991267988808424794443839434655920239360814764000951599022939879419136287216681744888844&lk=1&rawformassumption=%22ClashPrefs%22+-%3E+%7B%22Math%22%7D).

Au lieu de cela, nous devons nous tourner vers une méthode _heuristique_ qui fait un travail raisonnablement bon pour estimer les clusters qui produiront le score de modularité le plus élevé, sans essayer chaque possibilité.

C'est un algorithme appelé _Fast-Greedy Modularity-Maximization_, et il est quelque peu analogue à l'algorithme de clustering hiérarchique agglomératif décrit ci-dessus. Au lieu de fusionner selon la distance, 'Mod-Max' fusionne les communautés selon les changements de modularité. 

Voici comment cela se passe :

**Commencez** par attribuer initialement chaque sommet à sa propre communauté, et calculez la modularité de l'ensemble du réseau, _M_.

**Étape 1** nécessite que pour chaque paire de communautés liée par au moins une seule arête, l'algorithme calcule le changement résultant de modularité Δ_M_ si les deux communautés étaient fusionnées en une seule.

**Étape 2** prend ensuite la paire de communautés qui produit la plus grande augmentation de Δ_M_, qui sont ensuite fusionnées. Calculez la nouvelle modularité _M_ pour ce clustering, et gardez-en une trace.

**Répétez** les étapes 1 et 2 — chaque fois en fusionnant la paire de communautés pour laquelle le faire produit le plus grand gain en Δ_M_, puis enregistrez le nouveau motif de clustering et son score de modularité associé _M_.

**Arrêtez** lorsque tous les sommets sont regroupés en un seul cluster géant. Maintenant, l'algorithme vérifie les enregistrements qu'il a gardés au fur et à mesure, et identifie le motif de clustering qui a retourné la valeur la plus élevée de _M_. C'est la structure de communauté retournée.

#### **Détails supplémentaires**

Ouf ! C'était intensif en calcul, au moins pour nous, les humains. 

La théorie des graphes est une source riche de problèmes computationnellement difficiles, souvent NP-difficiles — pourtant elle a également un potentiel incroyable pour fournir des informations précieuses sur des systèmes et des ensembles de données complexes. 

Demandez simplement à Larry Page, dont l'algorithme PageRank éponyme — qui a aidé à propulser Google du statut de start-up à la domination mondiale en moins d'une génération — était entièrement basé sur la théorie des graphes.

La détection de communautés est un domaine de recherche actuel majeur en théorie des graphes, et il existe de nombreuses alternatives à la Maximisation de la Modularité, qui, bien qu'utile, présente certains inconvénients.

Pour commencer, son approche agglomérative voit souvent de petites communautés bien définies englouties dans des communautés plus grandes. Cela est connu sous le nom de _limite de résolution_ — l'algorithme ne trouvera pas de communautés en dessous d'une certaine taille. 

Un autre défi est que plutôt que d'avoir un pic global distinct et facile à atteindre, l'approche Mod-Max tend en fait à produire un large "plateau" de nombreux scores de modularité élevés similaires — ce qui rend quelque peu difficile l'identification absolue du score maximum.

D'autres algorithmes utilisent différentes façons de définir et d'aborder la détection de communautés.

_Edge-Betweenness_ est un algorithme diviseur, commençant avec tous les sommets regroupés en un seul cluster géant. Il procède ensuite à l'élimination itérative des arêtes les moins "importantes" du réseau, jusqu'à ce que tous les sommets soient laissés isolés. Cela produit une structure hiérarchique, avec des sommets similaires plus proches dans la hiérarchie.

Un autre algorithme est _Clique Percolation_, qui prend en compte le chevauchement possible entre les communautés de graphes. 

Un autre ensemble d'algorithmes est basé sur les [marches aléatoires](https://en.wikipedia.org/wiki/Random_walk) à travers le graphe, et il existe des méthodes de [_clustering spectral_](https://en.wikipedia.org/wiki/Spectral_clustering) qui commencent à plonger dans la décomposition en valeurs propres de la matrice d'adjacence et d'autres matrices dérivées de celle-ci. Ces idées sont utilisées dans l'extraction de caractéristiques dans des domaines tels que la vision par ordinateur.

Il serait bien au-delà de la portée de cet article de donner à chaque algorithme son propre exemple détaillé. Il suffit de dire que c'est un domaine de recherche actif, fournissant des méthodes puissantes pour donner un sens aux données qui, même il y a une génération, auraient été extrêmement difficiles à traiter.

### Conclusion

Espérons que cet article vous a informé et inspiré pour mieux comprendre comment les machines peuvent donner un sens aux données. L'avenir est un lieu en rapide évolution, et beaucoup de ces changements seront motivés par ce que la technologie deviendra capable de faire dans la prochaine génération ou deux.

Comme indiqué dans l'introduction, l'apprentissage automatique est un domaine de recherche extraordinairement ambitieux, dans lequel des problèmes massivement complexes nécessitent d'être résolus de la manière la plus précise et la plus efficace possible. Les tâches qui nous viennent naturellement en tant qu'humains nécessitent des solutions innovantes lorsqu'elles sont entreprises par des machines.

Il reste encore beaucoup de progrès à faire, et quiconque contribuera à la prochaine idée révolutionnaire sera sans doute généreusement récompensé. Peut-être que quelqu'un lisant cet article sera derrière le prochain algorithme puissant ?

Toutes les grandes idées doivent commencer quelque part !