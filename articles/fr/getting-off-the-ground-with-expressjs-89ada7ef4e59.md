---
title: Décoller avec Express.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-08T19:49:49.000Z'
originalURL: https://freecodecamp.org/news/getting-off-the-ground-with-expressjs-89ada7ef4e59
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ofMfrqFMfpaTH_RMvI_RQA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Décoller avec Express.js
seo_desc: 'By Victor Ofoegbu

  Writing web apps with the Node.js framework


  A common moment of truth is when you develop a lot of applications that need the
  same or identical functionality. It’s now obvious that copying and pasting code
  isn’t scalable — you need ...'
---

Par Victor Ofoegbu

#### Écrire des applications web avec le framework Node.js

![Image](https://cdn-media-1.freecodecamp.org/images/1*ofMfrqFMfpaTH_RMvI_RQA.jpeg)

Un moment de vérité courant se produit lorsque vous développez de nombreuses applications qui nécessitent les mêmes fonctionnalités ou des fonctionnalités identiques. Il est désormais évident que copier et coller du code n'est pas scalable — vous avez besoin d'un outil conçu pour la flexibilité, la minimalité et la réutilisabilité.

C'est là qu'Express s'intègre dans la stack MERN. C'est un framework Node.js pour construire des applications web scalables.

Dans cet article, nous allons approfondir la construction d'applications web avec le framework Express. Nous examinerons l'intégration de la base de données, les sessions et les cookies, les moteurs de templating pour solidifier notre flux de travail, et enfin les préoccupations de production et de sécurité.

Ce tutoriel nécessite que vous ayez Node.js et npm installés, et vous devriez posséder une compréhension de base de Node.js et de JavaScript en général. Si vous n'êtes pas familier avec Node.js, voici mon dernier article : [The only NodeJs introduction you'll ever need](https://codeburst.io/the-only-nodejs-introduction-youll-ever-need-d969a47ef219?source=activity---post_recommended_rollup). C'est un excellent point de départ pour plonger dans Node.js.

### Faisons Express !

Express a été construit par TJ Holowaychuk qui s'est inspiré du framework Ruby on Rails Sinatra. La dernière version d'Express est la 4.16.1. Express 4 est devenu plus léger en abandonnant certains des modules que les développeurs n'utilisaient pas toujours. Ainsi, ils pouvaient facilement les importer uniquement lorsqu'ils en avaient besoin. Cela a du sens, n'est-ce pas ?

Pour commencer avec Express, vous devez l'installer et l'importer dans votre programme.

1) Créez un dossier appelé `express-app`, `cd` dedans et tapez `npm init`. Cela crée notre fichier `package.json`.

2) Toujours sur le terminal ou la ligne de commande, tapez `npm install --save express`. Cela installera express dans le projet. Le double tiret `save` signifie simplement que nous l'ajoutons à notre fichier `package.json`.

3) À la racine de notre dossier express-app, créez un fichier `server.js` et copiez ceci à l'intérieur.

```js
const express = require('express'),
      app = express();

app.get('/',(request,response)=>{
  response.send('Hello world');
});

//Lier le serveur à un port(3000)
app.listen(3000,()=>console.log('express server started at port 300'));
```

const express = require('express'),      app = express();app.get('/',(request,response)=>{  response.send('Hello world');});//Lier le serveur à un port(3000)app.listen(3000,()=>console.log('express server started at port 300'));

4) Retournez au terminal, toujours dans le même dossier, et tapez `node server.js`. Allez dans votre navigateur et visitez [localhost](http://localhost:3000).

Nous importons notre module Express. Si vous étiez assez observateur, vous avez dû remarquer que nous n'avions pas besoin du module `http` comme nous le faisons dans les applications Node.js pures. C'est parce qu'Express l'utilise, donc nous n'avons pas besoin de le faire à nouveau.

Lorsque nous `require ('express')`, ce qui nous est exporté est une fonction, donc nous pouvons l'appeler directement et l'assigner à la variable `app`. À ce stade, rien ne fonctionnera jusqu'à ce que nous gérions réellement la requête. Cela s'appelle le `routing` et cela signifie donner au client ce qu'il demande.

Express nous donne quelques verbes de base pour effectuer des opérations HTTP (comme GET, POST, PUT et DELETE). Dans notre exemple ici, nous utilisons une méthode `app.get()` qui gère les requêtes GET vers le serveur. Elle prend deux arguments : le `path` de la requête et un callback pour gérer la requête.

Si vous n'avez pas compris cela, je vais expliquer davantage.

Un **path** est une adresse vers une ressource sur un ordinateur. **Un callback est une fonction passée à une autre fonction en tant qu'argument qui est appelée lorsque certaines conditions se produisent.**

Vous vous souvenez peut-être de ceci :

```
$('p').click(function(){
   console.log('Vous avez cliqué sur moi')
});
```

Ici, nous ajoutons un callback à déclencher lorsque p est cliqué. Vous voyez ? C'est facile.

Sur la dernière ligne de `server.js`, nous écoutons sur le port 3000 et console.log lorsque nous démarrons le serveur.

Je parie que vous ne pouvez pas écrire des applications avec cela. Approfondissons.

### Routing dans Express

Le routing signifie assigner des fonctions pour répondre aux requêtes des utilisateurs. Les routeurs Express sont essentiellement des middlewares (ce qui signifie qu'ils ont accès aux objets `request` et `response` et font un peu de travail pour nous).

Le routing dans Express suit ce format de base :

```
app.VERB('path', callback…);
```

**Où `VERB` est l'un des verbes `GET`, `POST`, `PUT`, et `DELETE`.**

Nous pouvons ajouter autant de callbacks que nous le souhaitons. Voici un exemple :

```js
const express = require('express'),
      app = express();
      
function sayHello(request,response,next){
  console.log('Je dois être appelé');
  next();
}

app.get('/', sayHello, (request, response)=>{
  response.send('sayHello');
});

app.listen(3000,()=>console.log('Express server started at port 3000'));
```

Allez dans votre terminal ou invite de commande et tapez `node server.js`. Vous verrez que la fonction `sayHello` se déclenche avant que la réponse ne soit envoyée au navigateur.

La fonction `sayHello` prend trois arguments (`request`, `response`, et `next`).

La fonction `next()`, lorsqu'elle est appelée, transfère le contrôle au middleware ou à la route suivante.

#### Les objets request et response

L'objet `request` contient des informations sur la requête entrante. Voici les propriétés et méthodes les plus utiles :

La variable `**request.params**` stocke un objet de paramètres de requête GET nommés. Par exemple, effacez votre fichier `server.js` et collez ceci à l'intérieur :

```js
const express = require('express'),
      app = express();
      
app.get('/:name/:age', (request, response)=>{
   response.send(request.params);
});

app.listen(3000,()=>console.log('Express server started at port 3000'));
```

Exécutez ceci avec `node server.js`, puis allez dans votre navigateur et exécutez : `[https://localhost:3000/john/5](https://localhost:3000/john/5)`

Dans le code ci-dessus, nous obtenons des variables de l'URL et les envoyons au navigateur. Le point est que `request.params` est un objet contenant tous ces paramètres GET. Remarquez le deux-points avant les paramètres. Ils différencient les paramètres de route des chemins de route normaux.

La propriété `**request.body**` stocke les paramètres de formulaire POST.

La propriété `**request.query**` est utilisée pour extraire les données de formulaire GET. Voici un exemple de cela :

1) Créez un autre dossier appelé `express-query`, puis créez deux fichiers : `server.js` et `form.html`. Collez ceci dans `server.js` :

```js
const express = require('express'),
      app = express();
      
//route sert à la fois la page de formulaire et traite les données de formulaire
app.get('/', (request, response)=>{
  console.log(request.query);
  response.sendFile(__dirname +'/form.html');
});

app.listen(3000,()=>console.log('Express server started at port 3000'));
```

2) Copiez ceci dans le fichier `form.html` :

