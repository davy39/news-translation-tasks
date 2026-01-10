---
title: Comment classer des photos en 600 classes en utilisant neuf millions d'images
  Open Images
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-20T18:16:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-classify-photos-in-600-classes-using-nine-million-open-images-65847da1a319
coverImage: https://cdn-media-1.freecodecamp.org/images/1*EI4YPmaav7hc79e0GH__BQ.png
tags:
- name: Computer Vision
  slug: computer-vision
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Comment classer des photos en 600 classes en utilisant neuf millions d'images
  Open Images
seo_desc: 'By Aleksey Bilogur

  If you’re looking build an image classifier but need training data, look no further
  than Google Open Images.

  This massive image dataset contains over 30 million images and 15 million bounding
  boxes. That’s 18 terabytes of image dat...'
---

Par Aleksey Bilogur

Si vous cherchez à construire un classificateur d'images mais que vous avez besoin de données d'entraînement, ne cherchez pas plus loin que [Google Open Images](https://storage.googleapis.com/openimages/web/index.html).

Ce vaste ensemble de données d'images contient plus de 30 millions d'images et 15 millions de boîtes englobantes. Cela représente 18 téraoctets de données d'images !

De plus, Open Images est beaucoup plus ouvert et accessible que certains autres ensembles de données d'images de cette envergure. Par exemple, ImageNet a des licences restrictives.

Cependant, il n'est pas facile pour les développeurs sur des machines individuelles de trier autant de données. Vous devez télécharger et traiter plusieurs fichiers de métadonnées, et créer votre propre espace de stockage (ou demander l'accès à un bucket Google Cloud).

D'un autre côté, il n'y a pas beaucoup d'ensembles de données d'images personnalisés disponibles, car franchement, ils sont difficiles à créer et à partager.

Dans cet article, nous allons construire et distribuer un pipeline simple de machine learning de bout en bout en utilisant Open Images.

Nous verrons comment créer votre propre ensemble de données autour de l'une des 600 étiquettes incluses dans les données de boîtes englobantes d'Open Images.

Nous allons montrer notre travail en construisant des "sandwichs ouverts". Ce sont des classificateurs d'images simples et reproductibles conçus pour répondre à une question ancienne : [un hamburger est-il un sandwich](https://english.stackexchange.com/questions/246580/is-a-hamburger-considered-a-sandwich) ?

