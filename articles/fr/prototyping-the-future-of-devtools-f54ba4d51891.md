---
title: Prototypage du futur des DevTools
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-12T22:33:10.000Z'
originalURL: https://freecodecamp.org/news/prototyping-the-future-of-devtools-f54ba4d51891
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Q5pRPJHVNHQYpD-zgd5_Dg.png
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Prototypage du futur des DevTools
seo_desc: 'By Konrad Dzwinel

  12 years ago web development had almost no tooling. There was no easy way to inspect
  the DOM, monitor the network or even console.log things.


  Web development in 2002 — debugging with alerts. From “Pure JavaScript” (ISBN 0672321416)...'
---

Par Konrad Dzwinel

Il y a 12 ans, le développement web n'avait presque aucun outil. Il n'y avait aucun moyen facile d'inspecter le DOM, de surveiller le réseau ou même de faire un `console.log`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*cB6j0QtGioPdqeumSxJuiQ.png)
_Le développement web en 2002 — débogage avec des alertes. Extrait de « Pure JavaScript » (ISBN 0672321416)_

Ces temps sombres peuvent être résumés par cette citation de Joe Hewitt, créateur de Firebug et de l'API Console :

> « Je suis toujours surpris d'entendre les gens appeler FireBug 'innovant'. Cela montre à quel point la boîte à outils du développeur web est devenue faible, au point qu'une chose aussi ancienne qu'une console puisse être considérée comme novatrice. »

