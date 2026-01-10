---
title: Comment améliorer votre code ReactJS – Conseils pour la lisibilité et la performance
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-09-11T20:34:10.000Z'
originalURL: https://freecodecamp.org/news/improve-reactjs-code
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/Group-5.png
tags:
- name: Code Quality
  slug: code-quality
- name: React
  slug: react
- name: React
  slug: reactjs
seo_title: Comment améliorer votre code ReactJS – Conseils pour la lisibilité et la
  performance
seo_desc: "By Neha sharma\nReactJS is one of the most popular JavaScript libraries\
  \ for building scalable and performant applications. \nWhen you're working on ReactJS\
  \ projects, whether they're large or small, you'll need to focus on code quality,\
  \ readability, mai..."
---

Par Neha Sharma

ReactJS est l'une des bibliothèques JavaScript les plus populaires pour construire des applications scalables et performantes. 

Lorsque vous travaillez sur des projets ReactJS, qu'ils soient grands ou petits, vous devez vous concentrer sur la qualité du code, la lisibilité, la maintenabilité et la scalabilité. 

Écrire un bon code vous aidera également à réduire les commentaires de PR de vos coéquipiers (et soyons honnêtes – qui n'aime pas les commentaires comme LGTM :) ).

Dans ce tutoriel, vous apprendrez comment améliorer votre code React. Je partagerai mes conseils préférés avec des exemples de code pour vous montrer comment tout fonctionne. Ceux-ci vous aideront à écrire un code maintenable, scalable et lisible.

Vous devriez avoir une familiarité de base avec React pour tirer le meilleur parti de ce guide.

## 1. Utiliser des constantes

En JavaScript, nous pouvons déclarer des constantes en utilisant le mot-clé `const`. Cela nous aide à éviter de redéclarer la même valeur. Les constantes sont donc un excellent choix pour stocker les clés API et d'autres valeurs similaires.

Les constantes améliorent la scalabilité, la lisibilité et l'internationalisation de toute base de code React. 

Dans chaque projet ReactJS, vous devriez éviter de coder en dur les chaînes de caractères (contenu) dans vos composants. 

Cela rendra votre projet plus maintenable, scalable et lisible, car il isole les couches UI, données et contenu les unes des autres.

Les constantes incluent :

* Clés API
* URLs
* Contenu

De nombreux sites web supportent plusieurs langues, comme l'anglais, le français, l'espagnol, etc. Cela est connu sous le nom d'internationalisation (ou i18n pour faire court). 

Si vous activez les fonctionnalités i18n sur votre site, vous devriez créer des fichiers de constantes séparés pour votre contenu – par exemple `en.js` et `fr.js`. Même si vous n'avez pas de support multilingue ou pas d'i18n, il est toujours bon de garder votre contenu en dehors de votre code dans un fichier de constantes.

Vous pouvez nommer votre fichier de constantes soit `[LANGUE_INITIALE].js`, soit `constants.js`. Ce sont les noms de fichiers les plus courants que les développeurs utilisent à cette fin.

### Comment créer votre fichier de constantes :

Les constantes sont simplement des objets JavaScript avec des paires clé/valeur. Nous commençons par déclarer l'objet avec un nom qui reflète le contenu qu'il contient. Comme ce sont des chaînes de caractères, nous utilisons des guillemets pour les entourer. Avant d'exporter les messages, faites un `Object.freeze()` – cela évitera tout changement de valeur accidentel depuis l'extérieur de toute clé. 

Pour utiliser les constantes, nous devons importer le fichier dans le fichier du composant. Une fois importé, nous pouvons utiliser l'opérateur point pour accéder aux clés :

```Javascript
// constants.js ou en.js
const MESSAGES = { 
    'HEADING': 'Bienvenue sur le site",
    'ENTER_YOUR_NAME': 'Entrez votre nom',
    'HOME': [{
        'HEADING': 'Bienvenue à la maison'
     }]
}

Object.freeze(MESSAGES);

export default MESSAGES;
```

```javaScript

// Utilisation de constants.js dans un composant
import MESSAGES from '../constants/constants

const Home = () => {
    return(
        <p>{MESSAGES.HEADING}</h1>
    )
}

export default Home;

```

## 2. Utiliser des Helpers / Utils

Lorsqu'on travaille sur une base de code ReactJS, il est crucial d'identifier les parties du code qui peuvent être des utils ou helpers indépendants, au lieu de coupler étroitement les composants.

Les helpers ou utils sont responsables de l'exécution d'une tâche qui peut être utilisée à plusieurs endroits et par plusieurs développeurs. Parmi les exemples, on trouve le formatage de dates, la formation de chaînes de caractères, le code d'appel API et la manipulation du DOM, pour n'en nommer que quelques-uns.

### Pourquoi utiliser des Helpers / Utils ?

Chaque composant doit être responsable d'une seule tâche, ce qui est connu sous le nom de "principe de responsabilité unique". 

Nous devons identifier les fonctions réutilisables et les déplacer vers les utils pour les raisons suivantes :

1. Cela donne des composants plus propres et un code plus propre
2. Pas de couplage serré
3. Fonctionnalité facilement scalable
4. Facile à maintenir et à déboguer
5. Meilleure réutilisabilité
6. Les composants sont maintenant responsables uniquement de l'UI

```javascript
```
// dateUtils.js : Déplacement de formatDate vers un fichier util séparé pour la réutilisabilité

export function formatDate(date) {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return new Date(date).toLocaleDateString(undefined, options);
}
```

```react
// Composant Blog.jsx mis à jour après l'utilisation de l'utilitaire
import React, { Component } from 'react';
import { formatDate } from './dateUtils'; 

const Blog = ({title, content, date}) => {
	return (
        <div>
            <h2>{title}</h2>
            <p>{content}</p>
            <p>Publié le : {formatDate(date)}</p>
        </div>
    );
}
}

