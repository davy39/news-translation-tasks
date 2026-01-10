---
title: 3 Hooks React que votre prochain projet nécessite
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2022-02-16T15:39:06.000Z'
originalURL: https://freecodecamp.org/news/react-hooks-your-next-project-needs
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/3-react-hooks-your-next-project-needs.png
tags:
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: 3 Hooks React que votre prochain projet nécessite
seo_desc: 'Here are three custom hooks that will add essential functionality to your
  React projects in just a line of code.

  React hooks are powerful for their ability to give us reusable stateful features
  that are separate from our components.

  I’ve put together...'
---

Voici trois hooks personnalisés qui ajouteront des fonctionnalités essentielles à vos projets React en une seule ligne de code.

Les hooks React sont puissants pour leur capacité à nous offrir des fonctionnalités étatiques réutilisables qui sont séparées de nos composants.

J'ai rassemblé une courte liste de trois hooks React personnalisés qui valent la peine d'être utilisés dans presque tous les projets que vous réalisez.

## 1. Hook useFetch

Dans pratiquement toutes les applications que vous créez, vous allez récupérer des données depuis une API externe.

L'approche standard consiste à effectuer l'appel API dans `useEffect` et à le réaliser en utilisant l'API fetch, intégrée dans le navigateur.

```javascript
function BlogPosts() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("http://jsonplaceholder.typicode.com/posts")
      .then((response) => response.json())
      .then((data) => setData(data));
  }, []);
}
```

Non seulement ce code est assez répétitif pour effectuer la requête GET, la convertir en JSON et la définir dans l'état, mais il n'est pas réutilisable.

Si vous souhaitiez le réutiliser, vous devriez déclarer useState et useEffect dans ce composant également.

Enfin, notre code ne gère aucun état d'erreur ou de chargement, ce qui est nécessaire lors de la récupération de données à l'exécution dans notre client React.

Heureusement, le hook `useFetch` est une bien meilleure abstraction qui résout toutes ces considérations en une seule ligne de code.

Le seul code supplémentaire que nous devons ajouter est quelques conditionnelles qui gèrent nos états de chargement et d'erreur :

```javascript
import useFetch from "react-fetch-hook";

function BlogPosts() {
  const { isLoading, error, data } = useFetch('http://jsonplaceholder.typicode.com/posts');

  if (isLoading) return <div>Chargement...</div>;
  if (error) return <div>Erreur ! {error.status}</div>;

  // retourner les données ici...
}

```

Vous obtenez le même résultat, mais avec moins de code, une gestion des erreurs ajoutée et une meilleure expérience utilisateur (si vous utilisez un beau spinner de chargement).

Vous pouvez installer `useFetch` en exécutant :

```bash
npm install react-fetch-hook

```

Si vous voulez un hook tiers encore plus avancé pour effectuer vos requêtes de données (qui peut prendre en charge le rafraîchissement et la mise en cache de vos requêtes), regardez SWR et React Query.

## 2. Hook useForm

Écrire des formulaires dans React peut être fastidieux, car c'est répétitif et implique généralement beaucoup de code pour ajouter des fonctionnalités courantes comme la validation.

Voici à quoi ressemble un formulaire très basique dans React, où nous avons une seule entrée d'email et gérons la soumission du formulaire avec `handleSubmit`.

```javascript
import isEmail from "validator/lib/isEmail";

function EmailForm() {
  function handleSubmit(event) {
    event.preventDefault();
    const email = event.target.elements.email.value;
    if (isEmail(email)) {
      console.log("formulaire soumis : ", email);
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="email">Adresse Email</label>
      <input id="email" type="email" required />
      <button type="submit">Soumettre</button>
    </form>
  );
}
```

Mais remarquez que nous avons un code plus impératif, où nous devons utiliser `event.preventDefault()` pour dire à la page de ne pas se recharger, pour obtenir la valeur de l'email depuis l'objet `elements` de notre élément cible (le formulaire lui-même), et ensuite valider l'email en utilisant la bibliothèque `validator`.

Oui, nous validons la valeur de l'email qui est tapée, mais s'il y a une erreur de validation, nous devons en informer l'utilisateur.

L'utilisation du hook `useForm` de `@mantine/hooks` nous donne un hook personnalisé et réutilisable pour gérer tout l'état de notre formulaire et montrer facilement les erreurs à notre utilisateur.

