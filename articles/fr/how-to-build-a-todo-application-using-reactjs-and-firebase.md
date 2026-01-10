---
title: Comment construire une TodoApp en utilisant ReactJS et Firebase
subtitle: ''
author: Sharvin Shah
co_authors: []
series: null
date: '2020-04-15T00:01:20.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-todo-application-using-reactjs-and-firebase
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-11-at-5.10.03-PM.png
tags:
- name: Apps
  slug: apps-tag
- name: Firebase
  slug: firebase
- name: React
  slug: reactjs
seo_title: Comment construire une TodoApp en utilisant ReactJS et Firebase
seo_desc: 'Hello folks, welcome to this tutorial. Before we begin you should be familiar
  with basic ReactJS concepts. If you''re not, I would recommend that you go through
  the ReactJS documentation.

  We will use the following components in this application:


  Reac...'
---

Bonjour à tous, bienvenue dans ce tutoriel. Avant de commencer, vous devriez être familier avec les concepts de base de ReactJS. Si ce n'est pas le cas, je vous recommande de consulter la [documentation ReactJS](https://reactjs.org/docs/getting-started.html).

Nous allons utiliser les composants suivants dans cette application :

1. [**ReactJS**](https://reactjs.org/)

2. [**Material UI**](https://material-ui.com/)

3. [**Firebase**](https://firebase.google.com/)

4. [**ExpressJS**](https://expressjs.com/)

5. [**Postman**](https://www.postman.com/)

## À quoi notre application va ressembler :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Account-1.gif align="left")

*Création de compte*

![Image](https://www.freecodecamp.org/news/content/images/2020/04/ezgif.com-optimize.gif align="left")

*Tableau de bord TodoApp*

---

## Architecture de l'application :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/TodoApp-1.png align="left")

*Architecture de l'application*

## Comprendre nos composants :

Vous vous demandez peut-être pourquoi nous utilisons Firebase dans cette application. Eh bien, il fournit une **authentification sécurisée**, une **base de données en temps réel**, un **composant serverless** et un **bucket de stockage**.

Nous utilisons Express ici afin de ne pas avoir à gérer les exceptions HTTP. Nous allons utiliser tous les packages Firebase dans notre composant de fonctions. Cela est dû au fait que nous ne voulons pas rendre notre application cliente trop volumineuse, ce qui tend à ralentir le processus de chargement de l'UI.

**Note :** Je vais diviser ce tutoriel en quatre sections distinctes. Au début de chaque section, vous trouverez un commit git qui contient le code développé dans cette section. De plus, si vous souhaitez voir le code complet, il est disponible dans ce [dépôt](https://github.com/Sharvin26/TodoApp).

## Section 1 : Développement des API Todo

Dans cette section, nous allons développer ces éléments :

1. **Configurer les fonctions Firebase.**

2. **Installer le framework Express et construire les API Todo.**

3. **Configurer Firestore comme base de données.**

Le **code de l'API Todo** implémenté dans cette section peut être trouvé à ce [commit](https://github.com/Sharvin26/TodoApp/tree/256e69f5d53646b648347b6f1fbdb965ad184763).

### Configurer les fonctions Firebase :

Allez sur la [console Firebase](https://firebase.google.com/).

![Image](https://www.freecodecamp.org/news/content/images/2020/04/FirebaseFunctions.png align="left")

*Console Firebase*

Sélectionnez l'option **Ajouter un projet**. Après cela, suivez le gif ci-dessous étape par étape pour configurer le projet Firebase.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/FirebaseConfigure.gif align="left")

*Configuration Firebase*

Allez dans l'onglet des fonctions et cliquez sur le bouton **Commencer** :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/FirebaseFunctionConfig1.png align="left")

*Tableau de bord des fonctions*

Vous verrez une boîte de dialogue qui contient des instructions sur **Comment configurer les fonctions Firebase**. Allez dans votre environnement local. Ouvrez un outil de ligne de commande. Pour installer les outils Firebase sur votre machine, utilisez la commande suivante :

```shell
 npm install -g firebase-tools
```

Une fois cela fait, utilisez la commande `firebase init` pour configurer les fonctions Firebase dans votre environnement local. Sélectionnez les options suivantes lors de l'initialisation de la fonction Firebase dans l'environnement local :

1. Quelles fonctionnalités de l'interface de ligne de commande Firebase souhaitez-vous configurer pour ce dossier ? Appuyez sur Espace pour sélectionner les fonctionnalités, puis sur Entrée pour confirmer vos choix => *Fonctions : Configurer et déployer des fonctions Cloud*

2. Tout d'abord, associons ce répertoire de projet à un projet Firebase ... *=> Utiliser un projet existant*

3. Sélectionnez un projet Firebase par défaut pour ce répertoire => *nom_de_l_application*

4. Quel langage souhaitez-vous utiliser pour écrire des fonctions Cloud ? => *JavaScript*

5. Souhaitez-vous utiliser ESLint pour détecter les bugs probables et imposer un style ? => *N*

6. Souhaitez-vous installer les dépendances avec npm maintenant ? (Y/n) => *Y*

Une fois la configuration terminée, vous recevrez le message suivant :

```shell
✓ Initialisation de Firebase terminée !
```

Voici la structure de notre répertoire une fois l'initialisation terminée :

```shell
+-- firebase.json 
+-- functions
|   +-- index.js
|   +-- node_modules
|   +-- package-lock.json
|   +-- package.json
```

Ouvrez maintenant le fichier `index.js` dans le répertoire des fonctions et copiez-collez le code suivant :

```js
const functions = require('firebase-functions');

exports.helloWorld = functions.https.onRequest((request, response) => {
     response.send("Hello from Firebase!");
});
```

Déployez le code vers les fonctions Firebase en utilisant la commande suivante :

```shell
firebase deploy
```

Une fois le déploiement terminé, vous recevrez la ligne de journal suivante à la fin de votre ligne de commande :

```shell
> ✓ Déploiement terminé !
> Console du projet : https://console.firebase.google.com/project/todoapp-<id>/overview
```

Allez dans **Console du projet > Fonctions** et vous y trouverez l'URL de l'API. L'URL ressemblera à ceci :

```shell
https://<region-d-hebergement>-todoapp-<id>.cloudfunctions.net/helloWorld
```

Copiez cette URL et collez-la dans le navigateur. Vous recevrez la réponse suivante :

```shell
Hello from Firebase!
```

Cela confirme que notre fonction Firebase a été configurée correctement.

### Installer le framework Express :

Maintenant, installons le framework `Express` dans notre projet en utilisant la commande suivante :

```shell
npm i express
```

Maintenant, créons un répertoire **APIs** à l'intérieur du répertoire **functions**. À l'intérieur de ce répertoire, nous créerons un fichier nommé `todos.js`. Supprimez tout du fichier `index.js` et copiez-collez le code suivant :

```js
//index.js

const functions = require('firebase-functions');
const app = require('express')();

const {
    getAllTodos
} = require('./APIs/todos')

app.get('/todos', getAllTodos);
exports.api = functions.https.onRequest(app);
```

Nous avons assigné la fonction getAllTodos à la route **/todos**. Ainsi, tous les appels API sur cette route seront exécutés via la fonction getAllTodos. Allez maintenant dans le fichier `todos.js` sous le répertoire APIs et écrivons la fonction getAllTodos.

```js
//todos.js

exports.getAllTodos = (request, response) => {
    todos = [
        {
            'id': '1',
            'title': 'salutation',
            'body': 'Bonjour le monde de sharvin shah' 
        },
        {
            'id': '2',
            'title': 'salutation2',
            'body': 'Bonjour2 monde2 de sharvin shah' 
        }
    ]
    return response.json(todos);
}
```

Ici, nous avons déclaré un objet JSON d'exemple. Plus tard, nous le dériverons de Firestore. Mais pour l'instant, nous retournerons cela. Déployez maintenant cela vers votre fonction Firebase en utilisant la commande `firebase deploy`. Elle demandera la permission de supprimer le module **helloworld** – entrez simplement **y**.

```shell
Les fonctions suivantes sont trouvées dans votre projet mais n'existent pas dans votre code source local : helloWorld

Souhaitez-vous procéder à la suppression ? Sélectionner non continuera le reste des déploiements. (y/N) y
```

Une fois cela fait, allez dans **Console du projet > Fonctions** et vous y trouverez l'URL de l'API. L'API ressemblera à ceci :

```shell
https://<region-d-hebergement>-todoapp-<id>.cloudfunctions.net/api
```

Maintenant, allez dans le navigateur et copiez-collez l'URL et ajoutez **/todos** à la fin de cette URL. Vous obtiendrez la sortie suivante :

```json
[
        {
            'id': '1',
            'title': 'salutation',
            'body': 'Bonjour le monde de sharvin shah' 
        },
        {
            'id': '2',
            'title': 'salutation2',
            'body': 'Bonjour2 monde2 de sharvin shah' 
        }
]
```

### Firebase Firestore :

Nous allons utiliser une base de données Firestore de Firebase comme base de données en temps réel pour notre application. Allez maintenant dans **Console > Base de données** dans la console Firebase. Pour configurer Firestore, suivez le gif ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Firestore.gif align="left")

*Configuration de Firestore*

Une fois la configuration terminée, cliquez sur le bouton **Démarrer la collection** et définissez **ID de la collection** comme **todos**. Cliquez sur Suivant et vous obtiendrez la fenêtre contextuelle suivante :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/FireStore-collection.png align="left")

*Création de la base de données manuellement*

Ignorez la clé DocumentID. Pour le **champ, type et valeur**, reportez-vous au JSON ci-dessous. Mettez à jour la valeur en conséquence :

```json
{
    Champ : title,
    Type : String,
    Valeur : Bonjour le monde
},
{
    Champ : body,
    Type : String,
    Valeur : Bonjour les gens, j'espère que vous restez à la maison...
},
{
    Champ : createtAt,
    type : timestamp,
    valeur : Ajoutez la date et l'heure actuelles ici
}
```

Appuyez sur le bouton enregistrer. Vous verrez que la collection et le document sont créés. Retournez à l'environnement local. Nous devons installer `firebase-admin` qui contient le package firestore dont nous avons besoin. Utilisez cette commande pour l'installer :

```shell
npm i firebase-admin
```

Créez un répertoire nommé **util** sous le répertoire **functions**. Allez dans ce répertoire et créez un fichier nommé `admin.js`. Dans ce fichier, nous importerons le package firebase admin et initialiserons l'objet de la base de données firestore. Nous l'exporterons afin que d'autres **modules** puissent l'utiliser.

```js
//admin.js

const admin = require('firebase-admin');

admin.initializeApp();

const db = admin.firestore();

module.exports = { admin, db };
```

Maintenant, écrivons une API pour récupérer ces données. Allez dans le fichier `todos.js` sous le répertoire **functions > APIs**. Supprimez l'ancien code et copiez-collez le code ci-dessous :

```js
//todos.js

const { db } = require('../util/admin');

exports.getAllTodos = (request, response) => {
	db
		.collection('todos')
		.orderBy('createdAt', 'desc')
		.get()
		.then((data) => {
			let todos = [];
			data.forEach((doc) => {
				todos.push({
                    todoId: doc.id,
                    title: doc.data().title,
					body: doc.data().body,
					createdAt: doc.data().createdAt,
				});
			});
			return response.json(todos);
		})
		.catch((err) => {
			console.error(err);
			return response.status(500).json({ error: err.code});
		});
};
```

Ici, nous récupérons tous les todos de la base de données et les transmettons au client dans une liste.

Vous pouvez également exécuter l'application localement en utilisant la commande `firebase serve` au lieu de la déployer à chaque fois. Lorsque vous exécutez cette commande, vous pouvez obtenir une erreur concernant les identifiants. Pour la corriger, suivez les étapes mentionnées ci-dessous :

1. Allez dans **Paramètres du projet** (icône des paramètres en haut à gauche)

2. Allez dans l'onglet **comptes de service**

3. En bas, il y aura l'option de **Générer une nouvelle clé**. Cliquez sur cette option et elle téléchargera un fichier avec une extension JSON.

4. Nous devons exporter ces identifiants vers notre session de ligne de commande. Utilisez la commande suivante pour cela :

```shell
export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/[NOM_DU_FICHIER].json"
```

Après cela, exécutez la commande firebase serve. Si vous obtenez toujours l'erreur, utilisez la commande suivante : `firebase login --reauth`. Elle ouvrira la page de connexion Google dans un navigateur. Une fois la connexion effectuée, elle fonctionnera sans aucune erreur.

Vous trouverez une URL dans les journaux de votre outil de ligne de commande lorsque vous exécutez une commande firebase serve. Ouvrez cette URL dans le navigateur et ajoutez `/todos` après celle-ci.

```shell
✓ functions[api]: fonction http initialisée (http://localhost:5000/todoapp-<id-du-projet>/<nom-de-la-région>/api).
```

Vous obtiendrez la sortie JSON suivante dans votre navigateur :

```json
[
    {
        "todoId":"W67t1kSMO0lqvjCIGiuI",
        "title":"Bonjour le monde",
        "body":"Bonjour les gens, j'espère que vous restez à la maison...",
        "createdAt":{"_seconds":1585420200,"_nanoseconds":0 }
    }
]
```

### Écrire d'autres API :

Il est temps d'écrire toutes les autres API todo dont nous aurons besoin pour notre application.

1. **Créer un élément Todo :** Allez dans le fichier `index.js` sous le répertoire des fonctions. Importez la méthode postOneTodo sous la méthode getAllTodos existante. Assignez également la route POST à cette méthode.

```js
//index.js

const {
    ..,
    postOneTodo
} = require('./APIs/todos')

app.post('/todo', postOneTodo);
```

Allez dans le fichier `todos.js` à l'intérieur du répertoire des fonctions et ajoutez une nouvelle méthode `postOneTodo` sous la méthode `getAllTodos` existante.

```js
//todos.js

exports.postOneTodo = (request, response) => {
	if (request.body.body.trim() === '') {
		return response.status(400).json({ body: 'Ne doit pas être vide' });
    }
    
    if(request.body.title.trim() === '') {
        return response.status(400).json({ title: 'Ne doit pas être vide' });
    }
    
    const newTodoItem = {
        title: request.body.title,
        body: request.body.body,
        createdAt: new Date().toISOString()
    }
    db
        .collection('todos')
        .add(newTodoItem)
        .then((doc)=>{
            const responseTodoItem = newTodoItem;
            responseTodoItem.id = doc.id;
            return response.json(responseTodoItem);
        })
        .catch((err) => {
			response.status(500).json({ error: 'Quelque chose s'est mal passé' });
			console.error(err);
		});
};
```

Dans cette méthode, nous ajoutons un nouveau Todo à notre base de données. Si les éléments de notre corps sont vides, nous retournerons une réponse 400, sinon nous ajouterons les données.

Exécutez la commande firebase serve et ouvrez l'application Postman. Créez une nouvelle requête et sélectionnez le type de méthode **POST**. Ajoutez l'URL et un corps de type JSON.

```shell
URL: http://localhost:5000/todoapp-<id-de-l-app>/<nom-de-la-région>/api/todo

MÉTHODE: POST

Corps: {
   "title":"Bonjour le monde",
   "body": "Nous écrivons cette API géniale"
}
```

Appuyez sur le bouton d'envoi et vous obtiendrez la réponse suivante :

```json
{
     "title": "Bonjour le monde",
     "body": "Nous écrivons cette API géniale",
     "createdAt": "2020-03-29T12:30:48.809Z",
     "id": "nh41IgARCj8LPWBYzjU0"
}
```

2. **Supprimer un élément Todo :** Allez dans le fichier `index.js` sous le répertoire des fonctions. Importez la méthode deleteTodo sous la méthode postOneTodo existante. Assignez également la route DELETE à cette méthode.

```js
//index.js

const {
    ..,
    deleteTodo
} = require('./APIs/todos')

app.delete('/todo/:todoId', deleteTodo);
```

Allez dans le fichier `todos.js` et ajoutez une nouvelle méthode `deleteTodo` sous la méthode `postOneTodo` existante.

```js
//todos.js

exports.deleteTodo = (request, response) => {
    const document = db.doc(`/todos/${request.params.todoId}`);
    document
        .get()
        .then((doc) => {
            if (!doc.exists) {
                return response.status(404).json({ error: 'Todo non trouvé' })
            }
            return document.delete();
        })
        .then(() => {
            response.json({ message: 'Suppression réussie' });
        })
        .catch((err) => {
            console.error(err);
            return response.status(500).json({ error: err.code });
        });
};
```

Dans cette méthode, nous supprimons un Todo de notre base de données. Exécutez la commande firebase serve et allez dans Postman. Créez une nouvelle requête, sélectionnez le type de méthode **DELETE** et ajoutez l'URL.

```shell
URL: http://localhost:5000/todoapp-<id-de-l-app>/<nom-de-la-région>/api/todo/<id-du-todo>

MÉTHODE: DELETE
```

Appuyez sur le bouton d'envoi et vous obtiendrez la réponse suivante :

```json
{
   "message": "Suppression réussie"
}
```

3. **Modifier un élément Todo :** Allez dans le fichier `index.js` sous le répertoire des fonctions. Importez la méthode editTodo sous la méthode deleteTodo existante. Assignez également la route PUT à cette méthode.

```js
//index.js

const {
    ..,
    editTodo
} = require('./APIs/todos')

app.put('/todo/:todoId', editTodo);
```

Allez dans le fichier `todos.js` et ajoutez une nouvelle méthode `editTodo` sous la méthode `deleteTodo` existante.

```js
//todos.js

exports.editTodo = ( request, response ) => { 
    if(request.body.todoId || request.body.createdAt){
        response.status(403).json({message: 'Non autorisé à modifier'});
    }
    let document = db.collection('todos').doc(`${request.params.todoId}`);
    document.update(request.body)
    .then(()=> {
        response.json({message: 'Mis à jour avec succès'});
    })
    .catch((err) => {
        console.error(err);
        return response.status(500).json({ 
                error: err.code 
        });
    });
};
```

Dans cette méthode, nous modifions un Todo de notre base de données. Notez ici que nous n'autorisons pas l'utilisateur à modifier les champs todoId ou createdAt. Exécutez la commande firebase serve et allez dans Postman. Créez une nouvelle requête, sélectionnez le type de méthode **PUT**, et ajoutez l'URL.

```shell
URL: http://localhost:5000/todoapp-<id-de-l-app>/<nom-de-la-région>/api/todo/<id-du-todo>

MÉTHODE: PUT
```

Appuyez sur le bouton d'envoi et vous obtiendrez la réponse suivante :

```json
{  
   "message": "Mis à jour avec succès"
}
```

**Structure du répertoire jusqu'à présent :**

```shell
+-- firebase.json 
+-- functions
|   +-- API
|   +-- +-- todos.js
|   +-- util
|   +-- +-- admin.js
|   +-- index.js
|   +-- node_modules
|   +-- package-lock.json
|   +-- package.json
|   +-- .gitignore
```

Avec cela, nous avons terminé la première section de l'application. Vous pouvez prendre une pause, boire un café, et après cela, nous travaillerons sur le développement des API utilisateur.

## Section 2 : Développement des API utilisateur

Dans cette section, nous allons développer ces composants :

1. **API d'authentification utilisateur (connexion et inscription).**

2. **API pour obtenir et mettre à jour les détails de l'utilisateur.**

3. **API pour mettre à jour la photo de profil de l'utilisateur.**

4. **Sécurisation de l'API Todo existante.**

Le code de l'API utilisateur implémenté dans cette section peut être trouvé à ce [commit](https://github.com/Sharvin26/TodoApp/tree/951a8605d988b8e17bd1623eac5c46e449786d1b).

Alors commençons à construire l'API d'authentification utilisateur. Allez dans **Console Firebase > Authentification.**

![Image](https://www.freecodecamp.org/news/content/images/2020/04/FirebaseAuthentication.png align="left")

*Page d'authentification Firebase*

Cliquez sur le bouton **Configurer la méthode de connexion**. Nous utiliserons l'email et le mot de passe pour la validation de l'utilisateur. Activez l'option **Email/Mot de passe.**

![Image](https://www.freecodecamp.org/news/content/images/2020/04/FirebaseAuth1.png align="left")

*Page de configuration de l'inscription Firebase*

Pour l'instant, nous allons créer manuellement notre utilisateur. Tout d'abord, nous allons construire l'API de connexion. Après cela, nous construirons l'API d'inscription.

Allez dans l'onglet Utilisateurs sous Authentification, remplissez les détails de l'utilisateur et cliquez sur le bouton **Ajouter un utilisateur.**

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Login.png align="left")

*Ajout d'un utilisateur manuellement*

### 1. API de connexion utilisateur :

Tout d'abord, nous devons installer le package `firebase`, qui contient la **bibliothèque d'authentification Firebase**, en utilisant la commande suivante :

```shell
npm i firebase
```

Une fois l'installation terminée, allez dans le répertoire **functions > APIs**. Ici, nous créerons un fichier `users.js`. Maintenant, dans `index.js`, nous importons une méthode loginUser et assignons la route POST à celle-ci.

```js
//index.js

const {
    loginUser
} = require('./APIs/users')

// Utilisateurs
app.post('/login', loginUser);
```

Allez dans **Paramètres du projet > Général** et vous y trouverez la carte suivante :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/app.png align="left")

*Obtention de la configuration Firebase*

Sélectionnez l'icône Web, puis suivez le gif ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/project.gif align="left")

Sélectionnez l'option **continuer vers la console**. Une fois cela fait, vous verrez un JSON avec la configuration Firebase. Allez dans le répertoire **functions > util** et créez un fichier `config.js`. Copiez-collez le code suivant dans ce fichier :

```js
// config.js

module.exports = {
    apiKey: "............",
    authDomain: "........",
    databaseURL: "........",
    projectId: ".......",
    storageBucket: ".......",
    messagingSenderId: "........",
    appId: "..........",
    measurementId: "......."
};
```

Remplacez `............` par les valeurs que vous obtenez sous **Console Firebase > Paramètres du projet > Général > vos applications > Extrait SDK Firebase > config**.

Copiez-collez le code suivant dans le fichier `users.js` :

```js
// users.js

const { admin, db } = require('../util/admin');
const config = require('../util/config');

const firebase = require('firebase');

firebase.initializeApp(config);

const { validateLoginData, validateSignUpData } = require('../util/validators');

// Connexion
exports.loginUser = (request, response) => {
    const user = {
        email: request.body.email,
        password: request.body.password
    }

    const { valid, errors } = validateLoginData(user);
	if (!valid) return response.status(400).json(errors);

    firebase
        .auth()
        .signInWithEmailAndPassword(user.email, user.password)
        .then((data) => {
            return data.user.getIdToken();
        })
        .then((token) => {
            return response.json({ token });
        })
        .catch((error) => {
            console.error(error);
            return response.status(403).json({ general: 'Identifiants incorrects, veuillez réessayer' });
        })
};
```

Ici, nous utilisons un module firebase **signInWithEmailAndPassword** pour vérifier si les identifiants soumis par l'utilisateur sont corrects. S'ils sont corrects, nous envoyons le token de cet utilisateur, sinon un statut 403 avec un message "Identifiants incorrects".

Maintenant, créons `validators.js` sous le répertoire **functions > util**. Copiez-collez le code suivant dans ce fichier :

```js
// validators.js

const isEmpty = (string) => {
	if (string.trim() === '') return true;
	else return false;
};

exports.validateLoginData = (data) => {
   let errors = {};
   if (isEmpty(data.email)) errors.email = 'Ne doit pas être vide';
   if (isEmpty(data.password)) errors.password = 'Ne doit pas être vide';
   return {
       errors,
       valid: Object.keys(errors).length === 0 ? true : false
    };
};
```

Avec cela, notre **LoginAPI** est complétée. Exécutez la commande `firebase serve` et allez dans Postman. Créez une nouvelle requête, sélectionnez le type de méthode **POST**, et ajoutez l'URL et le corps.

```shell
URL: http://localhost:5000/todoapp-<id-de-l-app>/<nom-de-la-région>/api/login

MÉTHODE: POST

Corps: {   
    "email":"Ajoutez l'email qui est assigné à l'utilisateur dans la console", 
    "password": "Ajoutez le mot de passe qui est assigné à l'utilisateur dans la console"
}
```

Envoyez la requête dans Postman et vous obtiendrez la sortie suivante :

```json
{   
    "token": ".........."
}
```

Nous utiliserons ce token dans une partie à venir pour **obtenir les détails de l'utilisateur**. N'oubliez pas que ce token expire dans **60 minutes**. Pour générer un nouveau token, utilisez à nouveau cette API.

### 2. API d'inscription utilisateur :

Le mécanisme d'authentification par défaut de Firebase ne vous permet de stocker que des informations comme l'email, le mot de passe, etc. Mais nous avons besoin de plus d'informations pour identifier si cet utilisateur possède ce todo afin qu'il puisse effectuer des opérations de lecture, de mise à jour et de suppression sur celui-ci.

Pour atteindre cet objectif, nous allons créer une nouvelle collection appelée **users**. Sous cette collection, nous stockerons les données de l'utilisateur qui seront mappées au todo en fonction du nom d'utilisateur. Chaque nom d'utilisateur sera unique pour tous les utilisateurs sur la plateforme.

Allez dans `index.js`. Nous importons une méthode signUpUser et assignons la route POST à celle-ci.

```js
//index.js

const {
    ..,
    signUpUser
} = require('./APIs/users')

app.post('/signup', signUpUser);
```

Maintenant, allez dans `validators.js` et ajoutez le code suivant sous la méthode `validateLoginData`.

```js
// validators.js

const isEmail = (email) => {
	const emailRegEx = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
	if (email.match(emailRegEx)) return true;
	else return false;
};

exports.validateSignUpData = (data) => {
	let errors = {};

	if (isEmpty(data.email)) {
		errors.email = 'Ne doit pas être vide';
	} else if (!isEmail(data.email)) {
		errors.email = 'Doit être une adresse email valide';
	}

	if (isEmpty(data.firstName)) errors.firstName = 'Ne doit pas être vide';
	if (isEmpty(data.lastName)) errors.lastName = 'Ne doit pas être vide';
	if (isEmpty(data.phoneNumber)) errors.phoneNumber = 'Ne doit pas être vide';
	if (isEmpty(data.country)) errors.country = 'Ne doit pas être vide';

	if (isEmpty(data.password)) errors.password = 'Ne doit pas être vide';
	if (data.password !== data.confirmPassword) errors.confirmPassword = 'Les mots de passe doivent être identiques';
	if (isEmpty(data.username)) errors.username = 'Ne doit pas être vide';

	return {
		errors,
		valid: Object.keys(errors).length === 0 ? true : false
	};
};
```

Maintenant, allez dans `users.js` et ajoutez le code suivant sous le module `loginUser`.

```js
// users.js

exports.signUpUser = (request, response) => {
    const newUser = {
        firstName: request.body.firstName,
        lastName: request.body.lastName,
        email: request.body.email,
        phoneNumber: request.body.phoneNumber,
        country: request.body.country,
		password: request.body.password,
		confirmPassword: request.body.confirmPassword,
		username: request.body.username
    };

    const { valid, errors } = validateSignUpData(newUser);

	if (!valid) return response.status(400).json(errors);

    let token, userId;
    db
        .doc(`/users/${newUser.username}`)
        .get()
        .then((doc) => {
            if (doc.exists) {
                return response.status(400).json({ username: 'ce nom d\'utilisateur est déjà pris' });
            } else {
                return firebase
                        .auth()
                        .createUserWithEmailAndPassword(
                            newUser.email, 
                            newUser.password
                    );
            }
        })
        .then((data) => {
            userId = data.user.uid;
            return data.user.getIdToken();
        })
        .then((idtoken) => {
            token = idtoken;
            const userCredentials = {
                firstName: newUser.firstName,
                lastName: newUser.lastName,
                username: newUser.username,
                phoneNumber: newUser.phoneNumber,
                country: newUser.country,
                email: newUser.email,
                createdAt: new Date().toISOString(),
                userId
            };
            return db
                    .doc(`/users/${newUser.username}`)
                    .set(userCredentials);
        })
        .then(()=>{
            return response.status(201).json({ token });
        })
        .catch((err) => {
			console.error(err);
			if (err.code === 'auth/email-already-in-use') {
				return response.status(400).json({ email: 'Email déjà utilisé' });
			} else {
				return response.status(500).json({ general: 'Quelque chose s\'est mal passé, veuillez réessayer' });
			}
		});
}
```

Nous validons nos données utilisateur, et après cela, nous envoyons un email et un mot de passe au module **createUserWithEmailAndPassword** de Firebase pour créer l'utilisateur. Une fois l'utilisateur créé avec succès, nous enregistrons les identifiants de l'utilisateur dans la base de données.

Avec cela, notre **API d'inscription** est complétée. Exécutez la commande `firebase serve` et allez dans Postman. Créez une nouvelle requête, sélectionnez le type de méthode **POST**. Ajoutez l'URL et le corps.

```shell
URL: http://localhost:5000/todoapp-<id-de-l-app>/<nom-de-la-région>/api/signup

MÉTHODE: POST

Corps: {
   "firstName": "Ajoutez un prénom ici",
   "lastName": "Ajoutez un nom de famille ici",
   "email":"Ajoutez un email ici",
   "phoneNumber": "Ajoutez un numéro de téléphone ici",
   "country": "Ajoutez un pays ici",
   "password": "Ajoutez un mot de passe ici",
   "confirmPassword": "Ajoutez le même mot de passe ici",
   "username": "Ajoutez un nom d'utilisateur unique ici"
}
```

Appuyez sur le bouton d'envoi de la requête dans Postman et vous obtiendrez la sortie suivante :

```json
{   
    "token": ".........."
}
```

Maintenant, allez dans **Console Firebase > Base de données** et vous y verrez la sortie suivante :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/database.png align="left")

Comme vous pouvez le voir, notre collection d'utilisateurs est créée avec succès avec un document.

### 3. Télécharger la photo de profil de l'utilisateur :

Nos utilisateurs pourront télécharger leur photo de profil. Pour y parvenir, nous utiliserons le bucket de stockage. Allez dans **Console Firebase > Stockage** et cliquez sur le bouton **Commencer**. Suivez le GIF ci-dessous pour la configuration :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/storage.gif align="left")

Maintenant, allez dans l'onglet **Règles** sous Stockage et mettez à jour la permission pour l'accès au bucket comme indiqué dans l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/storageRule.png align="left")

Pour télécharger la photo de profil, nous utiliserons le package nommé `busboy`. Pour installer ce package, utilisez la commande suivante :

```shell
npm i busboy
```

Allez dans `index.js`. Importez la méthode uploadProfilePhoto sous la méthode signUpUser existante. Assignez également la route POST à cette méthode.

```js
//index.js

const auth = require('./util/auth');

const {
    ..,
    uploadProfilePhoto
} = require('./APIs/users')

app.post('/user/image', auth, uploadProfilePhoto);
```

Ici, nous avons ajouté une couche d'authentification afin que seul un utilisateur associé à ce compte puisse télécharger l'image. Maintenant, créez un fichier nommé `auth.js` dans le répertoire **functions > utils**. Copiez-collez le code suivant dans ce fichier :

```js
// auth.js

const { admin, db } = require('./admin');

module.exports = (request, response, next) => {
	let idToken;
	if (request.headers.authorization && request.headers.authorization.startsWith('Bearer ')) {
		idToken = request.headers.authorization.split('Bearer ')[1];
	} else {
		console.error('Aucun token trouvé');
		return response.status(403).json({ error: 'Non autorisé' });
	}
	admin
		.auth()
		.verifyIdToken(idToken)
		.then((decodedToken) => {
			request.user = decodedToken;
			return db.collection('users').where('userId', '==', request.user.uid).limit(1).get();
		})
		.then((data) => {
			request.user.username = data.docs[0].data().username;
			request.user.imageUrl = data.docs[0].data().imageUrl;
			return next();
		})
		.catch((err) => {
			console.error('Erreur lors de la vérification du token', err);
			return response.status(403).json(err);
		});
};
```

Ici, nous utilisons le module **verifyIdToken** de Firebase pour vérifier le token. Après cela, nous décodons les détails de l'utilisateur et les passons dans la requête existante.

Allez dans `users.js` et ajoutez le code suivant sous la méthode `signup` :

```js
// users.js

deleteImage = (imageName) => {
    const bucket = admin.storage().bucket();
    const path = `${imageName}`
    return bucket.file(path).delete()
    .then(() => {
        return
    })
    .catch((error) => {
        return
    })
}

// Télécharger la photo de profil
exports.uploadProfilePhoto = (request, response) => {
    const BusBoy = require('busboy');
	const path = require('path');
	const os = require('os');
	const fs = require('fs');
	const busboy = new BusBoy({ headers: request.headers });

	let imageFileName;
	let imageToBeUploaded = {};

	busboy.on('file', (fieldname, file, filename, encoding, mimetype) => {
		if (mimetype !== 'image/png' && mimetype !== 'image/jpeg') {
			return response.status(400).json({ error: 'Mauvais type de fichier soumis' });
		}
		const imageExtension = filename.split('.')[filename.split('.').length - 1];
        imageFileName = `${request.user.username}.${imageExtension}`;
		const filePath = path.join(os.tmpdir(), imageFileName);
		imageToBeUploaded = { filePath, mimetype };
		file.pipe(fs.createWriteStream(filePath));
    });
    deleteImage(imageFileName);
	busboy.on('finish', () => {
		admin
			.storage()
			.bucket()
			.upload(imageToBeUploaded.filePath, {
				resumable: false,
				metadata: {
					metadata: {
						contentType: imageToBeUploaded.mimetype
					}
				}
			})
			.then(() => {
				const imageUrl = `https://firebasestorage.googleapis.com/v0/b/${config.storageBucket}/o/${imageFileName}?alt=media`;
				return db.doc(`/users/${request.user.username}`).update({
					imageUrl
				});
			})
			.then(() => {
				return response.json({ message: 'Image téléchargée avec succès' });
			})
			.catch((error) => {
				console.error(error);
				return response.status(500).json({ error: error.code });
			});
	});
	busboy.end(request.rawBody);
};
```

Avec cela, notre **API de téléchargement de photo de profil** est complétée. Exécutez la commande `firebase serve` et allez dans Postman. Créez une nouvelle requête, sélectionnez le type de méthode **POST**, ajoutez l'URL, et dans la section du corps, sélectionnez le type comme form-data.

La requête est protégée, vous devrez donc également envoyer le **jeton porteur**. Pour envoyer le jeton porteur, connectez-vous à nouveau si le jeton a expiré. Après cela, dans **Application Postman > Onglet Autorisation > Type > Jeton Porteur** et dans la section jeton, collez le jeton.

```shell
URL: http://localhost:5000/todoapp-<id-de-l-app>/<nom-de-la-région>/api/user/image

