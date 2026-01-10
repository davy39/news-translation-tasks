---
title: 9 algorithmes clés de machine learning expliqués en anglais simple
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-16T17:13:54.000Z'
originalURL: https://freecodecamp.org/news/a-no-code-intro-to-the-9-most-important-machine-learning-algorithms-today
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a3c740569d1a4ca2466.jpg
tags:
- name: algorithms
  slug: algorithms
- name: Machine Learning
  slug: machine-learning
- name: statistics
  slug: statistics
seo_title: 9 algorithmes clés de machine learning expliqués en anglais simple
seo_desc: 'By Nick McCullum

  Machine learning is changing the world. Google uses machine learning to suggest
  search results to users. Netflix uses it to recommend movies for you to watch. Facebook
  uses machine learning to suggest people you may know.

  Machine lea...'
---

Par Nick McCullum

Le [machine learning](https://gum.co/pGjwd) change le monde. Google utilise le machine learning pour suggérer des résultats de recherche aux utilisateurs. Netflix l'utilise pour recommander des films à regarder. Facebook utilise le machine learning pour suggérer des personnes que vous pourriez connaître.

Le machine learning n'a jamais été aussi important. En même temps, comprendre le machine learning est difficile. Le domaine est rempli de jargon. Et le nombre de différents algorithmes de ML augmente chaque année.

Cet article vous présentera les concepts fondamentaux du domaine du machine learning. Plus spécifiquement, nous discuterons des concepts de base derrière les 9 algorithmes de machine learning les plus importants aujourd'hui.

# Systèmes de recommandation

### Qu'est-ce que les systèmes de recommandation ?

Les [systèmes de recommandation](https://nickmccullum.com/python-machine-learning/introduction-recommendation-systems/) sont utilisés pour trouver des entrées similaires dans un ensemble de données.

Peut-être que l'exemple le plus courant dans le monde réel d'un système de recommandation existe à l'intérieur de Netflix. Plus spécifiquement, son service de streaming vidéo recommandera des films et des émissions de télévision suggérés en fonction du contenu que vous avez déjà regardé.

Un autre système de recommandation est la fonction "Personnes que vous pourriez connaître" de Facebook, qui suggère des amis possibles pour vous en fonction de votre liste d'amis existante.

Les systèmes de recommandation entièrement développés et déployés sont extrêmement sophistiqués. Ils sont également très intensifs en ressources.

### Systèmes de recommandation et algèbre linéaire

Les systèmes de recommandation entièrement développés nécessitent une solide formation en algèbre linéaire pour être construits à partir de zéro.

En raison de cela, il peut y avoir des concepts dans cette section que vous ne comprenez pas si vous n'avez jamais étudié l'algèbre linéaire auparavant.

Ne vous inquiétez pas, cependant - la bibliothèque Python scikit-learn rend très facile la construction de systèmes de recommandation. Vous n'avez donc pas besoin d'une grande formation en algèbre linéaire pour construire des systèmes de recommandation réels.

### Comment fonctionnent les systèmes de recommandation ?

Il existe deux principaux types de systèmes de recommandation :

* Systèmes de recommandation basés sur le contenu
* Systèmes de recommandation par filtrage collaboratif

Les systèmes de recommandation basés sur le contenu vous donnent des recommandations basées sur la similarité des éléments que vous avez déjà utilisés. Ils se comportent exactement comme vous vous attendez à ce qu'un système de recommandation se comporte.

Les systèmes de recommandation par filtrage collaboratif produisent des recommandations basées sur la connaissance des interactions de l'utilisateur avec les éléments. En d'autres termes, ils utilisent la sagesse des foules. (D'où le terme "collaboratif" dans son nom.)

Dans le monde réel, les systèmes de recommandation par filtrage collaboratif sont beaucoup plus courants que les systèmes basés sur le contenu. Cela est principalement dû au fait qu'ils donnent généralement de meilleurs résultats. Certains praticiens trouvent également les systèmes de recommandation par filtrage collaboratif plus faciles à comprendre.

Les systèmes de recommandation par filtrage collaboratif ont également une caractéristique unique que les systèmes basés sur le contenu n'ont pas. À savoir, ils ont la capacité d'apprendre des caractéristiques par eux-mêmes.

Cela signifie qu'ils peuvent même commencer à identifier des similarités entre les éléments basées sur des attributs que vous ne leur avez même pas dit de considérer.

Il existe deux sous-catégories au sein du filtrage collaboratif :

* Filtrage collaboratif basé sur la mémoire
* Filtrage collaboratif basé sur les modèles

Vous n'avez pas besoin de connaître les différences entre ces deux types de systèmes de recommandation par filtrage collaboratif pour réussir en machine learning. Il suffit de reconnaître que plusieurs types existent.

### Résumé de la section

Voici un bref résumé de ce que nous avons discuté sur les systèmes de recommandation dans ce tutoriel :

* Exemples de systèmes de recommandation dans le monde réel
* Les différents types de systèmes de recommandation, et comment les systèmes de filtrage collaboratif sont plus couramment utilisés que les systèmes de recommandation basés sur le contenu
* La relation entre les systèmes de recommandation et l'algèbre linéaire

# Régression linéaire

La [régression linéaire](https://nickmccullum.com/python-machine-learning/linear-regression-python/) est utilisée pour prédire certaines valeurs `y` en fonction de la valeur d'un autre ensemble de valeurs `x`.

### L'histoire de la régression linéaire

La régression linéaire a été créée dans les années 1800 par [Francis Galton](https://en.wikipedia.org/wiki/Francis_Galton).

Galton était un scientifique étudiant la relation entre les parents et les enfants. Plus spécifiquement, Galton étudiait la relation entre la taille des pères et la taille de leurs fils.

La première découverte de Galton était que les fils tendaient à être à peu près aussi grands que leurs pères. Cela n'est pas surprenant.

Plus tard, Galton a découvert quelque chose de beaucoup plus intéressant. La taille du fils tendait à être plus proche de la taille moyenne globale de toutes les personnes que de celle de son propre père.

Galton a donné un nom à ce phénomène : la **régression**. Plus précisément, il a dit "La taille du fils d'un père tend à régresser (ou à dériver vers) la taille moyenne (moyenne)".

Cela a conduit à un domaine entier en statistiques et en machine learning appelé régression.

### Les mathématiques de la régression linéaire

Lors de la création d'un modèle de régression, tout ce que nous essayons de faire est de tracer une ligne qui est aussi proche que possible de chaque point dans un ensemble de données.

L'exemple typique de cela est la méthode des "moindres carrés" de la régression linéaire, qui ne calcule que la proximité d'une ligne dans la direction haut-bas.

Voici un exemple pour vous aider à illustrer cela :

![Un exemple des mathématiques derrière la régression des moindres carrés](https://nickmccullum.com/images/python-machine-learning/introduction-linear-regression/least-squares-regression.gif)

Lorsque vous créez un modèle de régression, votre produit final est une équation que vous pouvez utiliser pour prédire la valeur y d'une valeur x, sans connaître la valeur y à l'avance.

# Régression logistique

La [régression logistique](https://nickmccullum.com/python-machine-learning/logistic-regression-python/) est similaire à la régression linéaire sauf qu'au lieu de calculer une valeur numérique `y`, elle estime à quelle catégorie appartient un point de données.

### Qu'est-ce que la régression logistique ?

La régression logistique est un modèle de machine learning utilisé pour résoudre des problèmes de classification.

Voici quelques exemples de problèmes de classification en machine learning :

* E-mails de spam (spam ou non spam ?)
* Réclamations d'assurance automobile (radiation ou réparation ?)
* Diagnostic de maladies

Chacun des problèmes de classification a exactement deux catégories, ce qui en fait des exemples de problèmes de **classification binaire**.

La régression logistique est bien adaptée pour résoudre les problèmes de **classification binaire** - nous attribuons simplement aux différentes catégories une valeur de `0` et `1` respectivement.

Pourquoi avons-nous besoin de la régression logistique ? Parce que vous ne pouvez pas utiliser un modèle de régression linéaire pour faire des prédictions de classification binaire. Cela ne donnerait pas un bon ajustement, puisque vous essayez d'ajuster une ligne droite à travers un ensemble de données avec seulement deux valeurs possibles.

Cette image peut vous aider à comprendre pourquoi les modèles de régression linéaire sont mal adaptés aux problèmes de classification binaire :

![Classification par régression linéaire](https://nickmccullum.com/images/python-machine-learning/introduction-logistic-regression/linear-regression-classification.png)

Dans cette image, l'axe `y` représente la probabilité qu'une tumeur soit maligne. Inversement, la valeur `1-y` représente la probabilité qu'une tumeur ne soit pas maligne. Comme vous pouvez le voir, le modèle de régression linéaire fait un mauvais travail de prédiction de cette probabilité pour la plupart des observations dans l'ensemble de données.

C'est pourquoi les modèles de régression logistique sont utiles. Ils ont une courbe à leur ligne de meilleur ajustement, ce qui les rend beaucoup mieux adaptés pour prédire des données catégorielles.

Voici un exemple qui compare un modèle de régression linéaire à un modèle de régression logistique en utilisant les mêmes données d'entraînement :

![Régression linéaire vs régression logistique](https://nickmccullum.com/images/python-machine-learning/introduction-logistic-regression/linear-vs-logistic-regression.png)

### La fonction sigmoïde

La raison pour laquelle le modèle de régression logistique a une courbe dans sa courbe est qu'il n'est pas calculé en utilisant une équation linéaire. Au lieu de cela, les modèles de régression logistique sont construits en utilisant la fonction sigmoïde (également appelée fonction logistique en raison de son utilisation dans la régression logistique).

Vous n'aurez pas à mémoriser la [fonction sigmoïde](https://en.wikipedia.org/wiki/Sigmoid_function) pour réussir en machine learning. Cela dit, avoir une certaine compréhension de son apparence est utile.

L'équation est montrée ci-dessous :

![L'équation sigmoïde](https://nickmccullum.com/images/python-machine-learning/introduction-logistic-regression/sigmoid-equation.png)

La principale caractéristique de la fonction sigmoïde à comprendre est la suivante : quelle que soit la valeur que vous lui passez, elle générera toujours une sortie comprise entre 0 et 1.

### Utilisation des modèles de régression logistique pour faire des prédictions

Pour utiliser le modèle de régression linéaire pour faire des prédictions, vous devez généralement spécifier un point de coupure. Ce point de coupure est généralement `0,5`.

Utilisons notre exemple de diagnostic de cancer de notre image précédente pour voir ce principe en pratique. Si le modèle de régression logistique produit une valeur inférieure à 0,5, alors le point de données est classé comme une tumeur non maligne. De même, si la fonction sigmoïde produit une valeur supérieure à 0,5, alors la tumeur serait classée comme maligne.

### Utilisation d'une matrice de confusion pour mesurer la performance de la régression logistique

Une matrice de confusion peut être utilisée comme un outil pour comparer les vrais positifs, les vrais négatifs, les faux positifs et les faux négatifs en machine learning.

Les matrices de confusion sont particulièrement utiles lorsqu'elles sont utilisées pour mesurer la performance des modèles de régression logistique. Voici un exemple de la façon dont nous pourrions utiliser une matrice de confusion :

![Un exemple de matrice de confusion](https://nickmccullum.com/images/python-machine-learning/introduction-logistic-regression/confusion-matrix.png)
_Dans ce diagramme, TN signifie "Vrai Négatif" et FN signifie "Faux Négatif". FP signifie "Faux Positif" et TP signifie "Vrai Positif"._

Une matrice de confusion est utile pour évaluer si votre modèle est particulièrement faible dans un quadrant spécifique de la matrice de confusion. Par exemple, il pourrait avoir un nombre anormalement élevé de faux positifs.

Elle peut également être utile dans certaines applications, pour s'assurer que votre modèle fonctionne bien dans une zone particulièrement dangereuse de la matrice de confusion.

Dans cet exemple de cancer, par exemple, vous voudriez être très sûr que votre modèle n'a pas un taux très élevé de faux négatifs, car cela indiquerait que quelqu'un a une tumeur maligne que vous avez incorrectement classée comme non maligne.

### Résumé de la section

Dans cette section, vous avez eu votre première exposition aux modèles de machine learning de régression logistique.

Voici un bref résumé de ce que vous avez appris sur la régression logistique :

* Les types de problèmes de classification qui sont adaptés pour être résolus en utilisant des modèles de régression logistique
* Que la fonction logistique (également appelée fonction sigmoïde) produit toujours une valeur entre 0 et 1
* Comment utiliser des points de coupure pour faire des prédictions en utilisant un modèle de machine learning de régression logistique
* Pourquoi les matrices de confusion sont utiles pour mesurer la performance des modèles de régression logistique

# K-Nearest Neighbors

L'algorithme [K-nearest neighbors](https://nickmccullum.com/python-machine-learning/k-nearest-neighbors-python/) peut vous aider à résoudre des problèmes de classification où il y a plus de deux catégories.

### Qu'est-ce que l'algorithme K-Nearest Neighbors ?

L'algorithme K-nearest neighbors est un algorithme de classification basé sur un principe simple. En fait, le principe est si simple qu'il est mieux compris à travers un exemple.

Imaginez que vous avez des données sur la taille et le poids des joueurs de football et de basketball. L'algorithme K-nearest neighbors peut être utilisé pour prédire si un nouvel athlète est soit un joueur de football soit un joueur de basketball.

Pour ce faire, l'algorithme K-nearest neighbors identifie les `K` points de données qui sont les plus proches de la nouvelle observation.

L'image suivante visualise cela, avec une valeur K de `3` :

![Une visualisation des k plus proches voisins](https://nickmccullum.com/images/python-machine-learning/introduction-k-nearest-neighbors/k-nearest-neighbors.jpg)

Dans cette image, les joueurs de football sont étiquetés comme des points de données bleus et les joueurs de basketball sont étiquetés comme des points orange. Le point de données que nous essayons de classifier est étiqueté en vert.

Puisque la majorité (2 sur 3) des points de données les plus proches des nouveaux points de données sont des joueurs de football bleus, alors l'algorithme K-nearest neighbors prédira que le nouveau point de données est également un joueur de football.

### Les étapes pour construire un algorithme K-Nearest Neighbors

Les étapes générales pour construire un algorithme K-nearest neighbors sont :

1. Stocker toutes les données
2. Calculer la [distance euclidienne](https://en.wikipedia.org/wiki/Euclidean_distance) du nouveau point de données `x` à tous les autres points de l'ensemble de données
3. Trier les points de l'ensemble de données par ordre de distance croissante de `x`
4. Prédire en utilisant la même catégorie que la majorité des `K` points de données les plus proches de `x`

### L'importance de K dans un algorithme K-Nearest Neighbors

Bien que cela ne soit pas évident au départ, changer la valeur de `K` dans un algorithme K-nearest neighbors changera la catégorie à laquelle un nouveau point est assigné.

Plus spécifiquement, avoir une valeur `K` très basse fera en sorte que votre modèle prédise parfaitement vos données d'entraînement et prédise mal vos données de test. De même, avoir une valeur `K` trop élevée rendra votre modèle inutilement complexe.

La visualisation suivante illustre bien cela :

![Valeur K et taux d'erreur](https://nickmccullum.com/images/python-machine-learning/introduction-k-nearest-neighbors/k-value-error-rates.png)

### Les avantages et inconvénients de l'algorithme K-Nearest Neighbors

Pour conclure cette introduction à l'algorithme K-nearest neighbors, je voulais discuter brièvement des avantages et inconvénients de l'utilisation de ce modèle.

Voici quelques avantages principaux de l'algorithme K-nearest neighbors :

* L'algorithme est simple et facile à comprendre
* Il est trivial d'entraîner le modèle sur de nouvelles données d'entraînement
* Il fonctionne avec n'importe quel nombre de catégories dans un problème de classification
* Il est facile d'ajouter plus de données à l'ensemble de données
* Le modèle n'accepte que deux paramètres : `K` et la métrique de distance que vous souhaitez utiliser (généralement la distance euclidienne)

De même, voici quelques-uns des principaux inconvénients de l'algorithme :

* Il y a un coût computationnel élevé pour faire des prédictions, puisque vous devez trier l'ensemble de données
* Il ne fonctionne pas bien avec des caractéristiques catégorielles

### Résumé de la section

Voici un bref résumé de ce que vous venez d'apprendre sur l'algorithme k-nearest neighbors :

* Un exemple de problème de classification (joueurs de football vs joueurs de basketball) que l'algorithme K-nearest neighbors pourrait résoudre
* Comment le K-nearest neighbors utilise la distance euclidienne des points de données voisins pour prédire à quelle catégorie appartient un nouveau point de données
* Pourquoi la valeur de `K` est importante pour faire des prédictions
* Les avantages et inconvénients de l'utilisation de l'algorithme K-nearest neighbors

# Arbres de décision et forêts aléatoires

Les [arbres de décision et forêts aléatoires](https://nickmccullum.com/python-machine-learning/decision-trees-random-forests-python/) sont tous deux des exemples de méthodes d'arbres.

Plus spécifiquement, les arbres de décision sont des modèles de machine learning utilisés pour faire des prédictions en parcourant chaque caractéristique d'un ensemble de données, une par une. Les forêts aléatoires sont des ensembles d'arbres de décision qui utilisent des ordres aléatoires des caractéristiques dans les ensembles de données.

### Qu'est-ce que les méthodes d'arbres ?

Avant de nous plonger dans les fondements théoriques des méthodes d'arbres en machine learning, il est utile de commencer par un exemple.

Imaginez que vous jouez au basketball tous les lundis. De plus, vous invitez toujours le même ami à venir jouer avec vous.

Parfois l'ami vient vraiment. Parfois, ils ne viennent pas.

La décision de venir ou non dépend de nombreux facteurs, comme la météo, la température, le vent et la fatigue. Vous commencez à remarquer ces caractéristiques et commencez à les suivre avec la décision de votre ami de jouer ou non.

Vous pouvez utiliser ces données pour prédire si votre ami viendra jouer au basketball ou non. Une technique que vous pourriez utiliser est un arbre de décision. Voici à quoi ressemblerait cet arbre de décision :

![Un exemple d'un arbre de décision](https://nickmccullum.com/images/python-machine-learning/introduction-decision-tree/decision-tree.png)

Chaque arbre de décision a deux types d'éléments :

* `Nœuds` : emplacements où l'arbre se divise selon la valeur de certains attributs
* `Arêtes` : le résultat d'une division vers le nœud suivant

Vous pouvez voir dans l'image ci-dessus qu'il y a des nœuds pour `perspective`, `humidité` et `vent`. Il y a une arête pour chaque valeur potentielle de chacun de ces attributs.

Voici deux autres termes de l'arbre de décision que vous devriez comprendre avant de continuer :

* `Racine` : le nœud qui effectue la première division
* `Feuilles` : nœuds terminaux qui prédisent le résultat final

Vous avez maintenant une compréhension de base de ce que sont les arbres de décision. Nous apprendrons comment construire des arbres de décision à partir de zéro dans la section suivante.

### Comment construire des arbres de décision à partir de zéro

Construire des arbres de décision est plus difficile que vous ne l'imaginez. Cela est dû au fait que décider quelles caractéristiques diviser vos données (qui est un sujet appartenant aux domaines de l'[Entropie](https://en.wikipedia.org/wiki/Entropy) et du [Gain d'information](https://machinelearningmastery.com/information-gain-and-mutual-information/#:~:text=Information%20gain%20is%20the%20reduction,before%20and%20after%20a%20transformation.)) est un problème mathématiquement complexe.

Pour remédier à cela, les praticiens du machine learning utilisent généralement de nombreux arbres de décision en utilisant un échantillon aléatoire de caractéristiques choisies comme division.

En d'autres termes, un nouvel échantillon aléatoire de caractéristiques est choisi pour chaque arbre à chaque division. Cette technique est appelée **forêts aléatoires**.

En général, les praticiens choisissent généralement la taille de l'échantillon aléatoire de caractéristiques (dénoté `m`) pour être la racine carrée du nombre total de caractéristiques dans l'ensemble de données (dénoté `p`). Pour être concis, `m` est la racine carrée de `p`, puis une caractéristique spécifique est sélectionnée aléatoirement à partir de `m`.

Si cela ne vous semble pas complètement clair pour le moment, ne vous inquiétez pas. Cela sera plus clair lorsque vous construirez finalement votre premier modèle de forêt aléatoire.

### Les avantages de l'utilisation des forêts aléatoires

Imaginez que vous travaillez avec un ensemble de données qui a une caractéristique très forte. En d'autres termes, l'ensemble de données a une caractéristique qui est beaucoup plus prédictive du résultat final que les autres caractéristiques de l'ensemble de données.

Si vous construisez vos arbres de décision manuellement, alors il est logique d'utiliser cette caractéristique comme la première division de l'arbre de décision. Cela signifie que vous aurez plusieurs arbres dont les prédictions sont fortement corrélées.

Nous voulons éviter cela puisque prendre la moyenne de variables fortement corrélées ne réduit pas significativement la variance. En sélectionnant aléatoirement des caractéristiques pour chaque arbre dans une forêt aléatoire, les arbres deviennent décorrélés et la variance du modèle résultant est réduite. Cette décorrélation est le principal avantage de l'utilisation des forêts aléatoires par rapport aux arbres de décision faits à la main.

### Résumé de la section

Voici un bref résumé de ce que vous avez appris sur les arbres de décision et les forêts aléatoires dans cet article :

* Un exemple de problème que vous pourriez prédire en utilisant des arbres de décision
* Les éléments d'un arbre de décision : `nœuds`, `arêtes`, `racines`, et `feuilles`
* Comment prendre des échantillons aléatoires de caractéristiques d'arbres de décision nous permet de construire une forêt aléatoire
* Pourquoi utiliser des forêts aléatoires pour décorrélér les variables peut être utile pour réduire la variance de votre modèle final

# Machines à vecteurs de support

Les [machines à vecteurs de support](https://nickmccullum.com/python-machine-learning/support-vector-machines-python/) sont des algorithmes de classification (bien que, techniquement parlant, ils pourraient également être utilisés pour résoudre des problèmes de régression) qui divisent un ensemble de données en catégories en le divisant par l'écart le plus large entre les catégories. Ce concept sera rendu plus clair à travers des visualisations dans un moment.

### Qu'est-ce que les machines à vecteurs de support ?

Les [machines à vecteurs de support](https://en.wikipedia.org/wiki/Support_vector_machine) - ou SVM pour faire court - sont des modèles de machine learning supervisés avec des algorithmes d'apprentissage associés qui analysent les données et reconnaissent les motifs.

Les machines à vecteurs de support peuvent être utilisées à la fois pour des problèmes de classification et de régression. Dans cet article, nous examinerons spécifiquement l'utilisation des machines à vecteurs de support pour résoudre des problèmes de classification.

### Comment fonctionnent les machines à vecteurs de support ?

Plongeons dans le fonctionnement réel des machines à vecteurs de support.

Étant donné un ensemble d'exemples d'entraînement - chacun d'eux étant marqué pour appartenir à l'une des deux catégories - un algorithme d'entraînement de machine à vecteurs de support construit un modèle. Ce modèle attribue de nouveaux exemples à l'une des deux catégories. Cela fait de la machine à vecteurs de support un classificateur linéaire binaire non probabiliste.

Le SVM utilise la géométrie pour faire des prédictions catégorielles.

Plus spécifiquement, un modèle SVM mappe les points de données comme des points dans l'espace et divise les catégories séparées de sorte qu'elles soient divisées par un écart ouvert qui est aussi large que possible. Les nouveaux points de données sont prédits pour appartenir à une catégorie en fonction du côté de l'écart auquel ils appartiennent.

Voici un exemple de visualisation qui peut vous aider à comprendre l'intuition derrière les machines à vecteurs de support :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-57.png)

Comme vous pouvez le voir, si un nouveau point de données tombe du côté gauche de la ligne verte, il sera étiqueté avec la catégorie rouge. De même, si un nouveau point de données tombe du côté droit de la ligne verte, il sera étiqueté comme appartenant à la catégorie bleue.

Cette ligne verte est appelée un **hyperplan**, qui est un élément important du vocabulaire pour les algorithmes de machines à vecteurs de support.

Prenons un autre exemple de représentation visuelle d'une machine à vecteurs de support :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-58.png)

Dans ce diagramme, l'hyperplan est étiqueté comme l'**hyperplan optimal**. La théorie des machines à vecteurs de support définit l'**hyperplan optimal** comme celui qui maximise la marge entre les points de données les plus proches de chaque catégorie.

Comme vous pouvez le voir, la ligne de marge touche en réalité trois points de données - deux de la catégorie rouge et un de la catégorie bleue. Ces points de données qui touchent les lignes de marge sont appelés **vecteurs de support** et sont à l'origine du nom des machines à vecteurs de support.

### Résumé de la section

Voici un bref résumé de ce que vous venez d'apprendre sur les machines à vecteurs de support :

* Que les machines à vecteurs de support sont un exemple d'algorithme de machine learning supervisé
* Que les machines à vecteurs de support peuvent être utilisées pour résoudre à la fois des problèmes de classification et de régression
* Comment les machines à vecteurs de support catégorisent les points de données en utilisant un **hyperplan** qui maximise la marge entre les catégories dans un ensemble de données
* Que les points de données qui touchent les lignes de marge dans une machine à vecteurs de support sont appelés **vecteurs de support**. Ces points de données sont à l'origine du nom des machines à vecteurs de support.

# Clustering K-Means

Le [clustering K-means](https://nickmccullum.com/python-machine-learning/k-means-clustering-python/) est un algorithme de machine learning qui vous permet d'identifier des segments de données similaires au sein d'un ensemble de données.

### Qu'est-ce que le clustering K-Means ?

Le clustering K-means est un algorithme de machine learning non supervisé.

Cela signifie qu'il prend des données non étiquetées et tentera de regrouper des clusters similaires d'observations ensemble au sein de vos données.

Les algorithmes de clustering K-means sont très utiles pour résoudre des problèmes réels. Voici quelques cas d'utilisation pour ce modèle de machine learning :

* Segmentation des clients pour les équipes marketing
* Classification de documents
* Optimisation des itinéraires de livraison pour des entreprises comme Amazon, UPS ou FedEx
* Identification et réaction aux centres de criminalité au sein d'une ville
* Analyse des sports professionnels
* Prédiction et prévention de la cybercriminalité

L'objectif principal d'un algorithme de clustering K-means est de diviser un ensemble de données en groupes distincts de sorte que les observations au sein de chaque groupe soient similaires les unes aux autres.

Voici une représentation visuelle de ce à quoi cela ressemble en pratique :

![Une visualisation d'un algorithme de clustering K-means](https://nickmccullum.com/images/python-machine-learning/introduction-k-means-clustering/k-means-clustering.png)

Nous explorerons les mathématiques derrière un clustering K-means dans la section suivante de ce tutoriel.

### Comment fonctionnent les algorithmes de clustering K-Means ?

La première étape pour exécuter un algorithme de clustering K-means est de sélectionner le nombre de clusters dans lesquels vous souhaitez diviser vos données. Ce nombre de clusters est la valeur `K` à laquelle il est fait référence dans le nom de l'algorithme.

Choisir la valeur `K` dans un algorithme de clustering K-means est un choix important. Nous parlerons plus tard dans cet article de la façon de choisir une valeur appropriée de `K`.

Ensuite, vous devez attribuer aléatoirement chaque point de votre ensemble de données à un cluster aléatoire. Cela donne notre affectation initiale que vous exécutez ensuite l'itération suivante jusqu'à ce que les clusters cessent de changer :

* Calculer le centroïde de chaque cluster en prenant le vecteur moyen des points au sein de ce cluster
* Réaffecter chaque point de données au cluster qui a le centroïde le plus proche

Voici une animation de la façon dont cela fonctionne en pratique pour un algorithme de clustering K-means avec une valeur `K` de `3`. Vous pouvez voir le centroïde de chaque cluster représenté par un caractère `+` noir.

![Une visualisation d'un algorithme de clustering K-means](https://nickmccullum.com/images/python-machine-learning/introduction-k-means-clustering/k-means-iteration.gif)

Comme vous pouvez le voir, cette itération continue jusqu'à ce que les clusters cessent de changer - ce qui signifie que les points de données ne sont plus affectés à de nouveaux clusters.

### Choisir une valeur K appropriée pour les algorithmes de clustering K-Means

Choisir une valeur `K` appropriée pour un algorithme de clustering K-means est en réalité assez difficile. Il n'y a pas de réponse "correcte" pour choisir la "meilleure" valeur `K`.

Une méthode que les praticiens du machine learning utilisent souvent est appelée **la méthode du coude**.

Pour utiliser la méthode du coude, la première chose que vous devez faire est de calculer la somme des erreurs au carré (SSE) pour votre algorithme de clustering K-means pour un groupe de valeurs `K`. La SSE dans un algorithme de clustering K-means est définie comme la somme de la distance au carré entre chaque point de données dans un cluster et le centroïde de ce cluster.

En tant qu'exemple de cette étape, vous pourriez calculer la SSE pour des valeurs `K` de `2`, `4`, `6`, `8`, et `10`.

Ensuite, vous voudrez générer un graphique de la SSE par rapport à ces différentes valeurs `K`. Vous verrez que l'erreur diminue à mesure que la valeur `K` augmente.

Cela a du sens - plus vous créez de catégories au sein d'un ensemble de données, plus il est probable que chaque point de données soit proche du centre de son cluster spécifique.

Cela dit, l'idée derrière la méthode du coude est de choisir une valeur de `K` à laquelle la SSE ralentit son taux de déclin de manière abrupte. Cette diminution abrupte produit un `coude` dans le graphique.

En tant qu'exemple, voici un graphique de la SSE par rapport à `K`. Dans ce cas, la méthode du coude suggérerait d'utiliser une valeur `K` d'environ `6`.

![Une visualisation d'un algorithme de clustering K-means](https://nickmccullum.com/images/python-machine-learning/introduction-k-means-clustering/elbow-method.png)

Importamment, `6` n'est qu'une estimation pour une bonne valeur de `K` à utiliser. Il n'y a jamais une "meilleure" valeur `K` dans un algorithme de clustering K-means. Comme pour beaucoup de choses dans le domaine du machine learning, il s'agit d'une décision très dépendante de la situation.

### Résumé de la section

Voici un bref résumé de ce que vous avez appris dans cet article :

* Exemples de problèmes de machine learning non supervisés que l'algorithme de clustering K-means est capable de résoudre
* Les principes de base de ce qu'est un algorithme de clustering K-means
* Comment fonctionne l'algorithme de clustering K-means
* Comment utiliser la méthode du coude pour sélectionner une valeur appropriée de `K` dans un modèle de clustering K-means

# Analyse en composantes principales

L'[analyse en composantes principales](https://nickmccullum.com/python-machine-learning/principal-component-analysis-python/) est utilisée pour transformer un ensemble de données à nombreuses caractéristiques en un ensemble de données transformé avec moins de caractéristiques où chaque nouvelle caractéristique est une combinaison linéaire des caractéristiques préexistantes. Cet ensemble de données transformé vise à expliquer la plupart de la variance de l'ensemble de données original avec une simplicité beaucoup plus grande.

### Qu'est-ce que l'analyse en composantes principales ?

L'analyse en composantes principales est une technique de machine learning utilisée pour examiner les interrelations entre des ensembles de variables.

En d'autres termes, l'analyse en composantes principales étudie des ensembles de variables afin d'identifier la structure sous-jacente de ces variables.

L'analyse en composantes principales est parfois appelée **analyse factorielle**.

Sur la base de cette description, vous pourriez penser que l'analyse en composantes principales est assez similaire à la régression linéaire.

Ce n'est pas le cas. En fait, ces deux techniques ont des différences importantes.

### Les différences entre la régression linéaire et l'analyse en composantes principales

La régression linéaire détermine une ligne de meilleur ajustement à travers un ensemble de données. L'analyse en composantes principales détermine plusieurs lignes orthogonales de meilleur ajustement pour l'ensemble de données.

Si vous n'êtes pas familier avec le terme **orthogonal**, cela signifie simplement que les lignes sont à angles droits (90 degrés) l'une par rapport à l'autre - comme le Nord, l'Est, le Sud et l'Ouest sur une carte.

Considérons un exemple pour vous aider à comprendre cela mieux.

![Une analyse en composantes principales](https://nickmccullum.com/images/python-machine-learning/introduction-principal-component-analysis/principal-component-analysis.png)

Jetez un coup d'œil aux étiquettes des axes dans cette image.

Dans cette image, l'axe x des composantes principales explique 73 % de la variance dans l'ensemble de données. L'axe y des composantes principales explique environ 23 % de la variance dans l'ensemble de données.

Cela signifie que 4 % de la variance dans l'ensemble de données reste inexpliquée. Vous pourriez réduire ce nombre davantage en ajoutant plus de composantes principales à votre analyse.

### Résumé de la section

Voici un bref résumé de ce que vous avez appris sur l'analyse en composantes principales dans ce tutoriel :

* Que l'analyse en composantes principales tente de trouver des facteurs orthogonaux qui déterminent la variabilité dans un ensemble de données
* Les différences entre l'analyse en composantes principales et la régression linéaire
* À quoi ressemblent les composantes principales orthogonales lorsqu'elles sont visualisées à l'intérieur d'un ensemble de données
* Que l'ajout de plus de composantes principales peut vous aider à expliquer plus de la variance dans un ensemble de données