---
title: Comment créer votre première Action GitHub en JavaScript
subtitle: ''
author: Bassem
co_authors: []
series: null
date: '2022-01-10T17:36:34.000Z'
originalURL: https://freecodecamp.org/news/build-your-first-javascript-github-action
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/banner-1.png
tags:
- name: GitHub Actions
  slug: github-actions
- name: JavaScript
  slug: javascript
seo_title: Comment créer votre première Action GitHub en JavaScript
seo_desc: 'I love working with GitHub Actions. They''re easy to use yet so powerful.
  I''m especially excited when I see how creative people are when using them to automate
  different tasks.

  I want you to have that same power. That''s why I''m going to show you how t...'
---

J'adore travailler avec [GitHub Actions](https://docs.github.com/en/actions). Elles sont faciles à utiliser et pourtant si puissantes. Je suis particulièrement excité lorsque je vois à quel point les gens sont créatifs en les utilisant pour automatiser différentes tâches.

Je veux que vous ayez ce même pouvoir. C'est pourquoi je vais vous montrer comment créer votre première action personnalisée en JavaScript en quelques étapes seulement.

Commençons.

## Qu'est-ce qu'une Action GitHub ?

Tout d'abord, nous devons établir la distinction entre "GitHub Actions" et une "Action". Le premier est le nom du produit et le second est un code personnalisé que vous pouvez inclure dans un travail de workflow en tant qu'étape pour accomplir une tâche.

