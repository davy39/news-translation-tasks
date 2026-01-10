---
title: Comment utiliser LangChain et GPT pour analyser plusieurs documents
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2024-11-06T16:06:55.422Z'
originalURL: https://freecodecamp.org/news/how-to-use-langchain-and-gpt-to-analyze-multiple-documents
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1730909200914/e75f3725-7453-49c0-b4e9-8b14fbc3b783.jpeg
tags:
- name: generative ai
  slug: generative-ai
- name: langchain
  slug: langchain
- name: Python
  slug: python
seo_title: Comment utiliser LangChain et GPT pour analyser plusieurs documents
seo_desc: 'Over the past year or so, the developer universe has exploded with ingenious
  new tools, applications, and processes for working with large language models and
  generative AI.

  One particularly versatile example is the LangChain project. The overall goa...'
---

Au cours de l'année écoulée, l'univers des développeurs a explosé avec de nouveaux outils, applications et processus ingénieux pour travailler avec des modèles de langage de grande taille et l'IA générative.

Un exemple particulièrement polyvalent est [le projet LangChain](https://www.langchain.com/). L'objectif global est de fournir des intégrations faciles avec divers modèles LLM. Mais l'écosystème LangChain abrite également un nombre croissant de projets (parfois expérimentaux) repoussant les limites des modèles LLM.

Passez du temps à parcourir [le site web de LangChain](https://www.langchain.com/) pour vous faire une idée de ce qui est possible. Vous verrez combien d'outils sont conçus pour vous aider à construire des applications plus puissantes.

Mais vous pouvez également l'utiliser comme une alternative pour connecter votre IA préférée à Internet en direct. Plus précisément, cette démonstration vous montrera comment l'utiliser pour accéder, résumer et analyser de manière programmatique des documents en ligne longs et complexes.

Pour que tout cela se réalise, vous aurez besoin d'un environnement d'exécution Python (comme Jupyter Lab) et d'une clé API OpenAI valide.

### Préparez votre environnement

Une utilisation populaire de LangChain consiste à charger plusieurs fichiers PDF en parallèle et à demander à GPT d'analyser et de comparer leur contenu.

Comme vous pouvez le constater vous-même dans [la documentation de LangChain](https://python.langchain.com/docs/integrations/toolkits/document_comparison_toolkit), des modules existants peuvent être chargés pour permettre la consommation de PDF et l'analyse de texte en langage naturel. Je vais vous guider à travers un exemple d'utilisation qui est vaguement basé sur l'exemple de cette documentation. Voici comment cela commence :

```python
import os
os.environ['OPENAI_API_KEY'] = "sk-xxx"
from pydantic import BaseModel, Field
from langchain.chat_models import ChatOpenAI
from langchain.agents import Tool
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader
from langchain.chains import RetrievalQA
```

Ce code construira votre environnement et configura les outils nécessaires pour :

* Activer le chat OpenAI (ChatOpenAI)

* Comprendre et traiter le texte (OpenAIEmbeddings, CharacterTextSplitter, FAISS, RetrievalQA)

* Gérer un agent IA (Tool)

Ensuite, vous créerez et définirez une classe `DocumentInput` et une valeur appelée `llm` qui définit certains paramètres familiers de GPT qui seront appelés plus tard :

```python
class DocumentInput(BaseModel):
    question: str = Field()
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")
```

### Chargez vos documents

Ensuite, vous créerez quelques tableaux. Les trois variables `path` dans le tableau `files` contiennent les URL des rapports financiers récents émis par trois entreprises de logiciels/services informatiques : Alphabet (Google), Cisco et IBM.

Nous allons faire en sorte que GPT plonge dans les données de ces trois entreprises simultanément, que l'IA compare les résultats et que tout cela se fasse sans avoir à télécharger les PDF dans un environnement local.

Vous pouvez généralement trouver de tels dépôts légaux dans la section Relations avec les investisseurs du site web d'une entreprise.

```python
tools = []
files = [
    {
        "name": "alphabet-earnings",
        "path": "https://abc.xyz/investor/static/pdf/2023Q1\
        _alphabet_earnings_release.pdf",
    },
    {
        "name": "Cisco-earnings",
        "path": "https://d18rn0p25nwr6d.cloudfront.net/CIK-00\
            00858877/5b3c172d-f7a3-4ecb-b141-03ff7af7e068.pdf",
    },
    {
        "name": "IBM-earnings",
        "path": "https://www.ibm.com/investor/att/pdf/IBM_\
            Annual_Report_2022.pdf",
    },
    ]
```

Cette boucle `for` va itérer à travers chaque valeur du tableau `files` que je viens de vous montrer. Pour chaque itération, elle utilisera `PyPDFLoader` pour charger le fichier PDF spécifié, `loader` et `CharacterTextSplitter` pour analyser le texte, et les outils restants pour organiser les données et appliquer les embeddings. Elle invoquera ensuite la classe `DocumentInput` que nous avons créée précédemment :

```python
for file in files:
    loader = PyPDFLoader(file["path"])
    pages = loader.load_and_split()
    text_splitter = CharacterTextSplitter(chunk_size=1000, \
        chunk_overlap=0)
    docs = text_splitter.split_documents(pages)
    embeddings = OpenAIEmbeddings()
    retriever = FAISS.from_documents(docs, embeddings).as_retriever()
# Wrap retrievers in a Tool
tools.append(
    Tool(
        args_schema=DocumentInput,
        name=file["name"],
        func=RetrievalQA.from_chain_type(llm=llm, \
            retriever=retriever),
    )
)
```

### Interrogez votre modèle

À ce stade, nous sommes enfin prêts à créer un agent et à lui fournir notre prompt en tant qu'`input`.

```python
llm = ChatOpenAI(
    temperature=0,
    model="gpt-3.5-turbo-0613",
)
agent = initialize_agent(
    agent=AgentType.OPENAI_FUNCTIONS,
    tools=tools,
    llm=llm,
    verbose=True,
)
    agent({"input": "Based on these SEC filing documents, identify \
        which of these three companies - Alphabet, IBM, and Cisco \
        has the greatest short-term debt levels and which has the \
        highest research and development costs."})
```

La sortie que j'ai obtenue était courte et précise :

> 'output' : 'Based on the SEC filing documents:\\n\\n- The company with the greatest short-term debt levels is IBM, with a short-term debt level of $4,760 million.\\n- The company with the highest research and development costs is Alphabet, with research and development costs of $11,468 million.'

### Conclusion

Comme vous l'avez vu, LangChain vous permet d'intégrer plusieurs outils dans des opérations d'IA générative, permettant un accès programmatique multicouche à Internet en direct et des prompts LLM plus sophistiqués.

Avec ces outils, vous serez en mesure d'automatiser l'application de la puissance des moteurs d'IA à des actifs de données du monde réel en temps réel. Essayez-le par vous-même.

*Cet article est extrait de* [*mon livre Manning, The Complete Obsolete Guide to Generative AI*](https://www.amazon.com/dp/1633436985)*. Mais vous pouvez trouver beaucoup plus de bonnes choses technologiques sur* [*mon site web*](https://bootstrap-it.com/)*.*