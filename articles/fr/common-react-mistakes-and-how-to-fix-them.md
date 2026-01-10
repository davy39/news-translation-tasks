---
title: 4 erreurs courantes avec React que vous pourriez commettre – et comment les
  corriger
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-06-24T17:01:44.000Z'
originalURL: https://freecodecamp.org/news/common-react-mistakes-and-how-to-fix-them
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/fix-react-code-cover-image.png
tags:
- name: clean code
  slug: clean-code
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: 4 erreurs courantes avec React que vous pourriez commettre – et comment
  les corriger
seo_desc: 'Let''s go over the most common mistakes you might be making in your React
  code right now, plus how to fix them.

  If you want to create amazing React applications, it''s essential to avoid many
  common errors along the way.

  In this article, we''ll not only...'
---

Passons en revue les erreurs les plus courantes que vous pourriez commettre dans votre code React en ce moment, ainsi que comment les corriger.

Si vous souhaitez créer des applications React incroyables, il est essentiel d'éviter de nombreuses erreurs courantes en cours de route.

Dans cet article, nous allons non seulement couvrir comment corriger vos erreurs rapidement, mais aussi vous donner quelques modèles de conception géniaux pour améliorer votre code et le rendre plus fiable à l'avenir.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Blue-and-Yellow-Photo-Fun-Job-Post--Vacancy--Announcement-Twitter-Post-2-2.gif)

## 1. Ne passez pas les variables d'état à setState dans React

Dans le code ci-dessous, nous avons une application de todo qui affiche un tableau de todos (dans `TodoList`).

Nous pouvons ajouter de nouveaux todos dans le composant `AddTodo`, ce qui met à jour le tableau `todos` dans App.

Quel est le problème avec les props que nous avons passés à `AddTodo` ?

```js
export default function App() {
  const [todos, setTodos] = React.useState([]);

  return (
    <div>
      <h1>Liste de tâches</h1>
      <TodoList todos={todos} />
      <AddTodo setTodos={setTodos} todos={todos} />
    </div>
  );
}

function AddTodo({ setTodos, todos }) {
  function handleAddTodo(event) {
    event.preventDefault();
    const text = event.target.elements.addTodo.value;
    const todo = {
      id: 4,
      text,
      done: false
    };
    const newTodos = todos.concat(todo);
    setTodos(newTodos);
  }

  return (
    <form onSubmit={handleAddTodo}>
      <input name="addTodo" placeholder="Ajouter une tâche" />
      <button type="submit">Soumettre</button>
    </form>
  );
}
```

Nous ajoutons le nouveau todo au tableau `todos` puis nous définissons l'état comme nous devrions le faire. Cela mettra à jour les todos affichés dans le composant `TodoList`.

Cependant, puisque le nouvel état est basé sur l'état précédent, nous n'avons pas besoin de passer le tableau todos.

Au lieu de cela, nous pouvons accéder à l'état précédent des todos en écrivant une fonction dans la fonction setState. Tout ce que nous retournons de cette fonction sera défini comme le nouvel état.

En d'autres termes, nous n'avons besoin de passer que la fonction `setTodos` pour mettre à jour correctement l'état :

```js
export default function App() {
  const [todos, setTodos] = React.useState([]);

  return (
    <div>
      <h1>Liste de tâches</h1>
      <TodoList todos={todos} />
      <AddTodo setTodos={setTodos} />
    </div>
  );
}

function AddTodo({ setTodos }) {
  function handleAddTodo(event) {
    event.preventDefault();
    const text = event.target.elements.addTodo.value;
    const todo = {
      id: 4,
      text,
      done: false
    };
    setTodos(prevTodos => prevTodos.concat(todo));
  }

  return (
    <form onSubmit={handleAddTodo}>
      <input name="addTodo" placeholder="Ajouter une tâche" />
      <button type="submit">Soumettre</button>
    </form>
  );
}
```

## 2. Rendez vos composants React à responsabilité unique

Dans l'application ci-dessous, nous récupérons un certain nombre d'utilisateurs à partir d'une API dans notre composant d'application, nous plaçons ces données utilisateur dans un état, puis nous les affichons dans notre interface utilisateur.

Quel est le problème avec le composant `App` ?

```js
export default function App() {
  const [users, setUsers] = React.useState([]);

  React.useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/users")
      .then((res) => res.json())
      .then((data) => {
        setUsers(data);
      });
  }, []);

  return (
    <>
      <h1>Utilisateurs</h1>
      {users.map((user) => (
        <div key={user.id}>
          <div>{user.name}</div>
        </div>
      ))}
    </>
  );
}
```

Dans notre composant, nous faisons plusieurs choses.

Nous ne faisons pas seulement de la récupération de données distantes à partir d'un serveur, mais nous gérons également l'état ainsi que l'affichage de cet état avec JSX.

Nous faisons faire plusieurs choses à notre composant. Au lieu de cela, vos composants devraient faire une seule chose et bien la faire.

C'est l'un des principes clés de conception de l'acronyme SOLID, qui énonce cinq règles pour écrire des logiciels plus fiables.

Le S dans SOLID signifie le "principe de responsabilité unique", un principe essentiel à utiliser lors de l'écriture de composants React.

