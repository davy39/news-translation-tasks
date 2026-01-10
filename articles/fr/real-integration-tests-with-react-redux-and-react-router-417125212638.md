---
title: Tests d'intégration réels avec React, Redux et Router
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-06-19T21:52:21.000Z'
originalURL: https://freecodecamp.org/news/real-integration-tests-with-react-redux-and-react-router-417125212638
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Vv0HNvRhU0ihKVaBIpDUww.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Redux
  slug: redux
- name: Testing
  slug: testing
seo_title: Tests d'intégration réels avec React, Redux et Router
seo_desc: 'By Marcelo Lotif

  After being bitten a couple of times by bad refactoring and a broken app — even
  with all my tests green — I started to research about integration tests in React.
  Possibly also with Redux and React Router.

  To my absolute shock, I coul...'
---

Par Marcelo Lotif

Après avoir été piégé à plusieurs reprises par de mauvais refactoring et une application cassée — même avec tous mes tests au vert — j'ai commencé à faire des recherches sur les tests d'intégration dans React. Possiblement aussi avec Redux et React Router.

À ma grande surprise, je n'ai pas trouvé de bon matériel sur le sujet. Ceux que j'ai trouvés faisaient soit des tests d'intégration incomplets, soit simplement de la mauvaise manière.

Alors ici, nous allons construire un test d'intégration qui initialise un composant React, déclenche une interaction utilisateur simulée et vérifie que notre composant change de la manière attendue.

Ce dont il **ne** s'agit **pas** : les tests unitaires. Je ne vais pas approfondir ce sujet maintenant, mais il y a une très bonne raison pour laquelle nous, chez [Wave](http://waveapps.com) ([nous recrutons](https://www.waveapps.com/about-us/jobs/), au fait !), ralentissons sur nos tests unitaires et passons aux tests d'intégration. Faites défiler jusqu'en bas si cela vous intéresse.

Divulgation : Je n'aurais pas eu ces tests fonctionnant aussi bien qu'ils le font maintenant sans les excellents développeurs front-end de Wave, surtout l'incroyable [Tommy Li](https://github.com/tommyzli) qui a découvert comment connecter le router, alors merci !

### Installation

