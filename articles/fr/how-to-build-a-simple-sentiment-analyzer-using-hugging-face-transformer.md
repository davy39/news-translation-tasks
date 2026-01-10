---
title: Comment construire un analyseur de sentiment simple en utilisant Hugging Face
  Transformer
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2024-01-26T00:32:04.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-simple-sentiment-analyzer-using-hugging-face-transformer
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/pngtree-facial-emotions-illustration-in-black-outline-on-white-background-vector-picture-image_10574137.png
tags:
- name: natural language processing
  slug: natural-language-processing
- name: nlp
  slug: nlp
- name: Sentiment analysis
  slug: sentiment-analysis
seo_title: Comment construire un analyseur de sentiment simple en utilisant Hugging
  Face Transformer
seo_desc: "In this article, we will look at writing a sentiment analyzer using Hugging\
  \ Face Transformer, a powerful tool in the world of NLP. \nImagine you’re running\
  \ a business and you want to know what your customers think about your product.\
  \ Or maybe you’re a..."
---

Dans cet article, nous allons examiner l'écriture d'un analyseur de sentiment en utilisant Hugging Face Transformer, un outil puissant dans le monde du TAL (Traitement Automatique des Langues).

Imaginez que vous dirigez une entreprise et que vous souhaitez savoir ce que vos clients pensent de votre produit. Ou peut-être êtes-vous un réalisateur de films souhaitant évaluer la réaction du public à votre dernière sortie.

C'est là que l'analyse de sentiment entre en jeu.

> L'analyse de sentiment est une technique utilisée dans l'analyse de texte qui aide à identifier et à catégoriser les opinions exprimées dans un texte.

L'analyse de sentiment détermine si l'opinion exprimée dans un document, une phrase ou une caractéristique/aspect d'entité est positive, négative ou neutre.

Dans un monde où les données sont roi, l'analyse de sentiment est un joyau de la couronne. C'est comme avoir un superpouvoir pour comprendre le ton émotionnel derrière les mots à grande échelle.

Les entreprises l'utilisent pour comprendre les retours des clients sur les produits et services. Les gouvernements et les organisations l'utilisent pour avoir une idée de l'opinion publique.

Dans la gestion des médias sociaux, l'analyse de sentiment est utilisée pour la surveillance de marque, le service client et la recherche marketing.

Il ne s'agit pas seulement de comprendre combien de personnes parlent de votre marque ou produit, mais comment elles se sentent à ce sujet.

## Qu'est-ce que Hugging Face ?

Maintenant, parlons de Hugging Face. Non, ce n'est pas ce que vous pensez. Vous ne allez pas serrer des visages.

Dans le monde de l'IA, [Hugging Face](https://huggingface.co/) est une véritable star. C'est une communauté et une plateforme d'IA qui fournit des outils et des modèles de pointe pour le Traitement Automatique des Langues (TAL).

Imaginez cela comme une boîte à outils qui vous donne le pouvoir de comprendre et de générer le langage humain. C'est comme avoir un magicien linguistique à vos côtés.

L'offre la plus populaire de Hugging Face est la bibliothèque 'Transformers'. La bibliothèque Transformers est remplie d'API et d'outils qui vous permettent de facilement récupérer et entraîner des modèles pré-entraînés de premier ordre.

Lorsque vous choisissez ces modèles pré-entraînés, vous réduisez les coûts de calcul et l'empreinte carbone. De plus, vous économisez beaucoup de temps et de ressources que vous auriez autrement consacrés à l'entraînement d'un modèle à partir de zéro.

Ces modèles résolvent des tâches courantes dans divers domaines, comme :

* **Traitement Automatique des Langues (TAL)** : Ici, vous pouvez faire un tas de choses cool comme la classification de texte, la détection de noms ou d'entités dans le texte, la réponse à des questions, la modélisation de langage, la synthèse, la traduction, la gestion de questions à choix multiples, et même la génération de texte.
* **Vision par ordinateur** : Cela implique la classification d'images, la détection et le contour des objets dans les images, et plus encore.
* **Audio** : Vous pouvez travailler sur la reconnaissance automatique de la parole et la classification de différents types de sons.
* **Tâches multimodales** : Ce sont des tâches qui mélangent tout, comme répondre à des questions basées sur des tableaux, reconnaître du texte dans des images (comme des documents scannés), extraire des informations de ces documents, classifier des vidéos, et répondre à des questions basées sur des images.