MÉTHODE: GET

Corps: { RÉFÉREZ-VOUS À L'IMAGE ci-dessous }
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/cover.png align="left")

Appuyez sur le bouton d'envoi de la requête dans Postman et vous obtiendrez la sortie suivante :

```json
{        
    "message": "Image téléchargée avec succès"
}
```

### 4. Obtenir les détails de l'utilisateur :

Ici, nous récupérons les données de notre utilisateur depuis la base de données. Allez dans `index.js` et importez la méthode getUserDetail et assignez la route GET à celle-ci.

```js
// index.js

const {
    ..,
    getUserDetail
} = require('./APIs/users')

app.get('/user', auth, getUserDetail);
```

Maintenant, allez dans `users.js` et ajoutez le code suivant après le module `uploadProfilePhoto` :

```js
// users.js

exports.getUserDetail = (request, response) => {
    let userData = {};
	db
		.doc(`/users/${request.user.username}`)
		.get()
		.then((doc) => {
			if (doc.exists) {
                userData.userCredentials = doc.data();
                return response.json(userData);
			}	
		})
		.catch((error) => {
			console.error(error);
			return response.status(500).json({ error: error.code });
		});
}
```

Nous utilisons le module **doc().get()** de Firebase pour obtenir les détails de l'utilisateur. Avec cela, notre **API Obtenir les détails de l'utilisateur** est complétée. Exécutez la commande `firebase serve` et allez dans Postman. Créez une nouvelle requête, sélectionnez le type de méthode : **GET**, et ajoutez l'URL et le corps.

