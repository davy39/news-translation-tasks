---
title: Un flux de travail plus fluide — guides de style pour une meilleure conception
  et un meilleur développement
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-05-12T08:48:39.000Z'
originalURL: https://freecodecamp.org/news/a-more-seamless-workflow-style-guides-for-better-design-and-development-639fc55be28c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*cVX2sUbGosHSJkq8Ax2FiA.png
tags:
- name: Design
  slug: design
- name: Front-end Development
  slug: front-end-development
- name: user experience
  slug: user-experience
- name: UX
  slug: ux
- name: Web Development
  slug: web-development
seo_title: Un flux de travail plus fluide — guides de style pour une meilleure conception
  et un meilleur développement
seo_desc: 'By Ash Connolly

  Style guides can give many benefits to the entire workflow, from design right through
  to build.

  In short…

  During the design phase style guides encourage consistency in the visual identity
  and help keep the interface system as logical ...'
---

Par Ash Connolly

Les guides de style peuvent apporter de nombreux avantages à l'ensemble du flux de travail, de la conception à la construction.

#### En bref…

Pendant la phase de conception, les guides de style encouragent la cohérence de l'identité visuelle et aident à maintenir le système d'interface aussi logique que possible, ce qui améliore l'expérience utilisateur (UX).

Pendant la phase de développement, ils facilitent la transition de la conception au développement, car ils minimisent les erreurs de construction et encouragent les meilleures pratiques de développement modulaire.

De plus, les guides de style peuvent être convertis en « guides de style front-end vivants » qui rendent les mises à jour futures et la maintenance du site plus faciles grâce à une base de code plus propre, plus modulaire et plus structurée.

En bonus, le guide de style et le guide de style front-end vivant peuvent être utilisés comme livrable de projet et comme moyen de mieux communiquer l'identité de l'UI à votre équipe et à votre client.

#### Concevoir des interfaces

Lors de la conception d'une interface, celle-ci doit être cohérente et logique. Nous devons créer une taxonomie claire avec des affordances appropriées pour offrir la meilleure expérience utilisateur (UX). Ou plus simplement, **l'interface doit avoir du sens.**

Lorsque nous concevons une interface, nous ne concevons pas des pages ou des panneaux, nous créons un système de conception d'éléments et de composants qui seront utilisés dans diverses combinaisons. Si nous gardons cela à l'esprit, nous pouvons créer un système d'interface vraiment fluide et flexible.

Nous pouvons utiliser des guides de style pour abstraire et décomposer nos conceptions en éléments et composants modulaires et scalables, qui peuvent fonctionner ensemble pour former un système congruent.

Lorsque les interfaces ne sont pas considérées comme un système de conception, nous pouvons obtenir des interfaces désordonnées et incohérentes qui sont très déroutantes pour l'utilisateur :

#### **Qu'est-ce qu'un guide de style ?**

Un guide de style montre clairement comment tous les éléments et composants de l'interface doivent être représentés visuellement. C'est essentiellement une référence principale pour l'interface utilisateur (UI).

