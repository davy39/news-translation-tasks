---
title: 'Comment construire votre propre IA locale : Créer des RAG et des agents IA
  gratuits avec Qwen 3 et Ollama'
subtitle: ''
author: Chaitanya Rahalkar
co_authors: []
series: null
date: '2025-05-06T16:16:20.113Z'
originalURL: https://freecodecamp.org/news/build-a-local-ai
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1746545253944/58b04b54-e443-4804-bedd-3290bfda5bb7.png
tags:
- name: Python
  slug: python
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: learning
  slug: learning
- name: Machine Learning
  slug: machine-learning
seo_title: 'Comment construire votre propre IA locale : Créer des RAG et des agents
  IA gratuits avec Qwen 3 et Ollama'
seo_desc: 'The landscape of Artificial Intelligence is rapidly evolving, and one of
  the most exciting trends is the ability to run powerful Large Language Models (LLMs)
  directly on your local machine.

  This shift away from reliance on cloud-based APIs offers sig...'
---

Le paysage de l'intelligence artificielle évolue rapidement, et l'une des tendances les plus passionnantes est la possibilité d'exécuter des modèles de langage puissants (LLM) directement sur votre machine locale.

Ce passage à l'indépendance vis-à-vis des API basées sur le cloud offre des avantages significatifs en termes de confidentialité, de rentabilité et d'accessibilité hors ligne. Les développeurs et les passionnés peuvent désormais expérimenter et déployer des capacités d'IA sophistiquées sans envoyer de données à l'extérieur ou engendrer de frais d'API.

Ce tutoriel sert de guide pratique et concret pour exploiter cette puissance de l'IA locale. Il se concentre sur l'utilisation de la famille de modèles Qwen 3, une offre open-source de pointe d'Alibaba, combinée à Ollama, un outil qui simplifie considérablement l'exécution des LLM localement.

## Prérequis

Avant de plonger dans ce tutoriel, vous devez avoir une compréhension de base de la programmation Python et être à l'aise avec l'utilisation de la ligne de commande ou du terminal. Assurez-vous d'avoir Python 3 installé sur votre système.

Bien que l'expérience préalable avec l'IA ou les modèles de langage (LLM) soit bénéfique, elle n'est pas essentielle, car j'introduirai et expliquerai les concepts clés comme la génération augmentée par récupération (RAG) et les agents IA tout au long du guide.

Ce tutoriel sert de guide pratique et concret pour exploiter cette puissance de l'IA locale. Il se concentre sur l'utilisation de la famille de modèles Qwen 3, une offre open-source de pointe d'Alibaba, combinée à Ollama, un outil qui simplifie considérablement l'exécution des LLM localement.

## Table des matières

