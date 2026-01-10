---
title: Tutoriel sur les Hooks React – useState, useEffect, et comment créer des Hooks
  personnalisés
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2021-10-25T15:39:22.000Z'
originalURL: https://freecodecamp.org/news/introduction-to-react-hooks
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/g199.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
- name: Web Development
  slug: web-development
seo_title: Tutoriel sur les Hooks React – useState, useEffect, et comment créer des
  Hooks personnalisés
seo_desc: "Hooks were first introduced in React 16.8. And they're great because they\
  \ let you use more of React's features – like managing your component's state, or\
  \ performing an after effect when certain changes occur in state(s) without writing\
  \ a class. \nIn t..."
---

Les Hooks ont été introduits pour la première fois dans React 16.8. Et ils sont géniaux car ils vous permettent d'utiliser plus de fonctionnalités de React – comme gérer l'état de votre composant, ou effectuer un effet après que certains changements se produisent dans l'état (ou les états) sans écrire une classe. 

Dans cet article, vous apprendrez comment utiliser les Hooks dans React et comment créer vos propres Hooks personnalisés. Gardez simplement à l'esprit que vous pouvez utiliser les hooks uniquement pour les composants fonctionnels. 

## Qu'est-ce que le Hook useState ?

L'état de votre application est destiné à changer à un moment donné. Cela pourrait être la valeur d'une variable, d'un objet, ou de tout type de données existant dans votre composant.

Pour que les changements soient reflétés dans le DOM, nous devons utiliser un Hook React appelé `useState`. Voici à quoi il ressemble :

```javascript
import { useState } from "react";

function App() {
  const [name, setName] = useState("Ihechikara");
  const changeName = () => {
    setName("Chikara");
  };

  return (
    <div>
      <p>Mon nom est {name}</p>
      <button onClick={changeName}> Cliquez-moi </button>
    </div>
  );
}

export default App;

```

Regardons de plus près ce qui se passe dans le code ci-dessus.

```javascript
import { useState } from "react";
```

Pour pouvoir utiliser ce Hook, vous devez importer le Hook **`useState`** depuis React. Nous utilisons un composant fonctionnel appelé `app`. 

```javascript
const [name, setName] = useState("Ihechikara");
```

Après cela, vous devez créer votre état et lui donner une valeur initiale (ou état initial) qui est "Ihechikara". La variable d'état est appelée `name`, et `setName` est la fonction pour mettre à jour sa valeur. 

Avoir une bonne compréhension de certaines des fonctionnalités ES6 vous aidera à saisir les fonctionnalités de base de React. Ci-dessus, nous avons utilisé l'affectation par décomposition pour assigner une valeur de nom initiale à l'état dans `useState("Ihechikara")`. 

```javascript
return (
    <div>
      <p>Mon nom est {name}</p>
      <button onClick={changeName}> Cliquez-moi </button>
    </div>
  );
}

```

Ensuite, le DOM contient un paragraphe avec la variable name et un bouton qui déclenche une fonction lorsqu'il est cliqué. La fonction `changeName()` appelle la fonction `setName()` qui change ensuite la valeur de la variable name en la valeur passée à la fonction `setName()`. 

Les valeurs de votre état ne doivent pas être codées en dur. Dans la section suivante, vous verrez comment utiliser le Hook `useState` dans les formulaires. 

Pour les débutants en React, notez que vous créez vos fonctions et variables avant l'instruction return.

## Comment utiliser le Hook useState dans les formulaires

Cette section vous aidera à comprendre comment créer des valeurs d'état pour vos formulaires et les mettre à jour lorsque vous en avez besoin. Le processus n'est pas si différent de ce que nous avons vu dans la section précédente. 

Comme toujours, importez le Hook `useState` : 

```javascript
import { useState } from "react";

```

Nous allons créer l'état initial comme nous l'avons fait auparavant. Mais dans ce cas, ce sera une chaîne vide puisque nous traitons avec la valeur d'un élément d'entrée. Coder en dur la valeur signifie que l'entrée aura cette valeur chaque fois que la page est rechargée. C'est-à-dire :

```javascript
  const [name, setName] = useState("");

```

Maintenant que nous avons créé l'état, créons l'élément d'entrée dans le DOM et assignons la variable name comme sa valeur initiale. Voici à quoi cela ressemble :

```javascript
return (
    <div>
      <form>
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          placeholder="Votre Nom"
        />
        <p>{name}</p>
      </form>
    </div>
  );
```

