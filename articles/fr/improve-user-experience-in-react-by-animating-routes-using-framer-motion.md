---
title: Comment améliorer l'expérience utilisateur dans les applications React – Animer
  les routes avec Framer Motion
subtitle: ''
author: David Jaja
co_authors: []
series: null
date: '2023-04-04T22:27:19.000Z'
originalURL: https://freecodecamp.org/news/improve-user-experience-in-react-by-animating-routes-using-framer-motion
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/Article-Cover.png
tags:
- name: animation
  slug: animation
- name: React
  slug: react
- name: user experience
  slug: user-experience
seo_title: Comment améliorer l'expérience utilisateur dans les applications React
  – Animer les routes avec Framer Motion
seo_desc: "In the modern digital landscape, user experience (UX) has become a central\
  \ focus of web development. Providing a smooth, captivating, and aesthetically pleasing\
  \ interface can really influence user satisfaction and retention. \nRoute animation\
  \ is a fre..."
---

Dans le paysage numérique moderne, l'expérience utilisateur (UX) est devenue un axe central du développement web. Fournir une interface fluide, captivante et esthétiquement plaisante peut vraiment influencer la satisfaction et la fidélisation des utilisateurs.

L'animation des routes est un aspect souvent sous-estimé de l'UX qui peut considérablement améliorer l'interactivité d'un site web.

Dans ce tutoriel, je vais vous guider à travers les étapes d'incorporation d'animations de routes dans les applications React en utilisant Framer Motion, une bibliothèque d'animation puissante et conviviale.

## Importance de l'animation des routes dans les applications web

Animer les routes peut rendre les transitions entre différentes pages ou sections d'un site web plus visuellement attrayantes et interactives. Les animations de routes fluides améliorent l'expérience utilisateur globale en fournissant un sentiment de continuité et de fluidité. Elles peuvent également minimiser les temps de chargement perçus et maintenir les utilisateurs engagés pendant que le nouveau contenu est récupéré ou rendu.

Si vous êtes comme moi, et que vous êtes un amateur d'animations esthétiques, vous serez d'accord pour dire que les sites web qui ont des animations et des transitions fluides, surtout entre leurs parties (routes), tendent à laisser une impression plus forte et à vous faire naviguer plus longtemps que ceux qui sont moins animés.

## Une brève introduction à React et Framer Motion

React est devenu une bibliothèque JavaScript largement utilisée pour créer des interfaces utilisateur, en particulier dans le contexte des applications à page unique (SPA). En tant que solution axée sur les SPA, React charge une seule page HTML et modifie dynamiquement le contenu en fonction de la navigation de l'utilisateur dans l'application, via des changements de route.

Framer Motion, une bibliothèque d'animation open-source conçue pour React, offre une API simple et expressive pour générer des animations complexes.

La bibliothèque dispose d'un large éventail de capacités d'animation, y compris la physique des ressorts, la gestion des gestes et le support du rendu côté serveur. Cela fait de Framer Motion un choix idéal pour implémenter des animations de routes dans les applications React.

## Comment configurer votre environnement de développement

Avant de pouvoir commencer à animer des routes dans une application React, vous devez configurer votre environnement de développement. Cela inclut l'installation de [Node.js](https://nodejs.org/en/download) et [npm](https://www.npmjs.com/package/download) (Node Package Manager) sur votre ordinateur.

### Comment créer un projet React

Une fois que vous avez installé Node.js et npm, vous pouvez créer un nouveau projet React en utilisant l'outil de ligne de commande Create React App. Exécutez la commande suivante dans votre terminal :

```
npx create-react-app react-framer-animation
```

Après cela, ouvrez ce dossier avec votre éditeur de code. Cela devrait ressembler à quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/001-Setting-up-and-opening-your-react-app.png)
_Configuration et ouverture de votre application React_

**Note** : dans ce tutoriel, j'utiliserai l'[éditeur VSCode](https://code.visualstudio.com/download) pour le développement, mais tout éditeur de texte moderne devrait suffire.

Ensuite, vous vous débarrassez de tous les styles de base et des fichiers inutiles dans votre application.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/002-Clearing-the-clutter-files.png)
_Suppression des fichiers inutiles_

Votre prochaine étape de configuration consiste à installer _framer motion_ et _react-router_ dans votre application React. Ouvrez simplement le terminal de votre éditeur de code et exécutez :

```
npm install framer-motion react-router-dom
```

