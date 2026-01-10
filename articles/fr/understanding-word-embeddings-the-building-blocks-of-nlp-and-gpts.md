---
title: 'Comprendre les plongements de mots : les éléments de base du TAL et des GPT'
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2023-09-24T12:17:31.000Z'
originalURL: https://freecodecamp.org/news/understanding-word-embeddings-the-building-blocks-of-nlp-and-gpts
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/nlp1.png
tags:
- name: natural language processing
  slug: natural-language-processing
seo_title: 'Comprendre les plongements de mots : les éléments de base du TAL et des
  GPT'
seo_desc: 'Word embeddings serve as the foundation for many applications, from simple
  text classification to complex machine translation systems. But what exactly are
  word embeddings, and how do they work? Let''s find out.

  What Are Word Embeddings?

  Word embeddin...'
---

Les plongements de mots servent de fondation pour de nombreuses applications, allant de la classification de texte simple aux systèmes complexes de traduction automatique. Mais qu'est-ce que les plongements de mots exactement, et comment fonctionnent-ils ? Découvrons-le.

## Qu'est-ce que les plongements de mots ?

Les plongements de mots servent d'ADN numérique pour les mots dans le monde du traitement automatique du langage naturel (TAL). En essence, les plongements de mots convertissent les mots en vecteurs numériques (un terme sophistiqué pour des tableaux de nombres). Ces vecteurs peuvent être traités par des algorithmes d'apprentissage automatique.

Pensez à ces vecteurs comme une empreinte numérique pour chaque mot. Par exemple, le mot « pomme » pourrait être représenté par un vecteur numérique comme [0.2, -0.4, 0.7].

L'avantage principal des plongements de mots est leur capacité à capturer l'essence sémantique des mots. En termes plus simples, ils aident les machines à comprendre le sens et les nuances derrière chaque mot.

Par exemple, si « pomme » est proche de « fruit » dans cet espace numérique mais loin de « voiture », la machine comprend qu'une pomme est plus liée aux fruits qu'aux véhicules.

Au-delà de la signification individuelle, les plongements de mots encodent également les relations entre les mots. Les mots qui apparaissent souvent ensemble dans le même contexte auront des vecteurs similaires ou « plus proches ».

![Image](https://www.freecodecamp.org/news/content/images/2023/09/Screenshot-2023-09-24-at-5.43.04-PM.png)
_Plongements de mots_

Par exemple, dans l'espace numérique, les vecteurs représentant « roi » et « reine » pourraient être plus proches l'un de l'autre que ceux représentant « roi » et « pomme ». Cela est dû au fait que l'algorithme a appris à partir de nombreux textes que « roi » et « reine » apparaissent souvent dans des contextes similaires, comme des discussions sur la royauté, tandis que « roi » et « pomme » ne le font pas.

## Pourquoi avons-nous besoin des plongements de mots ?

Les modèles de langage traditionnels traitaient les mots comme des entités séparées et isolées.

Par exemple, le mot « chien » pourrait être représenté comme un identifiant unique, disons 1, tandis que le mot « chat » comme 2. Cette approche ne parvient pas à capturer la relation entre « chien » et « chat », qui sont tous deux des animaux et des animaux de compagnie.

Les plongements de mots résolvent ce problème en plaçant les mots avec des significations ou des contextes similaires à proximité les uns des autres dans un espace multidimensionnel.

## Algorithmes pour générer des plongements

### Word2Vec

Des chercheurs chez Google ont développé Word2Vec, qui utilise des réseaux de neurones pour générer des plongements de mots. Le modèle traite un grand corpus de texte et produit des vecteurs de mots de haute qualité.

Il détermine ces plongements en analysant le contexte dans lequel les mots apparaissent, basé sur l'idée que les mots trouvés dans des contextes similaires partagent probablement une signification sémantique.

### GloVe (Global Vectors for Word Representation)

Des chercheurs de Stanford ont développé GloVe, qui construit une grande table pour surveiller la fréquence à laquelle les mots co-occurrent dans un ensemble de données textuelles. Le modèle utilise ensuite des méthodes mathématiques pour simplifier cette table, générant des vecteurs numériques pour des mots individuels.

Ces vecteurs encapsulent à la fois la signification et les relations entre les mots, posant les bases pour diverses tâches d'apprentissage automatique liées au langage.

### FastText

Le laboratoire de recherche en IA de Facebook a créé FastText, qui améliore le modèle Word2Vec en considérant les mots comme des assemblages de plus petites chaînes de caractères, ou n-grammes de caractères.

Cette méthode permet au modèle de capturer plus efficacement les intricacies des langues ayant des structures de mots complexes et d'incorporer des mots non présents dans les données d'entraînement originales. Par conséquent, FastText produit un modèle de langage plus adaptable et complet, utile pour un ensemble diversifié de tâches d'apprentissage automatique.

## Plongements de mots et GPT

![Image](https://www.freecodecamp.org/news/content/images/2023/09/gpt.gif)
_Plongements de mots et GPT_

Les plongements de mots sont un composant fondamental dans les modèles GPT comme GPT-2, GPT-3 et GPT-4. Cependant, l'architecture et l'approche sont un peu plus avancées par rapport aux modèles plus simples qui reposent uniquement sur les plongements de mots.

Dans les modèles traditionnels qui utilisent des plongements de mots comme Word2Vec ou GloVe, chaque mot est converti en un vecteur fixe dans un espace prédéfini. Ces vecteurs sont ensuite utilisés comme entrée pour d'autres algorithmes d'apprentissage automatique pour des tâches comme la classification, le clustering, ou même dans des modèles séquence-à-séquence pour la traduction automatique.

En revanche, les modèles GPT utilisent une variante connue sous le nom de « plongements de transformateurs », qui non seulement plongent les mots individuels mais considèrent également le contexte dans lequel un mot apparaît.

Cela est essentiel pour comprendre le sens des mots qui peuvent changer en fonction des mots qui les entourent. Par exemple, le mot « banque » pourrait signifier une institution financière ou le bord d'une rivière, selon le contexte.

L'architecture GPT prend une séquence de mots (ou plus précisément, de tokens) comme entrée et les traite à travers plusieurs couches de blocs de transformateurs. Ces blocs produisent une nouvelle séquence de vecteurs qui représentent non seulement les mots individuels, mais aussi leurs relations avec tous les autres mots dans la séquence d'entrée.

Cette séquence est ensuite utilisée pour des tâches de TAL, allant de la complétion de texte à la traduction et au résumé.

Ainsi, bien que les modèles GPT utilisent des plongements, ils sont bien plus dynamiques et sensibles au contexte que les plongements de mots traditionnels. Les plongements dans les modèles GPT font partie d'un système plus large et plus complexe conçu pour comprendre et générer du texte semblable à celui des humains en fonction de l'entrée qu'il reçoit.

## Conclusion

Les plongements de mots offrent un moyen efficace et computationnellement efficient de représenter les mots sous forme de vecteurs, capturant les intricacies du langage dans une forme que les machines peuvent comprendre. Ils sont au cœur de nombreuses applications de TAL, améliorant la précision et la sophistication des modèles de langage.

À mesure que la technologie continue d'évoluer, les méthodes de génération et d'utilisation des plongements de mots évolueront également, promettant des capacités de traitement du langage encore plus robustes et nuancées dans les années à venir.

_Si vous avez trouvé cet article intéressant, [rejoignez ma newsletter](https://manishmshiva.com/) et je vous enverrai un email avec mon contenu chaque vendredi._