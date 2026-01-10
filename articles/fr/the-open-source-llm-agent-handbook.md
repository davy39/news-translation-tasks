---
title: 'Le manuel de l''agent LLM open source : comment automatiser des tâches complexes
  avec LangGraph et CrewAI'
subtitle: ''
author: Balajee Asish Brahmandam
co_authors: []
series: null
date: '2025-06-03T14:20:30.237Z'
originalURL: https://freecodecamp.org/news/the-open-source-llm-agent-handbook
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1748956366197/c4dd2bba-430a-4f12-a3d4-becc6707c52e.png
tags:
- name: llm
  slug: llm
- name: openai
  slug: openai
- name: Open Source
  slug: opensource
- name: agentic AI
  slug: agentic-ai
- name: '#agent'
  slug: agent
- name: agents
  slug: agents
- name: ML
  slug: ml
- name: Bash
  slug: bash
- name: Beginner Developers
  slug: beginners
- name: Python
  slug: python
- name: AI
  slug: ai
seo_title: 'Le manuel de l''agent LLM open source : comment automatiser des tâches
  complexes avec LangGraph et CrewAI'
seo_desc: 'Ever feel like your AI tools are a bit...well, passive? Like they just
  sit there, waiting for your next command? Imagine if they could take initiative,
  break down big problems, and even work together to get things done.

  That''s exactly what LLM agents...'
---

Vous avez déjà l'impression que vos outils d'IA sont un peu... eh bien, passifs ? Comme s'ils restaient assis là, attendant votre prochaine commande ? Imaginez s'ils pouvaient prendre l'initiative, décomposer les gros problèmes et même travailler ensemble pour accomplir les choses.

C'est exactement ce que les agents LLM apportent sur la table. Ils changent la façon dont nous automatisons les tâches complexes et peuvent aider à concrétiser nos idées d'IA d'une toute nouvelle manière.

Dans cet article, nous explorerons ce que sont les agents LLM, comment ils fonctionnent et comment vous pouvez construire le vôtre en utilisant des frameworks open source incroyables.

### Ce que nous allons couvrir :

