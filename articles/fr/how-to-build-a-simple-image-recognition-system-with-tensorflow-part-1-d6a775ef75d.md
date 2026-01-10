---
title: Comment construire un système simple de reconnaissance d'images avec TensorFlow
  (Partie 1)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-02T19:52:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-simple-image-recognition-system-with-tensorflow-part-1-d6a775ef75d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7euCCTB_Qoxogrw2bK_HHQ.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Machine Learning
  slug: machine-learning
- name: neural networks
  slug: neural-networks
- name: Python
  slug: python
- name: TensorFlow
  slug: tensorflow
seo_title: Comment construire un système simple de reconnaissance d'images avec TensorFlow
  (Partie 1)
seo_desc: 'By Wolfgang Beyer

  This isn’t a general introduction to Artificial Intelligence, Machine Learning or
  Deep Learning. There are already lots of great articles covering these topics (for
  example here or here).

  And this isn’t a discussion about whether AI...'
---

Par Wolfgang Beyer

Ce n'est pas une introduction générale à l'intelligence artificielle, à l'apprentissage automatique ou à l'apprentissage profond. Il existe déjà de nombreux articles excellents couvrant ces sujets (par exemple [ici](http://fortune.com/ai-artificial-intelligence-deep-machine-learning/) ou [ici](https://medium.com/@ageitgey/machine-learning-is-fun-80ea3ec3c471)).

Et ce n'est pas une discussion sur le fait de savoir si l'IA va asservir l'humanité ou simplement voler tous nos emplois. Vous pouvez trouver beaucoup de spéculations et quelques craintes prématurées ailleurs.

Au lieu de cela, cet article est une description détaillée de la manière de se lancer dans l'apprentissage automatique en construisant un système qui est (quelque peu) capable de reconnaître ce qu'il voit dans une image.

Je suis actuellement en train d'apprendre l'intelligence artificielle et l'apprentissage automatique. Et la manière dont j'apprends le mieux n'est pas seulement en lisant des choses, mais en construisant réellement des choses et en obtenant une certaine expérience pratique. Et c'est de cela que parle cet article. Je veux vous montrer comment vous pouvez construire un système qui effectue une tâche simple de vision par ordinateur : reconnaître le contenu d'une image.

Je ne prétends pas être un expert moi-même. J'apprends encore, et il y a beaucoup à apprendre. Je décris ce avec quoi j'ai joué, et si c'est quelque peu intéressant ou utile pour vous, c'est génial ! Si, en revanche, vous trouvez des erreurs ou avez des suggestions d'améliorations, faites-le moi savoir, afin que je puisse apprendre de vous.

Vous n'avez besoin d'aucune expérience préalable avec l'apprentissage automatique pour pouvoir suivre. Le code exemple est écrit en Python, donc une connaissance de base de Python serait idéale, mais la connaissance de tout autre langage de programmation est probablement suffisante.

### Pourquoi la reconnaissance d'images ?

La reconnaissance d'images est une excellente tâche pour développer et tester des approches d'apprentissage automatique. La vision est débattablement notre sens le plus puissant et nous vient naturellement à nous, humains. Mais comment faisons-nous réellement ? Comment le cerveau traduit-il l'image sur notre rétine en un modèle mental de notre environnement ? Je ne pense pas que quiconque sache exactement.

Le point est, il semble facile pour nous de le faire — si facile que nous n'avons même pas besoin de faire un effort conscient pour cela — mais difficile pour les ordinateurs à faire (En fait, cela pourrait ne pas être si facile pour nous non plus, peut-être que nous ne sommes simplement pas conscients de la quantité de travail que cela représente. Plus de la moitié de notre cerveau semble être directement ou indirectement impliquée dans la vision).

Comment pouvons-nous faire en sorte que les ordinateurs effectuent des tâches visuelles lorsque nous ne savons même pas comment nous le faisons nous-mêmes ? C'est là que l'apprentissage automatique entre en jeu. Au lieu d'essayer de trouver des instructions détaillées étape par étape sur la manière d'interpréter les images et de les traduire en un programme informatique, nous laissons l'ordinateur le découvrir par lui-même.

Le but de l'apprentissage automatique est de donner aux ordinateurs la capacité de faire quelque chose sans qu'on leur dise explicitement comment le faire. Nous fournissons simplement une sorte de structure générale et donnons à l'ordinateur l'opportunité d'apprendre par l'expérience, de manière similaire à la façon dont nous, humains, apprenons par l'expérience.

Mais avant de commencer à penser à une solution complète pour la vision par ordinateur, simplifions quelque peu la tâche et regardons un sous-problème spécifique qui est plus facile à gérer pour nous.

### Classification d'images et le jeu de données CIFAR-10

Nous allons essayer de résoudre un problème qui est aussi simple et petit que possible tout en restant suffisamment difficile pour nous enseigner des leçons précieuses. Tout ce que nous voulons que l'ordinateur fasse est ce qui suit : lorsqu'on lui présente une image (avec des dimensions d'image spécifiques), notre système doit l'analyser et lui attribuer une seule étiquette. Il peut choisir parmi un nombre fixe d'étiquettes, chacune étant une catégorie décrivant le contenu de l'image. Notre objectif est que notre modèle choisisse la catégorie correcte aussi souvent que possible. Cette tâche est appelée classification d'images.

Nous allons utiliser un jeu de données standardisé appelé [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html). CIFAR-10 se compose de 60 000 images. Il y a 10 catégories différentes et 6 000 images par catégorie. Chaque image a une taille de seulement 32 par 32 pixels. La petite taille rend parfois difficile pour nous, humains, de reconnaître la catégorie correcte, mais cela simplifie les choses pour notre modèle informatique et réduit la charge de calcul nécessaire pour analyser les images.

![Image](https://cdn-media-1.freecodecamp.org/images/0*LcHvFOyLREXIrTjX.png)
_Images aléatoires de chacune des 10 classes du jeu de données CIFAR-10. En raison de leur faible résolution, les humains auraient également du mal à étiqueter correctement toutes ces images._

La manière dont nous entrons ces images dans notre modèle est en fournissant au modèle un ensemble de nombres. Chaque pixel est décrit par trois nombres à virgule flottante représentant les valeurs rouge, vert et bleu pour ce pixel. Cela donne 32 x 32 x 3 = 3 072 valeurs pour chaque image.

En plus de CIFAR-10, il existe de nombreux autres jeux de données d'images qui sont couramment utilisés dans la communauté de la vision par ordinateur. L'utilisation de jeux de données standardisés sert deux objectifs. Premièrement, c'est beaucoup de travail pour créer un tel jeu de données. Vous devez trouver les images, les traiter pour répondre à vos besoins et étiqueter chacune d'entre elles individuellement. La deuxième raison est que l'utilisation du même jeu de données nous permet de comparer objectivement différentes approches entre elles.

De plus, les jeux de données d'images standardisés ont conduit à la création de listes de meilleurs scores en vision par ordinateur et de compétitions. La compétition la plus célèbre est probablement le [Image-Net Competition](http://www.image-net.org/), dans laquelle il y a 1000 catégories différentes à détecter. Le gagnant de 2012 était un algorithme développé par Alex Krizhevsky, Ilya Sutskever et Geoffrey Hinton de l'Université de Toronto ([article technique](https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf)) qui a dominé la compétition et gagné par une énorme marge. C'était la première fois que l'approche gagnante utilisait un réseau de neurones convolutif, ce qui a eu un grand impact sur la communauté de la recherche. Les réseaux de neurones convolutifs sont des réseaux de neurones artificiels vaguement modélisés d'après le cortex visuel trouvé chez les animaux. Cette technique existait depuis un certain temps, mais à l'époque, la plupart des gens ne voyaient pas encore son potentiel à être utile. Cela a changé après la compétition Image-Net de 2012. Soudain, il y a eu un grand intérêt pour les réseaux de neurones et l'apprentissage profond (l'apprentissage profond est simplement le terme utilisé pour résoudre des problèmes d'apprentissage automatique avec des réseaux de neurones multicouches). Cet événement joue un grand rôle dans le démarrage du boom de l'apprentissage profond de ces dernières années.

### Apprentissage supervisé

Comment pouvons-nous utiliser le jeu de données d'images pour faire en sorte que l'ordinateur apprenne par lui-même ? Même si l'ordinateur fait la partie apprentissage par lui-même, nous devons encore lui dire quoi apprendre et comment le faire. La manière dont nous faisons cela est en spécifiant un processus général de la manière dont l'ordinateur devrait évaluer les images.

Nous définissons un modèle mathématique général de la manière d'obtenir une étiquette de sortie à partir d'une image d'entrée. La sortie concrète du modèle pour une image spécifique dépend alors non seulement de l'image elle-même, mais aussi des paramètres internes du modèle. Ces paramètres ne sont pas fournis par nous, mais sont appris par l'ordinateur.

Tout cela se révèle être un problème d'optimisation. Nous commençons par définir un modèle et fournir des valeurs de départ pour ses paramètres. Ensuite, nous fournissons le jeu de données d'images avec ses étiquettes connues et correctes au modèle. C'est la phase d'entraînement. Pendant cette phase, le modèle examine à plusieurs reprises les données d'entraînement et continue de changer les valeurs de ses paramètres. Le but est de trouver des valeurs de paramètres qui entraînent la sortie du modèle étant correcte aussi souvent que possible. Ce type d'entraînement, dans lequel la solution correcte est utilisée avec les données d'entrée, est appelé apprentissage supervisé. Il existe également l'apprentissage non supervisé, dans lequel le but est d'apprendre à partir de données d'entrée pour lesquelles aucune étiquette n'est disponible, mais cela dépasse le cadre de cet article.

Après la fin de l'entraînement, les valeurs des paramètres du modèle ne changent plus et le modèle peut être utilisé pour classer des images qui n'ont pas fait partie de son jeu de données d'entraînement.

![Image](https://cdn-media-1.freecodecamp.org/images/0*p1KQuZlKY--ArR3I.png)
_Pendant l'entraînement, les prédictions du modèle sont comparées à leurs valeurs réelles. Ces informations sont ensuite utilisées pour mettre à jour les paramètres. Pendant le test, il n'y a plus de retour, le modèle génère simplement des étiquettes._

### TensorFlow

[TensorFlow](https://www.tensorflow.org/) est une bibliothèque logicielle open source pour l'apprentissage automatique, qui a été publiée par Google en 2015 et est rapidement devenue l'une des bibliothèques d'apprentissage automatique les plus populaires utilisées par les chercheurs et les praticiens du monde entier. Nous l'utilisons pour effectuer les calculs numériques intensifs pour notre modèle de classification d'images.

### Construction du modèle, un classifieur Softmax

Le code complet pour ce modèle est [disponible sur Github](https://github.com/wolfib/image-classification-CIFAR10-tf). Pour l'utiliser, vous devez avoir installé ce qui suit :

* Python (le code a été testé avec Python 2.7, mais Python 3.3+ devrait également fonctionner, [Lien vers les instructions d'installation](https://wiki.python.org/moin/BeginnersGuide/Download))
* TensorFlow ([Lien vers les instructions d'installation](https://www.tensorflow.org/versions/r0.12/get_started/os_setup.html))
* Jeu de données CIFAR-10 : Téléchargez la version Python du jeu de données depuis [https://www.cs.toronto.edu/~kriz/cifar.html](https://www.cs.toronto.edu/~kriz/cifar.html) ou utilisez le [lien direct](https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz) vers l'archive compressée. Placez le répertoire extrait `cifar-10-batches-py/` dans le répertoire où vous mettez le code source Python, de sorte que le chemin vers les images soit `/chemin-vers-vos-fichiers-source-python/cifar-10-batches-py/`.

Très bien, nous sommes enfin prêts à commencer. Examinons le fichier principal de notre expérience, `softmax.py`, et analysons-le ligne par ligne :

Les déclarations future doivent être présentes dans tous les fichiers Python TensorFlow pour assurer la compatibilité avec Python 2 et 3 selon le [guide de style TensorFlow](https://www.tensorflow.org/versions/r0.11/how_tos/style_guide.html).

Ensuite, nous importons TensorFlow, numpy pour les calculs numériques, et le module time. `data_helpers.py` contient des fonctions qui aident à charger et préparer le jeu de données.

Nous démarrons un chronomètre pour mesurer le temps d'exécution et définissons quelques paramètres. J'en parlerai plus tard lorsque nous les utiliserons réellement. Ensuite, nous chargeons le jeu de données CIFAR-10. Puisque la lecture des données ne fait pas partie du cœur de ce que nous faisons, j'ai mis ces fonctions dans le fichier séparé `data_helpers.py`, qui lit essentiellement les fichiers contenant le jeu de données et place les données dans une structure de données facile à manipuler pour nous.

Une chose importante à mentionner est que `load_data()` divise les 60 000 images en deux parties. La partie la plus grande contient 50 000 images. Cet ensemble d'entraînement est ce que nous utilisons pour entraîner notre modèle. Les 10 000 autres images sont appelées ensemble de test. Notre modèle ne voit jamais celles-ci jusqu'à ce que l'entraînement soit terminé. Ce n'est qu'alors, lorsque les paramètres du modèle ne peuvent plus être modifiés, que nous utilisons l'ensemble de test comme entrée pour notre modèle et mesurons la performance du modèle sur l'ensemble de test.

Cette séparation des données d'entraînement et de test est très importante. Nous ne saurions pas à quel point notre modèle est capable de faire des généralisations s'il était exposé au même jeu de données pour l'entraînement et pour le test. Dans le pire des cas, imaginez un modèle qui mémorise exactement toutes les données d'entraînement qu'il voit. Si nous devions utiliser les mêmes données pour le tester, le modèle fonctionnerait parfaitement en cherchant simplement la solution correcte dans sa mémoire. Mais il n'aurait aucune idée de ce qu'il faut faire avec des entrées qu'il n'a jamais vues auparavant.

Ce concept d'un modèle apprenant les caractéristiques spécifiques des données d'entraînement et négligeant éventuellement les caractéristiques générales, que nous aurions préféré qu'il apprenne, est appelé surapprentissage. Le surapprentissage et comment l'éviter est un grand problème en apprentissage automatique. Plus d'informations sur le surapprentissage et pourquoi il est généralement conseillé de diviser les données non seulement en 2 mais en 3 ensembles de données différents peuvent être trouvées dans [cette vidéo](https://www.coursera.org/learn/machine-learning/lecture/QGKbr/model-selection-and-train-validation-test-sets) ([miroir youtube](https://www.youtube.com/watch?v=z6aBwtEby_Y)) (la vidéo fait partie du grand cours gratuit d'Andrew Ng sur [l'apprentissage automatique sur Coursera](https://www.coursera.org/learn/machine-learning)).

Pour revenir à notre code, `load_data()` retourne un dictionnaire contenant

* `images_train` : le jeu de données d'entraînement sous forme de tableau de 50 000 par 3 072 (= 32 pixels x 32 pixels x 3 canaux de couleur) valeurs.
* `labels_train` : 50 000 étiquettes pour l'ensemble d'entraînement (chaque nombre entre 0 et 9 représentant laquelle des 10 classes l'image d'entraînement appartient)
* `images_test` : ensemble de test (10 000 par 3 072)
* `labels_test` : 10 000 étiquettes pour l'ensemble de test
* `classes` : 10 étiquettes textuelles pour traduire la valeur de classe numérique en un mot (0 pour 'avion', 1 pour 'voiture', etc.)

Maintenant, nous pouvons commencer à construire notre modèle. Les calculs numériques réels sont gérés par TensorFlow, qui utilise un backend C++ rapide et efficace pour cela. TensorFlow veut éviter de basculer répétitivement entre Python et C++ car cela ralentirait nos calculs.

Le flux de travail courant est donc de définir d'abord tous les calculs que nous voulons effectuer en construisant un soi-disant graphe TensorFlow. Pendant cette phase, aucun calcul n'est réellement effectué, nous préparons simplement le terrain. Ce n'est qu'ensuite que nous exécutons les calculs en fournissant des données d'entrée et en enregistrant les résultats.

Alors commençons à définir notre graphe. Nous décrivons d'abord la manière dont nos données d'entrée pour le graphe TensorFlow ressemblent en créant des placeholders. Ces placeholders ne contiennent aucune donnée réelle, ils spécifient simplement le type et la forme des données d'entrée.

Pour notre modèle, nous définissons d'abord un placeholder pour les données d'image, qui se compose de valeurs à virgule flottante (`tf.float32`). L'argument `shape` définit les dimensions d'entrée. Nous fournirons plusieurs images en même temps (nous parlerons de ces lots [plus tard](http://www.wolfib.com/Image-Recognition-Intro-Part-1/#batching)), mais nous voulons rester flexibles sur le nombre d'images que nous fournissons réellement. La première dimension de `shape` est donc `None`, ce qui signifie que la dimension peut être de n'importe quelle longueur. La deuxième dimension est 3 072, le nombre de valeurs à virgule flottante par image.

Le placeholder pour les informations d'étiquette de classe contient des valeurs entières (`tf.int64`), une valeur dans la plage de 0 à 9 par image. Puisque nous ne spécifions pas combien d'images nous allons entrer, l'argument `shape` est `[None]`.

`weights` et `biases` sont les variables que nous voulons optimiser. Mais parlons d'abord de notre modèle.

Notre entrée se compose de 3 072 nombres à virgule flottante et la sortie souhaitée est l'une des 10 valeurs entières différentes. Comment passons-nous de 3 072 valeurs à une seule ? Commençons par la fin. Au lieu d'une seule valeur entière entre 0 et 9, nous pourrions également regarder 10 valeurs de score — une pour chaque classe — et ensuite choisir la classe avec le score le plus élevé. Notre question originale se transforme donc en : Comment passons-nous de 3 072 valeurs à 10 ?

L'approche simple que nous adoptons est de regarder chaque pixel individuellement. Pour chaque pixel (ou plus précisément chaque canal de couleur pour chaque pixel) et chaque classe possible, nous demandons si la couleur du pixel augmente ou diminue la probabilité de cette classe.

Disons que le premier pixel est rouge. Si les images de voitures ont souvent un premier pixel rouge, nous voulons que le score pour la voiture augmente. Nous y parvenons en multipliant la valeur du canal de couleur rouge du pixel par un nombre positif et en ajoutant cela au score de la voiture. De même, si les images de chevaux n'ont jamais ou rarement un pixel rouge à la position 1, nous voulons que le score du cheval reste bas ou diminue. Cela signifie multiplier par un petit nombre ou négatif et ajouter le résultat au score du cheval.

Pour chacune des 10 classes, nous répétons cette étape pour chaque pixel et additionnons toutes les 3 072 valeurs pour obtenir un score global unique, une somme de nos 3 072 valeurs de pixel pondérées par les 3 072 poids de paramètres pour cette classe. À la fin, nous avons 10 scores, un pour chaque classe. Ensuite, nous regardons simplement quel score est le plus élevé, et c'est notre étiquette de classe.

![Image](https://cdn-media-1.freecodecamp.org/images/0*6_bFowzKogccTKsS.png)
_Une image est représentée par un tableau linéaire de 3 072 valeurs. Chaque valeur est multipliée par un paramètre de poids et les résultats sont additionnés pour obtenir un résultat unique — le score de l'image pour une classe spécifique._

La notation pour multiplier les valeurs de pixel par les valeurs de poids et additionner les résultats peut être considérablement simplifiée en utilisant la notation matricielle. Notre image est représentée par un vecteur de 3 072 dimensions. Si nous multiplions ce vecteur par une matrice de poids de 3 072 x 10, le résultat est un vecteur de 10 dimensions contenant exactement les sommes pondérées qui nous intéressent.

![Image](https://cdn-media-1.freecodecamp.org/images/0*IhOj7J2wjKbk0M7a.png)
_Calcul des valeurs de classe d'une image pour toutes les 10 classes en une seule étape via la multiplication matricielle._

Les valeurs réelles dans la matrice 3 072 x 10 sont nos paramètres de modèle. Si elles sont aléatoires/incorrectes, notre sortie sera aléatoire/incorrecte. C'est là que les données d'entraînement entrent en jeu. En regardant les données d'entraînement, nous voulons que le modèle découvre les valeurs des paramètres par lui-même.

Tout ce que nous disons à TensorFlow dans les deux lignes de code montrées ci-dessus, c'est qu'il y a une matrice de poids de paramètres de 3 072 x 10, qui sont tous définis à 0 au début. En plus, nous définissons un deuxième paramètre, un vecteur de biais de 10 dimensions. Le biais n'interagit pas directement avec les données d'image et est ajouté aux sommes pondérées. Le biais peut être vu comme un point de départ pour nos scores.

Pensez à une image qui est totalement noire. Toutes ses valeurs de pixel seraient 0, donc tous les scores de classe seraient 0 aussi, peu importe à quoi ressemble la matrice `weights`. Avoir des biais nous permet de commencer avec des scores de classe non nuls.

C'est là que la prédiction a lieu. Nous avons arrangé les dimensions de nos vecteurs et matrices de telle sorte que nous pouvons évaluer plusieurs images en une seule étape. Le résultat de cette opération est un vecteur de 10 dimensions pour chaque image d'entrée.

![Image](https://cdn-media-1.freecodecamp.org/images/0*z35bdmCy_5i-BzLH.png)
_Calcul des valeurs de classe pour toutes les 10 classes pour plusieurs images en une seule étape via la multiplication matricielle._

Le processus d'obtention de bonnes valeurs pour les paramètres `weights` et `bias` est appelé entraînement et fonctionne comme suit : d'abord, nous entrons des données d'entraînement et laissons le modèle faire une prédiction en utilisant ses valeurs de paramètres actuelles. Cette prédiction est ensuite comparée aux étiquettes de classe correctes. Le résultat numérique de cette comparaison est appelé perte. Plus la valeur de perte est petite, plus les étiquettes prédites sont proches des étiquettes correctes et vice versa.

Nous voulons que le modèle minimise la perte, afin que ses prédictions soient proches des vraies étiquettes. Mais avant de regarder la minimisation de la perte, jetons un coup d'œil à la manière dont la perte est calculée.

Les scores calculés à l'étape précédente, stockés dans la variable `logits`, contiennent des nombres réels arbitraires. Nous pouvons transformer ces valeurs en probabilités (valeurs réelles entre 0 et 1 qui s'additionnent à 1) en appliquant la [fonction softmax](https://en.wikipedia.org/wiki/Softmax_function), qui comprime essentiellement son entrée en une sortie avec les attributs souhaités. L'ordre relatif de ses entrées reste le même, donc la classe avec le score le plus élevé reste la classe avec la probabilité la plus élevée. La distribution de probabilité de sortie de la fonction softmax est ensuite comparée à la distribution de probabilité réelle, qui a une probabilité de 1 pour la classe correcte et 0 pour toutes les autres classes.

Nous utilisons une mesure appelée [entropie croisée](https://en.wikipedia.org/wiki/Cross_entropy) pour comparer les deux distributions (une explication plus technique peut être trouvée [ici](https://cs231n.github.io/linear-classify/#softmax)). Plus l'entropie croisée est petite, plus la différence entre la distribution de probabilité prédite et la distribution de probabilité correcte est petite. Cette valeur représente la perte dans notre modèle.

Heureusement, TensorFlow gère tous les détails pour nous en fournissant une fonction qui fait exactement ce que nous voulons. Nous comparons `logits`, les prédictions du modèle, avec `labels_placeholder`, les étiquettes de classe correctes. La sortie de `sparse_softmax_cross_entropy_with_logits()` est la valeur de perte pour chaque image d'entrée. Nous calculons ensuite la valeur de perte moyenne sur les images d'entrée.

Mais comment pouvons-nous changer nos valeurs de paramètres pour minimiser la perte ? C'est là que TensorFlow fait sa magie. Via une technique appelée différentiation automatique, il peut calculer le gradient de la perte par rapport aux valeurs des paramètres. Cela signifie qu'il connaît l'influence de chaque paramètre sur la perte globale et si le diminuer ou l'augmenter d'une petite quantité réduirait la perte. Il ajuste ensuite toutes les valeurs des paramètres en conséquence, ce qui devrait améliorer la précision du modèle. Après cette étape d'ajustement des paramètres, le processus redémarre et le groupe suivant d'images est fourni au modèle.

TensorFlow connaît différentes techniques d'optimisation pour traduire les informations de gradient en mises à jour réelles des paramètres. Ici, nous utilisons une option simple appelée descente de gradient qui ne regarde que l'état actuel du modèle lors de la détermination des mises à jour des paramètres et ne prend pas en compte les valeurs passées des paramètres.

La descente de gradient n'a besoin que d'un seul paramètre, le taux d'apprentissage, qui est un facteur d'échelle pour la taille des mises à jour des paramètres. Plus le taux d'apprentissage est grand, plus les valeurs des paramètres changent après chaque étape. Si le taux d'apprentissage est trop grand, les paramètres pourraient dépasser leurs valeurs correctes et le modèle pourrait ne pas converger. S'il est trop petit, le modèle apprend très lentement et met trop de temps à arriver à de bonnes valeurs de paramètres.

Le processus de catégorisation des images d'entrée, de comparaison des résultats prédits aux résultats réels, de calcul de la perte et d'ajustement des valeurs des paramètres est répété de nombreuses fois. Pour des modèles plus grands et plus complexes, les coûts de calcul peuvent rapidement augmenter, mais pour notre modèle simple, nous n'avons besoin ni de beaucoup de patience ni de matériel spécialisé pour voir des résultats.

Ces deux lignes mesurent la précision du modèle. `argmax` de `logits` le long de la dimension 1 retourne les indices de la classe avec le score le plus élevé, qui sont les étiquettes de classe prédites. Les étiquettes sont ensuite comparées aux étiquettes de classe correctes par `tf.equal()`, qui retourne un vecteur de valeurs booléennes. Les booléens sont convertis en valeurs flottantes (chacune étant soit 0 soit 1), dont la moyenne est la fraction d'images correctement prédites.

Nous avons enfin terminé de définir le graphe TensorFlow et sommes prêts à commencer à l'exécuter. Le graphe est lancé dans une session à laquelle nous pouvons accéder via la variable `sess`. La première chose que nous faisons après avoir lancé la session est d'initialiser les variables que nous avons créées précédemment. Dans les définitions de variables, nous avons spécifié des valeurs initiales, qui sont maintenant attribuées aux variables.

Ensuite, nous démarrons le processus d'entraînement itératif qui doit être répété `max_steps` fois.

Ces lignes choisissent aléatoirement un certain nombre d'images dans les données d'entraînement. Les morceaux résultants d'images et d'étiquettes des données d'entraînement sont appelés lots. La taille du lot (nombre d'images dans un seul lot) nous indique la fréquence à laquelle l'étape de mise à jour des paramètres est effectuée. Nous calculons d'abord la perte moyenne sur toutes les images d'un lot, puis nous mettons à jour les paramètres via la descente de gradient.

Si, au lieu de nous arrêter après un lot, nous classions d'abord toutes les images de l'ensemble d'entraînement, nous pourrions calculer la vraie perte moyenne et le vrai gradient au lieu des estimations lorsque nous travaillons avec des lots. Mais cela prendrait beaucoup plus de calculs pour chaque étape de mise à jour des paramètres. À l'autre extrême, nous pourrions définir la taille du lot à 1 et effectuer une mise à jour des paramètres après chaque image. Cela entraînerait des mises à jour plus fréquentes, mais les mises à jour seraient beaucoup plus erratiques et ne seraient souvent pas dans la bonne direction.

Habituellement, une approche quelque part entre ces deux extrêmes donne l'amélioration la plus rapide des résultats. Pour des modèles plus grands, les considérations de mémoire sont également très pertinentes. Il est souvent préférable de choisir une taille de lot aussi grande que possible, tout en étant encore capable de faire tenir toutes les variables et les résultats intermédiaires dans la mémoire.

Ici, la première ligne de code choisit `batch_size` indices aléatoires entre 0 et la taille de l'ensemble d'entraînement. Ensuite, les lots sont construits en choisissant les images et les étiquettes à ces indices.

Toutes les 100 itérations, nous vérifions la précision actuelle du modèle sur le lot de données d'entraînement. Pour ce faire, nous devons simplement appeler l'opération de précision que nous avons définie précédemment.

C'est la ligne la plus importante dans la boucle d'entraînement. Nous disons au modèle d'effectuer une seule étape d'entraînement. Nous n'avons pas besoin de répéter ce que le modèle doit faire pour pouvoir faire une mise à jour des paramètres. Toutes les informations ont été fournies dans la définition du graphe TensorFlow. TensorFlow sait que la mise à jour de la descente de gradient dépend de la connaissance de la `loss`, qui dépend des `logits` qui dépendent des `weights`, des `biases` et du lot d'entrée réel.

Nous devons donc simplement fournir le lot de données d'entraînement au modèle. Cela est fait en fournissant un dictionnaire d'alimentation dans lequel le lot de données d'entraînement est attribué aux placeholders que nous avons définis précédemment.

Après la fin de l'entraînement, nous évaluons le modèle sur l'ensemble de test. C'est la première fois que le modèle voit l'ensemble de test, donc les images de l'ensemble de test sont complètement nouvelles pour le modèle. Nous évaluons à quel point le modèle entraîné peut gérer des données inconnues.

Les dernières lignes impriment combien de temps il a fallu pour entraîner et exécuter le modèle.

### Résultats

Exécutons le modèle avec la commande « `python softmax.py` ». Voici à quoi ressemble ma sortie :

```
Step   0: training accuracy 0.14 Step 100: training accuracy 0.32 Step 200: training accuracy 0.3 Step 300: training accuracy 0.23 Step 400: training accuracy 0.26 Step 500: training accuracy 0.31 Step 600: training accuracy 0.44 Step 700: training accuracy 0.33 Step 800: training accuracy 0.23 Step 900: training accuracy 0.31 Test accuracy 0.3066 Total time: 12.42s
```

Que signifie cela ? La précision de l'évaluation du modèle entraîné sur l'ensemble de test est d'environ 31 %. Si vous exécutez le code vous-même, votre résultat sera probablement autour de 25-30 %. Donc notre modèle est capable de choisir l'étiquette correcte pour une image qu'il n'a jamais vue auparavant environ 25-30 % du temps. Ce n'est pas mal !

Il y a 10 étiquettes différentes, donc une devinette aléatoire donnerait une précision de 10 %. Notre méthode très simple est déjà bien meilleure que de deviner au hasard. Si vous pensez que 25 % semble encore assez bas, n'oubliez pas que le modèle est encore assez stupide. Il n'a aucune notion de caractéristiques d'image réelles comme des lignes ou même des formes. Il regarde strictement la couleur de chaque pixel individuellement, complètement indépendant des autres pixels. Une image décalée d'un seul pixel représenterait une entrée complètement différente pour ce modèle. En tenant compte de cela, 25 % ne semble plus si mauvais.

Que se passerait-il si nous entraînions pour plus d'itérations ? Cela n'améliorerait probablement pas la précision du modèle. Si vous regardez les résultats, vous pouvez voir que la précision de l'entraînement n'augmente pas de manière constante, mais fluctue plutôt entre 0,23 et 0,44. Il semble que nous ayons atteint la limite de ce modèle et que voir plus de données d'entraînement n'aiderait pas. Ce modèle n'est pas capable de fournir de meilleurs résultats. En fait, au lieu de s'entraîner pendant 1000 itérations, nous aurions obtenu une précision similaire après significativement moins d'itérations.

Une dernière chose que vous avez probablement remarquée : la précision du test est assez inférieure à la précision de l'entraînement. Si cet écart est assez grand, c'est souvent un signe de surapprentissage. Le modèle est alors plus finement ajusté aux données d'entraînement qu'il a vues, et il n'est pas capable de généraliser aussi bien aux données précédemment invisibles.

Cet article est déjà devenu assez long. Je voudrais vous remercier de l'avoir lu en entier (ou d'avoir sauté directement à la fin) ! J'espère que vous avez trouvé quelque chose qui vous intéresse, que ce soit le fonctionnement d'un classifieur d'apprentissage automatique ou comment construire et exécuter un graphe simple avec TensorFlow. Bien sûr, il reste encore beaucoup de matériel que j'aimerais ajouter. Jusqu'à présent, nous n'avons parlé que du classifieur softmax, qui n'utilise même pas de réseaux de neurones.

Mon prochain article de blog change cela : Découvrez combien l'utilisation d'un petit modèle de réseau de neurones peut améliorer les résultats ! [Lisez-le ici](https://medium.com/@woolfib/how-to-build-a-simple-image-recognition-system-with-tensorflow-part-2-c83348b33bce#.t279qavhj).

Merci d'avoir lu. Vous pouvez également consulter d'autres articles que j'ai écrits sur [mon blog](http://www.wolfib.com).