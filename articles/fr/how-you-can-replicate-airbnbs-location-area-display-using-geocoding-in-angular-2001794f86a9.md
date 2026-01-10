---
title: Comment reproduire l'affichage de la zone de localisation d'Airbnb en utilisant
  le géocodage dans Angular
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-22T18:28:35.000Z'
originalURL: https://freecodecamp.org/news/how-you-can-replicate-airbnbs-location-area-display-using-geocoding-in-angular-2001794f86a9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*kowBDo9y5hXO73JQUBu6AQ.png
tags:
- name: Angular
  slug: angular
- name: Google
  slug: google
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Comment reproduire l'affichage de la zone de localisation d'Airbnb en utilisant
  le géocodage dans Angular
seo_desc: 'By Filip Jerga

  Have you thought about integrating Google Maps into your project? Do you know how
  to geocode a location? It’s not that hard. All it takes is 20 minutes, several lines
  of code, and basic programming knowledge. So let’s see how it’s done...'
---

Par Filip Jerga

Avez-vous pensé à intégrer Google Maps dans votre projet ? Savez-vous comment géocoder un lieu ? Ce n'est pas si difficile. Il suffit de 20 minutes, de quelques lignes de code et de connaissances de base en programmation. Alors voyons comment cela se fait.

### Commençons par les dépendances et la clé API

Tout ce dont nous avons besoin est d'installer [Angular Google Maps (AGM)](https://angular-maps.com/). Il existe de nombreux packages sur Internet qui vous fournissent des composants Google Maps "prêts à l'emploi". C'est à vous de choisir celui que vous préférez. **J'ai choisi AGM en raison de son API bien documentée et de sa large gamme de composants.**

Il est maintenant temps de configurer notre clé API. **Pas de clé API, pas de plaisir avec une carte !** Google a récemment eu une idée intéressante. Vous devez fournir vos détails de facturation afin de configurer votre projet et d'obtenir votre clé API. Pas de soucis ! Vous devez atteindre un certain nombre de requêtes pour être facturé pour le service.

**Nous devons activer l'API Maps JavaScript (25 000 requêtes gratuites par jour) et l'API Geocoding (2 500 requêtes gratuites par jour).** Vous avez également la possibilité de définir votre limite quotidienne afin de ne pas la dépasser.

**Pour obtenir votre clé API, suivez ces étapes :**

1. Allez dans la [console des développeurs Google](https://console.developers.google.com/projectselector/apis/dashboard).
2. Créez un nouveau projet
3. Allez dans la section bibliothèque et activez **Maps JavaScript API** et **Geocoding API**
4. Obtenez vos identifiants (clé API). Et puis célébrez :)