Il est utile de mentionner que les guides de style peuvent porter de nombreux noms, tels que [style tiles](http://styletil.es/), [interface inventories](http://bradfrost.com/blog/post/interface-inventory/) et [pattern libraries](https://boagworld.com/design/pattern-library/). Il y aura sans doute plusieurs nouveaux termes pour décrire un guide de style d'ici la publication de cet article de blog !

Voici un petit exemple du guide de style de Medium.com lors de son lancement ([tiré d'une étude de cas de Teehanlax](http://www.teehanlax.com/story/medium/)) :

![Image](https://cdn-media-1.freecodecamp.org/images/1*cVX2sUbGosHSJkq8Ax2FiA.png)
_Guide de style de Medium_

Comme vous pouvez le voir, il montre les divers éléments d'interface tels que les boutons, les menus déroulants, la hiérarchie typographique, les infobulles, la palette de couleurs, etc. D'un coup d'œil, vous obtenez instantanément un aperçu de l'identité visuelle de l'interface. Vous remarquerez peut-être que cela ne semble pas avoir tous les éléments d'interface utilisés sur leur site web, mais c'est un bon exemple.

Les guides de style sont essentiels pour maintenir la cohérence de l'identité visuelle d'une interface et ils peuvent être bénéfiques à la fois en interne, pour votre équipe, et en externe, pour toute personne travaillant avec votre marque ou votre interface.

Nous pouvons utiliser les principes de l'Atomic Design pour améliorer cette approche. [Atomic Design](http://patternlab.io/about.html) décompose cet axiome du système de conception et nous donne les principes de base pour rendre la création de systèmes de conception aussi claire et simple que possible.

#### **Qu'est-ce que l'Atomic Design ?**

« Atomic Design est une méthodologie utilisée pour construire des systèmes de conception web. »
— Brad Frost

L'Atomic Design commence de zéro. Il commence par la conception d'éléments de base comme les étiquettes de formulaire, les entrées, les paragraphes, les en-têtes et les boutons. Ensuite, des groupes d'éléments de base forment des composants, des groupes de composants forment des modèles et des groupes de modèles forment des pages.

Atomic Design en un GIF :


Le grand avantage de l'Atomic Design est que vous n'avez pas à le suivre à la lettre. Nous n'avons pas à donner aux éléments et composants des noms comme atomes et molécules, mais nous pouvons prendre ces principes de base et les appliquer à la conception d'un guide de style clair et concis.

#### **Pourquoi utiliser un guide de style ?**

Les guides de style nous offrent les avantages suivants :

* Encouragent les designers à penser à l'interface comme un système organique, scalable et flexible.
* Encouragent la cohérence de l'identité visuelle et aident à maintenir la taxonomie/système de l'interface aussi logique que possible, conduisant à une meilleure UX.
* Rendent la conception des interfaces plus méthodique et basée sur les composants.
* Aident à communiquer rapidement l'identité de l'interface aux autres membres de l'équipe ou à vos clients.
* Nous donnent une vue d'ensemble et facilitent la détection des éléments d'interface incongrus.
* Rendent très clair pour un développeur de commencer à construire.
* Bénéfiques pour les clients, à la fois comme livrable de projet et comme flux de communication.

> Globalement, si nous abordons la conception d'interface avec des guides de style à l'esprit, ils nous aideront à créer des interfaces cohérentes et plus conviviales, car ils rendent la conception plus méthodique et claire, ce qui conduira à une meilleure expérience pour les utilisateurs.

#### **Les designers font déjà cela**

Un bon designer pensera sans doute déjà aux interfaces de cette manière, cependant, l'utilisation d'un guide de style aide à mieux communiquer l'identité de l'interface et l'UX aux autres. Le designer peut savoir pourquoi une certaine couleur est utilisée pour certaines actions de bouton, mais cela ne sert pas à grand-chose si personne d'autre ne sait pourquoi. Avoir un guide de style aide les autres à mieux comprendre l'UI et la logique utilisée par le designer.

#### **Les guides de style ne prennent pas plus de temps**

Il faut très peu de temps pour créer un guide de style. Un bon designer aura déjà résolu les problèmes d'interface, établi une hiérarchie des éléments et leur utilisation, donc déplacer ces éléments dans un guide de style prend peu de temps. Même pour les plus petits projets, les guides de style peuvent être bénéfiques.

#### **Comment les guides de style comblent-ils l'écart entre la conception et le développement front-end ?**

Lorsque qu'un développeur reçoit une conception web ou une application à construire, il est souvent fourni avec des fichiers de conception contenant des conceptions de pages du site web ou de l'application. Il doit interpréter cette conception, analyser et planifier la construction de manière approfondie, identifier les éléments et composants de l'interface, tenter de comprendre la taxonomie de l'UI. **Essentiellement, tenter de comprendre le système de conception.**

#### **Mais, le designer n'a-t-il pas déjà fait cela ?**

Idéalement, le designer aura abordé la conception avec tous ces éléments d'interface à l'esprit. Il aura déjà déterminé à quoi ressemble un appel à l'action principal, quelles couleurs doivent être utilisées pour des types spécifiques d'actions de bouton, quels changements de taille de police se produisent à différentes tailles d'écran, et comment les mises en page changent pour les composants à différentes tailles d'écran.

Si le développeur doit analyser et interpréter l'interface, alors du temps est perdu. De plus, des erreurs peuvent être commises et des nuances peuvent être manquées lorsque le développeur essaie de comprendre la conception.

> Consciemment ou non, le designer aura déjà créé le système de conception que le développeur essaie de construire, et ce système de conception doit être communiqué clairement.

Je suis sûr que chaque développeur a construit un composant pour que le designer mentionne ensuite que ce n'est pas ainsi qu'il était censé fonctionner ou se comporter. Les guides de style aident à améliorer la communication de l'interface et à éviter les erreurs pendant le processus de construction.

#### **Comment les guides de style aident-ils le développement front-end ?**

L'utilisation de guides de style pendant la phase de conception rationalise la transition vers la construction. Idéalement, les designers et les développeurs devraient communiquer régulièrement, cependant, si un designer peut remettre un guide de style clairement conçu, pour un nouveau site web ou une nouvelle application, à un développeur, celui-ci peut alors voir rapidement tous les éléments de base et les composants. Ils peuvent ensuite construire rapidement et méthodiquement avec aussi peu de confusion ou d'incertitude que possible.

Les guides de style fonctionnent de manière transparente avec les directives front-end modernes et les structures CSS basées sur les composants, telles que [BEM](http://bem.it/), [CSS guidelines](http://cssguidelin.es/) et [Inverted Triangle CSS](http://www.creativebloq.com/web-design/manage-large-scale-web-projects-new-css-architecture-itcss-41514731), car ils partagent les mêmes principes — d'abord construire ou concevoir des éléments de base, puis construire ou concevoir des composants plus complexes et réutilisables.

Cela signifie que notre guide de style peut être transféré facilement en CSS propre, modulaire et basé sur les composants !

![Image](https://cdn-media-1.freecodecamp.org/images/1*beC-XLTSrvfcFRX29EW9qg.gif)
_Comme un gant !_

À ce stade, tout ce que le développeur a à faire est de construire le guide de style en HTML et CSS, créant un **guide de style front-end.**

Voici quelques exemples de guides de style front-end :  
[Codepen](http://codepen.io/guide)   
[Code For America by Clearleft](http://codeforamerica.clearleft.com/)  
[Mozilla Firefox](https://www.mozilla.org/en-US/styleguide/websites/sandstone/buttons/)

#### **Un petit problème…**

Maintenir la cohérence du guide de style front-end avec le code utilisé sur le site web en direct peut être délicat. Si nous devons mettre à jour le balisage d'un composant, et que ce composant existe dans le guide de style front-end et sur le site web, **en tant que morceaux de code entièrement séparés**, nous créons plus de travail pour nous-mêmes. En conséquence, le guide de style front-end pourrait être négligé, ne pas être mis à jour comme il se doit et tomber en désuétude.

Nous pouvons résoudre ce problème en utilisant des modèles de balisage avec des outils comme [handlebars](http://handlebarsjs.com/), [dust.js](http://www.dustjs.com/), ou [twig](http://twig.sensiolabs.org/). Ces outils nous permettent de produire du balisage où nous le souhaitons, mais ils sont toujours liés à une seule source. **Cela nous permet de créer un guide de style front-end _vivant_.**

#### **Guides de style front-end vivants**

Un guide de style front-end vivant est identique à un guide de style front-end, mais les éléments et composants qu'il affiche sont une représentation exacte de ce qui est utilisé, ou sera utilisé sur les pages du site web ou de l'application en direct.

Si je devais mettre à jour un élément de bouton en changeant son balisage ou son CSS, ce changement serait reflété instantanément sur le site web ou l'application.

#### **Pourquoi utiliser un guide de style front-end vivant en développement ?**

Nous pouvons voir les avantages des guides de style pendant la phase de conception, mais pourquoi créer une version **« vivante »** en code de notre guide de style, pourquoi créer un guide de style front-end vivant ? Ils aident de la manière suivante :

* Rendent la construction de sites web plus méthodique et basée sur les composants.
* Encouragent le CSS modulaire et basé sur les composants pour une base de code plus propre, donc plus rapide.
* Facilitent les tests de réactivité et le débogage général.
* Nous permettent d'utiliser les principes de l'Atomic Design en développement.
* Modularisent le code, ce qui facilite la réutilisation du balisage et du CSS sur d'autres projets.
* Avoir tous les éléments d'interface « vivants » sur une seule page facilite les mises à jour et les reconceptions.
* Permet d'identifier facilement et rapidement les incohérences de l'interface.
* Nous permet de vérifier que tous les composants peuvent fonctionner ensemble sur une seule page sans aucun conflit de code.
* Fournit une page principale pour le balisage et la référence de l'interface utilisateur.
* Peut être utilisé comme livrable pour le client et le projet.

En bonus, les guides de style front-end peuvent parfois aider les designers non familiarisés avec le code à commencer à voir comment ils pourraient commencer à coder.

#### **Conclusion — flux de travail basé sur les guides de style**

Les guides de style et les guides de style vivants ont aidé à rationaliser et à concentrer mon flux de travail.

Pendant la phase de conception, ils aident à identifier les incohérences de l'interface et à me rappeler que les interfaces sont des systèmes de conception flexibles. Pendant la transition de la conception au développement, ils aident à minimiser les erreurs et à accélérer la remise. À la phase de développement, les guides de style peuvent être intégrés en HTML et CSS de manière transparente, car ils partagent des principes majeurs avec les directives front-end et les structures CSS basées sur les composants. L'utilisation de guides de style vivants rend ensuite les mises à jour et les reconceptions aussi faciles et gérables que possible.

Espérons qu'un flux de travail basé sur les guides de style puisse également vous être bénéfique, mais comme toujours avec tout ce qui concerne le web et la conception, il existe mille façons d'aborder un projet. Si vous avez trouvé un flux de travail qui fonctionne pour vous, continuez à l'utiliser !

**Liens supplémentaires :**  
[Sales Force — Lightning Design System](https://www.lightningdesignsystem.com/)  
[Anna Debenham — Style Guides](http://styleguides.io/)   
[Samantha Warren — Styletiles](http://styletil.es/)  
[Brad Frost — Patternlab](http://patternlab.io/)

Si vous souhaitez en savoir plus sur les guides de style et le développement front-end, n'hésitez pas à [me suivre sur Twitter !](https://twitter.com/AshConnnolly) ?