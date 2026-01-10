---
title: Comment créer une application React en 2024
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2024-01-26T13:44:45.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-react-app-in-2024
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/build-react-app-2024.png
tags:
- name: Developer Tools
  slug: developer-tools
- name: projects
  slug: projects
- name: React
  slug: react
seo_title: Comment créer une application React en 2024
seo_desc: 'In 2024, there are more ways than ever to get your React projects started.
  But which one should you choose?

  In this article, I''m going to break down all of the major ways you can use to create
  a React app and which one you should pick based off of yo...'
---

En 2024, il existe plus de façons que jamais de démarrer vos projets React. Mais laquelle devriez-vous choisir ?

Dans cet article, je vais décomposer toutes les principales méthodes que vous pouvez utiliser pour créer une application React et laquelle vous devriez choisir en fonction des besoins de votre projet.

Je vais également inclure un guide rapide à la fin pour vous montrer exactement comment choisir entre chacune d'elles selon le type de projet que vous construisez.

Commençons !

## ❌ Pourquoi vous ne devriez pas utiliser Create React App

En 2023, l'outil Create React App a été déprécié, ce qui signifie qu'il n'est plus maintenu. Create React App a été la méthode de référence pour créer un nouveau projet React, mais il a été détrôné par un certain nombre d'alternatives différentes.

Pour cette raison, Create React App n'est pas une option que je recommanderais pour créer un nouveau projet React en 2024.

## 💨 Comment créer une application React avec Vite

Vous vous demandez peut-être : "Quel est un bon remplacement pour Create React App ?" Cette option est Vite.

Vite est idéal pour créer des projets React rendus côté client qui s'exécutent exclusivement dans le navigateur.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/vite.png)
_Page d'accueil de la documentation de Vite_

Pour lancer un nouveau projet React avec Vite, vous n'avez qu'à exécuter une seule commande :

```bash
npm create vite@latest my-react-app -- --template react
```

L'avantage de Vite est, comme son nom l'indique, qu'il est beaucoup plus rapide que pratiquement toutes les alternatives. Vite brille particulièrement par la rapidité avec laquelle il s'exécute en développement.

Vite est peu opinionné, cependant, ce qui signifie que vous devrez probablement installer une suite de bibliothèques tierces pour des fonctionnalités de base, comme le routage et la récupération de données.

Si votre application n'a pas de serveur ou si vous utilisez une API externe et qu'elle n'a pas besoin de rendu côté serveur, Vite est un choix parfait.

De plus, Vite est livré avec son propre fichier de configuration, **vite.config.js**, qui peut nécessiter de lire la documentation afin de configurer des éléments tels que les variables d'environnement, les options de build et les options d'image.

## 🧞 Comment créer une application React avec Next.js

Si vous cherchez un moyen de construire une application React qui vous offre une expérience de type single-page app (SPA) mais avec un rendu côté serveur et des composants serveur, Next.js est votre choix.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/nextjs.png)
_Page d'accueil de la documentation de Next.js_

Next.js est actuellement la seule option qui propose des composants serveur, ce qui vous permet de marquer un composant comme `async` et d'utiliser `await` dans une opération sur le serveur.

```tsx
async function getData() {
  const res = await fetch('https://api.example.com/...');
  return res.json();
}
 
export default async function Page() {
  const data = await getData();
 
  return <main>{data}</main>;
}
```

L'avantage des composants serveur est que vous n'avez pas à afficher un indicateur de chargement dans votre application avant de récupérer les données. Les composants serveur vous permettent d'envoyer beaucoup moins de JavaScript au client, ce qui conduit à des temps de chargement plus rapides pour vos utilisateurs.

Les composants serveur nécessitent cependant que vous ayez un serveur, ce qui signifie qu'ils ne peuvent pas être déployés aussi simplement qu'une application React rendue côté client créée avec Vite.

Next.js est puissant car il propose de nombreuses fonctionnalités intégrées, telles qu'un routage basé sur des fichiers, l'optimisation des images et le chargement des polices, pour n'en nommer que quelques-unes.

Next.js vous permet également d'utiliser des actions serveur, une nouvelle fonctionnalité React qui vous permet d'exécuter du code serveur en appelant une fonction.

```tsx
// Composant Serveur
export default function Page() {
  // Action Serveur
  async function create() {
    'use server'
 
    // ...
  }
 
  return (
    // ...
  )
}
```

Next.js dispose également de gestionnaires de routes, qui vous permettent de faire des requêtes HTTP vers un point de terminaison API. C'est quelque chose que les applications React rendues côté client ne peuvent pas faire, car il n'y a pas de serveur.

Avec tous les avantages de Next.js, il présente une courbe d'apprentissage plus raide. Il existe un certain nombre de concepts spécifiques à Next.js qui peuvent sembler aller à l'encontre de certains concepts React que vous avez déjà appris.

Par exemple, dans les composants serveur, vous ne pouvez pas utiliser les Hooks React. Cela signifie que vous devez vous appuyer sur des modèles tels que le stockage de l'état dans l'URL.

Malgré la courbe d'apprentissage, Next.js est le framework React le plus populaire et est utilisé pour construire des applications React impressionnantes qui alimentent des startups à des entreprises du Fortune 500.

