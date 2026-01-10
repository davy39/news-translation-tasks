---
title: Quel est le bon Content-Type pour JSON ? Explication du type MIME de l'en-tête
  de requête
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-12-08T22:07:17.000Z'
originalURL: https://freecodecamp.org/news/what-is-the-correct-content-type-for-json-request-header-mime-type-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fcf4739e6787e098393bd6d.jpg
tags:
- name: browser
  slug: browser
- name: internet
  slug: internet
- name: json
  slug: json
- name: servers
  slug: servers
seo_title: Quel est le bon Content-Type pour JSON ? Explication du type MIME de l'en-tête
  de requête
seo_desc: 'By Dillion Megida

  Every resource used on the internet has a media type, also known as a MIME type
  which stands for Multipurpose Internet Mail Extension. This information is necessary
  for transactions between server and client.

  The browser needs to kn...'
---

Par Dillion Megida

Chaque ressource utilisée sur Internet possède un type de média, également appelé type MIME (Multipurpose Internet Mail Extension). Ces informations sont nécessaires pour les transactions entre le serveur et le client.

Le navigateur doit connaître le type de média des ressources qui lui sont envoyées afin de pouvoir les traiter correctement.

Il en va de même pour le serveur. Il doit connaître le type de ressources qui lui sont envoyées pour un analyse et un traitement précis.

## Où le Content-Type est-il déclaré ?

Le type de média de toute ressource est déclaré dans la propriété `Content-Type` de l'en-tête de requête (sur le client, lors de l'envoi d'une requête au serveur) ou dans l'en-tête de réponse (sur le serveur, lors de l'envoi d'une réponse).

Sans déclarer explicitement le type de contenu d'une ressource, le client peut tenter de détecter automatiquement le type, mais le résultat peut ne pas être précis. C'est pourquoi il est important de le déclarer explicitement.

## Types de médias

Les types de médias existent sous diverses formes. Ils sont classés en différents groupes :

- application
- audio
- font
- example
- image
- message
- model
- multipart
- text
- et video

Ces catégories ont également leurs propres types. Par exemple, `application/json` est un type sous `application` et `text/html` est un type sous `text`.

Vous pouvez trouver une liste complète des types de médias sur le site de l'[IANA](https://www.iana.org/assignments/media-types/media-types.xhtml) (un organisme qui coordonne certains des éléments clés d'Internet).

Tous ces types couvrent divers types de données tels que le texte, l'audio, les images, le HTML et bien d'autres types utilisés sur Internet.

## Le navigateur doit connaître le type de média d'une ressource

Comme je l'ai mentionné ci-dessus, le navigateur doit savoir quel type de contenu il reçoit. Voici un exemple pour illustrer cela.

Le code suivant est un serveur Node qui sert un fichier HTML :

```js
const http = require("http");
const fs = require("fs");
const path = require("path");

const server = http.createServer(function (req, res) {
	const filePath = path.join(__dirname, "index.html");
	var stat = fs.statSync(filePath);

	res.writeHead(200, {
		"Content-Type": "text/css",
		"Content-Length": stat.size,
	});

	const readStream = fs.createReadStream(filePath);
	readStream.pipe(res);
});

server.listen(5000);

console.log("Serveur web Node.js sur le port 5000 est en cours d'exécution..");
```

Ne vous inquiétez pas des détails du code. Tout ce qui vous intéresse, c'est le fichier `index.html` que nous servons et le fait que le `Content-Type` est `text/css`.

Voici le contenu de `index.html` :

```html
<h1>Page d'accueil</h1>
```

Bien sûr, un document HTML est différent d'un fichier CSS. Voici le résultat sur `localhost:5000` lorsque le serveur est démarré :

![Screenshot-2020-12-08-at-10.12.32](https://www.freecodecamp.org/news/content/images/2020/12/Screenshot-2020-12-08-at-10.12.32.png)

Vous pouvez également confirmer la réponse obtenue en vérifiant les en-têtes dans l'onglet réseau des DevTools.

Voici le résultat sur un navigateur Chrome :

![Screenshot-2020-12-08-at-10.13.34](https://www.freecodecamp.org/news/content/images/2020/12/Screenshot-2020-12-08-at-10.13.34.png)

Le navigateur a reçu le contenu comme un type CSS, donc il a essayé de le traiter comme du CSS.

Notez également que la connaissance complète du type de contenu reçu par le navigateur réduit les vulnérabilités de sécurité, car le navigateur connaît les normes de sécurité à mettre en place pour ces données.

Maintenant que vous comprenez le concept des types MIME et leur importance, passons à JSON.

## Le bon Content-Type pour JSON

JSON doit être correctement interprété par le navigateur pour être utilisé de manière appropriée. `text/plain` était généralement utilisé pour JSON, mais selon l'[IANA](https://www.iana.org/assignments/media-types/media-types.xhtml), le type MIME officiel pour JSON est `application/json`.

Cela signifie que lorsque vous envoyez du JSON au serveur ou recevez du JSON du serveur, vous devez toujours déclarer le `Content-Type` de l'en-tête comme `application/json`, car c'est la norme que le client et le serveur comprennent.

## Conclusion

Comme indiqué ci-dessus, le serveur (comme le navigateur) doit connaître le type de données qui lui est envoyé, par exemple, dans une requête POST. C'est la raison pour laquelle les `formulaires` avec des fichiers contiennent généralement l'attribut `enctype` avec une valeur de `multipart/form-data`.

Sans encoder la requête de cette manière, la requête POST ne fonctionnera pas. De plus, une fois que le serveur connaît le type de données qu'il a reçu, il sait alors comment analyser les données encodées.

Dans cet article, nous avons examiné ce que sont les types MIME et leur but. Nous avons également vu le type de contenu officiel pour JSON. J'espère que vous savez maintenant pourquoi il est important de déclarer les types de ressources lorsqu'ils sont utilisés sur Internet.