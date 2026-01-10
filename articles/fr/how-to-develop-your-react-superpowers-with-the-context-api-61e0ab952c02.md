---
title: Comment développer vos superpouvoirs React avec l'API Context
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-19T19:37:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-develop-your-react-superpowers-with-the-context-api-61e0ab952c02
coverImage: https://cdn-media-1.freecodecamp.org/images/0*XUtWIwT2DgPoLkd5
tags:
- name: coding
  slug: coding
- name: freeCodeCamp.org
  slug: freecodecamp
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
seo_title: Comment développer vos superpouvoirs React avec l'API Context
seo_desc: 'By Eduardo Vedes

  Hey everyone! ❤️

  This time I’m going to show how to use the Context API in React.

  Context provides a way to pass data through the component tree without having to
  pass props down manually along every level.

  React typically works with...'
---

Par Eduardo Vedes

Salut à tous ! ❤️

Cette fois-ci, je vais vous montrer comment utiliser l'API Context dans React.

Context fournit un moyen de transmettre des données à travers l'arborescence des composants sans avoir à passer manuellement les props à chaque niveau.

React fonctionne généralement avec un flux de données de haut en bas (parent vers enfant). Cela fonctionne très bien en cascade de props, donnant toujours au DOM virtuel la capacité de vérifier et de déclencher des re-rendus lorsqu'ils sont nécessaires.

Nous avons également un état local à l'intérieur de chaque composant stateful pour gérer les changements, permettant à l'utilisateur de modifier les données qui sont propagées via les props.

