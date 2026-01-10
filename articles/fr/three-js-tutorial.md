---
title: Tutoriel Three.js - Comment construire une voiture simple avec texture en 3D
subtitle: ''
author: Hunor Márton Borbély
co_authors: []
series: null
date: '2021-03-22T13:47:23.000Z'
originalURL: https://freecodecamp.org/news/three-js-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-19-at-11.31.27-1.png
tags:
- name: Game Development
  slug: game-development
- name: JavaScript
  slug: javascript
- name: three.js
  slug: three-js
seo_title: Tutoriel Three.js - Comment construire une voiture simple avec texture
  en 3D
seo_desc: 'Putting together a 3D scene in the browser with Three.js is like playing
  with Legos. We put together some boxes, add lights, define a camera, and Three.js
  renders the 3D image.

  In this tutorial, we''re going to put together a minimalistic car from box...'
---

Assembler une scène 3D dans le navigateur avec Three.js, c'est comme jouer avec des Legos. Nous assemblons quelques boîtes, ajoutons des lumières, définissons une caméra, et Three.js rend l'image 3D.

Dans ce tutoriel, nous allons assembler une voiture minimaliste à partir de boîtes et apprendre à appliquer une texture dessus. 

Tout d'abord, nous allons configurer les choses – nous définirons les lumières, la caméra et le rendu. Ensuite, nous apprendrons à définir des géométries et des matériaux pour créer des objets 3D. Et enfin, nous allons coder des textures avec JavaScript et HTML Canvas.

## Comment configurer le projet Three.js

Three.js est une bibliothèque externe, donc nous devons d'abord l'ajouter à notre projet. J'ai utilisé NPM pour l'installer dans mon projet, puis je l'ai importé au début du fichier JavaScript.

```javascript
import * as THREE from "three"; 

const scene = new THREE.Scene();

. . .
```

Tout d'abord, nous devons définir la scène. La scène est un conteneur qui contient tous les objets 3D que nous voulons afficher ainsi que les lumières. Nous allons ajouter une voiture à cette scène, mais d'abord, configurons les lumières, la caméra et le rendu.

### Comment configurer les lumières

Nous allons ajouter deux lumières à la scène : une lumière ambiante et une lumière directionnelle. Nous définissons les deux en réglant une couleur et une intensité. 

La couleur est définie comme une valeur hexadécimale. Dans ce cas, nous la réglons sur blanc. L'intensité est un nombre entre 0 et 1, et comme les deux brillent simultanément, nous voulons que ces valeurs soient autour de 0,5. 

```javascript
. . . 

const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
scene.add(ambientLight);

const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
directionalLight.position.set(200, 500, 300);
scene.add(directionalLight); 

. . .
```

La lumière ambiante brille dans toutes les directions, donnant une couleur de base à notre géométrie tandis que la lumière directionnelle simule le soleil. 

La lumière directionnelle brille de très loin avec des rayons lumineux parallèles. Nous définissons une position pour cette lumière qui définit la direction de ces rayons lumineux. 

Cette position peut être un peu déroutante, alors laissez-moi expliquer. Parmi tous les rayons parallèles, nous en définissons un en particulier. Ce rayon lumineux spécifique brillera de la position que nous définissons (200,500,300) vers la coordonnée 0,0,0. Le reste sera parallèle à celui-ci. 

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Loop-driver.015.jpeg)

Comme les rayons lumineux sont parallèles et brillent de très loin, les coordonnées exactes n'ont pas d'importance ici – plutôt, ce sont leurs proportions qui comptent. 

Les trois paramètres de position sont les coordonnées X, Y et Z. Par défaut, l'axe Y pointe vers le haut, et comme il a la valeur la plus élevée (500), cela signifie que le haut de notre voiture reçoit le plus de lumière. Il sera donc le plus brillant. 

Les deux autres valeurs définissent de combien la lumière est courbée le long des axes X et Z, c'est-à-dire combien de lumière le devant et le côté de la voiture recevront. 

### Comment configurer la caméra

Ensuite, configurons la caméra qui définit comment nous regardons cette scène. 

Il y a deux options ici – les caméras en perspective et les caméras orthographiques. Les jeux vidéo utilisent principalement des caméras en perspective, mais nous allons utiliser une caméra orthographique pour avoir un look plus minimaliste et géométrique.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Loop-driver.018.jpeg)

