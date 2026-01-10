---
title: Comment construire une application avec Node.js
subtitle: ''
author: Ijeoma Igboagu
co_authors: []
series: null
date: '2024-08-05T17:56:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-event-app-with-node-js
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1741114813767/a2786471-5a6a-4450-bdb1-f7d1162c2a90.png
tags:
- name: JavaScript
  slug: javascript
- name: node js
  slug: node-js
seo_title: Comment construire une application avec Node.js
seo_desc: 'Node.js it’s a runtime environment that allows you to run JavaScript code
  on the server side for building server-side applications. It works well for creating
  fast and scalable applications.

  In this article, I will use a simple event management app a...'
---

Node.js est un environnement d'exécution qui permet d'exécuter du code JavaScript côté serveur pour construire des applications côté serveur. Il est bien adapté pour créer des applications rapides et évolutives.

Dans cet article, je vais utiliser une simple application de gestion d'événements comme exemple pour vous montrer comment construire une application en utilisant Node.js, Express.js et MongoDB.

À la fin, vous saurez comment configurer un projet Node.js, créer un serveur avec Express.js, afficher des pages dynamiques avec JavaScript intégré et vous connecter à une base de données MongoDB pour gérer vos données.

### Ce que vous allez apprendre

* Configurer un projet Node.js
  
* Créer un serveur avec Express.js
  
* Rendre des pages dynamiques avec ejs
  
* Se connecter à une base de données MongoDB
  
* Créer des modèles et des schémas pour vos données
  
* Gérer les requêtes et réponses HTTP
  

## Table des matières

