---
title: Qu'est-ce que les GitHub Actions et comment automatiser les tests et les notifications
  Slack ?
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-06-03T14:45:00.000Z'
originalURL: https://freecodecamp.org/news/what-are-github-actions-and-how-can-you-automate-tests-and-slack-notifications
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/github-actions.jpg
tags:
- name: automation
  slug: automation
- name: 'automation testing '
  slug: automation-testing
- name: CI/CD
  slug: cicd
- name: continuous delivery
  slug: continuous-delivery
- name: continuous deployment
  slug: continuous-deployment
- name: Continuous Integration
  slug: continuous-integration
- name: Devops
  slug: devops
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: GitHub Actions
  slug: github-actions
- name: slack
  slug: slack
- name: Software Testing
  slug: software-testing
- name: 'tech '
  slug: tech
- name: Testing
  slug: testing
seo_title: Qu'est-ce que les GitHub Actions et comment automatiser les tests et les
  notifications Slack ?
seo_desc: "Automation is a powerful tool. It both saves us time and can help reduce\
  \ human error. \nBut automation can be tough and can sometimes prove to be costly.\
  \ How can Github Actions help harden our code and give us more time to work on features\
  \ instead of ..."
---

L'automatisation est un outil puissant. Elle nous fait gagner du temps et peut aider à réduire les erreurs humaines. 

Mais l'automatisation peut être difficile et parfois coûteuse. Comment les GitHub Actions peuvent-elles aider à renforcer notre code et nous donner plus de temps pour travailler sur les fonctionnalités plutôt que sur les bugs ?