Dans [mon article précédent](https://www.freecodecamp.org/news/render-3d-objects-in-browser-drawing-a-box-with-threejs/), nous avons discuté des différences entre les deux caméras en détail. Par conséquent, dans celui-ci, nous ne discuterons que de la façon de configurer une caméra orthographique. 

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Loop-driver.019.jpeg)

Pour la caméra, nous devons définir un frustum de vue. Il s'agit de la région dans l'espace 3D qui sera projetée sur l'écran. 

Dans le cas d'une caméra orthographique, il s'agit d'une boîte. La caméra projette les objets 3D à l'intérieur de cette boîte vers l'un de ses côtés. Comme chaque ligne de projection est parallèle, les caméras orthographiques ne déforment pas les géométries.

```javascript
. . .

// Configuration de la caméra
const aspectRatio = window.innerWidth / window.innerHeight;
const cameraWidth = 150;
const cameraHeight = cameraWidth / aspectRatio;

const camera = new THREE.OrthographicCamera(
  cameraWidth / -2, // gauche
  cameraWidth / 2, // droite
  cameraHeight / 2, // haut
  cameraHeight / -2, // bas
  0, // plan proche
  1000 // plan éloigné
);
camera.position.set(200, 200, 200);
camera.lookAt(0, 10, 0);

. . .
```

Pour configurer une caméra orthographique, nous devons définir à quelle distance chaque côté du frustum se trouve du point de vue. Nous définissons que le côté gauche est à 75 unités à gauche, le plan droit est à 75 unités à droite, et ainsi de suite. 

Ici, ces unités ne représentent pas les pixels de l'écran. La taille de l'image rendue sera définie au niveau du rendu. Ici, ces valeurs ont une unité arbitraire que nous utilisons dans l'espace 3D. Plus tard, lors de la définition des objets 3D dans l'espace 3D, nous allons utiliser les mêmes unités pour définir leur taille et leur position. 

Une fois que nous avons défini une caméra, nous devons également la positionner et la diriger dans une direction. Nous déplaçons la caméra de 200 unités dans chaque dimension, puis nous la faisons regarder vers la coordonnée 0,10,0. Cela se trouve presque à l'origine. Nous regardons vers un point légèrement au-dessus du sol, où se trouvera le centre de notre voiture. 

### Comment configurer le rendu

Le dernier élément que nous devons configurer est un rendu qui rend la scène selon notre caméra dans notre navigateur. Nous définissons un WebGLRenderer comme ceci :

```js
. . .

// Configuration du rendu
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.render(scene, camera);

document.body.appendChild(renderer.domElement);
```

Ici, nous définissons également la taille du canevas. C'est le seul endroit où nous définissons la taille en pixels, puisque nous définissons comment il doit apparaître dans le navigateur. Si nous voulons remplir toute la fenêtre du navigateur, nous transmettons la taille de la fenêtre. 

Et enfin, la dernière ligne ajoute cette image rendue à notre document HTML. Elle crée un élément HTML Canvas pour afficher l'image rendue et l'ajoute au DOM. 

## Comment construire la voiture dans Three.js

Maintenant, voyons comment nous pouvons composer une voiture. Tout d'abord, nous allons créer une voiture sans texture. Il s'agira d'un design minimaliste – nous allons simplement assembler quatre boîtes.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-19-at-11.18.04.png)

### Comment ajouter une boîte

Tout d'abord, nous créons une paire de roues. Nous allons définir une boîte grise qui représente à la fois une roue gauche et une roue droite. Comme nous ne voyons jamais la voiture par en dessous, nous ne remarquerons pas que, au lieu d'avoir une roue gauche et une roue droite séparées, nous n'avons qu'une grande boîte. 

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-19-at-11.01.43.png)

Nous aurons besoin d'une paire de roues à l'avant et à l'arrière de la voiture, donc nous pouvons créer une fonction réutilisable.

```js
. . . 

function createWheels() {
  const geometry = new THREE.BoxBufferGeometry(12, 12, 33);
  const material = new THREE.MeshLambertMaterial({ color: 0x333333 });
  const wheel = new THREE.Mesh(geometry, material);
  return wheel;
}

. . .
```

