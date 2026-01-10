---
title: Comment créer un générateur de personnages de RPG Full Stack avec MongoDB,
  Express, Vue et Node (la pile MEVN)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-09T18:50:41.000Z'
originalURL: https://freecodecamp.org/news/build-a-full-stack-mevn-app
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c3a740569d1a4ca30ca.jpg
tags:
- name: api
  slug: api
- name: 'Back end development '
  slug: back-end-development
- name: Express
  slug: express
- name: Express.js
  slug: expressjs
- name: Front-end Development
  slug: front-end-development
- name: full stack
  slug: full-stack
- name: mongoose
  slug: mongoose
- name: node
  slug: node
- name: Node.js
  slug: nodejs
- name: REST
  slug: rest
- name: REST API
  slug: rest-api
- name: vue
  slug: vue
seo_title: Comment créer un générateur de personnages de RPG Full Stack avec MongoDB,
  Express, Vue et Node (la pile MEVN)
seo_desc: 'By M. S. Farzan

  I''m a tabletop game developer, and enjoy making apps that have the potential to
  perform some service related to gaming. In this article, we''ll walk through the
  steps to create a roleplaying game character generator using MongoDB, Expr...'
---

Par M. S. Farzan

Je suis un développeur de [jeux de table](https://www.nightpathpub.com/) et j'aime créer des applications qui peuvent offrir des services liés aux jeux. Dans cet article, nous allons passer en revue les étapes pour créer un générateur de personnages de jeu de rôle en utilisant [MongoDB](https://www.mongodb.com/), [Express](https://expressjs.com/), [Vue](http://vuejs.org/), et [Node](https://nodejs.org/en/) (également connu sous le nom de pile "MEVN"). 

Prérequis : ce tutoriel suppose que vous avez Node/[NPM](https://www.npmjs.com/) et MongoDB installés et configurés, avec un éditeur de code et un [CLI](https://en.wikipedia.org/wiki/Command-line_interface) (ou [IDE](https://www.freecodecamp.org/news/how-to-set-up-an-integrated-development-environment-ide/)) prêt à l'emploi.

Si vous préférez suivre un tutoriel visuel, vous pouvez consulter la vidéo compagnon de cet article ci-dessous :

%[https://youtu.be/i5XUgda08qk]

Je devrais également mentionner que ce tutoriel n'aurait pas été possible sans l'article de Bennett Dungan sur [la création d'une API REST](https://dev.to/beznet/build-a-rest-api-with-node-express-mongodb-4ho4), le tutoriel d'Aneeta Sharma sur [les applications web MEVN full stack](https://medium.com/@anaida07/mevn-stack-application-part-1-3a27b61dcae0), et l'article de Matt Maribojoc sur [le même sujet](https://medium.com/@mattmaribojoc/creating-a-todo-app-with-a-mevn-full-stack-part-1-da0f4df7e15).  

J'ai utilisé chacun de ces articles en plus de la documentation officielle (pour [Vue](https://vuejs.org/v2/guide/), [Express](https://expressjs.com/en/starter/installing.html), et bien plus encore) pour apprendre à créer mes propres applications MEVN (vous pouvez en savoir plus sur mon parcours avec les API web [ici](https://www.freecodecamp.org/news/i-built-a-web-api-with-express-flask-aspnet/)). 

Vous pouvez accéder à l'ensemble du dépôt pour ce tutoriel sur [GitHub](https://github.com/sominator/mevn-character-generator).

## Le Front End

Notre application va nous permettre de créer de nouveaux personnages de jeu de rôle et de les visualiser ensemble, avec la pile suivante :

<ul>
    <li>Client Vue</li>
    <li>Serveur Node/Express</li>
    <li>Base de données MongoDB</li>
</ul>

Le client Vue effectuera des [requêtes HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) vers le serveur Node/Express (ou "[API](https://en.wikipedia.org/wiki/Application_programming_interface)"), qui communiquera à son tour avec notre base de données MongoDB pour envoyer les données vers le haut de la pile.

Nous allons commencer par ouvrir une ligne de commande, créer un nouveau répertoire pour notre projet et naviguer dans ce répertoire :

```cli
mkdir mevn-character-generator
cd mevn-character-generator
```

Nous allons ensuite installer le [Vue CLI](https://cli.vuejs.org/) globalement pour nous aider à échafauder une application de base : 

```cli
npm install -g @vue/cli
```

Ensuite, nous allons utiliser le Vue CLI pour créer une nouvelle application appelée "Client" dans notre répertoire mevn-character-generator :

```cli
vue create client
```

Vous pouvez simplement appuyer sur "entrée" à l'invite pour continuer.

Nous pouvons exécuter notre application en naviguant d'abord dans le dossier /client :

```cli
cd client
npm run serve
```

Lorsque le script a terminé son exécution, nous pouvons maintenant ouvrir une page de navigateur et naviguer vers l'URL indiquée par notre terminal (généralement http://localhost:8080 ou 8081). Nous devrions voir quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Vue-Template.PNG)

Super ! Le Vue CLI a échafaudé une application de base pour nous et la rend directement dans le navigateur. Il rechargera également la page automatiquement en cas de modifications de fichiers et affichera des erreurs si quelque chose dans le code semble incorrect.

Ouvrons le répertoire du projet dans notre éditeur de code pour examiner la structure des fichiers, qui devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Client-Directory.PNG)

Si vous êtes OCD comme moi, vous pouvez supprimer le fichier "favicon.ico" et le dossier "/assets" car nous n'en aurons pas besoin pour ce projet.

En plongeant dans /src/main.js, nous voyons :

```javascript
import Vue from 'vue'
import App from './App.vue'

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')

```

Ce fichier est le point d'entrée principal pour notre client. Il indique au navigateur de monter notre fichier App.vue sur la div avec l'id "#app" dans /public/index.html.

Regardons /src/App.vue (j'ai omis une partie du code pour plus de lisibilité) :

```javascript
<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  }
}
</script>

<style>
#app {
...
}
</style>
```

App.vue est un composant Vue typique, avec des balises <template>, <script> et <style>.

La section entre les balises <template> est le HTML que nous voyons rendu à l'écran. À l'intérieur, nous voyons une référence à l'image que nous avons supprimée, et un composant <HelloWorld/> qui reçoit le message "Welcome to Your Vue.js App."

La section <script> importe d'autres composants qui sont utilisés, et exporte les données que nous voulons inclure dans notre application. Notez que dans App.vue, nous importons HelloWorld.vue depuis un autre répertoire, et l'exportons en tant que composant afin que notre main.js puisse y avoir accès.

Les balises <style> sont pour votre propre CSS brillant et vibrant, que nous n'utiliserons pas pour ce tutoriel (womp womp).

Suivons le fil vers /src/components/HelloWorld.vue :

```javascript
<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
...
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<!-- Ajoutez l'attribut "scoped" pour limiter le CSS à ce composant uniquement -->
<style scoped>
...
</style>
```

HelloWorld.vue suit une structure de composant similaire à App.vue. Il s'attend à recevoir les [props](https://vuejs.org/v2/guide/components-props.html) "msg" en tant que String depuis le composant parent qui l'appelle (qui est dans ce cas App.vue). HelloWorld.vue sert ensuite le message directement dans le modèle HTML entre les accolades sous la forme {{msg}}.

Il est également important de noter que les balises <style> ici (que nous n'utilisons toujours pas) sont limitées, ce qui signifie que si vous souhaitez appliquer du CSS à ce composant seul, vous pouvez le faire.

Supprimons tout le HTML dans HelloWorld.vue et changeons le nom du fichier en "CharacterViewer.vue." Mettez à jour le code comme suit :

```javascript
<template>
    <div class="character-viewer">
        <h1>Character Viewer</h1>
    </div>
</template>

<script>
    export default {
        name: 'CharacterViewer'
    }
</script>

<style scoped>

</style>
```

C'est beaucoup plus simple, mais cela nécessite de changer toutes les références à "HelloWorld" dans App.vue :

```javascript
<template>
  <div id="app">
    <CharacterViewer />
  </div>
</template>

<script>
import CharacterViewer from './components/CharacterViewer.vue'

export default {
  name: 'App',
  components: {
    CharacterViewer
  }
}
</script>
```

Le Vue CLI, qui a peut-être été en train de vous envoyer des erreurs pendant que vous supprimiez et réorganisiez des éléments, devrait se recharger. Si vous consultez à nouveau votre navigateur, vous verrez :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Base-App.PNG)

Assez excitant. Ajoutons un composant "Character Creator" en dupliquant CharacterViewer.vue et en l'appelant "CharacterCreator.vue", en remplaçant le code :

```javascript
<template>
    <div class="character-creator">
        <h1>Character Creator</h1>
    </div>
</template>

<script>
    export default {
        name: 'CharacterCreator'
    }
</script>

<style scoped>

</style>
```

Puis référençons notre nouveau composant dans App.vue :

```
<template>
    <div id="app">
        <CharacterViewer />
        <CharacterCreator />
    </div>
</template>

<script>
    import CharacterViewer from './components/CharacterViewer.vue'
    import CharacterCreator from './components/CharacterCreator.vue'

    export default {
        name: 'App',
        components: {
            CharacterViewer,
            CharacterCreator
        }
    }
</script>
```

Cool. Maintenant, le site devrait nous montrer :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Base-App-2.PNG)

C'est super, mais disons que nous voulons visualiser dynamiquement chacun des composants indépendamment les uns des autres. Nous pourrions utiliser des menus radiaux comme sélecteurs qui guideront la logique de notre application, mais je préfère utiliser des boutons lors de la création d'une interface utilisateur.

Ajoutons-en quelques-uns :

```javascript
<template>
    <div id="app">
        <button v-on:click="toggle='character-viewer'">View all characters</button>
        <button v-on:click="toggle='character-creator'">Create a character</button>
        <CharacterViewer v-show="toggle==='character-viewer'" />
        <CharacterCreator v-show="toggle==='character-creator'" />
    </div>
</template>

<script>
    import CharacterViewer from './components/CharacterViewer.vue'
    import CharacterCreator from './components/CharacterCreator.vue'

    export default {
        name: 'App',
        components: {
            CharacterViewer,
            CharacterCreator
        },
        data: function () {
            return {
                toggle: "character-viewer"
            }
        }
    }
</script>
```

Pour comprendre le code ci-dessus, travaillons de bas en haut du script. 

Nous avons ajouté une fonction "data" à la section d'exportation de notre application, qui retourne un objet pouvant stocker des données pour nous. Ces données peuvent à leur tour nous aider à gérer l'[état](https://vuejs.org/v2/guide/components.html) de l'application. Dans ce code, nous avons créé un "toggle" qui est défini sur "character-viewer."

Dans le modèle HTML au-dessus du script, nous avons créé deux boutons : l'un pour "View all characters" et l'autre pour "Create a character." L'attribut "v-on:click" dans les balises <button> indique à Vue que lorsqu'on clique dessus, Vue doit changer la valeur de "toggle" en "character-viewer" ou "character-creator," selon le bouton sur lequel on clique.

Juste en dessous des boutons, les directives "v-show" instruisent Vue de n'afficher le composant "CharacterViewer" que si "toggle" est égal à "character-viewer", ou le composant "CharacterCreator" s'il est égal à "character-creator." 

Félicitations, notre application affiche maintenant du contenu de manière dynamique en fonction des entrées de l'utilisateur !

Maintenant, nous pouvons passer à la création de la structure de base pour visualiser et créer des personnages de jeu de rôle. Dans CharacterCreator.vue, mettez à jour le code :

```javascript
<template>
    <div class="character-creator">
        <h1>Character Creator</h1>
        <label for="character-name">Character Name: </label>
        <input type="text" id="character-name" v-model="name" placeholder="Enter a name" /> <br /><br />
        <label for="professions-list">Character Profession: </label>
        <select id="professions-list" v-model="profession">
            <option value="Mage">Mage</option>
            <option value="Thief">Thief</option>
            <option value="Warrior">Warrior</option>
        </select>
        <p>{{name}}</p>
        <p>{{profession}}</p>
    </div>
</template>

<script>
    export default {
        name: 'CharacterCreator',
        data: function () {
            return {
                name: "",
                profession: ""
            }
        }
    }
</script>
```

Nous venons de créer une entrée de texte où les joueurs peuvent saisir un nom de personnage, et une simple liste déroulante à partir de laquelle ils peuvent choisir une profession.  

L'attribut "v-model" lie chacune de ces entrées aux valeurs "name" et "profession" dans notre objet de données dans le script.  

Nous avons également temporairement ajouté un {{name}} et {{profession}} dans le modèle HTML afin de pouvoir nous assurer que tout fonctionne correctement. Après avoir enregistré, le Vue CLI devrait automatiquement réafficher l'application pour qu'elle ressemble à ceci lorsque vous cliquez sur "Create a character" :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Character-Creator.PNG)

Ce n'est certainement pas joli, mais ça marche ! Je vous laisse le design à vos compétences folles en CSS.

## Le Back End

Passons au back end. Ouvrez une nouvelle ligne de commande et naviguez jusqu'au répertoire racine (mevn-character-generator). Créez un nouveau répertoire pour notre serveur et naviguez dedans :

```cli
mkdir server
cd server
```

Maintenant, initialisez le répertoire :

```
npm init
```

Vous pouvez simplement continuer à appuyer sur "entrée" aux invites si vous ne souhaitez pas changer les détails.

Ensuite, installez nos dépendances et enregistrez-les dans le projet :

```
npm install --save express dotenv nodemon mongoose cors
```

Prenons un moment pour examiner chacun de ces éléments à tour de rôle. [Express](https://expressjs.com/) va servir de framework web principal pour le back end, tandis que [dotenv](https://www.npmjs.com/package/dotenv) nous permet de déclarer certaines [variables d'environnement](https://en.wikipedia.org/wiki/Environment_variable) qui nous aideront avec le cheminement et la configuration. [Nodemon](https://nodemon.io/) surveille automatiquement notre serveur pour les changements et le redémarre pour nous, et [Mongoose](https://mongoosejs.com/) sert de [ODM](https://en.wikipedia.org/wiki/Object-relational_mapping#Object-oriented_databases) pour mapper nos données sur MongoDB. Enfin, [CORS](https://expressjs.com/en/resources/middleware/cors.html) nous permet de faire des [requêtes cross-origin](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) entre notre client et notre serveur, un sujet dont j'ai parlé [ici](https://www.freecodecamp.org/news/i-built-a-web-api-with-express-flask-aspnet/).

C'est beaucoup de dépendances ! Dans notre éditeur de code, nous devons créer quelques fichiers et répertoires pour échafauder un serveur avec lequel travailler. Dans notre nouveau répertoire /server, créez quatre fichiers appelés "server.js", ".env", "characters.js", et "character.js" :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Server-Directory.PNG)

Remplacez le script "test" dans notre package.json par le script "dev" ci-dessous :

```json
{
  "name": "server",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "dependencies": {
    "cors": "^2.8.5",
    "dotenv": "^8.2.0",
    "express": "^4.17.1",
    "mongoose": "^5.9.3",
    "nodemon": "^2.0.2"
  },
  "devDependencies": {},
  "scripts": {
    "dev": "nodemon server.js"
  },
  "author": "",
  "license": "ISC"
}

```

Maintenant, lorsque nous tapons "npm run dev" dans la ligne de commande, il exécutera Nodemon avec server.js comme point d'entrée pour le back end de notre application.

Nous allons créer notre serveur en ajoutant le code suivant à server.js :

```javascript
require('dotenv').config();
const express = require('express');
const server = express();
const cors = require('cors');

server.use(express.json());
server.use(cors());

server.get("/", (req, res) => {
    res.send("Hello World!");
})

server.listen(3000, () => console.log("Server started!"));
```

Nous faisons beaucoup de choses ici dès le départ, mais nous nous remercierons plus tard. Tout d'abord, nous importons les variables d'environnement dont nous aurons besoin pour exécuter notre serveur de développement, ainsi qu'Express et CORS. Nous créons un serveur qui s'exécute sur Express et qui est capable d'analyser JSON et d'utiliser CORS.  

Ensuite, nous disons au serveur que lorsqu'un utilisateur navigue vers le répertoire racine ("/") dans un navigateur, il doit envoyer le message "Hello World!"  

Enfin, nous disons au serveur d'écouter sur le port 3000, et de journaliser dans la console que le "Server started!"

Tapez ce qui suit dans une ligne de commande _séparée_ de celle qui exécute notre application Vue, en vous assurant d'être dans le répertoire /server :

```cli
npm run dev
```

Ouvrez un navigateur à l'adresse http://localhost:3000. Vous devriez voir :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Hello-World.PNG)

Super !

Maintenant que le serveur est en marche, nous devons faire fonctionner notre base de données. Ouvrez une _troisième_ ligne de commande et tapez ce qui suit :

```cli
mongod
```

Cela _devrait_ faire fonctionner notre base de données, mais cela dépendra de la manière dont vous avez installé et configuré MongoDB avant de vous attaquer à ce tutoriel. Dans certains cas, vous devrez travailler avec le [chemin](https://docs.mongodb.com/guides/server/install/) de votre base de données et de MongoDB lui-même pour que tout soit correct.

Une fois que la commande "mongod" fonctionne, ajoutez la ligne suivante à votre fichier .env :

```javascript
DATABASE_URL = mongodb://localhost/characters
```

Nous allons utiliser ce qui précède dans un instant pour connecter notre base de données. Ajoutez le code suivant à votre fichier server.js, juste sous la ligne concernant l'importation de CORS :

```javascript
const mongoose = require('mongoose');
mongoose.connect(process.env.DATABASE_URL, { useNewUrlParser: true });
const db = mongoose.connection;
db.on('error', (error) => console.error(error));
db.once('open', () => console.log('Connected to database!'));
```

Ici, nous importons Mongoose dans notre serveur et le connectons à l'URL de la base de données que nous avons déclarée dans le fichier .env.  

Cette connexion est assignée à la variable "db" pour une référence facile, et s'il y a une erreur, nous avons demandé au serveur de la journaliser dans la console. Sinon, si tout fonctionne correctement, la console devrait journaliser que nous sommes "Connectés à la base de données !"

Enregistrez tous vos fichiers, permettant à Nodemon de redémarrer le serveur avec les messages CLI que le "Serveur démarré !" et que vous êtes "Connecté à la base de données !"

Maintenant que tout est connecté côté back end, nous devrons ajouter un "schéma" Mongoose, qui est un modèle de ce à quoi nos données devraient ressembler. Ajoutez ce qui suit à character.js :

```javascript
const mongoose = require('mongoose');

const characterSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true
    },
    profession: {
        type: String,
        required: true
    }
});

module.exports = mongoose.model('Character', characterSchema);
```

Après avoir importé Mongoose, nous avons ajouté un nouveau schéma qui mappe le nom et la profession du personnage que nous avons créés dans notre client front end aux champs requis dans la base de données back end. Les deux sont de type "String", et sont requis lors de l'envoi à la base de données.

Nous devons dire au serveur comment accéder à la base de données et quoi faire une fois qu'il y est, mais cela deviendra désordonné si nous essayons d'ajouter tout ce code à server.js. Supprimons le bloc de code qui commence par "server.get..." et remplaçons-le par :

```javascript
const router = require('./characters');
server.use('/characters', router);
```

Ce snippet dit simplement au serveur : "quand quelqu'un va à l'[endpoint HTTP](https://en.wikipedia.org/wiki/Web_API#Endpoints) /characters, fais ce qui est dans le fichier characters.js."

Votre fichier server.js complet devrait maintenant ressembler à ce qui suit :

```javascript
require('dotenv').config();
const express = require('express');
const server = express();
const cors = require('cors');

const mongoose = require('mongoose');
mongoose.connect(process.env.DATABASE_URL, { useNewUrlParser: true });
const db = mongoose.connection;
db.on('error', (error) => console.error(error));
db.once('open', () => console.log('Connected to database!'));

server.use(express.json());
server.use(cors());

const router = require('./characters');
server.use('/characters', router);

server.listen(3000, () => console.log("Server started!"));
```

Remarque : il est considéré comme une bonne pratique de garder vos modèles et routes dans des dossiers "/models" et "/routes", respectivement, mais nous avons simplifié les chemins pour ce tutoriel.

Mettons ce fichier characters.js en marche. Commencez par entrer ce qui suit :

```javascript
const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
    res.send("Hello World!")
});

module.exports = router;
```

Si nous naviguons vers http://localhost:3000/characters, nous obtenons le message "Hello World!" que nous avons vu précédemment. Pas trop mal – nous avons réussi à migrer notre code vers un fichier séparé pour garder les choses un peu plus ordonnées.

Ajouter un peu plus à characters.js nous aidera à remplir le reste de notre API back end, mais faisons une pause pour considérer ce que nous essayons de faire.

Dans ce projet, nous voulons pouvoir faire des requêtes GET et POST depuis le client vers le serveur, qui à son tour "Lira" et "Créera" des éléments dans la base de données (représentant le "R" et le "C" dans "[CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete)"). Nous commencerons par la méthode GET car nous avons déjà une structure pour celle-ci : 

```javascript
const express = require('express');
const router = express.Router();
const Character = require('./Character');

router.get('/', async (req, res) => {
    try {
        const characters = await Character.find();
        res.json(characters);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

module.exports = router;
```

Nous créons une [fonction asynchrone](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function) qui, lorsqu'elle reçoit une requête, tente de trouver tous les personnages dans notre base de données qui correspondent à notre schéma Mongoose. Elle les envoie ensuite tous en réponse JSON. Si quelque chose ne va pas, elle envoie plutôt une [erreur 500](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500).

Le rechargement de la page que nous avons ouverte sur http://localhost:3000/characters retournera un "[]" excitant, mais c'est génial ! Cela signifie simplement que la requête GET retourne un tableau vide car la base de données est vide. Bon travail !

## Connecter le Front End et le Back End

Retour à notre client ! Dans une ligne de commande au répertoire mevn-character-generator/client, installez [Axios](https://www.npmjs.com/package/axios) :

```
npm install --save axios
```

Axios nous permet de faire des requêtes HTTP depuis notre client. Si vous êtes intéressé, vous pouvez en savoir plus sur son fonctionnement avec Vue [ici](https://vuejs.org/v2/cookbook/using-axios-to-consume-apis.html).

Dans notre fichier /client/src/components/CharacterViewer.vue, nous devons faire des requêtes GET au serveur afin de pouvoir récupérer les personnages de la base de données, et nous le ferons en utilisant Axios :

```javascript
<template>
    <div class="character-viewer">
        <h1>Character Viewer</h1>
        <p>{{characters}}</p>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: 'CharacterViewer',
        data: function () {
            return {
                characters: null
            }
        },
        methods: {
            getCharacters: function () {
                axios
                    .get('http://localhost:3000/characters')
                    .then(response => (this.characters = response.data))
            }
        },
        mounted: function () {
            this.getCharacters();
        }
    }
</script>

<style scoped>
</style>

```

Dans la section script, nous avons créé une variable de données appelée "characters", qui commence par "null."  

Dans notre objet "methods", qui est l'endroit où Vue stocke les fonctions que vous pouvez utiliser dans tout votre composant, nous avons créé une fonction "getCharacters()". "getCharacters()" appellera Axios pour obtenir l'endpoint http://localhost:3000/characters et stocker les données de sa réponse dans la variable "characters".  

Lorsque le composant est monté pour la première fois, il exécutera "getCharacters()" pour obtenir tous les personnages de la base de données et les afficher dans la section template HTML ci-dessus.

Nous ne verrons toujours rien d'excitant sur notre page client (toujours en cours de rendu sur http://localhost:8080 ou 8081) car nous n'avons pas encore ajouté de personnages à la base de données. 

Astuce pro ! Si vous êtes nerveux à propos de cette étape et que vous n'êtes pas sûr que les choses fonctionnent correctement, vous pouvez utiliser une application tierce comme [Postman](https://www.postman.com/) pour faire des requêtes HTTP à une API sans avoir à d'abord connecter votre client.

Sautons à notre routeur /server/characters.js et ajoutons la logique pour une requête POST :

```javascript
const express = require('express');
const router = express.Router();
const Character = require('./Character');

router.get('/', async (req, res) => {
    try {
        const characters = await Character.find();
        res.json(characters);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

router.post('/', async (req, res) => {
    const character = new Character({
        name: req.body.name,
        profession: req.body.profession
    });
    try {
        const newCharacter = await character.save();
        res.status(201).json(newCharacter);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

module.exports = router;
```

Sous la requête GET, nous avons ajouté une fonction POST asynchrone qui crée un "character", qui est une nouvelle copie du schéma Mongoose Character.js. La requête qui arrive au serveur doit inclure un "name" et un "profession" dans le corps, qui doivent être enregistrés dans la base de données en tant que "newCharacter" et renvoyés en tant que réponse JSON avec un [succès 201](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/201).

S'il y a une erreur, le serveur doit l'envoyer en amont avec un statut de [400](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/400).

De manière folle, ce code est tout ce dont nous avons besoin pour terminer le back end de notre application. Si nous allons dans notre fichier /client/src/components/CharacterCreator.vue, nous pouvons tout rassembler :

```javascript
<template>
    <div class="character-creator">
        <h1>Character Creator</h1>
        <label for="character-name">Character Name: </label>
        <input type="text" id="character-name" v-model="name" placeholder="Enter a name" /> <br /><br />
        <label for="professions-list">Character Profession: </label>
        <select id="professions-list" v-model="profession">
            <option value="Mage">Mage</option>
            <option value="Thief">Thief</option>
            <option value="Warrior">Warrior</option>
        </select><br /><br />
        <button v-on:click="postCharacter">Create Character</button>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        name: 'CharacterCreator',
        data: function () {
            return {
                name: null,
                profession: null
            }
        },
        methods: {
            postCharacter: function () {
                axios
                    .post('http://localhost:3000/characters', {
                        name: this.name,
                        profession: this.profession
                    });
            }
        }
    }
</script>
```

Nous avons ajouté une fonction "postCharacter()" au composant CharacterCreator.vue, qui enverra une requête POST à l'endpoint http://localhost:3000/characters avec un "name" et un "profession" dans le corps.

Le "name" et le "profession" sont tirés des variables de notre objet de données, qui sont elles-mêmes liées aux entrées que nous avons créées précédemment par l'attribut "v-model".

Nous avons ajouté un bouton "Create Character" qui appelle la fonction "postCharacter()" lorsqu'il est cliqué. Lorsque nous faisons une requête POST en utilisant le créateur de personnages, nous pouvons maintenant faire ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/POST-Request.PNG)

Et notre requête GET ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/GET-Request.PNG)

ÇA MARCHE. Mais nous devons nettoyer notre requête GET pour qu'elle soit plus lisible, surtout lorsque de nouveaux utilisateurs sont ajoutés. Voici ce que nous allons ajouter à la partie <template> de CharacterViewer.vue :

```html
<template>
    <div class="character-viewer">
        <h1>Character Viewer</h1>
        <p v-for="(character, index) in characters" v-bind:key="index">{{character.name}} is a {{character.profession}}!</p>
        <button v-on:click="getCharacters">Refresh Characters</button>
    </div>
</template>
```

Ici, nous utilisons "v-for" pour demander à Vue d'itérer sur chacun des personnages dans les données de réponse (actuellement stockées dans la variable "characters") et d'afficher leurs noms et professions.

Le Vue CLI se mettra en colère si vous ne fournissez pas une clé unique pour chacun des éléments itérés, nous utilisons donc "v-bind" pour créer une clé basée sur l'index de l'élément.

Nous avons également ajouté un bouton "Refresh Characters" qui appellera la fonction "getCharacters()" afin que nous puissions voir les nouveaux personnages au fur et à mesure qu'ils sont ajoutés sans avoir à rafraîchir la page. 

Le Character Viewer est beaucoup plus propre :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/GET-Request-Filtered-1.PNG)

Et avec cela, notre application est entièrement fonctionnelle !  Bon travail !

...

...

Mais que faire si nous voulons éliminer ce bouton "Refresh Characters" et simplement avoir tous les personnages chargés chaque fois que nous naviguons vers la section Character Viewer de l'application ?

Tout d'abord, nous devrons apporter ces modifications à App.vue :

```javascript
<template>
    <div id="app">
        <button v-on:click="toggle='character-viewer'; getCharacters()">View all characters</button>
        <button v-on:click="toggle='character-creator'">Create a character</button>
        <CharacterViewer v-show="toggle==='character-viewer'" :characters="characters"/>
        <CharacterCreator v-show="toggle==='character-creator'" />
    </div>
</template>

<script>
    import CharacterViewer from './components/CharacterViewer.vue'
    import CharacterCreator from './components/CharacterCreator.vue'
    import axios from "axios"

    export default {
        name: 'App',
        components: {
            CharacterViewer,
            CharacterCreator
        },
        data: function () {
            return {
                toggle: "character-viewer",
                characters: null
            }
        },
        methods: {
            getCharacters: function () {
                axios
                    .get('http://localhost:3000/characters')
                    .then(response => (this.characters = response.data))
            }
        },
        mounted: function () {
            this.getCharacters();
        }
    }
</script>
```

Nous avons migré la fonctionnalité "getCharacters()" vers App.vue et l'appelons maintenant lorsque l'application est montée, ainsi que chaque fois que nous cliquons sur le bouton "View all characters". Nous passons également la variable "characters" - qui stocke nos données de réponse de l'API serveur - en tant que props au composant "CharacterViewer" dans la section <template>.

Il ne reste plus qu'à nettoyer CharacterViewer.vue et à indiquer qu'il doit s'attendre à un tableau appelé "characters" en tant que props :

```javascript
<template>
    <div class="character-viewer">
        <h1>Character Viewer</h1>
        <p v-for="(character, index) in characters" v-bind:key="index">{{character.name}} is a {{character.profession}}!</p>
    </div>
</template>

<script>
    export default {
        name: 'CharacterViewer',
        props: {
            characters: Array
        }
    }
</script>
```

NOUS L'AVONS FAIT.  

Nous avons créé un générateur de personnages de jeu de rôle entièrement fonctionnel. Son client Vue répond dynamiquement aux entrées de l'utilisateur et peut faire des requêtes GET et POST à une API de serveur Node/Express, qui à son tour lit et écrit dans une base de données MongoDB.

Bien joué. Vous pouvez utiliser ce projet comme modèle pour vos propres applications full stack MEVN, ou travailler avec le HTML et le CSS pour le rendre plus riche en fonctionnalités et plus convivial.

Une étape amusante suivante serait de rechercher les [API RESTful](https://restfulapi.net/) plus en profondeur et d'ajouter des requêtes PATCH et DELETE afin de pouvoir mettre à jour ou supprimer des personnages si nécessaire. Un bon point de départ serait la [documentation Express](https://expressjs.com/en/guide/routing.html), ou l'article de Bennett Dungan sur [la création d'une API REST](https://dev.to/beznet/build-a-rest-api-with-node-express-mongodb-4ho4).

Vous pouvez également apprendre à déployer ce type d'application sur Heroku [ici](https://www.freecodecamp.org/news/how-to-deploy-a-full-stack-web-app-with-heroku/).

Bon codage !

Si vous avez aimé cet article, envisagez de [découvrir mes jeux et livres](https://www.nightpathpub.com/), de [vous abonner à ma chaîne YouTube](https://www.youtube.com/msfarzan?sub_confirmation=1), ou de [rejoindre le Discord _Entromancy_](https://discord.gg/RF6k3nB).

M. S. Farzan, Ph.D. a écrit et travaillé pour des entreprises de jeux vidéo et des sites éditoriaux de haut profil tels qu'Electronic Arts, Perfect World Entertainment, Modus Games et MMORPG.com, et a servi en tant que Community Manager pour des jeux comme _Dungeons & Dragons Neverwinter_ et _Mass Effect: Andromeda_. Il est le Directeur Créatif et le Game Designer Principal de _[Entromancy: A Cyberpunk Fantasy RPG](https://www.nightpathpub.com/rpg)_ et l'auteur de _[The Nightpath Trilogy](http://nightpathpub.com/books)_. Retrouvez M. S. Farzan sur Twitter [@sominator](https://twitter.com/sominator).