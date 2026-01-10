---
title: Comment créer un clone de Hacker News en utilisant React
subtitle: ''
author: Yogesh Chavan
co_authors: []
series: null
date: '2021-02-12T18:22:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-hacker-news-clone-using-react
coverImage: https://cdn-media-2.freecodecamp.org/w1280/60262bb70a2838549dcc42b6.jpg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: Comment créer un clone de Hacker News en utilisant React
seo_desc: 'In this tutorial, we will build a mini Hacker News clone in React.

  We will be using React Hooks syntax for building this application. So if you''re
  new to React Hooks, check out my Introduction to React Hooks article to learn the
  basics of Hooks.

  So l...'
---

Dans ce tutoriel, nous allons créer un mini clone de [Hacker News](https://news.ycombinator.com/) en React.

Nous utiliserons la syntaxe des Hooks React pour construire cette application. Si vous êtes nouveau dans les Hooks React, consultez mon article [Introduction aux Hooks React](https://levelup.gitconnected.com/an-introduction-to-react-hooks-50281fd961fe?source=friends_link&sk=89baff89ec8bc637e7c13b7554904e54) pour apprendre les bases des Hooks.

Alors, commençons.

## Introduction à l'API

Nous utiliserons l'API Hackernews depuis [cette url](https://github.com/HackerNews/API).

API pour obtenir les meilleures histoires, utilisez cette URL : [https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty](https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty)

API pour obtenir les nouvelles histoires, utilisez cette URL : [https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty](https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty)

API pour obtenir les meilleures histoires, utilisez cette URL : [https://hacker-news.firebaseio.com/v0/beststories.json?print=pretty](https://hacker-news.firebaseio.com/v0/beststories.json?print=pretty)

Chacune des API d'histoires ci-dessus retourne uniquement un tableau d'ID représentant une histoire.

Ainsi, pour obtenir les détails de cette histoire particulière, nous devons faire un autre appel API.

API pour obtenir les détails de l'histoire, utilisez cette URL : [https://hacker-news.firebaseio.com/v0/item/story_id.json?print=pretty](https://hacker-news.firebaseio.com/v0/item/story_id.json?print=pretty)

Par exemple : [https://hacker-news.firebaseio.com/v0/item/26061935.json?print=pretty](https://hacker-news.firebaseio.com/v0/item/26061935.json?print=pretty)

## Comment configurer le projet

Créez un nouveau projet en utilisant `create-react-app` :

```js
npx create-react-app hackernews-clone-react-app
```

Une fois le projet créé, supprimez tous les fichiers du dossier `src` et créez les fichiers `index.js` et `styles.scss` à l'intérieur du dossier `src`. Créez également les dossiers `components`, `hooks`, `router`, `utils` à l'intérieur du dossier `src`.

Installez les dépendances requises comme ceci :

```js
yarn add axios@0.21.0 bootstrap@4.6.0 node-sass@4.14.1 react-bootstrap@1.4.0 react-router-dom@5.2.0
```

Ouvrez `styles.scss` et ajoutez le contenu depuis [ici](https://github.com/myogeshchavan97/hackernews-clone-react-app/blob/master/src/styles.scss) à l'intérieur.

Nous utiliserons la syntaxe SCSS pour écrire du CSS. Si vous êtes nouveau dans SCSS, consultez [mon article ici](https://medium.com/better-programming/an-introduction-to-sass-scss-fdbda159b40?source=friends_link&sk=c0846e19ddb4f53919a6abaf29032d10) pour une introduction.

## Comment créer les pages initiales

Créez un nouveau fichier `Header.js` à l'intérieur du dossier `components` avec le contenu suivant :

```jsx
import React from 'react';
import { NavLink } from 'react-router-dom';

const Header = () => {
  return (
    <React.Fragment>
      <h1>Clone de Hacker News</h1>
      <div className="nav-link">
        <NavLink to="/top" activeClassName="active">
          Meilleurs Articles
        </NavLink>
        <NavLink to="/new" activeClassName="active">
          Derniers Articles
        </NavLink>
        <NavLink to="/best" activeClassName="active">
          Articles Populaires
        </NavLink>
      </div>
    </React.Fragment>
  );
};

export default Header;
```

Dans ce fichier, nous avons ajouté un menu de navigation pour voir les différents types d'histoires. Chaque lien a ajouté une classe `active`. Ainsi, lorsque nous cliquons sur ce lien, il sera mis en surbrillance, indiquant sur quelle route nous nous trouvons.

Créez un nouveau fichier `HomePage.js` à l'intérieur du dossier `components` avec le contenu suivant :

```jsx
import React from 'react';

const HomePage = () => {
  return <React.Fragment>Page d'accueil</React.Fragment>;
};

export default HomePage;
```

Créez un nouveau fichier `PageNotFound.js` à l'intérieur du dossier `components` avec le contenu suivant :

```jsx
import React from 'react';
import { Link } from 'react-router-dom';

const PageNotFound = () => {
  return (
    <p>
      Page non trouvée. Allez à <Link to="/">Accueil</Link>
    </p>
  );
};

export default PageNotFound;
```

Créez un nouveau fichier `AppRouter.js` à l'intérieur du dossier `router` avec le contenu suivant :

```jsx
import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import Header from '../components/Header';
import HomePage from '../components/HomePage';
import PageNotFound from '../components/PageNotFound';

const AppRouter = () => {
  return (
    <BrowserRouter>
      <div className="container">
        <Header />
        <Switch>
          <Route path="/" component={HomePage} exact={true} />
          <Route component={PageNotFound} />
        </Switch>
      </div>
    </BrowserRouter>
  );
};

export default AppRouter;
```

Dans ce fichier, initialement, nous avons ajouté deux routes pour le routage – une pour la page d'accueil et l'autre pour les routes invalides.

Si vous êtes nouveau dans React Router, consultez mon cours gratuit [Introduction à React Router](https://yogeshchavan1.podia.com/react-router-introduction).

Maintenant, ouvrez le fichier `src/index.js` et ajoutez le contenu suivant à l'intérieur :

```jsx
import React from 'react';
import ReactDOM from 'react-dom';
import AppRouter from './router/AppRouter';
import 'bootstrap/dist/css/bootstrap.min.css';
import './styles.scss';

ReactDOM.render(<AppRouter />, document.getElementById('root'));
```

Maintenant, démarrez l'application en exécutant la commande `yarn start` et vous verrez l'écran suivant :

![Écran initial](https://gist.github.com/myogeshchavan97/aa75611665802aadfd3ba6bfeb0fe59b/raw/06ff931efc03ef42cd70a8a44c0dd211a53f5a59/initial_page_1.png)

## Intégration de l'API

Maintenant, à l'intérieur du dossier `utils`, créez un nouveau fichier appelé `constants.js` avec le contenu suivant :

```js
export const BASE_API_URL = 'https://hacker-news.firebaseio.com/v0';
```

Créez un autre fichier avec le nom `apis.js` à l'intérieur du dossier `utils` avec le contenu suivant :

```jsx
import axios from 'axios';
import { BASE_API_URL } from './constants';

const getStory = async (id) => {
  try {
    const story = await axios.get(`${BASE_API_URL}/item/${id}.json`);
    return story;
  } catch (error) {
    console.log('Erreur lors de la récupération d\'une histoire.');
  }
};

export const getStories = async (type) => {
  try {
    const { data: storyIds } = await axios.get(
      `${BASE_API_URL}/${type}stories.json`
    );
    const stories = await Promise.all(storyIds.slice(0, 30).map(getStory));
    return stories;
  } catch (error) {
    console.log('Erreur lors de la récupération de la liste des histoires.');
  }
};
```

Dans ce fichier, pour la fonction `getStories`, nous passons le type d'histoire que nous voulons (`top`, `new` ou `best`). Ensuite, nous faisons un appel API à l'URL `.json` respective fournie au début de cet article.

Notez que nous avons déclaré la fonction comme `async` afin de pouvoir utiliser le mot-clé `await` pour appeler l'API et attendre que la réponse arrive.

```js
const { data: storyIds } = await axios.get(
  `${BASE_API_URL}/${type}stories.json`
);
```

Comme la bibliothèque `axios` retourne toujours le résultat dans la propriété `.data` de la réponse, nous extrayons cette propriété et la renommons en `storyIds` car l'API retourne un tableau d'ID d'histoires.

Ici, nous utilisons la syntaxe de déstructuration ES6 pour renommer la propriété `data` en `storyIds`. Cela facilite la compréhension de ce que contient `storyIds` plutôt que de l'appeler `data`.

Notez que le code ci-dessus est le même que le code ci-dessous :

```js
const response = await axios.get(
  `${BASE_API_URL}/${type}stories.json`
);
const storyIds = response.data;
```

Puisque nous obtenons un tableau d'ID d'histoires en retour, au lieu de faire des appels API séparés pour chaque `id` et d'attendre que le précédent se termine, nous utilisons la méthode `Promise.all` pour faire des appels API simultanément pour tous les ID d'histoires.

```js
const stories = await Promise.all(
  storyIds.slice(0, 30).map((storyId) => getStory(storyId))
);
```

Ici, nous utilisons la méthode Array slice pour ne prendre que les 30 premiers ID d'histoires afin que les données se chargent plus rapidement.

Ensuite, nous utilisons la méthode Array map pour appeler la fonction `getStory` afin de faire un appel API à l'élément d'histoire individuel en lui passant le `storyId`.

Comme dans la fonction map, nous prenons simplement le storyId et le passons à la fonction `getStory`. Nous pouvons le simplifier avec le code suivant :

```js
const stories = await Promise.all(storyIds.slice(0, 30).map(getStory));
```

Ainsi, le `storyId` sera automatiquement passé à la fonction `getStory`.

À l'intérieur de la fonction `getStory`, nous utilisons la syntaxe des littéraux de gabarit ES6 pour créer une URL dynamique basée sur l'ID passé pour faire un appel API.

Et une fois que nous avons les histoires disponibles, nous les retournons depuis la fonction `getStories`.

## Comment créer le récupérateur de données

Créez un nouveau fichier `dataFetcher.js` à l'intérieur du dossier `hooks` avec le contenu suivant :

```jsx
import { useState, useEffect } from 'react';
import { getStories } from '../utils/apis';

const useDataFetcher = (type) => {
  const [stories, setStories] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    setIsLoading(true);
    getStories(type)
      .then((stories) => {
        setStories(stories);
        setIsLoading(false);
      })
      .catch(() => {
        setIsLoading(false);
      });
  }, [type]);

  return { isLoading, stories };
};

export default useDataFetcher;
```

Dans ce fichier, nous avons déclaré un hook personnalisé `useDataFetcher` qui prend le type d'histoire comme paramètre et appelle la fonction `getStories` définie dans le fichier `apis.js` à l'intérieur du hook `useEffect`.

Nous avons ajouté deux variables d'état ici en utilisant le hook `useState`, à savoir `stories` et `isLoading`. Avant de faire l'appel API, nous définissons l'état `isLoading` sur `true`. Une fois que nous obtenons la réponse complète, nous le définissons sur `false`.

Nous définissons également l'état `isLoading` sur `false` à l'intérieur du bloc catch afin que si une erreur se produit, le chargeur sera masqué.

Une fois la réponse reçue, nous définissons le tableau `stories` avec la réponse de l'API et nous retournons `isLoading` et `stories` depuis le hook dans un objet. Cela signifie que tout composant utilisant ce hook pourra obtenir la valeur mise à jour de ces valeurs d'état.

De plus, notez que nous avons ajouté `type` comme dépendance au hook `useEffect` en tant que deuxième paramètre à l'intérieur du tableau. Ainsi, chaque fois que nous cliquons sur le menu de navigation (pour les histoires `top`, `latest` ou `best`), le type changera et ce hook `useEffect` s'exécutera à nouveau pour faire un appel API afin d'obtenir les histoires liées à ce type.

Si vous vous souvenez, à l'intérieur du fichier `apis.js`, la fonction `getStories` est déclarée comme `async`, donc elle retournera toujours une promesse. Par conséquent, nous avons ajouté le gestionnaire `.then` à la fonction `getStories` pour obtenir les données réelles de la réponse à l'intérieur du hook `useEffect` à l'intérieur du fichier `dataFetcher.js` comme ceci :

```js
getStories(type)
      .then((stories) => {
      ...
```

## Comment afficher les données dans l'interface utilisateur

Maintenant, créez un nouveau fichier appelé `ShowStories.js` à l'intérieur du dossier `components` avec le contenu suivant :

```jsx
import React from 'react';
import Story from './Story';
import useDataFetcher from '../hooks/dataFetcher';

const ShowStories = (props) => {
  const { type } = props.match.params;
  const { isLoading, stories } = useDataFetcher(type);

  return (
    <React.Fragment>
      {isLoading ? (
        <p className="loading">Chargement...</p>
      ) : (
        <React.Fragment>
          {stories.map(({ data: story }) => (
            <Story key={story.id} story={story} />
          ))}
        </React.Fragment>
      )}
    </React.Fragment>
  );
};

export default ShowStories;
```

Dans ce fichier, nous utilisons le hook personnalisé `useDataFetcher` à l'intérieur du composant. En fonction du drapeau `isLoading`, nous affichons soit le message `Chargement` soit la liste des histoires en utilisant la méthode Array map pour chaque histoire individuelle.

Créez un nouveau fichier `Story.js` à l'intérieur du dossier `components` avec le contenu suivant :

```jsx
import React from 'react';

const Link = ({ url, title }) => (
  <a href={url} target="_blank" rel="noreferrer">
    {title}
  </a>
);

const Story = ({ story: { id, by, title, kids, time, url } }) => {
  return (
    <div className="story">
      <div className="story-title">
        <Link url={url} title={title} />
      </div>
      <div className="story-info">
        <span>
          par{' '}
          <Link url={`https://news.ycombinator.com/user?id=${by}`} title={by} />
        </span>
        |<span>
          {new Date(time * 1000).toLocaleDateString('fr-FR', {
            hour: 'numeric',
            minute: 'numeric'
          })}
        </span>|
        <span>
          <Link
            url={`https://news.ycombinator.com/item?id=${id}`}
            title={`${kids && kids.length > 0 ? kids.length : 0} commentaires`}
          />
        </span>
      </div>
    </div>
  );
};

export default Story;
```

Dans ce fichier, nous affichons l'histoire individuelle.

Pour définir le composant `Link`, nous utilisons la syntaxe raccourcie de la fonction fléchée ES6 de retour implicite.

Ainsi, le code ci-dessous :

```jsx
const Link = ({ url, title }) => (
  <a href={url} target="_blank" rel="noreferrer">
    {title}
  </a>
);
```

est le même que ce code :

```jsx
const Link = ({ url, title }) => {
  return (
    <a href={url} target="_blank" rel="noreferrer">
     {title}
    </a>
  );
}
```

Dans une fonction fléchée, si une instruction est sur une seule ligne, nous pouvons omettre les accolades et le mot-clé return.

Ainsi, le code ci-dessous :

```js
const add = (a,b) => a + b;
```

est le même que ce code :

```js
const add = (a,b) => {
  return a + b;
}
```

Mais pour que le JSX paraisse net et comme une instruction sur une seule ligne, nous ajoutons les parenthèses supplémentaires lors de la définition du composant `Link`.

Ensuite, pour le composant `Story`, nous l'avons défini comme ceci :

```jsx
const Story = ({ story: { id, by, title, kids, time, url } }) => {
  // du code
}
```

Ici, nous utilisons la syntaxe de déstructuration ES6 pour obtenir les propriétés de l'objet story qui a été passé depuis le composant `ShowStories`.

Ainsi, le code ci-dessus est le même que le code ci-dessous :

```jsx
const Story = (props) => {
  const { id, by, title, kids, time, url } = props.story;
  // du code
}
```

qui est le même que le code ci-dessous :

```jsx
const Story = ({ story }) => {
  const { id, by, title, kids, time, url } = story;
  // du code
}
```

Dans la réponse de l'API, nous obtenons l'heure de l'histoire en secondes. Ainsi, dans le composant `Story`, nous la multiplions par 1000 pour la convertir en millisecondes afin de pouvoir afficher la date correcte dans le bon format en utilisant la méthode `toLocaleDateString` de JavaScript :

```js
{new Date(time * 1000).toLocaleDateString('fr-FR', {
  hour: 'numeric',
  minute: 'numeric'
})}
```

Maintenant, ouvrez le fichier `AppRouter.js` et ajoutez une autre Route pour le composant `ShowStories` avant la Route `PageNotFound`.

```jsx
<Switch>
  <Route path="/" component={HomePage} exact={true} />
  <Route path="/:type" component={ShowStories} />
  <Route component={PageNotFound} />
</Switch>
```

Ajoutez également une importation pour le composant `ShowStories` en haut :

```js
import ShowStories from '../components/ShowStories';
```

Maintenant, redémarrez l'application en exécutant la commande `yarn start` et vérifiez l'application.

![Chargement des nouvelles](https://gist.github.com/myogeshchavan97/aa75611665802aadfd3ba6bfeb0fe59b/raw/06ff931efc03ef42cd70a8a44c0dd211a53f5a59/working_navigation.gif)

Comme vous pouvez le voir, l'application charge correctement les meilleures, les dernières et les meilleures histoires depuis l'API HackerNews.

## Comment gérer la redirection dynamique

Si vous vous souvenez, nous avons ajouté le composant `HomePage` pour afficher quelque chose lorsque l'application se charge. Mais maintenant, nous n'avons plus besoin du composant `HomePage`, car nous pouvons afficher la page des meilleures histoires lorsque l'application se charge.

Alors, ouvrez le fichier `AppRouter.js` et changez les deux premières routes du code ci-dessous :

```jsx
<Route path="/" component={HomePage} exact={true} />
<Route path="/:type" component={ShowStories} />
```

en ce code :

```jsx
<Route path="/" render={() => <Redirect to="/top" />} exact={true} />
<Route
  path="/:type"
  render={({ match }) => {
    const { type } = match.params;
    if (!['top', 'new', 'best'].includes(type)) {
       return <Redirect to="/" />;
    }
    return <ShowStories type={type} />;
  }}
/>
```

Dans la première Route, lorsque nous chargeons l'application en visitant `http://localhost:3000/`, nous redirigeons l'utilisateur vers la route `/top`.

```jsx
<Route path="/" render={() => <Redirect to="/top" />} exact={true} />
```

Ici, nous utilisons le motif des props de rendu. Ainsi, au lieu de fournir un composant, nous utilisons une prop avec le nom `render` où nous pouvons écrire le code du composant directement à l'intérieur de la fonction.

Pour savoir pourquoi nous utilisons `render` au lieu de la prop `component` et quel problème cela résout, consultez mon cours gratuit [Introduction à React Router](https://yogeshchavan1.podia.com/react-router-introduction).

Ensuite, nous avons ajouté une route `/:type` :

```jsx
<Route
  path="/:type"
  render={({ match }) => {
    const { type } = match.params;
    if (!['top', 'new', 'best'].includes(type)) {
      return <Redirect to="/" />;
    }
    return <ShowStories type={type} />;
  }}
/>
```

Ici, si la route correspond à `/top` ou `/new` ou `/best`, nous montrons à l'utilisateur le composant `ShowStories`. Si l'utilisateur entre une valeur invalide pour une route comme `/something`, nous redirigerons l'utilisateur vers la route `/top` qui rendra le composant `ShowStories` avec les histoires `top`.

Nous utilisons la méthode Array `includes` ES7 dans le code ci-dessus à l'intérieur de la condition if.

Par défaut, le routeur React passe certaines props à chaque composant mentionné dans `<Route />`. L'une d'entre elles est `match`, donc `props.match.params` contiendra la valeur réelle passée pour le `type`.

Par conséquent, lorsque nous accédons à `http://localhost:3000/top`, `props.match.params` contiendra la valeur `top`. Lorsque nous accédons à `http://localhost:3000/new`, `props.match.params` contiendra la valeur `new`, et ainsi de suite.

Pour la fonction de prop de rendu, nous utilisons la déstructuration pour obtenir la propriété `match` de l'objet props en utilisant la syntaxe suivante :

```jsx
render={({ match }) => {
}
```

qui est la même chose que :

```jsx
render={(props) => {
 const { match } = props;
}
```

De plus, n'oubliez pas d'importer le composant `Redirect` depuis le package `react-router-dom` en haut du fichier `AppRouter.js`.

```jsx
import { BrowserRouter, Redirect, Route, Switch } from 'react-router-dom';
```

Maintenant, ouvrez le fichier `ShowStories.js` et changez le code ci-dessous :

```jsx
const ShowStories = (props) => {
  const { type } = props.match.params;
  const { isLoading, stories } = useDataFetcher(type);
```

en ce code :

```jsx
const ShowStories = ({ type }) => {
  const { isLoading, stories } = useDataFetcher(type ? type : 'top');
```

Ici, nous passons la prop `type` passée depuis le composant `AppRouter` au hook personnalisé `useDataFetcher`. Cela rendra le bon type de données, en fonction du `type` passé.

## Comment ajouter un overlay de chargement

Maintenant, nous avons ajouté un code de redirection pour rediriger automatiquement vers la route `/top` au chargement de l'application. La route invalide redirige également vers la route `/top`.

Mais lorsque les données sont en cours de chargement, nous affichons un simple message de chargement. Pendant que les données sont en cours de chargement, l'utilisateur peut cliquer sur un autre lien pour faire des requêtes supplémentaires au serveur, ce qui n'est pas bon.

Alors, ajoutons le message de chargement avec un overlay à l'écran afin que l'utilisateur ne puisse pas cliquer nulle part pendant le chargement des données.

Créez un nouveau fichier `Loader.js` à l'intérieur du dossier `components` avec le contenu suivant :

```jsx
import { useState, useEffect } from 'react';
import ReactDOM from 'react-dom';

const Loader = (props) => {
  const [node] = useState(document.createElement('div'));
  const loader = document.querySelector('#loader');

  useEffect(() => {
    loader.appendChild(node).classList.add('message');
  }, [loader, node]);

  useEffect(() => {
    if (props.show) {
      loader.classList.remove('hide');
      document.body.classList.add('loader-open');
    } else {
      loader.classList.add('hide');
      document.body.classList.remove('loader-open');
    }
  }, [loader, props.show]);

  return ReactDOM.createPortal(props.children, node);
};

export default Loader;
```

Maintenant, ouvrez le fichier `public/index.html` et à côté de la div avec l'id `root`, ajoutez une autre div avec l'id `loader`, comme ceci :

```js
<div id="root"></div>
<div id="loader"></div>
```

La méthode `ReactDOM.createPortal` que nous avons utilisée dans `Loader.js` insérera le loader à l'intérieur de la div avec l'id `loader`, donc il sera en dehors de la hiérarchie DOM de notre application `React`. Cela signifie que nous pouvons l'utiliser pour fournir un overlay pour toute notre application. C'est la raison principale de l'utilisation du `React Portal` pour créer un loader.

Ainsi, même si nous incluons le composant `Loader` dans le fichier `ShowStories.js`, il sera rendu en dehors de toutes les divs (mais à l'intérieur de la div avec l'id `loader`).

Dans le fichier `Loader.js`, nous avons d'abord créé une div où nous ajouterons un message de loader

```js
const [node] = useState(document.createElement('div'));
```

Ensuite, nous ajoutons la classe `message` à cette div et enfin nous ajoutons cette div à la div loader ajoutée dans `index.html` :

```js
document.querySelector('#loader').appendChild(node).classList.add('message');
```

et en fonction de la prop `show` passée depuis le composant `ShowStories`, nous ajouterons ou supprimerons la classe `hide`. Ensuite, nous rendrons enfin le composant `Loader` en utilisant ceci :

```js
ReactDOM.createPortal(props.children, node);
```

Ensuite, nous ajoutons ou supprimons la classe `loader-open` de la balise body de la page, ce qui désactivera ou activera le défilement de la page :

```js
document.body.classList.add('loader-open');
document.body.classList.remove('loader-open');
```

Les données que nous passons entre les balises d'ouverture et de fermeture `Loader` à l'intérieur du composant `ShowStories` seront disponibles à l'intérieur de `props.children`. Ainsi, nous pouvons afficher un simple message de chargement ou nous pouvons inclure une image à afficher comme loader.

Maintenant, utilisons ce composant.

Ouvrez le fichier `ShowStories.js` et remplacez son contenu par le contenu suivant :

```jsx
import React from 'react';
import Story from './Story';
import useDataFetcher from '../hooks/dataFetcher';
import Loader from './Loader';

const ShowStories = (props) => {
  const { type } = props.match.params;
  const { isLoading, stories } = useDataFetcher(type);

  return (
    <React.Fragment>
      <Loader show={isLoading}>Chargement...</Loader>
      <React.Fragment>
        {stories.map(({ data: story }) => (
          <Story key={story.id} story={story} />
        ))}
      </React.Fragment>
    </React.Fragment>
  );
};

export default ShowStories;
```

Ici, nous utilisons le composant Loader en lui passant la prop show.

```jsx
<Loader show={isLoading}>Chargement...</Loader>
```

Maintenant, si vous vérifiez l'application, vous verrez l'overlay de chargement :

![Overlay de chargement](https://gist.github.com/myogeshchavan97/aa75611665802aadfd3ba6bfeb0fe59b/raw/06ff931efc03ef42cd70a8a44c0dd211a53f5a59/loader.gif)

Ainsi, maintenant l'utilisateur ne peut pas cliquer sur aucun lien pendant le chargement des données, ce qui est une belle amélioration.

Pour chaque histoire, nous affichons l'auteur et le nombre total de commentaires sous forme de liens hypertextes. En cliquant dessus, nous sommes redirigés vers le site web Hackernews pour afficher les détails respectifs comme vous pouvez le voir dans le gif ci-dessous.

![Liens hypertextes fonctionnels](https://gist.github.com/myogeshchavan97/aa75611665802aadfd3ba6bfeb0fe59b/raw/06ff931efc03ef42cd70a8a44c0dd211a53f5a59/links.gif)

## Points de conclusion

Nous avons terminé la construction de la fonctionnalité de l'application.

Vous pouvez trouver le code source complet de GitHub [ici](https://github.com/myogeshchavan97/hackernews-clone-react-app), et une démonstration en direct [ici](https://hackernews-clone-react-app.netlify.app/).

Pour aller plus loin dans vos compétences, vous pouvez améliorer l'application en ajoutant des fonctionnalités supplémentaires comme :

* Ajouter une fonctionnalité de pagination pour charger les 30 prochains enregistrements pour chaque page
* Créer une page séparée dans l'application pour afficher les commentaires en utilisant l'[API Hacker News](https://github.com/HackerNews/API). Lorsque vous cliquez dessus, le nombre de commentaires compte le lien au lieu de rediriger l'utilisateur vers le site web Hackernews

### Merci d'avoir lu !

Vous voulez construire plus de projets incroyables ? Consultez-les [ici](https://github.com/myogeshchavan97#choose-pinned-repositories).

De plus, vous pouvez consulter mon cours gratuit [Introduction à React Router](https://yogeshchavan1.podia.com/react-router-introduction) pour apprendre React Router à partir de zéro.

Vous voulez apprendre toutes les fonctionnalités ES6+ en détail, y compris let et const, les promesses, diverses méthodes de promesses, la déstructuration de tableaux et d'objets, les fonctions fléchées, async/await, import et export et bien plus encore ?

Consultez mon livre [Maîtriser le JavaScript Moderne](https://yogeshchavan1.podia.com/mastering-modern-javascript?coupon=LA1HR55). Ce livre couvre tous les prérequis pour apprendre React et vous aide à devenir meilleur en JavaScript et React.

**N'oubliez pas de vous abonner à ma [newsletter hebdomadaire](https://yogeshchavan.dev) pour obtenir des conseils, astuces, articles et offres de réduction incroyables directement dans votre boîte de réception.**