---
title: Comment construire le projet d'application de vote freeCodeCamp — un tutoriel
  approfondi
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-25T15:21:48.000Z'
originalURL: https://freecodecamp.org/news/building-the-free-codecamp-voting-app-1a6fdce1f4a8
coverImage: https://cdn-media-1.freecodecamp.org/images/0*4X_YWp8mLlizkbZm.
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: React
  slug: react
- name: Redux
  slug: redux
- name: Web Development
  slug: web-development
seo_title: Comment construire le projet d'application de vote freeCodeCamp — un tutoriel
  approfondi
seo_desc: 'By Daniel Deutsch

  The voting app challenge on freeCodeCamp was the first freeCodeCamp project in the
  curriculum that struck me as really hard. I just couldn’t do it as easily as all
  the other challenges. So much knowledge in of so many concepts is ne...'
---

Par Daniel Deutsch

Le défi de l'application de vote sur freeCodeCamp était le premier projet freeCodeCamp dans le programme qui m'a semblé vraiment difficile. Je ne pouvais pas le faire aussi facilement que tous les autres défis. Tant de connaissances dans tant de concepts sont nécessaires pour le construire.

Je n'ai pas trouvé de tutoriels ou d'exemples qui décomposaient ce défi avec des outils à jour. J'ai donc décidé de documenter mon processus de construction.

Dans ce tutoriel, nous utiliserons :

* MongoDB
* Express
* React + Redux
* Node.js

aussi connu sous le nom de "MERN-Stack".

