---
title: Comment coder un clone du jeu Crossy Road avec Three.js
subtitle: ''
author: Hunor Márton Borbély
co_authors: []
series: null
date: '2025-02-20T23:29:26.115Z'
originalURL: https://freecodecamp.org/news/how-to-code-a-crossy-road-game-clone-with-threejs
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1740094139765/282432bf-1a5b-40e4-8b74-7aa854fd20ac.png
tags:
- name: ThreeJS
  slug: threejs
- name: Game Development
  slug: game-development
- name: JavaScript
  slug: javascript
- name: javascript game
  slug: javascript-game
seo_title: Comment coder un clone du jeu Crossy Road avec Three.js
seo_desc: In this tutorial, you’ll learn how to create a clone of the mobile game
  Crossy Road with Three.js. The goal of this game is to move a character through
  an endless path of static and moving obstacles. You have to go around trees and
  avoid getting hit ...
---

Dans ce tutoriel, vous apprendrez à créer un clone du jeu mobile Crossy Road avec Three.js. Le but de ce jeu est de déplacer un personnage à travers un chemin sans fin d'obstacles statiques et mobiles. Vous devez contourner les arbres et éviter de vous faire heurter par les voitures.

Il y a beaucoup de choses à couvrir dans ce tutoriel : nous commencerons par configurer la scène, la caméra et les lumières. Ensuite, vous apprendrez à dessiner le joueur et la carte avec les arbres et les voitures. Nous aborderons également comment animer les véhicules, et nous ajouterons des gestionnaires d'événements pour déplacer le joueur sur la carte. Enfin, nous ajouterons la détection de collision entre les voitures et le joueur.

