---
title: Comment créer un menu accordéon en React à partir de zéro – Aucune bibliothèque
  externe requise
subtitle: ''
author: Yogesh Chavan
co_authors: []
series: null
date: '2021-03-15T22:52:29.000Z'
originalURL: https://freecodecamp.org/news/build-accordion-menu-in-react-without-external-libraries
coverImage: https://cdn-media-2.freecodecamp.org/w1280/604df0d628094f59be2558d6.jpg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: Comment créer un menu accordéon en React à partir de zéro – Aucune bibliothèque
  externe requise
seo_desc: 'There are many ways to use accordion menus, like displaying a list of FAQs,
  showing various menus and submenus, displaying the locations of a particular company,
  and so on.

  In this article, we''ll see how to build an accordion menu in React completely...'
---

Il existe de nombreuses façons d'utiliser les menus accordéon, comme afficher une liste de FAQ, montrer divers menus et sous-menus, afficher les emplacements d'une entreprise particulière, et ainsi de suite.

Dans cet article, nous verrons comment construire un menu accordéon en React complètement à partir de zéro, étape par étape, sans utiliser de bibliothèques externes.

Nous utiliserons la syntaxe des Hooks React pour construire cette application en React. Donc, si vous êtes nouveau dans les Hooks React, consultez mon article [Introduction aux Hooks React](https://levelup.gitconnected.com/an-introduction-to-react-hooks-50281fd961fe?source=friends_link&sk=89baff89ec8bc637e7c13b7554904e54) pour apprendre les bases des Hooks.

**Vous pouvez voir la démonstration en direct de l'application [ici](https://react-accordion-demo.netlify.app/).**

Alors, commençons.

## Configuration initiale du projet

Créez un nouveau projet en utilisant `create-react-app`

```javascript
npx create-react-app react-accordion-demo

```

Une fois le projet créé, supprimez tous les fichiers du dossier `src` et créez les fichiers `index.js`, `App.js` et `styles.css` à l'intérieur du dossier `src`. Créez également un nouveau dossier nommé `utils` à l'intérieur du dossier `src`.

Ouvrez le fichier `styles.css` et ajoutez le contenu de [ici](https://github.com/myogeshchavan97/react-accordion-demo/blob/master/src/styles.css) à l'intérieur.

## Comment créer les pages initiales

Ouvrez le fichier `src/App.js` et ajoutez le contenu suivant à l'intérieur :

```jsx
import React from 'react';

const App = () => {
  const accordionData = {
    title: 'Section 1',
    content: `Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quis sapiente
      laborum cupiditate possimus labore, hic temporibus velit dicta earum
      suscipit commodi eum enim atque at? Et perspiciatis dolore iure
      voluptatem.`
  };

  const { title, content } = accordionData;

  return (
    <React.Fragment>
      <h1>Démonstration de l'accordéon React</h1>
      <div className="accordion">
        <div className="accordion-item">
          <div className="accordion-title">
            <div>{title}</div>
            <div>+</div>
          </div>
          <div className="accordion-content">{content}</div>
        </div>
      </div>
    </React.Fragment>
  );
};

export default App;

```

Ici, nous utilisons les propriétés de l'objet `accordionData` pour afficher le contenu de l'accordéon.

Pour la propriété `content`, nous utilisons la syntaxe des littéraux de gabarit ES6 (``) afin de pouvoir répartir le contenu sur plusieurs lignes, et nous avons utilisé un texte factice lorem ipsum.

Maintenant, ouvrez le fichier `src/index.js` et ajoutez le contenu suivant à l'intérieur :

```jsx
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import './styles.css';

ReactDOM.render(<App />, document.getElementById('root'));

```

Maintenant, si vous exécutez l'application en utilisant la commande `yarn start` depuis le terminal, vous verrez l'écran suivant :

![Initial Accordion](https://gist.github.com/myogeshchavan97/98ae4f4ead57fde8d47fcf7641220b72/raw/92ab4961521a20180285b6fdf5179b6d17fbcdff/accordion_initial.png)

## Comment ouvrir et fermer le menu accordéon

Comme vous pouvez le voir ci-dessus, nous affichons une seule section en tant que partie de l'accordéon. Mais par défaut, l'accordéon est développé et nous ne pouvons pas le fermer. Ajoutons donc une fonctionnalité pour ouvrir et fermer l'accordéon.

Ajoutez un nouvel état à l'intérieur du composant comme indiqué ci-dessous :

```js
const [isActive, setIsActive] = useState(false);

```

Ici, nous avons défini l'état `isActive`. En fonction de cela, nous masquerons ou afficherons le contenu de l'accordéon.

Importons également le hook `useState` en haut du fichier :

```js
import React, { useState } from 'react';

```

Maintenant, pour la `div` avec la classe `accordion-title`, ajoutez le gestionnaire `onClick` comme ceci :

```jsx
<div className="accordion">
  <div className="accordion-item">
    <div
      className="accordion-title"
      onClick={() => setIsActive(!isActive)}
    >
      <div>{title}</div>
      <div>{isActive ? '-' : '+'}</div>
    </div>
    {isActive && <div className="accordion-content">{content}</div>}
  </div>
</div>

```

Ici, nous inversons la valeur de l'état `isActive` lorsque nous cliquons sur la div `accordion-title`. Si la valeur de `isActive` est `false`, nous la définissons sur `true` et vice-versa.

Nous affichons également le signe `+` ou `-` en fonction de la valeur de `isActive` en utilisant l'opérateur ternaire.

Et si la valeur de l'état `isActive` est `true`, alors nous affichons uniquement le contenu de l'accordéon comme indiqué ci-dessous :

```jsx
{isActive && <div className="accordion-content">{content}</div>}

```

Maintenant, si vous vérifiez l'application, vous verrez l'écran suivant :

![Open and close accordion](https://gist.github.com/myogeshchavan97/98ae4f4ead57fde8d47fcf7641220b72/raw/92ab4961521a20180285b6fdf5179b6d17fbcdff/open_close.gif)

Comme vous pouvez le voir, initialement, l'accordéon est fermé. Lorsque nous cliquons sur le titre, l'accordéon s'ouvre et nous pouvons cliquer à nouveau pour le fermer.

## Comment ajouter plusieurs sections dans l'accordéon

Cela fonctionne bien pour une seule section de l'accordéon. Mais si nous avons plusieurs sections, il ne sera pas bon de copier-coller le même code JSX encore et encore avec un contenu différent.

Créons donc un composant séparé pour afficher uniquement l'accordéon. Ensuite, en fonction du nombre de sections, nous bouclerons sur le composant pour afficher plusieurs sections.

Créez un nouveau fichier `Accordion.js` à l'intérieur du dossier `src` et ajoutez le contenu suivant à l'intérieur :

```jsx
import React, { useState } from 'react';

const Accordion = ({ title, content }) => {
  const [isActive, setIsActive] = useState(false);

  return (
    <div className="accordion-item">
      <div className="accordion-title" onClick={() => setIsActive(!isActive)}>
        <div>{title}</div>
        <div>{isActive ? '-' : '+'}</div>
      </div>
      {isActive && <div className="accordion-content">{content}</div>}
    </div>
  );
};

export default Accordion;

```

Ici, nous avons déplacé l'état et la div `accordion-item` du fichier `App.js` vers `Accordion.js`. Nous passons les props dynamiques `title` et `content` au composant en utilisant la syntaxe de déstructuration ES6 comme ceci :

```js
const Accordion = ({ title, content }) => {

```

Maintenant, ouvrez le fichier `App.js` et remplacez-le par le contenu suivant :

```jsx
import React from 'react';
import Accordion from './Accordion';

const App = () => {
  const accordionData = [
    {
      title: 'Section 1',
      content: `Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quis sapiente
      laborum cupiditate possimus labore, hic temporibus velit dicta earum
      suscipit commodi eum enim atque at? Et perspiciatis dolore iure
      voluptatem.`
    },
    {
      title: 'Section 2',
      content: `Lorem ipsum, dolor sit amet consectetur adipisicing elit. Mollitia veniam
      reprehenderit nam assumenda voluptatem ut. Ipsum eius dicta, officiis
      quaerat iure quos dolorum accusantium ducimus in illum vero commodi
      pariatur? Impedit autem esse nostrum quasi, fugiat a aut error cumque
      quidem maiores doloremque est numquam praesentium eos voluptatem amet!
      Repudiandae, mollitia id reprehenderit a ab odit!`
    },
    {
      title: 'Section 3',
      content: `Sapiente expedita hic obcaecati, laboriosam similique omnis architecto ducimus magnam accusantium corrupti
      quam sint dolore pariatur perspiciatis, necessitatibus rem vel dignissimos
      dolor ut sequi minus iste? Quas?`
    }
  ];

  return (
    <div>
      <h1>Démonstration de l'accordéon React</h1>
      <div className="accordion">
        {accordionData.map(({ title, content }) => (
          <Accordion title={title} content={content} />
        ))}
      </div>
    </div>
  );
};

export default App;

```

Ici, nous avons converti `accordionData` d'un objet en un tableau d'objets. Nous parcourons ce tableau en utilisant la méthode map, et nous passons le `title` et le `content` correspondants au composant `Accordion`.

Maintenant, si vous vérifiez l'application, vous verrez que les trois sections s'affichent et nous pouvons ouvrir et fermer chaque section comme indiqué ci-dessous :

![final working accordion](https://gist.github.com/myogeshchavan97/98ae4f4ead57fde8d47fcf7641220b72/raw/92ab4961521a20180285b6fdf5179b6d17fbcdff/final_working.gif)

## Comment refactoriser le code

Comme vous pouvez le voir, en déplaçant simplement la section accordéon dans un composant séparé et en passant le contenu dynamique en tant que props, nous sommes en mesure de créer une version fonctionnelle d'un accordéon à partir de zéro.

Il est préférable de garder les données statiques dans un fichier séparé. Déplaçons donc le tableau `accordionData` vers un fichier différent et importons-le dans `App.js`.

Créez un nouveau fichier appelé `content.js` à l'intérieur du dossier `utils` et ajoutez le contenu suivant à l'intérieur :

```js
export const accordionData = [
  {
    title: 'Section 1',
    content: `Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quis sapiente
    laborum cupiditate possimus labore, hic temporibus velit dicta earum
    suscipit commodi eum enim atque at? Et perspiciatis dolore iure
    voluptatem.`
  },
  {
    title: 'Section 2',
    content: `Lorem ipsum, dolor sit amet consectetur adipisicing elit. Mollitia veniam
    reprehenderit nam assumenda voluptatem ut. Ipsum eius dicta, officiis
    quaerat iure quos dolorum accusantium ducimus in illum vero commodi
    pariatur? Impedit autem esse nostrum quasi, fugiat a aut error cumque
    quidem maiores doloremque est numquam praesentium eos voluptatem amet!
    Repudiandae, mollitia id reprehenderit a ab odit!`
  },
  {
    title: 'Section 3',
    content: `Sapiente expedita hic obcaecati, laboriosam similique omnis architecto ducimus magnam accusantium corrupti
    quam sint dolore pariatur perspiciatis, necessitatibus rem vel dignissimos
    dolor ut sequi minus iste? Quas?`
  }
];

```

Maintenant, ouvrez `App.js` et remplacez-le par le contenu suivant :

```jsx
import React from 'react';
import Accordion from './Accordion';
import { accordionData } from './utils/content';

const App = () => {
  return (
    <div>
      <h1>Démonstration de l'accordéon React</h1>
      <div className="accordion">
        {accordionData.map(({ title, content }) => (
          <Accordion title={title} content={content} />
        ))}
      </div>
    </div>
  );
};

export default App;

```

Ici, nous avons simplement importé les données statiques depuis le fichier externe et les avons supprimées du fichier `App.js`.

Ainsi, le code semble maintenant propre et facile à comprendre, et la fonctionnalité fonctionne comme avant.

![final working accordion](https://gist.github.com/myogeshchavan97/98ae4f4ead57fde8d47fcf7641220b72/raw/92ab4961521a20180285b6fdf5179b6d17fbcdff/final_working.gif)

## Points de conclusion

Nous avons terminé la construction de la fonctionnalité de notre application.

**Vous pouvez trouver le code source complet de cette application sur GitHub dans [ce dépôt](https://github.com/myogeshchavan97/react-accordion-demo).**

### Merci d'avoir lu !

Vous souhaitez apprendre toutes les fonctionnalités d'ES6+ en détail, y compris let et const, les promesses, diverses méthodes de promesses, la déstructuration de tableaux et d'objets, les fonctions fléchées, async/await, import et export, et bien plus encore à partir de zéro ?

Consultez mon livre [Maîtriser le JavaScript Moderne](https://modernjavascript.yogeshchavan.dev/). Ce livre couvre tous les prérequis pour apprendre React et vous aide à devenir meilleur en JavaScript et React.

<a href="https://modernjavascript.yogeshchavan.dev/" target="_blank"><img src="https://gist.github.com/myogeshchavan97/98ae4f4ead57fde8d47fcf7641220b72/raw/92ab4961521a20180285b6fdf5179b6d17fbcdff/freecodecamp_image.jpeg" alt="Maîtriser le JavaScript Moderne"></a>