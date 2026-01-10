---
title: Alternatives à LangChain pour construire des workflows IA et agentiques
subtitle: ''
author: Maham Codes
co_authors: []
series: null
date: '2025-01-30T18:59:27.703Z'
originalURL: https://freecodecamp.org/news/langchain-alternatives-for-building-ai-and-agentic-workflows
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1738696551914/6800aa71-d6f2-472a-8982-35af81509813.png
tags:
- name: AI
  slug: ai
- name: llm
  slug: llm
seo_title: Alternatives à LangChain pour construire des workflows IA et agentiques
seo_desc: Building AI and agentic workflows is at the core of modern AI development
  in 2025. And LangChain has been the go-to framework for creating AI applications
  for a while now. But some developers are seeking alternatives that offer more flexibility,
  simp...
---

La construction de workflows IA et agentiques est au cœur du développement moderne de l'IA en 2025. Et LangChain a été le framework de référence pour créer des applications IA depuis un certain temps. Mais certains développeurs recherchent des alternatives offrant plus de flexibilité, de simplicité et de rentabilité.

Bien que LangChain ait permis un développement rapide d'applications alimentées par des LLM avec des outils pour le chaînage, les agents et la mémoire, son abstraction lourde, son débogage complexe et sa difficulté avec les cas d'utilisation réels en font souvent un outil plus adapté au prototypage qu'aux applications de niveau production.

Dans cet article, nous explorerons quelques alternatives puissantes à LangChain que vous pouvez essayer et qui vous aideront à construire des workflows IA et agentiques efficaces. Je passerai en revue les principales caractéristiques et les meilleurs cas d'utilisation de chacune afin que vous puissiez vous faire une bonne idée de la manière dont elles pourraient vous aider.

## Table des matières

