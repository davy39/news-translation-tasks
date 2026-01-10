---
title: Comment construire des applications React sur l'API REST de WordPress
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-03T07:47:43.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-react-apps-on-top-of-the-wordpress-rest-api-bcc632808025
coverImage: https://cdn-media-1.freecodecamp.org/images/1*10rDJAvtCHTZz-NdIMpGLQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
- name: WordPress
  slug: wordpress
seo_title: Comment construire des applications React sur l'API REST de WordPress
seo_desc: 'By Andrey Pokrovskiy

  UPDATE 06/16/2017:I updated the project to use ReactRouter 4 and Webpack 2. Some
  parts were refactored and simplified. Included links to the frontend React demo
  and Wordpress backend demo.

  WordPress is a powerful content manageme...'
---

Par Andrey Pokrovskiy

**MISE À JOUR 16/06/2017 :**  
**_J'ai mis à jour le projet pour utiliser ReactRouter 4 et Webpack 2. Certaines parties ont été refactorisées et simplifiées. J'ai inclus des liens vers la démonstration React frontend et la démonstration backend Wordpress._**

WordPress est un outil puissant de gestion de contenu. Mais lorsqu'il s'agit de développer sur celui-ci, cela peut être assez frustrant. Le mélange fou de HTML et de boucles PHP de WordPress peut souvent s'avérer peu intuitif à comprendre et difficile à maintenir.

Il y a cependant une lumière au bout du tunnel ! À partir de la version 4.7, WordPress est livré avec une API REST intégrée, et les plugins ne sont plus nécessaires. Cela facilite l'utilisation de WordPress strictement comme un stockage de données backend ou un CMS, tout en permettant une solution front end totalement personnalisée de votre choix.

Vous n'avez plus besoin d'avoir une installation locale de WordPress et de gérer la configuration des vhosts. Votre processus de développement local peut être limité à la construction du front end qui est connecté à une installation WordPress hébergée sur un serveur distant.

