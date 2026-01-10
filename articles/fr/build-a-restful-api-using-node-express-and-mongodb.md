---
title: Comment construire une API RESTful en utilisant Node, Express et MongoDB
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-02-21T18:15:19.000Z'
originalURL: https://freecodecamp.org/news/build-a-restful-api-using-node-express-and-mongodb
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/How-to-Build-a-Weather-Application-using-React--65-.png
tags:
- name: Express
  slug: express
- name: MongoDB
  slug: mongodb
- name: node
  slug: node
- name: REST API
  slug: rest-api
seo_title: Comment construire une API RESTful en utilisant Node, Express et MongoDB
seo_desc: 'By Nishant Kumar

  In this article, we''ll build a RESTful API using Node, Express, and MongoDB. We
  will create endpoints for creating data, reading data, updating data, and deleting
  data (basic CRUD operations).

  But before we get started, make sure you...'
---

Par Nishant Kumar

Dans cet article, nous allons construire une API RESTful en utilisant Node, Express et MongoDB. Nous allons créer des endpoints pour créer des données, lire des données, mettre à jour des données et supprimer des données (opérations CRUD de base).

Mais avant de commencer, assurez-vous d'avoir Node installé sur votre système. Si ce n'est pas le cas, rendez-vous sur [https://nodejs.org/en/download/](https://nodejs.org/en/download/) pour le télécharger et l'installer.

## Commençons par la configuration de base

Dans un dossier vide, exécutez la commande suivante :

```
npm init
```

Cette commande vous demandera diverses informations, telles que le nom de votre projet, l'auteur, le dépôt, etc. Ensuite, elle générera un fichier **package.json** dans ce dossier.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-19-130254.jpeg)

```
{
  "name": "rest-api-express-mongo",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC"
}

```

Ce fichier Package.json contiendra tous les scripts, comme comment exécuter l'application, ou comment tester l'application, ainsi que toutes les dépendances.

Nous devons installer quelques dépendances maintenant.

```
npm i express mongoose nodemon dotenv
```

Ici,

1. Express sera utilisé pour le middleware afin de créer divers endpoints CRUD.
2. Mongoose pour gérer les données dans MongoDB en utilisant diverses requêtes.
3. Nodemon pour redémarrer notre serveur chaque fois que nous sauvegardons notre fichier.
4. Dotenv pour gérer un fichier **.env**.

Alors, allez-y et installez-les.

Après leur installation, créez un fichier nommé **index.js**. Ce sera le point d'entrée de notre application.

Et dans ce fichier, ajoutons Express et Mongoose, et exécutons le fichier.

```
const express = require('express');
const mongoose = require('mongoose');
```

Maintenant, transférons le contenu d'Express dans une nouvelle constante appelée **app**.

```
const express = require('express');
const mongoose = require('mongoose');

const app = express();
```

Maintenant, écoutons les changements de ce fichier sur le port 3000.

```
const express = require('express');
const mongoose = require('mongoose');

const app = express();

app.use(express.json());

app.listen(3000, () => {
    console.log(`Serveur démarré sur le port ${3000}`)
})
```

Maintenant, le serveur est configuré sur le **port 3000**. Écrivons le script pour démarrer notre serveur. Nous avons également ajouté **app.use**. À l'intérieur, nous avons un extrait de code qui nous permet d'accepter les données au format JSON.

Dans le fichier package.json, ajoutez un script qui dit ce qui suit :

```
"scripts": {
    "start": "nodemon index.js"
},
```

Cela signifie que nous pouvons démarrer notre serveur en utilisant **npm start**, et il s'exécutera en utilisant le package Nodemon que nous avons installé précédemment.

Tapez npm start dans le terminal, et nous verrons la sortie suivante dans le terminal :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-19-132326.jpeg)

## Comment configurer la base de données MongoDB

Maintenant, configurons la base de données MongoDB. Rendez-vous sur [https://account.mongodb.com/account/login](https://account.mongodb.com/account/login) et créez votre compte, ou connectez-vous si vous en avez déjà un.

Après vous être connecté, nous devons créer une base de données.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-19-132848.jpeg)

Alors, créez un **Cluster Partagé Gratuit**.

Il vous demandera le nom d'utilisateur et le mot de passe, alors remplissez-les.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-19-132958.jpeg)

Ensuite, ajoutez votre adresse IP.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-19-133131.jpeg)

Cliquez sur Terminer et Fermer.

