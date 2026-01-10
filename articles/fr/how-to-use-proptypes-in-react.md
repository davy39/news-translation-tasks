---
title: Comment utiliser PropTypes dans React
subtitle: ''
author: Ateev Duggal
co_authors: []
series: null
date: '2022-02-14T16:36:09.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-proptypes-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/props.png
tags:
- name: React
  slug: react
seo_title: Comment utiliser PropTypes dans React
seo_desc: 'PropTypes are a good first line defense when it comes to debugging your
  apps. But before getting into detail about PropTypes, we have to understand the
  concept of props.

  Props are the read-only properties that are shared between components to give th...'
---

Les PropTypes sont une bonne première ligne de défense lorsqu'il s'agit de déboguer vos applications. Mais avant d'entrer dans les détails des PropTypes, nous devons comprendre le concept de props.

Les [Props](https://tekolio.com/what-are-props-in-react-and-how-to-use-them/) sont les propriétés en lecture seule qui sont partagées entre les composants pour donner au flux unidirectionnel de React une touche dynamique. Elles sont principalement partagées du composant parent vers le composant enfant, mais l'inverse est également possible (bien que non recommandé).

Dans ce blog, nous discuterons de la manière de valider ou de vérifier les props que nous passons pour éviter un débogage complexe à un stade ultérieur.

## Qu'est-ce que les PropTypes ?

Les PropTypes sont simplement un mécanisme qui garantit que la valeur passée est du type de données correct. Cela permet de s'assurer que nous ne recevons pas d'erreur à la toute fin de notre application par la console, ce qui pourrait ne pas être facile à gérer.

Je ne recommande pas de les utiliser dans des applications courtes comme des projets pour l'auto-pratique, mais cela dépend totalement de vous. Pour des projets plus importants, comme pour un client, c'est souvent un choix judicieux et une bonne pratique de les utiliser.

Il existe de nombreux types différents de PropTypes et chacun d'eux a ses propres classes ES6 uniques que nous pouvons utiliser. Nous discuterons de chaque type dans cet article.

## Comment utiliser les PropTypes

Avant la sortie de React 15.5.0, les PropTypes étaient disponibles dans le package React, mais maintenant nous devons ajouter la bibliothèque prop-types dans notre projet.

Nous pouvons le faire en exécutant la commande suivante dans notre terminal :

```javascript
npm install prop-types --save
```

Nous pouvons utiliser PropTypes pour valider toute donnée que nous recevons des props. Mais avant de l'utiliser, nous devrons l'importer comme toujours dans notre application :

```javascript
import PropTypes from 'prop-types';
```

Ils sont souvent utilisés après la fin du composant et commencent par le nom du composant comme montré :

```javascript
import React from 'react';
import { PropTypes } from "prop-types";
 
const Count = (props) => {
  return (
    <>
      .........
    </>
  )
};
 
Count.propTypes = {
  //// la clé est le nom de la prop et
// la valeur est le PropType
}
export default Count;
```

Les PropTypes sont également des objets avec une paire clé-valeur où la 'clé' est le nom de la prop tandis que la valeur représente le type ou la classe par laquelle ils sont définis.

Puisque la définition des PropTypes sur un composant ne dépend pas de l'implémentation du composant, nous omettons le code du composant lui-même dans tous les exemples suivants. Le code ci-dessus peut être simplifié comme suit :

```javascript
Count.propTypes = {
// Mettre les props ici
}
```

Discutons du nombre de types de PropTypes qui existent avant de les comprendre avec un exemple.

## Types de base des PropTypes

La manière la plus basique de vérifier le type d'une prop est de vérifier si elle appartient à la catégorie des types primitifs en JavaScript, tels qu'un booléen, une chaîne de caractères, un objet, et ainsi de suite.

Voici la liste de tous les types de données considérés comme primitifs ou basiques avec leurs classes que nous pouvons utiliser pour vérifier les props.

| **Type** | **Classe** | **Exemple** |
| --- | --- | --- |
| **String** | PropType.string | "hello" |
| **Object** | PropType.object | {name: "Rohit"} |
| **Number** | PropType.number | 10 |
| **Boolean** | PropType.bool | true/false |
| **Function** | PropType.func | const say = {console.log("hello")} |
| **Symbol** | PropType.symbol | Symbol("m") |

Voici un exemple qui nous montre comment utiliser ces PropTypes pour la vérification de type dans notre application. Comme nous l'avons déjà discuté, ils sont définis comme des objets avec une paire clé-valeur où la clé est le nom de l'objet tandis que la valeur contient les classes qui seront utilisées pour la vérification de type.

```javascript
Count.propTypes = {
  name: PropTypes.string,
  age: PropTypes.number,
  address: PropTypes.object,
  friends: PropTypes.array,
};
```

Dans le code ci-dessus, la prop name est censée avoir une valeur qui est une chaîne de caractères, age est un nombre, address est un objet, et friends est un tableau. Si une valeur autre que celle-ci a été utilisée pour les mêmes props en tant que valeur, elle affichera une erreur dans la console comme ceci :

![Image](https://lh3.googleusercontent.com/NoiuFl2D3WofbIe7_CsqbNkolVLFzXyPSvvADV3LvFug2jp2oMhBXFl42Qy79e4LkGAOio5RD5rAhlUOBJEoSP3oDUuWNwxb1wCfQYdYQpWvdtDbKQQDkwt0rMSD9dlQAhXozKKC align="left")

*Erreur de console pour les PropTypes incorrects*

Nous pouvons enchaîner n'importe lequel des éléments ci-dessus avec `isRequired` pour nous assurer qu'un avertissement est affiché si la prop n'est pas fournie.

```javascript
Count.propTypes = {
  basicObject: PropTypes.object,
  numbers: PropTypes.objectOf(PropTypes.numbers),
  messages: PropTypes.instanceOf(Message),
  contactList: PropTypes.shape({
    name: PropTypes.string.isRequired,
    phone: PropTypes.string.isRequired,
  }),
};
```

## Type collectif

Nous avons vu comment valider ou vérifier pour voir dans quelle catégorie de type de données de base les props tombent. Mais il existe de nombreuses autres façons dont les props peuvent être passées et utilisées – comme des types collectifs tels qu'un tableau de nombres, de chaînes de caractères, et ainsi de suite. Alors, qu'en est-il d'eux ?

Nous pouvons également vérifier les props pour eux. Voici les différentes façons dont un type de données peut être combiné et utilisé.

### Types de tableau

Ici, nous discuterons de toutes les possibilités qui peuvent être formées avec un tableau avec leurs exemples, tout comme nous l'avons vu avec les types de base.

| **Type** | **Classe** | **Exemple** |
| --- | --- | --- |
| **Array** | PropTypes.array | [] |
| **Array of numbers** | PropTypes.arrayOf([type]) | [1,2,3] |
| **Array of string** | PropTypes.oneOf([arr]) | ["Red", "blue"] |
| **Array of objects** | PropTypes.oneOfType([types]) | PropTypes.string, |

```javascript
Count.propTypes = {
  counts: PropTypes.array,
  users: PropTypes.arrayOf(PropTypes.object),
  alarmColor: PropTypes.oneOf(['red', 'blue']),
  description: PropTypes.oneOfType([
  PropTypes.string,
  PropTypes.instanceOf(Title)
  ]),
  }
```

### Types d'objet

Tout comme les types de tableau, voici quelques-uns des types d'objet collectifs :

| **Type** | **Classe** | **Exemple** |
| --- | --- | --- |
| **Object** | PropTypes.object | {name: "Anu"} |
| **Number Object** | PropTypes.objectOf() | {age: 25} |
| **Object Shape** | PropTypes.shape() | {name: PropTypes.string, |
| **Instance** | PropTypes.objectOf() | New message() |

```javascript
Count.propTypes = {
  basicObject: PropTypes.object,
  numbers: PropTypes.objectOf(PropTypes.numbers),
  messages: PropTypes.instanceOf(Message),
  contactList: PropTypes.shape({
    name: PropTypes.string,
    phone: PropTypes.string,
  }),
};
```

## Vérification de type avancée

Il existe de nombreuses façons autres que la vérification de type de base que nous pouvons utiliser pour vérifier nos props. Cette méthode se concentre principalement sur le code React plutôt que sur les types de données.

### Comment vérifier un composant React

Si vous voulez simplement vérifier si une prop est un composant React, vous pouvez utiliser **PropTypes.element**. Cela est utile pour s'assurer qu'un composant n'a qu'un seul composant enfant.

| **Type** | **Classe** | **Exemple** |
| --- | --- | --- |
| **Element** | PropTypes.element | <Title /> |

```javascript
Count.propTypes = {
  displayEle: PropTypes.element,
};
```

### Comment vérifier un nom de composant React

Enfin, nous pouvons vérifier si la prop est le nom d'un composant React en utilisant **PropTypes.elementType**.

```javascript
Component.propTypes = {
  as: PropTypes.elementType
}
```

```javascript
<AnotherComponent as={Component} />
```

## Types personnalisés

Nous pouvons également avoir un validateur personnalisé ou une vérification de type pour les props, mais cela nécessite un objet d'erreur si la validation échoue.

Vous pouvez utiliser cela pour les tableaux et les objets, mais l'objet d'erreur sera appelé pour chaque clé dans le tableau ou l'objet. Les deux premiers arguments du validateur sont le tableau ou l'objet lui-même et la clé de l'élément actuel.

| **Type** | **Classe** | **Exemple** |
| --- | --- | --- |
| **Custom** | function(props, propName, componentName) {} | "hello" |
| **Custom Array** | PropTypes.arrayOf(function(props, propName, componentName) {}) | ["hello"] |

```javascript
Count.propTypes = {  // fonction normale
  customProp: function (props, propName, componentName) {
    if (!/matchme/.test(props[propName])) {
      return new Error(
        "Invalid prop `" +
          propName +
          "` supplied to" +
          " `" +
          componentName +
          "`. Validation failed."
      );
    }
  },
};
```

```javascript
Count.propTypes = { // fonction de tableau
  customArrayProp: PropTypes.arrayOf(function (
    propValue,
    key,
    componentName,
    location,
    propFullName
  ) {
    if (!/matchme/.test(propValue[key])) {
      return new Error(
        "Invalid prop `" +
          propFullName +
          "` supplied to" +
          " `" +
          componentName +
          "`. Validation failed."
      );
    }
  }),
};
```

## PropTypes par défaut

Parfois, nous voulons pouvoir définir une valeur par défaut pour une prop. Par exemple, notre composant parent peut ne pas nécessiter qu'un titre soit passé. Mais nous voulons toujours qu'un titre soit rendu.

Dans des cas comme celui-ci, nous pouvons définir une valeur par défaut pour notre titre qui sera automatiquement rendue si le titre n'a pas été passé en tant que prop depuis notre composant parent.

```javascript
Header.defaultProp = {
  title: "GitHub Users",
};
```

Nous pouvons lire plus à ce sujet dans la [documentation officielle](https://reactjs.org/docs/typechecking-with-proptypes.html).

## Exemple

Comprenons comment tout cela fonctionne avec un simple code React.

Nous allons créer deux composants réutilisables, **About.js** et **Count.js**. Le composant **About** est le composant parent et le composant **Count** est le composant enfant comme montré ici :

![Image](https://lh4.googleusercontent.com/9h86z3UDdPR9zlqR19PVQFJYvAq0j2r6ZobSn1cC6Ev8JAjQo_tFRJobuIQeg0sHLc8Wha8yZp3SGQGcxrxYMA-Mo_HrCsxBrPnv6TfhqS_q9Iqioku1LaRTbx69qBsx_PueJtqe align="left")

![Image](https://lh3.googleusercontent.com/2RbGh5-GHCcP57-3GG9ysJ-9p7xFIOKRzg2Z_TzzJFObcqalPbUe_8MDe1iyckfD0rKxg6Kfcksd8V9uNx9SHV6sUr8yM37Z2NP1k7YS_e7WLIz-OXtq-jOS7DsRTjfj-C0PBPBp align="left")

Et si nous changeons la valeur de la prop age d'un nombre en une chaîne de caractères sans changer son type (PropTypes) ?

```javascript
import React from "react";
import Count from "./Count";
const About = () => {
  return (
    <>
      <div className="app">
        <Count name="Ateev" age="25" />
      </div>
    </>
  );
};
 
