---
title: Comment automatiser les migrations de base de données dans MongoDB
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-31T18:23:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-automate-database-migrations-in-mongodb-d6b68efe084e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4cqBCNV_7TmcsdogIaxzUA.jpeg
tags:
- name: database
  slug: database
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: Productivity
  slug: productivity
- name: 'tech '
  slug: tech
seo_title: Comment automatiser les migrations de base de données dans MongoDB
seo_desc: 'By Shailesh Shekhawat

  Introduction

  As a software developer at some point, you might have to deal with database migrations
  in one way or another.

  As software or applications evolve and improve over the time, your database must
  as well. And we have to ...'
---

Par Shailesh Shekhawat

### **Introduction**

En tant que développeur logiciel, à un moment donné, vous devrez peut-être gérer des migrations de base de données d'une manière ou d'une autre.

À mesure que les logiciels ou les applications évoluent et s'améliorent avec le temps, votre base de données doit également évoluer. Et nous devons nous assurer que les données restent cohérentes dans toute l'application.

Il existe un certain nombre de façons différentes dont un schéma peut changer d'une version de votre application à la suivante.

* **Un nouveau membre est ajouté**
* **Un membre est supprimé**
* **Un membre est renommé**
* **Le type d'un membre est changé**
* **La représentation d'un membre est changée**

**Alors, comment gérez-vous tous les changements ci-dessus ?**

<iframe src="https://giphy.com/embed/a5viI92PAF89q" width="480" height="331" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/reaction-a5viI92PAF89q">via GIPHY</a></p>

Il existe deux stratégies :

* Écrire un script qui prendra en charge la mise à niveau du schéma ainsi que sa rétrogradation vers les versions précédentes
* Mettre à jour vos documents au fur et à mesure qu'ils sont utilisés

La deuxième stratégie est beaucoup plus dépendante du code et doit rester dans votre base de code. Si le code est somehow supprimé, alors de nombreux documents ne sont pas mis à niveau.

Par exemple, s'il y a eu 3 versions d'un document, [1, 2, et 3] et que nous supprimons le code de mise à niveau de la version 1 à la version 2, tous les documents qui existent encore en version 1 ne sont pas mis à niveau. Personnellement, je vois cela comme un surcoût de maintenance du code et cela devient inflexible.

Puisque cet article traite de l'automatisation des migrations, je vais vous montrer comment vous pouvez écrire un script simple qui prendra en charge les changements de schéma ainsi que les tests unitaires.

### Un membre a été ajouté

Lorsque qu'un membre a été ajouté au schéma, les documents existants n'auront pas l'information. Vous devez donc interroger tous les documents où ce membre n'existe pas et les mettre à jour.

Procedons à l'écriture de code.

Il existe déjà plusieurs modules npm disponibles, mais j'ai utilisé la bibliothèque [node-migrate](https://github.com/tj/node-migrate). J'en ai essayé d'autres aussi, mais certains d'entre eux ne sont plus bien maintenus, et j'ai rencontré des problèmes pour me configurer avec d'autres.

#### Prérequis

