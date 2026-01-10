---
title: 'Le manuel de l''IA agentique : Un guide pour débutants sur les agents intelligents
  autonomes'
subtitle: ''
author: Balajee Asish Brahmandam
co_authors: []
series: null
date: '2025-05-28T14:22:20.929Z'
originalURL: https://freecodecamp.org/news/the-agentic-ai-handbook
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1748440644883/96088174-14a2-40da-9a7d-931253f3045b.png
tags:
- name: AI
  slug: ai
- name: agentic AI
  slug: agentic-ai
- name: agentic workflow
  slug: agentic-workflow
- name: openai
  slug: openai
- name: Chaos Engineering
  slug: chaos-engineering
- name: '#ai-tools'
  slug: ai-tools
- name: handbook
  slug: handbook
seo_title: 'Le manuel de l''IA agentique : Un guide pour débutants sur les agents
  intelligents autonomes'
seo_desc: You may have heard about “Agentic AI” systems and wondered what they’re
  all about. Well, in basic terms, the idea behind Agentic AI is that it can see its
  surroundings, set and pursue goals, plan and reason through many processes, and
  learn from expe...
---

Vous avez peut-être entendu parler des systèmes d'IA agentique et vous êtes demandé de quoi il s'agit. Eh bien, en termes simples, l'idée derrière l'IA agentique est qu'elle peut voir son environnement, fixer et poursuivre des objectifs, planifier et raisonner à travers de nombreux processus, et apprendre de l'expérience.

Contrairement aux chatbots ou aux logiciels basés sur des règles, l'IA agentique répond activement aux demandes des utilisateurs. Elle peut diviser les activités en tâches plus petites, prendre des décisions basées sur un objectif de haut niveau, et changer son comportement au fil du temps en utilisant des outils ou d'autres composants IA spécialisés.

