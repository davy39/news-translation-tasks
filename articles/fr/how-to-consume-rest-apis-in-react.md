---
title: Comment consommer des API REST dans React – un guide pour débutants
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-06-21T15:35:38.000Z'
originalURL: https://freecodecamp.org/news/how-to-consume-rest-apis-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/cover-template-2.jpg
tags:
- name: axios
  slug: axios
- name: React
  slug: react
- name: REST API
  slug: rest-api
seo_title: Comment consommer des API REST dans React – un guide pour débutants
seo_desc: 'React is a popular frontend library that developers use to create applications.
  And you will need to integrate APIs into your React application at some point if
  you want to build production-ready apps.

  Every developer who wants to build modern, robus...'
---

React est une bibliothèque frontend populaire que les développeurs utilisent pour créer des applications. Et vous devrez intégrer des API dans votre application React à un moment donné si vous souhaitez construire des applications prêtes pour la production.

Tout développeur qui souhaite construire des applications web modernes et robustes avec React doit comprendre comment consommer des API pour récupérer des données dans leurs applications React.

Dans ce guide pour débutants, vous apprendrez comment consommer une API RESTful dans React, y compris la récupération, la suppression et l'ajout de données. Nous aborderons également les deux principales méthodes pour consommer des API RESTful et comment les utiliser avec les hooks React.

### Voici un scrim interactif sur la consommation d'API REST dans React (plus de scrims ci-dessous) :

<iframe src="https://scrimba.com/scrim/coc6f42838bab19b28a86cca1?embed=freecodecamp,mini-header" width="100%" height="480"></iframe>

## Qu'est-ce qu'une API REST ?

Si vous avez déjà passé du temps à programmer ou à rechercher sur la programmation, vous avez probablement rencontré le terme "API".

API signifie Application Programming Interface. C'est un medium qui permet à différentes applications de communiquer de manière programmatique entre elles et de retourner une réponse en temps réel.

Roy Fielding a défini REST en 2000 comme un style architectural et une méthodologie couramment utilisés dans le développement de services internet, tels que les systèmes hypermédia distribués. C'est un acronyme qui signifie "REpresentational State Transfer".

Lorsqu'une requête est faite via une API REST, elle envoie une représentation de l'état actuel de la ressource au demandeur ou au point de terminaison. Cette représentation d'état peut prendre la forme de JSON (JavaScript Object Notation), XML ou HTML.

JSON est le format de fichier le plus largement utilisé car il est indépendant du langage et peut être lu à la fois par les humains et les machines.

**Par exemple :**

```json
[
   {
      "userId": 1,
      "id": 1,
      "title": "sunt excepturi",
      "body": "quia et suscipit\nsuscipit recusandae consequuntur "
   },
   {
      "userId": 1,
      "id": 2,
      "title": "qui est esse",
      "body": "est rerum tempore vitae\nsequi sint nihil"
   }
]
```

## Comment consommer des API REST dans React

Vous pouvez consommer des API REST dans une application React de diverses manières, mais dans ce guide, nous examinerons deux des approches les plus populaires : Axios (un client HTTP basé sur les promesses) et Fetch API (une API web intégrée au navigateur).

**Note :** Pour comprendre pleinement ce guide, vous devez être familier avec JavaScript, React et les hooks React, car ils sont centraux.

Avant d'aborder comment consommer des API, il est important de comprendre que la consommation d'API dans React est très différente de la manière dont cela se fait en JavaScript. Cela est dû au fait que ces requêtes sont maintenant effectuées dans un composant React.

Dans notre cas, nous utiliserons des composants fonctionnels, ce qui signifie que nous devons utiliser deux hooks React majeurs :

* **Hook useEffect :** Dans React, nous effectuons des requêtes API à l'intérieur du hook `useEffect()`. Il s'exécute soit immédiatement lorsque l'application est montée, soit après qu'un état spécifique est atteint. Voici la syntaxe générale que nous utiliserons :

```bash
useEffect(() => {
    // récupération des données ici
}, []);
```

