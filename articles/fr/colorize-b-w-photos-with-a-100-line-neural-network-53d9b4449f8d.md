---
title: Comment coloriser des photos en noir et blanc avec seulement 100 lignes de
  code de réseau de neurones
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-29T15:02:49.000Z'
originalURL: https://freecodecamp.org/news/colorize-b-w-photos-with-a-100-line-neural-network-53d9b4449f8d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Wk43GNwKLB4kYjQt5i8ntQ.png
tags:
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Comment coloriser des photos en noir et blanc avec seulement 100 lignes
  de code de réseau de neurones
seo_desc: 'By Emil Wallner

  Earlier this year, Amir Avni used neural networks to troll the subreddit/r/Colorization
  — a community where people colorize historical black and white images manually using
  Photoshop.

  They were astonished with Amir’s deep learning bot...'
---

Par Emil Wallner

Plus tôt cette année, Amir Avni a utilisé des réseaux de neurones pour [troller le subreddit](http://www.whatimade.today/our-frst-reddit-bot-coloring-b-2/)/r/Colorization — une communauté où les gens colorisent manuellement des images historiques en noir et blanc en utilisant Photoshop.

Ils étaient stupéfaits par le bot de deep learning d'Amir. Ce qui pouvait prendre jusqu'à un mois de travail manuel pouvait maintenant être fait en quelques secondes.

J'étais fasciné par le réseau de neurones d'Amir, alors je l'ai reproduit et documenté le processus. Commençons par regarder certains des résultats/échecs de mes expériences (faites défiler jusqu'en bas pour le résultat final).

