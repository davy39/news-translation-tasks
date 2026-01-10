---
title: Tout ce que vous devez savoir sur 'module' et 'require' dans Node.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-24T06:56:00.000Z'
originalURL: https://freecodecamp.org/news/require-module-in-node-js-everything-about-module-require-ccccd3ad383
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tZaoIiIYEv0bc0bLO-CYVg.png
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Tout ce que vous devez savoir sur 'module' et 'require' dans Node.js
seo_desc: 'By Srishti Gupta

  Modules


  Node.js treats each JavaScript file as a separate module.


  For instance, if you have a file containing some code and this file is named xyz.js,
  then this file is treated as a module in Node, and you can say that you’ve creat...'
---

Par Srishti Gupta

### Modules

> Node.js traite chaque fichier JavaScript comme un module séparé.

Par exemple, si vous avez un fichier contenant du code et que ce fichier est nommé `xyz.js`, alors ce fichier est traité comme un _module_ dans Node, et vous pouvez dire que vous avez créé un module nommé `xyz`.

![Image](https://cdn-media-1.freecodecamp.org/images/I7AE0rZ1lpEU9AhiKUgm1TjeJl3JUeWY-CsF)
_Fichier JavaScript dans Node.js correspondant à un 'module'_

Prenons un exemple pour mieux comprendre cela.

Vous avez un fichier nommé `circle.js` qui contient la logique pour calculer l'aire et la circonférence d'un cercle d'un rayon donné, comme indiqué ci-dessous :

_circle.js_

Vous pouvez appeler le fichier `circle.js` un module nommé `circle`.

Vous vous demandez peut-être pourquoi il est nécessaire d'avoir plusieurs modules ? Vous auriez pu écrire tout le code dans un seul module. Eh bien, il est très important d'écrire du code modulaire. Par modulaire, je veux dire que votre code doit être indépendant et faiblement couplé. Imaginez qu'il y ait une grande application et que tout votre code soit écrit en un seul endroit, dans un seul fichier. Trop désordonné, n'est-ce pas ?

### Comment le code écrit à l'intérieur d'un module s'exécute-t-il ?

Avant d'exécuter le code écrit à l'intérieur d'un module, Node prend tout le code et l'enferme dans une fonction wrapper. La syntaxe de cette fonction wrapper est :

![Image](https://cdn-media-1.freecodecamp.org/images/jrHUpyWccEG3RTJQg54GR78bbJw6FxN6cWtf)
_Tout le code que vous écrivez dans un module réside dans la fonction wrapper !_

La fonction wrapper pour le module `circle` ressemblera à celle donnée ci-dessous :

Vous pouvez voir qu'il y a une fonction wrapper au niveau racine englobant tout le code écrit à l'intérieur du module `circle`.

> Tout le code écrit à l'intérieur d'un module est privé pour le module, sauf indication explicite contraire (exporté).

C'est l'avantage le plus significatif d'avoir des modules dans Node.js. Même si vous définissez une variable globale dans un module en utilisant les mots-clés `var`, `let` ou `const`, les variables sont limitées localement au module plutôt que d'être globales. Cela se produit parce que chaque module a sa propre fonction wrapper et le code écrit à l'intérieur d'une fonction est local à cette fonction et ne peut pas être accessible en dehors de cette fonction.

![Image](https://cdn-media-1.freecodecamp.org/images/ppIlxCPf-ko2PaAXyhiOqckmoNtcyHKeYCs1)
_Le code écrit à l'intérieur d'un module est privé pour celui-ci !_

Imaginez qu'il y a deux modules — _A_ et _B_. Le code écrit à l'intérieur du _module A_ est enfermé dans la fonction wrapper correspondant au _module A_. La même chose se produit avec le code écrit à l'intérieur du _module B_. Parce que le code appartenant aux deux modules est enfermé dans des fonctions différentes, ces fonctions ne pourront pas accéder au code de l'autre. (Souvenez-vous que chaque fonction en JavaScript a sa propre portée locale ?) C'est la raison pour laquelle le _module A_ ne peut pas accéder au code écrit à l'intérieur du _module B_ et vice-versa.

Les cinq paramètres — `exports`, `require`, `module`, `__filename`, `__dirname` sont disponibles à l'intérieur de chaque module dans Node. Bien que ces paramètres soient globaux pour le code à l'intérieur d'un module, ils sont locaux au module (à cause de la fonction wrapper comme expliqué ci-dessus). Ces paramètres fournissent des informations précieuses liées à un module.

Revenons au module `circle`, que vous avez vu plus tôt. Il y a trois constructions définies dans ce module — une variable constante `PI`, une fonction nommée `calculateArea` et une autre fonction nommée `calculateCircumference`. Un point important à garder à l'esprit est que toutes ces constructions sont privées au module `circle` par défaut. Cela signifie que vous ne pouvez pas utiliser ces constructions dans un autre module sauf si elles sont explicitement spécifiées.

Donc, la question qui se pose maintenant est : comment spécifiez-vous quelque chose dans un module qui peut être utilisé par un autre module ? C'est là que les paramètres `module` et `require` de la fonction wrapper sont utiles. Discutons de ces deux paramètres dans cet article.

### `**module**`

Le paramètre `module` (plutôt un mot-clé dans un module dans Node) fait référence à l'objet représentant le _module actuel_. `exports` est une clé de l'objet `module`, dont la valeur correspondante est un objet. La valeur par défaut de l'objet `module.exports` est `{}` (objet vide). Vous pouvez vérifier cela en enregistrant la valeur du mot-clé `module` à l'intérieur de n'importe quel module. Vérifions quelle est la valeur du paramètre `module` à l'intérieur du module `circle`.

_circle.js_

Remarquez qu'il y a une instruction `console.log(module);` à la fin du code dans le fichier donné ci-dessus. Lorsque vous voyez la sortie, elle enregistrera l'objet `module`, qui a une clé nommée `exports` et la valeur correspondant à cette clé est `{}` (un objet vide).

Maintenant, que fait l'objet `module.exports` ? Eh bien, il est utilisé pour définir des éléments qui peuvent être exportés par un module. Tout ce qui est exporté d'un module peut, à son tour, être mis à la disposition d'autres modules. Exporter quelque chose est assez facile. Vous devez simplement l'ajouter à l'objet `module.exports`. Il existe trois façons d'ajouter quelque chose à l'objet `module.exports` pour l'exporter. Discutons de ces méthodes une par une.

**Méthode 1 :**
**(Définir des constructions puis utiliser plusieurs instructions `module.exports` pour ajouter des propriétés)**

Dans la première méthode, vous définissez d'abord les constructions puis utilisez plusieurs instructions _module.exports_ où chaque instruction est utilisée pour exporter quelque chose d'un module. Regardons cette méthode en action et voyons comment vous pouvez exporter les deux fonctions définies dans le module `circle`.

_circle.js_

Comme je vous l'ai dit plus tôt, `module` est un objet ayant la clé nommée `exports` et cette clé (`module.exports`), à son tour, consiste en un autre objet. Maintenant, si vous remarquez le code donné ci-dessus, tout ce que vous faites est d'ajouter de nouvelles propriétés (paires clé-valeur) à l'objet `module.exports`.

La première propriété a la clé `calculateArea` (définie à la ligne 19) et la valeur écrite à droite de l'opérateur d'affectation est la fonction définie avec le nom `calculateArea` (à la ligne 9).

La deuxième propriété (définie à la ligne 20) a la clé `calculateCircumference` et la valeur est la fonction définie avec le nom `calculateCircumference` (à la ligne 16).

Ainsi, vous avez assigné deux propriétés (paires clé-valeur) à l'objet `module.exports`.

De plus, n'oublions pas que vous avez utilisé la notation par points ici. Vous pouvez alternativement utiliser la notation par crochets pour assigner les propriétés à l'objet `module.exports` et ajouter les fonctions — `calculateArea` et `calculateCircumference` en spécifiant les clés suivant la notation par crochets. Ainsi, vous pouvez écrire les deux lignes suivantes pour ajouter des propriétés à l'objet `module.exports` en utilisant la notation par crochets tout en remplaçant les deux dernières lignes (utilisant la notation par points) dans le code donné ci-dessus :

```
// exporter des éléments en les ajoutant à l'objet module.exports en utilisant la notation par crochets
```

```
module.exports['calculateArea'] = calculateArea;module.exports['calculateCircumference'] = calculateCircumference; 
```

Essayons maintenant de logger la valeur de l'objet `module.exports` après avoir ajouté les propriétés. Remarquez que l'instruction suivante est ajoutée à la fin du code dans le fichier donné ci-dessous :

```
// logger le contenu de l'objet module.exports après avoir ajouté des propriétés
```

```
console.log(module.exports);
```

_circle.js_

Vérifions la sortie de ce code et voyons si tout fonctionne bien. Pour ce faire, sauvegardez votre code et exécutez la commande suivante dans votre _Terminal_ :

```
node circle
```

Sortie :

```
{    calculateArea: [Function: calculateArea],   calculateCircumference: [Function: calculateCircumference] }
```

Les constructions — `calculateArea` et `calculateCircumference`, ajoutées à l'objet `module.exports`, sont loggées. Ainsi, vous avez ajouté avec succès les deux propriétés dans l'objet `module.exports` afin que les fonctions — `calculateArea` et `calculateCircumference` puissent être exportées du module `circle` vers un autre module.

Dans cette méthode, vous avez d'abord défini toutes les constructions puis utilisé plusieurs instructions _module.exports_ où chaque instruction est utilisée pour ajouter une propriété à l'objet `module.exports`.

**Méthode 2 :**
**(Définir des constructions puis utiliser une seule instruction `module.exports` pour ajouter des propriétés)**

Une autre façon est de définir toutes les constructions d'abord (comme vous l'avez fait dans la méthode précédente) mais d'utiliser une seule instruction `module.exports` pour les exporter toutes. Cette méthode est similaire à la syntaxe de la notation littérale d'objet où vous ajoutez toutes les propriétés à un objet en une seule fois.

Ici, vous avez utilisé la notation littérale d'objet et ajouté les deux fonctions — `calculateArea` et `calculateCircumference` (toutes en une fois) à l'objet `module.exports` en écrivant une seule instruction _module.exports_.

Si vous vérifiez la sortie de ce code, vous obtiendrez le même résultat que celui obtenu précédemment en utilisant la méthode 1.

**Méthode 3 :**
**(Ajouter des propriétés à l'objet `module.exports` lors de la définition des constructions)**

Dans cette méthode, vous pouvez ajouter les constructions à l'objet `module.exports` lors de leur définition. Voyons comment cette méthode peut être adoptée dans notre module `circle`.

Dans le code donné ci-dessus, vous pouvez voir que les fonctions du module sont ajoutées à l'objet `module.exports` lorsqu'elles sont définies. Regardons comment cela fonctionne. Vous ajoutez une clé `calculateArea` à l'objet `module.exports` et la valeur correspondant à cette clé est la définition de la fonction.

Notez que la fonction n'a plus de nom et est une fonction anonyme qui est simplement traitée comme une valeur pour une clé d'un objet. Ainsi, cette fonction ne peut pas être référencée dans le module `circle` et vous ne pouvez pas invoquer cette fonction à l'intérieur de ce module en écrivant l'instruction suivante :

```
calculateArea(8);
```

Si vous essayez d'exécuter l'instruction ci-dessus, vous obtiendrez une `ReferenceError` indiquant `calculateArea is not defined`.

Maintenant que vous avez appris comment spécifier ce qui doit être exporté d'un module, comment pensez-vous que l'autre module pourra utiliser les éléments exportés ? Vous devez importer le module dans un autre module afin de pouvoir utiliser les éléments exportés du premier dans le second. C'est là que nous devons discuter d'un autre paramètre nommé `require`.

### **require**

Le mot-clé `require` fait référence à une fonction qui est utilisée pour importer toutes les constructions exportées en utilisant l'objet `module.exports` d'un autre module. Si vous avez un module _x_ dans lequel vous exportez certaines constructions en utilisant l'objet `module.exports` et que vous souhaitez importer ces constructions exportées dans le module _y_, vous devez alors nécessiter le module _x_ dans le module _y_ en utilisant la fonction `require`. La valeur retournée par la fonction `require` dans le module _y_ est égale à l'objet `module.exports` dans le module _x_.

![Image](https://cdn-media-1.freecodecamp.org/images/N6RvqZ73VV1jBVwXFGq4btuHNztUnTRTcVEf)
_La fonction **require** retourne l'objet **module.exports**_

Comprenons cela en utilisant l'exemple que nous avons discuté plus tôt. Vous avez déjà le module `circle` à partir duquel vous exportez les fonctions `calculateArea` et `calculateCircumference`. Maintenant, voyons comment vous pouvez utiliser la fonction `require` pour importer les éléments exportés dans un autre module.

Créons d'abord un nouveau fichier dans lequel vous utiliserez le code exporté du module `circle`. Nommons ce fichier `app.js` et vous pouvez l'appeler le module `app`.

L'objectif est d'importer dans le module `app` tout le code exporté du module `circle`. Alors, comment pouvez-vous inclure votre code écrit dans un module à l'intérieur d'un autre module ?

Considérez la syntaxe de la fonction `require` donnée ci-dessous :

```
const variableToHoldExportedStuff = require('idOrPathOfModule');
```

La fonction `require` prend un argument qui peut être un ID ou un chemin. L'ID fait référence à l'identifiant (ou nom) du module nécessaire. Vous devez fournir l'ID comme argument lorsque vous utilisez les modules tiers ou les modules de base fournis par le Node Package Manager. En revanche, lorsque vous avez des modules personnalisés définis par vous, vous devez fournir le chemin du module comme argument. Vous pouvez en savoir plus sur la fonction require à partir de ce [lien](https://nodejs.org/api/modules.html#modules_require_id).

Parce que vous avez déjà défini un module personnalisé nommé `circle`, vous fournirez le chemin comme argument à la fonction `require`.

_app.js_

Si vous remarquez bien, le point au début du chemin signifie qu'il s'agit d'un chemin relatif et que les modules `app` et `circle` sont stockés au même endroit.

Connectons-nous à la console de la variable `circle`, qui contient le résultat retourné par la fonction `require`. Voyons ce qui est contenu dans cette variable.

_app.js_

Vérifiez la sortie en sauvegardant tout votre code et en exécutant la commande suivante dans votre Terminal (ce dernier n'est pas requis si vous avez installé le package `nodemon`) :

```
node app
```

Sortie :

```
{ calculateArea: [Function: calculateArea],calculateCircumference: [Function: calculateCircumference] }
```

Comme vous pouvez le voir, la fonction `require` retourne un objet, dont les clés sont les noms des variables/fonctions qui ont été exportées du module requis (`circle`). En bref, la fonction `require` retourne l'objet `module.exports`.

Accédons maintenant aux fonctions importées du module `circle`.

_app.js_

Sortie :

```
Area = 200.96, Circumference = 50.24
```

Que pensez-vous qu'il se passera si j'essaie d'accéder à la variable nommée `PI` définie dans le module `circle` à l'intérieur du module `app` ?

_app.js_

Sortie :

```
Area = 200.96, Circumference = 50.24pi = undefined
```

Pouvez-vous comprendre pourquoi `pi` est `undefined` ? Eh bien, c'est parce que la variable `PI` n'est pas exportée du module `circle`. Souvenez-vous du point où je vous ai dit que vous ne pouvez pas accéder au code écrit à l'intérieur d'un module dans un autre module car tout le code écrit à l'intérieur d'un module est privé sauf s'il est exporté ? Ici, vous essayez d'accéder à quelque chose qui n'a pas été exporté du module `circle` et qui est privé pour celui-ci.

Donc, vous vous demandez peut-être pourquoi vous n'avez pas obtenu de `ReferenceError`. C'est parce que vous essayez d'accéder à une clé nommée `PI` à l'intérieur de l'objet `module.exports` retourné par la fonction `require`. Vous savez également que la clé nommée `PI` n'existe pas dans l'objet `module.exports`.

Notez que lorsque vous essayez d'accéder à une clé inexistante dans un objet, vous obtenez le résultat `undefined`. C'est la raison pour laquelle vous obtenez `PI` comme `undefined` au lieu d'obtenir une `ReferenceError`.

Maintenant, exportons la variable `PI` du module `circle` et voyons si la réponse change.

_circle.js_

Remarquez que ici, vous n'utilisez pas le nom de la variable `PI` comme clé de la propriété ajoutée à l'objet `module.exports`. Vous utilisez plutôt un autre nom, qui est `lifeOfPi`.

C'est une chose intéressante à noter. Lorsque vous exportez une construction de code, vous pouvez donner n'importe quel nom à la clé lors de l'ajout d'une propriété à l'objet `module.exports`. Il n'est pas obligatoire d'utiliser le même nom que celui que vous avez utilisé lors de la définition de la construction. C'est parce que vous pouvez utiliser n'importe quel identifiant valide comme clé dans un objet JavaScript. Ainsi, du côté gauche de l'opérateur d'affectation, vous pouvez utiliser n'importe quel identifiant valide, mais du côté droit de l'opérateur d'affectation, vous devez fournir une valeur qui est définie comme une construction dans la portée du module actuel (comme vous avez défini les variables et les fonctions dans le module 'circle').

Un point important à noter est que lors de l'importation de quelque chose d'un autre module dans le module actuel, vous devez utiliser la même clé que celle que vous avez utilisée lors de l'exportation.

_app.js_

Parce que vous avez utilisé la clé `lifeOfPi`, vous devez utiliser la même clé pour accéder à la variable `PI` définie dans le module `circle`, comme c'est fait dans le code donné ci-dessus.

Sortie :

```
Area = 200.96, Circumference = 50.24pi = 3.14
```

Que pensez-vous qu'il se passera si vous utilisez le nom de la variable au lieu d'utiliser la clé qui a été utilisée lors de l'exportation ? En bref, essayons d'accéder à `PI` (nom de la variable) au lieu de `lifeOfPi` (clé utilisée lors de l'exportation de `PI`).

_app.js_

Sortie :

```
Area = 200.96, Circumference = 50.24pi = undefined
```

Cela se produit parce que l'objet `module.exports` ne connaît plus la variable `PI`. Il ne connaît que les clés qui lui ont été ajoutées. Parce que la clé utilisée pour exporter la variable `PI` est `lifeOfPi`, cette dernière peut seulement être utilisée pour accéder à la première.

### TL;DR

* Chaque fichier dans Node.js est appelé un _module_.
* Avant d'exécuter le code écrit dans un module, Node.js prend tout le code écrit à l'intérieur du module et le convertit en une fonction wrapper, qui a la syntaxe suivante :

```
(function(exports, require, module, __filename, __dirname) { // tout le code du module réside ici});
```

* La fonction wrapper garantit que tout le code écrit à l'intérieur d'un module est privé pour celui-ci, sauf indication explicite contraire (exporté). Les paramètres `exports`, `require`, `module`, `__filename` et `__dirname` agissent comme des variables globales pour tout le code dans un module. Puisque chaque module a sa propre fonction wrapper, le code écrit à l'intérieur d'une fonction wrapper devient local à cette fonction wrapper (lire module) et n'est pas accessible à l'intérieur d'une autre fonction wrapper (lire module).
* Le mot-clé `module` fait référence à l'objet représentant le module actuel. L'objet `module` a une clé nommée `exports`. `module.exports` est un autre objet qui est utilisé pour définir ce qui peut être exporté par un module et peut être mis à la disposition d'autres modules. En bref, si un module veut exporter quelque chose, il doit être ajouté à l'objet `module.exports`.
* La valeur par défaut de l'objet `module.exports` est `{}`.
* Il existe trois méthodes pour exporter quelque chose d'un module, ou ajouter quelque chose à l'objet `module.exports` :  
1. Définir toutes les constructions d'abord puis utiliser plusieurs instructions `module.exports` où chaque instruction est utilisée pour exporter une construction.  
2. Définir toutes les constructions d'abord puis utiliser une seule instruction `module.exports` pour exporter toutes les constructions à la fois en suivant la notation littérale d'objet.  
3. Ajouter des constructions à l'objet `module.exports` lors de leur définition.
* Le mot-clé `require` fait référence à une fonction qui est utilisée pour importer toutes les variables et fonctions exportées en utilisant l'objet `module.exports` d'un autre module. En bref, si un fichier veut importer quelque chose, il doit le déclarer en utilisant la syntaxe suivante :

```
require('idOrPathOfModule');
```

* Lors de l'exportation de quelque chose d'un module, vous pouvez utiliser n'importe quel identifiant valide. Il n'est pas obligatoire de donner le nom exact de la variable/fonction comme clé de la propriété ajoutée à l'objet `module.exports`. Assurez-vous simplement d'utiliser la même clé pour accéder à quelque chose que celle que vous avez utilisée lors de son exportation.