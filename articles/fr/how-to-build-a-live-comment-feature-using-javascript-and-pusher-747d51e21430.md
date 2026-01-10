---
title: Comment créer une fonctionnalité de commentaires en direct en utilisant JavaScript
  et Pusher
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-02T17:07:20.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-live-comment-feature-using-javascript-and-pusher-747d51e21430
coverImage: https://cdn-media-1.freecodecamp.org/images/0*AFHx4TZQ480CmwUU.png
tags:
- name: Apps
  slug: apps-tag
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Comment créer une fonctionnalité de commentaires en direct en utilisant
  JavaScript et Pusher
seo_desc: 'By Rahat Khanna

  These days “Social” has become the buzzword and we all want our apps to be the center
  of these amazing social conversations. Comments on a post, video, update or any
  feature of your new app is a great way to add fun and enriching soci...'
---

Par Rahat Khanna

De nos jours, le terme « Social » est devenu le mot à la mode et nous voulons tous que nos applications soient au centre de ces conversations sociales incroyables. Les commentaires sur une publication, une vidéo, une mise à jour ou toute autre fonctionnalité de votre nouvelle application sont un excellent moyen d'ajouter des conversations sociales amusantes et enrichissantes à votre application.

Si ces conversations peuvent être en temps réel, c'est encore mieux. Nous allons donc discuter dans cet article de la manière dont nous pouvons créer une fonctionnalité de commentaires en temps réel pour nos applications web en utilisant [Pusher](https://pusher.com/) avec JavaScript Vanilla en front-end et [Node.js](https://nodejs.org/en/) en back-end.

Nous appellerons ce système de commentaires en temps réel **Flash Comments**, qui peut être réutilisé pour plusieurs publications/fonctionnalités dans votre application et peut générer des conversations incroyables en temps réel. Seules des connaissances de base en HTML, CSS et JavaScript sont nécessaires pour suivre ce billet de blog.

Notre application ressemblera à quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/0*pDZl2GiJiqbr2pBK.gif)

### Sections

* Brève introduction à Pusher
* S'inscrire avec Pusher
* Application Node.js et Express pour exposer une API de création de commentaires et déclencher un événement Pusher
* Front-End utilisant JavaScript Vanilla pour s'abonner à un canal

**Passez les deux premières sections si vous êtes déjà inscrit avec Pusher.**

### Brève introduction à Pusher

Pusher est une plateforme incroyable qui abstrait les complexités de la mise en œuvre d'un système en temps réel par nous-mêmes en utilisant WebSockets ou Long Polling. Nous pouvons instantanément ajouter des fonctionnalités en temps réel à nos applications web existantes en utilisant Pusher, car il prend en charge une grande variété de kits de développement logiciel (SDK).

Des kits d'intégration sont disponibles pour une variété de bibliothèques front-end comme Backbone, React, Angular et jQuery, ainsi que pour des plateformes/langages back-end comme .NET, Java, Python, Ruby, PHP et GO.

### S'inscrire avec Pusher

