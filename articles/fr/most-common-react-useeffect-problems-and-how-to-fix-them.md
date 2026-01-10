---
title: React.useEffect Hook – Problèmes courants et comment les résoudre
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-10-14T22:07:02.000Z'
originalURL: https://freecodecamp.org/news/most-common-react-useeffect-problems-and-how-to-fix-them
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/react-1.png
tags:
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: React.useEffect Hook – Problèmes courants et comment les résoudre
seo_desc: 'By Iva Kop

  React hooks have been around for a while now. Most developers have gotten pretty
  comfortable with how they work and their common use cases. But there is one useEffect
  gotcha that a lot of us keep falling for.

  The use case

  Let''s start with ...'
---

Par Iva Kop

Les hooks React existent depuis un certain temps. La plupart des développeurs se sont familiarisés avec leur fonctionnement et leurs cas d'utilisation courants. Mais il y a un piège avec `useEffect` dans lequel beaucoup d'entre nous tombent encore.

# Le cas d'utilisation

Commençons par un scénario simple. Nous construisons une application React et nous voulons afficher le nom d'utilisateur de l'utilisateur actuel dans l'un de nos composants. Mais d'abord, nous devons récupérer le nom d'utilisateur à partir d'une API.

Parce que nous savons que nous aurons besoin d'utiliser les données de l'utilisateur ailleurs dans notre application, nous voulons également abstraire la logique de récupération des données dans un hook React personnalisé.

Essentiellement, nous voulons que notre composant React ressemble à ceci :

```
const Component = () => {
  // useUser custom hook
  
  return <div>{user.name}</div>;
};

```

Cela semble assez simple !

# Le hook React useUser

La deuxième étape serait de créer notre hook personnalisé `useUser`.

```
const useUser = (user) => {
  const [userData, setUserData] = useState();
  useEffect(() => {
    if (user) {
      fetch("users.json").then((response) =>
        response.json().then((users) => {
          return setUserData(users.find((item) => item.id === user.id));
        })
      );
    }
  }, []);

  return userData;
};

```

Analysons cela. Nous vérifions si le hook reçoit un objet utilisateur. Après cela, nous récupérons une liste de nos utilisateurs à partir d'un fichier appelé `users.json` et nous le filtrons afin de trouver l'utilisateur avec l'id dont nous avons besoin.

Ensuite, une fois que nous avons les données nécessaires, nous les enregistrons dans l'état `userData` de notre hook. À la fin, nous retournons `userData`.

_**Note** : Ceci est un exemple simplifié à des fins d'illustration uniquement ! La récupération de données dans le monde réel est beaucoup plus compliquée. Si vous êtes intéressé par le sujet, [consultez mon article](https://blog.whereisthemouse.com/graphql-requests-made-easy-with-react-query-and-typescript) sur la création d'une configuration de récupération de données avec ReactQuery, Typescript et GraphQL._

Intégrons le hook dans notre composant React et voyons ce qui se passe.

```
const Component = () => {
  const user = useUser({ id: 1 });
  return <div>{user?.name}</div>;
};

```

Bien ! Tout semble fonctionner comme prévu. Mais attendez... qu'est-ce que c'est ?

# Règle exhaustive-deps d'ESLint

Nous avons un avertissement ESLint dans notre hook :

```
React Hook useEffect has a missing dependency: 'user'. Either include it or remove the dependency array. (react-hooks/exhaustive-deps)

```

Hmm, notre `useEffect` semble avoir une dépendance manquante. Oh, bien ! Ajoutons-la. Qu'est-ce qui pourrait mal se passer ? 😂

```
const useUser = (user) => {
  const [userData, setUserData] = useState();
  useEffect(() => {
    if (user) {
      fetch("users.json").then((response) =>
        response.json().then((users) => {
          return setUserData(users.find((item) => item.id === user.id));
        })
      );
    }
  }, [user]);

  return userData;
};

```

Oh-oh ! Il semble que notre `Component` ne cesse de se re-rendre. Que se passe-t-il ici ?!

