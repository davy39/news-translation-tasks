---
title: Tutoriel Three.js – Comment rendre des objets 3D dans le navigateur
subtitle: ''
author: Hunor Márton Borbély
co_authors: []
series: null
date: '2021-02-03T23:06:37.000Z'
originalURL: https://freecodecamp.org/news/render-3d-objects-in-browser-drawing-a-box-with-threejs
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/Stack.002-1.jpeg
tags:
- name: 3d
  slug: 3d
- name: '#Game Design'
  slug: game-design
- name: Game Development
  slug: game-development
- name: JavaScript
  slug: javascript
- name: three.js
  slug: three-js
seo_title: Tutoriel Three.js – Comment rendre des objets 3D dans le navigateur
seo_desc: "If you have ever wanted to build a game with JavaScript, you might have\
  \ come across Three.js. \nThree.js is a library that we can use to render 3D graphics\
  \ in the browser. The whole thing is in JavaScript, so with some logic you can add\
  \ animation, int..."
---

Si vous avez déjà voulu créer un jeu avec JavaScript, vous avez peut-être rencontré Three.js. 

Three.js est une bibliothèque que nous pouvons utiliser pour rendre des graphiques 3D dans le navigateur. Tout est en JavaScript, donc avec un peu de logique, vous pouvez ajouter de l'animation, de l'interaction, ou même en faire un jeu. 

Dans ce tutoriel, nous allons passer par un exemple très simple. Nous allons rendre une boîte 3D, et en faisant cela, nous allons apprendre les bases de Three.js. 

Three.js utilise WebGL sous le capot pour rendre des graphiques 3D. Nous pourrions utiliser WebGL directement, mais c'est très complexe et plutôt bas niveau. D'un autre côté, Three.js est comme jouer avec des Legos. 

Dans cet article, nous allons voir comment placer un objet 3D dans une scène, configurer l'éclairage et une caméra, et rendre la scène sur un canevas. Alors voyons comment nous pouvons faire tout cela.

## Définir l'objet Scène

Tout d'abord, nous devons définir une scène. Ce sera un conteneur où nous placerons nos objets 3D et nos lumières. L'objet scène a également certaines propriétés, comme la couleur de fond. La définir est facultatif cependant. Si nous ne la définissons pas, le fond sera noir par défaut.

```js
import * as THREE from "three";

const scene = new THREE.Scene();
scene.background = new THREE.Color(0x000000); // Optionnel, le noir est la valeur par défaut

...
```

## Géométrie + Matériau = Maillage

Ensuite, nous ajoutons notre boîte 3D à la scène en tant que maillage. Un maillage est une combinaison d'une géométrie et d'un matériau.

```js
...

// Ajouter un cube à la scène
const geometry = new THREE.BoxGeometry(3, 1, 3); // largeur, hauteur, profondeur
const material = new THREE.MeshLambertMaterial({ color: 0xfb8e00 });
const mesh = new THREE.Mesh(geometry, material);
mesh.position.set(0, 0, 0); // Optionnel, 0,0,0 est la valeur par défaut
scene.add(mesh);

...
```

### Qu'est-ce qu'une Géométrie ?

Une géométrie est une forme rendue que nous construisons - comme une boîte. Une géométrie peut être construite à partir de sommets ou nous pouvons utiliser une géométrie prédéfinie. 

La BoxGeometry est l'option prédéfinie la plus basique. Nous devons seulement définir la largeur, la hauteur et la profondeur de la boîte et c'est tout. 

Vous pourriez penser que nous ne pouvons pas aller loin en définissant des boîtes, mais de nombreux jeux avec un design minimaliste n'utilisent qu'une combinaison de boîtes. 

Il existe également d'autres géométries prédéfinies. Nous pouvons facilement définir un plan, un cylindre, une sphère, ou même un icosaèdre.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/freecodecamp-4.001.jpeg)

### Comment travailler avec un Matériau

Ensuite, nous définissons un matériau. Un matériau décrit l'apparence d'un objet. Ici, nous pouvons définir des choses comme la texture, la couleur ou l'opacité. 

