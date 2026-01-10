---
title: Comment créer une application d'inscription multi-étapes avec des transitions
  animées en utilisant la stack MERN
subtitle: ''
author: Yogesh Chavan
co_authors: []
series: null
date: '2021-03-09T22:24:05.000Z'
originalURL: https://freecodecamp.org/news/build-a-multi-step-registration-app-with-animated-transitions-using-mern-stack
coverImage: https://cdn-media-2.freecodecamp.org/w1280/6044ae70a7946308b76836e2.jpg
tags:
- name: app development
  slug: app-development
- name: Express
  slug: express
- name: full stack
  slug: full-stack
- name: JavaScript
  slug: javascript
- name: MongoDB
  slug: mongodb
- name: node
  slug: node
- name: React
  slug: react
seo_title: Comment créer une application d'inscription multi-étapes avec des transitions
  animées en utilisant la stack MERN
seo_desc: 'In this article, we will build an amazing Multi Step Registration form
  with smooth animated transitions using the MERN stack (MongoDB, Express, React,
  and Node.js).

  By building this App, you will learn a lot of concepts in React and Node.js including...'
---

Dans cet article, nous allons créer un formulaire d'inscription multi-étapes incroyable avec des transitions animées fluides en utilisant la stack MERN (MongoDB, Express, React et Node.js).

En construisant cette application, vous apprendrez de nombreux concepts dans React et Node.js, notamment :

* Comment gérer les données de plusieurs formulaires avec validation pour chaque champ
* Comment conserver les valeurs des données de formulaires entre les routes
* Comment mettre à jour les indications de progression pour chaque étape d'inscription
* Comment charger les états et villes spécifiques à un pays depuis l'API
* Comment créer des animations de glissement fluides en utilisant la bibliothèque très populaire framer-motion
* Comment créer des API Rest en utilisant Express.js
* Comment implémenter la fonctionnalité de connexion et d'inscription avec MongoDB
* Comment stocker et valider les mots de passe stockés sous forme cryptée dans MongoDB

Et bien plus encore.

