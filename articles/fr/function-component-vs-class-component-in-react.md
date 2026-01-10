---
title: Composants Fonction vs Composants Classe dans React – Avec Exemples
subtitle: ''
author: Joan Ayebola
co_authors: []
series: null
date: '2024-04-16T22:37:11.000Z'
originalURL: https://freecodecamp.org/news/function-component-vs-class-component-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/Ivory-and-Blue-Lavender-Aesthetic-Photo-Collage-Presentation--5-.png
tags:
- name: components
  slug: components
- name: React
  slug: react
seo_title: Composants Fonction vs Composants Classe dans React – Avec Exemples
seo_desc: 'In React, there are two primary ways to create components: function and
  class components. Each has its own syntax and use cases, although with the introduction
  of React Hooks, the gap between them has narrowed significantly. But the selection
  of appr...'
---

Dans React, il existe deux façons principales de créer des composants : les composants fonction et les composants classe. Chacun a sa propre syntaxe et ses cas d'utilisation, bien que l'introduction des Hooks React ait considérablement réduit l'écart entre eux. Mais le choix des types de composants appropriés reste très crucial pour construire des applications React efficaces et maintenables.

Dans cet article, nous explorerons les différences fondamentales entre les composants fonction et les composants classe, en fournissant une compréhension claire de leurs forces et de leurs cas d'utilisation idéaux.

En comprenant ces concepts, les développeurs peuvent prendre des décisions éclairées lors de la construction de composants React, améliorant ainsi la structure et la fonctionnalité de leurs applications web.

## Qu'est-ce que les Composants React ?

Dans React, les composants sont les éléments de base d'une interface utilisateur. Ce sont des morceaux de code réutilisables et autonomes qui représentent une partie de l'interface utilisateur. React vous permet de décomposer votre interface utilisateur en composants plus petits, ce qui facilite la gestion et la maintenance de votre base de code.

Vous pouvez considérer les composants comme des éléments HTML personnalisés qui encapsulent leur propre logique et structure d'interface utilisateur. Ils peuvent accepter des entrées appelées props (abréviation de propriétés) et retourner des éléments React décrivant ce qui doit apparaître à l'écran.

Il existe deux principaux types de composants dans React :

**Composants Fonction :** Ce sont des fonctions JavaScript simples qui prennent des props en entrée et retournent des éléments JSX. Ils sont souvent utilisés pour des composants de présentation ou sans état.

**Composants Classe :** Ce sont des classes ES6 qui étendent `React.Component` ou `React.PureComponent`. Ils ont une méthode `render()` où vous définissez la structure de l'interface utilisateur de votre composant en utilisant JSX. Les composants classe sont utilisés pour les composants qui doivent gérer l'état ou avoir des méthodes de cycle de vie.

Avec l'introduction des Hooks React, les composants fonction ont acquis la capacité de gérer l'état et d'utiliser des méthodes de cycle de vie, brouillant la distinction entre les composants fonction et les composants classe. Cependant, les deux types de composants sont encore largement utilisés dans les applications React.

## Composants Fonction vs Composants Classe : Aperçu de Haut Niveau

### Composants Fonction

**Syntax :** Les composants fonction sont définis en utilisant le mot-clé `function` ou la syntaxe des fonctions fléchées.

```jsx
import React from 'react';

// Composant fonction utilisant le mot-clé function
function FunctionComponent(props) {
  return (
    <div>
      <h1>Bonjour, {props.name} !</h1>
      <p>Ceci est un composant fonction.</p>
    </div>
  );
}

// Composant fonction utilisant la syntaxe des fonctions fléchées
const FunctionComponent = (props) => {
  return (
    <div>
      <h1>Bonjour, {props.name} !</h1>
      <p>Ceci est un composant fonction.</p>
    </div>
  );
};

export default FunctionComponent;

```

Dans l'extrait de code ci-dessus, les deux exemples définissent un composant fonction appelé `FunctionComponent` qui prend `props` en entrée et retourne des éléments JSX. Le composant affiche simplement un message de salutation ainsi qu'un texte.

