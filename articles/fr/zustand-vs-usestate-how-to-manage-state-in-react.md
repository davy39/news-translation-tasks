---
title: Zustand vs useState – Comment gérer l'état dans les applications React
subtitle: ''
author: Ijeoma Igboagu
co_authors: []
series: null
date: '2024-05-15T09:28:40.000Z'
originalURL: https://freecodecamp.org/news/zustand-vs-usestate-how-to-manage-state-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/Add-a-heading--1-.png
tags:
- name: React
  slug: react
- name: React
  slug: reactjs
seo_title: Zustand vs useState – Comment gérer l'état dans les applications React
seo_desc: 'State management in React applications has evolved a lot in recent years,
  especially with the advancement of functional state and the introduction of hooks.

  Developers have more flexibility and state management has generally become simpler.
  But as ap...'
---

La gestion d'état dans les applications React a beaucoup évolué ces dernières années, notamment avec l'avancement de l'état fonctionnel et l'introduction des hooks.

Les développeurs ont plus de flexibilité et la gestion d'état est généralement devenue plus simple. Mais à mesure que les applications grandissent, elles deviennent plus complexes à gérer – et vous pourriez avoir besoin d'une solution de gestion d'état plus robuste.

Les hooks React fournissent des solutions intégrées pour gérer l'état de vos applications – par exemple, avec le hook `useState()`. Mais il existe d'autres bibliothèques comme [MobX](https://mobx.js.org/README.html), [Zustand](https://www.npmjs.com/package/zustand) et [Recoil](https://recoiljs.org/) qui peuvent aider à simplifier la gestion d'état.

Dans cet article, je me concentrerai sur `Zustand` et le comparerai avec le hook `useState()`. Vous pouvez consulter une comparaison de [useState() et Redux ici](https://www.freecodecamp.org/news/usestate-vs-redux-state-management/) si vous souhaitez en savoir plus sur Redux et comment il se compare à `useState()`.

Pour commencer, je veux m'assurer que vous comprenez comment fonctionnent `useState()` et `Zustand`. Ensuite, nous les comparerons pour voir quelle est la meilleure solution pour votre projet.

## Prérequis

Avant de commencer à coder, assurez-vous d'avoir les éléments suivants :

* [Node.js](https://nodejs.org/en) installé sur votre système.

* Une compréhension de base de [React.js](https://react.dev/).

* Un éditeur de code que vous préférez, comme [Visual Studio Code](https://code.visualstudio.com/) ou [Sublime Text](https://www.sublimetext.com/download).

## Comment utiliser `useState()` pour la gestion d'état

### Présentation du hook useState

`useState()` est un hook React intégré qui permet aux composants fonctionnels de gérer l'état sans utiliser de composants de classe. Il fournit un moyen simple de déclarer des variables d'état et de les mettre à jour dans les composants fonctionnels.

Pour plus d'informations sur le hook `useState()`, [vous pouvez consulter ce tutoriel](https://www.freecodecamp.org/news/usestate-hook-3-different-examples/). Il vous fournira des informations détaillées et des exemples liés à `useState()` dans React.

### Utilisation de base et syntaxe

La syntaxe de `useState()` est simple. Elle prend un état initial comme argument et retourne un tableau avec la valeur actuelle de l'état et une fonction pour mettre à jour cette valeur.

```javascript
const [text, setText] = useState();
```

Regardons un exemple de l'utilisation de `useState()`.

État initial de l'application :

```javascript


const Usestate = () => {


  return (
    <div className='container'>
      <h1>
       Gestion d'état avec useState()
      </h1>
      <br />
      <div className='input'>
        <input
          type='text'
          className='input'
        />
        <button>
          Changer la couleur
        </button>
      </div>
    </div>
  );
}

export default Usestate;
```

Dans le code ci-dessus, nous avons un composant React nommé `Usestate`. Il rend une interface simple avec un titre "Gestion d'état avec useState()", un champ de saisie de texte et un bouton étiqueté "Changer la couleur".

Voici le résultat de ce code :

![Un exemple montrant l'état initial de l'application](https://www.freecodecamp.org/news/content/images/2024/05/useState---zustand.png align="left")

*État initial de l'application*

Maintenant, ajoutons `useState()` et le rendons fonctionnel. Voici le code :

```javascript
import { useState } from "react";

const Usestate = () => {
  const [text, setText] = useState('black');
  const [color, setColor] = useState('black'); // Un autre état pour stocker la couleur choisie par l'utilisateur

  const handleInputChange = (e) => {
    setText(e.target.value);
  };

  // Une fonction a été déclarée
  const handleButtonClick = () => {
    setColor(text); // elle met à jour la couleur choisie lorsque le bouton est cliqué
  };

  return (
    <div className='container'>
      <h1 style={{color:color}}>
        Gestion d'état avec useState()
      </h1>
      <br />
      <div className='input'>
        <input
          type='text'
          className='input'
          value={text}
          onChange={handleInputChange}
        />
        <button className='btn' onClick={handleButtonClick}>
          Changer la couleur
        </button>
      </div>
    </div>
  );
}

export default Usestate;
```

Dans le code ci-dessus, la variable d'état `text` est définie sur l'état initial (couleur) en utilisant `useState()`. La fonction `setText` est définie pour mettre à jour la valeur de la couleur lorsque le bouton est cliqué.

Le deuxième état défini stocke la mise à jour de la couleur par l'utilisateur. Ainsi, la couleur du `text` reste inchangée jusqu'à ce que le bouton soit cliqué. Une fois le bouton cliqué, l'état de la couleur est mis à jour avec la valeur de `text`, changeant la couleur du `text` en ce que l'utilisateur tape.

Voici le résultat :

![Ajout de useState() à l'application](https://www.freecodecamp.org/news/content/images/2024/05/useState---zustand.gif align="left")

*Ajout de useState() à l'application*

### Avantages et inconvénients de `useState()`

Avantages :

* Intégré à React, donc pas besoin de dépendances supplémentaires.

* API simple et intuitive, facile à comprendre et à utiliser.

Inconvénients :

* Limité à la gestion de l'état local du composant.

* Peut conduire à du [prop drilling](https://www.freecodecamp.org/news/avoid-prop-drilling-in-react/) dans les composants profondément imbriqués, ce qui peut causer de la confusion si vous ne comprenez pas le prop drilling.

* Les scénarios complexes de gestion d'état peuvent nécessiter une logique supplémentaire pour être gérés.

Pour en savoir plus sur `useState()` et d'autres hooks fonctionnels, consultez cet article : [Simplifiez votre programmation React sans effort avec ces 8 hooks incroyables](https://ijaycent.hashnode.dev/simplify-your-react-programming-effortlessly-with-these-8-amazing-hooks).

## Comment utiliser la bibliothèque Zustand pour la gestion d'état

### Présentation de Zustand

`Zustand` est un outil pratique de gestion d'état pour gérer l'état dans les applications React. Il est petit, fonctionne rapidement et évolue avec vos besoins.

Avec `Zustand`, vous pouvez créer et mettre à jour des états globaux qui peuvent être facilement partagés entre différentes parties de votre application. C'est comme avoir un hub central pour les informations de votre application, ce qui simplifie l'organisation et l'accès aux données depuis n'importe quel endroit de votre application.

### Utilisation de base et syntaxe de Zustand

Pour commencer avec Zustand, suivez ces étapes :

Tout d'abord, commencez par installer Zustand dans votre application React en utilisant la commande :

```javascript
npm install zustand
// ou
yarn add zustand
```

Ensuite, dans votre application React, accédez au répertoire `src` et créez un nouveau dossier appelé `store`.

À l'intérieur du dossier `store`, créez un fichier nommé `color.js` (ou tout autre nom préféré). Ce fichier JavaScript définit votre état.

![Architecture de votre application React](https://www.freecodecamp.org/news/content/images/2024/05/zustand-color.js-1.png align="left")

*Architecture de votre application React*

Ensuite, dans ce fichier `color.js`, importez la fonction `create` de Zustand pour commencer à configurer votre gestion d'état :

```plaintext
import { create } from zustand
```

Nous allons utiliser la fonction `create` pour construire un hook personnalisé, qui agit comme le point d'accès principal à notre store.

Le fichier `color.js` est l'endroit où nous garderons toutes nos valeurs d'état et les actions. Pensez aux actions comme aux valeurs mises à jour. C'est similaire à la façon dont vous utilisez `useState()`.

```javascript
import { create } from 'zustand';

// Créer un hook personnalisé appelé useColor
export const useColor = create((set) => ({
  // État initial : text et color tous deux définis sur 'black'
  text: 'black',
  color: 'black',

  // Fonction pour mettre à jour l'état du text
  setText: (text) => set({ text }),

  // Fonction pour mettre à jour l'état de la couleur
  setColor: (color) => set({ color }),
}));
```

Passons en revue ce que fait ce code :

* Ce code crée un outil spécial (un hook) appelé `useColor` en utilisant Zustand.

* L'outil `useColor` aide à suivre deux choses : le texte et la couleur.

* Au début, le texte et la couleur sont tous deux définis sur "black".

* Il y a deux autres outils dans `useColor` : `setText`, qui est utilisé pour changer le texte en ce que nous voulons, et `setColor`, qui est utilisé pour changer la couleur en n'importe quelle couleur que nous choisissons.

La création de ce store implique de le définir dans un fichier. Cela le rend réutilisable dans toute votre application et le rend global. Cela élimine le besoin de se soucier de passer des props.

Ensuite, vous devez le passer à votre composant pour qu'il soit utilisé :

```javascript
// D'abord, nous allons importer useColor depuis un dossier nommé 'store'
import { useColor } from '../store/color';


const UseZustand = () => {
  // nous allons importer les fonctions que nous avons définies dans color.js et les déstructurer pour pouvoir les utiliser dans notre composant
    // passer un état dans le hook personnalisé que nous avons créé ; cet état sera maintenant utilisé pour définir et mettre à jour les valeurs
  const { text, color, setText, setColor } = useColor((state) => ({
    text: state.text,
    color: state.color,
    setText: state.setText,
    setColor: state.setColor,
  }));


  const handleInputChange = (e) => {
    setText(e.target.value);
  };
    
    
// Fonction définie pour le bouton
// Lorsque le bouton est cliqué, nous utilisons setColor pour changer la couleur en ce que nous avons tapé
  const handleButtonClick = () => {
    setColor(text);
  };

  
  return (
    <div className='container'>
      <h1 style={{ color: color }}>
        Gestion d'état avec Zustand
      </h1>
      <br />
      <div className='input'>
        <input
          type='text'
          className='input'
          value={text}
          onChange={handleInputChange}
        />
        <button className='btn' onClick={handleButtonClick}>
          Changer la couleur
        </button>
      </div>
    </div>
  );
};


export default UseZustand;
```

En résumé :

* Nous utilisons un outil appelé `useColor` pour suivre le texte et la couleur.

* Dans notre section d'application `UseZustand`, nous permettons aux utilisateurs de taper quelque chose et de changer sa couleur en cliquant sur un bouton.

Voici à quoi ressemble le résultat final :

![Application de zustand à l'application](https://www.freecodecamp.org/news/content/images/2024/05/applying-zustand.gif align="left")

*Application de zustand à l'application*

### Avantages et inconvénients de Zustand

Avantages :

* Gestion d'état globale sans prop drilling.

* Simple et concis pour définir et accéder à l'état.

* Support intégré pour les middleware et les outils de développement.

Inconvénients :

* Nécessite une dépendance supplémentaire par rapport à useState.

* Peut introduire une courbe d'apprentissage pour les développeurs nouveaux à la bibliothèque.

## En quoi Zustand diffère-t-il de useState ?

Contrairement à `useState()`, Zustand permet aux développeurs de créer et de gérer un état global qui peut être accessible depuis n'importe quel composant de l'application sans prop drilling.

Il offre une approche plus centralisée de la gestion d'état.

### Facteurs à considérer lors du choix entre Zustand et useState

Voici quelques éléments simples à considérer lors du choix entre Zustand et useState :

* **Complexité de l'état** : Si l'état de votre application est simple, useState pourrait suffire. Mais pour des besoins d'état plus complexes, Zustand pourrait être meilleur.

* **Vitesse** : Zustand est connu pour être rapide, ce qui est idéal si votre application doit être rapide.

* **Compétences de l'équipe** : Si votre équipe connaît déjà l'utilisation des hooks React, useState pourrait être plus facile. Mais si ils sont ouverts à l'apprentissage de quelque chose de nouveau, Zustand pourrait valoir le coup.

* **Croissance de l'application** : Considérez comment votre application pourrait évoluer au fil du temps. L'approche centralisée de Zustand peut faciliter la gestion de l'état à mesure que votre application grandit.

* **Support de la communauté** : Voyez quelles ressources et aides sont disponibles pour Zustand et useState. Une communauté solide peut être utile.

En réfléchissant à ces éléments, vous devriez pouvoir décider. Cela vous montrera quelle option de gestion d'état est la meilleure pour votre projet.

### Quelles sont les différences entre ces deux outils de gestion d'état ?

La différence entre les deux outils réside dans leurs fonctionnalités, ce qui vous permet de prendre une décision éclairée.

| Fonctionnalité | useState | Zustand |
| --- | --- | --- |
| **Gestion de la complexité** | Bon pour l'état simple dans un composant | Meilleur pour l'état complexe partagé entre plusieurs composants |
| **Portée de l'état** | Local à un composant | État global qui peut être utilisé par n'importe quel composant |
| **Performance** | Fonctionne bien pour les petites tâches | Conçu pour réduire les re-rendus |
| **Facilité d'utilisation** | Très simple à démarrer, aucune configuration nécessaire | Nécessite un peu plus de configuration, plus de fonctionnalités mais un peu plus difficile à apprendre |
| **Évolutivité** | Peut devenir compliqué à mesure que l'application grandit, souvent besoin d'autres outils pour les grandes applications | Gère bien la croissance, plus facile à gérer l'état dans les grandes applications |
| **Support et outils** | Fait partie de React, beaucoup d'aide et d'informations disponibles, aucune bibliothèque supplémentaire nécessaire | Bibliothèque séparée, bon support, pas autant d'informations que useState mais toujours bon |
| **Courbe d'apprentissage** | useState est plus facile à apprendre | Zustand a une courbe d'apprentissage légèrement plus raide en raison de son processus de création de store. |

### Cas d'utilisation

1. Pour une gestion d'état simple, useState() est souvent suffisant.

2. Zustand offre des avantages comme un état centralisé et la réduction du prop drilling dans les applications complexes.

3. En ce qui concerne la performance, Zustand est conçu pour être rapide et efficace. Il est fait pour réduire les re-rendus inutiles de vos composants. Cela peut rendre votre application plus fluide.

Vous ne savez pas quoi construire avec `useState()` ou `zustand` ? Vous pouvez consulter cette application très simple construite avec React : [Birthday Reminder](https://ijayhub.github.io/Birthday-reminder/). Et la voici sur mon [GitHub](https://github.com/ijayhub/Birthday-reminder).

## Conclusion

En conclusion, `Zustand` et `useState()` sont tous deux utiles pour gérer l'état dans React. Ils servent à des fins différentes en fonction des exigences et de l'échelle de votre projet. Vous devez comprendre les forces et les faiblesses de chaque approche afin de choisir la meilleure option de gestion d'état pour votre application.

Avez-vous déjà utilisé `Zustand` ou `useState()` ? Partagez vos expériences, vos idées et vos conseils sur [Twitter](https://https//twitter.com/ijaydimples)! Votre contribution pourrait faire une réelle différence pour d'autres développeurs confrontés à la gestion d'état dans React.

Vous pouvez lire la [documentation de Zustand](https://docs.pmnd.rs/zustand/getting-started/introduction) pour en savoir plus.

Si vous avez trouvé cet article utile, partagez-le avec d'autres qui pourraient également le trouver intéressant.

Restez informé de mes projets en me suivant sur [Twitter](https://https//twitter.com/ijaydimples) et [LinkedIn](https://www.linkedin.com/in/ijeoma-igboagu/) ou consultez mon [BioDrop](https://www.biodrop.io/ijayhub).

Si vous aimez ce que je fais et souhaitez montrer votre soutien ou souhaitez [montrer un peu d'amour](https://selar.co/showlove/httpsselarcow43744), envisagez de [m'offrir un café](https://www.buymeacoffee.com/ijewriter) ou de consulter mon e-livre pour enfants ! Votre soutien compte beaucoup pour moi !

Continuez à apprendre, continuez à partager et bon codage !

Merci d'avoir lu.