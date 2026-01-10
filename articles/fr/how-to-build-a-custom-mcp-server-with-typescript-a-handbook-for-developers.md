---
title: Comment construire un serveur MCP personnalisé avec TypeScript – Un guide pour
  les développeurs
subtitle: ''
author: Sumit Saha
co_authors: []
series: null
date: '2025-06-25T16:31:35.374Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-custom-mcp-server-with-typescript-a-handbook-for-developers
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1750868512407/95f366d3-9115-423a-8d63-66e53171931a.png
tags:
- name: Model Context Protocol
  slug: model-context-protocol
- name: TypeScript
  slug: typescript
- name: JavaScript
  slug: javascript
- name: '#ai-tools'
  slug: ai-tools
seo_title: Comment construire un serveur MCP personnalisé avec TypeScript – Un guide
  pour les développeurs
seo_desc: MCP (Model Context Protocol) lets you connect your code, data, and tools
  to AI applications like Claude and Cursor. This handbook explains how it works with
  real-world analogies, and shows you how to build a custom MCP server using TypeScript
  that fe...
---

MCP (Model Context Protocol) vous permet de connecter votre code, vos données et vos outils à des applications d'IA comme Claude et Cursor. Ce guide explique comment cela fonctionne avec des analogies du monde réel, et vous montre comment construire un serveur MCP personnalisé en utilisant TypeScript qui alimente des données en temps réel dans un environnement d'IA.

### Voici ce que nous allons couvrir :