Le premier exemple utilise le mot-clé `function` pour définir le composant fonction, tandis que le second exemple utilise la syntaxe des fonctions fléchées. Les deux syntaxes sont valides et atteignent le même résultat.

**Gestion de l'État :** Traditionnellement, les composants fonction étaient sans état et ne pouvaient pas conserver leur propre état. Cependant, avec l'introduction des Hooks React (comme `useState`), les composants fonction peuvent maintenant gérer l'état en utilisant les Hooks.

```jsx
import React, { useState } from 'react';

const FunctionComponent = () => {
  // Utilisation du Hook useState pour gérer l'état
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Compte : {count}</p>
      <button onClick={() => setCount(count + 1)}>Incrémenter</button>
    </div>
  );
};

export default FunctionComponent;

```

Dans cet exemple, nous utilisons le Hook `useState` pour initialiser une variable d'état `count` avec une valeur initiale de `0`. Le Hook `useState` retourne un tableau avec deux éléments : la valeur actuelle de l'état (`count`) et une fonction (`setCount`) pour mettre à jour l'état.

Lorsque le bouton est cliqué, `setCount` est appelé avec la nouvelle valeur de `count`, déclenchant un nouveau rendu avec la valeur d'état mise à jour affichée. Cela démontre comment les composants fonction peuvent maintenant conserver et gérer leur propre état en utilisant les Hooks React, les rendant plus puissants et polyvalents.

**Méthodes de Cycle de Vie :** Les composants fonction n'ont pas de méthodes de cycle de vie. Cependant, avec les Hooks React, vous pouvez utiliser le Hook `useEffect` pour répliquer le comportement du cycle de vie (comme `componentDidMount`, `componentDidUpdate`, `componentWillUnmount`, etc.).

Discutons de certaines des méthodes de cycle de vie les plus couramment utilisées :

**componentDidMount :** Cette méthode est invoquée immédiatement après qu'un composant est monté (c'est-à-dire inséré dans l'arbre DOM). Elle est couramment utilisée pour effectuer une configuration initiale, telle que la récupération de données depuis une API ou la configuration d'écouteurs d'événements.

**componentDidUpdate :** Cette méthode est invoquée immédiatement après qu'une mise à jour se produit. Elle est déclenchée chaque fois que les props ou l'état du composant changent. Elle est couramment utilisée pour effectuer des actions basées sur l'état ou les props mis à jour, telles que des appels API supplémentaires.

**componentWillUnmount :** Cette méthode est invoquée immédiatement avant qu'un composant soit démonté et détruit. Elle est couramment utilisée pour effectuer un nettoyage, tel que la suppression d'écouteurs d'événements ou l'annulation de toute tâche en cours.

```jsx
import React, { useState, useEffect } from 'react';

const FunctionComponent = () => {
  const [count, setCount] = useState(0);

  // Hook useEffect pour répliquer componentDidMount et componentDidUpdate
  useEffect(() => {
    // Ce bloc de code s'exécute après chaque rendu
    console.log("Le composant a été monté ou mis à jour");

    // Fonction de nettoyage (répliquant componentWillUnmount)
    return () => {
      console.log("Le composant va être démonté");
    };
  });

  return (
    <div>
      <p>Compte : {count}</p>
      <button onClick={() => setCount(count + 1)}>Incrémenter</button>
    </div>
  );
};

export default FunctionComponent;

```

Dans cet exemple, le Hook `useEffect` est utilisé sans tableau de dépendances. Cela signifie que l'effet s'exécutera après chaque rendu, répliquant efficacement à la fois le comportement de `componentDidMount` et `componentDidUpdate`. À l'intérieur de l'effet, vous pouvez effectuer tout nettoyage nécessaire, tel que la désinscription des abonnements ou la suppression des écouteurs d'événements, en retournant une fonction de nettoyage. Cette fonction de nettoyage sera exécutée lorsque le composant sera démonté, répliquant efficacement le comportement de `componentWillUnmount`.

En exploitant le Hook `useEffect`, les composants fonction peuvent maintenant atteindre le même comportement de cycle de vie que les composants classe, brouillant davantage la distinction entre les deux types de composants.

