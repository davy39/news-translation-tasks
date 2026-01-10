---
title: Comment écrire un code plus propre avec les schémas Mongoose
subtitle: ''
author: ِAya Nabil Othman
co_authors: []
series: null
date: '2024-09-06T13:44:56.627Z'
originalURL: https://freecodecamp.org/news/how-to-write-cleaner-code-using-mongoose-schemas
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1725431278897/86823d79-7b9c-4512-a834-edcdd4e11ac3.jpeg
tags:
- name: mongoose
  slug: mongoose
- name: clean code
  slug: clean-code
- name: JavaScript
  slug: javascript
- name: MongoDB
  slug: mongodb
- name: Object Oriented Programming
  slug: object-oriented-programming
- name: dry
  slug: dry
- name: APIs
  slug: apis
seo_title: Comment écrire un code plus propre avec les schémas Mongoose
seo_desc: 'If you are used to building NodeJS applications using the Mongoose ORM,
  this article is for you. In it, we''ll discuss some cool features of Mongoose schemas
  that''ll help you write more organized and maintainable code.

  To get the most out of this guid...'
---

Si vous avez l'habitude de créer des applications NodeJS en utilisant l'ORM Mongoose, cet article est pour vous. Nous y aborderons certaines fonctionnalités intéressantes des schémas Mongoose qui vous aideront à écrire un code plus organisé et facile à maintenir.

Pour tirer le meilleur parti de ce guide, vous devriez avoir des bases en JavaScript, comprendre le fonctionnement de Mongoose et connaître les principes fondamentaux de la programmation orientée objet.

### Voici ce que nous allons couvrir :

