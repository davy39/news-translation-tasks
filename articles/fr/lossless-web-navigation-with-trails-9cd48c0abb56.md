---
title: Navigation Web sans perte avec des Trails
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-24T17:29:26.000Z'
originalURL: https://freecodecamp.org/news/lossless-web-navigation-with-trails-9cd48c0abb56
coverImage: https://cdn-media-1.freecodecamp.org/images/1*a2HidWVvbaqVlct9OORVhw.png
tags:
- name: Browsers
  slug: browsers
- name: Design
  slug: design
- name: interaction design
  slug: interaction-design
- name: internet
  slug: internet
- name: UX
  slug: ux
seo_title: Navigation Web sans perte avec des Trails
seo_desc: 'By Patryk Adaś

  Since the early 2000’s, the desktop metaphor of tabbed browsing has dominated the
  way we navigate the web. With Browser.html, a Mozilla Research project aimed at
  building a browser user interface built in HTML for nightly builds of Ser...'
---

Par Patryk Adaś

Depuis le début des années 2000, la métaphore du bureau de la navigation par onglets a dominé la façon dont nous naviguons sur le web. Avec [Browser.html](https://github.com/browserhtml/browserhtml), un projet de recherche Mozilla visant à construire une interface utilisateur de navigateur en HTML pour les builds nocturnes de [Servo](https://servo.org/), nous expérimentons **l'évolution du navigateur standard à onglets vers un modèle basé sur les _trails_.**

Le but des trails est de construire **non seulement une fenêtre vers le contenu web, mais aussi un récit de l'activité de l'utilisateur.** Notre espoir est que notre travail puisse aider à faire avancer l'état de la navigation plus près de l'idéal d'un outil qui _améliore_ notre processus cognitif, plutôt que d'augmenter notre charge cognitive.

Pour illustrer le type de scénario auquel nous pensons, nous allons vous présenter notre amie Nala.

### La recherche de la pizza parfaite

Nala est à la recherche de pizzerias. Dans son navigateur traditionnel à onglets, elle commence par une recherche _(1)_ qui la mène à une page de résultats de recherche _(2)_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7qOw8C6wzXJi6ieHobEKTw.png)

Elle suit un lien vers une liste de restaurants sur Yelp _(3)_, et vérifie une pizzeria prometteuse _(4)_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*404g1U_jYU4pYrO1292hsg.png)

Les liens externes sur Yelp s'ouvrent dans des onglets séparés, donc lorsque Nala clique sur un lien vers le site web d'un restaurant, cela ouvre un nouvel onglet _(5)_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*mhoj_P3uphTdyGKvK2o6QQ.png)

Le nouvel onglet n'a aucun historique, ni aucune connexion avec le premier onglet. **Tout l'historique de la façon dont Nala est arrivée sur le site web du restaurant est perdu !**

L'amnésie du navigateur s'aggrave alors qu'elle va regarder plus d'options : en revenant au premier onglet _(6)_ et en naviguant en arrière vers les résultats Yelp _(7)_, elle cherche un autre restaurant.