1. [Qu'est-ce qu'un workflow IA et agentique ?](#heading-quest-ce-quun-workflow-ia-et-agentique)
    
2. [Langbase](#heading-langbase)
    
3. [LlamaIndex](#heading-llamaindex)
    
4. [AG2](#heading-ag2)
    
5. [Braintrust](#heading-braintrust)
    
6. [FlowiseAI](#heading-flowiseai)
    
7. [Conclusion 🙌](#heading-conclusion)
    

## Qu'est-ce qu'un workflow IA et agentique ?

Un **workflow IA** fait référence à une série de tâches exécutées par des systèmes IA, suivant généralement une séquence prédéfinie. Il gère des tâches comme l'extraction de données, le traitement et la génération de sorties basées sur des instructions claires.

Un **workflow agentique** va plus loin. Il implique que l'IA prenne l'initiative, prenne des décisions et gère des tâches de manière autonome. Dans les workflows agentiques, l'IA adapte ses actions en fonction de son environnement ou d'objectifs prédéfinis, souvent sans intervention humaine.

En bref, un workflow IA devient plus "agentique" lorsqu'il commence à penser, décider et agir de manière indépendante, agissant comme un agent intelligent. Plus l'IA peut prendre de décisions par elle-même, moins elle a besoin d'être sollicitée par un humain.

Maintenant que nous avons clarifié ce qu'est un workflow IA et agentique, examinons quelques autres outils et frameworks qui pourraient servir d'alternatives à LangChain, chacun offrant des capacités et des approches uniques que vous pouvez utiliser pour construire vos workflows IA et agentiques.

## Langbase

[Langbase](http://langbase.com) est une plateforme de développement IA composable et serverless avec orchestration multi-agents et mémoire à long terme avancée. Elle est conçue pour un développement et un déploiement IA fluides. Langbase prend en charge plus de 100 LLM via une seule API, garantissant une expérience développeur unifiée, avec un changement et une optimisation faciles des modèles.

💡 L'orchestration multi-agents fait référence à la coordination de plusieurs agents IA pour travailler ensemble sur des tâches. Elle implique de contrôler le flux des tâches, de s'assurer que les agents travaillent dans la bonne séquence et de coordonner leurs actions pour maximiser l'efficacité.

### Produits Langbase

La plateforme offre les produits suivants :

1. **Pipe Agents** : Les agents Pipe sur Langbase sont différents des autres agents. Ce sont des agents IA serverless avec des outils agentiques qui peuvent fonctionner avec n'importe quel langage ou framework. Les agents Pipe sont facilement déployables, et avec une seule API, ils vous permettent de connecter 100+ LLM à n'importe quelle donnée pour construire n'importe quel workflow API développeur.
    
2. **Memory Agents** : Les agents mémoire de Langbase (solution de mémoire à long terme) sont conçus pour acquérir, traiter, conserver et récupérer des informations de manière fluide. Ils attachent dynamiquement des données privées à n'importe quel LLM, permettant des réponses contextuelles en temps réel et réduisant les hallucinations. La mémoire, lorsqu'elle est connectée à un agent Pipe, devient un agent mémoire.
    
3. **BaseAI.dev** : BaseAI est le premier framework web IA open-source. Avec lui, vous pouvez commencer à construire des pipes, outils et mémoire agentiques locaux, et déployer en serverless avec une seule commande.
    
4. **AI Studio** : Langbase AI Studio fournit un terrain de jeu pour collaborer sur des agents IA, la mémoire et les outils. Avec lui, vous pouvez construire, collaborer, tester et déployer des agents Pipe et mémoire (RAG).
    
5. **LangUI** : LangUI est une bibliothèque Tailwind gratuite et open-source avec des composants prêts à l'emploi conçus pour les projets IA et GPT.
    
6. **Langbase SDK** : Langbase offre un SDK IA TypeScript qui simplifie le développement. Il vous aide à intégrer facilement les LLM, à créer des agents mémoire et à les enchaîner dans des pipelines, le tout avec un code minimal. Il prend en charge JavaScript, TypeScript, Node.js, Next.js, React et plus encore, permettant un développement plus rapide avec une excellente expérience développeur.
    

![Source : Langbase](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcniBaqv7TmuUdmUqWejNJiulwjZDMf6Jg_Eh-AajXof7kfPVDKbiPXTQ3kgP-mXLA8cLZM87HYiL0_e6txSimQlcoPg90DCQ2lVYte1D_fzWiEGMsDP6IQMGiAO42a3-011owoHg?key=U363uJCJj9tPrezMPf7fa2Fc align="left")

### Fonctionnalités clés

* **Plateforme API-first** : API simples (Pipe et agents mémoire) pour une intégration facile avec une documentation claire et un support communautaire.
    
    💡 Utilisez l'API Pipe pour gérer les agents Pipe dans votre compte Langbase. Elle dispose de points de terminaison pour créer, mettre à jour, lister et exécuter. L'API Memory de Langbase vous permet de gérer les mémoires et les documents dans votre compte Langbase de manière programmatique.
    
* **Environnement serverless** : Langbase fonctionne dans un environnement entièrement serverless, éliminant le besoin pour les développeurs de gérer l'infrastructure. Cela simplifie la mise à l'échelle et le déploiement, permettant aux développeurs de tous niveaux de compétence, et pas seulement aux experts en IA/ML, de construire, mettre à l'échelle et déployer des agents IA de manière fluide.
    
* **Infrastructure composable** : Langbase est la **première plateforme IA composable**. Elle est construite pour la flexibilité et la modularité. Les développeurs peuvent combiner des modèles en pipelines, chacun se concentrant sur une tâche spécifique. Cela rend le développement plus facile, montre le coût de chaque étape et permet de créer des expériences hautement personnalisées. En choisissant le meilleur modèle pour chaque tâche, Langbase vous aide à construire des workflows efficaces qui répondent à différents besoins.
    
    💡 L'IA composable signifie combiner différents modèles IA comme des blocs de construction pour créer des solutions personnalisées. C'est simple, flexible et s'adapte à vos besoins.
    
* **Efficacité des coûts** : Langbase offre significativement plus de valeur à un coût inférieur à celui de LangChain, avec des coûts de dépassement de seulement 2 $ pour 1 000 exécutions contre 5 $ pour LangChain.
    

### Cas d'utilisation

Langbase est parfait pour les développeurs recherchant des solutions rentables avec un changement de modèle fluide via une seule API. Il est bien adapté pour les projets nécessitant une infrastructure IA composable/modulaire et des fonctionnalités avancées de mémoire à long terme. Il excelle également dans la construction de workflows autonomes avec collaboration multi-agents.

Voici quelques applications spécifiques que vous pouvez construire en utilisant Langbase :

* **Agent de support client** : Construisez des agents/applications de support client capables de gérer des conversations complexes et contextuelles à travers les tickets de support, les e-mails et les chats, fournissant des résolutions précises et efficaces. Consultez les agents de support client [ici](https://langbase.com/docs/solutions/customer-support).
    
* **Agent de codage** : Créez des applications multi-agents qui assistent les développeurs en générant des extraits de code, en déboguant et en révisant le code en temps réel, améliorant la productivité dans les workflows de développement logiciel. Voici un exemple de démonstration d'agent de codage [demo](https://code-alchemist.langbase.dev/).
    

### Commencer avec Langbase

* Pour commencer avec Langbase, inscrivez-vous gratuitement [ici](https://langbase.com/signup).
    
* Pour créer un agent Pipe, tapez simplement pipe.new dans la barre de recherche.
    
* Pour créer un agent mémoire, tapez rag.new dans la barre de recherche.

## LlamaIndex

[LlamaIndex](https://www.llamaindex.ai/) est un framework open-source construit pour les applications RAG et les systèmes basés sur des agents. Il fournit des outils essentiels pour ingérer, structurer et connecter des données privées ou spécifiques à un domaine aux LLM, permettant une génération de texte plus précise et fiable.

Avec son support pour la construction d'agents et l'intégration de pipelines RAG dans le cadre d'un ensemble d'outils plus large, LlamaIndex offre la flexibilité nécessaire pour gérer des tâches complexes.

### Fonctionnalités clés

* **Chargement de données** : LlamaIndex rend l'importation de données fluide avec le support de 150+ sources, y compris les API, les PDF, les documents et les bases de données SQL. En utilisant des **connecteurs de données (LlamaHub)**, les développeurs peuvent intégrer des données diverses dans leurs applications LLM sans effort. Les exemples incluent l'extraction de données en temps réel à partir d'API, le chargement d'informations structurées à partir de MySQL ou PostgreSQL, et l'ingestion de texte à partir de PDF ou de rapports.
    
    💡 Les chargeurs de données sont des utilitaires qui permettent d'ingérer facilement des données pour la recherche et la récupération par un grand modèle de langage.
    
* **Indexation** : L'indexation organise et stocke les données pour une récupération facile et rapide, créant des structures comme des index vectoriels ou documentaires. Avec LlamaIndex, vous pouvez stocker et indexer des données sur plusieurs fournisseurs (par exemple, des bases de données vectorielles, documentaires, graphiques et SQL).
    
* **Requêtage** : Le requêtage récupère des informations spécifiques à partir de données indexées, permettant des recherches et des workflows avancés comme les pipelines RAG pour des réponses contextuelles. Pour cela, LlamaIndex vous permet de construire des workflows de requête avancés avec récupération, post-traitement et synthèse de réponse pour les chaînes de prompts et les pipelines RAG.
    
    💡 Un **Pipeline de requête** dans LlamaIndex est un moyen simple de concevoir des workflows de requête pour différentes tâches comme le RAG et l'extraction de données structurées. Il vous aide à définir comment les requêtes interagissent avec vos données, rendant facile la gestion des workflows de base et avancés. Lisez à propos des pipelines de requête LlamaIndex [ici](https://www.llamaindex.ai/blog/introducing-query-pipelines-025dc2bb0537).
    
* **Évaluations** : Inclut des modules pour évaluer la qualité de la récupération et des réponses, améliorant le suivi des performances.
    

### Cas d'utilisation

LlamaIndex est préféré pour l'indexation fluide des données et la récupération rapide, le rendant plus adapté aux applications RAG prêtes pour la production. D'autre part, LangChain fournit plus de composants prêts à l'emploi, facilitant la création de diverses architectures LLM.

Voici quelques applications RAG spécifiques que vous pouvez construire en utilisant LlamaIndex :

* **Assistant d'analyses financières** : Construisez un assistant de connaissances pour les analystes financiers afin de récupérer des informations en temps réel à partir des données de marché, des rapports de résultats et des documents financiers internes, permettant une prise de décision plus rapide et une évaluation des risques.
    
* **Conseiller en fabrication** : Créez un assistant alimenté par l'IA pour rationaliser les workflows de production en accédant aux manuels d'équipement, aux journaux de maintenance et aux données de la chaîne d'approvisionnement, améliorant l'efficacité opérationnelle et réduisant les temps d'arrêt.
    

![Source : LlamaIndex](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeaMsX_VAc5eaX5XfO5fbZLa3Ak5yxQyKApHm1NcNR2iBtDovLuLBTXE2tUax73e9DZprnllnBdGva14hjGPPb1pzwiPn-TFa0Ckb0w6JbCeWQr8HAbWAq62sPdX8xfXCyFZ2UvYw?key=U363uJCJj9tPrezMPf7fa2Fc align="left")

### Commencer avec LlamaIndex

Vous pouvez commencer avec LlamaIndex en Python ou TypeScript en seulement 5 lignes de code.

1. Définissez la variable d'environnement `OPENAI_API_KEY` avec votre clé API OpenAI.
    
2. Installez la bibliothèque Python : `pip install llama-index`
    
3. Placez vos documents dans un dossier nommé `data`, puis utilisez ce code de démarrage pour les interroger :
    

```python
pythonCopyEditfrom llama_index.core import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()
response = query_engine.query("Votre question ici")
print(response)
```

Pour plus de détails, consultez leur [documentation](https://docs.llamaindex.ai/en/stable/#getting-started).

## AG2

[AG2](https://ag2.ai/) (anciennement AutoGen) est un framework open-source pour construire des agents IA et permettre la collaboration multi-agents. AG2 fournit un framework pour construire des workflows autonomes et la collaboration d'agents, simplifiant la création d'agents spécialisés qui peuvent travailler ensemble de manière fluide.

💡 La **collaboration multi-agents** fait référence à plusieurs agents travaillant ensemble vers un objectif commun, chacun effectuant des tâches et partageant des informations selon les besoins. Les agents peuvent être indépendants et spécialisés, mais ils collaborent pour accomplir une tâche.

### Fonctionnalités clés

* **Collaboration d'agents** : Prend en charge l'orchestration multi-agents pour une communication et une gestion des tâches fluides.
    
* **Rôles d'agents flexibles** : Définissez les comportements, rôles et workflows des agents avec un code intuitif. Attribuez des rôles spécifiques aux agents, tels que collecteur de données, analyste ou décideur, et faites-les interagir dans des conversations ou travailler de manière indépendante. Par exemple, un agent peut rassembler des informations, tandis qu'un autre les traite et fournit des insights. Ces conversations entre agents peuvent conduire à l'accomplissement de tâches, chaque agent contribuant en fonction de son rôle désigné, rendant les workflows plus dynamiques et efficaces.
    
* **Support humain dans la boucle** : AG2 permet une implication humaine fluide dans le workflow en permettant des méthodes d'entrée personnalisables, telles que des remplacements manuels ou des boucles de feedback. Il offre une transmission contextuelle, ce qui signifie que le système peut passer des tâches à un humain au bon moment, en fonction de conditions ou d'exigences spécifiques. De plus, des interfaces interactives sont fournies, permettant aux humains de réviser, approuver ou ajuster les actions des agents en temps réel, garantissant que le système reste aligné avec le jugement et la supervision humains.
    
* **Modèles de conversation** : Des modèles intégrés automatisent les tâches de coordination comme le routage des messages, la gestion d'état et la sélection dynamique des intervenants.
    

### Cas d'utilisation

AG2 se distingue par sa capacité à gérer des interactions complexes entre agents, ce qui en fait un excellent choix pour les workflows multi-agents nécessitant une collaboration humaine.

Voici quelques applications IA que vous pouvez construire en utilisant AG2 :

* **Pipelines de création et de révision de contenu** : Construisez des workflows collaboratifs où un agent génère du contenu écrit ou visuel, un autre s'assure de la conformité avec les directives, et un réviseur humain fournit des contributions créatives ou une approbation finale.
    
* **Plateformes d'éducation personnalisées** : Créez des assistants d'apprentissage où un agent sélectionne du contenu éducatif, un autre conçoit des parcours d'apprentissage personnalisés, et un troisième surveille les progrès des étudiants. Les enseignants ou mentors peuvent intervenir pour fournir des feedbacks personnalisés ou des ajustements au programme.
    

![Source : AG2](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcuX2p7__EXrxmGP6pFHPKNtQDz6_d6vUU3PFpSy-viwSBIYpti3JCdCQzw3vUmrGOhnUG7Z9JqVd_PKgil3OI6KD5gnEe5yBDA4ImZ_5Lq-f16iIJ5RiaD6DEJuyneXT6TLw-oCQ?key=U363uJCJj9tPrezMPf7fa2Fc align="left")

### Commencer avec AG2

AG2 nécessite **Python version >= 3.9, < 3.14**. Il peut être installé depuis pip :

```python
pip install ag2
```

Pour plus de détails, visitez la [documentation](https://docs.ag2.ai/docs/Getting-Started).

## Braintrust

[Braintrust](https://www.braintrust.dev/) est une plateforme complète pour évaluer, améliorer et déployer des grands modèles de langage (LLM) avec des outils pour l'ingénierie de prompts, la gestion des données et l'évaluation continue. Conçue pour rendre la construction d'applications IA plus robuste et itérative, Braintrust vous aide à prototyper rapidement avec différents prompts et modèles, à évaluer les performances avec des outils intégrés et à surveiller les interactions en temps réel.

### Fonctionnalités clés

* **Expérimentation itérative** : Prototypage et test rapides de prompts avec différents modèles dans le [playground](https://www.braintrust.dev/docs/guides/playground) intégré. Vous pouvez expérimenter avec des entrées de jeux de données réels, comparer les réponses entre les modèles (OpenAI, Anthropic, Mistral, Google, Meta, et plus), et affiner les performances dans le playground.
    
* **Insights de performance** : Évaluez les performances des modèles et des prompts avec des outils intégrés comme le playground de prompts, les imports de jeux de données et les fonctions de notation. Vous pouvez tester les sorties contre des données réelles, comparer les modèles et affiner les prompts de manière itérative. Utilisez des heuristiques ou des notations basées sur les LLM pour évaluer la précision, suivre les résultats et améliorer les performances au fil du temps dans l'UI ou le SDK de Braintrust.
    
* **Surveillance en temps réel** : Suivez les interactions IA avec des logs détaillés, capturant les entrées, les sorties et les métadonnées pour chaque requête. Braintrust log les traces des appels IA, les décomposant en spans pour identifier les problèmes, surveiller le comportement des utilisateurs et affiner les performances. Les logs s'intègrent de manière fluide avec les évaluations, créant une boucle de feedback pour l'amélioration continue des modèles.
    
* **Gestion centralisée des données** : Braintrust intègre les données de production, de staging et d'évaluations, vous permettant de suivre les changements, comparer les itérations et affiner les modèles au fil du temps. Le versioning garantit que vous pouvez revenir en arrière, auditer et épingler les évaluations à des versions spécifiques de jeux de données, soutenant l'expérimentation structurée et les révisions humaines dans la boucle pour une amélioration continue.
    
    💡 Les jeux de données vous permettent de collecter des données à partir de la production, du staging, des évaluations et même manuellement, puis d'utiliser ces données pour exécuter des évaluations et suivre les améliorations au fil du temps.
    

### Cas d'utilisation

Braintrust est idéal pour le développement et l'évaluation itératifs de modèles, en particulier pour les projets nécessitant des pipelines de test et de déploiement robustes. Il se distingue pour la construction d'applications LLM scalables, offrant des insights basés sur les données qui permettent une optimisation précise et une amélioration continue.

Voici quelques applications que vous pouvez construire avec Braintrust :

* **Évaluation d'un assistant de chat** : Avec Braintrust, vous pouvez évaluer un assistant de chat en vous assurant que l'IA conversationnelle maintient le contexte pour des réponses précises. Il permet des évaluations automatisées pour évaluer la qualité des réponses, gère les jeux de données pour affiner les cas de test et suit les performances pour une amélioration continue.
    
* **Barre de recherche IA** : Braintrust aide à optimiser la recherche alimentée par l'IA en garantissant la précision et la conscience du contexte. Il log les requêtes pour identifier les lacunes, évalue les résultats de recherche pour la pertinence et compare les versions de modèles pour suivre les améliorations.
    

### Commencer avec Braintrust

* Pour commencer, [inscrivez-vous](https://www.braintrust.dev/signup) sur Braintrust.
    
* Une fois inscrit, vous serez invité à créer une organisation gratuitement.
    
* Pour exécuter votre première évaluation, vous pouvez utiliser soit l'[UI](https://www.braintrust.dev/docs/start/eval-ui) soit le [code de démarrage](https://www.braintrust.dev/docs/start/eval-sdk) disponible. Installez le SDK Braintrust en utilisant cette commande :
    
    ```bash
    npm install braintrust autoevals
    ```
    
    Pour plus de détails, visitez la [documentation](https://www.braintrust.dev/docs/start).
    

![Source : Braintrust](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcwXfdLQfJnKfYu0kNauwNFALM0fZfDPiuajC8DgcImgdUL-UmGpzhFQhRVUPj9LPLoJM_UWz7eAEU_yqwepSfgyIbFQTNIqxnABuueLNWke74CMewIe1nsp9FzO8p7WqYZbYMHpA?key=U363uJCJj9tPrezMPf7fa2Fc align="left")

## FlowiseAI

[FlowiseAI](https://flowiseai.com/) est un outil open source low-code pour les développeurs afin de construire des flux d'orchestration LLM personnalisés et des agents IA. Avec son interface intuitive de glisser-déposer, Flowise rend la technologie LLM accessible à un public plus large, y compris ceux ayant peu ou pas d'expérience en codage.

### Fonctionnalités clés

* **Itération rapide** : L'approche low-code permet des itérations rapides, facilitant le passage des tests à la production en une fraction du temps.
    
* **Chatflow et orchestration LLM** : Connectez de manière fluide les LLM avec la mémoire, les chargeurs de données, la mise en cache et les outils de modération pour gérer la manière dont les modèles traitent les entrées, récupèrent les données pertinentes et génèrent des réponses. Cela garantit des interactions contrôlées entre les modèles, les entrées utilisateur et les sources de données externes pour des performances optimales.
    
* **100+ intégrations** : Connectez-vous facilement avec des outils comme Langchain et LlamaIndex pour améliorer vos workflows. Ces intégrations vous aident à lier des sources de données, gérer des tâches et ajouter des fonctionnalités supplémentaires, vous permettant de construire des applications IA personnalisées. Utilisez-les pour automatiser le travail, améliorer les performances des modèles ou étendre les capacités de votre système en fonction de vos besoins.
    
* **Agents et assistants** : Construisez des agents autonomes qui exécutent des tâches en utilisant des outils comme les multi-agents ou les agents séquentiels, améliorant les capacités de votre application. Ces agents peuvent interagir avec des sources de données externes et des outils, leur permettant d'effectuer des tâches spécialisées de manière efficace. Par exemple, Flowise propose deux approches pour créer des systèmes basés sur des agents : les Multi-Agents, qui travaillent ensemble de manière collaborative et spécialisée, et les Agents Séquentiels, qui traitent les tâches de manière structurée, étape par étape. En intégrant ces systèmes, vous pouvez automatiser des workflows complexes et améliorer l'exécution des tâches au sein de votre application.
    
* **Convivial pour les développeurs** : Étendez et intégrez avec vos applications en utilisant des API, des SDK et des options de chat intégrées, y compris le SDK React et les widgets intégrés.
    

### Cas d'utilisation

Flowise est idéal pour les développeurs ayant peu d'expérience en codage construisant des workflows LLM et les équipes ayant besoin de mises à jour rapides sans perdre de fonctionnalités. Il rend les workflows IA avancés faciles à utiliser, même pour les non-experts.

Il s'intègre avec des frameworks comme LangChain et LlamaIndex, ce qui en fait un choix idéal pour un développement IA simplifié. Mais il peut poser des défis pour ceux qui sont nouveaux dans les LLM, et les approches code-first peuvent être mieux adaptées pour les tâches hautement spécialisées.

Voici quelques exemples pratiques que vous pouvez construire en utilisant Flowise :

* **Interroger plusieurs documents** : Avec Flowise, vous pouvez construire des systèmes qui interrogent plusieurs documents en les téléchargeant sur Pinecone avec des métadonnées. Les agents outils aident le LLM à sélectionner le document approprié en fonction de la question.
    
* **Assistants personnels** : Développez des assistants capables de gérer des tâches, de planifier des rendez-vous et de fournir des rappels avec Flowise.
    

### Commencer avec FlowiseAI

* Pour commencer, installez Flowise localement en utilisant NPM.
    
    ```bash
    npm install -g flowise
    ```
    
    💡 Prérequis : assurez-vous que [NodeJS](https://nodejs.org/en/download) est installé sur la machine. Node `v18.15.0` ou `v20` et versions supérieures sont supportées.
    
* Démarrez Flowise en utilisant cette commande et ouvrez [localhost:3000](http://localhost:3000) :
    
    ```bash
    npx flowise start
    ```
    

Pour plus de détails, consultez ces étapes de [démarrage](https://docs.flowiseai.com/getting-started).

![Source : FlowiseAI](https://docs.flowiseai.com/~gitbook/image?url=https%3A%2F%2F1820151947-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fy8ifwt9BYklr92KDdr48%252Fuploads%252Fgit-blob-b24c3b670833a97778c5374146e905d026e0b122%252Fmulti-docs-upload.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=1196a9d4&sv=2 align="left")

## Conclusion 🙌

Les workflows IA et agentiques évoluent rapidement, et LangChain n'est plus la seule option. Le choix du bon outil dépend des besoins de votre projet : orchestration flexible des agents, réduction des coûts ou intégration fluide. Alors que nous avançons en 2025, ces alternatives méritent votre attention pour construire l'avenir de l'IA.

Merci d'avoir lu !