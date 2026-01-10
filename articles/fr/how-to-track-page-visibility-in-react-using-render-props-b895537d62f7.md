---
title: Comment suivre la visibilité de la page dans React en utilisant les render
  props
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-05T22:40:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-track-page-visibility-in-react-using-render-props-b895537d62f7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*WsI4NrSVmdM-xjYDPa-Wgw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Render Props
  slug: render-props
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment suivre la visibilité de la page dans React en utilisant les render
  props
seo_desc: 'By Soumyajit Pathak

  In this article, we will create a simple reusable React component that tracks “Page
  Visibility State.”

  When creating a web application you may come across situations where you need to
  track the current visibility state of the app....'
---

Par Soumyajit Pathak

Dans cet article, nous allons créer un composant React simple et réutilisable qui suit l'« État de Visibilité de la Page ».

Lors de la création d'une application web, vous pouvez rencontrer des situations où vous devez suivre l'état de visibilité actuel de l'application. Vous devrez peut-être lire/mettre en pause une vidéo ou un effet d'animation, limiter certaines tâches intensives en performance ou simplement suivre le comportement de l'utilisateur pour l'analyse en fonction de si l'onglet du navigateur est actif ou non.

Maintenant, cette fonctionnalité semble assez simple à implémenter jusqu'à ce que vous essayiez réellement de l'implémenter pour la première fois. Il s'avère que suivre si l'utilisateur interagit activement avec l'application web ou non peut être assez délicat.

Il existe une API de Visibilité de Page qui fonctionne bien pour la plupart des cas, mais elle ne gère pas tous les cas possibles d'inactivité de l'onglet du navigateur. L'**API de Visibilité de Page** qui envoie un événement `visibilitychange` pour informer les écouteurs que l'état visible de la page a changé, ou présente certaines irrégularités. Elle ne déclenche pas l'événement dans certains cas même lorsque la fenêtre ou l'onglet du navigateur concerné est hors de vue ou hors focus.

Pour gérer certains de ces cas particuliers, nous devons utiliser une combinaison d'écouteurs d'événements `focus` et `blur` sur à la fois le `document` et l'élément `window`. Vous pouvez trouver une discussion détaillée à ce sujet [ici](https://stereologics.wordpress.com/2015/04/02/about-page-visibility-api-hidden-visibilitychange-visibilitystate/).

Nous allons implémenter la logique de contournement décrite dans le tutoriel mentionné ci-dessus dans une petite application React. Ne vous inquiétez pas, vous pouvez le lire plus tard — nous expliquerons chaque aspect de la logique que nous allons utiliser.