```js
<!--action spécifie que le formulaire soit géré sur la même page-->
<form action='/' method='GET'>
  <input type='text' name='name'/>
  <input type='email' name='email'/>
  <input type='submit'/>
</form>
```

Exécutez le code avec `node server.js`, tapez `[localhost:3000](http://localhost:3000)`, et remplissez et soumettez le formulaire dans votre navigateur. Après avoir soumis le formulaire, les données que vous avez remplies sont enregistrées dans la console.

`**request.headers**` contient des paires clé/valeur de la requête reçue par le serveur. Les serveurs et les clients utilisent des en-têtes pour communiquer leur compatibilité et leurs contraintes.

`**request.accepts(['json','html'])**` contient un tableau de formats de données et retourne le format que le navigateur préfère pour collecter les données. Nous verrons également cela lors du traitement des formulaires Ajax.

`**request.url**` stocke des données sur l'URL de la requête.

`**request.ip:**` contient l'adresse IP (Internet Protocol) du navigateur demandant des informations.

L'objet `response` est également livré avec quelques méthodes pratiques pour obtenir des informations utiles sur la requête sortante.

`**response.send(message)**` envoie son argument au navigateur.

`**response.json()**` envoie son argument en tant que données au navigateur au format JSON.

`**response.cookie(name,value,duration)**` fournit une interface pour définir des cookies sur les navigateurs. Nous parlerons également des cookies.

`**response.redirect([redirect status], url)**` redirige le navigateur vers l'URL spécifiée avec le statut optionnel.

`**response.render('file',{routeData: routedata})**` rend une vue au navigateur et prend un objet contenant des données dont le routeur pourrait avoir besoin. Vous comprendrez mieux lorsque nous verrons les vues.

`**response.set(name,value)**` définit les valeurs d'en-tête. Mais vous ne voulez pas faire cela, car cela interfère avec le travail du navigateur.

`**response.status(status)**` définit le statut d'une réponse particulière (404, 200, 401 et ainsi de suite).

Vous n'avez pas besoin de mémoriser tout cela. En les utilisant, vous les maîtriserez subconsciemment.

### Express Router

Avec Express Router, nous pouvons diviser notre application en fragments qui peuvent avoir leurs propres instances d'express à utiliser. Nous pouvons les rassembler de manière très propre et modulaire.

Prenons par exemple. Ces quatre URLs aléatoires :

localhost:3000/users/john

localhost:3000/users/mark

localhost:3000/posts/newpost

localhost:3000/api

Notre approche normale de faire cela avec Express serait :

```js
const express = require('express'),
      app = express();

//Différentes routes
app.get('/users/john',(request,response)=>{
    response.send(`Page de John`);
});

app.get('/users/mark',(request,response)=>{
    response.send(`Page de John`);
});

app.get('/posts/newpost',(request,response)=>{
  response.send(`Ceci est un nouveau post`);
});

app.get('/api',(request,response)=>{
  response.send('Point de terminaison API');
});

app.listen(3000,()=>console.log('Serveur démarré sur le port 3000'));
```

Il n'y a rien de mal avec ce modèle à ce stade. Mais il a un potentiel d'erreurs. Lorsque nos routes sont au nombre de cinq, il n'y a pas beaucoup de problèmes. Mais lorsque les choses grandissent et que beaucoup de fonctionnalités sont requises, mettre tout ce code dans notre `server.js` n'est pas quelque chose que nous voulons faire.

#### **Laissons Router faire cela pour nous**

Créez un dossier appelé `react-router` à la racine de notre projet, créez un fichier à l'intérieur et appelez-le `basic_router.js`. Copiez ceci à l'intérieur :

```js
const express = require('express'),
      router = express.Router();

//utilisation de routes normales
router.get('/john',(request,response)=>{
  response.send('Page d\'accueil de l\'utilisateur');
});

router.get('/mark',(request,response)=>{
  response.send('Page d\'accueil de l\'utilisateur');
});

//exportation du routeur vers d'autres modules
module.exports = router;
```

Nous créons essentiellement une autre instance d'Express. Cette fois, nous appelons la fonction `Router()` d'Express. Il est possible d'appeler directement `express()` en tant que fonction (comme dans notre `**server.js**`) et d'appeler également `express.Router()`. Cela est dû au fait qu'Express est exporté en tant que fonction, et en JavaScript, les fonctions sont également des objets.

Nous ajoutons des routes comme une application Express normale. Mais nous ne le lions à aucun port. L'objet `router` contient toutes les routes que nous avons définies, donc nous exportons uniquement cet objet afin que d'autres parties de notre programme puissent également l'utiliser.

