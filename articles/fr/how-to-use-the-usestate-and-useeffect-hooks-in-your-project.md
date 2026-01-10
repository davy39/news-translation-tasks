---
title: React Hooks – Comment utiliser les Hooks useState et useEffect dans votre projet
subtitle: ''
author: Okoro Emmanuel Nzube
co_authors: []
series: null
date: '2024-03-08T15:37:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-the-usestate-and-useeffect-hooks-in-your-project
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/React-JS-Hooks.png
tags:
- name: hooks
  slug: hooks
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: React Hooks – Comment utiliser les Hooks useState et useEffect dans votre
  projet
seo_desc: 'Hooks allow function components to have access to state and other React
  features, such as lifecycle methods. These Hook features were introduced to React
  version 16.8.

  One of the interesting things about the Hook features is that they let you use Rea...'
---

Les Hooks permettent aux composants fonctionnels d'avoir accès à l'état et à d'autres fonctionnalités React, telles que les méthodes de cycle de vie. Ces fonctionnalités de Hooks ont été introduites dans la version 16.8 de React.

L'une des choses intéressantes concernant les fonctionnalités des Hooks est qu'elles vous permettent d'utiliser React sans classes. Cela, à son tour, aide à simplifier votre base de code et vous aide à écrire un code plus propre et plus intuitif.

Dans cet article, vous apprendrez comment utiliser les Hooks courants dans votre projet.

## Avantages des React Hooks

Passons en revue certaines des raisons pour lesquelles vous pourriez vouloir utiliser les Hooks dans votre projet :

* **Facile à utiliser et à comprendre :** Avec les Hooks, vous pouvez écrire un code plus direct. Ces commandes de Hooks ne peuvent être écrites qu'à l'intérieur d'un composant fonctionnel.

* **Code réutilisable :** Les Hooks vous permettent de réutiliser une logique particulière utilisée dans un composant à travers plusieurs autres composants.

* **Meilleures performances d'optimisation :** Les Hooks offrent une approche plus efficace pour utiliser les fonctionnalités React comme l'état et les fonctions de cycle de vie, ce qui améliore les performances par rapport aux composants de classe dans certaines situations.

## Différents types de React Hooks

Les fonctionnalités des React Hooks sont de différents types, allant de `useState`, `useEffect`, `useRef`, `useReducer`, et ainsi de suite.

## Règles des React Hooks

Il existe quelques règles importantes concernant les fonctionnalités des React Hooks qui doivent être strictement suivies. Passons-les en revue dans les sections suivantes.

### Les Hooks doivent être appelés à l'intérieur d'une fonction React

Les Hooks ne doivent pas être utilisés à l'intérieur d'un composant de classe – ils peuvent et doivent être appelés uniquement à l'intérieur de la fonction React.

Cette première règle spécifie essentiellement qu'un composant Hook ne doit pas être trouvé dans un composant de classe, mais dans un composant fonctionnel.

Voici la mauvaise façon d'implémenter la fonctionnalité Hook :

```javascript
import React, { Component } from 'react';
import React, {useState} from react;

class App extends Component {
 const [count, setCount] = useState(0);
 
  render() {
    return (
      <div>
        <h1>Bonjour, je suis un composant de classe !</h1>
      </div>
    );
  }
}

export default App;
```

Et voici la bonne façon d'implémenter la fonctionnalité Hook :

```javascript
import React, { useState } from 'react';

function App() {
  const [userName, setUsername] = useState('');
  
  };

  return ( Votre code JSX va ici.....);
};

export default App;
```

L'exemple de code ci-dessus montre une bonne façon d'utiliser une fonctionnalité Hook.

Si vous utilisez une fonctionnalité Hook dans un composant de classe, comme dans le premier exemple, votre code générera une erreur. Par conséquent, vous ne pouvez implémenter un Hook qu'à l'intérieur d'un composant fonctionnel.

### Les Hooks ne peuvent être appelés qu'au niveau supérieur d'un composant

Vous ne pouvez implémenter/appeler un React Hook qu'au niveau supérieur d'un composant avant tout autre code.

En utilisant le code de la section précédente comme exemple, vous pouvez voir que immédiatement après `function App ()`.

La prochaine chose qui vient est la commande Hook – dans cet exemple, nous avons utilisé le Hook `useState`. C'est de quoi parle la deuxième règle.

### Les Hooks ne peuvent pas être utilisés dans une instruction conditionnelle

Nous avons différents types d'instructions conditionnelles/rendering allant de `if`, `else`, et ainsi de suite.

La règle ci-dessus signifie que les conditionnelles ne peuvent pas être appliquées directement aux Hooks. Cela est dû au fait que les Hooks sont appelés dans le même ordre à chaque rendu d'un composant fonctionnel.

Vous pouvez exécuter des Hooks de manière conditionnelle dans un composant fonctionnel, mais pour que cela fonctionne, cette condition doit être déterminée par la logique de haut niveau et ne doit pas être imbriquée dans d'autres blocs ou composants.

La raison en est que les Hooks doivent être invoqués au niveau le plus élevé du composant, plutôt que sous des conditions, des boucles ou des fonctions imbriquées.

Voici un exemple :

