---
title: Comment journaliser une API Node.js dans une application Express.js avec des
  plugins Mongoose
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-13T21:46:05.000Z'
originalURL: https://freecodecamp.org/news/how-to-log-a-node-js-api-in-an-express-js-app-with-mongoose-plugins-efe32717b59
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tLsF0BLHtCPk5voPS1yFhw.jpeg
tags:
- name: debugging
  slug: debugging
- name: Developer
  slug: developer
- name: JavaScript
  slug: javascript
- name: MongoDB
  slug: mongodb
- name: Node.js
  slug: nodejs
seo_title: Comment journaliser une API Node.js dans une application Express.js avec
  des plugins Mongoose
seo_desc: 'By Shailesh Shekhawat


  This tutorial will require prior knowledge of the mongoose Object Relational Mapping
  (ORM) technique


  Introduction

  As your application grows, logging becomes a crucial part to keep track of everything.
  It is especially importan...'
---

Par Shailesh Shekhawat

> Ce tutoriel nécessitera des connaissances préalables de la technique de mappage objet-relationnel (ORM) [mongoose](https://mongoosejs.com/)

#### Introduction

À mesure que votre application grandit, la journalisation devient une partie cruciale pour garder une trace de tout. Elle est particulièrement importante à des fins de débogage.

De nos jours, il existe déjà des modules de journalisation disponibles sur npm. Ces modules peuvent stocker les journaux dans un fichier dans différents formats ou niveaux. Nous allons discuter de la journalisation de l'API dans votre application Node.js Express en utilisant l'ORM populaire Mongoose.

Alors, comment créer un **plugin Mongoose** qui effectuera la journalisation pour vous de manière plus propre et facilitera la journalisation de l'API ?

#### Qu'est-ce qu'un plugin dans Mongoose ?

Dans Mongoose, les schémas sont pluggables. Un plugin est comme une fonction que vous pouvez utiliser dans votre schéma et réutiliser encore et encore sur les instances de schéma.

Mongoose fournit également des **plugins globaux** que vous pouvez utiliser pour tous les schémas. Par exemple, nous allons écrire un plugin qui créera un `**diff**` de deux `**jsons**` et l'écrira dans `**mongodb**`**.**

### Étape 1 : Création d'un modèle de schéma de journalisation de base

Créons un schéma de journalisation de base avec les six propriétés suivantes :

* **Action :** Comme son nom l'indique, il s'agira d'un cours d'action de l'API, qu'il s'agisse de `create`, `update`, `delete` ou autre chose.
* **Catégorie :** Catégorie de l'API. Par exemple, médecins et patients. C'est plus comme une classe.
* **CrééPar :** Utilisateur qui utilise l'API ou l'a invoquée.
* **Message :** Ici, vous pouvez inclure tout type de message que vous souhaitez afficher et qui aura du sens ou aidera lors du débogage.
* **Diff :** Il s'agit de la propriété principale qui contiendra le _diff_ de deux _JSONs_

Vous pouvez ajouter plus de champs si vous le souhaitez et qui ont du sens pour votre propre application. Un schéma peut être modifié et mis à niveau selon les besoins.

Voici notre modèle : `models/log.js`

```js
const mongoose = require('mongoose')
const Schema = mongoose.Schema
const { ObjectId } = Schema

const LogSchema = new Schema({
  action: { type: String, required: true },
  category: { type: String, required: true },
  createdBy: { type: ObjectId, ref: 'Account', required: true },
  message: { type: String, required: true },
  diff: { type: Schema.Types.Mixed },
},{
  timestamps: { createdAt: 'createdAt', updatedAt: 'updatedAt' },
})

LogSchema.index({ action: 1, category: 1 })

module.exports = mongoose.model('Log', LogSchema)
```

### Étape 2 : Écrire une fonction pour obtenir la différence entre 2 JSONs

Donc, l'étape suivante consiste à avoir besoin d'une fonction réutilisable qui créera un `diff` de deux JSONs à la volée.

Appelons cela `diff.js`

```js
const _ = require('lodash')

exports.getDiff = (curr, prev) => {
  function changes(object, base) {
    return _.transform(object, (result, value, key) => {
      if (!_.isEqual(value, base[key]))
        result[key] = (_.isObject(value) && _.isObject(base[key])) ? changes(value, base[key]) : value
    })
 }
 return changes(curr, prev)
}
```

J'ai utilisé **[lodash](https://lodash.com/docs/4.17.10)**, qui est une bibliothèque populaire, pour fournir la même fonctionnalité.

Décomposons la fonction ci-dessus et voyons ce qui se passe :

* **_.transform :** C'est une alternative à `.reduce` pour les tableaux. Basiquement, il va itérer sur les `keys` et `values` de votre objet. Il fournit un `accumulator` qui est le premier argument. `result` est l'accumulateur et il est mutable.
* **_.isEqual :** Effectue une comparaison profonde entre deux valeurs pour déterminer si elles sont équivalentes.

> **_isEqual_**_: Cette méthode supporte la comparaison de tableaux, de tampons de tableaux, de booléens, d'objets date, d'objets erreur, de maps, de nombres, d'objets `Object`, de regex, de sets, de chaînes, de symboles et de tableaux typés. Les objets `Object` sont comparés par leurs propres propriétés énumérables, non héritées. Les fonctions et les nœuds DOM sont comparés par égalité stricte, c'est-à-dire `===`._

Ici, nous itérons sur chaque propriété et valeur de l'objet et les comparons avec notre ancien/précédent objet.

Si la `value` de l'objet actuel n'est pas égale à une valeur de la même propriété dans l'objet précédent : `base[key]` et si cette valeur est l'objet lui-même, nous appelons la fonction `changes` **récursivement** jusqu'à ce qu'elle obtienne une valeur qui sera finalement stockée dans `result` comme `result[key] = value`.

### Étape 3 : Créer un plugin pour utiliser diff et l'enregistrer dans la base de données

Maintenant, nous devons garder une trace du `document` précédent dans la base de données et créer un `diff` avant de l'enregistrer dans `mongodb`.

```js
const _ = require('lodash')
const LogSchema = require('../models/log')
const { getDiff } = require('../utils/diff')

const plugin = function (schema) {
  schema.post('init', doc => {
    doc._original = doc.toObject({transform: false})
  })
  schema.pre('save', function (next) {
    if (this.isNew) {
      next()
    }else {
      this._diff = getDiff(this, this._original)
      next()
    }
})

  schema.methods.log = function (data)  {
    data.diff = {
      before: this._original,
      after: this._diff,
    }
    return LogSchema.create(data)
  }
}

module.exports = plugin
```

Dans Mongoose, il existe différents hooks disponibles. Pour l'instant, nous devons utiliser les méthodes `[init](https://mongoosejs.com/docs/api.html#document_Document-init)` et `[save](https://mongoosejs.com/docs/api.html#document_Document-save)` disponibles sur le schéma.

`this.isNew()` : Si vous créez un nouveau document, retournez simplement le middleware `next()`.

Dans `schema.post('init')` `[toObject()](https://mongoosejs.com/docs/api.html#document_Document-toObject)` :

```js
doc._original = doc.toObject({transform: false})
```

Les `Model` de Mongoose héritent des `Document`, qui ont une méthode `toObject()`. Elle convertira un `document` en un `Object()` et `transform:false` est pour ne pas permettre de transformer l'objet retourné.

### Étape 4 : Utilisation — Comment utiliser dans une API express.js

Dans votre fichier principal `server.js` ou `app.js` :

Initialisez un plugin [global](https://mongoosejs.com/docs/plugins.html) afin qu'il soit disponible pour tous les schémas. Vous pouvez également l'utiliser pour un schéma particulier en l'initialisant dans le modèle de schéma.

```js
const mongoose = require('mongoose')

mongoose.plugin(require('./app/utils/diff-plugin'))
```

Voici un exemple de base d'une API de mise à jour d'`user` :

```js
const User = require('../models/user')

exports.updateUser = (req, res, next) => {
  return User.findById(req.params.id)
    .then(user => {
        if (!user)
           throw new Error('L\'utilisateur cible n\'existe pas. Échec de la mise à jour.')
       const { name } = req.body
       if (name) user.name = name
       return user.save()
     })
     .then(result => {
       res.json(result)
       return result
     })
     .catch(next)
     .then(user => {
         if (user && typeof user.log === 'function') { 
            const data = {
              action: 'update-user',
              category: 'users',
              createdBy: req.user.id,
              message: 'Nom d\'utilisateur mis à jour',
         }
         return user.log(data)
     }
     }).catch(err => {
         console.log('Erreur capturée lors de la journalisation : ', err)
       })
}
```

### Conclusion

Dans ce tutoriel, vous avez appris à créer un plugin Mongoose et à l'utiliser pour journaliser les `changements` dans votre API. Vous pouvez faire beaucoup plus avec les plugins pour construire une application node robuste.

Voici des ressources pour en savoir plus sur Mongoose et l'utilisation des plugins :

* Guide 80/20 des plugins mongoose : [http://thecodebarbarian.com/2015/03/06/guide-to-mongoose-plugins](http://thecodebarbarian.com/2015/03/06/guide-to-mongoose-plugins)
* [https://mongoosejs.com/docs/plugins.html](https://mongoosejs.com/docs/plugins.html)

J'espère que vous trouverez ce tutoriel utile, n'hésitez pas à me contacter [ici](https://101node.io) si vous avez des questions.

Suivez [Shailesh Shekhawat](https://www.freecodecamp.org/news/author/thatshailesh/) pour être notifié chaque fois que je publie un nouvel article.

_N'hésitez pas à applaudir si vous avez trouvé cela digne d'être lu !_

_Originalement publié sur [101node.io](https://101node.io/blog/better-logging-with-mongoose-plugins-in-node-js-express-app/) le 2 septembre 2018._