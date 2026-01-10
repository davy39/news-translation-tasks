---
title: Comment utiliser l'API Context de React dans vos projets
subtitle: ''
author: Boateng Dickson
co_authors: []
series: null
date: '2023-03-29T20:04:36.000Z'
originalURL: https://freecodecamp.org/news/context-api-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/context-api-cover-main.jpg
tags:
- name: api
  slug: api
- name: React
  slug: react
- name: React context
  slug: react-context
- name: 'State Management '
  slug: state-management
seo_title: Comment utiliser l'API Context de React dans vos projets
seo_desc: Managing state is an essential part of developing applications in React.
  A common way to manage state is by passing props. Passing props means sending data
  from one component to another. It's a good way to make sure that data gets to the
  right place ...
---

La gestion de l'état est une partie essentielle du développement d'applications avec React. Une façon courante de gérer l'état consiste à transmettre des props. Transmettre des props signifie envoyer des données d'un composant à un autre. C'est un bon moyen de s'assurer que les données arrivent au bon endroit dans une application React.

Mais il peut être fastidieux de transmettre des props lorsque vous devez envoyer les mêmes données à de nombreux composants ou lorsque les composants sont éloignés les uns des autres. Cela peut ralentir une application et la rendre plus difficile à manipuler.

Heureusement, React propose une fonctionnalité intégrée connue sous le nom d'API Context qui aide à « téléporter » les données vers les composants qui en ont besoin sans passer par les props.

Dans cet article, nous explorerons le fonctionnement de l'API Context et comment l'utiliser efficacement dans vos applications React.

## Le problème de la transmission de props

Dans React, la transmission de props est un concept fondamental qui permet à un composant parent de partager des données avec ses composants enfants ainsi qu'avec d'autres composants au sein d'une application.

Dans de nombreux cas, la transmission de props peut être un moyen efficace de partager des données entre différentes parties de votre application. Mais transmettre des props le long d'une chaîne de plusieurs composants pour atteindre un composant spécifique peut rendre votre code excessivement lourd.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-198.png)
_Illustration de la transmission de props du parent aux enfants_

D'après le diagramme ci-dessus, pour transmettre des données au composant « Child B », nous devons les faire passer par tous les composants intermédiaires, même si ces composants n'utilisent pas réellement les données eux-mêmes. C'est ce qu'on appelle le « prop drilling ».

Le prop drilling peut rendre votre code plus difficile à lire et à maintenir, et peut également compliquer la refactorisation de vos composants par la suite.

C'est là qu'intervient l'API Context. Avec l'API Context, vous pouvez stocker des données au niveau supérieur de l'arborescence des composants et les mettre à la disposition de tous les autres composants qui en ont besoin sans transmettre de props.

## Comment fonctionne l'API Context

L'API Context permet de faire passer des données à travers une arborescence de composants sans avoir à transmettre manuellement des props à chaque niveau. Cela facilite le partage de données entre les composants.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-197.png)
_Un diagramme illustrant le fonctionnement de l'API Context_

Par exemple, supposons que vous ayez une application de shopping avec un composant qui affiche le panier d'un utilisateur et un autre composant qui affiche l'historique des commandes de l'utilisateur.

Avec l'API Context, vous pouvez créer un « contexte » qui contient les informations d'achat de l'utilisateur, comme son panier et son historique de commandes. Ensuite, vous pouvez utiliser ce contexte à la fois dans le composant du panier et dans celui de l'historique des commandes, sans avoir à transmettre les informations par les props.

C'est comme avoir une grande boîte qui contient tout ce dont vous avez besoin pour vos courses. Vous pouvez sortir les choses de la boîte quand vous en avez besoin et les remettre quand vous avez terminé.

Fondamentalement, l'API Context se compose de deux éléments principaux : le context provider et le context consumer. Le provider est responsable de la création et de la gestion du contexte, qui contient les données à partager entre les composants. D'autre part, le consumer est utilisé pour accéder au contexte et à ses données à partir d'un composant.

