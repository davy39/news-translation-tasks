---
title: Que faire lorsque vos données d'entraînement et de test proviennent de distributions
  différentes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-29T01:09:45.000Z'
originalURL: https://freecodecamp.org/news/what-to-do-when-your-training-and-testing-data-come-from-different-distributions-d89674c6ecd8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*IH5uBePl83tyOcWgzU7eyg.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: data
  slug: data
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: 'tech '
  slug: tech
seo_title: Que faire lorsque vos données d'entraînement et de test proviennent de
  distributions différentes
seo_desc: 'By Nezar Assawiel

  To build a well-performing machine learning (ML) model, it is essential to train
  the model on and test it against data that come from the same target distribution.

  However, sometimes only a limited amount of data from the target dis...'
---

Par Nezar Assawiel

Pour construire un modèle de machine learning (ML) performant, il est essentiel d'entraîner le modèle et de le tester avec des données provenant de la même distribution cible.

Cependant, parfois seule une quantité limitée de données de la distribution cible peut être collectée. Cela peut ne pas être suffisant pour construire les ensembles d'entraînement/développement/test nécessaires.

Pourtant, des données similaires provenant d'autres distributions de données pourraient être facilement disponibles. Que faire dans un tel cas ? Discutons de quelques idées !

#### **Quelques connaissances de base**

Pour mieux suivre la discussion ici, vous pouvez vous renseigner sur les concepts suivants de base en ML, si vous ne les connaissez pas déjà :

