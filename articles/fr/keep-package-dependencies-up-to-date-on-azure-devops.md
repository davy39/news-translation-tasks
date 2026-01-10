---
title: Comment maintenir vos dépendances de packages à jour sur Azure DevOps
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-18T20:15:51.000Z'
originalURL: https://freecodecamp.org/news/keep-package-dependencies-up-to-date-on-azure-devops
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/photo-1587620962725-abab7fe55159-1.png
tags:
- name: Azure
  slug: azure
- name: dependency management
  slug: dependency-management
- name: Devops
  slug: devops
seo_title: Comment maintenir vos dépendances de packages à jour sur Azure DevOps
seo_desc: 'By Apoorv Tyagi

  As a developer, how often have you seen a repository with packages that are out
  of date?

  New package updates generally include new features, performance improvements, and
  security fixes. But keeping track of all outdated dependencies ...'
---

Par Apoorv Tyagi

En tant que développeur, combien de fois avez-vous vu un dépôt avec des packages obsolètes ?

Les nouvelles mises à jour de packages incluent généralement de nouvelles fonctionnalités, des améliorations de performance et des correctifs de sécurité. Mais suivre toutes les dépendances obsolètes dans votre projet peut être vraiment ennuyeux et prendre beaucoup de temps, surtout si vous en avez beaucoup.

Pour faire ce genre de ménage, j'ai essayé [Dependabot](https://github.blog/2020-06-01-keep-all-your-packages-up-to-date-with-dependabot/).

## Comment fonctionne Dependabot

Dependabot parcourt les fichiers de dépendances de votre projet. Par exemple, il recherche dans vos fichiers `package.json` ou `pom.xml` et inspecte les dépendances obsolètes ou non sécurisées. S'il en trouve, il ouvre des pull requests individuelles pour mettre à jour chacune d'entre elles.

Cet outil est nativement intégré avec GitHub. Mais récemment, j'ai dû résoudre ce problème de mise à jour des dépendances pour un projet fonctionnant sur Azure DevOps. J'ai donc décidé de trouver une solution pour intégrer Dependabot avec Azure Pipelines. Dans cet article de blog, je vais partager ma solution.

Si vous allez sur [Azure DevOps Extension Marketplace](https://marketplace.visualstudio.com/azuredevops) et que vous recherchez "Dependabot", vous trouverez une [extension](https://marketplace.visualstudio.com/items?itemName=tingle-software.dependabot) de Tingle Software. En utilisant cette extension, nous pouvons facilement intégrer Dependabot avec nos dépôts dans Azure DevOps.

Vous pouvez vérifier si vous avez cette extension dans vos "Paramètres d'organisation" dans Azure DevOps. Si ce n'est pas le cas, assurez-vous de l'avoir installée avant de continuer.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/1-2.png)
_Extensions installées - Azure DevOps_

## Comment créer le pipeline Azure

Commençons maintenant par créer un nouveau fichier `YAML` pour votre pipeline Azure :

```
trigger: none

stages:
  - stage: CheckDependencies
    displayName: 'Vérifier les dépendances'
    jobs:
      - job: Dependabot
        displayName: 'Exécuter Dependabot'
        pool:
          vmImage: 'ubuntu-latest'
        steps:
          - task: dependabot@1
            displayName: 'Exécuter Dependabot'
            inputs:
              packageManager: 'npm'
              targetBranch: 'develop'
              openPullRequestsLimit: 10
 ```

Dans les paramètres de la tâche, j'ai spécifié trois paramètres :

1. **packageManager** : Il spécifie le type de packages à vérifier pour les mises à jour de dépendances. Exemples : `nuget`, `maven`, `gradle`, `npm`, etc.
2. **targetBranch** : Il s'agit d'un paramètre facultatif qui définit la branche à cibler lors de la création de pull requests. Si ce n'est pas spécifié, Dependabot choisira la branche `default` du dépôt. 
3. **openPullRequestsLimit** : Il s'agit à nouveau d'un paramètre facultatif qui spécifie le nombre maximum de pull requests ouvertes à avoir à un moment donné. Par défaut, il ouvre 5 pull requests à la fois.