Nous créons notre `server.js` principal, et l'ajoutons en tant que middleware. Oui, les middlewares facilitent le travail, vous vous souvenez ?

```js
const express = require('express'),
      app = express();

//importation du basic_router.js
app.use('/users',require('.react-router/basic_router'));

//routes
app.get('/posts/newpost',(request,response)=>{
  response.send('nouveau post');
});

app.get('/api',(request,response)=>{
  response.send('Route API');
});

app.listen(3000,()=>console.log('Express server started at port 3000'));
```

Maintenant, exécutez ceci. Naviguez vers `localhost:3000/user/john` et `localhost:3000/user/mark`. Vous voyez ? Les choses sont assez faciles à regrouper à ce stade.

Nous pouvons faire cela pour toutes les autres routes. Créez un autre fichier pour nos APIs. Nous l'appellerons `api_route.js`. Copiez ceci à l'intérieur :

```js
const express = require('express'),
      router = express.Router();

router.get('/',(request,response)=>{
  response.send('Page d\'accueil de l\'utilisateur');
});

//quelques autres points de terminaison pour soumettre des données
module.exports = router;
```

Maintenant, retournez à notre `**server.js**` et changez le code en ceci :

```js
const express = require('express'),
      app = express();

app.use('/users',require('./basic_router'));
                         
app.use('/api',require('./api_route'));

app.get('/posts/newpost',(request,response)=>{
   response.send('nouveau post');
});

app.listen(3000,()=>console.log('Express server started at port 3000'));
```

Cela représente suffisamment d'informations pour construire des routes d'applications web de base.

### Moteurs de templates

![Image](https://cdn-media-1.freecodecamp.org/images/1*2jgQ7PxyWZKsORaDoWe6_w.jpeg)
_Photo par [Unsplash](https://unsplash.com/photos/JaWmkrSFR2Q?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Michael Mroczek</a> sur <a href="https://unsplash.com/search/photos/engines?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

La plupart du temps, vous n'êtes pas définitif sur le nombre de pages que vous souhaitez avoir sur votre site web. Cela signifie que vous voudrez garder les choses flexibles, réutilisables et propres.

Imaginez que vous avez un pied de page que vous souhaitez utiliser sur chaque page. Ne serait-ce pas cool si vous le placiez simplement dans un fichier et l'intégriez avec une ligne de code sur chaque page ? Ou comment aimeriez-vous supprimer le `.html` de votre URL ?

Ce ne sont là que quelques-unes des choses que les moteurs de templates peuvent faire pour nous.

Il existe de nombreux moteurs de templates à l'heure actuelle. Mais nous utiliserons Handlebars pour voir comment fonctionne un template. Heureusement, les mêmes principes s'appliquent à presque tous les moteurs de templates — il n'y a que des changements de syntaxe.

Pour utiliser Handlebars, nous l'installons.

```
npm install --save express-handlebars
```

`require` dans votre fichier et configurez votre application pour l'utiliser comme suit :

```js
const express = require('express'),
      hbs = require('express-handlebars').create({defaultLayout:'main.hbs'}),
      app = express();

app.engine('hbs', hbs.engine);
app.set('view engine','hbs');
```

Faisons donc un rendu de base avec Handlebars :

1. Créez un dossier appelé `express-handlebars`, créez un dossier `views`, et à l'intérieur du dossier `views`, créez un autre dossier appelé `layouts`.

2) Créez un fichier `server.js` et collez ceci à l'intérieur :

```js
const express = require('express'),
      hbs = require('express-handlebars').create({defaultLayout:'main.hbs'}),
      app = express();

//définir notre moteur d'application sur handlebars
app.engine('hbs', hbs.engine);
app.set('view engine', 'hbs');
app.get('/',(request,response)=>{
  response.render('home',{title: 'Accueil'});
});

app.get('/about',(request,response)=>{
  response.render('about',{title: 'À propos'});
});

app.listen(3000,()=>console.log('Express server started at port 3000'));
```

3) À l'intérieur du dossier `layouts`, créez un fichier `main.hbs`. Collez ceci à l'intérieur :

```
<!-- Le fichier main.hbs agira comme un modèle par défaut pour chaque vue sur le site -->

<!DOCTYPE html>
<html>
<head>
<meta charset='UTF-8'>

<!-- La variable title sera remplacée par le titre de chaque page -->

<title>{{title}}</title>
</head>

<body>
<!-- Le contenu des autres pages remplacera la variable body -->
{{{body}}}
</body>
</html>
```

4) Ensuite, nous allons créer les vues séparées. À l'intérieur du dossier `views`, créez deux fichiers — `home.hbs` et `about.hbs`. Collez ce qui suit à l'intérieur de `home.hbs` :

```
//home.hbs
<!-- Ceci est la vue Accueil et sera rendu dans le layout main.hbs -->

<div>
  Bonjour, je suis la page d'accueil et vous êtes les bienvenus
</div>
```

et dans notre `about.hbs` :

```
//about.hbs
<!-- Ceci est la vue À propos et sera également rendu dans le layout main.hbs -->

<div>
  Bonjour, je suis la page à propos, que voulez-vous savoir
</div>
```

Faites un `node server.js` dans votre terminal et tapez `[http://localhost:3000](http://localhost:3000)` sur votre navigateur.

Qu'est-ce qui se passe ici ?

Nous commençons par importer `express-handlebars` et créer un `defaultLayout`, en l'assignant à `main.hbs`. Cela signifie que toutes nos vues seront rendues dans le layout `main.hbs`.

Jetez un coup d'œil au `server.js`. Juste quelques petites choses ont changé, n'est-ce pas ? Commençons par ces deux lignes :

```js
app.engine('hbs', hbs.engine);
app.set('view engine','hbs');
```

La première ligne définit le moteur de l'application sur `hbs.engine` et la deuxième ligne définit la propriété du moteur de vue sur handlebars. Assez simple, n'est-ce pas ?

Les routes dans notre `server.js` sont également un peu différentes. Voici le coupable :

```js
response.render('home',{title: 'Accueil'});
```

Alors que `.send()` envoie du texte brut au navigateur, `render()` recherche le premier paramètre dans le dossier `views` et le rend au navigateur. La plupart du temps, nous pourrions vouloir passer du contenu dynamique à la vue également. Nous donnons à la méthode render un objet comme deuxième paramètre. L'objet contient des clés et des valeurs de données à passer à l'intérieur de la vue.

