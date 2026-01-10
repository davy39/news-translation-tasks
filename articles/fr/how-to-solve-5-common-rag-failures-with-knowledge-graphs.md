---
title: Comment résoudre 5 échecs courants de RAG avec les Knowledge Graphs
subtitle: Aller au-delà de la recherche sémantique pour un raisonnement robuste.
author: Kamal Kishore
co_authors: []
series: null
date: '2025-11-13T15:20:24.336Z'
originalURL: https://freecodecamp.org/news/how-to-solve-5-common-rag-failures-with-knowledge-graphs
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1762904270014/5ebeec2b-0823-4f59-bdd7-bf37cb68a978.png
tags:
- name: 'RAG '
  slug: rag
- name: knowledge graph
  slug: knowledge-graph
- name: llm
  slug: llm
- name: AI
  slug: ai
seo_title: Comment résoudre 5 échecs courants de RAG avec les Knowledge Graphs
seo_desc: You may have built a Retrieval-Augmented Generation (RAG) pipeline to connect
  a vector store to a powerful LLM. And RAG pipelines are incredibly effective at
  grounding models in factual, up-to-date knowledge. But if you've worked with them
  long enoug...
---

Vous avez peut-être construit un pipeline de Retrieval-Augmented Generation (RAG) pour connecter un vector store à un LLM puissant. Les pipelines RAG sont incroyablement efficaces pour ancrer les modèles dans des connaissances factuelles et à jour. Mais si vous travaillez avec eux depuis assez longtemps, vous avez probablement atteint une limite.

Le système est excellent pour répondre à « Qu'est-ce que X ? » mais s'effondre lorsque vous demandez : « Quel est le lien entre X et Y, et que s'est-il passé après Z ? ».

Le problème est que le RAG standard, par sa nature même, brise le contexte. Il découpe les documents en fragments (chunks) isolés, les trouve sur la base de la similarité sémantique et espère que le LLM pourra reconstituer le puzzle. Cette approche est aveugle au contexte relationnel — le réseau de chronologies, de causes et de connexions — qui donne leur sens aux faits.

Lorsque les requêtes nécessitent de synthétiser des informations provenant de plusieurs documents ou un raisonnement complexe en plusieurs étapes, le RAG standard échoue.

Dans cet article, je vais vous donner un guide pratique, axé sur le code, pour résoudre ce problème. Nous irons au-delà de la simple recherche vectorielle en implémentant un modèle robuste basé sur les graphes pour construire des systèmes plus fiables et conscients des connaissances.

## Table des matières :

