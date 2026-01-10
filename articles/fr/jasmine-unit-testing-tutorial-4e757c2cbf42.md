---
title: Une introduction aux tests unitaires avec Jasmine
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-13T13:45:10.000Z'
originalURL: https://freecodecamp.org/news/jasmine-unit-testing-tutorial-4e757c2cbf42
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca766740569d1a4ca76f2.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Testing
  slug: testing
seo_title: Une introduction aux tests unitaires avec Jasmine
seo_desc: 'By Ahmed Bouchefra

  Jasmine is the most popular JS library for unit testing web apps. In this tutorial,
  designed for beginners, we’ll present you with a quick and complete guide to testing
  with Jasmine.

  You’ll get introduced to Jasmine, a popular beha...'
---

Par Ahmed Bouchefra

Jasmine est la bibliothèque JS la plus populaire pour les tests unitaires des applications web. Dans ce tutoriel, conçu pour les débutants, nous vous présentons un guide rapide et complet pour tester avec Jasmine.

Vous serez introduit à Jasmine, un framework populaire de développement piloté par le comportement (BDD) pour JavaScript. Nous verrons également un exemple pratique simple sur la façon d'écrire des tests unitaires avec Jasmine, ce qui peut vous aider à vérifier facilement les bugs dans votre code.

En résumé, nous verrons comment écrire des suites de tests, des spécifications et des attentes, et comment appliquer les matchers intégrés de Jasmine ou construire vos propres matchers personnalisés.

Nous verrons également comment vous pouvez regrouper des suites dans le but d'organiser vos tests pour des bases de code plus complexes.

### Présentation de Jasmine