export default About;
```

Nous recevrons une erreur dans la console disant ceci :

![Image](https://lh3.googleusercontent.com/NoiuFl2D3WofbIe7_CsqbNkolVLFzXyPSvvADV3LvFug2jp2oMhBXFl42Qy79e4LkGAOio5RD5rAhlUOBJEoSP3oDUuWNwxb1wCfQYdYQpWvdtDbKQQDkwt0rMSD9dlQAhXozKKC align="left")

Il est clairement indiqué que la valeur de la prop age passée ne correspond pas à la valeur attendue (PropTypes).

À partir de l'exemple ci-dessus, il devrait maintenant être clair comment nous pouvons utiliser les PropTypes. Vous pouvez également voir à quel point ils sont utiles pour déboguer vos applications lorsque l'application est trop grande pour trouver le bug avec des méthodes conventionnelles.

## Conclusion

Les PropTypes sont un excellent moyen de capturer les erreurs à l'exécution et agissent comme la première ligne de défense pour vos applications. Ils ne sont pas aussi sûrs en termes de typage que TypeScript, mais ils sont beaucoup plus faciles à configurer et à utiliser.

Vous pouvez également consulter certains de mes autres blogs :

1. [Que signifie le terme **Virtual DOM** dans React](https://tekolio.com/react-virtual-dom-explained-in-simple-words/)
    
2. [Qu'est-ce que les Hooks dans React ?](https://tekolio.com/what-are-hooks-in-react/)
    
3. [Comment créer un portfolio dans React](https://tekolio.com/how-i-made-my-portfolio-in-react/)