![Image](https://cdn-media-1.freecodecamp.org/images/6u6xAACbPcP1Ixt3k0znDLK7sFDakueWsGAn)
_Fonctionnalité de l'application_

> « Je ne crains pas l'homme qui a pratiqué 10 000 coups une fois, mais je crains l'homme qui a pratiqué un coup 10 000 fois. »

> — Bruce Lee

### De quoi parle cet article

Je vais décrire le processus de construction de l'application de vote pour le [défi freeCodeCamp](https://www.freecodecamp.com/challenges/build-a-voting-app).

Ce n'est pas un exemple optimisé pour construire l'application. Je suis ouvert à tout type de feedback. Je suis encore un débutant et j'ai aussi laissé certaines choses ouvertes.

Ce n'est pas conçu comme un tutoriel ! C'est simplement une documentation que j'ai écrite pendant la construction de l'application.

### Structure

Je vais diviser cet article en sections de back-end, front-end, visualisation des données et le processus de déploiement. Le projet sera disponible en tant que code source ouvert sur GitHub. C'est là que vous pouvez suivre les commits et le résultat final.

### Environnement de développement

* [JavaScript](https://www.javascript.com/) simple
* [Node.js](https://nodejs.org/en/)
* [Express](https://expressjs.com/) (Framework JS)
* [MongoDB](https://mlab.com/) (Base de données)
* [Yarn](https://yarnpkg.com/en/) (gestion des packages)
* [Visual Studio](https://code.visualstudio.com/) Code comme éditeur
* [Postman](https://www.getpostman.com/) (test des APIs)
* [Robomongo / Robo 3T](https://robomongo.org/) (travailler plus rapidement avec MongoDB)

### Packages / Fonctionnalités / Dépendances

#### Général

* ([ES 6](http://es6-features.org/) (spécification du langage de script JS))
* [eslint](https://www.npmjs.com/package/eslint) avec l'extension Airbnb (pour écrire du code de meilleure qualité)
* [nodemon](https://github.com/remy/nodemon) (redémarrage du serveur lorsque des changements se produisent)
* [Babel](https://babeljs.io/) (compilateur javascript)
* [Webpack](https://webpack.github.io/) (module bundler/builder)
* [dotenv](https://www.npmjs.com/package/dotenv) (pour configurer les variables d'environnement)
* [shortid](https://github.com/dylang/shortid) (générateur d'ID aléatoires)

### Back-end

* [Node.js](https://nodejs.org/) (environnement d'exécution JS pour le côté serveur)
* [MongoDB](https://www.mongodb.com/what-is-mongodb) (base de données basée sur des documents)
* [connect-mongo](https://github.com/jdesboeufs/connect-mongo) (pour stocker les sessions dans MongoDB)
* [body-parser](https://github.com/expressjs/body-parser) (pour analyser les requêtes entrantes)
* [express](http://expressjs.com/de/) (pour faire fonctionner l'application)
* [mongoose](http://mongoosejs.com/docs/) (modélisation des données objet pour simplifier les interactions avec MongoDB)
* [morgan](https://www.npmjs.com/package/morgan) (middleware de journalisation des requêtes HTTP)
* [passport](http://passportjs.org/) (middleware d'authentification pour Node.js)

### Front-end

* [React](https://facebook.github.io/react/) (Framework JS)
* [Redux](http://redux.js.org/docs/introduction/) (gestion d'état pour React)
* [Redux Thunk](http://redux.js.org/docs/introduction/) (Redux asynchrone)
* [Materialize CSS](http://materializecss.com/) (framework pour le design matériel)
* [React Router](https://github.com/ReactTraining/react-router) (routage dans le frontend)

### Visualisation

* [React Google Charts](https://www.npmjs.com/package/react-google-charts) (React wrapper pour Google Charts)
* [Google Charts](https://developers.google.com/chart/) (pour visualiser les données)

### Déploiement / DevOps

* [Heroku](https://www.heroku.com/) (PaaS pour exécuter des applications dans le cloud)
* (Unit)Testing : Non implémenté dans cette application (mais normalement, il devrait l'être)

### D'abord les premières choses

Tout d'abord, je vais configurer mon environnement :

* ajouter [Git](https://git-scm.com/) pour le contrôle de version
* créer votre gestion de packages avec [yarn init](https://yarnpkg.com/lang/en/docs/cli/init/)
* ajouter [express](http://expressjs.com/en/starter/installing.html) pour un développement web rapide
* ajouter le package [nodemon](https://nodemon.io/) pour redémarrer votre serveur lors des changements
* ajouter eslint.rc pour votre configuration [eslint](https://eslint.org/)
* ajouter [babel](https://babeljs.io/) et les plugins correspondants pour compiler JS

En tant qu'intégration supplémentaire, j'utiliserai :

* [Travis CI](https://travis-ci.org/) (pour l'intégration continue)
* [Code Climate](https://github.com/codeclimate/codeclimate) (pour la qualité du code)
* [Assertible](https://assertible.com/) (Surveillance des services Web, en particulier la vérification du déploiement — Assurance Qualité)

Voici mon commit sur [GitHub](https://github.com/DDCreationStudios/votingApp/tree/23a05a550f6e2e34cb182d3a271a4c44028d07f9) après la configuration.

### Back-end

Pour moi, le back-end est le plus difficile. C'est donc par là que je vais commencer.

#### Configurer les packages, le middleware et Mongoose

Je vais utiliser :

* [body-parser](https://github.com/expressjs/body-parser) pour analyser les corps de requête
* [morgan](https://www.npmjs.com/package/morgan) pour journaliser les requêtes HTTP
* [compression](https://www.npmjs.com/package/compression) pour compresser les corps de réponse
* [helmet](https://www.npmjs.com/package/helmet) pour définir la sécurité de base avec les en-têtes HTTP
* [mongoose](https://www.npmjs.com/package/mongoose) outil de modélisation d'objets pour la connexion asynchrone à la base de données

#### Prochaines étapes :

* créer un fichier **constants** pour définir vos différentes variables d'environnement et les paramètres correspondants
* créer un fichier **middleware** pour passer le middleware à votre application et différencier les environnements. Utilisez les packages **bodyparser** et **morgan** ici.
* créer un fichier **database** pour configurer la connexion mongoDB
* modularisez votre code et externalisez vos constantes, middleware et connexion à la base de données. Cela permet de garder des fichiers plus petits.
* importer tout dans votre fichier **app.js**, passer la fonction `middleware` et tester votre configuration avec une simple requête `http`

Voici mon commit sur [GitHub](https://github.com/DDCreationStudios/votingApp/tree/88a2436697be4147302ce2dbcd3104ed564c86fe) après cette configuration.

#### Configurer vos routes

Revoir les histoires d'utilisateurs et définir vos routes en conséquence.

Suivant l'approche [CRUD](https://fr.wikipedia.org/wiki/Create,_read,_update_and_delete) :

En tant qu'utilisateur non authentifié, je veux :

* voir tous les sondages (R)
* voir les sondages individuels (R)
* voter sur les sondages disponibles (C)

En tant qu'utilisateur authentifié, je veux :

* voir et lire tous les sondages (R)
* voir les sondages individuels (R)
* voter sur les sondages disponibles (C)
* créer de nouveaux sondages (C)
* créer de nouvelles options et votes (C)
* supprimer les sondages (D)

Par conséquent :

* configurer [la gestion des erreurs en tant que middleware](http://expressjs.com/en/guide/error-handling.html)
* configurer votre [objet routeur](http://expressjs.com/en/4x/api.html#router)
* créer vos routes GET, POST, DELETE et répondre avec des objets JSON
* tester les routes configurées avec [postman](https://www.getpostman.com/docs/postman/sending_api_requests/requests) (toutes doivent avoir un code de statut 200)
* [connecter vos routes](http://expressjs.com/en/guide/using-middleware.html) à votre middleware et app.js

#### Configurer Mongoose et vos schémas et connecter tout à vos routes

Lors de la configuration des schémas, réfléchissez à la manière dont vous souhaitez structurer les documents que vous allez stocker dans la base de données. Dans cet exemple, nous devons stocker l'utilisateur pour le processus d'authentification et les sondages avec des réponses.

Pour les sondages, nous avons besoin :

1. de la question
2. des réponses et des votes

* créer vos schémas et modèles [mongoose](http://mongoosejs.com/docs/guide.html)
* connecter à [mlab](https://mlab.com/) pour mieux surveiller vos actions de base de données

Soyez conscient que MLab crée des "Collections Système". Elles génèrent une erreur "duplicate key error index dup key: { : null }" dans postman, lors de la création de nouveaux sondages. Jusqu'à présent, je n'ai pas trouvé de solution, mais la suppression de toutes les collections nous permet de recommencer.

* utiliser le package [dotenv](https://www.npmjs.com/package/dotenv) pour stocker vos identifiants dans l'environnement et ajouter le fichier .env à .gitignore (si vous rendez votre projet open source)
* connecter vos routes avec votre modèle mongoose pour gérer les documents dans MongoDB

**Assurez-vous de lire la [Documentation](http://mongoosejs.com/docs/models.html)** si vous êtes bloqué. Cette partie est assez difficile si vous n'avez pas fait beaucoup de choses avec mongoose et MongoDB !

[Voici à quoi ressemblaient mes commits sur Github après ces étapes](https://github.com/DDCreationStudios/votingApp/tree/5dcd7359d2cb1b31e28a08869461b927094550c0).

#### Établir l'authentification et l'autorisation avec Twitter

Je veux utiliser la connexion Twitter comme fournisseur [OAuth](https://oauth.net/) pour l'authentification. Cela offre une meilleure expérience utilisateur et j'ai également pu explorer OAuth.

OAuth est un protocole standard qui permet aux utilisateurs d'autoriser l'accès à l'API pour les applications web et de bureau ou mobiles. Une fois l'accès accordé, l'application autorisée peut utiliser l'API au nom de l'utilisateur.

Bien sûr, j'ai trouvé [le excellent article](https://scotch.io/tutorials/easy-node-authentication-twitter) sur la manière de configurer le processus d'authentification dans Nodejs. Après avoir échoué à l'implémenter correctement dans mon application et avoir passé une journée entière, j'ai décidé de plonger directement dans la [documentation de passport](http://passportjs.org/docs) !

J'adore la citation qu'ils ont mise là :

« Malgré les complexités impliquées dans l'authentification, le code n'a pas à être compliqué. »

**✨ Encore une fois, pour rappel : Lisez la Documentation !**

* enregistrez votre application sur [twitter apps](https://apps.twitter.com/) et obtenez les bons paramètres. Déterminez le Niveau d'Accès et l'URL de Rappel
* ajoutez les packages [passport](http://passportjs.org/), [passport-twitter](https://www.npmjs.com/package/passport-twitter) et [express-session](https://www.npmjs.com/package/express-session) à votre application
* créez un fichier définissant une stratégie passport pour Twitter
* pour supporter la session de connexion, passport doit sérialiser et désérialiser l'utilisateur
* passez passport à votre configuration passport et connectez passport.initialize et passport.session à votre application en tant que middleware. Utilisez express-session avant cela !
* configurez les routes pour l'authentification et le rappel

Consultez mon commit sur [Github](https://github.com/DDCreationStudios/votingApp/tree/d398cce56b1df2d042c07d2849223e88a5a2ed7f) après ces étapes.

Après cela, connectez le processus d'authentification à votre base de données

✨ Conseil : Utilisez pour votre rappel et vos tests toujours `http://127.0.0.1:3000/` au lieu de `http://localhost:3000/`, car cela résout beaucoup de problèmes qui pourraient survenir avec passport-twitter. ?

* créez un schéma Mongoose pour vos utilisateurs afin de les suivre dans votre base de données
* remplissez la fonction de rappel de votre fichier passport.js lors de la mise en œuvre de la stratégie Twitter. Filtrez votre base de données pour l'utilisateur et créez-en un nouveau si un utilisateur n'existe pas
* utilisez le package [connect-mongo](https://www.npmjs.com/package/connect-mongo) pour créer un mongoStore et stocker vos sessions dans MongoDB
* créez une fonction pour tester si un utilisateur est authentifié. Implémentez-la dans vos routes souhaitées lors de la fourniture d'une autorisation suffisante

L'implémentation peut ressembler à ceci :

```
passport.use(		new Strategy(constants.TWITTER_STRATEGY, (req, token, tokenSecret, profile, cb) => {  process.nextTick(() => {    if (!req.user) {      User.findOne({ 'twitter.id': profile.id }, (err, user) => {        if (err) return cb(err);        if (user) {          if (!user.twitter.token) {            user.twitter.token = token;            user.twitter.username = profile.username;            user.twitter.displayName = profile.displayName;            user.save(() => {              if (err) return cb(err);              return cb(null, user);            });          }          return cb(null, user);        }
```

```
						// si aucun utilisateur n'est trouvé, en créer un        const newUser = new User();
```

```
        newUser.twitter.id = profile.id;        newUser.twitter.token = token;        newUser.twitter.username = profile.username;        newUser.twitter.displayName = profile.displayName;
```

```
        newUser.save(() => {          if (err) return cb(err);          return cb(null, newUser);        });      });    } else {					// lorsque l'utilisateur existe déjà et est connecté      const user = req.user;
```

```
      user.twitter.id = profile.id;      user.twitter.token = token;      user.twitter.username = profile.username;      user.twitter.displayName = profile.displayName;
```

```
      user.save((err) => {        if (err) return cb(err);        return cb(null, user);      });    }  });}),	);
```

Après cela, votre authentification et autorisation avec Twitter est terminée.

[Voici à quoi ressemblaient mes commits sur Github après ces étapes](https://github.com/DDCreationStudios/votingApp/tree/cb96c8b2062f5c634efcba2b258e3ad054799c48).

#### Établir l'authentification et l'autorisation locales

L'étape suivante est de s'authentifier localement. Il n'y a en fait pas grand-chose à faire, puisque nous avons déjà configuré l'environnement.

* mettez à jour votre schéma utilisateur pour le local en définissant l'email et le mot de passe
* ajoutez le package [bcrypt-nodejs](https://www.npmjs.com/package/bcrypt-nodejs) pour sécuriser les mots de passe
* ajoutez des méthodes de hachage et de validation de mot de passe à votre schéma
* définissez les routes. Ce processus clarifie toujours ce que je veux vraiment implémenter

J'ai eu un problème principal que je n'ai pu résoudre qu'après de nombreuses heures de recherche. Voici l'exemple de la [documentation](http://passportjs.org/docs/configure) :

```
app.get('/login', function(req, res, next) {  passport.authenticate('local', function(err, user, info) {    if (err) { return next(err); }    if (!user) { return res.redirect('/login'); }    req.logIn(user, function(err) {      if (err) { return next(err); }      return res.redirect('/users/' + user.username);    });  })(req, res, next);});
```

Passer l'authentification dans la fonction de rappel a fourni suffisamment de flexibilité pour afficher les erreurs. Mais il est très important de créer la session explicitement avec `logIn()` !

* assurez-vous de différencier dans les routes entre l'inscription et la connexion !
* J'ai installé EJS comme moteur de vue pour pouvoir tester mon inscription et ma connexion correctement et efficacement
* créez une route de déconnexion, qui détruit votre session

J'ai passé tant d'heures sur une erreur que je veux l'afficher ici : MongooseError: Cast to ObjectId failed for value "favicon.ico" at path "_id"

Je l'ai résolue en vérifiant tout le middleware qui avait une erreur majeure, et les routes. Il s'est avéré que définir une route sur ('/:pID') n'est pas bon lorsque l'on travaille en développement.

Consultez mon commit sur [GitHub](https://github.com/DDCreationStudios/votingApp/tree/30e9627ba3ac2c6b45c64bf2bad4df5726e15a67) après la configuration du back-end.

Bien sûr, à ce stade, le back-end n'est pas parfait. Mais il est suffisamment stable pour passer à l'étape suivante, le front-end.

Choses à faire :

* utiliser la validation avec [joi](https://www.npmjs.com/package/joi)
* écrire des tests unitaires

### Frontend

#### Réfléchissez avant d'agir !

Tout d'abord, réfléchissez à ce que vous voulez créer. Dessinez quelques croquis pour visualiser ce que vous voulez construire.

Ensuite, envisagez des frameworks appropriés. Je vais choisir [React.js](https://facebook.github.io/react/tutorial/tutorial.html) et la bibliothèque de gestion d'état [Redux](http://redux.js.org/). La taille de cette application ne nécessite **pas** nécessairement l'utilisation de Redux.

Je veux le construire comme une expérience de page unique. Je veux avoir de la scalabilité et j'aime pratiquer l'utilisation de Redux. Donc, c'est un bon choix.

Commencez à planifier tout cela en [pensant en React](https://facebook.github.io/react/docs/thinking-in-react.html).

#### Configuration nécessaire avec Babel et Webpack

Il est important de réaliser que [Babel](https://babeljs.io/) et [Webpack](https://webpack.github.io/) ne sont pas trop compliqués à configurer soi-même. Il existe tant de tutoriels pour les deux que vous pouvez le faire facilement vous-même.

* ajoutez Babel pour React et ES2015 :  
Ajoutez babel-preset-react babel-preset-es2015 à vos dépendances de développement pour compiler JSX en JS et avoir toutes les fonctionnalités ES6.
* mettez à jour votre fichier **.babelrc**
* mettez à jour votre configuration **webpack** et ajoutez le package [react-hot-loader](https://www.npmjs.com/package/react-hot-loader)

Tout d'abord, je veux structurer mon front-end sans le back-end pour connecter tout le front-end avec le back-end à la fin. Cela est dû au fait que je ne sais pas encore comment sera mon implémentation Redux. Donc, une connexion progressive au back-end ne serait pas efficace.

* restructurez votre **app.js** actuel dans un dossier propre
* créez un nouveau app.js comme point d'entrée et fournissez le [code de configuration de base](https://medium.com/@dabit3/beginner-s-guide-to-react-router-53094349669) pour rendre une page simple
* obtenez la configuration fonctionnelle. Installez les packages react-router, webpack-dev-server et react et react-dom
* l'ouverture d'une page sur le port du serveur de développement doit afficher votre composant react

[Voici à quoi ressemblaient mes commits sur Github après ces étapes](https://github.com/DDCreationStudios/votingApp/tree/9ed98937551ad5eb3208be392040b39c35d4d231).

#### Structure des composants

J'ai tout esquissé sur un papier et je suis arrivé à la conclusion que je dois construire 14 composants :

* le composant de l'application, qui héberge tout
* un en-tête
* un pied de page
* une barre latérale
* un composant d'inscription, de connexion et de médias sociaux
* un écran d'accueil
* une liste de tous les sondages
* l'affichage d'un sondage unique
* un composant pour le sondage et ses réponses
* les réponses sous forme de liste
* le graphique
* une page 404

Cette disposition était pour le début et devrait fournir un aperçu. Il est très naturel d'adapter la structure des composants lorsque l'application évolue.

#### Conception et construction des composants

* J'ai disposé tous les composants et les ai stylisés avec [Materialize](http://materializecss.com/). Materialize est un framework de design réactif.
* rappelez-vous que le stylisme avec React est plus compliqué que le stylisme des éléments HTML normaux. Pour des raisons de simplicité, j'ai tout fixé avec un stylisme en ligne sur le composant lui-même.

Conseil : Pour 100vh sur votre contenu principal, utilisez ce style en ligne sur une div. Il s'adapte parfaitement à la flexbox Materialize :

```
style={{  display: 'flex',  minHeight: '100vh',  flexDirection: 'column',}}
```

* Au fur et à mesure que vous construisez des composants, vous aurez une idée de la manière dont vous devez structurer votre gestion d'état avec React et Redux

Consultez mon commit sur [GitHub](https://github.com/DDCreationStudios/votingApp/tree/eb17c360e09515f22f8ac38574f576a53855037b) après la construction et le stylisme des composants

* Maintenant, nous devons configurer React Router pour obtenir une fonctionnalité de base et un sentiment pour l'application
* activez `historyApiFallback: true` sur votre serveur de développement webpack pour permettre un routage correct avec react router
* ajoutez l'état et sa gestion aux composants
* réalisez que Redux pourrait être une bonne prochaine étape

**Voici une liste d'apprentissages douloureux que j'ai dû subir tout au long de ce processus :**

* pour accéder aux propriétés des objets, utilisez la notation entre crochets au lieu de la notation par points. Par exemple : JavaScript `answers = answers.concat(this.refs[temp].value)`
* importer tout comme `* (import * as Polls from './ducks/polls';)` depuis ducks. Sinon, cela ne fonctionnera pas
* J'ai souvent lu à **ne pas** utiliser l'index d'une fonction map comme valeur de clé pour un composant. Cependant, lors du rendu avec `onChange` et de la génération d'une clé unique, l'entrée perd le focus et ne fonctionne pas correctement. Par exemple : `(const answerList = this.state.answers.map((answer, ind) => { return (<div className="input-field col s10" key={`ind}>)`
* lorsque vous itérez sur un tableau d'objets et que vous souhaitez changer les propriétés d'un objet, vous devez retourner un objet. Par exemple : `return{ answer: answ.answer, votes: 0};`   
Cela m'a pris 4 heures à comprendre ?

Les [Principes](http://redux.js.org/docs/introduction/ThreePrinciples.html) de Redux sont :

* Source unique de vérité
* L'état est en lecture seule
* Les changements sont faits avec des fonctions pures

Gardez à l'esprit que l'état local n'a pas besoin de participer à Redux lorsque son état n'est pas utilisé par d'autres composants.

* ajoutez les packages [react-redux](https://github.com/reactjs/react-redux) et [redux](https://github.com/reactjs/redux)
* utilisez la [structure ducks](https://github.com/erikras/ducks-modular-redux) pour mieux gérer les fichiers redux
* créez un store dans Redux et enveloppez votre application de rendu dans une balise `Provider` de react-redux
* connectez l'état à votre application avec `connect`
* ajoutez l'[Outil de Développement Redux](https://github.com/zalmoxisus/redux-devtools-extension) pour déboguer plus rapidement

Maintenant que l'État est disponible via Redux, il est temps de créer les gestionnaires d'événements et de tout rendre correctement. Maintenant, vous devriez également valider vos `propTypes`.

#### Visualisation

Pour afficher les résultats, j'ai choisi entre :

* [Recharts](http://recharts.org/#/en-US/examples/SimpleAreaChart)
* [Victory](http://formidable.com/open-source/victory/docs)
* [React-Vis](http://uber.github.io/react-vis/#/)
* [ReactD3](http://www.reactd3.org/docs/basic/#area)
* [React-Google-Charts](https://github.com/RakanNimer/react-google-charts)

Après avoir parcouru toutes les documentations et essayé quelques choses, j'ai fini par choisir React-Google-Charts. Google fournit de nombreuses options et le wrapper React facilite l'implémentation dans une application React.

Avec le wrapper React, cette étape a été super facile et rapide.

```
const resultChart = (props) => {  basic = [['Answer', 'Votes']];  (() => props.poll.answers.map(ans => basic.push([ans.answer, ans.votes])))();  return (    <Chart      chartType="PieChart"      data={basic}      options={{        title: `${props.poll.question}`,        pieSliceText: 'label',        slices: {          1: { offset: 0.1 },          2: { offset: 0.1 },          3: { offset: 0.1 },          4: { offset: 0.1 },        },        is3D: true,        backgroundColor: '#616161',      }}      graph_id="PieChart"      width="100%"      height="400px"      legend_toggle    />  );};
```

### Connecter le Front-end au Back-end Express avec React Router

#### Rendu côté client et côté serveur

Comme il s'agissait de ma première vraie application full-stack, la connexion du front-end et du back-end était un mystère pour moi. J'ai trouvé une bonne réponse à ma question sur Stack Overflow.

Pour résumer et citer la réponse de [Stijn](https://stackoverflow.com/users/286685/stijn-de-witt) :

> « Avec le routage côté client, que React-Router fournit, les choses sont moins simples. Au début, le client n'a encore chargé aucun code JS. Ainsi, la toute première requête sera toujours adressée au serveur. Celui-ci renverra alors une page contenant les balises de script nécessaires pour charger React et React Router, etc. Ce n'est que lorsque ces scripts ont été chargés que la phase 2 commence. Dans la phase 2, lorsque l'utilisateur clique sur le lien de navigation 'À propos de nous', par exemple, l'URL est modifiée localement uniquement en [http://example.com/about](http://example.com/about) (rendu possible par l'API History), mais aucune requête n'est faite au serveur. Au lieu de cela, React Router fait son travail côté client, détermine quelle vue React rendre et la rend. »

Pour lire plus de ses commentaires, cliquez [ici](https://stackoverflow.com/questions/27928372/react-router-urls-dont-work-when-refreshing-or-writting-manually).

En fin de compte, j'ai opté pour la solution catch-all : Voir dans mon fichier [routes.js](https://github.com/DDCreationStudios/votingApp/blob/master/src/serverSideES6/routes.js).

```
//routes.jsrouter.get('/*', (req, res) => {  const options = {    root: `${__dirname}/../../public/`,    dotfiles: 'deny',  };  res.sendFile('index.html', options);});
```

C'était facile et rapide à implémenter et couvrait les problèmes de base.

#### Servir tout ensemble

Pour comprendre cela, le meilleur moyen est de jeter un coup d'œil à mon fichier [package.json](https://github.com/DDCreationStudios/votingApp/blob/master/package.json).

Les scripts disent :

```
"scripts": {		"start": "node src/serverSide/server.js",		"serve": "babel-node src/serverSideES6/server.js",		"dev": "npm-run-all --parallel dev:*",		"dev:client": "webpack-dev-server --hot",		"dev:server": "nodemon src/serverSide/server.js",		"build": "npm-run-all --parallel build:*",		"build:client": "webpack --progress",		"build:server": "babel src/serverSideES6 --out-dir src/serverSide"	},
```

Le script `build` construit les fichiers côté client et côté serveur.

* Il compile tout mon code node.js ES6 en ES5 afin que Heroku puisse également le lire
* Webpack commence le bundling et la transpilation du côté client tel que de ES6 à ES5, et JSX à JavaScript.

Le script `dev` sert tout dans un environnement de développement et (hot) rechargement. Tout est aussi rapide et fluide que possible, lors de la modification de la base de code.

Le script `start` démarre réellement le serveur back-end, qui consomme également le front-end HTML, CSS, JavaScript construit et bundlé, présentant l'application entière.

### Déploiement

Pour déployer l'application, Heroku s'est une fois de plus avéré être la solution à adopter.

En utilisant la [CLI Heroku](https://devcenter.heroku.com/articles/heroku-cli), la commande `Heroku logs` aide beaucoup. J'ai toujours eu des problèmes à configurer mon application sur la plateforme. Mais après avoir résolu toutes les erreurs que les logs montrent, cela devient très facile.

Toujours important :

* Soyez conscient que les devDependencies ne sont pas installées
* Utilisez le build-pack adéquat. Dans ce cas, il s'agit de Node.js
* Ayez un script `start` ou définissez-en un dans votre Procfile
* Assurez-vous de pousser la bonne branche depuis le bon dépôt

### Conclusion

Comme vous pouvez le voir, ma documentation pour cet article se dégrade de plus en plus avec l'avancement de l'application. Cela est dû au fait que j'ai été complètement submergé par Redux. J'ai fait d'autres projets en parallèle et je n'ai pas pu suivre.

Mais ne vous inquiétez pas ! J'ai essayé de nommer mes commits aussi clairement que possible. Vous pouvez donc parcourir tous les commits pour plus de détails dans mon dépôt. Voir [Commits ici](https://github.com/DDCreationStudios/votingApp/commits/master).

Si vous avez des questions, n'hésitez pas à demander :)

* Le dépôt sur Github est disponible [ici](https://github.com/DDCreationStudios/votingApp).
* La version live du résultat est disponible [ici](https://ddcs-votingapp.herokuapp.com/).
* Les apprentissages et les chiffres sont disponibles [ici](https://github.com/DDCreationStudios/Writing/blob/master/articles/LearningsFirstFullStack.md).

Un grand merci à [Edo Rivai](https://twitter.com/EdoRivai), qui a donné des conseils très précieux tout au long du chemin. :)

Merci d'avoir lu mon article ! N'hésitez pas à laisser tout commentaire !