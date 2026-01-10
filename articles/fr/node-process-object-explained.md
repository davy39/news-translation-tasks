---
title: Objet Process de Node Expliqué
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-26T21:29:00.000Z'
originalURL: https://freecodecamp.org/news/node-process-object-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d7e740569d1a4ca380e.jpg
tags:
- name: node
  slug: node
- name: Node.js
  slug: nodejs
- name: toothbrush
  slug: toothbrush
seo_title: Objet Process de Node Expliqué
seo_desc: The process object in Node.js is a global object that can be accessed inside
  any module without requiring it. There are very few global objects or properties
  provided in Node.js and process is one of them. It is an essential component in
  the Node.js ...
---

L'objet `process` dans Node.js est un objet global accessible dans n'importe quel module sans avoir besoin de l'importer. Il existe très peu d'objets ou de propriétés globaux fournis dans Node.js et `process` en fait partie. C'est un composant essentiel dans l'écosystème Node.js car il fournit divers ensembles d'informations sur le runtime d'un programme. 

Pour explorer, nous utiliserons l'une de ses propriétés appelée `process.versions`. Cette propriété nous indique les informations sur la version de Node.js que nous avons installée. Elle doit être utilisée avec le flag `-p`.

```shell
$ node  -p "process.versions"

# output
{ http_parser: '2.8.0',
  node: '8.11.2',
  v8: '6.2.414.54',
  uv: '1.19.1',
  zlib: '1.2.11',
  ares: '1.10.1-DEV',
  modules: '57',
  nghttp2: '1.29.0',
  napi: '3',
  openssl: '1.0.2o',
  icu: '60.1',
  unicode: '10.0',
  cldr: '32.0',
  tz: '2017c' }
```

Une autre propriété que vous pouvez vérifier est `process.release`, qui est similaire à la commande `$ node --version` que nous avons utilisée lors de l'installation de Node.js. Mais cette fois, la sortie sera plus détaillée.

```shell
node -p "process.release"

# output
{ name: 'node',
  lts: 'Carbon',
  sourceUrl: 'https://nodejs.org/download/release/v8.11.2/node-v8.11.2.tar.gz',
  headersUrl: 'https://nodejs.org/download/release/v8.11.2/node-v8.11.2-headers.tar.gz' }
```

Ce sont quelques-unes des différentes commandes que nous pouvons utiliser en ligne de commande pour accéder à des informations qu'aucun module ne peut fournir autrement. 

Cet objet `process` est une instance de la classe EventEmitter. Il contient ses propres événements prédéfinis tels que `exit`, qui peut être utilisé pour savoir quand un programme Node.js a terminé son exécution. 

Exécutez le programme ci-dessous et vous pouvez observer que le résultat s'affiche avec le code de statut `0`. Dans Node.js, ce code de statut signifie qu'un programme s'est exécuté avec succès.

```js
process.on('exit', code => {
	setTimeout(() => {
		console.log('Ne sera pas affiché');
	}, 0);

	console.log('Sorti avec le code de statut :', code);
});
console.log('Exécution terminée');
```

Sortie du programme ci-dessus :

```shell
Exécution terminée
Sorti avec le code de statut : 0
```

`Process` fournit également diverses propriétés pour interagir. Certaines d'entre elles peuvent être utilisées dans une application Node pour fournir une passerelle de communication entre l'application Node et une interface de ligne de commande. Cela est très utile si vous construisez une application ou un utilitaire de ligne de commande avec Node.js

* process.stdin : un flux lisible
* process.stdout : un flux inscriptible
* process.stderr : un flux inscriptible pour reconnaître les erreurs

En utilisant `argv`, vous pouvez toujours accéder aux arguments passés en ligne de commande. `argv` est un tableau qui contient Node lui-même comme premier élément et le chemin absolu du fichier comme deuxième élément. À partir du troisième élément, il peut contenir autant d'arguments que vous le souhaitez.

Essayez le programme ci-dessous pour mieux comprendre comment utiliser ces différentes propriétés et fonctions.

```js
process.stdout.write('Bonjour le monde!' + '\n');

process.argv.forEach(function(val, index, array) {
	console.log(index + ': ' + val);
});
```

Si vous exécutez le code ci-dessus avec la commande suivante, vous obtiendrez la sortie et les deux premiers éléments de `argv` seront affichés.

```shell
$ node test.js

# output
Bonjour le monde!
0: /usr/local/bin/node
1: /Users/amanhimself/Desktop/articles/nodejs-text-tuts/test.js
```