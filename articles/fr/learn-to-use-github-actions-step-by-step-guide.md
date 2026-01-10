---
title: 'Apprendre à utiliser GitHub Actions : un guide étape par étape'
subtitle: ''
author: Rajdeep Singh
co_authors: []
series: null
date: '2025-01-16T14:35:38.373Z'
originalURL: https://freecodecamp.org/news/learn-to-use-github-actions-step-by-step-guide
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1736973439529/e0445f1c-62df-441f-a335-96c468a373da.png
tags:
- name: GitHub
  slug: github
- name: GitHub Actions
  slug: github-actions
seo_title: 'Apprendre à utiliser GitHub Actions : un guide étape par étape'
seo_desc: 'GitHub Actions are one of the most helpful features of GitHub. Actions
  help you automate, build, test, and deploy your app from your GitHub. They also
  help you perform code reviews and tests, manage branches, triage issues, and more.

  In simple terms,...'
---

[GitHub Actions](https://docs.github.com/en/actions) sont l'une des fonctionnalités les plus utiles de GitHub. Les Actions vous aident à automatiser, construire, tester et déployer votre application depuis votre GitHub. Elles vous aident également à effectuer des revues de code et des tests, gérer des branches, trier des problèmes, et plus encore.

En termes simples, le workflow GitHub crée un environnement (machine virtuelle basée sur le **runner**) pour tester, construire et déployer votre code dans le cloud en fonction de l'action que vous décrivez dans le fichier GitHub Action.

Ce tutoriel vous apprend comment ajouter une GitHub Action, en fournissant un exemple et des instructions étape par étape. Il convient aux débutants et aux développeurs intermédiaires.

## Table des matières :

1. [Prérequis](#heading-prerequis)
    
2. [Concepts clés des GitHub Actions](#heading-concepts-cles-des-github-actions)
    
3. [Comment créer une GitHub Action dans votre dépôt](#heading-comment-creer-une-github-action-dans-votre-depot)
    
    * [Créer une GitHub Action en utilisant l'interface utilisateur de GitHub](#heading-creer-une-github-action-en-utilisant-linterface-utilisateur-de-github)
        
    * [Créer une GitHub Action localement avec votre IDE](#heading-creer-une-github-action-localement-avec-votre-ide)
        
4. [Syntaxe des GitHub Actions](#heading-syntaxe-des-github-actions)
    
5. [Exemples de GitHub Actions](#heading-exemples-de-github-actions)
    
6. [Conclusion](#heading-conclusion)
    

## Prérequis

Pour tirer le meilleur parti de cet article, vous devez avoir au moins une connaissance de base de l'utilisation de GitHub et de YAML. Si vous ne connaissez pas les fondamentaux de GitHub, consultez [ce tutoriel approfondi sur Git et GitHub](https://www.freecodecamp.org/news/guide-to-git-github-for-beginners-and-experienced-devs/). Et [voici une introduction à YAML](https://www.freecodecamp.org/news/what-is-yaml-the-yml-file-format/).

Vous devez également comprendre les concepts principaux derrière les **événements**, **workflows**, **jobs** et **runners** et pourquoi ils sont importants lors de la création d'une GitHub Action.

Ce sont les ingrédients clés des actions GitHub, nous allons donc les passer en revue un par un avant de plonger dans la partie principale du tutoriel.

## Concepts clés des GitHub Actions

### **Workflows**

Un workflow est un processus automatisé configurable qui exécute une ou plusieurs tâches. Il est créé avec un fichier YAML dans votre dépôt et s'exécute lorsqu'un événement le déclenche. Les workflows peuvent également être déclenchés manuellement ou selon un calendrier défini.

Les workflows sont définis dans le répertoire `.github/workflows` d'un dépôt. Dans le dépôt, vous pouvez créer plusieurs workflows qui effectuent différentes tâches, telles que :

1. Construire et tester les pull requests
    
2. Déployer votre application dans le cloud
    
3. Exécuter un test sur chaque pull request
    

### **Événements**

Un événement est une activité spécifique dans un dépôt qui déclenche ou exécute un workflow dans votre dépôt GitHub. Par exemple, lorsque vous poussez du code dans le dépôt, il déclenche l'événement `push`. Il en va de même lorsque vous créez un nouveau problème - il déclenche l'événement `issues`. Et lorsque quelqu'un fait une pull request dans votre dépôt, il déclenche l'événement `pull_request`.

![Description des différents types d'événements dans GitHub](https://cdn.hashnode.com/res/hashnode/image/upload/v1736342712858/866f61a7-4750-45bf-82ea-d4e9535069a4.png align="center")

Voici quelques événements courants des GitHub Actions :

1. Push
    
2. pull_request
    
3. release
    
4. label
    
5. issues
    
6. milestone
    
7. label
    

Les événements `push`, `release` et `pull_request` sont les événements les plus courants. Pour en savoir plus sur les événements, vous pouvez [consulter la documentation GitHub](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows#about-events-that-trigger-workflows).

Il est bon de spécifier le type d'événement dans une GitHub Action. Par exemple, spécifier l'événement `pull_request` déclenchera l'action chaque fois qu'un utilisateur crée une pull request dans le dépôt GitHub.

```yaml
# .github/workflows/demo.yml

on:
  issues:
    types: [opened, edited, milestoned]
  
  pull_request:
    types:
      - opened
    branches:
      - 'releases/**'
```

Cela est utile car, si vous ne déclarez pas un type d'activité d'événement spécifique dans votre type d'événement, cela peut entraîner l'utilisation de ressources inutiles. La GitHub Action sera déclenchée avec chaque nouvelle pull request - il est donc préférable de définir quel type d'événement vous utilisez.

### Jobs

Les jobs des GitHub Actions s'exécutent en parallèle par défaut. Un workflow GitHub Action exécute une ou plusieurs tâches, chacune contenant un ensemble d'étapes qui exécutent des commandes ou des actions. Voici un exemple :

```yaml
# .github/workflows/demo.yml

name: Demo Workflows

on:
   push:

# Une exécution de workflow est composée d'une ou plusieurs tâches qui peuvent s'exécuter séquentiellement ou en parallèle
jobs:

jobs:
```

Vous pouvez définir une tâche pour qu'elle dépende d'(une) autre(s) tâche(s). Si les tâches n'ont pas de dépendances, elles s'exécuteront en parallèle. Lorsqu'une tâche dépend d'une autre, elle attendra que cette tâche se termine avant de commencer.

```yaml
# .github/workflows/demo.yml

jobs:
  build:
    name: Build
    needs: [ Development ]
    steps:
      - name: Build and deploy on Cloud
  dev:
    name: Development
    steps:
      - name: Run the developer

  Test:
    needs: [ build, dev ]
    name: Testing
    steps:
      - name: Testing the application
```

### Runners

Les **runners** sont des serveurs qui exécutent les workflows lorsqu'ils sont déclenchés. Chaque runner ne peut gérer qu'une seule tâche à la fois. GitHub propose des runners pour Ubuntu Linux, Microsoft Windows et MacOS pour exécuter vos workflows.

```yaml
# .github/workflows/demo.yml

name: Demo workflows

on:
  # Déclenche le workflow sur les événements push ou pull request mais uniquement pour la branche "main"
   push:
    branches: [ "main" ]

# Une exécution de workflow est composée d'une ou plusieurs tâches qui peuvent s'exécuter séquentiellement ou en parallèle
jobs:
  # Ce workflow contient une seule tâche appelée "build"
  build:
    # Le type de runner sur lequel la tâche sera exécutée
    runs-on: ubuntu-latest
```

Pour définir les runners, spécifiez la valeur du runner dans l'option `runs-on`. Vous pouvez la fournir sous forme de **chaîne unique** ou de **tableau de chaînes**.

```yaml
# .github/workflows/demo.yml

# Chaîne
runs-on: ubuntu-latest
# Tableau de chaînes
runs-on: [ ubuntu-latest, windows-latest, macos-latest ]
```

Maintenant que vous êtes familiarisé avec les éléments clés des GitHub Actions et leur fonctionnement, voyons comment utiliser les Actions en pratique.

## Comment créer une GitHub Action dans votre dépôt

Vous pouvez créer une GitHub Action dans GitHub très facilement. Il y a deux façons de le faire :

1. En utilisant l'interface utilisateur de Github
    
2. Localement avec votre IDE
    

De nombreux développeurs utilisent l'interface utilisateur de GitHub pour créer une Action. C'est une manière courante de créer une Action. Vous n'avez pas besoin de créer un dossier `.github/workflow` lorsque vous utilisez l'interface utilisateur de GitHub. GitHub crée automatiquement ce dossier pour vous. En revanche, pour des actions GitHub complexes, vous utiliserez généralement votre IDE.

Examinons chaque approche maintenant.

### Créer une GitHub Action en utilisant l'interface utilisateur de GitHub

Tout d'abord, allez dans le dépôt GitHub où vous souhaitez créer votre GitHub Action.

![Dépôt GitHub où vous souhaitez créer votre action](https://cdn.hashnode.com/res/hashnode/image/upload/v1736510921442/e4b338f5-c928-4aba-953d-0df5adee0bd3.png align="center")

Pour créer l'action, suivez ces étapes :

#### 1. Cliquez sur l'onglet Action

Cliquez sur l'onglet Action pour créer une GitHub Action. Vous verrez la page suivante :

![Créer la GitHub Action](https://cdn.hashnode.com/res/hashnode/image/upload/v1736511145120/79fc5a4a-26b9-4f41-bc7b-1c976ff47663.png align="center")

#### 2. Sélectionnez l'action de workflow

Les suggestions de GitHub fonctionnent automatiquement en fonction de la nature de votre projet. Sélectionnez le workflow GitHub et cliquez sur le bouton de configuration pour créer votre action.

![Sélectionnez le workflow github dans github](https://cdn.hashnode.com/res/hashnode/image/upload/v1736511580215/48ed1bb6-bc25-43fd-bf3d-2ac9f945f3eb.png align="center")

#### 3. Créez le workflow GitHub

Vous verrez la page suivante où vous pouvez éditer et créer votre action. Cliquez sur le bouton de validation des modifications pour sauvegarder l'action.

![Éditez et créez votre Action dans Github.](https://cdn.hashnode.com/res/hashnode/image/upload/v1736858011259/267d62ad-f41b-449e-b0dd-dab3a9251ba1.png align="center")

Et c'est tout - vous avez créé votre GitHub Action.

### Créer une GitHub Action localement avec votre IDE

Tout d'abord, ouvrez votre projet dans votre IDE actuel, tel que VS Code, Neovim, Vim, ou autre. Ensuite, créez un fichier `.github/workflow/nom-du-workflow.yml` dans votre projet. Copiez et collez le code suivant et sauvegardez et poussez votre code local dans le dépôt GitHub.

L'exemple de code d'action de workflow GitHub suivant imprime un message hello world.

```yaml
# .github/workflows/demo.yml

name: CI

# Contrôle quand le workflow sera exécuté
on:
  # Déclenche le workflow sur les événements push ou pull request mais uniquement pour la branche "main"
  push:
    branches: [ "main" ]

# Une exécution de workflow est composée d'une ou plusieurs tâches qui peuvent s'exécuter séquentiellement ou en parallèle
jobs:
  # Ce workflow contient une seule tâche appelée "build"
  build:
    # Le type de runner sur lequel la tâche sera exécutée
    runs-on: ubuntu-latest

    # Les étapes représentent une séquence de tâches qui seront exécutées dans le cadre de la tâche
    steps:
      # Vérifie votre dépôt sous $GITHUB_WORKSPACE, afin que votre tâche puisse y accéder
      - uses: actions/checkout@v4

      # Exécute une seule commande en utilisant le shell du runner
      - name: Exécuter un script en une ligne
        run: echo Bonjour, le monde !
```

J'utilise l'IDE Neovim pour créer un fichier `.github/workflow/demo.yml`. Cela ressemble à ceci.

![Créez une action localement en utilisant votre IDE.](https://cdn.hashnode.com/res/hashnode/image/upload/v1736935606919/aa187277-118a-4990-b240-684ced2f8a55.png align="center")

## Syntaxe des GitHub Actions

Pour créer une GitHub Action, il est important de comprendre la syntaxe des GitHub Actions. Dans cette section, vous apprendrez certaines des syntaxes les plus courantes que vous utiliserez pour créer vos Actions.

Nous travaillerons avec cet exemple d'Action et le passerons en revue partie par partie ci-dessous :

```yaml
# .github/workflows/demo.yml

name: Modèle d'Action GitHub 

on:

  pull_request:
    branches: [ "main" ]

  schedule:
    - cron:  '30 5,17 * * *'
  
  workflow_call:
    inputs:
      username:
        description: 'Un nom d\'utilisateur passé depuis le workflow appelant'
        default: 'john-doe'
        required: false
        type: string

  permissions:
    actions: read|write|none

  # permissions : read|write|none

# Une exécution de workflow est composée d'une ou plusieurs tâches qui peuvent s'exécuter séquentiellement ou en parallèle
jobs:

  # Ce workflow contient une seule tâche appelée "build"

  build:

    runs-on: ubuntu-latest

    # Les étapes représentent une séquence de tâches qui seront exécutées dans le cadre de la tâche

    steps:

      # Vérifie votre dépôt sous $GITHUB_WORKSPACE, afin que votre tâche puisse y accéder
      - uses: actions/checkout@v4
        if: ${{ github.event_name == 'pull_request' && github.event.action == 'unassigned' }}
        shell: zsh
        name: Installation du package NPM
        run: npm install
        with:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          first_name: Github
          last_name: Action
          args: L\'événement ${{ github.event_name }} a déclenché cette étape.
          entrypoint: /bin/echo
```

Maintenant, comprenons chaque option que vous pouvez voir dans cet exemple de workflow GitHub Action :

1. `name` : Le nom décrit le nom du workflow.
    
2. `pull_request` : La pull request fait partie du type d'événement. Cela signifie que quelqu'un a ajouté une pull request dans votre dépôt et que le workflow suivant a été exécuté.
    
3. `schedule` : Avec un calendrier, vous pouvez définir l'horaire dans vos workflows. Vous pouvez planifier un workflow pour qu'il s'exécute à certaines tâches à des heures UTC spécifiques ou en fonction d'intervalles après cinq minutes, etc.
    
4. `workflow_call` : Cela définit les entrées et sorties pour un workflow réutilisable.
    
5. `permissions` : Dans GitHub, certaines tâches nécessitent des permissions spéciales lors de l'utilisation de l'application GitHub et de l'API GitHub. Par exemple, pour les problèmes, la permission `write` permet à un utilisateur d'ajouter un commentaire à un problème. Pour d'autres permissions, vous pouvez consulter la documentation.
    
6. `jobs` : L'option `jobs` exécute une ou plusieurs tâches dans votre GitHub Action, chacune contenant un ensemble d'étapes qui exécutent des commandes ou des actions.
    
7. `runs-on` : L'option `runs-on` définit le type de machine sur lequel la tâche sera exécutée.
    
8. `steps` : Les tâches contiennent une séquence de tâches appelées `steps`. Les étapes peuvent exécuter des commandes, définir des tâches ou une action dans votre dépôt.
    
9. `name` : L'option name est utilisée pour définir le nom de la tâche, qui est affiché dans l'interface utilisateur de GitHub.
    
10. `if` : l'option `if` fonctionne de manière similaire à une conditionnelle if. Elle empêche une étape de s'exécuter sauf si une condition est remplie.
    
11. `shell` : L'option `shell` vous permet de définir un shell personnalisé.
    
12. `run` : L'option `run` aide à exécuter des commandes dans le shell du système d'exploitation. Par exemple, `run : ls`, `run : pwd`, etc.
    
13. `uses` : Avec l'option `uses`, vous pouvez exécuter des unités de code réutilisables ou d'autres packages. Vous l'utilisez généralement pour exécuter un package GitHub publié par un autre développeur sur le [GitHub marketplace](https://github.com/marketplace). La plupart des développeurs de packages utilisent JavaScript ou des fichiers de conteneur Docker.
    
14. `with` : l'option `with` accepte une valeur sous forme de map avec une paire clé/valeur. Elle a deux sous-options : `args` et un `entrypoint`. L'entrée est utilisée pour définir le fichier d'entrée pour Dockerfile. L'option args sera passée au point d'entrée du conteneur.
    

Vous utiliserez généralement cette syntaxe pour créer vos GitHub Actions. Dans la section suivante, vous apprendrez comment l'utiliser pour construire une GitHub Action.

Pour une syntaxe avancée des GitHub Actions, vous pouvez [consulter la documentation Github](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions).

## Exemples de GitHub Actions

Pour mieux comprendre comment fonctionnent les GitHub Actions, construisons quatre exemples de workflow GitHub Actions. Ce sont des exemples courants que de nombreux développeurs utilisent et qui vous apprendront comment fonctionnent les GitHub Actions.

### Configuration de Node

Dans la GitHub Action suivante, nous allons configurer un environnement Node.js pour notre application. Une fois que vous avez fait cela, vous pouvez tester et déployer votre application Node.js.

```yaml
# .github/workflows/nodejs.yml

name: Configurer l'environnement Node.js

on:
  push:
    branches: [ "main" ]
 
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - name: Utiliser Node.js ${{ matrix.node-version }}
      uses: actions/setup-node@v4
      with:
        node-version:  21
        cache: 'npm'
    - run: npm ci
    - run: npm run build --if-present
    - run: npm test
```

Pour notre exemple, nous exécutons notre action sur une machine Ubuntu. L'action GitHub est déclenchée chaque fois que vous (ou quelqu'un) poussez du code dans le dépôt. L'extension `actions/checkout@v4` définit la variable d'environnement `$GITHUB_WORKSPACE` sur votre répertoire de travail.

L'extension `actions/setup-node@v4` configure l'environnement Node.js, et l'option `run` de GitHub exécute la commande Linux.

### Configuration de Deno

Dans la GitHub Action suivante, nous allons configurer un environnement Deno pour notre application. Vous pouvez tester et analyser (en utilisant deno lint) le code pour détecter les erreurs, les problèmes de style, etc.

```yaml
name: Deno

on:
  push:
    branches: ["main"]

permissions:
  contents: read

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Configurer le dépôt
        uses: actions/checkout@v4

      - name: Configurer Deno
        uses: denoland/setup-deno@v2
        with:
          deno-version: v2.1.5

      - name: Exécuter le linter
        run: deno lint

      - name: Exécuter les tests
        run: deno test -A
```

Pour cet exemple, nous exécutons notre action sur une machine Ubuntu. L'action GitHub est déclenchée chaque fois que vous (ou quelqu'un) poussez du code dans le dépôt. L'extension `actions/checkout@v4` définit la variable d'environnement `$GITHUB_WORKSPACE` sur votre répertoire de travail.

L'extension `denoland/setup-deno@v2` configure l'environnement Deno et l'option `run` de GitHub exécute la commande Linux.

### Fichiers Zip

Dans l'exemple suivant, nous allons combiner le dossier `dist` et le fichier `manifest.json` dans une archive zip. Ensuite, nous allons sauvegarder le fichier zippé en tant qu'artefact pour une utilisation ultérieure ou un téléchargement :

```yaml
name: Fichiers Zip

on:
  release:
    types: [published]

jobs:
  zip-files:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: vimtor/action-zip@v1.2
        with:
          files: dist/ manifest.json
          dest: build.zip

       - uses: actions/upload-artifact@v4
         with:
           name: fichier zip
           path: ${{ github.workspace }}/build.zip
```

Pour cet exemple, nous exécutons notre action sur une machine Ubuntu. L'action GitHub est déclenchée chaque fois que quelqu'un pousse du code dans le dépôt. L'extension `actions/checkout@v4` définit la variable d'environnement `$GITHUB_WORKSPACE` sur votre répertoire de travail.

L'extension ou le package [`vimtor/action-zip@v1.2`](https://github.com/marketplace/actions/easy-zip-files) convertit les fichiers dans un dossier zip. Le package `actions/upload-artifact@v4` télécharge les artefacts pendant une exécution de workflow.

![Télécharger l'artefact dans GitHub Action.](https://cdn.hashnode.com/res/hashnode/image/upload/v1736875426358/0b918abf-317d-407c-a179-50693604deb7.png align="center")

### Déployer un site web statique

L'exemple suivant de GitHub Actions montre comment déployer un site web HTML sur GitHub Pages.

```yaml
# Workflow simple pour déployer du contenu statique sur GitHub Pages
name: Déployer du contenu statique sur Pages

on:
  # S'exécute sur les pushes ciblant la branche par défaut
  push:
    branches: ["main"]

# Définit les permissions du GITHUB_TOKEN pour permettre le déploiement sur GitHub Pages
permissions:
  contents: read
  pages: write
  id-token: write

# Autorise uniquement un déploiement concurrent, en sautant les exécutions en file d'attente entre l'exécution en cours et la dernière en file d'attente.
# Cependant, n'annulez PAS les exécutions en cours car nous voulons permettre à ces déploiements de production de se terminer.
concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:

  # Une seule tâche de déploiement puisque nous déployons simplement
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:

      - name: Checkout
        uses: actions/checkout@v4

      - name: Configurer Pages
        uses: actions/configure-pages@v5

      - name: Télécharger l'artefact
        uses: actions/upload-pages-artifact@v3
        with:
          # Télécharger l'ensemble du dépôt
          path: '.'

      - name: Déployer sur GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

Pour cet exemple, nous exécutons notre action sur une machine Ubuntu. L'action GitHub est déclenchée chaque fois que vous poussez du code dans le dépôt. L'extension `actions/checkout@v4` définit la variable d'environnement `$GITHUB_WORKSPACE` sur votre répertoire de travail.

Le package `actions/configure-pages@v5` vous aide à configurer GitHub Pages et vous permet de collecter des métadonnées sur votre site web. Pour plus de détails, consultez la documentation de l'action [configure-pages](https://github.com/marketplace/actions/configure-github-pages).

Le package `actions/upload-pages-artifact@v3` vous aide à empaqueter et télécharger des artefacts qui peuvent être déployés sur [GitHub Pages](https://pages.github.com/).

Le package `actions/deploy-pages@v4` est utilisé pour [déployer votre site web](https://github.com/actions/deploy-pages) sur GitHub Pages.

## Conclusion

GitHub Actions est un sujet vaste. Pour les comprendre plus pleinement, vous pouvez commencer par un exemple d'Action de base puis passer à des Actions plus avancées.

Lorsque vous utilisez GitHub Actions, le plus gros problème est d'attendre les résultats. Par exemple, créer et mettre à jour la date à laquelle le fichier GitHub Action pousse du code dans GitHub puis attendre le résultat de GitHub Action. Cela peut être une tâche chronophage, vous pouvez donc utiliser l'outil CLI act au lieu d'exécuter GitHub Actions localement sur un ordinateur portable ou un ordinateur.

J'ai publié un article approfondi sur freeCodeCamp sur [comment utiliser l'outil CLI Act](https://www.freecodecamp.org/news/how-to-run-github-actions-locally/) si vous souhaitez en savoir plus à ce sujet.

Merci d'avoir lu !