---
title: Apprendre les bases de la déstructuration des props dans React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-01T23:46:40.000Z'
originalURL: https://freecodecamp.org/news/the-basics-of-destructuring-props-in-react-a196696f5477
coverImage: https://cdn-media-1.freecodecamp.org/images/1*WUKuIELNzTHKfAeHLNlsqQ.jpeg
tags:
- name: ES6
  slug: es6
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Apprendre les bases de la déstructuration des props dans React
seo_desc: 'By Evelyn Chan

  When I first learned about ES6, I was hesitant to start using it. I’d heard a lot
  of great things about the improvements but at the same time, I’d just gotten used
  to the good ol’ original way of doing things and here was a new syntax ...'
---

Par Evelyn Chan

Lorsque j'ai appris pour la première fois ES6, j'étais réticente à commencer à l'utiliser. J'avais entendu beaucoup de bonnes choses sur les améliorations, mais en même temps, je venais tout juste de m'habituer à la bonne vieille méthode originale de faire les choses et voici qu'une nouvelle syntaxe était lancée pour que je l'apprenne.

Je l'ai évitée pendant un moment sous le prétexte de "si ce n'est pas cassé, ne le répare pas", mais j'ai récemment apprécié sa simplicité et le fait qu'elle devienne la norme en JavaScript.

Avec React, qui adopte pleinement la syntaxe ES6, la déstructuration ajoute une multitude d'avantages pour améliorer votre code. Cet article passera en revue les bases de la déstructuration des objets et comment cela s'applique aux props dans React.

### Raisons de déstructurer

#### **Améliore la lisibilité**

C'est un énorme avantage dans React lorsque vous passez des props. Une fois que vous avez pris le temps de déstructurer vos props, vous pouvez vous débarrasser de `props / this.props` devant chaque prop.

Si vous abstraisez vos composants dans différents fichiers, vous aurez également un endroit pratique pour référencer rapidement les props que vous passez sans avoir à changer d'onglet. Cette double vérification vous aide à attraper des erreurs telles que le passage de props excessives ou des fautes de frappe.

Vous pouvez aller plus loin en ajoutant une validation `propType`, qui vous permet de définir le type de chaque prop que vous passez. Lorsque vous êtes dans un environnement de développement, cela déclenche React pour enregistrer un avertissement si le type est différent de celui défini.

Les props peuvent être difficiles à suivre dans les applications complexes, donc définir clairement vos props lorsque vous les passez est extrêmement utile pour toute personne lisant votre code.

#### **Lignes de code plus courtes**

Voyez ce qui suit avant ES6 :

```
var object = { one: 1, two: 2, three: 3 }
```

```
var one = object.one;var two = object.two;var three = object.three
```

```
console.log(one, two, three) // imprime 1, 2, 3
```

C'est long, encombrant et prend beaucoup trop de lignes de code. Avec la déstructuration, votre code devient beaucoup plus clair.

Dans l'exemple ci-dessous, nous avons effectivement réduit le nombre de lignes à deux :

```
let object = { one: 1, two: 2, three: 3 }
```

```
let { one, two, three } = object;
```

```
console.log(one, two, three) // imprime 1, 2, 3
```

#### **Sucre syntaxique**

Cela rend le code plus beau, plus succinct, et comme si quelqu'un qui sait ce qu'il fait l'avait écrit. Je réitère quelque peu le premier point ici, mais après tout, si cela améliore la lisibilité, pourquoi ne pas le faire ?

### Composants fonctionnels vs. Composants de classe

La déstructuration dans React est utile pour les composants fonctionnels et de classe, mais elle est réalisée un peu différemment.

Considérons un composant parent dans notre application :

```
import React, { Component } from 'react';
```

```
class Properties extends Component {  constructor() {    super();    this.properties = [      {        title: 'Modern Loft',        type: 'Studio',        location: {          city: 'San Francisco',          state: 'CA',          country: 'USA'        }      },      {        title: 'Spacious 2 Bedroom',        type: 'Condo',        location: {          city: 'Los Angeles',          state: 'CA',          country: 'USA'        }      },    ];  }
```

```
render() {    return (      <div>        <Listing listing={this.properties[0]} />        <Listing listing={this.properties[1]} />      </div>    );  }}
```

