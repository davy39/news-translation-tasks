---
title: Comment atteindre stratégiquement les objectifs de performance de votre modèle
  de machine learning
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-19T16:32:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-strategically-accomplish-your-machine-learning-models-performance-goals-44dddc11697e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*VyUN0eeSx1yujR3tP3zToQ.jpeg
tags:
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: Supervised learning
  slug: supervised-learning
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment atteindre stratégiquement les objectifs de performance de votre
  modèle de machine learning
seo_desc: 'By Nezar Assawiel

  Introduction

  Machine learning (ML) development is an iterative process. You have an idea to solve
  the problem at hand, you build the idea and examine the results. You get another
  idea to improve the results and so on until you reach...'
---

Par Nezar Assawiel

### Introduction

Le développement en machine learning (ML) est un processus itératif. Vous avez une idée pour résoudre le problème en question, vous construisez cette idée et examinez les résultats. Vous obtenez une autre idée pour améliorer les résultats et ainsi de suite jusqu'à atteindre l'objectif de performance qui rend votre modèle prêt pour le déploiement en production — prêt à être utilisé par les utilisateurs finaux.

![Image](https://cdn-media-1.freecodecamp.org/images/W7qDzWbOJ1O78hu7oFLRRRKueOOCF07LYFd7)
_Figure 1. Le processus itératif dans le développement ML._

Cependant, il existe souvent de nombreuses idées et possibilités que vous pouvez essayer pour améliorer les performances et vous rapprocher de votre objectif. Par exemple, vous pouvez collecter plus de données, entraîner plus longtemps ou essayer des réseaux plus grands ou plus petits.

Aller dans la mauvaise direction pendant ce processus d'expérimentation peut être coûteux, surtout pour les grands projets. Personne ne veut passer deux mois à collecter plus de données pour découvrir plus tard que le gain de performance était négligeable et que cela ne valait pas un jour, et encore moins deux mois !

Fixer et travailler stratégiquement vers l'objectif de performance de votre modèle ML est vital pour accélérer le processus d'expérimentation et atteindre cet objectif. Dans cet article, je présente quelques conseils qui, je l'espère, vous aideront à cet égard.

### Connaissances préalables attendues

Cet article suppose que vous connaissez au moins les bases de la construction d'un modèle ML. Cette discussion n'a pas pour but d'illustrer ce qu'est un modèle ML ou comment en construire un. Plutôt, le contenu porte sur la manière d'améliorer stratégiquement un modèle ML pendant le processus de développement. **Plus précisément, les concepts et terminologies suivants devraient vous être familiers :**

* **ensembles d'entraînement, de développement (dev) et de test :** L'ensemble de développement est également appelé ensemble de validation ou de maintien. [Cet article](https://towardsdatascience.com/train-validation-and-test-sets-72cb40cba9e7) est une excellente introduction courte sur le sujet.
* **métriques d'évaluation (ou de performance) :** Ce sont les mesures utilisées pour indiquer à quel point un modèle ML est "bon" dans l'exécution de sa tâche. [Voici un article](https://towardsdatascience.com/metrics-to-evaluate-your-machine-learning-algorithm-f10ba6e38234) couvrant certaines des métriques de base utilisées en ML.
* **erreurs de biais (sous-ajustement) et de variance (surajustement) :** [Ceci](https://www.quora.com/What-is-the-best-way-to-explain-the-bias-variance-trade-off-in-laymans-terms) est une excellente explication de ces erreurs de manière simple.

### L'importance de l'orthogonalisation

Comme vous le savez, les étapes séquentielles dans le développement d'un modèle ML sont les suivantes :

1. bien ajuster l'ensemble d'entraînement. Par exemple, essayer un réseau plus grand, essayer une autre méthode d'optimisation de la fonction de coût, essayer un entraînement plus long.
2. bien ajuster l'ensemble de développement. Par exemple, essayer la régularisation, essayer de collecter plus de données d'entraînement.
3. bien ajuster l'ensemble de test. Par exemple, essayer un ensemble de développement plus grand.
4. bien performer en production. Si ce n'est pas le cas, l'ensemble de développement doit changer ou la fonction de coût du modèle.

Pendant ce processus, idéalement, vous aimeriez que les modifications que vous essayez — "contrôles du modèle" — soient indépendantes. Pourquoi ?

Prenez, par exemple, le volant d'une voiture. Lorsque vous tournez le volant à gauche, la voiture va à gauche. Lorsque vous le tournez à droite, la voiture va à droite. Que se passerait-il si tourner le volant à gauche faisait aller la voiture à gauche **et** augmentait la vitesse de la voiture ? Il deviendrait beaucoup plus difficile de contrôler la voiture, n'est-ce pas ? Pourquoi ? Parce que tourner le volant à gauche n'est **plus un contrôle indépendant** de la voiture. Il est couplé avec un autre contrôle, le contrôle de la vitesse. Il est toujours plus facile lorsque les contrôles sont indépendants.

Dans le développement ML, **l'arrêt précoce**, par exemple, est une forme de régularisation utilisée pour améliorer les performances sur l'ensemble de développement en s'entraînant uniquement sur une partie de l'ensemble d'entraînement. Ainsi, l'arrêt précoce est un contrôle qui **n'est pas indépendant** d'un autre contrôle, à savoir la durée d'entraînement.

Pour un processus de développement itératif plus rapide, vous aimeriez que vos contrôles soient indépendants, c'est-à-dire **orthogonalisés**. En d'autres termes, envisagez d'éviter les contrôles dépendants comme l'arrêt précoce autant que possible pour un processus de développement plus rapide.

### Stratégies

Avec l'introduction précédente à l'esprit, voici quelques conseils pour fixer et améliorer stratégiquement les performances de votre modèle :

#### **a) Combiner plusieurs métriques d'évaluation en une seule**

Il est probable que vous ayez plusieurs métriques d'évaluation pour évaluer la performance de votre modèle ML. Par exemple, vous pourriez avoir le rappel et la précision pour évaluer un classificateur. Le rappel et la précision sont des métriques concurrentes — typiquement, lorsque l'une augmente, l'autre diminue. Alors, comment choisissez-vous le meilleur classificateur dans le Tableau 1 ci-dessous, par exemple ?

Dans ce cas, il est bon de combiner la précision et le rappel en une seule métrique. Le score F1 [`F1 score= (2 *precision*recall)/(precision + recall)`] fera l'affaire, comme vous l'aurez peut-être déjà réalisé. Ainsi, le Classificateur A du Tableau 1 aura le meilleur score F1.

![Image](https://cdn-media-1.freecodecamp.org/images/VDbYkaITbwmpoj-nCZD4xrjHk5bR2Pc1ekzd)
_Tableau 1. Résultats de performance d'un classificateur (données synthétiques)._

Évidemment, ce processus est spécifique au problème. Votre application pourrait nécessiter de maximiser la précision. Dans ce cas, le Classificateur C dans le Tableau 1 sera votre meilleur choix.

**Optimisation et satisficing**

Vous pourriez vouloir suivre l'approche d'optimisation et de satisficing. Cela signifie que vous optimisez une métrique tant que l'autre ou les autres métriques atteignent un certain seuil minimum.

Supposons que les classificateurs du Tableau 1, et la précision et le temps d'exécution soient deux métriques comme montré dans le Tableau 2 ci-dessous. Vous pourriez être principalement préoccupé par l'optimisation d'une métrique — la précision — tant que les autres métriques — le temps d'exécution — atteignent un certain seuil. Dans cet exemple, le seuil de temps d'exécution est de 50 ms ou moins. Ainsi, vous cherchez le classificateur avec la plus haute précision **tant que** le temps d'exécution est de 50 ms ou moins. Ainsi, dans le Tableau 2, vous choisirez le Classificateur B.

![Image](https://cdn-media-1.freecodecamp.org/images/uDAYD411VFlfsBjhatOvt22hDNCCJFtOWl3B)
_Tableau 2. Résultats de performance d'un classificateur (données synthétiques)._

Cependant, si votre objectif est de maximiser la performance sur toutes les métriques, vous devrez les combiner.

Il n'est pas toujours facile de combiner toutes les métriques en une seule. Il peut y en avoir beaucoup. La relation entre elles n'est pas claire. Dans de tels cas, vous devrez être **créatif** et **attentif** en les combinant ! Le temps que vous investissez pour créer une métrique de performance **tout-en-un** en vaut la peine. Cela n'accélérera pas seulement le processus de développement, mais produira également un modèle bien performant en production.

#### **b) Définir correctement les ensembles d'entraînement, de développement et de test**

**Choisir la bonne taille pour la division train/dev/test**

Vous avez probablement vu la division 60 %, 20 %, 20 % pour les ensembles de données d'entraînement, de développement et de test, respectivement. Cela fonctionne bien pour les petits ensembles de données — disons 10 000 points de données ou moins. Cependant, lorsque vous travaillez avec de grands ensembles de données, surtout avec le deep learning, une division 98 %, 1 %, 1 % ou similaire pourrait être plus appropriée. Si vous avez 2 millions de points de données dans votre ensemble de données, une division de 1 % représente 20 000 points de données, ce qui est suffisant pour les ensembles de développement et de test.

En général, vous voulez que votre ensemble de développement soit suffisamment grand pour capturer les changements que vous apportez à votre modèle pendant votre processus d'expérimentation. Vous voulez que votre ensemble de test soit suffisamment grand pour vous donner une grande confiance dans la performance de votre modèle.

**Assurez-vous que les ensembles de développement et de test proviennent de la même distribution**

Bien que cela puisse sembler trivial, j'ai vu des développeurs expérimentés oublier ce point important. Supposons que vous avez expérimenté et amélioré de manière itérative un modèle qui prédit les défauts de paiement sur les prêts automobiles en fonction du code postal. N'attendez pas de votre modèle qu'il fonctionne correctement sur un ensemble de test provenant de zones de code postal avec un revenu moyen faible si l'ensemble de développement provient de zones de code postal avec un revenu moyen élevé, par exemple. Ce sont deux distributions différentes !

**Assurez-vous que les ensembles de développement et de test reflètent les données que votre modèle rencontrera en production**

Par exemple, si vous faites de la reconnaissance faciale, la résolution de vos images de dev/test devrait refléter la résolution des images en production. Bien que cela puisse être un exemple trivial, vous devriez examiner tous les aspects des données sur lesquelles votre application fonctionnera en production par rapport à vos données d'entraînement/dev/test. Si votre modèle fonctionne bien sur votre métrique et les ensembles dev/test mais pas aussi bien en production, vous avez la mauvaise métrique et/ou les mauvais ensembles dev/test !

#### **c) Identifier et traiter la "bonne" erreur en premier**

**Erreur de Bayes et erreur humaine**

L'erreur de Bayes est l'erreur théorique la plus faible qui existe dans un modèle, en d'autres termes, une erreur irréductible. Prenons, par exemple, un classificateur de chiens qui prédit si l'image en question est celle d'un chien ou d'un autre animal. Il peut y avoir certaines images si floues qu'il est impossible de les classer par des humains ou même le système le plus sophistiqué jamais inventé. Ce sera l'erreur de Bayes.

L'erreur humaine, par définition, est plus grande — pire — que l'erreur de Bayes. Cependant, l'erreur humaine est généralement très proche de l'erreur de Bayes puisque nous sommes vraiment bons pour reconnaître les motifs. Ainsi, l'erreur humaine est généralement utilisée comme une approximation de l'erreur de Bayes.

**Améliorer en dessous de la performance humaine**

Lorsque la performance de votre modèle ML est en dessous de la performance humaine, vous pouvez améliorer la performance en :

1. obtenant plus de données étiquetées par des humains
2. analysant les erreurs et incorporant les insights dans le système. Pourquoi le modèle ML se trompe-t-il sur ceci et cela alors que les humains ont raison ?
3. améliorant le modèle lui-même. Regardez s'il sous-ajuste — erreur de biais élevée — ou surajuste — erreur de variance élevée — et changez le modèle en conséquence.

Une fois que la performance humaine est dépassée, l'amélioration de la performance devient un processus beaucoup plus lent et plus difficile, comme vous pourriez vous y attendre.

![Image](https://cdn-media-1.freecodecamp.org/images/2DvahR7miwZrjbOlFXipt4xzVvO-cK06nN4A)
_Figure 2. Courbe de performance d'un modèle ML typique en fonction du temps passé productivement à améliorer la performance (figure illustrative)._

Alors, comment définissez-vous exactement l'erreur humaine ? C'est ce qui est discuté ensuite !

**Définir l'erreur humaine et identifier l'erreur à traiter en premier**

Prenons le problème de classification de chiens précédent — reconnaître si une image est celle d'un chien ou non. Après avoir fait quelques recherches, vous pourriez trouver l'erreur humaine comme suit :

* personne moyenne : 2 % d'erreur
* zoologiste moyen : 1 % d'erreur
* zoologiste expert : 0,6 % d'erreur
* une équipe de zoologistes experts : 0,4 % d'erreur

Maintenant, considérons les quatre cas dans le Tableau 3 ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/szzodis3DGMaOLNY33d1axIxMZ9K3Wqjnpji)
_Tableau 3. Erreurs d'un classificateur d'images de chiens (données synthétiques). Erreur humaine (de haut en bas) : équipe de zoologistes experts, un zoologiste expert, le zoologiste moyen et la personne moyenne._

Dans le Cas A, votre priorité devrait être le problème de sous-ajustement — biais élevé — comme indiqué par les erreurs en rouge, puisque l'erreur de biais (5 % - 2 % = 3 %) est plus grande que l'erreur de variance (6 % - 5 % = 1 %). Pour l'erreur humaine, la **plus grande** parmi les erreurs humaines qui sont **plus petites que l'erreur d'entraînement** est utilisée **en premier**. Ainsi, votre référence d'erreur humaine dans ce cas est celle de la personne moyenne — 2 % — puisque c'est la plus grande erreur parmi les erreurs humaines qui sont plus petites que l'erreur d'entraînement (toutes dans ce cas).

Dans le Cas B, vous pourriez avoir besoin d'améliorer l'erreur de variance en premier, 9 % - 5 % = 4 %, puisque elle est plus grande que l'erreur de biais de 5 % - 2 % = 3 %.

Dans le Cas C, vous avez dépassé la performance humaine de la personne moyenne et vous êtes à égalité avec la performance du zoologiste moyen. Ainsi, votre nouvelle erreur humaine devrait être celle du zoologiste expert — 0,6 % — ou même de l'équipe de zoologistes experts — 0,4 %. L'erreur de variance dans ce cas est de 0,2 % tandis que l'erreur de biais est entre 0,4 % et 0,6 %. Ainsi, vous devriez travailler sur cette erreur en premier — besoin de mieux ajuster les données d'entraînement.

**Dépasser la performance humaine**

Dans le Cas D, vous voyez que l'erreur d'entraînement est de 0,2 % tandis que la meilleure erreur humaine est de 0,4 %. Cela signifie-t-il que votre modèle a dépassé la performance humaine ou que le modèle surajuste de 0,2 % ?! Vous voyez, il n'est pas clair de savoir s'il faut se concentrer sur l'erreur de biais ou sur l'erreur de variance. De plus, si, en effet, votre modèle a dépassé la performance humaine et que vous cherchez toujours à améliorer le modèle, il devient peu clair quelle stratégie suivre d'un point de vue intuitif humain.

Il existe de nombreux modèles ML de nos jours qui surpassent la performance humaine, tels que les systèmes de recommandation de produits et de ciblage publicitaire en ligne. Ces "modèles qui surpassent la performance humaine" tendent à être des systèmes de perception non naturels, c'est-à-dire, pas des systèmes de vision par ordinateur, de reconnaissance vocale ou de traitement du langage naturel. La raison en est que nous, les humains, sommes vraiment bons dans les tâches de perception naturelle.

Cependant, avec les big data et le deep learning, il existe des systèmes de perception naturels qui surpassent la performance humaine et ils s'améliorent de plus en plus. Mais ces problèmes sont beaucoup plus difficiles que les problèmes de perception non naturels.

Publié à l'origine sur [assawiel.com/blog](http://www.assawiel.com/blog) le 24 mars 2018. Modifié : 4 octobre 2018