* **Hook useState :** Lorsque nous demandons des données, nous devons préparer un état dans lequel les données seront stockées lorsqu'elles seront retournées. Nous pouvons les sauvegarder dans un outil de gestion d'état tel que Redux ou dans un objet de contexte. Pour garder les choses simples, nous stockerons les données retournées dans l'état local de React.

```bash
const [posts, setPosts] = useState([]);
```

Apprenons maintenant comment obtenir, ajouter et supprimer des données en utilisant l'API [JSONPlaceholder posts API](https://jsonplaceholder.typicode.com/posts). Cette connaissance est applicable à tout type d'API, car ce guide est destiné aux débutants.

## Comment consommer des API en utilisant Fetch API

Fetch API est une méthode intégrée en JavaScript pour récupérer des ressources à partir d'un serveur ou d'un point de terminaison d'API. Elle est intégrée, donc vous n'avez pas besoin d'installer de dépendances ou de paquets.

La méthode `fetch()` nécessite un argument obligatoire, qui est le chemin ou l'URL de la ressource que vous souhaitez récupérer. Ensuite, elle retourne une promesse afin que vous puissiez gérer le succès ou l'échec en utilisant les méthodes `then()` et `catch()`.

Une requête fetch de base est très simple à écrire et ressemble au code ci-dessous. Nous récupérons simplement des données à partir d'une URL qui retourne des données au format JSON, puis nous les enregistrons dans la console :

```js
fetch('https://jsonplaceholder.typicode.com/posts?_limit=10')
   .then(response => response.json())
   .then(data => console.log(data));
```

La réponse par défaut est généralement une réponse HTTP régulière plutôt que le JSON réel, mais nous pouvons obtenir notre sortie sous forme d'objet JSON en utilisant la méthode json() de la réponse.

### Comment effectuer une requête GET dans React avec Fetch API

Vous pouvez utiliser la méthode HTTP GET pour demander des données à un point de terminaison.

Comme mentionné précédemment, Fetch API accepte un argument obligatoire, ce qui est vrai. Elle accepte également un argument d'option, qui est facultatif, surtout lorsque vous utilisez la méthode GET, qui est la méthode par défaut. Mais pour d'autres méthodes comme POST et DELETE, vous devrez attacher la méthode au tableau d'options :

```js
fetch(url, {
    method: "GET" // par défaut, donc nous pouvons l'ignorer
})
```

Jusqu'à présent, nous avons appris comment les choses fonctionnent, alors mettons tout ce que nous avons appris ensemble et effectuons une requête GET pour récupérer des données de notre API.

Encore une fois, nous utiliserons l'API en ligne gratuite [JSONPlaceholder](https://jsonplaceholder.typicode.com/posts) pour récupérer une liste de posts dans notre application :

```js
import React, { useState, useEffect } from 'react';

const App = () => {
   const [posts, setPosts] = useState([]);
   useEffect(() => {
      fetch('https://jsonplaceholder.typicode.com/posts?_limit=10')
         .then((response) => response.json())
         .then((data) => {
            console.log(data);
            setPosts(data);
         })
         .catch((err) => {
            console.log(err.message);
         });
   }, []);

return (
   // ... consommer ici
);
};
```

Nous avons créé un état dans le code précédent pour stocker les données que nous allons récupérer de l'API afin de pouvoir les consommer plus tard dans notre application. Nous avons également défini la valeur par défaut à un tableau vide.

```js
const [posts, setPosts] = useState([]);
```

L'opération principale s'est ensuite produite dans l'état useEffect, de sorte que les données/posts sont récupérées dès que l'application se charge. La requête fetch produit une promesse, que nous pouvons soit accepter, soit rejeter :

```js
useEffect(() => {
   fetch('https://jsonplaceholder.typicode.com/posts?_limit=10').then(
      (response) => console.log(response)
   );
}, []);
```

Cette réponse contient une grande quantité de données, telles que le code de statut, le texte et d'autres informations dont nous aurons besoin pour gérer les erreurs plus tard.

Jusqu'à présent, nous avons géré une résolution en utilisant `.then()`, mais elle a retourné un objet de réponse, ce qui n'est pas ce que nous voulons. Nous devons donc résoudre l'objet Response en format JSON en utilisant la méthode `json()`. Cela retourne également une promesse pour que nous obtenions les données réelles en utilisant le deuxième `.then()`.

