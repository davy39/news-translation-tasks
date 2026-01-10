---
title: Qu'est-ce qu'un ordinateur quantique ? Expliqué avec un exemple simple.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-22T20:59:54.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-quantum-computer-explained-with-a-simple-example-b8f602035365
coverImage: https://cdn-media-1.freecodecamp.org/images/0*juPpwvGEsj0xky-d
tags:
- name: Computer Science
  slug: computer-science
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: quantum computing
  slug: quantum-computing
seo_title: Qu'est-ce qu'un ordinateur quantique ? Expliqué avec un exemple simple.
seo_desc: 'By YK Sugi

  Hi everyone!

  The other day, I visited D-Wave Systems in Vancouver, Canada. It’s a company that
  makes cutting-edge quantum computers.

  I got to learn a lot about quantum computers there, so I’d like to share some of
  what I learned there with...'
---

Par YK Sugi

Bonjour à tous !

L'autre jour, j'ai visité [**D-Wave Systems**](https://www.dwavesys.com/) à Vancouver, au Canada. C'est une entreprise qui fabrique des ordinateurs quantiques de pointe.

J'ai pu en apprendre beaucoup sur les ordinateurs quantiques là-bas, alors je voudrais partager avec vous une partie de ce que j'ai appris dans cet article.

Le but de cet article est de vous donner une intuition précise de ce qu'est un ordinateur quantique en utilisant un exemple simple.

Cet article ne nécessitera pas que vous ayez des connaissances préalables en physique quantique ou en informatique pour pouvoir le comprendre.

D'accord, commençons.

**_Édition (26 févr. 2019) :_** J'ai récemment publié [une vidéo sur le même sujet](https://youtu.be/HdSmIUuGf-I) sur [ma chaîne YouTube](https://www.youtube.com/csdojo). Je vous recommande de la regarder ([cliquez ici](https://youtu.be/HdSmIUuGf-I)) avant ou après la lecture de cet article, car j'ai ajouté quelques arguments supplémentaires et plus nuancés dans la vidéo.

### Qu'est-ce qu'un ordinateur quantique ?

Voici un résumé en une phrase de ce qu'est un ordinateur quantique :

> Un ordinateur quantique est un type d'ordinateur qui utilise la mécanique quantique afin de pouvoir effectuer certains types de calculs plus efficacement qu'un ordinateur classique.

Il y a beaucoup à déballer dans cette phrase, alors laissez-moi vous expliquer ce que c'est exactement en utilisant un exemple simple.

Pour expliquer ce qu'est un ordinateur quantique, je devrais d'abord expliquer un peu le fonctionnement des ordinateurs classiques (non quantiques).

### Comment un ordinateur classique stocke l'information

Un ordinateur classique stocke l'information dans une série de 0 et de 1.

Différents types d'informations, tels que les nombres, le texte et les images, peuvent être représentés de cette manière.

Chaque unité de cette série de 0 et de 1 est appelée un bit. Ainsi, un bit peut être défini sur 0 ou 1.

#### Maintenant, qu'en est-il des ordinateurs quantiques ?

Un ordinateur quantique **n'utilise pas** de bits pour stocker l'information. Au lieu de cela, il utilise quelque chose appelé qubits.

Chaque qubit peut non seulement être défini sur 1 **ou** 0, mais il peut également être défini sur 1 **et** 0. Mais que signifie cela exactement ?

Laissez-moi expliquer cela avec un exemple simple. Cela va être un exemple quelque peu artificiel. Mais il sera toujours utile pour comprendre comment fonctionnent les ordinateurs quantiques.

### **Un exemple simple pour comprendre comment fonctionnent les ordinateurs quantiques**

Supposons que vous dirigez une agence de voyages et que vous devez déplacer un groupe de personnes d'un endroit à un autre.

Pour simplifier, disons que vous devez déplacer seulement 3 personnes pour l'instant — Alice, Becky et Chris.

Et supposons que vous avez réservé 2 taxis à cet effet, et que vous voulez déterminer qui monte dans quel taxi.

Supposons également que vous avez des informations sur qui est ami avec qui et qui est ennemi avec qui.

Ici, disons que :

* Alice et Becky sont amies
* Alice et Chris sont ennemis
* Becky et Chris sont ennemis

Et supposons que votre objectif ici est de diviser ce groupe de 3 personnes dans les deux taxis pour atteindre les deux objectifs suivants :

* Maximiser le nombre de **paires d'amis** qui partagent la même voiture
* Minimiser le nombre de **paires d'ennemis** qui partagent la même voiture

D'accord, voici la prémisse de base de ce problème. Réfléchissons d'abord à la manière dont nous pourrions résoudre ce problème en utilisant un ordinateur classique.

#### **Résoudre ce problème avec un ordinateur classique**

Pour résoudre ce problème avec un ordinateur classique, non quantique, vous devrez d'abord déterminer comment stocker les informations pertinentes avec des bits.

Étiquetons les deux taxis Taxi #1 et Taxi #0.

Ensuite, vous pouvez représenter qui monte dans quelle voiture avec 3 bits.

Par exemple, nous pouvons définir les trois bits à **0**, **0** et **1** pour représenter :

* Alice monte dans le Taxi #0
* Becky monte dans le Taxi #0
* Chris monte dans le Taxi #1

Puisqu'il y a deux choix pour chaque personne, il y a 2*2*2 = 8 façons de diviser ce groupe de personnes en deux voitures.

Voici une liste de toutes les configurations possibles :

A | B | C  
0 | 0 | 0  
0 | 0 | 1  
0 | 1 | 0  
0 | 1 | 1  
1 | 0 | 0  
1 | 0 | 1  
1 | 1 | 0  
1 | 1 | 1

En utilisant 3 bits, vous pouvez représenter l'une de ces combinaisons.

#### Calculer le score pour chaque configuration

Maintenant, en utilisant un ordinateur classique, comment déterminer quelle configuration est la meilleure solution ?

Pour ce faire, définissons comment nous pouvons calculer le score pour chaque configuration. Ce score représentera dans quelle mesure chaque solution atteint les deux objectifs que j'ai mentionnés précédemment :

* Maximiser le nombre de **paires d'amis** qui partagent la même voiture
* Minimiser le nombre de **paires d'ennemis** qui partagent la même voiture

Définissons simplement notre score comme suit :

(le score d'une configuration donnée) = (nombre de paires d'amis partageant la même voiture) - (nombre de paires d'ennemis partageant la même voiture)

Par exemple, supposons qu'Alice, Becky et Chris montent tous dans le Taxi #1. Avec trois bits, cela peut être exprimé comme **111**.

Dans ce cas, il n'y a qu'**une paire d'amis** partageant la même voiture — Alice et Becky.

Cependant, il y a **deux paires d'ennemis** partageant la même voiture — Alice et Chris, et Becky et Chris.

Ainsi, le score total de cette configuration est 1-2 = -1.

#### Résoudre le problème

Avec toute cette configuration, nous pouvons enfin résoudre ce problème.

Avec un ordinateur classique, pour trouver la meilleure configuration, vous devrez essentiellement passer en revue toutes les configurations pour voir laquelle obtient le score le plus élevé.

Ainsi, vous pouvez penser à construire un tableau comme celui-ci :

A | B | C | Score  
0 | 0 | 0 | -1  
0 | 0 | 1 | 1 <- l'une des meilleures solutions  
0 | 1 | 0 | -1  
0 | 1 | 1 | -1  
1 | 0 | 0 | -1  
1 | 0 | 1 | -1  
1 | 1 | 0 | 1 <- l'autre meilleure solution  
1 | 1 | 1 | -1

Comme vous pouvez le voir, il y a deux solutions correctes ici — 001 et 110, toutes deux obtenant un score de 1.

Ce problème est assez simple. Il devient rapidement trop difficile à résoudre avec un ordinateur classique à mesure que nous augmentons le nombre de personnes dans ce problème.

Nous avons vu qu'avec 3 personnes, nous devons passer en revue 8 configurations possibles.

Et s'il y a 4 personnes ? Dans ce cas, nous devrons passer en revue 2*2*2*2 = 16 configurations.

Avec n personnes, nous devrons passer en revue (2 à la puissance n) configurations pour trouver la meilleure solution.

Ainsi, s'il y a 100 personnes, nous devrons passer en revue :

* 2¹⁰⁰ ≈ 10³⁰ = un million de millions de millions de millions de millions de configurations.

Cela est simplement impossible à résoudre avec un ordinateur classique.

#### Résoudre ce problème avec un ordinateur quantique

Comment pourrions-nous résoudre ce problème avec un ordinateur quantique ?

Pour y réfléchir, revenons au cas de la division de 3 personnes en deux taxis.

Comme nous l'avons vu précédemment, il y avait 8 solutions possibles à ce problème :

A | B | C  
0 | 0 | 0  
0 | 0 | 1  
0 | 1 | 0  
0 | 1 | 1  
1 | 0 | 0  
1 | 0 | 1  
1 | 1 | 0  
1 | 1 | 1

Avec un ordinateur classique, en utilisant 3 bits, nous pouvions représenter une seule de ces solutions à la fois — par exemple, 001.

Cependant, avec un ordinateur quantique, en utilisant 3 **qubits**, nous pouvons représenter **les 8 solutions en même temps**.

Il y a des débats quant à ce que cela signifie exactement, mais voici comment je le conçois.

Tout d'abord, examinez le premier qubit parmi ces 3 qubits. Lorsque vous le définissez à **la fois** 0 et 1, c'est un peu comme créer deux mondes parallèles. (Oui, c'est étrange, mais suivez-moi ici.)

Dans l'un de ces mondes parallèles, le qubit est défini sur 0. Dans l'autre, il est défini sur 1.

Maintenant, que se passe-t-il si vous définissez le deuxième qubit sur 0 **et** 1 également ? Alors, c'est un peu comme créer 4 mondes parallèles.

Dans le premier monde, les deux qubits sont définis sur 00. Dans le deuxième, ils sont 01. Dans le troisième, ils sont 10. Dans le quatrième, ils sont 11.

De même, si vous définissez les trois qubits à la fois sur 0 et 1, vous créeriez 8 mondes parallèles — 000, 001, 010, 011, 100, 101, 110 et 111.

C'est une manière étrange de penser, mais c'est l'une des bonnes façons d'interpréter comment les qubits se comportent dans le monde réel.

Maintenant, lorsque vous appliquez un certain type de calcul sur ces trois qubits, vous appliquez en réalité le même calcul dans tous ces 8 mondes parallèles en même temps.

Ainsi, au lieu de passer en revue chaque solution potentielle séquentiellement, nous pouvons calculer les scores de toutes les solutions en même temps.

Avec cet exemple particulier, en théorie, votre ordinateur quantique serait capable de trouver l'une des meilleures solutions en quelques millisecondes. Encore une fois, ce sont 001 ou 110 comme nous l'avons vu précédemment :

A | B | C | Score  
0 | 0 | 0 | -1  
**0 | 0 | 1 | 1 <- l'une des meilleures solutions**  
0 | 1 | 0 | -1  
0 | 1 | 1 | -1  
1 | 0 | 0 | -1  
1 | 0 | 1 | **-1**  
**1 | 1 | 0 | 1 <- l'autre meilleure solution**  
1 | 1 | 1 | -1

En réalité, pour résoudre ce problème, vous devrez donner à votre ordinateur quantique deux choses :

* Toutes les solutions potentielles représentées avec des qubits
* Une fonction qui transforme chaque solution potentielle en un score. Dans ce cas, il s'agit de la fonction qui compte le nombre de paires d'amis et de paires d'ennemis partageant la même voiture.

Étant donné ces deux éléments, votre ordinateur quantique fournira l'une des meilleures solutions en quelques millisecondes. Dans ce cas, il s'agit de 001 ou 110 avec un score de 1.

Maintenant, en théorie, un ordinateur quantique est capable de trouver l'une des meilleures solutions à chaque fois qu'il est exécuté.

Cependant, en réalité, il y a des erreurs lors de l'exécution d'un ordinateur quantique. Ainsi, au lieu de trouver la meilleure solution, il pourrait trouver la deuxième meilleure solution, la troisième meilleure solution, et ainsi de suite.

Ces erreurs deviennent plus importantes à mesure que le problème devient de plus en plus complexe.

Ainsi, en pratique, vous voudrez probablement exécuter la même opération sur un ordinateur quantique des dizaines de fois ou des centaines de fois. Ensuite, choisissez le meilleur résultat parmi les nombreux résultats obtenus.

#### Comment un ordinateur quantique évolue

Même avec les erreurs que j'ai mentionnées, l'ordinateur quantique ne souffre pas du même problème d'évolutivité qu'un ordinateur classique.

Lorsque nous avons 3 personnes à diviser en deux voitures, le nombre d'opérations que nous devons effectuer sur un ordinateur quantique est de 1. Cela est dû au fait qu'un ordinateur quantique calcule le score de toutes les configurations en même temps.

Lorsque nous avons 4 personnes, le nombre d'opérations est toujours de 1.

Lorsque nous avons 100 personnes, le nombre d'opérations est toujours de 1. Avec une seule opération, un ordinateur quantique calcule les scores de toutes les **2¹⁰⁰** ≈ **10³⁰** = **un million de millions de millions de millions de millions** de configurations en même temps.

Comme je l'ai mentionné précédemment, en pratique, il est probablement préférable d'exécuter votre ordinateur quantique des dizaines de fois ou des centaines de fois et de choisir le meilleur résultat parmi les nombreux résultats obtenus.

Cependant, c'est toujours beaucoup mieux que d'exécuter le même problème sur un ordinateur classique et de devoir répéter le même type de calcul un million de millions de millions de millions de millions de fois.

#### Conclusion

Un grand merci à tous chez D-Wave Systems pour m'avoir expliqué tout cela avec patience.

D-Wave a récemment lancé un environnement cloud pour interagir avec un ordinateur quantique.

Si vous êtes un développeur et que vous souhaitez essayer d'utiliser un ordinateur quantique, c'est probablement la manière la plus simple de le faire.

Il s'appelle Leap, et il est disponible à l'adresse [https://cloud.dwavesys.com/leap](https://cloud.dwavesys.com/leap). Vous pouvez l'utiliser gratuitement pour résoudre des milliers de problèmes, et ils proposent également des tutoriels faciles à suivre pour commencer avec les ordinateurs quantiques une fois que vous vous êtes inscrit.

**Note de bas de page :**

* Dans cet article, j'ai utilisé le terme « ordinateur classique » pour désigner un ordinateur non quantique. Cependant, dans l'industrie de l'informatique quantique, les ordinateurs non quantiques sont généralement appelés ordinateurs classiques.