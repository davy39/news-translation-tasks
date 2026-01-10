---
title: Comment entraîner une IA pour convertir vos maquettes de design en HTML et
  CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-05T10:10:24.000Z'
originalURL: https://freecodecamp.org/news/how-you-can-train-an-ai-to-convert-your-design-mockups-into-html-and-css-cc7afd82fed4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*f85n6Sy78fw0GVN8kF1mLQ.jpeg
tags:
- name: Data Science
  slug: data-science
- name: Deep Learning
  slug: deep-learning
- name: Design
  slug: design
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
seo_title: Comment entraîner une IA pour convertir vos maquettes de design en HTML
  et CSS
seo_desc: 'By Emil Wallner

  Within three years, deep learning will change front-end development. It will increase
  prototyping speed and lower the barrier for building software.

  The field took off last year when Tony Beltramelli introduced the pix2code paper
  and ...'
---

Par Emil Wallner

Dans trois ans, le deep learning va changer le développement front-end. Il va augmenter la vitesse de prototypage et abaisser la barrière pour la construction de logiciels.

Le domaine a décollé l'année dernière lorsque Tony Beltramelli a introduit le [pix2code paper](https://arxiv.org/abs/1705.07962) et qu'Airbnb a lancé [sketch2code](https://airbnb.design/sketching-interfaces/).

![Image](https://cdn-media-1.freecodecamp.org/images/CworWMP3u1ZVSYrQrsMAIgwLhFT8WZy5mNRW)
_Photo par [Unsplash](https://unsplash.com/photos/y0_vFxOHayg?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Wesson Wang</a> sur <a href="https://unsplash.com/search/photos/tech-maker?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Actuellement, la plus grande barrière à l'automatisation du développement front-end est la puissance de calcul. Cependant, nous pouvons utiliser les algorithmes actuels de deep learning, ainsi que des données de formation synthétisées, pour commencer à explorer l'automatisation artificielle du front-end dès maintenant.

Dans cet article, nous allons enseigner à un réseau de neurones comment coder un site web HTML et CSS de base basé sur une image d'une maquette de design. Voici un aperçu rapide du processus :

#### 1) Donner une image de design au réseau de neurones entraîné

![Image](https://cdn-media-1.freecodecamp.org/images/Q5az2EKipOfUFI6KzFvHHQuSxWsXHTAEKM5-)

#### 2) Le réseau de neurones convertit l'image en balises HTML

![Image](https://cdn-media-1.freecodecamp.org/images/N1MawQALMnXsjFs6UCtHqo8Wfm30ieTNRBAT)

#### 3) Sortie rendue

![Image](https://cdn-media-1.freecodecamp.org/images/sDrXUHIRX5fI-kkUUsWX2FszawABaw81AOha)

Nous allons construire le réseau de neurones en trois itérations.

Tout d'abord, nous allons faire une version minimale pour comprendre les parties mobiles. La deuxième version, HTML, se concentrera sur l'automatisation de toutes les étapes et l'explication des couches du réseau de neurones. Dans la version finale, Bootstrap, nous allons créer un modèle qui peut généraliser et explorer la couche LSTM.

Tout le code est préparé sur [GitHub](https://github.com/emilwallner/Screenshot-to-code-in-Keras/blob/master/README.md) et [FloydHub](https://www.floydhub.com/emilwallner/projects/picturetocode) dans des notebooks Jupyter. Tous les notebooks FloydHub sont dans le répertoire `floydhub` et les équivalents locaux sont sous `local`.

Les modèles sont basés sur le [pix2code paper](https://arxiv.org/abs/1705.07962) de Beltramelli et les [tutoriels de légende d'image](https://machinelearningmastery.com/blog/page/2/) de Jason Brownlee. Le code est écrit en Python et Keras, un framework sur TensorFlow.

Si vous êtes nouveau dans le deep learning, je vous recommande de vous familiariser avec Python, la rétropropagation et les réseaux de neurones convolutionnels. Mes trois articles précédents sur le blog de FloydHub vous aideront à commencer :

* [Mon Premier Week-end de Deep Learning](https://blog.floydhub.com/my-first-weekend-of-deep-learning/)
* [Coder l'Histoire du Deep Learning](https://blog.floydhub.com/coding-the-history-of-deep-learning/)
* [Coloriser des Photos N&B avec des Réseaux de Neurones](https://blog.floydhub.com/colorizing-b&w-photos-with-neural-networks/)

### Logique Principale

Récapitulons notre objectif. Nous voulons construire un réseau de neurones qui générera des balises HTML/CSS correspondant à une capture d'écran.

Lorsque vous entraînez le réseau de neurones, vous lui donnez plusieurs captures d'écran avec le HTML correspondant.

Il apprend en prédisant toutes les balises HTML correspondantes une par une. Lorsqu'il prédit la prochaine balise, il reçoit la capture d'écran ainsi que toutes les balises correctes jusqu'à ce point.

Voici un simple [exemple de données d'entraînement](https://docs.google.com/spreadsheets/d/1xXwarcQZAHluorveZsACtXRdmNFbwGtN3WMNhcTdEyQ/edit?usp=sharing) dans une feuille Google.

Créer un modèle qui prédit mot par mot est l'approche la plus courante aujourd'hui. Il existe [d'autres approches](https://machinelearningmastery.com/deep-learning-caption-generation-models/), mais c'est la méthode que nous utiliserons tout au long de ce tutoriel.

Remarquez que pour chaque prédiction, il reçoit la même capture d'écran. Donc, s'il doit prédire 20 mots, il recevra la même maquette de design vingt fois. Pour l'instant, ne vous inquiétez pas de savoir comment fonctionne le réseau de neurones. Concentrez-vous sur la compréhension de l'entrée et de la sortie du réseau de neurones.

![Image](https://cdn-media-1.freecodecamp.org/images/p0VkqC9fWS8VKFVYfpr94IURWkmCq733gvNS)

Concentrons-nous sur le balisage précédent. Supposons que nous entraînons le réseau à prédire la phrase « Je peux coder. » Lorsqu'il reçoit « Je », il prédit alors « peux ». La fois suivante, il recevra « Je peux » et prédira « coder ». Il reçoit tous les mots précédents et n'a qu'à prédire le mot suivant.

![Image](https://cdn-media-1.freecodecamp.org/images/2ANgmLR9K-1DaPQ1jpEj5QLAroTlkQP08gvF)

Le réseau de neurones crée des caractéristiques à partir des données. Le réseau construit des caractéristiques pour lier les données d'entrée avec les données de sortie. Il doit créer des représentations pour comprendre ce qu'il y a dans chaque capture d'écran, la syntaxe HTML, qu'il a prédite. Cela construit la connaissance pour prédire la prochaine balise.

Lorsque vous voulez utiliser le modèle entraîné pour une utilisation réelle, c'est similaire à lorsque vous entraînez le modèle. Le texte est généré un par un avec la même capture d'écran à chaque fois. Au lieu de le nourrir avec les bonnes balises HTML, il reçoit le balisage qu'il a généré jusqu'à présent. Ensuite, il prédit la prochaine balise. La prédiction est initiée avec une « balise de début » et s'arrête lorsqu'elle prédit une « balise de fin » ou atteint une limite maximale. Voici un autre exemple dans [une feuille Google](https://docs.google.com/spreadsheets/d/1yneocsAb_w3-ZUdhwJ1odfsxR2kr-4e_c5FabQbNJrs/edit?usp=sharing).

![Image](https://cdn-media-1.freecodecamp.org/images/eR88p99eJAqppbGJfKyg4iNPRCo5r2O-zFSn)

### Version « Hello World »

Construisons une version « hello world ». Nous allons nourrir un réseau de neurones avec une capture d'écran d'un site web affichant « Hello World! » et lui apprendre à générer le balisage.

![Image](https://cdn-media-1.freecodecamp.org/images/unY3kzxqX0K9nbVw4iWXmvbrfzwYg-dGaMyA)

Tout d'abord, le réseau de neurones mappe la maquette de design en une liste de valeurs de pixels. De 0 à 255 dans trois canaux — rouge, bleu et vert.

![Image](https://cdn-media-1.freecodecamp.org/images/FDBfN7arjMPeyrH168pkEW8Bpk45aOhbJ5Ao)

Pour représenter le balisage de manière à ce que le réseau de neurones comprenne, j'utilise [one hot encoding](https://machinelearningmastery.com/how-to-one-hot-encode-sequence-data-in-python/). Ainsi, la phrase « Je peux coder » pourrait être mappée comme ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/XOtOmSIdPl1VMQ9h50lAMwoSa0L0X-V-VObK)

Dans le graphique ci-dessus, nous incluons la balise de début et de fin. Ces balises sont des indices pour savoir quand le réseau commence ses prédictions et quand s'arrêter.

Pour les données d'entrée, nous utiliserons des phrases, en commençant par le premier mot puis en ajoutant chaque mot un par un. Les données de sortie sont toujours un mot.

Les phrases suivent la même logique que les mots. Elles ont également besoin de la même longueur d'entrée. Au lieu d'être limitées par le vocabulaire, elles sont limitées par la longueur maximale de la phrase. Si elle est plus courte que la longueur maximale, vous la remplissez avec des mots vides, un mot avec juste des zéros.

![Image](https://cdn-media-1.freecodecamp.org/images/3sbJ3uuMOnze4PXEvEJZz7QA5M5vQQuOtk-l)

Comme vous le voyez, les mots sont imprimés de droite à gauche. Cela force chaque mot à changer de position pour chaque tour d'entraînement. Cela permet au modèle d'apprendre la séquence au lieu de mémoriser la position de chaque mot.

Dans le graphique ci-dessous, il y a quatre prédictions. Chaque ligne est une prédiction. À gauche se trouvent les images représentées dans leurs trois canaux de couleur : rouge, vert et bleu et les mots précédents. En dehors des crochets se trouvent les prédictions une par une, se terminant par un carré rouge pour marquer la fin.

![Image](https://cdn-media-1.freecodecamp.org/images/xVU1Xra7JH39nM-geNF0EPLbTZH5ZDspFZtZ)
_blocs verts = jetons de début | bloc rouge = jeton de fin_

```
#Longueur de la phrase la plus longue
max_caption_len = 3
#Taille du vocabulaire
vocab_size = 3
```

```
# Charger une capture d'écran pour chaque mot et les transformer en chiffres
images = []
for i in range(2):
    images.append(img_to_array(load_img('screenshot.jpg', target_size=(224, 224))))
images = np.array(images, dtype=float)
# Prétraiter l'entrée pour le modèle VGG16
images = preprocess_input(images)
```

```
#Transformer les jetons de début en encodage one-hot
html_input = np.array(
            [[[0., 0., 0.], #début
             [0., 0., 0.],
             [1., 0., 0.]],
             [[0., 0., 0.], #début <HTML>Hello World!</HTML>
             [1., 0., 0.],
             [0., 1., 0.]]])
```

```
#Transformer le mot suivant en encodage one-hot
next_words = np.array(
            [[0., 1., 0.], # <HTML>Hello World!</HTML>
             [0., 0., 1.]]) # fin
```

```
# Charger le modèle VGG16 entraîné sur imagenet et sortir la caractéristique de classification
VGG = VGG16(weights='imagenet', include_top=True)
# Extraire les caractéristiques de l'image
features = VGG.predict(images)
```

```
#Charger la caractéristique dans le réseau, appliquer une couche dense, et répéter le vecteur
vgg_feature = Input(shape=(1000,))
vgg_feature_dense = Dense(5)(vgg_feature)
vgg_feature_repeat = RepeatVector(max_caption_len)(vgg_feature_dense)
# Extraire les informations de la séquence d'entrée
language_input = Input(shape=(vocab_size, vocab_size))
language_model = LSTM(5, return_sequences=True)(language_input)
```

```
# Concaténer les informations de l'image et de l'entrée
decoder = concatenate([vgg_feature_repeat, language_model])
# Extraire les informations de la sortie concaténée
decoder = LSTM(5, return_sequences=False)(decoder)
# Prédire quel mot vient ensuite
decoder_output = Dense(vocab_size, activation='softmax')(decoder)
# Compiler et exécuter le réseau de neurones
model = Model(inputs=[vgg_feature, language_input], outputs=decoder_output)
model.compile(loss='categorical_crossentropy', optimizer='rmsprop')
```

```
# Entraîner le réseau de neurones
model.fit([features, html_input], next_words, batch_size=2, shuffle=False, epochs=1000)
```

Dans la version hello world, nous utilisons trois jetons : `start`, `<HTML><center><H1>Hello World!</H1></center></HTML>` et `end`. Un jeton peut être n'importe quoi. Il peut être un caractère, un mot ou une phrase. Les versions de caractères nécessitent un vocabulaire plus petit mais contraignent le réseau de neurones. Les jetons de niveau mot tendent à mieux performer.

Voici comment nous faisons la prédiction :

```
# Créer une phrase vide et insérer les jetons de début
sentence = np.zeros((1, 3, 3)) # [[0,0,0], [0,0,0], [0,0,0]]
start_token = [1., 0., 0.] # start
sentence[0][2] = start_token # placer start dans la phrase vide
    # Faire la première prédiction avec le jeton de début
second_word = model.predict([np.array([features[1]]), sentence])
    # Mettre le deuxième mot dans la phrase et faire les prédictions finales
sentence[0][1] = start_token
sentence[0][2] = np.round(second_word)
third_word = model.predict([np.array([features[1]]), sentence])
    # Placer le jeton de début et nos deux prédictions dans la phrase
sentence[0][0] = start_token
sentence[0][1] = np.round(second_word)
sentence[0][2] = np.round(third_word)
    # Transformer nos prédictions one-hot en jetons finaux
vocabulary = ["start", "<HTML><center><H1>Hello World!</H1></center></HTML>", "end"]
for i in sentence[0]:
print(vocabulary[np.argmax(i)], end=' ')
```

### Sortie

* **10 époques :** `start start start`
* **100 époques :** `start <HTML><center><H1>Hello World!</H1></center></HTML> <HTML><center><H1>Hello World!</H1></center></HTML>`
* **300 époques :** `start <HTML><center><H1>Hello World!</H1></center></HTML> end`

### Erreurs que j'ai faites :

* **Construire la première version fonctionnelle avant de rassembler les données.** Au début de ce projet, j'ai réussi à obtenir une copie d'un ancien archive du site d'hébergement Geocities. Il contenait 38 millions de sites web. Aveuglé par le potentiel, j'ai ignoré la charge de travail énorme qui serait nécessaire pour réduire le vocabulaire de 100K.
* **Traiter un téraoctet de données nécessite un bon matériel ou beaucoup de patience.** Après avoir rencontré plusieurs problèmes avec mon mac, j'ai fini par utiliser un serveur distant puissant. Prévoyez de louer une machine avec 8 cœurs CPU modernes et une connexion internet de 1GPS pour avoir un flux de travail décent.
* **Rien n'avait de sens jusqu'à ce que je comprenne les données d'entrée et de sortie.** L'entrée, X, est une capture d'écran et les balises de balisage précédentes. La sortie, Y, est la balise de balisage suivante. Lorsque j'ai compris cela, il est devenu plus facile de tout comprendre entre les deux. Il est également devenu plus facile d'expérimenter avec différentes architectures.
* **Soyez conscient des terriers de lapin.** Parce que ce projet intersecte avec de nombreux domaines du deep learning, je me suis retrouvé coincé dans de nombreux terriers de lapin en cours de route. J'ai passé une semaine à programmer des RNNs à partir de zéro, j'ai été trop fasciné par les espaces vectoriels d'embedding, et j'ai été séduit par des implémentations exotiques.
* **Les réseaux picture-to-code sont des modèles de légende d'image déguisés.** Même lorsque j'ai appris cela, j'ai encore ignoré de nombreux articles sur les légendes d'image, simplement parce qu'ils étaient moins cool. Une fois que j'ai eu une certaine perspective, j'ai accéléré mon apprentissage de l'espace problème.

### Exécuter le code sur FloydHub

FloydHub est une plateforme d'entraînement pour le deep learning. Je les ai découverts lorsque j'ai commencé à apprendre le deep learning et je les utilise depuis pour entraîner et gérer mes expériences de deep learning. Vous pouvez exécuter votre premier modèle en 30 secondes en cliquant sur ce bouton :

![Image](https://cdn-media-1.freecodecamp.org/images/acWQUgUHMXD92BCuTwLP1x7EU6MDXLC83hJf)

Cela ouvre un [Workspace](https://blog.floydhub.com/workspaces/) sur [FloydHub](https://www.floydhub.com/?utm_medium=readme&utm_source=pix2code&utm_campaign=aug_2018) où vous trouverez le même environnement et ensemble de données utilisés pour la version _Bootstrap_. Vous pouvez également trouver les modèles entraînés pour les tests.

Ou vous pouvez faire une installation manuelle en suivant ces étapes : [2-min installation](https://www.floydhub.com/) ou [mon tutoriel de 5 minutes.](https://www.youtube.com/watch?v=byLQ9kgjTdQ&t=21s)

#### **Cloner le dépôt**

```
git clone https://github.com/emilwallner/Screenshot-to-code-in-Keras.git
```

#### **Se connecter et initialiser l'outil de ligne de commande FloydHub**

```
cd Screenshot-to-code-in-Keras
floyd login
floyd init s2c
```

#### **Exécuter un notebook Jupyter sur une machine GPU cloud FloydHub :**

```
floyd run --gpu --env tensorflow-1.4 --data emilwallner/datasets/imagetocode/2:data --mode jupyter
```

Tous les notebooks sont préparés dans le répertoire FloydHub. Les équivalents locaux sont sous local. Une fois qu'il est en cours d'exécution, vous pouvez trouver le premier notebook ici : floydhub/Hello_world/hello_world.ipynb .

Si vous voulez des instructions plus détaillées et une explication des flags, consultez [mon article précédent](https://blog.floydhub.com/colorizing-b&w-photos-with-neural-networks/).

### Version HTML

Dans cette version, nous allons automatiser de nombreuses étapes du modèle Hello World. Cette section se concentrera sur la création d'une implémentation scalable et les pièces mobiles du réseau de neurones.

Cette version ne pourra pas prédire le HTML de sites web aléatoires, mais c'est toujours une excellente configuration pour explorer les dynamiques du problème.

![Image](https://cdn-media-1.freecodecamp.org/images/0tgXF4h7doWnPoBEW4HkAbsScrpgklsFHpRh)

### Aperçu

Si nous développons les composants du graphique précédent, cela ressemble à ceci.

![Image](https://cdn-media-1.freecodecamp.org/images/NobfYNSRI3IdmxiMkmuI76rdnOPGvTlqPn1z)

Il y a deux sections principales. Tout d'abord, l'encodeur. C'est ici que nous créons des caractéristiques d'image et des caractéristiques de balisage précédent. Les caractéristiques sont les blocs de construction que le réseau crée pour connecter les maquettes de design avec le balisage. À la fin de l'encodeur, nous collons les caractéristiques de l'image à chaque mot dans le balisage précédent.

Le décodeur prend ensuite la caractéristique de design et de balisage combinée et crée une caractéristique de balise suivante. Cette caractéristique est exécutée à travers un réseau de neurones entièrement connecté pour prédire la balise suivante.

#### **Caractéristiques de la maquette de design**

Puisque nous devons insérer une capture d'écran pour chaque mot, cela devient un goulot d'étranglement lors de l'entraînement du réseau ([exemple](https://docs.google.com/spreadsheets/d/1xXwarcQZAHluorveZsACtXRdmNFbwGtN3WMNhcTdEyQ/edit#gid=0)). Au lieu d'utiliser les images, nous extrayons les informations dont nous avons besoin pour générer le balisage.

Les informations sont encodées en caractéristiques d'image. Cela est fait en utilisant un réseau de neurones convolutionnel (CNN) déjà pré-entraîné. Le modèle est pré-entraîné sur Imagenet.

Nous extrayons les caractéristiques de la couche avant la classification finale.

![Image](https://cdn-media-1.freecodecamp.org/images/BoMXdL-Cc-ERswtJhUTRqrPMKFIDwLJlg-sq)

Nous obtenons 1536 images de huit par huit pixels connues sous le nom de caractéristiques. Bien qu'elles soient difficiles à comprendre pour nous, un réseau de neurones peut extraire les objets et la position des éléments à partir de ces caractéristiques.

#### **Caractéristiques de balisage**

Dans la version hello world, nous avons utilisé un encodage one-hot pour représenter le balisage. Dans cette version, nous utiliserons un embedding de mots pour l'entrée et garderons l'encodage one-hot pour la sortie.

La façon dont nous structurons chaque phrase reste la même, mais la façon dont nous mappons chaque jeton est changée. L'encodage one-hot traite chaque mot comme une unité isolée. Au lieu de cela, nous convertissons chaque mot dans les données d'entrée en listes de chiffres. Ceux-ci représentent la relation entre les balises de balisage.

![Image](https://cdn-media-1.freecodecamp.org/images/aO1Bx26av7tl9D3ar0j60GyzOiWZ1cj3ghdm)

La dimension de cet embedding de mots est de huit mais varie souvent entre 50 et 500 selon la taille du vocabulaire.

Les huit chiffres pour chaque mot sont des poids similaires à un réseau de neurones vanilla. Ils sont ajustés pour mapper comment les mots se rapportent les uns aux autres ([Mikolov et al., 2013](https://arxiv.org/abs/1301.3781)).

C'est ainsi que nous commençons à développer des caractéristiques de balisage. Les caractéristiques sont ce que le réseau de neurones développe pour lier les données d'entrée avec les données de sortie. Pour l'instant, ne vous inquiétez pas de ce qu'elles sont, nous approfondirons cela dans la section suivante.

### L'Encodeur

Nous allons prendre les embeddings de mots et les faire passer à travers un LSTM et retourner une séquence de caractéristiques de balisage. Celles-ci sont exécutées à travers une couche dense distribuée dans le temps — pensez-y comme une couche dense avec plusieurs entrées et sorties.

![Image](https://cdn-media-1.freecodecamp.org/images/dUMfmiIfBrJ7aEf2JdgGnIexunGvDf-DhSE2)

En parallèle, les caractéristiques de l'image sont d'abord aplaties. Peu importe comment les chiffres étaient structurés, ils sont transformés en une grande liste de nombres. Ensuite, nous appliquons une couche dense sur cette couche pour former une caractéristique de haut niveau. Ces caractéristiques d'image sont ensuite concaténées aux caractéristiques de balisage.

Cela peut être difficile à comprendre — alors décomposons-le.

#### **Caractéristiques de balisage**

Ici, nous faisons passer les embeddings de mots à travers la couche LSTM. Dans ce graphique, toutes les phrases sont rembourrées pour atteindre la taille maximale de trois jetons.

![Image](https://cdn-media-1.freecodecamp.org/images/mHJqcFAE2jMnZxx3e9zY20EoMxHZxLrLcHSR)

Pour mélanger les signaux et trouver des motifs de plus haut niveau, nous appliquons une couche dense TimeDistributed aux caractéristiques de balisage. TimeDistributed dense est la même chose qu'une couche dense, mais avec plusieurs entrées et sorties.

#### **Caractéristiques de l'image**

En parallèle, nous préparons les images. Nous prenons toutes les mini-caractéristiques d'image et les transformons en une longue liste. L'information n'est pas changée, juste réorganisée.

![Image](https://cdn-media-1.freecodecamp.org/images/w8JRSSONEjHw9s6QEBECFQ3Rcz0Gvho-2u5T)

Encore une fois, pour mélanger les signaux et extraire des notions de plus haut niveau, nous appliquons une couche dense. Puisque nous ne traitons qu'avec une seule valeur d'entrée, nous pouvons utiliser une couche dense normale. Pour connecter les caractéristiques de l'image aux caractéristiques de balisage, nous copions les caractéristiques de l'image.

Dans ce cas, nous avons trois caractéristiques de balisage. Ainsi, nous obtenons une quantité égale de caractéristiques d'image et de caractéristiques de balisage.

#### **Concaténation des caractéristiques de l'image et du balisage**

Toutes les phrases sont rembourrées pour créer trois caractéristiques de balisage. Puisque nous avons préparé les caractéristiques de l'image, nous pouvons maintenant ajouter une caractéristique d'image pour chaque caractéristique de balisage.

![Image](https://cdn-media-1.freecodecamp.org/images/NPWrspSfewc4DusETBcZpfDr1pbRBbl1rhbQ)

Après avoir collé une caractéristique d'image à chaque caractéristique de balisage, nous obtenons trois caractéristiques image-balisage. C'est l'entrée que nous alimentons dans le décodeur.

#### **Le Décodeur**

Ici, nous utilisons les caractéristiques image-balisage combinées pour prédire la balise suivante.

![Image](https://cdn-media-1.freecodecamp.org/images/csy-Et69VcXoEzTujHmWPOzm33TkCWQKyNdP)

Dans l'exemple ci-dessous, nous utilisons trois paires de caractéristiques image-balisage et produisons une caractéristique de balise suivante.

Notez que la couche LSTM a la séquence définie sur false. Au lieu de retourner la longueur de la séquence d'entrée, elle ne prédit qu'une seule caractéristique. Dans notre cas, il s'agit d'une caractéristique pour la balise suivante. Elle contient les informations pour la prédiction finale.

![Image](https://cdn-media-1.freecodecamp.org/images/gdiGgVgR2uwJ4mYzhaY0cT7DNjbbxzXAjZLi)

#### **La prédiction finale**

La couche dense fonctionne comme un réseau de neurones feedforward traditionnel. Elle connecte les 512 chiffres dans la caractéristique de la balise suivante avec les 4 prédictions finales. Supposons que nous avons 4 mots dans notre vocabulaire : start, hello, world, et end.

La prédiction de vocabulaire pourrait être [0.1, 0.1, 0.1, 0.7]. L'activation softmax dans la couche dense distribue une probabilité de 0 à 1, avec la somme de toutes les prédictions égale à 1. Dans ce cas, elle prédit que le 4ème mot est la balise suivante. Ensuite, vous traduisez l'encodage one-hot [0, 0, 0, 1] en la valeur mappée, disons « end ».

```
# Charger les images et les prétraiter pour inception-resnet
images = []
all_filenames = listdir('images/')
all_filenames.sort()
for filename in all_filenames:
    images.append(img_to_array(load_img('images/'+filename, target_size=(299, 299))))
images = np.array(images, dtype=float)
images = preprocess_input(images)
```

```
# Exécuter les images à travers inception-resnet et extraire les caractéristiques sans la couche de classification
IR2 = InceptionResNetV2(weights='imagenet', include_top=False)
features = IR2.predict(images)
```

```
# Nous allons limiter chaque séquence d'entrée à 100 jetons
max_caption_len = 100
# Initialiser la fonction qui créera notre vocabulaire
tokenizer = Tokenizer(filters='', split=" ", lower=False)
```

```
# Lire un document et retourner une chaîne
def load_doc(filename):
    file = open(filename, 'r')
    text = file.read()
    file.close()
    return text
```

```
# Charger tous les fichiers HTML
X = []
all_filenames = listdir('html/')
all_filenames.sort()
for filename in all_filenames:
    X.append(load_doc('html/'+filename))
```

```
# Créer le vocabulaire à partir des fichiers html
tokenizer.fit_on_texts(X)
```

```
# Ajouter +1 pour laisser de la place pour les mots vides
vocab_size = len(tokenizer.word_index) + 1
# Traduire chaque mot dans le fichier texte en index de vocabulaire correspondant
sequences = tokenizer.texts_to_sequences(X)
# Le fichier HTML le plus long
max_length = max(len(s) for s in sequences)
```

```
# Initialiser notre entrée finale au modèle
X, y, image_data = list(), list(), list()
for img_no, seq in enumerate(sequences):
    for i in range(1, len(seq)):
        # Ajouter toute la séquence à l'entrée et ne garder que le mot suivant pour la sortie
        in_seq, out_seq = seq[:i], seq[i]
        # Si la phrase est plus courte que max_length, remplissez-la avec des mots vides
        in_seq = pad_sequences([in_seq], maxlen=max_length)[0]
        # Mapper la sortie en encodage one-hot
        out_seq = to_categorical([out_seq], num_classes=vocab_size)[0]
        # Ajouter une image correspondant au fichier HTML
        image_data.append(features[img_no])
        # Couper la phrase d'entrée à 100 jetons, et l'ajouter aux données d'entrée
        X.append(in_seq[-100:])
        y.append(out_seq)
```

```
X, y, image_data = np.array(X), np.array(y), np.array(image_data)
```

```
# Créer l'encodeur
image_features = Input(shape=(8, 8, 1536,))
image_flat = Flatten()(image_features)
image_flat = Dense(128, activation='relu')(image_flat)
ir2_out = RepeatVector(max_caption_len)(image_flat)
```

```
language_input = Input(shape=(max_caption_len,))
language_model = Embedding(vocab_size, 200, input_length=max_caption_len)(language_input)
language_model = LSTM(256, return_sequences=True)(language_model)
language_model = LSTM(256, return_sequences=True)(language_model)
language_model = TimeDistributed(Dense(128, activation='relu'))(language_model)
```

```
# Créer le décodeur
decoder = concatenate([ir2_out, language_model])
decoder = LSTM(512, return_sequences=False)(decoder)
decoder_output = Dense(vocab_size, activation='softmax')(decoder)
```

```
# Compiler le modèle
model = Model(inputs=[image_features, language_input], outputs=decoder_output)
model.compile(loss='categorical_crossentropy', optimizer='rmsprop')
```

```
# Entraîner le réseau de neurones
model.fit([image_data, X], y, batch_size=64, shuffle=False, epochs=2)
```

```
# mapper un entier à un mot
def word_for_id(integer, tokenizer):
    for word, index in tokenizer.word_index.items():
        if index == integer:
            return word
    return None
```

```
# générer une description pour une image
def generate_desc(model, tokenizer, photo, max_length):
    # initialiser le processus de génération
    in_text = 'START'
    # itérer sur toute la longueur de la séquence
    for i in range(900):
        # encoder la séquence d'entrée en entier
        sequence = tokenizer.texts_to_sequences([in_text])[0][-100:]
        # remplir l'entrée
        sequence = pad_sequences([sequence], maxlen=max_length)
        # prédire le mot suivant
        yhat = model.predict([photo,sequence], verbose=0)
        # convertir la probabilité en entier
        yhat = np.argmax(yhat)
        # mapper l'entier à un mot
        word = word_for_id(yhat, tokenizer)
        # arrêter si nous ne pouvons pas mapper le mot
        if word is None:
            break
        # ajouter comme entrée pour générer le mot suivant
        in_text += ' ' + word
        # Imprimer la prédiction
        print(' ' + word, end='')
        # arrêter si nous prédisons la fin de la séquence
        if word == 'END':
            break
    return
```

```
# Charger et une image, la prétraiter pour IR2, extraire les caractéristiques et générer le HTML
test_image = img_to_array(load_img('images/87.jpg', target_size=(299, 299)))
test_image = np.array(test_image, dtype=float)
test_image = preprocess_input(test_image)
test_features = IR2.predict(np.array([test_image]))
generate_desc(model, tokenizer, np.array(test_features), 100)
```

### Sortie

![Image](https://cdn-media-1.freecodecamp.org/images/rT5TzIOaSW9L50-QfQOXzv42XzAlJuvxcm0M)

#### Liens vers les sites web générés

* [250 époques](https://emilwallner.github.io/html/250_epochs/)
* [350 époques](https://emilwallner.github.io/html/350_epochs/)
* [450 époques](https://emilwallner.github.io/html/450_epochs/)
* [550 époques](https://emilwallner.github.io/html/550_epochs/)

Si vous ne voyez rien lorsque vous cliquez sur ces liens, vous pouvez faire un clic droit et cliquer sur « Afficher la source de la page ». Voici le [site web original](https://emilwallner.github.io/html/Original/) pour référence.

### Erreurs que j'ai faites :

* **Les LSTMs sont beaucoup plus lourds pour ma cognition par rapport aux CNNs**. Lorsque j'ai déroulé tous les LSTMs, ils sont devenus plus faciles à comprendre. La [vidéo de Fast.ai sur les RNNs](http://course.fast.ai/lessons/lesson6.html) a été super utile. Concentrez-vous également sur les caractéristiques d'entrée et de sortie avant d'essayer de comprendre comment ils fonctionnent.
* **Construire un vocabulaire à partir de zéro est beaucoup plus facile que de réduire un énorme vocabulaire**. Cela inclut tout, des polices, tailles de div, et couleurs hexadécimales aux noms de variables et mots normaux.
* **La plupart des bibliothèques sont créées pour analyser des documents texte et non du code**. Dans les documents, tout est séparé par un espace, mais dans le code, vous avez besoin d'une analyse personnalisée.
* **Vous pouvez extraire des caractéristiques avec un modèle qui est entraîné sur Imagenet**. Cela peut sembler contre-intuitif puisque Imagenet a peu d'images web. Cependant, la perte est 30% plus élevée par rapport à un modèle pix2code, qui est entraîné à partir de zéro. Il serait intéressant d'utiliser un modèle de type inception-resnet pré-entraîné basé sur des captures d'écran web.

### Version Bootstrap

Dans notre version finale, nous allons utiliser un ensemble de données de sites web bootstrap générés à partir de l'article [pix2code](https://arxiv.org/abs/1705.07962). En utilisant le [bootstrap](https://getbootstrap.com/) de Twitter, nous pouvons combiner HTML et CSS et réduire la taille du vocabulaire.

Nous allons lui permettre de générer le balisage pour une capture d'écran qu'il n'a jamais vue auparavant. Nous allons également approfondir comment il construit des connaissances sur la capture d'écran et le balisage.

Au lieu de l'entraîner sur le balisage bootstrap, nous allons utiliser 17 jetons simplifiés que nous traduisons ensuite en HTML et CSS. [L'ensemble de données](https://github.com/tonybeltramelli/pix2code/tree/master/datasets) comprend 1500 captures d'écran de test et 250 images de validation. Pour chaque capture d'écran, il y a en moyenne 65 jetons, ce qui donne 96925 exemples d'entraînement.

En ajustant le modèle dans l'article pix2code, le modèle peut prédire les composants web avec une précision de 97% (BLEU 4-ngram greedy search, plus sur cela plus tard).

![Image](https://cdn-media-1.freecodecamp.org/images/22jp7W-84XQTYMnD8n13fD3OOEDsNmdLM6RY)

#### Une approche de bout en bout

Extraire des caractéristiques de modèles pré-entraînés fonctionne bien dans les modèles de légende d'image. Mais après quelques expériences, j'ai réalisé que l'approche de bout en bout de pix2code fonctionne mieux pour ce problème. Les modèles pré-entraînés n'ont pas été entraînés sur des données web et sont personnalisés pour la classification.

Dans ce modèle, nous remplaçons les caractéristiques d'image pré-entraînées par un réseau de neurones convolutionnel léger. Au lieu d'utiliser le max-pooling pour augmenter la densité d'information, nous augmentons les strides. Cela maintient la position et la couleur des éléments front-end.

![Image](https://cdn-media-1.freecodecamp.org/images/RIgV3yDJTktUueaKR7KS7pL1PeSzpgbMVO3e)

Il y a deux modèles principaux qui permettent cela : les réseaux de neurones convolutionnels (CNN) et les réseaux de neurones récurrents (RNN). Le réseau de neurones récurrent le plus courant est la mémoire à long et court terme (LSTM), donc c'est ce à quoi je vais me référer.

Il existe de nombreux tutoriels sur les CNN, et je les ai couverts dans [mon article précédent](https://blog.floydhub.com/colorizing-b&w-photos-with-neural-networks/). Ici, je vais me concentrer sur les LSTMs.

#### Comprendre les timesteps dans les LSTMs

L'une des choses les plus difficiles à comprendre sur les LSTMs est les timesteps. Un réseau de neurones vanilla peut être considéré comme deux timesteps. Si vous lui donnez « Hello », il prédit « World ». Mais il aurait du mal à prédire plus de timesteps. Dans l'exemple ci-dessous, l'entrée a quatre timesteps, un pour chaque mot.

Les LSTMs sont faits pour les entrées avec des timesteps. C'est un réseau de neurones personnalisé pour les informations dans l'ordre. Si vous déroulez notre modèle, il ressemble à ceci. Pour chaque étape descendante, vous gardez les mêmes poids. Vous appliquez un ensemble de poids à la sortie précédente et un autre ensemble à la nouvelle entrée.

![Image](https://cdn-media-1.freecodecamp.org/images/k6bsFnCGDThM1uQ0xfk1acrQDJIXJw17rBwx)

L'entrée et la sortie pondérées sont concaténées et additionnées avec une activation. C'est la sortie pour ce timestep. Puisque nous réutilisons les poids, ils tirent des informations de plusieurs entrées et construisent des connaissances de la séquence.

Voici une version simplifiée du processus pour chaque timestep dans un LSTM.

![Image](https://cdn-media-1.freecodecamp.org/images/wCuaxvU4R4X8i50WO9U7vfTPE1hh1XGyXwRO)

Pour vous familiariser avec cette logique, je vous recommande de construire un RNN à partir de zéro avec le [tutoriel brillant](https://iamtrask.github.io/2015/11/15/anyone-can-code-lstm/) d'Andrew Trask.

#### Comprendre les unités dans les couches LSTM

Le nombre d'unités dans chaque couche LSTM détermine sa capacité à mémoriser. Cela correspond également à la taille de chaque caractéristique de sortie. Encore une fois, une caractéristique est une longue liste de nombres utilisée pour transférer des informations entre les couches.

Chaque unité dans la couche LSTM apprend à suivre différents aspects de la syntaxe. Ci-dessous se trouve une visualisation d'une unité qui suit les informations dans la div de ligne. C'est le balisage simplifié que nous utilisons pour entraîner le modèle bootstrap.

![Image](https://cdn-media-1.freecodecamp.org/images/Hfrjx6Pg3h7tXIvtzs8ce5Vbz8qgW9o4EnZa)

Chaque unité LSTM maintient un état de cellule. Pensez à l'état de cellule comme à la mémoire. Les poids et les activations sont utilisés pour modifier l'état de différentes manières. Cela permet aux couches LSTM d'ajuster finement les informations à conserver et à rejeter pour chaque entrée.

En plus de faire passer une caractéristique de sortie pour chaque entrée, elle transmet également les états de cellule, une valeur pour chaque unité dans le LSTM. Pour vous familiariser avec la manière dont les composants au sein du LSTM interagissent, je recommande le [tutoriel de Colah](https://colah.github.io/posts/2015-08-Understanding-LSTMs/), l'[implémentation Numpy](http://blog.varunajayasiri.com/numpy_lstm.html) de Jayasiri, et la [conférence](https://www.youtube.com/watch?v=yCC09vCHzF8) et le [compte-rendu](https://karpathy.github.io/2015/05/21/rnn-effectiveness/) de Karphay.

```
dir_name = 'resources/eval_light/'
```

```
# Lire un fichier et retourner une chaîne
def load_doc(filename):
    file = open(filename, 'r')
    text = file.read()
    file.close()
    return text
```

```
def load_data(data_dir):
    text = []
    images = []
    # Charger tous les fichiers et les ordonner
    all_filenames = listdir(data_dir)
    all_filenames.sort()
    for filename in (all_filenames):
        if filename[-3:] == "npz":
            # Charger les images déjà préparées dans des tableaux
            image = np.load(data_dir+filename)
            images.append(image['features'])
        else:
            # Charger les jetons bootstrap et les envelopper dans une balise de début et de fin
            syntax = '<START> ' + load_doc(data_dir+filename) + ' <END>'
            # Séparer tous les mots avec un seul espace
            syntax = ' '.join(syntax.split())
            # Ajouter un espace après chaque virgule
            syntax = syntax.replace(',', ' ,')
            text.append(syntax)
    images = np.array(images, dtype=float)
    return images, text
```

```
train_features, texts = load_data(dir_name)
```

```
# Initialiser la fonction pour créer le vocabulaire
tokenizer = Tokenizer(filters='', split=" ", lower=False)
# Créer le vocabulaire
tokenizer.fit_on_texts([load_doc('bootstrap.vocab')])
```

```
# Ajouter une place pour le mot vide dans le vocabulaire
vocab_size = len(tokenizer.word_index) + 1
# Mapper les phrases d'entrée dans l'index du vocabulaire
train_sequences = tokenizer.texts_to_sequences(texts)
# Le plus long ensemble de jetons bootstrap
max_sequence = max(len(s) for s in train_sequences)
# Spécifier combien de jetons avoir dans chaque phrase d'entrée
max_length = 48
```

```
def preprocess_data(sequences, features):
    X, y, image_data = list(), list(), list()
    for img_no, seq in enumerate(sequences):
        for i in range(1, len(seq)):
            # Ajouter la phrase jusqu'au compte actuel (i) et ajouter le compte actuel à la sortie
            in_seq, out_seq = seq[:i], seq[i]
            # Remplir toutes les phrases de jetons d'entrée à max_sequence
            in_seq = pad_sequences([in_seq], maxlen=max_sequence)[0]
            # Transformer la sortie en encodage one-hot
            out_seq = to_categorical([out_seq], num_classes=vocab_size)[0]
            # Ajouter l'image correspondante au fichier de jetons bootstrap
            image_data.append(features[img_no])
            # Limiter la phrase d'entrée à 48 jetons et l'ajouter
            X.append(in_seq[-48:])
            y.append(out_seq)
    return np.array(X), np.array(y), np.array(image_data)
```

```
X, y, image_data = preprocess_data(train_sequences, train_features)
```

```
#Créer l'encodeur
image_model = Sequential()
image_model.add(Conv2D(16, (3, 3), padding='valid', activation='relu', input_shape=(256, 256, 3,)))
image_model.add(Conv2D(16, (3,3), activation='relu', padding='same', strides=2))
image_model.add(Conv2D(32, (3,3), activation='relu', padding='same'))
image_model.add(Conv2D(32, (3,3), activation='relu', padding='same', strides=2))
image_model.add(Conv2D(64, (3,3), activation='relu', padding='same'))
image_model.add(Conv2D(64, (3,3), activation='relu', padding='same', strides=2))
image_model.add(Conv2D(128, (3,3), activation='relu', padding='same'))
```

```
image_model.add(Flatten())
image_model.add(Dense(1024, activation='relu'))
image_model.add(Dropout(0.3))
image_model.add(Dense(1024, activation='relu'))
image_model.add(Dropout(0.3))
```

```
image_model.add(RepeatVector(max_length))
```

```
visual_input = Input(shape=(256, 256, 3,))
encoded_image = image_model(visual_input)
```

```
language_input = Input(shape=(max_length,))
language_model = Embedding(vocab_size, 50, input_length=max_length, mask_zero=True)(language_input)
language_model = LSTM(128, return_sequences=True)(language_model)
language_model = LSTM(128, return_sequences=True)(language_model)
```

```
#Créer le décodeur
decoder = concatenate([encoded_image, language_model])
decoder = LSTM(512, return_sequences=True)(decoder)
decoder = LSTM(512, return_sequences=False)(decoder)
decoder = Dense(vocab_size, activation='softmax')(decoder)
```

```
# Compiler le modèle
model = Model(inputs=[visual_input, language_input], outputs=decoder)
optimizer = RMSprop(lr=0.0001, clipvalue=1.0)
model.compile(loss='categorical_crossentropy', optimizer=optimizer)
```

```
#Sauvegarder le modèle pour chaque 2ème époque
filepath="org-weights-epoch-{epoch:04d}--val_loss-{val_loss:.4f}--loss-{loss:.4f}.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='val_loss', verbose=1, save_weights_only=True, period=2)
callbacks_list = [checkpoint]
```

```
# Entraîner le modèle
model.fit([image_data, X], y, batch_size=64, shuffle=False, validation_split=0.1, callbacks=callbacks_list, verbose=1, epochs=50)
```

### Précision des tests

Il est difficile de trouver une méthode équitable pour mesurer la précision. Supposons que vous compariez mot à mot. Si votre prédiction est décalée d'un mot, vous pourriez avoir 0% de précision. Si vous supprimez un mot qui synchronise la prédiction, vous pourriez obtenir 99/100.

J'ai utilisé le score BLEU, la meilleure pratique en traduction automatique et en modèles de légende d'image. Il divise la phrase en quatre n-grammes, de séquences de 1 à 4 mots. Dans la prédiction ci-dessous, « cat » devrait être « code ».

![Image](https://cdn-media-1.freecodecamp.org/images/4ldQsCGrBwQ3Y4k6E32iMM6OW2jdXLwvqG4t)

Pour obtenir le score final, vous multipliez chaque score par 25%, (4/5) * 0.25 + (2/4) * 0.25 + (1/3) * 0.25 + (0/2) * 0.25 = 0.2 + 0.125 + 0.083 + 0 = 0.408. La somme est ensuite multipliée par une pénalité de longueur de phrase. Puisque la longueur est correcte dans notre exemple, cela devient notre score final.

Vous pourriez augmenter le nombre de n-grammes pour le rendre plus difficile. Un modèle à quatre n-grammes est celui qui correspond le mieux aux traductions humaines. Je recommande d'exécuter quelques exemples avec le code ci-dessous et de lire la [page wiki](https://en.wikipedia.org/wiki/BLEU).

```
#Créer une fonction pour lire un fichier et retourner son contenu
def load_doc(filename):
    file = open(filename, 'r')
    text = file.read()
    file.close()
    return text
```

```
def load_data(data_dir):
    text = []
    images = []
    files_in_folder = os.listdir(data_dir)
    files_in_folder.sort()
    for filename in tqdm(files_in_folder):
        #Ajouter une image
        if filename[-3:] == "npz":
            image = np.load(data_dir+filename)
            images.append(image['features'])
        else:
        # Ajouter du texte et l'envelopper dans une balise de début et de fin
            syntax = '<START> ' + load_doc(data_dir+filename) + ' <END>'
            #Séparer chaque mot avec un espace
            syntax = ' '.join(syntax.split())
            #Ajouter un espace entre chaque virgule
            syntax = syntax.replace(',', ' ,')
            text.append(syntax)
    images = np.array(images, dtype=float)
    return images, text
```

```
#Initialiser la fonction pour créer le vocabulaire
tokenizer = Tokenizer(filters='', split=" ", lower=False)
#Créer le vocabulaire dans un ordre spécifique
tokenizer.fit_on_texts([load_doc('bootstrap.vocab')])
```

```
dir_name = '../../../../eval/'
train_features, texts = load_data(dir_name)
```

```
#charger le modèle et les poids
json_file = open('../../../../model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# charger les poids dans le nouveau modèle
loaded_model.load_weights("../../../../weights.hdf5")
print("Modèle chargé depuis le disque")
```

```
# mapper un entier à un mot
def word_for_id(integer, tokenizer):
    for word, index in tokenizer.word_index.items():
        if index == integer:
            return word
    return None
print(word_for_id(17, tokenizer))
```

```
# générer une description pour une image
def generate_desc(model, tokenizer, photo, max_length):
    photo = np.array([photo])
    # initialiser le processus de génération
    in_text = '<START> '
    # itérer sur toute la longueur de la séquence
    print('\nPrediction---->\n\n<START> ', end='')
    for i in range(150):
        # encoder la séquence d'entrée en entier
        sequence = tokenizer.texts_to_sequences([in_text])[0]
        # remplir l'entrée
        sequence = pad_sequences([sequence], maxlen=max_length)
        # prédire le mot suivant
        yhat = loaded_model.predict([photo, sequence], verbose=0)
        # convertir la probabilité en entier
        yhat = argmax(yhat)
        # mapper l'entier à un mot
        word = word_for_id(yhat, tokenizer)
        # arrêter si nous ne pouvons pas mapper le mot
        if word is None:
            break
        # ajouter comme entrée pour générer le mot suivant
        in_text += word + ' '
        # arrêter si nous prédisons la fin de la séquence
        print(word + ' ', end='')
        if word == '<END>':
            break
    return in_text
```

```
max_length = 48
```

```
# évaluer la compétence du modèle
def evaluate_model(model, descriptions, photos, tokenizer, max_length):
    actual, predicted = list(), list()
    # passer sur l'ensemble complet
    for i in range(len(texts)):
        yhat = generate_desc(model, tokenizer, photos[i], max_length)
        # stocker l'actual et le prédit
        print('\n\nReal---->\n\n' + texts[i])
        actual.append([texts[i].split()])
        predicted.append(yhat.split())
    # calculer le score BLEU
    bleu = corpus_bleu(actual, predicted)
    return bleu, actual, predicted
```

```
bleu, actual, predicted = evaluate_model(loaded_model, texts, train_features, tokenizer, max_length)
```

```
#Compiler les jetons en HTML et css
dsl_path = "compiler/assets/web-dsl-mapping.json"
compiler = Compiler(dsl_path)
compiled_website = compiler.compile(predicted[0], 'index.html')
```

```
print(compiled_website )
print(bleu)
```

### Sortie

![Image](https://cdn-media-1.freecodecamp.org/images/r7mUhHa-CvziLYb8mdu43CFxgwvKkBgjZIh-)

Liens vers des exemples de sortie

* [Site web généré 1](https://emilwallner.github.io/bootstrap/pred_1/) — [Original 1](https://emilwallner.github.io/bootstrap/real_1/)
* [Site web généré 2](https://emilwallner.github.io/bootstrap/pred_2/) — [Original 2](https://emilwallner.github.io/bootstrap/real_2/)
* [Site web généré 3](https://emilwallner.github.io/bootstrap/pred_3/) — [Original 3](https://emilwallner.github.io/bootstrap/real_3/)
* [Site web généré 4](https://emilwallner.github.io/bootstrap/pred_4/) — [Original 4](https://emilwallner.github.io/bootstrap/real_4/)
* [Site web généré 5](https://emilwallner.github.io/bootstrap/pred_5/) — [Original 5](https://emilwallner.github.io/bootstrap/real_5/)

### Erreurs que j'ai faites :

* **Comprendre les faiblesses des modèles au lieu de tester des modèles aléatoires.** Tout d'abord, j'ai appliqué des choses aléatoires telles que la normalisation par lots et des réseaux bidirectionnels et j'ai essayé d'implémenter l'attention. Après avoir examiné les données de test et vu qu'il ne pouvait pas prédire la couleur et la position avec une grande précision, j'ai réalisé qu'il y avait une faiblesse dans le CNN. Cela m'a conduit à remplacer le maxpooling par des strides augmentés. La perte de validation est passée de 0,12 à 0,02 et a augmenté le score BLEU de 85% à 97%.
* **N'utiliser des modèles pré-entraînés que s'ils sont pertinents.** Étant donné le petit ensemble de données, je pensais qu'un modèle d'image pré-entraîné améliorerait les performances. D'après mes expériences, un modèle de bout en bout est plus lent à entraîner et nécessite plus de mémoire, mais il est 30% plus précis.
* **Prévoir une légère variance lorsque vous exécutez votre modèle sur un serveur distant.** Sur mon mac, il lit les fichiers dans l'ordre alphabétique. Cependant, sur le serveur, ils étaient situés de manière aléatoire. Cela a créé un décalage entre les captures d'écran et le code. Il a toujours convergé, mais les données de validation étaient 50% moins bonnes que lorsque je l'ai corrigé.
* **Assurez-vous de comprendre les fonctions de la bibliothèque.** Incluez de l'espace pour le jeton vide dans votre vocabulaire. Lorsque je ne l'ai pas ajouté, il n'incluait pas l'un des jetons. Je ne l'ai remarqué qu'après avoir regardé la sortie finale plusieurs fois et remarqué qu'il ne prédisait jamais un jeton « single ». Après une vérification rapide, j'ai réalisé qu'il n'était même pas dans le vocabulaire. De plus, utilisez le même ordre dans le vocabulaire pour l'entraînement et les tests.
* **Utilisez des modèles plus légers lors de l'expérimentation.** L'utilisation de GRUs au lieu de LSTMs a réduit chaque cycle d'époque de 30%, et n'a pas eu un grand effet sur les performances.

### Prochaines étapes

Le développement front-end est un espace idéal pour appliquer le deep learning. Il est facile de générer des données, et les algorithmes actuels de deep learning peuvent mapper la plupart de la logique.

L'un des domaines les plus passionnants est [l'application de l'attention aux LSTMs](https://arxiv.org/pdf/1502.03044.pdf). Cela n'améliorera pas seulement la précision, mais nous permettra de visualiser où le CNN met son focus lorsqu'il génère le balisage.

L'attention est également la clé pour communiquer entre le balisage, les feuilles de style, les scripts et éventuellement le backend. Les couches d'attention peuvent suivre les variables, permettant au réseau de communiquer entre les langages de programmation.

Mais dans un avenir proche, le plus grand impact viendra de la construction d'une manière scalable de synthétiser les données. Ensuite, vous pouvez ajouter des polices, des couleurs, des mots et des animations étape par étape.

Jusqu'à présent, la plupart des progrès se font dans la prise de croquis et leur transformation en applications de modèle. En moins de deux ans, nous pourrons dessiner une application sur papier et avoir le front-end correspondant en moins d'une seconde. Il existe déjà deux prototypes fonctionnels construits par [l'équipe de design d'Airbnb](https://airbnb.design/sketching-interfaces/) et [Uizard](https://www.uizard.io/).

Voici quelques expériences pour commencer.

### Expériences

**Pour commencer**

* Exécuter tous les modèles
* Essayer différents hyperparamètres
* Tester une architecture CNN différente
* Ajouter des modèles LSTM bidirectionnels
* Implémenter le modèle avec un [ensemble de données différent](http://lstm.seas.harvard.edu/latex/). (Vous pouvez facilement monter cet ensemble de données dans vos travaux FloydHub avec ce flag `--data emilwallner/datasets/100k-html:data`)

**Expériences supplémentaires**

* Créer un générateur d'applications/web aléatoires solide avec la syntaxe correspondante.
* Données pour un modèle de croquis à application. Auto-convertir les captures d'écran d'applications/web en croquis et utiliser un GAN pour créer de la variété.
* Appliquer une couche d'attention pour visualiser le focus sur l'image pour chaque prédiction, [similaire à ce modèle](https://arxiv.org/abs/1502.03044).
* Créer un framework pour une approche modulaire. Par exemple, avoir des modèles d'encodeur pour les polices, un pour la couleur, un autre pour la mise en page et les combiner avec un décodeur. Un bon point de départ pourrait être des caractéristiques d'image solides.
* Alimenter le réseau avec des composants HTML simples et lui apprendre à générer des animations en utilisant CSS. Il serait fascinant d'avoir une approche d'attention et de visualiser le focus sur les deux sources d'entrée.

**Un grand merci à** Tony Beltramelli et Jon Gold pour leurs recherches et idées, et pour avoir répondu à des questions. Merci à Jason Brownlee pour ses tutoriels Keras stellaires (j'ai inclus quelques extraits de son tutoriel dans l'implémentation principale de Keras), et à Beltramelli pour avoir fourni les données. Merci également à Qingping Hou, Charlie Harrington, Sai Soundararaj, Jannes Klaas, Claudio Cabral, Alain Demenet et Dylan Djian pour avoir lu les brouillons de ceci.

### À propos d'Emil Wallner

Ceci est la quatrième partie d'une série de blogs en plusieurs parties d'Emil alors qu'il apprend le deep learning. Emil a passé une décennie à explorer l'apprentissage humain. Il a travaillé pour l'école de commerce d'Oxford, investi dans des startups éducatives et construit une entreprise de technologie éducative. L'année dernière, il s'est inscrit à [Ecole 42](https://twitter.com/paulg/status/847844863727087616) pour appliquer ses connaissances de l'apprentissage humain à l'apprentissage machine.

Si vous construisez quelque chose ou si vous êtes bloqué, contactez-moi ci-dessous ou sur twitter : [emilwallner](https://twitter.com/EmilWallner). J'adorerais voir ce que vous construisez.

Ceci a été publié pour la première fois comme un article communautaire sur le [blog de Floydhub](https://blog.floydhub.com/turning-design-mockups-into-code-with-deep-learning/).