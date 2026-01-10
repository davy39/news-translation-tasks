---
title: Construisez de meilleures applications React avec ces astuces simples
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-06-16T20:55:03.000Z'
originalURL: https://freecodecamp.org/news/build-better-react-apps-with-these-tricks
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/amazing-react-tricks.png
tags:
- name: React
  slug: react
- name: tips
  slug: tips
- name: Web Applications
  slug: web-applications
seo_title: Construisez de meilleures applications React avec ces astuces simples
seo_desc: 'Here''s a list of amazing tricks that you can use to improve your React
  applications instantly.

  These tips will not only make your code cleaner and more reliable, but they also
  aim to make your development experience easier and overall more enjoyable....'
---

Voici une liste d'astuces incroyables que vous pouvez utiliser pour améliorer instantanément vos applications React.

Ces conseils ne rendront pas seulement votre code plus propre et plus fiable, mais ils visent également à rendre votre expérience de développement plus facile et globalement plus agréable. 

Essayez ces techniques dans vos projets React dès aujourd'hui !

## Remplacez Redux par React Query

À mesure que votre application grandit, il devient plus difficile de gérer l'état entre vos composants. Vous pourriez donc vous tourner vers une bibliothèque de gestion d'état comme Redux.

Si votre application dépend de données provenant d'une API, vous utilisez souvent Redux pour récupérer cet état serveur, puis mettre à jour l'état de votre application.

Ce processus peut être complexe – non seulement vous devez récupérer les données, mais vous devez également gérer les différents états, selon que vous avez les données ou que vous êtes dans un état de chargement ou d'erreur.

Au lieu d'utiliser Redux pour gérer les données provenant d'un serveur, **utilisez une bibliothèque comme React Query.**

Tout d'abord, React Query vous donne un meilleur contrôle sur les requêtes HTTP dans vos applications React grâce à des hooks utiles, ainsi que la capacité de recharger facilement les données. Et il vous permet également de gérer l'état entre vos composants de manière transparente, souvent sans avoir à mettre à jour manuellement l'état vous-même.

Voici comment configurer React Query dans votre fichier index.js :

```js
import { QueryClient, QueryClientProvider } from 'react-query'
import ReactDOM from "react-dom";

import App from "./App";

const queryClient = new QueryClient()

const rootElement = document.getElementById("root");
ReactDOM.render(
  <QueryClientProvider client={queryClient}>
    <App />
  </QueryClientProvider>,
  rootElement
);
```

Ici, nous configurons un client de requête qui va mettre en place un cache pour gérer facilement toutes les requêtes que nous avons faites par le passé. Nous configurons également un composant fournisseur de client de requête pour le transmettre à l'ensemble de l'arborescence des composants.

### Comment faire des requêtes avec React Query

