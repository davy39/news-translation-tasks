---
title: Comment créer des bulles animées avec HTML5 Canvas et JavaScript
subtitle: ''
author: Shruti Kapoor
co_authors: []
series: null
date: '2023-09-05T14:08:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-animated-bubbles-with-html5-canvas-and-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/shrutikapoor.dev--11-.jpg
tags:
- name: animation
  slug: animation
- name: HTML5
  slug: html5
- name: JavaScript
  slug: javascript
seo_title: Comment créer des bulles animées avec HTML5 Canvas et JavaScript
seo_desc: 'Hello everyone! Welcome to this tutorial where we''re going to dive into
  the world of creating fun bubbles in code using HTML canvas and JavaScript. The
  best part? We''ll achieve all of this using just a touch of HTML and all JavaScript,
  no CSS.

  What w...'
---

Bonjour à tous ! Bienvenue dans ce tutoriel où nous allons plonger dans le monde de la création de bulles amusantes en code en utilisant HTML canvas et JavaScript. La meilleure partie ? Nous allons réaliser tout cela en utilisant juste une touche de HTML et tout JavaScript, sans CSS.

## Ce que nous allons apprendre

Dans cet article, vous allez maîtriser les concepts suivants :

* Comment créer des cercles en utilisant la méthode `arc` du contexte du canvas.
* Comment utiliser la fonction `requestAnimationFrame` pour des animations de cercles fluides.
* Comment exploiter la puissance des classes JavaScript pour créer plusieurs cercles sans répéter de code.
* Comment ajouter des styles de contour et des styles de remplissage à vos cercles pour un effet de bulle 3D.