![Image](https://www.freecodecamp.org/news/content/images/2023/04/003-Installing-he-necessary-dependencies.jpg)
_Installation des dépendances nécessaires_

Il ne reste plus qu'à exécuter `npm start` qui démarre un serveur de développement sur votre navigateur qui ouvre une page blanche.

## Comment fonctionne React Router

React Router est une bibliothèque largement utilisée pour gérer la navigation et le routage dans les applications React. Elle permet aux développeurs de créer des routes dynamiques et de gérer les changements de route de manière transparente (c'est-à-dire naviguer entre les pages ou les composants).

Pour vous aider à mieux comprendre, mettons en place les routes pour notre projet.

Tout d'abord, importez toutes les fonctionnalités nécessaires dans votre composant `App`

```js
import { BrowserRouter, NavLink, Route, Routes } from "react-router-dom";
```

Ensuite, créez le reste des composants que vous allez parcourir. Pour éviter les allers-retours fastidieux entre les composants, tous les composants seront créés dans le composant `App.js`.

```js
function Home() {
  return (
    <div
      className="home component"
    >
     <h1>  Home Component </h1>
    </div>
  );
}

function Header() {
  return (
    <div className="header">
      <span>Header Component</span>
      <ul>
      </ul>
    </div>
  );
}

function About() {
  return (
    <div
      className="about component"
    >
      <h1> About Component </h1>
    </div>
  );
}

function Contact() {
  return (
    <div
      className="contact component"
    >
      <h1> Contact Component </h1>
    </div>
  );
}
```

Pour rendre ces composants sur le navigateur, vous les intégrez simplement dans le composant `App`.

```js

function App() {
  return (
    <div classname="App">
      <Header />
      <Home />
      <About />
      <Contact />
    </div>
  );
}
```

À première vue, votre application devrait ressembler à ceci dans le navigateur :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/004-Initial-rendering-of-your-components-without-any-styling.png)
_Rendu initial de vos composants sans aucun style_

Pour améliorer l'apparence de votre application, ajoutez ces styles :

```css
@import url("https://fonts.googleapis.com/css2?family=Rajdhani:wght@600&display=swap");

body {
  font-family: "Rajdhani", sans-serif;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
.header {
  padding: 20px;
  box-shadow: 3px 3px 5px rgba(0, 0, 0, 0.2);
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 10px;
}
.header span {
  font-size: 20px;
}

.header ul {
  display: flex;
  gap: 20px;
}

.header ul a {
  text-decoration: none;
  border: 1.5px solid #555;
  padding: 5px 10px;
  color: #333;
}

.component {
  font-size: 30px;
  height: 87vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.home {
  background: rgb(214, 223, 135);
}
.about {
  background: rgb(115, 139, 243);
}

.contact {
  background: palevioletred;
}
```

Voici à quoi cela devrait ressembler maintenant :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/After-applying-css.gif)
_Application après l'application du CSS_

Avec vos composants stylisés, vous pouvez commencer à configurer les routes.

Tout d'abord, enveloppez le contenu de votre composant `App` avec le `BrowserRouter`, puis enveloppez davantage le contenu avec la fonction `Routes`. Vous faites cela pour spécifier les composants entre lesquels vous pouvez naviguer.

```js
function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Header />
        <Routes>
          <Home />
          <About />
          <Contact />
        </Routes>
      </BrowserRouter>
    </div>
  );
}
```

Gardez à l'esprit que le composant `header` n'est pas placé à l'intérieur du composant `Routes` car il va apparaître sur la page indépendamment de la route vers laquelle vous naviguez.

Ensuite, vous attribuez un chemin de route à chaque composant.

```js
function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Header />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/contact" element={<Contact />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}
```

Pour l'instant, puisque vous êtes dans la route racine (/), seul le composant home est visible.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/005-Home-page-after-setting-up-the-routes-1.png)
_Page d'accueil après la configuration des routes_

Pour naviguer entre les pages, vous utilisez l'élément `NavLink` dans votre `header` ul et spécifiez une route différente par `NavLink`. Cela permettra une navigation facile par `NavLink` sur lequel vous cliquez.

```js
function Header() {
  return (
    <div className="header">
      <span>Header Component</span>
      <ul>
        <NavLink to="/">Home</NavLink>
        <NavLink to="/about">About</NavLink>
        <NavLink to="/contact">Contact</NavLink>
      </ul>
    </div>
  );
}
```

Avec cela, vous avez réussi à configurer des boutons de route pour vos composants !

