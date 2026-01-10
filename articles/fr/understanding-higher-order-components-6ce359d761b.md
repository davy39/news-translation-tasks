---
title: Comprendre les composants d'ordre supérieur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-06-01T04:45:45.000Z'
originalURL: https://freecodecamp.org/news/understanding-higher-order-components-6ce359d761b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*w4MV4Ufnk2WWY4LgX9ZhPA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comprendre les composants d'ordre supérieur
seo_desc: 'By Tom Coleman

  Making sense of the rapidly changing React best practice.


  If you’re new to React, you may have heard about “Higher Order Components” and “Container”
  components. If so, you may be wondering what all the fuss is about. Or you may have
  e...'
---

Par Tom Coleman

#### _Comprendre la meilleure pratique React en rapide évolution._

![Image](https://cdn-media-1.freecodecamp.org/images/1*w4MV4Ufnk2WWY4LgX9ZhPA.jpeg)

Si vous êtes nouveau dans React, vous avez peut-être entendu parler des "composants d'ordre supérieur" et des composants "conteneurs". Si c'est le cas, vous vous demandez peut-être de quoi il s'agit. Ou vous avez peut-être même utilisé une API pour une bibliothèque qui en fournit un, et vous avez été un peu confus quant à la terminologie.

En tant que mainteneur de [l'intégration React d'Apollo](http://dev.apollodata.com/react/) — une bibliothèque open source populaire qui utilise largement les composants d'ordre supérieur — et auteur de beaucoup de sa documentation, j'ai passé un peu de temps à comprendre le concept moi-même.

J'espère que cet article pourra vous aider à éclaircir le sujet.

### **Un rappel sur React**

Cet article suppose que vous êtes familier avec React — si ce n'est pas le cas, il existe beaucoup de contenu de qualité. Par exemple, l'article de Sacha Greif sur [les 5 concepts React](https://medium.freecodecamp.com/the-5-things-you-need-to-know-to-understand-react-a1dbd5d114a3) est un bon point de départ. Néanmoins, passons en revue quelques points pour être sûr que nous sommes sur la même longueur d'onde.

Une application React se compose d'un ensemble de **composants**. Un composant reçoit un ensemble de propriétés d'entrée (**props**) et produit du HTML qui est rendu à l'écran. Lorsque les props du composant changent, il se re-rend et le HTML peut changer.

Lorsque l'utilisateur de l'application interagit avec ce HTML, via un type d'événement (comme un clic de souris), le composant le gère soit en déclenchant une prop de **rappel**, soit en changeant un **état** interne. Changer l'état interne provoque également son re-rendu ainsi que celui de ses enfants.

Cela conduit à un **cycle de vie** du composant, car un composant est rendu pour la première fois, attaché au DOM, reçoit de nouvelles props, etc.

La fonction de rendu d'un composant retourne une ou plusieurs instances d'autres composants. L'**arbre de vue** résultant est un bon modèle mental à garder à l'esprit pour comprendre comment les composants de l'application interagissent. En général, ils interagissent uniquement en passant des props à leurs enfants ou en déclenchant des rappels passés par leurs parents.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NS6TPKPJuCgsK2M45tPIGw.gif)
_Flux de données dans un arbre de vue React_

### **UI React vs état**

Cela semble presque dépassé maintenant, mais il fut un temps où tout était décrit en termes de distinction entre Modèles, Vues et Contrôleurs (ou Modèles de Vue, ou Présentateurs, etc.). Dans cette classification, la tâche d'une Vue est de **rendre** et de gérer l'interaction utilisateur, et celle d'un Contrôleur est de **préparer les données**.

Une tendance récente dans React est l'utilisation de **composants fonctionnels sans état**. Ces composants "purs" les plus simples ne transforment leurs props en HTML et n'appellent des props de rappel sur l'interaction utilisateur :

Ils sont fonctionnels car vous pouvez vraiment les considérer comme des fonctions. Si tout votre arbre de vue était composé d'eux, vous parlez vraiment d'une grande fonction pour produire du HTML composé d'appels à de nombreuses fonctions plus petites.

Une propriété intéressante des composants fonctionnels sans état est qu'ils sont super faciles à tester et simples à comprendre. Cela signifie qu'ils sont plus faciles à développer et plus rapides à déboguer.

Mais vous ne pouvez pas toujours vous en sortir ainsi. L'UI a besoin d'état. Par exemple, votre menu peut avoir besoin de s'ouvrir lorsque l'utilisateur passe la souris dessus (beurk, j'espère que non !) — et la façon de le faire dans React est certainement en utilisant l'état. Pour utiliser l'état, vous utilisez des composants basés sur des classes.

Là où les choses se compliquent, c'est lorsque vous connectez l'état "global" de votre UI à l'arbre de vue.

### État global

L'état global dans votre UI est l'état qui n'est pas directement et uniquement pertinent pour un seul composant. Il se compose généralement de deux types principaux de choses :

1. Les **données** de votre application qui proviennent d'un serveur. Typiquement, les données sont utilisées à plusieurs endroits et ne sont donc pas uniques à un seul composant.

2. **L'état global de l'UI**, (comme l'URL, et donc la page que l'utilisateur regarde).

Une approche de l'état global consiste à l'attacher au composant "racine" le plus élevé de votre application et à le transmettre dans l'arbre à tous les composants qui en ont besoin. Vous transmettez ensuite toutes les modifications de cet état vers le haut de l'arbre via une chaîne de rappels.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-RDYOXCu7BBOTnkFsE3yFg.gif)
_Flux de données depuis le store vers un arbre de vue, avec un seul conteneur_

Cette approche devient rapidement ingérable. Cela signifie que le composant racine doit comprendre les exigences de tout son arbre, et de même pour chaque parent de chaque sous-arbre de tout l'arbre. C'est là que le concept suivant intervient.

### **Conteneurs et composants de présentation**

Ce problème est généralement résolu en permettant aux composants d'accéder à l'état global n'importe où dans l'arbre de vue (une certaine retenue est généralement nécessaire).

Dans ce monde, les composants peuvent être classés en ceux qui accèdent à l'état global et ceux qui ne le font pas.

Les composants "purs" qui ne le font pas sont les plus faciles à tester et à comprendre (surtout s'ils sont des composants fonctionnels sans état). Dès qu'un composant est "impur", il est entaché et plus difficile à gérer.

Pour cette raison, [un modèle](https://medium.com/@dan_abramov/smart-and-dumb-components-7ca2f9a7c7d0) a émergé pour séparer chaque composant "impur" en **deux** composants :

* Le composant **conteneur** qui fait le travail "sale" de l'état global
* Le composant **de présentation** qui ne le fait pas.

Nous pouvons maintenant traiter le composant de présentation comme nous avons traité nos composants simples ci-dessus, et isoler le travail complexe et sale de gestion des données dans le conteneur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*tIdBW-TqotpALD3b2xk3SA.gif)
_Flux de données avec plusieurs conteneurs_

### Le conteneur

Une fois que vous avez adopté la séparation des composants de présentation/conteneur, l'écriture de composants conteneurs devient intéressante.

Une chose que vous remarquez est qu'ils ne ressemblent souvent pas beaucoup à un composant. Ils peuvent :

* Récupérer et passer une partie de l'état global (par exemple depuis Redux) à leur enfant.
* Exécuter une requête d'accès aux données (par exemple GraphQL) et passer les résultats à leur enfant.

De plus, si nous suivons une bonne séparation des préoccupations, nos conteneurs **ne rendront jamais qu'un seul composant enfant**. Le conteneur est nécessairement lié à l'enfant, car l'enfant est câblé en dur dans la fonction de rendu. Ou est-ce le cas ?

### Généralisation des conteneurs

Pour tout "type" de composant conteneur (par exemple, un qui accède au store de Redux), l'implémentation est la même, ne différant que dans les détails : quel composant enfant ils rendent, et quelles données exactes ils récupèrent.

Par exemple, dans le monde de Redux (si nous n'avions pas le HOC `connect` de `react-redux`), un conteneur pourrait ressembler à :

Même si ce conteneur ne fait pas la plupart de ce qu'un vrai conteneur Redux ferait, vous pouvez déjà voir que, mis à part l'implémentation de `mapStateToProps` et le `MyComponent` spécifique que nous enveloppons, il y a beaucoup de code standard que nous devrions écrire **chaque fois que nous écrivons un conteneur accédant à Redux**.

### Génération de conteneurs

En fait, il pourrait être plus simple d'écrire une fonction qui **génère** le composant conteneur en fonction des informations pertinentes (dans ce cas, le composant enfant et la fonction `mapStateToProps`).

C'est un **composant d'ordre supérieur** (HOC), qui est une **fonction** qui prend un composant enfant et quelques options, puis construit un conteneur pour cet enfant.

Il est "d'ordre supérieur" de la même manière qu'une "fonction d'ordre supérieur" — une fonction qui construit une fonction. En fait, vous pouvez penser aux composants React comme à des fonctions qui produisent une UI. Cela fonctionne particulièrement bien pour les composants fonctionnels sans état, mais si vous plissez les yeux, cela fonctionne également pour les composants de présentation avec état pur. Un HOC est exactement une fonction d'ordre supérieur.

### **Exemples de HOC**

Il y en a beaucoup, mais voici quelques-uns notables :

* Le plus courant est probablement la fonction `connect` de [Redux](http://redux.js.org), dont notre fonction `buildReduxContainer` ci-dessus n'est qu'une version médiocre.
* La fonction `withRouter` de [React Router](https://github.com/ReactTraining/react-router) qui récupère simplement le routeur du contexte et en fait une prop pour l'enfant.
* L'interface principale de `[react-apollo](http://dev.apollodata.com/react/)` est le HOC `graphql`, qui, étant donné un composant et une requête GraphQL, fournit les résultats de cette requête à l'enfant.
* [Recompose](https://github.com/acdlite/recompose) est une bibliothèque remplie de HOC qui effectuent une variété de petites tâches que vous pourriez vouloir abstraire de vos composants.

### **HOC personnalisés**

Devez-vous écrire de nouveaux HOC dans votre application ? Bien sûr, si vous avez des modèles de composants qui pourraient être généralisés.

> Au-delà du simple partage de bibliothèques d'utilitaires et de la composition simple, les HOC sont le meilleur moyen de partager un comportement entre les composants React.

Écrire un HOC est aussi simple qu'une fonction qui retourne une classe, comme nous l'avons vu avec notre fonction `buildReduxContainer` ci-dessus. Si vous voulez en savoir plus sur ce que vous pouvez faire lorsque vous construisez des HOC, je vous suggère de lire l'article [extêmement complet](https://medium.com/@franleplant/react-higher-order-components-in-depth-cf9032ee6c3e#.pvnx42kku) de Fran Guijarro sur le sujet.

### Conclusion

Les composants d'ordre supérieur sont au cœur une codification d'une séparation des préoccupations dans les composants de manière **fonctionnelle**. Les premières versions de React utilisaient des classes et des mixins pour atteindre la réutilisation de code, mais tous les signes indiquent que cette approche plus fonctionnelle guide la conception future de React.

Si vos yeux ont tendance à se voiler lorsque vous entendez parler de techniques de programmation fonctionnelle, ne vous inquiétez pas ! L'équipe React a fait un excellent travail en prenant les meilleures parties simplificatrices de ces approches pour nous guider tous vers l'écriture d'UI plus modulaires et composées.

Si vous voulez en savoir plus sur la construction d'applications de manière moderne et orientée composants, consultez ma [série d'articles](https://blog.hichroma.com/ui-components/home) sur [Chroma](http://hichroma.com), et si vous aimez cet article, envisagez de le ? et de le partager !