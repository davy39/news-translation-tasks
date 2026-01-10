---
title: Comment créer un bot Slack Meetup avec Standard Library et Node.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-29T07:38:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-meetup-slack-app-with-standard-library-52f96b27d95a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*bppC-vl7i0Mg0medcD-eAA.png
tags:
- name: api
  slug: api
- name: Apps
  slug: apps-tag
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: technology
  slug: technology
seo_title: Comment créer un bot Slack Meetup avec Standard Library et Node.js
seo_desc: 'By Janeth Ledezma

  In this guide, you will learn how to set up a Slack application that will display
  information from Meetup’s API, which serves stored data from Meetup to other application
  software.

  Meetup is a popular website where individuals with ...'
---

Par Janeth Ledezma

Dans ce guide, vous apprendrez à configurer une application [Slack](https://slack.com) qui affichera des informations provenantes de [l'API de Meetup](https://www.meetup.com/meetup_api/), qui sert des données stockées de Meetup à d'autres logiciels d'application.

[Meetup](https://meetup.com) est un site web populaire où des individus ayant des intérêts similaires forment des groupes pour organiser des événements dans leurs villes locales.

Une fois que nous aurons réussi à faire une requête à l'API de Meetup, nous recevrons une réponse de Meetup, nous extrairons des données spécifiques de la charge utile JSON, et nous afficherons ces données dans Slack. Nous concevrons l'attachement de notre application Slack de manière à ce qu'il affiche le nom de l'événement, la description, la date et l'heure, le lieu, et plus encore !

![Image](https://cdn-media-1.freecodecamp.org/images/-zI7vrqr8I9pF6n2OOehZufETjLb6qAt6xjB)

### Comment cela fonctionne :

Lorsque vous soumettez `/nextmeetup 94709&javascript` (ou tout code postal et un sujet d'intérêt) dans la boîte de message de Slack, un webhook sera déclenché. Le webhook, construit et hébergé sur Standard Library, fera d'abord une requête à l'API de Meetup, qui retournera une charge utile JSON avec les résultats de la requête.

Le webhook créera ensuite des messages Slack pour chaque événement et les publiera dans un canal spécifié.

Pas besoin de se sentir dépassé ! Prenons cela étape par étape.

### Ce dont vous aurez besoin :

[1 compte Slack](https://medium.com/p/52f96b27d95a/edit)

[1 compte Meetup](https://www.meetup.com/)

[1 compte Standard Library](https://stdlib.com/)

### Étape 1 : Configurer votre application Slack

Assurez-vous d'être [connecté à Slack](https://slack.com/signin) et visitez votre tableau de bord des applications Slack à l'adresse [https://api.slack.com/apps](https://api.slack.com/apps). Vous verrez un écran qui ressemble à ce qui suit.

![Image](https://cdn-media-1.freecodecamp.org/images/aZkh1776B3oyNpits0QtTqGstPsKZdRnQph5)

![Image](https://cdn-media-1.freecodecamp.org/images/nSYlmuf9O0E-WIChpfu5TimGz6Dk0OWmvL-r)

Cliquez sur **Créer une nouvelle application**. Vous serez présenté avec une fenêtre modale pour entrer le nom de votre application et l'espace de travail Slack de développement auquel vous souhaitez l'ajouter.

À partir de là, cliquez sur **Créer une application**, vous vous retrouverez sur une page **Informations de base**.

Faites défiler vers le bas jusqu'à **Informations d'affichage**. C'est ici que vous pouvez donner à votre application Slack un nom, une description et une image si vous le souhaitez.

Gardez la page **Informations de base** ouverte dans votre navigateur. Nous l'utiliserons dans un instant pour récupérer les informations d'identification de votre application Slack afin de connecter cette application à la logique backend hébergée sur Standard Library — le code qui exécute votre application.

### Étape 2 : Créer un compte Standard Library gratuit

Nous hébergerons le code de notre application Slack sur [Standard Library](https://stdlib.com) — le code qui demandera et recevra des informations spécifiques de l'API de Meetup. Alors, rendez-vous sur [Code on Standard Library](https://code.stdlib.com) et réclamez votre compte gratuit.

![Image](https://cdn-media-1.freecodecamp.org/images/GswdEExJ9xQZYnIRWgBAjLEpI1zhjqGte5-i)

### Étape 3 : Copier et modifier le modèle de code de l'application Slack sur Standard Library

Une fois que vous vous êtes connecté ou inscrit, vous atterrirez sur « **Featured API Source** ». Ce sont des modèles de code d'application disponibles sur [Standard Library](https://www.freecodecamp.org/news/how-to-build-a-meetup-slack-app-with-standard-library-52f96b27d95a/undefined) pour que chacun puisse facilement copier et modifier des applications. Vous allez sélectionner le modèle de code de l'application Slack et le modifier pour créer votre API qui alimentera votre application Slack.

Entrez un nom unique pour votre projet d'API et cliquez sur **Okay**.

#### Une brève explication du modèle de code source de l'application Slack :

Faisons une pause pour comprendre ce que nous regardons. La barre latérale de gauche est une structure de projet d'API que Standard Library a configurée pour vous afin de construire des applications Slack.

![Image](https://cdn-media-1.freecodecamp.org/images/3nIyUe9M-A4qx6nZAVuea9jcdUx21-djabIa)

Le modèle de code pour les applications Slack comporte quatre répertoires. Nous travaillerons uniquement dans le répertoire `functions` qui est équipé de trois autres dossiers :

`actions/, commands/, et events/` ainsi qu'un seul fichier `__main__.js`. Les instructions pour les actions Slack, les commandes slash et les événements pour votre application se trouvent dans ces dossiers.

Lorsque vous déployez votre API, Standard Library générera automatiquement des points de terminaison HTTPS (URL) pour chaque répertoire. Les URL résultantes nous permettront de configurer des webhooks qui écoutent et répondent aux [actions de Slack](https://api.slack.com/actions), aux [commandes slash](https://api.slack.com/slash-commands) et aux [événements](https://api.slack.com/events-api).

Tous les cinq dossiers (y compris le dossier `functions`) sont configurés avec un fichier `__main__.js` (le point de terminaison principal du répertoire). Ces points de terminaison `__main__.js` envoient les fonctions appropriées lorsqu'ils reçoivent un message de Slack. Pour ce tutoriel, le fichier `__main__.js` enverra le point de terminaison `commands` lorsque nous appellerons notre API via notre bot Slack. Maintenant, revenons à la configuration de notre bot !

### Étape 4 : Ajouter une commande à votre API Standard Library

![Image](https://cdn-media-1.freecodecamp.org/images/2YieSaBJlBzrtzxX30Jo-imlMtO0v8sr8fCH)
_Créer une commande supplémentaire_

`commands:` Le répertoire `commands` est le point de terminaison pour toutes les commandes slash de Slack. Créez une commande supplémentaire en plaçant votre curseur sur le répertoire `commands` et en cliquant avec le bouton droit. Sélectionnez **Nouveau fichier** et nommez votre fichier de commande slash **nextmeetup.js** et cliquez sur **Okay**.

![Image](https://cdn-media-1.freecodecamp.org/images/NGeSmqBZ9HUBIsGZUVSCqS1ML7nhjfdHHwLz)
_Nommer votre commande_

À ce stade, vous remarquerez une fonction JavaScript « hello world » à l'intérieur (`__main__.js`), qui est générée automatiquement.

![Image](https://cdn-media-1.freecodecamp.org/images/X6k8eDII32yPp-EnudBel9TPujnV6TSYV7bH)

Remplacez le contenu de `nextmeetup.js` par ce qui suit :

### Une brève explication du code :

Lorsque vous soumettez `/nextmeetup` via votre application Slack, vous faites une requête GET à l'API de Meetup.

Chaque requête à l'API de Meetup doit être authentifiée avec une clé API, nous passons donc notre clé Meetup de notre fichier `env.json` dans notre requête. Nous envoyons également notre requête GET avec les deux paramètres, zip et topic.

L'API de Meetup retourne un tableau d'objets d'événements Meetup, que nous pouvons voir à partir des journaux de Code on Standard Library en enregistrant notre réponse : `console.log(response.data)`. Votre onglet journaux est situé sous la section de débogage.

`response.data` est un tableau d'événements qui correspondent à votre requête, et nous voulons créer deux pièces jointes pour chaque événement (une pour le lieu et une pour les détails). Nous avons une fonction appelée `formatAttachement` que nous pouvons appeler sur chacun des événements. Les résultats sont placés dans un tableau appelé `attachments` qui est envoyé à Slack.

Une fois que vous avez copié et collé le code dans votre fichier `nextmeetup.js`, enregistrez les modifications et naviguez vers le fichier `env.json` dans le menu de la barre latérale.

### **Étape 5 : Remplir votre fichier env.json avec les informations d'identification et les clés de l'application**

À l'intérieur de `env.json`, vous remarquerez des variables d'environnement pour votre API. Vous pouvez définir différentes valeurs pour les environnements local, dev et release (production). Ce fichier contiendra toutes vos clés d'accès uniques à votre compte Standard Library, à votre compte Meetup et aux informations d'identification de votre application Slack.

Nous ne ferons des modifications que dans les variables d'environnement `"dev"` — **assurez-vous de modifier le bon ensemble** ! Notez que les valeurs `"dev"` sont pour votre environnement de développement et que les valeurs `"release"` ne doivent être remplies que lorsque vous êtes prêt à publier votre application. Les variables `"local"` peuvent être laissées vides lors du déploiement à partir de Code on Standard Library, mais elles doivent être remplies lors de l'utilisation des [outils de ligne de commande](https://github.com/stdlib/lib).

![Image](https://cdn-media-1.freecodecamp.org/images/kmKEINtXpdkj3DnRkNN2kgH0xLdt2l8zpvzt)

Commençons par remplir la variable `"STDLIB_TOKEN"`. Placez votre curseur entre les guillemets (voir l'écran) et soit cliquez avec le bouton droit et sélectionnez **Insérer le jeton de bibliothèque...** ou utilisez le raccourci ⌘ + K.

![Image](https://cdn-media-1.freecodecamp.org/images/BieAtoX31d6JZGVsw2zsOU8m24aKJO-dJjv9)
_Sélectionnez votre jeton de bibliothèque_

Sélectionnez **Library Token** pour remplir l'environnement `"dev"`.

Retournez maintenant à la page **Basic Information** de votre application Slack et faites défiler vers le bas jusqu'à **App Credentials** :

![Image](https://cdn-media-1.freecodecamp.org/images/XHdgD085GHzg7Te1kCHhJ7dumjiBFJDVqK5H)

Copiez votre **Client ID, Client Secret**, et **Verification Token**. Collez-les dans leurs champs respectifs dans la section `"dev"` du fichier `env.json`.

Ajoutez le nom que vous avez donné à votre application Slack pour `SLACK_APP_NAME`.

Ex : `SLACK_APP_NAME:Meetup-bot`

La valeur `"SLACK_REDIRECT"` sera un point de terminaison https généré par Standard Library une fois que vous aurez déployé votre API. Même si nous n'avons pas encore déployé, remplissez-le maintenant en utilisant cette structure. `https://<username>.api.stdlib.com/<apiname>@dev/auth/` — avec votre nom d'utilisateur de bibliothèque standard et le nom de votre API. Une fois que nous déployons le code, vous pouvez revenir pour confirmer que vous avez rempli cette valeur correctement.

Mon `SLACK_REDIRECT` ressemble à ceci : `[https://Janethl.api.stdlib.com/slack-meetup-bot@dev/auth/](https://Janethl.lib.id/slack-meetup-bot@dev/auth/)` — assurez-vous d'ajouter le chemin d'authentification avec un slash à la fin.

Les capacités et permissions de votre application Slack seront déjà configurées avec les [_scopes_](https://api.slack.com/docs/oauth-scopes) suivants :

`"SLACK_OAUTH_SCOPE"` : `bot,commands,chat:write:bot,chat:write:user,files:write:user,channels:history`

![Image](https://cdn-media-1.freecodecamp.org/images/xzltxI-lwFhcCpdQB-lXlBjlknAel681aiSL)

La dernière variable que vous devrez ajouter est votre clé API Meetup. Meetup exige que chaque requête soit authentifiée avec une clé API.

### Étape 6 : Récupérer votre clé API Meetup

Connectez-vous ou créez un compte sur Meetup.com. Rendez-vous sur [https://secure.meetup.com/meetup_api/key/](https://secure.meetup.com/meetup_api/key/) pour récupérer votre clé API unique. Cliquez sur le cadenas pour révéler votre clé API et copiez-la.

![Image](https://cdn-media-1.freecodecamp.org/images/JHccHqG9xWelNZYBO-5l8C0P0H6jsL-GOQUC)

Retournez à votre fichier `env.json` sur [Code on Standard Library](https://code.stdlib.com). Ajoutez votre clé Meetup en tant que valeur `"key"`, exactement comme je l'ai fait dans l'image :

![Image](https://cdn-media-1.freecodecamp.org/images/YXWKWY60H81suM-HQD4HHbxcRBs9Nfzt7y2J)

Assurez-vous d'enregistrer les modifications avec **⌘ + s** (ou cliquez sur **Save** en bas à droite).

Dans le menu de la barre latérale, ouvrez le fichier `__main__.js` situé sous le répertoire des événements. Déployez le code de votre application Slack sur Standard Library en cliquant sur « **Run** ».

![Image](https://cdn-media-1.freecodecamp.org/images/5MKFKtAxFpYx5zw7n4MgLd2l4bQHRRko2avG)

* _Peu après le déploiement de votre code, Standard Library génère une URL de point de terminaison d'API HTTPS où votre code réside. Cette adresse se compose de votre <username>.api.stdlib.com suivi du nom que vous avez donné à votre API @ l'environnement : https://janethl.api.stdlib.com/slack-meetup-bo]t@dev/_

Nous avons maintenant l'URL qui nous permettra d'envoyer et de recevoir des messages de notre application Slack à l'API de Meetup. Maintenant, nous devons définir notre URL comme webhook dans Slack, alors retournons au tableau de bord de l'application Slack.

### Étape 7 : Créer une nouvelle commande slash et définir un webhook

Nous devons maintenant configurer notre application Slack pour qu'elle réponde à une commande slash (`/`). Pour cela, nous devons configurer un webhook sur la page de l'API Slack.

#### Qu'est-ce qu'un webhook ?

Peut-être pouvons-nous comprendre ce qu'est un webhook en le comparant à une API. Les API sont basées sur les requêtes — ce qui signifie qu'elles fonctionnent lorsqu'une requête est faite à partir d'une application tierce. Un webhook est basé sur les événements — le code s'exécutera lorsqu'un événement spécifique le déclenchera.

Pour définir un webhook, un fournisseur de services doit permettre à ses consommateurs d'enregistrer une URL où le fournisseur peut envoyer des informations lorsqu'un événement se produit. Dans cet exemple, Slack nous permet d'enregistrer notre adresse URL, et une fois enregistrée, une commande slash peut déclencher notre webhook, qui exécutera le code dans notre URL.

Maintenant que nous comprenons cela, retournons à la page de l'API Slack pour définir notre webhook. Trouvez et sélectionnez **Slash Commands** dans le menu de la barre latérale.

![Image](https://cdn-media-1.freecodecamp.org/images/9RPI3R3aSmR2x1IgCzsvzhh0RLjxFvBUFtTJ)

Après avoir cliqué sur **Create New Command**, vous serez invité à entrer les détails de votre commande, pour cet exemple utilisez :

![Image](https://cdn-media-1.freecodecamp.org/images/RdkBTkWNoJkHfycs56tu2UoyVV8KXJhregfn)

Commande : `/nextmeetup`

RequestURL : `https://<username>.api.stdlib.com/<apiname>@dev/`commands/:bg

Short Description : `retrieves Meetup events`

Usage Hint : `[<zip>&&l`t;topic>]

Cliquez sur « **Save** » une fois terminé.

### Étape 8 : Activer OAuth & Permissions

![Image](https://cdn-media-1.freecodecamp.org/images/jEi9O8ZCrOwelWziR8q3mkNpPmLgQ8cTTaOB)

Retournez à votre [application Slack](https://api.slack.com/apps), dans le menu de la barre latérale, cliquez sur **OAuth & Permissions**.

Une fois là, vous devrez entrer une **Redirect URL** comme suit : `https://<username>.api.stdlib.com/<apiname>@dev/auth/`

cliquez sur « Add » et « Save URLS ».

_Cette URL de redirection doit correspondre à l'URL que nous avons définie dans le fichier `env.json` sur Code on Standard Library._

### Étape 9 : Ajouter un bot à votre application Slack

Retournez à votre page d'application Slack, et cliquez sur **Bot Users** dans la barre latérale de gauche. Cliquez sur **Add Bot User**. Gardez les paramètres par défaut.

![Image](https://cdn-media-1.freecodecamp.org/images/1nZYRzggEMPwybY5oqVPgmVrFb1Bt-7dwedm)
_Ajouter un utilisateur bot_

**La dernière étape** consiste à autoriser l'application. Dans votre navigateur, tapez : `https://<username>.api.stdlib.com/<apin`ame>@dev/`

![Image](https://cdn-media-1.freecodecamp.org/images/rNNe9b8cppAyfWgiNYwNYdf7ta6HoPZEyDlR)

![Image](https://cdn-media-1.freecodecamp.org/images/derVrVuzpBIm8FxXk9MVJFDPMIjzJ9P3lXtC)

Cliquez sur le bouton **Add to Slack**. Vous serez redirigé vers un autre écran d'autorisation.

Cliquez sur **Authorize**. Vous devriez voir un message de succès !

![Image](https://cdn-media-1.freecodecamp.org/images/h-QGo9rXpweIsERoYC23FICtUVmjdZDk528D)

### Étape 10 : Tester votre application Slack Meetup

![Image](https://cdn-media-1.freecodecamp.org/images/J3VxdRA0Vr0wFCUAy3e82nFvEEp4pMt3o6PB)

Vous avez terminé. Essayez-le ! Votre application Slack est maintenant disponible pour une utilisation dans l'espace de travail Slack que vous avez autorisé. Votre application Slack devrait répondre à une commande `/nextmeetup<94709>&<ja`vascript> comme je le montre dans la capture d'écran ci-dessus.

### C'est tout et merci !

J'espère que vous avez trouvé ce tutoriel utile. J'adorerais que vous **commentiez ici**, **m'envoyiez un e-mail à Janeth [at] stdlib [dot] com**, ou suiviez [Standard Library](http://www.stdlib.com?utm_source=content&utm_medium=blog&utm_campaign=scrape_service) sur Twitter, [@StdLibHQ](https://twitter.com/StdLibHQ).

_Janeth Ledezma est une développeuse pour Standard Library et diplômée de Cal — allez les bears ! Quand elle n'apprend pas la langue arabe ou ne fait pas de sport, vous pouvez la trouver en train d'explorer NorCal sur sa CBR500R._ ??? Suivez son parcours avec Standard Library sur Twitter @ms[s_ledezma.](https://twitter.com/mss_ledezma)_