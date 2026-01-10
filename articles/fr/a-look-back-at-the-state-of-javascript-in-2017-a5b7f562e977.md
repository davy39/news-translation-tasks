---
title: Un regard sur l'état de JavaScript en 2017
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-06T23:01:51.000Z'
originalURL: https://freecodecamp.org/news/a-look-back-at-the-state-of-javascript-in-2017-a5b7f562e977
coverImage: https://cdn-media-1.freecodecamp.org/images/1*k7XARFeR0RqgZhY1p5w8uA.png
tags:
- name: Data Science
  slug: data-science
- name: JavaScript
  slug: javascript
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Un regard sur l'état de JavaScript en 2017
seo_desc: 'By Sacha Greif

  In advance of the 2017 State of JS survey results, our panel of experts looks back
  on the past year

  One of the highlights of last year’s State of JavaScript survey results was the
  great panel of experts we assembled to analyze the resu...'
---

Par Sacha Greif

#### En prévision des résultats de l'enquête State of JS 2017, notre panel d'experts revient sur l'année écoulée

L'un des points forts des [résultats de l'enquête State of JS de l'année dernière](http://stateofjs.com/2016/introduction/) était le formidable panel d'experts que nous avions rassemblé pour analyser les résultats.

Cette année, nous avons adopté une approche légèrement différente et décidé de laisser les données parler d'elles-mêmes.

Mais je voulais toujours savoir ce que nos anciens panélistes (ainsi que deux nouveaux invités spéciaux) avaient fait au cours des 12 derniers mois, alors je les ai contactés pour leur poser quelques questions sur leur année en JavaScript.

### Rencontrez les panélistes

