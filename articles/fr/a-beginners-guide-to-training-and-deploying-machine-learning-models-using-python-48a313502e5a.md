---
title: Un guide pour débutants sur l'entraînement et le déploiement de modèles de
  machine learning avec Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-27T16:33:23.000Z'
originalURL: https://freecodecamp.org/news/a-beginners-guide-to-training-and-deploying-machine-learning-models-using-python-48a313502e5a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-W-ioBNBUF5eSDYWc-ZHxQ.png
tags:
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: scikit learn
  slug: scikit-learn
- name: 'tech '
  slug: tech
seo_title: Un guide pour débutants sur l'entraînement et le déploiement de modèles
  de machine learning avec Python
seo_desc: 'By Ivan Yung

  When I was first introduced to machine learning, I had no idea what I was reading.
  All the articles I read consisted of weird jargon and crazy equations. How could
  I figure all this out?

  I opened a new tab in Chrome and looked for easier...'
---

Par Ivan Yung

Lorsque j'ai été initié au machine learning, je n'avais aucune idée de ce que je lisais. Tous les articles que je lisais étaient remplis de jargon étrange et d'équations folles. Comment pourrais-je comprendre tout cela ?

J'ai ouvert un nouvel onglet dans Chrome et j'ai cherché des solutions plus simples. J'ai trouvé des APIs d'Amazon, Microsoft et Google qui faisaient tout le machine learning pour moi. Chaque projet de hackathon que je réalisais appelait leurs serveurs et WOW — cela avait l'air si intelligent ! J'étais accro.

Mais, après un an, j'ai réalisé que je n'apprenais rien. Tout ce que je faisais était décrit par cette bande dessinée Nedroid que j'ai modifiée :

![Image](https://cdn-media-1.freecodecamp.org/images/1*1YwLOx3wkKoLjRUD-NoiZA.png)
_[Source de l'image originale](https://nedroidcomics.tumblr.com/post/41879001445/the-internet" rel="noopener" target="_blank" title=")._

Finalement, je me suis assis et j'ai appris à utiliser le machine learning sans dépendre des mégacorporations. Et il s'avère que tout le monde peut le faire. Les bibliothèques actuelles que nous avons en Python sont incroyables. Dans cet article, je vais expliquer comment j'utilise ces bibliothèques pour créer un backend de machine learning approprié.

### Obtenir un jeu de données

Les projets de machine learning dépendent de la recherche de bons jeux de données. Si le jeu de données est mauvais ou trop petit, nous ne pouvons pas faire de prédictions précises. Vous pouvez trouver de bons jeux de données sur [Kaggle](http://kaggle.com) ou le [Dépôt de Machine Learning de l'UCI](https://archive.ics.uci.edu/ml/index.php).

Dans cet article, j'utilise un [jeu de données sur la qualité du vin](https://archive.ics.uci.edu/ml/datasets/Wine+Quality) avec de nombreuses caractéristiques et une étiquette. Les **caractéristiques** sont des variables indépendantes qui affectent la variable dépendante appelée **étiquette**. Dans ce cas, nous avons une colonne **étiquette** — la qualité du vin — qui est affectée par toutes les autres colonnes (caractéristiques comme le pH, la densité, l'acidité, etc.).

Dans le code Python suivant, j'utilise une bibliothèque appelée [pandas](https://pandas.pydata.org/) pour contrôler mon jeu de données. pandas fournit des jeux de données avec de nombreuses fonctions pour sélectionner et manipuler les données.

Tout d'abord, je charge le jeu de données dans un pandas et je le divise en étiquette et ses caractéristiques. Je saisis ensuite la colonne d'étiquette par son nom (quality) et je supprime la colonne pour obtenir toutes les caractéristiques.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Kybbe-8PK1jHttWyP0adow.png)
_Scikits-learn, la bibliothèque que nous utiliserons pour le machine learning_

### Entraîner un modèle

Le machine learning fonctionne en trouvant une relation entre une étiquette et ses caractéristiques. Nous faisons cela en montrant à un objet (notre modèle) un ensemble d'exemples de notre jeu de données. Chaque exemple aide à définir comment chaque caractéristique affecte l'étiquette. Nous appelons ce processus **l'entraînement de notre modèle**.

J'utilise l'objet estimateur de la bibliothèque [Scikit-learn](http://scikit-learn.org/stable/index.html) pour le machine learning simple. Les **estimateurs** sont des modèles vides qui créent des relations à travers un algorithme prédéfini.

Pour ce jeu de données sur le vin, je crée un modèle à partir d'un estimateur de régression linéaire. (La régression linéaire tente de tracer une ligne droite de meilleur ajustement à travers notre jeu de données.) Le modèle est capable d'obtenir les données de régression grâce à la fonction fit. Je peux utiliser le modèle en passant un ensemble fictif de caractéristiques à travers la fonction predict. L'exemple ci-dessous montre les caractéristiques pour un vin fictif. Le modèle renverra une réponse basée sur son entraînement.

Le code pour ce modèle et ce vin fictif est ci-dessous :

### Importer et exporter notre modèle Python

La bibliothèque [pickle](https://docs.python.org/2/library/pickle.html) facilite la sérialisation des modèles dans des fichiers que je crée. Je peux également recharger le modèle dans mon code. Cela me permet de garder mon code d'entraînement de modèle séparé du code qui déploie mon modèle.

Je peux importer ou exporter mon modèle Python pour l'utiliser dans d'autres scripts Python avec le code ci-dessous :

### Créer un serveur web simple

![Image](https://cdn-media-1.freecodecamp.org/images/1*wv3umUu_u8r7dgeXHX38uw.png)
_Flask, le framework que nous utiliserons pour créer un serveur web._

Pour déployer mon modèle, je dois d'abord créer un serveur. Les serveurs écoutent le trafic web et exécutent des fonctions lorsqu'ils trouvent une requête qui leur est adressée. La fonction qui s'exécute peut dépendre de la route de la requête et d'autres données qu'elle contient. Ensuite, le serveur peut envoyer un message de confirmation au demandeur.

Le framework Python [Flask](http://flask.pocoo.org/) me permet de créer des serveurs web en un temps record.

Dans le code ci-dessous, j'utilise Flask pour exécuter un serveur web simple à une seule route. Ma seule route écoute les requêtes POST et envoie un bonjour en retour. Les requêtes POST sont un type spécial de requête qui transporte des données dans un objet JSON.

### Ajouter le modèle à mon serveur

Avec la bibliothèque pickle, je peux charger notre modèle entraîné dans mon serveur web.

Notre serveur charge maintenant le modèle entraîné lors de son initialisation. Je peux y accéder en envoyant une requête POST à ma route "/echo". La route récupère un tableau de caractéristiques dans le corps de la requête et le donne au modèle. La prédiction du modèle est ensuite renvoyée au demandeur.

### Conclusion

Après avoir lu cet article, vous devriez être capable de créer votre propre backend de machine learning. Pour plus de détails, vous pouvez trouver un exemple complet que j'ai réalisé dans [ce dépôt](https://github.com/iYung/sklearn-flask-example).

Lorsque vous aurez le temps, je vous recommande de faire une pause dans le codage et de lire sur le machine learning. Cet article n'enseigne que les bases nécessaires pour créer un modèle. Il y a des sujets comme la réduction des pertes et les réseaux de neurones que vous devez connaître.

Bonne chance et bon codage !