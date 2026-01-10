---
title: Comment créer des formulaires dynamiques dans React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-02-09T18:08:52.000Z'
originalURL: https://freecodecamp.org/news/build-dynamic-forms-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/How-to-Build-a-Weather-Application-using-React--54-.png
tags:
- name: forms
  slug: forms
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: Comment créer des formulaires dynamiques dans React
seo_desc: "By Nishant Kumar\nIn this tutorial, let's learn how to build dynamic forms\
  \ in React. Using dynamic forms, we can add fields or remove them depending on our\
  \ needs. \nSo, let's get started.\nHow to Create a Form in React\nLet's create a\
  \ simple form first. ..."
---

Par Nishant Kumar

Dans ce tutoriel, apprenons à créer des formulaires dynamiques dans React. En utilisant des formulaires dynamiques, nous pouvons ajouter des champs ou les supprimer en fonction de nos besoins. 

Alors, commençons.

## Comment créer un formulaire dans React

Créons d'abord un formulaire simple. La syntaxe est simple :

```js
import './App.css';

function App() {
  return (
    <div className="App">
      <form>
        <div>
          <input
            name='name'
            placeholder='Nom'
          />
          <input
            name='age'
            placeholder='Âge'
          />
        </div>
      </form>
    </div>
  );
}

export default App;

```

Voici à quoi cela ressemblera :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-06-171620.jpeg)

Nous avons deux champs de saisie, qui sont Nom et Âge. Mais ces champs sont statiques. Alors, rendons-les dynamiques en utilisant les états de React.

### Comment rendre les formulaires dynamiques dans React

Créez un état appelé InputFields. Il contiendra un objet, avec les propriétés **name** et **age**. 

```js
const [inputFields, setInputFields] = useState([
    {name: '', age: ''}
])
```

Maintenant, mappons nos champs de formulaire à partir de leur état **inputFields**. 

```js
import { useState } from 'react';
import './App.css';

function App() {
  const [inputFields, setInputFields] = useState([
    { name: '', age: '' }
  ])
  return (
    <div className="App">
      <form>
        {inputFields.map((input, index) => {
          return (
            <div key={index}>
              <input
                name='name'
                placeholder='Nom'
              />
              <input
                name='age'
                placeholder='Âge'
              />
            </div>
          )
        })}
      </form>
    </div>
  );
}

export default App;

```

Maintenant, nous ne verrons qu'un seul ensemble de champs de saisie, car nous n'avons qu'un seul objet dans l'état **inputFields**. Si nous ajoutons plus d'objets, nous verrons plusieurs champs de saisie.

## Comment ajouter les valeurs de l'état inputFields

Maintenant, ajoutons les valeurs de l'état **inputFields** aux champs de saisie.

```js
import { useState } from 'react';
import './App.css';

function App() {
  const [inputFields, setInputFields] = useState([
    { name: '', age: '' }
  ])
  return (
    <div className="App">
      <form>
        {inputFields.map((input, index) => {
          return (
            <div key={index}>
              <input
                name='name'
                placeholder='Nom'
                value={input.name}
              />
              <input
                name='age'
                placeholder='Âge'
                value={input.age}
              />
            </div>
          )
        })}
      </form>
    </div>
  );
}

export default App;

```

Les valeurs seront **input.name** et **input.age.** 

Ajoutons également un événement onChange qui s'exécutera lorsque nous taperons quelque chose dans les champs de saisie.

Créez une fonction appelée **handleFormChange**. 

```js
const handleFormChange = () => {
    
}
```

Assignez cette fonction aux champs de saisie en tant qu'événement onChange.

```js
<div key={index}>
              <input
                name='name'
                placeholder='Nom'
                value={input.name}
                onChange={event => handleFormChange(index, event)}
              />
              <input
                name='age'
                placeholder='Âge'
                value={input.age}
                onChange={event => handleFormChange(index, event)}
              />
            </div>
```

Cet événement onChange prend deux paramètres, **index** et **event**. Index est l'index du tableau et event est les données que nous tapons dans le champ de saisie. Nous passons ceux-ci à la fonction **handleFormChange**. 

```js
const handleFormChange = (index, event) => {
    
}
```

Mais le problème est que si nous essayons de taper quelque chose dans les champs de saisie, nous ne pourrons pas. Parce que nous n'avons pas défini les états dans l'état **formFields**. Alors, faisons cela.

```js
 const handleFormChange = (index, event) => {
    let data = [...inputFields];
 }
```

Stockez notre état **inputFields** dans une variable appelée **data** en utilisant l'opérateur de décomposition (les trois points `...`). 

Ensuite, nous ciblerons l'index de la variable data en utilisant le paramètre index, et le nom de la propriété, aussi. 

```js
const handleFormChange = (index, event) => {
    let data = [...inputFields];
    data[index][event.target.name] = event.target.value;
}
```

