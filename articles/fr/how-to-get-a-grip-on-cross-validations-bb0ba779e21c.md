---
title: Comment maîtriser la validation croisée en apprentissage automatique
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-17T21:00:34.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-a-grip-on-cross-validations-bb0ba779e21c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_gg1Te-7SJfk9E2D-mORfw.png
tags:
- name: AI
  slug: ai
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment maîtriser la validation croisée en apprentissage automatique
seo_desc: 'By Shruti Tanwar

  Lately, I’ve had the chance to be involved in building a product that aims at accelerating
  ML/AI (Machine Learning / Artificial Intelligence) adoption for businesses. In the
  process of developing such an exciting product, I learned a...'
---

Par Shruti Tanwar

Récemment, j'ai eu l'opportunité de participer à la création d'un produit visant à accélérer l'adoption de l'IA/ML (Intelligence Artificielle / Apprentissage Automatique) pour les entreprises. Au cours du développement de ce produit passionnant, j'ai appris une ou deux choses en chemin.

Et bien que l'IA/ML soit un domaine trop vaste pour être couvert dans un seul article, je saisis cette occasion pour mettre en lumière l'un des concepts qui vous aidera à construire un modèle prédictif résilient. Un modèle capable de performer de manière fiable dans le monde réel et de se comporter de manière "équitable" sur des données invisibles.

Vous ne pouvez jamais être sûr à 100 % du comportement de votre modèle d'apprentissage automatique. Il y a toujours place à l'amélioration, au progrès ou à un certain ajustement 💡. Se contenter d'ajuster le modèle à vos données d'entraînement et espérer qu'il performe avec précision dans le monde réel serait un mauvais choix. Certains facteurs qui peuvent garantir ou au moins assurer une performance raisonnable doivent être considérés avant de déployer le modèle en production.

Vous devez vous assurer que votre modèle comprend les différents motifs dans vos données — qu'il n'est pas sous-ajusté ou sur-ajusté — et que le biais et la variance du modèle sont faibles.

La « **Validation Croisée** » ✅ est la technique qui vous aide à valider la performance de votre modèle. C'est une méthode statistique utilisée pour estimer la compétence des modèles d'apprentissage automatique. Voici une définition pour vous :

