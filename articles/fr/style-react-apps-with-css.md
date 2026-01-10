---
title: Comment styliser vos applications React avec CSS comme un pro
subtitle: ''
author: valentine Gatwiri
co_authors: []
series: null
date: '2023-01-18T20:55:27.000Z'
originalURL: https://freecodecamp.org/news/style-react-apps-with-css
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/pexels-tyler-hendy-52062.jpg
tags:
- name: CSS
  slug: css
- name: React
  slug: react
seo_title: Comment styliser vos applications React avec CSS comme un pro
seo_desc: "React is a JavaScript library for building user interfaces. And it's gained\
  \ a lot of popularity in the front-end development community. \nOne of the benefits\
  \ of using React is its integration with CSS, which allows developers to apply styles\
  \ to their ..."
---

React est une bibliothèque JavaScript pour construire des interfaces utilisateur. Et elle a gagné beaucoup de popularité dans la communauté de développement front-end. 

L'un des avantages de l'utilisation de React est son intégration avec CSS, qui permet aux développeurs d'appliquer des styles à leurs composants de manière modulaire et réutilisable. 

Dans ce tutoriel, vous apprendrez comment intégrer React avec CSS comme un pro en comprenant les différentes façons d'appliquer des styles à vos composants. Vous apprendrez également quelques bonnes pratiques pour organiser et maintenir votre code CSS. 

À la fin de ce tutoriel, vous devriez être capable de styliser vos composants React en toute confiance et de construire des interfaces utilisateur visuellement attrayantes.

### **Ce que vous allez apprendre**

Voici quelques choses que vous allez apprendre :

* Comment appliquer des styles CSS de base aux composants React
* Comment utiliser les modules CSS pour appliquer des styles avec portée aux composants
* Comment utiliser les bibliothèques CSS-in-JS comme styled-components pour styliser vos composants
* Comment appliquer des styles réactifs à vos composants en utilisant les requêtes média et d'autres techniques de design réactif
* Comment utiliser les animations et transitions CSS pour ajouter des effets visuels dynamiques à vos composants
* Bonnes pratiques pour organiser et maintenir votre CSS lors de la travail sur une grande application React.

## Comment intégrer React avec CSS

Il existe plusieurs façons d'intégrer React avec CSS. Voici quelques approches que vous pourriez trouver utiles :

### Utilisation des styles en ligne

Vous pouvez utiliser l'attribut `style` dans vos composants React pour spécifier des styles en ligne. Cela peut être pratique si vous avez seulement besoin d'appliquer quelques styles à un seul élément.

```jsx
import React from 'react';

function MyComponent() {
  return (
    <div style={{color: 'red', fontSize: '32px'}}>
      Ce texte est rouge et de 32px
    </div>
  );
}
```

