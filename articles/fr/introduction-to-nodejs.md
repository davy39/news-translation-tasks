---
title: Comment commencer avec Node.js – Guide du débutant pour Node
subtitle: ''
author: Arash Arora
co_authors: []
series: null
date: '2022-07-11T21:31:18.000Z'
originalURL: https://freecodecamp.org/news/introduction-to-nodejs
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/1200px-Node.js_logo.svg.png
tags:
- name: beginner
  slug: beginner
- name: JavaScript
  slug: javascript
- name: node
  slug: node
- name: Node.js
  slug: nodejs
seo_title: Comment commencer avec Node.js – Guide du débutant pour Node
seo_desc: 'By Arash Arora

  Node.js is a JavaScript runtime that extends its capability to the server-side.
  It is built on Chrome’s V8 JavaScript Engine.

  Node is an event-driven, non-blocking IO model. This means it''s asynchronous, and
  doesn''t block itself for on...'
---

Par Arash Arora

Node.js est un environnement d'exécution JavaScript qui étend ses capacités au côté serveur. Il est construit sur le moteur V8 JavaScript de Chrome.

Node est un modèle d'E/S piloté par événements et non bloquant. Cela signifie qu'il est asynchrone et ne se bloque pas pour une seule requête (mais passe immédiatement à la requête suivante). Cela rend Node extrêmement rapide et efficace.

Par piloté par événements, cela signifie que dès que Node démarre, il initialise toutes les variables et fonctions et attend qu'un événement se produise.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-195.png align="left")

NPM signifie Node Package Manager, qui vous aide à gérer vos packages pour Node. NPX signifie Node Package Execute, et il peut exécuter n'importe quel package npm sans même l'installer.

Pour télécharger npm, rendez-vous sur [https://nodejs.org/en/download/](https://nodejs.org/en/download/).

## Comment écrire votre premier programme Node.js (Hello World)

Créez un fichier appelé hello_world.js dans votre dossier de projet

Ouvrez ensuite le fichier dans votre éditeur de code comme VS Code. Tapez le code `console.log("Hello World");` dans votre éditeur.

Ouvrez le terminal et naviguez jusqu'à l'emplacement du fichier.

Tapez maintenant `node hello_world.js`.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-196.png align="left")

## Comment importer les modules principaux de Node

Commençons par le package de base, qui est **fs (file system)**. Vous l'utilisez pour créer, lire et modifier des fichiers.

Pour importer le module fs, tapez cette commande : `const fs = require("fs");`.

