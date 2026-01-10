---
title: Comment utiliser GitHub Actions pour automatiser le développement d'applications
  Android
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2021-08-16T20:18:40.000Z'
originalURL: https://freecodecamp.org/news/use-github-actions-to-automate-android-development
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/moises-de-paula-HPZZHJ-LuDI-unsplash.jpg
tags:
- name: Android
  slug: android
- name: android app development
  slug: android-app-development
- name: automation
  slug: automation
- name: GitHub Actions
  slug: github-actions
seo_title: Comment utiliser GitHub Actions pour automatiser le développement d'applications
  Android
seo_desc: "There are many repetitive tasks that we have to do every day. And they\
  \ can be a bit boring, difficult, and monotonous. \nBut instead of laboring away\
  \ at those daily tasks, you can delegate them so someone or something else does\
  \ them for you. That way,..."
---

Il existe de nombreuses tâches répétitives que nous devons effectuer chaque jour. Et elles peuvent être un peu ennuyeuses, difficiles et monotones. 

Mais au lieu de peiner sur ces tâches quotidiennes, vous pouvez les déléguer à quelqu'un ou quelque chose d'autre pour les faire à votre place. Ainsi, vous pouvez avoir plus de temps pour faire ce que vous voulez. Vous pouvez avoir du temps pour vous détendre.

Si vous avez déjà développé une application Android, vous savez à quel point certaines tâches peuvent être fastidieuses :

* Exécuter des tests
* Vérifier que l'application compile lors de la fusion de nouveau code
* Construire et publier l'application.

Alors, à qui devrions-nous passer ces tâches ? Un autre collègue ? Ils peuvent simplement les passer à quelqu'un d'autre et cela ne libérera le temps de personne. De plus, nous ne voulons pas ennuyer nos collègues. La solution ?

Dites bonjour à GitHub Actions. 💡

## Qu'est-ce que GitHub Actions ?

GitHub Actions sont des commandes que nous pouvons déclencher lorsqu'un événement se produit dans notre dépôt. Au cœur, une action est un fichier de configuration qui contient une liste de commandes décrivant :

* Ce qui doit se passer
* Quand cela doit se passer

Ce fichier de configuration est au format YAML (.yml) et un exemple ressemble à ceci :

```yaml
name: Mon Action GitHub

on: pull_request

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v1
```

Analysons l'exemple ci-dessus :

1. Nous donnons un nom à notre action (Mon Action GitHub) [**Optionnel]**
2. Nous indiquons quand cette action doit s'exécuter (lorsqu'une pull request est ouverte)
3. Nous commençons une liste de tâches (jobs) qui doivent se produire une fois cette action déclenchée
4. La première est une action de **build**
5. La commande **runs-on** indique à GitHub quel runner exécutera ce job (il s'agit d'un serveur virtuel et vous pouvez choisir entre Windows/Mac/Linux)
6. Chaque job peut avoir plusieurs phases regroupées par le mot-clé **steps**
7. Le mot-clé **uses** indique au script quelle action exécuter

Il s'agit d'un exemple très court qui ne montre pas toutes les fonctionnalités de GitHub Actions, mais il donne un aperçu de la structure du fichier de configuration. 

Dans les sections suivantes, nous créerons des actions qui aideront à maintenir notre cycle de développement efficace et performant.

Notez que tous les fichiers GitHub Actions doivent résider dans le dossier principal de votre projet dans le chemin .github/workflows :

