---
title: Comment gérer les formulaires dans Next.js avec les Server Actions et Zod pour
  la validation
subtitle: ''
author: Chidera Humphrey
co_authors: []
series: null
date: '2024-11-22T16:47:42.519Z'
originalURL: https://freecodecamp.org/news/handling-forms-nextjs-server-actions-zod
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1732137561737/293681e0-d2f4-4d88-9fbe-f7e5e9113554.png
tags:
- name: Next.js
  slug: nextjs
- name: Frontend Development
  slug: frontend-development
- name: form validation
  slug: form-validation
seo_title: Comment gérer les formulaires dans Next.js avec les Server Actions et Zod
  pour la validation
seo_desc: 'Forms are essential in modern websites, as they help you collect your users’
  information. So knowing how to handle forms properly is crucial when you’re building
  web applications.

  In this article, you will learn how to handle forms in Next.js using s...'
---

Les formulaires sont essentiels dans les sites web modernes, car ils aident à collecter les informations de vos utilisateurs. Savoir comment gérer les formulaires correctement est donc crucial lorsque vous construisez des applications web.

Dans cet article, vous apprendrez comment gérer les formulaires dans Next.js en utilisant les server actions et zod.

## Table des matières

* [Introduction aux Server Actions dans Next.js](#introduction-aux-server-actions-dans-nextjs)

* [Introduction à Zod pour la validation](#introduction-a-zod-pour-la-validation)

* [Comment construire le composant de formulaire de contact](#heading-comment-construire-le-composant-de-formulaire-de-contact)

* [Comment créer les Server Actions et valider les données du formulaire avec Zod](#heading-comment-creer-les-server-actions-et-valider-les-donnees-du-formulaire-avec-zod)

* [Comment intégrer la Server Action dans notre formulaire de contact](#heading-comment-integrer-la-server-action-dans-notre-formulaire-de-contact)

* [Conclusion](#conclusion)

## Prérequis et configuration du projet

Pour ce tutoriel, je suppose que vous connaissez JavaScript et comment configurer un projet Next.js (je ne vais pas passer par cette configuration ici).

Si vous n'avez pas encore configuré votre projet Next.js, utilisez la commande suivante et suivez les invites :

```sh
npx create-next-app
```

Voici ce que nous allons construire dans ce tutoriel :

![formulaire fonctionnel](https://cdn.hashnode.com/res/hashnode/image/upload/v1732051133068/960bd90a-cb22-4e8b-86e2-fdb78b5cf330.gif align="center")

**Note** : ce tutoriel se concentre principalement sur la logique et non sur le design. Pour le design complet, vous pouvez visiter le dépôt GitHub que j'ai lié à la fin.

## Introduction aux Server Actions dans Next.js

Alors, qu'est-ce que les server actions ? Les server actions sont exactement ce à quoi elles ressemblent : des actions ou des fonctions qui s'exécutent sur le serveur. Avec les server actions, vous pouvez faire des appels à des API externes ou récupérer des données depuis une base de données.

Avant Next.js 13, vous deviez utiliser des routes pour gérer les appels API et les soumissions de formulaires. Cela était complexe et fastidieux.

Mais l'introduction des server actions vous permet de communiquer avec des API externes et des bases de données directement dans vos composants Next.js.

En s'exécutant sur le serveur, les server actions permettent un traitement sécurisé des données, atténuant les risques de sécurité.

Les server actions sont également utiles pour gérer les formulaires car elles vous permettent de communiquer directement avec votre serveur et de limiter l'exposition des informations d'identification importantes au client.

Il existe deux façons de créer des server actions :

* La première méthode consiste à utiliser la directive `"use server"` au niveau supérieur d'une fonction. Vous ne pouvez utiliser cette méthode qu'à l'intérieur d'un composant serveur. L'utiliser à l'intérieur d'un composant client entraînera une erreur.

Par exemple :

```ts
async function getPosts() {
  "use server"; // cela fait de getPosts une server action

  // reste du code
}
```

* L'autre méthode consiste à créer un fichier séparé et à ajouter **"use server"** en haut du fichier. Cela garantit que toute fonction asynchrone exportée depuis le fichier est une server action.

```ts
// action.ts

"use server";

export async function getPosts() {
  const res = await fetch("https:...");
  const data = res.json();

  return data;
}
```

Dans l'exemple de code ci-dessus, `getPosts` est une server action.

## Introduction à Zod pour la validation

Zod est une bibliothèque de validation que vous pouvez utiliser pour valider les entrées de formulaire côté serveur. Cela garantit la cohérence entre le client et le serveur.

Zod est une bibliothèque d'abord TypeScript, ce qui signifie qu'elle offre une sécurité de type dès le départ.

Pour installer Zod dans votre application Next.js, utilisez la commande suivante :

```sh
npm install zod
```

Au cœur de la bibliothèque Zod se trouvent les schémas. Vous pouvez utiliser des schémas pour valider les entrées.

Voici comment définir un schéma :

```ts
import { z } from "zod";

const contactSchema = z.object({
  name: z.string().min(2, { message: "Le nom doit comporter au moins 2 caractères" }),
  email: z.string().email({ message: "Adresse e-mail invalide" }),
  message: z
    .string()
    .min(10, { message: "Le message doit comporter au moins 10 caractères" }),
});
```

Dans le `contactSchema`, nous spécifions que :

* `name` est de type `string` et doit comporter au moins 2 caractères,

* `email` est de type `string` et `email`, et

* `message` est de type `string` et doit comporter au moins 10 caractères.

La propriété `message` est ce qui sera affiché à l'écran lorsque tout ou une partie de la validation échoue.

Dans la section suivante, nous allons construire le formulaire de contact.

## Comment construire le composant de formulaire de contact

Dans cette section, nous allons construire l'interface utilisateur du formulaire de contact.

À l'intérieur du répertoire `app`, créez un dossier appelé "components".

À l'intérieur du dossier `components`, créez un nouveau fichier, `contactForm.tsx`, et ajoutez le code suivant :

```typescript
"use client";

function ContactForm() {
  return (
    <form action="">
      <input type="text" name="name" placeholder="Entrez votre nom" />
      <input type="email" name="email" placeholder="Entrez votre email" />
      <textarea name="message" cols={30} rows={10} placeholder="Tapez votre message"></textarea>
      <button type="submit">Envoyer le message</button>
    </form>
  );
}

export default ContactForm;
```

Dans le code ci-dessus, nous créons un simple formulaire de contact. Nous en avons fait un composant client, vous verrez pourquoi dans un instant.

Importez le composant `ContactForm` dans votre fichier `page.tsx` :

```typescript
import ContactForm from "./components/contactForm.tsx";

function Home() {
  return (
    <div>
      <h2>Formulaire de contact</h2>
      <ContactForm />
    </div>
  );
}
```

Vous devriez avoir quelque chose comme ceci :

![image du formulaire de contact](https://cdn.hashnode.com/res/hashnode/image/upload/v1732048786231/694ac568-9d71-4597-ba61-962483740320.png align="center")

Ensuite, nous allons valider les données de notre formulaire en utilisant zod.

## Comment créer les Server Actions et valider les données du formulaire avec Zod

Dans cette section, nous allons créer notre server action et valider les entrées de notre formulaire avec zod.

Dans le dossier **app**, créez un autre dossier, `api`.

À l'intérieur du dossier `api`, créez un fichier appelé `action.ts` et collez le code suivant :

```ts
"use server";

import { z } from "zod";

const contactFormSchema = z.object({
  name: z.string().trim().min(1, { message: "Le champ nom est requis" }),
  email: z.string().email({ message: "Adresse e-mail invalide" }),
  message: z.string().trim().min(1, { message: "Veuillez taper un message" }),
});

export async function sendEmail(prevState: any, formData: FormData) {
  const contactFormData = Object.fromEntries(formData);
  const validatedContactFormData = contactFormSchema.safeParse(contactFormData);


  if (!validatedContactFormData.success) {
    const formFieldErrors =
      validatedContactFormData.error.flatten().fieldErrors;

    return {
      errors: {
        name: formFieldErrors?.name,
        email: formFieldErrors?.email,
        message: formFieldErrors?.message,
      },
    };
  }

  return {
    success: "Votre message a été envoyé avec succès !",
  };
}
```

Dans le code ci-dessus, nous avons défini un `contactFormSchema` pour valider les entrées de notre formulaire.

La fonction `sendEmail` (qui est notre server action) accepte deux arguments :

* `prevState` qui sera utilisé pour afficher nos messages d'erreur et de succès, et

* `formData` qui sont les entrées de notre formulaire

FormData permet à notre fonction d'avoir accès aux champs du formulaire sans utiliser `useState` et il repose sur l'attribut `name`.

Nous utilisons `Object.fromEntries()` pour convertir le `formData` brut en un objet JavaScript régulier et nous le stockons dans la variable `contactFormData`.

Ensuite, nous validons le `contactFormData` en utilisant la méthode `safeParse()` de notre schéma zod, `contactFormSchema`.

En tant que bonne pratique de programmation, nous retournons tôt en vérifiant si la validation échoue. Si la validation échoue, nous retournons un objet avec une propriété `error`, qui est un objet contenant le message d'erreur de chaque champ de formulaire.

`formFieldsError` est assigné à la valeur de l'objet d'erreur de zod, qui contient le message d'erreur de chaque champ de formulaire.

Si tout se passe bien, nous retournons simplement un objet avec une propriété `success`.

**Note** : c'est ici que vous envoyez le message à votre email en utilisant le fournisseur de service email de votre choix. Pour l'article, nous retournons simplement un objet.

Dans la section suivante, nous allons intégrer la server action dans notre formulaire de contact.

## Comment intégrer la Server Action dans notre formulaire de contact

Dans cette section, nous allons intégrer la server action dans notre formulaire de contact.

Accédez au fichier `contactForm.tsx` et remplacez le contenu par le code suivant :

```typescript
"use client";

import { useFormState, useFormStatus } from "react-dom";
import { sendEmail } from "../api/action";

const initialState = {
  success: "",
  errors: {
    name: "",
    email: "",
    message: "",
  }
};

function ContactForm() {
  const [state, formAction] = useFormState(sendEmail, initialState);

  return (
    <div>
      <div className="py-6">
        <form action={formAction}>
          <div className="mb-4">
            <label htmlFor="name">Votre nom</label>
            <br />
            <input
              type="text"
              name="name"
              id="name"
              // required
              className="border w-full md:w-3/4 py-2 pl-2 rounded-lg rounded-l-lg block md:inline focus:outline-slate-500 border-gray-500"
              placeholder="Entrez votre nom..."
            />
            {state.errors?.name && (
              <p className="text-red-500">{state.errors.name}</p>
            )}
          </div>
          <div className="mb-4">
            <label htmlFor="email">Votre email</label>
            <br />
            <input
              type="email"
              name="email"
              id="email"
              // required
              className="border w-full md:w-3/4 py-2 pl-2 rounded-lg rounded-l-lg block md:inline focus:outline-slate-500 border-gray-500"
              placeholder="Entrez votre email..."
            />
            {state.errors?.email && (
              <p className="text-red-500">{state.errors.email}</p>
            )}
          </div>
          <div>
            <label htmlFor="message">Message</label>
            <br />
            <textarea
              name="message"
              id="message"
              // required
              cols={100}
              rows={10}
              className="border w-full md:w-3/4 py-3 pl-2 rounded-lg focus:outline-slate-500 border-gray-500"
              placeholder="Entrez votre message..."
            ></textarea>
            {state.errors?.message && (
              <p className="text-red-500">{state.errors.message}</p>
            )}
          </div>
          <SubmitButton />
        </form>
      </div>
      {state?.success && <p className="text-green-600">{state.success}</p>}
    </div>
  );
}

export default ContactForm;

function SubmitButton() {
  const { pending } = useFormStatus();

  return (
    <button
      type="submit"
      disabled={pending ? true : false}
      className="bg-green-600 text-white font-semibold px-3 py-2 rounded-lg"
    >
      {pending ? (
        <span>
          Soumission <RiLoader5Fill className="animate-spin" />
        </span>
      ) : (
        "Soumettre"
      )}
    </button>
  );
}
```

Dans le code mis à jour ci-dessus, nous avons importé deux hooks : `useFormState` et `useFormStatus` depuis "react-dom" et `sendEmail` depuis "api/action.ts".

Ensuite, nous avons créé une variable `initialState` pour contenir notre état initial. Cela sera utilisé dans le hook `useFormState`.

`initialState` est un objet avec :

* une propriété `success` pour le message de succès de notre server action, et

* un objet `errors`, qui est égal à l'objet `errors` que nous retournons dans notre server action si la validation échoue.

À l'intérieur de notre composant `ContactForm`, nous utilisons le hook `useFormState`. Ce hook accepte deux arguments : une server action et un état initial et retourne un tableau avec deux valeurs : l'état actuel et `formAction`.

`formAction` sera passé dans la propriété `action` de l'élément **form**. Cela gérera la soumission de notre formulaire, qui incorpore la validation zod.

Sous chaque champ de formulaire, nous rendons conditionnellement le message d'erreur de chaque champ de formulaire respectivement.

Sous l'élément **form**, nous rendons le message de succès si le formulaire a été soumis avec succès.

Le bouton de soumission est placé dans un composant différent, `SubmitButton`, afin que nous puissions utiliser le hook `useFormStatus`.

Le hook `useFormStatus` retourne un objet avec une propriété `pending`, que nous pouvons utiliser pour désactiver le bouton de soumission lorsque le formulaire est soumis.

En supposant que tout s'est bien passé, vous devriez avoir un formulaire de contact fonctionnel comme ceci :

![formulaire fonctionnel](https://cdn.hashnode.com/res/hashnode/image/upload/v1732051093066/c6cd1da7-fe24-4eea-85db-a6845efc501d.gif align="center")

Félicitations ! Vous venez de créer un formulaire de contact en utilisant les server actions et la bibliothèque de validation zod.

## Conclusion

Dans cet article, vous avez appris ce que sont les server actions et comment utiliser la bibliothèque zod. Vous avez également utilisé les server actions et zod pour construire un formulaire de contact.

Les server actions ne sont pas limitées à la soumission de formulaires et peuvent également être utilisées pour récupérer des données depuis des API externes et des bases de données.

Vous pouvez en apprendre plus avec ces ressources :

* [documentation zod](https://zod.dev/)

* [documentation server action](https://nextjs.org/docs/app/building-your-application/data-fetching/server-actions-and-mutations)

Voici le [dépôt GitHub](https://github.com/DeraCodings/server-action-zod) du projet complet.