* [Qu'est-ce que les GitHub Actions ?](#heading-quest-ce-que-les-github-actions)
* [Qu'est-ce que le CI/CD ?](#heading-quest-ce-que-le-cicd)
* [Que allons-nous construire ?](#heading-que-allons-nous-construire)
* [Partie 0 : Configuration d'un projet](#heading-partie-0-installation-dun-projet)
* [Partie 1 : Automatisation des tests](#heading-partie-1-automatisation-des-tests)
* [Partie 2 : Publication des nouvelles pull requests sur Slack](#heading-partie-2-publication-des-nouvelles-pull-requests-sur-slack)

%[https://www.youtube.com/watch?v=1n-jHHNSoTw]

## Qu'est-ce que les GitHub Actions ?

[Actions](https://github.com/features/actions) sont une fonctionnalité relativement nouvelle de [GitHub](https://github.com/) qui permet de configurer des workflows CI/CD en utilisant un fichier de configuration directement dans votre dépôt GitHub.

Auparavant, si vous vouliez configurer une forme d'automatisation avec des tests, des builds ou des déploiements, vous deviez recourir à des services comme [Circle CI](https://circleci.com/) et [Travis](https://travis-ci.org/) ou écrire vos propres scripts. Mais avec Actions, vous avez un support de première classe pour des outils puissants afin d'automatiser votre workflow.

## Qu'est-ce que le CI/CD ?

CI/CD signifie Intégration Continue et Déploiement Continu (ou peut être Livraison Continue). Ce sont deux pratiques de développement logiciel qui permettent aux équipes de construire des projets ensemble rapidement, efficacement et idéalement avec moins d'erreurs.

L'Intégration Continue est l'idée que, alors que différents membres de l'équipe travaillent sur le code dans différentes branches git, le code est fusionné dans une seule branche de travail qui est ensuite construite et testée avec des workflows automatisés. Cela aide à s'assurer constamment que le code de tout le monde fonctionne correctement ensemble et est bien testé.

Le Déploiement Continu va plus loin et porte cette automatisation au niveau du déploiement. Alors qu'avec le processus CI, vous automatisez les tests et la construction, le Déploiement Continu automatisera le déploiement du projet dans un environnement. 

L'idée est que le code, une fois passé par tous les processus de construction et de test, est dans un état déployable, donc il devrait pouvoir être déployé.

## Que allons-nous construire ?

Nous allons aborder deux workflows différents.

Le premier consistera simplement à exécuter des tests automatisés qui empêcheront une pull request d'être fusionnée si elle échoue. Nous ne passerons pas par la construction des tests, mais nous verrons comment exécuter des tests qui existent déjà.

Dans la deuxième partie, nous configurerons un workflow qui envoie un message à Slack avec un lien vers une pull request chaque fois qu'une nouvelle est créée. Cela peut être très utile lorsque vous travaillez sur des projets open source avec une équipe et que vous avez besoin d'un moyen de suivre les demandes.

## Partie 0 : Configuration d'un projet

Pour ce guide, vous pouvez vraiment travailler sur n'importe quel projet basé sur Node.js tant qu'il a des tests que vous pouvez exécuter pour la Partie 1.

Si vous souhaitez suivre un exemple plus simple que j'utiliserai, j'ai configuré un nouveau projet que vous pouvez cloner avec une seule fonction qui a deux tests capables de s'exécuter et de réussir.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/function-with-test.jpg)
_Une fonction avec deux tests_

Si vous souhaitez consulter ce code pour commencer, vous pouvez exécuter :

```shell
git clone --single-branch --branch start git@github.com:colbyfayock/my-github-actions.git

```

Une fois que vous avez cloné localement et installé les dépendances, vous devriez pouvoir exécuter les tests et voir qu'ils réussissent !

![Image](https://www.freecodecamp.org/news/content/images/2020/05/passing-tests.jpg)
_Tests réussis_

Il devrait également être noté que vous devrez avoir ce projet ajouté en tant que nouveau dépôt sur GitHub afin de suivre.

[Suivez avec le commit !](https://github.com/colbyfayock/my-github-actions/commit/6919b1b9beea4823fd28375f1864d233e23f2d26)

## Partie 1 : Automatisation des tests

Les tests sont une partie importante de tout projet qui nous permet de nous assurer que nous ne cassons pas le code existant pendant que nous travaillons. Bien qu'ils soient importants, ils sont aussi faciles à oublier.

Nous pouvons éliminer la nature humaine de l'équation et automatiser l'exécution de nos tests pour nous assurer que nous ne pouvons pas continuer sans corriger ce que nous avons cassé.

### Étape 1 : Création d'une nouvelle action

La bonne nouvelle, c'est que GitHub facilite vraiment le démarrage de ce workflow car il fait partie de leurs options préconfigurées.

Nous commencerons par naviguer vers l'onglet **Actions** sur la page de notre dépôt.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/github-actions-dashboard.jpg)
_Page de démarrage des GitHub Actions_

Une fois là-bas, nous verrons immédiatement quelques workflows de démarrage que GitHub nous propose pour commencer. Puisque nous utilisons un projet Node, nous pouvons cliquer sur **Configurer ce workflow** sous le workflow **Node.js**.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/github-action-new-nodejs-workflow.jpg)
_Configuration d'un workflow GitHub Action Node.js_

Après le chargement de la page, GitHub vous amènera à un nouvel éditeur de fichier qui a déjà un tas d'options de configuration ajoutées.

Nous allons en fait laisser cela "tel quel" pour notre première étape. Optionnellement, vous pouvez changer le nom du fichier en `tests.yml` ou quelque chose que vous retiendrez.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/github-action-create-new-workflow.jpg)
_Ajout d'un nouveau fichier de workflow GitHub Action_

Vous pouvez cliquer sur **Démarrer le commit** puis soit le commiter directement dans la branche `master` ou ajouter le changement à une nouvelle branche. Pour ce guide, je vais commiter directement dans `master`.

Pour voir notre nouvelle action s'exécuter, nous pouvons à nouveau cliquer sur l'onglet **Actions** qui nous ramènera à notre nouveau tableau de bord Actions.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/github-action-workflow-status.jpg)
_Affichage des événements du workflow GitHub Action_

De là, vous pouvez cliquer sur **Node.js CI** et sélectionner le commit que vous venez de faire ci-dessus et vous atterrirez sur notre nouveau tableau de bord d'action. Vous pouvez ensuite cliquer sur l'une des versions de node dans la barre latérale via **build (#.x)**, cliquer sur le menu déroulant **Exécuter npm test**, et nous pourrons voir le résultat de nos tests en cours d'exécution (ce qui, si vous me suivez, devrait réussir !).

![Image](https://www.freecodecamp.org/news/content/images/2020/05/github-action-workflow-logs.jpg)
_Affichage des logs d'un workflow GitHub Action_

[Suivez avec le commit !](https://github.com/colbyfayock/my-github-actions/commit/10e397966572ed9975cac40f6ab5f41c1255a947)

### Étape 2 : Configuration de notre nouvelle action

Alors, qu'avons-nous fait ci-dessus ? Nous allons passer en revue le fichier de configuration et ce que nous pouvons personnaliser.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/github-action-workflow-file.jpg)
_Fichier de workflow GitHub Action Node.js_

En commençant par le haut, nous spécifions notre nom :

```yaml
name: Node.js CI

```

Cela peut vraiment être ce que vous voulez. Ce que vous choisissez devrait vous aider à vous souvenir de ce que c'est. Je vais personnaliser cela en "Tests" pour que je sache exactement ce qui se passe.

```yaml
on:
  push:
    branches: [ master ]
  pull_request:
    branches: [ master ]

```

La clé `on` est la manière dont nous spécifions les événements qui déclenchent notre action. Cela peut être une variété de choses comme basé sur le temps avec [cron](https://en.wikipedia.org/wiki/Cron). Mais ici, nous disons que nous voulons que cette action s'exécute chaque fois que quelqu'un pousse des commits vers `master` ou que quelqu'un crée une pull request ciblant la branche `master`. Nous ne allons pas faire de changement ici.

```yaml
jobs:
  build:
    runs-on: ubuntu-latest

```

Ce prochain bit crée un nouveau job appelé `build`. Ici, nous disons que nous voulons utiliser la dernière version d'Ubuntu pour exécuter nos tests. [Ubuntu](https://ubuntu.com/) est courant, donc vous ne voudrez le personnaliser que si vous voulez l'exécuter sur un environnement spécifique.

```yaml
    strategy:
      matrix:
        node-version: [10.x, 12.x, 14.x]

```

À l'intérieur de notre job, nous spécifions une matrice de [stratégie](https://help.github.com/en/actions/reference/workflow-syntax-for-github-actions#jobsjob_idstrategy). Cela nous permet d'exécuter les mêmes tests sur quelques variations différentes. 

Dans ce cas, nous exécutons les tests sur 3 versions différentes de [node](https://nodejs.org/en/) pour nous assurer qu'il fonctionne sur toutes. Cela est définitivement utile pour s'assurer que votre code est flexible et prêt pour l'avenir, mais si vous construisez et exécutez votre code sur une version spécifique de node, vous pouvez changer cela pour cette version uniquement.

```yaml
    steps:
    - uses: actions/checkout@v2
    - name: Use Node.js ${{ matrix.node-version }}
      uses: actions/setup-node@v1
      with:
        node-version: ${{ matrix.node-version }}
    - run: npm ci
    - run: npm run build --if-present
    - run: npm test

```

Enfin, nous spécifions les étapes que nous voulons que notre job exécute. Décomposons cela :

* `uses: actions/checkout@v2` : Pour exécuter notre code, nous devons l'avoir disponible. Cela extrait notre code sur notre environnement de job afin que nous puissions l'utiliser pour exécuter des tests.
* `uses: actions/setup-node@v1` : Puisque nous utilisons node avec notre projet, nous aurons besoin qu'il soit configuré sur notre environnement. Nous utilisons cette action pour faire cette configuration pour nous pour chaque version que nous avons spécifiée dans la matrice que nous avons configurée ci-dessus.
* `run: npm ci` : Si vous n'êtes pas familier avec `npm ci`, c'est similaire à l'exécution de `npm install` mais utilise le fichier `package-lock.json` sans effectuer de mises à jour de correctifs. Donc, essentiellement, cela installe nos dépendances.
* `run: npm run build --if-present` : `npm run build` exécute le script de build dans notre projet. Le drapeau `--if-present` fait ce qu'il semble faire et n'exécute cette commande que si le script de build est présent. Cela ne fait pas de mal de le laisser car il ne s'exécutera pas sans le script, mais vous pouvez le supprimer car nous ne construisons pas le projet ici.
* `run: npm test` : Enfin, nous exécutons `npm test` pour exécuter nos tests. Cela utilise le script npm `test` configuré dans notre fichier `package.json`.

Et avec cela, nous avons fait quelques ajustements, mais nos tests devraient s'exécuter après que nous ayons commis ces changements et réussir comme avant !

![Image](https://www.freecodecamp.org/news/content/images/2020/05/github-action-workflow-logs-npm-test.jpg)
_Logs des tests réussis dans le workflow GitHub Action_

[Suivez avec le commit !](https://github.com/colbyfayock/my-github-actions/commit/087cd8e8592d1f2b520b6e44b70b0a242a9d2d72)

### Étape 3 : Test que nos tests échouent et empêchent les fusions

Maintenant que nos tests sont configurés pour s'exécuter automatiquement, essayons de les casser pour voir comment cela fonctionne.

À ce stade, vous pouvez vraiment faire ce que vous voulez pour casser intentionnellement les tests, mais [voici ce que j'ai fait](https://github.com/colbyfayock/my-github-actions/pull/1) :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/bad-changes-code-diff.jpg)
_Diff de code - https://github.com/colbyfayock/my-github-actions/pull/1_

Je retourne intentionnellement une sortie attendue différente afin que mes tests échouent. Et ils le font !

![Image](https://www.freecodecamp.org/news/content/images/2020/05/github-failing-checks.jpg)
_Vérifications de statut échouées sur la pull request_

Dans ma nouvelle pull request, ma nouvelle branche casse les tests, donc elle me dit que mes vérifications ont échoué. Si vous avez remarqué, cependant, elle est toujours verte pour la fusion, alors comment pouvons-nous empêcher les fusions ?

Nous pouvons empêcher les pull requests d'être fusionnées en configurant une Branche Protégée dans les paramètres de notre projet.

Tout d'abord, naviguez vers **Paramètres**, puis **Branches**, et cliquez sur **Ajouter une règle**.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/github-add-protected-branch.jpg)
_Règles de protection des branches GitHub_

Nous allons ensuite vouloir définir le motif du nom de la branche à `*`, ce qui signifie toutes les branches, cocher l'option **Exiger que les vérifications de statut réussissent avant la fusion**, puis sélectionner toutes nos différentes vérifications de statut que nous aimerions exiger pour réussir avant la fusion.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/github-configure-protected-branch.jpg)
_Configuration d'une règle de protection de branche dans GitHub_

Enfin, cliquez sur **Créer** en bas de la page.

Et une fois que vous revenez à la pull request, vous remarquerez que le message est un peu différent et indique que nous avons besoin que nos statuts réussissent avant de pouvoir fusionner.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/github-failing-checks-cant-merge.jpg)
_Tests échoués empêchant la fusion dans la pull request_

_Note : en tant qu'administrateur d'un dépôt, vous pourrez toujours fusionner, donc cela empêche techniquement uniquement les non-administrateurs de fusionner. Mais cela vous donnera des messages accrus si les tests échouent._

Et avec cela, nous avons une nouvelle GitHub Action qui exécute nos tests et empêche les pull requests de fusionner si elles échouent.

[Suivez avec la pull request !](https://github.com/colbyfayock/my-github-actions/pull/1)

_Note : nous ne fusionnerons pas cette pull request avant de continuer à la Partie 2._

## Partie 2 : Publication des nouvelles pull requests sur Slack

Maintenant que nous empêchons les demandes de fusion si elles échouent, nous voulons publier un message dans notre espace de travail [Slack](http://slack.com/) chaque fois qu'une nouvelle pull request est ouverte. Cela nous aidera à garder un œil sur nos dépôts directement dans Slack.

Pour cette partie du guide, vous aurez besoin d'un espace de travail Slack dans lequel vous avez les permissions de créer une nouvelle application de développeur et la capacité de créer un nouveau canal pour l'utilisateur bot qui sera associé à cette application.

### Étape 1 : Configuration de Slack

Il y a quelques choses que nous allons aborder lors de la configuration de Slack pour notre workflow :

* Créer une nouvelle application pour notre espace de travail
* Attribuer des permissions à notre bot
* Installer notre bot dans notre espace de travail
* Inviter notre nouveau bot dans notre canal

Pour commencer, nous allons créer une nouvelle application. Rendez-vous sur le [tableau de bord des applications Slack API](https://api.slack.com/apps). Si ce n'est pas déjà fait, connectez-vous à votre compte Slack avec l'espace de travail avec lequel vous souhaitez configurer cela.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/slack-create-new-app.jpg)
_Création d'une nouvelle application Slack_

Maintenant, cliquez sur **Créer une nouvelle application** où vous serez invité à entrer un nom et à sélectionner un espace de travail pour lequel vous souhaitez que cette application soit créée. Je vais appeler mon application "Gitbot" comme nom, mais vous pouvez choisir ce qui vous semble logique. Ensuite, cliquez sur **Créer une application**.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/slack-add-name-new-app.jpg)
_Configuration d'une nouvelle application Slack_

Une fois créée, naviguez vers le lien **Accueil de l'application** dans la barre latérale de gauche. Afin d'utiliser notre bot, nous devons lui attribuer des [portées OAuth](https://oauth.net/) afin qu'il ait les permissions de travailler dans notre canal, donc sélectionnez **Examiner les portées à ajouter** sur cette page.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/slack-app-review-scopes.jpg)
_Examen des portées de l'application Slack_

Faites défiler vers le bas et vous verrez une section **Portées** et en dessous une section **Jeton du bot**. Ici, cliquez sur **Ajouter une portée OAuth**. Pour notre bot, nous n'avons pas besoin de nombreuses permissions, donc ajoutez les portées `channels:join` et `chat:write` et nous devrions être prêts à partir.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/slack-app-add-scopes.jpg)
_Ajout de portées pour un jeton de bot d'application Slack_

Maintenant que nous avons nos portées, ajoutons notre bot à notre espace de travail. Faites défiler vers le haut sur cette même page jusqu'en haut et vous verrez un bouton qui dit **Installer l'application dans l'espace de travail**.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/slack-install-app-to-workspace.jpg)
_Installation de l'application Slack dans un espace de travail_

Une fois que vous cliquez dessus, vous serez redirigé vers une page d'autorisation. Ici, vous pouvez voir les portées que nous avons sélectionnées pour notre bot. Ensuite, cliquez sur **Autoriser**.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/slack-app-allow-workspace-permissions.jpg)
_Autorisation de l'application Slack à être installée dans l'espace de travail_

À ce stade, notre bot Slack est prêt à être utilisé. En haut de la page **OAuth & Permissions**, vous verrez un **Jeton d'accès OAuth de l'utilisateur bot**. C'est ce que nous utiliserons lors de la configuration de notre workflow, donc copiez et sauvegardez ce jeton ou retenez cet emplacement pour savoir comment le trouver plus tard.

_Note : ce jeton est privé - ne le donnez pas, ne le montrez pas dans une capture d'écran, et ne laissez personne le voir !_

![Image](https://www.freecodecamp.org/news/content/images/2020/05/slack-app-oauth-token.jpg)
_Copie du jeton d'accès OAuth pour l'utilisateur bot Slack_

Enfin, nous devons inviter notre bot Slack dans notre canal. Si vous ouvrez votre espace de travail, vous pouvez soit utiliser un canal existant, soit créer un nouveau canal pour ces notifications, mais vous voudrez entrer la commande `/invite @[nomdubot]` qui invitera notre bot dans notre canal.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/slack-invite-bot-to-channel.jpg)
_Invitation de l'utilisateur bot Slack dans le canal_

Et une fois ajouté, nous avons terminé la configuration de Slack !

![Image](https://www.freecodecamp.org/news/content/images/2020/05/slack-app-bot-joined-channel.jpg)
_Le bot Slack a été ajouté au canal_

### Créer une GitHub Action pour notifier Slack

Notre prochaine étape sera quelque peu similaire à la création de notre première GitHub Action. Nous allons créer un fichier de workflow que nous configurerons pour envoyer nos notifications.

Bien que nous puissions utiliser nos éditeurs de code pour cela en créant un fichier dans le répertoire `.github`, je vais utiliser l'interface utilisateur de GitHub.

Tout d'abord, revenons à notre onglet _Actions_ dans notre dépôt. Une fois là-bas, sélectionnez **Nouveau workflow**.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/github-new-workflow.jpg)
_Configuration d'un nouveau workflow GitHub Action_

Cette fois, nous allons démarrer le workflow manuellement au lieu d'utiliser une Action préconçue. Sélectionnez **configurer un workflow vous-même** en haut.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/github-set-up-new-workflow.jpg)
_Configuration manuelle d'un workflow GitHub Action_

Une fois la nouvelle page chargée, vous serez dirigé vers un nouveau modèle où nous pouvons commencer à travailler. Voici à quoi ressemblera notre nouveau workflow :

```yaml
name: Notifications Slack

on:
  pull_request:
    branches: [ master ]

jobs:
  notifySlack:

    runs-on: ubuntu-latest

    steps:
    - name: Notifier Slack
      env:
        SLACK_BOT_TOKEN: ${{ secrets.SLACK_BOT_TOKEN }}
      uses: abinoda/slack-action@master
      with:
        args: '{\"channel\":\"[Channel ID]\",\"blocks\":[{\"type\":\"section\",\"text\":{\"type\":\"mrkdwn\",\"text\":\"*Pull Request:* ${{ github.event.pull_request.title }}\"}},{\"type\":\"section\",\"text\":{\"type\":\"mrkdwn\",\"text\":\"*Qui ?:* ${{ github.event.pull_request.user.login }}\n*État de la demande :* ${{ github.event.pull_request.state }}\"}},{\"type\":\"section\",\"text\":{\"type\":\"mrkdwn\",\"text\":\"<${{ github.event.pull_request.html_url }}|Voir la Pull Request>\"}}]}'

```

Alors, que se passe-t-il dans ce qui précède ?

* `name` : nous définissons un nom convivial pour notre workflow
* `on` : nous voulons que notre workflow se déclenche lorsqu'une pull request est créée et cible notre branche `master`
* `jobs` : nous créons un nouveau job appelé `notifySlack`
* `jobs.notifySlack.runs-on` : nous voulons que notre job s'exécute sur une configuration de base de la dernière version d'Ubuntu
* `jobs.notifySlack.steps` : nous n'avons vraiment qu'une seule étape ici - nous utilisons une GitHub Action préexistante appelée [Slack Action](https://github.com/marketplace/actions/post-slack-message) et nous la configurons pour publier une notification sur notre Slack

Il y a deux points ici auxquels nous devons prêter attention, `env.SLACK_BOT_TOKEN` et `with.args`.

Pour que GitHub communique avec Slack, nous aurons besoin d'un jeton. C'est ce que nous définissons dans `env.SLACK_BOT_TOKEN`. Nous avons généré ce jeton dans la première étape. Maintenant que nous allons l'utiliser dans notre configuration de workflow, nous devons [l'ajouter en tant que Secret Git dans notre projet](https://help.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets#creating-encrypted-secrets-for-a-repository).

![Image](https://www.freecodecamp.org/news/content/images/2020/05/github-slack-token-secret.jpg)
_Secrets GitHub incluant SLACK_BOT_TOKEN_

La propriété `with.args` est ce que nous utilisons pour configurer la charge utile à l'API Slack qui inclut l'ID du canal (`channel`) et notre message réel (`blocks`).

La charge utile dans les arguments est convertie en chaîne et échappée. Par exemple, lorsqu'elle est développée, elle ressemble à ceci :

```json
{
  "channel": "[Channel ID]",
  "blocks": [{
    "type": "section",
    "text": {
      "type": "mrkdwn",
      "text": "*Pull Request:* ${{ github.event.pull_request.title }}"
    }
  }, {
    "type": "section",
    "text": {
      "type": "mrkdwn",
      "text": "*Qui ?:*n${{ github.event.pull_request.user.login }}n*État :*n${{ github.event.pull_request.state }}"
    }
  }, {
    "type": "section",
    "text": {
      "type": "mrkdwn",
      "text": "<${{ github.event.pull_request._links.html.href }}|Voir la Pull Request>"
    }
  }]
}

```

_Note : ceci est juste pour montrer à quoi ressemble le contenu, nous devons utiliser le fichier original avec l'argument converti en chaîne et échappé._

De retour à notre fichier de configuration, la première chose que nous définissons est notre ID de canal. Pour trouver notre ID de canal, vous devrez utiliser l'interface web de Slack. Une fois que vous avez ouvert Slack dans votre navigateur, vous voulez trouver votre ID de canal dans l'URL :

```
https://app.slack.com/client/[workspace ID]/[channel ID]

```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/slack-web-channel-id.jpg)
_ID de canal dans l'URL de l'application web Slack_

Avec cet ID de canal, vous pouvez modifier notre configuration de workflow et remplacer `[Channel ID]` par cet ID :

```yaml
with:
  args: '{\"channel\":\"C014RMKG6H2\",...

```

Le reste de la propriété des arguments est la manière dont nous configurons notre message. Il inclut des variables de l'événement GitHub que nous utilisons pour personnaliser notre message. 

Nous n'allons pas nous attarder à le modifier ici, car ce que nous avons déjà enverra un message de pull request de base, mais vous pouvez tester et construire votre propre charge utile avec le [Block Kit Builder](https://app.slack.com/block-kit-builder/) de Slack.

[Suivez avec le commit !](https://github.com/colbyfayock/my-github-actions/commit/e228b9899ef3da218d1a100d06a72259d45ea19e)

### Tester notre workflow Slack

Maintenant que nous avons notre workflow configuré avec notre application Slack, nous sommes enfin prêts à utiliser notre bot !

Pour cette partie, tout ce que nous avons à faire est de créer une nouvelle pull request avec n'importe quel changement que nous voulons. Pour tester cela, j'ai simplement [créé une nouvelle branche](https://github.com/colbyfayock/my-github-actions/pull/2) où j'ai ajouté une phrase au fichier `README.md`.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/github-test-pull-request.jpg)
_Diff de code - [https://github.com/colbyfayock/my-github-actions/pull/2](https://github.com/colbyfayock/my-github-actions/pull/2)_

Une fois que vous [avez créé cette pull request](https://github.com/colbyfayock/my-github-actions/pull/2), similaire à notre workflow de tests, GitHub exécutera notre workflow Slack ! Vous pouvez voir cela s'exécuter dans l'onglet Actions comme avant.

À condition que vous ayez tout configuré correctement, une fois le workflow exécuté, vous devriez maintenant avoir un nouveau message dans Slack de votre nouveau bot.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/slack-github-notification.jpg)
_Message automatisé du bot Slack concernant une nouvelle pull request_

_Note : nous ne fusionnerons pas cette pull request._

## Que pouvons-nous faire d'autre ?

### Personnaliser vos notifications Slack

Le message que j'ai préparé est simple. Il nous dit qui a créé la pull request et nous donne un lien vers celle-ci.

Pour personnaliser la mise en forme et le message, vous pouvez utiliser le [Block Kit Builder](https://app.slack.com/block-kit-builder/) de GitHub pour créer le vôtre.

Si vous souhaitez inclure des détails supplémentaires comme les variables que j'ai utilisées pour la pull request, vous pouvez utiliser les [contextes](https://help.github.com/en/actions/reference/context-and-expression-syntax-for-github-actions#contexts) disponibles de GitHub. Cela vous permet de récupérer des informations sur l'environnement et le job pour personnaliser votre message.

Je n'ai pas réussi à trouver d'exemples de charges utiles, alors voici un exemple de charge utile de contexte `github` à laquelle vous pourriez vous attendre dans l'événement.

[Exemple de contexte github](https://gist.github.com/colbyfayock/1710edb9f47ceda0569844f791403e7e)

### Plus d'actions GitHub

Avec notre capacité à créer de nouveaux workflows personnalisés, il n'y a pas grand-chose que nous ne pouvons pas automatiser. GitHub a même un [marketplace](https://github.com/marketplace?type=actions) où vous pouvez naviguer pour en trouver un.

Si vous vous sentez prêt à aller plus loin, vous pouvez même créer le vôtre ! Cela vous permet de configurer des scripts pour configurer un workflow afin d'effectuer les tâches dont vous avez besoin pour votre projet.

## Rejoignez la conversation !

%[https://twitter.com/colbyfayock/status/1268197100539514881]

## À quoi utilisez-vous les GitHub Actions ?

Partagez avec moi sur [Twitter](https://twitter.com/colbyfayock) !

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Follow Me On Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">?f4f9 Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;"> 2709f4e9 Sign Up For My Newsletter</a>
    </li>
  </ul>
</div>