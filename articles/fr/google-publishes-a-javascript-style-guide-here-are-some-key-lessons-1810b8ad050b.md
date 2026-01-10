---
title: 13 points notables du guide de style JavaScript de Google
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-27T12:35:22.000Z'
originalURL: https://freecodecamp.org/news/google-publishes-a-javascript-style-guide-here-are-some-key-lessons-1810b8ad050b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ouYvMzYuksK-IH1BPNKD0A.jpeg
tags:
- name: Google
  slug: google
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 13 points notables du guide de style JavaScript de Google
seo_desc: 'By Daniel Simmons

  For anyone who isn’t already familiar with it, Google puts out a style guide for
  writing JavaScript that lays out (what Google believes to be) the best stylistic
  practices for writing clean, understandable code.

  These are not hard a...'
---

Par Daniel Simmons

Pour ceux qui ne le connaissent pas déjà, [Google publie un guide de style](https://google.github.io/styleguide/jsguide.html) pour écrire du JavaScript qui expose (ce que Google considère comme) les meilleures pratiques stylistiques pour écrire du code propre et compréhensible.

Il ne s'agit pas de règles strictes pour écrire du JavaScript valide, mais seulement de prescriptions pour maintenir des choix de style cohérents et attrayants dans vos fichiers sources. Cela est particulièrement intéressant pour JavaScript, qui est un langage flexible et tolérant permettant une grande variété de choix stylistiques.

Google et [Airbnb](https://github.com/airbnb/javascript) ont deux des guides de style les plus populaires. Je vous recommande définitivement de consulter les deux si vous passez beaucoup de temps à écrire du JS.

Voici treize règles que je considère comme les plus intéressantes et pertinentes du guide de style JS de Google.

Elles traitent de tout, depuis des questions très débattues (tabulations contre espaces, et l'utilisation controversée des points-virgules), jusqu'à des spécifications plus obscures qui m'ont surpris. Elles vont définitivement changer la façon dont j'écris mon JS à l'avenir.

Pour chaque règle, je donnerai un résumé de la spécification, suivi d'une citation du guide de style qui décrit la règle en détail. Lorsque cela est applicable, je fournirai également un exemple du style en pratique, et le contrasterai avec du code qui ne suit pas la règle.

#### Utilisez des espaces, pas des tabulations

> À part la séquence de fin de ligne, le caractère d'espace horizontal ASCII (0x20) est le seul caractère d'espacement qui apparaît quelque part dans un fichier source. Cela implique que... Les caractères de tabulation ne sont **pas** utilisés pour l'indentation.

Le guide spécifie plus tard que vous devez utiliser deux espaces (pas quatre) pour l'indentation.

```
// mauvaisfunction foo() {				let name;}// mauvaisfunction bar() {	let name;}// bonfunction baz() {		let name;}
```

#### Les points-virgules SONT obligatoires

> Chaque instruction doit être terminée par un point-virgule. Se fier à l'insertion automatique de points-virgules est interdit.

Bien que je ne puisse imaginer pourquoi quelqu'un s'opposerait à cette idée, l'utilisation cohérente des points-virgules en JS devient le nouveau débat "espaces contre tabulations". Google se positionne fermement ici en défense du point-virgule.

```
// mauvaislet luke = {}let leia = {}[luke, leia].forEach(jedi => jedi.father = 'vader')
```

```
// bonlet luke = {};let leia = {};[luke, leia].forEach((jedi) => {  jedi.father = 'vader';});
```

#### N'utilisez pas encore les modules ES6

> N'utilisez pas encore les modules ES6 (c'est-à-dire les mots-clés `export` et `import`), car leur sémantique n'est pas encore finalisée. Notez que cette politique sera réexaminée une fois la sémantique entièrement standardisée.

```
// Ne faites pas encore ce genre de chose :
```

```
//------ lib.js ------export function square(x) {    return x * x;}export function diag(x, y) {    return sqrt(square(x) + square(y));}//------ main.js ------import { square, diag } from 'lib';
```

#### L'alignement horizontal est déconseillé (mais pas interdit)

> Cette pratique est autorisée, mais elle est **généralement déconseillée** par le style Google. Il n'est même pas nécessaire de _maintenir_ l'alignement horizontal dans les endroits où il était déjà utilisé.

L'alignement horizontal est la pratique consistant à ajouter un nombre variable d'espaces supplémentaires dans votre code, pour faire apparaître certains jetons directement sous certains autres jetons sur les lignes précédentes.

```
// mauvais{  tiny:   42,    longer: 435, };
```

```
// bon{  tiny: 42,   longer: 435,};
```

#### N'utilisez plus var

> Déclarez toutes les variables locales avec soit `const` soit `let`. Utilisez const par défaut, sauf si une variable doit être réassignée. Le mot-clé `var` ne doit pas être utilisé.

Je vois encore des gens utiliser `var` dans des exemples de code sur StackOverflow et ailleurs. Je ne sais pas s'il y a des gens qui feront un plaidoyer pour cela, ou si c'est juste une question de vieilles habitudes qui ont la vie dure.

```
// mauvaisvar example = 42;
```

```
// bonlet example = 42;
```

#### Les fonctions fléchées sont préférées

> Les fonctions fléchées fournissent une syntaxe concise et résolvent un certain nombre de difficultés avec `this`. Préférez les fonctions fléchées au mot-clé `function`, en particulier pour les fonctions imbriquées.

Je vais être honnête, je pensais que les fonctions fléchées étaient géniales simplement parce qu'elles étaient plus concises et plus agréables à regarder. Il s'avère qu'elles servent également un but assez important.

```
// mauvais[1, 2, 3].map(function (x) {  const y = x + 1;  return x * y;});// bon[1, 2, 3].map((x) => {  const y = x + 1;  return x * y;});
```

#### Utilisez les chaînes de caractères template au lieu de la concaténation

> Utilisez les chaînes de caractères template (délimitées avec ``) plutôt que la concaténation complexe de chaînes, en particulier si plusieurs littéraux de chaîne sont impliqués. Les chaînes de caractères template peuvent s'étendre sur plusieurs lignes.

```
// mauvaisfunction sayHi(name) {  return 'How are you, ' + name + '?';}// mauvaisfunction sayHi(name) {  return ['How are you, ', name, '?'].join();}// mauvaisfunction sayHi(name) {  return `How are you, ${ name }?`;}// bonfunction sayHi(name) {  return `How are you, ${name}?`;}
```

#### **Ne pas utiliser de continuation de ligne pour les longues chaînes**

> Ne pas utiliser de _continuations de ligne_ (c'est-à-dire, terminer une ligne à l'intérieur d'un littéral de chaîne avec un antislash) dans les littéraux de chaîne ordinaires ou template. Même si ES5 permet cela, cela peut conduire à des erreurs délicates si un espace de fin vient après le slash, et est moins évident pour les lecteurs.

Intéressamment, c'est une règle sur laquelle Google et Airbnb ne sont pas d'accord (voici [la spécification d'Airbnb](https://github.com/airbnb/javascript#strings--line-length)).

Alors que Google recommande de concaténer les chaînes plus longues (comme montré ci-dessous), le guide de style d'Airbnb recommande essentiellement de ne rien faire, et de permettre aux longues chaînes de continuer aussi longtemps qu'elles en ont besoin.

```
// mauvais (désolé, cela ne s'affiche pas bien sur mobile)const longString = 'This is a very long string that \    far exceeds the 80 column limit. It unfortunately \    contains long stretches of spaces due to how the \    continued lines are indented.';
```

```
// bonconst longString = 'This is a very long string that ' +     'far exceeds the 80 column limit. It does not contain ' +     'long stretches of spaces since the concatenated ' +    'strings are cleaner.';
```

#### "for... of" est le type préféré de boucle "for"

> Avec ES6, le langage dispose maintenant de trois types différents de boucles `for`. Toutes peuvent être utilisées, bien que les boucles `for`-`of` doivent être préférées lorsque cela est possible.

C'est une règle étrange à mon avis, mais je l'ai incluse car il est intéressant de noter que Google déclare un type préféré de boucle `for`.

J'ai toujours pensé que les boucles `for... in` étaient meilleures pour les objets, tandis que les boucles `for... of` étaient mieux adaptées aux tableaux. Une situation du type "le bon outil pour le bon travail".

Bien que la spécification de Google ici ne contredise pas nécessairement cette idée, il est intéressant de savoir qu'ils ont une préférence pour cette boucle en particulier.

#### N'utilisez pas eval()

> N'utilisez pas `eval` ou le constructeur `Function(...string)` (sauf pour les chargeurs de code). Ces fonctionnalités sont potentiellement dangereuses et ne fonctionnent tout simplement pas dans les environnements CSP.

La [page MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval) pour `eval()` contient même une section intitulée "Ne pas utiliser eval !".

```
// mauvaislet obj = { a: 20, b: 30 };let propName = getPropName();  // retourne "a" ou "b"eval( 'var result = obj.' + propName );
```

```
// bonlet obj = { a: 20, b: 30 };let propName = getPropName();  // retourne "a" ou "b"let result = obj[ propName ];  //  obj[ "a" ] est la même chose que obj.a
```

#### Les constantes doivent être nommées en MAJUSCULES séparées par des underscores

> Les noms de constantes utilisent `CONSTANT_CASE` : toutes les lettres en majuscules, avec les mots séparés par des underscores.

Si vous êtes absolument sûr qu'une variable ne devrait pas changer, vous pouvez l'indiquer en mettant le nom de la constante en majuscules. Cela rend l'immuabilité de la constante évidente lorsqu'elle est utilisée dans votre code.

Une exception notable à cette règle est si la constante est à portée de fonction. Dans ce cas, elle doit être écrite en camelCase.

```
// mauvaisconst number = 5;
```

```
// bonconst NUMBER = 5;
```

#### Une variable par déclaration

> Chaque déclaration de variable locale ne déclare qu'une seule variable : les déclarations telles que `let a = 1, b = 2;` ne sont pas utilisées.

```
// mauvaislet a = 1, b = 2, c = 3;
```

```
// bonlet a = 1;let b = 2;let c = 3;
```

#### Utilisez des guillemets simples, pas des guillemets doubles

> Les littéraux de chaîne ordinaires sont délimités avec des guillemets simples (`'`), plutôt qu'avec des guillemets doubles (`"`).

> Astuce : si une chaîne contient un caractère de guillemet simple, envisagez d'utiliser une chaîne template pour éviter d'avoir à échapper le guillemet.

```
// mauvaislet directive = "No identification of self or mission."
```

```
// mauvaislet saying = 'Say it ain\u0027t so.';
```

```
// bonlet directive = 'No identification of self or mission.';
```

```
// bonlet saying = `Say it ain't so`;
```

#### Une note finale

Comme je l'ai dit au début, il ne s'agit pas de mandats. Google n'est qu'un des nombreux géants de la technologie, et ce ne sont que des recommandations.

Cela dit, il est intéressant de regarder les recommandations de style publiées par une entreprise comme Google, qui emploie beaucoup de personnes brillantes qui passent beaucoup de temps à écrire du code excellent.

Vous pouvez suivre ces règles si vous souhaitez suivre les directives pour un "code source conforme à Google" — mais, bien sûr, beaucoup de gens ne sont pas d'accord, et vous êtes libre de rejeter tout ou partie de cela.

Je pense personnellement qu'il y a beaucoup de cas où la spécification d'Airbnb est plus attrayante que celle de Google. Peu importe la position que vous prenez sur ces règles particulières, il est toujours important de garder à l'esprit la cohérence stylistique lorsque vous écrivez un quelconque type de code.