Nous définissons la roue comme un maillage. Le maillage est une combinaison d'une géométrie et d'un matériau et il représentera notre objet 3D. 

La géométrie définit la forme de l'objet. Dans ce cas, nous créons une boîte en définissant ses dimensions le long des axes X, Y et Z à 12, 12 et 33 unités. 

Ensuite, nous transmettons un matériau qui définira l'apparence de notre maillage. Il existe différentes options de matériaux. La principale différence entre eux est la manière dont ils réagissent à la lumière.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/materials.001.jpeg)

Dans ce tutoriel, nous utiliserons `MeshLambertMaterial`. Le `MeshLambertMaterial` calcule la couleur pour chaque sommet. Dans le cas du dessin d'une boîte, cela représente essentiellement chaque côté. 

Nous pouvons voir comment cela fonctionne, car chaque côté de la boîte a une nuance différente. Nous avons défini une lumière directionnelle pour briller principalement d'en haut, donc le haut de la boîte est le plus brillant.

D'autres matériaux calculent la couleur, non seulement pour chaque côté mais pour chaque pixel à l'intérieur du côté. Ils donnent des images plus réalistes pour des formes plus complexes. Mais pour des boîtes éclairées avec une lumière directionnelle, ils ne font pas une grande différence. 

### Comment construire le reste de la voiture

Ensuite, de manière similaire, créons le reste de la voiture. Nous définissons la fonction `createCar` qui retourne un Groupe. Ce groupe est un autre conteneur comme la scène. Il peut contenir des objets Three.js. C'est pratique car si nous voulons déplacer la voiture, nous pouvons simplement déplacer le Groupe. 

```js
. . .

function createCar() {
  const car = new THREE.Group();
  
  const backWheel = createWheels();
  backWheel.position.y = 6;
  backWheel.position.x = -18;
  car.add(backWheel);
  
  const frontWheel = createWheels();
  frontWheel.position.y = 6;  
  frontWheel.position.x = 18;
  car.add(frontWheel);

  const main = new THREE.Mesh(
    new THREE.BoxBufferGeometry(60, 15, 30),
    new THREE.MeshLambertMaterial({ color: 0x78b14b })
  );
  main.position.y = 12;
  car.add(main);

  const cabin = new THREE.Mesh(
    new THREE.BoxBufferGeometry(33, 12, 24),
    new THREE.MeshLambertMaterial({ color: 0xffffff })
  );
  cabin.position.x = -6;
  cabin.position.y = 25.5;
  car.add(cabin);

  return car;
}

const car = createCar();
scene.add(car);

renderer.render(scene, camera);

. . .
```

Nous générons deux paires de roues avec notre fonction, puis définissons la partie principale de la voiture. Ensuite, nous ajouterons le haut de la cabine comme quatrième maillage. Ce sont tous simplement des boîtes avec des dimensions et des couleurs différentes.

