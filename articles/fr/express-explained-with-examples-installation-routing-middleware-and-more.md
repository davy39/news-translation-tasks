---
title: Express Expliqué avec des Exemples - Installation, Routage, Middleware, et
  Plus
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/express-explained-with-examples-installation-routing-middleware-and-more
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cfe740569d1a4ca354a.jpg
tags:
- name: Express
  slug: express
- name: node
  slug: node
- name: Node.js
  slug: nodejs
- name: toothbrush
  slug: toothbrush
seo_title: Express Expliqué avec des Exemples - Installation, Routage, Middleware,
  et Plus
seo_desc: 'Express

  When it comes to build web applications using Node.js, creating a server can take
  a lot of time. Over the years Node.js has matured enough due to the support from
  community. Using Node.js as a backend for web applications and websites help th...'
---

## **Express**

Lorsqu'il s'agit de construire des applications web en utilisant Node.js, la création d'un serveur peut prendre beaucoup de temps. Au fil des ans, Node.js a mûri grâce au soutien de la communauté. Utiliser Node.js comme backend pour des applications web et des sites web aide les développeurs à commencer à travailler sur leur application ou produit rapidement.

Dans ce tutoriel, nous allons examiner Express, qui est un framework Node.js pour le développement web qui offre des fonctionnalités comme le routage, le rendu et le support des API REST.

## **Qu'est-ce qu'Express ?**

Express est le framework Node.js le plus populaire car il nécessite un minimum de configuration pour démarrer une application ou une API et est rapide et non contraignant en même temps. En d'autres termes, il n'impose pas sa propre philosophie selon laquelle une application ou une API doit être construite d'une manière spécifique, contrairement à Rails et Django. Sa flexibilité peut être mesurée par le nombre de modules `npm` disponibles, ce qui le rend pluggable en même temps. Si vous avez des connaissances de base en HTML, CSS et JavaScript et que vous comprenez comment Node.js fonctionne en général, vous pourrez commencer avec Express en un rien de temps.

