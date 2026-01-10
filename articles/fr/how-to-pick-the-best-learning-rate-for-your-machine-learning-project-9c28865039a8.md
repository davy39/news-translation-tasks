---
title: Comment choisir le meilleur taux d'apprentissage pour votre projet de machine
  learning
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-16T16:25:58.000Z'
originalURL: https://freecodecamp.org/news/how-to-pick-the-best-learning-rate-for-your-machine-learning-project-9c28865039a8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*NJOjEommvMTHxdJERZgwFQ.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment choisir le meilleur taux d'apprentissage pour votre projet de machine
  learning
seo_desc: 'By David Mack

  A common problem we all face when working on deep learning projects is choosing
  a learning rate and optimizer (the hyper-parameters). If you’re like me, you find
  yourself guessing an optimizer and learning rate, then checking if they wo...'
---

Par David Mack

Un problème courant auquel nous sommes tous confrontés lors de la réalisation de projets de deep learning est le choix d'un taux d'apprentissage et d'un optimiseur (les hyper-paramètres). Si vous êtes comme moi, vous vous retrouvez à deviner un optimiseur et un taux d'apprentissage, puis à vérifier s'ils fonctionnent ([et nous ne sommes pas seuls](http://blog.dlib.net/2017/12/a-global-optimization-algorithm-worth.html)).

Pour mieux comprendre l'effet du choix de l'optimiseur et du taux d'apprentissage, j'ai entraîné le même modèle 500 fois. Les résultats montrent que les bons hyper-paramètres sont cruciaux pour le succès de l'entraînement, mais peuvent être difficiles à trouver.

Dans cet article, je discuterai des solutions à ce problème en utilisant des méthodes automatisées pour choisir les hyper-paramètres optimaux.

#### Configuration expérimentale

J'ai entraîné le réseau de neurones convolutionnel de base du [tutoriel de TensorFlow](https://www.tensorflow.org/tutorials/layers), qui apprend à reconnaître les chiffres [MNIST](https://en.wikipedia.org/wiki/MNIST_database). Il s'agit d'un réseau raisonnablement petit, avec deux couches convolutionnelles et deux couches denses, soit un total d'environ 3 400 poids à entraîner. La même graine aléatoire est utilisée pour chaque entraînement.

Il convient de noter que les résultats ci-dessous concernent un modèle et un ensemble de données spécifiques. Les hyper-paramètres idéaux pour d'autres modèles et ensembles de données seront différents.

_(Si vous souhaitez faire un don de temps GPU pour exécuter une version plus grande de cette expérience sur CIFAR-10, veuillez [me contacter](mailto:hello@octavian.ai))._

### Quel taux d'apprentissage fonctionne le mieux ?

La première chose que nous allons explorer est l'impact du taux d'apprentissage sur l'entraînement du modèle. Dans chaque exécution, le même modèle est entraîné à partir de zéro, en ne faisant varier que l'optimiseur et le taux d'apprentissage.

Le modèle a été entraîné avec 6 optimiseurs différents : Gradient Descent, Adam, Adagrad, Adadelta, RMS Prop et Momentum. Pour chaque optimiseur, il a été entraîné avec 48 taux d'apprentissage différents, de 0,000001 à 100 à des intervalles logarithmiques.

Dans chaque exécution, le réseau est entraîné jusqu'à ce qu'il atteigne au moins 97 % de précision d'entraînement. Le temps maximum autorisé était de 120 secondes. Les expériences ont été réalisées sur un Nvidia Tesla K80, hébergé par [FloydHub](https://www.floydhub.com/davidmack/projects/learning-rates). Le code source est [disponible en téléchargement](https://github.com/Octavian-ai/learning-rates).

Voici le temps d'entraînement pour chaque choix de taux d'apprentissage et d'optimiseur :

