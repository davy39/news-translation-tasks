---
title: Comment utiliser le Hook useState() dans React – Expliqué avec des exemples
  de code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-08T14:11:06.000Z'
originalURL: https://freecodecamp.org/news/usestate-hook-3-different-examples
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/usestate
seo_title: Comment utiliser le Hook useState() dans React – Expliqué avec des exemples
  de code
---

hook-2.jpg
étiquettes:
- name: JavaScript
  slug: javascript
- name: react hooks
  slug: react-hooks
- name: React
  slug: reactjs
seo_title: null
seo_desc: 'Par Mwendwa Bundi Emma

  L'un des hooks React les plus connus est le hook useState(). Il vous permet d'ajouter une
  variable d'état à votre composant. Le hook useState() peut contenir commodément des chaînes de caractères,
  des tableaux, des nombres, des objets et bien plus encore.

  Dans cet article, nous allons...'
---

Par Mwendwa Bundi Emma

L'un des hooks React les plus connus est le hook `useState()`. Il vous permet d'ajouter une variable d'état à votre composant. Le hook `useState()` peut contenir commodément des chaînes de caractères, des tableaux, des nombres, des objets et bien plus encore.

Dans cet article, nous allons apprendre à connaître le hook `useState()` et démontrer son utilisation avec trois exemples différents : un bouton avec rendu conditionnel, la gestion de formulaires et le célèbre compteur.

## Prérequis

* Vous aurez besoin de connaissances de base en HTML, CSS et JavaScript pour comprendre les idées derrière ce que vous créez dans ce tutoriel. 
* Il est également utile d'avoir des connaissances de base en React.
* Enfin, vous aurez besoin d'un IDE, de préférence [VS Code](https://code.visualstudio.com/).

Une fois que votre application React est opérationnelle, vous êtes prêt à utiliser useState. Pour commencer, vous devez importer `useState()` depuis React comme montré ci-dessous :

```js
import { useState } from 'react';
```

## Comment fonctionne `useState()` ?

Le hook `useState()` fonctionne en gérant et en manipulant l'état dans vos applications. 

Le hook `useState()` prend la première valeur (initiale) de la variable d'état comme argument. La deuxième valeur définit alors votre état, c'est pourquoi elle est toujours initiée comme `setState`. Alors, comment cela fonctionne-t-il ?

```js
const [state, setState] = useState(valeur initiale ici)

const [calories, setCalories] = useState(valeur initiale des calories)
```

Dans le cas du premier rendu, il retourne l'état initial et se met à jour avec une valeur différente lors du re-rendu en utilisant la fonction `set`.

## Rendu conditionnel avec le Hook `useState()`

Cet exemple vous permet de mettre à jour l'état en fonction de deux conditions : si l'utilisateur est connecté ou non. Cela explique également pourquoi l'état initial est défini sur false, pour signifier que l'utilisateur n'est pas connecté.

Vous allez créer un bouton de connexion qui utilise le hook `useState()` pour rendre deux résultats différents. 

L'un est un bouton de connexion avec un message demandant à l'utilisateur de se connecter. L'autre est un bouton qui, une fois que l'utilisateur est connecté, lui donne le choix de se déconnecter.

```react
import React from 'react'

const Signin = () => {
  return (
    <div>
        <div>
            <button type="button">Se déconnecter</button>
            <p>Bienvenue, content de vous voir ici<p>
        </div>
        <div>
            <button type="button">Se connecter</button>
            <p>Veuillez vous connecter</p>
        </div>
    </div>
  )
}

export default Signin;
```

Pour implémenter les fonctionnalités de connexion et de déconnexion, vous devrez importer `useState()`. Ensuite, vous devrez utiliser le rendu conditionnel pour spécifier comment les boutons répondront à un clic.

```react
import React, { useState } from 'react'

const Signin = () => {
    const [signedin, setSignedin] = useState(false)

    const handleSignin = () => {
        setSignedin(true)
    }

    const handleSignout = () => {
        setSignedin(false)
    }
  return (
         <div>
           { signedin ? ( 
        <div>
            <button type="button" onClick={handleSignout}>Se déconnecter</button>
            <p>Bienvenue, content de vous voir ici</p>
        </div>) :
        
        (<div>
            <button type="button" onClick={handleSignin}>Se connecter</button>
            <p>Veuillez vous connecter</p>
        </div>)
           }
        </div>
  )
}

export default Signin;
```

Que se passe-t-il dans le code ci-dessus ?

Tout d'abord, vous avez créé une variable avec le hook `useState()` qui définit `signedin` sur false. Pourquoi ? Parce que lors du premier chargement, vous ne voulez pas que l'utilisateur soit connecté. Mais une fois qu'ils cliquent sur le bouton de connexion, ils peuvent 'entrer'.

De plus, notez que vous avez importé le hook `useState()` en haut.

Vous avez ensuite créé des variables qui gèrent la connexion, la déconnexion et définissent la fonction `set` sur `true` et `false`, respectivement – c'est-à-dire `handleSignin` et `handleSignout`.

Après cela, vous avez créé un gestionnaire `onClick` qui écoute un clic sur le bouton et déclenche une action. Cette action est dirigée par l'opérateur conditionnel (ternaire).

