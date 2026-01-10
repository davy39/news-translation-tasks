---
title: Comment éviter les boucles infinies lors de l'utilisation de useEffect() dans
  ReactJS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-04-26T14:07:12.000Z'
originalURL: https://freecodecamp.org/news/prevent-infinite-loops-when-using-useeffect-in-reactjs
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/preventing-infinite-loops-react.png
tags:
- name: Loops
  slug: loops
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: Comment éviter les boucles infinies lors de l'utilisation de useEffect()
  dans ReactJS
seo_desc: 'By Roy Chng

  The useEffect hook in React has become a common tool for managing side effects in
  functional components. But there''s a common pitfall when using it: the potential
  for infinite loops. These can cause performance issues and disrupt the inte...'
---

Par Roy Chng

Le hook `useEffect` dans React est devenu un outil courant pour gérer les effets secondaires dans les composants fonctionnels. Mais il y a un piège courant lors de son utilisation : le potentiel de boucles infinies. Celles-ci peuvent causer des problèmes de performance et perturber le comportement prévu des composants.

Dans ce tutoriel, nous allons explorer comment éviter les boucles infinies lors de l'utilisation de `useEffect` dans React.

Vous utilisez le hook `useEffect` dans les composants fonctionnels de React pour gérer les effets secondaires, tels que la récupération de données depuis une API, la mise à jour du DOM, ou l'abonnement à des événements externes à React.

# Situations qui causent des boucles infinies

## Dépendances manquantes

Une erreur courante qui peut causer des boucles infinies est de ne pas spécifier un tableau de dépendances. `useEffect` vérifie si les dépendances ont changé après chaque rendu du composant.

Ainsi, lorsqu'aucune dépendance n'est fournie, l'effet s'exécutera après chaque rendu, ce qui peut entraîner une boucle continue de mises à jour si l'état est mis à jour.

Par exemple, considérons le code suivant :

```js
function ExampleComponent(){
    const [count, setCount] = useState(0);

    useEffect(() => {
        setCount((count) => count+1);
    });
}
```

Dans cet exemple, voici ce qui se passe :

* Lorsque le composant est initialement rendu, l'effet s'exécute.
* Lorsque l'effet est exécuté, il met à jour l'état du compteur, ce qui entraîne un nouveau rendu du composant.
* Puisque le composant est rendu à nouveau, cela provoque l'exécution de `useEffect` une nouvelle fois.
* Cela provoque une nouvelle mise à jour de l'état `count`, et ainsi de suite à l'infini.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/useEffect-code-1-6.gif)
_Animation montrant le processus d'une boucle infinie causée par useEffect_

Cela s'est produit parce qu'il n'y a pas de tableau de dépendances spécifié, indiquant que l'effet doit être exécuté à chaque fois après que le composant est rendu à nouveau.

Pour éviter cela, ajoutez un tableau de dépendances vide :

```js
function ExampleComponent(){
    const [count, setCount] = useState(0);

    useEffect(() => {
        setCount((count) => count+1);
    }, []);
}
```

Cela garantira que l'effet est exécuté uniquement après le rendu initial du composant.

Alternativement, si votre effet dépend d'un certain état, n'oubliez pas de l'ajouter comme dépendance :

```js
function ExampleComponent(){
    const [isLoggedIn, setIsLoggedIn] = useState(false);

    useEffect(() => {
        // logique
    }), [isLoggedIn];
}
```

De cette manière, l'effet est exécuté uniquement au début et lorsque la dépendance a changé après que le composant a été rendu à nouveau.

## Utilisation de références comme dépendances

En JavaScript, les types de données peuvent être catégorisés comme étant des valeurs de référence ou des valeurs primitives.

Les valeurs primitives sont des types de données de base tels que les chaînes de caractères, les booléens, les nombres, null et undefined.

D'autre part, les valeurs de référence sont des types de données plus complexes tels que les tableaux et les objets.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/primitive-vs-reference-values.png)
_Types de valeurs primitives et de référence en JavaScript_

Lorsqu'une valeur de référence est assignée à une variable, la valeur et l'emplacement de cette valeur sont stockés et la variable pointera uniquement vers cet emplacement.

Alors qu'avec une valeur primitive, la variable est directement assignée à la valeur de la primitive. La valeur est stockée dans une pile, une structure de données utilisée pour stocker des données statiques.

Avec des valeurs de référence telles que les fonctions et les objets, elles sont stockées dans un tas, une structure de données utilisée pour l'allocation dynamique de mémoire, ce qui est utile lors du stockage de types de données complexes.

La variable est ensuite assignée à l'emplacement dans la pile, qui pointe vers la valeur de référence dans le tas.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/stack-vs-heap.png)
_Un tas est une structure de données utilisée pour stocker des valeurs de référence_

Cela aide à rendre nos applications plus efficaces. Imaginez devoir créer un duplicata d'un objet complexe chaque fois qu'il est réassigné à une nouvelle variable ! Au lieu de cela, la nouvelle variable peut simplement pointer vers le même emplacement dans le tas.

