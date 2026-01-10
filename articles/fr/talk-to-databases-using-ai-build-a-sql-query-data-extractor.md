---
title: Comment parler à n'importe quelle base de données en utilisant l'IA – Construisez
  votre propre extracteur de données de requêtes SQL
subtitle: ''
author: Prankur Pandey
co_authors: []
series: null
date: '2025-01-08T21:52:12.212Z'
originalURL: https://freecodecamp.org/news/talk-to-databases-using-ai-build-a-sql-query-data-extractor
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1733842504544/0e9da173-718c-454e-841c-15c148e0fe93.jpeg
tags:
- name: AI
  slug: ai
- name: Databases
  slug: databases
- name: SQL
  slug: sql
- name: projects
  slug: projects
seo_title: Comment parler à n'importe quelle base de données en utilisant l'IA – Construisez
  votre propre extracteur de données de requêtes SQL
seo_desc: 'Recently, I took a break from writing to focus on my exams. During this
  time, I had an interesting experience: I had the chance to explain SQL (Structured
  Query Language) to my peers. While exploring SQL in-depth, I encountered a common
  frustration: ...'
---

Récemment, j'ai fait une pause dans l'écriture pour me concentrer sur mes examens. Pendant cette période, j'ai eu une expérience intéressante : j'ai eu l'occasion d'expliquer SQL (Structured Query Language) à mes pairs. En explorant SQL en profondeur, j'ai rencontré une frustration courante : l'écriture de requêtes SQL pour récupérer des données spécifiques à partir d'une base de données.

Cela a déclenché une idée. Et si je pouvais construire un outil où je n'aurais pas à écrire de requêtes SQL manuellement ? Au lieu de cela, je pourrais taper en anglais naturel et simple et laisser la base de données faire le travail pour moi.

Étant donné que nous vivons à l'ère de l'IA, l'utilisation de l'intelligence artificielle était la seule façon de transformer cette vision en réalité.

Dans ce tutoriel, je vais vous guider à travers la création d'un extracteur de données de requêtes SQL alimenté par l'IA. Cet outil vous permettra de récupérer des données à partir d'une base de données sans effort, sans écrire une seule ligne de code SQL.

### **Ce que nous allons couvrir :**

