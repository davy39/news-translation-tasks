---
title: Comment créer une application React avec une fonctionnalité Load More en utilisant
  les React Hooks
subtitle: ''
author: Yogesh Chavan
co_authors: []
series: null
date: '2021-04-27T18:12:22.000Z'
originalURL: https://freecodecamp.org/news/build-a-react-application-with-load-more-functionality-react-hooks
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/random_user.jpg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: Comment créer une application React avec une fonctionnalité Load More en
  utilisant les React Hooks
seo_desc: 'In this article, we will build a React application using class components.
  Then we''ll convert it to functional components using React Hooks in a step-by-step
  way.

  By building this app, you will learn:


  How to make API calls

  How to implement load more...'
---

Dans cet article, nous allons construire une application React en utilisant des composants de classe. Ensuite, nous la convertirons en composants fonctionnels en utilisant les React Hooks, étape par étape.

En construisant cette application, vous apprendrez :

* Comment effectuer des appels API
* Comment implémenter une fonctionnalité Load More (charger plus)
* Comment déboguer les problèmes d'application
* Comment utiliser async/await
* Comment mettre à jour le composant lorsque quelque chose change
* Comment résoudre le problème de boucle infinie dans le hook useEffect
* Comment refactoriser des composants basés sur des classes en composants fonctionnels avec des Hooks

et bien plus encore.

Alors, commençons.

