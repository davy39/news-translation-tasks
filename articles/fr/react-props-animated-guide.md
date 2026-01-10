---
title: Apprendre les Props React – Le Guide Animé
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2023-12-17T21:38:23.000Z'
originalURL: https://freecodecamp.org/news/react-props-animated-guide
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/react-props-animated.png
tags:
- name: React
  slug: react
seo_title: Apprendre les Props React – Le Guide Animé
seo_desc: 'Props are a common stumbling block when moving from JavaScript to React.

  In reality, using props in React components is almost identical to using arguments
  in plain JavaScript functions.

  Let''s take a quick look at what props are in React through some...'
---

Les props sont un obstacle courant lors du passage de JavaScript à React.

En réalité, l'utilisation des props dans les composants React est presque identique à l'utilisation des arguments dans les fonctions JavaScript simples.

Jetons un rapide coup d'œil à ce que sont les props dans React à travers quelques animations utiles. Cela vous aidera à visualiser comment les props fonctionnent et comment vous pouvez les utiliser dans vos projets React.

## Comment passer des données à une fonction JavaScript

La fonction JavaScript suivante est cassée. Que se passera-t-il si vous essayez de l'utiliser ?

```js
function sum() {
  return a + b;
} 

sum(); // Reference Error: a is not defined
```

![1](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/quaqsusb34cn96j9etvh.gif)
_Quand la fonction sum est appelée, elle lance une Reference Error: a is not defined_

Si vous appelez cette fonction, vous allez obtenir une Reference Error qui dit : "a is not defined".

Cela a du sens – la fonction `sum` utilise deux valeurs, `a` et `b`, mais n'a aucune idée de ce qu'elles sont.

Pour la corriger, nous devons ajouter `a` et `b` comme paramètres et passer deux nombres comme arguments.

```js
function sum(a, b) {
  return a + b;   
}

sum(2, 2); // 4
```

![2](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/6ad157f12fb7vqs2ndg5.gif)
_Corrigez la fonction sum en passant des valeurs aux deux arguments a et b_

C'est ainsi que vous passez des données à une fonction JavaScript, mais qu'en est-il d'un composant React ?

## Comment passer des données à un composant React

Un composant React ressemble beaucoup à une fonction JavaScript simple. Mais contrairement à une fonction JS, il retourne et rend des éléments React, comme un bouton.

```js
function Button() {
  return <button>Click me</button>;   
}
```

![3](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/cbqcu6zf3qwpufqpbp8c.gif)
_Composant React, Button, qui rend un élément bouton_

Pour appeler un composant React et lui faire afficher ces éléments, nous l'utilisons comme s'il s'agissait d'un élément HTML personnalisé, mais écrit en JavaScript.

```js
function App() {
  return <Button />;   
}

function Button() {
  return <button>Click me</button>;   
}
```

![4](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/xmcqn8e44iiid275os5r.gif)
_Le composant Button est utilisé dans un autre composant, App_

Mais comment passons-nous des données aux fonctions lorsqu'elles sont appelées de cette manière ?

En utilisant cette syntaxe similaire à HTML, nous pouvons lui passer n'importe quelle donnée que nous aimons comme s'il s'agissait d'un attribut HTML personnalisé.

Par exemple, si nous voulions ajouter notre propre texte personnalisé à notre bouton, nous pourrions ajouter un attribut text et définir sa valeur égale à une chaîne de caractères.

```js
function App() {
  return <Button text="\u2b50\ufe0f" />;   
}

function Button() {
  return <button>Click me</button>;   
}
```

![5](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/8qf1wtif6bfamoz7cb8j.gif)
_La prop "text" est ajoutée au composant Button, avec la valeur \u2b50\ufe0f_

Dans le monde de React, cet attribut personnalisé est ce que l'on appelle une "prop".

Nous pouvons ajouter autant de props à nos composants que nous le souhaitons. Elles peuvent être de n'importe quel type de données JavaScript.

```js
function App() {
  return <Button text="\u2b50\ufe0f" color="green" />;   
}

function Button() {
  return <button>Click me</button>;   
}
```

![6](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/98vxu9888zplkonokr3q.gif)
_Une prop nommée "color" (avec la valeur "green") est ajoutée au composant Button_

Si nous voulons utiliser les props que nous avons passées à notre composant, vous pourriez penser que chacune est passée comme un argument séparé.

![7](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/jsymr9ltwjl9kqqcxbpk.gif)
_Les props passées ne sont pas fournies comme des arguments séparés à un composant_

Mais ce n'est pas le cas. Contrairement à une fonction JavaScript régulière, toutes ces props sont collectées en une seule valeur, qui est elle-même un objet.

Ce paramètre unique est appelé et nommé "props".

![8](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/h2vkphx043s8x0mewa58.gif)
_Toutes les props qui sont passées à un composant deviennent des propriétés d'un seul objet dans les paramètres de ce composant_

Il peut être nommé n'importe quoi, mais la convention est d'appeler ce paramètre "props" parce que c'est ce qu'il contient – toutes les valeurs qui sont passées à ce composant.

Une autre raison pour laquelle il est logique d'appeler ces valeurs "props" est que ce que nous avons passé est transformé en propriétés d'un objet.

Une fois que nous avons passé les données que nous aimons à notre composant, elles peuvent être utilisées à l'intérieur de ce composant avec des accolades.

```js
function App() {
  return <Button text="\u2b50\ufe0f" color="green" />;   
}

function Button(props) {
  return (
    <button style={{ background: props.color }}>
     {props.text}
    </button>
  );
}
```

![9](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/n5smudo77dekbv641msq.gif)
_Les props "color" et "text" sont utilisées comme propriétés dans le composant Button_

Et un modèle pratique à utiliser si vos composants sont petits, est de déstructurer l'objet props.

En ajoutant une paire d'accolades dans vos paramètres, vous pouvez déstructurer les props en variables individuelles que vous pouvez utiliser directement.

```js
function App() {
  return <Button text="\u2b50\ufe0f" color="green" />;   
}

function Button({ color, text }) {
  return (
    <button style={{ background: color }}>
     {text}
    </button>
  );
}
```

![10](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/1c19ivyfpnfnpepejkjp.gif)
_Les props sont déstructurées en variables individuelles dans le composant Button, "color" et "text"_

## \ud83c\udfc6 Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : The React Bootcamp**](https://www.thereactbootcamp.com)

Il propose plus de 100 défis pratiques, des projets du monde réel et une série complète d'animations pour vous aider à enfin comprendre comment React fonctionne.

**C'est le cours que j'aurais aimé avoir quand j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*