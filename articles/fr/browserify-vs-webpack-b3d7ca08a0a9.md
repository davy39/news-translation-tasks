---
title: Browserify vs Webpack
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2015-07-27T13:11:47.000Z'
originalURL: https://freecodecamp.org/news/browserify-vs-webpack-b3d7ca08a0a9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*YW70wmIr2R3tb5Xtec2giw.jpeg
tags:
- name: browserify
  slug: browserify
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
- name: webpack
  slug: webpack
seo_title: Browserify vs Webpack
seo_desc: 'By Cory House

  If you need a cabin, why start

  with a mere pile of logs?


  In the land of JavaScript, no one is king for long.


  Just last year Grunt was effectively dethroned by Gulp. And now, just as Gulp and
  Browserify are finally reaching critical ma...'
---

Par Cory House

#### _Si vous avez besoin d'une cabane, pourquoi commencer_  
_avec un simple tas de bûches ?_

> Dans le monde de JavaScript, personne ne reste roi très longtemps.

L'année dernière, [Grunt](http://www.gruntjs.com) a été effectivement destitué par [Gulp](http://gulpjs.com/). Et maintenant, alors que Gulp et [Browserify](http://browserify.org/) atteignent enfin une masse critique, [Webpack](http://webpack.github.io/) menace de les déplacer tous les deux. Y a-t-il vraiment une raison convaincante de changer votre processus de construction front-end _encore une fois_ ?

Considérons les mérites de chaque approche.

### Browserify (et ses amis...)

