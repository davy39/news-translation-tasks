---
title: Comment classifier les papillons avec l'apprentissage profond dans Keras
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-08T18:59:32.000Z'
originalURL: https://freecodecamp.org/news/classify-butterfly-images-deep-learning-keras
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/1_K4agkAxY1R6zPzK8s_CqbQ-1.jpeg
tags:
- name: Data Science
  slug: data-science
- name: Deep Learning
  slug: deep-learning
- name: image classification
  slug: image-classification
- name: keras
  slug: keras
- name: Python
  slug: python
seo_title: Comment classifier les papillons avec l'apprentissage profond dans Keras
seo_desc: 'By Bert Carremans

  A while ago I read an interesting blog post on the website of the Dutch organization
  Vlinderstichting. Every year they organize a count of butterflies. Volunteers help
  in determining the different butterfly species in their garden. ...'
---

Par Bert Carremans

Il y a quelque temps, j'ai lu un article intéressant sur le site de l'organisation néerlandaise [Vlinderstichting](https://www.vlinderstichting.nl/actueel/nieuws/nieuwsbericht/?bericht=1492). Chaque année, ils organisent un recensement de papillons. Des bénévoles aident à déterminer les différentes espèces de papillons dans leur jardin. La Vlinderstichting collecte et analyse les résultats.

Comme la détermination des espèces de papillons est faite par les bénévoles, ce processus est inévitablement sujet à des erreurs. Par conséquent, la Vlinderstichting doit vérifier manuellement les soumissions, ce qui est chronophage.

Plus précisément, il y a trois papillons pour lesquels la Vlinderstichting reçoit de nombreuses déterminations erronées. Ce sont

* [Meadow brown](https://en.wikipedia.org/wiki/Meadow_brown) ou Maniola jurtina
* [Gatekeeper](https://en.wikipedia.org/wiki/Gatekeeper_(butterfly)) ou Pyronia tithonus
* [Small heath](https://en.wikipedia.org/wiki/Small_heath_(butterfly)) ou Coenonympha pamphilus

Dans cet article, je vais décrire les étapes pour ajuster un modèle d'apprentissage profond qui aide à faire la distinction entre les deux premiers papillons.

# Téléchargement d'images avec l'API Flickr

Pour entraîner un réseau de neurones convolutif, j'ai besoin de trouver des images de papillons avec l'étiquette correcte. Bien sûr, je pourrais prendre des photos moi-même des papillons que je veux classifier. Ils volent parfois dans mon jardin...

Je plaisante, cela prendrait des siècles. Pour cela, j'ai besoin d'une méthode automatisée pour obtenir les images. Pour ce faire, j'utilise l'API Flickr via Python.

## Configuration de l'API Flickr

Tout d'abord, j'installe le package [flickrapi](https://pypi.python.org/pypi/flickrapi/2.3) avec pip. Ensuite, je crée les clés API nécessaires sur le site Flickr pour me connecter à l'API Flickr.

En plus du package flickrapi, j'importe les packages os et urllib pour télécharger les images et configurer les répertoires.

```python
from flickrapi import FlickrAPI
import urllib
import os
import config
```

Dans le module config, je définis les clés publiques et secrètes pour l'API Flickr. Donc, il s'agit simplement d'un script Python (config.py) avec le code ci-dessous :

```python
API_KEY = 'XXXXXXXXXXXXXXXXX'  // remplacer par votre clé
API_SECRET = 'XXXXXXXXXXXXXXXXX'  // remplacer par votre secret
IMG_FOLDER = 'XXXXXXXXXXXXXXXXX'  // remplacer par votre dossier pour stocker les images
```

Je garde ces clés dans un fichier séparé pour des raisons de sécurité. Ainsi, vous pouvez enregistrer le code dans un dépôt public comme GitHub ou BitBucket et mettre le config.py dans .gitignore. Par conséquent, vous pouvez partager votre code avec d'autres sans avoir à vous soucier de quelqu'un ayant accès à vos identifiants.

Pour extraire des images de différentes espèces de papillons, j'ai écrit une fonction download_flickr_photos. Je vais expliquer cette fonction étape par étape. De plus, j'ai rendu le code complet disponible sur [GitHub](https://github.com/bertcarremans/Vlindervinder/tree/master/flickr).

## Paramètres d'entrée

Tout d'abord, je vérifie si les paramètres d'entrée sont du type ou des valeurs corrects. Si ce n'est pas le cas, je lève une erreur. L'explication des paramètres peut être trouvée dans la docstring de la fonction.

```python
if not (isinstance(keywords, str) or isinstance(keywords, list)):
    raise AttributeError('keywords must be a string or a list of strings')
if not (size in ['thumbnail', 'square', 'medium', 'original']):
    raise AttributeError('size must be "thumbnail", "square", "medium" or "original"')
if not (max_nb_img == -1 or (max_nb_img > 0 and isinstance(max_nb_img, int))):
    raise AttributeError('max_nb_img must be an integer greater than zero or equal to -1')
```

Deuxièmement, je définis certains des paramètres qui seront utilisés dans la méthode walk plus tard. Je crée une liste pour les mots-clés et détermine à partir de quelle URL les images doivent être téléchargées.

```python
if isinstance(keywords, str):
    keywords_list = []
    keywords_list.append(keywords)
else:
    keywords_list = keywords
if size == 'thumbnail':
    size_url = 'url_t'
elif size == 'square':
    size_url = 'url_q'
elif size == 'medium':
    size_url = 'url_c'
elif size == 'original':
    size_url = 'url_o'
```

## Connexion à l'API Flickr

Ensuite, je me connecte à l'API Flickr. Dans l'appel FlickrAPI, j'utilise les clés API définies dans le module config.

```python
flickr = FlickrAPI(config.API_KEY, config.API_SECRET)
```

## Création de sous-dossiers par espèce de papillon

Je sauvegarde les images de chaque espèce de papillon dans un sous-dossier séparé. Le nom de chaque sous-dossier est le nom de l'espèce de papillon, donné par le mot-clé. Si le sous-dossier n'existe pas encore, je le crée.

```python
results_folder = config.IMG_FOLDER + keyword.replace(" ", "_") + "/"
if not os.path.exists(results_folder):
    os.makedirs(results_folder)
```

## Parcourir la bibliothèque Flickr

```python
photos = flickr.walk(
    text=keyword,
    extras='url_m',
    license='1,2,4,5',
    per_page=50)
```

J'utilise la méthode walk de l'API Flickr pour rechercher des images pour le mot-clé spécifié. Cette méthode walk a les mêmes paramètres que la méthode [search](http://www.flickr.com/services/api/flickr.photos.search.html) dans l'API Flickr.

Dans le paramètre text, j'utilise le mot-clé pour rechercher des images liées à ce mot-clé. Deuxièmement, dans le paramètre extras, je spécifie url_m pour une taille petite, moyenne des images. Plus d'explications sur les tailles d'image et leur URL respective sont données dans cette [bibliothèque C Flickcurl](http://librdf.org/flickcurl/api/flickcurl-searching-search-extras.html).

Troisièmement, dans le paramètre license, je sélectionne des images avec une licence non commerciale. Plus d'informations sur les codes de licence et leur signification peuvent être trouvées sur la plateforme [API Flickr](https://www.flickr.com/services/api/flickr.photos.licenses.getInfo.html). Enfin, le paramètre per_page spécifie combien d'images je veux par page.

En conséquence, j'ai un générateur appelé photos pour télécharger les images.

## Téléchargement des images Flickr

Avec le générateur photos, je peux télécharger toutes les images trouvées pour la requête de recherche. D'abord, j'obtiens l'URL spécifique à laquelle je vais télécharger l'image. Ensuite, j'incrémente la variable count et utilise ce compteur pour créer les noms de fichiers des images.

Avec la méthode urlretrieve, je télécharge l'image et la sauvegarde dans le dossier pour l'espèce de papillon. Si une erreur se produit, j'affiche le message d'erreur.

```python
for photo in photos:
    try:
        url=photo.get('url_m')
        print(url)
        count += 1
        urllib.request.urlretrieve(url,  results_folder + str(count) +".jpg")
    except Exception as e:
        print(e, 'Download failure')
```

Pour télécharger plusieurs espèces de papillons, je crée une liste et appelle la fonction download_flickr_photos dans une boucle for. Pour simplifier, je ne télécharge que deux espèces de papillons parmi les trois mentionnées ci-dessus.

```python
butterflies = ['meadow brown butterfly', 'gatekeeper butterfly']
for butterfly in butterflies:
    download_flickr_photos(butterfly)
```

# Augmentation des données d'images

L'entraînement d'un convnet sur un petit nombre d'images entraînera un surapprentissage. Par conséquent, le modèle fera des erreurs dans la classification de nouvelles images, non vues. L'augmentation des données peut aider à éviter cela. Heureusement, Keras dispose de quelques outils pour transformer facilement les images.

J'aimerais le comparer à la façon dont mon fils classe les voitures sur la route. Pour le moment, il n'a que 2 ans et n'a pas vu autant de voitures qu'un adulte. Donc, on pourrait dire que son ensemble d'entraînement d'images est plutôt petit. Par conséquent, il est plus susceptible de mal classer les voitures. Par exemple, il prend parfois une ambulance pour un fourgon de police par erreur.

À mesure qu'il grandira, il verra plus d'ambulances et de fourgons de police, avec l'étiquette correspondante que je lui donnerai. Ainsi, son ensemble d'entraînement deviendra plus grand et il les classera donc plus correctement.

Pour cette raison, nous devons fournir au convnet plus d'images de papillons que nous n'en avons actuellement. Une solution facile pour cela est l'augmentation des données. En bref, cela signifie appliquer un ensemble de transformations aux images Flickr.

Keras fournit une [large gamme de transformations d'images](https://keras.io/preprocessing/image/). Mais d'abord, nous devons convertir les images pour que Keras puisse travailler avec elles.

## Conversion d'une image en nombres

Nous commençons par importer le module Keras. Nous allons démontrer les transformations d'images avec une image exemple. À cette fin, nous utilisons la méthode load_img.

```python
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
i = load_img('data/train/maniola_jurtina/1.jpg' )
x = img_to_array(i)
x = x.reshape((1,) + x.shape)
```

La méthode load_img crée un fichier Python Image Library. Nous devons convertir cela en un tableau Numpy pour l'utiliser dans la méthode ImageDataGenerator plus tard. Cela se fait avec la méthode pratique img_to_array. En conséquence, nous avons un tableau de forme 75x75x3. Ces dimensions reflètent la largeur, la hauteur et les valeurs RVB.

En fait, chaque pixel de l'image a 3 valeurs RVB. Celles-ci varient entre 0 et 255 et représentent l'intensité du Rouge, du Vert et du Bleu. Une valeur plus faible correspond à une intensité plus élevée et une valeur plus élevée à une intensité plus faible. Par exemple, un pixel peut être représenté comme une liste de ces trois valeurs [78, 136, 60]. Le noir serait représenté comme [0, 0, 0].

Enfin, nous devons ajouter une dimension supplémentaire pour éviter une ValueError lors de l'application des transformations. Cela se fait avec la fonction reshape.

D'accord, maintenant nous avons quelque chose avec quoi travailler. Continuons avec les transformations.

## Rotation

En spécifiant une valeur entre 0 et 180, Keras choisira aléatoirement un angle pour faire tourner l'image. Il le fera dans le sens des aiguilles d'une montre ou dans le sens inverse. Dans notre exemple, l'image sera tournée avec un maximum de 90 degrés.

ImageDataGenerator a également un paramètre fill_mode. La valeur par défaut est 'nearest'. En faisant tourner l'image dans la largeur et la hauteur de l'image originale, nous obtenons des pixels "vides". Le fill_mode utilise alors les pixels les plus proches pour remplir cet espace vide.

```python
imgGen = ImageDataGenerator(rotation_range = 90)
i = 1
for batch in imgGen.flow(x, batch_size=1, save_to_dir='example_transformations', save_format='jpeg', save_prefix='trsf'):
    i += 1
    if i > 3:
        break
```

Dans la méthode flow, nous spécifions où sauvegarder les images transformées. Assurez-vous que ce répertoire existe ! Nous préfixons également les nouvelles images créées pour plus de commodité. La méthode flow s'exécuterait indéfiniment, mais pour cet exemple, nous ne générons que trois images. Donc, lorsque notre compteur atteint cette valeur, nous sortons de la boucle for. Vous pouvez voir le résultat ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-102.png)

## Déplacement de la largeur

Dans le paramètre width_shift_range, vous spécifiez le ratio de la largeur originale par lequel l'image peut être déplacée vers la gauche ou la droite. Encore une fois, le fill_mode remplira les nouveaux pixels vides créés. Pour les exemples restants, je ne montrerai que comment instancier l'ImageDataGenerator avec le paramètre respectif. Le code pour générer les images est le même que dans l'exemple de rotation.

```python
imgGen = ImageDataGenerator(width_shift_range = 90)
```

Dans les images transformées, nous voyons que l'image est déplacée vers la droite. Les pixels vides sont remplis, ce qui lui donne un peu un aspect étiré.

La même chose peut être faite pour le déplacement vers le haut ou vers le bas en spécifiant une valeur pour le paramètre height_shift_range.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-103.png)

## Redimensionnement

Le redimensionnement d'une image multipliera les valeurs RVB de chaque pixel par une valeur choisie avant tout autre prétraitement. Dans notre exemple, nous appliquons une mise à l'échelle min-max aux valeurs. En conséquence, ces valeurs seront comprises entre 0 et 1. Cela rend les valeurs plus petites et plus faciles à traiter pour le modèle.

```python
imgGen = ImageDataGenerator(rescale = 1./255)
```

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-104.png)

## Cisaillement

Avec le paramètre shear_range, nous pouvons spécifier comment les transformations de cisaillement doivent être appliquées. Cette transformation peut produire des images plutôt étranges lorsque la valeur est trop élevée. Donc, ne la réglez pas trop haut.

```python
imgGen = ImageDataGenerator(shear_range = 0.2)
```

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-106.png)

## Zoom

Cette transformation zoome à l'intérieur de l'image. Tout comme le paramètre de cisaillement, cette valeur ne doit pas être exagérée pour garder les images réalistes.

```python
imgGen = ImageDataGenerator(zoom_range = 0.2)
```

## Retournement horizontal

Cette transformation retourne une image horizontalement. La vie peut être simple parfois...

```python
imgGen = ImageDataGenerator(horizontal_flip = True)
```

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-107.png)

## Toutes les transformations combinées

Maintenant que nous avons vu l'effet de chaque transformation séparément, nous appliquons toutes les combinaisons ensemble.

```python
imgGen = ImageDataGenerator(
    rotation_range = 40,
    width_shift_range = 0.2,
    height_shift_range = 0.2,
    rescale = 1./255,
    shear_range = 0.2,
    zoom_range = 0.2,
    horizontal_flip = True)
i = 1
for batch in imgGen.flow(x, batch_size=1, save_to_dir='example_transformations', save_format='jpeg', save_prefix='all'):
    i += 1
    if i > 3:
        break
```

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-108.png)

## Configuration de la structure des dossiers

Nous devons stocker ces images dans une structure de dossiers spécifique. Ainsi, nous pouvons utiliser la méthode flow_from_directory pour augmenter les images et créer les étiquettes correspondantes. Cette structure de dossiers doit ressembler à ceci :

* **train**
* maniola_jurtina
* 0.jpg
* 1.jpg
* …
* pyronia_tithonus
* 0.jpg
* 1.jpg
* …
* **validation**
* maniola_jurtina
* 0.jpg
* 1.jpg
* …
* pyronia_tithonus
* 0.jpg
* 1.jpg
* …

Pour créer cette structure de dossiers, j'ai créé un gist [img_train_test_split.py](https://gist.github.com/bertcarremans/679624f369ed9270472e37f8333244f5). N'hésitez pas à l'utiliser dans vos projets.

## Création des générateurs

Tout comme avant, nous spécifions les paramètres de configuration pour le générateur d'entraînement. Les images de validation ne seront pas transformées comme les images d'entraînement. Nous divisons simplement les valeurs RVB pour les rendre plus petites.

La méthode flow_from_directory prend les images du dossier train ou validation et génère des lots de 32 images transformées. En définissant le class_mode sur 'binary', une étiquette unidimensionnelle est créée en fonction du nom du dossier de l'image.

```python
train_datagen = ImageDataGenerator(
    rotation_range = 40,
    width_shift_range = 0.2,
    height_shift_range = 0.2,
    rescale = 1./255,
    shear_range = 0.2,
    zoom_range = 0.2,
    horizontal_flip = True)
validation_datagen = ImageDataGenerator(rescale=1./255)
train_generator = train_datagen.flow_from_directory(
    'data/train',
    batch_size=32,
    class_mode='binary')
validation_generator = validation_datagen.flow_from_directory(
    'data/validation',
    batch_size=32,
    class_mode='binary')
```

## Que faire des différentes tailles d'images ?

L'API Flickr vous permet de télécharger des images de tailles spécifiques. Cependant, dans les applications réelles, les tailles d'images ne sont pas toujours constantes. Si le rapport d'aspect des images est le même, nous pouvons simplement redimensionner les images. Sinon, nous pouvons rogner les images. Malheureusement, il est difficile de rogner l'image tout en gardant l'objet que nous voulons classifier intact.

Keras peut gérer différentes tailles d'images. Lors de la configuration du modèle, vous pouvez spécifier None pour la largeur et la hauteur dans input_shape.

```python
input_shape=(3, None, None)  # Theano
input_shape=(None, None, 3)  # Tensorflow
```

Je voulais montrer qu'il est possible de travailler avec différentes tailles d'images, cependant, cela présente quelques inconvénients.

* toutes les couches (par exemple, Flatten) ne fonctionneront pas avec None comme dimension d'entrée
* cela peut être lourd en calcul

# Construction du modèle d'apprentissage profond

Pour le reste de cet article, je vais discuter de la structure d'un réseau de neurones convolutif, illustré avec quelques exemples pour notre projet de papillons. À la fin de cet article, nous aurons nos premiers résultats de classification.

## De quelles couches un réseau de neurones convolutif est-il composé ?

Bien sûr, vous pouvez choisir combien de couches et leur type à ajouter à votre réseau de neurones convolutif (également appelé CNN ou convnet). Dans ce projet, nous allons commencer avec la structure suivante :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-111.png)

Comprenons ce que fait chaque couche et comment nous les créons avec Keras.

## Couche d'entrée

Ces différentes versions des images ont été modifiées via plusieurs transformations. Ensuite, ces images sont converties en une représentation numérique ou une matrice.

Les dimensions de cette matrice seront largeur x hauteur x nombre de canaux (couleur). Pour les images RVB, le nombre de canaux sera de trois. Pour les images en niveaux de gris, cela est égal à un. Ci-dessous, vous pouvez voir une représentation numérique d'une image RVB de 7x7.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-112.png)

Comme nos images sont de taille 75x75, nous devons spécifier cela dans le paramètre input_shape lors de l'ajout de la première couche convolutive.

```python
cnn = Sequential()
cnn.add(Conv2D(32,(3,3), input_shape = (3 ,75 ,75)))
```

## Couche convolutive

Dans les premières couches, le réseau de neurones convolutif recherchera des caractéristiques de bas niveau, comme des bords horizontaux ou verticaux. Plus nous avançons dans le réseau, plus il recherchera des caractéristiques de haut niveau, comme une aile de papillon, par exemple. Mais comment détecte-t-il des caractéristiques lorsqu'il ne reçoit que des nombres en entrée ? C'est là que les filtres entrent en jeu.

## Filtres (ou noyaux)

Vous pouvez penser à un filtre comme à un projecteur d'une taille spécifique qui scanne l'image. Le filtre exemple ci-dessous a des dimensions de 3x3x3 et contient des poids qui détecteront un bord vertical. Pour une image en niveaux de gris, les dimensions auraient été de 3x3x1. Habituellement, un filtre a des dimensions plus petites que l'image que nous voulons classifier. 3x3, 5x5 ou 7x7 sont typiquement utilisés. La troisième dimension doit toujours être égale au nombre de canaux.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-113.png)

Lors du balayage de l'image, les valeurs RVB sont transformées. Il effectue cette transformation en multipliant les valeurs RVB par les poids du filtre. Enfin, les valeurs multipliées sont ensuite sommées sur tous les canaux. Dans notre exemple d'image 7x7x3 et le filtre 3x3x3, cela donnerait un résultat de 5x5x1.

L'animation ci-dessous illustre cette opération de convolution. Pour simplifier, nous recherchons uniquement un bord vertical dans le canal Rouge. Ainsi, les poids pour les canaux Vert et Bleu sont tous égaux à zéro. Mais vous devez garder à l'esprit que les résultats de multiplication pour ces canaux sont ajoutés au résultat du canal Rouge.

Comme montré ci-dessous, la couche convolutive produira des résultats numériques. Lorsque vous avez des nombres plus élevés, cela signifie que le filtre est tombé sur la caractéristique qu'il recherchait. Dans notre exemple, un bord vertical.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0_ykXVTApvty9Q0lAX-1.gif)

Nous pouvons spécifier que nous voulons plus d'un filtre. Ces filtres pourraient avoir leur propre caractéristique à rechercher dans une image. Supposons que nous utilisions 32 filtres de taille 3x3x3. Le résultat de tous les filtres est empilé et nous obtenons un volume de 5x5x32 dans notre exemple. Dans l'extrait de code ci-dessus, nous avons ajouté 32 filtres de taille 3x3x3.

## Pas (Stride)

Dans l'exemple ci-dessus, nous avons vu que le filtre se déplace d'un pixel à la fois. C'est ce qu'on appelle le pas (stride). Nous pourrions augmenter le nombre de pixels que le filtre se déplace. Augmenter le pas réduira les dimensions de l'image originale beaucoup plus rapidement. Dans l'exemple ci-dessous, vous voyez comment le filtre se déplace avec un pas de 2, ce qui donnerait un résultat de 3x3x1 pour un filtre de 3x3x3 et une image de 7x7x3.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0_Ds4PLixAjvOMPF9j-1.gif)

## Remplissage (Padding)

En appliquant un filtre, les dimensions de l'image originale sont rapidement réduites. En particulier, les pixels sur les bords de l'image ne sont utilisés qu'une seule fois dans l'opération de convolution. Cela entraîne une perte d'informations. Si vous voulez éviter cela, vous pouvez spécifier un remplissage (padding). Le remplissage ajoute des "pixels supplémentaires" autour de l'image.

Supposons que nous ajoutons un remplissage d'un pixel autour de l'image 7x7x3. Cela donne une image de 9x9x3. Si nous appliquons un filtre de 3x3x3 et un pas de 1, nous obtenons un résultat de 7x7x1. Donc, dans ce cas, nous préservons les dimensions de l'image originale et les pixels extérieurs sont utilisés plus d'une fois.

Vous pouvez calculer le résultat de l'opération de convolution avec un remplissage et un pas spécifiques comme suit :

**1 + [(dimension originale + remplissage x 2 — dimension du filtre) / taille du pas]**

Par exemple, supposons que nous avons cette configuration de notre couche conv :

* image 7x7x3
* filtre 3x3x3
* remplissage de 1 pixel
* pas de 2 pixels

Cela donnera 1 + [(7 + 1 x 2—3) / 2] = 4

## Pourquoi avons-nous besoin de couches convolutives ?

Un avantage de l'utilisation des couches conv est que le nombre de paramètres à estimer est beaucoup plus faible. Beaucoup plus faible par rapport à une couche cachée normale. Supposons que nous continuons avec notre exemple d'image de 7x7x3 et un filtre de 3x3x3 sans remplissage et un pas de 1. La couche convolutive aurait 5x5x1 + 1 biais = 26 poids à estimer. Dans un réseau de neurones avec 7x7x3 entrées et 5x5x1 neurones dans la couche cachée, nous devrions estimer 3.675 poids. Imaginez ce que ce nombre est lorsque vous avez des images plus grandes...

## Couche ReLu

Ou unité linéaire rectifiée. Cette couche ajoute de la non-linéarité au réseau. La couche convolutive est une couche linéaire car elle additionne les multiplications des poids du filtre et des valeurs RVB.

Le résultat d'une fonction ReLu est égal à zéro pour toutes les valeurs de x <= 0. Sinon, il est égal à la valeur de x. Le code dans Keras pour ajouter une couche ReLu est :

```python
cnn.add(Activation('relu'))
```

## Pooling

Le pooling agrège le volume d'entrée afin de réduire davantage les dimensions. Cela accélère le temps de calcul car le nombre de paramètres à estimer est réduit. De plus, cela aide à éviter le surapprentissage en rendant le réseau plus robuste. Ci-dessous, nous illustrons le max pooling avec une taille de 2x2 et un pas de 2.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-115.png)

Le code dans Keras pour ajouter le pooling avec une taille de 2x2 est :

```python
cnn.add(MaxPooling2D(pool_size = (2 ,2)))
```

## Couche entièrement connectée

À la fin, le convnet est capable de détecter des caractéristiques de haut niveau dans les images d'entrée. Cela peut alors servir d'entrée pour une couche entièrement connectée. Avant de pouvoir le faire, nous allons aplatir la sortie de la dernière couche ReLu. L'aplatissement signifie que nous la convertissons en un vecteur. Les valeurs du vecteur sont ensuite connectées à tous les neurones de la couche entièrement connectée. Pour ce faire en Python, nous utilisons les fonctions Keras suivantes :

```python
cnn.add(Flatten())        
cnn.add(Dense(64))
```

## Abandon (Dropout)

Tout comme le pooling, l'abandon peut aider à éviter le surapprentissage. Il définit aléatoirement une fraction spécifiée des entrées à zéro, pendant l'entraînement du modèle. Un taux d'abandon entre 20 et 50 % est considéré comme fonctionnant bien.

```python
cnn.add(Dropout(0.2))
```

## Activation Sigmoid

Parce que nous voulons produire une probabilité que l'image soit l'une des deux espèces de papillons (c'est-à-dire une classification binaire), nous pouvons utiliser une couche d'activation sigmoid.

```python
cnn.add(Activation('relu'))
cnn.add(Dense(1))
cnn.add(Activation( 'sigmoid'))
```

## Application du réseau de neurones convolutif sur les images de papillons

Maintenant, nous pouvons définir la structure complète du réseau de neurones convolutif comme affiché au début de cet article. Tout d'abord, nous devons importer les modules Keras nécessaires. Ensuite, nous pouvons commencer à ajouter les couches que nous avons expliquées ci-dessus.

```python
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Flatten, Dense, Dropout
from keras.preprocessing.image import ImageDataGenerator
import time
IMG_SIZE = # Remplacer par la taille de vos images
NB_CHANNELS = # 3 pour les images RVB ou 1 pour les images en niveaux de gris
BATCH_SIZE = # Les valeurs typiques sont 8, 16 ou 32
NB_TRAIN_IMG = # Remplacer par le nombre total d'images d'entraînement
NB_VALID_IMG = # Remplacer par le nombre total d'images de validation
```

J'ai rendu certains paramètres supplémentaires explicites pour les couches conv. Voici une brève explication :

* kernel_size spécifie la taille du filtre. Donc pour la première couche conv, cette taille est de 2x2
* padding = 'same' signifie appliquer un remplissage zéro de telle sorte que la taille de l'image originale soit préservée.
* padding = 'valid' signifie que nous n'appliquons aucun remplissage.
* data_format = 'channels_last' est juste pour spécifier que le nombre de canaux de couleur est spécifié en dernier dans l'argument input_shape.

```python
cnn = Sequential()
cnn.add(Conv2D(filters=32, 
               kernel_size=(2,2), 
               strides=(1,1),
               padding='same',
               input_shape=(IMG_SIZE,IMG_SIZE,NB_CHANNELS),
               data_format='channels_last'))
cnn.add(Activation('relu'))
cnn.add(MaxPooling2D(pool_size=(2,2),
                     strides=2))
cnn.add(Conv2D(filters=64,
               kernel_size=(2,2),
               strides=(1,1),
               padding='valid'))
cnn.add(Activation('relu'))
cnn.add(MaxPooling2D(pool_size=(2,2),
                     strides=2))
cnn.add(Flatten())        
cnn.add(Dense(64))
cnn.add(Activation('relu'))
cnn.add(Dropout(0.25))
cnn.add(Dense(1))
cnn.add(Activation('sigmoid'))
cnn.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
```

Enfin, nous compilons cette structure de réseau et définissons le paramètre de perte sur binary_crossentropy qui est bon pour les cibles binaires et utilisons l'exactitude comme métrique d'évaluation.

Après avoir spécifié la structure du réseau, nous créons les générateurs pour les échantillons d'entraînement et de validation. Sur les échantillons d'entraînement, nous appliquons l'augmentation des données comme expliqué ci-dessus. Sur les échantillons de validation, nous n'appliquons aucune augmentation car ils sont simplement utilisés pour évaluer les performances du modèle.

```python
train_datagen = ImageDataGenerator(
    rotation_range = 40,                  
    width_shift_range = 0.2,                  
    height_shift_range = 0.2,                  
    rescale = 1./255,                  
    shear_range = 0.2,                  
    zoom_range = 0.2,                     
    horizontal_flip = True)
validation_datagen = ImageDataGenerator(rescale = 1./255)
train_generator = train_datagen.flow_from_directory(
    '../flickr/img/train',
    target_size=(IMG_SIZE,IMG_SIZE),
    class_mode='binary',
    batch_size = BATCH_SIZE)
validation_generator = validation_datagen.flow_from_directory(
    '../flickr/img/validation',
    target_size=(IMG_SIZE,IMG_SIZE),
    class_mode='binary',
    batch_size = BATCH_SIZE)
```

Avec la méthode flow_from_directory sur les générateurs, nous pouvons facilement parcourir toutes les images dans les répertoires spécifiés.

Enfin, nous pouvons ajuster le réseau de neurones convolutif sur les données d'entraînement et évaluer avec les données de validation. Les poids résultants du modèle peuvent être sauvegardés et réutilisés plus tard.

```python
start = time.time()
cnn.fit_generator(
    train_generator,
    steps_per_epoch=NB_TRAIN_IMG//BATCH_SIZE,
    epochs=50,
    validation_data=validation_generator,
    validation_steps=NB_VALID_IMG//BATCH_SIZE)
end = time.time()
print('Processing time:',(end - start)/60)
cnn.save_weights('cnn_baseline.h5')
```

Le nombre d'époques est arbitrairement défini à 50. Une époque est le cycle de propagation avant, de vérification de l'erreur et ensuite d'ajustement des poids pendant la rétropropagation.

Le steps_per_epoch est défini comme le nombre d'images d'entraînement divisé par la taille du lot (au fait, le symbole de double division garantira que le résultat est un entier et non un float). Spécifier une taille de lot supérieure à 1 accélérera le processus. Idem pour le paramètre validation_steps.

## Résultats

Après avoir exécuté 50 époques, nous avons une précision d'entraînement de 0,8091 et une précision de validation de 0,7359. Donc, le réseau de neurones convolutif souffre encore d'un surapprentissage assez important. Nous voyons également que la précision de validation varie beaucoup. Cela est dû au fait que nous avons un petit ensemble d'échantillons de validation. Il serait préférable de faire une validation croisée k-fold pour chaque tour d'évaluation. Mais cela prendrait beaucoup de temps.

Pour remédier au surapprentissage, nous pourrions :

* augmenter le taux d'abandon
* appliquer l'abandon à chaque couche
* trouver plus de données d'entraînement

Nous examinerons les deux premières options et surveillerons le résultat. Les résultats de notre premier modèle serviront de référence. Après avoir appliqué une couche d'abandon supplémentaire et augmenté les taux d'abandon, le modèle est un peu moins surapprenti.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-116.png)

J'espère que vous avez tous apprécié la lecture de cet article et appris quelque chose de nouveau. Le code complet est disponible sur [Github](https://github.com/bertcarremans/Vlindervinder). Santé !