---
title: 'Où stocker les données des composants React : state, store, static et this'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-08-13T07:33:11.000Z'
originalURL: https://freecodecamp.org/news/where-do-i-belong-a-guide-to-saving-react-component-data-in-state-store-static-and-this-c49b335e2a00
coverImage: https://cdn-media-1.freecodecamp.org/images/1*kt9otqHk14BZIMNruiG0BA.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Redux
  slug: redux
- name: Web Development
  slug: web-development
seo_title: 'Où stocker les données des composants React : state, store, static et
  this'
seo_desc: 'By Sam Corcos

  With the advent of React and Redux, a common question has emerged:


  What should I hold in the Redux store, and what should I save in local state?


  But this question is actually too simplistic, because there are also two other ways
  you c...'
---

Par Sam Corcos

Avec l'avènement de [React](https://facebook.github.io/react/) et [Redux](https://github.com/reactjs/redux), une question courante a émergé :

> Que devrais-je mettre dans le **store** Redux, et que devrais-je sauvegarder dans le **state** local ?

Mais cette question est en réalité trop simpliste, car il existe également deux autres façons de stocker des données pour une utilisation dans un composant : **static** et **this**.

Passons en revue ce que chacun de ces éléments représente et quand vous devriez les utiliser.

### State local

Lorsque React a été introduit pour la première fois, nous avons découvert le **state** local. L'important à savoir sur le **state** local est que lorsqu'une valeur de **state** change, cela déclenche un re-rendu.

Ce state peut être passé aux enfants sous forme de **props**, ce qui vous permet de séparer vos composants entre des composants intelligents de données et des composants de présentation simples si vous le souhaitez.

Voici une application de compteur basique utilisant le **state** local :

Vos données (la valeur du compteur) sont stockées dans le composant **App**, et peuvent être passées à ses enfants.

#### Cas d'utilisation

En supposant que votre compteur est important pour votre application, et qu'il stocke des données qui seraient utiles à d'autres composants, vous ne voudriez pas utiliser le **state** local pour conserver cette valeur.

