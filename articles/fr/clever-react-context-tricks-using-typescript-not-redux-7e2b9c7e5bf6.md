---
title: Astuces intelligentes avec le Context de React en utilisant TypeScript — pas
  Redux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-12T16:32:26.000Z'
originalURL: https://freecodecamp.org/news/clever-react-context-tricks-using-typescript-not-redux-7e2b9c7e5bf6
coverImage: https://cdn-media-1.freecodecamp.org/images/0*P698jwSEpcmSgYYS
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
- name: TypeScript
  slug: typescript
seo_title: Astuces intelligentes avec le Context de React en utilisant TypeScript
  — pas Redux
seo_desc: 'By Bill Girten

  by Bill Girten, Martin Maza, and Alison Stuart


  TLDR; Leverage React’s Context API as a light and powerful alternative to Redux.

  Let’s face it: when we first started to play with React, it was like a sugar rush.
  Just create a .jsx file...'
---

Par Bill Girten

par [Bill Girten](https://www.freecodecamp.org/news/clever-react-context-tricks-using-typescript-not-redux-7e2b9c7e5bf6/undefined), Martin Maza, et [Alison Stuart](https://www.freecodecamp.org/news/clever-react-context-tricks-using-typescript-not-redux-7e2b9c7e5bf6/undefined)

![Image](https://cdn-media-1.freecodecamp.org/images/-rYMEN2Cedi7XnC9ruyiJK5U3gztNeyKN1cO)

**TLDR;** Utilisez l'[API Context de React](https://reactjs.org/docs/context.html) comme une alternative légère et puissante à Redux.

Admettons-le : lorsque nous avons commencé à jouer avec React, c'était comme un rush de sucre. Il suffit de créer un fichier .jsx, d'ajouter quelques dépendances, et Wham-O ! — des pages ultra-rapides.

C'est là que l'excitation commence.

Avant que vous ne le sachiez, vous vous sentez sans limites en concevant la couche de présentation de votre application à une vitesse fulgurante. Puis vous avez cette idée folle de faire un appel AJAX à un microservice et de gérer l'état de l'application.

C'est là que la douleur commence...

Alors vous fouillez l'incroyable Internet d'Al Gore et découvrez que la solution privilégiée pour gérer l'état de l'application est [Redux](http://www.redux.js.org) de [Dan Abramov](https://www.freecodecamp.org/news/clever-react-context-tricks-using-typescript-not-redux-7e2b9c7e5bf6/undefined). Maintenant, vous apprenez les Actions, les Reducers et les Stores et vous plongez dans [ImmutableJS](https://facebook.github.io/immutable-js/) juste pour pouvoir gérer l'état. Après avoir utilisé mapStateToProps, votre composant React est généralement engagé dans ce qui est populairement appelé le "[prop drilling](https://blog.kentcdodds.com/prop-drilling-bb62e02cb691)".

Initialement, vous êtes d'accord pour passer des propriétés de parent à enfant et, parfois, à petit-enfant. Cependant, à mesure que l'application devient plus complexe, vous remarquez que parfois vous passez certaines propriétés à travers l'arbre des composants qui ne sont _pas utilisées_ par un composant descendant donné.

Maintenant, que faire ?!? Vous voulez pouvoir gérer l'état de l'application, _mais_ vous voulez le faire sans passer de propriétés à travers la hiérarchie. Il est temps pour quelques astuces intelligentes.

### **Comment l'API Context de React aide**

Facebook a publié l'API Context dans React v16.3 comme un mécanisme pour passer les actifs de l'application à travers un Provider à _n'importe quel_ composant enfant écoutant en tant que Consumer. Cela élimine le paradigme du "prop drilling". Imaginez : à _n'importe quel_ niveau, un composant parent pourrait définir son propre état (y compris des méthodes) et les fournir directement à tout consommateur participant. De plus, vous pouvez définir l'état en utilisant les méthodes passées par le Provider du Context.

![Image](https://cdn-media-1.freecodecamp.org/images/Sv7YltnxU2uwL3G0F6L7uao9zxxqgxH5BQq5)
_Fig. 2 — L'API Context de React peut réduire ou éliminer le besoin de "Prop Drilling" source de l'image : [The JavaScript Playground](https://javascriptplayground.com/context-in-reactjs-applications/" rel="noopener" target="_blank" title=")_

Nous allons vous montrer comment faire cela dans l'exemple ci-dessous.

**C'est parti !**

[**bgirten/clever-React-Context-tricks**](https://github.com/bgirten/clever-React-Context-tricks.git)
[_nouveaux experiments avec React Context. Contribuez au développement de bgirten/clever-React-Context-tricks en créant un compte sur... github.com_](https://github.com/bgirten/clever-React-Context-tricks.git)

![Image](https://cdn-media-1.freecodecamp.org/images/ncb0PHxVEZansTJLq54nCpdC0IjgFpKxMQlA)

Nous commençons par créer un objet State "initial" qui sera passé du composant App aux composants enfants. Remarquez que cet initialState inclut également des méthodes. Cette approche offre la capacité de définir des méthodes une seule fois, afin de pouvoir les réutiliser plus facilement.

![Image](https://cdn-media-1.freecodecamp.org/images/TpDU-j9zv5qwz9b14pNoVSaDSf0gVPUdRSNr)

Passez l'état initial dans le composant App et fournissez un Context. Chaque composant inclus dans la balise MyContext.Provider aura la capacité de consommer le contexte (qui dans ce cas inclut l'état initial du composant App).

![Image](https://cdn-media-1.freecodecamp.org/images/Bt0AuoHrGBFLvqfXRUMmhS0rYp4vrUEG2J25)

Contournez le "prop drilling" du composant enfant au composant petit-enfant.

![Image](https://cdn-media-1.freecodecamp.org/images/fVdLJZKi556Ibbytjb9hww-ZTIDKRpLLE9Zd)

La méthode locale handleFetchEvent fournit la capacité d'exécuter la méthode passée par le contexte (dans ce cas, updateStats). La méthode de rendu du composant se déclenche grâce à this.setState.

À la ligne 21, nous consommons le Context.Provider entrant, ce qui nous permet d'accéder à tous ces membres et méthodes définis dans l'état initial du composant App.

Même si des méthodes peuvent être passées depuis des niveaux supérieurs de l'arbre DOM, nous pouvons également invoquer le re-rendu du DOM en appelant simplement la méthode **setState** directement pour un composant React donné.

![Image](https://cdn-media-1.freecodecamp.org/images/RJiTN1aHJ6qSrFUdqesUU7kKE1mvcD21WZO0)

Et voici l'application chargée. Merci d'avoir suivi — vous pouvez trouver plus de contenu génial de ces auteurs sur :

[Github d'Alison](https://www.github.com/sedulous-mortal), [Github de Martin](https://www.github.com/87maza), et [Github de Bill](https://www.github.com/bgirten)