Nous pouvons diviser notre composant `App` en composants et hooks séparés qui ont chacun leur propre responsabilité. Tout d'abord, nous allons extraire la récupération de données distantes vers un hook React personnalisé.

Ce hook, que nous appellerons useUserData, s'occupera de récupérer les données et de les placer dans l'état local.

```js
function useUserData() {
  const [users, setUsers] = React.useState([]);

  React.useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/users")
      .then((res) => res.json())
      .then((json) => {
        setUsers(json);
      });
  }, []);

  return users;
}
```

Après cela, nous appellerons le hook dans `App` pour accéder à notre tableau `users`.

Cependant, au lieu d'afficher directement les données utilisateur dans notre instruction return dans `App`, nous créerons un composant `User` séparé qui contiendra tout le JSX nécessaire pour afficher chaque élément de ce tableau, ainsi que les styles associés (si nous en avons).

```js
function User({ user }) {
  const styles = {
    container: {
      margin: '0 auto',
      textAlign: 'center'
    }
  };

  return (
    <div style={styles.container}>
      <div>{user.name}</div>
    </div>
  );
}

export default function App() {
  const users = useUserData();

  return (
    <>
      <h1>Utilisateurs</h1>
      {users.map((user) => (
        <User key={user.id} user={user} />
      ))}
    </>
  );
}
```

Après cette refactorisation, nos composants ont maintenant une tâche claire et individuelle à accomplir, ce qui rend notre application beaucoup plus facile à comprendre et à étendre.

## 3. Rendez vos effets secondaires à responsabilité unique

Dans notre composant `App` ci-dessous, nous récupérons à la fois les données utilisateur et les données de publication.

Lorsque l'emplacement – l'URL – de notre application change, nous récupérons à la fois les données utilisateur et les données de publication.

```js
export default function App() {
  const location = useLocation();

  function getAuthUser() {
    // récupère l'utilisateur authentifié
  }

  function getPostData() {
    // récupère les données de publication
  }

  React.useEffect(() => {
    getAuthUser();
    getPostData();
  }, [location.pathname]);

  return (
    <main>
      <Navbar />
      <Post />
    </main>
  );
}
```

Nous affichons une nouvelle publication si l'URL change, mais devons-nous la récupérer à chaque fois que l'emplacement change ?

Non.

Dans une grande partie de votre code React, vous pourriez être tenté de mettre tous vos effets secondaires dans une seule fonction useEffect. Mais faire cela viole le principe de responsabilité unique que nous venons de mentionner.

Cela peut entraîner des problèmes tels que l'exécution d'effets secondaires lorsque nous n'en avons pas besoin. N'oubliez pas de garder vos effets secondaires à une seule responsabilité également.

Pour corriger notre code, tout ce que nous avons à faire est d'appeler `getAuthUser` dans un hook useEffect séparé. Cela garantit qu'il n'est pas appelé chaque fois que le chemin de l'emplacement change, mais seulement une fois lorsque notre composant d'application est monté.

```js
export default function App() {
  const location = useLocation();

  React.useEffect(() => {
    getAuthUser();
  }, []);

  React.useEffect(() => {
    getPostData();
  }, [location.pathname]);

  return (
    <main>
      <Navbar />
      <Post />
    </main>
  );
}
```

## 4. Utilisez des ternaires au lieu de `&&` dans JSX

Supposons que nous affichons une liste de publications dans un composant dédié, `PostList`.

Il est logique de vérifier si nous avons des publications avant de les parcourir.

Puisque notre liste `posts` est un tableau, nous pouvons utiliser la propriété `.length` pour vérifier et voir si elle est une valeur truthy (supérieure à 0). Si c'est le cas, nous pouvons mapper ce tableau avec notre JSX.

Nous pouvons exprimer tout cela avec l'opérateur and `&&` :

```js
export default function PostList({ posts }) {
  return (
    <div>
      <ul>
        {posts.length &&
          posts.map((post) => <PostItem key={post.id} post={post} />)}
      </ul>
    </div>
  );
}

```

Cependant, vous pourriez être surpris par ce que nous voyons, si nous devions exécuter un tel code. Si notre tableau est vide, nous ne voyons rien – nous voyons le nombre 0 !

Quoi ? Pourquoi cela ?!

C'est un problème lié à JavaScript, car la longueur de notre tableau est 0. Parce que 0 est une valeur falsy, l'opérateur `&&` ne regarde pas le côté droit de l'expression. Il retourne simplement le côté gauche – 0.

Quel est le meilleur moyen de corriger cela et d'éviter de telles erreurs à l'avenir ?

Dans de nombreux cas, nous ne devrions pas utiliser l'opérateur and, mais plutôt utiliser un ternaire pour définir explicitement ce qui sera affiché dans le cas où la condition n'est pas remplie.

Si nous devions écrire le code suivant avec un ternaire, nous inclurions la valeur `null` dans la condition else pour nous assurer que rien n'est affiché.

```js
export default function PostList({ posts }) {
  return (
    <div>
      <ul>
        {posts.length
          ? posts.map((post) => <PostItem key={post.id} post={post} />)
          : null}
      </ul>
    </div>
  );
}
```

En utilisant des ternaires au lieu de `&&`, vous pouvez éviter de nombreux bugs ennuyeux comme celui-ci.

Merci d'avoir lu !

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : Le React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le seul cours que j'aurais souhaité avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*