[Jasmine](http://jasmine.github.io/) est un framework très populaire de développement piloté par le comportement (BDD) pour JavaScript, utilisé pour les tests unitaires des applications JavaScript. Il fournit des utilitaires qui peuvent être utilisés pour exécuter des tests automatisés pour le code synchrone et asynchrone.

Jasmine possède de nombreuses fonctionnalités telles que :

* Il est rapide et a peu de surcharge et aucune dépendance externe.
* C'est une bibliothèque tout-en-un et offre tout ce dont vous avez besoin pour tester votre code.
* Il est disponible à la fois pour Node et le navigateur.
* Il peut être utilisé avec d'autres langages comme Python et Ruby.
* Il ne nécessite pas le DOM.
* Il fournit une syntaxe claire et facile à comprendre ainsi qu'une API riche et simple.
* Nous pouvons utiliser un langage naturel pour décrire les tests et les résultats attendus.

Jasmine est un outil open source disponible sous la licence permissive MIT. À l'heure de la rédaction de cet article, la dernière version majeure est _Jasmine 3.0_, qui offre de nouvelles fonctionnalités et quelques changements importants. La version _2.99_ de Jasmine fournira différents avertissements de dépréciation pour les suites qui ont un comportement différent dans la version _3.0_, ce qui facilitera la migration des développeurs vers la nouvelle version.

Vous pouvez lire les nouvelles fonctionnalités et les changements importants à partir de ce [document](https://github.com/jasmine/jasmine/blob/v3.0.0/release_notes/3.0.md).

### Utilisation de Jasmine

Vous pouvez utiliser Jasmine de nombreuses manières différentes :

* à l'ancienne en incluant à la fois le cœur de Jasmine et vos fichiers de test à l'aide d'une balise `<script>`,
* en tant qu'outil CLI utilisant Node.js,
* en tant que bibliothèque dans Node.js,
* en tant que partie d'un système de build comme Gulp.js ou Grunt.js via [grunt-contrib-jasmine](https://github.com/gruntjs/grunt-contrib-jasmine) et [gulp-jasmine-browser](https://github.com/jasmine/gulp-jasmine-browser)

Vous pouvez également utiliser Jasmine pour tester votre code Python avec [jasmine-py](https://github.com/jasmine/jasmine-py), qui peut être installé à partir de PyPI en utilisant la commande `pip install jasmine`. Ce package contient à la fois un serveur web qui sert et exécute une suite Jasmine pour votre projet et un script CLI pour exécuter des tests et des intégrations continues.

Jasmine est également disponible pour les projets Ruby via [jasmine-gem](https://github.com/jasmine/jasmine-gem), qui peut être installé en ajoutant `gem 'jasmine'` à votre Gemfile et en exécutant `bundle install`. Il inclut un serveur pour servir et exécuter des tests, un script CLI et également des générateurs pour les projets Ruby on Rails.

Concentrons-nous maintenant sur la façon d'utiliser Jasmine avec JavaScript :

### Utilisation de Jasmine en mode autonome

Commencez par télécharger la dernière version de Jasmine à partir de la page [releases](https://github.com/jasmine/jasmine/releases).

![Image](https://cdn-media-1.freecodecamp.org/images/c1Ieo1kBD-F8mAKy1ZKYbc2IayEoMWHDL1eH)

Ensuite, extrayez simplement le fichier zip, de préférence à l'intérieur d'un dossier dans le projet que vous souhaitez tester.

Le dossier contiendra un ensemble de fichiers et dossiers par défaut :

`/src` : contient les fichiers sources que vous souhaitez tester. Ce dossier peut être supprimé si vous avez déjà configuré le dossier de votre projet ou peut également être utilisé lorsque cela est approprié pour héberger votre code source.

`/lib` : contient les fichiers principaux de Jasmine.

`/spec` : contient les tests que vous allez écrire.

`SpecRunner.html` : ce fichier est utilisé comme exécutant de tests. Vous exécutez vos spécifications en lançant simplement ce fichier.

Voici le contenu d'un fichier `SpecRunner.html` par défaut :

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Jasmine Spec Runner v3.2.1</title>

  <link rel="shortcut icon" type="image/png" href="lib/jasmine-3.2.1/jasmine_favicon.png">
  <link rel="stylesheet" href="lib/jasmine-3.2.1/jasmine.css">

  <script src="lib/jasmine-3.2.1/jasmine.js"></script>
  <script src="lib/jasmine-3.2.1/jasmine-html.js"></script>
  <script src="lib/jasmine-3.2.1/boot.js"></script>

  <!-- inclure les fichiers sources ici... -->
  <script src="src/Player.js"></script>
  <script src="src/Song.js"></script>

  <!-- inclure les fichiers de spécification ici... -->
  <script src="spec/SpecHelper.js"></script>
  <script src="spec/PlayerSpec.js"></script>

</head>
<body>
</body>
</html>
```

N'oubliez pas que vous devez changer les fichiers inclus des dossiers `/src` et `/spec` pour contenir vos fichiers sources et de test réels.

### Utilisation de Jasmine en tant que bibliothèque

Vous pouvez également utiliser Jasmine en tant que bibliothèque dans votre projet. Par exemple, le code suivant importe et exécute Jasmine :

```javascript
var Jasmine = require('jasmine');
var jasmine = new Jasmine();

jasmine.loadConfigFile('spec/support/jasmine.json');

jasmine.execute();
```

Tout d'abord, nous importons Jasmine et utilisons la méthode `loadConfigFile()` pour charger le fichier de configuration disponible à partir du chemin `spec/support/jasmine.json`, puis nous exécutons finalement Jasmine.

### Utilisation de Jasmine via la CLI

Vous pouvez également utiliser Jasmine à partir de la CLI, ce qui vous permet d'exécuter facilement des tests Jasmine et d'afficher les résultats dans le terminal par défaut.

Nous suivrons cette approche pour exécuter nos tests d'exemple dans ce guide. Tout d'abord, exécutez la commande suivante pour installer Jasmine globalement :

```bash
npm install -g jasmine
```

> _Vous devrez peut-être exécuter **sudo** pour installer des packages npm globalement en fonction de votre [configuration npm](https://docs.npmjs.com/getting-started/fixing-npm-permissions)._

Maintenant, créez un dossier pour votre projet et naviguez à l'intérieur :

```bash
$ mkdir jasmine-project $ cd jasmine-project
```

Ensuite, exécutez la commande suivante pour initialiser votre projet pour Jasmine :

Cette commande crée simplement un dossier spec et un fichier de configuration JSON. Voici le résultat de la commande `dir` :

```bash
.
[0;34m[0;34m[0;34mspec[0m
    [0;34m[0;34m[0;34msupport[0m
        [0;34m[0;34m[0;34mjasmine.json[0m

2 directories, 1 file
```

Voici le contenu d'un fichier `jasmine.json` par défaut :

```js
{
  "spec_dir": "spec",
  "spec_files": [
    "**/*[sS]pec.js"
  ],
  "helpers": [
    "helpers/**/*.js"
  ],
  "stopSpecOnExpectationFailure": false,
  "random": true
}
```

* `spec_dir` : spécifie où Jasmine cherche les fichiers de test.
* `spec_files` : spécifie les motifs des fichiers de test, par défaut tous les fichiers JS qui se terminent par les chaînes **Spec** ou **spec**.
* `helpers` : spécifie où Jasmine cherche les fichiers d'assistance. Les fichiers d'assistance sont exécutés avant les spécifications et peuvent être utilisés pour définir des matchers personnalisés.
* `stopSpecOnExpectationFailure` : lorsqu'il est défini sur true, arrête immédiatement une spécification à la première défaillance d'une attente (peut être utilisé comme option CLI via `--stop-on-failure`).
* `random` : lorsqu'il est défini sur true, Jasmine exécute les cas de test de manière pseudo-aléatoire (peut être utilisé comme option CLI via `--random`).

Les tableaux `spec_files` et `helpers` peuvent également contenir des motifs [Glob](https://en.wikipedia.org/wiki/Glob_(programming)) (grâce au package [node-glob](https://github.com/isaacs/node-glob)) pour spécifier les chemins de fichiers, qui sont des motifs que vous utilisez généralement pour spécifier un ensemble de fichiers lorsque vous travaillez dans Bash (par exemple, `ls *.js`).

Si vous n'utilisez pas l'emplacement par défaut pour le fichier de configuration `jasmine.json`, vous devez simplement spécifier l'emplacement personnalisé via l'option `jasmine --config`.

Vous pouvez trouver plus d'options CLI dans la documentation officielle [docs](https://jasmine.github.io/setup/nodejs.html).

### Comprendre Jasmine

Dans cette section, nous apprendrons les éléments de base des tests Jasmine tels que les suites, les spécifications, les attentes, les matchers et les espions, etc.

Dans le dossier de votre projet, exécutez la commande suivante pour initialiser un nouveau module Node :

Cela créera un fichier `package.json` avec des informations par défaut :

```js
{
  "name": "jasmine-project",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
```

Ensuite, créez un fichier `index.js` et ajoutez le code suivant :

```js
function fibonacci(n){

    if (n === 1) {
        return [0, 1];
    }
    else {
        var s = fibonacci(n - 1);
        s.push(s[s.length - 1] + s[s.length - 2]);
        return s;
    }
}
function isPrime(num){
    for (let i = 2; i < num; i++)
        if (num % i === 0) return false;
    return num !== 1 && num !== 0;
}
function isEven(n) {
    return n % 2 == 0;
}
function isOdd(n) {
    return Math.abs(n % 2) == 1;
}

function toLowerCase(str){
    return str.toLowerCase();
}
function toUpperCase(str){
    return str.toUpperCase();
}
function contains(str, substring, fromIndex){
    return str.indexOf(substring, fromIndex) !== -1;
}
function repeat(str, n){
    return (new Array(n + 1)).join(str);
}

module.exports = {
    fibonacci: fibonacci,
    isPrime: isPrime,
    isEven: isEven,
    isOdd: isOdd,
    toLowerCase: toLowerCase,
    toUpperCase: toUpperCase,   
    contains: contains,
    repeat: repeat
};
```

### Suites

Une suite regroupe un ensemble de spécifications ou de cas de test. Elle est utilisée pour tester un comportement spécifique du code JavaScript qui est généralement encapsulé par un objet/classe ou une fonction. Elle est créée en utilisant la fonction globale Jasmine `describe()` qui prend deux paramètres, le titre de la suite de test et une fonction qui implémente le code réel de la suite de test.

Commençons par créer notre première suite de test. À l'intérieur du dossier `spec`, créez un fichier `MyJSUtilitiesSpec.js` et ajoutez :

```js
describe("MyJSUtilities", function() { /* ... */ });
```

_MyJSUtilities_ est le nom de cette suite de test de niveau supérieur.

#### Comment regrouper et imbriquer les suites

Pour mieux organiser et décrire précisément notre ensemble de tests, nous pouvons imbriquer des suites à l'intérieur de la suite de niveau supérieur. Par exemple, ajoutons deux suites à la suite _MyJSUtilities_ :

```js
describe("String Utils", function() { /*...*/});describe("Math Utils", function() { /*...*/});
```

À l'intérieur de la suite _Math Utils_, ajoutons également deux suites imbriquées :

```js
describe("Basic Math Utils", function() {   /* ... */ }); describe("Advanced Math Utils", function() {   /* ... */ });
```

Nous regroupons les tests liés en tests pour _String Utils_, _Basic Math Utils_ et _Advanced Math Utils_ et les imbriquons à l'intérieur de la suite de test de niveau supérieur _MyJSUtilities_. Cela composera vos spécifications sous forme d'arbres similaires à une structure de dossiers.

La structure d'imbrication sera affichée dans le rapport, ce qui vous permettra de trouver facilement les tests qui échouent.

#### Comment exclure les suites

Vous pouvez désactiver temporairement une suite en utilisant la fonction `xdescribe()`. Elle a la même signature (paramètres) qu'une fonction `describe()`, ce qui signifie que vous pouvez rapidement désactiver vos suites existantes en ajoutant simplement un `x` à la fonction.

Les spécifications dans une fonction `xdescribe()` seront marquées comme en attente et ne seront pas exécutées dans le rapport.

### Specs

Une spécification déclare un cas de test qui appartient à une suite de test. Cela se fait en appelant la fonction globale Jasmine `it()` qui prend deux paramètres, le titre de la spécification (qui décrit la logique que nous voulons tester) et une fonction qui implémente le cas de test réel.

Une spécification peut contenir une ou plusieurs attentes. Chaque attente est simplement une assertion qui peut retourner soit `true` soit `false`. Pour que la spécification soit réussie, toutes les attentes appartenant à la spécification doivent être `true`, sinon la spécification échoue.

À l'intérieur de notre suite _String Utils_, ajoutez ces spécifications :

```js
describe("String Utils", function() {  it("should be able to lower case a string",function() {    /*...*/  });  it("should be able to upper case a string",function() {    /*...*/  });  it("should be able to confirm if a string contains a substring",function() {    /*...*/  });  it("should be able repeat a string multiple times",function() {    /*...*/  });});
```

À l'intérieur de notre suite _Basic Math Utils_, ajoutons quelques spécifications :

```js
describe("Basic Math Utils", function() {  it("should be able to tell if a number is even",function() {    /*...*/  });     it("should be able to tell if a number is odd",function() {    /*...*/  });     });
```

Pour les _Advanced Math Utils_, ajoutons les spécifications :

```js
describe("Advanced Math Utils", function() {  it("should be able to tell if a number is prime",function() {    /*...*/  });   it("should be able to calculate the fibonacci of a number",function() {    /*...*/  }); });
```

#### Comment exclure les spécifications

Tout comme les suites, vous pouvez également exclure des spécifications individuelles en utilisant la fonction `xit()` qui désactive temporairement la spécification `it()` et marque la spécification comme en attente.

### Attentes

Les attentes sont créées en utilisant la fonction `expect()` qui prend une valeur appelée **actual** (cela peut être des valeurs, des expressions, des variables, des fonctions ou des objets, etc.). Les attentes composent la spécification et sont utilisées avec des fonctions de matcher (via chaînage) pour définir ce que le développeur attend d'une unité de code spécifique pour effectuer.

Une fonction de matcher compare une valeur **actual** (passée à la fonction `expect()` avec laquelle elle est chaînée) et une valeur **expected** (directement passée en tant que paramètre au matcher) et retourne soit **true** soit **false**, ce qui soit **réussit** soit **échoue** la spécification.

Vous pouvez chaîner la fonction `expect()` avec plusieurs matchers. Pour nier/inverser le résultat booléen de n'importe quel matcher, vous pouvez utiliser le mot-clé `not` avant d'appeler le matcher.

Implémentons les spécifications de notre exemple. Pour l'instant, nous utiliserons `expect()` avec le matcher `nothing()` qui fait partie des matchers intégrés que nous verrons un peu plus tard. Cela passera toutes les spécifications puisque nous n'attendons rien à ce stade.

```js
describe("MyJSUtilities", function() {describe(">String Utils", function() {  it("should be able to lower case a string",function() {    expect().nothing();  });  it("should be able to upper case a string",function() {    expect().nothing();  });  it("should be able to confirm if a string contains a substring",function() {    expect().nothing();  });  it("should be able repeat a string multiple times",function() {    expect().nothing();  });     });describe("Math Utils", function() { describe("Basic Math Utils", function() {  it("should be able to tell if a number is even",function() {    expect().nothing();  });     it("should be able to tell if a number is odd",function() {    expect().nothing();  });    }); describe("Advanced Math Utils", function() {  it("should be able to tell if a number is prime",function() {    expect().nothing();  });   it("should be able to calculate the fibonacci of a number",function() {    expect().nothing();  });     }); });});
```

Voici une capture d'écran des résultats à ce stade :

![Image](https://cdn-media-1.freecodecamp.org/images/jvFGz7IVrci3GpsfT520cJg1T9lK3puc8Fca)

Nous avons huit spécifications réussies et zéro échec.

Vous pouvez soit utiliser des matchers intégrés, soit également créer vos propres matchers personnalisés pour vos besoins spécifiques.

### Matchers intégrés

Jasmine fournit un ensemble riche de matchers intégrés. Voici quelques-uns des plus importants :

* `toBe()` pour tester l'identité,
* `toBeNull()` pour tester `null`,
* `toBeUndefined()/toBeDefined()` pour tester `undefined`/non `undefined`,
* `toBeNaN()` pour tester NaN (Not A Number)
* `toEqual()` pour tester l'égalité,
* `toBeFalsy()/toBeTruthy()` pour tester la fausseté/véracité, etc.

Vous pouvez trouver la liste complète des matchers dans la [documentation](https://jasmine.github.io/api/edge/matchers.html).

Implémentons maintenant nos spécifications avec certains de ces matchers lorsque cela est approprié. Tout d'abord, importez les fonctions que nous testons dans notre fichier `MyJSUtilitiesSpec.js` :

```
const utils = require("../index.js");
```

Ensuite, commencez par la suite _String Utils_ et changez `expect().nothing()` par les attentes appropriées.

Par exemple, pour la première spécification, nous attendons que la méthode `toLowerCase()` soit d'abord définie et deuxièmement qu'elle retourne une chaîne en minuscules, c'est-à-dire :

```js
it("should be able to lower case a string",function() {        expect(utils.toLowerCase).toBeDefined();        expect(utils.toLowerCase("HELLO WORLD")).toEqual("hello world");  });
```

Voici le code complet pour la suite :

```js
describe(">String Utils", function() {  it("should be able to lower case a string",function() {    expect(utils.toLowerCase).toBeDefined();    expect(utils.toLowerCase("HELLO WORLD")).toEqual("hello world");  });  it("should be able to upper case a string",function() {    expect(utils.toUpperCase).toBeDefined();    expect(utils.toUpperCase("hello world")).toEqual("HELLO WORLD");  });  it("should be able to confirm if a string contains a substring",function() {    expect(utils.contains).toBeDefined();    expect(utils.contains("hello world","hello",0)).toBeTruthy();  });  it("should be able repeat a string multiple times",function() {    expect(utils.repeat).toBeDefined();    expect(utils.repeat("hello", 3)).toEqual("hellohellohello");  });     });
```

### Matchers personnalisés

Jasmine offre la possibilité d'écrire des [matchers personnalisés](https://jasmine.github.io/tutorials/custom_matcher.html) pour implémenter des assertions non couvertes par les matchers intégrés ou simplement pour rendre les tests plus descriptifs et lisibles.

Par exemple, prenons la spécification suivante :

```js
it("should be able to tell if a number is even",function() {    expect(utils.isEven).toBeDefined();    expect(utils.isEven(2)).toBeTruthy();    expect(utils.isEven(1)).toBeFalsy();  });
```

Supposons que la méthode `isEven()` ne soit pas implémentée. Si nous exécutons les tests, nous obtiendrons des messages comme dans la capture d'écran suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/dHjK8DH8lMJRdUzXj23GiUMTPJ75zOg9rtbe)

Le message d'échec que nous obtenons dit _Expected undefined to be defined_, ce qui ne nous donne aucune indication de ce qui se passe. Alors, rendons ce message plus significatif dans le contexte de notre domaine de code (ce qui sera plus utile pour les bases de code complexes). À cette fin, créons un matcher personnalisé.

Nous créons des matchers personnalisés en utilisant la méthode `addMatchers()` qui prend un objet composé d'une ou plusieurs propriétés qui seront ajoutées en tant que matchers. Chaque propriété doit fournir une fonction de fabrication qui prend deux paramètres : `util`, qui possède un ensemble de fonctions utilitaires pour les matchers à utiliser (voir : `[matchersUtil.js](https://github.com/pivotal/jasmine/blob/master/src/core/matchers/matchersUtil.js)`) et `customEqualityTesters` qui doit être passé si `util.equals` est appelé, et doit retourner un objet avec une fonction `compare` qui sera appelée pour vérifier l'attente.

Nous devons enregistrer le matcher personnalisé avant d'exécuter chaque spécification en utilisant la méthode `beforeEach()` :

```js
describe("/Basic Math Utils", function () {beforeEach(function () {jasmine.addMatchers({hasEvenMethod:  function (util, customEqualityTesters) {return {compare:  function (actual, expected) {var  result  = { pass:  utils.isEven  !==  undefined };if (result.pass) {result.message  =  "Expected isEven() to be not defined."}else {result.message  =  "Expected isEven() to be defined."}return  result;}}}});});/*...*/});
```

Nous pouvons ensuite utiliser le matcher personnalisé au lieu de `expect(utils.isEven).toBeDefined()` :

```js
expect().hasEvenMethod();
```

Cela nous donnera un meilleur message d'échec :

![Image](https://cdn-media-1.freecodecamp.org/images/OulftEemEqJoqGYNoPhHY4v3ok1VE5LE0K05)

### Utilisation de beforeEach() et afterEach()

Pour initialiser et nettoyer vos spécifications, Jasmine fournit deux fonctions globales, `beforeEach()` et `afterEach()` :

* La fonction `beforeEach` est appelée une fois avant chaque spécification dans la suite où elle est appelée.
* La fonction `afterEach` est appelée une fois après chaque spécification dans la suite où elle est appelée.

Par exemple, si vous devez utiliser des variables dans votre suite de test, vous pouvez simplement les déclarer au début de la fonction `describe()` et mettre tout code d'initialisation ou d'instanciation à l'intérieur d'une fonction `beforeEach()`. Enfin, vous pouvez utiliser la fonction `afterEach()` pour réinitialiser les variables après chaque spécification afin d'avoir des tests unitaires purs sans avoir besoin de répéter le code d'initialisation et de nettoyage pour chaque spécification.

La fonction `beforeEach()` est également parfaitement combinée avec de nombreuses API Jasmine telles que la méthode `addMatchers()` pour créer des matchers personnalisés ou également avec la fonction `done()` pour attendre les opérations asynchrones avant de continuer les tests.

### Échec d'un test

Vous pouvez forcer un test à échouer en utilisant la méthode globale `fail()` disponible dans Jasmine. Par exemple :

```js
it("should explicitly fail", function () { fail('Forced to fail'); });
```

Vous devriez obtenir l'erreur suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/A0qZ0VRL7KrP2Xu0cCsRUq6vW4SRcMwov6Mn)

### Test des exceptions

Lorsque vous testez votre code, des erreurs et des exceptions peuvent être levées, vous pourriez donc avoir besoin de tester ces scénarios. Jasmine fournit les matchers `toThrow()` et `toThrowError()` pour tester lorsqu'une exception est levée ou pour tester une exception spécifique, respectivement.

Par exemple, si nous avons une fonction qui lève une exception `TypeError` :

```js
function throwsError() { throw new TypeError("A type error"); }
```

Vous pourriez écrire une spécification pour tester si une exception est levée :

```
it('it should throw an exception', function () { expect(throwsError).toThrow(); });
```

Ou vous pourriez également tester l'exception spécifique `TypeError` :

```js
it('it should throw a TypeError', function () { expect(throwsError).toThrowError(TypeError); });
```

### Comprendre les espions

Plus souvent qu'autrement, les méthodes dépendent d'autres méthodes. Cela signifie que lorsque vous testez une méthode, vous pouvez également tester ses dépendances. Cela n'est pas recommandé dans les tests, c'est-à-dire que vous devez vous assurer de tester la fonction pure en isolant la méthode et en voyant comment elle se comporte étant donné un ensemble d'entrées.

Jasmine fournit des [espions](http://jasmine.github.io/2.0/introduction.html#section-Spies) qui peuvent être utilisés pour espionner/écouter les appels de méthodes sur des objets et signaler si une méthode est appelée et avec quel contexte et arguments.

Jasmine fournit deux façons d'espionner les appels de méthodes : en utilisant les méthodes `spyOn()` ou `createSpy()`.

Vous pouvez utiliser `spyOn()` lorsque la méthode existe déjà sur l'objet, sinon vous devez utiliser `jasmine.createSpy()` qui retourne une nouvelle fonction.

Par défaut, un espion signalera uniquement si un appel a été effectué sans appeler la fonction espionnée (c'est-à-dire que la fonction cessera de s'exécuter), mais vous pouvez modifier le comportement par défaut en utilisant ces méthodes :

* `and.callThrough()` : appelle la fonction originale,
* `and.returnValue(value)` : retourne la valeur spécifiée,
* `and.callFake(fn)` : appelle la fonction fictive au lieu de la fonction originale,
* `and.throwError(err)` : lève une erreur,
* `and.stub()` : réinitialise le comportement de substitution par défaut.

Vous pouvez utiliser un espion pour recueillir des statistiques d'exécution sur la fonction espionnée, par exemple si vous voulez savoir combien de fois votre fonction a été appelée.

Supposons que nous voulons nous assurer que notre méthode `toUpperCase()` utilise la méthode intégrée `String.toUpperCase()`, nous devons simplement espionner `String.toUpperCase()` en utilisant :

```js
it("should be able to upper case a string", function () { 
```

```
var spytoUpperCase = spyOn(String.prototype, 'toUpperCase') 
```

```
expect(utils.toUpperCase).toBeDefined(); expect(utils.toUpperCase("hello world")).toEqual("HELLO WORLD"); expect(String.prototype.toUpperCase).toHaveBeenCalled(); expect(spytoUpperCase.calls.count()).toEqual(1); });
```

![Image](https://cdn-media-1.freecodecamp.org/images/k-BN6V3GrUluGjMy3gtCMOAeae6wvu4CVu52)

Le test a échoué en raison de la deuxième attente car `utils.toUpperCase("hello world")` a retourné undefined au lieu de _HELLO WORLD_. C'est parce que, comme nous l'avons mentionné, après avoir créé l'espion sur `toUpperCase()`, la méthode n'est pas exécutée. Nous devons changer ce comportement par défaut en appelant `callThrough()` :

> _Veuillez noter qu'une fonction `spy` remplace la fonction espionnée par un stub par défaut. Si vous devez appeler la fonction originale à la place, vous pouvez ajouter `.and.callThrough()` à votre objet `spy`._

```
var spytoUpperCase = spyOn(String.prototype, 'toUpperCase').and.callThrough();
```

Maintenant, toutes les attentes passent.

Vous pouvez également utiliser `and.callFake()` ou `and.returnValue()` pour simuler soit la fonction espionnée, soit simplement la valeur de retour si vous ne souhaitez pas appeler la fonction réelle :

```
var spytoUpperCase = spyOn(String.prototype, 'toUpperCase').and.returnValue("HELLO WORLD"); 
```

```js
var spytoUpperCase = spyOn(String.prototype, 'toUpperCase').and.callFake(function(){ return "HELLO WORLD"; });
```

Maintenant, si nous finissons par ne pas utiliser le `String.toUpperCase()` intégré dans notre propre implémentation de `utils.toUpperCase()`, nous obtiendrons ces échecs :

![Image](https://cdn-media-1.freecodecamp.org/images/z43QKVly7yBHOnKndLsZ6Id4roK-G0ut9ufK)

Les deux attentes `expect(String.prototype.toUpperCase).toHaveBeenCalled()` et `expect(spytoUpperCase.calls.count()).toEqual(1)` ont échoué.

### Comment gérer l'asynchronicité dans Jasmine

Si le code que vous testez contient des opérations asynchrones, vous avez besoin d'un moyen de faire savoir à Jasmine lorsque les opérations asynchrones sont terminées.

Par défaut, Jasmine attend que toute opération asynchrone, définie par un rappel, une promesse ou le mot-clé `async`, soit terminée. Si Jasmine trouve un rappel, une promesse ou un mot-clé async dans l'une de ces fonctions : `beforeEach`, `afterEach`, `beforeAll`, `afterAll`, et `it`, il attendra que l'opération asynchrone soit terminée avant de passer à l'opération suivante.

### Utilisation de `done()` avec `beforeEach()`/`it()` ..



Prenons notre exemple `simulateAsyncOp()` qui simule une opération asynchrone en utilisant `setTimeout()`. Dans un scénario réel, cela peut être une requête Ajax ou toute autre chose similaire qui se produit de manière asynchrone :

```js
function simulateAsyncOp(callback){ 
```

```
setTimeout(function () { callback(); }, 2000); }
```

Pour tester cette fonction, nous pouvons utiliser la fonction `beforeEach()` avec le rappel spécial `done()`. Notre code doit invoquer `done()` pour indiquer à Jasmine que l'opération asynchrone est terminée :

```js
describe("/Async Op", function () {var  asyncOpCompleted  =  false;beforeEach(function (done) {utils.simulateAsyncOp(function(){  asyncOpCompleted  =  true;  done();});});it("should be able to tell if the async call has completed", function () {  expect(asyncOpCompleted).toEqual(true);});});
```

Nous pouvons rapidement remarquer un inconvénient de cette méthode, nous devons donc écrire notre code pour accepter le rappel `done()`. Dans notre cas, nous n'avons pas codé en dur la méthode `done()` dans notre `simulateAsyncOp(fn)`, mais nous avons fourni un paramètre de rappel juste pour pouvoir appeler `done()`.

### Utilisation des promesses

Si vous ne voulez pas créer de code qui dépend de la façon dont vous écrivez votre test, vous pouvez utiliser une promesse à la place et appeler le rappel `done()` lorsque la promesse est résolue. Ou mieux encore, dans Jasmine 2.7+, si votre code retourne une `Promise`, Jasmine attendra qu'elle soit résolue ou rejetée avant d'exécuter le code suivant.

### Utilisation de async/await

Jasmine 2.7+ prend en charge les appels `async` et `await` dans les spécifications. Cela vous évite de mettre des assertions dans un bloc `.then()` ou `.catch()`.

```js
it("should work with async/await", async () => { let completed = false; completed = await utils.simulateAsyncOp(); expect(completed).toEqual(true); });
```

Voici l'implémentation de `simulateAsyncOp` :

```js
function simulateAsyncOp() { 
```

```js
return new Promise(resolve => { setTimeout(() => { resolve(true); }, 1000); }); }
```

### Utilisation de l'horloge Jasmine

L'horloge Jasmine est utilisée pour tester le code asynchrone qui dépend des fonctions de temps telles que `setTimeout()` de la même manière que nous testons le code synchrone en simulant les API basées sur le temps avec des méthodes personnalisées. De cette manière, vous pouvez exécuter les fonctions testées de manière synchrone en contrôlant ou en faisant avancer manuellement l'horloge.

Vous pouvez installer l'horloge Jasmine en appelant la fonction `jasmine.clock().install` dans votre spécification ou suite.

Après avoir utilisé l'horloge, vous devez la désinstaller pour restaurer les fonctions originales.

Avec l'horloge Jasmine, vous pouvez contrôler les fonctions JavaScript `setTimeout` ou `setInterval` en faisant avancer l'horloge afin de progresser dans le temps en utilisant la fonction `jasmine.clock().tick`, qui prend le nombre de millisecondes avec lequel vous pouvez vous déplacer.

Vous pouvez également utiliser l'horloge Jasmine pour simuler la date actuelle.

```js
beforeEach(function () {jasmine.clock().install();});afterEach(function() {jasmine.clock().uninstall();});it("should call the asynchronous operation synchronously", function() {var  completed  =  false;utils.simulateAsyncOp(function(){completed  =  true;});expect(completed).toEqual(false);jasmine.clock().tick(1001);expect(completed).toEqual(true);});
```

Voici la fonction `simulateAsyncOp` :

```
function simulateAsyncOp(callback){ 
```

```js
setTimeout(function () { callback(); }, 1000); }
```

> _Dans le cas où vous n'avez pas spécifié de temps pour la fonction `mockDate`, elle utilisera la date actuelle._

### Gestion des erreurs

Si votre code asynchrone échoue en raison d'une erreur, vous voulez que vos spécifications échouent correctement. À partir de Jasmine 2.6+, toute erreur non gérée est envoyée à la spécification actuellement exécutée.

Jasmine offre également un moyen que vous pouvez utiliser si vous devez explicitement faire échouer vos spécifications :

* en utilisant le rappel `done()` avec `beforeEach()` en appelant la méthode `done.fail(err)`,
* en passant simplement une erreur au rappel `done(err)` (Jasmine 3+),
* en appelant la méthode `reject()` d'une `Promise`.

### Conclusion

Dans ce guide, nous avons introduit Jasmine et vu comment commencer à utiliser Jasmine pour tester votre code JavaScript. Merci d'avoir lu !

Cet [article](https://www.techiediaries.com/jasmine-testing-tutorial/) a été initialement publié dans [techiediaries](https://www.techiediaries.com/).