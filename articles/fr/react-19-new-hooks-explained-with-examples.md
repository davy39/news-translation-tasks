---
title: React 19 – Nouveaux Hooks Expliqués avec des Exemples
subtitle: ''
author: Kunal Nalawade
co_authors: []
series: null
date: '2024-05-28T12:56:51.000Z'
originalURL: https://freecodecamp.org/news/react-19-new-hooks-explained-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/thumb.jpeg
tags:
- name: React
  slug: react
- name: React
  slug: reactjs
seo_title: React 19 – Nouveaux Hooks Expliqués avec des Exemples
seo_desc: 'Hi fellow readers! Web Development is a constantly evolving landscape.
  The whole ecosystem consists of different libraries and technologies. React is one
  of the most widely used libraries in web development.

  There are small releases every now and the...'
---

Bonjour chers lecteurs ! Le développement web est un paysage en constante évolution. Tout l'écosystème se compose de différentes bibliothèques et technologies. React est l'une des bibliothèques les plus largement utilisées dans le développement web.

Il y a des petites mises à jour de temps en temps. Cependant, cette année, l'équipe React a fait une annonce significative en introduisant une nouvelle version, React 19. Le 25 avril 2024, React a officiellement publié la version bêta de React 19 au public.

Cette version arrive avec une toute nouvelle série de fonctionnalités, ainsi que de nouveaux hooks. Dans cet article, nous allons discuter de quatre nouveaux hooks disponibles dans la nouvelle version :

