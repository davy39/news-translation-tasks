---
title: Comment effectuer une vérification de la similarité des phrases à l'aide de
  Sentence Transformers
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2025-09-03T16:29:56.496Z'
originalURL: https://freecodecamp.org/news/how-to-perform-sentence-similarity-check-using-sentence-transformers
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1756916978057/de0bda62-c9ea-48d1-b1ac-b78eb10e82d2.png
tags:
- name: Machine Learning
  slug: machine-learning
- name: natural language processing
  slug: natural-language-processing
- name: nlp
  slug: nlp
seo_title: Comment effectuer une vérification de la similarité des phrases à l'aide
  de Sentence Transformers
seo_desc: "Sentence similarity plays an important role in many natural language processing\
  \ (NLP) applications. \nWhether you build chatbots, recommendation systems, or search\
  \ engines, understanding how close two sentences are in meaning can improve user\
  \ experien..."
---

La similarité des phrases joue un rôle important dans de nombreuses applications de traitement du langage naturel (NLP). 

Que vous construisiez des chatbots, des systèmes de recommandation ou des moteurs de recherche, comprendre à quel point deux phrases sont proches en termes de sens peut améliorer l'expérience utilisateur – et c'est ce que la similarité des phrases vous permet de faire.

[Sentence Transformers](https://sbert.net/) rend ce processus simple et efficace. Dans ce guide, vous apprendrez ce qu'est la similarité des phrases, comment fonctionnent les Sentence Transformers et comment écrire du code pour mesurer la similarité entre deux ensembles de phrases.

## Table des matières

* [Qu'est-ce que la similarité des phrases ?](#heading-qu-est-ce-que-la-similarite-des-phrases)
    
* [Pourquoi utiliser Sentence Transformers](#heading-pourquoi-utiliser-sentence-transformers)
    
* [Chargement d'un modèle pré-entraîné](#heading-chargement-d-un-modele-pre-entraine)
    
* [Définition des phrases à comparer](#heading-definition-des-phrases-a-comparer)
    
* [Conversion des phrases en embeddings](#heading-conversion-des-phrases-en-embeddings)
    
* [Calcul de la similarité cosinus](#heading-calcul-de-la-similarite-cosinus)
    
* [Affichage des résultats](#heading-affichage-des-resultats)
    
* [Exemple de sortie](#heading-exemple-de-sortie)
    
* [Comment interpréter les scores](#heading-comment-interpreter-les-scores)
    
* [Applications concrètes de la similarité des phrases](#heading-applications-concretes-de-la-similarite-des-phrases)
    
    * [Recherche sémantique](#heading-recherche-semantique)
        
    * [Détection de doublons](#heading-detection-de-doublons)
        
    * [Systèmes de recommandation](#heading-systemes-de-recommandation)
        
    * [Chatbots et assistants virtuels](#heading-chatbots-et-assistants-virtuels)
        
    * [Améliorer les performances avec des modèles plus grands](#heading-ameliorer-les-performances-avec-des-modeles-plus-grands)
        
* [Conclusion](#heading-conclusion)
    

## Qu'est-ce que la similarité des phrases ?

La similarité des phrases est le processus de comparaison de deux phrases pour voir à quel point leur sens est proche. Elle ne s'arrête pas aux mots exacts, mais se concentre sur le sens qui se cache derrière eux.

Par exemple :

* « Le chat est assis dehors »
    
* « Le chien joue dans le jardin »
    

Les deux phrases parlent d'animaux à l'extérieur, elles partagent donc une certaine similarité même si elles utilisent des mots différents.

Ce type de compréhension est essentiel pour des tâches telles que le clustering de documents, la détection de doublons ou la recherche sémantique.

## Pourquoi utiliser Sentence Transformers

Les méthodes traditionnelles comme le [Bag of Words](https://www.freecodecamp.org/news/how-bag-of-words-works/) reposaient sur une simple correspondance de mots ou sur le comptage de fréquence. Mais celles-ci échouent lorsque les mots diffèrent alors que le sens reste le même.

Sentence Transformers résout ce problème en utilisant des modèles de langage basés sur les transformateurs comme [BERT](https://en.wikipedia.org/wiki/BERT_%28language_model%29) ou RoBERTa pour créer des embeddings.

Un [embedding](https://www.freecodecamp.org/news/understanding-word-embeddings-the-building-blocks-of-nlp-and-gpts/) est une liste de nombres qui représente le sens d'une phrase. Lorsque deux embeddings sont proches l'un de l'autre dans cet espace de haute dimension, leurs phrases ont un sens similaire.

La bibliothèque Sentence Transformers en Python facilite cela en fournissant des modèles pré-entraînés capables de générer des embeddings pour les phrases.

### Installation des bibliothèques requises

Avant de commencer à coder, assurez-vous d'installer les packages requis. Exécutez cette commande pour le faire :

```plaintext
pip install -U sentence-transformers
```

Cela installera la bibliothèque Sentence Transformers ainsi que ses dépendances.

## Chargement d'un modèle pré-entraîné

Sentence Transformers propose plusieurs modèles pré-entraînés. Pour cet exemple, vous utiliserez le modèle **all-MiniLM-L6-v2**. Il est léger, rapide et fonctionne bien pour la plupart des applications.

Voici comment le charger en Python :

```plaintext
from sentence_transformers import SentenceTransformer

# Load the model
model = SentenceTransformer("all-MiniLM-L6-v2")
```

Une fois chargé, ce modèle peut convertir n'importe quelle phrase en son embedding correspondant.

## Définition des phrases à comparer

Vous avez besoin de deux listes de phrases pour la comparaison. Voici un exemple :

```plaintext
sentences1 = [
    'The cat sits outside',
    'A man is playing guitar',
    'The movies are awesome'
]

sentences2 = [
    'The dog plays in the garden',
    'A woman watches TV',
    'The new movie is so great'
]
```

Chaque phrase de `sentences1` sera comparée à la phrase située à la même position dans `sentences2`.

## Conversion des phrases en embeddings

Maintenant que vous avez les phrases, vous devez les convertir en embeddings à l'aide du modèle.

Ajoutez ce code :

```plaintext
# Convert sentences to embeddings
embeddings1 = model.encode(sentences1, convert_to_tensor=True)
embeddings2 = model.encode(sentences2, convert_to_tensor=True)
```

L'argument `convert_to_tensor=True` indique au modèle de renvoyer des [tenseur PyTorch](https://docs.pytorch.org/tutorials/beginner/introyt/tensors_deeper_tutorial.html), qui fonctionnent bien avec les calculs de similarité.

## Calcul de la similarité cosinus

Une fois que vous avez les embeddings, vous avez besoin d'un moyen de mesurer la similarité. La métrique de [similarité cosinus](https://www.youtube.com/watch?v=zcUGLp5vwaQ) est couramment utilisée à cet effet.

La similarité cosinus examine l'angle entre deux vecteurs dans un espace de haute dimension. Si l'angle est petit, les vecteurs sont similaires.

Ajoutez ce code pour calculer la similarité :

```plaintext
from sentence_transformers import util
# Compute cosine similarity
cosine_scores = util.cos_sim(embeddings1, embeddings2)
```

Maintenant, `cosine_scores` contient le score de similarité pour chaque paire de phrases.

## Affichage des résultats

Pour voir les résultats clairement, formatez-les comme ceci :

```plaintext
# Print formatted results
for i in range(len(sentences1)):
    print(f"{sentences1[i]} \t\t {sentences2[i]} \t\t Score: {cosine_scores[i][i]:.4f}")
```

Cela affichera chaque paire de phrases ainsi que son score de similarité.

## Exemple de sortie

Si vous exécutez ce code, vous verrez un résultat similaire à celui ci-dessous. 

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1756385160047/576750a6-3c65-45e7-a634-f1e7375e7e16.png align="center")

La troisième paire a le score le plus élevé car les deux phrases parlent de films de manière positive.

## Comment interpréter les scores

Le score de similarité cosinus varie entre **-1** et **1**.

* Un score proche de **1** signifie que les phrases sont très similaires.
    
* Un score proche de **0** signifie qu'elles ne sont pas liées.
    
* Des valeurs négatives signifient que les phrases ne sont pas liées ou ont même un sens opposé.
    

Dans la plupart des cas réels, vous vous concentrez sur les valeurs comprises entre 0 et 1. Plus la valeur est élevée, plus les sens sont proches.

## Applications concrètes de la similarité des phrases

La similarité des phrases est devenue un élément central de nombreuses applications modernes car elle aide les systèmes à comprendre le sens plutôt que de s'appuyer sur des mots exacts. Ce changement rend la recherche, l'analyse et les recommandations beaucoup plus précises et utiles.

### **Recherche sémantique**

Les moteurs de recherche traditionnels dépendent de la correspondance par mots-clés. Si les mots exacts sont absents, les résultats deviennent souvent non pertinents. La [recherche sémantique](https://en.wikipedia.org/wiki/Semantic_search) résout ce problème en examinant le sens derrière une requête. 

Par exemple, si quelqu'un cherche « meilleures façons d'apprendre la guitare », le système peut renvoyer des résultats pour « conseils pratiques pour jouer de la guitare » même si les mots-clés diffèrent. Cela rend les expériences de recherche plus fluides et plus intelligentes.

### **Détection de doublons**

Les grands ensembles de données contiennent souvent du contenu répété ou quasi identique. Une vérification manuelle est impossible lorsqu'on traite des millions d'enregistrements. 

La similarité des phrases automatise cela en détectant les textes qui portent le même sens même si la formulation change légèrement. Ceci est particulièrement utile pour le nettoyage des données, les pipelines de web scraping ou la gestion du contenu généré par les utilisateurs.

### **Systèmes de recommandation**

Les moteurs de recommandation fonctionnent mieux lorsqu'ils comprennent le contexte. Par exemple, si un utilisateur aime les articles sur la « cuisine saine », le système peut recommander du contenu sur des « recettes nutritives » ou des « repas sains et rapides » en utilisant des scores de similarité. Cette approche va au-delà des mots-clés de surface et trouve des connexions plus profondes dans le texte.

### **Chatbots et assistants virtuels**

Les chatbots stockent un vaste ensemble de questions et réponses potentielles des utilisateurs. Lorsque quelqu'un tape une nouvelle question, le système doit trouver la réponse la plus pertinente. En utilisant la similarité des phrases, les chatbots font correspondre l'entrée de l'utilisateur avec la requête existante la plus proche en termes de sens, et non seulement de mots, ce qui conduit à des conversations plus précises et naturelles.

### Améliorer les performances avec des modèles plus grands

Le modèle [all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) est rapide et précis pour les tâches de petite à moyenne envergure.

Pour plus de précision, vous pouvez essayer des modèles plus grands comme [all-mpnet-base-v2](https://huggingface.co/sentence-transformers/all-mpnet-base-v2), bien qu'ils puissent nécessiter plus de mémoire et de temps d'exécution.

Remplacez le nom du modèle dans votre code pour utiliser un modèle pré-entraîné différent :

```plaintext
model = SentenceTransformer("all-mpnet-base-v2")
```

## Conclusion

Sentence Transformers facilite la mesure de la similarité des phrases à l'aide de modèles pré-entraînés. En convertissant les phrases en embeddings et en les comparant avec la similarité cosinus, vous pouvez créer des systèmes qui comprennent le sens plutôt que de vous fier à une simple correspondance de mots.

Avec seulement quelques lignes de code, vous pouvez intégrer cela dans des chatbots, des moteurs de recherche ou des systèmes de recommandation et créer des applications plus intelligentes.

*J'espère que vous avez apprécié cet article. Inscrivez-vous à ma newsletter gratuite* [***TuringTalks.ai***](https://www.turingtalks.ai/) *pour plus de tutoriels pratiques sur l'IA. Vous pouvez également* [*visiter mon site web*](https://manishshivanandhan.com/)*.*