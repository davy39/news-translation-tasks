---
title: Comment fonctionne le Bag of Words – Le fondement des modèles de langage
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2025-08-25T13:18:00.063Z'
originalURL: https://freecodecamp.org/news/how-bag-of-words-works
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1756127722792/e047e9d2-91ae-42f6-85d9-106260ddf432.png
tags:
- name: AI
  slug: ai
- name: Machine Learning
  slug: machine-learning
seo_title: Comment fonctionne le Bag of Words – Le fondement des modèles de langage
seo_desc: 'When people talk about modern AI, they often point to large language models
  like ChatGPT.

  These models seem smart, as they’re able to write, answer, and explain in natural
  language.

  But the roots of this technology go back to something very simple: t...'
---

Quand on parle d'IA moderne, on évoque souvent les grands modèles de langage comme ChatGPT.

Ces modèles semblent intelligents, car ils sont capables d'écrire, de répondre et d'expliquer en langage naturel.

Mais les racines de cette technologie remontent à quelque chose de très simple : le modèle Bag of Words (Sac de mots). Cette méthode, apparue il y a plusieurs décennies, a été l'un des premiers moyens de transformer du texte en nombres. Sans elle, les progrès que nous voyons aujourd'hui dans le traitement du langage naturel n'auraient pas été possibles.

Dans cet article, vous apprendrez ce qu'est l'algorithme Bag of Words et vous écrirez votre propre code pour créer une fonction afin de générer un sac de mots.

## Qu'est-ce que le Bag of Words ?

