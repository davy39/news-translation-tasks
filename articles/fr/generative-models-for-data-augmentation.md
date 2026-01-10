---
title: Comment fonctionnent les modèles génératifs dans l'apprentissage profond ?
  Les modèles génératifs pour l'augmentation de données expliqués
subtitle: ''
author: Oyedele Tioluwani
co_authors: []
series: null
date: '2024-07-26T12:22:23.000Z'
originalURL: https://freecodecamp.org/news/generative-models-for-data-augmentation
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/glenn-carstens-peters-1F4MukO0UNg-unsplash.jpg
tags:
- name: Deep Learning
  slug: deep-learning
seo_title: Comment fonctionnent les modèles génératifs dans l'apprentissage profond
  ? Les modèles génératifs pour l'augmentation de données expliqués
seo_desc: 'Data is at the heart of model training in the world of deep learning. The
  quantity and quality of training data determine the effectiveness of machine learning
  algorithms.

  On the other hand, obtaining massive amounts of precisely categorized data is ...'
---

Les données sont au cœur de l'entraînement des modèles dans le monde de l'apprentissage profond. La quantité et la qualité des données d'entraînement déterminent l'efficacité des algorithmes d'apprentissage automatique.

D'autre part, l'obtention de grandes quantités de données précisément catégorisées est une opération difficile et coûteuse en ressources. C'est là que l'augmentation de données entre en jeu en tant que solution attrayante, avec le potentiel innovant des modèles génératifs à son avant-garde.

Dans cet article, nous examinerons la pertinence fondamentale des modèles génératifs dans l'augmentation de données pour l'apprentissage profond, tels que les Variational Autoencoders (VAEs) et les Generative Adversarial Networks (GANs).

## Qu'est-ce que les modèles génératifs ?

Les modèles génératifs sont un type de modèle d'apprentissage automatique qui crée de nouveaux échantillons de données similaires à ceux d'un ensemble de données donné. Ils découvrent des tendances et des structures cachées dans les données, leur permettant de générer des points de données synthétiques similaires aux données réelles.

Ces modèles sont utilisés dans diverses applications, telles que la génération d'images, la génération de texte, l'augmentation de données, et autres. Par exemple, dans un projet de génération d'images, un modèle génératif pourrait être entraîné sur des images de chats et de chiens pour apprendre à générer de nouvelles images de chats et de chiens.

Ils apprennent des motifs et des styles à partir des données existantes et appliquent ces informations pour créer des choses similaires. C'est comme si votre ordinateur avait un moteur créatif qui génère de nouvelles idées après avoir étudié les tactiques utilisées dans les précédentes.

## Qu'est-ce que l'augmentation de données ?

L'augmentation de données est une technique d'apprentissage automatique et d'apprentissage profond qui utilise diverses transformations et ajustements des données existantes pour améliorer la qualité et la quantité d'un ensemble de données d'entraînement. Cela implique de générer de nouveaux échantillons de données à partir de ceux existants pour élargir la taille et la diversité d'un ensemble de données.

Le but principal de l'augmentation de données est d'améliorer les performances, la généralisation et la robustesse des modèles d'apprentissage automatique, notamment dans les tâches de vision par ordinateur et d'autres domaines pilotés par les données.

L'augmentation de données peut être utilisée pour améliorer les ensembles de données pour une large gamme d'applications d'apprentissage automatique, telles que la classification d'images, la détection d'objets et le traitement du langage naturel. Par exemple, l'augmentation de données peut être utilisée pour créer des photos synthétiques de visages, qui peuvent ensuite être utilisées pour entraîner un modèle d'apprentissage profond à détecter des visages dans des images du monde réel.

L'augmentation de données est une méthode importante dans le monde des données car elle répond aux préoccupations sous-jacentes de la quantité et de la qualité des données. L'accès à de grandes quantités de données diverses et bien étiquetées est nécessaire pour construire des modèles solides et précis dans de nombreuses applications d'apprentissage automatique et d'apprentissage profond.

L'augmentation de données est une méthode bénéfique pour élargir les ensembles de données limités en créant de nouveaux échantillons, ce qui améliore la généralisation et les performances des modèles. De plus, elle améliore la capacité des algorithmes d'apprentissage automatique à gérer les variations du monde réel, résultant en des systèmes d'IA plus fiables et flexibles.

