---
title: Comment simplifier et nettoyer la validation des entrées dans votre application
  Express.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-18T22:08:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-input-validation-simple-and-clean-in-your-express-js-app-ea9b5ff5a8a7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*e0mCbx2PuNysG54g0B1gRg.jpeg
tags:
- name: Express.js
  slug: expressjs
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: Productivity
  slug: productivity
- name: Web Development
  slug: web-development
seo_title: Comment simplifier et nettoyer la validation des entrées dans votre application
  Express.js
seo_desc: 'By Shailesh Shekhawat


  This tutorial requires prior knowledge of using the expressjs framework


  Why do we need server-side validation?


  Your client side validation is not enough and it may be subverted

  More prone to Man in middle attacks, and the ser...'
---

Par Shailesh Shekhawat

> Ce tutoriel nécessite des connaissances préalables sur l'utilisation du framework [expressjs](http://expressjs.com)

#### Pourquoi avons-nous besoin d'une validation côté serveur ?

* Votre validation côté client n'est pas suffisante et peut être contournée
* Plus vulnérable aux [attaques de l'homme du milieu](https://en.wikipedia.org/wiki/Man-in-the-middle_attack), et le serveur ne doit jamais faire confiance au côté client
* Un utilisateur peut désactiver la validation JavaScript côté client et manipuler les données

Si vous avez construit des applications web en utilisant un framework Express ou tout autre framework Node.js, la validation joue un rôle crucial dans toute application web qui vous oblige à valider le `body`, `param` ou `query` de la requête.

Écrire votre propre fonction middleware peut être fastidieux si

* vous voulez avancer rapidement tout en maintenant la qualité du code ou
* vous voulez éviter d'utiliser `**if** (**req**.body.head)` ou `**if** (**req**.params.isCool)` dans votre fonction de contrôleur principale où vous définissez la logique métier

Dans ce tutoriel, vous apprendrez comment valider les entrées dans une application Express.js en utilisant un module open source et populaire appelé [express-validator](https://github.com/ctavan/express-validator).

### Introduction à express-validator

La définition sur Github dit :

> express-validator est un ensemble de middlewares [express.js](http://expressjs.com/) qui enveloppe les fonctions de validation et de nettoyage de [validator.js](https://github.com/chriso/validator.js).

Le module implémente cinq API importantes :

* Check API
* Filter API
* Sanitization chain API
* Validation chain API
* Validation Result API

Examinons une route utilisateur de base `/route/user.js` sans aucun module de validation pour créer un utilisateur :

```js
/**
* @api {post} /api/user Créer un utilisateur
* @apiName Créer un nouvel utilisateur
* @apiPermission admin
* @apiGroup User
*
* @apiParam  {String} [userName] nom d'utilisateur
* @apiParam  {String} [email] Email
* @apiParam  {String} [phone] Numéro de téléphone
* @apiParam  {String} [status] Statut
*
* @apiSuccess (200) {Object} mixed objet `User`
*/

router.post('/', userController.createUser)
```

Maintenant dans le contrôleur utilisateur `/controllers/user.js`

```js
const User = require('./models/user')

exports.createUser = (req, res, next) => {
  /** Ici, vous devez valider l'entrée de l'utilisateur. 
   Disons que seul le nom et l'email sont des champs obligatoires
 */
  
  const { userName, email, phone, status } = req.body
  if (userName && email &&  isValidEmail(email)) { 
    
    // isValidEmail est une fonction personnalisée pour valider l'email que vous pourriez devoir écrire vous-même ou utiliser un module npm
    User.create({
      userName,
      email,
      phone,
      status,   
    })
    .then(user => res.json(user))
    .catch(next)
  }
}
```

Le code ci-dessus est juste un exemple de base de validation des champs par vous-même.

Vous pouvez gérer certaines validations dans votre modèle utilisateur en utilisant Mongoose. Pour les meilleures pratiques, nous voulons nous assurer que la validation se produit avant la logique métier.

[express-validator](https://github.com/ctavan/express-validator) prendra en charge toutes ces validations ainsi que le [nettoyage](https://www.quora.com/What-does-it-mean-to-sanitize-a-field-How-is-that-related-to-escaping-as-in-entering-in-malicious-input-that-escapes-or-something) des entrées.

#### **Installation**

```bash
npm install --save express-validator
```

Incluez le **module** dans votre fichier principal `server.js` :

```js
const express = require('express')
const bodyParser = require('body-parser')
const expressValidator = require('express-validator')
const app = express()
const router = express.Router()

app.use(bodyParser.json())

app.use(expressValidator())

app.use('/api', router)
```

Maintenant, en utilisant [express-validator](https://github.com/ctavan/express-validator), votre `/routes/user.js` ressemblera à ceci :

```js
router.post(
  '/', 
  userController.validate('createUser'), 
  userController.createUser,
)
```

Ici, `userController.validate` est une fonction middleware qui est expliquée ci-dessous. Elle accepte le nom de la `méthode` pour laquelle la validation sera utilisée.

Créons une fonction middleware `validate()` dans notre `/controllers/user.js` :

```js
const { body } = require('express-validator/check')

exports.validate = (method) => {
  switch (method) {
    case 'createUser': {
     return [ 
        body('userName', "userName n'existe pas").exists(),
        body('email', 'Email invalide').exists().isEmail(),
        body('phone').optional().isInt(),
        body('status').optional().isIn(['enabled', 'disabled'])
       ]   
    }
  }
}
```

Veuillez vous référer à [cet article](https://express-validator.github.io/docs/check-api.html) pour en savoir plus sur la définition des fonctions et leur utilisation.

La fonction `body` ne validera que `req.body` et prend deux arguments. Le premier est le `nom de la propriété`. Le second est votre `message` personnalisé qui sera affiché si la validation échoue. Si vous ne fournissez pas de message personnalisé, alors le message par défaut sera utilisé.

Comme vous pouvez le voir, pour un champ `obligatoire`, nous utilisons la méthode `.exists()`. Nous utilisons `.optional()` pour un champ `optionnel`. De même, `isEmail()` et `isInt()` sont utilisés pour valider l'`email` et l'`entier`.

Si vous voulez qu'un champ d'entrée n'inclue que certaines valeurs, alors vous pouvez utiliser `.isIn([])`. Cela prend un `tableau` de valeurs, et si vous recevez des valeurs autres que celles ci-dessus, alors une erreur sera générée.

Par exemple, le champ de statut dans l'extrait de code ci-dessus ne peut avoir qu'une valeur `enabled` ou `disabled`. Si vous fournissez une valeur autre que celle-ci, une erreur sera générée.

Dans `/controllers/user.js`, écrivons une fonction `**createUser**` où vous pouvez écrire la logique métier. Elle sera appelée après `**validate()**` avec le résultat des validations.

```js
const { validationResult } = require('express-validator/check');

exports.createUser = async (req, res, next) => {
   try {
      const errors = validationResult(req); // Trouve les erreurs de validation dans cette requête et les enveloppe dans un objet avec des fonctions pratiques

      if (!errors.isEmpty()) {
        res.status(422).json({ errors: errors.array() });
        return;
      }

      const { userName, email, phone, status } = req.body
      
      const user = await User.create({

        userName,

        email,

        phone,

        status,   
      })

      res.json(user)
   } catch(err) {
     return next(err)
   }
}
```

#### Si vous vous demandez ce qu'est validationResult(req) ?

**Cette fonction trouve les erreurs de validation dans cette requête et les enveloppe dans un objet avec des fonctions pratiques**

Maintenant, chaque fois que la requête inclut des paramètres de corps invalides ou que le champ `userName` est manquant dans `req.body`, votre serveur répondra comme ceci :

```js
{
  "errors": [{
    "location": "body",
    "msg": "userName est requis",
    "param": "userName"
  }]
}
```

Ainsi, si `userName` ou `email` ne satisfait pas la validation, chaque erreur retournée par la méthode `.array()` a le format suivant par défaut :

```js
{   
  "msg": "Le message d'erreur",
   
  "param": "nom du paramètre", 
  
  "value": "valeur du paramètre",   
  // Emplacement du paramètre qui a généré cette erreur.   
  // Il s'agit soit de body, query, params, cookies ou headers.   
  "location": "body",    
  
  // nestedErrors n'existe que lors de l'utilisation de la fonction oneOf
  "nestedErrors": [{ ... }] 
}
```

Comme vous pouvez le voir, ce module nous aide vraiment à prendre en charge la plupart des validations par lui-même. Il maintient également la qualité du code et se concentre principalement sur la logique métier.

C'était l'introduction à la validation des entrées en utilisant le module **express-validator** et découvrez comment valider un tableau d'éléments et créer votre propre validation personnalisée dans la [Partie 2](https://www.freecodecamp.org/news/how-to-perform-custom-validation-in-your-express-js-app-432eb423510f/) de cette série.

J'ai fait de mon mieux et j'espère avoir couvert suffisamment de détails pour que vous puissiez commencer.

Si vous rencontrez des problèmes, n'hésitez pas à _me [contacter](https://101node.io) ou à commenter ci-dessous_.  
Je serais heureux de vous aider :)

Suivez [Shailesh Shekhawat](https://www.freecodecamp.org/news/author/thatshailesh/) pour être notifié chaque fois que je publie un nouveau post.

_N'hésitez pas à applaudir si vous avez trouvé cela utile !_

_Originalement publié sur [101node.io](https://101node.io/blog/how-to-validate-inputs-in-express-js-app/) le 2 septembre 2018._