Dans l'exemple donné, le provider créera le contexte qui contient les informations d'achat de l'utilisateur, tandis que les composants consumers (panier et historique des commandes) accéderont à ce contexte pour récupérer les données dont ils ont besoin. Cela évite d'avoir à transmettre les informations via les props, ce qui rend votre code plus efficace et plus facile à gérer.

## Comment débuter avec l'API Context

Pour commencer à utiliser l'API Context dans vos applications, vous devrez suivre quelques étapes simples :

### 1. Créer un objet Context

Tout d'abord, vous devez créer un objet context en utilisant la fonction `createContext` de la bibliothèque 'react'. Cet objet context contiendra les données que vous souhaitez partager dans votre application.

Créez un nouveau fichier nommé `MyContext.js` dans le dossier `src` et ajoutez le code suivant pour créer un objet context :

```jsx
import { createContext } from 'react';

export const MyContext = createContext("");
```

Dans le code ci-dessus, nous importons `createContext` de React et l'utilisons pour créer un nouvel objet context nommé "MyContext". Ensuite, nous exportons l'objet context afin de pouvoir l'utiliser dans d'autres parties de notre application.

### 2. Envelopper les composants avec un Provider

Une fois que vous avez créé un objet context, vous devez envelopper les composants qui ont besoin d'accéder aux données partagées avec un composant Provider. Le composant Provider accepte une prop "value" qui contient les données partagées, et tout composant enfant du composant Provider peut accéder à ces données partagées.

Il est important de noter que le composant Provider doit être enveloppé autour du composant de niveau supérieur d'une application pour garantir que tous les composants enfants ont accès aux données partagées.

Voici un exemple qui montre comment envelopper des composants avec un Provider dans l'API Context :

```jsx
// Créer un composant parent qui enveloppe les composants enfants avec un Provider

import { useState, React } from "react";
import { MyContext } from "./MyContext";
import MyComponent from "./MyComponent";

function App() {
  const [text, setText] = useState("");

  return (
    <div>
      <MyContext.Provider value={{ text, setText }}>
        <MyComponent />
      </MyContext.Provider>
    </div>
  );
}

export default App;
```

Dans cet exemple, nous avons un composant parent appelé App. Ce composant possède une variable d'état appelée "text", qui est initialement définie sur une chaîne vide. Nous avons également défini une fonction appelée `setText` qui peut être utilisée pour mettre à jour la valeur de `text`.

À l'intérieur de l'instruction return du composant App, nous avons enveloppé les enfants de ce composant avec le composant provider ("MyContext.Provider"). Ensuite, nous avons passé un objet à la prop value du composant provider qui contient les valeurs "text" et "setText".

### 3. Consommer le Context

Maintenant que nous avons créé le composant provider, nous devons consommer le contexte dans d'autres composants. Pour ce faire, nous utilisons le hook "useContext" de React.

```jsx
import { useContext } from 'react';
import { MyContext } from './MyContext';

function MyComponent() {
  const { text, setText } = useContext(MyContext);

  return (
    <div>
      <h1>{text}</h1>
      <button onClick={() => setText('Hello, world!')}>
        Cliquez-moi
      </button>
    </div>
  );
}

export default MyComponent;
```

Dans cet exemple, nous avons utilisé le hook useContext pour accéder aux variables "text" et "setText" qui ont été définies dans le composant provider.

À l'intérieur de l'instruction return de "MyComponent", nous avons rendu un élément de titre qui affiche la valeur de `text`. Nous avons également rendu un bouton qui, lorsqu'il est cliqué, appellera la fonction `setText` pour mettre à jour la valeur de `text` à "Hello, world!".

<img src="https://i.imgur.com/a191j3C.gif" style="border: 1px solid #333; border-radius: 3px; box-shadow: 2px 1px 6px rgba(0,0,0,0.2)"/>

Et voilà ! C'est ainsi que vous pouvez utiliser l'API Context dans votre application React.

