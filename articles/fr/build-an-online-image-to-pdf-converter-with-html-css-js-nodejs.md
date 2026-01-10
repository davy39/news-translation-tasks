---
title: Comment créer un convertisseur d'images en PDF en ligne avec HTML, CSS, JS
  et NodeJS
subtitle: ''
author: Gideon Akinsanmi
co_authors: []
series: null
date: '2023-08-30T17:03:33.000Z'
originalURL: https://freecodecamp.org/news/build-an-online-image-to-pdf-converter-with-html-css-js-nodejs
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/png-img-pdf.png
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: Web Development
  slug: web-development
seo_title: Comment créer un convertisseur d'images en PDF en ligne avec HTML, CSS,
  JS et NodeJS
seo_desc: 'An online image-to-PDF converter is a website that helps you convert your
  images to PDFs. This tool is useful because it provides an efficient way to store
  your images.

  In this tutorial, you''ll learn how you can create your online image-to-pdf conver...'
---

Un convertisseur d'images en PDF en ligne est un site web qui vous aide à convertir vos images en PDF. Cet outil est utile car il fournit un moyen efficace de stocker vos images.

Dans ce tutoriel, vous apprendrez comment créer votre propre convertisseur d'images en PDF en ligne avec HTML, CSS, JavaScript et NodeJS.

