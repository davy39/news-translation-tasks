---
title: Comment coder un clone du jeu Crossy Road avec React Three Fiber
subtitle: ''
author: Hunor Márton Borbély
co_authors: []
series: null
date: '2025-02-26T21:20:27.097Z'
originalURL: https://freecodecamp.org/news/how-to-code-a-crossy-road-game-clone-with-react-three-fiber
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1740599557930/dcbb214e-c6d2-400e-8b2a-25fd81ac3c47.png
tags:
- name: React
  slug: reactjs
- name: Game Development
  slug: game-development
- name: reactthreefiber
  slug: reactthreefiber
seo_title: Comment coder un clone du jeu Crossy Road avec React Three Fiber
seo_desc: In this tutorial, you’ll learn how to create a clone of the mobile game
  Crossy Road with React Three Fiber. In a previous tutorial, I taught you how to
  build this game using Three.js and vanilla JavaScript. And here, you’ll learn how
  to make the same...
---

Dans ce tutoriel, vous apprendrez à créer un clone du jeu mobile Crossy Road avec React Three Fiber. Dans un [tutoriel précédent](https://www.freecodecamp.org/news/how-to-code-a-crossy-road-game-clone-with-threejs/), je vous ai appris à construire ce jeu en utilisant Three.js et JavaScript vanilla. Et ici, vous apprendrez à faire le même jeu avec React Three Fiber à la place.

Le but de ce jeu est de déplacer un personnage à travers un chemin sans fin d'obstacles statiques et mobiles. Vous devez contourner les arbres et éviter de vous faire frapper par les voitures.

Il y a beaucoup de choses à couvrir dans ce tutoriel : nous commencerons par configurer la scène, la caméra et les lumières. Ensuite, vous apprendrez à dessiner le joueur et la carte avec les arbres et les voitures. Nous couvrirons également comment animer les véhicules, et nous ajouterons des gestionnaires d'événements pour déplacer le joueur sur la carte. Enfin, nous ajouterons la détection de collision entre les voitures et le joueur.

Cet article est une version abrégée du tutoriel Crossy Road de mon site [JavaScriptGameTutorials.com](https://javascriptgametutorials.com/). Le tutoriel étendu est également disponible sous forme de vidéo sur [YouTube](https://www.youtube.com/watch?v=ccYrSACDNsw&ab_channel=HunorM%C3%A1rtonBorb%C3%A9ly).

## Table des matières

1. [React Three Fiber vs Three.js](#heading-react-three-fiber-vs-threejs)

2. [Comment installer le jeu](#heading-installation)

3. [Comment rendre une carte](#heading-comment-rendre-une-carte)

4. [Comment animer les voitures](#heading-comment-animer-les-voitures)

5. [Comment déplacer le joueur](#heading-comment-deplacer-le-joueur)

6. [Détection de collision](#heading-detection-de-collision)

7. [Prochaines étapes](#heading-prochaines-etapes)

## React Three Fiber vs Three.js

Vous vous demandez peut-être ce qu'est React Three Fiber et comment il se compare à Three.js ? React Three Fiber utilise Three.js sous le capot, mais il nous donne une manière différente de construire notre jeu avec React. Il est également plus facile à configurer, car React Three Fiber vient avec des paramètres par défaut sensés pour des choses comme la caméra.

React est devenu un framework front-end de premier plan, et React Three Fiber vous permet de définir une scène 3D en utilisant les modèles bien établis de React. Vous pouvez décomposer le jeu en composants React et utiliser des hooks pour l'animation, la gestion des événements et la détection de collision.

Sous le capot, React Three Fiber utilise toujours des objets Three.js. En fait, dans certains cas, nous accéderons aux objets Three.js sous-jacents et les manipulerons directement pour de meilleures performances. Mais lorsque nous construisons le jeu, nous utilisons les modèles familiers de React.

Alors, lequel devriez-vous utiliser ? Si vous êtes déjà familiarisé avec React, alors React Three Fiber pourrait donner plus de structure à vos jeux. Et après avoir lu ce tutoriel et construit le jeu avec moi, vous serez mieux équipé pour choisir.

## **Comment installer le jeu**

Dans ce chapitre, nous allons configurer la toile de dessin, la caméra et les lumières, et rendre une boîte représentant notre joueur.

### **Initialisation du projet**

Je recommande d'utiliser Vite pour initialiser le projet. Pour ce faire, allez dans votre terminal et tapez `npm create vite`, ce qui créera un projet initial pour vous.

Lors de la génération du projet, sélectionnez **React** (car React Three Fiber utilise React).

```bash
# Créer une application
npm create vite my-crossy-road-game
# Sélectionner React comme framework
# Sélectionner JavaScript

# Naviguer vers le projet
cd my-crossy-road-game

# Mettre à jour react et react-dom
npm install react@latest react-dom@latest

# Installer les dépendances
npm install three @react-three/fiber

# Démarrer le serveur de développement
npm run dev
```

Au moment de la rédaction de cet article, Vite utilisera React 18 par défaut. Pendant ce temps, React 19 est sorti, et la dernière version de React Three Fiber n'est compatible qu'avec React 19. Alors mettons à jour React et react-dom avec `npm install react@latest react-dom@latest`.

Après avoir initialisé le projet, naviguez vers le dossier du projet et installez les dépendances supplémentaires. Nous utiliserons Three.js et React Three Fiber avec `npm install three @react-three/fiber`.

Enfin, vous pouvez aller dans le terminal et taper `npm run dev` pour démarrer un serveur de développement. Ainsi, vous pouvez voir en direct le résultat de votre codage dans le navigateur.

### **La toile de dessin**

Créons un nouveau composant appelé `src/Game.jsx`. Ce sera la racine de notre jeu.

Le composant `Scene` contiendra la toile de dessin, la caméra et les lumières. Nous passerons le composant `Player` comme son enfant, qui rendra une boîte. Plus tard, nous ajouterons le composant `Map`, y compris les arbres, les voitures et les camions. Ce composant est également l'endroit où l'indicateur de score et les contrôles viendront plus tard.

```javascript
import { Scene } from "./components/Scene";
import { Player } from "./components/Player";

export default function Game() {
  return (
    <Scene>
      <Player />
    </Scene>
  );
}
```

### **Le fichier main.jsx**

Pour utiliser le nouveau composant `Game` comme notre racine, nous devons remplacer le composant `App` original dans le fichier `src/main.jsx`.

Cela vous donnera une erreur pour l'instant car nous n'avons pas implémenté les composants `Scene` et `Player`.

Maintenant que nous avons remplacé le composant `App`, nous pouvons supprimer l'original `App.jsx`, `App.css` et le dossier `assets`.

```javascript
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import Game from "./Game.jsx";

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <Game />
  </StrictMode>
);
```

Mettons également à jour le fichier `index.css` pour nous assurer que notre toile de dessin remplit tout l'écran.

```javascript
body {
  margin: 0;
  display: flex;
  min-height: 100vh;
}

#root {
  width: 100%;
}
```

### **Le joueur**

Commençons à ajouter les objets nécessaires pour rendre la première scène. Ajoutons une simple boîte pour représenter le joueur. Nous avons déjà ajouté le joueur à la scène, alors voyons comment définir ce joueur.

![Le joueur](https://cdn.hashnode.com/res/hashnode/image/upload/v1739804077435/9667f94f-5005-41f8-a6ed-faa6706f0be1.png align="left")

Le joueur sera une simple boîte. Pour dessiner un objet 3D, nous définirons une géométrie et un matériau. La géométrie définit la forme de l'objet, et le matériau définit son apparence. Ici, nous utilisons une géométrie de boîte pour définir une boîte. La géométrie de boîte prend trois arguments : la largeur, la profondeur et la hauteur de la boîte le long des axes x, y et z.

```javascript
export function Player() {
  return (
    <group>
      <mesh position={[0, 0, 10]}>
        <boxGeometry args={[15, 15, 20]} />
        <meshLambertMaterial color={0xffffff} />
      </mesh>
    </group>
  );
}
```

Nous avons différentes options pour le matériau. La principale différence entre eux est la manière dont ils réagissent à la lumière, s'ils réagissent. Ici, nous utilisons `meshLambertMaterial`, un matériau simple qui répond à la lumière. Nous définissons la propriété de couleur sur blanc.

![Différentes options de lumière](https://cdn.hashnode.com/res/hashnode/image/upload/v1739804142917/7b6a49e2-30df-40d8-bd4c-7ac1a2725931.png align="left")

Ensuite, nous enveloppons la géométrie et le matériau dans un mesh, que nous pouvons ajouter à la scène. Nous pouvons également positionner ce mesh en définissant ses positions X, Y et Z. Dans le cas d'une boîte, celles-ci définissent la position centrale. En définissant la position Z de cette boîte, nous l'élevons au-dessus du sol de la moitié de sa hauteur. Par conséquent, le bas de la boîte sera posé sur le sol.

Nous enveloppons également le mesh dans un élément de groupe. Ce n'est pas nécessaire à ce stade, mais avoir cette structure sera pratique lors de l'animation du joueur. En ce qui concerne l'animation du joueur, nous voulons séparer le mouvement horizontal et vertical. Nous voulons pouvoir suivre le joueur avec la caméra lorsqu'il se déplace, mais ne pas déplacer la caméra de haut en bas lorsque le joueur saute. Nous déplacerons le groupe horizontalement le long du plan XY avec la caméra et déplacerons le mesh verticalement.

### **La caméra**

Maintenant, examinons les différentes options de caméra. Il y a deux options principales pour la caméra : la caméra perspective, comme vous pouvez le voir à gauche dans l'image ci-dessous, et la caméra orthographique, que vous pouvez voir à droite.

La caméra perspective est la caméra par défaut dans Three.js et est le type de caméra le plus courant dans tous les jeux vidéo. Elle crée une projection en perspective, qui fait que les choses plus éloignées semblent plus petites et les choses juste devant la caméra semblent plus grandes.

D'autre part, la caméra orthographique crée des projections parallèles, ce qui signifie que les objets ont la même taille, quelle que soit leur distance par rapport à la caméra. Nous utiliserons une caméra orthographique ici pour donner à notre jeu un look plus arcade.

![Caméra perspective vs caméra orthographique](https://cdn.hashnode.com/res/hashnode/image/upload/v1739800656673/d2643544-b44c-418e-a475-2844e6626dbb.png align="left")

Dans Three.js, nous plaçons les objets 3D le long des axes X, Y et Z. Nous définissons le système de coordonnées de manière à ce que le sol soit sur le plan XY, de sorte que le joueur puisse se déplacer à gauche et à droite le long de l'axe x, vers l'avant et vers l'arrière le long de l'axe y, et lorsque le joueur saute, il montera le long de l'axe z.

Nous plaçons la caméra dans ce système de coordonnées à droite le long de l'axe x, derrière le joueur le long de l'axe y, et au-dessus du sol. Ensuite, la caméra regardera en arrière vers l'origine du système de coordonnées vers la coordonnée 0,0,0, où le joueur sera placé initialement.

![Le système de coordonnées](https://cdn.hashnode.com/res/hashnode/image/upload/v1739803742848/d202d09f-1c1b-4246-be23-2a6f6af52423.png align="left")

### **Les lumières**

Il existe de nombreux types de lumières dans Three.js. Ici, nous allons utiliser une lumière ambiante et une lumière directionnelle.

Vous pouvez voir le résultat de la lumière ambiante uniquement sur le côté gauche de l'image ci-dessous. La lumière ambiante éclaire toute la scène. Elle n'a pas de position ou de direction spécifique. Vous pouvez la considérer comme la lumière par une journée nuageuse lorsqu'il fait clair, mais qu'il n'y a pas d'ombres. La lumière ambiante est utilisée pour simuler la lumière indirecte.

![Lumière ambiante vs lumière directionnelle](https://cdn.hashnode.com/res/hashnode/image/upload/v1739800781538/9e140ef9-4133-4151-9fc5-b629504259a8.png align="left")

Maintenant, regardons la lumière directionnelle que vous pouvez voir à droite de l'image ci-dessus. Une lumière directionnelle a une position et une cible. Elle éclaire dans une direction spécifique avec des rayons lumineux parallèles. Même si elle a une position, vous pouvez plutôt la considérer comme le soleil qui brille de très loin. La position ici est plus pour définir la direction de la lumière, mais tous les autres rayons lumineux sont également parallèles à ce rayon lumineux. Vous pouvez donc la considérer comme le soleil.

![La lumière directionnelle brille avec des rayons lumineux parallèles](https://cdn.hashnode.com/res/hashnode/image/upload/v1739805160031/4742e1de-5dc0-4443-9716-af18581bfa1e.png align="left")

C'est pourquoi nous combinons une lumière ambiante (pour avoir une luminosité de base partout dans la scène) avec une lumière directionnelle (pour illuminer des côtés spécifiques de nos objets avec une couleur plus vive).

### **La scène**

Après avoir passé en revue les différentes options de caméra et de lumière, mettons-les ensemble dans le composant `Scene`. Nous configurons la toile avec une caméra orthographique et des lumières.

```javascript
import { Canvas } from "@react-three/fiber";

export const Scene = ({ children }) => {
  return (
    <Canvas
      orthographic={true}
      camera={{
        up: [0, 0, 1],
        position: [300, -300, 300],
      }}
    >
      <ambientLight />
      <directionalLight position={[-100, -100, 200]} />
      {children}
    </Canvas>
  );
};
```

Nous utilisons le composant `Canvas` de `@react-three/fiber`. Ce composant contiendra tous les objets 3D de la scène, donc il a une prop `children`.

Nous définissons la prop `orthographic` à `true` pour utiliser une caméra orthographique et la prop `camera` pour définir la position et l'orientation de la caméra. Les props de la caméra nécessitent des vecteurs ou des coordonnées définis par les valeurs x, y et z.

La prop `up` définit le vecteur haut de la caméra. Nous la définissons à `[0, 0, 1]` pour faire de l'axe z le vecteur haut. La prop `position` définit la position de la caméra. Nous déplaçons la caméra vers la droite le long de l'axe x, vers l'arrière le long de l'axe y et vers le haut le long de l'axe z.

Nous ajoutons également les lumières. Nous pouvons utiliser des éléments spécifiques à React Three Fiber dans l'élément `Canvas`. Nous ajoutons les composants `ambientLight` et `directionalLight` pour ajouter des lumières à la scène. Nous positionnons la lumière directionnelle vers la gauche le long de l'axe x, vers l'arrière le long de l'axe y et vers le haut le long de l'axe z.

C'est ainsi que notre première scène se rassemble. Nous avons rendu une simple boîte.

## **Comment rendre une carte**

Maintenant, ajoutons tous les autres objets à la scène. Dans ce chapitre, nous définirons la carte. La carte sera composée de plusieurs rangées, chacune décrite par des métadonnées. Chaque rangée peut être une forêt, une voie de voiture ou une voie de camion. Nous passerons en revue chaque type et définirons les objets 3D qui les représentent.

![Les différents types de rangées](https://cdn.hashnode.com/res/hashnode/image/upload/v1739803813951/3796e0c0-6f02-4c82-979b-a5192d8c3b8c.png align="left")

La carte peut être décomposée en rangées, et chaque rangée peut être décomposée en plusieurs tuiles. Le joueur se déplacera de tuile en tuile. Les arbres sont également placés sur une tuile distincte. Les voitures, en revanche, ne sont pas liées aux tuiles. Elles se déplacent librement dans la voie.

![Une rangée peut être décomposée en une tuile](https://cdn.hashnode.com/res/hashnode/image/upload/v1739803829719/38318821-8496-43d1-9b1c-a5b36d78af14.png align="left")

Nous définissons un fichier pour les constantes. Ici, nous définissons le nombre de tuiles dans chaque rangée. Dans ce cas, il y a 17 tuiles par rangée, allant de -8 à +8. Le joueur commencera au milieu à la tuile zéro.

```javascript
export const minTileIndex = -8;
export const maxTileIndex = 8;
export const tilesPerRow = maxTileIndex - minTileIndex + 1;
export const tileSize = 42;
```

### **La rangée de départ**

Tout d'abord, ajoutons la rangée de départ. Nous définirons quelques composants que nous allons utiliser pour rendre la carte, et nous rendrons la rangée initiale.

Créons un nouveau composant appelé `Map`. Bientôt, nous ajouterons ce groupe à la scène.

```javascript
import { Grass } from "./Grass";

export function Map() {
  return (
    <>
      <Grass rowIndex={0} />
    </>
  );
}
```

Ensuite, nous définissons le contenu de la carte. Plus tard, nous générerons les objets 3D en fonction des métadonnées et les utiliserons pour rendre la carte. Pour l'instant, utilisons simplement le composant Grass. Nous appelons le composant Grass avec l'index de la rangée, donc le composant Grass se positionnera en fonction de cet index de rangée.

Maintenant, définissons le composant Grass. Le composant Grass est la fondation et le conteneur des rangées de forêt et est également utilisé pour la rangée de départ. Il rend un groupe contenant une boîte plate, large et verte. Les dimensions de cette boîte sont déterminées par les constantes `tileSize` et `tilesPerRow`. La boîte a également une certaine hauteur, donc elle dépasse par rapport à la route, qui sera complètement plate.

```javascript
import { tilesPerRow, tileSize } from "../constants";

export function Grass({ rowIndex, children }) {
  return (
    <group position-y={rowIndex * tileSize}>
      <mesh>
        <boxGeometry args={[tilesPerRow * tileSize, tileSize, 3]} />
        <meshLambertMaterial color={0xbaf455} />
      </mesh>
      {children}
    </group>
  );
}
```

L'herbe peut servir de conteneur pour les arbres de la rangée. C'est pourquoi nous enveloppons la boîte verte dans un groupe afin que plus tard, nous puissions également ajouter des enfants à ce groupe. Nous positionnons le groupe le long de l'axe y en fonction de l'index de la rangée que nous avons reçu du composant Map. Pour la voie initiale, cela est zéro, mais comme nous allons avoir plusieurs voies, nous devons les placer selon cette position.

Maintenant que nous avons le conteneur de la carte et le composant d'herbe, nous pouvons enfin ajouter la carte à la scène.

```javascript
import { Scene } from "./components/Scene";
import { Player } from "./components/Player";
import { Map } from "./components/Map";

export default function Game() {
  return (
    <Scene>
      <Player />
      <Map />
    </Scene>
  );
}
```

### **Comment ajouter une rangée de forêt**

Maintenant que nous avons une forêt vide, ajoutons une autre rangée contenant des arbres. Nous définissons les métadonnées de la carte et rendons les rangées en fonction de ces métadonnées.

![Une rangée de forêt](https://cdn.hashnode.com/res/hashnode/image/upload/v1739806992172/139197f0-f2c1-4f11-aacf-f1fedeeaf9b0.png align="left")

Définissons les métadonnées de la carte. Les métadonnées sont un tableau d'objets qui contiennent des informations sur chaque rangée. Chaque rangée contiendra un type qui déterminera le type de la rangée et le reste des propriétés en fonction du type de rangée.

```javascript
export const rows = [
  {
    type: "forest",
    trees: [
      { tileIndex: -3, height: 50 },
      { tileIndex: 2, height: 30 },
      { tileIndex: 5, height: 50 },
    ],
  },
];
```

Les métadonnées pour une forêt incluent le type "forest" et une liste d'arbres. Chaque arbre a un index de tuile, qui représente sur quelle tuile il se trouve. Dans ce cas, nous avons 17 tuiles par rangée, allant de -8 à +8. Les arbres ont également une hauteur, qui est en fait la hauteur de la cime.

Pour rendre les rangées, étendons le composant `Map` pour rendre les rangées en fonction des métadonnées. Nous importons les métadonnées et mappons chaque rangée à un composant `Row` séparé.

Notez que le `rowIndex` est décalé de un par rapport à l'index du tableau car le premier élément du tableau de métadonnées deviendra la deuxième rangée (après la rangée de départ).

```javascript
import { rows } from "../metadata";
import { Grass } from "./Grass";
import { Row } from "./Row";

export function Map() {
  return (
    <>
      <Grass rowIndex={0} />

      {rows.map((rowData, index) => (
        <Row key={index} rowIndex={index + 1} rowData={rowData} />
      ))}
    </>
  );
}
```

Maintenant, définissons le composant `Row`. Le composant `Row` est essentiellement un switch case qui rend la rangée correcte en fonction de la propriété `type` de la rangée. Nous ne supportons que le type `forest` pour l'instant, mais nous étendrons ce fichier plus tard pour supporter les voies de voitures et de camions.

```javascript
import { Forest } from "./Forest";

export function Row({ rowIndex, rowData }) {
  switch (rowData.type) {
    case "forest": {
      return <Forest rowIndex={rowIndex} rowData={rowData} />;
    }
  }
}
```

Le composant `Forest` contient la fondation de la rangée, un composant `Grass`, et les arbres de la rangée.

Le composant `Grass` peut recevoir des enfants. Nous mappons les métadonnées des arbres aux composants `Tree` et les passons en tant qu'enfants au composant `Grass`. Chaque arbre reçoit son `tileIndex`, qui sera utilisé pour positionner l'arbre dans la rangée, et sa `height`.

```javascript
import { Grass } from "./Grass";
import { Tree } from "./Tree";

export function Forest({ rowIndex, rowData }) {
  return (
    <Grass rowIndex={rowIndex}>
      {rowData.trees.map((tree, index) => (
        <Tree
          key={index}
          tileIndex={tree.tileIndex}
          height={tree.height}
        />
      ))}
    </Grass>
  );
}
```

Les rangées de forêt ont également des arbres. Pour chaque élément du tableau des arbres, nous rendons un arbre. Le composant Tree rendra un objet 3D représentant l'arbre. Nous passons à ce composant l'index de la tuile que nous utiliserons pour positionner l'arbre dans la rangée et la hauteur.

![Un arbre](https://cdn.hashnode.com/res/hashnode/image/upload/v1739807310182/40cbb90b-0356-4db5-97bb-cdbe0c8e8cb8.png align="left")

Puisque nous avons déjà ajouté la carte à la scène, la forêt apparaîtra à l'écran. Mais d'abord, nous devons définir comment rendre un arbre. Nous allons représenter un arbre avec deux boîtes. Nous aurons une boîte pour le tronc et une pour la cime.

```javascript
import { tileSize } from "../constants";

export function Tree({ tileIndex, height }) {
  return (
    <group position-x={tileIndex * tileSize}>
      <mesh position-z={height / 2 + 20}>
        <boxGeometry args={[30, 30, height]} />
        <meshLambertMaterial color={0x7aa21d} />
      </mesh>
      <mesh position-z={10}>
        <boxGeometry args={[15, 15, 20]} />
        <meshLambertMaterial color={0x4d2926} />
      </mesh>
    </group>
  );
}
```

Ce sont deux boîtes simples, comme nous en avions avant avec le joueur et aussi dans le composant Grass. Le tronc est placé sur le sol. Nous le soulevons le long de l'axe Z de la moitié de sa hauteur, et la cime est placée sur le tronc. La hauteur de la cime est également basée sur la propriété de hauteur. Ces deux maillages sont enveloppés ensemble dans un groupe, puis nous positionnons ce groupe le long de l'axe X en fonction de la propriété d'index de la tuile.

### **Voies de voitures**

Maintenant, ajoutons un autre type de rangée : les voies de voitures. Le processus d'ajout de voies de voitures suivra une structure similaire. Nous définissons les métadonnées des voies, y compris les véhicules, puis nous les mappons en objets 3D.

![La voie de voitures](https://cdn.hashnode.com/res/hashnode/image/upload/v1739807532566/1c9cfdc9-2c45-476c-9ada-09f7abf79328.png align="left")

Dans les métadonnées, remplaçons la première rangée par une voie de voitures. La voie de voitures contiendra une seule voiture rouge se déplaçant vers la gauche. Nous avons une propriété de direction, qui est un indicateur booléen. Si cela est vrai, cela signifie que les voitures se déplacent vers la droite dans la voie, et si c'est faux, alors les véhicules se déplacent vers la gauche. Nous avons également une propriété de vitesse, qui définit combien d'unités chaque véhicule prend chaque seconde.

Enfin, nous avons un tableau de véhicules. Chaque voiture aura un index de tuile initial, qui représente uniquement sa position initiale car les voitures se déplaceront plus tard. Chaque voiture aura également une propriété de couleur, qui est une valeur de couleur hexadécimale.

```javascript
export const rows = [
  {
    type: "car",
    direction: false,
    speed: 1,
    vehicles: [{ initialTileIndex: 2, color: 0xff0000 }],
  },
];
```

Maintenant, pour rendre ce type de voie, nous devons étendre notre logique pour supporter les voies de voitures. Étendons le composant `Row` avec le support pour les voies de voitures. Si le type d'une rangée est `car`, nous le mappons à un composant `CarLane`.

```javascript
import { Forest } from "./Forest";
import { CarLane } from "./CarLane";

export function Row({ rowIndex, rowData }) {
  switch (rowData.type) {
    case "forest": {
      return <Forest rowIndex={rowIndex} rowData={rowData} />;
    }
    case "car": {
      return <CarLane rowIndex={rowIndex} rowData={rowData} />;
    }
  }
}
```

Le composant `CarLane` rend les voitures sur la route. Il a une structure similaire au composant `Forest`.

Il reçoit un objet `rowData` comme prop, qui contient les voitures à rendre. Il enveloppe les voitures dans un composant `Road` et mappe le tableau `rowData.vehicles` pour rendre chaque voiture.

```javascript
import { Road } from "./Road";
import { Car } from "./Car";

export function CarLane({ rowIndex, rowData }) {
  return (
    <Road rowIndex={rowIndex}>
      {rowData.vehicles.map((vehicle, index) => (
        <Car
          key={index}
          rowIndex={rowIndex}
          initialTileIndex={vehicle.initialTileIndex}
          direction={rowData.direction}
          speed={rowData.speed}
          color={vehicle.color}
        />
      ))}
    </Road>
  );
}
```

Les fonctions Road et Car sont nouvelles ici, alors examinons-les ensuite. La fonction Road retourne la fondation et le conteneur des voies de voitures et de camions. Similaire au composant Grass, elle retourne également un groupe contenant un plan gris.

![Le composant Road](https://cdn.hashnode.com/res/hashnode/image/upload/v1739807755293/e731a758-ac20-40f5-819b-82a5ae81e65f.png align="left")

La taille du plan est également déterminée par les constantes `tileSize` et `tilesPerRow`. Contrairement au composant Grass, cependant, il n'a aucune hauteur. Il est complètement plat. La route servira également de conteneur pour les voitures et les camions de la rangée, c'est pourquoi nous enveloppons le plan dans un groupe - afin que nous puissions ajouter des enfants à celui-ci.

```javascript
import { tilesPerRow, tileSize } from "../constants";

export function Road({ rowIndex, children }) {
  return (
    <group position-y={rowIndex * tileSize}>
      <mesh>
        <planeGeometry args={[tilesPerRow * tileSize, tileSize]} />
        <meshLambertMaterial color={0x454a59} />
      </mesh>
      {children}
    </group>
  );
}
```

Maintenant, regardons la voiture. La fonction Car retourne un modèle de voiture 3D très simple.

![Une voiture](https://cdn.hashnode.com/res/hashnode/image/upload/v1739807975022/dc04c3c1-de94-49fd-ad85-ade999c8862a.png align="left")

Elle contient une boîte pour le corps et une boîte plus petite pour la partie supérieure. Nous avons également deux maillages de roues. Parce que nous ne voyons jamais les voitures par en dessous, nous n'avons pas besoin de séparer les roues en gauche et droite. Nous pouvons simplement utiliser une longue boîte pour les roues avant et une autre pour les roues arrière.

```javascript
import { tileSize } from "../constants";

export function Car({
  rowIndex,
  initialTileIndex,
  direction,
  speed,
  color,
}) {
  return (
    <group
      position-x={initialTileIndex * tileSize}
      rotation-z={direction ? 0 : Math.PI}
    >
      <mesh position={[0, 0, 12]}>
        <boxGeometry args={[60, 30, 15]} />
        <meshLambertMaterial color={color} />
      </mesh>
      <mesh position={[-6, 0, 25.5]}>
        <boxGeometry args={[33, 24, 12]} />
        <meshLambertMaterial color={0xffffff} />
      </mesh>
      <mesh position={[-18, 0, 6]}>
        <boxGeometry args={[12, 33, 12]} />
        <meshLambertMaterial color={0x333333} />
      </mesh>
      <mesh position={[18, 0, 6]}>
        <boxGeometry args={[12, 33, 12]} />
        <meshLambertMaterial color={0x333333} />
      </mesh>
    </group>
  );
}
```

Nous regroupons tous ces éléments, les positionnons en fonction de la propriété `initialTileIndex` et les tournons en fonction de la propriété `direction`. Si la voiture va vers la gauche, nous la faisons tourner de 180°. Lorsque nous définissons les valeurs de rotation dans Three.js, nous devons les définir en radians, c'est pourquoi nous la définissons à Math.Pi, ce qui est équivalent à 180°.

Vous pouvez également trouver une version plus étendue de la façon de dessiner cette voiture avec des textures [dans cet article](https://www.freecodecamp.org/news/three-js-tutorial/).

En fonction des métadonnées, nous pouvons maintenant rendre une carte avec plusieurs rangées. Voici un exemple avec quelques voies supplémentaires. Bien sûr, n'hésitez pas à définir votre propre carte.

```javascript
export const rows = [
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
```

Cet article ne couvre pas les voies de camions, mais elles suivent une structure similaire. Le code pour cela peut être trouvé sur [JavaScriptGameTutorials.com](http://javascriptgametutorials.com/).

## **Comment animer les voitures**

Passons maintenant à l'animation des voitures dans leurs voies selon leur vitesse et leur direction.

C'est là que les choses commencent à diverger de la manière dont vous utiliseriez typiquement React. La méthode React consisterait à mettre à jour un état ou une prop et à laisser React re-rendre tout le composant. Cela est rapide lorsque vous travaillez avec des éléments HTML, mais ce n'est pas très efficace lorsque vous travaillez avec des objets 3D. Nous voulons [éviter de re-rendre](https://r3f.docs.pmnd.rs/advanced/pitfalls#avoid-setstate-in-loops) toute la scène et, au lieu de cela, mettre à jour la position des objets sous-jacents directement.

Nous utilisons React uniquement pour configurer la scène et les objets, puis nous laissons Three.js faire le travail lourd. React Three Fiber est juste une fine couche au-dessus de Three.js, donc nous pouvons accéder directement aux objets Three.js sous-jacents pour mettre à jour la position des voitures et des camions.

Nous allons utiliser un hook personnalisé, `useVehicleAnimation`, pour animer les véhicules. Ce hook aura besoin d'une référence à l'objet 3D qu'il doit manipuler. Avant de définir ce hook, obtenons une référence au groupe Three.js, qui représente la voiture. Nous utilisons le hook `useRef` de React pour stocker la référence et la lier à l'élément `group`.

Ensuite, nous passons cette référence au hook `useVehicleAnimation`, ainsi que la direction et la vitesse de la voiture.

```javascript
import { useRef } from "react";
import { tileSize } from "../constants";
import useVehicleAnimation from "../hooks/useVehicleAnimation";

export function Car({
  rowIndex,
  initialTileIndex,
  direction,
  speed,
  color,
}) {
  const car = useRef(null);
  useVehicleAnimation(car, direction, speed);

  return (
    <group
      position-x={initialTileIndex * tileSize}
      rotation-z={direction ? 0 : Math.PI}
      ref={car}
    >
      . . . 
    </group>
  );
}
```

Implémentons le hook `useVehicleAnimation` pour animer les véhicules. Il les déplace en fonction de leur vitesse et de leur direction jusqu'à la fin de la voie, puis les fait réapparaître à l'autre extrémité. De cette manière, les véhicules se déplacent en boucle infinie.

![Les voitures se déplacent en boucle infinie](https://cdn.hashnode.com/res/hashnode/image/upload/v1739808359961/eca84295-09d7-463a-8d29-e5f8069bb673.png align="left")

Ce hook utilise le hook `useFrame` que React Three Fiber fournit. Ce hook est similaire à `setAnimationLoop` dans Three.js. Il exécute une fonction à chaque frame d'animation.

De manière pratique, cette fonction reçoit le temps `delta`—le temps écoulé depuis la frame d'animation précédente. Nous multiplions cette valeur par la `speed` du véhicule pour obtenir la distance parcourue par la voiture pendant ce temps.

```javascript
import { useFrame } from "@react-three/fiber";
import { tileSize, minTileIndex, maxTileIndex } from "../constants";

export default function useVehicleAnimation(ref, direction, speed) {
  useFrame((state, delta) => {
    if (!ref.current) return;
    const vehicle = ref.current;

    const beginningOfRow = (minTileIndex - 2) * tileSize;
    const endOfRow = (maxTileIndex + 2) * tileSize;

    if (direction) {
      vehicle.position.x =
        vehicle.position.x > endOfRow
          ? beginningOfRow
          : vehicle.position.x + speed * delta;
    } else {
      vehicle.position.x =
        vehicle.position.x < beginningOfRow
          ? endOfRow
          : vehicle.position.x - speed * delta;
    }
  });
}
```

Nous mettons à jour directement la propriété `position.x` du groupe Three.js sous-jacent. Si le véhicule atteint la fin de la voie, nous le faisons réapparaître à l'autre extrémité.

Notez que la référence passée au hook peut être `null` car elle n'est définie qu'après le premier rendu. Si la référence n'est pas définie, nous quittons la fonction. Ensuite, l'animation commence dans la frame suivante.

## **Comment déplacer le joueur**

Maintenant, passons à l'animation du joueur. Déplacer le joueur sur la carte est plus complexe que déplacer les véhicules. Le joueur peut se déplacer dans toutes les directions, heurter des arbres ou se faire frapper par des voitures, et il ne devrait pas pouvoir sortir de la carte.

Dans ce chapitre, nous nous concentrons sur deux parties : collecter les entrées de l'utilisateur et exécuter les commandes de mouvement. Le mouvement du joueur n'est pas instantané - nous devons collecter les commandes de mouvement dans une file d'attente et les exécuter une par une. Nous allons collecter les entrées de l'utilisateur et les mettre dans une file d'attente.

### **Collecte des entrées de l'utilisateur**

Pour suivre les commandes de mouvement, nous créons un magasin pour le joueur. Nous n'utilisons pas de bibliothèque de gestion d'état, car nous n'avons pas besoin d'un magasin réactif. Nous définissons simplement notre état dans un fichier JavaScript régulier.

Le magasin gardera une trace de la position du joueur et de la file d'attente de mouvement. Le joueur commence au milieu de la première rangée, et la file de mouvement est initialement vide.

Nous exporterons également deux fonctions : **queueMove** ajoute la commande de mouvement à la fin de la file de mouvement, et la fonction **stepCompleted** supprime la première commande de mouvement de la file et met à jour la position du joueur en conséquence.

```javascript
export const state = {
  currentRow: 0,
  currentTile: 0,
  movesQueue: [],
};

export function queueMove(direction) {
  state.movesQueue.push(direction);
}

export function stepCompleted() {
  const direction = state.movesQueue.shift();

  if (direction === "forward") state.currentRow += 1;
  if (direction === "backward") state.currentRow -= 1;
  if (direction === "left") state.currentTile -= 1;
  if (direction === "right") state.currentTile += 1;
}
```

Maintenant, nous pouvons ajouter des écouteurs d'événements pour les événements de clavier afin d'écouter les touches fléchées. Le hook `useEventListeners` écoute les touches fléchées et appelle la fonction `queueMove` du magasin de joueurs avec la direction correspondante.

```javascript
import { useEffect } from "react";
import { queueMove } from "../stores/player";

export default function useEventListeners() {
  useEffect(() => {
    const handleKeyDown = (event) => {
      if (event.key === "ArrowUp") {
        queueMove("forward");
      } else if (event.key === "ArrowDown") {
        queueMove("backward");
      } else if (event.key === "ArrowLeft") {
        queueMove("left");
      } else if (event.key === "ArrowRight") {
        queueMove("right");
      }
    };

    window.addEventListener("keydown", handleKeyDown);

    // Fonction de nettoyage pour supprimer l'écouteur d'événement
    return () => {
      window.removeEventListener("keydown", handleKeyDown);
    };
  }, []);
}
```

Après avoir défini les écouteurs d'événements, nous devons également les importer dans le composant Game pour qu'ils fonctionnent.

```javascript
import { Scene } from "./components/Scene";
import { Player } from "./components/Player";
import { Map } from "./components/Map";
import useEventListeners from "./hooks/useEventListeners";

export default function Game() {
  useEventListeners();

  return (
    <Scene>
      <Player />
      <Map />
    </Scene>
  );
}
```

### **Exécution des commandes de mouvement**

Jusqu'à présent, nous avons collecté les entrées de l'utilisateur et mis chaque commande dans le tableau **movesQueue** dans le composant joueur. Maintenant, il est temps d'exécuter ces commandes une par une et d'animer le joueur.

Créons un nouveau hook appelé **usePlayerAnimation**. Son objectif principal est de prendre chaque commande de mouvement de la **moveQueue** une par une, de calculer la progression du joueur vers l'exécution d'un pas et de positionner le joueur en conséquence.

![Le mouvement du joueur](https://cdn.hashnode.com/res/hashnode/image/upload/v1739808997988/8adb70d2-bf5d-4e65-8ed9-29e8f297b487.png align="left")

Ce hook anime le joueur image par image. Il utilise le hook `useFrame`, tout comme le hook `useVehicleAnimation`. Cette fois, cependant, nous utilisons une `moveClock` séparée qui mesure chaque étape individuellement. Nous passons `false` au constructeur de l'horloge pour qu'elle ne démarre pas automatiquement. L'horloge démarre au début d'une étape. À chaque image d'animation, nous vérifions d'abord s'il reste des étapes à effectuer, et si c'est le cas et que nous ne traitons pas actuellement une étape, nous démarrons l'horloge.

```javascript
import * as THREE from "three";
import { useFrame } from "@react-three/fiber";
import { state, stepCompleted } from "../stores/player";
import { tileSize } from "../constants";

export default function usePlayerAnimation(ref) {
  const moveClock = new THREE.Clock(false);

  useFrame(() => {
    if (!ref.current) return;
    if (!state.movesQueue.length) return;
    const player = ref.current;

    if (!moveClock.running) moveClock.start();

    const stepTime = 0.2; // Secondes nécessaires pour faire un pas
    const progress = Math.min(
      1,
      moveClock.getElapsedTime() / stepTime
    );

    setPosition(player, progress);

    // Une fois qu'un pas est terminé
    if (progress >= 1) {
      stepCompleted();
      moveClock.stop();
    }
  });
}

. . .
```

Nous utilisons l'horloge de mouvement pour calculer la progression entre les deux tuiles. L'indicateur de progression peut être un nombre entre zéro et un. Zéro signifie que le joueur est encore au début du pas, et un signifie qu'il est arrivé à sa nouvelle position.

À chaque image d'animation, nous appelons la fonction **setPosition** pour définir la position du joueur selon la progression. Une fois que nous avons terminé un pas, nous appelons la fonction **stepCompleted** pour mettre à jour la position du joueur et arrêter l'horloge. S'il reste des commandes de mouvement dans la **movesQueue**, l'horloge redémarrera dans l'image d'animation suivante.

Maintenant que nous savons comment calculer la progression pour chaque pas, regardons comment définir la position du joueur en fonction de la progression. Le joueur sautera de tuile en tuile. Décomposons cela en deux parties : les composantes horizontale et verticale du mouvement.

Le joueur se déplace de la tuile actuelle à la tuile suivante dans la direction de la commande de mouvement. Nous calculons la position de départ et d'arrivée du joueur en fonction de la tuile actuelle et de la direction de la commande de mouvement. Ensuite, nous utilisons une interpolation linéaire avec une fonction utilitaire que Three.js fournit. Cela interpolera entre les positions de départ et d'arrivée en fonction de la progression.

```javascript
. . .

function setPosition(player, progress) {
  const startX = state.currentTile * tileSize;
  const startY = state.currentRow * tileSize;
  let endX = startX;
  let endY = startY;

  if (state.movesQueue[0] === "left") endX -= tileSize;
  if (state.movesQueue[0] === "right") endX += tileSize;
  if (state.movesQueue[0] === "forward") endY += tileSize;
  if (state.movesQueue[0] === "backward") endY -= tileSize;

  player.position.x = THREE.MathUtils.lerp(startX, endX, progress);
  player.position.y = THREE.MathUtils.lerp(startY, endY, progress);
  player.children[0].position.z = Math.sin(progress * Math.PI) * 8 + 10;
}
```

Pour la composante verticale, nous utilisons une fonction sinus pour que cela ressemble à un saut. Nous mappons essentiellement la progression à la première partie d'une onde sinusoïdale.

Ci-dessous, vous pouvez voir à quoi ressemble une onde sinusoïdale. Elle va de 0 à 2 Pi. Donc si vous multipliez la valeur de progression, qui va de 0 à 1 avec Pi, alors la progression se mappera dans la première moitié de cette onde sinusoïdale. La fonction sinus vous donnera alors une valeur entre zéro et un.

Pour faire paraître le saut plus haut, nous pouvons multiplier cela par une valeur. Dans ce cas, nous multiplions le résultat de la fonction sinus par huit, donc en conséquence, le joueur aura un saut où la hauteur maximale du saut sera de huit unités.

Nous devons également ajouter la position Z originale à la valeur - sinon, le joueur s'enfoncera à moitié dans le sol après le premier pas.

![Pour le mouvement vertical, nous utilisons une onde sinusoïdale](https://cdn.hashnode.com/res/hashnode/image/upload/v1739810397620/89119f6e-ced5-4cdb-8254-96fbf66479ed.png align="left")

Il est enfin temps de mettre à jour le composant `Player` pour que tout se rassemble. Nous créons une nouvelle référence avec `useRef` et l'assignons à l'élément `group`. Enfin, nous passons cette référence au hook `usePlayerAnimation` que nous venons d'implémenter.

```javascript
import { useRef } from "react";
import usePlayerAnimation from "../hooks/usePlayerAnimation";

export function Player() {
  const player = useRef(null);
  usePlayerAnimation(player);

  return (
    <group ref={player}>
      <mesh position={[0, 0, 10]} castShadow receiveShadow>
        <boxGeometry args={[15, 15, 20]} />
        <meshLambertMaterial color={0xffffff} flatShading />
      </mesh>
    </group>
  );
}
```

Si vous avez tout fait correctement, le joueur devrait pouvoir se déplacer sur le plateau de jeu, en allant vers l'avant, l'arrière, la gauche et la droite. Mais nous n'avons pas encore ajouté de détection de collision. Jusqu'à présent, le joueur peut se déplacer à travers les arbres et les véhicules et même sortir du plateau de jeu. Corrigons ces problèmes dans les étapes suivantes.

### Suivre le joueur avec la caméra

Nous avons défini la caméra dans le composant `Scene`. Par défaut, elle a une position statique. Au lieu de cela, nous voulons la déplacer avec le joueur. Nous pourrions ajuster sa position à chaque frame d'animation comme le joueur, mais il est plus facile d'attacher la caméra au composant `Player` pour qu'ils se déplacent ensemble.

Nous pouvons accéder à la caméra en utilisant le hook `useThree` de `@react-three/fiber`. Cela retourne un objet caméra Three.js que nous pouvons ajouter au groupe du joueur.

Nous avons déjà une référence au groupe représentant le joueur. Nous pouvons attacher la caméra au joueur en l'ajoutant comme enfant du groupe du joueur. Parce que la référence du joueur est indéfinie au premier rendu, nous devons utiliser le hook `useEffect` pour attacher la caméra uniquement une fois que la référence du joueur est définie.

```javascript
import { useRef, useEffect } from "react";
import { useThree } from "@react-three/fiber";
import usePlayerAnimation from "../hooks/usePlayerAnimation";

export function Player() {
  const player = useRef(null);
  const camera = useThree((state) => state.camera);

  usePlayerAnimation(player);

  useEffect(() => {
    if (!player.current) return;

    // Attacher la caméra au joueur
    player.current.add(camera);
  });

  return (
    . . .
  );
}
```

### **Restriction du mouvement du joueur**

Assurons-nous que le joueur ne peut pas se retrouver dans une position invalide. Nous vérifierons si un mouvement est valide en calculant où il emmènera le joueur. Si le joueur se retrouverait dans une position en dehors de la carte ou sur une tuile occupée par un arbre, nous ignorerons cette commande de mouvement.

![Calculer où le joueur se retrouvera](https://cdn.hashnode.com/res/hashnode/image/upload/v1739810555283/310afd32-6e5a-4143-bbe2-e0da558bd6d7.png align="left")

Tout d'abord, nous devons calculer où le joueur se retrouverait s'il effectuait un mouvement particulier. Chaque fois que nous ajoutons un nouveau mouvement à la file d'attente, nous devons calculer où le joueur se retrouverait s'il effectuait tous les mouvements de la file d'attente et prendre la commande de mouvement actuelle. Nous créons une fonction utilitaire qui prend la position actuelle du joueur et un tableau de mouvements et retourne la position finale du joueur.

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

![Vérifier si le joueur heurte un arbre](https://cdn.hashnode.com/res/hashnode/image/upload/v1739810684106/71c45122-b10c-4623-b575-184c1cf1fecb.png align="left")

Si le mouvement est invalide, nous retournons false. Tout d'abord, nous vérifions si la position finale est avant la rangée de départ ou si le numéro de tuile est en dehors de la plage des tuiles. Ensuite, nous vérifions les métadonnées de la rangée dans laquelle le joueur se retrouvera. Ici, l'index est décalé de un car les métadonnées de la rangée n'incluent pas la rangée de départ. Si nous nous retrouvons dans une rangée de forêt, nous vérifions si un arbre occupe la tuile vers laquelle nous nous déplaçons. Si l'une de ces conditions est vraie, nous retournons false.

```javascript
import { calculateFinalPosition } from "./calculateFinalPosition";
import { minTileIndex, maxTileIndex } from "../constants";
import { rows } from "../metadata";

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

Enfin, étendons la fonction **queueMove** du joueur avec la fonction **endsUpInValidPosition** pour vérifier si un mouvement est valide. Si la fonction **endsUpInValidPosition** retourne false, nous ne pouvons pas effectuer ce pas. Dans ce cas, nous quittons la fonction avant que le mouvement ne soit ajouté au tableau **movesQueue**. Ainsi, nous ignorons le mouvement.

```javascript
import { endsUpInValidPosition } from "../utilities/endsUpInValidPosition";

export let state = {
  currentRow: 0,
  currentTile: 0,
  movesQueue: [],
};

export function queueMove(direction) {
  const isValidMove = endsUpInValidPosition(
    { rowIndex: state.currentRow, tileIndex: state.currentTile },
    [...state.movesQueue, direction]
  );

  if (!isValidMove) return; // Ignorer le mouvement

  state.movesQueue.push(direction);
}

. . .
```

De cette manière, comme vous pouvez le voir, vous pouvez vous déplacer sur la carte - mais vous ne pouvez jamais vous déplacer avant la première rangée, vous ne pouvez pas aller trop loin à gauche ou trop loin à droite, et vous ne pouvez plus non plus traverser un arbre.

## **Détection de collision**

Pour terminer le jeu, ajoutons la détection de collision. Nous vérifions si le joueur est heurté par un véhicule, et si c'est le cas, nous affichons une fenêtre d'alerte.

![Calcul des boîtes de délimitation pour la détection de collision](https://cdn.hashnode.com/res/hashnode/image/upload/v1739826639155/1497d588-bf60-4fdc-a185-a01a781beafb.png align="left")

Nous ajoutons un nouveau hook qui vérifie, du point de vue des véhicules, s'ils heurtent le joueur. Jusqu'à présent, le joueur et les véhicules ont géré leur propre mouvement de manière indépendante. Ils n'ont aucune notion l'un de l'autre. Pour gérer la détection de collision, soit le joueur doit connaître les véhicules, soit les véhicules doivent connaître le joueur.

Nous choisirons la première approche car ainsi, nous n'avons besoin de stocker qu'une seule référence au joueur dans le magasin, et tous les véhicules peuvent vérifier cette référence. Étendons le magasin du joueur avec une propriété `ref` pour stocker la référence de l'objet joueur. Nous exposons également une méthode `setRef` qui définit cette référence.

```javascript
import { endsUpInValidPosition } from "../utilities/endsUpInValidPosition";

export const state = {
  currentRow: 0,
  currentTile: 0,
  movesQueue: [],
  ref: null,
};

. . .

export function setRef(ref) {
  state.ref = ref;
}
```

Ensuite, nous appelons la méthode `setRef` dans le composant `Player` pour définir la référence à l'objet joueur. Nous avons déjà la référence `player`, donc nous pouvons passer sa valeur à la méthode `setRef` dans le hook `useEffect` une fois qu'elle est définie.

```javascript
import { useRef, useEffect } from "react";
import { useThree } from "@react-three/fiber";
import usePlayerAnimation from "../hooks/usePlayerAnimation";
import { setRef } from "../stores/player";

export function Player() {
  const player = useRef(null);
  const camera = useThree((state) => state.camera);

  usePlayerAnimation(player);

  useEffect(() => {
    if (!player.current) return;

    // Attacher la caméra au joueur
    player.current.add(camera);

    // Définir la référence du joueur dans le magasin
    setRef(player.current);
  });

  return (
    . . .
  );
}
```

Ensuite, définissons un autre hook pour gérer la détection de collision. Nous vérifions si le joueur intersecte avec l'un des véhicules. Si c'est le cas, nous mettons fin au jeu.

Ce hook est du point de vue d'un véhicule. Il reçoit la référence `vehicle` et le `rowIndex`. Nous vérifions si le véhicule intersecte avec le joueur si le joueur est dans la même rangée, la rangée précédente ou la rangée suivante du véhicule. Nous utilisons le hook `useFrame` pour exécuter la logique de détection de collision à chaque frame.

Ensuite, nous créons des boîtes de délimitation pour le joueur et le véhicule pour vérifier une intersection. Cela peut être un peu excessif, car la forme de nos objets est connue, mais c'est une manière générique de gérer la détection de collision.

Si les boîtes de délimitation s'intersectent, nous affichons une alerte. Une fois que l'utilisateur clique sur OK dans l'alerte, nous rechargeons la page.

```javascript
import * as THREE from "three";
import { useFrame } from "@react-three/fiber";
import { state as player } from "../stores/player";

export default function useHitDetection(vehicle, rowIndex) {
  useFrame(() => {
    if (!vehicle.current) return;
    if (!player.ref) return;

    if (
      rowIndex === player.currentRow ||
      rowIndex === player.currentRow + 1 ||
      rowIndex === player.currentRow - 1
    ) {
      const vehicleBoundingBox = new THREE.Box3();
      vehicleBoundingBox.setFromObject(vehicle.current);

      const playerBoundingBox = new THREE.Box3();
      playerBoundingBox.setFromObject(player.ref);

      if (playerBoundingBox.intersectsBox(vehicleBoundingBox)) {
        window.alert("Game over!");
        window.location.reload();
      }
    }
  });
}
```

Enfin, nous appelons ce hook dans les composants de véhicules. Dans le composant `Car`, nous passons la référence `car` et le `rowIndex` au hook `useHitDetection`.

```javascript
import { useRef } from "react";
import { tileSize } from "../constants";
import useVehicleAnimation from "../hooks/useVehicleAnimation";
import useHitDetection from "../hooks/useHitDetection";

export function Car({
  rowIndex,
  initialTileIndex,
  direction,
  speed,
  color,
}) {
  const car = useRef(null);
  useVehicleAnimation(car, direction, speed);
  useHitDetection(car, rowIndex);

  return (
    . . .
  );
}
```

## **Prochaines étapes**

Félicitations, vous avez atteint la fin de ce tutoriel, et nous avons couvert toutes les principales fonctionnalités du jeu. Nous avons rendu une carte, animé les véhicules, ajouté la gestion des événements pour le joueur et ajouté la détection de collision.

J'espère que vous avez pris beaucoup de plaisir à créer ce jeu. Ce jeu, bien sûr, est loin d'être parfait, et il y a diverses améliorations que vous pouvez apporter si vous souhaitez continuer à travailler dessus.

Vous pouvez trouver le tutoriel étendu avec des démonstrations interactives sur [JavaScriptGameTutorials.com](http://javascriptgametutorials.com/). Là, nous couvrons également comment ajouter des ombres et des voies de camions et comment générer un nombre infini de rangées lorsque le joueur avance. Nous ajoutons également des éléments d'interface utilisateur pour les contrôles et l'indicateur de score, et nous ajoutons un écran de résultat avec un bouton pour réinitialiser le jeu.

Alternativement, vous pouvez trouver le tutoriel étendu sur [YouTube](https://www.youtube.com/watch?v=ccYrSACDNsw&ab_channel=HunorM%C3%A1rtonBorb%C3%A9ly).

%[https://www.youtube.com/watch?v=ccYrSACDNsw]