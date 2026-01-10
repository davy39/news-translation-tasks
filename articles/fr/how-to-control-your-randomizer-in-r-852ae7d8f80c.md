---
title: Comment contrôler votre générateur de nombres aléatoires en R
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-07T20:10:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-control-your-randomizer-in-r-852ae7d8f80c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*aI6mpoboOmJMKqvEU593xA.png
tags:
- name: Data Science
  slug: data-science
- name: General Programming
  slug: programming
- name: r language
  slug: r-language
- name: sampling
  slug: sampling
- name: statistics
  slug: statistics
seo_title: Comment contrôler votre générateur de nombres aléatoires en R
seo_desc: 'By Michelle Jones

  What happens when you need a particular type of randomization?


  200 random numbers using the normal distribution.

  Overview of random number generation in R

  R has at least 20 random number generator functions. Each uses a specific pr...'
---

Par Michelle Jones

Que se passe-t-il lorsque vous avez besoin d'un type particulier de randomisation ?

![Image](https://cdn-media-1.freecodecamp.org/images/KcZO-yHw1nNM1n8Mnq6gGWolKXhE1UNd3d2z)
_200 nombres aléatoires utilisant la distribution normale._

### Aperçu de la génération de nombres aléatoires en R

[R](https://cran.r-project.org) dispose d'au moins 20 fonctions de génération de nombres aléatoires. Chacune utilise une distribution de probabilité spécifique pour créer les nombres. Toutes nécessitent que vous spécifiiez le nombre de nombres aléatoires que vous souhaitez (l'image ci-dessus montre 200). Toutes sont disponibles dans R de base — aucun package requis.

Les distributions courantes des générateurs de nombres aléatoires sont :

* [normale](http://www.statisticshowto.com/probability-and-statistics/normal-distributions/) (rnorm) : moyenne par défaut de 0 et écart-type de 1
* [binomiale](http://www.statisticshowto.com/probability-and-statistics/binomial-theorem/binomial-distribution-formula/) (rbinom) : pas de valeurs par défaut, spécifiez le nombre d'essais et la probabilité de succès pour chaque essai
* [uniforme](https://www.investopedia.com/terms/u/uniform-distribution.asp) (runif) : valeur minimale par défaut de 0 et valeur maximale de 1

Parmi les trois ci-dessus, seul le générateur de nombres aléatoires binomiaux crée des entiers.

### Pourquoi créer des nombres aléatoires ?

Les problèmes impliquant des nombres aléatoires sont très courants — il y a environ [50 000 questions relatives aux nombres aléatoires](https://stackoverflow.com/search?q=random+numbers) sur Stack Exchange.

Mais pourquoi les utiliser ?

Les nombres aléatoires ont de nombreuses applications pratiques. Ils sont utilisés dans les [simulations de Monte Carlo](http://reference.wolfram.com/language/howto/PerformAMonteCarloSimulation.html). Ils sont utilisés en [cryptographie](https://crypto.stackexchange.com/questions/726/what-is-the-use-of-real-random-number-generators-in-cryptography). Ils ont été utilisés pour produire du contenu [CAPTCHA](https://support.google.com/a/answer/1217728?hl=en). Ils sont utilisés dans les [machines à sous](http://www.casinonewsdaily.com/slots-guide/random-number-generator-hit-frequency-vs-payout-ratio/). Ils ont également été utilisés pour des tâches plus mundanes telles que la création d'un ordre de tri aléatoire pour un tableau de données ordonnées.

### Problèmes avec les nombres aléatoires

Les questions courantes incluent « mes nombres aléatoires sont-ils vraiment aléatoires ? » et « comment puis-je générer des nombres aléatoires non répétés ? »

**Note** : ce dernier diminue l'aléatoire, car la population des nombres aléatoires possibles est réduite d'un chaque fois qu'un nombre aléatoire est tiré. La méthode est appropriée dans des situations telles que les loteries ou le bingo, où chaque ticket ou boule ne peut être tiré qu'une seule fois.

Ce problème en amène un autre ! Les nombres générés aléatoirement, échantillonnés sans remplacement, doivent être des entiers. Personne n'a de ticket 5,6932 ou de boule de bingo 0,18967.

### Un exemple pratique de problèmes de nombres aléatoires

Prenons l'exemple où j'ai 20 étudiantes du même âge. J'ai quatre méthodes d'enseignement que je souhaite tester. Je ne veux tester qu'une seule méthode d'enseignement pour chaque étudiante. Mathématiques simples — j'ai besoin de cinq étudiantes dans chaque groupe.

Mais comment faire pour que chaque étudiante soit assignée aléatoirement ?

Et comment m'assurer que seuls des entiers sont produits ?

Et comment faire tout cela en utilisant des nombres générés aléatoirement sans remplacement ? Je ne veux pas, par exemple, six étudiantes dans un groupe et quatre dans un autre.

Tout d'abord, je dois créer des données fictives, en R. Créons cette liste de fausses étudiantes.

```
FemaleStudents <- data.frame(Names=c("Alice", "Betty", "Carol", "Denise", "Erica", "Frances", "Gina", "Helen", "Iris", "Julie", "Katherine",                           "Lisa", "Michelle", "Ngaire", "Olivia", "Penelope", "Rachel", "Sarah", "Trudy", "Uma"))
```

Maintenant, nous avons un ensemble de données unidimensionnel de nos 20 étudiantes.

Nous savons que la fonction `runif()` ne crée pas d'entiers. Pourquoi ne pas arrondir les nombres aléatoires pour n'obtenir que des entiers et utiliser cette fonction ? Nous pouvons envelopper le nombre aléatoire dans une fonction d'arrondi.

**Question 1** : pourquoi est-ce que j'utilise la distribution uniforme aléatoire et non une autre, comme la distribution normale aléatoire ?

Il existe cinq types de fonctions d'arrondi en R. Nous utiliserons `round()`.

Pour obtenir les mêmes résultats, je vais définir une graine pour la génération de nombres aléatoires. Chaque fois que nous générons des nombres aléatoires, nous utiliserons la même graine. J'ai choisi 5 comme graine. Si vous ne définissez pas de graine, ou si vous définissez une graine autre que 5, vos résultats seront différents des miens.

```
set.seed(5)FemaleStudents$Group <- round(runif(20, 1, 5))
```

Cela semble avoir fonctionné. Nous avons chaque étudiante assignée à un groupe numéroté entre 1 et 5.

Vérifions notre assignation.

```
table(FemaleStudents$Group)
```

```
1 2 3 4 5 2 6 5 4 3
```

Zut. Un seul des cinq groupes a le nombre correct d'étudiantes (Groupe 4). Pourquoi cela s'est-il produit ?

Nous pouvons vérifier les nombres réellement produits par `runif()` sans arrondi, et laisser la sortie s'imprimer sur la console. Ici, la sortie s'imprime parce que je n'ai pas assigné la fonction à un objet (par exemple, à une variable de data.frame).

```
set.seed(5)runif(20,1,5)
```

```
[1] 1.800858 3.740874 4.667503 2.137598 1.418601 3.804230 3.111840 4.231741 4.826001 1.441812 2.093140 2.962053 2.273616 3.236691 2.050373[16] 1.807501 2.550103 4.551479 3.219690 4.368718
```

Comme nous pouvons le voir, l'arrondi a causé notre problème. Mais si nous n'avions pas arrondi, chaque étudiante aurait été assignée à un groupe différent.

Que faisons-nous ?

### sample()

`sample()` est maintenant l'une de mes fonctions préférées en R. Voyons comment elle fonctionne.

#### Allouer aléatoirement à des groupes de taille égale (les comptes importent)

Comment pouvons-nous l'utiliser pour assigner aléatoirement nos 20 étudiantes à quatre groupes de taille égale ?

Que se passe-t-il si nous essayons `sample()` normalement ?

```
set.seed(5)FemaleStudents$Sample <- sample(1:5, nrow(FemaleStudents), replace=TRUE)
```

**Question 2** : quelle sortie avez-vous obtenue lorsque vous avez utilisé `table(FemaleStudents$Sample)` ?

Nous pouvons résoudre ce problème en créant un vecteur de numéros de groupe, puis en utilisant un échantillonnage sans remplacement à partir de ce vecteur. La commande `rep` est utilisée pour créer une série de valeurs répétées. Vous pouvez l'utiliser pour répéter chaque nombre dans la série, comme je l'ai fait ici. Le nombre 1 est répété quatre fois, puis le nombre 2 est répété quatre fois, et ainsi de suite. Vous pouvez également l'utiliser pour répéter une séquence de nombres, si vous utilisez ce code à la place : `rep(1:5,4)`

```
OurGroups <- rep(1:5, each=4)set.seed(5)FemaleStudents$Sample <- sample(OurGroups, nrow(FemaleStudents), replace=FALSE)
```

Nous avons utilisé notre vecteur de nombres (`OurGroups`) pour assigner nos étudiantes à des groupes. Nous avons utilisé un échantillonnage sans remplacement (`replace=FALSE`) à partir de `OurGroups` parce que nous devons utiliser chaque valeur dans ce vecteur. Nous devons supprimer chaque valeur au fur et à mesure que nous l'utilisons.

Et nous obtenons le résultat que nous voulions !

```
table(FemaleStudents$Sample)
```

```
1 2 3 4 5 4 4 4 4 4
```

**Question 3** : pourquoi ai-je encore défini une graine ?

Un autre avantage de `sample()` est qu'il ne se soucie pas du type. Nous pouvons répéter l'assignation en utilisant un vecteur de chaînes de caractères. Cela peut être utile si vous ne voulez pas continuer à vous référer à ce que signifie « 1 ».

```
OurNamedGroups <- rep(c("Up", "Down", "Charmed", "Strange", "Top"), each=4)set.seed(5)FemaleStudents$Sample2 <- sample(OurNamedGroups, nrow(FemaleStudents), replace=FALSE)table(FemaleStudents$Sample2)
```

```
Charmed    Down Strange     Top      Up       4       4       4       4       4
```

Parce que nous avons utilisé la même graine, nous pouvons voir que la même assignation d'étudiantes a été effectuée, indépendamment du fait que nous ayons utilisé des données numériques ou des caractères pour l'assignation.

```
table(FemaleStudents$Sample,FemaleStudents$Sample2)       Charmed Down Strange Top Up  1       0    0       0   0  4  2       0    4       0   0  0  3       4    0       0   0  0  4       0    0       4   0  0  5       0    0       0   4  0
```

#### Allouer aléatoirement lorsque la taille du groupe n'est pas restreinte

Parfois, nous voulons allouer aléatoirement à des groupes, mais nous n'avons pas de vecteur de groupes. Nous n'allouons toujours qu'une seule unité (personne, mouton, bloc de fromage) à un seul groupe, et nous utilisons une allocation complètement aléatoire.

Supposons que notre école dispose d'une nouvelle salle de bibliothèque spéciale. Elle a été construite pour être insondable afin de donner aux étudiants un meilleur environnement d'étude. Le bibliothécaire en chef aimerait connaître les expériences des étudiants dans cette salle. Le seul problème est que la salle est limitée en taille. Le bibliothécaire en chef pense qu'un groupe d'environ quatre étudiants est suffisamment grand pour fournir les premiers retours.

Encore une fois, nous pouvons utiliser `sample()` pour choisir nos groupes d'étudiants. Dans ce cas, nous avons « des étudiants qui testeront la salle » et « des étudiants qui ne testeront pas la salle ». Je vais les appeler « Test » et « Not test ». Ces libellés ont été choisis pour être 1. courts et 2. facilement distinguables.

Parce que nous avons fait un échantillonnage sans remplacement plus tôt, nous n'avons pas spécifié de probabilités d'assignation aux groupes — nous avons simplement tiré une assignation d'un vecteur. Maintenant, nous allons utiliser un échantillonnage avec remplacement. Avec remplacement fait référence au groupe, et non aux étudiants.

Nous devons échantillonner avec remplacement car nous n'avons que deux groupes (« Test », « Not test ») et 20 étudiants. Si nous essayions d'échantillonner sans remplacement, notre code générerait une erreur.

Notre code est très similaire :

```
set.seed(5)FemaleStudents$Library <- sample(c("Test", "Not test"), nrow(FemaleStudents), replace=TRUE, prob=c(4/20,16/20))table(FemaleStudents$Library)
```

```
Not test     Test       15        5
```

Comme vous pouvez le voir, nous avons assigné cinq étudiants pour tester la salle, et non quatre. Ce type de résultat est attendu lorsque l'on traite de petits échantillons. Cependant, notre assignation d'étudiants est complètement aléatoire. Chaque étudiant avait exactement la même probabilité d'être assigné pour tester la salle. Le fait que les étudiants précédents soient testeurs ou non n'a eu aucun impact sur l'assignation de l'étudiant suivant.

Parcourons une partie de ce code.

J'ai construit une nouvelle variable dans le `data.frame` pour collecter l'assignation (`Library`).

Au lieu de traiter avec des nombres pour les noms de groupes, j'ai utilisé les chaînes de caractères que j'ai mentionnées précédemment. Parce que j'ai utilisé des chaînes de caractères, le `c()` doit envelopper les noms de groupes (`"Test"`, `"Not test"`) et chaque nom de groupe est séparé par une virgule.

Le remplacement a été défini sur `TRUE`.

La probabilité d'assignation à l'un ou l'autre groupe doit être fournie. Il s'agit de la partie `prob=c(4/20,16/20)` de la fonction `sample()`. Notez à nouveau comment `c()` est utilisé pour contenir les probabilités. Il est également intéressant de noter que les probabilités peuvent être exprimées sous forme de fractions, plutôt que de décimales.

### Hourra pour sample()

J'utilise `sample()` tout le temps pour le travail que je fais. La possibilité d'utiliser des chaînes de caractères, ainsi que de restreindre la sortie numérique aux entiers (et de définir la plage d'entiers souhaitée), me donne plus de contrôle que d'essayer d'utiliser l'une des fonctions de nombres aléatoires.

### Réponses

**Réponse 1** : J'ai utilisé une distribution uniforme aléatoire parce que je voulais que chaque valeur soit également probable.

**Réponse 2** : J'ai obtenu cette sortie :

```
1 2 3 4 5 2 7 4 2 5
```

**Réponse 3** : Si nous ne définissons pas de valeur de graine, ou si nous utilisons une valeur différente, l'assignation des étudiants spécifiques sera différente. Par exemple, lorsque la graine est 5, Alice est assignée au groupe 2. Si la graine est 7, Alice est assignée au groupe 5. La réplication est importante lorsque le code doit être réexécuté (par exemple, lors des tests).