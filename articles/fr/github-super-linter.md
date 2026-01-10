---
title: Comment utiliser GitHub Super Linter dans vos projets
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-08-30T15:25:35.000Z'
originalURL: https://freecodecamp.org/news/github-super-linter
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/FCC-1.png
tags:
- name: clean code
  slug: clean-code
- name: eslint
  slug: eslint
- name: GitHub
  slug: github
- name: GitHub Actions
  slug: github-actions
seo_title: Comment utiliser GitHub Super Linter dans vos projets
seo_desc: "By Rishit Dagli\nWhen you're starting a new project, you might have to\
  \ add multiple linting tools to beautify your code and prevent simple errors. \n\
  You will often use multiple linters – one of them might support an npm installation\
  \ and other one might..."
---

Par Rishit Dagli

Lorsque vous commencez un nouveau projet, vous devrez peut-être ajouter plusieurs outils de linting pour embellir votre code et prévenir les erreurs simples. 

Vous utiliserez souvent plusieurs linters – l'un d'eux pourrait supporter une installation npm et un autre pourrait avoir une installation PyPI, et ainsi de suite. Vous voudrez également configurer une certaine automatisation dans votre CI pour exécuter ces linters, mais ce processus est assez fastidieux 😫.

Dans cet article, je vais vous montrer comment utiliser GitHub Super Linter, un seul linter pour résoudre tous ces problèmes. La plupart de mes projets personnels utilisent également GitHub Super Linter, et j'ai personnellement trouvé que c'était un énorme sauveur.

## Pourquoi le Linting est-il nécessaire ?

Le linting est essentiellement une forme d'analyse statique de code. Il analyse le code que vous avez écrit contre certaines règles pour des erreurs stylistiques ou programmatiques. Pensez-y comme un outil qui signale les utilisations suspectes dans un logiciel.

Un linter peut vous aider à gagner beaucoup de temps en :

* Empêchant le code cassé d'être poussé
* Aidant à établir les meilleures pratiques de codage
* Construisant des directives pour la mise en page et le format du code
* Rendant les revues de code beaucoup plus fluides
* Signalant les bugs dans votre code à partir d'erreurs de syntaxe

Étant donné la nature utile des outils de linting, vous voudriez idéalement exécuter un linter avant toute revue de code sur chaque morceau de code qui est poussé dans votre dépôt. Cela vous aide définitivement à écrire un meilleur code, plus lisible et plus stable.

Voici un exemple d'utilisation de [Black](https://github.com/psf/black), un outil de linting pour Python axé sur la mise en forme du code.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Black-Example.png)
_Modifications de formatage apportées par Black_

GitHub Super Linter peut vous aider beaucoup à apporter ces capacités à vos projets facilement et efficacement. GitHub Super Linter est une combinaison de plusieurs linters couramment utilisés que vous pouvez utiliser très facilement. Il vous permet de configurer des exécutions automatisées pour ces linters, ainsi que de gérer plusieurs linters dans un seul projet !

Il existe également une tonne de capacités de personnalisation avec des variables d'environnement qui peuvent vous aider à personnaliser le Super Linter pour votre dépôt individuel.

## Comment utiliser GitHub Super Linter dans GitHub Actions

Super Linter est principalement conçu pour être exécuté dans une GitHub Action, ce qui est également la façon dont je l'ai utilisé depuis assez longtemps. Nous allons en parler en premier. Pour suivre, vous devriez créer une nouvelle GitHub Action dans votre dépôt. Créons un nouveau fichier à `.github/workflows/linter.yml`.

Par la suite, je supposerai que vous connaissez la syntaxe de base pour les GitHub Actions. Mais au cas où vous ne la connaîtriez pas ou auriez besoin d'un rapide rappel, je vous suggère de consulter ce [Guide de démarrage rapide](https://docs.github.com/en/actions/quickstart).

### Comment créer une Action

Nous avons déjà un fichier vide `.github/workflows/linter.yml`, que nous allons maintenant remplir avec une action que vous pouvez utiliser pour lint votre projet.

