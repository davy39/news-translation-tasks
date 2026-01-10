---
title: Une introduction à l'optimisation des hyperparamètres en haute dimension
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-13T18:09:37.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-high-dimensional-hyper-parameter-tuning-df5c0106e5a4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*veB2P1HZtGbhtsbDmgcLsg.jpeg
tags:
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
- name: optimization
  slug: optimization
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Une introduction à l'optimisation des hyperparamètres en haute dimension
seo_desc: 'By Thalles Silva

  Best practices for optimizing ML models


  If you ever struggled with tuning Machine Learning (ML) models, you are reading
  the right piece.

  Hyper-parameter tuning refers to the problem of finding an optimal set of parameter
  values for ...'
---

Par Thalles Silva

#### Bonnes pratiques pour optimiser les modèles de Machine Learning

![Image](https://cdn-media-1.freecodecamp.org/images/1*veB2P1HZtGbhtsbDmgcLsg.jpeg)

Si vous avez déjà eu du mal à optimiser les modèles de Machine Learning (ML), vous lisez le bon article.

**L'optimisation des hyperparamètres** fait référence au problème de trouver un ensemble optimal de valeurs de paramètres pour un algorithme d'apprentissage.

Généralement, le processus de choix de ces valeurs est une tâche chronophage.

Même pour des algorithmes simples comme la régression linéaire, trouver le meilleur ensemble d'hyperparamètres peut être difficile. Avec le Deep Learning, les choses se compliquent encore plus.

Certains des paramètres à optimiser lors de l'optimisation des réseaux de neurones (NNs) incluent :

* taux d'apprentissage
* momentum
* régularisation
* probabilité de dropout
* normalisation par lots

Dans cet article, nous parlons des bonnes pratiques pour optimiser les modèles de ML. Ces pratiques sont particulièrement utiles lorsque le nombre de paramètres à optimiser dépasse deux ou trois.

#### Le problème avec la recherche sur grille

La recherche sur grille est généralement un bon choix lorsque nous avons un petit nombre de paramètres à optimiser. Pour deux ou même trois paramètres différents, cela peut être la méthode à suivre.

Pour chaque hyperparamètre, nous définissons un ensemble de valeurs candidates à explorer.

Ensuite, l'idée est d'essayer de manière exhaustive chaque combinaison possible des valeurs des paramètres individuels.

Pour chaque combinaison, nous entraînons et évaluons un modèle différent.

À la fin, nous conservons celui avec la plus petite erreur de généralisation.

Le principal problème avec la recherche sur grille est qu'il s'agit d'un algorithme exponentiel. Son coût augmente de manière exponentielle avec le nombre de paramètres.

En d'autres termes, si nous devons optimiser _p_ paramètres et que chacun prend au plus _v_ valeurs, il s'exécute en [O(v) temps](https://guide.freecodecamp.org/computer-science/notation/big-o-notation/).

De plus, la recherche sur grille n'est pas aussi efficace pour explorer l'espace des hyperparamètres que nous pourrions le penser.

Regardez à nouveau le code ci-dessus. En utilisant cette configuration, nous allons entraîner un total de 256 modèles différents. Notez que si nous décidons d'ajouter un paramètre supplémentaire, le nombre d'expériences passerait à 1024.

Cependant, cette configuration n'explore que quatre valeurs différentes pour chaque hyperparamètre. C'est-à-dire que nous entraînons 256 modèles pour n'explorer que quatre valeurs du taux d'apprentissage, de la régularisation, etc.

De plus, la recherche sur grille nécessite généralement des essais répétitifs. Prenez les valeurs de `learning_rate_search` du code ci-dessus comme exemple.

```
learning_rate_search = [0.1, 0.01, 0.001, 0.0001]
```

Supposons qu'après notre premier essai (256 essais de modèles), nous obtenons le meilleur modèle avec une valeur de taux d'apprentissage de 0,01.

Dans cette situation, nous devrions essayer d'affiner nos valeurs de recherche en "zoomant" sur la grille autour de 0,01 dans l'espoir de trouver une valeur encore meilleure.

Pour ce faire, nous pourrions configurer une nouvelle recherche sur grille et redéfinir la plage de recherche du taux d'apprentissage comme suit :

```
learning_rate_search = [0.006, 0.008, 0.01, 0.04, 0.06]
```

Mais que se passe-t-il si nous obtenons le meilleur modèle avec une valeur de taux d'apprentissage de 0,0001 ?

Puisque cette valeur est à la limite de notre plage de recherche initiale, nous devrions décaler les valeurs et réessayer avec un ensemble différent comme :

```
learning_rate_search = [0.0001, 0.00006, 0.00002]
```

Et éventuellement essayer d'affiner la plage après avoir trouvé un bon candidat.

Tous ces détails soulignent à quel point la recherche d'hyperparamètres peut être chronophage.

### Une meilleure approche — Recherche aléatoire

Et si nous choisissions nos valeurs candidates d'hyperparamètres de manière aléatoire ? Aussi peu intuitif que cela puisse paraître, cette idée est presque toujours meilleure que la recherche sur grille.

#### Un peu d'intuition

Notez que certains hyperparamètres sont plus importants que d'autres.

Le taux d'apprentissage et le facteur de momentum, par exemple, valent plus la peine d'être optimisés que les autres.

Cependant, avec l'exception ci-dessus, il est difficile de savoir lesquels jouent des rôles majeurs dans le processus d'optimisation. En fait, je dirais que l'importance de chaque paramètre peut changer pour différentes architectures de modèles et ensembles de données.

Supposons que nous optimisons deux hyperparamètres — le taux d'apprentissage et la force de régularisation. Considérez également que seul le taux d'apprentissage compte pour le problème.

Dans le cas de la recherche sur grille, nous allons exécuter neuf expériences différentes, mais n'essayer que trois candidats pour le taux d'apprentissage.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UMQ1KOD053In4M8BA3sYzQ.png)
_Crédit Image : [Random Search for Hyper-Parameter Optimization](http://www.jmlr.org/papers/volume13/bergstra12a/bergstra12a.pdf" rel="noopener" target="_blank" title="), James Bergstra, Yoshua Bengio._

Maintenant, regardez ce qui se passe si nous échantillonnons les candidats uniformément de manière aléatoire. Dans ce scénario, nous explorons en fait neuf valeurs différentes pour chaque paramètre.

Si vous n'êtes pas encore convaincu, supposons que nous optimisons trois hyperparamètres. Par exemple, le taux d'apprentissage, la force de régularisation et le momentum.

![Image](https://cdn-media-1.freecodecamp.org/images/1*tkpDTzQKwekXbSd0L_e9Aw.png)
_Optimisation sur 3 hyperparamètres en utilisant la recherche sur grille._

Pour la recherche sur grille, nous exécuterions 125 entraînements, mais n'explorerions que cinq valeurs différentes de chaque paramètre.

D'autre part, avec la recherche aléatoire, nous explorerions 125 valeurs différentes de chaque paramètre.

#### Comment faire

Si nous voulons essayer des valeurs pour le taux d'apprentissage, disons dans la plage de 0,1 à 0,0001, nous faisons :

Notez que nous échantillonnons des valeurs à partir d'une **distribution uniforme sur une échelle logarithmique**.

Vous pouvez penser aux valeurs -1 et -4 (pour le taux d'apprentissage) comme les exposants dans l'intervalle [10e-1, 10e-4].

Si nous n'utilisons pas une échelle logarithmique, l'échantillonnage ne sera pas uniforme dans la plage donnée. En d'autres termes, vous ne devriez pas essayer d'échantillonner des valeurs comme :

Dans cette situation, la plupart des valeurs ne seraient pas échantillonnées à partir d'une région "valide". En fait, en considérant les échantillons de taux d'apprentissage dans cet exemple, **72 % des valeurs** tomberaient dans l'intervalle [0,02, 0,1].

De plus, 88 % des valeurs échantillonnées proviendraient de l'intervalle [0,01, 0,1]. C'est-à-dire que seulement 12 % des candidats de taux d'apprentissage, 3 valeurs, seraient échantillonnés à partir de l'intervalle [0,0004, 0,01]. Ne faites pas cela.

Dans le graphique ci-dessous, nous échantillonnons 25 valeurs aléatoires dans la plage [0,1, 0,0004]. Le graphique en haut à gauche montre les valeurs originales.

En haut à droite, notez que 72 % des valeurs échantillonnées sont dans l'intervalle [0,02, 0,1]. 88 % des valeurs se situent dans la plage [0,01, 0,1].

Le graphique du bas montre la distribution des valeurs. Seulement 12 % des valeurs sont dans l'intervalle [0,0004, 0,01]. Pour résoudre ce problème, échantillonnez les valeurs à partir d'une distribution uniforme sur une échelle logarithmique.

![Image](https://cdn-media-1.freecodecamp.org/images/1*aK1v6iIA8jNFYtaGe6bdNQ.png)

Un comportement similaire se produirait avec le paramètre de régularisation.

Notez également que, comme avec la recherche sur grille, vous devez considérer les deux cas que nous avons mentionnés ci-dessus.

Si le meilleur candidat se situe très près du bord, votre plage peut être décalée et doit être rééchantillonnée. De plus, après avoir choisi les premiers bons candidats, essayez de rééchantillonner sur une plage de valeurs plus fine.

En conclusion, voici les points clés à retenir.

* Si vous avez plus de deux ou trois hyperparamètres à optimiser, préférez la recherche aléatoire. Elle est plus rapide/facile à implémenter et converge plus rapidement que la recherche sur grille.
* Utilisez une échelle appropriée pour choisir vos valeurs. Échantillonnez à partir d'une distribution uniforme dans un espace logarithmique. Cela vous permettra d'échantillonner des valeurs également distribuées dans les plages de paramètres.
* Qu'il s'agisse de recherche aléatoire ou sur grille, faites attention aux candidats que vous choisissez. Assurez-vous que les plages des paramètres sont correctement définies et affinez les meilleurs candidats si possible.

Merci d'avoir lu ! Pour plus de contenus intéressants sur le Deep Learning, consultez certains de mes articles précédents :

[**Comment entraîner votre propre FaceID ConvNet en utilisant l'exécution Eager de TensorFlow**](https://medium.freecodecamp.org/how-to-train-your-own-faceid-cnn-using-tensorflow-eager-execution-6905afe4fd5a)  
[_Les visages sont partout — des photos et vidéos sur les sites de médias sociaux, aux applications de sécurité grand public comme le…medium.freecodecamp.org](https://medium.freecodecamp.org/how-to-train-your-own-faceid-cnn-using-tensorflow-eager-execution-6905afe4fd5a)[**Machine Learning 101 : Une introduction intuitive à la descente de gradient**](https://towardsdatascience.com/machine-learning-101-an-intuitive-introduction-to-gradient-descent-366b77b52645)  
[_La descente de gradient est, sans aucun doute, le cœur et l'âme de la plupart des algorithmes de Machine Learning (ML). Je crois définitivement…towardsdatascience.com](https://towardsdatascience.com/machine-learning-101-an-intuitive-introduction-to-gradient-descent-366b77b52645)