* **Ensembles d'entraînement, de développement (dev) et de test :** Notez que l'ensemble de développement est également appelé ensemble de validation ou de maintien. [Cet article](https://towardsdatascience.com/train-validation-and-test-sets-72cb40cba9e7) est une bonne introduction courte sur le sujet.
* **Erreurs de biais (sous-ajustement) et de variance (surajustement) :** [Ceci](https://www.quora.com/What-is-the-best-way-to-explain-the-bias-variance-trade-off-in-laymans-terms) est une excellente explication simple de ces erreurs.
* **Comment la division train/dev/test est correctement effectuée :** Vous pouvez vous référer à [cet article](https://medium.freecodecamp.org/how-to-strategically-accomplish-your-machine-learning-models-performance-goals-44dddc11697e) que j'ai écrit précédemment pour un bref aperçu de ce sujet.

### Scénario

Disons que vous construisez une application de classification d'images de chiens qui détermine si une image est celle d'un chien ou non.

L'application est destinée aux utilisateurs des zones rurales qui peuvent prendre des photos d'animaux avec leurs appareils mobiles pour que l'application classe les animaux pour eux.

En étudiant la distribution des données cibles, vous avez trouvé que les images sont principalement floues, de basse résolution et similaires à ce qui suit :

![Image](https://cdn-media-1.freecodecamp.org/images/4qHmR4-ZAX6hDOT7toyocFgFTzENQEkSk642)
_Gauche : Chien (race Volpino Italiano), Droite : Renard arctique._

Vous n'avez pu collecter que 8 000 images de ce type, ce qui n'est pas suffisant pour construire les ensembles d'entraînement/développement/test. Supposons que vous avez déterminé que vous aurez besoin d'au moins 100 000 images.

Vous vous êtes demandé si vous pouviez utiliser des images d'un autre ensemble de données — en plus des 8 000 images que vous avez collectées — pour construire les ensembles d'entraînement/développement/test.

Vous avez réalisé que vous pouvez facilement scraper le web pour construire un ensemble de données de 100 000 images ou plus, avec des fréquences similaires d'images de chiens vs. non-chiens à celles requises.

Mais, clairement, cet ensemble de données web provient d'une distribution différente, avec des images de haute résolution et claires comme les suivantes :

![Image](https://cdn-media-1.freecodecamp.org/images/ZcMgh4aInQxGlzFsj5zUuRJXwY4Zryyqu0wk)

![Image](https://cdn-media-1.freecodecamp.org/images/SqMDuHNj-H8a5VllzFSjv1ce5ebUuzT-H3aQ)

![Image](https://cdn-media-1.freecodecamp.org/images/GoVYRxUseI27Tj0jvTxdboPUTtFgKanC7Hyi)
_Images de chiens (gauche et droite) et d'un renard (centre)._

Comment construiriez-vous les ensembles d'entraînement/développement/test ?

Vous ne pouvez pas utiliser uniquement les 8 000 images originales que vous avez collectées pour construire les ensembles d'entraînement/développement/test, car elles ne sont pas suffisantes pour créer un classificateur performant. En général, la vision par ordinateur, comme d'autres problèmes de perception naturelle — reconnaissance vocale ou traitement du langage naturel — nécessite beaucoup de données.

De plus, vous ne pouvez pas utiliser uniquement l'ensemble de données web. Le classificateur ne performera pas bien sur les images floues des utilisateurs, qui sont différentes des images claires et haute définition du web utilisées pour entraîner le modèle.

Alors, que faites-vous ? Considérons quelques possibilités.

#### Une option possible — mélanger les données

Une chose que vous pouvez faire est de combiner les deux ensembles de données et de les mélanger aléatoirement. Ensuite, divisez l'ensemble de données résultant en ensembles d'entraînement/développement/test.

En supposant que vous avez décidé d'utiliser une division 96:2:2% pour les ensembles d'entraînement/développement/test, ce processus sera quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/vN2Sg-20NxtL5WYqDH6gzkoQmGgEp8arFVUu)

Avec cette configuration, les ensembles d'entraînement/développement/test proviennent tous de la même distribution, comme illustré par les couleurs dans le graphique ci-dessus, ce qui est souhaité.

Cependant, il y a un gros inconvénient ici !

Si vous regardez l'ensemble de développement, sur 2 000 images, en moyenne seulement 148 images proviennent de la distribution cible.

Cela signifie que pour la plupart, vous optimisez le classificateur pour la distribution des images web (1 852 images sur 2 000 images) — ce qui n'est **pas** ce que vous voulez !

La même chose peut être dite pour l'ensemble de test lors de l'évaluation de la performance du classificateur contre celui-ci. Donc, ce n'est pas une bonne façon de faire la division train/dev/test.

#### Une meilleure option

Une alternative est de faire en sorte que les ensembles de développement/test proviennent de l'ensemble de données de la distribution cible, et l'ensemble d'entraînement de l'ensemble de données web.

Disons que vous utilisez toujours une division 96:2:2% pour les ensembles d'entraînement/développement/test comme avant. Les ensembles de développement/test seront de 2 000 images chacun — provenant de la distribution cible — et le reste ira à l'ensemble d'entraînement, comme illustré ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/nDV-SlPBIuHNjC3valB5PphByOz6SwbI11B-)

En utilisant cette division, vous optimiserez le classificateur pour qu'il performe bien sur la distribution cible, ce qui est ce qui vous intéresse. Cela est dû au fait que les images de l'ensemble de développement proviennent uniquement de la distribution cible.

Cependant, la distribution d'entraînement est maintenant différente de la distribution de développement/test. Cela signifie que pour la plupart, vous entraînez le classificateur sur des images web. Ainsi, cela prendra plus de temps et d'efforts pour optimiser le modèle.

Plus important encore, vous ne pourrez pas facilement dire si l'erreur du classificateur sur l'ensemble de développement par rapport à l'erreur sur l'ensemble d'entraînement est une erreur de variance, une erreur de non-correspondance des données, ou une combinaison des deux.

Examinons cela plus en détail et voyons ce que nous pouvons faire à ce sujet.

#### Variance vs non-correspondance des données

Considérons la division train/dev/test de la deuxième option ci-dessus. Supposons que l'erreur humaine est nulle, pour simplifier.

Supposons également que vous avez trouvé que l'erreur d'entraînement est de 2 % et l'erreur de développement de 10 %. Combien des 8 % d'erreur entre ces deux valeurs est dû à la non-correspondance des données entre les deux ensembles — étant donné qu'ils proviennent de distributions différentes ? Et combien est dû à la variance du modèle (surajustement) ? Nous ne pouvons pas le dire.

Modifions la division train/dev/test. Prenez une petite portion de l'ensemble d'entraînement et appelez-la l'ensemble "pont". L'ensemble pont ne sera pas utilisé pour entraîner le classificateur. Il s'agit plutôt d'un ensemble indépendant. La division a maintenant quatre ensembles appartenant à deux distributions de données — comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/Fs65nHnro6cMkMKKq6HELKX0udt1ZL20e2CS)

#### Erreur de variance

Avec cette division, supposons que vous avez trouvé des erreurs d'entraînement et de développement de 2 % et 10 %, respectivement. Vous avez trouvé que l'erreur du pont est de 9 %, comme montré ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/f3fvUFd-FRiBaqk0362cbHBCGqRCWolHVA6N)

Maintenant, combien des 8 % d'erreur entre les erreurs des ensembles d'entraînement et de développement est une erreur de variance, et combien est une erreur de non-correspondance des données ?

Facile ! La réponse est 7 % d'erreur de variance et 1 % d'erreur de non-correspondance des données. Mais pourquoi ?

C'est parce que l'ensemble pont provient de la même distribution que l'ensemble d'entraînement, et la différence d'erreur entre eux est de 7 %. Cela signifie que le classificateur est surajusté à l'ensemble d'entraînement. Cela nous indique que nous avons un **problème de haute variance** entre les mains.

#### Erreur de non-correspondance des données

Maintenant, supposons que vous avez trouvé que l'erreur sur l'ensemble pont est de 3 % et le reste comme avant, comme montré ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/rgSqJ9pTEVNEYg0AyVeBFQjzYQFyie6Ar-IG)

Combien des 8 % d'erreur entre les ensembles d'entraînement et de développement est une erreur de variance et combien est une erreur de non-correspondance des données ?

La réponse est 1 % d'erreur de variance et 7 % d'erreur de non-correspondance des données. Pourquoi donc ?

Cette fois, c'est parce que le classificateur performe bien sur un ensemble de données qu'il n'a pas vu auparavant s'il provient de la même distribution, comme l'ensemble pont. Il performe mal s'il provient d'une distribution différente, comme l'ensemble de développement. Ainsi, nous avons un **problème de non-correspondance des données**.

Réduire l'erreur de variance est une tâche courante en ML. Par exemple, vous pouvez utiliser des méthodes de régularisation, ou allouer un ensemble d'entraînement plus grand.

Cependant, atténuer l'erreur de non-correspondance des données est un problème plus intéressant. Alors, parlons-en.

#### Atténuer la non-correspondance des données

Pour réduire l'erreur de non-correspondance des données, vous devrez somehow incorporer les caractéristiques des ensembles de données de développement/test — la distribution cible — dans l'ensemble d'entraînement.

Collecter plus de données de la distribution cible pour les ajouter à l'ensemble d'entraînement est toujours la meilleure option. Mais, si cela n'est pas possible (comme nous l'avons supposé au début de notre discussion), vous pouvez essayer les approches suivantes :

#### Analyse des erreurs

Analyser les erreurs sur l'ensemble de développement et comment elles diffèrent des erreurs sur l'ensemble d'entraînement pourrait vous donner des idées pour résoudre le problème de non-correspondance des données.

Par exemple, si vous trouvez que beaucoup des erreurs sur l'ensemble de développement se produisent lorsque l'arrière-plan de l'image de l'animal est rocheux, vous pouvez atténuer ces erreurs en ajoutant des images d'animaux avec un arrière-plan rocheux à l'ensemble d'entraînement.

#### Synthèse artificielle de données

Une autre façon d'incorporer les caractéristiques des ensembles de développement/test dans l'ensemble d'entraînement est de synthétiser des données avec des caractéristiques similaires.

Par exemple, nous avons mentionné précédemment que les images de nos ensembles de développement/test sont principalement floues, contrairement aux images claires du web qui constituent la majeure partie de notre ensemble d'entraînement. Vous pouvez ajouter artificiellement du flou aux images de l'ensemble d'entraînement pour les rendre plus similaires aux ensembles de développement/test comme dans l'image suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/ZvE-mWboEkz0Bo4QEjuwm4THSFLY1IoLTCsM)
_Image de l'ensemble d'entraînement avant et après floutage._

Cependant, il y a un point important à noter ici !

Vous pourriez finir par surajuster votre classificateur aux caractéristiques artificielles que vous avez créées.

Dans notre exemple, le flou que vous avez créé artificiellement par une fonction mathématique pourrait n'être qu'un petit sous-ensemble du flou qui existe dans les images de la distribution cible.

En d'autres termes, le flou dans la distribution cible pourrait être dû à de nombreuses raisons. Par exemple, le brouillard, un appareil photo de basse résolution, le mouvement du sujet pourraient tous être des causes. Mais votre flou synthétisé peut ne pas représenter toutes ces causes.

Plus généralement, lors de la synthèse de données pour l'ensemble d'entraînement pour tout type de problème (comme la vision par ordinateur ou la reconnaissance vocale), vous pourriez surajuster votre modèle à l'ensemble de données synthétisé.

Cet ensemble de données peut sembler suffisamment représentatif de la distribution cible à l'œil humain. Mais en fait, il n'est qu'un petit ensemble de la distribution cible. Donc, gardez cela à l'esprit tout en utilisant cet outil puissant — la synthèse de données.

#### En résumé

Lors du développement d'un modèle ML, idéalement, les ensembles de données d'entraînement/développement/test devraient tous provenir de la même distribution de données — celle des données que le modèle rencontrera lorsqu'il sera utilisé par les utilisateurs.

Cependant, parfois il n'est pas possible de collecter suffisamment de données de la distribution cible pour construire les ensembles d'entraînement/développement/test, tandis que des données similaires provenant d'autres distributions sont facilement disponibles.

Dans de tels cas, les ensembles de développement/test devraient provenir de la distribution cible tandis que les données des autres distributions peuvent être utilisées pour construire (la plupart de) l'ensemble d'entraînement. Des techniques de non-correspondance des données peuvent ensuite être utilisées pour atténuer les différences de distribution des données entre l'ensemble d'entraînement et les ensembles de développement/test.