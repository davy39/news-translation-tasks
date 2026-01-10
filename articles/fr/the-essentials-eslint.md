---
title: 'ESLint : Les faits essentiels sur les outils essentiels de développement front-end'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-13T15:07:35.000Z'
originalURL: https://freecodecamp.org/news/the-essentials-eslint
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/The-Essentials--ESLint-01.png
tags:
- name: eslint
  slug: eslint
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
seo_title: 'ESLint : Les faits essentiels sur les outils essentiels de développement
  front-end'
seo_desc: 'By Vinh Nguyen

  Recently, I''ve been getting more involved in front-end development. The more I
  do, the more my mind and my soul get lost in its chaotic world. Even a simple To–Do–List
  app can easily require a bunch of tools—ESLint, Babel, Webpack, to ...'
---

Par Vinh Nguyen

Récemment, je me suis davantage impliqué dans le développement front-end. Plus je m'y engage, plus mon esprit et mon âme se perdent dans son monde chaotique. Même une simple application de liste de tâches peut facilement nécessiter une multitude d'outils — [ESLint](https://eslint.org), [Babel](https://babeljs.io/), [Webpack](https://webpack.js.org/), pour n'en nommer que quelques-uns — et de packages juste pour commencer.

Heureusement, il existe de nombreux kits de démarrage afin que nous n'ayons pas à tout faire à partir de zéro. Avec eux, tout est déjà configuré pour que nous puissions commencer à écrire la première ligne de code immédiatement. Cela permet de gagner du temps sur des tâches répétitives et ennuyeuses, ce qui peut être idéal pour les développeurs expérimentés.

Cependant, cet avantage a un prix pour les débutants. Comme tout fonctionne dès le départ, cela semble magique, et ils ne savent peut-être pas ce qui se passe réellement sous le capot, ce qui est important à comprendre à un certain niveau. Bien que la courbe d'apprentissage ne soit pas aussi raide que d'autres — essayez de comparer avec certains outils que vous avez appris et utilisés, vous comprendrez ce que je veux dire — dans ce monde chaotique, nous avons besoin d'un guide de survie pour le voyage.

Cette série couvrira les outils fondamentaux du développement front-end et les connaissances essentielles dont nous avons besoin à leur sujet. Cela nous permettra de maîtriser les outils au lieu d'être contrôlés par eux.

Dans cette série, nous nous concentrerons sur l'expérience du développeur avec chacun de ces outils. L'objectif de cette série est donc de servir de guide de survie et de donner un aperçu de haut niveau de chaque outil, et non de servir de documentation.

Ce qui sera inclus :

* ESLint <- Nous sommes ici
* Babel
* Webpack
* Flow
* TypeScript
* Jest.

Assez de préambule, commençons avec le premier outil : ESLint.

# Qu'est-ce qu'ESLint et pourquoi devrions-nous l'utiliser ?

ESLint est, comme son nom l'indique, un linter pour [ECMAScript](http://www.ecma-international.org/publications/standards/Ecma-262.htm). Et la définition d'un linter est :

> une machine pour enlever les fibres courtes des graines de coton après l'égrainage.

Bien que le code et les graines de coton n'aient aucun rapport, qu'il s'agisse de code ou de graines de coton, un linter aidera à rendre les choses plus propres et plus cohérentes. Nous ne voulons pas voir du code comme ceci :

```javascript
const count = 1;
const message  =  "Hello, ESLint"
    count += 1
```

Cela semble non seulement laid, mais contient également une erreur. C'est là qu'ESLint intervient pour aider. Au lieu de laisser l'erreur être affichée dans la console du navigateur lorsque nous exécutons le code, ESLint la détectera pendant que nous tapons (enfin, pas vraiment : nous aurons besoin d'extensions d'éditeur ou d'IDE pour cela, ce qui sera couvert plus tard).

Bien sûr, cette erreur n'est pas difficile à corriger, mais ne serait-il pas plus agréable d'avoir un assistant qui nous rappelle chaque fois que nous sommes sur le point de faire une erreur et qui la corrige peut-être automatiquement pour nous ? Bien qu'ESLint ne puisse pas détecter tous les types d'erreurs, il nous épargne au moins certains efforts afin que nous puissions consacrer du temps à d'autres choses qui comptent et nécessitent une attention humaine.

# Comment fonctionne ESLint ?

Maintenant que nous savons ce qu'est ESLint et pourquoi nous en avons besoin, approfondissons un peu et voyons comment il fonctionne. En essence, nous pouvons le décomposer en trois grandes étapes.

## Analyseur syntaxique (Parser)

Le code que nous écrivons n'est rien de plus qu'une séquence de caractères. Cependant, cette séquence n'est pas simplement des caractères aléatoires : ils doivent suivre un ensemble de règles ou de conventions qui constituent la grammaire formant un langage.