```

Par exemple, dans le code ci-dessus, vous pouvez voir que nous avons une fonction `formatDate` à l'intérieur du composant `Blog`. Ici, nous pouvons déplacer `formatDate` vers les utils. Pourquoi ?

* `formatDate` est responsable du formatage de la date, et non de la publication de la date
* `formatDate` peut être utilisé par un autre composant
* `formatDate` peut avoir différents formats en fonction des exigences métier. Par exemple, maintenant nous passons un deuxième argument basé sur les exigences de ce composant. Si une nouvelle exigence survient, le développeur doit réécrire le composant.

## 3. Apprendre à utiliser les Props 

Pour communiquer entre les composants dans ReactJS, [nous utilisons `props`](https://www.freecodecamp.org/news/props-in-react/). Mais il existe différentes façons de le faire.

Il est crucial de choisir un seul style pour consommer les props dans le composant dans votre base de code. Cela rendra la base de code cohérente. Il existe plus d'une façon de déstructurer les props, c'est pourquoi vous devriez en choisir une seule pour la cohérence et la lisibilité de votre code.

Parlons des différentes façons de travailler avec les props dans React.

### Comment utiliser `Props`

Dans cette approche, nous devons répéter `props` chaque fois que nous utilisons `props`.

Cette approche n'est pas une bonne façon de consommer `props` car nous répétons props chaque fois que nous voulons les utiliser. En plus d'être répétitif, lorsque cela concerne la création de props imbriqués, cela nécessitera trop de frappe.

Votre temps en tant que développeur est important, et nous voulons optimiser le code partout où c'est possible et ne pas répéter les choses sauf si c'est absolument nécessaire.

Dans l'exemple de code ci-dessous, vous pouvez voir pourquoi cette approche n'est pas la meilleure. Nous avons le composant `Input` avec `props` tels que `type`, `placeholder`, `name`, et `changeHandler`. Dans la section `return`, nous répétons `props` avec chaque `attribute` tel que `props.type`.

```javascript
const Input = (props) => {
    return <input 
    type={props.type} 
    placeholder={props.placeholder} 
    name={props.name} 
    className="block p-2 my-2 text-black" 
    onChange={props.changeHandler}/>
}

