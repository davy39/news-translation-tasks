---
title: React Props/State Expliqué à travers la Chasse de Dark Vador contre les Rebelles
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-10-04T05:26:17.000Z'
originalURL: https://freecodecamp.org/news/react-props-state-explained-through-darth-vaders-hunt-for-the-rebels-8ee486576492
coverImage: https://cdn-media-1.freecodecamp.org/images/1*i4gLjg40GYrR12oVI5NsZw.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: star wars
  slug: star-wars
- name: Web Development
  slug: web-development
seo_title: React Props/State Expliqué à travers la Chasse de Dark Vador contre les
  Rebelles
seo_desc: 'By Kevin Kononenko

  If you’ve seen Star Wars, then you can understand props and state.

  Props and state are essential to writing readable React code. But they’re hard concepts
  to grasp, because they’re based around an entirely different paradigm than A...'
---

Par Kevin Kononenko

#### Si vous avez vu Star Wars, alors vous pouvez comprendre les props et le state.

Les props et le state sont essentiels pour écrire du code React lisible. Mais ce sont des concepts difficiles à saisir, car ils sont basés sur un paradigme entièrement différent de celui d'Angular ou de jQuery (si vous avez utilisé l'un ou l'autre).

Mais ne vous inquiétez pas — je vais tout clarifier avec une analogie Star Wars.

C'est exact. Si vous avez vu la série originale Star Wars, vous pouvez comprendre les props et le state.

Voici un rappel sans spoiler de la prémisse de base des épisodes 4 à 6 :

1. Dark Vador traque les rebelles sans relâche, car ils sont la dernière résistance contre l'Empire Galactique.
2. Les rebelles, dirigés par la princesse Leia et Luke Skywalker, doivent riposter et exploiter les vulnérabilités de l'Empire.
3. Dark Vador utilise une variété de tactiques pour tenter de découvrir les mouvements des rebelles, y compris une armée de Stormtroopers, une flotte de vaisseaux stellaires et une variété d'éclaireurs.

L'ensemble du plan des ressources de l'Empire dépend du leadership de Vador.

Si vous êtes habitué à utiliser jQuery, vous pourriez penser à créer un seul gestionnaire d'événements (comme un gestionnaire click()), puis à modifier explicitement différentes parties de l'interface utilisateur ligne par ligne.

Mais dans React, l'idée est que lorsque l'**state** est modifié, les changements se **propageront automatiquement** à tous les composants enfants via les **props**. Vous n'avez donc besoin d'écrire le code que pour changer une seule chose — l'**state** — et de regarder votre UI se mettre à jour.

Cela ressemble à la manière dont Dark Vador commande les trois ailes de son armée. Une fois qu'il reçoit des nouvelles de l'emplacement des rebelles, ses ressources se mobiliseront automatiquement pour lancer une attaque.

Commençons. Ce tutoriel nécessitera une connaissance de base de JSX, que vous pouvez apprendre davantage [ici](https://facebook.github.io/react/docs/thinking-in-react.html).

### Un Résumé de l'Empire Galactique

Voici les trois ailes de l'Empire Galactique.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NBQvDruVqf4qCPT-BDuADA.png)

**L'Armée Impériale** est composée de Stormtroopers, d'AT-AT, d'AT-ST et d'autres.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0CHW4ZMIqxwVBIou8vnXkA.png)

**La Marine Impériale** est composée de destroyers stellaires, de chasseurs TIE et d'autres.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pJpvQ3IJjJZEIAHSgOPx6w.png)

**Le Renseignement Militaire** est composé de chasseurs de primes comme Boba Fett, de droïdes sonde et d'autres éclaireurs spécialisés.

Voici un organigramme rapide qui donnera une direction sur la façon dont nous allons écrire nos composants.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Wb5PjkC4-AY-K8J494S4ng.png)

Un rappel : le premier objectif de Vador est de trouver l'emplacement des rebelles. Ceux qui sont en bas de l'organigramme sont les unités fonctionnelles réelles qui peuvent accomplir cela. Si l'un d'eux trouve une base rebelle, leurs instructions seraient de retourner vers Vador afin qu'il puisse exécuter ses plans de bataille.

