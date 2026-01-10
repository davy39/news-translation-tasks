---
title: Décentralisez votre application avec Google Cloud Platform
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-21T22:57:25.000Z'
originalURL: https://freecodecamp.org/news/decentralize-your-application-with-google-cloud-platform-7149ec6d0255
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Z68F4SMRusBjJ7Q8ox4Waw.jpeg
tags:
- name: decentralized apps
  slug: decentralized-apps
- name: Flask Framework
  slug: flask
- name: Google Cloud Platform
  slug: google-cloud-platform
- name: Microservices
  slug: microservices
- name: software architecture
  slug: software-architecture
seo_title: Décentralisez votre application avec Google Cloud Platform
seo_desc: 'By Simeon Kostadinov

  When first starting a new software project, you normally choose a certain programming
  language, a specific framework and libraries. Then you begin coding. After 2 - 3
  months you end up with a nicely working single application.

  Bu...'
---

Par Simeon Kostadinov

Lorsque vous commencez un nouveau projet logiciel, vous choisissez généralement un certain langage de programmation, un framework spécifique et des bibliothèques. Ensuite, vous commencez à coder. Après 2 à 3 mois, vous obtenez une application unique fonctionnant correctement.

**Mais, à mesure que le projet grandit et que de nouvelles fonctionnalités sont ajoutées, vous réalisez rapidement les inconvénients d'un système centralisé.** Difficile à maintenir et non évolutif sont quelques-unes des raisons qui vous feront chercher une meilleure solution. C'est là que les Microservices entrent en jeu.

#### Qu'est-ce que les Microservices ?

Les Microservices sont des systèmes construits indépendamment, chacun fonctionnant dans son propre processus et communiquant souvent via une API REST. Représentant différentes parties de votre application, ils sont déployables séparément et chaque partie peut être écrite dans n'importe quel langage.

Vous pouvez facilement voir comment, en traitant les problèmes d'un système monolithique, les Microservices sont devenus une exigence pour tout logiciel de pointe.

