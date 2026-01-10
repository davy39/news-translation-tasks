---
title: Comment déployer une application MERN sur Heroku en utilisant MongoDB Atlas
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-21T14:27:17.000Z'
originalURL: https://freecodecamp.org/news/deploying-a-mern-application-using-mongodb-atlas-to-heroku
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/1_qgxaya.png
tags:
- name: Express
  slug: express
- name: JavaScript
  slug: javascript
- name: MongoDB
  slug: mongodb
- name: Node.js
  slug: nodejs
- name: prototype
  slug: prototype
- name: React
  slug: react
seo_title: Comment déployer une application MERN sur Heroku en utilisant MongoDB Atlas
seo_desc: 'By Dillion Megida

  Introduction to MERN

  In this article, we''ll be building and deploying an application built with the
  MERN stack to Heroku.

  MERN, which stands for MongoDB, Express, React, and Node.js, is a popular tech stack
  used in building web appl...'
---

Par Dillion Megida

## Introduction à MERN

Dans cet article, nous allons construire et déployer une application construite avec la pile MERN sur Heroku.

MERN, qui signifie MongoDB, Express, React et Node.js, est une pile technologique populaire utilisée dans la construction d'applications web. Elle implique le travail frontal (avec React), le travail dorsal (avec Express et NodeJS) et une base de données (avec MongoDB).

