---
title: Comment écrire du code React plus propre
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-04-05T20:29:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-cleaner-react-code
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/7-ways-to-write-clean-react-code.png
tags:
- name: clean code
  slug: clean-code
- name: JavaScript
  slug: javascript
- name: JSX
  slug: jsx
- name: React
  slug: react
seo_title: Comment écrire du code React plus propre
seo_desc: "As React developers, we all want to write cleaner code that is simpler\
  \ and easier to read. \nIn this guide, I've put together seven of the top ways that\
  \ you can start writing cleaner React code today to make building React projects\
  \ and reviewing your ..."
---

En tant que développeurs React, nous voulons tous écrire du code plus propre, plus simple et plus facile à lire. 

Dans ce guide, j'ai rassemblé sept des meilleures façons de commencer à écrire du code React plus propre dès aujourd'hui pour faciliter la construction de projets React et la révision de votre code.

En général, apprendre à écrire du code React plus propre vous rendra plus précieux et globalement plus heureux en tant que développeur React, alors plongeons directement dans le sujet !

## 1. Utilisez les raccourcis JSX

Comment passez-vous une valeur de true à une prop donnée ? 

Dans l'exemple ci-dessous, nous utilisons la prop `showTitle` pour afficher le titre de notre application dans un composant Navbar. 

```js
// src/App.js

export default function App() {
  return (
    <main>
      <Navbar showTitle={true} />
    </main>
  );
}

function Navbar({ showTitle }) {
  return (
    <div>
      {showTitle && <h1>My Special App</h1>}
    </div>
  )
}
```

Devons-nous explicitement définir `showTitle` sur le booléen `true` ? Non ! Un raccourci rapide à retenir est que toute prop fournie à un composant a une valeur par défaut de true. 

Ainsi, si nous ajoutons la prop `showTitle` à Navbar, notre élément de titre sera affiché :

```js
// src/App.js

export default function App() {
  return (
    <main>
      <Navbar showTitle />
    </main>
  );
}

function Navbar({ showTitle }) {
  return (
    <div>
      {showTitle && <h1>My Special App</h1>} // titre affiché !
    </div>
  )
}
```

Un autre raccourci utile à retenir concerne le passage des props de type chaîne. Lorsque vous passez une valeur de prop qui est une chaîne, vous n'avez pas besoin de l'envelopper dans des accolades. 

Si nous définissons le titre de notre Navbar avec la prop `title`, nous pouvons simplement inclure sa valeur entre guillemets doubles :

```js
// src/App.js

export default function App() {
  return (
    <main>
      <Navbar title="My Special App" />
    </main>
  );
}

function Navbar({ title }) {
  return (
    <div>
      <h1>{title}</h1>
    </div>
  )
}
```

## 2. Déplacez le code non lié dans un composant séparé

Arguablement, la manière la plus facile et la plus importante d'écrire du code React plus propre est de bien maîtriser l'abstraction de notre code dans des composants React séparés. 

Examinons l'exemple ci-dessous. Que fait notre code ? 

Notre application affiche un composant Navbar. Nous itérons sur un tableau de posts avec `.map()` et affichons leur titre sur la page. 

```js
// src/App.js

export default function App() {
  const posts = [
    {
      id: 1,
      title: "How to Build YouTube with React"
    },
    {
      id: 2,
      title: "How to Write Your First React Hook"
    }
  ];

  return (
    <main>
      <Navbar title="My Special App" />
      <ul>
        {posts.map(post => (
          <li key={post.id}>
            {post.title}
          </li>
        ))}
      </ul>
    </main>
  );
}

function Navbar({ title }) {
  return (
    <div>
      <h1>{title}</h1>
    </div>
  );
}

```

Comment pouvons-nous rendre cela plus propre ? 

Pourquoi ne pas abstraire le code sur lequel nous itérons – nos posts – et les afficher dans un composant séparé, que nous appellerons FeaturedPosts. 

Faisons cela et regardons le résultat :

```js
// src/App.js

export default function App() {
 return (
    <main>
      <Navbar title="My Special App" />
      <FeaturedPosts />
    </main>
  );
}

function Navbar({ title }) {
  return (
    <div>
      <h1>{title}</h1>
    </div>
  );
}

function FeaturedPosts() {
  const posts = [
    {
      id: 1,
      title: "How to Build YouTube with React"
    },
    {
      id: 2,
      title: "How to Write Your First React Hook"
    }
  ];

  return (
    <ul>
      {posts.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  );
}

```

