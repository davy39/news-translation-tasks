---
title: Comment nous avons utilisé CircleCI 2.0 pour construire et déployer une application
  Angular sur AWS S3
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-19T15:41:37.000Z'
originalURL: https://freecodecamp.org/news/our-journey-for-using-circleci-2-0-to-build-and-deploy-an-angular-app-to-aws-s3-8e7ea3f51503
coverImage: https://cdn-media-1.freecodecamp.org/images/1*EgHXd1qjY6PMLQrj6wj1VA.jpeg
tags:
- name: Devops
  slug: devops
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment nous avons utilisé CircleCI 2.0 pour construire et déployer une
  application Angular sur AWS S3
seo_desc: 'By Marius Lazar

  In today’s world, continuous integration and deployment (CI & CD) is a very common
  practice and an important part in any application life cycle. If you want to avoid
  spending valuable time on tasks that you can actually automate, keep...'
---

Par Marius Lazar

Dans le monde d'aujourd'hui, l'intégration et le déploiement continus (CI & CD) sont des pratiques très courantes et constituent une partie importante du cycle de vie de toute application. Si vous voulez éviter de passer un temps précieux sur des tâches que vous pouvez réellement automatiser, continuez votre lecture.

Dans ce tutoriel, je vais vous guider à travers les étapes que nous avons suivies pour intégrer un pipeline CI & CD dans le processus de développement de l'une de nos applications Angular en utilisant CircleCI 2.0 et AWS S3.

### Prérequis

Avant de commencer ce tutoriel, je suppose que vous disposez des éléments suivants :

* Un compte CircleCI
* Un compte AWS avec les droits nécessaires pour créer de nouveaux utilisateurs
* Un Bucket AWS S3
* Un dépôt Bitbucket ou GitHub contenant votre projet
* Une tasse de café — vous savez… pour rester au chaud et concentré :)

### Configuration de CircleCI

Au travail. Pour configurer CircleCI, vous devez créer un nouveau dossier à la racine de votre projet appelé `.circleci` (notez le point) et y ajouter un fichier `config.yml`. Laissez-le vide pour l'instant.

Allez sur l'[interface de CircleCI](https://circleci.com/dashboard) et ajoutez votre projet en allant dans l'onglet `Projects > Add Project`. CircleCI devrait déjà avoir trouvé tous vos dépôts publics. Sélectionnez votre projet et appuyez sur le bouton `Setup project`.

Sélectionnez les options qui vous conviennent le mieux (Linux/Platform 2.0/Node dans notre cas), copiez l'exemple de configuration généré en bas de la page dans votre propre fichier de configuration, et poussez les modifications vers votre dépôt. Vous pouvez maintenant appuyer sur le bouton `Start building`.

