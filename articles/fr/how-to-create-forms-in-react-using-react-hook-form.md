---
title: Comment créer des formulaires dans React en utilisant react-hook-form
subtitle: ''
author: Yogesh Chavan
co_authors: []
series: null
date: '2022-10-27T19:47:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-forms-in-react-using-react-hook-form
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/cover.jpg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: Comment créer des formulaires dans React en utilisant react-hook-form
seo_desc: 'Creating forms in React is a complex task. It involves handling all the
  input states and their changes and validating that input when the form gets submitted.

  For simple forms, things are generally manageable. But as your form gets more complex
  and y...'
---

Créer des formulaires dans React est une tâche complexe. Cela implique de gérer tous les états des entrées et leurs changements, ainsi que de valider ces entrées lorsque le formulaire est soumis.

Pour les formulaires simples, les choses sont généralement gérables. Mais à mesure que votre formulaire devient plus complexe et que vous devez ajouter diverses validations, cela devient une tâche compliquée.

Ainsi, au lieu d'écrire manuellement tout le code et de gérer des formulaires complexes avec une logique de validation, nous pouvons utiliser la bibliothèque React la plus populaire pour cela, [react-hook-form](https://react-hook-form.com/).

C'est la bibliothèque React la plus populaire pour créer des formulaires par rapport à [formik](https://formik.org/), [react final form](https://final-form.org/react/), et autres, et je l'utilise pour tous mes projets clients.

