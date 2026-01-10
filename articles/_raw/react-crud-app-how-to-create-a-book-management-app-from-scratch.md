---
title: React CRUD App Tutorial – How to Build a Book Management App in React from
  Scratch
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
seo_title: null
seo_desc: "In this article, you will build a Book Management App in React from scratch.\
  \ \nBy creating this app, you will learn:\n\nHow to perform CRUD operations\nHow\
  \ to use React Router for navigation between routes\nHow to use React Context API\
  \ to pass data across..."
---

In this article, you will build a Book Management App in React from scratch. 

By creating this app, you will learn:

1. How to perform CRUD operations
2. How to use React Router for navigation between routes
3. How to use React Context API to pass data across routes
4. How to create a Custom Hook in React
5. How to store data in local storage to persist it even after page refresh
6. How to manage data stored in local storage using a custom hook

and much more.

We will be using React Hooks to build this application. So if you're new to React Hooks, check out my [Introduction to React Hooks](https://levelup.gitconnected.com/an-introduction-to-react-hooks-50281fd961fe?source=friends_link&sk=89baff89ec8bc637e7c13b7554904e54) article to learn the basics.

> Want to learn Redux from the absolute beginning and build a food ordering app from scratch? Check out the [Mastering Redux](https://master-redux.yogeshchavan.dev/) course.

## Initial Setup

Create a new project using `create-react-app`:

```js
npx create-react-app book-management-app

```

Once the project is created, delete all files from the `src` folder and create `index.js` and `styles.scss` files inside the `src` folder. Also, create `components`,  `context`, `hooks` and  `router` folders inside the `src` folder.

Install the necessary dependencies:

```js
yarn add bootstrap@4.6.0 lodash@4.17.21 react-bootstrap@1.5.2 node-sass@4.14.1 react-router-dom@5.2.0 uuid@8.3.2

```

Open `styles.scss` and add the contents from [here](https://github.com/myogeshchavan97/react-book-management-app/blob/master/src/styles.scss) inside it.

## How to Create the Initial Pages

Create a new file `Header.js` inside the `components` folder with the following content:

```jsx
import React from 'react';
import { NavLink } from 'react-router-dom';

const Header = () => {
  return (
    <header>
      <h1>Book Management App</h1>
      <hr />
      <div className="links">
        <NavLink to="/" className="link" activeClassName="active" exact>
          Books List
        </NavLink>
        <NavLink to="/add" className="link" activeClassName="active">
          Add Book
        </NavLink>
      </div>
    </header>
  );
};

export default Header;

```

Here, we've added two navigation links using the `NavLink` component of `react-router-dom`: one to see a list of all the books, and the other to add a new book.

We're using `NavLink` instead of the anchor tag ( `<a />`) so the page will not refresh when a user clicks on any of the links.

Create a new file called `BooksList.js` inside the `components` folder with the following content:

```js
import React from 'react';

const BooksList = () => {
  return <h2>List of books</h2>;
};

export default BooksList;

```

Create a new file called `AddBook.js` inside the `components` folder with the following content:

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

In this file, we're displaying a `BookForm` component (which we're yet to create). 

For the `BookForm` component, we're passing the `handleOnSubmit` method so we can do some processing later once we submit the form.

Now, create a new file `BookForm.js` inside the `components` folder with the following content:

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
      errorMsg = 'Please fill out all the fields.';
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
          <Form.Label>Book Name</Form.Label>
          <Form.Control
            className="input-control"
            type="text"
            name="bookname"
            value={bookname}
            placeholder="Enter name of book"
            onChange={handleInputChange}
          />
        </Form.Group>
        <Form.Group controlId="author">
          <Form.Label>Book Author</Form.Label>
          <Form.Control
            className="input-control"
            type="text"
            name="author"
            value={author}
            placeholder="Enter name of author"
            onChange={handleInputChange}
          />
        </Form.Group>
        <Form.Group controlId="quantity">
          <Form.Label>Quantity</Form.Label>
          <Form.Control
            className="input-control"
            type="number"
            name="quantity"
            value={quantity}
            placeholder="Enter available quantity"
            onChange={handleInputChange}
          />
        </Form.Group>
        <Form.Group controlId="price">
          <Form.Label>Book Price</Form.Label>
          <Form.Control
            className="input-control"
            type="text"
            name="price"
            value={price}
            placeholder="Enter price of book"
            onChange={handleInputChange}
          />
        </Form.Group>
        <Button variant="primary" type="submit" className="submit-btn">
          Submit
        </Button>
      </Form>
    </div>
  );
};