Cet article est une version abrégée du tutoriel Crossy Road de mon site [JavaScriptGameTutorials.com](https://javascriptgametutorials.com/). Le tutoriel étendu est également disponible sous forme de vidéo sur [YouTube](https://www.youtube.com/watch?v=vNr3_hQ3Bws&ab_channel=HunorM%C3%A1rtonBorb%C3%A9ly).

## Table des matières

1. [Comment installer le jeu](#heading-installation)

2. [Comment rendre une carte](#heading-comment-rendre-une-carte)

3. [Comment animer les voitures](#heading-comment-animer-les-voitures)

4. [Comment déplacer le joueur](#heading-comment-deplacer-le-joueur)

5. [Détection de collision](#heading-detection-de-collision)

6. [Prochaines étapes](#heading-prochaines-etapes)

## Comment installer le jeu

Dans ce chapitre, nous allons configurer la toile de dessin, la caméra et les lumières, et rendre une boîte représentant notre joueur.

### Initialisation du projet

Je recommande d'utiliser Vite pour initialiser le projet. Pour ce faire, allez dans votre terminal et tapez `npm create vite`, ce qui créera un projet initial pour vous.

```bash
# Créer une application
npm create vite my-crossy-road-game

# Naviguer vers le projet
cd my-crossy-road-game

# Installer les dépendances
npm install three

# Démarrer le serveur de développement
npm run dev
```

Lors de la génération du projet, sélectionnez **Vanilla** car nous n'utiliserons aucun framework front-end pour ce projet. Ensuite, naviguez vers le dossier du projet que Vite vient de créer pour vous et installez Three.js avec `npm install three`. Enfin, vous pouvez aller dans le terminal et taper `npm run dev` pour démarrer un serveur de développement. Ainsi, vous pouvez voir en direct le résultat de votre codage dans le navigateur.

### La toile de dessin

Maintenant, examinons ce projet. Le point d'entrée de ce projet est le fichier **index.html** dans le dossier racine. Remplaçons l'élément div par un élément canvas avec l'ID **game**. C'est la toile de dessin que Three.js utilisera pour rendre la scène. Ce fichier contient également une balise script qui pointe vers le fichier JavaScript principal.

```xml
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Vite App</title>
  </head>
  <body>
    <canvas class="game"></canvas>
    <script type="module" src="/src/main.ts"></script>
  </body>
</html>
```

### Le fichier main.js

Le fichier **main.js** est la racine de notre jeu. Remplaçons son contenu. Nous allons définir une scène Three.js contenant tous les éléments 3D, y compris le joueur, que nous allons bientôt définir. La scène comprend également une caméra que nous utiliserons avec le moteur de rendu pour rendre une image statique. Nous allons définir ces éléments dans les étapes suivantes.

```javascript
import * as THREE from "three";
import { Renderer } from "./Renderer";
import { Camera } from "./Camera";
import { player } from "./Player";
import "./style.css";

const scene = new THREE.Scene();
scene.add(player);

const camera = Camera();
player.add(camera);

const renderer = Renderer();
renderer.render(scene, camera);
```

### Le joueur

Commençons à ajouter les objets nécessaires pour rendre la première scène. Ajoutons une simple boîte pour représenter le joueur. Nous avons déjà ajouté le joueur à la scène dans le fichier principal, alors voyons comment définir ce joueur.

![Le joueur](https://cdn.hashnode.com/res/hashnode/image/upload/v1739804077435/9667f94f-5005-41f8-a6ed-faa6706f0be1.png align="center")

Dans ce fichier, nous écrivons une fonction qui crée un objet 3D et exporte une propriété contenant l'instance du joueur. Le joueur est un singleton. Il n'y a qu'un seul objet joueur dans le jeu, et chaque autre fichier peut y accéder via cette exportation.

```javascript
import * as THREE from "three";

export const player = Player();

function Player() {
  const player = new THREE.Group();

  const body = new THREE.Mesh(
    new THREE.BoxGeometry(15, 15, 20),
    new THREE.MeshLambertMaterial({ color: "white" })
  );
  body.position.z = 10;
  player.add(body);

  return player;
}
```

Initialement, le joueur sera une simple boîte. Pour dessiner un objet 3D, nous allons définir une géométrie et un matériau. La géométrie définit la forme de l'objet, et le matériau définit son apparence. Ici, nous utilisons une géométrie de boîte pour définir une boîte. La géométrie de boîte prend trois arguments : la largeur, la profondeur et la hauteur de la boîte le long des axes x, y et z.

Nous avons différentes options pour le matériau. La principale différence entre eux est la manière dont ils réagissent à la lumière, s'ils réagissent. Ici, nous utilisons **MeshLambertMaterial**, un matériau simple qui répond à la lumière. Nous définissons la propriété de couleur sur blanc.

![Différentes options de lumière](https://cdn.hashnode.com/res/hashnode/image/upload/v1739804142917/7b6a49e2-30df-40d8-bd4c-7ac1a2725931.png align="center")

Ensuite, nous enveloppons la géométrie et le matériau dans un maillage, que nous pouvons ajouter à la scène. Nous pouvons également positionner ce maillage en définissant ses positions X, Y et Z. Dans le cas d'une boîte, celles-ci définissent la position centrale. En définissant la position Z de cette boîte, nous l'élevons au-dessus du sol de la moitié de sa hauteur. Par conséquent, le bas de la boîte sera posé sur le sol.

Nous enveloppons également le maillage dans un élément de groupe. Ce n'est pas nécessaire à ce stade, mais avoir cette structure sera pratique lors de l'animation du joueur. En ce qui concerne l'animation du joueur, nous voulons séparer les mouvements horizontaux et verticaux. Nous voulons pouvoir suivre le joueur avec la caméra lorsqu'il se déplace, mais ne pas déplacer la caméra vers le haut et vers le bas lorsque le joueur saute. Nous déplacerons le groupe horizontalement le long du plan XY avec la caméra et déplacerons le maillage verticalement.

### La caméra

Maintenant, examinons les différentes options de caméra. Il existe deux principales options de caméra : la caméra perspective, comme vous pouvez le voir à gauche dans l'image ci-dessous, et la caméra orthographique, que vous pouvez voir à droite.

La caméra perspective est la caméra par défaut dans Three.js et est le type de caméra le plus courant dans tous les jeux vidéo. Elle crée une projection en perspective, qui fait paraître les objets plus éloignés plus petits et les objets juste devant la caméra plus grands.

D'autre part, la caméra orthographique crée des projections parallèles, ce qui signifie que les objets ont la même taille, quelle que soit leur distance par rapport à la caméra. Nous utiliserons ici une caméra orthographique pour donner à notre jeu un aspect plus arcade.

![Caméra perspective vs caméra orthographique](https://cdn.hashnode.com/res/hashnode/image/upload/v1739800656673/d2643544-b44c-418e-a475-2844e6626dbb.png align="center")

Dans Three.js, nous plaçons les objets 3D le long des axes X, Y et Z. Nous définissons le système de coordonnées de manière à ce que le sol soit sur le plan XY, de sorte que le joueur puisse se déplacer à gauche et à droite le long de l'axe x, vers l'avant et vers l'arrière le long de l'axe y, et lorsque le joueur saute, il montera le long de l'axe z.

Nous plaçons la caméra dans ce système de coordonnées à droite le long de l'axe x, derrière le joueur le long de l'axe y, et au-dessus du sol. Ensuite, la caméra regardera en arrière vers l'origine du système de coordonnées à la coordonnée 0,0,0, où le joueur sera placé initialement.

![Le système de coordonnées](https://cdn.hashnode.com/res/hashnode/image/upload/v1739803742848/d202d09f-1c1b-4246-be23-2a6f6af52423.png align="center")

Avec toute cette théorie en tête, définissons notre caméra. Nous créons un nouveau fichier pour la caméra et exportons la fonction caméra, qui retourne une caméra orthographique que nous utiliserons pour rendre la scène.

```javascript
import * as THREE from "three";

export function Camera() {
  const size = 300;
  const viewRatio = window.innerWidth / window.innerHeight;
  const width = viewRatio < 1 ? size : size * viewRatio;
  const height = viewRatio < 1 ? size / viewRatio : size;

  const camera = new THREE.OrthographicCamera(
    width / -2, // gauche
    width / 2, // droite
    height / 2, // haut
    height / -2, // bas
    100, // près
    900 // loin
  );

  camera.up.set(0, 0, 1);
  camera.position.set(300, -300, 300);
  camera.lookAt(0, 0, 0);

  return camera;
}
```

Pour définir une caméra, nous devons définir un frustum de caméra. Cela déterminera comment projeter les éléments 3D sur l'écran. Dans le cas d'une caméra orthographique, nous définissons une boîte. Tout ce qui se trouve dans la scène à l'intérieur de cette boîte sera projeté sur l'écran. Dans l'image ci-dessous, le point vert représente la position de la caméra et la boîte grise autour de la scène représente le frustum de la caméra.

![Le frustum de la caméra](https://cdn.hashnode.com/res/hashnode/image/upload/v1739804878454/3af6d9ba-1d35-4b98-8731-95af5889a1ed.png align="center")

Dans cette fonction, nous configurons le frustum de la caméra pour remplir la fenêtre du navigateur, et la largeur ou la hauteur sera de 300 unités, selon le rapport d'aspect. La plus petite valeur entre la largeur et la hauteur sera de 300 unités, et l'autre remplira l'espace disponible. Si la largeur est plus grande que la hauteur, alors la hauteur est de 300 unités. Si la hauteur est plus grande, alors la largeur est de 300 unités.

![Dimensionner la scène](https://cdn.hashnode.com/res/hashnode/image/upload/v1739805040485/c7b9aa02-3c5d-4a2e-a1ff-e9941ce83c39.png align="center")

Ensuite, nous définissons la position de la caméra. Nous déplaçons la caméra vers la droite le long de l'axe x avec 300 unités, puis derrière le joueur le long de l'axe y avec -300 unités, et enfin au-dessus du sol. Nous regardons également en arrière vers l'origine du système de coordonnées, vers la coordonnée 0,0,0, où le joueur est positionné initialement. Enfin, nous définissons quel axe pointe vers le haut. Ici, nous définissons l'axe z pour pointer vers le haut.

### Les lumières

Après avoir configuré la caméra, configurons les lumières. Il existe de nombreux types de lumières dans Three.js. Ici, nous allons utiliser une lumière ambiante et une lumière directionnelle.

Vous pouvez voir le résultat de la lumière ambiante uniquement sur le côté gauche de l'image ci-dessous. La lumière ambiante éclaircit toute la scène. Elle n'a pas de position ou de direction spécifique. Vous pouvez la considérer comme la lumière par une journée nuageuse lorsqu'il fait clair, mais qu'il n'y a pas d'ombres. La lumière ambiante est utilisée pour simuler la lumière indirecte.

![Lumière ambiante vs lumière directionnelle](https://cdn.hashnode.com/res/hashnode/image/upload/v1739800781538/9e140ef9-4133-4151-9fc5-b629504259a8.png align="center")

Maintenant, examinons la lumière directionnelle que vous pouvez voir à droite de l'image ci-dessus. Une lumière directionnelle a une position et une cible. Elle éclaire dans une direction spécifique avec des rayons lumineux parallèles. Même si elle a une position, vous pouvez plutôt la considérer comme le soleil qui brille de très loin. La position ici est plus pour définir la direction de la lumière, mais tous les autres rayons lumineux sont également parallèles à ce rayon lumineux. Vous pouvez donc la considérer comme le soleil.

![La lumière directionnelle brille avec des rayons lumineux parallèles](https://cdn.hashnode.com/res/hashnode/image/upload/v1739805160031/4742e1de-5dc0-4443-9716-af18581bfa1e.png align="center")

C'est pourquoi nous combinons une lumière ambiante (pour avoir une luminosité de base tout autour de la scène) avec une lumière directionnelle (pour illuminer des côtés spécifiques de nos objets avec une couleur plus vive).

Après avoir vu à quoi ressemblent les lumières, ajoutons une lumière ambiante et une lumière directionnelle à la scène dans notre fichier principal. Nous positionnons également la lumière directionnelle à gauche le long de l'axe x, derrière le joueur le long de l'axe y, et au-dessus du sol. Par défaut, la cible de la lumière directionnelle sera la coordonnée 0,0,0. Nous n'avons pas besoin de la définir.

```javascript
import * as THREE from "three";
import { Renderer } from "./Renderer";
import { Camera } from "./Camera";
import { player } from "./Player";
import "./style.css";

const scene = new THREE.Scene();
scene.add(player);

const ambientLight = new THREE.AmbientLight();
scene.add(ambientLight);

const dirLight = new THREE.DirectionalLight();
dirLight.position.set(-100, -100, 200);
scene.add(dirLight);

const camera = Camera();
player.add(camera);

const renderer = Renderer();
renderer.render(scene, camera);
```

Notez que nous ajoutons les lumières à la scène, mais nous ajoutons la caméra au joueur. Ainsi, lorsque nous animons le joueur, la caméra suivra le joueur.

### Le moteur de rendu

Nous avons défini beaucoup de choses, mais nous ne voyons toujours rien à l'écran. En tant que dernière pièce, nous devons avoir un moteur de rendu pour rendre la scène. Un moteur de rendu rend la scène 3D dans un élément canvas.

Dans cette fonction, nous obtenons l'élément canvas que nous avons défini dans le HTML et nous le définissons comme le contexte de dessin. Nous définissons également quelques paramètres supplémentaires. Nous rendons l'arrière-plan de la scène 3D transparent avec le drapeau alpha, définissons le rapport de pixels et définissons la taille du canvas pour remplir tout l'écran.

```javascript
import * as THREE from "three";

export function Renderer() {
  const canvas = document.querySelector("canvas.game");
  if (!canvas) throw new Error("Canvas non trouvé");

  const renderer = new THREE.WebGLRenderer({
    alpha: true,
    antialias: true,
    canvas: canvas,
  });
  renderer.setPixelRatio(window.devicePixelRatio);
  renderer.setSize(window.innerWidth, window.innerHeight);

  return renderer;
}
```

C'est ainsi que notre première scène se rassemble. Nous avons rendu une simple boîte.

## Comment rendre une carte

Maintenant, ajoutons tous les autres objets à la scène. Dans ce chapitre, nous allons définir la carte. La carte sera composée de plusieurs rangées, chacune décrite par des métadonnées. Chaque rangée peut être une forêt, une voie de voiture ou une voie de camion. Nous allons passer en revue chaque type et définir les objets 3D qui les représentent.

![Les différents types de rangées](https://cdn.hashnode.com/res/hashnode/image/upload/v1739803813951/3796e0c0-6f02-4c82-979b-a5192d8c3b8c.png align="center")

La carte peut être décomposée en rangées, et chaque rangée peut être décomposée en plusieurs tuiles. Le joueur se déplacera de tuile en tuile. Les arbres sont également placés sur une tuile distincte. Les voitures, en revanche, ne sont pas liées aux tuiles. Elles se déplacent librement dans la voie.

![Une rangée peut être décomposée en une tuile](https://cdn.hashnode.com/res/hashnode/image/upload/v1739803829719/38318821-8496-43d1-9b1c-a5b36d78af14.png align="center")

Nous définissons un fichier pour les constantes. Ici, nous définissons le nombre de tuiles dans chaque rangée. Dans ce cas, il y a 17 tuiles par rangée, allant de -8 à +8. Le joueur commencera au milieu à la tuile zéro.

```javascript
export const minTileIndex = -8;
export const maxTileIndex = 8;
export const tilesPerRow = maxTileIndex - minTileIndex + 1;
export const tileSize = 42;
```

### La rangée de départ

Tout d'abord, ajoutons la rangée de départ. Nous allons définir quelques composants que nous allons utiliser pour rendre la carte, et nous allons rendre la rangée initiale.

Créons un nouveau composant appelé Map. Ce fichier exposera les métadonnées de la carte et les objets 3D qui la représentent. Exportons un groupe appelé map. Ce conteneur contiendra tous les objets 3D pour chaque rangée. Bientôt, nous ajouterons ce groupe à la scène.

```javascript
import * as THREE from "three";
import { Grass } from "./Grass";

export const map = new THREE.Group();

const grass = Grass(0);
map.add(grass);
```

Ensuite, nous définissons le contenu de la carte. Plus tard, nous générerons les objets 3D en fonction des métadonnées et les utiliserons pour rendre la carte. Pour l'instant, appelons simplement la fonction Grass, qui retournera un autre groupe Three.js. Nous appelons la fonction grass avec l'index de la rangée, de sorte que le composant grass se positionnera en fonction de cet index de rangée. Ensuite, nous ajoutons le groupe retourné à la carte.

Maintenant, définissons le composant Grass. La fonction Grass retourne la fondation et le conteneur des rangées de forêt et est également utilisée pour la rangée de départ. Elle retourne un groupe contenant une boîte plate, large et verte. Les dimensions de cette boîte sont déterminées par les constantes **tileSize** et **tilesPerRow**. La boîte a également une certaine hauteur, de sorte qu'elle dépasse par rapport à la route, qui sera complètement plate.

```javascript
import * as THREE from "three";
import { tilesPerRow, tileSize } from "./constants";

export function Grass(rowIndex) {
  const grass = new THREE.Group();
  grass.position.y = rowIndex * tileSize;

  const foundation = new THREE.Mesh(
    new THREE.BoxGeometry(tilesPerRow * tileSize, tileSize, 3),
    new THREE.MeshLambertMaterial({ color: 0xbaf455 })
  );
  foundation.position.z = 1.5;
  grass.add(foundation);

  return grass;
}
```

L'herbe peut servir de conteneur pour les arbres de la rangée. C'est pourquoi nous enveloppons la boîte verte dans un groupe afin que plus tard, nous puissions également ajouter des enfants à ce groupe. Nous positionnons le groupe le long de l'axe y en fonction de l'index de la rangée que nous avons reçu du composant Map. Pour la voie initiale, celui-ci est zéro, mais comme nous allons avoir plusieurs voies, nous devons les placer selon cette position.

Maintenant que nous avons le conteneur de la carte et le composant d'herbe, nous pouvons enfin ajouter la carte à la scène.

```javascript
import * as THREE from "three";
import { Renderer } from "./Renderer";
import { Camera } from "./Camera";
import { player } from "./Player";
import { map } from "./Map";
import "./style.css";

const scene = new THREE.Scene();
scene.add(player);
scene.add(map);

const ambientLight = new THREE.AmbientLight();
scene.add(ambientLight);

const dirLight = new THREE.DirectionalLight();
dirLight.position.set(-100, -100, 200);
scene.add(dirLight);

const camera = Camera();
scene.add(camera);

const renderer = Renderer();
renderer.render(scene, camera);
```

### Comment ajouter une rangée de forêt

Maintenant que nous avons une forêt vide, ajoutons une autre rangée contenant des arbres. Nous définissons les métadonnées de la carte et rendons les rangées en fonction de ces métadonnées.

![Une rangée de forêt](https://cdn.hashnode.com/res/hashnode/image/upload/v1739806992172/139197f0-f2c1-4f11-aacf-f1fedeeaf9b0.png align="center")

De retour dans le composant Map, définissons les métadonnées de la carte. Les métadonnées sont un tableau d'objets qui contiennent des informations sur chaque rangée. Chaque rangée contiendra un type qui déterminera le type de la rangée et le reste des propriétés en fonction du type de rangée.

```javascript
import * as THREE from "three";
import { Grass } from "./Grass";

export const metadata = [
  {
    type: "forest",
    trees: [
      { tileIndex: -3, height: 50 },
      { tileIndex: 2, height: 30 },
      { tileIndex: 5, height: 50 },
    ],
  },
];

export const map = new THREE.Group();

const grass = Grass(0);
map.add(grass);
```

Les métadonnées pour une forêt incluent le type "forest" et une liste d'arbres. Chaque arbre a un index de tuile, qui représente sur quelle tuile il se trouve. Dans ce cas, nous avons 17 tuiles par rangée, allant de -8 à +8. Les arbres ont également une hauteur, qui est en fait la hauteur de la cime.

Pour rendre les rangées, nous parcourons ce tableau et générons des objets 3D pour chaque rangée en fonction du type de rangée. Pour le type forêt, il appelle à nouveau la fonction Grass, qui retournera un groupe Three.js. Nous appelons cette fonction Grass avec l'index de la rangée afin que la fonction Grass puisse se positionner le long de l'axe y. L'index de la rangée est décalé d'une unité par rapport à l'index du tableau car le premier élément des métadonnées deviendra la deuxième rangée juste après la rangée de départ, qui ne fait pas partie des métadonnées.

```javascript
import * as THREE from "three";
import { Grass } from "./Grass";
import { Tree } from "./Tree";

export const metadata = [
  {
    type: "forest",
    trees: [
      { tileIndex: -3, height: 50 },
      { tileIndex: 2, height: 30 },
      { tileIndex: 5, height: 50 },
    ],
  },
];

export const map = new THREE.Group();

const grass = Grass(0);
map.add(grass);

metadata.forEach((rowData, index) => {
  const rowIndex = index + 1;

  if (rowData.type === "forest") {
    const row = Grass(rowIndex);

    rowData.trees.forEach(({ tileIndex, height }) => {
      const three = Tree(tileIndex, height);
      row.add(three);
    });

    map.add(row);
  }
});
```

Les rangées de forêt ont également des arbres. Pour chaque élément du tableau des arbres, nous rendons un arbre. La fonction Tree retournera un objet 3D représentant l'arbre.

![Un arbre](https://cdn.hashnode.com/res/hashnode/image/upload/v1739807310182/40cbb90b-0356-4db5-97bb-cdbe0c8e8cb8.png align="center")

Nous transmettons à cette fonction l'index de la tuile que nous utiliserons pour positionner l'arbre dans la rangée et la hauteur. Nous ajoutons les arbres au groupe retourné par la fonction Grass, puis nous ajoutons le groupe entier retourné par la fonction Grass à la carte.

```javascript
import * as THREE from "three";
import { tileSize } from "../constants";

export function Tree(tileIndex, height) {
  const tree = new THREE.Group();
  tree.position.x = tileIndex * tileSize;

  const trunk = new THREE.Mesh(
    new THREE.BoxGeometry(15, 15, 20),
    new THREE.MeshLambertMaterial({ color: 0x4d2926 })
  );
  trunk.position.z = 10;
  tree.add(trunk);

  const crown = new THREE.Mesh(
    new THREE.BoxGeometry(30, 30, height),
    new THREE.MeshLambertMaterial({ color: 0x7aa21d })
  );
  crown.position.z = height / 2 + 20;
  tree.add(crown);

  return tree;
}
```

Puisque nous avons déjà ajouté la carte à la scène, la forêt apparaîtra à l'écran. Mais d'abord, nous devons définir comment rendre un arbre. Nous allons représenter un arbre avec deux boîtes. Nous allons avoir une boîte pour le tronc et une pour la cime.

Ce sont toutes deux des boîtes simples, comme nous en avions avant avec le joueur et aussi dans le composant Grass. Le tronc est placé sur le sol. Nous le soulevons le long de l'axe Z de la moitié de sa hauteur, et la cime est placée sur le tronc. La hauteur de la cime est également basée sur la propriété de hauteur. Ces deux maillages sont enveloppés ensemble dans un groupe, puis nous positionnons ce groupe le long de l'axe X en fonction de la propriété d'index de tuile.

### Voies de voitures

Maintenant, ajoutons un autre type de rangée : les voies de voitures. Le processus d'ajout de voies de voitures suivra une structure similaire. Nous définissons les métadonnées des voies, y compris les véhicules, puis nous les mappons en objets 3D.

![La voie de voitures](https://cdn.hashnode.com/res/hashnode/image/upload/v1739807532566/1c9cfdc9-2c45-476c-9ada-09f7abf79328.png align="center")

Dans le composant Map dans les métadonnées, remplaçons la première rangée par une voie de voitures. La voie de voitures contiendra une seule voiture rouge se déplaçant vers la gauche. Nous avons une propriété de direction, qui est un indicateur booléen. Si celle-ci est vraie, cela signifie que les voitures se déplacent vers la droite dans la voie, et si elle est fausse, alors les véhicules se déplacent vers la gauche. Nous avons également une propriété de vitesse, qui définit combien d'unités chaque véhicule prend chaque seconde.

Enfin, nous avons un tableau de véhicules. Chaque voiture aura un index de tuile initial, qui représente uniquement sa position initiale car les voitures se déplaceront plus tard. Chaque voiture aura également une propriété de couleur, qui est une valeur de couleur hexadécimale.

```javascript
import * as THREE from "three";
import { Grass } from "./Grass";
import { Tree } from "./Tree";

export const metadata = [
  {
    type: "car",
    direction: false,
    speed: 1,
    vehicles: [{ initialTileIndex: 2, color: 0xff0000 }],
  },
];

. . .
```

Maintenant, pour rendre ce type de voie, nous devons étendre notre logique pour supporter les voies de voitures. Nous ajoutons un autre bloc if qui est très similaire au rendu de la forêt. Dans le cas d'un type de voiture, nous appelons la fonction Road, qui retournera également un groupe Three.js. Nous appelons également cette fonction avec l'index de la rangée pour positionner le groupe selon la voie.

Ensuite, pour chaque élément du tableau des véhicules, nous créons un objet 3D représentant la voiture avec la fonction Car. Nous ajoutons les voitures au groupe retourné par la fonction Road, et nous ajoutons le groupe entier à la carte. Pour la fonction de voiture, nous transmettons également l'index de tuile initial que nous utiliserons pour positionner la voiture dans la rangée, la direction et la couleur.

```javascript
import * as THREE from "three";
import { Grass } from "./Grass";
import { Road } from "./Road";
import { Tree } from "./Tree";
import { Car } from "./Car";

export const metadata = [
  {
    type: "car",
    direction: false,
    speed: 1,
    vehicles: [{ initialTileIndex: 2, color: 0xff0000 }],
  },
];

export const map = new THREE.Group();

const grass = Grass(0);
map.add(grass);

metadata.forEach((rowData, index) => {
  const rowIndex = index + 1;

  if (rowData.type === "forest") {
    const row = Grass(rowIndex);

    rowData.trees.forEach(({ tileIndex, height }) => {
      const three = Tree(tileIndex, height);
      row.add(three);
    });

    map.add(row);
  }

  if (rowData.type === "car") {
    const row = Road(rowIndex);

    rowData.vehicles.forEach((vehicle) => {
      const car = Car(
        vehicle.initialTileIndex,
        rowData.direction,
        vehicle.color
      );
      row.add(car);
    });

    map.add(row);
  }
});
```

Les fonctions Road et Car sont nouvelles ici, alors examinons-les ensuite. La fonction Road retourne la fondation et le conteneur des voies de voitures et de camions. Similaire à la fonction Grass, elle retourne également un groupe contenant un plan gris.

![Le composant Road](https://cdn.hashnode.com/res/hashnode/image/upload/v1739807755293/e731a758-ac20-40f5-819b-82a5ae81e65f.png align="center")

La taille du plan est également déterminée par les constantes **tileSize** et **tilesPerRow**. Contrairement à la fonction grass, cependant, elle n'a aucune hauteur. Elle est complètement plate. La route servira également de conteneur pour les voitures et les camions dans la rangée, c'est pourquoi nous enveloppons le plan dans un groupe - afin que nous puissions ajouter des enfants à celui-ci.

```javascript
import * as THREE from "three";
import { tilesPerRow, tileSize } from "../constants";

export function Road(rowIndex) {
  const road = new THREE.Group();
  road.position.y = rowIndex * tileSize;

  const foundation = new THREE.Mesh(
    new THREE.PlaneGeometry(tilesPerRow * tileSize, tileSize),
    new THREE.MeshLambertMaterial({ color: 0x454a59 })
  );
  road.add(foundation);

  return road;
}
```

Maintenant, examinons la voiture. La fonction Car retourne un modèle de voiture 3D très simple.

![Une voiture](https://cdn.hashnode.com/res/hashnode/image/upload/v1739807975022/dc04c3c1-de94-49fd-ad85-ade999c8862a.png align="center")

Elle contient une boîte pour le corps et une boîte plus petite pour la partie supérieure. Nous avons également deux maillages de roues. Comme nous ne voyons jamais les voitures par en dessous, nous n'avons pas besoin de séparer les roues en gauche et droite. Nous pouvons simplement utiliser une longue boîte pour les roues avant et une autre pour les roues arrière.

```javascript
import * as THREE from "three";
import { tileSize } from "./constants";

export function Car(initialTileIndex, direction, color) {
  const car = new THREE.Group();
  car.position.x = initialTileIndex * tileSize;
  if (!direction) car.rotation.z = Math.PI;

  const main = new THREE.Mesh(
    new THREE.BoxGeometry(60, 30, 15),
    new THREE.MeshLambertMaterial({ color })
  );
  main.position.z = 12;
  car.add(main);

  const cabin = new THREE.Mesh(
    new THREE.BoxGeometry(33, 24, 12),
    new THREE.MeshLambertMaterial({ color: "white" })
  );
  cabin.position.x = -6;
  cabin.position.z = 25.5;
  car.add(cabin);

  const frontWheel = new THREE.Mesh(
    new THREE.BoxGeometry(12, 33, 12),
    new THREE.MeshLambertMaterial({ color: 0x333333 })
  );
  frontWheel.position.x = 18;
  frontWheel.position.z = 6;
  car.add(frontWheel);

  const backWheel = new THREE.Mesh(
    new THREE.BoxGeometry(12, 33, 12),
    new THREE.MeshLambertMaterial({ color: 0x333333 })
  );
  backWheel.position.x = -18;
  backWheel.position.z = 6;
  car.add(backWheel);

  return car;
}
```

Nous regroupons tous ces éléments, les positionnons en fonction de la propriété **initialTileIndex** et les tournons en fonction de la propriété **direction**. Si la voiture va vers la gauche, nous la faisons pivoter de 180°. Lorsque nous définissons les valeurs de rotation dans Three.js, nous devons les définir en radians, c'est pourquoi nous la définissons à Math.Pi, ce qui équivaut à 180°.

Vous pouvez également trouver une version plus étendue de la façon de dessiner cette voiture avec des textures [dans cet article](https://www.freecodecamp.org/news/three-js-tutorial/).

Sur la base des métadonnées, nous pouvons maintenant rendre une carte avec plusieurs rangées. Voici un exemple avec quelques voies supplémentaires. Bien sûr, n'hésitez pas à définir votre propre carte.

```javascript
. . .

export const metadata = [
  {
    type: "car",
    direction: false,
    speed: 188,
    vehicles: [
      { initialTileIndex: -4, color: 0xbdb638 },
      { initialTileIndex: -1, color: 0x78b14b },
      { initialTileIndex: 4, color: 0xa52523 },
    ],
  },
  {
    type: "forest",
    trees: [
      { tileIndex: -5, height: 50 },
      { tileIndex: 0, height: 30 },
      { tileIndex: 3, height: 50 },
    ],
  },
  {
    type: "car",
    direction: true,
    speed: 125,
    vehicles: [
      { initialTileIndex: -4, color: 0x78b14b },
      { initialTileIndex: 0, color: 0xbdb638 },
      { initialTileIndex: 5, color: 0xbdb638 },
    ],
  },
  {
    type: "forest",
    trees: [
      { tileIndex: -8, height: 30 },
      { tileIndex: -3, height: 50 },
      { tileIndex: 2, height: 30 },
    ],
  },
];

. . .
```

Cet article ne couvre pas les voies de camions, mais elles suivent une structure similaire. Le code pour cela peut être trouvé sur [JavaScriptGameTutorials.com](http://JavaScriptGameTutorials.com).

## Comment animer les voitures

Passons à l'animation des voitures dans leurs voies selon leur vitesse et leur direction. Pour déplacer les véhicules, nous devons d'abord pouvoir y accéder. Jusqu'à présent, nous les avons ajoutés à la scène, et théoriquement, nous pourrions parcourir la scène et déterminer quel objet représente un véhicule. Mais il est beaucoup plus facile de collecter leurs références dans nos métadonnées et d'y accéder via ces références.

Modifions la génération de la carte. Après avoir généré une voiture, nous ne les ajoutons pas seulement au groupe conteneur, mais nous sauvegardons également la référence avec leurs métadonnées. Après cela, nous pouvons aller aux métadonnées et accéder à chaque véhicule dans la scène.

```javascript
. . .

metadata.forEach((rowData, index) => {
  const rowIndex = index + 1;

  if (rowData.type === "forest") {
    const row = Grass(rowIndex);

    rowData.trees.forEach(({ tileIndex, height }) => {
      const three = Tree(tileIndex, height);
      row.add(three);
    });

    map.add(row);
  }

  if (rowData.type === "car") {
    const row = Road(rowIndex);

    rowData.vehicles.forEach((vehicle) => {
      const car = Car(
        vehicle.initialTileIndex,
        rowData.direction,
        vehicle.color
      );
      vehicle.ref = car; // Ajoute une référence à l'objet voiture dans les métadonnées
      row.add(car);
    });

    map.add(row);
  }
});
```

Ensuite, allons dans le fichier principal et définissons une fonction animate qui sera appelée à chaque frame d'animation. Pour l'instant, nous appelons uniquement la fonction **animateVehicles**, que nous allons définir ensuite. Plus tard, nous étendrons cette fonction avec une logique pour animer le joueur et pour avoir une détection de collision.

```javascript
import * as THREE from "three";
import { Renderer } from "./Renderer";
import { Camera } from "./Camera";
import { player } from "./Player";
import { map } from "./Map";
import { animateVehicles } from "./animateVehicles";
import "./style.css";

const scene = new THREE.Scene();
scene.add(player);
scene.add(map);

const ambientLight = new THREE.AmbientLight();
scene.add(ambientLight);

const dirLight = new THREE.DirectionalLight();
dirLight.position.set(-100, -100, 200);
scene.add(dirLight);

const camera = Camera();
scene.add(camera);

const renderer = Renderer();
renderer.setAnimationLoop(animate);

function animate() {
  animateVehicles();

  renderer.render(scene, camera);
}
```

Nous déplaçons également l'appel de rendu du moteur de rendu ici pour rendre la scène à chaque boucle d'animation. Pour appeler cette fonction à chaque frame, nous la passons à la fonction **setAnimationLoop** du moteur de rendu. Cela est similaire à **requestAnimationFrame** en JavaScript pur, sauf que cela s'appelle lui-même à la fin de la fonction, donc nous n'avons pas besoin de l'appeler à nouveau.

Maintenant, implémentons la fonction **animateVehicles**. Comme cette fonction fait partie de la fonction animate, cette fonction est appelée à chaque frame d'animation. Ici, nous utilisons une horloge Three.js pour calculer combien de temps s'est écoulé entre les frames d'animation. Ensuite, nous parcourons les métadonnées, prenons chaque véhicule de chaque voie de voiture ou de camion, et les déplaçons le long de l'axe x en fonction de leur vitesse, de leur direction et du temps écoulé.

```javascript
import * as THREE from "three";
import { metadata as rows } from "./Map";
import { minTileIndex, maxTileIndex, tileSize } from "./constants";

const clock = new THREE.Clock();

export function animateVehicles() {
  const delta = clock.getDelta();

  // Animer les voitures et les camions
  rows.forEach((rowData) => {
    if (rowData.type === "car" || rowData.type === "truck") {
      const beginningOfRow = (minTileIndex - 2) * tileSize;
      const endOfRow = (maxTileIndex + 2) * tileSize;

      rowData.vehicles.forEach(({ ref }) => {
        if (!ref) throw Error("Référence du véhicule manquante");

        if (rowData.direction) {
          ref.position.x =
            ref.position.x > endOfRow
              ? beginningOfRow
              : ref.position.x + rowData.speed * delta;
        } else {
          ref.position.x =
            ref.position.x < beginningOfRow
              ? endOfRow
              : ref.position.x - rowData.speed * delta;
        }
      });
    }
  });
}
```

Si une voiture atteint la fin de la voie, nous la faisons réapparaître à l'autre extrémité, selon sa direction. Cela crée une boucle infinie dans laquelle les voitures vont de gauche à droite ou de droite à gauche, selon leur direction. Une fois qu'elles atteignent la fin de la voie, elles recommencent depuis le début. Avec cette fonction, nous devrions avoir une scène où toutes les voitures se déplacent dans leurs voies.

![Les voitures se déplacent en boucle infinie](https://cdn.hashnode.com/res/hashnode/image/upload/v1739808359961/eca84295-09d7-463a-8d29-e5f8069bb673.png align="center")

## Comment déplacer le joueur

Maintenant, passons à l'animation du joueur. Déplacer le joueur sur la carte est plus complexe que déplacer les véhicules. Le joueur peut se déplacer dans toutes les directions, heurter des arbres ou se faire heurter par des voitures, et il ne devrait pas pouvoir sortir de la carte.

Dans ce chapitre, nous nous concentrons sur deux parties : collecter les entrées de l'utilisateur et exécuter les commandes de mouvement. Le mouvement du joueur n'est pas instantané - nous devons collecter les commandes de mouvement dans une file d'attente et les exécuter une par une. Nous allons collecter les entrées de l'utilisateur et les mettre dans une file d'attente.

### Collecte des entrées de l'utilisateur

Pour vérifier les commandes de mouvement, étendons le composant joueur avec un état. Nous suivons la position du joueur et la file d'attente de mouvement. Le joueur commence au milieu de la première rangée, et la file d'attente de mouvement est initialement vide.

Nous allons également exporter deux fonctions : **queueMove** ajoute la commande de mouvement à la fin de la file d'attente de mouvement, et la fonction **stepCompleted** supprime la première commande de mouvement de la file d'attente et met à jour la position du joueur en conséquence.

```javascript
. . .

export const position = {
  currentRow: 0,
  currentTile: 0,
};

export const movesQueue = [];

export function queueMove(direction) {
  movesQueue.push(direction);
}

export function stepCompleted() {
  const direction = movesQueue.shift();

  if (direction === "forward") position.currentRow += 1;
  if (direction === "backward") position.currentRow -= 1;
  if (direction === "left") position.currentTile -= 1;
  if (direction === "right") position.currentTile += 1;
}
```

Maintenant, nous pouvons ajouter des écouteurs d'événements pour les événements de clavier afin d'écouter les touches fléchées. Elles appellent toutes la fonction **queueMove** du joueur, que nous venons de définir pour le joueur avec la direction correspondante.

```javascript
import { queueMove } from "./Player";

window.addEventListener("keydown", (event) => {
  if (event.key === "ArrowUp") {
    queueMove("forward");
  } else if (event.key === "ArrowDown") {
    queueMove("backward");
  } else if (event.key === "ArrowLeft") {
    queueMove("left");
  } else if (event.key === "ArrowRight") {
    queueMove("right");
  }
});
```

Après avoir défini les écouteurs d'événements, nous devons également les importer dans le fichier principal pour qu'ils fonctionnent.

```javascript
import * as THREE from "three";
import { Renderer } from "./Renderer";
import { Camera } from "./Camera";
import { player } from "./Player";
import { map } from "./Map";
import { animateVehicles } from "./animateVehicles";
import "./style.css";
import "./collectUserInput"; // Importer les écouteurs d'événements

. . .
```

### Exécution des commandes de mouvement

Jusqu'à présent, nous avons collecté les entrées de l'utilisateur et mis chaque commande dans le tableau **movesQueue** dans le composant joueur. Maintenant, il est temps d'exécuter ces commandes une par une et d'animer le joueur.

Créons une nouvelle fonction appelée **animatePlayer**. Son objectif principal est de prendre chaque commande de mouvement de la **moveQueue** une par une, de calculer la progression du joueur vers l'exécution d'un pas, et de positionner le joueur en conséquence.

![Le mouvement du joueur](https://cdn.hashnode.com/res/hashnode/image/upload/v1739808997988/8adb70d2-bf5d-4e65-8ed9-29e8f297b487.png align="center")

Cette fonction anime le joueur image par image. Elle fera également partie de la fonction animate. Nous utilisons également une horloge de mouvement séparée qui mesure chaque pas individuellement. Nous passons false au constructeur de l'horloge pour qu'elle ne démarre pas automatiquement. L'horloge ne démarre qu'au début d'un pas. À chaque image d'animation, nous vérifions d'abord s'il reste des pas à faire, et s'il en reste et que nous ne traitons pas actuellement un pas, alors nous pouvons démarrer l'horloge. Une fois l'horloge en marche, nous animons le joueur de tuile en tuile avec chaque pas.

```javascript
import * as THREE from "three";
import { movesQueue, stepCompleted } from "./Player";

const moveClock = new THREE.Clock(false);

export function animatePlayer() {
  if (!movesQueue.length) return;

  if (!moveClock.running) moveClock.start();

  const stepTime = 0.2; // Secondes nécessaires pour faire un pas
  const progress = Math.min(1, moveClock.getElapsedTime() / stepTime);

  setPosition(progress);

  // Une fois qu'un pas est terminé
  if (progress >= 1) {
    stepCompleted();
    moveClock.stop();
  }
}

. . .
```

Nous utilisons l'horloge de mouvement pour calculer la progression entre les deux tuiles. L'indicateur de progression peut être un nombre entre zéro et un. Zéro signifie que le joueur est encore au début du pas, et un signifie qu'il est arrivé à sa nouvelle position.

À chaque image d'animation, nous appelons la fonction **setPosition** pour définir la position du joueur en fonction de la progression. Une fois que nous avons terminé un pas, nous appelons la fonction **stepCompleted** pour mettre à jour la position du joueur et arrêter l'horloge. S'il reste des commandes de mouvement dans la **movesQueue**, l'horloge redémarrera dans l'image d'animation suivante.

Maintenant que nous savons comment calculer la progression pour chaque pas, examinons comment définir la position du joueur en fonction de la progression. Le joueur sautera de tuile en tuile. Décomposons cela en deux parties : les composantes horizontale et verticale du mouvement.

Le joueur se déplace de la tuile actuelle à la tuile suivante dans la direction de la commande de mouvement. Nous calculons la position de départ et d'arrivée du joueur en fonction de la tuile actuelle et de la direction de la commande de mouvement. Ensuite, nous utilisons une interpolation linéaire avec une fonction utilitaire que Three.js fournit. Cela interpolera entre les positions de départ et d'arrivée en fonction de la progression.

```javascript
import * as THREE from "three";
import {
  player,
  position,
  movesQueue,
  stepCompleted,
} from "./components/Player";
import { tileSize } from "./constants";

. . .

function setPosition(progress) {
  const startX = position.currentTile * tileSize;
  const startY = position.currentRow * tileSize;
  let endX = startX;
  let endY = startY;

  if (movesQueue[0] === "left") endX -= tileSize;
  if (movesQueue[0] === "right") endX += tileSize;
  if (movesQueue[0] === "forward") endY += tileSize;
  if (movesQueue[0] === "backward") endY -= tileSize;

  player.position.x = THREE.MathUtils.lerp(startX, endX, progress);
  player.position.y = THREE.MathUtils.lerp(startY, endY, progress);
  player.children[0].position.z = Math.sin(progress * Math.PI) * 8 + 10;
}
```

Pour la composante verticale, nous utilisons une fonction sinus pour donner l'impression de sauter. Nous mappons essentiellement la progression à la première partie d'une onde sinusoïdale.

Ci-dessous, vous pouvez voir à quoi ressemble une onde sinusoïdale. Elle va de 0 à 2 Pi. Donc si vous multipliez la valeur de progression, qui va de 0 à 1 avec Pi, alors la progression sera mappée dans la première moitié de cette onde sinusoïdale. La fonction sinus donnera alors une valeur entre zéro et un.

Pour faire paraître le saut plus haut, nous pouvons multiplier cela par une valeur. Dans ce cas, nous multiplions le résultat de la fonction sinus par huit, de sorte qu'en conséquence, le joueur aura un saut où la hauteur maximale du saut sera de huit unités.

Nous devons également ajouter la position Z originale à la valeur - sinon, le joueur s'enfoncera à moitié dans le sol après le premier pas.

![Pour le mouvement vertical, nous utilisons une onde sinusoïdale](https://cdn.hashnode.com/res/hashnode/image/upload/v1739810397620/89119f6e-ced5-4cdb-8254-96fbf66479ed.png align="center")

Maintenant que nous avons défini la fonction **animatePlayer**, ajoutons-la à la boucle d'animation.

```javascript
import * as THREE from "three";
import { Renderer } from "./Renderer";
import { Camera } from "./Camera";
import { DirectionalLight } from "./DirectionalLight";
import { player } from "./Player";
import { map, initializeMap } from "./Map";
import { animateVehicles } from "./animateVehicles";
import { animatePlayer } from "./animatePlayer";
import "./style.css";
import "./collectUserInput";

. . .

function animate() {
  animateVehicles();
  animatePlayer();

  renderer.render(scene, camera);
}
```

Si vous avez tout fait correctement, le joueur devrait pouvoir se déplacer sur le plateau de jeu, se déplaçant vers l'avant, l'arrière, la gauche et la droite. Mais nous n'avons pas encore ajouté de détection de collision. Jusqu'à présent, le joueur peut se déplacer à travers les arbres et les véhicules et même sortir du plateau de jeu. Corrigons ces problèmes dans les étapes suivantes.

### Restriction du mouvement du joueur

Assurons-nous que le joueur ne peut pas se retrouver dans une position invalide. Nous vérifierons si un mouvement est valide en calculant où il emmènera le joueur. Si le joueur se retrouverait dans une position en dehors de la carte ou sur une tuile occupée par un arbre, nous ignorerons cette commande de mouvement.

![Calculer où le joueur va se retrouver](https://cdn.hashnode.com/res/hashnode/image/upload/v1739810555283/310afd32-6e5a-4143-bbe2-e0da558bd6d7.png align="center")

Tout d'abord, nous devons calculer où le joueur se retrouverait s'il effectuait un mouvement particulier. Chaque fois que nous ajoutons un nouveau mouvement à la file d'attente, nous devons calculer où le joueur se retrouverait s'il effectuait tous les mouvements dans la file d'attente et prendre la commande de mouvement actuelle. Nous créons une fonction utilitaire qui prend la position actuelle du joueur et un tableau de mouvements et retourne la position finale du joueur.

Par exemple, si la position actuelle du joueur est 0,0, restant au milieu de la première rangée, et que les mouvements sont vers l'avant et vers la gauche, alors la position finale sera la rangée 1, la tuile -1.

```javascript
export function calculateFinalPosition(currentPosition, moves) {
  return moves.reduce((position, direction) => {
    if (direction === "forward")
      return {
        rowIndex: position.rowIndex + 1,
        tileIndex: position.tileIndex,
      };
    if (direction === "backward")
      return {
        rowIndex: position.rowIndex - 1,
        tileIndex: position.tileIndex,
      };
    if (direction === "left")
      return {
        rowIndex: position.rowIndex,
        tileIndex: position.tileIndex - 1,
      };
    if (direction === "right")
      return {
        rowIndex: position.rowIndex,
        tileIndex: position.tileIndex + 1,
      };
    return position;
  }, currentPosition);
}
```

Maintenant que nous avons cette fonction utilitaire pour calculer où le joueur se retrouvera après avoir effectué un mouvement, créons une autre fonction utilitaire pour calculer si le joueur se retrouverait dans une position valide ou invalide. Dans cette fonction, nous utilisons la fonction **calculateFinalPosition** que nous venons de créer. Ensuite, nous vérifierons si le joueur se retrouverait en dehors de la carte ou sur une tuile occupée par un arbre.

![Vérifier si le joueur heurte un arbre](https://cdn.hashnode.com/res/hashnode/image/upload/v1739810684106/71c45122-b10c-4623-b575-184c1cf1fecb.png align="center")

Si le mouvement est invalide, nous retournons false. Tout d'abord, nous vérifions si la position finale est avant la rangée de départ ou si le numéro de tuile est en dehors de la plage des tuiles. Ensuite, nous vérifions les métadonnées de la rangée dans laquelle le joueur se retrouvera. Ici, l'index est décalé d'une unité car les métadonnées de la rangée n'incluent pas la rangée de départ. Si nous nous retrouvons dans une rangée de forêt, nous vérifions si un arbre occupe la tuile vers laquelle nous nous déplaçons. Si l'une de ces conditions est vraie, nous retournons false.

```javascript
import { calculateFinalPosition } from "./calculateFinalPosition";
import { minTileIndex, maxTileIndex } from "./constants";
import { metadata as rows } from "./Map";

export function endsUpInValidPosition(currentPosition, moves) {
  // Calculer où le joueur se retrouverait après le mouvement
  const finalPosition = calculateFinalPosition(
    currentPosition,
    moves
  );

  // Détecter si nous atteignons le bord du plateau
  if (
    finalPosition.rowIndex === -1 ||
    finalPosition.tileIndex === minTileIndex - 1 ||
    finalPosition.tileIndex === maxTileIndex + 1
  ) {
    // Mouvement invalide, ignorer la commande de mouvement
    return false;
  }

  // Détecter si nous heurtons un arbre
  const finalRow = rows[finalPosition.rowIndex - 1];
  if (
    finalRow &&
    finalRow.type === "forest" &&
    finalRow.trees.some(
      (tree) => tree.tileIndex === finalPosition.tileIndex
    )
  ) {
    // Mouvement invalide, ignorer la commande de mouvement
    return false;
  }

  return true;
}
```

Enfin, étendons la fonction **queueMove** du joueur avec la fonction **endsUpInValidPosition** pour vérifier si un mouvement est valide. Si la fonction **endsUpInValidPosition** retourne false, nous ne pouvons pas faire ce pas. Dans ce cas, nous retournons tôt de la fonction avant que le mouvement ne soit ajouté au tableau **movesQueue**. Ainsi, nous ignorons le mouvement.

```javascript
import * as THREE from "three";
import { endsUpInValidPosition } from "./endsUpInValidPosition";

. . .

export function queueMove(direction) {
  const isValidMove = endsUpInValidPosition(
    {
      rowIndex: position.currentRow,
      tileIndex: position.currentTile,
    },
    [...movesQueue, direction]
  );

  if (!isValidMove) return; // Retourner si le mouvement est invalide

  movesQueue.push(direction);
}

. . .
```

De cette manière, comme vous pouvez le voir, vous pouvez vous déplacer sur la carte - mais vous ne pouvez jamais vous déplacer avant la première rangée, vous ne pouvez pas aller trop loin à gauche ou trop loin à droite, et vous ne pouvez plus non plus traverser un arbre.

## Détection de collision

Pour terminer le jeu, ajoutons une détection de collision. Nous vérifions si le joueur est heurté par un véhicule, et si c'est le cas, nous affichons une fenêtre d'alerte.

![Calcul des boîtes englobantes pour la détection de collision](https://cdn.hashnode.com/res/hashnode/image/upload/v1739826639155/1497d588-bf60-4fdc-a185-a01a781beafb.png align="center")

Définissons une autre fonction pour définir la détection de collision. Nous vérifions si le joueur entre en intersection avec l'un des véhicules. Dans cette fonction, nous vérifions dans quelle rangée le joueur se trouve actuellement. L'index est décalé d'une unité car les métadonnées de la rangée n'incluent pas la rangée de départ. Si le joueur est dans la rangée de départ, nous obtenons undefined. Nous ignorons ce cas. Si le joueur est dans une voie de voiture ou de camion, nous parcourons les véhicules de la rangée et vérifions s'ils entrent en intersection avec le joueur. Nous créons des boîtes englobantes pour le joueur et le véhicule afin de vérifier les intersections.

```javascript
import * as THREE from "three";
import { metadata as rows } from "./Map";
import { player, position } from "./Player";

export function hitTest() {
  const row = rows[position.currentRow - 1];
  if (!row) return;

  if (row.type === "car" || row.type === "truck") {
    const playerBoundingBox = new THREE.Box3();
    playerBoundingBox.setFromObject(player);

    row.vehicles.forEach(({ ref }) => {
      if (!ref) throw Error("Référence du véhicule manquante");

      const vehicleBoundingBox = new THREE.Box3();
      vehicleBoundingBox.setFromObject(ref);

      if (playerBoundingBox.intersectsBox(vehicleBoundingBox)) {
        window.alert("Game over!");
        window.location.reload();
      }
    });
  }
}
```

Si les boîtes englobantes entrent en intersection, nous affichons une alerte. Une fois que l'utilisateur clique sur OK dans l'alerte, nous rechargeons la page. Nous appelons cette fonction dans la fonction **animate**, qui l'exécutera à chaque frame.

```javascript
import * as THREE from "three";
import { Renderer } from "./Renderer";
import { Camera } from "./Camera";
import { player } from "./Player";
import { map } from "./Map";
import { animateVehicles } from "./animateVehicles";
import { animatePlayer } from "./animatePlayer";
import { hitTest } from "./hitTest";
import "./style.css";
import "./collectUserInput";

. . .

function animate() {
  animateVehicles();
  animatePlayer();
  hitTest(); // Ajouter la détection de collision

  renderer.render(scene, camera);
}
```

## Prochaines étapes

Félicitations, vous êtes arrivé à la fin de ce tutoriel, et nous avons couvert toutes les principales fonctionnalités du jeu. Nous avons rendu une carte, animé les véhicules, ajouté la gestion des événements pour le joueur et ajouté la détection de collision.

J'espère que vous avez pris beaucoup de plaisir à créer ce jeu. Ce jeu, bien sûr, est loin d'être parfait, et il y a diverses améliorations que vous pouvez apporter si vous souhaitez continuer à travailler dessus.

Vous pouvez trouver le tutoriel étendu avec des démonstrations interactives sur [JavaScriptGameTutorials.com](http://JavaScriptGameTutorials.com). Là, nous couvrons également comment ajouter des ombres et des voies de camions et comment générer un nombre infini de rangées lorsque le joueur avance. Nous ajoutons également des éléments d'interface utilisateur pour les contrôles et l'indicateur de score, et nous ajoutons un écran de résultat avec un bouton pour réinitialiser le jeu.

Alternativement, vous pouvez trouver le tutoriel étendu sur [YouTube](https://www.youtube.com/watch?v=vNr3_hQ3Bws&ab_channel=HunorM%C3%A1rtonBorb%C3%A9ly).

%[https://www.youtube.com/watch?v=vNr3_hQ3Bws&ab_channel=HunorM%C3%A1rtonBorb%C3%A9ly]