Comme vous pouvez le voir, nous pouvons maintenant simplement regarder notre composant App. En lisant les noms des composants qu'il contient, Navbar et FeaturedPosts, nous voyons exactement ce que notre application affiche. 

## 3. Créez des fichiers séparés pour chaque composant

En partant de notre exemple précédent, nous incluons tous nos composants dans un seul fichier, le fichier app.js. 

De la même manière que nous abstraisons le code dans des composants séparés pour rendre notre application plus lisible, pour rendre les fichiers de notre application plus lisibles, nous pouvons mettre chaque composant que nous avons dans un fichier séparé. 

Cela nous aide à nouveau à séparer les préoccupations dans notre application. Cela signifie que chaque fichier est responsable d'un seul composant et qu'il n'y a pas de confusion sur l'origine d'un composant si nous voulons le réutiliser dans notre application :

```js
// src/App.js
import Navbar from './components/Navbar.js';
import FeaturedPosts from './components/FeaturedPosts.js';

export default function App() {
  return (
    <main>
      <Navbar title="My Special App" />
      <FeaturedPosts />
    </main>
  );
}
```

```js
// src/components/Navbar.js

export default function Navbar({ title }) {
  return (
    <div>
      <h1>{title}</h1>
    </div>
  );
}
```

```js
// src/components/FeaturedPosts.js

export default function FeaturedPosts() {
  const posts = [
    {
      id: 1,
      title: "How to Build YouTube with React"
    },
    {
      id: 2,
      title: "How to Write Your First React Hook"
    }
  ];

  return (
    <ul>
      {posts.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  );
}

```

De plus, en incluant chaque composant individuel dans son propre fichier, nous évitons qu'un fichier ne devienne trop encombré. Nous pourrions facilement voir notre fichier app.js devenir très grand si nous voulions ajouter tous nos composants dans ce fichier. 

## 4. Déplacez les fonctionnalités partagées dans des hooks React

En regardant notre composant FeaturedPosts, disons que, au lieu d'afficher des données de posts statiques, nous voulons récupérer nos données de posts depuis une API. 

Nous pourrions le faire avec l'API fetch. Vous pouvez voir le résultat ci-dessous :

```js
// src/components/FeaturedPosts.js

import React from 'react';

export default function FeaturedPosts() {
  const [posts, setPosts] = React.useState([]);  	
    
  React.useEffect(() => {
    fetch('https://jsonplaceholder.typicode.com/posts')
      .then(res => res.json())
      .then(data => setPosts(data));
  }, []);

  return (
    <ul>
      {posts.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  );
}
```

Cependant, que se passerait-il si nous voulions effectuer cette requête de données dans plusieurs composants ? 

Disons qu'en plus d'un composant FeaturedPosts, nous voulions créer un composant appelé simplement Posts avec les mêmes données. Nous devrions copier la logique que nous avons utilisée pour récupérer nos données et la coller également dans ce composant. 

Pour éviter d'avoir à faire cela, pourquoi ne pas simplement utiliser un nouveau hook React que nous pourrions appeler `useFetchPosts` :

```js
// src/hooks/useFetchPosts.js

import React from 'react';

export default function useFetchPosts() {
  const [posts, setPosts] = React.useState([]);  	
    
  React.useEffect(() => {
    fetch('https://jsonplaceholder.typicode.com/posts')
      .then(res => res.json())
      .then(data => setPosts(data));
  }, []);

  return posts;
}
```

Une fois que nous avons créé ce hook dans un dossier dédié 'hooks', nous pouvons le réutiliser dans les composants que nous souhaitons, y compris notre composant FeaturedPosts :

```js
// src/components/FeaturedPosts.js

import useFetchPosts from '../hooks/useFetchPosts.js';

export default function FeaturedPosts() {
  const posts = useFetchPosts()

  return (
    <ul>
      {posts.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  );
}
```

## 5. Retirez autant de JavaScript que possible de votre JSX

Une autre méthode très utile, mais souvent négligée, pour nettoyer nos composants est de retirer autant de JavaScript que possible de notre JSX. 

Examinons l'exemple ci-dessous :

```js
// src/components/FeaturedPosts.js

import useFetchPosts from '../hooks/useFetchPosts.js';

export default function FeaturedPosts() {
  const posts = useFetchPosts()

  return (
    <ul>
      {posts.map((post) => (
        <li onClick={event => {
          console.log(event.target, 'clicked!');
        }} key={post.id}>{post.title}</li>
      ))}
    </ul>
  );
}
```

