---
title: Comment utiliser le modèle de conception Adapter dans React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-10-21T00:33:49.000Z'
originalURL: https://freecodecamp.org/news/adapter-design-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/Title-ALD.png
tags:
- name: design patterns
  slug: design-patterns
- name: React
  slug: react
seo_title: Comment utiliser le modèle de conception Adapter dans React
seo_desc: 'By Kenneth Angelo Reyes

  When you''re coding in React or any other tool, you might want or need to use a
  third-party library. Let''s talk about an approach which will ensure that the third-party
  libraries you use will blend well with your application.

  A...'
---

Par Kenneth Angelo Reyes

Lorsque vous codez dans React ou tout autre outil, vous pouvez vouloir ou avoir besoin d'utiliser une bibliothèque tierce. Parlons d'une approche qui garantira que les bibliothèques tierces que vous utilisez s'intégreront bien à votre application.

En tant que développeurs d'applications, il n'est pas nécessaire de réinventer la roue à chaque fois que nous commençons un nouveau projet. Dans la plupart des cas, nous utiliserons une bibliothèque tierce qui offre une version stable de la fonctionnalité que nous recherchons.

## **Traiter les bibliothèques comme des plugins**

Dans le développement logiciel, lorsque vous utilisez une bibliothèque tierce, vous devez prendre en compte les points suivants :

* **L'application doit être agnostique en matière de bibliothèque.** À l'avenir, vous pourriez décider d'utiliser une bibliothèque différente. Cela ne devrait rien casser.
* **Assurer la cohérence du modèle de données.** Le modèle de données de l'application n'est probablement pas compatible avec le modèle de données de la bibliothèque. Dans ce cas, une transformation des données est nécessaire.
* **Assurer une dépendance minimale.** L'application n'a peut-être pas besoin d'utiliser toutes les fonctionnalités offertes par la bibliothèque. Vous ne devez consommer que les fonctionnalités dont vous avez besoin.

Essentiellement, tout cela indique que vous ne devez pas trop dépendre de la bibliothèque. Vous devez traiter les bibliothèques comme des plugins qui peuvent être facilement attachés ou détachés selon les besoins. Parlons de la manière dont vous pouvez faire cela.

## **Le modèle Adapter dans React**

Une façon de s'assurer que vous abordez tous les points mentionnés ci-dessus est d'utiliser le modèle adapter.

> Le modèle adapter convertit l'interface d'une classe en une autre interface que les clients attendent. L'adapter permet à des classes de travailler ensemble qui ne pourraient pas le faire autrement en raison d'interfaces incompatibles. ([Source](https://www.geeksforgeeks.org/adapter-pattern/))

Pour appliquer cela dans React, nous devons introduire un wrapper autour d'une bibliothèque tierce. Ce wrapper servira d'adapter, garantissant que l'application dispose toujours d'une référence stable à la fonctionnalité que nous souhaitons envelopper.

Dans React, il peut y avoir deux types de wrappers :

1. **Wrapper de composant** – pour envelopper les composants de bibliothèque
2. **Wrapper de fonction** – pour envelopper les fonctions de bibliothèque

Dans cet article, nous nous concentrerons davantage sur les wrappers de composants. Examinons un exemple.

## **Un wrapper de composant en action**

Pour notre exemple, nous allons créer un adapter pour [React Flow](https://reactflow.dev/), une bibliothèque de diagrammes tierce.

La bibliothèque React Flow expose de nombreuses fonctionnalités, mais pour notre exemple, nous n'avons besoin de faire que ce qui suit :

1. Rendre les nœuds de diagramme de base
2. Réagir lorsqu'un nœud est sélectionné
3. Réagir lorsqu'il n'y a plus de sélection

Pour ce faire, nous allons d'abord implémenter le `Diagram Adapter` :

```js
import ReactFlow, { isNode } from "react-flow-renderer";

const DiagramAdapter = ({ nodes, onActivateNode, onDeactivateAll }) => {
    const onSelectionChange = (elements) => {
        if (elements) {
            const selectedNodes = elements.filter((els) => isNode(els));

            if (selectedNodes.length > 0) {
                onActivateNode(selectedNodes[0].id);
            }
        }
    };

    const onPaneClick = () => onDeactivateAll();

    return (
        <div style={{ height: 650 }}>
            <ReactFlow
                elements={nodes}
                onSelectionChange={onSelectionChange}
                onPaneClick={onPaneClick} />
        </div>
    );
}

export default DiagramAdapter;

```

Dans le code ci-dessus, nous avons enveloppé le composant `ReactFlow` et y avons attaché quelques écouteurs d'événements. Ces écouteurs d'événements transformeront ensuite les données d'événement et appelleront les fonctions `onActivateNode` et `onDeactivateAll` correspondantes transmises par le composant parent de l'adapter.

De cette manière, le composant parent n'a même pas besoin de savoir quelle bibliothèque nous utilisons. Il sait simplement que `onActivateNode` et `onDeactivateAll` sont disponibles pour une utilisation.

Pour votre référence, nous pouvons utiliser l'adapter comme ceci :

```js
function App() {
  const nodes = [
    {
      id: "node_0",
      position: { x: 150, y: 25 },
      data: { label: "Start" }
    },
    {
      id: "node_1",
      position: { x: 150, y: 225 },
      data: { label: "End" }
    },
    {
      id: "node_0-node_1", type: "step", source: "node_0", target: "node_1"
    }
  ];

  const onActivateNode = (node) => {
    console.log("Activated", node);
  };

  const onDeactivateAll = (node) => {
    console.log("Deactivated all");
  };

  return (
    <DiagramAdapter 
        nodes={nodes}
        onActivateNode={onActivateNode}
        onDeactivateAll={onDeactivateAll} />
  );
}

```

### Un exemple plus réaliste

Pour un exemple plus réaliste, vous pouvez consulter l'un de mes projets d'apprentissage [ici](https://github.com/projectkenneth/react-low-code-app-builder/). Il s'agit d'un simple constructeur d'applications low-code créé en utilisant React et ReactFlow.

Le code de l'adapter peut être trouvé à `/src/Editor/DiagramAdapter.js`. Le composant parent peut être trouvé à `src/Editor/Canvas.js`.

## **Conclusion**

Félicitations ! Nous avons réussi à utiliser le modèle de conception adapter sur une application React.

Nous pouvons maintenant profiter des avantages de découpler notre application des bibliothèques tierces :

* Une application agnostique en matière de bibliothèque
* Cohérence du modèle de données
* Dépendance minimale

J'espère que vous avez appris quelque chose de nouveau aujourd'hui ! Si vous avez d'autres façons d'appliquer le modèle de conception adapter ou tout autre modèle de conception similaire sur une application React, faites-le moi savoir. J'ai hâte d'avoir de vos nouvelles.