* [node-migrate](https://github.com/tj/node-migrate) — Framework de migration abstrait pour Node
* [mongodb](https://www.npmjs.com/package/mongodb) — Pilote natif de MongoDB pour Nodejs
* [Mocha](https://mochajs.org/) — Framework de test
* [Chai](https://www.chaijs.com/) — Bibliothèque d'assertion pour écrire des cas de test
* [Bluebird](http://bluebirdjs.com/docs/install.html) : Bibliothèque de promesses pour gérer les appels d'API asynchrones
* [mkdirp](https://www.npmjs.com/package/mkdirp) : Comme `mkdir -p` mais en Node.js
* [rimraf](https://www.npmjs.com/package/rimraf) : `rm -rf` pour Node

### État de la migration

L'état de la migration est la clé la plus importante pour suivre votre migration actuelle. Sans cela, nous ne pourrons pas suivre :

* Combien de migrations ont été effectuées
* Quelle était la dernière migration
* Quelle est la version actuelle du schéma que nous utilisons

Et sans états, il n'y a aucun moyen de revenir en arrière, de mettre à niveau, et vice-versa vers un état différent.

#### Création de migrations

Pour créer une migration, exécutez `migrate create <titre>` avec un titre.

Par défaut, un fichier dans `./migrations/` sera créé avec le contenu suivant :

```js
'use strict'

module.exports.up = function (next) {
  next()
}

module.exports.down = function (next) {
  next()
}
```

Prenons un exemple de schéma `User` où nous avons une propriété `name` qui inclut à la fois les noms `first` et `last`.

Maintenant, nous voulons changer le schéma pour avoir une propriété `last` distincte.

Ainsi, pour automatiser cela, nous allons lire `name` à l'exécution et extraire le nom de famille et l'enregistrer en tant que nouvelle propriété.

Créez une migration avec cette commande :

```bash
$ migrate create add-last-name.js
```

Cet appel créera `./migrations/{timestamp in milliseconds}-add-last-name.js` sous le dossier `migrations` dans le répertoire racine.

Écrivons le code pour ajouter un nom de famille au schéma et aussi pour le supprimer.

#### Migration Up

Nous allons trouver tous les utilisateurs où la propriété `lastName` n'existe pas et créer une nouvelle propriété `lastName` dans ces documents.

```js
'use strict'
const Bluebird = require('bluebird')
const mongodb = require('mongodb')
const MongoClient = mongodb.MongoClient
const url = 'mongodb://localhost/Sample'
Bluebird.promisifyAll(MongoClient)

module.exports.up = next => {
  let mClient = null
  return MongoClient.connect(url)
  .then(client => {
    mClient = client
    return client.db();
  })
  .then(db => {
    const User = db.collection('users')
    return User
      .find({ lastName: { $exists: false }})
      .forEach(result => {
        if (!result) return next('All docs have lastName')
        if (result.name) {
           const { name } = result
           result.lastName = name.split(' ')[1]
           result.firstName = name.split(' ')[0]
        }
        return db.collection('users').save(result)
     })
  })
  .then(() => {
    
    mClient.close()
    return next()
  })
   .catch(err => next(err))
}
```

#### Migration Down

De même, écrivons une fonction où nous allons supprimer `lastName` :

```js
module.exports.down = next => {
let mClient = null
return MongoClient
   .connect(url)  
   .then(client => {
    mClient = client
    return client.db()
  })
  .then(db =>
    db.collection('users').update(
    {
       lastName: { $exists: true }
    },
    {
      $unset: { lastName: "" },
    },
     { multi: true }
  ))
  .then(() => {
    mClient.close()
    return next()
  })
  .catch(err => next(err))

}
```

#### Exécution des migrations

Consultez comment les migrations sont exécutées ici : [exécution des migrations](https://github.com/tj/node-migrate#running-migrations).

### Écrire un stockage d'état personnalisé

Par défaut, `migrate` stocke l'état des migrations qui ont été exécutées dans un fichier (`.migrate`).

Le fichier `.migrate` contiendra le code suivant :

```json
{
  "lastRun": "{timestamp in milliseconds}-add-last-name.js",
  "migrations": [
    {
      "title": "{timestamp in milliseconds}-add-last-name.js",
      "timestamp": {timestamp in milliseconds}
    }
  ]
}
```

Mais vous pouvez fournir un moteur de stockage personnalisé si vous souhaitez faire quelque chose de différent, comme les stocker dans votre base de données de choix.

Un moteur de stockage a une interface simple de `load(fn)` et `save(set, fn)`.

Tant que ce qui entre en tant que `set` sort de la même manière sur `load`, alors vous êtes prêt à partir !

Créons le fichier `db-migrate-store.js` dans le répertoire racine du projet.

```js
const mongodb = require('mongodb')
const MongoClient = mongodb.MongoClient
const Bluebird = require('bluebird')

Bluebird.promisifyAll(MongoClient)
class dbStore {
   constructor () {
     this.url = 'mongodb://localhost/Sample' . // Gérez cela selon votre environnement
    this.db = null
    this.mClient = null
   }
   connect() {
     return MongoClient.connect(this.url)
      .then(client => {
        this.mClient = client
        return client.db()
      })
   }
    load(fn) {
      return this.connect()
      .then(db => db.collection('migrations').find().toArray())
      .then(data => {
        if (!data.length) return fn(null, {})
        const store = data[0]
        // Vérifiez si le document ne contient pas les propriétés requises
          if (!Object
               .prototype
               .hasOwnProperty
               .call(store, 'lastRun') 
                ||
              !Object
              .prototype
              .hasOwnProperty
             .call(store, 'migrations'))
            {
            return fn(new Error('Fichier de stockage invalide'))
            }
        return fn(null, store)
      }).catch(fn)
    }
   save(set, fn) {
     return this.connect()
      .then(db => db.collection('migrations')
      .update({},
       {
         $set: {
           lastRun: set.lastRun,
         },
         $push: {
            migrations: { $each: set.migrations },
         },
      },
      {
         upsert: true,
         multi: true,
       }
      ))
       .then(result => fn(null, result))
       .catch(fn)
   }
}

module.exports = dbStore
```

`**load(fn)**` Dans cette fonction, nous vérifions simplement si le document de migration existant qui a été chargé contient la propriété `lastRun` et le tableau `migrations`.

`**save(set,fn)**` Ici, `set` est fourni par la bibliothèque et nous mettons à jour la valeur `lastRun` et ajoutons `migrations` au tableau existant.

Vous vous demandez peut-être où le fichier ci-dessus `db-migrate-store.js` est utilisé. Nous le créons parce que nous voulons stocker l'état dans la base de données, et non dans le dépôt de code.

Voici des exemples de tests où vous pouvez voir son utilisation.

### Automatiser les tests de migration

Installez Mocha :

```bash
$ npm install -g mocha
```

> Nous l'avons installé globalement pour pouvoir exécuter `mocha` depuis le terminal.

#### Structure

Pour configurer les tests de base, créez un nouveau dossier appelé « test » à la racine du projet, puis ajoutez un dossier appelé _migrations_ à l'intérieur.

Votre structure de fichiers/dossiers devrait maintenant ressembler à ceci :

```
├── package.json
├── app
│   ├── server.js
│   ├── models
│   │   └── user.js
│   └── routes
│       └── user.js
└── test
    migrations
    ├── create-test.js
    ├── up-test.js 
    └── down-test.js
```

#### Test — Créer une migration

**Objectif :** Il devrait créer le répertoire et le fichier de migrations.

`$ migrate create add-last-name`

Cela créera implicitement le fichier `./migrations/{timestamp in milliseconds}-add-last-name.js` sous le dossier `migrations` dans le répertoire racine.

Ajoutez maintenant le code suivant au fichier `create-test.js` :

```js
const Bluebird = require('bluebird')
const { spawn } = require('child_process')
const mkdirp = require('mkdirp')
const rimraf = require('rimraf')
const path = require('path')
const fs = Bluebird.promisifyAll(require('fs'))

describe('[Migrations]', () => {
    const run = (cmd, args = []) => {
    const process = spawn(cmd, args)
    let out = ""
    return new Bluebird((resolve, reject) => {
       process.stdout.on('data', data => {
         out += data.toString('utf8')
       })
      process.stderr.on('data', data => {
        out += data.toString('utf8')
      })
      process.on('error', err => {
         reject(err)
      })
     process.on('close', code => {
      resolve(out, code)
     })
   })
 }
    
const TMP_DIR = path.join(__dirname, '..', '..', 'tmp')
const INIT = path.join(__dirname, '..', '..', 'node_modules/migrate/bin', 'migrate-init')
const init = run.bind(null, INIT)
const reset = () => {
   rimraf.sync(TMP_DIR)
   rimraf.sync(path.join(__dirname, '..', '..', '.migrate'))
}

beforeEach(reset)
afterEach(reset)
describe('init', () => {
   beforeEach(mkdirp.bind(mkdirp, TMP_DIR))

   it('should create a migrations directory', done => {
      init()
      .then(() => fs.accessSync(path.join(TMP_DIR, '..', 'migrations')))
      .then(() => done())
      .catch(done)
   })
 })
})
```

Dans le test ci-dessus, nous utilisons la commande `migrate-init` pour créer le répertoire de migrations et le supprimer après chaque cas de test en utilisant `rimraf` qui est `rm -rf` sous Unix.

Plus tard, nous utilisons la fonction `fs.accessSync` pour vérifier si le dossier `migrations` existe ou non.

#### Test — Migration Up

**Objectif :** Il devrait ajouter `lastName` au schéma et stocker l'état de la migration.

Ajoutez le code suivant au fichier `up-test.js` :

```js
const chance = require('chance')()
const generateUser = () => ({
   email: chance.email(),
   name: `${chance.first()} ${chance.last()}`
 })
const migratePath = path.join(__dirname, '..', '..', 'node_modules/migrate/bin', 'migrate')
const migrate = run.bind(null, migratePath)

describe('[Migration: up]', () => {
   before(done => {
     MongoClient
     .connect(url)
     .then(client => {
       db = client.db()
      return db.collection('users').insert(generateUser())
      })
      .then(result => {
       if (!result) throw new Error('Failed to insert')
       return done()
      }).catch(done)
   })
   it('should run up on specified migration', done => {
     migrate(['up', 'mention here the file name we created above', '--store=./db-migrate-store.js'])
    .then(() => {
       const promises = []
       promises.push(
        db.collection('users').find().toArray()
       )
     Bluebird.all(promises)
    .then(([users]) => {
       users.forEach(elem => {
         expect(elem).to.have.property('lastName')
      })
      done()
    })
   }).catch(done)
 })
after(done => {
    rimraf.sync(path.join(__dirname, '..', '..', '.migrate'))
    db.collection('users').deleteMany()
    .then(() => {
      rimraf.sync(path.join(__dirname, '..', '..', '.migrate'))
      return done()
   }).catch(done)
 })
})
```

De même, vous pouvez écrire la migration down et les fonctions `before()` et `after()` restent essentiellement les mêmes.

### Conclusion

Espérons que vous pouvez maintenant automatiser vos changements de schéma avec des tests appropriés. :)

Récupérez le code final depuis le [dépôt](https://github.com/thatshailesh/mongodb-migration).

_N'hésitez pas à applaudir si vous avez trouvé cela utile !_