![Image](https://www.freecodecamp.org/news/content/images/2023/04/After-setting-up-routing-buttons.gif)
_Après la configuration des boutons de routage_

## Comment configurer vos routes pour l'animation

Maintenant, ma partie préférée de cet article – l'animation des routes. Pour animer les routes dans React avec framer motion, vous importez d'abord 2 propriétés.

```js 
import { motion, AnimatePresence } from "framer-motion";
```

La propriété `motion` transforme tout élément que vous préfixez en un élément `motion` qui peut être animé avec Framer, et le composant `AnimatePresence` permet des animations fluides lors de l'ajout, de la suppression ou de la modification de composants d'un _arbre de composants React_ (représentation visuelle ou hiérarchie de tous les composants utilisés dans une application React).

Pour animer les routes, vous commencez par envelopper le contenu du `BrowserRouter` avec le composant `AnimatePresence`.

```js
function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <AnimatePresence>
          <Header />
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/about" element={<About />} />
            <Route path="/contact" element={<Contact />} />
          </Routes>
        </AnimatePresence>
      </BrowserRouter>
    </div>
  );
}
```

Seul, le composant `AnimatePresence` ne peut pas dire quand un composant a été monté ou démonté, donc vous devrez écouter ce changement.

Pour ce faire, vous utilisez le hook `useLocation` qui écoute quand il y a un changement dans l'URL de votre application (c'est-à-dire quand la route a changé). Mais vous êtes confronté à une erreur lorsque vous importez et invoquez le hook `useLocation` dans votre composant `App`.

```js
import { useLocation } from "react-router-dom"
```

 ```js
 const location = useLocation();
 ```

![Image](https://www.freecodecamp.org/news/content/images/2023/04/006-Error-using-useLocation.png)
_Erreur lors de l'utilisation de useLocation_

Cette erreur est causée parce que le hook useLocation ne peut être utilisé qu'à l'intérieur d'un composant Router (un composant qui n'est pas un descendant d'un composant Router), qui fournit le contexte de routage pour le hook.

Pour résoudre ce problème, vous devez faire un peu de refactoring. Tout d'abord, vous créez un composant `LocationProvider`. Ce composant est un composant wrapper qui retourne le `AnimationPresence`.

```js
function LocationProvider() {  return <AnimatePresence></AnimatePresence>; }
```

Vous passez ensuite la prop `children` au `LocationProvider` que le composant `AnimatePresence` utilise pour envelopper tout élément enfant qui aurait une animation de routage lorsqu'il est monté ou démonté.

```js
function LocationProvider({ children }) {
  return <AnimatePresence>{children}</AnimatePresence>;
}
```

Ensuite, vous créez un composant `RoutesWithAnimation` où vous spécifiez chaque route et l'élément à monter dans cette route. Dans ce composant, vous pouvez maintenant utiliser le hook `useLocation` pour vérifier quand il y a un changement de route.

```js
function RoutesWithAnimation() {
  const location = useLocation();

  return (
    <Routes location={location} key={location.key}>
      <Route path="/" element={<Home />} />
      <Route path="/about" element={<About />} />
      <Route path="/contact" element={<Contact />} />
    </Routes>
  );
}
```

**Note** : Une prop `key` a été passée dans le composant `Routes` que React utilise pour rendre le composant correct lorsque l'emplacement change.

Enfin, vous nettoyez le composant `App` de toute la logique de routage que vous avez définie précédemment et vous la remplacez par le `RoutesWithAnimation` imbriqué dans le `LocationProvider`.

```js
function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Header />
        <LocationProvider>
          <RoutesWithAnimation />
        </LocationProvider>
      </BrowserRouter>
    </div>
  );
}
```

Pour confirmer que vous suivez les changements de route, enregistrez la valeur `location` dans la console et basculez entre les routes.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Confirming-that-react-is-tracking-that-route-changes.gif)

Comme vous pouvez le voir, chaque fois que vous changez de route, le chemin de la route est enregistré dans la console, ainsi qu'une propriété `key` unique.

## Comment animer les routes avec Framer

Pour animer quoi que ce soit dans Framer, vous devez spécifier les éléments suivants.

* Variants : Les variants sont un moyen de définir et d'animer les propriétés d'un composant. Un variant est un objet qui contient un ou plusieurs ensembles nommés de propriétés, où chaque ensemble représente un état d'animation différent. Pour créer un variant pour vos routes, vous définissez d'abord un objet variant :

```js
const routeVariants = {}
```

