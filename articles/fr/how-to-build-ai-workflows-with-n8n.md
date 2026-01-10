---
title: Comment créer des workflows d'IA avec n8n
subtitle: ''
author: Soham Mehta
co_authors: []
series: null
date: '2025-10-13T16:03:12.156Z'
originalURL: https://freecodecamp.org/news/how-to-build-ai-workflows-with-n8n
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1760371342462/f8874220-238b-4819-a6f1-c35756b355bc.png
tags:
- name: AI
  slug: ai
- name: Workflow Automation
  slug: workflow-automation
- name: n8n
  slug: n8n
- name: n8n workflows
  slug: n8n-workflows
seo_title: Comment créer des workflows d'IA avec n8n
seo_desc: 'n8n is a visual, node-based automation platform that lets you automate
  tasks with drag-and-drop nodes. It’s popular for multi-step automations and AI chains
  thanks to built-in nodes for agents and app integrations.

  In this tutorial, you’ll build a sm...'
---

n8n est une plateforme d'automatisation visuelle basée sur des nœuds qui vous permet d'automatiser des tâches avec des nœuds en glisser-déposer. Elle est populaire pour les automatisations multi-étapes et les chaînes d'IA grâce à ses nœuds intégrés pour les agents et les intégrations d'applications.

Dans ce tutoriel, vous allez créer un petit agent de calendrier personnel qui écoute un message de chat, extrait les détails d'un événement et crée une entrée dans Google Calendar. En chemin, vous apprendrez comment configurer n8n, ajouter un nœud AI Agent et transmettre des données structurées entre les nœuds.

## **Table des matières**

