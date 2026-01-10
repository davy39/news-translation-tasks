---
title: Comment construire une API GraphQL ultra-rapide avec Node.js, MongoDB et Fastify
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-23T15:47:45.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-blazing-fast-graphql-api-with-node-js-mongodb-and-fastify-77fd5acd2998
coverImage: https://cdn-media-1.freecodecamp.org/images/1*vUgaEEzxSp2YWsJ7p7jgjA.png
tags:
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment construire une API GraphQL ultra-rapide avec Node.js, MongoDB et
  Fastify
seo_desc: 'By Siegfried Grimbeek

  This tutorial is part two of a four part series, which aims to take you from scratch
  to deploying a fully functional full stack application.


  Part 1: How to build blazing fast REST APIs with Node.js, MongoDB, Fastify and Swagger...'
---

Par Siegfried Grimbeek

Ce tutoriel est la deuxième partie d'une série en quatre parties, qui vise à vous emmener de zéro au déploiement d'une application **full stack entièrement fonctionnelle**.

* Partie 1 : Comment construire des API REST ultra-rapides avec Node.js, MongoDB, Fastify et Swagger
* **Partie 2 : Comment construire une API GraphQL ultra-rapide avec Node.js, MongoDB, Fastify et GraphQL ! (Vous êtes ici.)**
* Partie 3 : Couplage de **Vue.js** avec une **API GraphQL**.
* Partie 4 : Déploiement d'une **API GraphQL** et d'une application frontend **Vue.js**.