* État initial de l'animation : Dans votre variant, vous spécifiez l'état initial de l'animation en créant un objet d'animation initial. Pour ce projet, l'animation que vous créez implique que chaque composant glisse depuis le bas (axe y) de la page. Pour ce faire, vous traduisez initialement l'ensemble du composant hors de la fenêtre d'affichage :

```js
const routeVariants = {
    initial: {
        y: '100vh'
    }
}
```

* État final de l'animation : Ensuite, vous spécifiez l'animation lorsque le composant est monté en spécifiant un état final de l'animation :

```js
const routeVariants = {
    initial: {
        y: '100vh'
    }
    final: {
        y: '0vh'
    }
}
```

Pour appliquer ces nouvelles propriétés d'animation à vos composants, vous faites d'abord de chaque composant un élément _motion_ en préfixant le mot-clé `motion`.

```js
function Home() {
  return <motion.div className="home component">  <h1> Home Component </h1></motion.div>;
}

function About() {
  return <motion.div className="about component"> <h1> About Component </h1></motion.div>;
}

function Contact() {
  return <motion.div className="contact component"> <h1> Contact Component </h1></motion.div>;
}
```

Ensuite, vous passez l'objet `variants` et chacun des états de variants à chaque composant que vous souhaitez animer. L'état `initial` est l'état démonté du composant et l'état `animate` est l'état monté du composant.

```js
function Home() {
  return (
    <motion.div
      variants={routeVariants}
      initial="initial"
      animate="final"
      className="home component"
    >
    <h1> Home Component </h1>
    </motion.div>
  );
}

function About() {
  return (
    <motion.div
      variants={routeVariants}
      initial="initial"
      animate="final"
      className="about component"
    >
     <h1>  About Component </h1>
    </motion.div>
  );
}

function Contact() {
  return (
    <motion.div
      variants={routeVariants}
      initial="initial"
      animate="final"
      className="contact component"
    >
    <h1> Contact Component </h1>
    </motion.div>
  );
}
```

Avec cela, votre animation devrait déjà fonctionner.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Initail-Routing-achieved-with-bouncy-effect.gif)
_Animation de routage initiale avec effet rebondissant supplémentaire obtenue_

Et voilà ! Vous avez réussi à animer les routes dans votre application React. Félicitations ! 🚀

Une chose que vous remarquerez est à quel point notre transition est rebondissante. Elle déborde légèrement dans le composant d'en-tête en entrant dans la page. Cela est dû au fait que le type d'animation par défaut dans Framer est le ressort qui se comporte ainsi.

Pour réduire l'effet, vous pouvez simplement spécifier une propriété `mass` sur l'état final de l'animation.

```js
final: {
    y: "0vh",
    transition: {
      type: "spring",
      mass: 0.4,
    },
  },
```

Cette propriété spécifie la masse du composant animé. Une augmentation de la valeur de la masse du composant animé entraîne un effet plus rebondissant et vice versa.

**Note** : La valeur de la masse est généralement maintenue entre 0 et 1. (0 étant sans effet de ressort et 1 étant beaucoup d'effet de ressort). La définition de la masse animée à 0,4 donne le résultat suivant :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Initail-Routing-achieved.gif)
_Effet rebondissant supplémentaire de routage résolu_

### Animations des enfants

Nous pouvons aller encore plus loin en animant la route séparément du contenu de cette route.

Commencez par créer un objet de variants enfants pour les titres dans chaque composant.

```js
const childVariants = {
  initial: {
    opacity: 0,
    y: "50px",
  },
  final: {
    opacity: 1,
    y: "0px",
    transition: {
      duration: 0.5,
      delay: 0.5,
    },
  },
};
```

Le `childVariant` anime les éléments enfants en les déplaçant vers le haut de 50px et en les rendant visibles en augmentant l'opacité. Enfin, le délai fait que cette animation se déclenche légèrement après l'animation du composant parent.

Pour rendre cette animation efficace, vous faites de chaque h1 un élément de mouvement. Après cela, vous définissez vos variants et états d'animation dans tous les éléments enfants que vous souhaitez animer. Chaque élément h1 devrait ressembler à ceci :

```js
 <motion.h1 variants={childVariants} initial="initial" animate="final">
        // Quel que soit le nom du composant qui était ici.
</motion.h1>
```

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Final-Routing-animation.gif)
_Résultat final avec animation de routage et d'enfants obtenue_

Et avec cela, vous avez implémenté une animation de routage assez élégante avec Framer, félicitations ! 🎉

Pour référence, voici le code complet :

