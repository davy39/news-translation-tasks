---
title: Comment utiliser les GitHub Actions pour appeler des webhooks et dominer Internet
  depuis vos PR
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-10T20:54:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-github-actions-to-call-webhooks
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/spring-2019-20.jpg
tags:
- name: GitHub
  slug: github
- name: GitHub Actions
  slug: github-actions
- name: Productivity
  slug: productivity
seo_title: Comment utiliser les GitHub Actions pour appeler des webhooks et dominer
  Internet depuis vos PR
seo_desc: "By Amber Wilkie\nGithub Actions are a new feature from everyone's favorite\
  \ code tool. While they take a little getting used to, they are very powerful tools\
  \ for CI (continuous integration) and other checks on your pull requests. \nHere,\
  \ I'll talk about..."
---

Par Amber Wilkie

Les GitHub Actions sont une nouvelle fonctionnalité de l'outil de code préféré de tous. Bien qu'elles nécessitent un peu d'habitude, ce sont des outils très puissants pour l'IC (intégration continue) et d'autres vérifications sur vos pull requests. 

Ici, je vais parler de l'utilisation des GitHub Actions pour appeler des webhooks. Et comme vous le savez, une fois que vous pouvez appeler un webhook, Internet est votre huître.


## Pourquoi pas les anciens webhooks ?

Maintenant, vous pourriez dire : "GitHub a déjà des webhooks, pourquoi s'embêter avec les actions ?" La réponse est simple : le _contrôle de version_. 

Si vous travaillez avec d'autres personnes sur votre base de code, vous voulez pouvoir suivre comment les changements de configuration ont eu lieu et qui en est responsable. 

Avec les paramètres de base de GitHub, vous ne savez pas ces choses - quelqu'un configure un webhook. Peut-être qu'il échoue un jour, alors quoi ? 

Avec les GitHub Actions, vous n'avez pas à quitter votre éditeur de texte pour voir ce qui se passe lorsque vous poussez votre code.

L'autre raison est qu'il existe un monde de choses que vous pouvez faire depuis les GitHub Actions, et quelques idées sont ci-dessous. J'avais besoin de webhooks pour un projet récent, mais il existe des fonctionnalités pour exécuter des tests, collecter la couverture de code, linting, et plus encore. 

Étant donné que tant d'entre nous utilisent GitHub tous les jours, il ne peut pas faire de mal de se familiariser avec cet nouvel outil.

# Votre première action

Alors, commençons. La première chose que vous devez faire est de créer un dossier `.github > workflows`. À l'intérieur, nous mettrons nos actions. Peu importe comment vous appelez le fichier - GitHub prendra toutes les actions que vous placez dans ce dossier spécial.

Voici le contenu de mon fichier de webhook. J'ai un point de terminaison d'API "Test pedant" qui vérifie les fichiers de ma PR et laisse un commentaire pédant si je n'ai pas écrit de tests.

```yaml
# Ceci est un workflow de base qui est déclenché manuellement
name: Rappel de test

# Contrôle quand l'action sera exécutée. Le workflow s'exécute lorsqu'il est déclenché manuellement via l'UI ou l'API.
on:
  # Déclenche le workflow sur push ou pull request,
  # mais seulement pour la branche main
  pull_request:
    branches: [ main ]

# Une exécution de workflow est composée d'une ou plusieurs tâches qui peuvent s'exécuter séquentiellement ou en parallèle
jobs:
  test_commentary:
    # Le type de runner sur lequel la tâche sera exécutée
    runs-on: ubuntu-latest

    # Les étapes représentent une séquence de tâches qui seront exécutées dans le cadre de la tâche
    steps:
    # Exécute une seule commande en utilisant le shell du runner
    - name: Webhook
      uses: distributhor/workflow-webhook
      with:
        url: "http://amberisgreat.ngrok.io/api/test_pedant"
        json: '{ "repository": "${{github.event.repository.full_name}}", "number": "${{github.event.number}}", "created_at": "${{github.event.pull_request.created_at}}", "updated_at": "${{github.event.pull_request.updated_at}}" }'
```

