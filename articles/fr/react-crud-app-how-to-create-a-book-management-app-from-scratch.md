---
title: Tutoriel React CRUD – Comment créer une application de gestion de livres en
  React à partir de zéro
subtitle: ''
author: Yogesh Chavan
co_authors: []
series: null
date: '2021-04-14T19:20:48.000Z'
originalURL: https://freecodecamp.org/news/react-crud-app-how-to-create-a-book-management-app-from-scratch
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/book_management.jpg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: Tutoriel React CRUD – Comment créer une application de gestion de livres
  en React à partir de zéro
seo_desc: "In this article, you will build a Book Management App in React from scratch.\
  \ \nBy creating this app, you will learn:\n\nHow to perform CRUD operations\nHow\
  \ to use React Router for navigation between routes\nHow to use React Context API\
  \ to pass data across..."
---

Dans cet article, vous allez créer une application de gestion de livres en React à partir de zéro. 

En créant cette application, vous apprendrez :

1. Comment effectuer des opérations CRUD
2. Comment utiliser React Router pour la navigation entre les routes
3. Comment utiliser l'API Context de React pour passer des données entre les routes
4. Comment créer un Hook personnalisé en React
5. Comment stocker des données dans le stockage local pour les conserver même après le rechargement de la page
6. Comment gérer les données stockées dans le stockage local en utilisant un hook personnalisé

et bien plus encore.