Vous pouvez trouver un gist avec la configuration finale [ici](https://gist.github.com/mariuslazar93/beefd809071015cff3689648185c8fa0).

### Comprendre le fichier de configuration CircleCI

Le cœur de ce tutoriel est de comprendre comment utiliser le fichier de configuration CircleCI. Il comporte 3 composants principaux : une version, une liste de jobs et une liste de workflows.

La version est assez évidente. C'est la version de CircleCI que nous allons utiliser.

Ensuite, nous avons la liste des jobs. Vous pouvez considérer un job comme un environnement indépendant pour exécuter une liste de commandes ou de **steps** (étapes). Les tâches courantes que vous pouvez accomplir au sein d'un job incluent :

* Installer les outils dont vous avez besoin pour exécuter/construire/tester votre projet
* Exécuter des commandes bash
* Stocker ou restaurer des éléments du cache CircleCI

Ensuite, nous avons la liste des workflows. Un workflow est un moyen de gérer vos jobs. Disons que vous avez besoin qu'un job ne s'exécute que sur des branches spécifiques ou à des moments précis, ou que vous voulez que certains jobs s'exécutent en parallèle et d'autres en séquence. C'est à cela que servent les workflows.

Une structure de base de configuration CircleCI :

Dans notre cas, nous avons deux jobs : **le job de build** et **le job de déploiement**. Je décrirai chacun d'eux dans les sections suivantes, mais pour l'instant, voyons quels attributs nous allons utiliser pour chacun des jobs :

* L'attribut **docker** — spécifie une image Docker utilisée pour créer le conteneur de l'environnement. CircleCI propose une liste d'images pré-construites que vous pouvez trouver [ici](https://circleci.com/docs/2.0/circleci-images/)
* L'attribut **working_directory** — le répertoire courant qui sera l'endroit où toutes les étapes s'exécuteront
* L'attribut **steps** — une liste d'étapes (commandes) que vous souhaitez exécuter dans le job actuel

Il existe quelques types d'étapes que nous allons utiliser dans notre configuration :

* L'étape **checkout** — utilisée pour récupérer le code de la branche actuelle dans le répertoire de travail
* L'étape **run** — utilisée pour exécuter une commande bash. Vous pouvez spécifier un nom descriptif que vous verrez dans l'interface de CircleCI
* L'étape **save_cache** — utilisée pour stocker un cache d'un fichier ou d'un répertoire dans le stockage CircleCI. Un cas d'utilisation courant consiste à n'installer les dépendances npm qu'une seule fois, puis à mettre en cache le dossier _node_modules_ en utilisant un hash du fichier package.json comme clé de cache
* L'étape **restore_cache** — utilisée pour restaurer un élément mis en cache à l'aide de la clé de cache

Chaque job a accès à certaines variables d'environnement prédéfinies. Vous pouvez consulter la liste complète [ici](https://circleci.com/docs/2.0/env-vars/#circleci-environment-variable-descriptions). Vous pouvez également configurer des variables d'environnement depuis l'interface de CircleCI ou comme attribut de job, mais dans ce tutoriel, nous n'utiliserons que les variables d'environnement suivantes :

* CIRCLE_BRANCH — représente la branche actuelle
* CIRCLE_SHA1 — représente un hash du commit actuel

### Configuration du pipeline CI

Le pipeline CI sera responsable de la construction, du linting et des tests du code source. Ces trois processus seront regroupés dans un seul job appelé **le job de build**.

Vous pouvez jeter un coup d'œil rapide au job de build final ci-dessous, mais je vais détailler chaque étape séparément afin que nous puissions en apprendre un peu plus sur ce qui s'y passe.

1. Nous commençons par récupérer le code de la branche actuelle

```
# Récupérer le code de la branche dans le working_directory
- checkout
```

2. Nous affichons la branche actuelle à des fins de débogage

```
# Afficher la branche actuelle
- run:
    name: Show current branch
    command: echo ${CIRCLE_BRANCH}
```

3. Nous restaurons le dossier _node_modules_ depuis le cache s'il existe. Vous pouvez jeter un œil à l'_étape 5_ pour voir comment il a été sauvegardé.

```
# Restaurer les dépendances locales depuis le cache
- restore_cache:
    keys:
        - v1-dependencies-{{ checksum "package.json" }}
        - v1-dependencies-
```

Vous remarquerez que nous utilisons deux clés de cache. **Une clé est un modèle pour rechercher un élément mis en cache.** La première est spécifique au fichier _package.json_ actuel et la seconde est plus générique et correspond à tous les dossiers _node_modules_ précédemment mis en cache.

Au cas où le cache spécifique n'existerait pas, nous allons chercher n'importe quel dossier _node_modules_ précédemment mis en cache et le restaurer à la place. C'est utile lorsque seules certaines de nos dépendances ont été mises à jour, car nous n'avons pas besoin de télécharger et d'installer toute la liste des dépendances. Nous ne le ferons que pour les paquets mis à jour et restaurerons les paquets inchangés depuis le cache.

4. Nous installons les dépendances du projet. Si ces dépendances ont déjà été restaurées depuis le cache, cette étape sera très rapide. Sinon, cela peut prendre jusqu'à quelques minutes. C'est pourquoi la mise en cache est importante. Elle vous fait gagner du temps et de l'argent.

```
# Installer les dépendances du projet
- run:
    name: Install local dependencies
    command: npm install
```

5. Nous mettons en cache le dossier _node_modules_ au cas où il n'existerait pas. Gardez à l'esprit qu'un cache est immuable, donc **il ne sera pas écrasé** s'il existe déjà.

```
# Mettre en cache les dépendances locales si elles n'existent pas
- save_cache:
    key: v1-dependencies-{{ checksum "package.json" }}
    paths:
        - node_modules
```

Un nouveau cache sera généré avec les dossiers/fichiers spécifiés dans l'attribut **paths** chaque fois que quelque chose est modifié dans le fichier package.json. La clé du cache est générée à l'aide de la fonction checksum, qui produira un hash encodé en base64 du contenu du fichier package.json.

Une technique couramment utilisée consiste à préfixer votre clé de cache avec un numéro de version, de sorte que chaque fois que vous souhaitez régénérer vos caches, il vous suffit de changer le numéro de version.

6. Nous exécutons les commandes de lint et de test. Il est probablement utile de noter que si l'une des étapes échoue, l'ensemble du build échouera.

```
# Vérifier la qualité du code source (linting)
- run:
    name: Linting
    command: npm run lint
```

```
# Tester le code source
- run:
    name: Testing
    command: npm run test
```

7. Nous exécutons la commande de build. Notez que nous allons utiliser une commande multi-lignes, chaque ligne s'exécutant dans le même shell, nous commençons donc la commande par le caractère pipe (|).

Nous vérifions le nom de la branche actuelle et exécutons le script npm correspondant pour construire le projet. Nous faisons cela parce que nous avons des configurations différentes basées sur l'environnement. Les fichiers résultants seront enregistrés dans le dossier _dist_.

```
# Construire le projet avec une configuration différente basée sur
# la branche actuelle
- run:
    name: Building
    command: |
        if [ "${CIRCLE_BRANCH}" == "staging" ]; then
            npm run build-qa
        elif [ "${CIRCLE_BRANCH}" == "master" ]; then
            npm run build-prod
        else
            npm run build-dev
        fi
```

8. Enfin, nous sauvegardons le dossier _dist_ dans le cache afin de pouvoir le restaurer plus tard dans le job de déploiement. Nous utilisons à la fois les variables d'environnement **CIRCLE_BRANCH** et **CIRCLE_SHA1** pour générer une clé de cache unique qui n'existe pas encore dans le cache.

Remarquez que nous ne sommes pas dans une commande shell, nous devons donc récupérer ces variables à partir de la variable `.Environment`.

```
# Mettre en cache le dossier dist pour le job de déploiement
- save_cache:
    key: v1-dist-{{ .Environment.CIRCLE_BRANCH }}-{{ .Environment.CIRCLE_SHA1 }}
    paths:
        - dist 
```

En note complémentaire, nous avons d'abord essayé d'installer angular-cli globalement et de le mettre en cache pour une utilisation ultérieure, mais l'installation prenait jusqu'à 30 secondes même lorsqu'elle était mise en cache. Nous avons donc décidé de créer quelques scripts npm pour exécuter les commandes ng en utilisant l'angular-cli local.

```
"scripts": {
  "ng": "ng",
  "start": "ng serve --env=local",
  "build": "ng build",
  "test": "ng test",
  "lint": "ng lint",
  "e2e": "ng e2e",
  "build-dev": "ng build --target=development --environment=dev",
  "build-qa": "ng build --target=production --environment=qa",
  "build-prod": "ng build --prod"
}
```

Et voilà ! Nous avons maintenant un pipeline CI fonctionnel. Vous devriez pouvoir enregistrer cela dans votre propre fichier de configuration, le pousser vers votre dépôt et vérifier si tout fonctionne comme prévu.

Au cas où vous vous poseriez la question, vous n'avez pas besoin de workflow pour exécuter un job. Par défaut, chaque job se déclenchera lorsque vous pousserez une modification.

### Configuration du pipeline CD

Le pipeline CD sera responsable du déploiement des fichiers de distribution résultant du job de build vers un bucket AWS S3. Devinez quoi ? Nous allons appeler cela **le job de déploiement**.

Avant de pouvoir continuer, nous devons donner à CircleCI les permissions d'accéder au Bucket AWS S3.

Tout d'abord, nous allons créer un nouvel utilisateur IAM dans la console de gestion AWS. Allez dans `Services > IAM > Users > Add User`. Donnez-lui un nom et sélectionnez la case **Programmatic access** pour le type d'accès.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fmO8C1uuqll7D2E4Wj05TA.png)
_Configuration de l'accès programmatique pour un nouvel utilisateur_