**Lisibilité :** Les composants fonction sont généralement plus concis et plus faciles à lire, surtout pour les composants plus simples.

### Composants Classe

**Syntax :** Les composants classe sont des classes ES6 qui étendent `React.Component` ou `React.PureComponent`. Ils ont une méthode `render()` où vous définissez la structure de l'interface utilisateur de votre composant en utilisant JSX.

```jsx
import React, { Component } from 'react';

// Définir un composant classe qui étend React.Component ou React.PureComponent
class ClassComponent extends Component {
  // Définir le constructeur si nécessaire
  constructor(props) {
    super(props);
    // Initialiser l'état si nécessaire
    this.state = {
      count: 0
    };
  }

  // Définir les méthodes de cycle de vie si nécessaire
  componentDidMount() {
    // Code à exécuter après que le composant est monté
  }

  // Définir les méthodes d'instance si nécessaire
  handleClick = () => {
    // Mettre à jour l'état ou effectuer une autre logique
    this.setState({ count: this.state.count + 1 });
  }

  // Définir la méthode render() pour retourner du JSX
  render() {
    return (
      <div>
        <p>Compte : {this.state.count}</p>
        <button onClick={this.handleClick}>Incrémenter</button>
      </div>
    );
  }
}

export default ClassComponent;

```

Dans cet exemple :

* Nous avons importé `React` et `Component` depuis le package 'react'.
* Nous avons défini un composant classe nommé `ClassComponent` qui étend `Component`.
* À l'intérieur du composant classe, nous pouvons définir un constructeur pour initialiser l'état ou lier les gestionnaires d'événements si nécessaire.
* Nous pouvons définir des méthodes de cycle de vie telles que `componentDidMount`, `componentDidUpdate`, etc., pour nous connecter à différentes étapes du cycle de vie du composant.
* Nous avons défini la méthode `render()`, qui retourne du JSX pour décrire la structure de l'interface utilisateur du composant.
* Toute méthode d'instance, gestionnaire d'événements ou autre logique peut être définie dans la classe.

**Gestion de l'État :** Les composants classe peuvent conserver et gérer l'état local en utilisant la propriété `this.state`. Ils peuvent également mettre à jour l'état en utilisant `this.setState()`.

Illustrons cela avec un exemple simple :

```jsx
import React, { Component } from 'react';

class ClassComponent extends Component {
  constructor(props) {
    super(props);
    // Initialiser l'état
    this.state = {
      count: 0
    };
  }

  // Définir une méthode pour mettre à jour l'état
  incrementCount = () => {
    // Utiliser this.setState() pour mettre à jour l'état
    this.setState({ count: this.state.count + 1 });
  }

  render() {
    return (
      <div>
        <p>Compte : {this.state.count}</p>
        <button onClick={this.incrementCount}>Incrémenter</button>
      </div>
    );
  }
}

export default ClassComponent;

```

Dans cet exemple :

* Nous avons initialisé l'état du composant dans le constructeur en utilisant `this.state`.
* La méthode `incrementCount` a été définie dans la classe pour mettre à jour l'état `count`. À l'intérieur de cette méthode, nous avons appelé `this.setState()` et passé un objet contenant le nouvel état ou une fonction qui retourne le nouvel état. React fusionnera le nouvel état avec l'état existant.
* Dans la méthode `render()`, nous avons accédé à l'état `count` en utilisant `this.state.count` et l'avons affiché dans le JSX.
* Lorsque le bouton est cliqué, la méthode `incrementCount` est appelée, ce qui met à jour l'état `count` et déclenche un nouveau rendu du composant.

Cela démontre comment les composants classe dans React peuvent gérer l'état local et le mettre à jour en utilisant `this.setState()`.

**Méthodes de Cycle de Vie :** Les composants classe ont accès à diverses méthodes de cycle de vie comme `componentDidMount`, `componentDidUpdate`, et `componentWillUnmount`, qui vous permettent de vous connecter à différentes étapes du cycle de vie d'un composant.

Voici un exemple démontrant l'utilisation de ces méthodes de cycle de vie dans un composant classe :