![Image](https://cdn-media-1.freecodecamp.org/images/z-NKnwq8RlBQ1CAnXUylT1B-DlSZQgby-Urw)
_Les images originales en noir et blanc proviennent d'Unsplash_

Aujourd'hui, la colorisation est généralement faite à la main dans Photoshop. Pour apprécier tout le travail acharné derrière ce processus, jetez un coup d'œil à cette magnifique vidéo de colorisation mémoire :

En bref, une image peut prendre jusqu'à un mois à coloriser. Cela nécessite des recherches approfondies. Un visage seul nécessite jusqu'à 20 couches de nuances roses, vertes et bleues pour obtenir le bon rendu.

Cet article est pour les débutants. Pourtant, si vous êtes nouveau dans la terminologie du deep learning, vous pouvez lire mes deux précédents articles [ici](https://blog.floydhub.com/my-first-weekend-of-deep-learning/) et [ici](https://blog.floydhub.com/coding-the-history-of-deep-learning/), et regarder la [conférence](https://www.youtube.com/watch?v=LxfUGhug-iQ) d'Andrej Karpathy pour plus de contexte.

Je vais vous montrer comment construire votre propre réseau de neurones de colorisation en trois étapes.

La première section décompose la logique principale. Nous construirons un réseau de neurones minimaliste de 40 lignes en tant que bot de colorisation « alpha ». Il n'y a pas beaucoup de magie dans ce snippet de code. Cela nous aidera à nous familiariser avec la syntaxe.

L'étape suivante consiste à créer un réseau de neurones capable de généraliser — notre version « bêta ». Nous pourrons coloriser des images que le bot n'a jamais vues auparavant.

Pour notre version « finale », nous combinerons notre réseau de neurones avec un classificateur. Nous utiliserons un [Inception Resnet V2](https://research.googleblog.com/2016/08/improving-inception-and-image.html) qui a été entraîné sur 1,2 million d'images. Pour rendre les couleurs plus vives, nous entraînerons notre réseau de neurones sur des portraits de [Unsplash](https://unsplash.com/).

Si vous voulez voir ce qui vous attend, voici un [Jupyter Notebook](https://www.floydhub.com/emilwallner/projects/color/43/code/Alpha-version/alpha_version.ipynb) avec la version Alpha de notre bot. Vous pouvez également consulter les trois versions sur [FloydHub](https://www.floydhub.com/emilwallner/projects/color/43/code) et [GitHub](https://github.com/emilwallner/Coloring-greyscale-images-in-Keras), ainsi que le code pour [toutes les expériences](https://www.floydhub.com/emilwallner/projects/color/jobs) que j'ai exécutées sur les GPU cloud de FloydHub.

### Logique principale

Dans cette section, je vais expliquer comment rendre une image, les bases des couleurs numériques et la logique principale de notre réseau de neurones.

Les images en noir et blanc peuvent être représentées en grilles de pixels. Chaque pixel a une valeur qui correspond à sa luminosité. Les valeurs vont de 0 à 255, du noir au blanc.

![Image](https://cdn-media-1.freecodecamp.org/images/-E40goEdeMZCIl7UH8vGN1BBe7AQXAngQkQ0)

Les images en couleur se composent de trois couches : une couche rouge, une couche verte et une couche bleue. Cela peut vous sembler contre-intuitif. Imaginez diviser une feuille verte sur un fond blanc en trois canaux. Intuitivement, vous pourriez penser que la plante n'est présente que dans la couche verte.

Mais, comme vous pouvez le voir ci-dessous, la feuille est présente dans les trois canaux. Les couches ne déterminent pas seulement la couleur, mais aussi la luminosité.

![Image](https://cdn-media-1.freecodecamp.org/images/mq8HhFZvcoGr4kxzjelwOzbyvrf2SMKgDxNj)

Pour obtenir la couleur blanche, par exemple, vous avez besoin d'une distribution égale de toutes les couleurs. En ajoutant une quantité égale de rouge et de bleu, cela rend le vert plus lumineux. Ainsi, une image en couleur encode la couleur et le contraste en utilisant trois couches :

![Image](https://cdn-media-1.freecodecamp.org/images/JKLZUfQIv5Wu55lep9EN4MZmDozm4tryBjLW)

Tout comme les images en noir et blanc, chaque couche dans une image en couleur a une valeur de 0 à 255. La valeur 0 signifie qu'elle n'a pas de couleur dans cette couche. Si la valeur est 0 pour tous les canaux de couleur, alors le pixel de l'image est noir.

Comme vous le savez peut-être, un réseau de neurones crée une relation entre une valeur d'entrée et une valeur de sortie. Pour être plus précis avec notre tâche de colorisation, le réseau doit trouver les traits qui relient les images en niveaux de gris avec les images colorées.

En somme, nous recherchons les caractéristiques qui relient une grille de valeurs en niveaux de gris aux trois grilles de couleurs.

![Image](https://cdn-media-1.freecodecamp.org/images/4AueuCZR9MRkEnl1pQbIa6J1IXu7GaEC81Rz)
_f() est le réseau de neurones, [N&B] est notre entrée, et [R],[G],[B] est notre sortie._

### Version Alpha

Nous allons commencer par créer une version simple de notre réseau de neurones pour coloriser une image du visage d'une femme. Ainsi, vous pouvez vous familiariser avec la syntaxe principale de notre modèle au fur et à mesure que nous ajoutons des fonctionnalités.

Avec seulement 40 lignes de code, nous pouvons effectuer la transition suivante. L'image du milieu est réalisée avec notre réseau de neurones et l'image de droite est la photo couleur originale. Le réseau est entraîné et testé sur la même image — nous reviendrons sur ce point lors de la version bêta.

![Image](https://cdn-media-1.freecodecamp.org/images/i0BF0Lhq7FP1JHbY52n9Ex9WpvwqjAXSAsJU)
_Photo par Camila Cordeiro_

#### Espace colorimétrique

Tout d'abord, nous utiliserons un algorithme pour changer les canaux de couleur, de RGB à Lab. **_L_** signifie luminosité, et **_a_** et **_b_** pour les spectres de couleur vert-rouge et bleu-jaune.

Comme vous pouvez le voir ci-dessous, une image encodée en Lab a une couche pour les niveaux de gris, et a compacté trois couches de couleur en deux. Cela signifie que nous pouvons utiliser l'image en niveaux de gris originale dans notre prédiction finale. De plus, nous n'avons que deux canaux à prédire.

![Image](https://cdn-media-1.freecodecamp.org/images/dVUUskOODMzF5O2K0yV1TDM8Cuseb7jB6Y8D)

Fait scientifique — 94 % des cellules de nos yeux déterminent la luminosité. Cela laisse seulement 6 % de nos récepteurs pour agir comme capteurs pour les couleurs. Comme vous pouvez le voir dans l'image ci-dessus, l'image en niveaux de gris est beaucoup plus nette que les couches de couleur. C'est une autre raison de garder l'image en niveaux de gris dans notre prédiction finale.

#### De N&B à la couleur

Notre prédiction finale ressemble à ceci. Nous avons une couche en niveaux de gris pour l'entrée, et nous voulons prédire deux couches de couleur, les **ab** dans **Lab**. Pour créer l'image couleur finale, nous inclurons l'image **L**/niveaux de gris que nous avons utilisée pour l'entrée. Le résultat sera la création d'une image **Lab**.

![Image](https://cdn-media-1.freecodecamp.org/images/3spQqgv2ssg6UQbeWv7tojgxmhZEj9VFEYX8)

Pour transformer une couche en deux couches, nous utilisons des filtres de convolution. Pensez à eux comme les filtres bleus/rouges dans les lunettes 3D. Chaque filtre détermine ce que nous voyons dans une image. Ils peuvent mettre en évidence ou supprimer quelque chose pour extraire des informations de l'image. Le réseau peut soit créer une nouvelle image à partir d'un filtre, soit combiner plusieurs filtres en une seule image.

Pour un réseau de neurones convolutionnel, chaque filtre est automatiquement ajusté pour aider au résultat souhaité. Nous commencerons par empiler des centaines de filtres et les réduire à deux couches, les couches **a** et **b**.

Avant d'entrer dans les détails de son fonctionnement, exécutons le code.

#### Exécuter le code sur FloydHub

Cliquez sur le bouton ci-dessous pour ouvrir un [Workspace](https://blog.floydhub.com/workspaces/) sur [FloydHub](https://www.floydhub.com/?utm_medium=readme&utm_source=colornet&utm_campaign=aug_2018) où vous trouverez le même environnement et le même jeu de données utilisés pour la _version complète_. Vous pouvez également trouver les modèles entraînés pour [Serving](https://github.com/floydhub/colornet-template#serve-an-interactive-web-page-for-your-own-model).

![Image](https://cdn-media-1.freecodecamp.org/images/Xf2GlQ87eVy8vc7PnY3fWpGJ0ep4QNxB8QQv)

Vous pouvez également faire une installation locale de FloydHub avec leur [installation en 2 minutes](https://www.floydhub.com/), regarder mon [tutoriel vidéo de 5 minutes](https://www.youtube.com/watch?v=byLQ9kgjTdQ&t=6s) ou consulter mon [guide étape par étape](https://blog.floydhub.com/my-first-weekend-of-deep-learning/). C'est la meilleure (et la plus facile) façon d'entraîner des modèles de deep learning sur des GPU cloud.

#### Version Alpha

Une fois FloydHub installé, utilisez les commandes suivantes :

```
git clone https://github.com/emilwallner/Coloring-greyscale-images-in-Keras
```

Ouvrez le dossier et initialisez FloydHub.

```
cd Coloring-greyscale-images-in-Keras/floydhubfloyd init colornet
```

Le tableau de bord web de FloydHub s'ouvrira dans votre navigateur. Vous serez invité à créer un nouveau projet FloydHub appelé `colornet`. Une fois cela fait, retournez à votre terminal et exécutez la même commande `init`.

```
floyd init colornet
```

D'accord, exécutons notre travail :

```
floyd run --data emilwallner/datasets/colornet/2:data --mode jupyter --tensorboard
```

Quelques notes rapides sur notre travail :

* Nous avons monté un jeu de données public sur FloydHub (que j'ai déjà téléchargé) dans le répertoire `data` avec la ligne ci-dessous :

```
--dataemilwallner/datasets/colornet/2:data
```

Vous pouvez explorer et utiliser ce jeu de données (et de nombreux autres jeux de données publics) en le visualisant sur [FloydHub](https://www.floydhub.com/emilwallner/datasets/cifar-10/1)

* Nous avons activé Tensorboard avec `--tensorboard`
* Nous avons exécuté le travail en mode Jupyter Notebook avec `--mode jupyter`
* Si vous avez des crédits GPU, vous pouvez également ajouter le drapeau GPU `--gpu` à votre commande. Cela le rendra environ 50 fois plus rapide

Allez dans le notebook Jupyter. Sous l'onglet Jobs sur le site web de FloydHub, cliquez sur le lien Jupyter Notebook et naviguez jusqu'à ce fichier :

```
floydhub/Alpha version/working_floyd_pink_light_full.ipynb
```

Ouvrez-le et cliquez sur Shift+Enter sur toutes les cellules.

Augmentez progressivement la valeur de l'époque pour avoir une idée de la façon dont le réseau de neurones apprend.

```
model.fit(x=X, y=Y, batch_size=1, epochs=1)
```

Commencez avec une valeur d'époque de 1 et augmentez-la à 10, 100, 500, 1000 et 3000. La valeur de l'époque indique combien de fois le réseau de neurones apprend de l'image. Vous trouverez l'image `img_result.png` dans le dossier principal une fois que vous aurez entraîné votre réseau de neurones.

```
# Get imagesimage = img_to_array(load_img('woman.png'))image = np.array(image, dtype=float)
```

```
# Import map images into the lab colorspaceX = rgb2lab(1.0/255*image)[:,:,0]Y = rgb2lab(1.0/255*image)[:,:,1:]Y = Y / 128X = X.reshape(1, 400, 400, 1)Y = Y.reshape(1, 400, 400, 2)
```

```
# Building the neural networkmodel = Sequential()model.add(InputLayer(input_shape=(None, None, 1)))model.add(Conv2D(8, (3, 3), activation='relu', padding='same', strides=2))model.add(Conv2D(8, (3, 3), activation='relu', padding='same'))model.add(Conv2D(16, (3, 3), activation='relu', padding='same'))model.add(Conv2D(16, (3, 3), activation='relu', padding='same', strides=2))model.add(Conv2D(32, (3, 3), activation='relu', padding='same'))model.add(Conv2D(32, (3, 3), activation='relu', padding='same', strides=2))model.add(UpSampling2D((2, 2)))model.add(Conv2D(32, (3, 3), activation='relu', padding='same'))model.add(UpSampling2D((2, 2)))model.add(Conv2D(16, (3, 3), activation='relu', padding='same'))model.add(UpSampling2D((2, 2)))model.add(Conv2D(2, (3, 3), activation='tanh', padding='same'))
```

```
# Finish modelmodel.compile(optimizer='rmsprop',loss='mse')
```

```
#Train the neural networkmodel.fit(x=X, y=Y, batch_size=1, epochs=3000)print(model.evaluate(X, Y, batch_size=1))
```

```
# Output colorizationsoutput = model.predict(X)output = output * 128canvas = np.zeros((400, 400, 3))canvas[:,:,0] = X[0][:,:,0]canvas[:,:,1:] = output[0]imsave("img_result.png", lab2rgb(canvas))imsave("img_gray_scale.png", rgb2gray(lab2rgb(canvas)))
```

Commande FloydHub pour exécuter ce réseau :

```
floyd run --data emilwallner/datasets/colornet/2:data --mode jupyter --tensorboard
```

#### Explication technique

Pour résumer, l'entrée est une grille représentant une image en noir et blanc. Elle produit deux grilles avec des valeurs de couleur. Entre les valeurs d'entrée et de sortie, nous créons des filtres pour les relier ensemble. Il s'agit d'un réseau de neurones convolutionnel.

Lorsque nous entraînons le réseau, nous utilisons des images en couleur. Nous convertissons les couleurs RVB en espace colorimétrique Lab. La couche en noir et blanc est notre entrée et les deux couches colorées sont la sortie.

![Image](https://cdn-media-1.freecodecamp.org/images/DonLhWNz4wst7PZn1ZSYSfEfY9O5h9vvr8dh)

À gauche, nous avons l'entrée N&B, nos filtres et la prédiction de notre réseau de neurones.

Nous mappons les valeurs prédites et les valeurs réelles dans le même intervalle. Ainsi, nous pouvons comparer les valeurs. L'intervalle varie de -1 à 1. Pour mapper les valeurs prédites, nous utilisons une fonction d'activation tanh. Pour toute valeur que vous donnez à la [fonction tanh](http://mathworld.wolfram.com/HyperbolicTangent.html), elle retournera -1 à 1.

Les vraies valeurs de couleur varient entre -128 et 128. Il s'agit de l'intervalle par défaut dans l'espace colorimétrique Lab. En les divisant par 128, elles tombent également dans l'intervalle -1 à 1. Cette « normalisation » nous permet de comparer l'erreur de notre prédiction.

Après avoir calculé l'erreur finale, le réseau met à jour les filtres pour réduire l'erreur totale. Le réseau continue dans cette boucle jusqu'à ce que l'erreur soit aussi faible que possible.

Clarifions quelques syntaxes dans le snippet de code.

```
X = rgb2lab(1.0/255*image)[:,:,0]Y = rgb2lab(1.0/255*image)[:,:,1:]
```

**1.0/255** indique que nous utilisons un espace colorimétrique RVB 24 bits. Cela signifie que nous utilisons des nombres entre 0 et 255 pour chaque canal de couleur. Cela donne 16,7 millions de combinaisons de couleurs.

Puisque les humains ne peuvent percevoir que 2 à 10 millions de couleurs, il n'est pas très utile d'utiliser un espace colorimétrique plus grand.

```
Y = Y / 128
```

L'espace colorimétrique Lab a une plage différente par rapport au RVB. Le spectre de couleur **ab** dans Lab varie de -128 à 128. En divisant toutes les valeurs dans la couche de sortie par 128, nous limitons la plage entre -1 et 1.

Nous la faisons correspondre avec notre réseau de neurones, qui retourne également des valeurs entre -1 et 1.

Après avoir converti l'espace colorimétrique en utilisant la fonction `rgb2lab()`, nous sélectionnons la couche en niveaux de gris avec : `**[ : , : , 0].**` Il s'agit de notre entrée pour le réseau de neurones. `[ : , : , 1: ]` sélectionne les deux couches de couleur, vert-rouge et bleu-jaune.

Après avoir entraîné le réseau de neurones, nous faisons une prédiction finale que nous convertissons en une image.

```
output = model.predict(X)output = output * 128
```

Ici, nous utilisons une image en niveaux de gris comme entrée et la faisons passer à travers notre réseau de neurones entraîné. Nous prenons toutes les valeurs de sortie entre -1 et 1 et les multiplions par 128. Cela nous donne la bonne couleur dans le spectre colorimétrique Lab.

```
canvas = np.zeros((400, 400, 3))canvas[:,:,0] = X[0][:,:,0]canvas[:,:,1:] = output[0]
```

Enfin, nous créons une toile RGB noire en la remplissant de trois couches de 0. Ensuite, nous copions la couche en niveaux de gris de notre image de test. Ensuite, nous ajoutons nos deux couches de couleur à la toile RGB. Ce tableau de valeurs de pixels est ensuite converti en une image.

#### Points clés de la version Alpha

* **Lire des articles de recherche est un défi.** Une fois que j'ai résumé les caractéristiques principales de chaque article, il est devenu plus facile de parcourir les articles. Cela m'a également permis de mettre les détails dans un contexte.
* **Commencer simplement est la clé.** La plupart des implémentations que je pouvais trouver en ligne faisaient 2 à 10K lignes de long. Cela rendait difficile l'obtention d'une vue d'ensemble de la logique principale du problème. Une fois que j'ai eu une version minimaliste, il est devenu plus facile de lire à la fois l'implémentation du code et les articles de recherche.
* **Explorez des projets publics.** Pour avoir une idée approximative de ce qu'il faut coder, j'ai parcouru 50 à 100 projets sur la colorisation sur Github.
* **Les choses ne fonctionneront pas toujours comme prévu.** Au début, il ne pouvait créer que des couleurs rouges et jaunes. Au début, j'avais une fonction d'activation Relu pour l'activation finale. Puisqu'elle ne mappe les nombres qu'en chiffres positifs, elle ne pouvait pas créer de valeurs négatives, les spectres bleu et vert. L'ajout d'une fonction d'activation tanh et le mappage des valeurs Y ont corrigé cela.
* **Compréhension > Vitesse.** Beaucoup des implémentations que j'ai vues étaient rapides mais difficiles à utiliser. J'ai choisi d'optimiser pour la vitesse d'innovation plutôt que pour la vitesse du code.

### Version Bêta

Pour comprendre la faiblesse de la version alpha, essayez de coloriser une image sur laquelle elle n'a pas été entraînée. Si vous essayez, vous verrez qu'elle fait une mauvaise tentative. C'est parce que le réseau a mémorisé les informations. Il n'a pas appris à coloriser une image qu'il n'a jamais vue auparavant. Mais c'est ce que nous allons faire dans la version bêta. Nous allons enseigner à notre réseau à généraliser.

Ci-dessous se trouve le résultat de la colorisation des images de validation avec notre version bêta.

Au lieu d'utiliser Imagenet, j'ai créé [un jeu de données public sur FloydHub](https://www.floydhub.com/emilwallner/datasets/colornet) avec des images de meilleure qualité. Les images proviennent d'[Unsplash](https://unsplash.com/) — des photos en licence creative commons par des photographes professionnels. Il comprend 9 500 images d'entraînement et 500 images de validation.

![Image](https://cdn-media-1.freecodecamp.org/images/BZBm1qEEWFclSw-S6LQavmedTm0ijiGaqD78)

#### L'extracteur de caractéristiques

Notre réseau de neurones trouve des caractéristiques qui relient les images en niveaux de gris à leurs versions colorées.

Imaginez que vous deviez coloriser des images en noir et blanc — mais avec la restriction de ne pouvoir voir que neuf pixels à la fois. Vous pourriez scanner chaque image de haut en bas et de gauche à droite et essayer de prédire quelle couleur chaque pixel devrait avoir.

![Image](https://cdn-media-1.freecodecamp.org/images/mt-qv1Zp-Cjw2hUpTaVp9LyQmeIpD0GKKM1G)

Par exemple, ces neuf pixels sont le bord de la narine de la femme juste au-dessus. Comme vous pouvez l'imaginer, il serait presque impossible de faire une bonne colorisation, alors vous le décomposez en étapes.

Tout d'abord, vous cherchez des motifs simples : une ligne diagonale, tous les pixels noirs, et ainsi de suite. Vous cherchez le même motif exact dans chaque carré et supprimez les pixels qui ne correspondent pas. Vous générez 64 nouvelles images à partir de vos 64 mini-filtres.

![Image](https://cdn-media-1.freecodecamp.org/images/vIOjTTUiUF5BAIn62BAN6EceZEbCFmD-AcOo)
_Le nombre d'images filtrées pour chaque étape_

Si vous scannez à nouveau les images, vous verrez les mêmes petits motifs que vous avez déjà détectés. Pour obtenir une compréhension de plus haut niveau de l'image, vous réduisez la taille de l'image de moitié.

![Image](https://cdn-media-1.freecodecamp.org/images/5QylrDkthjNwYWqjVhOhUy2yifuRILeNpm6r)
_Nous réduisons la taille en trois étapes_

Vous avez toujours un filtre 3x3 pour scanner chaque image. Mais en combinant vos neuf nouveaux pixels avec vos filtres de bas niveau, vous pouvez détecter des motifs plus complexes. Une combinaison de pixels peut former un demi-cercle, un petit point ou une ligne. Encore une fois, vous extrayez le même motif de l'image de manière répétée. Cette fois, vous générez 128 nouvelles images filtrées.

Après quelques étapes, les images filtrées que vous produisez peuvent ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/RnFvJJmiQVJXIXa36EwYyEhKSoeLi1S4-l0U)
_De Keras layer tutorial_

Comme mentionné, vous commencez par des caractéristiques de bas niveau, comme un bord. Les couches plus proches de la sortie sont combinées en motifs. Ensuite, elles sont combinées en détails, et finalement transformées en un visage. Ce [tutoriel vidéo](https://www.youtube.com/watch?v=AgkfIQ4IGaM) fournit une explication supplémentaire.

Le processus est similaire à celui de la plupart des réseaux de neurones qui traitent de la vision. Le type de réseau ici est connu sous le nom de réseau de neurones convolutionnel. Dans ces réseaux, vous combinez plusieurs images filtrées pour comprendre le contexte de l'image.

#### De l'extraction de caractéristiques à la couleur

Le réseau de neurones fonctionne de manière essai-erreur. Il fait d'abord une prédiction aléatoire pour chaque pixel. En fonction de l'erreur pour chaque pixel, il travaille en arrière à travers le réseau pour améliorer l'extraction de caractéristiques.

Il commence par ajuster les situations qui génèrent les plus grandes erreurs. Dans ce cas, les ajustements sont : colorier ou non, et comment localiser différents objets.

Le réseau commence par colorier tous les objets en brun. C'est la couleur qui est la plus similaire à toutes les autres couleurs, produisant ainsi la plus petite erreur.

Parce que la plupart des données d'entraînement sont assez similaires, le réseau a du mal à différencier les différents objets. Il échouera à générer des couleurs plus nuancées. C'est ce que nous explorerons dans la version complète.

Ci-dessous se trouve le code pour la version bêta, suivi d'une explication technique du code.

```
# Get imagesX = []for filename in os.listdir('../Train/'):    X.append(img_to_array(load_img('../Train/'+filename)))X = np.array(X, dtype=float)
```

```
# Set up training and test datasplit = int(0.95*len(X))Xtrain = X[:split]Xtrain = 1.0/255*Xtrain
```

```
#Design the neural networkmodel = Sequential()model.add(InputLayer(input_shape=(256, 256, 1)))model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))model.add(Conv2D(64, (3, 3), activation='relu', padding='same', strides=2))model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))model.add(Conv2D(128, (3, 3), activation='relu', padding='same', strides=2))model.add(Conv2D(256, (3, 3), activation='relu', padding='same'))model.add(Conv2D(256, (3, 3), activation='relu', padding='same', strides=2))model.add(Conv2D(512, (3, 3), activation='relu', padding='same'))model.add(Conv2D(256, (3, 3), activation='relu', padding='same'))model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))model.add(UpSampling2D((2, 2)))model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))model.add(UpSampling2D((2, 2)))model.add(Conv2D(32, (3, 3), activation='relu', padding='same'))model.add(Conv2D(2, (3, 3), activation='tanh', padding='same'))model.add(UpSampling2D((2, 2)))
```

```
# Finish modelmodel.compile(optimizer='rmsprop', loss='mse')
```

```
# Image transformerdatagen = ImageDataGenerator(        shear_range=0.2,        zoom_range=0.2,        rotation_range=20,        horizontal_flip=True)
```

```
# Generate training databatch_size = 50def image_a_b_gen(batch_size):    for batch in datagen.flow(Xtrain, batch_size=batch_size):        lab_batch = rgb2lab(batch)        X_batch = lab_batch[:,:,:,0]        Y_batch = lab_batch[:,:,:,1:] / 128        yield (X_batch.reshape(X_batch.shape+(1,)), Y_batch)
```

```
# Train modelTensorBoard(log_dir='/output')model.fit_generator(image_a_b_gen(batch_size), steps_per_epoch=10000, epochs=1)# Test imagesXtest = rgb2lab(1.0/255*X[split:])[:,:,:,0]Xtest = Xtest.reshape(Xtest.shape+(1,))Ytest = rgb2lab(1.0/255*X[split:])[:,:,:,1:]Ytest = Ytest / 128print model.evaluate(Xtest, Ytest, batch_size=batch_size)
```

```
# Load black and white imagescolor_me = []for filename in os.listdir('../Test/'):        color_me.append(img_to_array(load_img('../Test/'+filename)))color_me = np.array(color_me, dtype=float)color_me = rgb2lab(1.0/255*color_me)[:,:,:,0]color_me = color_me.reshape(color_me.shape+(1,))
```

```
# Test modeloutput = model.predict(color_me)output = output * 128
```

```
# Output colorizationsfor i in range(len(output)):        cur = np.zeros((256, 256, 3))        cur[:,:,0] = color_me[i][:,:,0]        cur[:,:,1:] = output[i]        imsave("result/img_"+str(i)+".png", lab2rgb(cur))
```

Voici la commande FloydHub pour exécuter le réseau de neurones Bêta :

```
floyd run --data emilwallner/datasets/colornet/2:data --mode jupyter --tensorboard
```

#### Explication technique

La principale différence avec les autres réseaux de neurones visuels est l'importance de la localisation des pixels. Dans les réseaux de colorisation, la taille ou le ratio de l'image reste le même tout au long du réseau. Dans d'autres types de réseaux, l'image se déforme à mesure qu'elle se rapproche de la couche finale.

Les couches de max-pooling dans les réseaux de classification augmentent la densité d'information, mais déforment également l'image. Elles ne valorisent que l'information, mais pas la disposition d'une image. Dans les réseaux de colorisation, nous utilisons plutôt un stride de 2, pour diminuer la largeur et la hauteur de moitié. Cela augmente également la densité d'information mais ne déforme pas l'image.

![Image](https://cdn-media-1.freecodecamp.org/images/z3panAJJuAKxXonehTzjD2h3jbQ60ByVsNT6)

Deux autres différences sont : les couches de suréchantillonnage et le maintien du ratio de l'image. Les réseaux de classification ne se soucient que de la classification finale. Par conséquent, ils continuent à réduire la taille et la qualité de l'image à mesure qu'elle se déplace dans le réseau.

Les réseaux de colorisation maintiennent le ratio de l'image constant. Cela est fait en ajoutant un remplissage blanc comme la visualisation ci-dessus. Sinon, chaque couche convolutionnelle coupe les images. Cela est fait avec le paramètre `*padding='same'*`.

Pour doubler la taille de l'image, le réseau de colorisation utilise [une couche de suréchantillonnage](https://keras.io/layers/convolutional/#upsampling2d).

```
for filename in os.listdir('/Color_300/Train/'):    X.append(img_to_array(load_img('/Color_300/Test'+filename)))
```

Cette boucle for compte d'abord tous les noms de fichiers dans le répertoire. Ensuite, elle itère à travers le répertoire d'images et convertit les images en un tableau de pixels. Enfin, elle les combine en un vecteur géant.

```
datagen = ImageDataGenerator(        shear_range=0.2,        zoom_range=0.2,        rotation_range=20,        horizontal_flip=True)
```

Avec `[ImageDataGenerator](https://keras.io/preprocessing/image/)`, nous ajustons les paramètres de notre générateur d'images. Ainsi, chaque image ne sera jamais la même, améliorant ainsi le taux d'apprentissage. Le `shear_range` incline l'image vers la gauche ou la droite, et les autres paramètres sont le zoom, la rotation et le retournement horizontal.

```
batch_size = 50def image_a_b_gen(batch_size):    for batch in datagen.flow(Xtrain, batch_size=batch_size):        lab_batch = rgb2lab(batch)        X_batch = lab_batch[:,:,:,0]        Y_batch = lab_batch[:,:,:,1:] / 128        yield (X_batch.reshape(X_batch.shape+(1,)), Y_batch)
```

Nous utilisons les images de notre dossier, Xtrain, pour générer des images basées sur les paramètres ci-dessus. Ensuite, nous extrayons la couche noir et blanc pour le `X_batch` et les deux couleurs pour les deux couches de couleur.

```
model.fit_generator(image_a_b_gen(batch_size), steps_per_epoch=1, epochs=1000)
```

Plus le GPU que vous avez est puissant, plus vous pouvez y mettre d'images. Avec cette configuration, vous pouvez utiliser 50 à 100 images. `steps_per_epoch` est calculé en divisant le nombre d'images d'entraînement par votre taille de lot.

Par exemple : 100 images avec une taille de lot de 50 donne 2 étapes par époque. Le nombre d'époques détermine combien de fois vous voulez entraîner toutes les images. 10K images avec 21 époques prendra environ 11 heures sur un GPU Tesla K80.

#### Points clés

* **Exécutez beaucoup d'expériences en petits lots avant de faire des exécutions plus grandes.** Même après 20 à 30 expériences, j'ai encore trouvé des erreurs. Juste parce que cela fonctionne ne signifie pas que cela fonctionne correctement. Les bugs dans un réseau de neurones sont souvent plus nuancés que les erreurs de programmation traditionnelles. L'un des plus bizarres était [mon hoquet Adam](https://twitter.com/EmilWallner/status/916309564966006784).
* **Un ensemble de données plus diversifié rend les images brunâtres.** Si vous avez [des images très similaires](https://github.com/2014mchidamb/DeepColorization/tree/master/face_images), vous pouvez obtenir un résultat décent sans avoir besoin d'une architecture plus complexe. Le compromis est que le réseau devient moins bon pour généraliser.
* **Formes, formes et formes.** La taille de chaque image doit être exacte et rester proportionnelle tout au long du réseau. Au début, j'ai utilisé une taille d'image de 300. La diviser par deux trois fois donne des tailles de 150, 75 et 35,5. Le résultat est la perte d'un demi-pixel ! Cela a conduit à de nombreux « hacks » jusqu'à ce que je réalise qu'il est préférable d'utiliser une puissance de deux : 2, 8, 16, 32, 64, 256 et ainsi de suite.
* **Création de jeux de données :** a) [Désactivez](http://osxdaily.com/2010/02/03/how-to-prevent-ds_store-file-creation/) le fichier .DS_Store, il m'a rendu fou. b) Soyez créatif. J'ai fini avec un script [console Chrome](https://github.com/emilwallner/useful-scripts/blob/master/auto_scroll_browser_window_console) et [une extension](https://chrome.google.com/webstore/detail/imagespark-ultimate-image/hooaoionkjogngfhjjniefmenehnopag) pour télécharger les fichiers. c) Faites une copie des fichiers bruts que vous scrapez et structurez vos [scripts de nettoyage](https://github.com/emilwallner/useful-scripts).

### Version complète

Notre version finale du réseau de neurones de colorisation comporte quatre composants. Nous divisons le réseau que nous avions auparavant en un encodeur et un décodeur. Entre eux, nous utiliserons une couche de fusion. Si vous êtes nouveau dans les réseaux de classification, je vous recommande de jeter un coup d'œil à [ce tutoriel](http://cs231n.github.io/classification/).

En parallèle à l'encodeur, les images d'entrée passent également par l'un des classificateurs les plus puissants d'aujourd'hui — le [Inception ResNet v2](https://research.googleblog.com/2016/08/improving-inception-and-image.html). Il s'agit d'un réseau de neurones entraîné sur 1,2 million d'images. Nous extrayons la couche de classification et la fusionnons avec la sortie de l'encodeur.

![Image](https://cdn-media-1.freecodecamp.org/images/qovQFs9u4JKRuqYEgN7kE2iWMZhX6I3WJPln)

Voici une [visualisation plus détaillée](https://github.com/baldassarreFe/deep-koalarization) de l'article original.

En transférant l'apprentissage du classificateur au réseau de colorisation, le réseau peut avoir une idée de ce qu'il y a dans l'image. Ainsi, permettant au réseau de faire correspondre une représentation d'objet avec un schéma de colorisation.

Voici quelques-unes des images de validation, en utilisant seulement 20 images pour entraîner le réseau.

![Image](https://cdn-media-1.freecodecamp.org/images/K3OU3lMzzks0UI-MGAap-fmYCuVhpjHKvTzQ)

La plupart des images se sont révélées médiocres. Mais j'ai pu en trouver quelques-unes décents grâce à un grand ensemble de validation (2 500 images). L'entraîner sur plus d'images a donné un résultat plus cohérent, mais la plupart d'entre elles sont devenues brunâtres. Voici une liste complète des [expériences que j'ai menées](https://www.floydhub.com/emilwallner/projects/color) incluant les images de validation.

Voici les architectures les plus courantes des recherches précédentes, avec des liens :

* Ajouter manuellement de petits points de couleur dans une image pour guider le réseau de neurones ([lien](http://www.cs.huji.ac.il/~yweiss/Colorization/))
* Trouver une image correspondante et transférer la colorisation (en savoir plus [ici](https://dl.acm.org/citation.cfm?id=2393402) et [ici](https://arxiv.org/abs/1505.05192))
* Encodeur résiduel et fusion des couches de classification ([lien](http://tinyclouds.org/colorize/))
* Fusion des hypercolonnes d'un réseau de classification (plus de détails [ici](https://arxiv.org/pdf/1603.08511.pdf) et [ici](https://arxiv.org/pdf/1603.06668.pdf))
* Fusion de la classification finale entre l'encodeur et le décodeur (détails [ici](http://hi.cs.waseda.ac.jp/~iizuka/projects/colorization/data/colorization_sig2016.pdf) et [ici](https://arxiv.org/abs/1712.03400))

**Espaces colorimétriques :** Lab, YUV, HSV et LUV (plus de détails [ici](http://cs231n.stanford.edu/reports/2016/pdfs/219_Report.pdf) et [ici](https://arxiv.org/abs/1605.00075))

**Perte :** Erreur quadratique moyenne, classification, classification pondérée ([lien](https://arxiv.org/pdf/1603.06668.pdf))

J'ai choisi l'architecture de la « couche de fusion » (la cinquième de la liste ci-dessus).

Cela parce qu'elle produit certains des meilleurs résultats. Elle est également plus facile à comprendre et à reproduire dans [Keras](https://keras.io/). Bien qu'il ne s'agisse pas de la conception de réseau de colorisation la plus puissante, c'est un bon point de départ. C'est une excellente architecture pour comprendre les dynamiques du problème de colorisation.

J'ai utilisé la conception de réseau de neurones de [cet article](https://arxiv.org/abs/1712.03400) par Federico Baldassarre et ses collaborateurs. J'ai procédé à ma propre interprétation dans Keras.

Note : dans le code ci-dessous, je passe du modèle séquentiel de Keras à leur API fonctionnelle. [[Documentation](https://keras.io/getting-started/functional-api-guide/)]

```
# Get imagesX = []for filename in os.listdir('/data/images/Train/'):    X.append(img_to_array(load_img('/data/images/Train/'+filename)))X = np.array(X, dtype=float)Xtrain = 1.0/255*X
```

```
#Load weightsinception = InceptionResNetV2(weights=None, include_top=True)inception.load_weights('/data/inception_resnet_v2_weights_tf_dim_ordering_tf_kernels.h5')inception.graph = tf.get_default_graph()
```

```
embed_input = Input(shape=(1000,))
```

```
#Encoderencoder_input = Input(shape=(256, 256, 1,))encoder_output = Conv2D(64, (3,3), activation='relu', padding='same', strides=2)(encoder_input)encoder_output = Conv2D(128, (3,3), activation='relu', padding='same')(encoder_output)encoder_output = Conv2D(128, (3,3), activation='relu', padding='same', strides=2)(encoder_output)encoder_output = Conv2D(256, (3,3), activation='relu', padding='same')(encoder_output)encoder_output = Conv2D(256, (3,3), activation='relu', padding='same', strides=2)(encoder_output)encoder_output = Conv2D(512, (3,3), activation='relu', padding='same')(encoder_output)encoder_output = Conv2D(512, (3,3), activation='relu', padding='same')(encoder_output)encoder_output = Conv2D(256, (3,3), activation='relu', padding='same')(encoder_output)
```

```
#Fusionfusion_output = RepeatVector(32 * 32)(embed_input) fusion_output = Reshape(([32, 32, 1000]))(fusion_output)fusion_output = concatenate([encoder_output, fusion_output], axis=3) fusion_output = Conv2D(256, (1, 1), activation='relu', padding='same')(fusion_output)
```

```
#Decoderdecoder_output = Conv2D(128, (3,3), activation='relu', padding='same')(fusion_output)decoder_output = UpSampling2D((2, 2))(decoder_output)decoder_output = Conv2D(64, (3,3), activation='relu', padding='same')(decoder_output)decoder_output = UpSampling2D((2, 2))(decoder_output)decoder_output = Conv2D(32, (3,3), activation='relu', padding='same')(decoder_output)decoder_output = Conv2D(16, (3,3), activation='relu', padding='same')(decoder_output)decoder_output = Conv2D(2, (3, 3), activation='tanh', padding='same')(decoder_output)decoder_output = UpSampling2D((2, 2))(decoder_output)
```

```
model = Model(inputs=[encoder_input, embed_input], outputs=decoder_output)
```

```
#Create embeddingdef create_inception_embedding(grayscaled_rgb):    grayscaled_rgb_resized = []    for i in grayscaled_rgb:        i = resize(i, (299, 299, 3), mode='constant')        grayscaled_rgb_resized.append(i)    grayscaled_rgb_resized = np.array(grayscaled_rgb_resized)    grayscaled_rgb_resized = preprocess_input(grayscaled_rgb_resized)    with inception.graph.as_default():        embed = inception.predict(grayscaled_rgb_resized)    return embed
```

```
# Image transformerdatagen = ImageDataGenerator(        shear_range=0.4,        zoom_range=0.4,        rotation_range=40,        horizontal_flip=True)
```

```
#Generate training databatch_size = 20
```

```
def image_a_b_gen(batch_size):    for batch in datagen.flow(Xtrain, batch_size=batch_size):        grayscaled_rgb = gray2rgb(rgb2gray(batch))        embed = create_inception_embedding(grayscaled_rgb)        lab_batch = rgb2lab(batch)        X_batch = lab_batch[:,:,:,0]        X_batch = X_batch.reshape(X_batch.shape+(1,))        Y_batch = lab_batch[:,:,:,1:] / 128        yield ([X_batch, create_inception_embedding(grayscaled_rgb)], Y_batch)
```

```
#Train model      tensorboard = TensorBoard(log_dir="/output")model.compile(optimizer='adam', loss='mse')model.fit_generator(image_a_b_gen(batch_size), callbacks=[tensorboard], epochs=1000, steps_per_epoch=20)
```

```
#Make a prediction on the unseen imagescolor_me = []for filename in os.listdir('../Test/'):    color_me.append(img_to_array(load_img('../Test/'+filename)))color_me = np.array(color_me, dtype=float)color_me = 1.0/255*color_mecolor_me = gray2rgb(rgb2gray(color_me))color_me_embed = create_inception_embedding(color_me)color_me = rgb2lab(color_me)[:,:,:,0]color_me = color_me.reshape(color_me.shape+(1,))
```

```
# Test modeloutput = model.predict([color_me, color_me_embed])output = output * 128
```

```
# Output colorizationsfor i in range(len(output)):    cur = np.zeros((256, 256, 3))    cur[:,:,0] = color_me[i][:,:,0]    cur[:,:,1:] = output[i]    imsave("result/img_"+str(i)+".png", lab2rgb(cur))
```

Voici la commande FloydHub pour exécuter le réseau de neurones complet :

```
floyd run --data emilwallner/datasets/colornet/2:data --mode jupyter --tensorboard
```

#### Explication technique

[L'API fonctionnelle de Keras](https://keras.io/getting-started/functional-api-guide/) est idéale lorsque nous concaténons ou fusionnons plusieurs modèles.

![Image](https://cdn-media-1.freecodecamp.org/images/kMNLgj1gQ71kdm5VbyRs33eOwkAYPn4zNLD7)

Tout d'abord, nous téléchargeons le réseau de neurones [Inception ResNet v2](https://research.googleblog.com/2016/08/improving-inception-and-image.html) et chargeons les poids. Puisque nous utiliserons deux modèles en parallèle, nous devons spécifier quel modèle nous utilisons. Cela est fait dans [Tensorflow](https://www.tensorflow.org/), le backend pour Keras.

```
inception = InceptionResNetV2(weights=None, include_top=True)inception.load_weights('/data/inception_resnet_v2_weights_tf_dim_ordering_tf_kernels.h5')inception.graph = tf.get_default_graph()
```

Pour créer notre lot, nous utilisons les images modifiées. Nous les convertissons en noir et blanc et les faisons passer à travers le modèle Inception ResNet.

```
grayscaled_rgb = gray2rgb(rgb2gray(batch))embed = create_inception_embedding(grayscaled_rgb)
```

Tout d'abord, nous devons redimensionner l'image pour qu'elle s'adapte au modèle Inception. Ensuite, nous utilisons le préprocesseur pour formater les valeurs de pixel et de couleur selon le modèle. Dans l'étape finale, nous la faisons passer à travers le réseau Inception et extrayons la couche finale du modèle.

```
def create_inception_embedding(grayscaled_rgb):    grayscaled_rgb_resized = []    for i in grayscaled_rgb:        i = resize(i, (299, 299, 3), mode='constant')        grayscaled_rgb_resized.append(i)    grayscaled_rgb_resized = np.array(grayscaled_rgb_resized)    grayscaled_rgb_resized = preprocess_input(grayscaled_rgb_resized)    with inception.graph.as_default():        embed = inception.predict(grayscaled_rgb_resized)    return embed
```

Revenons au générateur. Pour chaque lot, nous générons 20 images dans le format ci-dessous. Cela prend environ une heure sur un GPU Tesla K80. Il peut traiter jusqu'à 50 images à la fois avec ce modèle sans avoir de problèmes de mémoire.

```
yield ([X_batch, create_inception_embedding(grayscaled_rgb)], Y_batch)
```

Cela correspond à notre format de modèle colornet.

```
model = Model(inputs=[encoder_input, embed_input], outputs=decoder_output)
```

`encoder_input` est alimenté dans notre modèle Encodeur, la sortie du modèle Encodeur est ensuite fusionnée avec `embed_input` dans la couche de fusion ; la sortie de la fusion est ensuite utilisée comme entrée dans notre modèle Décodeur, qui retourne ensuite la sortie finale, `decoder_output`.

```
fusion_output = RepeatVector(32 * 32)(embed_input) fusion_output = Reshape(([32, 32, 1000]))(fusion_output)fusion_output = concatenate([fusion_output, encoder_output], axis=3) fusion_output = Conv2D(256, (1, 1), activation='relu')(fusion_output)
```

Dans la couche de fusion, nous multiplions d'abord la couche de catégorie 1000 par 1024 (32 * 32). De cette façon, nous obtenons 1024 lignes avec la couche finale du modèle Inception.

Cela est ensuite remodelé de 2D à 3D, une grille 32 x 32 avec les 1000 piliers de catégorie. Ceux-ci sont ensuite liés ensemble avec la sortie du modèle encodeur. Nous appliquons un réseau convolutionnel filtré 254 avec un noyau 1X1, la sortie finale de la couche de fusion.

#### Points clés

* **La terminologie de la recherche était décourageante.** J'ai passé trois jours à chercher sur Google des moyens d'implémenter le « modèle de fusion » dans Keras. Parce que cela semblait complexe, je ne voulais pas affronter le problème. Au lieu de cela, je me suis trompé en cherchant des raccourcis.
* **J'ai posé des questions en ligne.** Je n'avais pas un seul commentaire dans le canal Slack de Keras et Stack Overflow a supprimé mes questions. Mais, en décomposant publiquement le problème pour le rendre simple à répondre, cela m'a forcé à isoler l'erreur, me rapprochant d'une solution.
* **Envoyez des emails aux gens.** Bien que les forums puissent être froids, les gens se soucient si vous les contactez directement. Discuter des espaces colorimétriques sur Skype avec un chercheur est inspirant !
* **Après avoir retardé le problème de fusion, j'ai décidé de construire tous les composants avant de les assembler.** Voici [quelques expériences](https://www.floydhub.com/emilwallner/projects/color/24/code/Experiments/transfer-learning-examples) que j'ai utilisées pour décomposer la couche de fusion.
* **Une fois que j'ai eu quelque chose que je pensais fonctionner, j'étais hésitant à l'exécuter.** Bien que je savais que la logique principale était correcte, je ne croyais pas que cela fonctionnerait. Après une tasse de thé au citron et une longue promenade — je l'ai exécuté. Cela a produit une erreur après la première ligne de mon modèle. Mais après quatre jours, plusieurs centaines de bugs et plusieurs milliers de recherches Google, « Epoch 1/22 » est apparu sous mon modèle.

### Prochaines étapes

Coloriser des images est un problème profondément fascinant. C'est autant un problème scientifique qu'artistique. J'ai écrit cet article pour que vous puissiez vous mettre à niveau en colorisation et continuer là où je me suis arrêté. Voici quelques suggestions pour commencer :

* Implémentez-le avec un autre modèle pré-entraîné
* Essayez un autre jeu de données
* Augmentez la précision du réseau en utilisant plus d'images
* Construisez un amplificateur dans l'espace colorimétrique RGB. Créez un modèle similaire au réseau de colorisation, qui prend une image colorée saturée comme entrée et l'image colorée correcte comme sortie.
* Implémentez une classification pondérée
* Appliquez-le à la vidéo. Ne vous inquiétez pas trop de la colorisation, mais rendez le passage entre les images cohérent. Vous pourriez également faire quelque chose de similaire pour des images plus grandes, en les pavant avec des images plus petites.

**Vous pouvez également coloriser facilement vos propres images en noir et blanc avec mes trois versions du réseau de neurones de colorisation en utilisant FloydHub.**

* Pour la version alpha, remplacez simplement le fichier `woman.jpg` par votre fichier avec le même nom (taille d'image 400x400 pixels).
* Pour les versions bêta et complète, ajoutez vos images au dossier `Test` avant d'exécuter la commande FloydHub. Vous pouvez également les télécharger directement dans le Notebook vers le dossier Test pendant que le notebook est en cours d'exécution. Notez que ces images doivent être exactement de 256x256 pixels. De plus, vous pouvez télécharger toutes les images de test en couleur car elles seront automatiquement converties en N&B.

Si vous construisez quelque chose ou si vous êtes bloqué, envoyez-moi un message sur Twitter : [emilwallner](https://twitter.com/EmilWallner). J'adorerais voir ce que vous construisez.

**Un énorme merci à** Federico Baldassarre, pour avoir répondu à mes questions et pour leur travail précédent sur la colorisation. Merci également à Muthu Chidambaram, qui a influencé l'implémentation principale dans Keras, et à la communauté Unsplash pour avoir fourni les images. Merci également à Marine Haziza, Valdemaras Repsys, Qingping Hou, Charlie Harrington, Sai Soundararaj, Jannes Klaas, Claudio Cabral, Alain Demenet et Ignacio Tonoli pour avoir lu les brouillons de cet article.

#### À propos d'Emil Wallner

Ceci est la troisième partie d'une série de blogs en plusieurs parties d'Emil alors qu'il apprend le deep learning. Emil a passé une décennie à explorer l'apprentissage humain. Il a travaillé pour l'école de commerce d'Oxford, investi dans des startups éducatives et construit une entreprise de technologie éducative. L'année dernière, il s'est inscrit à [Ecole 42](https://twitter.com/paulg/status/847844863727087616) pour appliquer ses connaissances de l'apprentissage humain à l'apprentissage machine.

Vous pouvez suivre Emil sur [Twitter](https://twitter.com/EmilWallner) et [Medium](https://medium.com/@emilwallner).

Ceci a été publié pour la première fois en tant qu'article communautaire sur le [blog de Floydhub](https://blog.floydhub.com/colorizing-b&w-photos-with-neural-networks/).