---
title: Comment configurer la détection de contenu NSFW avec le Machine Learning
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-20T16:01:08.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-nsfw-content-detection-with-machine-learning-229a9725829c
coverImage: https://cdn-media-1.freecodecamp.org/images/0*auWeZYXZjFkr33e6
tags:
- name: AI
  slug: ai
- name: keras
  slug: keras
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: Comment configurer la détection de contenu NSFW avec le Machine Learning
seo_desc: 'By Gant Laborde

  Teaching a machine to recognize indecent content wasn’t difficult in retrospect,
  but it sure was tough the first time through.

  Here are some lessons learned, and some tips and tricks I uncovered while building
  an NSFW model.

  Though th...'
---

Par Gant Laborde

Enseigner à une machine à reconnaître du contenu indécent n'a pas été difficile en rétrospective, mais cela a été assez difficile la première fois.

Voici quelques leçons apprises, ainsi que quelques astuces et conseils que j'ai découverts en construisant un modèle NSFW.

Bien qu'il existe de nombreuses façons d'implémenter cela, l'objectif de cet article est de fournir un récit accessible afin que d'autres puissent comprendre à quoi ce processus peut ressembler.

Si vous êtes nouveau dans le ML, cela vous inspirera à entraîner un modèle. Si vous êtes familier avec cela, j'aimerais savoir comment vous auriez procédé pour construire ce modèle et vous demander de partager votre code.

### Le Plan :

1. Obtenir beaucoup de données
2. Étiqueter et nettoyer les données
3. Utiliser Keras et le transfert d'apprentissage
4. Affiner votre modèle

### Obtenir beaucoup de données

