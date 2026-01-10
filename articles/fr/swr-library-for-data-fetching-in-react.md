---
title: Comment utiliser la bibliothèque SWR pour une meilleure récupération de données
  dans React
subtitle: ''
author: Furkan Emin Can
co_authors: []
series: null
date: '2023-12-05T21:59:00.000Z'
originalURL: https://freecodecamp.org/news/swr-library-for-data-fetching-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/Cover.png
tags:
- name: hooks
  slug: hooks
- name: React
  slug: react
seo_title: Comment utiliser la bibliothèque SWR pour une meilleure récupération de
  données dans React
seo_desc: 'React is un-opinionated about how you fetch and manage the remote data
  in your application.

  You may think of using the useEffect hook for simple fetching operations, but it
  will not help you with caching, request deduplication, always serving real-ti...'
---

React est non-opinionné sur la manière dont vous récupérez et gérez les données distantes dans votre application.

Vous pourriez penser à utiliser le hook `useEffect` pour des opérations de récupération simples, mais il ne vous aidera pas avec la mise en cache, la déduplication des requêtes, la fourniture de données en temps réel, et ainsi de suite.

Les choses deviennent plus compliquées lorsque vous essayez de les implémenter vous-même. Mais heureusement, la bibliothèque SWR nous aide à résoudre certains problèmes courants et simplifie également le développement.

## Qu'est-ce que la bibliothèque SWR ?

