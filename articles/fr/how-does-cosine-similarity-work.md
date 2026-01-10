---
title: Comment fonctionne la similitude cosinus ? Les mathématiques derrière les LLM
  expliquées
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2025-09-18T01:12:39.036Z'
originalURL: https://freecodecamp.org/news/how-does-cosine-similarity-work
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1758157868492/7d242ca0-7721-4d25-93fb-2f0a6e319690.png
tags:
- name: 'LLM''s '
  slug: llms
- name: llm
  slug: llm
- name: Mathematics
  slug: mathematics
- name: Math
  slug: math
seo_title: Comment fonctionne la similitude cosinus ? Les mathématiques derrière les
  LLM expliquées
seo_desc: 'When you talk to a large language model (LLM), it feels like the model
  understands meaning. But under the hood, the system relies on numbers, vectors,
  and math to find the relationships between words and sentences.

  One of the most important tools tha...'
---

Lorsque vous communiquez avec un grand modèle de langage (LLM), vous avez l'impression que le modèle comprend le sens. Mais sous le capot, le système s'appuie sur des nombres, des vecteurs et des mathématiques pour trouver les [relations entre les mots](https://www.turingtalks.ai/p/how-to-perform-sentence-similarity-check-using-sentence-transformers) et les phrases.

L'un des outils les plus importants rendant cela possible est la similitude cosinus (cosine similarity). Si vous voulez savoir comment un LLM peut juger que deux phrases signifient presque la même chose, la similitude cosinus en est la clé.

Cet article explique la similitude cosinus en langage simple, présente les mathématiques qui la sous-tendent et fait le lien avec le fonctionnement des modèles de langage modernes. À la fin, vous comprendrez pourquoi cette idée simple de mesurer les angles entre les vecteurs alimente la recherche, les chatbots et de nombreux autres systèmes d'IA.

## **Table des matières**

* [Qu'est-ce que la similitude cosinus ?](#heading-qu-est-ce-que-la-similitude-cosinus)
    
* [Les mathématiques derrière la similitude cosinus](#heading-les-mathematiques-derriere-la-similitude-cosinus)
    
* [Un exemple simple](#heading-un-exemple-simple)
    
* [La similitude cosinus dans les plongements (embeddings)](#heading-la-similitude-cosinus-dans-les-plongements)
    
* [Comment les LLM utilisent la similitude cosinus](#heading-comment-les-llm-utilisent-la-similitude-cosinus)
    
* [Limites de la similitude cosinus](#heading-limites-de-la-similitude-cosinus)
    
* [Pourquoi cela compte pour les LLM](#heading-pourquoi-cela-compte-pour-les-llm)
    
* [Conclusion](#heading-conclusion)
    

## **Qu'est-ce que la similitude cosinus ?**

Imaginez que vous avez deux phrases. Pour un ordinateur, ce ne sont pas des mots mais des vecteurs, de longues listes de nombres qui capturent le sens.

La similitude cosinus mesure la proximité de ces deux vecteurs, non pas par leur longueur, mais par l'angle qui les sépare.

![Cosine Similarity](https://cdn.hashnode.com/res/hashnode/image/upload/v1757481567784/ccd74ce9-d561-47b5-a5e8-c3e77ed36e79.png align="center")

Pensez à deux flèches partant du même point. Si elles pointent dans la même direction, l'angle entre elles est de zéro et la similitude cosinus est de un. Si elles pointent dans des directions opposées, l'angle est de 180 degrés et la similitude cosinus est de moins un. Si elles forment un angle droit, la similitude cosinus est de zéro.

Ainsi, la similitude cosinus nous indique si deux vecteurs pointent dans la même direction générale. Dans les tâches linguistiques, cela signifie qu'elle nous indique si deux segments de texte portent un sens similaire.

## **Les mathématiques derrière la similitude cosinus**

Pour comprendre la similitude cosinus, nous devons examiner un peu de mathématiques. Le cosinus d'un angle en géométrie est le rapport entre le produit scalaire de deux vecteurs et le produit de leurs normes (magnitudes). Écrite sous forme de formule, la similitude cosinus ressemble à ceci :

```plaintext
cosine_similarity(A, B) = (A · B) / (||A|| * ||B||)
```

Ici :

* `A · B` est le produit scalaire (dot product) des vecteurs A et B.
    
* `||A||` est la norme (la longueur) du vecteur A.
    
* `||B||` est la norme du vecteur B.
    

Le produit scalaire multiplie les nombres correspondants dans les deux vecteurs et les additionne. La norme d'un vecteur revient à trouver la longueur d'une flèche, en utilisant le [théorème de Pythagore](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Pythagore).

Cette formule donne toujours une valeur comprise entre -1 et 1. Une valeur proche de 1 signifie que les vecteurs pointent presque dans la même direction. Une valeur proche de 0 signifie qu'ils ne sont pas liés. Une valeur proche de -1 signifie qu'ils sont opposés.

## **Un exemple simple**

Voyons un court exemple utilisant Python. Supposons que vous souhaitiez vérifier la similarité entre deux textes courts. Nous pouvons utiliser [scikit-learn](https://scikit-learn.org/) pour les transformer en vecteurs, puis calculer la similitude cosinus.

```plaintext
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

texts = [
    "I love machine learning",
    "I love deep learning"
]

vectorizer = TfidfVectorizer().fit_transform(texts)
vectors = vectorizer.toarray()

similarity = cosine_similarity([vectors[0]], [vectors[1]])
print("Cosine similarity:", similarity[0][0])
```

Le code commence par importer deux outils importants. `TfidfVectorizer` est chargé de transformer le texte en nombres, tandis que `cosine_similarity` mesure la similarité entre deux ensembles de nombres. Ensemble, ils nous permettent de comparer du texte d'une manière compréhensible pour un ordinateur.

Ensuite, nous définissons les phrases que nous voulons comparer. Dans cet exemple, nous utilisons "I love machine learning" et "I love deep learning". Ces deux phrases partagent certains mots tels que "I", "love" et "learning", tout en différant par un seul mot : "machine" contre "deep". Cela en fait d'excellents exemples de test, car ils sont manifestement liés mais pas identiques.

Le vectoriseur construit ensuite un vocabulaire à partir de tous les mots uniques des deux phrases. Pour ces entrées, le vocabulaire devient `["deep", "learning", "love", "machine"]`. Cela signifie que le programme dispose désormais d'une liste de tous les mots qu'il suivra lors de la construction de la représentation numérique des phrases.

Chaque phrase est ensuite convertie en vecteur, qui est simplement une liste de nombres. Ces nombres ne sont pas de simples comptages de mots bruts. Ils sont pondérés à l'aide de TF-IDF, qui signifie [Term Frequency–Inverse Document Frequency](https://www.learndatasci.com/glossary/tf-idf-term-frequency-inverse-document-frequency/).

TF-IDF donne plus d'importance aux mots qui comptent dans une phrase et moins d'importance aux mots très courants. Sous une forme simplifiée, la première phrase devient quelque chose comme `[0. 0.50154891 0.50154891 0.70490949]`, tandis que la seconde devient `[0.70490949 0.50154891 0.50154891 0. ]`. Les nombres peuvent paraître petits, mais ce qui compte, ce sont leurs valeurs relatives.

La méthode `.toarray()` convertit ensuite ces vecteurs en tableaux Python standards. Cela les rend plus faciles à manipuler, car la sortie TF-IDF est stockée par défaut dans un format creux (sparse) spécial.

Une fois les phrases représentées sous forme de vecteurs, la similitude cosinus est appliquée. Cette étape vérifie l'angle entre les deux vecteurs.

Si les vecteurs pointent exactement dans la même direction, leur score de similarité sera de un. S'ils ne sont pas liés, le score sera proche de zéro. S'ils pointent dans des directions opposées, le score sera négatif.

Dans ce cas, parce que les deux phrases partagent la plupart de leurs mots, les vecteurs pointent dans une direction similaire, de sorte que la similitude cosinus se situe aux alentours de 0,5 à 0,7.

En termes simples, ce code montre comment un ordinateur peut comparer deux phrases en les transformant en vecteurs de nombres, puis en vérifiant la proximité de ces vecteurs. En utilisant la similitude cosinus, le programme peut juger non seulement si les phrases partagent des mots, mais aussi à quel point leurs sens se chevauchent.

## **La similitude cosinus dans les plongements (embeddings)**

En pratique, les LLM comme GPT ou BERT n'utilisent pas de simples comptages de mots. Ils utilisent plutôt des plongements (embeddings).

Un [plongement (embedding)](https://www.freecodecamp.org/news/how-ai-agents-remember-things-vector-stores-in-llm-memory/) est un vecteur dense qui capture le sens. Chaque mot, phrase ou paragraphe est transformé en un ensemble de nombres qui le placent dans un espace de grande dimension.

Dans cet espace, les mots ayant un sens similaire sont proches les uns des autres. Par exemple, les plongements pour "roi" et "reine" sont plus proches que les plongements pour "roi" et "table".

La similitude cosinus est l'outil qui nous permet de mesurer la proximité de deux plongements. Lorsque vous recherchez "chien", le système peut chercher des plongements qui pointent dans une direction similaire. De cette façon, il trouve des résultats concernant "chiot", "canin" ou "animal de compagnie", même si ces mots exacts ne figurent pas dans votre requête.

## Comment les LLM utilisent la similitude cosinus

Les grands modèles de langage utilisent la similitude cosinus de nombreuses façons. Lorsque vous posez une question, le modèle encode votre entrée dans un vecteur. Il compare ensuite ce vecteur avec des connaissances stockées ou avec des réponses candidates en utilisant la similitude cosinus.

Pour la recherche sémantique, la similitude cosinus aide à classer les documents. Un système peut plonger tous les documents dans des vecteurs, puis plonger votre requête et calculer les scores de similarité. Les documents ayant les scores les plus élevés sont les plus pertinents.

Dans le clustering (regroupement), la similitude cosinus aide à regrouper les phrases qui ont un sens lié. Dans les systèmes de recommandation, elle aide à faire correspondre les utilisateurs aux articles en comparant leurs vecteurs de préférence.

Même lors de la génération de réponses, les LLM s'appuient sur la similitude vectorielle pour décider quels mots ou phrases suivent le mieux le contexte. La similitude cosinus donne au modèle un moyen simple mais puissant de mesurer la proximité du sens.

## **Limites de la similitude cosinus**

Bien que la similitude cosinus soit puissante, elle a des limites. Elle dépend fortement de la qualité des plongements. Si les plongements ne parviennent pas à bien capturer le sens, les scores de similarité peuvent ne pas refléter la proximité réelle.

De plus, la similitude cosinus ne mesure que la direction. Parfois, la magnitude contient également des informations utiles. Par exemple, le plongement d'une phrase peut avoir une longueur qui reflète le degré de confiance. En l'ignorant, la similitude cosinus peut perdre une partie de l'information.

Malgré ces limites, la similitude cosinus reste l'une des méthodes les plus utilisées dans le traitement du langage naturel.

## **Pourquoi cela compte pour les LLM**

La similitude cosinus n'est pas seulement une astuce mathématique. C'est un pont entre le langage humain et la compréhension des machines. Elle permet à un modèle de traiter le sens comme de la géométrie, transformant les questions et les réponses en points dans l'espace.

Sans la similitude cosinus, les plongements seraient moins utiles, et des tâches comme la recherche sémantique, le clustering et le classement seraient plus difficiles. En réduisant le problème à une mesure d'angles, nous rendons le sens mesurable et utilisable.

Chaque fois que vous effectuez une recherche sur Google, discutez avec une IA ou utilisez un moteur de recommandation, la similitude cosinus est à l'œuvre dans les coulisses.

## **Conclusion**

La similitude cosinus explique comment les LLM jugent la proximité de sens entre les mots, les phrases ou même des documents entiers. Elle fonctionne en comparant l'angle entre les vecteurs, et non leur longueur, ce qui la rend idéale pour le texte. Avec les plongements, la similitude cosinus devient le fondement de la recherche sémantique, du clustering, des recommandations et de nombreuses autres tâches dans le traitement du langage naturel.

La prochaine fois qu'une IA vous donnera une réponse qui semble "assez proche", rappelez-vous qu'une idée mathématique simple, mesurer l'angle entre deux flèches, fait une grande partie du travail.

*J'espère que vous avez apprécié cet article. Abonnez-vous à ma newsletter gratuite sur l'IA* [***TuringTalks.ai***](https://www.turingtalks.ai/) *pour plus de tutoriels pratiques sur l'IA. Vous pouvez également* [***visiter mon site web***](https://manishshivanandhan.com/)*.*