```javascript
import { TextInput, Button } from "@mantine/core";
import { useForm } from "@mantine/hooks";
import isEmail from "validator/lib/isEmail";

export default function EmailForm() {
  const form = useForm({
    initialValues: { email: "" },
    errorMessages: { email: "L'email est requis" },
    validationRules: {
      email: (value) => isEmail(value),
    },
  });

  function handleSubmit(values) {
    console.log("formulaire soumis : ", values);
  }

  return (
    <form onSubmit={form.onSubmit(handleSubmit)}>
      <TextInput
        required
        label="Email"
        placeholder="Adresse Email"
        {...form.getInputProps("email")}
      />
      <Button style={{ marginTop: 10 }} type="submit">
        Soumettre
      </Button>
    </form>
  );
}
```

Simplement en appelant le hook `useForm` et en spécifiant quel doit être le message d'erreur et la validation pour chaque champ, la valeur `form` nous donne toutes les fonctionnalités dont nous avons besoin dans notre formulaire grâce à des fonctions d'assistance comme `getInputProps` et `onSubmit`.

Voici à quoi ressemble l'état de notre formulaire lorsque notre utilisateur ne fournit pas un email valide :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-15-at-11.52.19-AM.png)

> Notez que dans de nombreux cas, les entrées HTML fournissent toute la validation dont vous avez besoin pour des valeurs courantes comme les emails simplement en ajoutant l'attribut `required`.

Vous pouvez installer `useForm` en exécutant :

```bash
npm install @mantine/hooks

```

## 3. Hook useLocalStorage

Il est utile dans les applications React de pouvoir stocker l'état de l'utilisateur localement dans le navigateur.

Si nous avions une application de streaming vidéo comme YouTube, nous pourrions sauvegarder les préférences vidéo de l'utilisateur (comme la lecture automatique activée ou désactivée) ou leur progression vidéo dans le stockage local de leur navigateur.

La difficulté d'utiliser le stockage local, cependant, est que tous les types de données JavaScript doivent être convertis en chaînes de caractères simples.

Nous faisons souvent cela en utilisant `JSON.stringify`. Mais si nous voulons obtenir l'élément du stockage local et utiliser les données, il doit être reconverti dans son type de données d'origine. Nous faisons cela en utilisant `JSON.parse`.

Cela peut être assez délicat, surtout si nous construisons une application React rendue côté serveur comme Next.js qui ne peut pas toujours accéder au navigateur et donc aux API de fenêtre comme le stockage local.

Que pouvons-nous faire ?

Un hook très utile à utiliser est à nouveau de `@mantine/hooks` et s'appelle `useLocalStorageValue`.

Imaginons que nous créons un basculeur qui stocke un paramètre de lecture automatique pour les vidéos de nos utilisateurs, qui peut être défini sur "on" ou "off".

Tout ce que nous devons fournir pour `useLocalStorageValue` est la clé à laquelle nous voulons assigner notre valeur dans le stockage local et sa valeur par défaut.

Cela fonctionne exactement comme `useState` et nous donne une variable d'état et une fonction de définition pour la mettre à jour.

```javascript
import { useLocalStorageValue } from "@mantine/hooks";

export default function ToggleAutoplay() {
  const [autoplay, setAutoplay] = useLocalStorageValue({
    key: "autoplay",
    defaultValue: "on",
  });

  function toggleAutoplay() {
    setAutoplay((current) => (current === "on" ? "off" : "on"));
  }

  return (
    <button
      onClick={toggleAutoplay}
      style={{ backgroundColor: autoplay === "on" ? "green" : "red" }}
    >
      Lecture automatique {autoplay === "on" ? "On" : "Off"}
    </button>
  );
}
```

Dans notre exemple ici, cliquer sur le bouton bascule la lecture automatique vers sa valeur opposée et la couleur de fond passe au vert si "on" et au rouge sinon.

Mais surtout, la valeur est sauvegardée dans le navigateur de notre utilisateur, donc lorsqu'ils actualisent, leur dernier choix sauvegardé est conservé.

Vous pouvez installer `useLocalStorageValue` en exécutant :

```bash
npm install @mantine/hooks

```

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : Le React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*