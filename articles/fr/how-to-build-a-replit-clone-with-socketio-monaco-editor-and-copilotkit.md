---
title: Comment construire un clone de Replit avec Socket.io, Monaco Editor et Copilotkit
subtitle: ''
author: Prankur Pandey
co_authors: []
series: null
date: '2025-02-20T23:16:04.811Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-replit-clone-with-socketio-monaco-editor-and-copilotkit
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1740064335866/a058fbf3-2d89-4e95-9d3b-07224f3985be.png
tags:
- name: AI
  slug: ai
- name: full stack
  slug: full-stack
seo_title: Comment construire un clone de Replit avec Socket.io, Monaco Editor et
  Copilotkit
seo_desc: I’ve been coding for about a decade now. And over the years, I’ve tried
  my fair share of development tools—especially IDEs like Sublime Text, Atom, and
  even NetBeans back in my college days. But when VS Code came along, it completely
  changed the game...
---

Je code depuis environ une décennie. Au fil des ans, j'ai essayé ma juste part d'outils de développement, en particulier des IDE comme Sublime Text, Atom, et même NetBeans à l'époque de mes études. Mais quand VS Code est arrivé, cela a complètement changé la donne pour moi. Il est léger, rapide et regorge de fonctionnalités qui rendent la vie plus facile en tant que développeur. Il est rapidement devenu mon outil préféré.

Avec toutes les avancées récentes en matière d'IA, je voulais construire quelque chose qui ne soit pas seulement amusant mais aussi une expérience d'apprentissage significative. C'est ainsi que ce projet est né : un simple clone inspiré de Replit pour le web. Il combine l'IA pour générer du code, vous permet d'exécuter des fichiers React et affiche la sortie de manière transparente, tout comme Replit. En plus de cela, vous pouvez modifier des fichiers et sauvegarder votre travail en temps réel, afin que rien ne soit jamais perdu.

### **Ce que nous allons couvrir :**

