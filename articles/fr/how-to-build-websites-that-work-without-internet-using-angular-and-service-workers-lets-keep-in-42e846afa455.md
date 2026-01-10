---
title: Comment créer des sites web qui fonctionnent sans internet en utilisant Angular
  et les service workers
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-03T16:21:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-websites-that-work-without-internet-using-angular-and-service-workers-lets-keep-in-42e846afa455
coverImage: https://cdn-media-1.freecodecamp.org/images/0*rJj-3GV2wU_Ky6gZ.png
tags:
- name: Angular
  slug: angular
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment créer des sites web qui fonctionnent sans internet en utilisant
  Angular et les service workers
seo_desc: 'By Tomiwa

  Introduction

  In this article, you will learn the theory of how service workers work. I provide
  a short tutorial to apply that theory to make a website that runs without the internet.
  Finally, I’ll discuss what this means for you and the fut...'
---

Par Tomiwa

### Introduction

Dans cet article, vous apprendrez la théorie du fonctionnement des service workers. Je fournis un court tutoriel pour appliquer cette théorie afin de créer un site web qui fonctionne sans internet. Enfin, je discuterai de ce que cela signifie pour vous et de l'avenir de l'internet.

Je m'enthousiasme lorsque je parle des service workers. Je vais faire un petit discours sur le problème que cela résout et pourquoi c'est génial. Ensuite, je plonge dans la théorie de leur fonctionnement et pourquoi c'est génial. Si vous voulez passer directement à la théorie ou au tutoriel, allez aux sections commençant par les titres **Théorie** et **Application** pour le code.

Cet article de blog est également disponible sous forme de :

