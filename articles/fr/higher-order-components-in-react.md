---
title: Comment utiliser les composants d'ordre supérieur dans React
subtitle: ''
author: valentine Gatwiri
co_authors: []
series: null
date: '2023-07-28T17:40:06.000Z'
originalURL: https://freecodecamp.org/news/higher-order-components-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-from-2023-07-26-11-39-58.png
tags:
- name: React
  slug: react
seo_title: Comment utiliser les composants d'ordre supérieur dans React
seo_desc: "Higher-order components (HOCs) are a powerful feature of the React library.\
  \ They allow you to reuse component logic across multiple components. \nIn React,\
  \ a higher-order component is a function that takes a component as an argument and\
  \ returns a new ..."
---

Les composants d'ordre supérieur (HOC) sont une fonctionnalité puissante de la bibliothèque React. Ils permettent de réutiliser la logique des composants dans plusieurs composants. 

Dans React, un composant d'ordre supérieur est une fonction qui prend un composant comme argument et retourne un nouveau composant qui enveloppe le composant original.

Les HOC permettent d'ajouter des fonctionnalités supplémentaires à un composant sans modifier le code du composant. Par exemple, vous pouvez utiliser un HOC pour ajouter des capacités d'authentification ou de routage à un composant ou pour appliquer un style ou un comportement spécifique à plusieurs composants.

Les HOC peuvent prendre des arguments supplémentaires, ce qui permet de personnaliser le comportement du HOC. Cela les rend flexibles et réutilisables pour ajouter des fonctionnalités à vos composants.

## Avantages de l'utilisation des composants d'ordre supérieur dans React

1. Réutilisabilité : Les HOC permettent de réutiliser la logique des composants dans plusieurs composants, ce qui peut faire gagner du temps et réduire la duplication de code.
2. Flexibilité : Les HOC peuvent prendre des arguments supplémentaires, ce qui permet de personnaliser le comportement du HOC. Cela en fait un moyen flexible d'ajouter des fonctionnalités à vos composants.
3. Séparation des préoccupations : Les HOC peuvent aider à séparer les préoccupations dans votre code en encapsulant certaines fonctionnalités dans un composant séparé. Cela peut rendre le code plus facile à lire et à maintenir.
4. Composition : Les HOC peuvent être composés ensemble pour créer des fonctionnalités plus complexes. Cela permet de construire des fonctionnalités à partir de petits morceaux réutilisables.
5. Les composants d'ordre supérieur peuvent être utilisés pour implémenter des préoccupations transversales dans votre application telles que l'authentification, la gestion des erreurs, la journalisation, le suivi des performances et bien d'autres fonctionnalités.

## Structure des composants d'ordre supérieur

Pour définir un composant d'ordre supérieur (HOC) dans React, vous suivrez généralement quelques étapes de base :

Tout d'abord, vous définirez la fonction HOC. Il s'agit d'une fonction qui prend un composant en entrée et retourne un nouveau composant avec des fonctionnalités supplémentaires.

```jsx
const hoc = (WrappedComponent) => {
  // ...
}
```

Ensuite, vous définissez le nouveau composant. Il s'agit d'un composant de classe qui enveloppe le `WrappedComponent` et ajoute des fonctionnalités supplémentaires.

```jsx
class NewComponent extends React.Component {
  // ...
  render() {
    // ...
  }
}
```

Ensuite, vous passez les props au `WrappedComponent`. Dans la méthode `render()` du `NewComponent`, passez toutes les props (y compris les props supplémentaires ajoutées par le HOC) au `WrappedComponent`.

```jsx
render() {
  return <WrappedComponent {...this.props} additionalProp={additionalProp} />
}
```

Enfin, retournez le nouveau composant. La fonction HOC doit retourner le `NewComponent` afin qu'il puisse être utilisé dans l'application.

```jsx
const hoc = (WrappedComponent) => {
  class NewComponent extends React.Component {
    // ...
    render() {

      // ...
    }
  }

  return NewComponent;
}

```

## Quand utiliser les HOC dans votre code React

### Authentification

Supposons que vous avez une application avec diverses routes, dont certaines nécessitent que l'utilisateur soit authentifié avant d'y accéder. 

Au lieu de dupliquer la logique d'authentification dans chaque composant ou route, vous pouvez créer un HOC appelé `withAuth` qui vérifie si l'utilisateur est authentifié et le redirige vers la page de connexion si ce n'est pas le cas. Ensuite, vous pouvez envelopper les composants ou routes spécifiques qui nécessitent une authentification avec ce HOC, réduisant ainsi la duplication et enforçant un comportement d'authentification cohérent.

### Journalisation

