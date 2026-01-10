---
title: 'Modèles de langage de nouvelle génération : Le manuel de la génération augmentée
  par récupération (RAG)'
date: '2024-06-11T21:18:00.000Z'
author: Vahe Aslanyan
authorURL: https://www.freecodecamp.org/news/author/vaheaslanyan/
originalURL: https://freecodecamp.org/news/retrieval-augmented-generation-rag-handbook
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/Next-Gen-Large-Language-Models-Cover-1--1-.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: 'LLM''s '
  slug: llms
- name: Machine Learning
  slug: machine-learning
seo_desc: "Retrieval Augmented Generation (RAG) signifies a transformative advancement\
  \ in large language models (LLMs). It combines the generative prowess of transformer\
  \ architectures with dynamic information retrieval. \nThis integration allows LLMs\
  \ to access a..."
---


La génération augmentée par récupération (RAG - Retrieval Augmented Generation) représente une avancée transformative dans les grands modèles de langage (LLM). Elle combine la prouesse générative des architectures transformer avec la récupération dynamique d'informations.

<!-- more -->

Cette intégration permet aux LLM d'accéder à des connaissances externes pertinentes et de les incorporer lors de la génération de texte, ce qui donne des résultats plus précis, contextuels et factuellement cohérents.

L'évolution des premiers systèmes basés sur des règles vers des modèles neuronaux sophistiqués comme BERT et GPT-3 a ouvert la voie au RAG, en remédiant aux limites de la mémoire paramétrique statique. De plus, l'avènement du RAG multimodal étend ces capacités en incorporant divers types de données tels que les images, l'audio et la vidéo. Cela améliore la richesse et la pertinence du contenu généré.

Ce changement de paradigme améliore non seulement la précision et l'interprétabilité des sorties des LLM, mais soutient également des applications innovantes dans divers domaines.

### Voici ce que nous allons couvrir :