```js
useEffect(() => {
   fetch('https://jsonplaceholder.typicode.com/posts?_limit=10')
      .then((response) => response.json())
      .then((data) => {
         console.log(data);
         setPosts(data);
      });
}, []);
```

Si nous regardons la console, nous verrons que nous avons récupéré 10 posts de notre API, que nous avons également définis dans l'état que nous avons spécifié précédemment.

Ceci n'est pas complet car nous n'avons géré que la résolution de la promesse et non le rejet de la promesse, que nous gérerons en utilisant la méthode `.catch()` :

```js
useEffect(() => {
   fetch('https://jsonplaceholder.typicode.com/posts?_limit=10')
      .then((response) => response.json())
      .then((data) => {
         console.log(data);
         setPosts(data);
      })
      .catch((err) => {
         console.log(err.message);
      });
}, []);
```

Jusqu'à présent, nous avons vu comment effectuer une requête `GET`. Cela peut être facilement consommé dans notre application en parcourant notre tableau :

```js
const App = () => {
// ...

   return (
   <div className="posts-container">
      {posts.map((post) => {
         return (
            <div className="post-card" key={post.id}>
               <h2 className="post-title">{post.title}</h2>
               <p className="post-body">{post.body}</p>
               <div className="button">
               <div className="delete-btn">Supprimer</div>
               </div>
            </div>
         );
      })}
   </div>
   );
};

export default App;
```

### Comment effectuer une requête POST dans React avec Fetch API

Vous pouvez utiliser la méthode HTTP `POST` pour envoyer des données à un point de terminaison. Elle fonctionne de manière similaire à la requête `GET`, la principale différence étant que vous devez ajouter la méthode et deux paramètres supplémentaires à l'objet optionnel :

```js
const addPosts = async (title, body) => {
await fetch('https://jsonplaceholder.typicode.com/posts', {
method: 'POST',
body: JSON.stringify({
   title: title,
   body: body,
   userId: Math.random().toString(36).slice(2),
}),
headers: {
   'Content-type': 'application/json; charset=UTF-8',
},
})
.then((response) => response.json())
.then((data) => {
   setPosts((posts) => [data, ...posts]);
   setTitle('');
   setBody('');
})
.catch((err) => {
   console.log(err.message);
});
};
```

Les principaux paramètres qui peuvent sembler étranges sont le corps et l'en-tête.

Le corps contient les données que nous voulons transmettre à l'API, que nous devons d'abord stringifier car nous envoyons des données à un serveur web. L'en-tête nous indique le type de données, qui est toujours le même lors de la consommation d'API REST. Nous définissons également l'état pour contenir les nouvelles données et distribuer les données restantes dans le tableau.

En regardant la méthode `addPost()` que nous avons créée, elle attend ces données d'un formulaire ou autre. Dans notre cas, j'ai créé un formulaire, obtenu les données du formulaire via des états, puis les ai ajoutées à la méthode lorsque le formulaire a été soumis :

```js
import React, { useState, useEffect } from 'react';
const App = () => {
const [title, setTitle] = useState('');
const [body, setBody] = useState('');
// ...
const addPosts = async (title, body) => {
   await fetch('https://jsonplaceholder.typicode.com/posts', {
      method: 'POST',
      body: JSON.stringify({
         title: title,
         body: body,
         userId: Math.random().toString(36).slice(2),
      }),
      headers: {
         'Content-type': 'application/json; charset=UTF-8',
      },
   })
      .then((response) => response.json())
      .then((data) => {
         setPosts((posts) => [data, ...posts]);
         setTitle('');
         setBody('');
      })
      .catch((err) => {
         console.log(err.message);
      });
};

const handleSubmit = (e) => {
   e.preventDefault();
   addPosts(title, body);
};    

return (
   <div className="app">
      <div className="add-post-container">
         <form onSubmit={handleSubmit}>
            <input type="text" className="form-control" value={title}
               onChange={(e) => setTitle(e.target.value)}
            />
            <textarea name="" className="form-control" id="" cols="10" rows="8" 
               value={body} onChange={(e) => setBody(e.target.value)} 
            ></textarea>
            <button type="submit">Ajouter un Post</button>
         </form>
      </div>
      {/* ... */}
   </div>
);
};

export default App;
```