[Heureusement, un ensemble vraiment cool de scripts de scraping a été publié pour un jeu de données NSFW](https://github.com/alexkimxyz/nsfw_data_scraper). Le code est simple et vient déjà avec des catégories de données étiquetées. Cela signifie qu'en acceptant simplement les paramètres par défaut de ce scraper de données, nous obtenons 5 catégories extraites de centaines de subreddits.

Les instructions sont assez simples, vous pouvez simplement exécuter les 6 scripts conviviaux. Faites attention à eux car vous pourriez décider de changer certaines choses.

Si vous avez plus de subreddits que vous souhaitez ajouter, vous devriez modifier les URLs sources avant d'exécuter l'étape 1.

> Par exemple — Si vous deviez ajouter une nouvelle source d'exemples neutres, vous ajouteriez à la liste des subreddits dans `nsfw_data_scraper/scripts/source_urls/neutral.txt`.

Reddit est une excellente ressource de contenu sur le web, puisque la plupart des subreddits sont légèrement modérés par des humains pour rester ciblés sur ce subreddit.

### Étiqueter et nettoyer les données

Les données que nous avons obtenues du scraper de données NSFW sont déjà étiquetées ! Mais attendez-vous à quelques erreurs. Surtout puisque Reddit n'est pas parfaitement curaté.

La duplication est également assez courante, mais peut être corrigée sans comparaison humaine lente.

La première chose que j'aime exécuter est `duplicate-file-finder` qui est le détecteur et suppresseur de fichiers exacts le plus rapide. Il est alimenté en Python.

[**Qarj/duplicate-file-finder**](https://github.com/Qarj/duplicate-file-finder)
[_Trouver des fichiers en double. Contribuez au développement de Qarj/duplicate-file-finder en créant un compte sur GitHub._github.com](https://github.com/Qarj/duplicate-file-finder)

Je peux généralement éliminer une majorité de doublons avec cette commande.

```
python dff.py --path train/path --delete
```

Maintenant, cela ne détecte pas les images qui sont "essentiellement" les mêmes. Pour cela, je recommande d'utiliser [un outil Macpaw appelé "Gemini 2"](https://macpaw.com/gemini).

![Image](https://cdn-media-1.freecodecamp.org/images/bDP2lY9uBf6Kk2f-EKjXCpabDnTl3uPuVIP)

Bien que cela semble super simple, n'oubliez pas de creuser dans les doublons automatiques, et de sélectionner TOUS les doublons jusqu'à ce que votre écran Gemini déclare "Rien de restant" comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/ips7SCI7zqpXXdmvSTZJCl5eInzHNRbBWcuT)

Il est sûr de dire que cela peut prendre un temps extrême si vous avez un énorme jeu de données. Personnellement, je l'ai exécuté sur chaque classification avant de l'exécuter sur le dossier parent afin de garder des temps d'exécution raisonnables.

### Utiliser Keras et le transfert d'apprentissage

J'ai examiné Tensorflow, Pytorch et Python brut comme moyens de construire un modèle de machine learning à partir de zéro. Mais je ne cherche pas à découvrir quelque chose de nouveau, je veux simplement faire quelque chose de préexistant de manière efficace. Alors j'ai opté pour une approche pragmatique.

J'ai trouvé Keras être l'API la plus pratique pour écrire un modèle simple. Même Tensorflow est d'accord et travaille actuellement à [devenir plus similaire à Keras](https://medium.com/tensorflow/standardizing-on-keras-guidance-on-high-level-apis-in-tensorflow-2-0-bad2b04c819a). De plus, avec seulement une carte graphique, je vais prendre un modèle préexistant populaire + ses poids, et simplement m'entraîner par-dessus avec un peu de transfert d'apprentissage.

Après quelques recherches, j'ai choisi [Inception v3](https://cloud.google.com/tpu/docs/inception-v3-advanced) pondéré avec [imagenet](http://image-net.org/about-overview). Pour moi, c'est comme aller au magasin de ML préexistant et acheter l'Aston Martin. Nous allons simplement enlever la couche supérieure pour pouvoir utiliser ce modèle selon nos besoins.

```py
conv_base = InceptionV3(    
  weights='imagenet',     
  include_top=False,     
  input_shape=(height, width, num_channels)
)
```

![Image](https://cdn-media-1.freecodecamp.org/images/Cf05CV83hyD1eVnXBMTvHpoIumCDdE5hUSeW)

Avec le modèle en place, j'ai ajouté 3 couches supplémentaires. Une couche de 256 neurones cachés, suivie d'une couche de 128 neurones cachés, suivie d'une couche finale de 5 neurones. Cette dernière étant la classification ultime en cinq classes finales modérées par softmax.

```py
# Ajouter 256
x = Dense(256, activation='relu', kernel_initializer=initializers.he_normal(seed=None), kernel_regularizer=regularizers.l2(.0005))(x)
x = Dropout(0.5)(x)
# Ajouter 128
x = Dense(128,activation='relu', kernel_initializer=initializers.he_normal(seed=None))(x)
x = Dropout(0.25)(x)
# Ajouter 5
predictions = Dense(5,  kernel_initializer="glorot_uniform", activation='softmax')(x)
```

Visuellement, ce code se transforme en ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/lc7FWvMTeY6fic-6PoAO9iM2k4ZE7Ljynb6-)

Certaines des choses ci-dessus peuvent sembler étranges. Après tout, ce n'est pas tous les jours que vous dites "glorot_uniform". Mais mis à part les mots étranges, mes nouvelles couches cachées sont régulées pour prévenir le surapprentissage.

J'utilise le dropout, qui supprimera aléatoirement des voies neuronales pour qu'aucune caractéristique ne domine le modèle.

![Image](https://cdn-media-1.freecodecamp.org/images/vuHimlxoXmGv4HdmwjMHjRnb11fEQ-cFGaz6)
_Trop tôt ?_

De plus, j'ai ajouté une régularisation L2 à la première couche également.

Maintenant que le modèle est terminé, j'ai augmenté mon jeu de données avec une certaine agitation générée. J'ai tourné, décalé, recadré, cisailé, zoomé, retourné et décalé les canaux de mes images d'entraînement. Cela aide à assurer que les images sont entraînées à travers le bruit commun.

Tous les systèmes ci-dessus sont destinés à prévenir le surapprentissage du modèle sur les données d'entraînement. Même s'il s'agit d'une tonne de données, je veux garder le modèle aussi généralisable à de nouvelles données que possible.

![Image](https://cdn-media-1.freecodecamp.org/images/Pq6cIzsEIcKcYmiMQekBd1zsPKtUchvrNwqF)
_Je t'ai couvert, modèle !_

Après avoir exécuté cela pendant longtemps, j'ai obtenu environ 87 % de précision sur le modèle ! C'est une assez bonne version un ! Rendons-la grande.

### Affiner votre modèle

#### Réglage fin de base

Une fois que les nouvelles couches sont entraînées, vous pouvez déverrouiller certaines couches plus profondes dans votre modèle Inception pour un réentraînement. Le code suivant déverrouille tout après la couche `conv2d_56`.

```py
set_trainable = False
for layer in conv_base.layers:    
    if layer.name == 'conv2d_56':
        set_trainable = True
    if set_trainable:
        layer.trainable = True
    else:
        layer.trainable = False
```

J'ai exécuté le modèle pendant longtemps avec ces couches nouvellement déverrouillées, et une fois que j'ai ajouté une décroissance exponentielle (via un taux d'apprentissage planifié), le modèle a convergé à 91 % de précision sur mes données de test !

Avec 300 000 images, trouver des erreurs dans les données d'entraînement était impossible. Mais avec un modèle avec seulement 9 % d'erreur, je pouvais décomposer les erreurs par catégorie, et ensuite je pouvais regarder seulement environ 5 400 images ! Essentiellement, je pouvais utiliser le modèle pour m'aider à trouver les mauvaises classifications et nettoyer le jeu de données !

Techniquement, cela ne trouverait que les faux négatifs. Ne faisant rien pour le biais sur les faux positifs, mais avec quelque chose qui détecte le contenu NSFW, j'imagine que le rappel est plus important que la précision.

#### La partie la plus importante de l'affinage

Même si vous avez beaucoup de données de test, elles sont généralement tirées du même puits. Le meilleur test est de rendre facile pour les autres d'utiliser et de vérifier votre modèle. Cela fonctionne mieux en open source et avec des démos simples. J'ai publié [http://nsfwjs.com](http://nsfwjs.com) qui a aidé la communauté à identifier les biais, et la communauté a fait exactement cela !

![Image](https://cdn-media-1.freecodecamp.org/images/ij7fLu-tghGePVI0E-da-xHaG2lwhK0Hkiwe)

La communauté a obtenu deux indicateurs intéressants de biais assez rapidement. Le plus amusant était que [Jeffrey Goldblum continuait à être mal catégorisé](https://shift.infinite.red/machine-learning-has-opinions-about-jeff-goldblum-strong-opinions-5438447ead35), et le moins amusant était que le modèle était trop sensible aux femmes.

Une fois que vous commencez à avoir des centaines de milliers d'images, il est difficile pour une seule personne (comme moi) d'identifier où un problème pourrait se trouver. Même si je regardais un millier d'images en détail pour le biais, je n'aurais même pas effleuré la surface du jeu de données dans son ensemble.

_C'est pourquoi il est important de parler._ Mal classer Jeffrey Goldblum est un point de données divertissant, mais identifier, documenter et ouvrir un ticket avec des exemples fait quelque chose de puissant et de bien. J'ai pu me mettre au travail pour corriger le biais.

Avec de nouvelles images, un entraînement amélioré et une meilleure validation, j'ai pu réentraîner le modèle sur quelques semaines et obtenir un bien meilleur résultat. Le modèle résultant était beaucoup plus précis dans la nature. Eh bien, à moins que vous n'ayez ri aussi fort que moi à propos du problème de Jeffrey Goldblum.

**Si je pouvais fabriquer un défaut... Je garderais Jeff.** Mais hélas, nous avons atteint 93 % de précision !

![Image](https://cdn-media-1.freecodecamp.org/images/avOLUcFEzFYhgsl7AirD9r5CC-PZdq3DtaEe)

### En Résumé

Cela a peut-être pris beaucoup de temps, mais ce n'était pas difficile, et c'était amusant de construire un modèle. Je vous suggère de prendre le code source et d'essayer par vous-même ! Je vais probablement même tenter de réentraîner le modèle avec d'autres frameworks pour comparaison.

> Montrez-moi ce que vous avez. Contribuez ou ⭐️ Surveillez le dépôt si vous souhaitez voir les progrès : [https://github.com/GantMan/nsfw_model](https://github.com/GantMan/nsfw_model)

![Image](https://cdn-media-1.freecodecamp.org/images/ruqh7LQQn8zhBYOaEmCVq76aF0eRD4eYHgG0)

![Image](https://cdn-media-1.freecodecamp.org/images/70liozeM4alstSXP78IIk8SbNCiiOFrnasPF)

[Gant Laborde](https://www.freecodecamp.org/news/how-to-set-up-nsfw-content-detection-with-machine-learning-229a9725829c/undefined) est Chief Technology Strategist chez [Infinite Red](http://infinite.red), un auteur publié, professeur adjoint, conférencier public mondial et scientifique fou en formation. Applaudissez/suivez/[tweetez](https://twitter.com/GantLaborde) ou rendez-lui visite [lors d'une conférence](http://gantlaborde.com/).

#### Avez-vous une minute ? Jetez un œil à quelques autres articles :

[**Évitez les cauchemars — NSFW JS**](https://shift.infinite.red/avoid-nightmares-nsfw-js-ab7b176978b1)
[_Vérification côté client du contenu indécent pour l'âme_shift.infinite.red](https://shift.infinite.red/avoid-nightmares-nsfw-js-ab7b176978b1)
[**5 Choses qui Sucent à propos du Travail à Distance**](https://shift.infinite.red/5-things-that-suck-about-remote-work-506b98dd38f9)
[_Les Pièges du Travail à Distance + Solutions Proposées_shift.infinite.red](https://shift.infinite.red/5-things-that-suck-about-remote-work-506b98dd38f9)