Vous pouvez faire des requêtes avec le hook useQuery, qui prend un identifiant pour votre requête (dans ce cas, puisque nous récupérons des données utilisateur, nous l'appellerons 'user'), ainsi qu'une fonction utilisée pour récupérer ces données.

```js
import { useQuery } from "react-query";

export default function App() {
  const { isLoading, isError, data } = useQuery("user", () =>
    fetch("https://randomuser.me/api").then((res) => res.json())
  );

  if (isLoading) return "Chargement...";
  if (isError) return "Erreur !";

  const user = data.results[0];
  return user.email;
}
```

Comme vous pouvez le voir, React Query s'occupe de gérer ces différents états qui peuvent se produire lorsque nous récupérons nos données. Nous n'avons plus besoin de gérer ces états nous-mêmes, nous pouvons simplement les déstructurer à partir de ce qui est retourné par `useQuery`.

Où intervient la partie gestion d'état de useQuery ?

Maintenant que nous avons récupéré les données utilisateur et que nous les avons stockées dans notre cache interne, tout ce que nous avons à faire pour pouvoir les utiliser dans n'importe quel autre composant est d'appeler `useQuery()` avec la clé 'user' que nous avons associée :

```js
import { useQuery } from "react-query";

export default function OtherComponent() {
  const { data } = useQuery('user');
    
  console.log(data);
}
```

## Rendez React Context plus facile avec un hook personnalisé

React Context est un excellent moyen de transmettre des données dans notre arborescence de composants. Il nous permet de transmettre des données à n'importe quel composant que nous souhaitons sans avoir à utiliser des props. 

Pour consommer le contexte dans un composant de fonction React, nous utilisons le hook `useContext`.

Cependant, il y a un léger inconvénient à le faire. Dans chaque composant où nous voulons consommer des données qui ont été transmises via le contexte, nous devons importer à la fois l'objet de contexte créé et importer React pour obtenir le hook useContext.

Au lieu d'avoir à écrire plusieurs instructions d'importation chaque fois que nous voulons lire depuis le contexte, nous pouvons simplement créer un hook React personnalisé.

```js
import React from "react";

const UserContext = React.createContext();

function UserProvider({ children }) {
  const user = { name: "Reed" };
  return <UserContext.Provider value={user}>{children}</UserContext.Provider>;
}

function useUser() {
  const context = React.useContext(UserContext);
  if (context === undefined) {
    throw new Error("useUser n'est pas dans UserProvider");
  }
  return context;
}

export default function App() {
  return (
    <UserProvider>
      <Main />
    </UserProvider>
  );
}

function Main() {
  const user = useUser();

  return <h1>{user.name}</h1>; // affiche "Reed"
}
```

Dans cet exemple, nous transmettons des données utilisateur via notre composant personnalisé UserProvider, qui prend un objet utilisateur et est enveloppé autour du composant Main.

Nous avons un hook `useUser` pour consommer plus facilement ce contexte. Nous n'avons besoin d'importer que ce hook lui-même pour consommer notre User Context dans n'importe quel composant que nous souhaitons, comme notre composant Main.

## Gérez les fournisseurs de contexte dans un composant personnalisé

Dans presque toutes les applications React que vous créez, vous aurez besoin de plusieurs fournisseurs de contexte.

Nous avons non seulement besoin de fournisseurs de contexte pour React Context que nous créons, mais aussi pour les bibliothèques tierces qui en dépendent (comme React Query) afin de transmettre leurs outils aux composants qui en ont besoin.

Une fois que vous avez travaillé sur votre projet React pendant un certain temps, voici à quoi cela tend à ressembler :

```js
ReactDOM.render(
  <Provider3>
    <Provider2>
      <Provider1>
        <App />
      </Provider1>
    </Provider2>
  </Provider3>,
  rootElement
);
```

Que pouvons-nous faire contre ce désordre ?

Au lieu de mettre tous nos fournisseurs de contexte dans notre fichier App.js ou index.js, nous pouvons créer un composant appelé ContextProviders. 

Cela nous permet d'utiliser la prop children, puis tout ce que nous avons à faire est de mettre tous ces fournisseurs dans ce seul composant :

```js
src/context/ContextProviders.js

export default function ContextProviders({ children }) {
  return (
    <Provider3>
      <Provider2>
        <Provider1>
          {children}
        </Provider1>
      </Provider2>
    </Provider3>
  );
}
```

Ensuite, enveloppez le composant ContextProviders autour de App :

```js
src/index.js

import ReactDOM from "react-dom";
import ContextProviders from './context/ContextProviders'
import App from "./App";

const rootElement = document.getElementById("root");
ReactDOM.render(
  <ContextProviders>
    <App />
  </ContextProviders>,
  rootElement
);
```

## Passez les props plus facilement en utilisant l'opérateur de propagation d'objet

Lorsqu'il s'agit de travailler avec des composants, nous passons généralement des données à l'aide de props. Nous créons un nom de prop et le définissons égal à sa valeur appropriée.

Cependant, si nous avons beaucoup de props que nous devons passer à un composant, devons-nous toutes les lister individuellement ?

Non, nous n'avons pas à le faire.

Un moyen très simple de pouvoir passer toutes les props que nous souhaitons sans avoir à écrire tous les noms de props et leurs valeurs correspondantes est d'utiliser le motif `{...props}`. 

Cela implique de mettre toutes nos données de props dans un objet et de propager toutes ces props individuellement vers le composant auquel nous voulons les passer :

```js
export default function App() {
  const data = {
    title: "Mon application géniale",
    greeting: "Bonjour !",
    showButton: true
  };

  return <Header {...data} />;
}

function Header(props) {
  return (
    <nav>
      <h1>{props.title}</h1>
      <h2>{props.greeting}</h2>
      {props.showButton && <button>Déconnexion</button>}
    </nav>
  );
}
```

## Itérez sur des fragments avec React Fragment

La fonction `.map()` dans React nous permet de prendre un tableau et d'itérer dessus, puis d'afficher les données de chaque élément dans un JSX. 

Cependant, dans certains cas, nous voulons itérer sur ces données mais nous ne voulons pas les retourner dans un élément JSX de fermeture. Peut-être qu'utiliser un élément JSX de fermeture modifierait notre style appliqué ou nous ne voulons simplement pas ajouter un autre élément au DOM. 

Un conseil peu connu pour pouvoir itérer sur un ensemble de données, et ne pas avoir l'élément parent comme un élément HTML, est d'utiliser `React.Fragment`. 

Pour utiliser la forme longue des fragments React, vous pouvez lui fournir la prop `key` qui est requise pour tout élément sur lequel nous itérons.

```js
import React from 'react'

export default function App() {
  const users = [
    {
      id: 1,
      name: "Reed"
    },
    {
      id: 2,
      name: "John"
    },
    {
      id: 3,
      name: "Jane"
    }
  ];

  return users.map((user) => (
    <React.Fragment key={user.id}>{user.name}</React.Fragment>
  ));
}
```

Notez que nous ne pouvons pas utiliser la prop `key` requise pour l'alternative de fragment raccourcie : `<></>`.

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à tout comprendre par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : Le React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*