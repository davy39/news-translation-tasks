---
title: Comment commencer à utiliser Firebase Hosting
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2018-02-08T15:19:38.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-using-firebase-hosting-439d4bd45cb6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*q2NlUEQNkZmI6KLvnT1tzA.png
tags:
- name: Firebase
  slug: firebase
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
- name: Web Hosting
  slug: web-hosting
seo_title: Comment commencer à utiliser Firebase Hosting
seo_desc: 'Interested in learning JavaScript? Get my ebook at jshandbook.com


  Firebase is a mobile and web application development platform that was developed
  by Firebase, Inc. in 2011. It was acquired by Google in 2014 and rolled up into
  the Google Cloud servi...'
---

> Intéressé par l'apprentissage de JavaScript ? Obtenez mon ebook sur [jshandbook.com](https://jshandbook.com/)

Firebase est une plateforme de développement d'applications mobiles et web qui a été développée par Firebase, Inc. en 2011. Elle a été acquise par Google en 2014 et intégrée au service Google Cloud. Aujourd'hui, c'est un produit phare de l'offre Google Cloud.

Firebase est un produit complexe et articulé, principalement ciblé pour les applications mobiles.

L'une de ses fonctionnalités moins connues, que nous allons discuter dans cet article, est le service d'hébergement web avancé de Firebase.

### Fonctionnalités de Firebase Hosting

Firebase Hosting fournit l'hébergement pour les sites web statiques, tels que

* les sites que vous pouvez générer en utilisant des générateurs de sites statiques
* les sites construits avec des plateformes CMS côté serveur, à partir desquels vous générez une copie statique du site web

Vous pouvez héberger n'importe quoi tant que ce n'est pas dynamique. Un blog WordPress, par exemple, est presque toujours un bon candidat pour être un site statique si vous utilisez Disqus ou les commentaires Facebook.

Firebase Hosting livre les fichiers via le CDN Fastly, en utilisant HTTPS et fournit un certificat SSL automatique, avec support de domaine personnalisé.

Son **niveau gratuit est généreux**, avec des plans économiques disponibles si vous le dépassez. Il est très convivial pour les développeurs, fournit un outil d'interface CLI, un processus de déploiement facile et des retours en arrière en un clic.

### Pourquoi devriez-vous utiliser Firebase Hosting ?

Firebase peut être un bon choix pour déployer des sites web statiques et des applications monopages.

J'aime utiliser Firebase Hosting principalement parce que j'ai testé de nombreux fournisseurs différents et Firebase offre une **vitesse incroyable** dans plusieurs emplacements géographiques sans avoir besoin d'un CDN séparé, puisque **le CDN est intégré** gratuitement.

Bien que d'avoir son propre VPS soit une très bonne option, **la surcharge de gestion de son propre serveur** pour un simple site web n'en vaut tout simplement pas la peine. Je préfère me concentrer sur le contenu plutôt que sur les opérations, tout comme je déployerais une application sur Heroku.

Firebase est encore plus facile à configurer que Heroku.

### Installer l'outil CLI de Firebase

Installez le CLI de Firebase avec

```
npm install -g firebase-tools
```

ou

```
yarn global add firebase-tools
```

Authentifiez-vous avec le compte Google (je suppose que vous avez déjà un compte Google) en exécutant

```
firebase login
```

### Créer un projet dans Firebase