Dans cet exemple, nous allons seulement définir une couleur. Il existe encore différentes options pour les matériaux. La principale différence entre la plupart d'entre eux est la manière dont ils réagissent à la lumière. 

Le plus simple est le MeshBasicMaterial. Ce matériau ne tient pas compte de la lumière du tout, et chaque côté aura la même couleur. Ce n'est peut-être pas la meilleure option, cependant, car vous ne pouvez pas voir les bords de la boîte.

Le matériau le plus simple qui tient compte de la lumière est le MeshLambertMaterial. Cela calculera la couleur de chaque sommet, ce qui est pratiquement chaque côté. Mais cela ne va pas au-delà.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/freecodecamp-4.002.jpeg)

Si vous avez besoin de plus de précision, il existe des matériaux plus avancés. Le MeshPhongMaterial ne calcule pas seulement la couleur par sommet mais par chaque pixel. La couleur peut changer au sein d'un côté. Cela peut aider avec le réalisme mais coûte également en performance. 

Cela dépend également des réglages de lumière et de la géométrie si cela a un effet réel. Si nous rendons des boîtes et utilisons une lumière directionnelle, le résultat ne changera pas beaucoup. Mais si nous rendons une sphère, la différence est plus évidente.

### Comment positionner un Maillage

Une fois que nous avons un maillage, nous pouvons également le positionner dans la scène et définir une rotation par chaque axe. Plus tard, si nous voulons animer des objets dans l'espace 3D, nous ajusterons principalement ces valeurs. 

Pour le positionnement, nous utilisons les mêmes unités que celles utilisées pour définir la taille. Peu importe si vous utilisez des petits nombres ou des grands nombres, vous devez simplement être cohérent dans votre propre monde. 

Pour la rotation, nous définissons les valeurs en radians. Donc si vous avez vos valeurs en degrés, vous devez les diviser par 180° puis multiplier par PI.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/freecodecamp-3.004.jpeg)

## Comment ajouter de la Lumière

Ensuite, ajoutons des lumières. Un maillage avec un matériau de base n'a pas besoin de lumière, car le maillage aura la couleur définie indépendamment des réglages de lumière. 

Mais le matériau Lambert et le matériau Phong nécessitent de la lumière. Si il n'y a pas de lumière, le maillage restera dans l'obscurité.

```js
...

// Configurer les lumières
const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
scene.add(ambientLight);

...
```

Nous allons ajouter deux lumières - une lumière ambiante et une lumière directionnelle. 

Tout d'abord, nous ajoutons la lumière ambiante. La lumière ambiante brille de toutes les directions, donnant une couleur de base à notre géométrie. 

Pour définir une lumière ambiante, nous définissons une couleur et une intensité. La couleur est généralement blanche, mais vous pouvez définir n'importe quelle couleur. L'intensité est un nombre entre 0 et 1. Les deux lumières que nous définissons fonctionnent de manière cumulative, donc dans ce cas, nous voulons que l'intensité soit d'environ 0,5 pour chacune.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/freecodecamp-3.003.jpeg)

La lumière directionnelle a une configuration similaire, mais elle a aussi une position. Le mot position ici est un peu trompeur, car cela ne signifie pas que la lumière provient d'une position exacte. 

La lumière directionnelle brille de très loin avec de nombreux rayons lumineux parallèles ayant tous un angle fixe. Mais au lieu de définir des angles, nous définissons la direction d'un seul rayon lumineux. 

Dans ce cas, elle brille de la direction de la position 10,20,0 vers la coordonnée 0,0,0. Mais bien sûr, la lumière directionnelle n'est pas seulement un rayon lumineux, mais une quantité infinie de rayons parallèles. 

Pensez-y comme au soleil. À une plus petite échelle, les rayons lumineux du soleil descendent également en parallèle, et la position du soleil n'est pas ce qui compte, mais plutôt sa direction. 

Et c'est ce que fait la lumière directionnelle. Elle brille sur tout avec des rayons lumineux parallèles de très loin.