![Image](https://www.freecodecamp.org/news/content/images/2021/08/1_5t9-LbXINncXYPUtYgY0TA.jpeg)

## Comment créer une GitHub Action pour les Pull Requests

Que vous travailliez sur un projet seul ou en équipe, il est crucial de s'assurer que votre application est stable. Il est donc logique de vérifier que votre application compile correctement et que tous les tests passent chaque fois que vous envisagez de fusionner une pull request. 

Nous avons déjà montré dans notre exemple comment extraire le code de notre dépôt. Dans cette action, nous inclurons les étapes suivantes :

1. Configuration de la version du JDK
2. Changement des permissions pour l'environnement virtuel
3. Exécution des tests (si nous en avons)
4. Construction de l'application

```yaml
name: Android Build

on: pull_request

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v1

      - name: Set Up JDK              // 1
        uses: actions/setup-java@v1
        with:
          java-version: 1.8

      - name: Change wrapper permissions  // 2
        run: chmod +x ./gradlew

      - name: Run Tests                   // 3
        run: ./gradlew test

      - name: Build Project               // 4
        run: ./gradlew assemble
```

Vous pouvez voir que ci-dessus, chaque étape a ses propres propriétés et attributs qui lui sont spécifiques. 

Je ne vais pas entrer dans les détails de chacune d'elles, car vous pouvez le faire vous-même via la documentation. Ce qui est commun à la plupart des étapes est le mot-clé **run**. Cet attribut indique quelle commande exécuter.

✨ Nous avons besoin de la deuxième étape pour que l'environnement virtuel puisse exécuter les commandes gradle. Sans cela, il ne pourra pas le faire.

## Comment créer une GitHub Action pour publier une application

Une fois que vous avez publié votre application pour la première fois, la republier devient une sorte de corvée. 

Vous devez vous assurer que la version est mise à jour, construire l'APK, le soumettre via la Google Play Console et d'autres tâches fastidieuses. 

Nous pouvons automatiser ce processus avec une autre GitHub Action. Cette action est un peu plus compliquée que la précédente, car elle nécessite l'utilisation de [GitHub Secrets](https://docs.github.com/en/actions/reference/encrypted-secrets). 

En résumé, GitHub Secrets est un moyen de stocker des informations sensibles en tant que variables d'environnement de votre dépôt. Nous allons en avoir besoin car :

1. Nous devons signer notre application
2. Nous allons donner à cette action la permission de soumettre notre application construite au Google Play Store

Découvrons d'abord comment créer des GitHub Secrets.

* Dans la page principale de votre dépôt, cliquez sur l'onglet **Paramètres**

![Image](https://www.freecodecamp.org/news/content/images/2021/08/1_JVm-YqUz-grjtXl6v1ySsg.jpeg)

* Dans le menu de gauche, il y aura une option intitulée **Secrets**

![Image](https://www.freecodecamp.org/news/content/images/2021/08/1_lAAL2-4XiOyLoaJYutJ4EA.jpeg)

* Pour créer un secret, appuyez sur le bouton **Nouveau secret de dépôt**

![Image](https://www.freecodecamp.org/news/content/images/2021/08/1_MiV5nk7LtM56v6bYcPH_2Q.jpeg)

Maintenant que nous avons réglé cela, examinons le script pour publier une application :

```yaml
name: Android Publish

on:
  workflow_dispatch:

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v1

      - name: Set Up JDK
        uses: actions/setup-java@v1
        with:
          java-version: 1.8

      - name: Change wrapper permissions
        run: chmod +x ./gradlew

      - name: Run Tests
        run: ./gradlew test

      - name: Build Project
        run: ./gradlew build

      - name: Build Release AAB      // 1
        run: ./gradlew bundleRelease

      - name: Sign AAB               // 2
        uses: r0adkll/sign-android-release@v1
        with:
          releaseDirectory: app/build/outputs/bundle/release
          signingKeyBase64: ${{ secrets.SIGN_KEY }}
          alias: ${{ secrets.ALIAS }}
          keyStorePassword: ${{ secrets.STORE_KEY_PASSWORD }}
          keyPassword: ${{ secrets.KEY_PASSWORD }}

      - name: Deploy to Play Store   // 3
        uses: r0adkll/upload-google-play@v1
        with:
          serviceAccountJsonPlainText: ${{secrets.SERVICE_ACCOUNT}}
          packageName: com.tomerpacific.laundry
          releaseFiles: app/build/outputs/bundle/release/app-release.aab
          track: production
```

Vous avez peut-être remarqué que cette action s'exécutera **on workflow_dispatch**. Que signifie cela ? En gros, cela permet à cette action d'être déclenchée manuellement depuis GitHub lui-même. 

Vous pouvez bien sûr décider d'exécuter cette action lorsqu'un push se produit sur la branche principale (par exemple).

L'étape marquée avec 1 dans l'extrait ci-dessus déclenche la construction d'un .aab de notre application. Ensuite, comme nous le ferions si nous le construisions dans Android Studio, nous devons signer ce fichier .aab. 

C'est la première fois que les GitHub Secrets entrent en jeu. Nous devons créer des secrets pour :

* La clé de signature (secrets.SIGN_KEY)
* L'alias de la clé (secrets.ALIAS)
* Le mot de passe de la clé du magasin (secrets.STORE_KEY_PASSWORD)
* Le mot de passe de la clé (secrets.KEY_PASSWORD)

Une fois que nous avons signé le fichier .aab, nous pouvons le déployer sur le Google Play Store. À cette étape, il y a un peu plus de travail à faire, car nous devons permettre à cette GitHub Action la permission de déployer des applications pour nous sur Google Play. Mais, attendez, comment faisons-nous cela ? Nous utilisons un [Compte de service](https://cloud.google.com/compute/docs/access/service-accounts).

### Comment créer un compte de service

> Un compte de service est une entité que vous créez pour indiquer aux services ou applications avec lesquels il interagit qu'il opère en votre nom.

Dans notre cas, notre GitHub Action va interagir avec le Google Play Store pour pouvoir télécharger une nouvelle version de notre application. 

Pour créer un compte de service, allez dans la Google Cloud Console. Si vous n'avez pas de compte là-bas, assurez-vous d'en créer un. Ensuite, sur la page principale, dans le menu de gauche, il y aura un élément de liste intitulé Comptes de service.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/1_5MKbbfXd8BzFywlBzsWytw.jpeg)

Une fois que vous avez cliqué dessus, sur le côté droit de la fenêtre, vous verrez les comptes de service que vous avez déjà. 

Nous voulons en créer un nouveau et dans la partie supérieure de la fenêtre, il y a un bouton pour le faire.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/1_em9j6HfzBMlG603v0O6SzA.jpeg)

Dans la fenêtre qui s'ouvre, vous devrez entrer le nom du service et vous pouvez également entrer une description.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/1_E1b3hZk9hS7PX4mM9LhJJA.jpeg)

Le nom donné ici sera l'identifiant unique de ce compte de service. 

Dans la deuxième étape, vous devrez donner un rôle à ce compte de service. Dans le menu déroulant **Sélectionner un rôle**, choisissez Basic → Éditeur.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/1_GPvZUINPACbTwH5jWNh-4w.jpeg)

Enfin, dans la troisième étape, remplissez votre email dans les deux champs sous la section "Accorder aux utilisateurs l'accès à ce compte de service" :

![Image](https://www.freecodecamp.org/news/content/images/2021/08/1_ARhcPbB3VgC-_-e-AQrCTg.jpeg)

Après avoir appuyé sur le bouton terminé, vous devrez créer une clé pour ce compte de service. L'action utilisera cette clé pour être identifiée par Google Play. 

Pour créer la clé, cliquez sur les trois points horizontaux sous l'étiquette Actions dans l'écran principal du compte de service. Dans le menu qui apparaît, sélectionnez **Gérer les clés**.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/1_n9gKn2b4xP3_SnOcVxsYhQ.jpeg)

Dans cette fenêtre, nous créerons une clé en sélectionnant le bouton **Nouvelle clé** et en choisissant "Créer une nouvelle clé" dans le menu qui apparaît.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/1_zkDo3a1b8Rw487u1SemAWQ.jpeg)

Nous avons maintenant l'option de choisir le format de notre nouvelle clé – le format par défaut est JSON et nous le laisserons sélectionné. Cliquez sur créer.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/1_17x3W1mL8nFC8I8WsPci0A.jpeg)

Une fois que vous avez fait cela, un fichier sera téléchargé sur votre ordinateur. Assurez-vous de conserver ce fichier car il contient toutes les données pertinentes pour votre compte de service et vous ne pourrez pas le télécharger à nouveau. 

Nous prendrons le contenu de ce fichier et créerons un secret GitHub avec (**secrets.SERVICE_ACCOUNT**).

Dernier point mais non des moindres, nous devons informer Google Play de ce compte de service. Pour ce faire, nous devons nous connecter à notre compte Google Play Console et nous rendre dans **Configuration → Accès API**. 

Si vous faites défiler la page, vous verrez une section intitulée Comptes de service. Vous devriez pouvoir voir le compte de service que vous avez créé précédemment. Cliquez sur le lien Accorder l'accès

![Image](https://www.freecodecamp.org/news/content/images/2021/08/1_bONaGlfRFYGPi2i3vJUntg.jpeg)

Dans les paramètres qui s'ouvrent, rendez-vous dans les permissions de l'application. Ici, vous choisirez avec quelle application ce compte de service interagit. 

Sous les permissions du compte, tout ce qui se trouve sous la section **releases** doit être coché. Je vous conseille vivement de regarder tous les autres paramètres et de décider vous-même ce que vous voulez laisser coché ou ce que vous voulez décocher. 

Une fois que vous avez terminé, cliquez sur le bouton **Inviter l'utilisateur** situé dans le coin inférieur droit.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/1_0ez0QuP59YwonfFePbjvzQ.jpeg)

Après l'envoi de l'invitation, nous pouvons exécuter l'action de publication vers le magasin.

## Comment surveiller nos actions dans GitHub

Pour voir quelles actions sont définies pour votre dépôt, cliquez sur l'onglet Actions. Cet onglet présente tous les workflows définis et ceux qui ont déjà été exécutés.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Workflows.jpg)

Sur le côté gauche, vous pouvez voir toutes les actions qui ont été définies et sur le côté droit, vous pouvez voir toutes les actions qui ont été exécutées. Si vous souhaitez consulter une action spécifique, vous pouvez cliquer dessus.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/workflow.jpg)

Si l'action est définie pour s'exécuter sur **workflow_dispatch**, vous verrez un bouton vous permettant de l'exécuter (comme sur l'image ci-dessus). 

Si vous souhaitez voir une exécution spécifique d'un workflow, vous pouvez également le faire depuis la page principale des Workflows en cliquant sur l'une des exécutions. Si l'une des actions échoue à s'exécuter, ce serait l'endroit pour enquêter et voir ce qui s'est mal passé. 

Notre première action est censée être déclenchée lorsqu'une pull request est ouverte. Si elle fonctionne correctement, vous devriez voir ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/08/pr.jpg)

Et voilà !

## Conclusion

Cela a été une longue lecture jusqu'à ce point, mais nous avons passé en revue tout ce dont vous avez besoin pour commencer à créer un pipeline d'intégration continue et de déploiement continu pour vos applications. 

Si vous êtes intéressé à voir comment les GitHub Actions sont configurées, vous pouvez les consulter dans l'un de mes dépôts ici :

%[https://github.com/TomerPacific/LaundrySymbols/actions]

Pour en savoir plus sur GitHub Actions, rendez-vous ici :

%[https://docs.github.com/en/actions]