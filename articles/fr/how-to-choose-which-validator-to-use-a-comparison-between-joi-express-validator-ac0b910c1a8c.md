---
title: 'Comment choisir quel validateur utiliser : une comparaison entre Joi et express-validator'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-09T16:28:17.000Z'
originalURL: https://freecodecamp.org/news/how-to-choose-which-validator-to-use-a-comparison-between-joi-express-validator-ac0b910c1a8c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*s3Fzn57ud8r82T56w9biWg.png
tags:
- name: Express.js
  slug: expressjs
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: 'Comment choisir quel validateur utiliser : une comparaison entre Joi et
  express-validator'
seo_desc: 'By Shailesh Shekhawat

  Imagine you have an e-commerce website and you’re allowing users to create accounts
  using their name and email. You want to make sure they sign up with real names,
  not something like cool_dud3.

  That''s where we use validation to ...'
---

Par Shailesh Shekhawat

Imaginez que vous avez un site web de commerce électronique et que vous permettez aux utilisateurs de créer des comptes en utilisant leur nom et leur email. Vous voulez vous assurer qu'ils s'inscrivent avec de vrais noms, pas quelque chose comme cool_dud3.

C'est là que nous utilisons la validation pour valider les entrées et nous assurer que les données d'entrée suivent certaines règles.