La meilleure pratique actuelle est d'utiliser le **state** local pour gérer l'état de votre interface utilisateur (UI) plutôt que les données. Par exemple, utiliser un [composant contrôlé](https://facebook.github.io/react/docs/forms.html#controlled-components) pour remplir un formulaire est une utilisation parfaitement valide du **state** local.

Un autre exemple de données d'UI que vous pourriez stocker dans le **state** local serait l'onglet actuellement sélectionné dans une liste d'options.

Une bonne façon de déterminer quand utiliser le **state** local est de considérer si la valeur que vous stockez sera utilisée par un autre composant. Si une valeur est spécifique à un seul composant (ou peut-être à un seul enfant de ce composant), alors il est sûr de garder cette valeur dans le **state** local.

**À retenir :** gardez l'état de l'UI et les données transitoires (comme les entrées de formulaire) dans le **state** local.

### Store Redux

Puis, après un certain temps et une fois que tout le monde a commencé à se familiariser avec l'idée de [flux de données unidirectionnel](https://www.youtube.com/watch?v=i__969noyAM), nous avons obtenu Redux.

Avec Redux, nous obtenons un **store** global. Ce store vit au plus haut niveau de votre application et passe les données à tous les enfants. Vous vous connectez au **store** global avec le wrapper [**connect** et une fonction **mapStateToProps**](https://github.com/reactjs/react-redux/blob/master/docs/api.md#connectmapstatetoprops-mapdispatchtoprops-mergeprops-options).

![Image](https://cdn-media-1.freecodecamp.org/images/1*jXzqMnnrXfePvfVglIYm5Q.jpeg)

Au début, les gens mettaient tout dans le **store** Redux. Utilisateurs, modales, formulaires, sockets... vous l'appelez.

Ci-dessous se trouve la même application de compteur, mais utilisant Redux. L'important à noter est que **counter** provient maintenant de **this.props.counter** après avoir été mappé depuis **mapStateToProps** dans la fonction **connect**, qui prend la valeur **counter** du **store** global et la mappe aux **props** du composant actuel.

Maintenant, lorsque vous cliquez sur le bouton, une action est dispatchée et le **store** global est mis à jour. Les données sont gérées en dehors de notre composant local et sont passées.

Il est utile de noter que lorsque les **props** sont mises à jour, cela déclenche également un re-rendu— tout comme lorsque vous mettez à jour le **state**.

#### Cas d'utilisation

Le **store** Redux est idéal pour conserver l'état de l'application plutôt que l'état de l'UI. Un exemple parfait est le statut de connexion d'un utilisateur. De nombreux composants auront besoin d'accéder à cette information, et dès que le statut de connexion change, tous ces composants (ceux qui sont rendus, au moins) devront être re-rendus avec les informations mises à jour.

Redux est également utile pour déclencher des événements pour lesquels vous avez besoin d'un accès sur plusieurs composants ou à travers plusieurs routes. Un exemple de cela serait une modale de connexion, qui peut être déclenchée par une multitude de boutons dans toute votre application. Plutôt que de rendre conditionnellement une modale dans une douzaine d'endroits, vous pouvez la rendre conditionnellement au niveau supérieur de votre application et utiliser une action Redux pour la déclencher en changeant une valeur dans le **store**.

**À retenir :** gardez les données que vous avez l'intention de partager entre les composants dans le **store**.

### this.<quelquechose>

L'une des fonctionnalités les moins utilisées lors de l'utilisation de React est **this**. Les gens oublient souvent que React n'est que du JavaScript avec la syntaxe ES2015. Tout ce que vous pouvez faire en JavaScript, vous pouvez aussi le faire en React.

L'exemple ci-dessous est une application de compteur fonctionnelle, similaire aux deux exemples ci-dessus.

Nous stockons la valeur **counter** dans le composant et utilisons [forceUpdate()](https://facebook.github.io/react/docs/component-api.html#forceupdate) pour re-rendre lorsque la valeur change. *C'est parce que les changements apportés à autre chose que **state** et **props** ne déclenchent pas de re-rendu*.

Ceci est en réalité un exemple de la façon dont vous ne devriez *pas* utiliser **this**. Si vous vous retrouvez à utiliser **forceUpdate()**, vous faites probablement quelque chose de mal. Pour les valeurs dont un changement devrait déclencher un re-rendu, vous devriez utiliser le **state** local ou les **props**/**store** Redux.

#### Cas d'utilisation

Le cas d'utilisation pour **this** est de stocker des valeurs dont un changement ne devrait pas déclencher un re-rendu. Par exemple, les sockets sont une chose parfaite à stocker sur **this**.

De plus, beaucoup de gens ne réalisent pas qu'ils utilisent déjà **this** tout le temps dans leurs définitions de fonctions. Lorsque vous définissez **render()**, vous définissez en réalité **this.prototype.render = function()**, mais cela est caché derrière la syntaxe de classe ES2015.

**À retenir :** utilisez **this** pour stocker des choses qui ne devraient pas déclencher un re-rendu.

### Static

Les méthodes et propriétés [**static**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/static) sont peut-être l'aspect le moins connu des classes ES2015 *(calmez-vous, oui, je sais qu'elles ne sont pas vraiment des classes sous le capot)*, principalement parce qu'elles ne sont pas utilisées très fréquemment. Mais elles ne sont en réalité pas particulièrement compliquées. Si vous avez utilisé [**PropTypes**](https://facebook.github.io/react/docs/reusable-components.html#prop-validation), vous avez déjà défini une propriété **static**.

Les deux blocs de code suivants sont identiques. Le premier montre comment la plupart des gens définissent PropTypes. Le second montre comment vous pouvez les définir avec **static**.

Comme vous pouvez le voir, **static** n'est pas si compliqué. C'est juste une autre façon d'assigner une valeur à une classe. *La principale différence entre **static** et **this** est que vous n'avez pas besoin d'instancier la classe pour accéder à la valeur*.

Dans l'exemple ci-dessus, vous pouvez voir que pour obtenir la valeur **staticProperty**, nous pourrions simplement l'appeler directement depuis la classe sans l'instancier, mais pour obtenir **prototypeProperty**, nous avons dû l'instancier avec **new App()**.

#### Cas d'utilisation

Les méthodes et propriétés statiques sont rarement utilisées, et devraient être utilisées pour des fonctions utilitaires dont tous les composants d'un type particulier auraient besoin.

**PropTypes** sont un exemple de fonction utilitaire que vous attacheriez à quelque chose comme un composant Button, puisque chaque bouton que vous rendez aura besoin de ces mêmes valeurs.

Un autre cas d'utilisation est si vous êtes préoccupé par la sur-récupération de données. Si vous utilisez GraphQL ou Falcor, vous pouvez spécifier quelles données vous voulez recevoir de votre serveur. Ainsi, vous ne recevez pas beaucoup plus de données que vous n'en avez réellement besoin pour votre composant.

Ainsi, dans l'exemple de composant ci-dessus, avant de demander les données pour un composant particulier, vous pourriez rapidement obtenir un tableau de valeurs requises pour votre requête avec **App.requiredData**. Cela vous permet de faire une demande sans sur-récupération.

**À retenir :** vous n'allez probablement jamais utiliser **static**.

### Cette autre option...

Il existe en réalité une autre option, que j'ai intentionnellement laissée hors du titre parce que vous devriez l'utiliser avec parcimonie : vous pouvez stocker des choses dans une variable de portée de module.

Il existe des situations spécifiques dans lesquelles cela a du sens, mais pour la plupart, vous ne devriez simplement pas le faire.

Vous pouvez voir que cela est presque identique à l'utilisation de **this**, sauf que nous stockons la valeur en dehors de notre composant, ce qui pourrait causer des problèmes si vous avez plus d'un composant par fichier. Vous pourriez vouloir utiliser cela pour définir des valeurs par défaut si les valeurs ne sont pas liées à votre **store**, sinon l'utilisation d'un **static** pour les props par défaut serait meilleure.

Si vous avez besoin de partager des données entre les composants et que vous souhaitez garder les données disponibles pour tout le module, il est presque toujours préférable d'utiliser votre **store** Redux.

**À retenir :** n'utilisez pas de variables de portée de module si vous pouvez l'éviter.

*Sam Corcos est le développeur principal et co-fondateur de [Sightline Maps](http://sightlinemaps.com), la plateforme la plus intuitive pour l'impression 3D de cartes topographiques, ainsi que de [LearnPhoenix.io](http://learnphoenix.io), un site de tutoriels intermédiaires-avancés pour construire des applications de production scalables avec Phoenix et React. Obtenez 20 $ de réduction sur LearnPhoenix avec le code promo : **free_code_camp*