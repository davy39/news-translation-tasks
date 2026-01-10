---
title: Comment utiliser LangChain pour construire avec des LLMs – Un guide pour débutants
subtitle: ''
author: Jacob Lee
co_authors: []
series: null
date: '2024-04-11T23:11:37.000Z'
originalURL: https://freecodecamp.org/news/beginners-guide-to-langchain
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/pexels-pixabay-417273--1-.jpg
tags:
- name: AI
  slug: ai
- name: 'LLM''s '
  slug: llms
seo_title: Comment utiliser LangChain pour construire avec des LLMs – Un guide pour
  débutants
seo_desc: "Large language models (LLMs) are incredibly powerful general reasoning\
  \ tools that are useful in a wide range of situations. \nBut working with LLMs presents\
  \ challenges that are different from building traditional software:\n\nCalls tend\
  \ to be long-runni..."
---

Les grands modèles de langage (LLMs) sont des outils de raisonnement général incroyablement puissants, utiles dans une large gamme de situations. 

Mais travailler avec des LLMs présente des défis différents de la construction de logiciels traditionnels :

* Les appels tendent à être longs et à diffuser la sortie générée dès qu'elle est disponible.
* Au lieu d'une entrée structurée (quelque chose comme JSON) avec des paramètres fixes, ils prennent du langage naturel non structuré et arbitraire en entrée. Ils sont capables de "comprendre" les subtilités de ce langage.
* Ils sont non déterministes. Vous pouvez obtenir différentes sorties même avec la même entrée.

