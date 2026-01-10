---
title: Comment ajouter la recherche web en temps réel à votre LLM avec Tavily
subtitle: Apprenez à connecter Tavily Search pour que votre IA puisse récupérer des
  faits en temps réel au lieu de deviner.
author: Manish Shivanandhan
co_authors: []
series: null
date: '2025-11-17T21:16:03.549Z'
originalURL: https://freecodecamp.org/news/how-to-add-real-time-web-search-to-your-llm-using-tavily
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1763414073220/a9ec7f2d-515e-4d1e-9150-a72450d8aec3.png
tags:
- name: llm
  slug: llm
- name: search
  slug: search
seo_title: Comment ajouter la recherche web en temps réel à votre LLM avec Tavily
seo_desc: 'Large language models are smart. But they are not always well-informed.

  They can write code, summarize books, and explain complex topics, but they struggle
  with real-time facts.

  Their knowledge ends at their training cutoff, which means they can’t te...'
---


Les grands modèles de langage (LLM) sont intelligents. Mais ils ne sont pas toujours bien informés.

Ils peuvent écrire du code, résumer des livres et expliquer des sujets complexes, mais ils ont des difficultés avec les faits en temps réel.

Leurs connaissances s'arrêtent à la date de coupure de leur entraînement (training cutoff), ce qui signifie qu'ils ne peuvent pas vous dire ce qui s'est passé la semaine dernière ou même l'année dernière.

C'est là que la recherche web intervient.