La première partie de la série est disponible [ici](https://medium.freecodecamp.org/how-to-build-blazing-fast-rest-apis-with-node-js-mongodb-fastify-and-swagger-114e062db0c9) et le code source de l'application peut être trouvé [ici](https://github.com/siegfriedgrimbeek/fastify-graphql-api).

Dans cette partie, nous allons revisiter les **modèles**, **contrôleurs** et **routes** de la première partie, puis intégrer [**GraphQL**](https://graphql.org/) dans l'application. En bonus, nous allons également utiliser [**Faker.js**](https://github.com/marak/Faker.js/) pour créer des données fictives et alimenter **la base de données**.

### Introduction :

**GraphQL** est un langage de requête pour les API et un runtime pour exécuter ces requêtes avec vos données existantes.

Chaque requête **GraphQL** passe par trois phases : les requêtes sont analysées, validées et exécutées.

**GraphQL** fournit une description complète et compréhensible des données dans votre API, donne aux clients le pouvoir de demander exactement ce dont ils ont besoin, facilite l'évolution des API au fil du temps et permet des outils de développement puissants. [En savoir plus](https://graphql.org/).

%[https://youtu.be/T571423fC68]

### Prérequis…

Si vous avez terminé la première partie de cette série, vous devriez avoir des connaissances de base/intermédiaires en **JavaScript**, **Node.js, Fastify.JS** et **MongoDB (Mongoose)**.

Pour suivre ce tutoriel, vous devrez compléter la [première partie](https://medium.freecodecamp.org/how-to-build-blazing-fast-rest-apis-with-node-js-mongodb-fastify-and-swagger-114e062db0c9) de cette série ou récupérer le code depuis [Git](https://github.com/siegfriedgrimbeek/fastify-api), bien que je recommande vivement de parcourir au moins la [première partie](https://medium.freecodecamp.org/how-to-build-blazing-fast-rest-apis-with-node-js-mongodb-fastify-and-swagger-114e062db0c9).

### Commençons !

Clonez le dépôt pour la première partie (ignorez cette étape si vous avez suivi la première partie et que vous continuez avec votre propre code) en ouvrant votre **terminal**, en naviguant vers votre répertoire de projet et en exécutant chacune des lignes de code suivantes :

```bash
git clone https://github.com/siegfriedgrimbeek/fastify-api.git
cd fastify-api
```

Maintenant que nous avons une copie du code, nous allons [mettre à jour nos packages](https://www.npmjs.com/package/npm-check-updates) et le fichier `package.json` en exécutant le code suivant :

```bash
sudo npm i -g npm-check-updates
ncu -u
npm install
```

Tout d'abord, nous installons globalement le package [npm](https://docs.npmjs.com/about-npm/) « [**npm-check-updates**](https://www.npmjs.com/package/npm-check-updates) », puis nous utilisons ce package pour mettre à jour automatiquement notre fichier `package.json` avec les dernières versions des packages, et enfin nous installons/mettons à jour tous nos **modules npm** en exécutant `npm install`.

Cela est fait pour garantir que tous ceux qui suivent le tutoriel travaillent avec les mêmes versions de packages.

### Refactorisons notre serveur et démarrons l'application !

![Image](https://cdn-media-1.freecodecamp.org/images/svTzrRuMRcyj062XemIBJuZUZl95QoIdF2KL)

Comme pour toutes les solutions logicielles, à mesure que la solution grandit, les développeurs doivent souvent **revisiter** et [**refactoriser**](https://fr.wikipedia.org/wiki/Refactoring) le code.

Dans le répertoire `src`, nous allons créer un nouveau fichier appelé `server.js` :

```bash
cd src
touch server.js
```

Ajoutez le code suivant au fichier `server.js` :

```js
// Require the fastify framework and instantiate it
const fastify = require('fastify')({
	logger: true
})

// Require external modules
const mongoose = require('mongoose')

// Connect to DB
mongoose
	.connect('mongodb://localhost/mycargarage')
	.then(() => console.log('MongoDB connected...'))
	.catch(err => console.log(err))

module.exports = fastify
```

Nous avons maintenant extrait la logique qui démarre le **serveur** dans le fichier `server.js`, ce qui nous permet de réutiliser ce code dans tout le projet.

Ensuite, nous devons mettre à jour notre fichier `index.js` dans le répertoire `src` :

```js

// Import Server
const fastify = require('./server.js')

// Import Routes
const routes = require('./routes')

// Import Swagger Options
const swagger = require('./config/swagger')

// Register Swagger
fastify.register(require('fastify-swagger'), swagger.options)

// Loop over each route
routes.forEach((route, index) => {
	fastify.route(route)
})

// Run the server!
const start = async () => {
	try {
		await fastify.listen(3000, '0.0.0.0')
		fastify.swagger()
		fastify.log.info(`server listening on ${fastify.server.address().port}`)
	} catch (err) {
		fastify.log.error(err)
		process.exit(1)
	}
}
start()
```

Nous revisiterons le fichier `index.js` une fois que nous aurons configuré **GraphQL**.

Démarrez le serveur **Fastify** en exécutant le code suivant dans votre **terminal** :

```bash
npm start
```

Notez qu'il n'y a pas de route par défaut configurée, donc pour l'instant, naviguer vers [http://localhost:3000/](http://localhost:3000/) entraînera un retour du serveur avec une erreur 404, ce qui est correct.

### Démarrer MongoDB et mettre à jour les modèles

![Image](https://cdn-media-1.freecodecamp.org/images/qfSA-X4Bk-VbUgwx8mdQxWCdP2FD1gNTbFyd)

Étendons le modèle existant pour inclure également les **Services** et les **Propriétaires**. Le diagramme ci-dessous démontre les relations entre les collections :

![Image](https://cdn-media-1.freecodecamp.org/images/ScuP0r5uq0smEYWhcz75s2R-waOSiv7BVFLn)
_Modèles de données_

* Une voiture peut avoir un propriétaire.
* Un propriétaire peut avoir plusieurs voitures.
* Une voiture peut avoir plusieurs services.

Revisitez le fichier `Car.js` dans le répertoire `models` et mettez-le à jour comme suit :

```js
// External Dependancies
const mongoose = require("mongoose")
const ObjectId = mongoose.Schema.Types.ObjectId

const carSchema = new mongoose.Schema({
  title: String,
  brand: String,
  price: String,
  age: Number,
  owner_id: ObjectId
})

module.exports = mongoose.model("Car", carSchema)
```

Créez deux nouveaux fichiers dans le répertoire `models`, `Owner.js` et `Service.js`, et ajoutez le code suivant aux fichiers respectivement :

`Owner.js`

```js
// External Dependancies
const mongoose = require('mongoose')

const ownerSchema = new mongoose.Schema({
	firstName: String,
	lastName: String,
	email: String
})

module.exports = mongoose.model('Owner', ownerSchema)
```

`Service.js`

```js
// External Dependancies
const mongoose = require("mongoose")
const ObjectId = mongoose.Schema.Types.ObjectId

const serviceSchema = new mongoose.Schema({
  car_id: ObjectId,
  name: String,
  date: String
})

module.exports = mongoose.model("Service", serviceSchema)
view rawService.js hosted with F496 by GitHub
```

Il n'y a pas de nouveaux concepts utilisés dans le code ci-dessus. Nous avons simplement créé des [Schémas Mongoose](https://mongoosejs.com/docs/guide.html) standards, comme pour le modèle `Car.js`.

### Revisiter le contrôleur de voiture et créer les contrôleurs supplémentaires

Il y a quelques légères modifications dans le `carController.js`, donc naviguez vers le répertoire `controllers` et mettez à jour votre fichier comme suit :

```js
// External Dependancies
const boom = require('boom')

// Get Data Models
const Car = require('../models/Car')

// Get all cars
exports.getCars = async () => {
	try {
		const cars = await Car.find()
		return cars
	} catch (err) {
		throw boom.boomify(err)
	}
}

// Get single car by ID
exports.getSingleCar = async req => {
	try {
		const id = req.params === undefined ? req.id : req.params.id
		const car = await Car.findById(id)
		return car
	} catch (err) {
		throw boom.boomify(err)
	}
}

// Add a new car
exports.addCar = async req => {
	try {
		const car = new Car(req)
		const newCar = await car.save()
		return newCar
	} catch (err) {
		throw boom.boomify(err)
	}
}

// Update an existing car
exports.updateCar = async req => {
	try {
		const id = req.params === undefined ? req.id : req.params.id
		const updateData = req.params === undefined ? req : req.params
		const update = await Car.findByIdAndUpdate(id, updateData, { new: true })
		return update
	} catch (err) {
		throw boom.boomify(err)
	}
}

// Delete a car
exports.deleteCar = async req => {
	try {
		const id = req.params === undefined ? req.id : req.params.id
		const car = await Car.findByIdAndRemove(id)
		return car
	} catch (err) {
		throw boom.boomify(err)
	}
}
```

Créez deux nouveaux fichiers dans le répertoire `controllers`, `serviceController.js` et `ownerController.js`, et ajoutez le code suivant aux fichiers respectivement :

`serviceController.js`

```js
// External Dependancies
const boom = require('boom')

// Get Data Models
const Service = require('../models/Service')

// Get single service ID
exports.getSingleService = async req => {
	try {
		const id = req.params === undefined ? req.id : req.params.id
		const service = await Service.findById(id)
		return service
	} catch (err) {
		throw boom.boomify(err)
	}
}

// Get single car's services
exports.getCarsServices = async req => {
	try {
		const id = req.params === undefined ? req.id : req.params.id
		const services = await Service.find({ car_id: id })
		return services
	} catch (err) {
		throw boom.boomify(err)
	}
}
```

`ownerController.js`

```js
// External Dependancies
const boom = require('boom')

// Get Data Models
const Owner = require('../models/Owner')
const Car = require('../models/Car')

// Get all owners
exports.getOwner = async () => {
	try {
		const owners = await Owner.find()
		return owners
	} catch (err) {
		throw boom.boomify(err)
	}
}

// Get single owner by ID
exports.getSingleOwner = async req => {
	try {
		const id = req.params === undefined ? req.id : req.params.id
		const owner = await Owner.findById(id)
		return owner
	} catch (err) {
		throw boom.boomify(err)
	}
}

// Get single owner's cars
exports.getOwnersCars = async req => {
	try {
		const id = req.params === undefined ? req.id : req.params.id
		const cars = await Car.find({ owner_id: id })
		return cars
	} catch (err) {
		throw boom.boomify(err)
	}
}
```

Le plus grand changement dans les contrôleurs est la manière dont nous obtenons les paramètres :

```js
const id = req.params === undefined ? req.id : req.params.id
const updateData = req.params === undefined ? req : req.params
```

Le code ci-dessus est appelé un « [**opérateur conditionnel (ternaire)**](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Operators/Conditional_Operator) » et est utilisé comme raccourci pour l'instruction if suivante :

```js
let id

if (req.params === undefined) {

id = req.id

} else {

id = req.params.id

}
```

Nous utilisons l'**opérateur ternaire** pour accommoder les requêtes provenant à la fois de l'**API REST** et de l'**API GraphQL**, car elles ont une implémentation légèrement différente.

### Il est temps d'alimenter la base de données avec des données fictives !

![Image](https://cdn-media-1.freecodecamp.org/images/XzVSE6N-ig-vdYK9FxnvuuZGv6Dvg0zH9gmJ)

Dans le répertoire `src`, créons un nouveau répertoire et un fichier en exécutant le code suivant :

```js
mkdir helpers
touch seed.js
```

Ajoutez le code suivant au fichier `seed.js` :

```js

// Import external dependancies
const faker = require('faker')
const boom = require('boom')

// Import internal dependancies
const fastify = require('../server.js')

// Fake data
const cars = [
	{
		name: 'Tesla',
		models: ['S', 'E', 'X', 'Y']
	},
	{
		name: 'Mercedes',
		models: ['GLA', 'GLC', 'GLE', 'GLS']
	},
	{
		name: 'BMW',
		models: ['X4', 'Z3', 'M2', '7']
	},
	{
		name: 'Audi',
		models: ['A1', 'A3', 'A4', 'A5']
	},
	{
		name: 'Ford',
		models: ['Fiesta', 'Focus', 'Fusion', 'Mustang']
	}
]
const serviceGarages = ['A++ Auto Services', "Gary's Garage", 'Super Service', 'iGarage', 'Best Service']

// Get Data Models
const Car = require('../models/Car')
const Owner = require('../models/Owner')
const Service = require('../models/Service')

// Fake data generation functions
const generateOwnerData = () => {
	let ownerData = []
	let i = 0

	while (i < 50) {
		const firstName = faker.fake('{{name.firstName}}')
		const lastName = faker.fake('{{name.lastName}}')
		const email = faker.fake(`${firstName.toLowerCase()}.${lastName.toLowerCase()}@gmail.com`)

		const owner = {
			firstName,
			lastName,
			email
		}

		ownerData.push(owner)
		i++
	}

	return ownerData
}

const generateCarData = ownersIds => {
	let carData = []
	let i = 0

	while (i < 1000) {
		const owner_id = faker.random.arrayElement(ownersIds)
		const carObject = faker.random.arrayElement(cars)
		const title = faker.random.arrayElement(carObject.models)
		const price = faker.random.number({ min: 5000, max: 30000 })
		const age = faker.random.number({ min: 2, max: 10 })

		const car = {
			owner_id,
			brand: carObject.name,
			title,
			price,
			age
		}

		carData.push(car)
		i++
	}

	return carData
}

const generateServiceData = carsIds => {
	let serviceData = []
	let i = 0

	while (i < 5000) {
		const car_id = faker.random.arrayElement(carsIds)
		const name = faker.random.arrayElement(serviceGarages)
		const date = faker.fake('{{date.past}}')

		const service = {
			car_id,
			name,
			date
		}

		serviceData.push(service)
		i++
	}

	return serviceData
}

fastify.ready().then(
	async () => {
		try {
			const owners = await Owner.insertMany(generateOwnerData())
			const ownersIds = owners.map(x => x._id)

			const cars = await Car.insertMany(generateCarData(ownersIds))
			const carsIds = cars.map(x => x._id)

			const services = await Service.insertMany(generateServiceData(carsIds))

			console.log(`
      Data successfully added:
        - ${owners.length} owners added.
        - ${cars.length} cars added.
        - ${services.length} services added.
      `)
		} catch (err) {
			throw boom.boomify(err)
		}
		process.exit()
	},
	err => {
		console.log('An error occured: ', err)
		process.exit()
	}
)
```

Décortiquons ce code :

Tout d'abord, nous importons deux bibliothèques externes, [**Faker.js**](https://github.com/marak/Faker.js/) qui est utilisé pour générer des données fictives et [**Boom**](https://github.com/hapijs/boom), qui est utilisé pour lancer des objets d'erreur compatibles http.

Ensuite, nous importons le fichier `server.js` qui va démarrer une instance de notre serveur, nous permettant d'interagir avec les **modèles**.

Nous déclarons ensuite deux tableaux avec des données fictives, `cars` et `serviceGarages`.

Puis nous importons les `modèles` et déclarons trois fonctions (`generateOwnerData`, `generateCarData`, `generateServiceData`) qui retournent chacune un tableau d'objets avec les données **propriétaire**, **voiture** et **service** respectivement.

Une fois que l'instance **Fastify.js** est prête, nous utilisons la fonction [**Mongoose** `insertMany()`](https://mongoosejs.com/docs/api.html#model_Model.insertMany) pour insérer les tableaux générés dans la base de données. La fonction retourne ensuite un tableau d'objets contenant les données d'objet originales et les `ids` de chaque enregistrement.

Nous utilisons la fonction [**JavaScript Map**](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/Array/map) pour créer un tableau d'`ids` des tableaux **propriétaires** et **voitures**. Nous utilisons le tableau `ownersIDs` lors de la génération des données de voiture et nous utilisons le tableau `carsIds` lors de la génération des données de service, ils sont passés dans les fonctions respectives et des valeurs sont sélectionnées aléatoirement parmi eux.

Enfin, nous devons installer le package **Faker.js** et ajouter la tâche de seed à notre fichier `package.json`.

Nous pouvons ajouter le package **Faker.js** en naviguant vers le **répertoire racine** et en exécutant le code suivant :

```bash
npm i faker -D
```

Nous ajoutons ensuite ce qui suit au fichier `package.json` :

```json
...

"scripts": {

...

"seed": "node ./src/helpers/seed.js"

},

...
```

C'est tout ! Nous pouvons maintenant exécuter notre script de seed depuis le répertoire racine du projet avec le code suivant :

```bash
npm run seed
```

Si vous utilisez [MongoDB Compass](https://www.mongodb.com/products/compass) (vous devriez), vous verrez les données dans votre base de données :

![Image](https://cdn-media-1.freecodecamp.org/images/hLUq7STJYtprAMW0fDIVlAj3s-u4FulWVUlZ)
_Base de données « mycargarage » vue dans MongoDB Compass_

### Installation, configuration et test de GraphQL

![Image](https://cdn-media-1.freecodecamp.org/images/tPZMxs0WHzOis6DPoX-T6Jo3RhAlLeBFXYR-)

Commençons par naviguer vers le **répertoire racine** et exécuter le code suivant :

```bash
npm i fastify-gql graphql
```

Cela installe **GraphQL** et l'adaptateur **Fastify barebone GraphQL**.

Naviguez vers le répertoire `src` et exécutez le code suivant :

```bash
mkdir schema
cd schema
touch index.js
```

Naviguez vers le répertoire `src` et mettez à jour le fichier `index.js` avec ce qui suit :

```js
// Import Server
const fastify = require('./server.js')

// Import external dependancies
const gql = require('fastify-gql')

// Import GraphQL Schema
const schema = require('./schema')

// Register Fastify GraphQL
fastify.register(gql, {
   schema,
   graphiql: true
})

... end here

// Import Routes
const routes = require('./routes')
```

Avec le code ci-dessus, nous requérons l'**Adaptateur Fastify GraphQL**, importons le **schéma** et enregistrons l'**Adaptateur GraphQL** avec **Fastify**.

Nous enregistrons le **schéma** et activons **GraphiQL**, un **IDE** intégré au navigateur pour explorer **GraphQL**.

Naviguez vers le répertoire `schema` et ouvrez le fichier `index.js` et ajoutez le code suivant :

```js
// Import External Dependancies
const graphql = require('graphql')

// Destructure GraphQL functions
const {
	GraphQLSchema,
	GraphQLObjectType,
	GraphQLString,
	GraphQLInt,
	GraphQLID,
	GraphQLList,
	GraphQLNonNull
} = graphql

// Import Controllers
const carController = require('../controllers/carController')
const ownerController = require('../controllers/ownerController')
const serviceController = require('../controllers/serviceController')

// Define Object Types
const carType = new GraphQLObjectType({
	name: 'Car',
	fields: () => ({})
})

const ownerType = new GraphQLObjectType({
	name: 'Owner',
	fields: () => ({})
})

const serviceType = new GraphQLObjectType({
	name: 'Service',
	fields: () => ({})
})

// Define Root Query
const RootQuery = new GraphQLObjectType({
	name: 'RootQueryType',
	fields: {
		car: {},
		cars: {},
		owner: {},
		service: {}
	}
})

// Define Mutations
const Mutations = new GraphQLObjectType({
	name: 'Mutations',
	fields: {
		addCar: {
			type: carType,
			args: {},
			async resolve(args) {
				return ''
			}
		},
		editCar: {
			type: carType,
			args: {},
			async resolve(args) {
				return ''
			}
		},
		deleteCar: {
			type: carType,
			args: {},
			async resolve(args) {
				return ''
			}
		}
	}
})

// Export the schema
module.exports = new GraphQLSchema({
	query: RootQuery,
	mutation: Mutations
})
```

Passons en revue le code ci-dessus :

Nous requérons le package principal **GraphQL** et utilisons la [Destructuration JavaScript](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment) pour obtenir les fonctions **GraphQL** nécessaires (`GraphQLSchema`, `GraphQLObjectType`, `GraphQLString`, `GraphQLInt`, `GraphQLID`, `GraphQLList` et `GraphQLNonNull`).

Nous importons nos trois `contrôleurs` (`carController`, `ownerController` et `serviceController`).

Nous déclarons les `carType`, `ownerType` et `serviceType` [**Types d'objets GraphQL**](https://graphql.org/graphql-js/object-types/), qui sont des fonctions acceptant un objet comme paramètre, avec une clé `name` et une clé `fields`.

Ces fonctions sont utilisées pour définir notre **schéma GraphQL**, similaire aux **modèles Mongoose** définis précédemment.

Les champs peuvent retourner un **type** particulier, et des **méthodes** qui prennent des arguments. [En savoir plus sur les Types d'objets](https://graphql.org/graphql-js/object-types/).

Ensuite, nous déclarons le `RootQuery` qui est également un **Type d'objet GraphQL** et se trouve au niveau supérieur de chaque serveur **GraphQL**. Il représente tous les points d'entrée possibles dans l'**API GraphQL**. [En savoir plus sur les champs racine et les résolveurs](https://graphql.org/learn/execution/).

Nous déclarons ensuite nos `Mutations`, qui sont utilisées pour **changer les données**. Bien que toute requête pourrait être implémentée pour changer les données, les opérations qui provoquent des changements doivent être envoyées explicitement **via une mutation**. [En savoir plus sur les Mutations](https://graphql.org/learn/queries/#mutations).

Enfin, nous exportons le `GraphQLSchema`.

Maintenant que nous avons notre modèle configuré, nous pouvons commencer à remplir les **Types d'objets**, **Root Query** et **Mutations**.

Notez qu'il existe des générateurs de schéma [Mongoose vers GraphQL](https://github.com/sarkistlt/mongoose-schema-to-graphql), mais pour les besoins du tutoriel, nous créerons manuellement le schéma.

Mettons à jour le **Type d'objet** `carType` comme suit :

```js
const carType = new GraphQLObjectType({
	name: 'Car',
	fields: () => ({
		_id: { type: GraphQLID },
		title: { type: GraphQLString },
		brand: { type: GraphQLString },
		price: { type: GraphQLString },
		age: { type: GraphQLInt },
		owner_id: { type: GraphQLID },
		owner: {
			type: ownerType,
			async resolve(parent, args) {
				return await ownerController.getSingleOwner({ id: parent.owner_id })
			}
		},
		services: {
			type: new GraphQLList(serviceType),
			async resolve(parent, args) {
				return await serviceController.getCarsServices({ id: parent._id })
			}
		}
	})
})
```

Approfondissons les fonctions **GraphQL**, en commençant par les types [Scalars](https://softwareengineering.stackexchange.com/questions/238033/what-does-it-mean-when-data-is-scalar) dans **GraphQL** :

**GraphQL** vient avec un ensemble de types scalaires par défaut :

* `Int` : Un entier signé sur 32 bits. `GraphQLInt`
* `Float` : Une valeur flottante double précision signée. `GraphQLFloat`
* `String` : Une séquence de caractères UTF-8. `GraphQLString`
* `Boolean` : `true` ou `false`. `GraphQLBoolean`
* `ID` : Le type scalaire ID représente un identifiant unique, souvent utilisé pour réinterroger un objet ou comme clé pour un cache. Le type ID est sérialisé de la même manière qu'une String ; cependant, le définir comme un `ID` signifie qu'il n'est pas destiné à être lisible par l'homme. `GraphQLID`

Les champs `owner` et `service` sont là où cela devient intéressant. Ces champs ne sont pas définis comme des **types scalaires** comme les autres — au lieu de cela, leur `type` fait référence au `ownerType` et `serviceType` que nous avons créés et que nous devons encore remplir.

Le deuxième argument que nous passons aux champs `owner` et `service` sont des fonctions [résolveurs](https://graphql.org/learn/execution/).

Les fonctions ou méthodes résolveurs sont des fonctions qui **résolvent une valeur** pour un type ou un champ dans un schéma.

Les résolveurs peuvent également être asynchrones ! Ils peuvent résoudre des valeurs à partir d'une autre **API REST, base de données, cache, constante, etc.**

> Vous pouvez considérer chaque champ dans une requête GraphQL comme une fonction ou une méthode du type précédent qui retourne le type suivant. En fait, c'est exactement ainsi que fonctionne GraphQL. Chaque champ de chaque type est soutenu par une fonction appelée le _résolveur_ qui est fournie par le développeur du serveur GraphQL. Lorsqu'un champ est exécuté, le _résolveur_ correspondant est appelé pour produire la valeur suivante.  
>   
> Si un champ produit une valeur scalaire comme une chaîne ou un nombre, alors l'exécution est terminée. Cependant, si un champ produit une valeur d'objet, alors la requête contiendra une autre sélection de champs qui s'appliquent à cet objet. Cela continue jusqu'à ce que des valeurs scalaires soient atteintes. Les requêtes GraphQL se terminent toujours par des valeurs scalaires.

Afin de créer la relation entre les différents types, nous passons les valeurs `_id` et `owner_id` dans les fonctions de contrôleur respectives.

Ainsi, nous demandons essentiellement les détails du propriétaire ainsi que les détails de la voiture :

```js
return await userController.getSingleOwner({ id: parent.owner_id })
```

et les détails de tous les services liés à la voiture :

```js
return await serviceController.getCarsServices({ id: parent._id })
```

Pour retourner une liste ou un tableau avec **GraphQL**, nous utilisons `GraphQLList`. [Voici](https://graphqlmastery.com/blog/graphql-list-how-to-use-arrays-in-graphql-schema) un excellent tutoriel approfondi sur l'utilisation des tableaux dans le schéma **GraphQL**, mais c'est vraiment simple : chaque fois que nous avons besoin d'un tableau, nous utiliserons la fonction `GraphQLList`.

Mettons à jour le `ownerType` et le `serviceType` avec le code suivant :

`ownerType`

```js
const ownerType = new GraphQLObjectType({
	name: 'Owner',
	fields: () => ({
		_id: { type: GraphQLID },
		firstName: { type: GraphQLString },
		lastName: { type: GraphQLString },
		email: { type: GraphQLString },
		cars: {
			type: new GraphQLList(carType),
			async resolve(parent, args) {
				return await ownerController.getOwnersCars({ id: parent._id })
			}
		}
	})
})
```

`serviceType`

```js
const serviceType = new GraphQLObjectType({
	name: 'Service',
	fields: () => ({
		_id: { type: GraphQLID },
		car_id: { type: GraphQLID },
		name: { type: GraphQLString },
		date: { type: GraphQLString },
		car: {
			type: carType,
			async resolve(parent, args) {
				return await carController.getSingleCar({ id: parent.car_id })
			}
		}
	})
})
```

Les deux **Types d'objets** ci-dessus sont très similaires au `carType`. Vous pouvez remarquer un motif entre les différents **Types d'objets** et leurs relations.

Nous pouvons maintenant remplir le `RootQuery` avec le code suivant :

```js
const RootQuery = new GraphQLObjectType({
	name: 'RootQueryType',
	fields: {
		car: {
			type: carType,
			args: { id: { type: GraphQLID } },
			async resolve(parent, args) {
				return await carController.getSingleCar(args)
			}
		},
		cars: {
			type: new GraphQLList(carType),
			async resolve(parent, args) {
				return await carController.getCars()
			}
		},
		owner: {
			type: ownerType,
			args: { id: { type: GraphQLID } },
			async resolve(parent, args) {
				return await ownerController.getSingleOwner(args)
			}
		},
		service: {
			type: serviceType,
			args: { id: { type: GraphQLID } },
			async resolve(parent, args) {
				return await serviceController.getSingleService(args)
			}
		}
	}
})
```

Il n'y a pas de nouveaux concepts dans le code ci-dessus, mais gardez à l'esprit que la requête `RootQuery` est le point d'entrée de toutes les requêtes sur l'**API GraphQL**. Ainsi, à partir de ce qui précède, nous pouvons voir que nous pouvons exécuter les requêtes suivantes directement :

* Obtenir toutes les voitures
* Obtenir une seule voiture
* Obtenir un seul propriétaire
* Obtenir un seul service

Ouvrons l'interface utilisateur **GraphiQL** et construisons quelques requêtes : [http://localhost:3000/graphiql.html](http://localhost:3000/graphiql.html)

![Image](https://cdn-media-1.freecodecamp.org/images/uu6PQdqiUejeUuFsO1KdXl2v7PYpF6KsOGOJ)

Les requêtes sont saisies à gauche, les résultats sont au centre et l'explorateur de documentation est à droite.

L'explorateur de documentation peut être utilisé pour explorer l'ensemble du graphe jusqu'au niveau Scalaire. Cela est très utile lors de la construction de requêtes.

Le langage utilisé pour construire les requêtes ressemble à JSON. Cette [feuille de triche](https://devhints.io/graphql) est une excellente référence.

Voici pourquoi **GraphQL** est si génial :

![Image](https://cdn-media-1.freecodecamp.org/images/vCpUlnX-63eB2nXol3wNb7bb7MpNkUz8jFXm)
_IDE GraphiQL_

Dans l'exemple ci-dessus, nous utilisons la requête racine `cars` pour afficher une liste de toutes les voitures, leurs propriétaires et leurs services.

![Image](https://cdn-media-1.freecodecamp.org/images/5-b6eyxOlNA5SsgL89U85EkJXmr6IRMCpLtT)
_Obtenir une seule voiture — requête racine car_

![Image](https://cdn-media-1.freecodecamp.org/images/zvztPdLyGRN-Sha3ZkZ9QhyjGRrZjC2dhfyw)
_Obtenir un seul propriétaire — requête racine owner_

![Image](https://cdn-media-1.freecodecamp.org/images/sX3N-8B8PUkpqlWpOwLBFCAymL3U8A7pHHtS)
_Obtenir un seul service — requête racine service_

Il nous reste un dernier sujet à aborder, celui des `mutations`. Mettons à jour les `mutations` avec le code suivant :

```js
const Mutations = new GraphQLObjectType({
	name: 'Mutations',
	fields: {
		addCar: {
			type: carType,
			args: {
				title: { type: new GraphQLNonNull(GraphQLString) },
				brand: { type: new GraphQLNonNull(GraphQLString) },
				price: { type: GraphQLString },
				age: { type: GraphQLInt },
				owner_id: { type: GraphQLID }
			},
			async resolve(parent, args) {
				const data = await carController.addCar(args)
				return data
			}
		},
		editCar: {
			type: carType,
			args: {
				id: { type: new GraphQLNonNull(GraphQLID) },
				title: { type: new GraphQLNonNull(GraphQLString) },
				brand: { type: new GraphQLNonNull(GraphQLString) },
				price: { type: new GraphQLNonNull(GraphQLString) },
				age: { type: new GraphQLNonNull(GraphQLInt) },
				owner_id: { type: GraphQLID }
			},
			async resolve(parent, args) {
				const data = await carController.updateCar(args)
				return data
			}
		},
		deleteCar: {
			type: carType,
			args: {
				id: { type: new GraphQLNonNull(GraphQLID) }
			},
			async resolve(parent, args) {
				const data = await carController.deleteCar(args)
				return data
			}
		}
	}
})
```

Comme avant, nous déclarons notre **Type d'objet**, spécifions le **nom** et les **champs**.

Une mutation se compose du **type**, des **args** et de la fonction **async resolve**. La fonction **resolve** passe les args au contrôleur, qui retourne le résultat de la mutation.

![Image](https://cdn-media-1.freecodecamp.org/images/tYpE1tGBixN4mxO8kfdXer-MXBXDqDPHNjdQ)
_Mutation addCar_

![Image](https://cdn-media-1.freecodecamp.org/images/i57zXGAVZ1qVKIv69sNLSXJs4H351cx7mB9j)
_Mutation editCar_

![Image](https://cdn-media-1.freecodecamp.org/images/MZW4-sSHxitchUGDZQUUEAZ-xMH-8BqnXzVa)
_Mutation deleteCar_

Vous avez maintenant codé une **API REST** entièrement fonctionnelle et une **API GraphQL** entièrement fonctionnelle.

Il n'y a pas de règles stipulant qu'il faut utiliser exclusivement **REST** ou exclusivement **GraphQL**. Dans certains projets, la meilleure solution peut être un mélange des deux. Cela se détermine vraiment au cas par cas.

Vous pouvez télécharger le code source depuis Git [ici](https://github.com/siegfriedgrimbeek/fastify-graphql-api).

#### Qu'est-ce qui suit ?

Dans le prochain tutoriel, nous allons consommer notre **API GraphQL** avec un frontend **Vue.js** en tant qu'application monopage !