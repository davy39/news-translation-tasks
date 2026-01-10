---
title: Le Prop Drilling dans React expliqué avec des exemples
subtitle: ''
author: Joan Ayebola
co_authors: []
series: null
date: '2024-03-27T14:00:52.000Z'
originalURL: https://freecodecamp.org/news/prop-drilling-in-react-explained-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/Ivory-and-Blue-Lavender-Aesthetic-Photo-Collage-Presentation--14-.png
tags:
- name: React
  slug: react
seo_title: Le Prop Drilling dans React expliqué avec des exemples
seo_desc: "Have you ever struggled to understand how data flows through your React\
  \ application? Prop drilling can be a culprit. \nProp drilling refers to the process\
  \ of passing down props through multiple layers of components, even when some of\
  \ those components ..."
---

Avez-vous déjà eu du mal à comprendre comment les données circulent dans votre application React ? Le prop drilling peut en être la cause.

Le prop drilling fait référence au processus de transmission de props à travers plusieurs couches de composants, même lorsque certains de ces composants n'utilisent pas directement les props.

Cela peut entraîner des défis tels que des maux de tête de débogage, des comportements inattendus dus aux mutations de props, et des composants fortement couplés et difficiles à réutiliser.

Dans cet article, nous allons discuter de ce qu'est le prop drilling, de ses pièges, et introduire des techniques pour garder vos composants indépendants et votre code maintenable.

## Qu'est-ce que le Prop Drilling ?

Le prop drilling, également connu sous le nom de "threading props" ou "component chaining", fait référence au processus de transmission de données d'un composant parent à des composants enfants imbriqués via des props.

Le prop drilling se produit lorsqu'une prop doit être transmise à travers plusieurs couches de composants imbriqués pour atteindre un composant enfant profondément imbriqué qui a réellement besoin de la prop. Chaque composant intermédiaire dans la hiérarchie doit transmettre la prop, même s'il ne l'utilise pas lui-même.

Considérons un scénario où vous avez un composant de haut niveau qui récupère des données depuis une API et doit transmettre ces données à plusieurs composants enfants imbriqués.

Au lieu de transmettre directement les données à chaque composant enfant, vous les transmettez à travers chaque composant intermédiaire dans la hiérarchie jusqu'à ce qu'elles atteignent le composant enfant souhaité. Cette transmission de props à travers plusieurs niveaux de composants est ce que le prop drilling implique.

Illustrons cela avec un exemple :

```jsx
// ParentComponent.js
import React from 'react';
import ChildComponent from './ChildComponent';

function ParentComponent() {
  const data = 'Hello from Parent';

  return (
    <div>
      <ChildComponent data={data} />
    </div>
  );
}

export default ParentComponent;

```

```jsx
// ChildComponent.js
import React from 'react';
import GrandchildComponent from './GrandchildComponent';

function ChildComponent(props) {
  return (
    <div>
      <GrandchildComponent data={props.data} />
    </div>
  );
}

export default ChildComponent;

```

```jsx
// GrandchildComponent.js
import React from 'react';

function GrandchildComponent(props) {
  return <div>{props.data}</div>;
}

export default GrandchildComponent;

```

Dans cet exemple, `GrandchildComponent` doit accéder à la prop `data`, mais `ParentComponent` et `ChildComponent` ne l'utilisent pas. Cependant, la prop `data` doit toujours être transmise à travers eux.

## Défis du Prop Drilling

### Complexité et code boilerplate

Le prop drilling peut entraîner une complexité accrue et du code boilerplate, surtout dans les grands arbres de composants. À mesure que les composants deviennent plus imbriqués, la gestion du flux de props devient plus difficile et peut encombrer la base de code.

```jsx
// Exemple de Prop Drilling
const ParentComponent = () => {
    const data = fetchData(); // Supposons que nous récupérons des données depuis une API
    return (
        <ChildComponentA data={data} />
    );
};

const ChildComponentA = ({ data }) => {
    return (
        <ChildComponentB data={data} />
    );
};

const ChildComponentB = ({ data }) => {
    return (
        <ChildComponentC data={data} />
    );
};

// Cela continue...

```

### Couplage des composants

Le prop drilling peut fortement coupler les composants ensemble, rendant plus difficile la refactorisation ou la restructuration de la hiérarchie des composants sans affecter d'autres parties de l'application. Cela peut entraîner une maintenabilité et une flexibilité réduites.

### Surcoût de performance

Transmettre des props à travers plusieurs niveaux de composants peut introduire un surcoût de performance, surtout si les props contiennent de grandes quantités de données.

Chaque composant intermédiaire dans la hiérarchie doit se re-rendre lorsque les props changent, ce qui peut potentiellement entraîner des re-rendus inutiles et impacter les performances.

## Comment surmonter le Prop Drilling

Il existe plusieurs techniques pour surmonter le prop drilling dans React.js :

* **Context API** : L'API Context de React permet de partager des données à travers l'arbre de composants sans passer explicitement des props à chaque niveau de la hiérarchie. Le contexte fournit un moyen de transmettre des données à travers l'arbre de composants sans avoir à passer manuellement des props à chaque niveau.
* **Bibliothèques de gestion d'état** : L'utilisation de bibliothèques de gestion d'état comme Redux ou MobX peut aider à centraliser et gérer l'état de l'application, réduisant ainsi le besoin de prop drilling.
* **Higher-Order Components (HOCs)** : Les HOCs sont des fonctions qui acceptent un composant en entrée et retournent un nouveau composant avec des props ou fonctionnalités supplémentaires. Ils peuvent être utilisés pour injecter des props sans les transmettre directement à travers chaque composant intermédiaire.
* **Render Props** : Les render props sont une technique pour partager du code entre les composants React en utilisant une prop dont la valeur est une fonction. Cela permet aux composants de partager du code sans recourir au prop drilling.

Refactorisons l'exemple précédent en utilisant l'API Context :

```jsx
// MyContext.js
import React from 'react';

const MyContext = React.createContext();

export default MyContext;

```

```jsx
// ParentComponent.js
import React from 'react';
import ChildComponent from './ChildComponent';
import MyContext from './MyContext';

function ParentComponent() {
  const data = 'Hello from Parent';

  return (
    <MyContext.Provider value={data}>
      <ChildComponent />
    </MyContext.Provider>
  );
}

export default ParentComponent;

```

```jsx
// ChildComponent.js
import React from 'react';
import GrandchildComponent from './GrandchildComponent';
import MyContext from './MyContext';

function ChildComponent() {
  return (
    <MyContext.Consumer>
      {data => <GrandchildComponent data={data} />}
    </MyContext.Consumer>
  );
}

export default ChildComponent;

```

```jsx
// GrandchildComponent.js
import React from 'react';
import MyContext from './MyContext';

function GrandchildComponent() {
  return (
    <MyContext.Consumer>
      {data => <div>{data}</div>}
    </MyContext.Consumer>
  );
}

export default GrandchildComponent;

```

Dans cet exemple refactorisé, nous avons utilisé l'API Context pour fournir et consommer la prop `data` sans avoir à la transmettre manuellement à travers chaque composant.

## Conclusion

Le prop drilling peut sembler un raccourci pratique au début, mais ses conséquences peuvent entraver la maintenabilité de votre code.

En utilisant des techniques comme l'API Context, les bibliothèques de gestion d'état, ou la puissance des render props, vous vous donnerez les moyens de construire des applications React propres, maintenables et évolutives.

Bon codage !

Connectez-vous avec moi sur [LinkedIn](https://linkedin.com/in/joanayebola).