---
title: Comment créer un statut de livraison de message dans Django
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-03T15:56:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-message-delivery-status-in-django-e8d1eb2e8b6a
coverImage: https://cdn-media-1.freecodecamp.org/images/0*iF8r7xsxvctowLcc.gif
tags:
- name: education
  slug: education
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Comment créer un statut de livraison de message dans Django
seo_desc: 'By Ogundipe Samuel

  Today, we will make a real-time message delivery status framework with Django and
  Pusher.


  A basic understanding of Django and Vue is needed in order to follow this tutorial.

  Setting up Django

  First, we need to install the Python D...'
---

Par Ogundipe Samuel

Aujourd'hui, nous allons créer un framework de statut de livraison de message en temps réel avec Django et Pusher.

![Image](https://cdn-media-1.freecodecamp.org/images/0*iF8r7xsxvctowLcc.gif)

Une compréhension de base de Django et Vue est nécessaire pour suivre ce tutoriel.

### Installation de Django

Tout d'abord, nous devons installer la bibliothèque Python Django si nous ne l'avons pas déjà. Pour installer Django, nous exécutons :

Après avoir installé Django, il est temps de créer notre projet. Ouvrez un terminal et créez un nouveau projet en utilisant la commande suivante :

[https://gist.github.com/4896cf41463ff83e191949a02bbead23](https://gist.github.com/4896cf41463ff83e191949a02bbead23)

Dans la commande ci-dessus, nous avons créé un nouveau projet appelé `pusher_message`. L'étape suivante sera de créer une application dans notre nouveau projet. Pour cela, exécutons les commandes suivantes :

Une fois que nous avons terminé la configuration de la nouvelle application, nous devons informer Django de notre nouvelle application, alors nous allons dans notre fichier `pusher_message\settings.py` et ajoutons l'application de message à nos applications installées comme vu ci-dessous :

Après avoir fait ce qui précède, il est temps pour nous d'exécuter l'application et de voir si tout s'est bien passé.

Dans notre terminal, nous exécutons :

Si nous naviguons dans notre navigateur vers `http://localhost:8000`, nous devrions voir ce qui suit :

### Configurer une application sur Pusher

À ce stade, Django est prêt et configuré. Nous devons maintenant configurer Pusher, ainsi que récupérer nos identifiants d'application.

Nous devons nous inscrire sur [Pusher](https://pusher.com/signup), créer une nouvelle application, et également copier notre clé d'application secrète et l'identifiant de l'application.

L'étape suivante consiste à installer les bibliothèques requises :

Dans la commande bash ci-dessus, nous avons installé un package, `pusher`. Il s'agit de la bibliothèque officielle Pusher pour Python, que nous utiliserons pour déclencher et envoyer nos messages à Pusher.

### Création de notre application

Tout d'abord, créons une classe de modèle, qui générera notre structure de base de données. Ouvrons `message\models.py` et remplaçons le contenu par ce qui suit :

Dans le bloc de code ci-dessus, nous avons défini un modèle appelé `Conversation`. La table de conversation se compose des champs suivants :

* Un champ pour lier le message à l'utilisateur qui l'a créé
* Un champ pour stocker le message
* Un champ pour stocker le statut du message
* Un champ pour stocker la date et l'heure de création du message

### Exécution des migrations

Nous devons effectuer des migrations et les exécuter afin que notre table de base de données puisse être créée. Pour cela, exécutons ce qui suit dans notre terminal :

### Création de nos vues

Dans Django, les vues ne font pas nécessairement référence à la structure HTML de notre application. En fait, nous pouvons la voir comme notre `Controller`, comme on l'appelle dans certains autres frameworks.

Ouvrons notre fichier `views.py` dans notre dossier `message` et remplaçons le contenu par ce qui suit :

Dans le code ci-dessus, nous avons défini quatre fonctions principales qui sont :

* `index`
* `broadcast`
* `conversation`
* `delivered`

Dans la fonction `index`, nous avons ajouté le décorateur login_required, et nous avons également passé l'argument login URL qui n'existe pas encore, car nous devrons le créer dans le fichier `urls.py`. De plus, nous avons rendu un modèle par défaut appelé `chat.html` que nous créerons également bientôt.

Dans la fonction `broadcast`, nous avons récupéré le contenu du message envoyé, l'avons enregistré dans notre base de données, et enfin déclenché une requête Pusher en passant notre dictionnaire de message, ainsi qu'un canal et un nom d'événement. Dans la fonction `conversations`, nous avons simplement récupéré toutes les conversations et les avons retournées sous forme de réponse JSON.

Enfin, nous avons la fonction `delivered`, qui est la fonction qui gère le statut de livraison de notre message.

Dans cette fonction, nous obtenons la conversation par l'ID fourni. Nous vérifions ensuite que l'utilisateur qui souhaite déclencher l'événement de livraison n'est pas l'utilisateur qui a envoyé le message en premier lieu. De plus, nous passons le `socket_id` afin que Pusher ne diffuse pas l'événement à la personne qui l'a déclenché.

Le `socket_id` sert d'identifiant pour la connexion socket qui a déclenché l'événement.

### Remplissage du fichier urls.py

Ouvrons notre fichier `pusher_message\urls.py` et remplaçons-le par ce qui suit :

Qu'est-ce qui a changé dans ce fichier ? Nous avons ajouté six nouvelles routes au fichier. Nous avons défini le point d'entrée et l'avons assigné à notre fonction `index`. Ensuite, nous avons défini l'URL de connexion, que le décorateur `login_required` essaierait d'accéder pour authentifier les utilisateurs.

Nous avons utilisé la fonction `auth` par défaut pour la gérer, mais nous avons passé notre propre modèle personnalisé pour la connexion, que nous créerons bientôt.

Ensuite, nous avons défini les routes pour le déclencheur de message `conversation`, toutes les `conversations`, et enfin la `delivered` conversation.

### Création des fichiers HTML

Maintenant, nous devons créer deux pages HTML pour que notre application fonctionne correctement. Nous avons référencé deux pages HTML au cours de la construction de l'application.

Créons un nouveau dossier dans notre dossier `messages` appelé `templates`.

Ensuite, créons un fichier appelé `login.html` dans notre dossier `templates` et remplaçons-le par ce qui suit :

### Composant Vue et liaisons Pusher

C'est tout ! Maintenant, chaque fois qu'un nouveau message est livré, il sera diffusé et nous pouvons écouter, en utilisant notre canal, pour mettre à jour le statut en temps réel. Ci-dessous se trouve notre exemple de composant écrit en utilisant Vue.js.

**Veuillez noter :** Dans le composant Vue ci-dessous, une nouvelle fonction appelée `**queryParams**` a été définie pour sérialiser notre corps POST afin qu'il puisse être envoyé en tant que `**x-www-form-urlencoded**` au serveur au lieu d'un `**payload**`. Nous avons fait cela parce que Django ne peut pas gérer les requêtes arrivant en tant que `**payload**`.

Ci-dessous se trouve l'image démontrant ce que nous avons construit :

![Image](https://cdn-media-1.freecodecamp.org/images/0*iF8r7xsxvctowLcc.gif)

### Conclusion

Dans cet article, nous avons couvert comment créer un statut de livraison de message en temps réel en utilisant Django et Pusher. Nous avons passé en revue l'exemption de certaines fonctions des vérifications CSRF, ainsi que l'exemption du diffuseur de recevoir un événement qu'il a déclenché.

Le code est hébergé sur un [dépôt GitHub public](https://github.com/samuelayo/pusher_django_message_delivery). Vous pouvez le télécharger à des fins éducatives.

Avez-vous une meilleure façon de construire notre application, des réserves ou des commentaires ? Faites-le nous savoir dans les commentaires. N'oubliez pas, partager, c'est apprendre.

Cet article a été publié à l'origine par l'auteur dans le blog de pusher [ici](https://blog.pusher.com/how-to-build-a-message-delivery-status-in-django/).

Cette version a été éditée pour plus de clarté et peut sembler différente de l'article original.