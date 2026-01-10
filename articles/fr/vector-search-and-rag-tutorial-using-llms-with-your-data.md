---
title: Tutoriel sur la recherche vectorielle et RAG – Utilisation des LLMs avec vos
  données
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2023-12-11T18:12:49.000Z'
originalURL: https://freecodecamp.org/news/vector-search-and-rag-tutorial-using-llms-with-your-data
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/vectorsearchthumb.png
tags:
- name: Vector Search
  slug: vector-search
- name: youtube
  slug: youtube
seo_title: Tutoriel sur la recherche vectorielle et RAG – Utilisation des LLMs avec
  vos données
seo_desc: 'You can use Vector Search and embeddings to easily combine your data with
  large language models like GPT-4.

  I just published a course on the freeCodeCamp.org YouTube channel that will teach
  you how to implement Vector Search on three different projec...'
---

Vous pouvez utiliser la recherche vectorielle et les embeddings pour combiner facilement vos données avec des grands modèles de langage comme GPT-4.

Je viens de publier un cours sur la chaîne YouTube freeCodeCamp.org qui vous apprendra à implémenter la recherche vectorielle sur trois projets différents.

Tout d'abord, vous apprendrez les concepts, puis je vous guiderai à travers le développement de trois projets.

Dans le premier projet, nous construisons une fonctionnalité de recherche sémantique pour trouver des films à l'aide de requêtes en langage naturel. Pour cela, nous utilisons Python, des modèles de machine learning et Atlas Vector Search.

Ensuite, nous créons une application simple de questions-réponses qui utilise l'architecture RAG et Atlas Vector Search pour répondre aux questions en utilisant vos propres données.

Et dans le projet final, nous modifions un clone de ChatGPT pour qu'il réponde aux questions sur la contribution au programme de freeCodeCamp.org en fonction de la documentation officielle. Ce projet peut être facilement modifié pour utiliser vos propres données ou documentation.

MongoDB a fourni une subvention qui a rendu ce cours possible. Leur Atlas Vector Search vous permet d'effectuer des recherches de similarité sémantique sur vos données, qui peuvent être intégrées avec des LLMs pour construire des applications alimentées par l'IA.

### Qu'est-ce que les embeddings vectoriels ?

Imaginez que vous avez beaucoup d'objets différents, comme des fruits, et que vous voulez les organiser de manière à montrer à quel point ils sont similaires ou différents. Dans le monde réel, vous pourriez les trier par couleur, taille ou goût. Dans le monde numérique, nous pouvons faire quelque chose de similaire avec les données, et c'est là que les embeddings vectoriels interviennent.

Les embeddings vectoriels sont comme une manière numérique de trier ou de décrire les choses. Chaque élément (comme un mot, une image, ou tout autre chose à laquelle vous pouvez penser) est transformé en une liste de nombres. Cette liste est appelée un "vecteur". Le plus intéressant est que les éléments similaires auront des vecteurs similaires.

En transformant les éléments en vecteurs (listes de nombres), nous pouvons utiliser les mathématiques pour les comprendre et les traiter. Par exemple, nous pouvons mesurer à quel point deux vecteurs sont proches pour voir à quel point les éléments qu'ils représentent sont similaires.

Les mots peuvent être transformés en vecteurs et les mots ayant des significations similaires auront des vecteurs proches les uns des autres. Cela aide dans des tâches comme la recherche d'informations, la traduction de langues, ou même la discussion avec une IA.

La création de ces embeddings implique généralement beaucoup de données et des mathématiques complexes. L'ordinateur examine de nombreux exemples (comme la manière dont les mots sont utilisés dans les phrases) et apprend la meilleure façon de les transformer en vecteurs.

### Qu'est-ce que la recherche vectorielle ?

La recherche vectorielle est une méthode utilisée pour trouver et récupérer des informations qui sont les plus similaires ou pertinentes par rapport à une requête donnée. Mais au lieu de chercher des correspondances exactes comme les moteurs de recherche traditionnels, la recherche vectorielle tente de comprendre le sens ou le contexte de la requête. La recherche vectorielle est un moyen de mettre en œuvre la recherche sémantique, ce qui signifie utiliser le sens des mots pour trouver des résultats pertinents.