Nous essayons de gérer un événement de clic sur l'un de nos posts. Vous pouvez voir que notre JSX devient beaucoup plus difficile à lire. Étant donné que notre fonction est incluse en tant que fonction en ligne, elle obscurcit le but de ce composant, ainsi que ses fonctions associées. 

Que pouvons-nous faire pour corriger cela ? Nous pouvons extraire la fonction en ligne, connectée à `onClick`, dans un gestionnaire séparé, auquel nous pouvons donner un nom approprié comme `handlePostClick`. 

Une fois que nous l'avons fait, notre JSX redevient lisible :

```js
// src/components/FeaturedPosts.js

import useFetchPosts from '../hooks/useFetchPosts.js';

export default function FeaturedPosts() {
  const posts = useFetchPosts()
  
  function handlePostClick(event) {
    console.log(event.target, 'clicked!');   
  }

  return (
    <ul>
      {posts.map((post) => (
        <li onClick={handlePostClick} key={post.id}>{post.title}</li>
      ))}
    </ul>
  );
}
```

## 6. Formatez les styles en ligne pour un code moins encombré

Un modèle courant pour les développeurs React est d'écrire des styles en ligne dans leur JSX. Mais une fois de plus, cela rend notre code plus difficile à lire et plus difficile à écrire du JSX supplémentaire :

```js
// src/App.js

export default function App() {
  return (
    <main style={{ textAlign: 'center' }}>
      <Navbar title="My Special App" />
    </main>
  );
}

function Navbar({ title }) {
  return (
    <div style={{ marginTop: '20px' }}>
      <h1 style={{ fontWeight: 'bold' }}>{title}</h1>
    </div>
  )
}
```

Nous voulons appliquer ce concept de séparation des préoccupations à nos styles JSX en déplaçant nos styles en ligne vers une feuille de style CSS, que nous pouvons importer dans n'importe quel composant que nous souhaitons. 

Une alternative pour réécrire vos styles en ligne est de les organiser en objets. Vous pouvez voir à quoi ressemblerait un tel modèle ci-dessous :

```js
// src/App.js

export default function App() {
  const styles = {
    main: { textAlign: "center" }
  };

  return (
    <main style={styles.main}>
      <Navbar title="My Special App" />
    </main>
  );
}

function Navbar({ title }) {
  const styles = {
    div: { marginTop: "20px" },
    h1: { fontWeight: "bold" }
  };

  return (
    <div style={styles.div}>
      <h1 style={styles.h1}>{title}</h1>
    </div>
  );
}
```

## 7. Réduisez le prop drilling avec le contexte React

Un autre modèle essentiel à employer pour vos projets React (surtout si vous avez des propriétés communes que vous souhaitez réutiliser dans vos composants, et que vous vous retrouvez à écrire beaucoup de props en double) est d'utiliser le contexte React. 

Par exemple, si nous voulons partager des données utilisateur dans plusieurs composants, au lieu de props répétées (un modèle appelé prop drilling), nous pourrions utiliser la fonctionnalité de contexte intégrée dans la bibliothèque React. 

Dans notre cas, si nous voulons réutiliser les données utilisateur dans nos composants Navbar et FeaturedPosts, tout ce que nous devons faire est d'envelopper toute notre application dans un composant fournisseur. 

Ensuite, nous pouvons transmettre les données utilisateur sur la prop value et consommer ce contexte dans nos composants individuels avec l'aide du hook `useContext` :

```js
// src/App.js

import React from "react";

const UserContext = React.createContext();

export default function App() {
  const user = { name: "Reed" };

  return (
    <UserContext.Provider value={user}>
      <main>
        <Navbar title="My Special App" />
        <FeaturedPosts />
      </main>
    </UserContext.Provider>
  );
}

// src/components/Navbar.js

function Navbar({ title }) {
  const user = React.useContext(UserContext);

  return (
    <div>
      <h1>{title}</h1>
      {user && <a href="/logout">Logout</a>}
    </div>
  );
}

// src/components/FeaturedPosts.js

function FeaturedPosts() {
  const posts = useFetchPosts();
  const user = React.useContext(UserContext);

  if (user) return null;

  return (
    <ul>
      {posts.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  );
}
```

## Conclusion

J'espère que vous trouverez ce guide utile lorsque vous essayez d'améliorer votre propre code React pour le rendre plus propre, plus facile à lire et, en fin de compte, plus agréable pour créer vos projets React.

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : The React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*