Le Bag of Words, souvent appelé BoW, est une méthode de [représentation de texte](https://www.freecodecamp.org/news/how-computers-understand-language/). Il prend une phrase, un paragraphe ou un document et le traite comme un « sac » de mots.

L'ordre des mots, la grammaire et la structure des phrases sont ignorés. Seule la présence ou la fréquence de chaque mot compte.

Prenez la phrase

```typescript
The cat sat on the mat.
```

Dans le Bag of Words, cela devient un décompte de mots.

```typescript
the:2, cat:1, sat:1, on:1, mat:1.
```

Une autre phrase comme celle-ci :

```typescript
The mat sat on the cat
```

ressemble à la précédente, même si le sens est différent.

C'est à la fois la force et la faiblesse du BoW. Cela rend le texte facile à traiter pour les ordinateurs mais fait l'impasse sur le contexte.

## Pourquoi le BoW a été une avancée majeure

Avant le Bag of Words, les ordinateurs n'avaient aucun moyen simple de gérer le langage humain. Les mots ne sont pas des nombres, et les algorithmes ont besoin de nombres pour fonctionner.

Le BoW a donné aux chercheurs un moyen de transformer des textes désordonnés en vecteurs de fréquences. Une fois sous forme numérique, les mots pouvaient être utilisés dans les statistiques, le clustering et le machine learning.

Les premières applications incluaient les filtres anti-spam, où certains mots comme « free » ou « win » signalaient des e-mails indésirables. Les moteurs de recherche l'utilisaient également pour faire correspondre les requêtes aux documents. Pour la première fois, le texte pouvait être traité à grande échelle.

## Un exemple simple de Bag of Words en Python

Voici un court exemple pour voir le Bag of Words en action. Nous allons prendre quelques phrases et les convertir en vecteurs de décompte de mots.

```typescript
from sklearn.feature_extraction.text import CountVectorizer
```

```typescript
docs = [
    "the cat sat on the mat",
    "the dog barked at the cat",
    "the mat was sat on by the cat"
]
```

```typescript
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(docs)
```

```typescript
print("Vocabulary:", vectorizer.get_feature_names_out())
print("Document-Term Matrix:\n", X.toarray())
```

Cela vous donnera le résultat suivant :

![Bag of Words](https://cdn.hashnode.com/res/hashnode/image/upload/v1755688011426/6e4e87bc-9f0e-4be4-a429-19a8ade70997.png align="center")

Ce que vous voyez dans le résultat, c'est le modèle Bag of Words transformant vos phrases en nombres. La première ligne montre le vocabulaire, qui est la collection de chaque mot unique apparu dans les trois phrases d'entrée.

Des mots comme « at », « barked », « cat », « dog », « mat », « on », « sat », « the » et « was » font tous partie de ce dictionnaire. Chaque position dans le vocabulaire a un ordre fixe, et cet ordre est utilisé pour mapper les mots aux colonnes de la matrice.

La deuxième partie du résultat est la matrice document-terme. Chaque ligne de cette matrice représente un document, et chaque nombre dans la ligne vous indique combien de fois le mot du vocabulaire est apparu dans ce document.

Par exemple, dans la première ligne, qui correspond à la phrase « the cat sat on the mat », les valeurs s'alignent avec le vocabulaire pour montrer que « the » est apparu deux fois, tandis que « cat », « sat », « on » et « mat » sont apparus une fois chacun. Tout autre mot du vocabulaire pour cette ligne est un zéro, ce qui signifie qu'il n'est jamais apparu dans ce document.

C'est l'essence même du Bag of Words. Il réduit chaque phrase à une ligne de nombres, où le sens et la grammaire sont ignorés, et seuls les décomptes de mots sont conservés. Au lieu de travailler avec du texte brut, la machine travaille désormais avec un tableau structuré de nombres.

Cette idée simple est ce qui a permis aux ordinateurs de commencer à analyser et à apprendre à partir du langage.

## Les limites du Bag of Words

Même s'il a été utile, le Bag of Words a ses limites.

La plus évidente est qu'il ignore le sens. Des phrases avec des rôles inversés (« dog chases cat » vs « cat chases dog ») se retrouvent avec le même vecteur.

Le BoW ne gère pas non plus bien les synonymes. Des mots comme « happy » et « joyful » sont traités comme différents, même s'ils signifient la même chose.

Un autre problème est la taille. Si le jeu de données contient des milliers de mots uniques, les vecteurs deviennent très grands et creux. Most values are zeros, ce qui rend le stockage et le calcul moins efficaces.

### Du Bag of Words vers de meilleurs modèles

Le Bag of Words a inspiré de meilleures méthodes. Une amélioration a été le [TF-IDF](https://www.geeksforgeeks.org/machine-learning/understanding-tf-idf-term-frequency-inverse-document-frequency/), qui donne un poids plus élevé aux mots rares mais importants, et un poids plus faible aux mots courants comme « the ».

Plus tard sont arrivés les [word embeddings](https://www.turingtalks.ai/p/understanding-word-embeddings-the-building-blocks-of-nlp-and-gpts) tels que Word2Vec et GloVe. Au lieu de compter les mots, les embeddings les mappent dans des vecteurs denses où les significations et les relations sont capturées. Des mots comme « king » et « queen » se retrouvent proches l'un de l'autre dans cet espace.

Les transformeurs modernes, comme BERT et GPT, poussent cela encore plus loin. Ils capturent non seulement le sens du mot mais aussi son contexte. Le mot « bank » dans « river bank » et « money bank » aura des embeddings différents selon la phrase. C'est quelque chose que le Bag of Words ne pourrait jamais faire.

### Pourquoi le Bag of Words compte encore

Même aujourd'hui, le Bag of Words n'est pas inutile. Pour de petits projets avec des données limitées, il peut toujours fournir des résultats solides.

Un classificateur de texte rapide utilisant le BoW fonctionne souvent plus vite et nécessite moins de puissance de calcul que l'entraînement d'un réseau de neurones profonds. Dans l'enseignement, il est également précieux car il montre la première étape de la transformation d'un texte brut en une forme lisible par machine.

Plus important encore, l'idée centrale du Bag of Words perdure. Les grands modèles de langage convertissent toujours le texte en vecteurs. La différence est qu'ils le font d'une manière beaucoup plus complexe et significative.

Le Bag of Words a été l'étincelle qui a fait réaliser aux chercheurs que : pour traiter le langage, nous devons d'abord le représenter sous forme de nombres.

## Conclusion

Le Bag of Words semble simple, peut-être même primitif par rapport aux outils que nous utilisons maintenant. Mais ce fut un tournant. Il a donné aux ordinateurs un moyen de voir le texte comme de la donnée, et il a jeté les bases de tout ce qui a suivi. Bien qu'il ne puisse pas capturer le sens profond ou le contexte, il nous a appris à combler le fossé entre les mots et les nombres.

Les grands modèles de langage peuvent sembler magiques, mais leurs racines remontent au Bag of Words. Le voyage du décompte des mots dans une phrase aux transformeurs avec des milliards de paramètres est la preuve que les grandes révolutions technologiques commencent souvent par des idées simples et modestes.

*J'espère que vous avez apprécié cet article. Inscrivez-vous à ma newsletter gratuite sur l'IA* [***TuringTalks.ai***](https://www.turingtalks.ai/) *pour plus de tutoriels pratiques sur l'IA. Vous pouvez également me retrouver sur* [***Linkedin***](https://www.linkedin.com/in/manishmshiva)***.***