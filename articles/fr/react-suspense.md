---
title: Comment utiliser React Suspense pour améliorer vos projets React
subtitle: ''
author: Okosa Leonard
co_authors: []
series: null
date: '2023-11-16T17:04:50.000Z'
originalURL: https://freecodecamp.org/news/react-suspense
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/pexels-pixabay-289323.jpg
tags:
- name: asynchronous
  slug: asynchronous
- name: React
  slug: react
seo_title: Comment utiliser React Suspense pour améliorer vos projets React
seo_desc: 'React''s ecosystem is always growing, and it seems like there are always
  new features and enhancements to make development more effective and user-friendly.

  React Suspense is one such feature that has become quite popular among React devs.

  In this gui...'
---

L'écosystème de React est toujours en croissance, et il semble qu'il y ait toujours de nouvelles fonctionnalités et améliorations pour rendre le développement plus efficace et convivial.

React Suspense est une telle fonctionnalité qui est devenue assez populaire parmi les développeurs React.

Dans ce guide, vous apprendrez tout sur React Suspense et examinerez ses fonctionnalités, cas d'utilisation et potentiel pour transformer vos applications web.

## Qu'est-ce que React Suspense ?

React Suspense est une nouvelle fonctionnalité publiée dans React.js version 16.6. Avec cette nouvelle fonctionnalité, les composants peuvent suspendre le rendu pendant qu'ils attendent qu'un processus asynchrone se termine, comme la séparation de code ou la récupération de données.

Suspense a été créé pour faciliter la création d'applications avec des indications de chargement améliorées et une expérience utilisateur plus cohésive. Il permet d'arrêter le rendu de l'arborescence des composants jusqu'à ce que des critères spécifiques soient satisfaits, ce qui facilite le travail des développeurs avec des données asynchrones.

### Un problème auquel les états de chargement sont confrontés dans React

La gestion des états de chargement dans React était un peu plus délicate avant React Suspense. Les développeurs devaient implémenter le mécanisme de chargement en utilisant des frameworks tiers comme Redux ou Mobx, le rendu conditionnel ou la gestion d'état. Cela résultait fréquemment en un code compliqué et sujet aux erreurs.

Ce problème a été résolu par React Suspense, qui offre une méthode plus sophistiquée et intégrée de gestion des actions asynchrones et des états de chargement.

## Concepts et fonctionnalités clés de React Suspense

Parlons de quelques concepts et fonctionnalités pour vous aider à comprendre React Suspense et son fonctionnement.

### 1) Composant Suspense

Un élément essentiel de React Suspense est le composant Suspense. Il vous permet de déclarer comment gérer le contenu de repli pendant que les actions asynchrones sont en attente et encapsuler n'importe quelle partie de votre arborescence de composants.

```jsx
<Suspense fallback={<LeoFallback />}>
  <LeoComponent />
</Suspense>
```

Dans ce cas d'utilisation, si le `LeoComponent` n'est pas prêt, React affichera le composant `LeoFallback` à la place.

### 2) Utilisation de `React.lazy()` ou `lazy()`

React dispose d'un mécanisme d'importation dynamique appelé `lazy()` qui vous permet de charger des composants de manière paresseuse.

En gros, le chargement paresseux fait référence à l'exigence qu'un composant ou une partie de code ne se chargera que lorsqu'il sera nécessaire. Cette fonctionnalité, qui a été incluse pour la première fois dans React 16.6, est fréquemment utilisée en conjonction avec React Suspense pour améliorer la vitesse des applications web en chargeant les composants uniquement lorsqu'ils sont nécessaires.

Cela est très utile pour minimiser la vitesse de chargement de votre application et réduire la taille initiale du bundle.

Nous allons maintenant examiner `lazy()` plus en profondeur et apprendre comment il fonctionne.

#### Syntaxe de base de `lazy()`

Pour utiliser `lazy()`, vous devez suivre ces étapes :

Tout d'abord, importez les composants `Suspense` de React, ainsi que les composants que vous avez l'intention de charger de manière paresseuse.

```jsx
import { Suspense } from 'react';
```

Ensuite, utilisez `lazy()` pour définir une importation dynamique. Pour le composant que vous souhaitez charger lentement, cette fonction accepte un argument qui est une fonction qui produit une instruction d'importation dynamique.