export default BookForm;

```

Let's understand what we're doing here.

Initially, we've defined a state as an object using the `useState` hook to store all the entered details like this:

```js
const [book, setBook] = useState({
    bookname: props.book ? props.book.bookname : '',
    author: props.book ? props.book.author : '',
    quantity: props.book ? props.book.quantity : '',
    price: props.book ? props.book.price : '',
    date: props.book ? props.book.date : ''
  });

```

As we'll be using the same `BookForm` component to add and edit the book, we're first checking if the `book` prop is passed or not using the ternary operator.

If the prop is passed, we're setting it to the passed value otherwise an empty string (`''`).

> Don't worry if it looks complicated now. You will understand it better once we build some initial functionality.

Then we've added a state for displaying an error message and we've used ES6 destructuring syntax to refer each of the property inside the state like this:

```js
const [errorMsg, setErrorMsg] = useState('');
const { bookname, author, price, quantity } = book;

```

From the `BookForm` component, we're returning a Form where we enter book name, book author, quantity, and price. We're using the [react-bootstrap](https://react-bootstrap.github.io/) framework to display the form in a nice format.

Each input field has added an `onChange` handler which calls the `handleInputChange` method.

Inside the `handleInputChange` method, we've added a switch statement to change the value of the state based on which input field is changed.

When we type anything in the `quantity` input field, `event.target.name` will be `quantity` so the first switch case will match. Inside that switch case, we're checking to see if the entered value is an integer without a decimal point.

If yes, then only do we update the state as shown below:

```js
if (value === '' || parseInt(value) === +value) {
  setBook((prevState) => ({
    ...prevState,
    [name]: value
  }));
}

```

So the user is not able to enter any decimal value for the quantity input field.

For the `price` switch case, we're checking for a decimal number with only two digits after the decimal point. So we've added a regular expression check that looks like this: `value.match(/^\d{1,}(\.\d{0,2})?$/)`.

If the price value matches with the regular expression only then do we update the state.

**Note:** For both the `quantity` and `price` switch cases, we're also checking for empty values like this: `value === ''`. This is to allow the user to entirely delete the entered value if they need to.

Without that check, the user will not be able to able to delete the entered value by pressing `Ctrl + A + Delete`.

For all other input fields, the default switch case will be executed which will update the state based on the user's entered value.

Next, once we submit the form, the `handleOnSubmit` method will be called.

Inside this method, we're first checking if the user has entered all the details using the `every` array method:

```js
const allFieldsFilled = values.every((field) => {
  const value = `${field}`.trim();
  return value !== '' && value !== '0';
});

```

The `every` array method is one of the most useful array methods in JavaScript. 

> Check out [my article here](https://www.freecodecamp.org/news/complete-introduction-to-the-most-useful-javascript-array-methods/) to learn about the most useful JavaScript array methods along with their browser support.

If all the values are filled in, then we're creating an object with all the filled in values. We're also calling the `handleOnSubmit` method by passing book as an argument, otherwise we're setting an error message. 

The `handleOnSubmit` method is passed as a prop from the  `AddBook` component.

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
  errorMsg = 'Please fill out all the fields.';
}

```

Note that to create a unique ID we're calling the `uuidv4()` method from the [uuid](https://www.npmjs.com/package/uuid) npm package.

Now, create a new file `AppRouter.js` inside the `router` folder with the following content:

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

Here, we have set up routing for various components like `BooksList` and `AddBook` using the `react-router-dom` library.