* [Prérequis et outils](#heading-prerequis-et-outils)

* [Ce que nous allons faire ici :](#heading-ce-que-nous-allons-faire-ici)

* [Comment fonctionne l'application ?](#heading-comment-fonctionne-lapplication)

* [Comment configurer vos outils](#heading-comment-configurer-vos-outils)

* [Structure et fonctionnalités de l'application](#heading-structure-et-fonctionnalites-de-lapplication)

* [Comment construire le backend](#heading-comment-construire-le-backend)

* [Comment construire le frontend](#heading-comment-construire-le-frontend)

* [Jouer avec le clone de Replit](#heading-jouer-avec-le-clone-de-replit)

* [Conclusion](#heading-conclusion)

## Prérequis et outils

Dans ce tutoriel, nous allons construire un clone de Replit alimenté par l'IA, un IDE basé sur le web. Cet IDE vous permettra de générer des fichiers de code React, de les modifier dans un environnement similaire à VSCode, de prévisualiser la sortie finale et de sauvegarder le code en temps réel. Il prendra également en charge les opérations CRUD sur les fichiers générés.

Pour ce projet, j'utiliserai certains outils que j'ai utilisés dans le passé, y compris ceux de mon projet [SQL Query Data Extractor](https://www.freecodecamp.org/news/talk-to-databases-using-ai-build-a-sql-query-data-extractor). Voici les outils et technologies que nous allons utiliser :

### Base de données

La base de données est l'épine dorsale de toute application, elle stocke les données et les sert selon les besoins. Pour ce projet, j'utiliserai mon préféré de toujours, MongoDB Atlas.

J'ai choisi MongoDB Atlas car il s'intègre parfaitement avec Next.js, et comme il s'agit d'une base de données basée sur le cloud, je n'ai pas besoin de l'héberger manuellement, ce qui en fait une solution plug-and-play. La réalisation d'opérations CRUD avec MongoDB Atlas est simple et efficace.

### Éditeur de code

L'éditeur de code est le cœur de ce projet, car il alimente l'expérience de l'IDE. Pour cela, j'utiliserai le légendaire Monaco Editor, le même éditeur qui alimente VSCode. Monaco Editor gère les fichiers sans effort et prend en charge une large gamme de types de fichiers. Dans ce projet, il permettra aux utilisateurs de visualiser et de modifier les fichiers de code.

### Prévisualisation du code

Une fois que nous avons généré et modifié le code dans le Monaco Editor, nous aurons besoin d'un moyen de prévisualiser sa sortie. Pour cela, j'utiliserai Sandpack de CodeSandbox, un outil gratuit et puissant pour les prévisualisations de code en direct.

Sandpack prend en charge divers frameworks et types de fichiers, que vous travailliez avec des fichiers HTML/CSS statiques ou des frameworks comme React. Il affiche les fichiers et leur sortie en temps réel de manière transparente.

### Agent IA

L'agent IA sera responsable de la génération de code en utilisant le traitement du langage naturel (NLP). Agissant comme un pont entre vos idées et le code, il prendra les invites des utilisateurs et les traduira en fichiers de code fonctionnels.

Pour cela, j'utiliserai CopilotKit, mon outil gratuit et open-source préféré pour la génération de code alimentée par l'IA. CopilotKit prendra vos idées et créera les fichiers de code correspondants en fonction de votre entrée.

### Modèle IA

L'agent IA s'appuie sur un modèle IA sous-jacent pour traiter les entrées des utilisateurs et générer du code. Pour ce projet, j'utiliserai GroqAI, une plateforme flexible et fiable qui prend en charge divers modèles IA populaires. La polyvalence de GroqAI en fait un choix parfait pour les exigences de ce projet.

### **Next.js**

Pour construire une application web robuste qui combine les fonctionnalités frontend et backend, j'utiliserai Next.js. C'est un excellent framework pour créer des applications évolutives, offrant un rendu côté serveur et d'autres fonctionnalités puissantes idéales pour ce projet.

### **Déploiement**

Pour le déploiement, vous pouvez choisir n'importe quel service. Je préfère Vercel, car il s'intègre parfaitement avec Next.js et est gratuit pour les projets de loisirs.

En combinant ces outils, vous construirez une application puissante et conviviale qui produit le code sans effort et fournit une prévisualisation en direct comme le fait Replit.

## **Ce que nous allons faire ici**

Dans ce tutoriel, vous suivrez ces étapes pour construire notre application :

**Étape 1 – Configurer la base de données :**

Configurer une base de données soit localement soit sur le cloud. Pour une intégration transparente, utilisez un outil de base de données en ligne qui prend en charge l'accès aux données et l'extraction via des API REST.

**Étape 2 – Obtenir les clés API cloud :**

Récupérez les clés API nécessaires pour votre modèle IA afin de permettre une intégration fluide et sécurisée.

**Étape 3 – Construire l'application web :**

Développez une application web et configurez le backend pour intégrer CopilotKit. Assurez-vous qu'il est correctement configuré pour une fonctionnalité efficace.

**Étape 4 – Former CopilotKit avec votre base de données :**

Fournissez vos données de base de données à CopilotKit afin qu'il puisse comprendre et utiliser les informations pour le traitement du langage naturel.

**Étape 5 – Intégrer l'interface de chat CopilotKit :**

Intégrez l'interface de chat CopilotKit dans votre application et configurez-la pour qu'elle fonctionne de manière transparente avec le flux de travail de votre application.

**Étape 6 – Tester localement :**

Exécutez l'application sur votre machine locale, testez chaque fonctionnalité de manière approfondie pour identifier et résoudre tout problème.

**Étape 7 – Déployer l'application :**

Une fois les tests terminés et l'application fonctionnant comme prévu, déployez-la sur une plateforme d'hébergement pour une utilisation publique.

## **Comment fonctionne l'application ?**

![explication-de-lapplication-en-fonctionnement](https://cdn.hashnode.com/res/hashnode/image/upload/v1739811798424/af2b925d-95d9-422c-8318-fe0d9d37962b.png align="center")

Ce projet est une expérience amusante et une étape vers mon objectif à long terme de construire quelque chose autour des éditeurs de code, particulièrement inspiré par VSCode.

La vraie magie opère avec CopilotKit. Dès que vous entrez une idée dans CopilotKit, il utilise des invites système prédéfinies qui s'adaptent aux exigences de votre projet. Ces invites permettent à CopilotKit d'interpréter les instructions en anglais simple et de les transformer en sorties significatives. Dans ce tutoriel, je vais vous montrer comment configurer ces invites système efficacement pour maximiser les résultats.

Par exemple, si vous entrez l'idée *"construire une simple application React"*, CopilotKit transmet cette idée au modèle IA intégré. Le modèle IA, travaillant en coordination avec les invites système de CopilotKit, génère les fichiers de code nécessaires en fonction de votre entrée.

Les fichiers générés sont ensuite affichés dans l'Explorateur de fichiers sur le côté gauche de l'écran. Vous pouvez facilement parcourir les fichiers créés par CopilotKit.

Pour prévisualiser le code, il suffit de cliquer sur un fichier comme `App.js`. Le code du fichier se chargera dans le Monaco Editor à gauche, tandis que la prévisualisation Sandpack à droite rendra une sortie en temps réel du fichier.

Vous pouvez maintenant expérimenter avec les fichiers : modifier le code, changer les couleurs, les polices ou le texte, et même écrire votre propre logique, tout comme avec des fichiers HTML, CSS ou React réguliers. Toutes les modifications que vous apportez seront sauvegardées en temps réel dans la base de données. Ainsi, même si vous fermez accidentellement le projet, votre progression sera intacte. Il suffit de rafraîchir la page, et votre code sera là où vous l'avez laissé.

## **Comment configurer vos outils**

Maintenant, nous allons passer en revue tout ce dont vous avez besoin pour configurer le projet.

### **Installer Next.js et les dépendances :**

Tout d'abord, vous devrez créer une application Next.js. Allez dans le terminal et exécutez la commande suivante :

```javascript
npx create-next-app@latest my-next-app
```

Remplacez `my-next-app` par le nom de votre projet souhaité et utilisez TypeScript.

Accédez au dossier du projet :

```javascript
cd my-next-app
```

Démarrez le serveur de développement :

```javascript
npm run dev
```

Ouvrez votre navigateur et accédez à [`http://localhost:3000`](http://localhost:3000/) pour voir votre application Next.js en action.

### **Installer CopilotKit et les dépendances**

Accédez au dossier racine du projet dans le terminal et exécutez la commande suivante. Cela installera toutes les dépendances nécessaires pour CopilotKit ainsi que d'autres packages essentiels, tels que dotenv, groq-sdk, sandpack, Monaco Editor, Lucide React, Socket et Mongoose.

```javascript
npm install @copilotkit/react-ui @copilotkit/react-core
npm install dotenv
npm install groq-sdk
npm install @codesandbox/sandpack-react
npm install @monaco-editor/react
npm install lucide-react
npm install mongoose
npm install socket.io
npm install socket.io-client
```

* **CopilotKit** : Cette dépendance gère toutes les opérations et configurations liées à CopilotKit.

* **Dotenv** : Utilisé pour gérer les variables d'environnement et garder les clés sensibles sécurisées dans le projet.

* **GroqSDK** : Facilite l'accès à divers modèles LLM via une seule clé API.

* **CodeSandbox Sandpack (React)** : Fournit la capacité d'afficher des aperçus en temps réel du code.

* **Monaco Editor** : Alimente l'environnement de type VSCode, permettant l'édition de code en temps réel.

* **Lucide React** : Une bibliothèque d'icônes utilisée pour afficher des icônes pour les fichiers et dossiers.

* **Mongoose** : Gère les schémas MongoDB pour stocker et récupérer des données de la base de données.

* **socket.io** : Un outil très puissant pour la synchronisation de données en temps réel entre le client et le serveur.

* **socket.io client** : Package client socket.io supplémentaire pour la communication de données.

### **Configurer le LLM pour l'action :**

Cette étape est cruciale pour le projet, car elle implique la configuration du LLM (Large Language Model) pour convertir les requêtes en langage naturel (anglais simple) en code fonctionnel React.

Il existe de nombreux LLM disponibles, chacun avec ses propres forces. Certains sont gratuits, tandis que d'autres sont payants, ce qui rend le processus de sélection pour ce projet un peu difficile.

Après une expérimentation approfondie, j'ai choisi l'adaptateur Groq parce que :

* Il intègre plusieurs LLM dans une seule plateforme.

* Il offre un accès via une clé API unifiée.

* Il est entièrement compatible avec CopilotKit.

#### **Comment configurer Groq Cloud**

Pour commencer avec Groq Cloud, visitez son site web et connectez-vous si vous avez déjà un compte ou créez un nouveau compte si vous êtes nouveau. Une fois connecté, accédez au tableau de bord Groq.

Voici la page d'accueil de Groq cloud :

![page d'accueil de groq cloud](https://cdn.hashnode.com/res/hashnode/image/upload/v1736352733541/92012af5-b3c4-4277-a50f-834c1900a2de.png align="left")

Une fois connecté, une nouvelle page s'ouvrira qui ressemblera à ceci :

![page du tableau de bord de groq cloud](https://cdn.hashnode.com/res/hashnode/image/upload/v1736353229314/67313c60-47b8-4f23-b3c0-e46fcdd5201a.png align="left")

Comme vous pouvez le voir, la barre latérale contient un lien Clés API. Cliquez dessus, et il ouvrira une nouvelle page comme montré dans l'image ci-dessous. Vous pouvez également sélectionner n'importe quel LLM de votre choix qui est donné en haut à droite avant l'option de visualisation du code.

![section api groqcloud](https://cdn.hashnode.com/res/hashnode/image/upload/v1736353347970/3406fa54-ddc2-4a00-8b27-22536486fc64.png align="left")

Ici, cliquez sur le bouton Créer une clé API, cela ouvrira une fenêtre contextuelle comme vous voyez ci-dessous. Entrez simplement le nom de votre clé API et cliquez sur Soumettre pour créer une nouvelle clé API pour vous. Ensuite, copiez cette clé API et collez-la dans votre fichier `.env`.

![page de création de clé api groq cloud](https://cdn.hashnode.com/res/hashnode/image/upload/v1736353563741/cd1a185a-2c77-470a-a5ce-eca564cf524a.png align="left")

Pour permettre un accès transparent à divers LLM sur Groq Cloud, générez une clé API en allant dans la section Clés API de Groq. Créez une nouvelle clé API spécifiquement pour le LLM, en veillant à ce qu'elle soit correctement configurée.

Avec le LLM configuré et tous les composants prêts, vous êtes maintenant prêt à construire le projet.

### Comment configurer la base de données

### **Étape 1 : Créer un compte MongoDB Atlas**

1. Allez sur le [site web de MongoDB Atlas](https://www.mongodb.com/cloud/atlas).

2. Cliquez sur "Essayer gratuitement" ou "S'inscrire".

3. Remplissez vos détails (nom, email, mot de passe) pour créer un compte.

4. Vérifiez votre adresse email en cliquant sur le lien envoyé dans votre boîte de réception.

![page d'inscription/connexion mongodb](https://cdn.hashnode.com/res/hashnode/image/upload/v1738858230073/c150c2be-8c4c-4e79-af44-3c0792b764e3.png align="center")

**Étape 2 : Créer un nouveau projet**

5. Après vous être connecté, vous serez redirigé vers le tableau de bord MongoDB Atlas.

6. Cliquez sur le bouton "Nouveau Projet". Cela vous mènera à la page Créer un Projet.

![page de création de projet mongodb](https://cdn.hashnode.com/res/hashnode/image/upload/v1739188846705/a25e1885-6f7d-4b00-907e-f03e4198d131.png align="center")

7. Remplissez le nom du projet et cliquez sur le bouton suivant, et il ouvrira une nouvelle page pour montrer les informations du propriétaire du projet.

![page de création de projet mongodb](https://cdn.hashnode.com/res/hashnode/image/upload/v1739189031867/42ae7fda-2a8e-4bd1-92f3-5c3dae4cc502.png align="center")

8. Maintenant, cliquez sur le bouton Créer un Projet. Cela vous mènera au tableau de bord principal du projet où vous aurez l'option de créer la base de données.

![page d'aperçu mongodb](https://cdn.hashnode.com/res/hashnode/image/upload/v1739189159505/35ecaac7-bbc4-4ee8-8ba0-196da2eaa311.png align="center")

9. Maintenant, cliquez sur le bouton Créer pour ouvrir une nouvelle page avec les détails de déploiement de votre cluster.

10. Choisissez un fournisseur cloud (AWS, Google Cloud ou Azure) et une région proche de votre emplacement.

11. Sélectionnez le "Niveau gratuit" (gratuit pour toujours, mais avec des ressources limitées) ou un niveau payant pour des projets plus importants.

![page de sélection de cluster mongodb](https://cdn.hashnode.com/res/hashnode/image/upload/v1739189327083/46c38f50-519e-473c-b302-b0239ab409f8.png align="center")

12. Donnez un nom à votre cluster (par exemple, `MyCluster`).

13. Cliquez sur "Créer un déploiement". Il faudra quelques minutes pour que le cluster soit provisionné.

14. Ensuite, il vous demandera de connecter votre cluster à la base de données via un service. Vous devriez voir votre nom d'utilisateur et mot de passe - gardez cela quelque part.

![page de connexion à la base de données mogodb](https://cdn.hashnode.com/res/hashnode/image/upload/v1739189624879/68a26902-861a-44b2-8d01-d04ceef55ddc.png align="center")

15. Ici, vous devrez vous créer un utilisateur de base de données, alors cliquez sur le bouton Créer un utilisateur de base de données.

16. Cela prendra quelques secondes pour terminer ce processus. Une fois terminé, fermez la fenêtre contextuelle et retournez au tableau de bord.

17. Sur la page du tableau de bord, vous pouvez voir le bouton Obtenir la chaîne de connexion. Allez-y et cliquez dessus.

![page de configuration de la base de données mongodb](https://cdn.hashnode.com/res/hashnode/image/upload/v1739189943883/84621420-312f-45e7-995e-18bf68245b1d.png align="center")

18. Cela ouvrira une nouvelle fenêtre contextuelle contenant votre URI MongoDB Atlas. Copiez simplement la chaîne, mettez-la dans votre fichier `.env` et utilisez le mot de passe que vous avez créé à l'étape 14.

![page d'affichage/masquage de l'URL mongodb](https://cdn.hashnode.com/res/hashnode/image/upload/v1739190119546/2dab2beb-02aa-4450-9272-fb7aac99c313.png align="center")

### Cas d'utilisation exemple :

```javascript
//fichier .env
MONGODB_URI='VOTRE URL MONGODB'
```

## **Structure et fonctionnalités de l'application**

L'accent de ce projet est mis sur la simplicité et la fonctionnalité, pour répliquer les fonctionnalités principales de Replit comme l'édition de code et les aperçus en temps réel. L'idée est de créer une application web simple qui vous permet de :

* Héberger trois composants essentiels : un explorateur de fichiers, l'éditeur Monaco et un bac à sable.

* Ouvrir les fichiers générés par CopilotKit dans l'éditeur Monaco et effectuer des opérations CRUD sur eux.

* Voir la sortie en temps réel de votre code pendant que vous travaillez.

* Discuter avec le chatbot CopilotKit, qui sera entièrement intégré à l'interface utilisateur.

Le plan est de garder l'implémentation propre et pratique tout en offrant une expérience de codage fluide.

### **Structure de la page web**

Puisque nous avons déjà configuré l'application Next.js, l'étape suivante consiste à créer une page web minimaliste avec les composants suivants :

1. **Explorateur de fichiers** : Affiche les fichiers générés par CopilotKit.

2. **Monaco Editor** : Un éditeur de code polyvalent qui gère divers types de fichiers et affiche le contenu.

3. **Bac à sable** : Montre la sortie en temps réel du code.

4. **Chatbot CopilotKit** : Génère des fichiers de code basés sur des invites en langage naturel.

### **Fonctionnalités clés**

* **Gestion des erreurs** : Toute défaillance, comme les problèmes d'API ou de base de données, sera mise en évidence avec du texte rouge pour une visibilité immédiate.

* **Présentation des données** : Les données sont présentées en deux parties : d'abord dans l'explorateur de fichiers pour les fichiers de code, et ensuite dans l'éditeur Monaco pour visualiser le contenu de ces fichiers.

* **Intégration du chatbot CopilotKit** : Le chatbot permettra des interactions en langage naturel avec la base de données. La boule de couleur bleue sur la page représente le chatbot CopilotKit, qui sert d'interface clé pour interagir avec la base de données.

  * Les utilisateurs peuvent poser des questions sur la base de données en utilisant le langage naturel.

  * Le chatbot traite ces requêtes, les convertit en SQL et récupère les résultats de manière transparente.

L'interface utilisateur ressemblera à quelque chose comme ceci : [https://replit-mongodb.vercel.app/](https://replit-mongodb.vercel.app/)

## **Comment construire le backend**

Avant de commencer à construire le backend, vous devrez mettre toutes les informations d'identification importantes dans votre fichier `.env`, qui devrait ressembler à ceci :

```xml
NEXT_PUBLIC_GROQ_CLOUD_API_KEY=<votre-clé-ici>
MONGODB_URI=<votre-url-mongodb>
```

Ce sont des variables d'environnement utilisées pour configurer des paramètres sensibles ou spécifiques à l'environnement dans une application :

1. `NEXT_PUBLIC_GROQ_CLOUD_API_KEY` :

  * Il s'agit d'une clé API publique pour accéder à l'API Groq Cloud.

  * Elle est préfixée par `NEXT_PUBLIC_`, ce qui signifie qu'elle est exposée au code côté client dans une application Next.js.

  * Remplacez `<votre-clé-ici>` par la clé API réelle fournie par Groq Cloud.

2. `MONGODB_URI` :

  * Il s'agit de la chaîne de connexion pour une base de données MongoDB.

  * Elle inclut l'URL de la base de données, les informations d'identification et d'autres détails de connexion.

  * Remplacez `<votre-url-mongodb>` par la chaîne de connexion MongoDB réelle.

### **Comment configurer le backend CopilotKit**

Ouvrez votre application Next.js dans n'importe quel éditeur de code, je préfère VSCode, et allez dans le dossier racine, qui ressemble à ceci :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1738858655371/f648cb98-62a0-4bdd-9d03-994c7bbf758f.png align="center")

À l'intérieur du dossier `app`, créez un nouveau dossier appelé `api`. À l'intérieur du dossier API, créez un autre dossier appelé `copilotkit`. Ensuite, créez un nouveau fichier appelé `route.js` et collez ce code à l'intérieur du fichier :

```jsx
import {
  CopilotRuntime,
  GroqAdapter,
  copilotRuntimeNextJSAppRouterEndpoint,
} from "@copilotkit/runtime";

import Groq from "groq-sdk";

const groq = new Groq({ apiKey: process.env.NEXT_PUBLIC_GROQ_CLOUD_API_KEY });

const copilotKit = new CopilotRuntime({
  async onResponse({ message, context }) {
    try {
      // Extraire toute opération de fichier du message et les traiter
      const fileBlocks = message.content.split("---");
      if (fileBlocks.length > 0) {
        // Formater la réponse pour utiliser l'action processFiles
        return {
          content: `@processFiles(response: \\`${message.content}\\`)`,
        };
      }
      return message;
    } catch (error) {
      console.error("Error in onResponse:", error);
      return message;
    }
  },
});

const serviceAdapter = new GroqAdapter({
  groq,
  model: "llama-3.3-70b-versatile",
  systemPrompt: `You are an AI-powered code generator integrated into a web-based IDE. Your task is to generate project files and code based on user commands.

When generating files, use this exact format:

FILE: filename.ext
CODE:
[code content here]

For multiple files, separate them with "---".

Example response:
I'll create a React component:

FILE: Button.jsx
CODE:
import React from 'react';

const Button = () => {
  return (
    <button className="btn">Click me</button>
  );
};

export default Button;

Important rules:
- Always include both FILE: and CODE: markers
- Use appropriate file extensions
- Generate complete, working code
- Maintain proper indentation
- Explain what you're creating before showing the files
- Make sure code is syntactically correct`,
});

export const POST = async (req) => {
  const { handleRequest } = copilotRuntimeNextJSAppRouterEndpoint({
    runtime: copilotKit,
    serviceAdapter,
    endpoint: "/api/copilotkit",
  });

  return handleRequest(req);
};
```

Voici une explication détaillée de chaque partie :

Ce code définit une intégration CopilotKit Runtime avec Next.js, conçue pour traiter les requêtes de génération et de gestion de fichiers de code dans un environnement IDE basé sur le web. Il se connecte au service cloud Groq pour des fonctionnalités supplémentaires et traite les sorties basées sur des fichiers à partir des réponses générées par l'IA.

Ce code configure une intégration CopilotRuntime avec le modèle IA de Groq pour générer et traiter des fichiers de code en réponse aux requêtes des utilisateurs. Voici une ventilation :

### **Composants clés** :

1. **Initialisation de Groq** :

  * Le SDK Groq est initialisé en utilisant la variable d'environnement `NEXT_PUBLIC_GROQ_CLOUD_API_KEY`.

  * Le modèle utilisé est `llama-3.3-70b-versatile`.

2. **CopilotRuntime** :

  * Une instance `CopilotRuntime` est créée avec un gestionnaire `onResponse` personnalisé.

  * La fonction `onResponse` traite la réponse de l'IA :

    * Extrait les blocs de fichiers (séparés par `---`) du message.

    * Formate la réponse pour déclencher une action `processFiles` si des blocs de fichiers sont détectés.

3. **GroqAdapter** :

  * Un `GroqAdapter` est configuré pour interagir avec l'API Groq.

  * Il inclut une invite système qui instruit l'IA à générer des fichiers de code dans un format spécifique :

    * Les fichiers sont marqués avec `FILE:` et `CODE:`.

    * Plusieurs fichiers sont séparés par `---`.

    * L'IA est instruite de générer un code complet et syntaxiquement correct avec des explications appropriées.

4. **Point de terminaison de l'API** :

  * Un point de terminaison `POST` est exposé en utilisant Next.js App Router.

  * Il utilise `copilotRuntimeNextJSAppRouterEndpoint` pour gérer les requêtes entrantes, en les passant au `CopilotRuntime` et au `GroqAdapter`.

### Exemple d'utilisation

1. **Requête**

  * Une requête POST à `/api/copilotkit` pourrait ressembler à ceci :

    ```bash
    curl -X POST http://localhost:3000/api/copilotkit \
    -H "Content-Type: application/json" \
    -d '{"command": "Create a React component for a button"}'
    ```

2. **Réponse de l'IA (traitée par `onResponse`)**

  * L'IA pourrait retourner cette réponse :

    ```plaintext
    FILE: Button.jsx
    CODE:
    import React from 'react';

    const Button = () => {
      return <button>Click me</button>;
    };

    export default Button;
    ```

3. **Réponse au client**

  * L'API enveloppe la réponse dans la structure formatée :

    ```json
    {
      "content": "@processFiles(response: `FILE: Button.jsx\nCODE:\nimport React from 'react';\n\nconst Button = () => {\n  return <button>Click me</button>;\n};\n\nexport default Button;`)"
    }
    ```

### Fonctionnalités clés

1. **Génération de code alimentée par l'IA avec la fenêtre contextuelle copilotkit** :

  * Le système génère des fichiers de projet complets basés sur les instructions de l'utilisateur.

  * Assure un formatage approprié (par exemple, les marqueurs `FILE:` et `CODE:`).

2. **Gestion des fichiers** :

  * Divise les réponses multi-fichiers en blocs gérables à l'aide de `---`.

  * Prend en charge les actions comme `@processFiles` pour l'intégration avec l'IDE.

3. **API évolutive** :

  * Conception modulaire avec `CopilotRuntime` et `GroqAdapter` permettant une extension et une personnalisation faciles.

4. **Gestion des erreurs** :

  * Journalise les erreurs sans interrompre le flux de travail.

  * Par défaut, retourne le message non traité en cas d'échec.

### Création de routes pour l'opération CRUD

Jusqu'à présent, nous avons couvert comment intégrer CopilotKit dans le backend. Maintenant, nous devons gérer les opérations sur les fichiers, nous allons donc créer une autre route pour gérer les fichiers avec la base de données.

Pour développer le backend pour la gestion des fichiers, je vais créer un nouveau dossier à l'intérieur du dossier API et le nommer `files`. À l'intérieur du dossier `files`, je vais créer un simple fichier `route.js`. Voici le code que je vais utiliser à l'intérieur du fichier :

* `app/api/files/route.tsx`

* ```javascript

import { NextResponse } from "next/server";
import mongoose from "mongoose";
import { connectDB, File } from "@/app/lib/mongodb";

// Type pour le corps de la requête
interface FileRequestBody {
  id?: string;
  name?: string;
  content?: string;
}
interface FileCreateRequest {
  name: string;
  content: string;
}

interface FileUpdateRequest {
  id: string;
  name?: string;
  content?: string;
}

// Récupérer tous les fichiers (GET /api/files)
export async function GET(): Promise<Response> {
  try {
    await connectDB(); // Assurer la connexion à la base de données
    const files = await File.find({});
    return NextResponse.json(files, { status: 200 });
  } catch (error) {
    return NextResponse.json(
      { error: "Failed to fetch files" },
      { status: 500 }
    );
  }
}

// Créer un nouveau fichier (POST /api/files)
export async function POST(req: Request): Promise<Response> {
  try {
    await connectDB(); // Assurer que la connexion à la base de données est réussie
    // Analyser le corps de la requête
    const { name, content }: FileRequestBody = await req.json();
    if (!name || !content) {
      throw new Error("Missing required fields: name or content");
    }

    // Journaliser les données entrantes pour le débogage
    console.log("Creating file with data:", { name, content });

    // Créer un nouveau fichier dans la base de données
    const newFile = new File({ name, content });
    await newFile.save();

    // Retourner le fichier nouvellement créé
    return NextResponse.json(newFile, { status: 201 });
  } catch (error: any) {
    // Journaliser l'erreur pour le débogage
    console.error("Error creating file:", error);

    return NextResponse.json(
      { error: "Failed to create file", message: error.message },
      { status: 400 }
    );
  }
}

// Mettre à jour le contenu du fichier (PUT /api/files)
export async function PUT(req: Request): Promise<Response> {
  try {
    await connectDB(); // Assurer la connexion à la base de données
    const { id, name, content }: FileRequestBody = await req.json();

    // Valider le format de l'ID
    if (!id || !mongoose.Types.ObjectId.isValid(id)) {
      return NextResponse.json({ error: "Invalid file ID" }, { status: 400 });
    }

    // Mettre à jour le nom ou le contenu du fichier si fourni
    const updatedFile = await File.findByIdAndUpdate(
      id,
      { ...(name && { name }), ...(content && { content }) },
      { new: true }
    );

    if (!updatedFile) {
      return NextResponse.json({ error: "File not found" }, { status: 404 });
    }

    return NextResponse.json(updatedFile, { status: 200 });
  } catch (error: any) {
    return NextResponse.json(
      { error: "Failed to update file" },
      { status: 400 }
    );
  }
}

// Supprimer un fichier (DELETE /api/files)
export async function DELETE(req: Request): Promise<Response> {
  try {
    await connectDB(); // Assurer la connexion à la base de données
    const { id }: FileRequestBody = await req.json();

    // Valider le format de l'ID
    if (!id || !mongoose.Types.ObjectId.isValid(id)) {
      return NextResponse.json({ error: "Invalid file ID" }, { status: 400 });
    }

    await File.findByIdAndDelete(id);
    return NextResponse.json(
      { message: "File deleted successfully" },
      { status: 200 }
    );
  } catch (error: any) {
    return NextResponse.json(
      { error: "Failed to delete file" },
      { status: 400 }
    );
  }
}
```

### **Explication du code** :

Ce code définit des routes API pour gérer les opérations CRUD (Create, Read, Update, Delete) sur une collection MongoDB appelée `File` dans une application Next.js. Chaque route est connectée à MongoDB en utilisant Mongoose et nous avons utilisé `NextResponse` pour formater les réponses.

### Décomposition du code

#### 1. **Imports**

```javascript
import { NextResponse } from "next/server";
import mongoose from "mongoose";
import connectDB from "@/app/lib/mongodb"; //nous avons créé ce fichier
import File from "@/app/lib/models/File"; //nous avons créé ce fichier
```

* `NextResponse` : Utilisé pour créer des réponses HTTP dans les routes API de Next.js.

* `connectDB` : Se connecte à la base de données MongoDB.

* `File` : Un modèle Mongoose représentant la collection `File`.

#### 2. **Récupérer tous les fichiers (GET)**

```javascript
export async function GET() {
  await connectDB(); // Assurer la connexion à la base de données
  try {
    const files = await File.find({}); // Récupérer tous les fichiers
    return NextResponse.json(files, { status: 200 }); // Retourner les fichiers au format JSON
  } catch (error) {
    return NextResponse.json(
      { error: "Failed to fetch files" },
      { status: 500 }
    );
  }
}
```

* **Objectif** : Récupère tous les documents dans la collection `File`.

* **Flux** :

  1. Se connecte à MongoDB.

  2. Utilise `File.find({})` pour récupérer tous les fichiers.

  3. Retourne les fichiers avec un statut `200` ou une erreur avec un statut `500`.

#### 3. **Créer un nouveau fichier (POST)**

```javascript
export async function POST(req) {
  await connectDB(); // Assurer la connexion à la base de données

  try {
    const { name, content } = await req.json(); // Analyser le corps de la requête
    if (!name || !content) {
      throw new Error("Missing required fields: name or content");
    }

    const newFile = new File({ name, content }); // Créer un nouveau fichier
    await newFile.save(); // Sauvegarder dans MongoDB

    return NextResponse.json(newFile, { status: 201 }); // Retourner le nouveau fichier
  } catch (error) {
    return NextResponse.json(
      { error: "Failed to create file", message: error.message },
      { status: 400 }
    );
  }
}
```

* **Objectif** : Crée un nouveau document dans la collection `File`.

* **Flux** :

  1. Analyse les champs `name` et `content` du corps de la requête.

  2. Valide les champs requis.

  3. Crée et sauvegarde le fichier dans MongoDB.

  4. Retourne le nouveau fichier avec un statut `201` ou une erreur avec un statut `400`.

#### 4. **Mettre à jour un fichier (PUT)**

```javascript
export async function PUT(req) {
  await connectDB(); // Assurer la connexion à la base de données
  try {
    const { id, name, content } = await req.json();

    if (!mongoose.Types.ObjectId.isValid(id)) {
      return NextResponse.json({ error: "Invalid file ID" }, { status: 400 });
    }

    const updatedFile = await File.findByIdAndUpdate(
      id,
      { ...(name && { name }), ...(content && { content }) },
      { new: true }
    );

    if (!updatedFile) {
      return NextResponse.json({ error: "File not found" }, { status: 404 });
    }

    return NextResponse.json(updatedFile, { status: 200 });
  } catch (error) {
    return NextResponse.json(
      { error: "Failed to update file" },
      { status: 400 }
    );
  }
}
```

* **Objectif** : Met à jour un document existant dans la collection `File`.

* **Flux** :

  1. Analyse l'`id`, `name` et `content` du corps de la requête.

  2. Valide l'`id` en utilisant `ObjectId` de Mongoose.

  3. Met à jour le document en utilisant `File.findByIdAndUpdate()` (met à jour uniquement les champs fournis).

  4. Retourne le document mis à jour avec un statut `200`, ou une erreur avec `400` ou `404`.

#### 5. **Supprimer un fichier (DELETE)**

```javascript
export async function DELETE(req) {
  await connectDB(); // Assurer la connexion à la base de données
  try {
    const { id } = await req.json();

    if (!mongoose.Types.ObjectId.isValid(id)) {
      return NextResponse.json({ error: "Invalid file ID" }, { status: 400 });
    }

    await File.findByIdAndDelete(id); // Supprimer le document
    return NextResponse.json(
      { message: "File deleted successfully" },
      { status: 200 }
    );
  } catch (error) {
    return NextResponse.json(
      { error: "Failed to delete file" },
      { status: 400 }
    );
  }
}
```

* **Objectif** : Supprime un document de la collection `File`.

* **Flux** :

  1. Analyse l'`id` du corps de la requête.

  2. Valide le format de l'`id`.

  3. Utilise `File.findByIdAndDelete()` pour supprimer le document.

  4. Retourne un message de succès avec un statut `200` ou une erreur avec `400`.

### Exemples de requêtes API : Comment tester l'API en local

1. **GET Tous les fichiers**

```bash
curl -X GET http://localhost:3000/api/files
```

2. **Créer un fichier (POST)**

```bash
curl -X POST http://localhost:3000/api/files \
-H "Content-Type: application/json" \
-d '{"name": "example.txt", "content": "This is a test file"}'
```

3. **Mettre à jour un fichier (PUT)**

```bash
curl -X PUT http://localhost:3000/api/files \
-H "Content-Type: application/json" \
-d '{"id": "64ffab67c728f51234567890", "name": "updated.txt", "content": "Updated content"}'
```

4. **Supprimer un fichier (DELETE)**

```bash
curl -X DELETE http://localhost:3000/api/files \
-H "Content-Type: application/json" \
-d '{"id": "64ffab67c728f51234567890"}'
```

### Création de schémas MongoDB

Maintenant, créez un dossier `lib` à l'intérieur du dossier `app`. Ce dossier `lib` gérera les tâches essentielles de la base de données, telles que le schéma de la base de données et la connectivité. À l'intérieur du dossier `lib`, créez un autre dossier nommé `models`. Dans ce dossier `models`, créez un nouveau fichier appelé `File.js` et collez le code suivant à l'intérieur.

Cette version simplifie les instructions et améliore la clarté tout en conservant le sens original.

```typescript

import mongoose, { Schema, Document, Model } from "mongoose";

// Définir une interface pour le document de fichier
interface IFile extends Document {
  name: string;
  content: string;
  createdAt: Date;
  updatedAt: Date;
}

// Définir le schéma pour le modèle de fichier
const fileSchema = new Schema<IFile>(
  {
    _id: { type: Schema.Types.ObjectId, auto: true }, // MongoDB default _id
    name: { type: String, required: true }, // Removed unique constraint
    content: { type: String, required: true },
  },
  { timestamps: true } // Automatically adds createdAt & updatedAt
);

// Exporter le modèle File avec la sécurité des types
const File: Model<IFile> =
  mongoose.models.File || mongoose.model<IFile>("File", fileSchema);

export default File;

```

### Explication du code

Ce code définit un schéma et un modèle Mongoose pour une collection `File` dans une base de données MongoDB. Il spécifie la structure et les règles pour les documents de la collection.

Ce code définit un schéma et un modèle Mongoose pour un document File dans MongoDB. Voici une brève explication :

### **Composants clés** :

1. **Interface (`IFile`)** :

  * Définit la structure d'un document `File` avec :

    * `name` (string, requis).

    * `content` (string, requis).

    * `createdAt` et `updatedAt` (gérés automatiquement par Mongoose).

2. **Schéma (`fileSchema`)** :

  * Mappe l'interface `IFile` à un schéma MongoDB.

  * Inclut :

    * `_id` : ObjectId auto-généré par MongoDB.

    * `name` et `content` : Champs requis.

    * `timestamps: true` : Ajoute automatiquement les champs `createdAt` et `updatedAt`.

3. **Modèle (`File`)** :

  * Crée ou récupère le modèle Mongoose pour la collection `File`.

  * Assure la sécurité des types en utilisant l'interface `IFile`.

### Connexion à la base de données

La moitié du travail est faite ! Maintenant, il est temps de connecter notre application à la base de données. Pour ce faire, je vais créer un nouveau fichier à l'intérieur du dossier `lib`, où nous avons précédemment créé le schéma de la base de données. Je vais nommer le fichier `mongodb.tsx` et coller le code suivant à l'intérieur :

```typescript
import mongoose, { Schema, Model, Connection } from "mongoose";
import { IFile } from "../types";

// Définir l'URI de connexion mongoose
const MONGODB_URI = process.env.MONGODB_URI;

if (!MONGODB_URI) {
  throw new Error(
    "Veuillez définir la variable d'environnement MONGODB_URI dans .env.local"
  );
}

let cached: {
  conn: Connection | null;
  promise: Promise<Connection> | null;
} = { conn: null, promise: null };

export async function connectDB(): Promise<Connection> {
  if (cached.conn) {
    return cached.conn;
  }

  if (!cached.promise) {
    cached.promise = mongoose.connect(MONGODB_URI!).then((mongoose) => {
      return mongoose.connection;
    });
  }

  try {
    cached.conn = await cached.promise;
  } catch (e) {
    cached.promise = null;
    throw e;
  }

  return cached.conn;
}

// Définir le schéma pour le modèle de fichier
const fileSchema = new Schema<IFile>(
  {
    name: { type: String, required: true },
    content: { type: String, required: true },
  },
  {
    timestamps: true,
  }
);

// Exporter le modèle File avec la sécurité des types
export const File = (mongoose.models.File ||
mongoose.model<IFile>("File", fileSchema)) as Model<IFile>;
```

### Explication du code

Ce code configure une connexion MongoDB en utilisant la bibliothèque `mongoose` dans une application Node.js ou Next.js. Il garantit que la base de données est connectée efficacement et évite les connexions redondantes.

Ce code configure une connexion MongoDB et définit un schéma et un modèle Mongoose pour un document File. Voici une brève explication :

### **Composants clés** :

1. **Connexion MongoDB** :

  * Utilise la variable d'environnement `MONGODB_URI` pour se connecter à MongoDB.

  * Implémente un mécanisme de mise en cache pour réutiliser la connexion et éviter plusieurs connexions.

  * Lance une erreur si `MONGODB_URI` n'est pas défini.

2. **Schéma (`fileSchema`)** :

  * Définit la structure d'un document `File` avec :

    * `name` (string, requis).

    * `content` (string, requis).

  * Ajoute automatiquement les timestamps `createdAt` et `updatedAt`.

3. **Modèle (`File`)** :

  * Crée ou récupère le modèle Mongoose pour la collection `File`.

  * Assure la sécurité des types en utilisant l'interface `IFile`.

#### Exemple de structure de répertoire :

```javascript
/project
  /pages
    /api
      test.js
  /utils
    connectDB.js
  .env.local
```

### Notes finales :

* Ce code évite plusieurs connexions MongoDB en vérifiant le `readyState`.

* Il est réutilisable et modulaire, ce qui le rend facile à maintenir.

* Toujours sécuriser le `MONGODB_URI` dans les variables d'environnement pour éviter d'exposer des informations d'identification sensibles.

### Assurer la sécurité des types

Puisque nous utilisons TypeScript, nous devrons déclarer le type de fichier `files`, `socket` et un `index`. Pour ce faire, créez un nouveau dossier dans le répertoire racine du projet et nommez-le `types` et créez trois fichiers `socket.ts`, `files.ts` et `index.ts` à l'intérieur du dossier. Dans chaque fichier, collez le code donné pour leur fichier respectif.

```typescript
//index.ts
export interface IFile {
  _id: string;
  name: string;
  content: string;
  createdAt?: Date;
  updatedAt?: Date;
}
//socket.ts
import { FileData } from '../types/file';

export interface ServerToClientEvents {
"new-file": (file: FileData) => void;
"delete-file": (fileId: string) => void;
"file-update": (data: { fileId: string; content: string }) => void;
}

export interface ClientToServerEvents {
"new-file": (file: FileData) => void;
"delete-file": (fileId: string) => void;
"file-update": (data: { fileId: string; content: string }) => void;
}
//file.ts
export interface FileData {
_id: string;
name: string;
content: string;
}
```

## **Comment construire le frontend**

Pour le frontend, nous allons le garder simple, en visant une interface utilisateur qui ressemble étroitement à Replit. Les composants clés dont nous avons besoin pour ce projet sont un explorateur de fichiers, un éditeur Monaco et un composant Sandbox.

* **Explorateur de fichiers** : Ce composant affichera et gérera les fichiers de code, positionné sur le côté gauche de l'écran.

* **Éditeur Monaco** : Ce composant permettra aux utilisateurs de visualiser et de modifier le contenu des fichiers de code.

* **Sandbox** : Ce composant rendra l'aperçu en direct du contenu à l'intérieur des fichiers de code.

Pour construire ces composants, nous n'utiliserons aucune bibliothèque d'interface utilisateur tierce ; au lieu de cela, nous nous appuierons uniquement sur TailwindCSS, qui est préconfiguré avec Next.js.

Maintenant, construisons les composants :

1. Ouvrez votre VS Code.

2. Ouvrez le dossier Next.js où vous avez créé votre projet.

Puisque je travaille sans un dossier `src`, vous ne trouverez qu'un dossier `app`. À l'intérieur du dossier `app`, créez un nouveau dossier appelé components.

* Après avoir créé le dossier, la structure de votre projet devrait ressembler à ceci :

* **FileExplorer.js -** C'est notre explorateur de fichiers

* **ScreenOne.js-** C'est notre éditeur Monaco

* **LivePreview.js-** C'est notre composant sandbox

Voyons comment je construis ces composants et vous pouvez le faire aussi,

### FileExploer.tsx

Le `FileExplorer` est un composant React qui affiche une liste de fichiers récupérés depuis un backend (MongoDB) et permet aux utilisateurs de sélectionner, créer, modifier et supprimer des fichiers. Il utilise les Hooks React pour la gestion d'état et les effets de cycle de vie, Tailwind CSS pour le style, et les icônes `lucide-react` pour les actions de l'interface utilisateur.

```typescript
import React, { useEffect, useState } from "react";
import { Plus, Trash2, Pencil } from "lucide-react";
import io, { Socket } from "socket.io-client";
import { FileData } from '../types/file';

interface FileExplorerProps {
files: FileData[];
onFileSelect: (file: FileData) => void;
currentFile: FileData | null;
}

const FileExplorer: React.FC<FileExplorerProps> = ({
files: initialFiles,
onFileSelect,
currentFile,
}) => {
const [files, setFiles] = useState<FileData[]>(initialFiles);
  const [socket, setSocket] = useState<Socket | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);
  const [newFileName, setNewFileName] = useState<string>("");
  const [editingFile, setEditingFile] = useState<string | null>(null);
  const [editedFileName, setEditedFileName] = useState<string>("");

  // Initialiser la connexion socket
  useEffect(() => {
    const socketInstance = io("http://localhost:3000", {
      reconnection: true,
      reconnectionAttempts: 5,
      reconnectionDelay: 1000,
    });

    socketInstance.on("connect", () => {
      console.log("Connecté au serveur Socket.IO");
    });

    socketInstance.on("connect_error", (error) => {
      console.error("Erreur de connexion socket :", error);
    });

    socketInstance.on("disconnect", () => {
      console.log("Déconnecté du serveur Socket.IO");
    });

    setSocket(socketInstance);

    return () => {
      if (socketInstance) {
        socketInstance.disconnect();
      }
    };
  }, []);

  useEffect(() => {
    if (!socket) return;

    // Écouter les mises à jour en temps réel
    socket.on("new-file", (newFile: FileData) => {
      setFiles((prevFiles) => {
        if (!prevFiles.some((file) => file._id === newFile._id)) {
          return [...prevFiles, newFile];
        }
        return prevFiles;
      });
    });

    socket.on("delete-file", (fileId: string) => {
      setFiles((prevFiles) => prevFiles.filter((file) => file._id !== fileId));
    });

    socket.on("update-file", (updatedFile: FileData) => {
      setFiles((prevFiles) =>
        prevFiles.map((file) =>
          file._id === updatedFile._id
            ? { ...file, name: updatedFile.name }
            : file
        )
      );
    });

    return () => {
      socket.off("new-file");
      socket.off("delete-file");
      socket.off("update-file");
    };
  }, [socket]);

  // Récupérer les fichiers initiaux
  const fetchFiles = async () => {
    try {
      const response = await fetch("/api/files");
      if (!response.ok) throw new Error("Échec de la récupération des fichiers");
    const data: FileData[] = await response.json();
      setFiles(data);
    } catch (error) {
      console.error("Erreur lors de la récupération des fichiers :", error);
      setError("Échec du chargement des fichiers");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchFiles();
  }, []);

  // Créer un nouveau fichier
  const createNewFile = async () => {
    if (!newFileName.trim()) return;
    try {
      const response = await fetch("/api/files", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name: newFileName }),
      });

      if (!response.ok) throw new Error("Échec de la création du fichier");

    const newFile: FileData = await response.json();
      socket?.emit("new-file", newFile);
      setNewFileName("");
    } catch (error) {
      console.error("Erreur lors de la création du fichier :", error);
    }
  };

  const handleDeleteFile = async (e: React.MouseEvent, id: string) => {
    e.stopPropagation();
    setFiles((prevFiles) => prevFiles.filter((file) => file._id !== id)); // Mise à jour optimiste

    try {
      const response = await fetch("/api/files", {
        method: "DELETE",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ id }),
      });

      if (!response.ok) throw new Error("Échec de la suppression du fichier");

      socket?.emit("delete-file", id);
    } catch (error) {
      console.error("Erreur lors de la suppression du fichier :", error);
      await fetchFiles(); // Revenir à l'état précédent si l'appel API échoue
    }
  };

const handleEditStart = (e: React.MouseEvent, file: FileData) => {
    e.stopPropagation();
    setEditingFile(file._id);
    setEditedFileName(file.name);
  };

  const handleEditSave = async (
    e: React.FocusEvent | React.KeyboardEvent,
    id: string
  ) => {
    e.preventDefault();
    if (!editedFileName.trim()) return;

    const previousFiles = [...files];
    setFiles((prevFiles) =>
      prevFiles.map((file) =>
        file._id === id ? { ...file, name: editedFileName } : file
      )
    ); // Mise à jour optimiste

    try {
      const response = await fetch("/api/files", {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ id, name: editedFileName }),
      });

      if (!response.ok) throw new Error("Échec de la mise à jour du fichier");

    const updatedFile: FileData = await response.json();
      socket?.emit("update-file", updatedFile);
      setEditingFile(null);
    } catch (error) {
      console.error("Erreur lors de la mise à jour du fichier :", error);
      setFiles(previousFiles); // Revenir à l'état précédent si l'appel API échoue
    }
  };

  return (
    <div className="w-64 bg-gray-900 p-4 h-full text-white rounded-lg shadow-lg flex flex-col">
      <h2 className="text-lg font-semibold mb-4">Fichiers</h2>

      {loading ? (
        <div className="text-gray-400 text-sm">Chargement des fichiers...</div>
      ) : error ? (
        <div className="text-red-500 text-sm">{error}</div>
      ) : files.length === 0 ? (
        <div className="text-gray-400 text-sm">Aucun fichier pour l'instant</div>
      ) : (
        <div className="space-y-2 overflow-y-auto flex-grow">
          {files.map((file) => (
            <div
              key={file._id}
              className={`cursor-pointer flex justify-between items-center p-2 rounded text-white transition-all duration-200 ${
                currentFile?._id === file._id
                  ? "bg-blue-600"
                  : "hover:bg-gray-700"
              }`}
              onClick={() => onFileSelect(file)}
            >
              {editingFile === file._id ? (
                <input
                  type="text"
                  value={editedFileName}
                onChange={(e: React.ChangeEvent<HTMLInputElement>) => setEditedFileName(e.target.value)}
                onBlur={(e: React.FocusEvent<HTMLInputElement>) => handleEditSave(e, file._id)}
                onKeyDown={(e: React.KeyboardEvent<HTMLInputElement>) =>
                e.key === "Enter" ? handleEditSave(e, file._id) : null
                }
                  autoFocus
                  className="bg-gray-800 text-white p-1 rounded outline-none w-32"
                />
              ) : (
                <span className="truncate flex-grow">📄 {file.name}</span>
              )}

              <div className="flex items-center gap-2">
                <button
                onClick={(e: React.MouseEvent) => handleEditStart(e, file)}
                  className="text-yellow-400 hover:text-yellow-600 p-1 rounded"
                >
                  <Pencil size={16} />
                </button>
                <button
                onClick={(e: React.MouseEvent) => handleDeleteFile(e, file._id)}
                  className="text-red-400 hover:text-red-600 p-1 rounded"
                >
                  <Trash2 size={16} />
                </button>
              </div>
            </div>
          ))}
        </div>
      )}

    </div>
  );
};

export default FileExplorer;
```

### **Explication du code**

### Brève explication du code

Le composant `FileExplorer` est un composant React conçu pour gérer et afficher une liste de fichiers en temps réel. Il utilise [**Socket.IO**](http://Socket.IO) pour les mises à jour en temps réel, permettant aux utilisateurs d'ajouter, de supprimer et de modifier des fichiers de manière dynamique.

### Fonctionnalités clés :

#### 1. **Gestion d'état**

Le composant utilise le Hook `useState` de React pour gérer les états suivants :

* `files` : Liste des fichiers affichés dans l'explorateur de fichiers.

* `socket` : La connexion active [Socket.IO](http://Socket.IO).

* `loading` & `error` : Gérer l'état du chargement des fichiers.

* `newFileName`, `editingFile`, et `editedFileName` : Gérer les processus de création et d'édition de fichiers.

```javascript
const [files, setFiles] = useState([]);
const [socket, setSocket] = useState(null);
const [loading, setLoading] = useState(true);
const [error, setError] = useState(null);
const [newFileName, setNewFileName] = useState("");
const [editingFile, setEditingFile] = useState(null);
const [editedFileName, setEditedFileName] = useState("");
```

#### 2. **Intégration de [**Socket.IO**](http://Socket.IO)**

* Établit une connexion en temps réel à un serveur [Socket.IO](http://Socket.IO).

* Écoute les événements comme `new-file`, `delete-file`, et `update-file` pour mettre à jour la liste des fichiers de manière dynamique.

* Nettoie la connexion socket lorsque le composant est démonté.

```javascript
useEffect(() => {
  const socketInstance = io("http://localhost:3000", {
    reconnection: true,
    reconnectionAttempts: 5,
    reconnectionDelay: 1000,
  });

  socketInstance.on("connect", () => {
    console.log("Connecté au serveur Socket.IO");
  });

  setSocket(socketInstance);

  return () => {
    if (socketInstance) socketInstance.disconnect();
  };
}, []);
```

#### 3. **Mises à jour de fichiers en temps réel**

Gère les événements en temps réel pour la création, la suppression et la mise à jour de fichiers.

```javascript
useEffect(() => {
  if (!socket) return;

  socket.on("new-file", (newFile) => {
    setFiles((prevFiles) =>
      prevFiles.some((file) => file._id === newFile._id)
        ? prevFiles
        : [...prevFiles, newFile]
    );
  });

  socket.on("delete-file", (fileId) => {
    setFiles((prevFiles) => prevFiles.filter((file) => file._id !== fileId));
  });

  socket.on("update-file", (updatedFile) => {
    setFiles((prevFiles) =>
      prevFiles.map((file) =>
        file._id === updatedFile._id
          ? { ...file, name: updatedFile.name }
          : file
      )
    );
  });

  return () => {
    socket.off("new-file");
    socket.off("delete-file");
    socket.off("update-file");
  };
}, [socket]);
```

#### 4. **Opérations CRUD**

* **Récupérer les fichiers** : Récupère la liste initiale des fichiers depuis le serveur.

* **Créer un fichier** : Envoie une requête POST pour ajouter un nouveau fichier.

* **Supprimer un fichier** : Envoie une requête DELETE pour supprimer un fichier et met à jour l'interface utilisateur de manière optimiste.

* **Modifier un fichier** : Envoie une requête PUT pour mettre à jour le nom d'un fichier et effectue des mises à jour optimistes.

Ce code définit un composant FileExplorer React qui permet aux utilisateurs de gérer et d'interagir avec des fichiers dans un système de fichiers.

**Note : Toutes les opérations sur l'application sont sauvegardées en temps réel pour la démonstration, vous pouvez rafraîchir la page pour voir que les modifications ne sont pas supprimées.**

### **ScreenOne.tsx**

Le composant `ScreenOne` est un panneau d'éditeur de code qui affiche et met à jour dynamiquement le code pour un fichier sélectionné. Il intègre l'éditeur Monaco pour mettre en évidence la syntaxe en fonction du type de fichier (par exemple, JavaScript, HTML, CSS).

Le composant montre le nom du fichier sélectionné, permet aux utilisateurs de modifier son contenu et envoie les mises à jour à la base de données en temps réel. Il offre également une interface utilisateur propre et conviviale avec un thème sombre et des options d'éditeur configurables. Cela est idéal pour les environnements de codage comme les IDE ou les terrains de jeu de code.

```typescript

import React, { useEffect, useState } from "react";
import { Editor } from "@monaco-editor/react";

interface File {
  name: string;
}

interface ScreenOneProps {
  selectedFile: File | null;
  code: string;
  onChange: (newCode: string | undefined) => void;
}

const ScreenOne: React.FC<ScreenOneProps> = ({ selectedFile, code, onChange }) => {
  const [language, setLanguage] = useState<string>("javascript");

  useEffect(() => {
    if (!selectedFile) return;
    setLanguage(getLanguageForFile(selectedFile.name));
  }, [selectedFile]);

  const getLanguageForFile = (filename: string): string => {
    const extension = filename.split(".").pop()?.toLowerCase();
    switch (extension) {
      case "js":
      case "jsx":
        return "javascript";
      case "html":
        return "html";
      case "css":
        return "css";
      case "json":
        return "json";
      default:
        return "plaintext";
    }
  };

  const handleCodeChange = (newCode: string | undefined): void => {
    onChange(newCode); // Appeler la prop onChange pour mettre à jour le code dans LivePreview
  };

  return (
    <div className="flex-1 flex flex-col bg-[#2d2d2d] text-white p-6 rounded-lg shadow-md">
      <div className="flex items-center justify-between mb-4">
        <h2 className="text-2xl font-semibold">Éditeur de code</h2>
        <div className="text-sm text-gray-400">
          {selectedFile ? selectedFile.name : "Aucun fichier sélectionné"}
        </div>
      </div>
      <div className="flex-grow bg-gray-800 rounded-lg shadow-inner">
        <Editor
          height="calc(100vh - 160px)"
          language={language}
          value={code}
          onChange={handleCodeChange} // Mettre à jour le code lors du changement
          theme="vs-dark"
          options={{
            minimap: { enabled: false },
            lineNumbers: "on",
            wordWrap: "on",
            scrollBeyondLastLine: false,
          }}
        />
      </div>
    </div>
  );
};

export default ScreenOne;
```

### **Explication du code**

### Explication du code :

Ce composant React, `ScreenOne`, représente un écran d'éditeur de code où les utilisateurs peuvent éditer des fichiers dans un langage de programmation spécifié. L'éditeur ajuste dynamiquement sa mise en évidence de syntaxe en fonction du type de fichier sélectionné. Il utilise la bibliothèque `@monaco-editor/react` pour l'interface de l'éditeur.

Ce code définit un composant React ScreenOne, qui est un éditeur de code utilisant l'éditeur Monaco (utilisé dans VS Code). Voici une brève explication :

### **Fonctionnalités clés** :

1. **Éditeur de code** :

  * Utilise la bibliothèque `@monaco-editor/react` pour rendre un éditeur de code.

  * Prend en charge la mise en évidence de la syntaxe pour divers langages (par exemple, JavaScript, HTML, CSS, JSON).

2. **Détection dynamique du langage** :

  * Détecte le langage de programmation en fonction de l'extension du fichier sélectionné (par exemple, `.js` → JavaScript).

  * Par défaut, utilise `plaintext` pour les types de fichiers non pris en charge.

3. **Props** :

  * `selectedFile` : Le fichier actuellement sélectionné (contient le nom du fichier).

  * `code` : Le contenu du code actuel à afficher dans l'éditeur.

  * `onChange` : Une fonction de rappel pour gérer les changements de code.

4. **UI** :

  * Affiche le nom du fichier et un titre ("Éditeur de code").

  * Stylisé avec Tailwind CSS pour un thème sombre et des coins arrondis.

5. **Configuration de l'éditeur** :

  * Utilise le thème `vs-dark`.

  * Désactive la mini-carte et active les numéros de ligne et le retour à la ligne automatique.

### **LivePreview.tsx**

Le composant `LivePreview` génère dynamiquement un aperçu en direct du code pour les projets statiques (HTML, CSS, JS) ou les projets basés sur React. Il détecte le type de projet, configure les fichiers nécessaires (par exemple, `index.html`, `App.js`), et rend un aperçu en temps réel en utilisant Sandpack de CodeSandbox. L'aperçu s'adapte au fichier sélectionné et se met à jour à mesure que le code change, offrant une expérience de codage fluide.

```typescript

import React, { useEffect, useState } from "react";
import {
  SandpackProvider,
  SandpackLayout,
  SandpackCodeEditor,
  SandpackPreview,
  SandpackThemeProvider,
} from "@codesandbox/sandpack-react";

interface FileAccumulator {
[key: string]: { code: string };
}

interface File {
  name: string;
  content: string;
}

interface LivePreviewProps {
files: File[];
currentFile: File | null;
code: string;
onCodeChange?: (value: string | undefined) => void;
}
interface SandpackFile {
  code: string;
}

interface SandpackFiles {
  [key: string]: SandpackFile;
}

const LivePreview: React.FC<LivePreviewProps> = ({ files, currentFile, code }) => {
  const [sandboxFiles, setSandboxFiles] = useState<Record<string, { code: string }>>({});
  const [template, setTemplate] = useState<"vanilla" | "react">("vanilla"); // Par défaut statique
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    if (!currentFile || !files) return;

    const newFiles: SandpackFiles = files.reduce((acc: FileAccumulator, file) => {
    acc[`/${file.name}`] = { code: file.content };
    return acc;
    }, {});

    // Vérifier si le projet est basé sur React
    const isReactProject = files.some(
      (file) =>
        file.name.endsWith(".jsx") ||
        (file.name.endsWith(".js") && file.content.includes("React"))
    );

    if (isReactProject) {
      setTemplate("react");

      // Assurer que App.js existe
      if (!newFiles["/App.js"]) {
        newFiles["/App.js"] = {
          code: `
            import React from "react";
            function App() { return <h1>Hello, React!</h1>; }
            export default App;
          `,
        };
      }

      // Assurer que index.js existe
      newFiles["/index.js"] = {
        code: `
          import React from "react";
          import ReactDOM from "react-dom/client";
          import App from "./App";

          const root = document.getElementById("root");
          if (root) {
            ReactDOM.createRoot(root).render(<App />);
          } else {
            console.error("Root element not found!");
          }
        `,
      };

      // Assurer que index.html existe
      newFiles["/index.html"] = {
        code: `
          <!DOCTYPE html>
          <html lang="en">
          <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>React App</title>
          </head>
          <body>
            <div id="root"></div>
          </body>
          </html>
        `,
      };

      // Assurer que package.json existe
      newFiles["/package.json"] = {
        code: JSON.stringify(
          {
            main: "/index.js",
            dependencies: {
              react: "18.2.0",
              "react-dom": "18.2.0",
            },
          },
          null,
          2
        ),
      };
    } else {
      setTemplate("vanilla");

      const htmlFile = files.find((f) => f.name.endsWith(".html"));
      if (htmlFile) {
        let htmlContent = htmlFile.content;

        // Injecter les fichiers CSS
        files
          .filter((f) => f.name.endsWith(".css"))
          .forEach((cssFile) => {
            htmlContent = htmlContent.replace(
              "</head>",
              `<link rel="stylesheet" href="${cssFile.name}"></head>`
            );
          });

        // Injecter les fichiers JS
        files
          .filter((f) => f.name.endsWith(".js"))
          .forEach((jsFile) => {
            htmlContent = htmlContent.replace(
              "</body>",
              `<script src="${jsFile.name}"></script></body>`
            );
          });

        newFiles["/index.html"] = { code: htmlContent };
      }
    }

    // S'assurer que le fichier actuel est inclus
    newFiles[`/${currentFile.name}`] = { code };
    setSandboxFiles(newFiles);
    setLoading(false);
  }, [files, currentFile, code]);

  return (
    <div className="flex-1 bg-white border-l border-gray-300">
      {loading ? (
        <div className="h-full flex items-center justify-center text-gray-500">
          Chargement...
        </div>
      ) : currentFile ? (
        <SandpackProvider
        template={template}
        files={sandboxFiles}
        options={{ activeFile: `/${currentFile.name}` }}
        >
        <SandpackThemeProvider>
            <SandpackLayout>
            <SandpackCodeEditor showTabs={false}  />
            <SandpackPreview style={{ height: "600px", border: "none" }} />
            </SandpackLayout>
        </SandpackThemeProvider>
        </SandpackProvider>
      ) : (
        <div className="h-full flex items-center justify-center text-gray-500">
          Sélectionnez un fichier à prévisualiser
        </div>
      )}
    </div>
  );
};

export default LivePreview;
```

### Explication du code

### Explication du code :

Le composant `LivePreview` fournit un environnement de prévisualisation en direct pour les fichiers HTML/CSS/JS statiques ou les projets basés sur React. Il utilise la bibliothèque Sandpack de CodeSandbox pour rendre dynamiquement les fichiers de code dans une fenêtre de prévisualisation similaire à un navigateur. Le composant ajuste automatiquement son comportement en fonction des types de fichiers et du contenu pour déterminer si le projet est statique ou basé sur React.

Ce code définit un composant React LivePreview qui utilise Sandpack (de CodeSandbox) pour fournir un éditeur de code en direct et un environnement de prévisualisation. Voici une brève explication :

### **Fonctionnalités clés** :

1. **Intégration de Sandpack** :

  * Utilise `@codesandbox/sandpack-react` pour rendre un éditeur de code et une prévisualisation en direct.

  * Prend en charge les projets React et JavaScript/HTML/CSS vanilla.

2. **Gestion dynamique des fichiers** :

  * Convertit une liste de fichiers (prop `files`) en un format compatible avec Sandpack.

  * Détecte automatiquement si le projet est basé sur React (par exemple, contient `.jsx` ou des imports React).

  * Assure que les fichiers nécessaires (par exemple, `App.js`, `index.js`, `index.html`, `package.json`) existent pour les projets React.

3. **Changement de modèle** :

  * Définit le modèle Sandpack sur `"react"` pour les projets React ou `"vanilla"` pour les projets HTML/CSS/JS statiques.

4. **Injection de code** :

  * Pour les projets vanilla, injecte les fichiers CSS et JS liés dans le fichier HTML.

5. **État de chargement** :

  * Affiche un message de chargement pendant le traitement des fichiers.

6. **UI** :

  * Affiche un éditeur de code et une prévisualisation en direct côte à côte.

  * Affiche un message si aucun fichier n'est sélectionné.

### Exécution des sockets dans l'application

Il est maintenant temps de s'attaquer à ce gros problème. Comme vous le savez, nous utilisons des sockets pour la communication de données en temps réel, nous avons donc besoin d'un fichier `server.tsx` dans le répertoire racine de l'application (en dehors du dossier `src`) et coller ce code :

```typescript

import { createServer, IncomingMessage, ServerResponse } from "http";
import { parse, UrlWithParsedQuery } from "url";
import next from "next";
import { Server, Socket } from "socket.io";

const dev: boolean = process.env.NODE_ENV !== "production";
const app = next({ dev });
const handle = app.getRequestHandler();

app.prepare().then(() => {
  const httpServer = createServer((req: IncomingMessage, res: ServerResponse) => {
    const parsedUrl: UrlWithParsedQuery = parse(req.url || "", true);
    handle(req, res, parsedUrl);
  });

  // Déterminer l'origine CORS de manière dynamique
  const allowedOrigin: string = dev
    ? "http://localhost:3000" // Développement local
    : "*"; // Déploiement Vercel

  // Initialiser Socket.IO avec une configuration CORS dynamique
  const io = new Server(httpServer, {
    cors: {
      origin: allowedOrigin,
      methods: ["GET", "POST"],
      credentials: true,
    },
  });

  // Gestionnaires d'événements Socket.IO
  io.on("connection", (socket: Socket) => {
    console.log("Client connecté");

    // Gérer la création de nouveaux fichiers
    socket.on("new-file", (newFile: { id: string; name: string; content: string }) => {
      console.log("Nouveau fichier créé :", newFile);
      // Diffuser à tous les clients sauf l'expéditeur
      socket.broadcast.emit("new-file", newFile);
    });

    // Gérer la suppression de fichiers
    socket.on("delete-file", (fileId: string) => {
      console.log("Fichier supprimé :", fileId);
      socket.broadcast.emit("delete-file", fileId);
    });

    // Gérer la mise à jour de fichiers
    socket.on("update-file", (updatedFile: { id: string; name: string; content: string }) => {
      console.log("Fichier mis à jour :", updatedFile);
      socket.broadcast.emit("update-file", updatedFile);
    });

    // Gérer la déconnexion du client
    socket.on("disconnect", () => {
      console.log("Client déconnecté");
    });
  });

  // Démarrer le serveur sur le port spécifié
  const PORT: number | string = process.env.PORT || 3000;
  httpServer.listen(PORT, () => {
    console.log(`> Prêt sur ${dev ? "http://localhost:3000" : allowedOrigin}`);
  });
});
```

### Explication du code

Ce code configure un **serveur Next.js** avec [**Socket.IO**](http://Socket.IO) pour la communication en temps réel. Il :

1. Initialise une application Next.js et la prépare à gérer les requêtes HTTP.

2. Configure CORS de manière dynamique pour [Socket.IO](http://Socket.IO), permettant les connexions depuis [`localhost:3000`](http://localhost:3000) en développement ou toutes les origines en production.

3. **Configure** [**Socket.IO**](http://Socket.IO) pour gérer les événements en temps réel comme :

  * Création de nouveaux fichiers

  * Suppression de fichiers

  * Mises à jour de fichiers

  * Déconnexion du client

4. Diffuse les événements à tous les clients connectés sauf l'expéditeur.

5. Démarre le serveur sur un port spécifié (par défaut : 3000).

C'est un serveur de base en temps réel pour la gestion de fichiers avec Next.js et [Socket.IO](http://Socket.IO).

### Regrouper tous les composants ensemble

Pour ce faire, nous devons modifier le fichier `page.tsx`. Copiez simplement le code donné et collez-le dans le fichier `page.js`

```typescript

"use client";
import React, { useState, useEffect } from "react";
import { useCopilotAction, useCopilotReadable } from "@copilotkit/react-core";
import { CopilotPopup } from "@copilotkit/react-ui";
import ScreenOne from "./components/ScreenOne";
import FileExplorer from "./components/FileExplorer";
import LivePreview from "./components/LivePreview";
import io, { Socket } from "socket.io-client";

interface File {
  _id: string;
  name: string;
  content: string;
}

function Page() {
  const [files, setFiles] = useState<File[]>([]);
  const [currentFile, setCurrentFile] = useState<File | null>(null);
  const [code, setCode] = useState<string>("// Sélectionnez ou créez un fichier");
  const [socket, setSocket] = useState<Socket | null>(null);
  const [fileContents, setFileContents] = useState<Record<string, string>>({});

  // Initialiser la connexion socket
  useEffect(() => {
    const socketInstance = io("http://localhost:3000", {
      reconnection: true,
      reconnectionAttempts: 5,
      reconnectionDelay: 1000,
    });

    socketInstance.on("connect", () => {
      console.log("Connecté au serveur Socket.IO");
    });

    // Gérer les mises à jour de fichiers en temps réel
    socketInstance.on(
      "file-update",
      ({ fileId, content }: { fileId: string; content: string }) => {
        setFileContents((prev) => ({
          ...prev,
          [fileId]: content,
        }));

        if (currentFile && currentFile._id === fileId) {
          setCode(content);
        }
      }
    );

    socketInstance.on("new-file", (newFile: File) => {
      setFiles((prev) => [...prev, newFile]);
      setFileContents((prev) => ({
        ...prev,
        [newFile._id]: newFile.content,
      }));
    });

    socketInstance.on("delete-file", (fileId: string) => {
      setFiles((prev) => prev.filter((file) => file._id !== fileId));
      setFileContents((prev) => {
        const updated = { ...prev };
        delete updated[fileId];
        return updated;
      });
    });

    setSocket(socketInstance);

    return () => {
      if (socketInstance) {
        socketInstance.disconnect();
      }
    };
  }, [currentFile]);

useCopilotReadable({
description: "État actuel de l'espace de travail",
value: {
    files: files.map((f) => f.name),
    currentFile: currentFile?.name,
    currentCode: code,
},
});

  const fetchFiles = async () => {
    try {
      const response = await fetch("/api/files");
      if (!response.ok) throw new Error("Échec de la récupération des fichiers");
      const data: File[] = await response.json();

      // Stocker tout le contenu des fichiers dans l'état
      const contents: Record<string, string> = {};
      data.forEach((file) => {
        contents[file._id] = file.content;
      });

      setFiles(data);
      setFileContents(contents);
    } catch (error) {
      console.error("Erreur lors de la récupération des fichiers :", error);
    }
  };

  useEffect(() => {
    fetchFiles();
  }, []);

  const handleFileSelect = async (file: File) => {
    setCurrentFile(file);

    // Utiliser le contenu mis en cache si disponible
    if (fileContents[file._id]) {
      setCode(fileContents[file._id]);
    } else {
      try {
        const response = await fetch(`/api/files/${file._id}`);
        if (!response.ok) throw new Error("Échec de la récupération du contenu du fichier");
        const data = await response.json();

        setFileContents((prev) => ({
          ...prev,
          [file._id]: data.content,
        }));
        setCode(data.content);
      } catch (error) {
        console.error("Erreur lors de la récupération du contenu du fichier :", error);
      }
    }
  };

  const handleCodeChange = async (value: string | undefined) => {
    if (!currentFile || !value) return;

    // Mettre à jour l'état local immédiatement
    setCode(value);
    setFileContents((prev) => ({
      ...prev,
      [currentFile._id]: value,
    }));

    try {
      // Émettre le changement aux autres clients
      if (socket) {
        socket.emit("file-update", {
          fileId: currentFile._id,
          content: value,
        });
      }

      // Sauvegarder dans le backend
      await fetch("/api/files", {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ id: currentFile._id, content: value }),
      });
    } catch (error) {
      console.error("Erreur lors de la mise à jour du fichier :", error);
    }
  };

  const processFiles = async ({ response }: { response: string }) => {
    try {
      const filePattern =
        /FILE:\s*([\w.\-\/]+)\s*\nCODE:\s*([\s\S]*?)(?=\nFILE:|$)/g;
      let match;
      const newFiles: File[] = [];

      while ((match = filePattern.exec(response)) !== null) {
        const fileName = match[1].trim();
        const fileContent = match[2].trim();

        if (fileName && fileContent) {
          const res = await fetch("/api/files", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ name: fileName, content: fileContent }),
          });

          if (res.ok) {
            const savedFile: File = await res.json();
            newFiles.push(savedFile);

            // Mettre à jour l'état local
            setFileContents((prev) => ({
              ...prev,
              [savedFile._id]: savedFile.content,
            }));

            // Émettre un nouveau fichier aux autres clients
            if (socket) {
              socket.emit("new-file", savedFile);
            }
          }
        }
      }

      setFiles((prevFiles) => [...prevFiles, ...newFiles]);
      return `Fichiers sauvegardés avec succès : ${newFiles
        .map((f) => f.name)
        .join(", ")}`;
    } catch (error) {
      console.error("Erreur lors du traitement des fichiers :", error);
      return "Échec de la sauvegarde des fichiers.";
    }
  };

  useCopilotAction({
    name: "processFiles",
    description: "Traite les fichiers générés par l'IA et les sauvegarde dans MongoDB",
    parameters: [{ name: "response", type: "string", required: true }],
    handler: processFiles,
  });

  return (
    <div className="h-screen flex bg-gray-100">
      <FileExplorer
        files={files}
        onFileSelect={handleFileSelect}
        currentFile={currentFile}
      />
      <div className="flex-1 flex flex-col p-4">
        <ScreenOne
          selectedFile={currentFile}
          code={code}
          onChange={handleCodeChange}
        />
      </div>
      <LivePreview
        files={files}
        currentFile={currentFile}
        code={code}
        onCodeChange={handleCodeChange}
      />
      <CopilotPopup
        instructions={`
    Vous êtes un générateur de code alimenté par l'IA. Utilisez les actions suivantes :

    1. @processFiles - Pour créer de nouveaux fichiers, utilisez ce format :
    @processFiles(response: \`
    FILE: filename.ext
    CODE:
    [contenu du fichier]
    \`)

    - Stockez les nouveaux fichiers dans MongoDB en utilisant /api/files.
    - Ensuite, récupérez immédiatement les fichiers de la base de données et affichez les fichiers dans FileExplorer
    - Classez et séparez correctement les différents types de fichiers :
      - Statiques : HTML, CSS, JS
      - React : JSX, JS (composants React)
    - Pour les projets React :
      - Assurez la présence de index.js comme point d'entrée.
      - Assurez-vous qu'il y a un fichier App.css pour le style
      - Assurez-vous que index.html contient une div root <div id="root"></div>.
      - Séparez correctement les composants (par exemple, App.js, Header.jsx).
      - Incluez un fichier package.json avec les dépendances React nécessaires.
      - Assurez-vous que tous les fichiers React suivent la syntaxe ES6+ et les meilleures pratiques React.

    2. @updateFile - Pour mettre à jour les fichiers existants :
    @updateFile(filename: "file.ext", content: "nouveau contenu")

    - Maintenez la compatibilité avec l'environnement React.
    - Assurez-vous que tout fichier mis à jour ne casse pas les imports existants.
  `}
        labels={{
          title: "Assistant de projet",
          initial: "Que souhaitez-vous créer ?",
        }}
      />
    </div>
  );
}

export default Page;
```

### Explication du code

1. **Gestion d'état** :

  * Suivi des fichiers (`files`), du fichier actuellement sélectionné (`currentFile`), du code dans le fichier sélectionné (`code`), du contenu des fichiers en temps réel (`fileContents`), et d'une connexion socket (`socket`).

2. [**Socket.IO**](http://Socket.IO) :

  * Établit une connexion à un serveur en utilisant [`Socket.IO`](http://Socket.IO), et gère les mises à jour de fichiers en temps réel comme la création, les mises à jour et les suppressions de fichiers.

  * Écoute les événements tels que `file-update`, `new-file`, et `delete-file` pour mettre à jour l'interface utilisateur et propager les changements entre les utilisateurs.

3. **Récupération des fichiers** :

  * Au montage du composant, il récupère tous les fichiers depuis une API et remplit l'état avec les fichiers et leur contenu.

  * Lors de la sélection d'un fichier, le contenu est soit récupéré depuis l'état mis en cache, soit récupéré depuis le serveur.

4. **Changements de code** :

  * Lorsque le code dans l'éditeur Monaco est mis à jour, le nouveau contenu est sauvegardé localement et envoyé au serveur et aux autres clients connectés via le socket.

5. **Traitement des fichiers par l'IA** :

  * Lorsque l'IA génère du code, la fonction `processFiles` analyse le contenu généré, crée des fichiers sur le backend, et met à jour le frontend. Ces fichiers sont stockés dans MongoDB et synchronisés avec le client via [Socket.IO](http://Socket.IO).

6. **Intégration de CopilotKit** :

  * Utilise le hook `useCopilotAction` pour intégrer la génération et la mise à jour de fichiers pilotés par l'IA.

  * Fournit des instructions pour créer et mettre à jour des fichiers via le `CopilotPopup`.

  * Donnez toujours des instructions détaillées au `CopilotPopup`.

7. **Composants UI** :

  * L'interface utilisateur comprend des composants comme `FileExplorer`, `ScreenOne`, et `LivePreview`, qui affichent les fichiers, permettent l'édition, et fournissent un aperçu en direct du code.

  * Le `CopilotPopup` agit comme un assistant pour guider l'IA dans la génération ou la mise à jour de fichiers.

Cette configuration crée un environnement d'édition de code collaboratif en temps réel avec support pour les projets statiques et basés sur React.

### **Configurer CopilotKit pour toute l'application**

Ceci sera la dernière étape de la construction de l'application. Accédez au fichier `layout.tsx` et ajoutez ce code :

```jsx
import { CopilotKit } from "@copilotkit/react-core";
import "./globals.css";
import "@copilotkit/react-ui/styles.css";
import { ReactNode } from "react";

export const metadata = {
  title: "Clone de Replit",
  description: "Clone de Replit avec Copilotkit",
};

// Définir le type de props pour RootLayout
interface RootLayoutProps {
  children: ReactNode;
}

export default function RootLayout({ children }: RootLayoutProps) {
  return (
    <html lang="en">
      <body>
        <CopilotKit runtimeUrl="/api/copilotkit">{children}</CopilotKit>
      </body>
    </html>
  );
}
```

Voici ce qui se passe dans ce code :

Ce code définit un composant `RootLayout`, qui sert de mise en page racine pour une application Next.js. Voici une brève explication :

### **Fonctionnalités clés** :

1. **Intégration de CopilotKit** :

  * Enveloppe toute l'application avec le composant `CopilotKit` de `@copilotkit/react-core`.

  * Configure le `runtimeUrl` sur `/api/copilotkit`, qui est le point de terminaison pour gérer les fonctionnalités liées à Copilot.

2. **Styles globaux** :

  * Importe les styles CSS globaux (`globals.css`) et les styles d'interface utilisateur de CopilotKit (`@copilotkit/react-ui/styles.css`).

3. **Métadonnées** :

  * Définit les métadonnées pour l'application (titre : `"Clone de Replit"`, description : `"Clone de Replit avec Copilotkit"`).

4. **Structure de la mise en page** :

  * Utilise les balises `html` et `body` pour structurer le document.

  * Rend les `children` (le reste de l'application) à l'intérieur de l'enveloppe `CopilotKit`.

### **Quelques notes importantes**

La conception et le déploiement d'une base de données peuvent varier en fonction des outils et des exigences. Pour ce projet, j'ai choisi l'approche la plus simple et la plus accessible.

### **Pourquoi CopilotKit ?**

CopilotKit est un outil puissant qui convertit les requêtes de traitement du langage naturel (NLP) en code backend exécutable qui s'exécute sur le modèle LLM de Meta. Si vous avez une alternative qui sert un objectif similaire, n'hésitez pas à l'utiliser. Il comble efficacement le fossé entre l'entrée en langage naturel et l'exécution technique, ce qui en fait un choix idéal pour des projets comme celui-ci.

### **Pourquoi GroqCloud ?**

J'ai sélectionné GroqCloud car il est gratuit et offre un accès à plusieurs grands modèles de langage (LLM) avec une seule clé API. Bien que des alternatives comme ChatGPT soient disponibles, elles peuvent nécessiter des plans payants. La polyvalence et l'abordabilité de GroqCloud en font le choix parfait pour ce tutoriel.

### **Bonnes pratiques de sécurité**

Ne jamais exposer vos informations d'identification publiquement. Stockez toujours les informations sensibles comme les clés API dans un fichier `.env` pour garder votre projet sécurisé.

### **Améliorations futures**

Bien que ce tutoriel se concentre sur la configuration et le travail avec des fichiers React, CopilotKit a une gamme de capacités beaucoup plus large que je vais expliquer dans les prochains articles de blog.

Je vise à construire au moins 15 produits IA en 2025.

Le support pour les fichiers statiques arrive bientôt.

Comme promis dans le tutoriel précédent, j'ai implémenté la fonctionnalité CRUD de CopilotKit dans ce tutoriel également.

Dans mon prochain tutoriel, je vais démontrer comment construire quelque chose de plus cool avec CopilotKit pour créer une application plus dynamique et fonctionnelle.

## **Jouer avec le clone de Replit**

Vous pouvez explorer le projet en direct via le lien suivant et demander au chatbot de construire quelque chose en React. [Lien du projet en direct](https://replit-mongodb.vercel.app/).

Pour une compréhension plus approfondie du code, consultez le dépôt GitHub ici : [Dépôt GitHub](https://github.com/prankurpandeyy/replit-mongodb).

Voici également une capture d'écran montrant son utilisation pratique. Dans cet exemple, au lieu de créer manuellement des fichiers de projet, vous pouvez simplement demander au chatbot **CopilotKit** de générer ces fichiers pour vous. Vous pouvez ensuite les modifier et jouer avec eux.

Par exemple, vous pouvez donner des commandes au chatbot CopilotKit comme : "Créer une application React".

### Gestion des erreurs

* **Retards de l'explorateur de fichiers** : Parfois, en raison de problèmes de base de données ou de déploiement Vercel, les fichiers peuvent être générés mais ne pas être immédiatement visibles dans l'explorateur de fichiers. Dans de tels cas, il suffit de rafraîchir la page et les composants manquants apparaîtront. Cela s'applique à toutes les opérations CRUD sur les fichiers et leur contenu également.

* **Sauvegarde en temps réel** : Toutes les modifications que vous apportez aux fichiers sont sauvegardées dans la base de données en temps réel, garantissant que votre travail n'est jamais perdu.

* **Erreurs de commande** : Si le chatbot affiche une erreur lors du traitement de vos commandes, réessayez simplement la commande jusqu'à ce que vous receviez une réponse.

* **Ajout de fichiers supplémentaires** : Pour ajouter de nouveaux fichiers au projet actuel, demandez simplement au chatbot :

  * "Ajoutez un nouveau fichier au projet actuel avec le nom de fichier et l'extension."

  Par exemple : "Ajoutez un nouveau fichier nommé `readme.md` dans ce projet"

### Démo vidéo

%[https://youtu.be/AjnzEDmiu2Y?si=1gMq19hzoFVQDgNy]

## **Conclusion**

J'espère que vous avez apprécié la construction de ce simple clone de Replit alimenté par l'IA. Dans ce projet, nous avons utilisé une base de données MongoDB, mais l'approche peut facilement être appliquée à d'autres bases de données, tant que vous pouvez récupérer les données.

Je prévois de créer de nombreux autres projets impliquant l'IA et d'autres outils de pointe. L'IA est vraiment un changement de jeu dans le domaine des TI, et je suis ravi de partager plus d'informations et d'implémentations pratiques des dernières technologies.

C'est tout de mon côté. Si vous avez trouvé cet article utile, n'hésitez pas à le partager et à me contacter. Je suis toujours ouvert à de nouvelles opportunités :

* Suivez-moi sur X : [Twitter de Prankur](https://x.com/prankurpandeyy)

* Connectez-vous avec moi sur LinkedIn : [LinkedIn de Prankur](https://linkedin.com/in/prankurpandeyy)

* Suivez-moi sur Github : [Github de Prankur](https://github.com/prankurpandeyy)

* Consultez mon portfolio : [Portfolio de Prankur](https://prankurpandeyy.netlify.app/)