---
title: Comment utiliser useMemo dans React – avec des exemples de code
subtitle: ''
author: Joan Ayebola
co_authors: []
series: null
date: '2024-02-07T18:13:41.000Z'
originalURL: https://freecodecamp.org/news/how-to-work-with-usememo-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Ivory-and-Blue-Lavender-Aesthetic-Photo-Collage-Presentation--6-.png
tags:
- name: hooks
  slug: hooks
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: Comment utiliser useMemo dans React – avec des exemples de code
seo_desc: "useMemo is a valuable tool in the React framework, designed to optimize\
  \ performance by memoizing expensive computations. \nWith useMemo, React can store\
  \ the result of a function call and reuse it when the dependencies of that function\
  \ haven't changed,..."
---

`useMemo` est un outil précieux dans le framework React, conçu pour optimiser les performances en mémorisant les calculs coûteux. 

Avec `useMemo`, React peut stocker le résultat d'un appel de fonction et le réutiliser lorsque les dépendances de cette fonction n'ont pas changé, plutôt que de recalculer la valeur à chaque rendu. 

`useMemo` se distingue comme un outil puissant pour optimiser les performances sans sacrifier la lisibilité ou la maintenabilité du code. Mais il est souvent négligé ou mal compris par les débutants. 

Dans ce guide complet, nous discuterons de ce qu'est `useMemo`, de son fonctionnement et de pourquoi il est un outil essentiel pour chaque développeur React.

### Table des matières