* [Prérequis & Outils](#heading-prerequisiteshttpswwwfreecodecamporgnewsreact-best-practices-ever-developer-should-knowheading-prerequsites-amp-tools)
    
* [Comment fonctionne l'application](#heading-how-does-the-app-work)?
    
* [Comment configurer vos outils](#heading-how-to-set-up-your-tools)
    
* [Comment configurer la base de données](#heading-how-to-set-up-the-database)
    
* [Structure et fonctionnalités de l'application](#heading-structure-and-features-of-the-app)
    
* [Comment construire le backend](#heading-how-to-build-the-back-end)
    
* [Comment construire le frontend](#heading-how-to-build-the-front-end)
    
* [Quelques notes importantes](#heading-some-important-notes)
    
* [Jouer avec la base de données](#heading-playing-with-the-database)
    
* [Conclusion](#heading-conclusion)
    

## Prérequis & Outils

Dans ce tutoriel, nous allons construire un outil d'extraction de données de requêtes SQL alimenté par l'IA. Il nous permettra d'interagir avec une base de données en utilisant le langage naturel, comme l'anglais simple, et de recevoir les mêmes résultats que si nous avions écrit des requêtes SQL.

Voici un aperçu des outils que nous allons utiliser pour créer cette application cool :

### Base de données

La base de données est un composant critique où nous allons stocker des données et les extraire plus tard pour que notre modèle d'IA les utilise lors de l'exécution d'opérations NLP. Au lieu d'héberger une base de données localement, j'ai choisi une base de données cloud gratuite qui permet l'extraction de données via des API REST. Pour ce projet, j'ai opté pour [restdb.io](http://restdb.io) car il offre une provision de base de données SQL transparente et prend en charge les API REST.

### Agent IA

Un agent IA servira d'intermédiaire entre la base de données et le modèle IA. Cet agent gérera les opérations du modèle IA et facilitera la communication transparente. Pour cela, j'utilise [**CopilotKit**](https://www.copilotkit.ai/), qui simplifie le processus d'intégration.

### Modèle IA (LLM)

Le modèle IA traduit les requêtes en anglais simple en requêtes SQL. Pour cela, j'utilise [**GroqAI**](https://groq.com/), qui prend en charge divers modèles IA populaires et offre la flexibilité nécessaire pour ce projet.

### Next.js

Pour développer une application web qui prend en charge les fonctionnalités frontend et backend, j'ai choisi **Next.js**. C'est un framework idéal pour construire des applications web robustes et évolutives avec des capacités de rendu côté serveur.

### Déploiement

Pour le déploiement, vous pouvez choisir n'importe quel service. Je préfère **Vercel**, car il s'intègre parfaitement avec Next.js et est gratuit pour les projets hobby.

En combinant ces outils, nous allons construire une application puissante et conviviale qui relie de manière transparente le langage naturel et les bases de données SQL.

## Ce que nous allons faire ici :

Voici les étapes que nous allons suivre dans ce tutoriel pour construire notre application :

**Étape 1 – Configurer la base de données :** Configurer la base de données localement, la déployer et y accéder, ou utiliser un outil de base de données en ligne qui permet l'accès et l'extraction de données via des API REST.

**Étape 2 – Obtenir les clés API cloud :** Obtenir les clés API nécessaires pour votre modèle IA afin de permettre une intégration transparente.

**Étape 3 – Construire une application web :** Créer une application web et configurer le backend pour intégrer CopilotKit. Le configurer dans l'application pour une fonctionnalité optimale.

**Étape 4 – Former CopilotKit sur votre base de données :** Fournir les données de votre base de données à CopilotKit. Il lira et comprendra les données pour faciliter le traitement du langage naturel.

**Étape 5 – Intégrer le chat CopilotKit :** Ajouter l'interface de chat CopilotKit dans votre application et la configurer pour assurer un fonctionnement fluide.

**Étape 6 – Tester localement :** Tester l'application sur votre machine locale pour identifier et corriger les problèmes.

**Étape 7 – Déployer l'application :** Une fois que tout fonctionne comme prévu, déployer l'application sur une plateforme d'hébergement.

## Comment fonctionne l'application ?

Vous êtes-vous déjà demandé comment écrire en anglais simple pourrait vous permettre de récupérer des données à partir d'une base de données SQL ?

La magie réside dans CopilotKit. Il vous permet de créer des copilotes alimentés par l'IA qui peuvent effectuer des opérations sur vos applications. Considérez CopilotKit comme votre assistant IA personnel ou chatbot. Alors, comment cela fonctionne-t-il ?

Eh bien, nous avons d'abord CopilotKit qui sert de chatbot alimenté par des modèles IA avancés.

Ensuite, lorsque vous fournissez des données au chatbot, il utilise ces données pour se former, construisant une compréhension de la structure et du contenu de votre base de données.

Enfin, lorsqu'une requête en langage naturel (comme "Qui utilise cette adresse e-mail ?") est saisie, le modèle IA la traite, la traduit en une requête SQL correspondante et récupère les données souhaitées à partir de la base de données.

Avec les puissantes capacités IA de CopilotKit, votre application peut relier de manière transparente le langage naturel et SQL, rendant les interactions avec la base de données plus intuitives.

## Comment configurer vos outils

Maintenant, nous allons passer en revue tout ce dont vous avez besoin pour configurer le projet.

### **1. Installer Next.js et les dépendances :**

Tout d'abord, vous devrez créer une application NextJS. Allez dans le terminal et exécutez la commande suivante :

```plaintext
npx create-next-app@latest my-next-app
```

Remplacez `my-next-app` par le nom de projet souhaité.

Accédez au dossier du projet :

```plaintext
cd my-next-app
```

Démarrez le serveur de développement :

```plaintext
npm run dev
```

Ouvrez votre navigateur et accédez à [`http://localhost:3000`](http://localhost:3000) pour voir votre application Next.js en action.

### **2. Installer CopilotKit et les dépendances**

Accédez au dossier racine du projet via le terminal et exécutez la commande ci-dessous. Elle installera toutes les dépendances importantes de CopilotKit et d'autres packages importants comme dotenv et Axios.

```plaintext
npm install @copilotkit/react-ui @copilotkit/react-core dotenv axios
```

* La dépendance **CopitlotKit** est uniquement pour la gestion des opérations et configurations de CopilotKit.
    
* La dépendance **Dotenv** est utilisée pour gérer les variables d'environnement, car nous devons garder les clés importantes dans le projet, telles que les variables d'environnement.
    
* **Axios** est pour la gestion des appels API.
    

### **3. Configurer la base de données**

Visitez [RestDB.io](http://RestDB.io) et connectez-vous ou créez un compte.

![page de connexion restdb.io ](https://cdn.hashnode.com/res/hashnode/image/upload/v1736349488854/435a5574-54b8-40b4-a1e5-f31aa79eeae8.png align="center")

Ci-dessus, vous pouvez voir la page de connexion pour RestDB.io, vous pouvez soit vous connecter si vous avez déjà un compte, soit créer un nouveau compte.

Une fois connecté, vous serez redirigé vers cette page. Là, vous verrez le bouton pour créer une nouvelle base de données.

![page de création de base de données restdb.io ](https://cdn.hashnode.com/res/hashnode/image/upload/v1736349634003/840cc3d6-c7e0-474f-9335-eca750aeacc5.png align="center")

Lorsque vous cliquez sur le bouton Créer, une fenêtre contextuelle apparaîtra. Là, vous devrez entrer le nom de la base de données comme montré dans l'image ci-dessous :

![fenêtre contextuelle de création de base de données restdb.io](https://cdn.hashnode.com/res/hashnode/image/upload/v1736349886708/c9846627-4351-40e0-a4bd-8342b6b5bf25.png align="center")

Lorsque vous entrez le nom de la base de données, cliquez ensuite sur "Go". J'ai mis **demosql** comme nom de la base de données. À ce stade, vous obtiendrez le lien de votre base de données nouvellement créée comme montré dans l'image ci-dessous :

![page de liste des bases de données restdb.io](https://cdn.hashnode.com/res/hashnode/image/upload/v1736350379651/27708c52-c8a0-405c-93d7-374833572007.png align="center")

Maintenant, cliquez sur l'URL de la base de données, cela vous mènera à cette page montrée dans l'image :

![page principale de la base de données restdb.io ](https://cdn.hashnode.com/res/hashnode/image/upload/v1736350576835/87abd648-1b8d-4d07-b30a-6f1076abdf06.png align="center")

Il est maintenant temps de créer une clé API pour accéder à la base de données. Pour ce faire, cliquez sur **Paramètres** et cela vous mènera à une nouvelle page montrée ci-dessous :

![page des paramètres de l'API restdb.io ](https://cdn.hashnode.com/res/hashnode/image/upload/v1736352142460/d61be8ac-c78f-4c71-a1f0-dbc230496bc5.png align="center")

Sur cette page, cliquez sur le bouton **Ajouter** et cela ouvrira une fenêtre contextuelle montrée ci-dessous dans l'image :

![fenêtre contextuelle de création de clé API restdb.io](https://cdn.hashnode.com/res/hashnode/image/upload/v1736352445417/b739b25d-e01d-4b72-b4a6-db3077866a60.png align="center")

Vous pouvez maintenant configurer vos actions API ici comme GET, POST, PUT et DELETE, lui donner le nom que vous voulez et l'enregistrer. Votre base de données est maintenant prête à interagir via l'API REST.

Copiez l'URL de la base de données et la clé API et placez-les dans le fichier .env.

Vous pouvez ajouter des tables, définir le schéma avec des colonnes et des types de données (par exemple, VARCHAR, INTEGER), et remplir les données manuellement ou via des téléchargements (Excel, CSV ou JSON). Pour ce projet, nous avons ajouté 21 enregistrements.

### 4. Configurer le LLM pour l'action :

Cette partie est cruciale pour le projet, car nous configurons le LLM (Large Language Model) pour gérer la conversion des requêtes NLP (anglais simple) en requêtes SQL.

De nombreux LLM sont disponibles sur le marché, chacun avec ses forces. Certains sont gratuits, d'autres payants, ce qui a rendu le choix du bon pour ce projet un défi.

Après de nombreuses expérimentations, j'ai choisi l'**Adaptateur Groq** car :

* Il consolide divers LLM sous une seule plateforme.
    
* Il fournit un accès via une clé API unifiée.
    
* Il est compatible avec CopilotKit.
    

#### Comment configurer Groq Cloud

Pour commencer avec Groq Cloud, [visitez son site web](https://console.groq.com/login) et connectez-vous si vous avez déjà un compte ou créez un nouveau compte si vous êtes nouveau. Une fois connecté, accédez au tableau de bord Groq.

C'est la page d'accueil de groq cloud :

![page d'accueil de groq cloud](https://cdn.hashnode.com/res/hashnode/image/upload/v1736352733541/92012af5-b3c4-4277-a50f-834c1900a2de.png align="center")

Une fois connecté, une nouvelle page s'ouvrira qui ressemblera à ceci :

![page du tableau de bord de groq cloud ](https://cdn.hashnode.com/res/hashnode/image/upload/v1736353229314/67313c60-47b8-4f23-b3c0-e46fcdd5201a.png align="center")

Comme vous pouvez le voir, la barre latérale contient un lien Clés API. Cliquez dessus, et cela ouvrira une nouvelle page comme montré dans l'image ci-dessous. Vous pouvez également sélectionner n'importe quel LLM de votre choix qui est donné en haut à droite avant l'option de visualisation du code.

![section API groqcloud](https://cdn.hashnode.com/res/hashnode/image/upload/v1736353347970/3406fa54-ddc2-4a00-8b27-22536486fc64.png align="center")

Ici, cliquez sur le bouton Créer une clé API, cela ouvrira une fenêtre contextuelle comme vous le voyez ci-dessous. Entrez simplement le nom de votre clé API et cliquez sur Soumettre, cela créera une nouvelle clé API pour vous. Copiez ensuite cette clé API et collez-la dans votre fichier .env.

![page de création de clé API groq cloud ](https://cdn.hashnode.com/res/hashnode/image/upload/v1736353563741/cd1a185a-2c77-470a-a5ce-eca564cf524a.png align="center")

Pour permettre un accès transparent à divers LLM sur Groq Cloud, générez une clé API en allant dans la section Clés API Groq. Créez une nouvelle clé API spécifiquement pour le LLM, en veillant à ce qu'elle soit correctement configurée.

Avec le LLM configuré et tous les composants prêts, vous êtes maintenant prêt à construire le projet.

## Structure et fonctionnalités de l'application

Nous allons aborder ce projet de manière simple, en nous concentrant sur la simplicité et la fonctionnalité. L'objectif principal est de créer une page web de base qui nous permet de :

* Vérifier si nos appels API ont réussi.
    
* Voir les données reçues de l'API.
    
* Interagir avec le chatbot CopilotKit intégré à l'interface utilisateur.
    

### Structure de la page web

Puisque nous avons déjà configuré l'**application Next.js**, l'étape suivante consiste à construire une page web minimaliste comprenant :

1. **Section d'en-tête :** Affiche le titre de l'application.
    
2. **Zone principale :**
    
    * **Tableaux :** Affichent les données récupérées de la base de données.
        
    * **Indicateurs de statut :** Affichent le statut des appels API et des opérations de la base de données. Si des problèmes surviennent, tels que des échecs d'API ou de base de données, les erreurs seront affichées en **texte rouge** pour plus de clarté.
        

### Fonctionnalités clés

* **Gestion des erreurs :** Tout échec, tel que des problèmes d'API ou de base de données, sera clairement marqué en texte rouge pour une visibilité immédiate.
    
* **Présentation des données :** À des fins de démonstration, l'ensemble de la base de données sera affiché dans des tableaux bien structurés.
    
* **Intégration du chatbot CopilotKit :** Ce chatbot sera configuré pour permettre des interactions en langage naturel avec la base de données. La **balle de couleur bleue** sur la page représente le **chatbot CopilotKit**. Ce chatbot est l'interface clé pour interagir avec la base de données.
    
    * En utilisant des requêtes en langage naturel, nous pouvons poser des questions sur les données de la base de données.
        
    * Le chatbot traite ces requêtes, les convertit en requêtes SQL et récupère les résultats de manière transparente.
        

Le frontend ressemblera à quelque chose comme ceci :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1734711368585/db3bd5fb-fee1-42a3-a638-b5b410c6fe69.png align="center")

## Comment construire le backend

Avant de commencer à construire le backend, vous devrez mettre toutes les informations d'identification importantes dans votre fichier **.env** qui ressemblera à quelque chose comme ceci :

```plaintext
NEXT_PUBLIC_COPILOTKIT_BACKEND_URL=http://localhost:3000/api/copilotkit
NEXT_PUBLIC_GROQ_CLOUD_API_KEY=
NEXT_PUBLIC_RESTDB_API_KEY=
NEXT_PUBLIC_RESTDB_BASE_URL=https://demosql-fdcb.restdb.io/rest/demo-data 
```

Alors, que sont toutes ces variables ? Passons-les en revue une par une :

1. `NEXT_PUBLIC_COPILOTKIT_BACKEND_URL=`[`http://localhost:3000/api/copilotkit`](http://localhost:3000/api/copilotkit) : Cela spécifie l'URL de base pour l'API backend de CopilotKit.
    
    * Le préfixe `NEXT_PUBLIC_` rend cette variable accessible à la fois côté serveur et côté client dans une application Next.js.
        
    * La valeur [`http://localhost:3000/api/copilotkit`](http://localhost:3000/api/copilotkit) indique que l'API s'exécute localement pendant le développement.
        
2. `NEXT_PUBLIC_GROQ_CLOUD_API_KEY=` : Cette variable est destinée à stocker une clé API pour un service GROQ Cloud. GROQ Cloud pourrait être lié à l'interrogation ou au traitement de données, vous devrez coller votre propre clé API Groq.
    
    * La variable est vide, indiquant que la clé API n'est pas encore définie. Elle devra probablement être remplie avec la valeur appropriée avant que l'application ne puisse accéder au service GROQ Cloud.
        
3. `NEXT_PUBLIC_RESTDB_API_KEY=` : Destinée à contenir la clé API pour accéder à un service **RESTdb**. Vous devrez coller votre propre clé API Groq.
    
    * RESTdb est un service de base de données qui fournit des API pour les interactions avec la base de données.
        
    * La variable est également vide, ce qui signifie que la clé doit être remplie avec une clé API valide pour que l'application puisse s'authentifier et interagir avec le service RESTdb.
        
4. `NEXT_PUBLIC_RESTDB_BASE_URL=`[`https://demosql-fdcb.restdb.io/rest/demo-data`](https://demosql-fdcb.restdb.io/rest/demo-data) : Définit l'URL de base pour interagir avec la base de données RESTdb. Cette URL sera créée lorsque vous créerez votre base de données. Ici, j'ai donné l'URL de ma base de données.
    
    * La valeur [`https://demosql-fdcb.restdb.io/rest/demo-data`](https://demosql-fdcb.restdb.io/rest/demo-data) pointe vers un point de terminaison spécifique de la base de données RESTdb appelé `demo-data`.
        
    * Ce pourrait être le point de terminaison où l'application récupère ou manipule des données de démonstration pour les tests ou le développement.
        

Nous avons ajouté avec succès les variables d'environnement à notre projet. Maintenant, il est temps de configurer le backend de l'API CopilotKit.

### Comment configurer le backend CopilotKit

Ouvrez votre application Next.js dans n'importe quel éditeur de code - je préfère VSCode - et allez dans le dossier racine, qui ressemble à ceci :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1734968233629/f338c977-02dd-4ee1-ae66-7417f03e026b.png align="center")

À l'intérieur du dossier de l'application, créez un nouveau dossier appelé `api`. À l'intérieur du dossier API, créez un autre dossier appelé `copilotkit`. Ensuite, créez un nouveau fichier appelé `route.js` et collez ce code à l'intérieur du fichier :

```javascript
import {
  CopilotRuntime,
  GroqAdapter,
  copilotRuntimeNextJSAppRouterEndpoint,
} from "@copilotkit/runtime";

import Groq from "groq-sdk";

const groq = new Groq({ apiKey: process.env.NEXT_PUBLIC_GROQ_CLOUD_API_KEY });
console.log(process.env.NEXT_PUBLIC_GROQ_CLOUD_API_KEY);
const copilotKit = new CopilotRuntime();

const serviceAdapter = new GroqAdapter({
  groq,
  model: "llama-3.1-70b-versatile",
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

Ce code définit un gestionnaire côté serveur pour une route API Next.js en utilisant les SDK CopilotKit et Groq. Il configure un environnement d'exécution pour traiter les requêtes vers un point de terminaison spécifié.

**1. Imports :**

```javascript
import {
  CopilotRuntime,
  GroqAdapter,
  copilotRuntimeNextJSAppRouterEndpoint,
} from "@copilotkit/runtime";

import Groq from "groq-sdk";
```

* `CopilotRuntime` et `GroqAdapter` : Ce sont des classes de la bibliothèque CopilotKit utilisées pour configurer et configurer l'environnement d'exécution et les adaptateurs pour les services basés sur l'IA.
    
    * `CopilotRuntime` : Un environnement d'exécution pour gérer les opérations CopilotKit.
        
    * `GroqAdapter` : Adapte et connecte un service Groq (utilisé pour l'interrogation ou le traitement des données) avec CopilotKit.
        
* `copilotRuntimeNextJSAppRouterEndpoint` : Une fonction utilitaire pour créer un gestionnaire pour un point de terminaison API Next.js App Router qui intègre CopilotKit.
    
* `Groq` de `"groq-sdk"` : Une bibliothèque pour interagir avec les services Groq est initialisée ici pour l'interrogation ou le traitement des données.
    

**2. Initialiser Groq :**

```javascript
const groq = new Groq({ apiKey: process.env.NEXT_PUBLIC_GROQ_CLOUD_API_KEY });
console.log(process.env.NEXT_PUBLIC_GROQ_CLOUD_API_KEY);
```

* Initialisation de `Groq` :
    
    * L'objet `Groq` est créé avec une clé API (`NEXT_PUBLIC_GROQ_CLOUD_API_KEY`) récupérée à partir des variables d'environnement.
        
    * Cette clé authentifie l'application avec le service Groq Cloud.
        
* `console.log(`[`process.env.NEXT`](http://process.env.NEXT)`_PUBLIC_GROQ_CLOUD_API_KEY)` : Journalise la clé API dans la console du serveur. **Note :** Évitez de journaliser les données sensibles en production pour garantir la sécurité.
    

**3. Initialiser l'environnement d'exécution CopilotKit**

```javascript
const copilotKit = new CopilotRuntime();
```

* Initialisation de `CopilotRuntime` : Crée une instance de l'environnement d'exécution de CopilotKit pour gérer les fonctionnalités et services de CopilotKit.
    

**4. Configurer l'adaptateur de service**

```javascript
const serviceAdapter = new GroqAdapter({
  groq,
  model: "llama-3.1-70b-versatile",
});
```

* `GroqAdapter` :
    
    * Configure un adaptateur pour connecter CopilotKit avec Groq.
        
    * Le paramètre `model` spécifie le modèle IA à utiliser. Ici, il s'agit de `"llama-3.1-70b-versatile"`, un modèle de langage polyvalent avec 70 milliards de paramètres.
        

**5. Gestionnaire POST exporté**

```javascript
export const POST = async (req) => {
  const { handleRequest } = copilotRuntimeNextJSAppRouterEndpoint({
    runtime: copilotKit,
    serviceAdapter,
    endpoint: "/api/copilotkit",
  });

  return handleRequest(req);
};
```

* Définit un gestionnaire `POST` pour un point de terminaison API Next.js App Router.
    
* **Composants clés :**
    
    1. `copilotRuntimeNextJSAppRouterEndpoint` :
        
        * Configure le gestionnaire pour le point de terminaison `/api/copilotkit`.
            
        * Prend `runtime` (CopilotKit) et `serviceAdapter` (GroqAdapter) en entrées pour configurer le comportement du point de terminaison.
            
    2. `handleRequest` :
        
        * Une fonction qui traite les requêtes HTTP entrantes (dans ce cas, les requêtes `POST`).
            
        * Cela permet à l'environnement d'exécution CopilotKit et à l'adaptateur de service de traiter les requêtes de manière dynamique.
            
* `return handleRequest(req);` : Invoque le gestionnaire et traite la requête entrante (`req`), retournant la réponse appropriée.
    

Comment tout cela fonctionne :

1. Le SDK Groq est initialisé avec une clé API pour l'authentification.
    
2. Un environnement d'exécution CopilotKit est configuré.
    
3. Un GroqAdapter connecte l'environnement d'exécution au service Groq avec un modèle IA spécifié.
    
4. Le point de terminaison `/api/copilotkit` est configuré pour gérer les requêtes POST, transmettre les requêtes à l'environnement d'exécution de CopilotKit et retourner la réponse traitée.
    

Avec cette configuration, vous avez intégré avec succès CopilotKit dans votre application Next.js. Le backend est maintenant entièrement fonctionnel, permettant une communication transparente avec la base de données via les API REST et l'interface CopilotKit.

## Comment construire le frontend

Pour le frontend, nous allons le garder aussi simple que possible. Nous avons juste besoin de quelques éléments pour mener à bien ce projet : nous avons besoin d'un composant Header et d'un composant Table.

1. **Composant Header** : Pour afficher le titre ou la description de l'application.
    
2. **Composant Table** : Pour visualiser les données récupérées de la base de données.
    

Pour y parvenir, nous allons utiliser ShadCN, une bibliothèque de composants frontend populaire connue pour son design épuré et sa facilité d'utilisation.

ShadCN fournit des composants préconstruits qui aident à accélérer le développement sans compromettre la qualité. En utilisant cette bibliothèque, nous pouvons nous concentrer sur la fonctionnalité tout en garantissant que l'interface utilisateur semble polie et professionnelle.

### **Comment installer ShadCN dans un projet Next**

Exécutez la commande suivante pour installer les composants ShadCN :

```javascript
npx shadcn@latest init
```

Cette commande :

* Initialise ShadCN dans votre projet.
    
* Crée un dossier `components` pour stocker les composants ShadCN.
    
* Met à jour le fichier `tailwind.config.js` avec les configurations requises.
    

Vous serez invité à répondre à quelques questions pour configurer `components.json` :

```bash
Quel style souhaitez-vous utiliser ?  New York
Quelle couleur souhaitez-vous utiliser comme couleur de base ?  Zinc
Souhaitez-vous utiliser des variables CSS pour les couleurs ?  non / oui
ajouter des composants
```

Pour ajouter des composants spécifiques, utilisez la commande suivante :

```bash
npx shadcn@latest add <nom-du-composant>
```

Par exemple, pour ajouter un composant de tableau :

```bash
npx shadcn@latest add table
```

Le dossier `components` contient maintenant un composant `button` prêt à l'emploi.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1734970231792/2e5ea193-f829-435e-b4dc-68bd8ce793ca.png align="center")

Dans le frontend, nous avons un dossier `components` qui contient le composant Table. Ce composant est responsable de l'affichage des données de la base de données dans un format tabulaire structuré.

En plus du composant `Table`, il y a deux fichiers supplémentaires dans le frontend. Ces fichiers servent à des fins différentes et seront intégrés plus tard dans le projet pour des fonctionnalités spécifiques.

Cette structure modulaire garantit que le frontend reste propre et organisé, ce qui facilite sa gestion et son expansion si nécessaire.

Explorons chaque fichier :

1. **Table.jsx :** Ce fichier est généré automatiquement par ShadCN lorsque nous avons installé le composant Table. Il contient la configuration par défaut pour le composant de tableau fourni par la bibliothèque ShadCN. **Ne modifiez pas ce fichier**, car il est essentiel pour le bon fonctionnement du composant.
    
2. **Tabledata.jsx :** Ce fichier est celui où nous remplissons le tableau avec les données récupérées de la base de données via des appels API. Le fichier `Tabledata.jsx` fait le pont entre l'API backend et l'affichage du tableau frontend.
    

Examinons de plus près le code :

```javascript
import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableFooter,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

export function Tabledata({ data }) {
  return (
    <Table className="text-center">
      <TableCaption className="text-sm text-green-600 font-bold ml-8">
        Données en direct de la base de données.
      </TableCaption>
      <TableHeader>
        <TableRow className="text-center ">
          <TableHead>Id</TableHead>
          <TableHead>nom</TableHead>
          <TableHead>email</TableHead>
          <TableHead>numéro de téléphone</TableHead>
          <TableHead>adresse</TableHead>
          <TableHead>ville</TableHead>
          <TableHead>état</TableHead>
          <TableHead>code postal</TableHead>
          <TableHead>pays</TableHead>
          <TableHead className="text-right">créé à </TableHead>
        </TableRow>
      </TableHeader>
      <TableBody>
        {data.map((db) => (
          <TableRow key={db._id}>
            <TableCell className="font-medium text-wrap w-12">
              {db._id}
            </TableCell>
            <TableCell className="font-medium">{db.name}</TableCell>
            <TableCell>{db.email}</TableCell>
            <TableCell>{db.phone_number}</TableCell>
            <TableCell className="text-right">{db.address}</TableCell>
            <TableCell className="text-right">{db.city}</TableCell>{" "}
            <TableCell className="text-right">{db.state}</TableCell>
            <TableCell className="text-right">{db.zip_code}</TableCell>{" "}
            <TableCell className="text-right">{db.country}</TableCell>
            <TableCell className="text-right">{db.created_at}</TableCell>
          </TableRow>
        ))}
      </TableBody>
    </Table>
  );
}
```

Ce code rend un tableau stylisé et dynamique avec des données provenant d'une base de données ou d'une API.

* **Imports** : Utilise des composants de tableau personnalisés (`Table`, `TableRow`, `TableCell`, etc.) à partir de `@/components/ui/table`.
    
* **Props** : Accepte une prop `data`, un tableau d'objets représentant les lignes du tableau.
    
* **Légende du tableau** : Affiche une légende, "Données en direct de la base de données", stylisée avec Tailwind CSS.
    
* **En-tête du tableau** : Définit les en-têtes de colonne tels que `Id`, `nom`, `email`, etc.
    
* **Lignes dynamiques** : Parcourt le tableau `data` pour générer des éléments `TableRow` de manière dynamique, en utilisant `_id` comme clé unique.
    
* **Cellules de données** : Affiche les champs d'objet (`_id`, `name`, `email`, etc.) dans des composants `TableCell` avec des styles personnalisés.
    
* **Tailwind CSS** : Styles appliqués pour l'alignement, le poids de la police et l'espacement.
    

### **NLQueryForm.jsx**

Dans ce fichier, nous gérons les appels API, définissons les actions CopilotKit et passons les données récupérées au composant Table. Ce fichier agit comme le hub logique central pour connecter l'API backend, les actions IA et l'affichage frontend.

Fonctionnalités clés de `NLQueryForm.jsx` :

1. **Intégration API** : Récupère les données de la base de données et gère les erreurs ou les états de chargement.
    
2. **Actions CopilotKit** : Définit les actions IA qui permettent d'interroger et d'interagir avec la base de données en utilisant le langage naturel.
    
3. **Passage de données** : Envoie les données traitées au composant `Table` pour l'affichage.
    

Voici le code :

```javascript
"use client";
import React, { useState, useEffect } from "react";
import { useCopilotReadable, useCopilotAction } from "@copilotkit/react-core";
import axios from "axios";
import { Tabledata } from "./Tabledata";

function NLQueryForm() {
  const [nlQuery, setNlQuery] = useState("");
  const [data, setData] = useState([]);
  console.log(" ~ NLQueryForm ~ data:", data);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(true);

  const API_KEY = process.env.NEXT_PUBLIC_RESTDB_API_KEY;
  const BASE_URL = process.env.NEXT_PUBLIC_RESTDB_BASE_URL;
  console.table({ API_KEY, BASE_URL });
  useEffect(() => {
    async function fetchData() {
      if (!API_KEY || !BASE_URL) {
        setError("La configuration de l'API est manquante");
        setLoading(false);
        return;
      }
      try {
        const response = await axios.get(BASE_URL, {
          headers: {
            "x-apikey": API_KEY,
            "Content-Type": "application/json",
          },
        });
        setData(response.data);
        setLoading(false);
      } catch (error) {
        console.error("Erreur lors de la récupération des données :", error);
        setError(
          error instanceof Error ? error.message : "Une erreur inconnue s'est produite"
        );
        setLoading(false);
      }
    }
    fetchData();
  }, [API_KEY, BASE_URL]);

  useCopilotReadable({
    description: "Interroger la base de données avec des informations détaillées",
    value: JSON.stringify(data.slice(0, 25)),
  });
  useCopilotAction({
    name: "fetchData",
    description: "Rechercher et filtrer les données en fonction d'une requête en langage naturel",
    parameters: [
      {
        name: "nlQuery",
        type: "string",
        description: "Terme de recherche en langage naturel pour la base de données",
        required: true,
      },
    ],

    handler: async ({ data }) => {
      setNlQuery(data);
      return JSON.stringify(data);
    },
  });

  if (loading) return <div>Chargement...</div>;

  return (
    <div>
      {error && <p style={{ color: "red" }}>{error}</p>}
      <div>
        <p className="text-sm text-green-600 font-bold text-center">
          Données en direct de la base de données.
        </p>
        <p className="text-sm text-green-600 font-bold text-center">
          Nombre total d'enregistrements : {data.length}
        </p>
        <Tabledata data={data} />
      </div>
    </div>
  );
}
export default NLQueryForm;
```

Voici une explication détaillée du composant `NLQueryForm` :

**Imports et dépendances :**

* Utilise React pour la gestion d'état (`useState`) et les effets secondaires (`useEffect`).
    
* Importe `axios` pour les requêtes HTTP.
    
* Importe `useCopilotReadable` et `useCopilotAction` de `@copilotkit/react-core` pour intégrer les fonctionnalités de CopilotKit.
    
* Importe un composant personnalisé `Tabledata` pour le rendu des données.
    

**Configuration du composant :**

* Définit un composant fonctionnel React `NLQueryForm`.
    
* Initialise les variables d'état :
    
    * `nlQuery` : Contient l'entrée de requête en langage naturel.
        
    * `data` : Stocke les données récupérées de l'API.
        
    * `error` : Stocke les erreurs qui se produisent lors de la récupération des données.
        
    * `loading` : Suivi de l'état de chargement du composant.
        

**Configuration de l'API :**

* Récupère les clés API et l'URL de base à partir des variables d'environnement (`NEXT_PUBLIC_RESTDB_API_KEY` et `NEXT_PUBLIC_RESTDB_BASE_URL`).
    
* Journalise ces valeurs à des fins de débogage en utilisant `console.table`.
    

**Récupération des données :**

* Utilise `useEffect` pour récupérer les données de l'API lors du rendu initial.
    
* Effectue une requête GET à l'API en utilisant `axios` avec les en-têtes requis.
    
* Met à jour `data` avec la réponse et arrête l'état de chargement.
    
* Gère les erreurs en les journalisant et en mettant à jour l'état `error`.
    

**Intégration de CopilotKit :**

* `useCopilotReadable` : Expose une description lisible et une tranche des 25 premiers enregistrements de `data`.
    
* `useCopilotAction` : Définit une action CopilotKit nommée `fetchData` qui :
    
    * Accepte une requête en langage naturel (`nlQuery`) en entrée.
        
    * Met à jour l'état `nlQuery` et le retourne sous forme de chaîne.
        

**Rendu conditionnel :**

* Affiche un message de chargement (`Chargement...`) si `loading` est vrai.
    
* Affiche un message d'erreur en texte rouge si une erreur se produit.
    

**Rendu :**

* Affiche un message indiquant les données en direct et le nombre total d'enregistrements.
    
* Passe l'état `data` au composant `Tabledata` pour le rendu.
    

**Export :**

* Exporte le composant `NLQueryForm` en tant qu'exportation par défaut.
    

### **Page.js**

Maintenant, allez dans le fichier `page.js` à l'intérieur du dossier de l'application et ajoutez ce code :

* ```javascript
    "use client";
    
    import NLQueryForm from "@/components/ui/nl-query-form";
    import { CopilotPopup } from "@copilotkit/react-ui";
    
    export default function Home() {
      return (
        <div className="min-h-screen bg-background">
          <header className="bg-primary text-primary-foreground py-6">
            <div className="container">
              <h1 className="text-3xl font-bold">
                Constructeur de requêtes SQL en langage naturel
              </h1>
            </div>
          </header>
          <main className="container py-8">
            <NLQueryForm />
          </main>
    
          <CopilotPopup
            instructions={
              "Vous aidez l'utilisateur du mieux que vous pouvez. Répondez de la meilleure manière possible en fonction des données dont vous disposez."
            }
            labels={{
              title: "Assistant Popup",
              initial: "Besoin d'aide ?",
            }}
          />
        </div>
      );
    }
    ```
    

Voici une explication simple du code ci-dessus :

* **Rendu côté client :**
    
    * `"use client";` indique que le fichier utilise le rendu côté client de React.
        
* **Importation des composants :**
    
    * `NLQueryForm` est importé depuis un répertoire de composants local pour être utilisé dans l'application.
        
    * `CopilotPopup` est importé depuis le package `@copilotkit/react-ui` pour afficher une fenêtre contextuelle interactive.
        
* **Fonction principale :**
    
    * `Home` est un composant fonctionnel React qui définit l'interface utilisateur pour la page d'accueil.
        
* **Disposition de la page :**
    
    * Un conteneur de page complète (`min-h-screen`) avec une couleur de fond (`bg-background`) enveloppe tout le contenu.
        
* **En-tête :**
    
    * Contient un titre avec le texte **"Constructeur de requêtes SQL en langage naturel"**.
        
    * Stylisé avec une couleur de fond et de texte primaire (`bg-primary`, `text-primary-foreground`).
        
* **Contenu principal :**
    
    * Affiche le composant `NLQueryForm` à l'intérieur d'un conteneur avec un remplissage (`py-8`).
        
* **Composant Popup :**
    
    * Ajoute un `CopilotPopup` en bas avec :
        
        * **Instructions :** Décrit le rôle de l'assistant.
            
        * **Libellés :** Inclut un titre et un message initial pour la fenêtre contextuelle.
            
* **Objectif :**
    
    * La page est conçue pour permettre aux utilisateurs d'interagir avec un constructeur de requêtes SQL en langage naturel et de recevoir de l'aide via une fenêtre contextuelle.
        

### **Configurer CopilotKit pour toute l'application**

Ce sera la dernière étape de la construction de l'application. Accédez au fichier `layout.js` et ajoutez ce code :

```javascript

import "./globals.css";
import { CopilotKit } from "@copilotkit/react-core";
import "@copilotkit/react-ui/styles.css";
export const metadata = {
  title: "Create Next App",
  description: "Generated by create next app",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <CopilotKit runtimeUrl="/api/copilotkit">{children}</CopilotKit>
      </body>
    </html>
  );
```

Voici ce qui se passe dans ce code :

* **Imports :**
    
    * `./globals.css` : Importe les styles CSS globaux pour l'application.
        
    * `@copilotkit/react-core` : Importe les fonctionnalités principales de CopilotKit.
        
    * `@copilotkit/react-ui/styles.css` : Inclut les styles prédéfinis pour les composants de l'interface utilisateur CopilotKit.
        
* **Métadonnées :**
    
    * L'objet `metadata` définit le titre et la description de l'application, qui sont utiles pour définir les balises méta dans le HTML généré pour le référencement et les informations utilisateur.
        
* **Fonction RootLayout :**
    
    * Cette fonction sert de wrapper de disposition racine pour l'application. Elle garantit une structure cohérente sur toutes les pages et intègre l'environnement d'exécution CopilotKit.
        
* **Structure :**
    
    * La disposition retourne un élément `<html>` avec un attribut `lang` défini sur `en` pour l'anglais.
        
    * À l'intérieur de la balise `<body>`, le composant CopilotKit est enveloppé autour de la prop `children`. Cette configuration :
        
        * Connecte l'application à l'environnement d'exécution CopilotKit en utilisant le point de terminaison de l'API `/api/copilotkit`.
            
        * Fournit l'accès aux fonctionnalités de CopilotKit, telles que la gestion des requêtes en langage naturel, dans toute l'application.
            

## Quelques notes importantes

La conception et le déploiement d'une base de données peuvent prendre diverses formes, en fonction des outils et des exigences. Pour ce projet, j'ai choisi l'approche la plus simple et la plus accessible.

#### Pourquoi CopilotKit ?

CopilotKit est un outil puissant qui convertit les requêtes NLP en code backend actionnable. Si vous avez une alternative qui fonctionne de manière similaire, n'hésitez pas à l'utiliser. Il comble le fossé entre l'entrée en langage naturel et l'exécution technique, ce qui le rend idéal pour des projets comme celui-ci.

#### Pourquoi GroqCloud ?

J'ai sélectionné **GroqCloud** car il est gratuit et offre un accès à plusieurs LLM avec une seule clé API. Bien que vous puissiez opter pour des alternatives comme ChatGPT, notez qu'elles peuvent nécessiter des plans payants. La polyvalence et l'abordabilité de GroqCloud en font un choix parfait pour ce tutoriel.

#### Considérations sur la base de données

La taille de votre base de données peut varier de très petite à énorme. Cependant, l'interaction avec la base de données dépend des limites de jetons du LLM que vous utilisez.

Puisque je travaille avec des outils gratuits, mon attention se porte sur une petite base de données pour garantir des interactions fluides.

#### Bonnes pratiques de sécurité

Ne jamais exposer vos informations d'identification publiquement. Stockez toujours les informations sensibles comme les clés API dans un fichier `.env` pour garder votre projet sécurisé.

#### Améliorations futures

Bien que ce tutoriel se concentre sur la configuration et l'interrogation d'une base de données, le potentiel de CopilotKit s'étend aux **opérations CRUD** (Create, Read, Update, Delete). Dans mon prochain tutoriel, je démontrerai comment implémenter des opérations CRUD complètes en utilisant CopilotKit pour une application plus dynamique et fonctionnelle.

## Jouer avec la base de données

Vous pouvez explorer le projet en direct via le lien suivant et poser des questions liées aux données de la base de données : [lien en direct](https://talktodb-inky.vercel.app/).

Pour une compréhension plus approfondie du code, voici le lien vers le dépôt GitHub : [github](https://github.com/prankurpandeyy/talktodb).

Voici également une capture d'écran démontrant son utilisation pratique. Dans cet exemple, au lieu d'écrire une requête SQL simple comme `SELECT * FROM demo_data WHERE email = '`[`riverashannon@lee.com`](mailto:riverashannon@lee.com)`';` pour extraire le nom de la personne, nous avons utilisé une requête NLP pour obtenir exactement le même résultat.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1735061714011/bec86e4a-bb7b-4d7f-97e9-284d54060db5.png align="center")

## Conclusion

J'espère que vous avez apprécié la construction de ce simple chatbot IA pour interagir avec la base de données. Dans ce projet, nous avons utilisé une simple base de données SQL, mais vous pouvez appliquer cette approche à n'importe quelle base de données tant que vous pouvez récupérer les données.

À l'avenir, je prévois de mettre en œuvre de nombreux nouveaux projets impliquant l'IA et d'autres outils. Les outils d'IA sont vraiment révolutionnaires dans le domaine de l'informatique, et j'ai hâte de vous fournir plus d'informations détaillées et d'implémentations pratiques des derniers outils émergents dans ce domaine.

Donc, c'est la fin de mon côté. Si vous avez trouvé cet article utile, alors partagez-le et connectez-vous avec moi - je suis ouvert aux opportunités :

* Suivez-moi sur X : [Twitter de Prankur](https://x.com/prankurpandeyy)
    
* Suivez-moi sur LinkedIn : [Linkedin de Prankur](https://linkedin.com/in/prankurpandeyy)
    
* Consultez mon portfolio ici : [Portfolio de Prankur](https://prankurpandeyy.netlify.app/)