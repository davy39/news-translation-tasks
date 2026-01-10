---
title: Comment mettre à jour les dépendances de manière sûre et automatique avec GitHub
  Actions et Renovate
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-05T17:18:02.000Z'
originalURL: https://freecodecamp.org/news/update-dependencies-automatically-with-github-actions-and-renovate
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/github_actions_and_renovate_logos-1.png
tags:
- name: automation
  slug: automation
- name: Continuous Integration
  slug: continuous-integration
- name: GitHub
  slug: github
- name: GitHub Actions
  slug: github-actions
seo_title: Comment mettre à jour les dépendances de manière sûre et automatique avec
  GitHub Actions et Renovate
seo_desc: 'By Ramón Morcillo

  In Software Development keeping up to date with technology updates is crucial. This
  is true both for developers as they learn and renew their skills, and also for the
  projects they work on and maintain.

  When you start a project, you...'
---

Par Ramón Morcillo

Dans le développement logiciel, **rester à jour face aux évolutions technologiques** est crucial. C'est vrai tant pour les développeurs qui apprennent et renouvellent leurs compétences, que pour les projets sur lesquels ils travaillent et qu'ils maintiennent.

Lorsque vous commencez un projet, vous le configurez normalement avec les dernières versions stables de toutes les bibliothèques et tous les outils.

Puis le temps passe, le projet grandit, et de nouvelles fonctionnalités et bibliothèques sont ajoutées. Mais **les versions des bibliothèques et des packages restent les mêmes, l'équipe ne les mettant jamais à jour**.

Après tout, pourquoi les mettre à jour si le projet fonctionne parfaitement avec les versions actuelles ?

