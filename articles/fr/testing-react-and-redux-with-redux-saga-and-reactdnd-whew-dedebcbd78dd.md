---
title: Comment tester React et Redux avec Redux-saga et ReactDnD (ouf !)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-20T03:40:29.000Z'
originalURL: https://freecodecamp.org/news/testing-react-and-redux-with-redux-saga-and-reactdnd-whew-dedebcbd78dd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Nj1K70EQq51Vjec3Y4sXdQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Redux
  slug: redux
- name: Testing
  slug: testing
seo_title: Comment tester React et Redux avec Redux-saga et ReactDnD (ouf !)
seo_desc: 'By Gregory Beaver

  Helpers and systems to make testing easier


  This article is the one I wish I had found before I started coding using all the
  fanciness of React.

  I’m currently working on a complex offline-first eventually-consistent scheduling
  appli...'
---

Par Gregory Beaver

#### Aides et systèmes pour faciliter les tests

![Image](https://cdn-media-1.freecodecamp.org/images/mDoghGWaZYvcTbg5qiDXP6Z1zxDvskf0NsqS)

Cet article est celui que j'aurais aimé trouver avant de commencer à coder en utilisant toutes les fonctionnalités avancées de React.

Je travaille actuellement sur une application complexe de planification hors ligne, éventuellement cohérente, pour un programme de musique d'été afin de remplacer une application Mac écrite en Objective C il y a de nombreuses années.

L'application utilise :

* un backend Node.js en [Express](http://expressjs.com/), avec des données stockées dans [CouchDB](http://couchdb.apache.org/) avec [PouchDB](https://pouchdb.com/) dans le navigateur pour persister l'état entre les sessions et pour gérer la réplication et les conflits, et [React](https://facebook.github.io/react/) avec [Redux](http://redux.js.org/) sur le frontend, [Redux-saga](https://redux-saga.github.io/redux-saga/) pour gérer les événements asynchrones, et pour pimenter le tout, une touche de glisser-déposer avec [React-DnD](https://react-dnd.github.io/react-dnd/). C'est également une application pilotée par les tests, avec une couverture de test de 100 % et actuellement un ratio de 591 lignes de code source à 7040 lignes de code de test.

Les leçons que j'ai apprises sur la manière d'éviter les tests fragiles, les tests trop dépendants et de faciliter le test d'une seule chose dans un seul test sont encapsulées dans cet article.

D'abord, cet article suppose que vous allez transpiler es6 en utilisant [babel](https://babeljs.io/), ou l'utiliser directement dans les navigateurs de pointe. Si vous devez apprendre à faire cela, il existe de nombreuses ressources excellentes sur la manière de configurer babel avec [webpack](https://webpack.github.io/) ou d'autres bundlers pour servir votre application. Cet article se concentre **uniquement** sur la manière de tester les choses une fois que votre environnement est opérationnel.

### TL;DR

Consultez le source à [https://github.com/cellog/testHelper](https://github.com/cellog/testHelper)

Mais vous allez vouloir lire ceci !

### Pourquoi tout cela est-il important ?

Histoire ! J'ai commencé à coder il y a de nombreuses années et j'ai vu de nombreuses tendances venir et partir. La frénésie de l'orienté objet des années 80 et 90 a révolutionné la séparation du code, mais a conduit à un code difficile à maintenir. Lorsque j'ai étudié l'informatique (brièvement) au début des années 90, c'était un peu comme le Far West. Ils nous donnaient des problèmes, et nous bidouillions jusqu'à ce que cela fonctionne. Plus ou moins. Il n'y avait aucun moyen de vérifier le système sauf en exécutant votre programme et en comparant la sortie à la sortie attendue en tant qu'amas monolithique... clusterfantasy. Clusterfriend. Vous voyez l'idée.

À la fin des années 90, la programmation extrême est devenue une chose, et soudainement, il y avait des frameworks de test à utiliser. Avancez rapidement de près de 20 ans, et nous avons des frameworks matures, extensibles et rapides avec une véritable isolation du code afin que nous puissions tester sans effets secondaires et des langages qui rendent cela facile également, comme notre ami Javascript.

J'ai passé une quantité considérable d'efforts au fil des ans à expérimenter différentes stratégies de développement. La plupart du temps, je concevais du code et écrivais ensuite des tests une fois que je suis sûr que la conception était suffisamment solide pour commencer ce travail. C'était bien, sauf quand ce n'était pas, et quand ce n'était pas, c'était la catastrophe. Je trouvais que le code était en fait impossible à tester.

Un excellent exemple est un site web que j'ai codé en utilisant [Meteor](https://www.meteor.com/). Meteor était incroyable et m'a permis de passer de 0 à 60 avec un site web complexe et fonctionnel en environ un mois et demi. C'était si simple que les tests ne semblaient même pas nécessaires. Cependant, je suis tombé sur un bug subtil avec la manière dont MongoDB était structuré, et j'en ai maintenant trouvé 2 ou 3 autres que je ne peux littéralement pas corriger sans une réécriture complète. Lorsque Meteor a introduit les tests, ils étaient spécifiques à Meteor et ne facilitaient pas l'exécution des tests dans plusieurs navigateurs, et ne supportent pas du tout wallaby sans un monolithe gigantesque de wallaby.js qui aurait besoin de ses propres tests unitaires pour être sûr qu'il fonctionne. Je me réveillais littéralement avec des cauchemars en essayant de résoudre ce problème.

Alors pour ce projet, j'ai décidé d'écrire des tests dès le début, en expérimentant avec la conception pilotée par les tests. Ce que j'ai trouvé, c'est que l'écriture des tests en premier fait changer la conception dès le début, et mon code est devenu plus simple. J'ai commencé à développer une suspicion intuitive lorsque le code devenait trop complexe, et j'ai commencé à effacer de larges parties de code lorsque les tests devenaient difficiles, ou complexes de quelque manière que ce soit, puis à trouver des solutions beaucoup plus élégantes en moitié moins de temps après avoir recommencé à zéro. Voici le piège : le rythme de développement est environ 4 fois plus lent que ce à quoi j'étais habitué auparavant. Cependant, je ne m'inquiète pas des bugs subtils qui pourraient s'immiscer. Je ne m'inquiète pas de la conception globale qui soit fragile. Le sentiment de confiance est exaltant et me libère pour rêver de solutions au lieu d'éteindre des incendies.

De plus, je refactorise souvent, à mesure que j'en apprends davantage sur le système que je conçois et que je découvre des hypothèses incorrectes subtiles sur le fonctionnement réel des bibliothèques et de la base de données que j'utilise ou de mes choix de conception. Je me surprends souvent à effacer et à réutiliser du code. Parce que j'efface et que je déplace des choses si souvent, et que les lignes de code de mes tests sont 14 fois plus longues que les lignes de code réel, afin de développer à un rythme raisonnable, les tests doivent être conçus chirurgicalement pour éviter d'exploser à chaque petit changement. J'ai appris cela à la dure.

La plupart de mes premiers tests avaient des dépendances subtiles aux choix de conception qui, franchement, n'avaient pas d'importance pour ce test. Je me retrouvais à parcourir et à copier/coller des changements dans 20 tests ou plus lorsque je refactorisais. Alors je me suis assis et j'ai cherché des moyens de supprimer toute dépendance des tests, et j'ai abouti au système décrit dans cet article.

Chaque test ne teste qu'une seule chose, généralement juste une seule ligne de code, et aucun changement dans une autre zone du composant testé ne fera échouer un test, sauf pour les erreurs de compilation ou d'autres erreurs facilement corrigibles. Mon espoir est que mes erreurs au début vous aideront à les éviter. Avec cela en tête, plongeons !

### Commencer

Commençons par une liste des outils que nous allons utiliser, et où les trouver.

Voici la liste des imports dont nous aurons besoin :

Nous utiliserons des imports standard de React, Redux, les liaisons entre React et Redux, ainsi que le contexte pour React-DnD et son backend de test. Parlons de teaspoon.

[Teaspoon](https://github.com/jquense/teaspoon) est une création brillante de Jason Quense qui permet de tester les composants React comme s'ils étaient du HTML en utilisant une interface de type jQuery. Il permet de tester si des propriétés spécifiques ont été passées, de déclencher facilement des événements avec des données mock, et également de définir facilement des propriétés ou l'état des composants React. C'est magnifique. Allez lire la documentation. À tout à l'heure.

![Image](https://cdn-media-1.freecodecamp.org/images/prYklFTuJoGSSwOdMl-lc0ioWc4BhKOG3aYL)
_La recherche d'images Google pour des images libres n'est-elle pas amusante ?_

### Construire l'aide de test à partir de zéro

Bienvenue !

L'étape suivante consiste à construire l'interface de test de composant de base. Ce que nous devons faire en premier est de configurer le code de rendu du composant. J'ai expérimenté avec le rendu shallow et deep de teaspoon, et j'ai conclu qu'il n'y a jamais une bonne raison d'utiliser le rendu shallow.

Le problème principal avec le rendu shallow est que dans une semaine, vous aurez oublié que vous avez utilisé le rendu shallow lorsque vous refactorisez quelque chose, et votre test échouera sans bonne raison, vous forçant à perdre 15 minutes à essayer de comprendre pourquoi jusqu'à ce que vous réalisiez que tout ce que vous avez à faire est d'activer le rendu deep et le test passera.

Alors, nous commençons avec une simple fonction renderComponent que nous utiliserons pour rendre n'importe quel composant React, et l'envelopper dans teaspoon afin que nous puissions tester des choses à ce sujet :

Ce code accepte une classe ou une fonction de composant React, et passe toute propriété spécifiée dans les props. Simple.

Ensuite, nous devons connecter Redux afin que nous puissions gérer l'état :

Maintenant, nous pouvons écrire des tests pour nous assurer que les propriétés sont utilisées dans nos composants :

Plus d'informations sur la manière d'écrire des tests efficaces plus tard. Pour l'instant, continuons avec le problème suivant.

Bientôt, vous aurez besoin de tester le changement d'une propriété. Malheureusement, cela est difficile à faire car le rendu est asynchrone, et les tests sont synchrones par nature. Heureusement, il existe un moyen de forcer le rendu à être synchrone. Sans entrer dans trop de détails sur le pourquoi, l'utilisation d'un composant d'ordre supérieur pour envelopper votre classe de composant et définir les props en utilisant l'état local de React forcerait un re-rendu afin que nous puissions tester l'effet d'un changement de propriété. Voici la nouvelle renderComponent :

Ensuite, nous devons réfléchir à la manière de tester les composants conteneurs. D'après mon expérience, il est tentant d'essayer de tester la sortie HTML de la classe React interne de la même manière, mais il est beaucoup plus maintenable de tester ce que le conteneur fait réellement. Les classes conteneurs ont un seul travail : transformer l'état de redux en propriétés de composant React.

En utilisant teaspoon, vous pouvez vérifier que les conteneurs prennent une partie de l'état et créent de manière fiable les noms et valeurs de composants que le composant React interne attend, sans avoir besoin de connaître quoi que ce soit sur les internes du composant React à l'intérieur du test du conteneur.

L'exception la plus notable à ce fait est que nous devons également tester les actions. Pour ce faire, il est préférable de tester soit le changement d'état attendu lors d'une action dispatchée, soit de vérifier si l'action a été envoyée.

Pour tester l'état, nous devons accéder à l'état après qu'une action soit déclenchée, et nous pouvons le faire en utilisant la méthode getState() du store redux. Donc, nous devrons retourner le store si nécessaire.

La méthode la plus découplée consiste à vérifier si l'action correcte a été envoyée. Pour ce faire, nous devrons créer un middleware redux qui enregistre simplement toutes les actions dans un tableau qui peut ensuite être utilisé pour vérifier les actions envoyées. Modifions renderComponent pour rendre ces deux scénarios possibles :

La question de savoir comment utiliser cette fonctionnalité plus avancée sera abordée dans la seconde moitié de cet article, où je décrirai comment utiliser cet aide pour écrire des tests efficaces et limités.

La dernière partie de l'aide de test est assez simple et ajoute simplement le support pour React-DnD. Tout ce dont nous avons besoin est d'envelopper tout dans un DragDropContext avec le backend de test :

Maintenant, nous pouvons accéder au gestionnaire Draggable et au backend avec `Draggable.getManager()` et `Draggable.getManager().getBackend()` comme documenté dans les docs de React-DnD. Notez que le `.prototype` est requis afin d'accéder à getManager().

À ce stade, nous sommes prêts à explorer comment utiliser cet aide de test efficacement.

### Écrire de grands tests en utilisant l'aide

Il y a quelques principes clés qui informent la manière dont j'écris les tests :

1. ne répétez rien
2. utilisez un code boilerplate intelligent
3. testez les propriétés et les actions séparément

Voici un exemple d'un composant en cours de test qui a à la fois des propriétés et des actions. L'exemple utilise [sinon](http://sinonjs.org/) pour tester les callbacks :

Notez que si vous souhaitez tester le changement d'une propriété afin de tester une méthode de cycle de vie telle que shouldComponentUpdate, vous devez utiliser la méthode [props()](https://github.com/jquense/teaspoon#fnprops) de teaspoon. Il en va de même pour [state()](https://github.com/jquense/teaspoon#fnstate) pour tester les changements d'état local.

Le test ci-dessus utilise quelques idées unificatrices :

1. même renderComponent() est abstrait en 2 nouvelles méthodes, une pour tester les propriétés (render), et une pour tester les actions (make).
2. Un ensemble générique de propriétés par défaut est spécifié afin qu'il n'y ait aucun avertissement React pour aucun test, permettant à chaque test de se concentrer sur une seule propriété (aptement nommée « generic »).
3. Il n'y a pas de test des propriétés visuelles/css/html directement au-delà de la vérification que l'échafaudage de base est présent
4. Le test se concentre sur la vérification que l'entrée externe dans le composant est correcte. Chaque propriété est testée, et chaque action est testée.
5. CSS/HTML est uniquement utilisé pour localiser l'endroit où les propriétés sont situées dans le DOM virtuel du composant

Nous allons étendre ces idées pour tester les conteneurs connectés react-redux ensuite.

### Tester les composants conteneurs connectés à Redux

La chose la plus importante qu'un composant redux fait est de transformer l'état en propriétés et les callbacks en actions redux. En utilisant le renderComponent que nous avons créé, nous pouvons facilement tester cela :

Ici, nous pouvons tester exclusivement que notre conteneur de connexion transforme l'état en les propriétés que nous attendons, et dispatch les actions que nous attendons. Dans la plupart de mes premiers tests, je vérifiais pour m'assurer que les actions modifiaient l'état (la deuxième méthode dans le test doSomething), mais cela duplique en fait le travail de vérification que vos reducers réduisent. Ainsi, si vous refactorisez un reducer, vous devez mettre à jour chaque test pour un conteneur connecté. Cela peut rendre le refactoring plus lent.

Au lieu de cela, vérifier quelles actions ont été dispatchées est complètement découplé du reducer, et vérifie simplement le contrat pour le composant connecté.

Il y a des inconvénients au découplage, dans le sens où un changement de reducer pourrait avoir plusieurs effets secondaires dans les conteneurs. Si vous en êtes conscient, alors vous êtes bien. Dans un environnement multi-développeurs, ou lorsque vous développez une amnésie quelques mois plus tard, vous pourriez vouloir que tout ce qui est connecté au reducer échoue lorsqu'un changement est fait.

### Tester un gestionnaire d'actions redux-saga

Si vous souhaitez tester un générateur redux-saga, cela est très bien documenté sur le site redux-saga. Si vous trouvez cela trop confus, et que vous souhaitez un article sur la manière dont je le fais (ou pourquoi j'ai choisi redux-saga), veuillez répondre dans les commentaires.

L'un des motifs que j'ai rencontrés dans cette application et qui nécessite redux-saga est la transformation d'une seule action en plusieurs actions. Le cas d'utilisation pour cela dans mon application de planification est l'écouteur que j'ai écrit pour mettre à jour l'instance CouchDB lorsque des enregistrements sont modifiés par le client. Afin de mettre en œuvre une détection de conflit appropriée pendant que les enregistrements sont mis à jour indépendamment en ligne, chaque enregistrement doit avoir le même identifiant. Ainsi, des identifiants uniques sont générés en fonction des noms des compositeurs des morceaux que les enfants pourraient jouer. Lorsque le nom d'un compositeur est mis à jour, chaque instance de l'utilisation de ce compositeur doit également être mise à jour. Ainsi, une seule action génère de nombreuses nouvelles actions. En raison du potentiel d'actions manquantes et d'état incohérent dans la base de données, j'ai écrit une saga pour écouter l'action de modification, puis envoyer de nombreuses nouvelles actions pour apporter les modifications nécessaires.

Ainsi, lors du clic sur un bouton d'enregistrement, une action est envoyée qui n'est pas gérée par un reducer. Au lieu de cela, elle est interceptée par la saga, et transformée en les nombreuses actions individuelles nécessaires. Elle met également à jour la base de données.

Cela aurait pu être mis en œuvre avec un middleware, mais redux-saga rend la gestion de toutes les parties asynchrones du travail si facile qu'il n'a pas de sens de réinventer la roue lorsque quelques lignes de code peuvent faire le même travail et être plus facilement testées. Comment tester cela ? Nous pourrions configurer un écouteur mock redux-saga pour l'action dans notre aide de test, mais combien de temps devons-nous attendre que la saga se termine avant de tester notre état pour nous assurer qu'il a été modifié ? Comment empêcher la saga d'essayer de modifier une base de données ? Un cauchemar s'ensuit !

En bref : dans ce cas, tout ce que nous devons vérifier est que le composant connecté dispatch l'action qui sera interceptée par la saga redux-saga. Un test séparé peut être utilisé pour vérifier la justesse de la saga elle-même. Une fois cela confirmé, nous pouvons être sûrs que l'action fonctionnera.

Ainsi, nous pouvons utiliser le middleware de journalisation que nous avons créé dans notre aide de test pour voir si l'action que nous avions l'intention d'envoyer est effectivement envoyée. Facile !

### Tester React-DnD

React-DnD a besoin d'un contexte de glisser-déposer pour fonctionner sans erreurs, même si vous ne faites rien avec le glisser-déposer dans le test. Si vous avez enveloppé l'un de vos composants, vous voudrez toujours pouvoir tester la fonctionnalité de base de ce composant, et notre aide de test rend cela possible. Vous pouvez tester la fonctionnalité de base en utilisant notre aide de test, et ignorer le glisser-déposer, puis tester le glisser-déposer dans un test séparé en utilisant les méthodes décrites dans la documentation de React-DnD si nécessaire. Très facile !

Le seul piège que j'ai trouvé est qu'il n'est pas intuitif de savoir comment simuler le glisser-déposer, et la documentation est inégale au mieux. Voici un test d'exemple de mon projet réel montrant comment tester l'interaction de glisser-déposer. Notez que les composants en question sont des composants dumb, et les propriétés `book` et `clear` sont des callbacks fournis par le composant conteneur connecté à redux. J'inclurai le conteneur même s'il n'est pas réellement testé par ces tests pour rendre cela plus clair. Notez également la création de fonctions d'aide pour extraire le sourceId et le targetId directement du composant, définies comme les fonctions `source` et `target` dans Slot.test.js.

### Outils que j'utilise et qui ont sauvé ma vie de programmeur

Si vous n'avez pas investi dans wallaby.js ou WebStorm, vous passez à côté de quelque chose. Avoir des résultats de test instantanés, une couverture de test instantanée visible ligne par ligne ainsi que votre intégration continue avec karma est une bénédiction. J'utilise karma sur BrowserStack pour vérifier que le code ne se casse pas dans les navigateurs mobiles et de bureau, et wallaby pour vérifier rapidement que mon code fonctionne et est couvert avant le commit.

Voici un exemple de wallaby.js que j'utilise pour mon projet, avec support pour les modules CSS dans les tests :

De plus, si vous n'utilisez pas [React-Storybook](https://getstorybook.io/), vous passez à côté de quelque chose. C'est le meilleur moyen de développer l'apparence visuelle de votre application avec une certaine assurance qu'elle fonctionnera. Il systématise les tests manuels, le dernier élément de toute application réussie, et les versions récentes peuvent même automatiser ces tests, bien que je ne l'aie pas utilisé personnellement.

### Conclusion

Il existe de nombreuses façons différentes de tester. Si vous développez une application complexe en react-redux, vous voudrez examiner attentivement comment découpler vos composants afin qu'ils puissent être facilement testés. Heureusement, avec cette aide de test simple et des principes de conception de test, les tests sont faciles, et vous pouvez refactoriser avec des effets secondaires limités sur les tests non liés, rendant le développement rapide et le changement facile.

Bon codage ! Laissez un commentaire si vous avez d'autres systèmes que je n'ai pas mentionnés, je suis toujours à la recherche de nouvelles idées. De plus, si quelque chose que j'ai dit n'est pas clair ou incomplet, veuillez demander et je suis heureux d'essayer de clarifier.

Cliquez également sur ce joli bouton de cœur, si vous avez aimé l'article !