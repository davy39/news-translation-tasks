---
title: Comment automatiser les mises à jour de la documentation API avec GitHub Actions
  et les spécifications OpenAPI
subtitle: ''
author: EZINNE ANNE EMILIA
co_authors: []
series: null
date: '2025-09-09T14:28:26.753Z'
originalURL: https://freecodecamp.org/news/how-to-automate-api-documentation-updates-with-github-actions-and-openapi-specifications
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1757428080226/175085d0-cfea-41a0-aa52-a50ad8212980.png
tags:
- name: GitHub
  slug: github
- name: github-actions
  slug: github-actions-1
- name: OpenApi
  slug: openapi
- name: documentation
  slug: documentation
seo_title: Comment automatiser les mises à jour de la documentation API avec GitHub
  Actions et les spécifications OpenAPI
seo_desc: Maintaining up-to-date API documentation is often one of the biggest pain
  points for developers and teams. Too often, the API spec changes but the docs lag
  behind, leaving developers with outdated or inconsistent information. This frustrates
  consumer...
---

Maintenir une documentation API à jour est souvent l'un des plus grands défis pour les développeurs et les équipes. Trop souvent, la spécification de l'API change mais la documentation prend du retard, laissant les développeurs avec des informations obsolètes ou incohérentes. Cela frustre les utilisateurs de votre API et augmente la charge de support.

C'est là que l'automatisation intervient. En combinant les spécifications OpenAPI avec GitHub Actions, vous pouvez vous assurer que votre documentation est toujours en synchronisation avec les modifications de votre API.

* **OpenAPI** agit comme le point de référence unique pour la conception de votre API, gardant votre documentation cohérente, précise et alignée avec votre API.
    
* **GitHub Actions** automatise le workflow, validant votre spécification, construisant la documentation et la publiant sur GitHub Pages en quelques secondes.
    

Ce tutoriel vous guide à travers un exemple concret sur la façon d'utiliser GitHub Actions pour mettre à jour automatiquement votre documentation.

## Table des matières

