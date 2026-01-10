---
title: Comment créer des formulaires dans React avec la bibliothèque react-hook-form
subtitle: ''
author: Yogesh Chavan
co_authors: []
series: null
date: '2020-11-02T23:44:40.000Z'
originalURL: https://freecodecamp.org/news/build-forms-in-react-with-react-hook-form-library
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9d9bdd49c47664ed817585.jpg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: Comment créer des formulaires dans React avec la bibliothèque react-hook-form
seo_desc: 'In this article, we will explore the react-hook-form library.

  You will learn how to use and integrate this library with React. We''ll also see
  why it''s becoming a popular choice for building both simple and complex forms with
  added support for handlin...'
---

Dans cet article, nous allons explorer la bibliothèque [react-hook-form](https://react-hook-form.com/).

Vous apprendrez comment utiliser et intégrer cette bibliothèque avec React. Nous verrons également pourquoi elle devient un choix populaire pour créer des formulaires simples et complexes avec un support ajouté pour la gestion des validations complexes.

### Commençons

Travailler avec des formulaires dans React est une tâche complexe. Et cela devient encore plus complexe lorsque le nombre de champs d'entrée augmente avec les validations.

Jetez un œil au code ci-dessous :

```js

import React, { useState } from "react";
import "./styles.css";

export default function App() {
  const [state, setState] = useState({
    email: "",
    password: ""
  });

  const handleInputChange = (event) => {
    setState((prevProps) => ({
      ...prevProps,
      [event.target.name]: event.target.value
    }));
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log(state);
  };

  return (
    <div className="App">
      <form onSubmit={handleSubmit}>
        <div className="form-control">
          <label>Email</label>
          <input
            type="text"
            name="email"
            value={state.email}
            onChange={handleInputChange}
          />
        </div>
        <div className="form-control">
          <label>Mot de passe</label>
          <input
            type="password"
            name="password"
            value={state.password}
            onChange={handleInputChange}
          />
        </div>
        <div className="form-control">
          <label></label>
          <button type="submit">Connexion</button>
        </div>
      </form>
    </div>
  );
}
```

Voici une démonstration sur Code Sandbox : [https://codesandbox.io/s/login-form-zjxs9](https://codesandbox.io/s/login-form-zjxs9).

Dans le code ci-dessus, nous n'avons que 2 champs de saisie, à savoir `email` et `password`, et un bouton de soumission.

Chaque champ de saisie a une valeur `value` et un gestionnaire `onChange` ajouté afin que nous puissions mettre à jour l'état en fonction de la saisie de l'utilisateur.

De plus, nous avons ajouté une méthode `handleSubmit` qui affiche les données saisies dans le formulaire dans la console.

Cela semble bien. Mais que se passe-t-il si nous devons ajouter des validations comme la validation de champ obligatoire, la validation de longueur minimale, la validation de mot de passe, la validation de champ email et également afficher les messages d'erreur correspondants ?

Le code deviendra plus complexe et long à mesure que le nombre de champs de saisie et leurs validations augmentent.

C'est une exigence très courante dans toute application. Donc, pour travailler facilement avec les formulaires, il existe diverses bibliothèques disponibles comme `Formik`, `redux-form`, `react-final-form`, `react-hook-form` et ainsi de suite.

Mais celle qui gagne en popularité est la bibliothèque `react-hook-form`.

Alors, apprenons maintenant pourquoi et comment l'utiliser. Pour cela, nous allons créer une nouvelle application React.

Créez un nouveau projet React en exécutant la commande suivante depuis le terminal :

```js
npx create-react-app react-hook-form-demo
```

Une fois le projet créé, supprimez tous les fichiers du dossier `src` et créez de nouveaux fichiers `index.js` et `styles.css` à l'intérieur du dossier `src`.

Pour installer la bibliothèque de formulaires, exécutez la commande suivante depuis le terminal :

```js
yarn add react-hook-form
```

## Comment créer des pages initiales

Ouvrez le fichier `src/index.js` et ajoutez le contenu suivant à l'intérieur :

```js

import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(<App />, document.getElementById('root'));
```

Ouvrez le fichier `src/styles.css` et ajoutez le contenu depuis [ici](https://github.com/myogeshchavan97/react-hook-form-demo/blob/master/src/styles.css) à l'intérieur.

Maintenant, créez un nouveau fichier `App.js` à l'intérieur du dossier `src` avec le contenu suivant :

```js

import React from "react";
import "./styles.css";

export default function App() {
  return (
    <div className="App">
      <form>
        <div className="form-control">
          <label>Email</label>
          <input type="text" name="email" />
        </div>
        <div className="form-control">
          <label>Mot de passe</label>
          <input type="password" name="password" />
        </div>
        <div className="form-control">
          <label></label>
          <button type="submit">Connexion</button>
        </div>
      </form>
    </div>
  );
}
```

Ici, nous avons simplement ajouté les champs email et mot de passe au formulaire.

## Création de formulaire de base avec react-hook-form

La bibliothèque `react-hook-form` fournit un hook `useForm` que nous pouvons utiliser pour travailler avec des formulaires.

Importez le hook `useForm` comme ceci :

```js
import { useForm } from 'react-hook-form';
```

Utilisez le hook `useForm` comme ceci :

```js
const { register, handleSubmit, errors } = useForm();
```

Ici,

* register est une fonction à utiliser comme ref fournie par le hook `useForm`. Nous pouvons l'assigner à chaque champ de saisie afin que `react-hook-form` puisse suivre les changements de la valeur du champ de saisie.
* handleSubmit est la fonction que nous pouvons appeler lorsque le formulaire est soumis
* errors contiendra les erreurs de validation, le cas échéant

Maintenant, remplacez le contenu du fichier `App.js` par le contenu suivant :

```js

import React from "react";
import { useForm } from "react-hook-form";
import "./styles.css";

export default function App() {
  const { register, handleSubmit, errors } = useForm();

  const onSubmit = (data) => {
    console.log(data);
  };

  return (
    <div className="App">
      <form onSubmit={handleSubmit(onSubmit)}>
        <div className="form-control">
          <label>Email</label>
          <input type="text" name="email" ref={register} />
        </div>
        <div className="form-control">
          <label>Mot de passe</label>
          <input type="password" name="password" ref={register} />
        </div>
        <div className="form-control">
          <label></label>
          <button type="submit">Connexion</button>
        </div>
      </form>
    </div>
  );
}
```

Dans le code ci-dessus, nous avons donné une ref à chaque champ de saisie que nous avons obtenu du hook `useForm`.

```js
ref={register}
```

De plus, nous avons ajouté la fonction onSubmit qui est passée à la fonction handleSubmit.

```js
<form onSubmit={handleSubmit(onSubmit)}>
```

Notez que pour chaque champ de saisie, nous avons donné un nom unique qui est obligatoire afin que `react-hook-form` puisse suivre les données changeantes.

Lorsque nous soumettons le formulaire, la fonction handleSubmit gérera la soumission du formulaire. Elle enverra les données saisies par l'utilisateur à la fonction onSubmit que nous enregistrons dans la console.

```js
const onSubmit = (data) => {  
 console.log(data);
};
```

Maintenant, démarrez l'application en exécutant la commande `yarn start`.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/initial_app.gif)

Comme vous pouvez le voir, lorsque nous soumettons le formulaire, les détails saisis par l'utilisateur sont affichés dans la console.

De plus, par rapport au code sans `react-hook-form` (que nous avons vu au début de cet article), ce code est beaucoup plus simple. Cela est dû au fait que nous n'avons pas à ajouter le gestionnaire `value` et `onChange` pour chaque champ de saisie et qu'il n'est pas nécessaire de gérer l'état de l'application nous-mêmes.

## Comment ajouter des validations au formulaire

Maintenant, ajoutons la validation de champ obligatoire et de longueur minimale aux champs de saisie.

Pour ajouter une validation, nous pouvons la passer à la fonction register qui est passée en tant que ref à chaque champ de saisie comme ceci :

```js

<input type="text" name="email" ref={register({ required: true})} />
<input
  type="password"
  name="password"
  ref={register({ required: true, minLength: 6 })}
/>
```

Nous voulons également afficher le message d'erreur si la validation échoue.

Lorsque la validation échoue, l'objet errors provenant de `useForm` sera rempli avec les champs pour lesquels la validation a échoué.

Ouvrez le fichier `App.js` et remplacez son contenu par le contenu suivant :

```js

import React from "react";
import { useForm } from "react-hook-form";
import "./styles.css";

export default function App() {
  const { register, handleSubmit, errors } = useForm();

  const onSubmit = (data) => {
    console.log(data);
  };

  return (
    <div className="App">
      <form onSubmit={handleSubmit(onSubmit)}>
        <div className="form-control ">
          <label>Email</label>
          <input
            type="text"
            name="email"
            ref={register({
              required: true,
              pattern: /^[^@ ]+@[^@ ]+\.[^@ .]{2,}$/
            })}
          />
          {errors.email && errors.email.type === "required" && (
            <p className="errorMsg">L'email est obligatoire.</p>
          )}
          {errors.email && errors.email.type === "pattern" && (
            <p className="errorMsg">L'email n'est pas valide.</p>
          )}
        </div>
        <div className="form-control">
          <label>Mot de passe</label>
          <input
            type="password"
            name="password"
            ref={register({ required: true, minLength: 6 })}
          />
          {errors.password && errors.password.type === "required" && (
            <p className="errorMsg">Le mot de passe est obligatoire.</p>
          )}
          {errors.password && errors.password.type === "minLength" && (
            <p className="errorMsg">
              Le mot de passe doit comporter au moins 6 caractères.
            </p>
          )}
        </div>
        <div className="form-control">
          <label></label>
          <button type="submit">Connexion</button>
        </div>
      </form>
    </div>
  );
}
```



![Image](https://www.freecodecamp.org/news/content/images/2020/11/initial_validation.gif)

Ici, pour le champ de saisie email, nous avons fourni les validations de champ obligatoire et de correspondance de motif.

```js
<input
    type="text"
    name="email"
    ref={register({
      required: true,
      pattern: /^[^@ ]+@[^@ ]+\.[^@ .]{2,}$/
    })}
  />
```

Ainsi, lorsque vous tapez dans le champ de saisie email, la validation s'exécutera une fois le formulaire soumis.

Si la validation échoue, alors le champ `errors.email` à l'intérieur de l'objet errors sera rempli avec le champ type que nous avons utilisé pour afficher le message d'erreur.

```js

{errors.email && errors.email.type === "required" && (
  <p className="errorMsg">L'email est obligatoire.</p>
)}
```

De manière similaire, nous avons ajouté la validation du champ mot de passe.

Ainsi, comme vous pouvez le voir, chaque champ de saisie est automatiquement mis en focus s'il y a une erreur de validation pour ce champ de saisie lorsque nous soumettons le formulaire.

De plus, le formulaire n'est pas soumis tant qu'il y a une erreur de validation. Vous pouvez voir que l'instruction `console.log` n'est imprimée que si le formulaire est valide.

Ainsi, l'utilisation de `react-hook-form` a réduit la quantité de code que nous devons écrire. La validation est également réactive, donc une fois que le champ devient valide, le message d'erreur disparaît instantanément.

Mais à mesure que le nombre de validations pour chaque champ augmente, les vérifications conditionnelles et le code des messages d'erreur augmenteront encore. Nous pouvons donc encore refactoriser le code pour le rendre encore plus simple.

Jetez un œil au code ci-dessous :

```js

import React from 'react';
import { useForm } from 'react-hook-form';
import './styles.css';

export default function App() {
  const { register, handleSubmit, errors } = useForm();

  const onSubmit = (data) => {
    console.log(data);
  };

  return (
    <div className="App">
      <form onSubmit={handleSubmit(onSubmit)}>
        <div className="form-control ">
          <label>Email</label>
          <input
            type="text"
            name="email"
            ref={register({
              required: 'L\'email est obligatoire.',
              pattern: {
                value: /^[^@ ]+@[^@ ]+\.[^@ .]{2,}$/,
                message: 'L\'email n\'est pas valide.'
              }
            })}
          />
          {errors.email && <p className="errorMsg">{errors.email.message}</p>}
        </div>
        <div className="form-control">
          <label>Mot de passe</label>
          <input
            type="password"
            name="password"
            ref={register({
              required: 'Le mot de passe est obligatoire.',
              minLength: {
                value: 6,
                message: 'Le mot de passe doit comporter au moins 6 caractères.'
              }
            })}
          />
          {errors.password && (
            <p className="errorMsg">{errors.password.message}</p>
          )}
        </div>
        <div className="form-control">
          <label></label>
          <button type="submit">Connexion</button>
        </div>
      </form>
    </div>
  );
}
```

Dans le code ci-dessus, nous avons modifié le code de validation de l'email et du mot de passe.

Pour le champ de saisie email, nous avons changé ce code précédent :

```js

<input
  type="text"
  name="email"
  ref={register({
    required: true,
    pattern: /^[^@ ]+@[^@ ]+\.[^@ .]{2,}$/
  })}
/>
```

en ce nouveau code :

```js

<input
  type="text"
  name="email"
  ref={register({
    required: 'L\'email est obligatoire.',
    pattern: {
      value: /^[^@ ]+@[^@ ]+\.[^@ .]{2,}$/,
      message: 'L\'email n\'est pas valide.'
    }
  })}
/>
```

Ici, nous avons directement fourni le message d'erreur que nous voulons afficher lors de l'ajout de la validation elle-même.

Ainsi, nous n'avons plus besoin d'ajouter des vérifications supplémentaires pour chaque validation. Nous affichons le message d'erreur en utilisant la propriété message disponible à l'intérieur de l'objet errors pour chaque champ de saisie.

```js
{errors.email && <p className="errorMsg">{errors.email.message}</p>}
```

Ainsi, en procédant de cette manière, le code est encore simplifié, ce qui facilite l'ajout de validations supplémentaires à l'avenir.

Notez que si des erreurs de validation existent, le gestionnaire onSubmit ne sera pas exécuté et le champ de saisie correspondant sera automatiquement mis en focus (ce qui est une bonne chose).

## Comment ajouter une méthode de validation personnalisée

Vous pouvez même fournir une validation personnalisée pour le champ de saisie en ajoutant une méthode `validate`. Cela est utile si vous devez effectuer des validations complexes comme ceci :

```js
// fonction de validation
const validatePassword = (value) => {
  if (value.length < 6) {
    return 'Le mot de passe doit comporter au moins 6 caractères.';
  } else if (
    !/(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?!.*\s)(?=.*[!@#$*])/.test(value)
  ) {
    return 'Le mot de passe doit contenir au moins une lettre majuscule, une lettre minuscule, un chiffre et un symbole spécial.';
  }
  return true;
};

// JSX
<input
  type="password"
  name="password"
  ref={register({
    required: 'Le mot de passe est obligatoire.',
    validate: validatePassword
  })}
/>
```

![Image](https://www.freecodecamp.org/news/content/images/2020/11/custom_validation.gif)

Maintenant, vous savez comment utiliser `react-hook-form` pour créer des formulaires dans React avec des validations complexes.

## Pourquoi react-hook-form est meilleur que les alternatives

Examinons quelques raisons supplémentaires pour lesquelles `react-hook-form` devrait devenir votre choix préféré pour travailler avec des formulaires.

* La complexité du code est moindre par rapport à `formik`, `redux-form` et autres alternatives.
* `react-hook-form` s'intègre bien avec la bibliothèque `yup` pour la validation de schéma afin que vous puissiez combiner vos propres schémas de validation.
* Le nombre de re-rendus dans l'application est faible par rapport aux alternatives.
* Le temps de montage est inférieur par rapport aux alternatives.

Pour les métriques de comparaison réelles, [lisez plus ici.](https://react-hook-form.com/)

## Conclusion

Dans cet article, nous avons vu comment utiliser `react-hook-form` et pourquoi c'est le choix préféré de nombreux développeurs pour créer des formulaires simples et complexes dans React.

Vous pouvez trouver le code source GitHub de cette application [ici](https://github.com/myogeshchavan97/react-hook-form-demo).

Si vous avez aimé cet article, alors vous aimerez aussi mes autres articles.

Abonnez-vous à ma [newsletter hebdomadaire](https://bit.ly/2HwVEA2) pour rejoindre plus de 1000 autres abonnés et recevoir des conseils, astuces et articles incroyables directement dans votre boîte de réception.