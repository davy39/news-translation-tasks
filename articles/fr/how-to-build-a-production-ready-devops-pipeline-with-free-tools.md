---
title: Comment construire un pipeline DevOps prêt pour la production avec des outils
  gratuits
subtitle: ''
author: Opaluwa Emidowojo
co_authors: []
series: null
date: '2025-04-28T20:15:34.331Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-production-ready-devops-pipeline-with-free-tools
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1745864420670/f36eb4a7-a24e-4d6e-859f-db7249ae0da0.png
tags:
- name: Devops
  slug: devops
- name: Devops articles
  slug: devops-articles
- name: AWS
  slug: aws
- name: Beginner Developers
  slug: beginners
- name: Kubernetes
  slug: kubernetes
- name: GitHub
  slug: github
- name: Terraform
  slug: terraform
- name: Docker
  slug: docker
- name: Node.js
  slug: nodejs
- name: YAML
  slug: yaml
seo_title: Comment construire un pipeline DevOps prêt pour la production avec des
  outils gratuits
seo_desc: 'A few months ago, I dove into DevOps, expecting it to be an expensive journey
  requiring costly tools and infrastructure. But I discovered you can build professional-grade
  pipelines using entirely free resources.

  If DevOps feels out of reach because y...'
---

Il y a quelques mois, je me suis lancé dans DevOps, m'attendant à ce que ce soit un voyage coûteux nécessitant des outils et une infrastructure onéreux. Mais j'ai découvert qu'il est possible de construire des pipelines de qualité professionnelle en utilisant uniquement des ressources gratuites.

Si DevOps vous semble inaccessible en raison des coûts, ne vous inquiétez pas. Je vais vous guider étape par étape pour créer un pipeline prêt pour la production sans dépenser un centime. Commençons !

## Table des matières

