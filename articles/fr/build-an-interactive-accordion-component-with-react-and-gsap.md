---
title: Comment créer un composant accordéon interactif avec React et GSAP
subtitle: ''
author: David Jaja
co_authors: []
series: null
date: '2023-04-25T15:47:34.000Z'
originalURL: https://freecodecamp.org/news/build-an-interactive-accordion-component-with-react-and-gsap
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/Cover-image-1.png
tags:
- name: animation
  slug: animation
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: Comment créer un composant accordéon interactif avec React et GSAP
seo_desc: "As websites become more sophisticated and user expectations continue to\
  \ rise, web developers must search for ways to create more engaging and interactive\
  \ user interfaces. \nOne powerful tool in a developer's arsenal is the accordion\
  \ component, a versa..."
---

À mesure que les sites web deviennent plus sophistiqués et que les attentes des utilisateurs continuent de croître, les développeurs web doivent rechercher des moyens de créer des interfaces utilisateur plus engageantes et interactives. 

Un outil puissant dans l'arsenal d'un développeur est le composant accordéon, un élément polyvalent et largement utilisé que l'on trouve sur presque tous les sites web. 

Dans cet article, nous allons explorer comment créer un composant accordéon dynamique et visuellement époustouflant en utilisant React et la bibliothèque GreenSock Animation Platform (GSAP). 

En combinant la flexibilité de React avec les capacités d'animation de GSAP, nous allons créer une expérience utilisateur fluide et immersive qui laissera vos visiteurs en vouloir plus. Alors attachez vos ceintures et préparez-vous à faire progresser vos compétences en développement web !

## Prérequis

* Fondamentaux de HTML et CSS
* Fondamentaux de ES6 JavaScript
* Fondamentaux de React et des React Hooks.

## Ce que nous allons couvrir :