La requête est protégée, vous devrez donc également envoyer le **jeton porteur**. Pour envoyer le jeton porteur, connectez-vous à nouveau si le jeton a expiré.

```shell
URL: http://localhost:5000/todoapp-<id-de-l-app>/<nom-de-la-région>/api/user
MÉTHODE: GET
```

Appuyez sur le bouton d'envoi de la requête dans Postman et vous obtiendrez la sortie suivante :

```json
{
   "userCredentials": {
       "phoneNumber": "........",
       "email": "........",
       "country": "........",
       "userId": "........",
       "username": "........",
       "createdAt": "........",
       "lastName": "........",
       "firstName": "........"
    }
}
```

### 5. Mettre à jour les détails de l'utilisateur :

Maintenant, ajoutons la fonctionnalité pour mettre à jour les détails de l'utilisateur. Allez dans `index.js` et copiez-collez le code suivant :

```js
// index.js

const {
    ..,
    updateUserDetails
} = require('./APIs/users')

app.post('/user', auth, updateUserDetails);
```

Maintenant, allez dans `users.js` et ajoutez le module `updateUserDetails` sous le module `getUserDetails` existant :

```js
// users.js

exports.updateUserDetails = (request, response) => {
    let document = db.collection('users').doc(`${request.user.username}`);
    document.update(request.body)
    .then(()=> {
        response.json({message: 'Mis à jour avec succès'});
    })
    .catch((error) => {
        console.error(error);
        return response.status(500).json({ 
            message: "Impossible de mettre à jour la valeur"
        });
    });
}
```