```jsx
const LeoComponent = lazy(() => import('./LeoComponent'));
```

Dans ce cas d'utilisation, le `LeoComponent` sera chargé de manière paresseuse lorsqu'il est nécessaire. L'instruction dynamique `import()` spécifie le chemin vers le composant que vous souhaitez importer.

Ensuite, encapsulez l'élément que vous souhaitez charger de manière paresseuse dans un élément Suspense. Vous pouvez désigner un composant de secours à afficher pendant que le composant chargé de manière paresseuse est en cours de récupération en utilisant le composant Suspense.

```jsx
function App() {
  return (
    <div>
      <Suspense fallback={<div>Chargement...</div>}>
        <LeoComponent />
      </Suspense>
    </div>
  );
}
```

Ici, pendant que le `LeoComponent` est en cours de récupération, le composant de secours sera affiché, indiquant que le contenu est en cours de chargement.

#### Avantages de `React.lazy()`

1. Vitesse améliorée : En chargeant sélectivement les composants nécessaires pour la vue actuelle et en ne chargeant pas tous les composants à la fois, le chargement paresseux des composants peut améliorer la vitesse de l'application.

2. Expérience utilisateur améliorée : Vous pouvez améliorer l'expérience utilisateur en informant les utilisateurs que l'application charge activement du matériel en utilisant Suspense pour afficher une indication de chargement.

3. Fractionnement de code : L'un des principaux avantages de `lazy()` est qu'il permet le fractionnement de code. Le processus de fractionnement de code implique de diviser le code de votre application en bundles plus petits et à la demande. Cela minimise la taille initiale du bundle et accélère le temps de chargement de votre application.

Avec `lazy()`, vous pouvez faire du fractionnement de code et du chargement paresseux des composants dans vos applications React. C'est une excellente fonctionnalité. C'est un outil utile pour rationaliser l'efficacité et les temps de chargement de vos applications web, améliorant l'expérience utilisateur en chargeant les composants uniquement lorsqu'ils sont nécessaires.

Il a des restrictions et certaines préoccupations, mais lorsqu'il est utilisé correctement, il peut être un outil utile dans votre boîte à outils pour le développement React.

### 3) Limites d'erreur

Les composants React connus sous le nom de limites d'erreur ont la capacité de détecter et de gérer les fautes à l'intérieur de leur sous-arborescence. Parce qu'ils peuvent gérer doucement tout problème qui survient pendant l'attente de données asynchrones, ils sont essentiels pour traiter le suspense.

```jsx
class ErrorBoundary extends React.Component {
  componentDidCatch(error, info) {
    // Gérer l'erreur
  }

  render() {
    return this.props.children;
  }
}
```

### 4) Qu'est-ce que le rendu concurrent ?

React Suspense a été introduit dans le cadre du mode concurrent, qui est un ensemble expérimental de fonctionnalités dans React. Plus tard, le rendu concurrent a été introduit.

Le rendu concurrent permet l'exécution de nombreuses tâches simultanément, améliorant la réactivité et l'efficacité des applications React. Il s'agit d'un composant du mode concurrent, une collection d'essais et d'erreurs de fonctionnalités conçues pour surmonter certains des inconvénients du rendu React traditionnel.

Garantir que l'interface utilisateur reste fluide et réactive même lorsque React gère un rendu complexe ou d'autres opérations asynchrones est l'objectif principal du rendu concurrent.

## Comment fonctionne React Suspense ?

Lors de l'utilisation de React Suspense avec des opérations asynchrones, il suit ces étapes :

1. Après que React se charge, un arbre de composants est rendu.

2. React vérifie s'il y a des composants enfants en état suspendu lorsqu'il rencontre un composant Suspense.

3. React affichera l'interface utilisateur de repli donnée jusqu'à ce que les données soient prêtes, si un composant enfant attend des données (par exemple, à la suite d'une importation `lazy()` ou d'une récupération de données).

4. React passe en douceur au rendu du contenu réel une fois les données disponibles.

Parce que cette procédure est automatisée, la gestion des actions asynchrones sans coder une logique sophistiquée est significativement plus facile pour les développeurs.

## Cas d'utilisation pour React Suspense

React Suspense est un outil flexible pour votre boîte à outils qui peut être utilisé dans une variété de scénarios, qui incluent :

### 1. Récupération de données

