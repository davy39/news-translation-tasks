---
title: Comment composer des animations Canvas en TypeScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-27T21:59:09.000Z'
originalURL: https://freecodecamp.org/news/how-to-compose-canvas-animations-in-typescript-9368dfa29028
coverImage: https://cdn-media-1.freecodecamp.org/images/0*pJTkQHXgr6hKmpXZ
tags:
- name: animation
  slug: animation
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: technology
  slug: technology
- name: TypeScript
  slug: typescript
seo_title: Comment composer des animations Canvas en TypeScript
seo_desc: 'By Changhui Xu

  Today we are going to create a canvas animation with pretty blooming flowers, step
  by step. You can follow along by playing StackBlitz projects in this blog post,
  and you are welcome to check out the source code in this GitHub repo.


  _...'
---

Par Changhui Xu

Aujourd'hui, nous allons créer une animation canvas avec de jolies fleurs en pleine floraison, **étape par étape**. Vous pouvez suivre en jouant avec les projets StackBlitz dans cet article de blog, et vous êtes les bienvenus pour consulter le code source dans [ce dépôt GitHub](https://github.com/changhuixu/canvas-animation-step-by-step).

![Image](https://cdn-media-1.freecodecamp.org/images/0*pJTkQHXgr6hKmpXZ)
_« Une photo en gros plan d'une abeille pollinisant des fleurs » par [Unsplash](https://unsplash.com/@goumbik?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Lukas Blazek</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Dans mon récent [article de blog](https://codeburst.io/canvas-animations-in-typescript-97ba0163cb19), j'ai décrit une vue d'ensemble de la composition d'animations canvas en utilisant TypeScript. Ici, je vais présenter un processus détaillé de la manière de modéliser des objets et de les animer sur canvas.

#### Table des matières

* [Dessiner des fleurs](#dessiner-des-fleurs)
* [Animer des fleurs](#animer-des-fleurs)
* [Ajouter des interactions à l'animation](#ajouter-des-interactions-a-lanimation)

### Dessiner des fleurs

Tout d'abord, nous avons besoin d'une fonction pour dessiner des fleurs sur canvas. Nous pouvons décomposer les parties d'une **fleur** en **pétales** et **centre** (pistil et étamine). Le centre de la fleur peut être abstrait comme un cercle rempli avec une certaine couleur. Les pétales poussent autour du centre, et ils peuvent être dessinés en faisant tourner le canvas avec un certain degré de symétrie.

Remarquez que les noms en gras (**fleur**, **pétale**, **centre**) impliquent des **modèles** dans le code. Nous allons définir ces modèles en identifiant leurs propriétés.

Concentrons-nous d'abord sur le dessin d'un pétale avec quelques abstractions. Inspiré par [ce tutoriel](https://www.html5canvastutorials.com/advanced/html5-canvas-blooming-flowers-effect/), nous savons que la forme du pétale peut être représentée par deux [courbes quadratiques](https://www.w3schools.com/tags/canvas_quadraticcurveto.asp) et deux [courbes de Bézier](https://www.w3schools.com/tags/canvas_beziercurveto.asp). Et nous pouvons dessiner ces courbes en utilisant les méthodes `quadraticCurveTo()` et `bezierCurveTo()` dans l'API HTML canvas.

Comme le montre la Figure 1 (1), une courbe quadratique a un point de départ, un point final, et un point de contrôle qui détermine la courbure de la courbe. Dans la Figure 1 (2), une courbe de Bézier a un point de départ, un point final, et deux points de contrôle.

Pour **connecter en douceur** deux courbes (n'importe quelles deux courbes, soit quadratiques ou de Bézier, ou autres), nous devons nous assurer que le point de connexion et les deux points de contrôle à proximité sont sur la même ligne, de sorte que ces **deux courbes aient la même courbure au point de connexion**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XwdZt1n54qbsXLaP67d3Ww.png)
_**Figure 1.** Dessiner une fleur étape par étape. (1) Courbe quadratique ; (2) Courbe de Bézier ; (3) Forme de pétale formée par deux courbes quadratiques (vert) et deux courbes de Bézier (bleu). Les points rouges sont les sommets des pétales. Les points bleus sont les points de contrôle des courbes des pétales. (4) Forme de pétale remplie avec une couleur. (5) Une forme de fleur générée par un cercle centré et des pétales tournés. (6) Une forme de fleur avec une ombre._

La Figure 1 (3) montre une forme de pétale de base composée de deux courbes quadratiques (vert) et de deux courbes de Bézier (bleu). Il y a 4 points rouges représentant les sommets des pétales et 6 points bleus représentant les points de contrôle des courbes.

Le sommet rouge du bas est le point central de la fleur et le sommet rouge du haut est la pointe du pétale de la fleur. Les deux sommets rouges du milieu représentent le rayon du pétale. Et l'angle entre ces deux sommets par rapport au point central est nommé étendue de l'angle du pétale. Vous pouvez jouer avec [ce projet StackBlitz](https://stackblitz.com/edit/petal-shape) sur la forme des pétales.

%[https://stackblitz.com/edit/petal-shape?embed=1&file=index.ts]

Après que la forme du pétale soit définie, nous pouvons remplir la forme avec une couleur et obtenir un pétale, comme le montre la Figure 1 (4). Avec les informations ci-dessus, nous sommes prêts à écrire notre premier modèle d'objet : **Petal**.

```ts
export class Petal {
  private readonly vertices: Point[];
  private readonly controlPoints: Point[][];
  
  constructor(
    public readonly centerPoint: Point,
    public readonly radius: number,
    public readonly tipSkewRatio: number,
    public readonly angleSpan: number,
    public readonly color: string
  ) {
    this.vertices = this.getVertices();
    this.controlPoints = this.getControlPoints(this.vertices);
  }
  
  draw(context: CanvasRenderingContext2D) {
    // dessiner des courbes en utilisant vertices et controlPoints  
  }
  
  private getVertices() {
    // calculer les coordonnées des sommets 
  }
  private getControlPoints(vertices: Point[]): Point[][] {
    // calculer les coordonnées des points de contrôle
  }
}
```

La classe auxiliaire `Point` dans `Petal` est définie comme suit. Les coordonnées utilisent des entiers (via `Math.floor()`) pour économiser de la puissance de calcul.

```ts
export class Point {
  constructor(public readonly x = 0, public readonly y = 0) {
    this.x = Math.floor(this.x);
    this.y = Math.floor(this.y);
  }
}
```

La représentation d'un **Centre de Fleur** peut être paramétrée par son point central, le rayon du cercle, et la couleur. Ainsi, le squelette de la classe `FlowerCenter` est le suivant :

```ts
export class FlowerCenter {
  constructor(
    private readonly centerPoint: Point,
    private readonly centerRadius: number,
    private readonly centerColor: string
  ) {}
  
  draw(context: CanvasRenderingContext2D) {
    // dessiner le cercle
  }
}
```

Puisque nous avons un pétale et un centre de fleur, nous sommes prêts à avancer pour dessiner une fleur, qui contient un cercle central et plusieurs pétales de la même forme.

D'un point de vue Orienté Objet, `Flower` peut être construit comme `new Flower(center: FlowerCenter, petals: Petal[])` ou comme `new Flower(center: FlowerCenter, numberOfPetals: number, petal: Petal)`. J'utilise la deuxième méthode, car aucun tableau n'est nécessaire pour ce scénario.

Dans le constructeur, vous pouvez ajouter quelques validations pour assurer l'intégrité des données. Par exemple, lancer une erreur si `center.centerPoint` ne correspond pas à `petal.centerPoint`.

```ts
export class Flower {
  constructor(
    private readonly flowerCenter: FlowerCenter,
    private readonly numberOfPetals: number,
    private petal: Petal
  ) {}
  
  draw(context: CanvasRenderingContext2D) {
    this.drawPetals(context);
    this.flowerCenter.draw(context);
  }
  
  private drawPetals(context: CanvasRenderingContext2D) {
    context.save();
    const cx = this.petal.centerPoint.x;
    const cy = this.petal.centerPoint.y;
    const rotateAngle = (2 * Math.PI) / this.numberOfPetals;
    for (let i = 0; i < this.numberOfPetals; i++) {
      context.translate(cx, cy);
      context.rotate(rotateAngle);
      context.translate(-cx, -cy);
      this.petal.draw(context);
    }
    context.restore();
  }
}
```

Faites attention à la méthode `drawPetals(context)`. Puisque la rotation se fait autour du point central de la fleur, nous devons d'abord translater le canvas pour déplacer l'origine vers le centre de la fleur, puis faire tourner le canvas. Après la rotation, nous devons translater le canvas en arrière de sorte que l'origine soit le (0, 0) précédent.

En utilisant ces modèles (`Flower`, `FlowerCenter`, `Petal`), nous sommes capables d'obtenir une fleur qui ressemble à la Figure 1 (5). Pour rendre la fleur plus concrète, nous ajoutons quelques effets d'ombre de sorte que la fleur ressemble à celle de la Figure 1 (6). Vous pouvez également jouer avec [le projet StackBlitz ci-dessous](https://stackblitz.com/edit/canvas-flower).

%[https://stackblitz.com/edit/canvas-flower?embed=1&file=index.ts]

### Animer des fleurs

Dans cette section, nous allons animer le processus de floraison des fleurs. Nous allons simuler le processus de floraison en augmentant le rayon des pétales au fil du temps. La Figure 2 montre l'animation finale dans laquelle les pétales des fleurs s'étendent à chaque image.

![Image](https://cdn-media-1.freecodecamp.org/images/1*tJ5xB9d4xcN3alxmqgEGMA.gif)
_**Figure 2.** Fleurs en floraison sur canvas._

Avant de faire les animations réelles, nous pouvons vouloir ajouter quelques variétés aux fleurs pour qu'elles ne soient pas ennuyeuses. Par exemple, nous pouvons générer des points aléatoires sur le canvas pour disperser les fleurs, nous pouvons générer des formes/tailles aléatoires de fleurs, et nous pouvons peindre des couleurs aléatoires pour elles. Ce type de travail est généralement fait dans un service spécifique dans le but de centraliser la logique et de réutiliser le code. Nous mettons ensuite la logique de randomisation dans la classe `FlowerRandomizationService`.

```ts
export class FlowerRandomizationService {
  constructor(){}
  getFlowerAt(point: Point): Flower {
    ... // randomisation
  }
  ...  // autres méthodes d'aide
}
```

Ensuite, nous créons une classe `BloomingFlowers` pour stocker un tableau de fleurs généré par `FlowerRandomizationService`.

Pour faire une animation, nous définissons une méthode `increasePetalRadius()` dans la classe `Flower` pour mettre à jour les objets fleur. Ensuite, en appelant `window.requestAnimationFrame(() => this.animateFlowers());` dans la classe `BloomingFlowers`, nous planifions un redessin sur le canvas à chaque image. Et les fleurs sont mises à jour via `flower.increasePetalRadius();` pendant chaque redessin. L'extrait de code ci-dessous montre une classe d'animation minimale.

```ts
export class BloomingFlowers {
  private readonly context: CanvasRenderingContext2D;
  private readonly canvasW: number;
  private readonly canvasH: number;
  private readonly flowers: Flower[] = [];
  
  constructor(
    private readonly canvas: HTMLCanvasElement,
    private readonly nFlowers: number = 30
  ) {
    this.context = this.canvas.getContext('2d');
    this.canvasWidth = this.canvas.width;
    this.canvasHeight = this.canvas.height;
    this.getFlowers();
  }
  
  bloom() {
    window.requestAnimationFrame(() => this.animateFlowers());
  }
  
  private animateFlowers() {
    this.context.clearRect(0, 0, this.canvasW, this.canvasH);
    this.flowers.forEach(flower => {
      flower.increasePetalRadius();
      flower.draw(this.context);
    });
    window.requestAnimationFrame(() => this.animateFlowers());
  }
  
  private getFlowers() {
    for (let i = 0; i < this.nFlowers; i++) {
      const flower = ... // obtenir une fleur randomisée
      this.flowers.push(flower);
    }
  }
}
```

Remarquez que la fonction de rappel dans `window.requestAnimationFrame(() => this.animateFlowers());` utilise la syntaxe des fonctions fléchées, qui est nécessaire pour préserver le contexte `this` de la classe de l'objet actuel.

L'extrait de code ci-dessus entraînerait une augmentation continue de la longueur des pétales de la fleur, car il n'a pas de mécanisme pour arrêter cette animation. Dans le code de démonstration, j'utilise un rappel `setTimeout()` pour terminer l'animation après 5 secondes. Et si vous voulez jouer une animation de manière récursive ? Une solution simple est démontrée dans [le projet StackBlitz ci-dessous](https://stackblitz.com/edit/canvas-flower-blooming), qui utilise un rappel `setInterval()` pour rejouer l'animation toutes les 8 secondes.

%[https://stackblitz.com/edit/canvas-flower-blooming?embed=1&file=index.ts]

C'est cool. Que pouvons-nous faire d'autre sur les animations canvas ?

### Ajouter des interactions à l'animation

Nous voulons que le canvas réponde aux événements clavier, aux événements souris ou aux événements tactiles. Comment ? Ajoutez des écouteurs d'événements.

Dans cette démonstration, nous allons créer un canvas interactif. Lorsque la souris clique sur le canvas, une fleur s'épanouit. Lorsque vous cliquez à un autre point sur le canvas, une autre fleur s'épanouit. En maintenant la touche CTRL enfoncée et en cliquant, le canvas sera effacé. La Figure 3 montre l'animation finale du canvas.

![Image](https://cdn-media-1.freecodecamp.org/images/1*SsPGDDNaxiQHHQnzT4YCvg.gif)
_**Figure 3.** Canvas interactif._

Comme d'habitude, nous créons une classe `InteractiveFlowers` pour contenir un tableau de fleurs. L'extrait de code de la classe `InteractiveFlowers` est le suivant.

```ts
export class InteractiveFlowers {
  private readonly context: CanvasRenderingContext2D;
  private readonly canvasW: number;
  private readonly canvasH: number;
  private flowers: Flower[] = [];
  private readonly randomizationService = 
               new FlowerRandomizationService();
  private ctrlIsPressed = false;
  private mousePosition = new Point(-100, -100);
  
  constructor(private readonly canvas: HTMLCanvasElement) {
    this.context = this.canvas.getContext('2d');
    this.canvasW = this.canvas.width;
    this.canvasH = this.canvas.height;
    
    this.addInteractions();
  }
  
  clearCanvas() {
    this.flowers = [];
    this.context.clearRect(0, 0, this.canvasW, this.canvasH);
  }
  
  private animateFlowers() {
    if (this.flowers.every(f => f.stopChanging)) {
      return;
    }
    this.context.clearRect(0, 0, this.canvasW, this.canvasH);
    this.flowers.forEach(flower => {
      flower.increasePetalRadiusWithLimit();
      flower.draw(this.context);
    });
    window.requestAnimationFrame(() => this.animateFlowers());
  }
  
  private addInteractions() {
    this.canvas.addEventListener('click', e => {
      if (this.ctrlIsPressed) {
        this.clearCanvas();
        return;
      }
      this.calculateMouseRelativePositionInCanvas(e);
      const flower = this.randomizationService
                         .getFlowerAt(this.mousePosition);
      this.flowers.push(flower);
      this.animateFlowers();
    });
    
    window.addEventListener('keydown', (e: KeyboardEvent) => {
      if (e.which === 17 || e.keyCode === 17) {
        this.ctrlIsPressed = true;
      }
    });
    window.addEventListener('keyup', () => {
      this.ctrlIsPressed = false;
    });
  }
  
  private calculateMouseRelativePositionInCanvas(e: MouseEvent) {
    this.mousePosition = new Point(
      e.clientX +
        (document.documentElement.scrollLeft || 
         document.body.scrollLeft) -
        this.canvas.offsetLeft,
      e.clientY +
        (document.documentElement.scrollTop || 
         document.body.scrollTop) -
        this.canvas.offsetTop
    );
  }
}
```

Nous ajoutons un écouteur d'événements pour suivre les événements de clic de la souris et les positions de la souris. Chaque clic ajoutera une fleur au tableau de fleurs. Puisque nous ne voulons pas laisser les fleurs s'étendre à l'infini, nous définissons une méthode `increasePetalRadiusWithLimit()` dans la classe `Flower` pour augmenter le rayon des pétales jusqu'à un incrément de 20. De cette manière, chaque fleur s'épanouira d'elle-même et cessera de s'épanouir après que son rayon de pétale ait augmenté de 20 unités.

J'ai défini un membre privé `stopChanging` dans la fleur pour optimiser l'animation, de sorte que l'animation s'arrêtera lorsque toutes les fleurs auront fini de s'épanouir.

Nous pouvons également écouter les événements `keyup`/`keydown` et ajouter des contrôles clavier au canvas. Dans cette démonstration, le contenu du canvas sera effacé lorsque l'utilisateur maintient la touche CTRL enfoncée et clique avec la souris. La condition de pression de la touche est suivie par le champ `ctrlIsPressed`. De même, vous pouvez ajouter d'autres champs pour suivre d'autres événements clavier afin de faciliter les contrôles granulaires sur le canvas.

Bien sûr, les écouteurs d'événements peuvent être optimisés en utilisant des Observables, surtout lorsque vous utilisez Angular. Vous pouvez jouer avec [le projet StackBlitz ci-dessous](https://stackblitz.com/edit/canvas-interactive-flowers).

%[https://stackblitz.com/edit/canvas-interactive-flowers?embed=1&file=index.ts]

Qu'est-ce qui suit ? Nous pouvons améliorer la démonstration des fleurs interactives en ajoutant des effets sonores et des sprites d'animation. Nous pouvons étudier comment la faire fonctionner de manière fluide sur toutes les plateformes et en faire une PWA ou une application mobile.

J'espère que cet article ajoute de la valeur au sujet des animations Canvas. Encore une fois, le code source est dans [ce dépôt GitHub](https://github.com/changhuixu/canvas-animation-step-by-step) et vous pouvez également jouer avec [ce projet StackBlitz](https://stackblitz.com/edit/canvas-interactive-flowers) et visiter un [site de démonstration](https://flowerscanvas.firebaseapp.com). N'hésitez pas à laisser des commentaires ci-dessous. Merci.

À bientôt !