Ici, nous utilisons la méthode **update** de Firebase. Avec cela, notre **API Mettre à jour les détails de l'utilisateur** est complétée. Suivez la même procédure pour une requête comme avec l'API Obtenir les détails de l'utilisateur ci-dessus avec un changement. Ajoutez un corps dans la requête ici et la méthode comme POST.

```shell
URL: http://localhost:5000/todoapp-<id-de-l-app>/<nom-de-la-région>/api/user

MÉTHODE: POST

Corps : {
    // Vous pouvez modifier le prénom, le nom et le pays
    // Nous désactiverons les autres balises de formulaire de notre UI
}
```

Appuyez sur le bouton d'envoi de la requête dans Postman et vous obtiendrez la sortie suivante :

```json
{
    "message": "Mis à jour avec succès"
}
```

### 6. Sécuriser les API Todo :

Pour sécuriser l'API Todo afin que seul l'utilisateur choisi puisse y accéder, nous apporterons quelques modifications à notre code existant. Tout d'abord, nous mettrons à jour notre `index.js` comme suit :

```js
// index.js

// Todos
app.get('/todos', auth, getAllTodos);
app.get('/todo/:todoId', auth, getOneTodo);
app.post('/todo',auth, postOneTodo);
app.delete('/todo/:todoId',auth, deleteTodo);
app.put('/todo/:todoId',auth, editTodo);
```

Nous avons mis à jour toutes les **routes Todo** en ajoutant `auth` afin que tous les appels API nécessitent un token et ne puissent être accessibles que par l'utilisateur particulier.

Après cela, allez dans `todos.js` sous le répertoire **functions > APIs**.

1. **Créer une API Todo :** Ouvrez `todos.js` et sous la méthode **postOneTodo**, ajoutez la clé username comme suit :

```js
const newTodoItem = {
     ..,
     username: request.user.username,
     ..
}
```

2. **Obtenir toutes les API Todos :** Ouvrez `todos.js` et sous la méthode **getAllTodos**, ajoutez la clause where comme suit :

```js
db
.collection('todos')
.where('username', '==', request.user.username)
.orderBy('createdAt', 'desc')
```

Exécutez firebase serve et testez notre API GET. **N'oubliez pas d'envoyer le jeton porteur.** Ici, vous obtiendrez une erreur de réponse comme suit :

```json
{   
    "error": 9
}
```

Allez dans la ligne de commande et vous verrez les lignes suivantes enregistrées :

```shell
i  functions: Début de l'exécution de "api">  Erreur: 9 FAILED_PRECONDITION: La requête nécessite un index. Vous pouvez le créer ici: <URL>>      at callErrorFromStatus
```

Ouvrez cela dans le navigateur et cliquez sur créer un index.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/index.png align="left")

Une fois l'index construit, envoyez à nouveau la requête et vous obtiendrez la sortie suivante :

```json
[
   {
      "todoId": "......",
      "title": "......",
      "username": "......",
      "body": "......",
      "createdAt": "2020-03-30T13:01:58.478Z"
   }
]
```

3. **Supprimer l'API Todo :** Ouvrez `todos.js` et sous la méthode **deleteTodo**, ajoutez la condition suivante. Ajoutez cette condition à l'intérieur de la requête **document.get().then()** sous la condition **!doc.exists**.

```js
..
if(doc.data().username !== request.user.username){
     return response.status(403).json({error:"Non autorisé"})
}
```

### Structure du répertoire jusqu'à présent :

```shell
+-- firebase.json 
+-- functions
|   +-- API
|   +-- +-- todos.js 
|   +-- +-- users.js
|   +-- util
|   +-- +-- admin.js
|   +-- +-- auth.js
|   +-- +-- validators.js
|   +-- index.js
|   +-- node_modules
|   +-- package-lock.json
|   +-- package.json
|   +-- .gitignore
```

Avec cela, nous avons terminé notre backend API. Prenez une pause, buvez un café, et après cela, nous commencerons à construire le front-end de notre application.

## Section 3 : Tableau de bord utilisateur

Dans cette section, nous allons développer ces composants :

1. **Configurer ReactJS et Material UI.**

2. **Construire les formulaires de connexion et d'inscription.**

3. **Construire la section Compte.**

Le code du tableau de bord utilisateur implémenté dans cette section peut être trouvé à ce [commit](https://github.com/Sharvin26/TodoApp/tree/2b207786651167c1ed5327c2c8583e97080abb54/view).

### 1. Configurer ReactJS et Material UI :

Nous allons utiliser le modèle create-react-app. Il nous donne une structure fondamentale pour développer l'application. Pour l'installer, utilisez la commande suivante :

```shell
npm install -g create-react-app
```

Allez dans le dossier racine du projet où se trouve le répertoire des fonctions. Initialisez notre application front-end en utilisant la commande suivante :

```shell
create-react-app view
```

N'oubliez pas d'utiliser la version **v16.13.1** de la bibliothèque ReactJS.

Une fois l'installation terminée, vous verrez ce qui suit dans vos journaux de ligne de commande :

```shell
cd view
  npm start
Bon codage !
```

Avec cela, nous avons configuré notre application React. Vous obtiendrez la structure de répertoire suivante :

```shell
+-- firebase.json 
+-- functions { Ce répertoire contient notre logique API }
+-- view { Ce répertoire contient nos composants FrontEnd }
+-- .firebaserc
+-- .gitignore
```

Maintenant, exécutez l'application en utilisant la commande `npm start`. Allez dans le navigateur sur `[http://localhost:3000/](http://localhost:3000/)` et vous verrez la sortie suivante :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/React1.png align="left")

Maintenant, nous allons supprimer tous les composants inutiles. Allez dans le répertoire view et supprimez tous les fichiers qui ont **[ Supprimer ]** devant eux. **Pour cela, reportez-vous à la structure de l'arborescence du répertoire ci-dessous.**

```shell
+-- README.md [ Supprimer ]
+-- package-lock.json
+-- package.json
+-- node_modules
+-- .gitignore
+-- public
|   +-- favicon.ico [ Supprimer ]
|   +-- index.html
|   +-- logo192.png [ Supprimer ]
|   +-- logo512.png [ Supprimer ]
|   +-- manifest.json
|   +-- robots.txt
+-- src
|   +-- App.css
|   +-- App.test.js
|   +-- index.js
|   +-- serviceWorker.js
|   +-- App.js
|   +-- index.css [ Supprimer ]
|   +-- logo.svg [ Supprimer ]
|   +-- setupTests.js
```

Allez dans `index.html` sous le répertoire public et supprimez les lignes suivantes :

```html
<link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
<link rel="apple-touch-icon" href="%PUBLIC_URL%/logo192.png" />
<link rel="manifest" href="%PUBLIC_URL%/manifest.json" />
```

Maintenant, allez dans `App.js` sous le répertoire src et remplacez l'ancien code par le code suivant :

```js
import React from 'react';
function App() {
  return (
    <div>
    </div>
  );
}
export default App;
```

Allez dans `index.js` et supprimez l'importation suivante :

```python
import './index.css'
```

Je n'ai pas supprimé `App.css` et je ne l'utilise pas dans cette application. Mais si vous souhaitez le supprimer ou l'utiliser, vous êtes libre de le faire.

Allez dans le navigateur sur `[http://localhost:3000/](http://localhost:3000/)` et vous obtiendrez un écran vide.

Pour installer Material UI, allez dans le répertoire view et copiez-collez cette commande dans le terminal :

```shell
npm install @material-ui/core
```

N'oubliez pas d'utiliser la version **v4.9.8** de la bibliothèque Material UI.

### 2. Formulaire de connexion :

Pour développer le formulaire de connexion, allez dans `App.js`. En haut de `App.js`, ajoutez les imports suivants :

```js
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import login from './pages/login';
```

Nous utilisons **Switch** et **Route** pour assigner des routes à notre TodoApp. Pour l'instant, nous ajouterons uniquement la route **/login** et assignerons un composant de connexion à celle-ci.

```html
// App.js

<Router>
    <div>
       <Switch>
           <Route exact path="/login" component={login}/>
       </Switch>
    </div>
</Router>
```

Créez un répertoire **pages** sous le répertoire **view** existant et un fichier nommé `login.js` sous le répertoire **pages**.

Nous importerons les composants Material UI et le package Axios dans le fichier `login.js` :

```js
// login.js

// Composants Material UI
import React, { Component } from 'react';
import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
import Link from '@material-ui/core/Link';
import Grid from '@material-ui/core/Grid';
import LockOutlinedIcon from '@material-ui/icons/LockOutlined';
import Typography from '@material-ui/core/Typography';
import withStyles from '@material-ui/core/styles/withStyles';
import Container from '@material-ui/core/Container';
import CircularProgress from '@material-ui/core/CircularProgress';

import axios from 'axios';
```

Nous ajouterons les styles suivants à notre page de connexion :

```js
// login.js

const styles = (theme) => ({
	paper: {
		marginTop: theme.spacing(8),
		display: 'flex',
		flexDirection: 'column',
		alignItems: 'center'
	},
	avatar: {
		margin: theme.spacing(1),
		backgroundColor: theme.palette.secondary.main
	},
	form: {
		width: '100%',
		marginTop: theme.spacing(1)
	},
	submit: {
		margin: theme.spacing(3, 0, 2)
	},
	customError: {
		color: 'red',
		fontSize: '0.8rem',
		marginTop: 10
	},
	progess: {
		position: 'absolute'
	}
});
```

Nous allons créer une classe nommée login qui contient un formulaire et un gestionnaire de soumission à l'intérieur.

```js
// login.js

class login extends Component {
	constructor(props) {
		super(props);

		this.state = {
			email: '',
			password: '',
			errors: [],
			loading: false
		};
	}

	componentWillReceiveProps(nextProps) {
		if (nextProps.UI.errors) {
			this.setState({
				errors: nextProps.UI.errors
			});
		}
	}

	handleChange = (event) => {
		this.setState({
			[event.target.name]: event.target.value
		});
	};

	handleSubmit = (event) => {
		event.preventDefault();
		this.setState({ loading: true });
		const userData = {
			email: this.state.email,
			password: this.state.password
		};
		axios
			.post('/login', userData)
			.then((response) => {
				localStorage.setItem('AuthToken', `Bearer ${response.data.token}`);
				this.setState({ 
					loading: false,
				});		
				this.props.history.push('/');
			})
			.catch((error) => {				
				this.setState({
					errors: error.response.data,
					loading: false
				});
			});
	};

	render() {
		const { classes } = this.props;
		const { errors, loading } = this.state;
		return (
			<Container component="main" maxWidth="xs">
				<CssBaseline />
				<div className={classes.paper}>
					<Avatar className={classes.avatar}>
						<LockOutlinedIcon />
					</Avatar>
					<Typography component="h1" variant="h5">
						Connexion
					</Typography>
					<form className={classes.form} noValidate>
						<TextField
							variant="outlined"
							margin="normal"
							required
							fullWidth
							id="email"
							label="Adresse Email"
							name="email"
							autoComplete="email"
							autoFocus
							helperText={errors.email}
							error={errors.email ? true : false}
							onChange={this.handleChange}
						/>
						<TextField
							variant="outlined"
							margin="normal"
							required
							fullWidth
							name="password"
							label="Mot de passe"
							type="password"
							id="password"
							autoComplete="current-password"
							helperText={errors.password}
							error={errors.password ? true : false}
							onChange={this.handleChange}
						/>
						<Button
							type="submit"
							fullWidth
							variant="contained"
							color="primary"
							className={classes.submit}
							onClick={this.handleSubmit}
							disabled={loading || !this.state.email || !this.state.password}
						>
							Se connecter
							{loading && <CircularProgress size={30} className={classes.progess} />}
						</Button>
						<Grid container>
							<Grid item>
								<Link href="signup" variant="body2">
									{"Vous n'avez pas de compte ? Inscrivez-vous"}
								</Link>
							</Grid>
						</Grid>
						{errors.general && (
							<Typography variant="body2" className={classes.customError}>
								{errors.general}
							</Typography>
						)}
					</form>
				</div>
			</Container>
		);
	}
}
```

À la fin de ce fichier, ajoutez l'exportation suivante :

```js
export default withStyles(styles)(login);
```

Ajoutez l'URL de nos fonctions Firebase à **view > package.json** comme suit :

> Rappelez-vous : Ajoutez une clé nommée **proxy** sous l'objet JSON browserslist existant

```json
"proxy": "https://<nom-de-la-région>-todoapp-<id>.cloudfunctions.net/api"
```

Installez les packages **Axios** et **material icon** en utilisant les commandes suivantes :

```shell
// Commande Axios :
npm i axios
// Icônes Material :
npm install @material-ui/icons
```

Nous avons ajouté une route de connexion dans `App.js`. Dans `login.js`, nous avons créé un composant de classe qui gère l'état, envoie la requête post à l'API de connexion en utilisant le package Axios. Si la requête est réussie, nous stockons le token. Si nous obtenons des erreurs dans la réponse, nous les affichons simplement sur l'UI.

Allez dans le navigateur à `[http://localhost:3000/login](http://localhost:3000/login)` et vous verrez l'UI de connexion suivante.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/LoginPage.png align="left")

*Page de connexion*

Essayez de remplir de mauvaises informations d'identification ou d'envoyer une requête vide et vous obtiendrez les erreurs. Envoyez une requête valide. Allez dans **Console de développement > Application**. Vous verrez que le token de l'utilisateur est stocké dans le stockage local. Une fois la connexion réussie, nous serons redirigés vers la page d'accueil.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/loginDev.png align="left")

