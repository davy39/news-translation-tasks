---
title: Comment styliser les composants React
subtitle: ''
author: Matéu.sh
co_authors: []
series: null
date: '2024-05-22T09:45:03.000Z'
originalURL: https://freecodecamp.org/news/how-to-style-react-components
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/How-to-style-react-components.png
tags:
- name: React
  slug: react
seo_title: Comment styliser les composants React
seo_desc: 'You can only make your React app visually appealing to users with styling.
  That makes styling a fundamental aspect of building captivating user interfaces.

  With React''s component-based architecture, there are a ton of options for styling.
  These inclu...'
---

Vous ne pouvez rendre votre application React visuellement attrayante pour les utilisateurs qu'avec le stylisme. Cela fait du stylisme un aspect fondamental de la création d'interfaces utilisateur captivantes.

Avec l'architecture basée sur les composants de React, il existe une multitude d'options de stylisme. Cela inclut le CSS traditionnel, l'approche utility-first, les solutions CSS-in-JS, et plus encore.

Dans cet article, nous explorerons diverses façons de styliser les composants React. Nous plongerons dans les meilleures pratiques pour un design réactif et accessible, et examinerons les considérations de performance pour vous guider dans le choix de l'approche de stylisme la plus efficace pour vos projets.

## Comment styliser les composants React avec le stylisme en ligne

Chaque élément JSX possède une propriété `style` que vous pouvez ajouter à sa balise d'ouverture. Cela signifie que vous pouvez ajouter un stylisme en ligne à JSX dans un composant React comme dans le HTML traditionnel.

La principale différence est que vous devez spécifier les styles en ligne sous forme d'objets. Dans cet objet, les clés sont les propriétés CSS écrites en _camelCase_, et les valeurs sont des chaînes correspondant à des valeurs CSS valides.

Et parce que les styles doivent être un objet, vous devez les ajouter à l'intérieur de deux accolades si vous les passez directement à l'élément :

```jsx
<h1 style={{ textAlign: 'center', marginTop: '2rem', color: '#F43596' }}>
  Bonjour
</h1>
```

Vous pouvez définir les mêmes styles en tant qu'objet séparé et les passer dans la propriété `style` :

```jsx
export default function Home() {
  const myStyles = {
   	textAlign: 'center',
   	marginTop: '2rem',
  	color: '#F43596',
  };

  return (
  	<main>
  	  <h1 style={myStyles}>Bonjour</h1>
   	</main>
  );
}

```

Si vous souhaitez gérer le CSS conditionnel avec le stylisme en ligne dans React, vous pouvez utiliser une combinaison du hook `useState` et de l'opérateur ternaire :

```jsx
'use client';

import { useState } from 'react';

const ConditionalInlineStyling = () => {
 const [isActive, setIsActive] = useState(false);

 const buttonStyle = {
   margin: '0 auto',
   backgroundColor: isActive ? 'green' : 'gray',
   cursor: isActive ? 'pointer' : 'not-allowed',
   color: 'white',
   padding: '0.6rem 1.2rem',
   border: 'none',
 };

 return (
   <div style={{ textAlign: 'center', marginTop: '2rem' }}>
     <button style={buttonStyle}>
       {isActive ? 'Active' : 'Inactive'}
     </button>
   </div>
 );
};

export default ConditionalInlineStyling;
```