La fonction de récupération de données de React Suspense facilite la gestion du chargement asynchrone des données dans vos applications React. React Suspense vous permet de reporter le rendu jusqu'à ce que les données soient disponibles, améliorant l'expérience utilisateur en offrant un contenu de repli ou des indications de chargement.

Je vais donner un exemple en utilisant une fausse API pour montrer comment récupérer des données en utilisant React Suspense.

Voici comment utiliser React Suspense pour gérer le chargement des données, en supposant que vous utilisez un framework comme React Query ou Relay pour la récupération de données :

#### Établir une limite d'erreur et React Suspense

Pour capturer toute erreur pendant la récupération des données, vous devez d'abord établir une limite d'erreur et un composant React Suspense. Voici comment créer un composant `ErrorBoundary` personnalisé dans React pour la récupération de données :

```jsx
import React from 'react';

class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  render() {
    if (this.state.hasError) {
      return <div>Erreur : Quelque chose ne va pas !</div>;
    }

    return this.props.children;
  }
}

export default ErrorBoundary;
```

#### Utiliser React Query pour récupérer des données

Si vous utilisez React Query pour récupérer des données, vous pouvez créer un composant qui utilise `useQuery` pour récupérer des données et l'envelopper dans `Suspense` :

```jsx
import React from 'react';
import { useQuery } from 'react-query';
import ErrorBoundary from './ErrorBoundary';

// Définissez votre fonction de récupération de données
async function fetchData() {
  const response = await fetch('https://api.example.com/data');
  if (!response.ok) {
    throw new Error('La réponse du réseau n\'était pas correcte');
  }
  return response.json();
}

function DataFetching() {
  const { data, isLoading, isError } = useQuery('data', fetchData);

  if (isLoading) {
    throw new Promise((resolve) => setTimeout(resolve, 2000)); // Simuler un délai de chargement
  }

  if (isError) {
    throw new Error('Erreur lors de la récupération des données');
  }

  return (
    <div>
      <h1>Récupération de données avec React Suspense</h1>
      <p>{data}</p>
    </div>
  );
}

function App() {
  return (
    <div>
      <h1>Application de Leo</h1>
      <ErrorBoundary>
        <React.Suspense fallback={<div>Chargement...</div>}>
          <DataFetchingComponent />
        </React.Suspense>
      </ErrorBoundary>
    </div>
  );
}

export default App;
```

Dans cet exemple, nous récupérons des données en utilisant le hook `useQuery` de React Query. Pour afficher l'indicateur de chargement, nous `throw in new Promise` pour imiter un délai de chargement si les données sont encore en cours de chargement (`isLoading est vrai`). Nous lançons une erreur afin que la limite d'erreur puisse la capturer s'il y a un problème.

Vous pouvez fournir un composant de secours à afficher pendant le chargement en enveloppant le composant `DataFetching` dans `Suspense`. C'est un message simple "Chargement..." dans ce cas.

Vous voudrez également vous assurer que la gestion des erreurs, les indications de chargement et la fonction de récupération de données sont toutes personnalisées selon vos besoins uniques de récupération de données.

Cet exemple montre comment React Suspense facilite la gestion d'état et la récupération de données, conduisant à une base de code plus organisée et compréhensible.

Ce sont des exemples de Suspense utilisé dans un scénario de récupération de données dans React.

### 2. Chargement paresseux dans React Suspense

Charger des composants de votre application uniquement lorsqu'ils sont nécessaires (chargement paresseux, également connu sous le nom de fractionnement de code) peut réduire la taille de votre bundle initial et accélérer le chargement de votre application React.

Vous pouvez utiliser `React.lazy()` en conjonction avec React `Suspense` pour inclure facilement le chargement paresseux dans votre application.

Voici les étapes pour implémenter le chargement paresseux avec React suspense :

Tout d'abord, importez React Suspense de React :

```jsx
import { Suspense } from 'react';
```

Ensuite, créez un composant chargé de manière paresseuse dans votre application React. Pour construire un composant qui se charge lentement, utilisez la méthode `React.lazy()`. Fournissez une fonction fléchée pour importer dynamiquement le composant.

```jsx
const LennyComponent = lazy(() => import('./LennyComponent'));
```