export default Input;

```

### Comment déstructurer les props 

Dans la deuxième façon de travailler avec `props`, nous utilisons [l'affectation par déstructuration JavaScript](https://www.freecodecamp.org/news/destructuring-patterns-javascript-arrays-and-objects/). 

C'est une amélioration par rapport à la première approche, car dans celle-ci nous ne répétons pas `props` chaque fois que nous utilisons props.

Voici un exemple de déstructuration de `props`. Dans le premier extrait de code, nous obtenons `type`, `placeholder`, `name`, et `changeHandler` de `props` dès le début du composant.

```js
const { type, placeholder, name, changeHandler } = props
```

Dans l'exemple de code ci-dessous, nous pouvons voir l'amélioration du code. Nous avons le composant `Input` avec `props`, mais au lieu de répéter `props.name`, nous déstructurons les props. C'est une énorme amélioration en termes de lisibilité et d'expérience développeur.

```javascript
const Input = (props) => {
    const { type, placeholder, name, changeHandler } = props;
    return <input 
    type={type} 
    placeholder={placeholder} 
    name={name} 
    className="block p-2 my-2 text-black" 
    onChange={changeHandler}/>
}

```

### Comment déstructurer les props dans les arguments du composant

C'est ma méthode préférée pour déstructurer les props. Les développeurs peuvent voir dès le début du composant quelles props seront utilisées dans le composant. Nous n'avons également aucune répétition du mot-clé `props`.

Comparé à l'approche précédente, c'est :

* DRY (Don't Repeat Yourself) : nous ne répétons pas les props
* Lisible : À la première ligne du composant (définition), nous savons quelles props il attend. Cela améliore la lisibilité et la clarté du composant.

Dans le code ci-dessous, nous pouvons voir que nous déstructurons `props` dans la définition du composant. Cela améliore grandement la lisibilité. Maintenant, les développeurs peuvent regarder la première ligne et comprendre combien et quelles `props` sont attendues dans ce composant.

```javascript
const Input = ({ type, placeholder, name, changeHandler }) => {
    return <input 
    type={type} 
    placeholder={placeholder} 
    name={name} 
    className="block p-2 my-2 text-black" 
    onChange={changeHandler}/>
}

```

## 4. Avoir un fichier par composant

Dans ReactJS, il est important d'avoir un fichier par composant. Cela aide à rendre votre code plus propre et plus maintenable.

Cela suit également le [principe de responsabilité unique](https://en.wikipedia.org/wiki/Single-responsibility_principle) que j'ai mentionné précédemment.

Il est tentant d'avoir un seul fichier et d'y écrire tout le code pour l'isolation – mais nous devons le diviser en composants plus petits.

Dans l'exemple ci-dessous, nous avons un fichier `Input.jsx` qui contient deux composants `Input` et `Icon`. Nous utilisons `Icon` dans la section `return` de `Input`.

Il semble que `Input` et `Icon` soient liés et qu'il soit logique de les regrouper dans un seul fichier. Mais nous ne devrions pas faire cela, car ce n'est pas une solution scalable (et ce n'est pas non plus réutilisable).

```javascript
// Ne faites pas cela :
import React from 'react';

// Nom du fichier : Input.jsx
// Cet exemple montre comment nous exportons 2 composants depuis un seul fichier
// Nous ne devrions PAS faire cela
const Input = ({ type, placeholder, name, changeHandler }) => {
    return <>
    <input 
    type={type} 
    placeholder={placeholder} 
    name={name} 
    className="block p-2 my-2 text-black" 
    onChange={changeHandler}/>
    
    <Icon type="warning"/>
}
        <>

const Icon = ({ type, url}) => {
    return <img src={url} data-type={type} />
}

export {Input, Icon};

