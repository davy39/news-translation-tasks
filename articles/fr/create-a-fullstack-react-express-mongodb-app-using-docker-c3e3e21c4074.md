---
title: Comment créer une application Full Stack React/Express/MongoDB en utilisant
  Docker
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-15T07:01:02.000Z'
originalURL: https://freecodecamp.org/news/create-a-fullstack-react-express-mongodb-app-using-docker-c3e3e21c4074
coverImage: https://cdn-media-1.freecodecamp.org/images/0*dpm3hLvU_dmwP-8U
tags:
- name: Docker
  slug: docker
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Comment créer une application Full Stack React/Express/MongoDB en utilisant
  Docker
seo_desc: 'By João Henrique

  In this tutorial, I will guide you through the process of containerizing a React
  FrontEnd, a Node/Express API, and a MongoDB database using Docker containers in
  a very simple way.


  I won’t go into much detail about how to work with a...'
---

Par João Henrique

**Dans ce tutoriel, je vais vous guider à travers le processus de conteneurisation d'un FrontEnd [React](https://reactjs.org/), d'une API [Node](https://nodejs.org/en/)/[Express](http://expressjs.com/) et d'une base de données [MongoDB](https://www.mongodb.com/what-is-mongodb) en utilisant des conteneurs [Docker](https://www.docker.com/) de manière très simple.**

> Je ne vais pas entrer dans les détails de l'utilisation de ces technologies. À la place, je vais laisser des liens, au cas où vous souhaiteriez en apprendre davantage sur l'une d'entre elles.

> L'objectif est de vous donner un guide pratique pour conteneuriser cette application Full-Stack simple, à utiliser comme point de départ pour construire vos propres applications.

#### Pourquoi devriez-vous vous intéresser à [Docker](https://www.docker.com/) ?

Docker est simplement l'une des technologies les plus importantes du moment. Il vous permet d'exécuter des applications à l'intérieur de conteneurs qui sont principalement isolés de « tout ».

Chaque conteneur est comme une machine virtuelle individuelle dépouillée de tout ce qui n'est pas nécessaire pour exécuter votre application. Cela rend les conteneurs très légers, rapides et sécurisés.

Les conteneurs sont également conçus pour être jetables. Si l'un d'eux devient incontrôlable, vous pouvez le supprimer et en créer un autre identique sans effort grâce au [système d'images de conteneurs](https://docs.docker.com/engine/reference/commandline/images/).

Une autre chose qui rend [Docker](https://www.docker.com/) génial est que l'application à l'intérieur des conteneurs s'exécutera de la même manière sur tous les systèmes (Windows, Mac ou Linux). C'est génial si vous développez sur votre machine et que vous souhaitez ensuite la déployer sur un fournisseur de cloud comme [GCP](https://cloud.google.com/kubernetes-engine/docs/) ou [AWS](https://aws.amazon.com/pt/).

#### Prêt à commencer !

1. Assurez-vous d'avoir [Node](https://nodejs.org/en/) et [Docker](https://www.docker.com/get-started) en cours d'exécution sur votre machine.
2. Je vais utiliser l'application React/Express que nous avons construite dans le tutoriel précédent intitulé [**Créer un FrontEnd React, un BackEnd Node/Express et les connecter ensemble**](https://medium.com/@jrshenrique/create-a-react-frontend-a-node-express-backend-and-connect-them-together-c5798926047c). Vous pouvez suivre ce tutoriel d'abord ou vous pouvez [cloner](https://help.github.com/articles/cloning-a-repository/) ce [**dépôt GitHub**](https://github.com/Joao-Henrique/React_Express_App_Medium_Tutorial) avec le code de base si vous n'êtes pas intéressé par le processus de création des applications [React](https://reactjs.org/) et [Express](http://expressjs.com/).
3. Si vous optez pour l'utilisation du dépôt, n'oubliez pas de faire **npm install** dans les dossiers **Client** et **API** pour installer toutes les dépendances nécessaires.
4. Et... c'est à peu près tout. Vous êtes prêt à commencer à conteneuriser des choses :)

#### Dockerfile

Selon la documentation :

> _un [Dockerfile](https://docs.docker.com/engine/reference/builder/#usage) est un document texte qui contient toutes les commandes qu'un utilisateur pourrait appeler sur la ligne de commande pour assembler une image. [Docker](https://www.docker.com/get-started) peut construire des images automatiquement en lisant les instructions d'un [Dockerfile](https://docs.docker.com/engine/reference/builder/#usage)._

#### Des conteneurs Docker partout !

Conteneuriser votre application avec [Docker](https://www.docker.com/get-started) est aussi simple que de créer un [Dockerfile](https://docs.docker.com/engine/reference/builder/#usage) pour chacune de vos applications afin de construire d'abord une image, puis d'exécuter chaque image pour obtenir vos conteneurs en direct.

#### Conteneurisez votre Client

Pour construire notre image Client, vous aurez besoin d'un [Dockerfile](https://docs.docker.com/engine/reference/builder/#usage). Créons-en un :

1. Ouvrez l'application [React/Express](https://medium.com/@jrshenrique/create-a-react-frontend-a-node-express-backend-and-connect-them-together-c5798926047c) dans votre éditeur de code préféré (j'utilise [VS Code](https://code.visualstudio.com/)).
2. Accédez au dossier **Client**.
3. Créez un nouveau fichier nommé **Dockerfile**.
4. Placez ce code à l'intérieur :

```
# Utilise une version plus légère de Node comme image parenteFROM mhart/alpine-node:8.11.4
```

```
# Définit le répertoire de travail sur /clientWORKDIR /client
```

```
# copie package.json dans le conteneur à /clientCOPY package*.json /client/
```

```
# installe les dépendancesRUN npm install
```

```
# Copie le contenu du répertoire courant dans le conteneur à /clientCOPY . /client/
```

```
# Rend le port 3000 disponible pour le monde extérieur à ce conteneurEXPOSE 3000
```

```
# Exécute l'application lorsque le conteneur est lancéCMD ["npm", "start"]
```

Cela instruira Docker de construire une image (en utilisant ces configurations) pour notre Client. Vous pouvez lire tout sur [Dockerfile ici](https://docs.docker.com/engine/reference/builder/#usage).

#### Conteneurisez votre API

Pour construire notre image API, vous aurez besoin d'un autre [Dockerfile](https://docs.docker.com/engine/reference/builder/#usage). Créons-le :

1. Accédez au dossier **API**.
2. Créez un nouveau fichier nommé **Dockerfile**.
3. Placez ce code à l'intérieur :

```
# Utilise une version plus légère de Node comme image parenteFROM mhart/alpine-node:8.11.4
```

```
# Définit le répertoire de travail sur /apiWORKDIR /api
```

```
# copie package.json dans le conteneur à /apiCOPY package*.json /api/
```

```
# installe les dépendancesRUN npm install
```

```
# Copie le contenu du répertoire courant dans le conteneur à /apiCOPY . /api/
```

```
# Rend le port 80 disponible pour le monde extérieur à ce conteneurEXPOSE 80
```

```
# Exécute l'application lorsque le conteneur est lancéCMD ["npm", "start"]
```

Cela instruira Docker de construire une image (en utilisant ces configurations) pour notre API. Vous pouvez lire tout sur [Dockerfile ici](https://docs.docker.com/engine/reference/builder/#usage).

#### Docker-Compose

Vous pourriez exécuter chaque conteneur individuel en utilisant les Dockerfiles. Dans notre cas, nous avons 3 conteneurs à gérer, nous allons donc utiliser docker-compose à la place. Compose est un outil pour définir et exécuter des applications Docker multi-conteneurs.

Laissez-moi vous montrer à quel point il est simple de l'utiliser :

1. Ouvrez l'application [React/Express](https://medium.com/@jrshenrique/create-a-react-frontend-a-node-express-backend-and-connect-them-together-c5798926047c) dans votre éditeur de code.
2. Dans le dossier principal de votre application, créez un nouveau fichier et nommez-le [**docker-compose.yml**](https://docs.docker.com/compose/overview/).
3. Écrivez ce code dans le fichier [**docker-compose.yml**](https://docs.docker.com/compose/overview/) :

```
version: "2"
```

```
services:    client:        image: webapp-client        restart: always        ports:            - "3000:3000"        volumes:            - ./client:/client            - /client/node_modules        links:            - api        networks:            webappnetwork
```

```
    api:        image: webapp-api        restart: always        ports:            - "9000:9000"        volumes:            - ./api:/api            - /api/node_modules        depends_on:            - mongodb        networks:            webappnetwork
```

Quelle sorcellerie est-ce donc ?

Vous devriez lire tout sur [**docker-compose ici**](https://docs.docker.com/compose/overview/).

En gros, je dis à Docker que je veux construire un conteneur appelé **client**, en utilisant l'image **webapp-client** (qui est l'image que nous avons définie dans notre Dockerfile Client) qui écoutera sur le port 3000. Ensuite, je lui dis que je veux construire un conteneur appelé **api** en utilisant l'image **webapp-api** (qui est l'image que nous avons définie dans notre Dockerfile API) qui écoutera sur le port 9000.

> Gardez à l'esprit qu'il existe de nombreuses façons d'écrire un fichier [**docker-compose.yml**](https://docs.docker.com/compose/overview/). Vous devriez explorer la documentation et utiliser ce qui convient le mieux à vos besoins.

#### Ajoutez une base de données [MongoDB](https://www.mongodb.com/what-is-mongodb)

Pour ajouter une base de données [MongoDB](https://www.mongodb.com/what-is-mongodb), il suffit d'ajouter ces lignes de code à votre fichier [**docker-compose.yml**](https://docs.docker.com/compose/overview/) :

```
    mongodb:        image: mongo        restart: always        container_name: mongodb        volumes:            - ./data-node:/data/db        ports:            - 27017:27017        command: mongod --noauth --smallfiles        networks:            - webappnetwork
```

Cela créera un conteneur en utilisant l'[image officielle MongoDB](https://hub.docker.com/_/mongo/).

#### Créez un réseau partagé pour vos conteneurs

Pour créer un réseau partagé pour vos conteneurs, ajoutez simplement le code suivant à votre fichier **docker-compose.yml** :

```
networks:    webappnetwork:        driver: bridge
```

Remarquez que vous avez déjà défini chaque conteneur de votre application pour utiliser ce réseau.

À la fin, votre fichier [**docker-compose.yml**](https://docs.docker.com/compose/overview/) devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/g-sJXjQARQ5DUglNTrgUia77fRELTh8dqyPU)
_docker-compose.yml_

Dans le fichier **docker-compose.yml**, l'indentation est importante. Soyez-en conscient.

#### Lancez vos conteneurs

1. Maintenant que vous avez un fichier [**docker-compose.yml**](https://docs.docker.com/compose/overview/), construisons vos images. Allez dans le terminal et, dans le répertoire principal de votre application, exécutez :

```
docker-compose build
```

2. Maintenant, pour que Docker lance les conteneurs, exécutez simplement :

```
docker-compose up
```

Et... comme par magie, vous avez maintenant votre Client, votre API et votre Base de données, tous en cours d'exécution dans des conteneurs séparés avec une seule commande. N'est-ce pas génial ?

#### Connectez votre API à MongoDB

1. Tout d'abord, installons [Mongoose](https://mongoosejs.com/) pour nous aider avec la connexion à [MongoDB](https://www.mongodb.com/what-is-mongodb). Dans votre terminal, tapez :

```
npm install mongoose
```

2. Maintenant, créez un fichier appelé **testDB.js** dans votre dossier de routes API et insérez ce code :

```
const express = require("express");const router = express.Router();const mongoose = require("mongoose");
```

```
// Variable à envoyer au Frontend avec le statut de la base de donnéeslet databaseConnection = "En attente de la réponse de la base de données...";
```

```
router.get("/", function(req, res, next) {    res.send(databaseConnection);});
```

```
// Connexion à MongoDBmongoose.connect("mongodb://mongodb:27017/test");
```

```
// Si une erreur de connexion survient, envoie un message d'erreurmongoose.connection.on("error", error => {    console.log("Erreur de connexion à la base de données :", error);    databaseConnection = "Erreur de connexion à la base de données";});
```

```
// Si la connexion à MongoDB est établie, envoie un message de succèsmongoose.connection.once("open", () => {    console.log("Connecté à la base de données !");    databaseConnection = "Connecté à la base de données";});
```

```
module.exports = router;
```

D'accord, voyons ce que fait ce code. Tout d'abord, j'importe Express, ExpressRouter et [Mongoose](https://mongoosejs.com/) pour les utiliser sur notre route /testDB. Ensuite, je crée une variable qui sera envoyée comme réponse indiquant ce qui s'est passé avec la requête. Ensuite, je me connecte à la base de données en utilisant Mongoose.connect(). Ensuite, je vérifie si la connexion fonctionne ou non, et je modifie la variable (que j'ai créée précédemment) en conséquence. Enfin, j'utilise module.exports pour exporter cette route afin de pouvoir l'utiliser dans le fichier app.js.

2. Maintenant, vous devez « dire » à [Express](http://expressjs.com/) d'utiliser cette route que vous venez de créer. Dans votre dossier API, ouvrez le fichier **app.js** et insérez ces deux lignes de code :

```
var testDBRouter = require("./routes/testDB");app.use("/testDB", testDBRouter);
```

Cela « dira » à [Express](http://expressjs.com/) que chaque fois qu'il y a une requête vers le point de terminaison **/testDB**, il doit utiliser les instructions du fichier **testDB.js**.

3. Maintenant, testons si tout fonctionne correctement. Allez dans votre terminal et appuyez sur **_control + C_** pour arrêter vos conteneurs. Ensuite, exécutez **_docker-compose up_** pour les relancer. Une fois que tout est en cours d'exécution, si vous naviguez vers [http://localhost:9000/testDB](http://localhost:9000/testDB), vous devriez voir le message **_Connecté à la base de données._**

À la fin, votre fichier **app.js** devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/khTJL10Rc2DfF0brSn2DLzIuWNbnP45RWa93)
_api/app.js_

Oui... cela signifie que l'API est maintenant connectée à la base de données. Mais votre FrontEnd ne le sait pas encore. Travaillons sur cela maintenant.

#### **Faire une requête depuis [React](https://reactjs.org/) vers la base de données**

Pour vérifier si l'application React peut atteindre la base de données, faisons une simple requête vers le point de terminaison que vous avez défini à l'étape précédente.

1. Allez dans votre dossier **Client** et ouvrez le fichier **App.js**.
2. Maintenant, insérez ce code sous la méthode **callAPI()** :

```
callDB() {    fetch("http://localhost:9000/testDB")        .then(res => res.text())        .then(res =>; this.setState({ dbResponse: res }))        .catch(err => err);}
```

Cette méthode va récupérer le point de terminaison que vous avez défini précédemment sur l'API et récupérer la réponse. Ensuite, elle stockera la réponse dans l'état du composant.

4. Ajoutez une variable à l'état du composant pour stocker la réponse :

```
dbResponse: ""
```

3. À l'intérieur de la méthode de cycle de vie **componentDidMount()**, insérez ce code pour exécuter la méthode que vous venez de créer lorsque le composant est monté :

```
this.callDB();
```

4. Enfin, ajoutez une autre balise **<p>** après celle que vous avez déjà pour afficher la réponse de la base de données :

```
<p className="App-intro">;{this.state.dbResponse}</p>
```

À la fin, votre fichier App.js devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/DIpuBT8d3achTYZWQr-fl00UKzGCpPHVQaD0)
_client/App.js_

#### Enfin, voyons si tout fonctionne

Dans votre navigateur, allez à [http://localhost:3000/](http://localhost:3000/) et si tout fonctionne correctement, vous devriez voir ces trois messages :

1. Bienvenue sur React
2. L'API fonctionne correctement
3. Connecté à la base de données

Quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/L0dS1-hvjlZspmeZt6KXVrZmvcd2jBZ0xPDK)
_[http://localhost:3000/](http://localhost:3000/" rel="noopener" target="_blank" title=")_

#### **Félicitations !!!**

Vous avez maintenant une application full stack avec un FrontEnd React, une API Node/Express et une base de données MongoDB. Tout cela fonctionne dans des conteneurs Docker individuels qui sont orchestrés avec un simple fichier docker-compose.

Cette application peut être utilisée comme un modèle pour construire votre application plus robuste.

Vous pouvez trouver tout le code que j'ai écrit [dans le dépôt du projet](https://github.com/Joao-Henrique/docker_tutorial).

> Soyez fort et continuez à coder !!!

...et n'oubliez pas d'être génial aujourd'hui ;)