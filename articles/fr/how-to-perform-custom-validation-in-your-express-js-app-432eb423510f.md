---
title: Comment effectuer une validation personnalisée dans votre application Express.js
  (Partie 2)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-01T22:46:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-perform-custom-validation-in-your-express-js-app-432eb423510f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KOwj7MMEgc1V_9t6EQP2ag.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment effectuer une validation personnalisée dans votre application Express.js
  (Partie 2)
seo_desc: 'By Shailesh Shekhawat

  In the previous post, I showed how to get started with input validation in an express.js
  application. I used the express-validator module and discussed its important features
  with implementation.

  If you haven’t checked that out,...'
---

Par Shailesh Shekhawat

Dans le [précédent article](https://medium.freecodecamp.org/how-to-make-input-validation-simple-and-clean-in-your-express-js-app-ea9b5ff5a8a7), j'ai montré comment commencer avec la validation des entrées dans une application express.js. J'ai utilisé le module [express-validator](https://github.com/ctavan/express-validator) et discuté de ses fonctionnalités importantes avec mise en œuvre.

Si vous ne l'avez pas encore consulté, veuillez lire le premier article [ici](https://medium.freecodecamp.org/how-to-make-input-validation-simple-and-clean-in-your-express-js-app-ea9b5ff5a8a7).

Alors maintenant, commençons. Dans la partie 2 de ce tutoriel, vous apprendrez comment effectuer une validation personnalisée dans une application Express.js.

### Ce que vous pouvez réaliser avec la validation personnalisée

* Elle peut être utilisée pour vérifier l'existence de l'entité dans votre base de données.
* Également pour tester si une certaine valeur existe dans un tableau, un objet, une chaîne, etc.
* Si vous souhaitez changer le format des données lui-même.

Et bien plus encore…

La bibliothèque [express-validator](https://express-validator.github.io/docs/) fournit une méthode `custom` que vous pouvez utiliser pour effectuer toutes sortes de validations personnalisées.

L'implémentation d'un validateur personnalisé utilise la méthode de chaîne [.custom()](https://express-validator.github.io/docs/validation-chain-api.html#customvalidator). Elle prend une fonction de validation.

Les validateurs personnalisés retournent des Promesses pour montrer une validation asynchrone ou `throw` n'importe quelle valeur/rejeter une promesse pour [utiliser un message d'erreur personnalisé](https://express-validator.github.io/docs/custom-error-messages.html#custom-validator-level).

Maintenant, je vais vous montrer des exemples des cas d'utilisation de validation personnalisée ci-dessus.

### Vérifier si l'entité existe dans votre base de données

Un point important que j'utilise au quotidien — et je suppose que vous l'utiliserez pour vérifier une entité contre une base de données.

Par exemple, si quelqu'un demande à mettre à jour son nom, vous l'utiliseriez pour une requête `PUT` basique `/api/users/:userId`.

Pour vous assurer que l'utilisateur doit exister dans notre base de données, j'ai créé une fonction pour vérifier contre la base de données.

```js
param('userId')
.exists()
.isMongoId()
.custom(val => UserSchema.isValidUser(val))
```

`isValidUser()` est une fonction statique qui effectuera un appel asynchrone à la base de données et vérifiera si l'utilisateur existe ou non.

Écrivons une fonction statique dans le `Schema` de mongoose :

```js
UserSchema.statics = {
   isValid(id) {
      return this.findById(id)
             .then(result => {
                if (!result) throw new Error('User not found')
      })
   },
}
```

Comme nous ne pouvons pas faire confiance à l'`userId` envoyé par le client uniquement sur la base de son format, nous devons nous assurer qu'il s'agit d'un compte réel.

### **Vérifier par rapport à certaines valeurs dans un tableau ou un objet**

Par exemple, si vous souhaitez appliquer une règle sur un **nom d'utilisateur** qui doit contenir un caractère `@`.

Ainsi, dans votre requête `POST` de création d'utilisateur ou lors de la mise à jour, vous pouvez faire quelque chose comme ceci :

```js
body('username', 'Nom d\'utilisateur invalide')
.exists()
.isString().isLowercase()
.custom(val => {   
   
   if (val.indexOf('@') !== -1) return true
    
   return false
}),
```

> _Rappel : Toujours retourner une valeur booléenne depuis le callback de la fonction `.custom()`. Sinon, votre validation pourrait ne pas fonctionner comme souhaité._

Comme vous pouvez le voir, nous pouvons effectuer toutes ces validations, y compris les validations asynchrones, directement dans le middleware au lieu de les faire dans un contrôleur.

<iframe src="https://giphy.com/embed/TkERwbWzAxvfa" width="480" height="360" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>

### Changer le format des données d'entrée

La bibliothèque dispose d'une fonctionnalité de [Nettoyage](https://express-validator.github.io/docs/sanitization.html) où le nettoyage personnalisé est effectué en utilisant `customerSanitizer()`.

Je l'ai utilisée pour changer la chaîne de valeurs séparées par des virgules en un tableau de chaînes.

Par exemple, nous avons une base de données de médecins. Quelqu'un veut obtenir uniquement les médecins qui sont **cardiologues** et **psychiatres**.

Nous avons stocké ces deux spécialisations sous forme de `**type**` dans notre base de données.

Une simple requête `GET` ressemblera à ceci :

```
GET /api/doctors?type=cardiologists,psychiatrist
```

Maintenant dans `mongodb`, nous pouvons utiliser l'opérateur `**$in**` pour rechercher plusieurs valeurs d'une propriété.

Une requête de base de données basique peut ressembler à ceci :

```js
Doctors.find({
   type: {
       
     $in: ['cardiologists', 'psychiatrist']
       
   }
})
```

Cela vous donnera tous les cardiologues et psychiatres.

À partir de la requête `GET` :

```js
req.query = {

  type: "cardiologists,psychiatrist"
  
}
```

Comme vous pouvez le voir dans `req.query`, vous obtiendrez une propriété `type` dont le type est une `string`.

Avec l'aide de `.customSanitizer()`, nous sommes en mesure de convertir une chaîne en un tableau de chaînes.

Au niveau de la validation :

```js
const commaToArray  = (value = '') => value.split(',')

sanitizeQuery('type').customSanitizer(commaToArray),
```

Maintenant, nous pouvons directement l'alimenter dans la requête de base de données pour l'opérateur `**$in**`.

**Et si je veux appliquer certaines règles à tous les éléments d'un tableau ou aux clés d'objets ?**

<iframe src="https://giphy.com/embed/a5viI92PAF89q" width="480" height="331" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/reaction-a5viI92PAF89q">via GIPHY</a></p>

#### Corps :

```js
{
  items:[
    {_id: 'someObjectId', number: '200'},
    ...
  ]
}
```

### Caractères génériques

Le caractère générique est l'une des grandes fonctionnalités de ce module. Il vous permet d'itérer sur un tableau d'éléments ou de clés d'objet et de valider chaque élément ou ses propriétés.

Le caractère `*` est également connu sous le nom de caractère générique.

Imaginez que je veux valider tous les `_id, number` des éléments.

```js
check('items.*._id')
.exists()
.isMongoId()
.custom(val => ItemSchema.isValid(val)), // similaire à isValidUser() 
sanitize('items.*.number').toInt()
```

Voilà — une introduction à la validation des entrées en utilisant le module express-validator.

Si vous rencontrez des problèmes, n'hésitez pas à [me contacter](https://101node.io) ou à commenter ci-dessous. 
Je serais heureux de vous aider :)

_N'hésitez pas à applaudir si vous avez trouvé cela utile !_

Suivez [Shailesh Shekhawat](https://www.freecodecamp.org/news/author/thatshailesh/) pour être notifié chaque fois que je publie un nouvel article.

_Publié à l'origine sur [101node.io](https://101node.io/blog/how-to-make-input-validation-in-express-js-app-part-2/) le 22 septembre 2018._