*Console de développement Google Chrome*

### 3. Formulaire d'inscription :

Pour développer le formulaire d'inscription, allez dans `App.js` et mettez à jour le composant `Route` existant avec la ligne ci-dessous :

```js
// App.js

<Route exact path="/signup" component={signup}/>
```

N'oubliez pas d'importer :

```js
// App.js

import signup from './pages/signup';
```

Créez un fichier nommé `signup.js` sous le **répertoire des pages**.

À l'intérieur de signup.js, nous importerons les packages Material UI et Axios :

```js
// signup.js

import React, { Component } from 'react';
import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
import Link from '@material-ui/core/Link';
import Grid from '@material-ui/core/Grid';
import LockOutlinedIcon from '@material-ui/icons/LockOutlined';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';
import withStyles from '@material-ui/core/styles/withStyles';
import CircularProgress from '@material-ui/core/CircularProgress';

import axios from 'axios';
```

Nous ajouterons les styles suivants à notre page d'inscription :

```js
// signup.js


const styles = (theme) => ({
	paper: {
		marginTop: theme.spacing(8),
		display: 'flex',
		flexDirection: 'column',
		alignItems: 'center'
	},
	avatar: {
		margin: theme.spacing(1),
		backgroundColor: theme.palette.secondary.main
	},
	form: {
		width: '100%', // Correction du problème IE 11.
		marginTop: theme.spacing(3)
	},
	submit: {
		margin: theme.spacing(3, 0, 2)
	},
	progess: {
		position: 'absolute'
	}
});
```

Nous allons créer une classe nommée signup qui contient un formulaire et un gestionnaire de soumission à l'intérieur.

```js
// signup.js

class signup extends Component {
	constructor(props) {
		super(props);

		this.state = {
			firstName: '',
			lastName: '',
			phoneNumber: '',
			country: '',
			username: '',
			email: '',
			password: '',
			confirmPassword: '',
			errors: [],
			loading: false
		};
	}

	componentWillReceiveProps(nextProps) {
		if (nextProps.UI.errors) {
			this.setState({
				errors: nextProps.UI.errors
			});
		}
	}

	handleChange = (event) => {
		this.setState({
			[event.target.name]: event.target.value
		});
	};

	handleSubmit = (event) => {
		event.preventDefault();
		this.setState({ loading: true });
		const newUserData = {
			firstName: this.state.firstName,
			lastName: this.state.lastName,
			phoneNumber: this.state.phoneNumber,
			country: this.state.country,
			username: this.state.username,
			email: this.state.email,
			password: this.state.password,
			confirmPassword: this.state.confirmPassword
		};
		axios
			.post('/signup', newUserData)
			.then((response) => {
				localStorage.setItem('AuthToken', `${response.data.token}`);
				this.setState({ 
					loading: false,
				});	
				this.props.history.push('/');
			})
			.catch((error) => {
				this.setState({
					errors: error.response.data,
					loading: false
				});
			});
	};

	render() {
		const { classes } = this.props;
		const { errors, loading } = this.state;
		return (
			<Container component="main" maxWidth="xs">
				<CssBaseline />
				<div className={classes.paper}>
					<Avatar className={classes.avatar}>
						<LockOutlinedIcon />
					</Avatar>
					<Typography component="h1" variant="h5">
						Inscription
					</Typography>
					<form className={classes.form} noValidate>
						<Grid container spacing={2}>
							<Grid item xs={12} sm={6}>
								<TextField
									variant="outlined"
									required
									fullWidth
									id="firstName"
									label="Prénom"
									name="firstName"
									autoComplete="firstName"
									helperText={errors.firstName}
									error={errors.firstName ? true : false}
									onChange={this.handleChange}
								/>
							</Grid>
							<Grid item xs={12} sm={6}>
								<TextField
									variant="outlined"
									required
									fullWidth
									id="lastName"
									label="Nom de famille"
									name="lastName"
									autoComplete="lastName"
									helperText={errors.lastName}
									error={errors.lastName ? true : false}
									onChange={this.handleChange}
								/>
							</Grid>

							<Grid item xs={12} sm={6}>
								<TextField
									variant="outlined"
									required
									fullWidth
									id="username"
									label="Nom d'utilisateur"
									name="username"
									autoComplete="username"
									helperText={errors.username}
									error={errors.username ? true : false}
									onChange={this.handleChange}
								/>
							</Grid>

							<Grid item xs={12} sm={6}>
								<TextField
									variant="outlined"
									required
									fullWidth
									id="phoneNumber"
									label="Numéro de téléphone"
									name="phoneNumber"
									autoComplete="phoneNumber"
									pattern="[7-9]{1}[0-9]{9}"
									helperText={errors.phoneNumber}
									error={errors.phoneNumber ? true : false}
									onChange={this.handleChange}
								/>
							</Grid>

							<Grid item xs={12}>
								<TextField
									variant="outlined"
									required
									fullWidth
									id="email"
									label="Adresse Email"
									name="email"
									autoComplete="email"
									helperText={errors.email}
									error={errors.email ? true : false}
									onChange={this.handleChange}
								/>
							</Grid>

							<Grid item xs={12}>
								<TextField
									variant="outlined"
									required
									fullWidth
									id="country"
									label="Pays"
									name="country"
									autoComplete="country"
									helperText={errors.country}
									error={errors.country ? true : false}
									onChange={this.handleChange}
								/>
							</Grid>

							<Grid item xs={12}>
								<TextField
									variant="outlined"
									required
									fullWidth
									name="password"
									label="Mot de passe"
									type="password"
									id="password"
									autoComplete="current-password"
									helperText={errors.password}
									error={errors.password ? true : false}
									onChange={this.handleChange}
								/>
							</Grid>
							<Grid item xs={12}>
								<TextField
									variant="outlined"
									required
									fullWidth
									name="confirmPassword"
									label="Confirmer le mot de passe"
									type="password"
									id="confirmPassword"
									autoComplete="current-password"
									onChange={this.handleChange}
								/>
							</Grid>
						</Grid>
						<Button
							type="submit"
							fullWidth
							variant="contained"
							color="primary"
							className={classes.submit}
							onClick={this.handleSubmit}
                            disabled={loading || 
                                !this.state.email || 
                                !this.state.password ||
                                !this.state.firstName || 
                                !this.state.lastName ||
                                !this.state.country || 
                                !this.state.username || 
                                !this.state.phoneNumber}
						>
							S'inscrire
							{loading && <CircularProgress size={30} className={classes.progess} />}
						</Button>
						<Grid container justify="flex-end">
							<Grid item>
								<Link href="login" variant="body2">
									Déjà un compte ? Connectez-vous
								</Link>
							</Grid>
						</Grid>
					</form>
				</div>
			</Container>
		);
	}
}
```

À la fin de ce fichier, ajoutez l'exportation suivante :

```js
export default withStyles(styles)(signup);
```

La logique pour le composant Signup est la même que pour le composant de connexion. Allez dans le navigateur à `[http://localhost:3000/signup](http://localhost:3000/signup)` et vous verrez l'UI d'inscription suivante. Une fois l'inscription réussie, nous serons redirigés vers la page d'accueil.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/SignupPage.png align="left")

*Formulaire d'inscription*

Essayez de remplir de mauvaises informations d'identification ou d'envoyer une requête vide et vous obtiendrez les erreurs. Envoyez une requête valide. Allez dans **Console de développement > Application**. Vous verrez que le token de l'utilisateur est stocké dans le stockage local.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/DevConsoleSignup.png align="left")

*Console de développement Chrome*

### 4. Section Compte :