1. [Puissance de l'IA locale avec Qwen 3 et Ollama](#heading-puissance-de-lia-locale-avec-qwen-3-et-ollama)
    
    * [Ollama : Votre passerelle locale vers les LLM](#heading-ollama-votre-passerelle-locale-vers-les-llm)
        
    * [Feuille de route du tutoriel](#heading-feuille-de-route-du-tutoriel)
        

2. [Comment configurer votre laboratoire d'IA locale](#heading-comment-configurer-votre-laboratoire-dia-locale)
    
    * [Installer Ollama](#heading-installer-ollama)
        
    * [Choisir votre modèle Qwen 3](#heading-choisir-votre-modele-qwen-3)
        
    * [Télécharger et exécuter Qwen 3 avec Ollama](#heading-telecharger-et-executer-qwen-3-avec-ollama)
        
    * [Configurer votre environnement Python](#heading-configurer-votre-environnement-python)
        
3. [Comment construire un système RAG local avec Qwen 3](#heading-comment-construire-un-systeme-rag-local-avec-qwen-3)
    
    * [Étape 1 : Préparer vos données](#heading-etape-1-preparer-vos-donnees)
        
    * [Étape 2 : Charger les documents en Python](#heading-etape-2-charger-les-documents-en-python)
        
    * [Étape 3 : Diviser les documents](#heading-etape-3-diviser-les-documents)
        
    * [Étape 4 : Choisir et configurer le modèle d'intégration](#heading-etape-4-choisir-et-configurer-le-modele-dintegration)
        
    * [Étape 5 : Configurer le magasin de vecteurs local (ChromaDB)](#heading-etape-5-configurer-le-magasin-de-vecteurs-local-chromadb)
        
    * [Étape 6 : Indexer les documents (intégrer et stocker)](#heading-etape-6-indexer-les-documents-integrer-et-stocker)
        
    * [Étape 7 : Construire la chaîne RAG](#heading-etape-7-construire-la-chaine-rag)
        
    * [Étape 8 : Interroger vos documents](#heading-etape-8-interroger-vos-documents)
        
4. [Comment créer des agents IA locaux avec Qwen 3](#heading-comment-creer-des-agents-ia-locaux-avec-qwen-3)
    
    * [Étape 1 : Définir des outils personnalisés](#heading-etape-1-definir-des-outils-personnalises)
        
    * [Étape 2 : Configurer le LLM de l'agent](#heading-etape-2-configurer-le-llm-de-lagent)
        
    * [Étape 3 : Créer le prompt de l'agent](#heading-etape-3-creer-le-prompt-de-lagent)
        
    * [Étape 4 : Construire l'agent](#heading-etape-4-construire-lagent)
        
    * [Étape 5 : Créer l'exécuteur de l'agent](#heading-etape-5-creer-lexecuteur-de-lagent)
        
    * [Étape 6 : Exécuter l'agent](#heading-etape-6-executer-lagent)
        
5. [Considérations avancées et dépannage](#heading-considerations-avancees-et-depannage)
    
    * [Contrôler le mode de réflexion de Qwen 3 avec Ollama](#heading-controler-le-mode-de-reflexion-de-qwen-3-avec-ollama)
        
    * [Gérer la longueur du contexte (num_ctx)](#heading-gerer-la-longueur-du-contexte-numctx)
        
    * [Limitations matérielles et VRAM](#heading-limitations-materielles-et-vram)
        
6. [Conclusion et prochaines étapes](#heading-conclusion-et-prochaines-etapes)
    

## Puissance de l'IA locale avec Qwen 3 et Ollama

L'exécution de LLM localement répond à plusieurs préoccupations clés associées aux services d'IA basés sur le cloud.

* La confidentialité est primordiale : les données traitées localement ne quittent jamais la machine de l'utilisateur.
    
* Le coût est un autre facteur majeur : l'utilisation de modèles open-source et d'outils comme Ollama élimine les frais d'abonnement aux API et les frais par jeton, rendant l'IA avancée accessible à tous.
    
* L'exécution locale permet une fonctionnalité hors ligne : cruciale pour les applications où la connectivité Internet est peu fiable ou indésirable.
    

### Ollama : Votre passerelle locale vers les LLM

Ollama agit comme un pont, rendant la puissance des modèles comme Qwen 3 accessible sur le matériel local. C'est un outil en ligne de commande qui simplifie le téléchargement, la configuration et l'exécution de divers LLM open-source sur macOS, Linux et Windows.

Ollama gère les complexités de la configuration du modèle et de l'utilisation du GPU, fournissant une interface simple pour les développeurs et les utilisateurs. Il expose également un point de terminaison API compatible avec OpenAI, permettant une intégration transparente avec des frameworks populaires comme LangChain.

### Feuille de route du tutoriel

Ce tutoriel vous guidera à travers le processus de :

1. **Configuration d'un environnement d'IA local** : Installation d'Ollama et sélection/exécution des modèles Qwen 3 appropriés.
    
2. **Construction d'un système RAG local** : Création d'un système qui permet de discuter avec des documents personnels en utilisant Qwen 3, Ollama, LangChain et ChromaDB pour le stockage de vecteurs.
    
3. **Création d'un agent d'IA local de base** : Développement d'un agent simple alimenté par Qwen 3 qui peut utiliser des outils définis par l'utilisateur (fonctions).
    

## Comment configurer votre laboratoire d'IA locale

La première étape consiste à préparer votre machine locale avec les outils et modèles nécessaires.

### Installer Ollama

Ollama fournit le moyen le plus simple d'exécuter des LLM localement.

* **Linux / macOS** : Ouvrez un terminal et exécutez le script d'installation officiel :
    
    ```bash
    curl -fsSL https://ollama.com/install.sh | sh
    ```
    
* **Windows** : Téléchargez l'installateur depuis le site web d'Ollama ([https://ollama.com/download](https://ollama.com/download)) et suivez les instructions d'installation.
    

Après l'installation, vérifiez-la en ouvrant une nouvelle fenêtre de terminal et en exécutant :

```bash
ollama --version
```

Ollama stocke généralement les modèles téléchargés dans `~/.ollama/models` sur macOS et `/usr/share/ollama/.ollama/models` sur Linux/WSL.

### Choisir votre modèle Qwen 3

Le choix du bon modèle Qwen 3 est crucial et dépend de la tâche prévue et du matériel disponible, principalement la RAM système et la VRAM du GPU. L'exécution de modèles plus grands nécessite plus de ressources mais offre généralement de meilleures performances et capacités de raisonnement.

Qwen 3 propose deux architectures principales disponibles via Ollama :

* **Modèles denses** : (comme `qwen3:0.6b`, `qwen3:4b`, `qwen3:8b`, `qwen3:14b`, `qwen3:32b`) Ces modèles activent tous leurs paramètres pendant l'inférence. Leurs performances sont prévisibles, mais les exigences en ressources augmentent directement avec le nombre de paramètres.
    
* **Modèles Mixture-of-Experts (MoE)** : (comme `qwen3:30b-a3b`) Ces modèles contiennent de nombreux sous-réseaux "experts" mais n'en activent qu'une petite fraction pour chaque jeton d'entrée. Cela leur permet d'atteindre les performances caractéristiques de leur grand nombre total de paramètres (par exemple, 30 milliards) tout en ayant des coûts d'inférence plus proches de leur nombre de paramètres *actifs* plus petit (par exemple, 3 milliards). Ils offrent un équilibre convaincant entre capacité et efficacité, surtout pour les tâches de raisonnement et de codage.
    

**Recommandation pour ce tutoriel** : Pour les exemples qui suivent, `qwen3:8b` offre un bon équilibre entre capacité et exigences de ressources pour de nombreuses machines modernes. Si les ressources sont plus limitées, `qwen3:4b` est une alternative viable. Le modèle MoE `qwen3:30b-a3b` offre d'excellentes performances, surtout pour le codage et le raisonnement, et fonctionne surprenamment bien sur les systèmes avec 16 Go+ de VRAM grâce à son activation parcimonieuse.

### Télécharger et exécuter Qwen 3 avec Ollama

Une fois que vous avez choisi un modèle, vous devrez le télécharger (le récupérer) via Ollama.

**Télécharger le modèle** : Ouvrez le terminal et exécutez (remplacez `qwen3:8b` par le tag souhaité) :

```bash
ollama pull qwen3:8b
```

Cette commande télécharge les poids du modèle et la configuration.

**Exécuter de manière interactive (test optionnel)** : Pour discuter directement avec le modèle depuis la ligne de commande :

```bash
ollama run qwen3:8b
```

Tapez les prompts directement dans le terminal. Utilisez `/bye` pour quitter la session. D'autres commandes utiles dans la session interactive incluent `/?` pour l'aide et `/set parameter <name> <value>` (par exemple, `/set parameter num_ctx 8192`) pour changer temporairement les paramètres du modèle pour la session en cours. Utilisez `ollama list` en dehors de la session pour voir les modèles téléchargés.

**Exécuter en tant que serveur** : Pour l'intégration avec des scripts Python (en utilisant LangChain), Ollama doit s'exécuter en tant que processus de serveur en arrière-plan, exposant une API. Ouvrez une fenêtre de terminal *séparée* et exécutez :

```bash
ollama serve
```

Gardez cette fenêtre de terminal ouverte pendant l'exécution des scripts Python. Cette commande démarre le serveur, écoutant généralement sur `http://localhost:11434`, fournissant un point de terminaison API compatible avec OpenAI.

### Configurer votre environnement Python

Un environnement Python dédié est recommandé pour gérer les dépendances.

**Créer un environnement virtuel** :

```bash
python -m venv venv
```

**Activer l'environnement** :

* macOS/Linux : `source venv/bin/activate`
    
* Windows : `venv\Scripts\activate`
    

**Installer les bibliothèques nécessaires** :

```bash
pip install langchain langchain-community langchain-core langchain-ollama chromadb sentence-transformers pypdf python-dotenv unstructured[pdf] tiktoken
```

* `langchain`, `langchain-community`, `langchain-core` : Le framework principal de LangChain pour construire des applications LLM.
    
* `langchain-ollama` : Intégration spécifique pour utiliser les modèles Ollama avec LangChain.
    
* `chromadb` : La base de données vectorielle locale pour stocker les intégrations de documents.
    
* `sentence-transformers` : Utilisé pour une méthode d'intégration locale alternative (expliquée plus tard).
    
* `pypdf` : Une bibliothèque pour charger des documents PDF.
    
* `python-dotenv` : Pour gérer les variables d'environnement (optionnel mais bonne pratique).
    
* `unstructured[pdf]` : Un chargeur de documents alternatif et puissant, surtout pour les PDF complexes.
    
* `tiktoken` : Utilisé par LangChain pour le comptage de jetons.
    

La configuration locale implique la coordination de plusieurs composants indépendants : Ollama lui-même, les poids spécifiques du modèle Qwen 3, l'environnement Python et diverses bibliothèques comme LangChain et ChromaDB. Assurer la compatibilité entre ces éléments et configurer correctement les paramètres (comme la taille de la fenêtre de contexte d'Ollama ou la sélection d'un modèle approprié pour la VRAM disponible) est la clé d'une expérience fluide.

Bien que cette modularité offre de la flexibilité - permettant de remplacer des composants comme le LLM ou le magasin de vecteurs - elle signifie également que la configuration initiale nécessite une attention particulière aux détails. Ce tutoriel vise à fournir des étapes claires et des valeurs par défaut sensées pour minimiser les points de friction potentiels.

## Comment construire un système RAG local avec Qwen 3

La génération augmentée par récupération (RAG) est une technique puissante qui améliore les LLM en leur fournissant des connaissances externes.

Au lieu de se fier uniquement à ses données d'entraînement, le LLM peut récupérer des informations pertinentes à partir d'un ensemble de documents spécifié (comme des PDF locaux) et utiliser ces informations pour répondre aux questions. Cela réduit considérablement les "hallucinations" (informations incorrectes ou fabriquées) et permet au LLM de répondre à des questions sur des données spécifiques et privées sans nécessiter de réentraînement.

Le processus principal de RAG implique :

1. Charger et diviser les documents en morceaux gérables.
    
2. Convertir ces morceaux en représentations numériques (intégrations) à l'aide d'un modèle d'intégration.
    
3. Stocker ces intégrations dans une base de données vectorielle pour une recherche efficace.
    
4. Lorsqu'une requête arrive, intégrer la requête et rechercher dans la base de données vectorielle les morceaux de documents les plus similaires.
    
5. Fournir ces morceaux pertinents (contexte) ainsi que la requête originale au LLM pour générer une réponse informée.
    

Construisons cela localement en utilisant Qwen 3, Ollama, LangChain et ChromaDB.

### Étape 1 : Préparer vos données

Créez un répertoire nommé `data` dans le dossier du projet. Placez le document PDF que vous souhaitez interroger dans ce répertoire. Pour ce tutoriel, utilisez un seul PDF principalement basé sur du texte (comme un article de recherche ou un rapport) pour simplifier.

```bash
mkdir data
# Copiez votre fichier PDF dans le répertoire 'data'
# par exemple, cp ~/Downloads/some_paper.pdf./data/mydocument.pdf
```

Si vous n'avez pas de PDF prêt à l'emploi que vous aimeriez utiliser, vous pouvez télécharger un PDF d'exemple (l'article Llama 2) pour ce tutoriel en utilisant la commande suivante dans votre terminal :

```bash

wget --user-agent "Mozilla" "https://arxiv.org/pdf/2307.09288.pdf" -O "data/llama2.pdf"
```

Cette commande crée le répertoire `data` et télécharge le PDF, le sauvegardant sous le nom `llama2.pdf` dans le répertoire `data`. Si vous préférez utiliser votre propre document, placez votre fichier PDF dans le répertoire `data` et mettez à jour le nom de fichier dans le code Python suivant.

### Étape 2 : Charger les documents en Python

Utilisez les chargeurs de documents de LangChain pour lire le contenu du PDF. `PyPDFLoader` est simple pour les PDF basiques. `UnstructuredPDFLoader` (nécessite `unstructured[pdf]`) peut gérer des mises en page plus complexes mais a plus de dépendances.

```python
# rag_local.py
import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader # Ou UnstructuredPDFLoader

load_dotenv() # Optionnel : Charge les variables d'environnement depuis le fichier .env

DATA_PATH = "data/"
PDF_FILENAME = "mydocument.pdf" # Remplacez par le nom de votre fichier PDF

def load_documents():
    """Charge les documents depuis le chemin de données spécifié."""
    pdf_path = os.path.join(DATA_PATH, PDF_FILENAME)
    loader = PyPDFLoader(pdf_path)
    # loader = UnstructuredPDFLoader(pdf_path) # Alternative
    documents = loader.load()
    print(f"Chargé {len(documents)} page(s) depuis {pdf_path}")
    return documents

# documents = load_documents() # Appelez ceci plus tard
```

### Étape 3 : Diviser les documents

Les grands documents doivent être divisés en morceaux plus petits adaptés à l'intégration et à la récupération. Le `RecursiveCharacterTextSplitter` tente de diviser le texte de manière sémantique (aux paragraphes, phrases, etc.) avant de recourir à des divisions de taille fixe. `chunk_size` détermine la taille maximale de chaque morceau (en caractères), et `chunk_overlap` spécifie combien de caractères doivent se chevaucher entre les morceaux consécutifs pour maintenir le contexte.

```python
# rag_local.py (suite)
from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_documents(documents):
    """Divise les documents en morceaux plus petits."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        is_separator_regex=False,
    )
    all_splits = text_splitter.split_documents(documents)
    print(f"Divisé en {len(all_splits)} morceaux")
    return all_splits

# loaded_docs = load_documents()
# chunks = split_documents(loaded_docs) # Appelez ceci plus tard
```

### Étape 4 : Choisir et configurer le modèle d'intégration

Les intégrations transforment le texte en vecteurs (listes de nombres) de sorte que les morceaux de texte sémantiquement similaires aient des vecteurs proches dans l'espace multidimensionnel.

#### Option A (Recommandée pour la simplicité) : Intégrations Ollama

Cette approche utilise Ollama pour servir un modèle d'intégration dédié. nomic-embed-text est un modèle open-source capable disponible via Ollama.

Tout d'abord, assurez-vous que le modèle d'intégration est téléchargé :

```bash
ollama pull nomic-embed-text
```

Ensuite, utilisez `OllamaEmbeddings` en Python :

```python
# rag_local.py (suite)
from langchain_ollama import OllamaEmbeddings

def get_embedding_function(model_name="nomic-embed-text"):
    """Initialise la fonction d'intégration Ollama."""
    # Assurez-vous que le serveur Ollama est en cours d'exécution (ollama serve)
    embeddings = OllamaEmbeddings(model=model_name)
    print(f"Initialisé les intégrations Ollama avec le modèle : {model_name}")
    return embeddings

# embedding_function = get_embedding_function() # Appelez ceci plus tard
```

#### Option B (Alternative) : Sentence Transformers

Cela utilise la bibliothèque sentence-transformers directement dans le script Python. Cela nécessite d'installer la bibliothèque (pip install sentence-transformers) mais ne nécessite pas de processus Ollama séparé pour les intégrations. Des modèles comme all-MiniLM-L6-v2 sont rapides et légers, tandis que all-mpnet-base-v2 offre une meilleure qualité.

```python
# Fonction d'intégration alternative utilisant Sentence Transformers
from langchain_community.embeddings import HuggingFaceEmbeddings

def get_embedding_function_hf(model_name="all-MiniLM-L6-v2"):
     """Initialise les intégrations HuggingFace (s'exécute localement)."""
     embeddings = HuggingFaceEmbeddings(model_name=model_name)
     print(f"Initialisé les intégrations HuggingFace avec le modèle : {model_name}")
     return embeddings

embedding_function = get_embedding_function_hf() # Utilisez ceci si vous choisissez l'Option B
```

Pour ce tutoriel, nous utiliserons l'Option A (Ollama Embeddings avec `nomic-embed-text`) pour garder la chaîne d'outils cohérente.

### Étape 5 : Configurer le magasin de vecteurs local (ChromaDB)

ChromaDB fournit un moyen efficace de stocker et de rechercher des intégrations vectorielles localement. L'utilisation d'un client persistant garantit que les données indexées sont sauvegardées sur le disque et peuvent être rechargées sans retravailler les documents à chaque fois.

```python
# rag_local.py (suite)
from langchain_community.vectorstores import Chroma

CHROMA_PATH = "chroma_db" # Répertoire pour stocker les données ChromaDB

def get_vector_store(embedding_function, persist_directory=CHROMA_PATH):
    """Initialise ou charge le magasin de vecteurs Chroma."""
    vectorstore = Chroma(
        persist_directory=persist_directory,
        embedding_function=embedding_function
    )
    print(f"Magasin de vecteurs initialisé/chargé depuis : {persist_directory}")
    return vectorstore

embedding_function = get_embedding_function()
vector_store = get_vector_store(embedding_function) # Appelez ceci plus tard
```

### Étape 6 : Indexer les documents (intégrer et stocker)

Il s'agit de l'étape d'indexation principale où les morceaux de documents sont convertis en intégrations et sauvegardés dans ChromaDB. La fonction `Chroma.from_documents` est pratique pour la création et l'indexation initiales. Si la base de données existe déjà, les ajouts ultérieurs peuvent utiliser `vectorstore.add_documents`.

```python
# rag_local.py (suite)

def index_documents(chunks, embedding_function, persist_directory=CHROMA_PATH):
    """Indexe les morceaux de documents dans le magasin de vecteurs Chroma."""
    print(f"Indexation de {len(chunks)} morceaux...")
    # Utilisez from_documents pour la création initiale.
    # Cela écrasera les données existantes si le répertoire existe mais n'est pas une base de données Chroma valide.
    # Pour les mises à jour incrémentielles, initialisez Chroma d'abord et utilisez vectorstore.add_documents().
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_function,
        persist_directory=persist_directory
    )
    vectorstore.persist() # Assurez-vous que les données sont sauvegardées
    print(f"Indexation terminée. Données sauvegardées dans : {persist_directory}")
    return vectorstore

#... (appels de fonctions précédents)
vector_store = index_documents(chunks, embedding_function) # Appelez ceci pour l'indexation initiale
```

Pour charger une base de données persistante existante plus tard :

```python
embedding_function = get_embedding_function()
vector_store = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)
```

### Étape 7 : Construire la chaîne RAG

Maintenant, assemblez les composants dans une chaîne LangChain Expression Language (LCEL). Cela implique d'initialiser le LLM Qwen 3 via Ollama, de créer un récupérateur à partir du magasin de vecteurs, de définir un prompt approprié et de les enchaîner ensemble.

Un paramètre critique lors de l'initialisation de `ChatOllama` pour RAG est `num_ctx`. Cela définit la taille de la fenêtre de contexte (en jetons) que le LLM peut gérer. La valeur par défaut d'Ollama (souvent 2048 ou 4096 jetons) peut être trop petite pour accueillir à la fois le contexte du document récupéré et la requête/prompt de l'utilisateur.

Les modèles Qwen 3 (8B et plus) supportent des fenêtres de contexte beaucoup plus grandes (par exemple, 128k jetons), mais les limites pratiques dépendent de votre RAM/VRAM disponible. Définir `num_ctx` à une valeur comme 8192 ou plus est souvent nécessaire pour un RAG efficace.

```python
# rag_local.py (suite)
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

def create_rag_chain(vector_store, llm_model_name="qwen3:8b", context_window=8192):
    """Crée la chaîne RAG."""
    # Initialiser le LLM
    llm = ChatOllama(
        model=llm_model_name,
        temperature=0, # Température plus basse pour des réponses RAG plus factuelles
        num_ctx=context_window # IMPORTANT : Définir la taille de la fenêtre de contexte
    )
    print(f"Initialisé ChatOllama avec le modèle : {llm_model_name}, fenêtre de contexte : {context_window}")

    # Créer le récupérateur
    retriever = vector_store.as_retriever(
        search_type="similarity", # Ou "mmr"
        search_kwargs={'k': 3} # Récupérer les 3 morceaux les plus pertinents
    )
    print("Récupérateur initialisé.")

    # Définir le modèle de prompt
    template = """Répondez à la question uniquement sur la base du contexte suivant :
{context}

Question : {question}
"""
    prompt = ChatPromptTemplate.from_template(template)
    print("Modèle de prompt créé.")

    # Définir la chaîne RAG en utilisant LCEL
    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
| prompt
| llm
| StrOutputParser()
    )
    print("Chaîne RAG créée.")
    return rag_chain

#... (appels de fonctions précédents)
vector_store = get_vector_store(embedding_function) # En supposant que la base de données est déjà indexée
rag_chain = create_rag_chain(vector_store) # Appelez ceci plus tard
```

L'efficacité du système RAG dépend de la configuration appropriée de chaque composant. La `chunk_size` et `chunk_overlap` dans le diviseur affectent ce que le récupérateur trouve. Votre choix de `embedding_function` doit être cohérent entre l'indexation et l'interrogation. Le paramètre `num_ctx` pour le LLM `ChatOllama` doit être suffisamment grand pour contenir le contexte récupéré et le prompt lui-même. Un modèle de prompt mal conçu peut également induire le LLM en erreur. Assurez-vous de régler soigneusement ces éléments pour des performances optimales.

### Étape 8 : Interroger vos documents

Enfin, invoquez la chaîne RAG avec une question liée au contenu du PDF indexé.

```python
# rag_local.py (suite)

def query_rag(chain, question):
    """Interroge la chaîne RAG et imprime la réponse."""
    print("\nInterrogation de la chaîne RAG...")
    print(f"Question : {question}")
    response = chain.invoke(question)
    print("\nRéponse :")
    print(response)

# --- Exécution principale ---
if __name__ == "__main__":
    # 1. Charger les documents
    docs = load_documents()

    # 2. Diviser les documents
    chunks = split_documents(docs)

    # 3. Obtenir la fonction d'intégration
    embedding_function = get_embedding_function() # Utilisation d'Ollama nomic-embed-text

    # 4. Indexer les documents (ne doit être fait qu'une fois par ensemble de documents)
    # Vérifiez si la base de données existe, sinon, indexez. Pour simplifier, nous pouvons réindexer ici.
    # Une approche plus robuste vérifierait si l'indexation est nécessaire.
    print("Tentative d'indexation des documents...")
    vector_store = index_documents(chunks, embedding_function)
    # Pour charger la base de données existante à la place :
    # vector_store = get_vector_store(embedding_function)

    # 5. Créer la chaîne RAG
    rag_chain = create_rag_chain(vector_store, llm_model_name="qwen3:8b") # Utilisez le modèle Qwen 3 choisi

    # 6. Interroger
    query_question = "Quel est le sujet principal du document ?" # Remplacez par une question spécifique
    query_rag(rag_chain, query_question)

    query_question_2 = "Résumé de la section d'introduction." # Un autre exemple
    query_rag(rag_chain, query_question_2)
```

Exécutez le script complet (`python rag_local.py`). Assurez-vous que la commande `ollama serve` est en cours d'exécution dans un autre terminal. Le script chargera le PDF, le divisera, intégrera les morceaux en utilisant `nomic-embed-text` via Ollama, les stockera dans ChromaDB, construira la chaîne RAG en utilisant `qwen3:8b` via Ollama, et exécutera enfin les requêtes. Il imprimera les réponses du LLM basées sur le contenu du document.

## Comment créer des agents IA locaux avec Qwen 3

Au-delà de répondre aux questions basées sur le texte fourni, les LLM peuvent agir en tant que moteur de raisonnement pour les agents IA. Les agents peuvent planifier des séquences d'actions, interagir avec des outils externes (comme des fonctions ou des API), et travailler à l'accomplissement d'objectifs plus complexes assignés par l'utilisateur.

Les modèles Qwen 3 ont été spécifiquement conçus avec de solides capacités d'appel de fonctions et d'agents. Bien qu'Alibaba fournisse le framework Qwen-Agent, ce tutoriel continuera à utiliser LangChain pour la cohérence et parce que son intégration avec Ollama pour les tâches d'agents est mieux documentée dans les matériaux fournis.

Nous allons construire un agent simple qui peut utiliser une fonction Python personnalisée comme outil.

### Étape 1 : Définir des outils personnalisés

Les outils sont des fonctions Python standard que l'agent peut choisir d'exécuter. La docstring de la fonction est cruciale, car le LLM l'utilise pour comprendre ce que fait l'outil et quels arguments il nécessite. Le décorateur `@tool` de LangChain simplifie l'encapsulation des fonctions pour l'utilisation par l'agent.

```python
# agent_local.py
import os
from dotenv import load_dotenv
from langchain.agents import tool
import datetime

load_dotenv() # Optionnel

@tool
def get_current_datetime(format: str = "%Y-%m-%d %H:%M:%S") -> str:
    """
    Retourne la date et l'heure actuelles, formatées selon la chaîne de format strftime Python fournie.
    Utilisez cet outil chaque fois que l'utilisateur demande la date, l'heure ou les deux.
    Exemples de chaînes de format : '%Y-%m-%d' pour la date, '%H:%M:%S' pour l'heure.
    Si aucun format n'est spécifié, le format par défaut est '%Y-%m-%d %H:%M:%S'.
    """
    try:
        return datetime.datetime.now().strftime(format)
    except Exception as e:
        return f"Erreur de formatage de la date/heure : {e}"

# Liste des outils que l'agent peut utiliser
tools = [get_current_datetime]
print("Outil personnalisé défini.")
```

### Étape 2 : Configurer le LLM de l'agent

Instanciez le modèle `ChatOllama` à nouveau, en utilisant une variante Qwen 3 adaptée à l'appel de fonctions. Le modèle `qwen3:8b` devrait être capable de gérer des cas d'utilisation d'outils simples.

Il est important de noter que la fiabilité de l'appel de fonctions avec des modèles locaux servis via Ollama peut parfois être moins cohérente qu'avec de grandes API commerciales comme GPT-4 ou Claude. Le LLM peut échouer à reconnaître quand un outil est nécessaire, halluciner des arguments ou mal interpréter la sortie de l'outil. Il est recommandé de commencer avec des prompts clairs et des outils simples.

```python
# agent_local.py (suite)
from langchain_ollama import ChatOllama

def get_agent_llm(model_name="qwen3:8b", temperature=0):
    """Initialise le modèle ChatOllama pour l'agent."""
    # Assurez-vous que le serveur Ollama est en cours d'exécution (ollama serve)
    llm = ChatOllama(
        model=model_name,
        temperature=temperature # Température plus basse pour une utilisation d'outil plus prévisible
        # Considérez l'augmentation de num_ctx si vous prévoyez des conversations longues ou un raisonnement complexe
        # num_ctx=8192
    )
    print(f"Initialisé le LLM de l'agent ChatOllama avec le modèle : {model_name}")
    return llm

# agent_llm = get_agent_llm() # Appelez ceci plus tard
```

### Étape 3 : Créer le prompt de l'agent

Les agents nécessitent des structures de prompt spécifiques qui guident leur raisonnement et leur utilisation d'outils. Le prompt inclut généralement des espaces réservés pour l'entrée de l'utilisateur (`input`), l'historique de la conversation (`chat_history`) et le `agent_scratchpad`. Le scratchpad est l'endroit où l'agent enregistre son processus de "réflexion" interne, les outils qu'il décide d'appeler et les résultats (observations) qu'il obtient de ces outils. LangChain Hub fournit des prompts préconstruits adaptés aux agents d'appel d'outils.

```python
# agent_local.py (suite)
from langchain import hub

def get_agent_prompt(prompt_hub_name="hwchase17/openai-tools-agent"):
    """Récupère le modèle de prompt de l'agent depuis LangChain Hub."""
    # Ce prompt est conçu pour OpenAI mais fonctionne souvent bien avec d'autres modèles d'appel d'outils.
    # Alternativement, définissez un ChatPromptTemplate personnalisé.
    prompt = hub.pull(prompt_hub_name)
    print(f"Prompt de l'agent récupéré depuis Hub : {prompt_hub_name}")
    # print("Structure du prompt :")
    # prompt.pretty_print() # Décommentez pour voir la structure du prompt
    return prompt

# agent_prompt = get_agent_prompt() # Appelez ceci plus tard
```

### Étape 4 : Construire l'agent

La fonction `create_tool_calling_agent` combine le LLM, les outils définis et le prompt en une unité exécutable qui représente la logique principale de l'agent.

```python
# agent_local.py (suite)
from langchain.agents import create_tool_calling_agent

def build_agent(llm, tools, prompt):
    """Construire l'agent exécutable d'appel d'outils."""
    agent = create_tool_calling_agent(llm, tools, prompt)
    print("Agent exécutable créé.")
    return agent

# agent_runnable = build_agent(agent_llm, tools, agent_prompt) # Appelez ceci plus tard
```

### Étape 5 : Créer l'exécuteur de l'agent

L'`AgentExecutor` est responsable de l'exécution de la boucle de l'agent. Il prend l'agent exécutable et les outils, invoque l'agent avec l'entrée, analyse la sortie de l'agent (qui pourrait être une réponse finale ou une demande d'appel d'outil), exécute les appels d'outils demandés et renvoie les résultats à l'agent jusqu'à ce qu'une réponse finale soit obtenue. Définir `verbose=True` est fortement recommandé pendant le développement pour observer le flux d'exécution étape par étape de l'agent.

```python
# agent_local.py (suite)
from langchain.agents import AgentExecutor

def create_agent_executor(agent, tools):
    """Crée l'exécuteur de l'agent."""
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True # Définir sur True pour voir les pensées de l'agent et les appels d'outils
    )
    print("Exécuteur de l'agent créé.")
    return agent_executor

# agent_executor = create_agent_executor(agent_runnable, tools) # Appelez ceci plus tard
```

### Étape 6 : Exécuter l'agent

Invoquez l'exécuteur de l'agent avec une requête utilisateur qui devrait déclencher l'utilisation de l'outil défini.

```python
# agent_local.py (suite)

def run_agent(executor, user_input):
    """Exécute l'exécuteur de l'agent avec l'entrée donnée."""
    print("\nInvocation de l'agent...")
    print(f"Entrée : {user_input}")
    response = executor.invoke({"input": user_input})
    print("\nRéponse de l'agent :")
    print(response['output'])

# --- Exécution principale ---
if __name__ == "__main__":
    # 1. Définir les outils (déjà fait ci-dessus)

    # 2. Obtenir le LLM de l'agent
    agent_llm = get_agent_llm(model_name="qwen3:8b") # Utilisez le modèle Qwen 3 choisi

    # 3. Obtenir le prompt de l'agent
    agent_prompt = get_agent_prompt()

    # 4. Construire l'agent exécutable
    agent_runnable = build_agent(agent_llm, tools, agent_prompt)

    # 5. Créer l'exécuteur de l'agent
    agent_executor = create_agent_executor(agent_runnable, tools)

    # 6. Exécuter l'agent
    run_agent(agent_executor, "Quelle est la date actuelle ?")
    run_agent(agent_executor, "Quelle heure est-il maintenant ? Utilisez le format HH:MM.")
    run_agent(agent_executor, "Racontez-moi une blague.") # Ne devrait pas utiliser l'outil
```

L'exécution de `python agent_local.py` (avec `ollama serve` actif) exécutera l'agent. Le paramètre `verbose=True` imprimera une sortie ressemblant au framework ReAct (Raisonnement et Action), montrant les "Pensées" internes de l'agent sur la manière de procéder, l'"Action" qu'il décide de prendre (appeler un outil spécifique avec des arguments), et l'"Observation" (le résultat retourné par l'outil).

La construction d'agents fiables avec des modèles locaux présente des défis uniques. La capacité du LLM à interpréter correctement le prompt, à comprendre quand utiliser les outils, à sélectionner le bon outil, à générer des arguments valides et à traiter la sortie de l'outil est cruciale.

Les modèles locaux, en particulier les plus petits ou fortement quantifiés, peuvent avoir du mal avec ces étapes de raisonnement par rapport à leurs homologues plus grands basés sur le cloud. Si le modèle `qwen3:8b` s'avère peu fiable pour des tâches d'agents plus complexes, envisagez d'essayer `qwen3:14b` ou le modèle efficace `qwen3:30b-a3b` si le matériel le permet.

Pour des flux de travail d'agents hautement complexes ou étatiques, l'exploration de frameworks comme LangGraph, qui offre plus de contrôle sur le flux d'exécution de l'agent, pourrait être bénéfique.

## Considérations avancées et dépannage

L'exécution de LLM localement offre une grande flexibilité mais introduit également des aspects de configuration spécifiques et des problèmes potentiels.

### Contrôler le mode de réflexion de Qwen 3 avec Ollama

L'inférence hybride unique de Qwen 3 permet de basculer entre un mode de "réflexion" approfondi pour le raisonnement complexe et un mode "non-réflexion" plus rapide pour le chat général. Bien que des frameworks comme Hugging Face Transformers ou vLLM puissent offrir des paramètres explicites (`enable_thinking`), la principale façon de contrôler cela lors de l'utilisation d'Ollama semble être par le biais de "commutateurs logiciels" intégrés dans le prompt.

Ajoutez `/think` à la fin d'un prompt utilisateur pour encourager un raisonnement étape par étape, ou `/no_think` pour demander une réponse rapide et directe. Vous pouvez faire cela via l'interface de ligne de commande Ollama ou potentiellement dans les prompts envoyés via l'API/LangChain.

```python
# Exemple utilisant ChatOllama de LangChain
from langchain_ollama import ChatOllama

llm_think = ChatOllama(model="qwen3:8b")
llm_no_think = ChatOllama(model="qwen3:8b") # Peut également définir le prompt système

# Invoquer avec modification du prompt
response_think = llm_think.invoke("Résolvez l'équation 2x + 5 = 15 /think")
print("Réponse de réflexion :", response_think)

response_no_think = llm_no_think.invoke("Quelle est la capitale de la France ? /no_think")
print("Réponse sans réflexion :", response_no_think)

# Alternativement, définir via le message système (peut être moins fiable tour par tour)
llm_system_no_think = ChatOllama(model="qwen3:8b", system="/no_think")
response_system = llm_system_no_think.invoke("Qu'est-ce que 2+2 ?")
print("Réponse système sans réflexion :", response_system)
```

Notez que la persistance de ces balises sur plusieurs tours dans une conversation peut nécessiter une gestion minutieuse des prompts.

### Gérer la longueur du contexte (`num_ctx`)

La fenêtre de contexte (`num_ctx`) détermine la quantité d'informations (prompt, historique, documents récupérés) que le LLM peut considérer à la fois. Les modèles Qwen 3 (8B+) supportent de grandes longueurs de contexte natives (par exemple, 128k jetons), mais Ollama utilise souvent une fenêtre beaucoup plus petite par défaut (comme 2048 ou 4096). Pour le RAG ou les conversations nécessitant la mémoire des tours précédents, cette valeur par défaut est souvent insuffisante.

Définissez `num_ctx` lors de l'initialisation de `ChatOllama` ou `OllamaLLM` dans LangChain :

```python
# Exemple de définition de la fenêtre de contexte à 8192 jetons
llm = ChatOllama(model="qwen3:8b", num_ctx=8192)
```

Soyez conscient que des valeurs `num_ctx` plus grandes augmentent considérablement la consommation de RAM et de VRAM. Mais les définir trop bas peut conduire le modèle à "oublier" le contexte ou même à entrer dans des boucles répétitives. Choisissez une valeur qui équilibre les exigences de la tâche avec les capacités matérielles.

### Limitations matérielles et VRAM

L'exécution de LLM localement est intensive en ressources.

* **VRAM** : Une GPU dédiée (NVIDIA ou Apple Silicon) avec suffisamment de VRAM est fortement recommandée pour des performances acceptables. La quantité de VRAM dicte la plus grande taille de modèle qui peut fonctionner efficacement. Reportez-vous au tableau de la section 2 pour des estimations.
    
* **RAM** : La RAM système est également cruciale, surtout si le modèle ne tient pas entièrement dans la VRAM. Ollama peut utiliser la RAM système comme solution de repli, mais cela est considérablement plus lent.
    
* **Quantification** : Ollama sert généralement des modèles quantifiés (par exemple, 4 bits ou 5 bits), ce qui réduit la taille du modèle et les exigences de VRAM de manière significative par rapport aux modèles en pleine précision, souvent avec une dégradation minimale des performances pour de nombreuses tâches. Les tags comme `:4b`, `:8b` impliquent généralement un niveau de quantification par défaut.
    

Si les performances sont lentes ou si des erreurs se produisent en raison de contraintes de ressources, envisagez :

* Utiliser un modèle Qwen 3 plus petit (comme 4B au lieu de 8B).
    
* Vous assurer qu'Ollama détecte et utilise correctement le GPU (vérifiez les journaux d'Ollama ou les outils de surveillance du système).
    
* Fermer d'autres applications gourmandes en ressources.
    

## Conclusion et prochaines étapes

Ce tutoriel vous a fourni un guide pratique pour configurer votre environnement d'IA locale en utilisant la puissante famille de modèles Qwen 3 et l'outil convivial Ollama.

Si vous avez suivi ces étapes, vous devriez avoir réussi à :

1. Installer Ollama et télécharger/exécuter des modèles Qwen 3 localement.
    
2. Construire un pipeline de génération augmentée par récupération (RAG) fonctionnel en utilisant LangChain et ChromaDB pour interroger des documents locaux.
    
3. Créer un agent IA de base capable de raisonnement et d'utilisation d'outils Python personnalisés.
    

L'exécution de ces systèmes localement déverrouille des avantages significatifs en termes de confidentialité, de coût et de personnalisation, rendant les capacités d'IA avancées plus accessibles que jamais. La combinaison des performances de Qwen 3 et de sa licence ouverte avec la facilité d'utilisation d'Ollama crée une plateforme puissante pour l'expérimentation et le développement.

**Ressources officielles :**

* **Qwen 3 :** [GitHub](https://github.com/QwenLM/Qwen3), [Documentation](https://qwen.readthedocs.io/en/latest/)
    
* **Ollama :** [Site web](https://ollama.com/), [Bibliothèque de modèles](https://ollama.com/library), [GitHub](https://github.com/ollama/ollama)
    
* **LangChain :** [Documentation Python](https://python.langchain.com/docs/get_started/introduction)
    
* **ChromaDB :** [Documentation](https://docs.trychroma.com/)
    
* **Sentence Transformers :** [Documentation](https://www.sbert.net/)
    

En tirant parti de ces outils puissants, gratuits et open-source, vous pouvez continuer à repousser les limites de ce qui est possible avec l'IA fonctionnant directement sur votre propre matériel.