La création de [Firebug](https://getfirebug.com/) en 2006 a marqué le début de l'outil moderne de développement web. Aujourd'hui, chaque navigateur majeur est livré avec des outils intégrés fantastiques pour les développeurs web. Derrière chaque DevTools, il y a une équipe dédiée de développeurs, de designers et de chefs de produit qui le fait avancer.

Alors que les DevTools sont devenus importants, ils ont commencé à rivaliser les uns avec les autres et à acquérir des tonnes de nouvelles capacités tout en essayant de suivre l'évolution de la plateforme.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Q5pRPJHVNHQYpD-zgd5_Dg.png)
_Les DevTools de Firefox ont été les premiers à présenter un inspecteur de grille — [https://youtu.be/dU7xtnzfqxQ](https://youtu.be/dU7xtnzfqxQ" rel="noopener" target="_blank" title=")_

### L'héritage de Firebug

Je crois qu'aujourd'hui, nous avons la chance d'avoir l'un des meilleurs outils de l'industrie. En fait, nos outils sont devenus si bons qu'ils sont constamment forkés et adaptés pour fonctionner avec [d'autres plateformes](https://github.com/ChromeDevTools/awesome-chrome-devtools#using-devtools-frontend-with-other-targetsplatforms).

![Image](https://cdn-media-1.freecodecamp.org/images/1*NsHYFM3kMcrylPwM8h5xIQ.png)
_Stetho — un fork de Chrome DevTools pour le débogage des applications Android — [https://facebook.github.io/stetho/](https://facebook.github.io/stetho/" rel="noopener" target="_blank" title=")_

Une chose qui m'a toujours frappé, c'est la manière dont les concepts originaux introduits par Joe dans Firebug vivent encore, presque inchangés, dans les DevTools d'aujourd'hui.

![Image](https://cdn-media-1.freecodecamp.org/images/1*qrDenX2fHKTPYyITLPOP5A.png)
_Panneau Éléments dans Edge, Safari, Chrome et Firefox DevTools._

Ces similitudes facilitent certainement notre vie lorsque nous passons d'un navigateur à l'autre, mais je me suis toujours demandé — ces concepts ont-ils jamais été remis en question ? Ou ont-ils simplement été copiés sans beaucoup de réflexion ? Et s'ils l'ont été, puis-je les remettre en question moi-même ?

### Trouver l'inspiration

Motivé par l'invitation à parler à [Front-Trends](https://www.youtube.com/watch?v=dLRgZnNSQCM), j'ai décidé de construire quelques prototypes montrant quelques chemins alternatifs que nos outils pourraient suivre à l'avenir. À la recherche d'inspiration, j'ai pensé à me familiariser avec les applications utilisées dans d'autres professions. J'espérais identifier quelques modèles et idées à emprunter.

Parcourir les manuels d'outils aléatoires, sans comprendre le contexte, ne semblait pas être un bon plan. Heureusement, j'ai quelques bons amis qui ne sont pas développeurs web et qui ont accepté de me présenter leurs outils. J'ai donc rencontré : Kasia — une ingénieure en structure, Bolko — photographe et cinéaste, Ola — scientifique et conceptrice de systèmes de mesure et de contrôle, Kuba — concepteur de jeux et programmeur, et Patrycja qui est graphiste. Je leur ai demandé de me guider à travers leur flux de travail habituel, de parler de ce qu'ils aiment et n'aiment pas dans leurs outils et de la manière dont ils apprennent les nouvelles fonctionnalités.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8B5Yu6NmVCLUH9TZY9hLXg.jpeg)
_Mes amis au travail._

Ces entretiens ont apporté quelques idées intrigantes sur la manière dont les autres travaillent. Voici quelques-unes des idées que j'ai recueillies et qui pourraient être apportées aux DevTools des navigateurs.

### Imaginer l'avenir

#### Flexibilité

Toutes les applications que l'on m'a présentées (DaVinci Resolve, Autocad, Sketch, LabView, Unity) ont des mises en page beaucoup plus flexibles que nos DevTools. Chaque panneau, onglet et fenêtre peut être déplacé, fermé et redimensionné. C'est quelque chose qui aide à personnaliser l'outil et à l'adapter à vos besoins. Unity permet même de sauvegarder et de gérer plusieurs mises en page avec facilité. Pendant ce temps, dans nos DevTools, il est impossible d'avoir les panneaux Performance et Sources côte à côte.

Pour montrer à quoi ressemblerait une mise en page flexible dans Chrome DevTools, j'ai construit un prototype basé sur [golden-layout](http://golden-layout.com/) :

#### Construction à partir de blocs

Une chose que j'ai adorée dans Sketch et LabView, c'est la manière dont ils permettent de construire des blocs plus grands à partir de blocs plus petits. Dans Sketch, vous pouvez créer une bibliothèque de symboles (par exemple, boutons, étiquettes, entrées) à partir de laquelle vous pouvez ensuite construire une conception complète d'une page web. Si vous décidez de changer l'apparence d'un bouton, vous pouvez rapidement passer d'une vue « page web » à l'édition d'un « symbole » spécifique. Et lorsque vous avez terminé, tous les boutons de votre conception sont mis à jour en conséquence.

Si vous avez eu l'occasion de construire une application ou un site web en utilisant un framework moderne, tout ce discours sur les « symboles » a probablement sonné une cloche. Avec tant de nouvelles applications construites avec des composants web/react/etc., je crois que nous pourrions grandement améliorer nos DevTools en les faisant mieux comprendre ces concepts.

Pour montrer à quoi pourrait ressembler une meilleure intégration avec les composants, j'ai créé un prototype qui permet au développeur de passer facilement de la page/écran particulière à un composant unique :

#### Inspecteur contextuel

Unity dispose d'un outil d'inspection très pratique qui vous présente différentes options en fonction de l'élément inspecté (modèle 3D, fichier sonore, scène). Vous n'avez pas à changer d'outil chaque fois que vous passez de la modification d'un modèle 3D à la modification d'un fichier sonore — l'inspecteur s'adapte simplement en fonction du contexte.

Dans nos DevTools, nous obtenons le même panneau « Styles » quel que soit le nœud de l'arborescence DOM que nous inspectons actuellement. Pour certaines choses, comme une balise META, un chemin SVG, une balise script, etc., le panneau « Styles » n'est pas très utile, alors dans mon prochain prototype, j'ai essayé de remédier à cela :

#### Timeline

Lors de l'édition d'une vidéo, par exemple avec DaVinci Resolve, vous travaillez sur une timeline qui vous permet de sauter facilement entre différentes parties de votre projet. Cette facilité d'aller et venir m'a fait penser à quel point cette fonctionnalité serait incroyablement utile dans nos outils.

L'animation s'est terminée avant que vous n'ayez eu le temps de l'inspecter ? Vous avez cliqué sur « Suivant » dans le débogueur trop de fois et avez manqué le code que vous vouliez déboguer ? Pour l'instant, vous devez recharger la page et réessayer, mais avec un outil de timeline, ce serait un jeu d'enfant :

Si ce prototype vous semble un peu trop futuriste, vous devriez savoir que nous avons déjà fait un pas pour le rendre possible — le moteur JavaScript d'Edge supporte le [Time Travel Debugging](https://github.com/nodejs/node-chakracore#time-travel-debugging).

#### Toile infinie

Presque tous les outils que l'on m'a présentés implémentaient une idée de « toile infinie ». L'idée est de vous donner un espace sur lequel vous pouvez librement disposer vos dessins, designs, composants, etc. Et si vous voulez vous concentrer sur l'un de ces éléments, tout est à un défilement et un zoom de distance.

Un développeur travaillant sur un site web n'interagit définitivement pas avec lui de la même manière qu'un utilisateur régulier. Peut-être est-il temps de repenser comment la fenêtre principale du navigateur pourrait être améliorée pour mieux répondre aux besoins des développeurs. Je crois que l'idée de « toile infinie » s'intègre parfaitement ici. Et si vous pouviez garder plusieurs appareils, navigateurs et tailles d'écran tous sur la même toile ? Ce serait bien de pouvoir prévisualiser rapidement toutes les pages de votre application ? Et si vous abandonniez complètement les onglets du navigateur pour passer à la navigation par défilement et zoom ?

### Transformer les idées en réalité

Espérons que vous avez aimé certaines des idées présentées ci-dessus et que vous êtes d'accord avec moi pour dire qu'elles rendraient nos outils encore meilleurs. Je suis sûr que vous avez aussi quelques bonnes idées. Mais maintenant, que faire ? Devons-nous simplement attendre et espérer que ces idées soient mises en œuvre ?

Si vous ne voulez pas attendre, j'ai de bonnes nouvelles. Les DevTools de [Firefox](https://developer.mozilla.org/en-US/docs/Tools/Adding_a_panel_to_the_toolbox) et de [Chrome](https://developer.chrome.com/extensions/devtools) peuvent être facilement étendus via des extensions de navigateur. Il est également possible de contribuer directement aux [DevTools de Firefox](https://github.com/devtools-html/debugger.html), aux [DevTools de Chrome](https://docs.google.com/document/d/1WNF-KqRSzPLUUfZqQG5AFeU_Ll8TfWYcJasa_XGf7ro/) ou à l'[Inspecteur Web de Safari](https://webkit.org/blog/2518/state-of-web-inspector/#contributing), car ils sont tous open source. Enfin, si vous souhaitez créer un outil qui s'intègre à un navigateur mais qui en est séparé (comme [VS Code](https://code.visualstudio.com/blogs/2016/02/23/introducing-chrome-debugger-for-vs-code)), vous pouvez le construire sur la base du [Protocole DevTools](https://chromedevtools.github.io/devtools-protocol/). Pour plus d'inspiration et d'exemples de ce qui est possible, je vous suggère de consulter [awesome-chrome-devtools](https://github.com/ChromeDevTools/awesome-chrome-devtools).

_(Un grand merci à [Kenneth](https://twitter.com/auchenberg) Auchenberg, [Jonathan Garbee](https://twitter.com/JonGarbee), [Umar Hansa](https://twitter.com/umaar) et [Jason Laster](https://twitter.com/jasonlaster11) pour avoir révisé cet article)_