Nous allons utiliser les Hooks React pour construire cette application. Donc, si vous êtes nouveau dans les Hooks React, consultez mon article [Introduction aux Hooks React](https://levelup.gitconnected.com/an-introduction-to-react-hooks-50281fd961fe?source=friends_link&sk=89baff89ec8bc637e7c13b7554904e54) pour apprendre les bases.

> Vous voulez apprendre Redux depuis le début et construire une application de commande de nourriture à partir de zéro ? Consultez le cours [Maîtriser Redux](https://master-redux.yogeshchavan.dev/).

## Installation initiale

Créez un nouveau projet en utilisant `create-react-app` :

```js
npx create-react-app book-management-app
```

Une fois le projet créé, supprimez tous les fichiers du dossier `src` et créez les fichiers `index.js` et `styles.scss` à l'intérieur du dossier `src`. Créez également les dossiers `components`, `context`, `hooks` et `router` à l'intérieur du dossier `src`.

Installez les dépendances nécessaires :

```js
yarn add bootstrap@4.6.0 lodash@4.17.21 react-bootstrap@1.5.2 node-sass@4.14.1 react-router-dom@5.2.0 uuid@8.3.2
```

Ouvrez `styles.scss` et ajoutez le contenu depuis [ici](https://github.com/myogeshchavan97/react-book-management-app/blob/master/src/styles.scss) à l'intérieur.

## Comment créer les pages initiales

Créez un nouveau fichier `Header.js` à l'intérieur du dossier `components` avec le contenu suivant :

```jsx
import React from 'react';
import { NavLink } from 'react-router-dom';

const Header = () => {
  return (
    <header>
      <h1>Application de gestion de livres</h1>
      <hr />
      <div className="links">
        <NavLink to="/" className="link" activeClassName="active" exact>
          Liste des livres
        </NavLink>
        <NavLink to="/add" className="link" activeClassName="active">
          Ajouter un livre
        </NavLink>
      </div>
    </header>
  );
};

export default Header;
```

Ici, nous avons ajouté deux liens de navigation en utilisant le composant `NavLink` de `react-router-dom` : un pour voir la liste de tous les livres, et un autre pour ajouter un nouveau livre.

Nous utilisons `NavLink` au lieu de la balise d'ancrage (`<a />`) pour que la page ne se recharge pas lorsque l'utilisateur clique sur l'un des liens.

Créez un nouveau fichier appelé `BooksList.js` à l'intérieur du dossier `components` avec le contenu suivant :

```js
import React from 'react';

const BooksList = () => {
  return <h2>Liste des livres</h2>;
};

export default BooksList;
```

Créez un nouveau fichier appelé `AddBook.js` à l'intérieur du dossier `components` avec le contenu suivant :

```jsx
import React from 'react';
import BookForm from './BookForm';

const AddBook = () => {
  const handleOnSubmit = (book) => {
    console.log(book);
  };

  return (
    <React.Fragment>
      <BookForm handleOnSubmit={handleOnSubmit} />
    </React.Fragment>
  );
};

export default AddBook;
```

Dans ce fichier, nous affichons un composant `BookForm` (que nous devons encore créer).

Pour le composant `BookForm`, nous passons la méthode `handleOnSubmit` afin de pouvoir effectuer un traitement ultérieur une fois le formulaire soumis.

Maintenant, créez un nouveau fichier `BookForm.js` à l'intérieur du dossier `components` avec le contenu suivant :

```jsx
import React, { useState } from 'react';
import { Form, Button } from 'react-bootstrap';
import { v4 as uuidv4 } from 'uuid';

const BookForm = (props) => {
  const [book, setBook] = useState({
    bookname: props.book ? props.book.bookname : '',
    author: props.book ? props.book.author : '',
    quantity: props.book ? props.book.quantity : '',
    price: props.book ? props.book.price : '',
    date: props.book ? props.book.date : ''
  });

  const [errorMsg, setErrorMsg] = useState('');
  const { bookname, author, price, quantity } = book;

  const handleOnSubmit = (event) => {
    event.preventDefault();
    const values = [bookname, author, price, quantity];
    let errorMsg = '';

    const allFieldsFilled = values.every((field) => {
      const value = `${field}`.trim();
      return value !== '' && value !== '0';
    });

    if (allFieldsFilled) {
      const book = {
        id: uuidv4(),
        bookname,
        author,
        price,
        quantity,
        date: new Date()
      };
      props.handleOnSubmit(book);
    } else {
      errorMsg = 'Veuillez remplir tous les champs.';
    }
    setErrorMsg(errorMsg);
  };

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    switch (name) {
      case 'quantity':
        if (value === '' || parseInt(value) === +value) {
          setBook((prevState) => ({
            ...prevState,
            [name]: value
          }));
        }
        break;
      case 'price':
        if (value === '' || value.match(/^\d{1,}(\.\d{0,2})?$/)) {
          setBook((prevState) => ({
            ...prevState,
            [name]: value
          }));
        }
        break;
      default:
        setBook((prevState) => ({
          ...prevState,
          [name]: value
        }));
    }
  };

  return (
    <div className="main-form">
      {errorMsg && <p className="errorMsg">{errorMsg}</p>}
      <Form onSubmit={handleOnSubmit}>
        <Form.Group controlId="name">
          <Form.Label>Nom du livre</Form.Label>
          <Form.Control
            className="input-control"
            type="text"
            name="bookname"
            value={bookname}
            placeholder="Entrez le nom du livre"
            onChange={handleInputChange}
          />
        </Form.Group>
        <Form.Group controlId="author">
          <Form.Label>Auteur du livre</Form.Label>
          <Form.Control
            className="input-control"
            type="text"
            name="author"
            value={author}
            placeholder="Entrez le nom de l'auteur"
            onChange={handleInputChange}
          />
        </Form.Group>
        <Form.Group controlId="quantity">
          <Form.Label>Quantité</Form.Label>
          <Form.Control
            className="input-control"
            type="number"
            name="quantity"
            value={quantity}
            placeholder="Entrez la quantité disponible"
            onChange={handleInputChange}
          />
        </Form.Group>
        <Form.Group controlId="price">
          <Form.Label>Prix du livre</Form.Label>
          <Form.Control
            className="input-control"
            type="text"
            name="price"
            value={price}
            placeholder="Entrez le prix du livre"
            onChange={handleInputChange}
          />
        </Form.Group>
        <Button variant="primary" type="submit" className="submit-btn">
          Soumettre
        </Button>
      </Form>
    </div>
  );
};

export default BookForm;
```

Comprenons ce que nous faisons ici.

Initialement, nous avons défini un état sous forme d'objet en utilisant le hook `useState` pour stocker toutes les informations saisies comme ceci :

```js
const [book, setBook] = useState({
    bookname: props.book ? props.book.bookname : '',
    author: props.book ? props.book.author : '',
    quantity: props.book ? props.book.quantity : '',
    price: props.book ? props.book.price : '',
    date: props.book ? props.book.date : ''
  });
```

Comme nous allons utiliser le même composant `BookForm` pour ajouter et modifier le livre, nous vérifions d'abord si la prop `book` est passée ou non en utilisant l'opérateur ternaire.

Si la prop est passée, nous la définissons à la valeur passée, sinon une chaîne vide (`''`).

> Ne vous inquiétez pas si cela semble compliqué maintenant. Vous comprendrez mieux une fois que nous aurons construit quelques fonctionnalités initiales.

Ensuite, nous avons ajouté un état pour afficher un message d'erreur et nous avons utilisé la syntaxe de déstructuration ES6 pour faire référence à chaque propriété à l'intérieur de l'état comme ceci :

```js
const [errorMsg, setErrorMsg] = useState('');
const { bookname, author, price, quantity } = book;
```

À partir du composant `BookForm`, nous retournons un formulaire où nous entrons le nom du livre, l'auteur du livre, la quantité et le prix. Nous utilisons le framework [react-bootstrap](https://react-bootstrap.github.io/) pour afficher le formulaire dans un format agréable.

Chaque champ de saisie a ajouté un gestionnaire `onChange` qui appelle la méthode `handleInputChange`.

À l'intérieur de la méthode `handleInputChange`, nous avons ajouté une instruction switch pour changer la valeur de l'état en fonction du champ de saisie modifié.

Lorsque nous tapons quelque chose dans le champ de saisie `quantity`, `event.target.name` sera `quantity`, donc le premier cas du switch correspondra. À l'intérieur de ce cas, nous vérifions si la valeur saisie est un entier sans point décimal.

Si oui, alors seulement nous mettons à jour l'état comme montré ci-dessous :

```js
if (value === '' || parseInt(value) === +value) {
  setBook((prevState) => ({
    ...prevState,
    [name]: value
  }));
}
```

Ainsi, l'utilisateur ne peut pas saisir de valeur décimale pour le champ de saisie de la quantité.

Pour le cas du switch `price`, nous vérifions un nombre décimal avec seulement deux chiffres après le point décimal. Nous avons donc ajouté une vérification d'expression régulière qui ressemble à ceci : `value.match(/^\d{1,}(\.\d{0,2})?$/)`.

Si la valeur du prix correspond à l'expression régulière, alors seulement nous mettons à jour l'état.

**Note :** Pour les cas de switch `quantity` et `price`, nous vérifions également les valeurs vides comme ceci : `value === ''`. Cela permet à l'utilisateur de supprimer entièrement la valeur saisie s'il en a besoin.

Sans cette vérification, l'utilisateur ne pourra pas supprimer la valeur saisie en appuyant sur `Ctrl + A + Delete`.

Pour tous les autres champs de saisie, le cas de switch par défaut sera exécuté, ce qui mettra à jour l'état en fonction de la valeur saisie par l'utilisateur.

Ensuite, une fois que nous soumettons le formulaire, la méthode `handleOnSubmit` sera appelée.

À l'intérieur de cette méthode, nous vérifions d'abord si l'utilisateur a saisi toutes les informations en utilisant la méthode `every` du tableau :

```js
const allFieldsFilled = values.every((field) => {
  const value = `${field}`.trim();
  return value !== '' && value !== '0';
});
```

La méthode `every` du tableau est l'une des méthodes de tableau les plus utiles en JavaScript.

> Consultez [mon article ici](https://www.freecodecamp.org/news/complete-introduction-to-the-most-useful-javascript-array-methods/) pour en savoir plus sur les méthodes de tableau JavaScript les plus utiles ainsi que leur support par les navigateurs.

Si toutes les valeurs sont remplies, alors nous créons un objet avec toutes les valeurs remplies. Nous appelons également la méthode `handleOnSubmit` en passant le livre comme argument, sinon nous définissons un message d'erreur.

La méthode `handleOnSubmit` est passée en tant que prop depuis le composant `AddBook`.

```js
if (allFieldsFilled) {
  const book = {
    id: uuidv4(),
    bookname,
    author,
    price,
    quantity,
    date: new Date()
  };
  props.handleOnSubmit(book);
} else {
  errorMsg = 'Veuillez remplir tous les champs.';
}
```

Notez que pour créer un ID unique, nous appelons la méthode `uuidv4()` du package npm [uuid](https://www.npmjs.com/package/uuid).

Maintenant, créez un nouveau fichier `AppRouter.js` à l'intérieur du dossier `router` avec le contenu suivant :

```jsx
import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import Header from '../components/Header';
import AddBook from '../components/AddBook';
import BooksList from '../components/BooksList';

const AppRouter = () => {
  return (
    <BrowserRouter>
      <div>
        <Header />
        <div className="main-content">
          <Switch>
            <Route component={BooksList} path="/" exact={true} />
            <Route component={AddBook} path="/add" />
          </Switch>
        </div>
      </div>
    </BrowserRouter>
  );
};

export default AppRouter;
```

Ici, nous avons configuré le routage pour divers composants comme `BooksList` et `AddBook` en utilisant la bibliothèque `react-router-dom`.

> Si vous êtes nouveau dans React Router, consultez mon cours gratuit [Introduction à React Router](https://yogeshchavan1.podia.com/react-router-introduction).

Maintenant, ouvrez le fichier `src/index.js` et ajoutez le contenu suivant à l'intérieur :

```js
import React from 'react';
import ReactDOM from 'react-dom';
import AppRouter from './router/AppRouter';
import 'bootstrap/dist/css/bootstrap.min.css';
import './styles.scss';

ReactDOM.render(<AppRouter />, document.getElementById('root'));
```

Maintenant, démarrez l'application React en exécutant la commande suivante depuis le terminal :

```js
yarn start
```

Vous verrez l'écran suivant lorsque vous accéderez à l'application à l'adresse [http://localhost:3000/](http://localhost:3000/).

![Image](https://www.freecodecamp.org/news/content/images/2021/04/initial_screen.gif)

![Image](https://www.freecodecamp.org/news/content/images/2021/04/add_book.gif)

Comme vous pouvez le voir, nous sommes en mesure d'ajouter correctement le livre et de l'afficher sur la console.

Mais au lieu de le journaliser dans la console, ajoutons-le au stockage local.

## Comment créer un Hook personnalisé pour le stockage local

Le stockage local est incroyable. Il nous permet de stocker facilement les données de l'application dans le navigateur et est une alternative aux cookies pour stocker des données.

L'avantage d'utiliser le stockage local est que les données seront enregistrées en permanence dans le cache du navigateur jusqu'à ce que nous les supprimions manuellement, donc nous pouvons y accéder même après avoir actualisé la page. Comme vous le savez peut-être, les données stockées dans l'état React seront perdues une fois que nous actualiserons la page.

Il existe de nombreux cas d'utilisation pour le stockage local, et l'un d'eux est de stocker les articles du panier d'achat afin qu'ils ne soient pas supprimés même si nous actualisons la page.

Pour ajouter des données au stockage local, nous utilisons la méthode `setItem` en fournissant une clé et une valeur :

```js
localStorage.setItem(key, value)
```

> La clé et la valeur doivent être des chaînes. Mais nous pouvons également stocker l'objet JSON en utilisant la méthode `JSON.stringify`.

Pour en savoir plus sur le stockage local et ses diverses applications en détail, consultez [cet article](https://javascript.plainenglish.io/everything-you-need-to-know-about-html5-local-storage-and-session-storage-479c63415c0a?source=friends_link&sk=f429aa5008683a3b0359db43f976efb3).

Créez un nouveau fichier `useLocalStorage.js` à l'intérieur du dossier `hooks` avec le contenu suivant :

```jsx
import { useState, useEffect } from 'react';

const useLocalStorage = (key, initialValue) => {
  const [value, setValue] = useState(() => {
    try {
      const localValue = window.localStorage.getItem(key);
      return localValue ? JSON.parse(localValue) : initialValue;
    } catch (error) {
      return initialValue;
    }
  });

  useEffect(() => {
    window.localStorage.setItem(key, JSON.stringify(value));
  }, [key, value]);

  return [value, setValue];
};

export default useLocalStorage;
```

Ici, nous avons utilisé un hook `useLocalStorage` qui accepte une `key` et une `initialValue`.

Pour déclarer l'état en utilisant le hook `useState`, nous utilisons [l'initialisation paresseuse](https://reactjs.org/docs/hooks-reference.html#lazy-initial-state).

Ainsi, le code à l'intérieur de la fonction passée à `useState` ne sera exécuté qu'une seule fois, même si le hook `useLocalStorage` est appelé plusieurs fois à chaque nouveau rendu de l'application.

Ainsi, initialement, nous vérifions s'il y a une valeur dans le stockage local avec la `key` fournie et nous retournons la valeur en la analysant à l'aide de la méthode `JSON.parse` :

```js
try {
  const localValue = window.localStorage.getItem(key);
  return localValue ? JSON.parse(localValue) : initialValue;
} catch (error) {
  return initialValue;
}
```

Ensuite, si la `key` ou la `value` change, nous mettrons à jour le stockage local :

```js
useEffect(() => {
    window.localStorage.setItem(key, JSON.stringify(value));
}, [key, value]);

return [value, setValue];
```

Ensuite, nous retournons la `value` stockée dans le stockage local et la fonction `setValue` que nous appellerons pour mettre à jour les données du localStorage.

## Comment utiliser le Hook de stockage local

Maintenant, utilisons ce hook `useLocalStorage` afin de pouvoir ajouter ou supprimer des données du stockage local.

Ouvrez le fichier `AppRouter.js` et utilisez le hook `useLocalStorage` à l'intérieur du composant :

```js
import useLocalStorage from '../hooks/useLocalStorage';

const AppRouter = () => {
 const [books, setBooks] = useLocalStorage('books', []);
 
 return (
  ...
 )
}
```

Maintenant, nous devons passer les `books` et `setBooks` en tant que props au composant `AddBook` afin de pouvoir ajouter le livre au stockage local.

Donc, changez la route de ce code :

```jsx
<Route component={AddBook} path="/add" />
```

en ce code :

```jsx
<Route
  render={(props) => (
    <AddBook {...props} books={books} setBooks={setBooks} />
  )}
  path="/add"
/>
```

Ici, nous utilisons le motif render props pour passer les props par défaut passées par React router ainsi que les `books` et `setBooks`.

> Consultez mon cours gratuit [Introduction à React Router](https://yogeshchavan1.podia.com/react-router-introduction) pour mieux comprendre ce motif render props et l'importance d'utiliser le mot-clé `render` au lieu de `component`.

Votre fichier `AppRouter.js` complet ressemblera maintenant à ceci :

```jsx
import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import Header from '../components/Header';
import AddBook from '../components/AddBook';
import BooksList from '../components/BooksList';
import useLocalStorage from '../hooks/useLocalStorage';

const AppRouter = () => {
  const [books, setBooks] = useLocalStorage('books', []);

  return (
    <BrowserRouter>
      <div>
        <Header />
        <div className="main-content">
          <Switch>
            <Route component={BooksList} path="/" exact={true} />
            <Route
              render={(props) => (
                <AddBook {...props} books={books} setBooks={setBooks} />
              )}
              path="/add"
            />
          </Switch>
        </div>
      </div>
    </BrowserRouter>
  );
};

export default AppRouter;
```

Maintenant, ouvrez `AddBook.js` et remplacez son contenu par le code suivant :

```jsx
import React from 'react';
import BookForm from './BookForm';

const AddBook = ({ history, books, setBooks }) => {
  const handleOnSubmit = (book) => {
    setBooks([book, ...books]);
    history.push('/');
  };

  return (
    <React.Fragment>
      <BookForm handleOnSubmit={handleOnSubmit} />
    </React.Fragment>
  );
};

export default AddBook;
```

Tout d'abord, nous utilisons la syntaxe de déstructuration ES6 pour accéder aux props `history`, `books` et `setBooks` dans le composant.

La prop `history` est automatiquement passée par React Router à chaque composant mentionné dans `<Route />`. Nous passons les props `books` et `setBooks` depuis le fichier `AppRouter.js`.

Nous stockons tous les livres ajoutés dans un tableau. À l'intérieur de la méthode `handleOnSubmit`, nous appelons la fonction `setBooks` en passant un tableau en ajoutant un livre nouvellement ajouté en premier, puis en étalant tous les livres déjà ajoutés dans le tableau `books` comme montré ci-dessous :

```js
setBooks([book, ...books]);
```

Ici, j'ajoute le `book` nouvellement ajouté en premier, puis j'étale les `books` déjà ajoutés parce que je veux que le dernier livre soit affiché en premier lorsque nous afficherons la liste des livres plus tard.

Mais vous pouvez changer l'ordre si vous le souhaitez comme ceci :

```js
setBooks([...books, book]);
```

Cela ajoutera le livre nouvellement ajouté à la fin de tous les livres déjà ajoutés.

Nous pouvons utiliser l'opérateur de propagation parce que nous savons que `books` est un tableau (comme nous l'avons initialisé à un tableau vide `[]` dans le fichier `AppRouter.js` comme montré ci-dessous) :

```js
 const [books, setBooks] = useLocalStorage('books', []);
```

Ensuite, une fois que le livre est ajouté au stockage local en appelant la méthode `setBooks`, à l'intérieur de la méthode `handleOnSubmit`, nous redirigeons l'utilisateur vers la page `Books List` en utilisant la méthode `history.push` :

```js
history.push('/');
```

Maintenant, vérifions si nous sommes capables de sauvegarder les livres dans le stockage local ou non.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/added_local_storage.gif)

Comme vous pouvez le voir, le livre est correctement ajouté au stockage local (et vous pouvez confirmer cela dans l'onglet applications des outils de développement Chrome).

## Comment afficher les livres ajoutés sur l'interface utilisateur

Maintenant, affichons les livres ajoutés sur l'interface utilisateur sous le menu `Books List`.

Ouvrez `AppRouter.js` et passez les `books` et `setBooks` en tant que props au composant `BooksList`.

Votre fichier `AppRouter.js` ressemblera maintenant à ceci :

```jsx
import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import Header from '../components/Header';
import AddBook from '../components/AddBook';
import BooksList from '../components/BooksList';
import useLocalStorage from '../hooks/useLocalStorage';

const AppRouter = () => {
  const [books, setBooks] = useLocalStorage('books', []);

  return (
    <BrowserRouter>
      <div>
        <Header />
        <div className="main-content">
          <Switch>
            <Route
              render={(props) => (
                <BooksList {...props} books={books} setBooks={setBooks} />
              )}
              path="/"
              exact={true}
            />
            <Route
              render={(props) => (
                <AddBook {...props} books={books} setBooks={setBooks} />
              )}
              path="/add"
            />
          </Switch>
        </div>
      </div>
    </BrowserRouter>
  );
};

export default AppRouter;
```

Ici, nous avons simplement changé la première Route liée au composant `BooksList`.

Maintenant, créez un nouveau fichier `Book.js` à l'intérieur du dossier `components` avec le contenu suivant :

```jsx
import React from 'react';
import { Button, Card } from 'react-bootstrap';

const Book = ({
  id,
  bookname,
  author,
  price,
  quantity,
  date,
  handleRemoveBook
}) => {
  return (
    <Card style={{ width: '18rem' }} className="book">
      <Card.Body>
        <Card.Title className="book-title">{bookname}</Card.Title>
        <div className="book-details">
          <div>Auteur : {author}</div>
          <div>Quantité : {quantity} </div>
          <div>Prix : {price} </div>
          <div>Date : {new Date(date).toDateString()}</div>
        </div>
        <Button variant="primary">Modifier</Button>{' '}
        <Button variant="danger" onClick={() => handleRemoveBook(id)}>
          Supprimer
        </Button>
      </Card.Body>
    </Card>
  );
};

export default Book;
```

Maintenant, ouvrez le fichier `BooksList.js` et remplacez son contenu par le code suivant :

```jsx
import React from 'react';
import _ from 'lodash';
import Book from './Book';

const BooksList = ({ books, setBooks }) => {

  const handleRemoveBook = (id) => {
    setBooks(books.filter((book) => book.id !== id));
  };

  return (
    <React.Fragment>
      <div className="book-list">
        {!_.isEmpty(books) ? (
          books.map((book) => (
            <Book key={book.id} {...book} handleRemoveBook={handleRemoveBook} />
          ))
        ) : (
          <p className="message">Aucun livre disponible. Veuillez ajouter des livres.</p>
        )}
      </div>
    </React.Fragment>
  );
};

export default BooksList;
```

Dans ce fichier, nous parcourons les `books` en utilisant la méthode `map` du tableau et les passons en tant que prop au composant `Book`.

Notez que nous passons également la fonction `handleRemoveBook` en tant que prop afin de pouvoir supprimer n'importe quel livre que nous voulons.

À l'intérieur de la fonction `handleRemoveBook`, nous appelons la fonction `setBooks` en utilisant la méthode `filter` du tableau pour conserver uniquement les livres qui ne correspondent pas à l'`id` du livre fourni.

```js
const handleRemoveBook = (id) => {
    setBooks(books.filter((book) => book.id !== id));
};
```

Maintenant, si vous vérifiez l'application en visitant [http://localhost:3000/](http://localhost:3000/), vous pourrez voir le livre ajouté sur l'interface utilisateur.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/list_page.png)

Ajoutons un autre livre pour vérifier l'ensemble du flux.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/add_delete.gif)

Comme vous pouvez le voir, lorsque nous ajoutons un nouveau livre, nous sommes redirigés vers la page de liste où nous pouvons supprimer le livre. Vous pouvez voir qu'il est instantanément supprimé de l'interface utilisateur ainsi que du stockage local.

De plus, lorsque nous actualisons la page, les données ne sont pas perdues. C'est la puissance du stockage local.

## Comment modifier un livre

Maintenant, nous avons les fonctionnalités d'ajout et de suppression pour les livres. Ajoutons un moyen de modifier les livres que nous avons.

Ouvrez `Book.js` et changez le code ci-dessous :

```jsx
<Button variant="primary">Modifier</Button>{' '}
```

en ce code :

```jsx
<Button variant="primary" onClick={() => history.push(`/edit/${id}`)}>
  Modifier
</Button>{' '}
```

Ici, nous avons ajouté un gestionnaire `onClick` pour rediriger l'utilisateur vers la route `/edit/id_du_livre` lorsque nous cliquons sur le bouton de modification.

Mais nous n'avons pas accès à l'objet `history` dans le composant `Book` car la prop `history` est passée uniquement aux composants qui sont mentionnés dans `<Route />`.

Nous rendons le composant `Book` à l'intérieur du composant `BooksList`, donc nous pouvons obtenir l'accès à `history` uniquement à l'intérieur du composant `BooksList`. Ensuite, nous pouvons le passer en tant que prop au composant `Book`.

Mais au lieu de cela, React router fournit un moyen facile en utilisant le hook `useHistory`.

Importez le hook `useHistory` en haut du fichier `Book.js` :

```js
import { useHistory } from 'react-router-dom';
```

et à l'intérieur du composant `Book`, appelez le hook `useHistory`.

```js
const Book = ({
  id,
  bookname,
  author,
  price,
  quantity,
  date,
  handleRemoveBook
}) => {
  const history = useHistory();
  ...
}
```

Maintenant, nous avons accès à l'objet `history` à l'intérieur du composant `Book`.

Votre fichier `Book.js` complet ressemble maintenant à ceci :

```jsx
import React from 'react';
import { Button, Card } from 'react-bootstrap';
import { useHistory } from 'react-router-dom';

const Book = ({
  id,
  bookname,
  author,
  price,
  quantity,
  date,
  handleRemoveBook
}) => {
  const history = useHistory();

  return (
    <Card style={{ width: '18rem' }} className="book">
      <Card.Body>
        <Card.Title className="book-title">{bookname}</Card.Title>
        <div className="book-details">
          <div>Auteur : {author}</div>
          <div>Quantité : {quantity} </div>
          <div>Prix : {price} </div>
          <div>Date : {new Date(date).toDateString()}</div>
        </div>
        <Button variant="primary" onClick={() => history.push(`/edit/${id}`)}>
          Modifier
        </Button>{' '}
        <Button variant="danger" onClick={() => handleRemoveBook(id)}>
          Supprimer
        </Button>
      </Card.Body>
    </Card>
  );
};

export default Book;
```

Créez un nouveau fichier appelé `EditBook.js` à l'intérieur du dossier `components` avec le contenu suivant :

```jsx
import React from 'react';
import BookForm from './BookForm';
import { useParams } from 'react-router-dom';

const EditBook = ({ history, books, setBooks }) => {
  const { id } = useParams();
  const bookToEdit = books.find((book) => book.id === id);

  const handleOnSubmit = (book) => {
    const filteredBooks = books.filter((book) => book.id !== id);
    setBooks([book, ...filteredBooks]);
    history.push('/');
  };

  return (
    <div>
      <BookForm book={bookToEdit} handleOnSubmit={handleOnSubmit} />
    </div>
  );
};

export default EditBook;
```

Ici, pour le gestionnaire `onClick` du bouton Modifier, nous redirigeons l'utilisateur vers la route `/edit/quelque_id` – mais une telle route n'existe pas encore. Donc, créons cela d'abord.

Ouvrez `AppRouter.js` et avant la balise de fermeture de `Switch`, ajoutez deux autres routes :

```jsx
<Switch>
...
<Route
  render={(props) => (
    <EditBook {...props} books={books} setBooks={setBooks} />
  )}
  path="/edit/:id"
/>
<Route component={() => <Redirect to="/" />} />
</Switch>
```

La première Route est pour le composant `EditBook`. Ici, le chemin est défini comme `/edit/:id` où `:id` représente un identifiant aléatoire.

La deuxième Route est pour gérer toutes les autres routes qui ne correspondent à aucune des routes mentionnées.

Ainsi, si nous accédons à une route aléatoire comme `/help` ou `/contact`, nous redirigerons l'utilisateur vers la route `/` qui est le composant `BooksList`.

Votre fichier `AppRouter.js` complet ressemble maintenant à ceci :

```jsx
import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import Header from '../components/Header';
import AddBook from '../components/AddBook';
import BooksList from '../components/BooksList';
import useLocalStorage from '../hooks/useLocalStorage';

const AppRouter = () => {
  const [books, setBooks] = useLocalStorage('books', []);

  return (
    <BrowserRouter>
      <div>
        <Header />
        <div className="main-content">
          <Switch>
            <Route
              render={(props) => (
                <BooksList {...props} books={books} setBooks={setBooks} />
              )}
              path="/"
              exact={true}
            />
            <Route
              render={(props) => (
                <AddBook {...props} books={books} setBooks={setBooks} />
              )}
              path="/add"
            />
            <Route
              render={(props) => (
                <EditBook {...props} books={books} setBooks={setBooks} />
              )}
              path="/edit/:id"
            />
            <Route component={() => <Redirect to="/" />} />
          </Switch>
        </div>
      </div>
    </BrowserRouter>
  );
};

export default AppRouter;
```

Maintenant, vérifions la fonctionnalité de modification de l'application.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/edit_book.gif)

Comme vous pouvez le voir, nous sommes en mesure de modifier le livre avec succès. Comprenons comment cela fonctionne.

Tout d'abord, à l'intérieur du fichier `AppRouter.js`, nous avons une route comme celle-ci :

```jsx
<Route
  render={(props) => (
    <EditBook {...props} books={books} setBooks={setBooks} />
  )}
  path="/edit/:id"
/>
```

et à l'intérieur du fichier `Book.js`, nous avons un bouton de modification comme celui-ci :

```jsx
<Button variant="primary" onClick={() => history.push(`/edit/${id}`)}>
  Modifier
</Button>
```

Ainsi, chaque fois que nous cliquons sur le bouton Modifier pour l'un des livres, nous redirigeons l'utilisateur vers le composant `EditBook` en utilisant la méthode `history.push` en passant l'identifiant du livre à modifier.

Ensuite, à l'intérieur du composant `EditBook`, nous utilisons le hook `useParams` fourni par `react-router-dom` pour accéder à `props.params.id`.

Ainsi, les deux lignes suivantes sont identiques.

```js
const { id } = useParams();

// la ligne de code ci-dessus est identique à la ligne de code ci-dessous

const { id } = props.match.params;
```

Une fois que nous avons obtenu cet `id`, nous utilisons la méthode `find` du tableau pour trouver le livre particulier dans la liste des livres avec l'`id` fourni correspondant.

```js
const bookToEdit = books.find((book) => book.id === id);
```

et ce livre particulier que nous passons au composant `BookForm` en tant que prop `book` :

```jsx
<BookForm book={bookToEdit} handleOnSubmit={handleOnSubmit} />
```

À l'intérieur du composant `BookForm`, nous avons défini l'état comme montré ci-dessous :

```js
const [book, setBook] = useState({
  bookname: props.book ? props.book.bookname : '',
  author: props.book ? props.book.author : '',
  quantity: props.book ? props.book.quantity : '',
  price: props.book ? props.book.price : '',
  date: props.book ? props.book.date : ''
});
```

Ici, nous vérifions si la prop `book` existe. Si oui, alors nous utilisons les détails du livre passé en tant que prop, sinon nous initialisons l'état avec une valeur vide (`''`) pour chaque propriété.

Et chaque élément d'entrée a fourni une prop `value` que nous définissons à partir de l'état comme ceci :

```jsx
<Form.Control
  ...
  value={bookname}
  ...
/>
```

Mais nous pouvons améliorer un peu la syntaxe `useState` à l'intérieur du composant `BookForm`.

Au lieu de définir directement un objet pour le hook `useState`, nous pouvons utiliser l'initialisation paresseuse comme fait dans le fichier `useLocalStorage.js`.

Donc, changez le code ci-dessous :

```js
const [book, setBook] = useState({
  bookname: props.book ? props.book.bookname : '',
  author: props.book ? props.book.author : '',
  quantity: props.book ? props.book.quantity : '',
  price: props.book ? props.book.price : '',
  date: props.book ? props.book.date : ''
});
```

en ce code :

```js
const [book, setBook] = useState(() => {
  return {
    bookname: props.book ? props.book.bookname : '',
    author: props.book ? props.book.author : '',
    quantity: props.book ? props.book.quantity : '',
    price: props.book ? props.book.price : '',
    date: props.book ? props.book.date : ''
  };
});
```

Grâce à ce changement, le code de définition de l'état ne sera pas exécuté à chaque nouveau rendu de l'application. Il ne sera exécuté qu'une seule fois lorsque le composant est monté.

> Notez que le nouveau rendu du composant se produit à chaque changement d'état ou de prop.

Si vous vérifiez l'application, vous verrez que l'application fonctionne exactement comme avant sans aucun problème. Mais nous avons simplement amélioré les performances de l'application d'un petit peu.

## Comment utiliser l'API Context de React

Maintenant, nous avons terminé de construire toute la fonctionnalité de l'application. Mais si vous vérifiez le fichier `AppRouter.js`, vous verrez que chaque Route semble un peu compliquée. Cela est dû au fait que nous passons les mêmes props `books` et `setBooks` à chaque composant en utilisant le motif render props.

Nous pouvons donc utiliser l'API Context de React pour simplifier ce code.

> Notez que cette étape est facultative. Vous n'avez pas besoin d'utiliser l'API Context car nous ne passons les props qu'à un seul niveau de profondeur et le code actuel fonctionne parfaitement bien et nous n'avons pas utilisé de mauvaise approche pour passer les props.

Mais juste pour rendre le code du Routeur plus simple et pour vous donner une idée de la manière de tirer parti de la puissance de l'API Context, nous allons l'utiliser dans notre application.

Créez un nouveau fichier `BooksContext.js` à l'intérieur du dossier `context` avec le contenu suivant :

```js
import React from 'react';

const BooksContext = React.createContext();

export default BooksContext;
```

Maintenant, à l'intérieur du fichier `AppRouter.js`, importez le contexte exporté ci-dessus.

```js
import BooksContext from '../context/BooksContext';
```

et remplacez le composant `AppRouter` par le code ci-dessous :

```jsx
const AppRouter = () => {
  const [books, setBooks] = useLocalStorage('books', []);

  return (
    <BrowserRouter>
      <div>
        <Header />
        <div className="main-content">
          <BooksContext.Provider value={{ books, setBooks }}>
            <Switch>
              <Route component={BooksList} path="/" exact={true} />
              <Route component={AddBook} path="/add" />
              <Route component={EditBook} path="/edit/:id" />
              <Route component={() => <Redirect to="/" />} />
            </Switch>
          </BooksContext.Provider>
        </div>
      </div>
    </BrowserRouter>
  );
};
```

Ici, nous avons converti le motif render props en routes normales et avons ajouté l'ensemble du bloc `Switch` à l'intérieur du composant `BooksContext.Provider` comme ceci :

```jsx
<BooksContext.Provider value={{ books, setBooks }}>
 <Switch>
 ...
 </Switch>
</BooksContext.Provider>
```

Ici, pour le composant `BooksContext.Provider`, nous avons fourni une prop `value` en passant les données que nous voulons accéder à l'intérieur des composants mentionnés dans la Route.

Ainsi, chaque composant déclaré en tant que partie de Route pourra accéder aux `books` et `setBooks` via l'API Context.

Maintenant, ouvrez le fichier `BooksList.js` et supprimez les props `books` et `setBooks` qui sont déstructurées, car nous ne passons plus directement les props.

Importez `BooksContext` et `useContext` en haut du fichier :

```js
import React, { useContext } from 'react';
import BooksContext from '../context/BooksContext';
```

Et au-dessus de la fonction `handleRemoveBook`, ajoutez le code suivant :

```js
const { books, setBooks } = useContext(BooksContext);
```

Ici, nous extrayons les props `books` et `setBooks` du `BooksContext` en utilisant le hook `useContext`.

Votre fichier `BooksList.js` complet ressemblera à ceci :

```jsx
import React, { useContext } from 'react';
import _ from 'lodash';
import Book from './Book';
import BooksContext from '../context/BooksContext';

const BooksList = () => {
  const { books, setBooks } = useContext(BooksContext);

  const handleRemoveBook = (id) => {
    setBooks(books.filter((book) => book.id !== id));
  };

  return (
    <React.Fragment>
      <div className="book-list">
        {!_.isEmpty(books) ? (
          books.map((book) => (
            <Book key={book.id} {...book} handleRemoveBook={handleRemoveBook} />
          ))
        ) : (
          <p className="message">Aucun livre disponible. Veuillez ajouter des livres.</p>
        )}
      </div>
    </React.Fragment>
  );
};

export default BooksList;
```

Maintenant, apportez des modifications similaires dans le fichier `AddBook.js`.

Votre fichier `AddBook.js` complet ressemblera à ceci :

```jsx
import React, { useContext } from 'react';
import BookForm from './BookForm';
import BooksContext from '../context/BooksContext';

const AddBook = ({ history }) => {
  const { books, setBooks } = useContext(BooksContext);

  const handleOnSubmit = (book) => {
    setBooks([book, ...books]);
    history.push('/');
  };

  return (
    <React.Fragment>
      <BookForm handleOnSubmit={handleOnSubmit} />
    </React.Fragment>
  );
};

export default AddBook;
```

Notez que ici, nous utilisons toujours la déstructuration pour la prop `history`. Nous avons simplement supprimé `books` et `setBooks` de la syntaxe de déstructuration.

Maintenant, apportez des modifications similaires dans le fichier `EditBook.js`.

Votre fichier `EditBook.js` complet ressemblera à ceci :

```jsx
import React, { useContext } from 'react';
import BookForm from './BookForm';
import { useParams } from 'react-router-dom';
import BooksContext from '../context/BooksContext';

const EditBook = ({ history }) => {
  const { books, setBooks } = useContext(BooksContext);
  const { id } = useParams();
  const bookToEdit = books.find((book) => book.id === id);

  const handleOnSubmit = (book) => {
    const filteredBooks = books.filter((book) => book.id !== id);
    setBooks([book, ...filteredBooks]);
    history.push('/');
  };

  return (
    <div>
      <BookForm book={bookToEdit} handleOnSubmit={handleOnSubmit} />
    </div>
  );
};

export default EditBook;
```

Si vous vérifiez l'application, vous verrez qu'elle fonctionne exactement comme avant, mais nous utilisons maintenant l'API Context de React.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/edit_delete.gif)

> Si vous voulez comprendre l'API Context en détail, consultez [cet article](https://medium.com/swlh/what-is-context-api-in-react-and-how-to-use-it-in-react-app-dedbcdd78801?source=friends_link&sk=5ea2b1078e16173036b95c477cde369c).

### Merci d'avoir lu !

Vous pouvez trouver le code source complet de cette application dans [ce dépôt](https://github.com/myogeshchavan97/react-book-management-app).

Vous voulez apprendre toutes les fonctionnalités ES6+ en détail, y compris let et const, les promesses, diverses méthodes de promesses, la déstructuration de tableaux et d'objets, les fonctions fléchées, async/await, import et export et bien plus encore à partir de zéro ?

**Consultez mon livre [Maîtriser le JavaScript Moderne](https://modernjavascript.yogeshchavan.dev/). Ce livre couvre tous les prérequis pour apprendre React et vous aide à devenir meilleur en JavaScript et React.**

> Consultez le contenu de l'aperçu gratuit du livre [ici](https://www.freecodecamp.org/news/learn-modern-javascript/).

De plus, vous pouvez consulter mon cours **gratuit** [Introduction à React Router](https://yogeshchavan1.podia.com/react-router-introduction) pour apprendre React Router à partir de zéro.

Vous voulez rester à jour avec du contenu régulier concernant JavaScript, React, Node.js ? [Suivez-moi sur LinkedIn](https://www.linkedin.com/in/yogesh-chavan97/).

<a href="https://bit.ly/3w0DGum" target="_blank" rel="noreferrer noopener"><img src="https://gist.github.com/myogeshchavan97/98ae4f4ead57fde8d47fcf7641220b72/raw/c3e4265df4396d639a7938a83bffd570130483b1/banner.jpg"></a>