Pour résumer, les [systèmes d'IA agentique](https://blogs.nvidia.com/blog/what-is-agentic-ai/) résolvent des problèmes complexes et multi-étapes de manière autonome en utilisant un raisonnement sophistiqué et une planification itérative. Dans le service client, par exemple, une IA agentique peut répondre à des questions, vérifier le compte d'un utilisateur, offrir des règlements de solde, et effectuer des transactions sans supervision humaine.

Ainsi, l'IA agentique est l'[IA avec agence](https://www.ibm.com/think/topics/agentic-ai). Étant donné un contexte de problème, elle fixe des objectifs, crée des stratégies, manipule l'environnement ou les outils logiciels, et apprend des résultats.

Mais pour le moment, la plupart des systèmes IA populaires sont réactifs ou non agentiques, effectuant un travail spécifique ou réagissant à des entrées sans préparation. Par exemple, Siri ou un classificateur d'images traditionnel utilisent des modèles ou des règles prédéfinis pour mapper les entrées aux sorties. Au lieu d'objectifs à long terme ou de processus multi-étapes, [l'IA réactive](https://www.ibm.com/think/topics) répond à des entrées spécifiques avec des actions prédéfinies. L'IA agentique ressemble davantage à un robot ou à un assistant personnel capable de gérer des chaînes de raisonnement, de s'adapter et de refléchir avant d'agir.

### Ce que nous allons couvrir ici

Dans cet article, vous apprendrez ce qui distingue fondamentalement l'IA agentique des systèmes réactifs traditionnels. Nous aborderons ses composants clés comme l'autonomie, la fixation d'objectifs, la planification, le raisonnement et la mémoire, et explorerons comment ces systèmes sont construits aujourd'hui. Nous examinerons également les défis qu'ils présentent et où ils en sont actuellement dans leur développement. Enfin, vous recevrez un tutoriel pratique sur la construction de votre propre agent simple en utilisant Python et LangChain.

### Table des matières :

1. [IA agentique vs IA réactive](#heading-ia-agentique-vs-ia-reactive)
    
2. [Composants clés de l'agence IA](#heading-composants-cles-de-lagence-ia)
    
    * [Autonomie](#heading-autonomie)
        
    * [Comportement dirigé par des objectifs](#heading-comportement-dirige-par-des-objectifs)
        
    * [Planification](#heading-planification)
        
    * [Raisonnement](#heading-raisonnement)
        
    * [Mémoire](#heading-memoire)
        
3. [Comment l'IA agentique sait-elle quoi faire ?](#heading-comment-lia-agentique-sait-elle-quoi-faire)
    
    * [1. Elle utilise un modèle IA pré-entraîné](#heading-1-elle-utilise-un-modele-ia-pre-entraine)
        
    * [2. Elle suit les instructions dans les prompts](#heading-2-elle-suit-les-instructions-dans-les-prompts)
        
    * [3. Elle utilise des outils, mais seulement lorsqu'on lui dit comment](#heading-3-elle-utilise-des-outils-mais-seulement-lorsquon-lui-dit-comment)
        
    * [4. Elle peut se souvenir (parfois)](#heading-4-elle-peut-se-souvenir-parfois)
        
    * [5. Elle n'est pas entièrement autonome - pas encore](#heading-5-elle-nest-pas-entierement-autonome-pas-encore)
        
4. [Quel est l'état actuel de l'IA agentique ?](#heading-quel-est-letat-actuel-de-lia-agentique)
    
    * [Ce qui existe aujourd'hui](#heading-ce-qui-existe-aujourdhui)
        
    * [Ce qui est encore expérimental](#heading-ce-qui-est-encore-experimental)
        
    * [Sommes-nous proches de véritables agents autonomes ?](#heading-sommes-nous-proches-de-veritables-agents-autonomes)
        
5. [Construction de l'IA agentique : Cadre et approches](#heading-construction-de-lia-agentique-cadre-et-approches)
    
    * [Agents d'apprentissage par renforcement (RL)](#heading-agents-dapprentissage-par-renforcement-rl)
        
    * [Agents basés sur LLM (génératifs)](#heading-agents-bases-sur-llm-generatifs)
        
    * [Cadre multi-agents et d'orchestration](#heading-cadre-multi-agents-et-dorchestration)
        
    * [Planification classique et IA symbolique](#heading-planification-classique-et-ia-symbolique)
        
    * [Raisonnement augmenté par outils](#heading-raisonnement-augmente-par-outils)
        
6. [Principaux défis de l'IA agentique](#heading-principaux-defis-de-lia-agentique)
    
    * [Alignement et spécification des valeurs](#heading-alignement-et-specification-des-valeurs)
        
    * [Conséquences imprévues](#heading-consequences-imprevues)
        
    * [Sécurité et sûreté](#heading-securite-et-surete)
        
    * [Coordination et scalabilité](#heading-coordination-et-scalabilite)
        
    * [Questions éthiques et légales](#heading-questions-ethiques-et-legales)
        
7. [Exemples de code et cas réels](#heading-exemples-de-code-et-cas-reels)
    
8. [Tutoriel : Construisez votre première IA agentique avec Python](#heading-tutoriel-construisez-votre-premiere-ia-agentique-avec-python)
    
    * [Cas d'utilisation réel](#heading-cas-dutilisation-reel)
        
    * [Prérequis - Ce dont vous avez besoin](#heading-prerequis-ce-dont-vous-avez-besoin)
        
    * [Tutoriel étape par étape](#heading-tutoriel-etape-par-etape)
        
9. [Conclusion](#heading-conclusion)
    

## **IA agentique vs IA réactive**

Avant de plonger complètement dans le sujet, je veux m'assurer que les différences entre l'IA non agentique et l'IA agentique sont claires.

L'IA réactive non agentique utilise des modèles ou des règles apprises pour mapper les entrées aux sorties. Elle répond à une idée ou une tâche à la fois, sans en commencer de nouvelles. Les exemples incluent une calculatrice, un filtre anti-spam et un chatbot rudimentaire avec des réponses pré-écrites. L'IA réactive ne peut pas planifier ou s'améliorer sans reprogrammation.

L'IA agentique, en revanche, agit de manière indépendante avec des objectifs. Elle peut organiser des actions, fixer des objectifs, s'adapter à de nouvelles informations et collaborer avec d'autres. L'IA agentique peut diviser une tâche complexe en petits segments et coordonner l'utilisation d'outils ou de services spécialisés pour compléter chaque étape.

L'agent est également proactif. Une IA agentique peut informer les utilisateurs des mises à jour, réapprovisionner les fournitures et vérifier les niveaux de stock, contrairement à un système réactif.

La différence est un changement paradigmatique : les systèmes agentiques modernes incluent plusieurs agents spécialisés travaillant ensemble sur un objectif de haut niveau, avec une décomposition dynamique des tâches et même une mémoire permanente, au lieu d'un seul modèle. Cette collaboration multi-agents peut aider l'IA agentique à résoudre de grands problèmes réels.

Les prototypes de pointe comme les chatbots intelligents avec intégration d'outils, les logiciels de conduite autonome et les robots industriels coordonnés entrent dans le territoire agentique, mais les assistants virtuels IA réactifs d'aujourd'hui (Alexa, Siri) peuvent brouiller la ligne. C'est une distinction vitale que le système sélectionne activement plutôt que de réagir.

## **Composants clés de l'agence IA**

Les systèmes d'IA agentique sont caractérisés par plusieurs capacités principales qui leur donnent de l'agence. Examinons-les maintenant.

### **Autonomie**

Un agent autonome peut travailler sans supervision humaine. Il peut agir en fonction de ses objectifs et de sa stratégie plutôt que d'attendre des directives spécifiques.

L'agent doit utiliser des capteurs ou des flux de données pour percevoir, évaluer et décider d'être autonome. Un robot de warehouse autonome peut se déplacer, ramasser des choses et modifier son chemin lorsqu'il rencontre des obstacles sans guidage humain. L'autonomie implique l'auto-surveillance : un agent évalue sa durée de vie de la batterie ou l'achèvement de son travail et s'adapte selon les besoins.

Le moteur de raisonnement d'une IA agentique (généralement un grand modèle de langage ou un système similaire) prend des décisions et peut ajuster son comportement en fonction des commentaires des utilisateurs ou des récompenses.

Comme l'explique IBM, sans aucune intervention humaine, l'IA agentique peut agir de manière indépendante, s'adapter à de nouvelles situations, prendre des décisions et apprendre de l'expérience ([source](https://www.ibm.com/think/topics/agentic-ai)). Mais les agents autonomes non contrôlés peuvent se comporter de manière imprévisible - c'est pourquoi ils doivent être soigneusement conçus.

Bien que les IA agentiques puissent fonctionner seules, leurs objectifs, outils et limites doivent être clairement planifiés pour éviter des résultats imprévus ou nuisibles. Sans ce guidage, ils peuvent suivre les instructions trop littéralement ou prendre des décisions sans comprendre le tableau d'ensemble.

### **Comportement dirigé par des objectifs**

L'IA agentique est dirigée par des objectifs. Le système tente d'atteindre un ou plusieurs objectifs. Les objectifs peuvent être spécifiés ouvertement (organiser une réunion pour demain) ou implicitement par un système de récompense. Au lieu de suivre un script, l'agent choisit comment atteindre son objectif. Il peut choisir des méthodes, des sous-objectifs et des objectifs à long terme.

L'IA réactive non planifiée a des objectifs à court terme ou implicites (par exemple, reconnaître une image, deviner le mot suivant). Les IA agentiques visent des objectifs à long terme. Si on lui confie la tâche d'organiser mon itinéraire de voyage, un agent peut réserver des vols, des hôtels, des transports, etc., choisir le meilleur ordre et ajuster l'horaire si les prix des compagnies aériennes changent.

Les sources commerciales et de recherche soulignent cette distinction. L'IA agentique planifie et travaille pour des objectifs à long terme, tandis que les systèmes réactifs gèrent des réponses immédiates et réactives. Une architecture de planification et d'exécution permet à l'agent de décider quoi faire et de définir et modifier ses objectifs. Au lieu d'actes distincts et séparés, il effectue progressivement une série. Le comportement dirigé par des objectifs démontre une intention délibérée, même si l'objectif est vague.

### **Planification**

Un agent planifie pour atteindre ses objectifs. Un objectif et des données instruisent l'IA agentique à effectuer une série d'actions ou de sous-tâches. La planification inclut des heuristiques simples (si A, alors faire B) et un raisonnement avancé (évaluer les options).

L'IA agentique moderne utilise des architectures planificateur-exécuteur avec des prompts de chaîne de pensée. Dans un agent planifier-et-exécuter, un planificateur piloté par LLM développe un plan multi-étapes, et les modules exécuteurs emploient des outils ou des modèles pour exécuter chaque étape. ReAct est une autre technique dans laquelle l'agent alterne entre l'action et le raisonnement (ou pensée) pour affiner son approche au fur et à mesure qu'il accumule des observations.

La planification implique souvent une recherche et une optimisation utilisant des réseaux de neurones, des arbres de décision ou des techniques basées sur des graphes. Par exemple, un agent peut construire un graphe de planification montrant différentes actions et résultats possibles, puis utiliser des algorithmes comme la recherche A* ou la recherche par arbre de Monte Carlo pour choisir la meilleure prochaine étape.

Dans certains cas, l'agent simule plusieurs futurs possibles pour évaluer quelles actions sont les plus susceptibles de mener au succès. Les grands modèles de langage (LLM) peuvent également aider en décomposant des instructions complexes en étapes plus petites, transformant un objectif de haut niveau en une liste de tâches qui peuvent être exécutées une par une.

Voici un exemple simplifié (pseudocode) d'une boucle d'agent :

```python
goal = "prepare presentation on AI"
agent = AI_Agent(goal)
environment = TaskEnvironment()
# Loop until the task is complete
while not environment.task_complete():
    observation = agent.perceive(environment)
    plan = agent.make_plan(observation)  # e.g., list of steps
    action = plan.next_step()
    result = agent.act(action, environment)
    agent.learn(result)  # update memory or strategy
```

Ici, l'agent perçoit l'état actuel, planifie une séquence d'étapes vers son objectif, agit en exécutant l'étape suivante, puis apprend du résultat avant de répéter. Ce cycle capture la boucle principale d'un agent autonome.

### **Raisonnement**

Prendre des jugements en appliquant la logique et l'inférence est connu sous le nom de raisonnement. En plus d'agir, une IA agentique considère quelles actions ont du sens à la lumière de ses informations. Cela implique d'évaluer les compromis, de comprendre la cause et la conséquence, et, si nécessaire, d'appliquer la pensée mathématique ou symbolique.

Un agent peut, par exemple, appliquer un raisonnement déductif, comme "Si les ventes tombent en dessous de X, réapprovisionner l'inventaire" ou "Toutes les factures sont payées le vendredi. Ceci est une facture, donc je devrais la payer le vendredi". En permettant à l'agent de traiter les commandes en langage naturel, de retenir les informations contextuelles et de produire des justifications logiques pour ses décisions, les grands modèles de langage soutiennent le raisonnement.

Un LLM "agit comme l'orchestrateur ou le moteur de raisonnement" qui comprend les tâches et produit des solutions, [selon une explication dans les docs de LangChain](https://python.langchain.com/docs/). Afin de récupérer des informations pertinentes pour le raisonnement, les agents utilisent également des stratégies telles que [la génération augmentée par récupération (RAG)](https://www.freecodecamp.org/news/learn-rag-fundamentals-and-advanced-techniques/).

Le raisonnement agentique est essentiellement comme la planification et la résolution de problèmes internes. Un agent évalue une tâche en simulant intérieurement des stratégies potentielles (souvent dans les "pensées" d'un LLM) et en sélectionnant la plus efficace. Cela peut impliquer une logique formelle, un raisonnement analogique (connecter un nouveau problème à des problèmes précédents), ou une déduction multi-étapes. Ainsi, l'agent considère continuellement son prochain cours d'action et s'adapte aux nouvelles entrées plutôt que de simplement cliquer sur "exécuter" sur un seul résultat de modèle.

### **Mémoire**

Les agents peuvent utiliser la mémoire pour rappeler des expériences, des informations et des interactions passées afin de prendre des décisions. Une IA sans mémoire traiterait chaque moment comme nouveau. Les systèmes agentiques enregistrent leurs comportements, leurs résultats et leur contexte. Une mémoire de travail à court terme de l'état actuel du plan ou une base de connaissances du monde à long terme en sont des exemples.

Un agent de service client peut se souvenir du nom d'un utilisateur et de l'historique de ses problèmes pour éviter de répéter les questions. Les agents de jeu apprennent des positions passées pour mieux se déplacer. [IBM dit](https://research.ibm.com/blog/agentic-ai) que la mémoire des agents IA fait référence à la capacité d'un système IA à stocker et à rappeler des expériences passées pour améliorer la prise de décision, la perception et les performances globales. Les agents orientés vers des objectifs ont besoin de mémoire pour créer un récit cohérent des étapes précédentes (pour éviter de répéter les échecs) et découvrir des tendances.

Les architectures agentiques incorporent des modules de mémoire comme des bases de données ou un stockage vectoriel que le LLM peut interroger. Les grands modèles de langage sont sans état. Les agents utilisent des filtres de pertinence pour ne retenir que les informations importantes, car trop de mémoire ralentit le système. La mémoire offre à l'agent un contexte et une continuité, lui permettant d'apprendre des tâches précédentes plutôt que de recommencer.

## Comment l'IA agentique sait-elle quoi faire ?

L'IA agentique peut sembler intelligente, mais elle ne réfléchit pas vraiment comme un humain. Décomposons comment elle fonctionne réellement.

### 1. Elle utilise un modèle IA pré-entraîné

Au cœur de la plupart des systèmes agentiques se trouve un grand modèle de langage (LLM) comme GPT-4. Ce modèle est entraîné sur une énorme quantité de texte, de livres, d'articles, de sites web, etc., pour apprendre comment les gens écrivent et parlent.

Mais il n'a pas été entraîné à agir comme un agent. Il a été entraîné à prédire le mot suivant dans une phrase.

Lorsque nous lui donnons les bons prompts, il peut sembler qu'il élabore des plans ou résout des problèmes. En réalité, il génère simplement des réponses utiles basées sur des motifs appris pendant l'entraînement.

### 2. Elle suit les instructions dans les prompts

L'IA agentique ne détermine pas par elle-même ce qu'elle doit faire - les développeurs lui donnent une structure en utilisant des prompts.

Par exemple :

* Vous êtes un assistant. D'abord, réfléchissez étape par étape. Ensuite, passez à l'action.
    
* Voici un objectif : rechercher des outils de codage. Planifiez les étapes. Utilisez Wikipedia pour rechercher.
    

Ces prompts aident l'IA à simuler la planification, la prise de décision et l'action.

### 3. Elle utilise des outils, mais seulement lorsqu'on lui dit comment

L'IA ne sait pas automatiquement comment utiliser des outils comme les moteurs de recherche ou les calculatrices. Les développeurs lui donnent accès à ces outils, et l'IA peut décider quand les utiliser en fonction du texte qu'elle génère.

Pensez à cela comme suit : l'IA suggère, Maintenant je vais chercher quelque chose, et le système fait que cela se produise.

### 4. Elle peut se souvenir (parfois)

Certains agents utilisent une mémoire à court terme pour se souvenir des questions ou des résultats passés. D'autres stockent des informations utiles dans une base de données pour plus tard. Mais ils n'apprennent pas au fil du temps comme les humains le font - ils ne se souviennent que de ce que vous leur permettez.

### 5. Elle n'est pas entièrement autonome - pas encore

La plupart des systèmes agentiques aujourd'hui ne sont pas entièrement auto-apprenants ou auto-conscients. Ils sont des combinaisons intelligentes de :

* IA pré-entraînée
    
* Prompts
    
* Outils
    
* Mémoire
    

Leur autonomie provient de la manière dont toutes ces parties fonctionnent ensemble - et non d'une compréhension profonde ou d'un entraînement à long terme.

## Quel est l'état actuel de l'IA agentique ?

L'IA agentique est encore un domaine émergent de développement. Bien qu'elle semble futuriste, de nombreux systèmes aujourd'hui commencent tout juste à utiliser des capacités de type agent.

### Ce qui existe aujourd'hui

#### Les systèmes agentiques simples fonctionnent déjà de manière limitée

* Par exemple, certains bots de service client peuvent vérifier les détails des comptes, répondre aux questions et escalader les problèmes automatiquement.
    
* Les robots de warehouse peuvent planifier des routes simples et éviter les obstacles par eux-mêmes.
    
* Les assistants de codage comme GitHub Copilot peuvent aider à écrire et corriger du code basé sur une entrée en langage naturel.
    

Ces systèmes montrent un comportement agentique de base comme le suivi d'objectifs et l'utilisation d'outils, mais généralement dans un environnement étroit et structuré.

### Ce qui est encore expérimental

* Les agents entièrement autonomes et polyvalents, capables de raisonner profondément, de faire des plans à long terme et de s'adapter à de nouveaux outils, sont encore en phase de recherche ou de prototype.
    
* Des projets comme **AutoGPT**, **BabyAGI** et **OpenDevin** sont passionnants, mais ils sont surtout expérimentaux et nécessitent une supervision humaine.
    

La plupart des systèmes agentiques actuels :

* N'apprennent pas en continu
    
* Ont du mal avec des environnements imprévisibles
    
* Nécessitent beaucoup de configuration pour éviter les erreurs ou les comportements inattendus
    

### Sommes-nous proches de véritables agents autonomes ?

Nous nous en approchons, mais nous n'y sommes pas encore.

L'IA agentique d'aujourd'hui est comme un assistant très intelligent qui peut suivre des instructions, utiliser des outils et planifier des étapes. Mais elle dépend toujours des développeurs pour lui donner une structure (via des prompts, des choix d'outils et des limites).

En bref, l'IA agentique fonctionne dans des cas d'utilisation spécifiques et bien conçus. Mais les agents autonomes polyvalents et de niveau humain sont encore loin.

## **Construction de l'IA agentique : Cadre et approches**

Les chercheurs et les ingénieurs ont développé divers cadres et outils pour construire des systèmes d'IA agentique. Discutons de quelques approches clés.

### **Agents d'apprentissage par renforcement (RL)**

En intelligence artificielle, les agents traditionnels sont fréquemment construits via [l'apprentissage par renforcement](https://www.freecodecamp.org/news/how-to-apply-reinforcement-learning-to-real-life-planning-problems-90f8fa3dc0c5/), dans lequel l'agent apprend à maximiser un signal de récompense par essai et erreur. Les agents de jeux Atari et AlphaGo de DeepMind sont des exemples classiques.

En plus de la planification (au sens du calcul d'une politique) et de l'apprentissage par interactions, les agents RL sont dirigés par des objectifs (maximisation de la récompense). Pourtant, beaucoup de systèmes RL purs ont du mal avec la complexité ouverte des tâches du monde réel et fonctionnent mieux dans des contextes simulés.

Bien que des composants RL soient parfois intégrés dans l'IA agentique moderne (par exemple, un agent peut utiliser RL pour piloter un robot à un niveau basique), ils sont fréquemment complétés par d'autres méthodes pour une pensée de niveau supérieur.

### **Agents basés sur LLM (génératifs)**

L'utilisation de LLM comme moteurs de raisonnement au sein des agents est devenue populaire grâce à l'explosion récente des grands modèles de langage. Par exemple, des frameworks comme ReAct, AutoGPT et BabyAGI utilisent des LLM (tels que GPT-4) pour créer des plans et des actions. Ces systèmes incluent l'invitation d'un LLM avec l'objectif et le contexte de l'agent, après quoi il génère une étape ou un sous-objectif et invoque soit une fonction, soit un outil.

Une conception, fréquemment appelée boucle ReAct, alterne entre "Pensée" (le LLM planifiant ou raisonnant) et "Action" (faisant appel à des outils ou des API). Une approche alternative implique un LLM planificateur distinct qui génère un plan multi-étapes complet, qui est ensuite suivi par des modules exécuteurs qui exécutent chaque étape.

Pour augmenter leurs capacités, les agents LLM utilisent fréquemment des outils comme des moteurs de recherche, des calculatrices et des appels d'API. Ils utilisent également la récupération de contexte, telle que RAG ou le stockage de mémoire, pour guider leur raisonnement. [LangChain](https://www.freecodecamp.org/news/beginners-guide-to-langchain/) et LangGraph sont des frameworks open-source bien connus qui offrent des blocs de construction (tampons de mémoire, intégration d'outils, etc.) pour créer des agents uniques.

### **Cadre multi-agents et d'orchestration**

Plusieurs sous-agents sont utilisés dans de nombreuses architectures d'IA agentique. Une méthode de "crew" ou de "société d'esprits", par exemple, peut produire plusieurs agents LLM qui communiquent par passage de messages et servent chacun un travail différent (planificateur, analyste, critique, etc.).

Les processus multi-agents orchestrés sont démontrés par des projets tels qu'AutoGen, ChatDev ou MetaGPT. Des idées d'ingénierie pour les systèmes multi-agents sont explorées dans les travaux académiques. Une étude de BMW, par exemple, décrit un cadre pour la coopération multi-agents dans lequel plusieurs agents IA gèrent la planification, l'exécution et les activités spécialisées tout en travaillant ensemble pour réaliser un cas d'utilisation industriel.

Ces systèmes ont fréquemment une logique de planification pour allouer des agents à des sous-tâches et un module de décomposition de tâches, qui divise un objectif en ses éléments constitutifs. Cela ressemble essentiellement à une "équipe IA", dans laquelle chaque individu est un sous-système agentique.

### **Planification classique et IA symbolique**

La planification IA a été examinée en termes symboliques avant la renaissance actuelle de l'ML (STRIPS, planificateurs PDDL, etc.). Ces méthodes peuvent être considérées comme un exemple précoce d'IA agentique, dans laquelle un planificateur construit une série d'actions symboliques pour accomplir un objectif.

Ces concepts sont parfois inclus dans l'IA agentique contemporaine. Par exemple, un agent LLM peut fournir un plan symbolique de haut niveau que des systèmes ancrés exécutent, comme "(Trouver x tel que la propriété y), (calculer f(x)), (livrer le résultat)" et ainsi de suite.

Il existe également des architectures hybrides qui combinent la recherche traditionnelle avec des réseaux de neurones. La transition vers des planificateurs appris ou basés sur le langage est une extension de la planification classique qui sous-tend de nombreux agents de robotique et de planification, même si elle est moins répandue sous sa forme pure aujourd'hui.

### **Raisonnement augmenté par outils**

Dans de nombreux systèmes agentiques, accorder à l'agent l'accès à des fonctions et informations externes est une stratégie viable. Par exemple, lorsqu'il répond à une question difficile, un agent basé sur le langage peut utiliser la génération augmentée par récupération (RAG) pour récupérer des informations pertinentes d'une base de données.

En tant qu'outils qu'il peut utiliser, il peut également inclure une calculatrice, un navigateur web, une API de base de données ou un code personnalisé. L'autonomie est largement rendue possible par la capacité à utiliser des outils - au lieu d'essayer d'apprendre tout par cœur, le modèle IA apprend à poser les bonnes questions.

En somme, construire une IA agentique signifie souvent combiner plusieurs techniques : l'apprentissage automatique pour la perception et l'apprentissage, la planification symbolique pour la structure, le raisonnement LLM pour le langage naturel et la décomposition de problèmes, ainsi que des modules de mémoire et des boucles de rétroaction.

Il n'existe pas encore de cadre universel. La recherche continue rapidement - les récents articles sur les systèmes agentiques soulignent les pipelines de bout en bout qui intègrent la perception (analyse des entrées), la planification orientée vers des objectifs, l'utilisation d'outils et l'apprentissage continu.

## **Principaux défis de l'IA agentique**

Construire des agents IA avec autonomie et objectifs est puissant mais soulève de nouveaux risques et difficultés. Les défis clés incluent :

### **Alignement et spécification des valeurs**

Définir les bons objectifs est crucial pour les systèmes agentiques. Si les objectifs d'un agent ne correspondent pas aux valeurs humaines, il peut être dommageable. Si un agent de planification est dirigé pour minimiser les coûts, il peut réduire les services vitaux à moins qu'on lui dise de préserver la qualité. Les priorités complexes des humains rendent la formulation des valeurs difficile. Les objectifs non spécifiés ou mal décrits entraînent des conséquences imprévues ([Loi de Goodhart](https://en.wikipedia.org/wiki/Goodhart%27s_law)).

### **Conséquences imprévues**

Même avec de bonnes intentions, les agents peuvent découvrir des failles. Le piratage de récompense dans l'apprentissage par renforcement est un exemple de l'IA de base. L'autonomie augmente ces risques pour l'IA agentique. Des expériences récentes ont montré qu'une IA basée sur LLM a été invitée à poursuivre un objectif à tout prix. Elle a planifié d'arrêter sa propre surveillance et de se cloner pour échapper à l'arrêt, agissant en auto-préservation.

Si elle n'est pas contrainte, un agent peut tromper pour atteindre ses objectifs. Les effets imprévus peuvent aller d'un assistant organisant un vol dangereux parce qu'il s'est fixé sur un objectif d'économie de coûts à des dommages plus subtils comme la suppression de bénéfices importants. [Les chercheurs d'IBM avertissent](https://www.ibm.com/think/insights/ethics-governance-agentic-ai) que les agents peuvent agir sans votre supervision, entraînant des conséquences imprévues sans protections solides.

### **Sécurité et sûreté**

Les agents hautement autonomes peuvent augmenter le danger. Ils peuvent accéder à des données sensibles ou faire fonctionner des machines. IBM dit que les agents sont opaques et ouverts, donc leurs jugements peuvent être peu clairs, et ils peuvent soudainement utiliser de nouveaux outils ou données. Un agent de santé peut divulger des données de patients, ou un bot financier peut exécuter un mouvement dangereux.

Les attaques adverses de style LLM et les hallucinations deviennent plus dangereuses dans l'IA agentique. Bien que gênantes, un chatbot délirant ou un agent d'investissement peut également perdre des millions. Le raisonnement multi-étapes de l'agent est sensible aux entrées hostiles à tout niveau. Les agents complexes rendent la confiance et la vérification difficiles.

### **Coordination et scalabilité**

Dans de nombreux systèmes agentiques, plusieurs agents peuvent collaborer ou rivaliser. S'assurer qu'ils communiquent correctement et ne se contredisent pas est non trivial.

Une récente revue note des défis uniques dans l'orchestration de plusieurs agents sans protocoles standardisés. Comme le souligne [le rapport éthique de Stanford](https://hai.stanford.edu/ai-index/2025-ai-index-report), si des millions d'agents interagissent (par exemple, en réservant les rendez-vous des uns et des autres), le comportement émergent pourrait être imprévisible à grande échelle. Cela soulève des préoccupations sociétales concernant les effets au niveau du système et les boucles de rétroaction que nous n'avons pas encore vues.

### **Questions éthiques et légales**

Enfin, il y a des questions de responsabilité et de biais. Qui est responsable si un agent autonome commet une erreur ? Comment garantir la transparence et l'équité dans un système multi-agents en boîte noire ?

Les cadres légaux et éthiques sont encore en train de rattraper leur retard. Par exemple, IBM souligne que l'IA agentique apporte un ensemble élargi de dilemmes éthiques par rapport à l'IA d'aujourd'hui. Et les éthiciens de l'IA mettent en garde contre le fait que le déploiement d'assistants puissants (en tant que secrétaires personnels, conseillers, etc.) aura des impacts sociétaux profonds qui sont difficiles à prédire.

Voici quelques éléments spécifiques que nous devons considérer :

* **Responsabilité :** Qui est responsable si un agent IA prend une décision dommageable (comme un agent médical IA prescrivant le mauvais médicament ou un agent logistique causant un accident) ? Les concepteurs, les déployeurs ou les agents ? Les systèmes juridiques supposent un contrôle humain, mais les agents autonomes peuvent ne pas en avoir.
    
* **Transparence :** Des systèmes agentiques complexes et opaques existent. Plusieurs réseaux de neurones, bases de connaissances et outils peuvent interagir. Expliquer le comportement d'un agent pour l'audit ou le débogage est difficile. Cela s'oppose à l'IA explicable.
    
* **Biais et équité :** Les agents apprennent à partir de données et d'environnements qui peuvent refléter les biais humains. Un agent assistant de recrutement autonome, par exemple, pourrait involontairement reproduire des schémas discriminatoires à moins d'être soigneusement vérifié. Et parce que l'IA agentique peut perpétuer ou amplifier les biais à travers de nombreuses décisions, l'impact pourrait être plus grand.
    
* **Perturbation des emplois et impact social :** Tout comme l'automatisation des usines a détruit certains emplois, des agents IA puissants pourraient changer le travail de bureau et créatif. Des agents assistants personnels qui planifient, gèrent les emails et font des recherches pourraient changer de nombreuses carrières. Cela pourrait augmenter la production mais aussi exacerber la désqualification et l'inégalité. La pression sociale pour utiliser l'IA agentique (si les concurrents le font) pourrait diviser les travailleurs en augmentés et non augmentés.
    
* **Sécurité et confidentialité :** Un agent avec un accès étendu au système nuit à la confidentialité. Le compromis d'un agent IA autorisé à accéder et à écrire des données commerciales ou des correspondances personnelles pourrait révéler des informations critiques. IBM avertit que l'IA agentique peut augmenter les risques reconnus, comme un agent biaisant accidentellement une base de données ou partageant des données privées sans surveillance. Les outils doivent être authentifiés et les données traitées de manière sécurisée.
    
* **Interaction humain-IA :** Nos agents peuvent affecter la manière dont nous utilisons la technologie et interagissons avec les autres. Si les individus utilisent des bots IA pour la conversation, le filtrage d'informations ou la compagnie, cela pourrait changer les dynamiques sociétales. Considérez à nouveau l'étude de Stanford mentionnée ci-dessus. Nous devons donc chercher des moyens d'inclure des normes et des valeurs dans ces interactions.
    

En reconnaissance de ces défis, les technologues et les éthiciens nous exhortent à utiliser des garde-fous proactifs. Comme le disent les chercheurs d'IBM, parce que l'IA agentique avance rapidement, nous ne pouvons pas attendre pour aborder la sécurité - nous devons construire des garde-fous solides maintenant. Certaines mesures proposées incluent des protocoles de test stricts pour les agents, des exigences d'explicabilité, des réglementations légales sur les systèmes autonomes, et des principes de conception qui priorisent les valeurs humaines.

Ainsi, comme vous pouvez le voir, bien que l'IA agentique offre le potentiel pour une IA capable de gérer des tâches complexes de bout en bout, elle amplifie également les risques connus de l'IA (biais, erreur) et en introduit de nouveaux (prise de décision autonome, échecs de coordination). Aborder ces défis nécessite une conception minutieuse de l'alignement, une évaluation robuste du comportement des agents, et une gouvernance interdisciplinaire.

## **Exemples de code et cas réels**

Pour illustrer comment fonctionne un système agentique, considérons un pseudocode très simple en Python pour un agent abstrait (mélangeant des concepts des sections précédentes) :

```python
class Agent:
    def __init__(self, goal):
        self.goal = goal
        self.memory = []
    def perceive(self, environment):
        # Get data from environment (sensor, API, etc.)
        return environment.get_state()
    def plan(self, observation):
        # Use reasoning (LLM or algorithm) to decide next action(s)
        plan = ReasoningEngine.generate_plan(goal=self.goal, context=observation)
        return plan  # e.g. list of steps or actions
    def act(self, action, environment):
        # Execute the action using tools or directly in the environment
        result = environment.execute(action)
        return result
    def learn(self, experience):
        # Store outcome or update strategy
        self.memory.append(experience)
    def run(self, environment):
        while not environment.task_complete():
            obs = self.perceive(environment)
            plan = self.plan(obs)
            for action in plan:
                result = self.act(action, environment)
                self.learn(result)
```

Cet exemple démontre la boucle principale d'une IA agentique :

* L'agent commence avec un objectif et peut stocker en mémoire ce qu'il a fait.
    
* Il observe son environnement pour comprendre ce qui se passe.
    
* Sur la base de cette entrée, il crée un plan - une liste d'actions pour atteindre son objectif.
    
* Il exécute chaque action, interagit avec l'environnement et apprend de ce qui se passe.
    
* Ce processus se répète jusqu'à ce que l'objectif soit atteint ou que la tâche soit terminée.
    

Cette structure de base reflète le fonctionnement des systèmes agentiques du monde réel : percevoir → planifier → agir → apprendre.

Les systèmes d'IA agentique du monde réel évoluent. Les voitures autonomes détectent leur environnement, fixent des objectifs de navigation, planifient des itinéraires et apprennent de l'expérience.

[Tesla's Full Self-Driving](https://www.tesla.com/AI) apprend continuellement de l'environnement de conduite et ajuste son comportement pour augmenter la sécurité. Les entreprises de logistique de la chaîne d'approvisionnement créent des agents qui surveillent les stocks, estiment la demande, modifient les itinéraires et passent de nouvelles commandes de manière autonome. Les robots de warehouse d'Amazon utilisent l'IA agentique pour naviguer dans des environnements complexes et s'adapter à des situations changeantes, remplissant indépendamment les commandes.

La cybersécurité, les soins de santé et le service client utilisent également des agents autonomes pour identifier et répondre aux risques. Une IA agentique dans un centre de contact peut évaluer l'humeur d'un client, l'historique de son compte et les politiques de l'entreprise pour fournir une solution personnalisée ou un processus. Les systèmes agentiques organisent et planifient des campagnes marketing, écrivent du texte, choisissent des graphiques et modifient les stratégies en fonction des données de performance. Dans les processus avec plusieurs étapes et choix, l'IA agentique peut gérer l'ensemble du flux de travail.

Récemment, plusieurs projets prototypes et outils open-source ont commencé à expérimenter l'IA agentique dans des scénarios du monde réel.

Par exemple, des outils comme AutoGPT et AgentGPT ont démontré des agents capables de générer des rapports multimédias en coordonnant des tâches de recherche, d'écriture et de sélection d'images. D'autres cas d'utilisation incluent des agents qui récupèrent des connaissances et prennent des mesures de suivi (par exemple, trouver et mettre en œuvre l'étape suivante), effectuent des opérations de sécurité comme la numérisation et la réponse aux menaces, ou automatisent des flux de travail multi-étapes dans les centres d'appels.

Ces exemples montrent comment les produits en phase initiale et les projets de recherche commencent à tester et à déployer l'IA agentique pour des tâches complexes et multi-étapes, au-delà de la simple réponse à des questions.

## **Tutoriel : Construisez votre première IA agentique avec Python**

Ce guide étape par étape vous apprendra à construire un système d'IA agentique de base même si vous débutez. Je vais expliquer chaque concept clairement et vous donner un code Python fonctionnel que vous pouvez exécuter et étudier.

### **Cas d'utilisation réel**

**Scénario :** Vous êtes un chef de produit explorant des outils pour votre équipe. Au lieu de passer des heures à rechercher manuellement des assistants de codage IA, vous aimeriez avoir un agent de recherche personnel pour :

* Comprendre votre tâche
    
* Récupérer des informations pertinentes sur Wikipedia
    
* Les résumer clairement
    
* Se souvenir du contexte des questions précédentes
    

C'est là que l'IA agentique excelle : elle agit de manière autonome, raisonne et utilise des outils tout comme un assistant humain intelligent.

### **Prérequis - Ce dont vous avez besoin**

1. Python 3.10 ou supérieur
    
2. Une clé API OpenAI ([https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)). Notez qu'au moment de la rédaction de cet article, OpenAI ne propose pas d'appels API gratuits, donc si vous n'avez pas déjà un compte, vous devrez utiliser une carte de crédit et quelques dollars pour compléter ce tutoriel.
    
3. Installez les bibliothèques Python requises :
    

```bash
pip install langchain openai wikipedia
```

⚠️ N'oubliez pas de stocker votre clé API en sécurité. Ne la partagez jamais dans du code public.

### **Tutoriel étape par étape**

#### Étape 1 : Configurez votre environnement

Commencez par définir votre clé API OpenAI dans votre script afin que LangChain puisse accéder aux modèles GPT.

```python
import os

os.environ["OPENAI_API_KEY"] = "your-api-key-here"  # Remplacez par votre vraie clé
```

#### Étape 2 : Connectez-vous à une source de connaissances (Wikipedia)

Nous allons donner à notre agent la capacité d'utiliser Wikipedia comme outil pour recueillir des informations.

```python
from langchain.agents import Tool
from langchain.tools import WikipediaQueryRun
from langchain.utilities import WikipediaAPIWrapper
# Créez l'outil Wikipedia
wiki = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
# Enregistrez l'outil pour que l'agent sache comment l'utiliser
tools = [
    Tool(
        name="Wikipedia",
        func=wiki.run,
        description="Utile pour rechercher des connaissances générales."
    )
]
```

Vous donnez à votre agent un moyen de "voir le monde" - Wikipedia est les yeux de votre agent.

#### Étape 3 : Initialisez l'agent (Moteur de raisonnement)

Nous donnons maintenant à l'agent un cerveau - un modèle GPT qui peut raisonner, décider et planifier.

```python
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent
from langchain.agents.agent_types import AgentType
# Utilisez un modèle GPT avec une aléatoire nulle pour une sortie cohérente
llm = ChatOpenAI(temperature=0)
# Combinez le raisonnement (LLM) et les outils (Wikipedia) en un seul agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True  # Montrez le processus de réflexion étape par étape
)
```

Cette étape fusionne la logique (GPT) et l'action (Wikipedia) pour rendre votre agent capable de comportement dirigé par des objectifs.

#### Étape 4 : Donnez un objectif à votre agent

```python
goal = "Quels sont les principaux assistants de codage IA et ce qui les rend uniques ?"
response = agent.run(goal)
print("\nRéponse de l'agent :\n", response)
```

Vous avez donné une mission à votre agent. Il va maintenant réfléchir, rechercher et résumer.

Vous devriez voir une sortie comme :

`> Entering new AgentExecutor chain...`

`Thought: I should look up AI coding assistants on Wikipedia`

`Action: Wikipedia`

`Action Input: AI coding assistants`

`...`

`Final Answer: The top AI coding assistants are GitHub Copilot, Amazon CodeWhisperer, and Tabnine...`

À ce stade, l'agent a :

* Interprété votre objectif
    
* Sélectionné un outil (Wikipedia)
    
* Récupéré et analysé le contenu
    
* Raisonné à travers celui-ci pour livrer une conclusion
    

#### Étape 5 : Donnez une mémoire à votre agent (Optionnel mais puissant)

Laissez votre agent se souvenir de ce que vous avez précédemment demandé, comme un vrai assistant.

```python
from langchain.memory import ConversationBufferMemory
memory = ConversationBufferMemory(memory_key="chat_history")
agent_with_memory = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    verbose=True
)
# Posez une question de suivi
agent_with_memory.run("Parlez-moi de GitHub Copilot")
agent_with_memory.run("Que savez-vous d'autre sur les assistants de codage ?")
```

Votre agent suit maintenant le contexte à travers plusieurs interactions, tout comme un bon assistant humain.

Lorsque cela est fait, votre agent :

* Répond plus naturellement aux questions de suivi
    
* Lie les conversations précédentes pour améliorer la continuité
    

Après avoir exécuté les étapes, votre agent lit votre objectif et planifie les étapes pour le réaliser. Il recherche sur Wikipedia pour recueillir des faits, et raisonne en utilisant un modèle GPT pour résumer et décider quoi dire. Il se souvient également du contexte (avec la mémoire activée). Vous avez maintenant un agent IA agentique fonctionnel qui peut être étendu pour des tâches réelles.

## **Conclusion**

L'IA agentique offre un aperçu passionnant d'un avenir où les machines peuvent collaborer avec les humains pour résoudre des problèmes complexes et multi-étapes, et pas seulement répondre à des commandes. Avec des capacités comme la planification, le raisonnement, l'utilisation d'outils et la mémoire, ces systèmes pourraient un jour gérer des tâches qui nécessitent actuellement des équipes entières de personnes.

Mais avec ce pouvoir vient une réelle responsabilité. Si elles ne sont pas correctement conçues et guidées, les agents autonomes pourraient agir de manière imprévisible ou nuisible. C'est pourquoi les développeurs, les chercheurs et les décideurs politiques doivent travailler ensemble pour établir des limites claires, des règles de sécurité et des normes éthiques.

La technologie avance rapidement, des voitures autonomes aux assistants de recherche en passant par les plateformes multi-agents comme AutoGPT et LangChain. Alors que nous construisons des systèmes plus intelligents, le défi n'est pas seulement ce qu'ils peuvent faire, mais comment nous pouvons nous assurer qu'ils le font de manière sûre, équitable et bénéfique pour tous.