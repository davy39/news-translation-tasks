---
title: Comment déployer votre application sur le web en utilisant Express.js et Heroku
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-02T11:55:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-your-site-using-express-and-heroku
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c56740569d1a4ca317c.jpg
tags:
- name: deployment
  slug: deployment
- name: Express
  slug: express
- name: Express JS
  slug: express-js
- name: full stack
  slug: full-stack
- name: Git
  slug: git
- name: Heroku
  slug: heroku
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: node
  slug: node
- name: Node.js
  slug: nodejs
- name: npm
  slug: npm
- name: Tutorial
  slug: tutorial
- name: Web Applications
  slug: web-applications
seo_title: Comment déployer votre application sur le web en utilisant Express.js et
  Heroku
seo_desc: 'By Peter Gleeson

  If you are new to the world of web development, you will spend a lot of time learning
  how to build static sites with HTML, CSS and JavaScript.

  You might then start learning how to use popular frameworks such as React, VueJS
  or Angula...'
---

Par Peter Gleeson

Si vous êtes nouveau dans le monde du développement web, vous passerez beaucoup de temps à apprendre comment construire des sites statiques avec HTML, CSS et JavaScript.

Vous pourriez ensuite commencer à apprendre à utiliser des frameworks populaires tels que [React](https://reactjs.org/), [VueJS](https://vuejs.org/) ou [Angular](https://angular.io/).

Mais après avoir essayé quelques nouvelles idées et exécuté certains sites localement, vous pourriez vous demander comment déployer réellement votre site ou votre application. Et il s'avère que cela peut parfois être difficile de savoir par où commencer.

Personnellement, je trouve que l'exécution d'un serveur Express hébergé sur Heroku est l'une des manières les plus simples de commencer. Cet article vous montrera comment faire cela.

[Heroku](https://www.heroku.com/) est une plateforme cloud qui supporte un certain nombre de langages de programmation et de frameworks différents.

Ce n'est pas un article sponsorisé - il existe bien sûr de nombreuses autres solutions disponibles, telles que :

* [Digital Ocean](https://www.digitalocean.com/)
* [Amazon Web Services](https://aws.amazon.com/)
* [Azure](https://azure.microsoft.com/en-gb/)
* [Google Cloud Platform](https://cloud.google.com/)
* [Netlify](https://www.netlify.com/)
* [ZEIT Now](https://zeit.co/)

Consultez-les toutes et voyez laquelle convient le mieux à vos besoins.

Personnellement, j'ai trouvé Heroku le plus rapide et le plus facile à utiliser "out of the box". Le niveau gratuit est quelque peu limité en termes de ressources. Cependant, je peux le recommander en toute confiance à des fins de test.

Cet exemple hébergera un site simple en utilisant un serveur Express. Voici les étapes de haut niveau :

1. Configuration avec Heroku, Git, npm
2. Créer un serveur Express.js
3. Créer des fichiers statiques
4. Déployer sur Heroku

Cela devrait prendre environ 25 minutes au total (ou plus si vous souhaitez passer plus de temps sur les fichiers statiques).

Cet article suppose que vous connaissez déjà :

* Quelques bases de HTML, CSS et JavaScript
* Une utilisation basique de la ligne de commande
* Git de niveau débutant pour le contrôle de version

Vous pouvez trouver tout le code dans [ce dépôt](https://github.com/pg0408/lorem-ipsum-demo).

### Installation

La première étape de tout projet est de configurer tous les outils dont vous savez que vous aurez besoin.

Vous devrez avoir :

* Node et npm installés sur votre machine locale (lisez comment faire [ici](https://nodejs.org/en/download/))
* Git installé (lisez [ce guide](https://www.atlassian.com/git/tutorials/install-git))
* L'interface de ligne de commande Heroku installée ([voici comment faire](https://devcenter.heroku.com/articles/heroku-cli#download-and-install))

**1. Créer un nouveau répertoire et initialiser un dépôt Git**

Depuis la ligne de commande, créez un nouveau répertoire de projet et déplacez-vous dedans.

```
$ mkdir lorem-ipsum-demo
$ cd lorem-ipsum-demo
```

Maintenant que vous êtes dans le dossier du projet, initialisez un nouveau dépôt Git.

⚠️ Cette étape est importante car [Heroku repose sur Git](https://devcenter.heroku.com/articles/how-heroku-works#deploying-applications) pour déployer le code de votre machine locale vers ses serveurs cloud ⚠️

```
$ git init
```

En tant qu'étape finale, vous pouvez créer un fichier README.md à modifier ultérieurement.

```
$ echo "Edit me later" > README.md
```

**2. Se connecter à l'interface de ligne de commande Heroku et créer un nouveau projet**

Vous pouvez vous connecter à Heroku en utilisant l'interface de ligne de commande Heroku (CLI). Vous devrez avoir un compte Heroku gratuit pour cela.

Il y a deux options ici. Par défaut, Heroku vous permet de vous connecter via le navigateur web. L'ajout du drapeau `-i` vous permet de vous connecter via la ligne de commande.

```
$ heroku login -i
```

Maintenant, vous pouvez créer un nouveau projet Heroku. J'ai appelé le mien `lorem-ipsum-demo`.

```
$ heroku create lorem-ipsum-demo
```

Nommer votre projet :

* Heroku générera un nom aléatoire pour votre projet si vous n'en spécifiez pas un dans la commande.
* Le nom fera partie de l'URL que vous pouvez utiliser pour accéder à votre projet, alors choisissez-en un que vous aimez. 
* Cela signifie également que vous devez choisir un nom de projet unique que personne d'autre n'a utilisé.
* Il est possible de renommer votre projet plus tard (donc ne vous inquiétez pas trop d'avoir le nom parfait tout de suite).

**3. Initialiser un nouveau projet npm et installer Express.js**

Ensuite, vous pouvez initialiser un nouveau projet npm en créant un fichier package.json. Utilisez la commande ci-dessous pour cela.

⚠️ Cette étape est cruciale. Heroku repose sur la fourniture d'un fichier package.json pour savoir qu'il s'agit d'un projet Node.js lors de la construction de votre application ⚠️

```
$ npm init -y
```

Ensuite, [installez Express](https://expressjs.com/en/starter/installing.html). Express est un framework de serveur largement utilisé pour NodeJS.

```
$ npm install express --save
```

Enfin, vous êtes prêt à commencer à coder !

### Écrire un serveur Express simple

L'étape suivante consiste à créer un fichier appelé `app.js`, qui exécute un serveur Express localement.

```
$ touch app.js
```

Ce fichier sera le point d'entrée de l'application lorsqu'elle sera prête. Cela signifie que la seule commande nécessaire pour lancer l'application sera :

```
$ node app.js
```

Mais d'abord, vous devez écrire du code dans le fichier.

**4. Modifier le contenu de app.js**

Ouvrez `app.js` dans votre éditeur préféré. Écrivez le code montré ci-dessous et cliquez sur enregistrer.

```javascript
// créer une application express
const express = require("express")
const app = express()

// utiliser le middleware express-static
app.use(express.static("public"))

// définir la première route
app.get("/", function (req, res) {
  res.send("<h1>Bonjour le monde !</h1>")
})

// démarrer le serveur pour écouter les requêtes
app.listen(process.env.PORT || 3000, 
	() => console.log("Le serveur est en cours d'exécution..."));
```

Les commentaires devraient aider à indiquer ce qui se passe. Mais décomposons rapidement le code pour mieux le comprendre :

* Les deux premières lignes nécessitent simplement le module Express et créent une instance d'une application Express.
* La ligne suivante nécessite l'utilisation du middleware `express.static`. Cela vous permet de servir des fichiers statiques (tels que HTML, CSS et JavaScript) depuis le répertoire que vous spécifiez. Dans ce cas, les fichiers seront servis depuis un dossier appelé `public`.
* La ligne suivante utilise `app.get()` pour définir une route URL. Toute requête URL vers l'URL racine sera répondue avec un simple message HTML.
* La partie finale démarre le serveur. Il recherche soit le port que Heroku utilisera, soit utilise par défaut le port 3000 si vous exécutez localement.

⚠️ L'utilisation de `process.env.PORT || 3000` dans la dernière ligne est importante pour déployer votre application avec succès ⚠️

Si vous enregistrez `app.js` et démarrez le serveur avec :

```
$ node app.js
```

Vous pouvez visiter [localhost:3000](http://localhost:3000/) dans votre navigateur et voir par vous-même que le serveur est en cours d'exécution.

### Créer vos fichiers statiques

L'étape suivante consiste à créer vos fichiers statiques. Ce sont les fichiers HTML, CSS et JavaScript que vous servirez chaque fois qu'un utilisateur visite votre projet.

Rappelez-vous dans `app.js` que vous avez indiqué au middleware `express.static` de servir les fichiers statiques depuis le répertoire `public`.

La première étape est bien sûr de créer un tel répertoire et les fichiers qu'il contiendra.

```
$ mkdir public
$ cd public
$ touch index.html styles.css script.js
```

**5. Modifier le fichier HTML**

Ouvrez `index.html` dans votre éditeur de texte préféré. Ce sera la structure de base de la page que vous servirez à vos visiteurs.

L'exemple ci-dessous crée une simple page d'accueil pour un générateur de [Lorem Ipsum](https://en.wikipedia.org/wiki/Lorem_ipsum), mais vous pouvez être aussi créatif que vous le souhaitez ici.

```html
<!DOCTYPE html>
<head>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
	<link href="https://fonts.googleapis.com/css?family=Alegreya|Source+Sans+Pro&display=swap" rel="stylesheet">
	<link rel="stylesheet" type="text/css" href="styles.css">
</head>
<html>
<body>
<h1>Générateur de Lorem Ipsum</h1>
  <p>Combien de paragraphes souhaitez-vous générer ?</p>
  <input type="number" id="quantity" min="1" max="20" value="1">
  <button id="generate">Générer</button>
  <button id="copy">Copier !</button>
<div id="lorem">
</div>
<script type="text/javascript" src="script.js"></script>
</body>
</html>
```

**6. Modifier le fichier CSS**

Ensuite, modifiez le fichier CSS `styles.css`. Assurez-vous qu'il est lié dans votre fichier HTML.

Le CSS ci-dessous est pour l'exemple Lorem Ipsum. Mais encore une fois, n'hésitez pas à être aussi créatif que vous le souhaitez.

```css
h1 {
	font-family: 'Alegreya' ;
}

body {
	font-family: 'Source Sans Pro' ;
	width: 50%;
	margin-left: 25%;
	text-align: justify;
	line-height: 1.7;
	font-size: 18px;
}

input {
	font-size: 18px;
	text-align: center;
}

button {
	font-size: 18px;
	color: #fff;
}

#generate {
	background-color: #09f;
}

#copy {
	background-color: #0c6;
}
```

**7. Modifier le fichier JavaScript**

Enfin, vous pourriez vouloir modifier le fichier JavaScript `script.js`. Cela vous permettra de rendre votre page plus interactive.

Le code ci-dessous définit deux fonctions de base pour le générateur de Lorem Ipsum. Oui, j'ai utilisé [JQuery](https://jquery.com/) - c'est rapide et facile à utiliser.

```javascript
$("#generate").click(function(){
	var lorem = $("#lorem");
	lorem.html("");
	var quantity = $("#quantity")[0].valueAsNumber;
	var data = ["Lorem ipsum", "quia dolor sit", "amet", "consectetur"];
	for(var i = 0; i < quantity; i++){
		lorem.append("<p>"+data[i]+"</p>");
	}
})

$("#copy").click(function() {
	var range = document.createRange();
	range.selectNode($("#lorem")[0]);
	window.getSelection().removeAllRanges();
	window.getSelection().addRange(range);
	document.execCommand("copy");
	window.getSelection().removeAllRanges();
	}
)
```

Notez que ici, la liste `data` est tronquée pour faciliter la démonstration. Dans l'application réelle, il s'agit d'une liste beaucoup plus longue de paragraphes complets. Vous pouvez voir le fichier entier dans le dépôt, ou consulter [ici la source originale](http://www.thelatinlibrary.com/cicero/fin1.shtml).

### Déployer votre application

Après avoir écrit votre code statique et vérifié que tout fonctionne comme prévu, vous pouvez vous préparer à déployer sur Heroku.

Cependant, il y a encore quelques choses à faire.

**8. Créer un Procfile**

Heroku aura besoin d'un Procfile pour savoir comment exécuter votre application.

Un Procfile est un "fichier de processus" qui indique à Heroku quelle commande exécuter afin de gérer un processus donné. Dans ce cas, la commande indiquera à Heroku comment démarrer votre serveur pour écouter sur le web.

Utilisez la commande ci-dessous pour créer le fichier.

⚠️ Cette étape est importante, car sans un Procfile, Heroku ne peut pas mettre votre serveur en ligne. ⚠️

```
$ echo "web: node app.js" > Procfile
```

Remarquez que le Procfile n'a pas d'extension de fichier (par exemple, ".txt", ".json"). 

De plus, voyez comment la commande `node app.js` est la même que celle utilisée localement pour exécuter votre serveur.

**9. Ajouter et commiter les fichiers à Git**

Rappelez-vous que vous avez initié un dépôt Git lors de la configuration. Peut-être avez-vous ajouté et commité des fichiers au fur et à mesure.

Avant de déployer sur Heroku, assurez-vous d'ajouter tous les fichiers pertinents et de les commiter.

```
$ git add .
$ git commit -m "prêt à déployer"
```

La dernière étape consiste à pousser vers votre branche principale Heroku.

```
$ git push heroku master
```

Vous devriez voir la ligne de commande imprimer une série d'informations alors qu'Heroku construit et déploie votre application.

La ligne à rechercher est : `Verifying deploy... done.`

Cela montre que votre build a réussi.

Maintenant, vous pouvez ouvrir le navigateur et visiter votre-nom-de-projet.herokuapp.com. Votre application sera hébergée sur le web pour que tous puissent la visiter !

### Récapitulatif rapide

Voici les étapes à suivre pour déployer une application Express simple sur Heroku :

1. Créer un nouveau répertoire et initialiser un dépôt Git
2. Se connecter à l'interface de ligne de commande Heroku et créer un nouveau projet
3. Initialiser un nouveau projet npm et installer Express.js
4. Modifier le contenu de app.js
5. Modifier les fichiers statiques HTML, CSS et JavaScript
6. Créer un Procfile
7. Ajouter et commiter à Git, puis pousser vers votre branche principale Heroku

### Choses à vérifier si votre application ne fonctionne pas

Parfois, malgré les meilleures intentions, les tutoriels sur Internet ne fonctionnent pas exactement comme vous l'aviez prévu.

Les étapes ci-dessous devraient aider à déboguer certaines erreurs courantes que vous pourriez rencontrer :

* Avez-vous initialisé un dépôt Git dans votre dossier de projet ? Vérifiez si vous avez exécuté `git init` plus tôt. Heroku repose sur Git pour déployer le code de votre machine locale.
* Avez-vous créé un fichier package.json ? Vérifiez si vous avez exécuté `npm init -y` plus tôt. Heroku nécessite un fichier package.json pour reconnaître qu'il s'agit d'un projet Node.js.
* Le serveur est-il en cours d'exécution ? Assurez-vous que votre Procfile utilise le nom de fichier correct pour démarrer le serveur. Vérifiez que vous avez `web: node app.js` et non `web: node index.js`.
* Heroku sait-il sur quel port écouter ? Vérifiez que vous avez utilisé `app.listen(process.env.PORT || 3000)` dans votre fichier app.js.
* Vos fichiers statiques contiennent-ils des erreurs ? Vérifiez-les en les exécutant localement et voyez s'il y a des bugs.

Merci d'avoir lu - si vous êtes arrivé jusqu'ici, vous pourriez vouloir [consulter la version finale](http://lorem-ipsum-demo.herokuapp.com/) du projet de démonstration.