---
title: Comment rechercher et filtrer des composants dans React
subtitle: ''
author: Spruce Emmanuel
co_authors: []
series: null
date: '2021-06-04T21:34:33.000Z'
originalURL: https://freecodecamp.org/news/search-and-filter-component-in-reactjs
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/wirxeocmd6tpnn9c5oqc.jpg
tags:
- name: create-react-app
  slug: create-react-app
- name: React
  slug: react
seo_title: Comment rechercher et filtrer des composants dans React
seo_desc: 'If you''re building a React app, you want your users to be able to search
  and get exact results. And if you are getting tons of items from an API, then you
  need to create a way for users to be able to find various items easily.

  For this tutorial we ar...'
---

Si vous construisez une application React, vous voulez que vos utilisateurs puissent rechercher et obtenir des résultats exacts. Et si vous obtenez des tonnes d'éléments depuis une API, alors vous devez créer un moyen pour que les utilisateurs puissent trouver facilement divers éléments.

Pour ce tutoriel, nous allons utiliser l'un des [projets API avancés gratuits de Frontend Mentor](https://www.frontendmentor.io/challenges/rest-countries-api-with-color-theme-switcher-5cacc469fec04111f7b848ca) comme exemple.

## Table des matières

1. Introduction
   
2. Comment configurer React
   
3. Comment récupérer les données
   
4. Comment rechercher des éléments dans l'API
   
5. Comment filtrer les éléments par région

# Introduction

Pour ce tutoriel, nous allons utiliser l'API gratuite [REST COUNTRIES API](https://restcountries.eu/) fournie par [Apilayer](https://apilayer.com/).

En gros, nous allons récupérer les données depuis notre endpoint API `https://restcountries.eu/rest/v2/all` et afficher les données sous une forme lisible par l'utilisateur.

Ensuite, nous fournirons un moyen pour que les utilisateurs puissent facilement rechercher des pays spécifiques par leurs noms et capitales. Voici un exemple de la réponse pour un pays particulier :

```json
[
  {
    "name": "Colombia",
    "topLevelDomain": [
      ".co"
    ],
    "alpha2Code": "CO",
    "alpha3Code": "COL",
    "callingCodes": [
      "57"
    ],
    "capital": "Bogotá",
    "altSpellings": [
      "CO",
      "Republic of Colombia",
      "República de Colombia"
    ],
    "region": "Americas",
    "subregion": "South America",
    "population": 48759958,
    "latlng": [
      4,
      -72
    ],
    "demonym": "Colombian",
    "area": 1141748,
    "gini": 55.9,
    "timezones": [
      "UTC-05:00"
    ],
    "borders": [
      "BRA",
      "ECU",
      "PAN",
      "PER",
      "VEN"
    ],
    "nativeName": "Colombia",
    "numericCode": "170",
    "currencies": [
      {
        "code": "COP",
        "name": "Colombian peso",
        "symbol": "$"
      }
    ],
    "languages": [
      {
        "iso639_1": "es",
        "iso639_2": "spa",
        "name": "Spanish",
        "nativeName": "Español"
      }
    ],
    "translations": {
      "de": "Kolumbien",
      "es": "Colombia",
      "fr": "Colombie",
      "ja": "コロンビア",
      "it": "Colombia",
      "br": "Colômbia",
      "pt": "Colômbia"
    },
    "flag": "https://restcountries.eu/data/col.svg",
    "regionalBlocs": [
      {
        "acronym": "PA",
        "name": "Pacific Alliance",
        "otherAcronyms": [],
        "otherNames": [
          "Alianza del Pacífico"
        ]
      },
      {
        "acronym": "USAN",
        "name": "Union of South American Nations",
        "otherAcronyms": [
          "UNASUR",
          "UNASUL",
          "UZAN"
        ],
        "otherNames": [
          "Unión de Naciones Suramericanas",
          "União de Nações Sul-Americanas",
          "Unie van Zuid-Amerikaanse Naties",
          "South American Union"
        ]
      }
    ],
    "cioc": "COL"
  }
]
```

À la fin de ce tutoriel, vous aurez appris comment rechercher dans une API et retourner uniquement les résultats demandés avec React.

# Comment configurer React

Nous allons utiliser `create-react-app` pour configurer notre projet car il offre une configuration de build moderne sans aucune configuration.

