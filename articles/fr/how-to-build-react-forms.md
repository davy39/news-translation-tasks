---
title: Comment créer des formulaires React facilement avec react-hook-form
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-03-12T16:39:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-react-forms
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/how-to-build-react-forms.png
tags:
- name: Form validations
  slug: form-validations
- name: forms
  slug: forms
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: Comment créer des formulaires React facilement avec react-hook-form
seo_desc: 'Nobody enjoys creating and re-creating complex forms with validation, React
  developers included.

  When it comes to building forms in React, it''s essential to use a form library
  that provides a lot of convenient tools and doesn’t require much code.

  Bas...'
---

Personne n'aime créer et recréer des formulaires complexes avec validation, y compris les développeurs React.

Lorsqu'il s'agit de créer des formulaires dans React, il est essentiel d'utiliser une bibliothèque de formulaires qui fournit de nombreux outils pratiques et ne nécessite pas beaucoup de code.

Sur la base de ces deux critères, utilité et simplicité, la bibliothèque de formulaires React idéale à utiliser pour vos applications est `react-hook-form`.

Voyons comment utiliser react-hook-form dans vos propres projets pour créer des formulaires riches et fonctionnels pour vos applications React.

## Comment installer react-hook-form

Examinons un cas d'utilisation typique : un utilisateur s'inscrivant à notre application.

Pour notre formulaire d'inscription, nous aurons trois champs pour le nom d'utilisateur, le mot de passe et l'email de tout nouvel utilisateur :

```jsx
import React from "react";

const styles = {
  container: {
    width: "80%",
    margin: "0 auto",
  },
  input: {
    width: "100%",
  },
};

export default function Signup() {
  return (
    <div style={styles.container}>
      <h4>S'inscrire</h4>
      <form>
        <input placeholder="Nom d'utilisateur" style={styles.input} />
        <input placeholder="Email" style={styles.input} />
        <input placeholder="Mot de passe" style={styles.input} />
        <button type="submit">Soumettre</button>
      </form>
    </div>
  );
}

```

Une fois que nous avons un projet React en cours d'exécution, nous commencerons par installer la bibliothèque `react-hook-form`.

```bash
npm i react-hook-form

```

## Comment utiliser le hook useForm

Pour commencer à utiliser `react-hook-form`, nous devons simplement appeler le hook `useForm`.

Lorsque nous le faisons, nous obtenons un objet à partir duquel nous allons déstructurer la propriété `register`.

`register` est une fonction que nous devons connecter à chacun des champs en tant que ref.

```jsx
function App() {
  const { register } = useForm();

  return (
    <div style={styles.container}>
      <h4>Inscription</h4>
      <form>
        <input ref={register} placeholder="Nom d'utilisateur" style={styles.input} />
        <input ref={register} placeholder="Email" style={styles.input} />
        <input ref={register} placeholder="Mot de passe" style={styles.input} />
        <button type="submit">Soumettre</button>
      </form>
    </div>
  );
}

```

La fonction register prendra la valeur que notre utilisateur a tapée dans chaque champ pour la valider. Register transmettra également chaque valeur à une fonction qui sera appelée lorsque notre formulaire sera soumis, ce que nous aborderons ensuite.

Pour que register fonctionne correctement, pour chaque champ, nous devons fournir un attribut name approprié. Par exemple, pour le champ de nom d'utilisateur, il aura un nom de "username".

La raison en est que lorsque notre formulaire est soumis, nous obtiendrons toutes les valeurs des champs dans un seul objet. Chacune des propriétés de l'objet sera nommée selon les attributs name des champs que nous avons spécifiés.

```jsx
function App() {
  const { register } = useForm();

  return (
    <div style={styles.container}>
      <h4>Mon formulaire</h4>
      <form>
        <input
          name="username"
          ref={register}
          placeholder="Nom d'utilisateur"
          style={styles.input}
        />
        <input
          name="email"
          ref={register}
          placeholder="Email"
          style={styles.input}
        />
        <input
          name="password"
          ref={register}
          placeholder="Mot de passe"
          style={styles.input}
        />
        <button type="submit">Soumettre</button>
      </form>
    </div>
  );
}

```

## Comment soumettre notre formulaire avec handleSubmit

Pour gérer la soumission de notre formulaire et recevoir les données d'entrée, nous ajouterons un `onSubmit` à notre élément de formulaire et le connecterons à une fonction locale du même nom :