Sur le marché, nous avons déjà un tas de bibliothèques de validation, mais je vais comparer deux bibliothèques de validation importantes : [Joi](https://github.com/hapijs/joi) et [express-validator](https://github.com/express-validator/express-validator) pour les **applications basées sur express.js**.

Cette comparaison est utile lorsque vous avez décidé d'utiliser une bibliothèque de validation d'entrée externe pour votre application construite sur **expressjs** et que vous n'êtes pas tout à fait sûr de celle à utiliser.

### Qui est quoi ?

#### Joi

Joi vous permet de créer des _plans_ ou des _schémas_ pour les objets JavaScript (un objet qui stocke des informations) afin d'assurer la _validation_ des informations clés.

#### Express-validator

_express-validator_ est un ensemble de [express.js](http://expressjs.com/) middlewares qui enveloppe les fonctions de validation et de nettoyage de [validator.js](https://github.com/chriso/validator.js).

Donc par définition, nous pouvons dire que :

* Joi peut être utilisé pour créer des schémas (comme nous utilisons mongoose pour créer des schémas NoSQL) et vous pouvez l'utiliser avec des objets JavaScript simples. C'est comme une bibliothèque plug n play et est facile à utiliser.
* D'autre part, _express-validator_ utilise [validator.js](https://github.com/chriso/validator.js) pour valider les routes expressjs, et il est principalement construit pour les applications express.js. Cela rend cette bibliothèque plus niche et fournit une validation et un nettoyage personnalisés prêts à l'emploi. De plus, je le trouve personnellement facile à comprendre :)

Trop de méthodes et d'API pour faire certaines validations dans Joi peuvent vous submerger, donc vous pourriez finir par fermer l'onglet.

Mais je peux me tromper — alors gardons les opinions de côté et comparons les deux bibliothèques.

### Instantiation

#### Joi

Dans Joi, vous devez utiliser `**Joi.object()**` pour instancier un objet de schéma Joi avec lequel travailler.

Tous les schémas nécessitent `Joi.object()` pour traiter la validation et d'autres fonctionnalités de Joi.

Vous devez lire séparément `req.body`, `req.params`, `req.query` pour le corps de la requête, les paramètres et la requête.

```js
const Joi = require('joi');

const schema = Joi.object().keys({
   // valider les champs ici
})
```

#### Express-validator

Vous pouvez simplement requérir _express-validator_ et commencer à utiliser ses méthodes. Vous n'avez pas besoin de lire les valeurs de `req.body`, `req.params`, et `req.query` séparément.

Vous devez simplement utiliser les méthodes `param, query, body` ci-dessous pour valider les entrées respectivement comme vous pouvez le voir ici :

```js
const {
  param, query, cookies, header 
  body, validationResult } = require('express-validator/check')

app.post('/user', [   
    
// valider les champs ici
 
], (req, res) => {
const errors = validationResult(req);
   
  if (!errors.isEmpty()) {     
    return res.status(422).json({ errors: errors.array() });   
  }
}
```

#### Le champ est requis

Prenons un exemple très basique où nous voulons nous assurer qu'un `username` doit être une chaîne de caractères requise et est `alphaNumérique` avec un nombre `min` et `max` de caractères.

* **Joi :**

```js
const Joi = require('joi');
const schema = Joi.object().keys({
    username: Joi.string().alphanum().min(3).max(30).required()
})

app.post('/user', (req, res, next) => {   
  const result = Joi.validate(req.body, schema)
  if (result.error) {
    return res.status(400).json({ error: result.error });
  }
});
```

* **Express-validator**

```js
const { body, validationResult } = require('express-validator/check')

app.post('/user', [   
 body('username')
  .isString()
  .isAlphanumeric()
  .isLength({min: 3, max: 30})
  .exists(), 
], (req, res) => {
  const errors = validationResult(req);
   
  if (!errors.isEmpty()) {     
    return res.status(422).json({ errors: errors.array() });   
  }
}
```

### Nettoyage

Le nettoyage consiste essentiellement à vérifier l'entrée pour s'assurer qu'elle est exempt de bruit, par exemple, nous avons tous utilisé `.trim()` sur une chaîne pour supprimer les espaces.

Ou si vous avez été confronté à une situation où un nombre arrive sous forme de `"1"`, dans ces cas, nous voulons nettoyer et convertir le type pendant l'exécution.

Malheureusement, Joi ne fournit pas de nettoyage prêt à l'emploi, mais _express-validator_ le fait.

#### Exemple : conversion en ObjectID de MongoDB

```js
const { sanitizeParam } = require('express-validator/filter');  

app.post('/object/:id',  
   sanitizeParam('id')
  .customSanitizer(value => {
     return ObjectId(value); 
}), (req, res) => {   // Gérer la requête });
```

### Validation personnalisée

#### Joi : **.extend(**`extension`**)**

Cela crée une nouvelle instance Joi personnalisée avec l'extension que vous fournissez incluse.

L'extension utilise certaines structures courantes qui doivent être décrites d'abord :

* `value` - la valeur traitée par Joi.
* `state` - un objet contenant le contexte actuel de la validation.
* `key` - la clé de la valeur actuelle.
* `path` - le chemin complet de la valeur actuelle.
* `parent` - le parent potentiel de la valeur actuelle.
* `options` - objet d'options fourni via `[any().options()](https://github.com/hapijs/joi/blob/master/API.md#anyoptionsoptions)` ou `[Joi.validate()](https://github.com/hapijs/joi/blob/master/API.md#validatevalue-schema-options-callback)`.

#### Extension

`extension` peut être :

* un seul objet d'extension
* une fonction de fabrication générant un objet d'extension
* ou un tableau de ceux-ci

Les objets d'extension utilisent les paramètres suivants :

* `name` - nom du nouveau type que vous définissez, cela peut être un type existant. Requis.
* `base` - un schéma Joi existant sur lequel baser votre type. Par défaut `Joi.any()`.
* `coerce` - une fonction optionnelle qui s'exécute avant la base, sert généralement lorsque vous souhaitez forcer les valeurs d'un type différent de votre base. Elle prend 3 arguments `value`, `state` et `options`.
* `pre` - une fonction optionnelle qui s'exécute en premier dans la chaîne de validation, sert généralement lorsque vous devez convertir des valeurs. Elle prend 3 arguments `value`, `state` et `options`.
* `language` - un objet optionnel pour ajouter des définitions d'erreurs. Chaque clé sera préfixée par le nom du type.
* `describe` - une fonction optionnelle prenant la description entièrement formée pour la post-traiter.
* `rules` - un tableau optionnel de règles à ajouter.
* `name` - nom de la nouvelle règle. Requis.
* `params` - un objet optionnel contenant des schémas Joi de chaque paramètre ordonné. Vous pouvez également passer un seul schéma Joi tant qu'il s'agit d'un `Joi.object()`. Bien sûr, certaines méthodes comme `pattern` ou `rename` ne seront pas utiles ou ne fonctionneront pas du tout dans ce contexte donné.
* `setup` - une fonction optionnelle qui prend un objet avec les paramètres fournis pour permettre la manipulation interne du schéma lorsqu'une règle est définie. Vous pouvez optionnellement retourner un nouveau schéma Joi qui sera pris comme la nouvelle instance de schéma. Au moins l'un de `setup` ou `validate` doit être fourni.
* `validate` - une fonction optionnelle pour valider les valeurs qui prend 4 paramètres `params`, `value`, `state` et `options`. Au moins l'un de `setup` ou `validate` doit être fourni.
* `description` - une chaîne optionnelle ou une fonction prenant les paramètres comme argument pour décrire ce que fait la règle.

**Exemple :**

```js
joi.extend((joi) => ({
    base: joi.object().keys({
        name: joi.string(),
        age: joi.number(),
        adult: joi.bool().optional(),
    }),
    name: 'person',
    language: {
        adult: 'doit être un adulte',
    },
rules: [
        {
            name: 'adult',
            validate(params, value, state, options) {

                if (!value.adult) {
                    // Générer une erreur, state et options doivent être passés
                    return this.createError('person.adult', {}, state, options);
                }

                return value; // Tout est OK
            }
        }
    ]
})
```

#### Express-validator

Un validateur personnalisé peut être implémenté en utilisant la méthode de chaîne `[.custom()](https://express-validator.github.io/docs/validation-chain-api.html#customvalidator)`. Il prend une fonction de validation.

Les validateurs personnalisés peuvent retourner des Promesses pour indiquer une validation asynchrone (qui sera attendue), ou `throw` n'importe quelle valeur/rejeter une promesse pour [utiliser un message d'erreur personnalisé](https://express-validator.github.io/docs/custom-error-messages.html#custom-validator-level).

```js
const {
  param, query, cookies, header 
  body, validationResult } = require('express-validator/check')

app.get('/user/:userId', [   
 param('userId')
  .exists()
  .isMongoId()
  .custom(val => UserSchema.isValidUser(val)), 
], (req, res) => {
    
const errors = validationResult(req);
   
  if (!errors.isEmpty()) {     
    return res.status(422).json({ errors: errors.array() });   
  }
}
```

### Validation conditionnelle

_express-validator_ ne supporte pas encore la validation conditionnelle, mais il y a une PR pour cela que vous pouvez vérifier [https://github.com/express-validator/express-validator/pull/658](https://github.com/express-validator/express-validator/pull/658)

Voyons comment cela fonctionne dans Joi :

#### `any.when(condition, options)`

`**any:**` Génère un objet de schéma qui correspond à n'importe quel type de données.

```js
const schema = Joi.object({
    a: Joi.any().valid('x'),
    b: Joi.any()
}).when(
    Joi.object({ b: Joi.exist() })
    .unknown(), {
    then: Joi.object({
        a: Joi.valid('y')
    }),
    otherwise: Joi.object({
        a: Joi.valid('z')
    })
});
```

#### `alternatives.when(condition, options)`

Ajoute un type de schéma alternatif conditionnel, basé soit sur une autre clé (pas la même que `any.when()`) valeur, soit sur un schéma regardant la valeur actuelle, où :

* `condition` - le nom de la clé ou [référence](https://github.com/hapijs/joi/blob/master/API.md#refkey-options), ou un schéma.
* `options` - un objet avec :
* `is` - le type joi condition requis. Interdit lorsque `condition` est un schéma.
* `then` - le type de schéma alternatif à essayer si la condition est vraie. Requis si `otherwise` est manquant.
* `otherwise` - le type de schéma alternatif à essayer si la condition est fausse. Requis si `then` est manquant.

```js
const schema = Joi
     .alternatives()
     .when(Joi.object({ b: 5 }).unknown(), {
        then: Joi.object({
           a: Joi.string(),
           b: Joi.any()
      }),
      otherwise: Joi.object({
        a: Joi.number(),
        b: Joi.any()
      })
});
```

### Validation imbriquée

Lorsque vous souhaitez valider un tableau d'objets/éléments ou simplement des clés d'objet

Les deux bibliothèques supportent la validation imbriquée

Et pour express-validator ?

#### Wildcards

Les wildcards vous permettent d'itérer sur un tableau d'éléments ou de clés d'objet et de valider chaque élément ou ses propriétés.

Le caractère `*` est également connu sous le nom de wildcard.

```js
const express = require('express'); 
const { check } = require('express-validator/check'); 
const { sanitize } = require('express-validator/filter');  
const app = express(); 

app.use(express.json());  
app.post('/addresses', [   
    check('addresses.*.postalCode').isPostalCode(),
    sanitize('addresses.*.number').toInt() 
], 
(req, res) => {   // Gérer la requête });
```

**Joi**

```js
const schema = Joi.object().keys({
    addresses: Joi.array().items(
        Joi.object().keys({
            postalCode: Joi.string().required(),
        }),
    )
});
```

### Messages d'erreur personnalisés

#### Joi

#### `any.error(err, [options])`

Remplace l'erreur joi par défaut par une erreur personnalisée

```js
let schema = Joi.string().error(new Error('Attendait VRAIMENT une chaîne de caractères'));
```

#### Express-validator

```js
const { check } = require('express-validator/check'); 

app.post('/user', [   
   // ...d'autres validations...   
   check('password')     
   .isLength({ min: 5 }).withMessage('doit faire au moins 5 caractères de long')
   .matches(/\d/).withMessage('doit contenir un nombre') 
], 
(req, res) => {   // Gérer la requête d'une manière ou d'une autre });
```

### Conclusion

J'ai couvert les parties les plus importantes des deux bibliothèques et vous pouvez décider vous-même celle que vous souhaitez utiliser. Veuillez me faire savoir dans les commentaires ci-dessous si j'ai oublié quelque chose d'important dans la comparaison.

J'espère que vous trouverez cela utile lorsque vous déciderez du prochain module de validation d'entrée pour votre application express.js.

J'ai écrit un article approfondi à ce sujet ici : [comment valider les entrées](https://medium.freecodecamp.org/how-to-make-input-validation-simple-and-clean-in-your-express-js-app-ea9b5ff5a8a7). N'hésitez pas à le consulter.

_N'hésitez pas à applaudir si vous avez trouvé cela une lecture utile !_

_Publié à l'origine sur [101node.io](https://101node.io/blog/javascript-validators-comparison-using-joi-vs-express-validator/) le 31 mars 2019._