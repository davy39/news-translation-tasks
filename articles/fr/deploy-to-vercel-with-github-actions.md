---
title: Comment déployer une application Next.js sur Vercel avec GitHub Actions
subtitle: ''
author: Chidiadi Anyanwu
co_authors: []
series: null
date: '2025-06-10T17:56:01.744Z'
originalURL: https://freecodecamp.org/news/deploy-to-vercel-with-github-actions
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1749577622920/8e35a6c1-3f4f-49a3-a4fe-dba80e24eec3.png
tags:
- name: deployment
  slug: deployment
- name: Next.js
  slug: nextjs
- name: GitHub
  slug: github
- name: GitHub Actions
  slug: github-actions
seo_title: Comment déployer une application Next.js sur Vercel avec GitHub Actions
seo_desc: Vercel is a cloud platform or Platform-as-a-Service (PaaS) designed to help
  frontend developers create, preview, and deploy web applications swiftly and efficiently.
  In this tutorial, we’ll focus on deploying a Next.js application to Vercel using
  Git...
---

Vercel est une plateforme cloud ou Platform-as-a-Service (PaaS) conçue pour aider les développeurs frontend à créer, prévisualiser et déployer des applications web rapidement et efficacement. Dans ce tutoriel, nous allons nous concentrer sur le déploiement d'une application Next.js sur Vercel en utilisant GitHub Actions.

