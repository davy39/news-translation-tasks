---
title: React 19 Actions – Comment simplifier la soumission de formulaires et les états
  de chargement
subtitle: ''
author: Shruti Kapoor
co_authors: []
series: null
date: '2024-07-02T21:29:47.000Z'
originalURL: https://freecodecamp.org/news/react-19-actions-simpliy-form-submission-and-loading-states
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/React--1-.jpg
tags:
- name: React
  slug: react
seo_title: React 19 Actions – Comment simplifier la soumission de formulaires et les
  états de chargement
seo_desc: 'React 19 introduces Actions, which are asynchronous functions. Actions
  are helpful in making form submissions easier. This tutorial dives into what Actions
  are and how to use them.

  You''ll learn about:


  The new React 19 feature, Actions

  The new React ...'
---

React 19 introduit les Actions, qui sont des fonctions asynchrones. Les Actions sont utiles pour simplifier la soumission de formulaires. Ce tutoriel explore ce que sont les Actions et comment les utiliser.

Vous apprendrez :

1. La nouvelle fonctionnalité de React 19, les Actions
2. Les nouveaux hooks de React 19, `useActionState` et `useFormStatus`
3. Comment convertir un formulaire React 18 en un formulaire React 19

J'ai également réalisé une [version vidéo de cet article](https://www.youtube.com/watch?v=ExZUdkfu-KE&t=443s) si vous souhaitez apprendre de cette manière également.

## Fonctionnalité : React Actions

Pour comprendre les Actions, examinons d'abord comment nous gérons les formulaires aujourd'hui. Dans React 18 et les versions antérieures, nous soumettons les formulaires en utilisant la fonction `handleSubmit` dans un bouton. Voici un formulaire simple avec un champ de saisie `name` :

```jsx
// Soumission de formulaire dans React 18
console.info('Formulaire React 18');

const [name, setName] = useState('');
const [isPending, setIsPending] = useState(false);

const handleChange = (event) => {
  setName(event.target.value);
};

const handleSubmit = (event) => {
  event.preventDefault();
  setIsPending(true);
  setTimeout(() => {
    // appel API
    setIsPending(false);
  }, 500);
};

return (
  <form>
    <input type="text" name="name" onChange={handleChange} />
    {isPending ? <p>Chargement...</p> : <p>Bonjour dans React 18, {name}</p>}
    <button onClick={handleSubmit} disabled={isPending}>
      Mettre à jour
    </button>
  </form>
);

```

Dans ce code, nous faisons ce qui suit :

1. Ajout d'un état de chargement : Nous utilisons une variable `isPending` pour suivre manuellement l'état de chargement.
2. Soumission du formulaire : Le formulaire est soumis en utilisant le gestionnaire d'événements `handleSubmit` attaché à l'événement `onClick` du bouton.
3. Capture de la valeur soumise : La fonction `handleChange` capture la valeur soumise et la stocke dans des variables d'état.

## Qu'est-ce que les React Actions ?

Avec React 19, la gestion des formulaires devient plus facile avec les Actions, inspirées par des frameworks tels que Remix. Une caractéristique clé est l'utilisation améliorée de `startTransition` pour gérer les états en attente.

`startTransition` a été introduit dans React 18, permettant aux développeurs de marquer certaines mises à jour comme moins urgentes.

Dans React 19, `startTransition` peut maintenant gérer des fonctions asynchrones, le rendant encore plus puissant pour gérer les tâches asynchrones et améliorer l'expérience utilisateur lors de la soumission de formulaires.

```js
const [isPending, startTransition] = useTransition();

const handleSubmit = () => {
  startTransition(async () => {
    const error = await updateName(name);
    if (error) {
      setError(error);
      return;
    }
    redirect('/path');
  });
};

```

Cette fonction asynchrone à l'intérieur de `startTransition` est appelée une Action. Ce qui rend les actions intéressantes, c'est qu'elles peuvent être utilisées directement pour soumettre des formulaires comme ceci :

