---
title: 'Mongoose 101 : Une introduction aux bases, sous-documents et population'
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2020-01-22T14:00:00.000Z'
originalURL: https://freecodecamp.org/news/mongoose101
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d9f740569d1a4ca38bb.jpg
tags:
- name: mongoose
  slug: mongoose
seo_title: 'Mongoose 101 : Une introduction aux bases, sous-documents et population'
seo_desc: "Mongoose is a library that makes MongoDB easier to use. It does two things:\n\
  \nIt gives structure to MongoDB Collections\nIt gives you helpful methods to use\n\
  \nIn this article, we'll go through: \n\nThe basics of using Mongoose \nMongoose\
  \ subdocuments\nMongo..."
---

Mongoose est une bibliothèque qui facilite l'utilisation de MongoDB. Elle fait deux choses :

1. Elle donne une structure aux collections MongoDB
2. Elle vous fournit des méthodes utiles à utiliser

Dans cet article, nous allons passer en revue :

1. Les bases de l'utilisation de Mongoose
2. Les sous-documents Mongoose
3. La population Mongoose

À la fin de l'article, vous devriez être capable d'utiliser Mongoose sans problème. 

## Prérequis

Je suppose que vous avez fait ce qui suit :

1. Vous avez installé MongoDB sur votre ordinateur
2. Vous savez comment établir une connexion locale à MongoDB
3. Vous savez comment voir les données que vous avez dans votre base de données
4. Vous savez ce que sont les "collections" dans MongoDB

Si vous ne connaissez pas l'un de ces points, veuillez lire ["Comment établir une connexion locale à MongoDB"](https://zellwk.com/blog/local-mongodb) avant de continuer.

