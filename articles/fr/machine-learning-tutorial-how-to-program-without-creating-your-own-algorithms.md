---
title: 'Tutoriel de Machine Learning : Comment programmer sans créer vos propres algorithmes'
subtitle: ''
author: Mark Mahoney
co_authors: []
series: null
date: '2025-10-09T15:49:20.886Z'
originalURL: https://freecodecamp.org/news/machine-learning-tutorial-how-to-program-without-creating-your-own-algorithms
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1760024939823/c2c53158-a2ec-4fe2-b222-236bef773e6b.png
tags:
- name: Perceptron
  slug: perceptron
- name: Supervised learning
  slug: supervised-learning
- name: Machine Learning
  slug: machine-learning
- name: AI
  slug: ai
seo_title: 'Tutoriel de Machine Learning : Comment programmer sans créer vos propres
  algorithmes'
seo_desc: 'Recreating the First Machine Learning Demo

  In 1958, Frank Rosenblatt demonstrated something remarkable to reporters in Washington,
  D.C. His "perceptron" could look at cards with shapes on them and tell which side
  the shape was on. The remarkable thin...'
---

## Recréer la première démo de Machine Learning

En 1958, [Frank Rosenblatt](https://en.wikipedia.org/wiki/Frank_Rosenblatt) a fait une démonstration remarquable aux journalistes à Washington, D.C. Son \"[perceptron](https://en.wikipedia.org/wiki/Mark_I_Perceptron)\" pouvait examiner des cartes comportant des formes et dire de quel côté se trouvait la forme. Ce qui était remarquable, c'est que le système n'était pas explicitement programmé pour faire cela – il a appris à le faire en regardant des exemples.

Dans les systèmes traditionnels, un programmeur réfléchit aux entrées d'un programme et conçoit des structures de données et des algorithmes pour résoudre le problème et produire des sorties utiles. Le programmeur humain est la vedette du spectacle.

Les systèmes de Machine Learning ne nécessitent pas qu'un programmeur spécifie **comment** résoudre un problème. Avec le [Machine Learning supervisé](https://en.wikipedia.org/wiki/Supervised_learning), les **entrées et sorties** du système sont utilisées pour **entraîner** le système. Il s'agit d'un changement fondamental dans la construction de systèmes afin qu'ils puissent reconnaître des modèles dans de nouvelles entrées et prédire des sorties. L'**apprentissage** est la vedette du spectacle.

Ce [code playback](https://playbackpress.com/books/cppbook/chapter/12/3) recrée l'expérience de Rosenblatt en utilisant des techniques modernes de programmation orientée objet. Vous verrez deux solutions au même problème. La première utilise la programmation traditionnelle où je conçois un algorithme pour résoudre le problème. L'autre est une utilisation très simple du Machine Learning qui **apprend** comment résoudre le problème.

[![](https://cdn.hashnode.com/res/hashnode/image/upload/v1759643953052/d58b6769-0f08-42c7-b228-3e73d9ce541b.png align=\"center\")](https://playbackpress.com/books/cppbook/chapter/12/3)

## Le problème

Chaque carte a une forme rectangulaire sur le côté gauche ou droit. Dans la démo originale de Rosenblatt, les cartes sont photographiées puis transformées en images de 20x20 pixels. Dans ce programme, je simule les cartes et les images. Le rôle du programme est d'examiner de nouvelles cartes et de prédire de quel côté se trouve la forme.

## L'approche traditionnelle

Le [code playback](https://playbackpress.com/books/cppbook/chapter/12/3) commence par une solution que j'ai imaginée. J'ai réfléchi aux entrées du système, 400 pixels d'une image, et j'ai développé un algorithme pour compter les pixels actifs de chaque côté. Le côté qui a le plus de pixels est celui pour lequel je « prédis » qu'il contient la forme.

Cela fonctionne bien. Les 500 cartes de test sont toutes prédites correctement. Mais j'ai dû dire à l'ordinateur exactement quoi faire.

## L'approche Machine Learning

Vient ensuite le perceptron, l'un des premiers exemples de Machine Learning. On lui donne de nombreuses entrées différentes (images de 400 pixels) et des sorties (étiquettes associées à chaque carte indiquant de quel côté se trouve la forme). Le perceptron prend les entrées et les sorties et apprend à prédire où se trouve une forme.

En tant que programmeur, je ne lui dis pas comment faire. Je configure le programme pour qu'il puisse apprendre des exemples qu'il voit pendant l'entraînement.

Mon perceptron utilise 400 poids (un pour chaque position de pixel). Au départ, tous les poids sont fixés à zéro. Le perceptron effectue des prédictions en multipliant chaque valeur de pixel par sa valeur de poids correspondante, puis en additionnant le tout. Si la somme est négative, il prédira la gauche. Sinon, il prédira la droite.

Le perceptron s'entraîne sur des exemples étiquetés. Lorsqu'il fait une mauvaise prédiction, il apprend en ajustant les poids concernés. Après l'entraînement, il réussit très bien à prédire correctement les cartes de test.

## Ce que vous apprendrez

Le [code playback](https://playbackpress.com/books/cppbook/chapter/12/3) vous guide à travers :

* La création de la représentation de la carte et des données de pixels
    
* L'implémentation de la solution sans IA (pour que vous puissiez voir l'approche traditionnelle)
    
* La construction d'une classe perceptron avec des poids
    
* La compréhension du mécanisme de prédiction (somme des produits)
    
* L'observation de la mise à jour des poids par l'entraînement en fonction des erreurs
    
* L'évolution des poids, passant de valeurs aléatoires à des modèles appris
    
* La compréhension de pourquoi certaines approches initiales échouent et comment les corriger
    

Vous verrez les valeurs réelles des poids après l'entraînement. Certains modèles sont évidents. D'autres sont surprenants. Le playback vous met au défi de comprendre et d'expliquer ces modèles.

## Pourquoi c'est important

C'est l'un des exemples les plus simples de Machine Learning que vous puissiez étudier. Le perceptron est essentiellement un neurone unique. Les réseaux de neurones modernes empilent de nombreux neurones en couches. Ils peuvent apprendre des modèles beaucoup plus complexes, mais l'idée de base est la même. C'est un excellent moyen de commencer votre voyage si vous voulez en savoir plus sur les réseaux de neurones, le Machine Learning et l'IA.

## Apprentissage interactif

[**Consultez le code playback complet ici**](https://playbackpress.com/books/cppbook/chapter/12/3)

Le playback inclut quelques défis en posant des questions en cours de route. Pouvez-vous déterminer combien d'exemples d'entraînement sont réellement nécessaires ? Quand le perceptron cesse-t-il de faire des erreurs pendant l'entraînement ? Le code est disponible en téléchargement pour que vous puissiez l'expérimenter, vous permettant de recréer un morceau de l'histoire de l'IA. Le perceptron de Rosenblatt est là où tout a commencé.

Le support de code playback est différent des vidéos ou tutoriels traditionnels. Vous êtes guidé à travers le code avec un récit et vous découvrez mes processus de réflexion. Si vous aimez ce format, j'ai encore plus de contenu gratuit sur mon site, [Playback Press](https://playbackpress.com/books). N'hésitez pas à partager vos commentaires, questions ou retours par e-mail : [mark@playbackpress.com](mailto:mark@playbackpress.com).