---
title: Comment créer des formulaires React avec Formik
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-20T16:56:05.000Z'
originalURL: https://freecodecamp.org/news/build-react-forms-with-formik-library
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Group-1--1-.jpg
tags:
- name: forms
  slug: forms
- name: React
  slug: react
seo_title: Comment créer des formulaires React avec Formik
seo_desc: "By Popoola Temitope\nForm building in React can be complex and time-consuming,\
  \ requiring state management, validation, and error handling. \nTo simplify this\
  \ process, the Formik library provides an intuitive solution for building forms\
  \ in React. Formik..."
---

Par Popoola Temitope

La création de formulaires dans [`React`](https://reactjs.org/) peut être complexe et chronophage, nécessitant la gestion de l'état, la validation et la gestion des erreurs. 

Pour simplifier ce processus, la bibliothèque [`Formik`](https://formik.org/) offre une solution intuitive pour créer des formulaires dans React. Formik possède une API simple et une validation intégrée, facilitant la collecte et la manipulation des données de saisie dans les applications React.

# Qu'est-ce que Formik ?

`[Formik](https://formik.org/)` est une bibliothèque open-source populaire pour créer et traiter les données de formulaires dans les applications React. Elle fournit de nombreux composants et fonctions utilitaires qui rendent la gestion des données de formulaire dans une application React plus agréable.

La méthode traditionnelle de gestion des formulaires dans React nécessite la création d'un hook **`useState()`** unique ou universel pour chaque champ de formulaire, l'ajout d'un écouteur d'événements à chaque champ et le déclenchement d'une méthode pour les mettre à jour individuellement. 

```javascript
// Méthode traditionnelle exaspérante de gestion de formulaires React

import { useState } from "react";

function InputForm() {
  const [input1, setInput1] = useState("");
  const [input2, setInput2] = useState("");

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    if (name === "input1") {
      setInput1(value);
    } else if (name === "input2") {
      setInput2(value);
    }
  };

  const handleSubmit = (event) => {
   // . . .
  };

  return (
    <form onSubmit={handleSubmit}>
      <input name="input1" value={input1} onChange={handleInputChange} />
      <input name="input2" value={input2} onChange={handleInputChange} />
      <button type="submit">Envoyer</button>
    </form>
  );
}

export default InputForm;
```

D'un autre côté, Formik gère toutes ces opérations fastidieuses pour nous en arrière-plan. Nous avons seulement besoin d'importer les composants qu'il fournit – nos données de formulaire sont immédiatement disponibles.

```javascript 
<Formik
  onSubmit={(formData) => {
    console.log(formData);
  }}
>
  {({ isSubmitting }) => (
    <Form>
      <Field type="text" name="fullname" placeholder="Saisissez le nom complet" />
      <Field type="email" name="email" placeholder="Saisissez l'adresse" />
      <button type="submit">Envoyer</button>
    </Form>
  )}
</Formik>;
```

En plus de nous aider à gérer les données de formulaire, Formik propose d'autres mécanismes qui nous permettent de valider les champs de formulaire, de suivre l'état de soumission du formulaire et de gérer les erreurs.

Ce tutoriel vous montrera comment utiliser Formik dans une application React en créant un formulaire d'inscription simple.

# Comment installer Formik

Pour commencer avec Formik, créons une nouvelle application React à l'aide de la commande ci-dessous :

```bash
npx create-react-app my-app
cd my-app
npm start
```

Une fois que notre application React est configurée, nous pouvons installer Formik avec la commande suivante :

```bash
npm install formik --save
```

Une fois Formik installé, nous pouvons importer ses composants et les utiliser dans notre application.

```javascript
import { Formik, Form, Field, ErrorMessage } from 'formik';
```

Dans le code d'importation ci-dessus, nous avons les éléments suivants :

* Le composant `Form` enveloppe tous les champs du formulaire et fournit le contexte essentiel pour utiliser les outils de Formik. Cela inclut la gestion de l'état du formulaire, la gestion de la validation et la soumission du formulaire.
* `Field` est un composant fourni par Formik qui représente un champ de formulaire. Nous pouvons utiliser ce composant pour générer un champ de saisie (input), de sélection (select) ou d'autres éléments de formulaire. Il gère automatiquement l'état du champ, comme sa valeur et sa validation.
* `ErrorMessage` est un composant fourni par Formik qui affiche un message d'erreur pour un champ spécifique. Nous pouvons utiliser ce composant pour afficher les erreurs de validation d'un champ. C'est particulièrement utile pour afficher les erreurs de formulaire de manière conviviale.

# Comment créer un formulaire avec Formik

Nous pouvons créer un champ de saisie de formulaire en enveloppant le formulaire et ses champs à l'intérieur du composant Formik. Le code ci-dessous est un exemple de création de formulaire à l'aide de Formik :

```javascript 
import React from "react";
import { Formik, Form, Field, ErrorMessage } from "formik";
function App() {
 return (
   <div className="App">
     <center>
       <h1>Créer un nouveau compte</h1>
       <Formik>
         {({ isSubmitting }) => (
           <Form>
             <Field
               type="text"
               name="fullname"
               placeholder="Saisissez votre nom complet"
             />
             <ErrorMessage name="fullname" component="div" />

             <Field
               type="email"
               name="email"
               placeholder="Saisissez votre adresse e-mail"
             />
             <ErrorMessage name="email" component="div" />

             <Field type="password" name="password" />
             <ErrorMessage name="password" component="div" />

             <button type="submit" disabled={isSubmitting}>
               Envoyer
             </button>
           </Form>
         )}
       </Formik>
     </center>
   </div>
 );
}
export default App;
```

Dans le code ci-dessus, le composant Formik enveloppe le formulaire et fournit des utilitaires tels que la validation du formulaire et la gestion de la soumission. Le composant `Field` définit chaque champ du formulaire, comme `fullname`, `email` et `password`, tandis que le composant `ErrorMessage` affiche les erreurs de validation pour chaque champ.

La prop `isSubmitting` est transmise à la fonction render prop, qui est utilisée pour désactiver le bouton d'envoi pendant la soumission du formulaire.

Ensuite, nous devons définir les valeurs initiales des champs en passant la prop `initialValues`. Nous pouvons définir les valeurs initiales pour fullname, email et password à l'aide du code ci-dessous :

```javascript 
<Formik initialValues={{ fullname: "", email: "", password: "" }}>
```

## Validation de formulaire avec Formik

Lors de la création de formulaires, il est essentiel de valider les données de saisie pour éviter les erreurs et offrir une expérience utilisateur interactive. Le code ci-dessous montre comment valider les données de saisie d'un formulaire à l'aide de Formik.

```javascript 
<Formik
         initialValues={{ fullname: "", email: "", password: "" }}
         validate={(values) => {
           const errors = {};
           if (!values.fullname) {
             errors.fullname = "Requis";
           }

           if (!values.email) {
             errors.email = "Requis";
           } else if (
             !/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i.test(values.email)
           ) {
             errors.email = "Adresse e-mail invalide";
           }
           if (!values.password) {
             errors.password = "Requis";
           }
           return errors;
         }}
       >
```

Dans le code ci-dessus, nous utilisons la prop `validate` pour définir une fonction de validation qui sera appelée chaque fois que l'utilisateur interagit avec le formulaire. Cette fonction prend les valeurs actuelles des champs du formulaire en paramètre et renvoie un objet spécifiant les erreurs éventuelles.

## Soumission de formulaire avec Formik

Formik utilise une fonction `onSubmit` pour gérer les données du formulaire chaque fois que le bouton d'envoi est cliqué. Il valide d'abord les données à l'aide de la fonction de validation. 

Pour traiter un formulaire à l'aide de la fonction `onSubmit`, ajoutez le code suivant au composant Formik :

```javascript
 <Formik
   initialValues={{ fullname: "", email: "", password: "" }}
   // . . .
   onSubmit={(values, { setSubmitting }) => {
     setTimeout(() => {
       alert(JSON.stringify(values, null, 2));
       setSubmitting(false);
     }, 400);
   }}
>
```

Selon le code ci-dessus, la fonction `onSubmit` est appelée lorsque le formulaire est soumis et utilise la fonction `setSubmitting` pour mettre à jour l'état du composant Formik pendant le processus de soumission.

Voici le résultat du formulaire que nous avons créé avec Formik :

![Image](https://lh6.googleusercontent.com/mhfCqUCehriSWJPKlD55nkuULYzndQOcNC43HsP5PxrfAsc6Cn42CF13uExK3li8gXiFevXpxD_tHe93DrXAgce_hGBO8RCHL1etkjcUGFJfP1VkN1wYceb6F_vywGL9BUG_TwGKU9daQ2O0x12eIcs)

# Conclusion

`Formik` est une bibliothèque React qui rend la création de formulaires facile et intuitive, surtout lors de la conception de formulaires complexes ou pour gagner du temps lors du développement.

Dans ce tutoriel, nous avons appris à utiliser Formik pour créer et gérer les états de formulaire dans les applications React. [Si vous souhaitez en savoir plus sur Formik, vous pouvez consulter leur documentation officielle](https://formik.org/docs/overview).