```js
...

const dirLight = new THREE.DirectionalLight(0xffffff, 0.6);
dirLight.position.set(10, 20, 0); // x, y, z
scene.add(dirLight);

...
```

Ici, nous définissons la position de la lumière pour qu'elle provienne du haut (avec la valeur Y) et la décalons un peu le long de l'axe X également. L'axe Y a la valeur la plus élevée. Cela signifie que le haut de la boîte reçoit le plus de lumière et ce sera le côté le plus brillant de la boîte. 

La lumière est également déplacée un peu le long de l'axe X, donc le côté droit de la boîte recevra également un peu de lumière, mais moins. 

Et parce que nous ne déplaçons pas la position de la lumière le long de l'axe Z, le côté avant de la boîte ne recevra aucune lumière de cette source. Si il n'y avait pas de lumière ambiante, le côté avant resterait dans l'obscurité. 

Il existe d'autres types de lumières également. La PointLight, par exemple, peut être utilisée pour simuler des ampoules. Elle a une position fixe et émet de la lumière dans toutes les directions. Et la SpotLight peut être utilisée pour simuler le projecteur d'une voiture. Elle émet de la lumière d'un seul point dans une direction le long d'un cône.

## Comment configurer la Caméra

Jusqu'à présent, nous avons créé un maillage avec une géométrie et un matériau. Et nous avons également configuré des lumières et les avons ajoutées à la scène. Nous avons encore besoin d'une caméra pour définir comment nous regardons cette scène. 

Il y a deux options ici : les caméras en perspective et les caméras orthographiques.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Stack.010.jpeg)

Les jeux vidéo utilisent principalement des caméras en perspective, car leur fonctionnement est similaire à la manière dont vous voyez les choses dans la vie réelle. Les choses qui sont plus éloignées semblent être plus petites et les choses qui sont juste devant vous semblent plus grandes. 

Avec les projections orthographiques, les choses auront la même taille peu importe leur distance par rapport à la caméra. Les caméras orthographiques ont un look plus minimal, géométrique. Elles ne déforment pas les géométries - les lignes parallèles apparaîtront en parallèle.

Pour les deux caméras, nous devons définir un frustum de vue. Il s'agit de la région dans l'espace 3D qui va être projetée sur l'écran. Tout ce qui est en dehors de cette région n'apparaîtra pas sur l'écran. Cela est dû au fait qu'il est soit trop proche soit trop éloigné, ou parce que la caméra n'est pas dirigée vers lui.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/freecodecamp-2.001.jpeg)

Avec la projection en perspective, tout ce qui se trouve dans le frustum de vue est projeté vers le point de vue avec une ligne droite. Les choses plus éloignées de la caméra apparaissent plus petites sur l'écran, car du point de vue, vous pouvez les voir sous un angle plus petit.

```js
...

// Caméra en perspective
const aspect = window.innerWidth / window.innerHeight;
const camera = new THREE.PerspectiveCamera(
  45, // champ de vision en degrés
  aspect, // ratio d'aspect
  1, // plan proche
  100 // plan éloigné
);

...
```

Pour définir une caméra en perspective, vous devez définir un champ de vision, qui est l'angle vertical depuis le point de vue. Ensuite, vous définissez un ratio d'aspect de la largeur et de la hauteur du cadre. Si vous remplissez toute la fenêtre du navigateur et que vous souhaitez conserver son ratio d'aspect, alors voici comment vous pouvez le faire. 

Ensuite, les deux derniers paramètres définissent à quelle distance les plans proche et éloigné sont du point de vue. Les choses qui sont trop proches de la caméra seront ignorées, et les choses qui sont trop éloignées seront également ignorées.

```js
...

// Caméra orthographique
const width = 10;
const height = width * (window.innerHeight / window.innerWidth);
const camera = new THREE.OrthographicCamera(
  width / -2, // gauche
  width / 2, // droite
  height / 2, // haut
  height / -2, // bas
  1, // proche
  100 // éloigné
);

...
```