```jsx
function App() {
  const { register } = useForm();

  function onSubmit() {}

  return (
    <div style={styles.container}>
      <h4>Mon formulaire</h4>
      <form onSubmit={onSubmit}>
        <input
          name="username"
          ref={register}
          placeholder="Nom d'utilisateur"
          style={styles.input}
        />
        <input
          name="email"
          ref={register}
          placeholder="Email"
          style={styles.input}
        />
        <input
          name="password"
          ref={register}
          placeholder="Mot de passe"
          style={styles.input}
        />
        <button type="submit">Soumettre</button>
      </form>
    </div>
  );
}

```

À partir de `useForm`, nous allons récupérer une fonction appelée `handleSubmit` et l'envelopper autour de onSubmit en tant que fonction d'ordre supérieur.

La fonction `handleSubmit` se chargera de collecter toutes nos données tapées dans chaque champ que nous recevrons dans `onSubmit` sous forme d'objet appelé `data`.

Maintenant, si nous faisons `console.log(data)`, nous pouvons voir ce que nous avons tapé dans chacun de nos champs dans une propriété du même nom :

```jsx
function App() {
  const { register, handleSubmit } = useForm();

  function onSubmit(data) {
    console.log(data); 
    // { username: 'test', email: 'test', password: 'test' }
  }

  return (
    <div style={styles.container}>
      <h4>Inscription</h4>
      <form onSubmit={handleSubmit(onSubmit)}>
        <input
          name="username"
          ref={register}
          placeholder="Nom d'utilisateur"
          style={styles.input}
        />
        <input
          name="email"
          ref={register}
          placeholder="Email"
          style={styles.input}
        />
        <input
          name="password"
          ref={register}
          placeholder="Mot de passe"
          style={styles.input}
        />
        <button type="submit">Soumettre</button>
      </form>
    </div>
  );
}

```

## Options de validation avec la fonction register

Pour valider notre formulaire et ajouter des contraintes pour chaque valeur de champ, c'est très simple : nous devons simplement passer des informations à la fonction `register`.

`register` accepte un objet, qui inclut un certain nombre de propriétés qui indiqueront à register comment valider un champ donné.

La première propriété est `required`. Par défaut, elle est définie sur false, mais nous pouvons la définir sur true pour nous assurer que le formulaire n'est pas soumis s'il n'est pas rempli.

Nous voulons que la valeur du nom d'utilisateur soit requise et nous voulons que les noms d'utilisateur de nos utilisateurs soient composés de plus de six caractères mais de moins de 24.

Pour appliquer cette validation, nous pouvons définir la contrainte de `minLength` à six, mais la `maxLength` doit être de 20 :

```jsx
<input
  name="username"
  ref={register({
    required: true,
    minLength: 6,
    maxLength: 20,
  })}
  style={styles.input}
  placeholder="Nom d'utilisateur"
/>

```

Si nous utilisions des nombres pour ce champ (par exemple, si ce champ était pour l'âge de la personne), nous utiliserions les propriétés `min` et `max` au lieu de `minLength` et `maxLength`.

Ensuite, nous pouvons fournir un motif regex si nous le souhaitons.

Si nous voulons qu'un nom d'utilisateur ne contienne que des caractères majuscules et minuscules, nous pouvons utiliser le regex suivant qui permet une validation personnalisée :

```jsx
<input
  name="username"
  ref={register({
    required: true,
    minLength: 6,
    maxLength: 20,
    pattern: /^[A-Za-z]+$/i,
  })}
  style={styles.input}
  placeholder="Nom d'utilisateur"
/>

```

Et enfin, il y a `validate`, une fonction personnalisée qui nous donne accès à la valeur tapée dans le champ. `validate` nous permet de fournir notre propre logique pour déterminer si elle est valide ou non (en retournant le booléen true ou false).

Pour l'email ici, nous voulons également qu'il soit requis et qu'il soit un email valide. Pour vérifier cela, nous pouvons passer le champ à une fonction de la bibliothèque `validator` appelée `isEmail`.

Si le champ est un email, il retourne true. Sinon, false :

```jsx
<input
  name="email"
  ref={register({
    required: true,
    validate: (input) => isEmail(input), // retourne true si valide
  })}
  style={styles.input}
  placeholder="Email"
/>

```

Pour la fonction `register` du mot de passe, nous définirons required à true, `minlength` à six, et nous ne définirons pas de `maxLength` :

```jsx
<input
  name="password"
  ref={register({
    required: true,
    minLength: 6
  })}
  style={styles.input}
  placeholder="Mot de passe"
/>
```

## Comment afficher les erreurs

Actuellement, si un champ de notre formulaire n'est pas valide, nous ne disons pas à notre utilisateur qu'il y a un problème. Nous devons leur donner un retour pour corriger les valeurs qu'ils ont fournies.

Lorsque l'un des champs est invalide, les données du formulaire ne sont tout simplement pas soumises (`onSubmit` n'est pas appelé). De plus, le premier champ avec une erreur est automatiquement mis au point, ce qui ne fournit pas à notre utilisateur de retour détaillé sur ce qui se passe.