Ceci est un composant fonctionnel dans React qui retourne un seul élément div avec un style en ligne. Le style en ligne définit la couleur du texte en rouge et la taille de la police à 32px. Lorsque ce composant est rendu dans une application React, il affichera un texte rouge avec une taille de police de 32px [comme vous pouvez le voir dans ce CodePen](https://codepen.io/gatwirival/pen/JjBbqme).

### Utilisation d'un fichier CSS

Vous pouvez créer un fichier CSS et l'importer dans vos composants React. Cela est utile si vous avez un ensemble de styles que vous souhaitez réutiliser dans plusieurs composants.

```css
/* my-styles.css */
.red-text {
  color: red;
}

.large-text {
  font-size: 32px;
}
```

Ceci est un fichier CSS qui contient deux sélecteurs de classe, `.red-text` et `.large-text`, qui peuvent être utilisés pour appliquer les styles correspondants aux éléments. La classe `.red-text` définit la couleur du texte en rouge et la classe `.large-text` définit la taille de la police à 32px.

Pour utiliser ces classes dans JSX, vous devez importer le fichier de feuille de style dans le fichier du composant, puis ajouter le className aux éléments JSX :

```jsx
import React from 'react';
import './my-styles.css';

function MyComponent() {
  return (
    <div className="red-text large-text">
      Ce texte est rouge et de 32px
    </div>
  );
}
```

[Voir le code sur Codepen](https://codepen.io/gatwirival/pen/oNMePNQ).

### Utilisation d'un préprocesseur CSS

Vous pouvez utiliser un préprocesseur CSS (tel que SASS ou LESS) pour écrire et organiser vos styles. Cela peut être pratique si vous souhaitez utiliser des fonctionnalités comme les variables, les mixins et les sélecteurs imbriqués dans vos styles.

```css
/* my-styles.scss */
$red: red;

.red-text {
  color: $red;
}

.large-text {
  font-size: 32px;
}
```

Ceci est un fichier SCSS (Sass) qui utilise des variables pour stocker des valeurs de couleur, qui peuvent être réutilisées dans toute la feuille de style. La variable `$red` est définie sur la valeur `red`, et est ensuite utilisée pour définir la couleur du texte de la classe `.red-text`. De plus, la classe `.large-text` définit la taille de la police à 32px.

```jsx
import React from 'react';
import './my-styles.scss';

function MyComponent() {
  return (
    <div className="red-text large-text">
      Ce texte est rouge et de 32px
    </div>
  );
}
```

Ceci est un composant fonctionnel React qui importe le fichier `my-styles.scss` et utilise les sélecteurs de classe définis dans ce fichier pour styliser les éléments dans le JSX. L'instruction `import` en haut du fichier est utilisée pour importer le fichier `my-styles.scss` dans le composant, permettant au composant d'utiliser les classes CSS définies dans ce fichier.

Le JSX dans la fonction `MyComponent` retourne un seul élément `div` avec le className `red-text large-text`. Cela signifie que l'élément div aura les deux styles de classe `.red-text` et `.large-text` qui ont été définis dans le fichier `my-styles.scss`, ce qui donne un texte rouge et de 32px à l'intérieur de la div.

Lorsque ce composant est rendu par une application React, il affichera un texte rouge avec une taille de police de 32px. Vous pouvez voir le code fonctionnel [ici](https://codepen.io/gatwirival/pen/bGjrxBw).

### Utilisation d'une bibliothèque CSS-in-JS

Il existe également plusieurs bibliothèques qui vous permettent d'écrire vos styles en JavaScript et de les appliquer à vos composants. 

Cela peut être pratique si vous souhaitez générer des styles dynamiquement ou tirer parti de fonctionnalités comme le thème. Certaines bibliothèques CSS-in-JS populaires incluent styled-components et emotion.

```jsx
import React from 'react';
import styled from 'styled-components';

const RedText = styled.div`
  color: red;
  font-size: 32px;
`;

function MyComponent() {
  return (
    <RedText>
      Ce texte est rouge et de 32px
    </RedText>
  );
}

```

Ceci est un composant fonctionnel React qui utilise la bibliothèque "styled-components" pour styliser ses éléments JSX. La bibliothèque `styled-components` vous permet d'écrire du code CSS réel pour styliser vos composants, de manière à ce qu'il soit limité au composant. Elle vous permet également d'utiliser des expressions JavaScript dans votre CSS.

Ici, le composant importe l'objet `styled` de la bibliothèque `styled-components` et crée un nouveau composant appelé `RedText` qui rend un élément `div` avec les styles définis à l'intérieur des backticks. Les styles définis à l'intérieur des backticks incluent la définition de la couleur du texte en rouge et de la taille de la police à 32px.

Ensuite, le composant retourne du JSX qui utilise le composant `RedText`, qui rend une div avec les styles définis.

Lorsque ce composant est rendu par une application React, il affichera un texte rouge avec une taille de police de 32px.

Cette méthode de stylisation vous permet de créer des composants réutilisables et autonomes, avec leurs propres styles, qui sont faciles à gérer et à tester.

## Comment utiliser les animations et transitions CSS pour ajouter des effets visuels dynamiques à vos composants

Pour utiliser les animations et transitions CSS dans un composant React, vous devrez utiliser un objet de style ou une feuille de style externe pour définir les styles de votre composant.

Voici un exemple d'utilisation d'un objet de style pour définir une simple animation CSS qui fait apparaître un élément lorsqu'il est monté :

```jsx
import React, { useEffect } from 'react';

function FadeInElement() {
  const [fadeIn, setFadeIn] = useState(false);

  useEffect(() => {
    setFadeIn(true);
  }, []);

  const fadeInStyle = {
    opacity: fadeIn ? 1 : 0,
    transition: 'opacity 500ms linear'
  };

  return <div style={fadeInStyle}>Fade In Element</div>;
}

```

Ceci est un composant fonctionnel React qui utilise les Hooks React pour créer une simple animation qui "fait apparaître" un élément à l'écran.

Le composant utilise le hook `useState` pour gérer l'état du composant, dans ce cas, il s'agit d'une valeur booléenne qui détermine si l'élément doit être visible ou non.

Le composant utilise également le hook `useEffect` pour écouter les changements dans le composant et définir l'état `fadeIn` à vrai lorsque le composant est rendu. Le useEffect prend un tableau vide comme second argument, ce qui signifie qu'il ne s'exécutera qu'une seule fois lorsque le composant est rendu pour la première fois (au montage).

Le composant définit ensuite un objet `fadeInStyle` qui utilise l'état `fadeIn` pour définir l'opacité de l'élément. Si `fadeIn` est vrai, l'élément sera complètement opaque (opacity: 1), sinon il sera complètement transparent (opacity: 0). La propriété de transition est également définie pour transitionner en douceur l'opacité sur 500ms.

Le composant retourne un élément `div` avec l'objet `fadeInStyle` comme style en ligne. Lorsque ce composant est rendu par une application React, il affichera le texte "Fade In Element" qui apparaît en douceur sur une période de 500ms. Vous pouvez voir le code fonctionnel [ici](https://codepen.io/gatwirival/pen/KKBvxWq).

Vous pouvez également utiliser la prop `className` et une feuille de style externe pour définir vos styles. Voici un exemple d'utilisation d'une feuille de style externe pour définir une simple transition CSS qui change la couleur d'un élément lorsqu'il est survolé :

```jsx
import React from 'react';
import './FadeInElement.css';

function FadeInElement() {
  return <div className="fade-in-element">Survolez-moi</div>;
}
```

```css
.fade-in-element {
  transition: color 500ms linear;
}

.fade-in-element:hover {
  color: blue;
}

```

Vous pouvez également utiliser la règle `@keyframes` pour définir des animations plus complexes. Par exemple :

```css
@keyframes pulse {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.1);
  }
  100% {
    transform: scale(1);
  }
}

.pulse {
  animation: pulse 500ms linear;
}
```

Vous pouvez ensuite appliquer l'animation `pulse` à un élément en utilisant la prop `className` :

```jsx
import React from 'react';
import './PulseElement.css';

function PulseElement() {
  return <div className="pulse">Pulse</div>;
}
```

## Bonnes pratiques pour organiser et maintenir votre CSS dans une grande application React

### Utiliser une bibliothèque CSS-in-JS 

Les bibliothèques CSS-in-JS comme styled-components et emotion vous permettent d'écrire vos styles en JavaScript et de les limiter automatiquement à vos composants comme montré ci-dessus. Cela peut aider à prévenir les conflits de noms et faciliter la gestion de vos styles.

### Utiliser une convention de nommage 

Il est bon d'utiliser une convention de nommage cohérente pour vos classes CSS afin de garder vos styles organisés et faciles à comprendre. Certaines conventions populaires incluent BEM (Block-Element-Modifier) et SMACSS (Scalable and Modular Architecture for CSS).

Voici un exemple de la façon dont ces conventions pourraient être utilisées ensemble dans un composant React :

```jsx
import React from 'react';
import './ProfileInfo.css';

function ProfileInfo(props) {
  return (
    <div className="profile-info">
      <h2>{props.name}</h2>
      <p>{props.bio}</p>
    </div>
  );
}

export default ProfileInfo;

```

Et le CSS correspondant :

```css
.profile-info {
  background-color: #f5f5f5;
  padding: 20px;
}
```

Dans ce code, les conventions de nommage suivantes sont utilisées :

* Le composant fonctionnel React est nommé "ProfileInfo", qui suit la convention UpperCamelCase ou PascalCase pour nommer les composants React.
* Le fichier CSS importé est nommé "ProfileInfo.css", qui suit également la convention UpperCamelCase et correspond au nom du composant.
* La classe dans le template JSX est "profile-info", qui suit la convention en minuscules et séparée par des tirets, également connue sous le nom de kebab-case, pour nommer les classes CSS.

Vous pouvez [lire plus sur les conventions de nommage ici](https://www.freecodecamp.org/news/snake-case-vs-camel-case-vs-pascal-case-vs-kebab-case-whats-the-difference/) si vous le souhaitez.

### Utiliser un linter

Un linter est un outil qui vérifie votre code pour les erreurs de style et de syntaxe. Il existe des linters disponibles pour CSS qui peuvent vous aider à garder vos styles cohérents et sans erreur.

Il existe plusieurs linters disponibles pour le linting du code CSS, tels que CSSLint, Stylelint et ESLint.

Pour utiliser un linter en CSS, vous devrez d'abord l'installer. Par exemple, pour installer CSSLint, vous pouvez utiliser npm en exécutant la commande suivante :

```bash
npm list -g csslint
```

Une fois le linter installé, vous pouvez l'utiliser pour linter votre code CSS en exécutant le linter et en passant le ou les fichiers que vous souhaitez linter en tant qu'arguments. 

Par exemple, pour linter un fichier appelé "styles.css" en utilisant CSSLint, vous devrez changer votre répertoire vers le dossier avec le fichier CSS puis exécuter la commande suivante :

```bash
csslint styles.css
```

Après avoir exécuté la commande ci-dessus, vous verrez la sortie suivante selon les erreurs dans votre code :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot-from-2023-01-18-21-14-00.png)

Vous pouvez également configurer le linter pour utiliser des règles et des paramètres spécifiques en créant un fichier de configuration. Le format du fichier de configuration dépend du linter que vous utilisez. Par exemple, CSSLint utilise un fichier `.csslintrc`.

Une fois que vous exécutez le linter, il sortira tous les problèmes ou avertissements qu'il trouve dans votre code CSS. Vous pouvez ensuite parcourir la sortie et corriger tous les problèmes qui ont été trouvés.

Note : Selon le linter que vous utilisez, le processus peut varier. Mais le concept de base est le même.

### Diviser vos styles en fichiers séparés

À mesure que votre projet grandit, il peut être utile de diviser vos styles en fichiers séparés, comme un fichier pour les styles de base, un pour les styles de mise en page et un pour les styles de thème. Cela peut faciliter la recherche et la maintenance de vos styles.

### Utiliser le contrôle de source

L'utilisation d'un système de contrôle de version comme Git pour suivre les changements de vos fichiers CSS peut faciliter la collaboration avec d'autres membres de l'équipe et également revenir en arrière si quelque chose ne va pas.

### Utiliser un préprocesseur CSS 

Les préprocesseurs CSS comme SASS et LESS peuvent vous aider à écrire et maintenir vos styles plus efficacement comme montré ci-dessus. Ils vous permettent d'utiliser des variables, des fonctions et d'autres fonctionnalités qui ne sont pas disponibles dans le CSS standard.

## Conclusion

L'intégration de React avec CSS peut être un outil puissant pour construire des applications web efficaces et stylées. 

En comprenant les principes du framework React et comment il interagit avec CSS, vous pouvez tirer parti des forces des deux technologies pour créer des interfaces utilisateur dynamiques et expressives. 

Que vous soyez un développeur expérimenté ou que vous débutiez avec React, apprendre à intégrer efficacement CSS peut faire passer vos compétences au niveau supérieur et vous aider à construire des applications vraiment impressionnantes.