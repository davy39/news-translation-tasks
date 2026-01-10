---
title: Modules JavaScript – Comment créer, importer et exporter un module en JS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-02-28T20:42:29.000Z'
originalURL: https://freecodecamp.org/news/javascript-modules
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/Add-a-subheading--1-.png
tags:
- name: JavaScript
  slug: javascript
- name: modules
  slug: modules
seo_title: Modules JavaScript – Comment créer, importer et exporter un module en JS
seo_desc: "By Dapo Adedire\nJavaScript, like most programming languages, was initially\
  \ used for small tasks. But as its popularity grew, so did the amount of code that\
  \ needed to be written. \nHaving a large amount of code in a single file can be\
  \ problematic, so i..."
---

Par Dapo Adedire

JavaScript, comme la plupart des langages de programmation, était initialement utilisé pour des petites tâches. Mais à mesure que sa popularité a grandi, la quantité de code à écrire a également augmenté. 

Avoir une grande quantité de code dans un seul fichier peut être problématique, il est donc utile de diviser le code en plusieurs parties. C'est là que les modules deviennent pratiques.

## Qu'est-ce qu'un Module ?

Les modules JavaScript sont un moyen d'organiser et de structurer le code. Ils permettent aux développeurs de diviser leur code en plus petites parties réutilisables. Vous pouvez les considérer comme de petits morceaux de code que vous pouvez importer et exporter entre différentes parties d'une application.

Tout au long de cet article, nous allons voir comment utiliser les modules dans votre programme et les meilleures façons de le faire.

Mais d'abord, parlons de quelques autres raisons d'utiliser les modules.

## Les Avantages de l'Utilisation des Modules

Votre code fonctionnera toujours si vous le mettez tout dans le même fichier. Mais vous pourriez vous causer quelques problèmes. Parlons de quelques avantages de l'utilisation des modules dans votre programme.

### Code Plus Organisé

L'utilisation de modules dans votre application rend tout bien trié et organisé. Cela facilite également la compréhension de votre travail pour quiconque souhaite parcourir votre code. 

Vous ne seriez probablement pas ravi de trouver une variable appelée "username" à la ligne 431 ou de devoir commencer à renommer une variable ou un nom de fonction partout où elle est utilisée dans une application.

### Réutilisabilité du Code

En décomposant votre code en composants modulaires plus petits, vous pouvez facilement réutiliser ces composants dans d'autres parties de votre application ou dans des applications entièrement nouvelles. 

Cela peut vous faire gagner beaucoup de temps et d'efforts, car vous n'avez pas à réécrire le même code encore et encore. 

De plus, si vous apportez des modifications à un module, ces modifications seront reflétées partout où ce module est utilisé, ce qui facilite la maintenance et la mise à jour de votre base de code.

### Pas de Conflits de Noms

L'utilisation de modules JavaScript vous aide à éviter les conflits de noms. Lorsque vous travaillez sur un grand projet, il est courant que les développeurs écrivent plusieurs fonctions et variables avec le même nom. Cela peut entraîner des conflits de noms où deux morceaux de code ou plus ont le même nom, provoquant des comportements inattendus et des erreurs. Avec les modules, vous n'avez pas ce problème.

## Comment Utiliser les Modules en JavaScript

### Comment Définir un Module

Voici la manière de base de définir un module. Imaginez deux fichiers nommés `main.js` et `generate.js`.

Voici main.js :

```javascript
let name = "Muhammad Ali"

```

Et voici generate.js :

```javascript
function generateUserCertificate(userName, date): 
    # générer le certificat de l'utilisateur. 
const myName = name
generateUserCertificate(myName, "2023-09-04")

```

Pour utiliser la variable "name" à l'intérieur du fichier generate.js, vous devez l'exporter depuis le fichier main.js et l'importer dans le fichier generate.js.

Il existe de nombreuses techniques que vous pouvez utiliser pour importer et exporter des fichiers.

Nous allons les passer en revue une par une.

## Types d'Exportations de Fichiers en JavaScript

### Exportations par Défaut

Voici comment effectuer une exportation par défaut dans un fichier JavaScript :