1. [Prérequis](#heading-prerequis)
    
    * [Comment configurer votre compte n8n](#heading-comment-configurer-votre-compte-n8n)
        
2. [Comment créer un agent de calendrier personnel](#heading-comment-creer-un-agent-de-calendrier-personnel)
    
    * [Étape 1 : Configurer le déclencheur de chat](#heading-etape-1-configurer-le-declencheur-de-chat)
        
    * [Étape 2 : Configurer l'agent d'IA](#heading-etape-2-configurer-l-agent-d-ia)
        
    * [Étape 3 : Ajouter le nœud Google Calendar](#heading-etape-3-ajouter-le-noeud-google-calendar)
        
    * [Étape 4 : C'est l'heure de tester !](#heading-etape-4-c-est-l-heure-de-tester)
        
3. [Conclusion](#heading-conclusion)
    

## Prérequis

* Compte n8n – étapes de configuration ci-dessous.
    
* [Compte Google](https://support.google.com/accounts/answer/27441) – vous créerez des événements dans Google Calendar.
    

### Comment configurer votre compte n8n

Vous pouvez configurer n8n soit sur le cloud, soit localement.

Pour le configurer sur le cloud (l'option la plus simple), vous pouvez créer un compte d'essai gratuit sur le [site web de n8n](https://n8n.io/).

Si vous préférez l'auto-hébergement via npm, vous pouvez installer le [paquet npm n8n](https://www.npmjs.com/package/n8n) gratuit et l'exécuter sur votre localhost (voici les [étapes](https://docs.n8n.io/hosting/installation/npm/) pour cela).

Vous pouvez également l'auto-héberger via [Docker](https://www.docker.com/) et exécuter l'image n8n sur votre machine. Je vais vous guider à travers cette procédure dès maintenant.

Tout d'abord, téléchargez et installez l'application [Docker Desktop](https://www.docker.com/).

![Capture d'écran du site Docker montrant les liens de navigation et les boutons pour "Download Docker Desktop" et "Learn about Docker for AI" sous le titre "Develop Agents".](https://cdn.hashnode.com/res/hashnode/image/upload/v1760074532772/e3987b3e-403c-4a96-b7a7-ed3347acbca0.png align="center")

Ensuite, cliquez sur « Search Images » et sélectionnez l'image `n8nio/n8n` :

![Interface Docker Desktop montrant une recherche pour "n8nio" sous Images. Plusieurs images de conteneurs sont listées avec les nombres de téléchargements et d'étoiles. Les options pour Pull et Run l'image sélectionnée sont visibles.](https://cdn.hashnode.com/res/hashnode/image/upload/v1760074368306/eff04dd0-dcae-4c34-b5a1-f28c0db72373.png align="center")

Cliquez sur `run` sur l'image et définissez votre port localhost dans les options.

![Capture d'écran d'une fenêtre de navigateur montrant une page "Set up owner account" pour n8n, un outil d'automatisation de workflow. Le formulaire demande l'e-mail, le prénom, le nom et le mot de passe.](https://cdn.hashnode.com/res/hashnode/image/upload/v1760076583465/5f0bea8c-8d9d-4703-9561-1ede643c852e.png align="center")

Vous devriez maintenant pouvoir accéder à n8n sur votre localhost.

## Comment créer un agent de calendrier personnel

Passons maintenant à la partie amusante ! Nous allons construire un workflow qui écoute un message de chat, utilise un agent d'IA pour comprendre la demande de l'utilisateur et crée automatiquement un événement Google Calendar. Ce workflow simple met en avant les nouvelles capacités d'IA de n8n.

Voici le détail des étapes que nous allons suivre :

1. Ajouter un nœud Chat pour envoyer un message à l'agent.
    
2. Laisser l'agent d'IA analyser le message et extraire les détails clés (titre, lieu, horaires).
    
3. Créer un événement Google Calendar avec ces détails.
    

### Étape 1 : Configurer le déclencheur de chat

Chaque workflow commence par un déclencheur. C'est l'événement qui lance tout. Utilisez un déclencheur de chat qui écoute les nouveaux messages.

1. Visitez le tableau de bord à l'adresse `https://<VOTRE_NOM_UTILISATEUR>.app.n8n.cloud/home/workflows` et cliquez sur `Create Workflow`.
    
2. Cliquez sur « Add first step.. » et ajoutez `On chat message` comme déclencheur.
    
3. Dans le panneau des propriétés du nœud, activez `Make Chat Publicly Available` (cela fournira une URL que vous pourrez partager avec des amis pour réserver des événements sur votre calendrier).
    

![Workflow n8n où vous cliquez sur "On chat message" comme nœud de départ](https://cdn.hashnode.com/res/hashnode/image/upload/v1759649236134/c9ffc656-26b9-45a1-9c17-a6aa97a9e997.gif align="center")

### Étape 2 : Configurer l'agent d'IA

Ce nœud est le « cerveau » du workflow. Le nœud AI Agent peut comprendre le langage naturel, prendre des décisions et extraire des données structurées. Chaque agent dispose de 4 modules principaux : modèle, prompt, outils et sortie.

#### 1\. Configurer le modèle

Cliquez sur l'icône **+** après le nœud déclencheur et ajoutez le nœud `AI Agent`. L'agent d'IA a besoin d'un modèle pour alimenter son raisonnement. Cliquez sur + sous `Chat Model` et sélectionnez le nœud `OpenAI Chat Model`.

Sélectionnez ensuite `n8n free OpenAI API credits` comme identifiant pour le moment. À l'avenir, vous pourrez vous inscrire sur le site de la [Plateforme OpenAI](https://platform.openai.com/) et accéder à la section "API keys" pour créer une nouvelle clé secrète.

![Cliquez sur le nœud "AI agent" et sélectionnez le modèle de chat OpenAI](https://cdn.hashnode.com/res/hashnode/image/upload/v1759692503994/ac37a0bf-1d39-4fbe-9393-94fda82ea7a8.gif align="center")

#### 2\. Activer l'outil de date et heure

Un outil est un nœud connecté que l'agent peut appeler pendant l'exécution pour effectuer des actions (comme récupérer des données, formater des dates ou exécuter du code) plutôt que de se contenter de raisonner par texte. Nous utiliserons l'outil « Date & Time » pour convertir la date lisible par l'utilisateur en un [Unix Timestamp](https://help.clicksend.com/en/articles/44235-what-is-a-unix-timestamp) avant d'appeler l'API Google Calendar.

Voici les étapes pour activer cet outil :

1. Cliquez sur le bouton + sous l'outil AI Agent.
    
2. Recherchez l'outil Date & Time.
    
3. Définissez l'opération sur `Format a Date`.
    
4. Sélectionnez Date comme `Defined automatically by the model` (permet à l'agent de transmettre la date lui-même).
    
5. Sélectionnez Format comme `Unix Timestamp`.
    
6. Renommez le champ de sortie en `unixTime`.
    

![Workflow n8n où nous cliquons sur Tool sous AI agent et sélectionnons l'outil Date time et sélectionnons "Unix timestamp" pour le format](https://cdn.hashnode.com/res/hashnode/image/upload/v1759692990713/e59e5f3e-4898-4aeb-af3a-e7dffbb44615.gif align="center")

#### 3\. Ajouter le prompt de l'agent

Un prompt d'agent est l'ensemble d'instructions et de contexte que vous donnez à un agent d'IA qui définit son comportement, ses objectifs et la manière dont il doit interpréter ou répondre aux entrées de l'utilisateur.

1. Double-cliquez sur l'AI Agent pour modifier le prompt.
    
2. Sélectionnez Source for Prompt (User Message) comme `Define below`.
    
3. Copiez le prompt suivant dans le Prompt (User Message) :
    

```plaintext
## Aperçu
Vous êtes un agent qui aide à analyser le message de l'utilisateur pour identifier les détails suivants :
1. Le titre de la réunion
2. Le lieu de la réunion
3. Les heures Unix de début et de fin de la réunion.

Voici le message de l'utilisateur : {{ $json.chatInput }}

## Règles pour l'identification de l'heure de l'événement :
- La date et l'heure actuelles sont : {{ $now }}
- Résolvez les expressions relatives comme "demain", "vendredi prochain", "dans 2 heures" par rapport à maintenant.
- Si une durée est donnée (ex: "30 min" ou "2 heures"), calculez event_end à partir de event_start.
- Si seule une heure de début est donnée, la durée par défaut est de 60 minutes.

## Obtention des unix event_start et event_end
- Utilisez l'outil "Date & Time" pour convertir l'heure de début et de fin de l'événement calculée en unixtime.
```

![Interface utilisateur de l'éditeur de workflow n8n affichant un workflow nommé "My workflow 2". L'écran montre des nœuds incluant "When chat message received", "AI Agent", et des connexions vers OpenAI Chat Model et Date & Time.](https://cdn.hashnode.com/res/hashnode/image/upload/v1759693520456/df1a9a71-f790-42c3-9128-7289aaa35b22.gif align="center")

#### 4\. Configurer la sortie structurée

1. Activez l'interrupteur `Require Specific Output Format` dans l'AI Agent.
    
2. Cliquez sur + sous Output Parser et sélectionnez `Structured Output Parser`.
    
3. Copiez l'exemple JSON suivant que nous voulons extraire du message utilisateur :
    

```json
{
	"meeting_title": "Apprendre la géométrie",
	"meeting_location": "Bibliothèque",
    "event_start": 1759644763,
    "event_end": 1759644764
}
```

![Capture d'écran d'une interface d'agent d'IA avec une boîte de dialogue montrant des paramètres tels que la source du message utilisateur et les options pour activer un format de sortie spécifique.](https://cdn.hashnode.com/res/hashnode/image/upload/v1759693798967/bc8ba49e-09f3-43ed-9278-1cd4ada54560.gif align="center")

### Étape 3 : Ajouter le nœud Google Calendar

La dernière étape consiste à prendre les données structurées de l'agent d'IA et à créer l'événement de calendrier.

1. Cliquez sur l'icône **+** après le nœud AI Agent et recherchez le nœud **Google Calendar**.
    
2. Sélectionnez Resource comme `Event` et Operation comme `Create`.
    
3. Créez de nouveaux identifiants OAuth2 et connectez-vous à votre compte Google. Vous serez invité à vous connecter à Google et à accorder l'autorisation à n8n.
    

Maintenant, vous allez mapper les données de l'agent d'IA aux champs du nœud Google Calendar. C'est là que la magie opère.

1. Sélectionnez Start comme `{{ DateTime.fromSeconds($json.output.event_start).toFormat("yyyy-MM-dd HH:mm:ss") }}`
    
2. Sélectionnez End comme `{{ DateTime.fromSeconds($json.output.event_end).toFormat("yyyy-MM-dd HH:mm:ss") }}`
    
3. Sélectionnez Location comme `{{ $json.output.meeting_location }}`
    
4. Sélectionnez Summary comme `{{ $json.output.meeting_title }}`
    

![Interface d'automatisation de workflow affichant une intégration de message de chat avec un agent d'IA, utilisant des nœuds pour OpenAI Chat Model, Date & Time et Structured Output Parser. Ajout du nœud de création d'événement "Google Calendar"](https://cdn.hashnode.com/res/hashnode/image/upload/v1759696195078/a35054a9-5c3d-44e8-9a30-5539f3675525.gif align="center")

### Étape 4 : C'est l'heure de tester !

C'est tout ! Vous avez maintenant un workflow alimenté par l'IA qui crée des événements sur votre calendrier. Vous pouvez activer votre workflow à l'aide de l'interrupteur en haut de l'écran. Cliquez sur « Open Chat » pour lancer une conversation et envoyer un message. Vous verrez l'ensemble du workflow en action ainsi que l'entrée et la sortie de chaque nœud.

Vous pouvez également cliquer sur le nœud Google Calendar pour trouver la colonne `htmlLink` qui fournira une URL où vous pourrez voir votre événement créé.

![Une configuration d'automatisation de workflow dans n8n montrant un processus où un message de chat déclenche un agent d'IA, qui interagit avec le modèle de chat OpenAI et un analyseur de sortie structuré pour créer un événement.](https://cdn.hashnode.com/res/hashnode/image/upload/v1759696671635/a98acab0-2fa6-4c86-976e-996d5af00c59.gif align="center")

## Conclusion

Dans ce tutoriel, vous avez appris à construire un workflow d'automatisation simple piloté par l'IA dans l'interface visuelle de n8n. La véritable puissance réside dans la création de workflows d'IA personnalisés en adaptant facilement votre propre agent, prompt et outils à vos besoins exacts.

L'écosystème de n8n prospère grâce aux [modèles de la communauté](https://n8n.io/workflows/), vous permettant d'utiliser des milliers de solutions pré-construites ou de partager vos propres créations. Si ce guide vous a aidé, essayez d'étendre le workflow par vous-même et explorez la documentation de n8n pour découvrir plus de nœuds. Bon codage !