---
title: Qu'est-ce que le linting et comment peut-il vous faire gagner du temps ?
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2019-10-09T14:30:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-linting-and-how-can-it-save-you-time
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/linting.jpg
tags:
- name: clean code
  slug: clean-code
- name: Code Quality
  slug: code-quality
- name: code review
  slug: code-review
- name: eslint
  slug: eslint
- name: front end
  slug: front-end
- name: Front-end Development
  slug: front-end-development
- name: frontend
  slug: frontend
- name: GatsbyJS
  slug: gatsbyjs
- name: JavaScript
  slug: javascript
- name: js
  slug: js
- name: React
  slug: reactjs
seo_title: Qu'est-ce que le linting et comment peut-il vous faire gagner du temps
  ?
seo_desc: 'One of the biggest challenges in software development is time. It’s something
  we can’t easily get more of, but linting can help us make the most out of the time
  we have.

  So what is linting?

  lint, or a linter, is a tool that analyzes source code to fl...'
---

L'un des plus grands défis du développement logiciel est le temps. C'est quelque chose que nous ne pouvons pas facilement obtenir davantage, mais le linting peut nous aider à tirer le meilleur parti du temps que nous avons.

## Qu'est-ce que le linting ?

**lint**, ou un **linter**, est un outil qui analyse le code source pour signaler les erreurs de programmation, les bugs, les erreurs stylistiques et les constructions suspectes. [https://en.wikipedia.org/wiki/Lint(software)](https://en.wikipedia.org/wiki/Lint(software))

En termes simples, un linter est un outil qui analyse votre code de manière programmatique dans le but de trouver des problèmes qui peuvent conduire à des bugs ou à des incohérences avec la santé et le style du code. Certains peuvent même aider à les corriger pour vous !

![Image](https://www.freecodecamp.org/news/content/images/2019/10/miachel-scott-tell-me-more.gif)
_Michael Scott - Tell me more_

Prenons par exemple l'exemple suivant :

```js
const test = 'I am a test';
console.log(`Test: ${test}`);
const test = 'Another one.';
```

Nous déclarons la constante `test` deux fois, ce qui ne plaira pas à notre moteur JavaScript. Avec les paramètres appropriés du linter et la configuration de surveillance, au lieu de tomber sur une erreur plus tard lorsque le code s'exécute, vous obtiendrez immédiatement une erreur grâce à votre linter qui s'exécute en arrière-plan :

```
  10:9  error  Parsing error: Identifier 'test' has already been declared

   8 |   const test = 'I am a test';
   9 |   console.log(`Test: ${2}`);
> 10 |   const test = 'Another one.';
     |         ^
```

Il peut être assez évident que vous avez 2 déclarations `const` identiques étant donné que cela ne fait que 3 lignes, mais dans une application plus complexe, cela peut faire gagner beaucoup de temps en évitant de devoir traquer un bug tenace qui n'est pas toujours évident.

## **En quoi le linting peut-il aider ?**

[Beaucoup de choses](https://eslint.org/docs/rules/), y compris, mais sans s'y limiter :

* Signaler les bugs dans votre code à partir d'erreurs de syntaxe
* Vous donner des avertissements lorsque le code peut ne pas être intuitif
* Fournir des suggestions pour les meilleures pratiques courantes
* Suivre les TODO et les FIXME
* Maintenir un style de code cohérent

La plupart des choses auxquelles vous pouvez penser existent probablement déjà [sous une forme ou une autre](https://github.com/dustinspecker/awesome-eslint), et si ce n'est pas le cas, vous pouvez même [créer des règles personnalisées](https://gist.github.com/sindresorhus/1656c46f23545deff8cc713649dcff26) qui répondent à vos besoins !

## **Comment cela aide-t-il réellement ou pourquoi devrais-je m'en soucier ?**

Probablement le plus grand thème sous-jacent de la liste ci-dessus est le fait que ces problèmes seront signalés immédiatement. Ces problèmes ne vous surprendront plus au milieu de l'exécution de votre application ou ne donneront plus d'anxiété à quelqu'un lors d'une revue de code. Vous et votre relecteur ne vous battrez plus sans fin de manière passive-agressive dans les commentaires pour savoir s'il faut inclure un point-virgule à la fin des instructions JS ([vous devriez](https://stackoverflow.com/a/444082) ?).

![Image](https://www.freecodecamp.org/news/content/images/2019/10/looking-for-semicolon.jpg)
_Grand-mère cherchant un point-virgule_

Tous ces moments qui vous empêchent d'être productif à cause d'une erreur de syntaxe stupide ou les micro-interactions que vous et vos coéquipiers avez lors d'une revue prennent du temps. Ils s'accumulent et finissent par prendre le temps que vous pourriez passer à corriger un autre bug ou à développer la prochaine grande fonctionnalité de votre produit.

## **Comment puis-je réellement commencer ?**

Bien qu'il existe des linters pour la plupart, sinon tous, les autres langages grand public, pour les besoins de cet article, je vais me concentrer sur JavaScript. Les mêmes principes s'appliquent, mais les outils peuvent être un peu différents.

Je vais vous montrer comment vous pouvez configurer le linting de base dans une application React. Vous pouvez facilement suivre en créant votre propre application React ou en utilisant mon modèle de départ [Gatsby](https://www.gatsbyjs.org/) : [https://github.com/colbyfayock/gatsby-starter-sass#starting-from-scratch](https://github.com/colbyfayock/gatsby-starter-sass#starting-from-scratch)

### **Votre Linter**

Pour commencer, nous avons d'abord besoin d'un linter. [Probablement le plus populaire](https://trends.google.com/trends/explore?geo=US&q=eslint,jshint,jslint) dans le monde JavaScript est [ESLint](https://eslint.org/). Votre linter sera en fait le moteur pour définir les règles et analyser vos fichiers pour les tester. ESLint est disponible en tant que [package npm](https://www.npmjs.com/package/eslint) et [une fois installé](https://eslint.org/docs/user-guide/getting-started), il vous permet de configurer un fichier de configuration de base et de démarrer avec quelques outils en ligne de commande.

Commençons par ajouter notre dépendance ESLint :

```
yarn add eslint -D
```

Nous installons cela en tant que `devDependency` (d'où le drapeau `-D`), car ce n'est pas quelque chose dont notre application a besoin pour fonctionner. Après son installation réussie, ajoutons-le à notre `package.json` en tant que script :

```json
...
"scripts": {
  ...
  "lint": "eslint .  --ext .js"
  ...
},
...
```

Dans ce qui précède, nous exécutons notre linter sur l'ensemble du répertoire du projet sur tout fichier ayant une extension `.js`. Si vous travaillez sur un grand projet avec de nombreux types de fichiers, peut-être même certains que vous ne souhaitez pas lint, vous pouvez [changer ce drapeau ou être plus spécifique](https://eslint.org/docs/user-guide/command-line-interface) avec d'autres options.

Pour prendre en charge ESLint, nous devons faire une chose de plus. Ajoutons un fichier à la racine de notre projet (probablement là où se trouve votre `package.json`) appelé `.eslintrc.js` et faisons en sorte que le contenu du fichier soit simplement :

```js
module.exports = {};
```

Une fois que vous êtes prêt, vous pouvez exécuter `yarn lint` et... obtenir une erreur.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/lint-with-import-errors.jpg)
_Résultats du lint - Erreurs d'importation_

C'est normal et attendu dans notre projet, alors continuons.

### **Votre Parseur**

Un outil courant dans la chaîne pour les développeurs JavaScript est [Babel](https://babeljs.io/), qui vous permet d'écrire du code avec des fonctionnalités qui peuvent ne pas être prises en charge dans tous les navigateurs, comme l'utilisation de [fonctions fléchées](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions), qui sont disponibles dans [ES6](http://es6-features.org/#Constants), et d'autres conventions comme l'importation de fichiers via `import`.

Le code que vous écrivez peut déjà passer par Babel pour fonctionner dans un navigateur, mais cela ne s'applique pas à ESLint par défaut, donc ESLint vous permet de spécifier un parseur qui permet au traitement de linting de voir le même code que votre navigateur. Dans ce cas, nous voulons utiliser le [parseur ESLint de Babel](https://github.com/babel/babel-eslint) qui est mis à notre disposition.

Pour le configurer, nous voulons d'abord installer notre dépendance :

```
yarn add babel-eslint -D
```

Typiquement, si vous utilisez `babel-eslint`, vous voudrez vous assurer que `babel` est installé à côté, mais dans notre cas, Gatsby utilise déjà `babel`, donc nous n'avons pas nécessairement besoin de l'ajouter. Après cela, nous voulons mettre à jour notre fichier de configuration `.eslintrc.js` avec quelques nouvelles options :

```js
module.exports = {
    "env": {
        "browser": true,
        "node": true,
        "es6": true
    },
    "parser": "babel-eslint"
};
```

Ici, nous informons ESLint que notre environnement s'exécutera dans node (la précompilation de Gatsby), dans le navigateur (l'application), et qu'il utilisera ES6. Cela aide ESLint à savoir comment exécuter votre code. De plus, nous voulons configurer notre parseur pour qu'il soit `babel-eslint`.

Une fois que nous sommes prêts, exécutons `yarn lint` à nouveau et... rien ne s'est vraiment passé.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/lint-with-nothing-happening.jpg)
_Résultats du lint - Rien ne s'est passé_

C'est toujours attendu, car nous n'avons pas encore configuré de règles !

### **Plugins pour votre code**

Vous écrivez une application [React](https://reactjs.org/) ? Le parseur Babel peut vous aider à transformer votre code, mais vous pourriez avoir du mal à être productif, car ESLint doit comprendre comment il doit fonctionner pour lint votre code React.

L'un des avantages d'ESLint est qu'il vous permet de [configurer des plugins](https://eslint.org/docs/developer-guide/working-with-plugins) qui ont la possibilité de créer et de définir des règles pour vous. Heureusement, en plus de notre parseur Babel ci-dessus qui fait une partie du travail, nous avons un [plugin React](https://github.com/yannickcr/eslint-plugin-react) disponible qui fait exactement cela et s'occupe du linting du JSX pour nous.

Commençons par installer notre dépendance :

```
yarn add eslint-plugin-react -D
```

De plus, mettons à jour notre fichier `.eslintrc.js` à nouveau :

```js
module.exports = {
    "settings": {
        "react": {
            "version": "detect"
        }
    },
    "env": {
        "browser": true,
        "node": true,
        "es6": true
    },
    "plugins": [
        "react"
    ],
    "parser": "babel-eslint"
};
```

Ce que nous ajoutons ici est un paramètre qui détecte automatiquement la version de React que vous utilisez, ce qui est utile pour que votre linting soit correctement analysé, puis nous configurons notre plugin React que nous avons installé ci-dessus.

Pour une dernière fois, nous allons exécuter notre script `lint` et obtenir rien :

![Image](https://www.freecodecamp.org/news/content/images/2019/10/lint-with-nothing-happening-1.jpg)
_Résultats du lint - Rien ne s'est passé_

### **Règles définies par les opinions des autres**

Si vous n'êtes pas vraiment sûr de par où commencer ou si vous voulez simplement vous lancer rapidement, il est recommandé d'activer [les règles recommandées par ESLint](https://eslint.org/docs/rules/). Ajoutons cela à notre fichier de configuration `.eslintrc.js` :

```js
module.exports = {
    "settings": {
        "react": {
            "version": "detect"
        }
    },
    "env": {
        "browser": true,
        "node": true,
        "es6": true
    },
    "plugins": [
        "react"
    ],
    "extends": [
        "eslint:recommended"
    ],
    "parser": "babel-eslint"
};
```

Et exécutons notre `yarn lint`.

Woah ! Cela va immédiatement vous donner beaucoup d'erreurs, il semble que quelque chose ne va pas.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/lint-with-react-errors.jpg)
_Résultats du lint - Erreurs React_

Puisque nous exécutons une application React, nous voulons également nous assurer que notre linter comprend les règles qu'il doit suivre, alors ajoutons également notre plugin React à la configuration `.eslintrc.js` :

```json
    "extends": [
        "eslint:recommended",
        "plugin:react/recommended"
    ],
```

Maintenant, si vous exécutez `yarn lint`, vous obtenez quelque chose de plus logique.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/lint-with-errors.jpg)
_Résultats du lint - Erreurs normales_

Si vous suivez, il semble que notre application de démarrage avait un point-virgule mal placé et une prop manquante dans notre validation `propTypes` pour `Layout.js`. Écrire cela m'a aidé à corriger mon propre dépôt ! ?

En allant plus loin, si celles-ci ne semblent pas répondre à vos besoins, de nombreux développeurs et équipes ont publié leurs propres configurations qu'ESLint vous permet d'utiliser facilement.

Parmi les plus populaires, on trouve :

* [Config d'Airbnb](https://www.npmjs.com/package/eslint-config-airbnb)
* [Semistandard](https://github.com/standard/eslint-config-semistandard)
* [Guide de style JS de Google](https://github.com/google/eslint-config-google)

Pas satisfait des options disponibles ? Vous pouvez même [créer et publier les vôtres](https://eslint.org/docs/6.0.0/developer-guide/shareable-configs) pour les superposer à d'autres comme point de départ ou essayer de les créer à partir de zéro.

### **Laissez-le faire le travail (la plupart du temps)**

Vous ne pensez pas que je vais vous faire corriger toutes ces choses vous-même, n'est-ce pas ? Eh bien, vous devrez peut-être en corriger certaines, mais essayons de faire en sorte qu'ESLint en corrige certaines pour nous.

Si vous avez remarqué après avoir exécuté la commande ci-dessus, ESLint nous a donné un message supplémentaire :

![Image](https://www.freecodecamp.org/news/content/images/2019/10/lint-fix-option.jpg)
_Résultats du lint - Option de correction_

Alors essayons ! Exécutons :

```
yarn lint --fix
```

Et devinez quoi, il ne nous donne maintenant qu'une seule erreur de linting.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/lint-with-one-error.jpg)
_Résultats du lint - 1 erreur_

Il s'avère qu'ESLint a pu corriger automatiquement notre problème de point-virgule, mais nous devons toujours ajouter `pageName` à nos `propTypes` de `Layout` manuellement, ce qui n'est pas trop difficile.

En l'exécutant une dernière fois et enfin plus rien ! Mais cette fois parce que tout a l'air bon.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/lint-with-nothing-happening-2.jpg)
_Résultats du lint - Aucune erreur_

## **Allez-y et écrivez du code désordonné !**

![Image](https://www.freecodecamp.org/news/content/images/2019/10/bruce-almighty-typing.gif)
_Bruce Almighty - Typing_

Je plaisante ? La bonne nouvelle ici, c'est que maintenant vous pouvez facilement jeter un coup d'œil à la santé générale de votre base de code ainsi que, espérons-le, corriger la plupart des problèmes automatiquement. Cela va éviter beaucoup de maux de tête lorsque vous travaillerez avec d'autres membres de votre équipe, et en général, c'est bien d'avoir tout votre code propre et bien rangé.

Cet article n'est qu'un début. ESLint est un livre grand ouvert avec des tonnes de plugins et de règles, et ce n'est pas le seul outil de linting dans le jeu. Amusez-vous et trouvez ce qui convient le mieux à vous et à votre équipe. Le peu de temps passé à le configurer pour votre application vous fera gagner beaucoup plus de temps à long terme.

## **Autres outils de linting à découvrir**

* [JSHint](https://jshint.com/) : une alternative à ESLint
* [Stylelint](https://github.com/stylelint/stylelint) : un outil de linting pour CSS et les syntaxes de type CSS comme [Sass](https://sass-lang.com/)
* [Awesome ESLint](https://github.com/dustinspecker/awesome-eslint) : une liste simple de configurations, parseurs, plugins et autres outils géniaux pour booster votre jeu ESLint
* [Webhint](https://webhint.io/) : outil de linting pour l'accessibilité, la vitesse et d'autres meilleures pratiques pour les sites web
* [Plugin A11y JSX](https://github.com/evcohen/eslint-plugin-jsx-a11y) : plugin ESLint pour vérifier les règles d'accessibilité sur les éléments JSX

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Follow Me On Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">? fe0f Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;"> 2709 fe0f Sign Up For My Newsletter</a>
    </li>
  </ul>
</div>

_Originalement publié_ à [https://www.colbyfayock.com/2019/10/what-is-linting-and-how-can-it-save-you-time](https://www.colbyfayock.com/2019/10/what-is-linting-and-how-can-it-save-you-time)