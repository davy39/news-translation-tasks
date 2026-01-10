---
title: Comment déstructurer les propriétés d'objet en utilisant array.map() dans React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-11-02T17:07:58.000Z'
originalURL: https://freecodecamp.org/news/destructure-object-properties-using-array-map-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/pexels-pixabay-276502.jpg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: Comment déstructurer les propriétés d'objet en utilisant array.map() dans
  React
seo_desc: "By Caleb Olojo\nOne of the methods frontend developers use the most in\
  \ JavaScript is the Array.prototype.map() method. \nFrom having to render a list\
  \ of items in the DOM to looping through a series of blog posts – and many more\
  \ – the usefulness goes on..."
---

Par Caleb Olojo

L'une des méthodes les plus utilisées par les développeurs frontend en JavaScript est la méthode `Array.prototype.map()`.

Que ce soit pour rendre une liste d'éléments dans le DOM ou pour parcourir une série d'articles de blog - et bien plus encore - son utilité est infinie.

Imaginons que vous avez une liste d'éléments dans un tableau qui doit être rendue en tant que composant React sur une page web. La manière idéale de mapper une série d'éléments dans un tableau ressemble à ceci :

```js
const shoppingList = ['Oranges', 'Cassava', 'Garri', 'Ewa', 'Dodo', 'Books']

export default function List() {
  return (
    <>
      {shoppingList.map((item, index) => {
        return (
          <ol>
            <li key={index}>{item}</li>
          </ol>
        )
      })}
    </>
  )
}
```

L'extrait ci-dessus remplit parfaitement son objectif. Mais que faire si vous devez mapper un tableau d'objets avec plusieurs propriétés ? Par exemple, un tableau comme celui ci-dessous ?

```js
const employees = [
  {
    name: 'Saka Manje',
    address: '14, cassava-garri-ewa street',
    gender: 'Male',
  },
  {
    name: 'Wawawa Warisii',
    address: '406, highway street',
    gender: 'Male',
  },
]
```

Pour être concis, restons avec deux éléments dans le tableau. Utilisons maintenant la même approche que celle utilisée dans l'extrait précédent.

```js
export default function EmployeesList() {
  return (
    <>
      {employees.map((employee, index) => {
        return (
          <div key={index}>
            <p>{employee.name}</p>
            <p>{employee.address}</p>
            <p>{employee.gender}</p>
          </div>
        )
      })}
    </>
  )
}
```

Bien que l'approche dans l'extrait ci-dessus semble parfaitement correcte, vous pourriez vous demander : "Que se passe-t-il lorsque je reçois des objets profondément imbriqués en tant que données depuis un endpoint ?"

## Comment déstructurer les propriétés d'objet

Dans la section précédente, nous avons passé en revue la manière conventionnelle de rendre les données d'un endpoint API sur une page web avec la méthode `.map()` de JavaScript.

Dans cette section, nous allons voir comment obtenir le même résultat sans utiliser la notation par points pour accéder aux propriétés du tableau.

Mais avant cela, que signifie exactement déstructurer les propriétés d'un objet ? Eh bien, le but de la déstructuration est de pouvoir accéder aux variables au sein des tableaux ou des objets, puis de procéder en les assignant à une variable. Vous pouvez voir un exemple ci-dessous.

```js
const person = {
  name: 'Adrian Tojubole',
  role: 'Lead Engineer',
  salary: '$130k/year',
}

let { name, role, salary } = person

console.log(name); // Adrian Tojubole
console.log(role); // Lead Engineer
console.log(salary); // $130k/year
```

Vous remarquerez que nous avons pu accéder aux propriétés - `name`, `role`, et `salary` - de l'objet `person`. Cela évite d'utiliser la notation par points pour y accéder, comme dans l'extrait ci-dessous, ce qui rend le processus répétitif pour nous.

```js
console.log(person.name);
console.log(person.role);
console.log(person.salary);
```

Cela étant dit, nous allons utiliser ce modèle chaque fois que nous voulons utiliser la méthode `.map()` dans React. Prenons le tableau d'objets ci-dessous, par exemple :

```js
const employeesData = [
  {
    name: 'Saka manje',
    address: '14, cassava-garri-ewa street',
    attributes: {
      height: '6ft',
      hairColor: 'Brown',
      eye: 'Black',
    },
    gender: 'Male',
  },
  {
    name: 'Adrian Toromagbe',
    address: '14, kogbagidi street',
    attributes: {
      height: '5ft',
      hairColor: 'Black',
      eye: 'Red',
    },
    gender: 'Male',
  },
]
```

Dans l'extrait ci-dessus, vous remarquerez que nous avons un objet imbriqué dans un autre objet, en tant que propriété. Maintenant, la manière initiale d'accéder aux propriétés de cet objet imbriqué ressemblerait à ceci :

```js
employeesData.map(data => data.attributes.height);
```

Mais, lorsque vous déstructurez les propriétés de cet objet, la syntaxe ressemble à ceci :

```js
employeesData.map(
  ({ name, address, attributes: { height, hairColor, eye }, gender }, index) => {
    return name, address, height, hairColor, eye
  }
)
```

L'extrait ci-dessus élimine le processus de faire ceci : `employee.name`, `employee.attributes.height`, et ainsi de suite.

Maintenant que vous avez une idée de son fonctionnement, il est temps de placer ce `.map()` dans un composant React, puis de retourner les propriétés correspondantes.

```js
export default function Employees() {
  return (
    <div>
      {employeesData.map(
        (
          { name, address, gender, attributes: { height, hairColor, eye } },
          index
        ) => {
          return (
            <div className="employees" key={index}>
              <p>{name}</p>
              <p>{address}</p>
              <p>{gender}</p>
              <p>{height}</p>
              <p>{eye}</p>
              <p>{hairColor}</p>
            </div>
          )
        }
      )}
    </div>
  )
}
```

## Conclusion

Avec cette approche, vous pouvez économiser beaucoup de temps que vous passez à utiliser la notation par points pour accéder aux propriétés des objets. Cela est utile avec le temps, car vous pourriez commencer à interagir avec des APIs GraphQL, et certaines de ces APIs sont connues pour retourner des objets profondément imbriqués en tant que données.

Vous pouvez également déstructurer les propriétés des tableaux. Un excellent exemple est la manière dont nous déstructurons une `value` et la fonction de rappel `setValue` lorsque nous utilisons l'un des hooks populaires de React - `useState`

```js
const [count, setCount] = React.useState(0)
```

Merci d'avoir lu ce tutoriel. J'espère que vous l'avez trouvé utile.