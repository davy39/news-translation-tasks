---
title: Axios React – Comment faire des requêtes GET, POST et DELETE vers une API
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-05-17T16:12:39.000Z'
originalURL: https://freecodecamp.org/news/axios-react-how-to-make-get-post-and-delete-api-requests
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/cover-template.jpg
tags:
- name: axios
  slug: axios
- name: crud
  slug: crud
- name: React
  slug: react
seo_title: Axios React – Comment faire des requêtes GET, POST et DELETE vers une API
seo_desc: 'Axios is an HTTP client library based on promises. It makes sending asynchronous
  HTTP requests to REST endpoints easier and helps you perform CRUD operations.

  This REST endpoint/API could be an external API like the Google API, GitHub API,
  and so on ...'
---

[Axios](https://axios-http.com/) est une bibliothèque cliente HTTP basée sur les promesses. Elle facilite l'envoi de requêtes HTTP asynchrones vers des endpoints REST et vous aide à effectuer des opérations CRUD.

Cet endpoint REST/API peut être une API externe comme l'API Google, l'API GitHub, et ainsi de suite – ou cela peut être votre propre serveur backend Node.js.

Dans ce guide, nous allons apprendre comment faire des requêtes GET, POST et DELETE avec Axios dans React. Cela fait simplement référence à la manière dont nous récupérons des données depuis une API, ajoutons des données à l'API, puis supprimons des données de notre API.

Les requêtes GET, POST et DELETE sont parmi les requêtes les plus courantes faites par les développeurs au quotidien. Après tout, nous aurons toujours besoin de récupérer des données à afficher dans notre application ou d'effectuer certaines opérations, ainsi que d'ajouter et de supprimer des données vers/depuis notre API.

### Voici un scrim interactif sur la façon de faire des requêtes GET, POST et DELETE avec Axios dans React :

<iframe src="https://scrimba.com/scrim/co6e84267986fe1194cb9ac07?embed=freecodecamp,mini-header" width="100%" height="480"></iframe>

## Pourquoi Axios ?

La prochaine question que vous pourriez vous poser est pourquoi utiliser Axios, étant donné que nous devons installer une bibliothèque supplémentaire. Voici quelques raisons :

* Axios utilise [XMLHttpRequest](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest) sous le capot, et il est largement supporté par la plupart des navigateurs, y compris les plus anciens comme Internet Explorer 11. Fetch(), en revanche, n'est compatible qu'avec Chrome 42+, Firefox 39+, Edge 14+ et Safari 10.3+ (vous pouvez voir le tableau complet de compatibilité sur [CanIUse.com](https://caniuse.com/fetch)).

* Lors de l'envoi de requêtes, Axios signe automatiquement les données, contrairement à fetch(), qui nécessite que nous le fassions manuellement.

* Contrairement à l'API Fetch, qui vous oblige à vérifier le code de statut et à lancer l'erreur vous-même, Axios a une meilleure gestion des erreurs et peut lancer des erreurs de la gamme 400 et 500.

## Comment commencer avec Axios dans React

Pour commencer avec Axios dans votre application React, installez d'abord React dans votre projet avec la commande suivante :

```bash
npm install axios
```

Une fois cela terminé, nous allons utiliser l'[API JSONPlacholder Posts](https://jsonplaceholder.typicode.com/posts) pour apprendre comment récupérer ces posts dans notre application React, ajouter de nouveaux posts, et enfin supprimer un post spécifique avec Axios.

Étant donné que c'est une application React, nous allons utiliser les hooks React pour accéder aux états et à d'autres fonctionnalités. Les hooks que nous allons utiliser sont `useEffect()` et `useState()`.

Essentiellement, nous allons utiliser le hook `useEffect()` pour récupérer les posts dès que l'application est rendue/montée, tandis que le hook `useState()` nous aidera à créer un stockage local pour nos données.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-89.png align="left")

### Comment créer l'instance Axios

Une fois que vous avez installé Axios avec succès, il est bon de créer une instance Axios. Ce n'est pas obligatoire, mais cela nous fait gagner du temps.

Pour créer une instance, nous allons utiliser la méthode `.create()`, qui nous permet de spécifier des informations telles que l'URL et éventuellement les en-têtes :

```javascript
import axios from "axios";

const client = axios.create({
  baseURL: "https://jsonplaceholder.typicode.com/posts" 
});
```

## Comment faire une requête GET avec Axios dans React

Vous pouvez utiliser les requêtes GET pour obtenir des données depuis un endpoint, et cela se produira dès que l'application est rendue grâce au hook `useEffect()`.

Nous allons utiliser la variable et ensuite attacher la méthode `.get()` pour faire une requête GET vers notre endpoint/API. Ensuite, nous allons utiliser un callback `.then()` pour obtenir toutes les données de réponse, car nous avons déjà une instance Axios qui contient le `baseURL` assigné à une variable (client).

En utilisant la propriété `.data`, nous obtenons les données de réponse, qui sont les données réelles de l'objet de réponse.

```javascript
const App = () => {
   const [posts, setPosts] = useState([]);

   useEffect(() => {
      client.get('?_limit=10').then((response) => {
         setPosts(response.data);
      });
   }, []);

   return (
      // ...
   );
};

export default App;
```

Nous définissons les données dans l'état que nous avons créé, afin qu'elles puissent être consommées dans notre application.

### Comment consommer une requête GET

Après avoir implémenté avec succès la requête GET, l'étape suivante consiste à consommer les données stockées dans l'état `posts`.

Étant donné que nous interrogeons un tableau de dix posts, nous devons parcourir cet état pour obtenir ces dix posts dans notre application :

```javascript
// ...

return (
  <div className="app">
    <h2>Tous les Posts 📫</h2>
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

// ...
```

## Comment faire une requête POST avec Axios dans React

Vous utilisez une requête POST pour envoyer des données à un endpoint. Cela fonctionne de manière similaire à une requête GET, sauf que la fonction créée pour effectuer cette tâche sera déclenchée lorsque le formulaire est soumis ou autre.

Cela prend un objet pour envoyer les données et ajoute également les données à l'état en étalant les données précédentes puis en ajoutant les nouvelles données :

```javascript
const App = () => {
   const [title, setTitle] = useState('');
   const [body, setBody] = useState('');
   const [posts, setPosts] = useState([]);

   // ...

   const handleSubmit = (e) => {
      e.preventDefault();
      addPosts(title, body);
   };

   const addPosts = (title, body) => {
      client
         .post('', {
            title: title,
            body: body,
         })
         .then((response) => {
            setPosts([response.data, ...posts]);
         });
      setTitle('');
      setBody('');
   };
   
   return (
      // ...
   );
};

export default App;
```

Lorsque le formulaire est soumis, nous appelons la fonction `handleSubmit()`, qui empêche la page de se recharger. Elle appelle également la fonction principale `addPosts()` en passant les données entrées dans le formulaire en tant que paramètre.

### Comment effectuer une requête DELETE dans React

Comme son nom l'indique, vous utilisez cela pour supprimer des données spécifiques de votre endpoint/API ainsi que de votre UI – DELETE peut gérer les deux.

Pour cela, nous allons utiliser la méthode DELETE en conjonction avec la variable client où nous avons initialisé Axios. Voici à quoi ressemblera la requête :

```javascript
const App = () => {
   const [posts, setPosts] = useState([]);

   // ...

   const deletePost = (id) => {
      client.delete(`${id}`);
      setPosts(
         posts.filter((post) => {
            return post.id !== id;
         })
      );
   };

   return (
      // ...
   );
};

export default App;
```

En gros, il y a une méthode `onClick=() => deletePost(post.id)` sur le bouton de suppression qui déclenche la méthode `deletePost()`. Nous lui avons passé l'`ID` du post particulier que nous essayons de supprimer afin de pouvoir identifier le post.

Nous le supprimons de l'UI après l'avoir supprimé de l'endpoint/API en utilisant la méthode filter pour retourner un tableau qui ne contient pas cet élément.

## Comment faire des requêtes dans React avec Async/Await

Jusqu'à présent, nous avons vu comment faire des requêtes Axios avec la syntaxe des promesses. Maintenant, voyons comment nous pouvons utiliser async/await pour écrire moins de code et éviter l'enchaînement `.then`, qui est beaucoup plus difficile à comprendre.

Pour utiliser async/await, appelez d'abord `async` dans la fonction. Ensuite, ajoutez la syntaxe `await` devant la fonction lors de l'envoi d'une requête et attendez une réponse jusqu'à ce que la promesse se résolve avec le résultat.

Lorsque nous utilisons async/await, toutes nos requêtes Axios ressembleront à ceci :

```javascript
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

   // DELETE avec Axios
   const deletePost = async (id) => {
      await client.delete(`${id}`);
      setPosts(
         posts.filter((post) => {
            return post.id !== id;
         })
      );
   };
    
   // gérer la soumission du formulaire
   const handleSubmit = (e) => {
      e.preventDefault();
      addPosts(title, body);
   };

   // POST avec Axios
   const addPosts = async (title, body) => {
      let response = await client.post('', {
         title: title,
         body: body,
      });
      setPosts([response.data, ...posts]);
      setTitle('');
      setBody('');
   };

   return (
      // ...
   );
};
```

## Comment gérer les erreurs dans Axios

Lors de la consommation de données depuis une API, il est toujours recommandé de gérer les erreurs pour aider à montrer le type d'erreur que nous obtenons. Ces erreurs peuvent survenir en raison de données incorrectes que nous passons, de la réalisation d'une requête vers une API incorrecte, ou d'une erreur réseau.

Nous pouvons gérer les erreurs dans Axios en utilisant les méthodes `.then()` et `.catch()`, ou en utilisant le bloc `try...catch` pour les requêtes Axios async/await.

### Comment gérer les erreurs dans Axios avec la méthode `.catch`

Vous pouvez implémenter cela en attachant une méthode `.catch()` à la méthode `.then()` pour gérer les erreurs. Supposons que la méthode `.then()` échoue :

```javascript
useEffect(() => {
  client
     .get('?_limit=10')
     .then((response) => {
        setPosts(response.data);
     })
     .catch((error) => {
        console.log(error);
     });
}, []);
```

### Comment gérer les erreurs dans Axios avec le bloc try…catch

Pour le scénario async/await, le bloc `try...catch` ressemblera à ceci :

```javascript
useEffect(() => {
  const fetchPost = async () => {
     try {
        let response = await client.get('?_limit=10');
        setPosts(response.data);
     } catch (error) {
        console.log(error);
     }
  };
  fetchPost();
}, []);
```

Vous pouvez lire plus sur la gestion des erreurs avec Axios [ici](https://stackabuse.com/handling-errors-with-axios/).

## Conclusion

Dans ce tutoriel, vous avez appris comment utiliser Axios, l'une des bibliothèques clientes HTTP les plus puissantes, pour effectuer les trois requêtes API de base.

Vous pouvez voir l'implémentation complète de la manière dont j'ai construit [l'application de posts en utilisant React et Axios dans ce dépôt](https://github.com/olawanlejoel/posts-jsonplaceholder-demo).