Selon la [documentation SWR](https://swr.vercel.app) :

> Le nom « SWR » est dérivé de `stale-while-revalidate`, une stratégie d'invalidation de cache HTTP popularisée par [HTTP RFC 5861](https://tools.ietf.org/html/rfc5861).
>
> SWR est une stratégie qui consiste d'abord à retourner les données du cache (stale), puis à envoyer la requête de récupération (revalidate), et enfin à fournir les données à jour.

Avec l'aide de cette stratégie, vous pouvez vous assurer de toujours afficher des données à jour à vos utilisateurs.

Ainsi, SWR est une bibliothèque basée sur la stratégie `stale-while-revalidate`, et elle fournit des hooks React pour la récupération de données.

Avant de passer aux détails, examinons les deux concepts les plus importants de SWR.

### Mise en cache

Un cache stocke les données pendant une durée spécifiée et fournit ces données aux utilisateurs qui les demandent dans cette période.

Le temps peut être une période déterminée comme `5000ms` ou peut être un événement comme la reconnexion à Internet.

SWR met automatiquement en cache les données récupérées, aidant à fournir rapidement les données sans effectuer de requêtes réseau redondantes.

### Révalidation

Lorsque le temps valide est dépassé, les données deviennent obsolètes. Lorsque l'utilisateur demande ces données, vous devez les révalider avant de les fournir.

Si les données sont obsolètes, SWR les révalide (les récupère à nouveau depuis le serveur) pour les maintenir à jour.

Par défaut, SWR révalide automatiquement les données (il suppose que les données sont obsolètes) dans trois cas :

1. Chaque fois que le composant est monté, même s'il y a des données dans le cache, il révalide.
2. Il révalide lorsque la fenêtre obtient le focus.
3. Il révalide lorsque le navigateur rétablit sa connexion réseau.

## Comment utiliser le hook `useSWR`

Le hook `useSWR` est le hook principal de la bibliothèque. Dans vos projets, vous l'utiliserez presque toujours.

Il accepte trois paramètres : `key`, `fetcher`, et `options`.

* `key` est une chaîne unique pour la requête comme un identifiant.
* `fetcher` est une fonction asynchrone qui accepte la `key` et retourne les `data`. SWR passe automatiquement la `key` à la fonction `fetcher` lors du chargement des données.
* `options` est un objet d'options disponibles pour le hook. Par exemple, vous pouvez spécifier le temps de cache dans l'objet `options`.

Et il retourne un objet avec les propriétés `data`, `error`, `isValidating`, `isLoading`, et `mutate`.

* `data` est la variable retournée par la fonction `fetcher`. Lors de la première requête, elle sera `undefined`.
* `error` est l'erreur lancée par la fonction `fetcher`. S'il n'y a pas d'erreur, elle sera `undefined`.
* `isLoading` est un booléen qui indique l'état de la **première** requête. Il est `true` pendant la première requête, et sera toujours `false` par la suite.
* `isValidating` est également un booléen qui indique l'état de la requête. Il est `true` pendant chaque requête, y compris la première.
* `mutate` est une fonction pour déclencher manuellement une révalidation.

## Comment j'ai utilisé SWR dans mon projet

La meilleure chose à propos de SWR est sa facilité d'utilisation. Je l'ai essayé dans mon premier projet pour la [Certification des Bibliothèques Front End](https://www.freecodecamp.org/learn/front-end-development-libraries) de freeCodeCamp et je l'ai beaucoup apprécié.

J'ai utilisé TypeScript pour le projet, mais je vous donnerai des exemples avec JavaScript. Donc, ne vous inquiétez pas si vous ne connaissez pas TypeScript – je vous recommande vivement de l'essayer si vous ne l'avez pas encore fait.

De plus, si vous êtes intéressé, vous pouvez trouver le code du projet dans son [dépôt GitHub](https://github.com/femincan/quote-factory).

### Comment ajouter la dépendance `swr` au projet

Pour pouvoir utiliser la bibliothèque, vous pouvez l'installer via `npm`, `pnpm`, ou `yarn`. Je préfère utiliser `pnpm` comme gestionnaire de paquets pour mon projet.

```bash
$ npm i swr
# ou
$ pnpm add swr
# ou
$ yarn add swr
```

### Créer la fonction `fetcher`

Le but de cette fonction est de récupérer les données par URL et de les retourner. J'utiliserai la fonction avec SWR.

```javascript
const fetcher = async (url) => {
  const { data } = await axios.get(url);

  return data;
};

```

La fonction `fetcher` :

* accepte un paramètre `url`,
* récupère les données avec la méthode `get` d'Axios,
* retourne les `data` retournées par la requête.

### Créer un hook qui récupère une citation aléatoire

Basé sur la [documentation SWR](https://swr.vercel.app/docs/getting-started#make-it-reusable), j'ai créé un hook appelé `useRandomQuote`. Ce hook est un wrapper pour le hook `useSWR`. Ainsi, je peux utiliser les mêmes données où que ce soit nécessaire.

```javascript
import useSWR from 'swr/immutable';

const useRandomQuote = () => {
  const { data, ...restSWR } = useSWR(
    'https://api.quotable.io/quotes/random',
    fetcher
  );

  return {
    ...restSWR,
    quote: data?.[0],
  };
};

export { useRandomQuote };

```

Le hook récupère les données avec `useSWR` et retourne un objet qui contient les variables déstructurées du hook `useSWR` et la propriété `quote` qui est le seul élément dans le tableau retourné. J'ai utilisé l'API Quotable pour une citation aléatoire, et l'API retourne un tableau avec un élément qui est la citation aléatoire.

Si vous l'avez remarqué, j'ai importé le hook `useSWR` depuis `swr/immutable` dans l'extrait de code. Il s'agit de la version du hook avec la révalidation automatique désactivée. Je préfère l'utiliser car je veux révalider les données manuellement avec la fonction `mutate`.

### Comment révalider les données manuellement

Si vous souhaitez révalider les données manuellement, vous pouvez utiliser la fonction `mutate` retournée par le hook `useSWR`.

Lorsque la fonction mutate est appelée, SWR révalide les données. Pendant ce processus, la variable `data` reste la même (ne sera pas undefined), et la variable `isValidating` devient true.

Le diagramme suivant de la [documentation SWR](https://swr.vercel.app/docs/advanced/understanding#fetch-and-revalidate) visualise le processus de révalidation :

![Un diagramme pour le modèle "Fetch and Revalidate" dans SWR](https://www.freecodecamp.org/news/content/images/2023/11/fetch-and-revalidate-pattern.png)
_Un diagramme pour le modèle "Fetch and Revalidate" dans SWR_

Dans mon projet, j'ai un composant `QuoteCard` qui affiche la citation actuelle. Ce composant a un bouton `New Quote` qui déclenche la récupération d'une nouvelle citation aléatoire.

```javascript
const QuoteCard = () => {
  const { /* ... */, mutate } = useRandomQuote();

  return (
    {/* ... */}
    <button
      // ...
      onClick={() => mutate()}
    >
      New Quote
    </button>
    {/* ... */}
  )
}

```

Dans le code ci-dessus, j'ai utilisé la fonction `mutate` dans le gestionnaire `onClick` du bouton `New Quote`.

### Comment gérer les requêtes concurrentes

Si l'utilisateur initie une nouvelle requête parallèlement à celle en cours, cela entraîne plusieurs requêtes concurrentes. Chaque requête attend que la précédente soit terminée avant de commencer le processus, ce qui entraîne une utilisation inutile du réseau et un temps d'attente.

J'ai rencontré le même problème dans mon projet. Lorsque l'utilisateur clique sur le bouton `New Quote` alors qu'une requête est encore en cours de chargement, l'application déclenche une nouvelle requête parallèlement à celle existante.

![Requêtes concurrentes déclenchées en cliquant continuellement sur le bouton "New Quote"](https://www.freecodecamp.org/news/content/images/2023/11/illustration.gif)
_Requêtes concurrentes déclenchées en cliquant continuellement sur le bouton "New Quote"_

Comme vous le voyez dans le GIF ci-dessus, lorsque je clique sur le bouton "New Quote" consécutivement, je dois attendre que toutes les requêtes soient terminées pour voir une citation aléatoire car SWR ne met à jour les données qu'après la dernière requête terminée.

En conséquence, je devrais annuler la requête précédente en cours après qu'une nouvelle requête soit initiée. Bien que j'aie vérifié la documentation de SWR, je n'ai pas trouvé de solution intégrée pour ce problème. J'ai essayé d'utiliser `AbortController` avec SWR, mais je n'ai pas réussi.

En tant que solution de contournement, j'ai désactivé le bouton `New Quote` pendant la validation pour pouvoir empêcher les requêtes concurrentes multiples.

Une petite note : J'ai également vérifié [React Query](https://tanstack.com/query/latest), et il a une solution intégrée pour cela. Je prévois de l'expérimenter dans mon prochain projet impliquant des données distantes.

## Conclusion

React ne se soucie pas de la manière dont vous récupérez et gérez les données distantes. Dans ce tutoriel, vous avez appris comment le faire avec SWR. Bien qu'il ait un gros inconvénient concernant l'annulation des requêtes concurrentes, vous pouvez généralement contourner cela et bénéficier de ses avantages.

Si vous n'avez pas utilisé SWR auparavant, je vous recommande vivement de l'essayer dans vos futurs projets. Cela vous fait gagner du temps et vous évite de rencontrer de nombreux types de bugs.

Merci d'avoir lu. Vous pouvez me contacter sur [Twitter](https://twitter.com/femincan) ou explorer davantage sur [mon site web personnel](https://femincan.dev). N'hésitez pas à me contacter – j'adorerais avoir de vos nouvelles !