---
title: React Context API Expliqué avec des Exemples
subtitle: ''
author: Matéu.sh
co_authors: []
series: null
date: '2024-05-30T08:13:54.000Z'
originalURL: https://freecodecamp.org/news/react-context-api-explained-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/Context-API.png
tags:
- name: React
  slug: react
seo_title: React Context API Expliqué avec des Exemples
seo_desc: Managing state has always been a critical aspect of making web applications
  with React. The most basic way to do this is prop drilling. In prop drilling, you
  pass props around from the parent component to other components that need it, no
  matter how ...
---

La gestion de l'état a toujours été un aspect critique de la création d'applications web avec React. La méthode la plus basique pour le faire est le prop drilling. Dans le prop drilling, vous passez des props du composant parent à d'autres composants qui en ont besoin, peu importe leur niveau d'imbrication.

Le problème avec le prop drilling est que, à mesure que l'application grandit en complexité, le passage de données à travers plusieurs niveaux de composants peut devenir désordonné, fastidieux et sujet aux erreurs.

L'API Context de React a été publiée en 2018 pour éviter le prop drilling en simplifiant la gestion de l'état et en rendant le partage de données à travers l'arborescence des composants plus efficace et sans erreur.

Cet article explorera l'API Context, en commençant par comprendre le besoin de celle-ci dans les applications React, en passant par sa configuration et son utilisation efficace. Nous examinerons également les cas d'utilisation courants, la comparerons avec d'autres solutions de gestion d'état, et discuterons des meilleures pratiques pour vous assurer d'utiliser l'API Context à son plein potentiel.

## Comprendre le Besoin de Context dans React

Examinons un exemple de base dans lequel nous avons un `ParentComponent` qui contient un état `count`, et vous devez passer cet état à un `GrandchildComponent` profondément imbriqué.

Voici le `ParentComponent` qui contient l'état et `setState` mais ne les utilise pas :

```jsx
'use client';

import { useState } from 'react';
import ChildComponent from './ChildComponent';

const ParentComponent = () => {
 const [count, setCount] = useState(0);

 return (
   <>
     <div className="text-center mt-3">
       <h2 className="text-3xl">Parent Component</h2>
       <small>Not using the count state</small>
     </div>


     <ChildComponent count={count} setCount={setCount} />
   </>
 );
};

export default ParentComponent;
```

Voici le `ChildComponent` qui n'utilise pas l'état et `setState` non plus, mais doit tout de même les prendre du `ParentComponent` et les passer au `GrandChildComponent` qui en a besoin :

```jsx
'use client';

import GrandChildComponent from './GrandChildComponent';

const ChildComponent = ({ count, setCount }) => {
 return (
   <>
     <div className="text-center mt-3">
       <h2 className="text-3xl">Child Component</h2>
       <small>Not Using the count state too</small>
     </div>

     <GrandChildComponent count={count} setCount={setCount} />
   </>
 );
};

export default ChildComponent;
```

Voici le `GrandChildComponent` qui a besoin de l'état et de `setState`, et les utilise :

```jsx
'use client';

const GrandChildComponent = ({ count, setCount }) => {
 return (
   <div>
     <div className="text-center mt-3">
       <h2 className="text-3xl">Grandchild Component</h2>
       <small>Using the count state</small>
     </div>
     <div className="text-center">
       <h3 className="text-2xl">Count is: {count}</h3>
       <button
         onClick={() => setCount(count + 1)}
         className="bg-pink-600 p-2 rounded text-white"
       >
         Increase Count
       </button>
     </div>
   </div>
 );
};

export default GrandChildComponent;
```

Et voici à quoi cela ressemble dans le navigateur une fois que le `ParentComponent` est importé dans le composant `Home` d'un projet Next JS :

