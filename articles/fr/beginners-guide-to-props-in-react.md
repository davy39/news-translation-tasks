---
title: Comment fonctionnent les Props dans React – Un guide pour débutants
subtitle: ''
author: Temitope Oyedele
co_authors: []
series: null
date: '2022-08-04T17:31:54.000Z'
originalURL: https://freecodecamp.org/news/beginners-guide-to-props-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/A-Beginner-s-Guide-to-Props-in-Reacte--1-.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: React
  slug: react
seo_title: Comment fonctionnent les Props dans React – Un guide pour débutants
seo_desc: "Props are used to store data that can be accessed by the children of a\
  \ React component. \nThey are part of the concept of reusability. Props take the\
  \ place of class attributes and allow you to create consistent interfaces across\
  \ the component hierarch..."
---

Les props sont utilisées pour stocker des données accessibles par les enfants d'un composant React.

Elles font partie du concept de réutilisabilité. Les props prennent la place des attributs de classe et vous permettent de créer des interfaces cohérentes dans toute la hiérarchie des composants.

Dans cet article, nous allons apprendre à utiliser les props dans React. Nous verrons ce qu'elles sont et comment elles fonctionnent. Ensuite, nous examinerons comment les props se comparent à l'état (state).

Ce que nous allons couvrir :

* Qu'est-ce que les props ?
* Comment déclarer une prop
* Comment utiliser `defaultProps`
* Props vs state dans React

Alors, commençons !

## Qu'est-ce que les Props dans React ?

Props signifie simplement propriétés. Elles sont ce qui rend les composants réutilisables. Parce qu'elles remplissent une fonction essentielle – elles passent des données d'un composant à un autre. 

Les props agissent comme un canal de communication entre les composants. Les props sont passées du parent à l'enfant et aident votre enfant à accéder aux propriétés qui ont été intégrées à l'arborescence du parent.

Maintenant, imaginez que nous avons un composant sous la forme d'un produit composé du nom du produit, de sa description et de son prix. Tout ce que nous avons à faire est d'écrire le composant une fois et de le réutiliser plusieurs fois en modifiant les données que nous passons via les props, ce qui le rend conforme à la sortie souhaitée.

Il est important de noter que :

* Nous utilisons les props dans les composants fonctionnels et basés sur les classes.
* Nous passons les props de haut en bas. Nous pouvons également l'appeler ancêtre à descendant, ou parent à enfant.
* Les props sont en lecture seule. Cela signifie que, une fois qu'un composant reçoit un ensemble de props, nous ne pouvons pas les changer, mais nous pouvons seulement les utiliser et les consommer et ne pouvons pas modifier les propriétés transmises au composant. Si nous voulons modifier cela, nous devrons introduire ce que nous appelons l'état (state) dans React.

## Comment utiliser les Props dans React

Nous allons utiliser mon explication précédente sur le fait d'avoir un produit comme composant et de le réutiliser plusieurs fois pour démontrer comment utiliser les props. 

La première chose que nous allons examiner est comment utiliser les props sans déstructuration. Ensuite, nous verrons comment utiliser les props avec déstructuration. 

Savoir comment utiliser les props sans déstructuration est essentiel pour un débutant afin que vous puissiez saisir l'idée de comment fonctionnent les props.

### Comment utiliser les Props sans déstructuration

Pour commencer, créons un composant fonctionnel :

```js
import React from "react";
 
function MyProducts() {
  return (
    <div>
  
    </div>
  );
}
 
export default MyProducts;
```

Ensuite, nous voulons initialiser nos props. Donc notre composant fonctionnel ressemblera à ceci :

```js
import React from "react";
 
function MyProducts(props) {
  return (
    <div>
      <h1>{props.name}</h1>
      <p>{props.description}</p>
      <p>{props.price}</p>
    </div>
  );
}
 
export default MyProducts;
```

Donc, en gros, nous avons passé `props` comme argument dans notre fonction. `props` est passé comme paramètre à notre composant fonctionnel. Nous avons ensuite essayé d'y accéder en écrivant ce qui suit : `props.name`, `props.price` et `props.description`.

Maintenant que nous avons fait cela, nous pouvons revenir à notre `App.js` pour rendre notre produit et passer quelques données à ces trois props. Les props sont passées comme des attributs HTML. Notre `App.js` ressemblera à ceci :

```js
import "./App.css";
import MyProducts from "./MyProducts";
function App() {
  return (
    <div className="App">
      <MyProducts
        name="temitope"
        description="le produit a des fonctionnalités fantastiques"
        price={1000}
      />
    </div>
  );
}
 
export default App;
```

Et voici notre résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/props.PNG)

Voici donc la logique pour utiliser les props. Nous avons d'abord dû les initialiser, puis nous avons dû accéder aux props et au type de propriété qu'elles contiennent. Ensuite, nos composants rendus consomment ces propriétés et y passent des données.

Les props sont très pratiques ! Pourquoi ? Parce que nous pouvons rendre un composant réutilisable de diverses manières. Pour confirmer cela, nous allons copier le `MyProducts` que nous avons rendu, en collant une autre ligne mais cette fois en passant d'autres données :

```js
import "./App.css";
import MyProducts from "./Myproducts";
function App() {
  return (
    <div className="App">
      <MyProducts
        name="temitope"
        description="le produit a des fonctionnalités fantastiques"
        price={1000}
      />
      <MyProducts
        name="iphone"
        description="fonctionnalités de caméra incroyables !"
        price={5000}
      />
    </div>
  );
}
 
export default App;
```

Vous pouvez donc voir que nous réutilisons simplement le même composant avec différentes propriétés. Regardons maintenant comment passer des props avec déstructuration.