Imaginez que vous souhaitez journaliser certaines données chaque fois qu'un ensemble spécifique de composants est monté ou mis à jour. Plutôt que d'ajouter la logique de journalisation à chaque composant, vous pouvez créer un HOC appelé `withLogger` qui gère la fonctionnalité de journalisation. 

En enveloppant les composants pertinents avec `withLogger`, vous pouvez obtenir une journalisation cohérente dans ces composants.

### Styling et Thématiques

Vous pourriez avoir un système de design avec des styles et thèmes réutilisables. Vous pouvez créer un HOC nommé `withTheme` qui fournit les props nécessaires liées au thème à un composant. 

De cette façon, le composant enveloppé peut facilement accéder et appliquer les styles appropriés en fonction du thème fourni.

## Comment utiliser les composants d'ordre supérieur dans React

Pour créer un HOC dans React, nous définissons une fonction qui prend un composant comme argument et retourne un nouveau composant qui enveloppe le composant original. Voici un exemple de HOC simple :

```jsx
import React from 'react';
import ReactDOM from 'react-dom';
const withLoading = (WrappedComponent) => {
  class WithLoading extends React.Component {
    state = {
      isLoading: true,
    };

    componentDidMount() {
      setTimeout(() => {
        this.setState({ isLoading: false });
      }, 2000);
    }

    render() {
      return (
        <WrappedComponent
          {...this.props}
          loading={this.state.isLoading}
        />
      );
    }
  }

  WithLoading.displayName = `withLoading(${WrappedComponent.displayName || WrappedComponent.name})`;

  return WithLoading;
};

const MyComponent = ({ loading }) => (
  <div>
    {loading ? <p>Chargement...</p> : <p>Bonjour, le monde !</p>}
  </div>
);

const MyComponentWithLoading = withLoading(MyComponent);

ReactDOM.render(
  <MyComponentWithLoading />,
  document.getElementById("root")
);
```

Dans cet exemple, le HOC `withLoading` prend un composant `WrappedComponent` en entrée et retourne un nouveau composant `WithLoading` qui ajoute une prop de chargement au `WrappedComponent`. 

Le composant `WithLoading` définit l'état `isLoading` à vrai initialement, puis après 2 secondes, le définit à faux. Le `WrappedComponent` est rendu avec la prop de chargement définie à `this.state.isLoading`.

Le composant `MyComponent` est un composant fonctionnel qui rend soit un message `Chargement...` soit un message `Bonjour, le monde !` en fonction de la valeur de la prop de chargement. 

Le composant `MyComponentWithLoading` est créé en passant `MyComponent` au HOC `withLoading`. Enfin, le composant `MyComponentWithLoading` est rendu en utilisant `ReactDOM.render()`.

## Exemple concret : HOC de journalisation

Construisons une simple application React réelle qui journalise les données lorsque l'utilisateur effectue certaines actions. Nous allons créer une application "Liste de tâches", et chaque fois qu'un utilisateur ajoute ou complète une tâche, nous allons journaliser l'événement dans la console du navigateur.

En supposant que vous avez déjà Node.js et npm installés sur votre système, ouvrez une fenêtre de terminal et exécutez les commandes suivantes :

```bash
npx create-react-app hoc-example
cd hoc-example

```

Créez le HOC `withLogger` dans le dossier `src`, créez un nouveau fichier nommé `withLogger.js`. Copiez le code suivant dans le fichier :

```jsx
import React, { useEffect } from 'react';

const withLogger = (WrappedComponent) => {
  const WithLogger = (props) => {
    useEffect(() => {
      // Journaliser les données lors du montage du composant
      console.log(`Le composant ${WrappedComponent.name} est monté.`);
      return () => {
        // Journaliser les données lors du démontage du composant
        console.log(`Le composant ${WrappedComponent.name} est démonté.`);
      };
    }, []);

    useEffect(() => {
      // Journaliser les données lors de la mise à jour du composant
      console.log(`Le composant ${WrappedComponent.name} est mis à jour.`);
    });

    return <WrappedComponent {...props} />;
  };

  WithLogger.displayName = `withLogger(${WrappedComponent.displayName || WrappedComponent.name})`;
  return WithLogger;
};

export default withLogger;

```

Le code ci-dessus démontre un composant d'ordre supérieur (HOC) appelé `withLogger`. Dans ce cas, le HOC `withLogger` ajoute une fonctionnalité de journalisation au composant qu'il enveloppe.

### Créer les composants de l'application Todo List 

Dans le dossier `src`, créez trois nouveaux fichiers appelés `TodoList.js`, `TodoItem.js` et `TodoForm.js`. Ces fichiers contiendront les composants de l'application Todo List.

