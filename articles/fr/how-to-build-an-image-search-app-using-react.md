---
title: Comment construire une application de recherche d'images avec React – Un tutoriel
  approfondi
subtitle: ''
author: Yogesh Chavan
co_authors: []
series: null
date: '2023-09-30T11:30:22.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-image-search-app-using-react
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/unsplash_image_search_app.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: Comment construire une application de recherche d'images avec React – Un
  tutoriel approfondi
seo_desc: 'In this article, we will build step-by-step a beautiful Unsplash Image
  Search App with pagination using React.

  By building this app, you will learn:


  How to build an application using Unsplash API in React

  How to make API Calls in different scenarios...'
---

Dans cet article, nous allons construire étape par étape une belle application de recherche d'images Unsplash avec pagination en utilisant React.

En construisant cette application, vous apprendrez :

* Comment construire une application en utilisant l'API Unsplash dans React
* Comment faire des appels API dans différents scénarios
* Comment utiliser le hook `useCallback` pour éviter la recréation de fonctions
* Comment utiliser ESLint pour corriger les problèmes de l'application
* Comment implémenter la pagination dans React

et bien plus encore...

Vous voulez regarder la version vidéo de ce tutoriel ? Vous pouvez consulter la vidéo ci-dessous :

%[https://www.youtube.com/watch?v=0YoT44j3Jg4&list=PLSJnlFr3D-mFm7-cdhnHdBvUdxUp-a9HL&index=17]

## Configuration initiale du projet

Nous allons utiliser [Vite](https://vitejs.dev/) pour créer un projet qui est une alternative populaire à `create-react-app`.

Exécutez la commande suivante pour créer un projet vite :

```js
npm create vite
```

Une fois exécuté, il vous sera posé quelques questions.

Pour le nom du projet, entrez `unsplash_image_search`.

Pour le framework, sélectionnez `React` et pour la variante, sélectionnez `JavaScript` :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/2_create_project.png)
_Création du projet avec Vite_

Une fois le projet créé, ouvrez le projet dans VS Code et exécutez les commandes suivantes depuis le terminal :

```js
cd unsplash_image_search
npm install
npm run dev
```

Accédez à l'application en naviguant vers [http://127.0.0.1:5173/](http://127.0.0.1:5173/).

![Image](https://www.freecodecamp.org/news/content/images/2023/09/3_project_started.png)
_Application démarrée_

Vous verrez l'écran de l'application par défaut comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/1_app_screen.png)
_Écran initial_

Ensuite, supprimez le fichier `App.css` et remplacez le contenu du fichier `App.jsx` par le contenu suivant :

```jsx
import React from 'react';
import './index.css';

const App = () => {
  return <div>Bienvenue dans la recherche d'images Unsplash</div>;
};

export default App;
```

Maintenant, ouvrez le fichier `index.css` et ajoutez le contenu de [ce dépôt GitHub](https://github.com/myogeshchavan97/unsplash_image_search/blob/master/src/index.css).

Installons les packages npm [Bootstrap](https://getbootstrap.com/) et [react-bootstrap](https://react-bootstrap.netlify.app/) en exécutant la commande suivante :

```js
npm install bootstrap react-bootstrap
```

Ouvrez le fichier `main.jsx` et ajoutez la ligne de code suivante en première ligne, pour ajouter le fichier CSS de base de bootstrap :

```js
import 'bootstrap/dist/css/bootstrap.min.css';
```

Le fichier complet `main.jsx` ressemblera à ceci :

```jsx
import 'bootstrap/dist/css/bootstrap.min.css';
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App.jsx';
import './index.css';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

Maintenant, redémarrez l'application en exécutant la commande `npm run dev`.

Vous verrez le message de bienvenue affiché à l'écran comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/4_initial_screen.png)
_Écran de bienvenue_

## Comment ajouter une entrée de recherche

Maintenant, remplacez le contenu du fichier `App.jsx` par le contenu suivant :

```jsx
import React from 'react';
import { Form } from 'react-bootstrap';
import './index.css';

const App = () => {
  return (
    <div className='container'>
      <h1 className='title'>Recherche d'images</h1>
      <div className='search-section'>
        <Form>
          <Form.Control
            type='search'
            placeholder='Tapez quelque chose pour rechercher...'
            className='search-input'
          />
        </Form>
      </div>
    </div>
  );
};

export default App;
```

Ici, nous affichons le titre de `Recherche d'images` à l'intérieur d'une classe `container`, qui est une classe Bootstrap, pour ajouter une marge à gauche et à droite de la page.

Ensuite, nous avons ajouté un [formulaire](https://react-bootstrap.netlify.app/docs/forms/overview/) avec un type de `search`.

Si vous vérifiez l'application, vous verrez l'écran suivant :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/5_searchbox.png)
_Interface utilisateur de recherche initiale_

Maintenant, nous devons stocker la valeur entrée par l'utilisateur quelque part dans le composant.

Comme nous n'aurons qu'un seul champ de saisie sur la page, nous utiliserons le hook [useRef](https://react.dev/reference/react/useRef) au lieu du hook `useState`.

L'utilisation du hook `useRef` ne réaffiche pas le composant lorsque sa valeur change, ce qui est bon pour l'amélioration des performances. En revanche, le changement d'état réaffiche le composant, donc tous les composants enfants seront également réaffichés.

À l'intérieur du fichier `App.jsx`, déclarez le hook `useRef` comme montré ci-dessous :

```jsx
const searchInput = useRef(null);
```

N'oubliez pas d'ajouter l'import pour le hook `useRef` en haut du fichier :

```jsx
import React, { useRef } from 'react';
```

Ajoutez également une prop `ref` pour l'entrée de recherche, comme ceci :

```jsx
<Form.Control
   type='search'
   placeholder='Tapez quelque chose pour rechercher...'
   className='search-input'
   ref={searchInput}
/>
```

Votre fichier complet `App.jsx` ressemblera à ceci :

```jsx
import React, { useRef } from 'react';
import { Form } from 'react-bootstrap';
import './index.css';

const App = () => {
  const searchInput = useRef(null);
  return (
    <div className='container'>
      <h1 className='title'>Recherche d'images</h1>
      <div className='search-section'>
        <Form>
          <Form.Control
            type='search'
            placeholder='Tapez quelque chose pour rechercher...'
            className='search-input'
            ref={searchInput}
          />
        </Form>
      </div>
    </div>
  );
};

export default App;
```

## Comment gérer l'action de soumission du formulaire

Lorsque nous entrons un terme de recherche dans la boîte de recherche et que nous appuyons sur la touche Entrée, nous voulons ajouter la fonctionnalité de recherche.

Pour ce faire, ajoutez un gestionnaire `onSubmit` à la balise `Form` et créez une méthode `handleSearch`. Et attribuez-la à la prop `onSubmit` comme ceci :

```jsx
import React, { useRef } from 'react';
import { Form } from 'react-bootstrap';
import './index.css';

const App = () => {
  const searchInput = useRef(null);

  const handleSearch = (event) => {
    event.preventDefault();
    console.log('soumis');
  };

  return (
    <div className='container'>
      <h1 className='title'>Recherche d'images</h1>
      <div className='search-section'>
        <Form onSubmit={handleSearch}>
          <Form.Control
            type='search'
            placeholder='Tapez quelque chose pour rechercher...'
            className='search-input'
            ref={searchInput}
          />
        </Form>
      </div>
    </div>
  );
};

export default App;
```

Ici, nous avons ajouté `<Form onSubmit={handleSearch}>` et à l'intérieur de la méthode `handleSearch`, nous avons utilisé la méthode `event.preventDefault`.

Une fois le formulaire soumis en appuyant sur la touche Entrée dans la boîte de recherche, la page ne se rechargera pas et un texte "soumis" sera affiché dans la console comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/6_submitted.gif)
_Action de soumission du formulaire_

Maintenant, au lieu d'imprimer "soumis", nous pouvons imprimer la valeur entrée par l'utilisateur en utilisant `searchInput.current.value`.

Ici, `searchInput` est la `ref` et `searchInput.current` sera l'entrée réelle de la boîte de recherche. De plus, l'utilisation de `searchInput.current.value` donnera la valeur réelle entrée par l'utilisateur.

Donc, remplacez la méthode `handleSearch` par le code suivant :

```jsx
const handleSearch = (event) => {
  event.preventDefault();
  console.log(searchInput.current.value);
};
```

Et maintenant, vous verrez la valeur entrée affichée dans la console :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/7_searchterm.gif)
_Affichage de la valeur du terme de recherche entré dans la console_

## Comment ajouter des options de recherche rapide

Maintenant, ajoutons des boutons d'action avec une classe `filters` pour une recherche rapide juste en dessous de la div `search-section` :

```jsx
<div className='container'>
      <h1 className='title'>Recherche d'images</h1>
      <div className='search-section'>
        ...
      </div>
      <div className='filters'>
        <div>Nature</div>
        <div>Oiseaux</div>
        <div>Chats</div>
        <div>Chaussures</div>
      </div>
</div>
```

Maintenant, l'application ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/8_buttons_added.png)
_Options de recherche rapide ajoutées_

Lorsque nous cliquons sur l'un des boutons affichés, nous pouvons afficher la valeur du bouton cliqué dans la boîte de recherche d'entrée, afin de pouvoir l'utiliser pour rechercher les images.

Changez la div `filters` en le code ci-dessous :

```jsx
<div className='filters'>
   <div onClick={() => handleSelection('nature')}>Nature</div>
   <div onClick={() => handleSelection('birds')}>Oiseaux</div>
   <div onClick={() => handleSelection('cats')}>Chats</div>
   <div onClick={() => handleSelection('shoes')}>Chaussures</div>
</div>
```

Dans le code ci-dessus, lorsque vous cliquez sur une option, nous transmettons l'option sélectionnée à la méthode `handleSelection`.

Maintenant, ajoutez une nouvelle méthode `handleSelection` à l'intérieur du composant `App` comme montré ci-dessous :

```jsx
const handleSelection = (selection) => {
  searchInput.current.value = selection;
};
```

Votre fichier complet `App.jsx` ressemblera à ceci :

```jsx
import React, { useRef } from 'react';
import { Form } from 'react-bootstrap';
import './index.css';

const App = () => {
  const searchInput = useRef(null);

  const handleSearch = (event) => {
    event.preventDefault();
    console.log(searchInput.current.value);
  };

  const handleSelection = (selection) => {
    searchInput.current.value = selection;
  };

  return (
    <div className='container'>
      <h1 className='title'>Recherche d'images</h1>
      <div className='search-section'>
        <Form onSubmit={handleSearch}>
          <Form.Control
            type='search'
            placeholder='Tapez quelque chose pour rechercher...'
            className='search-input'
            ref={searchInput}
          />
        </Form>
      </div>
      <div className='filters'>
        <div onClick={() => handleSelection('nature')}>Nature</div>
        <div onClick={() => handleSelection('birds')}>Oiseaux</div>
        <div onClick={() => handleSelection('cats')}>Chats</div>
        <div onClick={() => handleSelection('shoes')}>Chaussures</div>
      </div>
    </div>
  );
};

export default App;
```

![Image](https://www.freecodecamp.org/news/content/images/2023/09/9_selection.gif)
_Affichage de l'option de sélection dans la boîte de recherche_

## Comment obtenir l'accès à l'API Unsplash

Maintenant, pour implémenter la recherche d'images, nous devons obtenir la clé API depuis le [site web Unsplash](https://unsplash.com/).

Accédez à [cette URL](https://unsplash.com/developers), et cliquez sur le bouton "S'inscrire en tant que développeur" affiché en haut à droite de la page. Créez votre compte en entrant toutes les informations nécessaires.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/10_register_as_developer.png)

Une fois inscrit, vous serez redirigé vers [cette page](https://unsplash.com/oauth/applications) comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/11_applications_page.png)
_Inscription d'une nouvelle application avec l'API Unsplash_

Cliquez sur le bouton `Nouvelle application`. Sur l'écran suivant :

* Cochez toutes les cases et cliquez sur le bouton `Accepter les termes`
* Entrez les valeurs pour `Nom de l'application` et `Description` et cliquez sur le bouton `Créer une application`

![Image](https://www.freecodecamp.org/news/content/images/2023/09/13_create_application.gif)
_Création d'une nouvelle application avec l'API Unsplash_

Faites défiler un peu vers le bas et copiez la `Clé d'accès` qui est affichée à l'écran :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/14_access_key_copy.gif)
_Obtention de la clé d'accès depuis l'API Unsplash_

Ensuite, créez un nouveau fichier `.env` dans votre projet et ajoutez une nouvelle variable d'environnement avec le nom `VITE_API_KEY`. De plus, attribuez la valeur copiée de la clé API :

```jsx
VITE_API_KEY=A4UiJ5OIwL_4ccbCAE1ZXw3EgoNRotMbdNe12qtKHzM
```

Assurez-vous de commencer le nom de la variable par `VITE_` afin qu'elle soit accessible dans l'application.

La structure de votre dossier d'application ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/15_api_key.png)
_Structure de fichiers avec le fichier .env_

De plus, assurez-vous d'ajouter `.env` dans le fichier `.gitignore` afin que le fichier ne soit pas poussé vers GitHub lorsque les modifications sont poussées vers GitHub.

Maintenant, accédez à la [documentation Unsplash](https://unsplash.com/documentation) et cliquez sur la section `Rechercher des photos par mot-clé`. Et copiez l'URL de base de l'API suivante : `https://api.unsplash.com/search/photos`.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/16_base_api_url.gif)
_Page de documentation de l'API de recherche d'images_

Maintenant, ouvrez le fichier `App.jsx` et collez cette URL copiée en tant que `API_URL` après toutes les instructions d'importation, comme ceci :

```jsx
const API_URL = 'https://api.unsplash.com/search/photos';
```

Selon la documentation, l'API de recherche de photos avec l'URL ci-dessus accepte `query`, `page` et `per_page` en tant que paramètres de requête. Notez simplement cela, car nous allons l'utiliser bientôt.

## Comment faire un appel API à l'API Unsplash

Pour faire un appel API, installons d'abord la bibliothèque npm `axios` en exécutant la commande suivante depuis le dossier du projet :

```js
npm install axios
```

Une fois installé, redémarrez l'application en exécutant la commande `npm run dev`.

Ensuite, déclarez une nouvelle constante juste en dessous de la constante `API_URL` :

```jsx
const IMAGES_PER_PAGE = 20;
```

Ici, nous spécifions d'afficher `20` images par page lorsque nous implémenterons la pagination. Vous pouvez la changer en n'importe quelle valeur que vous souhaitez.

Ajoutez une nouvelle fonction `fetchImages` à l'intérieur du composant `App` comme ceci :

```jsx
const fetchImages = async () => {
  try {
    const { data } = await axios.get(
      `${API_URL}?query=${
        searchInput.current.value
      }&page=1&per_page=${IMAGES_PER_PAGE}&client_id=${
        import.meta.env.VITE_API_KEY
      }`
    );
    console.log('data', data);
  } catch (error) {
    console.log(error);
  }
};
```

Ici, nous avons défini une fonction `fetchImages` qui est déclarée `async` afin que nous puissions utiliser `await` à l'intérieur.

Si vous n'êtes pas familier avec les promesses et async/await, je vous recommande vivement de consulter [cet article](https://www.freecodecamp.org/news/javascript-promises-async-await-and-promise-methods/).

Ensuite, à l'intérieur de la fonction `fetchImages`, nous faisons un appel API GET en utilisant axios à l'URL que nous avons stockée dans la constante `API_URL` : `https://api.unsplash.com/search/photos`.

Pour l'URL de l'API, nous passons les paramètres de requête suivants en utilisant la [syntaxe de littéral de gabarit](https://bit.ly/3rtiQ9y) :

* `query` avec la valeur de l'entrée utilisateur ou la valeur de l'option de recherche rapide
* `page` avec une valeur de `1` pour obtenir les données de la première page
* `per_page` avec la valeur de `20` qui est définie dans la constante `IMAGES_PER_PAGE`
* `client_id` avec la valeur de la clé API du fichier `.env`.

Comme nous utilisons [Vite](https://vitejs.dev/), pour accéder aux variables d'environnement du fichier `.env`, nous devons utiliser `import.meta.env.VITE_API_KEY`.

Ici, `VITE_API_KEY` est la variable d'environnement que nous avons déclarée dans le fichier `.env`.

De plus, importez la bibliothèque `axios` en haut du fichier comme ceci :

```js
import axios from axios;
```

Le fichier `App.jsx` mis à jour ressemblera à ceci :

```jsx
import axios from 'axios';
import React, { useRef } from 'react';
import { Form } from 'react-bootstrap';
import './index.css';

const API_URL = 'https://api.unsplash.com/search/photos';
const IMAGES_PER_PAGE = 20;

const App = () => {
  const searchInput = useRef(null);

  const fetchImages = async () => {
    try {
      const { data } = await axios.get(
        `${API_URL}?query=${
          searchInput.current.value
        }&page=1&per_page=${IMAGES_PER_PAGE}&client_id=${
          import.meta.env.VITE_API_KEY
        }`
      );
      console.log('data', data);
    } catch (error) {
      console.log(error);
    }
  };

  const handleSearch = (event) => {
    event.preventDefault();
    console.log(searchInput.current.value);
  };

  const handleSelection = (selection) => {
    searchInput.current.value = selection;
    fetchImages();
  };

  return (
    <div className='container'>
      <h1 className='title'>Recherche d'images</h1>
      <div className='search-section'>
        <Form onSubmit={handleSearch}>
          <Form.Control
            type='search'
            placeholder='Tapez quelque chose pour rechercher...'
            className='search-input'
            ref={searchInput}
          />
        </Form>
      </div>
      <div className='filters'>
        <div onClick={() => handleSelection('nature')}>Nature</div>
        <div onClick={() => handleSelection('birds')}>Oiseaux</div>
        <div onClick={() => handleSelection('cats')}>Chats</div>
        <div onClick={() => handleSelection('shoes')}>Chaussures</div>
      </div>
    </div>
  );
};

export default App;
```

Si vous vérifiez l'application, vous verrez que, à chaque clic sur l'option de recherche rapide, l'appel API est effectué vers l'API Unsplash, et nous obtenons les données pour l'option sélectionnée.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/17_api_result.gif)
_Faire un appel API lorsque l'option de recherche rapide est cliquée_

Pour faire un appel API lorsque nous entrons le texte de recherche et appuyons sur la touche Entrée, nous devons appeler la fonction `fetchImages` depuis la fonction `handleSearch` également.

Pour ce faire, ajoutez un appel à la fonction `fetchImages` à l'intérieur de la fonction `handleSearch` comme montré ci-dessous :

```jsx
const handleSearch = (event) => {
    event.preventDefault();
    console.log(searchInput.current.value);
    fetchImages();
};
```

Maintenant, vous pourrez voir l'appel API effectué dans l'onglet réseau lorsque nous entrons un texte de recherche et appuyons sur la touche Entrée.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/18_search_result.gif)
_Faire un appel API lorsque le texte est entré dans la boîte de recherche_

## Comment stocker les données de l'API en utilisant l'état

Maintenant, affichons les images provenant de l'API à l'écran.

Pour les afficher à l'écran, nous devons d'abord stocker les données provenant de l'API.

Si vous regardez la structure de la réponse de l'API, vous verrez comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/19_response.png)
_Réponse de l'API_

Donc, déclarez deux états dans le fichier `App.jsx` : un pour stocker les images de réponse qui arrivent dans la propriété `results`, et un autre pour stocker `total_pages` afin que nous puissions implémenter la pagination.

```jsx
const App = () => {
  const searchInput = useRef(null);
  const [images, setImages] = useState([]);
  const [totalPages, setTotalPages] = useState(0);
  ....
}
```

Et mettez à jour la fonction `fetchImages` pour stocker `data.results` en utilisant `setImages` et les pages totales en utilisant la fonction `setTotalPages` :

```jsx
const fetchImages = async () => {
    try {
      const { data } = await axios.get(
        `${API_URL}?query=${
          searchInput.current.value
        }&page=1&per_page=${IMAGES_PER_PAGE}&client_id=${
          import.meta.env.VITE_API_KEY
        }`
      );
      console.log('data', data);
      setImages(data.results);
      setTotalPages(data.total_pages);
    } catch (error) {
      console.log(error);
    }
  };
```

## Comment afficher les images à l'écran

Maintenant, affichons les images que nous avons stockées dans la variable d'état `images`.

Si vous développez la réponse individuelle de l'image de l'API, vous pouvez voir les propriétés `id`, `alt_description`, `urls` que nous pouvons utiliser pour afficher les images individuelles.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/20_api_response.gif)
_Propriétés de la réponse de l'API_

Donc, juste après la div `filters`, ajoutez une autre div pour afficher les images comme ceci :

```jsx
<div className='filters'>
  ...
</div>
<div className='images'>
  {images.map((image) => {
    return (
      <img
        key={image.id}
        src={image.urls.small}
        alt={image.alt_description}
        className='image'
      />
    );
  })}
</div>
```

Ici, nous affichons la version `small` de l'image à partir de la propriété `urls` de l'image individuelle.

Nous pouvons simplifier le code ci-dessus davantage. À l'intérieur de la méthode `map` du tableau, au lieu d'utiliser une accolade avec un mot-clé `return`, nous pouvons le réécrire comme ceci :

```jsx
<div className='filters'>
  ...
</div>
<div className='images'>
{images.map((image) => (
  <img
    key={image.id}
    src={image.urls.small}
    alt={image.alt_description}
    className='image'
  />
))}
</div>
```

Ici, nous retournons implicitement le JSX de la méthode `map` du tableau en ajoutant une parenthèse autour du JSX.

Maintenant, si vous recherchez un texte, vous verrez les images affichées correctement.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/21_displayed_images.gif)
_Images affichées lorsque vous cliquez sur l'icône de recherche rapide_

![Image](https://www.freecodecamp.org/news/content/images/2023/09/22_displayed_images.gif)
_Images affichées lorsque vous cliquez sur l'icône de recherche rapide_

![Image](https://www.freecodecamp.org/news/content/images/2023/09/23_displayed_images.gif)
_Images affichées après avoir entré un terme de recherche_

## Comment implémenter la pagination

Maintenant, nous allons ajouter des boutons précédent et suivant pour voir différents ensembles d'images.

Donc, déclarez d'abord un nouvel état dans le composant `App` comme montré ci-dessous :

```jsx
const [page, setPage] = useState(1);
```

À l'intérieur de la fonction `fetchImages`, changez `page=1` en `page=${page}` afin que lorsque nous changeons la valeur de `page`, les images de la `page` sélectionnée soient chargées.

Ajoutez une nouvelle div avec une classe `buttons` juste en dessous de la div `images` comme montré ci-dessous :

```jsx
<div className='images'>
  ...
</div>
<div className='buttons'>
  {page > 1 && <Button>Précédent</Button>}
  {page < totalPages && <Button>Suivant</Button>}
</div>
```

Dans le code ci-dessus, nous affichons le bouton `Précédent` uniquement si la valeur de `page` est supérieure à `1`, ce qui signifie que pour la première page, nous ne verrons pas le bouton `Précédent`.

Et si la valeur actuelle de `page` est inférieure à `totalPages`, alors nous affichons uniquement le bouton `Suivant`. Cela signifie que pour la dernière page, nous ne verrons pas le bouton `Suivant`.

Si vous vous souvenez, nous avons déjà défini la valeur de `totalPages` à l'intérieur de la fonction `fetchImages` en appelant la fonction `setTotalPages`, et nous l'utilisons ci-dessus pour masquer le bouton `Suivant`.

De plus, n'oubliez pas d'ajouter l'import pour le composant `Button` de `react-bootstrap` à l'intérieur du composant `App` :

```jsx
import { Button } from 'react-bootstrap';
```

Maintenant, lorsque nous cliquons sur le bouton `Précédent`, nous devons `décrémenter` la valeur de la variable d'état `page`. Et lorsque nous cliquons sur le bouton `Suivant`, nous devons `incrémenter` la valeur de la variable d'état `page`.

Donc, ajoutons un gestionnaire `onClick` pour ces deux boutons comme montré ci-dessous :

```jsx
<div className='buttons'>
  {page > 1 && (
    <Button onClick={() => setPage(page - 1)}>Précédent</Button>
  )}
  {page < totalPages && (
    <Button onClick={() => setPage(page + 1)}>Suivant</Button>
  )}
</div>
```

Affichons la valeur de la variable d'état `page`, afin que nous puissions voir la valeur mise à jour.

Après la méthode `handleSelection`, ajoutez console.log comme ceci :

```jsx
console.log('page', page);
```

![Image](https://www.freecodecamp.org/news/content/images/2023/09/24_pagination.gif)
_Affichage de la valeur de la page actuelle dans la console_

Comme vous pouvez le voir ci-dessus, initialement pour la première page, nous ne voyons pas de bouton `Précédent`.

Et lorsque nous cliquons sur le bouton `Suivant`, nous voyons les boutons `Précédent` et `Suivant`, et la valeur de `page` est également incrémentée de `1` comme vous pouvez le voir dans la console.

Donc, à chaque clic sur le bouton `Suivant`, la valeur de `page` est incrémentée de `1`. Et à chaque clic sur le bouton `Précédent`, la valeur de `page` est décrémentée de `1`.

Et lorsque nous revenons à la première page, le bouton `Précédent` est à nouveau masqué, ce qui est attendu.

Comme vous l'avez peut-être remarqué ci-dessus, la valeur de la page change lorsque vous cliquez sur les boutons `Précédent` et `Suivant`, mais un nouvel ensemble d'images n'est pas chargé lorsque vous cliquez sur ces boutons.

C'est parce que nous ne faisons pas à nouveau l'appel API avec une valeur de page mise à jour lorsque la valeur de la page change.

Alors faisons juste cela.

Ajoutez un hook `useEffect` dans le composant `App` comme ceci :

```jsx
useEffect(() => {
  fetchImages();
}, [page]);
```

Maintenant, chaque fois que nous cliquons sur le bouton `Précédent` ou `Suivant`, la valeur de `page` change, donc le hook `useEffect` ci-dessus sera exécuté, où nous appelons la fonction `fetchImages` pour charger le prochain ensemble d'images.

Maintenant, si vous vérifiez l'application, vous verrez les images chargées correctement.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/25_loading_next_images.gif)
_Chargement du prochain ensemble d'images en utilisant la pagination_

Comme vous pouvez le voir ci-dessus, nous chargeons correctement les images lorsque nous cliquons sur le bouton `Précédent` ou `Suivant`.

Mais il y a un petit problème.

Si nous ne sommes pas sur la première ou la dernière page, nous voyons les boutons `Précédent` et `Suivant` et lorsque nous essayons de rechercher un autre terme ou cliquons sur les options de recherche rapide, nous voyons toujours le bouton `Précédent`.

Idéalement, lorsque nous recherchons un autre terme ou cliquons sur une autre option de recherche rapide, nous devrions commencer à partir de la première page, donc seul le bouton `Suivant` devrait être visible. Mais pour l'instant, les boutons `Précédent` et `Suivant` sont tous deux visibles comme vous pouvez le voir ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/26_previous_not_resetting.gif)
_Problème avec les boutons Précédent qui ne se masquent pas lors de la recherche_

Pour corriger ce problème, nous devons réinitialiser la valeur de l'état `page` une fois que nous recherchons un autre terme ou cliquons sur une autre option de recherche rapide.

Donc, à l'intérieur des méthodes `handleSearch` et `handleSelection`, appelez la fonction `setPage` avec une valeur de `1` comme ceci :

```jsx
const handleSearch = (event) => {
  event.preventDefault();
  console.log(searchInput.current.value);
  fetchImages();
  setPage(1);
};

const handleSelection = (selection) => {
  searchInput.current.value = selection;
  fetchImages();
  setPage(1);
};
```

Comme vous pouvez le voir, nous répétons les appels de fonction `fetchImages` et `setPage` dans ces deux méthodes.

Donc, créons une autre fonction avec le nom `resetSearch` et déplaçons les appels de fonction `fetchImages` et `setPage` à l'intérieur. Appelons cette fonction depuis les méthodes `handleSearch` et `handleSelection` comme montré ci-dessous :

```jsx
const resetSearch = () => {
  setPage(1);
  fetchImages();
};

const handleSearch = (event) => {
  event.preventDefault();
  console.log(searchInput.current.value);
  resetSearch();
};

const handleSelection = (selection) => {
  searchInput.current.value = selection;
  resetSearch();
};
```

Maintenant, si vous vérifiez l'application, vous verrez que nous obtenons toujours le résultat correct de la première page affiché lorsque nous cliquons sur l'option de recherche rapide ou entrons un terme de recherche, ce qui est attendu.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/27_correctly_loading_first_page.gif)
_Démonstration du bouton Précédent masqué à chaque recherche_

Votre fichier entier `App.jsx` ressemblera à ceci :

```jsx
import axios from 'axios';
import { useEffect, useRef, useState } from 'react';
import { Button, Form } from 'react-bootstrap';
import './index.css';

const API_URL = 'https://api.unsplash.com/search/photos';
const IMAGES_PER_PAGE = 20;

const App = () => {
  const searchInput = useRef(null);
  const [images, setImages] = useState([]);
  const [page, setPage] = useState(1);
  const [totalPages, setTotalPages] = useState(0);

  useEffect(() => {
    fetchImages();
  }, [page]);

  const fetchImages = async () => {
    try {
      const { data } = await axios.get(
        `${API_URL}?query=${
          searchInput.current.value
        }&page=${page}&per_page=${IMAGES_PER_PAGE}&client_id=${
          import.meta.env.VITE_API_KEY
        }`
      );
      console.log('data', data);
      setImages(data.results);
      setTotalPages(data.total_pages);
    } catch (error) {
      console.log(error);
    }
  };

  const resetSearch = () => {
    setPage(1);
    fetchImages();
  };

  const handleSearch = (event) => {
    event.preventDefault();
    console.log(searchInput.current.value);
    resetSearch();
  };

  const handleSelection = (selection) => {
    searchInput.current.value = selection;
    resetSearch();
  };

  console.log('page', page);

  return (
    <div className='container'>
      <h1 className='title'>Recherche d'images</h1>
      <div className='search-section'>
        <Form onSubmit={handleSearch}>
          <Form.Control
            type='search'
            placeholder='Tapez quelque chose pour rechercher...'
            className='search-input'
            ref={searchInput}
          />
        </Form>
      </div>
      <div className='filters'>
        <div onClick={() => handleSelection('nature')}>Nature</div>
        <div onClick={() => handleSelection('birds')}>Oiseaux</div>
        <div onClick={() => handleSelection('cats')}>Chats</div>
        <div onClick={() => handleSelection('shoes')}>Chaussures</div>
      </div>
      <div className='images'>
        {images.map((image) => (
          <img
            key={image.id}
            src={image.urls.small}
            alt={image.alt_description}
            className='image'
          />
        ))}
      </div>
      <div className='buttons'>
        {page > 1 && (
          <Button onClick={() => setPage(page - 1)}>Précédent</Button>
        )}
        {page < totalPages && (
          <Button onClick={() => setPage(page + 1)}>Suivant</Button>
        )}
      </div>
    </div>
  );
};

export default App;
```

## Comment trouver des bugs en utilisant ESLint

Lorsque vous travaillez sur une application React, vous devez toujours avoir l'extension ESLint VS Code activée.

Cela garantira que votre code est correct et qu'il ne produira pas de résultats inattendus à l'avenir.

En fonction de la configuration ESLint définie dans le fichier `.eslientrc`, vous obtiendrez des suggestions utiles pour améliorer votre code.

Donc, ouvrez votre panneau d'extensions VS Code et installez l'[extension ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint) comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/28_eslint_extension.png)
_Extension VS Code ESLint_

Après avoir installé l'extension, si vous vérifiez le fichier `App.jsx`, vous verrez immédiatement une ligne ondulée jaune pour la dépendance `page` du hook `useEffect`. Si vous survolez avec la souris, vous verrez l'avertissement comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/29_missing_dependency.png)
_Avertissement ESLint pour le hook useEffect_

Comme l'avertissement l'indique, nous devons ajouter une dépendance `fetchImages` dans le tableau des dépendances.

Nous recevons un avertissement parce que, dans le composant fonctionnel, à chaque réaffichage du composant, toutes les fonctions déclarées sont recréées, donc leur référence change.

Donc, si nous utilisons une variable ou une fonction externe à l'intérieur du hook `useEffect`, nous devons la mentionner dans les dépendances, afin que chaque fois que la dépendance change, le `useEffect` sera exécuté à nouveau.

Pour corriger cela, vous pouvez cliquer sur le lien de correction rapide et sélectionner l'option "mettre à jour les dépendances" comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/30_updating_dependency.gif)
_Mise à jour de la dépendance du hook useEffect_

Toutes les dépendances manquantes seront automatiquement ajoutées dans le tableau des dépendances.

Vous pouvez également choisir d'ajouter manuellement la dépendance si vous le souhaitez.

Cependant, avec ce changement, vous verrez un nouvel avertissement jaune pour la fonction `fetchImages` comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/31_fetchimages_warning.png)
_Avertissement ESLint pour useCallback_

Comme je l'ai dit précédemment, à chaque réaffichage du composant, la fonction `fetchImages` sera recréée et lorsqu'elle change, nous rappelons à nouveau la fonction `fetchImages` car elle est ajoutée dans la dépendance.

Pour éviter cela, nous devons envelopper la fonction `fetchImages` à l'intérieur du hook [useCallback](https://react.dev/reference/react/useCallback) comme montré ci-dessous :

```jsx
const fetchImages = useCallback(async () => {
  try {
    const { data } = await axios.get(
      `${API_URL}?query=${
        searchInput.current.value
      }&page=${page}&per_page=${IMAGES_PER_PAGE}&client_id=${
        import.meta.env.VITE_API_KEY
      }`
    );
    console.log('data', data);
    setImages(data.results);
    setTotalPages(data.total_pages);
  } catch (error) {
    console.log(error);
  }
}, [page]);
```

Dans le code ci-dessus, nous passons `page` en tant que dépendance car `page` est une variable externe dont la valeur pourrait changer à l'avenir lorsque nous cliquons sur les boutons `Précédent` ou `Suivant` ou recherchons un nouveau terme.

Si des variables changeantes sont utilisées à l'intérieur des hooks `useEffect` ou `useCallback` ou `useMemo`, nous devons les ajouter dans la liste des dépendances.

Maintenant, vous ne verrez plus d'avertissements dans le composant `App`.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/32_no_warnings.gif)
_Avertissement ESLint de useCallback corrigé_

Cependant, si vous vérifiez la console du navigateur, vous verrez une erreur et rien n'est affiché sur l'interface utilisateur car l'application a planté.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/33_access_before_initialization.png)
_Erreur de la console liée à l'expression de fonction_

Nous obtenons des erreurs car nous avons déclaré la fonction `fetchImages` en utilisant la syntaxe d'expression de fonction, et les fonctions déclarées en utilisant la syntaxe d'expression de fonction ne peuvent pas être appelées avant de les définir.

Attribuer une fonction à une variable en fait une expression de fonction.

Comme vous pouvez le voir dans l'image ci-dessous, nous appelons la fonction `fetchImages` à la ligne numéro 16 et nous déclarons la fonction à la ligne numéro 19 et les fonctions déclarées en utilisant la syntaxe d'expression de fonction ne peuvent pas être accessibles avant la déclaration.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/34_function_expression_error.png)
_Cause de l'erreur de la console_

Pour corriger cela, nous devons déclarer la fonction avant de l'appeler. Donc, déplacez la fonction `fetchImages` avant le hook useEffect et cela corrigera le problème.

Votre composant `App` ressemblera à ceci :

```jsx

const App = () => {
  const searchInput = useRef(null);
  const [images, setImages] = useState([]);
  const [page, setPage] = useState(1);
  const [totalPages, setTotalPages] = useState(0);

  const fetchImages = useCallback(async () => {
    try {
      const { data } = await axios.get(
        `${API_URL}?query=${
          searchInput.current.value
        }&page=${page}&per_page=${IMAGES_PER_PAGE}&client_id=${
          import.meta.env.VITE_API_KEY
        }`
      );
      console.log('data', data);
      setImages(data.results);
      setTotalPages(data.total_pages);
    } catch (error) {
      console.log(error);
    }
  }, [page]);

  useEffect(() => {
    fetchImages();
  }, [fetchImages, page]);

  const resetSearch = () => {
    setPage(1);
    fetchImages();
  };
  ...
}
```

Maintenant, si vous vérifiez l'application, il n'y aura pas d'erreur et l'application fonctionnera comme prévu.

## Améliorations du code

Actuellement, nous n'avons ajouté aucune validation dans l'application actuelle lorsque l'utilisateur entre un terme de recherche.

Lorsque la page est chargée, et lorsque nous n'entrons aucun texte et appuyons directement sur la touche Entrée dans la boîte de recherche d'entrée, nous faisons un appel API ce qui n'est pas bon.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/35_extra_api_call.gif)
_Démonstration des appels API effectués sans aucune valeur_

Pour corriger cela, avant de faire l'appel API, nous devons d'abord vérifier si `searchInput.current.value` n'est pas vide et ensuite seulement faire l'appel API.

Changez la fonction `fetchImages` de ce code :

```jsx
const fetchImages = useCallback(async () => {
  try {
    const { data } = await axios.get(
      `${API_URL}?query=${
        searchInput.current.value
      }&page=${page}&per_page=${IMAGES_PER_PAGE}&client_id=${
        import.meta.env.VITE_API_KEY
      }`
    );
    console.log('data', data);
    setImages(data.results);
    setTotalPages(data.total_pages);
  } catch (error) {
    console.log(error);
  }
}, [page]);
```

en le code ci-dessous :

```jsx
const fetchImages = useCallback(async () => {
  try {
    if (searchInput.current.value) {
      const { data } = await axios.get(
        `${API_URL}?query=${
          searchInput.current.value
        }&page=${page}&per_page=${IMAGES_PER_PAGE}&client_id=${
          import.meta.env.VITE_API_KEY
        }`
      );
      console.log('data', data);
      setImages(data.results);
      setTotalPages(data.total_pages);
    }
  } catch (error) {
    console.log(error);
  }
}, [page]);
```

![Image](https://www.freecodecamp.org/news/content/images/2023/09/36_no_api_calls.gif)
_Problème corrigé des appels API sans aucune valeur_

Comme vous pouvez le voir ci-dessus, initialement au chargement de la page et sans entrer de valeur, si nous appuyons sur la touche Entrée, aucun appel API n'est effectué.

Seulement lorsque nous tapons quelque chose et appuyons sur Entrée, l'appel API est effectué, ce qui est une bonne amélioration pour l'application.

## Comment supprimer une dépendance supplémentaire de `useEffect`

Comme nous avons ajouté un hook `useCallback` pour la fonction `fetchImages` qui a une dépendance `page`, nous n'avons plus besoin de la dépendance supplémentaire `page` pour le hook `useEffect`.

Donc, changez le code ci-dessous :

```jsx
useEffect(() => {
  fetchImages();
}, [fetchImages, page]);
```

en ce code :

```jsx
useEffect(() => {
  fetchImages();
}, [fetchImages]);
```

et l'application fonctionnera comme avant sans aucun problème.

## Comment afficher une indication de chargement

Comme vous l'avez peut-être remarqué dans l'image précédente, lorsque nous avons recherché le texte `bonjour`, les résultats n'ont pas été affichés immédiatement.

Comme nous faisons un appel API lorsque nous recherchons quelque chose, en fonction de la vitesse du réseau, cela peut prendre un certain temps pour obtenir les données de l'API.

Donc, pendant que l'appel API est encore en cours, nous pouvons afficher un message de chargement, et une fois que nous obtenons la réponse de l'API, nous afficherons les images.

Pour y parvenir, déclarez un nouvel état de chargement dans le composant `App` avec une valeur initiale de `false` :

```jsx
const [loading, setLoading] = useState(false);
```

Et maintenant, changez la fonction `fetchImages` en le code ci-dessous :

```jsx
const fetchImages = useCallback(async () => {
  try {
    if (searchInput.current.value) {
      setErrorMsg('');
      setLoading(true);
      const { data } = await axios.get(
        `${API_URL}?query=${
          searchInput.current.value
        }&page=${page}&per_page=${IMAGES_PER_PAGE}&client_id=${
          import.meta.env.VITE_API_KEY
        }`
      );
      setImages(data.results);
      setTotalPages(data.total_pages);
      setLoading(false);
    }
  } catch (error) {
    setErrorMsg('Erreur lors de la récupération des images. Réessayez plus tard.');
    console.log(error);
    setLoading(false);
  }
}, [page]);
```

Comme vous pouvez le voir ci-dessus, nous appelons `setLoading(true)` avant l'appel API et `setLoading(false)` après l'appel API.

Notez que nous appelons également `setLoading(false)` à l'intérieur du bloc catch.

Donc, même si l'API réussit ou échoue, nous définissons l'état `loading` sur `false` afin que nous ne voyions pas le message de chargement tout le temps.

Maintenant, pour afficher le message de chargement, changez le code ci-dessous :

```jsx
<div className='images'>
  {images.map((image) => (
    <img
      key={image.id}
      src={image.urls.small}
      alt={image.alt_description}
      className='image'
    />
  ))}
</div>
<div className='buttons'>
  {page > 1 && (
    <Button onClick={() => setPage(page - 1)}>Précédent</Button>
  )}
  {page < totalPages && (
    <Button onClick={() => setPage(page + 1)}>Suivant</Button>
  )}
</div>
```

en ce code :

```jsx
{loading ? (
  <p className='loading'>Chargement...</p>
) : (
  <>
    <div className='images'>
      {images.map((image) => (
        <img
          key={image.id}
          src={image.urls.small}
          alt={image.alt_description}
          className='image'
        />
      ))}
    </div>
    <div className='buttons'>
      {page > 1 && (
        <Button onClick={() => setPage(page - 1)}>Précédent</Button>
      )}
      {page < totalPages && (
        <Button onClick={() => setPage(page + 1)}>Suivant</Button>
      )}
    </div>
  </>
)}
```

Dans le code ci-dessus, si le chargement est vrai, alors nous affichons un message de chargement. Sinon, nous affichons les images provenant de l'API.

Si vous vérifiez l'application, vous verrez que l'indication de chargement s'affiche correctement.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/37_loading_indication.gif)
_Démonstration de l'indication de chargement_

## **Merci d'avoir lu**

C'est tout pour ce tutoriel. J'espère que vous avez appris beaucoup de choses.

Vous pouvez trouver le code source complet de cette application dans [ce dépôt](https://github.com/myogeshchavan97/unsplash_image_search).

Vous voulez regarder la version vidéo de ce tutoriel ? Vous pouvez consulter [cette vidéo](https://www.youtube.com/watch?v=0YoT44j3Jg4&list=PLSJnlFr3D-mFm7-cdhnHdBvUdxUp-a9HL&index=17).

Si vous voulez maîtriser JavaScript, ES6+, React et Node.js avec un contenu facile à comprendre, consultez ma [chaîne YouTube](https://www.youtube.com/@codingmastery_dev/). N'oubliez pas de vous abonner.

Vous voulez rester à jour avec un contenu régulier sur JavaScript, React et Node.js ? [Suivez-moi sur LinkedIn](https://www.linkedin.com/in/yogesh-chavan97/).