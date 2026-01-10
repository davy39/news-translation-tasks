---
title: Comment créer une API CRUD – Projet NodeJS et Express pour débutants
subtitle: ''
author: Victor Yakubu
co_authors: []
series: null
date: '2024-03-08T11:04:53.000Z'
originalURL: https://freecodecamp.org/news/create-crud-api-project
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/Swimm-Images-4.png
tags:
- name: api
  slug: api
- name: backend
  slug: backend
- name: crud
  slug: crud
- name: Express.js
  slug: expressjs
- name: Node.js
  slug: nodejs
seo_title: Comment créer une API CRUD – Projet NodeJS et Express pour débutants
seo_desc: An API is a technology that powers communication between software applications
  on the internet. API stands for Application Programming Interface, and it is basically
  a set of rules and protocols that define how different software can interact with
  ea...
---

Une API est une technologie qui alimente la communication entre les applications logicielles sur Internet. API signifie Interface de Programmation d'Applications, et c'est essentiellement un ensemble de règles et de protocoles qui définissent comment différents logiciels peuvent interagir les uns avec les autres. 

Imaginez avoir deux programmes différents : le programme A et le programme B. Pour que ces deux programmes communiquent ensemble, une API est nécessaire, et un ensemble de règles garantit qu'ils savent à quoi s'attendre lorsqu'ils interagissent les uns avec les autres.

En tant que développeur backend, vos responsabilités impliquent la construction d'applications côté serveur, la gestion du stockage des données et la fourniture des fonctionnalités nécessaires pour faire tout cela via des API. 