Ensuite, il y a la caméra orthographique. Ici, nous ne projetons pas les choses vers un seul point mais vers une surface. Chaque ligne de projection est parallèle. C'est pourquoi il n'a pas d'importance à quelle distance les objets sont de la caméra, et c'est pourquoi elle ne déforme pas les géométries. 

Pour les caméras orthographiques, nous devons définir à quelle distance chaque plan est du point de vue. Le plan de gauche est donc à cinq unités à gauche, et le plan de droite est à cinq unités à droite, et ainsi de suite.

```js
...

camera.position.set(4, 4, 4);
camera.lookAt(0, 0, 0);

...
```

Quelle que soit la caméra que nous utilisons, nous devons également la positionner et la diriger. Si nous utilisons une caméra orthographique, les nombres réels ici n'ont pas autant d'importance. Les objets apparaîtront de la même taille peu importe leur distance par rapport à la caméra. Ce qui compte, cependant, c'est leur proportion. 

Tout au long de ce tutoriel, nous avons vu tous les exemples à travers la même caméra. Cette caméra a été déplacée de la même unité le long de chaque axe et elle regarde vers la coordonnée 0,0,0. Positionner une caméra orthographique est comme positionner une lumière directionnelle. Ce n'est pas la position réelle qui compte, mais sa direction.

## Comment rendre la Scène

Nous avons donc réussi à assembler la scène et une caméra. Maintenant, il ne manque que la pièce finale qui rend l'image dans notre navigateur. 

Nous devons définir un WebGLRenderer. C'est la pièce capable de rendre l'image réelle dans un canevas HTML lorsque nous fournissons une scène et une caméra. C'est également ici que nous pouvons définir la taille réelle de ce canevas - la largeur et la hauteur du canevas en pixels tels qu'ils doivent apparaître dans le navigateur.

```js
import * as THREE from "three";

// Scène
const scene = new THREE.Scene();

// Ajouter un cube à la scène
const geometry = new THREE.BoxGeometry(3, 1, 3); // largeur, hauteur, profondeur
const material = new THREE.MeshLambertMaterial({ color: 0xfb8e00 });
const mesh = new THREE.Mesh(geometry, material);
mesh.position.set(0, 0, 0);
scene.add(mesh);

// Configurer les lumières
const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
scene.add(ambientLight);

const directionalLight = new THREE.DirectionalLight(0xffffff, 0.6);
directionalLight.position.set(10, 20, 0); // x, y, z
scene.add(directionalLight);

// Caméra
const width = 10;
const height = width * (window.innerHeight / window.innerWidth);
const camera = new THREE.OrthographicCamera(
  width / -2, // gauche
  width / 2, // droite
  height / 2, // haut
  height / -2, // bas
  1, // proche
  100 // éloigné
);

camera.position.set(4, 4, 4);
camera.lookAt(0, 0, 0);

// Rendu
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.render(scene, camera);

// Ajouter à HTML
document.body.appendChild(renderer.domElement);
```

Et enfin, la dernière ligne ici ajoute ce canevas rendu à notre document HTML. Et c'est tout ce dont vous avez besoin pour rendre une boîte. Cela peut sembler un peu trop pour une seule boîte, mais la plupart de ces choses, nous n'avons à les configurer qu'une seule fois. 

Si vous souhaitez avancer avec ce projet, alors regardez ma vidéo YouTube sur la façon de transformer cela en un simple jeu. Dans la vidéo, nous créons un jeu de construction de pile. Nous ajoutons une logique de jeu, des gestionnaires d'événements et de l'animation, et même un peu de physique avec Cannon.js.

%[https://youtu.be/hBiGFpBle7E]

Si vous avez des commentaires ou des questions sur ce tutoriel, n'hésitez pas à me tweeter [@HunorBorbely](https://twitter.com/HunorBorbely) ou à laisser un commentaire sur [YouTube](https://www.youtube.com/channel/UCxhgW0Q5XLvIoXHAfQXg9oQ).