Je recommande fortement de lire [Microservices (par James Lewis)](https://martinfowler.com/articles/microservices.html) et [On Monoliths and Microservices](https://dev.otto.de/2015/09/30/on-monoliths-and-microservices/) si vous souhaitez comprendre plus en profondeur les concepts clés de ce style architectural.

#### Que allez-vous construire ?

Cet article vous guidera à travers le processus de mise en œuvre d'un Microservice en utilisant [Google Cloud Platform](https://cloud.google.com/).

Imaginez que vous développez une application qui accepte une entrée de texte d'un utilisateur et détermine la catégorie des mots clés dans l'entrée.

Nous utiliserons un exemple pour illustrer la fonctionnalité de l'application. Considérez le texte d'exemple ci-dessous du [site Web de l'API Cloud Natural Language de GCP](https://cloud.google.com/natural-language/) :

> « Google, dont le siège est à Mountain View, a dévoilé le nouveau téléphone Android lors du Consumer Electronic Show. Sundar Pichai a déclaré dans son discours d'ouverture que les utilisateurs adorent leurs nouveaux téléphones Android. »

Notre application Web accepterait le texte ci-dessus comme entrée et retournerait la catégorie à laquelle appartiennent les mots clés, comme dans la figure ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1*SAeCcBhjaEY-JqaRzOaskA.png)
_Source : [Site Web de l'API Cloud Natural Language de GCP](https://cloud.google.com/natural-language/" rel="noopener" target="_blank" title=")_

Cette fonctionnalité est très appréciée et les gens l'utilisent des centaines de fois chaque jour. Maintenant, si vous allez offrir cette fonctionnalité en tant que service recevant un grand nombre de trafic quotidien, vous souhaitez répondre avec un système stable et fiable.

C'est pourquoi nous allons construire une application Flask légère, hébergée sur [Google App Engine](https://cloud.google.com/appengine/docs/flexible/python/). L'intégrer avec [Google Cloud Pub/Sub](https://cloud.google.com/pubsub/docs/) nous aidera à gérer toutes les requêtes asynchrones que nous recevons et à assurer que les utilisateurs n'attendent pas trop longtemps pour une réponse.

#### Créer et déployer l'application

Commençons d'abord par l'application Flask (vous pouvez également choisir Django, Node.js, Go ou tout autre outil utilisé pour construire des applications côté serveur). Si vous n'êtes pas très familier avec le développement d'une application Flask, cette [série Flask](https://damyanon.net/post/flask-series-environment/) peut vous montrer étape par étape comment configurer une application.

Pour les besoins de ce tutoriel, nous utiliserons cet exemple simple :

**Cet embed provient d'un site externe et ne semble plus être disponible**

Tout d'abord, vous devez installer les dépendances `pip install Flask gunicorn`. Vous utiliserez `**gunicorn**` pour exécuter l'application sur Google App Engine. Pour un accès local, vous pouvez exécuter `python text.py` dans la console et trouver l'application sur le port 8080.

Pour déployer l'application sur Google App Engine, vous devez suivre ces étapes :

* Créer un projet (suivez les instructions [« Avant de commencer » de la documentation](https://cloud.google.com/appengine/docs/flexible/python/quickstart)). **Enregistrez l'ID du projet pour plus tard.**
* Créer un fichier `app.yaml` (affiché ci-dessous), qui est utilisé par Google App Engine pour reconnaître l'application.
* Exécuter `gcloud app deploy` dans la console.

Le fichier `app.yaml` ressemble à ceci :

**Cet embed provient d'un site externe et ne semble plus être disponible**

La ligne 3 est importante, où vous utilisez `**gunicorn**` pour dire à Google App Engine d'exécuter l'application `**app**` à partir d'un fichier appelé `text.py` (l'application Flask). Vous pouvez en savoir plus sur la structure du fichier `.yaml` [ici](https://cloud.google.com/appengine/docs/standard/python/config/appref). Après le déploiement, vous devriez pouvoir accéder à votre projet depuis `https://[YOUR_PROJECT_ID].appspot.com`.

Lors de la construction d'applications prêtes pour la production, vous souhaitez souvent tester votre code avant de le mettre en ligne. Une façon de faire cela est d'exécuter votre application dans un serveur localement. Une meilleure approche est d'avoir une version de développement de l'application qui peut être testée non seulement depuis votre machine locale mais aussi depuis un environnement hébergé. Vous pouvez utiliser [Google App Engine versions](https://cloud.google.com/appengine/docs/admin-api/deploying-apps) pour cela.

Il suffit de déployer votre application avec `gcloud app deploy -v textdev` (pour le développement) ou `gcloud app deploy -v textprod` (pour la production).

Ensuite, accédez à `https://textdev.[YOUR_PROJECT_ID].appspot.com` ou `https://textprod.[YOUR_PROJECT_ID].appspot.com` pour accéder à la version spécifique.

#### Passer à l'échelle à l'infini

Jusqu'à présent, tout va bien. Vous avez une application fonctionnelle, hébergée sur Google Cloud Platform. Maintenant, vous devez ajouter [Google Cloud Pub/Sub](https://cloud.google.com/pubsub/docs/) et [Google Natural Language API](https://cloud.google.com/natural-language/).

Mais d'abord, expliquons l'architecture.

Une fois qu'une requête est reçue, l'application Flask publiera un message avec le texte sur un sujet (créé ci-dessous). Ensuite, un abonné (script Python) extraira ce message et appliquera l'API Google Natural Language à chaque texte. Enfin, le résultat sera enregistré dans une base de données.

Pour plusieurs requêtes, l'application les publie de manière asynchrone sur le sujet et l'abonné commence à exécuter la première. Lorsqu'il est prêt, il prend la deuxième et ainsi de suite.

Maintenant, vous devez modifier le fichier `text.py` :

**Cet embed provient d'un site externe et ne semble plus être disponible**

Le code des lignes 15 et 16 crée l'éditeur. À la ligne 18, il publie un message contenant l'email de l'utilisateur et l'entrée de texte.

Vous devez simplement remplir le `project_id` et le `topic_id` (lignes 6 et 7).

Puisque le `project_id` a été utilisé précédemment, ajoutez-le simplement ici.

Pour le `topic_id`, vous devez faire ce qui suit :

* [Activer l'API Google Cloud Pub/Sub](https://console.cloud.google.com/apis/dashboard)
* [Aller à la page Pub/Sub de votre projet](https://console.cloud.google.com/cloudpubsub/topicList)
* Créer un sujet et un abonnement
* Utiliser le nom du sujet comme votre `topic_id`
* Conserver le nom de l'abonnement pour plus tard. Vous en aurez besoin comme `subscription_id`

Magnifique ! Maintenant, vous avez un éditeur fonctionnel.

Passons à la configuration de l'abonné. Il y a deux fichiers à créer : `worker.py` et `startup-script.sh`.

Le fichier `worker.py` ressemble à ceci :

**Cet embed provient d'un site externe et ne semble plus être disponible**

Le fichier est légèrement plus grand, mais nous allons l'examiner étape par étape, en commençant par le bas.

Lorsque le fichier est exécuté, le code de la ligne 44 exécute `main()`. Cette fonction définit l'abonné avec votre `project_id` et `subscription_id` et lui attribue un rappel.

Le `callback` (initialisé à la ligne 7) va recevoir tous les messages et effectuer la tâche requise (déterminer la catégorie d'un texte). Si vous suivez le code du `callback`, vous pouvez facilement voir comment l'API Google Natural Language est utilisée.

La ligne intéressante est la ligne 11 où `message.ack()` accuse réception du message actuel. Vous pouvez voir cela comme si le worker disait : « J'ai terminé avec ce message et je suis prêt à traiter le suivant ».

Maintenant, vous devez implémenter `startup-script.sh`.

Il s'agit d'un script shell avec plusieurs commandes :

**Cet embed provient d'un site externe et ne semble plus être disponible**

Avant d'expliquer le code ci-dessus, je dois clarifier le processus.

En gros, [Google Cloud Compute Engine](https://console.cloud.google.com/compute) vous donne la possibilité de mettre à l'échelle une application en fournissant autant de machines virtuelles (VM) que nécessaire pour exécuter plusieurs workers simultanément.

Vous devez simplement ajouter le code pour le worker, que vous avez déjà, et configurer les VM. Avec le `worker.py`, vous devez également ajouter un `startup-script.sh` qui s'exécutera chaque fois qu'une nouvelle VM démarre.

De nouvelles instances de VM sont démarrées pour éviter les retards dans les réponses lorsqu'un grand nombre de messages est reçu.

Pour une explication plus approfondie et technique de ce processus, consultez la [documentation](https://cloud.google.com/compute/docs/).

Maintenant, laissez-moi vous guider à travers le script :

* **Ligne 1** : signifie que le script doit toujours être exécuté avec bash, plutôt qu'avec un autre shell.
* **Lignes 2 et 3** : crée et entre dans un nouveau répertoire où tous les fichiers seront stockés.
* **Ligne 4** : copie le fichier `worker.py` depuis [Google Cloud Storage](https://cloud.google.com/storage/docs/) dans la VM (je vais expliquer comment télécharger vos fichiers dans le stockage ci-dessous).
* **Ligne 5** : ici, vous devez spécifier une chaîne JSON de votre clé afin que Google puisse vérifier vos identifiants. Pour obtenir cette chaîne, vous devez [créer un compte de service](https://console.cloud.google.com/iam-admin/iam/project). Sélectionnez `**Fournir une nouvelle clé privée**` et pour `**Type de clé**`, utilisez `JSON`. Un fichier sera téléchargé sur votre ordinateur. Copiez le contenu et transformez-le en une chaîne JSON (en utilisant `JSON.stringify(key_in_json_format)` dans une console de navigateur). Collez-le à la place de `SERVICE_ACCOUNT_KEY`.
* **Ligne 6** : exporte la clé en tant que [variable d'environnement](https://developers.google.com/identity/protocols/application-default-credentials) qui sera utilisée par les API Google pour vérifier vos identifiants.
* **Lignes 7 - 12** : configure les paramètres et installe les bibliothèques Python.
* **Ligne 15** : exécute le worker.

Maintenant, vous devez télécharger `worker.py` et `startup-script.sh` dans votre stockage et configurer la VM. Pour télécharger les fichiers, allez [ici](https://console.cloud.google.com/storage/) et créez un nouveau bucket avec le même nom que votre ID de projet. Créez un dossier appelé _workers_ et téléchargez les scripts à l'intérieur. **Assurez-vous de changer le `worker.py` en un lien « Public » et modifiez les permissions du `_startup-script.sh_** **pour** que votre compte de service soit propriétaire.

#### Configurations et tests

La dernière étape consiste à configurer les paramètres de la VM et à tester le système. Suivez simplement les instructions [« Créer un modèle d'instance » de la documentation](https://cloud.google.com/solutions/media-processing-pub-sub-compute-engine) et vous êtes prêt à partir !

Une fois que la VM démarre, vous pouvez essayer d'envoyer des requêtes à votre application et examiner comment elle réagit en vérifiant les [journaux](https://console.cloud.google.com/logs/viewer).

#### Réflexions finales

Parcourir la documentation de Google peut vous aider beaucoup. Consultez également ce [tutoriel](https://cloud.google.com/solutions/media-processing-pub-sub-compute-engine) - vous pourriez le trouver utile lors de la mise en œuvre de certaines des étapes ci-dessus.

Je tiens à exprimer ma gratitude à [Logan Allen](https://www.freecodecamp.org/news/decentralize-your-application-with-google-cloud-platform-7149ec6d0255/undefined) pour m'avoir aidé à mieux comprendre ce processus. J'espère que vous le trouverez utile.

Laissez vos questions ou suggestions dans la section des commentaires.