* [Configurer votre environnement de développement](#heading-step-1-configurer-votre-environnement-de-developpement)
  
* [Configurer le serveur](#heading-step-2-configurer-le-serveur)
  
* [Installer et configurer Express.js](#heading-step-3-installer-et-configurer-expressjs)
  
* [Créer un modèle dynamique](#heading-step-4-creer-un-modele-dynamique)
  
* [Enregistrer vos données dans MongoDB](#heading-step-5-enregistrer-vos-donnees-dans-mongodb)
  
* [Se connecter à la base de données](#heading-step-6-se-connecter-a-la-base-de-donnees)
  
* [Créer le modèle pour la structure du document](#heading-step-7-creer-le-modele-pour-la-structure-du-document)
  
* [Créer des pages HTML](#heading-step-8-creer-des-pages-html)
  
* [Créer des partials](#heading-step-9-creer-des-partials)
  
* [Créer un fichier de variables d'environnement](#heading-step-10-creer-un-fichier-de-variables-denvironnement-env)
  
* [Étapes suivantes](#heading-etapes-suivantes)
  
* [Conclusion](#heading-conclusion)
  

![Commençons 🚀](https://www.freecodecamp.org/news/content/images/2024/07/image-56.png align="left")

*Commençons 🚀*

## Prérequis

* [Node.js](https://nodejs.org/en) installé sur votre système.
  
* Une bonne compréhension de [MongoDB](https://www.mongodb.com/).
  
* Un éditeur de code que vous préférez, tel que [Visual Studio Code](https://code.visualstudio.com/) ou [Sublime Text](https://www.sublimetext.com/download).
  

## Étape 1 : Configurer votre environnement de développement

### Installer Node.js et npm

Tout d'abord, vous devrez télécharger et installer Node.js depuis [nodejs.org](https://nodejs.org/). Ensuite, vous pouvez vérifier l'installation en exécutant : `node -v` et `npm -v`.

### Initialiser un nouveau projet

Créez un nouveau répertoire pour votre projet. Ensuite, initialisez le projet avec npm : `npm init -y` dans votre terminal.

```js
mkdir event-app
cd event-app
npm init -y
```

![Initialisation du projet](https://www.freecodecamp.org/news/content/images/2024/07/ShareX_OnHiLv8GvS-1.gif align="left")

*Initialisation du projet*

L'exécution de `npm init -y` crée le fichier `package.json`, comme montré ci-dessus. Ce fichier est crucial. Il stocke et suit toutes les bibliothèques tierces (dépendances) nécessaires pour votre application.

## Étape 2 : Configurer le serveur

Pour configurer votre serveur, créez un fichier appelé `server.js` ou `app.js`. Ce sont des noms courants. Ils sont utilisés pour leur nature descriptive. Mais vous pouvez nommer le fichier comme vous le souhaitez.

Le fichier `server.js` sera utilisé pour créer un serveur qui sera utilisé pour gérer, contrôler et router vers la page nécessaire dans notre application.

## Étape 3 : Installer et configurer Express.js

Express.js est un framework populaire pour les applications web pour Node.js et une bibliothèque tierce que nous utilisons dans notre application.

Express simplifie la gestion et la définition de diverses routes pour les requêtes HTTP. Il vous permet de gérer le routage de l'application et de le connecter au serveur.

### Pour utiliser Express :

Installez Express.js en exécutant la commande suivante dans votre terminal :

```javascript
npm install express
```

Requérez Express dans votre fichier `server.js`.

```js
const express = require('express')
```

Initialisez Express pour pouvoir l'utiliser dans votre application.

```js
const app = express()
```

Créez un chemin de routage pour obtenir la requête HTTP.

```javascript
// chemin de routage
app.get('/', (req, res) => {
  res.send('Hello World!');
});
```

Enfin, nous devons nous assurer que la connexion au serveur est correctement configurée. Lorsque nous démarrons le serveur dans le terminal, il s'ouvrira dans le navigateur.

Pour ce faire, utilisez la méthode `listen()`.

```javascript
// Démarrer le serveur
app.listen(3000, () => {
  console.log('Serveur démarré sur le port 3000');
});
```

Cette méthode écoutera les requêtes du serveur.

**Voici le code complet :**

```javascript
const express = require('express');


// Initialiser l'application
const app = express();

// chemin de routage
app.get('/', (req, res) => {
  res.send('Hello World!');
});

// Démarrer le serveur
app.listen(3000, () => {
  console.log('Serveur démarré sur le port 3000');
});
```

**Note :** Le chemin de routage ci-dessus était uniquement à des fins de test pour confirmer que le serveur fonctionne et est connecté. Nous fournirons un fichier différent pour l'application d'événements que nous créons.

Avec Express.js installé dans votre application, vous pouvez maintenant créer un serveur qui gérera toutes vos routes et connexions.

Pour démarrer le serveur, allez dans votre terminal.

Utilisez le mot-clé `node`, puis tapez `--watch`, un drapeau pour démarrer et redémarrer automatiquement le serveur chaque fois que vous apportez des modifications :

```javascript
node --watch server.js
```

Ou vous pouvez installer `[nodemon](https://www.npmjs.com/package/nodemon)` pour le même but. `Nodemon` détecte les changements dans le répertoire et redémarre votre application.

```javascript
npm install -g nodemon
```

Puis exécutez votre serveur avec :

```javascript
nodemon server.js
```

## Étape 4 : Créer un modèle dynamique

Nous avons besoin d'un moteur de modélisation pour rendre le code `HTML` dans le navigateur en utilisant Node.js. Nous utiliserons ejs **(Embedded JavaScript)** pour ce tutoriel, mais il en existe d'autres comme [Pug (anciennement connu sous le nom de Jade)](https://pugjs.org/api/getting-started.html) et [Express Handlebar](https://www.npmjs.com/package/express-handlebars), qui rendent également le HTML sur le serveur.

`ejs` vous permet d'intégrer JavaScript dans HTML pour créer des pages web dynamiques.

Pour installer `ejs`, exécutez :

```bash
npm install ejs
```

Pour configurer `ejs` dans `server.js`, requérez et définissez `ejs` comme moteur de modélisation :

![requiring ejs template in our application](https://www.freecodecamp.org/news/content/images/2024/07/image-51.png align="left")

*Requiring* `ejs` template in your application

```javascript
const express = require('express');
const app = express();

app.set('view engine', 'ejs');
```

Avec cette configuration, vous pouvez maintenant activer le rendu dynamique du code `HTML` dans votre application Node.js.

## Étape 5 : Enregistrer vos données dans MongoDB

Pour enregistrer les données que vous créez pour votre application, vous utiliserez MongoDB.

MongoDB est une base de données "Not Only SQL" (NoSQL) conçue pour stocker des collections de documents. Les bases de données SQL traditionnelles organisent les données dans des tables, mais MongoDB est optimisé pour gérer de grands volumes de données.

Pour en savoir plus, [consultez cet article](https://www.mongodb.com/resources/basics/databases/nosql-explained).

## Étape 6 : Se connecter à la base de données

Maintenant, nous devons nous connecter à la base de données, qui sera MongoDB pour ce tutoriel.

L'utilisation de MongoDB vous fournit une URL (Uniform Resource Locator) pour vous connecter à votre application. Cette URL vous connecte et agit comme un communicateur entre la base de données et votre application.

### Comment obtenir l'URL

Pour obtenir l'URL, suivez ces étapes simples :

1. **Inscription/Connexion** : Allez sur le [site web de MongoDB](https://www.mongodb.com/) et inscrivez-vous pour un compte ou connectez-vous si vous en avez déjà un.
  
2. **Créer un cluster** : Une fois connecté, créez un nouveau cluster. Cela configurera votre base de données.
  
3. **Se connecter à votre cluster** : Après la création de votre cluster, cliquez sur le bouton "Connect".
  
4. **Choisir une méthode de connexion** : Sélectionnez "Connect your application".
  
5. **Copier la chaîne de connexion** : MongoDB fournira une chaîne de connexion (URL) comme ceci :
  

```js
mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority
```

6. **Remplacer les espaces réservés** : Remplacez `<username>`, `<password>`, et `<dbname>` par votre nom d'utilisateur, mot de passe et nom de base de données réels.
  

Maintenant que vous avez l'URL, vous pouvez facilement vous connecter à votre base de données.

Pour faciliter cette connexion, nous utiliserons un outil appelé Mongoose.

### Qu'est-ce que Mongoose ?

[Mongoose](https://mongoosejs.com/) est une bibliothèque JavaScript qui facilite le travail avec MongoDB dans un environnement Node.js. Elle fournit un moyen simple de modéliser vos données. Vous pouvez définir des schémas, faire de la validation de données et construire des requêtes également.

### Comment établir une connexion

MongoDB vous a déjà fourni une URL pour la connexion. Maintenant, vous allez utiliser Mongoose pour envoyer vos documents à la base de données.

Pour utiliser Mongoose dans votre projet, suivez ces étapes :

Installez Mongoose en utilisant npm.

```js
npm i mongoose
```

Dans votre fichier `server.js`, vous devez requérir Mongoose pour l'utiliser comme connecteur à la base de données.

```js
const mongoose = require('mongoose');
```

Après avoir requis Mongoose, vous devez définir l'URL de connexion fournie dans votre fichier `server.js`.

`server.js` :

```js
const mongoose = require('mongoose');

// Remplacez <username>, <password>, et <dbname> par vos identifiants réels
const dbURL = 'mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority';

mongoose
  .connect(process.env.dbURL)
  .then((result) => {
    console.log('Connecté à MongoDB');
    app.listen(3000, () => {
      console.log('Serveur démarré sur le port 3000');
    });
  })
  .catch((err) => {
    console.error('Impossible de se connecter à MongoDB :', err);
  });
```

Cette configuration garantit que Mongoose agit comme le connecteur. Il connecte votre application à la base de données MongoDB.

## Étape 7 : Créer le modèle pour la structure du document

Ensuite, nous devons créer un modèle de document appelé un schéma afin que lorsque vous postez des données dans votre base de données, elles soient enregistrées correctement.

Pour créer ce modèle :

1. Créez un dossier nommé `models` pour garder votre application organisée.
  
2. À l'intérieur du dossier `models`, créez un fichier appelé `event.js`.
  

Dans le fichier `event.js`, vous utiliserez Mongoose pour définir le schéma des documents d'événements. Vous spécifierez la structure et les types de données pour les documents que vous enverrez à votre base de données.

Voici le fichier `event.js` créé à l'intérieur du dossier `models` :

```js
const mongoose = require('mongoose');

// Schéma
const EventSchema = new mongoose.Schema(
  {
    title: {
      type: String,
      required: true,
    },
    date: {
      type: Date,
      required: true,
    },
    organizer: {
      type: String,
      required: true,
    },
    price: {
      type: String,
      required: true,
    },
    time: {
      type: String,
      required: true,
    },
    location: {
      type: String,
      required: true,
    },
    description: {
      type: String,
      required: true,
    },
  },
  { timestamps: true }
);

const Event = mongoose.model('event', EventSchema);

module.exports = Event;
```

Lorsque cela est fait, exportez-le pour pouvoir l'utiliser dans votre fichier `server.js` en utilisant simplement le mot-clé **require**.

Avec le schéma créé, il peut maintenant être exporté vers le fichier `server.js`.

Votre fichier `server.js` ressemblera à ceci :

```js
const express = require('express');
const ejs = require('ejs');
const mongoose = require('mongoose');
const Event = require('../models/Events');// le fichier event.js
```

## Étape 8 : Créer des pages HTML

Comme nous en avons parlé précédemment, nous utilisons `ejs` dans l'étape 4 pour rendre le code `HTML`, ce qui nous permet de visualiser le code dans le navigateur.

### Page de formulaire

Tout d'abord, créons une page de formulaire. Avec la page de formulaire créée, vous pourrez faire des requêtes POST qui vous permettront d'envoyer des données à votre base de données MongoDB.

Pour créer un formulaire de base, assurez-vous qu'il inclut :

* Un attribut `action` qui spécifie la route pour envoyer les données.
  
* Un attribut `method` qui spécifie la méthode de requête HTTP - dans ce cas, la requête POST.
  

Un formulaire de base :

```js
<form action="/submit-event" method="POST">
    <h2>Formulaire de création d'événement</h2>
  <label for="title">Titre</label>
  <input type="text" id="title" name="title" required>

  <label for="date">Date</label>
  <input type="date" id="date" name="date" required>

  <label for="organizer">Organisateur</label>
  <input type="text" id="organizer" name="organizer" required>

  <label for="price">Prix</label>
  <input type="text" id="price" name="price" required>

  <label for="time">Heure</label>
  <input type="text" id="time" name="time" required>

  <label for="location">Lieu</label>
  <input type="text" id="location" name="location" required>

  <label for="description">Description</label>
  <textarea id="description" name="description" rows="4" required></textarea>

  <button type="submit">Soumettre</button>
</form>
```

NB : Assurez-vous d'ajouter l'attribut **name** à chaque entrée, sinon elle ne sera pas postée.

Le formulaire créé ci-dessus vous permettra de poster des données vers la route spécifiée. Vous les traiterez ensuite et les stockerez dans votre base de données.

**Voici le résultat :**

![La page de formulaire](https://www.freecodecamp.org/news/content/images/2024/07/image-53.png align="left")

*La page de formulaire*

Après avoir créé la page de formulaire, nous devons revenir au fichier `server.js` et créer une requête POST pour gérer la soumission du formulaire.

Fichier `server.js` :

```js
// poster des données

app.post('/submit-event', (req, res) => {
  const event = new Event(req.body);
  event.save()
    .then((result) => {
      res.redirect('/');
    })
    .catch((err) => {
      console.error(err);
    });
});
```

### La page d'accueil

Maintenant que le formulaire peut poster des données dans la base de données, nous pouvons créer la page d'accueil pour afficher les événements créés dans le navigateur.

Tout d'abord, dans votre fichier `server.js`, vous devez créer une fonction. Elle récupérera tous les événements postés depuis le formulaire et stockés dans la base de données.

Voici comment le configurer :

Ceci est une fonction créée dans `server.js` pour récupérer toutes les données de la base de données :

```js
// Pour obtenir tous les événements

router.get('/', (req, res) => {
  Event.find()
    .then((result) => {
      res.render('index', { title: 'Tous les événements', events: result })
    })
    .catch((err) => {
      console.error(err); 
  })
})
```

Ensuite, nous allons boucler dynamiquement à travers chaque partie en utilisant une boucle `forEach` dans le fichier de la page d'accueil. Puisque nous utilisons `ejs`, l'extension du fichier `HTML` sera `.ejs`.

```js
<div>
  <h2>Tous les événements</h2>
  <div>
    <% if (events.length > 0) { %>
      <% events.forEach(event => { %>
        <div>
          <h3><%= event.title %></h3>
          <p><%= event.description %></p>
          <a href="/event/<%= event.id %>">
            Lire la suite
          </a>
        </div>
      <% }) %>
    <% } else { %>
      <p>Aucun événement disponible pour le moment.</p>
    <% } %>
  </div>
</div>
```

Voici une explication de ce que fait chaque partie du code :

* **En-tête (**`<h2>Tous les événements</h2>`): Affiche "Tous les événements" comme en-tête.
  
* **Liste des événements (**`<div>`): Conteneur pour afficher une liste d'événements.
  
* **Vérification conditionnelle (** `<% if (events.length > 0) { %> ... <% } else { %> ... <% } %>`): Vérifie s'il y a des événements (`events.length > 0`). Si des événements existent, il boucle à travers chaque événement (`events.forEach`) pour afficher ses détails.
  
* Pour chaque événement, il crée un `<div>` contenant le titre de l'événement (`event.title`) dans une balise `<h3>`, la description de l'événement (`event.description`) dans une balise `<p>`, et un lien (`<a>`) pour voir plus de détails sur l'événement (`Lire la suite`). Le lien dirige vers `/event/event.id`, où `event.id` est l'identifiant unique de l'événement.
  
* **Message d'absence d'événements (**`<% } else { %> ... <% } %>`): Si aucun événement n'est présent (`events.length <= 0`), il affiche un message disant "Aucun événement disponible pour le moment."
  

## Étape 9 : Créer des partials

Rappelez-vous que vous avez installé `ejs` dans votre application pour faciliter des composants plus dynamiques. Il vous permet de décomposer votre code davantage pour être plus dynamique.

Pour organiser davantage votre code, vous utiliserez quelque chose appelé **Partials**.

Les Partials vous permettent de décomposer votre code en parties modulaires, scalables et gérables, gardant votre HTML organisé.

Tout d'abord, créons un partial pour la barre de navigation.

### Comment créer un Partial :

* À l'intérieur de votre dossier `views`, créez un nouveau dossier nommé `partials`
  
* À l'intérieur du dossier `partials`, créez un nouveau fichier appelé `nav.ejs`.
  
* Coupez le code de la barre de navigation de votre fichier de page d'accueil et collez-le dans `nav.ejs`.
  
### Exemple :

Tout d'abord, créez le dossier Partials et le fichier :

![nav partial](https://www.freecodecamp.org/news/content/images/2024/07/partial.png align="left")

*nav partial*

Utilisez la syntaxe `<%- include() %>` de `ejs` pour inclure le partial `nav.ejs` à travers les pages de votre application où vous voulez que la barre de navigation apparaisse.

![Include ()](https://www.freecodecamp.org/news/content/images/2024/07/include.png align="left")

*Syntaxe Include ()*

Voici le code :

```js
<!DOCTYPE html>
<html lang="en">
    <%- include('./partial/head.ejs') %>

<body>
    <%- include('./partial/nav.ejs') %>
    <main>
      hello
    </main>
      <%- include('./partial/footer.ejs') %>
</body>
</html>
```

Avec cette configuration, votre code HTML sera organisé. Il sera facile à gérer et à mettre à jour les composants comme la barre de navigation à travers différentes pages. Vous pouvez utiliser cette approche sur d'autres parties de votre application. Par exemple, la balise head, la balise footer, et d'autres composants réutilisables.

## Étape 10 : Créer un fichier de variables d'environnement (.Env)

Dans ce tutoriel, nous allons télécharger le projet sur GitHub. Vous protégerez votre numéro de port et l'URL MongoDB avec un stockage sécurisé. Vous utiliserez également un fichier de variables d'environnement, un fichier de configuration connu sous le nom de .env. Ce fichier garde les informations sensibles en sécurité. Il inclut les mots de passe et les URL d'API et empêche l'exposition.

Voici comment le configurer en utilisant Node.js :

Tout d'abord, installez le package `[dotenv](https://www.npmjs.com/package/dotenv)`.

```js
npm i dotenv
```

Ensuite, créez un fichier `.env`. À l'intérieur, ajoutez votre numéro de PORT et l'URL MongoDB. Cela devrait ressembler à ceci :

```plaintext
PORT=3000
dbURl='mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority';
```

Ensuite, mettez à jour votre fichier `.gitignore` :

```plaintext

/node_modules
.env
```

L'ajout de .env à votre .gitignore garantit qu'il n'est pas inclus dans votre dépôt GitHub. Cela indique à Git d'ignorer le fichier .env lors du téléchargement de votre code.

Ensuite, dans votre fichier `server.js`, requérez le package `dotenv`. Chargez les variables avec cette ligne en haut du fichier :

Pour le requérir, tapez simplement :

```js
require('dotenv').config();
```

De cette façon, vous n'avez pas besoin de coder en dur le numéro de PORT et l'URL MongoDB dans votre fichier `server.js`. Au lieu de cela, vous pouvez y accéder en utilisant `process.env.PORT` et `process.env.dbURl`.

Ainsi, votre fichier `server.js` sera plus propre et moins encombré 😵💻

```js
require('dotenv').config();
const express = require('express');
const ejs = require('ejs');
const mongoose = require('mongoose');

mongoose
  .connect(process.env.dbURL)
  .then((result) => {
    console.log('Connecté à MongoDB');
    app.listen(3000, () => {
      console.log('Serveur démarré sur le port 3000');
    });
  })
  .catch((err) => {
    console.error('Impossible de se connecter à MongoDB :', err);
  });
```

## Étapes suivantes

Pour développer cette application de base, envisagez d'ajouter des fonctionnalités telles que :

* Authentification des utilisateurs
  
* Fonctionnalité de recherche et de filtrage d'événements
  
* Édition et suppression d'événements
  
* Notifications pour les événements à venir
  

### Comment styliser l'application

Si vous souhaitez ajouter du style à votre application, suivez ces étapes :

Tout d'abord, créez un dossier `public`. À l'intérieur de ce dossier, créez un fichier `style.css` où vous écrirez votre CSS personnalisé.

Ensuite, dans votre fichier `HTML`, liez le fichier `style.css` dans la balise `<head>` comme vous le feriez normalement :

```js
<link rel="stylesheet" href="/style.css">
```

Pour vous assurer que votre fichier CSS est servi correctement, ajoutez la ligne suivante à votre fichier `server.js` :

```js
app.use(express.static('public'));
```

Cette application utilise Tailwind CSS pour le style. Mais l'utilisation de Tailwind est facultative. Vous pouvez utiliser n'importe quel framework CSS ou écrire du CSS personnalisé pour obtenir la mise en page souhaitée.

### Comment inclure des images

Toutes les images doivent être stockées dans le dossier `public` et référencées dans vos fichiers HTML. Vous devez également vous assurer que le dossier `public` est correctement configuré dans votre fichier `server.js` pour servir des fichiers statiques.

Voici un exemple de la façon de servir des fichiers statiques dans `server.js` :

```js
const express = require('express');
const app = express();


// Servir des fichiers statiques depuis le dossier 'public'
app.use(express.static('public'));
```

## Conclusion

Félicitations ! Vous avez construit une application simple en utilisant Node.js, Express.js, ejs et MongoDB. Avec ces bases, vous pouvez développer et améliorer votre application pour répondre à des besoins et fonctionnalités plus spécifiques.

N'hésitez pas à partager vos progrès ou à poser des questions si vous rencontrez des problèmes.

Si vous avez trouvé cet article utile, partagez-le avec d'autres qui pourraient également le trouver intéressant.

Restez à jour avec mes projets en me suivant sur [Twitter](https://https//twitter.com/ijaydimples), [LinkedIn](https://www.linkedin.com/in/ijeoma-igboagu/) et [GitHub](https://github.com/ijayhub)

Merci d'avoir lu 💖.

Bonne programmation !