> If you're new to React Router, Check out my free [React Router Introduction](https://yogeshchavan1.podia.com/react-router-introduction) course.

Now, open the `src/index.js` file and add the following contents inside it:

```js
import React from 'react';
import ReactDOM from 'react-dom';
import AppRouter from './router/AppRouter';
import 'bootstrap/dist/css/bootstrap.min.css';
import './styles.scss';

ReactDOM.render(<AppRouter />, document.getElementById('root'));

```

Now, start the React App by running the following command from the terminal:

```js
yarn start

```

You will see the following screen when you access the application at [http://localhost:3000/](http://localhost:3000/).

![Image](https://www.freecodecamp.org/news/content/images/2021/04/initial_screen.gif)

![Image](https://www.freecodecamp.org/news/content/images/2021/04/add_book.gif)

As you can see, we're correctly able to add the book and display it on the console.

But instead of logging into the console, let's add it to local storage.

## How to Create a Custom Hook for Local Storage

Local storage is amazing. It allows us to easily store application data in the browser and is an alternative to cookies for storing data.

The advantage of using local storage is that the data will be saved permanently in the browser cache until we manually delete it so we can access it even after refreshing the page. As you might know, data stored in the React state will be lost once we refresh the page.

There are many use cases for local storage, and one of them is to store shopping cart items so they will not be deleted even if we refresh the page.

To add data to local storage, we use the `setItem` method by providing a key and value:

```js
localStorage.setItem(key, value)

```

> Both the key and value have to be a string. But we can store the JSON object also by using the `JSON.stringify` method.

To learn about local storage and its various applications in detail, check out [this article](https://javascript.plainenglish.io/everything-you-need-to-know-about-html5-local-storage-and-session-storage-479c63415c0a?source=friends_link&sk=f429aa5008683a3b0359db43f976efb3).

Create a new file `useLocalStorage.js` inside the `hooks` folder with the following content:

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

Here, we've used a `useLocalStorage` hook that accepts a `key` and `initialValue`.

For declaring state using the `useState` hook, we're using [lazy initialization](https://reactjs.org/docs/hooks-reference.html#lazy-initial-state).

So the code inside the function passed to `useState` will be executed only once, even if the `useLocalStorage` hook is called multiple times on every re-render of the application.

So initially we're checking to see if there is any value in local storage with the provided `key` and we return the value by parsing it using the `JSON.parse` method:

```js
try {
  const localValue = window.localStorage.getItem(key);
  return localValue ? JSON.parse(localValue) : initialValue;
} catch (error) {
  return initialValue;
}

```

Then later, if there is any change in the `key` or `value`, we'll update the local storage:

```js
useEffect(() => {
    window.localStorage.setItem(key, JSON.stringify(value));
}, [key, value]);

return [value, setValue];

```

Then we're returning the `value` stored in local storage and `setValue` function which we will call to update the localStorage data.

## How to Use the Local Storage Hook

Now, let's use this `useLocalStorage` hook so we can add or remove data from local storage.

Open the `AppRouter.js` file and use the `useLocalStorage` hook inside the component:

```js
import useLocalStorage from '../hooks/useLocalStorage';

const AppRouter = () => {
 const [books, setBooks] = useLocalStorage('books', []);
 
 return (
  ...
 )
}

```

Now, we need to pass the `books` and `setBooks` as props to the `AddBook` component so we can add the book to local storage.

So change the route from this code:

```jsx
<Route component={AddBook} path="/add" />

```

to the below code:

```jsx
<Route
  render={(props) => (
    <AddBook {...props} books={books} setBooks={setBooks} />
  )}
  path="/add"
/>

```

Here, we're using the render props pattern to pass the default props passed by React router along with the `books` and `setBooks`.

> Check out my free [React Router Introduction](https://yogeshchavan1.podia.com/react-router-introduction) course to better understand this render props pattern and the importance of using the `render` keyword instead of `component`.

Your entire `AppRouter.js` file will look like this now:

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

Now open `AddBook.js` and replace its content with the following code:

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

First, we're using ES6 destructuring syntax to access the `history`, `books` and `setBooks` props into the component.

The `history` prop is automatically passed by React Router to every component mentioned in the `<Route />`. We're passing the `books` and `setBooks` props from the `AppRouter.js` file.

We're storing all the added books in an array. Inside the `handleOnSubmit` method, we're calling the `setBooks` function by passing an array by adding a newly added book first and then spreading all the books already added in the `books` array as shown below:

```js
setBooks([book, ...books]);

```

Here, I'm adding the newly added `book` first and then spreading the already added `books` because I want the latest book to be displayed first when we display the list of books later.

But you can change the order if you want like this:

```js
setBooks([...books, book]);

```

This will add the newly added book at the end of all the already added books.

We're able to use spread operator because we know that `books` is an array (as we have initialized it to an empty array `[]` in `AppRouter.js` file as shown below):

```js
 const [books, setBooks] = useLocalStorage('books', []);

```

Then once the book is added to local storage by calling the `setBooks` method, inside the `handleOnSubmit` method we're redirecting the user to the `Books List` page using `history.push` method:

```js
history.push('/');

```

Now, let's check If we're able to save the books to local storage or not.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/added_local_storage.gif)

As you can see, the book is correctly getting added to local storage (and you can confirm this in the applications tab of Chrome dev tools).

## How to Display Added Books on the UI

Now, let's display the added books on the UI under the `Books List` menu.

Open `AppRouter.js` and pass the `books` and `setBooks` as props to the `BooksList` component.

Your `AppRouter.js` file will look like this now:

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

Here, we've just changed the first Route related to the `BooksList` component.

Now, create a new file `Book.js` inside the `components` folder with the following content:

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
          <div>Author: {author}</div>
          <div>Quantity: {quantity} </div>
          <div>Price: {price} </div>
          <div>Date: {new Date(date).toDateString()}</div>
        </div>
        <Button variant="primary">Edit</Button>{' '}
        <Button variant="danger" onClick={() => handleRemoveBook(id)}>
          Delete
        </Button>
      </Card.Body>
    </Card>
  );
};

export default Book;

```

Now, open the `BooksList.js` file and replace its contents with the following code:

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
          <p className="message">No books available. Please add some books.</p>
        )}
      </div>
    </React.Fragment>
  );
};

export default BooksList;

```

In this file, we're looping over the `books` using the array `map` method and passing them as a prop to the `Book` component.

Note that we're also passing the `handleRemoveBook` function as a prop so we will be able to delete any book we want.

Inside the `handleRemoveBook` function, we're calling the `setBooks` function by using the array `filter` method to keep only books that do not match with the provided book `id`.

```js
const handleRemoveBook = (id) => {
    setBooks(books.filter((book) => book.id !== id));
};

```

Now, if you check the application by visiting [http://localhost:3000/](http://localhost:3000/), you will be able to see the added book on the UI.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/list_page.png)

Let's add another book to verify the entire flow.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/add_delete.gif)

As you can see, when we add a new book, we're getting redirected to the list page where we're able to delete the book. You can see that it's instantly deleted from the UI as well as from local storage.

Also when we refresh the page the data does not get lost. That's the power of local storage.

## How to Edit a Book

Now we have add and delete functionality for the books. Let's add a way to edit the books we have.

Open `Book.js` and change the below code:

```jsx
<Button variant="primary">Edit</Button>{' '}

```

to this code:

```jsx
<Button variant="primary" onClick={() => history.push(`/edit/${id}`)}>
  Edit
</Button>{' '}

```

Here, we've added an `onClick` handler to redirect the user to the `/edit/id_of_the_book` route when we click on the edit button.

But we don't have access to the `history` object in the `Book` component because the `history` prop is passed only to the components which are mentioned in the `<Route />`.

We're rendering the `Book` component inside the `BooksList` component so we can get access to `history` only inside the `BooksList` component. Then we can pass it as a prop to the `Book` component.

But instead of that, React router provides an easy way using the `useHistory` hook.

Import the `useHistory` hook at the top of the `Book.js` file:

```js
import { useHistory } from 'react-router-dom';

```

and inside the `Book` component, call the `useHistory` hook.

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

Now we have access to the `history` object inside the `Book` component.

Your entire `Book.js` file looks like this now:

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
          <div>Author: {author}</div>
          <div>Quantity: {quantity} </div>
          <div>Price: {price} </div>
          <div>Date: {new Date(date).toDateString()}</div>
        </div>
        <Button variant="primary" onClick={() => history.push(`/edit/${id}`)}>
          Edit
        </Button>{' '}
        <Button variant="danger" onClick={() => handleRemoveBook(id)}>
          Delete
        </Button>
      </Card.Body>
    </Card>
  );
};

export default Book;

```

Create a new file called `EditBook.js` inside the `components` folder with the following content:

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

Here, for the `onClick` handler of the Edit button, we're redirecting the user to the `/edit/some_id` route – but such a route does not exist yet. So let's create that first.

Open `AppRouter.js` and before the ending tag of `Switch` add two more routes:

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

The first Route is for the `EditBook` component. Here, the path is defined as `/edit/:id` where `:id` represents any random id.

The second Route is to handle all other routes that do not match with any of the routes mentioned.

So if we access any random route like `/help` or `/contact` then we'll redirect the user to the `/` route which is the `BooksList` component.

Your entire `AppRouter.js` file looks like this now:

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

Now, let's check the edit functionality of the app.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/edit_book.gif)

As you can see, we're successfully able to edit the book. Let's understand how this works.

First, inside the `AppRouter.js` file we have a route like this:

```jsx
<Route
  render={(props) => (
    <EditBook {...props} books={books} setBooks={setBooks} />
  )}
  path="/edit/:id"
/>

```

and inside the `Book.js` file, we have an edit button like this:

```jsx
<Button variant="primary" onClick={() => history.push(`/edit/${id}`)}>
  Edit
</Button>

```

So whenever we're clicking on the Edit button for any of the books, we're redirecting the user to the `EditBook` component using the `history.push` method by passing the id of the book to be edited.

Then inside the `EditBook` component, we're using the `useParams` hook provided by `react-router-dom` to access the `props.params.id`.

So the below two lines are identical.

```js
const { id } = useParams();

// the above line of code is same as the below code

const { id } = props.match.params;

```

Once we've gotten that `id`, we're using the array `find` method to find out the particular book from the list of books with the matching provided `id`.

```js
const bookToEdit = books.find((book) => book.id === id);

```

and this particular book we're passing to the `BookForm` component as a `book` prop:

```jsx
<BookForm book={bookToEdit} handleOnSubmit={handleOnSubmit} />

```

Inside the `BookForm` component, we've defined the state as shown below:

```js
const [book, setBook] = useState({
  bookname: props.book ? props.book.bookname : '',
  author: props.book ? props.book.author : '',
  quantity: props.book ? props.book.quantity : '',
  price: props.book ? props.book.price : '',
  date: props.book ? props.book.date : ''
});

```

Here, we're checking  to see if the `book` prop exists. If yes, then we're using the details of the book passed as a prop, otherwise we're initializing the state with an empty value (`''`)  for each property.

And each of the input elements has provided a `value` prop which we're setting from the state like this:

```jsx
<Form.Control
  ...
  value={bookname}
  ...
/>

```

But we can improve a bit on the `useState` syntax inside the `BookForm` component.

Instead of directly setting an object for the `useState` hook, we can use lazy initialization as done in the `useLocalStorage.js` file.

So change the below code:

```js
const [book, setBook] = useState({
  bookname: props.book ? props.book.bookname : '',
  author: props.book ? props.book.author : '',
  quantity: props.book ? props.book.quantity : '',
  price: props.book ? props.book.price : '',
  date: props.book ? props.book.date : ''
});

```

to this code:

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

Because of this change, the code for setting state will not be executed on every re-render of the application. It will just be executed once when the component is mounted.

> Note that the re-rendering of the component happens on every state or prop change.

If you check the application, you will see that the application works exactly as before without any issue. But we've just improved the application performance by a little bit.

## How to use React's Context API

Now we're done building out the entire application's functionality. But if you check the `AppRouter.js` file, you will see that each Route looks a bit complicated. This is because we're passing the same `books` and `setBooks` props to each of the components by using the render props pattern.

So we can use the React Context API to simplify this code.

> Note that this is an optional step. You don't need to use Context API as we're passing the props only one level deep and the current code is working perfectly fine and we've not used any wrong approach for passing the props.

But just to make the Router code simpler and to give you an idea about how to leverage the power of Context API, we will use it in our application.

Create a new file `BooksContext.js` inside the `context` folder with the following content:

```js
import React from 'react';

const BooksContext = React.createContext();

export default BooksContext;

```

Now, inside the `AppRouter.js` file, import the above exported context.

```js
import BooksContext from '../context/BooksContext';

```

and replace the `AppRouter` component with the below code:

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

Here, we've converted the render props pattern back to the normal routes and added the entire `Switch` block inside the `BooksContext.Provider` component like this:

```jsx
<BooksContext.Provider value={{ books, setBooks }}>
 <Switch>
 ...
 </Switch>
</BooksContext.Provider>

```

Here, for the `BooksContext.Provider` component, we've provided a `value` prop by passing the data we want to access inside the components mentioned in the Route.

So now, every component declared as a part of Route will be able to access the `books` and `setBooks` via the Context API.

Now, open the `BooksList.js` file and remove the `books` and `setBooks` props which are destructured, as we are no longer directly passing the props.

Import the `BooksContext` and `useContext` at the top of the file:

```js
import React, { useContext } from 'react';
import BooksContext from '../context/BooksContext';

```

And above the `handleRemoveBook` function, add the following code:

```js
const { books, setBooks } = useContext(BooksContext);

```

Here, we're taking out the `books` and `setBooks` props from the `BooksContext` using the `useContext` hook.

Your entire `BooksList.js` file will look like this:

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
          <p className="message">No books available. Please add some books.</p>
        )}
      </div>
    </React.Fragment>
  );
};

export default BooksList;

```

Now, make similar changes in the `AddBook.js` file.

Your entire `AddBook.js` file will look like this:

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

Note that here, we're still using the destructuring for the `history` prop. We've only removed the `books` and `setBooks` from the destructuring syntax.

Now, make similar changes in the `EditBook.js` file.

Your entire `EditBook.js` file will look like this:

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

If you check the application, you will see that it works exactly as before but we're now using React Context API.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/edit_delete.gif)

> If you want to understand the Context API in detail, check out my [this article](https://medium.com/swlh/what-is-context-api-in-react-and-how-to-use-it-in-react-app-dedbcdd78801?source=friends_link&sk=5ea2b1078e16173036b95c477cde369c).

### Thanks for reading!

You can find the complete source code for this application in [this repository](https://github.com/myogeshchavan97/react-book-management-app).

Want to learn all ES6+ features in detail including let and const, promises, various promise methods, array and object destructuring, arrow functions, async/await, import and export and a whole lot more from scratch?

**Check out my [Mastering Modern JavaScript](https://modernjavascript.yogeshchavan.dev/) book. This book covers all the pre-requisites for learning React and helps you to become better at JavaScript and React.**

> Check out free preview contents of the book [here](https://www.freecodecamp.org/news/learn-modern-javascript/).

Also, you can check out my **free** [Introduction to React Router](https://yogeshchavan1.podia.com/react-router-introduction) course to learn React Router from scratch.

Want to stay up to date with regular content regarding JavaScript, React, Node.js? [Follow me on LinkedIn](https://www.linkedin.com/in/yogesh-chavan97/).

<a href="https://bit.ly/3w0DGum" target="_blank" rel="noreferrer noopener"><img src="https://gist.github.com/myogeshchavan97/98ae4f4ead57fde8d47fcf7641220b72/raw/c3e4265df4396d639a7938a83bffd570130483b1/banner.jpg"></a>

