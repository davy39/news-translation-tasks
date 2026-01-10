---
title: Principes de l'Apprentissage Automatique Expliqués
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/machine-learning-principles-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d25740569d1a4ca362a.jpg
tags:
- name: Machine Learning
  slug: machine-learning
- name: toothbrush
  slug: toothbrush
seo_title: Principes de l'Apprentissage Automatique Expliqués
seo_desc: 'Learning is the Result of Representation, Evaluation, and Optimization

  The field of machine learning has exploded in recent years and researchers have
  developed an enormous number of algorithms to choose from. Despite this great variety
  of models to ...'
---

## **L'apprentissage est le résultat de la représentation, de l'évaluation et de l'optimisation**

Le domaine de l'apprentissage automatique a explosé ces dernières années et les chercheurs ont développé un nombre énorme d'algorithmes parmi lesquels choisir. Malgré cette grande variété de modèles disponibles, ils peuvent tous être distillés en trois composants.

Les trois composants qui constituent un modèle d'apprentissage automatique sont la représentation, l'évaluation et l'optimisation. Ces trois éléments sont principalement liés à l'apprentissage supervisé, mais ils peuvent également être liés à l'apprentissage non supervisé.

**Représentation** - cela décrit comment vous souhaitez examiner vos données. Parfois, vous pouvez vouloir penser à vos données en termes d'individus (comme dans les k-plus proches voisins) ou comme dans un graphe (comme dans les réseaux bayésiens).

**Évaluation** - à des fins d'apprentissage supervisé, vous devrez évaluer ou mettre un score sur la performance de votre apprenant afin qu'il puisse s'améliorer. Cette évaluation est effectuée à l'aide d'une fonction d'évaluation (également connue sous le nom de fonction objective ou fonction de score). Des exemples incluent la précision et l'erreur quadratique.

**Optimisation** - en utilisant la fonction d'évaluation ci-dessus, vous devez trouver l'apprenant avec le meilleur score à partir de cette fonction d'évaluation en utilisant une technique d'optimisation. Des exemples sont une recherche gloutonne et la descente de gradient.

## **La généralisation est essentielle**

La puissance de l'apprentissage automatique vient du fait de ne pas avoir à coder en dur ou à définir explicitement les paramètres qui décrivent vos données d'entraînement et les données invisibles. C'est l'objectif essentiel de l'apprentissage automatique : généraliser les résultats d'un apprenant.

Pour tester la généralisabilité d'un apprenant, vous voudrez avoir un ensemble de données de test séparé qui n'est pas utilisé de quelque manière que ce soit dans l'entraînement de l'apprenant. Cela peut être créé soit en divisant l'ensemble de vos données d'entraînement en un ensemble d'entraînement et un ensemble de test, soit en collectant simplement plus de données. Si l'apprenant devait utiliser des données trouvées dans l'ensemble de données de test, cela créerait une sorte de biais dans votre apprenant pour mieux performer que dans la réalité.

Une méthode pour avoir une idée de la performance de votre apprenant sur un ensemble de données de test est d'effectuer ce qu'on appelle la **validation croisée**. Cela divise aléatoirement vos données d'entraînement en un nombre donné de sous-ensembles (par exemple, dix sous-ensembles) et laisse un sous-ensemble de côté pendant que l'apprenant s'entraîne sur le reste. Et une fois que l'apprenant a été formé, l'ensemble de données laissé de côté est utilisé pour les tests. Cet entraînement, en laissant un sous-ensemble de côté, et les tests sont répétés à mesure que vous faites tourner les sous-ensembles.

## **Attention au surapprentissage**

Si un algorithme d'apprentissage s'adapte bien à un ensemble d'entraînement donné, cela n'indique pas simplement une bonne hypothèse. Le surapprentissage se produit lorsque la fonction d'hypothèse J(Θ) s'adapte trop étroitement à votre ensemble d'entraînement, ayant une variance élevée et une faible erreur sur l'ensemble d'entraînement tout en ayant une erreur de test élevée sur toute autre donnée.

En d'autres termes, le surapprentissage se produit si l'erreur de l'hypothèse, telle que mesurée sur l'ensemble de données qui a été utilisé pour entraîner les paramètres, se trouve être inférieure à l'erreur sur tout autre ensemble de données.

### **Choisir un degré de polynôme optimal**

Choisir le bon degré de polynôme pour la fonction d'hypothèse est important pour éviter le surapprentissage. Cela peut être réalisé en testant chaque degré de polynôme et en observant l'effet sur le résultat de l'erreur sur diverses parties de l'ensemble de données. Ainsi, nous pouvons diviser notre ensemble de données en 3 parties qui peuvent être utilisées pour optimiser le theta de l'hypothèse et le degré du polynôme.

Un bon ratio de division de l'ensemble de données est :

* Ensemble d'entraînement : 60%
* Validation croisée : 20%
* Ensemble de test : 20%

Les trois valeurs d'erreur peuvent ainsi être calculées par la méthode suivante :

1. Utiliser l'ensemble d'entraînement pour chaque degré de polynôme afin d'optimiser les paramètres dans `Θ`
2. Utiliser l'ensemble de validation croisée pour trouver le degré de polynôme avec l'erreur la plus faible
3. Utiliser l'ensemble de test pour estimer l'erreur de généralisation

### **Façons de corriger le surapprentissage**

Voici quelques-unes des façons de remédier au surapprentissage :

1. Obtenir plus d'exemples d'entraînement
2. Essayer un ensemble plus petit de caractéristiques
3. Augmenter le paramètre `λ lambda`