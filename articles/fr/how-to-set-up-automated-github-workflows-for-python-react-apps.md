---
title: Comment configurer des workflows GitHub automatisés pour vos applications Python
  et React
subtitle: ''
author: Preston Osoro
co_authors: []
series: null
date: '2024-11-07T15:22:11.678Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-automated-github-workflows-for-python-react-apps
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1730812659785/2975b117-81ee-4c73-ae24-6fb14e369714.png
tags:
- name: CI/CD
  slug: cicd
- name: GitHub Actions
  slug: github-actions
seo_title: Comment configurer des workflows GitHub automatisés pour vos applications
  Python et React
seo_desc: 'Automating workflows is an essential step in helping you maintain code
  quality in your applications – especially when working on both frontend and backend
  code in a single repository.

  In this guide, we’ll walk through setting up automated GitHub work...'
---

Automatiser les workflows est une étape essentielle pour vous aider à maintenir la qualité du code dans vos applications, surtout lorsque vous travaillez sur le code frontend et backend dans un seul dépôt.

Dans ce guide, nous allons passer en revue la configuration de workflows GitHub automatisés pour un backend Python (utilisant Flask ou Django) et un frontend React. Ces workflows aident à tester et valider les changements de code automatiquement, garantissant que tout problème est détecté tôt.

Nous supposerons :

* Vous avez déjà écrit des tests unitaires pour vos composants React et vos routes backend.

* Votre projet est configuré en tant que monodépôt, avec des répertoires séparés pour le frontend et le backend.

* Vous êtes familier avec GitHub Actions, la plateforme que nous utiliserons pour l'automatisation, et que vous utilisez l'environnement `ubuntu-latest` fourni par GitHub.

## Étape 1 : Créer des workflows GitHub Actions

Dans cette étape, nous allons définir deux workflows GitHub Actions, l'un pour le frontend et un autre pour le backend. Ces workflows exécuteront des tests automatiquement chaque fois que des changements sont poussés vers la branche `main`.

### Qu'est-ce qu'un workflow GitHub Action ?

Un workflow GitHub Action est un ensemble d'instructions qui indiquent à GitHub comment exécuter automatiquement des tâches en fonction de certains événements.

Ici, nos workflows exécuteront des tests et déploieront l'application uniquement si les tests réussissent. Les workflows sont déclenchés par des événements, tels qu'un push vers une branche, et se composent de jobs qui définissent les tâches que nous voulons automatiser.

### Pipeline CI/CD Frontend

Commençons par créer un nouveau fichier dans votre dépôt à l'emplacement `.github/workflows/frontend.yml`. Ce fichier configurera un pipeline automatisé pour gérer les tests et le déploiement du frontend. Ensuite, définissez le workflow avec le contenu suivant :

```yaml
name: Frontend CI/CD Pipeline

on:
  push:
    branches:
      - main  

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Cache Node.js modules
        uses: actions/cache@v3
        with:
          path: ./frontend/node_modules
          key: ${{ runner.os }}-node-${{ hashFiles('./frontend/package-lock.json') }}
          restore-keys: |
            ${{ runner.os }}-node-

      - name: Set up Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '20'

      - name: Install frontend dependencies
        run: yarn install
        working-directory: ./frontend 

      - name: Run frontend tests
        run: yarn test
        working-directory: ./frontend  
```

Voici une explication de ce que chaque partie fait :

1. `on: push`: Cela déclenche le workflow chaque fois qu'il y a un push vers la branche `main`.

2. **Checkout code**: Cette étape utilise l'action GitHub pour extraire le code du dépôt.

3. **Cache Node.js modules**: Met en cache `node_modules` pour accélérer l'exécution du workflow lors des exécutions suivantes.

4. **Set up Node.js**: Configure l'environnement Node.js pour l'installation des dépendances et les tests.

5. **Install dependencies and run tests**: Installe les packages avec Yarn puis exécute les tests pré-écrits pour vérifier que le frontend fonctionne comme prévu.

### **Pipeline CI/CD Backend**

Maintenant, créons un fichier séparé pour le workflow backend à l'emplacement `.github/workflows/backend.yml`. Ce fichier automatisera les tests et le déploiement pour le backend Python.