Cliquez sur `Next`. Nous devons maintenant donner des permissions à l'utilisateur. Dans notre cas, nous avons seulement besoin que l'utilisateur _circleci_ puisse lire/écrire dans un Bucket AWS S3. Recherchez et sélectionnez la politique **AmazonS3FullAccess**, puis appuyez sur le bouton `Create user`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6Yruj4AdYI4aAbPNzo383g.png)
_Sélection des permissions de l'utilisateur_

Sur la page suivante, vous aurez un **Access key ID** et une **Secret access key** pour le nouvel utilisateur. Gardez cette page ouverte et allez sur l'interface de CircleCI. Allez dans les paramètres du projet et recherchez **AWS Permissions**. Vous devrez utiliser les clés générées précédemment ici.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_X-b93Ssnh0kapIVRyw9aA.png)
_Configuration des permissions AWS d'un projet CircleCI_

Une fois cela fait, nous pouvons continuer avec notre job de déploiement.

Comme précédemment, vous trouverez le job de déploiement final ci-dessous. Mais je vais discuter de chaque étape séparément, même si elles sont assez simples cette fois-ci.

1. Nous commençons par afficher le nom de la branche à des fins de débogage.

```
# Afficher la branche actuelle
- run:
    name: Show current branch
    command: echo ${CIRCLE_BRANCH}
```