![Image](https://www.freecodecamp.org/news/content/images/2024/05/conditional-inline-styling.png)
_Stylisme en ligne conditionnel dans React_

L'avantage de l'utilisation du stylisme en ligne est qu'il est rapide et limité à un élément, tandis que l'inconvénient est qu'il est limité en fonctionnalités, car vous ne pouvez pas gérer directement les pseudo-classes et les pseudo-éléments.

## Comment utiliser les feuilles de style CSS dans React

L'utilisation de feuilles de style externes est une approche de stylisme courante dans React car elle est simple.

Tout ce que vous avez à faire est de créer un fichier CSS, de définir vos styles dedans, puis d'importer la feuille de style dans votre composant React.

Mais vous importez la feuille de style en utilisant le mot-clé `import` et spécifiez ensuite le chemin relatif de la feuille de style, et non avec la balise `link` comme vous le faites en HTML.

```js
import 'chemin-relatif-vers-fichier-css.css'
```

J'ai déplacé le stylisme en ligne pour le composant `ConditionalInlineStyling` dans un fichier CSS séparé et l'ai importé dans la page comme ci-dessous :

```jsx
'use client';

import { useState } from 'react';
import '@/styles/styles.css'; // Importer le fichier CSS


const ConditionalStyledComponent = () => {
 const [isActive, setIsActive] = useState(false);

 return (
   <div className="container">
     <button
       className={`button ${isActive ? 'button-active' : 'button-inactive'}`}
     >
       {isActive ? 'Active' : 'Inactive'}
     </button>
   </div>
 );
};

export default ConditionalStyledComponent;
```

Tout fonctionne toujours bien :

![Image](https://www.freecodecamp.org/news/content/images/2024/05/conditional-inline-styling-1.png)
_Stylisme conditionnel avec un fichier CSS dans React_

L'avantage d'utiliser des feuilles de style traditionnelles pour styliser les composants React est qu'il est facile de commencer, et la seule courbe d'apprentissage est la manière dont vous l'importez dans un composant.

## Comment utiliser les modules CSS pour un stylisme spécifique aux composants

Les modules CSS offrent une solution puissante pour écrire des styles spécifiques aux composants dans React. Ils vous permettent de limiter la portée des styles aux composants individuels, vous permettant ainsi d'éviter les conflits de noms et de simplifier la maintenance des styles.

Si vous utilisez Next JS ou tout autre framework React populaire, vous n'avez pas besoin d'étapes supplémentaires pour commencer à utiliser les modules CSS.

Pour utiliser les modules CSS dans React, créez un fichier avec l'extension `.module.css`. Par exemple, `styles.module.css`. Vous devez ensuite importer le fichier dans votre composant avec le mot-clé `import` et un nom de votre choix, par exemple, `styles` ou `classes`, suivi du chemin relatif du fichier de modules CSS :

```js
import styles from 'chemin-relatif-vers-fichier-modules-css.module.css';
```

Le nom que vous choisissez est maintenant un objet, les clés sont les classes dans le fichier de modules CSS et les valeurs sont les propriétés respectives de la classe.

Pour utiliser une classe du fichier de modules CSS, vous limitez la portée du nom d'importation choisi (`style` ou `classes`) à un nom de classe. Par exemple `<div className={styles.container}>`.

J'ai déplacé tous les styles pour le composant `ConditionalInlineStyling` dans un fichier de modules CSS que j'appelle `styles.module.css`. Voici comment je l'ai importé et utilisé :

```jsx
'use client';

import { useState } from 'react';
import styles from '@/styles/styles.module.css'; // Importer le fichier de modules CSS

const ConditionalStyledComponent = () => {
 const [isActive, setIsActive] = useState(false);


 return (
   <div className={styles.container}>
     <button
       className={`${styles.button} ${
         isActive ? styles.buttonActive : styles.buttonInactive
       }`}
     >
       {isActive ? 'Active' : 'Inactive'}
     </button>
   </div>
 );
};

export default ConditionalStyledComponent;
```

## Tailwind CSS et le stylisme utility-first dans React

Tailwind CSS est un framework CSS utility-first qui accélère le stylisme directement dans votre balisage.

Tailwind le fait en offrant un ensemble complet de classes utilitaires prédéfinies. Au lieu d'écrire du CSS personnalisé et de les importer, vous appliquez les classes à vos éléments JSX ou HTML, minimisant ainsi le besoin de CSS personnalisé.

Vous pouvez ajouter Tailwind CSS à un projet Next JS en sélectionnant Tailwind dans les invites après avoir exécuté `npx create-next-app@latest` et tout sera configuré pour vous.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Screenshot-2024-05-22-at-09.39.45.png)
_Outil CLI `create-next-app` demandant d'activer Tailwind CSS_

Ou vous pouvez ajouter Tailwind à un projet existant en exécutant les commandes ci-dessous :

```bash
$ npm install tailwindcss
$ npx tailwindcss init
```

Vous devrez ensuite faire la configuration vous-même, selon vos besoins. Après cela, assurez-vous d'avoir les directives suivantes dans votre fichier `globals.css` :

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

J'ai réécrit le composant `ConditionalInlineStyling` pour vous montrer à quoi ressemble l'utilisation de Tailwind CSS :

```jsx
'use client';

import { useState } from 'react';

const ConditionalStyledComponent = () => {
 const [isActive, setIsActive] = useState(true);

 return (
   <div className="text-center mt-8">
     <button
       className={`px-4 py-2 ${
         isActive
           ? 'bg-green-600 text-white cursor-pointer'
           : 'bg-gray-500 text-white cursor-not-allowed'
       }`}
     >
       {isActive ? 'Active' : 'Inactive'}
     </button>
   </div>
 );
};

export default ConditionalStyledComponent;
```

![Image](https://www.freecodecamp.org/news/content/images/2024/05/active-inactive-with-tailwind.png)
_Stylisme conditionnel avec Tailwind CSS dans React_

Tailwind CSS est génial car il n'a pas une courbe d'apprentissage raide et est la meilleure option pour le prototypage rapide. D'autres frameworks utility-first sont Bootstrap, Bulma et Chakra UI.

## Comment styliser les applications React avec CSS-in-JS

CSS-in-JS est une approche de stylisme dans laquelle le CSS est écrit en JavaScript, vous permettant de styliser vos composants en utilisant la syntaxe JavaScript.

Cette méthode offre une manière plus dynamique et modulaire de gérer les styles, facilitant la gestion des thèmes, des styles limités en portée, ainsi que des pseudo-classes et des pseudo-éléments.

styled-components est la bibliothèque CSS-in-JS la plus populaire. D'autres sont Emotion et styled-jss.

Pour utiliser styled-components, vous devez d'abord l'ajouter à votre projet en l'installant avec NPM ou tout autre gestionnaire de paquets :

```bash
npm install styled-components
```

Vous devez ensuite importer `styled` depuis `styled-components` :

```jsx
import styled from 'styled-components'
```

Pour définir des styles pour un élément ou un composant entier, vous devez définir un composant et l'assigner à `styled.element-name`, puis définir les styles que vous souhaitez à l'intérieur des backticks.

Par exemple, la syntaxe ci-dessous créera des styles pour un composant `Button` que vous pouvez utiliser directement :

```jsx
const Button = styled.button `
  /* Les styles CSS vont ici */
`;
```

Voici comment j'ai réécrit le composant pour utiliser styled-components :

```jsx
'use client';

import { useState } from 'react';
import styled from 'styled-components';

const Button = styled.button`
 background-color: ${(props) => (props.isActive ? 'green' : 'gray')};
 color: white;
 padding: 0.6rem 1.2rem;
 border: none;
 cursor: ${(props) => (props.isActive ? 'pointer' : 'not-allowed')};
 transition: background-color 0.3s;
`;

const Container = styled.div`
 display: flex;
 justify-content: center;
 align-items: center;
`;


const ConditionalStyledComponent = () => {
 const [isActive, setIsActive] = useState(false);

 return (
   <Container>
     <Button isActive={isActive}>
       {isActive ? 'Active' : 'Inactive'}
     </Button>
   </Container>
 );
};

export default ConditionalStyledComponent;
```

Pour utiliser les pseudo-classes avec styled-components, utilisez le signe `&` pour représenter le composant actuel, puis spécifiez la pseudo-classe, par exemple, `:hover`.

Voici comment je l'ai fait :

```jsx
'use client';

import styled from 'styled-components';

const Button = styled.button`
 background-color: green;
 color: white;
 padding: 0.6rem 1.2rem;
 border: none;
 transition: background-color 0.3s;


 &:hover {
   background-color: crimson;
   cursor: pointer;
 }
`;

const Container = styled.div`
 display: flex;
 justify-content: center;
 align-items: center;
 margin-top: 2rem;
`;

const Hover = () => {
 return (
   <Container>
     <Button>Survolez-moi</Button>
   </Container>
 );
};

export default Hover;
```

![Image](https://www.freecodecamp.org/news/content/images/2024/05/hover-with-styled-components.gif)
_Animation de survol utilisant styled-components_

## Bonnes pratiques pour un design réactif et accessible

### Utilisez des unités réactives partout où nécessaire

L'utilisation d'unités réactives comme les pourcentages (`%`), `em`, `rem`, et les unités de viewport (`vw` et `vh`) au lieu d'unités fixes comme px aide votre mise en page à s'adapter de manière fluide à différentes tailles d'écran.

**Les valeurs en pourcentage** permettent aux éléments de s'adapter proportionnellement à leur conteneur, facilitant ainsi la création de mises en page fluides.

**Les unités comme `em` et `rem`** sont basées sur la taille de la police, garantissant que les éléments s'adaptent proportionnellement à la taille du texte. Cela est particulièrement utile pour la typographie réactive, où les unités relatives permettent au texte de s'adapter en fonction des paramètres et préférences de l'utilisateur.

**Les unités de viewport (`vw` et `vh`)** sont relatives à la taille de la fenêtre d'affichage, ce qui les rend idéales pour créer des éléments qui s'adaptent à la fenêtre du navigateur.

### Utilisez les Media Queries pour un design réactif

Les Media Queries sont fondamentales pour le design réactif, car elles vous permettent d'appliquer différents styles en fonction de la taille de l'écran de l'appareil.

En utilisant les Media Queries, vous pouvez créer des points de rupture à des largeurs et hauteurs d'écran spécifiques pour ajuster votre mise en page, les tailles de police et d'autres styles.

Comme le CSS traditionnel, les bibliothèques CSS-in-JS comme styled-components et Emotion supportent les Media Queries dans leur syntaxe, vous permettant de définir des styles réactifs directement dans vos fichiers JavaScript.

### Profitez de Flexbox et Grid

Les algorithmes CSS Grid et Flexbox ont révolutionné le design réactif. Si vous ne les utilisez pas, vous passez à côté d'une fonctionnalité CSS géniale.

**CSS Grid** vous permet de créer des mises en page complexes basées sur des grilles qui s'ajustent automatiquement à différentes tailles d'écran. Cela facilite la définition des zones de votre mise en page qui doivent s'expander ou se contracter.

**Flexbox** fournit un modèle de boîte flexible qui peut réorganiser et redimensionner les éléments dynamiquement.

Avec CSS Grid et Flexbox, vous pouvez créer des barres de navigation réactives, des mises en page de formulaires et d'autres composants UI qui s'ajustent élégamment lorsque l'utilisateur redimensionne l'écran.

### Utilisez un contraste de couleur suffisant pour la lisibilité et l'accessibilité

Le contraste de couleur entre le texte et l'arrière-plan est vital pour la lisibilité et l'accessibilité. Un contraste élevé améliore la lisibilité et garantit que le contenu est accessible à un public plus large.

Analyser visuellement le contraste de couleur n'est pas une tâche facile, c'est pourquoi il existe des outils comme le [WebAIM Color Contrast Checker](https://webaim.org/resources/contrastchecker/) pour vous aider à vérifier que vos choix de couleurs répondent aux ratios de contraste nécessaires.

## Considérations de performance pour le stylisme des composants React

### Évitez les styles en ligne pour les grands composants

La commodité qui vient avec l'utilisation des styles en ligne peut vous tromper en les utilisant partout.

Des styles en ligne excessifs peuvent entraîner des problèmes de performance car ils sont recalculés à chaque rendu. Cela peut potentiellement causer des reflows et des repaints inutiles.

Dans les grands composants, envisagez d'utiliser des classes CSS ou des bibliothèques CSS-in-JS qui génèrent des noms de classe statiques, qui sont plus efficaces et plus faciles à gérer pour le navigateur.

### Minimisez et optimisez les fichiers CSS

Parce que les grands fichiers CSS peuvent augmenter le temps de chargement de votre application, vous devriez envisager de minimiser votre CSS en supprimant les styles inutilisés et en compressant la taille du fichier.

Des outils comme [CSS Nano](https://cssnano.github.io/cssnano/) et [PurgeCSS](https://purgecss.com/) vous permettent de compresser et de minimiser les fichiers CSS. Ces outils suppriment les règles CSS inutiles, réduisant la taille globale et améliorant les temps de chargement. De plus, envisagez de diviser votre CSS en fichiers plus petits et spécifiques aux composants qui peuvent être chargés à la demande.

### Utilisez CSS-in-JS avec prudence

Lorsque qu'un composant est rendu, les bibliothèques CSS-in-JS génèrent et injectent des styles, ce qui peut devenir coûteux si cela est excessif. Pour réduire cela, utilisez des styles statiques chaque fois que possible et évitez une utilisation excessive de styles dynamiques qui dépendent des props ou de l'état. De plus, envisagez d'utiliser la fonction d'aide CSS ou la fonction styled de manière judicieuse pour garder les styles efficaces.

### Utilisez des sélecteurs simples et efficaces

Des sélecteurs profondément imbriqués ou des sélecteurs trop génériques peuvent ralentir le moteur de rendu du navigateur. Optez pour des sélecteurs simples et efficaces qui ciblent des éléments ou des classes spécifiques. Cette pratique réduit le temps que le navigateur passe à faire correspondre les éléments aux styles.

## Conclusion

React est agnostique quant à l'approche de stylisme que vous utilisez. C'est pourquoi il offre une gamme de méthodes de stylisme pour divers besoins. Chaque approche offre des avantages uniques pour créer des designs réactifs et accessibles.

Le choix de la méthode de stylisme appropriée doit correspondre aux exigences de votre projet et à vos préférences personnelles. En examinant les forces de chaque méthode, vous pouvez développer des applications performantes, maintenables et visuellement attrayantes qui servent une base d'utilisateurs diversifiée sur plusieurs appareils.

## Apprendre React et Next JS

Souhaitez-vous maîtriser React pour commencer à construire des applications réelles ? Alors rejoignez mon cours React et Next JS sur Udemy aujourd'hui ! Je vous enseignerai React avec du codage pratique en construisant un jeu 2048 passionnant à partir de zéro, complet avec des animations époustouflantes !

[![Cours intensif Next.js sur Udemy](https://assets.mateu.sh/assets/fcc-universal)](https://assets.mateu.sh/r/fcc-universal)