Vous voulez voir le code ? Vous pouvez suivre dans [le dépôt sur GitHub](https://github.com/quiltdata/open-images).

### Téléchargement des données

Nous devons télécharger les données pertinentes avant de pouvoir faire quoi que ce soit avec.

C'est le défi principal lors de l'utilisation de Google Open Images (ou de tout ensemble de données externe, en réalité). Il n'y a pas de moyen facile de télécharger un sous-ensemble des données. Nous devons écrire un script qui le fasse pour nous.

J'ai écrit un script Python qui recherche les métadonnées dans l'[ensemble de données Open Images](https://github.com/openimages/dataset) pour des mots-clés que vous spécifiez. Il trouve les URLs originales des images correspondantes (sur [Flickr](https://www.flickr.com/)), puis les télécharge sur le disque.

C'est un témoignage de la puissance de Python que vous pouvez faire tout cela en seulement 50 lignes de code :

Ce script vous permet de télécharger le sous-ensemble d'images brutes qui ont des informations de boîtes englobantes pour n'importe quel sous-ensemble de catégories de notre choix :

```
$ git clone https://github.com/quiltdata/open-images.git$ cd open-images/$ conda env create -f environment.yml$ source activate quilt-open-images-dev$ cd src/openimager/$ python openimager.py "Sandwiches" "Hamburgers"
```

Les catégories sont organisées de manière hiérarchique.

Par exemple, `sandwich` et `hamburger` sont tous deux des sous-étiquettes de `food` (mais `hamburger` n'est pas une sous-étiquette de `sandwich` — hmm).

Nous pouvons visualiser l'ontologie sous forme d'arbre radial en utilisant Vega :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Wp0-dUSPLuwC6KN7hELNLw.png)

Vous pouvez voir une version interactive annotée de ce graphique (et télécharger le code derrière) [ici](https://alpha.quiltdata.com/b/quilt-example/tree/quilt/open_images/).

Toutes les catégories dans Open Images n'ont pas de données de boîtes englobantes associées.

Mais ce script vous permettra de télécharger n'importe quel sous-ensemble des 600 étiquettes qui en ont. Voici un aperçu de ce qui est possible :

`football`, `toy`, `bird`, `cat`, `vase`, `hair dryer`, `kangaroo`, `knife`, `briefcase`, `pencil case`, `tennis ball`, `nail`, `high heels`, `sushi`, `skyscraper`, `tree`, `truck`, `violin`, `wine`, `wheel`, `whale`, `pizza cutter`, `bread`, `helicopter`, `lemon`, `dog`, `elephant`, `shark`, `flower`, `furniture`, `airplane`, `spoon`, `bench`, `swan`, `peanut`, `camera`, `flute`, `helmet`, `pomegranate`, `crown`…

Pour les besoins de cet article, nous nous limiterons à deux seulement : `hamburger` et `sandwich`.

### Nettoyer, rogner

Une fois que nous avons exécuté le script et localisé les images, nous pouvons les inspecter avec `matplotlib` pour voir ce que nous avons :

```
import matplotlib.pyplot as pltfrom matplotlib.image import imread%matplotlib inlineimport os
```

```
fig, axarr = plt.subplots(1, 5, figsize=(24, 4))for i, img in enumerate(os.listdir('../data/images/')[:5]):    axarr[i].imshow(imread('../data/images/' + img))
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*8ytDl01L-ZoUKYxYREMkuw.png)
_Cinq exemples d'images {hamburger, sandwich} de Google Open Images V4._

Ces images ne sont pas faciles à utiliser pour l'entraînement. Elles ont tous les problèmes associés à la construction d'un ensemble de données en utilisant une source externe provenant de l'Internet public.

Juste cet petit échantillon ici démontre les différentes tailles, orientations et occlusions possibles dans nos classes cibles.

Dans un cas, nous n'avons même pas réussi à télécharger l'image réelle. Au lieu de cela, nous avons obtenu un espace réservé nous indiquant que l'image que nous voulions a depuis été supprimée !

Le téléchargement de ces données nous donne quelques milliers d'images d'exemple comme celles-ci. L'étape suivante consiste à tirer parti des informations de la boîte englobante pour rogner nos images afin de ne garder que les parties sandwich et hamburger.

Voici un autre tableau d'images, cette fois avec des boîtes englobantes incluses, pour démontrer ce que cela implique :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ii670RcCgXExc2CQgc-QEg.png)
_Boîtes englobantes. Remarquez (1) que l'ensemble de données inclut des "représentations" et (2) que les images brutes peuvent contenir de nombreuses instances d'objets._

[Ce notebook Jupyter annoté](https://github.com/quiltdata/open-images/blob/master/notebooks/build-dataset.ipynb) dans le [dépôt GitHub de démonstration](https://github.com/quiltdata/open-images) fait ce travail.

Je vais omettre de montrer ce code ici car il est légèrement compliqué. Cela est particulièrement vrai puisque nous devons également (1) refactoriser nos métadonnées d'image pour correspondre aux sorties d'images rognées et (2) extraire les images qui ont depuis été supprimées. Assurez-vous de consulter le notebook si vous souhaitez voir le code.

Après avoir exécuté le code du notebook, nous aurons un dossier `images_cropped` sur le disque contenant toutes les images rognées.

### Construction du modèle

Une fois que nous avons téléchargé les données, et les avons rognées et nettoyées, nous sommes prêts à entraîner le modèle.

Nous allons entraîner un [réseau de neurones convolutionnel](https://medium.freecodecamp.org/an-intuitive-guide-to-convolutional-neural-networks-260c2de0a050) (ou 'CNN') sur les données.

Les CNNs sont un type spécial de réseau de neurones qui construisent progressivement des caractéristiques de niveau supérieur à partir de groupes de pixels couramment trouvés dans les images.

La façon dont une image est notée sur ces diverses caractéristiques est ensuite pondérée pour générer un résultat de classification final.

Cette architecture fonctionne extrêmement bien car elle tire parti de la localité. En effet, tout pixel est susceptible d'avoir beaucoup plus en commun avec les pixels voisins qu'avec ceux qui sont éloignés.

Les CNNs ont également d'autres propriétés attrayantes, comme la tolérance au bruit et l'invariance d'échelle (dans une certaine mesure). Ces propriétés améliorent encore leurs capacités de classification.

Si vous n'êtes pas familier avec les CNNs, je recommande de parcourir l'excellent "[Comment fonctionnent les réseaux de neurones convolutionnels](https://brohrer.github.io/how_convolutional_neural_networks_work.html)" de Brandon Rohrer pour en apprendre davantage à leur sujet.

Nous allons entraîner un réseau de neurones convolutionnel très simple et voir comment même cela donne des résultats décents sur notre problème. J'utilise [Keras](https://keras.io/) pour définir et entraîner le modèle.

Nous commençons par disposer les images dans une certaine structure de répertoires :

```
images_cropped/    sandwich/        some_image.jpg        some_other_image.jpg        ...    hamburger/        yet_another_image.jpg        ...
```

Nous pointons ensuite Keras vers ce dossier en utilisant le code suivant :

Keras inspectera les dossiers d'entrée et déterminera qu'il y a deux classes dans notre problème de classification. Il assignera des noms de classes basés sur les noms des sous-dossiers et créera des "générateurs d'images" qui servent à partir de ces dossiers.

Mais nous ne retournons pas simplement les images elles-mêmes. Au lieu de cela, nous retournons des sélections aléatoirement sous-échantillonnées, inclinées et zoomées à partir des images (via `train_datagen.flow_from_directory`).

C'est un exemple d'augmentation de données en action.

L'augmentation de données est la pratique consistant à alimenter un classificateur d'images avec des versions aléatoirement rognées et déformées d'un ensemble de données d'entrée. Cela nous aide à surmonter la petite taille de notre ensemble de données. Nous pouvons entraîner notre modèle sur une seule image plusieurs fois. Chaque fois, nous utilisons un segment légèrement différent de l'image pré-traitée de manière légèrement différente.

Avec notre entrée de données définie, l'étape suivante consiste à définir le modèle lui-même :

C'est un modèle simple de réseau de neurones convolutionnel. Il contient seulement trois couches convolutionnelles : une seule couche de post-traitement densément connectée juste avant la couche de sortie, et une forte régularisation sous la forme d'une couche de dropout et d'une activation `relu`.

Toutes ces choses fonctionnent ensemble pour rendre plus difficile pour ce modèle de [surajuster](https://machinelearningmastery.com/overfitting-and-underfitting-with-machine-learning-algorithms/). Cela est important, étant donné la petite taille de notre ensemble de données d'entrée.

Enfin, la dernière étape consiste à ajuster le modèle.

Ce code sélectionne une taille de pas d'époque déterminée par notre taille d'échantillon d'image et la taille de lot choisie (16). Ensuite, il s'entraîne sur ces données pendant 50 époques.

L'entraînement est susceptible d'être suspendu tôt par le rappel `EarlyStopping`. Cela retourne le modèle le mieux performant avant la limite de 50 époques s'il ne voit pas d'amélioration dans le score de validation dans les quatre époques précédentes.

Nous avons sélectionné une valeur de patience aussi grande car il y a une quantité significative de variabilité dans la perte de validation du modèle.

Ce simple régime d'entraînement donne un modèle avec une précision d'environ 75 % :

```
              precision    recall  f1-score   support           0       0.90      0.59      0.71      1399           1       0.64      0.92      0.75      1109   micro avg       0.73      0.73      0.73      2508   macro avg       0.77      0.75      0.73      2508weighted avg       0.78      0.73      0.73      2508
```

Il est intéressant de noter que notre modèle est sous-confiant lorsqu'il classe les hamburgers (classe 0), mais surconfiant lorsqu'il classe les hamburgers (classe 1).

90 % des images classées comme hamburgers sont en fait des hamburgers. Mais seulement 59 % de tous les hamburgers réels sont classés correctement.

D'un autre côté, seulement 64 % des images classées comme sandwichs sont en fait des sandwichs. Mais 92 % des sandwichs sont classés correctement.

Ces résultats sont en ligne avec la précision de 80 % obtenue par Francois Chollet en appliquant un modèle très similaire à un sous-ensemble de taille similaire du classique [Cats versus Dogs](https://www.kaggle.com/c/dogs-vs-cats).

La différence est probablement principalement due à l'augmentation du niveau d'occlusion et de bruit dans l'ensemble de données Google Open Images V4.

L'ensemble de données inclut également des illustrations ainsi que des images photographiques. Celles-ci prennent parfois de grandes libertés artistiques, rendant la classification plus difficile. Vous pouvez choisir de les supprimer lors de la construction d'un modèle vous-même.

Cette performance peut être encore améliorée en utilisant des techniques d'[apprentissage par transfert](https://towardsdatascience.com/keras-transfer-learning-for-beginners-6c9b8b7143e). Pour en savoir plus, consultez l'article de blog de l'auteur de Keras, Francois Chollet, "[Building powerful image classification models using very little data](https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html)".

### Distribution du modèle

Maintenant que nous avons construit un ensemble de données personnalisé et entraîné un modèle, ce serait dommage de ne pas le partager.

Les projets de Machine Learning doivent être reproductibles. J'ai décrit la stratégie suivante dans un article précédent, "[Reproduire une construction de modèle de machine learning en quatre lignes de code](https://blog.quiltdata.com/reproduce-a-machine-learning-model-build-in-four-lines-of-code-b4f0a5c5f8c8)".

* Séparer les dépendances en données, code et composants d'environnement.
* Le contrôle de version des dépendances de données (1) la définition du modèle et (2) les données d'entraînement. Sauvegardez ces éléments dans un stockage d'objets versionné, par exemple [Amazon S3](https://aws.amazon.com/s3/) avec [Quilt T4](https://github.com/quiltdata/t4).
* Le contrôle de version des dépendances de code contrôle le code utilisé pour entraîner le modèle (utilisez git).
* Le contrôle de version des dépendances d'environnement contrôle l'environnement utilisé pour entraîner le modèle. Dans un environnement de production, cela devrait probablement être un fichier Docker, mais vous pouvez utiliser `pip` ou `conda` localement.
* Pour fournir à quelqu'un une copie réentraînable du modèle, donnez-lui le tuple `{data, code, environment}` correspondant.

En suivant ces principes, obtenir tout ce dont vous avez besoin pour entraîner votre propre copie de ce modèle tient en quelques lignes de code :

```
git clone https://github.com/quiltdata/open-images.gitconda env create -f open-images/environment.ymlsource activate quilt-open-images-devpython -c "import t4; t4.Package.install('quilt/open_images', dest='open-images/', registry='s3://quilt-example')"
```

Pour en savoir plus sur `{data, code, environment}`, consultez [le dépôt GitHub](https://github.com/quiltdata/open-images) et/ou [l'article correspondant](https://blog.quiltdata.com/reproduce-a-machine-learning-model-build-in-four-lines-of-code-b4f0a5c5f8c8).

### Conclusion

Dans cet article, nous avons démontré un pipeline de machine learning de classification d'images de bout en bout. Nous avons couvert tout, du téléchargement/transformation d'un ensemble de données à l'entraînement d'un modèle. Nous l'avons ensuite distribué de manière à ce que n'importe qui puisse le reconstruire lui-même plus tard.

Parce que les ensembles de données personnalisés sont difficiles à générer et à distribuer, au fil du temps, un groupe d'ensembles de données exemples qui sont utilisés partout a émergé. Ce n'est pas parce qu'ils sont réellement bons (ils ne le sont pas). Au lieu de cela, c'est parce qu'ils sont faciles.

Par exemple, le cours intensif de Machine Learning récemment publié par Google utilise largement l'[ensemble de données sur le logement en Californie](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html). Ces données ont maintenant presque deux décennies !

Envisagez plutôt d'explorer de nouveaux horizons. Utilisez des images réelles provenant de l'Internet vivant avec des décompositions catégorielles intéressantes. C'est plus facile que vous ne le pensez !