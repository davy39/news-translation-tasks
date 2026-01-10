---
title: Comparaison des thèses universitaires brésiliennes et américaines à l'aide
  du traitement du langage naturel
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-05-22T19:25:45.000Z'
originalURL: https://freecodecamp.org/news/comparing-brazilian-and-us-university-theses-using-natural-language-processing-47196a2f9d64
coverImage: https://cdn-media-1.freecodecamp.org/images/1*D4_EAQTuToB_u4nRFRQ_9A.png
tags:
- name: academia
  slug: academia
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: technology
  slug: technology
seo_title: Comparaison des thèses universitaires brésiliennes et américaines à l'aide
  du traitement du langage naturel
seo_desc: 'By Déborah Mesquita

  People are more likely to consider a thesis that’s written by a student at a top-ranked
  University as better than a thesis produced by a student at a University with low
  (or no) status.

  But in what way are the works different? Wha...'
---

Par Débora Mesquita

Les gens sont plus susceptibles de considérer une thèse écrite par un étudiant d'une université bien classée comme meilleure qu'une thèse produite par un étudiant d'une université de faible statut (ou sans statut).

Mais en quoi les travaux diffèrent-ils ? Que peuvent faire les étudiants des universités moins connues pour produire de meilleurs travaux et devenir plus connus ?

J'étais curieuse de répondre à ces questions, alors j'ai décidé d'explorer **deux choses uniquement** : les thèmes des travaux et leur nature. Mesurer la qualité d'une université est quelque chose de très complexe, et ce n'est pas mon objectif ici. Nous allons analyser un certain nombre de thèses de premier cycle en utilisant le traitement du langage naturel. Nous allons extraire des mots-clés en utilisant tf-idf et classer les thèses en utilisant l'Indexation Sémantique Latente (LSI).

### Les données

