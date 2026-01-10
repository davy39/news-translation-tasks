---
title: Comment utiliser Lighthouse dans GitHub Actions
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-03T13:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-lighthouse-in-github-actions
coverImage: https://www.freecodecamp.org/news/content/images/2019/11/zuccotti.jpg
tags:
- name: GitHub Actions
  slug: github-actions
- name: Lighthouse
  slug: lighthouse
seo_title: Comment utiliser Lighthouse dans GitHub Actions
seo_desc: 'By Adam Henson

  GitHub Actions are used to automate software engineering workflows. Similar to tools
  like CircleCI, Jenkins, Travis and many others, GitHub Actions provides a declarative
  API for defining workflows. These workflows can include jobs to ...'
---

Par Adam Henson

[GitHub Actions](https://help.github.com/en/actions/automating-your-workflow-with-github-actions) sont utilisés pour automatiser les workflows d'ingénierie logicielle. Similaire à des outils comme CircleCI, Jenkins, Travis et bien d'autres, GitHub Actions fournit une API déclarative pour définir des workflows. Ces workflows peuvent inclure des jobs pour construire, tester et déployer des applications. 

Lighthouse est un projet open-source de Google pour améliorer la qualité des pages web. Il fournit des métriques centrées sur l'utilisateur pour auditer le SEO, la performance, l'accessibilité, les meilleures pratiques et les applications web progressives. Pour une plongée plus profonde sur Lighthouse, veuillez lire « [Comment analyser la performance d'un site web avec Lighthouse](https://www.freecodecamp.org/news/three-ways-to-analyze-website-performance-with-lighthouse-8d100966c04b/) ». Cet article démontrera les points suivants :

* Implémentation de base de Lighthouse dans un workflow GitHub Actions.
* Configuration avancée pour afficher les résultats de Lighthouse dans les commentaires des pull requests.
* Téléchargements de rapports Lighthouse vers S3.
* Notifications Slack.

# Action GitHub Check Lighthouse

Cet article fournira un guide pour utiliser [Lighthouse Check Action](https://github.com/foo-software/lighthouse-check-action) pour automatiser les audits Lighthouse. Il peut être utilisé dans un workflow - [déclenché par n'importe quel événement](https://help.github.com/en/actions/automating-your-workflow-with-github-actions/events-that-trigger-workflows). Cet article démontrera comment utiliser l'action lorsqu'elle est déclenchée par un événement de pull request.

# Exemple de base

Avec les étapes suivantes, nous pouvons créer un workflow de base.

1. Créez et basculez vers une nouvelle branche localement.
2. Créez un fichier dans votre projet avec un chemin similaire à `.github/workflows/my-workflow.yml` (en remplaçant `my-workflow` par un nom de votre choix).
3. Remplissez le fichier avec l'exemple montré ci-dessous, en remplaçant le champ `urls` par une liste séparée par des virgules des URL que vous souhaitez tester.
4. Validez les changements localement et poussez la branche vers votre dépôt distant.
5. Depuis votre nouvelle branche, ouvrez une pull request.

```yaml
name: Vérification Lighthouse
on: [pull_request]

jobs:
  lighthouse-check:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@master
    - run: mkdir /tmp/artifacts
    - name: Exécuter Lighthouse
      uses: foo-software/lighthouse-check-action@master
      with:
        outputDirectory: /tmp/artifacts
        urls: 'https://www.foo.software,https://www.foo.software/contact'
    - name: Télécharger les artefacts
      uses: actions/upload-artifact@master
      with:
        name: Rapports Lighthouse
        path: /tmp/artifacts
 ```

Et voilà ? — nous avons un workflow avec Lighthouse ! En supposant que vous avez activé GitHub Actions dans votre dépôt, vous devriez voir quelque chose comme ci-dessous (_note : au moment de la rédaction, GitHub Actions est en mode « bêta » et [nécessite une inscription](https://github.com/features/actions)).

![Image](https://www.freecodecamp.org/news/content/images/2019/11/github-tabs.png)
_Onglets du dépôt GitHub_

En cliquant sur « Actions », vous verrez la liste de tous les workflows en cours d'exécution et précédents.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/list-github-actions.png)
_Liste des workflows GitHub Actions_

Après avoir suivi les étapes de notre exemple de base, vous devriez voir un élément dans cette liste. En cliquant dessus, nous verrons les résultats de Lighthouse imprimés dans la console.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/output-github-actions.png)
_Résultats de Lighthouse imprimés dans la console_

Grâce à notre configuration, nous avons également des résultats capturés dans des rapports HTML enregistrés en tant qu'« artefacts ».

![Image](https://www.freecodecamp.org/news/content/images/2019/11/artifacts-github-actions.png)
_Cliquer sur le menu déroulant « Artifacts » télécharge les rapports HTML_

![Image](https://www.freecodecamp.org/news/content/images/2019/11/lighthouse-report-github-actions.png)
_Rapport complet de Lighthouse en tant que fichier HTML téléchargé depuis « Artifacts »_

# Exemple avancé

L'action Lighthouse Check offre un ensemble complet de fonctionnalités en utilisant le module [lighthouse-check](https://github.com/foo-software/lighthouse-check) [NPM](https://github.com/foo-software/lighthouse-check) sous le capot. Il y a beaucoup plus que nous pouvons faire avec cela. Continuons !

## Commentaires sur les pull requests

En utilisant cette fonctionnalité, des commentaires sont publiés avec les résultats de Lighthouse à chaque commit. Nous pouvons le faire en suivant les étapes ci-dessous.

1. Créez un nouvel utilisateur ou trouvez un utilisateur existant pour agir en tant que « bot ».
2. [Créez un jeton d'accès personnel](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line) depuis ce compte utilisateur.
3. [Créez un secret GitHub pour stocker la valeur chiffrée](https://help.github.com/en/actions/automating-your-workflow-with-github-actions/creating-and-using-encrypted-secrets) depuis ci-dessus. Dans notre exemple, nous le nommons `LIGHTHOUSE_CHECK_GITHUB_ACCESS_TOKEN`.
4. Mettez à jour notre fichier de workflow avec le diff montré ci-dessous.
5. Validez et poussez.

```yaml
with:
+  accessToken: ${{ secrets.LIGHTHOUSE_CHECK_GITHUB_ACCESS_TOKEN }}
  outputDirectory: /tmp/artifacts
```

Avec cela, nous avons créé un bot pour publier les résultats de Lighthouse sur les pull requests ?!

![Image](https://www.freecodecamp.org/news/content/images/2019/11/pr-comment-1-github-actions.png)
_Résultats de Lighthouse en tant que commentaires de PR_

## Téléchargements de rapports S3

Dans notre exemple, nous conservons les résultats en téléchargeant les rapports en tant qu'artefacts dans notre workflow. Cette solution pourrait être suffisante dans certains cas, mais les artefacts ne sont pas stockés de manière permanente. Pour consulter les rapports, nous devons naviguer dans le workflow et télécharger manuellement les rapports depuis la vue des artefacts. 

Mais que faire si nous voulons une méthode plus fiable pour stocker et référencer les rapports ? C'est là que la fonctionnalité S3 entre en jeu. Nous pouvons configurer le stockage AWS S3 en suivant les étapes ci-dessous.

1. [Créez un compte AWS](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/) si vous n'en avez pas déjà un.
2. [Créez un bucket S3](https://docs.aws.amazon.com/AmazonS3/latest/gsg/SigningUpforS3.html) si vous n'en avez pas déjà un.
3. [Acquérez un identifiant de clé d'accès AWS et une clé d'accès secrète](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html).
4. [Créez des secrets GitHub](https://help.github.com/en/actions/automating-your-workflow-with-github-actions/creating-and-using-encrypted-secrets) pour ces deux valeurs. Dans notre exemple, nous utiliserons `LIGHTHOUSE_CHECK_AWS_ACCESS_KEY_ID` et `LIGHTHOUSE_CHECK_AWS_SECRET_ACCESS_KEY`, respectivement.
5. Ajoutez le nom du bucket et la [région](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html) (exemple : `us-east-1`) en tant que secrets GitHub : `LIGHTHOUSE_CHECK_AWS_BUCKET` et `LIGHTHOUSE_CHECK_AWS_REGION`.

Ensuite, nous mettrons à jour notre configuration avec le diff suivant.

```yaml
with:
  accessToken: ${{ secrets.LIGHTHOUSE_CHECK_GITHUB_ACCESS_TOKEN }}
+  awsAccessKeyId: ${{ secrets.LIGHTHOUSE_CHECK_AWS_ACCESS_KEY_ID }}
+  awsBucket: ${{ secrets.LIGHTHOUSE_CHECK_AWS_BUCKET }}
+  awsRegion: ${{ secrets.LIGHTHOUSE_CHECK_AWS_REGION }}
+  awsSecretAccessKey: ${{ secrets.LIGHTHOUSE_CHECK_AWS_SECRET_ACCESS_KEY }}
```

Dans notre prochain commit et push, les rapports sont automatiquement téléchargés vers S3 ✅! Nous avons également un lien vers ceux-ci dans nos commentaires de PR.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/pr-comment-github-actions.png)
_Commentaire de PR avec résultat Lighthouse et rapport S3 lié_

## Notifications Slack

Qu'est-ce qu'une nouvelle fonctionnalité dans un workflow DevOps sans notifications Slack ? Une fonctionnalité triste, en effet. Augmentons les choses en ajoutant des notifications à un canal Slack pour que toute notre équipe puisse voir. Nous pouvons accomplir cela en suivant les étapes ci-dessous.

1. [Créez un « Incoming Webhook » dans votre espace de travail Slack et autorisez un canal](https://api.slack.com/messaging/webhooks).
2. Ajoutez l'URL du Webhook en tant que [secret GitHub](https://help.github.com/en/actions/automating-your-workflow-with-github-actions/creating-and-using-encrypted-secrets) — `LIGHTHOUSE_CHECK_WEBHOOK_URL`.
3. Ajoutez les données GitHub et l'URL du Webhook à notre configuration avec le diff ci-dessous. Les données GitHub seront rendues dans nos notifications. Nous passons les données GitHub via la configuration avec le [« contexte » GitHub](https://help.github.com/en/actions/automating-your-workflow-with-github-actions/contexts-and-expression-syntax-for-github-actions#github-context).

```yaml
with:
  accessToken: ${{ secrets.LIGHTHOUSE_CHECK_GITHUB_ACCESS_TOKEN }}  +  author: ${{ github.actor }}
  awsAccessKeyId: ${{ secrets.LIGHTHOUSE_CHECK_AWS_ACCESS_KEY_ID }}
  awsBucket: ${{ secrets.LIGHTHOUSE_CHECK_AWS_BUCKET }}
  awsRegion: ${{ secrets.LIGHTHOUSE_CHECK_AWS_REGION }}
  awsSecretAccessKey: ${{ secrets.LIGHTHOUSE_CHECK_AWS_SECRET_ACCESS_KEY }}
+  branch: ${{ github.ref }}
  outputDirectory: /tmp/artifacts
+  sha: ${{ github.sha }}
+  slackWebhookUrl: ${{ secrets.LIGHTHOUSE_CHECK_WEBHOOK_URL }}
  urls: 'https://www.foo.software,https://www.foo.software/contact'
```

Notre prochain commit et push introduisent les notifications Slack ! Le lien « Lighthouse audit » dans la capture d'écran ci-dessous navigue vers le rapport S3 tel que configuré ✨.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/slack-github-actions.png)
_Notification Slack de Lighthouse_

## **Maintenir un historique**

[Vérification automatisée de Lighthouse de Foo](https://www.foo.software/lighthouse) est un outil que nous pouvons utiliser pour gérer un historique des audits Lighthouse. Nous pouvons nous connecter à celui-ci avec Lighthouse Check GitHub ! En faisant cela, vous pouvez exécuter Lighthouse à distance plutôt que dans un environnement GitHub local et dockerisé. Avec cela, nous pouvons être assurés que nos résultats Lighthouse ne sont pas instables en raison des changements d'infrastructure de GitHub. Suivez les [étapes documentées pour vous connecter avec Automated Lighthouse Check](https://github.com/foo-software/lighthouse-check-action#usage-automated-lighthouse-check-api).

![Image](https://www.freecodecamp.org/news/content/images/2020/01/automated-lighthouse-check.png)
_Un historique des audits Lighthouse avec « Automated Lighthouse Check »_

# Et maintenant ?

Vous pouvez trouver un exemple complet de ce qui précède dans la [documentation de Lighthouse Check Action](https://github.com/foo-software/lighthouse-check-action#example-usage). J'espère que cet article peut fournir une addition utile à votre workflow DevOps ! Avec Lighthouse intégré dans un pipeline CI/CD, nous pouvons rester pleinement équipés pour assurer une haute qualité en matière de SEO, de performance, d'accessibilité, de meilleures pratiques et d'applications web progressives.