* [useFormStatus](#heading-useformstatus)
  
* [useActionState](#heading-useactionstate)
  
* [useOptimistic](#heading-useoptimistic)
  
* [use](#heading-use)
  

## Implémentation Existante de la Gestion des Formulaires

Avant de passer au premier hook, voyons comment nous implémentons actuellement la gestion des formulaires dans React :

```javascript
import { submitAction } from "./actions";

const FormHandling = () => {
  const [name, setName] = useState("");
  const [pending, setPending] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();
    setPending(true);
    await submitAction({ name });
    setPending(false);
    setName("");
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={name}
        placeholder="Entrez votre nom"
        onChange={(e) => setName(e.target.value)}
      />
      <button type="submit">Soumettre</button>
      {pending && <p>Soumission de {name}...</p>}
    </form>
  );
};
```

Normalement, nous utilisons un formulaire contrôlé par état pour définir les données du formulaire et les utiliser pour les soumettre au serveur avec l'attribut `onSubmit` du formulaire. De plus, nous utilisons une variable d'état `pending` pour gérer les états de soumission en attente.

Les trois hooks suivants que j'ai présentés vont changer la façon dont nous gérons les formulaires.

## useFormStatus

Le hook `useFormStatus` donne des informations sur l'état du formulaire lors de la soumission du formulaire. Ce hook fait partie de React DOM, donc importez-le depuis `react-dom` :

```javascript
import {useFormStatus} from 'react-dom'
```

Ce hook peut être utilisé de la manière suivante :

```javascript
  const { pending, data } = useFormStatus();
```

Le hook ne prend aucun argument et retourne un objet contenant des informations sur l'état du formulaire. Il retourne :

* `pending`, qui est une valeur booléenne indiquant si le formulaire est en état d'attente.
  
* `data`, qui est un objet de type `[FormData](https://developer.mozilla.org/en-US/docs/Web/API/FormData)`, et contient les valeurs des champs du formulaire.
  

Ce hook ne peut être utilisé que dans un composant qui a un élément

comme parent. Il ne retourne des informations d'état que de l'élément formulaire parent et non de l'élément `<form>` rendu dans le même composant.

Le code suivant ne fonctionnera pas :

```javascript
const {pending, data} = useFormStatus()
return (
    <form action={submit}></form>
  );
```

Utilisons le même formulaire précédent et écrivons-le dans un composant séparé :

```javascript
import { submitAction } from "../../actions";
import { useFormStatus } from "react-dom";

const Form = () => {
  const { pending, data } = useFormStatus();

  return (
    <div>
      <input type="text" name="username" placeholder="Entrez votre nom" />
      <button disabled={pending} type="submit">
        Soumettre
      </button>
      {pending && <p>Soumission de {data?.get("username")}...</p>}
    </div>
  );
};

const FormStatusWithHooks = () => {
  return (
    <form
      action={async () => {
        await submitAction();
      }}
    >
      <Form />
    </form>
  );
};
```

Ici, au lieu d'utiliser `onSubmit`, nous utilisons la prop action de l'élément formulaire. Et nous avons utilisé l'objet `data` pour accéder aux champs du formulaire et les rendre.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1731049965919/b3e23267-8d1b-4d76-b996-8c7d965b96a5.png align="center")

*Rendu des données du formulaire avec état d'attente*

Vous pouvez utiliser n'importe quel nombre de formulaires à l'intérieur de l'élément parent `<form>` et obtenir l'état du formulaire avec le hook `useFormStatus`. Ainsi, vous n'avez pas besoin d'implémenter la même logique à chaque fois. Cela améliore la réutilisabilité du code.

## useActionState

`useActionState` peut être utilisé de la manière suivante :

```javascript
const [state, formAction] = useActionState(submitData, initialState);
```

Il prend les paramètres suivants :

* `submitData`, qui est la fonction appelée lorsque le formulaire est soumis. Cette fonction doit prendre deux paramètres : l'état actuel et un objet FormData.
  
* `initialState`, qui est la valeur initiale de l'état lorsque le formulaire n'est pas soumis.
  

Il retourne un tableau avec les éléments suivants :

* `state`, qui est l'état actuel rendu dans le composant. Cet état est égal à l'état initial.
  
* `formAction`, qui est la nouvelle action que vous pouvez passer à la prop action de votre élément formulaire. Cela exécute l'action que vous avez passée avec l'état actuel et retourne un nouvel état mis à jour.
  

Comprenons comment utiliser le hook avec le formulaire suivant :

```javascript
<form action={formAction}>
      <div>
        <input type="text" name="username" placeholder="Entrez votre nom" />
        <input type="number" name="age" placeholder="Entrez l'âge" />
        <button type="submit">Soumettre</button>
      </div>
    </form>
```

Ce formulaire soumet les informations de l'utilisateur, nom et âge, qui sont ajoutées à une liste d'utilisateurs stockée sous forme d'état. Utilisons le hook `useActionState` pour obtenir l'état :

```javascript
import { useActionState, useEffect } from "react";
import { submitActionWithCurrentState } from "../../actions";
const ActionStateComponent = () => {
  const [state, formAction] = useActionState(submitActionWithCurrentState, {
    users: [],
    error: null,
  });

return <form action={formAction}>...</form>
```

La méthode `submitActionWithCurrentState` retourne un nouvel état composé de la liste des utilisateurs modifiée et donne une erreur si un utilisateur avec le nom donné existe déjà. Affichons la liste des utilisateurs et l'erreur (le cas échéant) :

```javascript
<div className="error">{state?.error}</div>
      {state?.users?.map((user) => (
        <div key={user.username}>
          Nom : {user.username} Âge : {user.age}
        </div>
      ))}
```

Après avoir soumis le formulaire, le composant se réaffiche et met à jour l'état dans le composant.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1731050034809/e30a20be-aca2-4973-99ba-8cc6192657bb.png align="center")

*Liste des utilisateurs soumis stockés sous forme d'état*

Si vous essayez de soumettre un nom d'utilisateur existant, vous obtenez une erreur :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1731050059494/a5d51224-c6e4-43eb-b2ae-0ee4059d0b54.png align="center")

*Erreur si l'utilisateur existe déjà*

## useOptimistic

Comme son nom l'indique, `useOptimistic` met à jour l'interface utilisateur de manière optimiste pendant qu'une opération asynchrone est encore en cours. Lorsqu'un utilisateur soumet un formulaire qui modifie un élément de l'interface utilisateur, ce hook peut "optimistiquement" afficher le résultat attendu pendant que le formulaire est encore en cours de soumission.

* Si la soumission du formulaire réussit, l'interface utilisateur reste la même.
  
* Si la soumission du formulaire échoue, l'interface utilisateur revient à l'état précédent.
  

Cela vous permet de mettre à jour immédiatement l'interface utilisateur même si la soumission du formulaire prend du temps :

```javascript
const [optimisticState, setOptimisticState] = useOptimistic(actualState, updateFn);
```

Le hook `useOptimistic` prend les paramètres suivants :

* `actualState`, qui est la valeur de l'état optimiste lorsqu'aucune action n'est en attente.
  
* `updateFn` (facultatif), qui est une fonction prenant l'état actuel et la valeur passée à la méthode `setOptimisticState` et calcule l'optimisticState. Si ce paramètre n'est pas spécifié, l'état optimiste est égal à la nouvelle valeur.
  

Il retourne ce qui suit :

* `optimisticState`, qui est la valeur optimiste (temporaire) affichée pendant que l'action est en attente.
  
* `setOptimisticState`, qui est une fonction définissant l'état optimiste à une nouvelle valeur.
  

Prenons un formulaire qui effectue une opération asynchrone pour changer le titre de la page :

```javascript
import { useOptimistic, useState } from "react";

const OptimisticComponent = () => {
  const [title, setTitle] = useState("Titre");
  const [optimisticTitle, setOptimisticTitle] = useOptimistic(title);
  const [error, setError] = useState(null);
  const pending = title !== optimisticTitle;
  const handleSubmit = async (formData) => {
   
  };
  return (
    <div>
      <h2>{optimisticTitle}</h2>
      <p> {pending && "Mise à jour..."} </p>
      <form action={handleSubmit}>
        <input type="text" name="title" placeholder="Changer le Titre" />
        <button type="submit" disabled={pending}>
          Soumettre
        </button>
      </form>
      <div className="error">{error && error}</div>
    </div>
  );
};
```

Dans le code ci-dessus :

* Nous affichons la valeur optimiste du titre, qui est définie sur l'état `title` lorsqu'aucune action n'est en attente.
  
* Nous avons défini une variable d'attente qui est définie sur vrai si l'état actuel et optimiste ne correspondent pas. En fonction de cela, nous affichons un texte d'attente et désactivons le bouton.
  
* Nous affichons une erreur si l'opération asynchrone génère une erreur.
  

Maintenant, appelons notre fonction asynchrone qui résout ou rejette notre demande :

```javascript
import { submitTitle } from "../../actions";

const OptimisticComponent = () => {
  
  ...
  
  const handleSubmit = async (formData) => {
    setError(null);
    setOptimisticTitle(formData.get("title"));
    try {
      const updatedTitle = await submitTitle(formData);
      setTitle(updatedTitle);
    } catch (e) {
      setError(e);
    }
  };
  
  ...
  
};
```

Dans le code ci-dessus :

* Nous avons mis à jour les états comme nous l'avons fait initialement.
  
* Avant d'appeler l'opération asynchrone, nous définissons l'état optimiste sur le titre mis à jour que nous venons de soumettre.
  
* Si la promesse est rejetée, l'état optimiste revient à l'original, donc pas besoin de le définir à nouveau.
  

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1731050097373/a130fbe2-f3b4-4073-9330-4e38de8dfb4c.png align="center")

*Mise à jour du titre de manière optimiste*

## use

La méthode `use` n'a pas été publiée en tant que hook, mais en tant que partie de l'API React. Contrairement aux hooks React, `use` peut également être appelé à l'intérieur des instructions `if` et `for`. Cependant, `use` ne peut être appelé qu'à l'intérieur d'un Composant ou d'un Hook.

`use` vous permet de lire la valeur d'une [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) ou d'un [Context](https://react.dev/learn/passing-data-deeply-with-context) à l'intérieur d'un composant. Comprenons son utilisation dans la lecture des contextes et des promesses.

#### Lecture des contextes

Dans le cas des contextes, `use` fonctionne de manière similaire au hook [`useContext`](https://react.dev/reference/react/useContext). Il retourne la valeur fournie par le contexte à utiliser à l'intérieur du composant :

```javascript
import { createContext, use } from "react";
import "../../styles.css";

const ThemeContext = createContext(null);
const UseHookWithContext = () => {
  return (
    <ThemeContext.Provider theme="dark">
      <MyComponent />
    </ThemeContext.Provider>
  );
};

const MyComponent = () => {
  const theme = use(ThemeContext);
  return (
    <div className={`myContainer theme-${theme}`}>
      <h2>Bonjour !</h2>
    </div>
  );
};
```

Le code ci-dessus donne le résultat suivant :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1731050125728/19276d93-21ad-4694-8eb0-3f5f517235a7.png align="center")

*Thème sombre*

Contrairement à `useContext`, `use` offre plus de flexibilité puisqu'il peut également être utilisé de manière conditionnelle avec des instructions `if` :

```javascript
const CodeSnippet = ({canShow}) => {
    if(canShow) {
        const theme = use(ThemeContext)
        return <h2>Extrait de code affiché avec le thème {theme} </h2>
    }
    return null
}
```

#### Lecture des valeurs résolues des promesses

`use` retourne la valeur résolue de la promesse à utiliser à l'intérieur du composant. Il s'intègre avec l'API [Suspense](https://react.dev/reference/react/Suspense) pour afficher un message temporaire jusqu'à ce qu'une promesse soit résolue.

Prenons un composant client avec une promesse passée en tant que prop depuis un composant serveur :

```javascript
"use client";

import { Suspense } from "react";
import { ErrorBoundary } from "react-error-boundary";

const DataContainer = ({ dataPromise }) => {
  return (
      <Suspense fallback={<p>Récupération des données...</p>}>
        <DataComponent dataPromise={dataPromise} />
      </Suspense>
  );
};

const DataComponent = ({ dataPromise }) => {
  const data = use(dataPromise);
  return <div>{data && data}</div>;
};
```

Dans le code ci-dessus :

* La promesse créée dans un composant serveur est passée au composant client en tant que prop. Cela peut à son tour être passé à la méthode `use`. Cela permet au composant client de lire la valeur résolue de la promesse.
  
* L'API `Suspense` rend l'élément passé à la prop `fallback` pendant que la promesse est encore en attente.
  

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1731050154298/a5cc1b8f-63ba-400f-b42e-df1da7a81b3c.png align="center")

*Données affichées au clic sur le bouton*

En cas de rejet d'une promesse, il existe deux façons d'afficher une erreur aux utilisateurs :

1. Retourner un message d'erreur dans le bloc `catch` de la promesse et le traiter comme une promesse résolue :
  

```javascript
export function fetchData() {
  return new Promise((resolve, reject) => {
    ...
    // ...
    
  }).catch((err) => err);
}
```

2. Envelopper le composant avec un [ErrorBoundary](https://react.dev/reference/react/Component#catching-rendering-errors-with-an-error-boundary) :
  

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1731050189144/2aa97ad6-0da9-4ee2-8ba1-5770d8e66156.png align="center")

*Limite d'erreur rendue lorsque la promesse est rejetée*

Vous pouvez trouver le code complet dans le CodeSandbox [ici](https://codesandbox.io/p/sandbox/gracious-haslett-4qdzn4?file=%2Fsrc%2Findex.js&from-embed=). N'hésitez pas à le forker et à l'explorer.

%[https://codesandbox.io/embed/4qdzn4?view=preview&module=%2Fsrc%2FApp.js] 

Ce n'est pas la fin. React 19 a beaucoup plus à offrir. Vous pouvez consulter toutes les nouvelles fonctionnalités dans la [documentation](https://react.dev/blog/2024/04/25/react-19).

Actuellement, React 19 est encore en version bêta, donc ne l'utilisez pas pour les systèmes de production pour l'instant. Cependant, vous pouvez installer la version canary de React 19 en ajoutant les dépendances suivantes dans votre fichier `package.json` et en exécutant `npm i` :

```javascript
"dependencies": {
    "react": "canary",
    "react-dom": "canary",
  },
```

## Conclusion

L'équipe React a introduit plusieurs hooks utiles qui amélioreront la commodité pour les développeurs.

Les trois premiers hooks : `useFormStatus`, `useActionState` et `useOptimistic` changent la façon dont nous gérons les formulaires. Le hook `use` rend très pratique l'obtention de la valeur résolue d'une promesse à l'intérieur d'un composant.

Dans cet article, j'ai expliqué la syntaxe de chaque hook et démontré leurs exemples d'utilisation. Cela vous aidera certainement à comprendre ces hooks et comment les utiliser. J'espère que cela vous aidera dans vos futurs projets.

Si vous avez des questions ou besoin de clarifications supplémentaires, faites-le moi savoir. Vos retours sont toujours appréciés et valorisés ! Connectez-vous avec moi sur Twitter pour plus de mises à jour et de discussions. Merci pour votre lecture, et j'ai hâte de vous retrouver la prochaine fois !