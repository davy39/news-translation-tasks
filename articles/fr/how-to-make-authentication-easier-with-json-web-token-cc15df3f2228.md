---
title: Comment simplifier l'authentification de votre application en utilisant JSON
  Web Token
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-06-07T15:55:03.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-authentication-easier-with-json-web-token-cc15df3f2228
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_1sCpXcnCbvwlJ6uvAKIhw.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment simplifier l'authentification de votre application en utilisant
  JSON Web Token
seo_desc: 'By Sudheesh Shetty

  Every application we come across today implements security measures so that the
  user data is not misused. Security is always something that is changing and evolving.
  Authentication is one of the essential part of every application....'
---

Par Sudheesh Shetty

Chaque application que nous rencontrons aujourd'hui met en œuvre des mesures de sécurité afin que les données des utilisateurs ne soient pas détournées. La sécurité est toujours quelque chose qui change et évolue. L'authentification est l'une des parties essentielles de chaque application.

Il existe diverses façons d'authentifier l'utilisateur. Discutons de l'authentification basée sur les tokens en utilisant une application node.js. Pour cela, nous utiliserons les JSON Web Tokens.

### Qu'est-ce que les JSON Web Tokens (JWT) ?

Les JSON Web Tokens (JWT) sont une norme qui définit une manière compacte et autonome de transmettre en toute sécurité des informations entre les parties sous forme d'objet JSON.

* **Compact** : Taille plus petite pour un transfert facile.
* **Autonome** : Il contient toutes les informations sur l'utilisateur.

### Comment fonctionnent-ils ?

Lorsque l'utilisateur envoie une requête avec les paramètres requis comme le nom d'utilisateur et le mot de passe. L'application vérifie si le nom d'utilisateur et le mot de passe sont valides. Après validation, l'application créera un token en utilisant une charge utile et une clé secrète. Elle renverra ensuite le token à l'utilisateur pour qu'il le stocke et l'envoie avec chaque requête. Lorsque l'utilisateur envoie une requête avec ce token, l'application vérifie sa validité avec la même clé secrète. Si le token est valide, la requête est servie, sinon l'application enverra un message d'erreur approprié.

