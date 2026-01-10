---
title: Parcourir un objet imbriqué dans React.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-02T02:17:00.000Z'
originalURL: https://freecodecamp.org/news/iterate-through-nested-object-in-react-js
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9aa2740569d1a4ca26c5.jpg
tags:
- name: object
  slug: object
- name: React
  slug: react
- name: toothbrush
  slug: toothbrush
seo_title: Parcourir un objet imbriqué dans React.js
seo_desc: "If you've ever worked with APIs, you'll know that the structure of the\
  \ data they return can get complicated quickly.\nImagine you call an API from your\
  \ React project and the response looks something like this:\nObject1 {\n     Object2\
  \ {\n           prope..."
---

Si vous avez déjà travaillé avec des APIs, vous savez que la structure des données qu'elles retournent peut rapidement devenir compliquée.

Imaginez que vous appelez une API depuis votre projet React et que la réponse ressemble à ceci :

```json
Object1 {
     Object2 {
           propertyIWantToAcess:
           anotherpropertyIWantToAcess:
      }
}
```

Vous avez stocké les données dans l'état de votre composant sous `this.state.myPosts`, et vous pouvez accéder aux éléments de l'objet externe avec ce qui suit :

```jsx
render() {
    console.log(this.state.myPosts);

    const data = this.state.myPosts;

    const display = Object.keys(data).map((d, key) => {
    return (
      <div className="my-posts">
        <li key={key}>
          {data.current_route}
        </li>
      </div>
      );
    });

    return(
      <div>
        <ul>
          { display }
        </ul>
      </div>
    );
  }
```

Mais le problème est que vous n'êtes pas en mesure d'accéder aux objets internes.

Les valeurs des objets internes changeront toujours, donc vous ne pouvez pas coder en dur leurs clés et itérer à travers celles-ci pour obtenir les valeurs appropriées.

## Solutions possibles

Il peut être difficile de travailler directement avec des réponses d'API complexes, alors prenons du recul et simplifions :

```jsx
const visit = (obj, fn) => {
    const values = Object.values(obj)

    values.forEach(val => 
        val && typeof val === "object" ? visit(val, fn) : fn(val))
}

// Test rapide
const print = (val) => console.log(val)

const person = {
    name: {
        first: "John",
        last: "Doe"
    },
    age: 15,
    secret: {
        secret2: {
            secret3: {
                val: "I ate your cookie"
            }
        }
    }
}

visit(person, print)
/* Sortie
John
Doe
15
I ate your cookie
*/
```

La bibliothèque `lodash` dispose de méthodes simples pour accomplir la même chose, mais voici une manière rapide et simple de faire la même chose en JavaScript vanilla.

Mais disons que vous voulez simplifier davantage, quelque chose comme :

```jsx
render() {
    // Affiche les données
    console.log(this.state.myPosts);

    const data = this.state.myPosts;

    // Stocke l'objet imbriqué que je veux accéder dans la variable posts
    const posts = data.content;

    // Affiche avec succès l'objet imbriqué que je veux accéder
    console.log(posts);

    // Erreur, cela ne me permettra pas de passer la variable posts à Object.keys
    const display = Object.keys(posts).map(key =>
      <option value={key}>{posts[key]}</option>
    )


    return(
      <div>
        {display}
      </div>
    );
 }
```

Mais vous obtenez une erreur, `TypeError: can't convert undefined to object error` chaque fois que vous essayez de passer `posts` à `Object.keys`.

Gardez à l'esprit que cette erreur n'a rien à voir avec React. Il est illégal de passer un objet en tant qu'enfant d'un composant.

`Object.keys()` ne retourne que les clés de l'objet qui est passé en paramètre. Vous devrez l'appeler plusieurs fois pour itérer à travers toutes les clés imbriquées.

Si vous devez afficher l'objet imbriqué entier, une option consiste à utiliser une fonction pour convertir chaque objet en un composant React et le passer sous forme de tableau :

```jsx
let data= []

visit(obj, (val) => {
    data.push(<p>{val}</p>)  // enveloppe tout type non-objet dans <p>
})
...
return <SomeComponent> {data} </SomeComponent>
```

## Paquets utiles

Une autre option consiste à utiliser un paquet comme [json-query](https://www.npmjs.com/package/json-query) pour aider à itérer à travers les données JSON imbriquées.

Voici une version modifiée de la fonction `render` ci-dessus utilisant `json-query` :

```jsx
 render() {
   const utopian = Object.keys(this.state.utopianCash);
   console.log(this.state.utopianCash);

   var author = jsonQuery('[*][author]', { data: this.state.utopianCash }).value
   var title = jsonQuery('[*][title]', { data: this.state.utopianCash }).value
   var payout = jsonQuery('[*][total_payout_value]', { data: this.state.utopianCash }).value
   var postLink = jsonQuery('[*][url]', { data: this.state.utopianCash }).value
   var pendingPayout = jsonQuery('[*][pending_payout_value]', { data: this.state.utopianCash }).value
   var netVotes = jsonQuery('[*][net_votes]', { data: this.state.utopianCash }).value


   let display = utopian.map((post, i) => {
     return (
       <div className="utopian-items">
        <p>
          <strong>Auteur : </strong>
          {author[i]}
        </p>
        <p>
          <strong>Titre : </strong>
            <a href={`https://www.steemit.com` + postLink[i]}>{title[i]}</a>
        </p>
        <p>
          <strong>Paiement en attente : </strong>
            {pendingPayout[i]}
        </p>
        <p>
          <strong>Votes : </strong>
          {netVotes[i]}
        </p>
       </div>
     );
   });

    return (
      <div className="utopian-container">
        {display}
        <User />
      </div>
    );
  }
}