Prenez cette ligne dans notre fichier `main.hbs` dans notre dossier de layout.

```
//main.hbs
<title>{{title}}</title>
```

Le `{{title}}` est remplacé par ce qui est passé avec la vue. Dans notre cas, le `{title: 'Accueil'}`. Nous pouvons passer autant de valeurs que nous le souhaitons à la vue. Il suffit de l'ajouter comme propriété de l'objet.

Lorsque nous faisons un `response.render()`, Express sait où obtenir les fichiers que nous demandons. Regardons le `about.hbs`.

```
<!-- Ceci est la vue À propos et sera rendu dans le layout main.handlebars -->
<div>
  Bonjour, je suis la page à propos, que voulez-vous savoir
</div>
```

Le contenu de ce fichier remplace la variable body dans notre `layout.handlebars` :

```
{{{body}}}
```

Si vous vous demandez pourquoi nous utilisons deux accolades pour {{title}} et trois pour le {{{body}}}, vous êtes sur la bonne voie.

Lorsque nous utilisons deux accolades, nous affichons tout, même les balises HTML (non échappées). Voici ce que je veux dire.

Si le contenu que nous voulons envoyer au navigateur est `<b>Bonjour le monde</b>`, avec deux accolades, Express le rendra comme `<b&gt;Bonjour le monde</b>`. Si nous utilisons trois accolades, Express comprendra que nous voulons un texte en gras et le rendra comme Bonjour le monde (en gras).

C'est ainsi que fonctionnent les moteurs de templates dans Express. [Handlebars](http://handlebarsjs.com/) fournit une documentation d'une page. Je la considère comme un bon point de départ.

### Rendu de contenu statique dans Express

Avez-vous déjà pensé à l'endroit où nous allons stocker nos fichiers CSS, JavaScript et images ? Eh bien, Express fournit un middleware pour que le serveur sache où trouver le contenu statique.

Voici comment l'utiliser :

```js
app.use(express.static(__dirname +'public'));
```

Placez ceci en haut de votre `server.js`, juste après les instructions require. `__dirname` contient le chemin où le programme est exécuté.

Si vous n'avez pas compris cela, essayez ceci.

Supprimez tout dans votre `server.js`, et mettez ceci à l'intérieur :

`console.log(__dirname);`

Allez dans votre ligne de commande, et exécutez `node server.js`. Il vous montre le chemin vers le fichier node qui est en cours d'exécution.

L'endroit où nous stockons notre contenu statique nous appartient. Nous pourrions vouloir le nommer `assets` ou autre chose, mais vous devez vous assurer de l'ajouter au `dirname` comme suit :

```js
express.static(__dirname + 'static_folder_name').
```

### Middleware Express

Les middlewares sont des fonctions qui encapsulent des fonctionnalités. Ils effectuent des opérations sur les requêtes HTTP et nous fournissent une interface de haut niveau pour les personnaliser. La plupart des middlewares prennent trois arguments : les objets **request**, **response** et une fonction **next**. Dans les middlewares de gestion des erreurs, il y a un paramètre supplémentaire : l'objet **err**, qui peut nous informer de l'erreur et nous permettre de la transmettre à d'autres middlewares.

Nous ajoutons des middlewares à notre serveur en utilisant `**app.use(name_of_middleware)**`. Il est également important de noter que les middlewares sont utilisés dans le même ordre où ils ont été ajoutés. Je vous montrerai un exemple plus tard si vous ne comprenez pas.

Avec cette définition, nous pouvons également voir les fonctions de routage comme `app.get()`, `app.post()` et ainsi de suite, comme des middlewares, sauf qu'ils sont appliqués à des requêtes de verbes HTTP particuliers. Vous pourriez également trouver intéressant de savoir qu'il existe une route `app.all()` qui est appliquée à toutes les requêtes HTTP sans tenir compte du fait qu'elles soient GET, POST ou autres.

```js
//Ce middleware sera appelé pour chaque requête. GET ou POST
app.all((request,response)=>{
  console.log('Hello world');
})
```

Les gestionnaires de routes prennent deux paramètres, le chemin à correspondre et le middleware à exécuter.

```js
app.get('/',(request,,response)=>{
  response.send('Hello world');
});
```

Si le chemin est omis, le middleware s'applique à chaque requête GET.

```js
//Chaque requête GET appellera ce middleware
app.get((request,response)=>{
  response.send('Hello world');
});
```

Dans notre exemple ci-dessus, une fois que nous envoyons une requête `GET`, notre serveur répond au navigateur en envoyant un message `Hello world` puis se termine jusqu'à ce qu'il y ait une autre requête.

Mais nous pourrions vouloir que plus d'un middleware soit appelé. Il y a un moyen de faire cela. Vous vous souvenez de notre fonction `next` ? Nous pourrions l'utiliser pour transférer le contrôle à un autre middleware.

Voyons comment cela fonctionne. Copiez et collez ce code dans notre `server.js` :

```js
const express = require('express'),
      app = express();
      
//définir le port
app.set('port', process.env.PORT || 3000);

//premier middleware
app.use((request,respone,next)=>{
  console.log(`traitement des données pour ${request.url}`);
  next();
});

//deuxième middleware
app.use((request,response,next)=>{
  console.log(`Le response.send va terminer la requête`);
response.send(`Hello world`);
});

//troisième middleware
app.use((request,respone,next)=>{
  console.log(`Je ne serai jamais appelé`);
});

app.listen(3000,()=>console.log('Express server started at port 3000'));
```

Depuis le terminal, tapez `node server.js` et regardez le terminal. Allez dans votre navigateur et ouvrez `localhost:3000`. Regardez à nouveau votre console, et vous verrez quelque chose de similaire.

```
Express server started at port 3000
traitement des données pour /
Le response.send va terminer la requête
```

Notre premier middleware s'exécute chaque fois qu'une requête est reçue. Il écrit quelque chose dans la console et appelle la fonction `next()`. Appeler la fonction `next()` indique à Express de ne pas terminer l'objet `request` mais envoie le contrôle au **prochain** middleware. Chaque fois que nous écrivons un middleware sans appeler la fonction `next`, Express termine l'objet `request`.

