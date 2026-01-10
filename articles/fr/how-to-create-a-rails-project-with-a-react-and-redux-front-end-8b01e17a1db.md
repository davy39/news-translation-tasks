---
title: Comment créer un projet Rails avec un front-end React et Redux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-15T16:42:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-rails-project-with-a-react-and-redux-front-end-8b01e17a1db
coverImage: https://cdn-media-1.freecodecamp.org/images/1*EtGyA7lw9v-oJqZjJs2AZQ.png
tags:
- name: JavaScript
  slug: javascript
- name: Rails
  slug: rails
- name: React
  slug: react
- name: Redux
  slug: redux
- name: TypeScript
  slug: typescript
seo_title: Comment créer un projet Rails avec un front-end React et Redux
seo_desc: 'By Mark Hopson

  A complete guide to setting up a single-page Javascript App with React and Redux
  inside a Rails project.


  Update (Mar 17, 2019): Added Typescript to the last step of this project.

  This tutorial will show you how to create a single-page...'
---

Par Mark Hopson

#### Un guide complet pour configurer une application JavaScript monopage avec React et Redux à l'intérieur d'un projet Rails.

![Image](https://cdn-media-1.freecodecamp.org/images/1DRlu00V4rUeQFcC64Muori13cH2tdM94tEw)

_Mise à jour (17 mars 2019) : Ajout de [Typescript](https://github.com/Microsoft/TypeScript) à la dernière étape de ce projet._

Ce tutoriel vous montrera comment créer une [application monopage](https://www.bloomreach.com/en/blog/2018/07/what-is-a-single-page-application.html) avec React (et [Redux](https://redux.js.org/) et [Semantic UI](https://react.semantic-ui.com/)) à l'intérieur d'un projet Rails.

Ce tutoriel inclura également :

* [Redux](https://redux.js.org/)
* [React Router](https://github.com/ReactTraining/react-router)
* [Reselect](https://github.com/reduxjs/reselect)
* [Redux Thunk](https://github.com/reduxjs/redux-thunk)
* [Semantic UI](https://react.semantic-ui.com/)

_Note de côté #1. J'ai vu ce [guide merveilleux](https://medium.freecodecamp.org/how-to-make-create-react-app-work-with-a-node-backend-api-7c5c48acb1b0) récemment et il m'a inspiré pour en écrire un pour Rails._

_Note de côté #2. Voici le [tutoriel terminé](https://github.com/markhopson/rails-react-tutorial). L'[historique des commits](https://github.com/markhopson/rails-react-tutorial/commits/master) correspond (en quelque sorte) avec les étapes de ce guide._

### Aperçu

Pour vous donner une idée de ce que nous allons construire et de comment les choses vont fonctionner, voyez les 2 diagrammes ci-dessous.

#### Diagramme 1 : Gestion de la première requête HTTP (c'est-à-dire les requêtes du navigateur à notre application Rails)

Le diagramme ci-dessous illustre votre application React à l'intérieur de votre projet Rails, et le chemin (ligne noire solide) que la première requête prend pour retourner l'**application React** au client (navigateur).

![Image](https://cdn-media-1.freecodecamp.org/images/OxcrUVaQKCApwVhTqP2MpevTsr9O6uBVBK6u)
_Diagramme 1 : Comment notre projet gère la première requête du client (c'est-à-dire le navigateur)_

#### Diagramme 2 : Gestion des requêtes HTTP suivantes (c'est-à-dire les requêtes de notre application React à notre application Rails)

Après que l'application React soit chargée dans le navigateur de l'utilisateur, l'application React sera responsable de l'envoi des requêtes à votre application Rails (ligne noire solide). En d'autres termes, une fois React chargé, les requêtes à Rails proviendront du code JavaScript, et non du navigateur.

![Image](https://cdn-media-1.freecodecamp.org/images/PEaEcl3jJ6J0QUzGCQREKB9ovNgWn1kAUuNB)
_Diagramme 2 : Comment React interagit avec Rails (les requêtes HTTP proviendront de l'application React et non du navigateur lui-même)_

#### Autres notes importantes avant de commencer à coder

* Considérez votre application React comme étant séparée de votre application Rails. L'application React est strictement pour le front-end et s'exécute dans le navigateur de l'utilisateur. La partie Rails est strictement pour le back-end et s'exécute sur le serveur. L'application Rails ne sait rien de l'application React sauf quand retourner ses actifs statiques (HTML, JS et CSS compilés par Webpack).
* Une fois votre application React chargée par votre navigateur, toute la logique pour faire des requêtes HTTP (récupérer des données et transformer ces données en une vue) est faite dans le front-end (c'est-à-dire le navigateur).
* Votre application Rails ne sert effectivement aucune vue sauf celle qui sert votre application React. Dans ce tutoriel, la seule vue Rails est `/app/views/static/index.html.erb`.
* Tous les chemins `/api/*` sont gérés par l'application Rails, tandis que tous les autres chemins sont gérés par React à l'intérieur du navigateur (après que votre navigateur a chargé la première requête). Par exemple, `[http://votre-app.com/quelquechose](http://votre-app.com/quelquechose)` sera envoyé à l'application Rails, puis retourné à votre application React (le HTML/JS/CSS qui a déjà été chargé dans le navigateur), qui décidera quoi afficher à l'écran.
* [Considérations pour construire une application monopage](https://medium.freecodecamp.org/why-i-hate-your-single-page-app-f08bb4ff9134). Non nécessaire pour ce tutoriel mais utile.
* [Modèles de conception de composants React](https://medium.com/teamsubchannel/react-component-patterns-e7fb75be7bb0). Encore une fois, non nécessaire mais utile.

### Configuration système

Pour information, voici ma configuration système. Je ne dis pas que vous en avez besoin, mais quelque chose de similaire rendra cette expérience de tutoriel plus fluide.

* macOS 10.13.6 (High Sierra)
* Ruby 2.5.1
* Rails 5.2.1 (et Bundler 1.16.6)
* - gem install bundler -v 1.16.6
* Node 9.8.0

Enfin, passons au code !

### Étape 1 : Créer un nouveau projet Rails avec Webpack et React

Créez une nouvelle application Rails. J'ai nommé la mienne `rails-react-tutorial`.

```
rails new rails-react-tutorial --webpack=react
```

Voir [ici](https://guides.rubyonrails.org/5_1_release_notes.html#optional-webpack-support) pour plus d'informations sur le drapeau `--webpack=react` introduit dans Rails 5.1.

### Étape 2 : Assurez-vous que les gems Webpacker et React-Rails sont installés

Vérifiez si les gems [**Webpacker**](https://github.com/rails/webpacker) et [**React-Rails**](https://github.com/reactjs/react-rails) sont dans votre `Gemfile`. Si les gems ne sont pas là, ajoutez-les :

![Image](https://cdn-media-1.freecodecamp.org/images/dJaidHtjRCjdyj6rbyLpzO614UFTN2H8RJ1J)
_Parfois seul Webpacker est ajouté, et non React-Rails ; je ne sais pas pourquoi…_

Maintenant, exécutez ces commandes pour installer tout.

```
bundle install
```

```
# Cette commande peut ne pas être nécessaire.# Si déjà installé, elle vous demandera# de remplacer certains fichiers.rails webpacker:install
```

```
rails webpacker:install:react  rails generate react:installyarn install                   
```

Maintenant, exécutez `rails server -p 3000` et visitez `[http://localhost:3000](http://localhost:3000)` pour vous assurer que notre projet fonctionne.

**Astuce Pro #1** : exécutez `./bin/webpack-dev-server` dans une fenêtre séparée pendant le codage pour que les changements soient automatiquement compilés et rechargés dans le navigateur.

**Astuce Pro #2** : Si vous obtenez cette erreur `can’t activate sqlite3 (~> 1.3.6), already activated sqlite3–1.4.0` alors ajoutez `gem 'sqlite3', '~> 1.3.6'` au Gemfile. Voir [ce](https://stackoverflow.com/a/54529016/1176788) lien pour plus d'informations.

### Étape 3 : Ajouter une classe de contrôleur et une route à notre application Rails

Ajoutez une nouvelle route à notre application Rails. Pour cet exemple, nous ajouterons le point de terminaison `GET /v1/things` à `config/routes.rb`.

![Image](https://cdn-media-1.freecodecamp.org/images/m5F9mTi3f5w0PYylit7AGcwehshPSZDPcM9L)
_Notre fichier `config/routes.rb`_

Cette nouvelle route nécessitera un ThingsController. Créez un nouveau fichier `app/controllers/v1/things_controller.rb`. N'oubliez pas, il doit être dans le dossier `v1` car il appartient à notre API Rails.

![Image](https://cdn-media-1.freecodecamp.org/images/9PLtIbLYPQ1KNyl8nVQqVenLl-ZixF5pGwJa)
_Notre fichier /app/controllers/v1/things_controller.rb_

Notre contrôleur Things retournera une réponse codée en dur pour `GET /v1/things`.

À ce stade, vous devriez pouvoir relancer `rails server -p 3000` et visiter `[http://localhost:3000/v1/things](http://localhost:3000/v1/things)`.

![Image](https://cdn-media-1.freecodecamp.org/images/dW22FrdU6la7-AbXdjnFSzcsHwoDnt2ULL5B)
_Succès !_

Ensuite, nous créerons un nouveau composant React.

### Étape 4 : Générer un nouveau composant React

Créez un composant React HelloWorld qui accepte un paramètre de chaîne nommé `greeting` en exécutant la commande suivante :

```
rails generate react:component HelloWorld greeting:string
```

Un fichier doit être créé : `app/javascript/components/HelloWorld.js`.

![Image](https://cdn-media-1.freecodecamp.org/images/zFqPQS1aINW85gTBqLfG01mTiEAflXq798ih)
_Notre fichier `app/javascript/components/HelloWorld.js`_

### Étape 5 : Utiliser notre composant HelloWorld

Pour utiliser et voir notre nouveau composant HelloWorld, nous devons faire 2 choses : créer une vue qui intègre ce composant et ajouter une route pour pointer vers cette vue.

Pour créer une vue, créez le fichier `app/views/static/index.html.erb` et ajoutez ce qui suit :

![Image](https://cdn-media-1.freecodecamp.org/images/BFbI3X9mTUdmccYrrl3jqvbJOw8PNmmxSIag)
_"Hello" est passé en tant que paramètre "greeting" pour HelloWorld_

Pour notre nouvelle route, ajoutez la ligne suivante à notre fichier `routes.rb`, et un StaticController vide pour la supporter.

![Image](https://cdn-media-1.freecodecamp.org/images/KqdYPbAdYPyXpQRjF0ELU17XwZiY7dCaMuP1)
_Ajout d'une route pour servir notre nouvelle vue qui contient le composant HelloWorld_

Ajoutez ceci à `app/controllers/static_controller.rb` :

![Image](https://cdn-media-1.freecodecamp.org/images/NABHDjdE4RwGEibcfxXFR10IpTbqlqEs9Sr4)
_Un contrôleur vide_

Vous devriez maintenant pouvoir relancer `rails server -p 3000` et visiter `[http://localhost:3000/](http://localhost:3000/v1/things)` pour voir votre nouveau composant React (n'oubliez pas d'exécuter `./bin/webpack-dev-server` dans une fenêtre séparée pour que les changements JavaScript soient automatiquement compilés par webpack).

![Image](https://cdn-media-1.freecodecamp.org/images/LJbFwbm0ntl7zQzL937w4CgsrcjencsnMAYm)
_Succès ! Notre premier composant rendu._

Maintenant que nous avons un composant React qui s'affiche dans notre vue, développons notre application pour supporter plusieurs vues avec `react-router`.

### Étape 6 : Ajouter React-Router

Tout d'abord, exécutez cette commande pour ajouter `react-router-dom`, qui inclut et exporte tout `react-router` et quelques composants d'aide supplémentaires pour la navigation web. Plus d'informations [ici](https://github.com/ReactTraining/react-router/issues/4648).

```
npm install --save react-router-domyarn install
```

Cette commande devrait ajouter la ligne suivante à votre fichier `package.json`. Notez que 4.2.2 a été utilisé ici, mais votre version pourrait être différente.

![Image](https://cdn-media-1.freecodecamp.org/images/WJnBf1C9vRH45WCQ9Hce8Eu9UdXxwNUjNYC4)

Maintenant, utilisons React Router pour créer des routes pour notre front-end React.

### Étape 6 : Utiliser React-Router

`[react-router](https://github.com/ReactTraining/react-router)` nous permet de gérer toutes nos routes UI strictement avec JavaScript. Cela signifie que nous aurons besoin d'un seul composant "App" qui encapsule toute notre application. "App" utilisera également React-Router pour présenter le bon composant "Page" pour l'URL demandée.

Pour commencer, exécutez cette commande pour ajouter un composant App qui représentera toute notre application front-end.

```
rails generate react:component App
```

Ensuite, ouvrez le fichier du nouveau composant React créé, `app/javascript/components/App.js`, et ajoutez ce qui suit…

![Image](https://cdn-media-1.freecodecamp.org/images/6K0h9rD17Rj7vsY8K8JlUMoW57aKRohhYZvx)
_Notre application React avec 2 routes_

Maintenant, changez `index.html.erb` pour pointer vers notre nouveau composant App.

![Image](https://cdn-media-1.freecodecamp.org/images/uzdNclc4C2wOXwQjUrN-3BjdUgiXgtsYuNI3)
_Le composant App encapsulera tout notre front-end._

Enfin, modifiez votre `routes.rb` pour que Rails envoie toutes les requêtes qui ne sont pas pour l'API à notre composant App (via `StaticController#index`).

![Image](https://cdn-media-1.freecodecamp.org/images/5VVRBI2cAQA8IRGGyesRBsbI2N3tr3TUQ8gy)
_Nos routes.rb redirigent maintenant toutes les requêtes non-API et non-Ajax vers notre application React_

Nous pouvons maintenant exécuter `rails server -p 3000` et visiter `[http://localhost/](http://localhost/)` et `[http://localhost/](http://localhost/)hello` pour voir React-Router fonctionner (n'oubliez pas que `./bin/webpack-dev-server` permet le webpacking automatique).

Ensuite, nous devrons installer quelques dépendances supplémentaires avant de pouvoir connecter notre front-end React à notre API Rails.

### Étape 7 : Ajout de Redux, Sagas, Babel Polyfill et Axios

Maintenant, ajoutons les bibliothèques JavaScript suivantes pour notre front-end.

* [Redux](https://redux.js.org/) pour gérer l'état global de notre application.
* Babel-Polyfill pour activer les fonctionnalités JavaScript avancées qui pourraient ne pas être disponibles sur les anciens navigateurs web.
* [Reselect](https://github.com/reduxjs/reselect) et [React-Redux](https://github.com/reduxjs/react-redux) pour faciliter le travail avec Redux.

Pour installer tout, exécutez ce qui suit :

```
npm install --save redux babel-polyfill reselect react-reduxyarn install
```

Maintenant, nous allons utiliser ces outils pour configurer un magasin d'état Redux, puis ajouter quelques Actions et Réducteurs pour l'utiliser.

### Étape 8 : Configurer le magasin d'état Redux

Dans cette étape, nous allons configurer le magasin d'état Redux pour notre application avec le modèle suivant (nous ajouterons et supprimerons des "choses" dans les prochaines étapes).

```
{  "things": [    {      "name": "...",      "guid": "..."    }  ]}
```

Tout d'abord, créez un fichier `configureStore.js`. Cela initialisera notre magasin Redux.

![Image](https://cdn-media-1.freecodecamp.org/images/ZFFfX1kN-fXNEcHoy2utcuIwXWyVjVHOjP49)
_Code pour initialiser notre état Redux, et notre premier Réducteur !_

Maintenant, importez et utilisez `configureStore()` dans le composant App pour créer un état Redux et le connecter à notre App.

![Image](https://cdn-media-1.freecodecamp.org/images/JJlz1mKfcn0xk-tvyBX6ROtdd20jJWNHg3Y9)
_Initialisation de l'état Redux pour notre App_

Maintenant, vous avez Redux installé dans votre application ! Ensuite, nous créerons une Action et un Réducteur, et commencerons à écrire et lire depuis notre état Redux.

### Étape 9 : Ajouter une Action et un Réducteur

Maintenant que l'application a un état Redux, nous ajouterons un `<bouton>` à HelloWorld qui envoie une Action (que nous définirons ici) qui sera reçue par `rootReducer()`.

Tout d'abord, ajoutez la définition de l'Action `getThings()` et importez `createStructuredSelector()` et `connect()` dans le composant HelloWorld. Cela mappe des parties de l'état Redux, et des Actions (c'est-à-dire l'envoi de `getThings()`), aux props de HelloWorld.

Ensuite, ajoutez un `<bouton>` à HelloWorld qui envoie une Action `getThings()` (de ./actions/index.js) à chaque clic.

![Image](https://cdn-media-1.freecodecamp.org/images/OC1z0BMnwot2dpGpdw8nLeE7KV299yL8FuAD)
_Composant HelloWorld avec du nouveau code d'aide Redux_

Après avoir tout ajouté à HelloWorld, allez à `[http://localhost:3000/hello](http://localhost:3000/hello)`, ouvrez la console et cliquez sur le bouton "getThings" pour voir votre Action et les fonctions du Réducteur être appelées.

![Image](https://cdn-media-1.freecodecamp.org/images/JBA5AG2Mn7v0I3feseWjvqiuNveoOMndQhxk)
_Regardez la sortie console.log() pour voir notre Action être envoyée_

Maintenant que vous pouvez envoyer une Action qui peut être reçue par un Réducteur, faisons en sorte que le Réducteur modifie l'état Redux.

### Étape 10 : Faire en sorte que HelloWorld lise l'état React et affiche les "choses"

Insérez une liste `<ul>` dans HelloWorld et remplissez-la avec des "choses" de votre état Redux.

![Image](https://cdn-media-1.freecodecamp.org/images/U3gFj45R0kzszZFr316Bw70OfkjKtelrBGpB)
_HelloWorld avec <ul> qui lit les "choses" de notre état Redux_

Pour tester si cela fonctionne réellement, nous pouvons initialiser avec quelques données "choses". Une fois cela fait, nous pouvons actualiser la page et les voir dans notre liste.

![Image](https://cdn-media-1.freecodecamp.org/images/LpMQNM4kxe10tI8otmMB2qvj6YmoRjYiLdFf)
_Initialiser notre état Redux avec quelques "choses" pour voir si le front-end <ul> les lit correctement_

Maintenant que nous avons une Action et un Réducteur simples qui fonctionnent, nous allons étendre cela pour que l'Action interroge notre API Rails et que le Réducteur définisse le contenu des "choses" avec la réponse de l'API.

### Étape 11 : Installer Redux-Thunk

Nous aurons besoin de [Redux-Thunk](https://github.com/reduxjs/redux-thunk) pour permettre les flux de travail asynchrones (comme une requête HTTP) d'envoyer des Actions.

Installez `redux-thunk` en exécutant cette commande :

```
npm install --save redux-thunkyarn install
```

Maintenant, utilisons Thunk dans notre Action !

### Étape 12 : Utiliser redux-thunk et fetch() pour interroger l'API et définir l'état React avec les résultats

Tout d'abord, importons `redux-thunk` dans `configureStore.js` et installons-le dans notre magasin Redux pour que notre application puisse gérer les Actions "Thunk".

![Image](https://cdn-media-1.freecodecamp.org/images/iT1D-L38aPRqNJ2QsSDHancSC127DJhDXP0J)
_Nous devons installer Redux Thunk en tant que middleware Redux dans notre application._

Maintenant, testons que tout fonctionne en démarrant l'application et en chargeant une page.

Ensuite, modifions l'Action `getThings()` pour qu'elle retourne une fonction qui effectue ce qui suit (au lieu de retourner l'objet Action) :

1. Envoyer l'objet Action original
2. Faire un appel à notre API Rails.
3. Envoyer une nouvelle Action `getThingsSuccess(json)` lorsque l'appel réussit.

Pour cette étape, nous devrons également ajouter l'Action `getThingsSuccess(json)`.

![Image](https://cdn-media-1.freecodecamp.org/images/3AwByGTFi23tAaCgqnWW3QwRgYIqphlUY7-v)
_Notre nouvelle fonction d'Action getThings() qui fait bien plus que retourner un simple objet — grâce à Redux Thunk !_

Bien sûr, cela ne fait rien à l'état Redux puisque notre Réducteur ne fait aucun changement. Pour corriger cela, modifiez le Réducteur pour qu'il gère l'Action `GET_THINGS_SUCCESS` et retourne le nouvel état (avec la réponse de l'API Rails).

![Image](https://cdn-media-1.freecodecamp.org/images/-UxcmjkYR2YlPIweMTsxfdwVAaUyU69crZ-Y)
_Faisons en sorte que notre Réducteur modifie l'état Redux lorsque GET_THINGS_SUCCESS est envoyé_

Maintenant, si vous démarrez votre application, naviguez vers `localhost:3000/hello` et cliquez sur le bouton, votre liste devrait changer !

![Image](https://cdn-media-1.freecodecamp.org/images/NZxGKdIcW1rM6E5pJzenNmAjHCPBVsWNPwah)

Vous y êtes. Une API Rails connectée à une application React+Redux.

### (Bonus) Étape 13 : Installation des outils de développement Redux

Peut-être que j'aurais dû placer cette étape plus tôt, mais [Redux Dev Tools](https://github.com/zalmoxisus/redux-devtools-extension) est essentiel pour déboguer les Actions que votre application envoie, et comment ces Actions modifient votre état.

Voici comment l'installer. Tout d'abord, installez l'extension appropriée pour votre navigateur ([Chrome](https://chrome.google.com/webstore/detail/redux-devtools/lmhkpmbekcpmknklioeibfkpmmfibljd), Firefox).

Ensuite, exécutez ce qui suit pour installer la bibliothèque.

```
npm install --save-dev redux-devtools-extensionyarn install
```

Maintenant, utilisez-le pour initialiser votre magasin d'état Redux.

![Image](https://cdn-media-1.freecodecamp.org/images/zTmpSPNOpouTQyaatbSIHPrzZ8R8CLpv9hQQ)
_Installez Redux Dev Tools dans votre application. Vous devrez faire des modifications supplémentaires pour désactiver cela en mode production._

Après tout cela, vous devriez pouvoir voir un nouvel onglet, Redux, dans vos outils de développement Chrome (ou Firefox), qui vous permet de voir quelles Actions ont été envoyées, et comment chacune a modifié l'état de l'application. L'onglet React vous montrera également tous vos composants et leurs props et états.

![Image](https://cdn-media-1.freecodecamp.org/images/n15RQgRcGRJEITAOoot0g6kzYbkSjcpqDhgG)
_Le débogage des composants React et de l'état/des Actions Redux devient 100x plus facile avec cela_

Bon débogage !

### (Bonus) Étape 14 : Semantic UI

Semantic est une excellente bibliothèque pour les composants UI qui rend vraiment facile la création de sites web au look agréable rapidement.

Pour installer cette bibliothèque, exécutez ce qui suit.

```
npm install --save semantic-ui-css semantic-ui-reactyarn install
```

Ajoutez ceci à `app/javascript/packs/application.js` :

```
import 'semantic-ui-css/semantic.min.css';
```

Et ajoutez ceci à `app/views/static/index.html.erb` :

```
<%= stylesheet_pack_tag "application", :media => 'all' %>
```

![Image](https://cdn-media-1.freecodecamp.org/images/Fpgw4oXiZW8Y6p9AvBh1LnOnsZRZhijF6FsB)

![Image](https://cdn-media-1.freecodecamp.org/images/R8-0PWhJrXjIjXXeCUoiIVfFYTck1REyHrtB)
_Une belle UI rendue facile !_

### (Bonus) Étape 15 : Utiliser une structure de répertoire raisonnable

Cette étape est totalement optionnelle, et elle n'a rien à voir avec la fonction de l'application. Juste mon opinion sur la façon dont vous devriez organiser vos fichiers.

Comme vous pouvez probablement le deviner, entasser vos Actions dans le même fichier que vos composants, et avoir un seul réducteur pour toute votre application, ne s'adapte pas très bien lorsque votre application grandit. Voici ma structure de fichiers suggérée :

```
app|-- javascript   |-- actions      |-- index.js      |-- things.js   |-- components   |-- packs   |-- reducers      |-- index.js      |-- things.js
```

### (Bonus — Mise à jour du 17 mars 2019) Étape 16 : Installer Typescript !

[Typescript](https://github.com/Microsoft/TypeScript) est comme JavaScript mais avec des types ! Il est décrit comme un "[superset syntaxique strict de JavaScript](https://en.wikipedia.org/wiki/TypeScript)", ce qui signifie que JavaScript est considéré comme du Typescript valide, et les "fonctionnalités de type" sont toutes optionnelles.

À mon avis, Typescript est fantastique pour les grands projets JavaScript, comme un grand front-end React. Ci-dessous se trouvent les instructions sur la façon de l'installer, et une petite démonstration de celui-ci dans notre projet.

Tout d'abord, exécutez les commandes suivantes (prises du [README de Webpacker](https://github.com/rails/webpacker/blob/master/docs/typescript.md)) :

```
bundle exec rails webpacker:install:typescriptyarn add @types/react @types/react-dom
```

Maintenant, pour le voir en action, renommons `app/javascript/reducers/things.js` en `things.tsx` et ajoutons les lignes suivantes en haut du fichier :

![Image](https://cdn-media-1.freecodecamp.org/images/avtizC4rc2F9o8vKRFOITsBU42p9clMyAuaC)
_Ajoutons une interface pour dire à Typescript ce que "Thing" devrait être_

Après avoir ajouté `interface Thing`, utilisons-la en faisant en sorte que `const initialState` utilise ce type (vu dans la capture d'écran ci-dessus), et spécifions que `thingsReducer` retourne un tableau de type `Thing` (également vu dans la capture d'écran).

Tout devrait encore fonctionner, mais pour voir Typescript en action, ajoutons un cas `default` à `thingsReducer` et ajoutons `return 1`. Puisque `1` n'est pas un type `Thing`, nous verrons la sortie de `./bin/webpack-dev-server` échouer avec ce qui suit :

![Image](https://cdn-media-1.freecodecamp.org/images/AZ8YigkTdjeGHWLoG62dLsJ7Ksst3jqlEj43)
_Le type Thing est appliqué dans notre code_

Et c'est tout ! Vous pouvez maintenant ajouter des fichiers Typescript `.tsx` à votre projet et commencer à utiliser des types avec votre projet.

[Voici un excellent aperçu de Typescript et pourquoi vous devriez l'utiliser](https://stackoverflow.com/a/35048303/1176788).

### La Fin

Vous l'avez fait ! Vous avez créé une application Rails qui utilise React et Redux. C'est à peu près tout pour le tutoriel. J'espère que vous vous êtes amusé et que vous avez appris quelque chose en cours de route.

Si vous construisez quelque chose avec React et Rails, n'hésitez pas à le partager dans les commentaires ci-dessous — ainsi que toute question ou commentaire que vous pourriez avoir pour moi.

Merci d'avoir lu !