![Image](https://cdn-media-1.freecodecamp.org/images/-bK4I26MkIUgfx0n8pHdnkuUpHo7Gv0oxsXw)
_Les entraînements échoués sont représentés par des points manquants et des lignes discontinues_

Le graphique ci-dessus est intéressant. Nous pouvons voir que :

* Pour chaque optimiseur, la majorité des taux d'apprentissage échouent à entraîner le modèle.
* Il y a une forme de vallée pour chaque optimiseur : un taux d'apprentissage trop bas ne progresse jamais, et un taux d'apprentissage trop élevé provoque une instabilité et ne converge jamais. Entre les deux, il y a une bande de taux d'apprentissage "juste bons" qui entraînent avec succès.
* Il n'y a pas de taux d'apprentissage qui fonctionne pour tous les optimiseurs.
* Le taux d'apprentissage peut affecter le temps d'entraînement d'un ordre de grandeur.

En résumé, il est crucial de choisir le bon taux d'apprentissage. Sinon, votre réseau échouera à s'entraîner ou prendra beaucoup plus de temps à converger.

Pour illustrer comment chaque optimiseur diffère dans son taux d'apprentissage optimal, voici le modèle le plus rapide et le plus lent à entraîner pour chaque taux d'apprentissage, parmi tous les optimiseurs. Remarquez que le temps maximum est de 120s (par exemple, le réseau a échoué à s'entraîner) sur l'ensemble du graphique — il n'y a pas de taux d'apprentissage unique qui fonctionne pour chaque optimiseur :

![Image](https://cdn-media-1.freecodecamp.org/images/2z6pEcdYLajXFXdm5O-5KKbR9LNHj9OvRTLj)

Découvrez la large gamme de taux d'apprentissage (de 0,001 à 30) qui réussissent avec au moins un optimiseur dans le graphique ci-dessus.

### Quel optimiseur performe le mieux ?

Maintenant que nous avons identifié les meilleurs taux d'apprentissage pour chaque optimiseur, comparons la performance de chaque optimiseur entraîné avec le meilleur taux d'apprentissage trouvé pour lui dans la section précédente.

Voici la précision de validation de chaque optimiseur au fil du temps. Cela nous permet d'observer la rapidité, la précision et la stabilité de chacun :

![Image](https://cdn-media-1.freecodecamp.org/images/Q7LiyYjTzEKorkLjac-OP0ZZwPNyvRJ0KLP1)
_(Notez que cet entraînement a été réalisé beaucoup plus lentement que les expériences précédentes, avec des pauses fréquentes pour évaluer, afin que je puisse capturer une résolution plus élevée)_

Quelques observations :

* Tous les optimiseurs, à l'exception de [RMSProp](http://ruder.io/optimizing-gradient-descent/index.html#rmsprop) _(voir le dernier point)_, parviennent à converger en un temps raisonnable.
* Adam apprend le plus rapidement.
* Adam est plus stable que les autres optimiseurs et ne subit aucune baisse majeure de précision.
* RMSProp a été exécuté avec les arguments par défaut de TensorFlow (taux de décroissance 0,9, epsilon 1e-10, momentum 0,0) et il se peut que ceux-ci ne fonctionnent pas bien pour cette tâche. C'est un bon cas d'utilisation pour la recherche automatisée d'hyper-paramètres (voir la dernière section pour plus d'informations à ce sujet).

Adam avait également une gamme relativement large de taux d'apprentissage réussis dans l'expérience précédente. Dans l'ensemble, Adam est le meilleur choix parmi nos six optimiseurs pour ce modèle et cet ensemble de données.

### Comment la taille du modèle affecte-t-elle le temps d'entraînement ?

Examinons maintenant comment la taille du modèle affecte son entraînement.

Nous allons faire varier la taille du modèle par un facteur linéaire. Ce facteur va mettre à l'échelle linéairement le nombre de filtres convolutionnels et la largeur de la première couche dense, augmentant ainsi approximativement linéairement le nombre total de poids dans le modèle.

Il y a deux aspects que nous allons étudier :

1. Comment le temps d'entraînement change-t-il à mesure que le modèle grandit, pour un optimiseur et un taux d'entraînement fixes ?
2. Quel taux d'apprentissage entraîne le plus rapidement chaque taille de modèle, pour un optimiseur fixe ?

#### Comment le temps d'entraînement change-t-il à mesure que le modèle grandit ?

Ci-dessous, le temps nécessaire pour atteindre 96 % de précision d'entraînement sur le modèle, en augmentant sa taille de 1x à 10x. Nous avons utilisé l'un de nos hyper-paramètres les plus réussis des expériences précédentes :

![Image](https://cdn-media-1.freecodecamp.org/images/tquS47Rew7bWCWVUKxYQ-l4VIhN66UuUL8pI)
_La ligne rouge représente les données, la ligne pointillée grise est une tendance linéaire, à titre de comparaison_

* Le temps d'entraînement augmente linéairement avec la taille du modèle.
* Le même taux d'apprentissage entraîne avec succès le réseau pour toutes les tailles de modèle.

_(Remarque : les résultats suivants ne peuvent être fiables que pour l'ensemble de données et les modèles testés ici, mais pourraient valoir la peine d'être testés pour vos expériences.)_

C'est un résultat intéressant. Notre choix d'hyper-paramètres n'a pas été invalidé par la mise à l'échelle linéaire du modèle. Cela peut suggérer que la recherche d'hyper-paramètres peut être effectuée sur une version réduite d'un réseau, pour économiser du temps de calcul.

Cela montre également que, à mesure que le réseau devient plus grand, il n'entraîne pas de travail O(n²) pour converger le modèle (la croissance linéaire du temps peut s'expliquer par les opérations supplémentaires nécessaires pour l'entraînement de chaque poids).

Ce résultat est également rassurant, car il montre que notre framework de deep learning (ici TensorFlow) est efficace.

#### Quel taux d'apprentissage performe le mieux pour différentes tailles de modèle ?

Exécutons la même expérience pour plusieurs taux d'apprentissage et voyons comment le temps d'entraînement répond à la taille du modèle :

![Image](https://cdn-media-1.freecodecamp.org/images/ZFsYwLmU4nYhF9StoYJJ4YJXpSUA79xLXm6N)
_Les entraînements échoués sont représentés par des points manquants et des lignes discontinues_

* Les taux d'apprentissage 0,0005, 0,001, 0,00146 ont donné les meilleurs résultats — ceux-ci ont également donné les meilleurs résultats dans la première expérience. Nous voyons ici la même bande de "sweet spot" que dans la première expérience.
* Le temps d'entraînement de chaque taux d'apprentissage augmente linéairement avec la taille du modèle.
* La performance du taux d'apprentissage ne dépendait pas de la taille du modèle. Les mêmes taux qui ont donné les meilleurs résultats pour une taille 1x ont donné les meilleurs résultats pour une taille 10x.
* Au-dessus de 0,001, l'augmentation du taux d'apprentissage a augmenté le temps d'entraînement et a également augmenté la variance du temps d'entraînement (par rapport à une fonction linéaire de la taille du modèle).
* Le temps d'entraînement peut être modélisé approximativement comme _c + kn_ pour un modèle avec _n_ poids, un coût fixe c et une constante d'apprentissage _k=f(taux d'apprentissage)_.

En résumé, le taux d'apprentissage le plus performant pour une taille 1x était également le meilleur taux d'apprentissage pour une taille 10x.

### Automatiser le choix du taux d'apprentissage

Comme le montrent les résultats précédents, il est crucial pour l'entraînement du modèle d'avoir un bon choix d'optimiseur et de taux d'apprentissage.

Choisir manuellement ces hyper-paramètres est chronophage et sujet aux erreurs. À mesure que votre modèle change, le choix précédent d'hyper-paramètres peut ne plus être idéal. Il est peu pratique de continuer à effectuer de nouvelles recherches à la main.

Il existe plusieurs moyens de choisir automatiquement les hyper-paramètres. Je vais décrire ici quelques approches différentes.

#### Recherche par grille

La [recherche par grille](https://en.wikipedia.org/wiki/Hyperparameter_optimization#Grid_search) est ce que nous avons effectué dans la première expérience — pour chaque hyper-paramètre, créer une liste de valeurs possibles. Ensuite, pour chaque combinaison de valeurs possibles d'hyper-paramètres, entraîner le réseau et mesurer ses performances. Les meilleurs hyper-paramètres sont ceux qui donnent les meilleures performances observées.

La recherche par grille est très facile à mettre en œuvre et à comprendre. Il est également facile de vérifier que vous avez recherché une section suffisamment large de la recherche de paramètres. Elle est très populaire dans la recherche pour ces raisons.

#### Entraînement basé sur la population

L'[entraînement basé sur la population (DeepMind)](https://deepmind.com/blog/population-based-training-neural-networks/) est une implémentation élégante de l'utilisation d'un [algorithme génétique](https://en.wikipedia.org/wiki/Evolutionary_algorithm) pour le choix des hyper-paramètres.

Dans PBT, une population de modèles est créée. Ils sont tous continuellement entraînés en parallèle. Lorsqu'un membre de la population a eu suffisamment de temps pour s'entraîner et montrer une amélioration, sa précision de validation est comparée au reste de la population. Si ses performances sont dans les 20 % les plus bas, alors il copie et mute les hyper-paramètres et les variables de l'un des 20 % meilleurs performeurs.

De cette manière, les hyper-paramètres les plus réussis engendrent de nombreuses variantes légèrement mutées d'eux-mêmes et les meilleurs hyper-paramètres sont probablement découverts.

### Prochaines étapes

Merci d'avoir lu cette enquête sur les taux d'apprentissage. J'ai commencé ces expériences par curiosité et frustration autour de l'ajustement des hyper-paramètres, et j'espère que vous apprécierez les résultats et les conclusions autant que moi.

Si vous êtes intéressé par un sujet ou une extension particulière, [faites-le moi savoir](mailto:hello@octavian.ai). De plus, si vous êtes intéressé à faire un don de temps GPU pour exécuter une version beaucoup plus grande de cette expérience, [j'adorerais en parler](mailto:hello@octavian.ai).

Ces écrits font partie d'une exploration d'un an sur les sujets d'architecture IA. Suivez cette publication (et donnez quelques applaudissements à cet article !) pour obtenir des mises à jour lorsque les prochains articles seront publiés.