La recherche vectorielle utilise les embeddings vectoriels en transformant à la fois la requête de recherche et les éléments de la base de données (comme des documents, des images ou des produits) en vecteurs, puis en comparant ces vecteurs pour trouver les meilleures correspondances.

Voici comment le processus fonctionne en détail :

1. **Transformation des données en vecteurs** : Tout d'abord, tout doit être converti en vecteurs. Cela est fait en utilisant des modèles qui sont entraînés à comprendre différents types de données. Par exemple, un document texte est analysé et transformé en un vecteur qui représente son contenu et sa signification.
2. **Traitement de la requête** : Lorsque vous effectuez une requête de recherche, le même processus est appliqué pour transformer votre requête en un vecteur. Ce vecteur représente ce que vous cherchez.
3. **Calcul de la similarité** : Le vecteur de votre requête de recherche est ensuite comparé avec les vecteurs des éléments de la base de données. Cela est généralement fait en calculant la distance entre les vecteurs. La méthode la plus courante consiste à utiliser ce que l'on appelle la "similarité cosinus", qui mesure le cosinus de l'angle entre deux vecteurs. Si deux vecteurs sont très similaires, l'angle sera petit et la similarité cosinus sera élevée.
4. **Classement des résultats** : Sur la base de ces mesures de similarité, le système classe les éléments de la base de données. Ceux dont les vecteurs sont les plus proches du vecteur de requête sont considérés comme les plus pertinents et sont présentés comme les meilleurs résultats de recherche.
5. **Récupération des meilleures correspondances** : Enfin, le système récupère et affiche les éléments qui correspondent le mieux à la requête, selon la similarité de leurs vecteurs.

En essence, la recherche vectorielle utilise les embeddings vectoriels pour comprendre le contenu et le contexte à la fois de la requête et des éléments de la base de données. En comparant ces vecteurs, elle trouve et classe efficacement les résultats les plus pertinents, offrant un outil puissant pour rechercher dans de grands ensembles de données complexes.

### **Génération augmentée par récupération (RAG)**

L'architecture de génération augmentée par récupération (RAG) utilise la recherche vectorielle pour récupérer des documents pertinents en fonction de la requête d'entrée. Elle fournit ensuite ces documents récupérés comme contexte au LLM pour aider à générer une réponse plus informée et précise. C'est-à-dire qu'au lieu de générer des réponses purement à partir de motifs appris pendant l'entraînement, RAG utilise ces documents récupérés pertinents pour aider à générer une réponse plus informée et précise. Cela aide à répondre aux limitations des LLMs. Plus précisément :

* Les RAGs minimisent les hallucinations en ancrant les réponses du modèle dans des informations factuelles.
* En récupérant des informations à partir de sources à jour, RAG garantit que les réponses du modèle reflètent les informations les plus récentes et précises disponibles.
* Bien que RAG ne donne pas directement aux LLMs l'accès aux données locales d'un utilisateur, il leur permet d'utiliser des bases de données externes ou des bases de connaissances, qui peuvent être mises à jour avec des informations spécifiques à l'utilisateur.
* De plus, bien que RAG n'augmente pas la limite de tokens d'un LLM, il rend l'utilisation des tokens du modèle plus efficace en récupérant _uniquement les documents les plus pertinents_ pour générer une réponse.

### Atlas Vector Search

MongoDB Atlas Vector Search vous permet d'effectuer des recherches de similarité sémantique sur vos données, qui peuvent être intégrées avec des LLMs pour construire des applications alimentées par l'IA. Les données de diverses sources et dans différents formats peuvent être représentées numériquement sous forme d'embeddings vectoriels.

Atlas Vector Search vous permet de stocker des embeddings vectoriels aux côtés de vos données sources et métadonnées, en tirant parti de la puissance du modèle de document. Ces embeddings vectoriels peuvent ensuite être interrogés à l'aide d'un pipeline d'agrégation pour effectuer une recherche rapide de similarité sémantique sur les données, en utilisant un algorithme de plus proches voisins approximatifs.

Dans ce cours, vous apprendrez à utiliser Atlas Vector Search dans vos applications.

Regardez le cours complet sur [la chaîne YouTube freeCodeCamp.org](https://youtu.be/JEBDfGqrAUA) (1 heure de visionnage).

%[https://youtu.be/JEBDfGqrAUA]