```yaml
name: Backend CI/CD Pipeline

on:
  push:
    branches:
      - main  

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Cache Python packages
        uses: actions/cache@v3
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-pip-${{ hashFiles('./backend/requirements.txt') }}
          restore-keys: |
            ${{ runner.os }}-pip-

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.8'  

      - name: Create Virtual Environment
        run: python3 -m venv venv
        working-directory: ./backend

      - name: Install backend dependencies
        run: |
          source venv/bin/activate
          pip install -r requirements.txt  
        working-directory: ./backend

      - name: Configure DATABASE_URL securely
        env:
          DATABASE_URL: ${{ secrets.DATABASE_URL }}
        run: |
          if [ -z "$DATABASE_URL" ]; then
            echo "DATABASE_URL is missing" >&2
            exit 1
          fi

      - name: Run tests with pytest
        run: |
          source venv/bin/activate
          pytest tests/ --doctest-modules -q --disable-warnings
        working-directory: ./backend  

      - name: Deploy to Production
        if: ${{ success() }}
        run: |
          echo "Deploying to production..."

      - name: Notify on Failure
        if: ${{ failure() }}
        run: |
          echo "Build failed! Sending notification..."
```

Voici ce que fait ce workflow :

1. **Extrait le code** et **met en cache les packages Python** pour une exécution plus rapide lors des exécutions répétées.

2. **Configure Python** et crée un environnement virtuel pour isoler les dépendances.

3. **Installe les dépendances** dans l'environnement virtuel à partir de `requirements.txt`.

4. **Configure les variables d'environnement** de manière sécurisée avec GitHub Secrets. Dans cet exemple, nous utilisons une URL de base de données qui est stockée dans un secret GitHub pour un accès sécurisé.

5. **Exécute les tests backend** avec `pytest`, qui vérifie que les routes et fonctions backend fonctionnent correctement.

## **Étape 2 : Configurer les secrets**

Pour des raisons de sécurité, configurons les secrets GitHub pour stocker des informations sensibles, comme les chaînes de connexion à la base de données.

1. Allez dans votre dépôt GitHub et sélectionnez **Paramètres**.

2. Dans la barre latérale, sélectionnez **"Secrets et variables"**, puis cliquez sur **"Actions"**. 

3. Ajoutez un nouveau secret de dépôt :

   * **Nom** : `DATABASE_URL`

   * **Valeur** : Votre chaîne de connexion de base de données réelle.

L'utilisation des secrets GitHub garde les données sensibles en sécurité et les empêche d'apparaître dans votre base de code.

## Étape 3 : Valider et pousser les changements

Une fois vos fichiers de workflow prêts, validez et poussez les changements vers la branche `main`. Chaque fois que vous pousserez des changements vers `main`, GitHub Actions déclenchera automatiquement ces workflows, garantissant que votre code est rigoureusement testé.

## Étape 4 : Surveiller les exécutions des workflows

Après avoir poussé vos changements, naviguez vers l'onglet **Actions** dans votre dépôt GitHub pour surveiller les exécutions des workflows. Voici ce que vous y trouverez :

* **Exécutions des workflows** : Cette page liste chaque fois qu'un workflow est déclenché. Vous pouvez voir si le workflow a réussi, échoué ou est en cours.

* **Logs** : Cliquez sur une exécution spécifique d'un workflow pour voir les logs détaillés. Les logs sont divisés par étapes, vous pouvez donc voir exactement où un problème est survenu si quelque chose ne va pas.

### Identifier les problèmes dans les logs

Les logs de chaque étape fournissent des informations sur les problèmes :

* Si les dépendances échouent à s'installer, vous verrez des messages d'erreur spécifiant quel package a causé le problème.

* Si les tests échouent, les logs listeront les tests spécifiques et les raisons de l'échec, vous aidant à déboguer rapidement.

* Pour les workflows qui utilisent des secrets, les erreurs liées aux secrets manquants apparaîtront dans les étapes de configuration de l'environnement, vous permettant de corriger les problèmes de configuration.

En comprenant comment interpréter ces logs, vous pouvez résoudre les problèmes de manière proactive et garantir des déploiements fluides et fiables.

## Conclusion

En suivant ces étapes, vous avez configuré des workflows GitHub automatisés pour le frontend et le backend de votre application.

Cette configuration garantit que vos tests s'exécutent automatiquement à chaque push vers la branche `main`, aidant à maintenir une qualité de code élevée et une fiabilité.

Avec des workflows automatisés, vous pouvez vous concentrer davantage sur la construction de fonctionnalités et moins sur les tests manuels du code, sachant que vos workflows vous alerteront de tout problème dès le début.