## Pourquoi utiliser des modèles génératifs pour l'augmentation de données ?

Il existe plusieurs raisons pour lesquelles les modèles génératifs sont utilisés pour l'augmentation de données en apprentissage automatique :

1. **Diversité accrue des données :** Les modèles génératifs peuvent aider à augmenter la variété des ensembles de données, rendant les modèles d'apprentissage automatique plus résilients aux fluctuations du monde réel. Un modèle génératif pourrait être utilisé pour générer des images synthétiques de visages avec diverses expressions, âges et ethnies. Cela pourrait aider un modèle d'apprentissage automatique à apprendre à détecter des visages de manière plus fiable dans une large gamme de scénarios du monde réel.

2. **Amélioration de la généralisation des modèles :** L'utilisation de modèles génératifs pour augmenter les données expose les modèles d'apprentissage automatique à une collection plus large de variables de données pendant l'entraînement. Ce processus améliore la capacité du modèle à généraliser à de nouvelles données, précédemment inconnues, et ses performances globales. Cela est particulièrement pertinent pour les modèles d'apprentissage profond, qui nécessitent de vastes volumes de données pour un entraînement adéquat.

3. **Surmonter la rareté des données :** L'obtention d'un grand ensemble de données diversifié et étiqueté peut être un problème substantiel dans de nombreuses applications d'apprentissage automatique. En développant des données synthétiques, les modèles génératifs peuvent aider à gérer la rareté des données en réduisant la dépendance aux données réelles limitées.

4. **Réduction des biais :** En générant de nouveaux échantillons de données qui abordent les catégories sous-représentées ou biaisées, les modèles génératifs peuvent être utilisés pour éliminer les biais dans les données d'entraînement, améliorant l'équilibre dans les applications d'IA.

## Modèles génératifs pour l'augmentation de données

Deux principaux types de modèles génératifs peuvent être utilisés pour l'augmentation de données :

* Generative Adversarial Networks (GANs)

* Variational AutoEncoders (VAEs)

### Generative Adversarial Networks (GANs)

Les GANs sont des conceptions de réseaux de neurones utilisées pour créer de nouveaux échantillons de données comparables aux données d'entraînement. Ce sont des modèles d'apprentissage qui peuvent construire de nouveaux éléments qui semblent être tirés d'un certain ensemble de données. Par exemple, les GANs peuvent être entraînés sur un groupe de photos et ensuite utilisés pour produire de nouvelles images qui semblent provenir de l'ensemble original.

Voici une brève explication de comment fonctionnent les GANs :

* Un nouvel échantillon de données est généré par le générateur. Le discriminateur reçoit à la fois des échantillons nouveaux et réels.

* Le discriminateur tente de déterminer quels échantillons sont réels et lesquels sont fabriqués.

* La sortie du discriminateur est utilisée pour mettre à jour à la fois le générateur et le discriminateur.

Le générateur crée une image synthétique en prenant des données bruitées comme entrée. Le discriminateur essaie de classer correctement à la fois l'image fausse du générateur et une image réelle de l'ensemble d'entraînement.

Le générateur essaie d'améliorer ses variables pour produire une image fausse plus convaincante qui peut tromper le discriminateur. Le discriminateur cherche à s'améliorer en ajustant ses variables pour distinguer entre les images réelles et frauduleuses. Les deux réseaux continuent de rivaliser et de s'améliorer jusqu'à ce que le générateur produise des données similaires aux données réelles.

Il est adapté à l'augmentation de données grâce à sa capacité à générer des données synthétiques indiscernables des échantillons de données authentiques. Cela est significatif car les algorithmes d'apprentissage automatique apprennent à partir des données, et plus les données utilisées pour entraîner un modèle sont nombreuses, meilleures seront ses performances. D'autre part, la collecte de suffisamment de données réelles pour entraîner un modèle d'apprentissage automatique peut être coûteuse et chronophage.