Dans un [article précédent](https://www.freecodecamp.org/news/how-to-build-a-simple-portfolio-blog-with-nextjs/), nous avons construit un blog portfolio avec Next.js. Ici, vous apprendrez comment le déployer sur Vercel avec [GitHub Actions](https://www.freecodecamp.org/news/automate-cicd-with-github-actions-streamline-workflow/).

## Prérequis

Pour pouvoir déployer votre projet, vous devez avoir un dépôt GitHub du projet (vous pouvez toujours suivre si vous avez déjà un projet Next.js), et un compte Vercel. [Voici le dépôt GitHub avec lequel nous allons travailler](https://github.com/chidiadi01/simple-writer-portfolio). Vous pouvez le cloner pour suivre.

## Comment déployer votre application Next

### Créer un jeton Vercel et l'ajouter à vos secrets dans GitHub

Dans votre compte Vercel, allez dans Paramètres, puis allez dans Tokens.

![Tokens des paramètres du compte Vercel.](https://cdn.hashnode.com/res/hashnode/image/upload/v1749036906930/1c483351-0e78-4392-a948-53921ba2916c.png align="center")

Dans la section Créer un jeton, entrez un nom pour votre jeton, sélectionnez une date d'expiration et cliquez sur "créer".

![Création d'un jeton vercel](https://cdn.hashnode.com/res/hashnode/image/upload/v1749037009419/2a48b48d-31c4-4b72-a281-dd8eb689770d.png align="center")

Vous devriez voir un message de succès avec votre jeton. Ensuite, allez dans votre dépôt GitHub, et cliquez sur l'onglet "Paramètres".

![Vercel, message de succès du jeton créé.](https://cdn.hashnode.com/res/hashnode/image/upload/v1749037335441/1a46fb8b-8f3c-4d44-8ad5-c7de3340ef2b.png align="center")

Dans l'onglet Paramètres, allez dans Secrets et variables dans la barre latérale, puis cliquez sur Actions.

![Secrets des actions dans les paramètres du dépôt GitHub.](https://cdn.hashnode.com/res/hashnode/image/upload/v1749037726010/5ca33111-0dbe-4e3e-bde5-91a8e518f05b.png align="center")

Vous verrez une section pour ajouter des secrets. Ajoutez un secret nommé `VERCEL_TOKEN`, et collez le jeton là.

![jeton vercel, id de projet, id d'organisation.](https://cdn.hashnode.com/res/hashnode/image/upload/v1749037787198/53b42a96-ad79-4895-aba0-abe6d79eceb5.png align="center")

Le jeton Vercel est un jeton utilisé pour authentifier le runner GitHub. Le CLI Vercel installé sur le runner GitHub va exécuter les commandes avec votre compte. Ainsi, au lieu de devoir se connecter, il utilise le jeton d'accès pour vérifier qu'il a été réellement autorisé par vous à prendre les actions.

L'ID de l'organisation est utilisé pour indiquer à Vercel quel compte d'organisation ou d'équipe le projet doit être créé sous.

L'ID de projet indique ensuite à Vercel le projet spécifique que vous souhaitez déployer. Tout comme l'ID de l'organisation, il s'agit d'un identifiant unique.

### Installer le CLI Vercel et se connecter

Utilisez la commande suivante pour installer le CLI vercel globalement sur votre ordinateur :

```bash
npm install -g vercel
```

Ensuite, [connectez-vous au CLI](https://vercel.com/docs/cli/login) avec la commande suivante :

```bash
vercel login
```

Utilisez l'une des options pour vous connecter.

![méthodes de connexion](https://cdn.hashnode.com/res/hashnode/image/upload/v1749312895981/93c13b75-83da-4da7-b5c5-17572d126ce4.png align="center")

J'ai utilisé GitHub. Sélectionnez-en une avec les touches fléchées, et cliquez sur entrer.

![connexion réussie](https://cdn.hashnode.com/res/hashnode/image/upload/v1749312974078/2f470d5a-9e73-44be-b520-5179da61f86b.png align="center")

![connexion vercel](https://cdn.hashnode.com/res/hashnode/image/upload/v1749038078744/bbb5a43d-66a4-4531-a27c-12442c977568.png align="center")

### Créer un projet Vercel à partir de votre répertoire local

Naviguez jusqu'à votre répertoire de projet si vous n'y êtes pas déjà. Si vous avez déjà créé un projet sur Vercel via l'interface web, utilisez la commande [vercel link](https://vercel.com/docs/cli/link) pour lier votre répertoire actuel au projet Vercel. Si vous n'avez pas encore de projet Vercel, tapez simplement `vercel` dans le CLI et suivez les invites pour configurer le projet.

![Créer un nouveau projet Vercel](https://cdn.hashnode.com/res/hashnode/image/upload/v1749314606959/f6d7a71c-edc5-48f2-81ca-4fd3a92c44da.png align="center")

Avec cela, Vercel créera un dossier `.vercel` dans le projet. Ouvrez-le, et allez dans le fichier `project.json`.

![Project.json](https://cdn.hashnode.com/res/hashnode/image/upload/v1749038798352/23d8b1b9-5bbf-43df-9444-7adf1f7a9c2f.png align="center")

Dans le fichier, vous devriez voir votre ID de projet et votre ID d'organisation. Copiez-les et créez des secrets dans votre dépôt GitHub pour chacun.

![jeton vercel, id d'organisation, id de projet.](https://cdn.hashnode.com/res/hashnode/image/upload/v1749037787198/53b42a96-ad79-4895-aba0-abe6d79eceb5.png align="center")

### Créer votre fichier de workflow GitHub

À la racine de votre dossier de projet, créez le dossier `.github/workflow`. Ensuite, créez un fichier de workflow appelé `vercel_deploy.yml`.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1749039652451/f3c3a4ca-5d19-4866-a69d-9f4d3a760d8f.png align="center")

Dans le fichier, écrivez ceci :

```yaml
name: Déploiement de production Vercel
env:
  VERCEL_ORG_ID: ${{ secrets.VERCEL_ORG_ID }}
  VERCEL_PROJECT_ID: ${{ secrets.VERCEL_PROJECT_ID }}
on:
  push:
    branches:
      - main
    paths:
      - '01-simple-blog/**'  

jobs:
  Deploy-Production:
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: 01-simple-blog
    steps:
      - uses: actions/checkout@v2

      - name: Installer le CLI Vercel
        run: npm install --global vercel@latest

      - name: Récupérer les informations d'environnement Vercel
        run: vercel pull --yes --environment=production --token=${{ secrets.VERCEL_TOKEN }}

      - name: Construire les artefacts du projet
        run: vercel build --prod --token=${{ secrets.VERCEL_TOKEN }}
        continue-on-error: true
        
      - name: Déployer les artefacts du projet sur Vercel
        run: vercel deploy --prebuilt --prod --token=${{ secrets.VERCEL_TOKEN }}
```

Ceci est le fichier de workflow pour mon projet [simple-writer-portfolio](https://github.com/chidiadi01/simple-writer-portfolio/blob/main/.github/workflows/vercel_deploy.yml).

Tout d'abord, nous avons les variables d'environnement :

```yaml
env:
  VERCEL_ORG_ID: ${{ secrets.VERCEL_ORG_ID }}
  VERCEL_PROJECT_ID: ${{ secrets.VERCEL_PROJECT_ID }}
# Autres codes
```

Ensuite, nous avons le déclencheur. Cela se déclenche lorsque je pousse vers la branche main, affectant les fichiers dans le sous-répertoire `01-simple-blog`.

```yaml
# Code précédent
on:
  push:
    branches:
      - main
    paths:
      - '01-simple-blog/**'  
# Autres codes
```

Ensuite, nous avons la définition du travail. Ici, j'ai défini un travail "Deploy-Production" qui s'exécute sur Ubuntu. Par défaut, toutes les commandes là-bas s'exécuteront dans le répertoire `01-simple-blog`, ce qui équivaut à exécuter `cd 01-simple-blog` depuis la racine avant d'exécuter les commandes sur le shell. Je l'ai fait parce que le projet Next.js est dans ce répertoire, où se trouve le `package.json`.

```yaml
# Code précédent
jobs:
  Deploy-Production:
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: 01-simple-blog
# Autres codes
```

Ensuite, les étapes impliquées :

```yaml
# Code précédent
 steps:
      - uses: actions/checkout@v2

      - name: Installer le CLI Vercel
        run: npm install --global vercel@latest

      - name: Récupérer les informations d'environnement Vercel
        run: vercel pull --yes --environment=production --token=${{ secrets.VERCEL_TOKEN }}

      - name: Construire les artefacts du projet
        run: vercel build --prod --token=${{ secrets.VERCEL_TOKEN }}
        continue-on-error: true
        
      - name: Déployer les artefacts du projet sur Vercel
        run: vercel deploy --prebuilt --prod --token=${{ secrets.VERCEL_TOKEN }}
```

Avec ces étapes, Vercel est d'abord installé sur le runner GitHub. Ensuite, les informations d'environnement de Vercel sont récupérées. Le projet est construit avec `vercel build`, et les artefacts pré-construits sont ensuite poussés vers Vercel.

### Pousser vers GitHub et regarder votre code se déployer

Stagez vos changements, le cas échéant :

```bash
git add .
```

Validez les changements :

```bash
git commit -m "Ajout du workflow GitHub Actions"
```

Et poussez :

```bash
git push origin
```

Maintenant, allez dans votre dépôt en ligne, et vérifiez le déploiement.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1749042451313/3fa5a9a8-c14b-4f55-9e04-c51310500c3f.png align="center")

![Journaux d'exécution du workflow](https://cdn.hashnode.com/res/hashnode/image/upload/v1749042384631/d941710c-697d-46b8-a106-30f6ac3cedc3.png align="center")

## Conclusion

Avec votre workflow GitHub de base en place, vous pouvez maintenant apporter des modifications à votre code, pousser vers GitHub, et le voir se déployer automatiquement. Bien que Vercel vous permette de connecter votre dépôt directement, cette méthode vous offre plus de flexibilité et de personnalisation. Si vous avez aimé cet article, partagez-le avec d'autres. Vous pouvez également me contacter sur [LinkedIn](https://linkedin.com/in/chidiadi-anyanwu) ou [X](https://x.com/chidiadi01).