[**CodeSandbox**](https://codesandbox.io/embed/81x9n78qmj)  
[_CodeSandbox est un éditeur en ligne conçu pour les applications web._codesandbox.io](https://codesandbox.io/embed/81x9n78qmj)

Si vous souhaitez plonger dans le code ou regarder la démonstration, il est disponible sur [**Codesandbox**](https://codesandbox.io/s/81x9n78qmj) ainsi que sur [**Github**](https://github.com/drenther/react-page-visibility-example).

### Mise en route

![Image](https://cdn-media-1.freecodecamp.org/images/1*SZoc6eC41JBxJSQ_xODPrA.gif)
_La vidéo se met en pause lorsqu'elle est en arrière-plan_

Nous allons utiliser Codesandbox pour démarrer notre application React (vous pouvez également utiliser **create-react-app**). Nous allons créer une petite application qui aura un élément vidéo HTML5 qui ne se lira que lorsque l'onglet du navigateur est en focus ou actif, sinon il sera automatiquement mis en pause. Nous utilisons une vidéo car cela facilitera le test de la fonctionnalité de notre application.

Commençons par créer le composant le plus simple, c'est-à-dire le composant `Video`. Ce sera un composant simple qui recevra une prop Booléenne nommée `active` et une prop String nommée `src` qui contiendra l'URL de la vidéo. Si la prop `active` est vraie, alors nous lirons la vidéo. Sinon, nous la mettrons en pause.

Nous allons créer un simple composant de classe React. Nous allons rendre un simple élément vidéo avec sa source définie sur l'URL passée en utilisant la prop `src`, et nous utiliserons la nouvelle API `ref` de React pour attacher une `ref` au nœud DOM vidéo. Nous allons définir la vidéo en lecture automatique, en supposant que lorsque nous démarrons l'application, la page sera active.

Une chose à noter ici est que Safari ne permet plus la lecture automatique des éléments multimédias sans interaction de l'utilisateur. La méthode de cycle de vie `componentDidUpdate` est très pratique pour gérer les effets secondaires lorsque les props d'un composant changent. Par conséquent, ici, nous utiliserons cette méthode de cycle de vie pour lire et mettre en pause la vidéo en fonction de la valeur actuelle de `this.props.active`.

Les différences de préfixes des fournisseurs de navigateurs sont très ennuyeuses à gérer lors de l'utilisation de certaines API, et l'API de Visibilité de Page en fait certainement partie. Par conséquent, nous allons créer une fonction utilitaire simple qui gérera ces différences et nous retournera l'API compatible basée sur le navigateur de l'utilisateur de manière uniforme. Nous allons créer et exporter cette petite fonction à partir de **pageVisibilityUtils.js** sous le répertoire **src**.

Dans cette fonction, nous utiliserons un flux de contrôle basé sur une instruction if-else simple pour retourner l'API spécifique au navigateur. Vous pouvez voir que nous avons attaché le préfixe **ms** pour Internet Explorer et le préfixe **webkit** pour les navigateurs Webkit. Nous stockerons l'API correcte dans les variables de chaîne `hidden` et `visibilityChange` et les retournerons de la fonction sous la forme d'un simple objet. Enfin, nous exporterons la fonction.

Ensuite, nous passons à notre composant principal. Nous allons encapsuler toute notre logique de suivi de la visibilité de la page dans un composant de classe React réutilisable en exploitant le modèle **Render Props**. Nous allons créer un composant de classe appelé `VisibilityManager`. Ce composant gérera l'ajout et la suppression de tous les écouteurs d'événements basés sur le DOM.

Nous allons commencer par importer la fonction utilitaire que nous avons créée précédemment et l'invoquer pour obtenir les API spécifiques au navigateur correctes. Ensuite, nous allons créer le composant React et initialiser son état avec un seul champ `isVisible` défini sur `true`. Ce champ d'état Booléen sera responsable de refléter l'état de visibilité de notre page.

Dans la méthode de cycle de vie `componentDidMount` du composant, nous allons attacher un écouteur d'événement sur le document pour l'événement `visibilitychange` avec la méthode `this.handleVisibilityChange` comme gestionnaire. Nous allons également attacher des écouteurs d'événements pour les événements focus et blur sur le document ainsi que sur l'élément window. Cette fois, nous définirons `this.forceVisibilityTrue` et `this.forceVisibilityFalse` comme gestionnaires pour les événements focus et blur, respectivement.

Ensuite, nous allons créer la méthode `handleVisibilityChange` qui acceptera un seul argument `forcedFlag`. Cet argument `forceFlag` sera utilisé pour déterminer si la méthode est appelée à cause de l'événement `visibilitychange` ou des événements focus ou blur. Cela est dû au fait que les méthodes `forceVisibilityTrue` et `forceVisibilityFalse` ne font rien d'autre que d'appeler la méthode `handleVisibilityChange` avec les valeurs true et false pour l'argument `forcedFlag`.

À l'intérieur de la méthode `handleVisibilityChange`, nous vérifions d'abord si la valeur de l'argument `forcedFlag` est un Booléen (c'est parce que si elle est appelée à partir du gestionnaire d'événement `visibilitychange`, alors l'argument passé sera un objet [**SyntheticEvent**](https://reactjs.org/docs/events.html)).

Si c'est un Booléen, alors nous vérifions s'il est vrai ou faux. Lorsqu'il est vrai, nous appelons la méthode `setVisibility` avec true, sinon nous appelons la méthode avec false comme argument. La méthode `setVisibility` utilise la méthode `this.setState` pour mettre à jour la valeur du champ `isVisible` dans l'état du composant.

Mais, si `forcedFlag` n'est pas un Booléen, alors nous vérifions la valeur de l'attribut hidden sur le document et appelons la méthode `setVisibility` en conséquence. Cela conclut notre logique de suivi de l'état de visibilité de la page.

Pour rendre le composant réutilisable, nous utilisons le modèle Render Props. C'est-à-dire, au lieu de rendre un composant à partir de la méthode `render`, nous invoquons `this.props.children` en tant que fonction avec `this.state.isVisible`.

Enfin, nous montons notre application React sur le DOM dans notre fichier **index.js**. Nous importons nos deux composants React `VisibilityManager` et `Video` et créons un petit composant fonctionnel React `App` en les composant. Nous passons une fonction en tant qu'enfant du composant `VisibilityManager` qui accepte `isVisible` comme argument et le passe au composant `Video` dans son instruction return. Nous passons également une URL vidéo en tant que prop `src` au composant `Video`. C'est ainsi que nous consommons le composant `VisiblityManager` basé sur les Render Props. Enfin, nous utilisons la méthode `ReactDOM.render` pour rendre notre application React sur le nœud DOM avec l'id "root".

### Conclusion

Les API modernes des navigateurs deviennent vraiment puissantes et peuvent être utilisées pour faire des choses incroyables. La plupart de ces API sont de nature impérative et peuvent être délicates à utiliser parfois dans le paradigme déclaratif de React. L'utilisation de modèles puissants comme les Render Props pour envelopper ces API dans leurs propres composants React réutilisables peut être très utile.

_Publié à l'origine sur [able.bio](https://able.bio/drenther/track-page-visibility-in-react-using-render-props--78o9yw5)._