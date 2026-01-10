---
title: Ce que j'ai appris à React Europe 2017
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-05-23T13:56:01.000Z'
originalURL: https://freecodecamp.org/news/what-ive-learned-from-react-europe-2017-c433468890d6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*LI8kcoWrhCJUoAXdqz6vaQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: React Native
  slug: react-native
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Ce que j'ai appris à React Europe 2017
seo_desc: 'By Nicolas Cuillery

  Few days ago, the 3rd edition of the biggest React conference in Europe took place
  in Paris. No heatwave or transportation strike this year — only great talks and
  interesting people.

  Here is my feedback from my most appreciated ta...'
---

Par Nicolas Cuillery

Il y a quelques jours, la 3ème édition de la plus grande conférence React en Europe a eu lieu à Paris. Pas de canicule ni de grève des transports cette année — seulement de grandes conférences et des personnes intéressantes.

Voici mon retour sur les conférences que j'ai le plus appréciées lors de cette édition.

En parlant de personnes intéressantes, je voudrais remercier chaleureusement [Griffith](https://www.freecodecamp.org/news/what-ive-learned-from-react-europe-2017-c433468890d6/undefined) Tchen Pan, que je viens de rencontrer parmi le public, pour sa relecture de cet article, ainsi que mes coéquipiers chez [M6 Web](http://tech.m6web.fr/).

### Conférence d'ouverture

Ceux qui sont venus spécialement pour entendre des nouvelles et des mises à jour sur React ont pu être satisfaits : [Andrew Clark](https://www.freecodecamp.org/news/what-ive-learned-from-react-europe-2017-c433468890d6/undefined) a ouvert la conférence avec la feuille de route pour React. Toutes ces mises à jour peuvent être résumées en un seul nom : React Fiber.

Andrew a illustré React Fiber avec une analyse de performance du streaming vidéo dans le fil d'actualité. Ils ont dû faire face à de mauvaises performances causées par d'autres tâches bloquant le thread JS principal. C'était un problème de planification, résolu en divisant l'exécution des tâches : le thread principal est capable de traiter des morceaux au fur et à mesure qu'ils arrivent, de sorte que les vidéos ne sont plus interrompues. L'idée derrière React Fiber est de planifier ces tâches au niveau des composants via le rendu asynchrone.

Arrivant dans React 16, la refonte inclura également des fragments (groupe de composants frères, plus de wrapper div, il suffit de retourner un tableau dans la fonction de rendu). Une meilleure gestion des erreurs sera également livrée avec des limites d'erreur (c'est-à-dire try/catch pour les composants) et une distinction des erreurs critiques des autres. En cas d'erreur critique, le composant sera démonté pour éviter une UI dégradée, des données corrompues...

React 16 est déjà en production, prêt à être installé avec le tag _next_ :

`yarn add react@next`

Au-delà de React 16, la planification de rendu améliorée permet au rendu d'être priorisé, en fonction de la position dans la fenêtre d'affichage : cela permet aux éléments hors écran ou cachés d'être rendus en dernier sans retarder le rendu des composants "immédiatement visibles". Cela pourrait également améliorer l'expérience utilisateur lors de l'utilisation du code-splitting dans l'écran actuel. Le code-splitting pourrait causer un rendu en cascade sans fluidité de l'écran. Pour éviter cet effet secondaire, React 16 introduit une "phase de commit" qui consiste à retarder toutes les mises à jour du DOM à la fin de la phase de rendu pour éviter un DOM incohérent.

Introduire React Fiber était une excellente façon d'ouvrir la conférence. Ses nouvelles fonctionnalités sont très attendues par la communauté. Pour en savoir plus sur React Fiber : [https://github.com/acdlite/react-fiber-architecture](https://github.com/acdlite/react-fiber-architecture)

### Ce que j'ai appris en benchmarkant React

[Dominic Gannaway](https://www.freecodecamp.org/news/what-ive-learned-from-react-europe-2017-c433468890d6/undefined) de Facebook a présenté les optimisations récentes du package React. Inspiré par la conception de clones légers de React comme Inferno (créé par lui) et Preact, il travaille pour rendre le package React plus léger et plus rapide à charger.

Grâce à un nouveau système de build soutenu par [Rollup](https://github.com/rollup/rollup), le package React gagne 10% de poids et est 9% plus rapide à charger.

> Webpack est pour les apps, Rollup est pour les bibliothèques

Ils ont également externalisé le support de `PropTypes` ainsi que le code obsolète comme `React.createClass` (voir [ici](https://facebook.github.io/react/blog/2017/04/07/react-v15.5.0.html#new-deprecation-warnings)).

Dominic a souligné l'importance d'utiliser un outil de benchmark puissant et cohérent lors de la tentative d'optimisation du package React. Il a montré un outil intéressant de "benchmarking de snapshots" comparant les métriques actuelles par rapport aux précédentes (taille du package, temps de chargement initial, temps jusqu'à l'interactivité) qui s'exécute sur [Google Lighthouse](https://developers.google.com/web/tools/lighthouse/).

Cet outil a été d'une grande aide pour obtenir de la confiance lors du déplacement de la base de code React. C'est un préalable pour rendre React plus petit et plus rapide.

Pour en savoir plus sur le travail de Dominic :
Nouveau système de build : [https://github.com/facebook/react/pull/9327](https://github.com/facebook/react/pull/9327)
Benchmark : [https://github.com/facebook/react/pull/9465](https://github.com/facebook/react/pull/9465)

### Outils JavaScript de haute qualité

En tant qu'adoptant précoce de Jest, je peux dire que l'utilisation de Jest il y a deux ans était comme traverser le désert. J'ai également vécu la mutation de Jest qui est aujourd'hui un outil formidable et largement utilisé. C'est pourquoi j'ai été très heureux d'entendre [Christoph Pojer](https://www.freecodecamp.org/news/what-ive-learned-from-react-europe-2017-c433468890d6/undefined) raconter cette histoire.

![Image](https://cdn-media-1.freecodecamp.org/images/1*RGql2QYssW6i_RPldPED_A.jpeg)
_Bouffon triste ("Stańczyk" par [Jan Matejko](https://en.wikipedia.org/wiki/Jan_Matejko" rel="noopener" target="_blank" title="Jan Matejko))_

Cette histoire est : comment Jest est passé d'un outil à un "produit". Un produit est axé sur la performance et les fonctionnalités qui apportent l'adoptabilité, et dans le cas d'un runner de tests, deux expériences doivent être délicieuses : exécuter des tests et écrire des tests.

La performance a été améliorée en implémentant des exécutions de tests parallèles, en utilisant tous les CPU, et en mesurant les temps d'exécution pour mieux les planifier pour les prochaines exécutions.

Christoph et la communauté ont fait un excellent travail pour apporter des fonctionnalités intéressantes dans Jest, comme une sortie pertinente (diff utile au lieu de stacktrace d'erreur sans intérêt), un mode watch immersif (CLI interactif, navigation parmi la liste des cas de test pour les relancer).

Christoph a mentionné les tests de snapshot : en plus des tests conventionnels (ce n'est pas un remplacement !), c'est un excellent moyen de visualiser la sortie complète d'un composant (actuel vs attendu).

Jest 20 viendra avec le runner multi-projets. En utilisant l'option `--projects`, Jest est capable d'exécuter plusieurs suites de tests et de consolider les résultats des tests dans une seule fenêtre de terminal. Utile pour utiliser le mode watch sur une base de code multi-repo.

Jest a été déplacé vers une architecture multi-packages et certains d'entre eux sont utilisés sur plusieurs projets chez Facebook : jest-haste-map, jest-snapshot, jest-validate (un parseur d'options CLI comme [Commander](https://github.com/tj/commander.js)). Cela a été utile en interne pour consolider leurs infrastructures et partager les meilleures pratiques.

Il est intéressant de mentionner que Jest est maintenant maintenu par 2 développeurs principaux + la communauté. Nous sommes fortement encouragés à contribuer, le projet Jest est accessible et facile à contribuer.

Article de blog sur Jest 20 : [https://facebook.github.io/jest/blog/2017/05/06/jest-20-delightful-testing-multi-project-runner.html](https://facebook.github.io/jest/blog/2017/05/06/jest-20-delightful-testing-multi-project-runner.html)

### Pire est mieux : l'avantage de la fatigue JavaScript

Le point de cette conférence est que la fatigue JavaScript est une bonne chose, saine pour l'écosystème. [Kevin Lacker](https://www.freecodecamp.org/news/what-ive-learned-from-react-europe-2017-c433468890d6/undefined) a commencé par nous rappeler ce qu'est la [fatigue JavaScript](http://thefullstack.xyz/javascript-fatigue/).

Des centaines de nouvelles bibliothèques sont annoncées chaque mois sur [Hackernews](https://news.ycombinator.com/). Il est impossible de tout regarder. La bonne nouvelle est que vous n'avez pas à le faire : il suffit de choisir **la bonne chose**.

D'un principe conçu par Richard P. Gabriel dans les années quatre-vingt, la bonne chose a 4 caractéristiques dorées :

* Simplicité
* Exactitude
* Cohérence
* Complétude

Mais l'histoire montre que la bonne chose est parfois... pas la bonne chose. En fait, seule la simplicité compte.

> Les choses simples sont plus faciles à intégrer.

Le concept de **pire est mieux** est né. Nous pourrions supporter un manque d'exactitude, de cohérence ou de complétude si la chose est simple à gérer !

À ce stade, est venu le parallèle avec la montée de React : la simplicité avant toutes les autres caractéristiques.

La simplicité conduit à la popularité qui conduit aux contributeurs. Aujourd'hui, nous pouvons profiter de tout ce qui manquait à React à son lancement : gestion d'état, routage, outils de démarrage (create-react-app).

En parlant de create-react-app, il rassemble vraiment toutes les meilleures choses apportées par la communauté depuis 3 ans et il est bien meilleur qu'il n'aurait pu l'être au lancement de React.

La fatigue JavaScript, alors, est simplement la conséquence du grand nombre de contributeurs open-source.

En conclusion, lancez quelque chose de simple, rendez-le populaire (documenté, testé en conditions réelles), puis comblez les lacunes.

J'ai trouvé que Kevin avait fait une analogie intéressante entre l'écosystème JavaScript moderne et la théorie du _pire est mieux vs la bonne chose_.

Excellent article sur la théorie de Richard P. Gabriel : [https://en.wikipedia.org/wiki/Worse_is_better](https://en.wikipedia.org/wiki/Worse_is_better)

### Wabi Sabi

Ce mot japonais désigne l'art de la "beauté dans l'imperfection". [Cheng Lou](https://www.freecodecamp.org/news/what-ive-learned-from-react-europe-2017-c433468890d6/undefined) a fait une conférence philosophique et très inspirante ([pour la deuxième année consécutive](https://www.youtube.com/watch?v=mVVNJKv9esE)) sur les compromis.

Les compromis font partie intégrante de notre travail en tant qu'ingénieur logiciel car nous n'avons pas un temps et un budget illimités. Nous utilisons donc des morceaux de logiciels qui couvrent imparfaitement nos besoins. Disons 80% de nos besoins : cela correspond au **sweet spot** sur la courbe de Pareto, également connue sous le nom de règle 80/20. Cela signifie qu'une quantité raisonnable de temps (environ 20%) est suffisante pour couvrir 80% de nos besoins.

Notre monde informatique est rempli de systèmes à 80%. Par exemple, la compression d'images : si vous obtenez 80% de l'image originale pour 20% de sa taille, c'est un bon compromis.

Concernant React, le compromis peut être la communication avec les composants frères qui est bien plus difficile que les composants parent/enfant... La cause est le modèle arborescent, pratique pour 80% des cas. L'approche à 100% serait un modèle de graphe.

Flux est également un système à 80%. Certaines tâches sont difficiles, comme la gestion des effets secondaires ou des sources externes de changements. Redux est généralement excellent mais les programmeurs malchanceux dans la zone des 20% ont besoin de solutions de contournement. Cela me rappelle le [modèle dead drop](https://medium.com/@erikras/redux-dead-drop-1b9573705bec) par exemple.

> Certaines choses ne sont pas destinées à être optimisées.

Il est important de souligner que, parfois, le compromis est intentionnel car nous sommes dans le sweet spot, nous ne voulons pas bouger. Revenons à l'exemple React ci-dessus, si React passait à un modèle de graphe gérant 100% des cas d'utilisation, toute la bibliothèque serait plus complexe, ce qui n'est pas une bonne chose.

Être dans un système à 80% nous donne de la marge de manœuvre, cela stimule notre créativité et notre adaptabilité. Je travaille depuis quelques mois avec [redux-observable](https://redux-observable.js.org/) que je peux maintenant décrire comme "un compromis pour les 20% des cas que Redux ne couvre pas".

![Image](https://cdn-media-1.freecodecamp.org/images/1*DBGdHlkB6DVjBy62d3TANQ.gif)
_Et redux-observable est aussi un système à 80% !_

Il y a des inconvénients dans l'approche à 80%. Tout d'abord : les 20% évidemment. Cela peut ne pas être choisi pour construire des fondations. De plus, la conception à 80% rend généralement la composition cauchemardesque (mutations, effets secondaires, ...).

Certaines choses appartiennent au monde des 100%. Par exemple, la vérification des types avec Flow : une grande force de Flow est la capacité à typer incrémentalement votre base de code. Il est acceptable d'ajouter Flow fichier par fichier mais vous ne pouvez pas ajouter Flow partiellement dans un fichier car vous ne pourriez pas dire "OK, cette partie de mon application est fortement typée, je lui fais confiance". Vous perdriez le bénéfice de la vérification des types (la confiance).

Il est intéressant de mentionner que les systèmes à 80% et à 100% peuvent être complémentaires : vous pouvez utiliser un outil à 80% car vous avez un compilateur derrière la scène (100%, le compilateur ne vous lâche jamais).

Lire la documentation est une action à 80%, lire le code source est à 100%.

En conclusion, Cheng a mentionné une publication de Leslie Lamport comme source d'inspiration pour sa conférence. Il dit que la crédibilité de l'approche à 80% varie avec le domaine de la science, de 0% en mathématiques à 100% en sociologie/psychologie.

Encore une fois, Cheng a la capacité incroyable de voir le tableau d'ensemble avec du recul. J'ai trouvé sa conférence très instructive et... rafraîchissante dans une conférence aussi technique.

Publication de Leslie Lamport : [http://lamport.azurewebsites.net/pubs/future-of-computing.pdf](http://lamport.azurewebsites.net/pubs/future-of-computing.pdf)

### Comment le streaming peut supercharger React

[Sasha Aickin](https://www.freecodecamp.org/news/what-ive-learned-from-react-europe-2017-c433468890d6/undefined) a introduit sa conférence avec quelques métriques sur le temps de rendu initial (+1s de temps de chargement de page sur un site commercial conduit à -20% de taux de conversion), faisant le point que le SSR (Server Side Rendering) est vital.

Mais le SSR vient avec un autre problème : il provoque un délai entre le premier rendu (le navigateur peint le balisage rendu côté serveur immédiatement) et le "time-to-interactive" (le navigateur a chargé le bundle et le SPA est en marche). Cette durée est appelée de manière amusante par [Paul Lewis](https://www.freecodecamp.org/news/what-ive-learned-from-react-europe-2017-c433468890d6/undefined) la "vallée dérangeante".

De plus, le SSR ne se met pas à l'échelle : plus votre page est complexe, plus il faut de temps pour la rendre côté serveur. Et il est difficile de dire à votre PO : "Non, non, non, je ne peux pas faire ça, cela rendra toute la page plus lente !"

Plusieurs choses se passent lorsqu'une page est rendue côté serveur :

* Le navigateur envoie une requête au serveur,
* Le serveur récupère les données de l'API,
* Le serveur rend le balisage,
* Le serveur retourne la page avec le balisage.
* Le navigateur peint le balisage et envoie des requêtes pour les fichiers CSS et JS. Nous sommes entrés dans la vallée dérangeante.
* Le serveur répond aux fichiers demandés.
* Le navigateur charge et exécute le bundle.
* Nous avons enfin atteint la fin de la vallée dérangeante.

Le problème est que toutes ces tâches se produisent séquentiellement. Et si nous pouvions paralléliser les choses ?

Au lieu d'un SSR monolithique énorme, le serveur pourrait traiter le rendu de la page fragment par fragment. Prenons une page composée d'un titre, d'un contenu principal et de commentaires par exemple, Sasha a montré que le serveur pourrait retourner un "morceau", c'est-à-dire toutes les pièces nécessaires pour rendre une portion de la page (HTML + CSS + JS + JSON) pour chaque partie de la page.

Avec cette approche (SCR ou Server Chunk Rendering), le temps de rendu initial et la durée de la vallée dérangeante sont réduits (surtout sur mobile) car le SSR est plus un "stream" maintenant, il pourrait être parallélisé :

* Le navigateur envoie une requête au serveur,
* Le serveur traite et retourne le premier morceau (le titre)
* Pendant que le navigateur peint et le charge, le serveur commence à traiter le 2ème morceau (le contenu principal) et peut même demander à l'API les données du 3ème morceau (les commentaires) en même temps.
* Le serveur retourne le 2ème morceau
* Et ainsi de suite...

Un autre avantage est : si l'un des multiples appels à l'API tombe dans un trou noir, cela ne fait pas tomber toute la page, mais seulement la zone concernée par le morceau.

J'avais beaucoup d'interrogations en tête après la conférence : comment définir les morceaux dans chaque page de l'application ? Cela implique-t-il le retour des bons vieux templates HTML ? (Je suppose que je dois jeter un coup d'œil à la bibliothèque de Sasha [react-dom-stream](https://github.com/aickin/react-dom-stream)), mais, oui, il semble que nous ayons eu un aperçu de ce que sera l'avenir du SSR :

> Renommer ReactServer -> ReactDOMServerStream Ce fichier va être le remplacement de ReactDOMServer.

Les récentes pull requests montrent que quelque chose arrive dans le repo officiel de React : [https://github.com/facebook/react/pull/9710](https://github.com/facebook/react/pull/9710)

Article de blog sur la vallée dérangeante : [https://aerotwist.com/blog/when-everything-is-important-nothing-is/](https://aerotwist.com/blog/when-everything-is-important-nothing-is/)

### Lightning talks (jour 1)

#### return null; par Joshua Comeau

[Joshua Comeau](https://www.freecodecamp.org/news/what-ive-learned-from-react-europe-2017-c433468890d6/undefined) a parlé des composants "sans rendu". Ces composants ne rendent rien mais profitent du cycle de vie de React.

Il a présenté un composant `Log` très simple qui imprime son enfant dans la console, chaque fois qu'il change, grâce au cycle de vie de React.

Ensuite, un exemple plus sérieux : un composant enveloppant l'[API Web Speech](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API) qui lit à voix haute le contenu d'une entrée de texte. Le composant est capable d'interrompre le discours actuel avant de lire le nouveau contenu : puisque le nouveau contenu est une prop, cela pourrait être facilement implémenté dans un `componentWillReceiveProps`.

Joshua a rassemblé de grandes explications (ainsi que des diapositives et des exemples) dans son dépôt Github : [https://github.com/joshwcomeau/return-null](https://github.com/joshwcomeau/return-null)

#### Detox : Tests End-to-End et Bibliothèque d'Automatisation Graybox pour React Native

Même les personnes qui n'avaient jamais entendu parler de Detox savaient que quelque chose se préparait lorsque le public a applaudi avant le début de la conférence, juste lorsque le titre est apparu sur les écrans !

Dans le monde du développement mobile, le QA manuel est chronophage, jusqu'à 10 jours complets pour l'application Wix. Ainsi, [Tal Kol](https://www.freecodecamp.org/news/what-ive-learned-from-react-europe-2017-c433468890d6/undefined) et les gens de Wix ont mis des efforts dans les tests automatisés et utilisé le framework numéro 1 : [Appium](http://appium.io/). Cela n'a pas donné satisfaction car les tests doivent s'exécuter sur de vrais appareils, ils sont très lents, compliqués à écrire et instables (ils finissent avec _sleep()_ partout). Ils ont donc décidé de créer un nouvel outil : Detox !

Alors qu'Appium est une boîte noire, Detox est plus une "boîte grise" : tout sur l'appareil (ou le simulateur) est surveillé (réseau, thread JS, etc.), maintenu contrôlé et synchronisé pour éviter l'instabilité.

La conférence s'est terminée par une vidéo montrant une exécution très rapide de la suite de tests.

Nous avons rencontré exactement les mêmes problèmes avec Appium dans mon entreprise cliente [M6 Web](http://tech.m6web.fr/). En raison du format lightning talk, il était impossible d'expliquer en détail l'interne de Detox, donc nous avons encore beaucoup de questions (fonctionne-t-il avec une application brownfield ?), mais nous essaierons définitivement Detox par nous-mêmes !

Repo : [https://github.com/wix/detox](https://github.com/wix/detox)

#### Graphismes sérieux sur React Native

Excellente façon de clôturer le Jour 1 : une conférence visuelle remplie de choses cool comme des jeux vidéo, des filtres d'image, de la visualisation de données, ... par [James Ide](https://www.freecodecamp.org/news/what-ive-learned-from-react-europe-2017-c433468890d6/undefined) de Expo.

James a présenté le composant GLView de Expo qui est capable d'afficher des graphismes OpenGL accélérés par GPU sur un appareil mobile.

L'architecture du composant GLView est un peu différente des autres composants React Native. Il a utilisé la capacité de JavaScriptCore (l'environnement d'exécution JavaScript mobile) à appeler l'API native C sans utiliser le pont principal. Ainsi, les graphismes ne sont pas affectés par l'occupation du pont.

Ensuite, James a montré quelques interfaces graphiques comme des effets sur le flux vidéo de la caméra, des jeux vidéo et un exemple de vue 3D créée avec la bibliothèque existante [gl-react](https://github.com/gre/gl-react) qui est compatible avec React Native.

Documentation GLView : [https://docs.expo.io/versions/v17.0.0/sdk/gl-view.html](https://docs.expo.io/versions/v17.0.0/sdk/gl-view.html)

### Composition : un superpouvoir expliqué

Je trouve que la programmation fonctionnelle est généralement incroyablement utile, concise et élégante, mais nous ne devrions pas tomber dans le piège de faire de la PF... pour faire de la PF, lorsque le code devient moins lisible et compréhensible qu'avant. [Nik Graf](https://www.freecodecamp.org/news/what-ive-learned-from-react-europe-2017-c433468890d6/undefined) n'est pas tombé dans ce piège lorsqu'il a présenté sa conférence sur la composition, inspirée par son travail sur l'API de couleur de [polish](https://github.com/styled-components/polished).

Pour illustrer le problème original, Nik a présenté un exemple de code impératif utilisant [Lodash](https://lodash.com) (puisque la vidéo en direct a été temporairement supprimée de YouTube, j'ai réécrit des extraits de code similaires) :

Ce code rempli de variables temporaires pourrait être amélioré avec l'API de chaîne :

Cela est plus concis mais toujours pas parfait, il y a encore les opérateurs `chain` et `value` (sérieusement, qui n'a jamais oublié `.value()` à la fin d'une chaîne Lodash explicite ?). De plus, l'API de chaîne tue la capacité d'importer partiellement Lodash (voir [cet excellent article](https://medium.com/making-internets/why-using-chain-is-a-mistake-9bc1f80d51ba)).

La vraie composition permet de définir un pipe avec [Ramda](http://ramdajs.com/), [lodash/fp](https://github.com/lodash/lodash/wiki/FP-Guide) :

Nous pouvons trouver une syntaxe similaire peu élégante dans React avec le modèle HoC (High-Order Component) et, encore une fois, la composition pourrait améliorer la lisibilité :

La fonction `compose` de Ramda, lodash/fp, recompose ou react-apollo peut être utilisée ici (oh, j'ai déjà mis le gif mind-blown dans cet article, non ?). Donc il semble qu'il y ait un vrai modèle ici.

Cela a été une source d'inspiration lorsque Nik a créé l'API de couleur de polish : une couleur pourrait être une composition de teinte, de lumière et de saturation ! Ils ont fait une API cool comme Ramda ou Lodash/fp, composable mais aussi utilisable dans le style impératif grâce au currying.

De retour à React, Nik a montré que nous pouvons écrire notre propre fonction HoC pour éviter la répétition. Par exemple, lorsque nous avons un ensemble de composants qui ont besoin d'une prop booléenne pour être vraie pour afficher le contenu :

Nous pouvons faire de même avec une fonction HoC `withErrorMessage` qui décore une entrée de texte avec un message d'erreur par exemple.

Nik a clôturé la conférence avec un écran React VR montrant la rotation des planètes, la rotation est implémentée avec une syntaxe similaire à React Native Animated. Il explique comment l'animation est contenue dans une fonction HoC réutilisable `withRotation`.

Cette conférence a fourni des exemples pertinents pour illustrer les concepts de PF comme le currying, les fonctions d'ordre supérieur et comment ils pourraient être appliqués à React (Higher-order-Component). J'ai définitivement hâte d'analyser la HoC `withRotation` et de voir si je pourrais transposer cela sur mes projets React Native.

Doc React sur la composition et HoC : [https://facebook.github.io/react/docs/higher-order-components.html](https://facebook.github.io/react/docs/higher-order-components.html)

### React en tant que plateforme

C'est un fait bien connu qu'Airbnb utilise de manière extensive React et React Native. [Leland Richardson](https://www.freecodecamp.org/news/what-ive-learned-from-react-europe-2017-c433468890d6/undefined) a souligné que c'était un grand pas en avant :

Au lieu d'écrire Airbnb 3 fois (pour Web, iOS et Android) par 3 équipes différentes (JavaScript / Java / Swift), React et React Native permettent une écriture en 2 temps (Web et natif) par la même équipe (Javascript). Mais maintenant, l'ingénieur écrit deux fois un code presque identique. Ne serait-ce pas mieux s'ils l'écrivaient seulement une fois ?

> Écrire une fois, exécuter partout ?

Leland pense que nous pouvons y parvenir. React Native a été un déclic : React peut cibler plusieurs plateformes. Ensuite, [React Native pour Web](https://github.com/necolas/react-native-web) est arrivé, suivi par Windows, Ubuntu, VR, ...

Le plus grand obstacle au partage de composants entre les plateformes est l'importation de l'implémentation de la plateforme, par exemple avec React Native :

```
import { View } from 'react-native';
```

Notez qu'un composant React DOM n'a pas une telle importation pour des raisons de compatibilité, mais ne devrait-il pas en avoir pour des raisons de cohérence ?

```
import { Div } from 'react-dom'; //À discuter seulement, ne faites pas ça ;)
```

Sur la base de l'expérience de la bibliothèque de composants React Native d'Airbnb, seulement 7 API React Native sont largement utilisées. Beaucoup des 70+ API sont des compositions de ces 7 primitives.

Leland est venu avec une proposition : ces 7 API enveloppées dans un package NPM nommé react-primitives.

* `View`
* `Image`
* `Text`
* `Animated`
* `Touchable`
* `Platform`
* `StyleSheet`

Leland est conscient que ce n'est pas parfait : la présence de `Animated` est discutable. À l'inverse, `TextInput` n'est pas inclus malgré le fait qu'il ne peut pas être une composition des 7 primitives.

Mais peut-être qu'une extension de plateforme optionnelle est la réponse (inspirée par la capacité de React Native à définir des implémentations spécifiques à la plateforme en ajoutant un suffixe à la fin du nom de fichier).

Prenons l'exemple de la case à cocher : _Checkbox.js_ pourrait contenir une composition de primitives pour concevoir une case à cocher sur toutes les plateformes où la case à cocher n'existe pas. Et, en tant qu'optimisation, _Checkbox.web.js_ pourrait contenir uniquement le composant d'entrée de react-dom.

```
<input type="checkbox">
```

Comme si cela ne suffisait pas à convaincre, Leland a clôturé sa conférence avec [react-sketchapp](https://github.com/airbnb/react-sketchapp), montrant comment ils ont traité l'outil de design [Sketch](https://www.sketchapp.com/) comme une plateforme supplémentaire sans modifications dans la base de code grâce aux primitives. Les designers d'Airbnb peuvent concevoir des storyboards en utilisant la vraie bibliothèque de composants React Native.

react-primitives : [https://github.com/lelandrichardson/react-primitives](https://github.com/lelandrichardson/react-primitives)

### Lightning talks (jour 2)

#### Expo Snack

En plus de faire une grande introduction pour chaque intervenant pendant ces 2 jours, [Brent Vatne](https://www.freecodecamp.org/news/what-ive-learned-from-react-europe-2017-c433468890d6/undefined) a présenté Snack pour l'application Expo dans une conférence éclair.

Snack est le remplacement de l'ancien terrain de jeu React Native ([rnplay-web](https://github.com/rnplay/rnplay-web)). Le problème avec rnplay-web était une boucle de feedback très lente. Les modifications de code étaient envoyées au serveur qui devait exécuter le packager React Native et renvoyer la sortie au navigateur.

Avec Snack, les modifications de code de l'éditeur web sont envoyées à l'appareil et réexécutées directement.

Snack inclut également une génération de code QR pour obtenir votre code en cours d'exécution dans l'application Expo sur votre propre appareil.

Les exemples de la documentation officielle de React Native ont été déplacés vers Snack. Par exemple : [http://facebook.github.io/react-native/releases/next/docs/text.html](http://facebook.github.io/react-native/releases/next/docs/text.html)

Pour jouer avec la génération de code QR, le glisser-déposer des composants pontés d'Expo s'exécutant sur votre propre appareil en un rien de temps : [https://snack.expo.io/](https://snack.expo.io/)

#### Code-splitting et préchargement plus intelligents pour les applications React

Dans sa conférence éclair, [Brandon Dail](https://www.freecodecamp.org/news/what-ive-learned-from-react-europe-2017-c433468890d6/undefined) a parlé de code-splitting avec react-loadable et de sa capacité à précharger un composant en utilisant la méthode statique `preload()`.

Il existe 2 approches concernant le préchargement. Le préchargement "passif" est basé sur l'**intention** de l'utilisateur. Par exemple, une page de liste pourrait précharger la page de détail car il y a de bonnes chances que l'utilisateur veuille ouvrir la page de détail. Cette approche devrait être basée sur l'analyse pour éviter un préchargement inutile.

À l'inverse, l'approche "active" consiste en un préchargement basé sur l'**action** de l'utilisateur, comme une souris approchant d'un bouton (événement `onMouseEnter`). Pour ce cas, Brandon a créé la bibliothèque react-perimeter qui définit des limites autour d'un composant et appelle un callback lorsqu'elles sont franchies (similaire à un événement `onMouseEnter`) : utile pour appeler la méthode de préchargement.

react-loadable : [https://github.com/thejameskyle/react-loadable](https://github.com/thejameskyle/react-loadable)
react-perimeter : [https://github.com/aweary/react-perimeter](https://github.com/aweary/react-perimeter)

Seulement 2 jours après la conférence, les vidéos des conférences ont commencé à être publiées sur la chaîne YouTube de la conférence, restez à l'écoute sur [https://www.youtube.com/channel/UCorlLn2oZfgOJ-FUcF2eZ1A/videos](https://www.youtube.com/channel/UCorlLn2oZfgOJ-FUcF2eZ1A/videos) !