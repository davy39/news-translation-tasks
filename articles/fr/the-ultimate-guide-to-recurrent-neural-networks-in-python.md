---
title: Le Guide Ultime des Réseaux de Neurones Récurrents en Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-13T16:48:49.000Z'
originalURL: https://freecodecamp.org/news/the-ultimate-guide-to-recurrent-neural-networks-in-python
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c99bf740569d1a4ca2186.jpg
tags:
- name: neural networks
  slug: neural-networks
- name: Python
  slug: python
seo_title: Le Guide Ultime des Réseaux de Neurones Récurrents en Python
seo_desc: 'By Nick McCullum

  Recurrent neural networks are deep learning models that are typically used to solve
  time series problems. They are used in self-driving cars, high-frequency trading
  algorithms, and other real-world applications.

  This tutorial will te...'
---

Par Nick McCullum

Les réseaux de neurones récurrents sont des modèles d'apprentissage profond généralement utilisés pour résoudre des problèmes de séries temporelles. Ils sont utilisés dans les voitures autonomes, les algorithmes de trading à haute fréquence et d'autres applications réelles.

Ce tutoriel vous enseignera les fondamentaux des réseaux de neurones récurrents. Vous construirez également votre propre réseau de neurones récurrent qui prédit le prix de l'action de Facebook (FB) pour demain.

# **L'Intuition des Réseaux de Neurones Récurrents**

