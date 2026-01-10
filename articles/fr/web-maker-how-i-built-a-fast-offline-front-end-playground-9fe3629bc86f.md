---
title: Web Maker — Comment j'ai construit un bac à sable front-end rapide et hors
  ligne
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-07-31T18:34:26.000Z'
originalURL: https://freecodecamp.org/news/web-maker-how-i-built-a-fast-offline-front-end-playground-9fe3629bc86f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*V5SvqQu7FekmKtIa0r4ZiQ.png
tags:
- name: Design
  slug: design
- name: open source
  slug: open-source
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Web Maker — Comment j'ai construit un bac à sable front-end rapide et hors
  ligne
seo_desc: 'By kushagra gour

  Web Maker is a Chrome extension that gives you a blazing fast and offline front-end
  playground — right inside your browser.

  It’s used daily by thousands of developers around the world and has a 5 star rating
  from 700+ users. It was a...'
---

Par kushagra gour

[Web Maker](https://webmakerapp.com/) est une extension Chrome qui vous offre un bac à sable front-end ultra-rapide et hors ligne — directement dans votre navigateur.

Il est utilisé quotidiennement par des milliers de développeurs à travers le monde et a une [note de 5 étoiles de la part de 700+ utilisateurs](https://chrome.google.com/webstore/detail/web-maker/lkfkkhfhhdkiemehlpkgjeojomhpccnh/reviews). C'était également une extension mise en avant sur la page d'accueil du Chrome Webstore, deux fois !

Vous pouvez utiliser Web Maker pour jouer avec HTML, CSS et JavaScript directement dans le navigateur sans aucun éditeur externe ou configuration spécifique. Vous pouvez utiliser des choses comme Angular, React, Sass, Babel, ou Atomic CSS — comme ça.

### Pourquoi j'ai créé Web Maker

Si vous êtes un développeur front-end, vous avez probablement essayé un ou plusieurs des bacs à sable de code disponibles — comme CodePen, JSBin, JSFiddle — pour résoudre des problèmes de code ou pour discuter de snippets et de morceaux de logique avec des collègues.

Ils sont tous excellents et font parfaitement le travail.

Mais j'ai toujours ressenti une légère friction à les utiliser sur Internet — il y a un délai inhérent entre leur démarrage et leur utilisation.

Je voulais aussi un moyen rapide de bidouiller des choses en voyageant ou en attendant à l'aéroport, où vous êtes principalement hors ligne. Je pourrais opter pour un éditeur traditionnel et un navigateur, mais cela nécessite un peu de configuration.

En y réfléchissant davantage, j'ai réalisé qu'il existe de nombreux endroits dans le monde avec une connectivité Internet limitée ou inexistante. Les personnes qui veulent apprendre et faire du développement web là-bas ne peuvent pas utiliser ces bacs à sable en ligne. Cela ne devrait pas les empêcher d'apprendre et de créer des choses !

J'ai essayé de chercher quelque chose qui pourrait me donner ce que je voulais, mais je n'ai rien trouvé. Et ainsi Web Maker est né.

### Comment j'ai créé Web Maker

La version initiale de Web Maker était très basique. Elle avait trois sections éditables (qui étaient des instances de CodeMirror) pour HTML, CSS et JavaScript. Chaque fois que le code était mis à jour, il était combiné en une chaîne HTML avec tout placé en ligne. Cette chaîne HTML était ensuite déposée dans un document iframe et rendue.

Ce processus a changé au fil du temps et de nombreuses fonctionnalités ont été ajoutées depuis. Il y a beaucoup de décisions intéressantes, de fonctionnalités, de morceaux de logique et de défis que je partagerai dans cet article.

### Extension Chrome — la plateforme de distribution ultime

Je voulais une plateforme de distribution très simple pour Web Maker puisque c'était en phase initiale. Je voulais aussi quelque chose avec une large portée, alors j'ai choisi d'en faire une extension Chrome.

Le Chrome Web Store est très facile à utiliser. Pousser une mise à jour est très simple et rapide. La plateforme d'extension Chrome offre également des capacités qui peuvent être exploitées pour des fonctionnalités intéressantes. Un exemple dans Web Maker est la capture d'écran de l'aperçu. Il utilise l'API `[captureVisibleTab](https://developer.chrome.com/extensions/tabs#method-captureVisibleTab)` pour capturer l'aperçu de l'iframe et ensuite l'API `[downloads](https://developer.chrome.com/extensions/downloads)` pour le télécharger pour vous avec un clic de bouton.

### Écrit en JavaScript et CSS vanilla

J'ai travaillé avec des frameworks JavaScript comme [Angular](https://angularjs.org/) et [Vue](https://vuejs.org/) dans des applications de petite et grande échelle. J'aurais pu utiliser l'un des frameworks disponibles ici aussi. Mais pour Web Maker, j'ai décidé d'utiliser du vanilla pour me challenger et voir jusqu'où je pouvais aller sans framework jusqu'à ce que la base de code devienne spaghetti. Je voulais utiliser toutes les connaissances que j'ai acquises en travaillant avec ces frameworks et bibliothèques pour garder le code sain, organisé et DRY.

Comme la plupart des projets, j'ai commencé avec un seul fichier JavaScript `script.js`. Pour garder la base de code modulaire et organisée, j'ai déplacé les gros morceaux indépendants dans des fichiers séparés au besoin (par exemple, [utils.js](https://github.com/chinchang/web-maker/blob/master/src/utils.js) et [dropdown.js](https://github.com/chinchang/web-maker/blob/master/src/dropdown.js)).

En plus de cela, j'ai également écrit un petit système de directives (comme dans Angular/Vue) qui me permet de faire des choses comme :

```
<a class="btn" d-click="someFunction">Button</a>
```

et

```
<input d-change="someOtherFunction">
```

_Note : Je ne pouvais pas utiliser de scripts en ligne comme `onclick` ou `onchange`. Ils ne sont pas autorisés dans les extensions Chrome en raison des restrictions de sécurité._

Pour le CSS également, Web Maker ne repose que sur les fonctionnalités fournies par le navigateur comme les variables CSS. Puisque j'ai développé Web Maker uniquement pour Chrome, je peux utiliser en toute sécurité les nouvelles fonctionnalités à venir sans me soucier de la compatibilité entre navigateurs — un autre avantage de la création d'une extension Chrome.

Je prévois de me pencher sur les [web components](https://www.webcomponents.org/) pour diviser l'interface utilisateur en composants indépendants.

### Génération de l'aperçu

Comme je l'ai mentionné précédemment, dans la première version de l'application, l'aperçu final était simplement une chaîne HTML qui avait le CSS de l'utilisateur comme balise de style en ligne et le JavaScript de l'utilisateur comme balise de script en ligne. Et cette chaîne HTML était écrite dans un fichier HTML temporaire qui se chargeait dans un iframe. Le fichier HTML ressemblait à quelque chose comme ceci :

```
<html> <head>  <style>   user CSS here...  </style> </head> <body>  user html here...  <script>user JS here...</script>  </body></html>
```

Mais en travaillant sur la version 2.0 de Web Maker, j'ai découvert que sur Chrome Canary (v57 à l'époque), l'aperçu n'exécutait plus le JavaScript de l'utilisateur. Après inspection, j'ai trouvé une erreur de politique Chrome dans la console de développement qui disait :

> Refused to execute inline script because it violates the following Content Security Policy directive…

Maintenant, je savais déjà que la Content Security Policy (CSP) ne me permettait pas de mettre des scripts en ligne dans le balisage d'une extension Chrome, et j'avais tout mon JavaScript dans des fichiers séparés. C'était différent. *À partir de Chrome 57, la CSP avait commencé à s'appliquer aux iframes d'aperçu également.* La solution était de déplacer le JavaScript de l'utilisateur de l'inline vers un fichier JavaScript séparé.

J'ai donc refactorisé la logique et maintenant, à chaque actualisation, le JavaScript de l'utilisateur est écrit dans un fichier JavaScript temporaire. Celui-ci est ensuite chargé dans l'iframe d'aperçu.

Notez que l'iframe d'aperçu n'est pas actualisé à chaque frappe dans l'éditeur. L'actualisation est [debounced](https://davidwalsh.name/javascript-debounce-function) sur l'entrée de l'utilisateur — donc l'aperçu n'est actualisé que lorsque l'utilisateur a arrêté de taper pendant une courte durée. Sinon, cela entraînerait de nombreuses actualisations inutiles pendant que l'utilisateur tape.

La mise à jour du CSS est un peu différente. Contrairement au HTML et au JavaScript où l'iframe complet est actualisé, le CSS est mis à jour chaque fois qu'il est édité dans la balise de style de l'iframe. Il n'y a pas d'écriture de fichier ou d'actualisation d'iframe impliqué. Par conséquent, pour le CSS, l'actualisation de l'aperçu est beaucoup plus rapide.

### Prévention des boucles infinies en JavaScript

Comme je l'ai mentionné ci-dessus, l'aperçu s'actualise dès que l'utilisateur arrête de taper. À ce stade, il est possible que l'utilisateur ait fait une pause en écrivant une boucle en JavaScript, résultant en une forme partielle. Quelque chose comme :

```
for (var i = 0; i<10; [user_cursor_here]) {}
```

La condition d'incrémentation/décrémentation est manquante dans ce JavaScript — donc si elle était placée dans l'iframe, l'onglet du navigateur serait bloqué ! De tels cas doivent être évités par tout bac à sable comme Web Maker.

Web Maker le fait en analysant le JavaScript de l'utilisateur et en modifiant toutes les boucles de sorte que chaque boucle vérifie continuellement si elle n'a pas pris trop de temps à s'exécuter.

En gros, ceci :

```
for (var i = 0; i<10; [user_cursor_here]) {}
```

est converti en :

```
var _wmloopvar1 = Date.now();for (var i = 0; i<10; [user_cursor_here]) { if (Date.now() - _wmloopvar1 > 1000) { break; }\}
```

Si nous passons plus d'une seconde dans une boucle, nous sortons.

J'utilise [Esprima](http://esprima.org/) pour toute cette instrumentation. Voici un [article de blog détaillé](https://kushagragour.in/blog/2017/02/web-maker-infinite-loop-prevention/) sur la façon dont c'est fait. Notez que la logique mentionnée dans l'article de blog a été récemment refactorisée pour être plus efficace, comme [suggéré](https://twitter.com/AriyaHidayat/status/832302074704523267) par l'auteur d'Esprima, Ariya Hidayat.

### Préprocesseurs

Comme la plupart des bacs à sable front-end, Web Maker offre de nombreux préprocesseurs pour chaque HTML, CSS et JavaScript.

L'ajout de tout préprocesseur dans l'application nécessite d'obtenir son transpileur (compilateur source-à-source) et de comprendre comment il transpile le code d'entrée. Vous devez également savoir qu'il affiche les erreurs de transpilation à côté de chaque ligne.

Maintenant, presque tous les bacs à sable en ligne transpilent votre code sur leur serveur. Mais Web Maker n'a pas de serveur — il réside dans votre navigateur et s'exécute dans votre navigateur.

De nombreux transpileurs sont conçus pour être exécutés uniquement dans un environnement NodeJS, donc j'ai fait un effort pour les bundler en code compatible avec le navigateur. Web Maker utilise des transpileurs comme [CoffeeScript](http://coffeescript.org/v1/browser-compiler/coffee-script.js), [SASS](https://github.com/medialize/sass.js/), et [Babel](https://github.com/babel/babel-standalone).

À chaque changement dans l'éditeur, le code de l'utilisateur est envoyé au transpileur approprié, puis le code transpilé est envoyé à la génération de l'aperçu. J'ai utilisé une API basée sur les Promesses pour transpiler le code pour deux raisons :

1. Le transpileur SASS n'est pas synchrone. Il utilise un worker pour convertir le code SASS en CSS sur un thread séparé.
2. Je pourrais déplacer d'autres transpileurs vers un worker séparé également. La compilation de source peut parfois prendre beaucoup de temps. Elle peut également entraîner des boucles infinies, bloquant le thread principal de l'interface utilisateur dans de tels cas. Il est donc préférable de les déplacer vers un worker séparé.

Par exemple, la fonction qui convertit JavaScript ressemble à ceci dans un sens large :

```
function computeJs() { var d = deferred(); if (jsMode === JsModes.COFFEESCRIPT) {    try {   code = CoffeeScript.compile(code, { bare: true });  } catch (e) {   showErrors(    'js',    [{ lineNumber: e.location.first_line, message: e.message }]   );     } finally {   d.resolve(code);  }}
```

### Stockage

La version 2.0 de Web Maker a été livrée avec une capacité très importante pour stocker les créations des utilisateurs.

J'ai décidé d'utiliser `localStorage`. Ainsi, même si vous travaillez sur une machine différente, vous pouvez sauvegarder tous vos paramètres Web Maker comme la taille de l'indentation, le thème, etc.

Il aurait été génial si même les créations étaient stockées dans un stockage synchronisé comme les paramètres de l'extension. De cette façon, elles seraient accessibles sur tous les appareils. Le stockage synchronisé vient avec un quota d'espace comparativement plus faible, cependant, et je ne voulais pas risquer le travail sauvegardé.

Vous pourrez peut-être sauvegarder tout votre travail sur le cloud dans les futures versions !

Web Maker offre également une option pour exporter et importer toutes les créations sauvegardées.

### Construit sur des technologies web ouvertes et des bibliothèques open-source

Web Maker est construit sur plusieurs bibliothèques open source et est lui-même [open source](https://github.com/chinchang/web-maker).

Les trois panneaux d'édition où vous tapez réellement le code sont construits avec [CodeMirror](https://codemirror.net/). CodeMirror vient avec de nombreux add-ons et modes, ce qui permet à Web Maker de supporter l'autocomplétion de code, le pliage de code, la coloration syntaxique et les thèmes.

Grâce à [Esprima](http://esprima.org/), vous pouvez voir des erreurs JavaScript génériques dans votre code au fur et à mesure que vous tapez dans l'éditeur. Comme je l'ai mentionné précédemment, Esprima aide également à prévenir les boucles infinies.

En plus de cela, Web Maker utilise [Split.js](https://nathancahill.github.io/Split.js/), [Hint.css](https://kushagragour.in/lab/hint/), [Emmet](https://emmet.io/), [Inlet.js](https://github.com/enjalot/Inlet), et même Web Maker ! Oui, Web Maker est fait dans Web Maker.

### Défis

Il y a eu de nombreux ralentissements pendant le développement, mais je voudrais parler de deux principaux.

Comme je l'ai mentionné, lorsque je travaillais sur la version 2.0, j'ai découvert un changement majeur dans Chrome 57 qui a rompu la capacité de mettre des scripts en ligne dans le balisage de l'extension.

Il y avait aussi une fonctionnalité livrée avec la version 2.0 qui permettait à l'utilisateur d'ajouter n'importe quel nombre de bibliothèques JavaScript ou CSS externes. Lorsque l'utilisateur entre une URL de bibliothèque JavaScript, elle est ajoutée comme une balise de script avec l'attribut `src` défini sur l'URL. La CSP de l'extension Chrome, en plus d'empêcher le JavaScript en ligne, restreint également le JavaScript de charger des domaines sauf ceux mentionnés dans la CSP — ce qui signifiait que l'utilisateur ne pourrait pas charger de JavaScript externe depuis n'importe quel domaine aléatoire.

Ceci est actuellement partiellement résolu en mettant sur liste blanche tous les principaux CDN dans le fichier `manifest.json`. Ce n'est toujours pas parfait car l'utilisateur ne peut pas charger de JavaScript depuis d'autres domaines.

Une autre grande chose qui m'a frappé était la fonctionnalité _Capture d'écran de l'aperçu_. Cette fonctionnalité permet à l'utilisateur de capturer une capture d'écran de l'aperçu actuel et de la télécharger en tant qu'image avec un clic de bouton. Cette fonctionnalité a nécessité l'ajout de deux permissions supplémentaires : `downloads` et `<all_urls>`.

`<all_urls>` est en fait une permission étrange, mais c'est un must si vous voulez utiliser l'API `[captureVisibleTab](https://developer.chrome.com/extensions/tabs#method-captureVisibleTab)`. Voici à quoi cela ressemble lors de l'installation de l'extension :

![Image](https://cdn-media-1.freecodecamp.org/images/iFNRxms5xGDbyN5bOZc1Zf7ivmxyK9TFax03)
_Boîte de dialogue des permissions lors de l'installation de Web Maker_

La première ligne est assez effrayante pour quiconque installe l'extension.

De plus, si vous ajoutez une nouvelle permission pour une nouvelle version d'une extension, Chrome désactive l'extension installée et affiche une popup indiquant que l'extension nécessite une nouvelle permission.

Cela a alarmé certains utilisateurs qui avaient déjà installé Web Maker. Beaucoup de personnes qui ont vu cette nouvelle permission demandée ne l'ont pas autorisée et l'ont désinstallée immédiatement.

Après cette version particulière, j'ai vu une forte augmentation du nombre de désinstallations.

La morale de l'histoire : Soyez prudent avec les permissions que vous ajoutez à votre application. Sauf si nécessaire pour le fonctionnement de base, optez toujours pour des permissions optionnelles dans l'application.

### Conclusion

Web Maker a parcouru un long chemin en termes d'utilisabilité, de fonctionnalités et d'adoption. Être rapide et hors ligne le rend utilisable dans un grand nombre de scénarios, de la réalisation d'expériences web dans un train/avion à l'enseignement d'une classe d'étudiants.

Web Maker peut également être utilisé par des professionnels et des débutants dans des zones où Internet est lent ou absent.

Et je suis sûr que [Web Maker](https://webmakerapp.com/) peut aider énormément les campeurs de [FreeCodeCamp](https://www.freecodecamp.com/) dans leurs apprentissages et pratiques.

De plus, Web Maker est [open-source](https://github.com/chinchang/web-maker), donc tout le monde est invité à suggérer et à implémenter des fonctionnalités qu'ils pensent rendre plus utile. Cela pourrait être votre première étape pour apprendre [un peu de JavaScript pratique](https://hackernoon.com/unconventional-way-of-learning-a-new-programming-language-e4d1f600342c) en contribuant.

Si vous avez des suggestions, des commentaires ou des questions, tweetez-les [@webmakerApp](https://twitter.com/webmakerApp). Je suis impatient d'entendre vos retours et votre expérience avec.

[Installez Web Maker](https://webmakerapp.com/) et essayez-le, et suivez [Web Maker](https://medium.com/web-maker) sur Medium pour des conseils, des astuces et des articles pratiques.