### Comment effectuer une requête DELETE dans React avec Fetch API

Vous pouvez utiliser la méthode HTTP `DELETE` pour supprimer des données d'un point de terminaison. Elle fonctionne de manière similaire à la requête `GET`, la principale différence étant l'ajout de la méthode :

```js
const deletePost = async (id) => {
await fetch(`https://jsonplaceholder.typicode.com/posts/${id}`, {
   method: 'DELETE',
}).then((response) => {
   if (response.status === 200) {
      setPosts(
         posts.filter((post) => {
            return post.id !== id;
         })
      );
   } else {
      return;
   }
});
};
```

Cela se déclenche lorsque le bouton est cliqué, et nous obtenons l'`id` du post spécifique dans lequel le bouton a été cliqué. Ensuite, nous supprimons ces données de l'ensemble des données retournées.

Cela sera supprimé de l'API mais pas immédiatement de l'UI, c'est pourquoi nous avons ajouté un filtre pour supprimer également les données. Pour chaque élément dans la boucle, votre bouton de suppression ressemblera à ceci :

```js
const App = () => {
// ...

   return (
   <div className="posts-container">
      {posts.map((post) => {
         return (
            <div className="post-card" key={post.id}>
               {/* ... */}
               <div className="button">
                  <div className="delete-btn" onClick={() => deletePost(post.id)}>
                     Supprimer
                  </div>
               </div>    
            </div>
         );
      })}
   </div>
   );
};

export default App;
```

### Comment utiliser Async/Await dans Fetch API

Jusqu'à présent, nous avons vu comment faire des requêtes fetch normalement en utilisant la syntaxe de promesse, ce qui peut être confus à certains moments. Ensuite, vient l'enchaînement. Nous pouvons éviter l'enchaînement `.then()` en utilisant Async/await et écrire un code plus lisible.

Pour utiliser async/await, appelez d'abord `async` dans la fonction. Ensuite, lorsque vous faites une requête et attendez une réponse, ajoutez la syntaxe `await` devant la fonction pour attendre que la promesse se résolve avec le résultat.

Lorsque nous utilisons async/await, toutes nos requêtes Fetch ressembleront à ceci :

```js
import React, { useState, useEffect } from 'react';

const App = () => {
   const [title, setTitle] = useState('');
   const [body, setBody] = useState('');
   const [posts, setPosts] = useState([]);

   // GET avec Fetch API
   useEffect(() => {
      const fetchPost = async () => {
         const response = await fetch(
            'https://jsonplaceholder.typicode.com/posts?_limit=10'
         );
         const data = await response.json();
         console.log(data);
         setPosts(data);
      };
      fetchPost();
   }, []);

   // Supprimer avec FetchAPI
   const deletePost = async (id) => {
      let response = await fetch(
         `https://jsonplaceholder.typicode.com/posts/${id}`,
         {
            method: 'DELETE',
         }
      );
      if (response.status === 200) {
         setPosts(
            posts.filter((post) => {
               return post.id !== id;
            })
         );
      } else {
         return;
      }
   };

   // Post avec FetchAPI
   const addPosts = async (title, body) => {
      let response = await fetch('https://jsonplaceholder.typicode.com/posts', {
         method: 'POST',
         body: JSON.stringify({
            title: title,
            body: body,
            userId: Math.random().toString(36).slice(2),
         }),
         headers: {
            'Content-type': 'application/json; charset=UTF-8',
         },
      });
      let data = await response.json();
      setPosts((posts) => [data, ...posts]);
      setTitle('');
      setBody('');
   };

   const handleSubmit = (e) => {
      e.preventDefault();
      addPosts(title, body);
   };

   return (
      // ...
   );
};