React est tout au sujet de l'**interface utilisateur dynamique**. Lorsque l'utilisateur effectue une action spécifique, comment l'**state** change-t-il ? Dans ce cas, Dark Vador aurait un **state** appelé _rebelLocation_. Puisque c'est la variable dynamique clé, les trois ailes de l'Empire se mobiliseraient en raison d'un changement dans le **state** _rebelLocation_.

Stormtrooper rencontre une base rebelle → Retourne vers Dark Vador avec l'emplacement

L'utilisateur clique sur un certain élément → Met à jour le state d'un composant parent

Voici les bases en code, qui suivent l'organigramme ci-dessus :

### State Expliqué

Le **state** vous permet de changer dynamiquement de nombreux éléments à la fois en fonction d'une seule variable. Le **state** englobe les parties clés de votre UI qui changent en fonction de l'entrée de l'utilisateur.

Avec moins de choses à suivre dans le state, vous pourrez écrire des composants avec plus de clarté et moins d'opportunités pour les bugs. Lorsque le state change, de nombreux composants peuvent changer en conséquence en fonction de cette seule variable.

jQuery aborde cela en vous demandant d'écrire une ligne pour chaque élément qui doit être changé. Il n'est pas explicitement basé sur la relation parent-enfant comme le **state**.

Disons que les Stormtroopers rencontrent les rebelles. Vador leur a ordonné de lui faire rapport dès que possible. Une fois qu'ils reviennent avec un emplacement rebelle, Vador peut exécuter le reste de ses ordres, qui dépendaient de l'emplacement des rebelles. Voici un diagramme modifié qui trace le chemin à travers les composants listés ci-dessus.