1. [Qu'est-ce que useMemo ?](#heading-quest-ce-que-usememo)
2. [Comment fonctionne useMemo ?](#heading-comment-fonctionne-usememo)
3. [Quand utiliser useMemo ?](#heading-quand-utiliser-usememo)  
– [Formatage des données](#heading-formatage-des-donnees)  
– [Filtrage des données](#heading-filtrage-des-donnees)  
– [Tri des données](#heading-tri-des-donnees)  
– [Mémorisation des fonctions de rappel](#heading-memorisation-des-fonctions-de-rappel)  
– [Calculs coûteux](#heading-calculs-couteux)
4. [Avantages de useMemo](#heading-avantages-de-usememo)
5. [Syntaxe et utilisation du hook useMemo](#heading-syntaxe-et-utilisation-du-hook-usememo)  
– [Éviter les recalculs inutiles](#heading-eviter-les-recalculs-inutiles)  
– [Optimiser les performances de rendu](#heading-optimiser-les-performances-de-rendu)  
– [Gérer efficacement les données dérivées](#heading-gerer-efficacement-les-donnees-derivees)  
– [Améliorer l'expérience utilisateur](#heading-ameliorer-lexperience-utilisateur)
6. [Comment useMemo diffère-t-il des autres hooks comme useState et useEffect ?](#heading-comment-usememo-differe-des-autres-hooks-comme-usestate-et-useeffect)  
– [useState](#heading-usestate)  
– [useEffect](#heading-useeffect)  
– [useMemo](#heading-usememo)
7. [Comment mémoriser les calculs coûteux en utilisant useMemo](#heading-comment-memoriser-les-calculs-couteux-en-utilisant-usememo)  
– [Identifier le calcul coûteux](#heading-identifier-le-calcul-couteux)  
– [Envelopper le calcul avec useMemo](#heading-envelopper-le-calcul-avec-usememo)  
– [Spécifier les dépendances](#heading-specifier-les-dependances)
8. [Comment optimiser les calculs complexes dans les Render Props ou les composants d'ordre supérieur](#heading-comment-optimiser-les-calculs-complexes-dans-les-render-props-ou-les-composants-dordre-superieur)
9. [Comment utiliser useMemo avec des hooks personnalisés](#heading-comment-utiliser-usememo-avec-des-hooks-personnalises)
10. [Conseils pour utiliser useMemo efficacement](#heading-conseils-pour-utiliser-usememo-efficacement)  
– [Identifier les calculs coûteux](#heading-identifier-les-calculs-couteux)  
– [Choisir les bonnes dépendances](#heading-choisir-les-bonnes-dependances)  
– [Éviter la mémorisation inutile](#heading-eviter-la-memorisation-inutile)  
– [Mesurer les performances](#heading-mesurer-les-performances)
11. [Conclusion](#heading-conclusion)

## Qu'est-ce que useMemo ?

`useMemo` est un outil pratique dans React qui aide à rendre vos applications plus rapides. Imaginez que vous avez une fonction qui effectue un travail intensif, comme calculer un problème mathématique complexe ou formater des données. Normalement, React recalcule cette fonction à chaque rendu de votre composant, même si les entrées sont les mêmes. Cela peut ralentir les choses.

Mais avec `useMemo`, React se souvient du résultat de cette fonction tant que ses entrées restent les mêmes. Ainsi, si vos entrées ne changent pas, React récupère simplement le résultat stocké au lieu de le recalculer à chaque fois. Cela fait gagner du temps et rend votre application plus réactive. 

En termes simples, `useMemo` est comme avoir un assistant intelligent qui se souvient des réponses aux problèmes mathématiques, afin que vous n'ayez pas à les résoudre encore et encore.

## Comment fonctionne useMemo ?

Pour comprendre comment `useMemo` fonctionne, considérons un scénario où vous avez un composant qui rend une liste d'éléments, et vous devez effectuer un calcul intensif pour dériver la liste. 

Sans mémorisation, ce calcul intensif serait exécuté à chaque rendu, même si les entrées restent inchangées.

Voici un exemple de base sans `useMemo` :

```jsx
import React from 'react';

const ListComponent = ({ items }) => {
  const processedItems = processItems(items); // Calcul coûteux

  return (
    <ul>
      {processedItems.map(item => (
        <li key={item.id}>{item.name}</li>
      ))}
    </ul>
  );
};

const processItems = (items) => {
  // Calcul coûteux
  // Imaginez un traitement intensif ici
  return items.map(item => ({ id: item.id, name: item.name.toUpperCase() }));
};

export default ListComponent;

```

Dans cet exemple, la fonction `processItems` est appelée à chaque rendu, même si la propriété `items` reste la même. 

Pour optimiser cela, nous pouvons utiliser `useMemo` :

```jsx
import React, { useMemo } from 'react';

const ListComponent = ({ items }) => {
  const processedItems = useMemo(() => processItems(items), [items]);

  return (
    <ul>
      {processedItems.map(item => (
        <li key={item.id}>{item.name}</li>
      ))}
    </ul>
  );
};

const processItems = (items) => {
  // Calcul coûteux
  // Imaginez un traitement intensif ici
  return items.map(item => ({ id: item.id, name: item.name.toUpperCase() }));
};

export default ListComponent;

```

En enveloppant l'appel à `processItems` dans `useMemo`, React ne recalculera la valeur mémorisée que lorsque la propriété `items` changera. Cette optimisation peut améliorer considérablement les performances de votre application, en particulier lorsque vous traitez de grands ensembles de données ou des calculs complexes.

## Quand utiliser useMemo

Vous devez utiliser `useMemo` dans des scénarios où vous avez des calculs coûteux ou des transformations de données dans un composant fonctionnel qui sont recalculés inutilement à chaque rendu. 

Voici quelques exemples pratiques illustrant les scénarios d'utilisation de base pour `useMemo` :

### Formatage des données :

```jsx
const formattedData = useMemo(() => formatData(rawData), [rawData]);

```

* Utilisez `useMemo` pour formater les données brutes dans un format convivial pour l'affichage.
* Recalculez `formattedData` uniquement lorsque `rawData` change, optimisant ainsi les performances.

### Filtrage des données :

```jsx
const filteredData = useMemo(() => filterData(rawData, filterCriteria), [rawData, filterCriteria]);

```

* Utilisez `useMemo` pour filtrer une liste de données en fonction de certains critères.
* Assurez-vous que `filteredData` est recalculé uniquement lorsque `rawData` ou `filterCriteria` changent.

### Tri des données :

```jsx
const sortedData = useMemo(() => sortData(rawData, sortKey), [rawData, sortKey]);

```

* Utilisez `useMemo` pour trier une liste de données en fonction d'une clé spécifique.
* Retriez `sortedData` uniquement lorsque `rawData` ou `sortKey` changent.

### Mémorisation des fonctions de rappel :

```jsx
const handleClick = useMemo(() => {
  return () => {
    // Gérer l'événement de clic
  };
}, []);

```

* Utilisez `useMemo` pour mémoriser les fonctions de rappel afin d'éviter les recréations inutiles de fonctions à chaque rendu.
* Passez un tableau de dépendances vide (`[]`) pour vous assurer que la fonction de rappel n'est créée qu'une seule fois pendant le cycle de vie du composant.

### Calculs coûteux :

```jsx
const result = useMemo(() => {
  // Effectuer un calcul coûteux
  return performCalculation(input1, input2);
}, [input1, input2]);

```

* Utilisez `useMemo` pour mémoriser le résultat d'un calcul coûteux.
* Recalculez `result` uniquement lorsque `input1` ou `input2` changent.

Dans chacun de ces exemples, `useMemo` garantit que le calcul ou la transformation coûteux ne sont effectués que lorsque cela est nécessaire, réduisant ainsi les recalculs inutiles et optimisant les performances de vos composants fonctionnels.

## Avantages de useMemo

L'utilisation du hook `useMemo` dans les applications React offre de nombreux avantages pour l'optimisation des performances. 

### Éviter les recalculs inutiles :

Dans React, les composants se re-rendent chaque fois que leur état ou leurs propriétés changent. Si un composant effectue des calculs ou des calculs coûteux dans sa logique de rendu, ces calculs peuvent être réexécutés à chaque rendu, même si les entrées n'ont pas changé.

En utilisant `useMemo`, vous pouvez mémoriser ces calculs. React ne recalculera la valeur mémorisée que lorsque les dépendances (entrées) changent. Cela permet d'éviter les recalculs inutiles, améliorant ainsi les performances de vos composants.

### Optimiser les performances de rendu :

Les composants React peuvent devenir lents à rendre s'ils effectuent des calculs ou des transformations lourds lors de chaque cycle de rendu. Cela est particulièrement problématique dans les applications à grande échelle ou les composants qui se rendent fréquemment.

`useMemo` vous permet de mémoriser les résultats de ces calculs, garantissant qu'ils ne sont effectués que lorsque cela est nécessaire. Cela peut entraîner des améliorations significatives des performances de rendu en réduisant la charge de calcul de vos composants.

### Gérer efficacement les données dérivées :

Dans de nombreuses applications React, les données dérivées sont calculées à partir de l'état ou des propriétés des composants. Par exemple, les propriétés calculées, les listes filtrées ou les données formatées sont souvent dérivées de sources de données brutes.

La mémorisation des données dérivées avec `useMemo` garantit que ces calculs sont effectués efficacement et uniquement lorsque cela est nécessaire. Cela peut prévenir les re-rendus inutiles et optimiser les performances globales de votre application.

### Améliorer l'expérience utilisateur :

L'optimisation des performances est cruciale pour offrir une expérience utilisateur fluide et réactive. Des composants lents ou non réactifs peuvent entraîner une mauvaise expérience utilisateur et frustrer les utilisateurs.

En utilisant `useMemo` pour optimiser les performances de vos composants, vous pouvez vous assurer que votre application reste rapide et réactive, améliorant ainsi la satisfaction et l'engagement des utilisateurs.

`useMemo` est essentiel pour l'optimisation des performances dans les applications React car il permet d'éviter les recalculs inutiles, d'optimiser les performances de rendu, de gérer efficacement les données dérivées et d'améliorer l'expérience utilisateur globale. 

En mémorisant les calculs coûteux avec `useMemo`, vous pouvez créer des composants React rapides, réactifs et efficaces qui offrent une expérience utilisateur fluide.

## Syntaxe et utilisation du hook useMemo

Le hook `useMemo` dans React est utilisé pour mémoriser les calculs coûteux. Sa syntaxe est simple et il prend deux arguments : une fonction représentant le calcul à mémoriser et un tableau de dépendances. 

Voici la syntaxe et l'utilisation du hook `useMemo` :

```jsx
import React, { useMemo } from 'react';

const MyComponent = ({ data }) => {
  // Mémoriser le résultat du calcul coûteux
  const memoizedValue = useMemo(() => {
    // Effectuer un calcul coûteux en utilisant les données
    return processData(data);
  }, [data]); // Tableau de dépendances : recalculer si 'data' change

  return (
    <div>
      {/* Rendre la valeur mémorisée */}
      <p>{memoizedValue}</p>
    </div>
  );
};

export default MyComponent;

```

Dans cet exemple :

1. Nous importons `useMemo` de la bibliothèque React.
2. À l'intérieur du composant fonctionnel `MyComponent`, nous déclarons une constante `memoizedValue` en utilisant le hook `useMemo`.
3. Le premier argument de `useMemo` est une fonction qui effectue le calcul coûteux. Dans ce cas, nous appelons la fonction `processData` et passons `data` comme paramètre.
4. Le deuxième argument de `useMemo` est un tableau de dépendances. React ne recalculera la valeur mémorisée que si l'une de ces dépendances change. Ici, nous spécifions `[data]` comme tableau de dépendances, indiquant que `memoizedValue` doit être recalculé chaque fois que la propriété `data` change.
5. Enfin, nous rendons la `memoizedValue` à l'intérieur du JSX du composant.

En utilisant `useMemo`, nous nous assurons que le calcul coûteux à l'intérieur de la fonction n'est exécuté que lorsque cela est nécessaire, optimisant ainsi les performances de notre composant.

## Comment useMemo diffère-t-il des autres hooks comme useState et useEffect ?

`useMemo` diffère des autres hooks comme `useState` et `useEffect` dans son but et la manière dont il affecte le comportement des composants :

### useState :

* `useState` est utilisé pour gérer l'état dans les composants fonctionnels.
* Il permet de créer et de mettre à jour des variables d'état, déclenchant des re-rendus lorsque leurs valeurs changent.
* Les variables d'état gérées par `useState` sont généralement utilisées pour stocker des données qui peuvent changer au fil du temps, comme les entrées de formulaire, les bascules ou les compteurs.

### useEffect :

* `useEffect` est utilisé pour gérer les effets secondaires dans les composants fonctionnels.
* Il s'exécute après chaque rendu et permet d'effectuer des tâches comme la récupération de données, les abonnements ou la manipulation du DOM.
* `useEffect` permet de séparer les effets secondaires de la logique principale du composant, gardant vos composants propres et organisés.

### useMemo :

* `useMemo` est utilisé pour mémoriser les calculs coûteux dans les composants fonctionnels.
* Il met en cache le résultat d'une fonction et retourne le résultat mis en cache lorsque les entrées de la fonction restent inchangées.
* Contrairement à `useState` et `useEffect`, qui gèrent respectivement l'état et les effets secondaires, `useMemo` se concentre uniquement sur l'optimisation des performances en évitant les recalculs inutiles.

Alors que `useState` et `useEffect` sont utilisés pour gérer l'état et les effets secondaires, respectivement, `useMemo` est spécifiquement conçu pour l'optimisation des performances en mémorisant les calculs. Chaque hook sert un but distinct dans le développement React, mais ils peuvent être utilisés ensemble pour construire des composants efficaces et maintenables.

## Comment mémoriser les calculs coûteux en utilisant useMemo

Pour mémoriser les calculs coûteux en utilisant `useMemo`, suivez ces étapes :

### Identifier le calcul coûteux : 

Déterminez quels calculs dans votre composant sont coûteux et bénéficieraient de la mémorisation. Ceux-ci pourraient inclure des calculs complexes, des transformations de données ou des appels de fonctions qui consomment des ressources significatives.

### Envelopper le calcul avec useMemo : 

Utilisez le hook `useMemo` pour mémoriser le résultat du calcul. Le premier argument de `useMemo` est une fonction qui effectue le calcul, et le deuxième argument est un tableau de dépendances.

### Spécifier les dépendances : 

Fournissez un tableau de dépendances à `useMemo` pour indiquer quand la valeur mémorisée doit être recalculée. Si l'une des dépendances change, `useMemo` recalculera la valeur mémorisée.

Voici un exemple de la manière de mémoriser un calcul coûteux en utilisant `useMemo` :

```jsx
import React, { useMemo } from 'react';

const MyComponent = ({ data }) => {
  // Mémoriser le résultat du calcul coûteux
  const memoizedValue = useMemo(() => {
    // Effectuer le calcul coûteux ici
    return processData(data);
  }, [data]); // 'data' est une dépendance

  return (
    <div>
      {/* Rendre la valeur mémorisée */}
      <p>{memoizedValue}</p>
    </div>
  );
};

export default MyComponent;

```

Dans cet exemple :

* Nous utilisons `useMemo` pour mémoriser le résultat de la fonction `processData`, qui effectue le calcul coûteux.
* La propriété `data` est spécifiée comme une dépendance dans le tableau de dépendances `[data]`. Cela signifie que `memoizedValue` sera recalculé chaque fois que la propriété `data` change.
* La valeur mémorisée (`memoizedValue`) est ensuite rendue à l'intérieur du JSX du composant.

En mémorisant le calcul coûteux avec `useMemo`, nous nous assurons qu'il n'est recalculé que lorsque cela est nécessaire, optimisant ainsi les performances de notre composant.

## Comment optimiser les calculs complexes dans les Render Props ou les composants d'ordre supérieur

`useMemo` peut également être utilisé efficacement dans les render props ou les composants d'ordre supérieur (HOC) pour optimiser les calculs complexes. Considérez l'exemple de HOC suivant :

```jsx
import React, { useMemo } from 'react';

const withDataFetching = (WrappedComponent) => {
  return function WithDataFetching({ data }) {
    // Mémoriser le calcul de processedData
    const processedData = useMemo(() => processData(data), [data]);

    return <WrappedComponent processedData={processedData} />;
  };
};

const DisplayData = ({ processedData }) => {
  return (
    <div>
      {processedData.map(item => (
        <div key={item.id}>{item.name}</div>
      ))}
    </div>
  );
};

const processData = (data) => {
  // Calcul coûteux
  // Imaginez un traitement intensif ici
  return data.map(item => ({ id: item.id, name: item.name.toUpperCase() }));
};

export default withDataFetching(DisplayData);

```

Dans cet exemple, `processedData` est mémorisé dans le HOC `withDataFetching` en utilisant `useMemo`. Cette optimisation garantit que le calcul intensif dans `processData` n'est effectué que lorsque la propriété `data` change, améliorant ainsi les performances globales du composant.

## Comment utiliser useMemo avec des hooks personnalisés

Un autre cas d'utilisation puissant pour `useMemo` est dans les hooks personnalisés pour mémoriser les valeurs entre les composants. Créons un hook personnalisé qui récupère des données depuis une API et mémorise le résultat :

```jsx
import { useState, useEffect, useMemo } from 'react';

const useDataFetching = (url) => {
  const [data, setData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch(url);
      const result = await response.json();
      setData(result);
    };

    fetchData();
  }, [url]);

  // Mémoriser la valeur des données
  const memoizedData = useMemo(() => data, [data]);

  return memoizedData;
};

export default useDataFetching;

```

Maintenant, chaque fois que nous utilisons le hook `useDataFetching` dans un composant, la valeur `data` sera mémorisée en utilisant `useMemo`. Cela garantit que les données récupérées ne sont recalculées que lorsque l'URL change, évitant ainsi les appels API inutiles et améliorant les performances entre les composants.

## Conseils pour utiliser useMemo efficacement

Voici quelques conseils pour utiliser `useMemo` efficacement :

1. Identifier les calculs coûteux : Identifiez les parties de votre application qui impliquent des calculs ou des calculs lourds.
2. Choisir les bonnes dépendances : Assurez-vous d'inclure toutes les dépendances nécessaires dans le tableau de dépendances. Des dépendances manquantes pourraient entraîner un comportement inattendu.
3. Éviter la mémorisation inutile : Évitez de mémoriser des valeurs qui n'ont pas besoin de l'être, car cela peut ajouter une complexité inutile à votre code.
4. Mesurer les performances : Utilisez des outils de surveillance des performances pour mesurer l'impact de `useMemo` sur les performances de votre application et ajustez en conséquence.

## Conclusion

`useMemo` est un outil puissant pour optimiser les performances de vos applications React en mémorisant le résultat de calculs coûteux. 

En utilisant `useMemo` efficacement, vous pouvez prévenir les re-rendus inutiles et améliorer la réactivité globale de votre application. 

Alors, ne négligez pas `useMemo` simplement parce qu'il semble intimidant. Adoptez-le comme un outil précieux dans votre parcours de développement React, et exploitez son potentiel pour créer des applications web plus rapides et plus efficaces.