Nous utiliserons la syntaxe des React Hooks pour construire cette application dans React. Donc, si vous êtes nouveau dans les React Hooks, consultez mon article [Introduction aux React Hooks](https://levelup.gitconnected.com/an-introduction-to-react-hooks-50281fd961fe?source=friends_link&sk=89baff89ec8bc637e7c13b7554904e54) pour apprendre les bases des Hooks.

Nous utiliserons également une base de données MongoDB pour stocker les données des utilisateurs inscrits, alors assurez-vous d'installer MongoDB localement en suivant les instructions de [cet article](https://levelup.gitconnected.com/how-to-install-mongodb-database-on-local-environment-19a8a76f1b92?source=friends_link&sk=416b443bad1f86b292e4b72602cf5c9b).

Très bien, commençons.

## Installation initiale du projet

Créez un nouveau projet en utilisant `create-react-app` :

```javascript
npx create-react-app multi-step-form-using-mern

```

Une fois que vous avez créé le projet, supprimez tous les fichiers du dossier `src` et créez un fichier `index.js` et un fichier `styles.scss` à l'intérieur du dossier `src`. Créez également des dossiers `components`, `router` et `utils` à l'intérieur du dossier `src`.

Installez les dépendances nécessaires comme ceci :

```javascript
yarn add axios@0.21.1 bootstrap@4.6.0 react-bootstrap@1.5.0 country-state-city@2.0.0 framer-motion@3.7.0 node-sass@4.14.1 react-hook-form@6.15.4 react-router-dom@5.2.0 sweetalert2@10.15.5

```

Ouvrez votre fichier `styles.scss` et ajoutez le contenu depuis [ici](https://github.com/myogeshchavan97/multi-step-form-using-mern/blob/master/src/styles.scss) à l'intérieur.

Nous utiliserons la syntaxe SCSS pour écrire du CSS. Donc, si vous êtes nouveau dans SCSS, consultez [mon article ici](https://medium.com/better-programming/an-introduction-to-sass-scss-fdbda159b40?source=friends_link&sk=c0846e19ddb4f53919a6abaf29032d10) pour une introduction à celui-ci.

## Comment créer les pages initiales

Créez un nouveau fichier `Header.js` à l'intérieur du dossier `components` avec le contenu suivant :

```jsx
import React from 'react';

const Header = () => (
  <div>
    <h1>Inscription Multi-Étapes</h1>
  </div>
);

export default Header;

```

Créez un nouveau fichier `FirstStep.js` à l'intérieur du dossier `components` avec le contenu suivant :

```jsx
import React from 'react';

const FirstStep = () => {
  return (
    <div>
      Formulaire Première Étape
    </div>
  )
};

export default FirstStep;

```

Créez un nouveau fichier `AppRouter.js` à l'intérieur du dossier `router` avec le contenu suivant :

```jsx
import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import FirstStep from '../components/FirstStep';
import Header from '../components/Header';

const AppRouter = () => (
  <BrowserRouter>
    <div className="container">
      <Header />
      <Switch>
        <Route component={FirstStep} path="/" exact={true} />
      </Switch>
    </div>
  </BrowserRouter>
);

export default AppRouter;

```

Dans ce fichier, initialement, nous avons ajouté une seule route pour la première étape.

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

Démarrez l'application en exécutant la commande `yarn start` et vous verrez l'écran suivant :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/multi_initial_screen.png)

## Comment ajouter des étapes de progression dans l'en-tête

Créez un nouveau fichier appelé `Progress.js` à l'intérieur du dossier `components` avec le contenu suivant :

```jsx
import React from 'react';

const Progress = () => {
  return (
    <React.Fragment>
      <div className="steps">
        <div className="step">
          <div>1</div>
          <div>Étape 1</div>
        </div>
        <div className="step">
          <div>2</div>
          <div>Étape 2</div>
        </div>
        <div className="step">
          <div>3</div>
          <div>Étape 3</div>
        </div>
      </div>
    </React.Fragment>
  );
};

export default Progress;

```

et utilisez-le à l'intérieur du fichier `Header.js` comme montré ci-dessous :

```jsx
import React from 'react';
import Progress from './Progress';

const Header = () => (
  <div>
    <h1>Inscription Multi-Étapes</h1>
    <Progress />
  </div>
);

export default Header;

```

Maintenant, si vous vérifiez l'application, vous verrez l'écran suivant :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/with_progress.png)

## Comment créer le formulaire de la première étape

Ouvrez le fichier `components/FirstStep.js` et remplacez ce qui s'y trouve par le contenu suivant :

```jsx
import React from 'react';
import { useForm } from 'react-hook-form';
import { Form, Button } from 'react-bootstrap';

const FirstStep = (props) => {
  const { register, handleSubmit, errors } = useForm();

  const onSubmit = (data) => {
    console.log(data);
  };

  return (
    <Form className="input-form" onSubmit={handleSubmit(onSubmit)}>
      <div className="col-md-6 offset-md-3">
        <Form.Group controlId="first_name">
          <Form.Label>Prénom</Form.Label>
          <Form.Control
            type="text"
            name="first_name"
            placeholder="Entrez votre prénom"
            autoComplete="off"
            ref={register({
              required: 'Le prénom est requis.',
              pattern: {
                value: /^[a-zA-Z]+$/,
                message: 'Le prénom ne doit contenir que des caractères.'
              }
            })}
            className={`${errors.first_name ? 'input-error' : ''}`}
          />
          {errors.first_name && (
            <p className="errorMsg">{errors.first_name.message}</p>
          )}
        </Form.Group>

        <Form.Group controlId="last_name">
          <Form.Label>Nom</Form.Label>
          <Form.Control
            type="text"
            name="last_name"
            placeholder="Entrez votre nom"
            autoComplete="off"
            ref={register({
              required: 'Le nom est requis.',
              pattern: {
                value: /^[a-zA-Z]+$/,
                message: 'Le nom ne doit contenir que des caractères.'
              }
            })}
            className={`${errors.last_name ? 'input-error' : ''}`}
          />
          {errors.last_name && (
            <p className="errorMsg">{errors.last_name.message}</p>
          )}
        </Form.Group>

        <Button variant="primary" type="submit">
          Suivant
        </Button>
      </div>
    </Form>
  );
};

export default FirstStep;

```

Ici, nous utilisons une bibliothèque très populaire [react-hook-form](https://react-hook-form.com/) pour gérer facilement les formulaires avec des validations.

React-hook-form facilite grandement le travail avec des formulaires simples ainsi que complexes, car nous n'avons pas besoin de gérer l'état de chaque champ de saisie et son gestionnaire `onChange` nous-mêmes. Cela rend le code plus propre et plus facile à comprendre.

Consultez [mon article ici](https://www.freecodecamp.org/news/build-forms-in-react-with-react-hook-form-library/) pour en savoir plus sur `react-hook-form` en détail.

Comme vous pouvez le voir dans le code ci-dessus, pour utiliser la bibliothèque `react-hook-form`, nous devons d'abord importer et utiliser le hook `useForm`.

```jsx
  const { register, handleSubmit, errors } = useForm();

```

Ici,

* `register` est une fonction que nous utiliserons comme `ref` fourni par le hook `useForm`. Nous pouvons l'assigner à chaque champ de saisie afin que `react-hook-form` puisse suivre les changements de la valeur du champ de saisie
* `handleSubmit` est la fonction que nous pouvons appeler lorsque le formulaire est soumis
* `errors` contiendra les erreurs de validation, le cas échéant

Dans le code ci-dessus, nous avons donné un `ref` à chaque champ de saisie que nous avons obtenu du hook `useForm` comme ceci :

```js
ref={register({
  required: 'Le prénom est requis.',
  pattern: {
    value: /^[a-zA-Z]+$/,
    message: 'Le prénom ne doit contenir que des caractères.'
  }
})}

```

De plus, nous avons ajouté la fonction `onSubmit` qui est passée à la fonction `handleSubmit`.

```js
<Form className="input-form" onSubmit={handleSubmit(onSubmit)}>

```

Notez que pour chaque champ de saisie, nous avons donné un `name` unique qui est obligatoire afin que `react-hook-form` puisse suivre les données changeantes.

Lorsque nous soumettons le formulaire, la fonction `handleSubmit` gérera la soumission du formulaire. Elle enverra les données saisies par l'utilisateur à la fonction `onSubmit` que nous enregistrons dans la console.

```js
const onSubmit = (data) => {  
 console.log(data);
};

```

S'il y a des erreurs, nous les afficherons comme ceci :

```js
{errors.first_name && (
  <p className="errorMsg">{errors.first_name.message}</p>
)}

```

L'objet `errors` sera automatiquement rempli avec le nom de la propriété désigné par le `name` donné à chaque champ de saisie (s'il y a des erreurs). `first_name` dans le cas ci-dessus est le nom donné au premier champ de saisie.

Maintenant, vérifions la fonctionnalité de l'application :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/first_step_form.gif)

Comme vous pouvez le voir, avec très peu de code, nous avons ajouté une fonctionnalité de validation réactive au formulaire.

## Comment créer le formulaire de la deuxième étape

Maintenant, créez un nouveau fichier `SecondStep.js` à l'intérieur du dossier `components` avec le contenu suivant :

```jsx
import React from 'react';
import { useForm } from 'react-hook-form';
import { Form, Button } from 'react-bootstrap';

const SecondStep = (props) => {
  const { register, handleSubmit, errors } = useForm();

  const onSubmit = (data) => {
    console.log(data);
  };

  return (
    <Form className="input-form" onSubmit={handleSubmit(onSubmit)}>
      <div className="col-md-6 offset-md-3">
        <Form.Group controlId="first_name">
          <Form.Label>Email</Form.Label>
          <Form.Control
            type="email"
            name="user_email"
            placeholder="Entrez votre adresse email"
            autoComplete="off"
            ref={register({
              required: 'L\'email est requis.',
              pattern: {
                value: /^[^@ ]+@[^@ ]+\.[^@ .]{2,}$/,
                message: 'L\'email n\'est pas valide.'
              }
            })}
            className={`${errors.user_email ? 'input-error' : ''}`}
          />
          {errors.user_email && (
            <p className="errorMsg">{errors.user_email.message}</p>
          )}
        </Form.Group>

        <Form.Group controlId="password">
          <Form.Label>Mot de passe</Form.Label>
          <Form.Control
            type="password"
            name="user_password"
            placeholder="Choisissez un mot de passe"
            autoComplete="off"
            ref={register({
              required: 'Le mot de passe est requis.',
              minLength: {
                value: 6,
                message: 'Le mot de passe doit contenir au moins 6 caractères.'
              }
            })}
            className={`${errors.user_password ? 'input-error' : ''}`}
          />
          {errors.user_password && (
            <p className="errorMsg">{errors.user_password.message}</p>
          )}
        </Form.Group>

        <Button variant="primary" type="submit">
          Suivant
        </Button>
      </div>
    </Form>
  );
};

export default SecondStep;

```

Maintenant, ajoutons une autre route dans le fichier `AppRouter.js` pour le composant `SecondStep`.

```jsx
import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import FirstStep from '../components/FirstStep';
import Header from '../components/Header';
import SecondStep from '../components/SecondStep';

const AppRouter = () => (
  <BrowserRouter>
    <div className="container">
      <Header />
      <Switch>
        <Route component={FirstStep} path="/" exact={true} />
        <Route component={SecondStep} path="/second" />
      </Switch>
    </div>
  </BrowserRouter>
);

export default AppRouter;

```

De plus, importez le composant `SecondStep` en haut du fichier comme montré ci-dessus.

Maintenant, nous avons ajouté une route pour la deuxième étape, vérifions l'application en accédant à l'URL [http://localhost:3000/second](http://localhost:3000/second).

![Image](https://www.freecodecamp.org/news/content/images/2021/03/second_step_form.gif)

Comme vous pouvez le voir, la fonctionnalité fonctionne bien, mais nous accédons directement à la route `/second`. Au lieu de cela, ajoutons le code pour rediriger programmatiquement de l'étape 1 à l'étape 2.

Lorsque nous fournissons un composant pour la `Route` à l'intérieur du `BrowserRouter`, React Router passe automatiquement 3 props à ce composant, qui sont :

* history
* location
* match

Parmi ceux-ci, l'objet `history` contient une méthode `push` que nous pouvons utiliser pour rediriger d'un composant à un autre.

Donc, ouvrez le fichier `FirstStep.js` et remplacez la fonction `onSubmit` par le code suivant :

```js
const onSubmit = (data) => {
  console.log(data);
  props.history.push('/second');
};

```

Ici, pour la méthode `push`, nous avons fourni la route vers laquelle nous devons rediriger.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/redirection.gif)

Comme vous pouvez le voir, lorsque nous cliquons sur le bouton `Suivant` dans la première étape, nous sommes redirigés vers la deuxième étape.

Maintenant, créez un nouveau fichier `constants.js` à l'intérieur du dossier `utils` avec le contenu suivant :

```js
export const BASE_API_URL = 'http://localhost:3030';

```

Ici, nous spécifions l'URL de notre API backend afin de ne pas avoir à la spécifier dans chaque appel d'API. Nous devons simplement utiliser cette constante lorsque nous devons faire un appel d'API.

Maintenant, ajoutons une autre route dans notre fichier `AppRouter.js` pour le composant `ThirdStep`.

```jsx
...
<Switch>
  <Route component={FirstStep} path="/" exact={true} />
  <Route component={SecondStep} path="/second" />
  <Route component={ThirdStep} path="/third" />
</Switch>
...

```

## Comment obtenir une liste de tous les pays depuis l'API

Créez un nouveau fichier `ThirdStep.js` à l'intérieur du dossier `components` avec le contenu suivant :

```jsx
import React, { useState, useEffect } from 'react';
import { Form, Button } from 'react-bootstrap';
import csc from 'country-state-city';
import axios from 'axios';
import { BASE_API_URL } from '../utils/constants';

const ThirdStep = (props) => {
  const [countries, setCountries] = useState([]);
  const [states, setStates] = useState([]);
  const [cities, setCities] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  const [selectedCountry, setSelectedCountry] = useState('');
  const [selectedState, setSelectedState] = useState('');
  const [selectedCity, setSelectedCity] = useState('');

  useEffect(() => {
   const getCountries = async () => {
     try {
       const result = await csc.getAllCountries();
       console.log(result);
     } catch (error) {}
    };

    getCountries();
  }, []);

  const handleSubmit = async (event) => {
    event.preventDefault();
  };

  return (
    <Form className="input-form" onSubmit={handleSubmit}>
      <div className="col-md-6 offset-md-3"></div>
    </Form>
  );
};

export default ThirdStep;

```

Dans ce fichier, nous utilisons une bibliothèque npm [country-state-city](https://www.npmjs.com/package/country-state-city) pour obtenir une liste des pays, villes et états disponibles comme ceci :

```js
import csc from 'country-state-city';

```

Ensuite, dans le composant, nous avons défini quelques états :

```js
const [countries, setCountries] = useState([]);
const [states, setStates] = useState([]);
const [cities, setCities] = useState([]);
const [isLoading, setIsLoading] = useState(false);

const [selectedCountry, setSelectedCountry] = useState('');
const [selectedState, setSelectedState] = useState('');
const [selectedCity, setSelectedCity] = useState('');

```

Ici, `countries`, `states` et `cities` sont déclarés dans l'état qui stockera la liste des `countries`, `states` et `cities`, respectivement, provenant de l'API.

Nous ajoutons un autre état `isLoading` pour suivre le moment où les données sont en cours de chargement. `selectedCountry`, `selectedState` et `selectedCity` contiendront la valeur sélectionnée lorsque l'utilisateur sélectionne une valeur particulière dans le menu déroulant.

Ensuite, nous avons ajouté un hook `useEffect` pour faire un appel API afin d'obtenir la liste des pays comme montré ci-dessous :

```js
useEffect(() => {
  ...
  const result = await csc.getAllCountries();
  ...
}, []);

```

Ici, nous appelons la méthode `getAllCountries` de la bibliothèque `country-state-city` pour obtenir une liste des pays disponibles. 

Notez que nous avons passé un tableau vide `[]` comme deuxième argument au hook `useEffect` afin que le hook ne soit appelé qu'une seule fois lorsque le composant est monté.

Maintenant, ouvrez le fichier `SecondStep.js` et remplacez la fonction `onSubmit` par le code suivant :

```js
const onSubmit = (data) => {
  console.log(data);
  props.history.push('/third');
};

```

En utilisant ce code, nous pouvons facilement naviguer vers le composant `ThirdStep`.

Maintenant, vérifions l'application.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/countries_log.gif)

Comme vous pouvez le voir, lors du chargement du composant, nous obtenons une liste des pays disponibles dans un tableau d'objets.

Chaque objet contient une propriété `isoCode` et `name` que nous pouvons utiliser dans notre code pour l'afficher à l'écran.

Donc, modifiez le hook `useEffect` avec le code ci-dessous :

```js
useEffect(() => {
  const getCountries = async () => {
    try {
      setIsLoading(true);
      const result = await csc.getAllCountries();
      let allCountries = [];
      allCountries = result?.map(({ isoCode, name }) => ({
        isoCode,
        name
      }));
      const [{ isoCode: firstCountry } = {}] = allCountries;
      setCountries(allCountries);
      setSelectedCountry(firstCountry);
      setIsLoading(false);
    } catch (error) {
      setCountries([]);
      setIsLoading(false);
    }
  };

  getCountries();
}, []);

```

Ici, nous définissons d'abord le drapeau `isLoading` sur `true` pour indiquer que les données sont en cours de chargement, ce que nous utiliserons bientôt.

Chaque objet du tableau contient de nombreuses autres propriétés comme `phonecode`, `flag`, `currency`, etc., mais nous ne voulons que `isoCode` et `name`. Nous utilisons donc la méthode de mappage du tableau pour filtrer uniquement ces propriétés, comme montré ci-dessous :

```js
allCountries = result?.map(({ isoCode, name }) => ({
  isoCode,
  name
}));

```

Ici, nous utilisons l'opérateur de chaînage optionnel ES11 qui est désigné par le `?`. Le code après le `?` ne sera exécuté que si la référence précédente n'est pas `undefined` ou `null`. Et comme nous déstructurons `isoCode` et `name`, nous avons besoin de l'opérateur de chaînage optionnel.

L'opérateur de chaînage optionnel est très utile dans de nombreux scénarios. Vous pouvez en apprendre davantage à ce sujet dans mon livre [Mastering Modern JavaScript](https://modernjavascript.yogeshchavan.dev/).

Maintenant, nous avons le code suivant :

```js
const [{ isoCode: firstCountry } = {}] = allCountries;
setCountries(allCountries);
setSelectedCountry(firstCountry);
setIsLoading(false);

```

Comprenons ce que nous faisons ici.

Ici, nous avons utilisé la syntaxe de renommage de la déstructuration d'objet avec affectation. Nous déstructurons la propriété `isoCode` du premier objet du tableau d'objets `allCountries` et renommons la propriété `isoCode` en `firstCountry` simplement pour identifier qu'il s'agit du premier pays de la liste. 

Nous attribuons également un objet vide par défaut afin que si le tableau `allCountries` est vide, nous n'obtenions pas d'erreur.

En bref, nous disons de prendre la propriété `isoCode` du premier objet du tableau d'objets `allCountries` et de la renommer en `firstCountry`. 

Si la propriété `firstCountry` n'existe pas dans le premier objet du tableau `allCountries`, alors attribuer une valeur par défaut d'objet vide `{}` à la variable `firstCountry`.

Ensuite, nous mettons à jour la valeur de l'état `selectedCountry` à la valeur `firstCountry` et la valeur de l'état `isLoading` à `false` en utilisant le code ci-dessous :

```js
setSelectedCountry(firstCountry);
setIsLoading(false);

```

Maintenant, dans le fichier `ThirdStep.js`, changez le code suivant :

```jsx
return (
  <Form className="input-form" onSubmit={handleSubmit}>
    <div className="col-md-6 offset-md-3"></div>
  </Form>
);

```

par ce code :

```jsx
return (
    <Form className="input-form" onSubmit={handleSubmit}>
      <div className="col-md-6 offset-md-3">
        <Form.Group controlId="country">
          {isLoading && (
            <p className="loading">Chargement des pays. Veuillez patienter...</p>
          )}
          <Form.Label>Pays</Form.Label>
          <Form.Control
            as="select"
            name="country"
            value={selectedCountry}
            onChange={(event) => setSelectedCountry(event.target.value)}
          >
            {countries.map(({ isoCode, name }) => (
              <option value={isoCode} key={isoCode}>
                {name}
              </option>
            ))}
          </Form.Control>
        </Form.Group>
      </div>
    </Form>
  );

```

Nous pouvons voir la liste des pays peuplée dans le menu déroulant.

Maintenant, si vous naviguez vers l'étape 3, vous verrez l'écran suivant :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/country_populate.gif)

Comme vous pouvez le voir, le menu déroulant des pays est correctement peuplé avec tous les pays. Lorsque la valeur du menu déroulant change, l'état `selectedCountry` change également pour le code du pays (`isoCode`) comme vous pouvez le voir dans les outils de développement React.

## Comment obtenir une liste des états depuis l'API

Maintenant, ajoutons le code pour obtenir une liste des états en fonction du pays sélectionné.

Ajoutez le code suivant après le premier hook `useEffect` dans le fichier `ThirdStep.js`.

```js
useEffect(() => {
    const getStates = async () => {
      try {
        const result = await csc.getStatesOfCountry(selectedCountry);
        let allStates = [];
        allStates = result?.map(({ isoCode, name }) => ({
          isoCode,
          name
        }));
        console.log({ allStates });
        const [{ isoCode: firstState = '' } = {}] = allStates;
        setCities([]);
        setSelectedCity('');
        setStates(allStates);
        setSelectedState(firstState);
      } catch (error) {
        setStates([]);
        setCities([]);
        setSelectedCity('');
      }
    };

    getStates();
  }, [selectedCountry]);

```

Ici, nous appelons la méthode `getStatesOfCountry` de la bibliothèque `country-state-city` en passant le `selectedCountry` comme paramètre. Ensuite, en fonction du résultat de l'API, nous mettons à jour les états respectifs comme montré ci-dessous :

```js
setCities([]);
setSelectedCity('');
setStates(allStates);
setSelectedState(firstState);

```

Tous les menus déroulants de pays, d'état et de ville sont inter-reliés. Si nous changeons le pays, nous devons également mettre à jour l'état, ce que nous faisons dans le code ci-dessus.

Notez également que nous avons passé le `selectedCountry` comme deuxième paramètre au hook `useEffect` dans le tableau des dépendances :

```js
useEffect(() => {
 ...
}, [selectedCountry]); 

```

Ainsi, cet effet ne s'exécutera que lorsque l'état `selectedCountry` changera. Cela signifie que dès que nous changeons le menu déroulant du pays, nous faisons un appel API pour obtenir les états liés uniquement à ce pays, puis nous peuplons les valeurs du menu déroulant des états.

Maintenant, ajoutez le code suivant après la balise de fermeture du premier `Form.Group` qui se trouve après le menu déroulant du pays :

```jsx
<Form.Group controlId="state">
  <Form.Label>État</Form.Label>
  <Form.Control
    as="select"
    name="state"
    value={selectedState}
    onChange={(event) => setSelectedState(event.target.value)}
  >
    {states.length > 0 ? (
      states.map(({ isoCode, name }) => (
        <option value={isoCode} key={isoCode}>
          {name}
        </option>
      ))
    ) : (
      <option value="" key="">
        Aucun état trouvé
      </option>
    )}
  </Form.Control>
</Form.Group>

```

Ici, nous affichons le menu déroulant des états à l'écran. S'il n'y a pas d'états pour le pays sélectionné, nous affichons un message `Aucun état trouvé` car il existe certains pays qui n'ont pas d'états.

Maintenant, si vous vérifiez l'application, vous verrez l'écran suivant :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/state_populate.gif)

Comme vous pouvez le voir ci-dessus, lorsque nous changeons la valeur du menu déroulant du pays, la liste du menu déroulant des états est également mise à jour en fonction du pays sélectionné.

## Comment obtenir une liste des villes depuis l'API

Maintenant, peuplons les villes en fonction des valeurs du pays et de l'état.

Ajoutez un autre hook `useEffect` après le deuxième hook comme montré ci-dessous :

```js
useEffect(() => {
  const getCities = async () => {
    try {
      const result = await csc.getCitiesOfState(
        selectedCountry,
        selectedState
      );
      let allCities = [];
      allCities = result?.map(({ name }) => ({
        name
      }));
      const [{ name: firstCity = '' } = {}] = allCities;
      setCities(allCities);
      setSelectedCity(firstCity);
    } catch (error) {
      setCities([]);
    }
  };

  getCities();
}, [selectedState]);

```

Ici, nous appelons la méthode `getCitiesOfState` de la bibliothèque `country-state-city` en passant `selectedCountry` et `selectedState` comme paramètres. En fonction du résultat de l'API, nous mettons à jour le menu déroulant des villes.

Maintenant, ajoutez le code suivant après la balise de fermeture du deuxième `Form.Group` qui se trouve après le menu déroulant des états :

```jsx
<Form.Group controlId="city">
  <Form.Label>Ville</Form.Label>
  <Form.Control
    as="select"
    name="city"
    value={selectedCity}
    onChange={(event) => setSelectedCity(event.target.value)}
  >
    {cities.length > 0 ? (
      cities.map(({ name }) => (
        <option value={name} key={name}>
          {name}
        </option>
      ))
    ) : (
      <option value="">Aucune ville trouvée</option>
    )}
  </Form.Control>
</Form.Group>

```

Ici, nous affichons le menu déroulant des villes à l'écran. S'il n'y a pas de villes pour l'état sélectionné, nous affichons un message `Aucune ville trouvée` car il existe certains états qui n'ont pas de villes.

Maintenant, si vous vérifiez l'application, vous verrez l'écran suivant :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/city_populate.gif)

Comme vous pouvez le voir ci-dessus, lors du changement de pays et d'état, la liste correspondante des villes est peuplée dans le menu déroulant des villes.

De plus, ajoutez le bouton `Register` après la balise de fermeture du dernier `Form.Group` qui se trouve après le menu déroulant des villes :

```jsx
<Button variant="primary" type="submit">
  S'inscrire
</Button>

```

Maintenant, votre écran ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/last_step.png)