Il faudra un certain temps pour que notre cluster se termine, alors attendons. Pendant ce temps, créez un fichier appelé **.env** dans le dossier du projet.

Et dans la page d'accueil du Cluster, cliquez sur le bouton de connexion.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-19-133319.jpeg)

La fenêtre suivante apparaîtra :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-19-133404.jpeg)

Cliquez sur MongoDB Compass, et il retournera la chaîne suivante. Téléchargez et installez également MongoDB Compass.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-19-133516.jpeg)

Ajoutez votre nom d'utilisateur et votre mot de passe à cette chaîne que vous avez utilisée auparavant. La chaîne de connexion finale ressemblera à ceci :

```
mongodb+srv://nishant:********@cluster0.xduyh.mongodb.net/testDatabase

```

Ici, nishant est le nom d'utilisateur, suivi du mot de passe, et enfin le nom de la base de données.

Alors, collez cette chaîne dans le fichier **.env**.

```
DATABASE_URL = mongodb+srv://nishant:*******@cluster0.xduyh.mongodb.net/testDatabase

```

Maintenant, dans MongoDB Compass, ajoutez également cette chaîne.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-19-134347.jpeg)

Ensuite, cliquez sur Connecter.

Ici, nous obtiendrons deux bases de données qui sont par défaut. Une troisième sera créée automatiquement plus tard.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-19-134435.jpeg)

Maintenant, importons le contenu de notre fichier **.env** dans le fichier de script, index.js.

```
require('dotenv').config();

const mongoString = process.env.DATABASE_URL
```

Ici, nous stockons la chaîne dans une variable appelée **mongoString**.

Maintenant, connectons la base de données à notre serveur en utilisant Mongoose.

```
mongoose.connect(mongoString);
const database = mongoose.connection
```

Maintenant, nous devons envoyer un message de succès ou d'erreur selon que notre connexion à la base de données est réussie ou échoue.

```
database.on('error', (error) => {
    console.log(error)
})

database.once('connected', () => {
    console.log('Base de données connectée');
})
```

Ici, **database.on** signifie qu'il se connectera à la base de données et enverra toute erreur si la connexion échoue. Et **database.once** signifie qu'il ne s'exécutera qu'une seule fois. Si c'est un succès, il affichera un message indiquant que la base de données est connectée.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-19-135414-1.jpeg)

Voici le code complet jusqu'à ce point :

```
require('dotenv').config();

const express = require('express');
const mongoose = require('mongoose');
const mongoString = process.env.DATABASE_URL;

mongoose.connect(mongoString);
const database = mongoose.connection;

database.on('error', (error) => {
    console.log(error)
})

database.once('connected', () => {
    console.log('Base de données connectée');
})
const app = express();

app.use(express.json());

app.listen(3000, () => {
    console.log(`Serveur démarré sur le port ${3000}`)
})
```

## Comment créer nos routes pour les endpoints

Créez un dossier appelé routes, et à l'intérieur, créez un fichier appelé routes.js.

Importez ce fichier dans notre fichier de script principal, index.js.

```
const routes = require('./routes/routes');
```

Utilisons également ce fichier de routes.

```
const routes = require('./routes/routes');

app.use('/api', routes)
```

Ici, cet app.use prend deux choses. L'une est l'endpoint de base, et l'autre est le contenu des routes. Maintenant, tous nos endpoints commenceront par '/api'.

Nous obtiendrons une erreur car nous n'avons rien à l'intérieur du fichier de routes. Alors, ajoutons-les.

```
const express = require('express');

const router = express.Router()

module.exports = router;
```

Ici, nous utilisons Router d'Express, et nous l'exportons également en utilisant module.exports. Et maintenant, notre application fonctionnera correctement.

## Comment écrire nos endpoints

Maintenant, écrivons nos endpoints ici dans ce fichier de routes. Nous aurons cinq routes pour les actions suivantes :

1. Poster des données dans la base de données.
2. Obtenir toutes les données de la base de données.
3. Obtenir des données basées sur l'ID.
4. Mettre à jour des données basées sur l'ID.
5. Supprimer des données basées sur l'ID.

Alors, créons les routes pour ces actions :

```
//Méthode Post
router.post('/post', (req, res) => {
    res.send('Post API')
})

//Méthode Get all
router.get('/getAll', (req, res) => {
    res.send('Get All API')
})

//Méthode Get by ID
router.get('/getOne/:id', (req, res) => {
    res.send('Get by ID API')
})

//Méthode Update by ID
router.patch('/update/:id', (req, res) => {
    res.send('Update by ID API')
})

//Méthode Delete by ID
router.delete('/delete/:id', (req, res) => {
    res.send('Delete by ID API')
})
```