Nous allons commencer par donner un nom à notre action. C'est ce qui apparaît sous le Statut de Vérification de GitHub Action :

```yaml
name: Lint Code Base
```

Ensuite, spécifions les déclencheurs pour notre action. Cela répond à la question de savoir quand vous devez lint votre base de code. Ici, nous lui disons de lancer le lint à chaque push et à chaque pull request.

```yaml
name: Lint Code Base

on: [push, pull_request]
```

C'est une autre configuration très couramment utilisée pour les déclencheurs. Cela ne s'exécute que lorsque vous faites une pull request vers les branches `main` ou `master` et non lors des push vers ces branches.

```yaml
on:
  push:
    branches-ignore: [master, main]
  pull_request:
    branches: [master, main]
```

Ensuite, nous voulons configurer un job. Tous les composants que vous mettez dans un seul job s'exécuteront séquentiellement. Ici, pensez-y comme les étapes et dans quel ordre nous voulons qu'elles s'exécutent chaque fois que le déclencheur est satisfait. 

Nous nommerons ce job "Lint Code Base" et demanderons à GitHub d'exécuter notre job sur un runner avec la dernière version d'Ubuntu supportée par GitHub.

```yaml
name: Lint Code Base

on: [push, pull_request]

jobs:
  build:
    name: Lint Code Base
    runs-on: ubuntu-latest
```

Vous n'êtes pas limité à utiliser un seul type de runner (ubuntu-latest), comme nous le faisons ici. Il est courant d'avoir une matrice de types d'agents, mais dans ce cas, cela s'exécutera de la même manière sur tous les types de runners. Vous utilisez souvent une matrice de runners pour tester que votre code fonctionne bien sur tous les types de plateformes. 

GitHub Super Linter ne fonctionne pas différemment sur d'autres types de machines, donc nous utilisons simplement un seul type de machine.

Ensuite, nous commencerons à définir les étapes que nous voulons que ce workflow ait. Nous avons essentiellement deux étapes :

1. Checkout du code
2. Exécution du super linter

Passons au checkout du code. Pour ce faire, nous utiliserons l'action officielle de checkout de GitHub. 

Nous définirons `fetch-depth: 0` pour récupérer tout l'historique pour toutes les branches et tags, ce qui est nécessaire pour que Super linter obtienne une liste correcte des fichiers modifiés. Si vous ne l'aviez pas fait, un seul commit serait récupéré.  

Nous donnons également un nom à notre étape et lui disons que nous voulons utiliser l'action présente dans le dépôt GitHub à `actions/checkout@v3`.

```yaml
name: Lint Code Base

on: [push, pull_request]

jobs:
  build:
    name: Lint Code Base
    runs-on: ubuntu-latest

    steps:

      - name: Checkout Code
        uses: actions/checkout@v3
        with:
          fetch-depth: 0
```

Ce morceau de code checke votre dépôt sous `$GITHUB_WORKSPACE` ce qui permet au reste du workflow d'accéder à ce dépôt. Le dépôt que nous checkons est celui où réside votre code, idéalement le même dépôt.

### Comment exécuter le Linter

Maintenant, nous allons ajouter l'étape pour exécuter le linter puisque nous avons notre code checkout. Vous pouvez personnaliser GitHub Super Linter en utilisant des variables d'environnement lors de l'exécution de l'action.

```yaml
name: Lint Code Base

on: [push, pull_request]

jobs:
  build:
    name: Lint Code Base
    runs-on: ubuntu-latest

    steps:

      - name: Checkout Code
        uses: actions/checkout@v3
        with:
          fetch-depth: 0
      
      - name: Lint Code Base
        uses: github/super-linter@v4
```

Nous allons maintenant parler des variables d'environnement que vous utiliserez souvent avec GitHub Super Linter ainsi que quelques exemples.