![Image](https://www.freecodecamp.org/news/content/images/2024/08/car-boxes.jpg)

Par défaut, chaque géométrie sera au milieu, et leurs centres seront à la coordonnée 0,0,0. 

Tout d'abord, nous les soulevons en ajustant leur position le long de l'axe Y. Nous soulevons les roues de la moitié de leur hauteur – ainsi, au lieu de s'enfoncer à moitié dans le sol, elles reposent sur le sol. Ensuite, nous ajustons également les pièces le long de l'axe X pour atteindre leur position finale. 

Nous ajoutons ces pièces au groupe de la voiture, puis ajoutons le groupe entier à la scène. Il est important que nous ajoutions la voiture à la scène avant de rendre l'image, sinon nous devrons appeler le rendu à nouveau une fois que nous avons modifié la scène. 

### Comment ajouter une texture à la voiture

Maintenant que nous avons notre modèle de voiture très basique, ajoutons quelques textures à la cabine. Nous allons peindre les fenêtres. Nous définirons une texture pour les côtés et une pour l'avant et l'arrière de la cabine. 

![Image](https://www.freecodecamp.org/news/content/images/2021/03/textures.001.jpeg)

Lorsque nous configurons l'apparence d'un maillage avec un matériau, définir une couleur n'est pas la seule option. Nous pouvons également mapper une texture. Nous pouvons fournir la même texture pour chaque côté ou nous pouvons fournir un matériau pour chaque côté dans un tableau. 

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Loop-driver.038.jpeg)

En tant que texture, nous pourrions utiliser une image. Mais au lieu de cela, nous allons créer des textures avec JavaScript. Nous allons coder des images avec HTML Canvas et JavaScript. 

Avant de continuer, nous devons faire quelques distinctions entre Three.js et HTML Canvas. 

Three.js est une bibliothèque JavaScript. Elle utilise WebGL sous le capot pour rendre des objets 3D en une image, et elle affiche le résultat final dans un élément canvas. 

HTML Canvas, en revanche, est un élément HTML, tout comme l'élément `div` ou la balise de paragraphe. Ce qui le rend spécial, cependant, c'est que nous pouvons dessiner des formes sur cet élément avec JavaScript. 

C'est ainsi que Three.js rend la scène dans le navigateur, et c'est ainsi que nous allons créer des textures. Voyons comment elles fonctionnent. 

### Comment dessiner sur un HTML Canvas

Pour dessiner sur un canvas, nous devons d'abord créer un élément canvas. Bien que nous créions un élément HTML, cet élément ne fera jamais partie de notre structure HTML. En soi, il ne sera pas affiché sur la page. Au lieu de cela, nous allons le transformer en une texture Three.js. 

Voyons comment nous pouvons dessiner sur ce canvas. Tout d'abord, nous définissons la largeur et la hauteur du canvas. La taille ici ne définit pas la taille à laquelle le canvas apparaîtra, c'est plutôt comme la résolution du canvas. La texture sera étirée sur le côté de la boîte, quelle que soit sa taille.

```javascript
function getCarFrontTexture() {
  const canvas = document.createElement("canvas");
  canvas.width = 64;
  canvas.height = 32;
  const context = canvas.getContext("2d");

  context.fillStyle = "#ffffff";
  context.fillRect(0, 0, 64, 32);

  context.fillStyle = "#666666";
  context.fillRect(8, 8, 48, 24);

  return new THREE.CanvasTexture(canvas);
}
```

Ensuite, nous obtenons le contexte de dessin 2D. Nous pouvons utiliser ce contexte pour exécuter des commandes de dessin. 

Tout d'abord, nous allons remplir tout le canvas avec un rectangle blanc. Pour ce faire, nous définissons d'abord le style de remplissage en blanc. Ensuite, nous remplissons un rectangle en définissant sa position en haut à gauche et sa taille. Lors du dessin sur un canvas, par défaut, la coordonnée 0,0 se trouvera dans le coin supérieur gauche. 

Ensuite, nous remplissons un autre rectangle avec une couleur grise. Celui-ci commence à la coordonnée 8,8 et ne remplit pas le canvas, il ne peint que les fenêtres. 

Et c'est tout – la dernière ligne transforme l'élément canvas en une texture et la retourne, afin que nous puissions l'utiliser pour notre voiture. 

```javascript
function getCarSideTexture() {
  const canvas = document.createElement("canvas");
  canvas.width = 128;
  canvas.height = 32;
  const context = canvas.getContext("2d");

  context.fillStyle = "#ffffff";
  context.fillRect(0, 0, 128, 32);

  context.fillStyle = "#666666";
  context.fillRect(10, 8, 38, 24);
  context.fillRect(58, 8, 60, 24);

  return new THREE.CanvasTexture(canvas);
}
```

De manière similaire, nous pouvons définir la texture latérale. Nous créons à nouveau un élément canvas, nous obtenons son contexte, puis nous remplissons d'abord tout le canvas pour avoir une couleur de base, et ensuite nous dessinons les fenêtres sous forme de rectangles. 

### Comment mapper des textures sur une boîte

Maintenant, voyons comment nous pouvons utiliser ces textures pour notre voiture. Lorsque nous définissons le maillage pour le haut de la cabine, au lieu de définir un seul matériau, nous en définissons un pour chaque côté. Nous définissons un tableau de six matériaux. Nous mappons des textures sur les côtés de la cabine, tandis que le haut et le bas auront toujours une couleur unie. 

```javascript
. . .

function createCar() {
  const car = new THREE.Group();

  const backWheel = createWheels();
  backWheel.position.y = 6;
  backWheel.position.x = -18;
  car.add(backWheel);

  const frontWheel = createWheels();
  frontWheel.position.y = 6;
  frontWheel.position.x = 18;
  car.add(frontWheel);

  const main = new THREE.Mesh(
    new THREE.BoxBufferGeometry(60, 15, 30),
    new THREE.MeshLambertMaterial({ color: 0xa52523 })
  );
  main.position.y = 12;
  car.add(main);

  const carFrontTexture = getCarFrontTexture();

  const carBackTexture = getCarFrontTexture();

  const carRightSideTexture = getCarSideTexture();

  const carLeftSideTexture = getCarSideTexture();
  carLeftSideTexture.center = new THREE.Vector2(0.5, 0.5);
  carLeftSideTexture.rotation = Math.PI;
  carLeftSideTexture.flipY = false;

  const cabin = new THREE.Mesh(new THREE.BoxBufferGeometry(33, 12, 24), [
    new THREE.MeshLambertMaterial({ map: carFrontTexture }),
    new THREE.MeshLambertMaterial({ map: carBackTexture }),
    new THREE.MeshLambertMaterial({ color: 0xffffff }), // haut
    new THREE.MeshLambertMaterial({ color: 0xffffff }), // bas
    new THREE.MeshLambertMaterial({ map: carRightSideTexture }),
    new THREE.MeshLambertMaterial({ map: carLeftSideTexture }),
  ]);
  cabin.position.x = -6;
  cabin.position.y = 25.5;
  car.add(cabin);

  return car;
}

. . .
```

La plupart de ces textures seront mappées correctement sans aucun ajustement. Mais si nous tournons la voiture, nous pouvons voir les fenêtres apparaître dans le mauvais ordre sur le côté gauche.

![Image](https://www.freecodecamp.org/news/content/images/2024/08/fixing-texture-before-after.jpg)
_Côté droit et côté gauche avant et après la correction de la texture_

Cela est attendu car nous utilisons la texture pour le côté droit ici également. Nous pouvons définir une texture séparée pour le côté gauche ou nous pouvons miroir le côté droit.

Malheureusement, nous ne pouvons pas retourner une texture horizontalement. Nous ne pouvons retourner une texture que verticalement. Nous pouvons corriger cela en 3 étapes.

Tout d'abord, nous tournons la texture de 180 degrés, ce qui équivaut à PI en radians. Avant de la tourner, cependant, nous devons nous assurer que la texture est tournée autour de son centre. Ce n'est pas le comportement par défaut – nous devons définir que le centre de rotation est à mi-chemin. Nous définissons 0,5 sur les deux axes, ce qui signifie essentiellement 50 %. Enfin, nous retournons la texture à l'envers pour la mettre dans la bonne position.

## Conclusion

Alors, qu'avons-nous fait ici ? Nous avons créé une scène qui contient notre voiture et les lumières. Nous avons construit la voiture à partir de boîtes simples. 

Vous pourriez penser que c'est trop basique, mais si vous y réfléchissez, de nombreux jeux mobiles avec des looks stylisés sont en fait créés en utilisant des boîtes. Ou pensez simplement à Minecraft pour voir jusqu'où vous pouvez aller en assemblant des boîtes. 

Ensuite, nous avons créé des textures avec HTML canvas. HTML canvas est capable de bien plus que ce que nous avons utilisé ici. Nous pouvons dessiner différentes formes avec des courbes et des arcs, mais parfois un design minimal est tout ce dont nous avons besoin.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-19-at-11.31.27-2.png)

Et enfin, nous avons défini une caméra pour établir comment nous regardons cette scène, ainsi qu'un rendu qui rend l'image finale dans le navigateur.

## Prochaines étapes

Si vous voulez jouer avec le code, vous pouvez trouver le code source sur [CodePen](https://codepen.io/HunorMarton/pen/qBqzQOJ). Et si vous voulez avancer avec ce projet, alors regardez ma vidéo YouTube sur la façon de transformer cela en un jeu. 

Dans ce tutoriel, nous créons un jeu de course de trafic. Après avoir défini la voiture, nous dessinons la piste de course, nous ajoutons la logique du jeu, les gestionnaires d'événements et l'animation.

%[https://youtu.be/JhgBwJn1bQw]