Vous pouvez suivre avec moi, ou utiliser [le codepen final](https://codepen.io/shrutikapoor08/pen/wvQXMVO) si vous voulez jeter un coup d'œil au code source.

Si vous préférez apprendre en format vidéo, suivez cette vidéo :



%[https://www.youtube.com/watch?v=IjPgXP3gDyI&ab_channel=ShrutiKapoor]

## Commencer

Tout d'abord, nous avons besoin d'un élément HTML5 Canvas. Canvas est un élément puissant pour créer des formes, des images et des graphiques. C'est ce que nous allons utiliser pour créer les bulles.

Commençons par le configurer :

```html
<canvas id="canvas"></canvas>

```

Pour faire quoi que ce soit de significatif avec canvas, nous devons avoir accès à son `contexte`. [Contexte](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D) fournit une interface pour rendre des objets sur le canvas et dessiner des formes.

Voici comment obtenir l'accès au canvas et à son contexte.

```js
const canvas = document.getElementById('canvas');
const context = canvas.getContext('2d');

```

Nous allons également configurer notre canvas pour utiliser toute la hauteur et la largeur de la fenêtre :

```js
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

```

Ensuite, nous allons donner au canvas un joli fond bleu clair apaisant en ajoutant un peu de CSS. C'est le seul CSS que nous allons utiliser. Vous pouvez également le faire avec JavaScript si vous le souhaitez.

```css
#canvas {
  background: #00b4ff;
}

```

## Comment créer des bulles avec Canvas

Passons à la partie amusante. Nous allons créer des bulles en cliquant sur le canvas. Pour y parvenir, nous allons commencer par créer un gestionnaire d'événements de clic :

```js
canvas.addEventListener('click', handleDrawCircle);

```

Puisque nous devons savoir où nous avons cliqué sur notre canvas, nous allons suivre cela dans notre fonction `handleDrawCircle` et utiliser les coordonnées de l'événement :

```js

//Nous ajoutons x et y ici car nous en aurons besoin plus tard.
let x, y
const handleDrawCircle = (event) => {
  x = event.pageX;
  y = event.pageY;

  // Dessiner une bulle !
  drawCircle(x, y);
};

```

### Comment dessiner des cercles en utilisant la méthode `arc`

Pour créer des cercles, nous allons utiliser la [méthode `arc` disponible sur le contexte du canvas.](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/arc) La méthode `arc` accepte `x` et `y` (le centre du cercle), un rayon, et un angle de départ et un angle de fin qui pour nous seront `0` et `2* Math.PI` respectivement parce que nous créons un cercle complet.

C'est-à-dire :

```js
const drawCircle = (x, y) => {
  context.beginPath();
  context.arc(x, y, 50, 0, 2 * Math.PI);

  context.strokeStyle = 'white';
  context.stroke();
};

```

![Dessiner des cercles](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/1zrbq3gcpff40nbvzbt8.png)
_cercles créés en utilisant la méthode arc_

### Comment déplacer des cercles en utilisant la méthode `requestAnimationFrame`

Maintenant que nous avons des cercles, faisons-les bouger parce que...

![Une scène de la chanson "I like to move it" du film -Madagascar](https://media.giphy.com/media/ptS6CV6Ty7Dt26k6wq/giphy.gif)

Rappelons que lorsque nous avons créé un cercle, nous avons utilisé la méthode `arc` qui acceptait les coordonnées `x` et `y` — le centre du cercle. Si nous déplaçons les coordonnées `x` et `y` de notre cercle très rapidement, cela donnera l'impression que les cercles bougent. Essayons cela !

```js
//Définir une vitesse pour incrémenter les coordonnées x et y

const dx = Math.random() * 3;
const dy = Math.random() * 7;

//Incrémenter le centre du cercle avec cette vitesse
x = x + dx;
y = y - dy;

```

Nous pouvons déplacer cela dans une fonction :

```js
let x, y;

const move = () => {
  const dx = Math.random() * 3;
  const dy = Math.random() * 7;

  x = x + dx;
  y = y - dy;
};

```

Pour donner à notre cercle un mouvement fluide, nous allons créer une fonction `animate` et utiliser la méthode `requestAnimationFrame` du navigateur pour créer un cercle en mouvement :

```js
const animate = () => {
  context.clearRect(0, 0, canvas.width, canvas.height);

  move();
	drawCircle(x,y);

  requestAnimationFrame(animate);
};

//N'oubliez pas d'appeler animate en bas 
animate();

```

![Cercle en animation](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/z01uy7e82sqia06svu5t.gif)
_cercles en mouvement créés avec la méthode requestAnimationFrame_

### Comment créer des particules en utilisant une classe Particle

Maintenant que nous avons créé un cercle, il est temps de créer plusieurs cercles ! Mais avant de faire cela, préparons notre code.

Pour éviter de répéter notre code, nous allons utiliser des classes et introduire une classe `Particle`. Les particules sont les éléments de base de notre œuvre d'art dynamique et de notre animation. Chaque bulle est une particule avec sa propre position, taille, mouvement et attributs de couleur. Définissons une classe **`Particle`** pour encapsuler ces propriétés :

```js
class Particle {
  constructor(x = 0, y = 0) {}

  draw() {
    // Dessiner la particule comme un cercle coloré
    // ...
  }

  move() {
    // Implémenter le mouvement de la particule
    // ...
  }
}

```

Déplaçons certaines des constantes que nous avions configurées vers la classe `Particle` :

```js
class Particle {
  constructor(x = 0, y = 0) {
    this.x = x;
    this.y = y;
    this.radius = Math.random() * 50;
    this.dx = Math.random() * 3;
    this.dy = Math.random() * 7;
  }

  draw() {
    // Dessiner la particule comme un cercle coloré
    // ...
  }

  move() {
    // Implémenter le mouvement de la particule
    // ...
  }
}

```

La méthode **`draw`** sera responsable du rendu de la particule sur le canvas. Nous avons déjà implémenté cette fonctionnalité dans `drawCircle`, alors déplaçons-la dans notre classe et mettons à jour les variables pour qu'elles soient des variables de classe :

```js
class Particle {
  constructor(x = 0, y = 0) {
    this.x = x;
    this.y = y;
    this.radius = Math.random() * 50;
    this.dx = Math.random() * 3;
    this.dy = Math.random() * 7;
    this.color = 'white';
  }

  draw() {
    context.beginPath();
    context.arc(this.x, this.y, this.radius, 0, 2 * Math.PI);
    context.strokeStyle = this.color;
    context.stroke();

    context.fillStyle = this.color;
    context.fill();
  }

  move() {}
}

```

De même, déplaçons la fonction `move` dans la classe :

```js
move() {
	this.x = this.x + this.dx;
	this.y = this.y - this.dy;
}

```

Ensuite, nous devons nous assurer que nous appelons la classe `Particle` dans notre gestionnaire d'événements :

```js
const handleDrawCircle = (event) => {
  const x = event.pageX;
  const y = event.pageY;

  const particle = new Particle(x, y);
};

canvas.addEventListener('click', handleDrawCircle);

```

Puisque nous devons accéder à cette particule dans notre fonction animate afin d'appeler la méthode `move` sur celle-ci, nous allons stocker cette particule dans un tableau appelé `particleArray`. Ce tableau sera également utile lors de la création de nombreuses particules. 

Voici le code mis à jour pour refléter cela :

```js
const particleArray = [];

const handleDrawCircle = (event) => {
  const x = event.pageX;
  const y = event.pageY;

  const particle = new Particle(x, y);
  particleArray.push(particle);
};

canvas.addEventListener('click', handleDrawCircle);

```

N'oubliez pas de mettre à jour la fonction `animate` également :

```javascript
const animate = () => {
	context.clearRect(0, 0, canvas.width, canvas.height);

	particleArray.forEach((particle) => {
		particle?.move();
		particle?.draw();
	});

	requestAnimationFrame(animate);
};
```

À ce stade, vous verrez ces particules sur votre écran :

![Plusieurs cercles en mouvement](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/92rs6a5i1xn4v2gzdv8o.gif)

Super ! Maintenant, passons à la partie amusante ! Créons beaucoup de cercles et stylisons-les pour qu'ils ressemblent à des bulles.

Pour créer beaucoup de bulles, nous allons créer des particules en utilisant une boucle `for` et les ajouter au `particleArray` que nous avons créé.

```js
const handleDrawCircle = (event) => {
  const x = event.pageX;
  const y = event.pageY;

  for (let i = 0; i < 50; i++) {
    const particle = new Particle(x, y);
    particleArray.push(particle);
  }
};

canvas.addEventListener('click', handleDrawCircle);

```

Dans la fonction animate, nous allons mettre à jour en continu le canvas en le nettoyant et en redessinant les particules dans leurs nouvelles positions. Cela donnera l'illusion que le cercle bouge :

```js
const animate = () => {
  context.clearRect(0, 0, canvas.width, canvas.height);

  particleArray.forEach((particle) => {
    particle?.move();
    particle?.draw();
  });

  requestAnimationFrame(animate);
};

animate();

```

![Plusieurs cercles en animation](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ya5u8w8qetqkcy2nbowe.gif)

Maintenant que nous avons des bulles qui bougent, il est temps d'ajouter de la couleur pour qu'elles ressemblent à de vraies bulles !

Nous allons le faire en ajoutant un dégradé de remplissage aux bulles. Cela peut être fait en utilisant la méthode `context.createRadialGradient` :

```js
const gradient = context.createRadialGradient(
  this.x,
  this.y,
  1,
  this.x + 0.5,
  this.y + 0.5,
  this.radius
);

gradient.addColorStop(0.3, 'rgba(255, 255, 255, 0.3)');
gradient.addColorStop(0.95, '#e7feff');

context.fillStyle = gradient;

```

![Bulles](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/l80yde62l9mw3ceh1f1i.gif)

[Voici le codepen final](https://codepen.io/shrutikapoor08/pen/wvQXMVO) si vous voulez jeter un coup d'œil au code source.

## Conclusion

Félicitations ! Vous venez de créer quelque chose de super amusant en utilisant uniquement HTML Canvas et JavaScript. Vous avez appris à utiliser la méthode `arc`, à exploiter la méthode `requestAnimationFrame`, à exploiter la puissance des classes JavaScript, et à styliser vos bulles en utilisant des dégradés pour l'effet de bulle 3D.

N'hésitez pas à expérimenter avec les couleurs, les vitesses et les tailles pour rendre vos animations vraiment uniques.

J'espère que vous avez eu autant de plaisir à suivre ce tutoriel que j'en ai eu à le créer. Maintenant, c'est à votre tour d'expérimenter. J'adorerais voir si vous avez essayé cela et ce que vous avez créé. Partagez avec moi votre lien de code et j'adorerais le vérifier.

---

Et maintenant une #DevJoke :

Question - Qui a gagné le débat pour le meilleur nom de variable de boucle ?

Réponse - i a gagné.

---

Si vous avez aimé cet article, partagez-le avec quelqu'un qui en bénéficiera. 

Si vous êtes intéressé par des articles comme celui-ci et des articles front-end sur JavaScript, React, GraphQL ou l'accessibilité et des conseils de carrière d'un ingénieur principal, [inscrivez-vous à ma newsletter](https://tinyletter.com/shrutikapoor) et recevez ceux-ci directement dans votre boîte de réception.