1. [Prérequis](#heading-prerequisites)
    
2. [Introduction](#introduction)
    
3. [Comment configurer votre contrôle de source et la structure de votre projet](#heading-how-to-set-up-your-source-control-and-project-structure)
    
4. [Comment construire votre pipeline CI avec GitHub Actions](#heading-how-to-build-your-ci-pipeline-with-github-actions)
    
5. [Comment optimiser les builds Docker pour CI](#heading-how-to-optimize-docker-builds-for-ci)
    
6. [Infrastructure as Code en utilisant Terraform et des fournisseurs cloud gratuits](#heading-infrastructure-as-code-using-terraform-and-free-cloud-providers)
    
7. [Comment configurer l'orchestration de conteneurs sur des ressources minimales](#heading-how-to-set-up-container-orchestration-on-minimal-resources)
    
8. [Comment créer un pipeline de déploiement gratuit](#heading-how-to-create-a-free-deployment-pipeline)
    
9. [Comment construire un système de monitoring complet](#heading-how-to-build-a-comprehensive-monitoring-system)
    
10. [Comment implémenter des tests de sécurité et des analyses](#heading-how-to-implement-security-testing-and-scanning)
    
11. [Optimisation des performances et mise à l'échelle](#heading-performance-optimization-and-scaling)
    
12. [Tout mettre ensemble](#heading-complete-cicd-pipeline-example)
    
13. [Conclusion](#conclusion)
    

## \ud83d\udee0 Prérequis

* **Connaissances de base en Git** : Cloner des dépôts, créer des branches, commiter du code et créer des PR
    
* **Familiarité avec la ligne de commande** : Pour Docker, Terraform et Kubernetes
    
* **Compréhension de base de CI/CD** : Concepts d'intégration/délivrance continue et pipelines
    

### Comptes nécessaires :

* Compte GitHub
    
* Au moins un fournisseur cloud : AWS Free Tier (recommandé), Oracle Cloud Free Tier, ou Google Cloud/Azure avec des crédits gratuits
    
* Terraform Cloud (niveau gratuit) pour la gestion de l'état de l'infrastructure
    
* Grafana Cloud (niveau gratuit) pour le monitoring
    
* UptimeRobot (niveau gratuit) pour les vérifications de disponibilité externe
    

### Outils à installer localement

| **Outil** | **Objectif** | **Lien d'installation** |
| --- | --- | --- |
| Git | Contrôle de version | [**Installer Git**](https://git-scm.com/downloads) |
| Docker | Conteneurisation | [**Installer Docker**](https://docs.docker.com/get-docker/) |
| Node.js & npm | Application exemple et builds | [**Installer Node.js**](https://nodejs.org/) |
| Terraform | Infrastructure as Code | [**Installer Terraform**](https://www.terraform.io/downloads) |
| kubectl | CLI Kubernetes | [**Installer kubectl**](https://kubernetes.io/docs/tasks/tools/) |
| k3d | Kubernetes léger | [**Installer k3d**](https://k3d.io/) |
| Trivy | Analyse de sécurité des conteneurs | [**Installer Trivy**](https://aquasecurity.github.io/trivy/v0.18.3/) |
| OWASP ZAP | Analyse de sécurité web | [**Installer ZAP**](https://www.zaproxy.org/download/) |

**Optionnel mais utile :**

* [**VS Code**](https://code.visualstudio.com/) ou tout bon éditeur de code
    
* Postman pour tester les APIs
    
* Compréhension de YAML et des Dockerfiles
    

## Introduction

Lorsque les gens entendent "DevOps", ils imaginent souvent des systèmes d'entreprise complexes alimentés par des outils coûteux et des services cloud premium. Mais la vérité est que vous n'avez pas besoin d'un budget énorme pour construire un pipeline DevOps solide et professionnel. Les fondements d'un bon DevOps - automatisation, cohérence, sécurité et visibilité - peuvent être construits entièrement avec des outils gratuits.

Dans ce guide, vous apprendrez à construire un pipeline DevOps prêt pour la production en utilisant des ressources sans coût. Nous utiliserons une simple application CRUD (Create, Read, Update, Delete) avec un frontend, une API backend et une base de données comme projet exemple pour démontrer chaque étape du processus.

## Comment configurer votre contrôle de source et la structure de votre projet

### 1\. Créer un dépôt bien structuré

Un dépôt propre est la fondation de votre pipeline. Nous allons configurer :

* Des dossiers séparés pour `frontend`, `backend` et `infrastructure`
    
* Un dossier `.github` pour contenir les configurations de workflow
    
* Des conventions de nommage claires et un `README.md` bien rédigé
    

\ud83d\udee0 **Astuce** : Utilisez des messages de commit sémantiques et envisagez d'adopter [**Conventional Commits**](https://www.conventionalcommits.org/) pour plus de clarté dans le versionnage et les journaux de modifications.

### 2\. Configurer la protection des branches sans fonctionnalités payantes

Bien que les règles plus avancées de GitHub nécessitent Pro, vous pouvez toujours :

* Exiger des pull requests avant de fusionner
    
* Activer les vérifications de statut pour empêcher le code cassé d'atterrir dans `main`
    
* Imposer un historique linéaire pour un contrôle de version plus propre
    

\ud83d\udca1 Cela rend votre projet plus sûr et plus collaboratif, sans avoir besoin de GitHub Enterprise.

### 3\. Implémenter des modèles de PR et des vérifications automatisées

Rendez vos revues plus fluides :

* Ajoutez un `PULL_REQUEST_TEMPLATE.md` pour guider les contributeurs
    
* Utilisez GitHub Actions (que nous configurerons dans la partie suivante) pour le linting, les tests et les vérifications de formatage
    

\u2728 Ces petites améliorations ajoutent de la finesse et du professionnalisme.

### 4\. Configurer les modèles d'issues GitHub et les tableaux de projet

Même les développeurs solo bénéficient du suivi des issues :

* Ajoutez des modèles d'issues pour les bugs et les fonctionnalités
    
* Utilisez GitHub Projects pour gérer le travail avec un tableau Kanban, tout gratuit et natif à GitHub
    

\ud83d\udccc **Bonus** : Cette configuration pose les bases des pratiques GitOps plus tard.

### 5\. Technique avancée : Configurer des scripts de validation personnalisés en tant que hooks de pré-commit

Avant que le code n'atteigne GitHub, vous pouvez attraper les problèmes localement avec les hooks Git. En utilisant un outil comme [**Husky**](https://typicode.github.io/husky/) ou [**pre-commit**](https://pre-commit.com/), vous pouvez :

* Linter le code avant qu'il ne soit commité
    
* Exécuter des tests ou des formatteurs automatiquement
    
* Empêcher les secrets d'être commités accidentellement
    

```json
// Initialiser Husky et installer les dépendances nécessaires
// Puis ajouter un hook de pré-commit qui exécute les tests avant d'autoriser le commit
npx husky-init && npm install
npx husky add .husky/pre-commit "npm test"
```

### **6\. Configuration de l'application CRUD exemple :**

Notre application CRUD gère les utilisateurs (créer, lire, mettre à jour, supprimer). Voici le code minimal avec des commentaires pour expliquer chaque partie :

**Backend** `(backend/)`:

```json
// backend/package.json
{
  "name": "crud-backend", // Nom du projet backend
  "version": "1.0.0", // Version pour suivre les changements
  "scripts": {
    "start": "node index.js", // Lance le serveur
    "test": "echo 'Ajoutez des tests ici'", // Placeholder pour les tests (à mettre à jour avec Jest plus tard)
    "lint": "eslint ." // Vérifie le style de code avec ESLint
  },
  "dependencies": {
    "express": "^4.17.1", // Framework web pour les endpoints API
    "pg": "^8.7.3" // Client PostgreSQL pour se connecter à la base de données
  },
  "devDependencies": {
    "eslint": "^8.0.0" // Outil de linting pour la qualité du code
  }
}
```

```javascript
// backend/index.js
const express = require('express'); // Importer Express pour construire l'API
const { Pool } = require('pg'); // Importer le client PostgreSQL
const app = express(); // Créer une application Express
app.use(express.json()); // Analyser les corps de requête JSON

// Se connecter à PostgreSQL en utilisant DATABASE_URL depuis les variables d'environnement
const pool = new Pool({ connectionString: process.env.DATABASE_URL });

// Endpoint de vérification de santé pour les sondes Kubernetes et le monitoring
app.get('/healthz', (req, res) => res.json({ status: 'ok' }));

// Obtenir tous les utilisateurs de la base de données
app.get('/users', async (req, res) => {
  const { rows } = await pool.query('SELECT * FROM users'); // Interroger la table users
  res.json(rows); // Envoyer les utilisateurs en JSON
});

// Ajouter un nouvel utilisateur à la base de données
app.post('/users', async (req, res) => {
  const { name } = req.body; // Obtenir le nom du corps de la requête
  // Insérer l'utilisateur et retourner le nouvel enregistrement
  const { rows } = await pool.query('INSERT INTO users(name) VALUES($1) RETURNING *', [name]);
  res.json(rows[0]); // Envoyer le nouvel utilisateur en JSON
});

// Démarrer le serveur sur le port 3000
app.listen(3000, () => console.log('Backend en cours d\'exécution sur le port 3000'));
```

**Frontend** `(frontend/)`:

```javascript
// frontend/package.json
{
  "name": "crud-frontend", // Nom du projet frontend
  "version": "1.0.0", // Version pour suivre les changements
  "scripts": {
    "start": "react-scripts start", // Lance le serveur de développement
    "build": "react-scripts build", // Construit pour la production
    "test": "react-scripts test", // Lance les tests (placeholder pour Jest)
    "lint": "eslint ." // Vérifie le style de code avec ESLint
  },
  "dependencies": {
    "react": "^17.0.2", // Bibliothèque principale React
    "react-dom": "^17.0.2", // Rend React dans le DOM
    "react-scripts": "^4.0.3", // Scripts pour le développement React
    "axios": "^0.24.0" // Client HTTP pour les appels API
  },
  "devDependencies": {
    "eslint": "^8.0.0" // Outil de linting pour la qualité du code
  }
}
```

```javascript
// frontend/src/App.js
import React, { useState, useEffect } from 'react'; // Importer React et les hooks
import axios from 'axios'; // Importer Axios pour les requêtes API

function App() {
  // État pour stocker les utilisateurs récupérés depuis le backend
  const [users, setUsers] = useState([]);
  // État pour le champ de saisie pour ajouter un nouvel utilisateur
  const [name, setName] = useState('');

  // Récupérer les utilisateurs lorsque le composant est monté
  useEffect(() => {
    axios.get('http://localhost:3000/users').then(res => setUsers(res.data));
  }, []); // Tableau vide signifie exécuter une fois au montage

  // Ajouter un nouvel utilisateur via l'API
  const addUser = async () => {
    const res = await axios.post('http://localhost:3000/users', { name }); // Poster un nouvel utilisateur
    setUsers([...users, res.data]); // Mettre à jour la liste des utilisateurs
    setName(''); // Effacer le champ de saisie
  };

  return (
    <div>
      <h1>Utilisateurs</h1>
      {/* Saisie pour le nom du nouvel utilisateur */}
      <input value={name} onChange={e => setName(e.target.value)} />
      {/* Bouton pour ajouter un utilisateur */}
      <button onClick={addUser}>Ajouter un utilisateur</button>
      {/* Lister tous les utilisateurs */}
      <ul>{users.map(user => <li key={user.id}>{user.name}</li>)}</ul>
    </div>
  );
}

export default App; // Exporter le composant
```

**Configuration de la base de données** :

```pgsql
-- infra/db.sql
-- Créer une table pour stocker les utilisateurs
CREATE TABLE users (
  id SERIAL PRIMARY KEY, -- ID auto-incrémenté
  name VARCHAR(100) NOT NULL -- Nom de l'utilisateur, requis
);
```

```javascript
crud-app/
 backend/
    package.json
    index.js
 frontend/
    package.json
    src/App.js
 infra/
    db.sql
 .github/
    workflows/
 README.md
```

Cette application fournit un endpoint `/users` (GET/POST) et un frontend pour lister/ajouter des utilisateurs, stockés dans PostgreSQL. L'endpoint `/healthz` supporte le monitoring. Enregistrez ce code dans votre dépôt pour suivre les étapes du pipeline.

## Comment construire votre pipeline CI avec GitHub Actions

### 1\. Configurer votre premier workflow GitHub Actions

Tout d'abord, créons un workflow de base qui construit, teste et lint votre application à chaque fois que vous poussez du code ou ouvrez une pull request. Cela garantit que votre application reste saine et que tout problème est détecté tôt.

Créez un fichier à `.github/workflows/ci.yml` et ajoutez ce qui suit :

```yaml
# Workflow CI pour construire, tester et lint l'application CRUD lors d'un push ou d'une pull request
name: CI Pipeline
on:
  push:
    branches: [main] # Déclencher lors des pushes sur la branche main
  pull_request:
    branches: [main] # Déclencher lors des PR sur la branche main
jobs:
  build:
    runs-on: ubuntu-latest # Utiliser le runner Linux gratuit de GitHub
    steps:
      - uses: actions/checkout@v3 # Vérifier le code du dépôt
      - name: Configurer Node.js # Installer l'environnement Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18' # Utiliser Node.js 18 pour la cohérence
      - name: Mettre en cache les dépendances # Mettre en cache node_modules pour accélérer les builds
        uses: actions/cache@v3
        with:
          path: ~/.npm # Mettre en cache le cache global de npm
          key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }} # Clé basée sur le système d'exploitation et package-lock.json
      - run: npm ci # Installer les dépendances de manière fiable en utilisant package-lock.json
      - run: npm test # Exécuter les tests définis dans package.json
      - run: npm run lint # Exécuter ESLint pour garantir la qualité du code
```

Ce workflow s'exécute automatiquement à chaque push et pull request sur la branche `main`. Il installe les dépendances, exécute les tests et effectue le linting du code, avec une mise en cache des dépendances pour rendre les builds plus rapides au fil du temps.

**Problèmes courants et solutions :**

* **"Secret non trouvé"** : Assurez-vous que `AWS_ACCESS_KEY_ID` est dans les secrets du dépôt (Paramètres → Secrets).
    
* **Les tests échouent** : Vérifiez `test/users.test.js` pour la connectivité à la base de données.
    

#### Comprendre les limites du niveau gratuit de GitHub Actions

Avant de construire plus de workflows, il est important de savoir ce que GitHub offre gratuitement.

Si vous travaillez sur des dépôts privés, vous obtenez 2 000 minutes gratuites par mois. Pour les dépôts publics, vous obtenez des minutes illimitées.

Pour éviter d'atteindre rapidement les limites :

* Mettez en cache vos dépendances pour réduire les temps d'installation.
    
* Ne déclenchez les workflows que sur des branches significatives (comme `main` ou `release`).
    
* Sautez les étapes inutiles lorsque vous le pouvez.
    

### 2\. Créer un pipeline de build multi-étapes

À mesure que votre application grandit, il est préférable de diviser votre pipeline CI en étapes claires comme **install**, **test** et **lint**. Cette structure rend les workflows plus faciles à maintenir et accélère les choses, car certaines tâches peuvent s'exécuter en parallèle.

Voici comment vous pouvez diviser le travail en plusieurs tâches pour plus de clarté :

```yaml
jobs:
  install:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: npm ci  # Installation propre des dépendances

  test:
    needs: install  # Cette tâche dépend de la fin de la tâche d'installation
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: npm test  # Exécuter la suite de tests

  lint:
    needs: install  # Cette tâche dépend également de l'installation mais s'exécute en parallèle avec le test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: npm run lint  # Exécuter les vérifications de linting
```

En divisant le pipeline en étapes, vous pouvez rapidement identifier quelle étape échoue, et vos tâches de test et de linting peuvent s'exécuter simultanément après l'installation des dépendances.

### 3\. Implémenter des builds matriciels pour les tests multi-environnements

Lorsque vous souhaitez que votre application fonctionne sur différentes versions de Node.js ou bases de données, les builds matriciels sont votre meilleur atout. Ils vous permettent de tester sur plusieurs environnements en parallèle, sans dupliquer de code.

Voici comment vous pouvez configurer une stratégie matricielle, pour tester sur plusieurs environnements simultanément :

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: [14.x, 16.x, 18.x]  # Test sur plusieurs versions de Node
        database: [postgres, mysql]        # Test contre différentes bases de données
    steps:
      - uses: actions/checkout@v3
      - name: Utiliser Node.js ${{ matrix.node-version }}
        uses: actions/setup-node@v3
        with:
          node-version: ${{ matrix.node-version }}
      - run: npm install
      - run: npm test  # Cela exécutera 6 combinaisons de tests différentes (3 versions de Node × 2 bases de données)
```

Les builds matriciels permettent de gagner du temps et de détecter tôt les bugs spécifiques à un environnement.

### 4\. Optimiser le workflow avec la mise en cache des dépendances

Chaque seconde compte dans CI. La mise en cache des dépendances peut aider à économiser des minutes dans votre workflow en réutilisant les packages précédemment installés au lieu de les réinstaller à partir de zéro à chaque fois.

Voici comment configurer une mise en cache intelligente pour accélérer vos builds :

```yaml
- name: Mettre en cache les modules node
  uses: actions/cache@v3
  with:
    path: |  # Mettre en cache à la fois le cache global de npm et les node_modules locaux
      ~/.npm
      node_modules
    key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}  # Clé de cache basée sur le système d'exploitation et les dépendances
    restore-keys: |  # Clés de secours si la correspondance exacte n'est pas trouvée
      ${{ runner.os }}-node-
```

Cette configuration de cache vérifie si vos dépendances ont changé. Si ce n'est pas le cas, elle restaure le cache, rendant les builds significativement plus rapides.

## Comment optimiser les builds Docker pour CI

Lorsque vous construisez des images Docker dans CI, le temps de build peut rapidement devenir un goulot d'étranglement. Surtout si vos images sont volumineuses. Optimiser vos builds Docker rend vos pipelines beaucoup plus rapides, économise de la bande passante et produit des images plus petites et plus efficaces, prêtes pour le déploiement.

Dans cette section, je vais vous guider à travers la création d'un Dockerfile de base, l'utilisation de builds multi-étapes, la mise en cache des couches et l'activation de BuildKit pour des builds encore plus rapides.

### 1\. Créer un Dockerfile de base

Tout d'abord, commencez par un Dockerfile simple qui installe les dépendances de votre application et l'exécute. C'est ce que vous optimiserez plus tard.

```dockerfile
# Dockerfile simple pour une application Node.js
FROM node:18-alpine  # Utiliser Alpine pour une image de base plus petite
WORKDIR /app         # Définir le répertoire de travail
COPY . .             # Copier tous les fichiers dans le conteneur
RUN npm ci           # Installer les dépendances (installation propre)
CMD ["npm", "start"] # Démarrer l'application
```

L'utilisation d'une image Node.js basée sur Alpine aide à garder votre image petite dès le départ.

### 2\. Builds Docker multi-étapes

Ensuite, séparons le processus de build de l'image de production. Les builds multi-étapes vous permettent de compiler ou de construire votre application dans une étape et de copier uniquement le produit final dans une image propre et plus petite. Cela garde les images de production légères :

```dockerfile
# Étape 1 : Construire l'application
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./  # Copier les fichiers package en premier pour une meilleure mise en cache
RUN npm ci             # Installer toutes les dépendances
COPY . .               # Ensuite, copier le code source
RUN npm run build      # Construire l'application

# Étape 2 : Image de production avec une empreinte minimale
FROM node:18-alpine
WORKDIR /app
# Copier uniquement les actifs construits et les dépendances de production
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/package*.json ./
RUN npm ci --production  # Installer uniquement les dépendances de production
CMD ["node", "dist/server.js"]  # Exécuter l'application construite
```

Cette approche garde vos images de production légères et sécurisées en excluant les outils de build inutiles et les dépendances de développement.

### 3\. Optimisation de la mise en cache des couches

Pour des builds encore plus rapides, organisez vos instructions `Dockerfile` pour maximiser la mise en cache des couches. Copiez et installez les dépendances *avant* de copier votre code source complet.

De cette façon, Docker réutilise l'étape de cache npm install si vos dépendances n'ont pas changé, même si vous modifiez le code de votre application :

* D'abord : `COPY package*.json ./`
    
* Ensuite : `RUN npm ci`
    
* Enfin : `COPY . .`
    

### 4\. Activer BuildKit pour des builds plus rapides

Docker BuildKit est un moteur de build plus récent qui permet des fonctionnalités comme une meilleure mise en cache, des étapes de build parallèles et des builds globalement plus rapides.

Pour activer BuildKit pendant votre CI, exécutez :

```dockerfile
- name: Construire l'image Docker
  run: |
    # Activer BuildKit pour des builds parallèles et plus efficaces
    DOCKER_BUILDKIT=1 docker build -t myapp:latest .
```

L'activation de BuildKit peut considérablement accélérer les builds Docker complexes et est fortement recommandée pour tous les pipelines CI.

## Infrastructure as Code en utilisant Terraform et des fournisseurs cloud gratuits

### Pourquoi Infrastructure as Code (IaC) est important

Lorsque vous gérez l'infrastructure manuellement - c'est-à-dire en cliquant dans les tableaux de bord cloud ou en configurant les choses à la main - il est facile de perdre la trace de ce que vous avez fait et de la manière de le répéter.

Infrastructure as Code (IaC) résout ce problème en vous permettant de définir votre infrastructure avec du code, de la versionner comme du code d'application et de suivre chaque changement au fil du temps. Cela rend vos configurations faciles à reproduire dans différents environnements (développement, staging, production), garantit que les changements sont déclaratifs et audités, et réduit les erreurs humaines.

Que vous déployiez un seul serveur ou que vous mettez à l'échelle un système complexe, IaC pose les bases d'une infrastructure de qualité professionnelle dès le premier jour, vous permettant d'automatiser, de documenter et de faire croître votre environnement de manière systématique.

### Comment provisionner l'infrastructure avec Terraform

#### Initialiser un projet Terraform

Tout d'abord, définissez les fournisseurs et les versions dont vous avez besoin. Ici, nous utilisons le service d'hébergement cloud gratuit de Render :

```yaml
# Définir les fournisseurs requis et les versions
terraform {
  required_providers {
    render = {
      source  = "renderinc/render"  # Utilisation du niveau gratuit de Render
      version = "0.1.0"             # Spécifier la version du fournisseur pour la stabilité
    }
  }
}

# Configurer le fournisseur Render avec authentification
provider "render" {
  api_key = var.render_api_key  # Stocker la clé API comme variable
}
```

Ensuite, configurez le fournisseur en vous authentifiant avec votre clé API. Il est recommandé de stocker les secrets comme les clés API dans des variables au lieu de les coder en dur. Cette configuration indique à Terraform sur quelle plateforme vous travaillez (Render) et comment s'authentifier pour gérer les ressources automatiquement.

#### Provisionner une application web sur Render

Ensuite, définissez l'infrastructure que vous souhaitez - dans ce cas, un service web hébergé sur Render :

```yaml
# Définir un service web sur le niveau gratuit de Render
resource "render_service" "web_app" {
  name = "ci-demo-app"                                 # Nom du service
  type = "web_service"                                 # Type de service
  repo = "https://github.com/YOUR-USERNAME/YOUR-REPO"  # Dépôt source
  env = "docker"                                       # Utiliser l'environnement Docker
  plan = "starter"                                     # Plan du niveau gratuit
  branch = "main"                                      # Déployer depuis la branche main
  build_command = "docker build -t app ."              # Commande de build
  start_command = "docker run -p 3000:3000 app"        # Commande de démarrage
  auto_deploy = true                                   # Déploiement automatique sur les commits
}
```

Ce bloc de ressource décrit exactement comment votre application doit être déployée. Chaque fois que vous modifiez ce fichier et réappliquez, Terraform mettra à jour l'infrastructure pour correspondre.

#### Provisionner PostgreSQL gratuitement

La plupart des applications ont besoin d'une base de données, mais vous n'avez pas à payer pour une lorsque vous commencez. Des plateformes comme [Railway](https://railway.app/) offrent des niveaux gratuits qui sont parfaits pour le développement et les petits projets.

Vous pouvez rapidement créer une instance PostgreSQL gratuite en vous inscrivant sur la plateforme et en cliquant sur **"Créer un nouveau projet"**. À la fin, vous obtiendrez un `DATABASE_URL`, une chaîne de connexion que votre application utilisera pour communiquer avec la base de données.

#### Connecter l'application à la base de données

Dans Render (ou quelle que soit la plateforme que vous utilisez), définissez une variable d'environnement appelée `DATABASE_URL` et collez la chaîne de connexion de votre fournisseur PostgreSQL. Cela permet à votre application d'accéder en toute sécurité à la base de données sans coder en dur les informations d'identification dans votre base de code.

#### Rendre cela reproductible

Une fois tout défini, utilisez Terraform pour créer et appliquer un plan d'infrastructure :

```yaml
# Créer un plan d'exécution et l'enregistrer dans un fichier
terraform plan -out=infra.tfplan
# Appliquer le plan enregistré exactement comme prévu
terraform apply infra.tfplan
```

Enregistrer le plan dans un fichier (`infra.tfplan`) garantit que vous appliquez exactement ce que vous avez revu, donc il n'y aura pas de surprises.

**Problèmes courants et solutions :**

* **Fournisseur non trouvé** : Exécutez `terraform init`.
    
* **Erreur de clé API** : Vérifiez `render_api_key` dans les variables Terraform Cloud.
    

## Comment configurer l'orchestration de conteneurs sur des ressources minimales

Lorsque vous travaillez avec des ressources limitées comme un ordinateur portable, un petit serveur ou une VM cloud légère, la configuration de Kubernetes complet peut être écrasante. Au lieu de cela, vous pouvez utiliser **K3d**, une distribution Kubernetes légère qui s'exécute dans des conteneurs Docker. Voici comment configurer un cluster minimal et efficace pour le développement local ou les tests.

### 1\. Installer K3d pour Kubernetes local

Tout d'abord, installez K3d. C'est une manière super légère d'exécuter des clusters Kubernetes dans Docker sans avoir besoin d'une configuration lourde comme Minikube.

```bash
# Télécharger et installer K3d - une distribution K8s légère
curl -s https://raw.githubusercontent.com/k3d-io/k3d/main/install.sh | bash
```

### 2\. Créer un cluster K3d léger

Une fois K3d installé, vous pouvez lancer un cluster avec des nœuds minimaux pour économiser des ressources.

```bash
# Créer un cluster K8s minimal avec 1 serveur et 2 nœuds agents
k3d cluster create dev-cluster \
  --servers 1 \                        # Nœud serveur unique pour minimiser l'utilisation des ressources
  --agents 2 \                         # Deux nœuds workers pour la distribution des pods
  --volume /tmp/k3dvol:/tmp/k3dvol \   # Monter le volume local pour la persistance
  --port 8080:80@loadbalancer \        # Mapper le port 8080 localement au port 80 dans le cluster
  --api-port 6443                      # Définir le port de l'API
```

Cette configuration vous donne un **cluster Kubernetes minuscule mais réel** qui est parfait pour l'expérimentation.

### 3\. Déployer avec des manifestes Kubernetes optimisés

Maintenant que votre cluster est en cours d'exécution, vous pouvez déployer votre application. Il est important de définir soigneusement les demandes et limites de ressources afin que vos pods ne consomment pas trop de mémoire ou de CPU.

```bash
# Manifest de déploiement optimisé pour les ressources
apiVersion: apps/v1
kind: Deployment
metadata:
  name: webapp  # Nom du déploiement
spec:
  replicas: 1   # Réplique unique pour économiser les ressources
  selector:
    matchLabels:
      app: webapp
  template:
    metadata:
      labels:
        app: webapp
    spec:
      containers:
        - name: app
          image: myapp:latest
          resources:
            # Définir des demandes de ressources minimales
            requests:
              memory: "64Mi"   # Demander seulement 64 Mo de mémoire
              cpu: "50m"       # Demander seulement 5 % d'un cœur de CPU
            # Définir des limites raisonnables
            limits:
              memory: "128Mi"  # Limiter à 128 Mo de mémoire
              cpu: "100m"      # Limiter à 10 % d'un cœur de CPU
```

Cela garantit que Kubernetes sait combien allouer et éviter de surcharger votre environnement léger.

### 4\. Configurer GitOps avec Flux

Pour gérer les déploiements automatiquement depuis votre dépôt GitHub, vous pouvez configurer GitOps en utilisant Flux.

```bash
# Installer le CLI Flux
brew install fluxcd/tap/flux

# Initialiser Flux sur votre cluster connecté à votre dépôt GitHub
flux bootstrap github \
  --owner=YOUR_GITHUB_USERNAME \    # Votre nom d'utilisateur GitHub
  --repository=YOUR_REPO_NAME \     # Dépôt pour stocker les manifestes Flux
  --branch=main \                   # Branche à utiliser
  --path=clusters/dev-cluster \     # Chemin dans le dépôt pour les configs du cluster
  --personal                        # Drapeau pour compte personnel
```

Flux surveille votre dépôt et applique les mises à jour à votre cluster, gardant tout déclaratif et reproductible.

**Problèmes courants et solutions :**

* **Les pods crashent** : Exécutez `kubectl logs pod-name` ou augmentez les ressources.
    
* **La synchronisation Flux échoue** : Vérifiez les permissions du token GitHub.
    

## Comment créer un pipeline de déploiement gratuit

Comme je l'ai dit initialement, tous les projets n'ont pas besoin d'une infrastructure coûteuse. Si vous commencez tout juste ou construisez des projets secondaires, les niveaux gratuits des fournisseurs cloud peuvent couvrir beaucoup de terrain.

### 1\. Comprendre les limitations des niveaux gratuits

Voici un aperçu rapide des niveaux gratuits populaires des clouds :

| Fournisseur | Points forts du niveau gratuit |
| --- | --- |
| AWS Free Tier | 750 heures/mois EC2, 5 Go S3, 1M de requêtes Lambda |
| Oracle Cloud Free Tier | 2 instances de calcul toujours gratuites, 30 Go de stockage |
| Google Cloud Free Tier | 1 instance f1-micro, 5 Go de stockage |

Connaître ces limites vous aide à rester dans le budget.

### 2\. Configurer les workflows de déploiement

Vous pouvez automatiser les déploiements avec GitHub Actions. Voici un exemple de workflow de déploiement vers AWS :

```yaml
# Workflow GitHub Action pour le déploiement vers AWS
name: AWS Deployment

on:
  push:
    branches:
      - main  # Déployer lors d'un push sur la branche main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3  # Vérifier le code

      # Configurer les identifiants AWS à partir des secrets GitHub
      - name: Configurer les identifiants AWS
        uses: aws-actions/configure-aws-credentials@v1
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1

      # Construire l'image Docker
      - name: Construire l'image Docker
        run: docker build -t myapp .

      # Pousser l'image vers AWS ECR
      - name: Pousser l'image Docker vers ECR
        run: |
          # Créer le dépôt s'il n'existe pas (ignorer les erreurs s'il existe)
          aws ecr create-repository --repository-name myapp || true

          # Se connecter à ECR
          aws ecr get-login-password | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.us-east-1.amazonaws.com

          # Taguer et pousser l'image
          docker tag myapp:latest <aws_account_id>.dkr.ecr.us-east-1.amazonaws.com/myapp:latest
          docker push <aws_account_id>.dkr.ecr.us-east-1.amazonaws.com/myapp:latest
```

### 3\. Implémenter des déploiements sans temps d'arrêt

Le zéro temps d'arrêt est crucial. Kubernetes rend cela facile avec les mises à jour progressives :

```yaml
# Déploiement Kubernetes configuré pour des mises à jour sans temps d'arrêt
apiVersion: apps/v1
kind: Deployment
metadata:
  name: crud-app
spec:
  replicas: 3  # Plusieurs répliques pour une haute disponibilité
  selector:
    matchLabels:
      app: crud-app
  template:
    metadata:
      labels:
        app: crud-app
    spec:
      containers:
      - name: app
        image: <docker_registry>/crud-app:latest
        ports:
        - containerPort: 80  # Exposer le port du conteneur
```

En ayant plusieurs répliques, vous garantissez que certains pods restent actifs pendant les mises à jour.

### 4\. Créer un déploiement multi-cloud pour la redondance

Si vous voulez une meilleure fiabilité, vous pouvez déployer sur différents clouds en parallèle :

```yaml
# Déployer sur plusieurs fournisseurs cloud pour la redondance
name: Cross-Cloud Deployment

on:
  push:
    branches:
      - main

jobs:
  # Déployer sur AWS
  aws-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Configuration et déploiement AWS
        run: |
          # Configurer AWS CLI avec les identifiants
          aws configure set aws_access_key_id ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws configure set aws_secret_access_key ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          # Commandes de déploiement AWS...

  # Déployer sur Oracle Cloud en parallèle
  oracle-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Configuration et déploiement Oracle
        run: |
          # Configurer Oracle Cloud CLI
          oci setup config
          # Commandes de déploiement Oracle Cloud...
```

Maintenant, si un cloud tombe en panne, l'autre reste opérationnel.

### 5\. Implémenter des rollbacks automatisés avec des vérifications de santé

Configurez des vérifications de santé pour que Kubernetes puisse effectuer un rollback automatiquement si quelque chose ne va pas :

```yaml
# Déploiement avec vérifications de santé pour les rollbacks automatisés
apiVersion: apps/v1
kind: Deployment
metadata:
  name: crud-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: crud-app
  template:
    metadata:
      labels:
        app: crud-app
    spec:
      containers:
      - name: crud-app
        image: <docker_registry>/crud-app:latest
        ports:
        - containerPort: 80
        # Vérifier si le conteneur est en vie
        livenessProbe:
          httpGet:
            path: /healthz  # Endpoint de vérification de santé
            port: 80
          initialDelaySeconds: 5  # Attendre avant la première vérification
          periodSeconds: 10       # Vérifier toutes les 10 secondes
        # Vérifier si le conteneur est prêt à recevoir du trafic
        readinessProbe:
          httpGet:
            path: /readiness  # Endpoint de vérification de préparation
            port: 80
          initialDelaySeconds: 5  # Attendre avant la première vérification
          periodSeconds: 10       # Vérifier toutes les 10 secondes
```

## Comment construire un système de monitoring complet

Même avec un petit déploiement, le monitoring est essentiel pour détecter les problèmes tôt. Maintenant, je vais vous guider à travers la configuration d'un système de monitoring complet pour votre application.

Vous apprendrez comment intégrer Grafana Cloud pour visualiser vos métriques, utiliser Prometheus pour collecter des données et configurer des alertes personnalisées pour surveiller les performances de votre application. Je couvrirai également le suivi des Objectifs de Niveau de Service (SLO) et la configuration du monitoring externe avec UptimeRobot pour vous assurer que vos endpoints sont toujours disponibles.

### 1\. Configurer le niveau gratuit de Grafana Cloud

Créez un compte Grafana Cloud et connectez Prometheus comme source de données. Ils offrent une utilisation gratuite généreuse, ce qui est parfait pour les petites équipes.

### 2\. Configurer Prometheus pour la collecte de métriques

Prometheus collecte les métriques de votre application.

```yaml
# prometheus.yml - Configuration de base de Prometheus
global:
  scrape_interval: 15s  # Collecter les métriques toutes les 15 secondes
scrape_configs:
  - job_name: 'crud-app'  # Nom de la tâche pour les métriques de crud-app
    static_configs:
      - targets: ['localhost:8080']  # Où collecter les métriques
```

Cela scrute votre application toutes les 15 secondes pour les métriques.

### 3\. Créer des tableaux de bord de monitoring

Grafana visualise les données de Prometheus. Vous pouvez créer des tableaux de bord en utilisant des requêtes comme :

```yaml
# Calculer le taux d'utilisation moyen du CPU par instance sur 1 minute
avg(rate(cpu_usage_seconds_total[1m])) by (instance)
```

Cela calcule l'utilisation moyenne du CPU sur la dernière minute par instance.

### 4\. Écrire des requêtes PromQL personnalisées pour les alertes

Vous pouvez créer des alertes intelligentes pour détecter l'augmentation des taux d'erreur, comme ci-dessous :

```yaml
# Calculer le taux d'erreur en pourcentage du nombre total de requêtes
# Alerter lorsque le taux d'erreur dépasse 5%
sum(rate(http_requests_total{status=~"5.."}[5m])) by (service)
  / 
sum(rate(http_requests_total[5m])) by (service) > 0.05
```

Cela alerte si plus de 5 % de votre trafic entraîne des erreurs.

### 5\. Implémenter le suivi des SLO avec un budget

Vous pouvez suivre les Objectifs de Niveau de Service (SLO) avec Prometheus gratuitement :

```yaml
# Calculer le pourcentage de requêtes complétées en moins de 200 ms
# Alerter lorsqu'il descend en dessous de 99%
rate(http_request_duration_seconds_bucket{le="0.2"}[5m]) 
  / rate(http_request_duration_seconds_count[5m]) 
> 0.99
```

Cela suit si 99 % des requêtes se complètent en moins de 200 ms.

### 6\. Configurer UptimeRobot pour le monitoring externe

Enfin, vous pouvez utiliser UptimeRobot pour vérifier si vos endpoints sont accessibles depuis l'extérieur et recevoir des alertes si quelque chose tombe en panne.

## Comment implémenter des tests de sécurité et des analyses

La sécurité doit être intégrée dans votre pipeline de développement dès le départ, et non ajoutée a posteriori. Dans cette section, je vais vous montrer comment implémenter des tests de sécurité et des analyses à diverses étapes de votre workflow.

Vous utiliserez GitHub CodeQL pour l'analyse statique du code, OWASP ZAP pour analyser les vulnérabilités web et Trivy pour analyser les images de conteneurs. Vous apprendrez également comment appliquer des seuils de sécurité directement dans votre pipeline CI.

### 1\. Activer l'analyse de code GitHub avec CodeQL

GitHub dispose d'une analyse de code intégrée avec CodeQL. Voici comment la configurer :

```yaml
# Workflow GitHub pour l'analyse de sécurité CodeQL
name: CodeQL

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  analyze:
    name: Analyser le code avec CodeQL
    runs-on: ubuntu-latest
    steps:
      - name: Vérifier le code
        uses: actions/checkout@v3

      # Initialiser les outils d'analyse CodeQL
      - name: Configurer CodeQL
        uses: github/codeql-action/init@v2

      # Exécuter l'analyse et générer les résultats
      - name: Analyser le code
        uses: github/codeql-action/analyze@v2
```

Cela analyse automatiquement votre code pour détecter les vulnérabilités de sécurité.

### 2\. Intégrer OWASP ZAP dans votre pipeline CI

Vous pouvez également analyser votre application déployée avec OWASP ZAP comme ceci :

```yaml
# Analyse de sécurité automatisée avec OWASP ZAP
name: ZAP Scan

on:
  push:
    branches:
      - main

jobs:
  zap-scan:
    runs-on: ubuntu-latest
    steps:
      - name: Vérifier le code
        uses: actions/checkout@v3

      # Exécuter l'analyse de sécurité ZAP contre l'application déployée
      - name: Exécuter l'analyse de sécurité ZAP
        uses: zaproxy/action-full-scan@v0.3.0
        with:
          target: 'https://yourapp.com'  # URL à analyser
```

Cela vérifie les vulnérabilités web courantes.

### 3\. Configurer Trivy pour l'analyse des vulnérabilités des conteneurs

Vous pouvez également vérifier vos images de conteneurs pour détecter les vulnérabilités avec Trivy :

```yaml
# Analyser les images Docker pour détecter les vulnérabilités en utilisant Trivy
- name: Exécuter le scanner de vulnérabilités Trivy
  uses: aquasecurity/trivy-action@master
  with:
    image-ref: 'crud-app:latest'   # Image à analyser
    format: 'table'             # Format de sortie
    exit-code: '1'              # Échouer le build si des vulnérabilités sont trouvées
    ignore-unfixed: true        # Ignorer les vulnérabilités sans correctifs
    severity: 'CRITICAL,HIGH'   # Alerter uniquement sur les vulnérabilités critiques et élevées
```

Vos builds échoueront si des problèmes graves sont détectés, vous gardant en sécurité par défaut.

### 4\. Créer des échecs de pipeline basés sur des seuils

Vous pouvez configurer vos pipelines pour échouer automatiquement si les vulnérabilités dépassent un seuil défini, appliquant ainsi des pratiques de sécurité strictes sans effort manuel. Voici à quoi cela devrait ressembler :

```yaml
# Échouer le pipeline si des vulnérabilités critiques ou élevées sont trouvées
- name: Exécuter le scanner de vulnérabilités Trivy
  uses: aquasecurity/trivy-action@master
  with:
    image-ref: 'crud-app:latest'   # Image à analyser
    format: 'json'              # Sortie en JSON pour l'analyse
    exit-code: '1'              # Échouer le build si des vulnérabilités sont trouvées
    severity: 'CRITICAL,HIGH'   # Vérifier les problèmes de vulnérabilités critiques et élevées
    ignore-unfixed: true        # Ignorer les vulnérabilités sans correctifs
```

Cela impose une posture de sécurité sans compromis - c'est-à-dire que si des vulnérabilités critiques ou élevées sont détectées, le build s'arrête immédiatement.

### 5\. Implémenter des vérifications de sécurité personnalisées

Parfois, vous devez aller au-delà des scanners automatisés. Voici un exemple basique d'une vérification de sécurité personnalisée que vous pouvez ajouter à votre pipeline :

```yaml
#!/bin/bash

# Script personnalisé pour vérifier les secrets codés en dur dans le code source
# Vérifier les clés API codées en dur dans les fichiers source
if grep -r "API_KEY" ./src; then
  echo "Problème de sécurité : Clés API codées en dur trouvées."
  exit 1  # Échouer le build
else
  echo "Aucune clé API codée en dur trouvée."
fi
```

Vous pouvez étendre ce script pour analyser des motifs comme les clés privées, les mots de passe ou d'autres informations sensibles, aidant à détecter les problèmes avant qu'ils n'atteignent la production.

## Optimisation des performances et mise à l'échelle

Optimiser tôt vous évite des problèmes plus tard. Voici comment rendre vos pipelines plus rapides, plus intelligents et plus évolutifs :

### 1\. Mesurer les temps d'exécution du pipeline

Comprendre combien de temps chaque étape prend est la première étape pour l'améliorer :

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      # Enregistrer l'heure de début
      - name: Démarrer le chronomètre
        run: echo "Heure de début : $(date)"

      - uses: actions/checkout@v3
      - run: npm install

      # Enregistrer l'heure de fin pour calculer la durée
      - name: Fin du chronomètre
        run: echo "Heure de fin : $(date)"
```

Plus tard, vous pouvez automatiser le suivi du temps pour des rapports complets et des alertes.

### 2\. Implémenter des stratégies de parallélisation

Divisez vos tâches intelligemment pour gagner du temps :

```yaml
jobs:
  # Première tâche pour installer les dépendances
  install:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: npm ci

  # Exécuter les tests en parallèle avec le linting
  test:
    runs-on: ubuntu-latest
    needs: install  # Dépend de la tâche d'installation
    steps:
      - uses: actions/checkout@v3
      - run: npm test

  # Exécuter le linting en parallèle avec les tests
  lint:
    runs-on: ubuntu-latest
    needs: install  # Dépend également de la tâche d'installation
    steps:
      - uses: actions/checkout@v3
      - run: npm run lint
```

Résultat : Les tests et le linting s'exécutent en parallèle après l'installation des dépendances, réduisant considérablement le temps du pipeline.

### 3\. Configurer la mise en cache distribuée

La mise en cache évite à votre workflow de répéter des tâches coûteuses :

```yaml
# Mettre en cache les dépendances pour accélérer les builds
- name: Mettre en cache les modules node
  uses: actions/cache@v3
  with:
    path: |
      ~/.npm           # Mettre en cache le cache global de npm
      node_modules     # Mettre en cache les dépendances locales
    key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}  # Clé basée sur le système d'exploitation et le hash des dépendances
    restore-keys: |    # Clés de secours si la correspondance exacte n'est pas trouvée
      ${{ runner.os }}-node-
```

**Astuce :** Mettez également en cache les artefacts de build, les couches Docker et les plans Terraform lorsque cela est possible.

### 4\. Créer des benchmarks de performance

Suivez vos temps de build au fil du temps avec des benchmarks :

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      # Stocker l'heure de début comme variable d'environnement
      - name: Démarrer le chronomètre
        id: start_time
        run: echo "start_time=$(date +%s)" >> $GITHUB_ENV

      - uses: actions/checkout@v3
      - run: npm install

      # Calculer et afficher le temps écoulé
      - name: Fin du chronomètre et calcul du temps écoulé
        run: |
          end_time=$(date +%s)
          elapsed_time=$((end_time - ${{ env.start_time }}))
          echo "Temps de build : $elapsed_time secondes"
```

Avec des benchmarks en place, vous pouvez surveiller les régressions et déclencher des optimisations automatiquement.

### 5\. Comment planifier la croissance au-delà des niveaux gratuits

* **Comprendre les structures de tarification des clouds :** AWS, Azure, GCP offrent tous des niveaux gratuits généreux, mais connaissez les limites pour éviter les factures surprises. *(J'ai été là et ce n'était pas joli.)*
    
* **Envisager de passer à des outils CI/CD plus avancés :** Jenkins, CircleCI, GitLab peuvent offrir de meilleures performances ou un contrôle auto-hébergé à mesure que vous grandissez.
    
* **Automatiser le provisionnement des ressources :** Utilisez l'Infrastructure as Code (IaC) avec Terraform, Pulumi ou AWS CDK pour mettre à l'échelle dynamiquement votre infrastructure lorsque votre équipe ou votre trafic grandit.
    

## Exemple complet de pipeline CI/CD

Voici un exemple complet qui rassemble tout :

```yaml
# Pipeline CI/CD complet de bout en bout
name: CI/CD Pipeline

on:
  push:
    branches:
      - main

jobs:
  # Tâche de configuration initiale
  setup:
    runs-on: ubuntu-latest
    steps:
      - name: Vérifier le code
        uses: actions/checkout@v3

  # Tâche de build et de test
  build:
    runs-on: ubuntu-latest
    needs: setup  # Dépend de la tâche de configuration
    steps:
      - name: Configurer Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '16'
      - name: Installer les dépendances
        run: npm install
      - name: Exécuter l'analyse de sécurité
        run: npx eslint .  # Exécuter ESLint pour les règles de sécurité

  # Tâche de déploiement sur Kubernetes
  deploy:
    runs-on: ubuntu-latest
    needs: build  # Dépend du build réussi
    steps:
      - name: Configurer le cluster K3d
        run: k3d cluster create dev-cluster --servers 1 --agents 2 --port 8080:80@loadbalancer
      - name: Appliquer les manifestes Kubernetes
        run: kubectl apply -f k8s/  # Appliquer tous les manifestes K8s dans le répertoire k8s
      - name: Déployer l'application
        run: kubectl rollout restart deployment/webapp  # Redémarrer le déploiement pour une mise à jour sans temps d'arrêt

  # Tâche de provisionnement de l'infrastructure
  terraform:
    runs-on: ubuntu-latest
    needs: deploy  # Exécuter après le déploiement
    steps:
      - name: Configurer Terraform
        uses: hashicorp/setup-terraform@v2
      - name: Initialisation Terraform
        run: terraform init  # Initialiser Terraform
      - name: Appliquer Terraform
        run: terraform apply -auto-approve  # Appliquer automatiquement les changements d'infrastructure
```

#### **Runbook : Déploiement échoué :**

**Problème :** Les pods échouent en raison des limites de ressources (par exemple, OOMKilled, CrashLoopBackOff).  
**Solution :**

```yaml
  kubectl top pod
  kubectl edit deployment crud-app
  kubectl apply -f deployment.yaml
  kubectl rollout status deployment/crud-app
```

**Astuce :** Définissez des demandes et limites de ressources réalistes tôt, cela vous fera gagner du temps de débogage plus tard.

## Conclusion

En suivant ce tutoriel, vous savez maintenant comment construire un pipeline DevOps prêt pour la production en utilisant des outils gratuits :

* **CI/CD** : GitHub Actions pour les tests, le linting et la construction.
    
* **Infrastructure** : Terraform pour la configuration AWS/Render et PostgreSQL.
    
* **Orchestration** : K3d pour Kubernetes local.
    
* **Monitoring** : Grafana, Prometheus, UptimeRobot.
    
* **Sécurité** : CodeQL, OWASP ZAP, Trivy pour l'analyse des vulnérabilités.
    

Ce pipeline est évolutif et sécurisé, et il est parfait pour les petits projets. À mesure que votre application grandit, vous pourriez vouloir envisager des plans payants pour plus de ressources (par exemple, des instances AWS plus grandes, des métriques Grafana illimitées). Vous pouvez consulter [AWS Free Tier](https://aws.amazon.com/free/), [Terraform Docs](https://developer.hashicorp.com/terraform/docs), et [Grafana Docs](https://grafana.com/docs/) pour plus d'apprentissage.

**PS** : J'adorerais voir ce que vous construisez. Partagez votre pipeline sur le [forum de FreeCodeCamp](https://forum.freecodecamp.org/) ou mentionnez-moi sur X [@Emidowojo](https://x.com/Emidowojo) avec #DevOpsOnABudget, et dites-moi quels défis vous avez rencontrés. Vous pouvez également me contacter sur [LinkedIn](https://www.linkedin.com/in/emidowojo/) si vous souhaitez rester en contact. Si vous avez lu jusqu'à la fin de cet article, merci pour votre lecture !