---
title: 'Comment utiliser LangChain et LangGraph : Un guide pour débutants sur les
  workflows d''IA'
subtitle: Découvrez comment LangChain et LangGraph vous aident à concevoir des workflows
  d'IA intelligents et adaptatifs, passant de simples prompts à des applications complètes.
author: Manish Shivanandhan
co_authors: []
series: null
date: '2025-11-05T17:23:58.632Z'
originalURL: https://freecodecamp.org/news/how-to-use-langchain-and-langgraph-a-beginners-guide-to-ai-workflows
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1762363391314/34c1c950-b257-40b2-a03d-cbaf1bfbd4b6.png
tags:
- name: langchain
  slug: langchain
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: langgraph
  slug: langgraph
- name: Python
  slug: python
seo_title: 'Comment utiliser LangChain et LangGraph : Un guide pour débutants sur
  les workflows d''IA'
seo_desc: 'Artificial intelligence is moving fast. Every week, new tools appear that
  make it easier to build apps powered by large language models.

  But many beginners still get stuck on one question: how do you structure the logic
  of an AI application? How do y...'
---

L'intelligence artificielle évolue rapidement. Chaque semaine, de nouveaux outils apparaissent, facilitant la création d'applications alimentées par de grands modèles de langage.

Pourtant, de nombreux débutants se heurtent encore à une question : comment structurer la logique d'une application d'IA ? Comment connecter les prompts, la mémoire, les outils et les API de manière propre ?

