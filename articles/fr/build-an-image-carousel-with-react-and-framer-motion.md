---
title: Comment créer un carrousel d'images avec React et Framer Motion
subtitle: ''
author: Clinton Joy
co_authors: []
series: null
date: '2023-07-03T09:47:00.000Z'
originalURL: https://freecodecamp.org/news/build-an-image-carousel-with-react-and-framer-motion
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-2023-06-26-at-10.45.34.png
tags:
- name: animation
  slug: animation
- name: React
  slug: react
seo_title: Comment créer un carrousel d'images avec React et Framer Motion
seo_desc: "You've probably come across carousels in many modern-day applications.\
  \ Known by various names such as sliders or rotators, these versatile web elements\
  \ showcase content in a visually appealing, sliding, or rotating manner. \nCarousels\
  \ can help you sav..."
---

Vous avez probablement déjà rencontré des carrousels dans de nombreuses applications modernes. Connus sous divers noms tels que sliders ou rotateurs, ces éléments web polyvalents présentent du contenu de manière visuellement attrayante, glissante ou rotative.

Les carrousels peuvent vous aider à économiser de l'espace ainsi qu'à améliorer votre interface utilisateur et à offrir une excellente expérience utilisateur.

Les carrousels sont devenus un élément incontournable de la conception d'interfaces utilisateur, souvent utilisés pour afficher des images, des témoignages, et plus encore. Ils sont indispensables lors de la création d'une interface engageante et dynamique.

Dans cet article, nous allons plonger dans le processus de création d'un carrousel d'images en utilisant React et Framer Motion, en vous guidant à travers chaque étape pour créer un composant visuel époustouflant et interactif pour votre application.

## Qu'est-ce que Framer Motion ?

Il s'agit d'une bibliothèque d'animation open-source pour les applications React que vous pouvez utiliser pour créer des animations dynamiques et réactives pour notre application web.

Framer Motion dispose de plusieurs fonctionnalités utiles, notamment :

1. Animation : Cela vous permet de faire des transitions fluides pour vos composants.
2. Geste : Il prend en charge les mouvements tactiles et de la souris, ce qui vous permet de prendre en compte certains événements.
3. Variantes : Framer Motion vous permet de déclarer des composants de manière déclarative, en gardant votre code organisé et réutilisable.

Toutes ces fonctionnalités sont très utiles et nous allons bientôt les voir en action.

