---
title: Comment basculer un élément dans React en utilisant les Hooks React
subtitle: ''
author: deji adesoga
co_authors: []
series: null
date: '2022-11-07T18:26:54.000Z'
originalURL: https://freecodecamp.org/news/toggle-elements-in-react-using-hooks
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/Copy-of-Coffee-Tutorial-YouTube-Thumbnail--1-.png
tags:
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
- name: Web Development
  slug: web-development
seo_title: Comment basculer un élément dans React en utilisant les Hooks React
seo_desc: 'When building a web application, toggling an element is one of the key
  features you are likely to come across and may need to implement in your project.

  There are various ways you can toggle an element. In this article, we will take
  a look at how we ...'
---

Lors de la création d'une application web, le basculement d'un élément est l'une des fonctionnalités clés que vous êtes susceptible de rencontrer et que vous devrez peut-être implémenter dans votre projet.

Il existe diverses façons de basculer un élément. Dans cet article, nous allons examiner comment nous pouvons implémenter des fonctionnalités de basculement de cinq (5) manières différentes dans React.

## Table des matières

* [Comment installer et configurer le projet React](#heading-comment-installer-et-configurer-le-projet-react)
    
* [Comment basculer un élément en utilisant les opérateurs logiques](#heading-comment-basculer-un-element-en-utilisant-les-operateurs-logiques)
    
* [Comment basculer un élément en utilisant le Hook useToggle](#heading-comment-basculer-un-element-en-utilisant-le-hook-usetoggle)
    
* [Comment basculer un élément en utilisant l'opérateur ternaire](#heading-comment-basculer-un-element-en-utilisant-loperateur-ternaire)
    
* [Comment basculer un élément en utilisant l'instruction If/Else](#heading-comment-basculer-un-element-en-utilisant-linstruction-ifelse)
    
* [Comment basculer un élément en utilisant le style conditionnel CSS](#heading-comment-basculer-un-element-en-utilisant-le-style-conditionnel-css)
    
* [Conclusion](#heading-conclusion)
    

Vous pouvez également regarder la version vidéo de cet article ci-dessous, ou sur ma [chaîne YouTube](https://www.youtube.com/watch?v=S_mgSHCWCmA&t=15s) :

%[https://www.youtube.com/watch?v=5CTFTDpHHto] 

## Comment installer et configurer le projet React

Pour créer un projet React, vous devez avoir accès à NPM (Node Package Manager). L'accès à NPM nécessite que vous ayez Node.js installé. Vous pouvez installer Node en vous rendant sur le site [officiel de Node.js](https://nodejs.org/en/) et en téléchargeant Node.js.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/npm-3.png align="left")

*Documentation officielle de Node.js*

Je vous conseille de sélectionner la version "Recommandée pour la plupart des utilisateurs". Une fois l'installation terminée, vous pouvez ouvrir votre terminal et exécuter les commandes `node -v` et `npm -v`. Cela vous donne des détails sur la version de Node et npm que vous avez.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/terminal-2-1.png align="left")

*Terminal affichant les versions de node et npm*

Toujours dans votre terminal, vous pouvez maintenant installer [Create React App](https://create-react-app.dev/) qui est une plateforme qui vous permet de créer un projet React en utilisant la commande suivante :

`npm i create-react-app`

L'étape suivante consiste à créer un nouveau projet React à partir du terminal en exécutant la commande :

```php
npm init react-app toggle
cd toggle 
code .
```

Ci-dessus, nous avons créé un nouveau projet appelé `toggle`. Ensuite, nous avons navigué dans le répertoire du projet nouvellement créé et ouvert le projet dans notre éditeur de code. Nous pouvons maintenant commencer le processus d'implémentation des différentes méthodes de basculement d'un élément.

## Comment basculer un élément en utilisant les opérateurs logiques

Pour nous assurer que la conception de notre page est structurée, nous allons configurer Bootstrap 5 à l'intérieur du projet React.

Pour ce faire, rendez-vous sur le site [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/) et copiez le lien CDN CSS. Ensuite, allez dans votre fichier `index.html` dans votre projet React qui se trouve dans le répertoire `public`. Collez le lien CDN dans la section head, comme vous pouvez le voir dans le code ci-dessous :

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8" />
  <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="theme-color" content="#000000" />
  <meta name="description" content="Web site created using create-react-app" />
  <link rel="apple-touch-icon" href="%PUBLIC_URL%/logo192.png" />
  <link rel="manifest" href="%PUBLIC_URL%/manifest.json" />
  <!-- Lien CDN Bootstrap 5 -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
  <title>React App</title>
</head>

<body>
  <noscript>You need to enable JavaScript to run this app.</noscript>
  <div id="root"></div>
</body>

</html>
```

Ensuite, créez un nouveau dossier appelé `components` à l'intérieur du répertoire `src`. Puis créez un nouveau fichier appelé `LogicalNot.js` à l'intérieur du dossier `components`. Pour implémenter la méthode de l'opérateur **logical not**, nous allons implémenter le code ci-dessous :

```jsx
import React, { useState } from 'react'

const LogicalNot = () => {

  //Utilisation de la fonction en ligne et de l'opérateur Logical Not (!) pour basculer l'état
  const [toggle, setToggle] = useState(true)

  return (
    <>
      <button 
            onClick={() => setToggle(!toggle)} 
            class="btn btn-primary mb-5">
          Basculer l'état
      </button>
      {toggle && (
        <ul class="list-group">
          <li class="list-group-item">Un élément</li>
          <li class="list-group-item">Un deuxième élément</li>
          <li class="list-group-item">Un troisième élément</li>
          <li class="list-group-item">Un quatrième élément</li>
          <li class="list-group-item">Et un cinquième</li>
        </ul>
      )}
    </>
  )
}
export default LogicalNot
```

À l'intérieur du fichier `LogicalNot.js`, nous commençons par :

* Importer le hook `useState`.
    
* Ensuite, nous créons deux variables appelées `toggle` et `setToggle`, tout en définissant l'état initial à **true**.
    
* Ensuite, à l'intérieur de la section *jsx*, nous créons un bouton qui a un gestionnaire d'événements `onClick`. Dans ce gestionnaire `onClick`, nous créons une fonction anonyme en utilisant le setter que nous avons déclaré précédemment appelé `setToggle`. Nous définissons ensuite l'argument dans la fonction anonyme à `!toggle` ce qui crée un effet false lorsqu'il est cliqué.
    
* Enfin, nous basculons l'élément dans la balise `ul` en l'enveloppant autour de la variable `toggle` puis en le rendant conditionnellement sur la page en utilisant l'opérateur logique `&&`.
    

Pour afficher le fichier `LogicalNot.js` sur le navigateur, rendez-vous dans le fichier `App.js` et importez le fichier là-bas comme vu ci-dessous :

```javascript
import './App.css';
import LogicalNot from './components/LogicalNot';

function App() {
  return (
    <div className="App mt-5">
      <LogicalNot />
    </div>
  );
}

export default App;
```

Avec cela, vous devriez avoir le résultat ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/logicanot_2.gif align="left")

*Exemple d'opérateur logical not*

## Comment basculer un élément en utilisant le Hook useToggle

Vous allez commencer cette étape en créant un nouveau fichier appelé `ToggleHook.js` à l'intérieur du dossier *components*. À l'intérieur de ce fichier, importez le hook `useState`.

```jsx
import React, { useState } from 'react'
```

Ensuite, créez une variable appelée `useToggle` qui contiendra la logique pour le hook `useToggle` comme vous pouvez le voir ci-dessous :

```javascript
  //Utilisation du Hook useToggle

  const useToggle = (initialState) => {
    const [toggleValue, setToggleValue] = useState(initialState);

    const toggler = () => { setToggleValue(!toggleValue) };
    return [toggleValue, toggler]
  };
```

* Ci-dessus, nous avons créé une fonction de rappel et lui avons donné un paramètre appelé `initialState`.
    
* Ensuite, nous avons utilisé le hook `useState` pour créer un getter et un setter appelés `toggleValue` et `setToggleValue`, respectivement. Le hook `useState` prend le paramètre `initialState` que nous avons créé précédemment qui définit la valeur initiale comme false par défaut.
    
* Enfin, nous avons créé une variable appelée `toggler`. Cette variable contient une fonction anonyme qui contient nos variables `useState` et définit ensuite les résultats à la valeur opposée lorsqu'elle est cliquée. Nous avons ensuite retourné les variables `toggleValue` et `toggler` dans un tableau.
    

Avec cela, nous pouvons maintenant utiliser le hook `useToggle` pour créer une variable getter et setter comme vous pouvez le voir ci-dessous :

```jsx
  const [toggle, setToggle] = useToggle();
```

Nous pouvons maintenant implémenter la logique du hook `useToggle` dans la partie `jsx` de notre code :

```html
    return (
    <div>
      <button 
            onClick={setToggle} 
            class="btn btn-secondary mb-5">
          Basculer l'état
      </button>

      {toggle && (
        <ul class="list-group">
          <li class="list-group-item">Un élément</li>
          <li class="list-group-item">Un deuxième élément</li>
          <li class="list-group-item">Un troisième élément</li>
          <li class="list-group-item">Un quatrième élément</li>
          <li class="list-group-item">Et un cinquième</li>
        </ul>
      )}

    </div>
  )
```

* Ci-dessus, nous avons créé un bouton qui contient un gestionnaire d'événements `onClick` en utilisant le setter `setToggle` déclaré précédemment.
    
* Ensuite, nous avons rendu les éléments en fonction de la condition booléenne de la variable `toggle` lorsqu'elle est cliquée.
    

Avec cela, nous devrions avoir le résultat ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/useToggle.gif align="left")

*Exemple de useToggle*

## Comment basculer un élément en utilisant l'opérateur ternaire

L'opérateur ternaire est un opérateur JavaScript qui prend trois opérations différentes, qui sont :

* Une condition
    
* Un point d'interrogation (?) pour exécuter une condition si elle est vraie
    
* Un deux-points (:) pour exécuter une condition si elle est fausse
    

Pour implémenter cette méthode, vous allez commencer par importer le hook `useState` :

```javascript
import React, { useState } from 'react'
```

Ensuite, vous devez créer deux variables en utilisant le hook `useState` et définir la valeur par défaut à true :

```javascript
  const [toggle, setToggle] = useState(true);
```

Ensuite, créez une variable appelée `handleClick` qui contient une fonction de rappel. Dans cette fonction, appelez le setter `setToggle` puis passez `!toggle` pour retourner une valeur opposée lorsqu'elle est cliquée, comme vous pouvez le voir ci-dessous :

```javascript
  const handleClick = () => {
    setToggle(!toggle);
  };
```

Enfin, vous pouvez maintenant rendre la logique des variables que vous avez créées dans votre `jsx` :

```javascript
  return (
    <div>
      <button 
      onClick={handleClick} 
      class="btn btn-info mb-5">
      Basculer l'état
      </button>

      {toggle ?
        <ul class="list-group">
          <li class="list-group-item">Un élément</li>
          <li class="list-group-item">Un deuxième élément</li>
          <li class="list-group-item">Un troisième élément</li>
          <li class="list-group-item">Un quatrième élément</li>
          <li class="list-group-item">Et un cinquième</li>
        </ul>
        :
        <></>
      }
    </div>
  )
```

* Ci-dessus, nous avons créé un bouton qui utilise un gestionnaire d'événements `onClick` pour référencer la variable `handleClick` que nous avons créée précédemment.
    
* Ensuite, nous pouvons rendre les éléments en utilisant la condition de la variable `toggle`, ainsi que le point d'interrogation (?) qui affiche les éléments si la variable `toggle` est définie à true, ou affiche un fragment *jsx* vide en utilisant le deux-points (:) si la variable toggle est définie à false.
    

Avec cela, nous devrions avoir le résultat ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/ternary.gif align="left")

*Exemple d'opérateur ternaire*

## Comment basculer un élément en utilisant l'instruction If/Else

L'instruction `If/Else` est une instruction conditionnelle utilisée pour effectuer différentes actions en fonction de certains paramètres. L'instruction `if` exécute une certaine condition si elle est vraie, et l'instruction `else` s'exécute lorsque la condition est fausse.

Pour voir l'instruction if/else en action, commençons par importer le hook `useState` :

```javascript
import React, { useState } from 'react'
```

Ensuite, créez les variables getter et setter puis définissez la valeur par défaut à true :

```javascript
 const [toggle, setToggle] = useState(true);
```

Ensuite, créez une variable appelée `handleClick` qui contient la fonction de rappel. Dans cette fonction, appelez le setter `setToggle` puis passez `!toggle` pour retourner une valeur opposée lorsqu'elle est cliquée, comme vous pouvez le voir ci-dessous :

```javascript
  const handleClick = () => {
    setToggle(!toggle)
  };
```

Vous pouvez maintenant afficher les éléments en utilisant le getter `toggle` dans le `jsx` comme vous pouvez le voir ci-dessous :

```javascript
if (toggle) {
    return (
      <div>
        <button onClick={handleClick} class="btn btn-dark mb-5">Basculer l'état</button>
        <ul class="list-group">
          <li class="list-group-item">Un élément</li>
          <li class="list-group-item">Un deuxième élément</li>
          <li class="list-group-item">Un troisième élément</li>
          <li class="list-group-item">Un quatrième élément</li>
          <li class="list-group-item">Et un cinquième</li>
        </ul>
      </div>
    )
  } else {
    return <button onClick={handleClick} class="btn btn-dark mb-5">Basculer l'état</button>
  }
```

* Dans le `jsx`, nous avons enveloppé tout l'élément autour de l'instruction `if/else`.
    
* Dans l'instruction `if`, nous avons rendu les éléments qui contiennent les éléments de la liste sur la page lorsque le `toggle` est défini à true.
    
* Dans le bloc else, cependant, lorsque le toggle est défini à false, seul l'élément bouton est retourné.
    

Avec cela, nous obtenons le résultat ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/if-else.gif align="left")

*Exemple d'instruction if/else*

## Comment basculer un élément en utilisant le style conditionnel CSS

Le style conditionnel est l'une des façons dont vous pouvez manipuler les éléments DOM dans React en fonction d'une condition spécifique. Comme nous l'avons fait précédemment, commençons par importer le hook `useState` dans React :

```javascript
import React, { useState } from 'react'
```

Ensuite, configurez votre hook `useState` en créant les variables requises :

```javascript
  const [toggle, setToggle] = useState(true);
```

Ensuite, créez la fonction qui aide à définir la valeur de votre état opposé lorsqu'elle est cliquée :

```javascript
  const handleClick = () => {
    setToggle(!toggle);
  };
```

Avec cela, vous pouvez maintenant configurer le style conditionnel dans la section `jsx` de votre code :

```javascript
 return (
    <div>
      <button onClick={handleClick} class="btn btn-warning mb-5">Basculer l'état</button>

      <ul class="list-group" style={{ display: toggle ? 'block' : 'none' }}>
        <li class="list-group-item">Un élément</li>
        <li class="list-group-item">Un deuxième élément</li>
        <li class="list-group-item">Un troisième élément</li>
        <li class="list-group-item">Un quatrième élément</li>
        <li class="list-group-item">Et un cinquième</li>
      </ul>

    </div>
  )
```

* Ci-dessus, nous avons commencé par créer le bouton qui contient le gestionnaire d'événements `onClick` appelé `handleClick` comme créé précédemment.
    
* Ensuite, nous avons utilisé l'attribut style dans la balise `ul` pour définir conditionnellement l'affichage à block lorsque la variable `toggle` est true. Si la variable `toggle` est false, nous définissons l'affichage à none. Cela est possible grâce à l'opérateur ternaire.
    

Le résultat ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/condition.gif align="left")

*Exemple de style conditionnel*

## Conclusion

Dans ce tutoriel, vous avez appris les différentes façons de basculer des éléments dans une application React. Si vous souhaitez accéder à la base de code, vous pouvez cloner le dépôt [ici](https://github.com/desoga10/showandhide) sur GitHub.

De plus, si vous avez apprécié cet article, vous pouvez montrer votre soutien en vous abonnant à ma [chaîne YouTube](https://www.youtube.com/TheCodeAngle) où je crée des tutoriels géniaux sur les technologies de développement web comme Angular, React, JavaScript, Html, CSS, et bien d'autres concepts.