Lorsque nous voulons abstraire un peu plus, nous pouvons utiliser [Redux](https://redux.js.org/) pour abstraire l'état ou les props vers un magasin "externe", une seule source de vérité — si vous n'avez pas lu mon article sur [Comment se lancer avec Redux en dix minutes](https://www.freecodecamp.org/news/redux-get-the-ball-rolling-in-10min-9d9551ff4b3c/), n'hésitez pas à le faire !

Même avec tous ces outils dans la ceinture à outils, il peut être fastidieux de gérer certains types de données (props, état, etc.) à l'intérieur de notre application.

**Imaginez les informations de l'utilisateur actuellement authentifié**, **les thèmes**, **la locale** ou **même les données liées à la langue**.

**Ce sont des informations qui sont considérées comme "globales" dans un arbre de composants React. Une fois que vous changez ces informations, toute l'application doit se re-rendre pour se mettre à jour.**

**Context est conçu pour partager des données qui peuvent être considérées comme "globales".**

**Alors, pour comprendre cela, mettons-nous au travail ! Si vous le souhaitez, vous pouvez cloner mon dépôt GitHub [ici](https://github.com/evedes/context-api) et jouer un peu avec ces choses que nous allons faire :**

### **01. Mettons-nous au travail**

**Construisons une App, qui a un Dashboard.**

**À l'intérieur du Dashboard, il y a un Widget qui rend un Bouton Thématique.**

**Le Bouton Thématique permet à l'utilisateur de changer le thème de l'App.**

**Quelque chose comme ceci :**

![Image](https://cdn-media-1.freecodecamp.org/images/6MtkhVhYrMlECQeAxuheRqIg3KoaxjSdyXXn)
_Image de l'App_

**Alors, commençons par notre composant App :**

![Image](https://cdn-media-1.freecodecamp.org/images/2EqqvPMMI15R9OCIkgOlUl8sdQvtGJ4TGcVr)
_Composant App_

**Ce composant a un état, une méthode `changeTheme` et un rendu qui rend le composant `<Dashboard />`.**

![Image](https://cdn-media-1.freecodecamp.org/images/oSyRro0zLaTZDxeupfrGsEbvDC0sQnWJkNFH)
_Composant Dashboard_

**Le composant Dashboard reçoit des props et rend un composant Widget en passant les props `changeTheme` et theme.**

![Image](https://cdn-media-1.freecodecamp.org/images/4c8zM8aEJ-X8Z97TM5KZV5r1pITAAPfeebQr)
_Composant Widget_

**Le composant Widget reçoit des props de son parent et rend un Bouton en lui passant les props `changeTheme` et theme.**

![Image](https://cdn-media-1.freecodecamp.org/images/DiKuckapUyedtersEvx4XKMlCy114dILkFXP)
_Composant Bouton_

**Le Bouton reçoit les props de son parent et les utilise enfin pour rendre un bouton avec une `className` qui dépend du thème choisi par l'utilisateur.**

**Le Bouton permet également à l'utilisateur de changer le thème de rouge à bleu et vice-versa. C'est pourquoi il a un gestionnaire `onClick` qui déclenche la méthode `changeTheme` passée de haut en bas depuis le composant App -> Dashboard -> Widget -> Bouton.**

**Comme vous le voyez tous, cela fait beaucoup de props, beaucoup de complexité, beaucoup de code répété, beaucoup de ?.**

**Alors, à ce moment-là, vous vous demandez comment pouvons-nous éviter cela ? Comment pouvons-nous abstraire toutes ces choses liées au thème et rendre notre code plus propre ?**

**La réponse à cela est d'utiliser l'API Context fournie par React !!**

### **02. Implémentation de l'API Context**

**D'accord, commençons par le commencement.**

**Prenons toute la complexité liée au thème en dehors de notre composant principal App.**

![Image](https://cdn-media-1.freecodecamp.org/images/ezlk3BhbsT4QLsjJobmLVFMF9ztfb7U1sGGG)
_ThemeContext et ThemeProvider_

**Pour cela, nous avons commencé par créer un `ThemeContext` en utilisant `React.createContext()`.**

**Ensuite, nous avons créé un composant stateful appelé `ThemeProvider` qui gérera l'état, la méthode `changeTheme` qui est spécifique à cette préoccupation de thème.**

**Dans la méthode de rendu, nous retournerons le <ThemeContext.Provider> avec les props `value` qui contiennent tout ce que nous voulons propager. Ce composant embrassera les { this.props.children } en utilisant le motif render props.**

> **Au fait, si vous voulez en savoir plus sur le motif render props, ne manquez pas mon article à ce sujet [ici](https://medium.freecodecamp.org/how-to-develop-your-react-superpowers-with-the-render-props-pattern-b74e68c6d053).**

**De cette façon, nous pouvons injecter dans tout ce que le <ThemeProvider /> embrasse les props de valeur avec notre état et la méthode changeTheme.**

**D'accord, l'étape suivante consiste à nettoyer toutes les props ? que nous avons passées dans notre flux parent-enfant de haut en bas et, très important, à envelopper le retour de notre composant App dans notre composant <ThemeProvider/> — cela donnera du "contexte" à notre App ?.**

![Image](https://cdn-media-1.freecodecamp.org/images/RTL2t1GEAdEdAni6TwyC6SPN6LHF815ZyXzX)

**C'est beaucoup plus propre maintenant, tout le monde ! ❤️ Je suis si heureux avec ça ! ?**

**Concentrons-nous sur notre composant Bouton :**

![Image](https://cdn-media-1.freecodecamp.org/images/IeENT3TT5mmn6El3raVFbw2PSDuw8f4XayxP)

**Eh bien, ici nous avons simplement connecté le composant <ThemeContext.Consumer> et à l'intérieur, nous avons passé une fonction à rendre en tant qu'enfant avec le contexte.**

**Pour ceux d'entre vous qui ne sont pas au courant, cette notation <> </> est la même que faire <React.Fragment>;</React.Fragment>.**

### **03. Conclusion**

**Je me suis tellement amusé avec ça, tout le monde ! Nous avons pu encapsuler toute la logique de thème à l'intérieur d'un composant approprié appelé <ThemeProvider>.**

**Nous avons injecté le contexte là où nous en avions besoin. Dans ce cas, c'était dans le composant <App> mais cela pourrait être fait n'importe où au-dessus de l'endroit où nous voulons consommer les données.**

**En fin de compte, nous avons consommé les données au point requis. Dans ce cas, c'était dans un composant Bouton.**

**Nous avons nettoyé notre application de tout le flux de props de haut en bas.**

**C'est un gagnant-gagnant, mes amis ! ?**

**Merci beaucoup, et n'oubliez jamais de "Rester Fort et Continuer à Coder !" ?**

### **04. Bibliographie**

**01. [Documentation React](https://reactjs.org/docs/getting-started.html)**

**evedes, Jan2019**