Il existe [différents types d'API](https://blog.postman.com/different-types-of-apis/) comme REST, GraphQL, gRPC, SOAP et WebSockets. Cependant, en matière de développement web, l'une d'entre elles est plus populaire, et c'est l'[API REST](https://www.freecodecamp.org/news/what-is-a-rest-api/).

Dans cet article, vous apprendrez à créer une API CRUD avec Node.js et Express en utilisant l'architecture REST, et à la fin de cet article, vous devriez avoir une API entièrement fonctionnelle capable d'effectuer des opérations CRUD.

Alors, plongeons dans le monde du développement backend avec Node.js et Express et commençons notre voyage pour construire une API CRUD.

## Table des matières

* [Qu'est-ce qu'une API CRUD ?](#heading-questce-quune-api-crud)
* [Qu'est-ce que Node.js ?](#heading-questce-que-nodejs)
* [Pourquoi Node ?](#heading-pourquoi-node)
* [Comment installer Node.js](#heading-comment-installer-nodejs)
* [Qu'est-ce qu'Express ?](#heading-questce-que-express)
* [Pourquoi avez-vous besoin d'Express ?](#heading-pourquoi-avez-vous-besoin-dexpress)
* [Prérequis](#heading-prerequis)
* [Comment configurer votre environnement de développement](#heading-comment-configurer-votre-environnement-de-developpement)
* [Comment configurer un serveur pour votre API RESTful CRUD avec Node.js et Express](#heading-comment-configurer-un-serveur-pour-votre-api-restful-crud-avec-nodejs-et-express)
* [Exemple d'API CRUD](#heading-exemple-dapi-crud)
* [Comment créer des routes d'API](#heading-comment-creer-des-routes-dapi)
* [Comment créer votre propre API CRUD](#heading-comment-creer-votre-propre-api-crud)
* [Comment créer le point de terminaison GET /users](#heading-comment-creer-le-point-de-terminaison-get-users)
* [Comment tester votre requête API GET](#heading-comment-tester-votre-requete-api-get)
* [Comment créer le point de terminaison POST /users](#heading-comment-creer-le-point-de-terminaison-post-users)
* [Comment tester la requête POST](#heading-comment-tester-la-requete-post)
* [Comment créer le point de terminaison GET /users/:id](#heading-comment-creer-le-point-de-terminaison-get-usersid)
* [Comment tester la requête GET](#heading-comment-tester-la-requete-get)
* [Comment créer le DELETE /users/:id](#heading-comment-creer-le-delete-usersid)
* [Comment tester la requête DELETE](#heading-comment-tester-la-requete-delete)
* [Comment créer le point de terminaison PATCH /users/:id](#heading-comment-creer-le-point-de-terminaison-patch-usersid)
* [Comment tester la requête PATCH](#heading-comment-tester-la-requete-patch)
* [Conclusion](#heading-conclusion)

## Qu'est-ce qu'une API CRUD ?

Dans le développement web, les opérations CRUD sont le pain et le beurre des systèmes backend. Cela est dû au fait qu'elles permettent de "Créer", "Lire", "Mettre à jour" et "Supprimer" des données via votre API. 

Voici un aperçu rapide des quatre méthodes HTTP principales associées aux opérations CRUD :

* **GET** : Utilisé pour lire ou récupérer des données depuis le serveur.
* **POST** : Utilisé pour créer de nouvelles données sur le serveur.
* **PUT** : Utilisé pour mettre à jour des données existantes sur le serveur.
* **DELETE** : Utilisé pour supprimer des données du serveur.

Pratiquement toutes les applications web interagissent avec une base de données pour effectuer ces quatre opérations principales. Qu'il s'agisse d'une plateforme de médias sociaux, d'un site web de commerce électronique ou d'une application météo, elles reposent toutes sur la création, la lecture, la mise à jour et la suppression de données. 

Par exemple, WhatsApp a récemment ajouté une fonction d'édition à l'application, permettant aux utilisateurs de faire des corrections à un message déjà envoyé. C'est une partie de l'opération CRUD en action (mise à jour).

Dans le contexte de la construction d'une API web, ces opérations deviennent l'épine dorsale de la manière dont votre application interagit avec les données. Votre API fournit des points de terminaison qui permettent aux applications clientes (comme les applications web ou mobiles) d'effectuer ces opérations sur le serveur. 

Cette communication entre le client et le serveur est l'essence du développement web, et comprendre comment créer une API CRUD est une compétence cruciale pour un développeur web.

## Qu'est-ce que Node.js ?

Node.js est un environnement d'exécution open-source et multiplateforme pour exécuter du code JavaScript en dehors d'un navigateur. Très souvent, nous l'utilisons pour construire des services backend, également appelés API. Node est idéal pour construire des services backend hautement scalables, intensifs en données et en temps réel qui alimentent nos applications clientes.

## Pourquoi Node ?

* C'est l'un des choix les plus populaires pour construire le backend.
* Vous pouvez écrire du JavaScript sur toute votre stack, ce qui facilite la transition d'un développeur frontend à un développeur backend et vice versa.
* Il permet une mise à l'échelle facile des applications, ce qui en fait un bon choix pour les grands projets professionnels.
* Il est rapide et non bloquant. Cela est dû à la nature asynchrone et pilotée par événements de Node.js.
* Node.js dispose d'une communauté dynamique et d'un riche écosystème de packages et de bibliothèques.

## Comment installer Node.js

Étapes d'installation :

1. Téléchargez l'installateur Mac/Windows depuis le [site web de Node.js](https://nodejs.org/en/download).
2. Choisissez la version Long-Term Support (LTS) qui est affichée à gauche.
3. Après le téléchargement, installez/exécutez l'installateur, puis suivez les invites. (Vous devrez cliquer sur le bouton SUIVANT plusieurs fois et accepter les paramètres d'installation par défaut).
4. Pour confirmer que Node a été installé avec succès, ouvrez votre terminal et exécutez la commande. (Pour Windows, vous devrez peut-être redémarrer votre commande avant de l'exécuter.)

```
node --version
```

## Qu'est-ce qu'Express ?

Express est un framework backend web ou côté serveur rapide, minimaliste et non opinionné pour Node.js. Basiquement, il vous donne la capacité de construire vos API comme vous le souhaitez, avec moins de code.

C'est un framework construit sur Node.js qui vous permet de créer votre backend avec facilité. Vous pouvez utiliser Express en combinaison avec des frameworks frontend comme React, Angular ou Vue pour construire des applications full-stack.

## Pourquoi avez-vous besoin d'Express ?

* Il facilite grandement la construction d'applications web avec Node.js.
* Il est extrêmement léger, rapide et gratuit.
* Il est utilisé pour les applications rendues côté serveur ainsi que pour les API/Microservices.
* C'est le Node le plus populaire.
* Il vous donne un contrôle total sur les requêtes et les réponses.

## Prérequis

Pour suivre ce tutoriel, vous aurez besoin des éléments suivants :

* Connaissance de base de JavaScript
* Téléchargez et installez [Node.js](https://nodejs.org/en) et [Postman](https://www.postman.com/downloads/) sur votre ordinateur

Voir le code complet de ce tutoriel sur [Github](https://github.com/Aviatorscode2/crud-api-tutorial).

## Comment configurer votre environnement de développement

Avant de plonger dans la création de votre API, passons par le processus de création d'un serveur de base sur votre ordinateur local. 

Voici les étapes à suivre :

### Étape #1 – Créer un répertoire

Créez un répertoire/dossier sur votre ordinateur. Ouvrez le dossier dans un éditeur de code.

### Étape #2 – Créer le fichier index.js

Créez un fichier **index.js** à l'intérieur du dossier en utilisant cette commande :

```
touch index.js
```

### Étape #3 – Initialiser NPM

Initialisez NPM à l'intérieur du dossier en exécutant cette commande dans votre terminal :

```
npm init -y
```

La commande créera un fichier **package.json** avec des valeurs par défaut.

### Étape #5 – Installer Express

Utilisez la commande ci-dessous pour installer Express.js

```
npm install express
```

Après avoir installé Express, allez dans le fichier **package.json** et incluez **"type" : "module"**. Cette déclaration indiquera à Node que ce projet utilisera la [syntaxe des modules ES6](https://nodejs.org/api/packages.html#type) (import/export) au lieu de common.js, qui est le défaut dans Node.  


![Image](https://lh7-us.googleusercontent.com/s0sHrHSK7ulqOU4Ddw6WzER6waGEGaCxV26mk-ieuqDVKYBZSKlJ1aDW8WXbCOlfzC1xcW8lXh1-HVSNnYUXYM3MRmmy0N-6uQh-J3qDnjHtxB5atRbJQ-cxR1AWzLTa9RTwv_cXNXpNGz3lbSBHejM)
_fichier package.json avec `type:module`_

## Comment configurer un serveur pour votre API RESTful CRUD avec Node.js et Express

Pour créer une API [RESTful](https://www.freecodecamp.org/news/what-is-rest-rest-api-definition-for-beginners/#:~:text=An%20API%20that%20complies%20with%20some%20or%20all%20of%20the%20six%20guiding%20constraints%20of%20REST%20is%20considered%20to%20be%20RESTful.) CRUD, vous devez d'abord configurer votre serveur. Vous pouvez le faire en suivant ces étapes :

### Étape #1 – Écrire votre code d'application serveur dans le fichier index.js

Basiquement, un code de serveur ressemblera à ceci :

```javascript
import express from 'express';
import bodyParser from 'body-parser'

const app = express();
const PORT = 5000

app.use(bodyParser.json());

app.listen(PORT, () => console.log(`Serveur en cours d'exécution sur le port : http://localhost:${PORT}`));

```

Voici une explication pour le code ci-dessus :

* Dans la première ligne, nous avons importé `express` depuis le module Express que nous avons installé.
* Le `bodyParser` vient avec Express, et il nous permet de prendre en charge le corps de la requête POST entrante.
* Ensuite, nous avons créé une `app` en utilisant l'objet `express`.
* Nous avons ensuite spécifié le port pour l'application – il a été défini sur **5000** (si vous obtenez une erreur en utilisant ce port, il se peut que le port soit actuellement utilisé par une autre application, vous pouvez donc soit changer votre port, soit arrêter l'autre application d'utiliser le port).
* Ensuite, nous avons spécifié que les données JSON seront utilisées dans l'application.
* Une fois cela créé, nous avons utilisé la méthode `listen` sur l'`app` pour faire en sorte que notre application écoute les requêtes entrantes. La méthode accepte deux choses : le **PORT**, où nous écouterons les requêtes de notre côté client, et une fonction de rappel qui sera déclenchée lorsque notre serveur sera configuré.

### Étape #2 – Démarrer le serveur

Vous pouvez maintenant démarrer votre serveur en exécutant cette commande. Si vous avez utilisé un fichier différent, remplacez index.js par le nom du fichier où se trouve le serveur.

```
node index.js
```

Votre serveur devrait maintenant être en cours d'exécution sur le **port 5000**. Vous pouvez vérifier que votre serveur est en cours d'exécution sur votre terminal.

### Étape #3 – Installer Nodemon (Optionnel)

Pour le moment, chaque fois que vous apportez des modifications à votre fichier serveur, vous devrez redémarrer le serveur avant que vos modifications ne soient prises en compte (vous pouvez essayer et voir). Pour résoudre ce problème, vous pouvez utiliser Nodemon. Exécutez la commande pour l'installer :

```
npm install nodemon
```

Pour utiliser Nodemon, rendez-vous dans votre fichier **package.json** et configurez un script. Remplacez votre script de démarrage par ceci :

```
"start": "nodemon index.js"
```

Notez que **index.js** est le fichier où le code du serveur est écrit.

Vous pouvez maintenant démarrer votre serveur en exécutant cette commande :

```
npm start
```

Avec ce code, nous avons configuré un serveur qui écoute sur le port 5000 et affiche un message lorsqu'il démarre. Mais ce n'est qu'un début car notre serveur doit faire beaucoup plus. 

Explorons comment gérer les requêtes API ensuite.

## Exemple d'API CRUD

Commençons par définir les routes de l'API pour chaque opération CRUD. Ces routes serviront de points d'entrée pour votre API, et elles mapperont des actions spécifiques que nous voulons effectuer sur nos données. 

Dans notre cas, ces actions sont la création, la lecture, la mise à jour et la suppression de données.

## Comment créer des routes d'API

Lorsque le port ([http://localhost:5000/](http://localhost:5000/)) est ouvert dans un navigateur, vous obtiendrez une erreur.

![Image](https://lh7-us.googleusercontent.com/p-3qnXzvHDxcsbhpYXO4VMopivQMhqgSPwSTXXDQJW_2GRhFFvkpL8JitNShGcrjyQiMx87ZwkK_4iEbs3JieTdRJQ13Q94O0hV7U9mwOpcm9ET7Yngb2TXQpItUrpepYzeXzg4rZMGdnxonhMREHAo)
_localhost:5000 dans le navigateur sans aucune route_

Cela est dû au fait que Node.js et Express sont tous deux basés sur le routage, et nous n'avons encore aucune route. 

Vous pouvez définir des routes d'API en utilisant les méthodes `app.get()`, `app.post()`, `app.put()` et `app.delete()` dans votre application Express (dans le fichier **index.js**). 

Voici comment créer une route pour gérer les requêtes GET en utilisant la fonction `app.get()` :

```
app.get('/', (req, res)
```

La fonction `app.get()` accepte deux paramètres. Le premier est utilisé pour spécifier le chemin (dans ce cas, il s'agit de '/'). 

Le deuxième paramètre est une fonction de rappel où vous définissez ce qui se passe lorsque la requête GET est appelée. La fonction a également [deux paramètres](https://www.freecodecamp.org/news/express-explained-with-examples-installation-routing-middleware-and-more/) : le corps de la requête (`req`), qui peut contenir des informations telles que la chaîne de requête, les paramètres, le corps et les en-têtes HTTP. Alors que l'objet de réponse (`res`) contient les informations que vous souhaitez envoyer.

Voici le code complet :

```javascript
import express from 'express';
import bodyParser from 'body-parser'
const app = express();

const PORT = 5000;

app.use(bodyParser.json());

app.get('/', (req, res) => {
    console.log('[ROUTE GET]');
    res.send('BONJOUR DE LA PAGE D\'ACCUEIL');
})

app.listen(PORT, () => console.log(`Serveur en cours d\'exécution sur le port : http://localhost:${PORT}`));

```

Lorsque vous retournez à [http://localhost:5000/](http://localhost:5000/) et que vous l'actualisez, vous ne devriez plus obtenir d'erreur.

![Image](https://lh7-us.googleusercontent.com/6289p5Vl_k4v2ULLd5iUVCpr-sykpbcEytcHsqoJZTB4MgWgDEfVuH1_4aTt0w9ThAhFNCn_rMrlwNFB2hfgOKWQ3znH3MHnHRxh0sd1czb_ntBHMIWS6HtAIo3yuCgDEFK7RVFGvTel0s89T3qTKjc)
_localhost:5000 dans le navigateur avec la route GET_

## Comment créer votre propre API CRUD

Pour cette API, vous allez gérer un ensemble d'utilisateurs. La gestion des utilisateurs dans une base de données est un excellent exemple car c'est un cas d'utilisation courant dans la plupart des applications. 

Voici les points de terminaison de l'API que vous allez créer :

1. GET /users - trouver tous les utilisateurs
2. POST /users - créer un utilisateur
3. GET /users/:id - trouver un utilisateur spécifique
4. DELETE /users/:id - supprimer un utilisateur spécifique
5. PATCH /users/:id - mettre à jour un utilisateur spécifique.

### Comment créer le point de terminaison GET /users

La lecture de données est l'une des opérations les plus courantes dans une API. Dans cet exemple, vous allez obtenir la liste de tous les utilisateurs dans votre base de données fictive. Ces informations seront présentées au format JSON.

Pour définir une route pour récupérer les données des utilisateurs depuis la base de données, suivez ces étapes :

* Créez un nouveau dossier appelé routes
* Créez un nouveau fichier appelé **users.js** à l'intérieur du dossier routes.
* Écrivez le code pour configurer le routeur GET.

```javascript
import express from 'express';
const router = express.Router();

// Base de données fictive
const users = [
  {
    first_name: 'John',
    last_name: 'Doe',
    email: 'johndoe@example.com',
  },
  {
    first_name: 'Alice',
    last_name: 'Smith',
    email: 'alicesmith@example.com',
  },
];

// Obtenir la liste des utilisateurs depuis la base de données fictive
router.get('/', (req, res) => {
    res.send(users);
})

export default router
```

Dans cet extrait de code :

* `import express from 'express';` importe le framework Express.js
* `const router = express.Router();` crée une nouvelle instance de routeur, stockée dans la variable router.
* La variable `users` sert de base de données fictive contenant un tableau d'utilisateurs.
* La fonction `router.get()` configure une route qui répond aux requêtes HTTP GET.
* La deuxième partie du code `(req, res) => { ... }` est une fonction de rappel. Elle est exécutée lorsqu'une requête est faite à la route GET.
* À l'intérieur de la fonction de rappel, nous avons utilisé `res.send(users)` pour envoyer une réponse au client. Dans cet exemple, nous envoyons la variable `users` comme réponse. Ainsi, lorsqu'un utilisateur accède à l'URL GET, le serveur répond en envoyant les données à l'intérieur de la variable `users` au format JSON au client.

Enregistrez vos modifications dans le fichier **users.js**. Ensuite, faites ce qui suit dans le fichier **index.js** :

Importez vos routes utilisateur depuis **user.js** :

```javascript
import userRoutes from './routes/users.js'
```

Utilisez la méthode `app.use`, et spécifiez le chemin et le gestionnaire de routeur :

```javascript
app.use('/users', userRoutes);
```

Lorsque l'utilisateur visite [http://localhost:5000/users](http://localhost:5000/users), le routeur est déclenché. Il agit effectivement comme un filtre, déterminant quand un ensemble spécifique de routes doit être appliqué.

Voici le code complet pour le fichier **index.js** :

```javascript
import express from 'express';
import bodyParser from 'body-parser'
const app = express();
import userRoutes from './routes/users.js'

const PORT = 5000;

app.use(bodyParser.json());

app.use('/users', userRoutes);

app.get('/', (req, res) => res.send('BONJOUR DE LA PAGE D\'ACCUEIL'))

app.get('/', (req, res));

app.listen(PORT, () => console.log(`Serveur en cours d\'exécution sur le port : http://localhost:${PORT}`));
```

#### **Comment tester votre requête API GET**

Vous pouvez utiliser soit un navigateur (les navigateurs ne peuvent être utilisés que pour effectuer des requêtes GET) soit Postman pour tester la requête GET. 

Copiez donc votre URL d'API, [http://localhost:5000/users](http://localhost:5000/users), et collez-la soit sur Postman soit dans votre navigateur. Si vous utilisez Postman, vous devrez d'abord faire une requête GET, puis coller votre URL d'API, et enfin cliquer sur envoyer. Après cela, vous verrez la liste des utilisateurs dans votre console Postman.

![Image](https://lh7-us.googleusercontent.com/XBhjewUFTBvBhc2larsYwqzS3-RHp7qFBrO4lvScf91EUFO5TEgt83iU48h9ArDK3EbrPwdS7_-WkI51JkDUHH4v2U9pWXdYMSbKeCpQrYRunvhuvAIAadzcAyj8y0hojjxs1CIlAo7TigoTJrM3y5c)
_test de la route GET postman_

### Comment créer le point de terminaison POST /users

Vous pouvez utiliser la requête POST pour ajouter des données à votre base de données. Elle accepte les entrées du client et les stocke dans la base de données. Pour créer des données dans notre API, nous allons définir une route qui accepte les requêtes POST et sauvegarde les données dans la base de données fictive que vous avez configurée. 

Mais avant cela, vous aurez besoin du package UUID. Utilisez cette commande pour l'installer :

```
npm install uuid
```

Ce package vous aidera à générer un identifiant unique pour chaque utilisateur que vous allez créer. Cela sera utile lorsque vous implémenterez les requêtes GET, DELETE et PATCH de l'utilisateur par ID, où vous aurez besoin d'un moyen d'identifier un utilisateur spécifique.

Donc, dans le fichier **users.js**, faites ce qui suit :

Importez le package `uuid` :

```
import { v4 as uuidv4 } from 'uuid';
```

Deuxièmement, vous devrez implémenter le code pour la requête POST. 

Voici à quoi cela ressemble :

```javascript
router.post('/', (req, res) => {
    const user = req.body;

    users.push({ ...user, id: uuidv4() });

    res.send(`${user.first_name} a été ajouté à la base de données`);
}) 
```

Dans cet extrait de code :

* La fonction `router.post()` configure une route qui répond aux requêtes HTTP POST. Cela signifie que lorsqu'un client envoie une requête POST à l'URL racine de votre application, cette route sera déclenchée.
* Dans la fonction de rappel `(req, res) => { ... }`, nous accédons à l'objet `req`, qui représente la requête entrante faite par le client. Plus précisément, nous nous intéressons à la propriété `req.body`. Cette propriété contient les données (prénom, nom et email) que le client enverra dans le corps de la requête POST.
* Avec `const user = req.body`, nous extrayons ces données de `req.body` et les stockons dans la variable `user`.
* Ensuite, nous avons ajouté les données `user` à un tableau appelé `users`. Pour nous assurer que chaque utilisateur a un identifiant unique, nous générons un identifiant unique universel (UUID) en utilisant une fonction comme `uuidv4()` et l'incluons comme id dans l'objet utilisateur. Cela aide à garder les enregistrements des utilisateurs distincts et identifiables.
* Enfin, nous avons utilisé `res.send()` pour envoyer une réponse au client. Dans ce cas, nous envoyons un message simple informant le client que l'utilisateur a été ajouté avec succès à la base de données. Le message inclut le prénom de l'utilisateur pour une touche personnalisée.

Voici le code complet

```javascript
import express from 'express';
import { v4 as uuidv4 } from 'uuid';

const router = express.Router();

const users = [];

// Ajout d'utilisateurs à notre base de données fictive

router.post('/', (req, res) => {
    const user = req.body;

    users.push({ ...user, id: uuidv4() });

    res.send(`${user.first_name} a été ajouté à la base de données`);
})  

export default router
```

#### **Comment tester la requête POST**

Voici les étapes à suivre pour faire une requête POST sur Postman :

* Allez sur Postman
* Ouvrez un nouvel onglet de requête
* Sélectionnez "POST" dans la liste des méthodes HTTP disponibles
* Dans le champ URL, entrez l'URL complète où vous souhaitez envoyer la requête POST ([http://localhost:5000/users](http://localhost:5000/users))
* Cliquez sur l'onglet "Body" dans la fenêtre de requête.
* Choisissez le format dans lequel vous souhaitez envoyer vos données POST (choisissez JSON).
* Entrez les données que vous souhaitez envoyer dans le corps de la requête. Ces données doivent correspondre au format attendu par le serveur.
* Enfin, cliquez sur "Envoyer"  


![Image](https://lh7-us.googleusercontent.com/olNqMdggCcvhUotN9ospAjg8r7t-HE_3yUqGrEkf_dKnCGTwFiKWQJB3x4dccUbHPlYbP-j8S7a2xBG3TpMvceVdmz_nC8zRtaRQzfeknyyo-OQJDwuSFZJkWPiQctDkoTYfZCsVnE1ljQN96Hxow54)
_test de la route POST postman_

Si cela réussit, vous obtiendrez une réponse disant : "Daanny a été ajouté à la base de données."

Pour confirmer qu'il a été ajouté, faites une requête GET, et vous devriez voir le nouvel utilisateur ajouté à votre base de données. (Remarque : Ces informations utilisateur seront perdues lorsque votre serveur redémarrera, car elles ne sont pas sauvegardées dans une base de données réelle).

![Image](https://lh7-us.googleusercontent.com/cHmJ3hcsMb5Vnj9zh_kSdqBMRrgtR1pQJ3-_DgHgukwdtyLrnG5AN0jyL4gGtzyTYUJj4w_ENO6ZqVsMZLqdnRytOgP4tR5A2B2T_TnDHNbRDEb9JAGF7SmTwVVwBczzg02JmLfWAucyeyMlnPs1Ehg)
_test de la route GET postman_

### Comment créer le point de terminaison GET /users/:id

Récupérer des données spécifiques basées sur un identifiant unique, tel qu'un ID d'utilisateur, est une opération courante. Il est souvent essentiel pour construire des fonctionnalités comme les profils d'utilisateurs ou récupérer des enregistrements individuels d'une base de données. 

Dans cette section, vous allez explorer comment utiliser ce point de terminaison (users/:id) pour récupérer les informations d'un utilisateur en fonction d'un ID d'utilisateur fourni. 

Commençons !

```javascript
router.get('/:id', (req, res) => {
    const { id } = req.params;

    const foundUser = users.find((user) => user.id === id)

    res.send(foundUser)
});
```

Voici ce que fait cet extrait de code :

* La fonction `router.get()` configure une route qui répond aux requêtes HTTP GET. Dans cet exemple, nous avons défini une route avec ('/:id'). La partie :id est un paramètre de route, qui nous permet de capturer une valeur dynamique depuis l'URL. Dans ce cas, il représente l'ID de l'utilisateur que nous voulons récupérer.
* Dans la fonction de rappel `(req, res) => { ... }`, nous pouvons accéder à l'objet `req`, qui représente la requête entrante faite par le client. Plus précisément, nous nous intéressons à `req.params`, qui contient les valeurs des paramètres de route. Dans ce cas, nous déstructurons `id` depuis `req.params`, extrayant ainsi l'ID de l'utilisateur depuis l'URL. Par exemple, si un client fait une requête GET à /users/123, l'id sera '123'.
* Nous avons utilisé la méthode `.find()` pour rechercher dans ces données en fonction de l'ID de l'utilisateur (id) capturé depuis l'URL. Cette méthode tente de trouver un utilisateur dont l'ID correspond à l'id fourni.
* Une fois que nous avons localisé les données de l'utilisateur (si elles existent), nous les envoyons comme réponse en utilisant `res.send(foundUser)`. La variable `foundUser` contient l'objet utilisateur qui correspond à l'ID demandé.

#### **Comment tester la requête GET**

Pour tester l'API, suivez ces étapes :

* Allez dans votre onglet de requête POST et faites autant de requêtes que vous le souhaitez pour ajouter un nouvel utilisateur à la base de données.
* Allez dans votre onglet de requête GET et faites une requête pour voir la liste des utilisateurs que vous avez ajoutés

![Image](https://lh7-us.googleusercontent.com/qEuvm-1QKHvGmFCmru5dF2b9JSW5ua_dMcovZaKFZL_NChfSQqaazX4QvvSrSkjMzTO9Yqon5zhsZ5ZZwrWO0WifthlOKfboojC6ws8Fju2HK5TcE1oLvZZhOaO5xljRIUvYt_oun_NsIH13sq2Yf0o)
_test de la route GET postman_

* Copiez l'id de l'un des utilisateurs de la liste
* Créez un nouvel onglet de requête GET, copiez l'URL de base de l'API et ajoutez l'id de l'un des utilisateurs. Elle doit être dans un format comme ceci : [http://localhost:5000/users/734a9e75-b3f5-415f-82fb-79b4fdf1a593](http://localhost:5000/users/734a9e75-b3f5-415f-82fb-79b4fdf1a593)
* Cliquez sur "Envoyer". Si c'est réussi, vous verrez les informations de l'utilisateur de l'id utilisateur que vous avez utilisé pour la requête

![Image](https://lh7-us.googleusercontent.com/ui9cj6HDXIifMjzlnICvnzgIGOssvRbGeCrlos2DXG541b4r9Dsn0mVrXZBfyCwvO6gh3yovrbsDD1I7EU0-5j7r3fRIrQ4XFX1QR-vlFJlXuXb1Ht753re7ZDf2cC7VyPyLgee6a6gZmwjnkCb8RI0)
_test de la route GET postman_

### Comment créer le DELETE /users/:id

Parfois, il est nécessaire de supprimer des comptes utilisateurs ou des enregistrements spécifiques d'une base de données pour diverses raisons, telles que la désactivation de comptes. 

Ici, vous allez explorer comment utiliser ce point de terminaison pour supprimer les données d'un utilisateur en fonction d'un ID d'utilisateur fourni.

Pour supprimer des données, nous allons définir une route qui accepte les requêtes DELETE et supprime les données de la base de données.

Voir le code pour supprimer un utilisateur d'une base de données ci-dessous

```javascript
router.delete('/:id', (req, res) => {
  const { id } = req.params;

  users = users.filter((user) => user.id !== id)

  res.send(`${id} supprimé avec succès de la base de données`);
});
```

Voici ce que fait ce code :

* La fonction `router.delete()` configure une route qui répond aux requêtes HTTP DELETE. Dans cet exemple, nous avons défini une route avec ('/:id'), où :id est un paramètre de route. Il capture une valeur dynamique depuis l'URL, représentant l'ID de l'utilisateur que nous voulons supprimer.
* Dans la fonction de rappel `(req, res) => { ... }`, nous pouvons accéder à l'objet `req`, qui représente la requête entrante faite par le client. Plus précisément, nous nous intéressons à `req.params`, qui contient les valeurs des paramètres de route. Ici, nous déstructurons id depuis `req.params`, extrayant ainsi l'ID de l'utilisateur depuis l'URL. Par exemple, si un client envoie une requête DELETE à /users/123, id sera '123'.
* En supposant que nous avons un tableau ou une base de données (users) contenant les données des utilisateurs, nous employons la méthode `.filter()` pour créer un nouveau tableau qui exclut l'utilisateur avec l'ID correspondant (id). Cela supprime effectivement l'utilisateur de la base de données.
* Après avoir supprimé avec succès l'utilisateur, nous envoyons une réponse au client en utilisant `res.send()`. La réponse contient un message confirmant la suppression, y compris l'ID de l'utilisateur qui a été supprimé de la base de données.

#### **Comment tester la requête DELETE**

Voici les étapes pour supprimer un utilisateur de la base de données sur Postman :

* Allez sur Postman
* Ouvrez un nouvel onglet de requête
* Sélectionnez "DELETE" dans la liste des méthodes HTTP disponibles
* Entrez l'URL. Elle doit contenir l'id de l'utilisateur que vous souhaitez supprimer (par exemple : [http://localhost:5000/users/734a9e75-b3f5-415f-82fb-79b4fdf1a593](http://localhost:5000/users/734a9e75-b3f5-415f-82fb-79b4fdf1a593)). Si vous n'avez pas d'utilisateur dans votre base de données, vous devrez en créer un et copier l'id.
* Cliquez sur "Envoyer".  


![Image](https://lh7-us.googleusercontent.com/bTO6dcTaujyxm7ruPcyCJTzMfZemFop1oqU803Fif2kCeq1Z2q3uB1-JHB1aK4-ePIimPvb1LBYuty8_YFd7xP_i8UVhFZewWHlmwKy3MlWssMWtdaBnXtCkyB8NZebDnldJzRXc_v0Fs7MS4rZJq_g)
_test de la route DELETE postman_

![Image](https://lh7-us.googleusercontent.com/B9YHqAtEyg1f0O0CAojNJDXjK212LCxFodc9Ld3j04bdZsK9R5qHExSxaKGCAqgI0W79jHJ2bN3l9GkVgB3DYAd192zB9LzThvcAZJFuXoBO5JUqcUKWyBWcc6q4KirQA4B6Hi6t1NN3eU8e-dH10pY)
_test de la route DELETE postman_

### Comment créer le point de terminaison PATCH /users/:id

Il arrive que vous n'ayez pas besoin de mettre à jour une ressource ou un objet entier. Au lieu de cela, vous souhaiteriez apporter des modifications ou des ajustements partiels. C'est là que la requête HTTP PATCH entre en jeu.

Par exemple, après avoir créé un nouvel utilisateur, vous pouvez modifier soit le prénom, le nom ou l'email de cet utilisateur en utilisant la requête PATCH. Voyons comment faire cela.

```javascript
router.patch('/:id', (req, res) => {
  const { id } = req.params;

  const { first_name, last_name, email} = req.body;

  const user = users.find((user) => user.id === id)

  if(first_name) user.first_name = first_name;
  if(last_name) user.last_name = last_name;
  if(email) user.email = email;

  res.send(`L'utilisateur avec l'ID ${id} a été mis à jour`)
  
});
```

Voici ce que cet extrait de code accompli :

* La fonction `router.patch()` configure une route qui répond aux requêtes HTTP PATCH. Dans cet exemple, nous avons défini une route avec ('/:id'), où :id est un paramètre de route. Il capture la valeur dynamique depuis l'URL, représentant l'ID de l'utilisateur que nous voulons mettre à jour.
* Dans la fonction de rappel `(req, res) => { ... }`, nous pouvons accéder à l'objet `req`, qui représente la requête entrante faite par le client. Plus précisément, nous nous intéressons à `req.params`, qui contient les valeurs des paramètres de route (id dans ce cas), et `req.body`, qui contient les données à mettre à jour.
* Ensuite, nous avons utilisé `.find()` pour localiser l'objet utilisateur avec l'ID correspondant (id). Une fois trouvé, nous pouvons procéder à la modification des données de l'utilisateur en fonction du contenu de `req.body`. Nous avons également vérifié si les propriétés first_name, last_name ou email existent dans `req.body`. Si elles existent, nous pouvons mettre à jour les propriétés correspondantes de l'objet utilisateur avec les nouvelles valeurs. Cela nous permet d'apporter des modifications sélectives aux données de l'utilisateur sans affecter d'autres attributs.
* Après avoir appliqué avec succès les modifications demandées, nous envoyons une réponse au client en utilisant `res.send()`. La réponse inclut un message confirmant la mise à jour réussie des données de l'utilisateur, ainsi que l'ID de l'utilisateur.

#### **Comment tester la requête PATCH**

Suivez ces étapes pour faire une requête PATCH dans Postman :

* Allez sur Postman
* Ouvrez un nouvel onglet de requête
* Sélectionnez "PATCH" dans la liste des méthodes HTTP disponibles
* Entrez l'URL ; l'URL contiendra l'id de l'utilisateur que vous souhaitez supprimer (par exemple : [http://localhost:5000/users/734a9e75-b3f5-415f-82fb-79b4fdf1a593](http://localhost:5000/users/734a9e75-b3f5-415f-82fb-79b4fdf1a593)). Si vous n'avez pas d'utilisateur dans votre base de données, vous devrez en créer un et copier l'id.
* Cliquez sur l'onglet "Body" dans la fenêtre de requête et choisissez le format dans lequel vous souhaitez envoyer vos données PATCH (par exemple : JSON, form-data, x-www-form-urlencoded).
* Entrez les données que vous souhaitez envoyer dans le corps de la requête. Ces données doivent inclure uniquement les modifications spécifiques que vous souhaitez apporter à la ressource.
* Cliquez ensuite sur le bouton "Envoyer". Postman enverra la requête PATCH à l'URL spécifiée avec les données fournies.

![Image](https://lh7-us.googleusercontent.com/K1OH_u-2DOJbkMqlQ3uJow9XNKh0iOmE8fedCCspUiQIHcvm-DmIorFvZcApoDWGSK4YMkFR7RtcHBmzMZaJUyXy7SMDJWxH_PDLFmugGPNQDmKzM6HE3tPOBQZaS1388bZzLlmcTThQa_wy1ZPrm1g)
_test de la route PATCH postman_

## Conclusion

Les API sont le pivot reliant divers composants logiciels et leur permettant de fonctionner ensemble de manière transparente. Elles leur permettent de communiquer, de partager des données et d'effectuer des tâches. Dans le contexte du développement web, les API permettent au web de fonctionner comme nous le connaissons aujourd'hui.

Dans ce tutoriel, nous avons exploré le développement backend en créant une API CRUD avec Node.js et Express. Nous avons couvert divers concepts, comme la configuration d'un environnement de développement, la création d'un serveur avec Express et Node.js, et surtout, comment gérer les opérations CRUD et tester votre API en utilisant Postman.

Bien que nous ayons couvert les aspects fondamentaux de la création d'API dans ce tutoriel, il existe encore un vaste paysage de connaissances à explorer concernant les API. Cela inclut comment sécuriser votre API en ajoutant une authentification, comment utiliser des middlewares, l'interaction avec les bases de données, le déploiement d'API, et bien plus encore.