> Vous voulez apprendre Redux depuis le début et construire une application de commande de nourriture à partir de zéro ? Consultez mon cours [Mastering Redux](https://master-redux.yogeshchavan.dev/).

## Configuration initiale du projet

Créez un nouveau projet en utilisant `create-react-app` :

```
npx create-react-app class-to-hooks-refactoring
```

Une fois le projet créé, supprimez tous les fichiers du dossier `src` et créez les fichiers `index.js` et `styles.css` à l'intérieur du dossier `src`. Créez également un dossier `components` à l'intérieur du dossier `src`.

Installez la bibliothèque `axios` en exécutant la commande suivante depuis le dossier du projet :

```
yarn add axios@0.21.1

```

Ouvrez le fichier `styles.css` et ajoutez-y le contenu de [ce dépôt GitHub](https://github.com/myogeshchavan97/class-to-hooks-refactoring/blob/master/src/styles.css).

## Comment créer les pages initiales

Créez un nouveau fichier nommé `Header.js` dans le dossier `components` avec le contenu suivant :

```jsx
import React from "react";

const Header = () => {
  return <h1 className="header">Utilisateurs aléatoires</h1>;
};

export default Header;

```

Créez un nouveau fichier nommé `App.js` dans le dossier `src` avec le contenu suivant :

```jsx
import React from 'react';
import Header from './components/Header';

export default class App extends React.Component {
  render() {
    return (
      <div className="main-section">
        <Header />
        <h2>Composant App</h2>
      </div>
    );
  }
}

```

Maintenant, ouvrez le fichier `index.js` et ajoutez-y le contenu suivant :

```js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import './styles.css';

ReactDOM.render(<App />, document.getElementById('root'));

```

Maintenant, démarrez l'application en exécutant la commande `yarn start` depuis le terminal.

Vous verrez l'écran suivant si vous accédez à l'application sur [http://localhost:3000/](http://localhost:3000/).

![Image](https://www.freecodecamp.org/news/content/images/2021/04/index_page.png)

## Comment effectuer un appel API

Nous utiliserons l'API [Random Users](https://randomuser.me/) pour obtenir une liste d'utilisateurs aléatoires.

Ouvrez donc votre fichier `App.js` et ajoutez la méthode `componentDidMount` à l'intérieur du composant :

```js
componentDidMount() {
    axios
      .get('https://randomuser.me/api/?page=0&results=10')
      .then((response) => {
        console.log(response.data);
      })
      .catch((error) => console.log('error', error));
  }

```

Importez également `axios` en haut du fichier :

```js
import axios from 'axios';

```

Votre fichier `App.js` complet ressemblera maintenant à ceci :

```js
import React from 'react';
import Header from './components/Header';
import axios from 'axios';

export default class App extends React.Component {
  componentDidMount() {
    axios
      .get('https://randomuser.me/api/?page=0&results=10')
      .then((response) => {
        console.log(response.data);
      })
      .catch((error) => console.log('error', error));
  }

  render() {
    return (
      <div className="main-section">
        <Header />
        <h2>Composant App</h2>
      </div>
    );
  }
}

```

Ici, nous effectuons un appel API pour obtenir initialement une liste de 10 enregistrements à l'URL `https://randomuser.me/api/?page=0&results=10`.

Maintenant, si vous vérifiez l'application, vous verrez la réponse de l'API dans la console.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/result-1.png)

Maintenant, déclarons un état (state) pour stocker le résultat et les indicateurs liés aux messages de chargement et d'erreur.

Remplacez le contenu de `App.js` par le code suivant :

```js
import React from 'react';
import Header from './components/Header';
import axios from 'axios';

export default class App extends React.Component {
  state = {
    users: [],
    isLoading: false,
    errorMsg: ''
  };

  componentDidMount() {
    this.setState({ isLoading: true });
    axios
      .get('https://randomuser.me/api/?page=0&results=10')
      .then((response) => {
         this.setState({ users: response.data.results, errorMsg: '' });
      })
      .catch((error) =>
        this.setState({
          errorMsg: 'Erreur lors du chargement des données. Réessayez plus tard.'
        })
      )
      .finally(() => {
        this.setState({ isLoading: false });
      });
  }

  render() {
    const { users, isLoading, errorMsg } = this.state;
    console.log(users);

    return (
      <div className="main-section">
        <Header />
        {isLoading && <p className="loading">Chargement...</p>}
        {errorMsg && <p className="errorMsg">{errorMsg}</p>}
      </div>
    );
  }
}

```

Ici, nous avons déclaré un état directement à l'intérieur de la classe en utilisant la [syntaxe des propriétés de classe](https://javascript.plainenglish.io/how-to-write-clean-and-easy-to-understand-react-code-using-class-properties-syntax-5b375b0618d3?source=friends_link&sk=c170992cab9025fddb7b34b8894ea993), qui est une manière courante d'écrire l'état dans les composants basés sur des classes.

```js
state = {
  users: [],
  isLoading: false,
  errorMsg: ''
};

```

Ensuite, à l'intérieur de la méthode `componentDidMount`, nous définissons d'abord l'état `isLoading` sur `true` avant d'effectuer l'appel API.

```js
this.setState({ isLoading: true });

```

Une fois que nous recevons la réponse de l'API, nous stockons le résultat dans le tableau `users` qui est déclaré dans l'état. Nous définissons également l'état `errorMsg` comme vide, afin que les erreurs précédentes soient effacées.

```js
this.setState({ users: response.data.results, errorMsg: '' });

```

Et dans le bloc `.catch`, nous définissons le `errorMsg` au cas où il y aurait une erreur lors de l'appel API.

Ensuite, nous utilisons le bloc `.finally` pour définir l'état `isLoading` sur `false`.

```js
.finally(() => {
  this.setState({ isLoading: false });
});

```

L'utilisation de `finally` nous aide à éviter la duplication de code ici car nous n'avons pas besoin de définir `isLoading` sur `false` à nouveau dans `.then` et dans le bloc `.catch`. C'est parce que le bloc `finally` sera toujours exécuté, qu'il s'agisse d'un succès ou d'un échec.

Et dans la méthode render, nous affichons soit le message d'erreur, soit le message de chargement, ainsi que le tableau `users` de l'état dans la console.

Maintenant, si vous vérifiez l'application, vous verrez les informations des `users` dans la console en cas de succès ou un message d'erreur sur l'interface utilisateur en cas d'échec de l'API.

## Comment afficher les informations des utilisateurs

Maintenant, affichons les informations des `users` à l'écran.

Créez un nouveau fichier `User.js` dans le dossier `components` avec le contenu suivant :

```js
import React from "react";

const User = ({ name, location, email, picture }) => {
  return (
    <div className="random-user">
      <div className="user-image">
        <img src={picture.medium} alt={name.first} />
      </div>
      <div className="user-details">
        <div>
          <strong>Nom :</strong> {name.first} {name.last}
        </div>
        <div>
          <strong>Pays :</strong> {location.country}
        </div>
        <div>
          <strong>E-mail :</strong> {email}
        </div>
      </div>
    </div>
  );
};

export default User;

```

Maintenant, créez un nouveau fichier `UsersList.js` dans le dossier `components` avec le contenu suivant :

```js
import React from 'react';
import User from './User';

const UsersList = ({ users }) => {
  return (
    <div className="user-list">
      {users && users.map((user) => <User key={user.login.uuid} {...user} />)}
    </div>
  );
};

export default UsersList;

```

Maintenant, ouvrez le fichier `App.js` et remplacez la méthode `render` par le code suivant :

```js
render() {
  const { users, isLoading, errorMsg } = this.state;

  return (
    <div className="main-section">
      <Header />
      {isLoading && <p className="loading">Chargement...</p>}
      {errorMsg && <p className="errorMsg">{errorMsg}</p>}
      <UsersList users={users} />
    </div>
  );
}

```

Ici, nous passons le tableau `users` comme une prop au composant `UsersList`. À l'intérieur du composant `UsersList`, nous bouclons sur le tableau et envoyons les informations de l'utilisateur au composant `User` en décomposant toutes les propriétés de chaque `user` individuel avec `{...props}`. Cela finit par afficher les données à l'écran.

Importez également le composant `UsersList` en haut du fichier :

```js
import UsersList from './components/UsersList';

```

Si vous vérifiez l'application maintenant, vous verrez l'écran suivant :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/random_users.gif)

Comme vous pouvez le voir, à chaque rafraîchissement de la page, un nouvel ensemble d'utilisateurs aléatoires s'affiche à l'écran.

## Comment ajouter la fonctionnalité Load More

Maintenant, ajoutons la fonctionnalité Load More qui permettra à notre application de charger l'ensemble suivant de 10 utilisateurs à chaque clic sur le bouton.

Modifiez la méthode `render` du fichier `App.js` avec le code suivant :

```js
render() {
  const { users, isLoading, errorMsg } = this.state;

  return (
    <div className="main-section">
      <Header />
      <UsersList users={users} />
      {errorMsg && <p className="errorMsg">{errorMsg}</p>}
      <div className="load-more">
        <button onClick={this.loadMore} className="btn-grad">
          {isLoading ? 'Chargement...' : 'Charger plus'}
        </button>
      </div>
    </div>
  );
}

```

Ici, nous avons ajouté la vérification `isLoading` à l'intérieur du bouton pour afficher soit le texte `Chargement...` soit `Charger plus` sur le bouton.

Ajoutez une nouvelle propriété `page` à l'état et initialisez-la à `0`.

```js
state = {
  users: [],
  page: 0,
  isLoading: false,
  errorMsg: ''
};

```

Et ajoutez la fonction de gestion `loadMore` avant la méthode `render` pour incrémenter la valeur de l'état `page` de 1 à chaque clic sur le bouton.

```js
loadMore = () => {
  this.setState((prevState) => ({
    page: prevState.page + 1
  }));
};

```

Ici, nous utilisons l'état précédent pour calculer la valeur d'état suivante de la page, donc le code ci-dessus est le même que le code ci-dessous :

```js
loadMore = () => {
  this.setState((prevState) => {
    return {
      page: prevState.page + 1
    };
  });
};

```

Nous utilisons simplement la syntaxe raccourcie ES6 pour retourner un objet depuis la fonction.

Maintenant, à l'intérieur de la méthode `componentDidMount`, modifiez l'URL de l'API du code ci-dessous :

```js
'https://randomuser.me/api/?page=0&results=10'

```

par ce code :

```js
`https://randomuser.me/api/?page=${page}&results=10`

```

Ici, nous utilisons la syntaxe des littéraux de gabarits ES6 pour utiliser la valeur dynamique de l'état `page` afin de charger l'ensemble suivant d'utilisateurs à chaque clic sur le bouton.

Déstructurez la `page` depuis l'état à l'intérieur de la méthode `componentDidMount` comme ceci :

```js
componentDidMount() {
  const { page } = this.state;
  ....
}

```

> Vous voulez explorer toutes les fonctionnalités ES6+ en détail ? Consultez mon livre [Mastering Modern JavaScript](https://modernjavascript.yogeshchavan.dev/).

Maintenant, vérifions la fonctionnalité de l'application.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/load_more_state_changing.gif)

Comme vous pouvez le voir, lorsque nous cliquons sur le bouton `Charger plus`, l'état `page` change dans les React DevTools, mais nous n'obtenons pas la nouvelle liste d'utilisateurs affichée à l'écran.

C'est parce que même si nous changeons l'état `page`, nous n'effectuons pas de nouvel appel API pour obtenir l'ensemble suivant d'utilisateurs avec la valeur `page` modifiée. Alors, corrigeons cela.

Créez une nouvelle fonction `loadUsers` au-dessus de la fonction `loadMore` et déplacez tout le code de `componentDidMount` à l'intérieur de la fonction `loadUsers`. Appelez ensuite la fonction `loadUsers` depuis la méthode `componentDidMount`.

Ajoutez également une méthode `componentDidUpdate` à l'intérieur du composant `App` comme ceci :

```js
componentDidUpdate(prevProps, prevState) {
  if (prevState.page !== this.state.page) {
    this.loadUsers();
  }
}

```

Comme nous mettons à jour la valeur de l'état `page` dans la fonction `loadMore`, une fois l'état mis à jour, la méthode `componentDidUpdate` sera appelée. Nous vérifions donc si la valeur d'état précédente de `page` n'est pas égale à la valeur d'état actuelle. Ensuite, nous effectuons à nouveau l'appel API en appelant la fonction `loadUsers`.

> Consultez mon [article précédent](https://www.freecodecamp.org/news/what-is-state-in-react-explained-with-examples/) pour en savoir plus sur pourquoi et quand nous devons utiliser la méthode `componentDidUpdate`.

Votre fichier `App.js` complet ressemblera maintenant à ceci :

```js
import React from 'react';
import Header from './components/Header';
import axios from 'axios';
import UsersList from './components/UsersList';

export default class App extends React.Component {
  state = {
    users: [],
    page: 0,
    isLoading: false,
    errorMsg: ''
  };

  componentDidMount() {
    this.loadUsers();
  }

  componentDidUpdate(prevProps, prevState) {
    if (prevState.page !== this.state.page) {
      this.loadUsers();
    }
  }

  loadUsers = () => {
    const { page } = this.state;

    this.setState({ isLoading: true });
    axios
      .get(`https://randomuser.me/api/?page=${page}&results=10`)
      .then((response) => {
        this.setState({ users: response.data.results, errorMsg: '' });
      })
      .catch((error) =>
        this.setState({
          errorMsg: 'Erreur lors du chargement des données. Réessayez plus tard.'
        })
      )
      .finally(() => {
        this.setState({ isLoading: false });
      });
  };

  loadMore = () => {
    this.setState((prevState) => ({
      page: prevState.page + 1
    }));
  };

  render() {
    const { users, isLoading, errorMsg } = this.state;

    return (
      <div className="main-section">
        <Header />
        <UsersList users={users} />
        {errorMsg && <p className="errorMsg">{errorMsg}</p>}
        <div className="load-more">
          <button onClick={this.loadMore} className="btn-grad">
            {isLoading ? 'Chargement...' : 'Charger plus'}
          </button>
        </div>
      </div>
    );
  }
}

```

Maintenant, si vous vérifiez à nouveau l'application en exécutant la commande `yarn start`, vous verrez l'écran suivant :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/new_users_loaded.gif)

Comme vous pouvez le voir, nous obtenons une nouvelle liste d'utilisateurs affichée à chaque clic sur le bouton charger plus. Mais le problème est que nous ne pouvons voir que 10 utilisateurs à la fois.

Apportons donc des modifications pour ajouter de nouveaux utilisateurs à la liste d'utilisateurs déjà affichée.

Pour cela, nous devons changer la façon dont nous définissons l'état `users`.

Notre appel `setState` actuel à l'intérieur de la fonction `loadUsers` ressemble à ceci :

```js
this.setState({ users: response.data.results, errorMsg: '' });

```

Ici, nous remplaçons toujours le tableau `users` par le nouvel ensemble d'utilisateurs. Modifiez donc l'appel `setState` ci-dessus par le code suivant :

```js
this.setState((prevState) => ({
  users: [...prevState.users, ...response.data.results],
  errorMsg: ''
}));

```

Ici, nous utilisons la syntaxe de mise à jour (updater syntax) de `setState`. Nous créons un nouveau tableau en décomposant les `users` déjà ajoutés en utilisant `...prevState.users`, puis nous ajoutons un nouvel ensemble de `users` en utilisant `...response.data.results`.

De cette façon, nous ne perdrons pas les données `users` précédemment chargées et nous pourrons également ajouter un nouvel ensemble de `users`.

Maintenant, si vous vérifiez à nouveau l'application, vous verrez le comportement correct du chargement des données.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/correct_loading.gif)

## Comment améliorer le code en utilisant Async/await

Si vous vérifiez la fonction `loadUsers`, vous verrez que le code semble complexe et difficile à lire.

```js
loadUsers = () => {
  const { page } = this.state;

  this.setState({ isLoading: true });
  axios
    .get(`https://randomuser.me/api/?page=${page}&results=10`)
    .then((response) => {
      this.setState((prevState) => ({
        users: [...prevState.users, ...response.data.results],
        errorMsg: ''
      }));
    })
    .catch((error) =>
      this.setState({
        errorMsg: 'Erreur lors du chargement des données. Réessayez plus tard.'
      })
    )
    .finally(() => {
      this.setState({ isLoading: false });
    });
};

```

Nous pouvons corriger cela en utilisant la syntaxe async/await.

Tout d'abord, nous devons marquer la fonction `loadUsers` comme async :

```js
loadUsers = async () => {

```

Parce que nous ne pouvons utiliser le mot-clé `await` qu'à l'intérieur d'une fonction déclarée comme `async`.

Maintenant, remplacez la fonction `loadUsers` par le code suivant :

```js
loadUsers = async () => {
  try {
    const { page } = this.state;

    this.setState({ isLoading: true });
    const response = await axios.get(
      `https://randomuser.me/api/?page=${page}&results=10`
    );

    this.setState((prevState) => ({
      users: [...prevState.users, ...response.data.results],
      errorMsg: ''
    }));
  } catch (error) {
    this.setState({
      errorMsg: 'Erreur lors du chargement des données. Réessayez plus tard.'
    });
  } finally {
    this.setState({ isLoading: false });
  }
};

```

Ici, nous avons utilisé le mot-clé `await` avant l'appel `axios.get` afin que la ligne de code suivante, qui est l'appel `setState`, ne soit pas exécutée tant que nous n'avons pas reçu la réponse de l'API.

S'il y a une erreur lors de la réception de la réponse de l'API, le bloc `catch` sera exécuté. Le bloc `finally` définira l'état `isLoading` sur `false`.

Votre fichier `App.js` modifié ressemblera maintenant à ceci :

```js
import React from 'react';
import Header from './components/Header';
import axios from 'axios';
import UsersList from './components/UsersList';

export default class App extends React.Component {
  state = {
    users: [],
    page: 0,
    isLoading: false,
    errorMsg: ''
  };

  componentDidMount() {
    this.loadUsers();
  }

  componentDidUpdate(prevProps, prevState) {
    if (prevState.page !== this.state.page) {
      this.loadUsers();
    }
  }

  loadUsers = async () => {
    try {
      const { page } = this.state;

      this.setState({ isLoading: true });
      const response = await axios.get(
        `https://randomuser.me/api/?page=${page}&results=10`
      );

      this.setState((prevState) => ({
        users: [...prevState.users, ...response.data.results],
        errorMsg: ''
      }));
    } catch (error) {
      this.setState({
        errorMsg: 'Erreur lors du chargement des données. Réessayez plus tard.'
      });
    } finally {
      this.setState({ isLoading: false });
    }
  };

  loadMore = () => {
    this.setState((prevState) => ({
      page: prevState.page + 1
    }));
  };

  render() {
    const { users, isLoading, errorMsg } = this.state;

    return (
      <div className="main-section">
        <Header />
        <UsersList users={users} />
        {errorMsg && <p className="errorMsg">{errorMsg}</p>}
        <div className="load-more">
          <button onClick={this.loadMore} className="btn-grad">
            {isLoading ? 'Chargement...' : 'Charger plus'}
          </button>
        </div>
      </div>
    );
  }
}

```

Maintenant, le code de la fonction `loadUsers` semble beaucoup plus propre et plus facile à comprendre qu'auparavant. Et si vous vérifiez l'application, vous verrez qu'elle fonctionne également correctement.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/correct_loading-1.gif)

## Comment refactoriser le code d'un composant de classe en composant fonctionnel

Nous avons terminé de construire la fonctionnalité complète de l'application. Refactorisons maintenant le code pour utiliser des composants fonctionnels avec les React Hooks.

> Si vous débutez avec les React Hooks, consultez [mon article ici](https://levelup.gitconnected.com/an-introduction-to-react-hooks-50281fd961fe?source=friends_link&sk=89baff89ec8bc637e7c13b7554904e54) pour une introduction aux Hooks.

Créez un nouveau fichier nommé `AppFunctional.js` dans le dossier `src` avec le contenu suivant :

```js
import React from 'react';

const AppFunctional = () => {
  return (
    <div>
      <h2>Composant fonctionnel</h2>
    </div>
  );
};

export default AppFunctional;

```

Nous avons créé un nouveau fichier pour le composant fonctionnel afin que vous puissiez comparer les deux codes et le conserver pour référence.

Maintenant, ouvrez le fichier `index.js` et remplacez le contenu du fichier par le code suivant :

```js
import React from 'react';
import ReactDOM from 'react-dom';
import AppFunctional from './AppFunctional';
import './styles.css';

ReactDOM.render(<AppFunctional />, document.getElementById('root'));

```

Ici, nous avons utilisé le composant `AppFunctional` à l'intérieur de la méthode `render` et nous avons également ajouté l'importation correspondante en haut du fichier.

Maintenant, si vous redémarrez votre application en utilisant la commande `yarn start`, vous verrez l'écran suivant :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/functional_component.png)

Nous affichons donc correctement le code du composant `AppFunctional` à l'écran.

Maintenant, remplacez le contenu du composant `AppFunctional` par le code suivant :

```js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Header from './components/Header';
import UsersList from './components/UsersList';

const AppFunctional = () => {
  const [users, setUsers] = useState([]);
  const [page, setPage] = useState(0);
  const [isLoading, setIsLoading] = useState(false);
  const [errorMsg, setErrorMsg] = useState('');

  useEffect(() => {
    const loadUsers = async () => {
      try {
        setIsLoading(true);
        const response = await axios.get(
          `https://randomuser.me/api/?page=${page}&results=10`
        );

        setUsers([...users, ...response.data.results]);
        setErrorMsg('');
      } catch (error) {
        setErrorMsg('Erreur lors du chargement des données. Réessayez plus tard.');
      } finally {
        setIsLoading(false);
      }
    };

    loadUsers();
  }, []);

  const loadMore = () => {
    setPage((page) => page + 1);
  };

  return (
    <div className="main-section">
      <Header />
      <UsersList users={users} />
      {errorMsg && <p className="errorMsg">{errorMsg}</p>}
      <div className="load-more">
        <button onClick={loadMore} className="btn-grad">
          {isLoading ? 'Chargement...' : 'Charger plus'}
        </button>
      </div>
    </div>
  );
};

export default AppFunctional;

```

Ici, nous avons initialement déclaré les états requis en utilisant le hook `useState` :

```js
const [users, setUsers] = useState([]);
const [page, setPage] = useState(0);
const [isLoading, setIsLoading] = useState(false);
const [errorMsg, setErrorMsg] = useState('');

```

Ensuite, nous avons ajouté un hook `useEffect` et lui avons passé un tableau vide `[]` comme second argument. Cela signifie que le code à l'intérieur du hook `useEffect` ne sera exécuté qu'une seule fois lors du montage du composant.

```js
useEffect(() => {
 // votre code
}, []);

```

Nous avons déplacé toute la fonction `loadUsers` à l'intérieur du hook `useEffect`, puis nous l'avons appelée à l'intérieur du hook comme ceci :

```js
useEffect(() => {
  const loadUsers = async () => {
    // votre code
  };

  loadUsers();
}, []);

```

Nous avons également supprimé toutes les références à `this.state` car les composants fonctionnels n'ont pas besoin du contexte `this`.

Avant d'effectuer l'appel API, nous définissons l'état `isLoading` sur `true` en utilisant `setIsLoading(true);`.

Comme nous avons déjà accès au tableau `users` à l'intérieur du composant, nous le définissons directement comme un nouveau tableau pour la fonction `setUsers` comme ceci :

```js
setUsers([...users, ...response.data.results]);

```

> Si vous voulez savoir pourquoi nous ne pouvons pas utiliser le mot-clé `async` directement pour la fonction du hook `useEffect`, consultez [cet article](https://javascript.plainenglish.io/handling-api-calls-using-async-await-in-useeffect-hook-990fb4ae423?source=friends_link&sk=dd686f066a434c41a76c352e3ec69767).

Ensuite, nous avons modifié la fonction `loadMore` du code ci-dessous :

```js
loadMore = () => {
  this.setState((prevState) => ({
    page: prevState.page + 1
  }));
};

```

par ce code :

```js
const loadMore = () => {
  setPage((page) => page + 1);
};

```

> Notez que pour déclarer une fonction dans des composants fonctionnels, vous devez ajouter `const` ou `let` avant la déclaration. Comme la fonction ne va pas changer, il est recommandé d'utiliser `const` tel que `const loadMore = () => { }`.

Ensuite, nous avons copié le contenu de la méthode `render` tel quel à l'intérieur du composant `AppFunctional` pour retourner le JSX. Nous avons également changé `onClick={this.loadMore}` en `onClick={loadMore}`.

```jsx
return (
  <div className="main-section">
    <Header />
    <UsersList users={users} />
    {errorMsg && <p className="errorMsg">{errorMsg}</p>}
    <div className="load-more">
      <button onClick={loadMore} className="btn-grad">
        {isLoading ? 'Chargement...' : 'Charger plus'}
      </button>
    </div>
  </div>
);

```

Maintenant, si vous vérifiez l'application, vous verrez l'écran suivant :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/functional_load_more_not_working.gif)

Comme vous pouvez le voir, les utilisateurs sont correctement chargés, mais la fonctionnalité load more ne fonctionne pas.

C'est parce que nous n'effectuons l'appel API qu'une seule fois lors du montage du composant, car nous passons le tableau de dépendances vide `[]` comme second argument au hook `useEffect`.

Pour effectuer à nouveau l'appel API lorsque l'état `page` change, nous devons ajouter `page` comme dépendance pour le hook `useEffect` comme ceci :

```js
useEffect(() => {
  // exécuter le code pour charger les utilisateurs
}, [page]);

```

Le `useEffect` ci-dessus revient au même que d'écrire le code ci-dessous :

```js
componentDidUpdate(prevProps, prevState) {
  if (prevState.page !== this.state.page) {
    // exécuter le code pour charger les utilisateurs
  }
}

```

`useEffect` permet vraiment d'écrire moins de code et de le rendre facile à comprendre.

Ainsi, avec ce changement, le code à l'intérieur du hook `useEffect` sera exécuté lors du montage du composant ainsi que lorsque l'état `page` est modifié.

Maintenant, si vous vérifiez l'application, vous verrez que la fonctionnalité load more fonctionne à nouveau comme prévu.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/correct_loading-2.gif)

Mais si vous vérifiez le terminal/l'invite de commande, vous pourriez voir un avertissement comme indiqué ci-dessous (si `ESLint` est installé sur votre machine) :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/eslint_warning.png)

Ces avertissements nous aident à éviter des problèmes dans notre application qui pourraient survenir plus tard, il est donc toujours bon de les corriger si possible.

Comme nous référençons l'état `users` à l'intérieur de la fonction `loadUsers`, nous devons également l'inclure dans le tableau de dépendances. Alors, faisons-le.

Incluez `users` comme dépendance avec `page` comme ceci :

```js
useEffect(() => {
  // votre code
}, [page, users]);

```

Vérifions maintenant la fonctionnalité de l'application.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/infinite_loop.gif)

Comme vous pouvez le voir, nous obtenons continuellement un nouvel ensemble d'utilisateurs à mesure que nous faisons défiler la page et l'application entre dans une boucle infinie.

C'est parce que lorsque le composant est monté, le code à l'intérieur du hook `useEffect` est exécuté pour effectuer un appel API. Une fois que nous obtenons le résultat, nous définissons le tableau `users`.

Comme `users` est mentionné dans la liste des dépendances, une fois que le tableau `users` est modifié, `useEffect` s'exécutera à nouveau, et cela se produira encore et encore, créant une boucle infinie.

Donc, pour corriger cela, nous devons éviter de référencer le tableau `users` externe d'une manière ou d'une autre. Pour ce faire, utilisons la syntaxe de mise à jour (updater syntax) de set state pour définir l'état `users`.

Par conséquent, modifiez le code ci-dessous :

```js
setUsers([...users, ...response.data.results]);

```

par ce code :

```js
setUsers((users) => [...users, ...response.data.results]);

```

Ici, nous utilisons la valeur précédente de `users` pour créer un nouveau tableau `users`.

Maintenant, nous pouvons supprimer `users` du tableau de dépendances de `useEffect` car nous ne référençons plus la variable externe `users`.

Votre hook `useEffect` modifié ressemblera maintenant à ceci :

```js
useEffect(() => {
  const loadUsers = async () => {
    try {
      setIsLoading(true);
      const response = await axios.get(
        `https://randomuser.me/api/?page=${page}&results=10`
      );

      setUsers((users) => [...users, ...response.data.results]);
      setErrorMsg('');
    } catch (error) {
      setErrorMsg('Erreur lors du chargement des données. Réessayez plus tard.');
    } finally {
      setIsLoading(false);
    }
  };

  loadUsers();
}, [page]);

```

Si vous vérifiez l'application maintenant, vous verrez qu'elle fonctionne comme prévu sans aucun problème.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/correct_loading-3.gif)

Et nous ne recevons plus d'erreurs dans le terminal maintenant.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/no_error.png)

### Merci de m'avoir lu !

Vous pouvez trouver le code source complet de cette application dans [ce dépôt](https://github.com/myogeshchavan97/class-to-hooks-refactoring) et une démo en direct de l'application déployée [ici](https://random-users-app.netlify.app/).

À partir d'ES6, il y a eu de nombreux ajouts utiles à JavaScript comme :

* La déstructuration ES6
* La syntaxe d'importation et d'exportation
* Les fonctions fléchées
* Les promesses (Promises)
* Async/await
* L'opérateur de chaînage optionnel et bien plus encore.

**Vous pouvez tout apprendre sur les fonctionnalités ES6+ en détail dans mon livre [Mastering Modern JavaScript](https://modernjavascript.yogeshchavan.dev/).**

> Consultez le contenu de l'aperçu gratuit du livre [ici](https://www.freecodecamp.org/news/learn-modern-javascript/).

De plus, vous pouvez consulter mon cours **gratuit** [Introduction to React Router](https://yogeshchavan1.podia.com/react-router-introduction) pour apprendre React Router à partir de zéro.

Vous voulez rester à jour avec du contenu régulier concernant JavaScript, React, Node.js ? [Suivez-moi sur LinkedIn](https://www.linkedin.com/in/yogesh-chavan97/).

<a href="https://bit.ly/3w0DGum" target="_blank" rel="noreferrer noopener"><img src="https://gist.github.com/myogeshchavan97/98ae4f4ead57fde8d47fcf7641220b72/raw/c3e4265df4396d639a7938a83bffd570130483b1/banner.jpg"></a>