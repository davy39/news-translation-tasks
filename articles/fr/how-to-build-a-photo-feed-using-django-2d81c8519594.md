---
title: Comment créer un fil de photos avec Django
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-03T15:34:18.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-photo-feed-using-django-2d81c8519594
coverImage: https://cdn-media-1.freecodecamp.org/images/0*lYy3cb9EF5I8Pz1E.png
tags:
- name: education
  slug: education
- name: Life lessons
  slug: life-lessons
- name: 'self-improvement '
  slug: self-improvement
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Comment créer un fil de photos avec Django
seo_desc: 'By Ogundipe Samuel

  Today, we will make a real-time photo feed framework using Django and Pusher. This
  is like a mini Instagram, but without the comments and filter functionality.


  A basic understanding of Django and jQuery is needed to follow this tu...'
---

Par Ogundipe Samuel

Aujourd'hui, nous allons créer un framework de fil de photos en temps réel en utilisant Django et Pusher. C'est comme un mini Instagram, mais sans les commentaires et les fonctionnalités de filtres.

![Image](https://cdn-media-1.freecodecamp.org/images/0*aTITCCoNi8aLM4_G.gif)

Une compréhension de base de Django et jQuery est nécessaire pour suivre ce tutoriel.

### Installation de Django

Tout d'abord, vous devez installer la bibliothèque Django (si ce n'est pas déjà fait).

Pour installer Django, exécutez :

Après avoir installé Django, il est temps de créer notre projet. Ouvrez un terminal et créez un nouveau projet en utilisant la commande suivante :

Dans la commande ci-dessus, nous avons créé un nouveau projet appelé `photofeed`. L'étape suivante sera de créer une application dans notre nouveau projet. Pour cela, exécutons les commandes suivantes :

Une fois que nous avons terminé la configuration de la nouvelle application, Django doit connaître notre nouvelle application. Pour cela, nous allons dans notre fichier `feed\settings.py` et ajoutons l'application de messagerie à nos applications installées comme suit :

Après avoir fait ce qui précède, il est temps d'exécuter l'application et de voir si tout s'est bien passé. Dans notre terminal, nous exécutons :

Si nous naviguons dans notre navigateur vers `http://localhost:8000`, nous devrions voir ce qui suit :