![Tout va bien](https://www.freecodecamp.org/news/content/images/2020/11/this-is-fine-1.jpg)

## Pourquoi vous devriez maintenir vos projets à jour

Voici quelques raisons pour lesquelles vous devriez garder vos dépendances à jour :
 - Résoudre les problèmes des anciennes versions.
 - Ajouter des correctifs de vulnérabilité.
 - Augmenter les performances globales.
 - Ajouter de nouvelles fonctionnalités.
 - ...
 
Lorsque vous gardez vos dépendances à jour, vous résolvez les problèmes des versions antérieures et améliorez les performances grâce à de nouvelles optimisations. Vous pouvez également utiliser les nouvelles fonctionnalités ajoutées par d'autres développeurs.

Toutes ces améliorations contribuent à la *maintenabilité du code* et à la santé globale du projet.

Nous avons tous travaillé sur des projets où les dépendances n'ont jamais (ou rarement) été mises à jour. Et ce n'est pas une partie de plaisir.

Alors, comment garder nos projets à jour ?

Tout d'abord, vous pouvez exécuter `npm outdated` pour [voir les dernières versions](https://docs.npmjs.com/cli/outdated) des packages que vous utilisez actuellement.

Vous pouvez ensuite exécuter `npm update` pour les mettre à jour (cela ne les mettra pas à jour vers les versions majeures). Mais comment savoir quelles mises à jour casseront le projet et lesquelles ne le feront pas ?

Ensuite, vous devez réfléchir au moment où vous devriez tout mettre à jour. Quand vérifier les mises à jour – chaque jour ? chaque semaine ? ...chaque mois ?

## Ce que vous apprendrez dans ce tutoriel

C'est pourquoi j'ai réalisé ce projet : pour découvrir GitHub Actions et l'utiliser afin d'avoir un **moyen sûr de mettre à jour automatiquement les dépendances sans faire échouer le projet**.

Dans ce tutoriel, vous apprendrez à utiliser l'[application Renovate](https://github.com/renovatebot/renovate) pour vérifier les mises à jour des dépendances, puis soumettre des Pull Requests pour les mettre à jour. Cela vous permet de vous *abstraire* de la vérification des mises à jour, afin de vous concentrer sur des choses plus importantes.

L'intérêt d'utiliser [GitHub Actions](https://github.com/features/actions) est de mettre en place un workflow et de le déclencher à chaque Pull Request. Il vérifiera que le build et les tests réussissent avec les dépendances mises à jour avant de les ajouter au projet.

## Table des matières

- [Pour commencer](#pour-commencer)
- [Configurer le workflow GitHub Actions](#configurer-le-workflow-github-actions)
- [Ajouter Renovate](#ajouter-renovate)
- [Conclusion](#conclusion)
- [Ressources utiles](#ressources-utiles)

## Pour commencer

Bien que **cette approche puisse être appliquée à n'importe quel projet**, nous utiliserons un projet [React](https://reactjs.org) créé avec [Create React App](https://github.com/facebook/create-react-app). Cela nous donnera un projet de base avec tout ce qu'il faut pour travailler.

Au fait, si vous n'avez pas Node.js installé, voici le [lien](https://nodejs.org/en/download/) pour le faire.

Si vous voulez voir le résultat final avant de commencer, [le voici](https://github.com/reymon359/github-actions-and-renovate).

Commençons donc par exécuter :

```bash
npx create-react-app my-app
cd my-app
npm start
```

Si vous utilisez npm 5.1 ou une version antérieure, vous ne pouvez pas utiliser `npx`. À la place, installez `create-react-app` globalement :

```bash
npm install -g create-react-app
```

Puis exécutez :

```bash
create-react-app my-app
```

## Configurer le workflow GitHub Actions

Nous allons maintenant procéder à la définition d'un workflow GitHub Actions dans notre repository pour automatiser le processus.

*[GitHub Actions](https://github.com/features/actions) est une fonctionnalité de GitHub qui vous aide à automatiser vos workflows de développement logiciel. Elle peut tout gérer, des tâches simples aux capacités d'intégration continue (CI) et de déploiement continu (CD) personnalisées de bout en bout dans vos repositories.*

Dans notre dossier racine, nous allons créer un nouveau dossier nommé `.github`. À l'intérieur de celui-ci, nous créerons un dossier `workflows`. Voici à quoi devrait ressembler votre projet après ces étapes :

```
📂 my-app
├── 📂 .github
│   └── 📂 workflows
├── ...
...
```

C'est ici que nous allons créer et ajouter nos workflows. Les workflows GitHub Actions sont les processus automatisés d'intégration continue que nous voulons exécuter dans notre projet.

Les workflows sont composés de jobs qui contiennent un ensemble d'étapes (steps). Pour les expliquer plus clairement, créons notre propre workflow et parcourons-le étape par étape.

Dans le répertoire `.github/workflows`, ajoutez un fichier `.yml` ou `.yaml` et nommez-le `main.yml`. J'ai choisi ce nom pour rester simple, mais vous pouvez lui donner n'importe quel autre nom comme `build-test.yml` ou `continuous-integration-workflow.yml`.

```text
📂 my-app
├── 📂 .github
│   └── 📂 workflows
│       └── 📄 main.yml
├── ...
...
```

[Voici](https://gist.github.com/reymon359/514cf378456457f1798293fe0ed99f3a) à quoi ressemblera le workflow à la fin, au cas où vous voudriez simplement le copier et l'ajouter directement avant l'explication.

```yml
name: Build and Test

on:
  push:
    branches: [master]
  pull_request:
    branches: [master]

jobs:
  build_and_test:
    runs-on: ubuntu-latest

    strategy:
      matrix:
        node: [10, 12]

    steps:
      - name: Checkout
        uses: actions/checkout@v2
      - name: Use Node.js ${{ matrix.node-version }}
        uses: actions/setup-node@v1
        with:
          node-version: ${{ matrix.node-version }}
      - name: Install project
        run: npm install
      - name: Build the project
        run: npm run build --if-present
      - name: Run tests
        run: npm test
```

Le premier paramètre de notre workflow sera son **nom** (`name`).

```yml
name: Build and Test
```

Le deuxième paramètre est le **déclencheur** (`on`).

Nous pouvons choisir si le workflow est **déclenché par un événement comme un push ou une pull request sur une branche spécifique**, ou nous pouvons même planifier un [cron](https://en.wikipedia.org/wiki/Cron) pour le **déclencher automatiquement à chaque intervalle de temps défini !**

Dans notre projet, nous voudrons le déclencher lors d'un push sur la branche master, et lorsque l'application Renovate soumet une Pull Request pour mettre à jour une dépendance :

```yml
on:
  push:
    branches: [master]
  pull_request:
    branches: [master]
```

Ensuite, nous définissons les **jobs**.
 
Dans cet exemple, il n'y aura qu'un seul job : **build and test** le projet, et nous choisissons la machine virtuelle où le job sera exécuté.

```yml
jobs:
  build_and_test:
    runs-on: ubuntu-latest
```

Vient ensuite la **matrix** où nous allons configurer la combinaison de versions et de systèmes sur lesquels nous voulons exécuter notre workflow. Dans notre cas, nous l'exécuterons sur Node.js 10 et 12.

```yml
    strategy:
      matrix:
        node-version: [10, 12]
```

Enfin, les étapes (**steps**) du workflow. La première est l'[action checkout](https://github.com/actions/checkout) qui est une action standard que vous devez inclure dans votre workflow lorsque vous avez besoin d'une copie de votre repository pour exécuter le workflow.

Ensuite, vous pouvez exécuter d'autres actions et processus. Dans notre application, nous utiliserons l'action **setup-node** avec la matrix que nous avons définie précédemment. Ensuite, nous ajouterons des étapes pour installer le projet, le builder et exécuter les tests.

```yml
    steps:
      - name: Checkout
        uses: actions/checkout@v2
      - name: Use Node.js ${{ matrix.node-version }}
        uses: actions/setup-node@v1
        with:
          node-version: ${{ matrix.node-version }}
      - name: Install project
        run: npm install
      - name: Build the project
        run: npm run build --if-present
      - name: Run tests
        run: npm test
```

Maintenant, créez un repository GitHub pour le projet, commitez les modifications locales effectuées et pushez-les.

Petite astuce : si vous voulez le créer plus rapidement, allez sur [repo.new](https://repo.new) ou [github.new](https://github.new). Vous pouvez aussi utiliser [gist.new](https://gist.new) pour les gists !

Une fois que vous aurez poussé vos modifications, le workflow s'exécutera. Vous pourrez alors voir comment cela s'est passé dans l'onglet `Actions` [de votre projet GitHub](https://github.com/reymon359/github-actions-and-renovate/actions).

![Workflow GitHub Actions](https://www.freecodecamp.org/news/content/images/2020/11/github_actions_workflows.png)

## Ajouter Renovate

[Renovate](https://github.com/marketplace/renovate) est une application gratuite, open-source et personnalisable qui vous aide à mettre à jour automatiquement vos dépendances dans vos projets logiciels en recevant des pull requests.

Elle est utilisée par des entreprises de logiciels comme Google, Mozilla et Uber, et vous pouvez l'utiliser sur GitHub, GitLab, Bitbucket, Azure DevOps et Gitea.

Nous allons ajouter un bot qui soumettra des pull requests à notre repository lorsqu'il y aura des mises à jour dans les dépendances de notre projet.

Ce qui est génial, et c'est tout l'intérêt de notre projet, c'est que nous avons précédemment défini dans notre workflow d'exécuter les tests avec les pull requests. Ainsi, lorsque Renovate en soumet une, **nous vérifierons automatiquement si les mises à jour proposées cassent le projet ou non avant de les merger dans la branche master**.

![Enfant levant le pouce](https://www.freecodecamp.org/news/content/images/2020/11/thumbs_up_kid.gif)

Pour ajouter Renovate à notre projet, nous devons installer [son application](https://github.com/apps/renovate) dans le repository du projet.

Faites attention lors de la sélection du repository auquel vous souhaitez ajouter Renovate et choisissez celui créé précédemment. Si vous avez fait une erreur et que vous souhaitez le reconfigurer, vous pouvez le faire dans l'[onglet Applications des paramètres personnels](https://github.com/settings/installations) de votre compte.

Après quelques minutes, vous devrez accepter et merger la Pull Request d'onboarding que vous recevrez.

Une fois intégrée, vous devez la configurer en mettant à jour le fichier `renovate.json` à la racine du projet. N'oubliez pas de puller les modifications après avoir mergé la Pull Request pour qu'il apparaisse.

Vous pouvez utiliser la configuration par défaut où Renovate soumettra les pull requests dès qu'il trouvera des mises à jour et attendra que vous les mergiez :

```json
{
  "extends": ["config:base"]
}
```

Ou vous pouvez l'adapter aux exigences de votre projet comme [celle utilisée par Renovate lui-même](https://github.com/renovatebot/renovate/blob/master/renovate.json).

Pour éviter tout problème et en apprendre un peu plus sur l'outil, nous utiliserons une configuration avec certaines de ses fonctionnalités les plus utiles.

Si vous voulez en savoir plus sur sa configuration, voici la [documentation](https://docs.renovatebot.com/).

[Ceci](https://gist.github.com/reymon359/4c4417522cd0922cfbc63ad75ca2c945) sera notre fichier `renovate.json`. Jetez-y un œil, et je l'expliquerai après.

```json
{
  "extends": [
    "config:base"
  ],
  "packageRules": [
    {
      "updateTypes": [
        "minor",
        "patch"
      ],
      "automerge": true
    }
  ],
  "timezone": "Europe/Madrid",
  "schedule": [
    "after 10pm every weekday",
    "before 5am every weekday",
    "every weekend"
  ]
}
```

Dans la première partie, nous indiquons à Renovate que notre configuration sera une extension de celle par défaut.
```json
{
  "extends": [
    "config:base"
  ],
```

Ensuite, nous avons les `packageRules`. Après quelques mois d'utilisation, j'ai réalisé que vérifier les pull requests (de temps en temps) et les accepter si les tests réussissaient était une perte de temps considérable.

C'est pourquoi l'`automerge` est défini sur true, afin que Renovate fusionne automatiquement la pull request si le workflow s'est déroulé avec succès.

Pour restreindre un peu la liberté de Renovate, nous définissons qu'il ne peut effectuer l'`automerge` que lorsqu'il s'agit d'une mise à jour `minor` (mineure) ou `patch`.

De cette façon, s'il s'agit d'une mise à jour `major` (majeure) ou d'un autre type, c'est nous qui vérifierons si cette mise à jour doit être ajoutée ou non.

[Ici](https://docs.renovatebot.com/configuration-options/#updatetypes), vous trouverez plus d'informations sur les types de mises à jour disponibles.

```json
  "packageRules": [
    {
      "updateTypes": [
        "minor",
        "patch"
      ],
      "automerge": true
    }
  ],
```

Enfin, nous avons la planification horaire. Si vous travaillez seul ou en équipe à certaines heures, il est agréable que les mises à jour soient effectuées lorsque vous ne travaillez pas pour éviter les distractions inutiles.

Nous sélectionnons notre fuseau horaire et y ajoutons un [planning](https://docs.renovatebot.com/presets-schedule/) personnalisé. Vous pouvez trouver les noms de fuseaux horaires valides [ici](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

```json
  "timezone": "Europe/Madrid",
  "schedule": [
    "after 10pm every weekday",
    "before 5am every weekday",
    "every weekend"
  ],
```

Quoi qu'il en soit, si vous ne vous souciez pas de l'heure à laquelle les pull requests seront soumises, ou si les personnes qui contribuent au code se trouvent dans des fuseaux horaires différents, vous pouvez supprimer cette partie.

Une fois la configuration mise à jour, nous poussons les modifications sur GitHub pour que l'application Renovate s'adapte à la nouvelle configuration.

Vous avez enfin les dépendances du projet à jour en toute sécurité sans avoir à les vérifier. [Voici le projet résultant](https://github.com/reymon359/github-actions-and-renovate) après avoir suivi toutes les étapes mentionnées ci-dessus.

N'oubliez pas que si vous avez ajouté la partie planification horaire, la pull request ne sera pas mergée automatiquement tant qu'elle ne respectera pas cette configuration.

## Conclusion

Il existe d'autres moyens de maintenir les dépendances à jour de manière automatisée. Mais si vous utilisez GitHub pour héberger votre code, vous devriez en profiter et tirer le meilleur parti de ses formidables fonctionnalités gratuites.

Si vous vous demandez ce que vous pouvez faire d'autre et automatiser avec les applications et actions GitHub, jetez un œil à sa [Marketplace](https://github.com/marketplace).

De plus, vous pouvez regarder [un projet que j'ai réalisé](https://github.com/reymon359/up-to-date-react-template) et sur lequel je travaille de temps en temps. Il a servi de base à ce tutoriel. Il est un peu plus complexe et possède plus de fonctionnalités que celui de ce tutoriel.

J'espère que vous avez apprécié cet article et que vous avez découvert GitHub Actions et ses applications. Si vous avez des questions, des suggestions ou des commentaires en général, n'hésitez pas à me contacter sur l'un des réseaux sociaux de [mon site](https://ramonmorcillo.com) ou <a ref="mailto:hey@ramonmorcillo.com">par mail</a>.

## Ressources utiles

Voici une collection de liens et de ressources qui, selon moi, peuvent être utiles pour s'améliorer et en apprendre davantage sur GitHub Actions et ses applications.

- [Projet du tutoriel](https://github.com/reymon359/github-actions-and-renovate). - Le projet résultant de ce tutoriel.
- [GitHub Marketplace](https://github.com/marketplace). - L'endroit pour trouver toutes les GitHub Actions et Apps.
- [Configuration du workflow GitHub Actions](https://help.github.com/en/actions/configuring-and-managing-workflows/configuring-a-workflow) - La documentation complète sur la configuration d'un workflow sur GitHub Actions.
- [Application GitHub Renovate](https://github.com/marketplace/renovate) - La page principale de l'application Renovate sur la GitHub Marketplace.
- [Workflow du projet GitHub Actions](https://gist.github.com/reymon359/514cf378456457f1798293fe0ed99f3a). - Le workflow utilisé dans ce tutoriel.
- [Fichier de configuration de l'application Renovate](https://gist.github.com/reymon359/4c4417522cd0922cfbc63ad75ca2c945). - Le fichier de configuration personnalisé de l'application Renovate du tutoriel.
- [Up to Date React Template](https://github.com/reymon359/up-to-date-react-template). - Un projet personnel qui utilise l'approche décrite dans ce tutoriel.