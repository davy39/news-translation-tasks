---
title: '#LearnByDIY - Comment créer un framework de tests unitaires JavaScript à partir
  de zéro'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-09T03:01:20.000Z'
originalURL: https://freecodecamp.org/news/learnbydiy-how-to-create-a-javascript-unit-testing-framework-from-scratch-c94e0ba1c57a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*cedi3xCR8cINoPAje7Nrjw.jpeg
tags:
- name: DIY
  slug: diy
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Testing
  slug: testing
seo_title: '#LearnByDIY - Comment créer un framework de tests unitaires JavaScript
  à partir de zéro'
seo_desc: 'By Alcides Queiroz

  I promise, this is gonna be fun. =)

  Probably, automated tests are part of your daily routine (if not, please stop reading
  this article and start from the beginning, by learning from the father of TDD himself).
  You’ve been using tes...'
---

Par Alcides Queiroz

Je promets, ce sera amusant. =)

Probablement, les tests automatisés font partie de votre routine quotidienne (si ce n'est pas le cas, veuillez arrêter de lire cet article et [commencez par le début](https://www.amazon.com/Test-Driven-Development-By-Example/dp/0321146530), en apprenant du père du TDD lui-même). Vous avez utilisé des frameworks de test tels que [Node-tap](https://www.node-tap.org/) (ou [Tape](https://github.com/substack/tape)), [Jasmine](https://jasmine.github.io/), [Mocha](https://mochajs.org/) ou [QUnit](https://qunitjs.com/) depuis un certain temps, en acceptant simplement qu'ils font des choses magiques et sans poser trop de questions à leur sujet. Ou, si vous êtes comme moi, peut-être êtes-vous toujours curieux de savoir comment les choses fonctionnent, y compris les frameworks de test, bien sûr.

Cet article vous guidera à travers le processus de création d'un framework de test JavaScript à partir de zéro, avec un DSL assez décent et une sortie détaillée. Il s'agit du premier article de ma série **#LearnByDIY**. L'idée est de démystifier certains types de logiciels auxquels nous sommes habitués, en créant des versions simplifiées de ceux-ci.

#### Avertissements

Avant de commencer, quelques notes importantes :

* Le but de cet article n'est **pas** de créer un outil prêt pour la production. S'il vous plaît, **n'utilisez pas le framework que nous allons créer pour tester du code de production**. Son but est purement éducatif. =)
* Naturellement, notre petit framework ne sera pas complet. Des choses comme les tests asynchrones, les exécutions parallèles, un ensemble plus riche de matchers, un CLI (avec des options comme `--watch`), des rapporteurs et des DSL pluggables, etc., ne seront pas présents dans notre version finale. Cependant, je **recommande fortement** que vous continuiez à jouer avec ce projet et que vous essayiez peut-être d'**implémenter certaines de ces parties manquantes**. Peut-être pouvez-vous le transformer en un projet open source sérieux. J'adorerais savoir que ce projet de jouet est devenu un framework de test "réel".

### ⚔️ Tyrion - Un petit framework de test

Notre framework sera minuscule, mais "brave" pour sa taille. Donc, il n'y a pas de meilleur nom que Tyrion (ouais, c'est aussi mon personnage préféré de GoT).