export default App;
```

#### Voici un scrim interactif pour vous guider à travers cela :

<iframe src="https://scrimba.com/scrim/co1af4d8f8db412c467e20af0?embed=freecodecamp,mini-header" width="100%" height="480"></iframe>

### Comment gérer les erreurs avec Fetch API

Dans cette section, nous verrons comment gérer les erreurs à la fois de manière traditionnelle et avec async/await.

Nous pouvons utiliser les données de réponse pour gérer les erreurs dans Fetch API, ou nous pouvons utiliser l'instruction try/catch lorsque nous utilisons async/await.

Voyons comment nous pouvons faire cela typiquement dans Fetch API :

```js
const fetchPost = () => {
fetch('https://jsonplaceholder.typicode.com/posts?_limit=10')
   .then((response) => {
      if (!response.ok) {
         throw Error(response.statusText);
      }
      return response.json();
   })
   .then((data) => {
      console.log(data);
      setPosts(data);
   })
   .catch((err) => {
      console.log(err.message);
   });
};
```

Vous pouvez lire plus sur les erreurs de Fetch API [ici](https://www.tjvantoll.com/2015/09/13/fetch-and-errors/).

Et pour async/await, nous pouvons utiliser `try` et `catch` comme ceci :

```js
const fetchPost = async () => {
   try {
      const response = await fetch(
         'https://jsonplaceholder.typicode.com/posts?_limit=10'
      );
      const data = await response.json();
      setPosts(data);
   } catch (error) {
      console.log(error);
   }
};
```

## Comment consommer des API en utilisant Axios

Axios est une bibliothèque cliente HTTP basée sur les promesses qui simplifie l'envoi de requêtes HTTP asynchrones aux points de terminaison REST. Ce point de terminaison dans notre cas est l'API JSONPlaceholder Posts, à laquelle nous effectuerons des requêtes `GET`, `POST` et `DELETE`.

#### Voici un scrim interactif qui vous guidera à travers les étapes pendant que vous lisez :

<iframe src="https://scrimba.com/scrim/cob6540b4a1ad315f83abd56d?embed=freecodecamp,mini-header" width="100%" height="480"></iframe>

### Comment installer et configurer une instance Axios

Axios, contrairement à Fetch API, n'est pas intégré, donc nous devrons l'incorporer dans notre projet pour l'utiliser.

Vous pouvez ajouter Axios à votre projet en exécutant la commande suivante :

```js
npm install axios
```

Une fois que vous avez installé Axios avec succès, nous pouvons procéder à la création d'une instance, ce qui est facultatif mais recommandé car cela nous évite des répétitions inutiles.

Pour créer une instance, nous utilisons la méthode `.create()`, que nous pouvons utiliser pour spécifier des informations telles que l'URL et éventuellement les en-têtes :

```js
import axios from "axios";

const client = axios.create({
   baseURL: "https://jsonplaceholder.typicode.com/posts" 
});
```

### Comment effectuer une requête GET dans React avec Axios

Nous utiliserons l'instance que nous avons déclarée précédemment pour effectuer la requête GET. Tout ce que nous ferons est de définir les paramètres, le cas échéant, et d'obtenir la réponse au format JSON par défaut.

Contrairement à la méthode Fetch API, aucune option n'est requise pour déclarer la méthode. Nous attachons simplement la méthode à l'instance et l'interrogeons.

```js
useEffect(() => {
   client.get('?_limit=10').then((response) => {
      setPosts(response.data);
   });
}, []);
```

### Comment effectuer une requête POST dans React avec Axios

Comme mentionné précédemment, vous pouvez utiliser la méthode `POST` pour envoyer des données à un point de terminaison. Elle fonctionne de manière similaire à la requête `GET`, la principale différence étant la nécessité d'inclure la méthode et une option pour contenir les données que nous envoyons :

```js
const addPosts = (title, body) => {
   client
      .post('', {
         title: title,
         body: body,
      })
      .then((response) => {
         setPosts((posts) => [response.data, ...posts]);
      });
};
```

### Comment effectuer une requête DELETE dans React avec Axios

Nous pouvons effectuer des requêtes de suppression en utilisant la méthode delete, qui obtient l'`id` et le supprime de l'API. Nous utiliserons également la méthode filter pour le supprimer de l'UI, comme nous l'avons fait avec la méthode Fetch API :

```js
const deletePost = (id) => {
   client.delete(`${id}`);
   setPosts(
      posts.filter((post) => {
         return post.id !== id;
      })
   );
};
```

### Comment utiliser Async/Await dans Axios

Jusqu'à présent, nous avons vu comment faire des requêtes Axios en utilisant la syntaxe de promesse. Mais maintenant, voyons comment nous pouvons utiliser async/await pour écrire moins de code et éviter l'enchaînement `.then()`.

Lorsque nous utilisons async/await, toutes nos requêtes Axios ressembleront à ceci :

```js
import React, { useState, useEffect } from 'react';

