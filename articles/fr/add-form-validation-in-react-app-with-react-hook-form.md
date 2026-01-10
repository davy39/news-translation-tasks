---
title: Comment ajouter la validation de formulaire dans les formulaires React en utilisant
  React Hook Form
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-10-12T20:52:04.000Z'
originalURL: https://freecodecamp.org/news/add-form-validation-in-react-app-with-react-hook-form
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/How-to-Build-a-Weather-Application-using-React--19--1.png
tags:
- name: Form validations
  slug: form-validations
- name: forms
  slug: forms
- name: React
  slug: react
seo_title: Comment ajouter la validation de formulaire dans les formulaires React
  en utilisant React Hook Form
seo_desc: 'By Nishant Kumar

  Creating forms with proper validation can be tough and problematic. But in this
  blog post, I will show you how to do so in a simple and straightforward way.

  We''ll learn how to add validation in a form using React and React Hook Form....'
---

Par Nishant Kumar

Créer des formulaires avec une validation appropriée peut être difficile et problématique. Mais dans cet article de blog, je vais vous montrer comment le faire de manière simple et directe.

Nous allons apprendre comment ajouter une validation dans un formulaire en utilisant React et React Hook Form.

### Voici un scrim interactif sur la façon d'ajouter la validation de formulaire dans les formulaires React :

<iframe src="https://scrimba.com/scrim/cobc44a7ba60db603359ae530?embed=freecodecamp,mini-header" width="100%" height="480"></iframe>

## Comment créer un formulaire dans React

Nous allons commencer par créer un formulaire en utilisant la bibliothèque Semantic UI. Alors, installons-la en utilisant l'une des commandes suivantes :

```bash
 yarn add semantic-ui-react semantic-ui-css
 ## Ou NPM
 npm install semantic-ui-react semantic-ui-css
```

Après l'avoir installée, vous devez importer le package dans votre fichier index.js, qui est le fichier d'entrée principal de votre application.

```
import 'semantic-ui-css/semantic.min.css'
```

Ensuite, nous avons besoin d'un formulaire avec quatre champs. Alors, créons-le avec le code suivant :

```
import React from 'react';
import { Form, Button } from 'semantic-ui-react';

export default function FormValidation() {
    return (
        <div>
            <Form>
                <Form.Field>
                    <label>Prénom</label>
                    <input placeholder='Prénom' type="text" />
                </Form.Field>
                <Form.Field>
                    <label>Nom de famille</label>
                    <input placeholder='Nom de famille' type="text" />
                </Form.Field>
                <Form.Field>
                    <label>Email</label>
                    <input placeholder='Email' type="email" />
                </Form.Field>
                <Form.Field>
                    <label>Mot de passe</label>
                    <input placeholder='Mot de passe' type="password" />
                </Form.Field>
                <Button type='submit'>Soumettre</Button>
            </Form>
        </div>
    )
}

```

Nous avons maintenant un formulaire. Il a quatre champs, qui sont Prénom, Nom de famille, Email et Mot de passe. Il a également un bouton Soumettre pour que les utilisateurs puissent soumettre le formulaire.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screenshot-2021-10-09-103510.png)

### Comment installer React Hook Form

Pour installer [React Hook Form](https://react-hook-form.com/), utilisez la commande suivante :

```
 npm install react-hook-form
```

Vous pouvez lire la documentation si vous souhaitez en savoir plus sur la bibliothèque. Nous pouvons l'utiliser pour les applications React web et React Native.

La première chose que nous devons faire ici est d'obtenir les données des champs de saisie et de les afficher dans la console. Nous devons d'abord importer le package :

```jsx
import { useForm } from 'react-hook-form';
```

Ensuite, nous devons déstructurer l'objet **`useForm`** dans notre application, comme ceci :

```
const { register, handleSubmit, formState: { errors } } = useForm();
```

Maintenant, nous allons utiliser la propriété **`register`** de l'objet **`useForm`** pour enregistrer nos champs de formulaire. Cela ressemblera à ceci :

```jsx
<Form.Field>
  <label>Prénom</label>
  <input placeholder='Prénom' type='text' {...register('firstName')} />
</Form.Field>;

```

Maintenant, le champ de formulaire Prénom a la clé firstName. Comme vous pouvez le voir, nous l'avons déclaré dans **register**. Répétez cela pour tous les autres champs.

```jsx
import React from 'react';
import { Form, Button } from 'semantic-ui-react';
import { useForm } from 'react-hook-form';

export default function FormValidation() {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm();
  return (
    <div>
      <Form>
        <Form.Field>
          <label>Prénom</label>
          <input
            placeholder='Prénom'
            type='text'
            {...register('firstName')}
          />
        </Form.Field>
        <Form.Field>
          <label>Nom de famille</label>
          <input
            placeholder='Nom de famille'
            type='text'
            {...register('lastName')}
          />
        </Form.Field>
        <Form.Field>
          <label>Email</label>
          <input placeholder='Email' type='email' {...register('email')} />
        </Form.Field>
        <Form.Field>
          <label>Mot de passe</label>
          <input
            placeholder='Mot de passe'
            type='password'
            {...register('password')}
          />
        </Form.Field>
        <Button type='submit'>Soumettre</Button>
      </Form>
    </div>
  );
}

```

Voici le code complet jusqu'à ce point. Quatre champs, et tous enregistrés.

Maintenant, sur le Form, nous devons créer un événement `onSubmit`. Cela signifie que si nous cliquons sur le bouton Soumettre en bas, nos données de formulaire doivent être soumises.

```
<Form onSubmit={handleSubmit(onSubmit)}>
```

Et nous devons également créer une fonction onSubmit, qui effectuera une action spécifique lorsque le bouton de soumission sera cliqué ou pressé.

```jsx
const { register, handleSubmit, formState: { errors } } = useForm();
const onSubmit = (data) => {
  console.log(data);
}
```

Ainsi, si nous cliquons sur le bouton de soumission, nos données saisies s'afficheront dans la console.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screenshot-2021-10-09-104958.png)

## Comment ajouter une validation à nos formulaires

Maintenant, voici l'étape finale et la plus attendue. Ajoutons les validations.

Commençons par le champ Prénom. Nous allons utiliser les propriétés required et maxLength, qui sont assez explicites.

* **Required** signifie que le champ est obligatoire.
* **MaxLength** indique la longueur maximale des caractères que nous entrons.

```jsx
<input
  placeholder='Prénom'
  type="text"
  {...register("firstName", { required: true, maxLength: 10 })}
/>
```

Ainsi, définissez `required` sur true et `maxLength` sur 10. Ensuite, si nous soumettons le formulaire sans entrer le Prénom, ou si le nombre de caractères est supérieur à 10, cela générera une erreur.

Mais nous devons également ajouter le message d'erreur lui-même. Ajoutez le message d'erreur suivant après le champ de formulaire Prénom.

```
{errors.firstName && <p>Veuillez vérifier le Prénom</p>}
```

Ici, cela générera une erreur. Alors, vérifions ce qui s'est passé.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screenshot-2021-10-09-105958.png)

Vous pouvez voir l'erreur après le champ Prénom qui dit "Veuillez vérifier le Prénom".

Répétez ce processus pour le Nom de famille.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screenshot-2021-10-09-110249.png)