[Heroku](https://www.heroku.com/), en revanche, est une plateforme en tant que service (PaaS) qui permet aux développeurs de construire, exécuter et exploiter des applications entièrement dans le cloud.

Pour la base de données, nous utiliserons MongoDB Atlas, qui est un service de base de données cloud mondial pour les applications modernes. Cela est plus sécurisé que MongoDB installé localement sur notre serveur et cela nous donne également plus de ressources sur nos serveurs.

Pour le frontal, nous allons construire une simple application React qui fait des requêtes POST à une API pour ajouter un utilisateur, et peut également faire des requêtes GET pour obtenir tous les utilisateurs.

_Vous pouvez sauter à n'importe quelle étape avec la table des matières listée ci-dessous._

## Table des matières

* [Introduction à MERN](#heading-introduction-a-mern)
* [Commençons à construire](#heading-commencons-a-construire)
* [Construction de l'application React](#heading-construction-de-lapplication-react)
* [Création du Backend](#heading-creation-du-backend)
* [Connecter la base de données MongoDB Atlas](#heading-connecter-la-base-de-donnees-mongodb-atlas)
* [Appel des APIs sur le Frontend](#heading-appel-des-apis-sur-le-frontend)
* [Déploiement sur Heroku](#heading-deploiement-sur-heroku)
* [Créer une application Heroku](#heading-creer-une-application-heroku)
* [Configurer package.json](#heading-configurer-packagejson)
* [Conclusion](#heading-conclusion)

## Commençons à construire

### Construction de l'application React

**Note :** Avant de commencer avec notre projet, `node` doit être installé sur votre ordinateur. `node` nous fournit également `npm`, qui est utilisé pour installer des packages.

#### Installer `create-react-app`

`create-react-app` est utilisé pour créer une application React de démarrage.

Si vous n'avez pas `create-react-app` installé, tapez ce qui suit dans la ligne de commande :

```shell
npm i create-react-app -g
```

Le drapeau `-g` installe le package globalement.

#### Créer le répertoire du projet

```shell
create-react-app my-project
cd my-project
```

Ce qui précède crée un répertoire 'my-project', et installe les dépendances qui seront utilisées dans l'application React de démarrage. Après l'installation, la deuxième commande change le répertoire du projet.

#### Démarrer l'application et faire les modifications nécessaires

```shell
npm start
```

La commande ci-dessus démarre l'application React, ce qui vous donne une URL où vous pouvez prévisualiser le projet. Vous pouvez ensuite faire les modifications nécessaires comme changer les images ou le texte.

#### Installer axios

```shell
npm i axios --save
```

`axios` est une bibliothèque JavaScript utilisée pour faciliter les requêtes HTTP. Elle sera utilisée pour envoyer des requêtes depuis le frontal (React) vers les APIs fournies par le backend.

### Création du Backend

Le backend gère les APIs, traite les requêtes et se connecte également à la base de données.

#### Installer les packages backend

```shell
npm i express cors mongoose body-parser --save
```

1. `express` : "Express est un framework d'application web Node.js minimal et flexible qui fournit un ensemble robuste de fonctionnalités pour les applications web" - Documentation [Express](http://expressjs.com/)
2. `cors` : "CORS est un package node.js pour fournir un middleware Connect/Express qui peut être utilisé pour activer CORS avec diverses options" - [Documentation cors](https://www.npmjs.com/package/cors)
3. `mongoose` : "Mongoose est un outil de modélisation d'objets MongoDB conçu pour fonctionner dans un environnement asynchrone. Mongoose prend en charge les promesses et les rappels" - [Documentation Mongoose](https://www.npmjs.com/package/mongoose)
4. `body-parser` : "Middleware d'analyse de corps Node.js." - [Documentation body-parser](https://www.npmjs.com/package/mongoose)

#### Créer le dossier backend

```shell
mkdir backend
cd backend
```

#### Configurer le backend

##### Créer un point d'entrée `server.js`

Tout d'abord, créez un fichier `server.js`, qui sera le point d'entrée du backend.

```shell
touch server.js
```

Dans `server.js`, tapez ce qui suit :

```js
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const path = require('path')
const app = express();
require('./database');
-----
app.use(bodyParser.json());
app.use(cors());
-----
// API
const users = require('/api/users');
app.use('/api/users', users);
-----
app.use(express.static(path.join(__dirname, '../build')))
app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname, '../build'))
})
-----
const port = process.env.PORT || 5000;
app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```

`express.static` fournit des fichiers statiques qui sont ceux construits lorsque `npm run build` est exécuté sur un projet React. N'oubliez pas que le fichier construit se trouve dans le dossier build.

D'après notre configuration, toute requête envoyée à `/api/users` sera envoyée à l'API `users` que nous allons configurer.

##### Configurer l'API `users`

```shell
mkdir api
touch api/users.js
```

Dans `api/users.js`, ajoutez ce qui suit :

```js
const express = require('express');
const router = express.Router()
-----
const User = require('../models/User');
-----
router.get('/', (req, res) => {
    User.find()
        .then(users => res.json(users))
        .catch(err => console.log(err))
})
-----
router.post('/', (req, res) => {
    const { name, email } = req.body;
    const newUser = new User({
        name: name, email: email
    })
    newUser.save()
        .then(() => res.json({
            message: "Compte créé avec succès"
        }))
        .catch(err => res.status(400).json({
            "error": err,
            "message": "Erreur lors de la création du compte"
        }))
})
module.exports = router 
```

Dans le code ci-dessus, nous créons un gestionnaire de requêtes GET et POST qui récupère tous les utilisateurs et publie les utilisateurs. La récupération et l'ajout d'un utilisateur à la base de données sont aidés par le modèle `User` que nous allons créer.

##### Créer le modèle `User`

```shell
mkdir models
touch models/user.js
```

Dans `models/user.js`, ajoutez ce qui suit :

```js
const mongoose = require('mongoose');
const Schema = mongoose.Schema;
-----
const userSchema = new Schema({
    name: {
        type: String,
        required: true
    },
    email: {
        type: String,
        required: true
    }
})
module.exports = mongoose.model("User", userSchema, "users")
```

Dans le code ci-dessus, un schéma est créé pour l'utilisateur qui contient les champs de l'utilisateur. À la fin du fichier, le modèle ("User") est exporté avec le schéma et la collection ("users").

##### Connecter la base de données MongoDB Atlas

Selon [la documentation](https://www.mongodb.com/cloud/atlas), "MongoDB Atlas est le service de base de données cloud mondial pour les applications modernes."

Tout d'abord, nous devons nous enregistrer sur Mongo cloud. Suivez [cette documentation](https://docs.atlas.mongodb.com/getting-started/) pour créer un compte Atlas et créer votre cluster.

Une chose à noter est **la liste blanche de votre adresse IP de connexion**. Si vous ignorez cette étape, vous n'aurez pas accès au cluster, alors faites attention à cette étape.

Le cluster est un petit serveur qui gérera nos collections (similaires aux tables dans les bases de données SQL). Pour connecter votre backend au cluster, créez un fichier `database.js`, qui, comme vous pouvez le voir, est requis dans `server.js`. Ensuite, entrez ce qui suit :

```js
const mongoose = require('mongoose');
const connection = "mongodb+srv://username:<password>@<cluster>/<database>?retryWrites=true&w=majority";
mongoose.connect(connection,{ useNewUrlParser: true, useUnifiedTopology: true, useFindAndModify: false})
    .then(() => console.log("Base de données connectée avec succès"))
    .catch(err => console.log(err));
```

Dans la variable `connection`, entrez votre `username` (pour MongoDB cloud), votre `password` (mot de passe du cluster), votre `cluster` (adresse de votre cluster) et la `database` (nom de votre base de données). Toutes ces informations peuvent être facilement découvertes si vous avez suivi la documentation.

## Appel des APIs sur le Frontend

Toutes les APIs seront disponibles sur `localhost:5000` localement, comme nous l'avons configuré dans `server.js`. Lorsque l'application est déployée sur Heroku, le serveur utilisera le port fourni par le serveur (`process.env.PORT`).

Pour simplifier les choses, React nous permet de spécifier un proxy vers lequel les requêtes seront envoyées.

Ouvrez `package.json` et ajoutez ce qui suit juste avant la dernière accolade :

```json
"proxy": "http://localhost:5000"
```

De cette manière, nous pouvons envoyer directement des requêtes à `api/users`. Et lorsque notre site est déployé et construit, le port par défaut de notre application sera utilisé avec la même API.

Ouvrez `App.js` pour React et ajoutez ce qui suit :

```js
import React, {useState, useEffect} from 'react'
import axios from 'axios';
-----
const App = function () {
	const [users, setUsers] = useState(null);

	const [username, setUsername] = useState("");
	const [email, setEmail] = useState("");
	useEffect(() => {
		axios
			.get("/api/users")
			.then((users) => setUsers(users))
			.catch((err) => console.log(err));
	}, []);

	function submitForm() {
		if (username === "") {
			alert("Veuillez remplir le champ du nom d'utilisateur");
			return;
		}
		if (email === "") {
			alert("Veuillez remplir le champ email");
			return;
		}
		axios
			.post("/api/users", {
				username: username,
				email: email,
			})
			.then(function () {
				alert("Compte créé avec succès");
				window.location.reload();
			})
			.catch(function () {
				alert("Impossible de créer le compte. Veuillez réessayer");
			});
	}
	return (
		<>
			<h1>Mon Projet</h1>
			{users === null ? (
				<p>Chargement...</p>
			) : users.length === 0 ? (
				<p>Aucun utilisateur disponible</p>
			) : (
				<>
					<h2>Utilisateurs disponibles</h2>
					<ol>
						{users.map((user, index) => (
							<li key={index}>
								Nom : {user.name} - Email : {user.email}
							</li>
						))}
					</ol>
				</>
			)}

			<form onSubmit={submitForm}>
				<input
					onChange={(e) => setUsername(e.target.value)}
					type="text"
					placeholder="Entrez votre nom d'utilisateur"
				/>
				<input
					onChange={(e) => setEmail(e.target.value)}
					type="text"
					placeholder="Entrez votre adresse email"
				/>
				<input type="submit" />
			</form>
		</>
	);
};
export default App
```

Les hooks `useState` et `useEffect` sont utilisés pour gérer l'état et les `sideEffects`. Ce qui se passe essentiellement, c'est que le premier état des utilisateurs est `null` et 'Chargement...' est affiché dans le navigateur. 

Dans `useEffect`, `[]` est utilisé pour spécifier qu'à l'étape `componentDidMount` (lorsque le composant est monté), une requête Axios est faite à l'API qui s'exécute sur `localhost:5000`. Si elle obtient le résultat et qu'il n'y a pas d'utilisateur, 'Aucun utilisateur disponible' est affiché. Sinon, une liste numérotée des utilisateurs est affichée.

Si vous souhaitez en savoir plus sur `useState` et `useEffect`, consultez cet article - [Qu'est-ce que React Hooks ?](https://blog.soshace.com/what-the-heck-is-react-hooks/)

Avec le formulaire disponible, une requête POST peut être faite pour publier un nouvel utilisateur. L'état des entrées est contrôlé et envoyé à l'API à `localhost:5000` lors de la soumission. Ensuite, la page est actualisée et le nouvel utilisateur est affiché.

## Déploiement sur Heroku

Pour déployer votre application sur Heroku, vous devez avoir un compte Heroku. 

Allez sur [leur page](https://www.heroku.com/) pour créer un compte. Ensuite, suivez [leur documentation](https://devcenter.heroku.com/articles/creating-apps) sur la façon de créer une application Heroku. Consultez également [la documentation](https://devcenter.heroku.com/articles/heroku-cli) sur Heroku CLI.

### Créer une application Heroku

Tout d'abord, connectez-vous à Heroku :

```shell
heroku login
```

Cela vous redirigera vers une URL dans le navigateur où vous pourrez vous connecter. Une fois terminé, vous pourrez continuer dans le terminal.

Dans le même répertoire du projet React, exécutez ce qui suit :

```shell
heroku create
```

Cela créera une application Heroku et vous donnera également l'URL pour accéder à l'application.

### Configurer package.json

Heroku utilise votre fichier package.json pour savoir quels scripts exécuter et quelles dépendances installer pour que votre projet s'exécute avec succès.

Dans votre fichier `package.json`, ajoutez ce qui suit :

```json
{
    ...
    "scripts": {
        ...
        "start": "node backend/server.js",
        "heroku-postbuild": "NPM_CONFIG_PRODUCTION=false npm install npm && run build"
    },
    ...
    "engines": {
        "node": "10.16.0"
    }
}
```

Heroku exécute un post-build, qui, comme vous pouvez le voir, installe vos dépendances et exécute un build de votre projet React. Ensuite, il démarre votre projet avec le script `start` qui démarre essentiellement votre serveur. Après cela, votre projet devrait fonctionner correctement.

`engines` spécifie les versions des moteurs comme `node` et `npm` à installer.

#### Pousser vers Heroku

```shell
git push heroku master
```

Cela pousse votre code vers Heroku. N'oubliez pas d'inclure les fichiers inutiles dans `.gitignore`.

Après quelques secondes, votre site sera prêt. Si des erreurs surviennent, vous pouvez vérifier votre terminal ou aller sur votre tableau de bord dans le navigateur pour voir les logs de build.

Vous pouvez maintenant prévisualiser votre site à l'URL que Heroku a envoyée lorsque vous avez exécuté `heroku create`.

C'est tout ce qu'il y a à faire. Heureux que vous ayez lu jusqu'ici.

## Conclusion

Bien sûr, il y a plus à dire sur les applications de la pile MERN.

Cet article n'a pas abordé en profondeur les authentifications, les connexions, les sessions, et tout cela. Il a simplement couvert comment déployer des applications de la pile MERN sur Heroku et travailler avec MongoDB Atlas.

Vous pouvez trouver d'autres articles comme celui-ci sur mon blog - [dillionmegida.com](https://dillionmegida.com)

Merci d'avoir lu.