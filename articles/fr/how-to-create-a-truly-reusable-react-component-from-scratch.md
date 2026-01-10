---
title: Comment créer un composant React vraiment réutilisable à partir de zéro
subtitle: ''
author: Yogesh Chavan
co_authors: []
series: null
date: '2021-08-20T17:54:40.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-truly-reusable-react-component-from-scratch
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/pexels-sarah-chai-7262760.jpg
tags:
- name: components
  slug: components
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
- name: Web Development
  slug: web-development
seo_title: Comment créer un composant React vraiment réutilisable à partir de zéro
seo_desc: 'In this tutorial, you will build an app with React. And you will learn
  how to create a truly reusable auto-suggestion component from scratch.

  This application will allow a user to search for a country in a list of countries.
  It will display matching ...'
---

Dans ce tutoriel, vous allez créer une application avec React. Et vous allez apprendre à créer un composant d'auto-suggestion vraiment réutilisable à partir de zéro.

Cette application permettra à un utilisateur de rechercher un pays dans une liste de pays. Elle affichera les suggestions correspondantes sous le champ de saisie pour le pays que l'utilisateur a entré.

En construisant cette application, vous apprendrez :

* Comment créer un composant réutilisable
* Comment utiliser le hook `useRef` pour gérer les auto-suggestions
* Comment créer un hook réutilisable personnalisé
* Comment effectuer la recherche efficacement

et bien plus encore.

Vous pouvez trouver la démonstration en direct de l'application finale [ici](https://react-autosuggestion-app.netlify.app/).

Ci-dessous se trouve la démonstration fonctionnelle de la fonctionnalité d'auto-suggestion.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/suggestion_demo.gif)

Alors, commençons à construire l'application.

## Installation du projet

Nous allons utiliser create-react-app pour initialiser le projet.

Nous utiliserons la syntaxe des React Hooks pour créer les composants. Donc, si vous n'êtes pas familier avec cela, consultez mon [article sur les hooks ici](https://levelup.gitconnected.com/an-introduction-to-react-hooks-50281fd961fe?source=friends_link&sk=89baff89ec8bc637e7c13b7554904e54).

Créez un nouveau projet React en exécutant la commande suivante :

```js
npx create-react-app react-autosuggestion-app
```

Une fois que vous avez créé le projet, supprimez tous les fichiers du dossier `src` et créez les fichiers `index.js`, `App.js`, `styles.css` à l'intérieur du dossier `src`.

Créez également les dossiers `components` et `custom-hooks` à l'intérieur du dossier `src`.

Installez les dépendances requises en exécutant la commande suivante à partir du terminal ou de l'invite de commande :

```js
yarn add axios@0.21.1 lodash@4.17.21 react-bootstrap@1.6.1 bootstrap@5.1.0
```