Je suppose également que vous savez comment utiliser MongoDB pour créer une application CRUD simple. Si vous ne savez pas comment faire cela, veuillez lire ["Comment créer une application CRUD avec Node, Express et MongoDB"](https://zellwk.com/blog/crud-express-mongodb) avant de continuer.

## Bases de Mongoose

Ici, vous apprendrez comment :

1. Se connecter à la base de données
2. Créer un modèle
3. Créer un document
4. Trouver un document
5. Mettre à jour un document
6. Supprimer un document

### Connexion à une base de données

Tout d'abord, vous devez télécharger Mongoose.

```bash
npm install mongoose --save
```

Vous pouvez vous connecter à une base de données avec la méthode `connect`. Disons que nous voulons nous connecter à une base de données appelée `street-fighters`. Voici le code dont vous avez besoin :

```js
const mongoose = require('mongoose')
const url = 'mongodb://127.0.0.1:27017/street-fighters'

mongoose.connect(url, { useNewUrlParser: true })
```

Nous voulons savoir si notre connexion a réussi ou échoué. Cela nous aide à déboguer.

Pour vérifier si la connexion a réussi, nous pouvons utiliser l'événement `open`. Pour vérifier si la connexion a échoué, nous utilisons l'événement `error`.

```js
const db = mongoose.connection
db.once('open', _ => {
  console.log('Base de données connectée :', url)
})

db.on('error', err => {
  console.error('erreur de connexion :', err)
})
```

Essayez de vous connecter à la base de données. Vous devriez voir un journal comme ceci :

<img src="https://zellwk.com/images/2019/mongoose/connect-database.png" alt="Connecté à une base de données.">

### Création d'un modèle

Dans Mongoose, vous devez **utiliser des modèles pour créer, lire, mettre à jour ou supprimer des éléments** d'une collection MongoDB.

Pour créer un modèle, **vous devez créer un schéma**. Un schéma vous permet de **définir la structure d'une entrée** dans la collection. Cette entrée est également appelée un document.

Voici comment vous créez un schéma :

```js
const mongoose = require('mongoose')
const Schema = mongoose.Schema

const schema = new Schema({
  // ...
})
```

Vous pouvez utiliser [10 types de valeurs différents](https://mongoosejs.com/docs/guide.html) dans un schéma. La plupart du temps, vous utiliserez ces six :

- String
- Number
- Boolean
- Array
- Date
- ObjectId

Mettons cela en pratique.

Disons que nous voulons créer des personnages pour notre base de données Street Fighter.

Dans Mongoose, il est courant de **mettre chaque modèle dans son propre fichier**. Nous allons donc créer un fichier `Character.js` d'abord. Ce fichier `Character.js` sera placé dans le dossier `models`.

```bash
project/
    |- models/
        |- Character.js
```

Dans `Character.js`, nous créons un `characterSchema`.

```js
const mongoose = require('mongoose')
const Schema = mongoose.Schema

const characterSchema = new Schema({
  // ...
})
```

Disons que nous voulons enregistrer deux choses dans la base de données :

1. Nom du personnage
2. Nom de leur mouvement ultime

Les deux peuvent être représentés avec des chaînes de caractères.

```js
const mongoose = require('mongoose')
const Schema = mongoose.Schema

const characterSchema = new Schema({
  name: String,
  ultimate: String
})
```

Une fois que nous avons créé `characterSchema`, nous pouvons utiliser la méthode `model` de mongoose pour créer le modèle.

```js
module.exports = mongoose.model('Character', characterSchema)
```

### Création d'un document

Disons que vous avez un fichier appelé `index.js`. C'est ici que nous effectuerons les opérations Mongoose pour ce tutoriel.

```bash
project/
    |- index.js
    |- models/
        |- Character.js
```

Tout d'abord, vous devez charger le modèle Character. Vous pouvez faire cela avec `require`.

```js
const Character = require('./models/Character')
```

Disons que vous voulez créer un personnage appelé Ryu. Ryu a un mouvement ultime appelé "Shinku Hadoken".

Pour créer Ryu, vous utilisez `new`, suivi de votre modèle. Dans ce cas, c'est `new Character`.

```js
const ryu = new Character ({
  name: 'Ryu',
  ultimate: 'Shinku Hadoken'
})
```

`new Character` crée le personnage en mémoire. Il n'a pas encore été enregistré dans la base de données. **Pour enregistrer dans la base de données, vous pouvez exécuter la méthode `save`**.

```js
ryu.save(function (error, document) {
  if (error) console.error(error)
  console.log(document)
})
```

Si vous exécutez le code ci-dessus, vous devriez voir ceci dans la console.

<figure role="figure"><img src="https://zellwk.com/images/2019/mongoose/saved.png" alt="Ryu enregistré dans la base de données."></figure>

#### Promesses et Async/await

**Mongoose supporte les promesses.** Cela vous permet d'écrire un code plus lisible comme ceci :

```js
// Cela fait la même chose que ci-dessus
function saveCharacter (character) {
  const c = new Character(character)
  return c.save()
}

saveCharacter({
  name: 'Ryu',
  ultimate: 'Shinku Hadoken'
})
  .then(doc => { console.log(doc) })
  .catch(error => { console.error(error) })
```

Vous pouvez également utiliser le mot-clé `await` si vous avez une fonction asynchrone.

Si le code des promesses ou async/await vous semble étranger, je vous recommande de lire ["JavaScript async et await"](https://zellwk.com/blog/async-await) avant de continuer avec ce tutoriel.

```js
async function runCode() {
  const ryu = new Character({
    name: 'Ryu',
    ultimate: 'Shinku Hadoken'
  })

  const doc = await ryu.save()
  console.log(doc)
}

runCode()
  .catch(error => { console.error(error) })
```

Note : J'utiliserai le format async/await pour le reste du tutoriel.

#### Unicité

Mongoose ajoute un nouveau personnage à la base de données chaque fois que vous utilisez `new Character` et `save`. Si vous exécutez le(s) code(s) ci-dessus trois fois, vous vous attendriez à voir trois Ryu dans la base de données.

<figure role="figure"><img src="https://zellwk.com/images/2019/mongoose/three-ryus.png" alt="Trois Ryu dans la base de données."></figure>

Nous ne voulons pas avoir trois Ryu dans la base de données. Nous voulons avoir **UN SEUL Ryu**. Pour cela, nous pouvons utiliser l'option **unique**.

```js
const characterSchema = new Schema({
  name: { type: String, unique: true },
  ultimate: String
})
```

L'option `unique` **crée un index unique**. Elle garantit que nous ne pouvons pas avoir deux documents avec la même valeur (pour `name` dans ce cas).

Pour que `unique` fonctionne correctement, vous devez **effacer la collection Characters**. Pour effacer la collection Characters, vous pouvez utiliser ceci :

```js
await Character.deleteMany({})
```

Essayez d'ajouter deux Ryu dans la base de données maintenant. Vous obtiendrez une erreur `E11000 duplicate key error`. Vous ne pourrez pas enregistrer le deuxième Ryu.

<figure role="figure"><img src="https://zellwk.com/images/2019/mongoose/dup-error.png" alt="Erreur de clé dupliquée."></figure>

Ajoutons un autre personnage dans la base de données avant de continuer le reste du tutoriel.

```js
const ken = new Character({
  name: 'Ken',
  ultimate: 'Guren Enjinkyaku'
})

await ken.save()
```

<figure role="figure"><img src="https://zellwk.com/images/2019/mongoose/ryu-ken.png" alt="La base de données contient deux personnages."></figure>

### Trouver un document

Mongoose vous donne deux méthodes pour trouver des éléments dans MongoDB.

1. `findOne` : Obtient un document.
2. `find` : Obtient un tableau de documents

#### findOne

`findOne` **retourne le premier document** qu'il trouve. Vous pouvez spécifier n'importe quelle propriété à rechercher. Recherchons `Ryu` :

```js
const ryu = await Character.findOne({ name: 'Ryu' })
console.log(ryu)
```

<figure role="figure"><img src="https://zellwk.com/images/2019/mongoose/found-one.png" alt="Ryu trouvé dans la base de données."></figure>

#### find

`find` **retourne un tableau** de documents. Si vous spécifiez une propriété à rechercher, il retournera les documents qui correspondent à votre requête.

```js
const chars = await Character.find({ name: 'Ryu' })
console.log(chars)
```

<figure role="figure"><img src="https://zellwk.com/images/2019/mongoose/found-many-ryu.png" alt="Parcouru la base de données et trouvé un personnage avec le nom Ryu."></figure>

Si vous n'avez pas spécifié de propriétés à rechercher, il retournera un tableau qui contient tous les documents de la collection.

```js
const chars = await Character.find()
console.log(chars)
```

<figure role="figure"><img src="https://zellwk.com/images/2019/mongoose/found-many.png" alt="Trouvé deux personnages dans la base de données."></figure>

### Mettre à jour un document

Disons que Ryu a trois mouvements spéciaux :

1. Hadoken
2. Shoryuken
3. Tatsumaki Senpukyaku

Nous voulons ajouter ces mouvements spéciaux dans la base de données. Tout d'abord, nous devons mettre à jour notre `CharacterSchema`.

```js
const characterSchema = new Schema({
  name: { type: String, unique: true },
  specials: Array,
  ultimate: String
})
```

Ensuite, nous utilisons l'une de ces deux méthodes pour mettre à jour un personnage :

1. Utiliser `findOne`, puis utiliser `save`
2. Utiliser `findOneAndUpdate`

#### findOne et save

Tout d'abord, nous utilisons `findOne` pour obtenir Ryu.

```js
const ryu = await Character.findOne({ name: 'Ryu' })
console.log(ryu)
```

Ensuite, nous mettons à jour Ryu pour inclure ses mouvements spéciaux.

```js
const ryu = await Character.findOne({ name: 'Ryu' })
ryu.specials = [
  'Hadoken',
  'Shoryuken',
  'Tatsumaki Senpukyaku'
]
```

Après avoir modifié `ryu`, nous exécutons `save`.

```js
const ryu = await Character.findOne({ name: 'Ryu' })
ryu.specials = [
  'Hadoken',
  'Shoryuken',
  'Tatsumaki Senpukyaku'
]

const doc = await ryu.save()
console.log(doc)
```

<figure role="figure"><img src="https://zellwk.com/images/2019/mongoose/ryu-updated.png" alt="Ryu mis à jour."></figure>

#### findOneAndUpdate

`findOneAndUpdate` est la même chose que la méthode `findOneAndModify` de MongoDB.

Ici, vous recherchez Ryu et passez les champs que vous voulez mettre à jour en même temps.

```js
// Syntaxe
await findOneAndUpdate(filter, update)
```

```js
// Utilisation
const doc = await Character.findOneAndUpdate(
  { name: 'Ryu' },
  {
    specials: [
      'Hadoken',
      'Shoryuken',
      'Tatsumaki Senpukyaku'
    ]
  })

console.log(doc)
```

<figure role="figure"><img src="https://zellwk.com/images/2019/mongoose/ryu-updated.png" alt="Ryu mis à jour."></figure>

#### Différence entre findOne + save vs findOneAndUpdate

Deux différences majeures.

Tout d'abord, la **syntaxe pour ``findOne` + `save`` est plus facile à lire** que `findOneAndUpdate`.

Ensuite, `findOneAndUpdate` ne déclenche pas le middleware `save`.

**Je choisirai `findOne` + `save`** plutôt que `findOneAndUpdate` à tout moment à cause de ces deux différences.

### Supprimer un document

Il existe deux façons de supprimer un personnage :

1. `findOne` + `remove`
2. `findOneAndDelete`

#### Utilisation de findOne + remove

```js
const ryu = await Character.findOne({ name: 'Ryu' })
const deleted = await ryu.remove()
```

#### Utilisation de findOneAndDelete

```js
const deleted = await Character.findOneAndDelete({ name: 'Ken' })
```

## Sous-documents

Dans Mongoose, les **sous-documents** sont des documents qui sont **imbriqués dans d'autres documents**. Vous pouvez repérer un sous-document lorsqu'un schéma est imbriqué dans un autre schéma.

Note : MongoDB appelle les sous-documents **documents intégrés**.

```js
const childSchema = new Schema({
  name: String
});

const parentSchema = new Schema({
  // Sous-document unique
  child: childSchema,

  // Tableau de sous-documents
  children: [ childSchema ]
});
```

En pratique, vous n'avez pas besoin de créer un `childSchema` séparé comme dans l'exemple ci-dessus. Mongoose vous aide à créer des schémas imbriqués lorsque vous imbriquez un objet dans un autre objet.

```js
// Ce code est le même que ci-dessus
const parentSchema = new Schema({
  // Sous-document unique
  child: { name: String },

  // Tableau de sous-documents
  children: [{name: String }]
});
```

Dans cette section, vous apprendrez à :

1. Créer un schéma qui inclut un sous-document
2. Créer des documents qui contiennent des sous-documents
3. Mettre à jour des sous-documents qui sont des tableaux
4. Mettre à jour un seul sous-document

### Mise à jour de characterSchema

Disons que nous voulons créer un personnage appelé Ryu. Ryu a trois mouvements spéciaux.

1. Hadoken
2. Shinryuken
3. Tatsumaki Senpukyaku

Ryu a également un mouvement ultime appelé :

1. Shinku Hadoken

Nous voulons enregistrer les noms de chaque mouvement. Nous voulons également enregistrer les touches nécessaires pour exécuter ce mouvement.

Ici, chaque mouvement est un sous-document.

```js
const characterSchema = new Schema({
  name: { type: String, unique: true },
  // Tableau de sous-documents
  specials: [{
    name: String,
    keys: String
  }]
  // Sous-document unique
  ultimate: {
    name: String,
    keys: String
  }
})
```

Vous pouvez également utiliser la syntaxe childSchema si vous le souhaitez. Cela rend le schéma Character plus facile à comprendre.

```js
const moveSchema = new Schema({
  name: String,
  keys: String
})

const characterSchema = new Schema({
  name: { type: String, unique: true },
  // Tableau de sous-documents
  specials: [moveSchema],
  // Sous-document unique
  ultimate: moveSchema
})
```

### Création de documents contenant des sous-documents

Il existe deux façons de créer des documents contenant des sous-documents :

1. Passer un objet imbriqué dans `new Model`
2. Ajouter des propriétés dans le document créé.

#### Méthode 1 : Passer l'objet entier

Pour cette méthode, nous construisons un objet imbriqué qui contient à la fois le nom de Ryu et ses mouvements.

```js
const ryu = {
  name: 'Ryu',
  specials: [{
    name: 'Hadoken',
    keys: '\u00e2\u2020\u201c \u00e2\u2020\u02dc \u00e2\u2020\u2019 P'
  }, {
    name: 'Shoryuken',
    keys: '\u00e2\u2020\u2019 \u00e2\u2020\u201c \u00e2\u2020\u02dc \u00e2\u2020\u2019 P'
  }, {
    name: 'Tatsumaki Senpukyaku',
    keys: '\u00e2\u2020\u201c \u00e2\u2020\u2122 \u00e2\u2020\u0090 K'
  }],
  ultimate: {
    name: 'Shinku Hadoken',
    keys: '\u00e2\u2020\u201c \u00e2\u2020\u02dc \u00e2\u2020\u2019 \u00e2\u2020\u201c \u00e2\u2020\u02dc \u00e2\u2020\u2019 P'
  }
}
```

Ensuite, nous passons cet objet dans `new Character`.

```js
const char = new Character(ryu)
const doc = await char.save()
console.log(doc)
```

<figure role="figure"><img src="https://zellwk.com/images/2019/mongoose-subdocuments/ryu.png" alt="Image du document de Ryu."></figure>

#### Méthode 2 : Ajout de sous-documents plus tard

Pour cette méthode, nous créons d'abord un personnage avec `new Character`.

```js
const ryu = new Character({ name: 'Ryu' })
```

Ensuite, nous modifions le personnage pour ajouter des mouvements spéciaux :

```js
const ryu = new Character({ name: 'Ryu' })
const ryu.specials = [{
  name: 'Hadoken',
  keys: '\u00e2\u2020\u201c \u00e2\u2020\u02dc \u00e2\u2020\u2019 P'
}, {
  name: 'Shoryuken',
  keys: '\u00e2\u2020\u2019 \u00e2\u2020\u201c \u00e2\u2020\u02dc \u00e2\u2020\u2019 P'
}, {
  name: 'Tatsumaki Senpukyaku',
  keys: '\u00e2\u2020\u201c \u00e2\u2020\u2122 \u00e2\u2020\u0090 K'
}]
```

Ensuite, nous modifions le personnage pour ajouter le mouvement ultime :

```js
const ryu = new Character({ name: 'Ryu' })

// Ajoute les mouvements spéciaux
const ryu.specials = [{
  name: 'Hadoken',
  keys: '\u00e2\u2020\u201c \u00e2\u2020\u02dc \u00e2\u2020\u2019 P'
}, {
  name: 'Shoryuken',
  keys: '\u00e2\u2020\u2019 \u00e2\u2020\u201c \u00e2\u2020\u02dc \u00e2\u2020\u2019 P'
}, {
  name: 'Tatsumaki Senpukyaku',
  keys: '\u00e2\u2020\u201c \u00e2\u2020\u2122 \u00e2\u2020\u0090 K'
}]

// Ajoute le mouvement ultime
ryu.ultimate = {
  name: 'Shinku Hadoken',
  keys: '\u00e2\u2020\u201c \u00e2\u2020\u02dc \u00e2\u2020\u2019 \u00e2\u2020\u201c \u00e2\u2020\u02dc \u00e2\u2020\u2019 P'
}
```

Une fois que nous sommes satisfaits de `ryu`, nous exécutons `save`.

```js
const ryu = new Character({ name: 'Ryu' })

// Ajoute les mouvements spéciaux
const ryu.specials = [{
  name: 'Hadoken',
  keys: '\u00e2\u2020\u201c \u00e2\u2020\u02dc \u00e2\u2020\u2019 P'
}, {
  name: 'Shoryuken',
  keys: '\u00e2\u2020\u2019 \u00e2\u2020\u201c \u00e2\u2020\u02dc \u00e2\u2020\u2019 P'
}, {
  name: 'Tatsumaki Senpukyaku',
  keys: '\u00e2\u2020\u201c \u00e2\u2020\u2122 \u00e2\u2020\u0090 K'
}]

// Ajoute le mouvement ultime
ryu.ultimate = {
  name: 'Shinku Hadoken',
  keys: '\u00e2\u2020\u201c \u00e2\u2020\u02dc \u00e2\u2020\u2019 \u00e2\u2020\u201c \u00e2\u2020\u02dc \u00e2\u2020\u2019 P'
}

const doc = await ryu.save()
console.log(doc)
```

<figure role="figure"><img src="https://zellwk.com/images/2019/mongoose-subdocuments/ryu.png" alt="Image du document de Ryu."></figure>

### Mise à jour des sous-documents de tableau

La façon la plus simple de mettre à jour les sous-documents est :

1. Utiliser `findOne` pour trouver le document
2. Obtenir le tableau
3. Changer le tableau
4. Exécuter `save`

Par exemple, disons que nous voulons ajouter `Jodan Sokutou Geri` aux mouvements spéciaux de Ryu. Les touches pour `Jodan Sokutou Geri` sont `\u00e2\u2020\u201c \u00e2\u2020\u02dc \u00e2\u2020\u2019 K`.

Tout d'abord, nous trouvons Ryu avec `findOne`.

```js
const ryu = await Characters.findOne({ name: 'Ryu' })
```

Les documents Mongoose se comportent comme des objets JavaScript réguliers. Nous pouvons obtenir le tableau `specials` en écrivant `ryu.specials`.

```js
const ryu = await Characters.findOne({ name: 'Ryu' })
const specials = ryu.specials
console.log(specials)
```

<figure role="figure"><img src="https://zellwk.com/images/2019/mongoose-subdocuments/specials.png" alt="Journal des mouvements spéciaux."></figure>

Ce tableau `specials` est un tableau JavaScript normal.

```js
const ryu = await Characters.findOne({ name: 'Ryu' })
const specials = ryu.specials
console.log(Array.isArray(specials)) // true
```

Nous pouvons utiliser la méthode `push` pour ajouter un nouvel élément dans `specials`,

```js
const ryu = await Characters.findOne({ name: 'Ryu' })
ryu.specials.push({
  name: 'Jodan Sokutou Geri',
  keys: '\u00e2\u2020\u201c \u00e2\u2020\u02dc \u00e2\u2020\u2019 K'
})
```

Après avoir mis à jour `specials`, nous exécutons `save` pour enregistrer Ryu dans la base de données.

```js
const ryu = await Characters.findOne({ name: 'Ryu' })
ryu.specials.push({
  name: 'Jodan Sokutou Geri',
  keys: '\u00e2\u2020\u201c \u00e2\u2020\u02dc \u00e2\u2020\u2019 K'
})

const updated = await ryu.save()
console.log(updated)
```

<figure role="figure"><img src="https://zellwk.com/images/2019/mongoose-subdocuments/ryu-updated.png" alt="Ryu mis à jour avec Jodan Sokutou Geri"></figure>

### Mise à jour d'un seul sous-document

Il est encore plus facile de mettre à jour les sous-documents uniques. Vous pouvez modifier le document directement comme un objet normal.

Disons que nous voulons changer le nom ultime de Ryu de Shinku Hadoken à Dejin Hadoken. Ce que nous faisons est :

1. Utiliser `findOne` pour obtenir Ryu.
2. Changer le `name` dans `ultimate`
3. Exécuter `save`

```js
const ryu = await Characters.findOne({ name: 'Ryu' })
ryu.ultimate.name = 'Dejin Hadoken'

const updated = await ryu.save()
console.log(updated)
```

<figure role="figure"><img src="https://zellwk.com/images/2019/mongoose-subdocuments/ryu-3.png" alt="Document de Ryu avec Dejin Hadoken."></figure>

## Population

Les documents MongoDB ont une limite de taille de 16 Mo. Cela signifie que vous pouvez utiliser des sous-documents (ou documents intégrés) s'ils sont peu nombreux.

Par exemple, les personnages de Street Fighter ont un nombre limité de mouvements. Ryu n'a que 4 mouvements spéciaux. Dans ce cas, il est acceptable d'intégrer les mouvements directement dans le document du personnage de Ryu.

<figure role="figure"><img src="https://zellwk.com/images/2019/mongoose-population/ryu.png" alt="Document de Ryu."></figure>

Mais si vous avez des données qui peuvent contenir un nombre illimité de sous-documents, vous devez concevoir votre base de données différemment.

Une façon est de créer deux modèles séparés et de les combiner avec populate.

### Création des modèles

Disons que vous voulez créer un blog. Et vous voulez stocker le contenu du blog avec MongoDB. Chaque article de blog a un titre, un contenu et des commentaires.

Votre premier schéma pourrait ressembler à ceci :

```js
const blogPostSchema = new Schema({
  title: String,
  content: String,
  comments: [{
    comment: String
  }]
})

module.exports = mongoose.model('BlogPost', blogPostSchema)
```

Il y a un problème avec ce schéma.

Un article de blog peut avoir un nombre illimité de commentaires. Si un article de blog explose en popularité et que les commentaires gonflent, le document pourrait dépasser la limite de 16 Mo imposée par MongoDB.

Cela signifie que nous ne devrions pas intégrer les commentaires dans les articles de blog. Nous devrions créer une collection séparée pour les commentaires.

```js
const comments = new Schema({
  comment: String
})

module.exports = mongoose.model('Comment', commentSchema)
```

Dans Mongoose, nous pouvons lier les deux modèles avec Population.

Pour utiliser Population, nous devons :

1. Définir `type` d'une propriété sur `Schema.Types.ObjectId`
2. Définir `ref` sur le modèle que nous voulons lier.

Ici, nous voulons que `comments` dans `blogPostSchema` soit lié à la collection Comment. Voici le schéma que nous utiliserons :

```js
const blogPostSchema = new Schema({
  title: String,
  content: String,
  comments: [{ type: Schema.Types.ObjectId, ref: 'Comment' }]
})

module.exports = mongoose.model('BlogPost', blogPostSchema)
```

### Création d'un article de blog

Disons que vous voulez créer un article de blog. Pour créer l'article de blog, vous utilisez `new BlogPost`.

```js
const blogPost = new BlogPost({
  title: 'Weather',
  content: `How's the weather today?`
})
```

Un article de blog peut avoir zéro commentaire. Nous pouvons enregistrer cet article de blog avec `save`.

```js
const doc = await blogPost.save()
console.log(doc)
```

<figure role="figure"><img src="https://zellwk.com/images/2019/mongoose-population/blog-post-no-comments.png" alt="Créé un document d'article de blog sans commentaires."></figure>

### Création de commentaires

Maintenant, disons que nous voulons créer un commentaire pour l'article de blog. Pour ce faire, nous créons et enregistrons le commentaire.

```js
const comment = new Comment({
  comment: `It's damn hot today`
})

const savedComment = await comment.save()
console.log(savedComment)
```

<figure role="figure"><img src="https://zellwk.com/images/2019/mongoose-population/comment.png" alt="Créé et enregistré un commentaire."></figure>

Remarquez que le commentaire enregistré a un attribut `_id`. Nous devons ajouter cet attribut `_id` dans le tableau `comments` de l'article de blog. Cela crée le lien.

```js
// Enregistre le commentaire dans la base de données
const savedComment = await comment.save()

// Ajoute le commentaire à l'article de blog
// Ensuite, enregistre l'article de blog dans la base de données
const blogPost = await BlogPost.findOne({ title: 'Weather' })
blogPost.comments.push(savedComment._id)
const savedPost = await blogPost.save()
console.log(savedPost)
```

<figure role="figure" aria-label="Article de blog avec commentaires."><img src="https://zellwk.com/images/2019/mongoose-population/blog-post-with-comments.png" alt=""><figcaption>Article de blog avec commentaires.</figcaption></figure>

### Recherche d'articles de blog et de leurs commentaires

Si vous essayez de rechercher l'article de blog, vous verrez que l'article de blog contient un tableau d'IDs de commentaires.

```js
const blogPost = await BlogPost.findOne({ title: 'Weather' })
console.log(blogPost)
```

<figure role="figure"><img src="https://zellwk.com/images/2019/mongoose-population/blog-post-with-comments.png" alt="Article de blog trouvé contenant des IDs de commentaires."></figure>

Il existe quatre façons d'obtenir des commentaires.

1. Population Mongoose
2. Méthode manuelle #1
3. Méthode manuelle #2
4. Méthode manuelle #3

#### Population Mongoose

Mongoose vous permet de récupérer des documents liés avec la méthode `populate`. Ce que vous devez faire est d'appeler `.populate` lorsque vous exécutez avec `findOne`.

Lorsque vous appelez populate, vous devez passer la `clé` de la propriété que vous voulez peupler. Dans ce cas, la `clé` est `comments`. (Note : Mongoose appelle cette `clé` un "chemin").

```js
const blogPost = await BlogPost.findOne({ title: 'Weather' })
  .populate('comments')
console.log(blogPost)
```

<figure role="figure"><img src="https://zellwk.com/images/2019/mongoose-population/populated.png" alt="Commentaires peuplés par Mongoose."></figure>

#### Méthode manuelle (méthode 1)

Sans Mongoose Populate, vous devez trouver les commentaires manuellement. Tout d'abord, vous devez obtenir le tableau des commentaires.

```js
const blogPost = await BlogPost.findOne({ title: 'Weather' })
  .populate('comments')
const commentIDs = blogPost.comments
```

Ensuite, vous parcourez `commentIDs` pour trouver chaque commentaire. Si vous optez pour cette méthode, il est légèrement plus rapide d'utiliser `Promise.all`.

```js
const commentPromises = commentIDs.map(_id => {
  return Comment.findOne({ _id })
})
const comments = await Promise.all(commentPromises)
console.log(comments)
```

<figure role="figure"><img src="https://zellwk.com/images/2019/mongoose-population/found-comments.png" alt="Commentaires trouvés."></figure>


#### Méthode manuelle (méthode 2)

Mongoose vous donne un opérateur `$in`. Vous pouvez utiliser cet opérateur `$in` pour trouver tous les commentaires dans un tableau. Cette syntaxe prend un peu d'effort pour s'y habituer.

Si je devais faire la méthode manuelle, je préférerais la méthode manuelle #1 à celle-ci.

```js
const commentIDs = blogPost.comments
const comments = await Comment.find({
    '_id': { $in: commentIDs }
})

console.log(comments)
```

<figure role="figure"><img src="https://zellwk.com/images/2019/mongoose-population/found-comments.png" alt="Commentaires trouvés."></figure>

#### Méthode manuelle (méthode 3)

Pour la troisième méthode, nous devons changer le schéma. Lorsque nous enregistrons un commentaire, nous lions le commentaire à l'article de blog.

```js
// Lier les commentaires à l'article de blog
const commentSchema = new Schema({
  comment: String
  blogPost: [{ type: Schema.Types.ObjectId, ref: 'BlogPost' }]
})

module.exports = mongoose.model('Comment', commentSchema)
```

Vous devez enregistrer le commentaire dans l'article de blog, et l'ID de l'article de blog dans le commentaire.

```js
const blogPost = await BlogPost.findOne({ title: 'Weather' })

// Enregistre le commentaire
const comment = new Comment({
  comment: `It's damn hot today`,
  blogPost: blogPost._id
})
const savedComment = comment.save()

// Lie l'article de blog au commentaire
blogPost.comments.push(savedComment._id)
await blogPost.save()
```

Une fois que vous avez fait cela, vous pouvez rechercher dans la collection Comments les commentaires qui correspondent à l'ID de votre article de blog.

```js
// Recherche des commentaires
const blogPost = await BlogPost.findOne({ title: 'Weather' })
const comments = await Comment.find({ _id: blogPost._id })
console.log(comments)
```

<figure role="figure"><img src="https://zellwk.com/images/2019/mongoose-population/found-comments.png" alt="Commentaires trouvés."></figure>

Je préférerais la méthode manuelle #3 à la méthode manuelle #1 et à la méthode manuelle #2.

Et la population bat les trois méthodes manuelles.

## Résumé rapide

Vous avez appris à utiliser Mongoose à trois niveaux différents dans cet article :

1. Mongoose de base
2. Sous-documents Mongoose
3. Population Mongoose

C'est tout !


<hr>

Merci d'avoir lu. Cet article a été initialement publié sur [mon blog](https://zellwk.com/blog/mongoose
).  Inscrivez-vous à ma newsletter si vous voulez plus d'articles pour vous aider à devenir un meilleur développeur frontend.