Vous pouvez créer un compte gratuit sur Pusher [ici](http://pusher.com/signup). Après votre inscription et votre première connexion, vous serez invité à créer une nouvelle application comme le montre l'image ci-dessous. Vous devrez remplir certaines informations sur votre projet ainsi que la bibliothèque front-end ou le langage back-end avec lequel vous allez construire votre application. Vous avez également la possibilité de sélectionner le cluster de Pusher en fonction de la distribution géographique de vos utilisateurs. J'ai choisi `ap2 (Mumbai, Inde)` car je pourrais construire une application pour la région de l'Inde.

![Image](https://cdn-media-1.freecodecamp.org/images/0*AFHx4TZQ480CmwUU.png)

Pour cet article en particulier, nous sélectionnerons JavaScript pour le front-end et Node.js pour le back-end comme le montre l'image ci-dessus.

Cela vous montrera simplement un ensemble de codes d'exemple de démarrage pour ces sélections, mais vous pouvez utiliser n'importe quel kit d'intégration plus tard avec cette application.

![Image](https://cdn-media-1.freecodecamp.org/images/0*_dzai36l6cdqlv90.png)

### Application Node.js

Vous pouvez créer un nouveau dossier nommé `**flash-comments**` et exécuter la commande suivante à la racine du dossier :

Il vous demandera une série d'informations concernant l'application et créera un nouveau fichier `**package.json**` à l'intérieur de votre dossier.

Nous utiliserons le framework Express, simple et populaire, dans Node.js. Maintenant, nous allons installer les packages importants qui seront utilisés dans notre application Express minimale.

Après avoir installé tous les modules `npm` requis, nous allons créer un fichier point d'entrée pour notre application Node.js nommé `server.js` à l'intérieur du dossier racine. Ajoutez le code de base suivant pour un serveur HTTP à exécuter en utilisant le port `9000`.

Pusher dispose d'un module NPM open source pour les intégrations Node.js que nous allons utiliser. Il fournit un ensemble de méthodes utilitaires pour s'intégrer avec les API de Pusher en utilisant un `**appId**`, une `**key**` et un `**secret**` uniques. Nous allons d'abord installer le module `pusher` `npm` en utilisant la commande suivante :

Maintenant, nous pouvons utiliser require pour obtenir le module Pusher et créer une nouvelle instance en passant un objet d'options avec des clés importantes pour initialiser notre intégration. Pour cet article, j'ai mis des clés aléatoires. Vous devrez les obtenir pour votre application depuis le tableau de bord de Pusher.

Vous devrez remplacer le `appId`, la `key` et le `secret` par des valeurs spécifiques à votre propre application. Après cela, nous allons écrire le code pour une nouvelle API qui sera utilisée pour créer un nouveau commentaire. Cette API exposera la route `/comment` avec la méthode HTTP `POST` et attendra un objet pour le commentaire avec les propriétés `name`, `email` et `comment`. Ajoutez le code suivant à votre fichier `server.js` avant la partie `app.listen`.

Dans le code ci-dessus, nous avons extrait les données de `req.body` dans un objet `newComment` et les avons utilisées pour appeler la méthode `trigger` sur l'instance `Pusher`.

### Concepts importants de Pusher

#### Canal

Dans Pusher, nous avons un regroupement conceptuel appelé « canaux » et il fournit le moyen de base de filtrer les données dans Pusher. Un canal peut représenter de nombreuses entités dans une application réelle. Par exemple : Dans notre application de commentaires, un canal peut être des commentaires pour un article spécifique, une vidéo, un billet de blog, une photo ou une diffusion en direct d'un événement.

Nous créerions un nouvel identifiant de canal unique pour chacune de ces entités afin d'identifier ou de regrouper de manière unique les données telles que les commentaires associés à l'une de ces entités. Deux vidéos en direct uniques doivent également avoir des canaux séparés afin que nous puissions afficher le flux de commentaires en direct respectif sur leurs pages respectives.

Nous allons donc créer un nouveau canal unique pour chaque entité avec leur identifiant unique. Par exemple, un canal de commentaires pour une vidéo YouTube peut être nommé `comments-youtube-234`.

Il existe trois types de canaux :

* **Canal Public** — peut être souscrit par quiconque connaît le nom du canal.
* **Canal Privé** — canal auquel peuvent s'abonner uniquement les utilisateurs autorisés. Si le nom du canal a un préfixe `private-`, il sera considéré comme un canal privé.
* **Canal de Présence** — il s'agit d'un type de canal spécial similaire au canal privé, car seuls les utilisateurs autorisés peuvent s'y abonner. La liste des abonnés est également maintenue et notifiée aux autres utilisateurs. Le nom du canal doit avoir un préfixe `presence-`.

Nous utiliserons un canal public dans notre billet de blog que nous nommons **flash-comments**, mais vous devriez idéalement utiliser un canal privé pour les systèmes de commentaires avec un nom unique pour chaque entité pour laquelle vous souhaitez activer la fonctionnalité de commentaires.

### Événement

Maintenant, les données réelles dans Pusher sont transmises via des événements, qui est le moyen principal d'emballer les messages. Un événement peut être déclenché par un back-end ou même par un client dans des cas spéciaux pour un canal particulier. Un canal est nécessaire pour garantir que votre message atteint le destinataire prévu.

Nous donnons un nom unique à chaque événement afin que nous puissions configurer des gestionnaires pour recevoir et traiter ces messages d'événement à chaque extrémité client qui s'est abonnée à un canal.

### Méthode de déclenchement de Pusher

Maintenant, nous allons comprendre notre code côté serveur pour envoyer un événement au canal Pusher `**flash-comments**`.

Nous utilisons la méthode `.trigger(channel-name, event-name, payload)` pour envoyer un événement depuis le serveur chaque fois que l'API `POST` est appelée pour créer un nouveau commentaire. Pour la simplicité de cet article, nous n'utiliserons aucune base de données pour sauvegarder et persister les commentaires, mais dans un système de production, vous devrez stocker un commentaire correspondant à un identifiant d'entité unique comme un identifiant de vidéo YouTube ou un identifiant de billet de blog.

Maintenant, nous pouvons exécuter notre serveur en utilisant la commande `node server`. Notre service web sera accessible à l'URL `http://localhost:9000/comment`. Nous pouvons écrire une requête `POST` en utilisant une extension Chrome comme [Postman](https://www.getpostman.com/) ou même [**curl**](https://curl.haxx.se/) pour tester si elle retourne `{ "created":"true" }`.

La commande curl pour tester votre API `POST` sera la suivante :

### Front-End utilisant JavaScript Vanilla

Maintenant, nous allons écrire la partie la plus cruciale, le code front-end en utilisant JavaScript Vanilla. Dans le code front-end, nous allons développer une section de boîte de commentaires qui aura les deux fonctionnalités suivantes :

* **Afficher** tous les commentaires en direct ajoutés au canal avec une animation fluide
* **Ajouter** un nouveau commentaire aux commentaires en direct en appelant l'API `POST` que nous venons de créer

### Étape 1 : Créer un dossier nommé public et créer un fichier index.html

Nous avons déjà écrit du code dans notre fichier `server.js` pour servir du contenu statique depuis le dossier `public`, nous allons donc écrire tout notre code front-end dans ce dossier.

Veuillez créer un nouveau dossier `public` et également créer un fichier `index.html` vide pour l'instant.

### Étape 2 : Ajouter le code de base à notre index.html

Nous allons ajouter un code de base pour configurer la structure de base de notre application web comme `Header`, et `Sections` où le contenu comme une vidéo ou un billet de blog peut être mis, ainsi que la section qui contiendra notre boîte de `**Flash Comments**`.

### Étape 3 : Créer le fichier style.css

Maintenant, nous allons également créer un fichier `style.css` pour contenir le code CSS important pour styliser notre application web et le composant `**flash comments**`. Nous allons ajouter des styles de base pour rendre notre squelette.

### Étape 4 : Ajouter la bibliothèque pusher.js et créer app.js

Maintenant, nous allons ajouter la bibliothèque pusher.js disponible sur son CDN pour l'utiliser afin de nous intégrer au système Pusher en utilisant du code JavaScript simple. Veuillez ajouter la balise de script suivante à la fin du body avant sa balise de fermeture :

Créez également un nouveau fichier `app.js` où nous allons écrire tout notre code et importer également le même fichier dans notre fichier `index.html` après la balise de script pour importer le fichier `pusher.js`.

Dans notre fichier `app.js`, nous allons maintenant écrire le code pour initialiser l'instance Pusher en utilisant la clé API client unique que nous avons obtenue depuis le tableau de bord Pusher. Nous allons également passer un objet spécifiant le cluster et définir le drapeau encrypted à true afin que tous les messages et communications soient chiffrés. Nous allons également utiliser `pusher.subscribe('channel-name')` pour écouter tous les événements pour un canal spécifique.

Nous allons créer une IIFE JavaScript (Immediately Invoking Functions) pour créer une portée privée afin de ne pas polluer la portée globale. Veuillez ajouter le code suivant au fichier `app.js` :

### Étape 5 : Créer un formulaire pour ajouter un nouveau commentaire

Maintenant, nous allons créer les contrôles de formulaire pour permettre à l'utilisateur de saisir son nom, son email et le texte du commentaire pour créer un nouveau commentaire en utilisant notre API Node.js et Pusher. Nous allons ajouter le code HTML suivant à l'intérieur de la balise de formulaire existante pour créer le formulaire :

Dans le code du formulaire ci-dessus, nous avons utilisé des validations HTML5 comme `required` et `type=email` qui n'autoriseront pas l'utilisateur à laisser ces champs vides ou à soumettre un email invalide. Ces validations fonctionneront automatiquement dans la plupart des navigateurs qui supportent les validations de formulaire HTML5.

De plus, nous allons ajouter le CSS suivant pour styliser le formulaire :

Après avoir construit le formulaire visuel, nous devons maintenant attacher un gestionnaire d'événements à l'événement `Submit` du formulaire. Nous allons le faire en utilisant le code suivant dans le fichier `app.js`, probablement en haut après les déclarations `var` :

Maintenant, nous allons écrire le code pour l'implémentation du gestionnaire `addNewComment` avec le code suivant :

Nous utilisons une requête XHR native pour faire une requête AJAX à l'API Node. Vous pouvez utiliser soit jQuery AJAX, soit une méthode `ajax` spécifique à un framework dans votre application. Maintenant, si nous exécutons notre application, remplissons le formulaire et le soumettons, nous verrons un message `Success: { created: true }` dans la console des outils de développement de notre navigateur.

De plus, nous pouvons voir le tableau de bord Pusher pour voir les statistiques sur les messages d'événements envoyés pour un canal.

![Image](https://cdn-media-1.freecodecamp.org/images/0*nxysjGfuHjjcCK1k.png)

### Étape 6 : Afficher la liste des commentaires reçus pour ce canal

Maintenant, nous allons nous lier à l'événement `new_comment` sur ce canal `flash-comments` afin que nous puissions recevoir tout message concernant la création de nouveaux commentaires effectués depuis n'importe quel client en temps réel, et nous pouvons afficher tous ces commentaires.

Nous allons d'abord ajouter un modèle pour un nouveau commentaire dans notre fichier `index.html` à l'intérieur de la balise div avec `id="comments-list"`.

Maintenant, nous allons écrire le code JavaScript pour nous lier à l'événement new_comment sur l'instance de canal pusher à laquelle nous nous sommes abonnés. Chaque fois que l'événement `new_comment` sera déclenché, nous prendrons le contenu innerHTML du modèle et remplacerons les espaces réservés `{{name}}, {{email}} & {{comment}}` par les données passées avec l'événement et les ajouterons à l'élément div `comments-list`.

En utilisant le code ci-dessus, une nouvelle balise div représentant le nouveau commentaire sera automatiquement créée et ajoutée au conteneur `comments-list`.

Nous allons maintenant ajouter le CSS suivant pour afficher correctement la liste des commentaires et également animer chaque fois qu'un nouveau commentaire apparaît dans la liste :

Maintenant, vous pouvez exécuter l'application que nous avons construite, soit dans deux navigateurs différents, soit dans une fenêtre de navigateur normale et l'autre en mode navigation privée, et ajouter plusieurs commentaires. Nous pouvons voir que les commentaires en direct seront ajoutés en temps réel avec une animation fluide.

![Image](https://cdn-media-1.freecodecamp.org/images/0*EU6UJeB7p1ZyImwq.gif)

Le code complet de ce tutoriel est disponible sur [GitHub](https://github.com/mappmechanic/flash-comments).

### Conclusion

Nous avons construit une belle application web avec une fonctionnalité de commentaires en direct en utilisant Pusher, Node.js et JavaScript Vanilla. Nous pouvons utiliser ce composant avec n'importe laquelle de nos applications et activer les commentaires en direct pour une variété d'entités sociales comme les vidéos, les billets de blog, les sondages, les articles et les diffusions en direct.

Nous avons utilisé le serveur Node.js pour créer une API REST afin d'obtenir un nouveau commentaire et déclencher un événement Pusher sur un canal spécifique. Pour toute application réelle, nous pouvons prendre un identifiant unique pour chaque entité et utiliser un nom de canal unique pour chaque entité. Dans un scénario de production, nous pouvons également stocker les commentaires dans un stockage persistant et les récupérer plus tard.

Nous avons également créé une application Front-End, qui se connectera à l'API Pusher en utilisant la bibliothèque pusher.js. Nous avons créé un formulaire pour appeler l'API Node qui déclenchera l'événement `new_comment`. Les commentaires sont affichés en temps réel avec une animation en utilisant la méthode bind sur l'instance de canal.

Cet article a été initialement publié sur le [blog de Pusher](https://blog.pusher.com/build-live-comments-feature-using-javascript/).