Pour ce projet, nous allons utiliser [React](https://facebook.github.io/react/), [Redux](https://github.com/reactjs/react-redux), [React](https://github.com/ReactTraining/react-router)/[Redux Router](https://github.com/acdlite/redux-router) (optionnel) et [Thunk](https://github.com/gaearon/redux-thunk) (optionnel) pour exécuter l'application, [Jest](https://facebook.github.io/jest/) et [Enzyme](https://github.com/airbnb/enzyme) pour les tests.

Je vais sauter la configuration de tous ces outils, car il existe de nombreux tutoriels à ce sujet.

Pour configurer les bases de mon test d'intégration, je vais un peu tricher et créer une fonction utilitaire avec du code boilerplate :

### Test

Dans votre fichier de test, vous devrez d'abord importer certaines dépendances, votre reducer et votre composant :

Ensuite, dans la fonction _beforeEach_, configurez vos variables de test d'intégration en utilisant cette fonction utilitaire :

(Si vous n'utilisez pas React Router ou Thunk, vous pouvez simplement supprimer leurs références ici et dans la fonction utilitaire et cela fonctionnera de la même manière.)

Maintenant, vous êtes prêt à monter votre composant et à le tester. Imaginons que ce composant rend une _div_, qui affiche un texte provenant du reducer. Lorsque vous cliquez dessus, le texte doit changer pour une autre chaîne, disons 'nouveau texte'. Pour tester cette interaction, vous pouvez simplement faire :

C'est tout 😊 Avec ce code très simple, vous testez la _div_ appelant un producteur d'actions au clic, qui envoie une action au reducer, qui change les données, déclenchant un re-rendu du composant, qui est censé changer de la manière dont vous voulez qu'il change. Si l'une de ces étapes échoue, votre test devient rouge et vous savez que cette fonctionnalité de votre application ne fonctionne pas.

Vous pouvez essayer d'aller plus loin dans cette chaîne et vérifier d'autres choses :

### Test des appels API

Dans le monde réel, vous devrez probablement appeler des API pour récupérer des données pour votre application, et c'est la partie que vous devez simuler afin de tester les choses efficacement. Nous allons utiliser Jest ici, ce qui n'est pas la meilleure façon de simuler les requêtes http, mais je vais le faire pour la commodité.

En supposant que vous utilisez un client http hypothétique pour appeler un endpoint via sa fonction _get_ lorsque vous cliquez sur la _div_, puis définissez le retour de cet appel dans le reducer qui s'affiche à nouveau dans la _div_ :

Dans une application encore plus réelle, cette fonction _get_ vous retournera un objet Promise. Les choses deviennent un peu compliquées à partir de là car la fonction de clic simulée n'est pas consciente de cette promesse et il n'y a aucun moyen d'exécuter sa fonction _then_. La référence à l'objet a été perdue.

Nous devrons somehow attendre que cette promesse soit résolue avant d'exécuter les assertions. Nous contournons cela en faisant un petit hack dans une fonction utilitaire :

Et notre test va maintenant ressembler à ceci :

Avec l'instruction _async … await_, disponible depuis ES7, notre test va attendre que toutes les promesses soient résolues afin qu'il puisse faire ses assertions. Jest n'a actuellement aucune solution pour cela, mais ce hack fonctionne assez bien dans la vie réelle.

Si vous avez des producteurs d'actions plus compliqués avec d'autres promesses appelées dans le _resolve_ ou _reject_ de cette première promesse, je vous suggère de tester ces appels en unité et de tester également les résultats finaux de tous les cas dans les tests d'intégration.

### Plus de tests

Au cas où vous devriez définir un état initial pour votre composant, vous pouvez envoyer des actions manuellement jusqu'à atteindre l'état souhaité :

```
store.dispatch({ payload: 'data', type: 'SOME_ACTION' });
```

Vous pouvez également devenir fou sur ces assertions et tester chaque petite chose, ou garder cela simple en sachant que la couverture de test sera la même que si vous aviez ajouté des tests unitaires sur chacune des couches de cette application, mais avec beaucoup moins de code. De plus, vous testez également comment ces couches se connectent entre elles et comment votre application répond aux entrées utilisateur et aux changements de stockage de données.

Veuillez laisser votre opinion dans la section des commentaires, il y a beaucoup d'améliorations à apporter ici et je suis heureux de modifier cela selon vos suggestions. Merci !

### Y U NO UNIT TEST ?!?

Nous, chez [Wave](http://waveapps.com) (ai-je mentionné [nous recrutons](https://www.waveapps.com/about-us/jobs/) ?), avons fait une tonne de tests unitaires front-end avant et, pour être honnête, la majorité d'entre eux ont été quelque peu inutiles. Bien sûr, ils sont au cœur du TDD, mais certains tests unitaires de reducers et de producteurs d'actions sont simplement du code boilerplate et n'ajoutent pas beaucoup de valeur au code ou au processus TDD.

Vous pouvez en fait faire du très bon TDD avec uniquement des tests d'intégration, et ils seront utiles à l'avenir pour repérer les liens brisés entre les couches de votre application et finalement pour vérifier si votre application se comporte comme prévu, ce qui est le but des tests automatisés.

Ne vous méprenez pas, nous testons toujours en unité les cas limites qui sont trop compliqués ou ennuyeux à reproduire dans les tests d'intégration, mais la majorité de nos tests unitaires sont devenus inutiles dès que nous avons ajouté des tests d'intégration comme ci-dessus. En fin de compte, cela signifie que le temps que nous passons maintenant à réfléchir, développer et corriger les tests est beaucoup plus court qu'avant et ils sont beaucoup plus efficaces pour repérer les problèmes dans l'application. Donc, win win 😊

Un problème que vous pourriez rencontrer est avec le montage profond, au lieu du rendu shallow. Vous pourriez penser que certains arbres de composants sont trop compliqués à monter, mais je dirai qu'un autre avantage de monter le composant racine est de tester si les composants enfants sont instanciés correctement. Si vous avez des composants enfants connectés, vous pouvez les tester séparément si vous préférez. Je n'ai pas essayé de faire un rendu shallow d'un composant connecté pour voir si cette configuration de test d'intégration fonctionne toujours, mais vous pouvez essayer. Si vous n'aimez pas monter et n'avez pas de composants enfants connectés, une autre possibilité que je n'ai pas explorée est le rendu shallow puis la connexion manuelle. L'important ici est de se sentir à l'aise avec la quantité et la qualité des tests que vous écrivez, en vous assurant qu'ils aident réellement à faire automatiquement certains tests de régression et à découvrir des problèmes cachés pour vous.