Pour construire la page de compte, nous devons d'abord créer notre **page d'accueil** à partir de laquelle nous chargerons la **section compte**. Allez dans `App.js` et mettez à jour la route suivante :

```js
// App.js

<Route exact path="/" component={home}/>
```

N'oubliez pas l'importation :

```js
// App.js

import home from './pages/home';
```

Créez un nouveau fichier nommé `home.js`. Ce fichier sera l'index de notre application. Les sections Compte et Todo se chargent toutes deux sur cette page en fonction du clic sur le bouton.

Importez les packages Material UI, le package Axios, nos composants personnalisés Account, todo et le middleware auth.

```js
// home.js

import React, { Component } from 'react';
import axios from 'axios';

import Account from '../components/account';
import Todo from '../components/todo';

import Drawer from '@material-ui/core/Drawer';
import AppBar from '@material-ui/core/AppBar';
import CssBaseline from '@material-ui/core/CssBaseline';
import Toolbar from '@material-ui/core/Toolbar';
import List from '@material-ui/core/List';
import Typography from '@material-ui/core/Typography';
import Divider from '@material-ui/core/Divider';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import withStyles from '@material-ui/core/styles/withStyles';
import AccountBoxIcon from '@material-ui/icons/AccountBox';
import NotesIcon from '@material-ui/icons/Notes';
import Avatar from '@material-ui/core/avatar';
import ExitToAppIcon from '@material-ui/icons/ExitToApp';
import CircularProgress from '@material-ui/core/CircularProgress';

import { authMiddleWare } from '../util/auth'
```

Nous définirons notre drawerWidth comme suit :

```js
const drawerWidth = 240;
```

Nous ajouterons le style suivant à notre page d'accueil :

```js
const styles = (theme) => ({
	root: {
		display: 'flex'
	},
	appBar: {
		zIndex: theme.zIndex.drawer + 1
	},
	drawer: {
		width: drawerWidth,
		flexShrink: 0
	},
	drawerPaper: {
		width: drawerWidth
	},
	content: {
		flexGrow: 1,
		padding: theme.spacing(3)
	},
	avatar: {
		height: 110,
		width: 100,
		flexShrink: 0,
		flexGrow: 0,
		marginTop: 20
	},
	uiProgess: {
		position: 'fixed',
		zIndex: '1000',
		height: '31px',
		width: '31px',
		left: '50%',
		top: '35%'
	},
	toolbar: theme.mixins.toolbar
});
```

Nous allons créer une classe nommée home. Cette classe aura un appel API pour obtenir la photo de profil de l'utilisateur, le prénom et le nom de famille. Elle aura également une logique pour choisir quel composant afficher, soit Todo soit Account :

```js
class home extends Component {
	state = {
		render: false
	};

	loadAccountPage = (event) => {
		this.setState({ render: true });
	};

	loadTodoPage = (event) => {
		this.setState({ render: false });
	};

	logoutHandler = (event) => {
		localStorage.removeItem('AuthToken');
		this.props.history.push('/login');
	};

	constructor(props) {
		super(props);

		this.state = {
			firstName: '',
			lastName: '',
			profilePicture: '',
			uiLoading: true,
			imageLoading: false
		};
	}

	componentWillMount = () => {
		authMiddleWare(this.props.history);
		const authToken = localStorage.getItem('AuthToken');
		axios.defaults.headers.common = { Authorization: `${authToken}` };
		axios
			.get('/user')
			.then((response) => {
				console.log(response.data);
				this.setState({
					firstName: response.data.userCredentials.firstName,
					lastName: response.data.userCredentials.lastName,
					email: response.data.userCredentials.email,
					phoneNumber: response.data.userCredentials.phoneNumber,
					country: response.data.userCredentials.country,
					username: response.data.userCredentials.username,
					uiLoading: false,
					profilePicture: response.data.userCredentials.imageUrl
				});
			})
			.catch((error) => {
				if(error.response.status === 403) {
					this.props.history.push('/login')
				}
				console.log(error);
				this.setState({ errorMsg: 'Erreur lors de la récupération des données' });
			});
	};

	render() {
		const { classes } = this.props;		
		if (this.state.uiLoading === true) {
			return (
				<div className={classes.root}>
					{this.state.uiLoading && <CircularProgress size={150} className={classes.uiProgess} />}
				</div>
			);
		} else {
			return (
				<div className={classes.root}>
					<CssBaseline />
					<AppBar position="fixed" className={classes.appBar}>
						<Toolbar>
							<Typography variant="h6" noWrap>
								TodoApp
							</Typography>
						</Toolbar>
					</AppBar>
					<Drawer
						className={classes.drawer}
						variant="permanent"
						classes={{
							paper: classes.drawerPaper
						}}
					>
						<div className={classes.toolbar} />
						<Divider />
						<center>
							<Avatar src={this.state.profilePicture} className={classes.avatar} />
							<p>
								{' '}
								{this.state.firstName} {this.state.lastName}
							</p>
						</center>
						<Divider />
						<List>
							<ListItem button key="Todo" onClick={this.loadTodoPage}>
								<ListItemIcon>
									{' '}
									<NotesIcon />{' '}
								</ListItemIcon>
								<ListItemText primary="Todo" />
							</ListItem>

							<ListItem button key="Account" onClick={this.loadAccountPage}>
								<ListItemIcon>
									{' '}
									<AccountBoxIcon />{' '}
								</ListItemIcon>
								<ListItemText primary="Account" />
							</ListItem>

							<ListItem button key="Logout" onClick={this.logoutHandler}>
								<ListItemIcon>
									{' '}
									<ExitToAppIcon />{' '}
								</ListItemIcon>
								<ListItemText primary="Logout" />
							</ListItem>
						</List>
					</Drawer>

					<div>{this.state.render ? <Account /> : <Todo />}</div>
				</div>
			);
		}
	}
}
```

Ici, dans le code, vous verrez que `authMiddleWare(this.props.history);` est utilisé. Ce middleware vérifie si le authToken est null. Si oui, il redirigera l'utilisateur vers `login.js`. Cela est ajouté pour que notre utilisateur ne puisse pas accéder à la route `/` sans s'inscrire ou se connecter. À la fin de ce fichier, ajoutez l'exportation suivante :

```js
export default withStyles(styles)(home);
```

Maintenant, vous vous demandez peut-être ce que fait ce code de `home.js` :

```python
<div>{this.state.render ? <Account /> : <Todo />}</div>
```

Il vérifie l'état de rendu que nous définissons lors du clic sur le bouton. Créons le répertoire des composants, et dans ce répertoire, créez deux fichiers : `account.js` et `todo.js`.

Créons un répertoire nommé **util** et un fichier nommé `auth.js` dans ce répertoire. Copiez-collez le code suivant dans `auth.js` :

```js
export const authMiddleWare = (history) => {
    const authToken = localStorage.getItem('AuthToken');
    if(authToken === null){
        history.push('/login')
    }
}
```

Pour l'instant, dans le fichier `todo.js`, nous allons simplement écrire une classe qui rend le texte **Bonjour, je suis todo**. Nous travaillerons sur nos todos dans la section suivante :

```js
import React, { Component } from 'react'

import withStyles from '@material-ui/core/styles/withStyles';
import Typography from '@material-ui/core/Typography';

const styles = ((theme) => ({
    content: {
        flexGrow: 1,
        padding: theme.spacing(3),
    },
    toolbar: theme.mixins.toolbar,
    })
);

class todo extends Component {
    render() {
        const { classes } = this.props;
        return (
            <main className={classes.content}>
            <div className={classes.toolbar} />
            <Typography paragraph>
                Bonjour, je suis todo
            </Typography>
            </main>
        )
    }
}

export default (withStyles(styles)(todo));
```

Maintenant, il est temps pour la section compte. Importez Material UI, clsx, axios et le middleware auth dans notre fichier `account.js`.

```js
// account.js

import React, { Component } from 'react';

import withStyles from '@material-ui/core/styles/withStyles';
import Typography from '@material-ui/core/Typography';
import CircularProgress from '@material-ui/core/CircularProgress';
import CloudUploadIcon from '@material-ui/icons/CloudUpload';
import { Card, CardActions, CardContent, Divider, Button, Grid, TextField } from '@material-ui/core';

import clsx from 'clsx';

import axios from 'axios';
import { authMiddleWare } from '../util/auth';
```

Nous ajouterons le style suivant à notre page Compte :

```js
// account.js

const styles = (theme) => ({
	content: {
		flexGrow: 1,
		padding: theme.spacing(3)
	},
	toolbar: theme.mixins.toolbar,
	root: {},
	details: {
		display: 'flex'
	},
	avatar: {
		height: 110,
		width: 100,
		flexShrink: 0,
		flexGrow: 0
	},
	locationText: {
		paddingLeft: '15px'
	},
	buttonProperty: {
		position: 'absolute',
		top: '50%'
	},
	uiProgess: {
		position: 'fixed',
		zIndex: '1000',
		height: '31px',
		width: '31px',
		left: '50%',
		top: '35%'
	},
	progess: {
		position: 'absolute'
	},
	uploadButton: {
		marginLeft: '8px',
		margin: theme.spacing(1)
	},
	customError: {
		color: 'red',
		fontSize: '0.8rem',
		marginTop: 10
	},
	submitButton: {
		marginTop: '10px'
	}
});
```

Nous allons créer un composant de classe nommé account. Pour l'instant, copiez-collez simplement le code suivant :