![Image](https://cdn-media-1.freecodecamp.org/images/1*gGuj7I_E5hXqt42Bi1sdYA.png)
_Gardons cela ouvert pour un petit moment. Nous avons besoin de notre clé API dans Angular._

### Commençons à coder !

Réchauffez vos machines et ouvrez vos projets dans les éditeurs de code de votre choix, car les choses vont devenir sérieuses maintenant.

Créons un module de carte pour avoir tout ensemble. Nous avons besoin d'un service pour gérer toute la logique et des composants pour afficher une carte. Très facile — tapez simplement dans le terminal : **ng g component map.** Vous pouvez également consulter ma structure de dossiers et mon composant de carte dans mon [projet GitHub](https://github.com/Jerga99/bwm-ng).

Dans le même dossier que votre dossier de composant de carte, créez **map.module.ts**. Nous devons importer **AgmCoreModule** et lui donner la clé API que nous avons obtenue de Google. **N'oubliez pas de référencer votre MapModule dans le module principal AppModule (ou tout autre module où vous souhaitez afficher une carte) !**

Le module AGM nous fournira tous les composants et directives nécessaires pour afficher une carte Google. Il gérera le chargement de l'API Google Maps, donc nous devons nous concentrer uniquement sur le géocodage d'un lieu.

### Nous avons besoin d'un service

Afin de ne pas polluer notre composant de carte avec la logique de géocodage, il est toujours bon de pratique d'utiliser un service. Créez le service de carte dans le même dossier que votre logique liée à la carte et implémentez la fonction suivante :

Décomposons cela :

1. Nous obtenons le géocodeur de l'objet window car je n'ai pas trouvé d'abstraction dans le package AGM. **Geocoder expose les fonctions nécessaires pour géocoder le lieu.**
2. Ensuite, nous retournerons un Observable car pourquoi pas ? **Le géocodage est asynchrone, et la meilleure façon de travailler avec du code asynchrone dans Angular est définitivement les observables.**
3. Appelez geocode avec un lieu. Après un certain temps, lorsque la fonction est résolue, notre fonction de rappel est appelée avec un résultat et un statut.
4. Vérifiez le statut, et s'il est **OK**, nous sommes prêts à partir. **Le géocodage a réussi et nous pouvons obtenir les coordonnées de notre lieu en appelant une fonction lat et lng sur l'objet geometry.**
5. Si le statut n'est pas OK, émettez simplement une erreur et versez une larme :(

Cela devrait suffire pour notre service. Ce n'était pas si difficile, n'est-ce pas ?

### Continuer avec le composant de carte de location

Revenons à notre composant de carte et remplissons le modèle avec une carte AGM.

Voici un peu de code tiré de la documentation officielle d'AGM. **Nous référençons le composant agm-map.** Cela affichera Google Maps sur la page, **mais n'oubliez pas de définir la hauteur de agm-map**, sinon il ne sera pas affiché ! Allez dans votre fichier SCSS ou CSS et écrivez : **agm-map {height: 400px}**.

Afin d'afficher un lieu sur la carte, **nous devons fournir les propriétés d'entrée de latitude et de longitude à agm-circle** (le composant qui affichera la zone circulaire du lieu sur la carte). La propriété zoom zoome simplement sur la carte, afin que le lieu soit plus visible. Vous pouvez voir que nous affichons le agm-circle uniquement lorsque nous avons une latitude et une longitude. D'autres propriétés à considérer sont le rayon du cercle, la couleur et l'opacité.

**Le plus important sur agm-map est l'eventEmitter mapReady.** Cette fonction émettra un événement lorsque l'API Google Maps sera chargée et qu'une carte sera prête à afficher un lieu. **C'est le meilleur moment pour nous d'appeler notre Map Service et de géocoder le lieu !** Alors ne perdons pas de temps — créons la fonction mapReadyHandler dans notre fichier map component.ts.

La voici. **MapReadyHandler appellera getGeoLocation, qui est responsable de l'appel de notre service avec la valeur du lieu.** Lorsque le lieu est géolocalisé et émis par le service, nous obtiendrons les coordonnées dans la fonction de rappel subscribe.

Nous avons presque terminé. **Maintenant, nous devons simplement définir une lat et une lng et appeler detectChanges pour nous assurer que notre carte sera mise à jour avec la zone affichée.**

### Dernière pièce du puzzle

Notre composant de carte est terminé. Maintenant, nous devons simplement l'afficher à l'écran. Vous pouvez choisir le composant parent de votre choix où vous souhaitez afficher votre carte. Dans mon cas, je voulais afficher la carte de mon lieu de location. Voir le code ci-dessous :

**Je référence mon composant de carte à l'intérieur de la page de détails de location** et je fournis la propriété d'entrée de lieu à l'intérieur. Par exemple, cela pourrait être : New York, Main Street. **Et voilà ! La carte avec le lieu est affichée lorsque nous naviguons vers la page de détails de la location.**

### Récapitulatif

Pour nous assurer que tout est clair maintenant, voyons cela dans une perspective plus large :

![Image](https://cdn-media-1.freecodecamp.org/images/1*nC3brY6LKHObyEzKsLFuyA.png)

J'espère que vous comprenez maintenant comment cela fonctionne ! Si vous avez des questions, n'hésitez pas à me contacter ou à laisser un commentaire.

Maintenant, vous savez comment intégrer Google Maps dans une application Angular. Il s'agit d'une version très simple. Si vous êtes intéressé par quelque chose de plus difficile, vous pouvez consulter [mon dépôt de projet GitHub](https://github.com/Jerga99/bwm-ng/tree/master/src/app/common/map).

Pour une vue d'ensemble du projet terminé, vous pouvez voir mon cours sur Udemy : [The Complete Angular, React & Node | Airbnb style application](http://bit.ly/2vs8jKM).

Bon codage !

Filip Jerga