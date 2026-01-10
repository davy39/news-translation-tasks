---
title: Comment construire un serveur MCP de liste de tâches avec TypeScript – avec
  Auth, Base de données et Facturation
subtitle: ''
author: Shola Jegede
co_authors: []
series: null
date: '2025-10-22T19:59:14.912Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-to-do-list-mcp-server-using-typescript
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1761162036666/77972b3f-9dc8-404f-b40d-fb70ee73e2a5.png
tags:
- name: mcp
  slug: mcp
- name: mcp server
  slug: mcp-server
- name: TypeScript
  slug: typescript
seo_title: Comment construire un serveur MCP de liste de tâches avec TypeScript –
  avec Auth, Base de données et Facturation
seo_desc: 'In this tutorial, you’ll build a To-Do list MCP server using TypeScript.
  You’ll learn how to implement authentication, persistence, and billing, to make
  the server robust and functional for real users.

  By the end, you’ll have a working MCP server tha...'
---

Dans ce tutoriel, vous allez construire un serveur MCP (Model Context Protocol) de liste de tâches en utilisant TypeScript. Vous apprendrez à implémenter l'authentification, la persistance et la facturation, afin de rendre le serveur robuste et fonctionnel pour de vrais utilisateurs.

À la fin, vous aurez un serveur MCP opérationnel qui :

* Authentifie les utilisateurs avec Kinde.
    
* Stocke les données de tâches dans une base de données Neon Postgres.
    
* Applique des limites de facturation et prend en charge les mises à niveau.
    
* Expose toutes ces fonctionnalités en tant qu'outils MCP à l'intérieur de Cursor.
    

Cet article vous guidera à travers chaque étape, vous aidant à comprendre les décisions de conception que vous pourrez adapter pour vos propres projets.

## Ce que vous allez apprendre

