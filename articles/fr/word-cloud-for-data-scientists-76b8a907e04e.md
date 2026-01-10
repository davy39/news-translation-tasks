---
title: Une méthode simple pour créer des nuages de mots pour les data scientists
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-23T05:24:33.000Z'
originalURL: https://freecodecamp.org/news/word-cloud-for-data-scientists-76b8a907e04e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*HYtC28uzCWtTK2r_cR_3CA.png
tags:
- name: Data Science
  slug: data-science
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: text mining
  slug: text-mining
- name: visualization
  slug: visualization
seo_title: Une méthode simple pour créer des nuages de mots pour les data scientists
seo_desc: 'By Kavita Ganesan

  About a year ago, I looked high and low for a Python word cloud library that I could
  use from within my Jupyter notebook. I needed it to be flexible enough to use counts
  or tfidf when needed or just accept a set of words and corresp...'
---

Par Kavita Ganesan

Il y a environ un an, j'ai cherché partout une bibliothèque Python pour créer des nuages de mots que je pourrais utiliser directement dans mon notebook Jupyter. J'avais besoin qu'elle soit suffisamment flexible pour utiliser des `counts` ou `tfidf` si nécessaire, ou simplement accepter un ensemble de mots avec leurs poids correspondants.

J'ai été un peu surprise que quelque chose comme cela n'existe pas déjà dans des bibliothèques comme `plotly`. Tout ce que je voulais, c'était obtenir une compréhension rapide de mes données textuelles et de mes vecteurs de mots. Je pensais que ce n'était probablement pas trop demander…

Me voilà un an plus tard, utilisant ma propre bibliothèque de visualisation [word_cloud](https://github.com/kavgan/word_cloud). Ce n'est pas la plus joli ni la plus sophistiquée, mais elle fonctionne pour la plupart des cas. J'ai décidé de la partager afin que d'autres puissent également l'utiliser. Après l'[installation](https://github.com/kavgan/word_cloud), voici quelques façons de l'utiliser.

#### Générer des nuages de mots avec un seul document texte

Cet exemple montre comment générer des nuages de mots avec un seul document. Bien que les couleurs puissent être randomisées, dans cet exemple, les couleurs sont basées sur les paramètres de couleur par défaut.

Par défaut, les mots sont pondérés par leur fréquence, sauf si vous demandez explicitement une pondération tfidf. La pondération tfidf n'a de sens que si vous avez beaucoup de documents au départ.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HYtC28uzCWtTK2r_cR_3CA.png)
_nuage de mots basé sur un seul document_

#### Générer des nuages de mots à partir de plusieurs documents

Imaginons que vous avez 100 documents d'une même catégorie de nouvelles et que vous voulez simplement voir quelles sont les mentions courantes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*lKQBi3n4OfjawldVtXrU5g.png)
_nuage de mots basé sur plusieurs documents_

#### Générer des nuages de mots à partir de poids existants

Imaginons que vous avez un ensemble de mots avec leurs poids correspondants et que vous souhaitez simplement les visualiser. Tout ce que vous avez à faire est de vous assurer que les poids sont normalisés entre [0 - 1].

![Image](https://cdn-media-1.freecodecamp.org/images/1*NyGmBmZ4OOiOPLir9h4doA.png)
_nuage de mots à partir de poids existants_

J'espère que vous trouverez cela utile ! N'hésitez pas à proposer des modifications pour améliorer la sortie - il suffit d'ouvrir une pull request avec vos changements.

### Liens

* [Voir mon notebook Jupyter avec des exemples de code](https://colab.research.google.com/drive/1AkdUKEFmaYom77r6KPh18jdQrplIQbKQ)
* [Commencer à utiliser la bibliothèque word_cloud](https://github.com/kavgan/word_cloud)