![Image](https://cdn-media-1.freecodecamp.org/images/1*go7yyXmlbrzVJg7QDRJmjQ.png)

Les ordres sont déjà transmis à chaque membre en bas du tableau. Une fois qu'ils tombent sur des rebelles, ils savent qu'ils doivent retourner auprès de Lord Vador. Le **state** _rebelLocation_ sera alors mis à jour avec la planète, qu'il s'agisse d'« Endor », de « Hoth » ou d'un autre endroit.

C'est le même concept que de recevoir une entrée utilisateur puis de mettre à jour le state dans un composant parent. De nombreux praticiens de React choisissent d'écrire des composants avec une fonction unique, donc le composant qui écoute réellement l'entrée utilisateur sera presque toujours différent du composant qui détient le state.

**Ci-dessus :** Stormtrooper imbriqué dans ImperialArmy imbriqué dans vadersEmpire

**Dans une vraie application :** Entrée utilisateur imbriquée dans une div parent imbriquée dans une div parent

#### Que se passe-t-il lorsque le state change ?

C'est la beauté de React. Plutôt que d'écrire des gestionnaires d'événements compliqués (comme dans jQuery), tout dépend des changements dans le state. Vous pouvez clairement tracer les changements dans l'UI à ces changements de state.

Dans ce cas, une fois que _rebelLocation_ est découvert, le **state** changerait pour cette planète. Mais ce n'est que la moitié de l'histoire. Dark Vador aurait des plans en tête pour mobiliser différents actifs en fonction de ce changement de state. Il peut les préparer à l'avance pour cette possibilité. Comme dans, « Lorsque nous trouverons leur planète, rendez-vous immédiatement et préparez-vous à une attaque ! »

Une fois que le state change, les changements sont automatiquement partagés avec les 3 ailes de l'Empire. De même, lorsque le state d'un composant parent change, les composants enfants héritent automatiquement du nouveau state.

![Image](https://cdn-media-1.freecodecamp.org/images/1*3-O1sL-whbHAa8prrqeCDQ.png)

Chaque composant peut également avoir son propre state. Par exemple, le composant _ImperialArmy_ pourrait avoir un state _troopsCount_ qui compte les membres de l'armée. Nous ne modifierons pas cela dans cet exemple, mais vous pouvez imaginer qu'une bataille pourrait affecter _troopsCount_.

Remarquez comment ce state ne dépend pas de _rebelLocation_. Si c'était le cas, nous ne voudrions pas déclarer explicitement un autre state. Nous voudrions qu'il se mette à jour automatiquement en fonction d'un changement dans le state _rebelLocation_.

Puisqu'il est indépendant, voici à quoi ressemble le code :

Attendez, alors comment ce state est-il communiqué entre les différents composants ? Cela nous amène aux... props !

### Props Expliqués

Avec notre cas de Dark Vador, nous avons en fait besoin de deux ensembles d'instructions lorsqu'il s'agit de commander les Stormtroopers et autres unités en bas de notre organigramme.

**Question 1 :** Que doivent faire les Stormtroopers s'ils rencontrent les rebelles ?

**Réponse :** Rapporter à Dark Vador.

**Question 2 :** Où les Stormtroopers doivent-ils se rendre ?

**Réponse :** _si_ les rebelles n'ont pas été trouvés, recherchez la galaxie au hasard. _Sinon_, allez à l'emplacement des rebelles pour les attaquer.

Les **props** nous permettent de surveiller en continu le **state** _rebelLocation_, et d'ordonner un mouvement de troupes si le state change. _rebelLocation_ est une chaîne de caractères. Mais qu'en est-il des ordres qui doivent se produire lorsqu'ils trouvent initialement les rebelles ?

Nous pouvons en fait passer une fonction en tant que **props** également ! Cela signifie que nous pouvons passer un callback à chaque Stormtrooper qui s'exécutera si ce trooper découvre la cible. Dans l'image suivante, vous pouvez suivre le chemin tracé par « Orders » pour tracer les **props**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*go7yyXmlbrzVJg7QDRJmjQ.png)

Dans une interface utilisateur typique, disons qu'un utilisateur clique sur un bouton, et vous voulez mettre à jour le state d'un composant parent. Vous devez également passer un callback de ce composant parent qui sera déclenché lors du clic de l'utilisateur. Ce callback peut ensuite mettre à jour le state **parce qu'il provient du même parent qui a défini le state**.

C'est important, alors explorons ce code ligne par ligne :

**Ligne 8 :** Nous créons la commande pour les Stormtroopers qu'ils doivent revenir avec l'emplacement des rebelles immédiatement lorsqu'ils le trouvent.

**Ligne 19 :** Nous passons la commande à toute l'armée via les **props** updateLocation.

**Ligne 32 :** L'Armée Impériale transmet cette commande à chaque Stormtrooper avec des **props** updateLocation identiques.

**Ligne 42 :** Nous créons une fonction discoverLocation afin de pouvoir passer la valeur de l'entrée dans le callback updateLocation() lorsqu'il est déclenché.

**Ligne 53 :** Lorsqu'un Stormtrooper trouve l'emplacement, il déclenche la fonction discoverLocation() afin que nous puissions retourner l'emplacement via updateLocation(). Cela met à jour le **state** dans le composant parent _vadersArmy_.

**Autres Notes :** Nous avons également passé le rebelLocation jusqu'à chaque Stormtrooper. Dans ce tutoriel, nous ne ferons rien avec cette information, mais à l'avenir, vous pouvez imaginer que cela pourrait être utilisé pour déplacer l'emplacement de toutes les troupes vers la base rebelle.

### Un Récapitulatif Final

1. Dark Vador donne à chaque membre de l'Empire Galactique un ordre : Si vous trouvez les rebelles, faites-moi rapport immédiatement. En code, il s'agit d'une fonction dans le composant parent _vadersArmy_ qui est ensuite passée à chaque enfant via les **props**.
2. L'Armée, la Marine et le Renseignement Militaire (trois divisions de l'Empire) transmettent cette instruction à chaque troupe, encore une fois via les **props**.
3. Chaque membre de l'Empire a les instructions. Lorsqu'ils rencontrent les rebelles, ils utiliseront un callback pour transmettre l'emplacement jusqu'à Dark Vador, qui mettra à jour tout l'Empire avec la nouvelle simultanément et se préparera pour la bataille. Cela simule une entrée utilisateur dynamique qui change le **state** du composant parent.

Si vous avez aimé cet article, vous aimerez peut-être aussi mes [autres explications](https://www.rtfmanual.io/guides/) de sujets CSS et JavaScript difficiles, tels que le positionnement, le Modèle-Vue-Contrôleur et les callbacks.

Et si vous pensez que cela pourrait aider d'autres personnes dans la même situation que vous, donnez-lui un « cœur » !