* [Prérequis](#heading-prerequisites)
    
* [Qu'est-ce que le Model Context Protocol (MCP) ?](#heading-quest-ce-que-le-model-context-protocol-mcp)
    
    * [Que signifie "Protocole" ?](#heading-que-signifie-protocole)
        
    * [Qu'est-ce qu'un "Modèle" ?](#heading-quest-ce-quun-modele)
        
    * [Qu'est-ce que le "Contexte" ?](#heading-quest-ce-que-le-contexte)
        
    * [Mettre tout ensemble : Qu'est-ce que le Model Context Protocol ?](#heading-mettre-tout-ensemble-quest-ce-que-le-model-context-protocol)
        
* [Pourquoi MCP est nécessaire](#heading-pourquoi-mcp-est-necessaire)
    
    * [Le connecteur MCP en action](#heading-le-connecteur-mcp-en-action)
        
    * [Accès universel à travers les plateformes](#heading-acces-universel-a-travers-les-plateformes)
        
    * [Les développeurs sont essentiels](#heading-les-developpeurs-sont-essentiels)
        
    * [Au-delà des intégrations intégrées](#heading-au-dela-des-integrations-integrees)
        
    * [La puissance de la réutilisabilité](#heading-la-puissance-de-la-reutilisabilite)
        
    * [Le fardeau sans MCP](#heading-le-fardeau-sans-mcp)
        
    * [Un exemple pratique avec GitHub](#heading-un-exemple-pratique-avec-github)
        
    * [Pourquoi MCP est important pour les développeurs](#heading-pourquoi-mcp-est-important-pour-les-developpeurs)
        
* [RAG vs MCP](#heading-rag-vs-mcp)
    
    * [Qu'est-ce que RAG](#heading-quest-ce-que-rag)
        
    * [RAG : La préparation "Mise en Place"](#heading-rag-la-preparation-mise-en-place)
        
    * [MCP : Le chariot d'assistant roulant](#heading-mcp-le-chariot-dassistant-roulant)
        
    * [Mettre tout ensemble](#heading-mettre-tout-ensemble)
        
* [Documentation MCP](#heading-documentation-mcp)
    
* [Comment les applications d'IA communiquent avec les serveurs MCP – Un exemple pratique](#heading-comment-les-applications-dia-communiquent-avec-les-serveurs-mcp-un-exemple-pratique)
    
    * [Scénario : Demander à Claude à propos de votre emploi du temps](#heading-scenario-demander-a-claude-a-propos-de-votre-emploi-du-temps)
        
    * [Découverte du bon serveur MCP](#heading-decouverte-du-bon-serveur-mcp)
        
    * [Le serveur MCP récupère et retourne les données](#heading-le-serveur-mcp-recupere-et-retourne-les-donnees)
        
    * [Le modèle convertit les données structurées en langage naturel](#heading-le-modele-convertit-les-donnees-structurees-en-langage-naturel)
        
    * [Sous le capot : Abstraction de la complexité](#heading-sous-le-capot-abstraction-de-la-complexite)
        
    * [Miroir des flux de travail standard des applications web](#heading-miroir-des-flux-de-travail-standard-des-applications-web)
        
* [Comment les serveurs MCP fonctionnent en interne](#heading-comment-les-serveurs-mcp-fonctionnent-en-interne)
    
* [L'architecture MCP – Comment tout s'assemble](#heading-larchitecture-mcp-comment-tout-sassemble)
    
    * [1. Hôte MCP](#heading-1-hote-mcp)
        
    * [2. Client MCP](#heading-2-client-mcp)
        
    * [3. Serveur MCP](#heading-3-serveur-mcp)
        
    * [4. Sources de données – Locales ou distantes](#heading-4-sources-de-donnees-locales-ou-distantes)
        
* [Opportunités pour les développeurs web](#heading-opportunites-pour-les-developpeurs-web)
    
    * [Options de SDK : Choisissez votre langage](#heading-options-de-sdk-choisissez-votre-langage)
        
    * [D'un service backend à un développeur habilité par l'IA](#heading-dun-service-backend-a-un-developpeur-habilite-par-lia)
        
* [Configuration et intégration du serveur MCP](#heading-configuration-et-integration-du-serveur-mcp)
    
* [Résumé](#heading-resume)
    

## Prérequis

Pour suivre ce guide et en tirer le meilleur parti, vous devriez avoir :

1. **Compréhension de base de TypeScript ou JavaScript** : Bien que nous utilisions TypeScript ici, la connaissance de JavaScript seul est suffisante pour suivre les exemples.
    
2. **Familiarité avec Node.js et npm** : Vous devriez savoir comment initialiser un projet, installer des packages et exécuter des scripts en utilisant Node et npm.
    
3. **Expérience avec le terminal/la ligne de commande** : Surtout pour comprendre des concepts comme stdin et stdout, et exécuter des serveurs locaux.
    
4. **Confort avec les variables d'environnement (fichiers .env)** : Vous allez définir des clés API et d'autres données sensibles dans un fichier .env.
    
5. **Connaissance de base des API REST et des concepts HTTP** : Cela aide à comprendre comment nous utilisions les outils d'IA pour récupérer le contexte avant MCP et pourquoi MCP simplifie le processus.
    
6. **Familiarité avec Google Cloud / Console API (optionnel mais recommandé)** : Puisque ce guide implique l'intégration avec Google Calendar, vous devriez savoir comment :
    
    * Générer une clé API publique Google
        
    * Trouver ou créer un Google Calendar et accéder à son ID
        
7. **Éditeur Cursor installé (optionnel mais recommandé)** : Pour suivre les étapes finales d'intégration avec l'éditeur de code alimenté par l'IA.
    
8. **Certaine exposition aux outils d'IA comme Claude, Cursor ou ChatGPT** : Cela vous aide à comprendre comment MCP relie les données externes au contexte de l'IA.
    

J'ai également créé une vidéo pour accompagner ce guide. Si vous êtes du genre à aimer apprendre à partir de vidéos ainsi que de texte, vous pouvez la consulter ici :

%[https://www.youtube.com/watch?v=XC49e0pliEE] 

## Qu'est-ce que le Model Context Protocol (MCP) ?

Commençons par le début : qu'est-ce que le MCP exactement ? MCP signifie **Model Context Protocol**. Et si nous le décomposons mot par mot – "modèle", "contexte" et "protocole" – cela devient en fait assez facile à comprendre.

Mais avant de plonger, voici un rapide contexte : Le Model Context Protocol a été développé par une entreprise appelée [**Anthropic**](https://www.anthropic.com). Vous en avez probablement entendu parler. Ce sont eux qui ont construit [**Claude**](https://claude.ai), l'assistant IA populaire. Ils ont introduit MCP pour la première fois en novembre 2024, et en peu de temps, il est devenu une norme adoptée par de nombreuses autres entreprises, y compris Microsoft.

Maintenant, explorons ce que MCP signifie vraiment en comprenant chaque terme.

### Que signifie "Protocole" ?

Commençons par le dernier mot : Protocole. Que signifie "Protocole" ? Eh bien, c'est un ensemble de règles.

En tant que développeurs, nous travaillons avec des protocoles tout le temps. Par exemple, lorsque nous travaillons avec le **protocole HTTP**, ce n'est pas juste une communication aléatoire – il y a un ensemble de règles que nous suivons. Lorsque nous construisons des API REST, nous utilisons des méthodes spécifiques comme `GET`, `POST`, `PUT`, `PATCH`, ou `DELETE`. Nous transférons des données dans des formats spécifiques comme JSON, XML, ou même JSON-RPC. Tout cela est une communication structurée qui suit un protocole.

De manière similaire, les agents IA ou les applications basées sur l'IA doivent également suivre une approche structurée lors de l'échange d'informations. Nous explorerons cela plus en détail dans un instant, mais pour l'instant, retenez simplement : un protocole est simplement un ensemble de règles.

### Qu'est-ce qu'un "Modèle" ?

Ensuite, parlons du "Modèle". Le terme "Modèle" est quelque chose que vous connaissez probablement déjà assez bien. Nous utilisons tous des modèles d'une manière ou d'une autre, surtout les grands modèles de langage ou LLMs.

Prenez GPT d'OpenAI, Gemini de Google, Claude d'Anthropic – vous pouvez utiliser ceux-ci tous les jours. Il existe de nombreux modèles disponibles maintenant, comme le nouveau DeepSeek et ainsi de suite. Le point est, nous interagissons déjà régulièrement avec des modèles. Nous posons des questions, et ils nous donnent des réponses.

Mais vous êtes-vous déjà demandé comment ces LLMs fonctionnent réellement ? La plupart des gens pensent que lorsque vous demandez quelque chose à un modèle, il va chercher des réponses sur Internet. Mais ce n'est pas comme ça que cela fonctionne.

Ce que ces modèles font réellement, c'est **prédire le mot suivant** dans une phrase – c'est tout. Ils sont des **experts en langage** – ils ne connaissent pas les "faits" en temps réel ou ne récupèrent pas de données en direct sur le web. Au lieu de cela, ils ont été formés avec une énorme quantité d'informations au préalable (pré-formés). Ensuite, lorsque vous demandez quelque chose, ils essaient de déterminer : "Quel mot vient probablement ensuite en fonction de ce que l'utilisateur vient de dire ?"

C'est pourquoi, lorsque vous demandez quelque chose, la réponse apparaît mot par mot – comme si elle était tapée. Et non, ce n'est pas une animation sophistiquée de l'interface utilisateur. C'est simplement comment les LLMs fonctionnent : ils prédisent un mot à la fois. Cela ressemble à de la frappe parce que cela est généré en temps réel, un mot à la fois.

C'est le cœur de **l'IA générative**. Ils sont des experts en langage naturel – comprendre comment nous parlons, prédire ce que nous sommes susceptibles de dire ensuite et générer des réponses en conséquence.

### Qu'est-ce que le "Contexte" ?

Maintenant, passons au "Contexte". En anglais, le contexte signifie le sujet ou l'arrière-plan de quelque chose. Par exemple, lorsque vous envoyez un e-mail, vous ajoutez une ligne d'objet. Et simplement en regardant l'objet, le destinataire se fait une idée de ce dont parle l'e-mail – même avant de l'ouvrir.

De même, lorsque vous parlez à un modèle comme ChatGPT ou Claude, vous fournissez quelques lignes – peut-être une question ou un peu de contexte. Cette entrée devient le "Contexte".

La réponse du modèle dépend entièrement du contexte que vous fournissez. Il utilise ce contexte pour commencer à prédire le mot suivant. Si le modèle sait déjà à quoi vous faites référence, en fonction du contexte, il vous donnera une réponse précise. Mais si vous ne fournissez pas assez de contexte, il ne peut pas vous aider correctement – même s'il s'agit d'un LLM puissant.

Laissez-moi vous donner un exemple simple : Supposons que vous allez voir Claude et que vous demandez : *"Qui suis-je ?"* Sera-t-il capable de répondre à cela ? Non, il ne le sera pas. Mais si dans un message précédent vous aviez dit à Claude : *"Hey, je suis Sumit"* et que plus tard dans la même session vous demandez *"Qui suis-je ?"*, il dira : *"Vous êtes Sumit."* Pourquoi ? Parce qu'il a maintenant du contexte.

Donc, le contexte est juste une information de fond – et meilleur est le contexte que vous donnez, meilleure est la réponse que le modèle peut fournir. C'est ainsi que ces LLMs sont conçus pour fonctionner.

### Mettre tout ensemble : Qu'est-ce que le Model Context Protocol ?

Donc, lorsque nous disons "Model Context Protocol", nous parlons d'un **ensemble de règles ou de protocoles** qui définissent comment alimenter le **contexte** dans un **modèle**. Maintenant, quel est ce contexte que nous alimentons ? Il pourrait s'agir de n'importe quel type d'information externe – quelque chose en dehors des connaissances par défaut du modèle.

C'est comme aller sur Claude Desktop et lui dire : *"Hey, je suis Sumit !"* et ensuite demander : *"Qui suis-je ?"* Encore une fois, il le saura parce que vous le lui avez dit avant.

Mais voici le piège : les modèles ne savent pas magiquement ce qu'il y a dans votre calendrier, vos e-mails, vos bases de données ou vos fichiers. Alors, comment rendre ces données disponibles pour eux ? C'est là que MCP intervient.

MCP nous permet d'alimenter ces morceaux d'informations externes – comme votre emploi du temps, vos données de projet, ou autre chose – dans un modèle, mais de manière structurée et standardisée. Et c'est ce qui rend MCP si puissant.

![Model Context Protocol - Communication structurée](https://cdn.hashnode.com/res/hashnode/image/upload/v1750671107217/c0c8c59d-5c2c-451e-9649-0889cae36c05.png align="center")

## Pourquoi MCP est nécessaire

Maintenant que vous comprenez ce qu'est MCP, parlons de pourquoi nous en avons besoin. Pourquoi Anthropic a-t-il inventé cette chose en premier lieu ?

Réfléchissons à la manière dont nous utilisons différents éditeurs de code dans notre travail quotidien. Un éditeur de code moderne vraiment puissant et équipé d'IA est [Cursor](https://www.cursor.com). Personnellement, je ne l'utilise pas régulièrement, mais il est parfait pour cette démonstration. Imaginez que vous êtes dans votre éditeur Cursor. Et, comme beaucoup d'entre vous le savent, vous pouvez discuter avec Cursor pendant que vous codez. Vous pouvez lui demander d'expliquer quelque chose, de générer du code, de refactoriser la logique, et ainsi de suite.

### Le connecteur MCP en action

Maintenant, supposons que vous demandez à Cursor quelque chose qui dépend des données de votre machine locale – peut-être une grande base de données d'e-mails ou vos propres documents personnels. Cursor peut-il accéder à ces données par défaut ? Non, il ne le peut pas. Mais que se passe-t-il si – et c'est la partie importante – vous connectez un composant personnalisé à Cursor ?

Appelons-le un **serveur MCP**. Si vous connectez votre serveur MCP à Cursor, voici ce qui se passe : Cursor ne peut toujours pas accéder directement à vos fichiers. Mais maintenant, lorsque vous lui posez une question, il se tournera vers ce serveur MCP et dira : "*Hey, savez-vous quelque chose à ce sujet ?"* Et le serveur MCP – puisque vous l'avez construit pour se connecter à vos fichiers ou bases de données – récupérera les informations pertinentes, les transformera en contexte et les renverra au modèle. Maintenant, le modèle a le contexte nécessaire pour générer une réponse intelligente et informée.

Et le meilleur ? Vous n'êtes pas limité à un seul connecteur. Vous pouvez connecter plusieurs serveurs MCP à votre application.

### Accès universel à travers les plateformes

Parlons maintenant d'un exemple réel – quelque chose que je vais vous montrer plus tard avec des exemples de code dans ce guide.

![Comment le serveur MCP communique avec les données locales et génère une réponse](https://cdn.hashnode.com/res/hashnode/image/upload/v1750678334371/7244b0ee-f015-48f2-9433-2cf29a194b06.jpeg align="center")

Supposons que vous demandiez à Cursor : "*Ai-je des réunions aujourd'hui ?"* Maintenant, pour répondre à cela, l'IA aurait besoin d'accéder à votre emploi du temps, n'est-ce pas ? Supposons que vous utilisez Google Calendar pour gérer vos réunions. Cursor peut-il se connecter directement à votre Google Calendar ? Non, il ne le peut pas. Et pas seulement Cursor – ChatGPT ou Claude ne peuvent pas accéder à votre calendrier non plus, à moins que vous ne construisiez manuellement cette intégration.

Mais voici le truc : que se passe-t-il si vous voulez que cela fonctionne universellement ? Comme, peu importe d'où vous posez la question ? Vous pourriez la poser depuis Cursor aujourd'hui, mais quelqu'un d'autre pourrait la poser depuis ChatGPT demain.

Dans les deux cas, nous voulons que ces outils accèdent à votre calendrier et retournent le même résultat. Pour que cela soit possible, nous avons besoin d'une manière universelle de se connecter – et c'est exactement ce qu'un serveur MCP permet. Si vous créez un serveur MCP qui suit le protocole et se connecte à votre calendrier, alors toute application d'IA qui supporte MCP peut s'y connecter et obtenir le bon contexte. C'est une autre raison pour laquelle MCP est si puissant.

![Comment MCP alimente le contexte dans l'éditeur Cursor](https://cdn.hashnode.com/res/hashnode/image/upload/v1750671538182/0955d5b2-48ce-4e12-877b-0eeb7d2ddad2.png align="center")

### Les développeurs sont essentiels

Et le meilleur ? C'est vous (le développeur) qui allez construire ces serveurs MCP. Ce n'est pas quelque chose que les utilisateurs réguliers peuvent construire – vous avez besoin de compétences en codage pour cela.

C'est l'une des raisons pour lesquelles l'IA ne remplacera pas les développeurs tout de suite :)

### Au-delà des intégrations intégrées

Comparons cela à ce qui se passait avant. Par exemple, aujourd'hui, ChatGPT vous permet de faire des recherches sur le web – vous pouvez simplement lui demander de trouver quelque chose en ligne, et il récupérera le résultat. Mais cette fonctionnalité n'est là que parce que [OpenAI](https://openai.com), les créateurs de ChatGPT, l'ont intégrée dans l'application.

Maintenant, imaginez votre propre produit – comme mon site web logicBase Labs. Supposons que des étudiants viennent sur le site et posent des questions via une boîte de chat que vous avez construite. Cet assistant IA vous appartient – il fait partie de votre logiciel. Vous pouvez le connecter à n'importe quel modèle, comme GPT, Claude, peu importe, qui comprend le langage naturel. Mais vous devez toujours lui fournir les bonnes informations pour qu'il puisse répondre de manière significative.

Alors, que faites-vous ? Vous construisez votre propre serveur MCP, peut-être en utilisant Node.js, Python ou Java – peu importe la pile technologique avec laquelle vous êtes à l'aise. Ce serveur MCP est une application complètement autonome. Maintenant, vous construisez également votre interface de chat – l'UI où les étudiants tapent des questions. Vous le connectez au LLM (comme GPT ou Claude) et à votre serveur MCP personnalisé.

### La puissance de la réutilisabilité

Voici le meilleur : votre serveur MCP est maintenant indépendant et réutilisable. Vous pourriez même le donner à une autre entreprise, comme une autre entreprise EdTech qui veut utiliser votre calendrier ou votre logique de gestion de données. Ils peuvent simplement modifier votre serveur MCP, remplacer la logique par leurs propres données et l'utiliser avec leur client de chat. Et boom – c'est maintenant une solution universelle.

Encore mieux, supposons que les données à l'intérieur de mon site web logicBase Labs changent à l'avenir. Pas de problème ! Je n'aurai pas besoin de réécrire la logique du connecteur. Le code qui récupère et formate les données reste le même. Le contenu peut changer, mais la structure est stable.

### Le fardeau sans MCP

Mais si je n'utilisais pas MCP, que devrais-je faire ? Je devrais tout intégrer dans mon client. Chaque assistant IA devrait porter le fardeau de la logique, de la construction du contexte et de la récupération des données. Si quelque chose changeait – disons la structure du dépôt GitHub, le format de l'emploi du temps ou le schéma de la base de données – je devrais aller et mettre à jour chaque client individuellement. C'est un cauchemar !

### Un exemple pratique avec GitHub

Laissez-moi vous donner un autre exemple concret. Supposons que vous voulez connecter votre GitHub à Cursor. Vous voulez dire quelque chose comme : "*Hey, pousse mon code sur GitHub*" – et ça marche. Pour que cela se produise sans MCP, que devriez-vous normalement faire ? Vous devriez :

* Lire la [documentation de l'API GitHub](https://docs.github.com/en/rest)
    
* Écrire la logique d'intégration
    
* Gérer l'authentification OAuth
    
* Traiter les jetons d'accès et les limites de l'API
    

C'est complexe. C'est désordonné. Mais imaginez ceci : Et si GitHub lui-même publiait son propre serveur MCP ? Alors tout ce que vous avez à faire est :

* Brancher ce serveur MCP dans Cursor
    
* Laisser le modèle découvrir les capacités
    
* Dire : "*Pousse mon code*"
    

Et boom – ça marche ! Vous n'avez pas besoin d'écrire de logique d'intégration personnalisée. C'est la magie de MCP. Et voici le meilleur : GitHub a déjà publié son [serveur MCP officiel](https://github.com/github/github-mcp-server). Vous pouvez l'utiliser dès maintenant.

### Pourquoi MCP est important pour les développeurs

J'espère que vous voyez maintenant le tableau plus large. Les serveurs MCP sont un changement de jeu. Ils ne réduisent pas seulement votre charge de travail – ils créent de nouvelles opportunités d'emploi pour des développeurs comme nous. Cela ne va pas "remplacer votre travail". Plutôt, cela crée un nouveau travail précieux qui n'existait pas auparavant.

## RAG vs MCP

Maintenant que nous avons couvert MCP, examinons une autre approche populaire appelée [RAG](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) et voyons comment elles diffèrent. De nombreux constructeurs d'IA commencent par utiliser RAG pour ancrer leurs modèles dans des connaissances statiques, il est donc utile de voir comment cette approche se compare à la diffusion de données en direct avec MCP.

### Qu'est-ce que RAG ?

Tout d'abord, qu'est-ce que RAG ? **Retrieval-Augmented Generation** est une technique dans laquelle un modèle d'IA accède à une "bibliothèque" externe de documents au moment où vous posez une question. Il récupère uniquement les pages dont il a besoin, les insère dans votre prompt et écrit ensuite sa réponse en utilisant ces extraits exacts. En d'autres termes, il s'augmente dynamiquement avec du texte pertinent provenant d'un large corpus.

### RAG : La préparation "Mise en Place"

Imaginez que vous êtes le chef de cuisine préparant le service. Avant l'ouverture des portes, vous et votre équipe faites une **mise en place** complète : vous hachez, mesurez et arrangez chaque ingrédient sur votre comptoir pour qu'il soit prêt au moment où vous en avez besoin. Lorsque les commandes commencent à affluer, vous prenez simplement ce qui est déjà disposé – pas besoin de courir vers la réserve.

Comment cela fonctionne :

1. Récupérer : Votre système recherche dans un magasin de documents les "ingrédients" (extraits de texte) les plus pertinents.
    
2. Augmenter : Ces extraits sont mélangés dans votre prompt d'IA.
    
3. Générer : Le modèle prépare une réponse ancrée dans ce lot d'informations.
    

RAG est idéal pour le contenu statique ou rarement modifié (pensez aux manuels de politique, aux articles de recherche ou à tout "livre de recettes" qui n'est pas réécrit en cours de service).

### MCP : Le chariot d'assistant roulant

Maintenant, imaginez qu'en plein milieu du dîner, vous réalisez que vous avez besoin d'une herbe fraîche ou d'une garniture spéciale qui n'était pas préparée. Au lieu d'arrêter la cuisine, vous faites rouler un chariot d'assistant chargé de tous les nouveaux articles qui apparaissent – ils vous apportent cette garniture dès qu'elle est prête.

Comment cela fonctionne :

1. Abonnement/Flux : Votre client IA ouvre une ligne directe vers la source de données.
    
2. Livraison : Dès que de nouvelles données (comme une mise à jour de commande en direct ou une lecture de capteur) sont disponibles, elles vous sont apportées.
    
3. Consommation : Votre modèle peut puiser dans ces données fraîches à tout moment pendant la génération.
    

MCP est idéal pour les scénarios nécessitant des informations à la minute (comme les tableaux de bord en direct, les chatbots se nourrissant de l'activité récente des utilisateurs, les flux de capteurs IoT, etc.).

### Mettre tout ensemble

* RAG seul : Meilleur lorsque votre "mise en place" est suffisamment extensive pour couvrir tout ce dont vous avez besoin – des connaissances de fond pré-préparées.
    
* MCP seul : Requis lorsque vous avez besoin d'un "chariot roulant" d'ingrédients frais à portée de main.
    
* Approche combinée : Faites votre "mise en place" de fond avec RAG pour un contexte approfondi, et gardez le chariot d'assistant roulant avec MCP pour fournir des mises à jour en direct – afin que votre IA ait des connaissances de fond approfondies ainsi que de la fraîcheur en temps réel.
    

## Documentation MCP

Examinons maintenant la [documentation officielle MCP](https://modelcontextprotocol.io/introduction). Cela aidera à clarifier les choses. Alors, que dit la définition ?

> MCP est un protocole ouvert qui standardise la manière dont les applications fournissent du contexte aux LLMs. ([Source : Documentation MCP](https://modelcontextprotocol.io/introduction))

Oui – exactement ce dont nous avons déjà parlé. Ensuite, vient une ligne brillante de la documentation :

> Pensez à MCP comme à un port USB-C pour les applications d'IA. ([Source : Documentation MCP](https://modelcontextprotocol.io/introduction))

Faisons une pause ici, car cette analogie est super importante. Pensez au port USB-C sur les appareils modernes. Nous l'utilisons tous. Mais vous souvenez-vous de ce que c'était avant ? À l'époque, votre ordinateur avait des tonnes de ports différents – HDMI, VGA, USB-A, prise audio, vous voyez le genre. Vous deviez gérer différents câbles pour tout. Peut-être que votre souris était USB-A, votre clavier utilisait un autre port, et votre moniteur externe avait besoin de HDMI. C'était un vrai bazar.

![Analogie du connecteur universel USB-C](https://cdn.hashnode.com/res/hashnode/image/upload/v1750678229073/7df559c2-48bf-4a39-8415-31276609ca98.jpeg align="center")

Mais maintenant ? Tout utilise USB-C. Un connecteur universel pour les données, l'alimentation, l'audio, la vidéo – tout. C'est exactement ce que MCP est pour les applications d'IA. Au lieu de construire des intégrations ou des connecteurs séparés pour chaque outil d'IA (Cursor, ChatGPT, Claude, etc.), vous construisez maintenant un serveur MCP standardisé et tout outil d'IA qui supporte MCP peut s'y connecter. C'est pourquoi ce protocole est une si grosse affaire.

## Comment les applications d'IA communiquent avec les serveurs MCP – Un exemple pratique

Laissez-moi vous guider à travers un autre exemple pour vous aider à vraiment comprendre cela. Imaginez que vous utilisez Claude. Vous lui posez une question simple : "*Ai-je une réunion aujourd'hui ?*"

### Scénario : Demander à Claude à propos de votre emploi du temps

Maintenant, Claude n'a pas réellement cette information. Si vous n'avez connecté aucun serveur MCP, il vous donnera une réponse vague. Probablement quelque chose de gentil et générique, car il est bon en langage naturel – mais pas spécifique. Mais si vous voulez une vraie réponse – quelque chose de factuel – vous devez lui fournir du contexte. Et c'est là que le serveur MCP intervient.

![Réponse vague de Claude sans MCP](https://cdn.hashnode.com/res/hashnode/image/upload/v1750671970459/c1cecbfc-1012-4580-ba95-ccfeb0854129.png align="center")

### Découverte du bon serveur MCP

Supposons que Claude est connecté à un serveur MCP. Les choses deviennent intéressantes. Dès que vous posez la question, Claude regardera d'abord la liste des serveurs MCP auxquels il est connecté. Ensuite, il choisira intelligemment le bon et demandera :

*"Hey, quelles sont vos capacités ?"*

Parce que votre serveur MCP pourrait être capable de faire beaucoup de choses. Peut-être qu'il peut :

* Donner une liste complète des événements du calendrier
    
* Vérifier s'il y a une réunion à une date spécifique
    
* Récupérer des données depuis Google Calendar
    
* Résumer des documents
    

Donc, le modèle détermine d'abord :

*"Quelles sont ces capacités dont j'ai besoin ?"*

Dans ce cas, il décide :

*"D'accord, je dois juste savoir si l'utilisateur a une réunion aujourd'hui."*

Ensuite, Claude envoie un message au serveur MCP – dans un format spécifique, que nous examinerons sous peu. C'est un peu comme le fonctionnement des API REST. Le message dit quelque chose comme :

*"Voici la date. Dites-moi si l'utilisateur a une réunion."*

### Le serveur MCP récupère et retourne les données

Maintenant, le serveur MCP prend cette entrée, se connecte à Google Calendar (ou à la source que vous avez configurée) et exécute la logique nécessaire. Finalement, il envoie une réponse, généralement dans un format structuré comme **JSON-RPC**. Il peut retourner une liste de réunions ou juste une – selon ce qui s'applique.

### Le modèle convertit les données structurées en langage naturel

Maintenant, voici la beauté de la chose. Même si le serveur MCP retourne quelque chose de technique (comme JSON), Claude ne le montrera jamais à l'utilisateur. Parce que c'est un **modèle de langage**, il convertira ces données structurées en une phrase naturelle et fluide comme :

*"Oui, vous avez une réunion avec Dr. Chuck à 16h."*

![Réponse positive de Claude avec le serveur MCP](https://cdn.hashnode.com/res/hashnode/image/upload/v1750672087724/efa2637d-1a35-4f7a-b8f6-2d9183580c23.png align="center")

### Sous le capot : Abstraction de la complexité

Pour l'utilisateur, cela semble magique. Mais derrière les scènes, beaucoup de choses viennent de se passer :

* Le modèle a trouvé le bon serveur MCP
    
* Il a sélectionné la bonne capacité
    
* Il a passé l'entrée correcte
    
* Le serveur a exécuté la logique, obtenu les données et retourné un résultat structuré
    
* Et enfin, le modèle a transformé cela en langage humain
    

### Miroir des flux de travail standard des applications web

C'est exactement comme cela que nos sites web fonctionnent aussi. Supposons qu'un utilisateur visite votre site web et tape quelque chose dans une boîte de message. Vous récupérez des données en backend, peut-être appelez une API ou exécutez une requête de base de données. Cette réponse revient en JSON – mais l'utilisateur ne voit jamais cela. Ce qu'il voit, c'est la réponse finale polie de l'UI. Même principe ici. Donc j'espère qu'il est maintenant clair à quel point ce système est puissant.

## Comment les serveurs MCP fonctionnent en interne

Maintenant, allons un peu plus loin et comprenons comment un serveur MCP fonctionne réellement sous le capot – techniquement. Un serveur MCP fonctionne principalement à travers quelque chose appelé **entrée et sortie standard**, ou en termes de programmation, `stdin` et `stdout`. Alors, que signifie cela ? Décomposons-le avec un exemple.

Vous savez, lorsque vous ouvrez un terminal dans l'éditeur Cursor, il vous donne un shell de base où vous pouvez taper des commandes ? Ce terminal utilise le système d'entrée et de sortie standard de votre machine.

Maintenant, typiquement, lorsque les sites web communiquent avec des API, ils utilisent des API REST sur HTTP. Mais avec les serveurs MCP – surtout lorsqu'ils sont utilisés localement – nous n'utilisons pas HTTP. Voici pourquoi : beaucoup de fois, votre serveur MCP s'exécute sur votre propre machine, connecté à des bases de données ou des fichiers locaux. Donc, au lieu de passer par des appels réseau, il utilise une communication directe au niveau du système via `stdin` et `stdout`.

![Processus de transport local MCP similaire à l'API REST](https://cdn.hashnode.com/res/hashnode/image/upload/v1750678140969/9f22b8a9-9c56-45cc-95ae-5b946e379133.jpeg align="center")

Supposons que vous êtes dans Cursor, et que vous tapez quelque chose comme :

```bash
echo "hello"
```

Que se passe-t-il ? Le terminal lit votre entrée (`stdin`), la traite et imprime `hello` en retour via `stdout`. Ce même schéma est utilisé par les serveurs MCP.

Maintenant, imaginez que l'application d'IA (comme Claude) essaie de parler à votre serveur MCP. Comment fait-elle cela ? Elle n'envoie pas de requête HTTP comme un client web. Au lieu de cela, elle écrit la requête directement dans l'**entrée standard** du serveur MCP – tout comme le fonctionnement d'une commande de terminal. Et ensuite, votre serveur MCP lit cette entrée, effectue l'action nécessaire (peut-être qu'il parle à Google Calendar, une base de données, un système de fichiers, peu importe) et une fois terminé, il envoie la réponse en utilisant la **sortie standard**.

Imaginons une conversation réelle entre Claude et votre serveur MCP. Vous demandez à Claude :

*"Ai-je une réunion aujourd'hui ?"*

Claude réalise qu'il n'a pas cette information par lui-même. Alors, que fait-il ? D'abord, il découvre les outils ou méthodes disponibles – il vérifie tous les serveurs MCP connectés pour voir ce qu'ils peuvent faire. Ensuite, il détermine intelligemment la meilleure méthode à utiliser. Supposons qu'il détermine :

*"D'accord, je devrais appeler la méthode* `calendar` *."*

Il écrit ensuite une entrée structurée dans le stdin de votre serveur MCP, quelque chose comme :

```json
{

0 
0 "method": "calendar",

0 
0 "params": {

0 
0 
0 
0 "date": "2025-06-16"

0 
0 }
}
```

D'accord, le format réel peut différer, mais conceptuellement, c'est comme ça. Votre serveur MCP reçoit ensuite cette entrée, exécute la logique, récupère peut-être des données depuis votre Google Calendar, et répond ensuite comme ceci :

```json
{

0 
0 "result": {

0 
0 
0 
0 "meetings": [

0 
0 
0 
0 
0 
0 {

0 
0 
0 
0 
0 
0 
0 
0 "title": "Team Sync",

0 
0 
0 
0 
0 
0 
0 
0 "time": "4:00 PM"

0 
0 
0 
0 
0 
0 }

0 
0 
0 
0 ]

0 
0 }
}
```

Maintenant, voici le plus important : Claude ne montre pas ce JSON à l'utilisateur.

Il lit ces données brutes, exécute son modèle de langage naturel, et dit enfin :

*"Oui, vous avez une réunion 'Team Sync' aujourd'hui à 16h."*

C'est tout le cycle de vie. Et l'utilisateur ? Il ne sait même pas ce qui se passe en coulisses. Tout comme lorsqu'une personne non technique utilise votre site web, elle ne connaît pas les appels fetch ou les réponses JSON. Elle voit simplement une interface utilisateur fluide. Même principe ici.

Et cette approche `stdin`/`stdout` fonctionne très bien localement – surtout pour les données sur votre machine. Plus tard, nous verrons comment les choses fonctionnent différemment lorsque vous vous connectez à des services distants. Mais pour l'instant, retenez simplement :

MCP n'utilise pas d'appels HTTP pour la communication locale. Il fonctionne via le terminal – `stdin` et `stdout`.

Et cela le rend rapide, sécurisé et incroyablement flexible.

## L'architecture MCP – Comment tout s'assemble

Examinons maintenant l'architecture MCP. Une fois que vous verrez la structure, tout ce que nous avons discuté aura encore plus de sens. Voici ce que montre le diagramme (le diagramme a été collecté à partir de la [documentation MCP](https://modelcontextprotocol.io/introduction)) :

[![Diagramme d'architecture MCP provenant de la documentation](https://cdn.hashnode.com/res/hashnode/image/upload/v1750672357388/9d07577d-447e-4a13-b205-1d0e72b5d18a.png align="center")](https://modelcontextprotocol.io/introduction)

Nous avons un **hôte** – qui pourrait être Claude, ou toute application alimentée par l'IA. Cet hôte est connecté à un ou plusieurs **serveurs MCP** via le **protocole MCP**. Et ces serveurs MCP sont à leur tour connectés à des **sources de données externes**, qui pourraient être des fichiers locaux ou des services distants comme des API, des calendriers, des bases de données, etc.

Maintenant, que fait le serveur MCP ? Il récupère les données de ces sources externes, prépare le contexte approprié et le renvoie à l'hôte en utilisant le protocole MCP. Ce contexte est ensuite utilisé par le LLM pour générer une réponse pertinente et naturelle.

Toute cette communication – au moins lorsqu'elle est effectuée localement – se fait via l'entrée et la sortie standard (`stdin` et `stdout`) comme nous l'avons discuté précédemment.

Passons en revue les composants un par un.

### 1. Hôte MCP

Tout d'abord, nous avons l'hôte MCP. Il s'agit de l'application d'IA, quelque chose comme Claude, Cursor, ou même votre propre interface d'IA. Si nous comparons cela à l'architecture web traditionnelle, l'hôte est comme le serveur de votre site web – le cerveau principal qui dirige le spectacle. Dans le contexte de Cursor, l'éditeur Cursor lui-même est l'hôte MCP.

### 2. Client MCP

Ensuite, nous avons le client MCP. Alors, qu'est-ce que le client dans ce contexte ? Eh bien, en développement web, pensez au navigateur de l'utilisateur comme le client – pas l'utilisateur lui-même, mais le navigateur réel qui envoie des requêtes et reçoit des réponses. Dans le monde MCP, le client MCP est la partie interne de l'hôte qui se connecte aux serveurs MCP.

Prenons à nouveau Cursor comme exemple.

Si vous allez dans les paramètres de Cursor, vous verrez quelque chose appelé **MCP Tools**. C'est là que vous pouvez ajouter n'importe quel serveur MCP personnalisé. Cursor a un client intégré qui vous permet de brancher votre propre serveur. Si vous construisiez votre propre éditeur comme Cursor, vous devriez écrire cette logique client vous-même pour gérer des choses comme la découverte de serveurs, la mise en forme des requêtes et la lecture des réponses. Bonne nouvelle, il existe [déjà une spécification et des bibliothèques](https://modelcontextprotocol.io/quickstart/client) pour aider avec cela aussi.

### 3. Serveur MCP

Ensuite, bien sûr, vient le serveur MCP, dont nous avons déjà longuement parlé. C'est l'outil que vous construisez qui sait comment récupérer ou générer du contexte à partir de fichiers, d'API, de calendriers, de n'importe quoi. Vous pouvez le faire avec Node, Python, Java – ce que vous voulez. Tant qu'il suit le protocole, il fonctionnera. Et rappelez-vous – il peut être réutilisé à travers différentes applications d'IA. C'est la beauté de MCP.

### 4. Sources de données – Locales ou distantes

Enfin, mais non des moindres, nous avons les sources de données. Votre serveur MCP doit récupérer des données de quelque part. Ce "quelque part" pourrait être :

* Une base de données SQLite ou Postgres locale
    
* Votre système de fichiers
    
* Une API externe comme Google Calendar ou GitHub
    
* Un tableau de bord SaaS tiers
    
* N'importe quoi d'autre qui contient un contexte pertinent
    

Le point est : vous abstraisez la gestion des données dans votre serveur MCP. Ainsi, l'hôte IA ne se soucie pas de la manière dont les données sont récupérées – il obtient simplement un contexte structuré en retour.

Donc, pour résumer :

* L'**hôte MCP** est votre application d'IA (comme Claude, Cursor ou une application personnalisée).
    
* Le **client MCP** est le pont à l'intérieur de cet hôte qui se connecte aux serveurs MCP externes.
    
* Le **serveur MCP** est ce que vous, le développeur, construisez – pour fournir du contexte.
    
* Et les **sources de données** sont les services backend ou fichiers qui contiennent vos connaissances.
    

Tout communique entre eux via le protocole MCP. Et localement, tout se passe via `stdin`/`stdout`, comme une conversation entre programmes dans le terminal. Donc, c'est tout le résumé en une seule fois. J'espère que vous comprenez maintenant comment tout cela fonctionne.

![Les composants MCP communiquent entre eux](https://cdn.hashnode.com/res/hashnode/image/upload/v1750672511389/bd68a3f8-7bf3-4fcc-b631-c99a4ea05667.png align="center")

## Opportunités pour les développeurs web

### Options de SDK : Choisissez votre langage

D'accord, nous allons bientôt commencer à construire un serveur MCP – et pour cela, nous utiliserons le SDK TypeScript. Maintenant, si vous regardez la documentation, vous remarquerez qu'il existe de nombreux SDK disponibles. Vous pouvez construire des serveurs MCP en utilisant :

* C#
    
* Java
    
* Kotlin
    
* Python
    
* Ruby
    
* Swift (pour mobile)
    
* et bien sûr, TypeScript – qui est essentiellement JavaScript avec des superpouvoirs !
    

Et puisque JavaScript est comme ma langue maternelle, je vais naturellement choisir TypeScript ici. Maintenant, ne vous inquiétez pas – cela ne sera pas super technique. Je ne vais pas m'asseoir et coder ligne par ligne avec vous, mais je vais vous guider à travers les parties importantes pour que vous ayez une compréhension claire.

### D'un service backend à un développeur habilité par l'IA

Ce que vous allez trouver, c'est que tout ce que nous allons faire ici est quelque chose que vous connaissez probablement déjà. Parce que c'est encore juste du codage régulier. Vous allez construire un service backend – tout comme celui que vous avez peut-être fait des centaines de fois auparavant. La seule différence est que maintenant, votre application fera partie de l'**écosystème MCP**.

Pensez à cela comme ceci : En tant que développeur, vous ne changez pas de carrière. Vous n'abandonnez pas vos compétences actuelles. Vous faites toujours ce que vous avez toujours fait – écrire de la logique, structurer des données, gérer des API. Le seul changement est dans **où** vous branchez ce code. Au lieu de simplement servir des requêtes HTTP ou de retourner des composants React, maintenant votre code sera utilisé pour alimenter du contexte dans les LLMs. Et cela, c'est le pont vers le monde de l'IA.

Soyons réalistes : dans le monde d'aujourd'hui, construire une autre application CRUD n'est pas suffisant. Si votre application n'est pas profondément intégrée dans l'écosystème de l'IA, elle va se faire distancer. Mais si vous comprenez des concepts comme MCP, et si vous savez comment construire et exposer du contexte structuré à n'importe quel modèle, alors vous n'êtes plus simplement un développeur. Vous êtes un développeur habilité par l'IA !

Vous construisez l'infrastructure qui connecte les données du monde réel aux applications d'IA. Et c'est énorme ! C'est pourquoi je crois vraiment que tout cet écosystème MCP va exploser dans les mois et années à venir. Je crois que les entreprises du monde entier vont commencer à construire et à publier leurs propres serveurs MCP – tout comme tout le monde construit maintenant des API ou des SDK. Bientôt, nous atteindrons un point où les gens ne visiteront plus le site web de votre entreprise pour remplir un formulaire ou lire des FAQ statiques. Ils poseront simplement une question à l'intérieur de ChatGPT, Claude ou Cursor, comme :

*"Quels sont les plans tarifaires pour logicBase Labs ?"*

Et ils obtiendront une réponse – non pas parce que ces modèles sont formés sur votre site web, mais parce que vous avez construit un serveur MCP qui leur donne des données en temps réel, personnalisées et authentifiées.

Alors oui, maintenant, allons de l'avant et construisons notre premier serveur MCP – rapidement et de manière facile à suivre. Parce qu'en fin de compte, c'est là que des développeurs comme vous appartiennent : en réunissant le meilleur de vos compétences existantes et en les appliquant à l'intérieur de l'univers de l'IA.

## Configuration et intégration du serveur MCP

Alors, pour construire un serveur MCP, nous avons atterri sur la page officielle du dépôt GitHub pour le [SDK TypeScript de MCP](https://github.com/modelcontextprotocol/typescript-sdk). Maintenant, pour ceux d'entre vous qui ne connaissent pas TypeScript, il n'y a rien à craindre. Parce que TypeScript est essentiellement un sur-ensemble de JavaScript. Donc même si vous n'êtes pas familier avec TypeScript, ce n'est pas grave. Vous pouvez écrire votre code en JavaScript simple, et puisque tout code JavaScript valide est également du TypeScript valide, vous êtes prêt à partir.

Et si vous êtes un développeur JavaScript régulier, vous trouverez tout ici familier – comme vous vous y attendez de toute documentation typique. Ils ont fourni un petit modèle simple pour un serveur TypeScript. C'est une configuration de serveur minimale et unique, et c'est exactement le modèle que j'utiliserais pour construire mon propre serveur. Passons en revue la configuration.

Mon projet est un projet Node.js. J'ai créé un fichier `server.js`, et honnêtement, c'est le seul fichier que j'ai utilisé dans ce projet. Tout le code est écrit à l'intérieur de ce fichier.

Étape par étape, voici ce que j'ai fait :

#### 1. Initialiser le projet

```bash
npm init
```

Cela crée le fichier `package.json`.

#### 2. Installer le package MCP requis

Exécutez la commande d'installation (mentionnée dans la [documentation](https://github.com/modelcontextprotocol/typescript-sdk)).

```bash
npm install @modelcontextprotocol/sdk
```

#### 3. Importer et créer le serveur MCP

J'ai importé `McpServer` du package installé puis créé une nouvelle instance en utilisant `new McpServer()`. Vous devez passer un objet avec un nom et une version :

```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";

// créer le serveur MCP
const server = new McpServer({
    name: "Calendrier de Sumit",
    version: "1.0.0",
});
```

#### 4. Ajouter un outil (fonction)

Les outils sont les fonctions que votre client IA peut invoquer. J'ai utilisé la fonction `server.tool()` du SDK et passé trois choses :

* Un nom significatif : `getMyCalendarDataByDate` afin que mon application IA comprenne quel outil appeler
    
* Validation de l'entrée en utilisant `zod`
    
* Une fonction de rappel asynchrone qui récupère les données de réunion
    

```typescript
// enregistrer l'outil dans MCP
server.tool(
    "getMyCalendarDataByDate",
    {
        date: z.string().refine((val) => !isNaN(Date.parse(val)), {
            message: "Format de date invalide. Veuillez fournir une chaîne de date valide.",
        }),
    },
    async ({ date }) => {
        return {
            content: [
                {
                    type: "text",
                    text: JSON.stringify(await getMyCalendarDataByDate(date)),
                },
            ],
        };
    }
);
```

Le rappel reçoit la date validée et l'utilise pour appeler une fonction de contrôleur asynchrone appelée `getMyCalendarDataByDate` qui récupère les données de Google Calendar. Maintenant, nous allons écrire la fonction.

#### 5. Intégration de Google Calendar

Tout d'abord, nous devons installer le package `googleapis` avec la commande suivante dans le terminal :

```bash
npm install googleapis
```

Ensuite, importer l'objet `google` du package installé.

```typescript
import { google } from "googleapis";
```

Maintenant, écrivons la fonction `getMyCalendarDataByDate` et appelons la méthode `google.calendar` selon l'[API Google Calendar](https://developers.google.com/workspace/calendar/api/quickstart/nodejs). Cette méthode `google.calendar()` reçoit un objet en tant que paramètre et nous devons mentionner `version` et `auth` ici. `version` est simplement le numéro de version de l'API Calendar et `auth` est la clé API publique de Google pour l'authentification.

```typescript
async function getMyCalendarDataByDate(date) {
    const calendar = google.calendar({
        version: "v3",
        auth: process.env.GOOGLE_PUBLIC_API_KEY,
    });
}
```

Ici, vous pouvez voir que j'ai utilisé la clé API publique de Google comme variable d'environnement. Donc, nous allons créer un fichier `.env` à la racine du répertoire du projet et ajouter ce qui suit à l'intérieur de ce fichier :

```plaintext
GOOGLE_PUBLIC_API_KEY=ÉCRIRE_VOTRE_CLÉ_API_PUBLIQUE_GOOGLE
```

N'oubliez pas de remplacer par votre propre clé API publique Google. Vous pouvez récupérer votre clé publique depuis la [Console Cloud Google](https://cloud.google.com/cloud-console).

Maintenant, nous devons calculer le `début` et la `fin` de la date donnée (UTC) reçue sous forme de `chaîne` dans le paramètre `date` de la fonction `getMyCalendarDataByDate`.

```typescript
// Calculer le début et la fin de la date donnée (UTC)
const start = new Date(date);
start.setUTCHours(0, 0, 0, 0);
const end = new Date(start);
end.setUTCDate(end.getUTCDate() + 1);
```

Maintenant, il est temps de récupérer la liste des événements depuis mon Google Public Calendar. Pour cela, selon l'API Google Calendar, nous devons appeler la fonction `calendar.events.list` et lui passer les options nécessaires :

```typescript
const res = await calendar.events.list({
    calendarId: process.env.CALENDAR_ID,
    timeMin: start.toISOString(),
    timeMax: end.toISOString(),
    maxResults: 10,
    singleEvents: true,
    orderBy: "startTime",
});
```

Ici, vous pouvez voir que j'ai mentionné mon ID de calendrier public en utilisant une autre variable d'environnement appelée `CALENDAR_ID`. Donc, retournez à votre fichier .env et définissez la nouvelle variable d'environnement :

```plaintext
CALENDAR_ID=VOTRE_PROPRE_ID_DE_CALENDRIER_PUBLIC
```

Juste une petite note – votre `CALENDAR_ID` sera simplement votre adresse e-mail Google, par exemple `quelquun@gmail.com`. N'oubliez pas non plus de rendre votre calendrier public, sinon cet exemple et cette configuration d'API ne fonctionneront pas.

Pour rendre votre Google Calendar public, vous devez ajuster les paramètres de partage du calendrier dans Google Calendar sur un ordinateur. Naviguez jusqu'au calendrier que vous souhaitez partager, puis trouvez la section "Autorisations d'accès pour les événements" et cochez la case étiquetée "Rendre disponible au public". Vous pouvez ensuite choisir le niveau d'accès que vous souhaitez accorder aux autres.

Voici un guide étape par étape :

* Allez sur [Google Calendar](https://calendar.google.com/) sur votre ordinateur.
    
* Trouvez le calendrier que vous souhaitez partager sous la section "Mes calendriers" sur le côté gauche de l'écran.
    
* Cliquez sur les trois points (Plus) à côté du nom du calendrier et sélectionnez "Paramètres et partage".
    
* Sous "Autorisations d'accès pour les événements", cochez la case à côté de "Rendre disponible au public".
    

Et pour les options `timeMin` et `timeMax`, j'ai utilisé les dates et heures de `début` et `fin` que nous venons de calculer ci-dessus.

Maintenant, nous allons obtenir le tableau `events` à partir de `res.data.items` puis mapper ces événements pour obtenir le tableau final `meetings`. Nous devons également gérer le tableau vide pour aucun événement.

```typescript
const events = res.data.items || [];
const meetings = events.map((event) => {
    const start = event.start.dateTime || event.start.date;
    return `${event.summary} à ${start}`;
});

if (meetings.length > 0) {
    return {
        meetings,
    };
} else {
    return {
        meetings: [],
    };
}
```

Faisons un peu de gestion des erreurs. Nous allons simplement pousser notre logique de récupération d'événements ci-dessus à l'intérieur d'un bloc `try/catch` et gérer l'erreur à l'intérieur du bloc `catch`. Donc voici notre code mis à jour :

```typescript
try {
    const res = await calendar.events.list({
        calendarId: process.env.CALENDAR_ID,
        timeMin: start.toISOString(),
        timeMax: end.toISOString(),
        maxResults: 10,
        singleEvents: true,
        orderBy: "startTime",
    });

    const events = res.data.items || [];
    const meetings = events.map((event) => {
        const start = event.start.dateTime || event.start.date;
        return `${event.summary} à ${start}`;
    });

    if (meetings.length > 0) {
        return {
            meetings,
        };
    } else {
        return {
            meetings: [],
        };
    }
} catch (err) {
    return {
        error: err.message,
    };
}
```

Pour exécuter le serveur localement en utilisant `stdin`/`stdout`, j'ai utilisé la fonction `stdioServerTransport()` du package MCP et je l'ai passée à la méthode `start()` du serveur. Cette partie ressemble à ceci :

```typescript
const transport = stdioServerTransport();
server.start(transport);
```

Ensuite, j'ai enveloppé tout cela à l'intérieur d'une fonction asynchrone `init()` pour éviter l'`await` de niveau supérieur et j'ai appelé la fonction `init`.

```typescript
function init(){
    const transport = stdioServerTransport();
    server.start(transport);
}

init();
```

#### 6. Code source final

Voici donc le code complet pour mon fichier `server.js` :

```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import dotenv from "dotenv";
import { google } from "googleapis";
import { z } from "zod";

dotenv.config();

// créer le serveur MCP
const server = new McpServer({
    name: "Calendrier de Sumit",
    version: "1.0.0",
});

// fonction outil
async function getMyCalendarDataByDate(date) {
    const calendar = google.calendar({
        version: "v3",
        auth: process.env.GOOGLE_PUBLIC_API_KEY,
    });

    // Calculer le début et la fin de la date donnée (UTC)
    const start = new Date(date);
    start.setUTCHours(0, 0, 0, 0);
    const end = new Date(start);
    end.setUTCDate(end.getUTCDate() + 1);

    try {
        const res = await calendar.events.list({
            calendarId: process.env.CALENDAR_ID,
            timeMin: start.toISOString(),
            timeMax: end.toISOString(),
            maxResults: 10,
            singleEvents: true,
            orderBy: "startTime",
        });

        const events = res.data.items || [];
        const meetings = events.map((event) => {
            const start = event.start.dateTime || event.start.date;
            return `${event.summary} à ${start}`;
        });

        if (meetings.length > 0) {
            return {
                meetings,
            };
        } else {
            return {
                meetings: [],
            };
        }
    } catch (err) {
        return {
            error: err.message,
        };
    }
}

// enregistrer l'outil dans MCP
server.tool(
    "getMyCalendarDataByDate",
    {
        date: z.string().refine((val) => !isNaN(Date.parse(val)), {
            message: "Format de date invalide. Veuillez fournir une chaîne de date valide.",
        }),
    },
    async ({ date }) => {
        return {
            content: [
                {
                    type: "text",
                    text: JSON.stringify(await getMyCalendarDataByDate(date)),
                },
            ],
        };
    }
);

// définir le transport
async function init() {
    const transport = new StdioServerTransport();
    await server.connect(transport);
}

// appeler l'initialisation
init();
```

Ensuite, installez les packages nécessaires `dotenv`, `googleapis` et `zod` avec la commande suivante :

```bash
npm install dotenv googleapis zod
```

Maintenant, vous pouvez démarrer le serveur avec la commande `node server.js` dans votre terminal et vérifier si tout fonctionne correctement ou non. Au cas où vous obtiendriez un avertissement pour ajouter une ligne `type: "module"` à l'intérieur de votre fichier `package.json`, allez-y et faites-le. Cet avertissement est attendu car nous utilisons la syntaxe de module ES pour importer nos packages au lieu de la syntaxe Common JS par défaut.

Enfin, nous avons terminé avec la partie codage.

#### 7. Connexion avec l'éditeur Cursor

Après avoir configuré le serveur, j'ai dû l'enregistrer dans l'éditeur **Cursor** :

Commencez par ouvrir les paramètres de Cursor → Outils & Intégrations → Nouveau serveur MCP.

![Comment connecter le serveur MCP dans cursor](https://cdn.hashnode.com/res/hashnode/image/upload/v1750673140780/14ac470e-38e7-4cf4-bef8-823fc155c015.png align="center")

À l'intérieur de l'objet, fournissez un nouvel objet avec les propriétés suivantes selon le [guide de configuration du client Cursor](https://docs.cursor.com/context/model-context-protocol#manual-configuration) mentionné dans la [documentation Cursor](https://docs.cursor.com/welcome) :

* Un nom : `Données du calendrier de Sumit`
    
* Commande : `node`
    
* Arguments : chemin complet vers `server.js`
    
* Variables d'environnement : clé API et ID du calendrier
    

Exemple :

```json
{
    mcpServers: {
        "sumits-calendar-data": {
            command: "node",
            args: ["/full/path/to/project/server.js"],
            env: {
                GOOGLE_API_KEY: "...",
                CALENDAR_ID: "...",
            },
        },
    },
}
```

![Comment connecter le serveur MCP dans Cursor](https://cdn.hashnode.com/res/hashnode/image/upload/v1750673187700/9a07465a-0e7b-4bb7-9523-286dcf38373a.png align="center")

Enregistrez et redémarrez Cursor. L'outil apparaîtra maintenant comme **actif (vert)**.

#### 8. Testez votre serveur MCP

Maintenant, ouvrez la fenêtre de chat de Cursor et tapez :

*"Ai-je des réunions aujourd'hui ?"*

Vous verrez que :

* Il détecte l'intention
    
* Choisit le bon outil MCP
    
* Passe la date d'aujourd'hui comme entrée
    
* Le serveur MCP retourne des données structurées
    
* Le client IA répond naturellement. Dans mon cas, j'ai enregistré un événement dans mon Google Calendar à la date d'aujourd'hui, donc il a retourné :
    

*"Oui, vous avez une réunion avec Dr. Chuck à 16h."*

Cela fonctionne même dans d'autres langues. Si vous posez la même question dans une autre langue que l'anglais, vous obtenez toujours la bonne réponse. Si aucune réunion n'est prévue pour une date donnée, par exemple si vous écrivez :

*"Ai-je une réunion demain ?"

Il répond :

*"Non, vous n'avez aucune réunion prévue pour demain."*

Ainsi, votre serveur MCP personnalisé fonctionne maintenant pleinement, alimentant des données réelles depuis Google Calendar dans votre éditeur d'IA.

Cela ouvre d'énormes possibilités. Imaginez la même approche avec GitHub, Notion, des tableaux de bord internes, des CRM – n'importe quoi. Tout commence par la construction et le câblage de votre serveur MCP de la bonne manière.

Faites-moi savoir si vous aimeriez en construire un pour votre propre projet ! Et si ce guide a été même un peu utile pour mettre en place votre premier serveur MCP, j'adorerais en entendre parler – ce serait une grande inspiration pour moi d'écrire plus de guides comme celui-ci à l'avenir.

## Résumé

Vous pouvez trouver tout le code source de ce guide dans [ce dépôt GitHub](https://github.com/logicbaselabs/mcp-tutorial). Si cela vous a aidé d'une quelconque manière, envisagez de lui donner une étoile pour montrer votre soutien !

De plus, si vous avez trouvé le guide précieux, n'hésitez pas à le partager avec d'autres qui pourraient en bénéficier. J'apprécierais vraiment vos commentaires – mentionnez-moi sur X [@sumit\_analyzen](https://x.com/sumit_analyzen), regardez mes [tutoriels de codage](https://youtube.com/@logicBaseLabs), ou connectez-vous simplement avec moi sur [LinkedIn](https://www.linkedin.com/in/sumitanalyzen).