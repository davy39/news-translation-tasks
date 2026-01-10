---
title: Apprenez à gérer l'authentification avec Node en utilisant Passport.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-12T17:44:27.000Z'
originalURL: https://freecodecamp.org/news/learn-how-to-handle-authentication-with-node-using-passport-js-4a56ed18e81e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*OUk_mC8ojHhStMEURjbI8g.jpeg
tags: []
seo_title: Apprenez à gérer l'authentification avec Node en utilisant Passport.js
seo_desc: 'By Antonio Erdeljac

  Support me by reading it from its original source: ORIGINAL SOURCE

  In this article you will learn how to handle authentication for your Node server
  using Passport.js. This article does not cover Frontend authentication. Use this
  t...'
---

Par Antonio Erdeljac

Soutenez-moi en le lisant depuis sa source originale : [**SOURCE ORIGINALE**](https://www.signet.hr/learn-how-to-handle-authentication-with-node-using-passport-js/)

Dans cet article, vous apprendrez à gérer l'**authentification** pour votre serveur Node en utilisant **Passport.js**. Cet article **ne couvre pas l'authentification Frontend**. Utilisez ceci pour configurer votre **authentification Backend** (générer un token pour chaque utilisateur et protéger les routes).

Gardez à l'esprit que **si vous êtes bloqué à une étape, vous pouvez vous référer à ce [dépôt GitHub](https://github.com/AntonioErdeljac/passport-tutorial)**.

### Dans cet article, je vais vous enseigner ce qui suit :

* Gestion des routes protégées
* Gestion des tokens JWT
* Gestion des réponses non autorisées
* Création d'une API basique
* Création de modèles et de schémas

### Introduction

#### Qu'est-ce que Passport.js ?

Passport est un middleware d'authentification pour [Node.js](https://nodejs.org/). Étant extrêmement flexible et modulaire, Passport peut être intégré discrètement dans toute application web basée sur [Express](https://expressjs.com/). Un ensemble complet de stratégies prend en charge l'authentification en utilisant un [nom d'utilisateur et un mot de passe](http://www.passportjs.org/docs/username-password/), [Facebook](http://www.passportjs.org/docs/facebook/), [Twitter](http://www.passportjs.org/docs/twitter/), et [plus encore](http://www.passportjs.org/packages/). En savoir plus sur Passport [ici](http://www.passportjs.org/).

### Tutoriel

#### Création de notre serveur Node à partir de zéro

Créez un nouveau répertoire avec ce fichier "app.js" à l'intérieur :

<script src="https://gist.github.com/AntonioErdeljac/3fada52d3c4efa8ef5cd04408bebaee0.js"></script>

Nous allons installer [nodemon](https://github.com/JakRowan/nodenom/blob/master/package.json) pour un développement plus facile.

<script src="https://gist.github.com/AntonioErdeljac/bdfca5e9df272ff71db047d5ed7e3f96.js"></script>

Ensuite, nous allons exécuter notre "app.js" avec celui-ci.

```bash
$ nodemon app.js
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*6kdVzksHWBymrCL20pNyzA.png)
_Résultat attendu après l'exécution de la commande ci-dessus_

#### Création du modèle utilisateur

Créez un nouveau dossier appelé "models", et créez le fichier "Users.js" à l'intérieur de ce dossier. C'est ici que nous allons définir notre "UsersSchema". Nous allons utiliser `JWT` et `Crypto` pour générer `hash` et `salt` à partir de la chaîne de caractères `password` reçue. Cela sera utilisé plus tard pour valider l'utilisateur.

<script src="https://gist.github.com/AntonioErdeljac/d4b1611e8ce92943c067b3a6ab51154b.js"></script>

![Image](https://cdn-media-1.freecodecamp.org/images/1*updLloBs1oJyVGplMGG4lQ.png)
_Vous devriez maintenant avoir cette structure_

Ajoutons notre nouveau modèle à "app.js".

Ajoutez la ligne suivante à votre fichier "app.js" après avoir configuré `Mongoose` :

```js
require('./models/Users');
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*YDxu9Xcr1SqDjQLzTVI9MA.png)

#### Configurer Passport

Créez un nouveau dossier "config" avec le fichier "passport.js" à l'intérieur :

<script src="https://gist.github.com/AntonioErdeljac/3baa23e152bbc068eebd730e05918eca.js"></script>

Dans ce fichier, nous utilisons la méthode `validatePassword` que nous avons définie dans le `User model`. En fonction du résultat, nous retournons une sortie différente de la `LocalStrategy` de Passport.

![Image](https://cdn-media-1.freecodecamp.org/images/1*TxTXHZEmeZoEff1TeW9hDA.png)
_Vous devriez maintenant avoir cette structure_

Connectons "passport.js" à notre fichier "app.js". Ajoutez la ligne suivante **en dessous de tous** les `models` :

```js
require('./config/passport');
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*_Uem3m6YuPSnhx9DZsJ5sA.png)
_Le require de Passport doit être en dessous de tous les modèles_

#### Routes et options d'authentification

Créez un nouveau dossier appelé "routes" avec le fichier "auth.js" à l'intérieur.

Dans ce fichier, nous utilisons la fonction `getTokenFromHeaders` pour obtenir un **JWT token** qui sera envoyé depuis le **côté client** dans les **en-têtes de la requête**. Nous créons également un objet `auth` avec les propriétés `optional` et `required`. Nous utiliserons celles-ci plus tard dans nos routes.

<script src="https://gist.github.com/AntonioErdeljac/e78af14bb27bb63ebdd1ab9fb8e29bd5.js"></script>

Dans le même dossier "routes", créez un fichier "index.js" :

<script src="https://gist.github.com/AntonioErdeljac/b83682d7192df9c4ceb7026cedee2610.js"></script>

Nous avons maintenant besoin d'un dossier "api" à l'intérieur du dossier "routes", avec un autre fichier "index.js" à l'intérieur.

<script src="https://gist.github.com/AntonioErdeljac/158effaaeb527f6d756cf3178a48b5c4.js"></script>

![Image](https://cdn-media-1.freecodecamp.org/images/1*xT-bMD4RPNbS0trhqltHQQ.png)
_Vous devriez maintenant avoir cette structure_

Maintenant, créons le fichier "users.js" que nous requérons dans "api/index.js".

Tout d'abord, nous allons créer une route **auth optionnelle** `‘/’` qui sera utilisée pour la création de nouveaux modèles (inscription).

```js
router.post('/', auth.optional, (req, res, next) ...
```

Après cela, nous allons créer une autre route **auth optionnelle** `‘/login’`. Cela sera utilisé pour activer notre configuration passport et valider un mot de passe reçu avec un email.

```js
router.post('/login', auth.optional, (req, res, next) ...
```

Enfin, nous allons créer une route **auth requise**, qui sera utilisée pour retourner l'utilisateur actuellement connecté. Seuls les utilisateurs connectés (utilisateurs dont le token est envoyé avec succès via les en-têtes de la requête) ont accès à cette route.

```js
router.get('/current', auth.required, (req, res, next) ...
```

<script src="https://gist.github.com/AntonioErdeljac/c787327eab1c1bb4e216fabe0fb9d8c3.js"></script>

![Image](https://cdn-media-1.freecodecamp.org/images/1*FhlHO36q_NTY73Qhw2Vfiw.png)
_Vous devriez maintenant avoir cette structure_

Ajoutons notre dossier "routes" à "app.js". Ajoutez la ligne suivante **en dessous de notre passport** `require` :

```js
app.use(require('./routes'));
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*B44dNEd8f0Ii5GDkNJ0fLQ.png)

### Test des routes

Je vais utiliser [Postman](https://www.getpostman.com/) pour envoyer des requêtes à notre serveur.

Notre serveur accepte le corps suivant :

```json
{
  "user": {
    "email": String,
    "password": String
  }
}
```

#### Création d'une requête POST pour créer un utilisateur

Corps de test :

![Image](https://cdn-media-1.freecodecamp.org/images/1*e_U1SfVcGty_8XAZ8gWuSQ.png)

Réponse :

```json
{
    "user": {
        "_id": "5b0f38772c46910f16a058c5",
        "email": "erdeljac.antonio@gmail.com",
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImVyZGVsamFjLmFudG9uaW9AZ21haWwuY29tIiwiaWQiOiI1YjBmMzg3NzJjNDY5MTBmMTZhMDU4YzUiLCJleHAiOjE1MzI5MDgxNTEsImlhdCI6MTUyNzcyNDE1MX0.4TWc1TzY6zToHx_O1Dl2I9Hf9krFTqPkNLHI5U9rn8c"
    }
}
```

Nous allons maintenant utiliser ce token et l'ajouter à nos "Headers" dans la configuration de Postman.

![Image](https://cdn-media-1.freecodecamp.org/images/1*3TqFAWgy1bULj-ECJRyKKw.png)

Et maintenant, testons notre route **auth only**.

#### Création d'une **requête GET pour retourner l'utilisateur actuellement connecté**

URL de la requête :

```
GET http://localhost:8000/api/users/current
```

Réponse :

```json
{
    "user": {
        "_id": "5b0f38772c46910f16a058c5",
        "email": "erdeljac.antonio@gmail.com",
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImVyZGVsamFjLmFudG9uaW9AZ21haWwuY29tIiwiaWQiOiI1YjBmMzg3NzJjNDY5MTBmMTZhMDU4YzUiLCJleHAiOjE1MzI5MDgzMTgsImlhdCI6MTUyNzcyNDMxOH0.5UnA2mpS-_puPwwxZEb4VxRGFHX6qJ_Fn3pytgGaJT0"
    }
}
```

Essayons de le faire **sans token dans les "Headers"**.

Réponse :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ggNxOl_DMzg6dklIJAKG3g.png)

### La fin

Merci d'avoir suivi ce tutoriel. Si vous remarquez des erreurs, veuillez me les signaler. **Si vous êtes bloqué à une étape**, veuillez vous référer à [ce dépôt GitHub](https://github.com/AntonioErdeljac/passport-tutorial).

**Vous pouvez me contacter via :**

* erdeljac DOT antonio AT gmail.com
* [Linkedin](https://www.linkedin.com/in/antonio-erdeljac/)

**Découvrez mon application [SwipeFeed](https://play.google.com/store/apps/details?id=com.swipefeed.android).**