1. [Qu'est-ce qu'un schéma Mongoose ?](#heading-quest-ce-quun-schema-mongoose)
    
2. [Discriminateur](#heading-discriminateur)
    
3. [Statiques](#heading-statiques)
    
4. [Méthodes](#heading-methodes)
    
5. [Query Builder](#heading-query-builder)
    
6. [Hooks](#heading-hooks)
    
7. [Résumé](#heading-resume)
    

## **Qu'est-ce qu'un schéma Mongoose ?**

Les schémas Mongoose offrent une manière structurée de modéliser les données dans une base de données MongoDB, vous permettant de définir les propriétés et le comportement des documents. Les schémas servent de plan (blueprint) pour un document qui est enregistré dans la base de données. Ils permettent aux développeurs d'appliquer l'intégrité des données et de travailler avec MongoDB de manière plus intuitive et organisée.

Au sein d'une collection MongoDB, un schéma définit les champs des documents, leurs types de données, les règles de validation, les valeurs par défaut, les contraintes, et bien plus encore.

De manière programmatique, un schéma Mongoose est un objet JavaScript. En réalité, il s'agit d'une instance d'une classe intégrée appelée `Schema` à l'intérieur du module `mongoose`. Pour cette raison, vous pouvez ajouter d'autres méthodes à son prototype. Cela vous aidera à implémenter de nombreuses fonctionnalités sous forme de middleware, méthodes, statiques, et plus encore. Vous en apprendrez davantage sur certaines d'entre elles dans ce tutoriel.

### **Fonctionnalités que vous apprendrez à implémenter :**

* [Discriminateur](#discriminateur)
    
* [Statiques](#statiques)
    
* [Méthodes](#methodes)
    
* [Query Builder](#query-builder)
    
* [Hooks](#hooks)
    

## Discriminateur

Un discriminateur est une fonctionnalité qui vous permet de créer plusieurs modèles (sous-types) qui héritent d'un modèle de base (parent). Cela se fait en définissant un schéma de base, puis en l'étendant avec des champs supplémentaires spécifiques à chaque sous-type ou chaque schéma enfant.

Tous les documents, quel que soit leur modèle spécifique, sont stockés dans la même collection MongoDB. Cela permet de garder vos données organisées dans une seule collection tout en permettant des requêtes et une gestion des données flexibles. De plus, chaque document comprend un champ spécial qui indique son type de modèle spécifique, permettant à Mongoose de distinguer les différents sous-types.

**Comment utiliser** `discriminator` **:**

1. Commencez par définir un schéma de base, qui contiendra les champs communs aux sous-types. Après cela, créez un modèle à partir de celui-ci.
    
    ```javascript
    import mongoose from 'mongoose';
    
    const baseSchema = new mongoose.Schema({
        name: { type: String, required: true },
    }, { discriminatorKey: 'kind' }); // par défaut '__t');
    
    const BaseModel = mongoose.model('Base', baseSchema);
    ```
    
2. Créez les sous-types qui étendent le schéma de base en définissant le `discriminator` pour chacun.
    
    ```javascript
    const catSchema = new mongoose.Schema({
        meow: { type: Boolean, default: true }
    });
    // sous-type
    const Cat = BaseModel.discriminator('Cat', catSchema);
    
    const dogSchema = new mongoose.Schema({
        bark: { type: Boolean, default: true }
    });
    // sous-type
    const Dog = BaseModel.discriminator('Dog', dogSchema);
    ```
    
3. Vous pouvez ensuite créer des documents de manière habituelle. Tous les documents seront stockés dans la même collection, mais chacun possède son propre type en fonction de son modèle de sous-type.
    
    ```javascript
    const fluffy = await Cat.create({ name: 'Fluffy' });
    const rover = await Dog.create({ name: 'Rover' });
    ```
    

### Cas d'utilisation de `discriminator` :

Supposons que vous construisiez une application web d'e-commerce multi-utilisateurs qui accueille trois rôles d'utilisateur principaux : *administrateurs*, *clients* et *vendeurs*. Chacun de ces rôles joue un rôle crucial dans l'écosystème des achats en ligne.

Si vous essayez de construire une classe pour chaque rôle, vous constaterez que les trois ont des champs et des méthodes communs. Vous pouvez décider de créer un schéma parent (user) et d'autres schémas enfants (client, seller, admin) qui en héritent.

Vous pouvez utiliser le `discriminator` pour y parvenir.

Dans votre fichier `user.model.js`, ajoutez le code suivant :

```javascript
import mongoose from "mongoose";

const userSchema = mongoose.Schema(
  {
    name: String,
    profilePic: String,
    email: String,
    password: String,
    birthDate: Date,
    accountAcctivated: { type: Boolean, default: false },
  },
  {
    timestamps: true,
    discriminatorKey: "role",
  }
);

const User = mongoose.model("User", userSchema);
export default User;
```

Vous avez maintenant le modèle de base (`User`) dont les autres sous-types hériteront. Dans ce schéma parent, vous définissez les champs communs que tous les utilisateurs partageront, quels que soient leurs rôles.

Dans votre fichier `client.model.js` :

```javascript
import mongoose from "mongoose";
import User from "./user.model.js";

const clientSchema = mongoose.Schema(
  {
    products: Array,
    address: String,
    phone: String,
  }
);

const Client = User.discriminator("Client", clientSchema);
export default Client;
```

Dans votre fichier `seller.model.js` :

```javascript
import mongoose from "mongoose";
import User from "./user.model.js";

export const sellerSchema = mongoose.Schema(
  {
    rating: Number,
    businessType: { type: String, enum: ["individual", "corporation"] },
  }
);

const Seller = User.discriminator("Seller", sellerSchema);
export default Seller;
```

Dans votre fichier `admin.model.js` :

```javascript
import mongoose from "mongoose";
import User from "./user.model.js";

export const adminSchema = mongoose.Schema(
  {
    permissions: Array,
    assignedTasks: Array,
    department: String,
  }
);

const Admin = User.discriminator("Admin", adminSchema);
export default Admin;
```

Les sous-types ou enfants seront `Client`, `Seller` et `Admin`. Dans chaque schéma de sous-type, vous devez ajouter tous les champs ou comportements supplémentaires spécifiques à ce sous-type uniquement. En créant le modèle enfant à l'aide du discriminateur, le modèle enfant héritera de tous les champs et méthodes de son modèle parent `User`.

Ainsi, le code précédent créera une collection `user` dans la base de données, chaque document ayant un champ `role` soit Client, Seller ou Admin. Tous les documents partagent désormais les champs parents (`user`), et selon le `role` de chaque document, chacun dispose d'un autre champ supplémentaire.

Bien que tous les documents soient enregistrés dans une seule collection, les modèles sont entièrement séparés lors du codage. Qu'est-ce que cela signifie ?

Par exemple, si vous avez besoin de récupérer tous les clients de la collection `User`, vous devez écrire `Client.find({})`. Cette instruction utilise la clé de discriminateur pour trouver tous les documents dont le `role` est `Client`. De cette façon, toutes les opérations ou requêtes qui font référence à l'un des modèles enfants seront toujours écrites séparément du modèle parent.

**Remarque :** Avant de passer aux sections suivantes, gardez à l'esprit que les statiques, méthodes, query builders ou hooks doivent être définis avant de créer le modèle lui-même (c'est-à-dire avant `const User = mongoose.model("User", userSchema);`).

## Statiques

Les statiques sont utiles pour définir des fonctions qui opèrent au niveau du modèle. Elles vous permettent de définir des fonctions réutilisables pour des opérations liées à l'ensemble du modèle. Elles aident à encapsuler la logique qui s'applique au modèle plutôt qu'à des documents individuels, rendant votre code plus propre, mieux organisé et facile à maintenir.

Des méthodes comme `find`, `findOne`, `findById` et d'autres sont toutes des méthodes attachées au modèle. En utilisant la propriété `statics` des schémas Mongoose, vous pourrez construire votre propre méthode de modèle.

Les statiques sont puissantes. En les utilisant, vous pouvez encapsuler des requêtes complexes que vous pourriez vouloir réutiliser. De plus, vous pouvez créer des statiques pour des opérations qui modifient ou agrègent des données, comme le comptage de documents ou la recherche de documents basés sur des critères spécifiques.

### Cas d'utilisation de `statics`

Les statiques sont faciles à construire. Vous définissez une méthode statique sur votre schéma en utilisant l'objet `statics`.

Dans votre fichier `user.model.js`, ajoutez ces méthodes statiques, `countUsers` et `findByEmail` :

```javascript
// méthode de modèle
userSchema.statics.countUsers = function () {
    return this.countDocuments({});
};

// méthode de modèle
userSchema.statics.findByEmail = async function (email) {
  return await this.findOne({ email });
};
```

À l'intérieur de toute méthode statique, `this` fait référence au **modèle** lui-même. Dans cet exemple, `this` dans `this.findOne({ email })` fait référence au modèle `User`.

Exemple d'utilisation :

```javascript
const user = await User.findByEmail("foo@bar.com");
// ou
const client = await Client.findByEmail("foo@bar.com");
// ou
const seller = await Seller.findByEmail("foo@bar.com");
// ou
const admin = await Admin.findByEmail("foo@bar.com");
```

Lorsque vous appelez la méthode statique sur votre modèle, la méthode est appelée et `this` est remplacé par le modèle sur lequel vous avez appelé la statique. Cette ligne effectue une requête pour trouver un seul document dans la collection MongoDB où le champ `email` correspond à l'argument `email` fourni.

## Méthodes

Les méthodes sont des fonctions que vous pouvez définir sur un schéma et qui peuvent être appelées sur des instances de documents créées à partir de ce schéma. Elles aident à encapsuler la logique au sein du document lui-même, rendant votre code plus propre et plus modulaire.

En utilisant des méthodes d'instance, vous pouvez facilement interagir avec et manipuler les données associées à des documents spécifiques.

### Cas d'utilisation de `methods`

Vous pouvez définir des méthodes sur le schéma en utilisant l'objet `methods`.

Dans votre fichier `user.model.js`, ajoutez une méthode de document grâce à laquelle vous pouvez vérifier le mot de passe d'un utilisateur :

```javascript
// méthode d'instance ou de document
userSchema.methods.getProfile = function () {
    return `${this.name} (${this.email})`;
};

// méthode d'instance ou de document
userSchema.methods.checkPassword = function (password) {
    return password === this.password ? true : false;
};
```

À l'intérieur de toute méthode de document, `this` fait référence au **document** lui-même. Dans cet exemple, `this` dans `this.password` fait référence au document `user` sur lequel la méthode sera appelée. Cela signifie que vous pouvez accéder à tous les champs de ce document. C'est très précieux car vous pouvez récupérer, modifier et vérifier tout ce qui concerne ce document.

Exemple d'utilisation :

```javascript
const client = await Client.findById(...)
client.checkPassword("12345")
// ou
const seller = await Seller.findById(...)
seller.checkPassword("12345")
// ou
const admin = await Admin.findById(...)
admin.checkPassword("12345")
```

Puisque les méthodes sont des fonctions de niveau instance, elles sont appelées sur les documents. `await Client.findById(...)` retournera un document qui possède toutes les méthodes intégrées ainsi que vos propres méthodes prédéfinies `checkPassword` et `getProfile`. Ainsi, en appelant, par exemple `client.checkPassword("12345")`, le mot-clé `this` dans la définition de la fonction `checkPassword` sera remplacé par le document `client`. Cela comparera à son tour le mot de passe de l'utilisateur avec le mot de passe enregistré précédemment dans la base de données.

## Query Builder

Un Query Builder dans Mongoose est une méthode personnalisée que vous pouvez définir sur l'objet de requête pour simplifier et encapsuler des modèles de requête courants. Ces Query Builders vous permettent de créer une logique de requête réutilisable et lisible, facilitant ainsi le travail avec vos données.

L'une des utilisations les plus précieuses des Query Builders est le chaînage. Ils peuvent être chaînés avec d'autres Query Builders que vous avez créés ou avec des méthodes de requête standard comme find, sort, etc.

### Cas d'utilisation du Query Builder

Vous définissez des Query Builders en les ajoutant à la propriété `query` d'un schéma Mongoose.

Dans votre fichier `user.model.js`, ajoutez une méthode d'aide à la requête qui vous permet d'implémenter la pagination.

```javascript
// helper de requête
userSchema.query.paginate = function ({ page, limit }) {
    // du code ici
    const skip = limit * (page - 1);
    return this.skip(skip).limit(limit);
};
```

Pour implémenter la pagination, vous avez besoin de deux variables importantes : d'abord, le numéro de page, et ensuite, le nombre d'éléments que vous récupérerez par page.

Pour interroger la base de données pour un nombre spécifique de documents, vous utiliserez toujours les méthodes de requête intégrées `skip` et `limit` dans `mongoose`. `skip` est utilisé pour placer un curseur après un certain nombre de documents, après quoi la requête sera exécutée. `limit` est utilisé pour récupérer un nombre spécifique de documents.

À l'intérieur de toute méthode de Query Builder, `this` fait référence à la **requête** elle-même. Et puisque les Query Builders sont chaînables, vous pouvez les appeler les uns après les autres.

Enfin, toute méthode de Query Builder doit retourner un `objet de requête mongoose`, c'est pourquoi vous devez écrire `return this.skip(skip).limit(limit)`.

Exemple d'utilisation :

```javascript
const results = await Client.find().paginate({ page: 2, limit: 5 });
// ou
const results = await Seller.find().paginate({ page: 2, limit: 5 });
// ou
const results = await Admin.find().paginate({ page: 2, limit: 5 });
```

Vous pouvez ensuite l'appeler sur n'importe quelle requête, et `await Client.find().paginate({ page: 2, limit: 5 })` invoquera la fonction `paginate` et remplacera le mot-clé `this` par `Client.find()` en utilisant le Query Builder.

Vous pouvez implémenter la pagination avec certaines conditions, mais vous appellerez toujours `skip` et `limit`. En définissant le Query Builder `paginate`, vous ne vous répéterez pas et vous pourrez encapsuler la logique dans une seule fonction.

## Hooks

Les hooks (également connus sous le nom de middleware) sont des fonctions qui sont exécutées à des points spécifiques du cycle de vie d'un document. Ils vous permettent d'ajouter un comportement personnalisé avant ou après certaines opérations, telles que l'enregistrement, la mise à jour ou la suppression de documents.

Types de Hooks

* Hooks Pre : Exécutés avant une opération.
    
* Hooks Post : Exécutés après une opération.
    

### Cas d'utilisation des Hooks

Dans votre fichier `user.model.js`, ajoutez un middleware `post` save grâce auquel vous pouvez envoyer un e-mail pour l'activation du compte une fois que le document utilisateur est enregistré dans la base de données.

```javascript
// hook post
userSchema.post("save", async function (doc, next) {
  // logique d'envoi d'e-mail
  // si réussi
  return next();
  // si échoué
  return next(new Error("Échec de l'envoi de l'e-mail !"));
});
```

La fonction de rappel sera invoquée une fois que vous aurez créé un utilisateur via `model.create()` ou chaque fois que vous appellerez la méthode `save()` sur le document utilisateur.

Dans cet exemple, si vous devez éviter d'envoyer des e-mails lors de la sauvegarde, vous devriez écrire une condition pour être sûr que ce `save` concerne uniquement un nouvel utilisateur. Vous pouvez écrire quelque chose comme `if (doc.createdAt.getTime() === doc.updatedAt.getTime())`.

### **Résumé**

Dans cet aperçu des fonctionnalités de Mongoose, nous avons exploré quatre concepts clés : les discriminateurs, les statiques, les méthodes et les hooks.

Les **discriminateurs** vous permettent de créer plusieurs modèles qui partagent un schéma commun, permettant de stocker différents types de documents dans une seule collection. Cela facilite la gestion des données et les requêtes.

Les **statiques** sont des méthodes au niveau du modèle qui fournissent des fonctionnalités réutilisables applicables à l'ensemble du modèle. Elles encapsulent des requêtes complexes et une logique de manipulation de données, aidant à maintenir votre base de code propre et facile à entretenir.

Les **méthodes** sont des fonctions au niveau de l'instance qui opèrent sur des instances de documents individuelles. Elles permettent des comportements personnalisés et des manipulations de données spécifiques à chaque document, vous permettant de modifier les données du document d'une manière spécifique, comme le formatage ou le calcul de valeurs basées sur ses champs.

Les **hooks** (ou middleware) vous permettent d'exécuter des fonctions à des points spécifiques du cycle de vie du document, comme avant ou après la sauvegarde, la mise à jour ou la suppression d'un document. C'est utile pour implémenter la validation, la journalisation ou tout autre effet secondaire lié aux opérations de base de données.

Ensemble, ces fonctionnalités améliorent la polyvalence et l'organisation de vos modèles Mongoose, facilitant la création d'applications robustes et maintenables avec MongoDB.

[Ici](https://github.com/Ayanabilothman/mongoose-schema-features), vous trouverez un dépôt où vous pourrez en apprendre davantage sur les schémas Mongoose et les cas d'utilisation.