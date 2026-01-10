---
title: Comment créer une liste de tâches avec React Hooks
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-19T16:43:20.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-todo-list-with-react-hooks-ebaa4e3db3b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*mKtppOPghvXQKu0jte2B_g.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment créer une liste de tâches avec React Hooks
seo_desc: 'By Yazeed Bzadough

  React v16.7.0-alpha introduced Hooks, and I’m excited.

  What Are Hooks?

  They’re functions that give you React features like state and lifecycle hooks without
  ES6 classes.

  Some benefits are


  Isolating stateful logic, making it easier...'
---

Par Yazeed Bzadough

React v16.7.0-alpha a introduit les [Hooks](https://reactjs.org/docs/hooks-intro.html), et je suis excité.

### Qu'est-ce que les Hooks ?

Ce sont des fonctions qui vous donnent des fonctionnalités React comme l'état et les hooks de cycle de vie sans classes ES6.

Certains avantages sont

- Isoler la logique d'état, ce qui facilite les tests.
- Partager la logique d'état sans props de rendu ou composants d'ordre supérieur.
- Séparer les préoccupations de votre application en fonction de la logique, et non des hooks de cycle de vie.
- Éviter les classes ES6, car elles sont capricieuses, _ne sont pas réellement des classes,_ et posent problème même pour les développeurs JavaScript expérimentés.

Pour plus de détails, voir [l'introduction officielle aux Hooks de React](https://reactjs.org/docs/hooks-intro.html).

#### Adopter les Hooks progressivement

Au moment de la rédaction, les Hooks étaient en version alpha, et leur API pouvait changer à tout moment.

React 16.8.0 était la première version stable à supporter les Hooks, et il y a de plus en plus de tutoriels et d'exemples de code chaque jour. Cependant, comme il n'y a pas de plans pour supprimer les classes de React et que les Hooks fonctionneront avec le code existant, l'équipe React recommande d'éviter les "grandes réécritures". Au lieu de cela, ils suggèrent de pratiquer les Hooks dans des composants non critiques d'abord, puis de les utiliser à la place des classes à l'avenir.

### Construisons une liste de tâches

![](https://cdn-media-1.freecodecamp.org/images/1*zRNbgEedt8wchJNrZ1NuHg.gif)

Les listes de tâches sont l'exemple le plus utilisé pour une bonne raison — elles sont fantastiques pour la pratique. Je recommande cela pour tout langage ou bibliothèque que vous souhaitez essayer.

La nôtre ne fera que quelques choses

- Afficher les tâches dans un style Material Design
- Permettre l'ajout de tâches via une entrée
- Supprimer les tâches

### Installation

Voici les liens [GitHub](https://github.com/yazeedb/react-hooks-todo) et [CodeSandbox](https://codesandbox.io/s/github/yazeedb/react-hooks-todo).

```
git clone https://github.com/yazeedb/react-hooks-todo
cd react-hooks-todo
npm install
```

La branche `master` contient le projet terminé, donc vérifiez la branche `start` si vous souhaitez suivre.

`git checkout start`

Et exécutez le projet.

`npm start`

L'application devrait fonctionner sur `localhost:3000`, et voici notre interface utilisateur initiale.

![](https://cdn-media-1.freecodecamp.org/images/1*ohwA9I861XXghIFAL2Kpcw.png)

Elle est déjà configurée avec [material-ui](http://material-ui.com/) pour donner à notre page un look professionnel. Commençons à ajouter quelques fonctionnalités !

### Le composant TodoForm

Ajoutez un nouveau fichier, `src/TodoForm.js`. Voici le code de départ.

```jsx
import React from 'react';
import TextField from '@material-ui/core/TextField';

const TodoForm = ({ saveTodo }) => {
  return (
    <form>
      <TextField variant="outlined" placeholder="Ajouter une tâche" margin="normal" />
    </form>
  );
};

export default TodoForm;
```

Étant donné le nom, nous savons que son travail est d'ajouter des tâches à notre état. À ce propos, **voici notre premier hook**.

### useState

Regardez ce code

```js
import { useState } from 'react';

const [value, setValue] = useState('');
```

`useState` est simplement une fonction qui prend l'état initial et retourne un tableau. Allez-y et `console.log` le.

Le premier index du tableau est la valeur actuelle de votre état, et le deuxième index est une fonction de mise à jour.

Nous les avons donc nommés de manière appropriée `value` et `setValue` en utilisant [l'affectation par déstructuration ES6](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment).

### useState avec les formulaires

Notre formulaire doit suivre la valeur de l'entrée et appeler `saveTodo` lors de la soumission. `useState` peut nous aider avec cela !

Mettez à jour `TodoForm.js`, le nouveau code est en **gras**.

```jsx
import React, { useState } from 'react';
import TextField from '@material-ui/core/TextField';

const TodoForm = ({ saveTodo }) => {
  const [value, setValue] = useState('');

  return (
    <form
      onSubmit={(event) => {
        event.preventDefault();
        saveTodo(value);
      }}
    >
      <TextField
        variant="outlined"
        placeholder="Ajouter une tâche"
        margin="normal"
        onChange={(event) => {
          setValue(event.target.value);
        }}
        value={value}
      />
    </form>
  );
};

export default TodoForm;
```

De retour dans `index.js`, importez et utilisez ce composant.

```jsx
// ...

import TodoForm from './TodoForm';

// ...

const App = () => {
  return (
    <div className="App">
      <Typography component="h1" variant="h2">
        Tâches
      </Typography>

      <TodoForm saveTodo={console.warn} />
    </div>
  );
};
```

Maintenant, votre valeur est enregistrée lors de la soumission (appuyez sur entrer).

![](https://cdn-media-1.freecodecamp.org/images/1*R3Bf_6tAIC9nGyBSoW48Tg.png)

### useState avec les tâches

Nous avons également besoin d'un état pour nos tâches. Importez `useState` dans `index.js`. Notre état initial doit être un tableau vide.

```jsx
import React, { useState } from 'react';

// ...

const App = () => {
  const [todos, setTodos] = useState([]);

  // ...
};
```

### Composant TodoList

Créez un nouveau fichier appelé `src/TodoList.js`.

Modification : Merci à [Takahiro Hata](https://medium.com/@takahirohata) de m'avoir aidé à déplacer `onClick` au bon endroit !

```jsx
import React from 'react';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemSecondaryAction from '@material-ui/core/ListItemSecondaryAction';
import ListItemText from '@material-ui/core/ListItemText';
import Checkbox from '@material-ui/core/Checkbox';
import IconButton from '@material-ui/core/IconButton';
import DeleteIcon from '@material-ui/icons/Delete';

const TodoList = ({ todos, deleteTodo }) => (
  <List>
    {todos.map((todo, index) => (
      <ListItem key={index.toString()} dense button>
        <Checkbox tabIndex={-1} disableRipple />
        <ListItemText primary={todo} />
        <ListItemSecondaryAction>
          <IconButton
            aria-label="Supprimer"
            onClick={() => {
              deleteTodo(index);
            }}
          >
            <DeleteIcon />
          </IconButton>
        </ListItemSecondaryAction>
      </ListItem>
    ))}
  </List>
);

export default TodoList;
```

Il prend deux props

- `todos` : Le tableau des tâches. Nous parcourons chaque tâche et créons un élément de liste.
- `deleteTodo` : Cliquer sur le `IconButton` d'une tâche déclenche cette fonction. Il passe l'`index`, qui identifiera de manière unique une tâche dans notre liste.

Importez ce composant dans votre `index.js`.

```jsx
import TodoList from './TodoList';
import './styles.css';

const App = () => {
  //...
};
```

Et utilisez-le dans votre fonction `App` comme ceci

```jsx
<TodoForm saveTodo={console.warn} />
<TodoList todos={todos} />
```

### Ajout de tâches

Toujours dans `index.js`, modifions notre prop `saveTodo` de `TodoForm`.

```jsx
<TodoForm
  saveTodo={(todoText) => {
    const trimmedText = todoText.trim();

    if (trimmedText.length > 0) {
      setTodos([...todos, trimmedText]);
    }
  }}
/>
```

Fusionnez simplement les tâches existantes avec notre nouvelle tâche, en supprimant les espaces supplémentaires.

Nous pouvons maintenant ajouter des tâches !

![](https://cdn-media-1.freecodecamp.org/images/1*3fiAjGTZh6umusulyIqbkg.gif)

### Effacer l'entrée

Remarquez que l'entrée ne se vide pas après l'ajout d'une nouvelle tâche. Ce n'est pas une bonne expérience utilisateur !

Nous pouvons le corriger avec un petit changement de code dans `TodoForm.js`.

```jsx
<form
  onSubmit={(event) => {
    event.preventDefault();

    saveTodo(value);

    setValue('');
  }}
/>
```

Une fois qu'une tâche est enregistrée, définissez l'état du formulaire sur une chaîne vide.

Cela a l'air bien maintenant !

![](https://cdn-media-1.freecodecamp.org/images/1*N9EeEN3ZG12VubC10OT-9A.gif)

### Suppression de tâches

`TodoList` fournit l'`index` de chaque tâche, car c'est un moyen garanti de trouver celle que nous voulons supprimer.

`TodoList.js`

```jsx
<IconButton
  aria-label="Supprimer"
  onClick={() => {
    deleteTodo(index);
  }}
>
  <DeleteIcon />
</IconButton>
```

Nous allons en profiter dans `index.js`.

```jsx
<TodoList
  todos={todos}
  deleteTodo={(todoIndex) => {
    const newTodos = todos.filter((_, index) => index !== todoIndex);

    setTodos(newTodos);
  }}
/>
```

Toutes les tâches qui ne correspondent pas à l'`index` fourni sont conservées et stockées dans l'état en utilisant `setTodos`.

La fonctionnalité de suppression est complète !

![](https://cdn-media-1.freecodecamp.org/images/1*i7WsUbuF0pI2HS0b6ddZ8Q.gif)

### Abstraction de l'état des tâches avec useState

J'ai mentionné que les Hooks sont excellents pour séparer la logique d'état et la logique des composants. Voici à quoi cela pourrait ressembler dans notre application de tâches.

Créez un nouveau fichier appelé `src/useTodoState.js`.

```js
import { useState } from 'react';

export default (initialValue) => {
  const [todos, setTodos] = useState(initialValue);

  return {
    todos,
    addTodo: (todoText) => {
      setTodos([...todos, todoText]);
    },
    deleteTodo: (todoIndex) => {
      const newTodos = todos.filter((_, index) => index !== todoIndex);

      setTodos(newTodos);
    }
  };
};
```

C'est notre même code de `index.js`, mais séparé ! Notre gestion d'état n'est plus étroitement couplée au composant.

Maintenant, importez-le simplement.

```jsx
import React from 'react';
import ReactDOM from 'react-dom';
import Typography from '@material-ui/core/Typography';
import TodoForm from './TodoForm';
import TodoList from './TodoList';
import useTodoState from './useTodoState';
import './styles.css';

const App = () => {
  const { todos, addTodo, deleteTodo } = useTodoState([]);

  return (
    <div className="App">
      <Typography component="h1" variant="h2">
        Tâches
      </Typography>

      <TodoForm
        saveTodo={(todoText) => {
          const trimmedText = todoText.trim();

          if (trimmedText.length > 0) {
            addTodo(trimmedText);
          }
        }}
      />

      <TodoList todos={todos} deleteTodo={deleteTodo} />
    </div>
  );
};

const rootElement = document.getElementById('root');
ReactDOM.render(<App />, rootElement);
```

Et tout fonctionne toujours normalement.

![](https://cdn-media-1.freecodecamp.org/images/1*i7WsUbuF0pI2HS0b6ddZ8Q.gif)

### Abstraction de l'état de l'entrée du formulaire avec useState

Nous pouvons faire de même avec notre formulaire !

Créez un nouveau fichier, `src/useInputState.js`.

```js
import { useState } from 'react';

export default (initialValue) => {
  const [value, setValue] = useState(initialValue);

  return {
    value,
    onChange: (event) => {
      setValue(event.target.value);
    },
    reset: () => setValue('')
  };
};
```

Et maintenant `TodoForm.js` devrait ressembler à ceci.

```jsx
import React from 'react';
import TextField from '@material-ui/core/TextField';
import useInputState from './useInputState';

const TodoForm = ({ saveTodo }) => {
  const { value, reset, onChange } = useInputState('');

  return (
    <form
      onSubmit={(event) => {
        event.preventDefault();

        saveTodo(value);
        reset();
      }}
    >
      <TextField
        variant="outlined"
        placeholder="Ajouter une tâche"
        margin="normal"
        onChange={onChange}
        value={value}
      />
    </form>
  );
};

export default TodoForm;
```

Et nous avons terminé ! J'espère que vous avez apprécié, à la prochaine fois !