---
title: Ce que j'ai appris en lisant le code source de Redux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-10-19T22:58:46.000Z'
originalURL: https://freecodecamp.org/news/what-i-learned-from-reading-the-redux-source-code-836793a48768
coverImage: https://cdn-media-1.freecodecamp.org/images/1*BpaqVMW2RjQAg9cFHcX1pw.png
tags:
- name: JavaScript
  slug: javascript
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: Redux
  slug: redux
- name: Web Development
  slug: web-development
seo_title: Ce que j'ai appris en lisant le code source de Redux
seo_desc: 'By Anthony Ng

  I’ve always heard that reading code is a good way to expand your horizons as a developer.

  So I made a conscious decision to really dig deep into a well-written JavaScript
  library and learn as much as I could.

  I chose to look at Redux be...'
---

Par Anthony Ng

J'ai toujours entendu dire que lire du code est un bon moyen d'élargir ses horizons en tant que développeur.

J'ai donc pris la décision consciente de vraiment plonger dans une bibliothèque JavaScript bien écrite et d'apprendre autant que possible.

J'ai choisi de regarder [Redux](https://github.com/reactjs/redux) parce qu'il a une base de code relativement petite.

Cet article ne sera pas un tutoriel sur Redux, mais plutôt des morceaux d'information que j'ai appris en regardant leur code source. Si vous êtes intéressé à apprendre Redux lui-même, je vous recommande vivement de regarder la série [Getting Started with Redux](https://egghead.io/courses/getting-started-with-redux) du créateur de Redux lui-même, Dan Abramov.

### Apprendre de l'Open Source

Lorsque de nouveaux développeurs me demandent quelle est la meilleure façon d'apprendre, je réponds qu'ils devraient travailler sur des projets.

C'est incroyable quand vous tombez sur une idée de projet sur laquelle travailler et que vous utiliseriez vous-même. Cette passion pour un produit vous aidera à traverser ces sessions de débogage de plusieurs heures et vous empêchera de l'abandonner lorsque les choses deviennent difficiles.

Mais il y a un inconvénient à ne travailler que par soi-même. Vous ne remarquerez aucune des mauvaises habitudes que vous prenez en cours de route. Vous n'apprendrez aucune des meilleures pratiques. Vous n'entendrez pas parler de tous les nouveaux frameworks et outils qui poussent autour de vous. Et vous remarquerez rapidement que vos compétences stagnent pendant votre aventure solitaire.

Lorsque cela est possible, je vous recommande de chercher d'autres développeurs pour programmer en binôme.

S'asseoir à côté d'un pair (ou si vous avez de la chance, quelqu'un de plus expérimenté) vous permet d'observer leurs processus de pensée. Vous pouvez voir comment leurs doigts glissent sur le clavier. Vous pouvez regarder comment ils luttent pour résoudre des algorithmes. Vous pouvez apprendre de nouveaux outils de développement et des raccourcis clavier. Vous pouvez absorber toutes les choses intangibles que vous n'apprendrez pas en travaillant seul.

Être au cœur de l'action est l'endroit idéal pour être.

![Image](https://cdn-media-1.freecodecamp.org/images/rMVEJty44Wio6gQ-S31abQO77VNx4bjGdXwz)
_Un violon Stradivarius_

Prenons par exemple le violon Stradivarius. Les instruments Stradivarius ont une réputation pour une excellente qualité sonore qui (arguablement) n'a pas d'égal. De nombreuses théories ont été présentées pour expliquer la supériorité des Stradivarius, allant du bois récupéré dans de vieilles cathédrales à des conservateurs de bois spéciaux qui étaient utilisés à l'époque. Les gens ont essayé de le reproduire avec de pauvres résultats parce que nous ne savons pas comment Antonio Stradivari travaillait.

Mais imaginez tous les secrets et astuces que l'on pourrait apprendre si vous étiez dans la même pièce qu'Antonio, assis juste à côté de lui pendant qu'il travaillait.

C'est ainsi que vous devriez traiter vos sessions de programmation en binôme. Vous devriez apporter une bonne dose de curiosité en regardant votre pair créer du code à la Stradivarius. Il n'y a pas de meilleure opportunité pour voir tout le sang, la sueur et les larmes qui entrent dans une ligne de code.

Pour beaucoup, l'opportunité de programmer en binôme est un luxe rare. Mais tout le monde peut apprendre des autres en regardant le code qu'ils ont écrit.

Lire du code bien écrit est comme lire un roman bien écrit. Cela implique plus d'interprétation de votre part que si vous parliez directement avec l'auteur. Mais vous pouvez recueillir une richesse d'informations en lisant les commentaires et le code.

Pour ceux qui sont sceptiques quant à la quantité de choses que l'on peut apprendre en lisant le code de quelqu'un d'autre, notez cette histoire. Un lycéen nommé Bill Gates a fouillé dans les poubelles d'une entreprise pour obtenir leur code source et apprendre leurs secrets.

Si quelqu'un comme Bill Gates a pris tout ce mal pour lire le code de quelqu'un d'autre, je pense que cela vaut la peine pour nous d'ouvrir un dépôt Github et de faire de même.

![Image](https://cdn-media-1.freecodecamp.org/images/wBf6sIwzTXqNlqMZ86TUikxd8tisDtTSHzBe)
_Pas de code source ici_

Lire du code et apprendre des autres n'est pas un nouveau concept. Les tutoriels sont structurés de manière à ce que vous suiviez un maître à travers un voyage de codage. Un tutoriel bien écrit donnera l'impression que vous êtes assis à côté de l'auteur. Vous avez l'opportunité de lire les problèmes auxquels ils pensent.

Les liens hypertexte fournissent des ressources que vous pouvez lire et même le faire au milieu du tutoriel (vous ne feriez pas cela dans une session de programmation en binôme). La section des commentaires et les réseaux sociaux vous permettent d'avoir des conversations avec les maîtres.

Je regarde aussi des gens coder sur YouTube. Je recommande la série [SuperCharged Live Coding Session](https://www.youtube.com/watch?v=rBSY7BOYRo4) de la chaîne YouTube des développeurs de Google Chrome. Vous pouvez regarder deux ingénieurs de Google coder un projet en direct. Vous pouvez voir comment ils abordent les problèmes de performance, luttent contre les fautes de frappe comme le reste d'entre nous, et se bloquent.

### Leçons apprises en cours de route

#### ESLint

Le linting est un processus qui consiste à examiner votre code pour y détecter des erreurs potentielles. Il aide à faire respecter le style de code et à garder votre code cohérent et propre. Vous pouvez utiliser vos propres règles de style personnalisées ou des règles prédéfinies qui suivent des styles conventionnels (comme celles fournies par Airbnb).

Le linting est particulièrement efficace lorsque vous travaillez avec une équipe de développeurs. Il aide le code à avoir l'air comme s'il avait été écrit par une seule personne. Il force également les gens à suivre les guides de style de l'entreprise (que les développeurs pourraient ne pas prendre le temps de lire autrement).

Les linters ne sont pas seulement pour l'esthétique. Ils vous forcent à suivre les meilleures pratiques. Par exemple, ils peuvent vous dire quand utiliser le mot-clé "const" pour les variables qui ne sont pas réassignées.

Si vous utilisez des plugins React, ils peuvent vous avertir des composants qui peuvent être refactorisés en composants fonctionnels sans état. Ils sont également un excellent moyen d'apprendre la nouvelle syntaxe ES6 et même de vous dire où vous pouvez mettre à jour votre code avec de nouvelles fonctionnalités.

Voici les instructions pour commencer rapidement avec ESlint dans votre projet :

1. Installez le package ESlint.

```
$ npm install --save-dev eslint
```

2. Configurez les options ESlint.

```
./node_modules/.bin/eslint --init
```

3. Configurez un script npm pour exécuter votre linter dans votre fichier package.json (facultatif).

```
"scripts": {  "lint": "./node_modules/.bin/eslint"}
```

4. Exécutez le linter.

```
$ npm run lint
```

Consultez [leur documentation](http://eslint.org/docs/user-guide/getting-started) pour plus de détails sur la façon de commencer.

De nombreux éditeurs ont également des plugins qui linteront vos fichiers au fur et à mesure que vous tapez.

Parfois, les linters peuvent se plaindre du code dont vous avez réellement besoin, comme un console.log. Vous pouvez dire à votre linter d'ignorer certaines lignes de code dans leur analyse.

Pour ce faire avec ESlint, vous pouvez inclure les commentaires suivants :

```
 // Ignorer une seule ligne console.log('Hello World'); // eslint-disable-line no-console
```

```
// Ignorer plusieurs lignes /* eslint-disable no-console */ console.log('Hello World'); console.log('Goodbye World'); /* eslint-enable no-console */
```

#### Vérifier la minification

J'ai trouvé une fonction "isCrushed()" aléatoire à l'intérieur du code source qui n'avait pas de corps. C'était étrange.

Mais j'ai découvert que son seul but était de voir si le code était minifié. Pendant la minification, les noms de fonctions et de variables sont raccourcis. Il y avait une instruction if qui vérifiait si la fonction "isCrushed()" existait toujours avec ce nom. Un avertissement serait affiché si le code minifié était utilisé en développement.

#### Ne craignez pas les erreurs

J'avais rarement utilisé des erreurs dans mon code en dehors de l'apprentissage. JavaScript est un langage faiblement typé, donc nous devrions être paranoïaques quant à ce qui est passé dans nos fonctions. Nous devrions lancer des erreurs et crier comme le ferait un langage fortement typé.

Enfin, utilisez les instructions try...catch...finally avec ces erreurs. Cela rendra votre code plus facile à déboguer et à comprendre à l'avenir.

Jetez un coup d'œil à cette belle trace de pile que les erreurs produisent dans la console.

![Image](https://cdn-media-1.freecodecamp.org/images/qMigCcjLcdgeo5BdPANRZWYXEsml1d5IIcdi)
_Une trace de pile utile_

Les erreurs rendent vos intentions explicites. Par exemple, si votre fonction "add()" n'attend que des nombres, alors faites-le savoir au monde entier.

```
 function add(a, b) {   if(typeof a !== 'number' || typeof b !== 'number') {     throw new Error('Arguments invalides passés. Attendus des nombres');   }
```

```
   return a + b; }
```

```
var sum = add('foo', 2); // les erreurs empêcheront les conséquences involontaires dans votre code 
```

#### Composition de fonctions

Il y avait une fonction "compose()" qui construisait de nouvelles fonctions à partir de fonctions existantes :

```
 function compose(...funcs) {   if (funcs.length === 0) {     return arg => arg   }
```

```
   if (funcs.length === 1) {     return funcs[0]   }
```

```
   const last = funcs[funcs.length — 1]   const rest = funcs.slice(0, -1)   return (...args) => rest.reduceRight((composed, f) => f(composed),    last(...args)) } 
```

Si j'ai une fonction existante qui élève un nombre au carré et une autre fonction qui double un nombre, je peux les combiner ensemble dans une nouvelle fonction.

```
 function square(num) {   return num * num; }
```

```
function double(num) {   return num * 2;}
```

```
function squareThenDouble(num) {   return compose(double, square)(num);}
```

```
console.log(squareThenDouble(7)); // 98 
```

Je ne sais pas si je vais jamais utiliser cela, mais c'est bien de l'avoir dans mes outils.

#### Méthodes natives

Lorsque je regardais la fonction "compose()", je suis tombé sur une méthode de tableau "reduceRight()" que je n'avais jamais entendue. Cela m'a fait me demander combien d'autres fonctions natives je n'ai pas apprises.

Regardons un extrait de code qui utilise la méthode native de tableau "filter()" et un autre qui ne l'utilise pas, et voyons pourquoi il est utile de savoir quelles fonctions natives existent.

```
 function custom(array) {   let newArray = [];
```

```
   for(var i = 0; i < array.length; i++) {     if(array[i]) {       newArray.push(array[i]);     }   }
```

```
   return newArray; }
```

```
 function native(array) {   return array.filter((current) => current); }
```

```
 const myArray = [false, true, true, false, false]; console.log(custom(myArray)); console.log(native(myArray)); 
```

Vous pouvez voir à quel point le code qui utilise "filter()" est concis. Plus important encore, nous ne réinventons pas la roue. La fonction "filter()" a été utilisée par des millions d'autres utilisateurs et est probablement moins boguée que votre implémentation.

Avant d'écrire votre propre solution, vérifiez si le problème a déjà été résolu dans le langage que vous utilisez. Vous serez surpris du nombre de méthodes utilitaires qu'un langage peut avoir. (Par exemple, consultez cette méthode Ruby pour les [permutations répétées](https://ruby-doc.org/core-2.2.0/Array.html#method-i-repeated_permutation) dans un tableau).

#### Noms de fonctions descriptifs

En regardant le code source, j'ai vu un certain nombre de noms de fonctions longs.

1. getUndefinedStateErrorMessage
2. getUnexpectedStateShapeWarningMessage
3. assertReducerSanity

Bien qu'ils ne roulent pas sur la langue, il n'y a aucune confusion sur ce qu'ils font.

Utilisez des noms descriptifs dans votre code. Vous passerez plus de temps à lire du code qu'à l'écrire, alors rendez-le plus facile à lire pour vous et pour tout le monde.

Les avantages d'utiliser des noms descriptifs longs dépassent largement l'irritation que vous ressentez à cause des frappes supplémentaires. Les éditeurs de texte modernes ont des fonctionnalités d'autocomplétion qui vous aident à taper, donc vous n'avez aucune excuse pour utiliser "x" ou "y" comme variables.

#### console.error vs. console.log

N'utilisez pas console.log pour tout. Si vous avez une erreur que vous voulez imprimer, utilisez console.error. Vous obtenez une belle impression rouge avec une trace de pile dans votre console.

![Image](https://cdn-media-1.freecodecamp.org/images/f5yaQnce2-QTYdm15yPUZxxra9KIMSX-GzI1)
_console.error()_

Jetez un coup d'œil à la [documentation](https://developer.mozilla.org/en-US/docs/Web/API/Console) pour la console et voyez quelles autres méthodes sont disponibles. Il y a un minuteur intégré (console.time()), vous pouvez imprimer vos informations dans une disposition de tableau (console.table()) et bien plus encore.

N'ayez pas peur de fouiller dans le code Open Source. Vous apprendrez définitivement quelque chose et pourriez même trouver quelque chose à contribuer.

Faites-moi savoir quelles choses vous avez apprises en lisant le code des autres.