En connectant un modèle à une API de recherche comme [Tavily](https://www.tavily.com/), vous pouvez donner à votre LLM l'accès à des informations factuelles et actuelles provenant d'Internet. Cela rend votre assistant IA, votre chatbot ou votre pipeline RAG beaucoup plus précis et conscient du contexte.

Ce guide vous montrera comment activer la recherche web en temps réel dans votre workflow LLM en utilisant Tavily et LangChain.

Veuillez noter que Tavily est un outil payant (avec un niveau gratuit généreux) et qu'il est populaire au sein de la communauté LangChain. Je ne suis pas affilié au produit – il est simplement utilisé dans un cours sur les agents IA que je suis et semblait être un exemple utile.

## Ce que nous allons couvrir :

* [Pourquoi ajouter la recherche web à un LLM](#heading-pourquoi-ajouter-la-recherche-web-a-un-llm) ?
    
* [Comment fonctionne Tavily](#heading-comment-fonctionne-tavily)
    
* [Configuration de Tavily](#heading-configuration-de-tavily)
    
* [Créer un agent LLM avec Tavily Search](#heading-creer-un-agent-llm-avec-tavily-search)
    
* [Comment fonctionne Tavily Search](#heading-comment-fonctionne-tavily-search)
    
* [Utiliser Tavily sans LangChain](#heading-utiliser-tavily-sans-langchain)
    
* [Améliorer la qualité de la recherche](#heading-ameliorer-la-qualite-de-la-recherche)
    
* [Construire un chatbot capable de recherche](#heading-construire-un-chatbot-capable-de-recherche)
    
* [Applications concrètes](#heading-applications-concretes)
    
* [Pourquoi Tavily est un bon choix](#heading-pourquoi-tavily-est-un-bon-choix)
    
* [Conclusion](#heading-conclusion)
    

## Pourquoi ajouter la recherche web à un LLM ?

Lorsque vous posez à un modèle une question telle que « Quels sont les meilleurs Frameworks d'IA en 2025 ? », il essaie de prédire une réponse à partir de ses données d'entraînement. Si ces données s'arrêtent en 2023, il pourrait lister des outils obsolètes.

En intégrant la recherche web, vous donnez au modèle un moyen de vérifier les informations avant de répondre.

Ce processus est appelé [génération augmentée par récupération](https://www.freecodecamp.org/news/retrieval-augmented-generation-rag-handbook/) (RAG). Il combine deux étapes : la récupération de données pertinentes et la génération d'une réponse basée sur celles-ci.

Tavily gère la partie récupération. Il parcourt le web pour trouver le contenu le plus pertinent et le renvoie sous forme de résumés propres et structurés que les LLM peuvent facilement utiliser. Le résultat est une IA qui semble intelligente et reste précise.

## Comment fonctionne Tavily

Tavily est une API de recherche web conçue spécifiquement pour les applications d'IA.

Contrairement aux moteurs de recherche traditionnels qui renvoient des liens, Tavily renvoie des résumés courts et pertinents avec du contexte. Il se concentre sur la fourniture d'informations concises que les modèles peuvent comprendre sans analyse complexe.

L'API Tavily est simple et rapide. Vous pouvez l'utiliser directement avec Python, Node.js ou via les intégrations LangChain.

Elle prend également en charge le filtrage avancé, le ciblage par sujet et le contrôle du nombre maximal de résultats pour vous aider à affiner la quantité et la qualité des données récupérées.

## Configuration de Tavily

Tout d'abord, inscrivez-vous sur tavily.com et obtenez une clé API. Tavily n'est pas un outil gratuit mais propose 1000 crédits gratuits pour nous permettre de tester.

Ensuite, installez les packages requis :

```python
pip install -qU langchain langchain-openai langchain-tavily
```

Une fois installés, exportez votre clé API pour que Tavily puisse authentifier vos requêtes.

```python
export TAVILY_API_KEY="your_api_key"
```

Vous êtes maintenant prêt à connecter Tavily à un modèle de langage via LangChain.

## Créer un agent LLM avec Tavily Search

[LangChain](https://www.turingtalks.ai/p/langchain-vs-langgraph) facilite la combinaison de plusieurs outils avec votre modèle. Dans cet exemple, nous allons créer un agent qui utilise Tavily comme moteur de recherche.

```python
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

# Initialize the Tavily Search tool
tavily_search = TavilySearch(max_results=5, topic="general")

# Initialize the agent with the search tool
agent = create_agent(
    model=ChatOpenAI(model="gpt-5"),
    tools=[tavily_search],
    system_prompt="You are a helpful research assistant. Use web search to find accurate, up-to-date information."
)
# Use the agent
response = agent.invoke({
    "messages": [{"role": "user", "content": "What is the most popular sport in the world? Include only Wikipedia sources."}]
})
print(response)
```

Cet exemple crée un agent conversationnel propulsé par le modèle GPT d'OpenAI et l'outil Tavily Search. L'agent lit la requête de l'utilisateur, utilise Tavily pour récupérer des données web pertinentes et renvoie une réponse à jour.

Le `system_prompt` donne au modèle des instructions claires pour s'appuyer sur les résultats du web pour la précision factuelle. Vous pouvez le personnaliser pour limiter ou étendre la dépendance de l'agent à la recherche.

## Comment fonctionne Tavily Search

1. L'utilisateur envoie une question. L'agent reçoit le message et détermine qu'il a besoin d'informations externes.
    
2. Tavily effectue une recherche. Il interroge le web pour trouver des résultats pertinents, résumant le contenu en extraits lisibles avec des liens vers les sources.
    
3. Le LLM lit les résumés. Le modèle utilise ces extraits comme contexte et génère une réponse finale qui inclut des faits du monde réel.
    

Ce modèle transforme votre LLM d'une base de connaissances statique en un assistant dynamique qui reste à jour avec des données en direct.

## Utiliser Tavily sans LangChain

Vous pouvez également utiliser Tavily directement avec Python si vous souhaitez plus de contrôle sur le flux.

```python
from tavily import TavilyClient
from openai import OpenAI

tavily = TavilyClient(api_key="your_api_key")
client = OpenAI()

def answer_with_tavily(question):
    search_results = tavily.search(question)
    snippets = "\n".join([r["content"] for r in search_results["results"]])
    prompt = f"Use the following search results to answer the question:\n\n{snippets}\n\nQuestion: {question}"
    response = client.responses.create(model="gpt-4o-mini", input=prompt)
    return response.output_text
print(answer_with_tavily("What are the biggest AI startups of 2025?"))
```

Cet exemple envoie les résumés de recherche Tavily directement dans un Prompt de LLM. C'est simple, flexible et cela fonctionne même sans LangChain.

## Améliorer la qualité de la recherche

Vous pouvez rendre les résultats de Tavily plus pertinents en ajustant quelques paramètres.

* **max_results :** contrôle le nombre d'extraits à renvoyer. Des valeurs plus faibles rendent les réponses plus rapides et plus ciblées.
    
* **topic :** aide à restreindre le type de contenu que vous souhaitez (comme « technology », « science » ou « finance »).
    
* **filters :** utilisé pour restreindre les résultats à certains domaines ou exclure ceux qui ne sont pas souhaités.
    

Par exemple :

```python
tavily_search = TavilySearch(max_results=3, topic="technology")
```

Cette configuration indique à Tavily de ne renvoyer que les trois meilleurs résultats liés à la technologie, idéal pour des requêtes ciblées.

## Construire un chatbot capable de recherche

Une fois que vous avez connecté Tavily, vous pouvez créer un chatbot qui utilise automatiquement la recherche en cas de besoin.

Par exemple, si une requête contient des mots comme « dernier », « aujourd'hui » ou « actualités », l'agent peut déclencher une recherche Tavily.

```python
def smart_chatbot(question):
    if any(word in question.lower() for word in ["today", "latest", "recent", "news"]):
        return answer_with_tavily(question)
    else:
        return client.responses.create(model="gpt-4o-mini", input=question).output_text
```

Cela rend votre chatbot dynamique, utilisant des données en temps réel lorsque c'est nécessaire, tout en gardant les réponses simples rapides.

## Applications concrètes

Les LLM augmentés par la recherche sont utilisés partout.

Les assistants de recherche les utilisent pour extraire des articles récents, les équipes marketing pour suivre les tendances et les analystes pour recueillir des informations concurrentielles. Les développeurs construisent des agents de connaissance capables d'explorer automatiquement la documentation ou les réglementations.

En combinant les résultats de recherche structurés de Tavily avec la puissance de raisonnement d'un LLM, vous pouvez construire des outils qui restent à la fois précis et conversationnels.

## Pourquoi Tavily est un bon choix

Les API de recherche traditionnelles renvoient du HTML non structuré ou des extraits bruts que les modèles ont du mal à lire.

Tavily est optimisé pour l'IA. Il nettoie, résume et filtre les données avant de les renvoyer. La sortie est concise, lisible et peut être utilisée directement dans vos Prompts ou vos pipelines RAG.

Il réduit également les [hallucinations](https://www.ibm.com/think/topics/ai-hallucinations) car le modèle dispose d'un contexte factuel et ancré sur lequel travailler. Cela le rend idéal pour les systèmes d'IA en production qui ont besoin de fiabilité autant que de créativité.

Tavily n'est pas la seule option pour la recherche web. Il existe d'autres options comme RAG web browser, Exa, etc. Voici une [liste complète](https://apify.com/alternatives/tavily-alternatives) avec leurs avantages et inconvénients.

## Conclusion

Les grands modèles de langage sont puissants, mais ils ne vivent pas sur Internet. Sans recherche, ils devinent. Avec Tavily, ils savent.

En intégrant Tavily dans votre workflow LLM, vous comblez le fossé entre l'intelligence statique et la connaissance en temps réel. Que vous construisiez un chatbot, un outil de recherche ou un assistant IA, l'ajout de Tavily Search donne à votre modèle l'accès aux informations les plus actuelles du monde.

La combinaison de LangChain, OpenAI et Tavily transforme n'importe quel LLM en un chercheur IA connecté, informé et fiable, capable de répondre enfin aux questions sur aujourd'hui, et pas seulement sur hier.

*J'espère que vous avez apprécié cet article. Inscrivez-vous à ma newsletter gratuite* [***TuringTalks.ai***](https://www.turingtalks.ai/) *pour plus de tutoriels pratiques sur l'IA. Vous pouvez également* [***visiter mon site web***](https://manishshivanandhan.com/)*.*