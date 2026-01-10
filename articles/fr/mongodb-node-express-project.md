---
title: Apprendre Node + MongoDB en créant un projet de raccourcisseur d'URL
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-18T21:47:03.000Z'
originalURL: https://freecodecamp.org/news/mongodb-node-express-project
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/urlshortener.jpg
tags:
- name: MongoDB
  slug: mongodb
- name: node
  slug: node
- name: projects
  slug: projects
seo_title: Apprendre Node + MongoDB en créant un projet de raccourcisseur d'URL
seo_desc: 'By Mehul Mohan

  If you want to learn about something, what better way than by building a project
  around the thing you want to learn?

  In this blog post, we''ll learn about MongoDB, Mongoose, Node, and other tech by
  building a simple URL shortener applic...'
---

Par Mehul Mohan

Si vous voulez apprendre quelque chose, quelle meilleure façon que de construire un projet autour de la chose que vous voulez apprendre ?

Dans cet article de blog, nous allons apprendre MongoDB, Mongoose, Node et d'autres technologies en construisant une application simple de raccourcisseur d'URL. 

Les raccourcisseurs d'URL sont partout, des liens que vous partagez sur Twitter aux services populaires comme bit.ly. Mais avez-vous déjà pensé à créer un raccourcisseur d'URL rapide pour vous-même ?

Nous allons donc passer par la pratique concrète de la construction d'un raccourcisseur d'URL avec MongoDB comme solution backend. Ce projet vous donnera confiance dans vos connaissances et consolidera chaque concept que vous apprenez. Commençons.

## Introduction au projet