Pour configurer React, lancez votre terminal (soit celui fourni par votre système d'exploitation, soit vous pouvez utiliser un éditeur comme VS Code) et exécutez les commandes suivantes :

```bash
npx create-react-app my-app 
cd my-app 
npm start
```

Si vous n'êtes pas sûr de la manière de configurer correctement un projet `create-react-app`, vous pouvez vous référer au guide officiel ici à [create-react-app-dev](https://create-react-app.dev/docs/getting-started/).

Pour notre cas et pour afficher des résultats en direct dans ce tutoriel, nous allons utiliser [Codepen](https://codepen.io/) pour configurer notre projet. Vous pouvez le faire en utilisant un modèle Codepen de [Lathryx](https://codepen.io/MrMaster) :

%[https://codepen.io/MrMaster/pen/oNYWNjr] 

et voilà, nous avons React configuré dans Codepen.

## Comment récupérer les données depuis notre endpoint API

Maintenant que nous avons réussi à configurer notre projet React, il est temps de récupérer les données depuis notre API. Il existe de nombreuses façons de récupérer des données dans React, mais les deux plus populaires sont **Axios** (un client HTTP basé sur les promesses) et l'**API Fetch** (une API web intégrée au navigateur).

Nous allons utiliser l'`API Fetch` fournie par le navigateur et Ajax pour récupérer nos données depuis notre endpoint API. Voici un exemple utilisant les hooks de [Ajax et APIs par React](https://reactjs.org/docs/faq-ajax.html) :

```js
function MyComponent() {
      const [error, setError] = useState(null);
      const [isLoaded, setIsLoaded] = useState(false);
      const [items, setItems] = useState([]);

      // Note : le tableau de dépendances vide [] signifie
      // que cet useEffect s'exécutera une fois
      // similaire à componentDidMount()
      useEffect(() => {
        fetch("https://api.example.com/items")
          .then(res => res.json())
          .then(
            (result) => {
              setIsLoaded(true);
              setItems(result);
            },
            // Note : il est important de gérer les erreurs ici
            // au lieu d'un bloc catch() pour ne pas masquer
            // les exceptions des bugs réels dans les composants.
            (error) => {
              setIsLoaded(true);
              setError(error);
            }
          )
      }, [])

      if (error) {
        return <div>Erreur : {error.message}</div>;
      } else if (!isLoaded) {
        return <div>Chargement...</div>;
      } else {
        return (
          <ul>
            {items.map(item => (
              <li key={item.id}>
                {item.name} {item.price}
              </li>
            ))}
          </ul>
        );
      }
    }
```

Cela récupère les données depuis notre endpoint à la `ligne 10` et utilise ensuite `setState` pour mettre à jour notre composant lorsqu'il obtient les données.

À partir de la `ligne 27`, nous affichons un message d'erreur si la récupération des données depuis notre API échoue. Si elle ne échoue pas, nous affichons les données sous forme de liste.

Si vous n'êtes pas familier avec les listes React, je vous suggère de consulter ce guide sur les [Listes et Clés React](https://reactjs.org/docs/lists-and-keys.html).

Maintenant, utilisons ce code pour récupérer et afficher les données depuis notre API REST COUNTRIES.

À partir de l'exemple de code ci-dessus, nous voulons `importer useState depuis React` puis changer la `ligne 10` en :

`fetch("`[`https://restcountries.eu/rest/v2/all")`
](https://restcountries.eu/rest/v2/all"\)
)

Lorsque nous mettons tout ensemble, nous avons :

```js
import { useState, useEffect } from "https://cdn.skypack.dev/react";

    // Note : le tableau de dépendances vide [] signifie
    // que cet useEffect s'exécutera une fois
    function App() {
        const [error, setError] = useState(null);
        const [isLoaded, setIsLoaded] = useState(false);
        const [items, setItems] = useState([]);

        useEffect(() => {
            fetch("https://restcountries.eu/rest/v2/all")
                .then((res) => res.json())
                .then(
                    (result) => {
                        setIsLoaded(true);
                        setItems(result);
                    },
                    // Note : il est important de gérer les erreurs ici
                    // au lieu d'un bloc catch() pour ne pas masquer
                    // les exceptions des bugs réels dans les composants.
                    (error) => {
                        setIsLoaded(true);
                        setError(error);
                    }
                );
        }, []);
```

**Note :** nous importons `useState` et `useEffect` depuis `"`[`https://cdn.skypack.dev/react`](https://cdn.skypack.dev/react)`";`. Cela est dû au fait que nous utilisons un CDN pour importer React dans Codepen. Si vous configurez React localement, vous devriez utiliser `import { useState, useEffect } from "react";`.

Ensuite, nous voulons afficher nos données reçues sous forme de liste de pays. Le code final pour faire cela ressemble à ceci :

```js

    // Note : le tableau de dépendances vide [] signifie
    // que cet useEffect s'exécutera une fois
    function App() {
        const [error, setError] = useState(null);
        const [isLoaded, setIsLoaded] = useState(false);
        const [items, setItems] = useState([]);

        useEffect(() => {
            fetch("https://restcountries.eu/rest/v2/all")
                .then((res) => res.json())
                .then(
                    (result) => {
                        setIsLoaded(true);
                        setItems(result);
                    },
                    // Note : il est important de gérer les erreurs ici
                    // au lieu d'un bloc catch() pour ne pas masquer
                    // les exceptions des bugs réels dans les composants.
                    (error) => {
                        setIsLoaded(true);
                        setError(error);
                    }
                );
        }, []);

        if (error) {
            return <>{error.message}</>;
        } else if (!isLoaded) {
            return <>chargement...</>;
        } else {
            return (
                /* ici nous parcourons les éléments et affichons chaque item sous forme de carte  */
                <div className="wrapper">
                    <ul className="card-grid">
                        {items.map((item) => (
                            <li>
                                <article className="card" key={item.callingCodes}>
                                    <div className="card-image">
                                        <img src={item.flag} alt={item.name} />
                                    </div>
                                    <div className="card-content">
                                        <h2 className="card-name">{item.name}</h2>
                                        <ol className="card-list">
                                            <li>
                                                population:{" "}
                                                <span>{item.population}</span>
                                            </li>
                                            <li>
                                                Région: <span>{item.region}</span>
                                            </li>
                                            <li>
                                                Capitale: <span>{item.capital}</span>
                                            </li>
                                        </ol>
                                    </div>
                                </article>
                            </li>
                        ))}
                    </ul>
                </div>
            );
        }
    }

    ReactDOM.render(<App />, document.getElementById("root"));
```

Voici l'aperçu en direct de ceci dans Codepen :

%[https://codepen.io/Spruce_khalifa/pen/ZELeWoN] 

Maintenant que nous avons réussi à récupérer et afficher les données depuis notre API REST COUNTRIES, nous pouvons maintenant nous concentrer sur la recherche parmi les pays qui sont affichés.

Mais avant de faire cela, stylisons l'exemple ci-dessus avec CSS (car il a l'air laid lorsqu'il est affiché comme ceci).

Lorsque nous ajoutons du CSS à l'exemple ci-dessus, nous obtenons quelque chose qui ressemble à l'exemple ci-dessous :

%[https://codepen.io/Spruce_khalifa/pen/zYNZBBB] 

Bien que le CSS que nous avons ajouté ne soit pas parfait, il affiche les pays de manière plus ordonnée que précédemment, vous êtes d'accord ?

## Comment construire le composant de recherche

À l'intérieur de notre fonction APP, nous utilisons les hooks `useState()` pour définir la requête `q` comme une chaîne vide. Nous avons également `setQ` que nous utiliserons pour lier la valeur de notre formulaire de recherche.

À la `ligne 13`, nous utilisons `useState` pour définir un tableau de valeurs par défaut que nous voulons pouvoir rechercher depuis l'API. Cela signifie que nous voulons pouvoir rechercher n'importe quel pays par sa `Capitale` et son `nom` uniquement. Vous pouvez toujours rendre ce tableau plus long en fonction de vos préférences.

```js
        const [error, setError] = useState(null);
        const [isLoaded, setIsLoaded] = useState(false);
        const [items, setItems] = useState([]);

        //     définir la requête de recherche comme une chaîne vide
        const [q, setQ] = useState("");
        //     définir les paramètres de recherche
        //     nous voulons seulement rechercher les pays par capitale et nom
        //     cette liste peut être plus longue si vous le souhaitez
        //     vous pouvez rechercher des pays même par leur population
        // il suffit de l'ajouter à ce tableau
        const [searchParam] = useState(["capital", "name"]);

        useEffect(() => {
            // notre code de fetch
        }, []);

     }
```

À l'intérieur de notre fonction de retour, nous allons créer le formulaire de recherche et notre code ressemble maintenant à ceci :

```js
            return <>{error.message}</>;
        } else if (!isLoaded) {
            return <>chargement...</>;
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
                                value={q}
                                /*
                                // définir la valeur de notre useState q
                                //  à chaque fois que l'utilisateur tape dans la boîte de recherche
                                */
                                onChange={(e) => setQ(e.target.value)}
                            />
                            <span className="sr-only">Rechercher des pays ici</span>
                        </label>
                    </div>
                    <ul className="card-grid">
                        {items.map((item) => (
                            <li>
                                <article className="card" key={item.callingCodes}>
                                    <div className="card-image">
                                        <img src={item.flag} alt={item.name} />
                                    </div>
                                    <div className="card-content">
                                        <h2 className="card-name">{item.name}</h2>
                                        <ol className="card-list">
                                            <li>
                                                population:{" "}
                                                <span>{item.population}</span>
                                            </li>
                                            <li>
                                                Région: <span>{item.region}</span>
                                            </li>
                                            <li>
                                                Capitale: <span>{item.capital}</span>
                                            </li>
                                        </ol>
                                    </div>
                                </article>
                            </li>
                        ))}
                    </ul>
                </div>
            );
        }
    }

    ReactDOM.render(<App />, document.getElementById("root"));
```

Maintenant, nous allons créer une fonction pour gérer notre recherche et la placer au-dessus de notre retour (le code ci-dessus).

```js
            return items.filter((item) => {
                return searchParam.some((newItem) => {
                    return (
                        item[newItem]
                            .toString()
                            .toLowerCase()
                            .indexOf(q.toLowerCase()) > -1
                    );
                });
            });
        }
```

Cette fonction prend nos éléments récupérés et retourne tous les éléments qui correspondent à quelque chose dans notre tableau `searchParam` si l'`indexOF()` est `> -1`.

Maintenant que la fonction est configurée, pour l'utiliser, nous allons envelopper les données retournées avec notre fonction de recherche.

`{serach(items).map((item) => ( <li> // la carte va ici </li> ))}`

Maintenant, les données stockées dans notre `useState()` vont être filtrées dans notre fonction de recherche avant d'être passées aux éléments de la liste, ne retournant ainsi que les éléments qui correspondent à notre requête.

Voici le code lorsqu'il est assemblé et l'aperçu en direct sur Codepen. Essayez d'utiliser le formulaire de recherche ci-dessous pour rechercher n'importe quel pays par son nom ou sa capitale.

%[https://codepen.io/Spruce_khalifa/pen/wvgJWdO?editors=0010] 

## Comment filtrer les pays par région

Maintenant, nous pouvons aller plus loin en filtrant les pays par leur région. Supposons que nous ne voulons pas afficher tous les pays, nous voulons simplement afficher et pouvoir rechercher des pays uniquement en `Afrique` ou en `Asie`. Vous pouvez y parvenir en utilisant le hook `useState()` dans React.

### Régions :

1. Afrique
   
2. Amérique
   
3. Asie
   
4. Europe
   
5. Océanie

Maintenant que nous connaissons nos régions, créons notre composant de filtre. Tout d'abord, nous définissons le `useState` du filtre comme ceci :

`const [filterParam, setFilterParam] = useState(["All"]);`

Remarquez que nous définissons le useState par défaut à `ALL` intentionnellement, car nous voulons pouvoir afficher et rechercher tous les pays si aucune région n'est spécifiée.

```js
       <select
    /*
    // ici nous créons une entrée de sélection basique
    // nous définissons la valeur à la valeur sélectionnée
    // et mettons à jour l'état setFilterParam() chaque fois que onChange est appelé
    */
      onChange={(e) => {
      setFilterParam(e.target.value);
       }}
       className="custom-select"
       aria-label="Filtrer les pays par région">
        <option value="All">Filtrer par région</option>
        <option value="Africa">Afrique</option>
        <option value="Americas">Amérique</option>
        <option value="Asia">Asie</option>
        <option value="Europe">Europe</option>
        <option value="Oceania">Océanie</option>
        </select>
        <span className="focus"></span>
        </div>
```

Maintenant que nous avons créé notre filtre, il ne reste plus qu'à modifier la `fonction de recherche`. En gros, nous vérifions la région entrée et ne retournons que les pays qui ont cette région :

```js
function search(items) {
       return items.filter((item) => {
    /*
    // ici nous vérifions si notre région est égale à notre état c
    // si elle est égale, alors ne retourner que les éléments qui correspondent
    // sinon, retourner tous les pays
    */
       if (item.region == filterParam) {
           return searchParam.some((newItem) => {
             return (
               item[newItem]
                   .toString()
                   .toLowerCase()
                   .indexOf(q.toLowerCase()) > -1
                        );
                    });
                } else if (filterParam == "All") {
                    return searchParam.some((newItem) => {
                        return (
                            item[newItem]
                                .toString()
                                .toLowerCase()
                                .indexOf(q.toLowerCase()) > -1
                        );
                    });
                }
            });
        }
```

Vous pouvez trouver le code complet et l'aperçu en direct sur Codepen. Essayez de filtrer les pays et regardez les résultats.

%[https://codepen.io/Spruce_khalifa/pen/BapWzPe?editors=0010

] 

Une fois que nous avons ajouté un peu de CSS, nous pouvons maintenant voir l'aperçu final de notre application React.

%[https://codepen.io/Spruce_khalifa/pen/GRrWjmR?editors=0010] 

# Conclusion

Lorsque vous traitez avec un grand ensemble de données que vous devez afficher à un utilisateur, les fonctions de recherche et de filtrage aident cet utilisateur à naviguer et à trouver rapidement des informations importantes.

Si vous avez des questions, vous pouvez me contacter et je serai ravi de discuter.

Vous pouvez trouver l'aperçu complet de ce projet ici à [earthly vercel app](https://earthly.vercel.app). Vous pouvez me suivre sur [Twitter @sprucekhalifa](https://twitter.com/sprucekhalifa).