1. [L'état actuel des agents LLM](#heading-letat-actuel-des-agents-llm)
   
   * [Des chatbots aux agents autonomes](#heading-des-chatbots-aux-agents-autonomes)
       
   * [Que peuvent faire les agents aujourd'hui ?](#heading-que-peuvent-faire-les-agents-aujourdhui)
       
   * [Qu'est-ce qui est disponible pour construire ?](#heading-quest-ce-qui-est-disponible-pour-construire)
       
   * [Pourquoi maintenant est le meilleur moment pour apprendre](#heading-pourquoi-maintenant-est-le-meilleur-moment-pour-apprendre)
       
2. [Que sont les agents LLM et pourquoi sont-ils importants ?](#heading-que-sont-les-agents-llm-et-pourquoi-sont-ils-importants)
   
   * [Qu'est-ce qu'un LLM ?](#heading-quest-ce-quun-llm)
       
   * [Alors, qu'est-ce qu'un agent LLM ?](#heading-alors-quest-ce-quun-agent-llm)
       
   * [Pourquoi est-ce important ?](#heading-pourquoi-est-ce-important)
       
3. [L'essor des frameworks d'agents open source](#heading-lessor-des-frameworks-dagents-open-source)
   
   * [Frameworks d'agents open source populaires](#heading-frameworks-dagents-open-source-populaires)
       
   * [Ce que ces outils permettent](#heading-ce-que-ces-outils-permettent)
       
   * [Pourquoi utiliser un framework au lieu de construire à partir de zéro ?](#heading-pourquoi-utiliser-un-framework-au-lieu-de-construire-a-partir-de-zero)
       
4. [Concepts clés derrière la conception des agents](#heading-concepts-cles-derriere-la-conception-des-agents)
   
   * [La boucle de l'agent](#heading-la-boucle-de-lagent)
       
   * [Composants clés d'un agent](#heading-composants-cles-dun-agent)
       
   * [Collaboration multi-agents](#heading-collaboration-multi-agents)
       
5. [Projet : Automatisez votre emploi du temps quotidien à partir des emails](#heading-projet-automatisez-votre-emploi-du-temps-quotidien-a-partir-des-emails)
   
   * [Ce que nous automatisons](#heading-ce-que-nous-automatisons)
       
   * [Étape 1 : Installer les outils requis](#heading-etape-1-installer-les-outils-requis)
       
   * [Étape 2 : Définir la tâche](#heading-etape-2-definir-la-tache)
       
   * [Étape 3 : Construire le flux de travail avec LangGraph](#heading-etape-3-construire-le-flux-de-travail-avec-langgraph)
       
6. [Collaboration multi-agents avec CrewAI](#heading-collaboration-multi-agents-avec-crewai)
   
   * [Qu'est-ce que CrewAI ?](#heading-quest-ce-que-crewai)
       
   * [Rôles d'exemple pour la tâche de résumé d'email](#heading-roles-dexemple-pour-la-tache-de-resume-demail)
       
   * [Exemple de code CrewAI](#heading-exemple-de-code-crewai)
       
7. [Que se passe-t-il réellement pendant l'exécution ?](#heading-que-se-passe-t-il-reellement-pendant-lexecution)
   
8. [Les agents LLM sont-ils sûrs ? Ce qu'il faut savoir sur la sécurité et la confidentialité](#heading-les-agents-llm-sont-ils-surs-ce-quil-faut-savoir-sur-la-securite-et-la-confidentialite)
   
9. [Dépannage et conseils](#heading-depannage-et-conseils)
   
10. [Explorez plus d'automatisations quotidiennes](#heading-explorez-plus-dautomatisations-quotidiennes)
    
11. [Qu'est-ce qui est à venir dans la technologie des agents ?](#heading-quest-ce-qui-est-a-venir-dans-la-technologie-des-agents)
    
12. [Résumé final](#heading-resume-final)
    

## L'état actuel des agents LLM

Les agents LLM sont l'une des avancées les plus passionnantes dans le domaine de l'IA en ce moment. Ils aident déjà à automatiser des tâches réelles, mais ils évoluent encore. Alors, où en sommes-nous aujourd'hui ?

### Des chatbots aux agents autonomes

Les grands modèles de langage (LLM) comme GPT-4, Claude, Gemini et LLaMA ont évolué de simples chatbots en moteurs de raisonnement surprenamment capables. Ils sont passés de la réponse à des questions de trivia et de la génération de dissertations à l'exécution de raisonnements complexes, au suivi d'instructions en plusieurs étapes et à l'interaction avec des outils comme la recherche web et les interpréteurs de code.

Mais voici le hic : ces modèles sont **réactifs**. Ils attendent une entrée et donnent une sortie. Ils ne conservent pas la mémoire entre les tâches, ne planifient pas à l'avance ou ne poursuivent pas de buts par eux-mêmes. C'est là que les **agents LLM** interviennent - ils comblent cette lacune en ajoutant de la structure, de la mémoire et de l'autonomie.

### Que peuvent faire les agents aujourd'hui ?

Actuellement, les agents LLM sont déjà utilisés pour :

* Résumer des emails ou des documents
   
* Planifier des emplois du temps quotidiens
   
* Exécuter des scripts DevOps
   
* Rechercher des réponses dans des API ou des outils
   
* Collaborer en petites "équipes" pour accomplir des tâches complexes
   

Mais ils ne sont pas encore parfaits. Les agents peuvent encore :

* Rester bloqués dans des boucles
   
* Mal comprendre les objectifs
   
* Nécessiter des prompts détaillés et des garde-fous
   

C'est parce que cette technologie est encore à un stade précoce. Les frameworks s'améliorent rapidement, mais la fiabilité et la mémoire sont encore en cours de développement. Donc, gardez cela à l'esprit lorsque vous expérimentez.

### Pourquoi maintenant est le meilleur moment pour apprendre

La vérité est : nous en sommes encore aux débuts. Mais pas *trop* tôt.

C'est le moment parfait pour commencer à expérimenter avec les agents :

* Les outils sont suffisamment matures pour construire des projets réels
   
* La communauté grandit rapidement
   
* Et vous n'avez pas besoin d'être un expert en IA, il suffit d'être à l'aise avec Python
   

## Que sont les agents LLM et pourquoi sont-ils importants ?

Avant de plonger dans le monde passionnant des agents, parlons un peu plus des bases.

### Qu'est-ce qu'un LLM ?

Un LLM, ou grand modèle de langage, est essentiellement une IA qui a appris à partir d'une énorme quantité de texte provenant d'Internet - pensez aux livres, articles, code, et bien plus encore. Vous pouvez l'imaginer comme un moteur de complétion automatique super-intelligent. Mais il fait bien plus que simplement terminer vos phrases. Il peut aussi :

* Répondre à des questions délicates
   
* Résumer de longs articles ou documents
   
* Écrire du code, des emails ou des histoires créatives
   
* Traduire des langues instantanément
   
* Même résoudre des énigmes logiques et avoir des conversations engageantes
   

Vous avez probablement entendu parler de ChatGPT, qui est alimenté par les modèles GPT d'OpenAI. D'autres LLM populaires que vous pourriez rencontrer incluent Claude (d'Anthropic), LLaMA (de Meta), Mistral et Gemini (de Google).

Ces modèles fonctionnent simplement en prédisant le mot suivant dans une phrase en fonction du contexte. Bien que cela semble simple, lorsqu'ils sont entraînés sur des milliards de mots, les LLM deviennent capables de comportements surprenamment intelligents, comprenant vos instructions, suivant un raisonnement étape par étape et produisant des réponses cohérentes sur presque tous les sujets que vous pouvez imaginer.

### Alors, qu'est-ce qu'un agent LLM ?

Bien que les LLM soient super puissants, ils sont généralement juste *réactifs* - ils ne répondent que lorsque vous leur demandez quelque chose. Un agent LLM, en revanche, est *proactif*.

Les agents LLM peuvent :

* Décomposer de grandes tâches complexes en étapes plus petites et gérables
   
* Prendre des décisions intelligentes et déterminer quoi faire ensuite
   
* Utiliser des "outils" comme la recherche web, des calculatrices ou même d'autres applications
   
* Travailler vers un objectif, même si cela prend plusieurs étapes ou essais
   
* S'associer avec d'autres agents pour accomplir des objectifs partagés
   

En bref, les agents LLM peuvent penser, planifier, agir et s'adapter.

Imaginez un agent LLM comme votre nouvel assistant super-efficace : vous lui donnez un objectif, et il détermine comment l'atteindre tout seul.

### Pourquoi est-ce important ?

Ce passage de la simple réponse à la poursuite active d'objectifs ouvre un monde de possibilités passionnantes :

* Automatiser les tâches ennuyeuses d'IT ou de DevOps
   
* Générer des rapports détaillés à partir de données brutes
   
* Vous aider dans des projets de recherche en plusieurs étapes
   
* Lire vos emails quotidiens et mettre en évidence les informations clés
   
* Exécuter vos outils internes pour effectuer des actions réelles
   

Contrairement aux anciens bots basés sur des règles, les agents LLM peuvent raisonner, réfléchir et apprendre de leurs tentatives. Cela les rend beaucoup plus adaptés aux tâches réelles qui sont désordonnées, nécessitent de la flexibilité et dépendent de la compréhension du contexte.

## L'essor des frameworks d'agents open source

Il n'y a pas si longtemps, si vous vouliez construire un système d'IA capable d'agir de manière autonome, cela signifiait écrire une tonne de code personnalisé, gérer laborieusement la mémoire et essayer d'assembler des dizaines de composants. C'était un travail complexe, délicat et hautement spécialisé.

Mais devinez quoi ? Ce n'est plus le cas.

En 2024, une vague de frameworks open source fantastiques a fait son apparition. Ces outils ont rendu incroyablement plus facile la construction de puissants agents LLM sans que vous ayez à réinventer la roue à chaque fois.

### Frameworks d'agents open source populaires

| **Framework** | **Description** | **Mainteneur** |
| --- | --- | --- |
| LangGraph | Framework basé sur des graphes pour l'état et la mémoire des agents | LangChain |
| CrewAI | "Moteur de collaboration multi-agents basé sur les rôles" | Communauté (CrewAI) |
| AutoGen | Orchestration de chat multi-agents personnalisable | Microsoft |
| AgentVerse | Framework modulaire pour la simulation et le test d'agents | Projet open source |

### Ce que ces outils permettent

Ces frameworks vous fournissent des blocs de construction prêts à l'emploi pour gérer les parties les plus délicates de la création d'agents :

* **Planification** - Permettre aux agents de décider de leur prochain mouvement
   
* **Utilisation d'outils** - Connecter facilement les agents à des choses comme les systèmes de fichiers, les navigateurs web, les API ou les bases de données
   
* **Mémoire** - Stocker et récupérer des informations passées ou des résultats intermédiaires pour un contexte à long terme
   
* **Collaboration multi-agents** - Configurer des équipes d'agents qui travaillent ensemble sur des objectifs partagés
   

### Pourquoi utiliser un framework au lieu de construire à partir de zéro ?

Bien que vous *pourriez* construire un agent personnalisé à partir de zéro, utiliser un framework vous fera économiser une énorme quantité de temps et d'efforts. Les bibliothèques d'agents open source sont livrées avec :

* Un support intégré pour l'orchestration des LLM
   
* Des modèles éprouvés pour la planification des tâches, le suivi de l'avancement et l'obtention de feedback
   
* Une intégration facile avec des modèles populaires comme OpenAI, ou même des modèles que vous exécutez localement
   
* La flexibilité de passer d'un seul agent utile à des équipes entières d'agents
   

En gros, ces frameworks vous permettent de vous concentrer sur **ce que votre agent devrait faire**, plutôt que de vous perdre dans la construction de tous les mécanismes internes. De plus, choisir l'open source signifie que vous bénéficiez des contributions de la communauté, de la transparence dans leur fonctionnement et de la liberté de les ajuster à vos besoins exacts, sans être enfermé dans un seul fournisseur.

## Concepts clés derrière la conception des agents

Pour vraiment comprendre comment fonctionnent les agents LLM, il est utile de les considérer comme des systèmes orientés objectifs qui cyclent constamment à travers l'observation, le raisonnement et l'action. Cette boucle continue leur permet de s'attaquer à des tâches qui vont au-delà des simples questions et réponses, passant à une véritable automatisation, à l'utilisation d'outils et à l'adaptation à la volée.

### La boucle de l'agent

La plupart des agents LLM fonctionnent selon un modèle mental appelé **Boucle de l'agent** - un cycle étape par étape qui se répète jusqu'à ce que le travail soit terminé. Voici comment cela fonctionne généralement :

* **Percevoir** : L'agent commence par remarquer quelque chose dans son environnement ou en recevant de nouvelles informations. Cela pourrait être votre prompt, une donnée ou l'état actuel d'un système.
   
* **Planifier** : En fonction de ce qu'il perçoit et de son objectif global, l'agent décide quoi faire ensuite. Il pourrait décomposer la tâche en sous-objectifs plus petits ou déterminer le meilleur outil pour le travail.
   
* **Agir** : L'agent agit ensuite. Cela pourrait signifier exécuter une fonction, appeler une API, rechercher sur le web, interagir avec une base de données ou même demander de l'aide à un autre agent.
   
* **Réfléchir** : Après avoir agi, l'agent examine le résultat : Cela a-t-il fonctionné ? Le résultat était-il utile ? Devrait-il essayer une approche différente ? En fonction de cela, il met à jour son plan et continue jusqu'à ce que la tâche soit terminée.
   

Cette boucle est ce qui rend les agents si dynamiques. Elle leur permet de gérer des tâches en constante évolution, d'apprendre à partir de résultats partiels et de corriger leur trajectoire - des qualités vitales pour construire de véritables assistants IA utiles.

### Composants clés d'un agent

Pour faire leur travail efficacement, les agents sont construits autour de plusieurs parties cruciales :

* **Outils** sont la manière dont un agent interagit avec le monde réel (ou numérique). Ceux-ci peuvent être n'importe quoi, des moteurs de recherche, des environnements d'exécution de code, des lecteurs de fichiers ou des clients API, à des calculatrices simples ou des scripts en ligne de commande.
   
* **Mémoire** permet aux agents de se souvenir de ce qu'ils ont fait ou vu à travers différentes étapes. Cela pourrait inclure des choses que vous avez dites précédemment, des résultats temporaires ou des décisions clés. Certains frameworks offrent une mémoire à court terme (juste pour une session), tandis que d'autres supportent une mémoire à long terme qui peut couvrir plusieurs sessions ou objectifs.
   
* **Environnement** fait référence aux données externes ou au contexte du système dans lequel l'agent opère - pensez aux API, documents, bases de données, fichiers ou entrées de capteurs. Plus un agent a d'informations et d'accès à son environnement, plus les actions qu'il peut entreprendre sont significatives.
   
* **Objectif** est l'objectif ultime de l'agent : ce qu'il essaie d'accomplir. Les objectifs doivent être spécifiques et clairs - par exemple, "générer un emploi du temps quotidien", "résumer ce document" ou "extraire des tâches des emails".
   

### Collaboration multi-agents

Pour des systèmes plus avancés, vous pouvez même avoir plusieurs agents travaillant ensemble pour atteindre une cible partagée. Chaque agent peut se voir attribuer un **rôle** spécifique qui met en avant sa spécialité - tout comme des personnes travaillant en équipe.

Par exemple :

* Un **agent chercheur** pourrait être chargé de rassembler des informations.
   
* Un **agent codeur** pourrait écrire des scripts Python ou des routines d'automatisation.
   
* Un **agent réviseur** pourrait vérifier les résultats et s'assurer que tout est conforme.
   

Ces agents peuvent discuter entre eux, partager des informations et même débattre ou voter sur des décisions. Ce type de travail d'équipe permet aux systèmes d'IA de s'attaquer à des tâches plus grandes et plus complexes tout en gardant les choses organisées et modulaires.

## Projet : Automatisez votre emploi du temps quotidien à partir des emails

### Ce que nous automatisons

Pensez à votre routine matinale typique :

* Vous ouvrez votre boîte de réception.
   
* Vous parcourez rapidement une série d'emails.
   
* Vous essayez de repérer les réunions, les tâches et les rappels importants.
   
* Ensuite, vous écrivez manuellement une liste de choses à faire ou ajoutez des éléments à votre calendrier.
   

Utilisons un agent LLM pour rendre ce processus sans effort. Notre agent va :

* Lire une liste de vos messages électroniques
   
* Extraire les éléments sensibles au temps comme les réunions ou les délais
   
* Résumer le tout dans un bel emploi du temps quotidien propre
   

### Étape 1 : Installer les outils requis

Pour commencer, vous aurez besoin de trois outils principaux : Python, VSCode et une clé API OpenAI.

#### 1. Installer Python 3.9 ou supérieur

Téléchargez la dernière version de Python 3.9+ depuis le site officiel : [https://www.python.org/downloads/](https://www.python.org/downloads/)

Une fois installé, vérifiez-le en exécutant `python --version` dans votre terminal.

Cette commande demande simplement à votre système de signaler la version de Python actuellement installée. Vous devriez voir Python 3.9.x ou une version supérieure pour assurer la compatibilité avec notre projet.

#### 2. Installer VSCode (Optionnel mais recommandé)

VSCode est un éditeur de code fantastique et convivial qui fonctionne parfaitement avec Python. Vous pouvez le télécharger ici : [https://code.visualstudio.com/](https://code.visualstudio.com/).

#### 3. Obtenir votre clé API OpenAI

Rendez-vous sur : https://platform.openai.com

Connectez-vous ou créez un nouveau compte. Accédez à votre page des clés API. Cliquez sur "Créer une nouvelle clé secrète" et assurez-vous de copier cette clé quelque part en sécurité pour plus tard.

#### 4. Installer les bibliothèques Python

Ouvrez votre terminal ou invite de commande et installez ces packages essentiels :

```bash
pip install langgraph langchain openai
```

Cette commande utilise pip, le gestionnaire de packages de Python, pour télécharger et installer trois bibliothèques cruciales pour notre agent :

* langgraph : Le framework principal que nous utiliserons pour construire le flux de travail de notre agent.
   
* langchain : Une bibliothèque fondamentale pour travailler avec les grands modèles de langage, sur laquelle LangGraph est construit.
   
* openai : La bibliothèque Python officielle pour se connecter aux puissants modèles d'IA d'OpenAI.
   

Si vous êtes enthousiaste à l'idée d'essayer des configurations multi-agents (que nous couvrirons dans l'étape 5), installez également CrewAI :

```bash
pip install crewai
```

Cette commande installe CrewAI, un framework spécialisé qui facilite l'orchestration de plusieurs agents IA travaillant ensemble en équipe.

**5. Définir votre clé API OpenAI**

Vous devez vous assurer que votre code Python peut trouver et utiliser votre clé API OpenAI. Cela se fait généralement en la définissant comme une variable d'environnement.

Sur macOS/Linux, exécutez ceci dans votre terminal (remplacez "votre-clé-api" par votre clé réelle) :

```bash
export OPENAI_API_KEY="votre-clé-api"
```

Cette commande définit une variable d'environnement nommée OPENAI_API_KEY. Les variables d'environnement sont un moyen sécurisé pour les applications (comme votre script Python) d'accéder à des informations sensibles sans les coder directement dans le code lui-même.

Sur Windows (en utilisant l'invite de commande), faites ceci :

```bash
set OPENAI_API_KEY="votre-clé-api"
```

C'est la commande équivalente sous Windows pour définir la variable d'environnement `OPENAI_API_KEY`.

Maintenant, votre code Python sera prêt à communiquer avec le modèle OpenAI !

### Étape 2 : Définir la tâche

Nous en avons brièvement discuté au début de cette section. Mais pour réitérer, voici ce que nous voulons que notre agent fasse :

* Rechercher des réunions, des événements et des tâches importantes.
   
* Les noter rapidement dans un carnet ou une application.
   
* Créer un plan mental approximatif pour votre journée.
   

Cette routine prend du temps et de l'énergie mentale. Donc, avoir un agent qui le fait pour nous sera super utile.

### Étape 3 : Construire le flux de travail avec LangGraph

#### Qu'est-ce que LangGraph ?

LangGraph est un framework génial qui vous aide à construire des agents en utilisant un flux de travail "basé sur des graphes", un peu comme dessiner un organigramme. Il est alimenté par LangChain et vous donne beaucoup plus de contrôle sur l'ordre exact de chaque étape dans le processus de votre agent.

Chaque "nœud" dans ce graphe représente un point de décision ou une fonction qui :

* Prend une entrée (son "état" actuel).
   
* Effectue un raisonnement ou une action (souvent impliquant le LLM et ses outils).
   
* Retourne une sortie mise à jour (un nouvel "état").
   

Vous dessinez les connexions entre ces nœuds, et LangGraph l'exécute ensuite comme une machine à états intelligente et automatisée.

#### Pourquoi utiliser LangGraph ?

* Vous obtenez le contrôle de l'ordre précis d'exécution.
   
* C'est fantastique pour construire des flux de travail qui ont plusieurs étapes ou même se ramifient en différents chemins.
   
* Il fonctionne bien avec les modèles basés sur le cloud (comme OpenAI) et les modèles que vous exécutez localement.
   

D'accord - maintenant écrivons le code.

##### **1. Simuler l'entrée des emails**

Dans une application réelle, votre agent se connecterait probablement à Gmail ou Outlook pour récupérer vos vrais emails. Pour cet exemple, cependant, nous allons simplement coder en dur quelques messages d'exemple pour garder les choses simples :

```python
Python

emails = """
1. Sujet : Réunion debout à 10h
2. Sujet : Révision client à rendre avant 17h
3. Sujet : Déjeuner avec Sarah à midi
4. Sujet : Avertissement de budget AWS - 80% d'utilisation
5. Sujet : Rendez-vous chez le dentiste - 16h
"""
```

Cette chaîne de caractères Python multiline, `emails`, sert de substitut au contenu réel des emails. Nous fournissons une liste simple et structurée de sujets d'emails pour démontrer comment l'agent traitera le texte.

##### **2. Définir la logique de l'agent**

Maintenant, nous allons dire au modèle GPT d'OpenAI comment traiter ce texte d'email et le transformer en un résumé.

```python
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated, List
import operator

# Définir l'état pour notre graphe
class AgentState(TypedDict):



 emails: str



 result: str

llm = ChatOpenAI(temperature=0, model="gpt-4o") # Utilisation de gpt-4o pour de meilleures performances

def calendar_summary_agent(state: AgentState) -> AgentState:



 emails = state["emails"]



 prompt = f"Résumé de l'emploi du temps d'aujourd'hui basé sur ces emails, en listant d'abord les éléments sensibles au temps puis les autres notes importantes. Soyez concis et utilisez des puces :\n{emails}"



 summary = llm.invoke(prompt).content



 return {"result": summary, "emails": emails} # Assurez-vous que les emails sont également retournés
```

Voici ce qui se passe :

* **Imports** : Nous importons les composants nécessaires :
   
   * `ChatOpenAI` pour se connecter au LLM,
       
   * `StateGraph` et `END` de `langgraph.graph` pour construire notre flux de travail d'agent,
       
   * `TypedDict`, `Annotated`, et `List` de `typing` pour la vérification de type et la structure,
       
   * `operator` (bien que non utilisé dans cet extrait, il peut aider pour les comparaisons ou la logique).
       
* **AgentState** : Ce `TypedDict` définit la forme des données avec lesquelles notre agent travaillera. Il inclut :
   
   * `emails` : les messages d'entrée bruts.
       
   * `result` : la sortie finale (le résumé quotidien).
       
* **llm = ChatOpenAI(...) : Initialise le modèle de langage. Nous utilisons GPT-4o avec `temperature=0` pour garantir une sortie cohérente et prévisible - parfait pour les tâches de résumé structuré.
   
* **calendar_summary_agent(state: AgentState) : Cette fonction est le "cerveau" de notre agent. Elle :
   
   * Prend l'état actuel, qui inclut une liste d'emails.
       
   * Extrait les emails de cet état.
       
   * Construit un prompt qui indique au modèle de générer un résumé concis de l'emploi du temps quotidien en utilisant des puces, en priorisant les éléments sensibles au temps.
       
   * Envoie ce prompt au modèle avec `llm.invoke(prompt).content`, qui retourne la réponse du LLM sous forme de texte brut.
       
   * Retourne un nouveau dictionnaire `AgentState` contenant :
       
       * `result` : le résumé généré,
           
       * `emails` : préservé au cas où nous en aurions besoin en aval.
           

##### **3. Construire et exécuter le graphe**

Maintenant, utilisons LangGraph pour cartographier le flux de notre tâche à agent unique, puis exécutons-le.

```python
builder = StateGraph(AgentState)
builder.add_node("calendar", calendar_summary_agent)
builder.set_entry_point("calendar")
builder.set_finish_point("calendar") # END est implicite si non défini explicitement

graph = builder.compile()

# Exécuter le graphe en utilisant vos données d'email simulées
result = graph.invoke({"emails": emails})
print(result["result"])
```

Voici ce qui se passe :

* **builder = StateGraph(AgentState) :** Nous initialisons un objet StateGraph. En passant AgentState, nous indiquons à LangGraph la structure de données attendue pour son état interne.
   
* **builder.add_node("calendar", calendar_summary_agent) :** Cette ligne ajoute un "nœud" nommé à notre graphe. Nous l'appelons "calendar", et nous le lions à notre fonction `calendar_summary_agent`, ce qui signifie que cette fonction sera exécutée lorsque ce nœud est actif.
   
* **builder.set_entry_point("calendar") :** Cela définit "calendar" comme la toute première étape de notre flux de travail. Lorsque nous démarrons le graphe, l'exécution commence ici.
   
* **builder.set_finish_point("calendar") :** Cela indique à LangGraph que, une fois le nœud "calendar" terminé, l'ensemble du processus du graphe est complet.
   
* **graph = builder.compile() :** Cette commande prend notre plan de graphe défini et le "compile" en un flux de travail exécutable.
   
* **result = graph.invoke({"emails": emails}) :** C'est là que la magie opère ! Nous disons à notre graphe de commencer à s'exécuter. Nous lui passons un état initial qui contient nos données d'emails. Le graphe traitera ensuite ces données à travers ses nœuds jusqu'à ce qu'il atteigne un point de fin, retournant l'état final.
   
* **print(result["result"])** : Enfin, nous récupérons l'emploi du temps résumé à partir du résultat (l'état final de notre graphe) et l'affichons sur la console.
   

#### Exemple de sortie

`Votre emploi du temps :`  
`- 10:00 AM - Réunion debout`  
`- 12:00 PM - Déjeuner avec Sarah`  
`- 4:00 PM - Rendez-vous chez le dentiste`  
`- Soumettre le rapport client avant 17:00`  
`- Avertissement de budget AWS - vérifier l'utilisation`

Boum ! Vous venez de construire un agent IA qui peut lire vos emails et établir votre emploi du temps quotidien. Plutôt cool, non ? C'est un aperçu simple mais puissant de ce que les agents LLM peuvent faire avec seulement quelques lignes de code.

## Collaboration multi-agents avec CrewAI

### Qu'est-ce que CrewAI ?

CrewAI est un framework open source passionnant qui vous permet de construire des *équipes* d'agents qui travaillent ensemble de manière transparente, tout comme une équipe de projet dans le monde réel ! Chaque agent dans une configuration CrewAI :

* A un rôle spécifique et spécialisé.
   
* Peut communiquer et partager des informations avec ses coéquipiers.
   
* Collabore pour atteindre un objectif commun.
   

Cette approche multi-agents est super utile lorsque votre tâche est trop grande ou trop complexe pour un seul agent, ou lorsque la décomposer en parties spécialisées la rend plus claire et plus efficace.

### Rôles d'exemple pour la tâche de résumé d'email

Imaginons notre tâche de résumé d'email gérée par une petite équipe d'agents :

| **Nom de l'agent** | **Rôle** | **Responsabilité** |
| --- | --- | --- |
| Extracteur | Scanneur d'emails | "Trouver les réunions, rappels et tâches dans les emails" |
| Priorisateur | Optimiseur d'emploi du temps | Trier les éléments par urgence et heure |
| Formateur | Générateur de sortie | "Écrire un agenda quotidien propre et poli" |

### Exemple de code CrewAI

```python
from crewai import Agent, Crew, Task, Process
from langchain_openai import ChatOpenAI
import os

# Définir votre clé API OpenAI à partir des variables d'environnement
# os.environ["OPENAI_API_KEY"] = "VOTRE_CLE_API" # Assurez-vous que cela est défini, ou défini directement

# Initialiser le LLM (utilisation de gpt-4o pour de meilleures performances)
llm = ChatOpenAI(temperature=0, model="gpt-4o")

# Définir les agents avec des rôles et objectifs spécifiques
extractor = Agent(



 role="Scanneur d'emails",



 goal="Trouver toutes les réunions, rappels et tâches dans les emails donnés, en extrayant précisément les détails comme l'heure, la date et le sujet.",



 backstory="Vous êtes un expert dans l'analyse des emails pour en extraire les informations clés. Vous extrayez méticuleusement chaque détail pertinent.",



 verbose=True,



 allow_delegation=False,



 llm=llm
)

prioritizer = Agent(



 role="Optimiseur d'emploi du temps",



 goal="Trier les éléments extraits par urgence et heure, en les préparant pour un agenda quotidien.",



 backstory="Vous êtes un maître de la gestion du temps, sachant toujours ce qui doit être fait en premier. Vous organisez les tâches de manière logique.",



 verbose=True,



 allow_delegation=False,



 llm=llm
)

formatter = Agent(



 role="Générateur de sortie",



 goal="Générer un agenda quotidien propre, poli et concis au format à puces, listant clairement tous les éléments de l'emploi du temps.",



 backstory="Vous êtes une secrétaire professionnelle, garantissant que toutes les sorties sont parfaitement formatées et faciles à lire. Vous privilégiez la clarté.",



 verbose=True,



 allow_delegation=False,



 llm=llm
)

# Simuler l'entrée des emails
emails = """
1. Sujet : Réunion debout à 10h
2. Sujet : Révision client à rendre avant 17h
3. Sujet : Déjeuner avec Sarah à midi
4. Sujet : Avertissement de budget AWS - 80% d'utilisation
5. Sujet : Rendez-vous chez le dentiste - 16h
"""

# Définir les tâches pour chaque agent
extract_task = Task(



 description=f"Extraire tous les événements, réunions et tâches pertinents de ces emails : {emails}. Concentrez-vous sur les détails précis.",



 agent=extractor,



 expected_output="Une liste d'éléments extraits avec leurs détails (par exemple, '- Réunion debout à 10h', '- Révision client à rendre avant 17h')."
)

prioritize_task = Task(



 description="Prioriser les éléments extraits par heure et urgence. Les réunions d'abord, puis les délais, puis les autres notes.",



 agent=prioritizer,



 context=[extract_task], # La sortie de extract_task est l'entrée ici



 expected_output="Une liste priorisée d'éléments de l'emploi du temps."
)

format_task = Task(



 description="Formater l'emploi du temps priorisé en un agenda quotidien propre et facile à lire en utilisant des puces. Assurez-vous d'utiliser un langage concis.",



 agent=formatter,



 context=[prioritize_task], # La sortie de prioritize_task est l'entrée ici



 expected_output="Un agenda quotidien bien formaté avec des puces."
)

# Instancier l'équipe
crew = Crew(



 agents=[extractor, prioritizer, formatter],



 tasks=[extract_task, prioritize_task, format_task],



 process=Process.sequential, # Les tâches sont exécutées séquentiellement



 verbose=2 # Affiche plus de détails pendant l'exécution
)

# Exécuter l'équipe
result = crew.kickoff()
print("\n########################")
print("## Agenda Quotidien Final ##")
print("########################\n")
print(result)
```

Voici ce qui se passe :

* **Imports** : Nous importons les classes clés de CrewAI : Agent, Crew, Task et Process. Nous importons également `ChatOpenAI` pour notre modèle de langage et os pour gérer les variables d'environnement.
   
* **llm = ChatOpenAI(...) :** Tout comme dans l'exemple LangGraph, cela configure notre modèle de langage OpenAI, en s'assurant que ses réponses sont directes (temperature=0) et en utilisant le modèle gpt-4o.
   
* **Définitions des agents (extractor, prioritizer, formatter) :**
   
   * Chacune de ces variables crée une instance d'Agent. Un agent est défini par son rôle (ce qu'il fait), un objectif spécifique qu'il essaie d'atteindre et une histoire (une sorte de personnalité ou d'expertise qui aide le LLM à comprendre son but).
       
   * verbose=True est super utile pour le débogage, car il fait en sorte que les agents impriment leurs "pensées" pendant qu'ils travaillent.
       
   * allow_delegation=False signifie que ces agents ne passeront pas leurs tâches assignées à d'autres agents (bien que cela puisse être défini sur True pour des scénarios de délégation plus complexes).
       
   * llm=llm connecte chaque agent à notre modèle de langage OpenAI.
       
* **Emails simulés** : Nous réutilisons les mêmes données d'exemple d'emails pour cet exemple.
   
* **Définitions des tâches (extract_task, prioritize_task, format_task) :**
   
   * Chaque Task définit un morceau spécifique de travail qu'un agent doit effectuer.
       
   * description indique clairement à l'agent en quoi consiste la tâche.
       
   * agent attribue cette tâche à l'un de nos agents définis (par exemple, extractor pour extract_task).
       
   * context=[...] est une partie critique de la collaboration de CrewAI. Il indique à une tâche d'utiliser la *sortie* d'une tâche précédente comme son *entrée*. Par exemple, prioritize_task prend la sortie de extract_task comme son contexte.
       
   * expected_output donne à l'agent une idée de ce à quoi son résultat devrait ressembler, aidant à guider le LLM.
       
* **crew = Crew(...) :**
   
   * C'est là que nous assemblons notre équipe ! Nous créons une instance de Crew, en lui donnant notre liste d'agents et de tâches.
       
   * process=Process.sequential indique à l'équipe d'exécuter les tâches les unes après les autres dans l'ordre où elles sont définies dans la liste des tâches. CrewAI supporte également des processus plus avancés comme les hiérarchiques.
       
   * verbose=2 vous montrera un journal très détaillé du fonctionnement interne et de la communication de l'équipe.
       
* **result = crew.kickoff() :** Cette commande démarre officiellement l'ensemble du flux de travail multi-agents. Les agents commenceront à collaborer, à partager des informations et à travailler à travers leurs tâches assignées en séquence.
   
* **fprint(result) :** Enfin, la sortie consolidée de l'effort collaboratif de toute l'équipe est imprimée sur votre console.
   

CrewAI gère intelligemment toute la communication entre les agents, détermine qui doit travailler sur quoi et quand, et transmet la sortie en douceur d'un agent à l'autre - c'est comme avoir une mini chaîne de montage IA !

## Que se passe-t-il réellement pendant l'exécution ?

Alors, que vous utilisiez LangGraph ou CrewAI, que se passe-t-il réellement en coulisses lorsqu'un agent s'exécute ? Décomposons le processus d'exécution :

* Le système reçoit un **état d'entrée** (par exemple, vos emails).
   
* Le premier agent ou nœud de graphe lit cette entrée et utilise un **grand modèle de langage (LLM)** pour la comprendre.
   
* En fonction de sa compréhension, l'agent décide d'une **action** comme extraire des événements clés ou appeler un outil spécifique.
   
* Si nécessaire, l'agent peut **invoquer des outils** (comme une recherche web ou un lecteur de fichiers) pour obtenir plus de contexte ou effectuer des opérations externes.
   
* Le résultat de cette action est ensuite **transmis à l'agent suivant** dans l'équipe (si c'est une configuration multi-agents) ou retourné directement à vous.
   

L'exécution continue jusqu'à ce que :

* La tâche soit entièrement terminée.
   
* Tous les agents aient terminé leurs rôles assignés.
   
* Une condition d'arrêt ou un point "END" désigné dans le flux de travail soit atteint.
   

Pensez à cela comme un moteur de flux de travail super-intelligent où chaque étape implique du raisonnement, de la prise de décision et de la mémorisation des interactions précédentes.

## Les agents LLM sont-ils sûrs ? Ce qu'il faut savoir sur la sécurité et la confidentialité

Aussi géniaux que soient les agents LLM, ils soulèvent une question importante : *pouvez-vous vraiment faire confiance à une IA pour exécuter des parties de votre flux de travail ou interagir avec vos données ?* Cela dépend. Si vous utilisez des services comme OpenAI ou Anthropic, vos données sont chiffrées en transit et (pour l'instant) ne sont pas utilisées pour l'entraînement.

Mais certaines données pourraient encore être temporairement enregistrées pour prévenir les abus. C'est généralement acceptable pour les tests et les projets personnels, mais si vous travaillez avec des informations commerciales sensibles, des données clients ou tout ce qui est privé, vous devrez être prudent.

Utilisez des entrées anonymisées, évitez d'exposer des jeux de données complets et envisagez d'exécuter des agents localement en utilisant des modèles open source comme LLaMA ou Mistral si le contrôle total est important pour vous.

Vous pouvez également définir des limites claires pour vos agents afin qu'ils ne dépassent pas les bornes. Pensez à cela comme à l'intégration d'un nouveau stagiaire : vous ne lui donneriez pas accès à tout dès le premier jour.

Donnez aux agents uniquement les outils et fichiers dont ils ont besoin, conservez des logs de ce qu'ils font et revoyez toujours les résultats avant de les laisser apporter des modifications réelles.

À mesure que cette technologie se développe, de nouvelles fonctionnalités de sécurité arrivent, comme un meilleur bac à sable, des limites de mémoire et un accès basé sur les rôles. Mais pour l'instant, il est judicieux de traiter vos agents comme des assistants puissants qui nécessitent encore une certaine supervision humaine.

## Dépannage et conseils

Parfois, les agents peuvent être un peu capricieux ! Voici quelques problèmes courants que vous pourriez rencontrer et comment les résoudre :

| **Problème** | **Solution suggérée** |
| --- | --- |
| L'agent semble boucler indéfiniment | Définissez un nombre maximum d'itérations ou définissez un point d'arrêt plus clair. |
| La sortie est trop bavarde ou verbeuse | Utilisez des prompts plus spécifiques (par exemple, "Répondez uniquement avec des puces"). |
| L'entrée est trop longue ou est tronquée | Décomposez les grands morceaux de contenu en morceaux plus petits et résumez-les individuellement. |
| L'agent s'exécute trop lentement | Essayez d'utiliser un modèle LLM plus rapide comme gpt-3.5 ou envisagez d'exécuter un modèle local. |

Un conseil utile : Vous pouvez également ajouter des instructions print() ou des messages de journalisation à l'intérieur de vos fonctions d'agent pour voir ce qui se passe à chaque étape et déboguer les transitions d'état.

## Explorez plus d'automatisations quotidiennes

Une fois que vous avez construit une tâche basée sur des agents, vous trouverez incroyablement facile d'adapter le modèle pour d'autres automatisations. Voici quelques idées cool pour stimuler votre créativité :

| **Type de tâche** | **Exemple d'automatisation** |
| --- | --- |
| Assistant DevOps | "Lire les journaux système, détecter les problèmes potentiels et suggérer des solutions." |
| Suivi financier | Lire les relevés bancaires ou les fichiers CSV et résumer vos habitudes de dépenses/budgets. |
| Organisateur de réunions | Après une réunion, extraire automatiquement les points d'action et attribuer des propriétaires. |
| Nettoyeur de boîte de réception | "Étiqueter, archiver et supprimer automatiquement les emails non urgents." |
| Résumeur de notes | Convertir vos notes quotidiennes en une liste de tâches ou un résumé bien formaté. |
| Vérificateur de liens | Extraire les URL des documents et tester automatiquement s'ils sont toujours valides. |
| Formateur de CV | Noter les CV par rapport aux descriptions de poste et les formater automatiquement. |

Chacune de ces tâches peut être construite en utilisant les mêmes principes et frameworks dont nous avons discuté, qu'il s'agisse de LangGraph ou de CrewAI.

## Qu'est-ce qui est à venir dans la technologie des agents ?

Les agents LLM évoluent à une vitesse fulgurante, et la prochaine vague d'innovation est déjà là :

* **Systèmes de mémoire plus intelligents** : Attendez-vous à ce que les agents aient une meilleure mémoire à long terme, leur permettant d'apprendre sur des périodes prolongées et de se souvenir des conversations et actions passées.
   
* **Agents multimodaux** : Les agents ne géreront plus seulement le texte ! Ils pourront traiter et comprendre les images, l'audio et la vidéo, les rendant beaucoup plus polyvalents.
   
* **Frameworks de planification avancés** : Des techniques comme ReAct, Toolformer et AutoGen améliorent constamment la capacité des agents à raisonner, planifier et réduire ces "hallucinations" gênantes.
   
* **Déploiement en périphérie** : Imaginez des agents fonctionnant entièrement hors ligne sur votre ordinateur ou appareil local en utilisant des modèles légers comme LLaMA 3 ou Mistral.
   

Dans un avenir très proche, vous verrez des agents intégrés de manière transparente dans :

* Vos pipelines DevOps
   
* Les flux de travail d'entreprise
   
* Les outils de productivité quotidiens
   
* Les applications mobiles et les appareils intelligents
   
* Les jeux, simulations et plateformes éducatives
   

## Résumé final

D'accord, faisons un rapide récapitulatif de toutes les choses cool que vous venez d'apprendre et d'accomplir :

* Vous avez une solide compréhension de ce que sont les agents LLM et pourquoi ils sont si puissants.
   
* Vous avez vu comment les frameworks open source comme LangGraph et CrewAI facilitent la construction d'agents.
   
* Vous avez construit un vrai agent LLM en utilisant LangGraph pour automatiser une tâche quotidienne courante : résumer votre boîte de réception !
   
* Vous avez exploré le monde de la collaboration multi-agents avec CrewAI, en comprenant comment des équipes d'IA peuvent travailler ensemble.
   
* Vous avez appris comment prendre ces principes et les appliquer à l'automatisation de nombreuses autres tâches.
   

Alors, la prochaine fois que vous vous retrouvez coincé à faire quelque chose de répétitif, demandez-vous simplement : "Hé, puis-je construire un agent pour ça ?" La réponse est probablement oui !

### Récapitulatif des ressources

Voici quelques ressources utiles si vous souhaitez approfondir la construction d'agents LLM :

| **Ressource** | **Lien** |
| --- | --- |
| Documentation LangGraph | [https://docs.langgraph.dev/](https://docs.langgraph.dev/) |
| GitHub CrewAI | [https://github.com/joaomdmoura/crewAI](https://github.com/joaomdmoura/crewAI) |
| Documentation LangChain | [https://docs.langchain.com/docs/](https://docs.langchain.com/docs/) |
| Documentation de l'API OpenAI | [https://platform.openai.com/docs](https://platform.openai.com/docs) |
| Python 3.9+ | [https://www.python.org/downloads/](https://www.python.org/downloads/) |
| VSCode | [https://code.visualstudio.com/](https://code.visualstudio.com/) |