![Image](https://cdn-media-1.freecodecamp.org/images/K5CmM7TSxE9wCaLCV7bVYoxsydT2Wfm2fGZM)

* [Michael Shilman](https://medium.com/@shilman): [Testing](http://2016.stateofjs.com/2016/testing/)
* [Jennifer Wong](http://mochimachine.org): [Build Tools](http://2016.stateofjs.com/2016/buildtools/)
* [Tom Coleman](https://twitter.com/tmeasday): [State Management](http://2016.stateofjs.com/2016/statemanagement/)
* [Michael Rambeau](https://michaelrambeau.com/): [Full-Stack Frameworks](http://2016.stateofjs.com/2016/fullstack/)
* Invité spécial #1: [Wes Bos](http://wesbos.com/)
* Invité spécial #2: [Raphaël Benitte](https://twitter.com/benitteraphael) (créateur de [Nivo](http://nivo.rocks/#/))

### En regardant ce que vous avez écrit l'année dernière, quelles sont vos réflexions sur l'évolution de ce domaine spécifique depuis ?

#### Michael Shilman

Parmi les choix de l'enquête de l'année dernière, Jest a explosé et a dépassé Jasmine en [téléchargements NPM](https://npm-stat.com/charts.html?package=jest&package=jasmine&package=mocha&from=2016-11-10&to=2017-11-10).

Jest supporte les tests de snapshot, j'ai vu beaucoup de gens utiliser les snapshots comme une alternative moins coûteuse aux tests unitaires pour les comportements d'entrée/sortie de base. Cela est particulièrement populaire dans le domaine de l'UI, avec [Storyshots](https://github.com/storybooks/storybook/tree/master/addons/storyshots), ainsi qu'un écosystème entier d'outils connexes tels que [Loki](https://loki.js.org/), [Percy](https://percy.io/), [Screener](https://screener.io/), et [Chromatic](https://blog.hichroma.com/introducing-chromatic-ui-testing-for-react-c5cc01a79aaa).

#### Jennifer Wong

L'enquête de l'année dernière a définitivement prédit certaines des tendances de 2017. Avec la popularité continue de tout ce qui est nouveau et brillant, il n'est pas surprenant que Webpack soit toujours aussi fort. Yarn ne faisait même pas partie de l'enquête l'année dernière, mais il a pris de l'ampleur depuis sa première version complète en septembre. Je suis curieuse de voir ce qui se passera alors que Yarn et npm se disputent le marché.

![Image](https://cdn-media-1.freecodecamp.org/images/kLs-tiPLuDxKrmiAz-wBbJfLHhn51uNYC66O)
_Yarn_

#### Tom Coleman

Je ne suis pas sûr qu'un véritable concurrent à Redux ait émergé, mais peut-être que dans la communauté, il y a eu un mouvement vers ce que le créateur Dan Abramov a toujours dit : « toutes les applications n'ont pas besoin de Redux, et dans de nombreux cas, cela apporte plus de complexité que cela n'en résout ».

Avec l'utilisation croissante des outils de gestion des données serveur, en particulier pour les données GraphQL (voir Apollo et Relay Modern), le besoin d'outils complexes de gestion des données côté client a probablement quelque peu diminué. Il sera intéressant de voir comment les mouvements de ces outils vers la prise en charge des données locales se dérouleront également.

### Quels nouveaux outils/bibliothèques/frameworks JavaScript intéressants avez-vous utilisés en 2017 ?

#### Michael Shilman

Ma plus grande découverte en matière de testing en 2017 a été [Cypress](https://www.cypress.io/) en tant qu'option OSS/commerciale très pratique pour les tests de bout en bout, bien que je trouve qu'il est encore un peu rugueux sur les bords.

De plus, je maintens [Storybook](https://storybook.js.org/), qui est l'outil de développement d'UI le plus populaire pour React, React Native et Vue.

#### Jennifer Wong

Nous sommes en train de transitionner une grande partie de notre code frontend au travail vers React, Redux, Webpack et Yarn. Cela a été une transition intéressante et compliquée, mais beaucoup de mains ont rendu le travail plus léger. Cela a été en partie motivé par la création d'un système de design partagé et d'une bibliothèque de composants.

#### Tom Coleman

[Prettier](https://github.com/prettier/prettier)! Je ne peux plus écrire de code, je suis tellement dépendant de cet outil. J'ai beaucoup utilisé [Jest](https://facebook.github.io/jest/) et j'en suis vraiment satisfait. Je me suis vraiment mis à [Storybook](https://storybook.js.org/) et je l'utilise de plus en plus (et j'ai commencé à aider à le maintenir!)

![Image](https://cdn-media-1.freecodecamp.org/images/cMbciVyeg0O2x9T1se7pt5TSnyrpvfUszl2b)
_Prettier_

Sinon, j'ai été très occupé à développer [Chromatic](https://blog.hichroma.com/introducing-chromatic-ui-testing-for-react-c5cc01a79aaa), un outil de test de régression visuelle pour Storybook. C'est vraiment excitant de voir certaines entreprises commencer à tester correctement leur frontend (nous inclus!)

#### Michael Rambeau

L'outil préféré que j'ai trouvé en 2017 était [Prettier](https://github.com/prettier/prettier). Il me fait gagner beaucoup de temps lorsque j'écris du code, car je ne m'inquiète plus de « styliser » mon code.

Je ne me soucie plus des tabulations ou des points-virgules... Il suffit de faire Ctrl S dans l'IDE et tout est bien formaté! De plus, cela réduit les frictions avec les autres membres de l'équipe lorsque nous travaillons sur la même base de code.

#### Wes Bos

Toutes sortes de choses! [date-fns](https://date-fns.org/) a remplacé mon utilisation de [moment.js](https://momentjs.com/). [Next.js](https://github.com/zeit/next.js/) a été important pour moi pour construire des applications React rendues côté serveur. J'ai également appris Apollo pour travailler avec GraphQL.

#### Raphaël Benitte

Travaillant à la fois sur plusieurs projets open-source et au travail, il est vraiment important de pouvoir améliorer l'automatisation. L'utilisation de Prettier, ESLint, Jest, [Validate-commit-msg](https://github.com/willsoto/validate-commit) avec [Lint-staged](https://github.com/okonet/lint-staged) a vraiment aidé dans ce domaine.

J'ai également construit [Nivo](http://nivo.rocks/#/), une bibliothèque de visualisation de données pour React.

![Image](https://cdn-media-1.freecodecamp.org/images/XnkZpYJWd70GlMZUC6YCMaTSDdSjYEYEx3wC)

Enfin, avec l'essor de Async/Await et son support natif dans Node.js, j'ai également essayé [Koa](http://koajs.com/). Bien que son écosystème soit plus restreint que celui d'Express, je l'ai trouvé facile à prendre en main, et si vous êtes familier avec Express, vous ne serez pas perdu.

### Si quelqu'un voulait apprendre JavaScript à partir de zéro aujourd'hui, quelles sont les 3 technologies que vous lui recommanderiez de se concentrer ?

#### Michael Shilman

* React pour l'UI.
* Webpack pour le build.
* Apollo pour le networking.

#### Jennifer Wong

N'importe quel framework, n'importe quel outil de build, et Node. Beaucoup de concepts se traduisent entre les frameworks et les outils de build, donc espérons que bien apprendre l'un peut aider à comprendre les autres. Si je devais choisir un de chaque, peut-être React et Webpack parce qu'ils sont tendance — et les technologies tendances se présentent bien aux gens de l'industrie.

#### Tom Coleman

Certainement React, bien que les autres frontends soient intéressants, la part d'esprit de React est devenue assez énorme ces jours-ci. Un must.

GraphQL, je pense que la plupart des développeurs frontend expérimentés reconnaissent que les problèmes qu'il résout sont assez universels, et c'est un plaisir de travailler avec.

![Image](https://cdn-media-1.freecodecamp.org/images/Zsu1hWoY6yMCBvOZ0cIGFBk-6pou6u4Hcgfk)
_GraphQL_

Storybook, je pense que construire à partir de composants et de leurs états est l'avenir du développement d'applications, et Storybook est l'outil leader pour le faire.

#### Michael Rambeau

* React, en tant que couche frontend
* Express, en tant que serveur backend
* Jest, en tant que solution de test pour le code frontend et backend.

#### Wes Bos

Si vous commencez tout juste à apprendre, vous avez besoin de petites victoires pour rester excité par le langage. Donc, je dirais qu'en plus des fondamentaux, apprenez l'API DOM, apprenez Async + Await, et apprenez une nouvelle API visuelle comme les animations web.

#### Raphaël Benitte

* Si vous êtes vraiment nouveau en JavaScript, commencez par les bases — et ES6, qui fait maintenant partie des bases.
* Évidemment, React pour construire des UIs
* [GraphQL](http://graphql.org/), qui devient mature et est maintenant utilisé par de grandes entreprises comme Facebook, GitHub, Twitter et [beaucoup d'autres](http://graphql.org/users/)...

### Quel est votre plus grand point de frustration avec JavaScript aujourd'hui ?

#### Michael Shilman

J'espère qu'une meilleure pratique et une bibliothèque de choix émergeront pour le CSS-in-JS. Bien qu'il y ait beaucoup de bons choix, cela reste fragmenté, et une grande partie du monde fait encore du CSS-in-CSS, donc beaucoup de confusion à moins que ce soit votre focus.

#### Jennifer Wong

Les changements constants. Au moment où j'apprends une nouvelle technologie, nous passons à la suivante. Aussi, arrêtez de voler mon CSS, JavaScript!

#### Tom Coleman

Webpack. Outil extraordinairement puissant qui se situe beaucoup trop loin sur le spectre de la « configuration sur la convention ».

Il est très difficile d'éviter d'avoir à apprendre ses intrications pour travailler sur des applications JS, mais souvent ce sont des détails dont vous ne devriez pas vraiment avoir à vous soucier. J'espère toujours que Meteor pourra regagner le trône comme la meilleure façon de construire une application JS moderne.

#### Michael Rambeau

Le manque de standard, le fait que vous ayez beaucoup de choses à considérer lorsque vous choisissez votre stack avant de commencer un nouveau projet. Mais les choses s'améliorent!

#### Wes Bos

`checking && checking.for && checking.for.nested && checking.for.nested.properties`. Je sais qu'il existe des fonctions utilitaires pour faire cela, mais il semble que nous pourrions obtenir cela dans le langage bientôt.

#### Raphaël Benitte

Il y a trop d'outils... Il est difficile de choisir le bon, et nous devons être vraiment prudents avec les tendances car elles peuvent évoluer très rapidement dans l'écosystème JS.

### À quoi vous réjouissez-vous le plus en 2018 dans l'écosystème JavaScript ?

#### Michael Shilman

Liste de souhaits (je ne sais pas si l'un de ces éléments se réalisera en 2018) :

* GraphQL atteint le niveau de commodité de Meteor pour la synchronisation des données.
* Universal (web/mobile) se stabilise et décolle pour React Native.
* Cypress ou un concurrent émerge pour les tests de bout en bout.

#### Jennifer Wong

Stabilisation. Je croise les doigts pour que la « stack » JavaScript et la communauté commencent à se calmer un peu, et que nous entrions dans une routine qui cause moins de perturbations.

#### Tom Coleman

La fin de Babel! J'aime Babel, mais avec Node 8, je n'ai presque plus besoin de Babel. C'est génial de travailler à nouveau si près de l'interpréteur.

Évidemment, les normes ES continueront d'avancer, mais avec les modules et async/await, beaucoup des coins plus frustrants de JS ont été résolus et de nombreux projets seront probablement satisfaits de la version JS livrée avec Node et **tous** les navigateurs modernes très bientôt!

#### Michael Rambeau

Je suis curieux de voir comment GraphQL va croître. Va-t-il devenir le nouveau standard lors de la publication d'une API?

#### Wes Bos

Maintenant que Node est stable et que tous les navigateurs ont Async+Await, je me réjouis à l'idée que les promesses natives deviennent courantes dans les frameworks, les bibliothèques utilitaires et le code que vous écrivez au quotidien.

#### Raphaël Benitte

La plupart des langages ont un outil de build dédié/préféré (par exemple, Maven pour Java). Bien que nous ayons beaucoup d'options en ce qui concerne JavaScript, ces solutions sont trop souvent dédiées au frontend. J'aimerais voir npm (ou Yarn) ajouter la prise en charge de fonctionnalités de base telles que la documentation, l'autocomplétion, les dépendances de scripts, etc. Sinon, je continuerai probablement à utiliser GNU Make.

Et celui-ci est assez controversé, mais nous avons vu que les gens sont vraiment intéressés par des solutions comme [TypeScript](https://www.typescriptlang.org/) (ou [Flow](https://flow.org/)). Node.js et les navigateurs ont fait un effort clair pour avancer plus vite, mais si vous voulez un typage statique, vous devrez toujours ajouter une autre phase de transpilation. Alors, pourquoi pas un JavaScript typé statiquement natif? Vous pouvez trouver une discussion sur le sujet [ici](https://esdiscuss.org/topic/es8-proposal-optional-static-typing).

### Conclusion

Il semble que notre panel soit d'accord sur au moins quelques points : React est un pari sûr, Prettier est un excellent outil, et oui, l'écosystème JavaScript est encore trop complexe...

Ce qui est exactement ce que nous avons essayé de résoudre en premier lieu lorsque nous avons fait cette enquête!

Nous lancerons notre site de résultats très bientôt. En fait, dans une semaine, le 12 décembre.

Nous organiserons un [livestream de lancement + Q&A](https://medium.com/@sachagreif/announcing-the-stateofjs-2017-launch-livestream-14e4aeeeec3a) afin que vous puissiez nous poser toutes les questions que vous voulez — ou simplement traîner! Et qui sait, nous pourrions même avoir des invités spéciaux qui passent... ;)

Si vous voulez savoir quand les résultats seront en ligne et recevoir une notification pour le hangout, vous pouvez [nous laisser votre email](http://stateofjs.com/) et nous vous tiendrons au courant.