* `VALIDATE_ALL_CODEBASE` : cela décide si Super Linter doit lint l'ensemble de la base de code ou seulement les changements introduits avec ce commit. Ces changements sont découverts en utilisant `git diff`, mais vous pouvez également changer l'algorithme de recherche (mais nous n'aborderons pas cela dans cet article). Exemple : `VALIDATE_ALL_CODEBASE: true`.
* `GITHUB_TOKEN` : Comme le nom le suggère, il s'agit de la valeur du token GitHub. Si vous utilisez cela, GitHub affichera chacun des linters que vous utilisez (nous verrons comment faire cela bientôt) comme des vérifications séparées sur l'interface utilisateur. Exemple : Dans GitHub Actions, vous pouvez utiliser `GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}`.
* `DEFAULT_BRANCH` : Le nom de la branche par défaut du dépôt. Exemple : `DEFAULT_BRANCH: main`.
* `IGNORE_GENERATED_FILES` : Au cas où vous auriez des fichiers qui sont générés par des outils, vous pourriez les marquer comme `@generated`. Si cette variable d'environnement est définie sur true, Super Linter ignore ces fichiers. Exemple : `IGNORE_GENERATED_FILES: true`.
* `IGNORE_GITIGNORED_FILES` : Exclut les fichiers qui sont dans .gitignore du linting. Exemple : `IGNORE_GITIGNORED_FILES: true`.
* `LINTER_RULES_PATH` : Un chemin personnalisé où tous les fichiers de personnalisation des linters doivent être. Par défaut, vos fichiers sont censés être dans `.github/linters/`. Exemple : `LINTER_RULES_PATH: /`.

Ce sont quelques-unes des variables d'environnement que vous utiliserez le plus souvent, mais aucune de celles dont nous avons parlé jusqu'à présent ne traite du linting spécifique à un langage. 

Si vous n'utilisez aucune des variables d'environnement dont nous parlons, Super Linter trouve et utilise automatiquement tous les linters applicables pour votre base de code.

## Comment ajouter des linters spécifiques à Super Linter

Vous serez souvent intéressé à utiliser uniquement des linters spécifiques pour vos projets. Vous pouvez utiliser le modèle de variable d'environnement suivant pour ajouter les linters que vous souhaitez :

```
VALIDATE_{LANGUAGE}_{LINTER}
```

Vous pouvez trouver les conventions de nommage pour celles-ci dans la liste des [Linters supportés](https://github.com/github/super-linter#supported-linters).

Voici quelques exemples, où nous spécifions que nous voulons utiliser Black pour lint tous les fichiers Python, ESLint pour les fichiers JavaScript, et HTMLHint pour les fichiers HTML.

```yaml
name: Lint Code Base

on: [push, pull_request]

jobs:
  build:
    name: Lint Code Base
    runs-on: ubuntu-latest

    steps:

      - name: Checkout Code
        uses: actions/checkout@v3
        with:
          fetch-depth: 0

      - name: Lint Code Base
        uses: github/super-linter@v4
        env:
          VALIDATE_ALL_CODEBASE: true
          VALIDATE_JAVASCRIPT_ES: true
          VALIDATE_PYTHON_BLACK: true
          VALIDATE_HTML: true
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

Une fois que vous définissez l'un des linters sur `true`, tous les autres linters ne s'exécuteront pas. Dans l'extrait ci-dessus, aucun des linters sauf ESLint, Black ou HTMLHint ne s'exécutera.

Cependant, dans cet exemple, nous définissons un seul linter sur `false` pour que tous les linters sauf ESLint s'exécutent ici :

```yaml
name: Lint Code Base

on: [push, pull_request]

jobs:
  build:
    name: Lint Code Base
    runs-on: ubuntu-latest

    steps:

      - name: Checkout Code
        uses: actions/checkout@v3
        with:
          fetch-depth: 0

      - name: Lint Code Base
        uses: github/super-linter@v4
        env:
          VALIDATE_ALL_CODEBASE: true
          VALIDATE_JAVASCRIPT_ES: false
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

## Comment personnaliser les vérifications de lint

Les linters utilisent souvent des fichiers de configuration pour que vous puissiez modifier les règles utilisées par le linter. Dans les deux exemples complets que j'ai montrés ci-dessus, Super Linter essaiera de trouver tous les fichiers de configuration sous `.github/linters/`.

Cela pourrait être votre fichier `.eslintrc.yml` utilisé pour configurer ESLint, `.htmlhintrc` pour configurer HTMLHint, et ainsi de suite.

Voici un exemple de fichier de configuration si vous utilisez le linter Flake8 pour Python :

```
[flake8]
max-line-length = 120
```

Vous enregistrez cela dans `.github/linters/.flake8`. Vous l'utiliserez ensuite lors de l'exécution du linter Flake8. Vous pouvez trouver un exemple de fichiers de configuration modèles que vous pouvez utiliser [ici](https://github.com/github/super-linter/tree/main/TEMPLATES). 

Cependant, voici deux exemples de la façon dont vous pouvez modifier ce chemin :

1. Tous vos fichiers de configuration de linter sont dans un autre répertoire

Ajoutez le chemin du répertoire comme une variable d'environnement comme ceci :

```yaml
LINTER_RULES_PATH: configs/
```

2.   Ajoutez un chemin pour un fichier de configuration

Vous pouvez également coder en dur un chemin pour un linter spécifique comme une variable d'environnement. Voici un exemple :

```yaml
JAVASCRIPT_ES_CONFIG_FILE: configs/linters/.eslintrc.yml
```

## Comment exécuter Super Linter en dehors de GitHub Actions

GitHub Super Linter a été conçu pour être exécuté dans GitHub Actions. Mais l'exécuter localement ou sur d'autres plateformes CI peut être particulièrement utile. Vous exécuterez essentiellement Super Linter comme vous le feriez localement sur toute autre plateforme CI.

### Comment exécuter Super Linter localement

Vous voulez d'abord tirer le dernier conteneur Docker depuis DockerHub avec cette commande :

```shell
docker pull github/super-linter:latest
```

Pour exécuter ce conteneur, vous exécutez ensuite ce qui suit :

```shell
docker run -e RUN_LOCAL=true -e USE_FIND_ALGORITHM=true VALIDATE_PYTHON_BLACK=true -v /project/directory:/tmp/lint github/super-linter
```

Remarquez quelques choses ici :

* Nous l'exécutons avec le flag `RUN_LOCAL` pour contourner certaines des vérifications de GitHub Actions. Cela définit automatiquement `VALIDATE_ALL_CODEBASE` sur true.
* Nous mappons notre base de code locale à `/tmp/lint` pour que le linter puisse récupérer le code.
* La façon dont nous définissons les variables d'environnement est bien sûr différente, mais le processus global d'exécution de GitHub Super Linter reste le même.

### Comment exécuter Super Linter sur d'autres plateformes CI

Exécuter GitHub Super Linter sur d'autres plateformes CI est assez similaire à l'exécuter localement. Voici un exemple de son exécution dans Azure Pipelines par [Tao Yang](https://blog.tyang.org/2020/06/27/use-github-super-linter-in-azure-pipelines/).

```yaml
- job: lint_tests
  displayName: Lint Tests
  pool:
    vmImage: ubuntu-latest
  steps:
  - script: |
      docker pull github/super-linter:latest
      docker run -e RUN_LOCAL=true -v $(System.DefaultWorkingDirectory):/tmp/lint github/super-linter
    displayName: 'Code Scan using GitHub Super-Linter'
```

Cela exécute simplement les commandes que nous aurions pour exécuter le Super Linter localement en tant que script. Vous pourriez l'exécuter de la même manière exacte sur d'autres plateformes CI.

## **Conclusion**

Merci de m'avoir suivi jusqu'à la fin. J'espère que vous avez appris une ou deux choses sur le linting et l'utilisation de GitHub Super Linter. Cela a certainement été l'un de mes projets open source préférés.

Si vous avez appris quelque chose de nouveau ou apprécié la lecture de cet article, veuillez le partager pour que d'autres puissent le voir. En attendant, à la prochaine publication !

Vous pouvez également me trouver sur Twitter [@rishit_dagli](https://twitter.com/rishit_dagli), où je tweete sur l'open source et l'apprentissage automatique.