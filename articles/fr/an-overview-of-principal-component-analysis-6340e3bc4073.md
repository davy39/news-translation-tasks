---
title: Aperçu de l'Analyse en Composantes Principales
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-01T16:12:23.000Z'
originalURL: https://freecodecamp.org/news/an-overview-of-principal-component-analysis-6340e3bc4073
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ldDA-9rCN_gG3qaMzIA6fA.png
tags:
- name: algorithms
  slug: algorithms
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: statistics
  slug: statistics
- name: 'tech '
  slug: tech
seo_title: Aperçu de l'Analyse en Composantes Principales
seo_desc: 'By Moshe Binieli

  This article will explain you what Principal Component Analysis (PCA) is, why we
  need it and how we use it. I will try to make it as simple as possible while avoiding
  hard examples or words which can cause a headache.

  A moment of hon...'
---

Par Moshe Binieli

Cet article vous expliquera ce qu'est l'Analyse en Composantes Principales (ACP), pourquoi nous en avons besoin et comment nous l'utilisons. Je vais essayer de le rendre aussi simple que possible tout en évitant les exemples ou les mots difficiles qui pourraient causer un mal de tête.

Un moment d'honnêteté : pour comprendre pleinement cet article, une compréhension de base de certaines notions d'algèbre linéaire et de statistiques est essentielle. Prenez quelques minutes pour réviser les sujets suivants, si nécessaire, afin de faciliter la compréhension de l'ACP :

* vecteurs
* vecteurs propres
* valeurs propres
* variance
* covariance

### **Comment cet algorithme peut-il nous aider ? Quelles sont les utilisations de cet algorithme ?**

* Identifie les directions les plus pertinentes de la variance dans les données.
* Aide à capturer les caractéristiques les plus "importantes".
* Plus facile à effectuer des calculs sur le jeu de données après la réduction de dimension puisque nous avons moins de données à traiter.
* Visualisation des données.

### Explication verbale courte.

Supposons que nous avons 10 variables dans notre jeu de données et supposons que 3 variables capturent 90 % du jeu de données, et 7 variables capturent 10 % du jeu de données.

Supposons que nous voulons visualiser 10 variables. Bien sûr, nous ne pouvons pas faire cela, nous pouvons visualiser seulement un maximum de 3 variables (peut-être qu'à l'avenir nous pourrons en faire plus).

Nous avons donc un problème : nous ne savons pas quelles variables capturent la plus grande variabilité dans nos données. Pour résoudre ce mystère, nous appliquerons l'algorithme ACP. Le résultat nous dira quelles sont ces variables. Cela semble cool, n'est-ce pas ? 😉

### **Quelles sont les étapes pour faire fonctionner l'ACP ? Comment appliquons-nous la magie ?**

1. Prenez le jeu de données sur lequel vous voulez appliquer l'algorithme.
2. Calculez la matrice de covariance.
3. Calculez les vecteurs propres et leurs valeurs propres.
4. Triez les vecteurs propres selon leurs valeurs propres par ordre décroissant.
5. Choisissez les premiers K vecteurs propres (où k est la dimension à laquelle nous voulons aboutir).
6. Construisez un nouveau jeu de données réduit.

### Temps pour un exemple avec des données réelles.

#### 1) **Charger le jeu de données dans une matrice :**

Notre **objectif principal** est de déterminer combien de variables sont les plus importantes pour nous et de rester uniquement avec elles.

Pour cet exemple, nous utiliserons le programme "Spyder" pour exécuter Python. Nous utiliserons également un jeu de données assez cool qui est intégré dans "sklearn.datasets" et qui s'appelle "load_iris". Vous pouvez en lire plus sur ce jeu de données sur [Wikipedia](https://en.wikipedia.org/wiki/Iris_flower_data_set).

Tout d'abord, nous allons charger le module iris et transformer le jeu de données en une matrice. Le jeu de données contient 4 variables avec 150 exemples. Par conséquent, la dimensionnalité de notre matrice de données est : (150, 4).

```
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
```

```
irisModule = load_iris()
dataset = np.array(irisModule.data)
```