1.  **[Chapitre 1. Introduction au RAG][1]**  
    – [**1.1** Qu'est-ce que le RAG ? Un aperçu][2]  
    – [**1.2** Comment le RAG résout des problèmes complexes][3]
2.  **[Chapitre 2. Fondements techniques][4]**  
    – [**2.1** Transition des LM neuronaux vers le RAG][5]  
    – [**2.2** Comprendre la mémoire du RAG : Paramétrique vs Non-Paramétrique][6]  
    – [**2.3** RAG multimodal : Intégrer plusieurs types de données][7]
3.  **[Chapitre 3. Mécanismes fondamentaux][8]**  
    – [**3.1** La puissance de la combinaison de la récupération d'information et de la génération dans le RAG][9]  
    – [**3.2** Stratégies d'intégration pour les récupérateurs et les générateurs][10]
4.  **[Chapitre 4. Applications et cas d'utilisation][11]**  
    – [**4.1** Le RAG à l'œuvre : de la QA à l'écriture créative][12]  
    – [**4.2** Le RAG pour les langues à faibles ressources : étendre la portée et les capacités][13]
5.  **[Chapitre 5. Techniques d'optimisation][14]**  
    – [**5.1** Techniques de récupération avancées pour optimiser les systèmes RAG][15]
6.  **[Chapitre 6. Défis et innovations][16]**  
    – [**6.1** Défis actuels et orientations futures pour le RAG][17]  
    – [**6.2** Accélération matérielle et déploiement efficace des systèmes RAG][18]
7.  **[Chapitre 7. Réflexions finales][19]**  
    – [**7.1** L'avenir du RAG : conclusions et réflexions][20]

## Prérequis

Pour aborder le contenu axé sur les grands modèles de langage (LLM) comme la génération augmentée par récupération (RAG), deux prérequis essentiels sont :

1.  **Fondamentaux du Machine Learning** : Comprendre les concepts et algorithmes de base du machine learning est crucial, en particulier leur application aux architectures de réseaux neuronaux.
2.  **Traitement du langage naturel (NLP)** : La connaissance des techniques de NLP, y compris le prétraitement de texte, la tokenization et l'utilisation d'embeddings, est vitale pour travailler avec les modèles de langage.

## Chapitre 1 : Introduction au RAG

La génération augmentée par récupération (RAG) révolutionne le traitement du langage naturel en combinant la récupération d'informations et les modèles génératifs. Le RAG accède dynamiquement à des connaissances externes, améliorant ainsi la précision et la pertinence du texte généré.

Ce chapitre explore les mécanismes, les avantages et les défis du RAG. Nous plongeons dans les techniques de récupération, l'intégration avec les modèles génératifs et l'impact sur diverses applications.

Le RAG atténue les hallucinations, incorpore des informations à jour et résout des problèmes complexes. Nous discutons également de défis tels que la récupération efficace et les considérations éthiques. Ce chapitre offre une compréhension complète du potentiel transformateur du RAG dans le traitement du langage naturel.

### 1.1 Qu'est-ce que le RAG ? Un aperçu

La génération augmentée par récupération (RAG) représente un changement de paradigme dans le traitement du langage naturel, intégrant de manière fluide les forces de la récupération d'informations et des modèles de langage génératifs. Les systèmes RAG exploitent des sources de connaissances externes pour améliorer la précision, la pertinence et la cohérence du texte généré, remédiant ainsi aux limites de la mémoire purement paramétrique des modèles de langage traditionnels. ([Lewis et al., 2020][21])

En récupérant et en incorporant dynamiquement des informations pertinentes pendant le processus de génération, le RAG permet des sorties plus ancrées contextuellement et factuellement cohérentes dans un large éventail d'applications, de la réponse aux questions et des systèmes de dialogue à la synthèse et à l'écriture créative. ([Petroni et al., 2021][22])

![arxiv.org](https://arxiv.org/html/2312.10997v5/extracted/2312.10997v5/images/RAG_case.png) _Fonctionnement d'un système RAG - arxiv.org_

Le mécanisme central du RAG implique deux composants principaux : la récupération et la génération.

Le composant de récupération recherche efficacement dans de vastes bases de connaissances pour identifier les informations les plus pertinentes en fonction de la requête d'entrée ou du contexte. Des techniques telles que la récupération éparse (sparse retrieval), qui utilise des index inversés et la correspondance basée sur les termes, et la récupération dense (dense retrieval), qui emploie des représentations vectorielles denses et la similitude sémantique, sont utilisées pour optimiser le processus de récupération. ([Karpukhin et al., 2020][23])

Les informations récupérées sont ensuite intégrées dans le modèle génératif, généralement un grand modèle de langage comme GPT ou T5, qui synthétise le contenu pertinent en une réponse cohérente et fluide. ([Izacard & Grave, 2021][24])

L'intégration de la récupération et de la génération dans le RAG offre plusieurs avantages par rapport aux modèles de langage traditionnels. En ancrant le texte généré dans des connaissances externes, le RAG réduit considérablement l'incidence des hallucinations ou des sorties factuellement incorrectes. ([Shuster et al., 2021][25])

Le RAG vous permet également d'incorporer des informations à jour, garantissant que les réponses générées reflètent les dernières connaissances et développements dans un domaine donné. ([Lewis et al., 2020][26]) Cette adaptabilité est particulièrement cruciale dans des domaines tels que la santé, la finance et la recherche scientifique, où la précision et l'actualité des informations sont de la plus haute importance. ([Petroni et al., 2021][27])

Cependant, le développement et le déploiement de systèmes RAG présentent également des défis importants. La récupération efficace à partir de bases de connaissances à grande échelle, l'atténuation des hallucinations et l'intégration de diverses modalités de données font partie des obstacles techniques à surmonter. ([Izacard & Grave, 2021][28])

De plus, les considérations éthiques, telles que la garantie d'une récupération et d'une génération d'informations impartiales et équitables, sont cruciales pour le déploiement responsable des systèmes RAG. ([Bender et al., 2021][29]) Le développement de métriques et de cadres d'évaluation complets capturant l'interaction entre la précision de la récupération et la qualité générative est essentiel pour évaluer l'efficacité des systèmes RAG. ([Lewis et al., 2020][30])

Alors que le domaine du RAG continue d'évoluer, les futures directions de recherche se concentrent sur l'optimisation des processus de récupération, l'expansion des capacités multimodales, le développement d'architectures modulaires et l'établissement de cadres d'évaluation robustes. ([Izacard & Grave, 2021][31]) Ces avancées amélioreront l'efficacité, la précision et l'adaptabilité des systèmes RAG, ouvrant la voie à des applications plus intelligentes et polyvalentes dans le traitement du langage naturel.

Voici un exemple de code Python de base illustrant une configuration de génération augmentée par récupération (RAG) utilisant les bibliothèques populaires LangChain et FAISS :

```
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader  
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

# 1. Load and Embed Documents
loader = TextLoader('your_documents.txt')  # Replace with your document source
documents = loader.load()
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(documents, embeddings)

# 2. Retrieve Relevant Documents
def retrieve_docs(query):
    return vectorstore.similarity_search(query)

# 3. Set Up RAG Chain
llm = OpenAI(temperature=0.1)  # Adjust temperature for response creativity
chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vectorstore.as_retriever())

# 4. Use the RAG Model
def get_answer(query):
    return chain.run(query)

# Example usage
query = "What are the key features of Company X's latest product?"
answer = get_answer(query)
print(answer)

#Example Usage Company History
query = "When was Company X founded and who were the founders?"
answer = get_answer(query)
print(answer)

#Example Usage Financial Performance 
query = "What were Company X's revenue and profit figures for the last quarter?"
answer = get_answer(query)
print(answer)

#Example Usage Future Outlook 
query = "What are Company X's plans for expansion or new product development?"
answer = get_answer(query)
print(answer)
```

En exploitant la puissance de la récupération et de la génération, le RAG est porteur d'immenses promesses pour transformer la façon dont nous interagissons avec l'information et la générons, révolutionnant divers domaines et façonnant l'avenir de l'interaction homme-machine.

### 1.2 Comment le RAG résout des problèmes complexes

La génération augmentée par récupération (RAG) offre une solution puissante aux problèmes complexes avec lesquels les grands modèles de langage (LLM) traditionnels ont du mal, en particulier dans les scénarios impliquant de vastes quantités de données non structurées.

L'un de ces problèmes est la capacité à engager des conversations significatives sur des documents spécifiques ou du contenu multimédia, comme des vidéos YouTube, sans fine-tuning préalable ou entraînement explicite sur le matériel cible.

Les LLM traditionnels, malgré leurs impressionnantes capacités génératives, sont limités par leur mémoire paramétrique, qui est fixée au moment de l'entraînement. ([Lewis et al., 2020][32]) Cela signifie qu'ils ne peuvent pas accéder directement ou incorporer de nouvelles informations au-delà de leurs données d'entraînement, ce qui rend difficile la tenue de discussions informées sur des documents ou des vidéos non vus.

Par conséquent, les LLM peuvent générer des réponses incohérentes, non pertinentes ou factuellement incorrectes lorsqu'ils sont sollicités par des requêtes liées à un contenu spécifique. ([Petroni et al., 2021][33])

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-58.png) _Points de douleur du RAG - DataScienceDojo_

Le RAG remédie à cette limitation en intégrant un composant de récupération qui permet au modèle d'accéder dynamiquement à des informations pertinentes provenant de sources de connaissances externes et de les incorporer pendant le processus de génération.

En tirant parti de techniques de récupération avancées, telles que la récupération dense de passages (dense passage retrieval) ([Karpukhin et al., 2020][34]) ou la recherche hybride ([Izacard & Grave, 2021][35]), les systèmes RAG peuvent identifier efficacement les passages ou segments les plus pertinents d'un document ou d'une vidéo donnés en fonction du contexte conversationnel.

Par exemple, considérons un scénario où un utilisateur souhaite engager une conversation sur une vidéo YouTube spécifique traitant d'un sujet scientifique. Un système RAG peut d'abord transcrire le contenu audio de la vidéo, puis indexer le texte résultant en utilisant des représentations vectorielles denses.

Ensuite, lorsque l'utilisateur pose une question liée à la vidéo, le composant de récupération du système RAG peut identifier rapidement les passages les plus pertinents de la transcription sur la base de la similitude sémantique entre la requête et le contenu indexé.

Les passages récupérés sont ensuite transmis au modèle génératif, qui synthétise une réponse cohérente et informative répondant directement à la question de l'utilisateur tout en ancrant la réponse dans le contenu de la vidéo. ([Shuster et al., 2021][36])

Cette approche permet aux systèmes RAG d'engager des conversations éclairées sur un large éventail de documents et de contenus multimédias sans avoir besoin d'un fine-tuning explicite. En récupérant et en incorporant dynamiquement des informations pertinentes, le RAG peut générer des réponses plus précises, contextuellement pertinentes et factuellement cohérentes par rapport aux LLM traditionnels. ([Lewis et al., 2020][37])

De plus, la capacité du RAG à gérer des données non structurées provenant de diverses modalités, telles que le texte, les images et l'audio, en fait une solution polyvalente pour les problèmes complexes impliquant des sources d'information hétérogènes. ([Izacard & Grave, 2021][38]) À mesure que les systèmes RAG continuent d'évoluer, leur potentiel pour s'attaquer à des problèmes complexes dans divers domaines augmente.

En exploitant des techniques de récupération avancées et l'intégration multimodale, le RAG peut permettre des agents conversationnels plus intelligents et conscients du contexte, des systèmes de recommandation personnalisés et des applications à forte intensité de connaissances.

À mesure que la recherche progresse dans des domaines tels que l'indexation efficace, l'alignement cross-modal et l'intégration récupération-génération, le RAG jouera sans aucun doute un rôle crucial pour repousser les limites de ce qui est possible avec les modèles de langage et l'intelligence artificielle.

## Chapitre 2 : Fondements techniques

Ce chapitre plonge dans le monde fascinant de la génération augmentée par récupération (RAG) multimodale, une approche de pointe qui transcende les limites des modèles traditionnels basés sur le texte.

En intégrant de manière fluide diverses modalités de données telles que les images, l'audio et la vidéo avec les grands modèles de langage (LLM), le RAG multimodal permet aux systèmes d'IA de raisonner sur un paysage informationnel plus riche.

Nous explorerons les mécanismes derrière cette intégration, tels que l'apprentissage contrastif (contrastive learning) et l'attention cross-modale, et comment ils permettent aux LLM de générer des réponses plus nuancées et contextuellement pertinentes.

Bien que le RAG multimodal offre des avantages prometteurs tels qu'une précision améliorée et la capacité de prendre en charge de nouveaux cas d'utilisation comme la réponse visuelle aux questions (VQA), il présente également des défis uniques. Ces défis incluent le besoin de jeux de données multimodaux à grande échelle, une complexité de calcul accrue et le potentiel de biais dans les informations récupérées.

En nous lançant dans ce voyage, nous allons non seulement découvrir le potentiel transformateur du RAG multimodal, mais aussi examiner de manière critique les obstacles qui nous attendent, ouvrant la voie à une compréhension plus profonde de ce domaine en évolution rapide.

### 2.1 Des LM neuronaux au RAG

L'évolution des modèles de langage a été marquée par une progression constante, des premiers systèmes basés sur des règles aux modèles statistiques et neuronaux de plus en plus sophistiqués.

À l'origine, les modèles de langage s'appuyaient sur des règles artisanales et des connaissances linguistiques pour générer du texte, ce qui donnait des résultats rigides et limités. L'avènement des modèles statistiques, tels que les modèles n-grammes, a introduit une approche axée sur les données qui apprenait des motifs à partir de grands corpus, permettant une génération de langage plus naturelle et cohérente. ([Redis][39])

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-7.png) _Fonctionnement du RAG - promptingguide.ai_

Cependant, c'est l'émergence des modèles basés sur les réseaux neuronaux, en particulier les architectures transformer comme BERT et GPT-3, qui a révolutionné le domaine du traitement du langage naturel (NLP).

Ces modèles, connus sous le nom de grands modèles de langage (LLM), exploitent la puissance du deep learning pour capturer des motifs linguistiques complexes et générer du texte de type humain avec une fluidité et une cohérence sans précédent. ([Yarnit][40]) La complexité et l'échelle croissantes des LLM, avec des modèles comme GPT-3 affichant plus de 175 milliards de paramètres, ont conduit à des capacités remarquables dans des tâches telles que la traduction de langues, la réponse aux questions et la création de contenu.

Malgré leurs performances impressionnantes, les LLM traditionnels souffrent de limitations dues à leur dépendance à une mémoire purement paramétrique. ([StackOverflow][41]) Les connaissances encodées dans ces modèles sont statiques, limitées par la date de coupure de leurs données d'entraînement.

Par conséquent, les LLM peuvent générer des sorties factuellement incorrectes ou incohérentes avec les dernières informations. De plus, l'absence d'accès explicite à des sources de connaissances externes entrave leur capacité à fournir des réponses précises et contextuellement pertinentes aux requêtes exigeant des connaissances approfondies.

La génération augmentée par récupération (RAG) émerge comme une solution de rupture pour remédier à ces limitations. En intégrant de manière fluide des capacités de récupération d'informations avec la puissance générative des LLM, le RAG permet aux modèles d'accéder dynamiquement à des connaissances pertinentes provenant de sources externes et de les incorporer pendant le processus de génération.

Cette fusion de la mémoire paramétrique et non paramétrique permet aux LLM équipés du RAG de produire des sorties non seulement fluides et cohérentes, mais aussi factuellement précises et contextuellement informées.

Le RAG représente un bond en avant significatif dans la génération de langage, fusionnant les forces des LLM avec les vastes connaissances disponibles dans les référentiels externes. En exploitant le meilleur des deux mondes, le RAG permet aux modèles de générer du texte plus fiable, informatif et aligné avec les connaissances du monde réel.

Ce changement de paradigme ouvre de nouvelles possibilités pour les applications de NLP, de la réponse aux questions et la création de contenu aux tâches à forte intensité de connaissances dans des domaines tels que la santé, la finance et la recherche scientifique.

### 2.2 Mémoire paramétrique vs non paramétrique

La mémoire paramétrique fait référence aux connaissances stockées dans les paramètres des modèles de langage pré-entraînés, tels que BERT et GPT-4. Ces modèles apprennent à capturer des motifs et des relations linguistiques à partir de vastes quantités de données textuelles pendant le processus d'entraînement, encodant ces connaissances dans leurs millions ou milliards de paramètres.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-8.png) _Backprop de bout en bout via q et p0 - miro.medium.com_

Les points forts de la mémoire paramétrique incluent :

*   **Fluidité** : Les modèles de langage pré-entraînés génèrent du texte de type humain avec une fluidité et une cohérence remarquables, capturant les nuances et le style du langage naturel. ([Redis][42] et [Lewis et al][43].)
*   **Généralisation** : Les connaissances encodées dans les paramètres du modèle lui permettent de se généraliser à de nouvelles tâches et domaines, activant des capacités de transfer learning et de few-shot learning. ([Redis][44] et [Lewis et al][45].)

Cependant, la mémoire paramétrique présente également des limites importantes :

*   **Erreurs factuelles** : Les modèles de langage peuvent générer des sorties incohérentes avec les faits du monde réel, car leurs connaissances sont limitées aux données sur lesquelles ils ont été entraînés.
*   **Connaissances obsolètes** : Les connaissances encodées dans les paramètres du modèle deviennent périmées avec le temps, car elles sont fixées au moment de l'entraînement et ne reflètent pas les mises à jour ou les changements dans le monde réel.
*   **Coût de calcul élevé** : L'entraînement de grands modèles de langage nécessite des quantités massives de ressources informatiques et d'énergie, ce qui rend la mise à jour de leurs connaissances coûteuse et chronophage.
*   **Connaissances générales** : Les connaissances capturées par les modèles de langage sont larges et générales, manquant de la profondeur et de la spécificité requises pour de nombreuses applications spécialisées.

En revanche, la mémoire non paramétrique fait référence à l'utilisation de sources de connaissances explicites, telles que des bases de données, des documents et des graphes de connaissances, pour fournir des informations à jour et précises aux modèles de langage. Ces sources externes servent de forme de mémoire complémentaire, permettant aux modèles d'accéder à des informations pertinentes et de les récupérer à la demande pendant le processus de génération.

Les avantages de la mémoire non paramétrique incluent :

*   **Informations à jour** : Les sources de connaissances externes peuvent être facilement mises à jour et maintenues, garantissant que le modèle a accès aux informations les plus récentes et les plus précises.
*   **Réduction des hallucinations** : "En récupérant des informations pertinentes à partir de sources externes, le RAG réduit considérablement l'incidence des hallucinations ou des sorties génératives factuellement incorrectes." ([Lewis et al.][46] et [Guu et al.][47])
*   **Connaissances spécifiques au domaine** : La mémoire non paramétrique permet aux modèles de tirer parti de connaissances spécialisées provenant de sources spécifiques au domaine, permettant des sorties plus précises et contextuellement pertinentes pour des applications particulières. ([Lewis et al.][48] et [Guu et al.][49])

Les limites de la mémoire paramétrique soulignent la nécessité d'un changement de paradigme dans la génération de langage.

> Le RAG représente une avancée significative dans le traitement du langage naturel en améliorant les performances des modèles génératifs grâce à l'intégration de techniques de récupération d'informations. ([Redis][50])

Voici le code Python pour démontrer la distinction entre la mémoire paramétrique et non paramétrique dans le contexte du RAG, avec une mise en évidence claire de la sortie :

```
from sentence_transformers import SentenceTransformer
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.llms import OpenAI


# Sample Document Collection (assume more substantial documents in a real scenario)
documents = [
    "The Large Hadron Collider (LHC) is the world's largest and most powerful particle accelerator.",
    "The LHC is located at CERN, near Geneva, Switzerland.",
    "The LHC is used to study the fundamental particles of matter.",
    "In 2012, the LHC discovered the Higgs boson, a particle that gives mass to other particles.",
]

# 1. Non-Parametric Memory (Retrieval with Embeddings)
model_name = "sentence-transformers/all-mpnet-base-v2"
embeddings = HuggingFaceEmbeddings(model_name=model_name)
vectorstore = FAISS.from_documents(documents, embeddings)

# 2. Parametric Memory (Language Model with Retrieval)
llm = OpenAI(temperature=0.1)  # Adjust temperature for response creativity
chain = RetrievalQAWithSourcesChain.from_chain_type(llm=llm, chain_type="stuff", retriever=vectorstore.as_retriever())

# --- Queries and Responses ---

query = "What was discovered at the LHC in 2012?"
answer = chain.run(query)
print("Parametric (w/ Retrieval): ", answer["answer"])  

query = "Where is the LHC located?"
docs = vectorstore.similarity_search(query)  
print("Non-Parametric: ", docs[0].page_content)
```

### Sortie :

```
Parametric (w/ Retrieval):  The Higgs boson, a particle that gives mass to other particles, was discovered at the LHC in 2012.
Non-Parametric:  The LHC is located at CERN, near Geneva, Switzerland.
```

Et voici ce qui se passe dans ce code :

#### Mémoire paramétrique :

*   Exploite les vastes connaissances du LLM pour générer une réponse complète, incluant le fait crucial que le boson de Higgs donne de la masse aux autres particules. Le LLM est "paramétré" par ses données d'entraînement étendues.

#### Mémoire non paramétrique :

*   Effectue une recherche de similitude dans l'espace vectoriel, trouvant le document le plus pertinent qui répond directement à la question sur l'emplacement du LHC. Il ne synthétise pas de nouvelles informations, il récupère simplement le fait pertinent.

#### Différences clés :

| Caractéristique | Mémoire paramétrique | Mémoire non paramétrique |
| --- | --- | --- |
| **Stockage des connaissances** | Encodé dans les paramètres du modèle (poids) sous forme de représentations apprises. | Stocké directement sous forme de texte brut ou d'autres formats (ex: embeddings). |
| **Récupération** | Utilise les capacités génératives du modèle pour produire du texte pertinent à la requête basé sur ses connaissances apprises. | Implique la recherche de documents qui correspondent étroitement à la requête (ex: par similitude ou mots-clés). |
| **Flexibilité** | Très flexible et peut générer des réponses inédites, mais peut aussi halluciner (générer des infos incorrectes). | Moins flexible, mais moins sujet aux hallucinations car il repose sur des données existantes. |
| **Style de réponse** | Peut produire des réponses plus élaborées et nuancées, mais potentiellement avec plus d'infos non pertinentes. | Fournit des réponses directes et concises, mais peut manquer de contexte ou d'élaboration. |
| **Coût de calcul** | La génération de réponses peut être intensive en calcul, surtout pour les grands modèles. | La récupération peut être plus rapide, surtout avec des algorithmes d'indexation et de recherche efficaces. |

En combinant les forces de la mémoire paramétrique et non paramétrique, le RAG remédie aux limites des modèles de langage traditionnels et permet la génération de sorties plus précises, à jour et contextuellement pertinentes. ([Redis][51], [Lewis et al.][52], et [Guu et al.)][53]

### 2.3 RAG multimodal : Intégrer le texte

Le RAG multimodal étend le paradigme traditionnel du RAG basé sur le texte en incorporant plusieurs modalités de données, telles que les images, l'audio et la vidéo, afin d'améliorer les capacités de récupération et de génération des grands modèles de langage (LLM).

En exploitant des techniques d'apprentissage contrastif, les systèmes RAG multimodaux apprennent à intégrer des types de données hétérogènes dans un espace vectoriel partagé, permettant une récupération cross-modale fluide. Cela permet aux LLM de raisonner sur un contexte plus riche, combinant des informations textuelles avec des indices visuels et auditifs pour générer des sorties plus nuancées et contextuellement pertinentes. ([Shen et al.][54])

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-9.png) _Le diagramme illustre un système de recommandation où un grand modèle de langage traite la requête d'un utilisateur en embeddings, qui sont ensuite mis en correspondance par similitude cosinus dans une base de données vectorielle contenant des embeddings de texte et d'image, pour récupérer et recommander les éléments les plus pertinents. - opendatascience.com_

Une approche clé du RAG multimodal est l'utilisation de modèles basés sur les transformers comme ViLBERT et LXMERT qui emploient des mécanismes d'attention cross-modale. Ces modèles peuvent prêter attention à des régions pertinentes dans les images ou à des segments spécifiques dans l'audio/vidéo tout en générant du texte, capturant des interactions fines entre les modalités. Cela permet des réponses plus ancrées visuellement et contextuellement. ([Protecto.ai][55])

L'intégration du texte avec d'autres modalités dans les pipelines RAG implique des défis tels que l'alignement des représentations sémantiques entre différents types de données et la gestion des caractéristiques uniques de chaque modalité pendant le processus d'encodage. Des techniques telles que l'encodage spécifique à la modalité et la cross-attention sont utilisées pour relever ces défis. ([Zhu et al.][56])

Cependant, les avantages potentiels du RAG multimodal sont significatifs, notamment une précision, une contrôlabilité et une interprétabilité améliorées du contenu généré, ainsi que la capacité de prendre en charge de nouveaux cas d'utilisation tels que la réponse visuelle aux questions et la création de contenu multimodal.

Par exemple, Li et al. (2020) ont proposé un cadre RAG multimodal pour la réponse visuelle aux questions qui récupère les images et les informations textuelles pertinentes pour générer des réponses précises, surpassant les approches précédentes de pointe sur des benchmarks comme VQA v2.0 et CLEVR. ([MyScale][57])

Malgré les résultats prometteurs, le RAG multimodal introduit également de nouveaux défis, tels qu'une complexité de calcul accrue, le besoin de jeux de données multimodaux à grande échelle et le potentiel de biais et de bruit dans les informations récupérées.

Les chercheurs explorent activement des techniques pour atténuer ces problèmes, telles que des structures d'indexation efficaces, des stratégies d'augmentation de données et des méthodes d'entraînement adverses. ([Sohoni et al.][58])

## Chapitre 3 : Mécanismes fondamentaux du RAG

Ce chapitre explore l'interaction complexe entre les récupérateurs et les modèles génératifs dans les systèmes de génération augmentée par récupération (RAG), soulignant leurs rôles cruciaux dans l'indexation, la récupération et la synthèse d'informations pour produire des réponses précises et contextuellement pertinentes.

Nous plongeons dans les nuances des techniques de récupération éparse et dense, en comparant leurs forces et faiblesses dans différents scénarios. De plus, nous examinons diverses stratégies pour intégrer les informations récupérées dans les modèles génératifs, telles que la concaténation et la cross-attention, et discutons de leur impact sur l'efficacité globale des systèmes RAG.

En comprenant ces stratégies d'intégration, vous obtiendrez des informations précieuses sur la manière d'optimiser les systèmes RAG pour des tâches et des domaines spécifiques, ouvrant la voie à une utilisation plus informée et efficace de ce puissant paradigme.

### 3.1 La puissance de la combinaison de la récupération d'information et de la génération dans le RAG

La génération augmentée par récupération (RAG) représente un paradigme puissant qui intègre de manière fluide la récupération d'informations avec les modèles de langage génératifs. Le RAG est composé de deux composants principaux, comme son nom l'indique : la Récupération et la Génération.

Le composant de récupération est responsable de l'indexation et de la recherche dans un vaste référentiel de connaissances, tandis que le composant de génération exploite les informations récupérées pour produire des réponses contextuellement pertinentes et factuellement précises. ([Redis][59] et [Lewis et al.][60])

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-10.png) _L'image montre un système RAG où une base de données vectorielle traite les données en morceaux (chunks), interrogés par un modèle de langage pour récupérer des documents pour l'exécution de tâches et des sorties précises. - superagi.com_

Le processus de récupération commence par l'indexation de sources de connaissances externes, telles que des bases de données, des documents et des pages web. ([Redis][61] et [Lewis et al.][62]) Les récupérateurs et les indexeurs jouent un rôle crucial dans ce processus, organisant et stockant efficacement les informations dans un format qui facilite la recherche et la récupération rapides.

Lorsqu'une requête est posée au système RAG, le récupérateur fouille la base de connaissances indexée pour identifier les éléments d'information les plus pertinents sur la base de la similitude sémantique et d'autres métriques de pertinence.

Une fois les informations pertinentes récupérées, le composant de génération prend le relais. Le contenu récupéré est utilisé pour prompter et guider le modèle de langage génératif, lui fournissant le contexte et l'ancrage factuel nécessaires pour générer des réponses précises et informatives.

Le modèle de langage emploie des techniques d'inférence avancées, telles que les mécanismes d'attention et les architectures transformer, pour synthétiser les informations récupérées avec ses connaissances préexistantes et générer un texte cohérent et fluide.

Le flux d'informations au sein d'un système RAG peut être illustré comme suit :

```
graph LR
A[Requête] --> B[Récupérateur]
B --> C[Base de connaissances indexée]
C --> D[Informations pertinentes]
D --> E[Générateur]
E --> F[Réponse]
```

Les avantages du RAG sont multiples :

> Cette fusion des capacités de récupération et de génération permet la création de réponses qui sont non seulement contextuellement appropriées mais aussi informées par les _informations_ les plus actuelles et précises disponibles. ([Guu et al.][63])

En exploitant des sources de connaissances externes, le RAG réduit considérablement l'incidence des hallucinations ou des sorties factuellement incorrectes, qui sont des pièges courants des modèles purement génératifs.

De plus, le RAG permet l'intégration d'informations à jour, garantissant que les réponses générées reflètent les dernières connaissances et développements dans un domaine donné. Ceci est particulièrement crucial dans des domaines tels que la santé, la finance et la recherche scientifique, où la précision et l'actualité des informations sont de la plus haute importance. ([Guu et al.][64] et [NVIDIA][65])

Le RAG présente également une adaptabilité remarquable, permettant aux modèles de langage de gérer une grande variété de tâches avec des performances accrues. En récupérant dynamiquement des informations pertinentes en fonction de la requête ou du contexte spécifique, le RAG permet aux modèles de générer des réponses adaptées aux exigences uniques de chaque tâche, qu'il s'agisse de réponse aux questions, de génération de contenu ou d'applications spécifiques à un domaine.

De nombreuses études ont démontré l'efficacité du RAG pour améliorer la précision factuelle, la pertinence et l'adaptabilité des modèles de langage génératifs.

Par exemple, Lewis et al. (2020) ont montré que le RAG surpassait les modèles purement génératifs sur une gamme de tâches de réponse aux questions, obtenant des résultats de pointe sur des benchmarks tels que Natural Questions et TriviaQA. ([Lewis et al.][66])

De même, Izacard et Grave (2021) ont démontré la supériorité du RAG sur les modèles de langage traditionnels dans la génération de texte long cohérent et factuellement cohérent.

La génération augmentée par récupération représente une approche transformative de la génération de langage, exploitant la puissance de la récupération d'informations pour améliorer la précision, la pertinence et l'adaptabilité des modèles génératifs.

En intégrant de manière fluide les connaissances externes aux capacités linguistiques préexistantes, le RAG ouvre de nouvelles possibilités pour le traitement du langage naturel et ouvre la voie à des systèmes de génération de langage plus intelligents et fiables.

### 3.2 Stratégies d'intégration récupérateur-générateur

Les systèmes de génération augmentée par récupération (RAG) reposent sur deux composants clés : les récupérateurs et les modèles génératifs. Les récupérateurs sont chargés de rechercher et de récupérer efficacement les informations pertinentes dans des bases de connaissances à grande échelle.

> "Cela implique deux phases principales, l'indexation et la recherche. L'indexation organise les documents pour faciliter une récupération efficace, en utilisant soit des index inversés pour la récupération éparse, soit un encodage vectoriel dense pour la récupération dense." ([Redis][67])

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-11.png) _Le modèle d'architecture du RAG - miro.medium.com_

Les techniques de récupération éparse (sparse retrieval), telles que TF-IDF et BM25, représentent les documents comme des vecteurs épars de haute dimension, où chaque dimension correspond à un terme unique dans le vocabulaire. La pertinence d'un document par rapport à une requête est déterminée par le chevauchement des termes, pondéré par leur importance.

Par exemple, en utilisant la bibliothèque populaire Elasticsearch, un récupérateur basé sur TF-IDF peut être implémenté comme suit :

```
from elasticsearch import Elasticsearch

es = Elasticsearch()
es.index(index="documents", doc_type="_doc", body={"text": "This is a sample document."})

query = "sample"
results = es.search(index="documents", body={"query": {"match": {"text": query}}})
```

Les techniques de récupération dense (dense retrieval), telles que la récupération dense de passages (DPR) et les modèles basés sur BERT, représentent les documents et les requêtes comme des vecteurs denses dans un espace d'embedding continu. La pertinence est déterminée par la similitude cosinus entre les vecteurs de la requête et du document.

Le DPR peut être implémenté en utilisant la bibliothèque Hugging Face Transformers :

```
from transformers import DPRContextEncoder, DPRQuestionEncoder

context_encoder = DPRContextEncoder.from_pretrained("facebook/dpr-ctx_encoder-single-nq-base")
question_encoder = DPRQuestionEncoder.from_pretrained("facebook/dpr-question_encoder-single-nq-base")

context_embeddings = context_encoder(documents)
query_embedding = question_encoder(query)

scores = torch.matmul(query_embedding, context_embeddings.transpose(0, 1))
```

Les modèles génératifs, tels que GPT et T5, sont utilisés dans le RAG pour générer des réponses cohérentes et contextuellement pertinentes basées sur les informations récupérées. Le fine-tuning de ces modèles sur des données spécifiques au domaine et l'emploi de techniques de prompt engineering peuvent améliorer considérablement leurs performances dans les systèmes RAG. ([DEV Community][68])

Les stratégies d'intégration déterminent comment le contenu récupéré est incorporé dans les modèles génératifs.

> "Le composant de génération utilise le contenu récupéré pour formuler des réponses cohérentes et contextuellement pertinentes avec les phases de prompting et d'inférence." ([Redis][69])

Deux approches courantes sont la concaténation et la cross-attention.

La concaténation consiste à ajouter les passages récupérés à la requête d'entrée, permettant au modèle génératif de prêter attention aux informations pertinentes pendant le processus de décodage.

Bien que simple à mettre en œuvre, cette approche peut éprouver des difficultés avec les séquences longues et les informations non pertinentes. ([DEV Community][70]) Les mécanismes de cross-attention, tels que RAG-Token et RAG-Sequence, permettent au modèle génératif de prêter attention sélectivement aux passages récupérés à chaque étape du décodage.

Cela permet un contrôle plus fin sur le processus d'intégration mais s'accompagne d'une complexité de calcul accrue.

Par exemple, RAG-Token peut être implémenté en utilisant la bibliothèque Hugging Face Transformers :

```
from transformers import RagTokenizer, RagRetriever, RagSequenceForGeneration

tokenizer = RagTokenizer.from_pretrained("facebook/rag-token-nq")
retriever = RagRetriever.from_pretrained("facebook/rag-token-nq", index_name="exact", use_dummy_dataset=True)
model = RagSequenceForGeneration.from_pretrained("facebook/rag-token-nq")

input_ids = tokenizer(query, return_tensors="pt").input_ids
retrieved_docs = retriever(input_ids)
generated_output = model.generate(input_ids, retrieved_docs=retrieved_docs)
```

Le choix du récupérateur, du modèle génératif et de la stratégie d'intégration dépend des exigences spécifiques du système RAG, telles que la taille et la nature de la base de connaissances, l'équilibre souhaité entre efficacité et efficacité, et le domaine d'application cible.

## Chapitre 4 : Applications et cas d'utilisation

Ce chapitre explore le potentiel transformateur de la génération augmentée par récupération (RAG) dans la révolution des langues à faibles ressources et des applications multilingues. Nous approfondissons des stratégies telles que la traduction de documents sources vers des langues riches en ressources, l'utilisation d'embeddings multilingues et l'emploi de l'apprentissage fédéré (federated learning) pour surmonter les limitations de données et les différences linguistiques.

De plus, nous abordons le défi critique de l'atténuation des hallucinations dans les systèmes RAG multilingues afin de garantir une génération de contenu précise et fiable. En explorant ces approches innovantes, ce chapitre offre un guide complet pour exploiter la puissance du RAG au service de l'inclusivité et de la diversité dans le traitement des langues.

### 4.1 Applications du RAG : de la QA à l'écriture créative

La génération augmentée par récupération (RAG) a trouvé de nombreuses applications pratiques dans divers domaines, illustrant son potentiel à révolutionner la façon dont nous interagissons avec l'information et la générons. En exploitant la puissance de la récupération et de la génération, les systèmes RAG ont démontré des améliorations significatives en termes de précision, de pertinence et d'engagement des utilisateurs.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-13.png) _Fonctionnement du RAG - miro.medium.com_

### Réponse aux questions (Question Answering)

Le RAG s'est avéré être un changement de donne dans le domaine de la réponse aux questions. En récupérant des informations pertinentes à partir de sources de connaissances externes et en les intégrant dans le processus de génération, les systèmes RAG peuvent fournir des réponses plus précises et contextuellement pertinentes aux requêtes des utilisateurs. ([LangChain][71] et [Django Stars][72])

Par exemple, Izacard et Grave (2021) ont proposé un modèle basé sur le RAG appelé Fusion-in-Decoder (FiD), qui a atteint des performances de pointe sur plusieurs benchmarks de réponse aux questions, notamment Natural Questions et TriviaQA. ([Izacard and Grave][73])

FiD exploite un récupérateur dense pour extraire des passages pertinents et un modèle génératif pour synthétiser les informations récupérées en une réponse cohérente, surpassant les modèles purement génératifs par une marge significative. ([Izacard and Grave][74])

### Systèmes de dialogue

Le RAG a également trouvé des applications dans la création d'agents conversationnels plus engageants et informatifs. En incorporant des connaissances externes via la récupération, les systèmes de dialogue basés sur le RAG peuvent générer des réponses qui sont non seulement contextuellement appropriées mais aussi factuellement ancrées. ([LlamaIndex][75] et [MyScale][76])

Shuster et al. (2021) ont introduit un système de dialogue basé sur le RAG appelé BlenderBot 2.0, qui a démontré des capacités conversationnelles améliorées par rapport à son prédécesseur. ([Shuster et al.][77])

BlenderBot 2.0 récupère des informations pertinentes à partir d'un ensemble diversifié de sources de connaissances, y compris Wikipédia, des articles de presse et les réseaux sociaux, lui permettant d'engager des conversations plus informées et cohérentes sur un large éventail de sujets. ([Shuster et al.][78])

### Synthèse (Summarization)

Le RAG s'est montré prometteur pour améliorer la qualité des résumés générés en incorporant des informations pertinentes provenant de multiples sources. ([Hyperight][79]) Pasunuru et al. (2021) ont proposé un modèle de synthèse basé sur le RAG appelé PEGASUS-X, qui récupère et intègre des passages pertinents de documents externes pour générer des résumés plus informatifs et cohérents.

PEGASUS-X a surpassé les modèles purement génératifs sur plusieurs benchmarks de synthèse, démontrant l'efficacité de la récupération pour améliorer la précision factuelle et la pertinence des résumés générés.

### Écriture créative

Le potentiel du RAG s'étend au-delà des domaines factuels et s'aventure dans le domaine de l'écriture créative. En récupérant des passages pertinents dans un corpus diversifié d'œuvres littéraires, les systèmes RAG peuvent générer des histoires ou des articles originaux et engageants.

Rashkin et al. (2020) ont introduit un modèle d'écriture créative basé sur le RAG appelé CTRL-RAG, qui récupère des passages pertinents dans un jeu de données de fiction à grande échelle et les intègre dans le processus de génération. CTRL-RAG a démontré sa capacité à générer des histoires cohérentes et stylistiquement consistantes, illustrant le potentiel du RAG dans les applications créatives.

### Études de cas

Plusieurs articles de recherche et projets ont démontré l'efficacité du RAG dans divers domaines.

Par exemple, Lewis et al. (2020) ont introduit le cadre RAG et l'ont appliqué à la réponse aux questions en domaine ouvert, atteignant des performances de pointe sur le benchmark Natural Questions. ([Lewis et al.][80]) Ils ont souligné les défis d'une récupération efficace et l'importance du fine-tuning du modèle génératif sur les passages récupérés.

Dans une autre étude de cas, Petroni et al. (2021) ont appliqué le RAG à la tâche de fact-checking, démontrant sa capacité à récupérer des preuves pertinentes et à générer des verdicts précis. Ils ont mis en évidence le potentiel du RAG pour lutter contre la désinformation et améliorer la fiabilité des systèmes d'information.

L'impact du RAG sur l'expérience utilisateur et les métriques commerciales a été significatif. En fournissant des réponses plus précises et informatives, les systèmes basés sur le RAG ont amélioré la satisfaction et l'engagement des utilisateurs. ([LlamaIndex][81] et [MyScale][82])

Dans le cas des agents conversationnels, le RAG a permis des interactions plus naturelles et cohérentes, entraînant une augmentation de la rétention et de la fidélité des utilisateurs. ([LlamaIndex][83] et [MyScale][84]) Dans le domaine de l'écriture créative, le RAG a le potentiel de rationaliser les processus de création de contenu et de générer de nouvelles idées, économisant du temps et des ressources pour les entreprises.

Comme vous pouvez le voir, les applications pratiques du RAG couvrent un large éventail de domaines, de la réponse aux questions et des systèmes de dialogue à la synthèse et à l'écriture créative. En exploitant la puissance de la récupération et de la génération, le RAG a démontré des améliorations significatives en termes de précision, de pertinence et d'engagement des utilisateurs.

À mesure que le domaine continue d'évoluer, nous pouvons nous attendre à voir des applications plus innovantes du RAG, transformant la façon dont nous interagissons avec l'information et la générons dans divers contextes.

### 4.2 Le RAG pour les langues à faibles ressources et les contextes multilingues

Exploiter la puissance de la génération augmentée par récupération (RAG) pour les langues à faibles ressources et les contextes multilingues n'est pas seulement une opportunité, c'est une nécessité. Avec plus de 7 000 langues parlées dans le monde, dont beaucoup manquent de ressources numériques substantielles, le défi est clair : comment s'assurer que ces langues ne sont pas laissées pour compte à l'ère du numérique ?

### La traduction comme pont

Une stratégie efficace consiste à traduire les documents sources dans une langue plus riche en ressources avant l'indexation. Cette approche tire parti des vastes corpus disponibles dans des langues comme l'anglais, améliorant considérablement la précision et la pertinence de la récupération.

En traduisant les documents en anglais, vous pouvez puiser dans les vastes ressources et les techniques de récupération avancées déjà développées pour les langues à hautes ressources, améliorant ainsi les performances des systèmes RAG dans les contextes à faibles ressources.

### Embeddings multilingues

Les avancées récentes dans les embeddings de mots multilingues offrent une autre solution prometteuse. En créant des espaces d'embedding partagés pour plusieurs langues, vous pouvez améliorer les performances translingues même pour les langues à très faibles ressources.

La recherche a montré que l'incorporation de langues intermédiaires avec des embeddings de haute qualité peut combler le fossé entre des paires de langues distantes, améliorant ainsi la qualité globale des embeddings multilingues.

Cette méthode améliore non seulement la précision de la récupération, mais garantit également que le contenu généré est contextuellement pertinent et linguistically cohérent.

### Apprentissage fédéré (Federated Learning)

L'apprentissage fédéré présente une approche novatrice pour surmonter les contraintes de partage de données et les différences linguistiques. En affinant les modèles sur des sources de données décentralisées, vous pouvez préserver la vie privée des utilisateurs tout en améliorant les performances du modèle dans plusieurs langues.

Cette méthode a démontré une précision supérieure de 6,9 % et une réduction de 99 % des paramètres d'entraînement par rapport aux méthodes traditionnelles, ce qui en fait une solution très efficace pour les systèmes RAG multilingues.

### Atténuation des hallucinations

L'un des défis critiques du déploiement de systèmes RAG dans des contextes multilingues est l'atténuation des hallucinations — les cas où le modèle génère des informations factuellement incorrectes ou non pertinentes.

Les techniques RAG avancées, telles que le RAG modulaire, introduisent de nouveaux modules et des stratégies de fine-tuning pour résoudre ce problème. En mettant continuellement à jour la base de connaissances et en employant des métriques d'évaluation rigoureuses, vous pouvez réduire considérablement l'incidence des hallucinations et garantir que le contenu généré est à la fois précis et fiable.

### Mise en œuvre pratique

Pour mettre en œuvre ces stratégies efficacement, considérez les étapes pratiques suivantes :

1.  **Exploiter la traduction** : Traduisez les documents en langues à faibles ressources vers une langue à hautes ressources comme l'anglais avant l'indexation.
2.  **Utiliser des embeddings multilingues** : Incorporez des langues intermédiaires avec des embeddings de haute qualité pour améliorer les performances translingues.
3.  **Adopter l'apprentissage fédéré** : Affinez les modèles sur des sources de données décentralisées pour améliorer les performances tout en préservant la confidentialité.
4.  **Atténuer les hallucinations** : Employez des techniques RAG avancées et des mises à jour continues de la base de connaissances pour garantir la précision factuelle.

En adoptant ces stratégies, vous pouvez améliorer considérablement les performances des systèmes RAG dans les contextes multilingues et à faibles ressources, garantissant qu'aucune langue n'est laissée pour compte dans la révolution numérique.

## Chapitre 5 : Techniques d'optimisation

Ce chapitre explore les techniques de récupération avancées qui sous-tendent l'efficacité des systèmes de génération augmentée par récupération (RAG). Nous examinons comment l'optimisation des morceaux (chunks), l'intégration de métadonnées, l'indexation basée sur les graphes, les techniques d'alignement, la recherche hybride et le re-ranking améliorent la précision, la pertinence et l'exhaustivité de la récupération d'informations.

En comprenant ces méthodes de pointe, vous obtiendrez un aperçu de la manière dont les systèmes RAG évoluent, passant de simples moteurs de recherche à des fournisseurs d'informations intelligents capables de comprendre des requêtes complexes et de fournir des réponses précises et contextuellement pertinentes.

### 5.1 Techniques de récupération avancées pour optimiser les systèmes RAG

Les systèmes de génération augmentée par récupération (RAG) révolutionnent la façon dont nous accédons à l'information et l'utilisons. Le cœur de ces systèmes réside dans leur capacité à récupérer efficacement les informations pertinentes.

Plongeons plus profondément dans les techniques de récupération avancées qui permettent aux systèmes RAG de fournir des réponses précises, contextuellement pertinentes et complètes.

### Optimisation des morceaux (Chunk Optimization) : Maximiser la pertinence par une récupération granulaire

Dans le monde des systèmes RAG, les documents volumineux peuvent être écrasants. L'optimisation des morceaux résout ce défi en décomposant les textes étendus en unités plus petites et plus maniables appelées "chunks". Cette granularité permet aux systèmes de récupération de cibler des sections spécifiques de texte qui s'alignent sur les termes de la requête, améliorant ainsi la précision et l'efficacité.

L'art de l'optimisation des morceaux réside dans la détermination de la taille idéale du morceau et de son chevauchement (overlap). Un morceau trop petit peut manquer de contexte, tandis qu'un morceau trop grand peut diluer la pertinence. Le chunking dynamique, une technique qui adapte la taille du morceau en fonction de la structure et de la sémantique du contenu, garantit que chaque morceau est cohérent et contextuellement significatif.

### Intégration de métadonnées : Exploiter la puissance des balises d'information

Les métadonnées, ces informations souvent négligées qui accompagnent les documents, peuvent être une mine d'or pour les systèmes de récupération. En intégrant des métadonnées telles que le type de document, l'auteur, la date de publication et les balises thématiques, les systèmes RAG peuvent effectuer des recherches plus ciblées.

La récupération par auto-requête (self-query retrieval), une technique rendue possible par l'intégration de métadonnées, permet au système de générer des requêtes supplémentaires basées sur les résultats initiaux. Ce processus itératif affine la recherche, garantissant que les documents récupérés correspondent non seulement à la requête, mais répondent également aux exigences spécifiques et aux besoins contextuels de l'utilisateur.

### Structures d'indexation avancées : Réseaux basés sur les graphes pour les requêtes complexes

Les méthodes d'indexation traditionnelles, comme les index inversés et les encodages vectoriels denses, ont des limites face aux requêtes complexes impliquant plusieurs entités et leurs relations. Les index basés sur les graphes offrent une solution en organisant les documents et leurs connexions dans une structure de graphe.

Cette organisation de type graphe permet un parcours et une récupération efficaces des documents connexes, même dans des scénarios complexes. L'indexation hiérarchique et la recherche de plus proches voisins approximatifs (ANN) améliorent encore la scalabilité et la vitesse des systèmes de récupération basés sur les graphes.

### Techniques d'alignement : Garantir la précision et réduire les hallucinations

La crédibilité des systèmes RAG repose sur leur capacité à fournir des informations précises. Les techniques d'alignement, telles que l'entraînement contre-factuel (counterfactual training), répondent à cette préoccupation. En exposant le modèle à des scénarios hypothétiques, l'entraînement contre-factuel lui apprend à distinguer les faits du monde réel des informations générées, réduisant ainsi les hallucinations.

Dans les systèmes RAG multimodaux, qui intègrent des informations provenant de diverses sources comme le texte et les images, l'apprentissage contrastif joue un rôle crucial. Cette technique aligne les représentations sémantiques de différentes modalités de données, garantissant que les informations récupérées sont cohérentes et intégrées contextuellement.

### Recherche hybride : Allier la précision des mots-clés et la compréhension sémantique

La recherche hybride combine le meilleur des deux mondes : la rapidité et la précision de la recherche par mots-clés avec la compréhension sémantique de la recherche vectorielle. Initialement, une recherche par mots-clés réduit rapidement le pool de documents potentiels.

Ensuite, une recherche vectorielle affine les résultats sur la base de la similitude sémantique. Cette approche est particulièrement efficace lorsque les correspondances exactes de mots-clés sont essentielles, mais qu'une compréhension plus profonde de l'intention de la requête est également nécessaire pour une récupération précise.

### Re-ranking : Affiner la pertinence pour une réponse optimale

Dans l'étape finale de la récupération, le re-ranking intervient pour affiner les résultats. Des modèles de machine learning, tels que les cross-encoders, réévaluent les scores de pertinence des documents récupérés. En traitant la requête et les documents ensemble, ces modèles acquièrent une compréhension plus profonde de leur relation.

Cette comparaison nuancée garantit que les documents les mieux classés s'alignent véritablement avec la requête et le contexte de l'utilisateur, offrant une expérience de recherche plus satisfaisante et informative.

La puissance des systèmes RAG réside dans leur capacité à récupérer et à présenter des informations de manière fluide. En employant ces techniques de récupération avancées – optimisation des morceaux, intégration de métadonnées, indexation basée sur les graphes, techniques d'alignement, recherche hybride et re-ranking – les systèmes RAG deviennent plus que de simples moteurs de recherche. Ils évoluent vers des fournisseurs d'informations intelligents, capables de comprendre des requêtes complexes, de discerner les nuances et de fournir des réponses précises, pertinentes et dignes de confiance.

## Chapitre 6 : Défis et innovations

Ce chapitre examine les défis critiques et les orientations futures dans le développement et le déploiement des systèmes de génération augmentée par récupération (RAG).

Nous explorons les complexités de l'évaluation des systèmes RAG, notamment le besoin de métriques complètes et de cadres adaptatifs pour évaluer leurs performances avec précision. Nous abordons également les considérations éthiques telles que l'atténuation des biais et l'équité dans la récupération et la génération d'informations.

Nous examinons également l'importance de l'accélération matérielle et des stratégies de déploiement efficaces, en soulignant l'utilisation de matériel spécialisé et d'outils d'optimisation comme Optimum pour améliorer les performances et la scalabilité.

En comprenant ces défis et en explorant des solutions potentielles, ce chapitre fournit une feuille de route complète pour l'avancement continu et la mise en œuvre responsable de la technologie RAG.

### 6.1 Défis et orientations futures

Les systèmes de génération augmentée par récupération (RAG) ont démontré un potentiel remarquable pour améliorer la précision, la pertinence et la cohérence du texte généré. Cependant, le développement et le déploiement des systèmes RAG présentent également des défis importants qui doivent être relevés pour réaliser pleinement leur potentiel.

> "L'évaluation des systèmes RAG implique donc de prendre en compte un certain nombre de composants spécifiques et la complexité de l'évaluation globale du système." ([Salemi et al.][85])

### Défis dans l'évaluation des systèmes RAG

L'un des principaux défis techniques du RAG est de garantir une récupération efficace des informations pertinentes à partir de bases de connaissances à grande échelle. ([Salemi et al.][86] et [Yu et al.][87])

À mesure que la taille et la diversité des sources de connaissances continuent de croître, le développement de mécanismes de récupération scalables et robustes devient de plus en plus critique. Des techniques telles que l'indexation hiérarchique, la recherche de plus proches voisins approximatifs et des stratégies de récupération adaptatives doivent être explorées pour optimiser le processus de récupération.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-14.png) _Certains des éléments impliqués dans un système RAG - miro.medium.com_

Un autre défi majeur est l'atténuation du problème de l'hallucination, où le modèle génératif produit des informations factuellement incorrectes ou incohérentes.

Par exemple, un système RAG pourrait générer un événement historique qui n'a jamais eu lieu ou attribuer à tort une découverte scientifique. Bien que la récupération aide à ancrer le texte généré dans des connaissances factuelles, garantir la fidélité et la cohérence de la sortie générée reste un problème complexe.

Par exemple, un système RAG peut récupérer des informations précises sur une découverte scientifique à partir d'une source fiable comme Wikipédia, mais le modèle génératif peut toujours halluciner en combinant ces informations de manière incorrecte ou en ajoutant des détails inexistants.

Le développement de mécanismes efficaces pour détecter et prévenir les hallucinations est un domaine de recherche actif. Des techniques telles que la vérification des faits à l'aide de bases de données externes et le contrôle de cohérence par recoupement de plusieurs sources sont en cours d'exploration. Ces méthodes visent à garantir que le contenu généré reste précis et fiable, malgré les défis inhérents à l'alignement des processus de récupération et de génération.

L'intégration de sources de connaissances diverses, telles que des bases de données structurées, du texte non structuré et des données multimodales, pose des défis supplémentaires dans les systèmes RAG. ([Yu et al.][88] et [Zilliz][89]) L'alignement des représentations et de la sémantique à travers différentes modalités de données et formats de connaissances nécessite des techniques sophistiquées, telles que l'attention cross-modale et l'embedding de graphes de connaissances. Assurer la compatibilité et l'interopéabilité de diverses sources de connaissances est crucial pour le fonctionnement efficace des systèmes RAG. ([Zilliz][90])

Au-delà des défis techniques, les systèmes RAG soulèvent également d'importantes considérations éthiques. Garantir une récupération et une génération d'informations impartiales et équitables est une préoccupation majeure. Les systèmes RAG peuvent par inadvertance amplifier les biais présents dans les données d'entraînement ou les sources de connaissances, conduisant à des sorties discriminatoires ou trompeuses. ([Salemi et al.][91] et [Banafa][92])

Le développement de techniques pour détecter et atténuer les biais, telles que l'entraînement adverse et la récupération soucieuse de l'équité, est une direction de recherche importante. ([Banafa][93])

### Orientations futures de la recherche

Pour relever les défis de l'évaluation des systèmes RAG, plusieurs solutions potentielles et directions de recherche peuvent être explorées.

Le développement de métriques d'évaluation complètes capturant l'interaction entre la précision de la récupération et la qualité générative est crucial. ([Salemi et al.][94])

Des métriques évaluant la pertinence, la cohérence et l'exactitude factuelle du texte généré, tout en tenant compte de l'efficacité du composant de récupération, doivent être établies. ([Salemi et al.][95]) Cela nécessite une approche holistique qui dépasse les métriques traditionnelles comme BLEU et ROUGE et incorpore l'évaluation humaine et des mesures spécifiques aux tâches.

L'exploration de cadres d'évaluation adaptatifs et en temps réel est une autre direction prometteuse.

Les systèmes RAG opèrent dans des environnements dynamiques où les sources de connaissances et les exigences des utilisateurs peuvent évoluer avec le temps. ([Yu et al.][96]) Le développement de cadres d'évaluation capables de s'adapter à ces changements et de fournir un retour en temps réel sur les performances du système est essentiel pour une amélioration et un suivi continus.

Cela peut impliquer des techniques telles que l'apprentissage en ligne, l'apprentissage actif et l'apprentissage par renforcement pour mettre à jour les métriques et les modèles d'évaluation en fonction des retours des utilisateurs et du comportement du système. ([Yu et al.][97])

Des efforts de collaboration entre chercheurs, praticiens de l'industrie et experts du domaine sont nécessaires pour faire progresser le domaine de l'évaluation du RAG. L'établissement de benchmarks, de jeux de données et de protocoles d'évaluation standardisés peut faciliter la comparaison et la reproductibilité des systèmes RAG à travers différents domaines et applications. ([Salemi et al.][98] et [Banafa][99])

L'engagement avec les parties prenantes, y compris les utilisateurs finaux et les décideurs politiques, est crucial pour garantir que le développement et le déploiement des systèmes RAG s'alignent sur les valeurs sociétales et les principes éthiques. ([Banafa][100])

Ainsi, bien que les systèmes RAG aient montré un immense potentiel, relever les défis de leur évaluation est crucial pour leur adoption généralisée et la confiance qu'on leur accorde. En développant des métriques d'évaluation complètes, en explorant des cadres d'évaluation adaptatifs et en temps réel, et en favorisant les efforts de collaboration, nous pouvons ouvrir la voie à des systèmes RAG plus fiables, impartiaux et efficaces.

À mesure que le domaine continue d'évoluer, il est essentiel de prioriser les efforts de recherche qui non seulement font progresser les capacités techniques du RAG, mais garantissent également leur déploiement responsable et éthique dans des applications du monde réel.

### 6.2 Accélération matérielle et déploiement efficace des systèmes RAG

L'exploitation de l'accélération matérielle est essentielle pour le déploiement efficace des systèmes de génération augmentée par récupération (RAG). En déchargeant les tâches gourmandes en calcul sur du matériel spécialisé, vous pouvez améliorer considérablement les performances et la scalabilité de vos modèles RAG.

### Exploiter le matériel spécialisé

Les outils d'optimisation spécifiques au matériel d'Optimum offrent des avantages substantiels. Par exemple, le déploiement de systèmes RAG sur des processeurs Habana Gaudi peut entraîner une réduction notable de la latence d'inférence, tandis que les optimisations d'Intel Neural Compressor peuvent encore améliorer les métriques de latence. Le matériel AWS Inferentia, optimisé via Optimum Neuron, peut accroître les capacités de débit (throughput), rendant votre système RAG plus réactif et efficace.

### Optimiser l'utilisation des ressources

L'utilisation efficace des ressources est cruciale. Les optimisations d'Optimum ONNX Runtime peuvent conduire à une utilisation plus efficace de la mémoire, tandis que l'API BetterTransformer peut améliorer l'utilisation du CPU et du GPU. Ces optimisations garantissent que votre système RAG fonctionne à son efficacité maximale, réduisant les coûts opérationnels et améliorant les performances.

### Scalabilité et flexibilité

Optimum permet une transition fluide entre différents accélérateurs matériels, activant une scalabilité dynamique. Ce support multi-matériel vous permet de vous adapter aux variations de la demande de calcul sans reconfiguration majeure. De plus, les fonctionnalités de quantification et d'élagage (pruning) de modèles dans Optimum peuvent faciliter des tailles de modèles plus efficaces, rendant le déploiement plus facile et plus rentable.

### Études de cas et applications concrètes

Considérez l'application d'Optimum dans la récupération d'informations médicales. En tirant parti des optimisations spécifiques au matériel, les systèmes RAG peuvent gérer efficacement de grands jeux de données, offrant une récupération d'informations précise et rapide. Cela améliore non seulement la qualité des soins de santé, mais renforce également l'expérience utilisateur globale.

#### Étapes pratiques pour la mise en œuvre

1.  **Sélectionner le matériel approprié** : Choisissez des accélérateurs matériels comme Habana Gaudi ou AWS Inferentia en fonction de vos exigences de performance spécifiques.
2.  **Utiliser les outils d'optimisation** : Implémentez les outils d'optimisation d'Optimum pour améliorer la latence, le débit et l'utilisation des ressources.
3.  **Assurer la scalabilité** : Profitez du support multi-matériel pour faire évoluer dynamiquement votre système RAG selon les besoins.
4.  **Optimiser la taille du modèle** : Utilisez la quantification et l'élagage de modèles pour réduire la charge de calcul et faciliter le déploiement.

En intégrant ces stratégies, vous pouvez améliorer considérablement les performances, la scalabilité et l'efficacité de vos systèmes RAG, garantissant qu'ils sont bien équipés pour gérer des applications complexes du monde réel.

## Conclusion : Le potentiel transformateur du RAG

La génération augmentée par récupération (RAG) représente un paradigme transformateur dans le traitement du langage naturel, intégrant de manière fluide la puissance de la récupération d'informations aux capacités génératives des grands modèles de langage.

En exploitant des sources de connaissances externes, les systèmes RAG ont démontré des améliorations remarquables dans la précision, la pertinence et la cohérence du texte généré à travers un large éventail d'applications, de la réponse aux questions et des systèmes de dialogue à la synthèse et à l'écriture créative.

L'évolution des modèles de langage, des premiers systèmes basés sur des règles aux architectures neuronales de pointe comme BERT et GPT-3, a ouvert la voie à l'émergence du RAG. Les limites de la mémoire purement paramétrique des modèles de langage traditionnels, telles que les dates de coupure des connaissances et les incohérences factuelles, ont été efficacement traitées par l'incorporation de la mémoire non paramétrique via des mécanismes de récupération.

Les composants centraux des systèmes RAG, à savoir les récupérateurs et les modèles génératifs, travaillent en synergie pour produire des sorties contextuellement pertinentes et factuellement ancrées.

Les récupérateurs, employant des techniques telles que la récupération éparse et dense, fouillent efficacement de vastes bases de connaissances pour identifier les informations les plus pertinentes. Les modèles génératifs, s'appuyant sur des architectures comme GPT et T5, synthétisent le contenu récupéré en un texte cohérent et fluide.

Les stratégies d'intégration, telles que la concaténation et la cross-attention, déterminent comment les informations récupérées sont incorporées dans le processus de génération.

Les applications pratiques du RAG couvrent divers domaines, illustrant son potentiel à révolutionner diverses industries.

Dans la réponse aux questions, le RAG a considérablement amélioré la précision et la pertinence des réponses, permettant une récupération d'informations plus informative et fiable. Les systèmes de dialogue ont bénéficié du RAG, résultant en des conversations plus engageantes et cohérentes. Les tâches de synthèse ont vu leur qualité et leur cohérence renforcées par l'intégration d'informations pertinentes provenant de sources multiples. Même l'écriture créative a été explorée, avec des systèmes RAG générant des histoires originales et stylistiquement consistantes.

Cependant, le développement et l'évaluation des systèmes RAG présentent également des défis importants. La récupération efficace à partir de bases de connaissances à grande échelle, l'atténuation de l'hallucination et l'intégration de diverses modalités de données font partie des obstacles techniques à surmonter. Les considérations éthiques, telles que la garantie d'une récupération et d'une génération d'informations impartiales et équitables, sont cruciales pour le déploiement responsable des systèmes RAG.

Pour réaliser pleinement le potentiel du RAG, les futures directions de recherche doivent se concentrer sur le développement de métriques d'évaluation complètes capturant l'interaction entre la précision de la récupération et la qualité générative.

Des cadres d'évaluation adaptatifs et en temps réel capables de gérer la nature dynamique des systèmes RAG sont essentiels pour une amélioration et un suivi continus. Des efforts de collaboration entre chercheurs, praticiens de l'industrie et experts du domaine sont nécessaires pour établir des benchmarks, des jeux de données et des protocoles d'évaluation standardisés.

Alors que le domaine du RAG continue d'évoluer, il est porteur d'immenses promesses pour transformer la façon dont nous interagissons avec l'information et la générons. En exploitant la puissance de la récupération et de la génération, les systèmes RAG ont le potentiel de révolutionner divers domaines, de la récupération d'informations et des agents conversationnels à la création de contenu et à la découverte de connaissances.

La génération augmentée par récupération représente un jalon significatif dans le voyage vers une génération de langage plus intelligente, précise et contextuellement pertinente.

En comblant le fossé entre la mémoire paramétrique et non paramétrique, les systèmes RAG ont ouvert de nouvelles possibilités pour le traitement du langage naturel et ses applications.

À mesure que la recherche progresse et que les défis sont relevés, nous pouvons nous attendre à ce que le RAG joue un rôle de plus en plus central dans le façonnage de l'avenir de l'interaction homme-machine et de la génération de connaissances.

### À propos de l'auteur

Ici Vahe Aslanyan, au carrefour de l'informatique, de la science des données et de l'IA. Visitez [vaheaslanyan.com][101] pour voir un portfolio qui témoigne de précision et de progrès. Mon expérience fait le pont entre le développement full-stack et l'optimisation de produits d'IA, portée par la résolution de problèmes de manière inédite.

Avec un parcours incluant le lancement d'un [bootcamp de science des données de premier plan][102] et la collaboration avec les meilleurs spécialistes de l'industrie, mon objectif reste d'élever l'éducation technologique aux standards universels.

### Comment aller plus loin ?

Après avoir étudié ce guide, si vous souhaitez approfondir vos connaissances et que l'apprentissage structuré est votre style, envisagez de nous rejoindre chez [**LunarTech**][103]. Nous proposons des cours individuels et un Bootcamp en Science des Données, Machine Learning et IA.

Nous fournissons un programme complet qui offre une compréhension approfondie de la théorie, une mise en œuvre pratique concrète, un matériel d'entraînement étendu et une préparation aux entretiens sur mesure pour vous préparer au succès à votre propre rythme.

Vous pouvez consulter notre [Ultimate Data Science Bootcamp][104] et rejoindre [un essai gratuit][105] pour tester le contenu par vous-même. Il a été reconnu comme l'un des [Meilleurs Bootcamps de Science des Données de 2023][106] et a été présenté dans des publications prestigieuses comme [Forbes][107], [Yahoo][108], [Entrepreneur][109] et plus encore. C'est votre chance de faire partie d'une communauté qui prospère grâce à l'innovation et au savoir. Voici le message de bienvenue !

<iframe width="560" height="315" src="https://www.youtube.com/embed/c-SXFXegVTw" style="aspect-ratio: 16 / 9; width: 100%; height: auto;" title="YouTube video player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen="" loading="lazy"></iframe>

### Connectez-vous avec moi

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-57.png) _Newsletter [LunarTech][110]_