Les GANs peuvent aider à réduire le coût et le temps nécessaires à la collecte de données en produisant des données synthétiques similaires aux données réelles. Cela est particulièrement bénéfique pour les applications où la collecte de données réelles est difficile ou coûteuse, comme l'imagerie médicale ou les données de vidéosurveillance.

Les GANs peuvent également être utilisés en raison de leur variété. Cela est dû au fait que les GANs peuvent être utilisés pour produire des échantillons de données qui n'existaient pas dans l'ensemble de données original. Cela peut aider à améliorer la robustesse des modèles d'apprentissage automatique pour les variations du monde réel.

### Variational AutoEncoders (VAEs)

Les VAEs sont un type de modèle génératif et une variation des autoencodeurs utilisés en apprentissage automatique et en apprentissage profond. Ce sont une forme de modèle génératif qui peut générer de nouveaux échantillons de données comparables aux données sur lesquelles ils ont été entraînés.

Les VAEs sont une sorte de modèle bayésien, ce qui implique qu'ils emploient des distributions de probabilité pour représenter l'incertitude dans les données. Cela permet aux VAEs de créer des échantillons de données plus réalistes que d'autres types de modèles génératifs.

Les VAEs fonctionnent en apprenant la représentation des données dans l'espace latent. L'espace latent est une représentation compressée des données qui capture les qualités les plus pertinentes des données. En échantillonnant à partir de l'espace latent et en décodant les échantillons dans l'espace de données original, les VAEs peuvent ensuite être utilisés pour produire de nouveaux échantillons de données.

Voici une illustration simple de comment fonctionne un VAE :

* L'encodeur reçoit un échantillon de données en entrée, comme une image d'un animal.

* L'encodeur génère une représentation de l'espace latent des données, qui est une version compressée de l'image qui capture les caractéristiques les plus pertinentes du chat, telles que la forme, la taille et la couleur de la fourrure.

* La représentation de l'espace latent est alimentée dans le décodeur.

* Le décodeur génère un échantillon de données reconstruit, qui est une nouvelle image d'un animal qui ressemble à l'image originale.

L'encodeur et le décodeur sont enseignés pour réduire la différence entre les images reconstruites et originales. Cela est accompli en employant une fonction de perte qui compare la similarité des deux photos.

Les VAEs sont un outil puissant de modélisation générative qui peut être utilisé pour la production d'images, la génération de texte, la compression de données et le débruitage de données. Ils offrent un cadre probabiliste pour modéliser et produire des distributions de données complexes tout en préservant un espace latent structuré pour la production et l'interpolation de données.

La capacité à générer des données similaires aux données réelles les qualifie également pour l'augmentation de données. Cela signifie que les données augmentées produites par les VAEs sont hautement réalistes et alignées avec la distribution des données sous-jacentes, ce qui est requis pour une augmentation de données efficace.

Chaque point dans l'espace latent structuré des VAEs représente une variation significative des données. Cela permet une création de données contrôlée. Les utilisateurs peuvent construire de nouvelles instances de données avec des attributs ou des variantes spécifiques en échantillonnant différents endroits dans l'espace latent, ce qui les rend adaptés à une augmentation de données ciblée.

Les VAEs peuvent résoudre les problèmes de rareté des données en générant des données synthétiques lorsque les données réelles sont limitées. Cela est particulièrement précieux dans les scénarios où la collecte de plus de données réelles est impratique ou coûteuse.

À mesure que les VAEs continuent de s'améliorer, ils joueront probablement un rôle de plus en plus important dans l'entraînement des modèles d'apprentissage automatique.

## Conclusion

Les modèles génératifs ont joué un rôle significatif dans la pratique de l'augmentation de données dans le domaine de l'apprentissage automatique.

Par exemple, les GANs ont été utilisés pour générer des images synthétiques de visages, qui ont été utilisées pour entraîner des modèles d'apprentissage automatique à détecter des visages dans des images du monde réel.

Les VAEs ont également été utilisés pour créer des images synthétiques d'automobiles qui ont ensuite été utilisées pour entraîner des modèles d'apprentissage automatique à reconnaître des voitures dans des photographies du monde réel.

Ce sont toutes des applications réelles des modèles génératifs dans l'augmentation de données.

J'espère que cet article a été utile.