Notre ensemble de données contient des résumés de thèses de premier cycle en informatique de l'[Université Fédérale de Pernambuco](https://en.wikipedia.org/wiki/Federal_University_of_Pernambuco) (UFPE), située au Brésil, et de l'[Université Carnegie Mellon](https://en.wikipedia.org/wiki/Carnegie_Mellon_University), située aux États-Unis. Pourquoi Carnegie Mellon ? Parce que c'était la seule université où j'ai pu trouver une liste de thèses produites par des étudiants qui étaient à la fin de leur programme de premier cycle.

Le [Times Higher Education World University Rankings](https://www.timeshighereducation.com/world-university-rankings/2017/world-ranking#!/page/0/length/25/sort_by/rank/sort_order/asc/cols/stats) indique que Carnegie Mellon a le 6ème meilleur programme en informatique, tandis que l'UFPE n'est même pas dans ce classement. Carnegie Mellon se classe 23ème dans le classement mondial des universités, et l'UFPE est autour de la 801ème place.

Tous les travaux ont été produits entre les années 2002 et 2016. Chaque thèse contient les informations suivantes :

* titre de la thèse
* résumé de la thèse
* année de la thèse
* université où la thèse a été produite

Les thèses de Carnegie Mellon peuvent être trouvées [ici](https://www.csd.cs.cmu.edu/education/bscs/thesis-topics.html) et les thèses de l'Université Fédérale de Pernambuco peuvent être trouvées [ici](http://cin.ufpe.br/~tg/).

### Étape 1 — Investigation des thèmes des thèses

#### Extraction des mots-clés

Pour obtenir les thèmes de la thèse, nous allons utiliser un algorithme bien connu appelé tf-idf.

#### tf-idf

Ce que fait tf-idf, c'est pénaliser les mots qui **apparaissent beaucoup** dans un document et en même temps **apparaissent beaucoup dans d'autres documents**. Si cela se produit, le mot n'est pas un bon choix pour caractériser ce texte (car le mot pourrait également être utilisé pour caractériser _tous_ les textes). Utilisons [un exemple](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) pour mieux comprendre cela. Nous avons deux documents :

Document 1 :

```
| Terme  | Compte des termes | |--------|------------| | this   |     1      | | is     |     1      | | a      |     2      | | sample |     1      |
```

Et Document 2 :

```
| Terme    | Compte des termes | |---------|------------| | this    |     1      | | is      |     1      | | another |     2      | | example |     3      |
```

D'abord, voyons ce qui se passe. Le mot _this_ apparaît 1 fois dans les deux documents. Cela pourrait signifier que le mot est neutre, n'est-ce pas ?

D'un autre côté, le mot _example_ apparaît 3 fois dans le Document 2 et 0 fois dans le Document 1. Intéressant.

Maintenant, appliquons un peu de mathématiques. Nous devons calculer deux choses : TF (Fréquence des Termes) et IDF (Fréquence Inverse des Documents).

L'équation pour TF est :

```
TF(t) = (Nombre de fois que le terme t apparaît dans le document) / (Nombre total de termes dans le document)
```

Donc pour les termes _this_ et _example_, nous avons :

```
TF('this',   Document 1) = 1/5 = 0.2TF('example',Document 1) = 0/5 = 0
```

```
TF('this',   Document 2) = 1/7 = 0.14TF('example',Document 2) = 3/7 = 0.43
```

L'équation pour IDF est :

```
IDF(t) = log_e(Nombre total de documents / Nombre de documents où le terme t est présent)
```

Pourquoi utilisons-nous un logarithme ici ? Parce que tf-idf est une [heuristique](https://en.wikipedia.org/wiki/Heuristic).

> L'intuition était qu'un terme de requête qui apparaît dans de nombreux documents n'est pas un bon discriminateur, et devrait être donné moins de poids que celui qui apparaît dans peu de documents, et la mesure était une implémentation heuristique de cette intuition. — [Stephen Robertson](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.97.7340&rep=rep1&type=pdf)

Comme [usɛr11852](https://stats.stackexchange.com/users/11852/us%ce%b5r11852) l'explique [ici](https://stats.stackexchange.com/questions/161640/understanding-the-use-of-logarithms-in-the-tf-idf-logarithm) :

> L'aspect mis en avant est que la pertinence d'un terme ou d'un document n'augmente pas proportionnellement avec la fréquence du terme (ou du document). L'utilisation d'une fonction sous-linéaire (le logarithme) aide donc à atténuer cet effet. … L'influence de valeurs très grandes ou très petites (par exemple, des mots très rares) est également amortie. — [usɛr11852](https://stats.stackexchange.com/questions/161640/understanding-the-use-of-logarithms-in-the-tf-idf-logarithm)

En utilisant l'équation pour IDF, nous avons :

```
IDF('this',   Documents) = log(2/2) = 0
```

```
IDF('example',Documents) = log(2/1) = 0.30
```

Et enfin, le TF-IDF :

```
TF-IDF('this',   Document 2) = 0.14 x 0 = 0TF-IDF('example',Document 2) = 0.43 x 0.30 = 0.13
```

J'ai utilisé les 4 mots avec les scores les plus élevés issus de l'algorithme tf-idf pour chaque thèse. J'ai fait cela en utilisant CountVectorizer et TfidfTransformer de [scikit-learn](http://scikit-learn.org/stable/).

Vous pouvez voir le **Jupyter notebook avec le code** [ici](https://github.com/dmesquita/tdcfloripa2017/blob/master/extract_keywords.ipynb).

Avec 4 mots-clés pour chaque thèse, j'ai utilisé la bibliothèque [WordCloud](https://github.com/amueller/word_cloud) pour visualiser les mots pour chaque université.

![Image](https://cdn-media-1.freecodecamp.org/images/rQQbAtpEZYsk2AQ12rPxbIfIVtPf6hDoVq25)
_Mots-clés pour l'UFPE_

![Image](https://cdn-media-1.freecodecamp.org/images/YFw7RGJdQXHiJMvC6Ya0HRYnZnvn5VUlmRHV)
_Mots-clés pour Carnegie Mellon_

### Modélisation des sujets

Une autre stratégie que j'ai utilisée pour explorer les thèmes des thèses des deux universités était la modélisation des sujets avec l'[Indexation Sémantique Latente](https://en.wikipedia.org/wiki/Latent_semantic_analysis) (LSI).

#### Indexation Sémantique Latente

Cet algorithme obtient des données à partir de tf-idf et utilise la décomposition de matrice pour regrouper les documents en sujets. Nous aurons besoin de quelques notions d'algèbre linéaire pour comprendre cela, alors commençons.

#### Décomposition en Valeurs Singulières (SVD)

Tout d'abord, nous devons définir comment faire cette décomposition de matrice. Nous allons utiliser la [Décomposition en Valeurs Singulières](https://en.wikipedia.org/wiki/Singular_value_decomposition) (SVD). Étant donné une matrice _M_ de dimensions _m x n_, _M_ peut être décrite comme :

```
M = UDV*
```

Où _U_ et _V*_ sont des [bases orthonormées](https://en.wikipedia.org/wiki/Orthonormal_basis) (_V*_ représente la transposée de la matrice _V_). Une base orthonormée est le résultat si nous avons deux choses (normal + orthogonal) :

* lorsque tous les vecteurs sont de longueur 1
* lorsque tous les vecteurs sont mutuellement orthogonaux (ils forment un angle de 90°)

_D_ est une matrice diagonale (les entrées en dehors de la diagonale principale sont toutes à zéro).

Pour avoir une idée de la manière dont tout cela fonctionne ensemble, nous allons utiliser l'explication géométrique brillante de [cet article](http://www.ams.org/samplings/feature-column/fcarc-svd) par David Austing.

Disons que nous avons une matrice _M_ :

```
M = | 3 0 |    | 0 1 |
```

Nous pouvons prendre un point (_x_,_y_) dans le plan et le transformer en un autre point en utilisant la multiplication de matrices :

```
| 3 0 |  . | x | = | 3x || 0 1 |    | y |   | y  |
```

L'effet de cette transformation est montré ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/lm4mjFlEkmxbRiGyVkGvNu6ImJkWl-wzuBVA)
_x,y avant. Source : [http://www.ams.org/samplings/feature-column/fcarc-svd](http://www.ams.org/samplings/feature-column/fcarc-svd" rel="noopener" target="_blank" title=")_

![Image](https://cdn-media-1.freecodecamp.org/images/9MmrSVNihenregEuCPu3r56uWv1iOz3xv4zE)
_x,y après. Source : [http://www.ams.org/samplings/feature-column/fcarc-svd](http://www.ams.org/samplings/feature-column/fcarc-svd" rel="noopener" target="_blank" title=")_

Comme nous pouvons le voir, le plan est étiré horizontalement d'un facteur de 3, tandis qu'il n'y a pas de changement vertical.

Maintenant, si nous prenons une autre matrice, _M'_ :

```
M' = | 2 1 |     | 1 2 |
```

L'effet est :

![Image](https://cdn-media-1.freecodecamp.org/images/F-HDjcaeJ-MUM41sRUCxMjmPIMUn611YtNhw)
_x,y avant. Source : [http://www.ams.org/samplings/feature-column/fcarc-svd](http://www.ams.org/samplings/feature-column/fcarc-svd" rel="noopener" target="_blank" title=")_

![Image](https://cdn-media-1.freecodecamp.org/images/tD2f46D10GMQtR9zHl70C8agQ3X6pJbaRcuf)
_x,y après. Source : [http://www.ams.org/samplings/feature-column/fcarc-svd](http://www.ams.org/samplings/feature-column/fcarc-svd" rel="noopener" target="_blank" title=")_

Il n'est pas si clair comment décrire simplement l'effet géométrique de la transformation. Cependant, tournons notre grille de 45 degrés et voyons ce qui se passe.

![Image](https://cdn-media-1.freecodecamp.org/images/H2vS1tWqmjZM104LEw-2Xo5RwPWvgRX6f0sT)
_x,y avant, dans une grille à 45 degrés. Source : [http://www.ams.org/samplings/feature-column/fcarc-svd](http://www.ams.org/samplings/feature-column/fcarc-svd" rel="noopener" target="_blank" title=")_

![Image](https://cdn-media-1.freecodecamp.org/images/mck7i9bXbMhjH6up91o0GUAbFUSAl0KGuFLm)
_x,y après, dans une grille à 45 degrés. Source : [http://www.ams.org/samplings/feature-column/fcarc-svd](http://www.ams.org/samplings/feature-column/fcarc-svd" rel="noopener" target="_blank" title=")_

Nous voyons maintenant que cette nouvelle grille est transformée de la même manière que la grille originale était transformée par la matrice diagonale : **la grille est étirée d'un facteur de 3 dans une direction**.

Maintenant, utilisons quelques définitions. _M_ est une **matrice diagonale** (les entrées en dehors de la diagonale principale sont toutes à zéro) et _M_ et _M'_ sont toutes deux [**symétriques**](https://en.wikipedia.org/wiki/Symmetric_matrix) (si nous prenons les colonnes et les utilisons comme nouvelles lignes, nous obtiendrons la même matrice).

Multiplier par une **matrice diagonale** entraîne un effet de [mise à l'échelle](https://en.wikipedia.org/wiki/Scaling_(geometry)) (une transformation linéaire qui agrandit ou rétrécit les objets par un facteur d'échelle).

> L'effet que nous avons vu (le même résultat pour _M_ et _M'_) est une situation très spéciale qui résulte du fait que la matrice _M'_ est symétrique. Si nous avons une matrice symétrique 2 x 2, il s'avère que nous pouvons toujours faire tourner la grille dans le domaine de sorte que la matrice agisse en étirant et peut-être en réfléchissant dans les deux directions. En d'autres termes, les matrices symétriques se comportent comme des matrices diagonales. — [David Austin](http://www.ams.org/samplings/feature-column/fcarc-svd)

> « C'est l'essence géométrique de la décomposition en valeurs singulières pour les matrices 2 x 2 : pour toute matrice 2 x 2, nous pouvons trouver une grille orthogonale qui est transformée en une autre grille orthogonale. » — [David Austin](http://www.ams.org/samplings/feature-column/fcarc-svd)

Nous allons exprimer ce fait en utilisant des vecteurs : avec un choix approprié de vecteurs unitaires orthogonaux _v1_ et _v2_, les vecteurs _Mv1_ et _Mv2_ sont orthogonaux.

![Image](https://cdn-media-1.freecodecamp.org/images/Ba9G7FFiNLv7Ukb4-f0cuanwn3Il1TxxOHf9)
_v1 et v2 dans la grille originale. Source : [http://www.ams.org/samplings/feature-column/fcarc-svd](http://www.ams.org/samplings/feature-column/fcarc-svd" rel="noopener" target="_blank" title=")_

![Image](https://cdn-media-1.freecodecamp.org/images/pwPiTYpUd7g6bZGdtl3QaY5Znq3Zu-8Uh2uB)
_Mv1 et Mv2 dans la nouvelle grille. Source : [http://www.ams.org/samplings/feature-column/fcarc-svd](http://www.ams.org/samplings/feature-column/fcarc-svd" rel="noopener" target="_blank" title=")_

Nous allons utiliser _n1_ et _n2_ pour désigner les vecteurs unitaires dans la direction de _Mv1_ et _Mv2_. Les longueurs de _Mv1_ et _Mv2_ — désignées par σ1 et σ2 — décrivent la quantité dont la grille est étirée dans ces directions particulières.

Maintenant que nous avons une essence géométrique, revenons à la formule :

```
M = UDV*
```

* _U_ est une matrice dont les colonnes sont les vecteurs _n1_ et _n2_ (**vecteurs unitaires de la grille 'nouvelle'**, dans la direction de _v1_ et v2)
* _D_ est une matrice diagonale dont les entrées sont σ1 et σ2 (**la longueur de chaque vecteur**)
* _V*_ est une matrice dont les colonnes sont _v1_ et _v2_ (**vecteurs de la grille 'ancienne'**)

Maintenant que nous comprenons un peu comment fonctionne la SVD, voyons comment la LSI utilise cette technique pour regrouper les textes. Comme le montre [Ian Soboroff](https://scholar.google.com/citations?user=TcFyZgcAAAAJ) dans son cours de Recherche d'Information [slides](https://www.csee.umbc.edu/~ian/irF02/lectures/12LSI.pdf) :

* _U_ est une matrice pour **transformer de nouveaux documents**
* _D_ est la matrice diagonale qui donne **l'importance relative des dimensions** (nous parlerons plus de ces dimensions dans un instant)
* _V*_ est une **représentation de _M_ en _k_ dimensions**

Pour voir comment cela fonctionne, nous allons utiliser des titres de documents de deux domaines (Interaction Homme-Machine et Théorie des Graphes). Ces exemples proviennent de l'article [An Introduction to Latent Semantic Analysis](http://lsa.colorado.edu/papers/dp1.LSAintro.pdf).

```
c1: Human machine interface for ABC computer applications c2: A survey of user opinion of computer system response time c3: System and human system engineering testing of EPS
```

```
m1: The generation of random, binary, ordered trees m2: The intersection graph of paths in trees m3: Graph minors: A survey
```

La première étape consiste à créer une matrice avec le nombre de fois que chaque terme apparaît :

```
| terme     | c1 | c2 | c3 | m1 | m2 | m3 | |-----------|----|----|----|----|----|----|| human     | 1  | 0  | 1  | 0  | 0  | 0  || interface | 1  | 0  | 0  | 0  | 0  | 0  | | computer  | 1  | 1  | 0  | 0  | 0  | 0  | | user      | 0  | 1  | 0  | 0  | 0  | 0  | | system    | 0  | 1  | 2  | 0  | 0  | 0  | | survey    | 0  | 1  | 0  | 0  | 0  | 1  | | trees     | 0  | 0  | 0  | 1  | 1  | 0  | | graph     | 0  | 0  | 0  | 0  | 1  | 1  | | minors    | 0  | 0  | 0  | 0  | 0  | 1  |
```

En décomposant la matrice, nous obtenons ceci (vous pouvez utiliser cet [outil en ligne](http://www.bluebit.gr/matrix-calculator/default.aspx) pour appliquer la SVD) :

```
# Matrice U (pour transformer de nouveaux documents)
```

```
-0.386  0.222 -0.096 -0.458  0.357 -0.105-0.119  0.055 -0.434 -0.379  0.156 -0.040-0.345 -0.062 -0.615 -0.089 -0.264  0.135-0.226 -0.117 -0.181  0.290 -0.420  0.175-0.760  0.218  0.493  0.133 -0.018  0.044-0.284 -0.498 -0.176  0.374  0.033 -0.311-0.013 -0.321  0.289 -0.571 -0.582 -0.386-0.069 -0.621  0.185 -0.252  0.236  0.675-0.057 -0.382  0.005  0.085  0.453 -0.485
```

Matrice qui donne l'importance relative des dimensions :

```
# Matrice D (importance relative des dimensions)
```

```
2.672 0.000 0.000 0.000 0.000 0.0000.000 1.983 0.000 0.000 0.000 0.0000.000 0.000 1.625 0.000 0.000 0.0000.000 0.000 0.000 1.563 0.000 0.0000.000 0.000 0.000 0.000 1.263 0.0000.000 0.000 0.000 0.000 0.000 0.499
```

Représentation de _M_ en _k_ dimensions (dans ce cas, nous avons _k_ documents) :

```
# Matrice V* (représentation de M en k dimensions)
```

```
-0.318 -0.604 -0.713 -0.005 -0.031 -0.153 0.108 -0.231  0.332 -0.162 -0.475 -0.757-0.705 -0.294  0.548  0.178  0.291  0.009-0.593  0.453 -0.122 -0.365 -0.527  0.132 0.197 -0.531  0.254 -0.461 -0.274  0.572-0.020  0.087 -0.033 -0.772  0.580 -0.242
```

D'accord, nous avons les matrices. Mais maintenant la matrice n'est pas 2 x 2. Avons-nous vraiment besoin du nombre de dimensions que cette matrice terme-document a ? Toutes les dimensions sont-elles des caractéristiques importantes pour chaque terme et chaque document ?

Revenons à l'exemple de David Austin. Disons maintenant que nous avons _M''_ :

```
M'' = | 1 1 |      | 2 2 |
```

![Image](https://cdn-media-1.freecodecamp.org/images/W8PjHGo4AFtHcw1l3BafJSFftpNXKxX-40Ji)
_x,y avant_

Maintenant, _M''_ **n'est plus une matrice symétrique**. Pour cette matrice, la valeur de σ2 est zéro. Sur la grille, le résultat de la multiplication est :

![Image](https://cdn-media-1.freecodecamp.org/images/fVr6rdBLQKOk7vQEHZp509Q6UtXTCSMwVNwc)
_x,y après_

Nous avons que si une valeur de la diagonale principale de _D_ est zéro, **ce terme n'apparaît pas dans la décomposition de _M_**.

> De cette manière, nous voyons que le **rang** de _M_, qui est la dimension de l'image de la transformation linéaire, est égal au nombre de valeurs non nulles. — [David Austin](http://www.ams.org/samplings/feature-column/fcarc-svd)

Ce que fait la LSI, c'est changer la dimensionnalité des termes.

> Dans la matrice originale, les termes sont k-dimensionnels (k est le nombre de documents). Le nouvel espace a une dimensionnalité plus faible, donc les dimensions sont maintenant des groupes de termes qui tendent à co-occurrencer dans les mêmes documents. — [Ian Soboroff](https://www.csee.umbc.edu/~ian/irF02/lectures/12LSI.pdf)

Maintenant, nous pouvons revenir à l'exemple. Créons un espace avec deux dimensions. Pour cela, nous n'utiliserons que deux valeurs de la matrice diagonale _D_ :

```
# Matrice D2
```

```
2.672 0.000 0.000 0.000 0.000 0.0000.000 1.983 0.000 0.000 0.000 0.0000.000 0.000 0.000 0.000 0.000 0.0000.000 0.000 0.000 0.000 0.000 0.0000.000 0.000 0.000 0.000 0.000 0.0000.000 0.000 0.000 0.000 0.000 0.000
```

Comme [Alex Thomo](http://webhome.cs.uvic.ca/~thomo/) l'explique dans [ce tutoriel](http://webhome.cs.uvic.ca/~thomo/svd.pdf), les **termes** sont représentés par les vecteurs lignes de _U2 x D2_ (_U2_ est _U_ avec seulement 2 dimensions) et les **documents** sont représentés par les vecteurs colonnes de _D2 x V2*_ (_V2*_ est _V*_ avec seulement 2 dimensions). Nous multiplions par _D2_ parce que _D_ est la matrice diagonale qui donne l'importance relative des dimensions, vous vous souvenez ?

Ensuite, nous calculons les coordonnées de chaque terme et de chaque document à travers ces multiplications. Le résultat est :

```
human     = (-1.031, 0.440)interface = (-0.318, 0.109)computer  = (-0.922, -0.123)user      = (-0.604, -0.232)system    = (-2.031, -0.232) survey    = (-0.759, -0.988)trees     = (-0.035, -0.637)graph     = (-0.184, -1.231) minors    = (-0.152, -0.758)
```

```
c1        = (-0.850, 0.214)c2        = (-1.614, -0.458)c3        = (-1.905, 0.658)m1        = (-0.013, -0.321)m2        = (-0.083, -0.942)m3        = (-0.409, -1.501)
```

En utilisant matplotlib pour visualiser cela, nous avons :

![Image](https://cdn-media-1.freecodecamp.org/images/lbXXYC51B2DdA6H7syhguOtJaRL2P7hDUznE)
_Le résultat pour chaque terme et chaque document_

Cool, n'est-ce pas ? Les vecteurs en rouge sont des documents d'Interaction Homme-Machine et ceux en bleu sont des documents de Théorie des Graphes.

Et le choix du nombre de dimensions ?

> Le nombre de dimensions retenues dans la LSI est une question empirique. Parce que le principe sous-jacent est que les données originales ne doivent pas être parfaitement régénérées, mais plutôt qu'une dimensionnalité optimale doit être trouvée pour induire correctement les relations sous-jacentes, l'approche factorielle analytique habituelle consistant à choisir une dimensionnalité qui représente le plus parcimonieusement la vraie variance des données originales n'est pas appropriée. — [Source](http://lsa.colorado.edu/papers/dp1.LSAintro.pdf)

La mesure de similarité calculée dans l'espace de dimension réduite est généralement, mais pas toujours, le cosinus entre les vecteurs.

Et maintenant, nous pouvons revenir à l'ensemble de données avec les thèses des universités. J'ai utilisé le [modèle lsi](https://radimrehurek.com/gensim/models/lsimodel.html) de [gensim](https://radimrehurek.com/gensim/index.html). Je n'ai pas trouvé beaucoup de différences entre les travaux des universités (tous semblaient appartenir au même cluster). Le sujet qui différenciait le plus les travaux des universités était celui-ci :

```
y topic:[('object', 0.29383227033104375), ('software', -0.22197520420133632), ('algorithm', 0.20537550622495102), ('robot', 0.18498675015157251), ('model', -0.17565360130127983), ('project', -0.164945961528315), ('busines', -0.15603883815175643), ('management', -0.15160458583774569), ('process', -0.13630070297362168), ('visual', 0.12762128292042879)]
```

Visuellement, nous avons :

![Image](https://cdn-media-1.freecodecamp.org/images/qGWt-ux3yZvGy6Oii3d39jkdaSEe03EKj3qF)
_Visualisation pour le sujet y_

Sur l'image, le sujet _y_ est sur l'axe des y. Nous pouvons voir que les thèses de Carnegie Mellon sont plus associées à **'object', 'robot', et 'algorithm'** et les thèses de l'UFPE sont plus associées à **'software', 'project', et 'business'**. 

Vous pouvez voir le **Jupyter notebook avec le code** [ici](https://github.com/dmesquita/tdcfloripa2017/blob/master/create_clusters.ipynb).

### Étape 2 — Investigation de la nature des travaux

J'ai toujours eu l'impression qu'au Brésil, les étudiants produisent beaucoup de thèses avec des revues de littérature, tandis que dans les autres universités, ils font peu de thèses comme celle-ci. Pour vérifier, j'ai analysé les titres des thèses.

Habituellement, lorsqu'une thèse est une revue de littérature, le mot 'study' apparaît dans le titre. J'ai ensuite pris tous les titres de toutes les thèses et vérifié les mots qui apparaissent le plus, pour chaque université. Les résultats étaient :

![Image](https://cdn-media-1.freecodecamp.org/images/3m9h8rxe9TqywOoZL27WNJ3hIJLdQQPn7GNy)
_Mots des titres de l'UFPE_

![Image](https://cdn-media-1.freecodecamp.org/images/qz3qYBjfO9zaLmgzesQH3Hh8LsaAYeTCEwFZ)
_Mots des titres de Carnegie Mellon_

Vous pouvez voir le **Jupyter notebook avec le code** [ici](https://github.com/dmesquita/tdcfloripa2017/blob/master/analyze_titles.ipynb).

### Résultats

L'impression que j'ai eue de cette analyse simple était que les thèmes des travaux ne différaient pas beaucoup. Mais il était possible de visualiser ce qui semble être les spécialités de chaque institution. L'Université Fédérale de Pernambuco produit plus de travaux liés aux **projets et aux affaires** et Carnegie Mellon produit plus de travaux liés aux **robots et aux algorithmes**. À mon avis, cette différence de spécialités n'est pas quelque chose de mauvais, elle montre simplement que chaque université est spécialisée dans certains domaines.

Un point à retenir était qu'au Brésil, nous devons produire des travaux différents au lieu de simplement faire des revues de littérature.

Une chose importante que j'ai réalisée en faisant l'analyse (et qui ne vient pas des résultats de l'analyse elle-même), c'est que simplement avoir la meilleure thèse ne suffit pas. J'ai commencé l'analyse en essayant d'identifier _pourquoi ils produisent de meilleurs travaux que nous_ et ce que nous pouvons faire pour _y arriver_ et _devenir plus connus_. Mais j'ai senti que peut-être une façon d'_y arriver_ est simplement de montrer plus de nos travaux et d'échanger plus de connaissances avec eux. La raison est que cela peut nous forcer à produire des articles plus pertinents et à nous améliorer avec les retours.

Je pense aussi que cela s'applique à tout le monde, tant pour les étudiants universitaires que pour nous, les professionnels. Cette citation qui résume bien cela :

> « Ce n'est pas suffisant d'être bon. Pour être trouvé, il faut être trouvable. » — [Austin Kleon](https://www.goodreads.com/work/quotes/25771145-show-your-work-10-ways-to-share-your-creativity-and-get-discovered)

Et c'est tout, merci d'avoir lu !

*Si vous avez trouvé cet article utile, cela signifierait beaucoup si vous cliquez sur le ? et partagez avec des amis. Suivez-moi pour plus d'articles sur la Science des Données et l'Apprentissage Automatique.*