Par exemple, une action peut publier votre code sur un gestionnaire de paquets comme [npm](https://www.npmjs.com/) ou [yarn](https://yarnpkg.com/). Elle peut également s'intégrer à un fournisseur de services SMS pour vous alerter lorsqu'un problème urgent est créé dans votre dépôt. Ou elle peut allumer votre machine à café lorsque vous créez une nouvelle pull request. 

Les possibilités sont infinies pour ce que vous pouvez faire !

## Quels sont les composants de GitHub Actions ?

Avant de commencer à écrire du code, il est important pour nous de comprendre les éléments de base de GitHub Actions.

![build-your-first-github-action_components](https://www.freecodecamp.org/news/content/images/2022/01/build-your-first-github-action_components.png)

Décomposons ce diagramme, en commençant par la gauche et en allant vers la droite :

1. **Événement** : C'est l'événement qui déclenche l'action. Il représente une activité dans le dépôt qui déclenchera l'exécution d'un workflow.
1. **Workflow** : C'est le workflow qui est exécuté lorsque l'événement se produit.
1. **Travail** : Un ensemble d'étapes qui sont exécutées en séquence pour accomplir une tâche. Chaque travail s'exécute sur son propre runner.
1. **Étape** : Une étape est soit un script shell, soit une action qui sera exécutée sur le runner assigné pour le travail dont l'étape fait partie.
1. **Runner** : Un runner est une machine virtuelle (ou tout ordinateur avec un système d'exploitation pris en charge) qui exécute les étapes d'un travail.

Cela est très bien expliqué dans la documentation extensive de GitHub, et vous pouvez en lire plus sur les composants [ici](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions#the-components-of-github-actions).

## Quand dois-je créer une Action ?

Puisque chaque étape peut être soit un script shell soit une action, comment décider quelle option choisir ?

Si vous répondez "oui" à l'une des questions suivantes, alors vous êtes mieux de créer une Action :

1. D'autres personnes bénéficieront-elles de l'action que vous créez et la réutiliseront-elles ?
1. Avez-vous besoin de construire une logique complexe qui ne peut pas être écrite dans un script shell ?
1. Allez-vous utiliser des bibliothèques tierces ?
1. Avez-vous besoin de faire des appels API à un service tiers ?
1. Avez-vous la capacité de maintenir ce code et de publier des correctifs ou des mises à jour ?
1. Avez-vous besoin de pouvoir exécuter cette action sur différents systèmes d'exploitation ?
1. Êtes-vous compétent en JavaScript mais pas en Bash ou PowerShell ?
1. Voulez-vous apprendre à en créer une ?

## Créons notre Action

Nous allons créer une Action qui créera un commentaire chaque fois qu'une pull request est ouverte sur notre dépôt et ajoutera des labels en fonction des types de fichiers modifiés. Le commentaire contiendra un résumé des changements introduits dans la pull request.

![build-your-first-github-preview](https://www.freecodecamp.org/news/content/images/2022/01/build-your-first-github-preview.png)

### 1. Créer un dépôt public vide

Commençons par créer un dépôt GitHub vide appelé : `PR-metadata-action`. Ce sera le dépôt que nous utiliserons pour stocker notre Action.

Il doit être public, sinon nous ne pourrons pas l'utiliser dans nos workflows.

![build-your-first-github-action_newrepo-1](https://www.freecodecamp.org/news/content/images/2022/01/build-your-first-github-action_newrepo-1.png)

### 2. Cloner le dépôt localement et initialiser un projet Node

Allez dans le dossier où vous souhaitez stocker le dépôt de l'Action. Ensuite, clonons le dépôt sur notre machine :

```bash
$ git clone git@github.com:Link-/PR-metadata-action.git
Cloning into 'PR-metadata-action'...
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (4/4), done.
Receiving objects: 100% (4/4), done.
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
```

Dans le dossier de notre dépôt nouvellement créé, initialisons un nouveau projet Node.js :

```bash
$ cd PR-metadata-action/
$ npm init -y
Wrote to /Users/link-/PR-metadata-action/package.json:

{
  "name": "pr-metadata-action",
  "version": "1.0.0",
  "description": "Ajoute les changements de fichiers de la pull request en tant que commentaire à une nouvelle PR ouverte",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/Link-/PR-metadata-action.git"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "bugs": {
    "url": "https://github.com/Link-/PR-metadata-action/issues"
  },
  "homepage": "https://github.com/Link-/PR-metadata-action#readme"
}
```

### 3. Créer un fichier de métadonnées d'Action

Créons `action.yml`. Ce fichier est très important, car il définira l'`interface` de notre Action :

- **inputs** : les paramètres contenant les données que l'action s'attend à utiliser pendant l'exécution
- **outputs** : les données qu'une action définit après son exécution. Nous n'aurons pas de sortie pour notre action cette fois-ci.
- **runs** : spécifie le runtime d'exécution de l'action, qui sera node16 dans ce cas

Lisez plus sur la [syntaxe du fichier de métadonnées](https://docs.github.com/en/actions/creating-actions/metadata-syntax-for-github-actions).

```yaml
name: 'PR Metadata Action'
description: 'Ajoute les changements de fichiers de la pull request en tant que commentaire à une nouvelle PR ouverte'
inputs:
  owner:
    description: 'Le propriétaire du dépôt'
    required: true
  repo:
    description: 'Le nom du dépôt'
    required: true
  pr_number:
    description: 'Le numéro de la pull request'
    required: true
  token:
    description: 'Le token à utiliser pour accéder à l'API GitHub'
    required: true
runs:
  using: 'node16'
  main: 'index.js'
```

### 4. Ajouter les packages de l'outil Actions

GitHub a créé un kit de développement logiciel (SDK) open source qui rendra votre vie beaucoup plus facile lors de la création d'actions.

Les 2 principaux packages que nous utiliserons aujourd'hui sont :

- [@actions/core](https://github.com/actions/toolkit/tree/main/packages/core) : ce package contient la fonctionnalité principale de l'Action, telle que l'objet `context` qui contient les informations sur l'exécution en cours, l'objet `inputs` qui contient les paramètres de l'action, et l'objet `outputs` qui contiendra les données que l'action définit après son exécution.

- [@actions/github](https://github.com/actions/toolkit/tree/main/packages/github) : ce package contient le client REST de l'API GitHub que nous utiliserons pour interagir avec l'API GitHub.

```bash
$ npm install @actions/core
added 3 packages, and audited 4 packages in 1s

found 0 vulnerabilities

$ npm install @actions/github
added 21 packages, and audited 25 packages in 1s

found 0 vulnerabilities
```

Notre structure de dossier devrait maintenant ressembler à ceci :

```bash
/Users/link-/PR-metadata-action
├── LICENSE
├── README.md
├── action.yml
├── node_modules
├── package-lock.json
└── package.json

1 directory, 6 files
```

### 5. Écrire l'Action

Créer un fichier `.gitignore` est important à ce stade pour éviter de pousser des fichiers inutiles vers le dépôt.

Un outil génial que j'utilise fréquemment est : <https://www.toptal.com/developers/gitignore>

Mon fichier `.gitignore` est :

```text
https://www.toptal.com/developers/gitignore/api/visualstudiocode,macos,node
```

Créez-en un qui est spécifique à votre environnement et projet.

Nous sommes enfin prêts à créer notre fichier `index.js`. C'est ici que toute la logique de notre action sera. Nous pouvons définitivement avoir une structure plus complexe, mais pour l'instant, un fichier suffira.

J'ai commenté tout le code ci-dessous pour que vous sachiez ce qui se passe étape par étape.

```js
const core = require('@actions/core');
const github = require('@actions/github');

const main = async () => {
  try {
    /**
     * Nous devons récupérer toutes les entrées qui ont été fournies à notre action
     * et les stocker dans des variables pour que nous puissions les utiliser.
     **/
    const owner = core.getInput('owner', { required: true });
    const repo = core.getInput('repo', { required: true });
    const pr_number = core.getInput('pr_number', { required: true });
    const token = core.getInput('token', { required: true });

    /**
     * Maintenant, nous devons créer une instance d'Octokit que nous utiliserons pour appeler
     * les endpoints de l'API REST de GitHub.
     * Nous passerons le token comme argument au constructeur. Ce token
     * sera utilisé pour authentifier nos requêtes.
     * Vous pouvez trouver toutes les informations sur la façon d'utiliser Octokit ici :
     * https://octokit.github.io/rest.js/v18
     **/
    const octokit = new github.getOctokit(token);

    /**
     * Nous devons récupérer la liste des fichiers qui ont été modifiés dans la Pull Request
     * et les stocker dans une variable.
     * Nous utilisons octokit.paginate() pour boucler automatiquement sur toutes les pages des
     * résultats.
     * Référence : https://octokit.github.io/rest.js/v18#pulls-list-files
     */
    const { data: changedFiles } = await octokit.rest.pulls.listFiles({
      owner,
      repo,
      pull_number: pr_number,
    });


    /**
     * Contient la somme de toutes les additions, suppressions et changements
     * dans tous les fichiers de la Pull Request.
     **/
    let diffData = {
      additions: 0,
      deletions: 0,
      changes: 0
    };

    // Référence pour l'utilisation de Array.reduce() :
    // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce
    diffData = changedFiles.reduce((acc, file) => {
      acc.additions += file.additions;
      acc.deletions += file.deletions;
      acc.changes += file.changes;
      return acc;
    }, diffData);

    /**
     * Boucler sur tous les fichiers modifiés dans la PR et ajouter des labels selon 
     * les types de fichiers.
     **/
    for (const file of changedFiles) {
      /**
       * Ajouter des labels selon les types de fichiers.
       */
      const fileExtension = file.filename.split('.').pop();
      switch(fileExtension) {
        case 'md':
          await octokit.rest.issues.addLabels({
            owner,
            repo,
            issue_number: pr_number,
            labels: ['markdown'],
          });
        case 'js':
          await octokit.rest.issues.addLabels({
            owner,
            repo,
            issue_number: pr_number,
            labels: ['javascript'],
          });
        case 'yml':
          await octokit.rest.issues.addLabels({
            owner,
            repo,
            issue_number: pr_number,
            labels: ['yaml'],
          });
        case 'yaml':
          await octokit.rest.issues.addLabels({
            owner,
            repo,
            issue_number: pr_number,
            labels: ['yaml'],
          });
      }
    }

    /**
     * Créer un commentaire sur la PR avec les informations que nous avons compilées à partir de la
     * liste des fichiers modifiés.
     */
    await octokit.rest.issues.createComment({
      owner,
      repo,
      issue_number: pr_number,
      body: `
        La Pull Request #${pr_number} a été mise à jour avec : \n
        - ${diffData.changes} changements \n
        - ${diffData.additions} additions \n
        - ${diffData.deletions} suppressions \n
      `
    });

  } catch (error) {
    core.setFailed(error.message);
  }
}

// Appeler la fonction principale pour exécuter l'action
main();
```

### 6. Pousser nos fichiers d'Action vers GitHub

Ajoutons, validons et poussons nos fichiers vers la branche principale en amont :

```bash
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
 .gitignore
 action.yml
 index.js
 package-lock.json
 package.json

nothing added to commit but untracked files present (use "git add" to track)
```

Ajoutons tous les fichiers à être préparés :

```bash
$ git add .
```

Maintenant, nous pouvons valider nos changements :

```bash
$ git commit -m "Add main action structure"
[main 1fc5d18] Add main action structure
 5 files changed, 686 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 action.yml
 create mode 100644 index.js
 create mode 100644 package-lock.json
 create mode 100644 package.json
```

Et poussons nos changements :

```bash
$ git push origin main
Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 16 threads
Compressing objects: 100% (7/7), done.
Writing objects: 100% (7/7), 5.82 KiB | 5.82 MiB/s, done.
Total 7 (delta 0), reused 0 (delta 0), pack-reused 0
To github.com:Link-/PR-metadata-action.git
   457fee2..1fc5d18  main -> main
```

### 7. Comment tester notre Action

Pour pouvoir tester notre action, nous devons créer un bundle. Si vous avez remarqué à l'étape précédente, nous n'avons pas poussé notre dossier `node_modules` qui contient les packages que nous avons utilisés pour construire notre fichier `index.js`.

Notre action ne s'exécutera pas sans ces packages ! Pour résoudre ce problème, nous pouvons utiliser un outil appelé [ncc](https://github.com/vercel/ncc). Il nous aidera à créer un fichier qui inclut notre code et tous les packages dont nous avons besoin pour exécuter notre action.

Commençons par installer `ncc` :

```bash
$ npm install @vercel/ncc

added 1 package, and audited 26 packages in 5s

found 0 vulnerabilities
```

Compiler notre JavaScript est aussi simple que d'exécuter :

```bash
$ ncc build index.js -o dist
ncc: Version 0.22.1
ncc: Compiling file index.js
530kB  dist/index.js
530kB  [845ms] - ncc 0.22.1
```

Cela créera un nouveau répertoire appelé `dist` et créera un fichier appelé `index.js` qui contient notre code et tous les packages dont nous avons besoin pour exécuter notre action.

Maintenant, nous devons nous assurer que notre fichier `action.yml` contient la section `runs` correcte. Vous devez remplacer :

```yaml
runs:
  using: 'node16'
  main: 'index.js'
```

par :

```yaml
runs:
  using: 'node16'
  main: 'dist/index.js'
```

Poussons nos changements une dernière fois en amont (vers notre dépôt GitHub). Assurez-vous que notre dossier `dist/` n'est pas dans le fichier `.gitignore` :

```bash
$ git status
$ git add .
$ git commit -m "Add compiled action"
[main adfc4f0] Add compiled action
 4 files changed, 8505 insertions(+), 3 deletions(-)
 create mode 100644 dist/index.js
$ git push origin main
```

Nous sommes enfin prêts à créer notre workflow ! Créez un nouveau workflow dans le même dépôt ou dans n'importe quel autre dépôt (public ou privé, cela n'a pas d'importance) comme suit :

```bash
mkdir -p .github/workflows
touch .github/workflows/pr-metadata.yaml
```

Copiez le workflow suivant dans notre fichier `pr-metadata.yaml` :

```yaml
name: PR metadata annotation

on: 
  pull_request:
    types: [opened, reopened, synchronize]

jobs:

  annotate-pr:
    runs-on: ubuntu-latest
    name: Annotates pull request with metadata
    steps:
      - name: Annotate PR
        uses: link-/PR-metadata-action@main
        with:
          owner: ${{ github.repository_owner }}
          repo: ${{ github.event.repository.name }}
          pr_number: ${{ github.event.number }}
          token: ${{ secrets.GITHUB_TOKEN }}
```

Lorsque vous avez terminé toutes ces étapes, notre dépôt devrait ressembler à ceci :

![build-your-first-github-final_repo](https://www.freecodecamp.org/news/content/images/2022/01/build-your-first-github-final_repo.png)

Pour tester ce workflow, nous devons apporter une modification à notre dépôt et créer une Pull Request (PR). Nous pouvons le faire en éditant directement le fichier `README.md` sur GitHub :

![build-your-first-github_demo](https://www.freecodecamp.org/news/content/images/2022/01/build-your-first-github_demo.gif)

## Bonnes pratiques pour GitHub Actions

Enfin, je veux partager avec vous quelques bonnes pratiques lors de la création d'Actions personnalisées :

- Adoptez le principe de responsabilité unique. Assurez-vous que vos actions **font une seule chose**. Cela rendra votre code plus facile à maintenir et à tester.

- Réfléchissez bien à l'interface de votre action (entrées et sorties). **Gardez vos interfaces simples et claires en réduisant le nombre d'entrées optionnelles.**

- Nous ne l'avons pas fait dans ce tutoriel, mais vous devez **valider les entrées de votre action !** La majorité des problèmes de sécurité pourraient être éliminés en validant les entrées.

- Assurez-vous que votre **action est idempotente**, c'est-à-dire que si vous exécutez l'action plusieurs fois en séquence, le résultat devrait toujours être le même. Dans notre cas, l'action devrait s'exécuter et poster un commentaire et ajouter les labels, ou elle devrait se terminer proprement.

- Lisez et **suivez les meilleures pratiques de durcissement de la sécurité** documentées dans [ces GitHub Docs](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions).

- Ne créez pas une nouvelle action si vous n'êtes pas en mesure de la maintenir. **Recherchez des actions similaires dans le marketplace et utilisez-les à la place.**


## Conclusion

Pour ce tutoriel, nous avons créé une action personnalisée qui commente un résumé des changements dans une Pull Request et ajoute des labels pour les types de fichiers qui ont été modifiés.

Vous devriez être en mesure de réutiliser ces étapes pour créer des actions plus complexes qui peuvent faire beaucoup plus !

Je suis en train de créer un cours DevOps complet utilisant GitHub Actions. Si vous cherchez plus d'informations approfondies sur la façon dont vous pouvez utiliser les Actions pour l'Intégration Continue, la Livraison Continue, ou gitOps (parmi de nombreux autres sujets), gardez un œil sur ces vidéos :

%[https://youtu.be/Ftq1yFwPJQ4]

Bon codage !