![Image](https://www.freecodecamp.org/news/content/images/2024/05/prop-drilling.gif)
_Prop drilling dans React_

C'est le prop drilling en action. Vous pouvez voir que le `ChildComponent` qui n'utilise pas l'état `count` et `setCount` doit tout de même absorber les deux car ils seront utilisés dans le `GrandChildComponent`.

C'est ainsi que vous continuerez à passer l'état dans l'application. Alors, que se passe-t-il si vous avez des composants encore plus profonds dans l'arborescence ? Comme `GreatGrandChild` et même `GreatGreatGrandChild` ? Pourquoi un parent doit-il déranger sa jeune génération avec ses problèmes ?

Dans les applications plus grandes, le prop drilling peut rendre le code plus difficile à maintenir et à comprendre. Chaque composant intermédiaire doit être conscient des props qu'il doit passer, même s'il ne les utilise pas.

C'est pourquoi l'API Context existe pour éviter ce prop drilling fastidieux et rendre l'utilisation de l'état dans les composants profondément imbriqués moins fastidieuse et plus directe.

## Comment Fonctionne l'API Context ?

L'API Context fournit un moyen de partager des valeurs comme l'état, les fonctions, ou toute autre donnée à travers l'arborescence des composants sans passer manuellement les props à chaque niveau. Cela est particulièrement utile pour les données globales que de nombreux composants doivent accéder.

Pour commencer à utiliser l'API Context, la première chose à faire est de créer un contexte en utilisant la méthode `createContext()`. Cette fonction retourne un objet de contexte avec deux composants – un `Provider` et un `Consumer`.

Le `Provider` est utilisé pour envelopper la partie de votre arborescence de composants où vous souhaitez que le contexte soit disponible. Il accepte une prop `value` obligatoire qui contient les données que vous souhaitez partager à travers d'autres composants. Lorsque la prop `value` du `Provider` change, tous les descendants qui consomment le contexte seront re-rendus.

Le `Consumer` permet à tout composant descendant d'utiliser le contexte. Il prend une fonction comme enfant, où l'argument de la fonction est la valeur actuelle du contexte. Dans React moderne, le hook `useContext` est souvent utilisé à la place de `Consumer` pour une meilleure lisibilité et simplicité.

## Comment Configurer un Provider de Contexte

Pour vous montrer comment configurer un provider de contexte, j'utiliserai l'état de compteur et la fonction `setCount` de l'exemple de prop drilling.

Rappelez-vous que la première chose à faire est de créer un contexte en utilisant la méthode `createContext`. Je vais le faire dans un fichier `context/counterContext.js`. C'est la convention pour nommer un fichier de contexte – `functionalityContext.js` ou `.ts`.

Voici les étapes complètes pour configurer un provider de contexte :

* Importer `createContext` et `useState` depuis React
* Créer une constante `CounterContext` et la définir sur `createContext`
* Passer les valeurs par défaut à `createContext`
* Créer le composant `CounterProvider` qui prendra `children`
* Définir votre `state` et `setState`
* Retourner un `CounterContext.Provider` qui prendra `count` et `setCount` comme valeurs de la prop `value`
* Passer `children` – il représente tout ce qui sera imbriqué lorsque le Contexte est consommé
* Exporter `CounterContext` et `CounterProvider`

```jsx
import { createContext, useState } from 'react';

const CounterContext = createContext({
 count: 0,
 setCount: () => {},
});

const CounterProvider = ({ children }) => {
 const [count, setCount] = useState(0);

 return (
   <CounterContext.Provider value={{ count, setCount }}>
     {children}
   </CounterContext.Provider>
 );
};

export { CounterContext, CounterProvider };
```

Ce même processus s'applique de la même manière à tout contexte que vous souhaitez créer.

## Comment Consommer le Contexte dans les Composants React

Pour consommer un contexte, la première chose à faire est de l'importer et de l'envelopper autour de l'application.

Pour notre petite application de compteur, vous pouvez le faire à l'intérieur du fichier `layout` d'un projet Next JS 14 en important `CounterProvider` depuis le fichier `counterContext` et en l'enveloppant autour de `{children}` à l'intérieur de la balise `body` :

```jsx
import { CounterProvider } from '@/context/counterContext';

export default function RootLayout({
 children,
}: Readonly<{ children: React.ReactNode }>) {
 return (
   <html lang="en">
     <body className={inter.className}>
       {/* Envelopper le CounterProvider autour des enfants */}
       <CounterProvider>{children}</CounterProvider>
     </body>
   </html>
 );
}

```

Maintenant, toutes les pages et composants auront accès à l'état `count` et à la fonction `setCount`.

Maintenant, à l'intérieur du composant `GrandChild` où l'état `count` et la fonction `setCount` sont utilisés, importez `useContext` depuis `'react'` et `CounterContext` depuis le fichier `counterContext`, puis supprimez les props.

De plus, extrayez l'état `count` et `setCount` du `CounterContext` que vous avez importé comme ceci :

```jsx
const { count, setCount } = useContext(CounterContext);

```

Vous pouvez laisser `count` et `setCount` tels quels et tout fonctionnera bien :

```jsx
'use client';

import { useContext } from 'react';
import { CounterContext } from '@/context/counterContext';

const GrandChildComponent = () => {
 const { count, setCount } = useContext(CounterContext);

 return (
   <div>
     <div className="text-center mt-3">
       <h2 className="text-3xl">Grandchild Component</h2>
       <small>Using the count state</small>
     </div>
     <div className="text-center">
       <h3 className="text-2xl">Count is: {count}</h3>
       <button
         onClick={() => setCount(count + 1)}
         className="bg-pink-600 p-2 rounded text-white"
       >
         Increase Count
       </button>
     </div>
   </div>
 );
};

export default GrandChildComponent;
```

Tout fonctionne toujours bien :

![Image](https://www.freecodecamp.org/news/content/images/2024/05/prop-drilling-1.gif)
_API Context pour atténuer le prop drilling dans React_

## Cas d'Utilisation Courants pour l'API Context

L'API Context est polyvalente et peut être utilisée dans divers scénarios où la gestion de l'état et le partage de données entre plusieurs composants sont nécessaires. Voici quelques cas d'utilisation courants :

* **Gestion de l'état global dans les applications moyennes à grandes** : l'API Context peut gérer la gestion de l'état global comme les articles du panier dans une application de commerce électronique ou la chanson actuellement jouée dans une application musicale.
* **Gestion de l'authentification** : utiliser l'API Context et d'autres solutions similaires pour gérer l'état d'authentification est un cas d'utilisation courant. Les états comme l'utilisateur actuel et les jetons d'authentification peuvent être partagés à travers l'application en utilisant l'API Context. Cela permet à tout composant d'accéder au statut d'authentification de l'utilisateur et d'effectuer des actions comme la connexion et la déconnexion, ou d'afficher certains éléments en fonction de l'état.
* **Gestion des Thèmes** : Un autre cas d'utilisation populaire pour l'API Context est la gestion des thèmes (basculer entre le mode sombre et le mode clair). Vous pouvez le faire en stockant l'état du thème dans un contexte, puis en accédant et en mettant à jour le thème dans n'importe quel composant sans avoir à passer des props à travers plusieurs couches.

D'autres cas d'utilisation sont la localisation, les préférences utilisateur comme les paramètres de notification, les états d'ouverture, de fermeture et de basculement d'une modale, la gestion des requêtes API, la navigation par fil d'Ariane, la progression des étapes, et tout autre point où l'état est impliqué.

## Comparaison de l'API Context avec d'Autres Solutions de Gestion d'État

L'API Context est l'un des plusieurs outils disponibles pour gérer l'état dans une application React. Il en existe d'autres comme Redux et Redux Toolkit, Zustand, et MobX. Chacun d'eux a ses propres forces et cas d'utilisation idéaux.

### Redux

Redux est une bibliothèque tierce qui fournit un conteneur d'état prévisible et suit le modèle d'architecture Flux. Il nécessite plus de code boilerplate et a une courbe d'apprentissage plus raide par rapport à l'API Context.

Cette courbe d'apprentissage plus raide a été considérablement réduite par l'introduction de Redux Toolkit – une forme plus simple et plus légère de Redux.

Redux fournit des fonctionnalités supplémentaires comme les middlewares, le débogage avec voyage dans le temps avec Redux Devtools, et des outils pour gérer les effets secondaires. Il est souvent considéré comme plus adapté aux applications plus grandes avec des besoins complexes de gestion d'état.

### Zustand

Zustand est une bibliothèque externe construite sur l'API Context et les hooks. Il fournit une API légère pour gérer l'état global dans les applications React en utilisant un seul store (ou plusieurs stores si nécessaire). Il est mieux adapté aux petites et moyennes applications React avec des besoins modérés de gestion d'état.

Zustand gère automatiquement les mises à jour, les abonnements et les re-rendus efficaces. Il supporte les middlewares, l'intégration des DevTools, le débogage avec voyage dans le temps, et offre des fonctionnalités comme les mises à jour partielles de l'état, les mises à jour immutables et les fonctions de sélection.

### MobX

MobX est une autre bibliothèque tierce qui utilise des données observables et des réactions pour gérer l'état. Il a un style de programmation plus impératif par rapport à l'approche fonctionnelle de Redux.

MobX est plus facile à apprendre et à utiliser pour les petites applications, tout comme l'API Context. Il fournit des fonctionnalités comme les valeurs calculées et les dérivations automatiques.

## Bonnes Pratiques pour Utiliser l'API Context dans React

Si vous souhaitez utiliser l'API Context de manière efficace, il y a quelques bonnes pratiques à suivre pour vous assurer que votre application reste maintenable, performante et évolutive. Voici quelques directives et conseils pour utiliser l'API Context :

### Toujours Fournir des Valeurs par Défaut

Fournir des valeurs par défaut peut vous aider à éviter les erreurs indéfinies lorsqu'un contexte est utilisé en dehors de son provider.

```jsx
const UserContext = createContext({
 user: { name: 'Guest', age: null },
 setUser: () => {},
});

```

### Ne Pas Trop Utiliser le Contexte

Une utilisation excessive du contexte peut entraîner des problèmes de performance et rendre la gestion de l'état plus difficile à comprendre. N'utilisez le contexte que pour l'état global qui doit vraiment être accessible par de nombreux composants.

Vous pouvez le faire en créant plusieurs contextes pour différentes parties de votre application au lieu d'un seul contexte tout-en-un.

```jsx
const ThemeContext = React.createContext();
const AuthContext = React.createContext();

```

Cela réduit les re-rendus inutiles et garde la gestion de l'état modulaire.

### Éviter les Mises à Jour Fréquentes

Utilisez l'état local pour les données changeant fréquemment. En effet, les mises à jour fréquentes des valeurs de contexte peuvent provoquer le re-rendu de tous les composants consommateurs, ce qui pourrait avoir un impact négatif sur les performances.

```jsx
const UserContext = createContext();

const UserProvider = ({ children }) => {
 const [user, setUser] = useState({ name: 'John Doe', age: 30 });
 const [isOnline, setIsOnline] = useState(true); // état local pour une donnée changeant fréquemment

 return (
   <UserContext.Provider value={{ user, setUser }}>
     {children}
   </UserContext.Provider>
 );
};
```

### Utiliser des Hooks Personnalisés pour Encapsuler la Logique

Efforcez-vous de créer des hooks personnalisés pour encapsuler la logique de consommation du contexte. Cela améliore la lisibilité et la réutilisabilité du code.

```jsx
const useUser = () => {
 const context = useContext(UserContext);
 if (!context) {
   throw new Error('useUser must be used within a UserProvider');
 }
 return context;
};

```

### Mémoïser les Valeurs de Contexte

Utiliser le hook `useMemo` pour mémoïser les valeurs de contexte peut aider à prévenir les re-rendus inutiles des composants consommateurs.

```jsx
const UserProvider = ({ children }) => {
 const [user, setUser] = useState({ name: 'John Doe', age: 30 });

 const value = useMemo(() => ({ user, setUser }), [user, setUser]);

 return <UserContext.Provider value={value}>{children}</UserContext.Provider>;
};
```

## Résumé

Dans cet article, nous avons exploré l'API Context, en commençant par comprendre son besoin et son fonctionnement. En utilisant un exemple de compteur, nous avons configuré un Provider de Contexte et consommé le contexte dans un composant pour démontrer son utilisation.

Nous avons discuté des cas d'utilisation courants pour l'API Context et l'avons comparée avec d'autres solutions de gestion d'état comme Redux, MobX et Zustand. Enfin, nous avons couvert les meilleures pratiques pour utiliser l'API Context de manière efficace.

J'espère que tout ce qui a été couvert dans cet article vous aidera à comprendre l'API Context et à l'utiliser dans vos projets React.

### Apprendre React et Next JS

Vous voulez maîtriser d'autres fonctionnalités incroyables de React comme l'API Context ? Rejoignez mon cours React et Next JS sur Udemy ! Vous apprendrez à construire le jeu 2048 à partir de zéro et obtiendrez des informations sur la résolution des erreurs courantes que les développeurs React rencontrent chaque jour.

[![Next.js crash course on Udemy](https://assets.mateu.sh/assets/fcc-universal)](https://assets.mateu.sh/r/fcc-universal)

P.S. Cela signifierait beaucoup pour moi si vous décidez de partager cet article sur vos réseaux sociaux.