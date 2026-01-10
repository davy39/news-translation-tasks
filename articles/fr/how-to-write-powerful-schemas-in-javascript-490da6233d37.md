---
title: Comment écrire des schémas puissants en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-21T04:53:38.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-powerful-schemas-in-javascript-490da6233d37
coverImage: https://cdn-media-1.freecodecamp.org/images/1*u_gVBtCyIcrWbOBv3xDCWg.png
tags:
- name: JavaScript
  slug: javascript
- name: mongoose
  slug: mongoose
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment écrire des schémas puissants en JavaScript
seo_desc: 'By Diego Haz

  Introducing schm, a functional and highly composable library for creating schemas
  in JavaScript and Node.js


  _Background photo by [Willi Heidelbach](https://www.flickr.com/photos/wilhei/" rel="noopener"
  target="blank" title="Vá para a ga...'
---

Par Diego Haz

#### Présentation de [schm](https://github.com/diegohaz/schm), une bibliothèque fonctionnelle et hautement composable pour créer des schémas en JavaScript et Node.js

![Image](https://cdn-media-1.freecodecamp.org/images/1*u_gVBtCyIcrWbOBv3xDCWg.png)
_Photo de fond par [Willi Heidelbach](https://www.flickr.com/photos/wilhei/" rel="noopener" target="_blank" title="Vá para a galeria de Willi Heidelbach)_

Je travaille avec HTML, CSS et JavaScript depuis 2002. La première fois que j'ai eu besoin d'un type de schéma en JavaScript, c'était il y a seulement quelques années.

Après avoir utilisé de nombreuses bibliothèques différentes et même avoir écrit [une](https://github.com/diegohaz/querymen) et [une autre](https://github.com/diegohaz/bodymen), j'ai décidé de créer [schm](https://github.com/diegohaz/schm). C'est le résultat de toute mon expérience avec les schémas en JavaScript.

### Qu'est-ce que [schm](https://github.com/diegohaz/schm) ?

`schm` est un groupe de packages npm pour aider les développeurs à gérer les schémas en JavaScript et Node.js.

Il est fortement inspiré par [Mongoose Schemas](http://mongoosejs.com/docs/guide.html). En fait, ils sont si similaires que vous pouvez utiliser les paramètres `schm` dans les schémas Mongoose et vice-versa. Ce n'est pas spécifique à MongoDB, cependant. Vous pouvez l'utiliser pour tout en JavaScript.

### Quels types de problèmes [schm](https://github.com/diegohaz/schm) résout-il ?

#### ? Analyse et validation des valeurs de formulaire

Sur le client, vous pouvez utiliser des schémas pour définir des modèles pour les formulaires HTML. Cela facilite la transformation et la validation des valeurs. De plus, si vous utilisez Node.js sur le serveur, vous pouvez utiliser le même schéma. Le résultat est un comportement cohérent entre les validations client et serveur.

#### ? Analyse et validation de la chaîne de requête

Considérez la chaîne de requête suivante : `/?term=John&page=2&limit=10`. En combinant des packages tels que [schm-koa](https://github.com/diegohaz/schm/tree/master/packages/schm-koa), [schm-express](https://github.com/diegohaz/schm/tree/master/packages/schm-express) et/ou [schm-mongo](https://github.com/diegohaz/schm/tree/master/packages/schm-mongo), vous pourrez analyser et valider les chaînes de requête avec des termes de recherche et une pagination avec facilité.

#### ⚪ Communication entre le client et le serveur

Si vous avez une application qui consomme des ressources à partir d'une API REST, par exemple, vous pouvez utiliser des schémas pour définir, sur le client, la structure d'objet que votre client s'attend à recevoir du serveur. Si quelque chose change sur le serveur (des propriétés ont été renommées, par exemple), vous pouvez simplement mettre à jour votre schéma pour que votre application entière continue de fonctionner.

### Création d'un schéma

Un schéma simple est juste une carte de clés et de types :

C'est la même chose que d'utiliser une propriété `type` :

Un schéma peut également être une carte entre des clés et des valeurs par défaut. Les types seront automatiquement déduits :

Cela équivaut à faire ce qui suit :

Pour en savoir plus sur la façon d'écrire des schémas, consultez [Mongoose Schemas](http://mongoosejs.com/docs/guide.html).

### Analyse des valeurs

Après avoir défini le schéma, vous pouvez l'utiliser pour analyser les valeurs. Ce processus convertira les valeurs aux types appropriés, ainsi qu'en appliquant d'autres analyseurs définis dans le schéma. Voici les analyseurs disponibles : `type`, `default`, `set`, `get`, `trim`, `uppercase`, `lowercase`.

La sortie sera quelque chose comme ceci :

```
{  name: "HAZ",  birthdate: Tue Apr 10 1990 00:00:00 GMT,}
```

### Validation des valeurs

Tout comme dans [Mongoose Schemas](http://mongoosejs.com/docs/guide.html), vous pouvez définir des règles de validation dans vos schémas. Voici les validateurs disponibles : `validate`, `required`, `match`, `enum`, `max`, `min`, `maxlength`, `minlength`.

Vous pouvez également créer des analyseurs et des validateurs personnalisés en étendant le schéma. Nous en parlerons plus tard dans cet article.

L'erreur de validation sera, par défaut, un tableau d'objets décrivant les erreurs.

```
[  {    message: "age must be greater than or equal 18",    min: 18,    param: "age",    validator: "min",    value: 17,  }]
```

Si la validation réussit, elle retournera les valeurs analysées, tout comme `parse()`.

### Composition de plusieurs schémas

Supposons que vous avez des schémas séparés décrivant un `body`, une `identity` et d'autres choses, et que vous souhaitez les composer pour construire un schéma `human`. C'est aussi facile que cela en a l'air :

Une autre façon de composer des schémas est par imbrication. Un schéma peut être utilisé comme un `type` dans un autre schéma :

### Extension des schémas

C'est là que `schm` brille vraiment. Vous pouvez ajouter des analyseurs et des validateurs personnalisés ou même remplacer le comportement par défaut des méthodes `parse` et `validate` en créant des groupes de schémas.

Un **groupe de schémas** est une fonction qui reçoit le schéma précédent comme seul argument. En plus des `params`, `parsers` et `validators` précédents, l'objet schéma a une méthode `merge`, qui est utile pour les fonctions de groupe de schémas pour fusionner de nouvelles fonctionnalités dans les schémas précédents.

La sortie de l'extrait ci-dessus sera quelque chose comme ceci :

```
{  name: "Haz!!!",  age: 27,}
```

Si vous voulez aller plus loin et en savoir plus sur la création d'analyseurs personnalisés, consultez comment les analyseurs sont écrits à l'intérieur de la bibliothèque principale [ici](https://github.com/diegohaz/schm/blob/master/packages/schm/src/parsers.js).

En étendant les schémas, nous pouvons créer de nombreuses sortes de choses. C'est ainsi que la plupart des bibliothèques satellites `schm`, telles que [schm-translate](https://github.com/diegohaz/schm/tree/master/packages/schm-translate), [schm-computed](https://github.com/diegohaz/schm/tree/master/packages/schm-computed) et [schm-mongo](https://github.com/diegohaz/schm/tree/master/packages/schm-mongo), sont écrites.

Nous allons parler de l'une d'entre elles maintenant.

### Renommage des clés de valeurs

[schm-translate](https://github.com/diegohaz/schm/tree/master/packages/schm-translate) est l'une des bibliothèques satellites les plus simples, mais puissantes, de `schm`. C'est un peu plus que [10 lignes de code](https://github.com/diegohaz/schm/blob/master/packages/schm-translate/src/index.js) compressées en une fonction qui vous permet de traduire les clés de valeurs vers les clés de votre schéma.

Supposons que vous travaillez sur une application web qui consomme des ressources à partir d'une API REST. Soudain, les développeurs changent des choses sur l'API, ce qui fait que le corps de la réponse retourne un modèle légèrement différent de celui auquel le client s'attendait. Au lieu d'une propriété `email`, il retourne maintenant un tableau d'`emails`.

Cela fera probablement planter votre application. Si vous n'avez pas de schéma ou d'autre moyen centralisé pour gérer cet objet, vous devrez mettre à jour chaque partie de l'application pour vous conformer aux changements du serveur.

Avec `schm` et `schm-translate`, cela peut être résolu en changeant quelques lignes de code en un seul endroit :

La sortie sera exactement celle à laquelle votre application s'attendait avant le changement :

```
{  name: "Haz",  email: "hazdiego@gmail.com",}
```

[Cliquez ici pour voir la liste de tous les packages](https://github.com/diegohaz/schm#packages)

### En quoi cela est-il différent des autres bibliothèques de schémas ?

Une question courante est la différence entre `schm` et d'autres bibliothèques, telles que [Joi](https://github.com/hapijs/joi) et [ajv](https://github.com/epoberezkin/ajv) (qui suit la spécification [JSON Schema](http://json-schema.org/)).

Comparé à `ajv`, `schm` ne suit aucune spécification particulière. Au lieu de cela, il essaie d'imiter l'API Mongoose Schema. De plus, même si `ajv` a certaines fonctionnalités d'analyse, elles sont limitées aux [valeurs par défaut](https://github.com/epoberezkin/ajv#assigning-defaults) et à la [coercition de type](https://github.com/epoberezkin/ajv#coercing-data-types).

Dans `schm`, la capacité à analyser les valeurs en fonction du schéma est ce qui permet de transformer une chaîne de requête en une requête MongoDB, par exemple.

Cela dit, `Joi` et `ajv` peuvent être combinés avec `schm`. Vous pouvez facilement l'étendre pour utiliser une méthode de validation différente :

### Merci d'avoir lu ceci !

Si vous aimez cela et que vous le trouvez utile, voici quelques choses que vous pouvez faire pour montrer votre soutien :

* Cliquez sur le bouton d'applaudissements ? plusieurs fois sur cet article (jusqu'à 50)
* Donnez une étoile ⭐ sur GitHub : [https://github.com/diegohaz/schm](https://github.com/diegohaz/schm)
* Suivez-moi sur GitHub : [https://github.com/diegohaz](https://github.com/diegohaz)
* Suivez-moi sur Twitter : [https://twitter.com/diegohaz](https://twitter.com/diegohaz)