De haut en bas : 
* D'abord, nous donnons un nom à l'action (`Rappel de test`). 
* Ensuite, nous spécifions quand nous voulons qu'elle s'exécute (`on`). Vous n'avez pas à choisir de branches. Si vous le voulez pour toutes les PR, faites simplement `on: [pull_request]`. GitHub a une longue liste d'[événements qui peuvent déclencher une action](https://docs.github.com/en/actions/reference/events-that-trigger-workflows#webhook-events).
* `jobs` est une liste des tâches. Là où j'ai `test_commentary`, vous mettrez une clé pour votre tâche (cela peut être n'importe quoi). Votre tâche s'exécute probablement sur `ubuntu-latest`, mais vérifiez la tâche elle-même. Une tâche peut avoir plusieurs étapes. La mienne en a une.
* Donnez à votre étape un `name` (cela peut aussi être n'importe quoi)
* `uses` fait référence à l'endroit où le code est stocké. (Vous pouvez écrire vos propres actions si vous le souhaitez !)
* Différentes actions prennent différentes entrées - celle-ci utilise `with` et les clés d'entrée.

J'utilise une [fonction de webhook de "distributhor"](https://github.com/distributhor/workflow-webhook). GitHub n'a pas encore de tâche de webhook officielle, mais ils en auront peut-être au moment où vous lirez ceci. 

Cette action prend au moins une entrée : `url`, le point de terminaison que vous voulez atteindre avec cette action. `json` fait référence aux données que vous allez envoyer.

## La charge utile des GitHub Actions
Ces informations étaient un peu difficiles à trouver dans la documentation des GitHub Actions. 

La charge utile pour une GitHub Action est imbriquée sous `github.event`. Vous devez également savoir quelle action vous poussez les données depuis - car il y a diverses clés disponibles sur `event` selon l'action que vous référencez (listées comme `action` dans la documentation des charges utiles). 

La documentation pertinente se trouve [ici](https://docs.github.com/en/developers/webhooks-and-events/webhook-events-and-payloads).

Ma bibliothèque ne me permettait pas de simplement pousser tout l'`event` dans mon webhook - c'est pourquoi vous voyez les clés spécifiquement extraites. Peut-être que l'action que vous écrivez prendra tout l'`event` (et alors vous pourrez m'en parler !)

# GitHub Actions en... action
Et c'est tout ce dont vous avez besoin ! Tant que votre webhook répond avec un 200, votre action obtiendra une coche verte.

![GitHub Action en cours d'exécution](https://wilkie.tech/static/d3ccbdc63b22ba44de82ac52fea3ec6d/d3ebb/ga_running.png)

Si votre action échoue, vous pouvez voir ce qui s'est mal passé dans l'onglet Actions. La mienne échoue parce que je n'ai plus mon tunnel ngrok en cours d'exécution.

![Échec de l'action GitHub](https://wilkie.tech/static/183c23e95f3199b7832b4a83f39e4c99/3e755/ga_details.png)

# Bonus : comment obtenir et utiliser ngrok
Sans rapport avec cette fonctionnalité, il est très utile de pouvoir ouvrir un port hébergé localement pour les services externes. 

Dans ce cas, je veux que mon GitHub Action déclenche mon localhost, afin que je puisse tester la charge utile et l'exécution de mon webhook. Lorsque je mettrai cela en production, je remplacerai l'`url` par la version de production du code.

[Ngrok](https://ngrok.com/) à la rescousse ! Ngrok est un service qui crée un tunnel vers votre localhost. C'est gratuit, aussi. 

Mon entreprise paie pour que quelques-uns d'entre nous aient des URLs réservées (à cause des choses de développement web-to-mobile) mais pour vos besoins ici, gratuit est parfait. 

Il suffit de faire `brew install ngrok` (ou le gestionnaire de paquets que vous utilisez), de lancer votre localhost servant le code du webhook, et `ngrok http <votre-port>`. 

Maintenant, vous avez créé une connexion publique à votre localhost. GitHub pourra y accéder et vous pourrez tester votre exécution. Soyez simplement conscient que les tunnels gratuits expirent après un certain temps et nécessiteront une nouvelle URL.

# Et maintenant ?
Si cela vous donne des idées cool pour ce que vous pouvez faire avec les changements de votre GitHub, vous devriez consulter le [Marketplace des Actions](https://github.com/marketplace?type=actions). 

Vous y trouverez que des gens très intelligents ont imaginé toutes sortes de choses à faire lorsque des événements sont déclenchés dans votre GitHub. Ici, vous trouverez des auto-linters, des connexions Jira, des outils de déploiement et bien plus encore. 

Bonnes actions !