```html
<form action="{actionFn}">...</form>

```

Ce format peut vous sembler familier si vous avez de l'expérience avec PHP.

## Comment créer une React Action

Pour créer une fonction asynchrone, nous pouvons utiliser un nouveau hook introduit dans React 19 appelé `useActionState`. Nous appelons ce hook et passons une fonction d'action et un état initial. Ce hook retourne l'état mis à jour et une action de formulaire `actionFn`, qui peut être utilisée pour configurer un formulaire.

```js
const [state, actionFn] = useActionState(submitAction, { name: '' });

```

Maintenant, avec cela configuré avec le formulaire, nous avons ce qui suit :

```jsx
<form action={actionFn}>
  <input type="text" name="name" />

  <button type="submit" disabled="{pending}">
    Mettre à jour
  </button>
</form>

```

Pour ajouter un état de chargement, nous pouvons utiliser un nouveau hook introduit dans React 19 appelé `useFormStatus`.

```js
const { pending, data, method, action } = useFormStatus();

```

Ce hook fournit des informations sur l'état du formulaire. L'état `pending` indique si le formulaire est en cours de soumission, et `data` est un objet `FormData` contenant les données soumises. Nous utilisons cet état en attente pour afficher un chargeur.

Mais il y a un point important : ce hook ne peut être utilisé que dans un composant enfant, et non dans le formulaire lui-même. Nous devons donc créer des composants enfants `SubmitButton` et `Loader` pour récupérer un état `pending` :

```js
function Loader() {
  const { pending } = useFormStatus();
  return <div>{pending && "Chargement..."}</div>;
}

function SubmitButton() {
  const { pending } = useFormStatus();
  return (
    <button type="submit" disabled={pending}>
      Mettre à jour
    </button>
  );
}

....

return(
<form action={formAction}>
      <input type="text" name="name" />
      <Loader />
      <SubmitButton />
    </form>
)

```

Nous pouvons également capturer des informations utiles sur les données soumises au formulaire en les récupérant à partir de l'état retourné par `useActionState`.

```js
const [state, formAction] = useActionState(submitAction, { name: '' });

```

Voici donc le formulaire final :

```jsx
function Loader() {
  const { pending } = useFormStatus();
  return <div>{pending && 'Chargement...'}</div>;
}

function SubmitButton() {
  const { pending } = useFormStatus();
  return (
    <button type="submit" disabled={pending}>
      Mettre à jour
    </button>
  );
}

function Name({ name }) {
  return <p>Bonjour dans React 19 {name}</p>;
}

function App() {
  console.info('Formulaire React 19');

  const [state, formAction] = useActionState(submitAction, { name: '' });

  return (
    <form action={formAction}>
      <input type="text" name="name" />
      <Loader />
      <SubmitButton />
      <Name name={state?.name} />
    </form>
  );
}

```

Comparez cela avec le formulaire React 18 en haut de cet article pour voir la différence.

## Conclusion

En utilisant les actions ainsi que des hooks comme `useActionState` et `useFormStatus`, nous pouvons facilement gérer les états de formulaire, capturer les données soumises et fournir des retours réactifs aux utilisateurs lors de la soumission de formulaires pour montrer les états en attente.

Je suis enthousiaste à l'idée de cette expérience améliorée de gestion des formulaires dans React 19, et j'ai hâte de supprimer les `handleSubmits`, `useState` et états `pending` inutiles.

Dans mon prochain article, je discuterai d'une autre nouvelle fonctionnalité passionnante de React : le React Compiler. Cet outil mémoïse automatiquement, éliminant le besoin de `useMemo` et `useCallback`. Restez à jour et recevez l'article directement dans votre boîte de réception en vous abonnant à ma newsletter.

<iframe src="https://shrutikapoor.substack.com/embed" width="480" height="320" style="border:1px solid #EEE; background:white;" frameborder="0" scrolling="no"></iframe>