Nous avons cinq méthodes qui utilisent les méthodes REST de Post, Get, Patch et Delete.

Ce routeur prend la route comme premier paramètre. Ensuite, dans le deuxième paramètre, il prend un callback.

Dans le callback, nous avons un **res** et un **req**. **res** signifie **réponse**, et **req** signifie **requête**. Nous utilisons **res** pour envoyer des réponses à notre client, comme Postman, ou tout client front-end. Et nous utilisons **req** pour recevoir des requêtes d'une application cliente comme Postman, ou tout client front-end.

Ensuite, dans le corps du callback, nous imprimons un message qui dit le message de l'API respective.

Enregistrez ceci, et ouvrez Postman pour vérifier les endpoints. Téléchargez [Postman](https://www.postman.com/downloads/) si vous ne l'avez pas. C'est un outil incroyable pour tester les endpoints d'API.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-19-141237.jpeg)

Ajoutez cette adresse dans la barre d'adresse, puis cliquez sur Envoyer, ou appuyez sur entrée.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-19-141328.jpeg)

Nous obtiendrons ce message dans le corps de Postman, car nous envoyons simplement un message en utilisant **res.send**.

Maintenant, prenons une réponse d'une application cliente. Imprimons simplement un ID.

Nous devons d'abord changer la fonction **getOne**. Nous obtenons l'ID en utilisant **req.params.id**, puis nous l'envoyons à l'application cliente en utilisant **res.send**.

```
//Méthode Get by ID
router.get('/getOne/:id', (req, res) => {
    res.send(req.params.id)
})
```

```
localhost:3000/api/getOne/1000
```

Ajoutez cet endpoint dans la barre d'adresse. Ici, nous utilisons l'endpoint **getOne**, suivi de l'ID. Ensuite, cliquez sur Envoyer.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-19-142619.jpeg)

Nous obtiendrons l'ID dans le corps de la réponse dans Postman.

## Comment créer le modèle

Maintenant, créons un modèle qui définira la structure de notre base de données.

Créez un dossier appelé model et à l'intérieur, un fichier appelé model.js.

```
const mongoose = require('mongoose');

const dataSchema = new mongoose.Schema({
    name: {
        required: true,
        type: String
    },
    age: {
        required: true,
        type: Number
    }
})

module.exports = mongoose.model('Data', dataSchema)
```

Ici, nous avons un schéma qui définit la structure de notre base de données. Il a une propriété **name** et une propriété **age**. Les deux champs ont des types et les deux sont requis.

Ensuite, nous exportons simplement le modèle de schéma.

Maintenant, importez ce modèle à l'intérieur du fichier **routes.js**.

```
const Model = require('../models/model');
```

## Comment poster des données dans la base de données

Créons le corps des données à poster en utilisant le modèle que nous venons de créer.

```
router.post('/post', (req, res) => {
    const data = new Model({
        name: req.body.name,
        age: req.body.age
    })
})
```

Notre name et age acceptent le name et l'âge de **req body**. Nous obtenons ces données de l'application cliente telle que **Postman**, ou tout client frontend comme **React** ou **Angular**.

Nous allons également créer un bloc **try-catch** pour gérer les messages de succès et les erreurs.

```
//Méthode Post
router.post('/post', (req, res) => {
    const data = new Model({
        name: req.body.name,
        age: req.body.age
    })

    try{

    }
    catch(error){
        
    }
})
```

Dans le bloc try, nous sauvegardons les **data** en utilisant **data.save()**. Ensuite, nous stockons les données dans une const appelée **dataToSave**.

Nous envoyons également le message de succès avec les données dans le corps de la réponse.

Et dans le bloc catch, nous recevons toute erreur si nous en avons.

```
//Méthode Post
router.post('/post', (req, res) => {
    const data = new Model({
        name: req.body.name,
        age: req.body.age
    })

    try {
        const dataToSave = data.save();
        res.status(200).json(dataToSave)
    }
    catch (error) {
        res.status(400).json({message: error.message})
    }
})
```

Maintenant, ajoutons quelques données depuis Postman. Mais avant cela, cette fonction doit être asynchrone pour fonctionner. Alors, nous allons utiliser async-await.

```
router.post('/post', async (req, res) => {
    const data = new Model({
        name: req.body.name,
        age: req.body.age
    })

    try {
        const dataToSave = await data.save();
        res.status(200).json(dataToSave)
    }
    catch (error) {
        res.status(400).json({message: error.message})
    }
})
```

Si nous ajoutons les données dans le corps et cliquons sur Envoyer, nous obtiendrons ce qui suit :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-19-145714.jpeg)