Nous avons terminé la création des écrans pour toutes les étapes. Maintenant, faisons fonctionner la progression des étapes dans l'en-tête afin qu'il soit clair à quelle étape nous nous trouvons actuellement.

## Comment ajouter un indicateur de progression dans l'en-tête

Nous affichons le composant `Progress` à l'intérieur du composant `Header`, mais le composant `Progress` n'est pas mentionné dans aucune des `Route`s dans le fichier `AppRouter.js`. De plus, `Header` n'est pas mentionné dans la `Route`. 

Par défaut, nous n'avons pas accès aux props `history`, `location` et `match` dans les composants `Header` et `Progress` pour identifier sur quelle route nous nous trouvons.

Mais il existe un moyen facile de corriger cela. React Router fournit un composant `withRouter` que nous pouvons utiliser dans le composant `Progress` afin que nous ayons accès aux props `history`, `location` et `match`.

Ouvrez le fichier `Progress.js` et ajoutez l'import du composant `withRouter` en haut du fichier :

```js
import { withRouter } from 'react-router-dom';

```

et changez l'instruction d'export de ce code :

```js
export default Progress;

```

en ce code :

```js
export default withRouter(Progress);

```

Ainsi, lorsque nous passons le composant `Progress` au composant `withRouter`, nous aurons accès aux props `history`, `location` et `match` à l'intérieur du composant `Progress`.

Maintenant, remplacez le composant `Progress` par le code suivant :

```jsx
const Progress = ({ location: { pathname } }) => {
  const isFirstStep = pathname === '/';
  const isSecondStep = pathname === '/second';
  const isThirdStep = pathname === '/third';

  return (
    <React.Fragment>
      <div className="steps">
        <div className={`${isFirstStep ? 'step active' : 'step'}`}>
          <div>1</div>
          <div>
            {isSecondStep || isThirdStep ? (
              <Link to="/">Étape 1</Link>
            ) : (
              'Étape 1'
            )}
          </div>
        </div>
        <div className={`${isSecondStep ? 'step active' : 'step'}`}>
          <div>2</div>
          <div>{isThirdStep ? <Link to="/second">Étape 2</Link> : 'Étape 2'}</div>
        </div>
        <div className={`${pathname === '/third' ? 'step active' : 'step'}`}>
          <div>3</div>
          <div>Étape 3</div>
        </div>
      </div>
    </React.Fragment>
  );
};

```

Ici, dans la première ligne, nous déstructurons la propriété `location` de l'objet `props` puis la propriété `pathname` de la propriété `location` en une seule ligne comme ceci :

```jsx
const Progress = ({ location: { pathname } }) => {

```

Et en fonction de la route sur laquelle nous nous trouvons, nous ajoutons la classe `active` à chaque div `step`.

De plus, importez le composant `Link` en haut du fichier :

```js
import { Link, withRouter } from 'react-router-dom';

```

Maintenant, si vous vérifiez l'application, vous verrez l'écran suivant :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/progress_working.gif)

Comme vous pouvez le voir, lorsque nous sommes sur une étape particulière, ce numéro d'étape est affiché comme actif dans la barre de progression avec un texte en surbrillance. Ensuite, lorsque nous naviguons à travers les étapes, le texte des étapes précédentes est affiché comme un lien afin que nous puissions revenir à n'importe quelle étape pour modifier des données.

## Comment conserver les données saisies entre les routes

Mais vous remarquerez que, lorsque nous revenons à l'étape 1 en cliquant sur le lien depuis l'étape 3, les données saisies dans l'étape 1 sont perdues.

Cela est dû au fait que lorsque nous passons d'une route à une autre, React Router démonte complètement le composant de la route précédente et monte le composant de la route suivante connecté à cette route. Cela entraîne la perte de toutes les valeurs d'état.

Alors, ajoutons un moyen de préserver les données qui ont été saisies lors de la navigation vers l'étape précédente.

Comme vous le savez, seuls les composants connectés aux routes mentionnées dans le fichier `AppRouter.js` sont montés et démontés lors du changement de route. Mais le composant `AppRouter` dans notre cas n'est pas démonté même lorsque les routes changent.