Le point fort des Transformers est qu'ils sont flexibles avec différents frameworks. Que vous soyez adepte de [PyTorch](https://turingtalks.substack.com/p/pytorch-vs-tensorflow-for-deep-learning), TensorFlow ou JAX, Transformers vous couvre.

Sa facilité d'utilisation et sa nature complète en font un choix privilégié pour les chercheurs, les développeurs et les entreprises.

## Code pour l'analyse de sentiment

Maintenant que vous savez ce que sont l'analyse de sentiment et Hugging Face, écrivons un peu de code. Nous allons utiliser Python et la bibliothèque `transformers` de Hugging Face pour construire un analyseur de sentiment simple.

Vous pouvez soit utiliser votre terminal, installer Python et exécuter le code, soit utiliser un [Google Colab notebook](https://colab.research.google.com/). Je recommande cette dernière option car elle est pré-installée avec Python.

Installez la bibliothèque `transformers` avec cette commande :

```
pip install transformers
```

Si vous utilisez un notebook Colab, utilisez un symbole **!** avant la commande pour que le notebook la traite comme une commande shell (Colab exécute le code comme Python par défaut).

```
!pip install transfomers
```

Une fois l'installation terminée, vous pouvez commencer à utiliser la bibliothèque. Tout d'abord, importons `pipeline` depuis la bibliothèque transformers.

```
from transformers import pipeline
```

Dans Hugging Face, un "pipeline" est comme un outil qui vous aide à effectuer une série d'étapes pour transformer les données dans la forme que vous souhaitez. Le pipeline simplifie l'utilisation de ces outils pour différentes tâches, sans avoir besoin de connaître tous les détails complexes sur le fonctionnement interne de ces outils.

Maintenant, chargeons le pipeline `sentiment-analysis`.

```
sentiment_pipeline = pipeline("sentiment-analysis")

```

Maintenant, me croiriez-vous si je vous disais que nous avons presque terminé ? Notre modèle d'analyse de sentiment est prêt et nous pouvons passer du texte au pipeline et obtenir l'étiquette ainsi qu'un score de sentiment.

```
# Exécuter l'analyse de sentiment
result = sentiment_pipeline("Chaque nouveau jour apporte une chance de créer des souvenirs joyeux et de saisir de nouvelles opportunités.")

# Imprimer le résultat
print(result)
```

Voici le résultat du code ci-dessus :

```
[{'label': 'POSITIVE', 'score': 0.9998821020126343}]
```

Si vous souhaitez passer plusieurs phrases, passez un tableau d'entrées au pipeline.

```
result = sentiment_pipeline(["Chaque nouveau jour apporte une chance de créer des souvenirs joyeux et de saisir de nouvelles opportunités.","Malgré les efforts, le projet n'a pas répondu aux attentes, entraînant déception et frustration au sein de l'équipe."])
print(result)
```

Voici le résultat du code ci-dessus :

```
[{'label': 'POSITIVE', 'score': 0.9998821020126343}, {'label': 'NEGATIVE', 'score': 0.9997937083244324}]
```

J'espère que vous comprenez à quel point la bibliothèque Hugging Face Transformer est puissante. Ce n'est qu'un exemple des nombreux modèles pré-entraînés que Hugging Face propose. À moins que vous ne travailliez sur un problème unique, vous devriez trouver un modèle pré-entraîné dans Hugging Face disponible pour vous.

## Résumé

Dans cet article, nous avons appris l'analyse de sentiment et Hugging Face, un outil puissant dans le monde du TAL. Plus important encore, vous avez fait vos premiers pas dans la réalisation d'une analyse de sentiment en utilisant la bibliothèque Hugging Face Transformers.

Rappelez-vous, ce que nous avons couvert n'est que la partie émergée de l'iceberg. Le domaine du TAL est vaste et en constante évolution. La bibliothèque Hugging Face Transformers est un allié puissant dans votre voyage à travers l'IA. Elle simplifie les tâches complexes et vous donne accès à des modèles pré-entraînés, vous faisant économiser du temps et des ressources.

J'espère que vous avez apprécié cet article. Trouvez plus d'articles pour débutants sur l'IA sur **[turingtalks.ai](https://www.turingtalks.ai/)**