* [Pourquoi aller au-delà des serveurs MCP de base](#heading-pourquoi-aller-au-dela-des-serveurs-mcp-de-base)
    
* [Ce que vous allez construire](#heading-ce-que-vous-allez-construire)
    
* [Prérequis](#heading-prerequis)
    
* [Configuration du projet](#heading-configuration-du-projet)
    
* [Configuration de la base de données avec Neon PostgreSQL](#heading-configuration-de-la-base-de-donnees-avec-neon-postgresql)
    
    * [1\. Connectez votre base de données Neon](#heading-1-connectez-votre-base-de-donnees-neon)
        
    * [2\. Créez votre fichier DB](#heading-2-creez-votre-fichier-db)
        
    * [3\. Analyse étape par étape de setup-db.ts](#heading-3-analyse-etape-par-etape-de-setup-dbts)
        
    * [4\. Fichier setup-db.ts complet](#heading-4-fichier-setup-dbts-complet)
        
* [Authentification avec Kinde](#heading-authentification-avec-kinde)
    
    * [1\. Créez une application Kinde](#heading-1-creez-une-application-kinde)
        
    * [2\. Configurez les paramètres Kinde](#heading-2-configurez-les-parametres-kinde)
        
    * [3\. Variables d'environnement](#heading-3-variables-denvironnement)
        
    * [4\. Créez le serveur d'authentification Kinde](#heading-4-creez-le-serveur-dauthentification-kinde)
        
    * [5\. Flux d'authentification complet](#heading-5-flux-dauthentification-complet)
        
    * [6\. Pourquoi cela est important](#heading-6-pourquoi-cela-est-important)
        
    * [7\. Connexions clés](#heading-7-connexions-cles)
        
    * [8\. Fichier kinde-auth-server.ts complet](#heading-8-fichier-kinde-auth-serverts-complet)
        
* [Implémentation du serveur MCP (avec intégration du système de facturation)](#heading-implementation-du-serveur-mcp-avec-integration-du-systeme-de-facturation)
    
    * [1\. Créez votre fichier](#heading-1-creez-votre-fichier)
        
    * [2\. Configuration du projet et importations](#heading-2-configuration-du-projet-et-importations)
        
    * [3\. Connexion et configuration de la base de données](#heading-3-connexion-et-configuration-de-la-base-de-donnees)
        
    * [4\. Système d'authentification](#heading-4-systeme-dauthentification)
        
    * [5\. Fonctions utilitaires principales](#heading-5-fonctions-utilitaires-principales)
        
    * [6\. Implémentation principale du serveur](#heading-6-implementation-principale-du-serveur)
        
    * [7\. Enregistrement des outils](#heading-7-enregistrement-des-outils)
        
    * [8\. Gestionnaires d'outils](#heading-8-gestionnaires-doutils)
        
    * [9\. Fichier server.ts complet](#heading-9-fichier-serverts-complet)
        
    * [10\. Flux de données et intégration](#heading-10-flux-de-donnees-et-integration)
        
    * [11\. Gestion des erreurs et sécurité](#heading-11-gestion-des-erreurs-et-securite)
        
    * [12\. Tests et déploiement](#heading-12-tests-et-deploiement)
        
* [Tester le système complet](#heading-tester-le-systeme-complet)
    
    * [1\. Démarrer les services](#heading-1-demarrer-les-services)
        
    * [2\. Configurer Cursor MCP](#heading-2-configurer-cursor-mcp)
        
    * [3\. Tester le flux complet](#heading-3-tester-le-flux-complet)
        
* [Dépannage](#heading-depannage)
    
    * [1\. Serveur MCP non détecté](#heading-1-serveur-mcp-non-detecte)
        
    * [2\. Problèmes de connexion à la base de données](#heading-2-problemes-de-connexion-a-la-base-de-donnees)
        
    * [3\. Problèmes d'authentification Kinde](#heading-3-problemes-dauthentification-kinde)
        
    * [4\. Erreurs de jeton](#heading-4-erreurs-de-jeton)
        
* [Architecture finale du serveur MCP](#heading-architecture-finale-du-serveur-mcp)
    
* [Conclusion](#heading-conclusion)
    
    * [Étapes suivantes](#heading-etapes-suivantes)
        
    * [Ressources](#heading-ressources)
        

## Pourquoi aller au-delà des serveurs MCP de base ?

Si vous avez lu ce [manuel MCP de freeCodeCamp](https://www.freecodecamp.org/news/how-to-build-a-custom-mcp-server-with-typescript-a-handbook-for-developers), vous avez appris à configurer un serveur MCP simple en TypeScript. C'est utile pour apprendre le protocole, mais cela ne reflète pas ce dont vous avez besoin en production.

Une application réelle nécessite :

* **L'authentification** pour que chaque utilisateur ait ses propres données et permissions.
    
* **La persistance** pour que les données soient stockées dans une base de données fiable.
    
* **La facturation** pour que vous puissiez appliquer des limites et monétiser l'usage.
    

Sans cela, un serveur MCP n'est qu'une démonstration.

## Ce que vous allez construire

Dans ce tutoriel, vous allez construire un serveur MCP de tâches avec TypeScript qui inclut les éléments essentiels d'un backend prêt pour la production :

* **Authentification** avec Kinde
    
* **Persistance de base de données** avec Neon Postgres
    
* **Application de la facturation** avec un niveau gratuit et un chemin de mise à niveau
    
* **Exposition des outils MCP** pour que tout cela fonctionne de manière transparente
    

À la fin, vous aurez un serveur MCP qui ressemble davantage au backend d'une application SaaS et un modèle que vous pourrez étendre pour vos propres idées.

## Prérequis

Avant de commencer, vous aurez besoin de :

**Comptes et Services (tous gratuits) :**

* [Compte Kinde](https://kinde.com) **→** pour l'authentification et la facturation
    
* [Compte Neon](https://neon.com) **→** pour la base de données PostgreSQL
    
* Node.js (v18+) ([télécharger](https://nodejs.org/en/download))
    
* Cursor IDE **→** pour l'intégration MCP et le test des outils ([télécharger](https://cursor.com/download))
    

**Outils de développement :**

* Accès au terminal / ligne de commande
    
* Git (optionnel, pour le contrôle de version)
    

## Configuration du projet

Tout d'abord, créez un nouveau dossier :

```powershell
mkdir todo-mcp-server
cd todo-mcp-server
```

Ensuite, initialisez un projet Node.js :

```powershell
npm init -y
```

Ensuite, installez les dépendances dont votre serveur aura besoin :

```powershell
npm install @modelcontextprotocol/sdk @neondatabase/serverless @kinde-oss/kinde-typescript-sdk express jsonwebtoken jwks-client express-session
```

Le package `@modelcontextprotocol/sdk` nous donne tout ce dont nous avons besoin pour construire et exposer des serveurs et des outils MCP. Nous utilisons `@neondatabase/serverless` pour nous connecter à une base de données Neon Postgres, et `@kinde-oss/kinde-typescript-sdk` gère l'authentification et la facturation via Kinde.

Nous installerons également `express`, qui facilite la définition des routes et la gestion des middlewares. Pour vérifier les jetons utilisateur de Kinde, nous utiliserons `jsonwebtoken` avec `jwks-client`. Enfin, `express-session` s'occupera de la gestion de l'état de la session pour que les utilisateurs puissent rester connectés entre les requêtes.

Ensuite, configurez TypeScript et quelques définitions de types pour le développement :

```powershell
npm install -D typescript @types/node @types/express @types/express-session tsx
```

Le package `typescript` active TypeScript dans votre projet afin que vous puissiez écrire du code fortement typé. Les packages `@types/*` fournissent des définitions de types pour Node.js, Express et le middleware de session, vous offrant une meilleure autocomplétion et vérification des erreurs dans votre éditeur.

Enfin, `tsx` permet d'exécuter très facilement des fichiers TypeScript directement sans avoir besoin de les pré-compiler avant de lancer votre application.

Ensuite, créez un fichier `.env` à la racine de votre projet et collez ces variables :

```json
# Database
DATABASE_URL=postgresql://user:pass@host:port/db

# Kinde Authentication
KINDE_ISSUER_URL=https://votre-domaine.kinde.com
KINDE_CLIENT_ID=votre_client_id
KINDE_CLIENT_SECRET=votre_client_secret

# Security
JWT_SECRET=votre_cle_secrete

# Environment
NODE_ENV=development
```

Cela stocke tous les identifiants que vous utiliserez pour ce projet.

Ensuite, créez un fichier `tsconfig.json` à la racine du projet pour indiquer au compilateur TypeScript comment gérer votre code :

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "moduleResolution": "node",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "outDir": "./dist",
    "rootDir": "./src"
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

Enfin, mettez à jour vos scripts dans `package.json` :

```json
{
  "scripts": {
    "build": "tsc",
    "dev": "tsx src/server.ts",
    "start": "node dist/server.js",
    "auth-server": "tsx src/kinde-auth-server.ts",
    "setup-db": "tsx src/setup-db.ts"
  }
}
```

## Configuration de la base de données avec Neon PostgreSQL

Pour alimenter votre serveur MCP de tâches, vous utiliserez Neon, une plateforme PostgreSQL serverless. Cela nous donne une base de données entièrement gérée et évolutive sans se soucier de l'infrastructure.

### 1\. Connectez votre base de données Neon

* Inscrivez-vous ou connectez-vous à votre [console de compte Neon](https://console.neon.tech).
    
* Créez un nouveau projet.
    
* Copiez la chaîne de connexion, vous en aurez besoin dans votre fichier `.env`.
    

### 2\. Créez votre fichier DB

À l'intérieur de votre projet, créez un nouveau fichier dans votre dossier `src/` et nommez-le `setup-db.ts`. Ce fichier créera les tables, les index et le schéma sur lesquels votre application repose.

Présentation de l'architecture de la base de données :

```markdown
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   setup-db.ts   │───▶│  Base de données │───▶│   PostgreSQL    │
│   (Schéma)      │    │   Neon (Sls)    │    │   (Tables)      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### 3\. Analyse étape par étape de `setup-db.ts`

**Étape 1 : Importations et connexion à la base de données**

Commencez par importer les packages dont vous aurez besoin et configurer votre connexion à la base de données :

```typescript
import { neon } from '@neondatabase/serverless';
import dotenv from 'dotenv';

dotenv.config();

const sql = neon(process.env.DATABASE_URL!);
```

Le package `dotenv` charge vos variables d'environnement à partir d'un fichier `.env` afin que vous n'ayez pas à coder en dur les secrets dans votre code. La fonction `neon` connecte votre application à votre base de données Neon Postgres, et la variable `sql` vous offre un moyen propre et typé d'exécuter des requêtes.

À ce stade, votre application a tout ce dont elle a besoin pour communiquer avec la base de données.

**Étape 2 : Fonction de configuration principale**

Créons maintenant une fonction pour gérer le processus de configuration de la base de données :

```typescript
async function setupDatabase() {
  console.log('Configuration du schéma de la base de données...');
  try {
    // Opérations de base de données ici
  } catch (error) {
    console.error('Erreur lors de la configuration de la base de données:', error);
    process.exit(1);
  }
}
```

Cette fonction regroupe toute votre logique de création de schéma en un seul endroit, ce qui la rend facile à gérer. Elle capture et enregistre également toutes les erreurs au lieu d'échouer silencieusement. Les messages de la console vous donnent un retour en temps réel pendant l'exécution de la configuration.

**Étape 3 : Table des tâches (To-Dos)**

Ensuite, créez une table pour stocker toutes les tâches des utilisateurs :

```typescript
await sql`
  CREATE TABLE IF NOT EXISTS todos (
    id SERIAL PRIMARY KEY,
    user_id TEXT NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    completed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  )
`;
```

Cette table contient les tâches de chaque utilisateur. La colonne `user_id` lie chaque tâche à l'utilisateur qui l'a créée, tandis que le champ `completed` suit si une tâche est terminée ou en attente. Les horodatages automatiques `created_at` et `updated_at` facilitent le tri des tâches ou le suivi de leur historique.

**Étape 4 : Table des utilisateurs**

Définissons maintenant une table pour gérer les comptes utilisateurs et les détails de facturation :

```typescript
await sql`
  CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    user_id TEXT UNIQUE NOT NULL,
    name TEXT,
    email TEXT,
    subscription_status TEXT DEFAULT 'free' CHECK (subscription_status IN ('free', 'active', 'cancelled')),
    plan TEXT DEFAULT 'free',
    free_todos_used INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  )
`;
```

Cette table stocke les informations de base de chaque utilisateur ainsi que les détails de son abonnement. La valeur `user_id` provient directement de Kinde lors de l'authentification. Les colonnes `subscription_status` et `free_todos_used` vous aident à appliquer les niveaux de facturation et à limiter le nombre de tâches gratuites qu'un utilisateur peut créer avant de devoir passer à un forfait supérieur.

**Étape 5 : Index de performance**

Ensuite, ajoutons quelques index pour accélérer les opérations courantes de la base de données :

```typescript
await sql`
  CREATE INDEX IF NOT EXISTS idx_todos_user_id ON todos(user_id)
`;

await sql`
  CREATE INDEX IF NOT EXISTS idx_todos_created_at ON todos(created_at)
`;

await sql`
  CREATE INDEX IF NOT EXISTS idx_users_user_id ON users(user_id)
`;
```

Ces index aident à accélérer les recherches et le tri. Le premier permet à la base de données de trouver rapidement les tâches appartenant à un utilisateur spécifique. Le deuxième accélère le tri des tâches par date de création. Et le dernier permet des recherches rapides d'utilisateurs basées sur leur `user_id` Kinde.

**Étape 6 : Journalisation de succès**

Une fois que tout est exécuté, il est utile d'afficher un résumé clair de ce qui a été créé :

```typescript
console.log('✅ Schéma de base de données créé avec succès !');
console.log('📋 Tables créées :');
console.log('  - todos (id, user_id, title, description, completed, created_at, updated_at)');
console.log('  - users (id, user_id, subscription_status, plan, free_todos_used, created_at, updated_at)');
console.log('🔍 Index créés pour une performance optimale');
```

Ces journaux vous donnent un retour immédiat une fois la configuration terminée.

**Étape 7 : Gestion des erreurs**

```typescript
try {
} catch (error) {
  console.error('❌ Erreur lors de la configuration de la base de données:', error);
  process.exit(1);
}
```

Cela gère gracieusement toutes les erreurs de configuration de la base de données.

**Étape 8 :** Mettez à jour votre fichier `.env` à la racine de votre projet avec votre chaîne de connexion Neon :

```json
DATABASE_URL=postgresql://username:password@host/database?sslmode=require
```

**Étape 9 : Exécution de la fonction**

Au bas de `setup-db.ts`, exécutez la fonction :

```typescript
setupDatabase();
```

Cela exécute immédiatement la configuration de la base de données lorsque le script est lancé.

Maintenant, lancez cette commande dans votre terminal :

```powershell
npm run setup-db
```

Sortie attendue :

```powershell
🚀 Configuration du schéma de la base de données...
✅ Schéma de base de données créé avec succès !
📋 Tables créées :
  - todos (id, user_id, title, description, completed, created_at, updated_at)
  - users (id, user_id, subscription_status, plan, free_todos_used, created_at, updated_at)
🔍 Index créés pour une performance optimale
```

### 4\. Fichier `setup-db.ts` complet

Vous pouvez consulter l'implémentation complète du fichier `setup-db.ts` dans le [dépôt GitHub](https://github.com/sholajegede/todo_mcp_server/blob/main/src/setup-db.ts) et le copier directement dans votre projet.

## Authentification avec Kinde

Pour sécuriser votre serveur MCP, vous utiliserez [Kinde](https://kinde.com), un fournisseur d'authentification qui facilite la gestion des connexions, des sessions utilisateur et des jetons.

Vous connecterez également Kinde à votre base de données Neon afin que les nouveaux utilisateurs soient automatiquement créés lors de leur connexion.

### 1\. Créez une application Kinde

* Allez sur le [Tableau de bord Kinde](https://app.kinde.com/admin).
    
* Créez une nouvelle application.
    
* Notez ces valeurs (vous les utiliserez bientôt) :
    
    * **Domaine** : [`https://votre-domaine.kinde.com`](https://your-domain.kinde.com)
        
    * **ID Client** : `votre-client-id`
        
    * **Secret Client** : `votre-client-secret`
        

### 2\. Configurez les paramètres Kinde

Dans votre tableau de bord Kinde, enregistrez ces URL comme vos :

* URL de redirection → [`http://localhost:3000/callback`](http://localhost:3000/callback)
    
* URL de déconnexion → [`http://localhost:3000`](http://localhost:3000)
    

### 3\. Variables d'environnement

Mettez à jour le fichier `.env` à la racine de votre projet avec les identifiants de votre tableau de bord Kinde :

```json
KINDE_ISSUER_URL=https://votre-domaine.kinde.com
KINDE_CLIENT_ID=votre_client_id
KINDE_CLIENT_SECRET=votre_client_secret
```

### 4\. Créez le serveur d'authentification Kinde

Vous allez construire un serveur Express (`src/kinde-auth-server.ts`) pour gérer l'authentification. Ce serveur gérera la connexion et la déconnexion OAuth avec Kinde, stockera les sessions utilisateur et créera ou mettra à jour automatiquement les utilisateurs dans votre base de données Neon à chaque connexion.

**4.1 : Dépendances et configuration**

Commencez par importer les packages nécessaires :

```typescript
import express from 'express';
import session from 'express-session';
import { createKindeServerClient, GrantType, SessionManager } from '@kinde-oss/kinde-typescript-sdk';
import jwt from 'jsonwebtoken';
import dotenv from 'dotenv';
import { neon } from '@neondatabase/serverless';
```

L'importation `express` alimente le serveur web qui gérera les routes d'authentification. `express-session` gère les sessions utilisateur. Le package `@kinde-oss/kinde-typescript-sdk` est le SDK officiel de Kinde, qui gère les flux OAuth.

Vous utiliserez `jsonwebtoken` pour décoder et vérifier les jetons utilisateur, tandis que `dotenv` chargera les variables d'environnement. Enfin, `@neondatabase/serverless` connectera votre serveur à la base de données Neon Postgres.

**4.2 : Connexion à votre base de données**

```typescript
const sql = neon(process.env.DATABASE_URL!);
```

Ceci initialise un client SQL typé utilisant votre `DATABASE_URL`.

**4.3 : Étendre la session de connexion**

```typescript
declare module 'express-session' {
  interface SessionData {
    accessToken?: string;
    idToken?: string;
    userInfo?: any;
    userName?: string;
    userEmail?: string;
  }
}
```

Ceci étend les types d'`express-session` afin que vous puissiez stocker les jetons Kinde et les informations utilisateur directement dans la session.

**4.4 : Configurer les sessions**

Configurons maintenant la gestion des sessions :

```typescript
app.use(session({
  secret: process.env.JWT_SECRET || 'votre_cle_secrete_jwt',
  resave: true,
  saveUninitialized: true,
  cookie: { 
    secure: false,
    maxAge: 7 * 24 * 60 * 60 * 1000, // 7 jours
    httpOnly: true,
    sameSite: 'lax'
  }
}));
```

La valeur `secret` est utilisée pour signer et vérifier les cookies de session. Les paramètres du cookie maintiennent les utilisateurs connectés jusqu'à 7 jours. Le réglage `httpOnly` aide à protéger contre les attaques XSS, tandis que `sameSite: 'lax'` permet aux utilisateurs de se connecter à travers différentes origines.

**4.5 : Créer une fabrique de gestionnaire de session**

Ensuite, vous définirez une petite fonction utilitaire pour gérer les données de session pour chaque requête :

```typescript
const createSessionManager = (req: any): SessionManager => ({
  getSessionItem: async (key: string) => req.session?.[key],
  setSessionItem: async (key: string, value: any) => {
    if (!req.session) req.session = {};
    req.session[key] = value;
  },
  removeSessionItem: async (key: string) => {
    if (req.session) delete req.session[key];
  },
  destroySession: async () => {
    req.session = {};
  }
});
```

**4.6 : Créer le client Kinde**

Configurez le client Kinde qui gérera le flux de connexion et de déconnexion OAuth :

```typescript
const kindeClient = createKindeServerClient(GrantType.AUTHORIZATION_CODE, {
  authDomain: process.env.KINDE_ISSUER_URL!,
  clientId: process.env.KINDE_CLIENT_ID!,
  clientSecret: process.env.KINDE_CLIENT_SECRET!,
  redirectURL: '<http://localhost:3000/callback>',
  logoutRedirectURL: '<http://localhost:3000>',
});
```

Ceci connecte votre application à Kinde en utilisant le type d'autorisation **Authorization Code**, qui est l'option la plus sécurisée pour les applications côté serveur.

**4.7 : Créer la route de la page d'accueil (**`GET /`**)**

```typescript
app.get('/', (req, res) => {
  const token = req.session?.accessToken;
  const userInfo = req.session?.userInfo;
  
  if (token) {
    // Afficher l'état connecté avec les jetons
  } else {
    // Afficher le bouton de connexion
  }
});
```

**4.8 : Créer la route de connexion (**`GET /login`**)**

```typescript
app.get('/login', async (req, res) => {
  try {
    const sessionManager = createSessionManager(req);
    const loginUrl = await kindeClient.login(sessionManager);
    res.redirect(loginUrl.toString());
  } catch (error) {
    console.error('Erreur de connexion:', error);
    res.status(500).send('Échec de la connexion');
  }
});
```

**4.9 : Route de rappel OAuth (**`GET /callback`**)**

C'est ici que Kinde redirige les utilisateurs après la connexion. Tout d'abord, vous récupérez le `code` d'autorisation pour l'échange de jetons, puis vous échangez ce code contre des jetons et stockez ces jetons dans la session.

Enfin, ajoutez ce code qui créera ou mettra à jour automatiquement l'utilisateur dans la base de données :

```typescript
const existingUser = await sql`SELECT * FROM users WHERE user_id = ${userId}`;

if (existingUser.length === 0) {
  await sql`
    INSERT INTO users (user_id, name, email, subscription_status, plan, free_todos_used)
    VALUES (${userId}, ${userName}, ${userEmail}, 'free', 'free', 0)
  `;
} else {
  await sql`
    UPDATE users 
    SET name = ${userName}, email = ${userEmail}
    WHERE user_id = ${userId}
  `;
}
```

**4.10 : Créer la route de déconnexion (**`GET /logout`**)**

```typescript
app.get('/logout', async (req, res) => {
  try {
    req.session.destroy((err) => {
      if (err) {
        console.log('Erreur de destruction de session:', err);
      }
      res.redirect('/');
    });
  } catch (error) {
    console.error('Erreur de déconnexion:', error);
    res.status(500).send('Échec de la déconnexion');
  }
});
```

### 5\. Flux d'authentification complet

```markdown
1. L'utilisateur visite / → voit le bouton de connexion.
2. Clique sur connexion → va sur Kinde.
3. Se connecte → redirigé vers /callback.
4. Le callback échange le code contre des jetons.
5. Les jetons sont stockés dans la session.
6. L'utilisateur est créé/mis à jour dans la base de données.
7. L'utilisateur peut maintenant accéder au serveur MCP.
```

### 6\. Pourquoi cela est important

En plaçant Kinde devant votre serveur MCP, vous obtenez une couche d'authentification sécurisée et transparente sans avoir à gérer manuellement les mots de passe ou les jetons. Vos utilisateurs peuvent se connecter en toute sécurité et leurs sessions persistent.

### 7\. Connexions clés

* **Session ↔ Base de données** : Synchronisation des données utilisateur
    
* **Kinde ↔ Session** : Les jetons circulent de Kinde vers le stockage de session
    
* **Session ↔ MCP** : Jetons passés au serveur pour le contrôle d'accès
    
* **Base de données ↔ MCP** : Facturation utilisateur + tâches lues depuis Neon
    

### 8\. Fichier `kinde-auth-server.ts` complet

Vous pouvez consulter l'implémentation complète du fichier `kinde-auth-server.ts` dans le [dépôt GitHub](https://github.com/sholajegede/todo_mcp_server/blob/main/src/kinde-auth-server.ts) et le copier directement dans votre projet.

## Implémentation du serveur MCP (avec intégration du système de facturation)

Il est maintenant temps de créer le fichier principal de votre serveur MCP. Ce fichier servira de point d'entrée, reliant votre base de données, l'authentification, les gestionnaires d'outils et le flux global.

### 1\. Créez votre fichier

À l'intérieur de votre projet, créez un nouveau fichier :

```bash
src/server.ts
```

### 2\. Configuration du projet et importations

En haut du fichier, importez les dépendances :

```typescript
import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import { CallToolRequestSchema, ListToolsRequestSchema } from '@modelcontextprotocol/sdk/types.js';
import { neon } from '@neondatabase/serverless';
import jwt from 'jsonwebtoken';
import fs from 'fs';
import path from 'path';
```

La classe `Server` est la fondation de votre implémentation. `StdioServerTransport` gère la communication entre votre serveur MCP et d'autres outils via l'entrée et la sortie standard, ce qui est exactement la façon dont Cursor se connecte en coulisses.

### 3\. Connexion et configuration de la base de données

```typescript
const sql = neon(process.env.DATABASE_URL!);
const TOKEN_FILE = '.auth-token';
```

La constante `TOKEN_FILE` agit comme un système de stockage local léger pour les jetons d'authentification.

### 4. Système d'authentification

Pour gérer les jetons, vous ajouterez trois fonctions utilitaires : `getStoredToken()`, `storeToken()` et `decodeJWT()`.

### 5. Fonctions utilitaires principales

**5.1. Vérifier le statut de facturation**

Cette fonction vérifie le statut de facturation d'un utilisateur et applique une limite d'une seule tâche pour le niveau gratuit. Elle crée également automatiquement un utilisateur dans la base de données s'il n'existe pas.

**5.2. Vérifier la permission de création de tâche**

Il s'agit d'un simple wrapper qui renvoie un booléen pour les vérifications de permission.

### 6. Implémentation principale du serveur

Initialisez votre serveur MCP :

```typescript
const server = new Server(
  {
    name: 'todo-mcp-server',
    version: '1.0.0',
  },
  {
    capabilities: {
      tools: {},
    },
  }
);
```

### 7. Enregistrement des outils

Chaque outil que votre IDE Cursor peut utiliser doit être répertorié. Vous enregistrez ici tous les outils que votre serveur MCP exposera.

Les outils que vous créerez incluent :

* Authentification → `login`, `save_token`, `logout`
    
* Gestion des tâches → `list_todos`, `create_todo`, `update_todo`, `delete_todo`
    
* Facturation → `refresh_billing_status`
    

### 8. Gestionnaires d'outils

Chaque outil a son propre gestionnaire qui vérifie l'authentification, communique avec la base de données et renvoie une réponse structurée.

**8.1. Outil Login**

L'outil `login` est responsable du démarrage du flux d'authentification avec Kinde.

**8.2. Outil Save Token**

L'outil `save_token` gère le stockage local du jeton d'authentification de l'utilisateur.

**8.3. Outil List To-Dos**

L'outil `list_todos` récupère toutes les tâches appartenant à l'utilisateur authentifié.

**8.4. Outil Create To-Do**

L'outil `create_todo` permet aux utilisateurs authentifiés d'ajouter de nouvelles tâches, tout en vérifiant les limites de facturation.

**8.5. Outil Update To-Do**

L'outil `update_todo` permet de modifier le titre, la description ou le statut d'une tâche existante.

**8.6. Outil Delete To-Do**

L'outil `delete_todo` permet de supprimer une tâche spécifique.

**8.7. Outil Refresh Billing Status**

L'outil `refresh_billing_status` permet de forcer une nouvelle vérification du statut de facturation depuis Kinde.

**8.8. Outil Logout**

L'outil `logout` permet de mettre fin à la session en effaçant le jeton stocké localement.

### 9\. Fichier `server.ts` complet

Vous pouvez consulter l'implémentation complète du fichier `server.ts` dans le [dépôt GitHub](https://github.com/sholajegede/todo_mcp_server/blob/main/src/server.ts).

### 10\. Flux de données et intégration

Flux complet des données :

```markdown
Entrée utilisateur 
   → Serveur MCP 
      → Vérification de l'authentification
         → Vérification de la facturation
            → Opération de base de données
               → Réponse
```

Diagramme :

```mermaid
flowchart LR
    A[Entrée utilisateur] --> B[Serveur MCP]
    B --> C{Authentifié ?}
    C -- Non --> D[Rejeter la requête]
    C -- Oui --> E{Facturation OK ?}
    E -- Non --> F[Rejeter la requête]
    E -- Oui --> G[Opération de base de données]
    G --> H[Mise à jour usage + Réponse]
```

### 11. Gestion des erreurs et sécurité

* **Validation JWT** : Chaque requête valide le jeton JWT.
* **Isolation utilisateur** : Les utilisateurs ne peuvent accéder qu'à leurs propres tâches.
* **Prévention de l'injection SQL** : Utilisation de requêtes paramétrées.

### 12. Tests et déploiement

Enfin, démarrez le serveur MCP et testez-le avec `npm run dev`.

## **Tester le système complet**

### 1\. Démarrer les services

```powershell
# Terminal 1 : Démarrer le serveur MCP
npm run dev

# Terminal 2 : Démarrer le serveur d'authentification Kinde
npm run auth-server
```

### 2\. Configurer Cursor MCP

Dans votre projet Cursor :

* Allez dans Settings → Tools & MCP → New MCP Server
* Modifiez le fichier `~/.cursor/mcp.json` et collez le code de configuration avec vos identifiants.

### 3\. Tester le flux complet

Ouvrez votre fenêtre de chat Cursor et testez les commandes MCP : *login*, *save_token*, *list to-dos*, *create to-do*, *refresh billing status*.

## Dépannage

### 1\. Serveur MCP non détecté
* Vérifiez la syntaxe de votre fichier `mcp.json`.
* Assurez-vous que les chemins de fichiers sont des **chemins absolus**.
* Redémarrez Cursor.

### 2\. Problèmes de connexion à la base de données
* Vérifiez votre variable `DATABASE_URL`.
* Assurez-vous que votre base de données Neon est active.

### 3\. Problèmes d'authentification Kinde
* Vérifiez les URL de redirection dans le tableau de bord Kinde.
* Assurez-vous que votre serveur d'authentification tourne sur le port `3000`.

### 4\. Erreurs de jeton
* Utilisez le jeton ID fourni par Kinde, pas le jeton d'accès.

## Architecture finale du serveur MCP

```markdown
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Cursor IDE    │    │   Serveur MCP    │    │  Auth Kinde     │
│                 │◄──►│                  │◄──►│   Serveur       │
│ - Outils MCP    │    │ - CRUD Tâches    │    │ - Flux OAuth    │
│ - Interface Chat│    │ - Facturation    │    │ - Stockage Jeton│
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │ Neon PostgreSQL │
                       │                 │
                       │ - Table Users    │
                       │ - Table Todos    │
                       │ - Données Fact. │
                       └─────────────────┘
```

## Conclusion

Vous venez de construire un serveur MCP entièrement fonctionnel avec :

* **Authentification** → connexions sécurisées avec Kinde
    
* **Persistance des données** → tâches stockées dans Neon
    
* **Application de la facturation** → limites d'utilisation + chemin de mise à niveau
    
* **Exposition des outils** → outils MCP accessibles dans Cursor
    

### Étapes suivantes

Voici quelques idées pour étendre ce que vous avez construit :

* **Contrôle d'accès basé sur les rôles (RBAC) :** créez des permissions administrateur vs utilisateur normal.
* **Niveaux de facturation :** proposez des forfaits gratuit, pro et entreprise.
* **Fonctionnalités :** ajoutez la recherche, des tags ou le partage de tâches.

### Ressources

Vous pouvez trouver le code source complet de ce tutoriel dans [ce dépôt GitHub](https://github.com/sholajegede/todo_mcp_server). Si cela vous a aidé, n'hésitez pas à lui donner une étoile (⭐) ! Vous pouvez également me mentionner sur X [@wani\_shola](https://x.com/wani_shola) ou [me contacter sur LinkedIn](https://www.linkedin.com/in/sholajegede).