Il génère également un ID unique. Ouvrez l'application MongoDB Compass, et vous verrez la base de données et cet enregistrement que vous venez de créer :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-19-150007.jpeg)

## Comment obtenir toutes les données

Obtenir des données est également simple. Juste quelques lignes de code :

```
router.get('/getAll', async (req, res) => {
    try{
        const data = await Model.find();
        res.json(data)
    }
    catch(error){
        res.status(500).json({message: error.message})
    }
})
```

Ici, nous utilisons la méthode **Model.find** pour récupérer toutes les données de la base de données. Ensuite, nous les retournons au format JSON. Si nous avons une erreur, nous l'obtiendrons également.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-19-150423.jpeg)

Si nous appelons cet endpoint dans Postman, nous obtiendrons un tableau d'objets dans le corps de Postman.

## Comment obtenir des données basées sur l'ID

Celui-ci est également simple. Nous devons simplement passer l'ID du document, qui est **req.params.id**, dans une méthode appelée **findById**.

```
//Méthode Get by ID
router.get('/getOne/:id', async (req, res) => {
    try{
        const data = await Model.findById(req.params.id);
        res.json(data)
    }
    catch(error){
        res.status(500).json({message: error.message})
    }
})
```

Si nous cliquons sur Envoyer, nous obtiendrons les données basées sur l'ID.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-19-150808.jpeg)

## Comment mettre à jour et supprimer des données basées sur l'ID

Tout d'abord, ciblons la méthode de mise à jour en utilisant la méthode **patch**.

```
//Méthode Update by ID
router.patch('/update/:id', async (req, res) => {
    try {
        const id = req.params.id;
        const updatedData = req.body;
        const options = { new: true };

        const result = await Model.findByIdAndUpdate(
            id, updatedData, options
        )

        res.send(result)
    }
    catch (error) {
        res.status(400).json({ message: error.message })
    }
})
```

Ici, nous avons trois paramètres que nous passons dans la méthode **findByIdAndUpdate**, que nous utilisons pour trouver un document par ID et le mettre à jour.

Le **req.params.id** est la const id, **updatedData** qui contient le req.body, et les **options**, qui spécifient si les données mises à jour doivent être retournées dans le corps ou non.

Testons cela maintenant. Collez simplement l'ID d'un document spécifique, et cliquez sur Envoyer. Changez également les endpoints.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-19-152717.jpeg)

Nous mettons à jour en utilisant un ID, et il est mis à jour.

La suppression est également simple. Implémentons-la :

```
//Méthode Delete by ID
router.delete('/delete/:id', async (req, res) => {
    try {
        const id = req.params.id;
        const data = await Model.findByIdAndDelete(id)
        res.send(`Document avec ${data.name} a été supprimé..`)
    }
    catch (error) {
        res.status(400).json({ message: error.message })
    }
})
```

Nous obtenons l'ID ici, puis nous utilisons Model.findByIdAndDelete pour supprimer ce champ, tout en passant l'id.

Nous stockons les données mises à jour dans une const **data**.

Dans la réponse, nous obtiendrons le message que ce document avec le nom spécifique a été supprimé.

Si nous testons cela, nous obtiendrons ce qui suit :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-19-153557.jpeg)

Donc, les cinq méthodes sont terminées. Nous pouvons poster des données et obtenir toutes les données (basées sur l'ID aussi). Nous pouvons également les mettre à jour et les supprimer.

### Merci d'avoir lu !

Dans cet article, vous avez appris tout sur la conception et le développement d'une API RESTful en utilisant Node, Express et MongoDB.

Maintenant, vous pouvez utiliser ces endpoints pour construire une application Full-Stack, avec Vanilla JavaScript, React, Angular, Next ou Vue.js.

Vous pouvez également consulter ma vidéo sur le même sujet, [RESTful APIs - Build a RESTful API using Node, Express, and MongoDB](https://youtu.be/paxagc55loU)

N'hésitez pas à télécharger le code depuis [Github](https://github.com/nishant-666/Rest-Api-Express-MongoDB) et à expérimenter.

> Bon apprentissage.