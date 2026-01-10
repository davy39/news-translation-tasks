---
title: Comment créer un Meetupbot pour Slack en utilisant Node.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-13T19:49:56.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-meetupbot-for-slack-using-node-js-618725aa4c6e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*YQTE7lkH8LNnkguLdzaDkA.png
tags:
- name: api
  slug: api
- name: bots
  slug: bots
- name: Meetup
  slug: meetup
- name: slack
  slug: slack
- name: 'tech '
  slug: tech
seo_title: Comment créer un Meetupbot pour Slack en utilisant Node.js
seo_desc: 'By premprakashsingh


  What is Slack?

  If you are new to Slack, it’s a great platform for team collaboration and instant
  messaging used in and out of organizations to help team communication and collaboration.

  I first used Slack for a study group. You c...'
---

Par premprakashsingh

![Image](https://cdn-media-1.freecodecamp.org/images/1*qj03MmP47z5lduohrVC5aA.png)

### Qu'est-ce que Slack ?

Si vous êtes nouveau sur [Slack](https://slack.com/), c'est une excellente plateforme pour la collaboration d'équipe et la messagerie instantanée utilisée au sein et en dehors des organisations pour aider à la communication et à la collaboration d'équipe.

J'ai utilisé Slack pour la première fois pour un groupe d'étude. Vous pouvez créer différents canaux pour séparer les messages et les discussions. Vous pouvez également créer des canaux privés pour garder les messages privés au sein d'une équipe.

La meilleure fonctionnalité est qu'il permet également des intégrations sur sa plateforme. Et c'est ce qui le différencie des autres plateformes de messagerie et de collaboration.

Vous pouvez intégrer Google Calendar, Twitter, Trello, et plus encore. Il vous permet également de créer des applications personnalisées comme des bots.

### Projet

Dans cet article, je vais vous guider à travers la création d'un [MeetupBot](https://meetupbotteam.github.io/meetupbot-landing-page/) pour Slack en utilisant Node.js. Il vous donnera une liste de meetups qui se déroulent près de votre localisation en fonction de vos intérêts.

Vous êtes excité ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*l2W7LDBTPVvEAArgB4Sg2w.gif)

Il utilisera les commandes slash de Slack. Vous pouvez taper **/meetupbot** depuis Slack pour appeler le [MeetupBot](https://meetupbotteam.github.io/meetupbot-landing-page/) et il vous saluera avec la liste des commandes.

J'ai construit ce projet dans le cadre d'une cohorte [Chingu](https://medium.com/chingu) avec mes 2 membres d'équipe [Zameer](https://github.com/zamhaq) et [Linus](https://github.com/nusli)

![Image](https://cdn-media-1.freecodecamp.org/images/1*VTIZoHI-bb-CuXb85G6DHg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*2ROpGK4lel2ZHV5rG8PI0A.png)

Vous aurez besoin de connaissances de base en Node.js et en fonctionnement des API. Commençons.

### Étapes pour créer un MeetupBot pour Slack

#### Étape 1 — Installation du projet

URL de mon dépôt : [slack-meetup-bot](https://github.com/PREMPRAKASHSINGH/slack-meetup-bot)
Glitch : [glitch.com](https://glitch.com/)
Meetup_api : [meetup.com/meetup_api](https://www.meetup.com/meetup_api/)

* Tout d'abord, fork mon dépôt [ici](https://github.com/PREMPRAKASHSINGH/slack-meetup-bot).
* Ensuite, allez sur [glitch.com](https://glitch.com/) et créez un projet et modifiez le nom du projet pour un nom plus court.
* Cliquez sur **Nom du projet** > **Options avancées**. Ensuite, cliquez sur **Importer depuis GitHub**. Vous devez d'abord accorder l'accès au dépôt GitHub pour importer vos dépôts dans Glitch.
* Allez sur [Meetup Api ici](https://www.meetup.com/meetup_api/) et cliquez sur l'onglet **Clé API** et sauvegardez-la car vous devrez la passer avec chaque requête à l'API Meetup.
* Dans votre projet Glitch, ouvrez le fichier `**.env**` et définissez une variable **SECRET** comme votre clé API Meetup en tant que `SECRET=<MeetupApiKey>`
* Cliquez sur **Afficher Live** dans Glitch et vous obtiendrez l'URL de votre projet Glitch.

#### Étape 2 — Créer une application Slack

* Allez sur [Slack apps](https://api.slack.com/) puis cliquez sur **Vos applications** > **Créer une nouvelle** application.

Il vous montrera l'écran suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*EOvPe85KeYY8q_refsTtyQ.png)

Entrez le nom de l'application et sélectionnez **Espace de travail Slack de développement** puis cliquez sur **Créer une application**. Maintenant, nous devons faire 3 choses pour le voir fonctionner dans notre espace de travail Slack.

Sur l'écran suivant, vous verrez votre page de configuration de l'application avec les éléments suivants :

1. Activer les webhooks entrants.
2. Créer des commandes slash.
3. Installer votre application dans votre espace de travail.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EusJC6rdy4lN82UtELAbMw.png)

* Maintenant, cliquez sur **Incoming Webhooks** et activez-le.
Les Incoming Webhooks vous permettent de poster des messages dans Slack.
* Ensuite, cliquez sur **Slash Command** et créez-en une comme **/meetupbot**. La commande est `/meetupbot`, l'**URL de requête** est `<glitch-project-url>/meetupbot`, et ajoutez une **description courte** et un **indice d'utilisation**. 

![Image](https://cdn-media-1.freecodecamp.org/images/1*eWKdYfwrTuq-TrbrVBn6ng.png)

* En activant les Incoming Webhooks et en créant des Slash Commands, vous devriez déjà avoir une coche verte sur les permissions.
* Maintenant, cliquez sur **Installer votre application dans votre espace de travail** et cela vous mènera à l'écran suivant pour confirmer et autoriser avant l'installation. Et maintenant, vous êtes prêt à partir.

#### Étape 3 — Testez-le dans votre canal

Ouvrez votre canal d'équipe Slack et tapez **/meetupbot** et vous devriez voir vos commandes apparaître. Cliquez sur **Entrée** et vous verrez un message de salutation de MeetupBot et une liste de commandes que vous pouvez utiliser.

Puisque vous n'avez créé qu'une seule commande slash, allez sur votre page d'application et créez 1 commande supplémentaire comme **/meetupbot-show** avec l'**URL de requête** `<glitch-project-url>/meetupbot-show` (Suivez l'étape 2 — créer une commande Slack).

Maintenant, essayez cette commande, tapez `/meetupbot-show San Francisco et JavaScript` puis appuyez sur Entrée et vous verrez la liste des meetups JavaScript à San Francisco avec des détails comme le nom de l'événement et du groupe Meetup, la date du Meetup, le statut, le lieu et le nombre de Rsvp. Cliquez sur l'événement et il vous mènera à leur page d'événement Meetup.

Donc, c'est tout, félicitations, vous avez créé avec succès un MeetupBot pour Slack en utilisant Node.js.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6MYbG_q1sUHux_vYTIBW-w.gif)

### Comprenons le code.

Nous utilisons l'API Google Geocode pour obtenir la latitude et la longitude à partir du paramètre de localisation/adresse qui est passé dans la commande. Cette latitude et longitude, ainsi que le paramètre d'intérêt, sont ensuite passés à l'API Meetup pour obtenir une liste de meetups.

Nous utilisons également Express.js et les promesses JavaScript, les packages npm Moment.js pour analyser les dates et Request pour faire des appels API.

Que se passe-t-il lorsque vous appelez `/meetupbot` ? Il fait une requête Post à `glitch-project-url/meetupbot`.

Le corps de la requête contient `user_name`, `text` et d'autres informations. L'objet de réponse est le format de réponse JSON pour l'API Slack.

Que se passe-t-il lorsque vous appelez `/meetupbot-show` ? Il fait une requête Post à `glitch-project-url/meetupbot`. Le corps de la requête contient `user_name`, `text` (comme la localisation et l'intérêt séparés par « & ») et d'autres informations.

Nous vérifions d'abord que les paramètres de localisation et d'intérêt envoyés avec la commande ne sont pas vides.

Ensuite, nous passons la localisation à la méthode `getGeocode` qui est une promesse JavaScript qui fait des appels à l'API Google Geocode et retourne la latitude et la longitude, qui est ensuite passée à la promesse `getMeetupEvents` pour obtenir la liste des meetups en faisant un appel à l'API Meetup.

L'API Meetup retourne un tableau d'objets d'événements meetup et nous parcourons ce tableau pour créer un tableau d'objets d'événements au format de réponse Slack et continuons à le pousser dans le tableau `attachment` que nous avons créé au début.

Et cette réponse avec les pièces jointes d'événements est ensuite retournée comme réponse et est affichée dans votre Slack.

Cette réponse ne sera visible que par vous (l'utilisateur qui appelle le bot) et ne dérangera pas les autres membres du canal.

Dans le code ci-dessus, nous avons 2 promesses comme suit :

* `getGeoCode()` — Cela prend la localisation comme paramètre et fait un appel API à l'API Google Geocode avec la localisation comme chaîne de requête et retourne `latlong`.
* `getMeetupEvents()` — Cela prend la localisation et l'intérêt comme paramètres et fait un appel API à l'API Meetup contenant la clé API, la latitude, la longitude, le texte ou l'intérêt et le rayon comme paramètres de chaîne de requête.

Le code ci-dessus utilise les promesses JavaScript qui sont principalement utilisées pour gérer les opérations asynchrones. Il vous permet d'écrire du code asynchrone qui est similaire en style au code synchrone.

Aide également à éviter les rappels imbriqués en utilisant `then` chaînable. Si vous avez des rappels imbriqués dans le code, cela ressemble à une structure pyramidale également connue sous le nom de "callback hell".

### MeetupBot officiel

Le MeetupBot officiel a une commande supplémentaire comme **/meetupbot-find** pour obtenir la liste des groupes meetup dans votre localisation/zone et a également un code Oauth afin que vous puissiez l'installer en cliquant sur le bouton ajouter à Slack.

Vous pouvez le trouver ici [Page de destination de MeetupBot](https://meetupbotteam.github.io/meetupbot-landing-page/) et [Dépôt github de MeetupBot](https://github.com/MeetupBotTeam/slack-meetup-bot). Commencez à l'utiliser maintenant.

Avez-vous trouvé cet article utile ? Écrivez vos commentaires ci-dessous.

Si vous avez trouvé cet article utile, partagez-le avec vos amis et donnez quelques applaudissements.

— Merci :)

Publié à l'origine [ici](http://howtocoder.com/blog/how-to-build-meetupbot-for-slack-using-nodejs).