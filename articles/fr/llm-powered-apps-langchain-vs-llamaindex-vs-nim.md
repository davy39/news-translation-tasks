---
title: 'Quels outils utiliser pour les applications alimentées par LLM : LangChain
  vs LlamaIndex vs NIM'
subtitle: ''
author: Bhavishya Pandit
co_authors: []
series: null
date: '2024-10-21T17:34:21.746Z'
originalURL: https://freecodecamp.org/news/llm-powered-apps-langchain-vs-llamaindex-vs-nim
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1729527716896/58932669-914c-4380-88c8-33ffbad99b5f.webp
tags:
- name: 'LLM''s '
  slug: llms
- name: large language models
  slug: large-language-models
- name: AI
  slug: ai
- name: Machine Learning
  slug: machine-learning
seo_title: 'Quels outils utiliser pour les applications alimentées par LLM : LangChain
  vs LlamaIndex vs NIM'
seo_desc: 'If you’re considering building an application powered by a Large Language
  Model, you may wonder which tool to use.

  Well, two well-established frameworks—LangChain and LlamaIndex—have gained significant
  attention for their unique features and capabili...'
---

Si vous envisagez de construire une application alimentée par un grand modèle de langage, vous vous demandez peut-être quel outil utiliser.

Eh bien, deux frameworks bien établis, LangChain et LlamaIndex, ont attiré une attention significative pour leurs caractéristiques et capacités uniques. Mais récemment, NVIDIA NIM a émergé comme un nouveau joueur dans le domaine, ajoutant ses outils et fonctionnalités au mélange.

Dans cet article, nous allons comparer LangChain, LlamaIndex et NVIDIA NIM pour vous aider à déterminer quel framework convient le mieux à votre cas d'utilisation spécifique.

## **Table des matières :**