2. Nous restaurons le dossier _dist_ mis en cache lors du job de build.

```
# Restaurer le cache du job de build qui contient le
# dossier dist à déployer
- restore_cache:
    key: v1-dist-{{ .Environment.CIRCLE_BRANCH }}-{{ .Environment.CIRCLE_SHA1 }}
```

3. Nous installons l'aws cli en utilisant les droits _sudo_.

```
# Installer l'aws cli
- run:
    name: Install aws cli
    command:
        sudo apt-get -y -qq install awscli
```

4. Nous exécutons la commande de déploiement qui va déployer le code du dossier _dist_ vers le Bucket AWS S3 correspondant à l'environnement actuel. Nous avons à nouveau une commande multi-lignes, nous devons donc commencer par le caractère pipe (|).

```
# Déployer vers le bucket S3 correspondant à la branche actuelle
- run:
    name: Deploy to S3
    command: |
        if [ "${CIRCLE_BRANCH}" == "develop" ]; then
            aws s3 sync dist s3://project-dev/ --delete
        elif [ "${CIRCLE_BRANCH}" == "staging" ]; then
            aws s3 sync dist s3://project-qa/ --delete
        elif [ "${CIRCLE_BRANCH}" == "master" ]; then
            aws s3 sync dist s3://project/ --delete
        fi
```

La signature pour déployer vers un Bucket AWS S3 en utilisant l'aws cli est la suivante :

```
aws s3 sync <% path-to-folder %> s3://<% bucket-name %>/ --delete
```

Le flag delete videra le bucket avant de déployer tout fichier.

Encore une chose. Ou peut-être deux… Nous avons rencontré 2 erreurs après avoir mis en place cette configuration. Elles ne sont peut-être pas applicables dans votre cas, mais je vous en donne quand même un court résumé.

