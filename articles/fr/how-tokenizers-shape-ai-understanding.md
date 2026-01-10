---
title: Explication des Tokenizers – Comment les Tokenizers aident l'IA à comprendre
  le langage
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2024-03-27T11:35:07.000Z'
originalURL: https://freecodecamp.org/news/how-tokenizers-shape-ai-understanding
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/ab427b80-a502-11ea-8467-694f4e40dfa7.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: 'LLM''s '
  slug: llms
- name: natural language processing
  slug: natural-language-processing
seo_title: Explication des Tokenizers – Comment les Tokenizers aident l'IA à comprendre
  le langage
seo_desc: 'Tokenizers are the fundamental tools that enable artificial intelligence
  to dissect and interpret human language. Let’s look at how tokenizers help AI systems
  comprehend and process language.

  In the fast-evolving world of natural language processing ...'
---

Les tokenizers sont les outils fondamentaux qui permettent à l'intelligence artificielle de disséquer et d'interpréter le langage humain. Examinons comment les tokenizers aident les systèmes d'IA à comprendre et à traiter le langage.

Dans le monde en rapide évolution du traitement automatique du langage naturel (NLP), les tokenizers jouent un rôle pivot.

Les tokenizers sont les héros méconnus qui, en coulisses, donnent un sens au langage humain pour que les machines puissent le comprendre.

Plongeons-nous dans ce que sont les tokenizers et explorons leurs cas d'utilisation. Nous vous présenterons également Huggingface, une plateforme de premier plan dans le domaine de l'IA et du NLP.

Nous vous guiderons également à travers un exemple de code simple utilisant la bibliothèque de tokenizers de Huggingface.

## Qu'est-ce que les Tokenizers ?

Imaginez que vous essayez d'enseigner à un robot à comprendre et à parler des langues humaines. Le premier défi auquel vous seriez confronté est de savoir comment décomposer le langage en morceaux que le robot peut assimiler. C'est là que les tokenizers interviennent.

Les tokenizers décomposent le langage complexe en morceaux gérables, transformant le texte brut en une forme structurée que les modèles d'IA peuvent facilement traiter. Cette étape, en apparence simple, est cruciale, permettant aux machines de saisir les nuances de la communication humaine.

Pensez aux tokenizers comme aux chefs qui hachent les ingrédients avant qu'un repas ne soit cuisiné. Sans cette étape, la préparation de plats complexes (ou la compréhension de phrases complexes) serait beaucoup plus difficile.

Grâce à la tokenisation, les systèmes d'IA peuvent reconnaître des motifs, comprendre le contexte et générer des réponses de plus en plus similaires à l'interaction humaine.

En décomposant les complexités du langage en morceaux digestes, les tokenizers non seulement améliorent les capacités linguistiques de l'IA, mais ouvrent également la voie à des modèles d'apprentissage automatique plus intuitifs, efficaces et précis.

## Qu'est-ce que les Tokenizers de Huggingface ?