Cela signifie que le meilleur endroit pour stocker les données saisies par l'utilisateur est dans le composant `AppRouter`.

Ajoutons l'état `user`, les fonctions `updateUser` et `resetUser` à l'intérieur du fichier `AppRouter.js`.

```js
const [user, setUser] = useState({});

const updateUser = (data) => {
  setUser((prevUser) => ({ ...prevUser, ...data }));
};

const resetUser = () => {
  setUser({});
};

```

Ainsi, nous stockerons les données saisies par l'utilisateur à chaque étape dans l'état `user` qui est un objet.

Dans la fonction `updateUser`, nous passons des données pour mettre à jour l'état `user`. Dans la fonction `updateUser`, nous étalons d'abord les valeurs de l'objet `user` en utilisant la variable `prevUser`, puis nous étalons l'objet `data` afin que l'objet résultant soit la fusion des deux objets.

Pour mettre à jour l'état, nous utilisons la syntaxe de mise à jour de l'état avec la syntaxe de retour implicite pour l'objet.

Ainsi, ce code :

```js
setUser((prevUser) => ({ ...prevUser, ...data }));

```

est le même que le code ci-dessous :

```js
setUser((prevUser) => {
  return {
    ...prevUser,
    ...data
  };
});

```

Comme vous pouvez le voir ci-dessus, si nous voulons retourner implicitement un objet à partir d'une fonction fléchée, nous pouvons sauter le mot-clé return et enfermer l'objet dans des parenthèses.

Cela rendra le code plus court et vous aidera également à éviter les erreurs de frappe dans votre code. Grâce à cela, vous constaterez que la plupart du code React est écrit en utilisant la syntaxe de retour implicite.

Ainsi, si nous sommes à l'étape 1, nous passerons `{first_name: 'Mike', last_name: 'Jordan' }` comme `data` et l'ajouterons à l'état `user`.

Ensuite, à l'étape 2, si nous passons `{user_email: 'test@example.com', user_password: 'test@123'}` comme `data`, alors la fonction `updateUser` mettra à jour l'`user` comme montré ci-dessous :

```js
const prevUser = { first_name: 'Mike', last_name: 'Jordan' };
const data = { user_email: 'test@example.com', user_password: 'test@123' };

const result = { ...prevUser, ...data };
console.log(result); // { first_name: 'Mike', last_name: 'Jordan', user_email: 'test@example.com', user_password: 'test@123' }

```

Maintenant, nous avons créé l'état `user` et la fonction `updateUser`. Nous devons donc les passer à chaque route qui est connectée à l'étape afin que nous puissions sauvegarder les données saisies par l'utilisateur en appelant la fonction `updateUser`.

Nos routes actuelles dans le fichier `AppRouter.js` ressemblent à ceci :

```js
<Switch>
  <Route component={FirstStep} path="/" exact={true} />
  <Route component={SecondStep} path="/second" />
  <Route component={ThirdStep} path="/third" />
</Switch>

```

Ainsi, pour passer `user` et `updateUser` en tant que props aux composants connectés à la route, nous ne pouvons pas les passer comme ceci :

```js
<Route component={FirstStep} path="/" exact={true} user={user} updateUser={updateUser} />

```

Car de cette manière, les props seront passés à la `Route` et non au composant `FirstStep`. Nous devons donc utiliser la syntaxe suivante :

```js
<Route
  render={(props) => (
    <FirstStep {...props} user={user} updateUser={updateUser} />
  )}
  path="/"
  exact={true}
/>

```

Ici, nous utilisons le motif des props de rendu pour passer les props. Cela passera correctement les props et ne recréera pas le composant `FirstStep` à chaque nouveau rendu.

Vous pouvez consulter mon cours [Introduction à React Router](https://yogeshchavan1.podia.com/react-router-introduction) pour en savoir plus sur pourquoi nous devons utiliser `render` au lieu de la prop `component`.

Maintenant, après avoir apporté cette modification pour toutes les routes liées aux étapes, vos routes ressembleront à ceci :

```jsx
<BrowserRouter>
  <div className="container">
    <Header />
    <Switch>
      <Route
        render={(props) => (
          <FirstStep {...props} user={user} updateUser={updateUser} />
        )}
        path="/"
        exact={true}
      />
      <Route
        render={(props) => (
          <SecondStep {...props} user={user} updateUser={updateUser} />
        )}
        path="/second"
      />
      <Route
        render={(props) => (
          <ThirdStep {...props} user={user}  />
        )}
        path="/third"
      />
    </Switch>
  </div>
</BrowserRouter>

```

Notez que nous ne passons pas la prop `updateUser` à la route du composant `ThirdStep`, car lorsque nous soumettons le formulaire depuis l'étape 3, nous enregistrerons toutes les données directement dans la base de données.

Si vous le souhaitez, vous pouvez passer la fonction `updateUser` au composant `ThirdStep` et l'enregistrer dans l'état en appelant la fonction `updateUser` (mais ce n'est pas nécessaire).

Maintenant, utilisons la fonction `updateUser` à l'intérieur de ces composants pour enregistrer les données.

Donc, ouvrez les fichiers `FirstStep.js` et `SecondStep.js` et, à l'intérieur de la fonction de gestionnaire `onSubmit`, ajoutez `props.updateUser(data)` comme première instruction.

```js
// FirstStep.js
const onSubmit = (data) => {
  props.updateUser(data);
  props.history.push('/second');
};

// SecondStep.js
const onSubmit = (data) => {
  props.updateUser(data);
  props.history.push('/third');
};

```

Maintenant, si vous vérifiez l'application, vous verrez l'écran suivant :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/saving_to_state.gif)

Comme vous pouvez le voir, initialement l'état du composant `AppRouter` est un objet vide. Mais lorsque nous soumettons le formulaire à chaque étape, l'objet d'état est mis à jour avec les données saisies par l'utilisateur.

Maintenant, utilisons ces données enregistrées dans l'état et peuplons-les dans les champs de saisie respectifs lorsque nous revenons à l'étape précédente depuis l'étape suivante.

Comme vous le savez, nous utilisons `react-hook-form` pour gérer les données changeantes de nos formulaires dans les composants `FirstStep` et `SecondStep` en utilisant le hook `useForm`.

Mais le hook `useForm` prend également un paramètre optionnel que nous pouvons utiliser pour persister les valeurs entre les changements de route.

Donc, changez le code ci-dessous du fichier `FirstStep.js` :

```js
const { register, handleSubmit, errors } = useForm();

```

par ce code :

```js
const { user } = props;
const { register, handleSubmit, errors } = useForm({
  defaultValues: {
    first_name: user.first_name,
    last_name: user.last_name
  }
});

```

Ici, nous déstructurons la prop `user` de l'objet props que nous passons dans la route du fichier `AppRouter.js`. Ensuite, nous utilisons la propriété `defaultValues` pour définir la valeur de chaque champ de saisie.

Juste pour vous rappeler, `first_name` et `last_name` sont les noms donnés aux champs de saisie dans le composant `FirstStep` que react-hook-form utilise pour suivre les données changeantes.

Maintenant, si vous vérifiez l'application, vous verrez l'écran suivant :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/data_retained.gif)

Comme vous pouvez le voir, lorsque nous revenons de l'étape 2 à l'étape 1, les données saisies à l'étape 1 ne sont pas perdues. Cela est dû au fait que nous les réinitialisons avec les données de l'état `user` lorsque le composant est remonté lors du changement de route.

Maintenant, ajoutons un code similaire dans le fichier `SecondStep.js` également :

```js
const { user } = props;
const { register, handleSubmit, errors } = useForm({
  defaultValues: {
    user_email: user.user_email,
    user_password: user.user_password
  }
});

```

Si vous vérifiez l'application, vous verrez l'écran suivant :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/data_retained_step2.gif)

Comme vous pouvez le voir, lorsque nous revenons de l'étape 3 à l'étape 2 ou à l'étape 1, les données saisies à l'étape 1 et à l'étape 2 ne sont pas perdues. Nous avons donc réussi à préserver les données entre les étapes.

## Comment ajouter des transitions animées à l'application

Maintenant, ajoutons une fonctionnalité d'animation de glissement fluide à l'application.

Pour ajouter une animation, nous utilisons la bibliothèque très populaire [framer motion](https://www.framer.com/motion/).

Framer motion facilite l'ajout d'animations en utilisant une approche déclarative de la même manière que React fait les choses.

Alors, ajoutons une animation dans le composant `FirstStep`.

Ouvrez le fichier `FirstStep.js` et ajoutez l'instruction d'import pour la bibliothèque framer motion en haut du fichier :

```js
import { motion } from 'framer-motion';

```

Pour animer un élément sur la page, nous devons le préfixer avec `motion` comme ceci :

```html
<div>Cliquez ici pour l'animer</div>

// le code ci-dessus devra être converti en

<motion.div>Cliquez ici pour l'animer</motion.div>

```

L'utilisation de motion comme préfixe retournera un composant React auquel des capacités d'animation spécifiques ont été ajoutées afin que nous puissions passer des props à cet élément.

Donc, à l'intérieur du fichier `FirstStep.js`, après avoir ajouté le préfixe motion à la div suivante :

```html
<div className="col-md-6 offset-md-3">
...
</div>

```

elle ressemblera à ceci :

```html
<motion.div className="col-md-6 offset-md-3">
...
</motion.div>

```

Une fois que nous avons ajouté un préfixe motion, nous pouvons fournir des props supplémentaires à cet élément comme ceci :

```html
<motion.div
  className="col-md-6 offset-md-3"
  initial={{ x: '-100vw' }}
  animate={{ x: 0 }}
>
...
</motion.div>

```

Ici, nous avons fourni une prop `initial` pour spécifier l'emplacement à partir duquel l'animation commencerá. Nous voulons que l'ensemble du formulaire glisse depuis le côté gauche, donc nous avons fourni la valeur `x` comme `-100vw`. Cela signifie 100% de la largeur de la fenêtre d'affichage depuis le côté gauche. Ainsi, la position initiale du formulaire sera à gauche mais non visible à l'écran.

Ensuite, nous avons fourni la prop `animate` avec une valeur `x` de `0` afin que le formulaire glisse depuis la gauche et revienne à sa position d'origine sur la page. Si nous fournissons une valeur de `10` pour `x`, il se déplacera alors à `10px` sur le côté droit de sa position d'origine.

Maintenant, votre code JSX entier dans le fichier `FirstStep.js` ressemblera à ceci :

```jsx
return (
  <Form className="input-form" onSubmit={handleSubmit(onSubmit)}>
    <motion.div
      className="col-md-6 offset-md-3"
      initial={{ x: '-100vw' }}
      animate={{ x: 0 }}
    >
      <Form.Group controlId="first_name">
        <Form.Label>Prénom</Form.Label>
        <Form.Control
          type="text"
          name="first_name"
          placeholder="Entrez votre prénom"
          autoComplete="off"
          ref={register({
            required: 'Le prénom est requis.',
            pattern: {
              value: /^[a-zA-Z]+$/,
              message: 'Le prénom ne doit contenir que des caractères.'
            }
          })}
          className={`${errors.first_name ? 'input-error' : ''}`}
        />
        {errors.first_name && (
          <p className="errorMsg">{errors.first_name.message}</p>
        )}
      </Form.Group>

      <Form.Group controlId="last_name">
        <Form.Label>Nom</Form.Label>
        <Form.Control
          type="text"
          name="last_name"
          placeholder="Entrez votre nom"
          autoComplete="off"
          ref={register({
            required: 'Le nom est requis.',
            pattern: {
              value: /^[a-zA-Z]+$/,
              message: 'Le nom ne doit contenir que des caractères.'
            }
          })}
          className={`${errors.last_name ? 'input-error' : ''}`}
        />
        {errors.last_name && (
          <p className="errorMsg">{errors.last_name.message}</p>
        )}
      </Form.Group>

      <Button variant="primary" type="submit">
        Suivant
      </Button>
    </motion.div>
  </Form>
);

```

Maintenant, si vous vérifiez l'application, vous verrez l'animation de glissement au chargement de la page :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/sliding_animation.gif)

