---
title: Comment détecter un clic à l'extérieur avec React et les Hooks
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-18T17:17:32.000Z'
originalURL: https://freecodecamp.org/news/how-to-detect-an-outside-click-with-react-and-hooks-25dbaa30abcd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xJYzPKhZBDlYsR2nwkbvPQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
seo_title: Comment détecter un clic à l'extérieur avec React et les Hooks
seo_desc: 'By Andrei Cacio

  What does “Outside Click” mean?

  You can think of it as the “anti-button”. An outside click is a way to know if the
  user clicks everything BUT a specific component. You may have seen this behavior
  when opening a dropdown menu or a drop...'
---

Par Andrei Cacio

### Que signifie « Clic à l'extérieur » ?

Vous pouvez le considérer comme l'« anti-bouton ». Un clic à l'extérieur est un moyen de savoir si l'utilisateur clique sur tout SAUF un composant spécifique. Vous avez peut-être vu ce comportement lors de l'ouverture d'un menu déroulant ou d'une liste déroulante et en cliquant à l'extérieur pour le fermer.

Il existe toutes sortes d'autres cas d'utilisation pour une telle fonctionnalité :

* lors de la fermeture de listes déroulantes
* lors de la fermeture de fenêtres modales
* lors de la transition en mode édition pour les éléments modifiables
* fermeture
* et bien plus encore…

Maintenant, voyons comment nous pouvons écrire un composant React générique et réutilisable qui incorporera ce comportement.

### À quoi cela ressemblera

Un flux heureux devrait ressembler à ceci :

### Structure du composant

Pour que ce composant fonctionne, nous devrons attacher un gestionnaire d'événements de clic sur le document lui-même. Cela nous aidera à détecter lorsque nous cliquons n'importe où sur la page. Ensuite, nous devrons vérifier si notre cible cliquée diffère de notre élément enveloppé. Une structure de base ressemblera donc à ceci :

_Pour le premier exemple, nous commencerons à coder en utilisant le style de classe React, puis nous le refactoriserons avec la nouvelle API Hooks._

Nous avons implémenté deux fonctions de cycle de vie :

* **componentDidMount()** : attachera l'écouteur d'événement
* **componentWillUnmount()** : nettoiera le gestionnaire de clic avant que le composant ne soit détruit

et ensuite nous rendons tout ce que ces composants enveloppent. Pour notre premier exemple ci-dessus, il rendra le <span>.

### La condition « ClickOutside »

Maintenant, nous devons vérifier si l'utilisateur clique à l'extérieur de l'enfant enveloppé. Une solution _naïve_ consiste à comparer l'élément cible (l'élément sur lequel nous cliquons) avec le nœud de notre enfant. Mais cela ne fonctionnera que si nous avons un nœud simple (niveau unique) comme enfant. Si notre enfant enveloppé a plus de sous-nœuds, alors cette solution échouera.

Heureusement, il existe une méthode appelée [**.contains()**](https://developer.mozilla.org/en/docs/Web/API/Node/contains) qui nous indique si un nœud est un enfant d'un nœud donné. L'étape suivante consistera à obtenir l'accès au nœud de notre enfant. Pour y parvenir, nous utiliserons [React Refs](https://reactjs.org/docs/refs-and-the-dom.html).

Les Refs sont le moyen de React de nous donner accès à l'objet nœud brut. Nous utiliserons également l'API de React pour gérer les composants **this.props.children**. Nous avons besoin de cette API car nous allons injecter notre ref créée à notre enfant enveloppé. En gardant cela à l'esprit, notre composant ressemblera à ceci :

Parfait, cela devrait fonctionner comme prévu. Au moins pour notre flux heureux (un enfant enveloppé). Si nous avons l'intention d'envelopper plus d'un nœud, nous devons apporter quelques ajustements :

* nous devons avoir un tableau de refs (autant que nos enfants enveloppés)
* nous devons utiliser **React.Children.map** pour cloner chaque enfant et injecter la ref associée de notre tableau privé de refs

Cela devrait faire l'affaire. Maintenant, refactorisons cela en utilisant les Hooks !

### Hooks

React 16.8 a introduit une nouvelle API appelée [Hooks](https://reactjs.org/docs/hooks-intro.html). Avec les Hooks, nous pouvons écrire moins de code et obtenir une empreinte plus petite sur notre base de code. De plus, les Hooks tirent parti des fonctions qui sont des citoyens de première classe en JavaScript. Si vous êtes familier avec les [composants fonctionnels sans état](https://hackernoon.com/react-stateless-functional-components-nine-wins-you-might-have-overlooked-997b0d933dbc) dans React, vous êtes à moitié là. Notre refactorisation initiale ressemblera à ceci :

Jusqu'à présent, nous utilisons toujours l'ancienne API React pour déclarer un composant fonctionnel sans état simple. Cependant, nous avons toujours besoin de ces fonctions de cycle de vie pour attacher notre gestionnaire au nœud **document**.

C'est là que le [Hook d'effet](https://reactjs.org/docs/hooks-effect.html) intervient. Le Hook d'effet remplacera nos méthodes « **componentDidMount** » et « **componentWillUnmount** ». Le Hook d'effet sera appelé juste après le rendu des composants, ce qui nous aidera à attacher notre gestionnaire souhaité à temps. De plus, pour la partie nettoyage, si le Hook d'effet retourne une fonction, cette fonction sera appelée juste avant que le composant ne soit démonté. C'est donc le bon moment pour faire un peu de nettoyage. Dans la prochaine refactorisation, les choses deviendront un peu plus claires.

C'est la forme finale de notre composant fonctionnel utilisant le Hook d'effet. Si vous voulez voir les deux exemples en action, vous pouvez les exécuter ci-dessous. (_Vous pouvez exporter par défaut soit le composant de classe, soit le composant fonctionnel et l'application se comportera de la même manière._)

### Conclusion

Bien que le comportement de clic à l'extérieur soit une fonctionnalité largement utilisée, il peut ne pas être si simple à implémenter dans React. Avec cet exemple, j'ai pris la liberté d'expérimenter un peu avec les Hooks React et de construire la solution de deux manières pour comparer les deux approches. Je suis un grand fan des composants fonctionnels, et maintenant avec l'aide des Hooks, nous pouvons les emmener au niveau supérieur.