```jsx
import React, { Component } from 'react';

class ClassComponent extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: null
    };
  }

  componentDidMount() {
    // Récupérer les données initiales lorsque le composant est monté
    this.fetchData();
  }

  componentDidUpdate(prevProps, prevState) {
    // Vérifier si les données ont changé
    if (prevState.data !== this.state.data) {
      // Les données ont changé, effectuer des actions supplémentaires
      console.log('Les données ont été mises à jour :', this.state.data);
    }
  }

  componentWillUnmount() {
    // Tâches de nettoyage avant que le composant soit démonté
    console.log('Le composant va être démonté');
    // Par exemple, supprimer les écouteurs d'événements, annuler les tâches en cours, etc.
  }

  fetchData() {
    // Simuler la récupération de données depuis une API
    setTimeout(() => {
      this.setState({ data: 'Données récupérées depuis une API' });
    }, 1000);
  }

  render() {
    return (
      <div>
        <p>Données : {this.state.data}</p>
      </div>
    );
  }
}

export default ClassComponent;

```

Dans cet exemple :

* `componentDidMount` est utilisé pour récupérer les données initiales lorsque le composant est monté.
* `componentDidUpdate` est utilisé pour journaliser un message chaque fois que l'état des données change.
* `componentWillUnmount` est utilisé pour journaliser un message avant que le composant soit démonté.

Ces méthodes de cycle de vie fournissent des points d'entrée à différentes étapes du cycle de vie d'un composant, permettant d'effectuer des tâches de configuration, de mise à jour et de nettoyage selon les besoins.

**Méthodes d'Instance :** Vous pouvez définir des méthodes personnalisées directement sur la classe, ce qui peut être utile pour organiser la logique de votre composant.

```jsx
import React, { Component } from 'react';

class ClassComponent extends Component {
  constructor(props) {
    super(props);
    this.state = {
      count: 0
    };
  }

  // Méthode personnalisée pour gérer l'incrémentation du compte
  handleIncrement = () => {
    this.setState({ count: this.state.count + 1 });
  }

  // Méthode personnalisée pour gérer la décrémentation du compte
  handleDecrement = () => {
    this.setState({ count: this.state.count - 1 });
  }

  render() {
    return (
      <div>
        <p>Compte : {this.state.count}</p>
        <button onClick={this.handleIncrement}>Incrémenter</button>
        <button onClick={this.handleDecrement}>Décrémenter</button>
      </div>
    );
  }
}

export default ClassComponent;

```

Dans cet exemple :

* Nous avons défini deux méthodes d'instance personnalisées `handleIncrement` et `handleDecrement` dans le composant classe. Ces méthodes ont été définies en utilisant la syntaxe des fonctions fléchées pour garantir qu'elles ont accès au contexte `this` correct.
* La méthode `handleIncrement` met à jour l'état `count` en l'incrémentant de 1 lorsqu'elle est appelée.
* La méthode `handleDecrement` met à jour l'état `count` en le décrémentant de 1 lorsqu'elle est appelée.
* Ces méthodes personnalisées sont ensuite utilisées comme gestionnaires d'événements pour les boutons dans le JSX retourné par la méthode `render`.

La définition de méthodes d'instance personnalisées dans les composants classe aide à organiser la logique du composant, le rendant plus lisible et maintenable. De plus, ces méthodes peuvent être réutilisées dans différentes parties du composant, améliorant la réutilisabilité du code.

Il est important de noter que, avec l'introduction des Hooks React, de nombreuses tâches traditionnellement gérées par les composants classe peuvent maintenant être accomplies en utilisant des composants fonction.

Les Hooks tels que `useState`, `useEffect`, `useContext`, et autres fournissent une manière plus simple et plus concise de gérer l'état, de gérer les effets secondaires et de partager la logique entre les composants. Ce changement vers les Hooks permet aux développeurs d'écrire un code plus fonctionnel et modulaire, réduisant la dépendance aux composants classe.

Bien que les composants classe aient encore leur place, surtout dans les bases de code héritées, la polyvalence et la flexibilité des Hooks font des composants fonction le choix préféré pour construire des applications React modernes.