### Comment utiliser les Props avec déstructuration

La déstructuration est une fonctionnalité JavaScript qui vous permet d'extraire des sections de données d'un tableau ou d'un objet. Regardons un bref exemple de comment cela fonctionne.

Supposons que nous avons un tableau de todos et que nous voulons obtenir les deux premiers éléments de ce tableau. Une ancienne méthode serait de le faire comme ceci :

```js
const todo = ["bath","sleep","eat"];
// ancienne méthode
const firstTodo = todo[0];//bath
const secondTodo = todo[1];//sleep
 
console.log(firstTodo);
console.log(secondTodo);
```

La déstructuration offre une méthode beaucoup plus facile pour faire cela :

```js
const todo = ["bath","sleep","eat"];
 
// déstructuration
const [firstTodo, secondTodo] = todo;// bath, sleep
 
console.log(firstTodo);
console.log(secondTodo);


```

Dans React, la déstructuration nous permet de séparer ou de déballer nos props, ce qui nous permet d'accéder à nos props et de les utiliser dans un format plus lisible.

Nous pouvons utiliser la déstructuration avec le code de la section précédente comme suit :

```js
import React from "react";
 
function MyProducts({ name, description, price }) {
  return (
    <div>
      <h1>{name}</h1>
      <p>{description}</p>
      <p>{price}</p>
    </div>
  );
}
 
export default MyProducts;

```

La différence entre cette méthode et la précédente est que nous séparons les props, les déstructurons, puis les rendons. Si nous vérifions notre résultat, nous verrons qu'il est toujours intact.

Puisque les props peuvent être passées de haut en bas, nous pouvons créer un autre composant enfant dans lequel nous pouvons transmettre les attributs du parent. Voyons comment cela se fait. 

Créez un autre fichier appelé `AdditionalDescription` et passez quelques props sous la forme d'un nom et d'une description dans sa fonction :

```js
import React from "react";
 
function AdditionalDescription({ name, description }) {
  return (
    <div>
   
    </div>
 
  );
}
 
export default AdditionalDescription;
```

Nous aurons ensuite deux balises de paragraphe montrant le nom et la description. Cela rendra ce composant comme ceci :

```js
import React from "react";
 
function AdditionalDescription([name, description]) {
  return (
  <div>
      <p>{name}</p>
      <p>{description}</p>
  </div>
  )
}
 
export default AdditionalDescription;
```

Maintenant, rendons notre `AdditionalDescription` et transmettons-lui quelques props :

```js
<AdditionalDescription name={name} description={description} />
```

Vous verrez qu'il prend les props du parent.

## Comment définir une valeur par défaut pour les Props

`defaultProps` est une propriété de composant React qui nous permet de définir des valeurs par défaut pour l'argument props. Elle est généralement utile lorsque nous n'avons aucune donnée de props transmise. 

Allons-y et créons une prop par défaut :

```js
import React from "react";
 
function MyProducts({ name, description, price }) {
  return (
    <div>
      <h1>{name}</h1>
      <p>{description}</p>
      <p>{price}</p>
    </div>
  );
}
Myproducts.defaultProps = {
  name: "temitope",
  description: "j'aime cette fonctionnalité",
  price: 500,
};
 
export default MyProducts;
```

Nous avons déclaré des valeurs par défaut pour nos props vers la fin du code, juste avant d'exporter le composant. 

Pour déclarer des props par défaut, nous avons utilisé le nom du composant suivi d'un point et ensuite `defaultProps`, qui est inclus lorsque vous créez une application React.

Avec cela, nous n'aurons pas de prop vide car ces valeurs seront désormais les valeurs initiales partout où nous importons ce composant. Mais lorsque nous y passons des données, les valeurs par défaut sont alors remplacées.

## Props vs State dans React

L'état (state) est une autre façon de gérer vos données dans React. Alors, comment l'état diffère-t-il des props ? La première chose à noter est que, tandis que les props sont `en lecture seule` et sont immuables, les états changent de manière asynchrone et sont mutables.

Un état peut changer au fil du temps, et ce changement peut se produire en réponse à une action de l'utilisateur ou à un événement système. L'état ne peut être accessible ou modifié qu'à l'intérieur du composant. 

Les props, en revanche, permettent le passage de données d'un composant à un autre. Voici un tableau ci-dessous pour montrer comment ils diffèrent :

<table style="border:none;border-collapse:collapse;"><colgroup><col width="61"><col width="241"><col width="245"></colgroup><tbody><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">s/n</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Props</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"> state</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">1</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Les props sont en lecture seule</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"> L'état change de manière asynchrone</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">2</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Elles sont immuables</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Elles sont mutables</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">3</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Elles vous permettent de passer des données d'un composant à un autre</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Elles contiennent des informations sur les composants</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">4</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Elles peuvent être transmises et accessibles par un composant enfant</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Elles ne peuvent pas être accessibles par un composant enfant</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">5</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Les props sont principalement utilisées pour communiquer entre les composants</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">L'état est utilisé pour rendre les changements dynamiques</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">6</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Les props rendent les composants réutilisables</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Les états ne peuvent pas rendre les composants réutilisables</span></p></td></tr></tbody></table>

## Conclusion

Cet article a parlé de tout ce que vous devez savoir sur les props en tant que débutant. Vous avez appris ce qu'elles sont et comment les utiliser. 

Nous avons également examiné comment les props diffèrent de l'état, en citant quelques exemples qui vous seront utiles pour comprendre pleinement ce que sont les props.

Veuillez partager cet article si vous l'avez trouvé utile. Merci d'avoir lu !