Les [réseaux de neurones récurrents](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/) sont un exemple du domaine plus large des [réseaux de neurones](https://www.freecodecamp.org/news/deep-learning-neural-networks-explained-in-plain-english/). D'autres exemples incluent :

* [Les réseaux de neurones artificiels](https://nickmccullum.com/python-deep-learning/artificial-neural-network-tutorial/)
* [Les réseaux de neurones convolutifs](https://nickmccullum.com/python-deep-learning/convolutional-neural-network-tutorial/)

Cet article se concentrera sur les réseaux de neurones récurrents.

Ce tutoriel commencera notre discussion sur les réseaux de neurones récurrents en discutant de l'intuition derrière les réseaux de neurones récurrents.

## **Les Types de Problèmes Résolus par les Réseaux de Neurones Récurrents**

Bien que nous n'en ayons pas encore explicitement discuté, il existe généralement de larges catégories de problèmes que chaque type de réseau de neurones est conçu pour résoudre :

* Réseaux de neurones artificiels : problèmes de classification et de régression
* [Réseaux de neurones convolutifs](https://nickmccullum.com/python-deep-learning/introduction-convolutional-neural-networks/) : problèmes de vision par ordinateur

Dans le cas des réseaux de neurones récurrents, ils sont généralement utilisés pour résoudre des problèmes d'analyse de séries temporelles.

Chacun de ces trois types de réseaux de neurones (artificiels, convolutifs et récurrents) sont utilisés pour résoudre des problèmes d'apprentissage automatique supervisé.

## **Mapping des Réseaux de Neurones aux Parties du Cerveau Humain**

Comme vous vous en souvenez, les réseaux de neurones ont été conçus pour imiter le cerveau humain. Cela est vrai à la fois pour leur construction (le cerveau et les réseaux de neurones sont composés de neurones) et leur fonction (ils sont tous deux utilisés pour prendre des décisions et faire des prédictions).

Les trois parties principales du cerveau sont :

* Le cerveau
* Le tronc cérébral
* Le cervelet

Arguablement, la partie la plus importante du cerveau est le cerveau. Il contient quatre lobes :

* Le lobe frontal
* Le lobe pariétal
* Le lobe temporal
* Le lobe occipital

La principale innovation que contiennent les réseaux de neurones est l'idée de poids.

Autrement dit, la caractéristique la plus importante du cerveau que les réseaux de neurones ont imité est la capacité d'apprendre des autres neurones.

La capacité d'un réseau de neurones à changer ses poids à chaque époque de sa phase d'entraînement est similaire à la mémoire à long terme que l'on observe chez les humains (et autres animaux).

Le lobe temporal est la partie du cerveau associée à la mémoire à long terme. Séparément, le réseau de neurones artificiels était le premier type de réseau de neurones à avoir cette propriété de mémoire à long terme. En ce sens, de nombreux chercheurs ont comparé les réseaux de neurones artificiels au lobe temporal du cerveau humain.

De même, le lobe occipital est le composant du cerveau qui alimente notre vision. Puisque les réseaux de neurones convolutifs sont généralement utilisés pour résoudre des problèmes de vision par ordinateur, on pourrait dire qu'ils sont équivalents au lobe occipital dans le cerveau.

Comme mentionné, les réseaux de neurones récurrents sont utilisés pour résoudre des problèmes de séries temporelles. Ils peuvent apprendre des événements qui se sont produits lors des itérations précédentes récentes de leur phase d'entraînement. De cette manière, ils sont souvent comparés au lobe frontal du cerveau, qui alimente notre mémoire à court terme.

Pour résumer, les chercheurs associent souvent chacun des trois réseaux de neurones aux parties suivantes du cerveau :

* Réseaux de neurones artificiels : le lobe temporal
* Réseaux de neurones convolutifs : le lobe occipital
* Réseaux de neurones récurrents : le lobe frontal

## **La Composition d'un Réseau de Neurones Récurrent**

Discutons maintenant de la composition d'un réseau de neurones récurrent. Tout d'abord, rappelons que la composition d'un réseau de neurones de base a l'apparence suivante :

![Un réseau de neurones de base](https://nickmccullum.com/images/python-deep-learning/intuition-recurrent-neural-networks/basic-neural-network.png)

La première modification à apporter à ce réseau de neurones est que chaque couche du réseau doit être compressée ensemble, comme ceci :

![Un réseau de neurones compressé](https://nickmccullum.com/images/python-deep-learning/intuition-recurrent-neural-networks/squashed-neural-network.png)

Ensuite, trois autres modifications doivent être apportées :

* Les synapses des neurones du réseau de neurones doivent être simplifiées en une seule ligne
* L'ensemble du réseau de neurones doit être tourné de 90 degrés
* Une boucle doit être générée autour de la couche cachée du réseau de neurones

Le réseau de neurones aura maintenant l'apparence suivante :

![Un réseau de neurones récurrent](https://nickmccullum.com/images/python-deep-learning/intuition-recurrent-neural-networks/recurrent-neural-network.png)

Cette ligne qui entoure la couche cachée du réseau de neurones récurrent est appelée la boucle temporelle. Elle est utilisée pour indiquer que la couche cachée génère non seulement une sortie, mais que cette sortie est réinjectée en tant qu'entrée dans la même couche.

Une visualisation est utile pour comprendre cela. Comme vous pouvez le voir dans l'image suivante, la couche cachée utilisée sur une observation spécifique d'un ensemble de données est non seulement utilisée pour générer une sortie pour cette observation, mais elle est également utilisée pour entraîner la couche cachée de l'observation suivante.

![Un réseau de neurones récurrent de série temporelle](https://nickmccullum.com/images/python-deep-learning/intuition-recurrent-neural-networks/time-series-recurrent-neural-network.png)

Cette propriété d'une observation aidant à entraîner l'observation suivante est la raison pour laquelle les réseaux de neurones récurrents sont si utiles pour résoudre des problèmes d'analyse de séries temporelles.

## Résumé – L'Intuition des Réseaux de Neurones Récurrents

Dans ce tutoriel, vous avez eu votre première introduction aux réseaux de neurones récurrents. Plus spécifiquement, nous avons discuté de l'intuition derrière les réseaux de neurones récurrents.

Voici un bref résumé de ce que nous avons discuté dans ce tutoriel :

* Les types de problèmes résolus par les réseaux de neurones récurrents
* Les relations entre les différentes parties du cerveau et les différents réseaux de neurones que nous avons étudiés dans ce cours
* La composition d'un réseau de neurones récurrent et comment chaque couche cachée peut être utilisée pour aider à entraîner la couche cachée de l'observation suivante dans l'ensemble de données

# **Le Problème du Gradient Évanescent dans les Réseaux de Neurones Récurrents**

Le problème du gradient évanescent a historiquement été l'un des plus grands obstacles au succès des réseaux de neurones récurrents.

Pour cette raison, il est important de comprendre le problème du gradient évanescent avant de construire votre premier RNN.

Cette section expliquera le problème du gradient évanescent en anglais simple, y compris une discussion des solutions les plus utiles à ce problème intéressant.

## **Qu'est-ce que le Problème du Gradient Évanescent ?**

Avant de plonger dans les détails du problème du gradient évanescent, il est utile d'avoir une certaine compréhension de la manière dont le problème a été initialement découvert.

Le problème du gradient évanescent a été découvert par [Sepp Hochreiter](https://en.wikipedia.org/wiki/Sepp_Hochreiter), un informaticien allemand qui a joué un rôle influent dans le développement des réseaux de neurones récurrents en apprentissage profond.

Explorons maintenant le problème du gradient évanescent en détail. Comme son nom l'indique, le problème du gradient évanescent est lié aux algorithmes de descente de gradient en apprentissage profond. Rappelez-vous qu'un algorithme de descente de gradient ressemble à ceci :

![Un algorithme de descente de gradient finalisé](https://nickmccullum.com/images/python-deep-learning/gradient-descent/finalized-gradient-descent.png)

Cet algorithme de descente de gradient est ensuite combiné avec un algorithme de rétropropagation pour mettre à jour les poids des synapses dans tout le réseau de neurones.

Les réseaux de neurones récurrents se comportent légèrement différemment car la couche cachée d'une observation est utilisée pour entraîner la couche cachée de l'observation suivante.

![Un algorithme de descente de gradient de réseau de neurones récurrent](https://nickmccullum.com/images/python-deep-learning/vanishing-gradient-problem/rnn-backpropogation.png)

Cela signifie que la fonction de coût du réseau de neurones est calculée pour chaque observation dans l'ensemble de données. Ces valeurs de fonction de coût sont représentées en haut de l'image suivante :

![Un algorithme de descente de gradient de réseau de neurones récurrent](https://nickmccullum.com/images/python-deep-learning/vanishing-gradient-problem/rnn-cost-function.png)

Le problème du gradient évanescent se produit lorsque l'algorithme de rétropropagation se déplace en arrière à travers tous les neurones du réseau de neurones pour mettre à jour leurs poids. La nature des réseaux de neurones récurrents signifie que la fonction de coût calculée à une couche profonde du réseau de neurones sera utilisée pour changer les poids des neurones à des couches moins profondes.

Les mathématiques qui calculent ce changement sont multiplicatives, ce qui signifie que le gradient calculé dans une étape qui est profonde dans le réseau de neurones sera multiplié en arrière à travers les poids plus tôt dans le réseau. Autrement dit, le gradient calculé profondément dans le réseau est « dilué » lorsqu'il se déplace en arrière à travers le réseau, ce qui peut faire disparaître le gradient – donnant ainsi son nom au problème du gradient évanescent !

Le facteur réel qui est multiplié à travers un réseau de neurones récurrent dans l'algorithme de rétropropagation est représenté par la variable mathématique `Wrec`. Il pose deux problèmes :

* Lorsque `Wrec` est petit, vous rencontrez un problème de gradient évanescent
* Lorsque `Wrec` est grand, vous rencontrez un problème de gradient explosif

Notez que ces deux problèmes sont généralement appelés par le nom plus simple de « problème du gradient évanescent ».

Pour résumer, le problème du gradient évanescent est causé par la nature multiplicative de l'algorithme de rétropropagation. Cela signifie que les gradients calculés à une étape profonde du réseau de neurones récurrent ont soit un impact trop faible (dans un problème de gradient évanescent) soit un impact trop grand (dans un problème de gradient explosif) sur les poids des neurones qui sont moins profonds dans le réseau de neurones.

## **Comment Résoudre le Problème du Gradient Évanescent**

Il existe un certain nombre de stratégies qui peuvent être utilisées pour résoudre le problème du gradient évanescent. Nous explorerons des stratégies pour les problèmes de gradient évanescent et de gradient explosif séparément. Commençons par ce dernier.

### **Résolution du Problème du Gradient Explosif**

Pour les gradients explosifs, il est possible d'utiliser une version modifiée de l'algorithme de rétropropagation appelée `truncated backpropagation`. L'[algorithme de truncated backpropagation](https://machinelearningmastery.com/gentle-introduction-backpropagation-time/) limite le nombre de pas de temps sur lesquels la rétropropagation sera effectuée, arrêtant l'algorithme avant que le problème du gradient explosif ne se produise.

Vous pouvez également introduire des `pénalités`, qui sont des techniques codées en dur pour réduire l'impact d'une rétropropagation lorsqu'elle se déplace à travers des couches moins profondes dans un réseau de neurones.

Enfin, vous pourriez introduire un `clipping de gradient`, qui introduit un plafond artificiel qui limite la taille que le gradient peut atteindre dans un algorithme de rétropropagation.

### **Résolution du Problème du Gradient Évanescent**

L'initialisation des poids est une technique qui peut être utilisée pour résoudre le problème du gradient évanescent. Elle implique de créer artificiellement une valeur initiale pour les poids dans un réseau de neurones afin d'empêcher l'algorithme de rétropropagation d'attribuer des poids qui sont irréalistiquement petits.

Vous pourriez également utiliser des réseaux d'états écho, qui sont un type spécifique de réseau de neurones conçu pour éviter le problème du gradient évanescent. Les réseaux d'états écho sont hors du cadre de ce cours. Avoir connaissance de leur existence est suffisant pour l'instant.

La solution la plus importante au problème du gradient évanescent est un type spécifique de réseau de neurones appelé Long Short-Term Memory Networks (LSTMs), qui ont été pionniers par Sepp Hochreiter et [Jürgen Schmidhuber](https://en.wikipedia.org/wiki/J%C3%BCrgen_Schmidhuber). Rappelez-vous que M. Hochreiter était le scientifique qui a initialement découvert le problème du gradient évanescent.

Les LSTMs sont utilisés dans des problèmes principalement liés à la reconnaissance vocale, avec l'un des exemples les plus notables étant [Google utilisant un LSTM pour la reconnaissance vocale](https://googleblog.blogspot.com/2015/07/neon-prescription-or-rather-new.html) en 2015 et expérimentant une diminution de 49 % des erreurs de transcription.

Les LSTMs sont considérés comme le réseau de neurones de référence pour les scientifiques intéressés par la mise en œuvre de réseaux de neurones récurrents. Nous nous concentrerons largement sur les LSTMs pour le reste de ce cours.

## **Résumé – Le Problème du Gradient Évanescent**

Dans cette section, vous avez appris le problème du gradient évanescent des réseaux de neurones récurrents.

Voici un bref résumé de ce que nous avons discuté :

* Que Sepp Hochreiter était le premier scientifique à découvrir le problème du gradient évanescent dans les réseaux de neurones récurrents
* Ce que le problème du gradient évanescent (et son cousin, le problème du gradient explosif) implique
* Le rôle de `Wrec` dans les problèmes de gradient évanescent et de gradient explosif
* Comment les problèmes de gradient évanescent et de gradient explosif sont résolus
* Le rôle des LSTMs comme solution la plus courante au problème du gradient évanescent

# **Long Short-Term Memory Networks (LSTMs)**

Les réseaux de mémoire à long court terme (LSTMs) sont un type de réseau de neurones récurrent utilisé pour résoudre [le problème du gradient évanescent](https://nickmccullum.com/python-deep-learning/vanishing-gradient-problem/).

Ils diffèrent des réseaux de neurones récurrents « réguliers » de manière importante.

Ce tutoriel vous présentera les LSTMs. Plus tard dans ce cours, nous construirons et entraînerons un LSTM à partir de zéro.

## **Table des Matières**

Vous pouvez sauter à une section spécifique de ce tutoriel LSTM en utilisant la table des matières ci-dessous :

* [L'Histoire des LSTMs](https://nickmccullum.com/python-deep-learning/lstms-long-short-term-memory-networks/#the-history-of-lstms)
* [Comment les LSTMs Résolvent le Problème du Gradient Évanescent](https://nickmccullum.com/python-deep-learning/lstms-long-short-term-memory-networks/#how-lstms-solve-the-vanishing-gradient-problem)
* [Comment Fonctionnent les LSTMs](https://nickmccullum.com/python-deep-learning/lstms-long-short-term-memory-networks/#how-lstms-work)
* [Variations des Architectures LSTM](https://nickmccullum.com/python-deep-learning/lstms-long-short-term-memory-networks/#variations-of-lstm-architectures)
* [La Variation Peephole](https://nickmccullum.com/python-deep-learning/lstms-long-short-term-memory-networks/#the-peephole-variation)
* [La Variation Coupled Gate](https://nickmccullum.com/python-deep-learning/lstms-long-short-term-memory-networks/#the-coupled-gate-variation)
* [Autres Variations LSTM](https://nickmccullum.com/python-deep-learning/lstms-long-short-term-memory-networks/#other-lstm-variations)
* [Pensées Finales](https://nickmccullum.com/python-deep-learning/lstms-long-short-term-memory-networks/#final-thoughts)

## **L'Histoire des LSTMs**

Comme nous l'avons mentionné dans la dernière section, les deux figures les plus importantes dans le domaine des LSTMs sont [Sepp Hochreiter](https://en.wikipedia.org/wiki/Sepp_Hochreiter) et [Jürgen Schmidhuber](https://en.wikipedia.org/wiki/J%C3%BCrgen_Schmidhuber).

Ce dernier était le directeur de thèse du premier à l'Université Technique de Munich en Allemagne.

La thèse de doctorat de Hochreiter a introduit les LSTMs au monde pour la première fois.

## **Comment les LSTMs Résolvent le Problème du Gradient Évanescent**

Dans le dernier tutoriel, nous avons appris comment le terme `Wrec` dans l'algorithme de rétropropagation peut conduire soit à un problème de gradient évanescent, soit à un problème de gradient explosif.

Nous avons exploré diverses solutions possibles à ce problème, y compris les pénalités, le clipping de gradient, et même les réseaux d'états écho. Les LSTMs sont la meilleure solution.

Alors, comment fonctionnent les LSTMs ? Ils changent simplement la valeur de `Wrec`.

Dans notre explication du problème du gradient évanescent, vous avez appris que :

* Lorsque `Wrec` est petit, vous rencontrez un problème de gradient évanescent
* Lorsque `Wrec` est grand, vous rencontrez un problème de gradient explosif

Nous pouvons en fait être beaucoup plus spécifiques :

* Lorsque `Wrec < 1`, vous rencontrez un problème de gradient évanescent
* Lorsque `Wrec > 1`, vous rencontrez un problème de gradient explosif

Cela a du sens si vous pensez à la nature multiplicative de l'algorithme de rétropropagation.

Si vous avez un nombre qui est inférieur à `1` et que vous le multipliez contre lui-même encore et encore, vous finirez par obtenir un nombre qui disparaît. De même, multiplier un nombre supérieur à `1` contre lui-même de nombreuses fois donne un nombre très grand.

Pour résoudre ce problème, les LSTMs définissent `Wrec = 1`. Il y a certainement plus à dire sur les LSTMs que de définir `Wrec = 1`, mais c'est définitivement le changement le plus important que cette spécification de réseaux de neurones récurrents apporte.

## **Comment Fonctionnent les LSTMs**

Cette section expliquera comment fonctionnent les LSTMs. Avant de continuer, il est utile de mentionner que je vais utiliser des images de l'article de blog de Christopher Olah [Understanding LSTMs](https://colah.github.io/posts/2015-08-Understanding-LSTMs/), qui a été publié en août 2015 et contient certaines des meilleures visualisations LSTM que j'ai jamais vues.

Pour commencer, considérons la version de base d'un réseau de neurones récurrent :

![Un réseau de neurones récurrent de base](https://nickmccullum.com/images/python-deep-learning/lstms/recurrent-neural-network.png)

Ce réseau de neurones possède des neurones et des synapses qui transmettent les sommes pondérées des sorties d'une couche en tant qu'entrées de la couche suivante. Un algorithme de rétropropagation se déplacera en arrière à travers cet algorithme et mettra à jour les poids de chaque neurone en réponse à la fonction de coût calculée à chaque époque de sa phase d'entraînement.

En revanche, voici à quoi ressemble un LSTM :

![Un LSTM](https://nickmccullum.com/images/python-deep-learning/lstms/lstm.png)

Comme vous pouvez le voir, un LSTM a une complexité intégrée bien plus grande qu'un réseau de neurones récurrent régulier. Mon objectif est de vous permettre de comprendre pleinement cette image d'ici la fin de ce tutoriel.

Tout d'abord, familiarisons-nous avec la notation utilisée dans l'image ci-dessus :

![La notation que nous utiliserons dans notre tutoriel LSTM](https://nickmccullum.com/images/python-deep-learning/lstms/lstm-notation.png)

Maintenant que vous avez une idée de la notation que nous utiliserons dans ce tutoriel LSTM, nous pouvons commencer à examiner la fonctionnalité d'une couche au sein d'un réseau de neurones LSTM. Chaque couche a l'apparence suivante :

![Un nœud d'un réseau de neurones LSTM](https://nickmccullum.com/images/python-deep-learning/lstms/lstm-node.png)

Avant de plonger dans la fonctionnalité des nœuds au sein d'un réseau de neurones LSTM, il est utile de noter que chaque entrée et sortie de ces modèles d'apprentissage profond est un vecteur. En Python, cela est généralement représenté par un [tableau NumPy](https://nickmccullum.com/advanced-python/numpy-arrays/) ou une autre structure de données unidimensionnelle.

La première chose qui se produit au sein d'un LSTM est la [fonction d'activation](https://nickmccullum.com/python-deep-learning/deep-learning-activation-functions/) de la `couche de porte d'oubli`. Elle examine les entrées de la couche (étiquetées `xt` pour l'observation et `ht` pour la sortie de la couche précédente du réseau de neurones) et produit soit `1` soit `0` pour chaque nombre dans l'état de cellule de la couche précédente (étiqueté `Ct-1`).

Voici une visualisation de l'activation de la `couche de porte d'oubli` :

![Un nœud d'un réseau de neurones LSTM](https://nickmccullum.com/images/python-deep-learning/lstms/lstm-node-1.png)

Nous n'avons pas encore discuté de l'état de cellule, alors faisons-le maintenant. L'état de cellule est représenté dans notre diagramme par la longue ligne horizontale qui traverse le haut du diagramme. Par exemple, voici l'état de cellule dans nos visualisations :

![État de cellule dans les réseaux LSTM](https://nickmccullum.com/images/python-deep-learning/lstms/cell-state.png)

Le but de l'état de cellule est de décider quelles informations faire passer des différentes observations sur lesquelles un réseau de neurones récurrent est entraîné. La décision de faire passer ou non des informations est prise par des `portes` - dont la `porte d'oubli` est un exemple principal. Chaque porte au sein d'un LSTM aura l'apparence suivante :

![État de cellule dans les réseaux LSTM](https://nickmccullum.com/images/python-deep-learning/lstms/cell-state.png)

Le caractère `c3` au sein de ces portes fait référence à la fonction Sigmoid, que vous avez probablement vue utilisée dans les [modèles de machine learning de régression logistique](https://nickmccullum.com/python-machine-learning/logistic-regression-python/). La fonction sigmoid est utilisée comme un type de fonction d'activation dans les LSTMs qui détermine quelles informations sont transmises à travers une porte pour affecter l'état de cellule du réseau.

Par définition, la fonction Sigmoid ne peut produire que des nombres entre `0` et `1`. Elle est souvent utilisée pour calculer des probabilités pour cette raison. Dans le cas des modèles LSTM, elle spécifie quelle proportion de chaque sortie doit être autorisée à influencer l'état de cellule.

Les deux étapes suivantes d'un modèle LSTM sont étroitement liées : la `couche de porte d'entrée` et la `couche tanh`. Ces couches travaillent ensemble pour déterminer comment mettre à jour l'état de cellule. En même temps, la dernière étape est complétée, ce qui permet à la cellule de déterminer quoi oublier de la dernière observation dans l'ensemble de données.

Voici une visualisation de ce processus :

![Un nœud d'un réseau de neurones LSTM](https://nickmccullum.com/images/python-deep-learning/lstms/lstm-node-2.png)

La dernière étape d'un LSTM détermine la sortie pour cette observation (dénotée `ht`). Cette étape passe à la fois par une fonction sigmoid et une fonction tangente hyperbolique. Elle peut être visualisée comme suit :

![Un nœud d'un réseau de neurones LSTM](https://nickmccullum.com/images/python-deep-learning/lstms/lstm-node-3.png)

Cela conclut le processus d'entraînement d'une seule couche d'un modèle LSTM. Comme vous pouvez l'imaginer, il y a beaucoup de mathématiques sous la surface que nous avons survécu. Le but de cette section est d'expliquer largement comment fonctionnent les LSTMs, pas pour que vous compreniez profondément chaque opération du processus.

## **Variations des Architectures LSTM**

Je voulais conclure ce tutoriel en discutant de quelques variations différentes de l'architecture LSTM qui sont légèrement différentes du LSTM de base que nous avons discuté jusqu'à présent.

Pour un bref rappel, voici à quoi ressemble un nœud généralisé d'un LSTM :

![Un nœud d'un réseau de neurones LSTM](https://nickmccullum.com/images/python-deep-learning/lstms/lstm-node.png)

### **La Variation Peephole**

Peut-être la variation la plus importante de l'architecture LSTM est la variante `peephole`, qui permet aux couches de porte de lire les données de l'état de cellule.

Voici une visualisation de ce à quoi pourrait ressembler la variante peephole :

![Un nœud d'un réseau de neurones LSTM peephole](https://nickmccullum.com/images/python-deep-learning/lstms/peephole-lstm-node.png)

Notez que bien que ce diagramme ajoute un peephole à chaque porte du réseau de neurones récurrent, vous pourriez également ajouter des peepholes à certaines portes et pas à d'autres.

### **La Variation Coupled Gate**

Il existe une autre variation de l'architecture LSTM où le modèle prend la décision de ce qu'il faut oublier et de ce qu'il faut ajouter de nouvelles informations ensemble. Dans le modèle LSTM original, ces décisions étaient prises séparément.

Voici une visualisation de ce à quoi ressemble cette architecture :

![Un nœud d'un réseau de neurones LSTM à porte couplée](https://nickmccullum.com/images/python-deep-learning/lstms/coupled-gate-lstm-node.png)

## **Autres Variations LSTM**

Ce ne sont que deux exemples de variantes de l'architecture LSTM. Il en existe beaucoup d'autres. Quelques-unes sont listées ci-dessous :

* [Gated Recurrent Units (GRUs)](https://en.wikipedia.org/wiki/Gated_recurrent_unit)
* [Depth Gated RNNs](https://arxiv.org/abs/1508.03790)
* [Clockwork RNNs](https://arxiv.org/abs/1402.3511)

## **Résumé - Long Short-Term Memory Networks**

Dans ce tutoriel, vous avez eu votre première exposition aux réseaux de mémoire à long court terme (LSTMs).

Voici un bref résumé de ce que vous avez appris :

* Une (très) brève histoire des LSTMs et le rôle que Sepp Hochreiter et Jürgen Schmidhuber ont joué dans leur développement
* Comment les LSTMs résolvent le problème du gradient évanescent
* Comment fonctionnent les LSTMs
* Le rôle des portes, des fonctions sigmoïdes et de la fonction tangente hyperbolique dans les LSTMs
* Quelques-unes des variations les plus populaires de l'architecture LSTM

# **Comment Construire et Entraîner un Réseau de Neurones Récurrent**

Jusqu'à présent dans notre discussion sur les réseaux de neurones récurrents, vous avez appris :

* L'intuition de base derrière les [réseaux de neurones récurrents](https://nickmccullum.com/python-deep-learning/intuition-recurrent-neural-networks/)
* Le [problème du gradient évanescent](https://nickmccullum.com/python-deep-learning/vanishing-gradient-problem/) qui a historiquement entravé le progrès des réseaux de neurones récurrents
* Comment les [réseaux de mémoire à long court terme (LSTMs)](https://nickmccullum.com/python-deep-learning/lstms-long-short-term-memory-networks/) aident à résoudre le problème du gradient évanescent

Il est maintenant temps de construire votre premier réseau de neurones récurrent ! Plus spécifiquement, ce tutoriel vous enseignera comment construire et entraîner un LSTM pour prédire le prix de l'action de Facebook (FB).

## **Table des Matières**

Vous pouvez sauter à une section spécifique de ce tutoriel Python sur les réseaux de neurones récurrents en utilisant la table des matières ci-dessous :

* [Téléchargement de l'ensemble de données pour ce tutoriel](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/#downloading-the-data-set-for-this-tutorial)
* [Importation des bibliothèques dont vous aurez besoin pour ce tutoriel](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/#importing-the-libraries-you-ll-need-for-this-tutorial)
* [Importation de notre ensemble d'entraînement dans le script Python](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/#importing-our-training-set-into-the-python-script)
* [Application de la mise à l'échelle des caractéristiques à notre ensemble de données](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/#applying-feature-scaling-to-our-data-set)
* [Spécification du nombre de pas de temps pour notre réseau de neurones récurrent](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/#specifying-the-number-of-timesteps-for-our-recurrent-neural-network)
* [Finalisation de nos ensembles de données en les transformant en tableaux NumPy](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/#finalizing-our-data-sets-by-transforming-them-into-numpy-arrays)
* [Importation de nos bibliothèques TensorFlow](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/#importing-our-tensorflow-libraries)
* [Construction de notre réseau de neurones récurrent](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/#building-our-recurrent-neural-network)
* [Ajout de notre première couche LSTM](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/#adding-our-first-lstm-layer)
* [Ajout de Dropout Regularization](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/#adding-some-dropout-regularization)
* [Ajout de trois autres couches LSTM avec Dropout Regularization](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/#adding-three-more-lstm-layers-with-dropout-regularization)
* [Ajout de la couche de sortie à notre réseau de neurones récurrent](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/#adding-the-output-layer-to-our-recurrent-neural-network)
* [Compilation de notre réseau de neurones récurrent](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/#compiling-our-recurrent-neural-network)
* [Ajustement du réseau de neurones récurrent sur l'ensemble d'entraînement](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/#fitting-the-recurrent-neural-network-on-the-training-set)
* [Faire des prédictions avec notre réseau de neurones récurrent](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/#making-predictions-with-our-recurrent-neural-network)
* [Importation de nos données de test](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/#importing-our-test-data)
* [Construction de l'ensemble de données de test dont nous avons besoin pour faire des prédictions](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/#building-the-test-data-set-we-need-to-make-predictions)
* [Mise à l'échelle de nos données de test](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/#scaling-our-test-data)
* [Regroupement de nos données de test](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/#grouping-our-test-data)
* [Faire des prédictions](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/#actually-making-predictions)
* [Le code complet pour ce tutoriel](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/#the-full-code-for-this-tutorial)
* [Pensées finales](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/#final-thoughts)

## **Téléchargement de l'ensemble de données pour ce tutoriel**

Pour suivre ce tutoriel, vous devrez télécharger deux ensembles de données :

* Un ensemble de données d'entraînement contenant des informations sur le prix de l'action de Facebook du début de 2015 à la fin de 2019
* Un ensemble de données de test contenant des informations sur le prix de l'action de Facebook pendant le premier mois de 2020

Notre réseau de neurones récurrent sera entraîné sur les données de 2015-2019 et sera utilisé pour prédire les données de janvier 2020.

Vous pouvez télécharger les données d'entraînement et de test en utilisant les liens ci-dessous :

* [Données d'entraînement](https://nickmccullum.com/files/recurrent-neural-networks/FB_training_data.csv)
* [Données de test](https://nickmccullum.com/files/recurrent-neural-networks/FB_test_data.csv)

Chacun de ces ensembles de données est simplement des exports de Yahoo! Finance. Ils ressemblent à ceci (lorsqu'ils sont ouverts dans Microsoft Excel) :

![Un exemple d'ensemble de données que nous utiliserons pour entraîner notre réseau de neurones récurrent](https://nickmccullum.com/images/python-deep-learning/recurrent-neural-networks/excel-file.png)

Une fois les fichiers téléchargés, déplacez-les dans le répertoire dans lequel vous souhaitez travailler et ouvrez un [Jupyter Notebook](https://nickmccullum.com/python-course/jupyter-notebook-basics/).

## **Importation des bibliothèques dont vous aurez besoin pour ce tutoriel**

Ce tutoriel dépendra de plusieurs bibliothèques Python open-source, notamment [NumPy](https://nickmccullum.com/advanced-python/numpy/), [pandas](https://nickmccullum.com/advanced-python/pandas/), et [matplotlib](https://nickmccullum.com/python-visualization/how-to-import-matplotlib/).

Commençons notre script Python en important certaines de ces bibliothèques :

```py

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt


```

## **Importation de notre ensemble d'entraînement dans le script Python**

La prochaine tâche à accomplir est d'importer notre ensemble de données dans le script Python.

Nous importerons initialement l'ensemble de données en tant que [DataFrame pandas](https://nickmccullum.com/advanced-python/pandas-dataframes/) en utilisant la méthode `read_csv`. Cependant, puisque le module `keras` de `TensorFlow` n'accepte que les [tableaux NumPy](https://nickmccullum.com/advanced-python/numpy-arrays/) en tant que paramètres, la structure de données devra être transformée après l'importation.

Commençons par importer l'ensemble du fichier `.csv` en tant que DataFrame :

```py

training_data = pd.read_csv('FB_training_data.csv')


```

Vous remarquerez en regardant le DataFrame qu'il contient de nombreuses façons différentes de mesurer le prix de l'action de Facebook, y compris le prix d'ouverture, le prix de clôture, les prix haut et bas, et les informations de volume :

![Un exemple d'ensemble de données que nous utiliserons pour entraîner notre réseau de neurones récurrent](https://nickmccullum.com/images/python-deep-learning/recurrent-neural-networks/training_data.png)

Nous devrons sélectionner un type spécifique de prix de l'action avant de continuer. Utilisons `Close`, qui indique le prix de clôture non ajusté de l'action de Facebook.

Maintenant, nous devons sélectionner cette colonne du DataFrame et la stocker dans un tableau NumPy. Voici la commande pour le faire :

```py

training_data = training_data.iloc[:, 1].values


```

Notez que cette commande écrase la variable `training_data` existante que nous avions créée précédemment.

Vous pouvez maintenant vérifier que notre variable `training_data` est bien un tableau NumPy en exécutant `type(training_data)`, qui devrait retourner :

```py

numpy.ndarray


```

## **Application de la mise à l'échelle des caractéristiques à notre ensemble de données**

Prenons maintenant le temps d'appliquer une mise à l'échelle des caractéristiques à notre ensemble de données.

Pour un bref rappel, il existe deux principales façons d'appliquer la mise à l'échelle des caractéristiques à votre ensemble de données :

* Standardisation
* Normalisation

Nous utiliserons la normalisation pour construire notre réseau de neurones récurrent, ce qui implique de soustraire la valeur minimale de l'ensemble de données puis de diviser par la plage de l'ensemble de données.

Voici la fonction de normalisation définie mathématiquement :

![Équation de normalisation de la mise à l'échelle des caractéristiques](https://nickmccullum.com/images/python-deep-learning/recurrent-neural-networks/normalization.jpg)

Heureusement, `scikit-learn` rend très facile l'application de la normalisation à un ensemble de données en utilisant sa classe `MinMaxScaler`.

Commençons par importer cette classe dans notre script Python. La classe `MinMaxScaler` se trouve dans le module `preprocessing` de `scikit-learn`, donc la commande pour importer la classe est :

```py

from sklearn.preprocessing import MinMaxScaler


```

Ensuite, nous devons créer une instance de cette classe. Nous assignerons le nouvel objet créé à une variable appelée `scaler`. Nous utiliserons les paramètres par défaut pour cette classe, donc nous n'avons pas besoin de passer quoi que ce soit :

```py

scaler = MinMaxScaler()


```

Puisque nous n'avons pas spécifié de paramètres non par défaut, cela mettra à l'échelle notre ensemble de données de sorte que chaque observation soit entre `0` et `1`.

Nous avons créé notre objet `scaler` mais notre ensemble de données `training_data` n'a pas encore été mis à l'échelle. Nous devons utiliser la méthode `fit_transform` pour modifier l'ensemble de données original. Voici l'instruction pour le faire :

```py

training_data = scaler.fit_transform(training_data.reshape(-1, 1))


```

## **Spécification du nombre de pas de temps pour notre réseau de neurones récurrent**

La prochaine chose que nous devons faire est de spécifier notre nombre de `timesteps`. Les [timesteps](https://machinelearningmastery.com/use-timesteps-lstm-networks-time-series-forecasting/) spécifient combien d'observations précédentes doivent être considérées lorsque le réseau de neurones récurrent fait une prédiction sur l'observation actuelle.

Nous utiliserons `40` timesteps dans ce tutoriel. Cela signifie que pour chaque jour que le réseau de neurones prédit, il considérera les 40 jours précédents de prix des actions pour déterminer sa sortie. Notez que puisque il y a seulement ~20 jours de trading dans un mois donné, utiliser 40 timesteps signifie que nous nous basons sur les données de prix des actions des 2 mois précédents.

Alors, comment spécifions-nous le nombre de timesteps dans notre script Python ?

Cela se fait en créant deux structures de données spéciales :

* Une structure de données que nous appellerons `x_training_data` qui contient les 40 dernières observations de prix des actions dans l'ensemble de données. Ce sont les données que le réseau de neurones récurrent utilisera pour faire des prédictions.
* Une structure de données que nous appellerons `y_training_data` qui contient le prix de l'action pour le jour de trading suivant. C'est le point de données que le réseau de neurones récurrent essaie de prédire.

Pour commencer, initialisons chacune de ces structures de données en tant que liste Python vide :

```py

x_training_data = []

y_training_data =[]


```

Maintenant, nous utiliserons une boucle for pour remplir les données réelles dans chacune de ces listes Python. Voici le code (avec une explication supplémentaire du code après le bloc de code) :

```py

for i in range(40, len(training_data)):

    x_training_data.append(training_data[i-40:i, 0])

    y_training_data.append(training_data[i, 0])


```

Décomposons les composants de ce bloc de code :

* La fonction `range(40, len(training_data))` fait en sorte que la boucle for itère de `40` à l'index final des données d'entraînement.
* La ligne `x_training_data.append(training_data[i-40:i, 0])` fait en sorte que la boucle ajoute les 40 prix des actions précédents à `x_training_data` à chaque itération de la boucle.
* De même, `y_training_data.append(training_data[i, 0])` fait en sorte que la boucle ajoute le prix de l'action du lendemain à `y_training_data` à chaque itération de la boucle.

## **Finalisation de nos ensembles de données en les transformant en tableaux NumPy**

TensorFlow est conçu pour fonctionner principalement avec des tableaux NumPy. Pour cette raison, la dernière chose que nous devons faire est de transformer les deux listes Python que nous venons de créer en tableaux NumPy.

Heureusement, c'est simple. Vous devez simplement envelopper les listes Python dans la fonction `np.array`. Voici le code :

```py

x_training_data = np.array(x_training_data)

y_training_data = np.array(y_training_data)


```

Une façon importante de vous assurer que votre script fonctionne comme prévu est de vérifier la forme des deux tableaux NumPy.

Le tableau `x_training_data` doit être un tableau NumPy bidirectionnel avec une dimension étant `40` (le nombre de timesteps) et la deuxième dimension étant `len(training_data) - 40`, qui évalue à `1218` dans notre cas.

De même, l'objet `y_training_data` doit être un tableau NumPy unidimensionnel de longueur `1218` (qui, encore une fois, est `len(training_data) - 40`).

Vous pouvez vérifier la forme des tableaux en imprimant leur attribut `shape`, comme ceci :

```py

print(x_training_data.shape)

print(y_training_data.shape)


```

Cela imprime :

```py

(1218, 40)

(1218,)


```

Les deux tableaux ont les dimensions que vous attendiez. Cependant, nous devons remodeler notre objet `x_training_data` une fois de plus avant de procéder à la construction de notre réseau de neurones récurrent.

La raison en est que la couche de réseau de neurones récurrent disponible dans TensorFlow n'accepte les données que dans un format très spécifique. Vous pouvez lire la documentation TensorFlow sur ce sujet [ici](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RNN#input_shape).

Pour remodeler l'objet `x_training_data`, j'utiliserai la méthode [np.reshape](https://nickmccullum.com/numpy-np-reshape/). Voici le code pour le faire :

```py

x_training_data = np.reshape(x_training_data, (x_training_data.shape[0], 

                                               x_training_data.shape[1], 

                                               1))


```

Maintenant, imprimons la forme de `x_training_data` une fois de plus :

```py

print(x_training_data.shape)


```

Cela produit :

```py

(1218, 40, 1)


```

Nos tableaux ont la forme souhaitée, nous pouvons donc procéder à la construction de notre réseau de neurones récurrent.

## **Importation de nos bibliothèques TensorFlow**

Avant de pouvoir commencer à construire notre réseau de neurones récurrent, nous devons importer un certain nombre de classes de TensorFlow. Voici les instructions que vous devez exécuter avant de continuer :

```py

from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import Dense

from tensorflow.keras.layers import LSTM

from tensorflow.keras.layers import Dropout


```

## **Construction de notre réseau de neurones récurrent**

Il est maintenant temps de construire notre réseau de neurones récurrent.

La première chose à faire est d'initialiser un objet de la classe `Sequential` de TensorFlow. Comme son nom l'indique, la classe `Sequential` est conçue pour construire des réseaux de neurones en ajoutant des séquences de couches au fil du temps.

Voici le code pour initialiser notre réseau de neurones récurrent :

```py

rnn = Sequential()


```

Comme pour nos [réseaux de neurones artificiels](https://nickmccullum.com/python-deep-learning/artificial-neural-network-tutorial/) et [réseaux de neurones convolutifs](https://nickmccullum.com/python-deep-learning/convolutional-neural-network-tutorial/), nous pouvons ajouter plus de couches à ce réseau de neurones récurrent en utilisant la méthode `add`.

## **Ajout de notre première couche LSTM**

La première couche que nous ajouterons est une couche [LSTM](https://nickmccullum.com/python-deep-learning/lstms-long-short-term-memory-networks/). Pour ce faire, passez une invocation de la classe `LSTM` (que nous venons d'importer) dans la méthode `add`.

La classe `LSTM` accepte plusieurs paramètres. Plus précisément, nous spécifierons trois arguments :

* Le nombre de neurones LSTM que vous souhaitez inclure dans cette couche. Augmenter le nombre de neurones est une méthode pour augmenter la dimensionnalité de votre réseau de neurones récurrent. Dans notre cas, nous spécifierons `units = 45`.
* `return_sequences = True` - cela doit toujours être spécifié si vous prévoyez d'inclure une autre couche LSTM après celle que vous ajoutez. Vous devez spécifier `return_sequences = False` pour la dernière couche LSTM de votre réseau de neurones récurrent.
* `input_shape` : le nombre de timesteps et le nombre de prédicteurs dans nos données d'entraînement. Dans notre cas, nous utilisons `40` timesteps et seulement `1` prédicteur (prix de l'action), donc nous ajouterons

Voici la méthode `add` complète :

```py

rnn.add(LSTM(units = 45, return_sequences = True, input_shape = (x_training_data.shape[1], 1)))


```

Notez que j'ai utilisé `x_training_data.shape[1]` au lieu de la valeur codée en dur au cas où nous déciderions d'entraîner le réseau de neurones récurrent sur un modèle plus grand à une date ultérieure.

## **Ajout de Dropout Regularization**

La [Dropout Regularization](https://machinelearningmastery.com/dropout-for-regularizing-deep-neural-networks/) est une technique utilisée pour éviter le surapprentissage lors de l'entraînement des réseaux de neurones.

Elle implique l'exclusion aléatoire - ou le « dropout » - de certaines sorties de couche pendant la phase d'entraînement.

TensorFlow facilite la mise en œuvre de la dropout regularization en utilisant la classe `Dropout` que nous avons importée plus tôt dans notre script Python. La classe `Dropout` accepte un seul paramètre : le taux de dropout.

Le taux de dropout indique combien de neurones doivent être abandonnés dans une couche spécifique du réseau de neurones. Il est courant d'utiliser un taux de dropout de 20 %. Nous suivrons cette convention dans notre réseau de neurones récurrent.

Voici comment vous pouvez demander à TensorFlow d'abandonner 20 % des neurones de la couche LSTM pendant chaque itération de la phase d'entraînement :

```py

rnn.add(Dropout(0.2))


```

## **Ajout de trois autres couches LSTM avec Dropout Regularization**

Nous allons maintenant ajouter trois autres couches LSTM (avec dropout regularization) à notre réseau de neurones récurrent. Vous verrez qu'après avoir spécifié la première couche LSTM, l'ajout de plus de couches est trivial.

Pour ajouter plus de couches, tout ce qui doit être fait est de copier les deux premières méthodes `add` avec un petit changement. À savoir, nous devons supprimer l'argument `input_shape` de la classe `LSTM`.

Nous garderons le nombre de neurones (ou `units`) et le taux de dropout identiques dans chacune des invocations de la classe `LSTM`. Puisque la troisième couche `LSTM` que nous ajoutons dans cette section sera notre dernière couche LSTM, nous pouvons supprimer le paramètre `return_sequences = True` comme mentionné précédemment. La suppression du paramètre définit `return_sequences` à sa valeur par défaut `False`.

Voici le code complet pour ajouter nos trois prochaines couches LSTM :

```py

rnn.add(LSTM(units = 45, return_sequences = True))

rnn.add(Dropout(0.2))

rnn.add(LSTM(units = 45, return_sequences = True))

rnn.add(Dropout(0.2))

rnn.add(LSTM(units = 45))

rnn.add(Dropout(0.2))


```

Ce code est très répétitif et viole le principe DRY (Don't repeat yourself) du développement logiciel. Mettons-le plutôt dans une boucle :

```py

for i in [True, True, False]:

    rnn.add(LSTM(units = 45, return_sequences = i))

    rnn.add(Dropout(0.2))


```

## **Ajout de la couche de sortie à notre réseau de neurones récurrent**

Terminons l'architecture de notre réseau de neurones récurrent en ajoutant notre couche de sortie.

La couche de sortie sera une instance de la classe `Dense`, qui est la même classe que nous avons utilisée pour créer [la couche de connexion complète](https://nickmccullum.com/python-deep-learning/flattening-full-connection/) de notre réseau de neurones convolutif plus tôt dans ce cours.

Le seul paramètre que nous devons spécifier est `units`, qui est le nombre de dimensions souhaité que la couche de sortie doit générer. Puisque nous voulons sortir le prix de l'action du lendemain (une seule valeur), nous spécifierons `units = 1`.

Voici le code pour créer notre couche de sortie :

```py

rnn.add(Dense(units = 1))


```

## **Compilation de notre réseau de neurones récurrent**

Comme vous vous en souviendrez des tutoriels sur les réseaux de neurones artificiels et les réseaux de neurones convolutifs, l'étape de compilation de la construction d'un réseau de neurones est celle où nous spécifions l'optimiseur et la fonction de perte du réseau de neurones.

TensorFlow nous permet de compiler un réseau de neurones en utilisant la méthode nommée de manière appropriée `compile`. Elle accepte deux arguments : `optimizer` et `loss`. Commençons par créer une fonction `compile` vide :

```py

rnn.compile(optimizer = '', loss = '')


```

Nous devons maintenant spécifier les paramètres `optimizer` et `loss`.

Commençons par discuter du paramètre `optimizer`. Les réseaux de neurones récurrents utilisent généralement l'optimiseur RMSProp dans leur étape de compilation. Cela dit, nous utiliserons l'optimiseur Adam (comme avant). L'optimiseur Adam est un optimiseur polyvalent qui est utile dans une grande variété d'architectures de réseaux de neurones.

Le paramètre `loss` est assez simple. Puisque nous prédisons une variable continue, nous pouvons utiliser l'erreur quadratique moyenne - tout comme vous le feriez lors de la mesure de la performance d'un [modèle de machine learning de régression linéaire](https://nickmccullum.com/python-machine-learning/linear-regression-python/). Cela signifie que nous pouvons spécifier `loss = mean_squared_error`.

Voici la méthode `compile` finale :

```py

rnn.compile(optimizer = 'adam', loss = 'mean_squared_error')


```

## **Ajustement du réseau de neurones récurrent sur l'ensemble d'entraînement**

Il est maintenant temps d'entraîner notre réseau récurrent sur nos données d'entraînement.

Pour ce faire, nous utilisons la méthode `fit`. La méthode `fit` accepte quatre arguments dans ce cas :

* **Les données d'entraînement** : dans notre cas, ce sera `x_training_data` et `y_training_data`
* **Époques** : le nombre d'itérations que vous souhaitez que le réseau de neurones récurrent soit entraîné. Nous spécifierons `epochs = 100` dans ce cas.
* **La taille du lot** : la taille des lots dans lesquels le réseau sera entraîné à chaque époque.

Voici le code pour entraîner ce réseau de neurones récurrent selon nos spécifications :

```py

rnn.fit(x_training_data, y_training_data, epochs = 100, batch_size = 32)


```

Votre Jupyter Notebook générera maintenant un certain nombre de sorties imprimées pour chaque époque dans l'algorithme d'entraînement. Elles ressemblent à ceci :

![Sorties d'entraînement de machine learning](https://nickmccullum.com/images/python-deep-learning/recurrent-neural-networks/training.png)

Comme vous pouvez le voir, chaque sortie montre combien de temps l'époque a pris à calculer ainsi que la fonction de perte calculée à cette époque.

Vous devriez voir la valeur de la fonction de perte lentement diminuer à mesure que le réseau de neurones récurrent est ajusté aux données d'entraînement au fil du temps. Dans mon cas, la valeur de la fonction de perte est passée de `0.0504` lors de la première itération à `0.0017` lors de la dernière itération.

## **Faire des prédictions avec notre réseau de neurones récurrent**

Nous avons construit notre réseau de neurones récurrent et l'avons entraîné sur les données du prix de l'action de Facebook au cours des 5 dernières années. Il est maintenant temps de faire quelques prédictions !

### **Importation de nos données de test**

Pour commencer, importons les données réelles du prix de l'action pour le premier mois de 2020. Cela nous donnera quelque chose à comparer avec nos valeurs prédites.

Voici le code pour le faire. Notez qu'il est très similaire au code que nous avons utilisé pour importer nos données d'entraînement au début de notre script Python :

```py

test_data = pd.read_csv('FB_test_data.csv')

test_data = test_data.iloc[:, 1].values


```

Si vous exécutez l'instruction `print(test_data.shape)`, elle retournera `(21,)`. Cela montre que nos données de test sont un tableau NumPy unidimensionnel avec 21 entrées - ce qui signifie qu'il y avait 21 jours de trading en bourse en janvier 2020.

Vous pouvez également générer un graphique rapide des données en utilisant `plt.plot(test_data)`. Cela devrait générer la visualisation Python suivante :

![Une visualisation de nos données de test](https://nickmccullum.com/images/python-deep-learning/recurrent-neural-networks/test_data.png)

Avec un peu de chance, nos valeurs prédites devraient suivre la même distribution.

### **Construction de l'ensemble de données de test dont nous avons besoin pour faire des prédictions**

Avant de pouvoir faire des prédictions pour le prix de l'action de Facebook en janvier 2020, nous devons d'abord apporter quelques modifications à notre ensemble de données.

La raison en est que pour prédire chacune des `21` observations de janvier, nous aurons besoin des `40` jours de trading précédents. Certains de ces jours de trading proviendront de l'ensemble de test tandis que le reste proviendra de l'ensemble d'entraînement. Pour cette raison, une certaine [concaténation](https://nickmccullum.com/advanced-python/how-to-concatenate-pandas-dataframes/) est nécessaire.

Malheureusement, vous ne pouvez pas simplement concaténer les tableaux NumPy immédiatement. Cela est dû au fait que nous avons déjà appliqué une mise à l'échelle des caractéristiques aux données d'entraînement mais que nous n'avons pas appliqué de mise à l'échelle des caractéristiques aux données de test.

Pour corriger cela, nous devons réimporter l'objet `x_training_data` original sous un nouveau nom de variable appelé `unscaled_x_training_data`. Pour des raisons de cohérence, nous réimporterons également les données de test sous forme de DataFrame appelé `unscaled_test_data` :

```py

unscaled_training_data = pd.read_csv('FB_training_data.csv')

unscaled_test_data = pd.read_csv('FB_test_data.csv')


```

Maintenant, nous pouvons concaténer la colonne `Open` de chaque DataFrame avec l'instruction suivante :

```py

all_data = pd.concat((unscaled_x_training_data['Open'], unscaled_test_data['Open']), axis = 0)


```

Cet objet `all_data` est une série pandas de longueur 1279.

Maintenant, nous devons créer un tableau de tous les prix des actions de janvier 2020 et des 40 jours de trading précédents à janvier. Nous appellerons cet objet `x_test_data` puisqu'il contient les valeurs `x` que nous utiliserons pour faire des prédictions de prix des actions pour janvier 2020.

La première chose que vous devez faire est de trouver l'index du premier jour de trading en janvier dans notre objet `all_data`. L'instruction `len(all_data) - len(test_data)` identifie cet index pour nous.

Cela représente la borne supérieure du premier élément du tableau. Pour obtenir la borne inférieure, il suffit de soustraire `40` de ce nombre. Autrement dit, la borne inférieure est `len(all_data) - len(test_data) - 40`.

La borne supérieure de l'ensemble du tableau `x_test_data` sera le dernier élément de l'ensemble de données. En conséquence, nous pouvons créer ce tableau NumPy avec l'instruction suivante :

```py

x_test_data = all_data[len(all_data) - len(test_data) - 40:].values


```

Vous pouvez vérifier si cet objet a été créé comme souhaité en imprimant `len(x_test_data)`, qui a une valeur de `61`. Cela a du sens - il devrait contenir les `21` valeurs pour janvier 2020 ainsi que les `40` valeurs précédentes.

La dernière étape de cette section consiste à remodeler rapidement notre tableau NumPy pour le rendre adapté à la méthode `predict` :

```py

x_test_data = np.reshape(x_test_data, (-1, 1))


```

Notez que si vous négligiez de faire cette étape, TensorFlow imprimerait un message utile qui expliquerait exactement comment vous devriez transformer vos données.

### **Mise à l'échelle de nos données de test**

Notre réseau de neurones récurrent a été entraîné sur des données mises à l'échelle. Pour cette raison, nous devons mettre à l'échelle notre variable `x_test_data` avant de pouvoir utiliser le modèle pour faire des prédictions.

```py

x_test_data = scaler.transform(x_test_data)


```

Notez que nous avons utilisé la méthode `transform` ici au lieu de la méthode `fit_transform` (comme avant). Cela est dû au fait que nous voulons transformer les données de test selon l'ajustement généré à partir de l'ensemble des données d'entraînement.

Cela signifie que la transformation appliquée aux données de test sera la même que celle appliquée aux données d'entraînement - ce qui est nécessaire pour que notre réseau de neurones récurrent fasse des prédictions précises.

### **Regroupement de nos données de test**

La dernière chose que nous devons faire est de regrouper nos données de test en `21` tableaux de taille `40`. Autrement dit, nous allons maintenant créer un tableau où chaque entrée correspond à une date de janvier et contient les prix des actions des `40` jours de trading précédents.

Le code pour faire cela est similaire à quelque chose que nous avons utilisé plus tôt :

```py

final_x_test_data = []

for i in range(40, len(x_test_data)):

    final_x_test_data.append(x_test_data[i-40:i, 0])

final_x_test_data = np.array(final_x_test_data)


```

Enfin, nous devons remodeler la variable `final_x_test_data` pour répondre aux normes TensorFlow.

Nous avons vu cela précédemment, donc le code ne devrait nécessiter aucune explication :

```py

final_x_test_data = np.reshape(final_x_test_data, (final_x_test_data.shape[0], 

                                               final_x_test_data.shape[1], 

                                               1))


```

### **Faire des prédictions**

Après une quantité absurde de retraitement des données, nous sommes maintenant prêts à faire des prédictions en utilisant nos données de test !

Cette étape est simple. Il suffit de passer notre objet `final_x_test_data` dans la méthode `predict` appelée sur l'objet `rnn`. Par exemple, voici comment vous pourriez générer ces prédictions et les stocker dans une variable appelée `predictions` :

```py

predictions = rnn.predict(final_x_test_data)


```

Traçons ces prédictions en exécutant `plt.plot(predictions)` (notez que vous devrez exécuter `plt.clf()` pour effacer votre toile d'abord) :

![Les prédictions originales de notre réseau de neurones récurrent](https://nickmccullum.com/images/python-deep-learning/recurrent-neural-networks/original_predictions.png)

Comme vous pouvez le voir, les valeurs prédites dans ce graphique sont toutes comprises entre `0` et `1`. Cela est dû au fait que notre ensemble de données est toujours mis à l'échelle ! Nous devons le mettre à l'échelle pour que les prédictions aient un sens pratique.

La classe `MinMaxScaler` que nous avons utilisée pour mettre à l'échelle notre ensemble de données dispose d'une méthode utile `inverse_transform` pour mettre à l'échelle les données. Voici comment vous pourriez mettre à l'échelle les données et générer un nouveau graphique :

```py

unscaled_predictions = scaler.inverse_transform(predictions)

plt.clf() #Cela efface le premier graphique de prédiction de notre toile

plt.plot(unscaled_predictions)


```

![Les prédictions non mises à l'échelle de notre réseau de neurones récurrent](https://nickmccullum.com/images/python-deep-learning/recurrent-neural-networks/unscaled-predictions.png)

Cela semble beaucoup mieux ! Toute personne qui a suivi le prix de l'action de Facebook pendant un certain temps peut voir que cela semble assez proche de l'endroit où Facebook a réellement été négocié.

Générons un graphique qui compare nos prix d'actions prédits avec le prix réel de l'action de Facebook :

```py

plt.plot(unscaled_predictions, color = '#135485', label = "Prédictions")

plt.plot(test_data, color = 'black', label = "Données réelles")

plt.title('Prédictions du prix de l\'action Facebook')


```

## **Le code complet pour ce tutoriel**

Vous pouvez consulter le code complet de ce tutoriel dans [ce dépôt GitHub](https://github.com/nicholasmccullum/python-deep-learning). Il est également collé ci-dessous pour votre référence :

```py

#Importer les bibliothèques de science des données nécessaires

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

#Importer l'ensemble de données en tant que DataFrame pandas

training_data = pd.read_csv('FB_training_data.csv')

#Transformer l'ensemble de données en un tableau NumPy

training_data = training_data.iloc[:, 1].values

#Appliquer la mise à l'échelle des caractéristiques à l'ensemble de données

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

training_data = scaler.fit_transform(training_data.reshape(-1, 1))

#Initialiser nos variables x_training_data et y_training_data 

#en tant que listes Python vides

x_training_data = []

y_training_data =[]

#Remplir les listes Python en utilisant 40 timesteps

for i in range(40, len(training_data)):

    x_training_data.append(training_data[i-40:i, 0])

    y_training_data.append(training_data[i, 0])

    

#Transformer nos listes en tableaux NumPy

x_training_data = np.array(x_training_data)

y_training_data = np.array(y_training_data)

#Vérifier la forme des tableaux NumPy

print(x_training_data.shape)

print(y_training_data.shape)

#Remodeler le tableau NumPy pour répondre aux normes TensorFlow

x_training_data = np.reshape(x_training_data, (x_training_data.shape[0], 

                                               x_training_data.shape[1], 

                                               1))

#Imprimer la nouvelle forme de x_training_data

print(x_training_data.shape)

#Importer nos bibliothèques TensorFlow

from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import Dense

from tensorflow.keras.layers import LSTM

from tensorflow.keras.layers import Dropout

#Initialiser notre réseau de neurones récurrent

rnn = Sequential()

#Ajouter notre première couche LSTM

rnn.add(LSTM(units = 45, return_sequences = True, input_shape = (x_training_data.shape[1], 1)))

#Effectuer une régularisation par dropout

rnn.add(Dropout(0.2))

#Ajouter trois couches LSTM supplémentaires avec une régularisation par dropout

for i in [True, True, False]:

    rnn.add(LSTM(units = 45, return_sequences = i))

    rnn.add(Dropout(0.2))

#(Code original pour les trois couches LSTM supplémentaires)

# rnn.add(LSTM(units = 45, return_sequences = True))

# rnn.add(Dropout(0.2))

# rnn.add(LSTM(units = 45, return_sequences = True))

# rnn.add(Dropout(0.2))

# rnn.add(LSTM(units = 45))

# rnn.add(Dropout(0.2))

#Ajouter notre couche de sortie

rnn.add(Dense(units = 1))

#Compiler le réseau de neurones récurrent

rnn.compile(optimizer = 'adam', loss = 'mean_squared_error')

#Entraîner le réseau de neurones récurrent

rnn.fit(x_training_data, y_training_data, epochs = 100, batch_size = 32)

#Importer l'ensemble de données de test et le transformer en un tableau NumPy

test_data = pd.read_csv('FB_test_data.csv')

test_data = test_data.iloc[:, 1].values

#Assurer que la forme des données de test a du sens

print(test_data.shape)

#Tracer les données de test

plt.plot(test_data)

#Créer des objets de données d'entraînement et de test non mis à l'échelle

unscaled_training_data = pd.read_csv('FB_training_data.csv')

unscaled_test_data = pd.read_csv('FB_test_data.csv')

#Concaténer les données non mises à l'échelle

all_data = pd.concat((unscaled_x_training_data['Open'], unscaled_test_data['Open']), axis = 0)

#Créer notre objet x_test_data, qui contient chaque jour de janvier + les 40 jours précédents

x_test_data = all_data[len(all_data) - len(test_data) - 40:].values

x_test_data = np.reshape(x_test_data, (-1, 1))

#Mettre à l'échelle les données de test

x_test_data = scaler.transform(x_test_data)

#Regrouper nos données de test

final_x_test_data = []

for i in range(40, len(x_test_data)):

    final_x_test_data.append(x_test_data[i-40:i, 0])

final_x_test_data = np.array(final_x_test_data)

#Remodeler le tableau NumPy pour répondre aux normes TensorFlow

final_x_test_data = np.reshape(final_x_test_data, (final_x_test_data.shape[0], 

                                               final_x_test_data.shape[1], 

                                               1))

#Générer nos valeurs prédites

predictions = rnn.predict(final_x_test_data)

#Tracer nos valeurs prédites

plt.clf() #Cela efface l'ancien graphique de notre toile

plt.plot(predictions)

#Mettre à l'échelle les valeurs prédites et retracer les données

unscaled_predictions = scaler.inverse_transform(predictions)

plt.clf() #Cela efface le premier graphique de prédiction de notre toile

plt.plot(unscaled_predictions)

#Tracer les valeurs prédites par rapport au prix réel de l'action de Facebook

plt.plot(unscaled_predictions, color = '#135485', label = "Prédictions")

plt.plot(test_data, color = 'black', label = "Données réelles")

plt.title('Prédictions du prix de l\'action Facebook')


```

## **Résumé - L'Intuition derrière les Réseaux de Neurones Récurrents**

Dans ce tutoriel, vous avez appris comment construire et entraîner un réseau de neurones récurrent.

Voici un bref résumé de ce que vous avez appris :

* Comment appliquer la mise à l'échelle des caractéristiques à un ensemble de données sur lequel un réseau de neurones récurrent sera entraîné
* Le rôle des `timesteps` dans l'entraînement d'un réseau de neurones récurrent
* Que TensorFlow utilise principalement des tableaux NumPy comme structure de données pour entraîner des modèles
* Comment ajouter des couches `LSTM` et `Dropout` à un réseau de neurones récurrent
* Pourquoi la régularisation par dropout est couramment utilisée pour éviter le surapprentissage lors de l'entraînement des réseaux de neurones
* Que la couche `Dense` de TensorFlow est couramment utilisée comme couche de sortie d'un réseau de neurones récurrent
* Que l'étape de `compilation` de la construction d'un réseau de neurones implique de spécifier son optimiseur et sa fonction de perte
* Comment faire des prédictions en utilisant un réseau de neurones récurrent
* Que les prédictions faites en utilisant un réseau de neurones entraîné sur des données mises à l'échelle doivent être mises à l'échelle pour être interprétables par les humains

Si vous avez trouvé cet article utile, consultez mon livre [Pragmatic Machine Learning](https://gumroad.com/l/pGjwd) pour un guide basé sur des projets sur les modèles d'apprentissage profond couverts ici et dans [mes autres articles](https://www.freecodecamp.org/news/author/nick/).

%[https://gumroad.com/l/pGjwd]