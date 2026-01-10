---
title: Comment installer TensorFlow et Keras en utilisant Anaconda Navigator — sans
  la ligne de commande
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-24T10:15:00.000Z'
originalURL: https://freecodecamp.org/news/install-tensorflow-and-keras-using-anaconda-navigator-without-command-line
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca140740569d1a4ca4d8c.jpg
tags:
- name: anaconda
  slug: anaconda
- name: keras
  slug: keras
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
- name: TensorFlow
  slug: tensorflow
seo_title: Comment installer TensorFlow et Keras en utilisant Anaconda Navigator —
  sans la ligne de commande
seo_desc: 'By Ekapope Viriyakovithya

  Say no to pip install in the command line! Here''s an alternative way to install
  TensorFlow on your local machine in 3 steps.


  _Photo by [Unsplash](https://unsplash.com/@kowalikus?utm_source=ghost&utm_medium=referral&utm_camp...'
---

Par Ekapope Viriyakovithya

Dites non à pip install dans la ligne de commande ! Voici une alternative pour installer TensorFlow sur votre machine locale en 3 étapes.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-239.png)
_Photo par [Unsplash](https://unsplash.com/@kowalikus?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Krzysztof Kowalik</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

# Pourquoi j'écris cela ?

J'ai joué avec pip install avec plusieurs configurations pendant plusieurs heures, essayant de comprendre comment configurer correctement mon environnement Python pour TensorFlow et Keras.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-31.png)
_pourquoi tensorflow est-il si difficile à installer — 600k+ résultats_

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-32.png)
_impossible d'installer tensorflow sur windows site:stackoverflow.com — 26k+ résultats_

# Juste avant d'abandonner, j'ai trouvé ceci...

_[Un avantage clé de l'installation de TensorFlow en utilisant conda plutôt que pip est le résultat du système de gestion des paquets conda. Lorsque TensorFlow est installé en utilisant conda, conda installe toutes les dépendances nécessaires et compatibles pour les paquets également.](https://www.anaconda.com/tensorflow-in-anaconda/?source=post_page---------------------------) ___

Cet article vous guidera à travers le processus d'installation de TensorFlow et Keras en utilisant la version GUI d'Anaconda. Je suppose que vous avez déjà téléchargé et installé [Anaconda Navigator](https://www.anaconda.com/distribution/?source=post_page---------------------------).

# Commençons !

1. Lancez Anaconda Navigator. Allez dans l'onglet Environments et cliquez sur 'Create'.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-33.png)
_Allez dans l'onglet 'Environments', cliquez sur 'Create'_

2. Saisissez un nouveau nom d'environnement - j'ai mis 'tensorflow_env'. **Assurez-vous de sélectionner Python 3.6 ici !** Ensuite 'Create', cela peut prendre quelques minutes.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-34.png)
_assurez-vous de sélectionner Python 3.6_

3. Dans votre nouvel environnement 'tensorflow_env', sélectionnez 'Not installed', et tapez 'tensorflow'. Ensuite, cochez 'tensorflow' et 'Apply'. La fenêtre contextuelle apparaîtra, allez-y et appliquez. Cela peut prendre plusieurs minutes.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-35.png)

Faites de même pour 'keras'.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-36.png)

Vérifiez votre installation en important les paquets. Si tout est correct, la commande ne retournera rien. Si l'installation a échoué, vous obtiendrez une erreur.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-37.png)
_aucune erreur ne s'affiche — Yeah!_

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-38.png)
_Vous pouvez également essayer avec Spyder._

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-39.png)
_aucune erreur ne s'affiche — Yeah!_

Et... Ta-da ! C'est fait ! Vous pouvez suivre [cet article](https://towardsdatascience.com/how-to-build-a-neural-network-with-keras-e8faa33d0ae4?source=post_page---------------------------) pour tester vos nouveaux paquets installés :)

---

Merci d'avoir lu. Veuillez essayer et faites-moi savoir vos commentaires !

Envisagez de me suivre sur [GitHub](https://github.com/ekapope?source=post_page---------------------------), [Medium](https://medium.com/@ekapope.v?source=post_page---------------------------), et [Twitter](https://twitter.com/EkapopeV?source=post_page---------------------------) pour obtenir plus d'articles et de tutoriels sur votre fil d'actualité si vous aimez ce que je fais. :)