Vous remarquerez que nous n'avons pas créé de fonction au-dessus de l'instruction return pour mettre à jour la valeur de l'état – mais il est toujours correct si vous décidez d'utiliser cette méthode.

Ici, nous utilisons l'écouteur d'événement `onChange` qui attend tout changement de valeur dans le champ de saisie. Chaque fois qu'il y a un changement, une fonction anonyme (qui prend l'objet événement comme paramètre) est déclenchée, ce qui à son tour appelle la fonction `setName()` pour mettre à jour la variable name avec la valeur actuelle du champ de saisie.

Voici à quoi ressemble le code final :

```javascript
import { useState } from "react";

function App() {
  const [name, setName] = useState("");

  return (
    <div>
      <form>
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          placeholder="Votre Nom"
        />
        <p>{name}</p>
      </form>
    </div>
  );
}

export default App;

```

## Qu'est-ce que le Hook useEffect ?

Le Hook Effect, comme son nom l'indique, exécute un effet chaque fois qu'il y a un changement d'état. Par défaut, il s'exécute après le premier rendu et chaque fois que l'état est mis à jour. 

Dans l'exemple ci-dessous, nous créons une variable d'état `count` avec une valeur initiale de zéro. Un bouton dans le DOM augmentera la valeur de cette variable de un chaque fois qu'il est cliqué. Le Hook useEffect s'exécutera chaque fois que la variable `count` changera et enregistrera certaines informations dans la console. 

```javascript
import { useState, useEffect } from "react";

function App() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    console.log(`Vous avez cliqué sur le bouton ${count} fois`)
  });

  return (
    <div>
      <button onClick={() => setCount(count + 1)}>Cliquez-moi</button>
    </div>
  );
}

export default App;

```

La première ligne de code où vous importez le(s) Hook(s) requis est toujours importante si vous allez "accrocher" cette fonctionnalité React. Nous avons importé les deux Hooks que nous avons utilisés ci-dessus : 

```javascript
import React, { useState, useEffect } from "react";

```

Notez que vous pouvez utiliser le Hook useEffect pour réaliser divers effets comme récupérer des données depuis une API externe (que vous verrez dans une autre section de cet article), changer le DOM dans votre composant, et ainsi de suite.

### Dépendances de useEffect

Mais que se passe-t-il si vous voulez que votre effet ne s'exécute qu'après le premier rendu, ou si vous avez plusieurs états et que vous voulez qu'un effet après soit attaché à l'un des états ? 

Nous pouvons faire cela en utilisant un tableau de dépendances qui est passé en tant que second argument dans le Hook `useEffect`. 

#### Comment exécuter un effet une seule fois

Pour le premier exemple, nous allons passer un tableau qui permet au Hook useEffect de ne s'exécuter qu'une seule fois. Voici un exemple de comment cela fonctionne :

```javascript
import { useState, useEffect } from "react";

function App() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    console.log(`Vous avez cliqué sur le bouton ${count} fois`)
  }, []);

  return (
    <div>
      <button onClick={() => setCount(count + 1)}>Cliquez-moi</button>
    </div>
  );
}

export default App;

```

Le code ci-dessus est le même que dans la section précédente, sauf que le Hook useEffect accepte un tableau vide `[]` comme second argument. Lorsque nous laissons le tableau vide, l'effet ne s'exécutera qu'une seule fois indépendamment des changements de l'état auquel il est attaché. 

#### Comment attacher un effet à un état particulier

```javascript
import { useState, useEffect } from "react";

function App() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    console.log(`Vous avez cliqué sur le premier bouton ${count} fois`);
  }, [count]);

  const [count2, setCount2] = useState(0);

  useEffect(() => {
    console.log(`Vous avez cliqué sur le second bouton ${count2} fois`)
  }, [count2]);

  return (
    <div>
      <button onClick={() => setCount(count + 1)}>Cliquez-moi</button>
      <button onClick={() => setCount2(count2 + 1)}>Cliquez-moi</button>
    </div>
  );
}

export default App;

```

Dans le code ci-dessus, nous avons créé deux états et deux Hooks useEffect. Chaque état a un effet après attaché à lui en passant le nom de l'état `[count]` et `[count2]` au tableau de dépendances correspondant de useEffect. 

