---
title: Comment démarrer avec Fastify
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-23T09:18:21.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-up-and-running-with-fastify-8b7e23781844
coverImage: https://cdn-media-1.freecodecamp.org/images/1*pBOfD2cpJNoFUcVA0Kj-zg.png
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment démarrer avec Fastify
seo_desc: 'By Ethan Arrowood


  Fast and low overhead web framework, for Node.js


  Fastify version 1 was released on March 7th. This post will show you how to get
  it set up, and we’ll discuss some of the incredible features Fastify has to offer.
  No configuration i...'
---

Par Ethan Arrowood

> Framework web rapide et léger, pour Node.js

La version 1 de Fastify a été [publiée le 7 mars](https://medium.com/@fastifyjs/fastify-goes-lts-with-1-0-0-911112c64752). Cet article vous montrera comment l'installer, et nous discuterons de certaines des fonctionnalités incroyables que Fastify a à offrir. Aucune configuration n'est nécessaire — la base de code de Fastify fonctionne sur les versions de Node 6.x, 8.x et 9.x.

#### Prêt ?

Commencez avec `npm i fastify` puis :

```
const fastify = require('fastify')()
```

```
fastify.get('/', (request, reply) => {  reply.send({ hello: 'world' })})
```

```
fastify.listen(3000, err => {  if (err) {    fastify.log.error(err)    process.exit(1)  }  fastify.log.info(    `server listening on ${fastify.server.address().port}`  )})
```

Lancez maintenant votre serveur avec : `node server`

✨ C'est tout ! Vous avez votre premier serveur Fastify en marche.

### Que se passe-t-il ici ?

```
const fastify = require('fastify')()
```

La ligne 1 importe le framework Fastify dans le projet JavaScript et l'instancie. Votre instance de serveur est maintenant stockée dans la variable `fastify`. Vous pouvez passer des options supplémentaires à cette ligne comme ceci :

```
const fastifyWithOptions = require('fastify')({  logger: {    prettyPrint: true   }})
```

Alimenté par le [logger Pino](https://getpino.io/#/), cette option rend la sortie de la console facile à lire et colorée. Consultez la documentation de Pino pour plus d'options de logger, et la documentation de Fastify pour plus d'options d'instance Fastify.

#### Ensuite : le routage

```
fastify.get('/', (request, reply) => {  reply.send({ hello: 'world' })})
```

Les lignes 3 à 5 définissent une [Route](https://www.fastify.io/docs/latest/Routes/) très basique. Les routes sont au cœur de tout serveur backend Node.js. Fastify supporte deux méthodes de définition des routes : la méthode abrégée utilisée ci-dessus, ou une méthode générale `.route` comme montré ci-dessous.

```
fastify.route({  method: 'GET',  url: '/',  handler: function (request, reply) {    reply.send({ hello: 'world' })  }})
```

Ces deux implémentations font exactement la même chose et ont la même performance, alors utilisez simplement celle qui vous semble la plus logique.

La déclaration de route a beaucoup plus d'options disponibles qui ne sont pas montrées ici.

* Fournir un [JSON Schema](http://json-schema.org/) pour les objets de requête et de réponse, ce qui peut augmenter le débit de 10–20%
* Définir une méthode `beforeHandler` qui est appelée juste avant la fonction `handler`. Cela est idéal pour l'authentification, et je démontre comment l'utiliser dans mon [plugin JWT Auth](https://github.com/Ethan-Arrowood/fastify-jwt-authz) (plus sur les plugins Fastify plus tard).

#### Mettez les moteurs en marche ! 3…2…1…C'est parti !

```
fastify.listen(3000, err => {  if (err) {    fastify.log.error(err)    process.exit(1)  }  fastify.log.info(    `server listening on ${fastify.server.address().port}`  )})
```

Enfin, démarrez l'instance Fastify sur le port localhost 3000. C'est la **dernière** étape requise pour créer votre propre instance Fastify. En interne, cette méthode attendra `.ready()` (qui est appelé après le chargement des plugins). Aucune nouvelle route ne peut être définie après avoir appelé la méthode `.listen()`.

### Et ensuite ? Les plugins !

L'une des meilleures fonctionnalités de Fastify est la facilité avec laquelle on peut écrire et incorporer des plugins dans une instance de serveur. Pour commencer, définissez une fonction :

```
function superPlugin (fastify, opts, next) {  fastify.decorate('superMethod', () => {    console.log(`Secret code: ${opts.secretCode}`)  })  next()}
```

Maintenant, en utilisant le module `fastify-plugin`, exportez votre nouveau plugin.

```
const fp = require('fastify-plugin')
```

```
module.exports = fp(superPlugin, {  fastify: '>=1.0.0',  name: 'super-plugin'})
```

Enfin, enregistrez votre plugin sur votre instance Fastify :

```
/* Dans le fichier principal server.js */const superPlugin = require('super-plugin')
```

```
fastify.register(superPlugin, {  secretCode: 'JavaScript est génial !'})
```

Maintenant, vous pouvez appeler la méthode `superMethod` partout où vous avez accès à votre instance Fastify.

```
/* server.js */
```

```
fastify.listen(3000, err => {  fastify.superMethod()})
```

Pour information : vous pouvez enregistrer des plugins dans d'autres plugins, ce qui limite la portée de ce plugin enfant au plugin parent uniquement. Ce sujet est trop avancé pour cet article, donc je ne le couvrirai pas en plus de détails. Vous pouvez lire plus sur les [plugins Fastify ici](https://www.fastify.io/docs/latest/Plugins/). Consultez les fichiers d'exemple complets dans un [Gist Github ici](https://gist.github.com/Ethan-Arrowood/35e54c688e290e8e6a996ccc5c711c2f).

### Allez de l'avant et conquérez

Fastify est rapide. Vraiment très rapide 💡

![Image](https://cdn-media-1.freecodecamp.org/images/7kA4wH6-mzlDXSub9GMnjkXyhrhPwml4x64i)
_[Benchmark Fastify v1.1.x](https://www.fastify.io/benchmarks/" rel="noopener" target="_blank" title=")_

Après cette brève introduction, je vous encourage à découvrir tout ce que [Fastify a à offrir](https://www.fastify.io/docs/latest/). Si vous aimez la programmation open source, Fastify est un excellent projet auquel [contribuer](https://github.com/fastify/fastify/issues). Il existe également un excellent [écosystème de plugins](https://www.fastify.io/ecosystem/) à découvrir et auquel contribuer !

Continuez le bon travail ~ Ethan Arrowood

[**Ethan Arrowood 💡 (@ArrowoodTech) | Twitter**](https://twitter.com/arrowoodtech)  
[**Les derniers Tweets de Ethan Arrowood 💡 (@ArrowoodTech). toujours à l'écoute de la musique. probablement en train de contribuer à l'open…twitter.com](https://twitter.com/arrowoodtech)  [**Ethan-Arrowood (Ethan Arrowood)**](https://github.com/Ethan-Arrowood)  
[_Ethan-Arrowood a 80 dépôts disponibles. Suivez leur code sur GitHub._github.com](https://github.com/Ethan-Arrowood)