---
title: Le manuel Express + Node.js - Apprendre le Framework JavaScript Express pour
  les débutants
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2022-11-18T18:52:29.000Z'
originalURL: https://freecodecamp.org/news/the-express-handbook
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/pexels-paul-ijsendoorn-1181202.jpg
tags:
- name: Express
  slug: express
- name: JavaScript
  slug: javascript
- name: node
  slug: node
seo_title: Le manuel Express + Node.js - Apprendre le Framework JavaScript Express
  pour les débutants
seo_desc: 'What is Express?

  Express is a Web Framework built upon Node.js.

  Node.js is an amazing tool for building networking services and applications.

  Express builds on top of its features to provide easy to use functionality that
  satisfies the needs of the W...'
---

## Qu'est-ce qu'Express ?

Express est un Framework Web construit sur Node.js.

Node.js est un outil incroyable pour construire des services et applications réseau.

Express s'appuie sur ses fonctionnalités pour fournir une fonctionnalité facile à utiliser qui satisfait les besoins du cas d'utilisation du serveur Web. Il est Open Source, gratuit, facile à étendre et très performant.

Il existe également de nombreux packages pré-construits que vous pouvez simplement intégrer et utiliser pour faire toutes sortes de choses.

[Vous pouvez obtenir une version PDF et ePub de ce manuel Express](https://thevalleyofcode.com/download/express/)

## Table des matières

* [Comment installer Express](#heading-comment-installer-express)

* [Le premier exemple "Hello, World"](#heading-le-premier-exemple-hello-world)

* [Paramètres de requête](#heading-parametres-de-requete)

* [Comment envoyer une réponse au client](#heading-comment-envoyer-une-reponse-au-client)

* [Comment envoyer une réponse JSON](#heading-comment-envoyer-une-reponse-json)

* [Comment gérer les cookies](#heading-comment-gerer-les-cookies)

* [Comment travailler avec les en-têtes HTTP](#heading-comment-travailler-avec-les-en-tetes-http)

* [Comment gérer les redirections](#heading-comment-gerer-les-redirections)

* [Le routage dans Express](#heading-le-routage-dans-express)

* [Les modèles dans Express](#heading-les-modeles-dans-express)

* [Middleware Express](#heading-middleware-express)

* [Comment servir des actifs statiques avec Express](#heading-comment-servir-des-actifs-statiques-avec-express)

* [Comment envoyer des fichiers au client](#heading-comment-envoyer-des-fichiers-au-client)

* [Sessions dans Express](#heading-sessions-dans-express)

* [Comment valider l'entrée dans Express](#heading-comment-valider-lentree-dans-express)

* [Comment assainir l'entrée dans Express](#comment-assainir-lentree-dans-express)

* [Comment gérer les formulaires dans Express](#heading-comment-gerer-les-formulaires-dans-express)

* [Comment gérer les téléchargements de fichiers dans les formulaires dans Express](#heading-comment-gerer-les-telechargements-de-fichiers-dans-les-formulaires-dans-express)

## Comment installer Express

Vous pouvez installer Express dans n'importe quel projet avec npm.

Si vous êtes dans un dossier vide, créez d'abord un nouveau projet Node.js avec cette commande :

```javascript
npm init -y
```

puis exécutez ceci :

```javascript
npm install express
```

pour installer Express dans le projet.

## Le premier exemple "Hello, World"

Le premier exemple que nous allons créer est un simple serveur Web Express.

Copiez ce code :

```js
const express = require('express')
const app = express()

app.get('/', (req, res) => res.send('Hello World!'))
app.listen(3000, () => console.log('Serveur prêt'))
```

Enregistrez ceci dans un fichier `index.js` à la racine de votre projet, et démarrez le serveur en utilisant cette commande :

```javascript
node index.js
```

Vous pouvez ouvrir le navigateur sur le port 3000 en localhost et vous devriez voir le message `Hello World!`.

Ces 4 lignes de code font beaucoup de choses en coulisses.

Tout d'abord, nous importons le package `express` dans la valeur `express`.

Nous instancions une application en appelant la méthode `express()`.

Une fois que nous avons l'objet application, nous lui disons d'écouter les requêtes GET sur le chemin `/`, en utilisant la méthode `get()`.

Il existe une méthode pour chaque verbe HTTP : `get()`, `post()`, `put()`, `delete()`, et `patch()` :

```js
app.get('/', (req, res) => { /* */ })
app.post('/', (req, res) => { /* */ })
app.put('/', (req, res) => { /* */ })
app.delete('/', (req, res) => { /* */ })
app.patch('/', (req, res) => { /* */ })
```

Ces méthodes acceptent une fonction de rappel – qui est appelée lorsqu'une requête est démarrée – et nous devons la gérer.

Nous passons une fonction fléchée :

```js
(req, res) => res.send('Hello World!')
```

Express nous envoie deux objets dans ce rappel, que nous avons appelés `req` et `res`. Ils représentent les objets Request et Response.

Les deux sont des standards et vous pouvez en lire plus sur eux [ici](https://developer.mozilla.org/en-US/docs/Web/API/Request) et [ici](https://developer.mozilla.org/en-US/docs/Web/API/Response).

Request est la requête HTTP. Il nous donne toutes les informations de la requête, y compris les paramètres de la requête, les en-têtes, le corps de la requête, et plus encore.

Response est l'objet de réponse HTTP que nous enverrons au client.

Ce que nous faisons dans ce rappel est d'envoyer la chaîne 'Hello World!' au client, en utilisant la méthode `Response.send()`.

Cette méthode définit cette chaîne comme le corps, et elle ferme la connexion.

La dernière ligne de l'exemple démarre effectivement le serveur, et lui dit d'écouter sur le port `3000`. Nous passons un rappel qui est appelé lorsque le serveur est prêt à accepter de nouvelles requêtes.

## Paramètres de requête

J'ai mentionné comment l'objet Request contient toutes les informations de la requête HTTP.

Voici les principales propriétés que vous utiliserez probablement :

| Propriété | Description |
| --- | --- |
| .app | contient une référence à l'objet app Express |
| .baseUrl | le chemin de base sur lequel l'app répond |
| .body | contient les données soumises dans le corps de la requête (doit être analysé et peuplé manuellement avant de pouvoir y accéder) |
| .cookies | contient les cookies envoyés par la requête (nécessite le middleware `cookie-parser`) |
| .hostname | le nom d'hôte tel que défini dans la valeur de l'en-tête [Host HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Host) |
| .ip | l'IP du client |
| .method | la méthode HTTP utilisée |
| .params | les paramètres nommés de la route |
| .path | le chemin de l'URL |
| .protocol | le protocole de la requête |
| .query | un objet contenant toutes les chaînes de requête utilisées dans la requête |
| .secure | vrai si la requête est sécurisée (utilise HTTPS) |
| .signedCookies | contient les cookies signés envoyés par la requête (nécessite le middleware `cookie-parser`) |
| .xhr | vrai si la requête est une [XMLHttpRequest](https://www.freecodecamp.org/news/xhr/) |

## Comment envoyer une réponse au client

Dans l'exemple Hello World, nous avons utilisé la méthode `send()` de l'objet Response pour envoyer une simple chaîne comme réponse, et pour fermer la connexion :

```js
(req, res) => res.send('Hello World!')
```

Si vous passez une chaîne, elle définit l'en-tête `Content-Type` sur `text/html`.

Si vous passez un objet ou un tableau, elle définit l'en-tête `Content-Type` sur `application/json`, et analyse ce paramètre en [JSON](https://www.freecodecamp.org/news/json/).

Après cela, `send()` ferme la connexion.

`send()` définit automatiquement l'en-tête de réponse HTTP `Content-Length`, contrairement à `end()` qui nécessite que vous le fassiez.

### Comment utiliser end() pour envoyer une réponse vide

Une alternative pour envoyer la réponse, sans aucun corps, est d'utiliser la méthode `Response.end()` :

```js
res.end()
```

### Comment définir le statut de la réponse HTTP

Utilisez la méthode `status()` sur l'objet réponse :

```js
res.status(404).end()
```

ou

```js
res.status(404).send('Fichier non trouvé')
```

`sendStatus()` est un raccourci :

```js
res.sendStatus(200)
// === res.status(200).send('OK')

res.sendStatus(403)
// === res.status(403).send('Interdit')

res.sendStatus(404)
// === res.status(404).send('Non trouvé')

res.sendStatus(500)
// === res.status(500).send('Erreur interne du serveur')
```

## Comment envoyer une réponse JSON

Lorsque vous écoutez les connexions sur une route dans Express, la fonction de rappel sera invoquée à chaque appel réseau avec une instance d'objet Request et une instance d'objet Response.

Exemple :

```js
app.get('/', (req, res) => res.send('Hello World!'))
```

Ici, nous avons utilisé la méthode `Response.send()`, qui accepte n'importe quelle chaîne.

Vous pouvez envoyer du [JSON](https://www.freecodecamp.org/news/json/) au client en utilisant `Response.json()`, une méthode utile.

Elle accepte un objet ou un tableau, et le convertit en JSON avant de l'envoyer :

```js
res.json({ username: 'Flavio' })
```

## Comment gérer les cookies

Utilisez la méthode `Response.cookie()` pour manipuler vos cookies.

Exemples :

```js
res.cookie('username', 'Flavio')
```

Cette méthode accepte un troisième paramètre, qui contient diverses options :

```js
res.cookie('username', 'Flavio', { domain: '.flaviocopes.com', path: '/administrator', secure: true })

res.cookie('username', 'Flavio', { expires: new Date(Date.now() + 900000), httpOnly: true })
```

Les paramètres les plus utiles que vous pouvez définir sont :

| Valeur | Description |
| --- | --- |
| `domain` | Le [nom de domaine du cookie](https://www.freecodecamp.org/news/cookies/#set-a-cookie-domain) |
| `expires` | Définit la [date d'expiration du cookie](https://www.freecodecamp.org/news/cookies/#set-a-cookie-expiration-date). Si manquant, ou 0, le cookie est un cookie de session |
| `httpOnly` | Définit le cookie pour qu'il soit accessible uniquement par le serveur web. Voir [HttpOnly](https://www.freecodecamp.org/news/cookies/#httponly) |
| `maxAge` | Définit le temps d'expiration relatif à l'heure actuelle, exprimé en millisecondes |
| `path` | Le [chemin du cookie](https://www.freecodecamp.org/news/cookies/#set-a-cookie-path). Par défaut '/' |
| `secure` | Marque le [cookie HTTPS uniquement](https://www.freecodecamp.org/news/cookies/#secure) |
| `signed` | Définit le cookie pour qu'il soit signé |
| `sameSite` | Valeur de [`SameSite`](https://www.freecodecamp.org/news/cookies/#samesite) |

Un cookie peut être effacé avec :

```js
res.clearCookie('username')
```

## Comment travailler avec les en-têtes HTTP

### Comment accéder aux valeurs des en-têtes HTTP d'une requête

Vous pouvez accéder à tous les en-têtes HTTP en utilisant la propriété `Request.headers` :

```js
app.get('/', (req, res) => {
  console.log(req.headers)
})
```

Utilisez la méthode `Request.header()` pour accéder à la valeur d'un en-tête de requête individuel :

```js
app.get('/', (req, res) => {
  req.header('User-Agent')
})
```

### Comment changer n'importe quelle valeur d'en-tête HTTP pour une réponse

Vous pouvez changer n'importe quelle valeur d'en-tête HTTP en utilisant `Response.set()` :

```js
res.set('Content-Type', 'text/html')
```

Il existe cependant un raccourci pour l'en-tête Content-Type :

```js
res.type('.html')
// => 'text/html'

res.type('html')
// => 'text/html'

res.type('json')
// => 'application/json'

res.type('application/json')
// => 'application/json'

res.type('png')
// => image/png:
```

## Comment gérer les redirections

Les redirections sont courantes dans le développement Web. Vous pouvez créer une redirection en utilisant la méthode `Response.redirect()` :

```js
res.redirect('/aller-la')
```

Cela crée une redirection 302.

Une redirection 301 est faite de cette manière :

```js
res.redirect(301, '/aller-la')
```

Vous pouvez spécifier un chemin absolu (`/aller-la`), une URL absolue (`https://unautresite.com`), un chemin relatif (`aller-la`) ou utiliser `..` pour revenir d'un niveau :

```js
res.redirect('../aller-la')
res.redirect('..')
```

Vous pouvez également rediriger vers la valeur de l'en-tête HTTP Referrer (par défaut `/` si non défini) en utilisant

```js
res.redirect('back')
```

## Le routage dans Express

Le routage est le processus de détermination de ce qui devrait se passer lorsqu'une URL est appelée, ou également quelles parties de l'application devraient gérer une requête entrante spécifique.

Dans l'exemple Hello World, nous avons utilisé ce code :

```js
app.get('/', (req, res) => { /* */ })
```

Cela crée une route qui mappe l'accès à l'URL du domaine racine `/` en utilisant la méthode HTTP GET à la réponse que nous voulons fournir.

### Paramètres nommés

Que faire si nous voulons écouter des requêtes personnalisées ? Peut-être voulons-nous créer un service qui accepte une chaîne et la retourne en majuscules – et nous ne voulons pas que le paramètre soit envoyé comme une chaîne de requête, mais comme partie de l'URL. Dans un cas comme celui-ci, nous utilisons des paramètres nommés :

```js
app.get('/uppercase/:theValue', (req, res) => res.send(req.params.theValue.toUpperCase()))
```

Si nous envoyons une requête à `/uppercase/test`, nous obtiendrons `TEST` dans le corps de la réponse.

Vous pouvez utiliser plusieurs paramètres nommés dans la même URL, et ils seront tous stockés dans `req.params`.

### Comment utiliser une expression régulière pour faire correspondre un chemin

Vous pouvez utiliser des [expressions régulières](https://flaviocopes.com/javascript-regular-expressions/) pour faire correspondre plusieurs chemins avec une seule instruction :

```js
app.get(/post/, (req, res) => { /* */ })
```

correspondra à `/post`, `/post/first`, `/thepost`, `/posting/something`, etc.

## Les modèles dans Express

Express est capable de gérer des moteurs de modèles côté serveur.

Les moteurs de modèles nous permettent d'ajouter des données à une vue, et de générer du HTML dynamiquement.

Express utilise Jade comme moteur par défaut. Jade est l'ancienne version de Pug, spécifiquement Pug 1.0.

Notez que le nom a été changé de Jade à Pug en raison d'un problème de marque déposée en 2016, lorsque le projet a publié la version 2. Vous pouvez toujours utiliser Jade, alias Pug 1.0, mais à l'avenir, il est préférable d'utiliser Pug 2.0

Bien que la dernière version de Jade soit ancienne, elle reste le moteur par défaut dans Express pour des raisons de compatibilité ascendante.

Dans tout nouveau projet, vous devriez utiliser Pug ou un autre moteur de votre choix. Le site officiel de Pug est [https://pugjs.org/](https://pugjs.org/).

Vous pouvez utiliser de nombreux moteurs de modèles différents, y compris Pug, Handlebars, Mustache, EJS et plus encore.

Pour utiliser Pug, nous devons d'abord l'installer :

```bash
npm install pug
```

et lors de l'initialisation de l'application Express, nous devons le définir :

```js
const express = require('express')
const app = express()
app.set('view engine', 'pug')
```

Nous pouvons maintenant commencer à écrire nos modèles dans des fichiers `.pug`.

Créez une vue about :

```js
app.get('/about', (req, res) => {
  res.render('about')
})
```

et le modèle dans `views/about.pug` :

```javascript
p Hello from Flavio
```

Ce modèle créera une balise `p` avec le contenu `Hello from Flavio`.

Vous pouvez interpoler une variable en utilisant ce code :

```js
app.get('/about', (req, res) => {
  res.render('about', { name: 'Flavio' })
})
```

```javascript
p Hello from #{name}
```

Consultez le [guide Pug](https://flaviocopes.com/pug) pour plus d'informations sur l'utilisation de Pug.

Ce convertisseur en ligne de HTML vers Pug sera d'une grande aide : [https://html-to-pug.com/](https://html-to-pug.com/).

## Middleware Express

Un middleware est une fonction qui s'intègre dans le processus de routage, effectuant une opération arbitraire à un moment donné dans la chaîne (selon ce que nous voulons qu'il fasse).

Il est couramment utilisé pour modifier les objets de requête ou de réponse, ou pour terminer la requête avant qu'elle n'atteigne le code du gestionnaire de route.

Le middleware est ajouté à la pile d'exécution comme suit :

```js
app.use((req, res, next) => { /* */ })
```

Cela ressemble à la définition d'une route, mais en plus des instances des objets Request et Response, nous avons également une référence à la fonction middleware *suivante*, que nous attribuons à la variable `next`.

Nous appelons toujours `next()` à la fin de notre fonction middleware, afin de passer l'exécution au gestionnaire suivant. Ce n'est que si nous voulons terminer prématurément la réponse et l'envoyer au client.

Vous utilisez généralement des middleware pré-construits, sous forme de packages `npm`. Vous pouvez trouver une grande liste de ceux disponibles [ici](https://expressjs.com/en/resources/middleware.html).

Un exemple est `cookie-parser`, qui est utilisé pour analyser les cookies dans l'objet `req.cookies`. Vous pouvez l'installer en utilisant `npm install cookie-parser` et vous l'utilisez comme ceci :

```js
const express = require('express')
const app = express()
const cookieParser = require('cookie-parser')

app.get('/', (req, res) => res.send('Hello World!'))

app.use(cookieParser())
app.listen(3000, () => console.log('Serveur prêt'))
```

Nous pouvons également définir une fonction middleware pour qu'elle s'exécute uniquement pour des routes spécifiques (pas pour toutes), en l'utilisant comme deuxième paramètre de la définition de la route :

```js
const myMiddleware = (req, res, next) => {
  /* ... */
  next()
}

app.get('/', myMiddleware, (req, res) => res.send('Hello World!'))
```

Si vous devez stocker des données générées dans un middleware pour les transmettre aux fonctions middleware suivantes, ou au gestionnaire de requête, vous pouvez utiliser l'objet `Request.locals`. Il attachera ces données à la requête actuelle :

```js
req.locals.name = 'Flavio'
```

## Comment servir des actifs statiques avec Express

Il est courant d'avoir des images, du CSS, et plus encore dans un sous-dossier `public`, et de les exposer au niveau racine :

```js
const express = require('express')
const app = express()

app.use(express.static('public'))

/* ... */

app.listen(3000, () => console.log('Serveur prêt'))
```

Si vous avez un fichier `index.html` dans `public/`, il sera servi si vous accédez maintenant à l'URL du domaine racine (`http://localhost:3000`)

## Comment envoyer des fichiers au client

Express fournit une méthode pratique pour transférer un fichier en tant que pièce jointe : `Response.download()`.

Une fois qu'un utilisateur accède à une route qui envoie un fichier en utilisant cette méthode, les navigateurs inviteront l'utilisateur à télécharger.

La méthode `Response.download()` vous permet d'envoyer un fichier joint à la requête, et le navigateur, au lieu de l'afficher dans la page, l'enregistrera sur le disque.

```js
app.get('/', (req, res) => res.download('./file.pdf'))
```

Dans le contexte d'une application :

```js
const express = require('express')
const app = express()

app.get('/', (req, res) => res.download('./file.pdf'))
app.listen(3000, () => console.log('Serveur prêt'))
```

Vous pouvez définir le fichier à envoyer avec un nom de fichier personnalisé :

```js
res.download('./file.pdf', 'user-facing-filename.pdf')
```

Cette méthode fournit une fonction de rappel que vous pouvez utiliser pour exécuter du code une fois le fichier envoyé :

```js
res.download('./file.pdf', 'user-facing-filename.pdf', (err) => {
  if (err) {
    // gérer l'erreur
    return
  } else {
    // faire quelque chose
  }
})
```

## Sessions dans Express

Par défaut, les requêtes Express sont séquentielles et aucune requête ne peut être liée à une autre. Il n'y a aucun moyen de savoir si cette requête provient d'un client qui a déjà effectué une requête précédemment.

Les utilisateurs ne peuvent pas être identifiés sauf en utilisant un mécanisme qui le rend possible.

C'est ce que sont les sessions.

Lorsque cela est implémenté, chaque utilisateur de votre API ou site web se verra attribuer une session unique, et cela vous permet de stocker l'état de l'utilisateur.

Nous allons utiliser le module `express-session`, qui est maintenu par l'équipe Express.

Vous pouvez l'installer en utilisant cette commande :

```bash
npm install express-session
```

et une fois que vous avez terminé, vous pouvez l'instancier dans votre application avec celle-ci :

```js
const session = require('express-session')
```

Ceci est un middleware, donc vous l'*installez* dans Express en utilisant ce qui suit :

```js
const express = require('express')
const session = require('express-session')

const app = express()
app.use(session({
  'secret': '343ji43j4n3jn4jk3n'
}))
```

Après cela, toutes les requêtes vers les routes de l'application utilisent maintenant des sessions.

`secret` est le seul paramètre requis, mais il y en a beaucoup d'autres que vous pouvez utiliser. Il devrait s'agir d'une chaîne unique et aléatoire pour votre application.

La session est attachée à la requête, donc vous pouvez y accéder en utilisant `req.session` ici :

```js
app.get('/', (req, res, next) => {
  // req.session
}
```

Cet objet peut être utilisé pour obtenir des données de la session, et également pour définir des données :

```js
req.session.name = 'Flavio'
console.log(req.session.name) // 'Flavio'
```

Ces données sont sérialisées en [JSON](https://www.freecodecamp.org/news/json/) lorsqu'elles sont stockées, donc vous pouvez utiliser des objets imbriqués en toute sécurité.

Vous pouvez utiliser des sessions pour communiquer des données à un middleware qui est exécuté plus tard, ou pour les récupérer plus tard, lors de requêtes ultérieures.

Où sont stockées les données de session ? Cela dépend de la manière dont vous avez configuré le module `express-session`.

Il peut stocker les données de session dans :

* **mémoire**, non destiné à la production

* une **base de données** comme MySQL ou Mongo

* un **cache mémoire** comme Redis ou Memcached

Il existe une grande liste de packages tiers qui implémentent une grande variété de différents magasins de cache compatibles dans [https://github.com/expressjs/session](https://github.com/expressjs/session).

Toutes les solutions stockent l'identifiant de session dans un cookie, et conservent les données côté serveur. Le client recevra l'identifiant de session dans un cookie, et l'enverra avec chaque requête HTTP.

Nous ferons référence à cela côté serveur pour associer l'identifiant de session aux données stockées localement.

La mémoire est le choix par défaut, et elle ne nécessite aucune configuration spéciale de votre part. C'est la chose la plus simple mais elle est destinée uniquement à des fins de développement.

Le meilleur choix est un cache mémoire comme Redis, pour lequel vous devez configurer sa propre infrastructure.

Un autre package populaire pour gérer les sessions dans Express est `cookie-session`, qui a une grande différence : il stocke les données côté client dans le cookie.

Je ne recommande pas de faire cela car stocker des données dans des cookies signifie qu'elles sont stockées côté client, et envoyées dans chaque requête faite par l'utilisateur. C'est également limité en taille, car il ne peut stocker que 4 kilo-octets de données.

Les cookies doivent également être sécurisés, mais par défaut ils ne le sont pas, puisque les cookies sécurisés sont possibles sur les sites HTTPS et vous devez les configurer si vous avez des proxies.

## Comment valider l'entrée dans Express

Voyons comment valider toute donnée entrant comme entrée dans vos points de terminaison Express.

Supposons que vous avez un point de terminaison POST qui accepte les paramètres name, email et age :

```js
const express = require('express')
const app = express()

app.use(express.json())

app.post('/form', (req, res) => {
  const name  = req.body.name
  const email = req.body.email
  const age   = req.body.age
})
```

Comment effectuez-vous une validation côté serveur sur ces résultats pour vous assurer que :

* name est une chaîne d'au moins 3 caractères ?

* email est un email réel ?

* age est un nombre, entre 0 et 110 ?

La meilleure façon de gérer la validation sur toute entrée provenant de l'extérieur dans Express est d'utiliser le [package `express-validator`](https://express-validator.github.io) :

```bash
npm install express-validator
```

Vous avez besoin des objets `check` et `validationResult` du package :

```js
const { check, validationResult } = require('express-validator');
```

Nous passons un tableau d'appels `check()` comme deuxième argument de l'appel `post()`. Chaque appel `check()` accepte le nom du paramètre comme argument. Ensuite, nous appelons `validationResult()` pour vérifier qu'il n'y a pas eu d'erreurs de validation. S'il y en a, nous les communiquons au client :

```js
app.post('/form', [
  check('name').isLength({ min: 3 }),
  check('email').isEmail(),
  check('age').isNumeric()
], (req, res) => {
  const errors = validationResult(req)
  if (!errors.isEmpty()) {
    return res.status(422).json({ errors: errors.array() })
  }

  const name  = req.body.name
  const email = req.body.email
  const age   = req.body.age
})
```

Remarquez que j'ai utilisé :

* `isLength()`

* `isEmail()`

* `isNumeric()`

Il existe de nombreuses autres méthodes, toutes provenant de [validator.js](https://github.com/chriso/validator.js#validators), y compris :

* `contains()`, vérifie si la valeur contient la valeur spécifiée

* `equals()`, vérifie si la valeur est égale à la valeur spécifiée

* `isAlpha()`

* `isAlphanumeric()`

* `isAscii()`

* `isBase64()`

* `isBoolean()`

* `isCurrency()`

* `isDecimal()`

* `isEmpty()`

* `isFQDN()`, vérifie s'il s'agit d'un nom de domaine entièrement qualifié

* `isFloat()`

* `isHash()`

* `isHexColor()`

* `isIP()`

* `isIn()`, vérifie si la valeur est dans un tableau de valeurs autorisées

* `isInt()`

* `isJSON()`

* `isLatLong()`

* `isLength()`

* `isLowercase()`

* `isMobilePhone()`

* `isNumeric()`

* `isPostalCode()`

* `isURL()`

* `isUppercase()`

* `isWhitelisted()`, vérifie l'entrée par rapport à une liste blanche de caractères autorisés

Vous pouvez valider l'entrée par rapport à une expression régulière en utilisant `matches()`.

Les dates peuvent être vérifiées en utilisant :

* `isAfter()`, vérifie si la date saisie est postérieure à celle que vous passez

* `isBefore()`, vérifie si la date saisie est antérieure à celle que vous passez

* `isISO8601()`

* `isRFC3339()`

Pour des détails exacts sur l'utilisation de ces validateurs, [reportons-nous à la documentation ici](https://github.com/chriso/validator.js#validators).

Toutes ces vérifications peuvent être combinées en les enchaînant :

```js
check('name')
  .isAlpha()
  .isLength({ min: 10 })
```

S'il y a une erreur, le serveur envoie automatiquement une réponse pour communiquer l'erreur. Par exemple, si l'email n'est pas valide, voici ce qui sera retourné :

```js
{
  "errors": [{
    "location": "body",
    "msg": "Invalid value",
    "param": "email"
  }]
}
```

Cette erreur par défaut peut être remplacée pour chaque vérification que vous effectuez, en utilisant `withMessage()` :

```js
check('name')
  .isAlpha()
  .withMessage('Doit être uniquement des caractères alphabétiques')
  .isLength({ min: 10 })
  .withMessage('Doit comporter au moins 10 caractères')
```

Et si vous voulez écrire votre propre validateur spécial et personnalisé ? Vous pouvez utiliser le validateur `custom`.

Dans la fonction de rappel, vous pouvez rejeter la validation soit en lançant une exception, soit en retournant une promesse rejetée :

```js
app.post('/form', [
  check('name').isLength({ min: 3 }),
  check('email').custom(email => {
    if (alreadyHaveEmail(email)) {
      throw new Error('Email déjà enregistré')
    }
  }),
  check('age').isNumeric()
], (req, res) => {
  const name  = req.body.name
  const email = req.body.email
  const age   = req.body.age
})
```

Le validateur personnalisé :

```js
check('email').custom(email => {
  if (alreadyHaveEmail(email)) {
    throw new Error('Email déjà enregistré')
  }
})
```

peut être réécrit comme ceci :

```js
check('email').custom(email => {
  if (alreadyHaveEmail(email)) {
    return Promise.reject('Email déjà enregistré')
  }
})
```

## Comment assainir l'entrée dans Express

Vous avez vu comment valider l'entrée provenant du monde extérieur vers votre application Express.

Il y a une chose que vous apprenez rapidement lorsque vous exécutez un serveur public : ne faites jamais confiance à l'entrée.

Même si vous assainissez et vous assurez que les gens ne peuvent pas entrer des choses étranges en utilisant le code côté client, vous serez toujours sujet aux personnes utilisant des outils (même juste les outils de développement du navigateur) pour POST directement à vos points de terminaison.

Ou des bots essayant toutes les combinaisons possibles d'exploits connues de l'homme.

Ce que vous devez faire, c'est assainir votre entrée.

Le [package `express-validator`](https://express-validator.github.io) que vous utilisez déjà pour valider l'entrée peut également être utilisé pour effectuer l'assainissement.

Supposons que vous avez un point de terminaison POST qui accepte les paramètres name, email et age :

```js
const express = require('express')
const app = express()

app.use(express.json())

app.post('/form', (req, res) => {
  const name  = req.body.name
  const email = req.body.email
  const age   = req.body.age
})
```

Vous pourriez le valider en utilisant :

```js
const express = require('express')
const app = express()

app.use(express.json())

app.post('/form', [
  check('name').isLength({ min: 3 }),
  check('email').isEmail(),
  check('age').isNumeric()
], (req, res) => {
  const name  = req.body.name
  const email = req.body.email
  const age   = req.body.age
})
```

Vous pouvez ajouter l'assainissement en enchaînant les méthodes d'assainissement après les méthodes de validation :

```js
app.post('/form', [
  check('name').isLength({ min: 3 }).trim().escape(),
  check('email').isEmail().normalizeEmail(),
  check('age').isNumeric().trim().escape()
], (req, res) => {
  //...
})
```

Ici, j'ai utilisé les méthodes :

* `trim()` supprime les caractères (espaces par défaut) au début et à la fin d'une chaîne

* `escape()` remplace `<`, `>`, `&`, `'`, `"` et `/` par leurs entités HTML correspondantes

* `normalizeEmail()` canonicalise une adresse email. Accepte plusieurs options pour mettre en minuscules les adresses email ou les sous-adresses (par exemple `flavio+newsletters@gmail.com`)

D'autres méthodes d'assainissement :

* `blacklist()` supprime les caractères qui apparaissent dans la liste noire

* `whitelist()` supprime les caractères qui n'apparaissent pas dans la liste blanche

* `unescape()` remplace les entités encodées en HTML par `<`, `>`, `&`, `'`, `"` et `/`

* `ltrim()` comme trim(), mais ne supprime les caractères qu'au début de la chaîne

* `rtrim()` comme trim(), mais ne supprime les caractères qu'à la fin de la chaîne

* `stripLow()` supprime les caractères de contrôle ASCII, qui sont normalement invisibles

Forcer la conversion vers un format :

* `toBoolean()` convertit la chaîne d'entrée en un booléen. Tout sauf '0', 'false' et '' retourne vrai. En mode strict, seulement '1' et 'true' retournent vrai.

* `toDate()` convertit la chaîne d'entrée en une date, ou null si l'entrée n'est pas une date

* `toFloat()` convertit la chaîne d'entrée en un float, ou NaN si l'entrée n'est pas un float

* `toInt()` convertit la chaîne d'entrée en un entier, ou NaN si l'entrée n'est pas un entier

Comme avec les validateurs personnalisés, vous pouvez créer un assainisseur personnalisé.

Dans la fonction de rappel, vous retournez simplement la valeur assainie :

```js
const sanitizeValue = value => {
  // assainir...
}

app.post('/form', [
  check('value').customSanitizer(value => {
    return sanitizeValue(value)
  }),
], (req, res) => {
  const value  = req.body.value
})
```

## Comment gérer les formulaires dans Express

Voici un exemple de formulaire HTML :

```html
<form method="POST" action="/submit-form">
  <input type="text" name="username" />
  <input type="submit" />
</form>
```

Lorsque l'utilisateur appuie sur le bouton de soumission, le navigateur effectuera automatiquement une requête `POST` à l'URL `/submit-form` sur la même origine de la page. Le navigateur envoie les données contenues, encodées en tant que `application/x-www-form-urlencoded`. Dans cet exemple particulier, les données du formulaire contiennent la valeur du champ de saisie `username`.

Les formulaires peuvent également envoyer des données en utilisant la méthode `GET`, mais la grande majorité des formulaires que vous construirez utiliseront `POST`.

Les données du formulaire seront envoyées dans le corps de la requête POST.

Pour les extraire, vous devrez utiliser le middleware `express.urlencoded()` :

```js
const express = require('express')
const app = express()

app.use(express.urlencoded({
  extended: true
}))
```

Maintenant, vous devez créer un point de terminaison `POST` sur la route `/submit-form`, et toutes les données seront disponibles sur `Request.body` :

```js
app.post('/submit-form', (req, res) => {
  const username = req.body.username
  //...
  res.end()
})
```

N'oubliez pas de valider les données avant de les utiliser avec `express-validator`.

## Comment gérer les téléchargements de fichiers dans les formulaires dans Express

Voici un exemple de formulaire HTML qui permet à un utilisateur de télécharger un fichier :

```html
<form method="POST" action="/submit-form" enctype="multipart/form-data">
  <input type="file" name="document" />
  <input type="submit" />
</form>
```

N'oubliez pas d'ajouter `enctype="multipart/form-data"` au formulaire, sinon les fichiers ne seront pas téléchargés.

Lorsque l'utilisateur appuie sur le bouton de soumission, le navigateur effectuera automatiquement une requête `POST` à l'URL `/submit-form` sur la même origine de la page. Le navigateur envoie les données contenues, non encodées comme un formulaire normal `application/x-www-form-urlencoded`, mais comme `multipart/form-data`.

Côté serveur, la gestion des données multipart peut être délicate et sujette aux erreurs, nous allons donc utiliser une bibliothèque utilitaire appelée **formidable**. [Voici le dépôt GitHub](https://github.com/felixge/node-formidable) – il a plus de 4000 étoiles et est bien maintenu.

Vous pouvez l'installer en utilisant :

```bash
npm install formidable
```

Ensuite, incluez-le dans votre fichier Node.js :

```js
const express = require('express')
const app = express()
const formidable = require('formidable')
```

Maintenant, dans le point de terminaison `POST` sur la route `/submit-form`, nous instancions un nouveau formulaire Formidable en utilisant `formidable.IncomingForm()` :

```js
app.post('/submit-form', (req, res) => {
  new formidable.IncomingForm()
})
```

Après cela, nous devons être en mesure d'analyser le formulaire. Nous pouvons le faire de manière synchrone en fournissant un rappel, ce qui signifie que tous les fichiers sont traités. Une fois que formidable a terminé, il les rend disponibles :

```js
app.post('/submit-form', (req, res) => {
  new formidable.IncomingForm().parse(req, (err, fields, files) => {
    if (err) {
      console.error('Erreur', err)
      throw err
    }
    console.log('Champs', fields)
    console.log('Fichiers', files)
    for (const file of Object.entries(files)) {
      console.log(file)
    }
  })
})
```

Ou, vous pouvez utiliser des événements au lieu d'un rappel. Par exemple, vous pouvez être notifié lorsque chaque fichier est analysé, ou d'autres événements tels que l'achèvement du traitement du fichier, la réception d'un champ non fichier, ou si une erreur s'est produite :

```js
app.post('/submit-form', (req, res) => {
  new formidable.IncomingForm().parse(req)
    .on('field', (name, field) => {
      console.log('Champ', name, field)
    })
    .on('file', (name, file) => {
      console.log('Fichier téléchargé', name, file)
    })
    .on('aborted', () => {
      console.error('Requête abandonnée par l\'utilisateur')
    })
    .on('error', (err) => {
      console.error('Erreur', err)
      throw err
    })
    .on('end', () => {
      res.end()
    })
})
```

Quelle que soit la méthode que vous choisissez, vous obtiendrez un ou plusieurs objets Formidable.File, qui vous donnent des informations sur le fichier téléchargé. Voici quelques-unes des méthodes que vous pouvez appeler :

* `file.size`, la taille du fichier en octets

* `file.path`, le chemin où le fichier est écrit

* `file.name`, le nom du fichier

* `file.type`, le type MIME du fichier

Le chemin par défaut est le dossier temporaire et peut être modifié si vous écoutez l'événement `fileBegin` :

```js
app.post('/submit-form', (req, res) => {
  new formidable.IncomingForm().parse(req)
    .on('fileBegin', (name, file) => {
        file.path = __dirname + '/uploads/' + file.name
    })
    .on('file', (name, file) => {
      console.log('Fichier téléchargé', name, file)
    })
    //...
})
```

## Merci d'avoir lu !

C'est tout pour ce manuel. Et n'oubliez pas que [vous pouvez obtenir une version PDF et ePub de ce manuel Express](https://thevalleyofcode.com/download/express/) si vous le souhaitez.