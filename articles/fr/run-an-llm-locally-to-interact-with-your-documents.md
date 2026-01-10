---
title: Comment exécuter un LLM localement pour interagir avec vos documents
subtitle: ''
author: Zoe Isabel Senón
date: '2026-01-10T00:38:09.929Z'
originalURL: https://acceleratingutopia.com/how-to-local-llm-private-docs/
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1767976983680/2e3671cd-4280-4a32-9508-47fe9c06ab22.png
tags:
- name: 'LLM''s '
  slug: llms
- name: ollama
  slug: ollama
- name: AI
  slug: ai
seo_title: Comment exécuter un LLM localement pour interagir avec vos documents
seo_desc: Learn how to run a LLM like ChatGPT locally to interact with your personal
  or business documents privately.
---

La plupart des outils d'IA vous obligent à envoyer vos prompts et vos fichiers à des serveurs tiers. C'est inacceptable si vos données incluent des journaux intimes, des notes de recherche ou des documents professionnels sensibles (contrats, présentations de conseil d'administration, fichiers RH, données financières). La bonne nouvelle : vous pouvez exécuter des LLM performants localement (sur un ordinateur portable ou votre propre serveur) et interroger vos documents sans envoyer un seul octet dans le cloud.

Dans ce tutoriel, vous apprendrez à exécuter un LLM de manière locale et privée, afin de pouvoir rechercher et discuter avec des journaux et des documents professionnels sensibles sur votre propre machine. Nous installerons **Ollama** et **OpenWebUI**, choisirons un modèle adapté à votre matériel, activerons la recherche de documents privés avec **nomic-embed-text**, et créerons une base de connaissances locale pour que tout reste sur le disque.

## Table des matières

* [Prérequis](#heading-prerequis)
    
* [Installation](#heading-installation)
    
* [Paramètres pour les documents](#heading-parametres-pour-les-documents)
    
* [Comment télécharger vos documents](#heading-comment-telecharger-vos-documents)
    
    * [(Optionnel) Ajouter une instruction système](#heading-optionnel-ajouter-une-instruction-systeme)
        
* [Comment exécuter votre LLM localement](#heading-comment-executer-votre-llm-localement)
    
* [Conclusion](#heading-conclusion)
    

## Prérequis

Vous aurez besoin d'un terminal (tous les systèmes — Windows, Mac, Linux — en incluent un, et vous pouvez trouver le vôtre avec une recherche rapide), et soit de Python et pip, soit de Docker, selon votre méthode d'installation préférée pour OpenWebUI.

## Installation

Vous aurez besoin d' [**Ollama**](https://ollama.com/download) et d' [**OpenWebUI**](https://docs.openwebui.com/getting-started/quick-start/). Ollama exécute les modèles, tandis qu'OpenWebUI vous offre une interface de navigation pour interagir avec votre LLM local, comme vous le feriez avec ChatGPT.

### Étape 1 : Installer Ollama

Téléchargez et installez Ollama depuis son [site officiel](https://ollama.com/download). Des installateurs sont disponibles pour **macOS**, **Linux** et **Windows**. Une fois installé, vérifiez qu'il fonctionne en ouvrant un terminal et en exécutant :

```bash
ollama list
```

Si Ollama est en cours d'exécution, cela renverra une liste de modèles actifs (ou une liste vide).

### Étape 2 : Installer OpenWebUI

Vous pouvez installer OpenWebUI soit avec Python (pip), soit avec Docker. Ici, nous allons montrer comment le faire avec pip, mais vous pouvez trouver les instructions pour Docker sur la [documentation officielle d'openwebui](https://docs.openwebui.com/getting-started/quick-start/).

Installez OpenWebUI avec la commande suivante :

```bash
pip install open-webui
```

Cela fonctionne sur **macOS, Linux et Windows**, tant que vous avez Python ≥ 3.9 installé.

Ensuite, démarrez le serveur :

```bash
open-webui serve
```

Puis ouvrez votre navigateur et allez sur :

```bash
http://localhost:8080
```

### Étape 3 : Installer un modèle

Choisissez un modèle dans la [liste des modèles Ollama](https://ollama.com/library) et téléchargez-le localement en copiant la commande fournie.

![Capture d'écran de la page de téléchargement du modèle avec une flèche pointant vers la case en haut à droite qui inclut la commande d'installation avec un raccourci pour copier-coller](https://cdn.hashnode.com/res/hashnode/image/upload/v1758302463715/fbbaabf7-6612-460c-8e09-1c5143eacc1a.png align="center")

Par exemple :

```bash
ollama pull gemma3:4b
```

Si vous n'êtes pas sûr du modèle que votre machine peut supporter, demandez à une IA d'en recommander un en fonction de votre matériel. Les modèles plus petits (1B–4B) sont plus sûrs sur les ordinateurs portables.

Je recommanderais Gemma3 comme point de départ (vous pouvez télécharger plusieurs modèles et basculer facilement de l'un à l'autre). Choisissez le **nombre de paramètres** à la fin (":4b", ":1b", etc.) en vous basant sur ce guide :

* Niveau 1 (petits ordinateurs portables ou ordinateurs peu puissants) : RAM ≤ 8 Go ou pas de GPU → 1B–2B.
    
* Niveau 2 : RAM 16 Go, GPU faible → 2B–4B.
    
* Niveau 3 : RAM ≥ 16 Go, 6–8 Go de VRAM → 4B–9B.
    
* Niveau 4 : RAM ≥ 32 Go, 12 Go+ de VRAM → 12B+.
    

Une fois que vous avez installé Ollama et le modèle souhaité, confirmez qu'ils sont actifs en exécutant `ollama list` dans le terminal :

![Image montrant le résultat de l'exécution de la commande "ollama list" (montre la liste des modèles téléchargés, dans ce cas "gemma3:1b")](https://cdn.hashnode.com/res/hashnode/image/upload/v1767465401368/d1b8abc0-7aaa-4c2f-ad4c-30ae908f9e8b.png align="left")

Lancez WebOpenUI pour démarrer l'interface du navigateur avec :

```bash
open-webui serve
```

Puis rendez-vous sur [http://localhost:8080/](http://localhost:8080/). Vous êtes maintenant prêt à commencer à utiliser votre LLM localement !

**Note** : il vous demandera des identifiants de connexion, mais ceux-ci n'ont pas vraiment d'importance si vous avez l'intention de l'utiliser uniquement localement.

![Capture d'écran de l'interface d'une instance en cours d'exécution d'OpenWebUI, montrant la page d'accueil, qui comprend une zone de saisie de texte au centre avec l'espace réservé "comment puis-je vous aider aujourd'hui ?", et un panneau latéral avec la liste des discussions précédentes, et des liens vers "recherche", "notes", "espace de travail" et "nouvelle discussion", ainsi qu'un bouton de réglage. En haut, il y a un sélecteur de modèle qui a actuellement "gemma3:1b" sélectionné comme modèle à utiliser.](https://cdn.hashnode.com/res/hashnode/image/upload/v1758302486263/14d93c7e-415c-463f-82da-fc515f28663a.png align="center")

## Paramètres pour les documents

Nous allons maintenant configurer tout ce dont nous avons besoin pour interagir avec nos documents locaux. Tout d'abord, nous devons installer le modèle « [**nomic-embed-text**](https://ollama.com/library/nomic-embed-text) » pour traiter nos documents. Installez-le avec :

```bash
ollama pull nomic-embed-text
```

**Note** : Si vous vous demandez pourquoi nous avons besoin d'un autre modèle (nomic-embed-text) en plus de notre modèle principal :

* Le modèle d'incorporation (`nomic-embed-text`) transforme chaque segment de texte de vos documents en un vecteur numérique afin qu'OpenWebUI puisse trouver rapidement des segments sémantiquement similaires lorsque vous posez une question.
    
* Le modèle de chat (par exemple `gemma3:1b`) reçoit votre question ainsi que ces segments récupérés comme contexte et génère la réponse en langage naturel.
    

Ensuite, vous devriez activer la fonction « **mémoire** » si vous voulez que le LLM se souvienne du contexte de vos conversations passées dans les futures.

Téléchargez la fonction de mémoire adaptative [**ici**](https://openwebui.com/f/alexgrama7/adaptive_memory_v2). Les fonctions sont comme des plug-ins.

![Capture d'écran montrant la page (site web) pour la fonction "adaptive memory v3". Elle montre un gros bouton "get", qui, lorsqu'on clique dessus, ouvre une vue contextuelle nommée "Open WebUI URL" avec l'espace réservé actuel étant "http:localhost:8080" (le port WebUI par défaut) et un bouton pour "importer vers WebUI" et un autre en dessous pour "Télécharger en tant qu'exportation JSON" au cas où le premier ne fonctionnerait pas)](https://cdn.hashnode.com/res/hashnode/image/upload/v1758302505221/b247316c-0863-410a-84c9-abc084a6631f.png align="center")

Nous allons maintenant mettre à jour nos paramètres pour activer ces fonctionnalités. Cliquez sur votre nom dans le coin inférieur gauche, puis sur « Paramètres ».

![Capture d'écran montrant le panneau de menu qui apparaît en cliquant sur l'icône ronde en bas à gauche avec l'initiale et le nom de l'utilisateur, montrant une liste d'options, commençant par "Paramètres" et suivie de "Discussions archivées", "Playground", "Panneau d'administration" et "Se déconnecter"](https://cdn.hashnode.com/res/hashnode/image/upload/v1758302517617/e73983f3-0e36-4c0a-a61c-96a0a42f1fab.png align="left")

Cliquez sur le premier, puis allez dans « Personnalisation » et activez « Mémoire ».

![Capture d'écran du panneau des paramètres d'OpenWebUI avec l'onglet Personnalisation ouvert et le bouton Mémoire activé pour enregistrer le contexte des conversations passées.](https://cdn.hashnode.com/res/hashnode/image/upload/v1752935284007/aa42c76b-f38c-4485-b442-8844c6c3a544.png align="center")

Nous allons maintenant accéder à l'autre panneau de paramètres (« Panneau d'administration »). Cliquez à nouveau sur votre nom dans le coin inférieur gauche et allez dans **Panneau d'administration → Paramètres → Documents**.

![Capture d'écran de la page Administration d'OpenWebUI → Paramètres → Documents, montrant un champ de saisie de texte appelé "Taille du segment" actuellement réglé sur 512](https://cdn.hashnode.com/res/hashnode/image/upload/v1758302570583/96784c55-484b-4c66-bdc4-ce23a7e901a1.png align="center")

Dans cette section (Panneau d'administration → Paramètres → Documents), trouvez la section « **Embedding** », allez dans « **Embedding Model Engine** » et choisissez Ollama (trouvez le menu déroulant à droite). Laissez la clé API vide.

Maintenant, sous « **Embedding Model** », écrivez `nomic-embed-text`. Allez ensuite dans « Retrieval » → activez « Full Context Mode ».

### Paramètres de découpage (chunking)

Vous devez également définir la **taille des segments** (chunk size) et le **chevauchement** (overlap). OpenWebUI divise les documents en segments plus petits avant de les indexer, car les modèles ne peuvent pas incorporer ou récupérer des textes très longs d'un seul tenant.

Une bonne valeur par défaut est de **128 à 512 tokens par segment**, avec un **chevauchement de 10 à 20 %**. Les segments plus grands préservent davantage de contexte mais sont plus lents et plus gourmands en mémoire, tandis que les segments plus petits sont plus rapides mais peuvent perdre le sens global. Le chevauchement aide à éviter que le contexte important ne soit coupé lors de la division du texte.

Voici un tableau indicatif, mais je recommande d'obtenir les valeurs recommandées pour votre cas d'utilisation et votre configuration spécifiques en les partageant (y compris le modèle de GPU ou d'ordinateur portable, le stockage, la RAM, etc.) avec un LLM comme ChatGPT ou Claude, **car changer les valeurs de découpage/chevauchement plus tard nécessite de retélécharger les documents.**

### Segments/chevauchement suggérés par niveau

| **Niveau / scénario** | **Matériel typique** | **Taille du segment (tokens)** | **Chevauchement (%)** | **Notes** |
| --- | --- | --- | --- | --- |
| Niveau 1 – contraint | ≤8 Go RAM, pas de GPU ou GPU faible | 128–256 | 10–15 | Priorise la vitesse et la faible utilisation de la mémoire. |
| Niveau 2 – moyen | 16 Go RAM, GPU modeste ou CPU puissant | 256–384 | 15–20 | Équilibre entre contexte et performance. |
| Niveau 3 – confortable | ≥16 Go RAM, 6–8 Go VRAM | 384–512 | 15–20 | Plus de sémantique par segment, reste pratique. |
| PDF techniques denses / docs juridiques | Tous, mais surtout Niveaux 2–3 | 384–512 | 15–20 | Garde les paragraphes et les arguments intacts. |
| Notes courtes, tickets, e-mails | Tous | 128–256 | 10–15 | Les éléments sont petits, les grands segments ne sont pas nécessaires. |
| Requêtes très longues, besoin de nombreux segments récupérés | Tous avec une fenêtre de contexte plus large | 256–384 | 10–15 | Les segments plus petits permettent d'insérer plus de morceaux dans le contexte. |

## Comment télécharger vos documents

Maintenant, l'étape finale : le téléchargement de vos documents ! Allez dans « Espace de travail » dans le panneau latéral, puis « Connaissance », et créez une nouvelle collection (base de données). Vous pouvez commencer à télécharger des fichiers ici.

![Capture d'écran de la page "Espace de travail" (après avoir cliqué sur "espace de travail" dans le panneau latéral) mettant en évidence le bouton "Espace de travail" sur le côté gauche, l'onglet "Connaissance" étant sélectionné parmi les options en haut de cette page d'Espace de travail, puis "Télécharger des fichiers" qui est la première option affichée sur la liste après avoir cliqué sur le bouton "+" (plus) à droite de la saisie de texte avec l'espace réservé qui dit "Rechercher dans la collection".](https://cdn.hashnode.com/res/hashnode/image/upload/v1758302584485/63c04901-f5d3-4ac7-bab5-b23362fb83cb.png align="center")

<div data-node-type="callout">
<div data-node-type="callout-emoji">⚠️</div>
<div data-node-type="callout-text">Assurez-vous de vérifier s'il y a des erreurs pendant le téléchargement. Malheureusement, elles ne s'affichent que sous forme de fenêtres contextuelles temporaires. Certaines erreurs peuvent être dues au format de vos fichiers, alors assurez-vous de vérifier la console pour d'autres journaux d'erreurs.</div>
</div>

Ensuite, dans « Espace de travail », passez à l'onglet « Modèles » et créez un nouveau modèle personnalisé. Créer un modèle personnalisé et y attacher votre base de connaissances indique à OpenWebUI de rechercher automatiquement dans votre collection de documents et d'inclure les segments les plus pertinents comme contexte chaque fois que vous posez une question.

![Capture d'écran de la page "Espace de travail" (après avoir cliqué sur "espace de travail" dans le panneau latéral), mettant en évidence le premier onglet/option dans le menu supérieur nommé "Modèles", qui, lorsqu'on clique dessus, affiche la liste des modèles personnalisés et une option pour en créer de nouveaux (dans ce cas, l'utilisateur en a créé un appelé "Gemma-custom-knowledge")](https://cdn.hashnode.com/res/hashnode/image/upload/v1758302593445/b5316a4a-8c8a-4348-a31e-1c10fe0e1abb.png align="center")

Ici, assurez-vous de sélectionner votre modèle (dans mon cas « gemma3:1b ») et d'attacher votre base de connaissances.

![Capture d'écran de la page de création de modèle, mettant en évidence les options sélectionnables sous le champ "Modèle de base (de)", mettant spécifiquement en évidence "gemma3:1b" ou le modèle de choix, sous l'option sélectionnée par défaut "sélectionner un modèle de base". Le deuxième élément mis en évidence en rouge est l'autre champ ci-dessous intitulé "Connaissance", avec un bouton appelé "Sélectionner la connaissance". Il y a 2 autres éléments mis en évidence en jaune (indiquant une priorité plus faible) : le premier est "Paramètres du modèle" qui comprend un champ de saisie "instruction système" juste en dessous, et l'autre est "Filtres" qui comprend plusieurs options sélectionnables en fonction des différents plugins ou "fonctions" installés.](https://cdn.hashnode.com/res/hashnode/image/upload/v1758302604758/df0c7948-bb9b-4615-8f09-21faaa64fdde.png align="center")

![Capture d'écran montrant les options disponibles après avoir cliqué sur "Sélectionner la connaissance" sous "Connaissance", mettant en évidence l'option qui dit "COLLECTION" en vert suivie du titre "Test-knowledge-base" (exemple de titre choisi par l'auteur) et de la description ajoutée par l'auteur ("ajout de mes documents")](https://cdn.hashnode.com/res/hashnode/image/upload/v1758302612285/8247d1c3-5f84-42de-9861-34416d0b7f10.png align="center")

### (Optionnel) Ajouter une instruction système

Lors de la création de votre modèle personnalisé dans **Espace de travail → Modèles**, vous pouvez définir une **instruction système** (system prompt) que le modèle utilisera pour le contexte tout au long de vos conversations.

Voici quelques exemples d'informations que vous pourriez vouloir ajouter :

* contexte sur vous-même *("Je suis un étudiant de 20 ans en bio-ingénierie intéressé par...")*
    
* votre style de communication préféré *("sans fioritures", "sois direct", "sois analytique"...)*
    
* contexte sur la structure de vos données
    

**Exemple d'instruction système :**

> Tu es un assistant réfléchi et analytique qui m'aide à explorer des schémas et des idées dans mes journaux personnels. Sois direct, évite les spéculations et distingue clairement les faits issus des documents de l'interprétation.

Cette instruction s'appliquera automatiquement à chaque discussion utilisant ce modèle personnalisé, aidant à garder des réponses cohérentes et alignées avec vos objectifs.

## Comment exécuter votre LLM localement

Ouvrez maintenant une nouvelle discussion et assurez-vous de sélectionner votre modèle personnalisé :

![Capture d'écran montrant la page "Nouvelle discussion" après avoir cliqué sur le symbole/bouton "+" (plus) à côté du nom du modèle personnalisé. Elle montre les options affichées lors du clic sur le champ de saisie qui indique "Rechercher un modèle" comme espace réservé, et l'option mise en évidence à l'intérieur est le nom du modèle personnalisé (dans ce cas, l'auteur a choisi le nom "Gemma-custom-knowledge")](https://cdn.hashnode.com/res/hashnode/image/upload/v1758302621012/241f461c-acf6-41ae-b68d-ad187790aef4.png align="center")

Vous êtes maintenant prêt à discuter avec vos propres documents dans un environnement local privé !

<div data-node-type="callout">
<div data-node-type="callout-emoji">⚠️</div>
<div data-node-type="callout-text"><strong>Note</strong> : Par défaut, l'interface/navigateur arrêtera de diffuser la réponse après cinq minutes, même s'il continuera à traiter votre requête en arrière-plan. Cela signifie que si votre requête prend plus de cinq minutes à être traitée, elle ne sera pas affichée sur le navigateur. Vous pouvez recharger la page et cliquer sur « continuer la réponse » pour obtenir le dernier résultat.</div>
</div>

<div data-node-type="callout">
<div data-node-type="callout-emoji">💡</div>
<div data-node-type="callout-text">Je recommande d'installer la fonction (plugin) <a target="_self" rel="noopener noreferrer nofollow" href="https://openwebui.com/f/alexgrama7/enhanced_context_tracker_v4" style="pointer-events: none">Enhanced Context Tracker</a> pour avoir plus de visibilité sur la progression de votre requête.</div>
</div>

## Conclusion

Vous disposez maintenant d'une pile LLM privée (**Ollama** pour les modèles, **OpenWebUI** pour l'interface utilisateur et **nomic-embed-text** pour les incorporations) reliée à votre base de connaissances sur disque. Vos journaux et documents professionnels restent locaux ; rien n'est envoyé à des tiers. Les réglages principaux sont simples : choisissez un modèle adapté à votre matériel, activez la mémoire et la récupération du contexte complet, utilisez un découpage/chevauchement raisonnable, et vérifiez la console lorsque les exécutions stagnent.

Si vous avez besoin de plus de puissance, déployez la même configuration sur votre propre serveur tout en conservant les garanties de confidentialité. À partir de là, itérez sur le choix du modèle, le découpage et les instructions, et ajoutez les fonctions optionnelles si vous avez besoin d'une visibilité plus profonde lors de travaux longs.