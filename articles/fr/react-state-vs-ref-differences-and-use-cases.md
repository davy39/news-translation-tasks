---
title: React State vs Refs – Différences et Cas d'Utilisation
subtitle: ''
author: Timothy Olanrewaju
co_authors: []
series: null
date: '2024-04-11T13:07:51.000Z'
originalURL: https://freecodecamp.org/news/react-state-vs-ref-differences-and-use-cases
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/STATE-VS-REF.png
tags:
- name: React
  slug: react
- name: 'State Management '
  slug: state-management
seo_title: React State vs Refs – Différences et Cas d'Utilisation
seo_desc: 'In this article, we''ll delve into a thorough comparison of React state
  and refs, exploring their suitability for specific scenarios.

  When faced with the need to store data in your React application, the first question
  that comes to mind is: "Will the...'
---

Dans cet article, nous allons examiner en détail une comparaison entre le `state` et les `refs` de React, en explorant leur adéquation pour des scénarios spécifiques.

Lorsque vous êtes confronté à la nécessité de stocker des données dans votre application React, la première question qui vient à l'esprit est : "Les données changeront-elles à un moment donné pendant le cycle de vie du composant ?" Si ce n'est pas le cas, une variable `const` régulière est bien adaptée. 

Cependant, si les données vont changer, c'est là que les hooks `useState` et `useRef` entrent en jeu.

## Comprendre les Hooks useState et useRef

### Hook useState

Le hook `useState` est conçu pour gérer l'état d'un composant, qui représente des données pouvant changer au fil du temps et importantes pour le rendu du composant. Vous pouvez ajouter un état à votre composant en important le hook `useState` de React.

```react
import { useState } from 'react';
```

Le hook `useState` est généralement initialisé avec une valeur initiale et retourne un tableau contenant une variable d'état déclarée et sa fonction de mise à jour associée. Cela ressemble à ceci :

```react
import { useState } from "react";

function App() {
  const [count, setCount] = useState(0); // hook useState déclaré
  
  return (
    <>
      <h1>Exemple d'état</h1>
      <div>
        <button onClick={() => setCount((count) => count + 1)}>
          count est {count}
        </button>
      </div>
    </>
  );
}
export default App;
```

Dans le code ci-dessus,

1. Le `useState` est initialisé avec une valeur de zéro et retourne une variable `count` et une fonction de mise à jour `setCount`.
2. La variable `count` est mise à jour dynamiquement par la fonction de mise à jour `setCount` qui incrémente `count` de 1. 
3. À chaque clic sur le bouton, le composant `App` est réaffiché et la valeur mise à jour est affichée dans le texte du bouton.

Avoir une bonne compréhension de l'état de React est important car c'est l'un des concepts les plus utilisés. Vous pouvez lire un article plus approfondi sur les états ici : [State Management in React](https://www.freecodecamp.org/news/react-state-management/).

### Hook useRef

Le hook `useRef` est utilisé pour créer des refs dans les composants React. Une ref est un objet avec une propriété `current` qui contient une valeur. Elle référence essentiellement un élément DOM ou une instance d'un composant. Nous pouvons lire et mettre à jour la valeur en accédant à la propriété current.

```react
const ref = useRef(initialValue)

ref.current = initialValue
```

Voici un extrait de code complet d'une ref en action :

```react
import { useRef } from "react";

function App() {
  let ref = useRef(0); 
  
  function handleIncrease() {
    ref.current++;
    alert(`Vous avez cliqué dessus ${ref.current} fois`);
  }
  return (
    <>
      <h1>Exemple de Ref</h1>
      <div>
        <button onClick={handleIncrease}>Cliquez Moi</button>
      </div>
    </>
  );
}

export default App;
```

Décomposons cela :

1. Nous avons importé `useRef` de React.
2. Dans notre composant `App`, nous avons déclaré un objet `ref` avec une valeur initiale définie à zéro.
3. `handleIncrease` est notre fonction de gestion qui incrémente la valeur `ref.current` de 1 et alerte ensuite l'utilisateur de la valeur actuelle.
4. Dans le JSX de notre composant `App`, nous avons un bouton avec une prop `onClick` et la fonction de gestion `handleIncrease` qui lui est passée.

Ayant compris comment les deux hooks fonctionnent, nous allons les comparer et explorer quand ils seraient adaptés à utiliser.

## React State vs Ref

### Déclenchement du Rendu