Alors, comment fonctionne l'opérateur ternaire ? Voici [ce que MDN en dit](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator) :

> "L'**opérateur conditionnel (ternaire)** est le seul opérateur JavaScript qui prend trois opérandes : une condition suivie d'un point d'interrogation (`?`), puis une expression à exécuter si la condition est [truthy](https://developer.mozilla.org/en-US/docs/Glossary/Truthy) suivie de deux points (`:`), et enfin l'expression à exécuter si la condition est [falsy](https://developer.mozilla.org/en-US/docs/Glossary/Falsy).   
>   
> Cet opérateur est fréquemment utilisé comme alternative à une instruction [`if...else`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else)."

Cela signifie que si vous cliquez sur le bouton de connexion, vous êtes accueilli et recevez le message de bienvenue. Une fois que vous cliquez sur le bouton de déconnexion, vous êtes invité à vous connecter, avec le message 'veuillez vous connecter'.

## Comment utiliser le Hook `useState()` dans une application de compteur React

Cet exemple vous aidera à montrer comment vous pouvez utiliser `useState()` pour mettre à jour votre état via des clics.

L'idée derrière ce simple compteur est que vos clics sont comptés. Donc, si vous cliquez sur le bouton 12 fois, le compteur se met à jour à 12. Notez que le bouton se met à jour à chaque clic/comptage.

```react
import React from 'react';


const Newcounter = () => {
    return (
        <div>
            <button type="button">Vous verrez le compte ici</button>
        </div>
    )
}


export default Newcounter;

```

Pour rendre le compteur fonctionnel, vous devez utiliser le hook comme montré ci-dessous (et encore une fois, n'oubliez pas d'importer `useState()` avant de l'utiliser) :

```react
const [count, setCount] = useState(0) 
```

Vous allez ensuite créer une autre variable qui incrémente les comptes de 0 à 1, 2, 3....

```react
const incrementCount = () => { setCount (count + 1) }
```

Vous pouvez maintenant retourner le compte incrémenté en utilisant le gestionnaire `onClick` comme montré ci-dessous :

```react
import React, { useState } from 'react';


const Newcounter = () => {
    const [count, setCount] = useState(0)

    const incrementCount = () => {
        setCount(count + 1)
    
    }
    return (
        <div>
            <button type="button" onClick={incrementCount}>Vous avez cliqué  
            {count} fois</button>
        </div>
    )
}


export default Newcounter;

```

## Comment utiliser le Hook `useState()` dans un formulaire dans React

Les formulaires utilisent `useState()` en permettant au développeur de définir un état vide qui utilise la fonction `set` pour gérer ce que l'utilisateur tape comme entrée. 

Ici, vous voulez essentiellement collecter le nom et l'email des utilisateurs via un formulaire, puis soumettre les informations.

Ci-dessous se trouve un formulaire simple pour démontrer comment le hook `useState()` rend cela possible.

Voici le formulaire avec lequel vous allez travailler :

```react
import React from 'react'

const Theform
 = () => {
  return (
    <div>
        <form>
            <input type="text" placeholder="entrez votre nom" required />
            <input type="email" placeholder="entrez votre email" required />
            <button type="submit">Soumettre</button>
        </form>

    </div>
  )
}

export default Theform;

```

Vous devrez importer le hook dans votre fichier. Après cela, utilisez le hook `useState` pour définir le nom et l'email à null en attendant que l'utilisateur saisisse ses détails.

Ensuite, vous allez créer une fonction fléchée avec `handleSubmit` qui exécute la méthode `preventDefault()`. `console.log` le nom de l'utilisateur et son email afin que vous puissiez obtenir ces détails en utilisant le gestionnaire d'événements `onSubmit()`.

Une fois cela fait, vous pouvez alors utiliser la fonction `set` pour le nom et l'email afin de cibler un changement dans l'entrée et obtenir la valeur de l'entrée que vous avez initialisée comme `user` et `email` dans votre hook `useState()`.

N'oubliez pas que le hook `useState` utilise cette fonction `set` pour le re-rendu. Dans ce cas, vous re-rendez les nouvelles valeurs que l'utilisateur a ajoutées dans le formulaire. C'est pourquoi vous définissez la valeur dans votre entrée comme `value={user}`.

```react
import React, { useState } from 'react'

const Theform
 = () => {

  const [user, setUser] = useState('')
  const [email, setEmail] = useState('')

  const handleSubmit = (e) => {
    e.preventDefault()
    console.log(user, email)

  }
  return (
    <div>
        <form onSubmit={handleSubmit}>
            <input type="text" placeholder="entrez votre nom"  onChange={(e) 
            => {setUser(e.target.value)}} value={user} required />
                
            <input type="email" placeholder="entrez votre email" onChange={(e)  
            => {setEmail(e.target.value)}} value={email} required />
            <button type="submit">Soumettre</button>
            
        </form>

    </div>
  )
}

export default Theform;

```

## Conclusion

Dans cet article, vous avez appris à connaître le hook `useState()` dans React en considérant trois exemples différents. N'oubliez pas, tout comme tous les autres hooks React, le hook useState() respecte les règles générales des hooks React.