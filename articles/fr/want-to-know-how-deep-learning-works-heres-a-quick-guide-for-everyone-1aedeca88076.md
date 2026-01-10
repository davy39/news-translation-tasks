---
title: Vous voulez savoir comment fonctionne le Deep Learning ? Voici un guide rapide
  pour tous.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-23T16:06:33.000Z'
originalURL: https://freecodecamp.org/news/want-to-know-how-deep-learning-works-heres-a-quick-guide-for-everyone-1aedeca88076
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1mpE6fsq5LNxH31xeTWi5w.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: business
  slug: business
- name: startup
  slug: startup
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Vous voulez savoir comment fonctionne le Deep Learning ? Voici un guide
  rapide pour tous.
seo_desc: 'By Radu Raicea

  Artificial Intelligence (AI) and Machine Learning (ML) are some of the hottest topics
  right now.

  The term “AI” is thrown around casually every day. You hear aspiring developers
  saying they want to learn AI. You also hear executives say...'
---

Par Radu Raicea

[**Intelligence Artificielle**](https://en.wikipedia.org/wiki/Artificial_intelligence) (AI) et [**Machine Learning**](https://en.wikipedia.org/wiki/Machine_learning) (ML) sont des sujets très en vogue en ce moment.

Le terme **« AI »** est utilisé de manière informelle tous les jours. Vous entendez des développeurs en herbe dire qu'ils veulent apprendre l'AI. Vous entendez aussi des cadres dire qu'ils veulent implémenter l'AI dans leurs services. Mais bien souvent, beaucoup de ces personnes ne comprennent pas ce qu'est l'AI.

Une fois que vous aurez lu cet article, vous comprendrez les bases de l'AI et du ML. Plus important encore, vous comprendrez comment le [Deep Learning](https://en.wikipedia.org/wiki/Deep_learning), le type de ML le plus populaire, fonctionne.

Ce guide est destiné à tout le monde, donc aucune mathématique avancée ne sera impliquée.

### Contexte

La première étape pour comprendre comment le Deep Learning fonctionne est de saisir les différences entre les termes importants.

#### Artificial Intelligence vs Machine Learning

> **Artificial Intelligence** est la réplication de l'intelligence humaine dans les ordinateurs.

Quand la recherche en AI a commencé, les chercheurs essayaient de répliquer l'intelligence humaine pour des tâches spécifiques — comme jouer à un jeu.

Ils ont introduit un grand nombre de règles que l'ordinateur devait respecter. L'ordinateur avait une liste spécifique d'actions possibles et prenait des décisions [basées sur ces règles](https://en.wikipedia.org/wiki/Expert_system).

> **Machine Learning** fait référence à la capacité d'une machine à apprendre en utilisant de grands ensembles de données au lieu de règles codées en dur.

Le ML permet aux ordinateurs d'apprendre par eux-mêmes. Ce type d'apprentissage tire parti de la puissance de calcul des ordinateurs modernes, qui peuvent facilement traiter de grands ensembles de données.

#### **Apprentissage supervisé vs apprentissage non supervisé**

> [**L'Apprentissage supervisé**](https://en.wikipedia.org/wiki/Supervised_learning) implique l'utilisation d'ensembles de données étiquetés qui ont des entrées et des sorties attendues.

Lorsque vous entraînez une AI à l'aide de l'apprentissage supervisé, vous lui donnez une entrée et lui indiquez la sortie attendue.

Si la sortie générée par l'AI est erronée, elle réajustera ses calculs. Ce processus est effectué de manière itérative sur l'ensemble de données, jusqu'à ce que l'AI ne fasse plus d'erreurs.

Un exemple d'apprentissage supervisé est une AI de prévision météorologique. Elle apprend à prédire la météo en utilisant des données historiques. Ces données d'entraînement ont des entrées (pression, humidité, vitesse du vent) et des sorties (température).

> [**L'Apprentissage non supervisé**](https://en.wikipedia.org/wiki/Unsupervised_learning) est la tâche de machine learning utilisant des ensembles de données sans structure spécifiée.

Lorsque vous entraînez une AI en utilisant l'apprentissage non supervisé, vous laissez l'AI effectuer des classifications logiques des données.

Un exemple d'apprentissage non supervisé est une AI de prédiction de comportement pour un site de commerce électronique. Elle n'apprendra pas en utilisant un ensemble de données étiqueté d'entrées et de sorties.

Au lieu de cela, elle créera sa propre classification des données d'entrée. Elle vous dira quel type d'utilisateurs est le plus susceptible d'acheter différents produits.

### Maintenant, comment fonctionne le Deep Learning ?

Vous êtes maintenant prêt à comprendre ce qu'est le Deep Learning et comment il fonctionne.

Le Deep Learning est une méthode de **machine learning**. Il nous permet d'entraîner une AI à prédire des sorties, étant donné un ensemble d'entrées. L'apprentissage supervisé et non supervisé peuvent tous deux être utilisés pour entraîner l'AI.

Nous allons apprendre comment le deep learning fonctionne en construisant un service hypothétique d'**estimation du prix des billets d'avion**. Nous l'entraînerons en utilisant une méthode d'apprentissage supervisé.

Nous voulons que notre estimateur de prix de billets d'avion prédise le prix en utilisant les entrées suivantes (nous excluons les billets aller-retour pour plus de simplicité) :

* Aéroport d'origine
* Aéroport de destination
* Date de départ
* Compagnie aérienne

#### Réseaux de neurones

Regardons à l'intérieur du cerveau de notre AI.

Comme les animaux, le cerveau de notre estimateur AI possède des neurones. Ils sont représentés par des cercles. Ces neurones sont interconnectés.

![Image](https://cdn-media-1.freecodecamp.org/images/n1u8onOuWkl5EzzPzBe4n8hOhbTDIDyMBrPM)
_Crédit image : [CS231n](http://cs231n.github.io/neural-networks-1/" rel="noopener" target="_blank" title=")_

Les neurones sont regroupés en trois types de couches différents :

1. Input Layer (Couche d'entrée)
2. Hidden Layer(s) (Couche(s) cachée(s))
3. Output Layer (Couche de sortie)

L'**input layer** reçoit les données d'entrée. Dans notre cas, nous avons quatre neurones dans la couche d'entrée : Aéroport d'origine, Aéroport de destination, Date de départ et Compagnie aérienne. L'input layer transmet les entrées à la première couche cachée.

Les **hidden layers** effectuent des calculs mathématiques sur nos entrées. L'un des défis de la création de réseaux de neurones est de décider du nombre de couches cachées, ainsi que du nombre de neurones pour chaque couche.

Le « **Deep** » dans Deep Learning fait référence au fait d'avoir **plus d'une** couche cachée.

L'**output layer** renvoie les données de sortie. Dans notre cas, elle nous donne la prédiction du prix.

![Image](https://cdn-media-1.freecodecamp.org/images/GDzpkmRqzE6KPOBfTfuShEziKgHWJa9djQ2O)

Alors, comment calcule-t-il la prédiction de prix ?

C'est ici que la **magie du Deep Learning** commence.

Chaque connexion entre les neurones est associée à un **weight** (poids). Ce poids dicte l'importance de la valeur d'entrée. Les poids initiaux sont définis de manière aléatoire.

Lors de la prédiction du prix d'un billet d'avion, la date de départ est l'un des facteurs les plus lourds. Par conséquent, les connexions des neurones de la date de départ auront un poids important.

![Image](https://cdn-media-1.freecodecamp.org/images/nV1gwecr8GV5hvNROR3yBJWn5MtPRyqiCHoX)
_Crédit image : [CodeProject](https://www.codeproject.com/Articles/1200392/Neural-Network" rel="noopener" target="_blank" title=")_

Chaque neurone possède une [Activation Function](https://en.wikipedia.org/wiki/Activation_function). Ces fonctions sont difficiles à comprendre sans raisonnement mathématique.

Simplement dit, l'un de ses objectifs est de « standardiser » la sortie du neurone.

Une fois qu'un ensemble de données d'entrée est passé par toutes les couches du réseau de neurones, il renvoie les données de sortie via l'output layer.

Rien de compliqué, n'est-ce pas ?

#### Training the Neural Network

Entraîner l'AI est la partie la plus difficile du Deep Learning. Pourquoi ?

1. Vous avez besoin d'un **grand ensemble de données**.
2. Vous avez besoin d'une **grande** quantité de **puissance de calcul**.

Pour notre estimateur de prix de billets d'avion, nous devons trouver des données historiques sur les prix des billets. Et en raison du grand nombre de combinaisons possibles d'aéroports et de dates de départ, nous avons besoin d'une très grande liste de prix de billets.

Pour entraîner l'AI, nous devons lui donner les entrées de notre ensemble de données et comparer ses sorties avec les sorties de l'ensemble de données. Comme l'AI n'est pas encore entraînée, ses sorties seront fausses.

Une fois que nous avons parcouru tout l'ensemble de données, nous pouvons créer une fonction qui nous montre à quel point les sorties de l'AI étaient éloignées des sorties réelles. Cette fonction est appelée la [Cost Function](https://en.wikipedia.org/wiki/Loss_function).

Idéalement, we want our cost function to be zero. C'est à ce moment-là que les sorties de notre AI sont les mêmes que les sorties de l'ensemble de données.

#### **Comment pouvons-nous réduire la cost function ?**

Nous modifions les weights entre les neurones. Nous pourrions les modifier de manière aléatoire jusqu'à ce que notre cost function soit basse, mais ce n'est pas très efficace.

Au lieu de cela, nous utiliserons une technique appelée le [Gradient Descent](https://en.wikipedia.org/wiki/Gradient_descent).

Le Gradient Descent est une technique qui nous permet de trouver le minimum d'une fonction. Dans notre cas, nous cherchons le minimum de la cost function.

Elle fonctionne en **modifiant les weights** par petits incréments **après chaque itération de l'ensemble de données**. En calculant la dérivée (ou gradient) de la cost function pour un certain ensemble de weights, nous sommes capables de voir dans quelle direction se trouve le minimum.

![Image](https://cdn-media-1.freecodecamp.org/images/d58SH7gTWXH9ZnoEd91iL-X3OUQcPCJj4J-j)
_Crédit image : [Sebastian Raschka](https://sebastianraschka.com/faq/docs/closed-form-vs-gd.html" rel="noopener" target="_blank" title=")_

Pour minimiser la cost function, vous devez itérer à travers votre ensemble de données de nombreuses fois. C'est pourquoi vous avez besoin d'une grande quantité de puissance de calcul.

La mise à jour des weights à l'aide du gradient descent se fait **automatiquement**. C'est ça la magie du Deep Learning !

Une fois que nous avons entraîné notre AI d'estimation de prix de billets d'avion, nous pouvons l'utiliser pour prédire les prix futurs.

### Où puis-je en apprendre plus ?

Il existe de nombreux autres types de réseaux de neurones : les [Convolutional Neural Networks](https://en.wikipedia.org/wiki/Convolutional_neural_network) pour la [Computer Vision](https://en.wikipedia.org/wiki/Computer_vision) et les [Recurrent Neural Networks](https://en.wikipedia.org/wiki/Recurrent_neural_network) pour le [Natural Language Processing](https://en.wikipedia.org/wiki/Natural_language_processing).

Si vous souhaitez apprendre l'aspect technique du Deep Learning, je vous suggère de suivre un cours en ligne.

Actuellement, l'un des meilleurs cours pour le Deep Learning est la [Deep Learning Specialization](https://www.coursera.org/specializations/deep-learning) d'[Andrew Ng](https://www.freecodecamp.org/news/want-to-know-how-deep-learning-works-heres-a-quick-guide-for-everyone-1aedeca88076/undefined). Si vous n'êtes pas intéressé par l'obtention d'un certificat, vous n'avez pas besoin de payer pour le cours. Vous pouvez le suivre en auditeur libre à la place.

Si vous avez des questions ou si vous souhaitez des explications plus techniques sur les concepts, n'hésitez pas à les poser ci-dessous !

### En résumé…

* Le Deep Learning utilise un Neural Network pour imiter l'intelligence animale.
* Il existe trois types de couches de neurones dans un réseau de neurones : l'Input Layer, la ou les Hidden Layer(s) et l'Output Layer.
* Les connexions entre les neurones sont associées à un weight, dictant l'importance de la valeur d'entrée.
* Les neurones appliquent une Activation Function sur les données pour « standardiser » la sortie provenant du neurone.
* Pour entraîner un Neural Network, vous avez besoin d'un grand ensemble de données.
* L'itération à travers l'ensemble de données et la comparaison des sorties produiront une Cost Function, indiquant à quel point l'AI est éloignée des sorties réelles.
* Après chaque itération à travers l'ensemble de données, les weights entre les neurones sont ajustés à l'aide du Gradient Descent pour réduire la cost function.

Si vous avez apprécié cet article, n'hésitez pas à me laisser quelques claps pour que plus de personnes le voient. Merci !

**Vous pouvez également consulter mon [récit sur la façon dont j'ai obtenu mon stage chez Shopify](https://medium.freecodecamp.org/how-i-got-an-internship-at-shopify-432cbe8da58a) !**

Pour plus de mises à jour, suivez-moi sur [Twitter](https://twitter.com/radu_raicea).