Dans cet article, je vais utiliser [ReactJS](https://facebook.github.io/react/) pour construire la partie front end de l'application, [React Router](https://github.com/ReactTraining/react-router) pour le routage, et [Webpack](https://webpack.js.org/) pour tout regrouper. Je vais également vous montrer comment intégrer Advanced Custom Fields, pour ceux d'entre nous qui en sont venus à dépendre comme outil pour créer une solution intuitive pour nos clients.

La stack ressemble à ceci :  
**- ReactJs**  
**- React Router v4**  
**- Alt (pour l'implémentation Flux)**  
**- Webpack v2**

**Dépôt GitHub** : [https://github.com/DreySkee/wp-api-react](https://github.com/DreySkee/wp-api-react)  
**URL de démonstration du frontend React** : [http://wp-api-react.surge.sh/](http://wp-api-react.surge.sh/)  
**URL de démonstration du backend Wordpress** : [http://andreypokrovskiy.com/projects/wp-api-react/wp-admin](http://andreypokrovskiy.com/projects/wp-api-react/wp-admin)  
**Utilisateur** : demo  
**Mot de passe** : wp-react-demo

### Installation du projet

Nommons le projet « wp-api-react ». Pour suivre, la première chose à faire est d'inclure ceci dans votre package.json et d'exécuter `npm install` :

Installez également webpack et webpack-dev-server globalement si vous ne l'avez pas déjà fait :

`npm i webpack webpack-dev-server -g`

Maintenant, dans le dossier du projet, créez `wepack.dev.js` pour la configuration de développement et `webpack.production.js` avec la configuration pour construire le projet pour la production.

Collez ceci dans `webpack.dev.config.js` :

Et ceci dans `webpack.production.config.js` :

Créez un dossier « src » à la racine du projet et créez `index.html` à l'intérieur. Le fichier `index.html` inclura ce morceau de code :

Ajoutons maintenant quelques dossiers supplémentaires au projet. À l'intérieur du dossier « src », créez un dossier « scripts » et à l'intérieur de « scripts », créez « components », « flux » et un fichier `index.js`. Cette structure aidera à garder les fichiers organisés.

À ce stade, la structure des dossiers devrait ressembler à ceci :

**wp-api-react/**  
 — **node_modules/**  
 — **src/**  
 — — **scripts/**  
 — — — **components/**   
 — — — **flux/**  
 — — — **index.js**  
 — — **index.html**  
 — **package.json**  
 — **webpack.config.js**

`index.js` est le point d'entrée pour Webpack et il contiendra toutes les routes du projet. Incluons React, React Router et la structure de routage de base dans le fichier :

`index.js` fait référence au composant Home dans les imports. Nous devons le créer dans le dossier « components ». `Home.js` sera le composant de modèle pour la page d'accueil. Incluez ceci dans le fichier :

Si vous exécutez `npm start` dans le terminal à l'intérieur du dossier du projet et ouvrez [http://localhost:8080/](http://localhost:8080/) dans le navigateur, vous devriez voir un message « Hello world ! ». Si vous commencez à modifier des fichiers, Webpack rechargera à chaud la page pour vous.

### Flux avec Alt

Il est maintenant temps d'implémenter [flux](https://facebook.github.io/flux/) en utilisant [Alt](http://alt.js.org/guide/). Vous devrez créer trois nouveaux dossiers à l'intérieur du dossier « flux » : « alt », « stores » et « actions » :

**wp-api/**  
 — **node_modules/**  
 — **src/**  
 — — **scripts/**  
 — — — **flux/**  
 — — — — **alt/**  
 — — — — **actions/**  
 — — — — **stores/**  
 — — — **components/**  
 — — — — **Home.js**  
 — — — **index.js**  
 — — **index.html**  
 — **package.json**  
 — **webpack.config.js**

Créez `Alt.js` à l'intérieur du dossier « alt » et collez ceci dans le fichier :

Tout ce que fait ce fichier, c'est exporter l'instance Alt que nous utiliserons dans les stores et les actions.

Créez `DataActions.js` dans le dossier « actions ». Ce fichier contiendra toute la logique pour obtenir les données des endpoints de l'API REST de WordPress. Pour communiquer avec l'API, nous utiliserons [axios](https://github.com/mzabriskie/axios). Incluez ceci dans `DataActions.js` :

N'oubliez pas de remplacer l'URL d'exemple de l'installation WordPress par la vôtre.

Créez `DataStore.js` dans le dossier « stores ». Ce fichier écoutera la méthode `getSuccess()` de DataActions.js qui retourne les données de l'API WordPress. Il stockera et manipulera ensuite les données. Collez ceci dans `DataStore.js` :

Pour obtenir les données de l'API WordPress et les rendre disponibles pour l'application, vous devez inclure `DataActions.js` dans `index.js` et envelopper la fonction de rendu dans `DataActions.getPages()`. La réponse retournée sera utilisée plus tard pour créer dynamiquement des routes :

Maintenant, chaque fois que l'application est initiée, `DataActions.getPages()` appelle l'endpoint de l'API WordPress et stocke les données retournées dans `DataStore.js`.

Pour y accéder, il suffit d'inclure `DataStore.js` dans n'importe quel composant et d'appeler la méthode appropriée. Par exemple, obtenons toutes les données à l'intérieur du fichier `Home.js` et `console.log` :

Après que Webpack ait actualisé la page, vous devriez voir l'objet de données retourné dans la console :

```
Object {pages: Array[1], posts: Array[1]}
```

### Routes dynamiques

Pour l'instant, il n'y a pas de routes définies dans l'application autre que la route d'index. Si vous avez quelques pages créées dans le backend WordPress, il y a des chances que vous souhaitiez qu'elles soient disponibles pour le front end. Pour ajouter dynamiquement des routes à React Router, nous devons ajouter une autre méthode dans `index.js`, appelons-la `buildRoutes()` :

Incluez `{this.buildRoutes(response)}` à l'intérieur de React Router juste après `<Route path="" component={ Home } exact` />. La méthode parcourt simplement toutes les pages retournées par l'API WordPress et retourne de nouvelles routes. Remarquez comment pour chaque route, elle ajoute le composant « Home ». Cela signifie que le composant « Home » sera utilisé pour chaque route.

Supposons que dans WordPress vous avez une page avec un slug « about ». Si vous allez à la route de cette page « /about », elle se chargera mais vous verrez toujours le même message « Hello World ». Dans le cas où vous n'avez besoin que d'un seul modèle pour chaque page, vous pouvez le laisser tel quel et obtenir les données spécifiques à la page en appelant `DataStore.getPageBySlug(slug)` et en fournissant le slug de la page actuelle.

Dans la plupart des cas, cependant, vous auriez besoin d'avoir plusieurs modèles pour différentes pages.

### Modèles de pages

Afin d'utiliser des modèles de pages, nous devons laisser React savoir quel modèle utiliser avec une page donnée. Nous pouvons utiliser le slug de la page qui est retourné par l'API pour mapper les modèles à différentes routes.

Supposons que nous avons deux pages avec les slugs « home » et « about ». Nous devons créer un objet qui mappe les slugs de pages aux chemins des composants React. Nommons l'objet templates et incluons-le dans `index.js` :

Nous avons également apporté des mises à jour à la méthode `buildRoutes()` pour nécessiter le bon composant. N'oubliez pas de créer le composant `About.js` pour mapper le slug « about ».

Pour obtenir des données spécifiques à une page, tout ce que vous avez à faire est d'appeler la méthode `DataStore.getPageBySlug(slug)` et de fournir le slug de la page actuelle :

```
render() {    let page = DataStore.getPageBySlug('about');
```

```
return (        <div>            <h1>{page.title.rendered}</h1>        </div>    );}
```

### Navigation dynamique

Maintenant, nous allons ajouter une navigation globale qui reflétera tous les liens des pages du backend WordPress. Tout d'abord, créez un composant `Header.js` dans le dossier « components » :

Nous obtenons toutes les pages de WordPress en utilisant `DataStore.getAllPages()`, puis nous les trions par « menu_order » avec lodash et nous les parcourons pour générer les `<Link` /> de React Router. Notez que la route de la page d'accueil est exclue du tableau allPages et incluse comme un lien séparé.

Incluez le composant `Header.js` dans `index.js` et vous verrez la navigation dynamique incluse sur chaque page :

### Advanced Custom Fields

La plupart des développeurs WordPress sont familiers avec le plugin [Advanced Custom Fields](https://www.advancedcustomfields.com/). Il rend le CMS WordPress entièrement personnalisable et convivial. Heureusement, il est très facile d'accéder aux données ACF en utilisant l'API WordPress.

Pour obtenir les données ACF des endpoints de l'API, nous devons installer un autre plugin appelé [ACF to REST API](https://wordpress.org/plugins/acf-to-rest-api/). Cela inclura une propriété acf dans l'objet retourné par l'API WordPress. Vous pouvez accéder aux champs acf comme suit :

```
render() {    let page = DataStore.getPageBySlug('about');    let acf = page.acf; // Données Advanced Custom Fields
```

```
return (        <div>            <h1>{acf.yourCustomFieldName}</h1>        </div>    );}
```

### Prochaines étapes

Très bien, nous avons couvert le cas d'utilisation le plus courant pour exploiter l'administration CMS de WordPress, ainsi qu'un front-end React.

Les prochaines étapes pourraient consister à ajouter du style au projet en Less ou Sass. Ou peut-être étendre le fichier `DataAction.js` en ajoutant des appels d'endpoints API supplémentaires pour récupérer plus de données comme les commentaires, les catégories et les taxonomies.

Je vous recommande fortement de consulter le [manuel officiel de l'API REST de WordPress](https://developer.wordpress.org/rest-api/), où la fonctionnalité de l'API est bien documentée. Vous y trouverez des informations sur CRUD, la pagination, l'authentification, les requêtes, la création d'endpoints personnalisés, et plus encore. Ces ressources vous aideront à étendre ce que nous avons construit ici.

_par **Andrey Pokrovskiy** — Développeur Senior chez [Gigareef](http://gigareef.com/)_

_Si vous êtes arrivé jusqu'ici, vous pourriez être le genre de développeur qui serait un excellent candidat chez Gigareef. Nous recherchons actuellement des développeurs talentueux pour travailler sur des projets impliquant ReactJS/MEAN Stack/Handlebars/Node._

_Envoyez un email à [jobs@gigareef.com](mailto:jobs@gigareef.com) et parlez-nous un peu de vous._

[_Gigareef_](http://gigareef.com)_, où la technologie s'épanouit_