Vous pouvez consulter tous les [Paramètres de tâche](https://github.com/tinglesoftware/dependabot-azure-devops/blob/main/src/extension/README.md#task-parameters) que l'extension prend en charge pour ajuster votre implémentation. Maintenant, il vous suffit de configurer ce fichier YAML avec un nouveau pipeline Azure et vous êtes prêt à l'exécuter.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/3-2.png)
_Configuration du pipeline - Azure DevOps_

L'étape suivante consiste à donner à votre dépôt l'accès au `Project Collection Build Service` afin que Dependabot puisse créer la pull request vers les dépôts de votre projet.

Pour cela, allez dans les paramètres de votre projet. Ici, vous cliquez sur les dépôts et recherchez le dépôt où vous avez intégré le pipeline.

Après avoir sélectionné celui-ci, cliquez sur l'onglet sécurité et recherchez **project collection build service**. Vous devez lui accorder les accès suivants :

* Contribuer
* Contribuer aux pull requests
* Créer une branche
* Créer une balise
* Forcer le push

![Image](https://www.freecodecamp.org/news/content/images/2022/01/2-1.png)
_Accès pour créer une PR dans le dépôt_

Avec cela, vous êtes complètement prêt à exécuter le pipeline. Une fois que vous l'aurez fait, vous commencerez à recevoir des pull requests dans votre dépôt avec les packages mis à jour.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/5-3.png)
_PR créée par Dependabot_

## Comment planifier le pipeline

Jusqu'à présent, vous avez dû déclencher manuellement le pipeline pour qu'il s'exécute. Pour qu'il s'exécute automatiquement, vous pouvez configurer des planifications pour vos pipelines. Cela déclenchera votre pipeline pour qu'il commence en fonction d'une planification.

Utilisez la syntaxe suivante et ajoutez-la tout en haut de votre fichier `YAML` :

```
schedules:
- cron: string
  displayName: string
  branches:
    include: [ string ]
  always: boolean
  ```

Le paramètre `include` des branches spécifie quelles branches la planification s'applique.

Le paramètre `always` spécifie s'il faut "toujours" exécuter le pipeline ou seulement s'il y a eu des changements de code source depuis la dernière exécution planifiée réussie. La valeur par défaut est false. 

Pour ce cas, vous définissez sa valeur à **true** car les mises à jour de Dependabot sont indépendantes de tout changement de code.

Le fuseau horaire pour les planifications cron est UTC et la syntaxe cron est la suivante :

```
mm HH DD MM DW
 \  \  \  \  \__ Jours de la semaine
  \  \  \  \____ Mois
   \  \  \______ Jours
    \  \________ Heures
     \__________ Minutes
```     

Donc, si vous voulez exécuter votre pipeline chaque semaine le dimanche à 12h UTC, vous devrez écrire - `cron: "0 12 * * 0"` (mettez à jour le cron pour répondre à vos besoins).

Voici à quoi votre fichier `YAML` final devrait ressembler après avoir ajouté une planification :

```
schedules:
  - cron: "0 12 * * 0"
    displayName: Mises à jour hebdomadaires des dépendances
    branches:
      include:
      - develop
    always: true
    
trigger: none

stages:
  - stage: CheckDependencies
    displayName: 'Vérifier les dépendances'
    jobs:
      - job: Dependabot
        displayName: 'Exécuter Dependabot'
        pool:
          vmImage: 'ubuntu-latest'
        steps:
          - task: dependabot@1
            displayName: 'Exécuter Dependabot'
            inputs:
              packageManager: 'npm'
              targetBranch: 'develop'
              openPullRequestsLimit: 10
 ```

Ce pipeline fait ce qui suit pour vous :

Il s'exécute sur une base hebdomadaire (dimanche 12h UTC dans ce cas) et recherche toute dépendance obsolète ou non sécurisée. S'il en trouve, il ouvre des pull requests pour mettre à jour chacune d'entre elles individuellement.

Espérons que cela vous aidera à maintenir vos dépendances de projet à jour dans Azure DevOps !

## Conclusion

Avec cela, nous arrivons à la fin de l'article. Mes DM sont toujours ouverts si vous souhaitez discuter davantage de tout sujet technique ou si vous avez des questions, des suggestions ou des commentaires en général :

* [Twitter](https://twitter.com/apoorv__tyagi)
* [LinkedIn](https://www.linkedin.com/in/apoorvtyagi/)
* [GitHub](https://github.com/apoorvtyagi)
* [Blog](https://apoorvtyagi.tech/)

Bon apprentissage ! 📛 😄