Dans cet article, nous allons explorer comment utiliser la bibliothèque [react-hook-form](https://react-hook-form.com/) en détail.

Alors, commençons.

## Pourquoi la bibliothèque react-hook-form est la bibliothèque de formulaires la plus populaire dans React

Voici quelques-unes des raisons pour lesquelles `react-hook-form` est un choix populaire pour créer des formulaires React.

* Le nombre de re-rendus dans l'application est plus faible par rapport aux alternatives car elle utilise des refs au lieu de l'état.
* La quantité de code que vous devez écrire est moindre par rapport à `formik`, `react-final-form` et autres alternatives.
* `react-hook-form` s'intègre bien avec la bibliothèque `yup` pour la validation de schéma, vous pouvez donc combiner vos propres schémas de validation.
* Le temps de montage est plus court par rapport aux autres alternatives.

Consultez le site [react-hook-form](https://react-hook-form.com/) pour une comparaison plus détaillée.

## Comment créer un formulaire sans utiliser de bibliothèque

Avant de créer un formulaire en utilisant la bibliothèque `react-hook-form`, créons un formulaire simple sans utiliser de bibliothèque.

Regardez le code ci-dessous :

```js
import React, { useState } from "react";
import "./styles.css";

export default function App() {
  const [state, setState] = useState({
    email: "",
    password: ""
  });

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setState((prevProps) => ({
      ...prevProps,
      [name]: value
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

Voici une [démo Code Sandbox](https://codesandbox.io/s/login-form-zird0r?file=/src/App.js).

Dans le code ci-dessus, nous n'avons que deux champs de saisie, à savoir `email` et `password`, et un bouton de soumission.

Chaque champ de saisie a une valeur et un gestionnaire `onChange` ajouté afin que nous puissions mettre à jour l'état en fonction de l'entrée de l'utilisateur.

De plus, nous avons ajouté une méthode `handleSubmit` qui affiche les données saisies dans le formulaire dans la console.

Cela semble bien. Mais que se passe-t-il si nous devons ajouter des validations comme la validation de champ obligatoire, la validation de longueur minimale, la validation de mot de passe, la validation de champ email et également afficher les messages d'erreur correspondants ?

Le code deviendra plus complexe et long à mesure que le nombre de champs de saisie et leurs validations augmentent.

## Comment installer react-hook-form

L'affichage de formulaires est une exigence très courante dans toute application.

Alors, apprenons pourquoi et comment utiliser react-hook-form. Pour cela, nous allons créer une nouvelle application React.

Créez un nouveau projet React en exécutant la commande suivante à partir du terminal :

```js
create-react-app demo-react-hook-form
```

Une fois le projet créé, supprimez tous les fichiers du dossier `src` et créez de nouveaux fichiers `index.js` et `styles.css` à l'intérieur du dossier `src`.

Pour installer la bibliothèque `react-hook-form`, exécutez la commande suivante à partir du terminal :

```js
npm install react-hook-form@7.38.0

OU

yarn add react-hook-form@7.38.0
```

Ici, nous installons la version `7.38.0` de la bibliothèque `react-hook-form`, qui est la dernière version au moment de la rédaction de cet article.

## Comment créer des pages initiales

Ouvrez le fichier `src/index.js` et ajoutez le contenu suivant à l'intérieur :

```js
import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);

```

Notez que le code ci-dessus utilise la syntaxe de React version 18+ pour le rendu de l'application.

Si vous utilisez une version de React inférieure à 18 (que vous pouvez confirmer à partir du fichier `package.json`), ajoutez alors le code suivant dans votre fichier `src/index.js`.

```js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(<App />, document.getElementById('root'));
```

Maintenant, ouvrez le fichier `src/styles.css` et ajoutez le contenu de [ici](https://gist.github.com/myogeshchavan97/2e0b00d38f8f927799d8180906e9dde3) à l'intérieur.

Maintenant, créez un nouveau fichier appelé `App.js` à l'intérieur du dossier `src` avec le contenu suivant :

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

## Comment créer un formulaire de base avec react-hook-form

La bibliothèque `react-hook-form` fournit un hook `useForm` que nous pouvons utiliser pour travailler avec des formulaires.

Importez le hook `useForm` comme ceci :

```js
import { useForm } from 'react-hook-form';
```

Vous pouvez utiliser le hook `useForm` comme ceci :

```js
const {
  register,
  handleSubmit,
  formState: { errors },
} = useForm();
```

Ici,

* `register` est une fonction fournie par le hook `useForm`. Nous pouvons l'assigner à chaque champ de saisie afin que `react-hook-form` puisse suivre les changements de la valeur du champ de saisie.
* `handleSubmit` est la fonction que nous pouvons appeler lorsque le formulaire est soumis.
* `errors` est une propriété imbriquée dans l'objet `formState` qui contiendra les erreurs de validation, le cas échéant.

Maintenant, remplacez le contenu du fichier `App.js` par le code suivant :

```js
import React from "react";
import { useForm } from "react-hook-form";
import "./styles.css";

export default function App() {
  const {
    register,
    handleSubmit,
    formState: { errors }
  } = useForm();

  const onSubmit = (data) => {
    console.log(data);
  };

  return (
    <div className="App">
      <form onSubmit={handleSubmit(onSubmit)}>
        <div className="form-control">
          <label>Email</label>
          <input type="text" name="email" {...register("email")} />
        </div>
        <div className="form-control">
          <label>Mot de passe</label>
          <input type="password" name="password" {...register("password")} />
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

Dans le code ci-dessus, nous avons ajouté une fonction register à chaque champ de saisie que nous avons obtenu du hook `useForm` en passant un nom unique à chaque fonction `register` comme ceci :

```js
{...register("email")}
```

Nous utilisons l'opérateur de décomposition afin que `react-hook-form` puisse décomposer tous les gestionnaires d'événements requis comme `onChange`, `onBlur`, et autres props pour ce champ de saisie.

Si vous ajoutez un `console.log({ ...register("email") });` à l'intérieur du composant, vous verrez ce qu'il retourne comme on peut le voir ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/register_output.png)

Nous avons également ajouté la fonction `onSubmit` qui est passée à la méthode `handleSubmit` comme ceci :

```js
<form onSubmit={handleSubmit(onSubmit)}>
...
```

Notez que vous devez passer un nom unique à la fonction `register` ajoutée pour chaque champ de saisie afin que `react-hook-form` puisse suivre les données changeantes.

Lorsque nous soumettons le formulaire, la fonction `handleSubmit` gérera la soumission du formulaire. Elle enverra les données saisies par l'utilisateur à la fonction `onSubmit` où nous enregistrons les données de l'utilisateur dans la console.

```js
const onSubmit = (data) => {  
 console.log(data);
};
```

Maintenant, démarrez l'application en exécutant la commande `npm start` ou `yarn start` et vous verrez l'écran suivant :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/login_logs-2.gif)

Voici une [démo Code Sandbox](https://codesandbox.io/s/login-form-forked-9so04x?file=/src/App.js).

Comme vous pouvez le voir, lorsque nous soumettons le formulaire, les détails saisis par l'utilisateur sont affichés dans la console.

De plus, par rapport au code sans `react-hook-form` (que nous avons vu au début de cet article dans cette [démo Code Sandbox](https://codesandbox.io/s/login-form-zird0r?file=/src/App.js)), ce code est beaucoup plus simple.

Cela est dû au fait que nous n'avons pas à ajouter le `value` et le gestionnaire `onChange` pour chaque champ de saisie et il n'est pas nécessaire de gérer l'état de l'application nous-mêmes.

## Comment ajouter des validations au formulaire

Maintenant, ajoutons la validation de champ obligatoire et de longueur minimale aux champs de saisie.

Pour ajouter une validation, nous pouvons passer un objet à la fonction `register` en tant que deuxième paramètre comme ceci :

```js
<input
  type="text"
  name="email"
  {...register("email", {
    required: true
  })}
/>

<input
  type="password"
  name="password"
  {...register("password", {
    required: true,
    minLength: 6
  })}
/>
```

Ici, pour le champ email, nous spécifions la validation de champ obligatoire. Pour le champ mot de passe, nous spécifions le champ obligatoire et la validation de longueur minimale de 6 caractères.

Lorsque la validation échoue, l'objet `errors` provenant du hook `useForm` sera rempli avec les champs pour lesquels la validation a échoué.

Nous utiliserons donc cet objet `errors` pour afficher des messages d'erreur personnalisés.

Ouvrez le fichier `App.js` et remplacez son contenu par le contenu suivant :

```js
import React from "react";
import { useForm } from "react-hook-form";
import "./styles.css";

export default function App() {
  const {
    register,
    handleSubmit,
    formState: { errors }
  } = useForm();

  const onSubmit = (data) => {
    console.log(data);
  };

  return (
    <div className="App">
      <form onSubmit={handleSubmit(onSubmit)}>
        <div className="form-control">
          <label>Email</label>
          <input
            type="text"
            name="email"
            {...register("email", {
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
            {...register("password", {
              required: true,
              minLength: 6
            })}
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

Si vous vérifiez l'application maintenant, vous verrez l'écran suivant :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/basic_validation-2.gif)

Voici une [démo Code Sandbox](https://codesandbox.io/s/login-form-with-validations-6388wx?file=/src/App.js).

Comme vous pouvez le voir, nous obtenons des erreurs de validation instantanées pour chaque champ de saisie une fois que nous soumettons le formulaire et que nous essayons ensuite d'entrer les valeurs dans les champs de saisie.

Si une erreur survient pour l'un des champs de saisie, l'objet `errors` sera rempli avec le type d'erreur que nous utilisons pour afficher notre propre message d'erreur personnalisé comme ceci :

```js
{errors.email && errors.email.type === "required" && (
    <p className="errorMsg">L'email est obligatoire.</p>
)}
{errors.email && errors.email.type === "pattern" && (
    <p className="errorMsg">L'email n'est pas valide.</p>
)}
```

Ici, en fonction du type d'erreur, nous affichons différents messages d'erreur.

En utilisant l'opérateur de chaînage optionnel [ES11](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining), vous pouvez simplifier davantage le code ci-dessus comme ceci :

```js
{errors.email?.type === "required" && (
    <p className="errorMsg">L'email est obligatoire.</p>
)}
{errors.email?.type === "pattern" && (
    <p className="errorMsg">L'email n'est pas valide.</p>
)}
```

De la même manière, nous avons ajouté la validation du champ mot de passe.

De plus, comme vous pouvez le voir, chaque champ de saisie est automatiquement mis au point lorsque nous soumettons le formulaire s'il y a une erreur de validation pour ce champ de saisie.

De plus, le formulaire n'est pas soumis tant qu'il y a une erreur de validation. Si vous vérifiez la console du navigateur, vous verrez que l'instruction `console.log` n'est imprimée que si le formulaire est valide et qu'il n'y a pas d'erreurs.

Ainsi, l'utilisation de `react-hook-form` a réduit la quantité de code que nous devions écrire. La validation est également réactive, donc une fois que le champ devient valide, le message d'erreur disparaît instantanément.

Mais à mesure que le nombre de validations pour chaque champ augmente, les vérifications conditionnelles et le code des messages d'erreur augmenteront encore. Nous pouvons donc refactoriser davantage le code pour le rendre encore plus simple.

Regardez le code ci-dessous :

```js
import React from "react";
import { useForm } from "react-hook-form";
import "./styles.css";

export default function App() {
  const {
    register,
    handleSubmit,
    formState: { errors }
  } = useForm();

  const onSubmit = (data) => {
    console.log(data);
  };

  return (
    <div className="App">
      <form onSubmit={handleSubmit(onSubmit)}>
        <div className="form-control">
          <label>Email</label>
          <input
            type="text"
            name="email"
            {...register("email", {
              required: "L'email est obligatoire.",
              pattern: {
                value: /^[^@ ]+@[^@ ]+\.[^@ .]{2,}$/,
                message: "L'email n'est pas valide."
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
            {...register("password", {
              required: "Le mot de passe est obligatoire.",
              minLength: {
                value: 6,
                message: "Le mot de passe doit comporter au moins 6 caractères."
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

Pour le champ de saisie de l'email, nous avons changé ce code précédent :

```js
 {...register("email", {
     required: true,
     pattern: /^[^@ ]+@[^@ ]+\.[^@ .]{2,}$/
 })}
```

en le code ci-dessous :

```js
{...register("email", {
    required: "L'email est obligatoire.",
    pattern: {
        value: /^[^@ ]+@[^@ ]+\.[^@ .]{2,}$/,
        message: "L'email n'est pas valide."
    }
})}
```

Ici, nous avons directement fourni le message d'erreur que nous voulons afficher tout en ajoutant la validation elle-même.

Ainsi, nous n'avons plus besoin d'ajouter des vérifications supplémentaires pour chaque validation. Nous affichons le message d'erreur en utilisant la propriété `message` disponible à l'intérieur de l'objet `errors` pour chaque champ de saisie comme ceci :

```js
{errors.email && <p className="errorMsg">{errors.email.message}</p>}
```

En procédant ainsi, le code est encore simplifié, ce qui facilite l'ajout de validations supplémentaires à l'avenir.

Notez que, s'il y a des erreurs de validation, le gestionnaire onSubmit ne sera pas exécuté et le champ de saisie correspondant sera automatiquement mis au point (ce qui est une bonne chose).

Voici une [démo Code Sandbox mise à jour](https://codesandbox.io/s/login-form-with-validations-simplified-7o4y0k?file=/src/App.js).

## Comment ajouter plusieurs validations

Vous pouvez même fournir plusieurs validations pour le champ de saisie en ajoutant un objet `validate`. Cela est utile si vous devez effectuer des validations complexes comme ceci :

```js
 <input
    type="password"
    name="password"
    {...register("password", {
        required: true,
        validate: {
            checkLength: (value) => value.length >= 6,
            matchPattern: (value) =>
            /(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?!.*\s)(?=.*[!@#$*])/.test(
                value
            )
        }
    })}
/>
```

et pour afficher les messages d'erreur, nous l'utilisons comme ceci :

```js
{errors.password?.type === "required" && (
    <p className="errorMsg">Le mot de passe est obligatoire.</p>
)}
{errors.password?.type === "checkLength" && (
    <p className="errorMsg">
    	Le mot de passe doit comporter au moins 6 caractères.
    </p>
)}
{errors.password?.type === "matchPattern" && (
    <p className="errorMsg">
    	Le mot de passe doit contenir au moins une lettre majuscule, une lettre minuscule, un chiffre et un symbole spécial.
    </p>
)}
```

Voici une [démo Code Sandbox](https://codesandbox.io/s/login-form-with-validations-multiple-zyvp69?file=/src/App.js).

![Image](https://www.freecodecamp.org/news/content/images/2022/10/multiple_validations.gif)

## Comment réinitialiser les valeurs du formulaire

Parfois, nous devons réinitialiser/effacer les données saisies par l'utilisateur après une certaine action.

Par exemple, une fois le formulaire soumis, nous voulons afficher le message de succès puis effacer les données du formulaire afin que l'utilisateur ne puisse pas soumettre à nouveau les mêmes données.

Dans un tel cas, nous pouvons appeler la fonction `reset` retournée par le hook `useForm` pour effacer les données du formulaire.

```js
const { reset } = useForm();

```

Voici une [démo Code Sandbox](https://codesandbox.io/s/reset-form-buowrs?file=/src/App.js).

![Image](https://www.freecodecamp.org/news/content/images/2022/10/reset.gif)

La fonction `reset` accepte également un objet optionnel où vous pouvez passer les valeurs que vous souhaitez réinitialiser pour les données du formulaire :

```js
reset({
    username: "Alex",
    email: "alex@example.com",
    password: "Test@123"
});
```

Ici, la clé username, email ou password doit correspondre au nom passé à la fonction `register` afin que le champ de saisie respectif soit défini sur la valeur passée.

## Comment définir les valeurs initiales du formulaire en utilisant defaultValues

Le hook [useForm](https://react-hook-form.com/api/useform/) accepte une liste d'options, dont l'une est `defaultValues`.

En utilisant `defaultValues`, nous pouvons définir des valeurs initiales pour les éléments de formulaire et les réinitialiser lors du passage d'une page à une autre comme ceci :

```js
const { user } = props;
const {
    register,
    handleSubmit,
    formState: { errors }
} = useForm({
   defaultValues: {
      first_name: user.first_name,
      last_name: user.last_name
    }
});

// JSX

<Form.Control
    type="text"
    {...register("first_name")}
/>

<Form.Control
    type="text"
    {...register("last_name")}
/>

```

Dans le code ci-dessus, pour la fonction `register`, nous avons passé `first_name` comme nom. Cela signifie que dans `defaultValues`, nous utilisons le même nom pour définir la valeur initiale.

Ainsi, pour définir correctement la valeur de saisie, vous devez utiliser le même nom utilisé dans la fonction `register` pour définir la valeur initiale en utilisant `defaultValues`.

Voici une [démo Code Sandbox](https://codesandbox.io/s/nice-khorana-80rktx?file=/src/components/FirstStep.js).

![Image](https://www.freecodecamp.org/news/content/images/2022/10/retain_values.gif)

## Comment utiliser react-hook-form avec d'autres bibliothèques

Parfois, nous pourrions utiliser certaines bibliothèques externes comme [react-select](https://react-select.com/home) pour permettre une sélection multiple dans une liste déroulante.

Dans de tels cas, nous ne pouvons pas directement ajouter la fonction `register` pour afficher la liste déroulante de sélection. Donc, si nous voulons ajouter des validations `react-hook-form` sans écrire notre propre code et fonction de gestionnaire, nous pouvons utiliser le composant `Controller` de `react-hook-form` comme ceci :

```js
import React from "react";
import { useForm, Controller } from "react-hook-form";
import Select from "react-select";
import "./styles.css";

const departments = [
  { value: "Computer-Science", label: "Computer Science" },
  { value: "Physics", label: "Physics" },
  { value: "Chemistry", label: "Chemistry" },
  { value: "Mathematics", label: "Mathematics" }
];

export default function App() {
  const {
    control,
    handleSubmit,
    formState: { errors }
  } = useForm();

  const onSubmit = (data) => {
    console.log(data);
  };

  return (
    <div className="App">
      <form onSubmit={handleSubmit(onSubmit)}>
        <div className="form-control">
          <label>Sélectionnez le département d'intérêt</label>
          <Controller
            name="department"
            control={control}
            rules={{ required: true }}
            render={({ field }) => (
              <Select {...field} isMulti options={departments} />
            )}
          />
          {errors.department && (
            <p className="errorMsg">Ce champ est obligatoire.</p>
          )}
        </div>
        <div className="form-control">
          <label></label>
          <button type="submit">Soumettre</button>
        </div>
      </form>
    </div>
  );
}

```

Voici une [démo Code Sandbox](https://codesandbox.io/s/react-hook-form-controller-g8jxbf?file=/src/App.js).

Comme vous pouvez le voir dans le code ci-dessus, nous importons le composant `Controller` en haut :

```js
import { useForm, Controller } from "react-hook-form";
```

et `control` du hook `useForm` comme ceci :

```js
const {
    control,
    handleSubmit,
    formState: { errors }
  } = useForm();
```

Notez que nous n'utilisons pas la fonction `register` ici.

L'utilisation régulière de la bibliothèque [react-select](https://react-select.com/home) pour permettre une sélection multiple se fait comme ceci :

```js
import Select from "react-select";

// utiliser
<Select isMulti options={options} />
```

Mais pour l'utiliser avec `react-hook-form`, nous devons l'envelopper dans le composant `Controller` :

```js
<Controller
    name="department"
    control={control}
    rules={{ required: true }}
    render={({ field }) => (
       <Select {...field} isMulti options={options} />
    )}
 />
```

Ici, nous devons donner une valeur unique pour la prop `name` dans le `Controller`.

Les validations sont ajoutées dans le cadre de la prop `rules` et nous utilisons la prop `render` pour rendre la liste déroulante `Select`.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/controller.gif)

## Comment utiliser d'autres types de saisie avec react-hook-form

Dans cette section, nous verrons comment utiliser les boutons radio et les cases à cocher avec `react-hook-form`.

Regardez le code ci-dessous :

```js
import React from "react";
import { Button, Form } from "react-bootstrap";
import { useForm } from "react-hook-form";
import "./styles.css";

export default function App() {
  const {
    register,
    handleSubmit,
    formState: { errors }
  } = useForm();

  const onSubmit = (data) => {
    console.log(data);
  };

  return (
    <div className="container">
      <form onSubmit={handleSubmit(onSubmit)}>
        <Form.Group className="mb-3" controlId="email">
          <Form.Label>Email</Form.Label>
          <Form.Control
            type="email"
            placeholder="Entrez votre email"
            {...register("email", {
              required: "Veuillez entrer votre email",
              pattern: {
                value: /^[^@ ]+@[^@ ]+\.[^@ .]{2,}$/,
                message: "Veuillez entrer un email valide"
              }
            })}
          />
          {errors.email && <p className="errorMsg">{errors.email.message}</p>}
        </Form.Group>
        <Form.Group className="mb-3" controlId="gender">
          <Form.Label>Sélectionnez le genre</Form.Label>
          <Form.Check
            type="radio"
            label="Homme"
            value="male"
            {...register("gender", {
              required: "Veuillez sélectionner votre genre"
            })}
          />
          <Form.Check
            type="radio"
            label="Femme"
            value="female"
            {...register("gender")}
          />
          {errors.gender && <p className="errorMsg">{errors.gender.message}</p>}
        </Form.Group>
        <Form.Group className="mb-3" controlId="skills">
          <Form.Label>Sélectionnez vos compétences</Form.Label>
          <Form.Check
            type="checkbox"
            label="JavaScript"
            value="JavaScript"
            {...register("skills", {
              required: "Veuillez sélectionner au moins une compétence"
            })}
          />
          <Form.Check
            type="checkbox"
            label="React"
            value="react"
            {...register("skills")}
          />
          <Form.Check
            type="checkbox"
            label="Node.js"
            value="nodejs"
            {...register("skills")}
          />
          <Form.Check
            type="checkbox"
            label="Angular"
            value="angular"
            {...register("skills")}
          />
          {errors.skills && <p className="errorMsg">{errors.skills.message}</p>}
        </Form.Group>
        <label></label>
        <Button type="submit" variant="primary">
          Soumettre
        </Button>
      </form>
    </div>
  );
}

```

Voici une [démo Code Sandbox](https://codesandbox.io/s/react-hook-form-other-inputs-zm7u7f?file=/src/App.js).

Dans le code ci-dessus, j'utilise [react-bootstrap](https://react-bootstrap.github.io/) pour rendre l'interface utilisateur plus agréable, donc `Form.Check` est un composant `react-bootstrap`.

Le point principal à retenir est que nous n'avons pas donné les mêmes noms pour la fonction `register` pour un groupe de boutons radio et de cases à cocher comme ceci :

```js
<Form.Check
    type="radio"
    label="Homme"
    value="male"
    {...register("gender", {
        required: "Veuillez sélectionner votre genre"
    })}
/>
<Form.Check
    type="radio"
    label="Femme"
    value="female"
    {...register("gender")}
/>
```

Dans le code ci-dessus, nous avons donné `gender` comme nom pour les deux boutons radio et `skills` comme nom pour toutes les cases à cocher comme montré ci-dessous :

```js
<Form.Check
    type="checkbox"
    label="JavaScript"
    value="JavaScript"
    {...register("skills", {
        required: "Veuillez sélectionner au moins une compétence"
    })}
/>
<Form.Check
    type="checkbox"
    label="React"
    value="react"
    {...register("skills")}
/>
<Form.Check
    type="checkbox"
    label="Node.js"
    value="nodejs"
    {...register("skills")}
/>
<Form.Check
    type="checkbox"
    label="Angular"
    value="angular"
    {...register("skills")}
/>
```

Notez également que la validation de champ obligatoire est ajoutée uniquement pour le premier bouton radio ou la première case à cocher. Parce que nous utilisons le même nom, nous n'avons pas besoin d'ajouter la même validation à chaque bouton radio ou case à cocher.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/radio_checkbox.gif)

## Comment définir des valeurs initiales pour les boutons radio et les cases à cocher

Parfois, nous pouvons avoir des boutons radio ou des cases à cocher présélectionnés que nous devons afficher au chargement de la page. Dans un tel cas, nous pouvons à nouveau utiliser l'option `defaultValues` du hook `useForm`.

Regardez le code ci-dessous :

```js
import React from "react";
import { Button, Form } from "react-bootstrap";
import { useForm } from "react-hook-form";
import "./styles.css";

const initialValues = {
  gender: "male",
  skills: {
    JavaScript: true,
    react: false,
    nodejs: true,
    angular: false
  }
};

export default function App() {
  const {
    register,
    handleSubmit,
    formState: { errors }
  } = useForm({
    defaultValues: {
      gender: initialValues.gender,
      skills: Object.keys(initialValues.skills).filter(
        (item) => initialValues.skills[item] === true
      )
    }
  });

  const onSubmit = (data) => {
    console.log(data);
  };

  return (
    <div className="container">
      <form onSubmit={handleSubmit(onSubmit)}>
        <Form.Group className="mb-3" controlId="email">
          <Form.Label>Email</Form.Label>
          <Form.Control
            type="email"
            placeholder="Entrez votre email"
            {...register("email", {
              required: "Veuillez entrer votre email",
              pattern: {
                value: /^[^@ ]+@[^@ ]+\.[^@ .]{2,}$/,
                message: "Veuillez entrer un email valide"
              }
            })}
          />
          {errors.email && <p className="errorMsg">{errors.email.message}</p>}
        </Form.Group>
        <Form.Group className="mb-3" controlId="gender">
          <Form.Label>Sélectionnez le genre</Form.Label>
          <Form.Check
            type="radio"
            label="Homme"
            value="male"
            {...register("gender", {
              required: "Veuillez sélectionner votre genre"
            })}
          />
          <Form.Check
            type="radio"
            label="Femme"
            value="female"
            {...register("gender")}
          />
          {errors.gender && <p className="errorMsg">{errors.gender.message}</p>}
        </Form.Group>
        <Form.Group className="mb-3" controlId="skills">
          <Form.Label>Sélectionnez vos compétences</Form.Label>
          <Form.Check
            type="checkbox"
            label="JavaScript"
            value="JavaScript"
            {...register("skills", {
              required: "Veuillez sélectionner au moins une compétence"
            })}
          />
          <Form.Check
            type="checkbox"
            label="React"
            value="react"
            {...register("skills")}
          />
          <Form.Check
            type="checkbox"
            label="Node.js"
            value="nodejs"
            {...register("skills")}
          />
          <Form.Check
            type="checkbox"
            label="Angular"
            value="angular"
            {...register("skills")}
          />
          {errors.skills && <p className="errorMsg">{errors.skills.message}</p>}
        </Form.Group>
        <label></label>
        <Button type="submit" variant="primary">
          Soumettre
        </Button>
      </form>
    </div>
  );
}

```

Voici une [démo Code Sandbox](https://codesandbox.io/s/react-hook-form-other-inputs-initial-values-t38s9v?file=/src/App.js).

Dans le code ci-dessus, nous avons un objet `initialValues` qui contient les valeurs que nous voulons définir au chargement initial de la page :

```js
const initialValues = {
  gender: "male",
  skills: {
    JavaScript: true,
    react: false,
    nodejs: true,
    angular: false
  }
};
```

Comme nous pouvons avoir plusieurs compétences, `skills` est un objet comme montré ci-dessus. Nous voulons donc afficher le bouton radio sélectionné si sa valeur est `male` et nous voulons afficher uniquement les cases à cocher sélectionnées pour lesquelles la valeur est `true` dans l'objet `skills`.

Par conséquent, pour l'option `defaultValues`, nous parcourons l'objet `skills` en utilisant la méthode `filter` pour trouver les compétences pour lesquelles la valeur est `true` comme montré ci-dessous :

```js
const {
    register,
    handleSubmit,
    formState: { errors }
  } = useForm({
    defaultValues: {
      gender: initialValues.gender,
      skills: Object.keys(initialValues.skills).filter(
        (item) => initialValues.skills[item] === true
      )
    }
  });
```

Comme les valeurs `JavaScript` et `nodejs` sont `true`, le tableau `skills` après la méthode `filter` deviendra `["JavaScript", "nodejs"]` donc l'objet `defaultValues` ressemblera à ceci :

```js
useForm({
    defaultValues: {
        gender: 'male',
        skills: ["JavaScript", "nodejs"]
    }
});
```

Par conséquent, lorsque la page est chargée, seul le genre `male` et les compétences `JavaScript` et `Node.js` seront sélectionnés/cochés par défaut.

Notez que la casse utilisée dans l'objet `skills` doit correspondre à la `value` spécifiée pour la case à cocher.

Ainsi, même si l'étiquette de la case à cocher est `Node.js`, sa valeur est `nodejs`, donc nous utilisons `nodejs` comme clé dans l'objet `initialValues`.

Ci-dessous se trouve la démonstration de l'apparence au chargement de la page.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/default_checked.gif)

Et c'est tout ! Vous avez appris comment utiliser react-hook-form pour construire plus facilement des formulaires complexes dans React.

## Merci d'avoir lu !

Si vous voulez apprendre Redux en détail à partir de zéro et construire 3 applications ainsi que l'application complète de commande de nourriture, consultez mon cours [Mastering Redux](https://master-redux.yogeshchavan.dev/).

Dans le cours, vous apprendrez :

* Redux de base et avancé
* Comment gérer l'état complexe des tableaux et des objets
* Comment utiliser plusieurs réducteurs pour gérer l'état complexe de Redux
* Comment déboguer une application Redux
* Comment utiliser Redux dans React en utilisant la bibliothèque react-redux pour rendre votre application réactive.
* Comment utiliser la bibliothèque redux-thunk pour gérer les appels API asynchrones
* Construire 3 applications différentes en utilisant Redux

et bien plus encore.

Enfin, nous construirons une application complète de commande de nourriture à partir de zéro avec l'intégration de Stripe pour accepter les paiements et la déployer en production.

**Vous voulez rester à jour avec du contenu régulier concernant JavaScript, React, Node.js ? [Suivez-moi sur LinkedIn](https://www.linkedin.com/in/yogesh-chavan97/).**