Comme vous pouvez le voir, le formulaire glisse depuis le côté gauche de la page, mais il ne semble pas encore très fluide.

Pour le rendre plus fluide, nous pouvons fournir une autre prop `transition` en plus des props `initial` et `animate`.

```html
<motion.div
  className="col-md-6 offset-md-3"
  initial={{ x: '-100vw' }}
  animate={{ x: 0 }}
  transition={{ stiffness: 150 }}
>
...
</motion.div>

```

Ici, nous avons ajouté une prop `transition` avec une valeur de `150` pour `stiffness`. Vous pouvez essayer de changer la valeur de `150` à autre chose et voir laquelle vous semble la meilleure. J'utiliserai `150` ici.

Maintenant, si vous vérifiez l'application, vous verrez une animation de glissement fluide au chargement de la page :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/smooth_animation.gif)

Apportons les mêmes modifications d'animation dans les fichiers `SecondStep.js` et `ThirdStep.js` :

```js
import { motion } from 'framer-motion';
...
<motion.div
  className="col-md-6 offset-md-3"
  initial={{ x: '-100vw' }}
  animate={{ x: 0 }}
  transition={{ stiffness: 150 }}
>
...
</motion.div>

```

Maintenant, si vous vérifiez l'application, vous verrez une animation de glissement fluide au chargement de la page pour les 3 étapes :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/all_steps_animation.gif)

## Comment configurer le backend avec Node.js

Nous avons terminé toute la fonctionnalité de base pour le front-end. Maintenant, configurons le code du serveur backend afin que nous puissions sauvegarder les données saisies dans le formulaire vers MongoDB.

Créez un nouveau dossier avec le nom `server` à l'extérieur du dossier `src`. Ensuite, créez des dossiers `models` et `routers` à l'intérieur du dossier `server`.

Maintenant, exécutez la commande suivante à partir du dossier `server` depuis le terminal :

```javascript
yarn init -y

```

Cela créera un fichier `package.json` à l'intérieur du dossier `server` afin que nous puissions gérer les dépendances.

Maintenant, installez les dépendances requises en exécutant la commande suivante à partir du dossier `server` depuis le terminal :

```javascript
yarn add bcryptjs@2.4.3 cors@2.8.5 express@4.17.1 mongoose@5.11.18 nodemon@2.0.7

```

Ensuite, créez un nouveau fichier avec le nom `.gitignore` à l'intérieur du dossier `server` et ajoutez la ligne suivante à l'intérieur afin que le dossier `node_modules` ne soit pas poussé vers GitHub (si vous décidez de pousser votre code vers GitHub) :

```javascript
node_modules

```

Créez un nouveau fichier `db.js` à l'intérieur du dossier `server` avec le contenu suivant :

```js
const mongoose = require('mongoose');

mongoose.connect('mongodb://127.0.0.1:27017/form-user', {
  useNewUrlParser: true,
  useCreateIndex: true,
  useUnifiedTopology: true
});

```

Ici, nous utilisons la bibliothèque `mongoose` pour travailler avec MongoDB. Pour la méthode `mongoose.connect`, nous avons fourni une chaîne de connexion avec la base de données `form-user` comme nom de la base de données.

Vous pouvez donner le nom que vous voulez au lieu de `form-user`.

Maintenant, créez un nouveau fichier avec le nom `index.js` à l'intérieur du dossier `server` et ajoutez le contenu suivant à l'intérieur :

```js
const express = require('express');
require('./db');

const app = express();
const PORT = process.env.PORT || 3030;

app.get('/', (req, res) => {
  res.send('<h2>Ceci provient du fichier index.js</h2>');
});

app.listen(PORT, () => {
  console.log(`serveur démarré sur le port ${PORT}`);
});

```

Maintenant, ouvrez le fichier `server/package.json` et ajoutez la section `scripts` à l'intérieur :

```js
"scripts": {
  "start": "nodemon index.js"
},

```

Ici, nous utilisons le package npm `nodemon` qui redémarrera le serveur Express si nous apportons des modifications à `index.js` ou aux fichiers inclus dans le fichier `index.js`. De cette manière, nous n'avons pas besoin de redémarrer manuellement le serveur à chaque changement.

Ainsi, votre fichier `package.json` complet ressemblera à ceci :

```js
{
  "name": "server",
  "version": "1.0.0",
  "main": "index.js",
  "license": "MIT",
  "scripts": {
    "start": "nodemon index.js"
  },
  "dependencies": {
    "bcryptjs": "2.4.3",
    "cors": "2.8.5",
    "express": "4.17.1",
    "mongoose": "5.11.18",
    "nodemon": "2.0.7"
  }
}

```

Maintenant, ouvrez un autre terminal et exécutez la commande `yarn start` depuis l'intérieur du dossier `server`.