Au lieu de simplement ne pas soumettre le formulaire, nous pouvons récupérer un objet `errors` à partir de useForm.

Et tout comme la fonction data que nous obtenons dans `onSubmit`, `errors` contient des propriétés correspondant à chacun des noms des champs s'il y a une erreur.

Pour notre exemple, nous pouvons ajouter une condition à chacun des champs et dire que s'il y a une erreur, nous définirons la `borderColor` en rouge.

```jsx
function App() {
  const { register, handleSubmit, errors } = useForm();

  function onSubmit(data) {
    console.log(data);
  }

  return (
    <div style={styles.container}>
      <h4>Mon formulaire</h4>
      <form onSubmit={handleSubmit(onSubmit)}>
        <input
          name="username"
          ref={register({
            required: true,
            minLength: 6,
            maxLength: 20,
            pattern: /^[A-Za-z]+$/i,
          })}
          style={{ ...styles.input, borderColor: errors.username && "red" }}
          placeholder="Nom d'utilisateur"
        />
        <input
          name="email"
          ref={register({
            required: true,
            validate: (input) => isEmail(input),
          })}
          style={{ ...styles.input, borderColor: errors.email && "red" }}
          placeholder="Email"
        />
        <input
          name="password"
          ref={register({
            required: true,
            minLength: 6,
          })}
          style={{ ...styles.input, borderColor: errors.password && "red" }}
          placeholder="Mot de passe"
        />
        <button type="submit" disabled={formState.isSubmitting}>
          Soumettre
        </button>
      </form>
    </div>
  );
}

```

## Mode de validation

Vous remarquerez que, par défaut, l'objet errors est mis à jour uniquement lorsque nous soumettons le formulaire. La validation par défaut n'est effectuée qu'au moment de la soumission du formulaire.

Nous pouvons changer cela en passant à `useForm` un objet, où nous pouvons définir le mode pour quand nous voulons que la validation soit effectuée : `onBlur`, `onChange`, ou `onSubmit`.

`onBlur` va faire en sorte que la validation s'exécute chaque fois que l'utilisateur "blure" ou clique en dehors du champ. `onChange` est chaque fois qu'un utilisateur tape dans le champ, et `onSubmit` est chaque fois que le formulaire est soumis.

Pour notre formulaire, choisissons `onBlur`.

```jsx
const { register, handleSubmit, errors } = useForm({
  mode: "onBlur",
});

```

Notez qu'il existe d'autres helpers pour définir et effacer les erreurs manuellement (`setError` et `clearError`). Ceux-ci seraient utilisés si, par exemple, vous aviez certains cas où vous voulez créer une erreur différente ou effacer une erreur vous-même dans `onSubmit`.

## Comment désactiver notre formulaire avec formState

La dernière valeur que nous pouvons obtenir du hook `useForm` est `formState`.

Il nous donne des informations importantes telles que lorsque certains champs ont été touchés, ainsi que lorsque le formulaire a été soumis.

Ainsi, si vous souhaitez désactiver le bouton de votre formulaire pour vous assurer que le formulaire n'est pas soumis plus de fois que nécessaire, nous pourrions définir disabled à `formState.isSubmitting`.

Chaque fois que nous soumettons notre formulaire, il sera désactivé jusqu'à ce qu'il ait terminé la validation et l'exécution de notre fonction onSubmit.

## Conclusion

J'espère que cet article vous a montré comment créer plus facilement des formulaires fonctionnels dans vos applications React.

Il est important de noter qu'il existe de nombreuses autres fonctionnalités qui accompagnent `react-hook-form` que je n'ai pas couvertes ici. La [documentation](https://react-hook-form.com) devrait couvrir tous les cas d'utilisation que vous pouvez imaginer.

Si vous êtes intéressé à voir la version finale de notre code, cliquez sur le lien CodeSandbox [ici](https://codesandbox.io/s/crazy-leavitt-nf74y).

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : Le React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le seul cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*