```js
// account.js

class account extends Component {
	constructor(props) {
		super(props);

		this.state = {
			firstName: '',
			lastName: '',
			email: '',
			phoneNumber: '',
			username: '',
			country: '',
			profilePicture: '',
			uiLoading: true,
			buttonLoading: false,
			imageError: ''
		};
	}

	componentWillMount = () => {
		authMiddleWare(this.props.history);
		const authToken = localStorage.getItem('AuthToken');
		axios.defaults.headers.common = { Authorization: `${authToken}` };
		axios
			.get('/user')
			.then((response) => {
				console.log(response.data);
				this.setState({
					firstName: response.data.userCredentials.firstName,
					lastName: response.data.userCredentials.lastName,
					email: response.data.userCredentials.email,
					phoneNumber: response.data.userCredentials.phoneNumber,
					country: response.data.userCredentials.country,
					username: response.data.userCredentials.username,
					uiLoading: false
				});
			})
			.catch((error) => {
				if (error.response.status === 403) {
					this.props.history.push('/login');
				}
				console.log(error);
				this.setState({ errorMsg: 'Erreur lors de la récupération des données' });
			});
	};

	handleChange = (event) => {
		this.setState({
			[event.target.name]: event.target.value
		});
	};

	handleImageChange = (event) => {
		this.setState({
			image: event.target.files[0]
		});
	};

	profilePictureHandler = (event) => {
		event.preventDefault();
		this.setState({
			uiLoading: true
		});
		authMiddleWare(this.props.history);
		const authToken = localStorage.getItem('AuthToken');
		let form_data = new FormData();
		form_data.append('image', this.state.image);
		form_data.append('content', this.state.content);
		axios.defaults.headers.common = { Authorization: `${authToken}` };
		axios
			.post('/user/image', form_data, {
				headers: {
					'content-type': 'multipart/form-data'
				}
			})
			.then(() => {
				window.location.reload();
			})
			.catch((error) => {
				if (error.response.status === 403) {
					this.props.history.push('/login');
				}
				console.log(error);
				this.setState({
					uiLoading: false,
					imageError: 'Erreur lors de l\'envoi des données'
				});
			});
	};

	updateFormValues = (event) => {
		event.preventDefault();
		this.setState({ buttonLoading: true });
		authMiddleWare(this.props.history);
		const authToken = localStorage.getItem('AuthToken');
		axios.defaults.headers.common = { Authorization: `${authToken}` };
		const formRequest = {
			firstName: this.state.firstName,
			lastName: this.state.lastName,
			country: this.state.country
		};
		axios
			.post('/user', formRequest)
			.then(() => {
				this.setState({ buttonLoading: false });
			})
			.catch((error) => {
				if (error.response.status === 403) {
					this.props.history.push('/login');
				}
				console.log(error);
				this.setState({
					buttonLoading: false
				});
			});
	};

	render() {
		const { classes, ...rest } = this.props;
		if (this.state.uiLoading === true) {
			return (
				<main className={classes.content}>
					<div className={classes.toolbar} />
					{this.state.uiLoading && <CircularProgress size={150} className={classes.uiProgess} />}
				</main>
			);
		} else {
			return (
				<main className={classes.content}>
					<div className={classes.toolbar} />
					<Card {...rest} className={clsx(classes.root, classes)}>
						<CardContent>
							<div className={classes.details}>
								<div>
									<Typography className={classes.locationText} gutterBottom variant="h4">
										{this.state.firstName} {this.state.lastName}
									</Typography>
									<Button
										variant="outlined"
										color="primary"
										type="submit"
										size="small"
										startIcon={<CloudUploadIcon />}
										className={classes.uploadButton}
										onClick={this.profilePictureHandler}
									>
										Télécharger une photo
									</Button>
									<input type="file" onChange={this.handleImageChange} />

									{this.state.imageError ? (
										<div className={classes.customError}>
											{' '}
											Mauvais format d'image || Formats pris en charge : PNG et JPG
										</div>
									) : (
										false
									)}
								</div>
							</div>
							<div className={classes.progress} />
						</CardContent>
						<Divider />
					</Card>

					<br />
					<Card {...rest} className={clsx(classes.root, classes)}>
						<form autoComplete="off" noValidate>
							<Divider />
							<CardContent>
								<Grid container spacing={3}>
									<Grid item md={6} xs={12}>
										<TextField
											fullWidth
											label="Prénom"
											margin="dense"
											name="firstName"
											variant="outlined"
											value={this.state.firstName}
											onChange={this.handleChange}
										/>
									</Grid>
									<Grid item md={6} xs={12}>
										<TextField
											fullWidth
											label="Nom de famille"
											margin="dense"
											name="lastName"
											variant="outlined"
											value={this.state.lastName}
											onChange={this.handleChange}
										/>
									</Grid>
									<Grid item md={6} xs={12}>
										<TextField
											fullWidth
											label="Email"
											margin="dense"
											name="email"
											variant="outlined"
											disabled={true}
											value={this.state.email}
											onChange={this.handleChange}
										/>
									</Grid>
									<Grid item md={6} xs={12}>
										<TextField
											fullWidth
											label="Numéro de téléphone"
											margin="dense"
											name="phone"
											type="number"
											variant="outlined"
											disabled={true}
											value={this.state.phoneNumber}
											onChange={this.handleChange}
										/>
									</Grid>
									<Grid item md={6} xs={12}>
										<TextField
											fullWidth
											label="Nom d'utilisateur"
											margin="dense"
											name="userHandle"
											disabled={true}
											variant="outlined"
											value={this.state.username}
											onChange={this.handleChange}
										/>
									</Grid>
									<Grid item md={6} xs={12}>
										<TextField
											fullWidth
											label="Pays"
											margin="dense"
											name="country"
											variant="outlined"
											value={this.state.country}
											onChange={this.handleChange}
										/>
									</Grid>
								</Grid>
							</CardContent>
							<Divider />
							<CardActions />
						</form>
					</Card>
					<Button
						color="primary"
						variant="contained"
						type="submit"
						className={classes.submitButton}
						onClick={this.updateFormValues}
						disabled={
							this.state.buttonLoading ||
							!this.state.firstName ||
							!this.state.lastName ||
							!this.state.country
						}
					>
						Enregistrer les détails
						{this.state.buttonLoading && <CircularProgress size={30} className={classes.progess} />}
					</Button>
				</main>
			);
		}
	}
}
```

À la fin de ce fichier, ajoutez l'exportation suivante :

```js
export default withStyles(styles)(account);
```

Dans `account.js`, il y a beaucoup de composants utilisés. D'abord, voyons à quoi ressemble notre application. Après cela, j'expliquerai tous les composants qui sont utilisés et pourquoi ils sont utilisés.

Allez dans le navigateur, et si votre token a expiré, il vous redirigera vers la page `login`. Ajoutez vos détails et connectez-vous à nouveau. Une fois que vous avez terminé, allez dans l'onglet Compte et vous trouverez l'UI suivante :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-88.png align="left")

*Section Compte*

Il y a 3 gestionnaires dans la section Compte :

1. **componentWillMount** : Il s'agit d'une méthode de cycle de vie intégrée de React. Nous l'utilisons pour charger les données avant le cycle de vie du rendu et mettre à jour nos valeurs d'état.

2. **ProfilePictureUpdate** : Il s'agit de notre gestionnaire personnalisé que nous utilisons afin que lorsque notre utilisateur clique sur le bouton Télécharger une photo, il envoie les données à un serveur et recharge la page pour afficher la nouvelle photo de profil de l'utilisateur.

3. **updateFormValues** : Il s'agit également de notre gestionnaire personnalisé pour mettre à jour les détails de l'utilisateur. Ici, l'utilisateur peut mettre à jour son prénom, son nom de famille et son pays. Nous n'autorisons pas les mises à jour de l'email et du nom d'utilisateur car notre logique backend dépend de ces clés.

En plus de ces 3 gestionnaires, il s'agit d'une page de formulaire avec un style par-dessus. Voici la structure du répertoire jusqu'à ce point à l'intérieur du dossier view :

```shell
+-- public 
+-- src
|   +-- components
|   +-- +-- todo.js
|   +-- +-- account.js
|   +-- pages
|   +-- +-- home.js
|   +-- +-- login.js
|   +-- +-- signup.js
|   +-- util
|   +-- +-- auth.js 
|   +-- README.md
|   +-- package-lock.json
|   +-- package.json
|   +-- .gitignore
```

Avec cela, nous avons terminé notre tableau de bord de compte. Maintenant, allez prendre un café, faites une pause et dans la section suivante, nous construirons le tableau de bord Todo.

## Section 4 : Tableau de bord Todo

Dans cette section, nous allons développer l'UI pour ces fonctionnalités du tableau de bord Todos :

1. **Ajouter un Todo :**

2. **Obtenir tous les todos :**

3. **Supprimer un todo**

4. **Modifier un todo**

5. **Obtenir un todo**

6. **Appliquer un thème**

Le code du tableau de bord Todo implémenté dans cette section peut être trouvé à ce [commit](https://github.com/Sharvin26/TodoApp/tree/3799980aa13eeb8d313e17d83aa3032748aedb00/view).

Allez dans `todos.js` sous le répertoire **components**. Ajoutez les imports suivants aux imports existants :

```js
import Button from '@material-ui/core/Button';
import Dialog from '@material-ui/core/Dialog';
import AddCircleIcon from '@material-ui/icons/AddCircle';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import IconButton from '@material-ui/core/IconButton';
import CloseIcon from '@material-ui/icons/Close';
import Slide from '@material-ui/core/Slide';
import TextField from '@material-ui/core/TextField';
import Grid from '@material-ui/core/Grid';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CircularProgress from '@material-ui/core/CircularProgress';
import CardContent from '@material-ui/core/CardContent';
import MuiDialogTitle from '@material-ui/core/DialogTitle';
import MuiDialogContent from '@material-ui/core/DialogContent';

import axios from 'axios';
import dayjs from 'dayjs';
import relativeTime from 'dayjs/plugin/relativeTime';
import { authMiddleWare } from '../util/auth';
```

Nous devons également ajouter les éléments CSS suivants dans les composants de style existants :

```js
const styles = (theme) => ({
	.., // Éléments CSS existants
	title: {
		marginLeft: theme.spacing(2),
		flex: 1
	},
	submitButton: {
		display: 'block',
		color: 'white',
		textAlign: 'center',
		position: 'absolute',
		top: 14,
		right: 10
	},
	floatingButton: {
		position: 'fixed',
		bottom: 0,
		right: 0
	},
	form: {
		width: '98%',
		marginLeft: 13,
		marginTop: theme.spacing(3)
	},
	toolbar: theme.mixins.toolbar,
	root: {
		minWidth: 470
	},
	bullet: {
		display: 'inline-block',
		margin: '0 2px',
		transform: 'scale(0.8)'
	},
	pos: {
		marginBottom: 12
	},
	uiProgess: {
		position: 'fixed',
		zIndex: '1000',
		height: '31px',
		width: '31px',
		left: '50%',
		top: '35%'
	},
	dialogeStyle: {
		maxWidth: '50%'
	},
	viewRoot: {
		margin: 0,
		padding: theme.spacing(2)
	},
	closeButton: {
		position: 'absolute',
		right: theme.spacing(1),
		top: theme.spacing(1),
		color: theme.palette.grey[500]
	}
});
```

Nous ajouterons la transition pour la boîte de dialogue pop-up :

```js
const Transition = React.forwardRef(function Transition(props, ref) {
	return <Slide direction="up" ref={ref} {...props} />;
});
```

Supprimez la classe todo existante et copiez-collez la classe suivante :

```js
class todo extends Component {
	constructor(props) {
		super(props);

		this.state = {
			todos: '',
			title: '',
			body: '',
			todoId: '',
			errors: [],
			open: false,
			uiLoading: true,
			buttonType: '',
			viewOpen: false
		};

		this.deleteTodoHandler = this.deleteTodoHandler.bind(this);
		this.handleEditClickOpen = this.handleEditClickOpen.bind(this);
		this.handleViewOpen = this.handleViewOpen.bind(this);
	}

	handleChange = (event) => {
		this.setState({
			[event.target.name]: event.target.value
		});
	};

	componentWillMount = () => {
		authMiddleWare(this.props.history);
		const authToken = localStorage.getItem('AuthToken');
		axios.defaults.headers.common = { Authorization: `${authToken}` };
		axios
			.get('/todos')
			.then((response) => {
				this.setState({
					todos: response.data,
					uiLoading: false
				});
			})
			.catch((err) => {
				console.log(err);
			});
	};

	deleteTodoHandler(data) {
		authMiddleWare(this.props.history);
		const authToken = localStorage.getItem('AuthToken');
		axios.defaults.headers.common = { Authorization: `${authToken}` };
		let todoId = data.todo.todoId;
		axios
			.delete(`todo/${todoId}`)
			.then(() => {
				window.location.reload();
			})
			.catch((err) => {
				console.log(err);
			});
	}

	handleEditClickOpen(data) {
		this.setState({
			title: data.todo.title,
			body: data.todo.body,
			todoId: data.todo.todoId,
			buttonType: 'Edit',
			open: true
		});
	}

	handleViewOpen(data) {
		this.setState({
			title: data.todo.title,
			body: data.todo.body,
			viewOpen: true
		});
	}

	render() {
		const DialogTitle = withStyles(styles)((props) => {
			const { children, classes, onClose, ...other } = props;
			return (
				<MuiDialogTitle disableTypography className={classes.root} {...other}>
					<Typography variant="h6">{children}</Typography>
					{onClose ? (
						<IconButton aria-label="close" className={classes.closeButton} onClick={onClose}>
							<CloseIcon />
						</IconButton>
					) : null}
				</MuiDialogTitle>
			);
		});

		const DialogContent = withStyles((theme) => ({
			viewRoot: {
				padding: theme.spacing(2)
			}
		}))(MuiDialogContent);

		dayjs.extend(relativeTime);
		const { classes } = this.props;
		const { open, errors, viewOpen } = this.state;

		const handleClickOpen = () => {
			this.setState({
				todoId: '',
				title: '',
				body: '',
				buttonType: '',
				open: true
			});
		};

		const handleSubmit = (event) => {
			authMiddleWare(this.props.history);
			event.preventDefault();
			const userTodo = {
				title: this.state.title,
				body: this.state.body
			};
			let options = {};
			if (this.state.buttonType === 'Edit') {
				options = {
					url: `/todo/${this.state.todoId}`,
					method: 'put',
					data: userTodo
				};
			} else {
				options = {
					url: '/todo',
					method: 'post',
					data: userTodo
				};
			}
			const authToken = localStorage.getItem('AuthToken');
			axios.defaults.headers.common = { Authorization: `${authToken}` };
			axios(options)
				.then(() => {
					this.setState({ open: false });
					window.location.reload();
				})
				.catch((error) => {
					this.setState({ open: true, errors: error.response.data });
					console.log(error);
				});
		};

		const handleViewClose = () => {
			this.setState({ viewOpen: false });
		};

		const handleClose = (event) => {
			this.setState({ open: false });
		};

		if (this.state.uiLoading === true) {
			return (
				<main className={classes.content}>
					<div className={classes.toolbar} />
					{this.state.uiLoading && <CircularProgress size={150} className={classes.uiProgess} />}
				</main>
			);
		} else {
			return (
				<main className={classes.content}>
					<div className={classes.toolbar} />

					<IconButton
						className={classes.floatingButton}
						color="primary"
						aria-label="Ajouter Todo"
						onClick={handleClickOpen}
					>
						<AddCircleIcon style={{ fontSize: 60 }} />
					</IconButton>
					<Dialog fullScreen open={open} onClose={handleClose} TransitionComponent={Transition}>
						<AppBar className={classes.appBar}>
							<Toolbar>
								<IconButton edge="start" color="inherit" onClick={handleClose} aria-label="close">
									<CloseIcon />
								</IconButton>
								<Typography variant="h6" className={classes.title}>
									{this.state.buttonType === 'Edit' ? 'Modifier Todo' : 'Créer un nouveau Todo'}
								</Typography>
								<Button
									autoFocus
									color="inherit"
									onClick={handleSubmit}
									className={classes.submitButton}
								>
									{this.state.buttonType === 'Edit' ? 'Enregistrer' : 'Soumettre'}
								</Button>
							</Toolbar>
						</AppBar>

						<form className={classes.form} noValidate>
							<Grid container spacing={2}>
								<Grid item xs={12}>
									<TextField
										variant="outlined"
										required
										fullWidth
										id="todoTitle"
										label="Titre du Todo"
										name="title"
										autoComplete="todoTitle"
										helperText={errors.title}
										value={this.state.title}
										error={errors.title ? true : false}
										onChange={this.handleChange}
									/>
								</Grid>
								<Grid item xs={12}>
									<TextField
										variant="outlined"
										required
										fullWidth
										id="todoDetails"
										label="Détails du Todo"
										name="body"
										autoComplete="todoDetails"
										multiline
										rows={25}
										rowsMax={25}
										helperText={errors.body}
										error={errors.body ? true : false}
										onChange={this.handleChange}
										value={this.state.body}
									/>
								</Grid>
							</Grid>
						</form>
					</Dialog>

					<Grid container spacing={2}>
						{this.state.todos.map((todo) => (
							<Grid item xs={12} sm={6}>
								<Card className={classes.root} variant="outlined">
									<CardContent>
										<Typography variant="h5" component="h2">
											{todo.title}
										</Typography>
										<Typography className={classes.pos} color="textSecondary">
											{dayjs(todo.createdAt).fromNow()}
										</Typography>
										<Typography variant="body2" component="p">
											{`${todo.body.substring(0, 65)}`}
										</Typography>
									</CardContent>
									<CardActions>
										<Button size="small" color="primary" onClick={() => this.handleViewOpen({ todo })}>
											{' '}
											Voir{' '}
										</Button>
										<Button size="small" color="primary" onClick={() => this.handleEditClickOpen({ todo })}>
											Modifier
										</Button>
										<Button size="small" color="primary" onClick={() => this.deleteTodoHandler({ todo })}>
											Supprimer
										</Button>
									</CardActions>
								</Card>
							</Grid>
						))}
					</Grid>

					<Dialog
						onClose={handleViewClose}
						aria-labelledby="customized-dialog-title"
						open={viewOpen}
						fullWidth
						classes={{ paperFullWidth: classes.dialogeStyle }}
					>
						<DialogTitle id="customized-dialog-title" onClose={handleViewClose}>
							{this.state.title}
						</DialogTitle>
						<DialogContent dividers>
							<TextField
								fullWidth
								id="todoDetails"
								name="body"
								multiline
								readonly
								rows={1}
								rowsMax={25}
								value={this.state.body}
								InputProps={{
									disableUnderline: true
								}}
							/>
						</DialogContent>
					</Dialog>
				</main>
			);
		}
	}
}
```

À la fin de ce fichier, ajoutez l'exportation suivante :

```js
export default withStyles(styles)(todo);
```

D'abord, nous allons comprendre comment fonctionne notre UI, puis nous comprendrons le code. Allez dans le navigateur et vous obtiendrez l'UI suivante :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/TodoDashboard.png align="left")

