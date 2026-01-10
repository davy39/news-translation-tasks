---
title: "Mise en cache dans React \x13 Comment utiliser les hooks useMemo et useCallback"
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-15T18:39:25.000Z'
originalURL: https://freecodecamp.org/news/caching-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/caching-react.jpg
tags:
- name: caching
  slug: caching
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: "Mise en cache dans React \x13 Comment utiliser les hooks useMemo et useCallback"
seo_desc: "By Scott Gary\nAs you become more proficient at coding in React, performance\
  \ will become a major focal point in your development process. \nAs with any tool\
  \ or programming methodology, caching plays a huge role when it comes to optimizing\
  \ React applica..."
---

Par Scott Gary

À mesure que vous devenez plus compétent en codant avec React, la performance deviendra un point focal majeur dans votre processus de développement.

Comme avec tout outil ou méthodologie de programmation, la mise en cache joue un rôle énorme lorsqu'il s'agit d'optimiser les applications React.

La mise en cache dans React est généralement appelée _mémoisation_. Elle est utilisée pour améliorer les performances en réduisant le nombre de fois qu'un composant est rendu en raison de mutations d'état ou de props.

React fournit deux API pour la mise en cache : useMemo et useCallback. useCallback est un hook qui mémoïse une fonction, tandis que useMemo est un hook qui mémoïse une valeur. Ces deux hooks sont souvent utilisés en conjonction avec l'API Context pour améliorer davantage l'efficacité.

Voici une liste de base des sujets que nous allons aborder dans cet article :

1. Comportement de mise en cache par défaut de React.
2. Le hook useMemo.
3. Le hook useCallback.

Pour suivre, vous aurez besoin d'une bonne compréhension de React et des composants avec état.

## Comportement de mise en cache par défaut dans React

