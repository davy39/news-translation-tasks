---
title: Comment fonctionne la bibliothèque de middleware Morgan pour Express ? Explications
  avec des exemples de code
subtitle: ''
author: Orim Dominic Adah
co_authors: []
series: null
date: '2025-09-29T18:14:54.062Z'
originalURL: https://freecodecamp.org/news/how-does-the-morgan-library-work
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1759169256698/9cb4e87a-2bc3-49ac-b1a6-b9d02d410ea1.png
tags:
- name: JavaScript
  slug: javascript
- name: Express.js
  slug: expressjs
- name: Libraries
  slug: libraries
seo_title: Comment fonctionne la bibliothèque de middleware Morgan pour Express ?
  Explications avec des exemples de code
seo_desc: Morgan is an Express middleware library that examines HTTP requests and
  logs details of the request to an output. It is one of the most popular Express
  middleware libraries with over 8,000 GitHub stars and more than 9,000 npm libraries
  dependent on i...
---

[Morgan](https://www.npmjs.com/package/morgan) est une bibliothèque de middleware pour Express qui examine les requêtes HTTP et enregistre les détails de la requête dans une sortie. C'est l'une des bibliothèques de middleware Express les plus populaires avec plus de 8 000 étoiles sur GitHub et plus de 9 000 bibliothèques npm qui en dépendent. GitHub rapporte que Morgan est utilisé par au moins 3,6 millions de dépôts.

Ce guide explique le code de la bibliothèque Morgan pour vous aider à comprendre son fonctionnement sous le capot. Cela est utile si vous avez de l'expérience avec Express et que vous souhaitez comprendre les rouages internes qui produisent les lignes de log Morgan. Une compréhension des fermetures (closures) en JavaScript est utile pour ce guide, mais pas indispensable.

## Table des matières

* [Qu'est-ce qu'un middleware Express ?](#heading-qu-est-ce-qu-un-middleware-express)
    
* [Un bref aperçu du fonctionnement de Morgan](#heading-un-bref-apercu-du-fonctionnement-de-morgan)
    
* [Qu'est-ce qu'un jeton (token) Morgan ?](#heading-qu-est-ce-qu-un-jeton-morgan)
    
* [Que se passe-t-il lors de l'initialisation de Morgan ?](#heading-que-se-passe-t-il-lors-de-l-initialisation-de-morgan)
    
* [Que se passe-t-il lorsque Morgan capture une requête ?](#heading-que-se-passe-t-il-lorsque-morgan-capture-une-requete)
    
* [Prochaines étapes](#heading-prochaines-etapes)
    

## Qu'est-ce qu'un middleware Express ?

Selon la [documentation d'Express](https://expressjs.com/en/guide/writing-middleware.html), un middleware est une fonction qui a accès aux objets de requête (request) et de réponse (response) ainsi qu'à la fonction `next` du cycle de requête Express. Ils sont généralement utilisés pour intercepter les requêtes afin d'exécuter des effets de bord avant ou après que la requête ne soit traitée par son gestionnaire de route.

Un middleware peut être utilisé pour :

* **Apporter des modifications aux objets de requête et de réponse** : Il peut modifier les objets de requête et de réponse en y attachant des propriétés telles que des en-têtes et des cookies.
    
* **Terminer le cycle requête-réponse** : Il peut mettre fin à une requête et envoyer une réponse au client avant ou après que la requête ne soit traitée par son gestionnaire de route.
    
* **Exécuter le middleware suivant dans la pile** : Il peut déclencher l'exécution du middleware suivant via l'argument de fonction `next`.
    

Une fonction nommée `next` est généralement le troisième argument d'un middleware et elle est utilisée pour passer la requête au middleware suivant. Si la fonction `next` n'est pas exécutée dans un middleware et que la requête n'est pas explicitement terminée par l'envoi d'une réponse au client, la requête restera en suspens et l'application sera bloquée pour le traitement des requêtes entrantes consécutives.

L'interface d'un middleware est présentée dans l'extrait de code ci-dessous :

```javascript
function middleware(request, response, next) {
    // opérations à effectuer lors de l'exécution de ce middleware
    next() // exécuter le middleware suivant
}
```

Un middleware peut intercepter et gérer les cas où les middlewares précédents ou les gestionnaires de routes lancent des erreurs non gérées. Ces middlewares sont généralement appelés middlewares de gestion d'erreurs et acceptent quatre arguments comme indiqué ci-dessous :

```javascript
function errorHandlerMiddleware(error, request, response, next) {}
```

L'argument `error` représente l'erreur non gérée.

Certains middlewares comme Morgan et [cors](https://www.npmjs.com/package/cors) sont des fonctions d'ordre supérieur. Ils acceptent des arguments de configuration lors de l'initialisation et renvoient une fonction middleware, exécutée par Express lorsqu'une requête survient.

```javascript
function initialise(...configArgs) {
    // utiliser configArgs ici
    return function middleware(request, response, next) {
        // peut également utiliser configArgs ici
        // opérations à effectuer lorsque ce middleware est touché par une requête
        next() // exécuter le middleware suivant
    }
}
```

## Un bref aperçu du fonctionnement de Morgan

```javascript
import morgan from "morgan"
// morgan(format, [options])
morgan("tiny") // initialise morgan et renvoie un middleware
// Exemple de sortie : GET /tiny 200 2 - 0.188 ms
```

Morgan est initialisé en l'exécutant avec un argument `format` obligatoire et un argument `options` facultatif. L'argument `format` peut être :

* Un nom de format Morgan prédéfini
    
* Une chaîne de format contenant des jetons (tokens) prédéfinis (un jeu de jetons)
    
* Une fonction de format personnalisée qui renvoie une sortie de log sous forme de chaîne de caractères
    

L'argument `options` est facultatif. C'est un objet avec trois propriétés :

* `immediate` (booléen) : Si `true`, la sortie du log sera créée dès la réception de la requête et non lors de l'envoi d'une réponse. La valeur par défaut est `false`.
    
* `skip` (fonction) : La fonction accepte les objets de requête et de réponse comme arguments et renvoie une valeur booléenne basée sur la logique interne. Si la valeur renvoyée est `true`, la ligne de log pour une requête n'est pas enregistrée. `skip` vaut `false` par défaut.
    
* `stream` (WritableStream) : Flux de sortie pour l'écriture des lignes de log. Par défaut, il s'agit de `process.stdout`, mais cela pourrait être un fichier.
    

Lorsque Morgan est initialisé, il stocke ses arguments d'initialisation dans des variables de fermeture (closure) et renvoie une fonction middleware. La fonction est exécutée lorsqu'une requête l'atteint et elle génère une ligne de log pour la requête. Le format et l'endroit où la ligne de log est envoyée sont déterminés par les arguments d'initialisation.

## Qu'est-ce qu'un jeton (token) Morgan ?

Un jeton Morgan est une chaîne de caractères préfixée par deux-points, correspondant à une propriété des objets de requête ou de réponse ou à une valeur générée par l'utilisateur. Par exemple, le jeton de la méthode de requête est `':method'` et le jeton du code d'état de la réponse est `':status'`. Un jeton peut également accepter un argument pour personnaliser son comportement. Par exemple, dans `':date[format]'`, `format` peut être remplacé par `clf`, `iso` ou `web` pour définir le format de la date qui figurera dans la ligne de log. Une compréhension des jetons Morgan est cruciale pour comprendre le fonctionnement de Morgan.

Vous pouvez créer de nouveaux jetons en utilisant la fonction `morgan.token`. L'extrait de code ci-dessous crée un nouveau jeton appelé `':type'` qui correspond à l'en-tête `Content-Type` de la réponse :

```javascript
morgan.token('type', function (req, res) {
    return res.headers['content-type']
})
```

Morgan possède des chaînes de formats nommés prédéfinis (`tiny`, `dev`, `short`, `combined`, `common`) contenant un ensemble de jetons, et chaque format nommé a son jeu de jetons et sa configuration spécifiques. Le jeu de jetons pour `tiny` est `':method :url :status :res[content-length] - :response-time ms'`. Morgan peut accepter ces formats nommés comme valeur de l'argument `format`.

En plus d'accepter des formats nommés, Morgan peut également accepter un jeu de jetons (par exemple `':method :url :status :res[content-length] - :response-time ms'`) comme argument `format`. Un troisième type d'argument que Morgan accepte pour `format` est une fonction de format. Une fonction de format accepte trois arguments et renvoie une chaîne qui forme la ligne de log pour chaque requête. Par exemple, la fonction de format décrite ci-dessous :

```javascript
morgan(function (tokens, req, res) {
    return `method: ${tokens.method(req, res)}
path: ${tokens.url(req, res)}
code: ${tokens.status(req, res)}`
})
```

Cela produira une sortie de ligne de log comme :

```bash
method: get
path: /
code: 200
```

`tokens.method`, `tokens.url` et `tokens.status` sont des exemples de fonctions sur l'objet `morgan` qui peuvent générer des valeurs à enregistrer. Pour illustrer, le tableau ci-dessous montre des exemples de méthodes de jetons, leur jeton et des exemples de valeurs de sortie :

| Méthode du jeton | Jeton | Exemple de sortie |
| --- | --- | --- |
| method | `“:method”` | get |
| url | `“:url”` | / |
| status | `”:status”` | 200 |

Les sections suivantes de cet article expliquent comment Morgan fonctionne sous le capot. Pour suivre, ouvrez le [fichier index.js de Morgan sur GitHub](https://github.com/expressjs/morgan/blob/master/index.js).

## Que se passe-t-il lors de l'initialisation de Morgan ?

Lorsque Morgan est initialisé, il fait une copie des arguments qui lui sont fournis. Pour les arguments qui n'ont pas été fournis, Morgan définit des valeurs par défaut. Par exemple, si aucun argument de chaîne `format` n'a été fourni, Morgan utilise le format nommé `'default'` et enregistre ensuite un avis d'obsolescence (deprecation notice) avec une suggestion d'une manière non obsolète de l'initialiser par la suite.

Morgan configure ensuite la fonction `formatLine` - la fonction qui crée et renvoie la ligne de log pour une requête lorsqu'elle est exécutée. Comment fait-il cela ?

Tout d'abord, Morgan vérifie si `format` est une fonction de format. Si c'est le cas, la fonction de format est assignée à `formatLine` et ensuite, Morgan configure le flux de sortie. Si `format` n'est pas une fonction, il est passé en argument à `getFormatFunction`. `getFormatFunction` accepte `format` et consulte le magasin d'objets de Morgan pour vérifier si `format` est :

* L'un des formats nommés de Morgan ou un format nommé défini par l'utilisateur créé via `morgan.format`
    
* Un jeu de jetons
    

S'il ne s'agit d'aucun des deux, Morgan utilise le format nommé `default`.

```javascript
function getFormatFunction (name) { // `name` est aussi `format`
  var fmt = morgan[name] || name || morgan.default

  return typeof fmt !== 'function'
    ? compile(fmt)
    : fmt
}
```

Si le format nommé correspond à une fonction de format après la recherche, Morgan renvoie la fonction de format, qui est ensuite assignée à `formatLine`, sinon, il correspond à un jeu de jetons. Morgan compile le jeu de jetons en une fonction de format via la fonction `compile` - l'une des fonctions les plus importantes du package Morgan.

### La fonction `compile` 

La fonction `compile` accepte un jeu de jetons et renvoie une fonction qui possède l'interface d'une fonction de format. Comment fait-elle cela ?

Avec la méthode JavaScript `replace`, elle utilise une RegEx pour rechercher toutes les occurrences d'un jeton dans le jeu de jetons et remplace chaque occurrence. Si le jeu de jetons est `':method :res[content-length] - :response-time ms'`, la méthode `replace` de la RegEx remplace les jetons comme illustré dans le tableau ci-dessous :

| nom | arg | chaîne de remplacement |
| --- | --- | --- |
| ‘method’ | `undefined` | `(tokens["method"](req, res) || "-") + " " +` |
| ‘res’ | `’content-length’` | `(tokens["res"](req, res, "content-length") || "-") + " - " +` |
| ‘response-time’ | undefined | `(tokens["response-time"](req, res) || "-") +` |

Le résultat du remplacement par RegEx est préfixé par `"use strict"\n return ""` et finit par produire la chaîne ci-dessous :

```plaintext
"use strict" 
    return "" +  
    (tokens["method"](req, res) || "-") + " " +   
    (tokens["res"](req, res, "content-length") || "-") + " - " + 
    (tokens["response-time"](req, res) || "-") + " ms"
```

La chaîne ci-dessus est utilisée pour créer une fonction de format à l'aide du [constructeur Function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/Function) et renvoyée sous la forme :

```javascript
function (tokens, req, res) {
  "use strict"
  return "" +
    (tokens["method"](req, res) || "-") + " " +
    (tokens["res"](req, res, "content-length") || "-") + " - " +
    (tokens["response-time"](req, res) || "-") + " ms"
}
```

La fonction de format est finalement stockée dans `formatLine`.

Lorsque `formatLine` est exécutée avec `morgan` comme argument `tokens`, elle créera une ligne de log. Dans le cas de l'exemple de jeu de jetons, elle créera une ligne de log qui ressemblera à `GET 20 1.233 ms`.

Après avoir créé la fonction `formatLine`, Morgan utilise la fonction `createBufferStream` pour configurer la diffusion (streaming) des lignes de log créées vers la sortie préférée si elle est définie par `options.stream`. Si `options.stream` n'est pas défini, il utilise `process.stdout`.

Morgan effectue toute cette configuration afin de pouvoir créer des lignes de log rapidement lors de la capture d'une requête. Il serait inefficace de faire tout cela pour chaque requête.

## Que se passe-t-il lorsque Morgan capture une requête ?

Lorsque Morgan capture une requête, il stocke l'adresse IP du client à l'aide de la fonction `getip`. Ensuite, il stocke l'heure à laquelle la requête l'a déclenché et l'attache à l'objet de requête dans les propriétés `_startAt` et `_startTime`.

* `_startAt` est utilisé pour calculer le temps total entre l'arrivée de la requête dans Morgan et le moment où la réponse a fini d'être écrite sur la connexion, en millisecondes.
    
* `_startTime` est utilisé pour calculer le temps de réponse - le temps entre la capture de la requête par Morgan et le moment où les en-têtes de réponse sont écrits.
    

Ensuite, Morgan tente de générer la ligne de log pour la requête et de l'enregistrer en exécutant la fonction `logRequest`. Morgan vérifie si la ligne de log doit être émise lors de la requête, et si c'est le cas, Morgan exécute `logRequest` puis exécute `next` pour passer la requête au middleware suivant.

```javascript
if (immediate) {
  logRequest()
} else {
  onHeaders(res, recordStartTime)
  onFinished(res, logRequest)
}

next()
```

Si la sortie du log doit être créée lors de la réponse, Morgan enregistre deux fonctions sur les écouteurs d'événements de l'objet de réponse :

* **Une fonction à exécuter lorsque les en-têtes commencent à être écrits sur l'objet de réponse** : Lorsque cet écouteur est déclenché, il enregistre l'heure à laquelle les en-têtes commencent à être écrits sur l'objet de réponse sous les noms `_startAt` et `startTime`. Ces valeurs sont utilisées pour calculer le temps de réponse et le temps total de la requête.
    
* **Une fonction à exécuter lorsque la requête se ferme, se termine ou échoue** : Elle exécute `logRequest` lorsque cet événement se produit.
    

Au sein de `logRequest`, Morgan vérifie la valeur de l'option `skip`. S'il s'agit d'une fonction, elle est exécutée et si elle renvoie `true`, Morgan ne crée pas de sortie de log pour la requête et s'arrête.

```javascript
function logRequest () {
  if (skip !== false && skip(req, res)) {
    debug('skip request')
    return
  }

  var line = formatLine(morgan, req, res)

  if (line == null) {
    debug('skip line')
    return
  }

  stream.write(line + '\n')
};
```

Si `skip` est `false` ou si son exécution évalue à `false`, Morgan génère la ligne de log pour la requête en utilisant `formatLine`. Si la ligne de log est `null`, Morgan s'arrête, sinon il envoie la ligne de log au support de sortie et s'arrête.

## Prochaines étapes

Vous avez appris comment le middleware Morgan pour Express produit des logs. Vous disposez désormais des compétences fondamentales pour choisir un autre middleware ou une bibliothèque Node.js que vous utilisez et l'étudier pour voir comment elle fonctionne. Choisissez-en une, étudiez-la, écrivez à son sujet et partagez vos découvertes avec les autres.

Si vous avez des questions, vous pouvez me contacter sur [LinkedIn](https://www.linkedin.com/in/orimdominicadah/). Je serai ravi de vous répondre.