En créant un objet context, en définissant un composant provider et en consommant le contexte dans d'autres composants, vous pouvez partager des données dans votre application de manière simple et efficace.

## Cas d'utilisation de l'API Context

Voici quelques cas d'utilisation réels de l'API Context.

1. **Gestion des thèmes :** Vous pouvez utiliser l'API Context pour stocker le thème actuel de votre application et le mettre à la disposition de tous les composants. De cette façon, chaque fois que l'utilisateur change de thème (comme l'activation du mode sombre), tous les composants seront mis à jour avec le nouveau thème.
2. **Authentification utilisateur :** Vous pouvez également utiliser l'API Context pour stocker le statut d'authentification d'un utilisateur et le transmettre à tous les composants qui en ont besoin. De cette façon, vous pouvez facilement restreindre l'accès à certaines parties de votre application en fonction du statut d'authentification de l'utilisateur.
3. **Support multilingue :** Vous pouvez stocker la langue actuelle de votre application dans le contexte et la transmettre à tous les composants qui en ont besoin. De cette façon, vous pouvez facilement basculer entre différentes langues sans avoir à transmettre la langue en tant que props à tous les composants.
4. **Accès aux données de sources externes :** Enfin, vous pouvez utiliser l'API Context pour stocker des données récupérées de sources externes telles que des API ou des bases de données et les mettre à la disposition de tous les composants. Cela peut simplifier votre code et faciliter la gestion des données dans votre application.

Dans l'ensemble, l'API Context offre un moyen flexible et efficace de gérer les données d'état dans votre application, et elle peut être particulièrement utile pour gérer les données globales qui doivent être partagées entre plusieurs composants.

## Bonnes pratiques pour l'API Context

Comme pour tout outil, il existe des bonnes pratiques et des pièges courants à garder à l'esprit lors de l'utilisation de l'API Context dans vos projets. Voici quelques conseils pour une utilisation efficace de l'API Context :

1. Utilisez un fichier séparé pour définir votre Context : C'est une bonne pratique de définir votre objet context dans un fichier séparé pour garder votre code organisé et facile à maintenir.
2. Limitez l'API Context à la gestion de l'état global uniquement : Il est préférable d'utiliser l'API Context pour gérer l'état qui doit être accessible via plusieurs composants de votre application. Évitez de l'utiliser pour un état qui ne doit être accessible qu'au sein d'un seul composant, car cela peut entraîner une complexité inutile et des problèmes de performance.
3. Utilisez les context providers avec parcimonie : Bien que les context providers puissent être un outil puissant pour gérer l'état global, il est généralement judicieux de les utiliser avec parcimonie. Envisagez plutôt d'utiliser les props pour transmettre les données dans votre arborescence de composants chaque fois que cela est possible.
4. Utilisez des valeurs par défaut : Lors de la création d'un nouveau contexte, il est conseillé de fournir une valeur par défaut qui sera utilisée si aucun provider n'est présent. Cela peut aider à prévenir les erreurs inattendues et à rendre votre code plus robuste. Notez que, pour le projet que nous avons réalisé ci-dessus, nous avons utilisé une chaîne vide comme valeur par défaut pour l'objet context.

## Récapitulatif

Dans cet article, nous avons exploré l'API Context de React, un outil puissant pour gérer l'état dans les applications React.

Nous avons passé en revue les bases de l'API Context, y compris la création d'un contexte, la création d'un composant Provider pour transmettre des données aux composants enfants et la consommation de données dans d'autres composants à l'aide du hook `useContext`.

## Conclusion

Si vous souhaitez explorer comment implémenter un thème mode clair/sombre dans vos propres projets React à l'aide de l'API Context, j'ai créé un site Web simple qui montre comment faire exactement cela. Vous pouvez trouver le code du projet sur mon [GitHub](https://github.com/dboatengg/context-api-tutorial).

En explorant le code et en expérimentant vos propres modifications, vous serez sur la bonne voie pour maîtriser l'API Context et libérer tout son potentiel dans vos propres projets.

Merci de m'avoir lu !