## Avantages des Composants Fonction

**Syntaxe Plus Simple :** Les composants fonction ont une syntaxe plus simple par rapport aux composants classe. Ils sont essentiellement des fonctions JavaScript qui prennent des props en entrée et retournent des éléments React. Cette simplicité les rend plus faciles à lire et à comprendre, surtout pour les débutants.

**Fonctions Pures :** Les composants fonction sont essentiellement des fonctions pures, ce qui signifie qu'ils dépendent uniquement de leur entrée (props) pour produire une sortie (UI). Ils n'ont pas d'état interne ni d'effets secondaires, ce qui les rend plus faciles à raisonner et à tester. Cette pureté aide également à améliorer les performances, car React peut optimiser le processus de rendu plus efficacement.

**Réutilisabilité :** Les composants fonction favorisent la réutilisabilité en encapsulant la logique de l'interface utilisateur dans de petites fonctions composables. Puisqu'ils sont simplement des fonctions JavaScript, ils peuvent être facilement réutilisés dans plusieurs parties de votre application, conduisant à un code plus modulaire et maintenable.

**Utilisation des Props dans les Composants Fonction :** Les composants fonction utilisent largement les props pour passer des données des composants parents aux composants enfants. Cette approche basée sur les props favorise un flux de données clair et prévisible dans votre application, rendant plus facile la compréhension de la manière dont les données sont passées et utilisées dans votre hiérarchie de composants.

## Avantages des Composants Classe

**Gestion Explicite de l'État :** Les composants classe fournissent une manière claire et explicite de gérer l'état du composant en utilisant la propriété `this.state`. Cela permet aux développeurs d'avoir un contrôle fin sur la gestion et les mises à jour de l'état dans le composant.

**Méthodes de Cycle de Vie :** Les composants classe ont accès à une gamme de méthodes de cycle de vie telles que `componentDidMount`, `componentDidUpdate`, et `componentWillUnmount`. Ces méthodes permettent aux développeurs de se connecter à différentes étapes du cycle de vie du composant, permettant des tâches comme la récupération de données, les abonnements aux événements, et les opérations de nettoyage.

**Méthodes d'Instance :** Les composants classe vous permettent de définir des méthodes d'instance personnalisées directement dans la classe. Ces méthodes encapsulent la logique du composant et peuvent être réutilisées dans tout le composant. Cela aide à organiser et structurer la base de code du composant.

**Support de l'Héritage :** Les composants classe font partie intégrante de React depuis ses débuts et sont encore largement utilisés dans de nombreuses bases de code. Ils fournissent une compatibilité ascendante et un support pour les projets hérités qui n'ont peut-être pas été mis à jour pour utiliser les composants fonction avec les Hooks.

**Robustesse :** Les composants classe imposent une structure plus stricte et une séparation des préoccupations, ce qui peut conduire à des bases de code plus robustes et maintenables, surtout dans les applications plus grandes avec une logique d'interface utilisateur complexe.

**Optimisation des Performances :** Les composants classe offrent des opportunités d'optimisation grâce à l'utilisation de `PureComponent` ou à l'implémentation manuelle de shouldComponentUpdate (une méthode de cycle de vie dans React). Ces optimisations peuvent aider à prévenir les rendus inutiles et améliorer les performances dans certains scénarios.

## Comment Gérer l'État Complexe et les Effets Secondaires (Avant les Hooks)

Avant l'introduction des Hooks React, les composants classe étaient le moyen principal de gérer l'état complexe et les effets secondaires dans les applications React. Voici comment les composants classe facilitaient cela :

**Gestion de l'État :** Les composants classe fournissaient un mécanisme intégré pour gérer l'état du composant en utilisant la propriété `this.state`. Les développeurs pouvaient initialiser l'état dans le constructeur et le mettre à jour en utilisant la méthode `this.setState()`. Cela permettait la gestion de structures d'état complexes et la synchronisation de l'état avec l'interface utilisateur.