Nous utiliserons cette salle de classe gratuite sur le [raccourcisseur d'URL](https://codedamn.com/practice/url-shortener-node) de codedamn pour obtenir une pratique concrète et évaluer nos progrès au fur et à mesure.

Nous utiliserons les technologies suivantes :

* Mongoose comme ORM
* MongoDB comme base de données backend
* Node.js comme backend
* Un simple fichier JS intégré comme frontend

Nous terminerons ce projet en 7 étapes, qui vous guideront du début à la fin. Commençons les labs maintenant.

## Partie 1 : Configuration du serveur Express

Commençons par configurer notre serveur Node. Nous utiliserons Express comme framework pour cette partie car il est facile à utiliser. Voici le [lien vers cette partie](https://codedamn.com/practice/url-shortener-node/36280bc2-36b5-4f4e-8976-ed4687dc7cbd).

Nous pouvons voir que c'est un exercice raisonnablement facile. Les deux seuls défis que nous devons surmonter sont les suivants :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/i1.png)

La solution pourrait ressembler à ceci :

```js
// Initialiser le serveur express sur le PORT 1337
const express = require('express')
const app = express()

app.get('/', (req, res) => {
	res.send('Hello World! - from codedamn')
})

app.get('/short', (req, res) => {
	res.send('Hello from short')
})

app.listen(process.env.PUBLIC_PORT, () => {
	console.log('Server started')
})
```

Simple et facile. Nous créons une autre route GET en utilisant `app.get`, et cela devrait faire le travail.

## Partie 2 : Configuration de notre moteur de vue

Maintenant que nous sommes familiers avec l'installation d'Express, jetons un coup d'œil au modèle `.ejs` que nous avons. Voici le [lien vers cette partie](https://codedamn.com/practice/url-shortener-node/0eb7b0b0-473e-4a83-9589-8ea13467972f).

Le moteur EJS vous permet de passer des variables avec le code Node.js à votre HTML et de les itérer ou de les afficher avant d'envoyer une réponse réelle au serveur. 

Jetez un rapide coup d'œil au fichier `views/index.ejs`. Il ressemblera à un fichier HTML régulier, sauf que vous pouvez utiliser des variables. 

Voici notre fichier `index.js` actuel :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/i2.png)

Maintenant, vous pouvez voir que dans le fichier `index.js`, nous avons la ligne `app.set('view engine', 'ejs')`. Elle indique à Express d'utiliser `ejs` comme moteur de modélisation par défaut.

Enfin, voyez que nous utilisons res.render et que nous ne passons que le nom du fichier, et non le chemin complet. Cela est dû au fait qu'Express recherchera automatiquement dans le dossier views les modèles `.ejs` disponibles. 

Nous passons les variables comme deuxième argument, que nous pouvons ensuite accéder dans le fichier EJS. Nous utiliserons ce fichier plus tard, mais pour l'instant, passons par un rapide défi.

Pour compléter ce défi, nous devons simplement changer le nom de `Mehul` en autre chose. 

Pour réussir ce défi, consultez d'abord le fichier `index.ejs`, puis mettez à jour votre nom en autre chose que vous aimez. Voici une bonne solution :

```js
const express = require('express')
const app = express()

app.set('view engine', 'ejs')

app.get('/', (req, res) => {
	res.render('index', { myVariable: 'My name is John!' })
})

app.listen(process.env.PUBLIC_PORT, () => {
	console.log('Server started')
})
```

## Partie 3 : Configuration de MongoDB

Maintenant que nous avons une certaine compréhension du frontend et du backend, passons à la configuration de MongoDB. Voici le [lien vers cette partie](https://codedamn.com/practice/url-shortener-node/523eaae7-27ff-47fe-bfdc-67a65dfd5711).

Nous utiliserons Mongoose pour nous connecter à MongoDB. Mongoose est un ORM pour MongoDB. 

En termes simples, MongoDB est une base de données très _flexible_, et elle permet toutes sortes d'opérations sur n'importe quoi. 

Bien que ce soit bon pour les données non structurées, la plupart du temps nous savons en fait à quoi ressembleront les données (comme les enregistrements utilisateurs ou les enregistrements de paiement). Ainsi, nous pouvons définir un _schéma_ pour MongoDB en utilisant Mongoose. Cela facilite beaucoup de fonctions pour nous.

Par exemple, une fois que nous avons un schéma, nous pouvons être assurés que la validation des données et toutes les vérifications nécessaires seront gérées automatiquement par Mongoose. Mongoose nous donne également un ensemble de fonctions d'assistance pour faciliter notre travail. Configurons-le maintenant.

Pour compléter cette partie, nous devons prendre en compte les points suivants :

* Le package NPM Mongoose a déjà été installé pour vous. Vous pouvez directement le `require`.
* Connectez-vous à l'URL `mongodb://localhost:27017/codedamn` en utilisant la méthode `mongoose.connect`.

Voici notre fichier index.js actuel :

```js
const express = require('express')
const app = express()
const mongoose = require('mongoose')

app.set('view engine', 'ejs')

app.get('/', (req, res) => {
	res.render('index')
})

app.post('/short', (req, res) => {
	const db = mongoose.connection.db
	// insert the record in 'test' collection

	res.json({ ok: 1 })
})

// Setup your mongodb connection here
// mongoose.connect(...)

// Wait for mongodb connection before server starts
app.listen(process.env.PUBLIC_PORT, () => {
	console.log('Server started')
})

```

Remplissons les espaces réservés appropriés avec le code pertinent :

```js
const express = require('express')
const app = express()
const mongoose = require('mongoose')

app.set('view engine', 'ejs')

app.get('/', (req, res) => {
	res.render('index')
})

app.post('/short', (req, res) => {
	const db = mongoose.connection.db
	// insert the record in 'test' collection
	db.collection('test').insertOne({ testCompleted: 1 })

	res.json({ ok: 1 })
})

// Setup your mongodb connection here
mongoose.connect('mongodb://localhost/codedamn', {
	useNewUrlParser: true,
	useUnifiedTopology: true
})
mongoose.connection.on('open', () => {
	// Wait for mongodb connection before server starts
	app.listen(process.env.PUBLIC_PORT, () => {
		console.log('Server started')
	})
})
```

Remarquez comment nous démarrons notre serveur HTTP uniquement lorsque notre connexion avec MongoDB est ouverte. C'est bien car nous ne voulons pas que les utilisateurs accèdent à nos routes avant que notre base de données soit prête.

Nous utilisons enfin la méthode `db.collection` ici pour insérer un simple enregistrement, mais nous aurons bientôt une meilleure façon d'interagir avec la base de données en utilisant les modèles Mongoose.

## Partie 4 : Configuration d'un schéma Mongoose

Maintenant que nous avons eu une expérience pratique avec l'implémentation de MongoDB dans la dernière section, dessinons le schéma pour notre raccourcisseur d'URL. Voici le [lien pour cette partie](https://codedamn.com/practice/url-shortener-node/a64e6946-a6ea-4ba7-8357-fe000c61658c).

Un schéma Mongoose nous permet d'interagir avec les collections Mongo de manière abstraite. Les documents riches de Mongoose exposent également des fonctions d'assistance comme `.save` qui sont suffisantes pour effectuer une requête DB complète afin de mettre à jour les modifications dans votre document.

Voici à quoi ressemblera notre schéma pour le raccourcisseur d'URL :

```js
const mongoose = require('mongoose')
const shortId = require('shortid')

const shortUrlSchema = new mongoose.Schema({
  full: {
    type: String,
    required: true
  },
  short: {
    type: String,
    required: true,
    default: shortId.generate
  },
  clicks: {
    type: Number,
    required: true,
    default: 0
  }
})

module.exports = mongoose.model('ShortUrl', shortUrlSchema)
```

Nous stockerons ce fichier dans le fichier `models/url.js`. Une fois que nous avons le schéma, nous pouvons passer cette partie de l'exercice. Nous devons faire les deux choses suivantes :

1. Créer ce modèle dans le fichier `models/url.js`. (Nous l'avons fait.)
2. Une requête POST à `/short` devrait ajouter quelque chose à la base de données à ce modèle.

Pour ce faire, nous pouvons générer un nouvel enregistrement en utilisant le code suivant :

```js
app.post('/short', async (req, res) => {
	// insert the record using the model
	const record = new ShortURL({
		full: 'test'
	})
	await record.save()
	res.json({ ok: 1 })
})
```

Vous verrez que nous pouvons omettre les champs `clicks` et `short` car ils ont déjà une valeur par défaut dans le schéma. Cela signifie que Mongoose les remplira automatiquement lorsque la requête s'exécutera.

Notre fichier `index.js` final pour passer ce défi devrait ressembler à ceci :

```
const express = require('express')
const app = express()
const mongoose = require('mongoose')
// import the model here
const ShortURL = require('./models/url')

app.set('view engine', 'ejs')

app.get('/', (req, res) => {
	res.render('index', { myVariable: 'My name is John!' })
})

app.post('/short', async (req, res) => {
	// insert the record using the model
	const record = new ShortURL({
		full: 'test'
	})
	await record.save()
	res.json({ ok: 1 })
})

// Setup your mongodb connection here
mongoose.connect('mongodb://localhost/codedamn')

mongoose.connection.on('open', () => {
	// Wait for mongodb connection before server starts
	app.listen(process.env.PUBLIC_PORT, () => {
		console.log('Server started')
	})
})
```

## Partie 5 : Lier le frontend, le backend et MongoDB

Maintenant que nous avons une bonne compréhension de la partie backend, revenons au frontend et configurons notre page web. Là, nous pouvons utiliser le bouton **Shrink** pour ajouter des enregistrements à la base de données. Voici le lien vers [cette partie](https://codedamn.com/practice/url-shortener-node/bfd9d2d7-e925-4ade-9d4b-f9e23124cc07).

Si vous regardez à l'intérieur du fichier `views/index.ejs`, vous verrez que nous avons déjà passé les données du formulaire sur la route backend `/short`. Mais pour l'instant, nous ne les récupérons pas.

* Vous pouvez voir qu'il y a une nouvelle ligne appelée `app.use(express.urlencoded({ extended: false }))` à la ligne 8, qui nous permet de lire la réponse de l'utilisateur depuis le formulaire.
* Dans le fichier `index.ejs`, vous pouvez voir que nous avons défini `name="fullURL"` qui est la façon dont nous pouvons recevoir l'URL sur le backend.

Voici notre fichier `index.ejs` :

```html
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<meta http-equiv="X-UA-Compatible" content="ie=edge" />
		<link
			rel="stylesheet"
			href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
		/>
		<title>codedamn URL Shortner Project</title>
	</head>
	<body>
		<div class="container">
			<h1>URL Shrinker</h1>
			<form action="/short" method="POST" class="my-4 form-inline">
				<label for="fullUrl" class="sr-only">URL</label>
				<input
					required
					placeholder="URL"
					type="url"
					name="fullUrl"
					id="fullUrl"
					class="form-control col mr-2"
				/>
				<button class="btn btn-success" type="submit">Shrink This!</button>
			</form>

			<table class="table table-striped table-responsive">
				<thead>
					<tr>
						<th>Full URL</th>
						<th>Short URL</th>
						<th>Clicks</th>
					</tr>
				</thead>
				<tbody>
					<% shortUrls.forEach(shortUrl => { %>
					<tr>
						<td><a href="<%= shortUrl.full %>"><%= shortUrl.full %></a></td>
						<td><a href="<%= shortUrl.short %>"><%= shortUrl.short %></a></td>
						<td><%= shortUrl.clicks %></td>
					</tr>
					<% }) %>
				</tbody>
			</table>
		</div>
	</body>
</html>

```

C'est un défi simple, car nous devons simplement mettre ce code pour le compléter :

```js
app.use(express.urlencoded({ extended: false }))

app.post('/short', async (req, res) => {
	// Grab the fullUrl parameter from the req.body
	const fullUrl = req.body.fullUrl
	console.log('URL requested: ', fullUrl)

	// insert and wait for the record to be inserted using the model
	const record = new ShortURL({
		full: fullUrl
	})

	await record.save()

	res.redirect('/')
})
```

Tout d'abord, nous récupérons l'URL envoyée par HTML en utilisant `req.body.fullUrl`. Pour activer cela, nous avons également `app.use(express.urlencoded({ extended: false }))` qui nous permet d'obtenir les données du formulaire.

Ensuite, nous créons et sauvegardons notre enregistrement comme nous l'avons fait la dernière fois. Enfin, nous redirigeons l'utilisateur vers la page d'accueil afin que l'utilisateur puisse voir les nouveaux liens.

**Astuce :** Vous pouvez rendre cette application plus intéressante en effectuant une requête Ajax vers l'API backend au lieu de la soumission typique de formulaire. Mais nous allons laisser cela ici car cela se concentre davantage sur la configuration MongoDB + Node plutôt que sur JavaScript.

## Partie 6 : Affichage des URL courtes sur le frontend

Maintenant que nous stockons des URL raccourcies dans MongoDB, passons à l'affichage de celles-ci sur le frontend également. 

Souvenez-vous des variables passées au modèle `ejs` précédemment ? Maintenant, nous allons les utiliser.

La boucle de modèle pour `ejs` a été faite pour vous dans le fichier `index.ejs` (vous pouvez voir cette boucle ci-dessus). Cependant, nous devons écrire la requête Mongoose pour extraire les données dans cette section.

Si nous regardons le modèle, nous verrons que dans `index.js`, nous avons le code suivant :

```js
app.get('/', (req, res) => {
	const allData = [] // write a mongoose query to get all URLs from here
	res.render('index', { shortUrls: allData })
})

```

Nous avons déjà un modèle défini avec nous pour interroger les données de Mongoose. Utilisons-le pour obtenir tout ce dont nous avons besoin.

Voici notre fichier de solution :

```js
const express = require('express')
const app = express()
const mongoose = require('mongoose')
// import the model here
const ShortURL = require('./models/url')

app.set('view engine', 'ejs')
app.use(express.urlencoded({ extended: false }))

app.get('/', async (req, res) => {
	const allData = await ShortURL.find()
	res.render('index', { shortUrls: allData })
})

app.post('/short', async (req, res) => {
	// Grab the fullUrl parameter from the req.body
	const fullUrl = req.body.fullUrl
	console.log('URL requested: ', fullUrl)

	// insert and wait for the record to be inserted using the model
	const record = new ShortURL({
		full: fullUrl
	})

	await record.save()

	res.redirect('/')
})

// Setup your mongodb connection here
mongoose.connect('mongodb://localhost/codedamn', {
	useNewUrlParser: true,
	useUnifiedTopology: true
})

mongoose.connection.on('open', async () => {
	// Wait for mongodb connection before server starts

	// Just 2 URLs for testing purpose
	await ShortURL.create({ full: 'http://google.com' })
	await ShortURL.create({ full: 'http://codedamn.com' })

	app.listen(process.env.PUBLIC_PORT, () => {
		console.log('Server started')
	})
})
```

Vous pouvez voir que c'était aussi simple que de faire `await ShortURL.find()` dans la variable `allData`. La partie suivante est celle où les choses deviennent un peu délicates.

## Partie 7 : Faire fonctionner la redirection

Nous avons presque terminé ! Nous avons l'URL complète et l'URL courte stockées dans la base de données maintenant, et nous les affichons également sur le frontend. 

Mais vous remarquerez que la redirection ne fonctionne pas pour l'instant et nous obtenons une erreur Express.

Corrigeons cela. Vous pouvez voir dans le fichier `index.js` qu'il y a une nouvelle route dynamique ajoutée à la fin qui gère ces redirections :

```
app.get('/:shortid', async (req, res) => {
	// grab the :shortid param
	const shortid = ''

	// perform the mongoose call to find the long URL

	// if null, set status to 404 (res.sendStatus(404))

	// if not null, increment the click count in database

	// redirect the user to original link
})
```

Nos défis pour cette partie ressemblent à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/i3.png)

D'accord. Tout d'abord, nous devons extraire l'URL complète lorsque nous visitons une URL courte. Voici comment nous allons faire cela :

```js
app.get('/:shortid', async (req, res) => {
	// grab the :shortid param
	const shortid = req.params.shortid

	// perform the mongoose call to find the long URL
	const rec = await ShortURL.findOne({ short: shortid })

	// ...
})

```

Maintenant, si nous voyons que notre résultat est null, nous enverrons un statut 404 :

```js
app.get('/:shortid', async (req, res) => {
	// grab the :shortid param
	const shortid = req.params.shortid

	// perform the mongoose call to find the long URL
	const rec = await ShortURL.findOne({ short: shortid })

	// if null, set status to 404 (res.sendStatus(404))
	if (!rec) return res.sendStatus(404)

	res.sendStatus(200)	
})
```

Cela passe notre premier défi. Ensuite, si nous avons en fait un lien, redirigeons l'utilisateur et incrémentons également le compteur de clics dans la base de données.

```js
app.get('/:shortid', async (req, res) => {
	// grab the :shortid param
	const shortid = req.params.shortid

	// perform the mongoose call to find the long URL
	const rec = await ShortURL.findOne({ short: shortid })

	// if null, set status to 404 (res.sendStatus(404))
	if (!rec) return res.sendStatus(404)

	// if not null, increment the click count in database
	rec.clicks++
	await rec.save()

	// redirect the user to original link
	res.redirect(rec.full)
})
```

De cette façon, nous pouvons incrémenter et stocker le résultat dans la base de données à nouveau. Et cela devrait passer tous nos défis.

## Conclusion

Félicitations ! Vous venez de construire un raccourcisseur d'URL fonctionnel complet par vous-même en utilisant Express + Node + MongoDB. Donnez-vous une tape dans le dos ! 

Le code source final est [disponible sur GitHub](https://github.com/codedamn-classrooms/node-mongodb-url-shortner/tree/lab7-sol).

Si vous avez des commentaires sur cet article ou sur les salles de classe de codedamn, n'hésitez pas à me contacter sur [Twitter](https://twitter.com/mehulmpt). Discutons-en :)