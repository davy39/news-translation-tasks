---
title: Tutoriel sur le développement piloté par les tests – Comment tester vos applications
  JavaScript et ReactJS
subtitle: ''
author: Oluwatobi Sofela
co_authors: []
series: null
date: '2022-07-26T17:51:22.000Z'
originalURL: https://freecodecamp.org/news/test-driven-development-tutorial-how-to-test-javascript-and-reactjs-app
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/test-driven-development-tutorial-how-to-test-javascript-and-reactjs-app-codesweetly-battlecreek-coffee-roasters-i22gbC3gFm4-unsplash.jpg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Software Testing
  slug: software-testing
- name: test driven development
  slug: test-driven-development
- name: Testing
  slug: testing
seo_title: Tutoriel sur le développement piloté par les tests – Comment tester vos
  applications JavaScript et ReactJS
seo_desc: 'Understanding test-driven development is an essential part of being a prolific
  software developer. Testing provides a solid platform for building reliable programs.

  This tutorial will show you all you need to implement test-driven development in
  your...'
---

Comprendre le développement piloté par les tests est une partie essentielle pour être un développeur logiciel prolifique. Les tests fournissent une plateforme solide pour construire des programmes fiables.

Ce tutoriel vous montrera tout ce dont vous avez besoin pour implémenter le développement piloté par les tests dans vos applications JavaScript et React.

## Table des matières