[LangChain](https://langchain.com/) est un framework populaire pour créer des applications alimentées par des LLMs. Il a été construit en gardant à l'esprit ces facteurs et d'autres, et fournit une large gamme d'[intégrations](https://python.langchain.com/docs/integrations/platforms/) avec des fournisseurs de modèles closed-source (comme [OpenAI](https://openai.com/), [Anthropic](https://www.anthropic.com/), et [Google](https://gemini.google.com/)), des modèles open source, et d'autres composants tiers comme les vectorstores.

Cet article vous guidera à travers les bases de la construction avec des LLMs et la [bibliothèque Python de LangChain](https://python.langchain.com). La seule exigence est une familiarité basique avec Python, aucune expérience en machine learning n'est nécessaire !

Vous apprendrez :

* [Configuration de base du projet](#heading-installation)
* [Utilisation des modèles de chat et autres composants fondamentaux de LangChain](#heading-premiers-pas)
* [Utilisation du LangChain Expression Language pour créer des chaînes](#heading-chainage)
* [Diffusion de la sortie dès qu'elle est générée](#heading-diffusion)
* [Passage de contexte pour orienter la sortie du modèle (concepts de base du RAG)](#heading-comment-guider-la-generation-avec-du-contexte)
* [Débogage et traçage des internes de vos chaînes](#heading-debogage)

Plongeons-nous !

## Installation du projet

Nous recommandons d'utiliser un [notebook Jupyter](https://jupyter.org/) pour exécuter le code de ce tutoriel, car il fournit un environnement propre et interactif. Consultez [cette page](https://jupyter.org/install) pour des instructions sur son installation locale, ou [essayez ce notebook Google Colab](https://colab.research.google.com/drive/1MsQNc7AMS3qY4Y94_ZN8ppWcNh0RgD-v?usp=sharing) pour une expérience dans le navigateur.

La première chose que vous devrez faire est de choisir quel modèle de chat vous souhaitez utiliser. Si vous avez déjà utilisé une interface comme ChatGPT auparavant, l'idée de base d'un modèle de chat vous sera familière – le modèle prend des messages en entrée et retourne des messages en sortie. La différence est que nous le ferons en code.

Ce guide utilise par défaut [Anthropic](https://python.langchain.com/docs/integrations/platforms/anthropic/) et leurs modèles de chat Claude 3, mais LangChain propose également une [large gamme d'autres intégrations](https://python.langchain.com/docs/integrations/chat/) parmi lesquelles choisir, y compris des modèles OpenAI comme GPT-4.

```bash
pip install langchain_core langchain_anthropic
```

Si vous travaillez dans un notebook Jupyter, vous devrez préfixer `pip` avec un symbole `%` comme ceci : `%pip install langchain_core langchain_anthropic`.

Vous aurez également besoin d'une clé API Anthropic, que vous pouvez [obtenir ici](https://console.anthropic.com/) depuis leur console. Une fois que vous l'avez, définissez-la comme variable d'environnement nommée `ANTHROPIC_API_KEY` :

```python
export ANTHROPIC_API_KEY="..."
```

Vous pouvez également passer une clé directement dans le modèle si vous préférez.

## Premiers pas

Vous pouvez initialiser votre modèle comme ceci :

```python
from langchain_anthropic import ChatAnthropic

chat_model = ChatAnthropic(
    model="claude-3-sonnet-20240229",
    temperature=0
)

# Si vous préférez passer votre clé explicitement
# chat_model = ChatAnthropic(
#   model="claude-3-sonnet-20240229",
#   temperature=0,
#   api_key="VOTRE_CLE_ANTHROPIC_API_KEY"
# )
```

Le paramètre `model` est une chaîne qui correspond à l'un des [modèles supportés par Anthropic](https://docs.anthropic.com/claude/docs/models-overview#model-comparison). Au moment de l'écriture, Claude 3 Sonnet offre un bon équilibre entre vitesse, coût et capacité de raisonnement. 

`temperature` est une mesure de la quantité d'aléatoire que le modèle utilise pour générer des réponses. Pour la cohérence, dans ce tutoriel, nous la définissons à `0`, mais vous pouvez expérimenter avec des valeurs plus élevées pour des cas d'utilisation créatifs.

Maintenant, essayons de l'exécuter :

```python
chat_model.invoke("Raconte-moi une blague sur les ours !")
```

Voici la sortie :

```shell
AIMessage(content="Voici une blague sur les ours pour vous :\\n\\nPourquoi l'ours s'est-il dissous dans l'eau ?\\nParce que c'était un ours polaire !")
```

Vous pouvez voir que la sortie est quelque chose appelé un `AIMessage`. Cela est dû au fait que les modèles de chat utilisent des [messages de chat](https://python.langchain.com/docs/modules/model_io/chat/message_types/) comme entrée et sortie.

**Note :** Vous avez pu passer une simple chaîne comme entrée dans l'exemple précédent car LangChain accepte quelques formes de raccourcis pratiques qu'il convertit automatiquement au format approprié. Dans ce cas, une seule chaîne est transformée en un tableau avec un seul `HumanMessage`.

LangChain contient également des abstractions pour les LLMs de complétion de texte pur, qui sont des entrées de chaîne et des sorties de chaîne. Mais au moment de l'écriture, les variantes ajustées pour le chat ont dépassé les LLMs en popularité. Par exemple, GPT-4 et Claude 3 sont tous deux des modèles de chat.

Pour illustrer ce qui se passe, vous pouvez appeler ce qui précède avec une liste de messages plus explicite :

```python
from langchain_core.messages import HumanMessage

chat_model.invoke([
    HumanMessage("Raconte-moi une blague sur les ours !")
])
```

Et vous obtenez une sortie similaire :

```shell
AIMessage(content="Voici une blague sur les ours pour vous :\\n\\nPourquoi l'ours a-t-il apporté une mallette au travail ?\\nC'était un ours d'affaires !")
```

### Modèles de prompts

Les modèles sont utiles seuls, mais il est souvent pratique de paramétrer les entrées pour ne pas répéter le code standard. LangChain fournit des **[modèles de prompts](https://python.langchain.com/docs/modules/model_io/prompts/)** à cet effet. 

![Image](https://www.freecodecamp.org/news/content/images/2024/04/prompt_and_model--1-.png)
_Modèles de prompts dans LangChain_

Un exemple simple serait quelque chose comme ceci :

```python
from langchain_core.prompts import ChatPromptTemplate

joke_prompt = ChatPromptTemplate.from_messages([
    ("system", "Vous êtes un humoriste de classe mondiale."),
    ("human", "Raconte-moi une blague sur {topic}")
])
```

Vous pouvez appliquer le modèle en utilisant la même méthode `.invoke()` que pour les modèles de chat :

```python
joke_prompt.invoke({"topic": "betteraves"})
```

Voici le résultat :

```shell
ChatPromptValue(messages=[
    SystemMessage(content='Vous êtes un humoriste de classe mondiale.'),
    HumanMessage(content='Raconte-moi une blague sur les betteraves')
])
```

Passons en revue chaque étape :

* Vous construisez un modèle de prompt composé de modèles pour un `SystemMessage` et un `HumanMessage` en utilisant `from_messages`.
* Vous pouvez considérer les `SystemMessages` comme des méta-instructions qui ne font pas partie de la conversation actuelle, mais qui guident purement l'entrée.
* Le modèle de prompt contient `{topic}` entre accolades. Cela désigne un paramètre requis nommé `"topic"`.
* Vous invoquez le modèle de prompt avec un dictionnaire avec une clé nommée `"topic"` et une valeur `"betteraves"`.
* Le résultat contient les messages formatés.

Ensuite, vous apprendrez comment utiliser ce modèle de prompt avec votre modèle de chat.

## Chaînage

Vous avez peut-être remarqué que le modèle de prompt et le modèle de chat implémentent tous deux la méthode `.invoke()`. En termes de LangChain, ils sont tous deux des instances de **[Runnables](https://python.langchain.com/docs/expression_language/interface/)**.

Vous pouvez composer des Runnables en "chaînes" en utilisant l'opérateur pipe (`|`) où vous `.invoke()` l'étape suivante avec la sortie de la précédente. Voici un exemple :

```python
chain = joke_prompt | chat_model
```

La `chain` résultante est elle-même un Runnable et implémente automatiquement `.invoke()` (ainsi que plusieurs autres méthodes, comme nous le verrons plus tard). C'est la base du [LangChain Expression Language (LCEL)](https://python.langchain.com/docs/expression_language/get_started/).

Invoquons cette nouvelle chaîne :

```python
chain.invoke({"topic": "betteraves"})
```

La chaîne retourne une blague dont le sujet est les betteraves :

```shell
AIMessage(content="Voici une blague sur les betteraves pour vous :\\n\\nPourquoi la betterave a-t-elle rougi ? Parce qu'elle a vu la vinaigrette !")
```

Maintenant, supposons que vous souhaitiez travailler uniquement avec la sortie de chaîne brute du message. LangChain possède un composant appelé **[Output Parser](https://python.langchain.com/docs/modules/model_io/output_parsers/)**, qui, comme son nom l'indique, est responsable de l'analyse de la sortie d'un modèle dans un format plus accessible. Puisque les chaînes composées sont également des Runnables, vous pouvez à nouveau utiliser l'opérateur pipe :

```python
from langchain_core.output_parsers import StrOutputParser

str_chain = chain | StrOutputParser()

# Équivalent à :
# str_chain = joke_prompt | chat_model | StrOutputParser()
```

Super ! Maintenant, invoquons-la :

```python
str_chain.invoke({"topic": "betteraves"})
```

Et le résultat est maintenant une chaîne comme nous l'espérions :

```shell
"Voici une blague sur les betteraves pour vous :\\n\\nPourquoi la betterave a-t-elle rougi ? Parce qu'elle a vu la vinaigrette !"
```

Vous passez toujours `{"topic": "betteraves"}` en entrée à la nouvelle `str_chain` car le premier Runnable de la séquence est toujours le modèle de prompt que vous avez déclaré précédemment.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/prompt_model_and_output_parser--1-.png)
_Modèle de prompt et analyseur de sortie_

## Diffusion

L'un des plus grands avantages de composer des chaînes avec LCEL est l'expérience de diffusion. 

Tous les Runnables implémentent la méthode `.stream()` (et `.astream()` si vous travaillez dans des environnements asynchrones), y compris les chaînes. Cette méthode retourne un générateur qui produira une sortie dès qu'elle sera disponible, ce qui nous permet d'obtenir la sortie aussi rapidement que possible.

Bien que chaque Runnable implémente `.stream()`, tous ne supportent pas plusieurs morceaux. Par exemple, si vous appelez `.stream()` sur un modèle de prompt, il ne produira qu'un seul morceau avec la même sortie que `.invoke()`.

Vous pouvez itérer sur la sortie en utilisant la syntaxe `for ... in`. Essayez avec la `str_chain` que vous venez de déclarer :

```python
for chunk in str_chain.stream({"topic": "betteraves"}):
    print(chunk, end="|")
```

Et vous obtenez plusieurs chaînes en sortie (les morceaux sont séparés par un caractère `|` dans la fonction print) :

```shell
Voici| une| blague| sur| les| betteraves| pour| vous| :|

Pourquoi| la| betterave| a-t-elle| rougi| ?| Parce| qu'elle| a| vu| la| vinaigrette| !|
```

Les chaînes composées comme `str_chain` commenceront à diffuser dès que possible, ce qui dans ce cas est le modèle de chat dans la chaîne. 

Certains Output Parsers (comme le `StrOutputParser` utilisé ici) et de nombreux [Primitives](https://python.langchain.com/docs/expression_language/primitives/) de LCEL sont capables de traiter les morceaux diffusés des étapes précédentes au fur et à mesure qu'ils sont générés – agissant essentiellement comme des flux de transformation ou des passe-plats – et ne perturbent pas la diffusion.

## Comment guider la génération avec du contexte

Les LLMs sont formés sur de grandes quantités de données et ont une certaine connaissance innée de divers sujets. Cependant, il est courant de passer au modèle des données privées ou plus spécifiques comme contexte lors de la réponse pour obtenir des informations ou des insights utiles. Si vous avez déjà entendu le terme "RAG", ou "retrieval-augmented generation" auparavant, c'est le principe de base derrière cela.

L'un des exemples les plus simples de cela est de dire au LLM quelle est la date actuelle. Parce que les LLMs sont des instantanés de leur formation, ils ne peuvent pas déterminer nativement l'heure actuelle. Voici un exemple :

```python
chat_model = ChatAnthropic(model_name="claude-3-sonnet-20240229")

chat_model.invoke("Quelle est la date actuelle ?")
```

La réponse :

```shell
AIMessage(content="Malheureusement, je n'ai pas vraiment de concept de la date et de l'heure actuelles. En tant qu'assistant IA sans calendrier intégré, je n'ai pas de sens dynamique de la date actuelle. Je peux vous fournir la date d'aujourd'hui en fonction de quand j'ai reçu mes données de formation, mais cela peut ne pas refléter la date actuelle que vous demandez.")
```

Maintenant, voyons ce qui se passe lorsque vous donnez au modèle la date actuelle comme contexte :

```python
from datetime import date

prompt = ChatPromptTemplate.from_messages([
    ("system", 'Vous savez que la date actuelle est "{current_date}".'),
    ("human", "{question}")
])

chain = prompt | chat_model | StrOutputParser()

chain.invoke({
    "question": "Quelle est la date actuelle ?",
    "current_date": date.today()
})
```

Et vous pouvez voir, le modèle génère la date actuelle :

```shell
"La date actuelle est 2024-04-05."
```

Bien ! Maintenant, allons plus loin. Les modèles de langage sont formés sur de vastes quantités de données, mais ils ne savent pas tout. Voici ce qui se passe si vous demandez directement au modèle de chat une question très spécifique sur un restaurant local :

```python
chat_model.invoke(
    "Quel a été le chiffre d'affaires total de l'Old Ship Saloon au T1 2023 ?"
 )
```

Le modèle ne connaît pas la réponse nativement, ou même ne sait pas de quel Old Ship Saloon parmi les nombreux dans le monde nous parlons :

```shell
AIMessage(content="Je suis désolé, je n'ai aucune donnée financière spécifique sur le chiffre d'affaires de l'Old Ship Saloon au T1 2023. En tant qu'assistant IA sans accès aux registres internes du saloon, je n'ai pas d'informations sur leurs revenus projetés futurs. Je ne peux fournir des réponses basées que sur des informations factuelles qui m'ont été fournies.")
```

Cependant, si nous pouvons donner plus de contexte au modèle, nous pouvons le guider pour qu'il trouve une bonne réponse :

```python
SOURCE = """
Chiffres de revenus trimestriels 2023 de l'Old Ship Saloon :
T1 : 174 782,38 $
T2 : 467 372,38 $
T3 : 474 773,38 $
T4 : 389 289,23 $
"""

rag_prompt = ChatPromptTemplate.from_messages([
    ("system", 'Vous êtes un assistant utile. Utilisez le contexte suivant lors de la réponse :\n\n{context}.'),
    ("human", "{question}")
])

rag_chain = rag_prompt | chat_model | StrOutputParser()

rag_chain.invoke({
    "question": "Quel a été le chiffre d'affaires total de l'Old Ship Saloon au T1 2023 ?",
    "context": SOURCE
})
```

Cette fois, voici le résultat :

```shell
"Selon le contexte fourni, le chiffre d'affaires de l'Old Ship Saloon au T1 2023 était de 174 782,38 $."
```

Le résultat semble bon ! Notez que l'augmentation de la génération avec un contexte supplémentaire est un sujet très approfondi - dans le monde réel, cela prendrait probablement la forme d'un document financier plus long ou d'une partie d'un document récupéré depuis une autre source de données. Le RAG est une technique puissante pour répondre à des questions sur de grandes quantités d'informations.

Vous pouvez consulter la [documentation de LangChain sur la génération augmentée par récupération (RAG)](https://python.langchain.com/docs/use_cases/question_answering/) pour en savoir plus.

## Débogage

Parce que les LLMs sont non déterministes, il devient de plus en plus important de voir les internes de ce qui se passe à mesure que vos chaînes deviennent plus complexes.

LangChain dispose d'une méthode `set_debug()` qui retournera des logs plus granulaires des internes de la chaîne : voyons cela avec l'exemple précédent.

Tout d'abord, nous devons installer le package principal `langchain` pour l'entrée afin d'importer la méthode :

```python
%pip install langchain
```

Ensuite, ajoutez ce code :

```python
from langchain.globals import set_debug

set_debug(True)

from datetime import date

prompt = ChatPromptTemplate.from_messages([
    ("system", 'Vous savez que la date actuelle est "{current_date}".'),
    ("human", "{question}")
])

chain = prompt | chat_model | StrOutputParser()

chain.invoke({
    "question": "Quelle est la date actuelle ?",
    "current_date": date.today()
})
```

Il y a beaucoup plus d'informations !

```shell
[chain/start] [1:chain:RunnableSequence] Entrée dans l'exécution de la chaîne avec l'entrée :
[inputs]
[chain/start] [1:chain:RunnableSequence > 2:prompt:ChatPromptTemplate] Entrée dans l'exécution du prompt avec l'entrée :
[inputs]
[chain/end] [1:chain:RunnableSequence > 2:prompt:ChatPromptTemplate] [1ms] Sortie de l'exécution du prompt avec la sortie :
[outputs]
[llm/start] [1:chain:RunnableSequence > 3:llm:ChatAnthropic] Entrée dans l'exécution du LLM avec l'entrée :
{
  "prompts": [
    "System: Vous savez que la date actuelle est \\"2024-04-05\\".\\nHuman: Quelle est la date actuelle ?"
  ]
}
...
[chain/end] [1:chain:RunnableSequence] [885ms] Sortie de l'exécution de la chaîne avec la sortie :
{
  "output": "La date actuelle que vous avez fournie est 2024-04-05."
}
```

Vous pouvez consulter [ce guide](https://python.langchain.com/docs/guides/development/debugging/) pour plus d'informations sur le débogage.

Vous pouvez également utiliser la méthode `astream_events()` [méthode](https://python.langchain.com/docs/expression_language/streaming/#using-stream-events) pour retourner ces données. Cela est utile si vous souhaitez utiliser des étapes intermédiaires dans la logique de votre application. Notez que cette méthode est `async` et nécessite un drapeau `version` supplémentaire puisqu'elle est encore en bêta :

```python
# Désactiver le mode débogage pour plus de clarté
set_debug(False)

stream = chain.astream_events({
    "question": "Quelle est la date actuelle ?",
    "current_date": date.today()
}, version="v1")

async for event in stream:
    print(event)
    print("-----")
```

```shell
{'event': 'on_chain_start', 'run_id': '90785a49-987e-46bf-99ea-d3748d314759', 'name': 'RunnableSequence', 'tags': [], 'metadata': {}, 'data': {'input': {'question': 'Quelle est la date actuelle ?', 'current_date': datetime.date(2024, 4, 5)}}}
-----
{'event': 'on_prompt_start', 'name': 'ChatPromptTemplate', 'run_id': '54b1f604-6b2a-48eb-8b4e-c57a66b4c5da', 'tags': ['seq:step:1'], 'metadata': {}, 'data': {'input': {'question': 'Quelle est la date actuelle ?', 'current_date': datetime.date(2024, 4, 5)}}}
-----
{'event': 'on_prompt_end', 'name': 'ChatPromptTemplate', 'run_id': '54b1f604-6b2a-48eb-8b4e-c57a66b4c5da', 'tags': ['seq:step:1'], 'metadata': {}, 'data': {'input': {'question': 'Quelle est la date actuelle ?', 'current_date': datetime.date(2024, 4, 5)}, 'output': ChatPromptValue(messages=[SystemMessage(content='Vous savez que la date actuelle est "2024-04-05".'), HumanMessage(content='Quelle est la date actuelle ?')])}
-----
{'event': 'on_chat_model_start', 'name': 'ChatAnthropic', 'run_id': 'f5caa4c6-1b51-49dd-b304-e9b8e176623a', 'tags': ['seq:step:2'], 'metadata': {}, 'data': {'input': {'messages': [[SystemMessage(content='Vous savez que la date actuelle est "2024-04-05".'), HumanMessage(content='Quelle est la date actuelle ?')]]}}}
-----
...
{'event': 'on_chain_end', 'name': 'RunnableSequence', 'run_id': '90785a49-987e-46bf-99ea-d3748d314759', 'tags': [], 'metadata': {}, 'data': {'output': 'La date actuelle est 2024-04-05.'}}
-----
```

Enfin, vous pouvez utiliser un service externe comme [LangSmith](https://smith.langchain.com) pour ajouter du traçage. Voici un exemple :

```python
# Inscrivez-vous sur <https://smith.langchain.com/>
# Définissez les variables d'environnement

# import os

# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_API_KEY"] = "VOTRE_CLE"
# os.environ["LANGCHAIN_PROJECT"] = "VOTRE_PROJET"

chain.invoke({
  "question": "Quelle est la date actuelle ?",
  "current_date": date.today()
})
```

```shell
"La date actuelle est 2024-04-05."
```

LangSmith capturera les internes à chaque étape, vous donnant un résultat [comme celui-ci](https://smith.langchain.com/public/628a15bb-45c8-4d39-987a-2896684a66c2/r).

Vous pouvez également ajuster les prompts et relancer les appels de modèle dans un bac à sable. En raison de la nature non déterministe des LLMs, vous pouvez également ajuster les prompts et relancer les appels de modèle dans un bac à sable, ainsi que créer des jeux de données et des cas de test pour évaluer les changements de votre application et détecter les régressions.

## Merci !

Vous avez maintenant appris les bases de :

* Les composants [Chat Model](https://python.langchain.com/docs/modules/model_io/chat/), [Prompt Template](https://python.langchain.com/docs/modules/model_io/prompts/), et [Output Parser](https://python.langchain.com/docs/modules/model_io/output_parsers/) de LangChain
* Comment enchaîner des composants avec diffusion.
* Utiliser des informations externes pour guider la génération du modèle.
* Comment déboguer les internes de vos chaînes.

Et si vous souhaitez en savoir plus sur la génération augmentée par récupération (RAG), voici un [cours RAG à partir de zéro sur la chaîne YouTube de freeCodeCamp](https://www.youtube.com/watch?v=sVcwVQRHIc8).

Consultez les ressources suivantes pour continuer votre voyage dans l'IA générative :

* [Documentation Python de LangChain](https://python.langchain.com/)
* [Chaîne YouTube de LangChain](https://www.youtube.com/@LangChain)

Vous pouvez également suivre LangChain sur X (anciennement Twitter) [@LangChainAI](https://twitter.com/LangChainAI) pour les dernières nouvelles, ou moi [@Hacubu](https://x.com/hacubu/).

Bon prompt !