## Table des matières
- [Prérequis](#heading-prerequisites)
- [Installation du projet](#heading-installation)
- [Étapes à suivre](#heading-steps-to-follow)
- [Comment créer la route URL racine](#heading-how-to-create-the-root-url-route)
- [Comment téléverser des images sur le serveur](#heading-how-to-upload-images-to-the-server)
- [Comment trier les images et les convertir en PDF](#heading-how-to-sort-the-images-and-convert-them-to-pdf)
- [Recommencer](#startingover)
- [Conclusion](#heading-conclusion)

## Prérequis
Avant de commencer ce projet, vous devez avoir ou connaître les langages/bibliothèques/frameworks suivants :

- HTML, CSS et JavaScript : Vous devez avoir une connaissance de base de l'utilisation de HTML, CSS et JavaScript pour suivre ce tutoriel. Vous devez savoir comment créer ces fichiers et les lier ensemble. Vous devez connaître les éléments fondamentaux de HTML, les sélecteurs CSS de base, les concepts JavaScript et le DOM.

- NodeJS et npm : Vous devez avoir npm et Node.js installés car nous les utiliserons pour installer les packages nécessaires à votre projet. Plus précisément, vous devez avoir une connaissance de base de l'importation et de l'utilisation des modules intégrés de Nodejs.

- [Nodemon](https://www.npmjs.com/package/nodemon) : Nodemon est un package Node important qui vous aidera à développer votre projet plus rapidement. Il aide à redémarrer votre serveur lorsque vous apportez des modifications au projet.

- [Express.js](https://www.expressjs.com) et express-generator : Express.js est le framework Node que vous utiliserez pour construire le serveur web. Express-generator est une bibliothèque qui vous aidera à créer les fichiers et dossiers nécessaires pour que Express.js fonctionne efficacement. Vous devez savoir comment créer une application Express de base.

- [Express-session](https://www.npmjs.com/package/express-session) : Il s'agit d'une bibliothèque middleware Express qui vous aidera à gérer les sessions de l'application. Vous devez connaître les configurations de cette bibliothèque.

- [Jade/Pug](https://pugjs.org) : Il s'agit d'un moteur de templating JavaScript qui vous aidera à rendre l'adresse des images téléversées dans un fichier HTML. Vous devez connaître les bases de cette bibliothèque.

- [PDFkit](https://pdfkit.org) : Il s'agit d'une bibliothèque JavaScript que nous utiliserons pour convertir les images en PDF.

- [Multer](https://www.npmjs.com/package/multer) : Il s'agit d'une bibliothèque Node qui gérera les téléversements de fichiers.

- [Sortablejs](https://www.npmjs.com/package/sortablejs) : Il s'agit d'une bibliothèque JavaScript de glisser-déposer que nous utiliserons dans le frontend pour réorganiser nos images avant qu'elles ne soient converties en PDF.

Enfin, vous devez savoir comment créer des dossiers et des fichiers (avec leurs extensions appropriées). Vous devez savoir comment éditer ces fichiers avec un éditeur de texte.

## Installation du projet
Tout d'abord, vous devez créer un dossier et y naviguer avec le CLI :

```
mkdir img2pdf
cd img2pdf
```

Ensuite, initialisez-le en tant que package npm afin de pouvoir installer toutes les bibliothèques nécessaires.

```
npm init -y
```

Si tout se passe bien, il y aura un fichier package.json dans votre dossier.

Le package.json devrait ressembler à ceci :

```
{
  "name": "img2pdf",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
```

Ensuite, nous installerons express-generator comme ceci :

```
npx express-generator
npm install
```

Nous choisirons `jade` comme moteur de templating par défaut.

La commande ci-dessus configurera tous les dossiers et bibliothèques nécessaires pour que Express.js fonctionne efficacement.

À la fin de l'installation, votre dossier de projet ressemblera à ceci :

```
/img2pdf
  /bin
    www
  /node_modules
    /public
	  /images
	  /javascripts
	  /stylesheets
  /routes
  /views
  app.js
  package.json
  package-lock.json
```

* `bin/www` est le point d'entrée de votre application.
* Le dossier `node_modules` stocke les packages nécessaires à notre projet.
* Le dossier `public` stockera les fichiers statiques qui seront retournés et stockés par le serveur.
* Le dossier `routes` stocke toutes les routes de l'application.
* Le dossier `views` stocke les fichiers Jade qui seront utilisés pour le rendu côté serveur.
* `app.js` est le fichier JavaScript racine.

Lorsque vous vérifiez votre fichier `package.json`, vous verrez que `Express.js`, `Jade` et quelques autres bibliothèques ont été installés.

Ensuite, nous installerons le package Nodemon globalement.

```
npm install -g nodemon
```

Enfin, nous installerons `PDFkit`, `Multer`, `Sortablejs` et `Express-session`.

```
npm i multer pdfkit sortablejs express-session
```

Ensuite, ajoutez un script `devstart` dans votre package.json. Il permettra à Nodemon de redémarrer votre application lorsque vous apportez des modifications à vos fichiers JavaScript.

```
"devstart": "nodemon ./bin/www"
```

À la fin de votre installation, votre fichier package.json devrait ressembler à ceci :

```
{
  "name": "img2pdf",
  "version": "0.0.0",
  "private": true,
  "scripts": {
    "start": "node ./bin/www",
	"devstart": "nodemon ./bin/www"
  },
  "dependencies": {
    "cookie-parser": "~1.4.4",
    "debug": "~2.6.9",
    "express": "~4.16.1",
	"express-session": "^1.17.3",
    "http-errors": "~1.6.3",
    "jade": "~1.11.0",
    "morgan": "~1.9.1",
    "multer": "^1.4.5-lts.1",
    "pdfkit": "^0.31.0",
    "sortablejs": "^1.15.0"
  }
}
```

Ensuite, vous naviguerez vers le dossier du projet et démarrerez le serveur de l'application.

```
cd img2pdf
set DEBUG=img2pdf:* & npm run devstart
```

Une fois que vous recevez un message de succès, cela signifie que le serveur est déjà en cours d'exécution.

Ouvrez votre navigateur web et tapez `http://localhost:3000/` dans la barre de recherche.

Si tout se passe bien, voici ce que vous devriez obtenir :

![home_express](https://www.freecodecamp.org/news/content/images/2023/08/home_express.PNG)

## Étapes à suivre

Avant d'écrire le code, passons en revue les étapes que nous allons suivre pour construire ce projet :

1. Tout d'abord, vous définirez une route qui retourne le fichier HTML `index` lorsque l'URL racine `/` est atteinte.

2. Dans votre fichier HTML `index`, vous créerez un formulaire qui n'accepte que les fichiers image (png, jpg) puis les envoie au serveur à une route définie.

3. Lorsque le serveur reçoit les images avec `Multer`, il les stockera dans un dossier, stockera l'adresse dans un stockage de session et redirigera la demande vers la route URL racine qui rendra un fichier `Jade` contenant l'adresse des images téléversées.

4. Dans le fichier `Jade`, vous activerez `Sortablejs` afin que l'utilisateur puisse réorganiser les images avant de les convertir en PDF. Il y aura également un bouton 'convertir en PDF' qui enverra l'adresse de l'image triée à la route `/pdf` du serveur.

5. Lorsque la route `/pdf` reçoit les images, vous utiliserez `PDFkit` pour convertir les images en PDF. Ensuite, vous enverrez l'adresse du PDF converti.

6. Lorsque l'utilisateur clique sur le lien PDF, le fichier sera téléchargé sur l'appareil de l'utilisateur.

## Comment créer la route URL racine

Tout d'abord, nous allons créer une route qui envoie un fichier index.html lorsque l'URL racine (`/`) est atteinte.

Voici le simple organigramme de cette opération :

![Organigramme illustrant le processus : Start -> L'utilisateur envoie une requête GET à l'URL racine '/' -> Le serveur retourne un fichier HTML -> End](https://www.freecodecamp.org/news/content/images/2023/08/flowchart-homepage.png)

Tout d'abord, ouvrez votre fichier routes/index.js et créez une route qui retourne un fichier HTML.

Remplacez tout le code dans le fichier routes/index.js par ceci :

```js
var express = require('express');
var router = express.Router();

var path = require('path');

//créer une route GET '/' qui retournera le fichier index.html stocké dans le dossier public/html
router.get('/', function(req, res, next) {
  res.sendFile(path.join(__dirname, '..','/public/html/index.html'));
}); 

module.exports = router;
```

Dans le code ci-dessus, nous avons inclus la bibliothèque `express` et activé la fonction `express.Router()`. Le module `path` a également été inclus car il sera utilisé pour décrire les chemins de fichiers.

Ensuite, nous avons défini une méthode de route qui gérera toutes les requêtes GET dirigées vers l'URL racine `/`. Chaque fois que la méthode de route reçoit une requête, elle utilisera la méthode `res.sendFile()` pour envoyer un fichier `index.html` à l'utilisateur.

La variable `__dirname` et la méthode `path.join()` utilisées dans la méthode `res.sendFile(...)` nous aident à spécifier précisément l'adresse du fichier `index.html`.

Ensuite, créez un dossier `html` dans le dossier public et ajoutez-y une page index.html.

Voici à quoi devrait ressembler votre dossier `public` :

```
/public
  /html
  /images
  /javascripts
  /stylesheets
```

Ensuite, créez un fichier `index.html` dans votre dossier `public/html` et ajoutez-y ce code :

```html
<DOCTYPE HTML> 
<html>
  <head>
    <title>Convertisseur IMG-en-PDF</title>
	<meta charset="UTF-8">
	<meta name="author" content="VOTRE NOM">
	<meta name="description" content="Convertissez facilement n'importe quel ensemble d'images en PDF">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
  </head>
  <body>
	<h1>Convertisseur d'images en PDF</h1>
  </body>
</html>
```

Si votre serveur est toujours en cours d'exécution, allez sur `https://localhost:3000/` dans votre navigateur web.

Voici ce que vous devriez obtenir :

![homepage-1](https://www.freecodecamp.org/news/content/images/2023/08/homepage-1.PNG)

Si vous n'avez pas démarré votre serveur, naviguez jusqu'au répertoire de votre projet (`cd img2pdf`) et exécutez cette commande :

```
set DEBUG=img2pdf:* & npm run devstart
```

## Comment téléverser des images sur le serveur

Dans cette section, je vais expliquer comment téléverser des images sur le serveur.

Voici l'organigramme simple de cette opération :

![Organigramme illustrant le processus : Start -> L'utilisateur envoie des images au serveur -> Le serveur reçoit les images, les renomme et les stocke dans un dossier -> Le serveur extrait les noms de fichiers des images, les stocke dans une session et redirige la demande vers l'URL racine -> La route URL racine reçoit la demande et rend un fichier Jade/Pug contenant les noms de fichiers des images -> end](https://www.freecodecamp.org/news/content/images/2023/08/flowchart-file-upload.png)

Voici ce qui se passe :

* L'utilisateur envoie des images au serveur
* Le serveur reçoit les images, les renomme et les stocke dans un dossier
* Le serveur extrait les noms de fichiers des images, les stocke dans une session, redirige la demande vers l'URL racine
* La route URL racine reçoit la demande et rend un fichier Jade/pug contenant les noms de fichiers des images
* Fin

Alors que votre serveur est toujours en cours d'exécution, remplacez le contenu de votre fichier `public/html/index.html` par ceci :

```html
<DOCTYPE HTML> 
<html>
  <head>
	<title>Convertisseur IMG-en-PDF</title>
	<meta charset="UTF-8">
	<meta name="author" content="Gideon Akinsanmi">
	<meta name="description" content="Convertissez facilement n'importe quel ensemble d'images en PDF">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel='stylesheet' href='/stylesheets/style.css' />
	<link rel='stylesheet' href='/stylesheets/index.css' />
  </head>
  <body>
	<main>
	  <header>
		<h1><a href='/'>IMG2PDF</a></h1>
	  </header>
	  <article>
		<p class='title'>Convertissez facilement vos images PNG et JPG</p>
		<form method='post' action='/upload' enctype='multipart/form-data'>
		  <input id='file-upload' type='file' name='images' accept='.png, .jpg' multiple/>
		  <p><label for='file-upload'>Sélectionner des fichiers</label></p>
		  <p id='selected-files'><code> </code> </p>
		  <p><input type='submit' value='upload' /></p>
		</form>
	  </article>
	  <footer>
		<p><code>copyright &copy; IMG2PDF 2023</code></p>
	  </footer>
	  <script>
		let fileUpload = document.getElementById('file-upload');
		let selectedFiles = document.querySelector('#selected-files code');
		let submitButton = document.querySelector('input[type=submit]');
			
		let filenames = ''
		fileUpload.onchange = function (){
			filenames = ''
			for(let file of this.files){
				filenames += file.name
				filenames += ','
			}
			selectedFiles.parentElement.style.display = 'block'
			selectedFiles.textContent = filenames
			submitButton.style.display = 'inline-block';
		}
	  </script>
	</main>
  </body>
</html>
```

Dans le code ci-dessus, nous avons lié certains fichiers CSS (`styles.css` et `index.css`) au document. Nous avons également créé un élément `form` qui envoie une requête POST à la route `/upload`. L'élément `form` a un `enctype` de `multipart/form-data` (sans cela, notre serveur ne peut pas recevoir les images).

Dans l'élément `form`, il y a un élément `input` qui nous aidera à obtenir les fichiers de l'appareil. L'input a un attribut `name` avec la valeur `images` (qui sera utilisé par multer pour identifier les images). Il a été configuré pour accepter plusieurs fichiers image (avec les extensions .png ou .jpg).

Il y a aussi un élément `input` qui agit comme le bouton de soumission. Il sera utilisé pour déclencher la demande de téléversement de fichier.

Ensuite, il y a l'élément `script` qui contient du code JavaScript qui ajoute de l'interactivité au document HTML.

Créez un fichier `style.css` dans votre dossier `public/stylesheets` et ajoutez-y ce code CSS :

```css
* {margin: 0;padding: 0;box-sizing: border-box;font-family:Poppins;transition: all 0.5s ease;}
main {display: flex;flex-direction:column;height:100vh;}
			
h1 a {color: #ff6600;text-decoration:none;}
h1 {background-color: white;font-size:25pt;padding:5px;text-align: center;}
			
p {font-size:20pt;text-align: center;margin-bottom: 25px;}
						
header, footer {border: 2px solid #ececec;}
			
article {padding:20px;flex-grow: 1;background-color: #fff7f0;}
footer p {margin-bottom: 0;font-size: 16pt;}
			
@media screen and (max-width: 380px) {
	footer p {font-size: 12pt;}
}
			
@media screen and (max-width: 300px) {
	h1 {font-size: 17pt;}
}
```

Le code CSS ci-dessus définit la mise en page générale de votre site web.

Ensuite, créez un fichier `index.css` dans votre dossier `public/stylesheets` et ajoutez-y ce code :

```css
p.title {font-size:30pt;}
p#selected-files {display:none;white-space: nowrap;overflow:hidden;text-overflow: ellipsis;}
			
label {display: inline-block;font-size:25pt;cursor:pointer;padding: 5px 45px;border-radius:25px;color:white;background-color: #ff9955;}
label:hover {background-color: #ff6600;}

input[type=file] {display: none;}
input[type=submit] {display: none;font-size:16pt;cursor:pointer;padding: 5px 25px;border-radius:25px;color:white;background-color:black;}
			
@media screen and (max-width: 380px) {
	p.title {font-size: 25pt;}
}
			
@media screen and (max-width: 300px) {
	p.title {font-size: 22pt;}
	label {font-size: 20pt;}
}
			
@media screen and (max-width: 250px) {
	label {padding: 5px 35px;}
}
```

Le code CSS ci-dessus définit le style spécifique des éléments `index.html`.

Ensuite, vous ouvrirez votre fichier `routes/index.js` et créerez une route `/upload` qui recevra les fichiers image, les stockera dans un dossier, stockera les noms de fichiers dans le stockage de session et redirigera la demande vers l'URL racine.

Tout d'abord, nous devons éditer le fichier `app.js` et activer `express-session`.

Ajoutez ce code à votre fichier `app.js` :

```js
//inclure le module express-session
var session = require('express-session');

//l'activer en tant que middleware express.js
app.use( session({secret: 'VOTRE_SECRET'}) )
```

Voici à quoi devrait ressembler votre fichier `app.js` :

```js
var createError = require('http-errors');
var express = require('express');
var path = require('path');
var logger = require('morgan');
var session = require('express-session');

var indexRouter = require('./routes/index');


var app = express();

// configuration du moteur de vue
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(express.static(path.join(__dirname, 'public')));
//activer express-session
app.use( session({secret: 'VOTRE_SECRET'}) )

app.use('/', indexRouter);


// capturer 404 et transmettre au gestionnaire d'erreurs
app.use(function(req, res, next) {
  next(createError(404));
});

// gestionnaire d'erreurs
app.use(function(err, req, res, next) {
  // définir les variables locales, ne fournissant l'erreur qu'en développement
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // rendre la page d'erreur s'il y a une erreur
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;
```

Ouvrez votre fichier `routes/index.js` et créez une route qui recevra les noms de fichiers des images, les stockera dans une session et redirigera vers l'URL racine :

```js
/importer la bibliothèque multer
var multer = require('multer');
var path = require('path');

//configuration du stockage de fichiers multer
let storage = multer.diskStorage({
	//stocker les images dans le dossier public/images
	destination: function(req, file, cb){
		cb(null, 'public/images')
	},
	//renommer les images
	filename: function(req, file, cb){
		cb(null, file.fieldname + '-' + Date.now() + '.' + file.mimetype.split('/')[1] )
	}
})

//configuration pour le filtre de fichiers
let fileFilter = (req, file, callback) => {
	let ext = path.extname(file.originalname);
	//si l'extension du fichier n'est pas '.png' ou '.jpg', retourner une page d'erreur, sinon retourner vrai
	if (ext !== '.png' && ext !== '.jpg'){
		return callback(new Error('Seuls les fichiers png et jpg sont acceptés'))
	} else {
		return callback(null, true)
	}
}

//initialiser Multer avec les configurations pour le stockage et le filtre de fichiers
var upload = multer({ storage, fileFilter: fileFilter});

router.post('/upload', upload.array('images'), function (req, res){
	let files = req.files;
	let imgNames = [];
	
	//extraire les noms de fichiers 
	for( i of files){
		let index = Object.keys(i).findIndex( function (e){return e === 'filename'})
		imgNames.push( Object.values(i)[index] )
	}
	//stocker les noms de fichiers des images dans une session
	req.session.imagefiles = imgNames
		
    //rediriger la demande vers la route URL racine
	res.redirect('/')
})
```

Dans le code ci-dessus, nous avons inclus la bibliothèque `Multer`. Ensuite, nous avons utilisé la méthode `multer.diskStorge()` pour décrire où les fichiers image seront stockés et comment ils doivent être renommés.

De plus, nous avons créé une fonction `fileFilter` pour nous assurer que seuls les fichiers png et jpg sont stockés par le serveur. Si l'utilisateur envoie un fichier qui n'est pas PNG ou JPG, une page d'erreur sera affichée avec le message "Seuls les fichiers png et jpg sont acceptés".

Ensuite, nous avons créé une méthode de route qui écoute les requêtes POST dirigées vers la route `/upload`.

Dans cette méthode de route, nous avons inclus la méthode upload.array('images') qui indique à mutler de ne stocker que les fichiers dont le nom est `images` (selon l'élément d'entrée HTML `<input id='file-upload' type='file' name='images' accept='.png, .jpg' multiple/>`).

Après cela, nous avons extrait les noms de fichiers de la propriété `req.files` et les avons stockés dans le stockage de session. Enfin, nous redirigeons la demande vers la route URL racine.

Dans le fichier `routes/index.js`, éditez la route URL racine afin qu'elle rende un fichier `index.jade` si la session stocke les noms de fichiers des images.

```js
router.get('/', function(req, res, next) {
	//s'il n'y a pas de noms de fichiers d'images dans une session, retourner la page HTML normale
	if (req.session.imagefiles === undefined){
		res.sendFile(path.join(__dirname, '..','/public/html/index.html'));
	} else {
	//s'il y a des noms de fichiers d'images stockés dans une session, les rendre dans un fichier index.jade
		res.render('index', {images: req.session.imagefiles} )
	}
});
```

Dans le code ci-dessus, lorsque la route URL racine reçoit une demande, elle vérifie d'abord s'il y a une propriété `imagefiles` stockée dans le stockage de session. Si ce n'est pas le cas, elle envoie le fichier `index.html`. Mais s'il y en a un, un fichier `index.jade` contenant les noms de fichiers des images sera envoyé.

Enfin, allez dans le fichier `views/index.jade` et éditez-le afin qu'il rende les images téléversées en HTML :

```
doctype html
html
  head
    title Convertisseur IMG-en-PDF
    meta(charset='UTF-8')
  body
    h1 Images
    each image in images
      img(src=`/images/${image}` width='200' height='200')
```

Le code ci-dessus est écrit en syntaxe Jade, lorsque le serveur le rend, il sera sous forme de document HTML.

**Note :** assurez-vous de faire l'indentation de votre contenu dans `Jade/Pug` avec soit la touche espace soit la touche tabulation, mais pas les deux.

Lorsque vous exécutez ou redémarrez votre serveur (`rs` avec `Nodemon`), allez sur http://localhost:3000/ et relancez le processus de téléversement (de la sélection des fichiers au clic sur le bouton de téléversement).

Vous devriez voir une page HTML contenant les images que vous avez téléversées.

Voici mon résultat :

![upload-images](https://www.freecodecamp.org/news/content/images/2023/08/upload-images.PNG)

## Comment trier les images et les convertir en PDF

Dans cette section, je vais expliquer comment vous pouvez permettre à l'utilisateur de réorganiser ses images et de les convertir en PDF.

Voici l'organigramme simple de cette opération :

![Organigramme illustrant le processus : Start -> L'utilisateur trie les images -> L'utilisateur clique sur 'convertir en PDF' -> Le navigateur envoie une demande au serveur contenant les noms de fichiers des images triées -> Le serveur reçoit la demande, convertit les images en PDF et envoie l'adresse au navigateur -> Le navigateur reçoit l'adresse et l'affiche à l'utilisateur -> L'utilisateur clique sur le lien et télécharge le PDF -> End](https://www.freecodecamp.org/news/content/images/2023/08/flowchart-sort-and-upload.png)

Voici ce qui se passe :

* L'utilisateur clique sur "convertir en PDF"
* Le navigateur envoie une demande au serveur contenant les noms de fichiers des images triées
* Le serveur reçoit la demande, convertit les images en PDF et envoie l'adresse au navigateur
* Le navigateur reçoit l'adresse et l'affiche à l'utilisateur
* L'utilisateur clique sur le lien et télécharge le PDF
* Fin

Dans le fichier `views/index.jade`, nous utiliserons `Sortablejs` pour trier les images.

Remplacez le contenu de votre fichier `index.jade` par ceci :

```
doctype html
html
  head
    title Convertisseur IMG-en-PDF
    meta(charset='UTF-8')
    link(rel='stylesheet' href='/stylesheets/style.css')
    link(rel='stylesheet' href='/stylesheets/index-view.css')
    script(type='module' src='/javascripts/sort.js' defer)
  body
    main
      header
        h1
          a(href='/') IMG2PDF
      article
        p 
          a(href='/new') Nouveau +
        div
          each image in images
           img(src=`/images/${image}` data-name=image width='200' height='200')
        p
          a(class='convert')
            span(class='text') Convertir en PDF &rarr;
            span(class='loader')
        p
          a(class='download' download) Télécharger &darr;
      footer
        p
          code copyright &copy; IMG2PDF 2023
```

Le code ci-dessus est un fichier Jade qui sera rendu sous forme de document HTML. Il contient les métadonnées du document (y compris les éléments `link` et `style` qui se connectent aux fichiers CSS et JavaScript), les éléments image, les hyperliens et quelques autres éléments HTML.

Ensuite, créez un fichier `public/stylesheets/index-view.css` et ajoutez-y ce code :

```css
p a {font-size:20pt;text-decoration: none;color: white;display: inline-block;padding: 5px 20px;margin-bottom:15px;background-color: #ff6600;cursor: pointer;}

div {margin:auto;margin-bottom: 15px;padding:10px;display: flex;flex-direction:row;flex-wrap:wrap;width:80%;background-color: rgba(255,255,255,0.9);}

div img {width: 200px;height:200px;object-fit: contain;padding: 10px;background-color: #ffe6d5;margin-right:10px;margin-bottom: 10px;cursor:pointer;}

p a.download {background-color: black;display:none;}

span.loader {display:none;border: 5px solid black;border-top: 5px solid white;border-radius:50%;width: 25px;height: 25px;animation: spin 0.5s linear infinite;}
	
	
@keyframes spin{
	0% {transform: rotate(0deg);}
	100% {transform: rotate(360deg);}
}
	
@media screen and (max-width: 620px) {	
	div img {width: 45%;height: 150px;}
}
	
@media screen and (max-width: 415px) {
	p a {font-size: 16pt;}
	div img {height: 120px;}
}
	
@media screen and (max-width: 330px) {
	p a {font-size: 14pt;}
	div {width: 100%;}
	div img {width:100%;margin-right: 0px;margin-bottom: 5px;}
}
	
@media screen and (max-width: 260px) {
	p a {font-size: 13pt;padding: 5px 10px;}
}
```

Ensuite, naviguez jusqu'au dossier `node_modules/sortablejs/modular` et copiez le fichier `sortable.core.esm.js` dans le dossier `public/javascripts`.

Ensuite, créez un fichier `public/javascripts/sort.js`.

Vous ajouterez du code qui activera `Sortablejs` et enverra les noms de fichiers triés au serveur pour conversion :

```js
import Sortable from '/javascripts/sortable.core.esm.js';

//utiliser sortablejs sur l'élément conteneur pour les balises d'image
let list = document.querySelector('div');
let sort = Sortable.create(list);

let convertButton = document.querySelector('a.convert');

//Lorsque le bouton de conversion est cliqué
convertButton.onclick = function(){
	let images = document.querySelectorAll('img');
	let loader = document.querySelector('span.loader');
	let convertText = document.querySelector('span.text');
	let downloadButton = document.querySelector('a.download');
	
	let filenames = [];
	//extraire les noms des images dans un tableau
	for(let image of images){
		filenames.push(image.dataset.name)
	}
	//activer l'animation de chargement
	loader.style.display = 'inline-block';
	convertText.style.display = 'none'
	
	//Créer une requête post qui enverra les noms de fichiers des images à la route '/pdf' et recevra le lien vers le fichier PDF
	fetch('/pdf', {
		method: 'POST',
		headers: {
			"Content-Type": "application/json"
		},
		body: JSON.stringify(filenames)
	})
	.then( (resp)=> {
		return resp.text()
	})
	.then( (data) => {
        //arrêter l'animation de chargement
		loader.style.display = 'none';
		
        //afficher le bouton de conversion et de téléchargement
		convertText.style.display = 'inline-block'
		downloadButton.style.display = 'inline-block'
		
        //attacher l'adresse au bouton de téléchargement
		downloadButton.href = data
	})
	.catch( (error) => {
		console.error(error.message)
	})	
}
```

Dans le code ci-dessus, nous avons importé le fichier JavaScript principal de Sortablejs et l'avons activé sur l'élément parent des éléments img.

Lorsque le bouton `Convertir en PDF` est cliqué, nous avons extrait les noms de fichiers des images des éléments img et les avons envoyés en tant que requête POST au serveur.

Lorsque le navigateur reçoit la réponse du serveur, nous avons attaché le lien au bouton de téléchargement afin que lorsque l'utilisateur clique dessus, le document PDF soit téléchargé sur l'appareil de l'utilisateur.

Ensuite, dans votre fichier `routes/index.js`, vous créerez une route `/pdf` qui recevra les noms de fichiers triés et les convertira en PDF.

Tout d'abord, créez un dossier `pdf` dans le dossier `public` et ajoutez ce code à votre fichier `routes/index.js` :

```js
var path = require('path');
var fs = require('fs');

//importer PDFkit
var PDFDocument = require('pdfkit');

router.post('/pdf', function(req, res, next) {
	let body = req.body
	
	//Créer un nouveau pdf
	let doc = new PDFDocument({size: 'A4', autoFirstPage: false}); 
	let pdfName = 'pdf-' + Date.now() + '.pdf';
	
	//stocker le pdf dans le dossier public/pdf
	doc.pipe( fs.createWriteStream( path.join(__dirname, '..',`/public/pdf/${pdfName}` ) ) );
	
	//créer les pages pdf et ajouter les images
	for(let name of body){
		doc.addPage()
		doc.image(path.join(__dirname, '..',`/public/images/${name}`),20, 20, {width: 555.28, align: 'center', valign: 'center'} )
	}
	//fin du processus
	doc.end();
	
    //envoyer l'adresse au navigateur
	res.send(`/pdf/${pdfName}`)
})
```

Dans le code ci-dessus, nous avons inclus `pdfkit` et créé une méthode de route qui répond aux requêtes POST dirigées vers l'URL `/pdf`. Dans cette méthode de route, nous avons utilisé `pdfkit` pour convertir toutes les images en PDF. Enfin, nous avons envoyé l'adresse du document PDF au document.

Lorsque vous redémarrez le serveur, naviguez vers `http://localhost:3000/` dans votre navigateur web et relancez le processus de téléversement de fichiers. Vous pourrez convertir vos images en PDF.

Voici une vidéo YouTube décrivant l'ensemble du processus :

%[https://youtu.be/JRSnpkGXQcA]

## Comment annuler et relancer les téléversements d'images

Dans cette section, nous allons créer une fonctionnalité qui permet à l'utilisateur d'annuler le projet de téléversement de fichiers existant et d'en créer un nouveau.

Rappelez-vous qu'il y a un bouton `Nouveau +` dans notre `views/index.jade` qui pointe vers la route `/new`.

```
...
article
  p 
    a(href='/new') Nouveau +
...
```

Maintenant, nous allons écrire la route dans notre fichier `routes/index.js`.

Voici l'organigramme simple de cette opération :

![Organigramme illustrant le processus : Start -> L'utilisateur clique sur le bouton 'Nouveau +' -> Le navigateur envoie une requête GET au serveur -> Le serveur supprime les images et efface leurs noms de fichiers du stockage de session -> Le serveur redirige la demande vers l'URL racine -> End](https://www.freecodecamp.org/news/content/images/2023/08/flowchart-start-over.png)

Voici ce qui se passe :

* L'utilisateur clique sur le bouton 'Nouveau +'
* Le navigateur envoie une requête GET au serveur
* Le serveur supprime les images et efface leurs noms de fichiers du stockage de session
* Le serveur redirige la demande vers l'URL racine
* Fin

Ajoutez ce code à votre fichier `routes/index.js` :

```js
router.get('/new', function(req, res, next) {
	//supprimer les fichiers stockés dans la session
	let filenames = req.session.imagefiles;
    
	let deleteFiles = async (paths) => {
		let deleting = paths.map( (file) => unlink(path.join(__dirname, '..', `/public/images/${file}`) ) )
		await Promise.all(deleting)
	}
	deleteFiles(filenames)
	
	//supprimer les données de la session
	req.session.imagefiles = undefined
    
	//rediriger vers l'URL racine
	res.redirect('/')
})
```

Dans le code ci-dessus, lorsque la route `/new` reçoit une requête GET, elle supprimera les images stockées dans le dossier et le stockage de session. Après cela, elle redirigera la demande vers l'URL racine.

Lorsque vous naviguez vers `http://localhost:3000/`, téléversez quelques images et annulez le processus de téléversement de fichiers existant, vous verrez que les images ont été supprimées du dossier et que vous avez été redirigé vers la page d'accueil.

## Conclusion

Avec le code ci-dessus, vous avez été en mesure de créer un convertisseur d'images en PDF en ligne. Félicitations !

Comme vous le savez, le développement logiciel est un processus continu. Vous pouvez donc essayer d'implémenter certaines fonctionnalités supplémentaires (telles que la sécurité, la validation des entrées, etc.) au projet.

Vous pouvez consulter mon [dépôt GitHub](https://github.com/Gidthecoder/img2pdf/) pour le code source complet.

Si vous avez des questions pour moi, vous pouvez consulter mon profil freeCodeCamp pour mes coordonnées. Je répondrai aussi vite que possible !

À bientôt.