* [Vidéo YouTube](http://bit.ly/pwa-tutorial-video)
* [Présentation](http://bit.ly/pwa-tutorial-slides)
* [Podcast](https://anchor.fm/tomiwa1a/episodes/How-to-Build-Websites-that-work-without-Internet-Using-Angular--Service-Workers-and-Firebase-e2ccp2)

### Table des matières

* Les sites web sont étranges
* Théorie : Comment fonctionnent les Service Workers
* Application : Tutoriel sur la création de sites web hors ligne
* Prérequis
* Installation du Service Worker
* Partie 1a : Construire le Service Worker
* Sortie du Service Worker
* Partie 1b : Tester le Service Worker (#2001441)
* Création d'un mini serveur
* Inspection des requêtes du serveur
* Où les fichiers sont-ils enregistrés ?
* Partie 2 : Sauvegarde des données externes (Partie 1 Git Tag : pwa-tutorial-0.1)
* Sauvegarde des appels d'API externes : #8593ada
* Partie 3 : Notifier les utilisateurs des nouvelles mises à jour (Partie 2 Git Tag : pwa-tutorial-0.2)
* Partie 4 : Déploiement (Partie 3 Git Tag : pwa-tutorial-0.3)
* Conclusion
* Qui a besoin d'applications mobiles
* L'avenir des sites web
* Lectures complémentaires

### Les sites web sont étranges

J'ai réalisé quelque chose récemment qui m'a fait comprendre à quel point les service workers peuvent être puissants. Lorsque j'ai internet, il semble qu'il y ait une infinité de choses qui rivalisent pour attirer mon attention.

Mais lorsque je suis dans un avion, par exemple, et qu'il n'y a pas de connexion internet, la compétition pour mon attention est beaucoup moins féroce. Les trois choses que je peux généralement faire sont de parcourir mes photos, regarder un film téléchargé ou lire un livre électronique.

Avec les service workers, si vous êtes en mesure de fournir une expérience web hors ligne à vos utilisateurs, vous pouvez attirer leur attention dans l'un de ces rares moments où la compétition pour celle-ci est la moins féroce.

Commençons par un simple diagramme. Que représentent les deux cercles dans ce diagramme de Venn ?

![Image](https://cdn-media-1.freecodecamp.org/images/0*E2A3mu1X9dugLi3F)

Je vais vous donner un indice. Amazon, Alibaba et Facebook sont parmi les plus grands sites web du monde, servant des millions d'utilisateurs chaque jour. Voici quelques statistiques pour vous donner une idée :

* Alibaba a réalisé [25 milliards de dollars](https://www.forbes.com/sites/helenwang/2017/11/12/alibabas-singles-day-by-the-numbers-a-record-25-billion-haul/#1a6df2421db1) de ventes en une journée (jour des célibataires)
* [40 %](https://www.skyhighnetworks.com/cloud-security-blog/microsoft-azure-closes-iaas-adoption-gap-with-amazon-aws/) des clients de cloud computing utilisent Amazon Web Services, y compris [Apple](https://techcrunch.com/2018/02/27/apple-now-relies-on-google-cloud-platform-and-amazon-s3-for-icloud-data/), Netflix et la CIA
* [2,2 milliards](https://www.statista.com/statistics/264810/number-of-monthly-active-facebook-users-worldwide/) de personnes utilisent Facebook chaque mois, 700 millions sur Instagram

Tout cela est bien et bon, mais il y a un petit problème. Sans Wi-Fi, leurs sites web entiers sont complètement inutilisables. Même si vous voulez simplement effectuer des tâches simples comme consulter les avis sur les produits pour des articles déjà dans votre panier, vous ne pouvez rien faire.

Comparez cela avec des sites comme [Google Drive](https://www.google.com/drive/) ou [Atila.ca](https://atila.ca/). [Atila.ca](http://atila.ca/) n'a pas un million d'utilisateurs, mais même lorsque vous n'avez pas de connexion internet, vous pouvez toujours utiliser le site. Google Drive est un autre site web qui fait cela bien. Vous pouvez en fait utiliser Google Drive même sans internet. Comme vous utiliseriez une application de bureau comme Microsoft Word. On apprend quelque chose de nouveau chaque jour, n'est-ce pas ?

![Image](https://cdn-media-1.freecodecamp.org/images/0*tcZGksocJwwGM4En)

Dans le passé, il semblait presque être une vérité que les sites web ne fonctionnaient pas sans internet. Une fois que vous réalisez le potentiel des service workers, vous changez complètement votre perspective sur la façon dont vous pensez aux sites web. Vous commencez à imaginer les améliorations significatives de l'expérience utilisateur que nous pouvons avoir sur nos sites préférés.

Imaginez que vous êtes dans le métro en train de vous rendre au travail sans internet. Vous n'avez même pas de service cellulaire. Mais vous pourriez toujours consulter les avis sur les produits des articles dans votre panier Amazon. Ou vous êtes dans un long vol en avion. Pendant que votre téléphone est en mode avion, vous pouvez lire les articles les plus populaires du New York Times. Ou vos articles préférés dans une liste que vous avez choisie de sauvegarder pour plus tard.

Vous pouvez voir que le potentiel est grand et il est facile de commencer à rêver. Revenons à la réalité et plongeons dans la théorie de la façon dont tout cela est possible.

### Théorie : Comment fonctionnent les Service Workers

Un service worker est un proxy ou un messager entre votre navigateur et internet. Lorsque votre application web demande des ressources (images, fichiers html, API json, etc.), le service worker les obtient pour vous sans avoir besoin de demander à internet. En termes littéraux, il s'agit d'un fichier JavaScript qui est expédié avec le reste de votre application. Ce fichier contient du code qui indique à votre application comment intercepter les requêtes réseau et les obtenir à partir du cache réseau.

Typiquement, lorsqu'un site web est chargé pour la première fois, le navigateur web effectue une série de requêtes vers le réseau pour les ressources dont votre site web a besoin pour fonctionner. Cela inclut généralement :

* les fichiers html pour l'affichage du contenu
* les fichiers CSS pour le style
* les fichiers Js pour la logique de l'application
* les images et autres ressources

Lorsque votre internet ne fonctionne pas, il n'y a aucun moyen pour le navigateur de contacter le réseau pour récupérer les fichiers nécessaires à l'affichage du site web. Il échoue donc et vous obtenez l'infâme "dinosaure sautant" sur Google Chrome.

Avec les service workers, la première fois que vous visitez un site, en plus de l'ensemble habituel de fichiers index.html, styles.css, main.js, etc. qui sont demandés, le navigateur demande également un fichier JavaScript de service worker à votre site web. Ce fichier est ensuite téléchargé et sauvegardé dans le cache de votre navigateur. Le fichier de service worker télécharge, versionne et met en cache tous les fichiers de votre application pour les servir plus tard.

![Image](https://cdn-media-1.freecodecamp.org/images/0*DWZmifjCFHNB6cyq)

Cela présente deux avantages très importants. Comme mentionné dans le titre, cela signifie que même lorsque votre connexion internet est interrompue, le site web fonctionnera toujours. Il n'a jamais besoin de demander quoi que ce soit à internet. Le service worker a tous les fichiers dont vous aurez besoin.

Inversement, cela signifie également que même si vous avez internet, l'application fonctionnera également plus rapidement. Lors des prochains chargements du site web, au lieu de faire un aller-retour complet vers le réseau pour obtenir les fichiers de l'application, il récupère simplement les fichiers du cache du navigateur et les sert à l'utilisateur.

### Application : Comment créer des sites web hors ligne

#### Prérequis

Avant de commencer, assurez-vous d'avoir installé les éléments suivants :

* [Node.js® et npm](https://nodejs.org/en/download/)
* Assurez-vous d'avoir node 8.X ou supérieur (node -v) et npm 5.x ou supérieur (npm -v)
* Installez globalement [Angular CLI](https://github.com/angular/angular-cli) :
* `npm install -g @angular/cli`
* Navigateur Google Chrome (optionnel, mais recommandé)
* Compte Google (optionnel, uniquement si vous souhaitez déployer sur Firebase)

#### Lancer le projet

* Allez sur [https://github.com/atilatech/atila-web-app](https://github.com/atilatech/atila-web-app)
* Clonez l'application web [demo.atila.ca](https://demo.atila.ca/) depuis Github : [atila-web-app](https://github.com/atilatech/atila-web-app)
* Consultez la branche pwa-tutorial : `git checkout pwa-tutorial`
* Consultez le commit de début du tutoriel : `git checkout pwa-tutorial-0.0`
* Installez les modules npm : `npm install`
* Lancez l'application ! : `ng serve -o`

Si vous obtenez une erreur `No NgModule`, allez dans n'importe quel fichier .ts et ajoutez un espace. C'est un bug vraiment étrange, mais vous pouvez lire ce [problème Github](https://github.com/angular/angular-cli/issues/9292#issuecomment-360178485) pour plus d'informations.

#### Installation du Service Worker

Pour installer le Service Worker et accéder aux différents objets Service Worker dans notre application, nous devons faire ce qui suit.

1. Installez le module @angular/serviceworker : npm install @angular/serviceworker
2. Cela installe un package npm qui inclut divers objets JavaScript de service worker que nous utiliserons dans les étapes suivantes
3. Dites à angular-cli de construire le projet avec le service worker : ng set apps.0.serviceWorker=true
4. Dites à angular CLI de produire automatiquement un fichier JavaScript qui contient le code pour le service worker lors de la construction du projet expliqué dans l'étape suivante.
5. Configurez votre service worker dans ngsw-config.json
6. Cela indique à votre service worker exactement quels fichiers il doit sauvegarder et comment il doit les sauvegarder
7. assetGroups : fichiers qui sont inclus dans le cadre de l'application
8. Lorsque l'application est mise à jour, ces ressources sont également mises à jour
9. dataGroups : ressources externes non versionnées avec l'application
10. Mode d'installation : Quelle stratégie de mise en cache utiliser lors de la première visualisation de ce fichier
11. Mode de mise à jour : Quelle stratégie de mise en cache utiliser lors de la mise à jour du fichier, après que nous l'ayons déjà installé
12. Stratégie de mise en cache
13. Prefetch : Sauvegardez ces fichiers avant même que nous les demandions
14. Lazy : Sauvegardez ces fichiers uniquement après qu'ils aient été demandés au moins une fois
15. Ajoutez un fichier manifest.json et référencez-le dans index.html

#### Configuration du Service Worker

![Image](https://cdn-media-1.freecodecamp.org/images/0*PZYiuo0W10jQvHmo)

* Cela indique à votre service worker exactement quels fichiers il doit sauvegarder et comment il doit les sauvegarder :
* assetGroups : fichiers inclus dans le cadre de l'application
* Lorsque l'application est mise à jour, ces ressources sont également mises à jour
* dataGroups : ressources externes non versionnées avec l'application
* Mode d'installation : Quelle stratégie de mise en cache utiliser lors de la première visualisation de ce fichier
* Mode de mise à jour : Quelle stratégie de mise en cache utiliser lors de la mise à jour du fichier, après que nous l'ayons déjà installé
* Stratégie de mise en cache
* Prefetch : Sauvegardez ces fichiers avant même que nous les demandions
* Lazy : Sauvegardez ces fichiers uniquement après qu'ils aient été demandés au moins une fois
* Vous pouvez consulter la [documentation officielle d'Angular sur la configuration du service worker](https://angular.io/guide/service-worker-config) pour plus de détails

#### Manifest.json

```
{"name": "Atila","short_name": "Atila","start_url": "index.html","display": "standalone","icons": [{"src": "assets/img/favicon-bg.png","sizes": "512x512","type": "image/png"}],"background_color": "#194f87","theme_color": "#194f87"}
```

C'est ce qui transforme votre application d'une application web en une application web progressive. Cela permet à votre application web d'être similaire à une application mobile native. Cela permet aux utilisateurs d'installer votre application sur leur écran d'accueil.

![Image](https://cdn-media-1.freecodecamp.org/images/0*P5myb3EsJHS_bugZ)

#### Enregistrer le Service Worker ([#d2b186f](https://github.com/atilatech/atila-web-app/commit/d2b186f1ecc3a0862fcb3bd863643f1d28eac970))

Maintenant, nous devons dire à notre application qu'un service worker existe. Nous enregistrons donc le module de service worker dans notre module d'application.

```
// src/app.module.ts
```

```
import {ServiceWorkerModule} from '@angular/service-worker';
```

```

```

```
Imports: [
```

```
,
```

```
ServiceWorkerModule.register('/ngsw-worker.js', {enabled: environment.production}),]
```

Ensuite, nous enregistrons le fichier de service worker si notre [navigateur prend en charge le service worker](https://jakearchibald.github.io/isserviceworkerready/) et que nous sommes en mode production.

```
// src/main.ts
```

```
if ('serviceWorker'  in  navigator  && environment.production) {
```

```
console.log("Service Worker in main.ts");
```

```
window.addEventListener('load', () =>; {
```

```
console.log("on page Load Service Worker in main.ts");
```

```
navigator.serviceWorker.register('/ngsw-worker.js', {
```

```
scope: '/',
```

```
})
```

```
.then(registration  =>; {
```

```
console.log("Service Worker registration completed main.ts", registration);
```

```
});
```

```
});
```

### Partie 1a : Construire le Service Worker

#### Sortie du Service Worker

Ensuite, nous allons construire le projet : `ng build --prod`

Examinons le dossier dist/ pour voir à quoi ressemble la construction d'une application avec un service worker.

![Image](https://cdn-media-1.freecodecamp.org/images/0*yK-cyZH5cBDp3spd)

#### Sortie du Service Worker : ngsw.json

Rappelons que dans l'étape précédente, nous avons créé un fichier appelé ngsw-config.json. Ce fichier spécifie les types de fichiers que nous voulions que notre service worker met en cache et comment nous voulions les mettre en cache. Lorsque le projet est construit, les règles dans le fichier ngsw-config.json sont développées pour inclure exactement les fichiers que nous allons mettre en cache. Le fichier ngsw.json inclut également une table de hachage pour indexer et récupérer les fichiers mis en cache. La table de hachage nous permet également de versionner nos fichiers. Nous pouvons suivre les versions de nos fichiers en cours d'exécution et si nous devons obtenir une nouvelle version.

![Image](https://cdn-media-1.freecodecamp.org/images/0*gtRBo57N9515LdBC)

![Image](https://cdn-media-1.freecodecamp.org/images/0*xrGnG1j9q-B1ONGy)

#### Sortie du Service Worker : ngsw-worker.js

Ce fichier est littéralement le service worker. Nous l'avons enregistré précédemment dans notre fichier main.ts. Il s'agit d'un fichier JavaScript simple. Il contient le code et la logique de la manière dont votre service worker s'enregistre et met en cache les données dans une base de données. Si vous êtes prêt pour un défi, essayez de parcourir le code et voyez si vous pouvez comprendre ce qui se passe.

![Image](https://cdn-media-1.freecodecamp.org/images/0*x_osOIZlwST--8Ui)

### Partie 1b : Tester le Service Worker ([#2001441](https://github.com/atilatech/atila-web-app/commit/2001441a948f8fc0768c43634020cd927763f812))

#### Création d'un mini serveur

* Les service workers sont utilisés dans un contexte hors ligne. Nous avons besoin d'un serveur qui peut simuler des environnements hors ligne
* Installez [npm http server](https://www.npmjs.com/package/http-server)
* `Npm install http-server@0.11.1 --save-dev`
* Construisez et exécutez le serveur :
* `ng build --prod` (optionnel)
* `http-server -p 8080 -c-1 dist`

#### Inspection des requêtes du serveur

* Visitez l'onglet Réseau de Chrome dans les outils de développement
* Faites cela avant d'aller sur localhost !
* Ouvrez un nouvel onglet
* Cliquez droit quelque part sur l'écran
* Inspecter > allez à l'onglet Réseau
* Ouvrez [http://localhost:8080/](http://localhost:8080/)

![Image](https://cdn-media-1.freecodecamp.org/images/0*Oy6aUcTa2mJF4Iil)

Notez qu'il n'y a pas de Wi-Fi en haut à droite. Vérifiez la console des outils de développement : Les ressources réseau externes échouent avec 504 mais nos fichiers réussissent (200).

#### Où les fichiers sont-ils enregistrés ?

Ouvrez l'onglet Application dans les outils de développement et vous verrez la section cache local. C'est la "base de données" où les service workers enregistrent vos fichiers. Il y a 2 tables. L'une contient les ressources réelles dont notre application a besoin. Une autre table de hachage avec des clés de hachage qui pointent vers chaque nom de fichier, comme nous l'avons vu dans notre fichier ngsw.json. C'est tout ! Vous avez maintenant une application web simple mais fonctionnelle hors ligne. Continuez à la partie 2 pour ajouter plus de fonctionnalités.

![Image](https://cdn-media-1.freecodecamp.org/images/0*OLvJkfQzjwyk5bef)

### Partie 2 : Sauvegarde des données externes (Partie 1 Git Tag : [pwa-tutorial-0.1](https://github.com/atilatech/atila-web-app/releases/tag/pwa-tutorial-0.1))

#### Pourquoi aucune de mes API ne fonctionne-t-elle ?

Lorsque vous essayez de naviguer en cliquant sur un lien, vous remarquerez une erreur de serveur. Votre service worker n'a pas ces API dans votre base de données, mais nous pouvons les ajouter. Quiz ! Si nous voulons dire à notre service worker de mettre en cache un nouveau type de fichier, où devons-nous mettre le code pour le faire :

1. Manifest.json
2. Ngsw-config.json
3. App.module.ts

![Image](https://cdn-media-1.freecodecamp.org/images/0*USs5NfuSBP-nCOjF)

Vous pouvez voir les requêtes réseau échouer dans l'onglet réseau de vos outils de développement.

#### Sauvegarde des appels d'API externes : Configuration ([Diff Github](https://github.com/atilatech/atila-web-app/commit/fe3f6aa30a01766d8d487711afd9aded4a0a3f13#diff-4553821adec55b6f464162aab4323c7a))

Maintenant, nous allons configurer notre ngsw-config.json pour mettre en cache les URL d'API externes également. Deux options de mise en cache :

1. Fraîcheur : Allez d'abord sur le réseau, si manquant, allez sur le
2. Performance : Allez d'abord sur le cache, puis allez sur le réseau

#### Sauvegarde des appels d'API externes : [#8593ada](https://github.com/atilatech/atila-web-app/commit/8f93ada504dd5b0dc210a64a73caee5ffd14927d)

Vous devrez peut-être utiliser une URL séparée qui permet à votre application d'y accéder via CORS. Nous utiliserons un service JSON spécial pour simuler ("mock") notre API de blog. Nous n'avons pas la permission d'utiliser l'API officielle d'Atila.

* Changez ScholarshipService.getPaginatedScholarships :
* Allez à `src/app/_service/scholarship.service.ts#L47`
* Changez : `this.http.post(${this.scholarshipsPreviewUrl}?page=${page}/, form_data)` en : this.http.get(`https://api.myjson.com/bins/dx1dc`)
* Changez BlogPostService.getBySlug :
* Allez à src/app/_service/blog-post.service.ts#L25
* Changez : this.http.get(`${this.blogUrl}blog/${username}/${slug}/`) en : this.http.get(`https://api.myjson.com/bins/v5ow0`)

### Partie 3 : Notifier les utilisateurs des nouvelles mises à jour (Partie 2 Git Tag : [pwa-tutorial-0.2](https://github.com/atilatech/atila-web-app/releases/tag/pwa-tutorial-0.2))

Lorsque qu'une nouvelle version est disponible sur le réseau, le service worker sert toujours l'ancienne version du cache pour gagner du temps.

* Ajoutez votre profil à la page de l'équipe : src/app/team/team.component.ts
* Ajoutez votre image et quelques informations dans le tableau des données de l'équipe
* Si vous reconstruisez le projet et redémarrez le serveur, vous remarquerez que votre profil n'apparaît pas encore.
* Nous pouvons ajouter un snackbar pour notifier l'utilisateur des nouvelles mises à jour
* npm install @angular/material@5.1.1 --save (vous avez peut-être déjà cela)
* Ensuite, nous créons swUpdate pour écouter les mises à jour du SW et mettre à jour si une nouvelle version est disponible. [Diff Github](https://github.com/atilatech/atila-web-app/commit/1c89769)

```
// src/app/app.component.ts    import {SwUpdate} from  "@angular/service-worker";...    Constructor (..., public swUpdate SWUpdate,)...ngOnInit() {
```

```
if (true) {
```

```
// vérifier le service worker pour voir si une nouvelle version de l'application est disponible
```

```
if (this.swUpdate.isEnabled) {
```

```
this.swUpdate.available.subscribe(() =>; {
```

```
const snackBarRef = this.snackBar.open('Nouvelle version disponible', 'Charger la nouvelle version');snackBarRef.onAction().subscribe(
```

```
() =>; {
```

```
location.reload();});			});		}	}}
```

Reconstruisez et réservez votre application

### Partie 4 : Déploiement (Partie 3 Git Tag : [pwa-tutorial-0.3](https://github.com/atilatech/atila-web-app/releases/tag/pwa-tutorial-0.3))

#### Déploiement sur Firebase Hosting

Pour voir l'effet du service worker, nous devons le déployer sur un vrai site web. J'aime Firebase Hosting. Vous pouvez transformer une application web de votre localhost en un site web en direct en moins de 5 minutes avec quelques étapes simples. Je fais cela depuis presque 2 ans maintenant et je suis toujours impressionné par la facilité du processus. Récemmment, j'ai également joué avec [l'hébergement de sites web statiques AWS S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html). C'est une autre bonne alternative que vous pouvez explorer :

#### Prérequis de déploiement :

1. [Créez un compte Google](https://accounts.google.com/SignUp?hl=en)
2. [Créez un compte Firebase](https://firebase.google.com/) et un projet Firebase
3. Installez les outils Firebase globalement : `npm install -g firebase-tools@4.2.0`
4. Connectez-vous à Firebase : `firebase login`
5. Initialisez le dépôt Firebase : `firebase init`
6. Choisissez les paramètres suivants :
7. Choisissez l'hébergement comme type de projet
8. Changez le dossier public en dist/
9. Configurez comme une application à page unique
10. Écraser idnex.html ? NON
11. Déployez ! `Firebase deploy`
12. Visitez l'URL dans la sortie de la ligne de commande pour voir votre application

C'est tout ! Félicitations, vous avez maintenant un site web qui peut fonctionner sans internet.

### Conclusion

#### Qui a besoin d'applications mobiles

J'ai [écrit](https://atila.ca/blog/tomiwa/why-we-chose-angular-over-react-and-django-over-ruby-on-rails-for-atila-the-essential-software-startup-techstack) [précédemment](https://atila.ca/blog/tomiwa/phlock-my-hardware-startup-that-disappeared) sur les raisons pour lesquelles je crois fermement que les startups et les entreprises devraient concevoir leurs produits technologiques comme des applications web progressives plutôt que comme des applications mobiles. Mes arguments principaux étant :

1. Devoir maintenir 2 bases de code séparées pour Android et IOS est une douleur : 2 ensembles d'utilisateurs, 2 ensembles de développeurs, 2 ensembles de problèmes. (Des choses comme [Flutter](https://flutter.io/) et [Ionic](https://ionicframework.com/) sont cool mais je ne crois pas qu'elles abordent le problème fondamental de 2 bases de code séparées.)
2. La plupart des gens n'utilisent que les mêmes 5 applications par jour, donc les convaincre de télécharger une autre application sera très difficile.
3. L'approbation et la distribution par les gardiens de l'App Store d'Apple et du Google Play Store ne sont pas amusantes.

Certains des arguments principaux contre les applications web incluent des choses comme :

1. Accessibilité hors ligne
2. Meilleure engagement des utilisateurs grâce aux notifications push
3. Accès aux fonctionnalités matérielles natives comme les caméras

Avec des fonctionnalités comme les service workers, je viens de montrer comment nous pouvons permettre aux sites web de fonctionner hors ligne. [Les applications web progressives permettent également les notifications push](https://developers.google.com/web/fundamentals/codelabs/push-notifications/).

Les fonctionnalités matérielles natives sont encore l'un des avantages que les applications mobiles ont, bien que cela [change](https://developers.google.com/web/fundamentals/media/capturing-images/). Sauf si c'est crucial pour votre application d'avoir ces fonctionnalités natives, j'encourage fortement les startups et les entreprises à envisager de faire de leur prochaine application une application web progressive.

Je pense que l'avenir de l'internet verra plus d'applications distribuées via les navigateurs et les URL que via les applications natives et les magasins d'applications. Dans un cas ironique de l'histoire qui se répète, c'est en fait un retour en arrière à l'avènement de l'internet dans les années 90 lorsque des entreprises comme Netscape et diverses startups "com" se portaient très bien en distribuant leur logiciel via le web.

#### L'avenir des sites web

Ne serait-ce pas génial si d'autres sites appliquaient cette même philosophie ? Imaginez que vous êtes comme moi et que vous avez une heure ou plus de trajet pour vous rendre au travail chaque jour. Oubliez le Wi-Fi, ils n'ont même pas de service cellulaire dans le métro.

Maintenant, supposons que je veux acheter des écouteurs Bluetooth et que je veux lire quelques avis Amazon avant de prendre ma décision. Ne serait-ce pas génial si je pouvais mettre en cache les détails des produits pour les articles dans mon panier et lire les avis en allant au travail ? Ensuite, au moment où j'arrive au travail, je peux simplement acheter l'article que je veux.

Ou imaginez que vous êtes dans l'avion pour un vol rapide de Toronto à Ottawa. Vous chargez le NY Times pour vous mettre à jour sur les nouvelles du matin, mais le site affiche le célèbre "dinosaure Google". Dans un monde idéal, le NY Times devrait mettre en cache les 5 articles les plus populaires. Cela permet aux utilisateurs de lire les articles et de laisser des commentaires hors ligne. Les commentaires peuvent être synchronisés lorsqu'ils se reconnectent à internet.

Google Docs fait cela le mieux. Google Docs est Microsoft Word, Powerpoint et Excel mais en mieux et construit pour Chrome. Vous n'avez pas besoin d'internet pour utiliser Microsoft Word. Parce que Google Docs fonctionne dans un navigateur web, vous devriez pouvoir utiliser Google Docs pour accéder et modifier vos éléments récents. Ce que Google Docs fait exactement bien.

Je me sens légèrement fier du fait que les grands sites web Amazon et NY Times ont besoin d'internet pour fonctionner. Je suis humble que le petit [Atila.ca](http://atila.ca/) fonctionne très bien avec et sans internet. ;) Lorsque l'internet est en panne, vous pouvez toujours voir les bourses d'études en vedette, les articles de blog et d'autres morceaux de contenu.

D'accord, ce sont surtout des #FirstWorldProblems. Mais une autre chose qui m'enthousiasme vraiment à propos de cette technologie, c'est la construction de l'internet pour les prochains milliards d'utilisateurs. Pour les personnes qui ont une connexion internet très lente ou inconsistante.

Par exemple, [HospitalRun](http://hospitalrun.io/) est une application hors ligne. Elle gère les hôpitaux dans le monde en développement. Ce sont des endroits où la connectivité intermittente est une réalité. Elle permet de transporter des dossiers dans des cliniques éloignées, où il peut n'y avoir aucun internet. Elle synchronise ensuite ces dossiers lorsqu'il y en a. (h/t [jonbellah.com](https://jonbellah.com/articles/offline-first/))

Chez Atila, l'un de nos projets est d'augmenter l'accès aux bourses d'études pour les étudiants des pays en développement. Il serait donc génial s'ils pouvaient lire des essais exemples et travailler sur leurs demandes de bourses d'études même s'ils vivaient dans des endroits avec une mauvaise connexion internet.

Je trouve personnellement l'idée des service workers et des applications web hors ligne très fascinante. Des technologies simples avec la capacité de changer fondamentalement les habitudes quotidiennes de milliards de personnes sont la raison pour laquelle j'ai choisi d'étudier le génie logiciel et pourquoi j'aime ce domaine. Je suis vraiment excité non seulement de voir comment l'avenir de l'internet se déroulera, mais aussi d'aider à construire l'avenir de l'internet et de la manière dont nous interagirons avec lui. L'avenir est déjà là, les gens. Merci d'avoir lu.

### Lectures complémentaires

* [Documentation officielle d'Angular sur les Service Workers](https://angular.io/guide/service-worker-intro)
* [Angular University : Angular Service Workers](https://blog.angular-university.io/angular-service-worker/)
* [Ajouter un Service Worker à une application Angular existante](https://medium.com/@cdeniz/transforming-an-existing-angular-application-into-a-progressive-web-app-d48869ba391f)
* [Angular Firebase — Déployer une application Angular sur Firebase](https://angularfirebase.com/lessons/deploying-an-angular-app-to-firebase/)