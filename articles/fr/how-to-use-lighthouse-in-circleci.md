---
title: Comment utiliser Lighthouse dans CircleCI
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-06T12:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-lighthouse-in-circleci
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/nyc-building-in-midtown-east.jpg
tags:
- name: Accessibility
  slug: accessibility
- name: CircleCI
  slug: circleci
- name: Lighthouse
  slug: lighthouse
- name: SEO
  slug: seo
- name: technology
  slug: technology
- name: Website performance
  slug: website-performance
seo_title: Comment utiliser Lighthouse dans CircleCI
seo_desc: 'By Adam Henson

  CircleCI is a popular tool for orchestrating CI/CD pipelines. Lighthouse is an open-source
  project from Google for improving the quality of web pages. It provides user-centric
  metrics to audit SEO, performance, accessibility, best prac...'
---

Par Adam Henson

[CircleCI](https://circleci.com/) est un outil populaire pour orchestrer les pipelines CI/CD. Lighthouse est un projet open-source de Google pour améliorer la qualité des pages web. Il fournit des métriques centrées sur l'utilisateur pour auditer le SEO, la performance, l'accessibilité, les bonnes pratiques et les applications web progressives. 

Pour une plongée plus profonde sur Lighthouse, vous pouvez lire « [Comment analyser la performance d'un site web avec Lighthouse](https://www.freecodecamp.org/news/three-ways-to-analyze-website-performance-with-lighthouse-8d100966c04b/) ». 

En combinant ces forces, nous pouvons établir une automatisation de la qualité des sites web. Cet article démontrera les points suivants :

* Implémentation de base de Lighthouse dans un workflow CircleCI.
* Configuration avancée pour afficher les résultats de Lighthouse dans les commentaires des pull requests.
* Téléchargements de rapports Lighthouse vers S3.
* Notifications Slack.

# Lighthouse Check CircleCI Orb

Les [CircleCI Orbs](https://circleci.com/docs/2.0/orb-intro/#section=configuration) sont des packages partageables d'éléments de configuration, incluant des jobs, des commandes et des exécutants que vous utilisez dans vos workflows. Cet article fournira un guide pour utiliser le [Lighthouse Check CircleCI Orb](https://circleci.com/orbs/registry/orb/foo-software/lighthouse-check) pour automatiser les audits Lighthouse.

### Exemple de base

Voici un exemple minimal et tout ce dont nous avons besoin pour exécuter Lighthouse automatiquement à chaque changement de code 💡. Dans cet exemple, [`https://www.foo.software`](https://www.foo.software) et [`https://www.foo.software/contact`](https://www.foo.software/contact) seront audités.

```yaml
version: 2.1

orbs:
  lighthouse-check: foo-software/lighthouse-check@0.0.8

jobs:
  test: 
    executor: lighthouse-check/default
    steps:
      - lighthouse-check/audit:
          urls: https://www.foo.software,https://www.foo.software/contact

workflows:
  test:
    jobs:
      - test
```

Avec cette configuration minimale, nous avons un résumé fourni dans la sortie de notre job. Nous avons également des rapports HTML complets enregistrés en tant qu'"artifacts" [CircleCI](https://circleci.com/docs/2.0/artifacts/).

![Image](https://www.freecodecamp.org/news/content/images/2020/01/circleci-orb-lighthouse-check-output.png)
_Sortie de l'Orb Lighthouse Check_

![Image](https://www.freecodecamp.org/news/content/images/2020/01/circleci-orb-lighthouse-check-artifacts.png)
_Artifacts enregistrés par l'Orb Lighthouse Check_

### Exemple avancé

Lighthouse Check CircleCI Orb offre un ensemble complet de fonctionnalités en utilisant le module [NPM](https://github.com/foo-software/lighthouse-check) [`lighthouse-check`](https://github.com/foo-software/lighthouse-check) sous le capot. Il y a beaucoup plus que nous pouvons faire avec cela. Procédez !

## Commentaires sur les Pull Requests

En utilisant cette fonctionnalité, des commentaires sont publiés avec les résultats de Lighthouse à chaque commit. Nous pouvons le faire en suivant les étapes ci-dessous.

1. Créez un nouvel utilisateur ou trouvez un utilisateur existant pour agir en tant que "bot".
2. [Créez un jeton d'accès personnel](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line) à partir de ce compte utilisateur.
3. [Créez une variable d'environnement CircleCI dans votre projet](https://circleci.com/docs/2.0/env-vars/#setting-an-environment-variable-in-a-project) pour stocker la valeur chiffrée ci-dessus. Dans notre exemple, nous la nommons `LIGHTHOUSE_CHECK_GITHUB_ACCESS_TOKEN`.
4. Mettez à jour notre fichier de configuration avec le diff montré ci-dessous.

```diff
+ prCommentAccessToken: $LIGHTHOUSE_CHECK_GITHUB_ACCESS_TOKEN
+ prCommentUrl: https://api.github.com/repos/foo-software/lighthouse-check-orb/pulls/${CIRCLE_PULL_REQUEST##*/}/reviews
urls: https://www.foo.software,https://www.foo.software/contact
```

Les mises à jour ci-dessus fournissent un jeton pour autoriser les commentaires sur une pull request correspondante. `prCommentUrl` doit être un endpoint au [format spécifié par l'API GitHub](https://developer.github.com/v3/pulls/reviews/#create-a-pull-request-review). Votre endpoint sera similaire mais avec les paramètres `owner` et `repo` remplacés ( `foo-software/lighthouse-check-orb` ). Avec cela, nous avons créé un bot pour publier les résultats de Lighthouse sur les pull requests 💡

![Image](https://www.freecodecamp.org/news/content/images/2020/01/lighthouse-check-pr-comment.png)
_Commentaires de PR Lighthouse Check_

## Téléchargements de rapports S3

Dans notre exemple, nous persistons les résultats en téléchargeant les rapports en tant qu'artifacts dans notre job. Cette solution pourrait être suffisante dans certains cas, mais les artifacts ne sont pas stockés de manière permanente. Pour consulter les rapports, nous devons naviguer dans le workflow et télécharger manuellement les rapports à partir de la vue des artifacts. 

Mais que faire si nous voulons une méthode plus fiable pour stocker et référencer les rapports ? C'est là que la fonctionnalité S3 entre en jeu. Nous pouvons configurer le stockage AWS S3 en suivant les étapes ci-dessous.

1. [Créez un compte AWS](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/) si vous n'en avez pas déjà un.
2. [Créez un bucket S3](https://docs.aws.amazon.com/AmazonS3/latest/gsg/SigningUpforS3.html) si vous n'en avez pas déjà un.
3. [Obtenez un identifiant de clé d'accès AWS et une clé d'accès secrète](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html).
4. [Créez des variables d'environnement CircleCI](https://circleci.com/docs/2.0/env-vars/#setting-an-environment-variable-in-a-project) pour ces deux valeurs. Dans notre exemple, nous utiliserons `LIGHTHOUSE_CHECK_AWS_ACCESS_KEY_ID` et `LIGHTHOUSE_CHECK_AWS_SECRET_ACCESS_KEY`, respectivement.
5. Ajoutez le nom du bucket et la [région](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html) (exemple : `us-east-1`) en tant que variables d'environnement CircleCI : `LIGHTHOUSE_CHECK_AWS_BUCKET` et `LIGHTHOUSE_CHECK_AWS_REGION`.

Ensuite, nous mettrons à jour notre configuration avec le diff suivant.

```diff
+ awsAccessKeyId: $LIGHTHOUSE_CHECK_AWS_ACCESS_KEY_ID
+ awsBucket: $LIGHTHOUSE_CHECK_AWS_BUCKET
+ awsRegion: $LIGHTHOUSE_CHECK_AWS_REGION
+ awsSecretAccessKey: $LIGHTHOUSE_CHECK_AWS_SECRET_ACCESS_KEY
prCommentUrl: https://api.github.com/repos/foo-software/lighthouse-check-orb/pulls/${CIRCLE_PULL_REQUEST##*/}/reviews
```

Dans notre prochain commit et push, les rapports sont automatiquement téléchargés vers S3 ✅! Nous avons également un lien vers ceux-ci dans nos commentaires de PR.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/pr-comment-lighthouse.png)
_Commentaire de PR avec résultat Lighthouse et rapport S3 lié_

## Notifications Slack

Qu'est-ce qu'une nouvelle fonctionnalité dans un workflow DevOps sans notifications Slack ? Une bien triste chose en effet. Augmentons les choses en ajoutant des notifications à un canal Slack pour que toute notre équipe puisse voir. Nous pouvons accomplir cela en suivant les étapes ci-dessous.

1. [Créez un "Incoming Webhook" dans votre espace de travail Slack et autorisez un canal](https://api.slack.com/messaging/webhooks).
2. Ajoutez l'URL du Webhook en tant que variable d'environnement CircleCI — `LIGHTHOUSE_CHECK_SLACK_WEBHOOK_URL`.

```diff
+ slackWebhookUrl: $LIGHTHOUSE_CHECK_SLACK_WEBHOOK_URL
urls: https://www.foo.software,https://www.foo.software/contact
```

Notre prochain commit et push introduit les notifications Slack ! Le lien "Lighthouse audit" dans la capture d'écran ci-dessous navigue vers le rapport S3 tel que configuré ✨

![Image](https://www.freecodecamp.org/news/content/images/2020/01/circleci-orb-lighthouse-check-slack.png)
_Notification Slack Lighthouse_

À ce stade, notre configuration "exemple avancé" complète ressemble à ce qui suit.

```yaml
usage:
  version: 2.1

  orbs:
    lighthouse-check: foo-software/lighthouse-check@0.0.8

  jobs:
    test: 
      executor: lighthouse-check/default
      steps:
        - lighthouse-check/audit:
            awsAccessKeyId: $LIGHTHOUSE_CHECK_AWS_ACCESS_KEY_ID
            awsBucket: $LIGHTHOUSE_CHECK_AWS_BUCKET
            awsRegion: $LIGHTHOUSE_CHECK_AWS_REGION
            awsSecretAccessKey: $LIGHTHOUSE_CHECK_AWS_SECRET_ACCESS_KEY
            prCommentAccessToken: $LIGHTHOUSE_CHECK_GITHUB_ACCESS_TOKEN
            prCommentUrl: https://api.github.com/repos/foo-software/lighthouse-check-orb/pulls/${CIRCLE_PULL_REQUEST##*/}/reviews
            slackWebhookUrl: $LIGHTHOUSE_CHECK_SLACK_WEBHOOK_URL
            urls: https://www.foo.software,https://www.foo.software/contact

  workflows:
    test:
      jobs:
        - test
```

## Maintenir un historique

[Foo's Automated Lighthouse Check](https://www.foo.software/lighthouse) est un outil que nous pouvons utiliser pour gérer un historique des audits Lighthouse. Nous pouvons nous connecter à celui-ci avec le Lighthouse Check Orb ! En faisant cela, vous pouvez exécuter Lighthouse à distance plutôt que dans un environnement local et dockerisé de CircleCI. Avec cela, nous pouvons être assurés que nos résultats Lighthouse ne sont pas instables en raison des changements d'infrastructure de CircleCI. Suivez les [étapes documentées pour vous connecter avec Automated Lighthouse Check](https://github.com/foo-software/lighthouse-check-orb#usage-automated-lighthouse-check-api).

![Image](https://www.freecodecamp.org/news/content/images/2020/01/automated-lighthouse-check.png)
_Un historique des audits Lighthouse avec "Automated Lighthouse Check"_

# Et maintenant ?

Vous pouvez trouver d'autres exemples d'utilisation de [Lighthouse Check Orb sur GitHub](https://github.com/foo-software/lighthouse-check-orb/tree/master/src/examples). J'espère que cet article a fourni un ajout utile à votre workflow DevOps ! Avec Lighthouse intégré dans un pipeline CI/CD, nous pouvons rester pleinement équipés pour assurer une haute qualité en matière de SEO, de performance, d'accessibilité, de bonnes pratiques et d'applications web progressives.