Pour approfondir votre compréhension de Framer Motion, vous pouvez explorer sa [documentation et ses ressources](https://www.framer.com/motion/). Mais pour cet article, nous nous concentrerons sur les fondamentaux. Alors que je vous guide à travers les bases de l'utilisation de Framer Motion, mon objectif principal est de construire un carrousel d'images impressionnant et engageant.

## Comment configurer votre environnement de développement

La première chose que nous allons faire est de configurer votre environnement de développement. Cela implique d'installer les packages nécessaires pour construire avec succès votre application. Cela inclut l'installation de [Node.js](https://nodejs.dev/en/download/) et [npm](https://www.npmjs.com/package/download)

Si vous avez déjà Node.js et npm installés, vous n'avez pas besoin de les télécharger et de les installer à nouveau.

### Créer une application React

À ce stade, je vais supposer que vous avez Node et npm installés. Pour créer une application React, rendez-vous simplement dans votre terminal et visitez le répertoire où vous souhaitez que votre application soit. Ensuite, exécutez cette commande :

```js
npx create-react-app react-image-carousel
```

Vous pouvez nommer votre application comme vous le souhaitez – mais pour les besoins de cet article, je l'appellerai `react-image-carousel`.

Lorsque votre application React est créée avec succès, ouvrez votre répertoire dans votre éditeur de code. Vous devriez obtenir certains fichiers et styles par défaut et cela devrait ressembler à ceci :

![Image](https://i.imgur.com/rC9qt5N.png)

Nous n'aurons pas besoin de la plupart de ces fichiers et styles pour ce projet, vous pouvez donc supprimer des fichiers comme app.test.js, logo.svg, reportWebVitals.js, setupTest.js. Vous pouvez également supprimer tous les styles par défaut dans la feuille App.css.

![Image](https://i.imgur.com/3en8Ssk.png)

Maintenant que votre application React est créée et configurée, la dernière étape pour configurer votre environnement de développement pour ce projet est d'installer Framer Motion.

Pour ce faire, rendez-vous simplement dans votre terminal, assurez-vous d'être dans le répertoire du projet et exécutez cette commande :

```js
 npm  install framer-motion
```

et cela devrait installer la dernière version de Framer Motion. Maintenant, vous devriez être prêt à partir. Utilisez simplement `npm run start` pour lancer le serveur de développement sur votre navigateur.

## Comment concevoir le composant Carousel

Pour commencer la conception, nous allons d'abord créer un composant `Carousel.js`. Dans le composant carousel, nous allons importer le hook `useState` de React puis les propriétés `motion` et `AnimatePresence` de Framer Motion.

```javascript
import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";

```

Nous créons ensuite notre fonction carousel qui prend la prop `images` qui sera un tableau d'URLs d'images :

```javascript
const Carousel = ({ images }) => {};

```

Dans notre fonction carousel, nous initialisons une variable d'état avec useState pour suivre l'index de l'image actuelle, nous utilisons `setCurrentIndex` comme fonction correspondante pour mettre à jour l'index.

Ensuite, nous créons 3 fonctions d'assistance pour gérer les interactions utilisateur qui incluent :

* handleNext : cela met à jour le currentIndex vers l'index suivant afin de changer l'image et s'il atteint la fin du tableau, il revient au début.
* handlePrevious : cela fait la même chose que la fonction handleNext, mais cette fois dans l'ordre inverse. Cela nous permet de revenir aux images.
* handleDotClick : cela prend un index comme paramètre et met à jour le currentIndex. Avec cela, nous pouvons sauter en avant et en arrière vers les images simplement en cliquant sur les points.

```javascript
const Carousel = ({ images }) => {
  const [currentIndex, setCurrentIndex] = useState(0);

  const handleNext = () => {
    setCurrentIndex((prevIndex) =>
      prevIndex + 1 === images.length ? 0 : prevIndex + 1
    );
  };
  const handlePrevious = () => {
    setCurrentIndex((prevIndex) =>
      prevIndex - 1 < 0 ? images.length - 1 : prevIndex - 1
    );
  };
  const handleDotClick = (index) => {
    setCurrentIndex(index);
  };

```

Ce sont les fonctions d'assistance dont nous aurons besoin pour notre composant.

### Comment créer notre modèle

Notre modèle est assez simple et se compose de notre image, de notre direction de slider et des points (indicateur).

```jsx
  return (
    <div className="carousel">
        <img
          key={currentIndex}
          src={images[currentIndex]}
        /><div className="slide_direction">
        <div className="left" onClick={handlePrevious}>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            height="20"
            viewBox="0 96 960 960"
            width="20"
          >
            <path d="M400 976 0 576l400-400 56 57-343 343 343 343-56 57Z" />
          </svg>
        </div>
        <div className="right" onClick={handleNext}>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            height="20"
            viewBox="0 96 960 960"
            width="20"
          >
            <path d="m304 974-56-57 343-343-343-343 56-57 400 400-400 400Z" />
          </svg>
        </div>
      </div>
      <div className="indicator">
        {images.map((_, index) => (
          <div
            key={index}
            className={`dot ${currentIndex === index ? "active" : ""}`}
            onClick={() => handleDotClick(index)}
          ></div>
        ))}
      </div>
    </div>
  );

```

Comme vous pouvez le voir dans le modèle, nous affichons l'image à l'index actuel. Ensuite, nous avons une div de `slide_direction` qui contient deux divs avec les noms de classe `left` et `right`. Nous les avons créées comme des boutons de navigation pour le carrousel. Elles utilisent des SVGs en ligne pour afficher des icônes de flèches, et leurs gestionnaires onClick sont définis sur `handlePrevious` et `handleNext`, respectivement.

Nous avons également une div indicateur que nous avons créée pour afficher une série de points représentant chaque image dans le carrousel. Elle parcourt le tableau d'images et crée un point pour chaque image, définissant la classe active pour le point correspondant à l'`currentIndex`.

Nous avons ensuite attaché un gestionnaire onClick pour chaque point qui est défini pour appeler `handleDotClick` avec l'index du point.

Et cela devrait être notre modèle pour l'instant. Il ne reste plus qu'à exporter le composant carousel, à l'importer dans le composant `App.js` et à ajouter un peu de CSS. Ensuite, nous serons prêts à commencer l'animation.

Nous exportons donc simplement notre fonction carousel depuis notre composant `Carousel.js`.

```jsx
export default Carousel;

```

## Comment utiliser le composant Carousel

Nous avons créé notre composant carousel. Mais pour l'utiliser, nous devons l'importer dans notre composant App.js :

```jsx
import Carousel from "./Carousel";

```

Après cela, nous pouvons créer notre tableau d'images, qui contiendra nos URLs d'images.

```jsx
const images = [
  "https://images.pexels.com/photos/169647/pexels-photo-169647.jpeg?auto=compress&cs=tinysrgb&w=600",
  "https://images.pexels.com/photos/313782/pexels-photo-313782.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
  "https://images.pexels.com/photos/773471/pexels-photo-773471.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
  "https://images.pexels.com/photos/672532/pexels-photo-672532.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
  "https://images.pexels.com/photos/632522/pexels-photo-632522.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
  "https://images.pexels.com/photos/777059/pexels-photo-777059.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
];

```

Ce sont simplement des images que j'ai obtenues de [pexels](https://www.pexels.com/) – c'est ce que nous allons utiliser pour ce projet.

Ensuite, nous ajoutons notre fonction App qui contiendra notre modèle d'application.

```jsx
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Image Carousel using React and Framer Motion</h1>
      </header>
      <main>
        <Carousel images={images} />
      </main>
    </div>
  );
}
export default App;

```

Comme vous pouvez le voir, nous avons notre en-tête qui affiche simplement un en-tête indiquant de quoi parle notre application.

Ensuite, nous avons la section principale qui contient notre composant carousel ajouté et prend une prop du tableau d'images. Si vous vous souvenez, c'est la prop que nous avons utilisée dans notre composant carousel pour afficher les images.

Enfin, nous exportons le composant App afin de pouvoir l'utiliser dans le fichier index.js.

Pour voir tout cela ensemble sans style, exécutez la commande `npm run start`. L'application devrait ressembler à ceci :

![Image](https://i.imgur.com/xN2meFY.gif)

  
Moche, n'est-ce pas ? Oui, je suis d'accord avec vous. Mais avec juste quelques lignes de CSS, cela sera transformé. Alors plongeons-nous.

### Comment ajouter le CSS

Je ne veux pas créer une feuille de style séparée pour le composant carousel, donc nous ferons tout notre CSS dans le fichier App.css. N'oubliez pas d'importer votre feuille de style.

```jsx
import "./App.css"

```

Voici notre CSS :

```css
@import url("https://fonts.googleapis.com/css2?family=Oswald:wght@600&display=swap");
.App-header {
  font-size: 1rem;
  text-align: center;
  font-family: "Oswald", sans-serif;
  padding-bottom: 2rem;
}
.carousel-images {
  position: relative;
  border-radius: 10px;
  height: 400px;
  max-width: 650px;
  margin: auto;
  overflow: hidden;
}
.carousel-images img {
  width: 99%;
  height: 99%;
  border-radius: 8px;
  border: #ff00008e solid 2px;
}
.slide_direction {
  display: flex;
  justify-content: space-between;
}
.left,
.right {
  background-color: #fb666675;
  color: #fff;
  padding: 10px 8px 8px 13px;
  margin: 0 20px;
  border-radius: 50%;
  position: absolute;
  top: 0;
  bottom: 0;
  margin: auto 10px;
  height: 25px;
  width: 25px;
}
.left {
  left: 0;
}
.right {
  right: 0;
}
.carousel-indicator {
  margin-top: 20px;
  display: flex;
  justify-content: center;
  gap: 20px;
}
.dot {
  background-color: #333;
  width: 15px;
  height: 15px;
  border-radius: 50%;
}
.active {
  background-color: #fa2020;
}

```

Et voici le résultat avec notre CSS :  


![Image](https://i.imgur.com/0CfxWn4.gif)

Vous serez probablement d'accord pour dire que cela a l'air beaucoup mieux et est déjà entièrement fonctionnel.

Maintenant, passons à l'ajout de notre animation en utilisant Framer Motion pour lui donner un bel aspect glissant.

## Comment ajouter une animation au composant Carousel

Pour commencer à animer avec Framer Motion, il y a quelques concepts que vous devez connaître car nous allons les utiliser souvent dans cette section. Ces concepts incluent :

* Variants : Considérez une variante comme un groupe nommé de propriétés. Son rôle est de définir comment un élément doit apparaître ou s'animer. Vous pouvez créer différentes variantes pour représenter différents états visuels ou animations pour un élément, comme `open`, `closed`, `hover`, et ainsi de suite.
* Initial : Il s'agit simplement de l'état que votre objet possédera avant que l'animation ne commence.
* Animate : Il s'agit simplement de l'état vers lequel votre objet s'animera, c'est aussi simple que cela.

De retour au projet, nous allons ajouter nos animations à notre composant carousel. Nous avons déjà importé les deux propriétés dont nous aurons besoin – les propriétés `motion` et `AnimatePresence`.

Je vais diviser cette section en trois parties car nous allons ajouter une animation à trois parties de notre code, y compris l'image, les directions du slider et le point indicateur.

### Animation de l'image

Pour animer la sortie et l'entrée d'une image, nous devons envelopper notre élément `img` avec un composant `AnimationPresence`. Cela nous permet d'ajouter une animation chaque fois qu'une image quitte ou entre. Ensuite, nous attachons un `motion.` à notre balise comme ceci.

```jsx
 <AnimatePresence>
  <motion.img key={currentIndex} src={images[currentIndex]} />
</AnimatePresence>;

```

Ensuite, nous allons à l'extérieur de notre modèle et déclarons nos variantes.

```jsx
  const slideVariants = {
    hiddenRight: {
      x: "100%",
      opacity: 0,
    },
    hiddenLeft: {
      x: "-100%",
      opacity: 0,
    },
    visible: {
      x: "0",
      opacity: 1,
      transition: {
        duration: 1,
      },
    },
    exit: {
      opacity: 0,
      scale: 0.8,
      transition: {
        duration: 0.5,
      },
    },
  };

```

Comme vous pouvez le voir, `sliderVariants` a quatre propriétés :

* hiddenRight : cela définit l'opacité de l'image à 0 et la place du côté droit du conteneur.
* hiddenLeft : cela fait la même chose que hiddenRight mais cette fois elle est définie du côté gauche.
* visible : c'est la propriété qui sera appelée pour que l'animation de glissement se produise depuis la position où se trouve l'image jusqu'au centre du conteneur.
* exit : cette animation contrôle la suppression de l'image de l'écran lorsqu'une autre image glisse.

Maintenant, nos variantes sont définies. Comment indiquons-nous d'où l'image doit glisser ? Nous devons définir un état de direction et mettre à jour l'état en fonction de laquelle des `slide_direction` a été cliquée.

```jsx
  const [direction, setDirection] = useState('left');

```

Nous définissons donc la direction pour commencer à gauche. Cela est logique puisque la première image à afficher sera la première image. Ensuite, nous allons dans notre fonction d'assistance et définissons la direction en fonction de la direction qui a été cliquée.

```jsx
  const handleNext = () => {
    setDirection("right");
    setCurrentIndex((prevIndex) =>
      prevIndex + 1 === images.length ? 0 : prevIndex + 1
    );
  };

  const handlePrevious = () => {
    setDirection("left");

    setCurrentIndex((prevIndex) =>
      prevIndex - 1 < 0 ? images.length - 1 : prevIndex - 1
    );
  };

  const handleDotClick = (index) => {
    setDirection(index > currentIndex ? "right" : "left");
    setCurrentIndex(index);
  };

```

Vous avez peut-être remarqué que nous n'avons pas seulement défini l'état pour `handleNext` et `handlePrevious`. Nous l'avons également fait pour `handleDotClick`. Ainsi, chaque fois qu'un point précédent ou suivant est cliqué, la direction sera définie en conséquence.

Juste un rappel – le but de la direction est de définir l'état initial de l'image afin que le slider puisse fonctionner comme il se doit.

Maintenant que notre direction est définie, utilisons nos variantes dans notre élément `img`.

```jsx
<AnimatePresence>
          <motion.img
            key={currentIndex}
            src={images[currentIndex]}
            variants={slideVariants}
            initial={direction === "right" ? "hiddenRight" : "hiddenLeft"}
            animate="visible"
            exit="exit"
          />
        </AnimatePresence>

```

Nous ajoutons donc la prop `variants` et la définissons égale à `slideVariants` que nous avons créée. Ensuite, nous avons ajouté la prop initial et l'avons définie égale à un opérateur ternaire. Cela définit l'état initial de l'image pour être soit `hiddenRight` soit `hiddenLeft` en fonction de laquelle des `slider_direction` ou `dot` a été cliquée.

Ensuite, nous ajoutons la propriété animate, qui anime l'image de la position initiale à la position que nous avons définie dans la propriété `visible`.

Enfin, nous ajoutons notre propriété exit et la définissons à `exit`. Cela anime l'image hors de l'écran lorsqu'une nouvelle image entre.

Il y a beaucoup de props que vous pouvez utiliser lorsque vous travaillez avec Framer Motion. Vous pouvez consulter la [documentation](https://www.framer.com/motion/component/#props) pour en savoir plus à leur sujet.

Et avec cela en place, notre carrousel d'images devrait fonctionner parfaitement.

![Image](https://i.imgur.com/4VNWzsq.gif)

### Animation des sliders et des points

Nous pourrions nous arrêter ici, mais je veux simplement ajouter quelques animations à mes directions de slider et à mes points.

```jsx
  const slidersVariants = {
    hover: {
      scale: 1.2,
      backgroundColor: "#ff00008e",
    },
  }; 
const dotsVariants = {
    initial: {
      y: 0,
    },
    animate: {
      y: -10,
      scale: 1.3,
      transition: { type: "spring", stiffness: 1000, damping: "10" },
    },
    hover: {
      scale: 1.1,
      transition: { duration: 0.2 },
    },
  };

```

Comme d'habitude, nous créons d'abord nos variantes. Pour `slidersVariants`, nous ajoutons simplement une propriété hover. Pour `dotsVariants`, nous avons trois propriétés : initial, animate et hover.

Tout comme nous l'avons fait avec l'élément `img`, nous ajouterons `motion.` comme préfixe au nom de l'élément afin d'utiliser Framer Motion.

```jsx
<div className="slide_direction">
  <motion.div
    variants={slidersVariants}
    whileHover="hover"
    className="left"
    onClick={handlePrevious}
  >
    <svg
      xmlns="http://www.w3.org/2000/svg"
      height="20"
      viewBox="0 96 960 960"
      width="20"
    >
      <path d="M400 976 0 576l400-400 56 57-343 343 343 343-56 57Z" />
    </svg>
  </motion.div>
  <motion.div
    variants={slidersVariants}
    whileHover="hover"
    className="right"
    onClick={handleNext}
  >
    <svg
      xmlns="http://www.w3.org/2000/svg"
      height="20"
      viewBox="0 96 960 960"
      width="20"
    >
      <path d="m304 974-56-57 343-343-343-343 56-57 400 400-400 400Z" />
    </svg>
  </motion.div>
</div>;

```

Comme vous pouvez le voir, nous avons ajouté nos variantes et les avons définies égales à `slidersVariants`. Ensuite, nous avons utilisé une nouvelle propriété `whileHover` et l'avons définie égale à la propriété over que nous avons spécifiée dans notre objet `slidersVariants`.

```jsx
<motion.div
  key={index}
  className={`dot ${currentIndex === index ? "active" : ""}`}
  onClick={() => handleDotClick(index)}
  initial="initial"
  animate={currentIndex === index ? "animate" : ""}
  whileHover="hover"
  variants={dotsVariants}
></motion.div>;

```

Ici, nous n'avons pas seulement ajouté une prop whileHover. Nous avons également ajouté une prop `initial` et une prop `animate` qui anime le point de l'image actuelle pour qu'il se distingue.

Dans notre objet `slidersVariants`, nous avons spécifié un type de transition de type spring qui lui donne une nature rebondissante lorsque la transition d'animation a lieu.

Ajoutez tout cela ensemble et notre élégant Carrousel d'Images est prêt. Voici le résultat final :

![Image](https://i.imgur.com/Bgghl7M.gif)

Juste pour référence, voici le code complet du composant carousel :

```jsx
import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";

const Carousel = ({ images }) => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [direction, setDirection] = useState(null);

  const slideVariants = {
    hiddenRight: {
      x: "100%",
      opacity: 0,
    },
    hiddenLeft: {
      x: "-100%",
      opacity: 0,
    },
    visible: {
      x: "0",
      opacity: 1,
      transition: {
        duration: 1,
      },
    },
    exit: {
      opacity: 0,
      scale: 0.8,
      transition: {
        duration: 0.5,
      },
    },
  };
  const slidersVariants = {
    hover: {
      scale: 1.2,
      backgroundColor: "#ff00008e",
    },
  };
  const dotsVariants = {
    initial: {
      y: 0,
    },
    animate: {
      y: -10,
      scale: 1.2,
      transition: { type: "spring", stiffness: 1000, damping: "10" },
    },
    hover: {
      scale: 1.1,
      transition: { duration: 0.2 },
    },
  };

  const handleNext = () => {
    setDirection("right");
    setCurrentIndex((prevIndex) =>
      prevIndex + 1 === images.length ? 0 : prevIndex + 1
    );
  };

  const handlePrevious = () => {
    setDirection("left");

    setCurrentIndex((prevIndex) =>
      prevIndex - 1 < 0 ? images.length - 1 : prevIndex - 1
    );
  };

  const handleDotClick = (index) => {
    setDirection(index > currentIndex ? "right" : "left");
    setCurrentIndex(index);
  };

  return (
    <div className="carousel">
        <div className="carousel-images">
        <AnimatePresence>
          <motion.img
            key={currentIndex}
            src={images[currentIndex]}
            initial={direction === "right" ? "hiddenRight" : "hiddenLeft"}
            animate="visible"
            exit="exit"
            variants={slideVariants}
          />
        </AnimatePresence>
        <div className="slide_direction">
          <motion.div
            variants={slidersVariants}
            whileHover="hover"
            className="left"
            onClick={handlePrevious}
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              height="20"
              viewBox="0 96 960 960"
              width="20"
            >
              <path d="M400 976 0 576l400-400 56 57-343 343 343 343-56 57Z" />
            </svg>
          </motion.div>
          <motion.div
            variants={slidersVariants}
            whileHover="hover"
            className="right"
            onClick={handleNext}
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              height="20"
              viewBox="0 96 960 960"
              width="20"
            >
              <path d="m304 974-56-57 343-343-343-343 56-57 400 400-400 400Z" />
            </svg>
          </motion.div>
        </div>
      </div>
      <div className="carousel-indicator">
        {images.map((_, index) => (
          <motion.div
            key={index}
            className={`dot ${currentIndex === index ? "active" : ""}`}
            onClick={() => handleDotClick(index)}
            initial="initial"
            animate={currentIndex === index ? "animate" : ""}
            whileHover="hover"
            variants={dotsVariants}
          ></motion.div>
        ))}
      </div>
    </div>
  );
};
export default Carousel;

```

Consultez le dépôt Git sur [GitHub](https://github.com/Cejay101/ImageCarousel).

Voici le site sur [Netlify](https://image-carousel-cj.netlify.app/).

_Juste une note qu'il y a des problèmes d'accessibilité avec ce code, et donc il ne devrait pas être utilisé dans un environnement de production._

## Ressources

Je comprends qu'il peut y avoir certains termes ou syntaxes qui peuvent ne pas être clairs, surtout si vous êtes nouveau dans React ou nouveau dans l'utilisation de Framer Motion. Voici quelques ressources que je recommanderais si vous voulez en savoir plus :

* [Documentation React](https://legacy.reactjs.org/docs)
* [Documentation Framer Motion](https://www.framer.com/motion/)
* [Cours Framer Motion](https://www.youtube.com/playlist?list=PL4cUxeGkcC9iHDnQfTHEVVceOEBsOf07i)

## Conclusion

Dans cet article, nous avons exploré le processus de conception d'un carrousel d'images engageant et réactif en utilisant la combinaison puissante de React et Framer Motion, une bibliothèque d'animation et de gestes.

En incorporant des composants comme `motion` et `AnimationPresence`, nous avons pu parcourir les étapes pour construire un carrousel visuellement attrayant. Ce carrousel met en valeur nos images et offre des transitions fluides entre les images avec des animations captivantes pour une expérience utilisateur améliorée.