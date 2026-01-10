---
title: How to automate database migrations in MongoDB
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
seo_title: null
seo_desc: 'By Shailesh Shekhawat

  Introduction

  As a software developer at some point, you might have to deal with database migrations
  in one way or another.

  As software or applications evolve and improve over the time, your database must
  as well. And we have to ...'
---

By Shailesh Shekhawat

### **Introduction**

As a software developer at some point, you might have to deal with database migrations in one way or another.

As software or applications evolve and improve over the time, your database must as well. And we have to make sure data remains consistent throughout the application.

There are a number of different ways that a schema can change from one version of your application to the next.

* **A new member is added**
* **A member is removed**
* **A member is renamed**
* **The type of a member is changed**
* **The representation of a member is changed**

**So how do you handle all of the above changes?**

<iframe src="https://giphy.com/embed/a5viI92PAF89q" width="480" height="331" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/reaction-a5viI92PAF89q">via GIPHY</a></p>

There are two strategies:

* Write a script that will take care of upgrading the schema as well as downgrading it to previous versions
* Update your documents as they are used

The second one is much more code-dependent and must stay in your codebase. If the code is somehow removed, then many of documents are not upgradeable.

For instance, if there have been 3 versions of a document, [1, 2, and 3] and we remove the upgrade code from version 1 to version 2, any documents that still exist as version 1 are not upgradeable. I personally see this as overhead to maintaining code and it becomes inflexible.

Since this article is about automating migrations, I am going to show you how you can write a simple script that will take care of schema changes as well as unit tests.

### A Member Has Been Added

When a member has been added to the schema, existing document won’t have the info. So you need to query all the documents where this member doesn’t exist and update them.

Let’s proceed with writing some code.

There are quite a few npm modules available already, but I have used the library [node-migrate](https://github.com/tj/node-migrate). I have tried others too, but some of them are not well-maintained anymore, and I faced issues getting set up with others.

#### Prerequisites

* [node-migrate](https://github.com/tj/node-migrate) — Abstract migration framework for Node
* [mongodb](https://www.npmjs.com/package/mongodb) — a Native driver of MongoDB for Nodejs
* [Mocha](https://mochajs.org/) — Testing framework
* [Chai](https://www.chaijs.com/) — Assertion library for writing test cases
* [Bluebird](http://bluebirdjs.com/docs/install.html): Promise library for handling async API calls
* [mkdirp](https://www.npmjs.com/package/mkdirp): Like `mkdir -p` but in Node.js
* [rimraf](https://www.npmjs.com/package/rimraf): `rm -rf` for Node

### Migration state

A migration state is the most important key for keeping track of your current migration. Without it, we won’t be able to track:

* How many migrations have been done
* What was the last migration
* What is the current version of the schema we are using

And without states, there is no way to rollback, upgrade, and vice-versa to a different state.

#### Creating Migrations

To create a migration, execute `migrate create <tit`le> with a title.

By default, a file in `./migrations/` will be created with the following content:

```js
'use strict'

module.exports.up = function (next) {
  next()
}

module.exports.down = function (next) {
  next()
}
```

Let’s take an example of a `User` schema where we have a property `name` which includes both `first` and `last` name.

Now we want to change the schema to have a separate `last` name property.

So in order to automate this, we will read `name` at runtime and extract the last name and save it as new property.

Create a migration with this command:

```bash
$ migrate create add-last-name.js
```

This call will create `./migrations/{timestamp in milliseconds}-add-last-name.js` under the `migrations` folder in the root directory.

Let's write code for adding a last name to the schema and also for removing it.

#### Up Migration

We will find all the users where `lastName` property doesn’t exist and create a new property `lastName` in those documents.

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

#### Down Migration

Similarly, let’s write a function where we will remove `lastName`:

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

#### Running Migrations

Check out how migrations are executed here: [running migrations](https://github.com/tj/node-migrate#running-migrations).

### Writing Custom State Storage

By default, `migrate` stores the state of the migrations which have been run in a file (`.migrate`).

`.migrate` file will contain the following code:

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

But you can provide a custom storage engine if you would like to do something different, like storing them in your database of choice.

A storage engine has a simple interface of `load(fn)` and `save(set, fn)`.

As long as what goes in as `set` comes out the same on `load`, then you are good to go!

Let’s create file `db-migrate-store.js` in root directory of the project.

```js
const mongodb = require('mongodb')
const MongoClient = mongodb.MongoClient
const Bluebird = require('bluebird')

Bluebird.promisifyAll(MongoClient)
class dbStore {
   constructor () {
     this.url = 'mongodb://localhost/Sample' . // Manage this accordingly to your environment
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
        // Check if does not have required properties
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
            return fn(new Error('Invalid store file'))
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

`**load(fn)**` In this function we are just verifying if the existing migration document that has been loaded contains the `lastRun` property and `migrations` array.

`**save(set,fn)**` Here `set` is provided by library and we are updating the `lastRun` value and appending `migrations` to the existing array.

You might be wondering where the above file `db-migrate-store.js` is used. We are creating it because we want to store the state in the database, not in the code repository.

Below are test examples where you can see its usage.

### Automate migration testing

Install Mocha:

```bash
$ npm install -g mocha
```

> We installed this globally so we’ll be able to run `mocha` from the terminal.

#### Structure

To set up the basic tests, create a new folder called “test” in the project root, then within that folder add a folder called _migrations_.

Your file/folder structure should now look like this:

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
        └── create-test.js
        └── up-test.js 
        └── down-test.js
```

#### Test — Create Migration

**Goal:** It should create the migrations directory and file.

`$ migrate create add-last-name`

This will implicitly create file `./migrations/{timestamp in milliseconds}-add-last-name.js` under the `migrations` folder in the root directory.

Now add the following code to the `create-test.js` file:

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

In the above test, we are using the `migrate-init` command to create the migrations directory and deleting it after each test case using `rimraf` which is `rm -rf` in Unix.

Later we are using `fs.accessSync` function to verify `migrations` folder exists or not.

#### Test — Up Migration

**Goal:** It should add `lastName` to schema and store migration state.

Add the following code to the `up-test.js` file:

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

Similarly, you can write down migration and `before()` and `after()` functions remain basically the same.

### Conclusion

Hopefully you can now automate your schema changes with proper testing. :)

Grab the final code from [repository](https://github.com/thatshailesh/mongodb-migration).

_Don’t hesitate to clap if you considered this a worthwhile read!_

