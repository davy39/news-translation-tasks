---
title: Comment gérer les téléchargements de fichiers sur le back-end en Node.js et
  Nuxt
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-04-20T22:27:42.000Z'
originalURL: https://freecodecamp.org/news/handle-file-uploads-on-the-backend-in-node-js-nuxt
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/Command-Line-Blog-Cover.png
tags:
- name: 'Back end development '
  slug: back-end-development
- name: JavaScript
  slug: javascript
- name: node
  slug: node
seo_title: Comment gérer les téléchargements de fichiers sur le back-end en Node.js
  et Nuxt
seo_desc: 'By Austin Gil

  In some previous tutorials, I covered how to upload files using HTML and JavaScript.
  It requires sending HTTP requests with the [Content-Type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type)
  header set to multipa...'
---

Par Austin Gil

Dans certains tutoriels précédents, j'ai expliqué comment télécharger des fichiers en utilisant [HTML](https://austingil.com/uploading-files-with-html/) et [JavaScript](https://austingil.com/upload-files-with-javascript/). Cela nécessite l'envoi de requêtes HTTP avec l'en-tête `[Content-Type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type)` défini sur `multipart/form-data`.

Aujourd'hui, nous allons sur le back-end pour recevoir ces requêtes `multipart/form-data` et accéder aux données binaires de ces fichiers.

## Quelques notions de base

La plupart des concepts de ce tutoriel devraient s'appliquer de manière générale à travers les frameworks, les environnements d'exécution et les langages, mais les exemples de code seront plus spécifiques.