Browserify est conceptuellement simple. Hé, voyez tous ces packages sympas sur [npm](http://npmjs.org) ? Laissez-moi les envelopper pour vous afin que vous puissiez les utiliser dans le navigateur. Pratique. Merci Browserify ! Pourtant, cette simplicité est aussi son talon d'Achille. Il y a de fortes chances que vous ayez une longue liste d'autres choses à faire comme la minification, le bundling, le linting, l'exécution de tests, etc.

Bien sûr, Browserify dispose d'un [riche écosystème de transforms](https://github.com/substack/node-browserify/wiki/list-of-transforms) pour vous aider à accomplir ces tâches. Mais pour tout configurer, vous êtes seul. Vous allez donc vous tourner vers un outil d'automatisation de construction JavaScript comme Grunt ou Gulp. Ces outils fonctionnent très bien, mais les configurer correctement est un processus qui prend du temps. Après avoir travaillé avec Grunt ou Gulp pendant un certain temps, vous commencez à réaliser une longue liste de choses que vous faites pour chaque projet. Ne serait-il pas agréable de commencer avec un outil plus puissant et plus opinionné qui ferait plus d'hypothèses sur votre processus de construction ?

Si vous pensez à votre processus de construction comme à une cabane en bois unique, alors Browserify avec Gulp/Grunt est comme commencer ici :

![Image](https://cdn-media-1.freecodecamp.org/images/1*E_cgh1eE6GAtWWMkQRc-3Q.jpeg)
_Un certain assemblage est requis._

### Webpack

Webpack aborde le problème de construction de manière fondamentalement plus intégrée et plus opinionnée. Dans Browserify, vous utilisez Gulp/Grunt et une longue liste de transforms et de plugins pour accomplir le travail. **Webpack offre suffisamment de puissance dès la sortie de la boîte pour que vous n'ayez généralement pas besoin de Grunt ou Gulp du tout**. Oui, désolé, cette nouvelle compétence brillante que vous venez de maîtriser est déjà presque inutile. Uh... youpi ? Soupir. Bienvenue dans la vie du développement front-end.

Mais bon, c'est le prix du progrès. Avec Webpack, vous pouvez déclarer un simple fichier de configuration pour définir votre processus de construction. Woah, un fichier de configuration ? Oui, si vous êtes passé de Grunt à Gulp parce que vous préférez le code à la configuration, cela peut sembler un pas en arrière. Mais la configuration n'est pas nécessairement une mauvaise chose.

> Les systèmes basés sur la configuration sont préférables aux systèmes impératifs s'ils font les bonnes hypothèses sur vos objectifs dès le départ.

Je trouve que Webpack fait exactement cela. Webpack suppose que vous devez déplacer des fichiers d'un répertoire source vers un répertoire de destination. Il suppose que vous voulez travailler avec des bibliothèques JavaScript dans divers formats de modules comme CommonJS et AMD. Il suppose que vous voudrez compiler divers formats en utilisant une [longue liste de loaders](https://www.npmjs.com/search?q=webpack+loader). Bien sûr, vous pouvez faire tout cela via Browserify et Gulp, mais vous devez faire plus de câblage vous-même. Et vous câblez manuellement deux technologies totalement séparées.

La nature intégrée de Webpack brille vraiment lorsque vous considérez les histoires de travail avec d'autres actifs comme les images et le CSS. Webpack est assez intelligent pour intégrer dynamiquement votre [CSS](http://webpack.github.io/docs/stylesheets.html) et vos [images](https://github.com/webpack/url-loader) lorsque cela a du sens. Vous pouvez simplement inclure ces actifs comme vous le faites avec JavaScript aujourd'hui. Vous voulez utiliser du CSS ? Facile :

```
require("./stylesheet.css");
```

Hein ? Pourquoi ne pas simplement référencer le CSS à l'ancienne ? Eh bien, Webpack va considérer la taille de ce fichier. **S'il est petit, il va intégrer la feuille de style !** S'il est long, il va minifier le fichier et lui donner un nom unique pour le cache busting. Cette même histoire fonctionne également pour les [images](https://github.com/webpack/url-loader) en utilisant le plugin url loader.

```js
img.src = require('glyph.png');
```

Webpack va encoder cette image en base64 si elle est suffisamment petite pour que cela ait du sens. Génial !

Puisque Webpack est totalement conscient de votre processus de construction, il peut [diviser intelligemment vos ressources en bundles](http://webpack.github.io/docs/code-splitting.html). Cela s'avère utile pour les SPAs plus grandes. Vos utilisateurs ne recevront que les fichiers dont ils ont besoin pour une page donnée au lieu d'un seul fichier JavaScript monolithique.

Enfin, si vous souhaitez profiter d'un développement rapide d'applications sans actualisation du navigateur, Webpack offre un [remplacement de module à chaud](http://webpack.github.io/docs/hot-module-replacement.html). Si vous travaillez avec React, vous pouvez utiliser [React Hot Loader](https://github.com/gaearon/react-hot-loader). Oui, [Browserify a un équivalent](https://github.com/milankinen/livereactload), mais selon mon expérience, l'implémentation de Webpack par [@dan_abromov](http://www.twitter.com/dan_abramov) est supérieure. Croyez-moi, une fois que vous aurez expérimenté le développement d'applications avec un retour rapide comme celui-ci, vous ne reviendrez jamais en arrière :

%[https://www.youtube.com/watch?v=xsSnOQynTHs]

Webpack suppose que vous voulez construire une cabane en bois. Vous commencez donc avec une vraie cabane, et il vous donne les outils nécessaires pour l'ajuster à vos besoins.

![Image](https://cdn-media-1.freecodecamp.org/images/1*YW70wmIr2R3tb5Xtec2giw.jpeg)
_Pourquoi ne pas commencer ici et ajuster quelques petites choses qui vous rendent unique ?_

### Conclusion

Si vous préférez configurer explicitement de petits outils à usage unique à partir de zéro, alors Browserify avec Gulp/Grunt sera plus votre style. Browserify est plus facile à comprendre initialement puisque la surface conceptuelle est beaucoup plus petite — en supposant que vous connaissiez déjà Gulp ou Grunt. Lorsque vous utilisez Gulp avec Browserify, le processus de construction résultant peut être plus facile à comprendre que le processus de construction équivalent de Webpack. Il est souvent plus explicite sur les intentions. Le riche écosystème de plugins de Browserify signifie que vous pouvez accomplir à peu près n'importe quoi avec suffisamment de câblage. Ah, le câblage. C'est le gros inconvénient. Être aussi explicite prend beaucoup de temps et de débogage pour être fait correctement. J'ai récemment créé un [kit de démarrage](https://github.com/coryhouse/react-flux-starter-kit) pour mon prochain cours Pluralsight sur React et Flux. Il intègre certaines technologies spécifiques à React, mais supprimer ces dépendances est trivial si vous cherchez simplement un moyen rapide de vous lancer avec Browserify et Gulp.

Mais si vous êtes à l'aise avec un peu de "magie" via un outil plus opinionné, alors Webpack peut réduire le temps nécessaire pour mettre en place un processus de construction robuste. J'ai constaté que mes configurations Webpack sont généralement environ la moitié de la taille du fichier Gulp équivalent. Le gain n'est pas seulement moins de frappe — cela se traduit également par moins de temps passé à déboguer votre configuration.

Les fichiers Grunt massifs ont découragé beaucoup de gens de l'idée de configuration. Mais l'échec de Grunt n'était pas la configuration. C'était un manque d'opinion. **La configuration n'est pas mauvaise.** C'est un gain de temps puissant lorsque les hypothèses sont correctes.

> L'outil de construction ne devrait pas nécessiter une construction personnalisée à partir de zéro. Il devrait fournir des points de personnalisation qui vous permettent de gérer les quelques choses qui vous rendent vraiment unique.

### Prêt à creuser plus profond ?

La [documentation mise à jour de Webpack](https://webpack.js.org) est excellente, mais je suggère de lire [l'excellente introduction de Pete Hunt](https://github.com/petehunt/webpack-howto) à la place. Ensuite, consultez « [Création d'un environnement de développement JavaScript](https://app.pluralsight.com/library/courses/javascript-development-environment) » sur Pluralsight ([essai gratuit](https://billing.pluralsight.com/individual/checkout/account-details?sku=IND-Y-PLUS-FT)) pour voir un environnement de développement complet construit à partir de zéro en utilisant Webpack.

Vous utilisez React ? Consultez « [Construction d'applications avec React et Redux en ES6](https://app.pluralsight.com/library/courses/react-redux-react-router-es6) ».

Participez à la discussion sur [Hacker News](https://news.ycombinator.com/item?id=9954973) ou [Reddit](https://www.reddit.com/r/javascript/comments/3erss1/browserify_vs_webpack/)

[Cory House](https://twitter.com/housecor) est l'auteur de [plusieurs cours sur JavaScript, React, le code propre, .NET, et plus encore sur Pluralsight](http://pluralsight.com/author/cory-house). Il est consultant principal chez [reactjsconsulting.com](http://www.reactjsconsulting.com), architecte logiciel chez VinSolutions, un MVP Microsoft, et forme des développeurs logiciels à l'international sur des pratiques logicielles comme le développement front-end et le code propre. Cory tweete sur JavaScript et le développement front-end sur Twitter en tant que [@housecor](http://www.twitter.com/housecor).