> La **[validation croisée](https://en.wikipedia.org/wiki/Cross-validation_(statistics))**, parfois appelée **estimation par rotation** ou **test hors échantillon**, est l'une des diverses techniques similaires de [validation de modèle](https://en.wikipedia.org/wiki/Model_validation) pour évaluer comment les résultats d'une analyse [statistique](https://en.wikipedia.org/wiki/Statistics) se généraliseront à un ensemble de données indépendant. Elle est principalement utilisée dans des contextes où l'objectif est la prédiction, et où l'on souhaite estimer avec quelle [précision](https://en.wikipedia.org/wiki/Accuracy) un [modèle prédictif](https://en.wikipedia.org/wiki/Predictive_modelling) performera en pratique.

En termes extrêmement simples, la mise en œuvre pratique du jargon ci-dessus serait la suivante :

Lors de l'entraînement d'un modèle, une partie des données est retirée avant le début de l'entraînement.   
Une fois l'entraînement terminé, les données qui ont été retirées sont utilisées pour tester la performance du modèle appris et ajuster les paramètres afin d'améliorer la performance finale du modèle.

C'est l'idée fondamentale pour toute la gamme de méthodes d'évaluation appelées _validation croisée_.

![Image](https://cdn-media-1.freecodecamp.org/images/augTyKVuV5uvIJKNnqUf3oR1K5n7E8DaqirO)
_Cycle de vie de la validation et de l'ajustement du modèle._

Avant de discuter des techniques de validation, examinons rapidement deux termes utilisés ci-dessus : sur-ajustement et sous-ajustement. Qu'est-ce exactement que le sous-ajustement et le sur-ajustement des modèles et comment cela affecte-t-il la performance d'un modèle avec des données réelles ?

Nous pouvons le comprendre facilement à travers le graphique suivant.

![Image](https://cdn-media-1.freecodecamp.org/images/hW2fMyk1PB4dhjyv9TzSj4Yt4K5bkJoUj284)

Un modèle est dit **sous-ajusté** (biais élevé) lorsqu'il performe mal sur les données d'entraînement. Comme nous pouvons le voir sur le graphique de gauche, la ligne ne couvre pas la plupart des points de données sur le graphique, ce qui signifie qu'elle n'a pas pu capturer la relation entre l'entrée (disons `X`) et la sortie à prédire (disons `Y`).

Un modèle **sur-ajusté** (variance élevée), en revanche, performe bien sur les données d'entraînement mais ne performe pas bien sur les données d'évaluation. Dans un tel cas, le modèle mémorise les données qu'il a vues au lieu d'apprendre et n'est pas capable de généraliser à des données invisibles.

Le graphique de droite représente le cas du sur-ajustement. Nous voyons que la ligne prédite couvre tous les points de données du graphique. Bien que cela puisse sembler indiquer que le modèle devrait fonctionner encore mieux, malheureusement, cela est loin de la vérité pratique. La ligne prédite couvrant tous les points, y compris le bruit et les valeurs aberrantes, produit des résultats médiocres en raison de sa complexité.

Passons maintenant aux différents types de techniques de validation croisée.

#### **Méthode de retenue (Holdout Method)**

Le type le plus simple de validation croisée. Ici, l'ensemble de données est séparé en deux ensembles, appelés ensemble d'entraînement et ensemble de test. Le modèle est ajusté uniquement sur l'ensemble d'entraînement. Ensuite, les prédictions sont faites pour les données de l'ensemble de test (que le modèle n'a jamais vues auparavant). Les erreurs qu'il commet sont agrégées pour donner l'erreur moyenne absolue de l'ensemble de test, qui est utilisée pour évaluer le modèle.

![Image](https://cdn-media-1.freecodecamp.org/images/-r5fjgSUHFROLDzfsbmMmToDXFusQ3hESc1W)
_Validation croisée par retenue_

Ce type d'évaluation dépend dans une certaine mesure des points de données qui se retrouvent dans l'ensemble d'entraînement et de ceux qui se retrouvent dans l'ensemble de test, et peut donc affecter l'évaluation en fonction de la manière dont la division est faite.

#### **Validation croisée K-fold (K-fold cross-validation)**

L'une des techniques de validation les plus populaires est la validation croisée K-fold. Cela est dû à sa simplicité qui produit généralement une estimation moins biaisée ou moins optimiste de la compétence du modèle que d'autres méthodes, telles qu'une simple division entraînement/test.

Ici, l'ensemble de données est divisé en `k` sous-ensembles, et la méthode de retenue est répétée `k` fois. Chaque fois, l'un des `k` sous-ensembles est utilisé comme ensemble de test et les autres `k-1` sous-ensembles constituent l'ensemble d'entraînement. Ensuite, l'erreur moyenne est calculée sur tous les `k` essais.

La procédure générale est la suivante :

1. Mélanger aléatoirement l'ensemble de données et le diviser en `k` groupes
2. Prendre un groupe comme ensemble de retenue ou de test et les groupes restants comme ensemble de données d'entraînement.
3. Ajuster un modèle sur l'ensemble d'entraînement et l'évaluer sur l'ensemble de test.
4. Conserver le score d'évaluation et jeter le modèle.
5. Résumer la compétence du modèle en utilisant l'échantillon des scores d'évaluation du modèle.

![Image](https://cdn-media-1.freecodecamp.org/images/mXGtXkZXwGrF4FsktIsKTftJyfZDILM4xpHD)
_Validation croisée K-fold_

L'avantage de cette méthode sur les autres est qu'il importe peu de la manière dont les données sont divisées. Chaque point de données se retrouvera dans un ensemble de test exactement une fois et se retrouvera dans l'ensemble d'entraînement exactement `k-1` fois. À mesure que `k` augmente, nous observons une diminution de la variance de l'estimation résultante.

Un inconvénient de cette méthode peut être le calcul requis pendant l'entraînement. L'algorithme d'entraînement doit être relancé à partir de zéro `k` fois, ce qui signifie qu'il faut `k` fois plus de calcul pour faire une évaluation.

#### **Validation croisée leave-one-out (Leave-one-out cross-validation)**

Leave-one-out est une sorte de cousine de la validation croisée K-fold où `k` devient égal à `n`, le nombre total de points de données dans l'ensemble. C'est essentiellement une version extrême logique de la validation K-fold. Comment cela fonctionne en pratique est en laissant exactement un point de données à chaque itération et en utilisant ce point de données pour faire la prédiction.

L'approximateur de fonction est entraîné sur toutes les données, exactement `n` fois, sauf pour un point et une prédiction est faite pour ce point. Comme avant, l'erreur moyenne est calculée et utilisée pour évaluer le modèle.

Nous y voilà et appelons cela une conclusion. J'espère que vous avez apprécié la lecture autant que j'ai apprécié la création. ❤️ Faites-moi savoir vos pensées ?, commentaires ? ou conseils ? dans les commentaires ci-dessous.  
Et pendant que vous y êtes, pourquoi ne pas aller voir ce que je construis avec mon équipe, chez [skyl.ai](https://skyl.ai/) et engager une conversation avec moi ou partager vos commentaires. Santé.