1. [Qu'est-ce que le développement piloté par les tests ?](#heading-installation)
2. [Exemple JavaScript d'un flux de travail de développement piloté par les tests](#heading-exemple-javascript-dun-flux-de-travail-de-developpement-pilote-par-les-tests)
3. [Comment utiliser Jest comme outil d'implémentation de tests](#heading-comment-utiliser-jest-comme-outil-dimplementation-de-tests)
4. [Choses importantes à savoir sur l'utilisation des modules ES6 avec Jest](#heading-choses-importantes-a-savoir-sur-lutilisation-des-modules-es6-avec-jest)
5. [Quels sont les avantages du développement piloté par les tests ?](#heading-quels-sont-les-avantages-du-developpement-pilote-par-les-tests)
6. [Qu'est-ce qu'un test unitaire dans le développement piloté par les tests](#heading-quest-ce-quun-test-unitaire-dans-le-developpement-pilote-par-les-tests) ?
7. [Qu'est-ce qu'un test d'intégration dans le développement piloté par les tests](#heading-quest-ce-quun-test-dintegration-dans-le-developpement-pilote-par-les-tests) ?
8. [Qu'est-ce qu'un test de bout en bout dans le développement piloté par les tests](#heading-quest-ce-quun-test-de-bout-en-bout-dans-le-developpement-pilote-par-les-tests) ?
9. [Que sont les test doubles dans le développement piloté par les tests](#heading-que-sont-les-test-doubles-dans-le-developpement-pilote-par-les-tests) ?
10. [Aperçu rapide du développement piloté par les tests jusqu'à présent](#heading-aperçu-rapide-du-developpement-pilote-par-les-tests-jusqua-present)
11. [Comment tester les composants React](#heading-comment-tester-les-composants-react)
12. [Test Runner vs. Outil de test de composants React : Quelle est la différence ?](#heading-test-runner-vs-outil-de-test-de-composants-react-quelle-est-la-difference)
13. [Projet : Comment fonctionne le test React](#heading-projet-comment-fonctionne-le-test-react)
14. [Aperçu](#heading-aperçu)

Alors, sans plus attendre, commençons par discuter de ce que signifie le développement piloté par les tests.

## Qu'est-ce que le développement piloté par les tests ?

Le **développement piloté par les tests (TDD)** est une pratique de codage où vous écrivez le résultat que vous souhaitez que votre programme produise avant de créer le programme.

En d'autres termes, le TDD vous oblige à préspécifier la sortie que votre programme prévu doit produire pour passer le test de fonctionnement de la manière dont vous l'aviez envisagé.

Ainsi, dans une pratique efficace de développement piloté par les tests, vous écriviez d'abord des tests qui expriment le résultat que vous attendez de votre programme prévu.

Ensuite, vous développiez le programme pour passer le test préécrit.

Par exemple, supposons que vous souhaitiez créer une calculatrice d'addition. Dans un tel cas, l'approche TDD serait comme suit :

![Diagramme de flux de travail du développement piloté par les tests](https://www.freecodecamp.org/news/content/images/2022/07/test-driven-development-tdd-workflow-diagram-codesweetly.png)
_Diagramme de flux de travail du développement piloté par les tests_

1. Écrivez un test spécifiant le résultat que vous attendez de la calculatrice pour produire pour passer le test d'être le programme que vous aviez en tête.
2. Développez la calculatrice pour passer le test préécrit.
3. Exécutez le test pour vérifier si la calculatrice passe ou échoue le test.
4. Refactorisez votre code de test (si nécessaire).
5. Refactorisez votre programme (si nécessaire).
6. Continuez le cycle jusqu'à ce que la calculatrice corresponde à votre vision.

Voyons maintenant un exemple JavaScript d'un flux de travail TDD.

## Exemple JavaScript d'un flux de travail de développement piloté par les tests

Les étapes ci-dessous utiliseront un simple programme JavaScript pour vous montrer comment aborder le TDD.

### 1. Écrivez votre test

Écrivez un test qui spécifie le résultat que vous attendez de votre programme de calculatrice :

```js
function additionCalculatorTester() {
  if (additionCalculator(4, 6) === 10) {
    console.log("✓ Test Passed");
  } else {
    console.error("✖ Test Failed");
  }
}
```

### 2. Développez votre programme

Développez le programme de calculatrice pour passer le test préécrit :

```js
function additionCalculator(a, b) {
  return a + b;
}
```

### 3. Exécutez le test

Exécutez le test pour vérifier si la calculatrice passe ou échoue le test :

```js
additionCalculatorTester();
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-ciui1u?devToolsHeight=33&file=index.js)

### 4. Refactorisez le test

Après avoir confirmé que votre programme a passé le test préécrit, il est temps de vérifier s'il y a besoin de le refactoriser.

Par exemple, vous pourriez refactoriser `additionCalculatorTester()` pour utiliser un [opérateur conditionnel](https://codesweetly.com/javascript-statement/#what-is-a-conditional-ternary-operator-in-javascript) comme suit :

```js
function additionCalculatorTester() {
  additionCalculator(4, 6) === 10 
    ? console.log("✓ Test Passed") 
    : console.error("✖ Test Failed");
}
```

### 5. Refactorisez le programme

Refactorisons également le code du programme pour utiliser une [fonction fléchée](https://codesweetly.com/javascript-function-object#arrow-function-expression-in-javascript).

```js
const additionCalculator = (a, b) => a + b;
```

### 6. Exécutez le test

Relancez le test pour vous assurer que votre programme fonctionne toujours comme prévu.

```js
additionCalculatorTester();
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-xp732h?devToolsHeight=33&file=index.js)

Remarquez que dans les exemples ci-dessus, nous avons implémenté le TDD sans utiliser de bibliothèques.

Mais vous pouvez également utiliser des outils puissants d'exécution de tests comme [Jasmine](https://jasmine.github.io/), [Mocha](https://mochajs.org/), [Tape](https://github.com/substack/tape), et [Jest](https://jestjs.io/), pour rendre votre implémentation de test plus rapide, plus simple et plus amusante.

Voyons comment utiliser Jest, par exemple.

## Comment utiliser Jest comme outil d'implémentation de tests

Voici les étapes que vous devrez suivre pour commencer à utiliser Jest comme votre outil d'implémentation de tests :

### Étape 1 : Obtenez la bonne version de Node et NPM

Assurez-vous d'avoir Node 10.16 (ou supérieur) et NPM 5.6 (ou supérieur) installés sur votre système.

Vous pouvez obtenir les deux en installant la dernière LTS depuis le site [Node.js](https://nodejs.org/en/).

Si vous préférez utiliser Yarn, assurez-vous d'avoir [Yarn 0.25 (ou supérieur)](https://yarnpkg.com/).

### Étape 2 : Créez un répertoire de projet

Créez un nouveau dossier pour votre projet.

```bash
mkdir addition-calculator-jest-project
```

### Étape 3 : Naviguez vers votre dossier de projet

En utilisant la ligne de commande, naviguez vers votre répertoire de projet.

```bash
cd path/to/addition-calculator-jest-project
```

### Étape 4 : Créez un fichier `package.json`

Initialisez un fichier `package.json` pour votre projet.

```bash
npm init -y
```

Ou, si votre [gestionnaire de paquets](https://codesweetly.com/package-manager-explained) est Yarn, exécutez :

```bash
yarn init -y
```

### Étape 5 : Installez Jest

Installez Jest comme un paquet de dépendance de développement comme suit :

```bash
npm install jest --save-dev
```

Alternativement, si votre gestionnaire de paquets est Yarn, exécutez :

```bash
yarn add jest --dev
```

### Étape 6 : Faites de Jest l'outil d'exécution de tests de votre projet

Ouvrez votre fichier `package.json` et ajoutez Jest au champ `test`.

```json
{
  "scripts": {
    "test": "jest"
  }
}
```

### Étape 7 : Créez votre fichier de projet

Créez un fichier que vous utiliserez pour développer votre programme.

```bash
touch additionCalculator.js
```

### Étape 8 : Créez votre fichier de test

Créez un fichier que vous utiliserez pour écrire vos cas de test.

```bash
touch additionCalculator.test.js
```

**Note :** Le nom de votre fichier de test doit se terminer par `.test.js` afin que Jest puisse le reconnaître comme le fichier contenant votre code de test.

### Étape 9 : Écrivez votre cas de test

Ouvrez votre fichier de test et écrivez du code de test qui spécifie le résultat que vous attendez de votre programme.

**Voici un exemple :**

```js
// additionCalculator.test.js

const additionCalculator = require("./additionCalculator");

test("addition of 4 and 6 to equal 10", () => {
  expect(additionCalculator(4, 6)).toBe(10);
});
```

Voici ce que nous avons fait dans l'extrait ci-dessus :

1. Nous avons importé le fichier de projet `additionCalculator.js` dans le fichier de test `additionCalculator.test.js`.
2. Nous avons écrit un cas de test spécifiant que nous attendons du programme `additionCalculator()` qu'il produise `10` chaque fois que les utilisateurs fournissent `4` et `6` comme [arguments](https://codesweetly.com/javascript-arguments).

**Note :**

- [`test()`](https://jestjs.io/docs/api#testname-fn-timeout) est l'une des méthodes globales de Jest. Elle accepte trois arguments :
  1. Le nom du test (`"addition of 4 and 6 to equal 10"`).
  2. Une fonction contenant les attentes que vous souhaitez tester.
  3. Un argument de délai d'attente facultatif.
- [`expect()`](https://jestjs.io/docs/expect#expectvalue) est une méthode Jest qui vous permet de tester la sortie de votre code.
- [`toBe()`](https://jestjs.io/docs/expect#tobevalue) est une fonction [Jest matcher](https://jestjs.io/docs/using-matchers) qui vous permet de comparer l'argument de `expect()` avec des valeurs primitives.

Supposons que vous exécutiez le code de test maintenant. Le test échouerait parce que vous n'avez pas développé le programme pour lequel vous avez créé le test. Alors, faisons cela maintenant.

### Étape 10 : Développez votre programme

Ouvrez votre fichier de projet et développez un programme pour passer le test préécrit.

**Voici un exemple :**

```js
// additionCalculator.js

function additionCalculator(a, b) {
  return a + b;
}

module.exports = additionCalculator;
```

L'extrait ci-dessus a créé un programme `additionCalculator()` et l'a exporté avec l'instruction `module.exports`.

### Étape 11 : Exécutez le test

Exécutez le test préécrit pour vérifier si votre programme a passé ou échoué.

```bash
npm run test
```

Alternativement, vous pouvez utiliser Yarn comme suit :

```bash
yarn test
```

Supposons que votre projet contient plusieurs fichiers de test et que vous souhaitez en exécuter un spécifique. Dans un tel cas, spécifiez le fichier de test comme suit :

```bash
npm run test additionCalculator.test.js
```

Alternativement, vous pouvez utiliser Yarn comme ceci :

```bash
yarn test additionCalculator.test.js
```

Une fois que vous avez initié le test, Jest imprimera un message de réussite ou d'échec sur la console de votre éditeur. Le message ressemblera à ceci :

```bash
$ jest
 PASS  ./additionCalculator.test.js
  √ addition of 4 and 6 to equal 10 (2 ms)

Test Suites: 1 passed, 1 total
Tests:       1 passed, 1 total
Snapshots:   0 total
Time:        2.002 s
Ran all test suites.
Done in 7.80s.
```

Si vous préférez que Jest exécute votre test automatiquement, ajoutez l'option `--watchAll` au champ `test` de votre `package.json`.

**Voici un exemple :**

```json
{
  "scripts": {
    "test": "jest --watchAll"
  }
}
```

Après avoir ajouté `--watchAll`, réexécutez la commande `npm run test` (ou `yarn test`) pour faire en sorte que Jest commence automatiquement à réexécuter votre test chaque fois que vous enregistrez des modifications.

**Note :** Vous pouvez quitter le mode watch en appuyant sur la touche **Q** de votre clavier.

### Étape 12 : Refactorisez le code de test

Maintenant que vous avez confirmé que votre programme fonctionne comme prévu, il est temps de vérifier s'il y a besoin de refactoriser le code de test.

Par exemple, supposons que vous avez réalisé que `additionalCalculator` devrait permettre aux utilisateurs d'additionner n'importe quel nombre de chiffres. Dans ce cas, vous pouvez refactoriser votre code de test comme suit :

```js
// additionCalculator.test.js

const additionCalculator = require("./additionCalculator");

describe("additionCalculator's test cases", () => {
  test("addition of 4 and 6 to equal 10", () => {
    expect(additionCalculator(4, 6)).toBe(10);
  });

  test("addition of 100, 50, 20, 45 and 30 to equal 245", () => {
    expect(additionCalculator(100, 50, 20, 45, 30)).toBe(245);
  });

  test("addition of 7 to equal 7", () => {
    expect(additionCalculator(7)).toBe(7);
  });

  test("addition of no argument provided to equal 0", () => {
    expect(additionCalculator()).toBe(0);
  });
});
```

Notez que la méthode [describe()](https://jestjs.io/docs/api#describename-fn) que nous avons utilisée dans l'extrait ci-dessus est un code facultatif—il aide à organiser les cas de test liés en groupes.

`describe()` accepte deux arguments :

1. Un nom que vous souhaitez donner au groupe de cas de test—par exemple, `"additionCalculator's test cases"`.
2. Une fonction contenant vos cas de test.

### Étape 13 : Refactorisez le programme

Maintenant que vous avez refactorisé votre code de test, faisons de même pour le programme `additionalCalculator`.

```js
// additionCalculator.js

function additionCalculator(...numbers) {
  return numbers.reduce((sum, item) => sum + item, 0);
}

module.exports = additionCalculator;
```

Voici ce que nous avons fait dans l'extrait ci-dessus :

1. Le code `...numbers` a utilisé l'opérateur de repos (`...`) de JavaScript pour mettre les arguments de la fonction dans un tableau.
2. Le code `numbers.reduce((sum, item) => sum + item, 0)` a utilisé la méthode [reduce()](https://codesweetly.com/javascript-reduce-method) de JavaScript pour additionner tous les éléments du tableau `numbers`.

### Étape 14 : Relancez le test

Une fois que vous avez terminé de refactoriser votre code, relancez le test pour confirmer que votre programme fonctionne toujours comme prévu.

### Et c'est tout !

Félicitations ! Vous avez utilisé avec succès Jest pour développer un programme de calculatrice d'addition en utilisant une approche de développement piloté par les tests ! 🎉

## Choses importantes à savoir sur l'utilisation des modules ES6 avec Jest

Jest ne reconnaît pas actuellement les modules ES6.

Cependant, supposons que vous préférez utiliser les instructions d'import/export d'ES6. Dans ce cas, faites ce qui suit :

### 1. Installez Babel comme dépendance de développement

```bash
npm install @babel/preset-env --save-dev
```

Ou, vous pouvez utiliser Yarn :

```bash
yarn add @babel/preset-env --dev
```

### 2. Créez un fichier `.babelrc` à la racine de votre projet

```bash
touch .babelrc
```

### 3. Ouvrez le fichier `.babelrc` et reproduisez le code ci-dessous

```json
{ "presets": ["@babel/preset-env"] }
```

La configuration ci-dessus vous permettra maintenant de changer l'instruction `require()` de l'étape 9 de ceci :

```js
const additionCalculator = require("./additionCalculator");
```

...en ceci :

```js
import additionCalculator from "./additionCalculator";
```

De même, vous pouvez maintenant également substituer l'instruction `export` de l'étape 10 de ceci :

```js
module.exports = additionCalculator;
```

...en ceci :

```js
export default additionCalculator;
```

**Note :** Jest a également spécifié des instructions similaires dans leur documentation [utilisation de Babel](https://jestjs.io/docs/getting-started#using-babel).

### 4. Relancez le test

Vous pouvez maintenant relancer le test pour confirmer que votre programme fonctionne toujours !

Maintenant que nous savons ce qu'est le développement piloté par les tests, nous pouvons discuter de ses avantages.

## Quels sont les avantages du développement piloté par les tests ?

Voici deux principaux avantages de l'adoption du développement piloté par les tests (TDD) dans votre flux de travail de programmation.

### 1. Comprendre le but de votre programme

Le développement piloté par les tests vous aide à comprendre les objectifs de votre programme.

En d'autres termes, puisque vous écrivez votre test avant le programme réel, le TDD vous fait réfléchir à ce que vous voulez que votre programme fasse.

Ensuite, après avoir documenté les objectifs du programme à l'aide d'un ou plusieurs tests, vous pouvez procéder en toute confiance à la création du programme.

Par conséquent, le TDD est un moyen utile de noter les résultats spécifiques que vous attendez de votre programme prévu.

### 2. Renforce la confiance

Le TDD est une référence pour savoir que votre programme fonctionne comme prévu. Il vous donne la confiance que votre programme fonctionne correctement.

Par conséquent, indépendamment de tout développement futur sur votre base de code, le TDD fournit un moyen efficace de tester si votre programme fonctionne toujours de manière appropriée.

Discutons maintenant de quelques termes populaires du TDD : "test unitaire", "test d'intégration", "E2E" et "test doubles".

## Qu'est-ce qu'un test unitaire dans le développement piloté par les tests ?

Un **test unitaire** est un test que vous écrivez pour évaluer la fonctionnalité d'une partie indépendante d'un programme. En d'autres termes, un test unitaire vérifie si une unité de programme entièrement isolée fonctionne comme prévu.

Le test que nous avons écrit pour le programme `additionalCalculator` de l'étape 10 est un excellent exemple de test unitaire.

Le test de `additionalCalculator()` de l'étape 10 est un test unitaire parce que le programme est une fonction indépendante qui ne dépend d'aucun code externe.

Notez que le but principal d'un test unitaire n'est pas de vérifier les bugs. Au lieu de cela, le but principal d'un test unitaire est de vérifier si une partie indépendante d'un programme (appelée unité) se comporte comme prévu sous divers cas de test.

## Qu'est-ce qu'un test d'intégration dans le développement piloté par les tests ?

Un **test d'intégration** évalue la fonctionnalité d'une partie dépendante d'un programme. En d'autres termes, un test d'intégration vérifie si un programme—qui dépend d'un autre code—fonctionne comme prévu.

Le test que nous avons écrit pour le programme `additionalCalculator` de l'étape 13 est un excellent exemple de test d'intégration.

Le test de `additionalCalculator()` de l'étape 13 est un test d'intégration parce que le programme est une fonction dépendante qui dépend de la méthode [reduce()](https://codesweetly.com/javascript-reduce-method) de JavaScript.

En d'autres termes, nous avons utilisé le cas de test préécrit pour évaluer l'intégration de `additionalCalculator()` et `reduce()`.

Par conséquent, supposons que JavaScript rende la méthode `reduce()` obsolète. Dans un tel cas, `additionalCalculator` échouera son test à cause de la méthode `reduce()`.

## Qu'est-ce qu'un test de bout en bout dans le développement piloté par les tests ?

Un **test de bout en bout (E2E)** évalue la fonctionnalité d'une interface utilisateur. En d'autres termes, E2E vérifie si votre interface utilisateur fonctionne comme prévu.

Regardez la [vidéo YouTube de Max](https://youtu.be/r9HdJ8P6GQI?t=1755) pour une bonne illustration d'un test de bout en bout.

## Que sont les test doubles dans le développement piloté par les tests ?

Les **test doubles** sont des objets d'imitation utilisés pour imiter des dépendances réelles comme les bases de données, les bibliothèques, les réseaux et les API.

Un test double vous permet de contourner les objets naturels dont dépend votre programme. Ils vous permettent de tester votre code indépendamment de toute dépendance.

Par exemple, supposons que vous devez vérifier si une erreur détectée dans votre application provient d'une API externe ou de votre code.

Mais supposons que le service de l'API est disponible uniquement en production—pas dans l'environnement de développement. Dans ce cas, vous avez deux options :

1. Attendre que votre application soit mise en ligne—ce qui pourrait prendre des mois.
2. Cloner l'API afin de pouvoir continuer votre test indépendamment de la disponibilité de la dépendance.

Les test doubles fournissent un moyen utile de cloner les dépendances de votre programme afin que vos activités de test ne rencontrent aucune perturbation.

Des exemples typiques de test doubles sont les objets factices, les mocks, les fakes et les stubs. Discutons-en ci-dessous.

### Qu'est-ce qu'un dummy dans le développement piloté par les tests ?

Un **dummy** est un test double utilisé pour imiter la valeur d'une dépendance spécifique.

Par exemple, supposons que votre application dépend d'une méthode tierce qui vous oblige à fournir certains arguments. Dans un tel cas, un dummy vous permet de passer des valeurs fictives aux paramètres de cette méthode.

### Qu'est-ce qu'un mock dans le développement piloté par les tests ?

**Mock** est un test double utilisé pour imiter une dépendance externe sans tenir compte des réponses que la dépendance peut retourner.

Par exemple, supposons que votre application dépend d'une API tierce (par exemple, Facebook)—que vous ne pouvez pas accéder en mode développement. Mock vous permet de contourner l'API afin que vous puissiez vous concentrer sur le test de votre code indépendamment de la disponibilité de l'API Facebook.

### Qu'est-ce qu'un stub dans le développement piloté par les tests ?

Un **stub** est un test double utilisé pour imiter une dépendance externe tout en retournant des valeurs codées à la main. Vous pouvez utiliser la valeur retournée pour évaluer le comportement de votre programme avec diverses réponses de cas de test de la dépendance.

Par exemple, supposons que votre application dépend d'une API tierce (par exemple, Facebook)—que vous ne pouvez pas accéder en mode développement. Stub vous permet de contourner l'API tout en imitant les valeurs exactes que Facebook retournera.

Par conséquent, stub vous aide à évaluer le comportement de votre programme avec divers scénarios de réponse.

### Qu'est-ce qu'un fake dans le développement piloté par les tests ?

**Fake** est un test double utilisé pour créer une implémentation de test fonctionnelle d'une dépendance externe avec des valeurs dynamiques.

Par exemple, vous pouvez utiliser fake pour créer une base de données locale qui vous permet de tester comment une base de données réelle fonctionnera avec votre programme.

## Aperçu rapide du développement piloté par les tests jusqu'à présent

Nous avons appris que le développement piloté par les tests vous aide à noter le comportement de votre programme avant de créer le programme.

Nous avons également vu un simple test JavaScript et utilisé Jest comme outil d'implémentation de tests.

Voyons maintenant comment tester les composants React.

## Comment tester les composants React

Les deux principaux outils dont vous avez besoin pour tester vos composants React sont :

1. Un outil d'exécution de tests
2. Un outil de test de composants React

Mais quelle est exactement la différence entre un test runner et un outil de test de composants React ? Découvrons-le.

## Test Runner vs. Outil de test de composants React : Quelle est la différence ?

Voici les différences entre un test runner et un outil de test de composants React.

### Qu'est-ce qu'un test runner ?

Un **test runner** est un outil que les développeurs utilisent pour exécuter un script de test et imprimer les résultats du test sur la ligne de commande (CLI).

Par exemple, supposons que vous souhaitiez exécuter les cas de test dans le script de test `App.test.js` de votre projet. Dans un tel cas, vous utiliserez un test runner.

Le test runner exécutera `App.test.js` et imprimera les résultats du test sur la ligne de commande.

Des exemples typiques de test runners sont [Jasmine](https://jasmine.github.io/), [Mocha](https://mochajs.org/), [Tape](https://github.com/substack/tape), et [Jest](https://jestjs.io/).

### Qu'est-ce qu'un outil de test de composants React ?

Un **outil de test de composants React** fournit des API utiles pour définir les cas de test d'un composant.

Par exemple, supposons que vous devez tester le composant `<App />` de votre projet. Dans un tel cas, vous utiliserez un outil de test de composants React pour définir les cas de test du composant.

En d'autres termes, un outil de test de composants React fournit les API pour écrire les cas de test de votre composant.

Des exemples typiques sont [Enzyme](https://enzymejs.github.io/enzyme/) et la [React Testing Library](https://testing-library.com/docs/react-testing-library/intro).

Maintenant que nous savons ce qu'est un test runner et un outil de test de composants React, utilisons un mini-projet pour comprendre comment fonctionne le test React.

## Projet : Comment fonctionne le test React

Dans les étapes suivantes, nous utiliserons [Jest](https://en.wikipedia.org/wiki/Jest_(JavaScript_framework)) et la [React Testing Library](https://testing-library.com/docs/react-testing-library/intro) (par Kent C. Dodds) pour apprendre comment fonctionne le test React.

**Note :** La documentation officielle de React [recommande](https://reactjs.org/docs/testing.html#tools) la combinaison Jest et React Testing Library pour tester les composants React.

### Étape 1 : Obtenez la bonne version de Node et NPM

Assurez-vous d'avoir [Node 10.16](https://codesweetly.com/package-manager-explained#how-to-check-the-installed-node-version) (ou supérieur) et NPM 5.6 (ou supérieur) installés sur votre système.

Si vous préférez utiliser Yarn, assurez-vous d'avoir Yarn 0.25 (ou supérieur).

### Étape 2 : Créez une nouvelle application React

Utilisez le package [create-react-app](https://create-react-app.dev/) de NPM pour créer une nouvelle application React appelée `react-testing-project`.

```bash
npx create-react-app react-testing-project
```

Alternativement, vous pouvez utiliser Yarn pour configurer votre projet comme suit :

```bash
yarn create react-app react-testing-project
```

### Étape 3 : Allez dans le répertoire du projet

Après le processus d'installation, naviguez dans le répertoire du projet comme suit :

```bash
cd react-testing-project
```

### Étape 4 : Configurez votre environnement de test

Installez les packages de test suivants :

* jest
* @testing-library/react
* @testing-library/jest-dom
* @testing-library/user-event

**Note :** Si vous avez initialisé votre projet React avec `create-react-app` (étape 2), vous n'avez pas besoin d'installer aucun des packages ci-dessus. Ils sont préinstallés et préconfigurés dans votre fichier `package.json`.

Maintenant, discutons de l'objectif de chacun des packages de test ci-dessus.

#### Qu'est-ce que Jest ?

[jest](https://www.npmjs.com/package/jest) est l'outil d'exécution de tests que nous utiliserons pour exécuter les scripts de test de ce projet et imprimer les résultats des tests sur la ligne de commande.

#### Qu'est-ce que @testing-library/react ?

[@testing-library/react](https://www.npmjs.com/package/@testing-library/react) est la React Testing Library qui vous donne les API dont vous avez besoin pour écrire des cas de test pour vos composants React.

#### Qu'est-ce que @testing-library/jest-dom ?

[@testing-library/jest-dom](https://www.npmjs.com/package/@testing-library/jest-dom) fournit un ensemble de matchers Jest personnalisés pour tester l'état du DOM.

**Note :** Jest vient déjà avec de nombreux matchers, donc l'utilisation de `jest-dom` est facultative. `jest-dom` étend simplement Jest en fournissant des matchers qui rendent votre test plus déclaratif, clair à lire et facile à maintenir.

#### Qu'est-ce que @testing-library/user-event ?

[@testing-library/user-event](https://www.npmjs.com/package/@testing-library/user-event) fournit l'API `userEvent` pour simuler l'interaction des utilisateurs avec votre application sur une page web.

**Note :** `@testing-library/user-event` est une meilleure alternative à l'API [fireEvent](https://testing-library.com/docs/dom-testing-library/api-events/#fireevent).

### Étape 5 : Nettoyez le dossier `src`

Supprimez tous les fichiers à l'intérieur du dossier `src` du répertoire du projet.

### Étape 6 : Créez vos fichiers de code

Créez les fichiers suivants à l'intérieur du dossier `src` de votre projet.

* `index.js`
* `App.js`
* `App.test.js`

### Étape 7 : Rendez le composant `App`

Ouvrez votre fichier `index.js` et rendez le composant `App` dans le DOM comme suit :

```js
// index.js

import React from "react";
import { createRoot } from "react-dom/client";
import App from "./App";

// Rendre le composant App dans le DOM racine
createRoot(document.getElementById("root")).render(<App />);
```

### Étape 8 : Écrivez votre cas de test

Supposons que vous souhaitez que votre fichier `App.js` rende un élément `<h1>CodeSweetly Test</h1>` sur la page web. Dans ce cas, ouvrez votre _script de test_ et écrivez du code de test spécifiant le résultat que vous attendez de votre composant `<App />`.

**Voici un exemple :**

```js
// App.test.js

import React from "react";
import { render, screen } from "@testing-library/react";
import "@testing-library/jest-dom";
import App from "./App";

test("codesweetly test heading", () => {
  render(<App />);
  expect(screen.getByRole("heading")).toHaveTextContent(/codesweetly test/i);
});
```

Voici les principales choses que nous avons faites dans l'extrait de test ci-dessus :

1. Nous avons importé les packages nécessaires pour écrire notre cas de test.
2. Nous avons écrit un cas de test spécifiant que nous attendons de notre composant `<App />` qu'il rende un élément d'en-tête avec un texte `"codesweetly test"`.

- [`test()`](https://jestjs.io/docs/api#testname-fn-timeout) est l'une des méthodes globales de Jest. Nous l'utilisons pour exécuter un cas de test. La méthode accepte trois arguments :
  - Le nom du test (`"codesweetly test heading"`)
  - Une fonction contenant les attentes que vous souhaitez tester
  - Un argument de délai d'attente facultatif
- [`render()`](https://testing-library.com/docs/react-testing-library/api/#render) est l'une des API de la React Testing Library. Nous l'utilisons pour rendre le composant que nous souhaitons tester.
- [`expect()`](https://jestjs.io/docs/expect#expectvalue) est une méthode Jest qui vous permet de tester la sortie de votre code.
- [`screen`](https://testing-library.com/docs/queries/about/#screen) est un objet de la React Testing Library contenant de nombreuses méthodes pour trouver des éléments sur une page.
- [`getByRole()`](https://testing-library.com/docs/queries/about/#priority) est l'une des méthodes de requête de la React Testing Library pour trouver des éléments sur une page.
- [`toHaveTextContent()`](https://github.com/testing-library/jest-dom#tohavetextcontent) est l'un des matchers personnalisés de `jest-dom` que vous pouvez utiliser pour confirmer la présence d'un contenu textuel dans un nœud spécifique.
- `/codesweetly test/i` est une syntaxe d'[expression régulière](https://codesweetly.com/javascript-regular-expression-object) que nous avons utilisée pour spécifier une recherche insensible à la casse pour `codesweetly test`.

Gardez à l'esprit qu'il existe trois autres façons d'écrire l'instruction expect ci-dessus :

```js
// 1. En utilisant la méthode toHaveTextContent() de jest-dom :
expect(screen.getByRole("heading")).toHaveTextContent(/codesweetly test/i);

// 2. En utilisant la propriété textContent de l'en-tête et la méthode toMatch() de Jest :
expect(screen.getByRole("heading").textContent).toMatch(/codesweetly test/i);

// 3. En utilisant l'option name de React Testing Library et la méthode toBeInTheDocument() de jest-dom
expect(screen.getByRole("heading", { name: /codesweetly test/i })).toBeInTheDocument();
```

**Astuce :**

Ajoutez une option `level` à la méthode `getByRole()` pour spécifier le niveau de votre en-tête.

**Voici un exemple :**

```js
test("codesweetly test heading", () => {
  render(<App />);
  expect(screen.getByRole("heading", { level: 1 })).toHaveTextContent(/codesweetly test/i);
});
```

L'option `level: 1` spécifie un élément d'en-tête `<h1>`.

Supposons que vous exécutiez le code de test maintenant. Le test échouera parce que vous n'avez pas développé le composant pour lequel vous avez créé le test. Alors, faisons cela maintenant.

### Étape 9 : Développez votre composant React

Ouvrez votre fichier `App.js` et développez le composant pour passer le test préécrit.

**Voici un exemple :**

```js
// App.js

import React from "react";

const App = () => <h1>CodeSweetly Test</h1>;

export default App;
```

Le composant `App`, dans l'extrait ci-dessus, rend un élément `<h1>` contenant le texte `"CodeSweetly Test"`.

### Étape 10 : Exécutez le test

Exécutez le test préécrit pour vérifier si votre programme a passé ou échoué.

```bash
npm test App.test.js
```

Alternativement, vous pouvez utiliser Yarn comme suit :

```bash
yarn test App.test.js
```

Une fois que vous avez initié le test, Jest imprimera un message de réussite ou d'échec sur la console de votre éditeur. Le message ressemblera à ceci :

```bash
$ jest
 PASS  src/App.test.js
  √ codesweetly test heading (59 ms)

Test Suites: 1 passed, 1 total
Tests:       1 passed, 1 total
Snapshots:   0 total
Time:        3.146 s
Ran all test suites related to changed files.
```

**Note :** Le `create-react-app` a configuré Jest en [mode watch](https://codesweetly.com/javascript-module-bundler/#what-is-webpack---progress---watch) par défaut. Par conséquent, après avoir exécuté `npm test` (ou `yarn test`), votre terminal actuellement ouvert continuera à traiter les activités de la commande `test`. Vous ne pourrez donc pas entrer de commande sur ce terminal jusqu'à ce que vous arrêtiez l'exécution de `test`. Mais vous pouvez ouvrir une nouvelle fenêtre de terminal simultanément avec celle qui traite `test`.

En d'autres termes, utilisez un terminal pour exécuter `test` et un autre pour entrer des commandes.

### Étape 11 : Exécutez l'application

Jetez un coup d'œil à votre application dans le navigateur en exécutant :

```bash
npm start
```

Ou, si votre [gestionnaire de paquets](https://codesweetly.com/package-manager-explained) est Yarn, exécutez :

```bash
yarn start
```

Une fois que vous avez exécuté la commande ci-dessus, votre application s'ouvrira automatiquement sur votre navigateur par défaut.

### Étape 12 : Refactorisez le code de test

Supposons que vous souhaitiez changer le texte de l'en-tête lorsque les utilisateurs cliquent sur un bouton. Dans ce cas, vous pouvez simuler l'interaction des utilisateurs avec le bouton pour confirmer qu'il fonctionne comme prévu.

**Voici un exemple :**

```js
// App.test.js

import React from "react";
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import "@testing-library/jest-dom";
import App from "./App";

describe("App component", () => {
  test("codesweetly test heading", () => {
    render(<App />);
    expect(screen.getByRole("heading")).toHaveTextContent(/codesweetly test/i);
  });

  test("a codesweetly project heading", () => {
    render(<App />);

    const button = screen.getByRole("button", { name: "Update Heading" });

    userEvent.click(button);

    expect(screen.getByRole("heading")).toHaveTextContent(/a codesweetly project/i);
  });
});
```

Voici les principales choses que nous avons faites dans l'extrait de test ci-dessus :

1. Nous avons importé les packages nécessaires pour écrire notre cas de test.
2. Nous avons écrit un cas de test spécifiant que nous attendons du composant `<App />` qu'il rende un élément d'en-tête avec un texte `"codesweetly test"`.
3. Nous avons écrit un autre cas de test simulant l'interaction des utilisateurs avec le bouton de l'application. En d'autres termes, nous avons spécifié que chaque fois qu'un utilisateur clique sur le bouton, nous attendons que l'en-tête de `<App />` se mette à jour avec le texte `"a codesweetly project"`.

**Note :**

- [`describe()`](https://jestjs.io/docs/api#describename-fn) est l'une des méthodes globales de Jest. C'est un code facultatif qui aide à organiser les cas de test liés en groupes. `describe()` accepte deux arguments :
  - Un nom que vous souhaitez donner au groupe de cas de test—par exemple, `"App component"`.
  - Une fonction contenant vos cas de test.
- [`userEvent`](https://www.npmjs.com/package/@testing-library/user-event) est le package de la React Testing Library contenant plusieurs méthodes pour simuler l'interaction des utilisateurs avec une application. Par exemple, dans l'extrait ci-dessus, nous avons utilisé la méthode `click()` de `userEvent` pour simuler un événement de clic sur l'élément bouton.
- Nous avons rendu `<App />` pour chaque cas de test parce que la React Testing Library démonte les composants rendus après chaque test. Cependant, supposons que vous avez de nombreux cas de test pour un composant. Dans ce cas, utilisez la méthode [`beforeEach()`](https://jestjs.io/docs/api#beforeeachfn-timeout) de Jest pour exécuter `render(<App />)` avant chaque test dans votre fichier (ou bloc `describe`).

### Étape 13 : Refactorisez votre composant React

Maintenant que vous avez refactorisé votre code de test, faisons de même pour le composant `App`.

```js
// App.js

import React, { useState } from "react";

const App = () => {
  const [heading, setHeading] = useState("CodeSweetly Test");

  const handleClick = () => {
    setHeading("A CodeSweetly Project");
  };

  return (
    <>
      <h1>{heading}</h1>
      <button type="button" onClick={handleClick}>
        Update Heading
      </button>
    </>
  );
};

export default App;
```

Voici les principales choses que nous avons faites dans l'extrait ci-dessus :

1. L'état `heading` de `App` a été initialisé avec une chaîne `"CodeSweetly Test"`.
2. Nous avons programmé une fonction `handleClick` pour mettre à jour l'état `heading`.
3. Nous avons rendu des éléments `<h1>` et `<button>` dans le DOM.

Notez ce qui suit :

* Le contenu de `<h1>` est la valeur actuelle de l'état `heading`.
* Chaque fois qu'un utilisateur clique sur l'élément bouton, l'écouteur d'événement `onClick()` déclenchera la fonction `handleClick()`. Et `handleClick` mettra à jour l'état `heading` de `App` en `"A CodeSweetly Project"`. Par conséquent, le contenu de `<h1>` changera en `"A CodeSweetly Project"`.

### Étape 14 : Relancez le test

Une fois que vous avez refactorisé votre composant, relancez le test (ou vérifiez le test en cours d'exécution) pour confirmer que votre application fonctionne toujours comme prévu.

Ensuite, vérifiez le navigateur pour voir vos mises à jour récentes.

### Et c'est tout !

Félicitations ! Vous avez utilisé avec succès Jest et la React Testing Library pour tester un composant React. 🎉

## Aperçu

Cet article a discuté de la manière dont le développement piloté par les tests fonctionne dans les applications JavaScript et ReactJS.

Nous avons également appris comment utiliser Jest et la React Testing Library pour rendre les tests plus simples et plus rapides.

Merci d'avoir lu !

### **Et voici une ressource utile sur ReactJS :**

J'ai écrit un livre sur React !

* Il est adapté aux débutants ✓
* Il contient des extraits de code en direct ✓
* Il contient des projets évolutifs ✓
* Il contient de nombreux exemples faciles à comprendre ✓

Le livre [React Explained Clearly](https://www.amazon.com/dp/B09KYGDQYW) est tout ce dont vous avez besoin pour comprendre ReactJS.

[![Livre React Explained Clearly Disponible Maintenant sur Amazon](https://www.freecodecamp.org/news/content/images/2022/01/Twitter-React_Explained_Clearly-CodeSweetly-Oluwatobi_Sofela.jpg)](https://www.amazon.com/dp/B09KYGDQYW)