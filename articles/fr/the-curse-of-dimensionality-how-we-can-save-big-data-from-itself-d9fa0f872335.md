---
title: Échapper à la malédiction de la dimensionnalité
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-12T05:27:04.000Z'
originalURL: https://freecodecamp.org/news/the-curse-of-dimensionality-how-we-can-save-big-data-from-itself-d9fa0f872335
coverImage: https://cdn-media-1.freecodecamp.org/images/1*i-RTdVP-I_JIod0o2xnarg.png
tags:
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Échapper à la malédiction de la dimensionnalité
seo_desc: 'By Peter Gleeson

  How do machines ‘see’? Or, in general, how can computers reduce an input of complex,
  high-dimensional data into a more manageable number of features?

  Extend your open hand in front of a nearby light-source, so that it casts a shadow
  ...'
---

Par Peter Gleeson

Comment les machines « voient-elles » ? Ou, en général, comment les ordinateurs peuvent-ils réduire une entrée de données complexes et de haute dimension en un nombre plus gérable de caractéristiques ?

Tendez votre main ouverte devant une source de lumière à proximité, de sorte qu'elle projette une ombre contre la surface la plus proche. Faites tourner votre main et étudiez comment son ombre change. Remarquez que sous certains angles, elle projette une ombre étroite et fine. Pourtant, sous d'autres angles, l'ombre ressemble beaucoup plus à la forme d'une main.