Allez sur [https://console.firebase.google.com/](https://console.firebase.google.com/) et créez un nouveau projet.

![Image](https://cdn-media-1.freecodecamp.org/images/0hzGqiYVSrZev8ogQPbGuw7yIa6K4VZWCgSq)

Maintenant, dans la console, exécutez ce qui suit à partir du dossier racine du site sur lequel vous travaillez :

```
firebase init
```

![Image](https://cdn-media-1.freecodecamp.org/images/l8Egdd07uOmSD9DABh0yGz2afrukibewdZWa)
_firebase init_

Appuyez sur Espace pour sélectionner l'option « Hosting », puis sur Entrée pour confirmer votre choix.

Maintenant, vous devez choisir le projet auquel vous souhaitez déployer le site.

![Image](https://cdn-media-1.freecodecamp.org/images/6J2TVueoEKaBSPIjJz6UvpZkLNNobMfBNmU9)

Choisissez « créer un nouveau projet ».

Maintenant, vous choisissez quel dossier contient la version statique de votre site. Par exemple, `public`.

On vous posera deux questions sur la configuration de l'application. Répondez « **Non** » aux deux :

* Configurer comme une application monopage (réécrire toutes les URL vers /index.html) ?
* Le fichier public/index.html existe déjà. Écraser ?

Cela empêchera Firebase d'ajouter son propre fichier index.html par défaut.

Maintenant, vous êtes prêt à partir :

![Image](https://cdn-media-1.freecodecamp.org/images/5NL3xuH0FsPqFq2whtP0QI6GL4tZIeyZLKa-)

### Configurer le site

L'application CLI de Firebase a créé le fichier `firebase.json` dans le dossier racine du site.

Dans cet article, je vais expliquer comment configurer une fonctionnalité simple dans Firebase Hosting, en ajoutant une petite partie de configuration dans le fichier `firebase.json`.

Je veux définir la directive d'en-tête Cache-Control sur tous les actifs du site - images, fichiers CSS et JS.

Un fichier `firebase.json` propre contient ce qui suit :

```
{   "hosting": {    "public": "public",     "ignore": [       "firebase.json", "**/.*",       "**/node_modules/**"     ]   } }
```

Il indique à Firebase où se trouve le contenu du site et quels fichiers il doit ignorer. N'hésitez pas à ajouter tous les dossiers que vous avez, sauf `public`.

Nous allons ajouter une nouvelle propriété, appelée `headers` :

```
{   "hosting": {     "public": "public",     "ignore": [       "firebase.json",      "**/.*",       "**/node_modules/**"    ],     "headers": [       {         "source" : "**/*.@(jpg|jpeg|gif|png|css|js)",         "headers" : [ {           "key" : "Cache-Control",           "value" : "max-age=1000000" //1 semaine+         } ]       }     ]   } }
```

Comme vous pouvez le voir, nous indiquons que pour tous les fichiers se terminant par `jpg|jpeg|gif|png|css|js`, Firebase doit appliquer la directive `Cache-Control:max-age=1000000`, ce qui signifie que tous les actifs sont mis en cache pendant plus d'une semaine.

### Publier le site

Lorsque vous êtes prêt à publier le site, vous exécutez simplement la commande suivante et Firebase s'occupera de tout.

```
firebase deploy
```

Vous pouvez maintenant ouvrir [https://votreprojet.firebaseapp.com](https://votreprojet.firebaseapp.com/) et vous devriez voir le site web en fonctionnement.

### Domaine personnalisé

L'étape logique suivante consiste à faire en sorte que votre site utilise un domaine personnalisé.

Allez sur [https://console.firebase.google.com/project/_/hosting/main](https://console.firebase.google.com/project/_/hosting/main) et cliquez sur le bouton « Connecter un domaine » :

![Image](https://cdn-media-1.freecodecamp.org/images/OktJ0asSC0uVphJs2HCoqYIrz3FvRD7yKKRA)

L'assistant vous demandera le nom de domaine, puis il vous fournira un enregistrement TXT que vous devez ajouter à votre panneau DNS d'hébergement pour vérifier le domaine.

Si le domaine est tout nouveau, cela peut prendre un certain temps avant de pouvoir passer cette étape.

Une fois cela fait, l'interface vous donnera deux **enregistrements A** à ajouter également à votre panneau DNS d'hébergement.

Si vous configurez `votredomaine.com`, n'oubliez pas de configurer également `www.votredomaine.com` en faisant une redirection.

![Image](https://cdn-media-1.freecodecamp.org/images/GCq9sjxSfJ1Jvw1JsZAVLjlF2EnJS213a4IH)

Maintenant, vous devez simplement attendre que votre hébergement mette à jour les enregistrements DNS et que les caches DNS se vident.

De plus, gardez à l'esprit que votre certificat SSL est automatiquement provisionné mais nécessite un peu de temps pour être valide.

> Intéressé par l'apprentissage de JavaScript ? Obtenez mon ebook sur [jshandbook.com](https://jshandbook.com/)