Pour un humain, passer de la lecture de texte ou de code à sa compréhension conceptuelle nous demande peu d'efforts. Pour un ordinateur, cela est beaucoup plus difficile à accomplir. Par exemple :

```javascript
const tool = 'ESLint' // 1
  const  tool  =  "ESLint" // 2
```

Lorsque nous lisons les deux lignes ci-dessus, nous savons immédiatement qu'elles sont identiques et peuvent être lues comme "il y a une constante nommée `tool` avec la valeur ESLint". Pour un ordinateur, qui ne comprend pas le sens, ces deux lignes semblent assez différentes. Par conséquent, si nous fournissons du code brut à ESLint, il est presque impossible de faire quoi que ce soit.

Lorsque les choses deviennent compliquées et difficiles à communiquer — pensez à la manière dont nous pouvons faire comprendre à un ordinateur ce que nous faisons — l'abstraction peut être une solution. En abstraisant une chose, nous cachons tous les détails inutiles, réduisons le bruit et gardons tout le monde sur la même page, ce qui facilite la communication. Dans l'exemple ci-dessus, un espace ou deux espaces n'ont pas d'importance, tout comme les guillemets simples ou doubles.

En d'autres termes, c'est ce que fait un analyseur syntaxique. Il convertit le code brut en un arbre de syntaxe abstraite (AST), et cet AST est utilisé comme support pour les règles de linting. Il y a encore de nombreuses étapes qu'un analyseur syntaxique doit effectuer pour créer un AST — si vous êtes intéressé à en apprendre davantage sur la génération d'un AST, [ce tutoriel](https://the-super-tiny-compiler.glitch.me/) donne un bon aperçu.

## Règles

L'étape suivante du processus consiste à exécuter l'AST à travers une liste de règles. Une règle est une logique pour identifier les problèmes potentiels existants dans le code à partir de l'AST. Les problèmes ici ne sont pas nécessairement des erreurs syntaxiques ou sémantiques, mais peuvent également être des problèmes stylistiques. La sortie donnée par une règle inclura des informations utiles pour une utilisation ultérieure, comme les lignes de code, les positions et des messages informatifs sur le problème.

En plus de détecter les problèmes, une règle peut même corriger automatiquement le code si possible. Par exemple, lorsque [no-multi-spaces](https://eslint.org/docs/rules/no-multi-spaces) est appliqué au code ci-dessus, il supprimera tous les espaces redondants, ce qui rendra le code propre et cohérent.

```javascript
  const  tool  =  "ESLint" // 2
// devient
const tool = "ESLint" // 2
```

Dans différents scénarios, une règle peut être utilisée à différents niveaux — désactivée, avertissement uniquement ou erreur stricte — et avoir diverses options, ce qui nous donne le contrôle sur la manière d'utiliser la règle.

## Résultat

Nous voici à la fin du processus. Avec la sortie d'une règle, il ne reste plus qu'à afficher cela de manière conviviale, grâce à toutes les informations utiles dont nous avons parlé précédemment. Ensuite, à partir du résultat, nous pouvons rapidement pointer le problème, où il se trouve, et apporter une correction, ou peut-être pas.

# Intégration

ESLint peut être utilisé comme un outil autonome avec son CLI robuste, mais c'est une manière basique d'utiliser ESLint. Nous ne voulons pas taper une commande chaque fois que nous voulons vérifier le code, surtout dans un environnement de développement. La solution à cela est d'intégrer ESLint dans notre environnement de développement afin que nous puissions écrire du code et voir les problèmes détectés par ESLint, le tout au même endroit.

Ce type d'intégration provient d'extensions spécifiques aux IDE ou aux éditeurs. Ces extensions nécessitent ESLint pour fonctionner, car elles exécutent ESLint en arrière-plan — il n'est donc pas surprenant que nous devions toujours installer ESLint avec elles, elles ne sont rien sans ESLint. Ce principe s'applique à d'autres extensions d'IDE ou d'éditeur que nous utilisons quotidiennement.

Vous souvenez-vous de la sortie d'une règle dont nous avons parlé plus haut ? Une extension l'utilisera pour l'afficher dans l'IDE ou l'éditeur. La manière exacte dont la sortie est affichée dépend de la manière dont l'extension est implémentée et de la manière dont l'IDE ou l'éditeur est ouvert à ses extensions. Certaines extensions tirent également parti des capacités de correction des problèmes des règles pour modifier le code lors de l'enregistrement si nous activons cette fonction.

# Configuration

La configuration est la principale force qui donne de la polyvalence à un outil. ESLint ne fait pas exception à cela, sauf qu'il possède la configuration la plus complète parmi les autres outils. En général, nous avons besoin d'un fichier ou d'un endroit pour mettre la configuration, et il y a plusieurs options pour nous.

Toutes ces options se résument à deux principales méthodes : soit nous avons un fichier de configuration séparé pour chaque outil, soit nous les regroupons tous dans `package.json`. `.eslintrc.js` est l'un des fichiers que ESLint recherchera pour sa configuration, et aussi celui avec la plus haute priorité.

La prochaine chose que nous devons savoir sur la configuration est sa hiérarchie et son comportement en cascade. Grâce à ces fonctionnalités, nous n'avons pas besoin d'avoir un fichier de configuration dans chaque dossier du projet.

Si un fichier de configuration n'existe pas dans un dossier, ESLint recherche simplement dans le dossier parent jusqu'à ce qu'il ne puisse plus en trouver. Ensuite, il reviendra à la configuration par défaut de l'utilisateur dans `~/.eslintrc`. Sinon, le fichier de configuration s'ajoutera ou remplacera ceux des niveaux supérieurs.

Il y a cependant un ajustement spécial à cela. Si nous spécifions `root: true` dans un fichier de configuration, la recherche s'arrêtera à ce fichier au lieu de remonter comme avant. De plus, ESLint utilisera ce fichier de configuration comme la configuration racine, et toutes les configurations enfants seront basées sur celle-ci.

Cela ne se limite pas à ESLint — ces choses sont courantes pour d'autres outils. Parlons de la configuration spécifique à ESLint.

## Analyseur syntaxique (Parser)

Le rôle de l'analyseur syntaxique dans ESLint a été discuté ci-dessus. Par défaut, ESLint utilise [Espree](https://github.com/eslint/espree) comme analyseur syntaxique. Nous pouvons changer cet analyseur syntaxique pour un autre compatible comme [babel-eslint](https://www.npmjs.com/package/babel-eslint) ou [@typescript-eslint/parser](https://www.npmjs.com/package/@typescript-eslint/parser) si nous utilisons Babel ou TypeScript, respectivement.

Pour configurer l'analyseur syntaxique, nous utilisons `parserOptions`. Parmi les options supportées par Espree, voici quelques-unes que nous utilisons souvent et auxquelles nous devons prêter attention :

* `ecmaVersion`

Nous devons spécifier la version ECMA appropriée pour les fonctionnalités que nous voulons utiliser. Par exemple, si `ecmaVersion: 5`, le code ci-dessous donnera quelques erreurs.

```javascript
let a = [1, 2, 3, 4] // erreur due au mot-clé `let`
var b = [...a, 5] // erreur due à la syntaxe de décomposition
```

L'analyseur syntaxique ne peut pas analyser le code car le mot-clé `let` et la syntaxe de décomposition ont été introduits dans ES6. Changer `ecmaVersion` en 6 ou plus résoudra simplement les erreurs.

* `sourceType`

De nos jours, nous écrivons presque tout en modules, puis nous les regroupons. Donc cette option, la plupart du temps, devrait être `module`.

Une autre valeur que nous pouvons utiliser — ainsi que la valeur par défaut — est `script`. La différence est de savoir si nous pouvons utiliser les [modules JS](https://v8.dev/features/modules) ou non, c'est-à-dire utiliser les mots-clés `import` et `export`. La prochaine fois que nous obtenons ce message d'erreur `Parsing error: 'import' and 'export' may appear only with 'sourceType: module'`, nous savons où regarder.

* `ecmaFeatures.jsx`

Il peut y avoir des fonctionnalités ES supplémentaires que nous voulons utiliser, par exemple la syntaxe [JSX](https://facebook.github.io/jsx/). Nous utilisons `ecmaFeatures.jsx: true` pour activer cette fonctionnalité. Notez que le support JSX d'Espree n'est pas le même que le JSX dans React. Si nous voulons un JSX spécifique à React, nous devrions utiliser [eslint-plugin-react](https://github.com/yannickcr/eslint-plugin-react) pour de meilleurs résultats.

Si nous utilisons un autre analyseur syntaxique, ces options sont plus ou moins les mêmes. Certains peuvent avoir moins d'options, et d'autres peuvent en avoir plus, mais elles sont toutes définies sous `parserOptions`.

## Environnement

Selon l'endroit où le code est exécuté, il existe différentes variables globales prédéfinies. Nous avons `window`, `document` dans le navigateur, par exemple. Il serait irritant si la règle [no-undef](https://eslint.org/docs/rules/no-undef) est activée et qu'ESLint nous dit constamment que `window` ou `document` n'est pas défini.

L'option `env` est là pour aider. En spécifiant une liste d'environnements, ESLint connaîtra les variables globales dans ces environnements et nous permettra de les utiliser sans un mot.

Il y a un environnement spécial auquel nous devons prêter attention, `es6`. Il définira implicitement `parserOptions.ecmaVersion` à 6 et activera toutes les fonctionnalités ES6 sauf pour les modules que nous devons toujours utiliser `parserOptions.sourceType: "module"` séparément.

# Plugins et configurations partageables

Avoir la même configuration pour les règles encore et encore dans différents projets peut être fastidieux. Heureusement, nous pouvons réutiliser une configuration et ne remplacer que les règles si nécessaire avec `extends`. Nous appelons ce type de configuration des configurations partageables, et ESLint en a déjà deux pour nous : `eslint:recommended` et `eslint:all`.

Par convention, les configurations partageables d'ESLint ont le préfixe `eslint-config` afin que nous puissions facilement les trouver via NPM avec le mot-clé [`eslint-config`](https://www.npmjs.com/search?q=keywords:eslint-config). Parmi des centaines de résultats, il y en a quelques-uns populaires, comme [eslint-config-airbnb](https://github.com/airbnb/javascript/tree/master/packages/eslint-config-airbnb) ou [eslint-config-google](https://github.com/google/eslint-config-google), à vous de choisir.

Dès le départ, ESLint dispose d'un ensemble de règles pour servir différents objectifs, des erreurs possibles, des meilleures pratiques, ES6 aux problèmes stylistiques. De plus, pour renforcer ses capacités, ESLint dispose d'un grand nombre de règles tierces fournies par près de mille plugins. Similaires aux configurations partageables, les plugins d'ESLint sont préfixés avec `eslint-plugin` et sont disponibles sur NPM avec le mot-clé [`eslint-plugin`](https://www.npmjs.com/search?q=keywords:eslint-plugin).

Un plugin définit un ensemble de nouvelles règles, et dans la plupart des cas, il expose ses propres configurations pratiques. Par exemple, [eslint-plugin-react](https://github.com/yannickcr/eslint-plugin-react) nous offre deux configurations partageables, `eslint-plugin-react:recommended` et `eslint-plugin-react:all`, tout comme `eslint:recommended` et `eslint:all`. Pour utiliser l'une d'entre elles, nous devons, tout d'abord, définir le nom du plugin, et ensuite étendre la configuration.

```javascript
{
  plugins: ["react"],
  extends: "plugin:react/recommended"
}

// Notez que nous devons préfixer la configuration par `plugin:react`
```

Une question courante à poser est de savoir quels plugins ou configurations utiliser. Bien que cela dépende largement de nos besoins, nous pouvons utiliser [Awesome ESLint](https://github.com/dustinspecker/awesome-eslint) comme référence pour trouver des plugins ainsi que des configurations utiles.

# Prettier

Nous y sommes presque — nous avons presque atteint la fin. Dernier point, mais non des moindres, nous allons discuter d'un compagnon populaire d'ESLint, [Prettier](https://github.com/prettier/prettier). En bref, Prettier est un formateur de code opinionné. Bien que Prettier puisse être utilisé seul, son intégration à ESLint améliore considérablement l'expérience, et [eslint-plugin-prettier](https://github.com/prettier/eslint-plugin-prettier) fait ce travail.

La différence entre l'utilisation de Prettier seul et l'utilisation de Prettier avec ESLint peut être résumée à la mise en forme du code comme un problème. Au lieu de donner des problèmes de format séparément, l'exécution de Prettier avec ESLint traitera les problèmes de format comme les autres problèmes. Cependant, ces problèmes sont toujours corrigibles, ce qui équivaut à formater le code.

C'est ainsi que fonctionne `eslint-plugin-prettier`. Il exécute Prettier, en tant que règle, en arrière-plan et compare le code avant et après son passage dans Prettier. Enfin, il signale les différences en tant que problèmes ESLint individuels. Pour corriger ces problèmes, le plugin utilise simplement le code formaté de Prettier.

Pour avoir cette intégration, nous devons installer à la fois `prettier` et `eslint-plugin-prettier`. `eslint-plugin-prettier` est également livré avec la configuration `eslint-plugin-prettier:recommended` — qui étend [eslint-config-prettier](https://github.com/prettier/eslint-config-prettier). Par conséquent, nous devons également installer `eslint-config-prettier` pour l'utiliser.

```javascript
{
  "plugins": ["prettier"],
  "extends": "plugin:prettier/recommended"
}
```

# Conclusion

Les linters ou formateurs de code sont devenus la norme de facto dans le développement logiciel en général, et ESLint, en particulier, dans le développement front-end.

Ses avantages vont bien au-delà de ce qu'il fait techniquement, car il aide les développeurs à se concentrer sur des questions plus importantes. Grâce à la délégation du style de code à une machine, nous pouvons éviter les styles opinionnés lors de la révision de code et utiliser ce temps pour une révision de code plus significative. La qualité du code en bénéficie également, et nous obtenons un code plus cohérent et moins sujet aux erreurs.

*Cet article a été initialement publié sur [mon blog](https://blog.vinhis.me/2019/08/03/the-essentials-of-essential-frontend-tools-eslint.html).*