Aussi utile que cela soit, les valeurs de référence peuvent poser problème lorsqu'elles sont utilisées comme dépendance. Cela est dû au fait que React comparera l'emplacement de la valeur de référence si elle est utilisée comme dépendance au lieu du contenu de la valeur.

Par exemple, considérons le composant :

```js
function ExampleComponent(props){
    const [count, setCount] = useState(1);
    let data = {
        a: 1,
        b: 2
    };
    useEffect(() => {
        setCount((count) => count+1);
        // autre logique
    }, [data]);
}
```

Dans ce cas, voici ce qui se passe :

* Lorsque le composant est initialement rendu, l'effet est exécuté
* Lorsque l'effet est exécuté, l'état est mis à jour. Cela provoque un nouveau rendu du composant
* Lorsque le composant est rendu à nouveau, un nouvel objet `data` est créé, donc son emplacement de référence est différent de celui précédent
* Cela provoque l'exécution de l'effet à nouveau puisque l'objet de dépendance `data` a changé
* Le cycle se répète, causant une boucle infinie

Pour éviter que cela ne se produise, nous pouvons utiliser le hook `useRef`. Il nous permet de réutiliser la même valeur entre les rendus.

Ce hook nous permet de stocker des valeurs qui persisteront entre les rendus, donc l'emplacement de référence de l'objet sera le même tout au long de tous les cycles de rendu.

```js
function ExampleComponent(props){
    const [count, setCount] = useState(1);
    const data = useRef({
        a: 1,
        b: 2,
    });
    useEffect(() => {
        setCount((count) => count+1);
        // logique
    }, [data.current]);
        
    // reste du composant
}
```

Le hook `useRef` prend une valeur initiale et retourne un seul objet avec une propriété appelée `current`.

La propriété `current` sera la valeur passée dans le hook `useRef`, et sera la même tout au long de tous les rendus du composant.

Cela garantit que l'effet ne s'exécute pas dans une boucle infinie puisque la dépendance dans le hook `useEffect` ne changera plus à chaque rendu du composant.

Notez que vous pouvez également changer la valeur de la propriété `data.current`. Par exemple :

```js
data.current = {c: 3, d: 4}
```

En changeant la valeur de `data.current`, cela **ne déclenchera pas** le rendu à nouveau du composant et React **n'est pas** conscient de ce changement.

## Utilisation de fonctions comme dépendances

Une autre raison pour laquelle `useEffect` peut causer une boucle infinie est si vous utilisez une fonction comme dépendance.

Puisqu'une fonction est une valeur de référence en JavaScript, nous rencontrons le même problème qu'avec l'utilisation d'objets comme dépendances.

Par exemple, si nous avons une fonction dans notre composant, la fonction sera recréée chaque fois que le composant est rendu à nouveau :

```js
function ExampleComponent(props){
    const [count, setCount] = useState(1);
    const submitForm = (event) => {
        // logique
    };
    useEffect(() => {
        setCount((count) => count+1);
        // logique
    }, [submitForm]);
    
    // reste du composant
}
```

Ainsi, lorsque le composant est initialement rendu :

* L'effet est exécuté initialement, provoquant la mise à jour de l'état `count`
* Puisque l'état a été mis à jour, le composant est rendu à nouveau, provoquant la recréation de la fonction `submitForm`
* L'effet s'exécutera à nouveau car la dépendance `submitForm` du hook `useEffect` a changé
* Lorsque l'effet s'exécute à nouveau, l'état `count` est mis à jour et la boucle continue

Pour éviter que la fonction ne soit recréée chaque fois que le composant est rendu à nouveau, nous pouvons utiliser le hook `useCallback` :

```js
function ExampleComponent(props){
    const [count, setCount] = useState(1);
    const submitForm = useCallback((event) => {
        // logique
    }, []);
    useEffect(() => {
        setCount((count) => count++);
        // logique
    }, [submitForm]);
    
    // reste du composant
}
```

Le hook `useCallback` accepte également deux arguments, le premier étant la fonction qui doit être mise en cache et stockée sans changer entre les rendus, et le second étant un tableau de dépendances. Si les dépendances dans le hook `useCallback` changent, la fonction est recréée.

Ainsi, similaire à l'utilisation de `useEffect`, nous pouvons utiliser un tableau de dépendances vide pour nous assurer que la fonction n'est pas recréée entre les rendus.

Cela empêche l'effet de s'exécuter dans une boucle infinie lorsqu'une fonction est utilisée comme dépendance.

## Résumé

Le hook `useEffect` dans React est nécessaire lors de la gestion des effets secondaires dans vos composants React. Mais même avec de l'expérience, des erreurs courantes peuvent entraîner des boucles infinies dans vos composants. Assurez-vous de surveiller les dépendances manquantes, et l'utilisation de références ou de fonctions comme dépendances lorsque cela se produit.

Nous avons également examiné comment utiliser les hooks `useRef` et `useCallback` pour empêcher les objets d'être recréés entre les rendus.

Si vous aimez mes écrits, envisagez de consulter ma [chaîne YouTube](https://www.youtube.com/@turbinethree) pour plus de contenu.

Bon codage !