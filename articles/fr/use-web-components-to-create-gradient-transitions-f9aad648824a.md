---
title: Comment utiliser les composants web pour créer des transitions de dégradé
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-21T15:34:47.000Z'
originalURL: https://freecodecamp.org/news/use-web-components-to-create-gradient-transitions-f9aad648824a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*LqPtF9fIss1cuVq3Ui_NFQ.gif
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment utiliser les composants web pour créer des transitions de dégradé
seo_desc: 'By Anthony Ng

  In this article, we will learn about Web Components. We will build a simple Web
  Component that transitions its gradient color.

  Web Components are a suite of different technologies that allow you to create reusable
  custom elements. Using...'
---

Par Anthony Ng

Dans cet article, nous allons apprendre les composants web. Nous allons construire un composant web simple qui fait une transition de couleur de dégradé.

Les composants web sont un ensemble de différentes technologies qui vous permettent de créer des éléments personnalisés réutilisables. Utiliser un élément personnalisé n'est pas différent d'utiliser une balise `<div` />. Vous pouvez créer des instances dans votre HTML. Vous pouvez créer une instance avec JavaScript. Vous pouvez attacher des écouteurs d'événements aux éléments personnalisés.

Avez-vous déjà regardé les spécifications HTML et pensé que les auteurs avaient oublié un élément important ? C'est la solution pour vous. Les éléments personnalisés fournissent un moyen pour les développeurs de construire leurs propres éléments DOM complets.

### Différence entre les éléments personnalisés et les composants web ?

