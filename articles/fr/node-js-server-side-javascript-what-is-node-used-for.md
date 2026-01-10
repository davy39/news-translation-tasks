---
title: JavaScript côté serveur avec Node.js – À quoi sert Node ?
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-09-27T21:34:58.000Z'
originalURL: https://freecodecamp.org/news/node-js-server-side-javascript-what-is-node-used-for
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/christina-wocintechchat-com-glRqyWJgUeY-unsplash.jpg
tags:
- name: 'Back end development '
  slug: back-end-development
- name: front end
  slug: front-end
- name: JavaScript
  slug: javascript
- name: node
  slug: node
- name: node js
  slug: node-js
seo_title: JavaScript côté serveur avec Node.js – À quoi sert Node ?
seo_desc: 'The release of Node.js in 2009 by Ryan Dahl increased the scope of what
  developers could do with JavaScript. Prior to that, you could only use JavaScript
  on the client side (the browser) or frontend of web applications.

  With Node.js, developers can c...'
---

La sortie de Node.js en 2009 par Ryan Dahl a étendu le champ d'action des développeurs avec JavaScript. Avant cela, vous ne pouviez utiliser JavaScript que du côté client (le navigateur) ou sur le frontend des applications web.

Avec Node.js, les développeurs peuvent créer des applications côté serveur, des outils en ligne de commande, et bien plus encore.

Cet article n'est pas un cours accéléré sur l'utilisation de Node.js (vous trouverez des ressources pour cela dans la dernière section de cet article). Il s'agit plutôt d'une introduction à ce qu'est Node.js, ses fonctionnalités et ses cas d'utilisation.

## Qu'est-ce que Node.js ?

Node.js est un environnement d'exécution JavaScript open source qui permet aux développeurs d'exécuter du code JavaScript sur le serveur.

Si cela vous semble trop complexe à comprendre, voyez-le de cette façon : Node.js est du JavaScript qui s'exécute en dehors du navigateur — sur le serveur.

Notez que Node.js n'est pas un langage de programmation — c'est un outil.

## Qu'est-ce qui rend Node.js si spécial ?

Dans cette section, nous allons aborder certaines des fonctionnalités qui rendent Node.js si intéressant à utiliser.

L'objectif n'est pas de comparer Node.js à d'autres technologies backend, mais de vous aider à comprendre certaines de ses fonctionnalités.

### Monothreadé et asynchrone

Node.js est rapide pour exécuter des tâches (recevoir des requêtes et renvoyer des réponses) en raison de sa nature monothreadée et asynchrone.

Expliquons certains de ces termes.

Par monothreadé (single threaded), on entend que Node.js dispose d'une source unique pour gérer les requêtes. Les technologies backend multithreadées allouent un nouveau thread pour chaque nouvelle requête.

Vous pouvez imaginer un thread comme une personne qui rend un service à plusieurs individus. Un exemple concret très populaire serait un restaurant. Nous allons approfondir cet exemple avec la partie asynchrone de Node.js.

Node.js est asynchrone car il peut gérer plusieurs requêtes simultanément. Revenons à l'exemple du restaurant.

Un client arrive dans un restaurant et s'assoit en attendant un serveur. Le serveur se rend à la table du client et prend sa commande. La commande est ensuite apportée en cuisine.

Mais le serveur n'attend pas que la commande soit prête avant de passer au client suivant. Il reviendra avec ce que le client a commandé quand ce sera prêt — en attendant, le serveur passe au client suivant et répète le même processus.

L'exemple ci-dessus est similaire au fonctionnement interne de Node.js. Il est capable de traiter plusieurs requêtes en utilisant un seul thread de manière asynchrone (sans attendre la fin d'une requête avant de passer à la suivante).

Ainsi, lorsque la réponse à une requête est prête, elle est renvoyée au client.

La nature monothreadée et asynchrone de Node.js le rend très rapide et idéal pour créer des applications intensives en données et en temps réel.

### JavaScript partout

Un autre avantage de l'utilisation de Node.js en tant que développeur web est la possibilité d'utiliser JavaScript sur le frontend et le backend de votre application web.

Avant la sortie de Node.js, les développeurs web devaient apprendre un langage de programmation différent pour construire le backend de leurs applications web.

Bien sûr, certains développeurs utilisent toujours des langages différents pour leur backend, mais Node.js permet d'utiliser facilement un seul langage — JavaScript — si vous le souhaitez.

### Temps d'exécution rapide

Node.js est construit sur le moteur JavaScript V8 de Google qui offre des performances très élevées. Cela permet à Node d'exécuter les requêtes rapidement.

### Compatibilité multiplateforme

Node.js supporte de nombreuses plateformes majeures. Vous pouvez donc écrire votre code et il s'exécutera sur Windows, MacOS, LINUX, UNIX et même sur certains appareils mobiles.

## À quoi sert Node ?

Voici quelques-unes des choses sympas que vous pouvez faire avec Node.js :

* Créer des serveurs web HTTP.
* Générer des pages web de manière dynamique.
* Collecter et envoyer des données de formulaires vers une base de données.
* Créer, lire, mettre à jour et supprimer des données stockées dans une base de données.
* Créer des APIs.
* Construire des outils en ligne de commande.
* Lire, écrire, déplacer, supprimer et ouvrir/fermer des fichiers sur un serveur.

## Résumé

Dans cet article, nous avons parlé de Node.js. Nous avons d'abord vu ce que c'est réellement.

Nous avons ensuite abordé certaines des fonctionnalités qui permettent à Node.js de se démarquer.

Enfin, nous avons vu une liste de la façon dont vous pouvez utiliser Node.js.

### Comment apprendre Node.js

Maintenant que vous avez eu une brève introduction à ce qu'est Node.js, ses fonctionnalités et son utilité, voici quelques ressources que vous pouvez utiliser pour apprendre à utiliser Node.js :

* [La certification Back End Development and APIs de freeCodeCamp](https://www.freecodecamp.org/learn/back-end-development-and-apis/). Vous apprendrez à écrire des applications backend avec Node.js et npm. Vous construirez également des applications web avec le Framework Express, ainsi que MongoDB et la bibliothèque Mongoose.
* [Un cours de 8 heures sur la chaîne YouTube freeCodeCamp.org](https://youtu.be/Oe421EPjeBE) qui vous enseignera Node.js et Express.
* [Un cours de 10 heures basé sur des projets sur la chaîne YouTube freeCodeCamp.org](https://www.youtube.com/watch?v=qwfE7fSVaZM&list=RDCMUC8butISFwT-Wl7EV0hUK0BQ&index=2). Vous construirez quatre projets à partir des connaissances acquises dans le cours de 8 heures ci-dessus.

Bon code !