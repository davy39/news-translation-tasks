---
title: Composants React – Comment créer un composant de recherche, de filtrage et
  de pagination dans React
subtitle: ''
author: Spruce Emmanuel
co_authors: []
series: null
date: '2022-06-07T23:37:17.000Z'
originalURL: https://freecodecamp.org/news/how-to-react-components
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/wirxeocmd6tpnn9c5oqc.jpg
tags:
- name: components
  slug: components
- name: React
  slug: react
seo_title: Composants React – Comment créer un composant de recherche, de filtrage
  et de pagination dans React
seo_desc: "I wrote the article \"How to Search and Filter Components in React\" exactly\
  \ one year ago.\nhttps://twitter.com/freeCodeCamp/status/1401192338073042954?s=20&t=LhPQBYEWz90YSd8lm_M6FA\n\
  \ \nSince then, a lot has changed. The API we used for the tutorial has s..."
---

J'ai écrit l'article « Comment rechercher et filtrer des composants dans React » exactement il y a un an.

%[https://twitter.com/freeCodeCamp/status/1401192338073042954?s=20&t=LhPQBYEWz90YSd8lm_M6FA]

Depuis lors, beaucoup de choses ont changé. L'API que nous avons utilisée pour le tutoriel a cessé de fonctionner, donc dans cet article, nous allons recréer nos exemples précédents tout en introduisant la pagination dans notre composant.

Ce tutoriel utilise React.js, vous aurez donc besoin d'une compréhension de base de React et de JavaScript pour suivre. Ce tutoriel suppose également que vous avez lu l'article précédent, Comment [rechercher et filtrer des composants dans React](https://www.freecodecamp.org/news/search-and-filter-component-in-reactjs/).

## Installation

Pour obtenir les données des pays pour ce tutoriel, nous allons utiliser [CountryAPI](https://countryapi.io/) de CountryAPI.io.

Nous aurons besoin d'une clé API pour utiliser l'API. Pour obtenir votre clé API, rendez-vous sur [CountryAPI](https://countryapi.io/register) et créez un compte. Votre clé API devrait apparaître sur votre tableau de bord :

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Web-capture_4-6-2022_184858_countryapi.io--1-.jpeg align="left")

Ensuite, nous allons créer une nouvelle application React avec [Create React App](https://create-react-app.dev/docs/getting-started/). Pour cela, exécutez les commandes suivantes dans votre terminal :

```js
# Exécutez ceci pour utiliser npm
npx create-react-app search-app
# Ou exécutez ceci pour utiliser yarn
yarn create react-app search-app
cd my-app
npm start
# Ou avec yarn
yarn start
```

Comme d'habitude, pour l'aperçu en direct, nous allons utiliser Codepen pour afficher tous nos exemples.

## Comment récupérer les données

Pour obtenir nos données, nous devons faire un appel GET à l'endpoint [`https://countryapi.io/api/all`](https://countryapi.io/api/all) tout en fournissant notre clé API. Dans le fichier **src** > **App.js** de l'application React que nous avons créée précédemment, supprimez tout le code existant et remplacez-le par ce qui suit :

```js
import { useState, useEffect } from "react";
import "./App.css";

function App() {
  const [error, setError] = useState(null);
  const [loaded, setLoaded] = useState(false);
  const [items, setItems] = useState([]);
  
   useEffect(() => {
    const request_headers = new Headers();
    const api_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxx";
    request_headers.append("Authorization", `Bearer ${api_key}`);
    request_headers.append("Content-Type", "application/json");

    const request_options = {
      method: "GET",
      headers: request_headers,
    };

    fetch("https://countryapi.io/api/all", request_options)
      .then((res) => res.json())
      .then(
        (result) => {
          setLoaded(true);
          setItems(result);
        },
        (error) => {
          setLoaded(true);
          setError(error);
        }
      );
  }, []);
  
  console.log(items)
  
  if (error) {
    return <>{error.message}</>;
  } else if (!loaded) {
    return <>loading...</>;
  } else {
     return (
     //
    );
  }
 }

export default App;
```

Tout ce que nous avons fait ci-dessus, c'est utiliser l'API fetch de JavaScript pour faire la requête GET à notre endpoint, puis stocker les données retournées dans l'état `items` en utilisant `setState(result)`.

### Comment afficher les données

Ensuite, nous devons afficher les données de l'API, qui seront une liste de tous les pays retournés par notre API.

Pour faire une liste, nous devons générer un tableau d'objets à partir des valeurs de notre objet retourné. Ouvrez le fichier **src** > **App.js** et ajoutez le code suivant :

```js
import { useState, useEffect } from "react";
import "./App.css";

function App() {
  const [error, setError] = useState(null);
  const [loaded, setLoaded] = useState(false);
  const [items, setItems] = useState([]);

  useEffect(() => {
    // fetch data
  }, []);

  const data = Object.values(items);

  if (error) {
    return <>{error.message}</>;
  } else if (!loaded) {
    return <>loading...</>;
  } else {
    return (
      <div className="wrapper">
        <ul className="card-grid">
          {data.map((item) => (
            <li key={item.alpha3Code}>
              <article className="card">
                <div className="card-image">
                  <img src={item.flag.large} alt={item.name} />
                </div>
                <div className="card-content">
                  <h2 className="card-name">{item.name}</h2>
                  // other card content
              </article>
            </li>
          ))}
        </ul>
      </div>
    );
  }
}

export default App;
```

Avec un peu de CSS ajouté, l'exemple ci-dessus ressemble à l'aperçu ci-dessous :

%[https://codepen.io/Spruce_khalifa/pen/yLvqezJ?editors=0010]

## Comment créer le composant de recherche

La première chose à faire est de créer un champ de saisie où les utilisateurs peuvent entrer leur requête de recherche. Ouvrez **src** > **App.js** et faites la modification suivante :

```js
...

function App() {
 const [query, setQuery] = useState("");
 
  if (error) {
    return <>{error.message}</>;
  } else if (!loaded) {
    return <>loading...</>;
  } else {
    return (
      <div className="wrapper">
        <div className="search-wrapper">
          <label htmlFor="search-form">
            <input
              type="search"
              name="search-form"
              id="search-form"
              className="search-input"
              placeholder="Rechercher..."
              onChange={(e) => setQuery(e.target.value)}
            />
            <span className="sr-only">Rechercher des pays ici</span>
          </label>
        </div>
        
        ...
      </div>
    );
  }
}

export default App;
```

Ci-dessus, nous avons créé un champ de saisie et, en utilisant le gestionnaire d'événements `onChange`, chaque fois que la valeur du champ de saisie change, nous définissons la valeur à `query` en utilisant le hook `useState`.

Ensuite, nous devons utiliser cette `query` pour filtrer les données retournées par notre API.

```js
const search_parameters = Object.keys(Object.assign({}, ...data));

 function search(data) {
    return items.filter(
      (item) =>
        search_parameters.some((parameter) =>
          item[parameter].toString().toLowerCase().includes(query)
        )
    );
  }
```

Décomposons un peu cela. Tout d'abord, nous avons créé une fonction `search()` qui prend nos `data` comme argument. En combinant les méthodes `Array.filter()` et `Array.some()`, nous avons vérifié si l'un de nos paramètres de recherche inclut la valeur de notre requête `includes(query)`.

Bien sûr, nous pouvons coder en dur nos paramètres de recherche :

```js
const search_parameters = ["Capital", "Name", ...]
```

Et bien que ce soit le moyen le plus rapide, ce n'est pas à l'épreuve du futur (les données retournées par une API peuvent changer) – je l'ai découvert à mes dépens. Au lieu de coder en dur, nous pouvons obtenir les paramètres de recherche à partir des `data` retournées par l'API.

```js
const search_parameters = Object.keys(Object.assign({}, ...data));
```

Enfin, nous devons utiliser les nouvelles données retournées par la fonction `search(data)` pour construire nos listes de pays. Ouvrez le fichier **App.js** et modifiez la liste que nous avons créée précédemment :

```js
...
{search(data).map((item) => (
 <li key={item.alpha3Code}>
  <article className="card">
   <div className="card-image">
    <img src={item.flag.large} alt={item.name} />
     </div>
   <div className="card-content">
    <h2 className="card-name">{item.name}</h2>
    ...           
   </div>
   </article>
 </li>
))}
```

Avec la fonctionnalité de recherche ajoutée, l'aperçu en direct ressemble maintenant à ceci :

%[https://codepen.io/Spruce_khalifa/pen/vYdaBEq?editors=0010]

## Comment créer le composant de filtrage

Un filtre est souvent utilisé pour regrouper les données par un mot-clé spécifique. Dans cet exemple, nous voulons regrouper les données par régions.

Encore une fois, au lieu de coder cela en dur, nous pouvons obtenir les régions à partir des données :

```js
const filter_items = [...new Set(data.map((item) => item.region))];
```

Après le champ de saisie de recherche que nous avons créé, ajoutez l'interface utilisateur du filtre – c'est un champ de sélection HTML `select` :

```js
...
const [filter, setFilter] = useState("");
...

<div className="select">
 <select
  onChange={(e) => setFilter(e.target.value)}
  className="custom-select"
  aria-label="Filter Countries By Region">
  <option value="">Filtrer par région</option>
  {filter_items.map((item) => (
   <option value={item}>Filtrer par {item}</option>
  ))}
</select>
<span className="focus"></span>
</div>
```

Pour ajouter le filtre, nous devons modifier la fonction `search(data)`. Ainsi, au lieu de retourner uniquement les données que nous avons recherchées, nous retournons maintenant les données selon notre paramètre de filtre :

```js
function search(items) {
    return items.filter(
      (item) =>
        item.region.includes(filter) &&
        search_parameters.some((parameter) =>
          item[parameter].toString().toLowerCase().includes(query)
        )
    );
  }
```

Et voilà – nous pouvons maintenant filtrer nos pays par région. L'aperçu en direct et le code complet peuvent être trouvés sur Codepen :

%[https://codepen.io/Spruce_khalifa/pen/ExQpYVp]

## Comment créer le composant de pagination

La pagination ne réduit pas seulement les listes d'éléments affichés sur une page web – elle augmente également les performances de l'application puisque les utilisateurs n'ont à télécharger que quelques ressources lorsque la page se charge.

Pour créer une pagination pour nos données de pays, nous allons commencer par spécifier le nombre d'éléments que nous voulons afficher dans un `useState` :

```js
const [paginate, setpaginate] = useState(8);
```

Ensuite, utilisons notre valeur `paginate` pour mettre à jour notre liste de pays :

```js
...
{search(data)
 .slice(0, paginate)
 .map((item) => (
 <li key={item.alpha3Code}>
  <article className="card">
   <div className="card-image">
    <img src={item.flag.large} alt={item.name} />
     </div>
   <div className="card-content">
    <h2 className="card-name">{item.name}</h2>
    ...           
   </div>
   </article>
 </li>
))}
```

Ensuite, nous devons créer une fonction où nous mettons à jour cet état chaque fois que nous l'appelons :

```js
const load_more = (event) => {
  setpaginate((prevValue) => prevValue + 8);
};
```

Enfin, créons un bouton qui appellera la fonction `load_more` lorsqu'il sera cliqué :

```js
<button onClick={load_more}>Charger plus</button>
```

Encore une fois, l'aperçu de la pagination peut être trouvé sur CodePen :

%[https://codepen.io/Spruce_khalifa/pen/NWyBKxb]

## Conclusion

Dans cet article, nous avons vu comment implémenter les fonctionnalités de recherche, de filtrage et de pagination dans React en construisant une application réelle utilisant [CountryAPI](https://countryapi.io/) de [CountryAPI.io](http://CountryAPI.io).

Si vous avez créé quelque chose de merveilleux avec cela, n'hésitez pas à tweeter à ce sujet et à me taguer [@sprucekhalifa](https://twitter.com/sprucekhalifa). Et n'oubliez pas de cliquer sur le bouton suivre.

Bon codage !