![Image](https://cdn-media-1.freecodecamp.org/images/1*cedi3xCR8cINoPAje7Nrjw.jpeg)
_Tyrion est petit, mais brave._

Nous utiliserons Node.js dans ce projet, avec les bons vieux modules CommonJS. La version minimale de Node dont vous aurez besoin est v8.6.0. Si vous avez une version plus ancienne, veuillez la mettre à jour.

Oh, j'ai presque oublié... J'utilise [Yarn](https://yarnpkg.com/lang/en/docs/install/) tout au long de cet article, pour des choses comme `yarn init`, `yarn link` et ainsi de suite, mais vous pouvez utiliser le "vanilla" NPM de manière similaire (`npm init`, `npm link`, ...).

#### Création de la structure de dossiers du projet

Tout d'abord, créons la structure de dossiers suivante :

```
tyrion/||______ proj/|      ||      |______ src/||______ playground/       |       |______ src/       |______ tests/
```

En d'autres "mots" :

```
$ mkdir -p tyrion/proj/src tyrion/playground/src tyrion/playground/tests
```

Nous avons besoin de deux dossiers, chacun pour un projet séparé.

* Le dossier `proj` contiendra le package du framework Tyrion.
* Le dossier `playground` contiendra un projet Node jetable pour jouer avec notre framework. Il servira de laboratoire pendant notre processus de développement.

#### Initialisation des projets Node

Allez dans le dossier `playground` et exécutez `yarn init -y`. Cette commande génère un fichier package.json de base. Ouvrez-le, supprimez la ligne `"main": "index.js",` et ajoutez une entrée "scripts" comme dans l'exemple ci-dessous :

```
{  "name": "playground",  "version": "1.0.0",  "scripts": {    "test": "node tests"  },  "license": "MIT"}
```

Après avoir créé ce fichier, faisons de même pour l'autre projet, le package Tyrion lui-même. Dans le dossier `proj`, exécutez `yarn init`. Il vous demandera certaines informations pour créer correctement le fichier package.json. Entrez les valeurs suivantes (en gras) :

```
question name (proj): tyrion <enter>question version (1.0.0): <enter>question description: <enter>question entry point (index.js): src/index.js <enter>question repository url: <enter>question author: <enter>question license (MIT): <enter>question private: <enter>
```

Maintenant, nous devons installer Tyrion comme une dépendance de développement dans notre projet playground. Si c'était un package publié, nous n'aurions besoin que de l'installer directement, via `npm i --dev` ou `yarn add --dev`. Comme nous n'avons Tyrion qu'en local, ce n'est pas possible. Heureusement, Yarn et NPM ont une fonctionnalité pour aider les développeurs pendant cette phase d'inception de package, nous permettant de simuler un lien entre deux packages (l'un comme dépendance de l'autre).

Pour créer ce lien de dépendance, allez dans le dossier `proj` et exécutez :

```
$ yarn link
```

Ensuite, dans le dossier `playground`, exécutez :

```
$ yarn link tyrion 
```

C'est tout. Maintenant Tyrion est une dépendance du projet playground.

#### Création de quelques modules pour être nos "cobayes"

Dans le dossier `playground/src`, créons deux modules à tester par Tyrion :

#### Écriture de quelques tests

Maintenant, il est temps d'utiliser notre imagination. À quoi devrait ressembler le DSL de Tyrion ? En avez-vous marre de `expect`, `assert`, et ainsi de suite ? Faisons quelque chose de différent, juste pour le plaisir. Je suggère `guarantee` comme notre fonction d'assertion. Ça vous plaît ?

Écrivons quelques tests pour voir cela plus clairement. Bien sûr, rien ne fonctionnera, puisque nous n'avons rien implémenté dans notre framework.

Et un fichier `tests/index.js`, pour importer nos tests en un seul endroit.

Tyrion empruntera l'un des principes de Node-tap :

> **Les fichiers de test doivent être des programmes "normaux" qui peuvent être exécutés directement.**

> Cela signifie qu'il ne peut pas nécessiter un runner spécial qui met des fonctions magiques dans un espace global. `node test.js` est un moyen parfaitement acceptable d'exécuter un test, et il devrait fonctionner exactement de la même manière que lorsqu'il est exécuté par le runner sophistiqué avec reporting et autres. Les tests JavaScript doivent être des programmes JavaScript ; pas des poèmes en langue anglaise avec une ponctuation étrange.

> [https://www.node-tap.org/#tutti-i-gusti-sono-gusti](https://www.node-tap.org/#tutti-i-gusti-sono-gusti).

Comme vous vous en souvenez peut-être, dans notre fichier package.json du playground, nous avons un script `test` qui exécute simplement `node tests`. Donc, pour l'exécuter, tapez simplement `npm test` et appuyez sur entrée. Oui, faites-le. Voyons-le planter :

![Image](https://cdn-media-1.freecodecamp.org/images/1*9h8lW-Kon3LuqlqQUI-0hA.png)

Cette erreur est claire. Nous n'avons rien dans notre framework. Aucun module n'est exporté du tout. Pour le corriger, dans le dossier `proj`, créez un fichier `src/index.js` exportant un objet vide, comme vous pouvez le voir ci-dessous :

```
module.exports = {};
```

Maintenant, nous allons exécuter `npm test` à nouveau :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ge5-uzTfUm-2bgrB8Gm3SQ.png)

Node se plaint parce que notre fonction `guarantee` n'existe pas. C'est simple à corriger, aussi :

```
const guarantee = () => {};
```

```
module.exports = { guarantee };
```

Exécutez à nouveau le script de test :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZNsFSHaRf8JWCRake1fTNw.png)

Voilà ! Pas d'erreurs, mais rien ne se passe non plus. =(

#### La fonction guarantee

Notre fonction d'assertion devrait s'exécuter sans faille si la valeur fournie est [_truthy_](https://developer.mozilla.org/en-US/docs/Glossary/Truthy), mais devrait lancer une erreur si elle est [_falsy_](https://developer.mozilla.org/en-US/docs/Glossary/Falsy).

Implémentons-la :

Et pour tester si cela fonctionne, ajoutons une autre assertion à la fin de notre fichier `number-utils.test.js` :

```
guarantee(123 === 321); // Cela devrait échouer 
```

Maintenant, exécutez-le une fois de plus :

![Image](https://cdn-media-1.freecodecamp.org/images/1*O8V_b4cKO7zxutYoLVuRdw.png)

A-ha ! Cela fonctionne ! C'est laid, mais c'est fonctionnel.

#### La fonction check

Nous avons besoin d'un moyen d'encapsuler les assertions dans des unités de test. Basiquement, tous les frameworks de test ont cette fonctionnalité, comme la fonction `it` dans Jasmine ou la fonction `test` dans Node-tap.

Dans Tyrion, notre fonction d'unité de test s'appellera `check`. Sa signature devrait être `check(testDescription, callback)`. Nous voulons également qu'elle nous donne une sortie plus conviviale, décrivant les tests réussis et échoués.

Voici à quoi cela ressemblera :

Maintenant, nous pouvons réécrire nos tests pour utiliser la nouvelle fonction `check` :

Et relancer notre suite de tests :

![Image](https://cdn-media-1.freecodecamp.org/images/1*CMuw0w6MzEfrKsyvR2QykQ.png)

Cool. Mais... qu'en est-il des couleurs ?? Ne serait-il pas plus facile de distinguer les tests réussis des tests échoués ?

Ajoutez le module [colors](https://www.npmjs.com/package/colors) comme dépendance :

```
yarn add colors
```

Donc, importez-le en haut du fichier `proj/src/index.js` :

```
const colors = require('colors');
```

Et ajoutons quelques couleurs à notre sortie :

```
const check = (title, cb) => {  try{    cb();    console.log(`${' OK '.bgGreen.black} ${title.green}`);  } catch(e) {    console.log(`${' FAIL '.bgRed.black} ${title.red}`);    console.log(e.stack.red);  }};
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*D_Qp69Sx7kC5AfX2N9nfzg.png)

C'est mieux. =)

#### La fonction xcheck

Il serait bien d'avoir un moyen facile de désactiver un test spécifique, comme la fonction `xit` dans Jasmine. Cela peut être facilement implémenté en créant une fonction no-op qui indique simplement qu'un test est désactivé (bien, ce n'est pas complètement no-op, mais presque) :

```
const xcheck = (title, cb) => {  console.log(`${' DISABLED '.bgWhite.black} ${title.gray}`);};
```

```
module.exports = { guarantee, check, xcheck };
```

Donc, importez la fonction `xcheck` dans le fichier `number-utils.test.js` et désactivez l'un de nos tests :

```
const { guarantee, check, xcheck } = require('tyrion');const numberUtils = require('../src/number-utils');
```

```
// method: isPrimexcheck('returns true for prime numbers', () => {  guarantee(numberUtils.isPrime(2));  guarantee(numberUtils.isPrime(3));  guarantee(numberUtils.isPrime(5));  guarantee(numberUtils.isPrime(7));  guarantee(numberUtils.isPrime(23));});
```

Et voici comment cela se comporte :

![Image](https://cdn-media-1.freecodecamp.org/images/1*kSCPsNlejl9OdZC8VUruyw.png)

#### Résumé des tests et code de sortie

Si nous voulions utiliser Tyrion sur un serveur CI, il devrait terminer son processus avec différents codes de sortie pour les conditions d'erreur et de succès.

Une autre fonctionnalité souhaitable est un résumé des tests. Il serait bien de savoir combien de tests ont réussi, échoué ou été ignorés (ceux désactivés). Pour cela, nous pourrions incrémenter des compteurs dans les fonctions `check` et `xcheck`.

Nous allons créer la fonction `end`, qui imprime le résumé des tests et termine avec le code de sortie approprié :

Et n'oubliez pas de l'appeler dans le fichier `playground/tests/index.js` :

```
const { end } = require('tyrion');
```

```
require('./string-utils.test');require('./number-utils.test');
```

```
end();
```

Ou peut-être :

```
const tyrion = require('tyrion');
```

```
require('./string-utils.test');require('./number-utils.test');
```

```
tyrion.end();
```

Maintenant, relançons `npm test` :

![Image](https://cdn-media-1.freecodecamp.org/images/1*MK7W8WxuDSD6grErVrSZKA.png)

Super, cela fonctionne.

#### La fonction group

De nombreux frameworks de test ont un moyen de regrouper les tests liés. Dans Jasmine, par exemple, il y a la fonction `describe`. Nous allons implémenter une fonction `group` à cette fin :

Et mettons à jour nos tests pour utiliser cette nouvelle fonction :

Voici la nouvelle sortie :

![Image](https://cdn-media-1.freecodecamp.org/images/1*8y2171rDoHbOhGMIt3myGw.png)

Eh bien, la bonne nouvelle est que cela fonctionne. La mauvaise nouvelle est que cela devient difficile à comprendre. Nous avons besoin d'un moyen d'indenter cette sortie afin de la rendre plus lisible :

Relancez-le :

![Image](https://cdn-media-1.freecodecamp.org/images/1*X1QQ7GuihVzZkFS6yQ91Jg.png)

C'est bien mieux !

Alors, comment cela fonctionne-t-il ?

* La fonction `repeat` répète une chaîne `n` fois.
* La fonction `indent` répète une indentation (de quatre espaces) `n` fois en utilisant la fonction `repeat`.
* La fonction `indentLines` indent une chaîne avec plusieurs lignes en ajoutant `n` indentations au début de chaque ligne. Nous l'utilisons pour indenter les piles d'erreurs.
* La variable `indentLevel` est incrémentée au début de chaque exécution de groupe et décrémentée à la fin. De cette façon, les groupes imbriqués peuvent être correctement indentés.

#### Plus de matchers

La fonction `guarantee` n'est pas assez flexible pour de nombreux scénarios. Nous avons besoin d'un ensemble plus riche de matchers afin de rendre nos tests plus significatifs.

Tout d'abord, créez le dossier `matchers` :

```
$ mkdir proj/src/matchers
```

Maintenant, nous allons créer chaque matcher dans un fichier séparé :

Le matcher `same` utilise l'opérateur d'égalité stricte (===) pour tester si deux arguments sont exactement le même objet (pour les types de référence) ou égaux (pour les types primitifs). Il se comporte de manière similaire au matcher `toBe` dans Jasmine et `t.equal` dans node-tap.

**Note :** Node-tap a également un matcher appelé `t.same`, mais il fonctionne différemment (il ne vérifiera pas si deux objets sont exactement les mêmes, mais s'ils sont profondément équivalents).

Le matcher `identical` vérifie que deux arguments sont équivalents. Il utilise l'opérateur `==` pour comparer les valeurs.

Le matcher `deeplyIdentical` fait une comparaison profonde de deux objets. Ce type de comparaison peut être considérablement complexe, ou au moins trop complexe pour le but de cet article. Donc, installons un module existant pour gérer l'égalité profonde et utilisons-le dans notre matcher :

```
$ yarn add deep-equal
```

Ensuite :

Voici à quoi ressemblera une erreur :

![Image](https://cdn-media-1.freecodecamp.org/images/1*P3SI0UMJlXOusnB0A9yrNw.png)

Le matcher `falsy` échouera si la valeur fournie est truthy.

Le matcher `truthy` fonctionne de manière similaire à notre fonction `guarantee`. Il réussit lorsque la valeur fournie est truthy et échoue si elle est falsy.

Le matcher `throws` réussira si une fonction lance une erreur. Il est possible de spécifier le message d'erreur souhaité, mais ce n'est pas obligatoire.

Un fichier `index.js` pour réexporter tous les matchers :

Et enfin, assemblons le tout :

Vous pouvez utiliser nos nouveaux matchers de cette manière :

```
const { guarantee, check } = require('tyrion');
```

```
check('playing with our new matchers', () => {  // La fonction guarantee originale fonctionne toujours  guarantee(123 === 123);
```

```
  guarantee.truthy('abc');  guarantee.falsy(null);
```

```
  const a = { whatever: 777 };  const b = a;  guarantee.same(a, b);  guarantee.identical(undefined, null);
```

```
  const c = { whatever: { foo: { bar: 'baz' } } };  const d = Object.assign({}, c);  guarantee.deeplyIdentical(c, d);
```

```
  function boom() { throw new Error('Some error...'); }  guarantee.throws(boom);  guarantee.throws(boom, 'Some error...');});
```

#### La fonction beforeEach

Pour implémenter une fonction `beforeEach`, nous devons utiliser une pile pour accumuler tous les callbacks `beforeEach`. Cela est fait pour chaque nouveau niveau de portée créé chaque fois qu'un groupe est déclaré :

Comment cela fonctionne-t-il ?

* Chaque fois qu'un groupe est déclaré, nous poussons un nouveau tableau dans la variable `beforeEachStack`. Ce tableau accumulera tous les callbacks `beforeEach` déclarés dans cette portée.
* Après qu'une exécution de groupe est terminée, nous supprimons le tableau au sommet de notre pile de callbacks.
* La fonction `beforeEach` reçoit un callback et l'ajoute au tableau au sommet de notre pile de callbacks.
* Au début de chaque fonction `check`, nous appelons chaque callback `beforeEach` à tous les niveaux de notre pile.

#### La fonction beforeAll

Notre dernière addition sera la fonction `beforeAll`. **Pour simplifier**, nous supposons que les appels à la fonction `beforeAll` seront toujours placés avant tous les groupes et tests (**ou**, lorsqu'ils sont dans une portée de groupe, tout en haut).

Sinon, si nous voulions nous assurer que la fonction `beforeAll` fonctionne correctement même au milieu ou à la fin d'un groupe, nous devrions changer radicalement notre logique existante. Eh bien, nous ne allons pas le faire, puisque ce n'est pas une utilisation rationnelle de cette fonction.

Notre version de `beforeAll` recevra simplement un callback et l'exécutera immédiatement.

```
const beforeAll = cb => cb();
```

```
module.exports = {   group, check, xcheck, guarantee, beforeAll, end };
```

Un exemple d'utilisation :

```
const { guarantee, check, group, beforeAll } = require('tyrion');
```

```
let a;beforeAll(() => {  a = { something: 'example' };});
```

```
group('playing with the beforeAll function', () => {  let b;  beforeAll(() => {    b = { something: 'example' };  });
```

```
  check('some test', () => {    guarantee.deeplyIdentical(a, b);  });
```

```
  check('another test', () => {    guarantee.identical(11, 11);  });});
```

#### La version finale de Tyrion

Cela a été un long voyage, mais Tyrion est enfin complet. =)

J'ai ajouté une option SILENT qui désactive la journalisation. Elle est utilisée pour faciliter le test de Tyrion (oui, les frameworks de test doivent aussi être testés).

Le projet complet est disponible [ici](https://www.github.com/alcidesqueiroz/tyrion).

#### Améliorations possibles

Tyrion manque de nombreuses fonctionnalités, comme :

* Support pour les tests asynchrones
* Exécution parallèle des tests
* Fonctions `afterEach` et `afterAll`
* Une fonction `xgroup`, qui désactive un groupe entier
* Une fonction similaire à [fit de Jasmine](https://jasmine.github.io/api/edge/global.html#fit)
* Espions
* Découplage du DSL de la logique de reporting.
* Rapporteurs pluggables
* Un CLI terminal (avec une option `--watch`)
* Encore plus de matchers
* Piles d'erreurs plus conviviales

Je vous encourage à continuer à jouer avec ce projet. N'hésitez pas à l'utiliser et à l'étendre. Veuillez me faire part de vos pensées, suggestions et expériences en laissant un commentaire ci-dessous. =)