C'est là qu'interviennent les Frameworks open-source populaires comme [LangChain](https://www.langchain.com/) et [LangGraph](https://www.langchain.com/langgraph).

Tous deux font partie du même écosystème et sont conçus pour vous aider à créer des workflows d'IA complexes sans réinventer la roue.

LangChain se concentre sur la construction de séquences d'étapes appelées chaînes, tandis que LangGraph va plus loin en ajoutant de la mémoire, des branchements et des boucles de rétroaction pour rendre votre IA plus intelligente et flexible.

Ce guide vous aidera à comprendre ce que font ces outils, en quoi ils diffèrent et comment vous pouvez commencer à les utiliser pour construire vos propres projets d'IA.

## **Ce que nous allons aborder**

1. [Qu'est-ce que LangChain ?](#heading-quest-ce-que-langchain)
    
    * [Pourquoi LangChain ne suffisait pas](#heading-pourquoi-langchain-ne-suffisait-pas)
        
2. [Qu'est-ce que LangGraph ?](#heading-quest-ce-que-langgraph)
    
3. [LangChain vs LangGraph](#heading-langchain-vs-langgraph)
    
4. [Quand utiliser chaque outil](#heading-quand-utiliser-chaque-outil)
    
5. [Ajouter de la mémoire et de la persistance](#heading-ajouter-de-la-memoire-et-de-la-persistance)
    
6. [Surveillance et débogage avec LangSmith](#heading-surveillance-et-debogage-avec-langsmith)
    
7. [L'écosystème LangChain](#heading-lecosysteme-langchain)
    
8. [Conclusion](#heading-conclusion)
    

## **Qu'est-ce que LangChain ?**

[LangChain](https://www.turingtalks.ai/p/how-to-build-better-ai-workflows-with-langchain) est un Framework Python et JavaScript qui vous aide à créer des applications alimentées par des modèles de langage. Il fournit une structure pour connecter des modèles comme GPT, des sources de données et des outils dans un flux unique.

Au lieu d'écrire de longs modèles de prompts ou de coder la logique en dur, vous utilisez des composants tels que des chaînes, des outils et des agents.

Un exemple simple consiste à enchaîner des prompts. Par exemple, vous pourriez d'abord demander au modèle de résumer un texte, puis utiliser ce résumé pour générer un titre. LangChain vous permet de définir ces deux étapes et de les connecter dans le code.

Voici un exemple de base en Python :

```python
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")
prompt = PromptTemplate.from_template("Summarize the following text:\n{text}")
chain = LLMChain(prompt=prompt, llm=llm)
result = chain.run({"text": "LangChain helps developers build AI apps faster."})
print(result)
```

Cette chaîne simple prend du texte et le fait passer par un modèle OpenAI pour obtenir un résumé. Vous pouvez ajouter d'autres étapes, comme une deuxième chaîne pour transformer ce résumé en titre ou en question.

LangChain fournit des modules pour les modèles de prompts, les modèles, les retrievers et les outils, afin que vous puissiez créer des workflows sans gérer la logique brute de l'API.

Voici la [documentation complète de LangChain](https://docs.langchain.com/oss/python/langchain/overview).

### **Pourquoi LangChain ne suffisait pas**

LangChain a facilité la création de workflows linéaires.

Mais la plupart des applications réelles ne sont pas linéaires. Lors de la [construction d'un chatbot](https://www.freecodecamp.org/news/build-a-custom-ai-chat-application-with-nextjs/), d'un outil de résumé ou d'un agent autonome, vous avez souvent besoin de boucles, de mémoire et de conditions.

Par exemple, si l'IA fait une supposition erronée, vous pourriez vouloir qu'elle réessaie. Si elle a besoin de plus de données, elle devrait appeler un outil de recherche. Ou si un utilisateur change de contexte, l'IA devrait se souvenir de ce qui a été discuté précédemment.

Les chaînes et les agents de LangChain pouvaient faire une partie de cela, mais le flux était difficile à visualiser et à gérer. Vous deviez écrire des chaînes imbriquées ou utiliser des rappels (callbacks) pour gérer les décisions.

Les développeurs voulaient une meilleure façon de représenter la manière dont les systèmes d'IA réfléchissent réellement. Pas en lignes droites, mais sous forme de graphes où les sorties peuvent mener à différents chemins.

C'est ce qui a conduit à LangGraph.

## **Qu'est-ce que LangGraph ?**

LangGraph est une extension de LangChain qui introduit une approche basée sur les graphes pour les workflows d'IA.

Au lieu d'enchaîner les étapes dans une seule direction, LangGraph vous permet de définir des nœuds et des arêtes comme dans un organigramme. Chaque nœud peut représenter une tâche, une action ou un appel de modèle.

Cette structure permet des boucles, des branchements et des chemins parallèles. C'est parfait pour construire des systèmes de type agent où le modèle raisonne, décide et agit.

Voici un exemple d'une configuration simple de LangGraph :

```python
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from langchain.agents import Tool

def multiply(a: int, b: int):
    return a * b
tools = [Tool(name="multiply", func=multiply, description="Multiply two numbers")]
llm = ChatOpenAI(model="gpt-4o-mini")
agent_executor = create_react_agent(llm, tools)
graph = StateGraph()
graph.add_node("agent", agent_executor)
graph.set_entry_point("agent")
graph.add_edge("agent", END)
app = graph.compile()
response = app.invoke({"input": "Use the multiply tool to get 8 times 7"})
print(response)
```

Cet exemple montre un graphe d'agent de base.

L'IA reçoit une requête, raisonne à son sujet, décide d'utiliser l'outil et termine la tâche. Vous pouvez imaginer étendre cela à des graphes plus complexes où l'IA peut réessayer, appeler des API ou récupérer de nouvelles informations.

LangGraph vous donne un contrôle total sur la façon dont l'IA se déplace entre les états. Chaque nœud peut avoir des conditions. Par exemple, si une réponse est incomplète, vous pouvez la renvoyer à un autre nœud pour l'affiner.

Cela rend LangGraph idéal pour construire des systèmes qui nécessitent plusieurs étapes de raisonnement, comme des bots d'analyse de documents, des réviseurs de code ou des assistants de recherche.

Voici la [documentation complète de LangGraph](https://docs.langchain.com/oss/python/langgraph/overview).

## **LangChain vs LangGraph**

LangChain et LangGraph partagent la même base, mais ils abordent les workflows différemment.

LangChain est linéaire. Chaque chaîne ou agent passe d'une étape à la suivante dans une séquence. Il est plus simple pour commencer, en particulier pour l'ingénierie de prompts, la génération augmentée par récupération (RAG) et les pipelines structurés.

LangGraph est dynamique. Il représente les workflows sous forme de graphes qui peuvent boucler, bifurquer et s'autocorriger.

Une bonne analogie est la suivante : LangChain, c'est comme écrire une liste de tâches dans l'ordre. LangGraph, c'est comme dessiner un organigramme où les décisions peuvent mener à différentes actions ou revenir aux étapes précédentes.

La plupart des développeurs commencent par LangChain pour apprendre les bases, puis passent à LangGraph lorsqu'ils souhaitent créer des systèmes d'IA plus interactifs ou autonomes.

## **Quand utiliser chaque outil**

Si vous construisez des outils simples comme des résumeurs de texte, des chatbots ou des récupérateurs de documents, LangChain suffit. Il est facile à prendre en main et s'intègre bien avec des modèles populaires comme GPT, Claude et Gemini.

Si vous voulez construire des agents multi-étapes, ou des applications qui réfléchissent et s'adaptent, optez pour LangGraph. Vous pouvez définir comment l'IA réagit à différents résultats, et vous obtenez plus de contrôle sur la logique de réessai, le changement de contexte et les boucles de rétroaction.

En pratique, de nombreux développeurs combinent les deux. LangChain fournit les blocs de construction, tandis que LangGraph organise la manière dont ces blocs interagissent.

## **Ajouter de la mémoire et de la persistance**

LangChain et LangGraph supportent tous deux la mémoire, ce qui permet à votre IA de se souvenir du contexte entre les interactions. C'est utile lorsque vous construisez des chatbots, des assistants ou des agents qui doivent transporter des informations à travers les étapes.

Par exemple, si un utilisateur se présente une fois, l'IA devrait être capable de se rappeler ce détail plus tard dans la conversation.

Dans LangChain, la mémoire est gérée via des modules intégrés comme `ConversationBufferMemory` ou `ConversationSummaryMemory`. Ceux-ci vous permettent de stocker les entrées et sorties précédentes afin que le modèle puisse s'y référer dans ses futures réponses.

Voici un exemple simple utilisant LangChain :

```python
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI

memory = ConversationBufferMemory()
llm = ChatOpenAI(model="gpt-4o-mini")
conversation = ConversationChain(llm=llm, memory=memory)

conversation.predict(input="Hello, I am Manish.")
response = conversation.predict(input="What did I just tell you?")
print(response)
```

Dans ce cas, le modèle se souvient de votre message précédent et répond en conséquence. L'objet mémoire agit comme un journal de conversation continu, gardant une trace du dialogue au fur et à mesure qu'il évolue.

LangGraph va encore plus loin en intégrant la mémoire dans l'état du graphe. Chaque nœud du graphe peut accéder à la mémoire partagée ou la mettre à jour, permettant à votre IA de maintenir le contexte à travers plusieurs étapes de raisonnement ou branches. Cette approche est particulièrement utile lors de la construction d'agents qui bouclent, revisitent des nœuds ou dépendent d'interactions précédentes.

Voici comment la mémoire peut être ajoutée à l'intérieur d'un workflow LangGraph :

```python
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langgraph.prebuilt import create_react_agent

llm = ChatOpenAI(model="gpt-4o-mini")
memory = ConversationBufferMemory()

agent = create_react_agent(llm)
graph = StateGraph()

# Add node with access to memory
graph.add_node("chat", lambda state: agent.invoke({"input": state["input"], "memory": memory}))
graph.set_entry_point("chat")
graph.add_edge("chat", END)

app = graph.compile()

app.invoke({"input": "Hello, I am Manish."})
response = app.invoke({"input": "What did I just tell you?"})
print(response)
```

Ici, le graphe garde une trace de la mémoire entre les invocations. Même si chaque appel passe par le même nœud, la mémoire `ConversationBufferMemory` partagée conserve ce qui a été dit précédemment. Cette conception vous permet de construire des agents qui se souviennent du contexte utilisateur, maintiennent l'historique et s'adaptent au fur et à mesure qu'ils se déplacent entre les nœuds.

Que vous utilisiez LangChain ou LangGraph, l'ajout de mémoire est ce qui transforme un simple workflow en un système avec état (stateful), capable de poursuivre une conversation, d'affiner son raisonnement et de répondre plus naturellement au fil du temps.

## **Surveillance et débogage avec LangSmith**

[LangSmith](https://www.langchain.com/langsmith/observability) est un autre outil important de l'écosystème LangChain. Il vous aide à visualiser, surveiller et déboguer vos applications d'IA.

Lors de la construction de workflows, vous voulez souvent voir comment le modèle se comporte, combien il coûte et où les choses tournent mal.

LangSmith enregistre chaque appel effectué par vos chaînes et vos agents. Vous pouvez visualiser les données d'entrée et de sortie, le timing, l'utilisation des tokens et les erreurs. Il fournit un tableau de bord qui montre comment votre système s'est comporté sur plusieurs exécutions.

Vous pouvez intégrer LangSmith facilement en définissant votre variable d'environnement :

```python-repl
export LANGCHAIN_TRACING_V2="true"
export LANGCHAIN_API_KEY="your_api_key_here"
```

Ensuite, chaque processus LangChain ou LangGraph que vous exécutez sera automatiquement enregistré dans LangSmith. Cela aide les développeurs à trouver des bugs, à optimiser les prompts et à comprendre comment le workflow se comporte à chaque étape.

Notez que si LangChain et LangGraph sont open-source, LangSmith est une plateforme payante. LangSmith est un outil précieux mais n'est pas une exigence pour construire des workflows d'IA.

## **L'écosystème LangChain**

LangChain n'est pas seulement une bibliothèque. C'est devenu un écosystème d'outils qui travaillent ensemble.

* **LangChain Core** : Le Framework principal pour les chaînes, les prompts et la mémoire.
    
* **LangGraph** : Une extension basée sur les graphes pour construire des workflows adaptatifs.
    
* **LangSmith** : Une plateforme de débogage et de surveillance pour les applications d'IA.
    
* **LangServe** : Une couche de déploiement qui vous permet de transformer vos chaînes et vos graphes en API en une seule commande.
    

Ensemble, ces outils forment une pile complète pour construire, gérer et déployer des applications de modèles de langage. Vous pouvez commencer par une chaîne simple, la faire évoluer vers un système basé sur les graphes, la tester avec LangSmith et la déployer à l'aide de LangServe.

## **Conclusion**

LangChain et LangGraph facilitent le passage des prompts à des systèmes d'IA prêts pour la production. LangChain vous aide à construire des flux linéaires qui connectent les modèles, les données et les outils. LangGraph vous permet d'aller plus loin en construisant des workflows adaptatifs et intelligents qui raisonnent et apprennent.

Pour les débutants, commencer par LangChain est le meilleur moyen de comprendre comment les modèles de langage peuvent interagir avec d'autres composants. À mesure que vos projets grandissent, LangGraph vous donnera la flexibilité nécessaire pour gérer une logique complexe et un état à long terme.

Que vous construisiez un chatbot, un agent ou un assistant de connaissances, ces outils vous aideront à passer de l'idée à la mise en œuvre plus rapidement et de manière plus fiable.

*J'espère que vous avez apprécié cet article. Inscrivez-vous à ma newsletter gratuite* [***TuringTalks.ai***](https://www.turingtalks.ai/) *pour plus de tutoriels pratiques sur l'IA. Vous pouvez également* [***visiter mon site web***](https://manishshivanandhan.com/)*.*