![Image](https://cdn-media-1.freecodecamp.org/images/YXHqyLU0LAHkble6hyDqeSipKK3p3QoIC8cC)
_Visualisation du jeu de données_

Il y a plus de lignes dans ce jeu de données — comme nous l'avons dit, il y a 150 lignes, mais nous ne pouvons en voir que 17.

Le concept de l'ACP est de réduire la dimensionnalité de la matrice en trouvant les directions qui capturent la plupart de la variabilité dans notre matrice de données. Par conséquent, nous aimerions les trouver.

#### 2) **Calculer la matrice de covariance :**

Il est temps de calculer la matrice de covariance de notre jeu de données, mais que signifie cela ? Pourquoi devons-nous calculer la matrice de covariance ? À quoi ressemblera-t-elle ?

La **[variance](https://en.wikipedia.org/wiki/Variance)** est l'espérance de l'écart quadratique d'une variable aléatoire par rapport à sa moyenne. Informellement, **elle mesure l'étalement d'un ensemble de nombres par rapport à leur moyenne.** La définition mathématique est :

![Image](https://cdn-media-1.freecodecamp.org/images/K52ek3Wc1IDyzQI3rWZcpqH3XoMVpp2452jY)

La **[covariance](https://en.wikipedia.org/wiki/Covariance)** est une mesure de la variabilité conjointe de deux variables aléatoires. En d'autres termes, comment deux caractéristiques varient l'une par rapport à l'autre. L'utilisation de la covariance est très courante lors de la recherche de motifs dans les données. La définition mathématique est :

![Image](https://cdn-media-1.freecodecamp.org/images/VP34PkFzIJfNHFEreKfU4KXmCjUePqm6ERtz)

À partir de cette définition, nous pouvons conclure que la matrice de covariance sera symétrique. Cela est important car cela signifie que ses vecteurs propres seront réels et non négatifs, ce qui nous facilite la tâche (nous vous mettons au défi de prétendre que travailler avec des nombres complexes est plus facile qu'avec des nombres réels !)

Après avoir calculé la matrice de covariance, elle ressemblera à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/aTBSknE6DhtopHBN23kDC-E4e5bCWf-mVLIV)
_Visualisation de la matrice de covariance_

Comme vous pouvez le voir, la diagonale principale est écrite comme **V** (variance) et le reste est écrit comme **C** (covariance), pourquoi cela ?

Parce que le calcul de la covariance de la même variable revient essentiellement à calculer sa variance (si vous n'êtes pas sûr pourquoi — prenez quelques minutes pour comprendre ce que sont la variance et la covariance).

Calculons en Python la matrice de covariance du jeu de données en utilisant le code suivant :

```
covarianceMatrix = pd.DataFrame(data = np.cov(dataset, rowvar = False), columns = irisModule.feature_names, index = irisModule.feature_names)
```

![Image](https://cdn-media-1.freecodecamp.org/images/4wUPiNCggyBdEZOjoqfTDvOpIqaqdBREVOMy)
_La matrice de covariance du jeu de données_

* Nous ne nous intéressons pas à la diagonale principale, car ce sont les variances de la même variable. Puisque nous essayons de trouver de nouveaux motifs dans le jeu de données, **nous ignorerons la diagonale principale.**
* Puisque la matrice est symétrique, covariance(a,b) = covariance(b,a), **nous ne regarderons que les valeurs supérieures de la matrice de covariance (au-dessus de la diagonale).**
Une chose importante à mentionner sur la covariance : si la covariance des variables **a** et **b** est **positive**, cela signifie qu'elles **varient dans la même direction.** Si la covariance de **a** et **b** est **négative**, elles varient dans des **directions différentes.**

#### 3) **Calculer les valeurs propres et les vecteurs propres :**

Comme je l'ai mentionné au début, les valeurs propres et les vecteurs propres sont les termes de base que vous devez connaître pour comprendre cette étape. Par conséquent, je ne vais pas l'expliquer, mais plutôt passer à leur calcul.

Le vecteur propre associé à la plus grande valeur propre indique la direction dans laquelle les données ont le plus de variance. Par conséquent, en utilisant les valeurs propres, nous saurons quels vecteurs propres capturent le plus de variabilité dans nos données.

```
eigenvalues, eigenvectors = np.linalg.eig(covarianceMatrix)
```

Voici le vecteur des valeurs propres, le premier index du vecteur des valeurs propres est associé au premier index de la matrice des vecteurs propres.

Les valeurs propres :

![Image](https://cdn-media-1.freecodecamp.org/images/HEXQgmvpNE7PxzuxIwjkI2bXAlBHFp2JwrMH)
_Valores propres de la matrice de covariance_

La matrice des vecteurs propres :

![Image](https://cdn-media-1.freecodecamp.org/images/7wEPUqxyvzXKBBxVtZnm6CicuKfqg6StG9x1)
_Matrice des vecteurs propres de la matrice de covariance_

#### 4) Choisir les premières K valeurs propres (K composantes principales/axes) :

Les valeurs propres nous indiquent la quantité de variabilité dans la direction de son vecteur propre correspondant. Par conséquent, le vecteur propre avec la plus grande valeur propre est la direction avec le plus de variabilité. Nous appelons ce vecteur propre la première composante principale (ou axe). Selon cette logique, le vecteur propre avec la deuxième plus grande valeur propre sera appelé la deuxième composante principale, et ainsi de suite.

Nous voyons les valeurs suivantes : 
[4.224, 0.242, 0.078, 0.023]

Traduisons ces valeurs en pourcentages et visualisons-les. Nous prendrons le pourcentage que chaque valeur propre couvre dans le jeu de données.

```
totalSum = sum(eigenvalues)
variablesExplained = [(i / totalSum) for i in sorted(eigenvalues, reverse = True)]
```

![Image](https://cdn-media-1.freecodecamp.org/images/jlZXLrss28kt9sfFeJ3zLJm8KKqtZUvE503Q)

Comme vous pouvez clairement le voir, la **première** valeur propre prend **92,5 %** et la **deuxième** prend **5,3 %**, et **la troisième et la quatrième ne couvrent pas beaucoup de données du jeu de données total.** Par conséquent, nous pouvons facilement décider de rester avec seulement **2 variables**, la première et la deuxième.

```
featureVector = eigenvectors[:,:2]
```

Supprimons la troisième et la quatrième variable du jeu de données. Il est important de dire qu'à ce stade, nous perdons certaines informations. Il est impossible de réduire les dimensions sans perdre certaines informations (sous l'hypothèse de position générale). L'algorithme ACP nous indique la bonne façon de réduire les dimensions tout en conservant la quantité maximale d'informations concernant nos données.

Et le jeu de données restant ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/4Smlm09-kewqyLQP4xWDWrIfC4wVXLMjY548)
_Vecteurs propres restants après la suppression de deux variables_

#### 5) **Construire le nouveau jeu de données réduit :**

Nous voulons construire un nouveau jeu de données réduit à partir des K composantes principales choisies.

Nous prendrons les K composantes principales choisies (k=2 ici) qui nous donnent une matrice de taille (4, 2), et nous prendrons le jeu de données original qui est une matrice de taille (150, 4).

![Image](https://cdn-media-1.freecodecamp.org/images/oa-Zyx7jj4ZFVqnOit5TCQge5HtOzRCKEjFq)
_Les matrices avec lesquelles nous devons travailler_

Nous effectuerons une multiplication de matrices de la manière suivante :

* La première matrice que nous prenons est la matrice qui contient les K composantes principales que nous avons choisies et nous transposons cette matrice.
* La deuxième matrice que nous prenons est la matrice originale et nous la transposons.
* À ce stade, nous effectuons une multiplication de matrices entre ces deux matrices.
* Après avoir effectué la multiplication de matrices, nous transposons la matrice résultante.

![Image](https://cdn-media-1.freecodecamp.org/images/KhmpIrq7pfs23am9uSfFkLhY-tD16Fc2PswV)
_Multiplication de matrices_

```
featureVectorTranspose = np.transpose(featureVector)
datasetTranspose = np.transpose(dataset)
newDatasetTranspose = np.matmul(featureVectorTranspose, datasetTranspose)
newDataset = np.transpose(newDatasetTranspose)
```

Après avoir effectué la multiplication des matrices et transposé la matrice résultante, voici les valeurs que nous obtenons pour les nouvelles données qui contiennent uniquement les K composantes principales que nous avons choisies.

![Image](https://cdn-media-1.freecodecamp.org/images/q3R-P6DpdinYG3m6nOFBGLuP49H-ZeCtbfbT)

### Conclusion

Comme (nous l'espérons) vous pouvez maintenant le voir, l'ACP n'est pas si difficile. Nous avons réussi à réduire les dimensions du jeu de données assez facilement en utilisant Python.

Dans notre jeu de données, nous n'avons pas causé d'impact sérieux car nous n'avons supprimé que 2 variables sur 4. Mais supposons que nous avons 200 variables dans notre jeu de données, et que nous avons réduit de 200 variables à 3 variables — cela devient déjà plus significatif.

Espérons que vous avez appris quelque chose de nouveau aujourd'hui. N'hésitez pas à contacter [Chen Shani](https://www.linkedin.com/in/chen-shani-638816184/) ou [Moshe Binieli](https://www.linkedin.com/in/moshe-binieli-22b11a137/) sur LinkedIn pour toute question.