**Méthodes de Cycle de Vie :** Les composants classe offraient une gamme de méthodes de cycle de vie qui permettaient aux développeurs de se connecter à différentes étapes du cycle de vie d'un composant. Ces méthodes de cycle de vie, telles que `componentDidMount`, `componentDidUpdate`, et `componentWillUnmount`, fournissaient des opportunités pour effectuer des tâches comme la récupération de données, la manipulation du DOM, ou les opérations de nettoyage.

**Méthodes d'Instance :** Les composants classe permettaient aux développeurs de définir des méthodes d'instance personnalisées directement dans la classe. Ces méthodes encapsulaient la logique du composant et permettaient une meilleure organisation et structure de la base de code du composant. Les méthodes d'instance pouvaient gérer une logique complexe, la gestion des événements, ou l'interaction avec des API externes.

**Composants d'Ordre Supérieur (HOC) et Render Props :** Avant l'adoption généralisée des Hooks, les développeurs utilisaient souvent des Composants d'Ordre Supérieur (HOC) ou des Render Props pour encapsuler et partager une logique complexe entre les composants. Les modèles HOC et Render Props facilitaient la réutilisation de la logique dans plusieurs composants, rendant plus facile la gestion de l'état complexe et des effets secondaires.

Dans l'ensemble, les composants classe fournissaient une approche structurée et basée sur les classes pour gérer l'état complexe et les effets secondaires dans les applications React. Bien que les Hooks aient depuis émergé comme une alternative plus légère et fonctionnelle, les composants classe continuent d'être utilisés dans de nombreuses bases de code, surtout dans les projets hérités ou les situations où des méthodes de cycle de vie ou des modèles spécifiques sont requis.

## Quand Utiliser Chaque Type de Composant

Discutons de quand utiliser les composants fonction et les composants classe dans React, ainsi que de quand les limites d'erreur peuvent nécessiter l'utilisation de composants classe :

### Quand Choisir les Composants Fonction

**Simplicité et Lisibilité :** Utilisez les composants fonction pour des éléments d'interface utilisateur plus simples ou des composants qui n'ont pas besoin d'état ou de méthodes de cycle de vie. Ils ont une syntaxe plus simple et sont plus faciles à lire et à comprendre, ce qui les rend idéaux pour les composants de présentation.

**Réutilisabilité et Composition :** Les composants fonction favorisent la réutilisabilité et la composition en vous permettant de créer de petites fonctions composables qui peuvent être facilement réutilisées dans votre application. Ils sont bien adaptés pour construire des composants d'interface utilisateur réutilisables.

**Performance :** Les composants fonction avec les Hooks React offrent une approche plus optimisée pour la gestion de l'état et les effets secondaires, pouvant conduire à de meilleures performances par rapport aux composants classe. Ils évitent le surcoût de l'instanciation de classe et fournissent une alternative plus légère.

### Quand Choisir les Composants Classe (Limites d'Erreur)

**Méthodes de Cycle de Vie :** Utilisez les composants classe lorsque vous avez besoin d'accéder à des méthodes de cycle de vie telles que `componentDidCatch`. Les composants classe fournissent un moyen d'implémenter des limites d'erreur, qui sont des composants qui attrapent les erreurs JavaScript n'importe où dans leur arbre de composants enfants et affichent une interface utilisateur de repli au lieu de faire planter toute l'application.

**Gestion de l'État Complexe et des Effets Secondaires (Avant les Hooks) :** Dans les bases de code héritées ou les situations où des méthodes de cycle de vie ou des optimisations spécifiques sont requises, les composants classe peuvent encore être le choix préféré. Ils offrent une approche plus structurée pour gérer l'état complexe, les effets secondaires et le comportement du cycle de vie.

**Compatibilité Ascendante :** Les composants classe sont encore largement utilisés dans de nombreuses bases de code React existantes et bibliothèques. Si vous travaillez sur un projet qui repose fortement sur les composants classe ou si vous devez vous intégrer avec des bibliothèques qui n'ont pas migré vers les composants fonction avec les Hooks, vous devrez peut-être utiliser les composants classe pour des raisons de compatibilité.

