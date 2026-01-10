---
title: Introduction à Mongoose pour MongoDB
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-11T20:00:49.000Z'
originalURL: https://freecodecamp.org/news/introduction-to-mongoose-for-mongodb-d2a7aa593c57
coverImage: https://cdn-media-1.freecodecamp.org/images/1*uTZXsVta4TwghNobMkZeZg.png
tags:
- name: MongoDB
  slug: mongodb
- name: mongoose
  slug: mongoose
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Introduction à Mongoose pour MongoDB
seo_desc: 'By Nick Karnik

  Mongoose is an Object Data Modeling (ODM) library for MongoDB and Node.js. It manages
  relationships between data, provides schema validation, and is used to translate
  between objects in code and the representation of those objects in M...'
---

Par Nick Karnik

Mongoose est une bibliothèque de modélisation de données objet (ODM) pour MongoDB et Node.js. Elle gère les relations entre les données, fournit une validation de schéma et est utilisée pour traduire entre les objets dans le code et la représentation de ces objets dans MongoDB.

![Image](https://cdn-media-1.freecodecamp.org/images/0*b5piDNW1dqlkJWKe.)
_Mappage d'objets entre Node et MongoDB géré via Mongoose_

MongoDB est une base de données de documents NoSQL sans schéma. Cela signifie que vous pouvez stocker des documents JSON dans celle-ci, et la structure de ces documents peut varier car elle n'est pas imposée comme dans les bases de données SQL. C'est l'un des avantages de l'utilisation de NoSQL car cela accélère le développement d'applications et réduit la complexité des déploiements.

Voici un exemple de la manière dont les données sont stockées dans Mongo vs. une base de données SQL :

![Image](https://cdn-media-1.freecodecamp.org/images/0*rcotALFe2LeebN_y.)

![Image](https://cdn-media-1.freecodecamp.org/images/0*QOKLctlRwxs5uKVo.)
_Documents NoSQL vs. Tables relationnelles en SQL_

### Terminologies

#### Collections

Les [_Collections_](https://mongoosejs.com/docs/guide.html#collection) dans Mongo sont équivalentes aux tables dans les bases de données relationnelles. Elles peuvent contenir plusieurs documents JSON.

#### Documents

Les [_Documents_](https://mongoosejs.com/docs/documents.html) sont équivalents aux enregistrements ou aux lignes de données en SQL. Alors qu'une ligne SQL peut référencer des données dans d'autres tables, les documents Mongo combinent généralement cela dans un document.

#### Champs

Les _Champs_, également connus sous le nom de propriétés ou d'attributs, sont similaires aux colonnes dans une table SQL. Dans l'image ci-dessus, `FirstName`, `LastName`, `Email` et `Phone` sont tous des champs.

#### Schéma

Bien que Mongo soit sans schéma, SQL définit un schéma via la définition de la table. Un schéma [_schema_](https://mongoosejs.com/docs/guide.html#schemas) Mongoose est une structure de données de document (ou forme du document) qui est imposée via la couche application.

#### SchemaTypes

Alors que les schémas Mongoose définissent la structure globale ou la forme d'un document, les [_SchemaTypes_](https://mongoosejs.com/docs/schematypes.html) définissent le type de données attendu pour les champs individuels (`String`, `Number`, `Boolean`, etc.).

Vous pouvez également passer des options utiles comme `required` pour rendre un champ non optionnel, `default` pour définir une valeur par défaut pour le champ, et bien plus encore.

#### Modèles

Les [_Modèles_](https://mongoosejs.com/docs/models.html) sont des constructeurs de niveau supérieur qui prennent un schéma et créent une instance d'un document équivalent aux enregistrements dans une base de données relationnelle.

#### Exemple

Voici un petit extrait de code pour illustrer certaines des terminologies ci-dessus :

```js
const puppySchema = new mongoose.Schema({
  name: {
    type: String,
    required: true
  },
  age: Number
});

const Puppy = mongoose.model('Puppy', puppySchema);

```

Dans le code ci-dessus, `puppySchema` définit la forme du document qui a deux champs, `name` et `age`.

Le `SchemaType` pour `name` est `String` et pour `age` est `Number`. Notez que vous pouvez définir le `SchemaType` pour un champ en utilisant un objet avec une propriété `type` comme avec `name`. Ou vous pouvez appliquer un `SchemaType` directement au champ comme avec `age`.

De plus, remarquez que le `SchemaType` pour `name` a l'option `required` définie sur `true`. Pour utiliser des options comme `required` et `lowercase` pour un champ, vous devez utiliser un objet pour définir le `SchemaType`.

En bas de l'extrait, `puppySchema` est compilé en un modèle nommé `Puppy`, qui peut ensuite être utilisé pour construire des documents dans une application.

### Getting Started

#### Installation de Mongo

Avant de commencer, installons Mongo. Vous pouvez choisir l'une des options suivantes (nous utilisons l'option #1 pour cet article) :

1. Téléchargez la version appropriée de MongoDB pour votre système d'exploitation depuis le [site web de MongoDB](https://www.mongodb.com/download-center#community) et suivez leurs instructions d'installation
2. [Créez un abonnement gratuit à une base de données sandbox](http://docs.mlab.com/) sur mLab
3. [Installez Mongo en utilisant Docker](https://docs.docker.com/samples/library/mongo/) si vous préférez utiliser Docker

Naviguons à travers quelques bases de Mongoose en implémentant un modèle qui représente des données pour un carnet d'adresses simplifié.

J'utilise Visual Studio Code, Node 8.9 et NPM 5.6. Lancez votre IDE préféré, créez un projet vide et commençons ! Nous utiliserons la syntaxe ES6 limitée dans Node, donc nous ne configurerons pas Babel.

#### Installation de NPM

Allons dans le dossier du projet et initialisons notre projet

```bash
npm init -y
```

Installons Mongoose et une bibliothèque de validation avec la commande suivante :

```bash
npm install mongoose validator
```

La commande d'installation ci-dessus installera la dernière version des bibliothèques. La syntaxe Mongoose dans cet article est spécifique à Mongoose v5 et au-delà.

#### Connexion à la base de données

Créez un fichier `./src/database.js` à la racine du projet.

Ensuite, nous ajouterons une classe simple avec une méthode qui se connecte à la base de données.

Votre chaîne de connexion variera en fonction de votre installation.

```js
let mongoose = require('mongoose');

const server = '127.0.0.1:27017'; // REMPLACER PAR VOTRE SERVEUR DE BASE DE DONNÉES
const database = 'fcc-Mail'; // REMPLACER PAR LE NOM DE VOTRE BASE DE DONNÉES

class Database {
  constructor() {
    this._connect();
  }

  _connect() {
    mongoose
      .connect(`mongodb://${server}/${database}`)
      .then(() => {
        console.log('Connexion à la base de données réussie');
      })
      .catch((err) => {
        console.error('Erreur de connexion à la base de données');
      });
  }
}

module.exports = new Database();

```

L'appel `require('mongoose')` ci-dessus retourne un objet Singleton. Cela signifie que la première fois que vous appelez `require('mongoose')`, il crée une instance de la classe Mongoose et la retourne. Lors des appels suivants, il retournera la même instance qui a été créée et retournée la première fois en raison du fonctionnement de l'import/export de modules en ES6.

![Image](https://cdn-media-1.freecodecamp.org/images/0*RvVsD_byUakUzuCj.)
_Flux de travail d'import/require de module_

De même, nous avons transformé notre classe `Database` en un singleton en retournant une instance de la classe dans l'instruction `module.exports` car nous avons besoin d'une seule connexion à la base de données.

ES6 rend très facile la création d'un modèle singleton (instance unique) en raison du fonctionnement du chargeur de modules qui met en cache la réponse d'un fichier précédemment importé.

### Schéma Mongoose vs. Modèle

Un modèle Mongoose est un wrapper sur le schéma Mongoose. Un schéma Mongoose définit la structure du document, les valeurs par défaut, les validateurs, etc., tandis qu'un modèle Mongoose fournit une interface vers la base de données pour créer, interroger, mettre à jour, supprimer des enregistrements, etc.

La création d'un modèle Mongoose comprend principalement trois parties :

#### **1. Référencement de Mongoose**

```js
let mongoose = require('mongoose');
```

Cette référence sera la même que celle retournée lors de la connexion à la base de données, ce qui signifie que les définitions de schéma et de modèle n'auront pas besoin de se connecter explicitement à la base de données.

#### 2. Définition du Schéma

Un schéma définit les propriétés du document via un objet où le nom de la clé correspond au nom de la propriété dans la collection.

```js
let emailSchema = new mongoose.Schema({
  email: String
});

```

Ici, nous définissons une propriété appelée `email` avec un type de schéma `String` qui mappe à un validateur interne qui sera déclenché lorsque le modèle sera enregistré dans la base de données. Il échouera si le type de données de la valeur n'est pas de type chaîne.

Les types de schéma suivants sont autorisés :

* Array
* Boolean
* Buffer
* Date
* Mixed (Un type de données générique / flexible)
* Number
* ObjectId
* String

Mixed et ObjectId sont définis sous `require('mongoose').Schema.Types`.

#### **3. Exportation d'un Modèle**

Nous devons appeler le constructeur de modèle sur l'instance Mongoose et lui passer le nom de la collection et une référence à la définition du schéma.

```js
module.exports = mongoose.model('Email', emailSchema);
```

Combinons le code ci-dessus dans `./src/models/email.js` pour définir le contenu d'un modèle d'email de base :

```js
let mongoose = require('mongoose');

let emailSchema = new mongoose.Schema({
  email: String
});

module.exports = mongoose.model('Email', emailSchema);

```

Une définition de schéma doit être simple, mais sa complexité est généralement basée sur les exigences de l'application. Les schémas peuvent être réutilisés et ils peuvent contenir plusieurs sous-schémas. Dans l'exemple ci-dessus, la valeur de la propriété email est un type de valeur simple. Cependant, elle peut également être un type d'objet avec des propriétés supplémentaires.

Nous pouvons créer une instance du modèle que nous avons défini ci-dessus et le remplir en utilisant la syntaxe suivante :

```js
let EmailModel = require('./email');

let msg = new EmailModel({
  email: 'ada.lovelace@gmail.com'
});

```

Améliorons le schéma `Email` pour rendre la propriété email unique, obligatoire et convertir la valeur en minuscules avant de l'enregistrer. Nous pouvons également ajouter une fonction de validation qui garantira que la valeur est une adresse email valide. Nous allons référencer et utiliser la bibliothèque de validation installée précédemment.

```js
let mongoose = require('mongoose');
let validator = require('validator');

let emailSchema = new mongoose.Schema({
  email: {
    type: String,
    required: true,
    unique: true,
    lowercase: true,
    validate: (value) => {
      return validator.isEmail(value);
    }
  }
});

module.exports = mongoose.model('Email', emailSchema);

```

### Opérations de base

Mongoose dispose d'une API flexible et offre de nombreuses façons d'accomplir une tâche. Nous ne nous concentrerons pas sur les variations car cela est hors de portée pour cet article, mais rappelez-vous que la plupart des opérations peuvent être effectuées de plus d'une manière, soit syntaxiquement, soit via l'architecture de l'application.

#### Créer un enregistrement

Créons une instance du modèle d'email et enregistrons-la dans la base de données :

```js
let EmailModel = require('./email');

let msg = new EmailModel({
  email: 'ADA.LOVELACE@GMAIL.COM'
});

msg
  .save()
  .then((doc) => {
    console.log(doc);
  })
  .catch((err) => {
    console.error(err);
  });

```

Le résultat est un document qui est retourné après un enregistrement réussi :

```json
{ 
  _id: 5a78fe3e2f44ba8f85a2409a,
  email: 'ada.lovelace@gmail.com',
  __v: 0 
}
```

Les champs suivants sont retournés (les champs internes sont préfixés par un underscore) :

1. Le champ `_id` est auto-généré par Mongo et est une clé primaire de la collection. Sa valeur est un identifiant unique pour le document.
2. La valeur du champ `email` est retournée. Remarquez qu'elle est en minuscules car nous avons spécifié l'attribut `lowercase: true` dans le schéma.
3. `__v` est la propriété versionKey définie sur chaque document lors de sa création par Mongoose. Sa valeur contient la révision interne du document.

Si vous essayez de répéter l'opération d'enregistrement ci-dessus, vous obtiendrez une erreur car nous avons spécifié que le champ email doit être unique.

#### Récupérer un enregistrement

Essayons de récupérer l'enregistrement que nous avons enregistré dans la base de données précédemment. La classe de modèle expose plusieurs méthodes statiques et d'instance pour effectuer des opérations sur la base de données. Nous allons maintenant essayer de trouver l'enregistrement que nous avons créé précédemment en utilisant la méthode find et en passant l'email comme terme de recherche.

```
EmailModel.find({
  email: 'ada.lovelace@gmail.com' // requête de recherche
})
  .then((doc) => {
    console.log(doc);
  })
  .catch((err) => {
    console.error(err);
  });

```

Le document retourné sera similaire à ce qui a été affiché lorsque nous avons créé l'enregistrement :

```json
{ 
  _id: 5a78fe3e2f44ba8f85a2409a,
  email: 'ada.lovelace@gmail.com',
  __v: 0 
}
```

#### Mettre à jour un enregistrement

Modifions l'enregistrement ci-dessus en changeant l'adresse email et en ajoutant un autre champ, le tout en une seule opération. Pour des raisons de performance, Mongoose ne retournera pas le document mis à jour, donc nous devons passer un paramètre supplémentaire pour le demander :

```js
EmailModel.findOneAndUpdate(
  {
    email: 'ada.lovelace@gmail.com' // requête de recherche
  },
  {
    email: 'theoutlander@live.com' // champ:valeurs à mettre à jour
  },
  {
    new: true, // retourner le document mis à jour
    runValidators: true // valider avant la mise à jour
  }
)
  .then((doc) => {
    console.log(doc);
  })
  .catch((err) => {
    console.error(err);
  });

```

Le document retourné contiendra l'email mis à jour :

```json
{ 
  _id: 5a78fe3e2f44ba8f85a2409a,
  email: 'theoutlander@live.com',
  __v: 0 
}
```

#### Supprimer un enregistrement

Nous utiliserons l'appel `findOneAndRemove` pour supprimer un enregistrement. Il retourne le document original qui a été supprimé :

```js
EmailModel.findOneAndRemove({
  email: 'theoutlander@live.com'
})
  .then((response) => {
    console.log(response);
  })
  .catch((err) => {
    console.error(err);
  });

```

### Aides

Nous avons examiné certaines des fonctionnalités de base ci-dessus connues sous le nom d'opérations CRUD (Create, Read, Update, Delete), mais Mongoose offre également la possibilité de configurer plusieurs types de méthodes et propriétés d'aide. Celles-ci peuvent être utilisées pour simplifier davantage le travail avec les données.

Créons un schéma d'utilisateur dans `./src/models/user.js` avec les champs `firstName` et `lastName` :

```js
let mongoose = require('mongoose');

let userSchema = new mongoose.Schema({
  firstName: String,
  lastName: String
});

module.exports = mongoose.model('User', userSchema);

```

#### Propriété virtuelle

Une propriété virtuelle n'est pas persistée dans la base de données. Nous pouvons l'ajouter à notre schéma en tant qu'aide pour obtenir et définir des valeurs.

Créons une propriété virtuelle appelée `fullName` qui peut être utilisée pour définir des valeurs sur `firstName` et `lastName` et les récupérer en tant que valeur combinée lors de la lecture :

```js
userSchema.virtual('fullName').get(function () {
  return this.firstName + ' ' + this.lastName;
});

userSchema.virtual('fullName').set(function (name) {
  let str = name.split(' ');

  this.firstName = str[0];
  this.lastName = str[1];
});

```

Les rappels pour get et set doivent utiliser le mot-clé function car nous devons accéder au modèle via le mot-clé `this`. L'utilisation de fonctions fléchées changera ce à quoi `this` fait référence.

Maintenant, nous pouvons définir `firstName` et `lastName` en attribuant une valeur à `fullName` :

```js
let model = new UserModel();

model.fullName = 'Thomas Anderson';

console.log(model.toJSON()); // Sortie des champs du modèle en JSON
console.log();
console.log(model.fullName); // Sortie du nom complet

```

Le code ci-dessus produira la sortie suivante :

```bash
{ _id: 5a7a4248550ebb9fafd898cf,
  firstName: 'Thomas',
  lastName: 'Anderson' }
  
Thomas Anderson
```

#### Méthodes d'instance

Nous pouvons créer des méthodes d'aide personnalisées sur le schéma et y accéder via l'instance du modèle. Ces méthodes auront accès à l'objet modèle et elles peuvent être utilisées de manière assez créative. Par exemple, nous pourrions créer une méthode pour trouver toutes les personnes qui ont le même prénom que l'instance actuelle.

Dans cet exemple, créons une fonction pour retourner les initiales de l'utilisateur actuel. Ajoutons une méthode d'aide personnalisée appelée `getInitials` au schéma :

```js
userSchema.methods.getInitials = function () {
  return this.firstName[0] + this.lastName[0];
};

```

Cette méthode sera accessible via une instance de modèle :

```js
let model = new UserModel({
  firstName: 'Thomas',
  lastName: 'Anderson'
});

let initials = model.getInitials();

console.log(initials); // Cela affichera : TA

```

#### Méthodes statiques

Similaires aux méthodes d'instance, nous pouvons créer des méthodes statiques sur le schéma. Créons une méthode pour récupérer tous les utilisateurs dans la base de données :

```js
userSchema.statics.getUsers = function () {
  return new Promise((resolve, reject) => {
    this.find((err, docs) => {
      if (err) {
        console.error(err);
        return reject(err);
      }

      resolve(docs);
    });
  });
};

```

L'appel de `getUsers` sur la classe Model retournera tous les utilisateurs dans la base de données :

```js
UserModel.getUsers()
  .then((docs) => {
    console.log(docs);
  })
  .catch((err) => {
    console.error(err);
  });

```

L'ajout de méthodes d'instance et statiques est une bonne approche pour implémenter une interface pour les interactions avec la base de données sur les collections et les enregistrements.

#### **Middleware**

Les middlewares sont des fonctions qui s'exécutent à des étapes spécifiques d'un pipeline. Mongoose supporte les middlewares pour les opérations suivantes :

* Aggregate
* Document
* Model
* Query

Par exemple, les modèles ont des fonctions `pre` et `post` qui prennent deux paramètres :

1. Type d'événement ('init', 'validate', 'save', 'remove')
2. Un rappel qui est exécuté avec **this** référençant l'instance du modèle

![Image](https://cdn-media-1.freecodecamp.org/images/0*iZwmyy25FSxuxXlH.)
_Exemple de Middleware (a.k.a. pre et post hooks)_

Essayons un exemple en ajoutant deux champs appelés `createdAt` et `updatedAt` à notre schéma :

```js
let mongoose = require('mongoose');

let userSchema = new mongoose.Schema({
  firstName: String,
  lastName: String,
  createdAt: Date,
  updatedAt: Date
});

module.exports = mongoose.model('User', userSchema);

```

Lorsque `model.save()` est appelé, il y a un événement `pre('save', ...)` et `post('save', ...)` qui est déclenché. Pour le deuxième paramètre, vous pouvez passer une fonction qui est appelée lorsque l'événement est déclenché. Ces fonctions prennent un paramètre pour la fonction suivante dans la chaîne de middleware.

Ajoutons un hook pre-save et définissons des valeurs pour `createdAt` et `updatedAt` :

```js
userSchema.pre('save', function (next) {
  let now = Date.now();

  this.updatedAt = now;
  // Définir une valeur pour createdAt uniquement si elle est nulle
  if (!this.createdAt) {
    this.createdAt = now;
  }

  // Appeler la fonction suivante dans la chaîne pre-save
  next();
});

```

Créons et enregistrons notre modèle :

```js
let UserModel = require('./user');

let model = new UserModel({
  fullName: 'Thomas Anderson'
});

msg
  .save()
  .then((doc) => {
    console.log(doc);
  })
  .catch((err) => {
    console.error(err);
  });

```

Vous devriez voir des valeurs pour `createdAt` et `updatedAt` lorsque l'enregistrement créé est imprimé :

```json
{ _id: 5a7bbbeebc3b49cb919da675,
  firstName: 'Thomas',
  lastName: 'Anderson',
  updatedAt: 2018-02-08T02:54:38.888Z,
  createdAt: 2018-02-08T02:54:38.888Z,
  __v: 0 }
```

#### Plugins

Supposons que nous voulons suivre quand un enregistrement a été créé et mis à jour pour la dernière fois sur chaque collection dans notre base de données. Au lieu de répéter le processus ci-dessus, nous pouvons créer un plugin et l'appliquer à chaque schéma.

Créons un fichier `./src/model/plugins/timestamp.js` et répliquons la fonctionnalité ci-dessus en tant que module réutilisable :

```js
module.exports = function timestamp(schema) {
  // Ajouter les deux champs au schéma
  schema.add({
    createdAt: Date,
    updatedAt: Date
  });

  // Créer un hook pre-save
  schema.pre('save', function (next) {
    let now = Date.now();

    this.updatedAt = now;
    // Définir une valeur pour createdAt uniquement si elle est nulle
    if (!this.createdAt) {
      this.createdAt = now;
    }
    // Appeler la fonction suivante dans la chaîne pre-save
    next();
  });
};

```

Pour utiliser ce plugin, nous le passons simplement aux schémas qui doivent recevoir cette fonctionnalité :

```js
let timestampPlugin = require('./plugins/timestamp');

emailSchema.plugin(timestampPlugin);
userSchema.plugin(timestampPlugin);

```

### Construction de requêtes

Mongoose dispose d'une API très riche qui gère de nombreuses opérations complexes supportées par MongoDB. Considérons une requête où nous pouvons construire progressivement des composants de requête.

Dans cet exemple, nous allons :

1. Trouver tous les utilisateurs
2. Sauter les 100 premiers enregistrements
3. Limiter les résultats à 10 enregistrements
4. Trier les résultats par le champ firstName
5. Sélectionner le firstName
6. Exécuter cette requête

```js
UserModel.find()               // trouver tous les utilisateurs
  .skip(100)                   // sauter les 100 premiers éléments
  .limit(10)                   // limiter à 10 éléments
  .sort({ firstName: 1 })      // trier par firstName ascendant
  .select({ firstName: true }) // sélectionner uniquement firstName
  .exec()                      // exécuter la requête
  .then((docs) => {
    console.log(docs);
  })
  .catch((err) => {
    console.error(err);
  });

```

### Conclusion

Nous avons à peine effleuré la surface en explorant certaines des capacités de Mongoose. C'est une bibliothèque riche, pleine de fonctionnalités utiles et puissantes qui la rendent agréable à utiliser avec les modèles de données dans la couche application.

Bien que vous puissiez interagir directement avec Mongo en utilisant le pilote Mongo, Mongoose simplifiera cette interaction en vous permettant de modéliser les relations entre les données et de les valider facilement.

**Fait amusant :** [**Mongoose**](http://mongoosejs.com) a été créé par [**Valeri Karpov**](https://www.freecodecamp.org/news/introduction-to-mongoose-for-mongodb-d2a7aa593c57/undefined) qui est un ingénieur incroyablement talentueux ! Il a inventé le terme [**The MEAN Stack**](http://thecodebarbarian.com/2013/04/29//easy-web-prototyping-with-mongodb-and-nodejs).

#### Si cet article vous a été utile, [suivez-moi sur Twitter](https://twitter.com/intent/follow?screen_name=theoutlander).

![Image](https://cdn-media-1.freecodecamp.org/images/1*278_8HmTEdaRAqFYUemQvQ.png)
_[Comment construire une API REST avec Node | Express | Mongo](https://twitter.com/intent/follow?screen_name=theoutlander" rel="noopener" target="_blank" title="">Vous aimerez peut-être aussi mon atelier sur youtube : </a><a href="https://youtu.be/egeHq-lYyxo" rel="noopener" target="_blank" title=")_