Ainsi, lorsque l'état de `count` change, le Hook useEffect responsable de la surveillance de ces changements exécutera tout effet après qui lui est assigné. Il en va de même pour `count2`.

## Comment créer vos propres Hooks

Maintenant que vous avez vu certains des Hooks intégrés dans React (consultez la [documentation](https://reactjs.org/docs/hooks-reference.html) pour voir plus de Hooks), il est temps de créer notre propre Hook personnalisé. 

Il y a beaucoup de possibilités pour ce que votre Hook peut faire. Dans cette section, nous allons créer un Hook qui récupère des données depuis une API externe et sortie les données vers le DOM. Cela vous évite le stress de recréer la même logique encore et encore dans différents composants. 

### Étape 1 – Créez votre fichier

Lors de la création d'un nouveau fichier pour un Hook personnalisé, assurez-vous toujours que le nom du fichier commence par "use". Je vais appeler le mien `useFetchData.js`.

### Étape 2 – Créez les fonctionnalités du Hook

Comme indiqué précédemment, nous utiliserons ce Hook pour récupérer des données depuis des API externes. Il sera dynamique donc rien n'a besoin d'être codé en dur. Voici comment nous allons faire cela :

```javascript
import { useState, useEffect} from 'react'

function useFetchData(url) {
    const [data, setData] = useState(null);

    useEffect(() => {
      fetch(url)
        .then((res) => res.json())
        .then((data) => setData(data))
        .catch((err) => console.log(`Erreur: ${err}`));
    }, [url]);

    return { data };
}

export default useFetchData


```

Pour expliquer ce qui s'est passé ci-dessus :

* Nous importons les Hooks : `import { useState, useEffect} from 'react'`.
* Nous créons un état pour contenir les données qui seront retournées – l'état initial sera null : `const [data, setData] = useState(null);`. Les données retournées mettront à jour la valeur de la variable `data` en utilisant la fonction `setData()`. 
* Nous créons un effet qui s'exécute au premier rendu et chaque fois que le paramètre `url` change : 

```javascript
useEffect(() => {
      fetch(url)
        .then((res) => res.json())
        .then((data) => setData(data))
        .catch((err) => console.log(`Erreur: ${err}`));
    }, [url]);
```

* Nous retournons la variable data : `return { data };`

### Étape 3 – Créez un nouveau fichier et importez le Hook personnalisé

Nous avons donc créé notre Hook personnalisé. Maintenant, créons un nouveau composant et voyons comment nous pouvons utiliser le Hook `useFetchData` dans celui-ci :

```javascript
import useFetchData from './useFetchData'
 
function Users() {
    const { data } = useFetchData("https://api.github.com/users");

  return (
      <div>
          {data && (
            data.map((user) =>(
                <div className="text-white" key={user.id}>
                    <h1> {user.login} </h1>
                    <p> { user.type } </p>
                </div>
            ))
          )}
      </div>
  )
}

export default Users;
```

Décomposons cela :

* Nous avons nommé le composant `Users.js` car il sera utilisé pour récupérer les données utilisateur depuis l'API GitHub (cela peut être n'importe quelle API). 
* Nous avons importé un Hook personnalisé : `import useFetchData from './useFetchData'`.
* Nous avons référencé le Hook avant l'instruction return et passé l'URL : `const { data } = useFetchData("https://api.github.com/users");`. Une requête API sera envoyée à l'URL que vous passez.
* En utilisant l'opérateur `&&`, le DOM ne sera mis à jour que lorsque la variable data aura été mise à jour avec les données de la requête API – c'est-à-dire, lorsque `data != null`.
* Nous avons parcouru les données retournées et les avons sorties vers le DOM.

## Conclusion

Si vous avez suivi jusqu'à ce point, alors vous devriez avoir une bonne compréhension de ce que sont les Hooks dans React, comment les utiliser, et comment créer vos propres Hooks personnalisés. Et la meilleure façon de comprendre pleinement cela est de pratiquer, alors ne vous contentez pas de lire. 

Cet article couvre les domaines principaux des Hooks, mais il ne vous apprendra pas tout ce qu'il y a à savoir sur les Hooks. Assurez-vous donc de consulter la [documentation React JS](https://reactjs.org/docs/hooks-intro.html) afin que vous puissiez en apprendre davantage à leur sujet.

Merci d'avoir lu. Vous pouvez me suivre sur Twitter [@ihechikara2](https://twitter.com/Ihechikara2).