* [Prérequis](#heading-prerequis)
    
* [Comment configurer votre dépôt](#heading-comment-configurer-votre-depot)
    
* [Comment créer la spécification OpenAPI](#heading-comment-creer-la-specification-openapi)
    
* [Comment tester la spécification API localement](#heading-comment-tester-la-specification-api-localement)
    
    * [Installer les outils](#heading-installer-les-outils)
        
    * [Créer une page d'accueil](#heading-creer-une-page-d-accueil)
        
    * [Valider votre spécification](#heading-valider-votre-specification)
        
    * [Prévisualiser dans le navigateur](#heading-previsualiser-dans-le-navigateur)
        
* [Comment pousser les modifications locales vers GitHub](#heading-comment-pousser-les-modifications-locales-vers-github)
    
* [Comment configurer votre workflow GitHub Actions](#heading-comment-configurer-votre-workflow-github-actions)
    
* [Comment configurer GitHub Pages](#heading-comment-configurer-github-pages)
    
    * [Qu'est-ce que GitHub Pages ?](#heading-qu-est-ce-que-github-pages)
        
    * [Configuration de GitHub Pages](#heading-configuration-de-github-pages)
        
* [Comment gérer plusieurs versions](#heading-comment-gerer-plusieurs-versions)
    
    * [À propos des versions](#heading-a-propos-des-versions)
        
        * [Version 1 (v1)](#heading-version-1-v1)
            
        * [Version 2 (v2)](#heading-version-2-v2)
            
        * [Version 3 (v3)](#heading-version-3-v3)
            
    * [Comment configurer les versions localement](#heading-comment-configurer-les-versions-localement)
        
    * [Comment valider les spécifications API](#heading-comment-valider-les-specifications-api)
        
    * [Comment mettre à jour le workflow GitHub Actions](#heading-comment-mettre-a-jour-le-workflow-github-actions)
        
* [Résumé](#heading-resume)
    

## Prérequis

* [Node.js et npm installés.](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)
    
* [Un compte GitHub avec des connaissances de base en Git.](https://www.freecodecamp.org/news/gitting-things-done-book/)
    
* [L'éditeur Visual Studio Code](https://code.visualstudio.com/download).
    
* [Des connaissances de base sur la documentation et OpenAPI](https://idratherbewriting.com/learnapidoc/).
    

## Comment configurer votre dépôt

Si vous n'en avez pas déjà un, créez un dépôt GitHub. Pour ce tutoriel, j'utiliserai `api-docs` comme nom de dépôt.

Ensuite, ouvrez VSCode et créez un dossier portant le même nom.

## Comment créer la spécification OpenAPI

À l'intérieur du dossier que vous venez de créer, créez un dossier nommé `spec` et ajoutez un fichier nommé `greetings.yaml` avec le contenu suivant :

```yaml
openapi: 3.0.3
info:
  title: Greetings API
  version: 1.0.0
  description: Il s'agit d'une API de salutations démontrant un point de terminaison simple avec des paramètres de requête et un support multilingue.
  license:
    name: MIT
    url: https://opensource.org/licenses/MIT
servers:
  - url: https://api.yourdomain.com/v1
    description: Serveur de production (v1)
  - url: https://staging.yourdomain.com/v1
    description: Serveur de staging (v1)
security:
  - api_key: []
paths:
  /hello:
    get:
      summary: Retourne une salutation
      operationId: getGreeting
      parameters:
        - name: name
          in: query
          required: false
          description: Nom de la personne à saluer
          schema:
            type: string
            example: Ezinne
        - name: lang
          in: query
          required: false
          description: Langue de la salutation (par défaut l'anglais)
          schema:
            type: string
            enum: [en, fr, es, ig]
            example: en
      responses:
        '200':
          description: Réponse réussie
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
              examples:
                english:
                  value: { message: "Hello, Ezinne!" }
                french:
                  value: { message: "Bonjour, Ezinne!" }
                spanish:
                  value: { message: "¡Hola, Ezinne!" }
                igbo:
                  value: { message: "Ndeewo, Ezinne!" }
components:
  securitySchemes:
    api_key:
      type: apiKey
      name: Authorization
      in: header
```

Il s'agit d'une spécification simple avec des salutations multilingues. À mesure que votre API se développe (par exemple avec plus de langues ou de versions), maintenir la documentation synchronisée manuellement peut devenir fastidieux. C'est pourquoi l'automatisation est utile.

## Comment tester la spécification API localement

### Installer les outils :

Avant de configurer GitHub Actions, vous pouvez tester la spécification API localement sur votre machine en installant [Redocly](https://github.com/Redocly) (anciennement Redoc) et en la testant dans un environnement HTML.

Redocly est un outil léger et personnalisable pour rendre les spécifications OpenAPI sous forme de documentation HTML interactive. Il est idéal pour le déploiement de sites statiques, ce qui le rend parfait pour ce scénario.

* Installez Redoc globalement avec `npm install -g @redocly/cli`
    
* Installez http-server globalement avec `npm install -g http-server`
    

Le http-server est un serveur local que vous pouvez utiliser pour tester la documentation sur votre machine avant de la pousser sur GitHub et de la déployer sur GitHub Pages.

### Créer une page d'accueil :

Dans votre projet, créez un dossier `docs` et ajoutez un fichier `index.html` :

```xml
<!DOCTYPE html>
<html>
  <head>
    <title>Documentation API</title>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1">
  </head>
  <body>
    <redoc spec-url="../spec/greetings.yaml"></redoc>
    <script src="https://cdn.redoc.ly/redoc/latest/bundles/redoc.standalone.js"></script>
  </body>
</html>
```

### Valider votre spécification :

`redocly lint spec/greetings.yaml`

Vous devriez voir ceci s'il n'y a pas d'erreurs ou d'avertissements :

```powershell
Woohoo! Your API description is valid. 🎉
```

**Note :** Valider votre spécification API avant le test est important car cela signalera toute erreur possible. En effet, Redocly ne parviendra pas à lancer la prévisualisation s'il y a des erreurs dans votre spécification.

### Prévisualiser dans le navigateur :

Exécutez `http-server`, et vous devriez voir ceci dans le terminal :

```powershell
Starting up http-server, serving ./
Available on:
  http://127.0.0.1:8080
  http://192.168.x.x:8080
Hit CTRL-C to stop the server
```

Ouvrez [`http://127.0.0.1:8080/`](http://localhost:8080/docs/index.html) et naviguez vers `/docs` pour voir votre documentation.

![Aperçu de la spécification API dans une page HTML](https://cdn.hashnode.com/res/hashnode/image/upload/v1756983802999/944b8603-7b2e-477a-8156-fdaa60f7e0af.png align="center")

## Comment pousser les modifications locales vers GitHub

Après avoir effectué des modifications locales, vous devez configurer la documentation de l'API afin qu'elle puisse se mettre à jour automatiquement chaque fois que vous apportez des modifications.

Exécutez ces commandes si vous poussez vers le dépôt pour la première fois :

```powershell
git init
git add .
git commit -m "premier commit"
git branch -M main
git remote add origin <votre-url-de-depot>
git push -u origin main
```

## Comment configurer votre workflow GitHub Actions

Vous pouvez configurer votre workflow GitHub en créant quelques dossiers.

Tout d'abord, créez `.github/workflows/` dans le dossier `api-docs`. Ensuite, à l'intérieur du dossier `workflows`, créez un fichier `docs.yml`. Il s'agit du fichier de workflow qui servira de déclencheur pour exécuter la validation, générer le HTML avec Redocly et déployer sur GitHub Pages en même temps.

```yaml
name: Build API Documentation and Deploy to GitHub Pages

on:
  push:
    branches:
      - main
    paths:
      - 'spec/greetings.yaml'

jobs:
  build-spec:
    runs-on: ubuntu-latest
    permissions:
      contents: write # nécessaire pour le déploiement gh-pages

    steps:
      # 1. Récupérer le dépôt
      - name: Checkout code
        uses: actions/checkout@v4

      # 2. Configurer Node.js
      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      # 3. Installer la CLI Redocly
      - name: Install Redocly CLI
        run: npm install -g @redocly/cli

      # 4. Valider la spécification OpenAPI
      - name: Validate OpenAPI Spec
        run: redocly lint spec/greetings.yaml

      # 5. Créer le répertoire de build
      - name: Create build directory
        run: mkdir -p public

      # 6. Copier la spécification
      - name: Copy spec
        run: mkdir -p public/spec && cp spec/greetings.yaml public/spec/

      # 7. Copier la page d'accueil
      - name: Copy landing page
        run: cp docs/index.html public/index.html

      # 8. Déployer sur GitHub Pages
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./public
```

Voici ce qui se passe dans ce code :

* S'exécute lorsque des modifications sont poussées vers `main` et affectent `spec/greetings.yaml`.
    
* Récupère le code du dépôt.
    
* Configure Node.js et installe Redocly.
    
* Valide votre spécification OpenAPI (ainsi les spécifications erronées ne seront pas déployées).
    
* Copie la spécification et la page d'accueil dans un dossier `public/`.
    
* Déploie `public/` sur la branche `gh-pages` avec GitHub Pages.
    

Puisque nous en avons terminé avec les tests locaux, mettez à jour le chemin du fichier dans le `index.html` :

```xml
<!DOCTYPE html>
<html>
  <head>
    <title>Documentation API</title>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1">
  </head>
  <body>
    <redoc spec-url="./spec/greetings.yaml"></redoc> <!--mettez à jour le chemin pour correspondre à votre config gh-->
    <script src="https://cdn.redoc.ly/redoc/latest/bundles/redoc.standalone.js"></script>
  </body>
</html>
```

Ceci afin que le répertoire `public` dans le workflow puisse y accéder correctement.

Ce workflow ne s'exécutera que lorsqu'il détectera des modifications dans la spécification API (`greetings.yaml`). Pour voir le workflow en action, effectuez une modification mineure dans `greetings.yaml`.

Poussez les modifications vers votre dépôt GitHub :

```powershell
git add .
git commit -m 'ajout de modifications'
git push
```

## Comment configurer GitHub Pages

### Qu'est-ce que GitHub Pages ?

[GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages) est une plateforme d'hébergement appartenant à GitHub où vous pouvez héberger des sites web directement depuis votre compte GitHub. Cela signifie que vous pouvez publier des sites statiques sur Internet en utilisant un domaine GitHub et toute personne disposant du lien du site peut y accéder.

Il existe d'autres plateformes d'hébergement que vous pouvez utiliser pour déployer des sites web statiques comme [Netlify](https://www.netlify.com/) et [Vercel](https://vercel.com/). Mais l'utilisation de GitHub Pages pour cette documentation est plus facile à configurer car elle se trouve sur la même plateforme.

### Configuration de GitHub Pages

Configurez GitHub Pages en cliquant sur l'onglet Settings de votre dépôt.

![Aperçu de l'onglet Settings dans le dépôt `api-docs`](https://cdn.hashnode.com/res/hashnode/image/upload/v1756985360548/fa3518a7-0b44-4c7b-ae7f-d0e0b17a84c6.png align="center")

Sous Source, choisissez :

* Deploy from branch : `gh-pages`
    
* Folder : `/ (root)`
    

![Aperçu étape par étape de la configuration gh-pages et root](https://cdn.hashnode.com/res/hashnode/image/upload/v1756985446692/a4774bcc-1a42-49f8-a9fd-8ca9339808ef.png align="center")

Ensuite, enregistrez et attendez que le workflow se termine.

Votre documentation sera en ligne à l'adresse : `https://<nom-utilisateur>.github.io/api-docs`.

## Comment gérer plusieurs versions

Et si vous aviez plusieurs versions d'API à mettre à jour ? Supposons que l'API de salutations simple de ce tutoriel ait vu de nouvelles fonctionnalités ajoutées à travers différentes versions. Dans ce cas, vous pouvez gérer les API pour les différentes versions sur une seule page et également les construire et les déployer automatiquement.

### À propos des versions

#### Version 1 (v1)

C'est le point de départ qui est `greetings.yaml`. L'API n'a qu'un seul point de terminaison `/hello` qui retourne une salutation en quatre langues (anglais, français, espagnol ou igbo).

#### Version 2 (v2)

Dans la version 2, l'API ajoute des fonctionnalités de création et de lecture. Vous pouvez :

* Utiliser `POST /hello` pour créer et enregistrer une salutation.
    
* Récupérer les salutations par leur ID unique avec `GET /hello/{id}`.
    

#### Version 3 (v3)

La version 3 s'appuie sur la v2 en ajoutant une fonctionnalité de mise à jour. En plus de créer et de récupérer des salutations, vous pouvez maintenant mettre à jour une salutation existante en utilisant `PUT /hello/{id}`.

### Comment configurer les versions localement

Tout d'abord, créez un dossier `v1` et déplacez-y le fichier `greetings.yaml`. Puisque nous allons utiliser des versions, vous pouvez supprimer le dossier `spec` existant.

Ensuite, créez un dossier `v2` et créez un fichier `greetings-v2.yaml`. [Obtenez l'API de salutations pour la version 2 ici](https://ezinneanne.github.io/api-doc/v2/greetings-v2.yaml).

Ensuite, créez un dossier `v3` et ajoutez le fichier `greetings-v3.yaml`. [Obtenez l'API de salutations pour la version 3 ici](https://ezinneanne.github.io/api-doc/v3/greetings-v3.yaml).

Pour suivre le même modèle que les autres, renommez le fichier de la version 1 en `greetings-v1.yaml`. Ensuite, mettez à jour votre `index.html` pour accommoder les deux autres versions.

```xml
<!DOCTYPE html>
<html>
  <head>
    <title>Documentation API</title>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
      body {
        font-family: Arial, sans-serif;
        margin: 0;
      }
      header {
        background: #2c3e50;
        color: white;
        padding: 1rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
      }
      select {
        padding: 0.4rem;
        font-size: 1rem;
      }
    </style>
  </head>
  <body>
    <header>
      <h2>Documentation API</h2>
      <div>
        <label for="version">Version : </label>
        <select id="version" onchange="loadSpec()">
          <option value="./v1/greetings-v1.yaml">v1</option>
          <option value="./v2/greetings-v2.yaml">v2</option>
          <option value="./v3/greetings-v3.yaml">v3</option>
        </select>
      </div>
    </header>

    <!-- Conteneur ReDoc -->
    <div id="redoc-container"></div>

    <!-- Script ReDoc -->
    <script src="https://cdn.redoc.ly/redoc/latest/bundles/redoc.standalone.js"></script>
    <script>
      function loadSpec() {
        const version = document.getElementById("version").value;
        Redoc.init(version, {}, document.getElementById("redoc-container"));
      }
      // Charger par défaut (v1) au premier chargement
      window.onload = loadSpec;
    </script>
  </body>
</html>
```

### Comment valider les spécifications API

Plus tôt dans cet article, j'ai mentionné le test de votre spécification localement. Maintenant que vous avez deux versions supplémentaires de l'API de salutations, exécutez le test pour mettre en évidence et corriger les erreurs existantes.

* Pour la version V2 : `redocly lint v2/greetings-v2.yaml`
    
* Pour la version V3 : `redocly lint v3/greetings-v3.yaml`
    

### Comment mettre à jour le workflow GitHub Actions

Maintenant que vous avez trois versions de spécification API, vous devez mettre à jour votre workflow afin qu'il surveille les trois fichiers de spécification et le document HTML pour les changements, puis les pousse et les déploie également sur GitHub Pages.

Ajoutez ceci à votre `.github/workflows/docs.yml` :

```yaml
# Nom du workflow
name: Build and Deploy API Documentation

on:
  push:
    branches: [ main ]
    paths:
      - 'docs/index.html'
      - 'v1/greetings-v1.yaml'
      - 'v2/greetings-v2.yaml'
      - 'v3/greetings-v3.yaml'

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest

    permissions:
      contents: write

    steps:
      # 1. Récupérer le dépôt
      - name: Checkout repository
        uses: actions/checkout@v4

      # 2. Créer le répertoire de build
      - name: Create build directory
        run: mkdir -p public

      # 3. Copier les spécifications YAML dans le dossier public
      - name: Copy v1 spec
        run: mkdir -p public/v1 && cp v1/greetings-v1.yaml public/v1/

      - name: Copy v2 spec
        run: mkdir -p public/v2 && cp v2/greetings-v2.yaml public/v2/

      - name: Copy v3 spec
        run: mkdir -p public/v3 && cp v3/greetings-v3.yaml public/v3/

      # 4. Copier la page d'accueil dans public
      - name: Copy landing page
        run: cp docs/index.html public/index.html

      # 5. Déployer sur GitHub Pages
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./public
```

Et enfin, poussez les changements et rechargez le site. Cela devrait présenter la documentation mise à jour.

![Aperçu de la documentation API dans un environnement GitHub Pages hébergé](https://cdn.hashnode.com/res/hashnode/image/upload/v1756986868235/9de187f1-12c4-46ca-a73b-daafa353ed1f.png align="center")

## Résumé

Dans ce tutoriel, vous avez appris à mettre à jour automatiquement vos documents d'API. Nous avons commencé par une seule spécification OpenAPI et une page HTML de base rendue par Redocly, et nous l'avons testée localement. Nous avons ensuite configuré GitHub Actions pour valider automatiquement la spécification, copier les fichiers et déployer la documentation sur GitHub Pages. Enfin, nous avons étendu la configuration pour gérer plusieurs versions d'API en un seul endroit.

Avec ce workflow, votre documentation reste précise, à jour et sans tracas, de sorte que chaque modification que vous apportez à votre spécification d'API est mise en ligne dès que vous poussez les changements.