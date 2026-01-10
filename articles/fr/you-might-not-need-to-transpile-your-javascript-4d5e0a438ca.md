---
title: Vous n'avez peut-être pas besoin de transpiler votre JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-05-19T10:01:51.000Z'
originalURL: https://freecodecamp.org/news/you-might-not-need-to-transpile-your-javascript-4d5e0a438ca
coverImage: https://cdn-media-1.freecodecamp.org/images/1*dzbgLnjV6aUOoLKdJwsOBQ.png
tags:
- name: Ecmascript 6
  slug: ecmascript-6
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
seo_title: Vous n'avez peut-être pas besoin de transpiler votre JavaScript
seo_desc: 'By Alex Ewerlöf

  Popular guides like YouMightNotNeedJQuery.com and You Don’t Need Lodash/Underscore
  have challenged common industry practices.

  This post is not as wild as, say, YouMightNotNeedJS.com, but it does elaborate on
  transpilation, and explain...'
---

Par Alex Ewerlöf

Des guides populaires comme [YouMightNotNeedJQuery.com](http://youmightnotneedjquery.com/) et [You Don’t Need Lodash/Underscore](https://github.com/you-dont-need/You-Dont-Need-Lodash-Underscore) ont remis en question les pratiques courantes de l'industrie.

Cet article n'est pas aussi audacieux que, disons, [YouMightNotNeedJS.com](http://youmightnotneedjs.com/), mais il élabore sur la transpilation et explique pourquoi elle pourrait ne pas être aussi nécessaire dans un avenir proche.

[StatCounter](http://gs.statcounter.com/) collecte des données sur plus de 15 milliards de vues de pages chaque mois à partir de 2,5 millions de sites web [dans le monde](http://gs.statcounter.com/sample-size/StatCounterGlobalStatsSep15_SampleSizeCountryBreakdown.csv). En mai 2017, voici le statu quo :

![Image](https://cdn-media-1.freecodecamp.org/images/TZrOepsL1TtIBX43uaB2PiIu-vDty8-Ltqfv)
_Part de marché des navigateurs en mai 2017 en %_

Ce qui rend ce diagramme intéressant, c'est que les trois principaux navigateurs (Chrome, Safari et Firefox) sont [evergreen](https://www.techopedia.com/definition/31094/evergreen-browser), ce qui signifie que 74 % des utilisateurs reçoivent automatiquement la dernière version de leur navigateur.

Vérifions si cette hypothèse est correcte.

Voici les principales versions de navigateurs sur le marché :

![Image](https://cdn-media-1.freecodecamp.org/images/eU4BIDJlbf-VSRVGDULUnx6fCH1hv1YEFipp)
_Distribution des versions de navigateurs selon [StatCounter](http://gs.statcounter.com/browser-version-market-share/desktop-mobile-tablet/worldwide/#monthly-201705-201705-bar" rel="noopener" target="_blank" title=")_

Chrome 58 [a été publié](https://www.chromium.org/developers/calendar) il y a moins d'un mois et sa version desktop détient 12,77 % de la part de marché mondiale des navigateurs. Chrome 57 a été publié seulement 42 jours avant et sa version desktop détient 9,96 % de la part de marché mondiale des navigateurs. Malheureusement, StatCounter ne différencie pas les versions de Chrome sur les plateformes mobiles, mais en supposant le même ratio que sur desktop, nous obtenons :

![Image](https://cdn-media-1.freecodecamp.org/images/G-MrEu5ceKHMXLhHb6sFmEgR4aZgK-P1NghN)
_Toutes les versions de Chrome sur le marché (à_

### Que signifie-t-il pour mon code ?

Selon le [Tableau de compatibilité ES](http://kangax.github.io/compat-table/es6/), la dernière version de tous les principaux navigateurs prend très bien en charge les fonctionnalités ES6 :

![Image](https://cdn-media-1.freecodecamp.org/images/GT4ajFI0MK3anwfsK28WB5dz7sQa4PTQ2QI6)
_Tous les principaux navigateurs ont une très bonne prise en charge d'ES6_

En d'autres termes, si vous transpilez votre JavaScript en ES5, vous rendez votre code inutilement volumineux et lent pour supporter une minorité d'utilisateurs qui auront probablement mis à jour leur système d'ici à ce que vous ayez réussi à configurer votre Webpack et Babel ! 💡

### Pourquoi transpiler encore ?

Vous pourriez encore vouloir transpiler votre code, mais espérons-le après avoir pesé les pour et les contre ou les alternatives possibles :

* Vous utilisez React JSX (qui est assez populaire en ce moment, donc je suppose que beaucoup de développeurs entrent dans cette catégorie). JSX, à sa base, est une **transformation** de XHTML en code JS et n'a pas nécessairement besoin d'un transpileur complet comme Babel. De plus, si tout ce dont vous avez besoin est [VirtualDom](https://github.com/Matt-Esch/virtual-dom), utilisez cela à la place.
* Vous voulez essayer les dernières fonctionnalités du langage. À moins que vous ne fassiez partie de TC39 ou que vous n'ayez un désir brûlant d'injecter des fonctionnalités de langage instables dans votre code de production, vous êtes probablement satisfait avec ES6. De nos jours, nous avons un langage décent dans la majorité des navigateurs et le besoin de transpiler s'estompe.
* Vous utilisez TypeScript et avez espérons-le [pesé les pour et les contre](https://medium.freecodecamp.com/when-should-i-use-typescript-311cb5fe801b). Le compilateur TypeScript, lorsqu'il cible une version moderne d'ES6, supprime principalement les informations de type plutôt que de transformer la syntaxe.
* Vous voulez réduire la taille du code en utilisant [tree shaking](http://www.engineyard.com/blog/tree-shaking) (voici comment le faire [dans webpack](https://medium.freecodecamp.org/tree-shaking-es6-modules-in-webpack-2-1add6672f31b) et [rollup](https://rollupjs.org/#tree-shaking)). Vous voulez obfusquer votre code ou réduire sa taille par minification. Vous voulez exclure conditionnellement une partie du code. Cela nécessite une analyse statique du code. Vous pouvez utiliser un bundler intelligent pour les services de production sensibles à la taille comme les appareils mobiles, mais nous allons voir des évaluations de coûts plus prudentes lors de la création de tels déploiements alternatifs. _Ces types d'analyse statique de code continueront d'être utiles en tant que « techniques d'optimisation avancées » pour le code de production._ Vous n'avez **pas besoin** de minifier vos fichiers. UglifyJS ne peut pas minifier ES6 pour le moment (bien qu'une branche harmonie existe), mais [Babili](https://github.com/babel/babili) peut le faire. Les algorithmes de compression font un travail assez décent ([pas lorsque les fichiers sont trop petits](https://webmasters.stackexchange.com/questions/31750/what-is-recommended-minimum-object-size-for-gzip-performance-benefits)) et à moins que vous ne livriez un système d'exploitation à chaque chargement de page, cela devrait bien fonctionner sans compression. De nos jours, les images et le contenu multimédia prennent beaucoup plus de bande passante que le code.
* Vous voulez l'éléphant dans la pièce :

![Image](https://cdn-media-1.freecodecamp.org/images/gIZoxcr0gHTrWkeMFXmybvvyMpmRqhUOrtqp)

NPM est [le plus grand](https://www.linux.com/news/event/Nodejs/2016/state-union-npm) gestionnaire de paquets sur la planète. La plupart des applications web non triviales utilisent du code de NPM, ce qui implique l'utilisation d'un bundler de modules. Cela va bientôt changer ! Chrome supporte déjà les modules ES6 dans [Canary](https://www.chromestatus.com/feature/5365692190687232) (Chrome 60 livrera officiellement cette fonctionnalité en août) et Safari est [proche de le livrer](https://bugs.webkit.org/show_bug.cgi?id=147340) également, tandis que Firefox et Edge y travaillent.

De plus, [HTTP/2](https://en.wikipedia.org/wiki/HTTP/2) permet de pousser volontairement des ressources vers le navigateur. Cela signifie que si **a.js** importe **b.js** et **c.js**, le serveur peut pousser **b.js** et **c.js** chaque fois que **a.js** est récupéré, ce qui minimise le temps entre les requêtes. Cela est bien sûr une vue simplifiée car en pratique, le navigateur pourrait déjà avoir **b.js** et **c.js** dans son cache. HTTP/2 est [supporté dans la majorité des navigateurs](http://caniuse.com/#search=http2).

### L'avenir sans transpilation

Considérant les statistiques ci-dessus, cela signifie que 2018 sera l'année où la majorité des applications web pourront se débarrasser des bundlers de modules ou des transpileurs.

La transpilation est un contournement. Nous l'avons peut-être fait trop longtemps et nous nous y sommes habitués, mais réfléchissez-y. Nous « compilons » un langage « interprété » en un langage « interprété » ! De plus :

* Configurer Webpack/Browserify est une taxe inutile dans de nombreux cas
* Le débogage avec les sourcemaps est toujours plus difficile que le débogage du script réel en cours d'exécution (qui a aimé essayer de déboguer `this` ou des variables lorsque les sourcemaps ne fonctionnent pas correctement ?)
* Cela tue le DX lorsque vous devez attendre quelques secondes (parfois une demi-minute) après chaque modification pour voir le dernier code. Le rechargement de module à chaud (HMR) est une réponse à cela, mais ce n'est pas toujours fluide et rapide à configurer. Sans transpilation, tout ce que vous avez à faire est de rafraîchir la page et en moins d'une seconde, votre dernière page est là !

En août, lorsque les modules ES6 seront livrés, certains types d'applications n'utiliseront pas du tout la transpilation :

* Extensions Chrome
* Applications de bureau Electron
* Applications web B2B conçues pour être exécutées par des utilisateurs professionnels qui disposent déjà de bons équipements fournis par l'entreprise

Lorsque la transpilation deviendra une chose du passé, les [bibliothèques avec syntaxe Hyperscript](https://mithril.js.org/hyperscript.html) apporteront les idées de React à _POJS_ (Plain Old JavaScript qui n'est pas transpilé et facilement déboguable sur la console).

### Ne transpilez pas, mais compilez pour de vrai !

[WASM](http://webassembly.org/) est le nouveau venu et c'est la cible de compilation officielle qui promet une [vitesse d'exécution plus rapide et une taille de code plus petite](https://www.youtube.com/watch?v=HktWin_LPf4). [Actuellement](http://caniuse.com/#feat=wasm), Chrome et Firefox supportent WASM, mais il y a un bon consensus parmi les grands vendeurs de navigateurs que WASM va être le runtime commun de l'avenir. Si vous avez Chrome, vous pouvez [l'essayer](http://webassembly.org/demo/).

Si vous êtes le genre de développeur qui a envie de quelque chose de nouveau, jetez un coup d'œil à [Rust](https://doc.rust-lang.org/book/). Il [compile en WASM](https://hackernoon.com/compiling-rust-to-webassembly-guide-411066a69fde) mais n'est pas limité au web. Les gens l'utilisent réellement pour écrire un [système d'exploitation](https://github.com/redox-os/redox) ou un [moteur de navigateur](https://github.com/servo/servo). De plus, les anciens développeurs C/C++ [l'approuvent et l'aiment](https://www.quora.com/What-do-C-C++-systems-programmers-think-of-Rust) et il a une communauté très accueillante.

### Quelques notes

* Selon l'ancien CTO de Mozilla, [Chrome a gagné](https://andreasgal.com/2017/05/25/chrome-won/) et il est peu probable qu'il y ait une autre guerre des navigateurs. La chose intéressante est que **Chrome a gagné avec la méritocratie**. Il est open source et Google a clairement défini [quelles informations il collecte](https://www.google.com/chrome/browser/privacy/whitepaper.html) auprès des utilisateurs. Chrome gagne [même les utilisateurs professionnels](https://tech.slashdot.org/story/17/05/28/0243212/even-for-businesses-chrome-is-the-top-browser) qui utilisent traditionnellement Windows. Néanmoins, alors que les utilisateurs finaux choisissent Chrome pour sa vitesse, sa sécurité et sa simplicité, les programmeurs adorent ses outils de développement. Google joue un rôle actif dans le TC39 qui dirige l'avenir de JavaScript et est en général le plus grand défenseur de la plateforme web, même si elle peut concurrencer son propre système d'exploitation mobile. Non seulement cela, mais Google aide également ses concurrents. Google a été l'un des plus grands soutiens financiers de Mozilla et son [moteur de rendu](https://www.chromium.org/blink) est utilisé par Opera.
* [Microsoft a officiellement](https://www.quora.com/What-do-C-C++-systems-programmers-think-of-Rust) abandonné le support pour IE il y a environ 17 mois. IE 11 continuera à recevoir des mises à jour de sécurité jusqu'en 2025, mais c'est à vous de décider de dépenser [des ressources significatives](http://kangax.github.io/compat-table/es6/#ie11) pour supporter un navigateur que seulement 3,24 % du marché utilise. Gardez également à l'esprit que Edge est le navigateur par défaut dans Windows 10. Si quelqu'un ne veut pas mettre à jour son Windows vers la dernière version, la récente [attaque WannaCrypt](https://blogs.technet.microsoft.com/msrc/2017/05/12/customer-guidance-for-wannacrypt-attacks/) lui donne probablement une raison de reconsidérer ! Je suis personnellement intéressé par toute étude de marché sur les revenus provenant de ce segment particulier de clients.
* Apple a mis en place [un ensemble de restrictions injustes](https://www.howtogeek.com/184283/why-third-party-browsers-will-always-be-inferior-to-safari-on-iphone-and-ipad/) pour tenir les autres vendeurs de navigateurs à l'écart de leur plateforme iOS. Ainsi, par exemple, Chrome sur iOS est techniquement limité à des parties du moteur de Safari ! Safari [était le nouveau IE](https://www.safari-is-the-new-ie.com/), jusqu'à ce qu'en 2016, ils fassent du bon travail et deviennent le navigateur avec la meilleure prise en charge d'ES6 :

![Image](https://cdn-media-1.freecodecamp.org/images/ZNAu3gayDVFlzT-Whu4mK9SO8HKzkMAn5iRU)
_Sorti il y a 16 mois, Safari 10 a apporté un bon niveau de prise en charge d'ES6 sur les plateformes iOS_

Globalement, la part de marché mondiale d'iOS/Safari est inférieure à celle d'Android/Chrome. Cela varie selon les pays, par exemple, dans les pays riches, iOS a une pénétration un peu plus élevée, tandis que dans le monde en développement, Android est le grand gagnant, mais globalement, voici les statistiques :

![Image](https://cdn-media-1.freecodecamp.org/images/WspFnEK2JxT7FTBR6PnTJE9TFfAPUmpaI3dR)
_Part de marché mondiale des navigateurs pour Android et iOS_

### Appel à l'action !

Si vous êtes assez vieux, vous vous souvenez probablement des jours ennuyeux où certains sites web forçaient (ou suggéraient poliment) leur navigateur de choix (principalement IE) :

![Image](https://cdn-media-1.freecodecamp.org/images/wmZ3Ec-6JN8RWacSXNou-EfFnowE60D8-KKj)

Nous ne voulons pas faire cela ! Peu importe à quel point nous sommes excités par Chrome, nous ne voulons pas ignorer 46 % du trafic web qui n'est pas rendu par Chrome.

> Juste parce que nous pourrions avoir le support des modules ES6 dans les navigateurs bientôt, cela ne signifie pas que nous pouvons nous débarrasser d'un processus de build et d'une stratégie de « bundling » appropriée. — [Stefan Judis](https://www.contentful.com/blog/2017/04/04/es6-modules-support-lands-in-browsers-is-it-time-to-rethink-bundling/)

Nous aurons toujours des personnes coincées avec un ancien navigateur dans le firmware de leur TV ou dans le système d'infodivertissement de leur voiture. Nous aurons toujours ce grand-père obstiné qui ne voit pas la nécessité d'investir dans la mise à jour de sa machine pour en faire un héritage. Les enfants continueront à utiliser l'ancien iPhone ou la tablette de leurs parents et [1 ordinateur portable par enfant](http://one.laptop.org/about/hardware) ne gagnera pas en puissance de traitement du jour au lendemain. Nous ne voulons exclure personne.

Ce n'est pas un nouveau problème. Malgré le fait qu'ES6 soit l'un des plus grands changements sur le web, la [dégradation élégante](https://www.w3.org/wiki/Graceful_degradation_versus_progressive_enhancement) peut encore fournir une certaine utilité pour la **minorité** tout en gardant les coûts de développement sous contrôle pour la majorité.

Dans un futur article, je discuterai de l'aspect pratique de la livraison de code moderne tout en ayant un plan de secours pour une dégradation élégante. Vous pouvez me suivre sur Twitter ou Medium pour rester informé.

**BONUS :** Jetez un coup d'œil à [JS Codeshift](https://github.com/facebook/jscodeshift). Il s'agit d'un CLI pour convertir l'ancien code JavaScript en nouveau code JavaScript, mettant même à jour les anciens appels de bibliothèque JavaScript vers leur dernière API. Il essaie de préserver autant que possible le style original. Workflow : après avoir validé vos modifications dans le contrôle de version, exécutez cela et faites une comparaison approfondie et exécutez les tests automatisés et manuels. Terminé !

**Mise à jour 1 (2017-09-08) :** Chrome 61 est arrivé il y a quelques jours avec un support complet des modules ES6. Il détient 54 % du marché mondial des navigateurs. Safari (14 % du marché mondial) supporte les modules ES6 depuis un certain temps.

**Mise à jour 2 (2017-09-10) :** vous pouvez toujours supporter les navigateurs qui ne supportent pas les modules ES6 grâce à [cette astuce](https://medium.com/dev-channel/es6-modules-in-chrome-canary-m60-ba588dfb8ab7) _<scri**pt nomod**ule src="compiled.js"><_;/scri**_pt>._** L'attribut nomodule indique aux navigateurs avec support des modules ES6 de ne pas charger le script. Sur Safari, il y a quelques mises en garde que vous pouvez lire sur la page qui parle de [l'astuce. R](https://html.spec.whatwg.org/multipage/scripting.html#the-script-element)ead the spec.

**Mise à jour 3 (2017-09-12) :** [Le support des modules ES6 arrive dans les navigateurs : est-il temps de repenser le bundling ?](https://www.contentful.com/blog/2017/04/04/es6-modules-support-lands-in-browsers-is-it-time-to-rethink-bundling/)

**Mise à jour 4 (2017-09-12) :** les modules sont _defer_red par défaut. Si vous voulez contourner cela, ajoutez un attribut _async_ à la balise script pour éviter le [Single Point Of Failure (SPOF)](https://www.stevesouders.com/blog/2010/06/01/frontend-spof/).

**Mise à jour 5 (2017-09-13) :** Node LTS 8.5 [supporte les modules ES6](https://nodejs.org/en/blog/release/v8.5.0/) (appelés ESM) derrière un flag lorsque le fichier a une extension ***.msj**. Voici une [bonne introduction](http://2ality.com/2017/09/native-esm-node.html) sur la façon dont ils sont utilisés.

**Mise à jour 6 (2017-09-22) :** [ici](https://philipwalton.com/articles/deploying-es2015-code-in-production-today/) se trouvent quelques excellents conseils pratiques pour supporter à la fois les nouveaux et les anciens navigateurs. Les économies de bande passante pour éviter la transpilation sont formidables !

**Mise à jour 7 (2018-01-15) :** [Lebab](https://lebab.io/) (l'inverse de Babel) dispose d'un CLI pour moderniser l'ancien JavaScript. Cela est un peu similaire au [CodeShift](https://github.com/facebook/jscodeshift) de Facebook car ils modernisent tous deux l'ancien code.

Le bug le plus largement déployé dans l'histoire de l'informatique a ouvert une grande opportunité pour nous ! Lisez [Pourquoi devrions-nous convaincre nos utilisateurs de mettre à jour leurs navigateurs ?](https://medium.freecodecamp.org/should-we-demand-the-latest-browser-version-d5c72f8c9ffb)