1. [Introduction à LangChain](#heading-introduction-a-langchain)
    
2. [Introduction à LlamaIndex](#heading-introduction-a-llamaindex)
    
3. [NVIDIA NIM](#heading-nvidia-nim)
    
4. [Quel outil utiliser](#heading-quel-outil-utiliser)?
    
5. [Conclusion](#heading-conclusion)
    

## **Introduction à LangChain**

Selon la documentation officielle de LangChain, « LangChain est un framework pour développer des applications alimentées par des modèles de langage ».

Nous pouvons élargir un peu cela et dire que LangChain est un framework polyvalent conçu pour construire des applications basées sur des données et des agents. Il offre une collection de composants et de chaînes pré-construites qui simplifient le travail avec les grands modèles de langage (LLM) comme GPT.

Que vous débutiez ou que vous soyez un développeur expérimenté, LangChain prend en charge à la fois le prototypage rapide et les applications de production à grande échelle.

Vous pouvez utiliser LangChain pour simplifier l'ensemble du cycle de développement d'une application LLM :

* **Développement :** LangChain offre des blocs de construction open-source, des composants et des intégrations tierces pour construire des applications.
    
* **Production :** LangSmith, un outil de LangChain, aide à surveiller et à évaluer les chaînes pour une optimisation et un déploiement continus.
    
* **Déploiement :** Vous pouvez utiliser LangGraph Cloud pour transformer vos applications LLM en API prêtes pour la production.
    

LangChain offre plusieurs bibliothèques open-source pour le développement et la production. Jetons un coup d'œil à certaines d'entre elles.

### **Composants de LangChain**

Les composants de LangChain sont des API de haut niveau qui simplifient le travail avec les LLM. Vous pouvez les comparer aux Hooks dans React et aux fonctions dans Python.

Ces composants sont conçus pour être intuitifs et faciles à utiliser. Un composant clé est l'interface LLM, qui se connecte de manière transparente à des fournisseurs comme OpenAI, Cohere et Hugging Face, vous permettant d'interroger facilement les modèles.

Dans cet exemple, nous utilisons la bibliothèque langchain_google_vertexai pour interagir avec Google Vertex AI, en utilisant spécifiquement le modèle **Gemini 1.5 Flash**. Décomposons ce que fait le code :

```python
from langchain_google_vertexai import ChatVertexAI

llm = ChatVertexAI(model="gemini-1.5-flash")
llm.invoke(
  "Qui était Napoléon ?"
)
```

**Importation de la classe ChatVertexAI :**

La première étape consiste à importer la classe ChatVertexAI, qui nous permet de communiquer avec la plateforme **Google Vertex AI**. Cette bibliothèque fait partie de l'écosystème LangChain, conçue pour intégrer de manière transparente les grands modèles de langage (LLM) dans les applications.

**Instanciation du LLM (Grand Modèle de Langage) :**

```python
llm = ChatVertexAI(model="gemini-1.5-flash")
```

Ici, nous créons une instance de la classe ChatVertexAI. Nous spécifions le modèle que nous voulons utiliser, qui dans ce cas est **Gemini 1.5 Flash**. Cette version de Gemini est optimisée pour des réponses rapides tout en maintenant une génération de langage de haute qualité.

**Envoyer une requête au modèle :**

```python
llm.invoke("Qui était Napoléon ?")

```

Enfin, nous utilisons la méthode invoke pour envoyer une question au modèle Gemini. Dans cet exemple, nous posons la question, **« Qui était Napoléon ? »**. Le modèle traite la requête et fournit une réponse, qui inclurait généralement des informations sur l'identité de Napoléon, son importance historique et ses principales réalisations.

### **Chaînes**

LangChain définit les chaînes comme des « séquences d'appels ». Pour comprendre comment fonctionnent les chaînes, nous devons savoir ce qu'est LCEL.

LCEL signifie LangChain Expression Language, qui est un moyen déclaratif de composer facilement des chaînes ensemble – c'est tout. LCEL nous aide simplement à combiner plusieurs chaînes en de longues chaînes.

LangChain prend en charge deux types de chaînes

1. Chaînes LCEL : Dans ce cas, LangChain offre une méthode de constructeur de niveau supérieur. Mais tout ce qui est fait sous le capot est la construction d'une chaîne avec LCEL.

    Par exemple, [create_stuff_documents_chain](https://api.python.langchain.com/en/latest/chains/langchain.chains.combine_documents.stuff.create_stuff_documents_chain.html#langchain.chains.combine_documents.stuff.create_stuff_documents_chain) est une chaîne LCEL qui prend une liste de documents et les formate tous dans une invite, puis transmet cette invite à un LLM. Elle transmet TOUS les documents, vous devez donc vous assurer qu'ils rentrent dans la fenêtre de contexte du LLM que vous utilisez.
    
2. Chaînes héritées : Les chaînes héritées sont construites en sous-classant une classe *Chain* héritée. Ces chaînes n'utilisent pas LCEL sous le capot mais sont des classes autonomes.

    Par exemple, [APIChain](https://api.python.langchain.com/en/latest/chains/langchain.chains.api.base.APIChain.html#langchain.chains.api.base.APIChain) : cette chaîne utilise un LLM pour convertir une requête en une demande d'API, puis exécute cette demande, obtient une réponse, et transmet ensuite cette demande à un LLM pour répondre.

Les chaînes héritées étaient des pratiques standard avant LCEL. Une fois que toutes les chaînes héritées auront une alternative LCEL, elles deviendront obsolètes et non prises en charge.

### **Guide de démarrage rapide de LangChain**

```python
!pip install -U langchain-google-genai

%env GOOGLE_API_KEY="votre-cle-api"

from langchain_google_genai import ChatGoogleGenerativeAI
```

#### **1. Utilisation de LangChain avec le modèle Gemini Pro de Google**

Ce code démontre comment intégrer le modèle Gemini Pro de Google avec LangChain pour des tâches de traitement du langage naturel.

```python
pip install -U langchain-google-genai
```

Tout d'abord, installez le package langchain-google-genai, qui vous permet d'interagir avec les modèles d'IA générative de Google via LangChain. Le drapeau -U garantit que vous obtenez la dernière version.

#### **2. Configuration de votre clé API**

```python
%env GOOGLE_API_KEY="votre-cle-api"
```

Vous devez authentifier vos requêtes API. Utilisez votre clé API Google en la définissant comme variable d'environnement. Cela garantit une communication sécurisée avec les services de Google.

#### **3. Accès au modèle Gemini Pro**

```python
from langchain_google_genai import ChatGoogleGenerativeAI
```

La classe ChatGoogleGenerativeAI est importée du package langchain-google-genai. Nous l'instancions, en spécifiant **Gemini Pro** — une version puissante des modèles génératifs de Google connue pour produire des sorties linguistiques de haute qualité.

#### **4. Interrogation du modèle**

```python
llm = ChatGoogleGenerativeAI(model="gemini-pro")
llm.invoke("Qui était Alexandre le Grand ?")
```

Enfin, vous invoquez le modèle en passant une requête. Dans cet exemple, la requête demande des informations sur **Alexandre le Grand**. Le modèle retournera une réponse détaillée, telle que son contexte historique et son importance.

## **Introduction à LlamaIndex**

LlamaIndex, précédemment connu sous le nom de GPT Index, est un framework de données conçu pour les applications de grands modèles de langage (LLM). Son objectif principal est d'ingérer, d'organiser et d'accéder à des données privées ou spécifiques à un domaine, offrant une suite d'outils qui simplifient l'intégration de telles données dans les LLM.

En termes simples, les LLM sont des modèles très puissants mais ils ne fonctionnent pas aussi bien lorsqu'ils sont utilisés avec de petits ensembles de données. LlamaIndex nous aide à intégrer nos données dans les LLM pour répondre à des besoins spécifiques.

LlamaIndex fonctionne en utilisant plusieurs composants ensemble. Examinons-les un par un.

### **Connecteurs de données**

LlamaIndex prend en charge l'ingestion de données à partir de plusieurs sources, telles que des API, des PDF et des bases de données SQL. Ces connecteurs rationalisent le processus d'intégration de données externes dans des applications basées sur des LLM.

```python
from llama_index.core import VectorStoreIndex, download_loader

from llama_index.readers.google import GoogleDocsReader

gdoc_ids = ["votre-id-google_doc"]
loader = GoogleDocsReader()

documents = loader.load_data(document_ids=gdoc_ids)
index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()
query_engine.query("Où l'auteur est-il allé à l'école ?")
```

Ce code utilise LlamaIndex pour charger et interroger des Google Docs. Il importe les classes nécessaires, spécifie les identifiants des Google Docs et charge le contenu du document à l'aide de GoogleDocsReader. Le contenu est ensuite indexé sous forme de vecteurs avec VectorStoreIndex, permettant une interrogation efficace. Enfin, il crée un moteur de requête pour récupérer des réponses à partir des documents indexés en fonction de questions en langage naturel, telles que "Où l'auteur est-il allé à l'école ?"

### **Indexation des données**

Le framework organise les données ingérées dans des formats intermédiaires conçus pour optimiser la manière dont les LLM accèdent et traitent les informations, garantissant à la fois l'efficacité et les performances.

Les index sont construits à partir de documents. Ils sont utilisés pour construire des moteurs de requête et des moteurs de chat qui permettent des questions et réponses ainsi que des discussions sur les données. Dans LlamaIndex, les index stockent les données dans des objets **Node**. Selon la documentation :

> « Un Node correspond à un morceau de texte d'un Document. LlamaIndex prend des objets Document et les analyse/découpe en interne en objets Node. » ([Source](https://docs.llamaindex.ai/en/stable/module_guides/indexing/index_guide/))

### **Moteurs**

LlamaIndex inclut divers moteurs pour interagir avec les données via le langage naturel. Ceux-ci incluent des moteurs pour interroger les connaissances, faciliter les interactions conversationnelles et des agents de données qui améliorent les flux de travail alimentés par les LLM.

### **Avantages de LlamaIndex**

* Facilite l'importation de données provenant de différentes sources, telles que des API, des PDF et des bases de données comme SQL/NoSQL, pour être utilisées dans des applications alimentées par des grands modèles de langage (LLM).
    
* Vous permet de stocker et d'organiser des données privées, les rendant prêtes pour différents usages, tout en travaillant en douceur avec des magasins de vecteurs et des bases de données.
    
* Dispose d'une fonction de requête intégrée qui vous permet d'obtenir des réponses intelligentes et basées sur les données en fonction de votre entrée.
    

### **Guide de démarrage rapide de LlamaIndex**

Dans cette section, vous apprendrez à utiliser **LlamaIndex** pour créer un index interrogeable à partir d'une collection de documents et interagir avec l'API d'OpenAI à des fins d'interrogation. Voici le code pour le faire :

```python
pip install llama-index
%env OPENAI_API_KEY = "votre-cle-api"

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
```

Maintenant, décomposons-le étape par étape :

#### 1. **Installer le package LlamaIndex**

```python
pip install llama-index
```

Vous commencez par installer le package llama-index, qui fournit des outils pour construire des index de documents basés sur des vecteurs permettant des requêtes en langage naturel.

#### **2. Définir la clé API OpenAI**

```python
%env OPENAI_API_KEY = "votre-cle-api"
```

Ici, la clé API OpenAI est définie comme une variable d'environnement pour authentifier et permettre la communication avec l'API d'OpenAI. Remplacez "votre-cle-api" par votre clé API réelle.

#### **3. Importer les composants nécessaires**

```python
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
```

La classe VectorStoreIndex est utilisée pour créer un index qui stockera des vecteurs représentant le contenu des documents, tandis que la classe SimpleDirectoryReader est utilisée pour lire des documents à partir d'un répertoire spécifié.

#### **4. Charger les documents**

```python
documents = SimpleDirectoryReader("data").load_data()
```

Le SimpleDirectoryReader charge les documents à partir du répertoire nommé "data". La méthode load_data() lit le contenu et le traite afin qu'il puisse être utilisé pour créer l'index.

#### **5. Créer l'index Vector Store**

```python
index = VectorStoreIndex.from_documents(documents)
```

Un VectorStoreIndex est créé à partir des documents. Cet index convertit le texte en intégrations vectorielles qui capturent la signification sémantique du texte, facilitant ainsi l'interprétation et l'interrogation par les modèles d'IA.

#### **6. Construire le moteur de requête**

```python
query_engine = index.as_query_engine()
```

Le moteur de requête est créé en convertissant l'index du magasin de vecteurs dans un format qui peut être interrogé. Ce moteur est le composant qui vous permet d'exécuter des requêtes en langage naturel contre l'index de documents.

#### **7. Interroger le moteur**

```python
response = query_engine.query("Qui est le protagoniste dans l'histoire ?")
```

Ici, une requête est faite à l'index demandant le protagoniste de l'histoire. Le moteur de requête traite la demande et utilise les intégrations de documents pour récupérer les informations les plus pertinentes des documents indexés.

#### **8. Afficher la réponse**

Enfin, la réponse du moteur de requête, qui contient la réponse à la requête, est imprimée.

Assurez-vous que votre structure de répertoire ressemble à ceci :

<table><tbody><tr><td colspan="1" rowspan="1"><p>|----- main.py<br>|----- data<br>&nbsp; &nbsp; &nbsp; &nbsp; |----- Matilda.txt</p></td></tr></tbody></table>

## **NVIDIA NIM**

Nvidia a récemment lancé son propre ensemble d'outils pour développer des applications LLM appelés NIM. NIM signifie **« Nvidia Inference Microservice ».**

NVIDIA NIM est une collection d'outils simples (microservices) qui aident à configurer et à exécuter rapidement des modèles d'IA sur le cloud, dans des centres de données ou sur des stations de travail.

Les NIM sont organisés par type de modèle. Par exemple, NVIDIA NIM pour les grands modèles de langage (LLM) facilite l'utilisation par les entreprises de modèles de langage avancés pour des tâches telles que la compréhension et le traitement du langage naturel.

### **Comment fonctionnent les NIM**

Lors de la première configuration d'un NIM, il vérifie votre matériel et trouve la meilleure version du modèle dans sa bibliothèque pour correspondre à votre système.

Si vous avez certains GPU NVIDIA (listés dans la Matrice de Support), NIM téléchargera et utilisera une version optimisée du modèle avec la bibliothèque TRT-LLM pour des performances rapides. Pour les autres GPU NVIDIA, il téléchargera un modèle non optimisé et l'exécutera en utilisant la bibliothèque vLLM.

L'idée principale est donc de fournir des modèles d'IA optimisés pour un développement local plus rapide et un environnement cloud pour l'héberger en production.

![Flux de démarrage d'un serveur REST API utilisant Nvidia NIM.](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcFaoW3vnIQUTqz9mpYGkO7r2JqD2P7ZMg_W4GE0a9KL_Dfm7j9fBXYlWCMJsuAPJufoxQ9xmwxb6ori54o9SGR0IkTxr5SZluSNu4LILK_6WGkImb7_EwHcwTalFxaaZmFtd4Qe-5n7MDF8N8tLL2D0a52?key=Cq76nL_EGCQTxNOs8pe9wg align="left")

### **Fonctionnalités de NIM**

NIM simplifie le processus d'exécution des modèles d'IA en gérant les détails techniques comme les moteurs d'exécution et les opérations d'exécution pour vous. C'est aussi l'option la plus rapide, que ce soit en utilisant TRT-LLM, vLLM ou d'autres méthodes.

NIM offre les fonctionnalités haute performance suivantes :

* **Déploiement scalable :** Il fonctionne bien et peut facilement passer de la gestion de quelques utilisateurs à des millions sans problème.
    
* **Support de modèles de langage avancés :** NIM est livré avec des moteurs pré-optimisés pour diverses conceptions de modèles de langage les plus récentes.
    
* **Intégration flexible :** L'ajout de NIM à vos applications et flux de travail existants est facile. Les développeurs peuvent utiliser un système compatible avec l'API OpenAI avec des fonctionnalités NVIDIA supplémentaires pour plus de capacités.
    
* **Sécurité de niveau entreprise :** NIM donne la priorité à la sécurité en utilisant des safetensors, en surveillant en continu les vulnérabilités (CVE) et en appliquant régulièrement des mises à jour de sécurité.
    

### **Guide de démarrage rapide de NIM**

#### 1. Générer une clé API NGC

Une clé API NGC est requise pour accéder aux ressources NGC et une clé peut être générée ici : [https://org.ngc.nvidia.com/setup/personal-keys](https://org.ngc.nvidia.com/setup/personal-keys).

#### 2. Exporter la clé API

```python
export NGC_API_KEY=<valeur>
```

#### 3. Connexion Docker à NGC

Pour extraire l'image du conteneur NIM de NGC, authentifiez-vous d'abord auprès du registre de conteneurs NVIDIA avec la commande suivante :

```python
echo "$NGC_API_KEY" | docker login nvcr.io --username '$oauthtoken' --password-stdin
```

#### 4. Lister les NIM disponibles

```python
ngc registry image list --format_type csv nvcr.io/nim/*
```

#### 5. Lancer NIM

La commande suivante lance un conteneur Docker pour le modèle llama3-8b-instruct. Pour lancer un conteneur pour un autre NIM, remplacez les valeurs de Repository et Latest_Tag par les valeurs de la commande de liste d'images précédente et changez la valeur de CONTAINER_NAME en quelque chose d'approprié.

```dockerfile
# Choisir un nom de conteneur pour la comptabilité
export CONTAINER_NAME=Llama3-8B-Instruct

# Le nom du conteneur de la commande précédente ngc registry image list
Repository=nim/meta/llama3-8b-instruct
Latest_Tag=1.1.2

# Choisir une image NIM LLM de NGC
export IMG_NAME="nvcr.io/${Repository}:${Latest_Tag}"

# Choisir un chemin sur votre système pour mettre en cache les modèles téléchargés
export LOCAL_NIM_CACHE=~/.cache/nim
mkdir -p "$LOCAL_NIM_CACHE"

# Démarrer le NIM LLM
docker run -it --rm --name=$CONTAINER_NAME \

 --runtime=nvidia \

 --gpus all \

 --shm-size=16GB \

 -e NGC_API_KEY=$NGC_API_KEY \

 -v "$LOCAL_NIM_CACHE:/opt/nim/.cache" \

 -u $(id -u) \

 -p 8000:8000 \

 $IMG_NAME
```

6. Cas d'utilisation : Demande de complétion OpenAI

```python
from openai import OpenAI

client = OpenAI(base_url="http://0.0.0.0:8000/v1", api_key="not-used")
prompt = "Il était une fois"
response = client.completions.create(
    model="meta/llama3-8b-instruct",
    prompt=prompt,
    max_tokens=16,
    stream=False
)
completion = response.choices[0].text
print(completion)
```

## **Quel outil utiliser ?**

Vous vous demandez peut-être : lequel de ces outils utiliser pour votre cas d'utilisation spécifique ? Eh bien, la réponse à cette question dépend de ce sur quoi vous travaillez.

LangChain est un excellent choix si vous cherchez un framework polyvalent pour intégrer plusieurs outils ou construire des agents intelligents capables de gérer plusieurs tâches simultanément.

Mais si votre principal objectif est la recherche intelligente et la récupération de données, LlamaIndex est la meilleure option, car il se spécialise dans l'indexation et la récupération d'informations pour les LLM, ce qui le rend idéal pour l'exploration approfondie de données. Bien que LangChain puisse gérer l'indexation et la récupération, LlamaIndex est optimisé pour ces tâches et offre une ingestion de données plus facile avec ses plugins et connecteurs.

D'autre part, si vous visez un déploiement de modèle haute performance, NVIDIA NIM est une excellente solution. NIM abstrait les détails techniques, offre une inférence rapide avec des outils comme TRT-LLM et vLLM, et fournit un déploiement scalable avec une sécurité de niveau entreprise.

Ainsi, pour les applications nécessitant une indexation et une récupération, LlamaIndex est recommandé. Pour déployer des LLM à grande échelle, NIM est un choix puissant. Sinon, LangChain seul est suffisant pour travailler avec les LLM.

## **Conclusion**

Dans cet article, nous avons comparé trois outils puissants pour travailler avec des grands modèles de langage : LangChain, LlamaIndex et NVIDIA NIM. Nous avons exploré les forces uniques de chaque outil, telles que la polyvalence de LangChain pour intégrer plusieurs composants, l'accent mis par LlamaIndex sur l'indexation et la récupération efficaces des données, et les capacités de déploiement de modèles haute performance de NVIDIA NIM.

Nous avons discuté des caractéristiques clés comme la scalabilité, la facilité d'intégration et les performances optimisées, montrant comment ces outils répondent à différents besoins au sein de l'écosystème de l'IA.

Bien que chaque outil ait ses défis, tels que la gestion d'infrastructures complexes ou l'optimisation pour des tâches spécifiques, LangChain, LlamaIndex et NVIDIA NIM offrent des solutions précieuses pour construire et mettre à l'échelle des applications alimentées par l'IA.