#### Composants fonctionnels

Dans cet exemple, nous voulons passer un objet `listing` de notre tableau de propriétés pour que le composant enfant le rende.

Voici à quoi ressemblerait un composant fonctionnel :

```
const Listing = (props) => (  <div>    <p>Titre : {props.listing.title}</p>    <p>Type : {props.listing.type}</p>    <p>      Emplacement : {props.listing.location.city},      {props.listing.location.state},      {props.listing.location.country}    </p>  </div>);
```

Ce bloc de code est entièrement fonctionnel mais a l'air terrible ! Au moment où nous arrivons à ce composant enfant `Listing`, nous savons déjà que nous référençons un listing, donc `props.listing` semble et est redondant. Ce bloc de code peut être rendu beaucoup plus propre grâce à la déstructuration.

Nous pouvons y parvenir dans le paramètre de la fonction lorsque nous passons l'argument props :

```
const Listing = ({ listing }) => (  <div>    <p>Titre : {listing.title}</p>    <p>Type : {listing.type}</p>    <p>      Emplacement : {listing.location.city},      {listing.location.state},      {listing.location.country}    </p>  </div>);
```

Mieux encore, nous pouvons déstructurer davantage les objets imbriqués comme ci-dessous :

```
const Listing = ({  listing: {    title,    type,    location: {      city,      state,      country    }  }}) => (  <div>    <p>Titre : {title}</p>    <p>Type : {type}</p>    <p>Emplacement : {city}, {state}, {country}</p>  </div>);
```

Pouvez-vous voir à quel point cela est plus facile à lire ? Dans cet exemple, nous avons déstructuré à la fois `listings` et les clés à l'intérieur de `listing`.

Un piège courant est de déstructurer uniquement les clés comme nous le faisons ci-dessous et d'essayer d'accéder à l'objet :

```
{ location: { city, state, country } }
```

Dans ce scénario, nous ne pourrions pas accéder à l'objet `location` via une variable nommée location.

Pour ce faire, nous devrions d'abord le définir avec une simple correction comme suit :

```
{ location, location: { city, state, country } }
```

Cela n'était pas flagrant pour moi au début, et j'avais occasionnellement des problèmes si je voulais passer un objet comme `location` en tant que prop après avoir déstructuré son contenu. Maintenant, vous êtes équipé pour éviter les mêmes erreurs que j'ai faites !

#### Composants de classe

L'idée est très similaire dans les composants de classe, mais l'exécution est un peu différente.

Jetez un œil ci-dessous :

```
import React, { Component } from 'react';
```

```
class Listing extends Component {  render() {    const {      listing: {        title,        type,        location: {          city,          state,          country        }      }    } = this.props;
```

```
return (      <div>        <p>Titre : {title}</p>        <p>Type : {type}</p>        <p>          Emplacement : {city}, {state}, {country}        </p>      </div>    )  }}
```

Vous avez peut-être remarqué dans l'exemple parent que nous pouvons déstructurer l'objet `Component` lorsque nous importons `React` dans les composants de classe. Cela n'est pas nécessaire pour les composants fonctionnels car nous n'étendrons pas la classe `Component` pour ceux-ci.

Ensuite, au lieu de déstructurer dans l'argument, nous déstructurons là où les variables sont appelées. Par exemple, si nous prenons le même composant enfant `Listing` et le refactorisons en une classe, nous déstructurerions dans la fonction `render` où les props sont référencées.

L'inconvénient de la déstructuration dans les composants de classe est que vous finirez par déstructurer les mêmes props chaque fois que vous les utilisez dans une méthode. Bien que cela puisse être répétitif, je dirais qu'un point positif est qu'il définit clairement quelles props sont utilisées dans chaque méthode.

De plus, vous n'aurez pas à vous soucier des effets secondaires tels que le changement accidentel d'une référence de variable. Cette méthode garde vos méthodes séparées et propres, ce qui peut être un énorme avantage pour d'autres opérations pendant vos projets telles que le débogage ou l'écriture de tests.

Merci d'avoir lu ! Si cela vous a aidé, veuillez applaudir et/ou partager cet article pour qu'il puisse aider les autres aussi ! 😊