```

Au lieu de cela, nous devons créer deux composants séparés pour `Input` et `Icon`, comme montré ci-dessous. Cela vous aidera à réutiliser les deux composants et à les scaler individuellement.

```javascript
// Faites cela à la place :
// Input.jsx : créez 2 fichiers séparés pour Input et InputIcon
import React from 'react';

const Input = ({ type, placeholder, name, changeHandler }) => {
    return <input 
    type={type} 
    placeholder={placeholder} 
    name={name} 
    className="block p-2 my-2 text-black" 
    onChange={changeHandler}/>
}

export default Input;


```

## 5. Ne pas utiliser de fonctions en ligne

Il est courant d'écrire des fonctions en ligne en JavaScript, mais il est préférable d'éviter de les ajouter lorsque c'est possible.

Vous devez garder votre JSX séparé de votre code logique. Les fonctions en ligne ne sont pas réutilisables, n'aident pas à l'abstraction du code et sont difficiles à tester.

C'est pourquoi vous devez toujours éviter les fonctions en ligne.

Dans l'exemple de code ci-dessous, nous avons la fonction `handleIncrement` en tant que fonction en ligne sur `button`. Elle n'est pas réutilisable et est étroitement couplée au composant :

```javascript
// Ne faites pas cela :
import React, { useState } from 'react';

function CounterInline() {
  const [count, setCount] = useState(0);

  const handleIncrement = () => {
    setCount(count + 1);
  };

  return (
    <div>
      <p>Compte : {count}</p>
      <button onClick={handleIncrement}>Incrémenter</button> 
    </div>
  );
}

export default CounterInline;


```

Alors, comment pouvons-nous éviter les fonctions en ligne ? Regardons comment vous pouvez refactoriser le code ci-dessus.

Dans le code ci-dessous, nous avons `incrementCount` utilisé sur `button` et il attend deux arguments. Nous avons rendu la fonction réutilisable ici :

```javascript
// Faites cela à la place :
import React, { useState } from 'react';

// Fonction autonome pour l'incrémentation
function incrementCount(currentCount, setCount) {
  setCount(currentCount + 1);
}

const CounterStandalone = () => {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Compte : {count}</p>
      <button onClick={() => incrementCount(count, setCount)}>Incrémenter</button>
    </div>
  );
}

export default CounterStandalone;


```

## 6. Implémenter un composant et une route 404 

Lors de l'implémentation du routage dans ReactJS, nous devons ajouter un composant 404.

Lorsque l'utilisateur essaie d'accéder à une page qui n'existe pas, le code de statut du serveur sera 404. En tant que développeur front-end, il est bon de montrer à l'utilisateur un message d'erreur pour lui donner un contexte.

React-router fournit un moyen facile d'afficher l'erreur lorsque le serveur retourne un 404. Vous devrez créer un composant qui doit être rendu lorsque le code de statut 404 est retourné par le serveur.

Chaque fois qu'un utilisateur tape ou atteint une route introuvable, la page 404 affichera l'erreur à l'utilisateur, ce qui est une meilleure expérience utilisateur (plutôt que de simplement voir un "404" inexpliqué).

Conseil : Dans le composant, ajoutez un lien vers la page d'accueil de votre site web. Cela aidera l'utilisateur à rediriger vers la page d'accueil de votre site web.

```JavaScript
    <route path="*" component={<Error404/>} />