Pour utiliser une fonction de ce module, vous pouvez vous référer à la [documentation](https://nodejs.org/docs/latest-v17.x/api/fs.html#file-system).

Pour créer un fichier, nous pouvons utiliser `fs.writeFileSync(filename, content);`.

```js
const fs = require("fs");
fs.writeFileSync("file.txt", "Hi there..");
```

![Image](https://miro.medium.com/max/446/1*KzqmGo9SE7R3XPYOS-3LXg.png align="left")

Pour ajouter quelque chose dans le même fichier, nous pouvons utiliser ceci :

```js
fs.appendFileSync(filename, content);
```

![Image](https://miro.medium.com/max/842/1*dOqUqcuJ5a5vl_BQ_E0dSg.png align="left")

## Comment installer les packages NPM

Nous allons maintenant utiliser un package npm très basique appelé **superheroes** (qui est une liste de super-héros aléatoires) pour vous aider à comprendre comment npm fonctionne.

Pour installer un package npm, nous pouvons utiliser cette commande dans le terminal :

```plaintext
npm install superheroes
```

Pour importer le package installé, tapez `const sh = require("superheroes");`.

Pour afficher le nom d'un super-héros aléatoire, utilisez cette commande :

```js
console.log(sh.random());
```

![Image](https://miro.medium.com/max/1400/1*WfHNl2GDgyXBEwfV6oV0GQ.png align="left")

Essayons un autre package. Nous allons maintenant installer l'un des packages npm les plus utilisés appelé **"chalk"** — il style les chaînes de texte dans le terminal.

Pour installer le package chalk (nous installerons la version 2.4.2 car elle nous permet d'importer le package en utilisant la méthode **require**), tapez la commande suivante :

```js
npm install chalk@2.4.2
```

Pour styliser la chaîne de texte, utilisez cette commande pour choisir la couleur de la chaîne :

```js
chalk.color(text)
```

![Image](https://miro.medium.com/max/1400/1*AQ5TX0vxzPn5N0lzrSBbJw.png align="left")

Vous pouvez en savoir plus sur le [package chalk ici](https://www.npmjs.com/package/chalk).

## Comment initier NPM dans notre programme

Pour initier NPM dans notre programme, nous pouvons utiliser la commande suivante :

```js
npm init
```

Appuyez ensuite sur Entrée ou répondez aux questions en conséquence.

![Image](https://miro.medium.com/max/1400/1*G_SVRqNdjuuWssQANvZgbw.png align="left")

Ou vous pouvez directement utiliser la commande `npm init -y` (équivalent à appuyer sur Entrée pour toutes les questions).

![Image](https://miro.medium.com/max/1400/1*CafNbhzEhvGAayNHnpb29A.png align="left")

Cela entraînera la création du fichier **package.json** :

![Image](https://miro.medium.com/max/1400/1*hYaMdTgcLdABQ1qqjQdpRQ.png align="left")

### Qu'est-ce que package.json ?

package.json est le cœur de tout projet Nodejs. Il conserve un enregistrement de toutes les dépendances (packages NPM) et contient les métadonnées de chaque projet.

Si quelqu'un d'autre télécharge le projet, ce fichier l'aidera à installer toutes les dépendances nécessaires pour exécuter le programme.

## Comment utiliser Moment.js — un package NPM

C'est l'un des packages npm les plus utilisés. Vous pouvez l'utiliser pour analyser et valider les dates.

Pour installer le package, exécutez cette commande :

```js
npm i moment
```

Importez le package comme ceci :

```js
const moment = require("moment");
```

Pour créer un objet Date pour obtenir la date et l'heure actuelles (méthode JavaScript), exécutez ce code :

```js
const time = new Date();
```

Maintenant, pour analyser ou formater la date, nous utiliserons le package **moment** :

```js
const parsedTime = moment(time).format("h:mm:ss");
```

Affichez l'heure analysée comme ceci :

```js
console.log(parsedTime);
```

![Image](https://miro.medium.com/max/1400/1*V3hJ24cmTASx9k6Rv83gXg.png align="left")

Voici le package.json pour ce projet qui inclut tous les packages de dépendances — **moment** dans ce cas.

![Image](https://miro.medium.com/max/1400/1*kKFpiaEOtsRbxN67do4HDw.png align="left")

Nous avons également **node_modules** dans le dossier du projet. Ce dossier contient toutes les dépendances dont notre projet dépend, y compris moment et d'autres packages dont moment dépend.

![Image](https://miro.medium.com/max/454/1*-mxxdXnGzLxG98LE2ebMDQ.png align="left")

**package-lock.json** est un autre fichier dans notre dossier de projet qui contient toutes les informations concernant le nom, les dépendances, la version des dépendances et la version verrouillée du projet.

Il décrit l'arborescence exacte qui a été générée pour permettre aux installations ultérieures d'avoir l'arborescence identique.

![Image](https://miro.medium.com/max/1400/1*b1VMBTQ3HtQtnaHUWGY8iQ.png align="left")

# Comment utiliser Express JS — un Framework NodeJS

Express est un framework d'application web Node.js qui offre une gamme complète de fonctionnalités pour les applications web et mobiles.

### Comment installer Express

Pour installer Express, exécutez cette commande :

```js
npm install express
```

Ensuite, vous devrez importer Express comme ceci :

```js
const express = require("express");
```

### Comment créer une application Express

Pour créer une application Express, exécutez simplement cette commande :

```js
const app = express()
```

### Comment démarrer un serveur sur le port 3000

```js
app.listen(3000, () => { 
    console.log("Server running on port 3000");
}
```

![Image](https://miro.medium.com/max/1400/1*jD3FvRLcd_j2MuZ0U6_bXw.png align="left")

Vous pouvez maintenant ouvrir [**http://localhost:3000**](http://localhost:3000/) pour atteindre votre serveur créé

![Image](https://miro.medium.com/max/844/1*IMLmUArtV_ctmiAG18TnJg.png align="left")

D'accord, donc "cannot get /" signifie qu'il n'y a pas encore de route définie "/".

Pour définir la route "/", nous utilisons la fonction `app.get()`.

La fonction **app.get (route, fonction de rappel)** est utilisée pour gérer toutes les requêtes GET.

La fonction de rappel a deux arguments, **req** et **res**, qui font référence aux requêtes HTTP et à la réponse souhaitée, respectivement. Les noms des arguments (req, res) ne sont pas fixes et peuvent être nommés comme vous le souhaitez.

```js
app.get("/", (req,res) => { 
    // app.get pour gérer les requêtes GET
    // req - requête http, res - réponse souhaitée
    res.send("Hello World"); // envoyer Hello World à cette route
}
```

## Comment créer un programme Hello World dans Express

Dans cette section, nous allons créer le programme de base Hello World dans Express.

```js
const express = require("express");
const app = express();
app.get("/", (req, res) => {  
    res.send("hello world");
});
app.listen(3000, () => {  
    console.log("Server running on 3000");
});
```

Et voici le résultat

![Image](https://miro.medium.com/max/1060/1*uRqmENgESv8cdq-0oSaX8A.png align="left")

## Comment rendre des fichiers statiques dans Express

Cette section nous introduit au concept de rendu de fichiers statiques en utilisant Express.

Tout d'abord, vous devrez créer un nouveau dossier de projet. Ensuite, vous initialiserez npm en utilisant `npm init -y`.

Installez le package Express `npm i express` et créez un fichier appelé app.js.

Ensuite, vous créerez une application et écouterez ou démarrerez le serveur sur le port 3000.

```js
const express = require("express");
const app = express();
app.listen(3000, () => {  
    console.log("Server running on 3000");
}
```

Pour rendre des pages web statiques telles que HTML, CSS et JS, créez un dossier nommé public dans le répertoire racine.

Comme nous nous concentrons uniquement sur le backend, nous ne passerons pas beaucoup de temps sur le frontend et créerons uniquement un fichier HTML dans le dossier public.

![Image](https://miro.medium.com/max/1142/1*-OiGmKZaz7GKc3NdNVjZdg.png align="left")

Nous allons maintenant importer le module **path** et joindre les chemins spécifiés en un seul :

```js
const path = require("path");
```

Pour rendre ces fichiers, nous devons utiliser la commande suivante :

```js
app.use(express.static(path.join(__dirname, "public")));
```

**__dirname →** retourne le répertoire actuel

```js
const express = require("express");
const path = require("path");
const app = new express();
app.use(express.static(path.join(__dirname, "/public")));
app.listen(3000, () => {  
    console.log("Server running on 3000");
});
```

Et voici le résultat :

![Image](https://miro.medium.com/max/1034/1*2U5Qi3XKOaNF0MjXSTo0tg.png align="left")

## Comment rendre des fichiers dynamiques dans Express

Dans cette section, nous allons apprendre à rendre des fichiers dynamiques dans lesquels nous pouvons utiliser des valeurs d'un objet d'entrée.

Pour rendre des pages web dynamiques, il existe de nombreux modèles tels que pug, handlebars, ejs, etc. Ces modèles nous permettent d'injecter des données dynamiques, des conditions si et des boucles au moment de l'exécution.

Mais ici, nous nous concentrerons sur handlebars.

Installez les packages (express et hbs) :

```js
npm i hbs express
```

Créez un fichier nommé app.js et importez les packages comme ceci :

```js
const express = require("express");
const hbs = require("hbs");
const path = require("path");
```

Créez une application Express et écoutez sur le port 3000 :

```js
const app = express();
app.listen(3000, (req,res) => {  
    console.log("Server running on 3000");
}
```

Pour que handlebars fonctionne, nous devons définir le moteur de vue comme hbs.

```js
app.set("view engine", "hbs");
```

Le moteur de vue nous permet de rendre des pages web dynamiques en utilisant le modèle spécifié.

Le moteur de vue recherche généralement le dossier "views" dans le dossier racine. Mais pour éviter les erreurs, nous mentionnerons le chemin de "views" en utilisant la commande suivante :

```js
app.set("views", path.join(__dirname, "/views"));
```

Créez maintenant un dossier **views** dans le répertoire racine. Sous celui-ci, créez un fichier appelé index.hbs (.hbs est l'extension de handlebars) et insérez le code HTML suivant :

### index.hbs

```html
<html>  
    <head> 
        <title>Dynamic Rendering</title> 
    </head>
    <body>  
      <h1>Dynamic Rendering</h1>   
      <p>{{author}}</p> <!--dynamic data recieved from server-->
    </body>
</html>
```

`{{author}}` — c'est la syntaxe pour insérer des données dynamiques

Pour rendre le fichier index.hbs, nous créerons une fonction app.get pour gérer la requête GET sur la route "/" et envoyer les données dynamiques **author**.

```js
app.get("/", (req, res) => { 
    res.render("index", {    
        author: "Arash Arora", 
    });
});
```

`res.render` est la fonction pour rendre la vue. Ici, nous devons passer deux arguments. Le premier est le nom du fichier sans l'extension et le second est l'objet des variables locales, par exemple **author**.

### fichier app.js

```js
const express = require("express");
const hbs = require("hbs");
const path = require("path");
const app = express();
app.set("view engine", "hbs");
app.set("views", path.join(__dirname, "/views"));
app.get("/", (req, res) => {  
    res.render("index", {    
        author: "Arash Arora", 
    });
});
app.listen(3000, (req, res) => { 
    console.log("Server listening on 3000");
});
```

### Structure du dossier

![Image](https://miro.medium.com/max/502/1*7xz9Fj17mTS5pZhxzf2dvw.png align="left")

Et voici le résultat :

![Image](https://miro.medium.com/max/824/1*JQt1mgjLTU-LJJ0XS7UH3A.png align="left")

# Comment créer des modèles avancés avec Handlebars

C'est ici que nous allons apprendre les composants réutilisables. Auparavant, nous devions construire des composants identiques pour chaque page lorsqu'il s'agissait d'en-têtes et de pieds de page.

Mais comme il y a tant de tâches répétitives, le templating avancé est le sauveur. Ce concept stipule que nous allons simplement créer un composant qui sera utilisé partout où nous en avons besoin.

### Handlebars a introduit le concept de Partials

Les Partials sont des fichiers handlebar réguliers que d'autres modèles peuvent appeler. Les Partials sont un concept de templating largement utilisé qui n'est pas spécifique à Handlebars.

Pour construire des modèles susceptibles d'être réutilisés, vous pouvez les isoler dans leurs fichiers (un Partial), puis les utiliser dans divers modèles. Vous pouvez considérer les partials comme une technique simple pour modulariser vos modèles.

Suivez ces étapes pour créer des partials :

* Initialisez npm → `npm init -y`
    
* Installez les packages requis, Express et hbs → `npm i express hbs`
    
* Créez votre dossier templates
    
* Créez deux dossiers supplémentaires dans le dossier templates : **partials et views**
    
* Créez maintenant un fichier **app.js**
    

![Image](https://miro.medium.com/max/472/1*98jLDll1IWq-vd8H0ieNCg.png align="left")

*La structure du dossier doit être similaire*

Créons deux fichiers partials : header.hbs et footer.hbs. Et nous ajouterons également deux vues, index.hbs et about.hbs.

![Image](https://miro.medium.com/max/422/1*E32yq-EHCLFfUFzbgIbJJg.png align="left")

### index.hbs

```html
<html lang="en">  
    <head>   
        <title>Advanced Templating</title>  
    </head>  
    <body>    
        {{>header}} <!--include the header component-->
        <p>I'm a savior</p>    
        {{>footer}} <!-- include the footer component -->
    </body>
</html>
```

### about.hbs

```html
<html lang="en">  
    <head>    
        <title>Advanced Templating -- About</title> 
    </head>
    <body>   
        {{>header}}   
        <p>Handlebars</p>    
        {{>footer}} 
    </body>
</html>
```

### header.hbs

```html
<header>  
    <h1>Advanced Templating</h1> 
    <h3>{{title}}</h3><!--dynamic data received from server-->
    <a href="/">Home</a> 
    <a href="/about">About</a>
</header>
```

### footer.hbs

```html
<footer>  
    <p>Created by {{name}}</p> <!--name -> dynamic data -->
</footer>
```

### app.js

```javascript
const express = require("express");
const hbs = require("hbs");
const path = require("path");
const app = express();
app.set("view engine", "hbs");
app.set("views", path.join(__dirname, "/templates/views"));
hbs.registerPartials(path.join(__dirname, "/templates/partials"));
app.get("/", (req, res) => {  
    res.render("index", {    
        title: "Home",    
        name: "Arash Arora",  
    });
});
app.get("/about", (req, res) => {  
    res.render("about", {    
        title: "About",    
        name: "Arash Arora",  
    });
});
app.listen(3000, () => {  
    console.log("Listening on port 3000");
});
```

Tout est identique à ce que j'ai expliqué dans la section sur le rendu des fichiers dynamiques dans Express — sauf qu'ici nous devons **enregistrer les partials** pour utiliser les partials.

### Comment enregistrer les partials

```js
hbs.registerPartials(path_to_partials)
```

Comme nous avons créé le répertoire partials dans le dossier templates, voici le chemin des partials :

```js
hbs.registerPartials(path.join(__dirname, "/templates/partials"));
```

# Conclusion

Dans cet article, nous avons couvert Node.js de la théorie à la pratique. Bien que Node.js soit un sujet vaste que vous ne pouvez pas apprendre entièrement à partir d'un seul article plus court, j'ai fait de mon mieux pour couvrir certaines des fonctionnalités essentielles pour vous aider à commencer le voyage.

En résumé, nous avons discuté de ce qu'est Node.js, qui est un environnement d'exécution JavaScript non bloquant, piloté par événements, asynchrone et utilisant un seul thread pour effectuer des opérations. Nous avons également discuté du framework d'application web Node.js minimal et flexible le plus utilisé, Express.

Ensuite, nous avons parlé de NPM, NPX de Node.js et du rendu des données statiques et dynamiques.

En fin de compte, Node.js est une technologie fantastique à connaître, et les possibilités sont infinies grâce à sa vaste communauté.