```javascript
function getAllUser():

export default getAllUser

```

Notez que vous ne pouvez utiliser qu'une seule exportation par défaut dans un fichier JavaScript. Vous pouvez également exporter avant la déclaration, comme ceci :

```javascript
export default function getAllUser():

```

C'est plus facile à lire, n'est-ce pas ?

### Exportations Nominales

Les exportations nominales vous permettent de partager plusieurs modules depuis un fichier, contrairement aux exportations par défaut qui ne peuvent en avoir qu'une seule dans un fichier. 

Vous n'aurez pas besoin d'utiliser la syntaxe "default" lorsque vous utilisez des exportations nominales. Les exportations nominales doivent également être enfermées dans des accolades si vous exportez plus d'un module.

Voici un exemple :

```javascript
const name = "Muhammad Ali"

export { name };

```

Vous pouvez également exporter avant la déclaration. Voici comment faire :

```javascript
export function sayHi(user) {
  alert(`Bonjour, ${user}!`);
}

export function sayHello(user) {
  alert(`Bonjour, ${user}!`);
}

```

Vous pouvez également exporter plusieurs variables, fonctions ou classes en utilisant des exportations nominales dans une seule instruction. Voici un exemple :

```javascript
const name = "Muhammad Alli"

function sayHello(user) {
  alert(`Bonjour, ${user}!`);
}

export { name, sayHello };

```

Note : Il est possible d'avoir à la fois une exportation par défaut et des exportations nominales dans un module.

```javascript
const age = 404;

const name = "Muhammad Alli"

export default function sayHello(user) {
  alert(`Bonjour, ${user}!`);
}

export { age, name };

```

### Comment Renommer les Exportations

Il est également possible de renommer vos modules avant de les exporter. Voici comment faire :

```javascript
export function sayHello(user) {
  alert(`Bonjour, ${user}!`);
}

export { sayHello as greet };

```

## Comment Importer des Modules

### Comment Importer une Exportation par Défaut Unique

Voici comment importer une exportation par défaut :

```javascript
import getAllUser from "getuser.js";

```

C'est tout – vous pouvez ensuite utiliser la fonction `getAllUser` n'importe où dans ce fichier.

### Comment Importer une Exportation Nominale Unique

Voici comment importer une exportation nominale unique.

```javascript
import { name } from "username.js"

```

### Comment Importer Plusieurs Exportations Nominales

Voici comment exporter plusieurs exportations nominales.

```javascript
 import { name, sayHello } from 'user.js'

```

### Comment Renommer les Importations

Vous pouvez également renommer les exportations avant de les utiliser dans un fichier JavaScript. Voici comment faire :

```javascript
import { userName as name, greet as sayHello } from 'user.js'

```

Cela importe essentiellement le module name et sayHello et les renomme, donc vous ne pouvez faire référence qu'à "userName" et "greet" dans ce module actuel.

### Comment Importer un Module Entier

Que faire s'il y a beaucoup de modules à importer et qu'il est fastidieux de créer une seule ligne d'exportations nominales pour chacun ? Vous pouvez alors les exporter de cette manière :

```javascript
import * as User from 'user.js'

```

Voici comment vous pouvez l'utiliser dans le module exporté :

```javascript
import * as User from 'user.js'

User.name
User.sayHi

```

## Conclusion

Les modules sont une fonctionnalité puissante en JavaScript qui permet aux développeurs d'organiser et de structurer leur code pour une meilleure lisibilité et réutilisabilité. Ils aident également à éviter les conflits de noms. 

En décomposant de grandes bases de code en modules plus petits et gérables, les développeurs peuvent écrire un code plus efficace et plus maintenable. 

Cet article a couvert les bases de la définition, de l'exportation et de l'importation de modules en JavaScript, y compris les exportations par défaut, les exportations nominales, le renommage des exportations et l'importation de modules entiers. 

En maîtrisant l'utilisation des modules, vous pouvez faire passer vos compétences en programmation JavaScript au niveau supérieur et écrire un code plus efficace et évolutif.

Vous pouvez partager vos pensées avec moi sur [Twitter](https://twitter.com/dapo_adedire) ici.

Bon codage ! ^-^