Entrer plus de 10 caractères générera également une erreur.

Maintenant, nous devons ajouter une validation pour les champs email et mot de passe. Ici, nous allons utiliser une autre propriété appelée **`Pattern`**. Pattern contiendra une valeur d'expression régulière, et elle sera vérifiée par rapport aux données saisies dans le formulaire.

```
pattern: /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/ 
```

Voici à quoi ressemble un motif d'expression régulière. C'est difficile à lire, mais c'est un motif pour la validation des emails. Utilisons cela dans notre application.

```jsx
<Form.Field>
  <label>Email</label>
  <input
    placeholder='Email'
    type='email'
    {...register('email', {
      required: true,
      pattern:
        /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/,
    })}
  />
</Form.Field>
```

Dans le champ de formulaire Email, ajoutez ce motif.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screenshot-2021-10-09-110849.png)

Entrer un format d'email incorrect générera une erreur. Mais l'erreur disparaîtra lorsque nous entrerons le bon format.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screenshot-2021-10-09-110950.png)

Faisons de même pour le champ de formulaire Mot de passe. Pour le champ mot de passe, nous avons la condition qu'il doit contenir une lettre majuscule, une lettre minuscule, et le nombre de caractères doit être compris entre 6 et 15. Si notre valeur saisie ne respecte pas l'une de ces vérifications, cela générera une erreur.

```jsx
<Form.Field>
  <label>Mot de passe</label>
  <input
    placeholder='Mot de passe'
    type='password'
    {...register('password', {
      required: true,
      pattern: /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,15}$/,
    })}
  />
</Form.Field>
{
  errors.password && <p>Veuillez vérifier le Mot de passe</p>;
}

```

Maintenant, nos quatre champs de formulaire sont complets.

```jsx
import React from 'react';
import { Form, Button } from 'semantic-ui-react';
import { useForm } from 'react-hook-form';

export default function FormValidation() {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm();
  const onSubmit = (data) => {
    console.log(data);
  };
  return (
    <div>
      <Form onSubmit={handleSubmit(onSubmit)}>
        <Form.Field>
          <label>Prénom</label>
          <input
            placeholder='Prénom'
            type='text'
            {...register('firstName', { required: true, maxLength: 10 })}
          />
        </Form.Field>
        {errors.firstName && <p>Veuillez vérifier le Prénom</p>}
        <Form.Field>
          <label>Nom de famille</label>
          <input
            placeholder='Nom de famille'
            type='text'
            {...register('lastName', { required: true, maxLength: 10 })}
          />
        </Form.Field>
        {errors.lastName && <p>Veuillez vérifier le Nom de famille</p>}
        <Form.Field>
          <label>Email</label>
          <input
            placeholder='Email'
            type='email'
            {...register('email', {
              required: true,
              pattern:
                /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/,
            })}
          />
        </Form.Field>
        {errors.email && <p>Veuillez vérifier l'Email</p>}
        <Form.Field>
          <label>Mot de passe</label>
          <input
            placeholder='Mot de passe'
            type='password'
            {...register('password', {
              required: true,
              pattern: /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,15}$/,
            })}
          />
        </Form.Field>
        {errors.password && <p>Veuillez vérifier le Mot de passe</p>}
        <Button type='submit'>Soumettre</Button>
      </Form>
    </div>
  );
}

```

Voici le code complet pour référence. Et nous pouvons également ajouter un peu de style à nos messages d'erreur – quelque chose comme ceci, peut-être :

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screenshot-2021-10-09-111533.png)

## **Conclusion**

Maintenant, vous savez comment ajouter une validation dans les formulaires React. Notez que React Hook Form ne fonctionne que dans les composants fonctionnels, pas dans les composants de classe.

Vous pouvez consulter ma vidéo sur [Ajoutons une validation dans les formulaires en utilisant React et React Hook Form](https://www.youtube.com/watch?v=7Jc5t9XEQIg&t=904s&ab_channel=Cybernatico), qui est sur ma chaîne YouTube.

Et voici le code complet sur [GitHub](https://github.com/nishant-666/React-Form-Validation-) pour référence.

> Bon apprentissage.