Dans React, les états déclenchent toujours un nouveau rendu en raison d'un mécanisme connu sous le nom de `reconciliation` – qui met à jour l'interface utilisateur en fonction des changements apportés à l'état ou aux props. 

En coulisses, React compare le nouvel état à l'ancien et calcule les changements minimaux nécessaires pour mettre à jour l'interface utilisateur qui reflète le nouvel état. Ce processus garantit la cohérence avec l'état ou les props modifiés.

En revanche, les refs ne déclenchent pas de nouveau rendu lorsque des changements leur sont apportés. Les refs ne sont pas directement liés au cycle de rendu du composant. 

Par conséquent, si vous souhaitez une interface utilisateur cohérente qui réagit aux changements de données, il est conseillé d'utiliser des états. Les refs sont mieux utilisés pour gérer des valeurs mutables sans affecter l'interface utilisateur.

### Mutabilité

L'état de React ne peut pas être changé directement une fois qu'il a été défini car la fonction de mise à jour met à jour la variable d'état. En utilisant cette approche, React maintient la prévisibilité et la stabilité du flux de données. Cela aide également à faciliter le débogage.

À l'inverse, les refs sont mutables car vous pouvez modifier la valeur `ref current` en dehors du processus de rendu. Les valeurs peuvent être changées à tout moment contrairement aux états – les refs n'ont pas de fonction de mise à jour. 

### Opérations de Lecture/Écriture

La fonction de mise à jour du hook `useState` vous permet de mettre à jour la valeur de l'état. Par exemple :

```react
const [state, setState] = useState(false)
function handleOpposite(){
	setState(!state)
 }
```

Dans ce code, nous pouvons voir que :

1. La valeur initiale est définie à une valeur booléenne de `false`.
2. La fonction `handleOpposite` nie la valeur booléenne de `state` et `setState` contient la valeur mise à jour de `true`.

Dans cette opération simple,

1. Une opération de **lecture** implicite a été effectuée car la valeur initiale a dû être accessible avant la négation.
2. Une opération d'**écriture** s'est produite lorsque la négation (!) a été utilisée sur la valeur initiale, ce qui a changé la valeur en son opposé.

Une opération de **lecture** explicite de l'état se produit lorsque vous accédez simplement à la variable d'état directement dans le JSX d'un composant. Par exemple :

```
<button onClick={() => setCount((count) => count + 1)}>
  count est {count}
 </button>
```

Le `{count}` est la valeur actuellement accessible de l'état et sera affiché sur l'UI en conséquence.

D'autre part, accéder ou modifier la valeur actuelle d'une `ref` pendant le rendu peut interférer avec le processus de réconciliation de React, potentiellement causant des incohérences entre le DOM virtuel et le DOM réel. 

Afin d'assurer un comportement prévisible et des performances optimales dans les composants, il est préférable de suivre les directives de React et d'éviter d'accéder ou de modifier les refs pendant le rendu.

### Persistance à Travers les Rendus

La persistance des données à travers les rendus dans React signifie que les données restent cohérentes et disponibles entre différents cycles de rendu d'un composant. Lorsque les données sont persistantes, elles restent inchangées et accessibles après un nouveau rendu. L'état et les refs persistent tous deux les données à travers les rendus.

La persistance est cruciale pour maintenir l'intégrité de l'état de l'application et garantit que les composants fonctionnent comme prévu. 

### Mises à Jour Asynchrones

Les mises à jour de l'état de React sont asynchrones, ce qui signifie que lorsqu'il y a une demande de mise à jour, il est possible que les mises à jour ne soient pas exécutées immédiatement. React peut laisser certaines modifications d'état pour plus tard tout en mettant à jour d'autres composants en une seule fois !

Les mises à jour des refs sont effectuées de manière synchrone où les tâches sont exécutées de manière séquentielle. Chaque tâche attend que la précédente se termine avant de commencer, garantissant qu'elles sont exécutées de manière prévisible et déterministe.

## Conclusion

Dans cet article, nous avons examiné en détail les hooks — `useState` et `useRef` — qui gèrent les données dynamiques (données qui changeront) dans les applications React. 

Nous avons comparé les deux hooks et à ce stade, vous devriez connaître leurs similitudes, différences, quand et où ils sont les mieux adaptés.

Connectez-vous avec moi sur [LinkedIn](https://www.linkedin.com/in/timothy-olanrewaju750/) pour des discussions et des publications liées au développement front-end. À la prochaine !