* [Prérequis](#heading-prerequis)
    
* [La base fragile : notre configuration RAG standard](#heading-la-base-fragile-notre-configuration-rag-standard)
    
* [Une implémentation plus robuste : le KnowledgeGraph](#heading-une-implementation-plus-robuste-le-knowledgegraph)
    
    * [Qu'est-ce qu'un Knowledge Graph ?](#heading-qu-est-ce-qu-un-knowledge-graph)
        
    * [Pourquoi est-ce plus efficace ?](#heading-pourquoi-est-ce-plus-efficace)
        
* [5 échecs de RAG et leurs solutions basées sur les graphes](#heading-5-echecs-de-rag-et-leurs-solutions-basees-sur-les-graphes)
    
    * [Modèle 1 : L'échec Multi-Hop](#heading-modele-1-l-echec-multi-hop)
        
    * [Modèle 2 : L'échec de synthèse causale](#heading-modele-2-l-echec-de-synthese-causale)
        
    * [Modèle 3 : Le piège de l'ambiguïté des entités](#heading-modele-3-le-piege-de-l-ambiguite-des-entites)
        
    * [Modèle 4 : L'échec des informations contradictoires](#heading-modele-4-l-echec-des-informations-contradictoires)
        
    * [Modèle 5 : L'hallucination de relation implicite](#heading-modele-5-l-hallucination-de-relation-implicite)
        
* [Réflexions finales](#heading-reflexions-finales)
    

### Prérequis

Ceci est un guide pratique, axé sur le code, destiné aux développeurs et ingénieurs ayant une certaine expérience du RAG. Pour suivre, vous devriez disposer des éléments suivants :

#### Connaissances conceptuelles

* Une solide compréhension de ce qu'est le Retrieval-Augmented Generation (RAG) et de ses composants de base (comme les vector stores et les LLM).
    
* Une familiarité avec les concepts de base des graphes (Nodes, Edges et relations) est également utile.
    

#### Configuration technique

* Un environnement Python.
    
* Une Google API Key active pour utiliser la Gemini API.
    
* Les bibliothèques Python `langchain`, `langchain_google_genai`, `faiss-cpu` et `networkx` installées.
    

## La base fragile : notre configuration RAG standard

Tout d'abord, établissons notre base de référence. Il s'agit d'un pipeline RAG standard et « naïf » utilisant LangChain et la Gemini API. Il ingère une liste d'objets `Document`, les transforme en embeddings et utilise un vector store FAISS pour récupérer les top-k fragments afin de répondre à une question.

Cette fonction `create_rag_chain` servira de point de comparaison.

```python
# Install necessary libraries
# !pip install -q -U langchain langchain_google_genai faiss-cpu networkx

import os
import networkx as nx
from collections import defaultdict
from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.schema.document import Document
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser

# --- Configure API Key (example) ---
# from google.colab import userdata
# GOOGLE_API_KEY = userdata.get('GOOGLE_API_KEY') 
# os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY 

# --- Initialize Models ---
# Make sure your API key is set in your environment
llm = GoogleGenerativeAI(model="gemini-1.5-pro-latest")
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

def create_rag_chain(docs):
    """Creates a simple RAG chain using FAISS as the vector store.""" 
    
    # Create vector store from documents
    vectorstore = FAISS.from_documents(docs, embeddings)
    # K=3 means it will retrieve the top 3 most relevant chunks
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    template = """
    Answer the following question based ONLY on the context provided.
    If the context doesn't contain the answer, say "I don't have enough information from the context."

    CONTEXT:
    {context}

    QUESTION:
    {question}
    """
    
    prompt = PromptTemplate.from_template(template)

    # Build the chain
    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()} 
        | prompt
        | llm 
        | StrOutputParser() 
    )
    
    return rag_chain
```

## Une implémentation plus robuste : le KnowledgeGraph

### Qu'est-ce qu'un Knowledge Graph ?

À la base, un Knowledge Graph (KG) est un moyen de stocker des données sous forme de réseau de Nodes et d'Edges.

* **Nodes** représentent des entités : `people`, `companies`, `concepts` ou `events`.
    
* **Edges** représentent les relations explicites et étiquetées entre elles : `ceo_of`, `attended` ou `partners_with`.
    

Au lieu de stocker un document comme « Jim Farley est le CEO de Ford », vous stockez deux Nodes (`Jim Farley`, `Ford`) connectés par un Edge dirigé (`ceo_of`).

### Pourquoi est-ce plus efficace ?

Cette structure est plus efficace car elle préserve les relations et en fait des citoyens de première classe.

Le RAG standard repose sur la « similarité sémantique ». Il est doué pour trouver des fragments de texte qui *ressemblent* à votre requête. Mais il est « aveugle au contexte relationnel » – l'élément même dont vous avez besoin pour des questions complexes.

L'approche par graphe résout ce problème. Lorsqu'une requête nécessite un raisonnement en plusieurs étapes, vous ne vous contentez pas de rechercher du texte similaire. Vous parcourez un chemin structuré et explicite dans le graphe. Cela permet au système de :

1. **Suivre des chaînes logiques :** Il peut répondre à des questions multi-hop en trouvant un chemin littéral d'un Node à un autre (par exemple, `F-150` → `made_by` → `Ford` → `ceo` → `Jim Farley`).
    
2. **Désambiguïser les entités :** Il peut utiliser les attributs des Nodes (comme `type: "company"`) pour distinguer deux entités portant le même nom.
    
3. **Résoudre les contradictions :** Il peut stocker des métadonnées (comme des dates) directement *sur l'Edge* pour déterminer par programmation le fait le plus actuel.
    

Vous passez de « deviner à partir d'un nuage de texte sémantiquement similaire » à l'interrogation d'une « mémoire globale » de la manière dont les faits sont explicitement connectés.

Voici l'implémentation pratique de notre `KnowledgeGraph`. Cette classe utilise `networkx` pour stocker les Nodes et les Edges dont nous venons de discuter, et inclut des méthodes spécifiques pour exécuter les modèles de requête structurés nécessaires pour résoudre nos échecs de RAG.

```python
class KnowledgeGraph:
    """
    A wrapper around networkx.DiGraph to store and query
    explicit entities and their relationships.
    """
    def __init__(self):
        self.graph = nx.DiGraph() 

    def add_data(self, nodes=None, edges=None):
        """Populates the graph with nodes and edges."""
        if nodes:
            for node, attrs in nodes:
                self.graph.add_node(node, **attrs) 
        if edges:
            for u, v, attrs in edges:
                self.graph.add_edge(u, v, **attrs) 

    # --- Query Patterns ---
 
    def query_multi_hop_path(self, source, target):
        """
        Pattern 1: Solves multi-hop queries by finding a path.
        """
        try:
            path = nx.shortest_path(self.graph, source=source, target=target) 
            # Format the answer based on the discovered path
            return f"{path[-2]} attended {path[-1]}." 
        except nx.NetworkXNoPath:
            return "Could not find a connection."

    def query_with_conflict_resolution(self, entity, relation, time_attr="year"):
        """
        Pattern 4: Resolves contradictions using metadata (like timestamps)
        stored on the edges.
        """
        candidates = []
        for neighbor in self.graph.neighbors(entity):
            edge_data = self.graph.get_edge_data(entity, neighbor) 
            if edge_data.get("label") == relation: 
                candidates.append((neighbor, edge_data.get(time_attr, 0))) 
        
        if not candidates: 
            return "No information found." 

        # Sort by the time attribute, descending, and take the latest
        latest = sorted(candidates, key=lambda item: item[1], reverse=True)[0] 
        return f"{latest[0]} (as of {latest[1]})" 

    def query_disambiguated(self, entity_name, entity_type, attribute_key):
        """
        Pattern 3: Uses node 'type' attributes to disambiguate
        entities with the same name.
        """
        for node, attrs in self.graph.nodes(data=True): 
            # Find the node that matches both name and type
            if entity_name in node and attrs.get("type") == entity_type: 
                # Return the requested attribute
                year = attrs['year']
                product = attrs[attribute_key]
                return f"{node}'s first product was the {product} in {year}." 
        return "Cannot disambiguate entity."

    def query_explicit_relation(self, source_node, relation_label):
        """
        Pattern 5: Finds partners based on an explicit edge label,
        preventing semantic 'bleed-over' from unrelated entities.
        """
        partners = [
            v for u, v, data in self.graph.edges(data=True) 
            if u == source_node and data.get('label') == relation_label
        ] 
        
        if partners:
            return f"{source_node} partnered with {', '.join(partners)}." 
        return f"No partners found for {source_node}."

# A helper function for Pattern 2 (Causal Rules)
# This logic is more rule-based but can be backed by a graph
def query_causal_chain(facts):
    """
    Pattern 2: Synthesizes a direct conclusion by following a
    chain of causal rules.
    """
    try:
        if facts["John"]["takes"] == "aspirin": 
            if facts["aspirin"]["is_a"] == "blood thinner": 
                if facts["blood thinner"]["risk_for"] == "surgery":
                    return "John is NOT safe due to increased bleeding risk from aspirin, a blood thinner."
    except KeyError:
        pass # Fall through to default
    return "Insufficient information to determine risk."
```

## 5 échecs de RAG et leurs solutions basées sur les graphes

Lançons cinq scénarios pour voir comment notre chaîne RAG standard se comporte par rapport à notre nouveau `KnowledgeGraph`.

### Modèle 1 : L'échec Multi-Hop

L'échec multi-hop se produit lorsqu'une réponse nécessite de connecter plusieurs faits distincts – une chaîne de raisonnement que le RAG brise souvent.

* **Requête :** « Quelle université le CEO de l'entreprise qui fabrique le F-150 a-t-il fréquentée ? »
    
* **Problème :** Un récupérateur standard pourrait obtenir des fragments pour `F-150 -> Ford` et `Jim Farley -> CEO`, mais manquer le fragment `Jim Farley -> Georgetown`. La chaîne est brisée.
    

#### Pourquoi le RAG Naïf échoue

Le travail du récupérateur est de trouver les `top-k=3` fragments qui sont **sémantiquement similaires** à l'ensemble de la requête. Lorsque l'utilisateur demande : « Quelle université le CEO de l'entreprise qui fabrique le F-150 a-t-il fréquentée ? », le récupérateur cherchera dans notre liste de 6 documents et récupérera probablement :

1. Le fragment sur l'**Université du Michigan** (à cause des mots « université » et « entreprises automobiles »).
    
2. Le fragment sur **Jim Farley** (à cause de « CEO », « Ford » et « ligne F-150 »).
    
3. Le fragment sur les **options de moteur du F-150** (à cause de « F-150 »).
    

Le contexte `top-k=3` transmis au LLM est maintenant rempli de faits non pertinents. Le seul fragment qui contient la *vraie* réponse (« ...Mr Farley... de l'Université de Georgetown ») est sémantiquement trop éloigné de la requête principale et n'est **jamais récupéré**. Le LLM échoue non pas parce qu'il manque d'intelligence, mais parce qu'on ne lui a jamais donné la bonne pièce du puzzle.

#### Pourquoi le GraphRAG réussit

Le Knowledge Graph ne se soucie pas de la similarité sémantique. Il effectue un parcours déterministe de relations explicites et vérifiées.

Nous demandons le *chemin* du Node `F-150` au Node `Georgetown University`. Le graphe suit la chaîne que nous avons définie : `F-150` → `made_by` → `Ford Motor Company` → `ceo` → `Jim Farley` → `attended` → `Georgetown University`. Il ne peut pas échouer ou être distrait par les documents « parasites » car il ne cherche pas – il **navigue** sur une carte pré-établie.

```python
# --Naive RAG
docs_s1 = [
	# --- The 3 "Answer" Chunks ---
	Document(page_content="The Ford F-150 is a full-size pickup truck made by Ford Motor Company."),
	Document(page_content="Jim Farley is the current CEO of Ford Motor Company."),
	Document(page_content="Mr. Farley received his undergraduate degree from Georgetown University."),
	
	# --- The 3 "Noise" Chunks (to distract the retriever) ---
	Document(page_content="The University of Michigan is renowned for its automotive engineering program, which partners with many car companies."),
	Document(page_content="The F-150 comes with several engine options, including a powerful 3.5L EcoBoost V6."),
	Document(page_content="Mary Barra, the CEO of General Motors, is a major competitor to Ford and its F-150 line.")
]
query_s1 = "Which university did the CEO of the company that makes the F-150 attend?"
rag_chain_s1 = create_rag_chain(docs_s1) # This uses top_k=3
print(f"Naive RAG Answer: {rag_chain_s1.invoke(query_s1)}")
#
# GraphRAG Pattern
graph_s1 = KnowledgeGraph()
edges_s1 = [
	("F-150", "Ford Motor Company", {"label": "made_by"}),
	("Ford Motor Company", "Jim Farley", {"label": "ceo"}),
	("Jim Farley", "Georgetown University", {"label": "attended"}),
]
graph_s1.add_data(edges=edges_s1)
print(f"GraphRAG Answer: {graph_s1.query_multi_hop_path('F-150', 'Georgetown University')}")
```

**Sortie :**

```plaintext
Naive RAG Answer: I don't have enough information from the context.
GraphRAG Answer: Jim Farley attended Georgetown University.
```

### Modèle 2 : L'échec de synthèse causale

Il s'agit de l'incapacité à passer de la récupération à la synthèse. Le RAG énumère des faits mais ne peut pas les combiner pour former une nouvelle conclusion.

* **Requête :** « John peut-il subir une chirurgie en toute sécurité tout en prenant de l'aspirine ? »
    
* **Problème :** Le RAG récupérera « John prend de l'aspirine », « L'aspirine est un anticoagulant » et « Les anticoagulants augmentent le risque chirurgical ». Mais il ne parviendra pas à synthétiser ces éléments en une réponse directe « Non, ce n'est pas sûr ».
    

#### Pourquoi le RAG Naïf échoue

Le récupérateur recherche des fragments sémantiquement similaires à la requête : « John », « sûr », « chirurgie » et « aspirine ». Dans une base de documents réelle, il est fort probable qu'il récupère des fragments « parasites » distrayants mais liés au sujet.

Dans notre exemple, les `top-k=3` fragments qu'il récupère pourraient être :

1. « John prend actuellement une faible dose d'aspirine quotidienne. » (Pertinent : « John », « aspirine »)
    
2. « Les contrôles de sécurité pré-chirurgicaux sont une procédure standard... » (Pertinent : « sécurité chirurgie »)
    
3. « John est par ailleurs en bonne santé et a reçu le feu vert pour l'intervention... » (Pertinent : « John », « sûr », « intervention »)
    

Le lien causal clé (« L'aspirine... est considérée comme un anticoagulant ») est sémantiquement moins similaire à la *requête complète* et se retrouve exclu du contexte `top-k=3`. Le LLM reçoit alors des informations incomplètes. Il voit « John prend de l'aspirine » et « John a le feu vert », il fournit donc une réponse évasive et ne peut pas faire le saut logique correct.

#### Pourquoi le GraphRAG réussit

Cette approche n'utilise pas la recherche sémantique. Elle utilise des règles logiques explicites (qui pourraient être soutenues par un graphe causal). La fonction `query_causal_chain` ne recherche pas de texte – elle exécute une chaîne logique prédéfinie :

1. *Fait :* John prend-il de l'aspirine ? Oui.
    
2. *Fait :* L'aspirine est-elle un anticoagulant ? Oui.
    
3. *Fait :* Un anticoagulant est-il un risque pour la chirurgie ? Oui.
    
4. *Conclusion :* Par conséquent, John n'est pas en sécurité.
    

Ce raisonnement déterministe, basé sur des règles, est immunisé contre le « bruit sémantique » qui distrait le RAG naïf.

```python
# Naive RAG
docs_s2 = [
	# --- The 3 "Answer" Chunks ---
	Document(page_content="Aspirin reduces blood clotting and is considered a blood thinner."),
	Document(page_content="Patients on blood thinners have increased bleeding risk during surgery."),
	Document(page_content="John is currently taking daily low-dose aspirin."),

	# --- The 3 "Noise" Chunks (to distract the retriever) ---
	Document(page_content="John is otherwise in good health and is cleared for the procedure by his cardiologist."),
	Document(page_content="Pre-surgery safety checks are standard procedure and usually focus on anesthesia allergies."),
	Document(page_content="Aspirin is also commonly used to relieve minor aches and pains, but this is not why John takes it.")
]
query_s2 = "Is John safe to undergo surgery while on aspirin?"
rag_chain_s2 = create_rag_chain (docs_s2)
print(f"Naive RAG Answer: {rag_chain_s2.invoke(query_s2)}")

# GraphRAG Pattern
facts_s2 = {
	"aspirin": {"is_a": "blood thinner"},
	"blood thinner": {"risk_for": "surgery"},
	"John": {"takes": "aspirin"},
}
print(f"GraphRAG Answer: {query_causal_chain(facts_s2)}")
```

**Sortie :**

```plaintext
Naive RAG Answer: Based on the context, John is currently taking daily low-dose aspirin...
GraphRAG Answer: John is NOT safe due to increased bleeding risk from aspirin, a blood thinner.
```

### Modèle 3 : Le piège de l'ambiguïté des entités

La recherche vectorielle a du mal avec la polysémie (mots ayant plusieurs sens). Elle s'appuie sur le contexte sémantique local, qui peut facilement être confondu.

* **Requête :** « Quand Apple a-t-elle sorti son premier produit ? »
    
* **Problème :** La requête « Apple » peut récupérer des documents concernant à la fois Apple (l'entreprise) et Apple (le fruit), ce qui sème la confusion chez le LLM.
    

#### Pourquoi le RAG Naïf échoue

La requête « Quand Apple a-t-elle sorti son premier produit ? » est sémantiquement ambiguë. Le récupérateur vectoriel, qui recherche la *proximité sémantique*, sera fortement attiré par les fragments « parasites » que nous avons ajoutés sur le fruit.

Les `top-k=3` fragments qu'il récupère seront probablement :

1. « La 'Cosmic Crisp' est un nouveau **produit Apple**... **sorti pour la première fois**... » (Similarité sémantique extrêmement élevée avec « Apple sort son premier produit »).
    
2. « La pomme Granny Smith... est un **produit** populaire... »
    
3. « De nombreux vergers de pommiers **sortent** leur nouvelle récolte... »
    

Le fragment *correct* (« L'Apple I a été introduit par Apple Inc... ») concerne une « entreprise » et un nom de « produit » spécifique. Il peut être sémantiquement *moins* similaire à la requête générale que le fragment « Cosmic Crisp ». Le LLM reçoit alors un contexte exclusivement sur les fruits et répond avec assurance (mais de manière incorrecte) au sujet de la pomme « Cosmic Crisp ».

#### Pourquoi le GraphRAG réussit

L'approche par graphe est immunisée contre cette ambiguïté. La fonction `query_disambiguated` ne se contente pas de rechercher « Apple ». Elle recherche explicitement un Node qui correspond à deux critères : `name='Apple'` ET `type='company'`.

Cette requête garantit structurellement qu'elle trouve le Node `Apple Inc.` et ignore le Node `apple (fruit)`, quelle que soit la similarité sémantique. Elle récupère ensuite de manière fiable l'attribut `first_product` du bon Node.

```python
# Naive RAG
docs_s3 = [
	# --- The "Answer" Chunks ---
	Document(page_content="The Apple was introduced by Apple Inc. in 1976."),
	Document(page_content="Apple Inc. is a technology company based in Cupertino."),

	# --- "Noise" Chunks (to create ambiguity) ---
	Document(page_content="The 'Cosmic Crisp' is a new apple product developed by Washington State University, first released to consumers in 2019."),
	Document(page_content="Apples (the fruit) were first cultivated in Central Asia thousands of years ago."),
	Document(page_content="The Granny Smith apple, first discovered in Australia, is a popular product for baking."),
	Document(page_content="Many apple orchards release their new harvest in the fall.")
]
query_s3 = "When did Apple release its first product?"
rag_chain_s3 = create_rag_chain(docs_s3)
print(f"Naive RAG Answer: {rag_chain_s3.invoke(query_s3)}")

# GraphRAG Pattern
graph_s3 = KnowledgeGraph()
nodes_s3 = [
	("Apple Inc.", {"type": "company", "first_product": "Apple I", "year": 1976}),
	("apple", {"type": "fruit", "origin": "Central Asia"}),
]
graph_s3.add_data(nodes=nodes_s3)
print(f"GraphRAG Answer: {graph_s3.query_disambiguated('Apple', 'company', 'first_product')}")
```

**Sortie :**

```python
Naive RAG Answer: The 'Cosmic Crisp', a new apple product, was first released to consumers in 2019.
GraphRAG Answer: Apple Inc.'s first product was the Apple I in 1976.
```

### Modèle 4 : L'échec des informations contradictoires

Le RAG est aveugle aux conflits de connaissances. S'il récupère deux ou plusieurs faits contradictoires, il ne peut pas les résoudre à l'aide de métadonnées telles que les dates ou la crédibilité de la source. Il va soit hésiter, soit les fusionner en une déclaration fausse, soit les présenter tous.

* **Requête :** « Qui est le CEO de Twitter ? »
    
* **Problème :** Le récupérateur trouve un fragment disant « Parag Agrawal (2022) » et un autre disant « Elon Musk (2023) ». Il peut également trouver d'autres informations connexes et déroutantes. Le LLM n'a aucun moyen de savoir quel fait est le plus actuel et fait autorité.
    

#### Pourquoi le RAG Naïf échoue

La requête « Qui est le CEO de Twitter ? » est sémantiquement similaire à *tous* les documents contenant les mots « CEO » et « Twitter ». Dans une base de connaissances réelle et évolutive, c'est la recette du désastre.

Les `top-k=3` fragments que notre récupérateur trouve seront un mélange de contradictions :

1. « En 2023, Elon Musk est devenu le CEO de Twitter. » (Correct, mais ancien)
    
2. « En 2022, Parag Agrawal était le CEO de Twitter. » (Ancien)
    
3. « Linda Yaccarino est l'actuelle CEO de X (anciennement Twitter)... » (Également correct, mais une personne/un rôle différent).
    

Le LLM se voit remettre trois noms différents et contradictoires pour le « CEO de Twitter » provenant de différentes périodes. Comme il a pour instruction de répondre *uniquement* à partir du contexte et qu'il n'a aucun mécanisme pour identifier quel fait est le plus récent, il ne peut pas donner une réponse unique et assurée. Il est forcé d'énumérer les conflits qu'il a trouvés.

#### Pourquoi le GraphRAG réussit

Le Knowledge Graph est conçu pour cela. Nous avons stocké la relation « CEO » sous forme d'**Edge avec métadonnées**, spécifiquement un attribut `year`.

Notre fonction `query_with_conflict_resolution` ne se contente pas de trouver tous les Edges liés au CEO. Elle effectue par programmation les étapes suivantes :

1. Trouve tous les Nodes connectés à « Twitter » par une étiquette `ceo`.
    
2. Extrait l'année (`year`) de chacun de ces Edges.
    
3. **Trie les candidats par année** par ordre décroissant.
    
4. Ne renvoie que le premier résultat.
    

Cela fournit un moyen déterministe et programmatique de résoudre les conflits et de toujours fournir le fait le plus actuel basé sur les horodatages explicites de notre graphe.

```python
# Naive RAG
docs_s4 = [
	# --- The "Answer" Chunks (conflicting) ---
	Document(page_content="In 2022, Parag Agrawal was the CEO of Twitter."),
	Document(page_content="In 2023, Elon Musk became the CEO of Twitter."),

	# --- "Noise" Chunks (to add more conflict/confusion) ---
	Document(page_content="Linda Yaccarino is the current CEO of X (formerly Twitter), overseeing business operations."),
	Document(page_content="Jack Dorsey, a co-founder and former CEO of Twitter, is now focused on his company Block."),
	Document(page_content="CEOs of major tech companies, including Twitter's, have recently testified before Congress.")
]
query_s4 = "Who is the CEO of Twitter?"
rag_chain_s4 = create_rag_chain(docs_s4)
print(f"Naive RAG Answer: {rag_chain_s4.invoke(query_s4)}")

#GraphRAG Pattern
graph_s4 = KnowledgeGraph()
edges_s4 = [
	("Twitter", "Parag Agrawal", {"label": "ceo", "year": 2022}),
	("Twitter", "Elon Musk", {"label": "ceo", "year": 2023}),
]
graph_s4.add_data(edges=edges_s4)
print(f"GraphRAG Answer: {graph_s4.query_with_conflict_resolution('Twitter', 'ceo', 'year')}") 
```

**Sortie :**

```python
Naive RAG Answer: According to the context, in 2022, Parag Agrawal was the CEO of Twitter. In 2023, Elon Musk became the CEO... Linda Yaccarino is the current CEO of X (formerly Twitter)...
GraphRAG Answer: Elon Musk (as of 2023)
```

### Modèle 5 : L'hallucination de relation implicite

Le RAG repose sur une proximité sémantique implicite, ce qui peut être dangereux. Si « Tesla », « Toyota » et « Panasonic » apparaissent tous près du mot « batterie » dans l'espace vectoriel, le LLM pourrait halluciner une relation qui n'existe pas.

* **Requête :** « Avec qui Tesla s'est-elle associée pour les batteries ? »
    
* **Problème :** La requête est sémantiquement « proche » de tout document mentionnant « Tesla », « partenaire » et « batteries ». Le récupérateur ira chercher des fragments basés sur cette proximité, même s'ils n'énoncent pas explicitement un partenariat, ce qui amènera le LLM à en déduire un.
    

#### Pourquoi le RAG Naïf échoue

Le récupérateur vectoriel recherchera des fragments qui « ressemblent » à la requête. Dans notre liste de documents étendue, il est fort probable qu'il récupère un contexte déroutant pour le LLM.

Les `top-k=3` fragments qu'il trouve seront probablement :

1. « Panasonic a un partenariat de longue date pour fabriquer des batteries... » (Pertinent : « Panasonic », « partenariat », « batteries »)
    
2. « Tesla développe des véhicules électriques et s'appuie sur une technologie de batterie avancée... » (Pertinent : « Tesla », « batterie »)
    
3. « Toyota fabrique également des batteries et a discuté de la technologie des batteries... » (Pertinent : « Toyota », « fabrique des batteries »)
    

Lorsque le LLM reçoit ce contexte, il a « Panasonic », « Tesla » et « Toyota » tous dans un contexte de « batterie ». Le fragment pour Panasonic ne le lie pas explicitement à Tesla. Le fragment pour Toyota mentionne également des batteries. Le LLM, forcé de synthétiser une réponse, peut déduire *incorrectement* un partenariat qui n'existe pas (comme avec Toyota) ou énoncer les faits sans confirmer la relation.

#### Pourquoi le GraphRAG réussit

Le Knowledge Graph n'est pas vulnérable à ce genre de « débordement sémantique ». Il ne se soucie pas de savoir si les Nodes sont « sémantiquement proches » les uns des autres.

Notre fonction `query_explicit_relation` pose une question structurelle très spécifique : « Partir du Node **'Tesla'** et ne renvoyer *que* les Nodes qui lui sont connectés par un Edge avec l'étiquette *exacte* **'partners_with'** ».

Le graphe parcourt alors ses Edges et n'en trouve qu'un seul : `("Tesla", "Panasonic", {"label": "partners_with"})`. Il lui est structurellement impossible d'halluciner un partenariat avec « Toyota » car aucun Edge `partners_with` de ce type n'existe pour Tesla dans le graphe.

```python
# Naive RAG
docs_s5 = [
	# --- The "Answer" Chunks (ambiguous) ---
	Document(page_content="Tesla develops electric vehicles and relies on advanced battery tech."),
	Document(page_content="Panasonic has a long-standing partnership to manufacture batteries for electric vehicles."),

	# --- "Noise" Chunks (to create a false signal) ---
	Document(page_content="Toyota also manufactures batteries and hybrid powertrains for its own vehicle lineup."),
	Document(page_content="Tesla, Panasonic, and Toyota are all major players in the EV and battery supply chain."),
	Document(page_content="A new partnership for solid-state batteries was announced, but it did not involve Tesla.")
]
query_s5 = "Who did Tesla partner with on batteries?"
rag_chain_s5 = create_rag_chain(docs_s5)
print(f"Naive RAG Answer: {rag_chain_s5.invoke(query_s5)}")
#
# GraphRAG Pattern
graph_s5 = KnowledgeGraph()
edges_s5 = [
	("Tesla", "Panasonic", {"label": "partners_with"}),
	("Toyota", "Toyota", {"label": "partners_with"}),
]
graph_s5.add_data(edges=edges_s5)
print(f"GraphRAG Answer: {graph_s5.query_explicit_relation('Tesla', 'partners_with')}") 
```

**Sortie :**

```python
Naive RAG Answer: Based on the context, Panasonic has a partnership to manufacture batteries, and Tesla relies on advanced battery tech. Toyota also manufactures batteries.
GraphRAG Answer: Tesla partnered with Panasonic.
```

## Réflexions finales

Le RAG standard est un outil essentiel, mais sa force réside dans la **récupération, pas dans le raisonnement**. Il faiblit lorsqu'une véritable synthèse est requise.

Vous constaterez peut-être qu'un LLM puissant comme Gemini peut encore répondre correctement à certains des scénarios simples de cet article. Les cinq modèles présentés ici sont destinés à forger l'intuition. Ils démontrent ce qui *peut* mal tourner et ce qui *tourne* mal à mesure que votre base de connaissances s'agrandit et se complexifie.

Le véritable échec du RAG naïf apparaît lorsque vous le nourrissez d'informations de plus en plus contradictoires, ambiguës ou incomplètes. Ce contexte « bruyant » force le LLM soit à halluciner des connexions, soit à échouer totalement dans son raisonnement.

En passant d'un « sac de fragments » à un Knowledge Graph structuré, vous construisez un système plus fiable et intelligent. Vous donnez à votre système une « mémoire globale » de la manière dont les faits se connectent explicitement, lui permettant de répondre à des questions complexes en parcourant un chemin vérifié plutôt qu'en devinant simplement à partir d'un nuage de texte sémantiquement similaire.