```javascript
import React, { useState, useEffect } from 'react';

function ConditionalEffectComponent() {
  const [isMounted, setIsMounted] = useState(false);

  useEffect(() => {
    if (isMounted) {
      // Effectuer un effet lorsque le composant est monté
      console.log('Composant monté');
    }
  }, [isMounted]); // Le tableau de dépendances garantit que l'effet s'exécute lorsque isMounted change

  return (
    <div>
      <button onClick={() => setIsMounted(!isMounted)}>
        {isMounted ? 'Démonter' : 'Monter'}
      </button>
    </div>
  );
}

export default ConditionalEffectComponent;
```

Dans l'exemple ci-dessus, le Hook `useEffect` est exécuté de manière conditionnelle en fonction de la valeur de la variable d'état `isMounted`.

En cliquant sur le bouton, la valeur de `isMounted` alterne, activant ou désactivant l'effet en fonction de la valeur mise à jour.

Cela est considéré comme approprié car le Hook est invoqué au niveau le plus élevé du composant et sa condition est déterminée par la logique globale au sein du composant.

## Comment utiliser le Hook useState

Le Hook `useState` de React vous permet d'avoir des variables d'état dans les composants fonctionnels.

Pour utiliser le Hook d'état, vous devez d'abord l'importer dans votre projet en utilisant la commande `import`.

La manière dont `useState` fonctionne est qu'il nous donne deux variables. La première variable est connue comme la valeur de l'état, et la deuxième variable est une fonction utilisée pour mettre à jour l'état.

Voici un exemple de comment procéder :

```javascript
import './App.css'
import React, { useState } from 'react';

function App() { 

	const [count, setCount] = useState(0); 

return ( 
	<div>
    	<p>Vous avez cliqué {count} fois</p>
        <button onClick={() => setCount(count + 1)}> Cliquez-moi
        </button>
    </div>
    ); 
}

export default App;
```

Dans l'exemple de code ci-dessus, vous pouvez voir que le Hook d'état a été utilisé dans un composant fonctionnel et non dans un composant de classe.

`count` et `setCount` sont les deux variables du Hook d'état, où `count` est la valeur actuelle de l'état et `setCount` est utilisé pour mettre à jour la valeur de l'état. Par conséquent, chaque fois que le bouton est cliqué, `setCount` mettra à jour la valeur du compteur.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/R1.gif align="left")

*Comment fonctionne le Hook useState*

## Comment utiliser le Hook useEffect

Le Hook `useEffect` dans React est comme un outil pratique pour les composants fonctionnels. Il aide à gérer les tâches qui ne sont pas directement liées à l'affichage, comme la récupération de données depuis Internet, la récupération de données depuis des points de terminaison d'API, ou la configuration de minuteries. Il peut être utilisé pour mettre à jour des composants même après qu'ils ont été affichés, rendant votre application plus dynamique.

Voici un exemple de base de l'utilisation de `useEffect` pour récupérer des données depuis un point de terminaison d'API :

```javascript
import React, { useState, useEffect } from 'react';

function MyComponent() {
  const [data, setData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('https://api.example.com/data');
        const jsonData = await response.json();
        setData(jsonData);
      } catch (error) {
        console.error('Erreur lors de la récupération des données :', error);
      }
    };

    fetchData(); // Appeler la fonction fetchData lorsque le composant est monté ou mis à jour

    // Fonction de nettoyage (optionnelle) pour gérer les désabonnements ou le nettoyage des ressources
    return () => {
      // Logique de nettoyage ici, si nécessaire
    };
  }, []); // Un tableau de dépendances vide signifie que l'effet ne s'exécute qu'une fois après le rendu initial

  return (
    <div>
      {/* Afficher les données récupérées */}
      {data && (
        <ul>
          {data.map(item => (
            <li key={item.id}>{item.name}</li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default MyComponent;
```

Dans l'exemple de code ci-dessus, `MyComponent` est un composant fonctionnel qui utilise les Hooks React, spécifiquement `useState` et `useEffect`, pour gérer l'état et exécuter des effets secondaires. Le Hook `useState` est utilisé pour initialiser une variable d'état appelée `data`. Cette variable stockera les données récupérées depuis un point de terminaison d'API.

Le Hook `useEffect` est utilisé pour demander des données depuis le point de terminaison d'API une fois que le composant est initialement rendu. Dans le `useEffect`, une fonction asynchrone `fetchData` est définie pour récupérer les données JSON depuis le point de terminaison d'API spécifié en utilisant l'API fetch.

Si la récupération des données est réussie, les données JSON retournées sont enregistrées dans la variable d'état `data` en utilisant la fonction `setData` fournie par le Hook `useState`.

Le Hook `useEffect` retourne également une fonction de nettoyage optionnelle, qui est actuellement vide mais peut être utilisée pour toute logique de nettoyage nécessaire.

Dans le JSX du composant, les données récupérées sont rendues de manière conditionnelle. Si les données ne sont pas nulles, une liste `<ul>` est produite en utilisant les éléments extraits du tableau de données avec map.

Enfin, la fonction `MyComponent` est exportée comme exportation par défaut du module, permettant son importation et son utilisation dans d'autres sections.

## Conclusion

En tant que développeur, les React Hooks sont un outil très utile et puissant pour les composants fonctionnels qui facilitent votre travail.

Je crois qu'à ce stade, vous savez maintenant ce qu'est un React Hook et comment utiliser les plus populaires.

Merci d'avoir lu, et bon codage !