*   [Suivez-moi sur LinkedIn pour une multitude de ressources gratuites en CS, ML et IA][111]
*   [Visitez mon site web personnel][112]
*   Abonnez-vous à ma [Newsletter sur la Science des Données et l'IA][113]

Si vous voulez en savoir plus sur une carrière en Science des Données, Machine Learning et IA, et apprendre comment décrocher un emploi en Science des Données, vous pouvez télécharger ce [Manuel de carrière en Science des Données et IA][114] gratuit.

[1]: #heading-chapitre-1-introduction-au-rag
[2]: #heading-11-qu-est-ce-que-le-rag-un-apercu
[3]: #heading-12-comment-le-rag-resout-des-problemes-complexes
[4]: #heading-chapitre-2-fondements-techniques
[5]: #heading-21-des-lm-neuronaux-au-rag
[6]: #heading-22-memoire-parametrique-vs-non-parametrique
[7]: #heading-23-rag-multimodal-integrer-le-texte
[8]: #heading-chapitre-3-mecanismes-fondamentaux-du-rag
[9]: #heading-31-la-puissance-de-la-combinaison-de-la-recuperation-d-information-et-de-la-generation-dans-le-rag
[10]: #heading-32-strategies-d-integration-recuperateur-generateur
[11]: #heading-chapitre-4-applications-et-cas-d-utilisation
[12]: #heading-41-applications-du-rag-de-la-qa-a-l-ecriture-creative
[13]: #heading-42-le-rag-pour-les-langues-a-faibles-ressources-et-les-contextes-multilingues
[14]: #heading-chapitre-5-techniques-d-optimisation
[15]: #heading-51-techniques-de-recuperation-avancees-pour-optimiser-les-systemes-rag
[16]: #heading-chapitre-6-defis-et-innovations
[17]: #heading-61-defis-et-orientations-futures
[18]: #heading-62-acceleration-materielle-et-deploiement-efficace-des-systemes-rag
[19]: #heading-conclusion-le-potentiel-transformateur-du-rag
[20]: #heading-conclusion-le-potentiel-transformateur-du-rag
[21]: https://arxiv.org/abs/2005.11401
[22]: https://aclanthology.org/2021.acl-long.198/
[23]: https://aclanthology.org/2020.emnlp-main.550/
[24]: https://aclanthology.org/2021.naacl-main.395/
[25]: https://aclanthology.org/2021.acl-long.518/
[26]: https://arxiv.org/abs/2005.11401
[27]: https://aclanthology.org/2021.acl-long.198/
[28]: https://aclanthology.org/2021.naacl-main.395/
[29]: https://dl.acm.org/doi/10.1145/3442188.3445922
[30]: https://arxiv.org/abs/2005.11401
[31]: https://aclanthology.org/2021.naacl-main.395/
[32]: https://arxiv.org/abs/2005.11401
[33]: https://aclanthology.org/2021.acl-long.198/
[34]: https://aclanthology.org/2020.emnlp-main.550/
[35]: https://aclanthology.org/2021.naacl-main.395/
[36]: https://aclanthology.org/2021.acl-long.518/
[37]: https://arxiv.org/abs/2005.11401
[38]: https://aclanthology.org/2021.naacl-main.395/
[39]: https://redis.io/glossary/retrieval-augmented-generation/
[40]: https://www.yarnit.app/post/creating-impact-a-spotlight-on-6-practical-retrieval-augmented-generation-use-cases
[41]: https://stackoverflow.blog/2023/10/18/retrieval-augmented-generation-keeping-llms-relevant-and-current/
[42]: https://redis.io/glossary/retrieval-augmented-generation/
[43]: https://arxiv.org/abs/2405.07437
[44]: https://redis.io/glossary/retrieval-augmented-generation/
[45]: https://arxiv.org/abs/2405.07437
[46]: https://arxiv.org/abs/2405.07437
[47]: https://cloud.google.com/use-cases/retrieval-augmented-generation
[48]: https://arxiv.org/abs/2405.07437
[49]: https://cloud.google.com/use-cases/retrieval-augmented-generation
[50]: https://redis.io/glossary/retrieval-augmented-generation/
[51]: https://redis.io/glossary/retrieval-augmented-generation/
[52]: https://arxiv.org/abs/2405.07437
[53]: https://cloud.google.com/use-cases/retrieval-augmented-generation
[54]: https://aws.amazon.com/blogs/machine-learning/create-a-multimodal-assistant-with-advanced-rag-and-amazon-bedrock/
[55]: https://www.protecto.ai/blog/multimodal-retrieval-augmented-generation
[56]: https://aclanthology.org/2023.findings-emnlp.314v2.pdf
[57]: https://myscale.com/blog/mastering-multimodal-rag-beginners-guide/
[58]: https://developer.nvidia.com/blog/an-easy-introduction-to-multimodal-retrieval-augmented-generation/
[59]: https://redis.io/glossary/retrieval-augmented-generation/
[60]: https://arxiv.org/abs/2005.11401
[61]: https://redis.io/glossary/retrieval-augmented-generation/
[62]: https://arxiv.org/abs/2005.11401
[63]: https://arxiv.org/abs/2002.08909
[64]: https://arxiv.org/abs/2002.08909
[65]: https://developer.nvidia.com/blog/an-easy-introduction-to-multimodal-retrieval-augmented-generation/
[66]: https://arxiv.org/abs/2005.11401
[67]: https://redis.io/glossary/retrieval-augmented-generation/
[68]: https://dev.to/pavanbelagatti/wth-is-retrieval-augmented-generation-rag-2a5a
[69]: https://redis.io/glossary/retrieval-augmented-generation/
[70]: https://dev.to/pavanbelagatti/wth-is-retrieval-augmented-generation-rag-2a5a
[71]: https://python.langchain.com/v0.1/docs/use_cases/question_answering/
[72]: https://djangostars.com/blog/rag-question-answering-with-python/
[73]: https://arxiv.org/abs/2007.01282
[74]: https://arxiv.org/abs/2007.01282
[75]: https://docs.llamaindex.ai/en/latest/use_cases/q_and_a/
[76]: https://myscale.com/blog/benefits-rag-qa-system-question-answering/
[77]: https://arxiv.org/abs/2106.01437
[78]: https://arxiv.org/abs/2106.01437
[79]: https://hyperight.com/7-practical-applications-of-rag-models-and-their-impact-on-society/
[80]: https://proceedings.neurips.cc/paper/2020/file/6b493230205f780e1bc26945df7481e5-Paper.pdf
[81]: https://docs.llamaindex.ai/en/latest/use_cases/q_and_a/
[82]: https://myscale.com/blog/benefits-rag-qa-system-question-answering/
[83]: https://docs.llamaindex.ai/en/latest/use_cases/q_and_a/
[84]: https://myscale.com/blog/benefits-rag-qa-system-question-answering/
[85]: https://arxiv.org/abs/2404.13781
[86]: https://arxiv.org/abs/2404.13781
[87]: https://arxiv.org/abs/2405.07437
[88]: https://arxiv.org/abs/2405.07437
[89]: https://zilliz.com/blog/how-to-evaluate-retrieval-augmented-generation-rag-applications
[90]: https://zilliz.com/blog/how-to-evaluate-retrieval-augmented-generation-rag-applications
[91]: https://arxiv.org/abs/2404.13781
[92]: https://www.linkedin.com/pulse/retrieval-augmented-generation-rag-artificial-prof-ahmed-banafa-ono4c
[93]: https://www.linkedin.com/pulse/retrieval-augmented-generation-rag-artificial-prof-ahmed-banafa-ono4c
[94]: https://arxiv.org/abs/2404.13781
[95]: https://arxiv.org/abs/2404.13781
[96]: https://arxiv.org/abs/2405.07437
[97]: https://arxiv.org/abs/2405.07437
[98]: https://arxiv.org/abs/2404.13781
[99]: https://www.linkedin.com/pulse/retrieval-augmented-generation-rag-artificial-prof-ahmed-banafa-ono4c
[100]: https://www.linkedin.com/pulse/retrieval-augmented-generation-rag-artificial-prof-ahmed-banafa-ono4c
[101]: https://www.freecodecamp.org/news/p/61bdcc92-ed93-4dc6-aeca-03b14c584b30/vaheaslanyan.com
[102]: https://www.freecodecamp.org/news/p/ad4edb43-532a-430e-82b2-1fb2558b7f73/lunartech.ai
[103]: https://lunartech.ai/
[104]: https://lunartech.ai/course-overview/
[105]: https://lunartech.ai/pricing/
[106]: https://www.itpro.com/business-strategy/careers-training/358100/best-data-science-boot-camps
[107]: https://www.forbes.com.au/brand-voice/uncategorized/not-just-for-tech-giants-heres-how-lunartech-revolutionizes-data-science-and-ai-learning/
[108]: https://finance.yahoo.com/news/lunartech-launches-game-changing-data-115200373.html?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAAM3JyjdXmhpYs1lerU37d64maNoXftMA6BYjYC1lJM8nVa_8ZwTzh43oyA6Iz0DfqLtjVHnknO0Zb8QTLIiHuwKzQZoodeM85hkI39fta3SX8qauBUsNw97AeiBDR09BUDAkeVQh6eyvmNLAGblVj3GSf1iCo81bwHQxknmhgng#
[109]: https://www.entrepreneur.com/ka/business-news/outpacing-competition-how-lunartech-is-redefining-the/463038
[110]: https://substack.com/@lunartech
[111]: https://ca.linkedin.com/in/vahe-aslanyan
[112]: https://vaheaslanyan.com/
[113]: https://tatevaslanyan.substack.com/
[114]: https://downloads.tatevaslanyan.com/six-figure-data-science-ebook