Si vous accédez à [http://localhost:3030/](http://localhost:3030/), vous verrez l'écran suivant :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/server_initial_page.png)

Cela montre que notre serveur Express est correctement configuré. Écrivons des API Rest pour stocker les données d'inscription des utilisateurs.

Créez un nouveau fichier appelé `user.js` à l'intérieur du dossier `server/models` avec le contenu suivant :

```js
const mongoose = require('mongoose');

const userSchema = mongoose.Schema(
  {
    first_name: {
      type: String,
      required: true,
      trim: true
    },
    last_name: {
      type: String,
      required: true,
      trim: true
    },
    user_email: {
      type: String,
      required: true,
      trim: true,
      validate(value) {
        if (!value.match(/^[^@ ]+@[^@ ]+\.[^@ .]{2,}$/)) {
          throw new Error('Email is not valid.');
        }
      }
    },
    user_password: {
      type: String,
      required: true,
      trim: true,
      minlength: 6
    },
    country: {
      type: String,
      required: true,
      trim: true
    },
    state: {
      type: String,
      trim: true
    },
    city: {
      type: String,
      trim: true
    }
  },
  {
    timestamps: true
  }
);

const User = mongoose.model('User', userSchema);

module.exports = User;

```

Ici, nous avons créé un schéma `User` pour définir la structure des données stockées dans la collection `User`.

Si vous n'avez jamais travaillé avec la bibliothèque `mongoose`, consultez [cet article](https://javascript.plainenglish.io/what-is-so-special-about-mongoose-library-when-working-with-mongodb-65096b97f8ae?source=friends_link&sk=5c98c783bd200aa6ce59aa8b16e56f1f) pour une introduction.

## Comment créer les API REST

Créez un nouveau fichier appelé `user.js` à l'intérieur du dossier `routers` avec le contenu suivant :

```js
const express = require('express');
const User = require('../models/user');
const bcrypt = require('bcryptjs');
const router = express.Router();

router.post('/register', async (req, res) => {
 const { user_email, user_password } = req.body;

 console.log('req.body', req.body);

 let user = await User.findOne({ user_email });
 if (user) {
   return res.status(400).send('Un utilisateur avec l\'email fourni existe déjà.');
 }

 try {
   user = new User(req.body);
   user.user_password = await bcrypt.hash(user_password, 8);

   await user.save();
   res.status(201).send();
 } catch (e) {
   res.status(500).send('Quelque chose s\'est mal passé. Veuillez réessayer plus tard.');
 }
});

module.exports = router;

```

Ici, nous avons créé une API post pour la route `/register`. Nous allons passer les données à cette API au format JSON. Le serveur Express les rend disponibles à l'intérieur de l'objet `req.body`, donc nous déstructurons la valeur de l'email et du mot de passe :

```js
const { user_email, user_password } = req.body;

```

Ensuite, en utilisant la méthode `findOne` du modèle `User`, nous vérifions d'abord s'il existe un utilisateur avec l'adresse email fournie.

```js
let user = await User.findOne({ user_email });

```

Si un tel utilisateur existe, nous renvoyons une erreur au client (qui est notre application React).

```js
return res.status(400).send('Un utilisateur avec l\'email fourni existe déjà.');

```

Il est toujours bon de spécifier le code de réponse HTTP de l'erreur lors de l'envoi de la réponse.

Vous pouvez trouver tous les codes d'état HTTP et leurs significations sur [ce site web](https://httpstatuses.com/).

Ensuite, nous passons toutes les données de l'utilisateur (comme `first_name`, `last_name`, `user_email`, `users_password`, `country`, `state` et `city`) qui sont présentes dans le `req.body` au constructeur `User`.

Mais nous ne voulons pas stocker les données saisies par l'utilisateur dans la base de données telles quelles. Nous allons donc utiliser la bibliothèque npm populaire [bcryptjs](https://www.npmjs.com/package/bcryptjs) pour hacher le mot de passe avant de l'enregistrer dans la base de données.

```js
user.user_password = await bcrypt.hash(user_password, 8);

```

Consultez [mon article ici](https://javascript.plainenglish.io/how-to-create-a-strong-and-secure-password-in-nodejs-which-cannot-be-decrypted-24d046b24958?source=friends_link&sk=87160d305a0b0cd97ec18d376a5d7765) pour en savoir plus sur `bcryptjs` en détail.

Et une fois le mot de passe haché, nous appelons la méthode `save` du modèle `User` pour enregistrer tous les détails ainsi que le mot de passe haché dans la base de données MongoDB.

```js
await user.save();

```

Une fois que nous avons terminé, nous renvoyons la réponse avec le code d'état `201` qui décrit qu'une ressource a été créée.

```js
res.status(201).send();

```

Notez qu'ici nous ne renvoyons aucune donnée – juste une réponse indiquant que la requête a réussi et qu'un nouvel enregistrement a été créé.

Ensuite, à la fin, nous exportons le routeur `express` afin de pouvoir l'utiliser dans le fichier `index.js`.

Maintenant, ouvrez le fichier `server/index.js` et importez le routeur utilisateur en haut du fichier :

```js
const userRouter = require('./routers/user');

```

Comme nous envoyons les données pour nous inscrire depuis l'application React vers le serveur Node.js au format JSON, nous devons ajouter le code suivant pour le middleware :

```js
app.use(express.json());

```

De plus, après la constante `PORT`, ajoutez la ligne de code suivante :

```js
app.use(userRouter);

```

Ainsi, votre fichier `server/index.js` complet ressemblera à ceci :

```js
const express = require('express');
const userRouter = require('./routers/user');
require('./db');

const app = express();
const PORT = process.env.PORT || 3030;

app.use(express.json());
app.use(userRouter);

app.get('/', (req, res) => {
  res.send('<h2>Ceci provient du fichier index.js</h2>');
});

app.listen(PORT, () => {
  console.log(`serveur démarré sur le port ${PORT}`);
});

```

Ici, nous avons fourni `userRouter` comme middleware pour l'application Express afin que nous puissions faire des requêtes API.

Il est toujours bon de séparer chaque routeur dans son propre fichier et de l'inclure en utilisant la méthode `app.use`. Cela évite d'agrandir le code en l'écrivant dans un seul fichier.

Maintenant, démarrez votre serveur de base de données MongoDB local en exécutant `./mongod --dbpath=<chemin_vers_le_dossier_mongodb-data>` comme expliqué dans [cet article](https://levelup.gitconnected.com/how-to-install-mongodb-database-on-local-environment-19a8a76f1b92?source=friends_link&sk=416b443bad1f86b292e4b72602cf5c9b) et gardez-le en cours d'exécution.

Puis redémarrez le serveur Express en exécutant `yarn start` depuis le dossier `server` et gardez-le en cours d'exécution.

Ouvrez un autre terminal et démarrez l'application react en exécutant `yarn start` si vous ne l'avez pas déjà fait.

Ainsi, vous aurez maintenant deux terminaux ouverts séparément – un pour exécuter l'application du serveur Express et un autre pour exécuter l'application React comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/vscode_terminals.gif)

Ici, nous ouvrons des terminaux à l'intérieur de VSCode. Vous pouvez ouvrir le premier terminal en allant dans le menu `Terminal -> Nouveau Terminal` dans VS Code. Ensuite, cliquez simplement sur l'icône `+` pour ouvrir des terminaux supplémentaires.

## Comment appeler les API REST depuis une application React

Maintenant, apportons les modifications de code dans notre application React pour faire l'appel API à notre API `/register`.

Ouvrez le fichier `ThirdStep.js` et remplacez la méthode `handleSubmit` par le code suivant :

```js
const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      const { user } = props;
      const updatedData = {
        country: countries.find(
          (country) => country.isoCode === selectedCountry
        )?.name,
        state:
          states.find((state) => state.isoCode === selectedState)?.name || '',
        city: selectedCity
      };

      await axios.post(`${BASE_API_URL}/register`, {
        ...user,
        ...updatedData
      });
    } catch (error) {
      if (error.response) {
        console.log('error', error.response.data);
      }
    }
  };

```

Ici, une fois que nous soumettons le formulaire à l'étape 2, nous appelons la méthode `handleSubmit` où nous faisons un appel API à notre API `/register` :

```js
await axios.post(`${BASE_API_URL}/register`, {
  ...user,
  ...updatedData
});

```

Ici, nous passons les données à l'API `/register` au format JSON.

Nous stockons le code du pays dans `selectedCountry` et le code de l'état dans la variable d'état `selectedState`. Ceux-ci sont désignés par `isoCode`, et nous utilisons d'abord la méthode `find` du tableau pour trouver les noms réels liés à ce code de pays et d'état comme montré ci-dessous :

```js
const updatedData = {
  country: countries.find(
    (country) => country.isoCode === selectedCountry
  )?.name,
  state:
    states.find((state) => state.isoCode === selectedState)?.name || '',
  city: selectedCity
};

```

À l'intérieur de la variable d'état `selectedCity`, nous stockons le nom, donc nous n'avons pas besoin d'utiliser la méthode de filtre ici.

Si vous souhaitez un rappel rapide sur les méthodes de tableau les plus largement utilisées (y compris la méthode de recherche de tableau), consultez [mon article ici](https://www.freecodecamp.org/news/complete-introduction-to-the-most-useful-javascript-array-methods/).

Lors de l'utilisation de la méthode `find` pour l'état, nous avons ajouté la condition `||`. Cela est dû au fait que si aucun état n'est disponible pour un pays sélectionné, alors lors de l'accès à `?.name`, il pourrait être `undefined`. Pour éviter de stocker `undefined` dans la base de données, nous utilisons l'opérateur `||` pour stocker une chaîne vide `''` au lieu de `undefined`.

## Comment tester les API REST

Maintenant, vérifions la fonctionnalité de l'application.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/cors_error.gif)

Comme vous pouvez le voir, lorsque nous essayons de soumettre le formulaire à l'étape 3, nous obtenons une erreur CORS (Cross-Origin Resource Sharing) dans la console du navigateur.

Cela est dû au fait que le navigateur ne nous permet pas d'accéder aux données d'une application s'exécutant sur un autre port – car nous exécutons notre application React sur le port 3000 et notre application Node.js sur le port 3030.

Cela est pour des raisons de sécurité et viole les politiques de domaine croisé.

Pour corriger cela, nous devons installer le package npm [cors](https://www.npmjs.com/package/cors) et l'utiliser dans notre fichier `server/index.js` afin que le serveur Node.js permette à toute application d'accéder à ses API.

Ne vous inquiétez pas, nous verrons comment nous pouvons utiliser les API Node.js sans utiliser `cors` plus tard dans cet article. Nous éviterons également d'avoir besoin d'exécuter deux terminaux séparés pour démarrer notre serveur React et Node.js.

Pour l'instant, ouvrez le fichier `server/index.js` et ajoutez l'import pour `cors` comme montré ci-dessous :

```js
const cors = require('cors');

```

Notez que nous avons déjà installé le package npm `cors` lors de la création du serveur Express précédemment.

Et ajoutez-le en tant que middleware Express avant l'instruction `app.use(userRouter)` comme ceci :

```js
app.use(express.json());
app.use(cors());
app.use(userRouter);

```

Maintenant, votre fichier `index.js` ressemblerá à ceci :

```js
const express = require('express');
const cors = require('cors');
const userRouter = require('./routers/user');
require('./db');

const app = express();
const PORT = process.env.PORT || 3030;

app.use(express.json());
app.use(cors());
app.use(userRouter);

app.get('/', (req, res) => {
 res.send('<h2>Ceci provient du fichier index.js</h2>');
});

app.listen(PORT, () => {
 console.log(`serveur démarré sur le port ${PORT}`);
});

```

Si vous soumettez le formulaire, vous verrez que les données ont été correctement enregistrées dans la console :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/save_log-1.gif)

Et les données sont également enregistrées dans la base de données comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/saved_into_db.png)

Ainsi, nous avons réussi à connecter notre application front-end React à l'application back-end Node.js et à enregistrer les données dans la base de données.

## Comment afficher la popup de retour d'inscription

Vous avez peut-être remarqué que nous n'affichons aucune indication que les données ont été enregistrées avec succès dans la base de données une fois que nous avons inscrit l'utilisateur. Alors, faisons cela maintenant.

Pour afficher le message de succès, nous utiliserons [sweetalert2](https://www.npmjs.com/package/sweetalert2) qui est une bibliothèque de modale popup populaire et personnalisable.

Importez-la dans le fichier `ThirdStep.js` comme montré ci-dessous :

```js
import Swal from 'sweetalert2';

```

À l'intérieur de la fonction `handleSubmit`, après l'appel `axios.post`, ajoutez le code suivant dans le bloc try :

```js
Swal.fire('Super !', "Vous êtes inscrit avec succès !", 'success').then(
(result) => {
  if (result.isConfirmed || result.isDismissed) {
    props.history.push('/');
  }
}
);

```

et dans le bloc catch, ajoutez le code suivant :

```js
if (error.response) {
  Swal.fire({
    icon: 'error',
    title: 'Oups...',
    text: error.response.data
  });
}

```

Ainsi, votre fonction `handleSubmit` ressemblera à ceci maintenant :

```js
const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      const { user } = props;
      const updatedData = {
        country: countries.find(
          (country) => country.isoCode === selectedCountry
        )?.name,
        state:
          states.find((state) => state.isoCode === selectedState)?.name || '', // ou condition ajoutée car selectedState pourrait être undefined
        city: selectedCity
      };

      await axios.post(`${BASE_API_URL}/register`, {
        ...user,
        ...updatedData
      });
      Swal.fire('Super !', "Vous êtes inscrit avec succès !", 'success').then(
        (result) => {
          if (result.isConfirmed || result.isDismissed) {
            props.history.push('/');
          }
        }
      );
    } catch (error) {
      if (error.response) {
        Swal.fire({
          icon: 'error',
          title: 'Oups...',
          text: error.response.data
        });
        console.log('error', error.response.data);
      }
    }
  };

```

Si vous vérifiez l'application, vous verrez l'écran suivant :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/email_error.gif)

Comme vous pouvez le voir, si l'utilisateur avec l'adresse e-mail existe déjà dans la base de données, nous affichons un message d'erreur à partir du bloc catch.

Et si l'e-mail de l'utilisateur n'existe pas dans la base de données, alors nous voyons la popup de succès comme vous pouvez le voir ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/success_register.gif)

Si vous vérifiez le code de la popup pour le succès, il ressemble à ceci :

```js
Swal.fire('Super !', "Vous êtes inscrit avec succès !", 'success').then(
  (result) => {
    if (result.isConfirmed || result.isDismissed) {
      props.history.push('/');
    }
  }
);

```

Ainsi, si l'utilisateur clique sur le bouton `OK` ou clique en dehors de la modale popup, nous redirigeons l'utilisateur vers l'étape 1 en utilisant `props.history.push('/');`. Mais nous devons également effacer les données saisies par l'utilisateur des champs de saisie une fois l'inscription réussie. Faisons cela maintenant.

Si vous vous souvenez, nous avons ajouté une fonction `resetUser` à l'intérieur du composant `AppRouter` pour effacer les données de l'état `user`.

Passons cette fonction en tant que prop au composant `ThirdStep`. Ainsi, votre route `ThirdStep` ressemblera à ceci :

```js
<Route
  render={(props) => (
    <ThirdStep
      {...props}
      user={user}
      updateUser={updateUser}
      resetUser={resetUser}
    />
  )}
  path="/third"
/>

```

Et à l'intérieur de la fonction `handleSubmit` du fichier `ThirdStep.js`, avant d'appeler `props.history.push('/');`, appelez la fonction `resetUser` comme ceci :

```js
Swal.fire('Super !', "Vous êtes inscrit avec succès !", 'success').then(
  (result) => {
    if (result.isConfirmed || result.isDismissed) {
      props.resetUser();
      props.history.push('/');
    }
  }
);

```

Maintenant, si vous inscrivez un nouvel utilisateur, vous verrez qu'après l'inscription, vous serez redirigé vers l'étape 1 et tous les champs de saisie seront également effacés.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/cleared_fields.gif)

## Comment ajouter une fonctionnalité de connexion à l'application

Nous avons ajouté toute la fonctionnalité d'inscription pour le front-end et le back-end. Ajoutons une fonctionnalité de connexion afin que nous puissions vérifier si un utilisateur avec un email et un mot de passe fournis existe déjà et ensuite récupérer les détails de cet utilisateur.

Ouvrez le fichier `routers/user.js` et ajoutez le code suivant à l'intérieur avant l'instruction `module.exports` :

```js
router.post('/login', async (req, res) => {
  try {
    const user = await User.findOne({ user_email: req.body.user_email });
    if (!user) {
      return res.status(400).send('L\'utilisateur avec l\'email fourni n\'existe pas.');
    }

    const isMatch = await bcrypt.compare(
      req.body.user_password,
      user.user_password
    );

    if (!isMatch) {
      return res.status(400).send('Identifiants invalides.');
    }
    const { user_password, ...rest } = user.toObject();

    return res.send(rest);
  } catch (error) {
    return res.status(500).send('Quelque chose s\'est mal passé. Veuillez réessayer plus tard.');
  }
});

```

Ici, nous vérifions d'abord si l'utilisateur avec l'email fourni existe déjà en utilisant la méthode `findOne`. Si aucun utilisateur n'existe, alors nous renvoyons une erreur avec un code d'état `400`.

Si un utilisateur avec l'adresse email fournie existe, alors nous utilisons la méthode `bcrypt.compare` pour comparer le mot de passe original non haché avec le mot de passe haché. Si le mot de passe haché ne correspond pas au mot de passe de l'objet `user`, alors nous renvoyons une erreur disant `Identifiants invalides`.

Mais si le mot de passe correspond, alors nous créons un nouvel objet `rest` avec toutes les propriétés de `user` sauf le mot de passe haché en utilisant l'opérateur de repos ES9 pour les objets :

```js
const { user_password, ...rest } = user.toObject();

```

Cela est dû au fait que nous ne voulons pas renvoyer le mot de passe haché pour des raisons de sécurité.

Ensuite, nous renvoyons l'objet `rest` avec le mot de passe supprimé à l'application cliente (notre application React).

Maintenant que nous avons créé l'API backend, intégrons la partie frontend pour notre fonctionnalité de connexion.

Créez un nouveau fichier appelé `Login.js` à l'intérieur du dossier `components` avec le code suivant :

```jsx
import React, { useState } from 'react';
import { useForm } from 'react-hook-form';
import { Form, Button } from 'react-bootstrap';
import axios from 'axios';
import { BASE_API_URL } from '../utils/constants';

const Login = () => {
  const { register, handleSubmit, errors } = useForm();
  const [successMessage, setSuccessMessage] = useState('');
  const [errorMessage, setErrorMessage] = useState('');
  const [userDetails, setUserDetails] = useState('');

  const onSubmit = async (data) => {
    console.log(data);

    try {
      const response = await axios.post(`${BASE_API_URL}/login`, data);
      setSuccessMessage('Utilisateur avec les identifiants fournis trouvé.');
      setErrorMessage('');
      setUserDetails(response.data);
    } catch (error) {
      console.log(error);
      if (error.response) {
        console.log('error', error.response.data);
        setErrorMessage(error.response.data);
      }
    }
  };

  return (
    <Form className="input-form" onSubmit={handleSubmit(onSubmit)}>
      <div className="col-md-6 offset-md-3">
        {errorMessage ? (
          <p className="errorMsg login-error">{errorMessage}</p>
        ) : (
          <div>
            <p className="successMsg">{successMessage}</p>

            {userDetails && (
              <div className="user-details">
                <p>Voici les détails de l'utilisateur :</p>
                <div>Prénom : {userDetails.first_name}</div>
                <div>Nom : {userDetails.last_name}</div>
                <div>Email : {userDetails.user_email}</div>
                <div>Pays : {userDetails.country}</div>
                <div>État : {userDetails.state}</div>
                <div>Ville : {userDetails.city}</div>
              </div>
            )}
          </div>
        )}
        <Form.Group controlId="first_name">
          <Form.Label>Email</Form.Label>
          <Form.Control
            type="email"
            name="user_email"
            placeholder="Entrez votre adresse email"
            ref={register({
              required: 'L\'email est requis.',
              pattern: {
                value: /^[^@ ]+@[^@ ]+\.[^@ .]{2,}$/,
                message: 'L\'email n\'est pas valide.'
              }
            })}
            className={`${errors.user_email ? 'input-error' : ''}`}
          />
          {errors.user_email && (
            <p className="errorMsg">{errors.user_email.message}</p>
          )}
        </Form.Group>

        <Form.Group controlId="password">
          <Form.Label>Mot de passe</Form.Label>
          <Form.Control
            type="password"
            name="user_password"
            placeholder="Choisissez un mot de passe"
            ref={register({
              required: 'Le mot de passe est requis.',
              minLength: {
                value: 6,
                message: 'Le mot de passe doit contenir au moins 6 caractères.'
              }
            })}
            className={`${errors.user_password ? 'input-error' : ''}`}
          />
          {errors.user_password && (
            <p className="errorMsg">{errors.user_password.message}</p>
          )}
        </Form.Group>

        <Button variant="primary" type="submit">
          Vérifier la connexion
        </Button>
      </div>
    </Form>
  );
};

export default Login;

```

Maintenant, ouvrez le fichier `AppRouter.js` et ajoutez une route pour Login à la fin de toutes les routes avant la balise de fermeture `Switch` comme ceci :

```jsx
<BrowserRouter>
     ...
    <Route component={Login} path="/login" />
    </Switch>
  </div>
</BrowserRouter>

```

Incluez également le composant `Login` en haut :

```js
import Login from '../components/Login';

```

Maintenant, si vous accédez à [http://localhost:3000/login](http://localhost:3000/login), vous verrez l'écran suivant :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/login_screen.png)

Ici, nous n'avons pas vraiment besoin d'afficher les étapes dans l'en-tête, alors ajoutons une condition pour les masquer sur la page de connexion.

Ouvrez le fichier `Progress.js` et ajoutez une autre variable const comme ceci :

```js
const isLoginPage = pathname === '/login';

```

Ensuite, ajoutez une condition d'opérateur ternaire avant le début de la div avec la classe `steps` :

```jsx
<React.Fragment>
  {!isLoginPage ? (
    <div className="steps">
     ...
    </div>
  ) : (
    <div></div>
  )}
</React.Fragment>

```

Si la page n'est pas une page de connexion, alors nous afficherons les étapes – sinon nous afficherons une div vide.

Notez que nous devons rendre une div vide si nous n'avons rien à rendre, car React lancera une erreur si nous ne retournons aucun JSX depuis le composant.

Votre fichier `Progress.js` complet ressemblera à ceci maintenant :

```jsx
import React from 'react';
import { Link, withRouter } from 'react-router-dom';

const Progress = ({ location: { pathname } }) => {
  const isFirstStep = pathname === '/';
  const isSecondStep = pathname === '/second';
  const isThirdStep = pathname === '/third';
  const isLoginPage = pathname === '/login';

  return (
    <React.Fragment>
      {!isLoginPage ? (
        <div className="steps">
          <div className={`${isFirstStep ? 'step active' : 'step'}`}>
            <div>1</div>
            <div>
              {isSecondStep || isThirdStep ? (
                <Link to="/">Étape 1</Link>
              ) : (
                'Étape 1'
              )}
            </div>
          </div>
          <div className={`${isSecondStep ? 'step active' : 'step'}`}>
            <div>2</div>
            <div>
              {isThirdStep ? <Link to="/second">Étape 2</Link> : 'Étape 2'}
            </div>
          </div>
          <div className={`${pathname === '/third' ? 'step active' : 'step'}`}>
            <div>3</div>
            <div>Étape 3</div>
          </div>
        </div>
      ) : (
        <div></div>
      )}
    </React.Fragment>
  );
};

export default withRouter(Progress);

```

## Comment tester la fonctionnalité de connexion

Maintenant, si vous vérifiez la page de connexion, vous verrez la page sans les étapes dans l'en-tête. Mais les étapes sont toujours affichées pour les autres pages.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/login_without_steps.png)

Et si vous entrez les bonnes informations de connexion, vous obtiendrez les détails liés à cet utilisateur comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/login_success_message.gif)

Si les informations de connexion sont invalides, vous verrez le message d'erreur comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/invalid_login.gif)

Si l'email existe mais que le mot de passe ne correspond pas, vous verrez le message d'erreur comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/invalid_credentials.gif)

Maintenant, comprenons le code du fichier `Login.js` :

```js
const onSubmit = async (data) => {
  console.log(data);

  try {
    const response = await axios.post(`${BASE_API_URL}/login`, data);
    setSuccessMessage('Utilisateur avec les identifiants fournis trouvé.');
    setErrorMessage('');
    setUserDetails(response.data);
  } catch (error) {
    console.log(error);
    if (error.response) {
      console.log('error', error.response.data);
      setErrorMessage(error.response.data);
    }
  }
};

```

Dans la fonction `onSubmit`, nous faisons un appel API à l'endpoint `/login` en passant les données saisies dans le formulaire de connexion.

Si aucune erreur n'est présente dans la réponse de l'API, nous définissons l'état `successMessage` et définissons l'état `userDetails` avec la réponse de l'API. Sinon, nous définissons l'état `errorMessage`.

Et dans le JSX, si l'état `errorMessage` n'est pas vide, nous affichons le message d'erreur, sinon nous affichons la valeur de l'état `successMessage` avec les données `userDetails` :

```jsx
{errorMessage ? (
  <p className="errorMsg login-error">{errorMessage}</p>
) : (
  <div>
    <p className="successMsg">{successMessage}</p>

    {userDetails && (
      <div className="user-details">
        <p>Voici les détails de l'utilisateur :</p>
        <div>Prénom : {userDetails.first_name}</div>
        <div>Nom : {userDetails.last_name}</div>
        <div>Email : {userDetails.user_email}</div>
        <div>Pays : {userDetails.country}</div>
        <div>État : {userDetails.state}</div>
        <div>Ville : {userDetails.city}</div>
      </div>
    )}
  </div>
)}

```

Notez que nous n'avons pas fourni de lien pour la page de connexion à l'écran car l'application est destinée à afficher la fonctionnalité de formulaire multi-étapes. J'ai inclus la page de connexion afin que vous puissiez avoir une idée de la manière de valider la connexion de l'utilisateur.

Si vous le souhaitez, vous pouvez inclure le lien de la page de connexion dans l'en-tête ou y accéder directement en utilisant [http://localhost:3000/login](http://localhost:3000/login).

## Comment configurer une page de route invalide

Maintenant, nous avons terminé toute la fonctionnalité de l'application. Ajoutons un peu de code afin que si nous entrons une route invalide dans l'URL du navigateur, l'utilisateur soit redirigé vers la page d'accueil.

Actuellement, si vous accédez à une route invalide comme [http://localhost:3000/contact](http://localhost:3000/contact), vous verrez une page blanche. Mais il n'y a également aucune erreur dans la console car il n'y a aucune route correspondante dans la liste des routes à l'intérieur du fichier `AppRouter.js`.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/blank_page-1.gif)

Ouvrez le fichier `AppRouter.js`, et après la route de connexion, entrez une autre route comme montré ci-dessous :

```jsx
  ...
  <Route component={Login} path="/login" />
  <Route render={() => <Redirect to="/" />} />
</Switch>

```

Ici, nous n'avons pas fourni de chemin à la composante `Route` pour la dernière Route. Cela signifie que si aucune des routes ci-dessus ne correspond, cette dernière Route sera exécutée. Cela redirigera l'utilisateur vers la route `/` qui est la route du composant `FirstPage`.

De plus, importez le composant `Redirect` de `react-router-dom` en haut du fichier :

```js
import { BrowserRouter, Redirect, Route, Switch } from 'react-router-dom';

```

Notez que vous devez l'entrer uniquement comme dernière route. De cette manière, si aucune des routes ci-dessus ne correspond, la dernière route sera exécutée et elle redirigera vers la page d'accueil.

Vérifions cela maintenant.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/page_not_found.gif)

Comme vous pouvez le voir, pour toutes les routes invalides, nous sommes redirigés vers la page d'accueil qui est la page de la première étape.

## Comment se débarrasser de la bibliothèque CORS

Comme vous le savez, pour exécuter cette application, nous devons démarrer notre application React en utilisant la commande `yarn start` dans un terminal. Nous devons également exécuter la commande `yarn start` depuis le dossier `server` pour le serveur backend. Et enfin, nous devons également garder notre serveur MongoDB en cours d'exécution dans le troisième terminal.

Alors, supprimons le besoin d'exécuter deux commandes `yarn start` séparées. Cela vous permettra également de déployer votre application sur un seul fournisseur d'hébergement.

Si vous vous souvenez, dans le fichier `server/index.js`, nous avons ajouté le code suivant :

```js
app.use(cors());

```

L'ajout de ce code permet à toute application d'accéder à nos API – ce qui est bien lorsque l'on travaille dans un environnement local. Mais ce n'est pas sûr de permettre à tout le monde d'accéder à nos API. Alors, corrigeons cela.

Ouvrez le fichier `server/index.js` et ajoutez le code ci-dessous juste au-dessus de la ligne `app.use(express.json());` :

```js
app.use(express.static(path.join(__dirname, '..', 'build')));

```

Ici, nous configurons notre application Express pour utiliser le contenu du dossier `build` comme point de départ de notre application.

Le dossier `build` sera créé lorsque nous exécuterons la commande `yarn build` pour notre application React.

Comme le dossier `build` sera créé à l'extérieur du dossier `server`, nous utilisons `..` pour sortir du dossier `server` afin d'y accéder.

De plus, importez le package Node `path` en haut du fichier :

```js
const path = require('path'); 

```

Nous n'avons pas besoin d'installer le package npm `path`, car il est ajouté par défaut lorsque nous installons Node.js sur notre système.

Maintenant, vous pouvez supprimer l'import `cors` et son utilisation du fichier `server/index.js`.

Votre fichier final `server/index.js` ressemblera à ceci :

```js
const path = require('path');
const express = require('express');
const userRouter = require('./routers/user');
require('./db');

const app = express();
const PORT = process.env.PORT || 3030;

app.use(express.static(path.join(__dirname, '..', 'build')));
app.use(express.json());
app.use(userRouter);

app.get('/', (req, res) => {
 res.send('<h2>Ceci provient du fichier index.js</h2>');
});

app.listen(PORT, () => {
 console.log(`serveur démarré sur le port ${PORT}`);
});

```

Maintenant, arrêtez les deux commandes `yarn start` des deux terminaux. Ensuite, dans un seul terminal, exécutez la commande `yarn build` depuis l'intérieur du dossier `multi-step-form-using-mern` qui est notre dossier de projet.

La commande `yarn build` prendra un certain temps pour se compléter car elle effectue certaines optimisations. Elle ne doit être exécutée que lorsque nous avons terminé toute la fonctionnalité de l'application et que nous sommes prêts à déployer l'application en production.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/build_completed.png)