```js
import {
  BrowserRouter,
  NavLink,
  Route,
  Routes,
  useLocation,
} from "react-router-dom";

import { motion, AnimatePresence } from "framer-motion";

const routeVariants = {
  initial: {
    y: "100vh",
  },
  final: {
    y: "0vh",
    transition: {
      type: "spring",
      mass: 0.4,
    },
  },
};

const childVariants = {
  initial: {
    opacity: 0,
    y: "50px",
  },
  final: {
    opacity: 1,
    y: "0px",
    transition: {
      duration: 0.5,
      delay: 0.5,
    },
  },
};

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Header />
        <LocationProvider>
          <RoutesWithAnimation />
        </LocationProvider>
      </BrowserRouter>
    </div>
  );
}

function LocationProvider({ children }) {
  return <AnimatePresence>{children}</AnimatePresence>;
}

function RoutesWithAnimation() {
  const location = useLocation();
  console.log(location);

  return (
    <Routes location={location} key={location.key}>
      <Route path="/" element={<Home />} />
      <Route path="/about" element={<About />} />
      <Route path="/contact" element={<Contact />} />
    </Routes>
  );
}

function Header() {
  return (
    <div className="header">
      <span>Header Component</span>
      <ul>
        <NavLink to="/">Home</NavLink>
        <NavLink to="/about">About</NavLink>
        <NavLink to="/contact">Contact</NavLink>
      </ul>
    </div>
  );
}

function Home() {
  return (
    <motion.div
      variants={routeVariants}
      initial="initial"
      animate="final"
      className="home component"
    >
      <motion.h1 variants={childVariants} initial="initial" animate="final">
        Home Component
      </motion.h1>
    </motion.div>
  );
}

function About() {
  return (
    <motion.div
      variants={routeVariants}
      initial="initial"
      animate="final"
  
      className="about component"
    >
      <motion.h1 variants={childVariants} initial="initial" animate="final">
        About Component
      </motion.h1>
    </motion.div>
  );
}

function Contact() {
  return (
    <motion.div
      variants={routeVariants}
      initial="initial"
      animate="final"
  
      className="contact component"
    >
      <motion.h1 variants={childVariants} initial="initial" animate="final">
        Contact Component
      </motion.h1>
    </motion.div>
  );
}
export default App;
```

Voici un lien vers le dépôt : [GitHub](https://github.com/Daiveedjay/Framer-Articl)

Et la version live : [Netlify](https://react-framer-article.netlify.app/)

## Réflexions finales

Je dois dire que j'ai pris beaucoup de plaisir à écrire cet article et à créer cette animation, et j'espère que vous aussi. (J'ai également actualisé une fois de trop parce que j'aimais l'effet d'animation 😉).

J'ai vraiment été motivé à publier cet article parce que lorsque j'ai appris Framer Motion il y a quelques semaines, j'ai eu du mal à trouver des ressources à jour pour m'apprendre à l'utiliser, surtout celles qui l'implémentaient avec la dernière version des deux outils (react-router v6 et Framer motion 10). J'espère donc que cet article fournit une référence pour une approche beaucoup plus récente des animations de routage avec Framer.

### Ressources

Pour en savoir plus sur framer motion et react-router, voici quelques ressources que je recommande :

* [Framer Motion (Pour React)](https://www.youtube.com/watch?v=2V1WK-3HQNk&list=PL4cUxeGkcC9iHDnQfTHEVVceOEBsOf07i)
* [Framer motion Docs](https://www.framer.com/motion/)
* [React Router In-depth](https://www.youtube.com/watch?v=OMQ2QARHPo0&list=PL4cUxeGkcC9iVKmtNuCeIswnQ97in2GGf)
* [React Router V6](https://www.youtube.com/watch?v=k2Zk5cbiZhg)

## Conclusion

En conclusion, l'animation des routes dans une application React en utilisant Framer Motion peut améliorer l'expérience utilisateur en créant des transitions fluides et transparentes entre différentes pages.

En incorporant des composants comme `AnimatePresence`, `motion` et `variants`, vous pouvez personnaliser les animations de votre application, la rendant plus engageante et visuellement attrayante.

La mise en œuvre d'animations peut améliorer le flux global et la navigation de votre application, créant une expérience plus agréable et réactive pour vos utilisateurs.

### Informations de contact

Vous souhaitez me contacter ? N'hésitez pas à me contacter sur les plateformes suivantes :

* Twitter : [@jajadavid8](https://twitter.com/JajaDavid8)
* LinkedIn : [David Jaja](https://www.linkedin.com/in/david-jaja-8084251b4/)
* Email : Jajadavidjid@gmail.com