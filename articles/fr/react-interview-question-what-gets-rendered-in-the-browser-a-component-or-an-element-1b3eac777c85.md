---
title: 'Question d''entretien React : Qu''est-ce qui est rendu dans le navigateur,
  un composant ou un élément ?'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-13T22:44:15.000Z'
originalURL: https://freecodecamp.org/news/react-interview-question-what-gets-rendered-in-the-browser-a-component-or-an-element-1b3eac777c85
coverImage: https://cdn-media-1.freecodecamp.org/images/1*mXjNHOx9bbQ5D4sSUAX2Lg.png
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
seo_title: 'Question d''entretien React : Qu''est-ce qui est rendu dans le navigateur,
  un composant ou un élément ?'
seo_desc: "By Samer Buna\n Trick Question \nYou might not like the answer because,\
  \ unfortunately, it is a bit complicated.\n\nIsn’t the word element synonymous to\
  \ the word component anyway??\n\n\nForm reactjs.org\n\nUpdate: This article is now\
  \ part of my book “React.js ..."
---

Par Samer Buna

#### ** Question piège **

Vous n'aimerez peut-être pas la réponse car, malheureusement, elle est un peu compliquée.

> Le mot **élément** n'est-il pas synonyme du mot **composant** de toute façon ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*mXjNHOx9bbQ5D4sSUAX2Lg.png)
_De reactjs.org_

> **Mise à jour :** Cet article fait maintenant partie de mon livre « React.js Beyond The Basics ».