Une fois la commande terminée avec succès, vous verrez un dossier `build` créé comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/file_structure.png)

Le dossier `build` contient toute notre application React, donc vous pouvez utiliser ce dossier `build` pour déployer votre application en production.

Maintenant, ouvrez le fichier `src/utils/constants.js` et remplacez ce code :

```js
export const BASE_API_URL = 'http://localhost:3030';

```

par le code ci-dessous :

```js
export const BASE_API_URL = '';

```

Maintenant, comme nous avons créé le dossier `build`, naviguez jusqu'au dossier `server` depuis le terminal et exécutez la commande `yarn start` :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/server_started.gif)

Comme vous pouvez le voir, le serveur a démarré sur le port `3030`. 

Alors, accédons à notre application à l'adresse [http://localhost:3030/](http://localhost:3030/).

![Image](https://www.freecodecamp.org/news/content/images/2021/03/complete_flow.gif)

Comme vous pouvez le voir, nous avons seulement besoin d'exécuter une commande `yarn start` pour démarrer le serveur Express Node.js. Le serveur Node.js rend notre application React sur le port `3030` depuis le dossier `build`. 

Ainsi, toutes nos API sont maintenant disponibles sur `http://localhost:3030` telles que `http://localhost:3030/register` et `http://localhost:3030/login`.

Par conséquent, nous avons changé la valeur `BASE_API_URL` pour une simple chaîne vide :

```js
export const BASE_API_URL = '';

```

Lorsque nous sommes déjà sur `http://localhost:3030`, nous pouvons faire toutes nos requêtes API POST en utilisant simplement `/login` et `/register`.

Ainsi, nous avons seulement besoin d'un terminal pour exécuter la commande `yarn start` et un autre terminal pour démarrer le service MongoDB. Cela signifie que nous pouvons déployer notre application sur un seul fournisseur d'hébergement comme [heroku](https://www.heroku.com/) au lieu de déployer l'application React sur un fournisseur d'hébergement et l'application Node.js sur un autre fournisseur d'hébergement.

Notez que si vous apportez des modifications au code de l'application React, vous devrez réexécuter la commande `yarn build` depuis le dossier du projet, puis la commande `yarn start` depuis le dossier `server`.

Mais il y a un problème avec cette configuration. Si vous allez directement à une route autre que la route `/` comme `/first`, `/second`, `/login` et ainsi de suite, vous obtiendrez une erreur comme vous le verrez ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/error.gif)

Cela est dû au fait que nous démarrons le serveur depuis Express.js, donc la requête ira toujours au serveur Express (notre serveur Node a été créé en utilisant Express) et il n'y a pas de route `/second` pour gérer cela côté Node. Donc, il nous donne une erreur.

Pour corriger cela, ouvrez le fichier `server/index.js` et ajoutez le code suivant avant l'instruction `app.listen` et après toutes les autres routes :

```js
app.use((req, res, next) => {
  res.sendFile(path.join(__dirname, '..', 'build', 'index.html'));
});

```

Ce code agira comme une route par défaut. Si aucune des routes précédentes ne correspond, ce code renverra le fichier `index.html` du dossier `build` qui est notre application React.

Et parce que la route `/second` est présente dans notre application React, vous verrez la page correcte de l'étape 2.

Si la route saisie n'est pas présente dans l'application Node.js ainsi que dans notre application React, alors l'utilisateur sera redirigé vers la page de l'étape 1 (notre page d'accueil) en raison de notre dernière route dans le fichier `AppRouter.js`.

```js
<Route render={() => <Redirect to="/" />} />

```

À ce stade, votre fichier `server/index.js` complet ressemblera à ceci :

```js
const path = require('path');
const express = require('express');
const userRouter = require('./routers/user');
require('./db');

const app = express();
const PORT = process.env.PORT || 3030;

app.use(express.static(path.join(__dirname, '..', 'build')));
app.use(express.json());
app.use(userRouter);

app.get('/', (req, res) => {
  res.send('<h2>Ceci provient du fichier index.js</h2>');
});

app.use((req, res, next) => {
  res.sendFile(path.join(__dirname, '..', 'build', 'index.html'));
});

app.listen(PORT, () => {
  console.log(`serveur démarré sur le port ${PORT}`);
});

```

Et vous n'obtiendrez plus d'erreur maintenant :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/error_fixed.gif)

Si vous souhaitez apprendre en profondeur comment rendre les applications React en utilisant Node.js, consultez [cet article](https://levelup.gitconnected.com/how-to-render-react-app-using-express-server-in-node-js-a428ec4dfe2b?source=friends_link&sk=3f152ac7908f540b209f07f683b494cd).

Maintenant, nous avons terminé avec la fonctionnalité front-end et back-end comme vous pouvez le voir ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/complete_working_app.gif)

## **Points de conclusion**

Nous avons terminé la construction de la fonctionnalité de l'application.

**Vous pouvez trouver le code source complet de cette application sur GitHub dans [ce dépôt](https://github.com/myogeshchavan97/multi-step-form-using-mern).**

Pour améliorer vos compétences, vous pouvez améliorer l'application en ajoutant une validation supplémentaire à l'étape 3 pour vérifier si l'utilisateur a saisi tous les détails dans le formulaire. Cela est important car vous pouvez accéder directement à la page de la deuxième étape du formulaire en utilisant [http://localhost:3030/second](http://localhost:3030/second) et continuer à partir de là.

### Merci d'avoir lu !

Vous souhaitez apprendre toutes les fonctionnalités ES6+ en détail, y compris let et const, les promesses, diverses méthodes de promesses, la déstructuration de tableaux et d'objets, les fonctions fléchées, async/await, import et export, et bien plus encore, depuis le début ?

Consultez mon livre [Mastering Modern JavaScript](https://modernjavascript.yogeshchavan.dev/). Ce livre couvre tous les prérequis pour apprendre React et vous aide à devenir meilleur en JavaScript et React.

De plus, vous pouvez consulter mon cours gratuit [Introduction à React Router](https://yogeshchavan1.podia.com/react-router-introduction) pour apprendre React Router depuis le début.

Vous souhaitez rester à jour avec du contenu régulier concernant JavaScript, React et Node.js ? [Suivez-moi sur LinkedIn](https://www.linkedin.com/in/yogesh-chavan97/).