const App = () => {
   const [title, setTitle] = useState('');
   const [body, setBody] = useState('');
   const [posts, setPosts] = useState([]);

   // GET avec Axios
   useEffect(() => {
      const fetchPost = async () => {
         let response = await client.get('?_limit=10');
         setPosts(response.data);
      };
      fetchPost();
   }, []);

   // Supprimer avec Axios
   const deletePost = async (id) => {
      await client.delete(`${id}`);
      setPosts(
         posts.filter((post) => {
            return post.id !== id;
         })
      );
   };

   // Post avec Axios
   const addPosts = async (title, body) => {
      let response = await client.post('', {
         title: title,
         body: body,
      });
      setPosts((posts) => [response.data, ...posts]);
   };

   const handleSubmit = (e) => {
      e.preventDefault();
      addPosts(title, body);
   };

   return (
      // ...
   );
};

export default App;
```

### Comment gérer les erreurs avec Axios

Pour les requêtes Axios basées sur les promesses, nous pouvons utiliser les méthodes `.then()` et `.catch()`, mais pour async/await, nous pouvons utiliser le bloc `try...catch`. Cela est très similaire à la manière dont nous avons implémenté Fetch API, et le bloc `try...catch` ressemblera à ceci :

```js
const fetchPost = async () => {
   try {
      let response = await client.get('?_limit=10');
      setPosts(response.data);
   } catch (error) {
      console.log(error);
   }
};
```

Vous pouvez lire plus sur la gestion des erreurs avec Axios [ici](https://stackabuse.com/handling-errors-with-axios/).

## Fetch API vs Axios

Vous avez peut-être remarqué quelques différences, mais mettons-les dans un tableau pratique afin que nous puissions comparer Fetch et Axios correctement.

Ces distinctions vous aideront à décider quelle méthode utiliser pour un projet spécifique. Parmi ces distinctions, on trouve :

| Axios | Fetch |
| --- | --- |
| Axios est un package tiers autonome simple à installer. | Fetch est intégré dans la plupart des navigateurs modernes. **Aucune installation** n'est requise en tant que telle. |
| Axios utilise la propriété **data**. | Fetch utilise la propriété **body**. |
| Les données Axios contiennent l'**objet**. | Le corps de Fetch doit être **stringifié**. |
| Lorsque le statut est 200 et que le statusText est 'OK', la requête Axios est acceptée. | La requête Fetch est ok lorsque **l'objet de réponse contient la propriété ok**. |
| Axios effectue des **transformations automatiques des données JSON**. | Fetch est un **processus en deux étapes** lors de la gestion des données JSON - d'abord, pour faire la requête réelle ; ensuite, pour appeler la méthode .json() sur la réponse. |
| Axios permet **l'annulation de la requête et le délai d'expiration de la requête**. | Fetch ne le permet pas. |
| Axios a un **support intégré pour le progrès du téléchargement**. | Fetch ne supporte pas le progrès du téléchargement. |
| Axios a un **large support des navigateurs**. | Fetch est uniquement compatible avec Chrome 42+, Firefox 39+, Edge 14+, et Safari 10.1+. (Ceci est connu sous le nom de Compatibilité Descendante). |

## Conclusion

Dans ce guide, nous avons appris comment consommer des API REST dans React en utilisant soit Fetch API soit Axios.

Cela vous aidera à commencer avec la consommation d'API dans React, et à partir de là, vous serez en mesure de consommer des données de manière plus complexe et de manipuler vos API comme vous le souhaitez.

Embarquez dans un voyage d'apprentissage ! [Parcourez plus de 200 articles d'experts sur le développement web](https://joelolawanle.com/contents). Consultez [mon blog](https://joelolawanle.com/posts) pour plus de contenu captivant de ma part.