> Lisez la version mise à jour de ce contenu et plus sur React à [**_jscomplete.com/react-beyond-basics_**](https://jscomplete.com/g/component-or-element)_._

Techniquement parlant, ReactDOM ne rend pas un composant React ou un élément React dans le DOM. Il rend des **éléments DOM soutenus par des instances de leurs composants**. Cela est vrai pour les composants de classe. Pour les composants de fonction, ReactDOM rend simplement des éléments DOM. Les composants de fonction n'ont pas d'instances (qui peuvent être accessibles avec `this`) donc, lors de l'utilisation d'un composant de fonction, ReactDOM rend un élément DOM généré à partir de l'élément retourné par la fonction.

Ce que vous devez comprendre ici, c'est qu'un élément React est différent d'un élément DOM. Un élément React est simplement une **description** d'un élément HTML, d'un composant React, ou d'un mélange de ces éléments.

D'accord, une meilleure question d'entretien pourrait être : **Lorsque vous utilisez quelque chose comme `<MyComponent` /> en JSX, est-ce un composant, un élément ou une instance ?

C'est un **élément** mais pas un élément DOM. C'est un élément React. L'indice ici est que toute balise JSX est traduite en un appel à `React.createElement`. Gardez cela à l'esprit. CREATE. **ELEMENT**.

Cependant, pour que React continue de travailler avec cet élément React, il devra soit invoquer une fonction, soit créer une instance à partir d'une classe.

Vous pourriez trouver les mots **composant**, **élément** et **instance** mélangés dans les guides et tutoriels React. Je suis moi-même coupable de mélanger ces mots, mais je pense qu'un débutant en React doit comprendre les distinctions importantes. Le blog React a un [article sur ce sujet](https://reactjs.org/blog/2015/12/18/react-components-elements-and-instances.html), mais je pense qu'il est un peu trop technique pour un débutant.

Voici comment je fournirais des définitions simples de ces mots aux débutants :

* Un **composant** React est un modèle. Un plan. Une définition globale. Cela peut être soit une **fonction**, soit une **classe** (avec une fonction de rendu).
* Un **élément** React est ce qui est **retourné** par les composants. C'est un objet qui décrit virtuellement les nœuds DOM qu'un composant représente. Avec un composant de fonction, cet élément est l'objet que la fonction retourne. Avec un composant de classe, l'élément est l'objet que la fonction de rendu du composant retourne. Les éléments React ne sont pas ce que nous voyons dans le navigateur. Ce sont simplement des objets en mémoire et nous ne pouvons rien changer à leur sujet.
* React crée, met à jour et détruit **instances** en interne pour déterminer l'arborescence des éléments DOM qui doit être rendue dans le navigateur. Lors de l'utilisation de composants de classe, il est courant de se référer à leurs éléments DOM rendus dans le navigateur comme des instances de composants. Vous pouvez rendre plusieurs instances du même composant. L'instance est le mot-clé `this` que vous utilisez à l'intérieur des composants basés sur des classes. Vous n'auriez pas besoin de créer une instance à partir d'une classe manuellement. Vous devez simplement vous rappeler qu'elle est quelque part dans la mémoire de React.
* Les éléments React basés sur des fonctions n'ont pas d'instances. Un composant de fonction peut toujours être rendu plusieurs fois, mais React n'associe simplement pas d'instance locale à chaque rendu. Il utilise simplement l'invocation de la fonction pour déterminer quel élément DOM rendre pour la fonction.

En résumé, ReactDOM ne rend pas les composants dans le navigateur, et il ne rend pas non plus les éléments (au sens de garder le terme élément pour représenter le résultat de `React.createElement`). Il ne rend pas non plus les instances. **Il rend des éléments DOM.**

Malheureusement, il semble que ce soit une pratique courante d'utiliser le terme composant pour désigner à la fois le modèle et les instances ou invocations utilisées via le modèle. Je ne blâme personne d'être confus ici. C'est un peu douloureux.

#### Quelle est l'histoire ici ?

Chaque application React commence par un appel `render` qui utilise un **élément React**. Utilisons l'exemple `HelloMessage` de [reactjs.org](https://reactjs.org/) légèrement modifié pour avoir également un composant de fonction :

```
const Today = () => (  <div>Aujourd'hui, nous sommes le {new Date().toDateString()}</div>);
```

```
class HelloMessage extends React.Component {  render() {    return (      <React.Fragment>        <div>Bonjour {this.props.name}</div>        <Today />      </React.Fragment>    );  }}
```

```
ReactDOM.render(  <HelloMessage name="Taylor" />,  mountNode);
```

Le premier élément React est celui avec lequel nous commençons dans l'appel `ReactDOM.render` :

```
<HelloMessage name="Taylor" /> // Ceci est un élément React
```

Cet élément React décrit que l'arborescence DOM à rendre doit commencer par le composant `HelloMessage` et une valeur de prop `name` égale à `Taylor`.

**React doit maintenant répondre à la question : Qu'est-ce que `HelloMessage` ?**

Chaque fois qu'un élément React décrit un composant React (comme l'élément React que nous avons ci-dessus), React utilise le composant pour remplacer cette description par ce que le composant retourne. Il crée une instance pour les composants basés sur des classes à ce stade et conserve une référence de celle-ci en mémoire. Il ne crée rien pour les composants basés sur des fonctions ; il les invoque simplement.

Ce qui est retourné par le composant `HelloMessage` est un élément React qui décrit un composant `React.Fragment`.

**React doit maintenant répondre à la question : Qu'est-ce que `React.Fragment` ?**

React continuera à réduire ces descriptions inconnues de composants jusqu'à ce qu'il n'ait plus que des nœuds DOM valides. La description de `React.Fragment` est traduite en 2 éléments React, l'un décrivant un `div` et l'autre décrivant un composant `Today`.

**React doit maintenant répondre à la question : Qu'est-ce que `Today` ?**

Il appelle la fonction `Today` pour résoudre cette dernière question. La fonction `Today` retourne un élément React qui décrit un `div`.

À ce stade, l'arborescence virtuelle est complète avec tous les éléments React qui décrivent les nœuds DOM. React utilise son algorithme de réconciliation pour déterminer ce qu'il faut mettre à jour dans le navigateur. Les nœuds qui ont été traduits avec une instance de composant conservent le pouvoir de modifier cette instance.

**Cela a-t-il clarifié un peu les choses ou ai-je encore plus confondu les termes ? Faites-le moi savoir dans les réponses ci-dessous.**

Merci pour votre lecture.

Apprendre React ou Node ? Consultez mes livres :

* [Learn React.js by Building Games](http://amzn.to/2peYJZj)
* [Node.js Beyond the Basics](http://amzn.to/2FYfYru)