1. La région du Bucket S3 n'était pas spécifiée.

> A client error (PermanentRedirect) occurred when calling the ListObjects operation: The bucket you are attempting to access must be addressed using the specified endpoint. Please send all future requests to this endpoint.

Pour résoudre cette erreur, nous avons dû ajouter la région du bucket à la commande de déploiement :

```
aws --region eu-west-2 s3 sync <% path %> s3://<% bucket-name %>/
```

2. L'autorisation pour le Bucket S3 utilisait un ancien protocole qui n'est pas supporté par le bucket actuel.

> A client error (InvalidRequest) occurred when calling the ListObjects operation: The authorization mechanism you have provided is not supported. Please use AWS4-HMAC-SHA256.

Pour résoudre cette erreur, nous avons dû définir le mécanisme d'autorisation pour l'authentification d'une requête AWS S3 afin d'utiliser la Signature Version 4 avant d'exécuter l'étape de déploiement :

```
# Définir la version de signature pour l'authentification S3
- run:
    name: Setting Signature Version 4 for S3 Request Authentication
    command: aws configure set default.s3.signature_version s3v4
```

C'est tout ! Nous avons maintenant un pipeline CD fonctionnel. Seul un petit problème… Il s'exécutera à chaque push. Configurons donc un workflow pour résoudre cela.

### Mettre les jobs CI & CD dans un workflow

Dans notre cas, nous voulons exécuter le job de build à chaque commit et le job de déploiement uniquement lorsque nous commitons sur les branches develop, staging ou master. Un workflow, par défaut, est déclenché par un push sur n'importe quelle branche.

Nous voulions en fait que le job de build ne s'exécute que lorsque nous faisons une Pull Request (PR), et cela est possible en allant dans les Paramètres Avancés de votre projet CircleCI et en activant l'option `Only build pull requests`.

Mais le problème survient lorsque vous devez exécuter le workflow sur une PR et aussi sur les branches develop, staging et master. Nous n'avons pas trouvé comment faire fonctionner cela. Mais si vous avez des suggestions, n'hésitez pas à me laisser un commentaire !

Revenons à notre configuration de workflow. Elle est assez explicite :

Vous pouvez voir que nous avons défini le workflow `build_and_deploy` qui contient… les jobs de build et de déploiement. Le job de build n'a aucune restriction, il s'exécutera donc chaque fois que le workflow s'exécutera.

D'un autre côté, le job de déploiement a une propriété `require` pour le job de build, ce qui signifie qu'il ne s'exécutera que si le job de build réussit. Il possède également un attribut `filter` qui est utilisé pour sélectionner les branches sur lesquelles il s'exécutera.

Avec cette configuration en place, nous avons limité l'exécution du job de déploiement aux branches develop, staging et master uniquement lorsque le job de build est réussi, ce qui est exactement ce que nous voulions.

C'est à peu près tout. Un gist avec l'intégralité de la configuration peut être trouvé [ici](https://gist.github.com/mariuslazar93/beefd809071015cff3689648185c8fa0).

### Fonctionnalité bonus

Si vous êtes comme nous et que vous aimez savoir ce qui se passe avec votre projet, vous serez heureux d'apprendre qu'il existe une application CircleCI pour Slack qui peut être configurée pour vous donner des alertes en temps réel lorsqu'un build réussit ou échoue. C'est agréable à avoir.

### Dernières réflexions

Je sais que cela peut être intimidant, mais n'ayez pas peur d'intégrer un pipeline CI & CD dans votre projet. Cela prendra un peu de temps avant d'obtenir la bonne configuration, mais cela en vaut la peine !

Si vous pensez que cet article vous a été utile, n'hésitez pas à le recommander et à le partager !

Merci de m'avoir lu ! Si vous avez des commentaires ou des questions, n'hésitez pas à me contacter ! Je suis toujours ravi d'aider :)