En résumé, les composants fonction avec les Hooks sont généralement préférés pour la plupart des cas d'utilisation en raison de leur simplicité, de leur réutilisabilité et de leurs avantages en termes de performance. Cependant, les composants classe sont encore pertinents, surtout lorsque des méthodes de cycle de vie ou des limites d'erreur spécifiques sont nécessaires. Il est essentiel de peser le pour et le contre de chaque type de composant et de choisir celui qui convient le mieux aux exigences et contraintes de votre projet.

### React Hooks : Combler l'Écart

Les React Hooks sont une fonctionnalité introduite dans React 16.8 qui permet aux composants fonction d'avoir une logique d'état et d'accéder aux fonctionnalités du cycle de vie de React sans avoir besoin d'écrire un composant classe. Les Hooks sont des fonctions qui vous permettent d'utiliser l'état de React et les fonctionnalités du cycle de vie depuis les composants fonction.

### Utilisation des Hooks pour la Gestion de l'État (useState)

Le Hook `useState` est l'un des Hooks React les plus fondamentaux. Il permet aux composants fonction de gérer l'état sans avoir besoin de définir une classe. Voici un exemple de l'utilisation de `useState` :

```jsx
import React, { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Compte : {count}</p>
      <button onClick={() => setCount(count + 1)}>Incrémenter</button>
    </div>
  );
}

```

Dans cet exemple, `useState` est utilisé pour déclarer une variable d'état `count` et une fonction `setCount` pour la mettre à jour. La valeur initiale de `count` est définie sur `0`. Chaque fois que `setCount` est appelé avec une nouvelle valeur, React réaffichera le composant avec l'état mis à jour.

### Autres Hooks Utiles (useEffect, useContext, etc.)

React fournit plusieurs autres Hooks pour gérer les effets secondaires, le contexte, et plus encore. Voici quelques-uns des plus couramment utilisés :

**`useEffect` :** Ce Hook vous permet d'effectuer des effets secondaires dans les composants fonction. Il remplace les méthodes de cycle de vie comme `componentDidMount`, `componentDidUpdate`, et `componentWillUnmount`. Vous pouvez l'utiliser pour récupérer des données, vous abonner à des événements externes, ou effectuer un nettoyage.

**`useContext` :** Ce Hook vous permet de consommer du contexte dans les composants fonction. Il vous permet d'accéder aux valeurs du `Context.Provider` le plus proche dans l'arbre des composants.

**`useReducer` :** Ce Hook est une alternative à `useState` pour gérer une logique d'état plus complexe. Il est basé sur le modèle du réducteur et est utile pour gérer les transitions d'état de manière prévisible.

**`useCallback` et `useMemo` :** Ces Hooks sont utilisés pour l'optimisation des performances. `useCallback` mémorise les fonctions, empêchant les rendus inutiles, tandis que `useMemo` mémorise les valeurs, empêchant les calculs coûteux à chaque rendu.

Ce ne sont que quelques exemples des nombreux Hooks disponibles dans React. Chaque Hook sert un but spécifique et permet aux composants fonction d'avoir les mêmes capacités que les composants classe, comblant l'écart entre les deux types de composants et permettant une approche plus fonctionnelle et composable pour construire des applications React.

### Conclusion

En résumé, les React Hooks ont eu un grand impact sur la manière dont nous construisons des composants dans React. Les composants fonction sont devenus très populaires car ils sont plus simples et plus flexibles que les composants classe.

Avec les Hooks, nous pouvons facilement gérer l'état, gérer les effets secondaires et contrôler le comportement des composants. Cela a rendu le développement React plus simple et plus efficace.

À l'avenir, les composants fonction avec les Hooks sont susceptibles de devenir la manière standard de construire des applications React. Ils sont plus faciles à utiliser et offrent de meilleures performances, ce qui en fait un favori parmi les développeurs.

Bien que les composants classe aient encore leur place, surtout dans les projets plus anciens, la tendance est à l'utilisation des composants fonction avec les Hooks. Ils fournissent une approche moderne et efficace pour construire des interfaces utilisateur, rendant le développement React plus agréable pour tous les participants.

Connectez-vous avec moi sur [LinkedIn](https://ng.linkedin.com/in/joan-ayebola).