Express a été développé par TJ Holowaychuk et est maintenant maintenu par la fondation Node.js et des développeurs open source. Pour commencer le développement avec Express, vous devez avoir Node.js et npm installés. Vous pouvez installer [Node.js](https://nodejs.org/en/) sur votre machine locale et avec lui vient l'utilitaire de ligne de commande `npm` qui nous aidera à installer des plugins ou des dépendances plus tard dans notre projet.

Pour vérifier si tout est installé correctement, veuillez ouvrir votre terminal et taper :

```shell
node --version
v5.0.0
npm --version
3.5.2
```

Si vous obtenez le numéro de version au lieu d'une erreur, cela signifie que vous avez installé Node.js et npm avec succès.

## **Pourquoi utiliser Express ?**

Avant de commencer avec le mécanisme d'utilisation d'Express comme framework backend, explorons d'abord pourquoi nous devrions envisager de l'utiliser ou les raisons de sa popularité.

* Express vous permet de construire des applications web et mobiles à page unique, multi-pages et hybrides. Une autre utilisation courante du backend est de fournir une API pour un client (qu'il soit web ou mobile).
* Il est livré avec un moteur de template par défaut, Jade, qui aide à faciliter le flux de données dans une structure de site web et prend en charge d'autres moteurs de template.
* Il prend en charge MVC (Modèle-Vue-Contrôleur), une architecture très courante pour concevoir des applications web.
* Il est multiplateforme et n'est pas limité à un système d'exploitation particulier.
* Il tire parti du modèle single-threaded et asynchrone de Node.js.

Chaque fois que nous créons un projet en utilisant `npm`, notre projet doit avoir un fichier `package.json`.

### **Création de package.json**

Un fichier JSON (JavaScript Object Notation) contient toutes les informations sur un projet Express. Le nombre de modules installés, le nom du projet, la version et d'autres méta-informations. Pour ajouter Express comme module dans notre projet, nous devons d'abord créer un répertoire de projet, puis créer un fichier package.json.

```shell
mkdir express-app-example
cd express-app-example
npm init --yes
```

Cela générera un fichier `package.json` à la racine du répertoire du projet. Pour installer un module à partir de `npm`, nous devons avoir un fichier `package.json` existant dans ce répertoire.

```json
{
  "name": "express-web-app",
  "version": "0.1.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "license": "MIT"
}
```

### **Installation d'Express**

Maintenant que nous avons le fichier `package.json`, nous pouvons installer Express en exécutant la commande :

```shell
npm install --save express
```

Nous pouvons confirmer qu'Express est correctement installé de deux manières. Premièrement, il y aura une nouvelle section dans le fichier `package.json` nommée `dependencies` sous laquelle notre Express existe :

```json
{
  "name": "express-web-app",
  "version": "0.1.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "license": "MIT",
  "dependencies": {
    "express": "4.16.0"
  }
}
```

La deuxième manière est qu'un nouveau dossier appelé `node_modules` est soudainement apparu à la racine de notre répertoire de projet. Ce dossier stocke les packages que nous installons localement dans notre projet.

## **Construction d'un Serveur avec Express**

Pour utiliser notre package installé pour le framework Express et créer une application serveur simple, nous allons créer le fichier `index.js` à la racine du répertoire de notre projet.

```javascript
const express = require('express');
const app = express();

app.get('/', (req, res) => res.send('Hello World!'));

app.listen(3000, () => console.log('Example app listening on port 3000!'));
```

Pour démarrer le serveur, allez dans votre terminal et tapez :

```shell
node index.js
```

Cela démarrera le serveur. Cette application minimale écoutera sur le port 3000. Nous faisons une requête via notre navigateur sur `http://localhost:3000` et notre serveur répondra avec `Hello World` auquel le navigateur est le client et le message sera affiché là.

La première ligne de notre code utilise la fonction `require` pour inclure le module `express`. C'est ainsi que nous incluons et utilisons un package installé à partir de npm dans n'importe quel fichier JavaScript de notre projet. Avant de commencer à utiliser Express, nous devons définir une instance de celui-ci qui gère la requête et la réponse du serveur au client. Dans notre cas, c'est la variable `app`.

`app.get()` est une fonction qui indique au serveur quoi faire lorsqu'une requête `get` à la route donnée est appelée. Elle a une fonction de rappel `(req, res)` qui écoute l'objet de requête entrant `req` et répond en conséquence en utilisant l'objet de réponse `res`. Les objets `req` et `res` sont mis à notre disposition par le framework Express.

L'objet `req` représente la requête HTTP et a des propriétés pour la chaîne de requête, les paramètres, le corps et les en-têtes HTTP. L'objet `res` représente la réponse HTTP qu'une application Express envoie lorsqu'elle reçoit une requête HTTP. Dans notre cas, nous envoyons un texte `Hello World` chaque fois qu'une requête est faite à la route `/`.

Enfin, `app.listen()` est la fonction qui démarre un port et un hôte, dans notre cas `localhost` pour les connexions afin d'écouter les requêtes entrantes d'un client. Nous pouvons définir le numéro de port tel que `3000`.

## **Anatomie d'une Application Express**

Une structure typique d'un fichier serveur Express contiendra probablement les parties suivantes :

**Dépendances**

Importation des dépendances telles qu'Express lui-même. Ces dépendances sont installées en utilisant `npm` comme nous l'avons fait dans l'exemple précédent.

**Instanciations**

Ce sont les déclarations pour créer un objet. Pour utiliser Express, nous devons instancier la variable `app` à partir de celui-ci.

**Configurations**

Ces déclarations sont les paramètres personnalisés de l'application qui sont définis après les instanciations ou définis dans un fichier séparé (plus sur cela lorsque nous discuterons de la structure du projet) et requis dans notre fichier serveur principal.

**Middleware**

Ces fonctions déterminent le flux du cycle requête-réponse. Elles sont exécutées après chaque requête entrante. Nous pouvons également définir des fonctions middleware personnalisées. Nous avons une section sur celles-ci ci-dessous.

**Routes**

Ce sont les points de terminaison définis dans notre serveur qui aident à effectuer des opérations pour une requête client particulière.

**Bootstrapping Serveur**

La dernière chose qui est exécutée dans un serveur Express est la fonction `app.listen()` qui démarre notre serveur.

Nous allons maintenant commencer à discuter des sections que nous n'avons pas encore abordées.

## **Routage**

Le routage fait référence à la manière dont une application côté serveur répond à une requête client à un point de terminaison particulier. Ce point de terminaison se compose d'un URI (un chemin tel que `/` ou `/books`) et d'une méthode HTTP telle que GET, POST, PUT, DELETE, etc.

Les routes peuvent être soit de bonnes vieilles pages web, soit des points de terminaison d'API REST. Dans les deux cas, la syntaxe est similaire, une route peut être définie comme suit :

```javascript
app.METHOD(PATH, HANDLER);
```

Les routeurs sont utiles pour séparer les préoccupations telles que les différents points de terminaison et garder les portions pertinentes du code source ensemble. Ils aident à construire un code maintenable. Toutes les routes sont définies avant l'appel de la fonction `app.listen()`. Dans une application Express typique, `app.listen()` sera la dernière fonction à exécuter.

### **Méthodes de Routage**

HTTP est un protocole standard pour qu'un client et un serveur communiquent. Il fournit différentes méthodes pour qu'un client fasse une requête. Chaque route a au moins une fonction de gestionnaire ou un rappel. Cette fonction de rappel détermine quelle sera la réponse du serveur pour cette route particulière. Par exemple, une route de `app.get()` est utilisée pour gérer les requêtes GET et en retour envoyer un message simple comme réponse.

```javascript
// Route de la méthode GET
app.get('/', (req, res) => res.send('Hello World!'));
```

### **Chemins de Routage**

Un chemin de routage est une combinaison d'une méthode de requête pour définir les points de terminaison auxquels les requêtes peuvent être faites par un client. Les chemins de route peuvent être des chaînes, des motifs de chaînes ou des expressions régulières.

Définissons deux autres points de terminaison dans notre application basée sur un serveur.

```javascript
app.get('/home', (req, res) => {
  res.send('Page d\'accueil');
});
app.get('/about', (req, res) => {
  res.send('À propos');
});
```

Considérez le code ci-dessus comme un site web minimal qui a deux points de terminaison, `/home` et `/about`. Si un client fait une requête pour la page d'accueil, il répondra uniquement avec `Page d\'accueil` et sur `/about`, il enverra la réponse : `Page À propos`. Nous utilisons la fonction `res.send` pour envoyer la chaîne au client si l'une des deux routes définies est sélectionnée.

### **Paramètres de Routage**

Les paramètres de route sont des segments d'URL nommés qui sont utilisés pour capturer les valeurs spécifiées à leur position dans l'URL. L'objet `req.params` est utilisé dans ce cas car il a accès à tous les paramètres passés dans l'URL.

```javascript
app.get('/books/:bookId', (req, res) => {
  res.send(req.params);
});
```

L'URL de la requête du client dans le code source ci-dessus sera `http://localhost:3000/books/23`. Le nom des paramètres de route doit être composé de caractères ([A-Za-z0-9_]). Un cas d'utilisation très général d'un paramètre de routage dans notre application est d'avoir une route 404.

```javascript
// Pour les routes invalides
app.get('*', (req, res) => {
  res.send('404! Il s\'agit d\'une URL invalide.');
});
```

Si nous démarrons maintenant le serveur à partir de la ligne de commande en utilisant `node index.js` et essayons de visiter l'URL : `http://localhost:3000/abcd`. En réponse, nous obtiendrons le message 404.

## **Fonctions Middleware**

Les fonctions middleware sont celles qui ont accès à l'objet de requête (`req`), à l'objet de réponse (`res`) et à la fonction `next` dans le cycle requête-réponse de l'application. L'objectif de ces fonctions est de modifier les objets de requête et de réponse pour des tâches comme l'analyse des corps de requête, l'ajout d'en-têtes de réponse, apporter d'autres modifications au cycle requête-réponse, mettre fin au cycle requête-réponse et appeler la fonction middleware suivante.

La fonction `next` est une fonction dans le routeur Express qui est utilisée pour exécuter les autres fonctions middleware succédant au middleware actuel. Si une fonction middleware n'inclut pas `next()`, cela signifie que le cycle requête-réponse se termine là. Le nom de la fonction `next()` ici est totalement arbitraire et vous pouvez la nommer comme vous le souhaitez, mais il est important de respecter les meilleures pratiques et d'essayer de suivre quelques conventions, surtout si vous travaillez avec d'autres développeurs.

De plus, lors de l'écriture d'un middleware personnalisé, n'oubliez pas d'ajouter la fonction `next()`. Si vous ne mentionnez pas `next()`, le cycle requête-réponse restera bloqué et votre serveur pourrait provoquer un délai d'attente du client.

Créons une fonction middleware personnalisée pour comprendre ce concept. Prenons cet exemple de code :

```javascript
const express = require('express');
const app = express();

// Simple journalisation de l'heure de la requête
app.use((req, res, next) => {
   console.log("Une nouvelle requête reçue à " + Date.now());

   // Cet appel de fonction indique que plus de traitement est
   // requis pour la requête actuelle et est dans le prochain middleware
   // fonction/gestionnaire de route.
   next();  
});

app.get('/home', (req, res) => {
  res.send('Page d\'accueil');
});

app.get('/about', (req, res) => {
  res.send('Page À propos');
});

app.listen(3000, () => console.log('Example app listening on port 3000!'));
```

Pour configurer un middleware, qu'il soit personnalisé ou disponible en tant que module npm, nous utilisons la fonction `app.use()`. Elle a un paramètre optionnel de chemin et un paramètre obligatoire de rappel. Dans notre cas, nous n'utilisons pas le paramètre optionnel de chemin.

```javascript
app.use((req, res, next) => {
  console.log('Une nouvelle requête reçue à ' + Date.now());
  next();
});
```

La fonction middleware ci-dessus est appelée pour chaque requête faite par le client. Lors de l'exécution du serveur, vous remarquerez que pour chaque requête du navigateur sur le point de terminaison `/`, vous serez invité avec un message dans votre terminal :

```shell
Une nouvelle requête reçue à 1467267512545
```

Les fonctions middleware peuvent être utilisées pour une route spécifique. Voir l'exemple ci-dessous :

```javascript
const express = require('express');
const app = express();

// Simple journalisation de l'heure de la requête pour une route spécifique
app.use('/home', (req, res, next) => {
  console.log('Une nouvelle requête reçue à ' + Date.now());
  next();
});

app.get('/home', (req, res) => {
  res.send('Page d\'accueil');
});

app.get('/about', (req, res) => {
  res.send('Page À propos');
});

app.listen(3000, () => console.log('Example app listening on port 3000!'));
```

Cette fois, vous ne verrez une invite similaire que lorsque le client demandera le point de terminaison `/home` puisque la route est mentionnée dans `app.use()`. Rien ne sera affiché dans le terminal lorsque le client demandera le point de terminaison `/about`.

L'ordre des fonctions middleware est important car elles définissent quand appeler quelle fonction middleware. Dans notre exemple ci-dessus, si nous définissons la route `app.get('/home')...` avant le middleware `app.use('/home')...`, la fonction middleware ne sera pas invoquée.

### **Fonctions Middleware Tierces**

Les fonctions middleware sont un modèle utile qui permet aux développeurs de réutiliser du code dans leurs applications et même de le partager avec d'autres sous forme de modules NPM. La définition essentielle du middleware est une fonction avec trois arguments : requête (ou req), réponse (res) et next, que nous avons observés dans la section précédente.

Souvent, dans notre application serveur basée sur Express, nous utiliserons des fonctions middleware tierces. Ces fonctions sont fournies par Express lui-même. Elles sont comme des plugins qui peuvent être installés en utilisant npm et c'est pourquoi Express est flexible.

Certaines des fonctions middleware les plus couramment utilisées dans une application Express sont :

#### **bodyParser**

Il permet aux développeurs de traiter les données entrantes, telles que la charge utile du corps. La charge utile est simplement les données que nous recevons du client pour être traitées. Très utile avec les méthodes POST. Il est installé en utilisant :

```shell
npm install --save body-parser
```

Utilisation :

```javascript
const bodyParser = require('body-parser');

// Pour analyser les données codées en URL
app.use(bodyParser.urlencoded({ extended: false }));

// Pour analyser les données JSON
app.use(bodyParser.json());
```

C'est probablement l'une des fonctions middleware tierces les plus utilisées dans toute application Express.

#### **cookieParser**

Il analyse l'en-tête Cookie et remplit `req.cookies` avec un objet clé par les noms de cookie. Pour l'installer,

```shell
$ npm install --save cookie-parser
```

```javascript
const cookieParser = require('cookie-parser');
app.use(cookieParser());
```

#### **session**

Cette fonction middleware crée un middleware de session avec les options données. Une session est souvent utilisée dans des applications telles que la connexion/inscription.

```shell
$ npm install --save session
```

```javascript
app.use(
  session({
    secret: 'chaine-arbitraire',
    resave: false,
    saveUninitialized: true,
    cookie: { secure: true }
  })
);
```

### **morgan**

Le middleware morgan suit toutes les requêtes et autres informations importantes en fonction du format de sortie spécifié.

```shell
npm install --save morgan
```

```javascript
const logger = require('morgan');
// ... Configurations
app.use(logger('common'));
```

`common` est un format de cas prédéfini que vous pouvez utiliser dans l'application. Il existe d'autres formats prédéfinis tels que tiny et dev, mais vous pouvez également définir votre propre format personnalisé en utilisant les paramètres de chaîne qui sont disponibles pour nous par morgan.

Une liste des fonctions middleware les plus utilisées est disponible à ce [lien](https://expressjs.com/en/resources/middleware.html).

## **Servir des Fichiers Statiques**

Pour servir des fichiers statiques tels que des feuilles de style CSS, des images, etc., Express fournit une fonction middleware intégrée `express.static`. Les fichiers statiques sont ceux que le client télécharge depuis un serveur.

C'est la seule fonction middleware qui vient avec le framework Express et nous pouvons l'utiliser directement dans notre application. Tous les autres middlewares sont tiers.

Par défaut, Express ne permet pas de servir des fichiers statiques. Nous devons utiliser cette fonction middleware. Une pratique courante dans le développement d'une application web est de stocker tous les fichiers statiques sous le répertoire 'public' à la racine d'un projet. Nous pouvons servir ce dossier pour inclure des fichiers statiques en écrivant dans notre fichier `index.js` :

```javascript
app.use(express.static('public'));
```

Maintenant, les fichiers statiques dans notre répertoire public seront chargés.

```shell
http://localhost:3000/css/style.css
http://localhost:3000/images/logo.png
http://localhost:3000/images/bg.png
http://localhost:3000/index.html
```

### **Plusieurs Répertoires Statiques**

Pour utiliser plusieurs répertoires d'actifs statiques, appelez la fonction middleware `express.static` plusieurs fois :

```javascript
app.use(express.static('public'));
app.use(express.static('files'));
```

### **Préfixe de Chemin Virtuel**

Un préfixe de chemin fixe peut également être fourni comme premier argument à la fonction middleware `express.static`. Cela est connu sous le nom de _Préfixe de Chemin Virtuel_ puisque le chemin réel n'existe pas dans le projet.

```javascript
app.use('/static', express.static('public'));
```

Si nous essayons maintenant de charger les fichiers :

```shell
http://localhost:3000/static/css/style.css
http://localhost:3000/static/images/logo.png
http://localhost:3000/static/images/bg.png
http://localhost:3000/static/index.html
```

Cette technique est utile lorsque vous fournissez plusieurs répertoires pour servir des fichiers statiques. Les préfixes sont utilisés pour aider à distinguer entre les différents répertoires.

## **Moteurs de Template**

Les moteurs de template sont des bibliothèques qui nous permettent d'utiliser différents langages de template. Un langage de template est un ensemble spécial d'instructions (syntaxe et structures de contrôle) qui indique au moteur comment traiter les données. L'utilisation d'un moteur de template est facile avec Express. Les moteurs de template populaires tels que Pug, EJS, Swig et Handlebars sont compatibles avec Express. Cependant, Express est livré avec un moteur de template par défaut, Jade, qui est la première version publiée de Pug.

Pour démontrer comment utiliser un moteur de template, nous allons utiliser Pug. C'est un moteur de template puissant qui offre des fonctionnalités telles que des filtres, des inclusions, l'interpolation, etc. Pour l'utiliser, nous devons d'abord l'installer en tant que module dans notre projet en utilisant `npm`.

```shell
npm install --save pug
```

Cette commande installera Pug et pour vérifier qu'il est installé correctement, il suffit de jeter un coup d'œil au fichier `package.json`. Pour l'utiliser avec notre application, nous devons d'abord le définir comme moteur de template et créer un nouveau répertoire './views' où nous stockerons tous les fichiers liés à notre moteur de template.

```javascript
app.set('view engine', 'pug');
app.set('views', './views');
```

Puisque nous utilisons `app.set()` qui indique la configuration dans notre fichier serveur, nous devons les placer avant de définir une route ou une fonction middleware.

Dans le répertoire `views`, créez un fichier appelé `index.pug`.

```pug
doctype html
  html
    head
      tite="Bonjour de Pug"
    body
      p.greetings Bonjour le Monde!  
```

Pour exécuter cette page, nous ajouterons la route suivante à notre application.

```javascript
app.get('/hello', (req, res) => {
  res.render('index');
});
```

Puisque nous avons déjà défini Pug comme notre moteur de template, dans `res.render`, nous n'avons pas à fournir l'extension `.pug`. Cette fonction rend le code dans n'importe quel fichier `.pug` en HTML pour que le client l'affiche. Les navigateurs ne peuvent rendre que les fichiers HTML. Si vous démarrez le serveur maintenant et visitez la route `http://localhost:3000/hello`, vous verrez le résultat `Bonjour le Monde` rendu correctement.

Dans Pug, vous devez remarquer que nous n'avons pas à écrire de balises de fermeture pour les éléments comme nous le faisons en HTML. Le code ci-dessus sera rendu en HTML comme suit :

```html
<!DOCTYPE html>
<html>
   <head>
      <title>Bonjour de Pug</title>
   </head>

   <body>
      <p class = "greetings">Bonjour le Monde!</p>
   </body>
</html>
```

L'avantage d'utiliser un moteur de template par rapport aux fichiers HTML bruts est qu'ils offrent un support pour effectuer des tâches sur les données. HTML ne peut pas rendre les données directement. Les frameworks comme Angular et React partagent ce comportement avec les moteurs de template.

Vous pouvez également passer des valeurs au moteur de template directement depuis la fonction de gestionnaire de route.

```javascript
app.get('/', (req, res) => {
  res.render('index', { title: 'Bonjour de Pug', message: 'Bonjour le Monde!' });
});
```

Pour le cas ci-dessus, notre fichier `index.pug` sera écrit comme suit :

```pug
doctype html
  html
    head
      title= title
    body
      h1= message
```

Le résultat sera le même que dans le cas précédent.

## **Structure de Projet d'une Application Express**

Puisqu'Express n'impose pas beaucoup de contraintes aux développeurs qui l'utilisent, il peut parfois être un peu accablant de savoir quelle structure de projet suivre. Il n'a pas de structure définie officiellement, mais le cas d'utilisation le plus courant que toute application basée sur Node.js suit est de séparer les différentes tâches dans différents modules. Cela signifie avoir des fichiers JavaScript séparés.

Passons en revue une structure typique d'une application web basée sur Express.

```text
project-root/
   node_modules/          // C'est là que les packages installés sont stockés
   config/
      db.js                // Connexion à la base de données et configuration
      credentials.js       // Mots de passe/clés API pour les services externes utilisés par votre application
      config.js            // Variables d'environnement
   models/                 // Pour les schémas mongoose
      books.js
      things.js
   routes/                 // Toutes les routes pour différentes entités dans différents fichiers
      books.js
      things.js
   views/
      index.pug
      404.pug
        ...
   public/                 // Tous les fichiers statiques
      images/
      css/
      javascript/
   app.js
   routes.js               // Requiert toutes les routes dans ce fichier et nécessite ensuite ce fichier dans
   app.js
   package.json
```

Ce modèle est communément connu sous le nom de MVC, modèle-vue-contrôleur. Tout simplement parce que notre modèle de base de données, l'interface utilisateur de l'application et les contrôleurs (dans notre cas, les routes) sont écrits et stockés dans des fichiers séparés. Ce modèle de conception facilite la mise à l'échelle de toute application web si vous souhaitez introduire plus de routes ou de fichiers statiques à l'avenir et le code est maintenable.