![Image](https://cdn-media-1.freecodecamp.org/images/1*cZMNV-d5kA_zPBV0gPQkBA.png)

Maintenant, lorsqu'elle sélectionne un nouveau restaurant _(8)_, **une partie de l'historique de navigation de l'onglet actuel est également perdue :**

![Image](https://cdn-media-1.freecodecamp.org/images/1*JTpAAWHBlwIZ0YMZPDsCJw.png)

En cliquant sur un lien externe vers le site web du prochain restaurant, un nouvel onglet s'ouvre à nouveau _(9)_, et rompt à nouveau la connexion avec l'historique qui l'a précédé.

![Image](https://cdn-media-1.freecodecamp.org/images/1*tW9QQd7vXGJ1inuAt13O2Q.png)

Pour regarder à nouveau les résultats de sa recherche initiale, Nala revient en arrière de quelques étapes dans l'historique du premier onglet et ouvre un autre lieu de pizza directement à partir de là _(10)_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*dWHcc6uSwXJFUv3NTaEVAw.png)

Dans cet exemple d'un scénario de recherche courant, plus d'un tiers de l'historique est perdu !

Bien sûr, les navigateurs fournissent généralement des outils comme les vues d'historique et les menus "onglets récents", [mais aucun de ceux-ci ne présente un récit qui correspond au parcours réel que Nala a suivi.](http://medium.freecodecamp.com/browserhistory-2abad38022b1)

### Des onglets aux trails

Avec Browser.html, nous prototypons une interface utilisateur qui raconte non seulement les fragments de l'historique de Nala qu'un navigateur à onglets préserve _(Version 1)_, mais tout cela _(Version 2)_ :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Z1Ue9kAxXyt0xS2ZiGa1yQ.png)

Mais ces arbres peuvent facilement devenir complexes. Ce qui nous semble le plus important, ce n'est pas où chaque exploration a divergé, mais le chemin complet menant à un résultat. C'est donc ce que nous affichons à l'utilisateur _(Version 3)_ :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Q46vM6br-gi0eTPhT5SBPg.png)

Chaque ligne représente un trail depuis la racine de l'arbre de navigation jusqu'à un résultat. L'avantage est qu'un trail raconte une histoire autonome de gauche à droite. En revanche, les doublons entraînent beaucoup de bruit visuel distractif. Heureusement, cela peut être supprimé en se concentrant sur un seul trail tout en pliant les autres.

Voici ce que Nala aurait réellement vu :

### Onglets et trails : identiques, mais différents.

Si vous ignorez les chemins menant à chaque sujet exploré, les trails ne sont pas différents des onglets conventionnels. Cela est intentionnel : notre objectif est d'améliorer les expériences utilisateur existantes, pas de les remplacer. Les utilisateurs peuvent continuer à utiliser les navigateurs comme ils l'ont toujours fait. Et pourtant, **chaque trail de navigation est un onglet qui raconte une histoire complète du début à la fin.** Cela nous offre des opportunités d'explorer d'autres améliorations de l'expérience utilisateur. En voici quelques-unes que nous envisageons :

* Partager non seulement des URLs, mais des trails entiers.
* Estomper les trails à mesure qu'ils deviennent non pertinents et éventuellement les retirer de la grille.
* Conserver les trails sous la forme qu'ils avaient lors de la visite, afin qu'ils puissent être revisités (hors ligne).
* Permettre l'annotation des trails afin que les utilisateurs puissent enregistrer leurs pensées tout en recherchant un sujet.
* Recherche collaborative sur un sujet.
* Ouvrir optionnellement des pages dans un nouveau trail.

### Le Chemin Vers les Trails

L'idée de visualiser le parcours d'un utilisateur à travers le web sous forme de trail n'est en aucun cas nouvelle. Même il y a soixante-dix ans, dans son essai marquant [As We May Think](http://www.theatlantic.com/magazine/archive/1945/07/as-we-may-think/303881/) popularisant l'idée de données hyperliées, [Vannevar Bush](https://en.wikipedia.org/wiki/Vannevar_Bush) décrivait une "machine memex". Il envisageait que cette machine nous aiderait à collecter et à partager des données à travers une bibliothèque personnelle qui nous aiderait à laisser une trace à travers notre processus de recherche.

Depuis lors, il y a eu plusieurs tentatives de créer un tel outil, commençant par [Trailmeme](https://www.youtube.com/watch?v=ofArVKb58-Q&t=1s) par [Xerox Trails](http://adsabs.harvard.edu/abs/2010SPIE.7540E..07R). Ce concept a été poursuivi par [Trailblazer](https://www-s.acm.illinois.edu/macwarriors/projects/trailblazer/) par [MacWarriors](https://www-s.acm.illinois.edu/macwarriors/) en 2004, actuellement suivi par [Trailblazer.io](http://www.trailblazer.io). Nous espérons qu'en reliant les idées de trails à des idiomes familiers à onglets, nous construirons sur des flux de travail existants et rendrons l'idée largement attrayante. Et Browser.html sert de banc d'essai idéal pour ces idées.

### Un Modèle Spatial

Je travaille sur un modèle spatial à travers diverses interactions utilisateur et animations. Cela devrait aider les utilisateurs à mieux comprendre ce qui se passe et comment naviguer sur le web de manière plus efficace.

[Vous pouvez en lire plus à ce sujet ici.](https://medium.freecodecamp.com/lossless-web-navigation-spatial-model-37f83438201d)

### Rejoignez-nous !

Nous travaillons actuellement à la construction de notre premier prototype fonctionnel. Si cela vous semble amusant, venez jeter un coup d'œil au projet [Browser.html](https://github.com/browserhtml/browserhtml) ! Vous pouvez trouver notre liste de [problèmes ouverts](https://github.com/browserhtml/browserhtml/issues) sur GitHub, ou venir discuter avec nous sur notre [Slack](https://browserhtml-slackin.herokuapp.com).