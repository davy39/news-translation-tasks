---
title: Comment construire de meilleurs workflows IA avec Langchain
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2024-03-13T13:38:40.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-better-ai-workflows-with-langchain
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/1700940849777.png
tags:
- name: AI
  slug: ai
- name: 'LLM''s '
  slug: llms
seo_title: Comment construire de meilleurs workflows IA avec Langchain
seo_desc: 'Have you ever wondered how to use Large Language Models (LLMs) like ChatGPT
  in your app?

  Yes, there is the OpenAI API. You can use it to generate responses based on prompts.
  But what if you want to build a complex application with LLMs integrated tig...'
---

Vous vous êtes déjà demandé comment utiliser des grands modèles de langage (LLMs) comme ChatGPT dans votre application ?

Oui, il y a l'API OpenAI. Vous pouvez l'utiliser pour générer des réponses basées sur des prompts. Mais que faire si vous souhaitez construire une application complexe avec des LLMs intégrés étroitement dans l'expérience utilisateur ? Que faire si vous souhaitez utiliser plusieurs services comme OpenAI, Mistral, et d'autres ?

La réponse est Langchain – un outil puissant conçu pour rationaliser et améliorer les workflows IA.

Examinons ce qu'est Langchain, pourquoi vous voudriez l'utiliser et comment travailler avec lui en utilisant un exemple simple.

## **Qu'est-ce que Langchain ?**

Langchain est une boîte à outils qui simplifie la construction et le déploiement de grands modèles de langage. Elle inclut ceux augmentés avec des capacités de récupération comme les RAGs.

LangChain vise à connecter des grands modèles de langage (LLMs) puissants comme GPT-3.5 et GPT-4 d'OpenAI avec diverses sources de données externes. Cette connexion aide à construire et à améliorer les applications de traitement du langage naturel (NLP).

Langchain gère le travail lourd, rendant plus facile la concentration sur la logique de l'application et l'expérience utilisateur.

De plus, les modèles GPT comme ChatGPT apprennent à partir des données disponibles jusqu'à leur sortie publique. Par exemple, bien que ChatGPT soit devenu disponible à la fin de 2022, sa première version ne connaissait que les choses de 2021 et avant.

LangChain permet aux modèles IA d'accéder et d'apprendre à partir de données plus récentes sans aucune limite.

## **Pourquoi utiliser Langchain ?**

LangChain offre plusieurs avantages par rapport à l'utilisation directe de l'API OpenAI (ou d'autres LLMs). Ceux-ci incluent :

* **Intégration avec plusieurs services** : LangChain permet aux développeurs de combiner les capacités d'OpenAI avec d'autres outils et services de manière transparente. Cela signifie que vous pouvez facilement mélanger et assortir différents modèles IA et bases de données pour obtenir les meilleurs résultats.
* **Fonctionnalité améliorée** : Langchain ajoute des fonctionnalités supplémentaires à ce qu'OpenAI offre. Par exemple, il peut aider à gérer des interactions plus complexes qui nécessitent de se souvenir des conversations passées ou de tirer des informations de sources externes.
* **Efficacité des coûts** : En optimisant comment et quand utiliser les modèles IA, LangChain peut aider à réduire les coûts. Il le fait par des méthodes comme la mise en cache, l'utilisation sélective de modèles et des méthodes optimisées de récupération de données.

LangChain est comme avoir une boîte à outils qui inclut non seulement tout ce qu'OpenAI offre, mais apporte également des composants supplémentaires dans le mélange. Langchain rend plus facile la construction d'applications puissantes et rentables alimentées par des LLMs.

## **Comment commencer avec Langchain et l'API OpenAI**

Pour vous donner un aperçu de la manière dont Langchain peut être appliqué, plongeons dans un exemple de code simple. Nous allons accéder à l'API OpenAI en utilisant Langchain pour générer une réponse à un prompt.

Installez OpenAI et Langchain dans votre environnement de développement ou un [notebook Google Colab](https://colab.research.google.com/). Assurez-vous d'avoir votre clé [OpenAI API](https://platform.openai.com/api-keys) avec vous :

```
pip install openai langchain
```

Maintenant, importons les bibliothèques :

```
import openai
from langchain.llms import OpenAI
```

Le `llms` dans le chemin d'importation signifie "Large Language Models". Ce module permet au script d'utiliser les fonctionnalités de LangChain conçues pour interagir avec les modèles d'OpenAI.

Maintenant, définissons la clé API :

```
openai.api_key = 'votre_clé_api_openai_ici'
```

Maintenant, nous allons initialiser le wrapper LangChain pour l'API OpenAI. Il créera une instance de la classe `OpenAI` importée de la bibliothèque LangChain, en passant la clé API OpenAI comme argument :

```
langchain_openai = OpenAI(api_key=openai.api_key)
```

L'instance `langchain_openai` sera utilisée pour interagir avec les modèles d'OpenAI via l'interface de LangChain.

Maintenant, nous sommes prêts à envoyer le prompt. Demandons à OpenAI quelle est la capitale de la France :

```
question = "Quelle est la capitale de la France ?"
response = langchain_openai(question)
```

Et imprimons la réponse :

```
print("Réponse d'OpenAI :", response)
```

Voici la réponse :

```
Réponse d'OpenAI :

La capitale de la France est Paris.
```

Ceci est un exemple simple d'utilisation de Langchain et OpenAI. Pour la documentation complète et les tutoriels, [visitez la documentation officielle](https://python.langchain.com/docs/get_started/introduction).

## **Conclusion**

Langchain ouvre un monde de possibilités pour les développeurs désireux d'explorer le potentiel des grands modèles de langage. Que vous souhaitiez automatiser des tâches, générer du contenu ou analyser des données, Langchain fournit un framework robuste et convivial.

Avec l'exemple de code fourni, j'espère que vous avez un point de départ pour expérimenter et construire vos applications alimentées par des LLMs en utilisant Langchain.

J'espère que vous avez apprécié cet article. [Visitez turingtalks.ai](https://www.turingtalks.ai/) pour des tutoriels AI hebdomadaires en format byte-sized.