![Image](https://cdn-media-1.freecodecamp.org/images/1*YO9j_eWCQLSfb4OxwoorrQ.jpeg)
_Flux de génération de token_

### Structure

La structure de base d'un JWT est quelque chose comme

```
header payload signature
```

* **header** : Il contient le type de token et l'algorithme utilisé pour créer la signature. Encodé en base64.
* **payload** : Toutes données utilisateur personnalisées comme le nom d'utilisateur et l'email.
* **signature** : Hachage du header encodé, de la charge utile et d'une clé secrète.

### Avantages des JWT

* **Clé unique** : Il n'est pas nécessaire d'appeler la base de données à chaque fois pour vérifier l'utilisateur. Une seule clé secrète décodera les tokens fournis par n'importe quel utilisateur.
* **Portable** : Le même token peut être utilisé parmi différents domaines ou différentes plateformes. Tout ce dont il a besoin est la clé.
* **Expiration facile** : On peut définir un temps d'expiration en utilisant JWT. Après ce temps, le JWT expire.

### Comment pouvons-nous le faire ?

Nous allons construire une application node.js avec quelques routes et les authentifier en utilisant des tokens. Une connaissance de base de node.js et de javascript est requise.

**Étape 1** — Ouvrez le terminal. Démarrez un nouveau projet dans un répertoire

```
cd auth
```

```
npm init
```

Cela démarrera un nouveau projet. Le processus demandera certaines informations. Fournissez tous les détails requis. Le processus créera _package.json_ et il ressemblera à quelque chose comme ceci.

```
{  "name": "auth",  "version": "1.0.0",  "description": "application pour expliquer l'authentification",  "main": "server.js",  "scripts": {    "test": "echo \"Erreur : aucun test spécifié\" && exit 1"  },  "author": "Votre nom",  "license": "ISC"}
```

**Étape 2** — Installez les dépendances. Retournez dans le terminal et collez la ligne suivante.

```
npm install express body-parser jsonwebtoken --save
```

* **_express:_** _Framework_ d'application web _Node.js_.
* **_body-parser:_** Pour obtenir les paramètres de notre requête POST.
* **_jsonwebtoken:_** Pour créer et vérifier les tokens.

Après avoir installé les dépendances, notre package.json ressemblera à quelque chose comme ceci :

```
{  "name": "auth",  "version": "1.0.0",  "description": "application pour expliquer l'authentification",  "main": "server.js",  "scripts": {    "test": "echo \"Erreur : aucun test spécifié\" && exit 1"  },  "author": "Votre nom",  "license": "ISC",  "dependencies": {    "body-parser": "^1.17.2",    "express": "^4.15.3",    "jsonwebtoken": "^7.4.1"  }}
```

**Étape 3 —** Créez le serveur

Créons un serveur, servant sur le port 3000 qui envoie le fichier index.html lorsque la route `/` est appelée. Nous allons également créer une API `/login` qui authentifie l'utilisateur et une API `/getusers` qui donne la liste des utilisateurs. Créons des données fictives pour l'instant et stockons-les dans le tableau 'users'. Vous pouvez également les remplacer par des appels à la base de données.

**Étape 4 —** Construisez le Client

Créons un client en utilisant HTML, Bootstrap et JavaScript. Notre client a deux parties : un écran de connexion et un endroit pour récupérer les utilisateurs. L'écran de connexion contiendra des zones de texte pour l'email et le mot de passe et un bouton pour envoyer la requête. Nous ajouterons également une zone de texte et un bouton pour passer le token et obtenir la liste des utilisateurs.

**Étape 5 —** Démarrez l'application

```
node server.js
```

### Notre application est-elle sécurisée ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*8zQJKP0zeK9dRKizu5k5kA.gif)

Non, vous pourriez voir que même si vous ne passez pas le token, vous pouvez obtenir la liste de tous les utilisateurs. Nous n'avons pas encore implémenté l'authentification. Ajoutons l'authentification à l'API `/getusers` afin que les utilisateurs avec un token valide puissent récupérer la liste des utilisateurs.

### Comment ajouter l'authentification ?

1. Incluez JWT dans le fichier server.js.

```
var jwt=require('jsonwebtoken');
```

2. Passez la charge utile (n'importe quel objet, ici passez l'objet utilisateur lui-même) et une chaîne secrète à la fonction sign pour créer un token.

```
var token=jwt.sign(<user>,<secret>);
```

3. Lorsque le token est créé avec succès, passez-le au client.

```
res.json({token:token});
```

Vous pouvez ensuite stocker le token côté client et le passer à chaque fois pendant la session pour l'authentification. Changeons la fonction "getlist" afin que nous puissions passer le token au serveur lorsque nous voulons accéder à la liste des utilisateurs.

Ajoutons un middleware pour authentifier `/getusers` ou toute route sécurisée qui sera ajoutée à l'avenir. Assurez-vous que toutes les routes nécessitant une authentification sont en dessous du middleware.

Dans server.js, nous avons d'abord la route de connexion qui crée le token. Après cela, nous avons le middleware que nous utiliserons pour vérifier le token. Toutes les routes nécessitant une authentification sont après le middleware. L'ordre est très important.

4. Pour décoder, vous passez le token et la clé secrète à la fonction verify. La fonction retournera une erreur si le token est invalide ou un succès si le token est valide.

```
jwt.verify(token,"samplesecret",(err,decod)=>{  //votre logique})
```

Appelez next() afin que les routes respectives soient appelées.

Le fichier server.js final ressemblera à ceci :

Le fichier index.html final ressemblera à ceci :

C'est tout. C'est un exemple simple de la façon d'utiliser un token pour authentifier votre application. J'ai mis le code complet sur GitHub. Vous pouvez le vérifier là-bas.

[**sudheeshshetty/JWT_Auth**](https://github.com/sudheeshshetty/JWT_Auth)  
[_Contribuez au développement de JWT_Auth en créant un compte sur GitHub._github.com](https://github.com/sudheeshshetty/JWT_Auth)

Merci d'avoir lu et n'oubliez pas de me suivre et de recommander cela aux autres en cliquant sur F491. Mon compte Twitter est [sudheeshshetty](https://twitter.com/sudheeshshetty).