Dans le deuxième middleware, nous passons la fonction `next()` comme argument mais nous ne l'appelons jamais. Cela termine l'objet `request` et le troisième middleware n'est jamais appelé. Notez que si nous n'avons jamais envoyé quoi que ce soit au navigateur dans le deuxième middleware, le client finira par expirer.

Voici quelques middlewares utiles dans Express.js :

* [Morgan](https://github.com/expressjs/morgan) — journalise chaque requête
* [CORS](https://github.com/expressjs/cors) — active le partage de ressources entre origines multiples
* [body-parser](https://github.com/expressjs/body-parser) — un middleware pour analyser le `request.body` dans les applications Express
* [Multer](https://github.com/expressjs/multer) — middleware Node.js pour gérer `multipart/form-data`
* [session](https://github.com/expressjs/session) — middleware de session simple pour Express.js
* [errorhandler](https://github.com/expressjs/errorhandler) — middleware de gestion des erreurs uniquement pour le développement
* [serve-favicon](https://github.com/expressjs/serve-favicon) — middleware de service de favicon
* [csurf](https://github.com/expressjs/csurf) — middleware de protection CSRF pour Node.js
* [Passport](http://www.passportjs.org/) — authentification simple et non intrusive
* [Merror](https://github.com/mamsoudi/merror) — un middleware Express convivial pour la gestion des erreurs HTTP et les réponses d'erreur
* [Expressa](https://github.com/thomas4019/expressa) — middleware express pour créer facilement des API REST

### Gestion des données de formulaire dans Express

La fonction principale du web est la communication. Express nous fournit des outils pour comprendre ce que les clients demandent et comment répondre correctement.

Express a essentiellement deux endroits pour stocker les données client. Le **request.querystring (pour les requêtes GET)** et le **request.body (pour les requêtes POST)**. Du côté client, il est idéal d'utiliser la méthode POST pour la soumission de formulaire car la plupart des navigateurs placent des limites sur la longueur de la `querystring` et des données supplémentaires sont perdues. Si vous ne savez pas ce qu'est une chaîne de requête, c'est la partie après votre URL qui contient des données et ne s'intègre pas correctement dans votre système de chemin de routage. Au cas où vous ne comprenez pas tout à fait ce qu'est une chaîne de requête, voici un exemple :

```
facebook.com/users?name=Victor&age=100&occupation=whatever
```

À partir du point où le point d'interrogation commence s'appelle la chaîne de requête. Elle transmet des données au serveur mais les expose dans l'URL.

Il est également bon de garder la chaîne de requête aussi propre que possible. Envoyer de grandes données avec des requêtes GET rend la chaîne de requête désordonnée.

Voyons une démonstration. Nous allons prendre certaines données de notre client via GET et les lui renvoyer.

Créez un dossier, appelez-le `form-data`, et créez deux fichiers à l'intérieur : `server.js` et `form.html`. Collez ceci dans les fichiers `server.js` et `form.html` respectivement :

```js
//fichier server.js

const express = require('express'),
      app = express();

//définir le port 
app.set('port', process.env.PORT || 3000);

//
app.get('/',(request,response)=>{
  response.sendFile(__dirname +'/form.html');
});

app.get('/process',(request,response)=>{
  console.log(request.query);
  response.send(`${request.query.name} a dit ${request.query.message}`);
});

app.listen(3000,()=>{
  console.log('Express server started at port 3000');
});
```

```html
//form.html

<!DOCTYPE html>
<html>
  <head>
    <meta charset='UTF-8'>
    <title>Page de formulaire</title>
    <style>
      *{
        margin:0;
        padding:0;
        box-sizing: border-box;
        font-size: 20px;
      }
      input{
        margin:20px;
        padding:10px;
      }
      input[type="text"],
      textarea {
        width:200px;
        margin:20px;
        padding:5px;
        height:30px;
        display: block;
      }
      textarea{
        resize:none;
        height:60px;
      }
    </style>
  </head>
<body>
  <form action='/process' method='GET'>
    <input type='text' name='name' placeholder='nom'/>
    <textarea name='message' placeholder='message'></textarea>
    <input type='submit'/>
  </form>
</body>
</html>
```

Exécutez `node server.js`, allez sur `localhost:3000`, remplissez le formulaire et soumettez-le.

Voici à quoi ressemblerait le résultat.

Dans notre fichier `server.js` ici, nous avons deux routes GET. Une pour `localhost:3000` et `localhost:3000/process`.

```js
app.get('/' ,(request,response)=>{
   response.sendFile(__dirname + '/form.html');
});
```

Et

```js
app.get('/process',(request,response)=>{
  response.send(`${request.query.name} a dit ${request.query.message}`);
});
```

Allez dans votre console. Vous verrez un objet. Cela prouve que notre `request.query` est un objet qui contient toutes les requêtes et leurs valeurs.

```js
{
  name: 'victor',
  message: 'Hello world'
}
```

Si vous regardez notre formulaire dans la page `form.html`, vous remarquerez que notre formulaire a des attributs `action` et `method`. L'attribut `action` spécifie la page ou la route qui doit gérer les données du formulaire ('process' dans ce cas). Lorsque le formulaire est soumis, il envoie une requête GET à la route `process` avec le contenu de notre formulaire en tant que données `querystring`.

Notre fichier `server.js` gère également la requête pour le chemin de processus et envoie les données passées de notre `form.html` au navigateur et à la console.

Voyons comment nous gérons cela avec la méthode POST. Il est temps d'effacer notre fichier `server.js`. Copiez et collez ce code dans `server.js` :

```js
//server.js

const express = require('express'),
      app = express(),
      
//Vous devez importer le middleware body-parser pour accéder à request.body dans express
bodyParser = require('body-parser');

//configuration de bodyparser
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

//définir notre port
app.set('port', process.env.PORT || 3000);

//Route Get pour localhost:3000
app.get('/',(request,response)=>{
  response.sendFile(__dirname +'/form.html');
});

//Route POST pour la gestion des formulaires
app.post('/',(request,response)=>{
  console.log(request.body);  
  response.send(`${request.body.name} a dit ${request.body.message}`);
});

app.listen(3000,()=>{
  console.log('Express server started at port 3000');
});
```

```js
//fichier form.html

<!DOCTYPE html>
<html>
  <head>
  <meta charset='UTF-8'>
  <title>Page de formulaire</title>
    <style>
      *{
        margin:0;
        padding:0;
        box-sizing: border-box;
        font-size: 20px;
      }
      input{
        margin:20px;
        padding:10px;
      }
      input[type='text'],
      textarea {
        width:200px;
        margin:20px;
        padding:5px;
        height:30px;
        display: block;
      }
      textarea{
        resize:none;
        height:60px;
      }
    </style>
  </head>
<body>
  <form action='/' method='POST'>
    <input type='text' name='name' placeholder='nom'/>
    <textarea name='message' placeholder='message'></textarea>
    <input type='submit'/>
  </form>
</body>
</html>
```

Si vous regardez de près, la première chose différente que nous faisons est d'importer et d'utiliser `body-parser`. Body-parser est un middleware qui rend les données POST disponibles dans notre `request.body`. Gardez à l'esprit que le `request.body` ne fonctionnera pas sans le middleware body-parser.

Vous remarquerez peut-être également que nous avons à la fois des gestionnaires de routes GET et POST. Le middleware GET affiche le formulaire et le middleware POST le traite. Il est possible pour les deux d'utiliser un seul chemin de route car ils ont des méthodes différentes.

Nous ne pouvions pas faire cela pour notre premier exemple car la méthode de notre formulaire était GET. Évidemment, vous ne pouvez pas avoir deux requêtes GET pour la même route et avoir les deux envoyer des données au navigateur. C'est pourquoi notre premier exemple a traité le formulaire sur le chemin `/process`.

### Gestion des formulaires AJAX

La gestion des formulaires Ajax avec Express est assez simple. Express nous fournit une propriété `request.xhr` pour nous dire si une requête est envoyée via AJAX. Nous pouvons coupler cela avec la méthode `request.accepts()` dont nous avons parlé plus tôt. Cela nous aide à déterminer le format dans lequel le navigateur veut les données. Si le client veut du JSON, eh bien, nous lui donnerons simplement du JSON.

Modifions notre `form.html` pour utiliser AJAX et notre `server.js` pour accepter AJAX et envoyer du JSON.

```html
<!DOCTYPE html>
<html>
  <head>
  <meta charset='UTF-8'>
  <title>Page de formulaire</title>
    <script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.js'></script>
  <style>
    *{
      margin:0;
      padding:0;
      box-sizing: border-box;
      font-size: 20px;
    }
    input{
      margin:20px;
      padding:10px;
    }
    input[type="text"],
    textarea {
      width:200px;
      margin:20px;
      padding:5px;
      height:30px;
      display: block;
    }
    textarea{
      resize:none;
      height:60px;
    }
  </style>
  </head>
<body>
  <div></div>
                       
  <form action='/' method='POST'>
    <input type='text' name='name' placeholder='nom'/>
    <textarea name='message' placeholder='message'></textarea>
    <input type='submit'/>
  </form>
                       
  <script>
    $('form').on('submit',makeRequest);
      function makeRequest(e){
        e.preventDefault();
        $.ajax({
          url:'/',
          type : 'POST',
          success: function(data){
            if(data.message){
              $('div').html(data.message);
            } else {
              $('div').html('Désolé, une erreur est survenue');
            }
          },
          error: function(){
            $('div').html('Désolé, une erreur est survenue');
          }
      });
    }
  </script>
  </body>
</html>
```

```js
//server.js

const express = require('express'),
      app = express(),
      bodyParser = require('body-parser');

//configuration du middleware body-parser
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

//définir le port de notre application
app.set('port', process.env.PORT || 3000);

//Route pour les requêtes get.
app.get('/',(request,response)=>{
  response.sendFile(__dirname +'/form.html');
});

//Route pour gérer les requêtes de formulaire POST.
app.post('/',(request,response)=>{
//nous vérifions si la requête est une requête AJAX et si elle accepte JSON
  if(request.xhr || request.accepts('json, html')==='json'){
    response.send({message:'Je voulais juste vous dire. Ça a marché'});
   } else {
    //Faites autre chose en rechargeant la page.
   }
});

app.listen(3000,()=>{
  console.log('Express server started at port 3000');
});
```

#### **Voici comment cela fonctionne**

Pas beaucoup de changements ici — nous avons juste ajouté un moyen de vérifier si la requête a été faite avec AJAX.

Donc voici ce que nous faisons. Nous avons fait de la requête une requête AJAX avec la méthode POST. Nous avons lié le CDN de jQuery. Dans la balise script, nous attachons un gestionnaire d'événements pour l'événement submit. Lorsque nous faisons cela, nous empêchons le comportement par défaut de recharger la page.

Nous utilisons ensuite la méthode jQuery `$.ajax()` pour faire une requête AJAX. Le serveur répond avec un objet avec une propriété `message`, que nous ajoutons ensuite à la div vide.

Si vous n'êtes pas familier avec AJAX, j'ai déjà écrit quelques articles sur AJAX. Consultez-les : [Une introduction en douceur à AJAX](https://codeburst.io/a-gentle-introduction-to-ajax-1e88e3db4e79) et [Des requêtes asynchrones plus faciles avec jQuery.](https://codeburst.io/easier-asynchronous-requests-with-jquery-80507b502e62)

### Bases de données dans les applications Node.js

MongoDB et CouchDB sont des systèmes de bases de données adaptés aux applications Node.js. Cela n'exclut pas complètement la possibilité d'utiliser d'autres bases de données. Nous allons examiner MongoDB, mais vous pouvez choisir celle que vous préférez.

Les documents remplacent les lignes dans une base de données relationnelle comme MySQL. Dans MongoDB et d'autres bases de données basées sur des documents, les données sont stockées et récupérées dans un format d'objet. Cela signifie que nous pouvons avoir des structures profondément imbriquées.

Si vous considérez les objets en JavaScript, il n'y a aucun moyen de valider que la valeur d'une propriété d'objet est d'un type particulier. Voici ce que je veux dire :

`const obj = { text : 1234}`

Il n'y a aucun moyen de s'assurer que la valeur de `text` est une chaîne.

Heureusement, il y a Mongoose. Mongoose vous permet de définir des schémas qui valident fortement les données et garantissent qu'elles correspondent aux objets ou documents dans une base de données MongoDB. Mongoose est un Object Document Mapper (ODM).

[Une introduction à Mongoose](https://code.tutsplus.com/articles/an-introduction-to-mongoose-for-mongodb-and-nodejs--cms-29527) est un bon point de départ pour explorer et travailler avec Mongoose.

### Sessions et Cookies dans Express

HTTP est sans état. Cela signifie que toute requête ou réponse envoyée par le navigateur ou le serveur respectivement ne conserve aucune information (état) sur les requêtes et réponses précédentes ou futures. Chaque requête individuelle contient tout ce qu'il faut pour provoquer une nouvelle réponse du serveur.

Mais il doit y avoir un moyen pour les serveurs de se souvenir des clients lorsqu'ils naviguent sur le site afin qu'ils n'aient pas à entrer des mots de passe sur chaque page.

Le web a été suffisamment innovant pour utiliser des cookies et des sessions. Les cookies sont essentiellement de petits fichiers stockés sur la machine du client. Lorsque les clients envoient des requêtes, le serveur les utilise pour les identifier. Un peu comme un passeport, le serveur sait alors que c'est eux et applique toutes leurs préférences.

L'idée serait donc de stocker des fichiers sur la machine du client. Bien que ce ne soit pas une mauvaise idée, nous voulons nous assurer de ne pas abuser du stockage de l'utilisateur en stockant d'énormes quantités de données. D'un autre côté, nous comprenons que si nous voulons rendre les choses plus difficiles à deviner et plus sécurisées, nous les rendons plus longues et plus complexes. Comment pouvons-nous atteindre ces deux objectifs simultanément ?

Les gens ont eu l'idée des sessions. L'idée des sessions est que, au lieu de stocker toutes les informations dans le cookie du client, le serveur stocke un identifiant dans le cookie (une petite chaîne). Lorsque le client envoie des requêtes, le serveur prend cette chaîne unique et la fait correspondre aux données de l'utilisateur sur le serveur. De cette façon, nous pouvons stocker n'importe quelle quantité de données et nous souvenir des utilisateurs.

Pour utiliser des cookies dans Express, nous devons importer le middleware `cookie-parser`. Vous vous souvenez de notre middleware ?

Je ne suis pas dans la meilleure position pour expliquer cela en profondeur. Mais quelqu'un l'a mieux fait ici : [Express sessions](https://glebbahmutov.com/blog/express-sessions/).

### Sécurité dans les applications Express

Le web n'est pas sécurisé par défaut. Les paquets sont la manière dont les données sont envoyées sur le web. Ces paquets ne sont pas chiffrés par défaut. Lorsque nous pensons à la sécurité web, le premier endroit où commencer est de sécuriser ces paquets.

**HTTPS** : Ce n'est pas un nouveau mot ! Comme vous l'avez peut-être deviné, la différence entre HTTP et HTTPS est le S (Sécurité). HTTPS chiffre les paquets voyageant à travers le web afin que les gens ne fassent pas de choses malveillantes avec.

#### Alors, comment obtenir HTTPS ?

Détendez-vous, prenons cela lentement. Pour obtenir HTTPS, vous devez approcher une Autorité de Certification (CA). HTTPS est basé sur le fait que le serveur possède un certificat de clé publique, parfois appelé SSL. Les CA attribuent des certificats aux serveurs qualifiés. Vous devez également comprendre que les CA créent des certificats racine qui sont installés lorsque vous installez votre navigateur. Ainsi, les navigateurs peuvent facilement communiquer avec les serveurs ayant également des certificats.

**Bonne nouvelle** : Tout le monde peut créer ses propres certificats.

**Mauvaise nouvelle** : Les navigateurs ne peuvent pas reconnaître ces certificats car ils n'ont pas été installés en tant que certificats racine.

**Impossible** : Vous ne pouvez pas configurer tous les navigateurs du monde lors de l'installation pour reconnaître votre certificat.

Je peux deviner ce que vous pensez maintenant. Vous pensez que vous pouvez créer votre propre certificat pour les tests et le développement et en obtenir un en production. Eh bien, c'est intelligent et possible.

Le navigateur vous donnera des avertissements, mais vous êtes conscient du problème, donc ce ne sera pas un gros problème. Voici un [article](https://deliciousbrains.com/https-locally-without-browser-privacy-errors/) qui vous guide à travers la création de votre propre certificat.

[**Comment configurer HTTPS localement sans obtenir d'ennuyeuses erreurs de confidentialité du navigateur**](https://deliciousbrains.com/https-locally-without-browser-privacy-errors/)  
[_Configurer HTTPS localement peut être une affaire délicate. Même si vous parvenez à maîtriser les certificats auto-signés dans_](https://deliciousbrains.com/https-locally-without-browser-privacy-errors/)  
[deliciousbrains.com](https://deliciousbrains.com/https-locally-without-browser-privacy-errors/)

Assez parlé. Supposons que vous avez maintenant le certificat SSL. Voici comment le faire fonctionner avec votre application Express.

#### Activer HTTPS dans votre application Node

Nous devons utiliser le module `https` pour HTTPS. Après avoir obtenu nos identifiants auprès d'une Autorité de Certification, nous les inclurons comme argument à la méthode `**createServer()**`.

```js
//server.js

const express = require('express'),
	  https = require('https'),
	  http = require('http'),
	  fs = require('fs'),
	  app = express();

//identifiants obtenus auprès d'une Autorité de Certification
var options = {
  key: fs.readFileSync('/path/to/key.pem'),
  cert: fs.readFileSync('/path/to/cert.pem')
};

//Lier l'application sur différents ports afin que l'application puisse être évaluée par HTTP et HTTPS
http.createServer(app).listen(80);
https.createServer(options, app).listen(443);
```

Remarquez que nous importons `http` et `https`. C'est parce que nous voulons répondre aux deux. Dans notre programme, nous utilisons le module `fs` (système de fichiers).

Nous fournissons essentiellement le chemin où notre clé SSL et notre certificat sont stockés. Un module ou autre chose. Observez que nous utilisons la méthode `**readFileSync**` au lieu de `**readFile**`. Si vous comprenez l'architecture de Node.js, vous déduirez que nous voulons lire le fichier de manière synchrone avant d'exécuter d'autres lignes de code.

L'exécution de ce code de manière asynchrone pourrait conduire à des situations où des aspects de notre code qui nécessitent le contenu du fichier ne les obtiennent pas à temps.

Les deux dernières lignes lient le HTTP et le HTTPS à deux ports différents et prennent des arguments différents. Pourquoi faisons-nous cela ?

La plupart du temps, nous voulons que notre serveur écoute toujours les requêtes avec HTTP et peut-être les redirige vers HTTPS.

**Note** : le port par défaut pour HTTPS est 443.

Pour faire cette redirection de base, nous allons installer et importer un module `express-force-ssl` en haut de notre programme comme suit :

```
npm install express-force-ssl
```

Et configurer comme suit :

```js
const express_force_ssl = require('express-force-ssl');
app.use(express_force_ssl);
```

Maintenant, notre serveur peut gérer à la fois les requêtes HTTP et HTTPS efficacement.

#### Cross-Site Request Forgery (CSRF)

C'est l'autre grande chose à laquelle vous voulez vous protéger. Cela se produit lorsque des requêtes arrivent sur votre serveur mais pas directement de votre utilisateur. Par exemple, vous avez une session active sur Facebook.com et vous avez un autre onglet ouvert. Des scripts malveillants peuvent s'exécuter sur l'autre site et faire des requêtes au serveur de Facebook.

Une façon de gérer cela est de s'assurer que les requêtes proviennent uniquement de votre site web. C'est assez simple. Nous attribuons un identifiant aux utilisateurs et l'attachons aux formulaires, afin que lorsqu'ils les soumettent, nous puissions faire correspondre l'identifiant et refuser l'accès s'il ne correspond pas.

Heureusement, il existe un middleware qui gère cela — le middleware `csurf`. Voici comment l'utiliser :

```
npm install csurf
```

Pour l'utiliser dans notre programme :

```js
const express = require('express'),
	  body_parser = require('body-parser'),
	  hbs = require('express-handlebars').create({defaultLayout: 'main',extname:'hbs'}),
	  session = require('express-session'),
	  csurf = require('csurf'),

	  app = express();

//définir le port de l'application
app.set('port', process.env.PORT || 3000);

//configurer l'application pour handlebars
app.engine('hbs', hbs.engine);
app.set('view engine', 'hbs');


//configurer une session csrf
app.use(session({
	name: 'Ma session csrf',
	secret: 'Mon super secret de session',
	  cookie: {
	  	maxAge: null,
	    httpOnly: true,
	    secure: true
	  }
	})
  );

app.use(csurf());

//configurer le middleware body parser
app.use(body_parser.urlencoded());

//Route pour se connecter
app.get('/login', (request,response)=>{
	console.log(request.csrfToken());
	response.render('login',{
		csrfToken : request.csrfToken(),
		title: 'Connexion'
	});
});

app.listen(3000,()=>console.log('Express app started at port 3000'));
```

```html
<b>Voici le jeton csrf généré</b> ({{csrfToken}})<br><br>

<form method='POST' action='/process'>
  <!--
Nous passons le jeton _csrf comme entrée cachée -->
  <input type='hidden' name='_csrf' csurf={{csrfToken}}/>
  <input type='text' name='name'/>
  <input type='submit'/>
</form>
```

Exécutez `node server.js`, allez dans votre navigateur `localhost:3000`, remplissez le formulaire et soumettez-le. Vérifiez également dans votre ligne de commande et voyez le jeton enregistré.

Ce que nous faisons, c'est générer et passer le `csrfToken` à notre vue de connexion.

**Note :** Le module `csurf` nécessite le module `express-session` pour fonctionner. Nous configurons notre session CSRF et la passons à la vue via la méthode `response.render()`.

Notre vue peut maintenant l'ajouter au formulaire ou à toute autre requête sensible.

Alors, que se passe-t-il lorsque le navigateur n'obtient pas le jeton CSRF des formulaires du navigateur ? Il génère une erreur. Assurez-vous d'avoir une route de gestion des erreurs dans votre application Express, sinon votre application pourrait mal se comporter.

#### Authentification

Une étape pour réduire les problèmes d'authentification est de permettre aux gens de s'inscrire et de se connecter avec des applications tierces (Facebook, Twitter, Google,+ et ainsi de suite). Beaucoup de gens ont ces comptes, et vous pouvez également avoir accès à certaines de leurs données comme les emails et les noms d'utilisateur. Des modules comme `passport.js` fournissent une interface très élégante pour gérer de telles authentifications.

Voici la [documentation officielle de passport.js](http://www.passportjs.org/docs/). Je pense que c'est un bon point de départ.

Une autre étape pour réduire les problèmes d'authentification est de toujours chiffrer tous les mots de passe et de les déchiffrer lorsqu'ils sont montrés aux utilisateurs.

Une dernière chose. Je vois cela sur beaucoup de sites web. Ils établissent des critères fous pour les mots de passe des utilisateurs sur le site. Je comprends qu'ils essaient de rendre les mots de passe plus sécurisés, mais réfléchissez-y. C'est le travail de qui ? Le développeur ou l'utilisateur ?

L'utilisateur devrait être le moins préoccupé par les problèmes de sécurité. Lorsque des critères comme ceux-ci sont établis pour les mots de passe, les utilisateurs n'ont pas d'autre choix que d'utiliser des mots de passe qu'ils n'oublieront jamais. Je sais que le web s'améliore et que nous trouverons un moyen de rendre l'authentification meilleure.

En attendant, je pense que nous pouvons terminer ici.

C'est beaucoup d'informations. Mais vous avez besoin de plus que cela pour construire des applications web scalables. Voici quelques livres instructifs pour en apprendre davantage sur Express.

Si cela a été utile, vous devriez me suivre sur [Twitter](https://twitter.com/vick_OnRails) pour plus de choses utiles.

1. [Express in action](https://www.amazon.com/Express-Action-Writing-building-applications/dp/1617292427) par [Evan Hahn](https://www.freecodecamp.org/news/getting-off-the-ground-with-expressjs-89ada7ef4e59/undefined).
2. [Getting MEAN with Express, Mongo, Angular and Node](https://www.amazon.com/Getting-MEAN-Mongo-Express-Angular/dp/1617294756) par [Simon Holmes](https://www.freecodecamp.org/news/getting-off-the-ground-with-expressjs-89ada7ef4e59/undefined).