![Image](https://cdn-media-1.freecodecamp.org/images/0*Bh4MhbFyoq9kt2XQ.png)

### Configuration d'une application sur Pusher

À ce stade, Django est prêt et configuré. Nous devons configurer Pusher ensuite, ainsi que récupérer nos identifiants d'application. Si vous ne l'avez pas déjà fait, inscrivez-vous à un compte [Pusher](https://pusher.com/signup) gratuit et créez une nouvelle application, puis copiez votre clé secrète, votre clé d'application et votre identifiant d'application.

![Image](https://cdn-media-1.freecodecamp.org/images/0*lYy3cb9EF5I8Pz1E.png)

L'étape suivante consiste à installer les bibliothèques requises :

Dans la commande bash ci-dessus, nous avons installé un package, Pusher. — Pusher : il s'agit de la bibliothèque officielle Pusher pour Python. Nous utiliserons cette bibliothèque pour déclencher et envoyer nos messages à l'API HTTP de Pusher.

### Création de notre application

Tout d'abord, créons une classe de modèle, qui générera notre structure de base de données. Ouvrons `feed\models.py` et remplaçons-le par ce qui suit :

Dans le bloc de code ci-dessus, nous avons défini un modèle appelé `Feed`. La table Feed se composera des champs suivants :

* Un champ pour stocker la description de la photo
* Un champ pour stocker la photo Dans le code ci-dessus, lors de la déclaration de notre champ document, nous avons inclus un attribut `upload_to`, que nous avons défini sur `static/documents`
Veuillez noter que ce chemin est relatif au chemin de `DJANGO MEDIA ROOT`, que nous allons définir maintenant.

Dans cet article, nous allons définir `MEDIA_ROOT` sur le dossier static dans notre application `feed`, afin qu'il puisse être servi en tant que fichier statique. Pour cela, déplaçons-nous vers notre fichier `photofeed/settings.py` et ajoutons le code ci-dessous à notre fichier, immédiatement après la déclaration `STATIC_URL`.

### Exécution des migrations

Nous devons effectuer des migrations et les exécuter, afin que notre table de base de données puisse être créée. Pour cela, exécutons ce qui suit dans notre terminal :

### Création de nos vues

Nos vues font référence au(x) fichier(s) qui contiennent la logique derrière l'application, souvent appelés `Controller`. Ouvrons notre fichier `views.py` dans notre dossier `feed` et remplaçons-le par ce qui suit :

Dans le code ci-dessus, nous avons défini trois fonctions principales qui sont :

* index
* pusher_authentication_
* push_feed

Dans la fonction `index`, nous récupérons toutes les photos disponibles dans la base de données. Les photos sont ensuite rendues dans la vue. Cela permet à un nouvel utilisateur de voir tous les fils précédents qui sont disponibles.

Dans la fonction `pusher_authentication`, nous vérifions que l'utilisateur actuel peut accéder à notre canal privé.

Dans la fonction `push_feed`, nous vérifions s'il s'agit d'une requête POST, puis nous essayons de valider notre formulaire avant de l'enregistrer dans la base de données. (Le formulaire utilisé dans cette méthode nommé `DocumentForm` n'est pas encore disponible. Nous allons le créer bientôt.) Après la validation du formulaire, nous plaçons ensuite notre appel à la bibliothèque Pusher pour une interaction en temps réel.

### Création de la classe de formulaire

Un formulaire Django gère la saisie des utilisateurs, la valide et la transforme en objets Python. Ils ont également quelques méthodes de rendu pratiques. Créons un fichier appelé `forms.py` dans notre dossier `feed` et ajoutons le contenu suivant :

Dans le bloc de code ci-dessus, nous avons importé notre modèle Feed et l'avons utilisé pour créer un formulaire. Ce formulaire gérera désormais la validation et le téléchargement des images dans le bon dossier.

### Remplissage du fichier urls.py

Ouvrons notre fichier `photofeed\urls.py` et remplaçons-le par ce qui suit :

Qu'est-ce qui a changé dans ce fichier ? Nous avons ajouté 3 nouvelles routes au fichier. Nous avons défini le point d'entrée et l'avons assigné à notre fonction `index`. Nous avons également défini l'URL push_feed et l'avons assignée à notre fonction `push_feed`. Cela sera responsable de l'envoi des mises à jour à Pusher en temps réel. Enfin, le point de terminaison `pusher_authentication` gère l'authentification de notre canal privé.

### Création des fichiers HTML

Maintenant, nous devons créer le fichier index.html que nous avons référencé comme modèle pour notre fonction index. Créons un nouveau dossier dans notre dossier `feed` appelé `templates`. Ensuite, créons un fichier appelé `index.html` dans notre dossier `templates` et remplaçons-le par le code ci-dessous :

Dans cet extrait HTML, notez que nous avons inclus certaines bibliothèques requises telles que :

* Bootstrap CSS
* Bibliothèque JavaScript jQuery
* Bibliothèque JavaScript Pusher

### Liaisons Pusher et extrait jQuery

C'est tout ! Maintenant, une fois qu'une photo est téléchargée, elle est également diffusée et nous pouvons écouter en utilisant notre canal pour mettre à jour le fil en temps réel. Ci-dessous se trouve notre exemple d'extrait jQuery utilisé pour gérer le téléchargement de fichiers ainsi que les mises à jour en temps réel de Pusher.

Ci-dessous une image de ce que nous avons construit :

![Image](https://cdn-media-1.freecodecamp.org/images/0*JzA7njPCUC9-ozFM.gif)

### Conclusion

Dans cet article, nous avons couvert comment créer un fil de photos en temps réel en utilisant Django et Pusher ainsi que le passage de jetons CSRF dans les requêtes AJAX en utilisant Django.

La base de code de ce tutoriel est disponible dans un [dépôt public Github](https://github.com/samuelayo/pusher_django_photo_feed). Vous pouvez la télécharger à des fins éducatives.

Avez-vous une meilleure façon de construire notre application, des réserves ou des commentaires, faites-le nous savoir dans les commentaires. N'oubliez pas que partager, c'est apprendre.

Cet article a été initialement publié sur le blog de Pusher [ici](https://blog.pusher.com/build-a-photo-feed-using-django/)