Une fois celles-ci installées, ouvrez le fichier `src/styles.css` et ajoutez le contenu de [ce fichier](https://github.com/myogeshchavan97/react-autosuggestion-app/blob/master/src/styles.css) à l'intérieur.

## Comment construire les pages initiales

Créez un nouveau fichier `countries.json` à l'intérieur du dossier `public` et ajoutez le contenu de [ce fichier](https://github.com/myogeshchavan97/react-autosuggestion-app/blob/master/public/countries.json) à l'intérieur.

Créez un fichier `AutoComplete.js` à l'intérieur du dossier `components` avec le code suivant :

```js
import React from 'react';

function AutoComplete({ isVisible, suggestions, handleSuggestionClick }) {
  return (
    <div className={`${isVisible ? 'show suggestion-box' : 'suggestion-box'}`}>
      <ul>
        {suggestions.map((country, index) => (
          <li key={index} onClick={() => handleSuggestionClick(country)}>
            {country}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default AutoComplete;
```

Dans ce fichier, nous affichons les suggestions à l'utilisateur une fois que l'utilisateur tape quelque chose dans la zone de texte.

Créez un fichier `useOutsideClick.js` à l'intérieur du dossier `custom-hooks` avec le code suivant :

```js
import { useState, useRef, useEffect } from 'react';

const useOutsideClick = () => {
  const [isVisible, setIsVisible] = useState(false);
  const ref = useRef();

  const handleOutsideClick = () => {
    if (ref.current) {
      setIsVisible(false);
    }
  };

  useEffect(() => {
    document.addEventListener('click', handleOutsideClick);
    return () => {
      document.removeEventListener('click', handleOutsideClick);
    };
  }, []);

  return [ref, isVisible, setIsVisible];
};

export default useOutsideClick;
```

Ici, nous avons créé un hook personnalisé qui affichera/masquera la boîte de suggestions.

Initialement, nous avons déclaré un état pour masquer la boîte de suggestions en définissant la valeur sur `false` :

```js
const [isVisible, setIsVisible] = useState(false);
```

Ensuite, nous avons déclaré une référence :

```js
const ref = useRef();
```

Nous retournons cette `ref` de notre hook personnalisé avec `isVisible` et `setIsVisible` comme ceci :

```js
return [ref, isVisible, setIsVisible];
```

Ainsi, à l'intérieur du composant où nous utilisons le hook `useOutsideClick`, nous pouvons utiliser cette référence pour l'assigner à la boîte de suggestions. Donc, s'il y a plusieurs champs de saisie, chaque champ de saisie aura sa propre boîte de suggestions et la fonctionnalité de masquage et d'affichage.

À l'intérieur de la fonction `handleOutsideClick`, nous avons le code suivant :

```js
const handleOutsideClick = () => {
  if (ref.current) {
    setIsVisible(false);
  }
};
```

Ici, nous vérifions `ref.current` car nous voulons appeler la fonction `setIsVisible` uniquement si la référence pour la boîte de suggestions est disponible et non chaque fois que nous cliquons sur la page.

Ensuite, nous avons ajouté des gestionnaires d'événements pour appeler la fonction `handleOutsideClick` :

```js
useEffect(() => {
  document.addEventListener('click', handleOutsideClick);
  return () => {
    document.removeEventListener('click', handleOutsideClick);
  };
}, []);
```

Nous supprimons également le gestionnaire d'événements en retournant une fonction du hook `useEffect` une fois que le composant est démonté.

## Comment créer un composant React réutilisable

Maintenant, créez un fichier `InputControl.js` à l'intérieur du dossier `components` avec le code suivant :

```js
/* eslint-disable react-hooks/exhaustive-deps */
import React, { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import _ from 'lodash';
import { Form } from 'react-bootstrap';
import AutoComplete from './AutoComplete';
import useOutsideClick from '../custom-hooks/useOutsideClick';

const InputControl = ({ name, label, placeholder }) => {
  const [documentRef, isVisible, setIsVisible] = useOutsideClick();
  const [suggestions, setSuggestions] = useState([]);
  const [selectedCountry, setSelectedCountry] = useState('');
  const [searchTerm, setSearchTerm] = useState('');
  const [errorMsg, setErrorMsg] = useState('');
  const ref = useRef();

  useEffect(() => {
    ref.current = _.debounce(processRequest, 300);
  }, []);

  function processRequest(searchValue) {
    axios
      .get('/countries.json')
      .then((response) => {
        const countries = response.data;
        const result = countries.filter((country) =>
          country.toLowerCase().includes(searchValue.toLowerCase())
        );
        setSuggestions(result);
        if (result.length > 0) {
          setIsVisible(true);
        } else {
          setIsVisible(false);
        }
        setErrorMsg('');
      })
      .catch(() => setErrorMsg('Something went wrong. Try again later'));
  }

  function handleSearch(event) {
    event.preventDefault();
    const { value } = event.target;
    setSearchTerm(value);
    ref.current(value);
  }

  function handleSuggestionClick(countryValue) {
    setSelectedCountry(countryValue);
    setIsVisible(false);
  }

  return (
    <Form.Group controlId="searchTerm">
      <Form.Label>{label}</Form.Label>
      <Form.Control
        className="input-control"
        type="text"
        value={searchTerm}
        name={name}
        onChange={handleSearch}
        autoComplete="off"
        placeholder={placeholder}
      />
      <div ref={documentRef}>
        {isVisible && (
          <AutoComplete
            isVisible={isVisible}
            suggestions={suggestions}
            handleSuggestionClick={handleSuggestionClick}
          />
        )}
      </div>
      {selectedCountry && (
        <div className="selected-country">
          Votre pays sélectionné : {selectedCountry}
        </div>
      )}
      {errorMsg && <p className="errorMsg">{errorMsg}</p>}
    </Form.Group>
  );
};

export default InputControl;
```

Dans ce fichier, nous avons créé un composant réutilisable avec une recherche et des suggestions disponibles dans le composant.

Initialement, nous référençons le hook `useOutsideClick` :

```js
const [documentRef, isVisible, setIsVisible] = useOutsideClick();
```

Nous stockons la référence retournée par le hook dans la variable `documentRef`.
Chaque fois qu'un utilisateur tape quelque chose dans la zone de texte, nous effectuons un appel API pour obtenir une liste de pays correspondant aux critères de recherche.

Mais pour éviter les appels API inutiles à chaque caractère saisi dans la zone de texte, nous utiliserons la méthode debounce de la bibliothèque [lodash](https://lodash.com/). Elle nous permet d'appeler l'API uniquement après 300 millisecondes une fois que l'utilisateur a arrêté de taper en utilisant le code suivant :

```js
ref.current = _.debounce(processRequest, 300);
```

L'appel de la fonction `_.debounce` retourne une fonction que nous avons stockée dans la variable `ref.current`. Nous appellerons la fonction stockée là une fois que 300 millisecondes se sont écoulées.

Nous utilisons ref au lieu d'une variable normale car nous avons besoin que cette initialisation se produise une seule fois lorsque le composant est monté. La valeur de la variable normale sera perdue à chaque nouveau rendu du composant lorsque certains états ou props changent.

Nous appelons la fonction stockée dans `ref.current` à partir de la fonction `handleSearch` en passant la valeur saisie par l'utilisateur.

Ainsi, une fois que nous appelons la fonction stockée dans `ref.current`, la fonction `processRequest` sera appelée en arrière-plan.

La fonction `processRequest` recevra automatiquement la valeur passée à la fonction `ref.current`.

À l'intérieur de la fonction `processRequest`, nous effectuons un appel API pour obtenir la liste des pays.

```js
function processRequest(searchValue) {
  axios
    .get('/countries.json')
    .then((response) => {
      const countries = response.data;
      const result = countries.filter((country) =>
        country.toLowerCase().includes(searchValue.toLowerCase())
      );
      setSuggestions(result);
      if (result.length > 0) {
        setIsVisible(true);
      } else {
        setIsVisible(false);
      }
      setErrorMsg('');
    })
    .catch(() => setErrorMsg('Something went wrong. Try again later'));
}
```

Ici, une fois que nous avons la réponse de l'API, nous utilisons la méthode de filtrage de tableau pour filtrer uniquement les pays qui correspondent au terme de recherche fourni.

Ensuite, nous définissons la liste des pays dans l'état des suggestions en utilisant `setSuggestions(result)`.

Ensuite, nous vérifions la longueur du tableau de résultats pour afficher ou masquer la boîte de suggestions.

Si vous vérifiez le JSX qui est retourné par le composant, il ressemble à ceci :

```js
return (
  <Form.Group controlId="searchTerm">
    <Form.Label>{label}</Form.Label>
    <Form.Control
      className="input-control"
      type="text"
      value={searchTerm}
      name={name}
      onChange={handleSearch}
      autoComplete="off"
      placeholder={placeholder}
    />
    <div ref={documentRef}>
      {isVisible && (
        <AutoComplete
          isVisible={isVisible}
          suggestions={suggestions}
          handleSuggestionClick={handleSuggestionClick}
        />
      )}
    </div>
    {selectedCountry && (
      <div className="selected-country">
        Votre pays sélectionné : {selectedCountry}
      </div>
    )}
    {errorMsg && <p className="errorMsg">{errorMsg}</p>}
  </Form.Group>
);
```

Ici, pour la zone de texte de saisie, nous avons ajouté un gestionnaire `handleSearch` onChange qui ressemble à ceci :

```js
function handleSearch(event) {
  event.preventDefault();
  const { value } = event.target;
  setSearchTerm(value);
  ref.current(value);
}
```

Nous mettons à jour l'état `searchTerm` avec la valeur tapée par l'utilisateur. Ensuite, nous appelons la fonction stockée dans `ref.current` en lui passant la valeur que l'utilisateur entre.

L'appel de `ref.current` appelle en interne la fonction `processRequest` où nous appelons réellement l'API.

Ensuite, après la zone de texte de saisie, nous avons ajouté une div avec la référence pour afficher les suggestions :

```js
<div ref={documentRef}>
  {isVisible && (
    <AutoComplete
      isVisible={isVisible}
      suggestions={suggestions}
      handleSuggestionClick={handleSuggestionClick}
    />
  )}
</div>
```

Nous affichons les suggestions uniquement si `isVisible` est vrai, ce qui se produit lorsque nous obtenons des résultats de l'API à l'intérieur de la fonction `processRequest`.

Ici, nous passons les suggestions à afficher dans le composant `AutoComplete`.
Une fois que nous cliquons sur l'une des suggestions, la fonction `handleSuggestionClick` s'exécute, ce qui met à jour le `selectedCountry` et masque les suggestions :

```js
function handleSuggestionClick(countryValue) {
  setSelectedCountry(countryValue);
  setIsVisible(false);
}
```

## Comment utiliser le composant réutilisable

Maintenant, ouvrez le fichier `App.js` et ajoutez le code suivant à l'intérieur :

```js
import React from 'react';
import { Form } from 'react-bootstrap';
import InputControl from './components/InputControl';

const App = () => {
  return (
    <div className="main">
      <h1>Démonstration de l'auto-suggestion React</h1>
      <div className="search-form">
        <Form>
          <InputControl
            name="country"
            label="Entrez le pays"
            placeholder="Tapez un nom de pays"
          />
        </Form>
      </div>
    </div>
  );
};

export default App;
```

Maintenant, démarrez l'application en exécutant la commande suivante à partir du terminal ou de l'invite de commande :

```js
yarn start
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/2.gif)

Comme vous pouvez le voir, une fois que vous sélectionnez une valeur dans la suggestion, la valeur sélectionnée s'affiche sous la zone de texte.

**Note :** nous avons créé un composant `InputControl` séparé qui affiche le champ de saisie avec sa boîte de suggestions.

Ainsi, nous pouvons réutiliser le même composant `InputControl` pour afficher des suggestions dans une autre zone de texte comme montré ci-dessous :

```js
import React from 'react';
import { Form } from 'react-bootstrap';
import InputControl from './components/InputControl';

const App = () => {
  return (
    <div className="main">
      <h1>Démonstration de l'auto-suggestion React</h1>
      <div className="search-form">
        <Form>
          <InputControl
            name="country"
            label="Entrez le pays"
            placeholder="Tapez un nom de pays"
          />
          <InputControl
            name="country"
            label="Entrez le pays"
            placeholder="Tapez un nom de pays"
          />
        </Form>
      </div>
    </div>
  );
};

export default App;
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/3.gif)

Comme vous pouvez le voir, nous avons ajouté un autre composant `InputControl` pour le pays, donc nous sommes en mesure de gérer les suggestions pour chaque zone de texte séparément.

Ainsi, si vous souhaitez afficher différentes suggestions pour une autre zone de texte, vous pouvez simplement passer une prop supplémentaire au composant `InputControl` et, en fonction de cette prop, afficher différents résultats dans la boîte de suggestions.

## Conclusion

Comme nous l'avons vu dans ce tutoriel, en créant un composant `InputControl` réutilisable et en utilisant `ref` pour gérer les suggestions de chaque zone de texte séparément, nous sommes en mesure de créer un composant vraiment réutilisable pour afficher des suggestions d'auto-complétion.

**Vous pouvez trouver le code source complet de ce tutoriel dans [ce dépôt](https://github.com/myogeshchavan97/react-autosuggestion-app) et la démonstration en direct [ici](https://react-autosuggestion-app.netlify.app/).**

## **Merci d'avoir lu !**

Si vous souhaitez apprendre Redux en détail à partir de zéro et construire 3 applications ainsi que l'application complète de commande de nourriture, consultez le cours [Mastering Redux](https://master-redux.yogeshchavan.dev/).

Dans le cours, vous apprendrez :

* Les bases et les concepts avancés de Redux
* Comment gérer l'état complexe des tableaux et des objets
* Comment utiliser plusieurs réducteurs pour gérer l'état complexe de Redux
* Comment déboguer une application Redux
* Comment utiliser Redux dans React en utilisant la bibliothèque react-redux pour rendre votre application réactive.
* Comment utiliser la bibliothèque redux-thunk pour gérer les appels API asynchrones
* Construire 3 applications différentes en utilisant Redux

et bien plus encore.

Enfin, nous construirons une application complète de commande de nourriture à partir de zéro avec l'intégration de Stripe pour accepter les paiements et la déployer en production.

Vous souhaitez rester à jour avec du contenu régulier concernant JavaScript, React, Node.js ? [Suivez-moi sur LinkedIn](https://www.linkedin.com/in/yogesh-chavan97/).