Expliquons.

# Le problème des re-rendus infinis

La raison pour laquelle notre composant se re-rend est que la dépendance de notre `useEffect` change constamment. Mais pourquoi ? Nous passons toujours le même objet à notre hook !

Bien qu'il soit vrai que nous passons un objet avec la même clé et la même valeur, ce n'est pas exactement le même objet. En réalité, nous créons un nouvel objet à chaque fois que nous re-rendons notre `Component`. Ensuite, nous passons le nouvel objet comme argument à notre hook `useUser`.

À l'intérieur, `useEffect` compare les deux objets, et comme ils ont une référence différente, il récupère à nouveau les utilisateurs et définit le nouvel objet utilisateur dans l'état. Les mises à jour de l'état déclenchent alors un re-rendu dans le composant. Et ainsi de suite, et ainsi de suite...

Alors, que pouvons-nous faire ?

# Comment le résoudre

Maintenant que nous comprenons le problème, nous pouvons commencer à chercher une solution.

La première et probablement la solution la plus évidente est de supprimer la dépendance du tableau de dépendances de `useEffect`, d'ignorer la règle ESLint et de continuer notre chemin.

Mais ce n'est pas la bonne approche. Cela peut (et probablement va) entraîner des bugs et des comportements inattendus dans notre application. Si vous voulez en savoir plus sur le fonctionnement de `useEffect`, je vous recommande vivement le [guide complet](https://overreacted.io/a-complete-guide-to-useeffect/) de Dan Abramov.

Alors, que faire ensuite ?

Dans notre cas, la solution la plus simple est de sortir l'objet `{ id: 1 }` du composant. Cela donnera à l'objet une référence stable et résoudra notre problème.

```
const userObject = { id: 1 };

const Component = () => {
  const user = useUser(userObject);
  return <div>{user?.name}</div>;
};

export default Component;

```

Mais ce n'est pas toujours possible. Imaginez que l'id de l'utilisateur dépendait d'une manière ou d'une autre des props ou de l'état du composant.

Il pourrait s'agir que nous utilisions des paramètres d'URL pour y accéder, par exemple. Si c'est le cas, nous avons un hook `useMemo` pratique à notre disposition qui mémoisera l'objet et assurera une fois de plus une référence stable.

```
const Component = () => {
  const { userId } = useParams();
  
  const userObject = useMemo(() => {
    return { id: userId };
  }, [userId]); // N'oubliez pas les dépendances ici non plus !

  const user = useUser(userObject);
  return <div>{user?.name}</div>;
};

export default Component;

```

Enfin, au lieu de passer une variable objet à notre hook `useUser`, il est possible de passer uniquement l'id de l'utilisateur lui-même, qui est une valeur primitive. Cela empêchera les problèmes d'égalité référentielle dans le hook `useEffect`.

```
const useUser = (userId) => {
  const [userData, setUserData] = useState();

  useEffect(() => {
    fetch("users.json").then((response) =>
      response.json().then((users) => {
        return setUserData(users.find((item) => item.id === userId));
      })
    );
  }, [userId]);

  return userData;
};

const Component = () => {
  const user = useUser(1);

  return <div>{user?.name}</div>;
};

```

Problème résolu !

Et nous n'avons même pas eu à enfreindre de règles ESLint en cours de route...

_**Note** : Si l'argument que nous passions au hook personnalisé était une fonction, plutôt qu'un objet, nous utiliserions des techniques très similaires pour éviter les re-rendus infinis. Une différence notable est que nous devrions remplacer `useMemo` par `useCallback` dans l'exemple ci-dessus._

Merci d'avoir lu !

Curieux à propos du code ? Jouez avec vous-même [ici](https://codesandbox.io/s/useeffect-gotcha-20jw9?file=/src/App.js).

Visitez mon [blog](https://blog.whereisthemouse.com/) et [suivez-moi](https://twitter.com/iva_kop) sur Twitter pour plus de contenu lié à React.

Image par [vectorjuice](https://www.freepik.com/vectors/technology)