[Huggingface](https://huggingface.co/) est une entreprise à la pointe de l'IA et du NLP.

Ils sont surtout connus pour leur bibliothèque Transformers, qui a facilité l'accès à des modèles NLP de pointe.

Au cœur de leurs innovations se trouve la bibliothèque de tokenizers, un outil puissant conçu pour convertir le texte en un format que les modèles d'IA peuvent comprendre. Cette bibliothèque est essentielle pour les développeurs et les chercheurs travaillant sur des projets d'IA.

Les tokenizers de Hugging Face ne sont pas seulement efficaces et rapides, mais ils supportent également une large gamme de langues, ce qui en fait des outils polyvalents pour des tâches NLP mondiales. Ils sont optimisés pour la performance, garantissant qu'ils peuvent gérer de grands volumes de texte sans compromettre la vitesse ou la précision.

Ce qui distingue les tokenizers de Hugging Face, c'est leur intégration avec la bibliothèque Transformers, une autre pierre angulaire de l'écosystème IA de Hugging Face.

Cette intégration permet un traitement transparent des données textuelles, les préparant pour des tâches complexes comme la traduction, la synthèse et l'analyse de sentiments.

La bibliothèque de tokenizers est continuellement mise à jour, incorporant les dernières découvertes de la recherche et les retours de la communauté pour améliorer ses capacités.

## Exemple de code simple de la bibliothèque de Tokenizers de Huggingface

Mettons-nous au travail avec un peu de code. Nous allons utiliser la bibliothèque de tokenizers de Huggingface pour tokenizer une phrase simple.

Tout d'abord, installons la bibliothèque Transformers de Huggingface. (Utilisez ! avant la commande si vous l'installez dans un [Google Collab notebook](https://colab.research.google.com/)).

```
pip install transformers
```

Tout d'abord, importons la classe `AutoTokenizer` de la bibliothèque Transformers. `AutoTokenizer` est une classe d'usine qui peut automatiquement charger le tokenizer correspondant à un modèle pré-entraîné que nous spécifions (dans ce cas, le modèle [bert-base-uncased](https://huggingface.co/google-bert/bert-base-uncased)).

```
from transformers import AutoTokenizer
```

Ensuite, nous créons une instance de la classe `AutoTokenizer` en appelant la méthode `from_pretrained`. Ce tokenizer est conçu pour fonctionner avec le modèle BERT et est configuré pour ne pas différencier les lettres majuscules et minuscules (d'où 'uncased').

```
tokenizer=AutoTokenizer.from_pretrained("bert-base-uncased")
```

Déclarons maintenant une chaîne de caractères pour la tokenisation.

```
text = "Hello, and welcome to the world of Tokenizers"
```

Utilisons la méthode `tokenize` du tokenizer avec le texte d'exemple comme argument.

```
tokens = tokenizer.tokenize(text)
```

La méthode `tokenize` divise le texte d'entrée en une liste de tokens ou de mots/sous-mots sur lesquels le modèle pré-entraîné a été formé. Pour des modèles comme BERT, les mots peuvent être divisés en unités plus petites (sous-mots ou caractères) pour gérer plus efficacement les mots hors vocabulaire.

Nous allons également convertir la liste de tokens en une liste d'entiers (IDs de tokens). Chaque entier correspond à un token spécifique dans le vocabulaire du tokenizer.

Cette conversion est nécessaire car les modèles d'apprentissage automatique ne comprennent pas directement le texte ; ils fonctionnent avec des données numériques.

```
token_ids = tokenizer.convert_tokens_to_ids(tokens)
```

Nous avons terminé. Affichons à la fois les tokens et leurs IDs correspondants.

```
print("Tokens:", tokens)
print("Token IDs:", token_ids)
```

Ce morceau de code charge donc un tokenizer pré-entraîné pour le modèle BERT, tokenize une phrase d'exemple et convertit ces tokens en leurs IDs correspondants. Ces IDs sont ce que les modèles d'apprentissage automatique traitent.

Voici la réponse :

```
Tokens: ['hello', ',', 'and', 'welcome', 'to', 'the', 'world', 'of', 'token', '##izer', '##s']
Token IDs: [7592, 1010, 1998, 6160, 2000, 1996, 2088, 1997, 19204, 17629, 2015]
```

Ces tokens et IDs de tokens sont cruciaux pour l'entraînement des modèles d'apprentissage automatique. Ils convertissent le texte en un format numérique que les modèles peuvent traiter, permettant la compréhension des nuances du langage.

Les tokens comme `##izer` et `##s` sont des exemples de la manière dont le tokenizer traite les mots ou parties de mots qui pourraient ne pas être dans son vocabulaire de base.

Le préfixe `##` indique que ce sont des unités de sous-mots ou des suffixes attachés au token précédent sans espace. Cela permet au modèle de gérer une large gamme de vocabulaire, y compris des mots nouveaux ou peu courants, en les décomposant en sous-composants connus.

# Conclusion

Les tokenizers sont fondamentaux pour le NLP, et la bibliothèque Transformers de Huggingface fournit une boîte à outils complète pour travailler avec eux.

En comprenant et en utilisant les tokenizers, nous pouvons combler le fossé entre le langage humain et la compréhension des machines, débloquant une large gamme d'applications en IA.

Que vous soyez un développeur expérimenté ou nouveau dans le NLP, plonger dans les méthodes de tokenisation est un excellent moyen d'améliorer vos compétences en apprentissage automatique.

J'espère que vous avez apprécié cet article. Si vous avez des questions, faites-le moi savoir dans les commentaires. [Visitez turingtalks.ai](https://www.turingtalks.ai/) pour des tutoriels AI hebdomadaires en format byte-sized.