![Image](https://cdn-media-1.freecodecamp.org/images/v-sEynqwgEZO8MYXjYTYco1Z8snXuUYU-0fQ)
*En faisant tourner votre main, voyez si vous pouvez trouver l'angle qui préserve le plus possible sa forme.*

Voyez si vous pouvez trouver l'angle qui projette le mieux votre main. Préservez autant d'informations que possible sur sa forme.

Derrière toute l'algèbre linéaire et les méthodes computationnelles, **c'est** ce que la réduction de dimensionnalité cherche à faire avec les données de haute dimension. Par rotation, vous pouvez trouver l'angle optimal qui représente votre main en 3D comme une ombre en 2D.

Il existe des techniques statistiques qui peuvent trouver la meilleure représentation des données dans un espace de dimension inférieure à celui dans lequel elles ont été initialement fournies.

Dans cet article, nous verrons pourquoi cette procédure est souvent nécessaire, via un tour de géométrie et de combinatoire qui défie l'esprit. Ensuite, nous examinerons le code derrière une gamme d'algorithmes utiles de réduction de dimensionnalité, étape par étape.

Mon objectif est de rendre ces concepts souvent difficiles plus accessibles au lecteur général — toute personne intéressée par la manière dont les techniques de science des données et d'apprentissage automatique transforment rapidement le monde tel que nous le connaissons.

L'apprentissage automatique semi-supervisé est un sujet brûlant dans le domaine de la science des données, et pour de bonnes raisons. Combiner les dernières avancées théoriques avec le matériel puissant d'aujourd'hui est une recette pour des percées passionnantes et des titres évoquant la science-fiction.

Nous pouvons attribuer une partie de son attrait à la manière dont il approximative notre propre expérience humaine d'apprentissage du monde qui nous entoure.

L'idée de haut niveau est simple : étant donné des informations sur un ensemble de données « d'entraînement » étiquetées, comment pouvons-nous généraliser et faire des inférences précises sur un ensemble de données précédemment « non vues » ?

Les algorithmes d'apprentissage automatique sont conçus pour mettre en œuvre cette idée. Ils utilisent une gamme d'hypothèses et de types de données d'entrée différents. Ceux-ci peuvent être simplistes comme le [clustering K-means](http://www.cs.otago.ac.nz/cosc430/ok.d/hartigan_1979_kmeans.pdf). Ou complexes comme l'[Allocation de Dirichlet Latente](http://ai.stanford.edu/~ang/papers/jair03-lda.pdf).

Derrière tous les algorithmes semi-supervisés, il y a deux hypothèses clés : **la continuité** et **l'intégration**. Celles-ci concernent la nature de l'[espace de caractéristiques](https://en.wikipedia.org/wiki/Feature_vector) dans lequel les données sont décrites. Ci-dessous se trouve une représentation visuelle des points de données dans un espace de caractéristiques en 3D.

![Image](https://cdn-media-1.freecodecamp.org/images/2oQ-MRCgdylb9ufU-JhKuUmqFLOFf62V1nau)
*Oui — c'est essentiellement juste un graphique de dispersion*

Les espaces de caractéristiques de dimension supérieure peuvent être considérés comme des graphiques de dispersion avec plus d'axes que nous ne pouvons en dessiner ou visualiser. Les mathématiques restent plus ou moins les mêmes !

La **continuité** est l'idée que des points de données similaires, comme ceux qui sont proches les uns des autres dans l'« espace de caractéristiques », sont plus susceptibles de partager la même étiquette. Avez-vous remarqué dans le graphique de dispersion ci-dessus que les points à proximité sont de couleur similaire ? Cette hypothèse est à la base d'un ensemble d'algorithmes d'apprentissage automatique appelés [algorithmes de clustering](https://medium.freecodecamp.org/how-machines-make-sense-of-big-data-an-introduction-to-clustering-algorithms-4bd97d4fbaba).

L'**intégration** est l'hypothèse que, bien que les données puissent être décrites dans un espace de caractéristiques de haute dimension tel qu'un « graphique de dispersion avec trop d'axes à dessiner », la structure sous-jacente des données est probablement de beaucoup plus faible dimension.

Par exemple, dans le graphique de dispersion ci-dessus, nous avons montré les données dans un espace de caractéristiques en 3D. Mais les points tombent plus ou moins le long d'un plan en 2D.

L'intégration nous permet de simplifier efficacement nos données en recherchant leur structure sous-jacente.

### Alors, à propos de cette malédiction...

En plus d'avoir le nom le plus cool et le plus effrayant de toute la science des données, les phénomènes collectivement connus sous le nom de [malédiction de la dimensionnalité](https://en.wikipedia.org/wiki/Curse_of_dimensionality) posent également de réels défis aux praticiens du domaine.

Bien que quelque peu du côté mélodramatique, le titre reflète une réalité inévitable de travailler avec des ensembles de données de haute dimension. Cela inclut ceux où chaque point de données est décrit par de nombreuses mesures ou « caractéristiques ».

Le thème général est simple — plus vous travaillez avec de dimensions, moins les techniques computationnelles et statistiques standard deviennent efficaces. Cela a des répercussions qui nécessitent des solutions de contournement sérieuses lorsque les machines traitent des Big Data. Avant de plonger dans certaines de ces solutions, discutons des défis soulevés par les données de haute dimension en premier lieu.

#### Charge de travail computationnelle

Travailler avec des données devient plus exigeant à mesure que le nombre de dimensions augmente. Comme de nombreux défis en science des données, cela se résume à la [combinatoire](http://mathworld.wolfram.com/Combinatorics.html).

![Image](https://cdn-media-1.freecodecamp.org/images/c0tnBcOZVtQdG2MHHmDmwExL60vmaciRhAlC)
*Imaginez rechercher un ensemble de boîtes pour trouver un trésor*

Avec _n_ = 1, il n'y a que 5 boîtes à rechercher. Avec _n_ = 2, il y a maintenant 25 boîtes ; et avec _n_ = 3, il y a 125 boîtes à rechercher. À mesure que _n_ devient plus grand, il devient difficile d'échantillonner toutes les boîtes. Cela rend le trésor plus difficile à trouver — surtout si beaucoup de boîtes sont probablement vides !

En général, avec _n_ dimensions, chacune permettant _m_ états, nous aurons _m^n_ combinaisons possibles. Essayez de substituer quelques valeurs différentes et vous serez convaincu que cela présente un défi de charge de travail par rapport à l'échantillonnage pour les machines chargées d'échantillonner répétitivement différentes combinaisons de variables.

Avec des données de haute dimension, nous ne pouvons tout simplement pas échantillonner de manière exhaustive toutes les combinaisons possibles, laissant de vastes régions de l'espace de caractéristiques dans l'obscurité.

#### Redondance dimensionnelle

Nous n'avons peut-être même pas besoin de soumettre nos machines à un travail aussi exigeant. Avoir de nombreuses dimensions ne garantit pas que chaque dimension est particulièrement utile. La plupart du temps, nous mesurons peut-être le même motif sous-jacent de plusieurs manières différentes.

Par exemple, nous pourrions examiner des données sur des joueurs de football professionnel ou de soccer. Nous pourrions décrire chaque joueur en six dimensions.

Cela pourrait être en termes de :

* nombre de buts marqués
* nombre de tirs tentés
* nombre de chances créées
* nombre de tacles gagnés
* nombre de blocs effectués
* nombre de dégagements effectués

![Image](https://cdn-media-1.freecodecamp.org/images/XD4OkqqZKK8tK8vDOVwz4RSdwgdQ4LyJchZS)
*Exemple de données sportives (... complètement fictives !)*

Il y a six dimensions. Pourtant, vous pourriez voir que nous décrivons en fait seulement deux qualités sous-jacentes — la capacité offensive et défensive — sous plusieurs angles.

C'est un exemple de l'hypothèse d'intégration dont nous avons discuté précédemment. Les données de haute dimension ont souvent une structure sous-jacente de beaucoup plus faible dimension.

Dans ce cas, nous nous attendrions à voir de fortes corrélations entre certaines de nos dimensions. **Les buts marqués** et **les tirs tentés** ne seront probablement pas indépendants l'un de l'autre. Une grande partie de l'information dans chaque dimension est déjà contenue dans certaines des autres.

Souvent, les données de haute dimension montreront un tel comportement. Beaucoup des dimensions sont, dans un certain sens, redondantes.

Les dimensions fortement corrélées peuvent avoir un impact nuisible sur d'autres techniques statistiques qui reposent sur des [hypothèses d'indépendance](http://www.stat.cmu.edu/~cshalizi/36-220/lecture-5.pdf). Cela pourrait conduire à des problèmes redoutés tels que le [surajustement](https://en.wikipedia.org/wiki/Overfitting).

De nombreux ensembles de données de haute dimension sont en fait les résultats de processus génératifs de plus faible dimension. L'exemple classique est [la voix humaine](http://www.sciencedirect.com/science/article/pii/S096098221001701X). Elle peut produire des données de très haute dimension à partir du mouvement d'un petit nombre de cordes vocales.

La haute dimensionnalité peut masquer les processus génératifs. Ce sont souvent ceux qui nous intéressent à apprendre davantage.

Non seulement la haute dimensionnalité pose des défis computationnels, mais elle le fait souvent sans apporter beaucoup de nouvelles informations.

Et ce n'est pas tout ! Voici où les choses commencent à devenir bizarres.

#### Insanité géométrique

Un autre problème découlant des données de haute dimension concerne l'efficacité de différentes métriques de distance, et les techniques statistiques qui en dépendent.

C'est un concept difficile à saisir, car nous sommes tellement habitués à penser en termes quotidiens de trois dimensions spatiales. Cela peut être un peu un obstacle pour nous, humains.

La géométrie commence à devenir étrange dans l'espace de haute dimension. Non seulement étrange à visualiser, mais plus « WTF-est-ce que c'est ?! » étrange.

Commençons par un exemple dans un nombre de dimensions plus familier. Supposons que vous envoyez un disque d'un diamètre de 10 cm à un ami qui aime les disques. Vous pourriez le faire entrer parfaitement dans une enveloppe carrée avec des côtés de 10 cm, ne laissant que les coins inutilisés. Quel pourcentage d'espace dans l'enveloppe reste inutilisé ?

Eh bien, l'enveloppe a une surface de 100 cm² à l'intérieur, et le disque occupe 78,5398... cm² (rappelons que [l'aire d'un cercle est égale à πr²](https://en.wikipedia.org/wiki/Area_of_a_circle)). En d'autres termes, le disque occupe ~78,5 % de l'espace disponible. Moins d'un quart reste vide dans les quatre coins.

Maintenant, supposons que vous emballez une balle qui a également un diamètre de 10 cm, cette fois dans une boîte en forme de cube avec des côtés de 10 cm. La boîte a un volume total de 10³ = 1000 cm³, tandis que la balle a un volume de 523,5988... cm³ (le [volume d'une sphère 3D](http://www.mathopenref.com/spherevolume.html) peut être calculé en utilisant 4/3 * πr³). Cela représente presque 52,4 % du volume total disponible. En d'autres termes, **presque la moitié** du volume de la boîte est de l'espace vide dans les huit coins.

Voyez ces exemples ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/-c3Gq6RvKlrY2av3KvtUEvS4yimS9JmpPOjk)
*Voyez-vous comment il reste plus d'espace vide dans le cube que dans le carré ?*

Le volume d'une sphère en 3D est plus petit dans l'exemple B que celui d'un cercle dans l'exemple B en 2D. Le centre d'un cube est plus petit que le centre d'un carré avec le même côté de longueur. Ce schéma continue-t-il dans plus de trois dimensions ? Ou lorsque nous traitons avec des **hyper-sphères** et des **hyper-cubes** ? Par où commençons-nous ?

Réfléchissons à ce qu'est réellement une sphère, mathématiquement parlant. Nous pouvons définir une sphère _n_-dimensionnelle comme la surface formée par la rotation d'un rayon de longueur fixe _r_ autour d'un point central dans un espace (_n+1_)-dimensionnel.

En 2D, cela trace le bord d'un cercle qui est une ligne 1D. En 3D, cela trace la surface 2D d'une sphère quotidienne. En 4D+, que nous ne pouvons pas facilement visualiser, ce processus dessine une hyper-sphère.

Il est plus difficile de se représenter ce concept dans des dimensions supérieures, mais le schéma que nous avons vu précédemment continue. Le volume relatif de la sphère diminue.

La [formule généralisée](http://mathworld.wolfram.com/Ball.html) pour le volume d'une hyper-sphère de rayon _r_ en _n_ dimensions est montrée ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/wEWJuTvkZ-6iJimgBBZsBVX4BWi67nGxpXpK)
*On ne sait jamais quand cela pourrait s'avérer utile !*

Γ est la fonction Gamma, décrite [ici](https://en.wikipedia.org/wiki/Gamma_function). Techniquement, nous devrions appeler le volume en > 3 dimensions **hyper-contenu**.

Le volume d'un hyper-cube avec des côtés de longueur _2r_ en _n_ dimensions est simplement (2_r_)^_n_. Si nous étendons notre exemple d'emballage de sphères à des dimensions supérieures, nous trouvons que le pourcentage de l'espace global rempli peut être trouvé par la formule générale :

![Image](https://cdn-media-1.freecodecamp.org/images/ViiaGScu2quDnAU0ttvQmz12uBJoaVjUJb2l)

Nous avons pris la première formule, multiplié par 1 / (2_r_)^_n_ et ensuite annulé là où _r_^_n_ apparaît des deux côtés de la fraction.

Regardez comment nous avons _n_/2 et _n_ comme exposants sur le numérateur (« haut ») et le dénominateur (« bas ») de cette fraction respectivement. Nous pouvons voir que lorsque _n_ augmente, le dénominateur croîtra plus vite que le numérateur. Cela signifie que la fraction devient de plus en plus petite. Sans parler du fait que le dénominateur contient également une fonction Gamma mettant en vedette _n_.

La [fonction Gamma](http://mathworld.wolfram.com/GammaFunction.html) est comme la [fonction factorielle](http://mathworld.wolfram.com/Factorial.html)... vous savez, celle où (_n_! = 2 x 3 x ... x _n_). La fonction Gamma tend également à croître très rapidement. En fait, _Γ(n) = (n-1)!_.

Cela signifie que lorsque le nombre de dimensions augmente, le dénominateur croît beaucoup plus vite que le numérateur. Ainsi, le volume de l'hyper-sphère diminue vers zéro.

Au cas où vous n'auriez pas très envie de calculer des fonctions Gamma et des hyper-volumes dans un espace de haute dimension, j'ai fait un graphique rapide :

![Image](https://cdn-media-1.freecodecamp.org/images/76EXIcg0v9VyH2SjnQscvF-hw50CUTH7aNTm)
*L'hyper-sphère rétrécit à mesure que nous ajoutons des dimensions supplémentaires !*

Le volume de l'hyper-sphère (par rapport à l'espace dans lequel elle vit) chute rapidement vers zéro. Cela a de graves répercussions dans le monde du Big Data.

**...Pourquoi ?**

Rappelons nos exemples en 2D et 3D. L'espace vide correspondait aux « coins » ou aux « régions éloignées » de l'espace global.

Pour le cas en 2D, notre carré avait 4 coins qui représentaient 21,5 % de l'espace total.

Dans le cas en 3D, notre cube avait maintenant 8 coins qui représentaient 47,6 % de l'espace total.

À mesure que nous passons à des dimensions supérieures, nous trouverons encore plus de coins. Cela représentera un pourcentage toujours croissant de l'espace total disponible.

Imaginez maintenant que nous avons des données réparties dans un espace multidimensionnel. Plus la dimensionnalité est élevée, plus la proportion totale de nos données sera « projetée » dans les coins, et plus les distances seront similaires entre les distances minimales et maximales entre les points.

Dans des dimensions supérieures, nos données sont plus clairsemées et plus régulièrement espacées. Cela rend la plupart des [fonctions de distance](https://en.wikipedia.org/wiki/Metric_%28mathematics%29) moins efficaces.

### Échapper à la malédiction !

Il existe un certain nombre de techniques qui peuvent projeter nos données de haute dimension dans un espace de dimension inférieure. Rappelons l'analogie d'un objet 3D placé devant une source de lumière projetant une ombre 2D contre un mur.

En réduisant la dimensionnalité de nos données, nous obtenons trois avantages :

* une charge de travail computationnelle plus légère
* moins de redondance dimensionnelle
* des métriques de distance plus efficaces

Pas étonnant que la réduction de dimensionnalité soit si cruciale dans les applications avancées d'apprentissage automatique telles que la [vision par ordinateur](http://www.bmva.org/visionoverview), le [TAL](https://en.wikipedia.org/wiki/Natural_language_processing) et la [modélisation prédictive](https://en.wikipedia.org/wiki/Predictive_modelling).

Nous allons passer en revue cinq méthodes couramment appliquées aux ensembles de données de haute dimension. Nous nous limiterons aux méthodes d'**extraction** de caractéristiques. Elles tentent d'identifier de nouvelles caractéristiques sous-jacentes aux données originales.

Les méthodes de [sélection de caractéristiques](https://en.wikipedia.org/wiki/Feature_selection) choisissent lesquelles des caractéristiques originales valent la peine d'être conservées. Nous les laisserons pour un autre article !

C'est une longue lecture avec beaucoup d'exemples détaillés. Alors ouvrez votre éditeur de code préféré, mettez la bouilloire en marche, et commençons !

### Mise à l'échelle multidimensionnelle (MDS)

#### Résumé visuel

![Image](https://cdn-media-1.freecodecamp.org/images/v0pcook5z-yrTIxt1xXqk7q6L4YeAt4Iht5Y)

MDS fait référence à une famille de techniques utilisées pour réduire la dimensionnalité. Elles projettent les données originales dans un espace de dimension inférieure, tout en préservant autant que possible les distances entre les points. Cela est généralement réalisé en minimisant une fonction de perte (souvent appelée **stress** ou **strain**) via un algorithme itératif.

Le stress est une fonction qui mesure combien de la distance originale entre les points a été perdue. Si notre projection fait un bon travail en retenant les distances originales, la valeur retournée sera faible.

#### Exemple détaillé

Si vous avez R installé, ouvrez-le dans votre IDE de choix. Sinon, si vous voulez suivre quand même, [vérifiez ce R-fiddle](http://www.r-fiddle.org/#/fiddle?id=zhhW8AQX&version=2).

Nous allons examiner le CMDS (Classical MDS) dans cet exemple. Il donnera une sortie identique à l'ACP (Analyse en Composantes Principales), que nous discuterons plus tard.

Nous allons utiliser deux des forces de R dans cet exemple :

* travailler avec la multiplication de matrices
* l'existence de jeux de données intégrés

Commencez par définir nos données d'entrée :

```r
M <- as.matrix(UScitiesD)
```

Nous voulons commencer avec une **matrice de distance** où chaque élément représente la [distance euclidienne](https://en.wikipedia.org/wiki/Euclidean_distance) (pensez au théorème de Pythagore) entre nos observations. Les ensembles de données `UScitiesD` et `eurodist` dans R sont des matrices de distance en ligne droite et routière entre une sélection de villes américaines et européennes.

Avec des données d'entrée non distantes, nous aurions besoin d'une étape préliminaire pour calculer d'abord la matrice de distance.

```r
M <- as.matrix(dist(raw_data))
```

Avec MDS, nous cherchons à trouver une **projection** de faible dimension des données qui préserve le mieux les distances entre les points. Dans le MDS classique, nous visons à minimiser une fonction de perte appelée `Strain`_._

![Image](https://cdn-media-1.freecodecamp.org/images/2jCi6r3r0ITuWKbJIiPC2Gjf2OllYnHSsw1K)

[Strain](http://www.stat.yale.edu/~lc436/papers/JCGS-mds.pdf) est une fonction qui calcule combien une projection donnée de faible dimension déforme les distances originales entre les points.

Avec MDS, des approches itératives (par exemple, via la [descente de gradient](http://mathworld.wolfram.com/MethodofSteepestDescent.html)) sont généralement utilisées pour nous rapprocher progressivement d'une solution optimale. Mais avec CMDS, il existe une méthode algébrique pour y parvenir.

Il est temps d'introduire un peu d'algèbre linéaire. Si ce sujet est nouveau pour vous, ne vous inquiétez pas — vous comprendrez les choses avec un peu de pratique. Un bon point de départ est de voir les matrices comme des blocs de nombres que nous pouvons manipuler tous à la fois, et de travailler à partir de là.

Les matrices suivent certaines règles pour les opérations. L'[addition](https://www.mathsisfun.com/algebra/matrix-introduction.html) et la [multiplication](https://www.mathsisfun.com/algebra/matrix-multiplying.html) peuvent être décomposées ou **décomposées** en [valeurs propres et vecteurs propres correspondants](https://www.utdallas.edu/~herve/Abdi-EVD2007-pretty.pdf).

**_Eigen-quoi maintenant ?_**

Une façon simple de penser à tout ce truc d'eigen est en termes de [transformations](https://www.mathplanet.com/education/geometry/transformations/transformation-using-matrices). Les transformations peuvent changer à la fois la direction et la longueur des [vecteurs](https://en.wikipedia.org/wiki/Euclidean_vector) sur lesquels elles agissent.

Comme montré ci-dessous, la matrice **A** décrit une transformation, qui est appliquée à deux vecteurs en multipliant **A** x _v_. La direction du vecteur bleu de 1 unité à travers et 3 unités vers le haut reste inchangée. Seule sa longueur change, ici elle double. Cela fait du vecteur bleu un vecteur propre de **A** avec une valeur propre de 2.

Le vecteur orange **change** de direction lorsqu'il est multiplié par **A**, donc il ne peut pas être un vecteur propre de **A**.

![Image](https://cdn-media-1.freecodecamp.org/images/8556cshR7FwIFkka9ZRccU2mhXaCrgD9y9xC)

Retour au CMDS — notre premier mouvement est de définir une [matrice de centrage](https://en.wikipedia.org/wiki/Centering_matrix) qui nous permet de **double centrer** nos données d'entrée. En R, nous pouvons l'implémenter comme suit :

```r
n <- nrow(M)
C <- diag(n) - (1/n) * matrix(rep(1, n^2), nrow = n)
```

Nous utilisons ensuite le support de R pour la multiplication de matrices `%*%` pour appliquer la matrice de centrage à nos données originales afin de former une nouvelle matrice, **B**.

```r
B <- -(1/2) * C %*% M %*% C
```

Bien ! Maintenant, nous pouvons commencer à construire notre matrice de projection en 2D. Pour ce faire, nous définissons deux matrices supplémentaires en utilisant les **vecteurs propres** associés aux deux plus grandes **valeurs propres** de la matrice **B**.

Comme ceci :

```r
E <- eigen(B)$vectors[,1:2]
L <- diag(2) * eigen(B)$values[1:2]
```

Calculons notre matrice de sortie en 2D **X**, et traçons les données selon les nouvelles coordonnées.

```r
X <- E %*% L^(1/2)
plot(-X, pch=4)
text(-X, labels = rownames(M), cex = 0.5)
```

![Image](https://cdn-media-1.freecodecamp.org/images/0HDy11LN4eumDJ7GnAvWt0aazlx-XSdTHpw3)
*N'hésitez pas à superposer une carte des États-Unis et vérifiez que tout s'aligne comme il se doit !*

Comment cela semble-t-il ? Plutôt bien, non ? Nous avons récupéré la disposition sous-jacente en 2D des villes à partir de notre matrice de distance d'entrée originale. Bien sûr, cette technique nous permet d'utiliser des matrices de distance calculées à partir d'ensembles de données de dimension encore plus élevée.

En savoir plus sur la variété des techniques qui relèvent de l'étiquette [MDS](http://www.bristol.ac.uk/media-library/sites/cmm/migrated/documents/chapter3.pdf).

### Analyse en Composantes Principales (ACP)

#### Résumé Visuel

![Image](https://cdn-media-1.freecodecamp.org/images/iCUMW5Ey7lPsBEDD3ueOq7ZFsNhgWyZ7NGaV)
*Faites tourner les axes pour décrire autant que possible la variation dans les données. Nous conservons la plupart de la variation dans les données en utilisant seulement un de nos nouveaux axes.*

Dans un grand ensemble de données avec de nombreuses dimensions, certaines des dimensions peuvent bien être corrélées et décrire essentiellement les mêmes informations sous-jacentes. Nous pouvons utiliser l'algèbre linéaire pour projeter nos données dans un espace de dimension inférieure, tout en conservant autant que possible les informations sous-jacentes.

Le résumé visuel ci-dessus fournit une explication de faible dimension. Dans le graphique de gauche, nos données sont décrites par deux axes, _x_ et _y_.

Dans le graphique du milieu, nous faisons tourner les axes à travers les données dans la direction qui capture autant de variation que possible. Le nouvel axe **PC1** décrit beaucoup plus de variation que l'axe **PC2**. En fait, nous pourrions ignorer **PC2** et conserver tout de même un grand pourcentage de la variation dans les données.

#### Exemple détaillé

Utilisons un exemple à petite échelle pour illustrer l'idée principale. Dans une session R ou dans [ce snippet sur R-fiddle](http://www.r-fiddle.org/#/fiddle?id=Vs42oTmQ&version=2)), chargeons l'un des jeux de données intégrés.

```r
data <- as.matrix(mtcars)
head(data)
dim(data)
```

Ici, nous avons 32 observations de différentes voitures sur 11 dimensions. Elles incluent des caractéristiques et des mesures telles que mpg, cylindres, puissance...

Mais combien de ces 11 dimensions avons-nous réellement besoin ? Certaines d'entre elles sont-elles corrélées ?

Calculons la corrélation entre le nombre de cylindres et la puissance. Sans aucune connaissance préalable, que pourrions-nous nous attendre à trouver ?

```r
cor(mtcars$cyl, mtcars$hp)
```

C'est un résultat intéressant. À +0,83, nous trouvons que le [coefficient de corrélation](http://www.investopedia.com/markets/) est assez élevé. Cela suggère que le nombre de cylindres et la puissance décrivent tous deux la même caractéristique sous-jacente. Est-ce que plus de nos dimensions font quelque chose de similaire ?

Corrélons toutes les paires de nos dimensions et construisons une **matrice de corrélation**. Parce que la vie est trop courte.

```r
cor(data)
```

Chaque cellule contient le coefficient de corrélation entre les dimensions de chaque ligne et colonne. La diagonale est toujours égale à 1.

Les coefficients de corrélation proches de +1 montrent une forte corrélation positive. Les coefficients proches de -1 montrent une forte corrélation négative. Nous pouvons voir certaines valeurs proches de -1 et +1 dans notre matrice de corrélation. Cela montre que nous avons certaines dimensions corrélées dans notre ensemble de données.

C'est cool, mais nous avons toujours le même nombre de dimensions avec lesquelles nous avons commencé. Jetons-en quelques-unes !

Pour ce faire, nous pouvons ressortir l'algèbre linéaire. L'un des points forts du langage R est qu'il est bon en algèbre linéaire, et nous allons en faire usage dans notre code. Notre première étape consiste à prendre notre matrice de corrélation et à trouver ses valeurs propres.

```r
e <- eigen(cor(data))
```

Inspectons les valeurs propres :

```r
e$valuesbarplot(e$values/sum(e$values),
    main="Proportion Variance expliquée")
```

![Image](https://cdn-media-1.freecodecamp.org/images/5KHzXlvX9bBvsYn6QtFyZPuoemJveCCQcSXB)
*Valeurs propres de la matrice de corrélation mtcars*

Nous voyons 11 valeurs qui diminuent assez dramatiquement sur le graphique à barres ! Nous voyons que le vecteur propre associé à la plus grande valeur propre explique environ 60 % de la variation dans nos données. Le vecteur propre associé à la deuxième plus grande valeur propre explique environ 24 % de la variation dans nos données originales. Cela fait déjà 84 % de la variation dans les données, expliquée par deux dimensions !

D'accord, disons que nous voulons conserver 90 % de la variation dans notre ensemble de données original. Combien de dimensions devons-nous conserver pour y parvenir ?

```r
cumulative <- cumsum(e$values/sum(e$values))
print(cumulative)

i <- which(cumulative >= 0.9)[1]
print(i)
```

Nous calculons la somme cumulative de la proportion relative de la variance totale de nos valeurs propres. Nous voyons que les vecteurs propres associés aux 4 plus grandes valeurs propres peuvent décrire 92,3 % de la variation originale dans nos données.

C'est utile ! Nous pouvons conserver >90 % de la structure originale en utilisant seulement 4 dimensions. Projetons l'ensemble de données original sur un espace en 4D. Pour ce faire, nous devons créer une matrice de poids, que nous appellerons **W**.

```r
W <- e$vectors[1:ncol(data),1:i]
```

**W** est une matrice 11 x 4. Rappelez-vous, 11 est le nombre de dimensions dans nos données originales, et 4 est le nombre que nous voulons avoir pour nos données transformées. Chaque colonne dans **W** est donnée par les vecteurs propres correspondant aux quatre plus grandes valeurs propres que nous avons vues précédemment.

Pour obtenir nos données transformées, nous multiplions l'ensemble de données original par la matrice de poids **W**. En R, nous effectuons la multiplication de matrices avec l'opérateur %*%.

```r
tD <- data %*% W
head(tD)
```

Nous pouvons visualiser notre ensemble de données transformé. Maintenant, chaque voiture est décrite en termes de 4 composantes principales au lieu des 11 dimensions originales. Pour mieux comprendre ce que ces composantes principales décrivent réellement, nous pouvons les corrélier avec les 11 dimensions originales.

```r
cor(data, tD[,1:i])
```

Nous voyons que la composante 1 est négativement corrélée avec les cylindres, la puissance et la cylindrée. Elle est également positivement corrélée avec le mpg et la possession d'un moteur droit (par opposition à un moteur en V). Cela suggère que la composante 1 est une mesure du type de moteur.

Les voitures avec des moteurs grands et puissants auront un score négatif pour la composante 1. Les moteurs plus petits et les voitures plus économes en carburant auront un score positif. Rappelez-vous que cette composante décrit environ 60 % de la variation dans les données originales.

De même, nous pouvons interpréter les composantes restantes de cette manière. Cela peut devenir plus difficile (si ce n'est impossible) à faire au fur et à mesure que nous avançons. Chaque composante suivante décrit une proportion de plus en plus petite de la variation globale dans les données. Rien ne vaut un peu d'expertise spécifique au domaine !

Il existe plusieurs aspects dans lesquels l'ACP peut varier par rapport à la méthode décrite ici. Vous pouvez lire un [livre](http://cda.psych.uiuc.edu/statistical_learning_course/Jolliffe%20I.%20Principal%20Component%20Analysis%20(2ed.,%20Springer,%202002)(518s)_MVsa_.pdf) entier sur le sujet.

### Analyse Discriminante Linéaire (LDA)

#### Résumé Visuel

![Image](https://cdn-media-1.freecodecamp.org/images/T1HUVIg84VZ2XSlPXDNQOwjOmx4uQZYLDrlx)
*Avec LDA, nous voulons trouver des axes qui séparent au mieux les différentes classes de données*

Sur l'axe original, les classes rouge et bleue se chevauchent. Par rotation, nous pouvons trouver un nouvel axe qui sépare mieux les classes. Nous pouvons choisir d'utiliser cet axe pour projeter nos données dans un espace de dimension inférieure.

L'ACP cherche des axes qui décrivent le mieux la variation au sein des données. L'Analyse Discriminante Linéaire (LDA) cherche des axes qui discriminent le mieux entre deux ou plusieurs classes au sein des données.

Cela est réalisé en calculant deux mesures

* **variance intra-classe**
* **variance inter-classe**.

L'objectif est d'optimiser le rapport entre elles. Il y a une variance minimale **au sein** de chaque classe et une variance maximale **entre** les classes. Nous pouvons faire cela avec des méthodes algébriques.

![Image](https://cdn-media-1.freecodecamp.org/images/FVB0kZoUgkFyNGnieASp0ucNZ9FJo8vUV4t8)
*Trouver des axes qui minimisent le rapport entre ces mesures est l'objectif de l'Analyse Discriminante Linéaire.*

Comme montré ci-dessus, **A** est la dispersion intra-classe. **B** est la dispersion inter-classe.

#### Comment cela fonctionne-t-il ?

Générons un ensemble de données simple pour cet exemple (pour le R-fiddle, [cliquez ici](http://www.r-fiddle.org/#/fiddle?id=VAoodF2P&version=2)).

```r
require(dplyr)
languages <- data.frame(
  HTML = c(22,20,15, 5, 5, 5, 0, 2, 0),
  JavaScript = c(20,25,25,20,20,15, 5, 5, 0),
  Java = c(15, 5, 0,15,30,30,10,10,15),
  Python = c( 5, 0, 2, 5,10, 5,40,35,30),
  job = c("Web","Web","Web","App","App","App","Data","Data","Data")
  )

View(languages)
```

Nous avons un ensemble de données fictif décrivant neuf développeurs en termes du nombre d'heures qu'ils passent à travailler dans chacun des quatre langages :

* HTML
* JavaScript
* Java
* Python

Chaque développeur est classé dans l'un des trois rôles de travail :

* développeur web
* développeur d'applications
* et scientifique des données

```r
cor(select(languages, -job))
```

Nous utilisons la fonction `select()` du package `dplyr` pour supprimer les étiquettes de classe de l'ensemble de données. Cela nous permet d'inspecter les corrélations entre les différents langages.

Sans surprise, nous voyons certains schémas. Il y a une forte corrélation positive entre HTML et JavaScript. Cela indique que les développeurs qui utilisent l'un de ces langages ont tendance à utiliser également l'autre.

Nous soupçonnons qu'il y a une structure de dimension inférieure sous cette ensemble de données en 4D. Rappelez-vous, quatre langages = quatre dimensions.

Utilisons LDA pour projeter nos données dans un espace de dimension inférieure qui sépare le mieux les trois classes de rôles de travail.

Tout d'abord, nous devons construire des matrices de dispersion **intra-classe** pour chaque classe. Utilisons les méthodes `filter()` et `select()` de `dplyr` pour décomposer nos données par rôle de travail.

```r
Web <- as.data.frame(
  scale(filter(languages, job == "Web") %>% 
    select(., -job),T))

App <- as.data.frame(
  scale(filter(languages, job == "App") %>%
    select(., -job),T))

Data <- as.data.frame(
  scale(filter(languages, job == "Data") %>%
    select(., -job),T))
```

Nous avons maintenant trois nouveaux ensembles de données, un pour chaque rôle de travail. Pour chacun d'eux, nous pouvons trouver une [matrice de covariance](https://en.wikipedia.org/wiki/Covariance_matrix). Cela est étroitement lié à la matrice de corrélation. Elle décrit également les tendances entre l'utilisation des langages.

Nous trouvons la matrice de dispersion intra-classe en additionnant chacune des trois matrices de covariance. Cela nous donne une matrice décrivant la dispersion au sein de chaque classe.

```r
within <- cov(Web) + cov(App) + cov(Data)
```

Maintenant, nous voulons trouver la matrice de dispersion inter-classe qui décrit la dispersion entre les classes. Pour ce faire, nous devons d'abord trouver le centre de chaque classe, en calculant les caractéristiques moyennes de chacune. Cela nous permet de former un `data.frame` où chaque colonne décrit le développeur moyen pour chaque classe.

```r
means <- t(data.frame(
  mean_Web <- sapply(Web, mean),
  mean_App <- sapply(App, mean),
  mean_Data <- sapply(Data, mean)))
```

Pour obtenir notre matrice de dispersion inter-classe, nous trouvons la covariance de cette matrice. :

```r
between <- cov(means)
```

Maintenant, nous avons deux matrices :

* notre matrice de dispersion intra-classe
* la matrice de dispersion inter-classe

Nous voulons trouver de nouveaux axes pour nos données qui minimisent le rapport entre la dispersion intra-classe et la dispersion inter-classe.

Nous faisons cela en trouvant les vecteurs propres de la matrice formée par :

![Image](https://cdn-media-1.freecodecamp.org/images/mEoUFYKZGkE2YMQ0i43YUdQKwC3GalUzWcB1)
*Nous multiplions l'inverse de la matrice de dispersion intra-classe SW par la matrice de dispersion inter-classe SB*

```r
e <- eigen(solve(within) %*% between)

barplot(e$values/sum(e$values),
  main='Variance expliquée')
  
W <- e$vectors[,1:2]
```

En traçant les valeurs propres, nous pouvons voir que les deux premiers vecteurs propres expliqueront plus de 95 % de la variation dans les données.

Transformons l'ensemble de données original et traçons les données dans son nouvel espace de dimension inférieure.

```r
LDA <- scale(select(languages, -job), T) %*% W
  
plot(LDA, pch="", 
  main='Analyse Discriminante Linéaire')

text(LDA[,1],LDA[,2],cex=0.75,languages$job,
  col=unlist(lapply(c(2,3,4),rep, 3)))
```

![Image](https://cdn-media-1.freecodecamp.org/images/gAR88rTA1WHtI0IeQqVnEHgNY4Nlgs0Jqszv)
*Ces axes semblent séparer les classes*

Et voilà ! Voyez comment les nouveaux axes font un travail incroyable en séparant les différentes classes ? Cela réduit la dimensionnalité des données et pourrait également s'avérer utile à des fins de classification.

Pour commencer à interpréter les nouveaux axes, nous pouvons les corrélier avec les données originales :

```r
cor(select(languages,-job),LDA)
```

Cela révèle comment l'Axe 1 est négativement corrélé avec JavaScript et HTML, et positivement corrélé avec Python. Cet axe sépare les Data Scientists des développeurs Web et App.

L'Axe 2 est corrélé avec HTML et Java dans des directions opposées. Cela sépare les développeurs Web des développeurs App. Ce serait une information intéressante, si les données n'étaient pas fictives...

Nous avons supposé que les trois classes sont toutes de taille égale, ce qui simplifie un peu les choses. LDA peut être appliqué à 2 classes ou plus, et peut être utilisé comme méthode de classification également.

Obtenez [l'image complète](https://www.isip.piconepress.com/publications/reports/1998/isip/lda/lda_theory.pdf) et la couverture de l'utilisation de LDA dans la classification.

### Réduction de dimensionnalité non linéaire

Les techniques couvertes jusqu'à présent sont assez bonnes dans de nombreux cas d'utilisation, mais elles font une hypothèse clé : que nous travaillons dans le contexte de la géométrie linéaire.

Parfois, c'est une hypothèse que nous devons abandonner.

La réduction de dimensionnalité non linéaire (NLDR) ouvre un monde fascinant de mathématiques avancées et de possibilités déroutantes dans des applications telles que la vision par ordinateur et l'autonomie.

Il existe de nombreuses méthodes NLDR disponibles. Nous allons examiner quelques techniques liées à l'**apprentissage de variétés**. Celles-ci approximeront la structure sous-jacente des données de haute dimension. Les [variétés](http://mathworld.wolfram.com/Manifold.html) sont l'un des nombreux concepts mathématiques qui peuvent sembler impénétrables mais qui sont en réalité vus tous les jours.

Prenez cette carte du monde :

![Image](https://cdn-media-1.freecodecamp.org/images/08-xLkvanFMueroIHTGaqZOfYdy0u3zrG2UF)
*Strictement parlant, la surface d'une sphère nécessite une carte de chaque hémisphère pour être correctement cartographiée...

Nous sommes tous à l'aise avec l'idée de représenter la surface d'une sphère sur une feuille de papier plate. Rappelez-vous que précédemment, une sphère est **définie** comme une surface 2D tracée à une distance fixe autour d'un point dans un espace 3D. La surface de la Terre est une variété 2D intégrée, ou enveloppée, dans un espace 3D.

Avec des données de haute dimension, nous pouvons utiliser le concept de variétés pour réduire le nombre de dimensions nécessaires pour décrire les données.

Pensez à la surface de la Terre. La Terre existe dans un espace 3D, donc nous devrions décrire l'emplacement, comme une ville, en trois dimensions. Cependant, nous n'avons aucun problème à utiliser seulement deux dimensions de latitude et de longitude à la place.

Les variétés peuvent être plus complexes et de dimension supérieure à l'exemple de la Terre ici. **Isomap** et **Laplacian Eigenmapping** sont deux méthodes étroitement liées utilisées pour appliquer cette réflexion aux données de haute dimension.

### Isomap

#### Résumé Visuel

![Image](https://cdn-media-1.freecodecamp.org/images/kjipj65OIbmyAH8KH9KXPjyRp7SpejKELU2-)

Nous pouvons voir nos données originales comme une structure sous-jacente en forme de U. La distance en ligne droite, comme le montre la flèche noire, entre **A** et **B** ne reflétera pas le fait qu'ils se trouvent à des extrémités opposées, comme le montre la ligne rouge.

Nous pouvons construire un graphe des plus proches voisins pour trouver le chemin le plus court entre les points. Cela nous permet de construire une matrice de distance qui peut être utilisée comme entrée pour MDS afin de trouver une représentation de dimension inférieure des données originales qui préserve la structure non linéaire.

Nous pouvons approximer les distances sur la variété en utilisant des techniques de théorie des graphes. Nous pouvons le faire en construisant un [graphe](http://barabasi.com/networksciencebook/) ou un réseau en connectant chacun de nos points de données originaux à un ensemble de points voisins.

En utilisant un algorithme de plus courts chemins, nous pouvons trouver la distance **géodésique** entre chaque point. Nous pouvons utiliser cela pour former une matrice de distance qui peut être une entrée pour une méthode de réduction de dimensionnalité linéaire.

#### Exemple détaillé

Nous allons implémenter un algorithme Isomap simple en utilisant un ensemble de données généré artificiellement. Nous garderons les choses en basse dimension, pour aider à visualiser ce qui se passe. [Voici le code](https://gist.github.com/anonymous/fa6bd23c09d488e3943f9cef86a3e352).

Commençons par générer quelques données :

```r
x <- y <- c(); a <- b <- 1

for(i in 1:1000){
  theta <- 0.01 * i
  x <- append(x,(a+b*theta)*(cos(theta)+runif(1,-1,1))
  y <- append(y,(a+b*theta)*(sin(theta)+runif(1,-1,1))
}

color <- rainbow(1200)[1:1000]
spiral <- data.frame(x,y,color)
plot(y~x, pch=20, col=color)
```

![Image](https://cdn-media-1.freecodecamp.org/images/yRLu437frkwxfF8Tf1O12WMbC34pafY1pbBO)
*Les points A et B sont à des extrémités opposées de la spirale. La distance en ligne droite entre eux ne reflète pas cela.*

Bien ! C'est une forme intéressante, avec une structure non linéaire claire. Nos données pourraient être vues comme dispersées le long d'une ligne 1D, courant entre le rouge et le violet, enroulée (ou **intégrée**) dans un espace 2D. Sous l'hypothèse de linéarité, les métriques de distance et autres techniques statistiques n'en tiendront pas compte.

Comment pouvons-nous démêler les données pour trouver leur structure sous-jacente 1D ?

```r
pc <- prcomp(spiral[,1:2])
plot(data.frame(
  pc$x[,1],1),col=as.character(spiral$color))
```

![Image](https://cdn-media-1.freecodecamp.org/images/wYe1pKEIsRqz-WjLUdeUtCmpB8VQNnS9EXUb)
*L'ACP nous déçoit ici. La ligne ne va pas du rouge au violet.*

L'ACP ne nous aidera pas, car c'est une technique de réduction de dimensionnalité **linéaire**. Voyez comment elle a effondré tous les points sur un axe traversant la spirale ? Au lieu de révéler le spectre sous-jacent rouge-violet des points, nous ne voyons que les points bleus dispersés le long de l'axe entier.

Essayons d'implémenter un algorithme Isomap. Nous commençons par construire un graphe à partir de nos points de données, en connectant chacun à ses _n_ points voisins les plus proches. _n_ est un **hyper-paramètre** que nous devons définir avant d'exécuter l'algorithme. Pour l'instant, utilisons _n_ = 5.

Nous pouvons représenter le graphe des _n_ plus proches voisins comme une [matrice d'adjacence](https://en.wikipedia.org/wiki/Adjacency_matrix) **A**.

L'élément à l'intersection de chaque ligne et colonne peut être soit 1 soit 0 selon que les points correspondants sont connectés ou non.

Construisons cela avec le code ci-dessous :

```r
n <- 5
distance <- as.matrix(dist(spiral[,1:2]))
A <- matrix(0,ncol=ncol(distance),nrow=nrow(distance))

for(i in 1:nrow(A)){
  neighbours <- as.integer(
    names(sort(distance[i,])[2:n+1]))
  A[i,neighbours] <- 1
}
```

Maintenant que nous avons notre graphe des _n_ plus proches voisins, nous pouvons commencer à travailler avec les données de manière non linéaire. Par exemple, nous pouvons commencer à approximer les distances entre les points sur la spirale en trouvant leur distance **géodésique** — en calculant la longueur du chemin le plus court entre eux.

L'[algorithme de Dijkstra](https://www.cs.usfca.edu/~galles/visualization/Dijkstra.html) est un algorithme célèbre qui peut être utilisé pour trouver le chemin le plus court entre deux points dans un graphe connecté. Nous pourrions implémenter notre propre version ici, mais pour rester sur le sujet, j'utiliserai la fonction `distances()` de la [bibliothèque igraph de R](http://igraph.org/).

```r
install.packages('igraph'); require(igraph)

graph <- graph_from_adjacency_matrix(A)
geo <- distances(graph, algorithm = 'dijkstra')
```

Cela nous donne une matrice de distance. Chaque élément représente le nombre minimal d'arêtes ou de liens nécessaires pour aller d'un point à un autre.

Voici une idée... pourquoi ne pas utiliser MDS pour trouver quelques coordonnées pour les points représentés dans cette matrice de distance ? Cela a fonctionné plus tôt pour les données des villes.

Nous pourrions envelopper notre exemple MDS précédent dans une fonction et appliquer notre propre version maison. Cependant, vous serez ravis de savoir que R fournit une fonction MDS intégrée que nous pouvons utiliser également. Réduisons à une dimension.

```r
md <- data.frame(
  'scaled'=cmdscale(geo,1),
  'color'=spiral$color)

plot(data.frame(
  md$scaled,1), col=as.character(md$color), pch=20)
```

![Image](https://cdn-media-1.freecodecamp.org/images/fBbRSNXu7Ew61cNiNnTjvYzwaUCklqMLIuG6)
*Nous y voilà — nous avons démêlé la spirale et préservé sa structure locale*

Nous avons réduit de 2D à 1D, sans ignorer la structure sous-jacente de la variété.

Pour des applications avancées d'apprentissage automatique non linéaire, c'est une grande avancée. Souvent, les données de haute dimension résultent d'un processus génératif de dimension inférieure. Notre exemple de spirale illustre cela.

La spirale originale a été tracée comme un `data.frame` de coordonnées _x_ et _y_. Mais nous avons généré celles-ci avec une boucle for, dans laquelle notre variable d'index `i` s'incrémentait de +1 à chaque itération.

En appliquant notre algorithme Isomap, nous avons recapitulé l'augmentation régulière de `i` à chaque itération de la boucle. Plutôt bien fait.

La version de Isomap que nous avons implémentée ici a été un peu simplifiée dans certaines parties. Par exemple, nous aurions pu pondérer notre matrice d'adjacence pour tenir compte des distances euclidiennes entre les points. Cela nous aurait donné une mesure plus nuancée de la distance géodésique.

Un inconvénient des méthodes comme celle-ci est la nécessité d'établir des valeurs de paramètres hyper appropriées. Si le seuil des plus proches voisins _n_ est trop bas, vous vous retrouverez avec un graphe fragmenté. S'il est trop élevé, l'algorithme sera insensible aux détails. Cette spirale pourrait devenir une ellipse si nous commençons à connecter des points sur différentes couches.

Cela signifie que ces méthodes fonctionnent mieux avec des données denses. Cela nécessite que la structure de la variété soit assez bien définie en premier lieu.

### Laplacian Eigenmapping

#### Résumé Visuel

![Image](https://cdn-media-1.freecodecamp.org/images/UnSWPMJbDrUu0sxFLWgg0gKAmNiWbuczx5tT)
*Comme avec Isomap, nous pouvons produire un graphe (ou réseau) de points voisins.*

En utilisant des idées de la Théorie Spectrale des Graphes, nous pouvons trouver une projection de dimension inférieure des données tout en conservant la structure non linéaire.

Encore une fois, nous pouvons approximer les distances sur la variété en utilisant des techniques de théorie des graphes. Nous pouvons le faire en construisant un graphe reliant chacun de nos points de données originaux à un ensemble de points voisins.

Laplacian Eigenmapping prend ce graphe et applique des idées de la théorie spectrale des graphes pour trouver un plongement de dimension inférieure des données originales.

#### Exemple détaillé

D'accord, vous avez réussi jusqu'ici. Votre récompense est la chance de vous plonger dans notre quatrième et dernier algorithme de réduction de dimensionnalité. Nous explorerons une autre technique non linéaire. Comme Isomap, elle utilise la théorie des graphes pour approximer la structure sous-jacente de la variété. [Consultez le code](https://gist.github.com/anonymous/4ac616cfd0b7e7dbee31e713826e075d).

Commençons avec des données en forme de spirale similaires à celles que nous avons utilisées auparavant. Mais rendons-la encore plus serrée.

```r
set.seed(100)

x <- y <- c();
a <- b <- 1

for(i in 1:1000){
  theta <- 0.02 * i
  x <- append(x,(a+b*theta)*(cos(theta)+runif(1,-1,1))
  y <- append(y,(a+b*theta)*(sin(theta)+runif(1,-1,1))
}

color <- rainbow(1200)[1:1000]
spiral <- data.frame(x,y,color)
plot(y~x, pch=20, col=color)
```

![Image](https://cdn-media-1.freecodecamp.org/images/Zf49fVR1ukuzkqLAr4aJ8kSF4nNsm14QpGAp)
*La distance en ligne droite entre A et B est beaucoup plus courte que la distance d'une extrémité de la spirale à l'autre.*

La distance naïve en ligne droite entre A et B est beaucoup plus courte que la distance d'une extrémité de la spirale à l'autre. Les techniques linéaires n'auront aucune chance !

Encore une fois, nous commençons par construire la matrice d'adjacence **A** d'un graphe des _n_ plus proches voisins. _n_ est un hyper-paramètre que nous devons choisir à l'avance.

Essayons _n_ = 10 :

```r
n <- 10
distance <- as.matrix(dist(spiral[,1:2]))
A <- matrix(0,ncol=ncol(distance),
  nrow=nrow(distance))

for(i in 1:nrow(A)){
  neighbours <- as.integer(
    names(sort(distance[i,])[2:n+1]))
  A[i,neighbours] <- 1
}

for(j in 1:nrow(A)){
  for(k in 1:ncol(A)){
    if(A[j,k] == 1){
      out[k,j] <- 1
    }
  }
}
```

Jusqu'à présent, c'est beaucoup comme Isomap. Nous avons ajouté quelques lignes de logique supplémentaires pour forcer la matrice à être symétrique. Cela nous permettra d'utiliser des idées de la [théorie spectrale des graphes](http://web.cs.ucdavis.edu/~bai/ECS231/ho_clustering.pdf) dans l'étape suivante. Nous allons définir la [matrice laplacienne](http://mathworld.wolfram.com/LaplacianMatrix.html) de notre graphe.

Nous faisons cela en construisant la matrice de degré **D**.

```r
D <- diag(nrow(A))

for(i in 1:nrow(D)){   
  D[i,i] = sum(A[,i])
}
```

C'est une matrice de la même taille que **A**, où chaque élément est égal à zéro — sauf ceux sur la diagonale, qui sont égaux à la somme de la colonne correspondante de la matrice **A**.

Ensuite, nous formons la matrice laplacienne **L** avec la simple soustraction :

```r
L = D - A
```

La matrice laplacienne est une autre représentation matricielle de notre graphe particulièrement adaptée à l'algèbre linéaire. Elle nous permet de calculer toute une gamme de propriétés intéressantes.

Pour trouver notre plongement en 1D des données originales, nous devons trouver un vecteur _x_ et une valeur propre λ.

Cela résoudra le [problème généralisé des valeurs propres](https://en.wikipedia.org/wiki/Eigendecomposition_of_a_matrix#Generalized_eigenvalue_problem) :

`**L**_x_ = λ**D**_x_`

Heureusement, vous pouvez ranger le crayon et le papier, car R fournit un package pour nous aider à faire cela.

```r
install.packages('geigen'); require(geigen)
eig <- geigen(L,D)
eig$values[1:10]
```

Nous voyons que la fonction `geigen()` a retourné les solutions de valeurs propres du plus petit au plus grand. Notez comment la première valeur est pratiquement nulle.

C'est l'une des propriétés de la matrice laplacienne — son nombre de valeurs propres nulles nous indique combien de composantes connectées nous avons dans le graphe. Si nous avions utilisé une valeur plus faible pour _n_, nous aurions pu construire un graphe fragmenté en, disons, trois parties séparées et non connectées — dans ce cas, nous aurions trouvé trois valeurs propres nulles.

Pour trouver notre plongement de faible dimension, nous pouvons prendre les vecteurs propres associés aux valeurs propres non nulles les plus basses. Puisque nous projetons de 2D en 1D, nous n'aurons besoin que d'un tel vecteur propre.

```r
embedding <- eig$vectors[,2]
plot(data.frame(embedding,1), col=spiral$colors, pch=20)
```

![Image](https://cdn-media-1.freecodecamp.org/images/ZJQmnnUPYQjnkVzgsb1VuezIIDXO-i39iSOB)
*Nous avons même révélé les mêmes « écarts » que nous avons vus dans la représentation originale en 2D !*

Et voilà — un autre ensemble de données non linéaires intégré avec succès dans des dimensions inférieures. Parfait !

Nous avons implémenté une version simplifiée de Laplacian Eigenmapping. Nous avons ignoré le choix d'un autre hyper-paramètre _t_, qui aurait eu pour effet de pondérer notre graphe des plus proches voisins.

Jetez un coup d'œil à [l'article original](http://web.cse.ohio-state.edu/~belkin.8/papers/LEM_NIPS_01.pdf) pour les détails complets et la justification mathématique.

### Conclusion

Nous y voilà — un aperçu de quatre techniques de réduction de dimensionnalité que nous pouvons appliquer aux données linéaires et non linéaires. Ne vous inquiétez pas si vous n'avez pas tout suivi des mathématiques (bien que félicitations si vous l'avez fait !). Rappelez-vous, nous devons toujours trouver un équilibre entre théorie et pratique en matière de science des données.

Ces algorithmes et plusieurs autres sont disponibles dans divers packages de [R](https://www.r-project.org/), et dans [scikit-learn](http://scikit-learn.org/stable/) pour Python.

Pourquoi, alors, avons-nous passé en revue chacun d'eux étape par étape ? Selon mon expérience, reconstruire quelque chose à partir de zéro est un excellent moyen de comprendre comment cela fonctionne.

La réduction de dimensionnalité touche plusieurs branches des mathématiques qui sont utiles dans la science des données et d'autres disciplines. Mettre ces concepts en pratique est un excellent exercice pour transformer la théorie en application.

Il existe, bien sûr, d'autres techniques que nous n'avons pas couvertes. Mais si vous avez encore un appétit pour plus d'apprentissage automatique, alors essayez les liens ci-dessous :

Techniques linéaires :

* [Analyse en Composantes Indépendantes](http://www.mit.edu/~gari/teaching/6.555/LECTURE_NOTES/ch15_bss.pdf)
* [Analyse Factorielle](https://en.wikipedia.org/wiki/Factor_analysis)

Non linéaires :

* [Plongement Localement Linéaire](http://science.sciencemag.org/content/290/5500/2323)
* [Autoencodeurs](http://proceedings.mlr.press/v27/baldi12a/baldi12a.pdf)
* [t-SNE](https://distill.pub/2016/misread-tsne/)

Merci d'avoir lu ! Si vous avez des commentaires ou des questions, veuillez laisser une réponse ci-dessous !