```

## 7. Récupérer les données de manière progressive

Dans les applications React, vous récupérez souvent des données via des APIs. 

Au lieu de récupérer et de créer l'UI en une seule fois, nous devons récupérer les données à la demande – par exemple, lors du défilement, lors du clic sur la pagination, etc.

Cela améliorera les performances de l'application ainsi que l'expérience utilisateur. 

Il existe quelques packages qui peuvent vous aider à implémenter le lazy-loading. Le lazy loading est une technique que vous pouvez utiliser pour charger les données à la demande ou progressivement selon les besoins. Au lieu d'afficher toutes les données de l'API à l'écran en une seule fois, il n'affichera que les données à la demande.

Voici comment vous pouvez installer le package `react-lazyload` :

```javascript
// installer le package react-lazyload
npm install react-lazyload
```

Et voici le code :

```javascript
// Créer un composant - ItemList.jsx
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ItemList = () => {
  const [items, setItems] = useState([]);

  useEffect(() => {
    // Récupérer les données de votre API ici
    axios.get('https://example.com/api/items')
      .then(response => {
        setItems(response.data);
      })
      .catch(error => {
        console.error('Erreur lors de la récupération des données :', error);
      });
  }, []);

  return (
    <div>
      <h2>Liste des éléments</h2>
      <ul>
        {items.map(item => (
          <li key={item.id}>
            {item.name}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ItemList;


```

```javascript
// App.js
import React, { lazy, Suspense } from 'react';
import LazyLoad from 'react-lazyload';

// Importer le composant lazy-loaded
const ItemList = lazy(() => import('./ItemList'));

function App() {
  return (
    <div>
      <h1>Exemple de React LazyLoad avec données API</h1>

      {/* Utiliser React LazyLoad pour lazy-loader le composant */}
      <LazyLoad height={200}>
        <Suspense fallback={<div>Chargement...</div>}>
          <ItemList />
        </Suspense>
      </LazyLoad>
    </div>
  );
}

export default App;


```

Dans l'exemple de code ci-dessus, nous avons créé un composant qui effectuera les requêtes API et rendra les données de l'API `ItemList.jsx`. Lors de l'utilisation de `ItemList` dans `App`, au lieu de rendre toutes les données en une seule fois, nous utiliserons `LazyLoad` pour charger le composant. 

En conséquence, le composant est chargé de manière paresseuse lorsqu'il est proche d'être visible dans le viewport, et les données de l'API seront affichées.

Certains des packages que vous pouvez utiliser pour le lazy loading sont `react-lazyload`, `react-infinite-scroll-component`, et `react-paginate`.

## 8. Utiliser des valeurs uniques pour les attributs Key

L'une des raisons pour lesquelles React est populaire est son "virtual DOM".

Le virtual DOM (VDOM) vous aide à optimiser le processus de mise à jour de l'UI. 

React ne mettra à jour que les nœuds qui ont changé et non tout le DOM, sauf si cela est nécessaire. C'est l'un des secrets des applications les plus performantes. 

React a besoin d'un attribut `key` pour identifier à quel nœud le changement s'est produit. C'est pourquoi nous devons toujours utiliser une valeur unique pour `key`. 

Un bon exemple de la façon de faire cela est d'ajouter l'`id` de chaque élément.

Note : utilisez l'index comme clé uniquement lorsque vos données sont statiques, non réordonnées ou filtrées.

```javascript
// List.jsx
import React from 'react';

const List = ({ items }) => (

  return(<ul>
    {items.map((item, index) => (
      <li key={index}>{item}</li>
    ))}
  </ul>)
);

export default List;

```

```javascript
// App.jsx
import List from './List';

const App = () => {
  const items = ['Élément 1', 'Élément 2', 'Élément 3', 'Élément 4', 'Élément 5'];

  return (
    <div>
      <h1>Exemple de liste simple</h1>
      <List items={items} />
    </div>
  );
};

export default App;
```

Dans l'exemple de code ci-dessus, nous créons une liste en mappant les données. Dans le composant `List`, nous attribuons l'`index` à l'attribut `key`. Cela sera utilisé par ReactJS sous le capot pour optimiser les performances chaque fois qu'un `li` sera mis à jour ou changé.

## 9. Utiliser les Types

L'utilisation d'outils avec vérification de type statique intégrée (comme TypeScript) peut vous aider à éviter des bugs inutiles dans votre code.

Cela soutiendra également votre code avec la qualité et la vérification de type. 

Si vous êtes quelqu'un qui commence tout juste à apprendre la vérification de type, alors vous pouvez commencer avec `proptypes` et apprendre TypeScript plus tard. 

JavaScript n'est pas strictement typé, ce qui signifie qu'il y a une probabilité plus élevée que vous ayez des bugs inattendus ou des erreurs de type. 

Par exemple, lorsque nous attendons qu'une prop soit un nombre, elle pourrait finir par être une chaîne de caractères, ce qui causerait une erreur.

Ainsi, les types stricts et TypeScript peuvent vous aider à éviter de tels bugs inattendus pendant le développement.

```javascript
import React from 'react';
import PropTypes from 'prop-types';

const UserCard = ({ name, age, email }) => {
  return (
    <div>
      <h2>Carte Utilisateur</h2>
      <p>Nom : {name}</p>
      <p>Âge : {age}</p>
      <p>Email : {email}</p>
    </div>
  );
};

// Définir les types de props pour le composant UserCard
UserCard.propTypes = {
  name: PropTypes.string.isRequired, // Une prop string requise
  age: PropTypes.number.isRequired,  // Une prop number requise
  email: PropTypes.string,           // Une prop string optionnelle
};

```

```javascript
import UserCard from 'userCard';

const App = () => {
  return (
    <div>
      <h1>Exemple PropTypes</h1>
      <UserCard name="John Doe" age={30} email="john@example.com" />
    </div>
  );
};

export default App;
```

Dans l'exemple de code ci-dessus, nous avons créé un composant `UserCard`. Ce composant attend 3 props : name, age, et email. En utilisant `proptypes`, nous déclarerons deux choses pour les props – le type de données (quel sera le type de données des props, par exemple string, number, etc.), et si c'est requis ou optionnel. 

Lors de l'utilisation du composant `UserCard`, si quelqu'un passe le mauvais type de données ou manque une prop requise, alors le code lancera une erreur et les avertira de la corriger. 

## 10. Utiliser les fonctions `lazy()` et `Suspense()`

ReactJS utilise le bundler Webpack (si vous utilisez create-react-app). 

Webpack s'occupe du bundling du code et effectue des fonctions comme [tree shaking](https://www.freecodecamp.org/news/tree-shaking-es6-modules-in-webpack-2-1add6672f31b/). 

Mais la façon dont React fonctionne, c'est qu'il télécharge tout le code côté client même si nous n'en avons pas besoin. C'est une tâche coûteuse. Si la taille de votre bundle est grande, cela impactera les performances de vos applications. 

Une bonne façon d'éviter cela est de charger le code à la demande en utilisant `lazy()`, ce qui permettra aux routes de se charger lorsqu'elles sont nécessaires.

```javascript
const LazyComponent = lazy(() => import('./LazyComponent'));
```

Lors de l'utilisation de `lazy()`, nous devons également utiliser `Suspense()`, car `lazy()` est une façon asynchrone de charger les composants. 

Nous ne voulons pas montrer à l'utilisateur un écran vide jusqu'à ce que notre route soit chargée. `Suspense()` aide en montrant un message pendant que le composant est en train de charger.

```javascript
 <Suspense fallback={<div>Chargement...</div>}>
        {/* Le LazyComponent ne sera chargé que lorsque nécessaire */}
        <LazyComponent />
 </Suspense>
```

## Conclusion

Ouf, nous avons atteint la fin. Ces conseils ne sont pas seulement limités aux grandes bases de code, mais aux projets de toute taille. 

Au niveau général, nous avons appris les concepts suivants :

1. Suivre le principe DRY
2. Suivre le principe de responsabilité unique
3. Créer une bonne expérience utilisateur en chargeant les données de manière progressive
4. Améliorer la lisibilité
5. Améliorer l'expérience développeur
6. Éviter les bugs au moment du développement
7. Améliorer les performances

Bon apprentissage !

N'hésitez pas. Venez dire bonjour ! Vous pouvez me trouver sur [Twitter](https://twitter.com/hellonehha), [LinkedIn](https://www.linkedin.com/in/nehha/), et [YouTube](https://youtube.com/@hellonehha).

Vous voulez voir de la calligraphie ? Consultez mon art sur instagram.com/calligraphyzen.