Je travaillerai dans un projet [Nuxt.js](https://nuxt.com/) qui s'exécute dans un environnement [Node.js](https://nodejs.org/). Nuxt a des façons spécifiques de [définir les routes API](https://nuxt.com/docs/guide/directory-structure/server) qui nécessitent d'appeler une fonction globale appelée `defineEventHandler`.

```javascript
/**
 * @see https://nuxt.com/docs/guide/directory-structure/server
 * @see https://nuxt.com/docs/guide/concepts/server-engine
 * @see https://github.com/unjs/h3
 */
export default defineEventHandler((event) => {
  return { ok: true };
});
```

L'argument `event` fournit un accès pour travailler directement avec l'objet de requête Node.js sous-jacent (a.k.a. `IncomingMessage`) via `event.node.req`. Ainsi, nous pouvons écrire notre code spécifique à Node dans une abstraction, comme une fonction appelée `doSomethingWithNodeRequest` qui reçoit cet objet de requête Node et fait quelque chose avec.

```javascript
export default defineEventHandler((event) => {
  const nodeRequestObject = event.node.req;

  doSomethingWithNodeRequest(event.node.req);

  return { ok: true };
});

/**
 * @param {import('http').IncomingMessage} req
 */
function doSomethingWithNodeRequest(req) {
  // Faire des choses spécifiques ici
}
```

Travailler directement avec Node de cette manière signifie que le code et les concepts devraient s'appliquer indépendamment du framework de haut niveau avec lequel vous travaillez. En fin de compte, nous terminerons en travaillant dans Nuxt.js.

## Comment gérer `multipart/form-data` dans Node.js

Dans cette section, nous allons plonger dans certains concepts de bas niveau qu'il est bon de comprendre, mais qui ne sont pas strictement nécessaires. N'hésitez pas à sauter cette section si vous êtes déjà familier avec les chunks, les streams et les buffers dans Node.js.

Le téléchargement d'un fichier nécessite l'envoi d'une requête `multipart/form-data`. Dans ces requêtes, le navigateur divise les données en petits "[chunks](https://en.wikipedia.org/wiki/Chunking_(computing))" et les envoie à travers la connexion, un chunk à la fois. Cela est nécessaire car les fichiers peuvent être trop volumineux pour être envoyés en une seule fois.

Les chunks de données envoyés au fil du temps constituent ce qu'on appelle un "[stream](https://en.wikipedia.org/wiki/Stream_(computing))". Les streams sont un peu difficiles à comprendre la première fois, du moins c'était le cas pour moi. Ils méritent un article complet (ou plusieurs) à eux seuls, donc je vais partager [l'excellent guide de web.dev](https://web.dev/streams/) au cas où vous souhaiteriez en savoir plus.

En gros, un stream est une sorte de tapis roulant de données, où chaque chunk peut être traité au fur et à mesure qu'il arrive. En termes de requête HTTP, le back-end reçoit des parties de la requête, un peu à la fois.

Node.js nous fournit une API de gestionnaire d'événements via la méthode `on` de l'objet de requête, qui nous permet d'écouter les événements "data" au fur et à mesure qu'ils sont streamés vers le back-end.

```javascript
/**
 * @param {import('http').IncomingMessage} req
 */
function doSomethingWithNodeRequest(req) {
  req.on("data", (data) => {
    console.log(data);
  }
}
```

Par exemple, lorsque je télécharge [une photo de Nugget faisant une adorable grimace de bâillement](https://www.instagram.com/p/CmUxW6jDmWO/), puis que je regarde la console du serveur, je vois des choses étranges qui ressemblent à ceci :

![Capture d'écran d'un terminal avec deux logs de texte qui commencent par "<Buffer", suivis d'une longue liste de valeurs hexadécimales à deux chiffres, et se terminent par un grand nombre et "... more bytes>".](https://austingil.com/wp-content/uploads/image-63-1080x103.png)
_J'ai utilisé une capture d'écran ici pour empêcher les technologies d'assistance de lire ce charabia à voix haute. Pouvez-vous imaginer ?_

Ces deux morceaux de texte incompréhensible sont appelés "[buffers](https://developer.mozilla.org/en-US/docs/Glossary/buffer)" et ils représentent les deux chunks de données qui composaient le stream de requête contenant la photo adorable de Nugget.

> Un buffer est un stockage en mémoire physique utilisé pour stocker temporairement des données pendant leur transfert d'un endroit à un autre. – [MDN](https://developer.mozilla.org/en-US/docs/Glossary/buffer)

Les buffers sont un autre concept étrange et de bas niveau que je dois expliquer lorsque je parle de travailler avec des fichiers en JavaScript.

JavaScript ne travaille pas directement sur des données binaires, donc nous devons apprendre à connaître les buffers. Ce n'est pas grave si ces concepts semblent encore un peu vagues. Comprendre tout complètement n'est pas la partie importante pour l'instant, et à mesure que vous continuerez à apprendre sur les transferts de fichiers, vous acquerrez une meilleure connaissance de la façon dont tout cela fonctionne ensemble.

Travailler avec un seul chunk partiel de données n'est pas super utile. Ce que nous pouvons faire à la place, c'est réécrire notre fonction en quelque chose avec lequel nous pouvons travailler :

1. Retourner une `[Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)` pour faciliter la syntaxe asynchrone.
2. Fournir un `[Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)` pour stocker les chunks de données à utiliser plus tard.
3. Écouter l'événement "data" et ajouter les chunks à notre collection au fur et à mesure qu'ils arrivent.
4. Écouter l'événement "end" et convertir les chunks en quelque chose avec lequel nous pouvons travailler.
5. Résoudre la `Promise` avec la charge utile finale de la requête.
6. Nous devons également nous souvenir de gérer les événements "error".

```javascript
/**
 * @param {import('http').IncomingMessage} req
 */
function doSomethingWithNodeRequest(req) {
  return new Promise((resolve, reject) => {
    /** @type {any[]} */
    const chunks = [];
    req.on('data', (data) => {
      chunks.push(data);
    });
    req.on('end', () => {
      const payload = Buffer.concat(chunks).toString()
      resolve(payload);
    });
    req.on('error', reject);
  });
}
```

Et chaque fois que la requête reçoit des données, elle pousse ces données dans le tableau de chunks.

Ainsi, avec cette fonction configurée, nous pouvons réellement `[await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)` cette `Promise` retournée jusqu'à ce que la requête ait terminé de recevoir toutes les données du stream de requête, et logger la valeur résolue dans la console.

```javascript
export default defineEventHandler((event) => {
  const nodeRequestObject = event.node.req;

  const body = await doSomethingWithNodeRequest(event.node.req);
  console.log(body)

  return { ok: true };
});
```

Ceci est le corps de la requête. N'est-ce pas magnifique ?

![Capture d'écran d'un terminal contenant une longue chaîne de texte incompréhensible incluant des valeurs alphanumériques ainsi que des symboles et des caractères qui ne peuvent pas être rendus. Cela ressemble légitimement à de l'écriture extraterrestre](https://austingil.com/wp-content/uploads/image-64-1080x479.png)
_Je ne sais honnêtement pas ce qu'un lecteur d'écran ferait si cela était du texte brut._

Si vous téléchargez un fichier image, il ressemblera probablement à un extraterrestre qui a piraté votre ordinateur. Ne vous inquiétez pas, ce n'est pas le cas. C'est littéralement à quoi ressemblent les contenus textuels de ce fichier. Vous pouvez même essayer d'ouvrir un fichier image dans un éditeur de texte basique et voir la même chose.

Si je télécharge un exemple plus basique, comme un fichier `.txt` avec du texte brut, le corps pourrait ressembler à ceci :

```
Content-Disposition: form-data; name="file"; filename="dear-nugget.txt"
Content-Type: text/plain

I love you!
------WebKitFormBoundary4Ay52hDeKB5x2vXP--
```

Remarquez que la requête est divisée en différentes sections pour chaque champ de formulaire. Les sections sont séparées par la "limite de formulaire", que le navigateur injecte par défaut.

Je vais sauter les détails excessifs, donc si vous voulez en lire plus, consultez `[Content-Disposition](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Disposition)` sur MDN. L'important à savoir est que les requêtes `multipart/form-data` sont beaucoup plus complexes que de simples paires clé/valeur.

La plupart des frameworks serveur fournissent des outils intégrés pour accéder au corps d'une requête. Nous avons donc réinventé la roue. Par exemple, Nuxt fournit une fonction globale `readBody`. Nous aurions donc pu accomplir la même chose sans écrire notre propre code :

```javascript
export default defineEventHandler((event) => {
  const nodeRequestObject = event.node.req;

  const body = await readBody(event.node.req);
  console.log(body)

  return { ok: true };
});
```

Cela fonctionne bien pour d'autres types de contenu, mais pour `multipart/form-data`, cela pose des problèmes. L'ensemble du corps de la requête est lu en mémoire sous forme d'une seule grande chaîne de texte. Cela inclut les informations `Content-Disposition`, les limites de formulaire, et les champs et valeurs du formulaire. Sans parler du fait que les fichiers ne sont même pas écrits sur le disque.

Le gros problème ici est que si un fichier très volumineux est téléchargé, il pourrait consommer toute la mémoire de l'application et la faire planter.

La solution est, une fois de plus, de travailler avec des streams.

Lorsque notre serveur reçoit un chunk de données du stream de requête, au lieu de le stocker en mémoire, nous pouvons le rediriger vers un autre stream. Plus précisément, nous pouvons l'envoyer vers un stream qui écrit des données sur le système de fichiers en utilisant `[createWriteStream](https://nodejs.org/api/fs.html#filehandlecreatewritestreamoptions)`. Au fur et à mesure que les chunks arrivent de la requête, ces données sont écrites sur le système de fichiers, puis libérées de la mémoire.

C'est à peu près aussi loin que je veux aller dans les concepts de bas niveau. Remontons pour résoudre le problème sans réinventer la roue.

## Comment utiliser une bibliothèque pour streamer des données sur le disque

Probablement mon meilleur conseil pour gérer les téléchargements de fichiers est d'utiliser une bibliothèque qui fait tout ce travail pour vous :

* Analyser les requêtes `multipart/form-data`
* Séparer les fichiers des autres champs de formulaire
* Streamer les données de fichiers dans le système de fichiers
* Vous fournir les données des champs de formulaire ainsi que des informations utiles sur les fichiers

Aujourd'hui, je vais utiliser une bibliothèque appelée [formidable](https://github.com/node-formidable/formidable/). Vous pouvez l'installer avec `npm install formidable`, puis l'importer dans votre projet.

```javascript
import formidable from 'formidable';
```

Formidable fonctionne directement avec l'objet de requête Node, que nous avons déjà récupéré de l'événement Nuxt ("Wow, quelle perspicacité incroyable !!" 🤩).

Nous pouvons donc modifier notre fonction `doSomethingWithNodeRequest` pour utiliser formidable à la place. Elle devrait toujours retourner une promesse car formidable utilise des callbacks, mais les promesses sont plus agréables à utiliser. Sinon, nous pouvons principalement remplacer le contenu de la fonction par formidable.

Nous devrons créer une instance formidable et l'utiliser pour analyser l'objet de requête. Tant qu'il n'y a pas d'erreur, nous pouvons résoudre la promesse avec un seul objet qui contient à la fois les champs de formulaire et les fichiers.

```javascript
/**
 * @param {import('http').IncomingMessage} req
 */
function doSomethingWithNodeRequest(req) {
  return new Promise((resolve, reject) => {
    /** @see https://github.com/node-formidable/formidable/ */
    const form = formidable({ multiples: true })
    form.parse(req, (error, fields, files) => {
      if (error) {
        reject(error);
        return;
      }
      resolve({ ...fields, ...files });
    });
  });
}
```

Cela nous fournit une fonction pratique pour analyser `multipart/form-data` en utilisant des promesses et accéder aux champs de formulaire réguliers de la requête, ainsi qu'aux informations sur les fichiers qui ont été écrits sur le disque en utilisant des streams.

Maintenant, nous pouvons examiner le corps de la requête :

```javascript
export default defineEventHandler((event) => {
  const nodeRequestObject = event.node.req;

  const body = await doSomethingWithNodeRequest(event.node.req);
  console.log(body)

  return { ok: true };
});
```

Nous devrions voir un objet contenant tous les champs de formulaire et leurs valeurs, mais pour chaque entrée de fichier, nous verrons un objet qui représente le fichier téléchargé, et non le fichier lui-même. Cet objet contient toutes sortes d'informations utiles, y compris son chemin sur le disque, son nom, son [mimetype](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types), et plus encore.

```javascript
{
  file-input-name: PersistentFile {
    _events: [Object: null prototype] { error: [Function (anonymous)] },
    _eventsCount: 1,
    _maxListeners: undefined,
    lastModifiedDate: 2023-03-21T22:57:42.332Z,
    filepath: '/tmp/d53a9fd346fcc1122e6746600',
    newFilename: 'd53a9fd346fcc1122e6746600',
    originalFilename: 'file.txt',
    mimetype: 'text/plain',
    hashAlgorithm: false,
    size: 13,
    _writeStream: WriteStream {
      fd: null,
      path: '/tmp/d53a9fd346fcc1122e6746600',
      flags: 'w',
      mode: 438,
      start: undefined,
      pos: undefined,
      bytesWritten: 13,
      _writableState: [WritableState],
      _events: [Object: null prototype],
      _eventsCount: 1,
      _maxListeners: undefined,
      [Symbol(kFs)]: [Object],
      [Symbol(kIsPerformingIO)]: false,
      [Symbol(kCapture)]: false
    },
    hash: null,
    [Symbol(kCapture)]: false
  }
}
```

Vous remarquerez également que le `newFilename` est une valeur hachée. Cela garantit que si deux fichiers sont téléchargés avec le même nom, vous ne perdrez pas de données. Vous pouvez, bien sûr, modifier la façon dont les fichiers sont écrits sur le disque.

Notez que dans une application standard, il est bon de stocker certaines de ces informations dans un endroit persistant, comme une base de données, afin de pouvoir facilement trouver tous les fichiers qui ont été téléchargés. Mais ce n'est pas le but de cet article.

Il y a une dernière chose que je veux corriger. Je ne veux traiter que les requêtes `multipart/form-data` avec formidable. Tout le reste peut être géré par un analyseur de corps intégré comme celui que nous avons vu ci-dessus.

Je vais donc créer une variable "body" d'abord, puis vérifier les en-têtes de la requête, et assigner la valeur du corps en fonction du "Content-Type". Je vais également renommer ma fonction en `parseMultipartNodeRequest` pour être plus explicite sur ce qu'elle fait.

Voici à quoi ressemble le tout (notez que `getRequestHeaders` est une autre fonction intégrée de Nuxt) :

```javascript
import formidable from 'formidable';

/**
 * @see https://nuxt.com/docs/guide/concepts/server-engine
 * @see https://github.com/unjs/h3
 */
export default defineEventHandler(async (event) => {
  let body;
  const headers = getRequestHeaders(event);

  if (headers['content-type']?.includes('multipart/form-data')) {
    body = await parseMultipartNodeRequest(event.node.req);
  } else {
    body = await readBody(event);
  }
  console.log(body);

  return { ok: true };
});

/**
 * @param {import('http').IncomingMessage} req
 */
function parseMultipartNodeRequest(req) {
  return new Promise((resolve, reject) => {
    /** @see https://github.com/node-formidable/formidable/ */
    const form = formidable({ multiples: true })
    form.parse(req, (error, fields, files) => {
      if (error) {
        reject(error);
        return;
      }
      resolve({ ...fields, ...files });
    });
  });
}
```

De cette façon, nous avons une API suffisamment robuste pour accepter `multipart/form-data`, du texte brut ou des requêtes encodées en URL.

## 🗣🗣🗣 Conclusion

Il n'y a pas d'emoji cor de rave, donc ceux-ci devront suffire. Nous avons couvert pas mal de choses, alors faisons un petit récapitulatif.

Lorsque nous téléchargeons un fichier en utilisant une requête `multipart/form-data`, le navigateur envoie les données un chunk à la fois, en utilisant un stream. C'est parce que nous ne pouvons pas mettre l'ensemble du fichier dans l'objet de requête en une seule fois.

Dans Node.js, nous pouvons écouter l'événement "data" de la requête pour travailler avec chaque chunk de données au fur et à mesure qu'il arrive. Cela nous donne accès au stream de la requête.

Bien que nous puissions capturer toutes ces données et les stocker en mémoire, ce n'est pas une bonne idée. Un téléchargement de fichier volumineux pourrait consommer toute la mémoire du serveur, le faisant planter.

Au lieu de cela, nous pouvons rediriger ce stream ailleurs, de sorte que chaque chunk soit reçu, traité, puis libéré de la mémoire. Une option est d'utiliser `[fs.createWriteStream](https://nodejs.org/api/fs.html#fscreatewritestreampath-options)` pour créer un `[WritableStream](https://developer.mozilla.org/en-US/docs/Web/API/WritableStream)` qui peut écrire sur le système de fichiers.

Au lieu d'écrire notre propre analyseur de bas niveau, nous devrions utiliser un outil comme formidable. Mais nous devons confirmer que les données proviennent d'une requête `multipart/form-data`. Sinon, nous pouvons utiliser un analyseur de corps standard.

Nous avons couvert beaucoup de concepts de bas niveau et abouti à une solution de haut niveau. Espérons que tout cela avait du sens et que vous avez trouvé cela utile.

Si vous avez des questions ou si quelque chose était confus, n'hésitez pas à [me contacter](https://austingil.com/). Je suis toujours heureux de vous aider.

Merci beaucoup d'avoir lu. Si vous avez aimé cet article et souhaitez me soutenir, les meilleures façons de le faire sont de [le partager](https://twitter.com/share?via=heyAustinGil), [de vous inscrire à ma newsletter](https://austingil.com/newsletter/), et [de me suivre sur Twitter](https://twitter.com/heyAustinGil).