Ensuite, enveloppez votre composant avec un `Suspense`. Enveloppez Suspense autour de la partie lente. Pendant que le composant paresseux est en cours de chargement, vous pouvez désigner une indication de chargement ou un composant de repli à afficher.

```jsx
function App() {
  return (
    <div>
      <h1>Application de Leo</h1>
      <Suspense fallback={<div>Chargement...</div>}>
        <LennyComponent />
      </Suspense>
    </div>
  );
}
```

Le composant peut être utilisé comme n'importe quel autre composant dans votre application React.

```jsx
function LennyComponent() {
  return <div>Ce composant est chargé de manière paresseuse.</div>;
}
```

Pour terminer la construction de votre application, vous devez utiliser un serveur de développement et un outil comme Webpack pour construire et servir votre application afin de garantir que les fonctions de fractionnement de code fonctionnent comme prévu. Votre code sera automatiquement divisé en morceaux en utilisant Webpack pour le chargement paresseux.

Cette configuration minimisera la taille initiale du bundle et accélérera le chargement de votre application React en ne chargeant le `LazyComponent` que lorsqu'il est nécessaire. Pendant que le composant est en cours de récupération, les utilisateurs verront l'indication de chargement (dans cet exemple, "Chargement..."). Le composant se charge et est rendu dans l'application avec facilité.

### 3. Meilleures expériences utilisateur

React Suspense peut être employé pour garantir une expérience utilisateur fluide en affichant des indicateurs de chargement ou un contenu de repli pendant le chargement des données. Cela réduit le temps de chargement perçu pour les personnes qui utilisent votre application React.

Par exemple, supposons que vous avez un composant qui récupère des données d'une API en utilisant `fetch` et que vous souhaitez afficher une animation de chargement pendant que les données sont en cours de récupération. Voici un exemple de base utilisant React Suspense :

```javascript
import React, { Suspense } from 'react';

// Un composant qui récupère des données
const fetchApiData = () => {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve('Données chargées !');
    }, 2000); // Simulation d'un délai de 2 secondes pour la récupération des données
  });
};

// Un composant qui utilise Suspense pour gérer la récupération asynchrone des données
const DataComponent = () => {
  const apiData = fetchApiData(); // Cela peut être n'importe quelle fonction asynchrone, comme un appel d'API

  return <div>{apiData}</div>;
};

// Envelopper le composant avec Suspense
const App = () => {
  return (
    <Suspense fallback={<LoadingSpinner />}>
      <DataComponent />
    </Suspense>
  );
};

// Un simple composant d'animation de chargement
const LoadingSpinner = () => {
  return <div>Chargement...</div>;
};
```

Dans cet exemple :

Le composant `DataComponent` utilise la méthode `fetchApiData` pour obtenir des données. Gardez à l'esprit que bien que `fetchApiData` soit vraiment une fonction simple qui retourne une promesse, elle peut en fait être un appel d'API dans des applications pratiques.

Le composant Suspense, qui nécessite un argument de repli, encapsule le composant App. Un composant qui sera affiché pendant que l'opération asynchrone est en cours d'exécution est le prop de repli. C'est le composant `LoadingSpinner` dans ce cas.

React Suspense s'occupera automatiquement de la récupération asynchrone des données lorsque le `DataComponent` est rendu. Le composant `LoadingSpinner` sera rendu si les données ne sont pas encore accessibles. Après que les données sont récupérées, l'interface utilisateur est mise à jour.

Cette méthode élimine le besoin de gestion manuelle de l'état de chargement, offrant une expérience utilisateur plus fluide. Ce code est simple et React Suspense fonctionne efficacement ici.

## Conclusion

React Suspense est un ajout majeur à l'écosystème React. Il fournit une méthode plus simple et intégrée de gestion des actions asynchrones et des états de chargement. Vous pouvez l'utiliser pour concevoir des applications qui offrent des temps de chargement plus rapides, une récupération de données plus efficace et de meilleures expériences utilisateur en utilisant `Suspense`, `React.lazy()` et les limites d'erreur.

Il est crucial de comprendre les capacités, restrictions et meilleures pratiques de tout instrument puissant. Le mode concurrent et React Suspense ont le pouvoir de révolutionner le développement d'applications web et d'améliorer l'expérience utilisateur encore plus. Mais à mesure que l'écosystème React continue de croître, il est impératif de rester à jour avec les derniers développements et les meilleures pratiques de l'industrie.