Par exemple, supposons que nous tapons dans le champ de saisie avec **index 0**. Donc, nous spécifions l'index dans data, et le nom de la propriété, en utilisant **event.target.name.** Et à l'intérieur de cet index de data, nous stockons les valeurs des champs de saisie en utilisant **event.target.value.** 

Maintenant, nous devons stocker ces données à l'intérieur du tableau **inputFields** en utilisant la méthode **setInputFields**. 

```js
const handleFormChange = (index, event) => {
   let data = [...inputFields];
   data[index][event.target.name] = event.target.value;
   setInputFields(data);
}
```

Maintenant, si nous tapons quelque chose dans les champs de saisie, cela apparaîtra dans les champs de saisie.

## Comment ajouter plus de champs de formulaire

Créons un bouton pour ajouter plus de champs de formulaire. 

```js
<button>Ajouter plus..</button>
```

Et une fonction aussi, qui sera déclenchée lorsque ce bouton est cliqué.

```js
const addFields = () => {
    
}
```

Ajoutons la fonction au bouton via un événement onClick.

```js
<button onClick={addFields}>Ajouter plus..</button>
```

Maintenant, dans la fonction addFields, nous devons créer un objet. Et chaque fois que nous cliquons sur le bouton, il sera ajouté à l'état **inputFields**, créant ainsi un nouveau champ de saisie.

```js
const addFields = () => {
    let newfield = { name: '', age: '' }
}
```

Ensuite, définissez ce newField à l'intérieur de l'état **inputFields**. 

```js
const addFields = () => {
    let newfield = { name: '', age: '' }

    setInputFields([...inputFields, newfield])
}
```

Ici, nous définissons également les **inputFields** existants en utilisant l'opérateur de décomposition, en conjonction avec le newfield. 

Si nous cliquons sur le bouton Ajouter un champ maintenant, il créera un nouveau champ de saisie.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-06-174542.jpeg)

## Comment créer un bouton de soumission

Créons un bouton de soumission et une fonction pour voir nos données lorsque nous soumettons le formulaire.

```js
<button>Soumettre</button>
```

Nous avons également besoin d'une fonction qui sera déclenchée lorsque nous cliquons sur ce bouton. Elle enregistrera les données dans la console, à partir des champs de saisie. Elle dispose également d'une méthode appelée **e.preventDefault()** qui empêchera la page de se rafraîchir.

```js
const submit = (e) => {
    e.preventDefault();
    console.log(inputFields)
}
```

Ajoutez cette fonction au bouton de soumission :

```js
<button onClick={submit}>Soumettre</button>
```

Et aussi dans la balise form :

```js
<form onSubmit={submit}>
```

Si nous soumettons, nous verrons nos données dans la console :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-06-175919.jpeg)

## Comment supprimer les champs à l'aide d'un bouton de suppression

Maintenant, créons un bouton pour supprimer ces champs si nous ne les voulons pas.

```js
<form>
        {inputFields.map((input, index) => {
          return (
            <div key={index}>
              <input
                name='name'
                placeholder='Nom'
                value={input.name}
                onChange={event => handleFormChange(index, event)}
              />
              <input
                name='age'
                placeholder='Âge'
                value={input.age}
                onChange={event => handleFormChange(index, event)}
              />
              <button>Supprimer</button>
            </div>
          )
        })}
      </form>
```

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-06-174720.jpeg)

Nous avons également besoin d'une fonction.

```js
const removeFields = () => {

}
```

Alors, assignez cette fonction au bouton de suppression.

```js
<button onClick={() => removeFields(index)}>Supprimer</button>
```

Nous passons l'index en tant que paramètre, qui est l'index des champs de saisie.

Ensuite, recevez cet index dans la fonction.

```js
const removeFields = (index) => {
  
}
```

Et comme avant, nous devons créer une nouvelle variable et stocker l'état **inputFields** dans cette nouvelle variable.

```js
const removeFields = (index) => {
    let data = [...inputFields];
}
```

Ensuite, nous devons épisser cette variable de données par l'index. Ensuite, nous devons la stocker dans l'état **inputFields** en utilisant setInputFields.

```js
const removeFields = (index) => {
    let data = [...inputFields];
    data.splice(index, 1)
    setInputFields(data)
}
```

Maintenant, si nous cliquons sur supprimer, cela supprimera ce champ de formulaire.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-06-175415.jpeg)

Nous avons donc cinq champs de saisie ici, avec cinq noms différents. Supprimons la saisie de Nishant.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-06-180336.jpeg)

Vous voyez qu'il a été supprimé. Et si nous soumettons, nous verrons nos données mises à jour dans la console.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-06-180434.jpeg)

## Conclusion

Maintenant, vous savez comment créer des formulaires dynamiques dans React. Félicitations !

Vous pouvez également regarder ma vidéo sur le même sujet [Dynamic Forms - How to Add Dynamic Forms in React](https://youtu.be/LcAyJRlvh8Y).

Essayez le code ici – [https://github.com/nishant-666/Dynamic-Forms](https://github.com/nishant-666/Dynamic-Forms).

Bonne apprentissage :)