Par défaut, [React](https://www.ohmycrawl.com/react/) utilise une technique appelée "comparaison superficielle" pour déterminer si un composant doit être re-rendu. Cela signifie essentiellement que si les props ou l'état d'un composant n'ont pas changé, React supposera que la sortie du composant n'a pas changé non plus et ne le re-rendra pas.

Bien que ce comportement de mise en cache par défaut soit très efficace en soi, il n'est pas toujours suffisant pour optimiser les composants complexes qui nécessitent une gestion d'état avancée.

Afin d'obtenir plus de contrôle sur le comportement de mise en cache et de rendu de votre composant, React offre les hooks **useMemo** et **useCallback**.

## Mise en cache dans React avec le hook useMemo

useMemo est utile lorsque vous devez effectuer un calcul coûteux pour récupérer une valeur, et que vous souhaitez vous assurer que le calcul n'est effectué que lorsque cela est nécessaire. En mémoïsant la valeur avec useMemo, vous pouvez vous assurer que la valeur n'est calculée que lorsque ses dépendances changent.

Dans un composant React, vous pouvez avoir plusieurs propriétés qui constituent votre état. Si une partie de l'état change et n'a rien à voir avec notre valeur coûteuse, pourquoi la recalculer si elle n'a pas changé ?

Voici un exemple de bloc de code reflétant une implémentation de base de useMemo :

```
react
import React, { useState, useMemo } from 'react';
function Example() {
const [txt, setTxt] = useState("Some text");
const [a, setA] = useState(0);
const [b, setB] = useState(0);
const sum = useMemo(() => {
console.log('Computing sum...');
return a + b;
}, [a, b]);
return (
<div>
<p>Text: {txt}</p>
<p>a: {a}</p>
<p>b: {b}</p>
<p>sum: {sum}</p>
<button onClick={() => setTxt("New Text!")}>Set Text</button>
<button onClick={() => setA(a + 1)}>Increment a</button>
<button onClick={() => setB(b + 1)}>Increment b</button>
</div>
);
}
```

Dans notre composant Example ci-dessus, supposons que la fonction **sum()** effectue un calcul coûteux. Si l'état **txt** est mis à jour, React va re-rendre notre composant, mais parce que nous avons mémoïse la valeur retournée de sum, cette fonction ne s'exécutera pas à nouveau à ce moment-là.

La seule fois où la fonction **sum()** s'exécutera est si l'état **a** ou **b** a été muté (changé). C'est une excellente amélioration par rapport au comportement par défaut, qui réexécutera cette méthode à chaque re-rendu.

## Mise en cache dans React avec le hook useCallback

useCallback est utile lorsque vous devez passer une fonction en tant que prop à un composant enfant, et que vous souhaitez vous assurer que la référence de la fonction ne change pas inutilement. En mémoïsant la fonction avec useCallback, vous pouvez vous assurer que la référence de la fonction reste la même tant que ses dépendances ne changent pas.

Sans entrer trop dans les détails des références de fonctions JavaScript, examinons simplement comment elles peuvent affecter le rendu de votre application React. Lorsque la référence d'une fonction change, tout composant enfant qui reçoit la fonction en tant que prop se re-rendra, même si la logique de la fonction elle-même n'a pas changé.

C'est parce que, comme nous l'avons déjà mentionné, React effectue une comparaison superficielle des valeurs des props pour déterminer si un composant doit être re-rendu, et une nouvelle référence de fonction sera toujours considérée comme une valeur différente de la précédente.

En d'autres termes, le simple fait de redéclarer une fonction (même la même fonction exacte) fait changer la référence, et provoquera le re-rendu inutile du composant enfant qui reçoit la fonction en tant que prop.

Voici un exemple de bloc de code reflétant une implémentation de base de useCallback :

```
react
import React, { useState, useCallback } from 'react';
function ChildComponent({ onClick }) {
console.log('ChildComponent is rendered');
return (
<button onClick={onClick}>Click me</button>
);
}
function Example() {
const [count, setCount] = useState(0);
const [txt, setTxt] = useState("Some text...");
const incrementCount = useCallback(() => {
setCount(prevCount => prevCount + 1);
}, [setCount]);
return (
<div>
<p>Text: {txt}</p>
<p>Count: {count}</p>
<button onClick={setTxt}>Set Text</button>
<button onClick={setCount}>Increment</button>
<ChildComponent onClick={incrementCount} />
</div>
);
}
```

Comme vous pouvez le voir dans l'exemple ci-dessus, nous passons la méthode **incrementCount** au lieu de la méthode **setCount** au composant enfant. C'est parce que **incrementCount** est mémoïsée, et lorsque nous exécutons notre méthode **setTxt**, elle ne provoquera pas le re-rendu inutile du composant enfant.

La seule façon pour que notre composant enfant se re-rende dans cet exemple est si la méthode **setCount** s'exécute, car nous l'avons passée en tant que paramètre de dépendance à notre mémoïsation **useCallback**.

## Conclusion

La mise en cache est une technique importante pour optimiser les applications React. En réduisant les re-rendus inutiles, la mise en cache peut aider à améliorer les performances et l'efficacité de votre application.

React fournit un comportement de mise en cache par défaut en utilisant un DOM virtuel pour comparer les changements d'état et de props, et ne met à jour les composants qu'après qu'une comparaison superficielle reflète les changements. C'est une excellente technique d'optimisation qui est suffisante dans de nombreux scénarios, mais parfois un contrôle plus fin est souhaité.

Les hooks useMemo et useCallback ont été créés pour atteindre ce contrôle fin.

useMemo est utilisé pour mémoïser les _résultats_ d'un appel de fonction, et est utile lorsque la fonction est coûteuse à calculer et que le résultat ne change pas souvent.

useCallback est utilisé pour mémoïser la référence réelle d'une fonction plutôt que la valeur retournée, et est utilisé lorsque la fonction est passée en tant que prop à des composants enfants qui pourraient provoquer des re-rendus inutiles.

Vous voulez en savoir plus ? Pour en savoir plus, consultez le [OhMyCrawl Blog](https://www.ohmycrawl.com/blog/) pour plus de conseils de programmation pour le SEO.