1. [Qu'est-ce qu'un composant accordéon ?](#heading-questce-quun-composant-accordeon)
2. [L'importance des composants accordéon dans la conception web](#heading-limportance-des-composants-accordeon-dans-la-conception-web)
3. [Un aperçu rapide de React et GSAP](#heading-un-aperçu-rapide-de-react-et-gsap)
4. [Comment configurer votre environnement de développement](#heading-comment-configurer-votre-environnement-de-developpement)
5. [Décomposition du projet](#heading-decomposition-du-projet)  
– [La section de l'interface utilisateur](#heading-la-section-de-linterface-utilisateur)  
– [La section de la fonctionnalité](#heading-la-section-de-la-fonctionnalité)  
– [La section de l'animation](#heading-la-section-de-lanimation)
6. [Conclusion](#heading-conclusion)

## Qu'est-ce qu'un composant accordéon ?

Un composant accordéon est un élément d'interface utilisateur utilisé pour présenter une liste d'éléments de manière compacte. Il se compose d'une liste verticale d'en-têtes qui développent et réduisent leur contenu correspondant lorsqu'on clique dessus. 

Ce type de composant est utile car il permet aux utilisateurs de parcourir rapidement une liste et de développer uniquement les éléments pertinents.

## L'importance des composants accordéon dans la conception web

Les composants accordéon sont devenus une partie essentielle de la conception web moderne, car ils permettent aux développeurs de sites web d'afficher de grandes quantités d'informations de manière compacte et organisée.  

Les composants accordéon sont particulièrement utiles pour les sites web riches en contenu où les utilisateurs peuvent être submergés par trop d'informations sur une seule page. 

Ils servent également à des usages tels que :

* Navigation : Les composants accordéon fournissent un moyen simple et intuitif pour les utilisateurs de naviguer à travers un site web. En organisant le contenu en sections repliables, les utilisateurs peuvent rapidement trouver ce qu'ils recherchent, sans avoir à faire défiler de longues pages.
* Économie d'espace : Les composants accordéon aident à économiser l'espace à l'écran en permettant aux concepteurs et développeurs de sites web d'afficher plusieurs sections de contenu dans un format compact. Cela est particulièrement important pour les appareils mobiles, où l'espace à l'écran est limité.
* Expérience utilisateur : Les composants accordéon peuvent aider à améliorer l'expérience utilisateur en réduisant l'encombrement et en facilitant la recherche d'informations par les utilisateurs. En gardant l'interface utilisateur propre et organisée, les utilisateurs sont moins susceptibles d'être submergés ou frustrés. De plus, la nature interactive des composants accordéon peut rendre l'expérience utilisateur plus engageante et agréable.

## Un aperçu rapide de React et GSAP

React est un framework JavaScript qui simplifie la création d'interfaces utilisateur dynamiques. Il y parvient en permettant aux développeurs de créer des composants individuels et réutilisables qui peuvent être assemblés pour former des interfaces complexes et interactives. 

Ce processus implique de décomposer l'interface en composants plus petits et plus faciles à gérer, qui peuvent être mis à jour indépendamment sans affecter l'ensemble de l'interface utilisateur.

GSAP, également connu sous le nom de GreenSock Animation Platform, est une bibliothèque JavaScript conçue pour créer des animations de haute qualité et des expériences interactives sur le web. 

Cette bibliothèque offre un ensemble complet d'outils pour produire des animations visuellement attrayantes et optimisées pour les performances. Avec GSAP, les développeurs peuvent créer des animations avec précision et avoir un contrôle complet sur le comportement de l'animation.

Lorsqu'ils sont utilisés ensemble, React et GSAP peuvent créer des interfaces utilisateur hautement interactives et visuellement époustouflantes, telles que des composants accordéon. React fournit le framework pour créer le composant accordéon, tandis que GSAP fournit les outils pour animer le composant et le rendre interactif.

## Comment configurer votre environnement de développement

Avant de pouvoir commencer à créer des composants dans une application React, vous devez configurer votre environnement de développement. Cela inclut l'installation de [Node.js](https://nodejs.org/en/download) et [npm](https://www.npmjs.com/package/download) (Node Package Manager) sur votre ordinateur.

### Comment créer un projet React

Après avoir installé Node.js et npm, vous pouvez utiliser l'outil de ligne de commande Create React App pour créer un nouveau projet React. Dans votre terminal local, exécutez la commande :

npx create-react-app react-gsap-dropdown

Ensuite, ouvrez ce dossier avec votre éditeur de code. Voici à quoi cela devrait ressembler :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/001---Initial-view-after-cra.png)
_Vue initiale après la création de l'application react_

**Note** : J'utiliserai l'[éditeur VSCode](https://code.visualstudio.com/download) pour le développement dans ce tutoriel, mais tout éditeur de texte moderne devrait suffire.

Ensuite, supprimez tous les styles de base et les fichiers inutiles de votre application.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/002---After-clearing-clutter-files.PNG)
_Après avoir supprimé les fichiers et styles inutiles_

L'étape suivante du processus de configuration consiste à installer GSAP dans votre application React. Ouvrez simplement le terminal dans votre éditeur de code et exécutez :

npm install gsap

![Image](https://www.freecodecamp.org/news/content/images/2024/04/installing-gsap.png)
_Installation de gsap_

Il ne reste plus qu'à exécuter `npm start`, ce qui lance un serveur de développement dans votre navigateur et affiche une page blanche.

## Décomposition du projet

Avant de commencer à construire votre projet, il est important de comprendre qu'il est divisé en trois parties :

* La section de l'interface utilisateur
* La section de la fonctionnalité
* La section de l'animation

### La section de l'interface utilisateur

Cette section inclut toutes les maquettes et les styles nécessaires pour rendre votre composant sur la page. Voici une étape par étape de la progression de cette section.

Tout d'abord, créez un élément parent dans votre composant App appelé `accordion__container`. Cet élément contient tous les éléments d'accordéon que vous souhaitez créer.

Ensuite, créez trois éléments enfants représentant chaque élément d'accordéon que vous rendrez extensible en fonction de l'interaction de l'utilisateur. Jusqu'à présent, votre structure de code devrait ressembler à ceci :

```html
<div className="App">
    <div className="accordion__container">
       <div className="accordion__item"></div>
       <div className="accordion__item"></div>
       <div className="accordion__item"></div>
    </div>
</div>
```

Dans chaque élément d'accordéon, imbriquez deux éléments enfants, `accordion__header` et `accordion__details`. Le `accordion__header` contiendra les informations affichées lorsque l'`accordion__item` est compact, et le `accordion__details` contiendra les informations lorsqu'il est développé.

```html
<div className="App">
    <div className="accordion__container">
       <div className="accordion__item"> 
          <div className="accordion__header"></div>
          <div className="accordion__details"></div>
       <div className="accordion__item">
          <div className="accordion__header"></div>
          <div className="accordion__details"></div>
       </div>
       <div className="accordion__item"> 
          <div className="accordion__header"></div>
          <div className="accordion__details"></div>
       </div>
    </div>
</div>
```

L'ajout de contenu aux deux éléments enfants donne le code suivant :

```html
<div className="accordion__container">
        <div className="accordion__item">
          <div className="accordion__header">
            <p className="accordion__number">01</p>
            <p className="accordion__name">The World's Tallest Building</p>
          </div>

          <div className="accordion__details">
            <ul>
              <li>
                The current tallest building in the world is the Burj Khalifa,
                located in Dubai, United Arab Emirates.
              </li>
              <li>
                It stands at a height of 828 meters (2,716 feet) tall and has
                163 floors.
              </li>
              <li>
                The building took six years to construct and was completed in
                2010.
              </li>
            </ul>
          </div>
        </div>

        <div className="accordion__item">
          <div className="accordion__header">
            <p className="accordion__number">02</p>
            <p className="accordion__name">
              Famous Inventors and Their Inventions
            </p>
          </div>
          <div className="accordion__details">
            <ul>
              <li>
                Nikola Tesla, a Serbian-American inventor, is credited with the
                invention of the AC (alternating current) electrical system.
              </li>
              <li>
                Thomas Edison, an American inventor, is credited with the
                invention of the light bulb.
              </li>
              <li>
                Alexander Graham Bell, a Scottish-born American inventor, is
                credited with the invention of the telephone.
              </li>
            </ul>
          </div>
        </div>
        <div className="accordion__item">
          <div className="accordion__header">
            <p className="accordion__number">03</p>
            <p className="accordion__name">Largest Deserts in the World</p>
          </div>
          <div className="accordion__details">
            <ul>
              <li>
                The Sahara Desert, located in Africa, is the largest hot desert
                in the world and covers an area of 9.2 million square kilometers
                (3.6 million square miles).
              </li>
              <li>
                The Antarctic Desert, located in Antarctica, is the largest cold
                desert in the world and covers an area of 14 million square
                kilometers (5.4 million square miles).
              </li>
              <li>
                The Arabian Desert, located in the Middle East, is the
                third-largest desert in the world and covers an area of 2.33
                million square kilometers (900,000 square miles).
              </li>
            </ul>
          </div>
        </div>
      </div>
```

Nous avons ajouté un élément `number` et `name` à l'élément `accordion__header`, et une liste non ordonnée avec des éléments de liste à l'élément `accordion__details`.

En regardant le composant dans votre navigateur, vous devriez voir ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/004---Initial-component-render-with-no-styling.png)
_Rendu initial du composant sans style_

Pour l'instant, votre composant ne ressemble pas à grand-chose, alors ajoutez le style ci-dessous.

```css

@import url("https://fonts.googleapis.com/css2?family=Dongle:wght@300;400&display=swap");

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
body {
  font-family: "Dongle", sans-serif;
}
.App {
  min-height: 100vh;
  display: flex;
  justify-content: center;
}
.accordion__container {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-top: 25px;
}
.accordion__item {
  display: flex;
  flex-direction: column;
  width: 750px;
  box-shadow: 0 0 32px rgba(0, 0, 0, 0.1);
  border-top: 4px solid transparent;
}
.accordion__header {
  display: flex;
  gap: 2rem;
  align-items: center;
  cursor: pointer;
  padding: 1rem 2rem;
}
.accordion__header:hover {
  background: #e7eaed;
}
.accordion__number {
  font-size: 40px;
  color: #ced4da;
}
.accordion__name {
  flex: 1;
  font-size: 40px;
}
.accordion__details {
  padding: 0 2rem;
}
.accordion__details ul {
  font-size: 30px;
  padding: 1rem 2rem;
  list-style-type: circle;
}
```

Ce style donne au `accordion__container` une largeur fixe et utilise certaines techniques Flexbox ainsi que du CSS de base pour donner au composant une apparence plus agréable.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/005---Component-with-stylings-applied-1.png)
_Composant rendu avec le style ajouté_

Comme vous pouvez le voir, votre composant est déjà bien disposé et plus attrayant pour les utilisateurs. Mais tous les détails de chaque élément d'accordéon sont visibles sans aucune interaction humaine. 

Pour résoudre ce problème, vous allez vouloir masquer tout le contenu dans chaque conteneur `accordion__details` en réduisant sa hauteur et en masquant tout débordement.

```css
.accordion__details {
  overflow: hidden;
  height: 0;
}
```

Ce code produit le résultat suivant :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/006--Component-after-hiding-details.PNG)
_Composant après avoir masqué les détails_

Avec cela, vous avez conclu la section de l'interface et pouvez maintenant passer à la révélation dynamique du contenu de tout élément d'accordéon sur lequel vous cliquez.

### La section de la fonctionnalité

Dans cette section, nous allons aborder les points suivants :

* Afficher dynamiquement les détails de chaque accordéon en fonction du clic de l'utilisateur.
* Assurer qu'un seul onglet d'accordéon est ouvert à la fois

Pour commencer, créez une classe `open` qui contiendra les styles que seul l'accordéon actuellement cliqué aura. Cette classe sera ajoutée à tout élément d'accordéon sur lequel vous cliquez.

```css
.open {
  border-color: #087f5b;
}

.open .accordion__header,
.open .accordion__number {
  color: #087f5b;
}

.open .accordion__details {
  height: auto;
}
```

Ensuite, vous allez créer une variable avec le hook `useState`. Ce hook est utilisé pour contenir l'état actuel d'un élément d'accordéon (c'est-à-dire s'il est ouvert ou non).

```js
const [openAccordion, setOpenAccordion] = useState(null);
```

Après cela, créez une fonction de rappel qui prend une valeur d'index distincte de chaque `accordion__item` et la compare avec la valeur dans votre variable d'état (`openAccordion`). La façon dont la fonction fonctionne est la suivante : si la valeur d'index est distincte de la valeur `openAccordion`, la fonction définit la valeur `openAccordion` sur la valeur d'index, sinon elle définit `openAccordion` sur null.

```js
 const handleAccordionClick = (index) => {
    if (index !== openAccordion) {
        setOpenAccordion(index);
     } else {
       setOpenAccordion(null);
    }
  };
```

Cette logique est utilisée pour rendre conditionnellement une classe dans votre balisage (c'est-à-dire ajouter ou supprimer une classe en fonction de l'élément sur lequel vous cliquez). Pour faire fonctionner cette fonction, vous utilisez un événement `onClick` sur chaque `accordion__header`, et appelez chaque `handleAccordionClick` avec une valeur d'`index` distincte.

```js
<div className="accordion__container">
        <div className="accordion__item">
          <div
            className="accordion__header"
             // ICI
            onClick={() => handleAccordionClick(0)}
          >
            <p className="accordion__number">01</p>
            <p className="accordion__name">The World's Tallest Building</p>
          </div>

          <div className="accordion__details">
            <ul>
              <li>
                The current tallest building in the world is the Burj Khalifa,
                located in Dubai, United Arab Emirates.
              </li>
              <li>
                It stands at a height of 828 meters (2,716 feet) tall and has
                163 floors.
              </li>
              <li>
                The building took six years to construct and was completed in
                2010.
              </li>
            </ul>
          </div>
        </div>

        <div className="accordion__item">
          <div
            className="accordion__header"
             // ICI
            onClick={() => handleAccordionClick(1)}
          >
            <p className="accordion__number">02</p>
            <p className="accordion__name">
              Famous Inventors and Their Inventions
            </p>
          </div>
          <div className="accordion__details">
            <ul>
              <li>
                Nikola Tesla, a Serbian-American inventor, is credited with the
                invention of the AC (alternating current) electrical system.
              </li>
              <li>
                Thomas Edison, an American inventor, is credited with the
                invention of the light bulb.
              </li>
              <li>
                Alexander Graham Bell, a Scottish-born American inventor, is
                credited with the invention of the telephone.
              </li>
            </ul>
          </div>
        </div>
        <div className="accordion__item">
          <div
            className="accordion__header"
            // ICI
            onClick={() => handleAccordionClick(2)}
          >
            <p className="accordion__number">03</p>
            <p className="accordion__name">Largest Deserts in the World</p>
          </div>
          <div className="accordion__details">
            <ul>
              <li>
                The Sahara Desert, located in Africa, is the largest hot desert
                in the world and covers an area of 9.2 million square kilometers
                (3.6 million square miles).
              </li>
              <li>
                The Antarctic Desert, located in Antarctica, is the largest cold
                desert in the world and covers an area of 14 million square
                kilometers (5.4 million square miles).
              </li>
              <li>
                The Arabian Desert, located in the Middle East, is the
                third-largest desert in the world and covers an area of 2.33
                million square kilometers (900,000 square miles).
              </li>
            </ul>
          </div>
        </div>
      </div>

```

Pour confirmer votre logique, enregistrez à la fois la valeur `openAccordion` et la valeur `index` dans la console, et cliquez sur chaque élément d'accordéon.

```js
  const handleAccordionClick = (index) => {
    console.log(openAccordion, index);
    if (index !== openAccordion) {
      setOpenAccordion(index);
    } else {
      setOpenAccordion(null);
    }
  };
```

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Testing-for-switching-logic.gif)
_Test de la logique de l'accordéon_

Comme vous pouvez le voir, cliquer sur le premier élément enregistre la valeur actuelle de `openAccordion` (null) et l'index actuel (0) dans la console. Il définit également la valeur de `openAccordion` sur l'index actuel.

Lorsque vous cliquez sur l'élément suivant, vous remarquez que la valeur `openAccordion` a été définie sur l'index précédent, ce qui implique que la valeur de `openAccordion` a été modifiée conditionnellement en fonction du clic de l'utilisateur.

Enfin, cliquer deux fois sur le même élément définit d'abord `openAccordion` sur l'index de cet élément, puis sur `null` puisque le bloc else de la fonction est déclenché lorsque `openAccordion === index`.

Pour afficher le contenu de chaque `accordion__item`, utilisez un opérateur ternaire pour ajouter conditionnellement la classe open à chaque élément.

```js
<div className="App">

      <div className="accordion__container">
        <div
        // ICI
          className={`accordion__item  ${openAccordion === 0 ? "open" : ""}`}
        >
          <div
            className="accordion__header"
            onClick={() => handleAccordionClick(0)}
          >
            <p className="accordion__number">01</p>
            <p className="accordion__name">The World's Tallest Building</p>
          </div>

          <div className="accordion__details">
            <ul>
              <li>
                The current tallest building in the world is the Burj Khalifa,
                located in Dubai, United Arab Emirates.
              </li>
              <li>
                It stands at a height of 828 meters (2,716 feet) tall and has
                163 floors.
              </li>
              <li>
                The building took six years to construct and was completed in
                2010.
              </li>
            </ul>
          </div>
        </div>

        <div
        // ICI
          className={`accordion__item  ${openAccordion === 1 ? "open" : ""}`}
        >
          <div
            className="accordion__header"
            onClick={() => handleAccordionClick(1)}
          >
            <p className="accordion__number">02</p>
            <p className="accordion__name">
              Famous Inventors and Their Inventions
            </p>
          </div>
          <div className="accordion__details">
            <ul>
              <li>
                Nikola Tesla, a Serbian-American inventor, is credited with the
                invention of the AC (alternating current) electrical system.
              </li>
              <li>
                Thomas Edison, an American inventor, is credited with the
                invention of the light bulb.
              </li>
              <li>
                Alexander Graham Bell, a Scottish-born American inventor, is
                credited with the invention of the telephone.
              </li>
            </ul>
          </div>
        </div>
        <div
        // ICI
          className={`accordion__item  ${openAccordion === 2 ? "open" : ""}`}
        >
          <div
            className="accordion__header"
            onClick={() => handleAccordionClick(2)}
          >
            <p className="accordion__number">03</p>
            <p className="accordion__name">Largest Deserts in the World</p>
          </div>
          <div className="accordion__details">
            <ul>
              <li>
                The Sahara Desert, located in Africa, is the largest hot desert
                in the world and covers an area of 9.2 million square kilometers
                (3.6 million square miles).
              </li>
              <li>
                The Antarctic Desert, located in Antarctica, is the largest cold
                desert in the world and covers an area of 14 million square
                kilometers (5.4 million square miles).
              </li>
              <li>
                The Arabian Desert, located in the Middle East, is the
                third-largest desert in the world and covers an area of 2.33
                million square kilometers (900,000 square miles).
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>


```

L'opérateur ternaire vérifie si chaque valeur d'`index` correspond à la valeur `openAccordion` et ajoute la classe `open` à l'`accordion__item` si c'est le cas.

Tester votre composant accordéon donne maintenant le résultat suivant :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Accordion-Working-without-animation-1.gif)
_Accordéon fonctionnel sans animation_

Comme vous pouvez le voir, votre accordéon est déjà entièrement fonctionnel. Grâce à la logique que vous avez implémentée avec l'opérateur ternaire, un seul élément d'accordéon peut être ouvert à la fois. Félicitations !

Hélas, votre composant est un peu ennuyeux, n'est-ce pas ? Il ressemble probablement à tous les autres accordéons que vous avez vus. Alors, épicez le vôtre et faites-en le sujet de discussion de la communauté tech en l'animant 😉.

### La section de l'animation

Pour l'instant, lorsque vous basculez la classe `open`, l'élément `accordion__details` passe de l'affichage d'aucun contenu au contenu complet en une fraction de seconde sans aucune animation. Il le fait en alternant la valeur de la hauteur de 0 à auto. 

Pour rendre l'accordéon plus interactif, vous allez utiliser GSAP pour animer la hauteur de chaque composant accordéon lorsqu'un élément d'accordéon est cliqué.

Commencez par créer une référence de tous les éléments d'accordéon :

```js
const accordionRefs = useRef([]);
```

**Note** : Le hook `useRef` prend un tableau car vous sélectionnez plusieurs éléments. Pour cibler distinctement chaque élément, utilisez un attribut `ref` et passez chaque index individuel dans le `ref`.

```js
<div className="App">
      <div className="accordion__container">
        <div
          className={`accordion__item  ${openAccordion === 0 ? "open" : ""}`}
           // ICI
          ref={(el) => (accordionRefs.current[0] = el)}
        >
          <div
            className="accordion__header"
            onClick={() => handleAccordionClick(0)}
          >
            <p className="accordion__number">01</p>
            <p className="accordion__name">The World's Tallest Building</p>
                     </div>

          <div
            className="accordion__details"
            
          >
            <ul>
              <li>
                The current tallest building in the world is the Burj Khalifa,
                located in Dubai, United Arab Emirates.
              </li>
              <li>
                It stands at a height of 828 meters (2,716 feet) tall and has
                163 floors.
              </li>
              <li>
                The building took six years to construct and was completed in
                2010.
              </li>
            </ul>
          </div>
        </div>

        <div
          className={`accordion__item ${openAccordion === 1 ? "open" : ""}`}
           // ICI
          ref={(el) => (accordionRefs.current[1] = el)}
        >
          <div
            className="accordion__header"
            onClick={() => handleAccordionClick(1)}
          >
            <p className="accordion__number">02</p>
            <p className="accordion__name">
              Famous Inventors and Their Inventions
            </p>
                      </div>
          <div
            className="accordion__details"
            
          >
            <ul>
              <li>
                Nikola Tesla, a Serbian-American inventor, is credited with the
                invention of the AC (alternating current) electrical system.
              </li>
              <li>
                Thomas Edison, an American inventor, is credited with the
                invention of the light bulb.
              </li>
              <li>
                Alexander Graham Bell, a Scottish-born American inventor, is
                credited with the invention of the telephone.
              </li>
            </ul>
          </div>
        </div>
        <div
          className={`accordion__item ${openAccordion === 2 ? "open" : ""}`}
          // ICI
          ref={(el) => (accordionRefs.current[2] = el)}
        >
          <div
            className="accordion__header"
            onClick={() => handleAccordionClick(2)}
          >
            <p className="accordion__number">03</p>
            <p className="accordion__name">Largest Deserts in the World</p>
                      </div>
          <div
            className="accordion__details"
            
          >
            <ul>
              <li>
                The Sahara Desert, located in Africa, is the largest hot desert
                in the world and covers an area of 9.2 million square kilometers
                (3.6 million square miles).
              </li>
              <li>
                The Antarctic Desert, located in Antarctica, is the largest cold
                desert in the world and covers an area of 14 million square
                kilometers (5.4 million square miles).
              </li>
              <li>
                The Arabian Desert, located in the Middle East, is the
                third-largest desert in the world and covers an area of 2.33
                million square kilometers (900,000 square miles).
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>

```

Ensuite, modifiez la fonction `handleAccordionClick` pour ajouter des animations GSAP.

```js
if (index === openAccordion) {
      gsap.to(
        accordionRefs.current[index].querySelector(".accordion__details"),
        {
          height: 0,
          duration: 1,
          ease: "power1.inOut",
         }
      );
    }
```

Explication de l'extrait de code ci-dessus :

* L'instruction conditionnelle vérifie d'abord si l'index de l'élément d'accordéon cliqué correspond à l'état actuel de l'accordéon.
* Ensuite, nous utilisons une méthode GSAP pour ajouter des animations lorsque la condition est vraie. La méthode `gsap.to` vous permet de définir les propriétés d'animation pour un élément, puis de faire passer en douceur l'élément de son état actuel à l'état final spécifié sur une période de temps. La méthode `gsap.to` prend en compte 2 paramètres, l'élément cible et le comportement spécifié de cet élément cible.
* Nous avons utilisé un attribut de traversée du DOM (`.querySelector`) pour sélectionner l'élément avec le nom de classe `accordion__details` à l'intérieur de cet élément d'accordéon et y avons attaché une animation et un style.

**Note :** Ce bloc de code sera déclenché chaque fois qu'un élément d'accordéon particulier est cliqué deux fois, (quand `index === openAccordion`), ce qui en fait une animation de fermeture.

Ensuite, vous devez tenir compte des animations d'ouverture et de fermeture des éléments d'accordéon précédemment ouverts.

```js
else {
      if (openAccordion !== null) {
        gsap.to(
          accordionRefs.current[openAccordion].querySelector(
            ".accordion__details"
          ),
          {
            height: 0,
            duration: 1,
            ease: "power1.inOut",
          }
        );
      }
      setOpenAccordion(index);
      gsap.fromTo(
        accordionRefs.current[index].querySelector(".accordion__details"),
        { height: 0 },
        {
          height: "auto",
          duration: 1,
          ease: "power1.inOut",
        }
      );
    }
```

* Le bloc else vérifie si la valeur actuelle de l'accordéon n'est pas nulle (si un en-tête d'accordéon a déjà été cliqué) et utilise GSAP pour fermer l'accordéon précédemment ouvert en utilisant la valeur stockée dans `openAccordion` pour cibler l'élément approprié.
* Ensuite, il met à jour la valeur `openAccordion` avec l'index de l'élément actuellement cliqué. Enfin, il utilise une méthode `gsap.fromTo` pour spécifier l'animation d'ouverture d'un élément d'accordéon. La méthode `gsap.fromTo` prend une condition de départ et de fin et anime l'élément d'accordéon en conséquence (de height: 0 à height: auto).

En regardant l'accordéon maintenant, vous verrez le résultat suivant :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Final-version-with-a-bug.gif)
_Version finale avec un bug_



Et avec cela, vous avez réussi à créer un composant accordéon interactif, félicitations ! 🎉

Il y a un petit bug cependant. Si vous cliquez sur un élément d'accordéon après l'avoir ouvert et fermé, il ne s'ouvre pas. Cela est dû au fait qu'après la fermeture de l'élément d'accordéon, la valeur de `openAccordion` est toujours définie sur l'index de cet élément d'accordéon. Cela fait que le code se comporte comme s'il y avait encore un élément d'accordéon ouvert même après l'avoir fermé. 

Pour résoudre ce problème, attachez un événement `onComplete` à la fonction `handleAccordionClick` qui définit la valeur de openAccordion sur null après la fin de l'animation. De cette façon, chaque fois que vous fermez l'accordéon, la valeur de `openAccordion` est réinitialisée et l'élément d'accordéon peut être rouvert.

```js
  const handleAccordionClick = (index) => {
    if (index === openAccordion) {
      gsap.to(
        accordionRefs.current[index].querySelector(".accordion__details"),
        {
          height: 0,
          duration: 1,
          ease: "power1.inOut",
          onComplete: () => setOpenAccordion(null),
        }
      );
      console.log(openAccordion);
    } else {
      if (openAccordion !== null) {
        gsap.to(
          accordionRefs.current[openAccordion].querySelector(
            ".accordion__details"
          ),
          {
            height: 0,
            duration: 1,
            ease: "power1.inOut",
          }
        );
      }
      setOpenAccordion(index);
      gsap.fromTo(
        accordionRefs.current[index].querySelector(".accordion__details"),
        { height: 0 },
        {
          height: "auto",
          duration: 1,
          ease: "power1.inOut",
        }
      );
    }
  };
```

Et avec cela, regardons le résultat final :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Final-bug-free-version-1.gif)
_Version finale sans bug_

Pour faciliter l'accessibilité, voici le code final complet :

```js
import { useRef, useState } from "react";
import "./App.css";
import { gsap } from "gsap";
function App() {
  const [openAccordion, setOpenAccordion] = useState(null);
  const accordionRefs = useRef([]);

  const handleAccordionClick = (index) => {
    if (index === openAccordion) {
      gsap.to(
        accordionRefs.current[index].querySelector(".accordion__details"),
        {
          height: 0,
          duration: 1,
          ease: "power1.inOut",
          onComplete: () => setOpenAccordion(null),
        }
      );
      // console.log(openAccordion);
    } else {
      if (openAccordion !== null) {
        gsap.to(
          accordionRefs.current[openAccordion].querySelector(
            ".accordion__details"
          ),
          {
            height: 0,
            duration: 1,
            ease: "power1.inOut",
          }
        );
      }
      setOpenAccordion(index);
      gsap.fromTo(
        accordionRefs.current[index].querySelector(".accordion__details"),
        { height: 0 },
        {
          height: "auto",
          duration: 1,
          ease: "power1.inOut",
        }
      );
    }
  };

  return (
    <div className="App">
      <div className="accordion__container">
        <div
          className={`accordion__item  ${openAccordion === 0 ? "open" : ""}`}
          ref={(el) => (accordionRefs.current[0] = el)}
        >
          <div
            className="accordion__header"
            onClick={() => handleAccordionClick(0)}
          >
            <p className="accordion__number">01</p>
            <p className="accordion__name">The World's Tallest Building</p>
          </div>

          <div className="accordion__details">
            <ul>
              <li>
                The current tallest building in the world is the Burj Khalifa,
                located in Dubai, United Arab Emirates.
              </li>
              <li>
                It stands at a height of 828 meters (2,716 feet) tall and has
                163 floors.
              </li>
              <li>
                The building took six years to construct and was completed in
                2010.
              </li>
            </ul>
          </div>
        </div>

        <div
          className={`accordion__item ${openAccordion === 1 ? "open" : ""}`}
          ref={(el) => (accordionRefs.current[1] = el)}
        >
          <div
            className="accordion__header"
            onClick={() => handleAccordionClick(1)}
          >
            <p className="accordion__number">02</p>
            <p className="accordion__name">
              Famous Inventors and Their Inventions
            </p>
          </div>
          <div className="accordion__details">
            <ul>
              <li>
                Nikola Tesla, a Serbian-American inventor, is credited with the
                invention of the AC (alternating current) electrical system.
              </li>
              <li>
                Thomas Edison, an American inventor, is credited with the
                invention of the light bulb.
              </li>
              <li>
                Alexander Graham Bell, a Scottish-born American inventor, is
                credited with the invention of the telephone.
              </li>
            </ul>
          </div>
        </div>
        <div
          className={`accordion__item ${openAccordion === 2 ? "open" : ""}`}
          ref={(el) => (accordionRefs.current[2] = el)}
        >
          <div
            className="accordion__header"
            onClick={() => handleAccordionClick(2)}
          >
            <p className="accordion__number">03</p>
            <p className="accordion__name">Largest Deserts in the World</p>
          </div>
          <div className="accordion__details">
            <ul>
              <li>
                The Sahara Desert, located in Africa, is the largest hot desert
                in the world and covers an area of 9.2 million square kilometers
                (3.6 million square miles).
              </li>
              <li>
                The Antarctic Desert, located in Antarctica, is the largest cold
                desert in the world and covers an area of 14 million square
                kilometers (5.4 million square miles).
              </li>
              <li>
                The Arabian Desert, located in the Middle East, is the
                third-largest desert in the world and covers an area of 2.33
                million square kilometers (900,000 square miles).
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
}
export default App;
```

Voici un lien vers le dépôt : [Github](https://github.com/Daiveedjay/React-Gsap-Accordion)

Et la version live : [Démo Live](https://react-gsap-accordion.netlify.app)

En bonus, j'ai préparé un fichier JSON dans le dépôt contenant toutes les informations remplies dans le composant accordéon pour mieux vous aider à écrire un code plus propre et réutilisable.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/007-Json-file.png)
_Fichier JSON_

## Conclusion

Dans ce tutoriel, vous avez appris à créer un composant accordéon en utilisant React et GSAP qui est non seulement fonctionnel mais aussi super cool ! 

Maintenant, vous pouvez impressionner vos amis et collègues avec vos compétences en création d'accordéons, et qui sait – peut-être allez-vous lancer une nouvelle tendance de sites web à thème accordéon :) N'oubliez pas d'utiliser vos pouvoirs pour le bien et non pour le mal, et accordez-vous toujours de manière responsable.

### Informations de contact

Vous voulez me contacter ou me connecter ? N'hésitez pas à me contacter sur les plateformes suivantes :

* Twitter : [@jajadavid8](https://twitter.com/JajaDavid8)
* LinkedIn : [David Jaja](https://www.linkedin.com/in/david-jaja-8084251b4/)
* Email : Jajadavidjid@gmail.com