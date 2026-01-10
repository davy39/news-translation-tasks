---
title: Déploiement continu pour Node.js sur la plateforme Google Cloud
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-15T01:19:51.000Z'
originalURL: https://freecodecamp.org/news/continuous-deployment-for-node-js-on-google-cloud-platform-751a035a28d5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*PsecxPuZQn0kVxC04OPU8Q.jpeg
tags:
- name: Continuous Integration
  slug: continuous-integration
- name: Google Cloud Platform
  slug: google-cloud-platform
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: 'tech '
  slug: tech
seo_title: Déploiement continu pour Node.js sur la plateforme Google Cloud
seo_desc: 'By Gautam Arora

  Google Cloud Platform (GCP) provides a host of options for Node developers to easily
  deploy our apps. Want a managed hosting solution like Heroku? App Engine, check!
  Want to host a containerized app? Kubernetes Engine, check! Want to ...'
---

Par Gautam Arora

[Google Cloud Platform (GCP)](https://cloud.google.com/) offre une multitude d'options pour les développeurs [Node](https://nodejs.org/en/) afin de déployer facilement nos applications. Vous voulez une solution d'hébergement gérée comme Heroku ? [App Engine](https://cloud.google.com/appengine/), c'est fait ! Vous voulez héberger une application conteneurisée ? [Kubernetes Engine](https://cloud.google.com/kubernetes-engine/), c'est fait ! Vous voulez déployer une application serverless ? [Cloud Functions](https://cloud.google.com/functions/), c'est fait !

Récemment au travail, j'ai pris plaisir à utiliser notre [service de déploiement continu interne](https://technology.condenast.com/story/departures-building-a-docker-container-based-deployment-platform-at-conde-nast) qui construit, teste et déploie rapidement les nouveaux commits poussés sur GitHub. Alors quand j'ai lu à propos du nouveau service [Cloud Build](https://techcrunch.com/2018/07/24/google-announces-cloud-build-its-new-continuous-integration-continuous-delivery-platform/) de Google, j'ai voulu l'essayer et voir si je pouvais recréer une expérience de déploiement tout aussi fluide pour moi-même. De plus, lors d'une conversation avec [Fransizka](https://twitter.com/fhinkel) de l'équipe Google Cloud, elle a identifié ce domaine comme un sujet où un tutoriel serait utile. Alors c'est parti...

### Mais attendez, qu'est-ce que Cloud Build ?

Cloud Build est un service de build géré dans GCP qui peut extraire du code à partir de diverses sources, exécuter une série d'étapes de build pour créer une image de build pour l'application, puis déployer cette image sur une flotte de serveurs.

Cloud Build fonctionne bien avec le propre dépôt de code source de Google, Bit Bucket ou GitHub. Il peut créer une image de build en utilisant un fichier de configuration Docker (`Dockerfile`) ou le propre fichier de configuration de Cloud Build (`cloudconfig.yaml`). Il peut déployer des applications (et des API) sur App Engine, Kubernetes Engine et Cloud Functions. Une fonctionnalité vraiment cool est Build Triggers. Ceux-ci peuvent être configurés pour surveiller un nouveau commit dans le dépôt de code et déclencher un nouveau build et déploiement.

#### Avant de plonger dans le grand bain...

Cet article partage les étapes détaillées et le code pour configurer le déploiement continu des applications Node sur GCP. Il suppose que vous êtes familier avec le développement d'applications Node simples, le travail avec la ligne de commande, et que vous avez une compréhension générale du déploiement d'applications sur des services cloud comme Heroku, AWS, Azure ou GCP.

Pour chaque section, un dépôt de code GitHub est fourni pour que vous puissiez suivre. Ne vous inquiétez pas cependant — n'hésitez pas à parcourir l'article pour apprendre les idées générales, et vous pouvez le mettre en favoris et y revenir plus tard si vous prévoyez de configurer cela. Le vrai plaisir d'avoir une configuration comme celle-ci est que vous pouvez déployer des applications rapidement.

### Déploiement continu pour App Engine Standard

Déployer une application Node sur App Engine est assez simple. Créez un nouveau projet dans Google Cloud Console, ajoutez un fichier de configuration `app.yaml` dans notre répertoire de code (qui décrit le runtime node que nous voulons utiliser — j'ai utilisé Node 8), et exécutez `gcloud app deploy` sur notre terminal — et c'est fait !

Si vous voulez essayer cela par vous-même, voici quelques ressources :

* [Application d'exemple pour App Engine](https://github.com/gautamarora/gae-node-hello-world)
* [Guide de démarrage rapide pour Node sur App Engine](https://cloud.google.com/appengine/docs/standard/nodejs/quickstart)

Donc, ce que nous avons fait jusqu'à présent en suivant le guide de démarrage rapide ci-dessus :

1. Créé un nouveau projet dans Google Cloud Console
2. Déployé notre application Node sur App Engine en utilisant _gcloud app deploy_

...maintenant, comment pouvons-nous automatiser la configuration de sorte que les modifications de code soient déployées automatiquement lors d'un push vers GitHub ?

Voici ce que nous devons faire :

1. Mettre notre code sur GitHub

* Rendez-vous sur GitHub pour créer un nouveau dépôt
* Suivez ensuite les instructions pour pousser le code de votre machine vers GitHub

2. Activer Cloud Build

* [Activer l'API Cloud Build](https://console.cloud.google.com/flows/enableapi?apiid=cloudbuild.googleapis.com&redirect=https://cloud.google.com/cloud-build/docs/quickstart-gcloud&_ga=2.113783623.-1976915987.1533866140) pour notre projet
* [Activer l'API App Engine](https://console.cloud.google.com/flows/enableapi?apiid=appengine.googleapis.com&_ga=2.114826311.-1976915987.1533866140) pour notre projet.
* Accorder l'IAM App Engine au compte de service Cloud Build en allant sur la page [IAM](https://console.cloud.google.com/iam-admin/iam), trouvez ce compte de service `<project-id>@cloudbuild.gserviceaccount.com`, modifiez-le et donnez-lui le rôle d'administrateur App Engine.

3. Créer un [fichier de configuration Cloud Build](https://cloud.google.com/cloud-build/docs/build-config)

* Créez un nouveau fichier `cloudbuild.yaml` qui ressemble à ceci :

```
steps:
  - name: 'gcr.io/cloud-builders/npm'
    args: ['install']
  - name: 'gcr.io/cloud-builders/npm'
    args: ['test']
  - name: "gcr.io/cloud-builders/gcloud"
    args: ["app", "deploy"]
timeout: "1600s"
```

Cette configuration comporte trois étapes de build (chaque ligne commençant par un tiret est une étape de build) qui exécuteront `npm install`, puis `npm test` et, si tout est bon, déployeront notre code sur App Engine.

Chaque étape de build est simplement comme une commande que nous exécutons sur notre machine. Mais dans ce cas, comme ce fichier est en yaml et que chaque étape est divisée sur 2 lignes de nom et d'args, cela peut sembler un peu déroutant.

Essayons ceci : pour la ligne commençant par « name », lisez son dernier mot puis lisez les valeurs dans la ligne « args ». J'espère que ce fichier a plus de sens maintenant !

4. Exécuter un Build manuellement (optionnel, juste pour vérification)

* Nous pouvons maintenant déployer notre application depuis notre machine en utilisant Cloud Build
* Exécutez la commande cloud build sur votre terminal : `gcloud builds submit --config cloudbuild.yaml .`

Cette commande démarre un build sur Cloud Build en utilisant le fichier de configuration que nous avons créé ci-dessus.

* Rendez-vous sur la page [Cloud Builds](https://console.cloud.google.com/cloud-build/builds) pour voir le build en cours.
* Attendez la fin du build, puis testez votre application Node en utilisant l'URL App Engine pour cette application.
* Vous pouvez apporter des modifications à votre application Node et appeler à nouveau cette commande pour démarrer plus de builds si vous le souhaitez.

5. Créer un Build Trigger

* Rendez-vous sur la page [Cloud Build Triggers](https://console.cloud.google.com/cloud-build/triggers) et sélectionnez Créer un Trigger
* Sur la page de configuration du Build Trigger, choisissez GitHub comme dépôt de code source. Cela nécessitera que vous autorisiez GCP à accéder à vos dépôts GitHub, ce que vous devrez approuver. Une fois cela fait, sélectionnez le dépôt GitHub pour votre application Node que vous avez poussé sur GitHub précédemment.
* Créez un trigger nommé `déploiement continu`, et pour le type de trigger, choisissez Branch avec regex pour le nom de la branche comme `master`. Cela garantira que les builds, tests et déploiements ne s'exécuteront que pour les push vers la branche master et non pour n'importe quelle branche.
* Pour le fichier de configuration du build, sélectionnez `cloudbuild.yaml`
* Cliquez maintenant sur le bouton Build Trigger

6. Exécuter un Build automatiquement en poussant un commit vers GitHub

* Avec notre build trigger créé, faites un simple commit sur votre application node, comme changer « Hello, World! » en « Hello, GCP! » et commitez et poussez ce code vers GitHub
* Retournez sur la page [Cloud Builds](https://console.cloud.google.com/cloud-build/builds) et vous remarquerez qu'un build a été déclenché automatiquement (si ce n'est pas le cas, donnez-lui quelques secondes de plus ou cliquez sur le bouton de rafraîchissement de la page)
* Une fois le build terminé et que vous voyez une coche verte, vous pouvez visiter votre application en utilisant son URL App Engine et voir que vos modifications sont maintenant en ligne !

Voici une capture d'écran des builds déclenchés par un push GitHub pour notre application :

![Image](https://cdn-media-1.freecodecamp.org/images/BwblpfTf5PSxQ4rXkzWshokcpg5iQJJEsThF)

Trop beau pour être vrai ?? Exécutez cette dernière étape quelques fois pour la tester quelques fois de plus. Notre première application est maintenant déployée sur App Engine à chaque commit sur master ?

![Image](https://cdn-media-1.freecodecamp.org/images/U057rpI1bqLVgfjn5DFIEZV-niVp6HY05VQ9)
_Photo par [Unsplash](https://unsplash.com/photos/g5FyZvIzUS4?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Willian Justen de Vasconcellos</a> sur <a href="https://unsplash.com/search/photos/shipping?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

### Déploiement continu pour Kubernetes Engine

Super, nous avons configuré notre application pour qu'elle se déploie sur App Engine lors d'un push GitHub, mais que faire si nous voulions la même configuration pour nos applications conteneurisées ? Essayons !

À un niveau élevé, le déploiement d'une application Node sur Kubernetes Engine comporte deux tâches principales. Premièrement, préparer notre application : conteneuriser l'application avec Docker, la construire et pousser l'image Docker vers Google Container Registry. Ensuite, configurer les choses du côté GCP : créer un cluster Kubernetes, créer un déploiement avec votre image d'application, puis créer un service pour permettre l'accès à votre application en cours d'exécution.

Si vous voulez essayer cela par vous-même, voici quelques ressources :

* [Application d'exemple pour Kubernetes Engine](https://github.com/gautamarora/gke-node-hello-world)
* [Conteneuriser une application Node avec Docker](https://nodejs.org/en/docs/guides/nodejs-docker-webapp/)
* [Déployer une application Hello World conteneurisée sur Kubernetes Engine](https://github.com/gautamarora/gke-node-hello-world/blob/master/DEPLOY.md#deploy-a-containerized-hello-world-application-to-kubernetes-engine)

Donc, ce que nous avons fait jusqu'à présent en utilisant les guides ci-dessus :

1. Créé un autre nouveau projet dans Google Cloud Console
2. Créé un cluster Kubernetes, un déploiement et un service
3. Déployé notre application Node conteneurisée sur Kubernetes Engine en utilisant _kubectl_

...mais ce que nous voulons, c'est une configuration de déploiement continu telle qu'un nouveau commit déclenche un build et un déploiement.

Voici ce que nous devons faire :

1. Mettre notre code sur GitHub

* Nous suivrons les mêmes étapes que dans la section précédente sur App Engine. Créez un nouveau dépôt et poussez le code de notre machine vers GitHub.

2. Activer Cloud Build

* [Activer l'API Cloud Build](https://console.cloud.google.com/flows/enableapi?apiid=cloudbuild.googleapis.com&redirect=https://cloud.google.com/cloud-build/docs/quickstart-gcloud&_ga=2.113783623.-1976915987.1533866140) pour notre projet
* [Activer l'API Kubernetes Engine](https://console.cloud.google.com/flows/enableapi?apiid=container.googleapis.com&_ga=2.147807223.-1976915987.1533866140) pour notre projet
* Accorder l'IAM Kubernetes Engine au compte de service Cloud en allant sur la page [IAM](https://console.cloud.google.com/iam-admin/iam) pour ce compte de service `<project-id>@cloudbuild.gserviceaccount.com`, modifiez-le et donnez-lui le rôle d'administrateur Kubernetes Engine

3. Créer un fichier de configuration Cloud Build

* Créez un nouveau fichier `cloudbuild.yaml` qui ressemble à ceci :

```
steps:
  - name: 'gcr.io/cloud-builders/npm'
    args: ['install']
  - name: 'gcr.io/cloud-builders/npm'
    args: ['test']
  - name: 'gcr.io/cloud-builders/docker'
    args: ["build", "-t", "gcr.io/$PROJECT_ID/my-image:$REVISION_ID", "."]
  - name: 'gcr.io/cloud-builders/docker'
    args: ["push", "gcr.io/$PROJECT_ID/image:$REVISION_ID"]
  - name: 'gcr.io/cloud-builders/kubectl'
    args:
      - 'set'
      - 'image'
      - 'deployment/my-deployment'
      - 'my-container=gcr.io/$PROJECT_ID/image:$REVISION_ID'
    env:
      - 'CLOUDSDK_COMPUTE_ZONE=us-east1-b'
      - 'CLOUDSDK_CONTAINER_CLUSTER=my-cluster'
```

Cette configuration comporte cinq étapes de build qui exécuteront `npm install` puis `npm test` pour s'assurer que notre application fonctionne, puis elle créera une image Docker et la poussera vers GCR, puis déployera notre application sur notre cluster Kubernetes. Les valeurs `_my-cluster, my-deployment et my-container_` dans ce fichier font référence aux ressources dans le cluster Kubernetes que nous avons créé (selon le guide que nous avons suivi ci-dessus). `_$REVISION_ID_` est une valeur variable que Cloud Build injecte dans la configuration en fonction du commit GitHub qui déclenche ce build.

4. Exécuter un Build manuellement (optionnel, pour vérification)

* Nous pouvons maintenant déployer notre application depuis notre machine en utilisant Cloud Build
* Exécutez la commande cloud build sur votre terminal : `gcloud builds submit --config cloudbuild.yaml --substitutions=REVISION_ID=1 .`

Nous passons également l'ID de révision dans cette commande, puisque nous exécutons manuellement ce build par rapport à un déclenchement par GitHub.

* Rendez-vous sur la page [Cloud Builds](https://console.cloud.google.com/cloud-build/builds) pour voir le build en action.
* À la fin du build, vous pouvez tester votre application Node en utilisant l'URL du service Kubernetes
* Vous pouvez apporter des modifications à votre application Node et appeler à nouveau cette commande pour démarrer plus de builds si vous le souhaitez

5. Créer un Build Trigger

* Les étapes pour configurer cela sont les mêmes que celles de la section précédente pour App Engine. Allez sur la page [Cloud Build Triggers](https://console.cloud.google.com/cloud-build/triggers) pour ce projet, sélectionnez le bon dépôt GitHub, créez un trigger appelé `déploiement continu` juste pour la branche `master` et vous avez terminé.
* Exécuter un Build automatiquement en poussant vers GitHub
* Cela est également identique à la section précédente pour App Engine — faites une modification, ajoutez, commitez et poussez vers GitHub, ce qui déclenchera un build que vous pouvez voir sur votre page [Cloud Builds](https://console.cloud.google.com/cloud-build/builds). Une fois le build terminé, vous pourrez voir l'application mise à jour en utilisant l'URL du service Kubernetes.

Voici une capture d'écran d'un build déclenché par un push GitHub pour notre application :

![Image](https://cdn-media-1.freecodecamp.org/images/lhzzRfcvgfRJaV-NXGSZw6KvyrwTjKVj-WZA)

Les étapes de cette section étaient presque identiques à celles de la section App Engine. Les principales différences étaient que nous devions conteneuriser notre application avec Docker, lancer notre cluster Kubernetes, puis avoir une configuration Cloud Build avec juste quelques étapes supplémentaires.

Mais au cœur, Cloud Build et ses Build Triggers fonctionnent presque de la même manière et nous offrent une expérience de déploiement fluide. Notre deuxième application est maintenant déployée sur Kubernetes Engine à chaque commit sur master ??

![Image](https://cdn-media-1.freecodecamp.org/images/jIX1ztshIMTpBiKNuw-YruekKbP0LIuxV6pB)
_Photo par [Unsplash](https://unsplash.com/photos/Esq0ovRY-Zs?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Maximilian Weisbecker</a> sur <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

### Déploiement continu pour Cloud Functions

Bien sûr, App Engine et Kubernetes Engine sont géniaux, mais qu'en est-il des déploiements automatisés pour notre application Serverless ? Je veux dire, ne pas avoir de serveurs à gérer du tout est vraiment le meilleur, non ? Faisons cela !

Déployer une application Node sur Cloud Functions nécessitera de créer un nouveau projet. Aucun fichier de configuration n'est nécessaire, et une fois que GCloud functions deploy est exécuté sur notre terminal, nos fonctions sont déployées !

Si vous voulez essayer cela par vous-même, voici les ressources dont vous aurez besoin :

* [Application d'exemple pour Cloud Functions](https://github.com/gautamarora/gae-node-hello-world)
* [Guide de démarrage rapide pour Node sur Cloud Functions](https://cloud.google.com/functions/docs/quickstart)
* [Test local des Cloud Functions en utilisant l'émulateur Node](https://cloud.google.com/functions/docs/emulator)

Si vous avez suivi jusqu'à présent, vous pouvez probablement déjà imaginer les étapes que nous devons faire :

1. Mettre notre code sur GitHub

* Nous savons déjà comment faire cela

2. Activer Cloud Build

* [Activer l'API Cloud Build](https://console.cloud.google.com/flows/enableapi?apiid=cloudbuild.googleapis.com&redirect=https://cloud.google.com/cloud-build/docs/quickstart-gcloud&_ga=2.113783623.-1976915987.1533866140) pour notre projet
* [Activer l'API Cloud Functions](https://console.cloud.google.com/flows/enableapi?apiid=cloudfunctions&_ga=2.84807769.-1976915987.1533866140) pour notre projet.
* Accorder l'IAM Cloud Functions au compte de service Cloud Build en allant sur la page [IAM](https://console.cloud.google.com/iam-admin/iam), trouvez ce compte de service `<project-id>@cloudbuild.gserviceaccount.com`, modifiez-le et donnez-lui le rôle d'éditeur de projet.

3. Créer un fichier de configuration Cloud Build

* Créez un nouveau fichier `cloudbuild.yaml` qui ressemble à ceci :

```
steps:
  - name: 'gcr.io/cloud-builders/npm'
    args: ['install']
  - name: 'gcr.io/cloud-builders/npm'
    args: ['test']
  - name: 'gcr.io/cloud-builders/gcloud'
      args:
        - beta
        - functions
        - deploy
        - helloWorld
        - --source=.
        - --runtime=nodejs8
        - --trigger-http
```

Similaire à la configuration App Engine, cette configuration comporte 3 étapes pour installer, puis tester le build, et si tout est bon, le déployer sur Cloud Functions.

4. Exécuter le Build manuellement (optionnel, pour vérification)

* Nous pouvons maintenant déployer notre fonction depuis notre machine en utilisant Cloud Build
* Exécutez ceci dans votre terminal : `gcloud builds submit --config cloudbuild.yaml .`
* Rendez-vous sur la page [Cloud Builds](https://console.cloud.google.com/cloud-build/builds) pour voir le build en action.
* À la fin du build, vous pouvez tester votre application serverless en utilisant l'URL Cloud Function

5. Créer un Build Trigger

* Les étapes pour configurer cela sont les mêmes que celles des sections précédentes pour App Engine et Kubernetes Engine. Allez sur la page [Cloud Build Triggers](https://console.cloud.google.com/cloud-build/triggers) pour ce projet, sélectionnez le bon dépôt GitHub, créez un trigger appelé `déploiement continu` juste pour la branche `master`, et vous avez terminé.

6. Exécuter un Build automatiquement en poussant vers GitHub

* Cela est également identique à la section précédente pour App Engine & Kubernetes Engine : faites une modification, ajoutez, commitez et poussez vers GitHub, ce qui déclenchera un build que vous pouvez voir sur votre page [Cloud Builds](https://console.cloud.google.com/cloud-build/builds). Une fois le build terminé, vous pourrez voir l'application mise à jour en utilisant l'URL Cloud Functions

Voici une capture d'écran d'un build déclenché par un push GitHub pour notre application d'exemple :

![Image](https://cdn-media-1.freecodecamp.org/images/UVSiRQerOS6aBhi8XUTJTxuVX976dsMDFgX5)

Les Cloud Functions étaient super faciles à configurer avec des builds automatisés et rendent le workflow « code → build → test → push → deploy » vraiment très rapide ! Notre troisième application est maintenant déployée sur Cloud Functions à chaque commit sur master ???

![Image](https://cdn-media-1.freecodecamp.org/images/41hLHGgzW9-5Np9cXWpgoltzPVltTqLNCfY0)
_Photo par [Unsplash](https://unsplash.com/photos/kAjrml-a8R0?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Jassim Vailoces</a> sur <a href="https://unsplash.com/search/photos/shipping?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

### Conclusion

Ouf ! Nous avons couvert beaucoup de terrain dans cet article. Si c'était votre première fois à essayer GCP pour Node, j'espère que vous avez pu voir à quel point il est facile et direct d'essayer les différentes options. Si vous étiez surtout impatient de comprendre comment configurer le déploiement continu pour les applications sur GCP, j'espère que vous n'avez pas été déçu non plus !

Avant de partir, je voulais juste m'assurer que vous n'avez pas manqué le fait que toutes les sections avaient une application d'exemple : [Hello World pour App Engine](https://github.com/gautamarora/gae-node-hello-world), [Hello World pour Kubernetes Engine](https://github.com/gautamarora/gke-node-hello-world) et [Hello World pour Cloud Functions](https://github.com/gautamarora/gcf-node-hello-world).

C'est tout pour l'instant ! Allons déployer du code ! ?

Merci d'avoir suivi. Si vous avez des questions ou si vous souhaitez signaler des erreurs dans cet article, n'hésitez pas à laisser un commentaire.

Si vous avez trouvé cet article utile, n'hésitez pas à ?

Et vous pouvez [me suivre sur Twitter ici.](http://twitter.com/gautam)