*Tableau de bord Todo*

Cliquez sur le bouton Ajouter en bas à droite et vous obtiendrez l'écran suivant :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/AddTodo.png align="left")

*Ajouter Todo*

Ajoutez le titre et les détails du Todo et appuyez sur le bouton soumettre. Vous obtiendrez l'écran suivant :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Added-Todo.png align="left")

*Tableau de bord Todo*

Après cela, cliquez sur le bouton voir et vous pourrez voir les détails complets du Todo :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/View-Todo.png align="left")

*Voir un seul Todo*

Cliquez sur le bouton Modifier et vous pourrez modifier le todo :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/EditTodo.png align="left")

*Modifier Todo*

Cliquez sur le bouton supprimer et vous pourrez supprimer le Todo. Maintenant que nous savons comment fonctionne le tableau de bord, nous allons comprendre les composants utilisés.

**1. Ajouter Todo :** Pour implémenter l'ajout d'un todo, nous utiliserons le [composant Dialogue](https://material-ui.com/components/dialogs/#full-screen-dialogs) de Material UI. Ce composant implémente une fonctionnalité de hook. Nous utilisons les classes, donc nous supprimerons cette fonctionnalité.

```js
// Cela définit l'état à ouvert et le drapeau buttonType à ajouter :
const handleClickOpen = () => {
      this.setState({
           todoId: '',
           title: '',
           body: '',
           buttonType: '',
           open: true
     });
};

// Cela définit l'état à fermé :
const handleClose = (event) => {
      this.setState({ open: false });
};
```

En plus de cela, nous allons également changer le placement du bouton Ajouter Todo.

```js
// Positionner notre bouton
floatingButton: {
    position: 'fixed',
    bottom: 0,
    right: 0
},

<IconButton className={classes.floatingButton} ... >
```

Maintenant, nous allons remplacer la balise de liste par un formulaire à l'intérieur de ce Dialogue. Cela nous aidera à ajouter le nouveau todo.

```js
// Afficher Modifier ou Enregistrer en fonction de l'état buttonType
{this.state.buttonType === 'Edit' ? 'Enregistrer' : 'Soumettre'}

// Notre formulaire pour ajouter un todo
<form className={classes.form} noValidate>
	<Grid container spacing={2}>
		<Grid item xs={12}>
        // TextField ici
        </Grid>
        <Grid item xs={12}>
        // TextField ici
        </Grid>
    </Grid>
</form>
```

Le handleSubmit contient la logique pour lire l'état `buttonType`. Si l'état est une chaîne vide `("")`, alors il publiera sur l'API Ajouter Todo. Si l'état est `Edit`, alors dans ce scénario, il mettra à jour le Todo à modifier.

**2. Obtenir les Todos :** Pour afficher les todos, nous utiliserons le `Grid container` et à l'intérieur, nous placerons le `Grid item`. À l'intérieur, nous utiliserons un composant `Card` pour afficher les données.

```js
<Grid container spacing={2}>
    {this.state.todos.map((todo) => (
	<Grid item xs={12} sm={6}>
	<Card className={classes.root} variant="outlined">
	    <CardContent>
        // Ici, nous montrerons le Todo avec les boutons voir, modifier et supprimer
        </CardContent>
    </Card>
    </Grid>))}
</Grid>
```

Nous utilisons la méthode map pour afficher l'élément todo car l'API les envoie dans une liste. Nous utiliserons le cycle de vie componentWillMount pour obtenir et définir l'état avant que le rendu ne soit exécuté. Il y a 3 boutons (**voir, modifier et supprimer**), donc nous aurons besoin de 3 gestionnaires pour gérer l'opération lorsque le bouton est cliqué. Nous apprendrons à connaître ces boutons dans leurs sous-sections respectives.

**3. Modifier Todo :** Pour modifier le todo, nous réutilisons le code de la boîte de dialogue pop-up qui est utilisé dans l'ajout de todo. Pour différencier les clics sur les boutons, nous utilisons un état `buttonType`. Pour Ajouter Todo, l'état `buttonType` est `("")` tandis que pour modifier le todo, il est `Edit`.

```js
handleEditClickOpen(data) {
	this.setState({
		..,
		buttonType: 'Edit',
		..
	});
}
```

Dans la méthode `handleSubmit`, nous lisons l'état `buttonType` puis envoyons la requête en conséquence.

**4. Supprimer Todo :** Lorsque ce bouton est cliqué, nous envoyons l'objet todo à notre gestionnaire deleteTodoHandler, puis il envoie la requête au backend.

```js
<Button size="small" onClick={() => this.deleteTodoHandler({ todo })}>Supprimer</Button>
```

**5. Voir Todo :** Lorsque nous affichons les données, nous les avons tronquées afin que l'utilisateur ait un aperçu de ce dont il s'agit. Mais si un utilisateur veut en savoir plus, il doit cliquer sur le bouton voir.

Pour cela, nous utiliserons le [dialogue personnalisé](https://material-ui.com/components/dialogs/#customized-dialogs). À l'intérieur, nous utilisons DialogTitle et DialogContent. Il affiche notre titre et notre contenu. Dans DialogContent, nous utiliserons le formulaire pour afficher le contenu que l'utilisateur a publié. (C'est une solution que j'ai trouvée, il y en a beaucoup et vous êtes libre d'essayer d'autres.)

```js
// Cela est utilisé pour supprimer le soulignement du formulaire
InputProps={{
       disableUnderline: true
}}

// Cela est utilisé pour que l'utilisateur ne puisse pas modifier les données
readonly
```

**6. Appliquer un thème :** Il s'agit de la dernière étape de notre application. Nous allons appliquer un thème à notre application. Pour cela, nous utilisons `createMuiTheme` et `ThemeProvider` de Material UI. Copiez-collez le code suivant dans `App.js` :

```js
import { ThemeProvider as MuiThemeProvider } from '@material-ui/core/styles';
import createMuiTheme from '@material-ui/core/styles/createMuiTheme';

const theme = createMuiTheme({
	palette: {
		primary: {
			light: '#33c9dc',
			main: '#FF5722',
			dark: '#d50000',
			contrastText: '#fff'
		}
	}
});

function App() {
	return (
        <MuiThemeProvider theme={theme}>
        // Le routeur et le commutateur seront ici.
        </MuiThemeProvider>
    );
}
```

Nous avons oublié d'appliquer un thème à notre bouton dans `todo.js` dans `CardActions`. Ajoutez la balise de couleur pour les boutons voir, modifier et supprimer.

```js
<Button size="small" color="primary" ...>
```

Allez dans le navigateur et vous verrez que tout est identique, sauf que l'application est d'une couleur différente.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/FinalTodo.png align="left")

*TodoApp après l'application du thème*

Et c'est terminé ! Nous avons construit une TodoApp en utilisant ReactJS et Firebase. Si vous l'avez construite jusqu'à ce point, alors un très grand bravo pour cette réalisation.

> N'hésitez pas à me contacter sur [Twitter](https://twitter.com/sharvinshah26) et [Github](https://github.com/Sharvin26).