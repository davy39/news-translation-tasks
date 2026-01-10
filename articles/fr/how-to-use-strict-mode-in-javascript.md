---
title: Qu'est-ce que le mode strict en JavaScript ? Explications avec des exemples
subtitle: ''
author: Benjamin Semah
co_authors: []
series: null
date: '2024-02-06T11:05:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-strict-mode-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-02-at-2.56.05-PM.png
tags:
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Qu'est-ce que le mode strict en JavaScript ? Explications avec des exemples
seo_desc: 'If you are a JavaScript developer, you may come across the string "use
  strict" at the top of your JavaScript code. This means that JavaScript''s strict
  mode is in use. But what does this mean, and why does it matter?

  In this article, you''ll learn what...'
---

Si vous êtes un développeur JavaScript, vous avez peut-être rencontré la chaîne "use strict" en haut de votre code JavaScript. Cela signifie que le mode strict de JavaScript est utilisé. Mais que signifie cela, et pourquoi est-ce important ?

Dans cet article, vous apprendrez ce que signifie écrire du code JavaScript en mode strict et comment vous pouvez l'activer. L'article couvre également certains avantages de l'utilisation du mode strict et quelques exemples qui montrent comment il diffère du JavaScript régulier.

## Table des matières

* [Qu'est-ce que le mode strict en JavaScript ?](#quest-ce-que-le-mode-strict-en-javascript)
    
* [Comment utiliser le mode strict en JavaScript](#comment-utiliser-le-mode-strict-en-javascript)
    
* [Différence entre le mode strict et le JavaScript régulier](#difference-entre-le-mode-strict-et-le-javascript-regulier)
    
* [Fonctionnalités JavaScript qui utilisent le mode strict par défaut](#fonctionnalites-javascript-qui-utilisent-le-mode-strict-par-defaut)
    
* [Conclusion](#conclusion)
    

## Qu'est-ce que le mode strict en JavaScript ?

Le mode strict est une fonctionnalité en JavaScript qui a été introduite dans ECMAScript 5. Il vous permet d'écrire du code de manière à suivre des règles plus strictes.

Lorsque le mode strict est activé, le moteur JavaScript applique des contraintes supplémentaires. Cela signifie que vous pourrez peut-être attraper certaines erreurs courantes qui seraient autrement passées inaperçues. Cela vous aide également à écrire un code plus propre et plus sécurisé.

## Comment utiliser le mode strict en JavaScript

Vous pouvez utiliser le mode strict JavaScript de deux manières. Vous pouvez soit activer le mode strict pour un fichier JavaScript entier, soit l'activer dans la portée d'une fonction.

Pour activer le mode strict pour l'ensemble du fichier JavaScript, vous ajoutez simplement la chaîne `"use strict"` en haut de votre code.

```javascript
"use strict"

// Votre code va ici...
```

Pour les fonctions, vous pouvez activer le mode strict en plaçant la chaîne `"use strict"` en haut du corps de votre fonction.

```javascript
function myFunction() {
  "use strict"
  // Le corps de la fonction va ici...
  
}
```

Vous devez placer la chaîne `"use strict"` en haut du fichier ou du corps de la fonction. Sinon, cela ne fonctionnera pas.

Mais vous êtes autorisé à ajouter des commentaires au-dessus de la chaîne `"use strict"`. À part les commentaires, tout le reste doit être en dessous de `"use strict"` pour que cela fonctionne.

## Différence entre le mode strict et le JavaScript régulier

Maintenant, voyons quelques-unes des règles que le mode strict applique et qui ne sont pas appliquées lors de l'écriture de code en JavaScript régulier.

### Utilisation d'une variable non déclarée

Lors de l'écriture de code JavaScript en mode strict, vous devez déclarer toutes les variables et objets avant de les utiliser. Cela est utile car cela aide à prévenir la création de variables globales par accident, ce qui peut entraîner des bugs.

Voici un exemple

```javascript
// JavaScript régulier

function regularFunc() {
  username = "Marie"
  console.log(username)
}

regularFunc()
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-01-at-8.20.00-AM.png align="left")

*Le JS régulier ne génère aucune erreur pour la variable username.*

```javascript
// Mode strict

function strictFunc() {
  "use strict"
  username = "Marie"
  console.log(username)
}

strictFunc()
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-02-at-7.07.08-AM.png align="left")

*Le mode strict génère une erreur pour les variables non déclarées.*

Dans la fonction `regularFunc`, le navigateur enregistre le `username` dans la console sans aucune erreur.

Mais avec la fonction `strictFunc` qui utilise le mode strict, elle génère une erreur de référence.

C'est parce que la variable `username` n'a pas été déclarée. Et le mode strict n'autorise pas l'utilisation de variables avant qu'elles ne soient déclarées.

### Duplication d'un nom de paramètre

En mode non strict, dupliquer un nom de paramètre dans une fonction est autorisé. Seule la dernière instance des doublons est autorisée tandis que les autres sont ignorées.

Mais les fonctions en mode strict n'autorisent pas cela. Elles génèrent une erreur de syntaxe en cas de doublons.

Voici un exemple :

```javascript
function addNums (num, num) {
  console.log(num + num)
}

addNums(2, 3) // 6
```

Dans l'exemple ci-dessus, le premier paramètre `num` est ignoré. Seule la seconde est utilisée. C'est pourquoi la fonction retourne 6 car 3 + 3 est égal à 6.

Mais lorsque vous définissez les mêmes paramètres dans une fonction en utilisant le mode strict, vous ne pouvez pas l'exécuter car elle générera une erreur de syntaxe. Le mode strict exige que chaque paramètre ait un nom unique.

C'est-à-dire :

```javascript
function addNums (num, num) {
  "use strict"
  console.log(num + num)
}

addNums(2, 3)
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-02-at-9.15.07-AM.png align="left")

*Le navigateur génère une erreur pour le nom de paramètre dupliqué.*

### Utilisation de mots-clés réservés pour l'avenir

En JavaScript, il y a certains mots-clés réservés pour une utilisation potentielle future. Et l'utilisation de ces mots-clés comme identifiants (tels que des variables ou des noms de fonctions) peut probablement causer des problèmes à l'avenir.

Par exemple, `package` est l'un de ces mots-clés. Lorsque vous n'utilisez pas le mode strict, vous pouvez l'utiliser pour nommer des variables et des fonctions.

```javascript
const package = "Ceci est un package"
console.log(package)
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-02-at-9.17.36-AM.png align="left")

*Résultat de la journalisation pour l'utilisation d'un mot-clé réservé en JavaScript régulier.*

Le mode strict n'autorise pas l'utilisation de ces mots-clés réservés. Cela garantit la compatibilité avec les futures versions de JavaScript.

```javascript
"use strict"
const package = "Ceci est un package"
console.log(package)
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-02-at-9.22.21-AM.png align="left")

*L'utilisation d'un mot-clé réservé en mode strict entraîne une erreur de syntaxe.*

D'autres mots-clés réservés pour l'avenir incluent :

* `implements`
    
* `interface`
    
* `private`
    
* `protected`
    
* `public`
    
* `static`
    
* `yield`
    
* `arguments`
    

### Utilisation de fonctionnalités obsolètes

Le mode strict restreint l'utilisation des fonctionnalités obsolètes de JavaScript comme `arguments.caller`, `arguments.callee`, et ainsi de suite.

Celles-ci sont interdites en raison de préoccupations de sécurité et de performance. Mais le mode non strict permet de les utiliser.

Voyons un exemple d'utilisation de `arguments.caller` en mode strict et non strict.

```javascript
// mode non strict

function outerFunction() {
  innerFunction();
}

function innerFunction() {
  console.log(innerFunction.caller); // Exemple de .caller
}

outerFunction();
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-02-at-10.18.11-AM.png align="left")

`arguments.caller` fonctionne en mode non strict sans aucune erreur.

L'utilisation de `.caller` sur `innerFunction` journalise `outerFunction` qui appelle la fonction interne dans la console. Cela fonctionne bien en mode non strict.

Mais l'utiliser en mode strict provoquera une erreur comme dans l'exemple ci-dessous.

```javascript
"use strict"

function outerFunction() {
  innerFunction();
}

function innerFunction() {
  console.log(innerFunction.caller); // Exemple de .caller
}

outerFunction();
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-02-at-10.23.14-AM.png align="left")

*Le mode strict génère une "Uncaught TypeError" pour l'utilisation de fonctionnalités obsolètes.*

### Assignation à une propriété en lecture seule

En mode non strict, lorsque vous essayez d'assigner une nouvelle valeur à une propriété en lecture seule, l'assignation ne modifiera pas la valeur de la propriété. Mais elle ne générera aucune erreur. Au lieu de cela, l'assignation échoue silencieusement, et la propriété conserve sa valeur d'origine.

```javascript
const obj = {}

Object.defineProperty(obj, 'key', { value: 10, writable: false })
obj.key = 20

console.log(obj.key)
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-02-at-11.23.16-AM.png align="left")

*Résultat de la journalisation pour* `object.key`

Cet exemple définit un nouvel objet vide `obj`. Et en utilisant `Object.defineProperty`, une nouvelle propriété `key` est ajoutée à `obj`. Cette propriété `key` est définie comme une propriété en lecture seule.

Comme vous pouvez le voir à partir du résultat de la journalisation, il n'y a pas d'erreur lorsque vous essayez de mettre à jour la valeur de `key`. Et la propriété `key` maintient la valeur d'origine de `10`.

En mode strict, cependant, tenter de mettre à jour la valeur de la propriété entraînera une `TypeError`. Cette application plus stricte aide à détecter les erreurs potentielles tôt.

```javascript
"use strict"
const obj = {}

Object.defineProperty(obj, 'key', { value: 10, writable: false })
obj.key = 20

console.log(obj.key)
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-02-at-11.43.54-AM.png align="left")

*Le mode strict génère une erreur lors de l'assignation d'une nouvelle valeur à une propriété en lecture seule.*

## Fonctionnalités JavaScript qui utilisent le mode strict par défaut

Certaines fonctionnalités JavaScript ne nécessitent pas que vous invoquiez explicitement `"use strict"`. Par défaut, le mode strict est appliqué pour prévenir les erreurs courantes et assurer la compatibilité avec les futures versions de JavaScript.

Des exemples de tels contextes incluent les suivants :

* Les classes ES6
    
* Les modules ES6
    
* Les fonctions fléchées
    
* Les littéraux de gabarits étiquetés
    

## Conclusion

JavaScript a commencé comme un langage pour ajouter une simple interactivité aux pages web. Mais il a depuis évolué pour devenir l'un des langages de programmation les plus utilisés pour créer des applications simples et complexes.

Alors que le langage évolue, certains de ses anciens défauts subsistent. La fonctionnalité de mode strict aide les développeurs JavaScript à gérer certains des problèmes que ces défauts causent.

Dans cet article, vous avez appris le mode strict, comment l'utiliser et comment il diffère de l'écriture de code JavaScript en mode non strict. Vous avez également appris divers contextes en JavaScript où les règles du mode strict sont appliquées par défaut.

Merci d'avoir lu. Et bon codage ! Pour des tutoriels plus approfondis, n'hésitez pas à [vous abonner à ma chaîne YouTube](https://www.youtube.com/@DevAfterHours).