Dans `TodoList.js`, ajoutez le code suivant :

```jsx
import React, { useState } from 'react';
import TodoItem from './TodoItem';
import withLogger from './withLogger';
import TodoForm from './TodoForm';

const TodoList = () => {
  const [todos, setTodos] = useState([]);
  const [newTodo, setNewTodo] = useState('');

  const addTodo = () => {
    if (newTodo.trim() !== '') {
      setTodos((prevTodos) => [...prevTodos, newTodo]);
      setNewTodo('');
    }
  };

  const completeTodo = (index) => {
    setTodos((prevTodos) => {
      const updatedTodos = [...prevTodos];
      updatedTodos.splice(index, 1);
      return updatedTodos;
    });
  };

  return (
    <div>
      <h1>Liste de tâches</h1>
      <TodoForm newTodo={newTodo} setNewTodo={setNewTodo} addTodo={addTodo} />
      <ul>
        {todos.map((todo, index) => (
          <TodoItem key={index} todo={todo} onComplete={() => completeTodo(index)} />
        ))}
      </ul>
    </div>
  );
};

export default withLogger(TodoList);
```

Dans le code ci-dessus, nous avons implémenté le composant `TodoList` et utilisé le HOC `withLogger` pour ajouter une fonctionnalité de journalisation. Le composant `TodoList` gère l'état d'une liste de tâches et fournit des fonctions pour ajouter et compléter des tâches.

Dans `TodoItem.js`, ajoutez le code suivant :

```jsx
import React from 'react';

const TodoItem = ({ todo, onComplete }) => {
  return (
    <li>
      {todo}
      <button onClick={onComplete}>Terminer</button>
    </li>
  );
};

export default TodoItem;

```

Le code ci-dessus est un simple composant fonctionnel qui rend un seul élément de tâche avec son bouton "Terminer" correspondant.

Ce composant `TodoItem` est responsable de l'affichage des éléments de tâche individuels et permet à l'utilisateur de les compléter en cliquant sur le bouton "Terminer". Il s'agit d'une partie simple et essentielle de l'application Todo List, et lorsqu'il est utilisé en conjonction avec le composant `TodoList`, il devrait fournir une expérience complète et fonctionnelle de Todo List.

Dans `TodoForm.js`, ajoutez le code suivant :

```jsx
import React from 'react';

const TodoForm = ({ newTodo, setNewTodo, addTodo }) => {
  return (
    <div>
      <input
        type="text"
        value={newTodo}
        onChange={(e) => setNewTodo(e.target.value)}
        placeholder="Entrez une nouvelle tâche"
      />
      <button onClick={addTodo}>Ajouter une tâche</button>
    </div>
  );
};

export default TodoForm;

```

Il s'agit d'un composant fonctionnel responsable de l'affichage du champ de saisie et du bouton "Ajouter une tâche", permettant aux utilisateurs d'ajouter de nouvelles tâches à la liste.

Avec ce composant `TodoForm`, les utilisateurs peuvent saisir un nouvel élément de tâche dans le champ de saisie et cliquer sur le bouton "Ajouter une tâche" pour l'ajouter à la liste gérée par le composant `TodoList`.

### Mettre à jour le composant App pour utiliser `MyComponent`

Ouvrez le fichier `App.js` dans le dossier `src` et remplacez son contenu par le code suivant :

```jsx
import React from 'react';
import TodoList from './TodoList';

function App() {
  return (
    <div>
      <TodoList />
    </div>
  );
}

export default App;

```

Enregistrez tous les fichiers et retournez au terminal. Assurez-vous que vous êtes toujours dans le dossier racine du projet (`hoc-example`). Maintenant, démarrez le serveur de développement en exécutant la commande suivante :

```bash
npm start

```

Cela lancera votre application React :

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-from-2023-07-28-14-34-45.png)

De plus, chaque fois que vous ajoutez ou complétez une tâche, l'application journalisera les événements dans la console du navigateur en utilisant le HOC `withLogger`. Par exemple, la console affichera :

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-from-2023-07-28-14-35-25-1.png)

C'est tout ! Vous avez maintenant implémenté un exemple concret de l'utilisation du composant d'ordre supérieur `withLogger` dans un projet React. Voici le code complet sur [GitHub](https://github.com/gatwirival/React-HOCs-Demo) 

## Conclusion

Dans cet article, nous avons discuté des composants d'ordre supérieur (HOC) dans React et de leurs avantages dans la construction de logiques de composants réutilisables et flexibles. Nous avons également discuté de leur structure et appris comment construire des HOC dans React.

Bonne programmation !