Beaucoup utilisent les termes Éléments Personnalisés et Composants Web de manière interchangeable. Les composants web sont un ensemble de différentes technologies, qui incluent les Éléments Personnalisés, le Shadow DOM et les Imports HTML. Les Éléments Personnalisés ont leurs propres spécifications ([voir ici](https://w3c.github.io/webcomponents/spec/custom/)).

![Image](https://cdn-media-1.freecodecamp.org/images/zOs1VT88fIUcs85VeNqhgfE69BP2c0pxbXV0)
_Les composants web sont un ensemble de technologies ; Éléments Personnalisés, Shadow DOM et Imports HTML._

Les composants web sont une fonctionnalité native du navigateur. Vous n'avez pas besoin de bibliothèques externes pour utiliser cette fonctionnalité. [Vous pouvez voir le tableau de support des navigateurs ici, étiqueté Browser Support](https://www.webcomponents.org/).

![Image](https://cdn-media-1.freecodecamp.org/images/l40i29nr1vsn2E0ECU8eeDMXXO-je7YDEi4-)
_Support des navigateurs pour les composants web. [https://www.webcomponents.org/](https://www.webcomponents.org/" rel="noopener" target="_blank" title=")_

[Vous pouvez voir le support pour les Éléments Personnalisés ici.](https://caniuse.com/#feat=custom-elementsv1)
[Vous pouvez voir le support pour les templates ici.](https://caniuse.com/#feat=imports)
[Vous pouvez voir le support pour le Shadow DOM ici.](https://caniuse.com/#feat=shadowdomv1)

### Donc, c'est React ?

React et les composants web résolvent des problèmes différents. Les composants web fournissent une forte encapsulation pour les composants réutilisables. React fournit une bibliothèque déclarative qui maintient le DOM synchronisé avec vos données.
React ne fait aucune différenciation entre un élément HTML natif et un composant web. Il gérera votre composant web personnalisé comme il le fait pour un élément HTML normal.

[Voir cet exemple d'une application React utilisant un composant web.](https://codesandbox.io/s/746omm2kwq)

La documentation React montre également comment vous pouvez utiliser React dans vos composants web. Je n'ai pas trouvé de scénario qui justifierait l'importation de React.

### Faisons une transition de fond en dégradé

Nous allons construire un composant web de dégradé comme celui ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/gxsEyj4zN7CzzZcjB12Rc0VqRnJ7BPAI4K9v)
_Transitions de dégradé_

Remarquez comment il fait une transition entre les fonds en dégradé. Nous ne pouvons pas faire de transition de fonds par défaut. [Voir Codepen ici](https://codepen.io/newyork-anthonyng/pen/PyJJmr).

Mais nous pouvons faire une transition d'opacité. [Voir Codepen ici](https://codepen.io/newyork-anthonyng/pen/mzBBBg?editors=1100).

Nous pouvons tirer parti de cela avec les pseudo-classes CSS pour obtenir l'effet souhaité. [Voir Codepen ici](https://codepen.io/newyork-anthonyng/pen/MPEEPo?editors=1100).

Nous pouvons tirer parti de cela avec la pseudo-classe CSS "before" pour obtenir l'effet souhaité. [Voir Codepen ici](https://codepen.io/newyork-anthonyng/pen/MPEEPo?editors=1100).

![Image](https://cdn-media-1.freecodecamp.org/images/Fwq5p4QWSluZOlDi0swvtRhB5OgkvTZi1uYp)
_L'élément div a une opacité de 1 ; l'élément de pseudo-classe before a une opacité de 0_

Il y a une couche (`<div` />) avec une couleur de dégradé. Il y a une deuxième couche (`div::before`) avec une couleur de dégradé différente. Cette deuxième couche se superpose à la première couche et a une opacité de 0. Pour démarrer la transition de dégradé, nous faisons une transition de l'opacité de la deuxième couche de 0 à 1. Cela nous donne l'effet que le dégradé est en transition.

En tant que développeur, c'est beaucoup de choses que vous devez savoir. Ne serait-il pas agréable d'avoir un moyen simple et déclaratif d'utiliser ce dégradé ? Imaginez un élément HTML appelé `<my-gradient-background` />. Il accepte un attribut de dégradé qui prend une couleur de dégradé, comme "red, white, blue". Lorsque nous changeons le dégradé, la couleur du dégradé fera une transition comme nous le voulons. C'est ce que nous allons créer.

### Construction du composant web

![Image](https://cdn-media-1.freecodecamp.org/images/rZpCINGKIpc-T3QSPW9vyG1qsY5ddnvPgfDs)

Pour créer un nouveau composant web, nous déclarons une nouvelle classe qui étend HTMLElement.

![Image](https://cdn-media-1.freecodecamp.org/images/-QNrmEl0ncCgR7hs2Gs5v79faJeAdlD61Igr)

Si vous souhaitez étendre la fonctionnalité d'un élément HTML existant, vous pouvez étendre à partir de celui-ci. Par exemple, pour étendre la fonctionnalité d'un `<p` />, vous étendriez HTMLParagraphElement.

![Image](https://cdn-media-1.freecodecamp.org/images/E3Kxs-MK46C6uWdc9aDOPDOdPbgydwchYS6N)

Nous attachons une racine d'ombre à notre composant web. L'API Shadow DOM nous permet d'attacher du DOM à notre élément de dégradé. Ce Shadow DOM est encapsulé dans notre composant et est (généralement) caché du reste du DOM. [Vous pouvez en lire plus sur le Shadow DOM ici](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_shadow_DOM).

![Image](https://cdn-media-1.freecodecamp.org/images/m64g8vpFm9ryWuGMy8yGP6exiFMX3QO6YKXa)

Dans notre Shadow DOM, nous ajoutons un peu de style pour l'élément de dégradé. Nous utilisons un `<div class="after"` /> au lieu d'un pseudo-élément ici. Cela est dû au fait que nous voulons référencer cette couche avec JavaScript. Nous ne pouvons pas référencer les pseudo-éléments avec JavaScript.

![Image](https://cdn-media-1.freecodecamp.org/images/3DTLIwfMdYlbxTYpNhwDHgFzQeaW2cSOgLnQ)

L'élément `host` est l'élément de dégradé lui-même. Nous pouvons le styliser comme s'il s'agissait d'un élément `<div` />.

![Image](https://cdn-media-1.freecodecamp.org/images/u1gafpfh9Rs2nKyz1w4wKHRryJQIZhkrSzDM)

Dans les attributs observés, nous retournons une liste d'attributs HTML que nous voulons surveiller. Lorsque ces attributs surveillés changent, une fonction de rappel sera déclenchée.

![Image](https://cdn-media-1.freecodecamp.org/images/BnywZqFz6WTW-QUPfsr1IIkMH8ctQ4tY8dOw)

Notre fonction `attributeChangedCallback` est déclenchée chaque fois qu'un attribut observé change. Nous obtenons 3 arguments dans notre fonction de rappel. Le premier argument est le `nom` de l'attribut qui a changé. Le deuxième argument est la valeur de l'attribut avant qu'il ne change. Le troisième argument est la valeur de l'attribut après qu'il a changé.

Dans notre fonction de rappel, nous mettons à jour notre élément "after".

![Image](https://cdn-media-1.freecodecamp.org/images/UQ0BA-ZKRmrMonVL2bIWdkzg9xv7g-OyICxZ)

![Image](https://cdn-media-1.freecodecamp.org/images/PvW7g04cINRkGMvdr1XOL0IavdS38Wuw9Pc5)

Nous mettons à jour la couleur de fond de notre élément "after" avec la nouvelle couleur de dégradé. Nous définissons également son opacité à 1. Notre élément "after" commencera à s'estomper, créant notre effet souhaité. Nous voulons faire un peu de nettoyage lorsque l'élément "after" a fini de s'estomper.

![Image](https://cdn-media-1.freecodecamp.org/images/m6OuFsRHdn1iKcDvuJSrM5f99j4-duDsXlt1)

![Image](https://cdn-media-1.freecodecamp.org/images/U9YmQyTr8NLJeRMYDDL0LVLbnxQRszJCJ4-r)

Notre élément "after" fait tout le travail de création de l'effet de transition de dégradé. Nous définissons notre élément "host" avec la nouvelle couleur de dégradé. Nous cachons l'élément "after" pour qu'il soit prêt pour la prochaine estompe. C'est tout le nettoyage dont nous avons besoin.

![Image](https://cdn-media-1.freecodecamp.org/images/YF6prxikn49jklX7vUfzp9O3PePGQ5FBs7Av)

Pour utiliser ce nouveau composant web, nous devons le définir comme suit.

Maintenant, vous pourrez utiliser `<my-gradient-background` /> comme un élément HTML normal.

Vous pouvez voir le code complet [ici](https://github.com/newyork-anthonyng/my-gradient-background/blob/master/index.js). N'hésitez pas à le télécharger avec `npm install --save my-gradient-background`.

### Références

* [https://developers.google.com/web/fundamentals/web-components/customelements](https://developers.google.com/web/fundamentals/web-components/customelements)
* [https://www.webcomponents.org/introduction](https://www.webcomponents.org/introduction)
* [https://developer.mozilla.org/en-US/docs/Web/Web_Components](https://developer.mozilla.org/en-US/docs/Web/Web_Components)
* [https://reactjs.org/docs/web-components.html](https://reactjs.org/docs/web-components.html)
* [https://html.spec.whatwg.org/multipage/custom-elements.html#custom-elements](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-elements)
* [https://w3c.github.io/webcomponents/spec/custom/#custom-elements](https://w3c.github.io/webcomponents/spec/custom/#custom-elements)