Si vous voulez créer quelque chose d'impressionnant avec React, vous pouvez certainement le faire avec Next.js.

## 🏃 Comment créer une application React avec Remix

Remix, comme Next.js, est un framework basé sur React qui se concentre différemment sur les standards du web pour offrir une meilleure expérience utilisateur. Remix vous permet également d'écrire du code React côté serveur et côté client.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/remix.png)
_Page d'accueil de la documentation de Remix_

Remix se targue de servir du contenu statique et dynamique plus rapidement que Next.js. Cela signifie qu'il est tout aussi bon pour construire des applications full-stack que des sites web statiques.

Au lieu de composants serveur et d'actions serveur, Remix a simplement des actions. Les actions vous permettent de gérer les mutations de données sur votre serveur, ce qui inclut tout ce qui n'est pas une requête GET. Les actions sont simplement des fonctions avec le nom action.

Pour obtenir des données, vous utilisez des fonctions simples appelées loaders. React Remix utilise React Router sous le capot. Donc, si vous êtes à l'aise avec React Router, vous vous sentirez probablement à l'aise avec Remix également.

```tsx
export async function loader() {
  return json(await fakeGetTodos());
}

export default function Todos() {
  const data = useLoaderData<typeof loader>();
  return (
    <div>
      <TodoList todos={data} />
      <Form method="post">
        <input type="text" name="title" />
        <button type="submit">Créer Todo</button>
      </Form>
    </div>
  );
}
```

Remix est un peu plus stable que Next.js et a une courbe d'apprentissage moins raide, vous permettant toujours de construire des applications tout aussi impressionnantes, le seul inconvénient étant qu'il n'est pas presque aussi populaire que Next.js. Il n'a donc pas le même soutien communautaire et les mêmes bibliothèques autour de lui.

Mais si vous voulez quelque chose avec un rendu côté serveur et un rendu côté client, Remix reste une excellente option pour construire votre prochain projet React.

## 🚀 Comment créer une application React avec Astro

La nouvelle façon de construire un projet React est définitivement la plus performante. Les applications React peuvent également être construites en utilisant un framework appelé Astro.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/astro.png)
_Page d'accueil de la documentation d'Astro_

L'objectif d'Astro est de livrer du contenu aux utilisateurs rapidement grâce à ce qu'on appelle l'"architecture d'îlots".

En bref, cela signifie que JavaScript est chargé uniquement lorsque l'utilisateur en a besoin, ce qui permet une expérience utilisateur beaucoup plus optimale. Si vous voulez le site web le plus rapide possible, je vous recommande vivement de regarder Astro.

Astro supporte le rendu côté serveur et est idéal pour les sites web axés sur le SEO qui sont largement statiques. Cependant, ce qui est intéressant avec Astro, c'est qu'il peut également exécuter du code sur le serveur si vous le choisissez. Il n'est pas aussi populaire de construire des applications full-stack entièrement dynamiques avec Astro, mais c'est possible de le faire.

Astro est également très flexible car il n'est même pas lié à React. Vous n'avez pas besoin d'utiliser React pour construire une application Astro, et vous pouvez utiliser React aux côtés d'autres frameworks tels que Vue et Svelte dans la même application.

Si vous construisez un site web qui contient des articles ou du contenu utilisant markdown ou MDX, Astro devrait être votre premier choix. Il utilise une fonctionnalité appelée "collections" pour décrire toutes les données dans vos fichiers markdown afin que vous sachiez exactement quel contenu va être rendu dans vos composants React.

Astro gagne rapidement en popularité, et c'est probablement le meilleur choix si vous êtes intéressé par la création d'un site web statique qui n'a pas besoin de base de données ou d'authentification, ou d'un site web qui est largement statique.

## 🤔 Alors, que devrais-je choisir ?

Si vous avez lu jusqu'à ce point et que vous essayez toujours de déterminer quel framework serait le meilleur pour construire un projet React en 2024, voici un résumé :

* Si vous débutez et apprenez les bases de React mais souhaitez construire un projet simple ou de taille moyenne, restez avec Vite.
* Si vous voulez un framework full-stack avec toutes les fonctionnalités, comme les composants serveur, et que vous ne craignez pas de passer du temps à apprendre des concepts supplémentaires, essayez Next.js.
* Si vous avez essayé Next.js et trouvez certains de ses concepts difficiles à comprendre, mais souhaitez toujours construire une application React full-stack, regardez définitivement Remix.
* Enfin, si vous avez un site web statique ou axé sur le contenu, et que vous n'avez pas vraiment besoin d'une base de données ou d'une authentification, je vous recommande vivement d'utiliser Astro.

## 🏆 Devenez un développeur React professionnel

À la recherche de la ressource ultime pour apprendre React de A à Z ?

✨ **[Présentation : Le React Bootcamp](https://www.thereactbootcamp.com)**

Le bootcamp propose toutes les ressources pour vous aider à réussir avec React :

* 🎬 200+ vidéos approfondies
* 🧩 100+ défis pratiques React
* 🏗️ 5+ projets de portfolio impressionnants
* 📝 10+ fiches de révision React essentielles
* 🧑‍🏫 Un bootcamp complet Next.js
* 🎥 Une série complète de vidéos animées

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même.

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
_Cliquez pour commencer_