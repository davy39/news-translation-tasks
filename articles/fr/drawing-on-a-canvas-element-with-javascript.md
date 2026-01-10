---
title: Comment dessiner avec JavaScript sur un élément Canvas HTML – Guide pour débutants
subtitle: ''
author: Hunor Márton Borbély
co_authors: []
series: null
date: '2024-02-08T00:08:11.000Z'
originalURL: https://freecodecamp.org/news/drawing-on-a-canvas-element-with-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Gorillas-Keynote.001-1.png
tags:
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
seo_title: Comment dessiner avec JavaScript sur un élément Canvas HTML – Guide pour
  débutants
seo_desc: 'There are many ways to code graphics for the web. You can create art with
  CSS. You can code an SVG image as part of an HTML file. Or you can generate graphics
  from JavaScript using the Canvas API.

  In this article, we''ll explore how to use JavaScript ...'
---

Il existe de nombreuses façons de coder des graphiques pour le web. Vous pouvez créer de [l'art avec CSS](https://codepen.io/search/pens?q=css+art). Vous pouvez [coder une image SVG](https://www.freecodecamp.org/news/svg-tutorial-learn-to-code-images/) dans un fichier HTML. Ou vous pouvez générer des graphiques à partir de JavaScript en utilisant l'API Canvas.

Dans cet article, nous allons explorer comment utiliser JavaScript pour dessiner quelques formes de base. Vous n'avez pas besoin de prérequis pour ce tutoriel. Nous allons simplement avoir un HTML simple et un fichier JavaScript que vous pouvez exécuter directement dans le navigateur.

Vous vous demandez peut-être – quelqu'un coderait-il une image à partir de JavaScript ? Pour commencer, vous pouvez générer des graphiques dynamiquement en fonction de certaines variables. Par exemple, vous pouvez créer un diagramme. Ou mieux encore, nous pouvons créer un jeu entier avec JavaScript comme nous le couvrons dans [ce tutoriel](https://www.freecodecamp.org/news/gorillas-game-in-javascript/).

%[https://www.freecodecamp.org/news/gorillas-game-in-javascript/]

L'article suivant se concentre sur une partie du tutoriel ci-dessus et vous apprend les bases du dessin avec JS.

## L'élément Canvas

Pour dessiner à l'écran, nous devons d'abord définir un élément canvas en HTML.

```html
<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="utf-8" />
    <title>Canvas</title>
    <script src="index.js" defer></script>
  </head>
    
  <body>
    <canvas id="myCanvas" width="1000" height="1000"></canvas>
  </body>
</html>
```

Cet élément a un ID, afin que nous puissions y accéder en JavaScript. Ici, nous définissons également sa taille. Si la taille est dynamique, nous pouvons également définir cette taille en JavaScript comme nous le faisons dans le tutoriel ci-dessus.

Nous avons défini un élément `<canvas>` en HTML. Comment dessiner dessus ?

Créons un fichier JavaScript séparé, où nous ajouterons le reste du code. Nous chargerons ce fichier avec l'élément script ci-dessus. Ensuite, dans `index.js`, nous obtenons d'abord l'élément canvas par son ID et obtenons son contexte de rendu.

```js
const canvas = document.getElementById("myCanvas"); 
const ctx = canvas.getContext("2d"); 

. . . 
```

Il s'agit d'une API intégrée avec de nombreuses méthodes et propriétés que nous pouvons utiliser pour dessiner sur le canvas. Dans les prochaines sections, nous continuerons avec ce fichier et verrons quelques exemples de l'utilisation de cette API.

### **Comment dessiner un rectangle**

Regardons quelques exemples rapides. La chose la plus basique que nous pouvons faire est de remplir un rectangle.

![Screenshot-2024-01-21-at-23.00.23-1](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-21-at-23.00.23-1.png)
_Utilisation de la méthode <code style="box-sizing: inherit; margin: 0px; padding: 0px 5px 2px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 400 !important; font-stretch: inherit; line-height: 1em; font-family: &quot;Roboto Mono&quot;, monospace; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; font-size: 0.8em; vertical-align: baseline; background: var(--gray15);">fillRect` pour remplir un rectangle_

```js
const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");

ctx.fillStyle = "#58A8D8";

ctx.fillRect(200, 200, 440, 320);
```

Avec la méthode `fillRect`, nous spécifions la coordonnée supérieure gauche de notre rectangle (200, 200), et nous définissons sa largeur et sa hauteur (440, 320).

Par défaut, la couleur de remplissage sera noire. Nous pouvons la changer en définissant la propriété `fillStyle`.

La façon dont le canvas fonctionne est que nous devons définir les paramètres de dessin avant de peindre, et non l'inverse. Ce n'est pas comme si nous peignions un rectangle, puis nous pouvons changer sa couleur. Une fois que quelque chose est sur le canvas, il reste tel quel.

Vous pouvez penser à cela comme à une toile réelle, où vous choisissez également la couleur avec votre pinceau avant de commencer à peindre avec. Ensuite, une fois que vous avez peint quelque chose, vous pouvez soit le couvrir en peignant par-dessus, soit essayer d'effacer le canvas. Mais vous ne pouvez pas vraiment changer les parties existantes. C'est pourquoi nous définissons la couleur ici à l'avance et non après.

### **Comment remplir un chemin**

Nous pouvons bien sûr dessiner des formes plus compliquées également. Nous pouvons définir un chemin, comme ceci :

![Screenshot-2024-01-21-at-23.01.23-1](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-21-at-23.01.23-1.png)
_Remplir un chemin_

```js
const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");

ctx.fillStyle = "#58A8D8";

ctx.beginPath();
ctx.moveTo(200, 200);
ctx.lineTo(500, 350);
ctx.lineTo(200, 500);
ctx.fill();
```

Les chemins commencent avec la méthode `beginPath` et se terminent en appelant soit la méthode `fill`, soit la méthode `stroke` – ou les deux. Entre les deux, nous construisons le chemin en appelant des méthodes de construction de chemin.

Dans cet exemple, nous dessinons un triangle. Nous nous déplaçons vers la coordonnée `200,200` avec la méthode `moveTo`. Ensuite, nous appelons la méthode `lineTo` pour nous déplacer vers le côté droit de notre forme. Puis nous continuons le chemin en appelant à nouveau la méthode `lineTo` vers `200,500`.

Rien de tout cela ne serait visible si nous ne terminions pas avec la méthode `fill` pour remplir le chemin que nous venons de construire.

### **Comment dessiner un trait**

De manière très similaire, nous pouvons également dessiner une ligne. Ici, nous commençons à nouveau avec la méthode `beginPath`. Nous construisons également la forme avec une méthode `moveTo` et deux méthodes `lineTo`. Les coordonnées ici sont les mêmes. Mais à la fin, nous n'appelons pas `fill` mais la méthode `stroke`. Cela, au lieu de remplir la forme, dessine la ligne que nous avons construite.

![Screenshot-2024-01-21-at-23.02.34-1](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-21-at-23.02.34-1.png)
_Dessiner un trait_

```js
const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");

ctx.strokeStyle = "#58A8D8";
ctx.lineWidth = 30;

ctx.beginPath();
ctx.moveTo(200, 200);
ctx.lineTo(500, 350);
ctx.lineTo(200, 500);
ctx.stroke();
```

Les traits ont différentes propriétés de style. Au lieu de la propriété `fillStyle`, nous définissons `strokeStyle`. À cette propriété – et également à `fillStyle` – nous pouvons attribuer toute valeur de couleur valide en CSS. Pour définir la largeur de la ligne, nous utilisons la propriété `lineWidth`.

Nous pouvons également construire des chemins plus complexes. Dans l'exemple ci-dessous, nous dessinons une courbe.

![Screenshot-2024-01-21-at-23.05.04-1](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-21-at-23.05.04-1.png)
_Dessiner une courbe_

```js
const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");

ctx.strokeStyle = "#58A8D8";
ctx.lineWidth = 30;

ctx.beginPath();
ctx.moveTo(200, 300);
ctx.quadraticCurveTo(500, 400, 800, 300);
ctx.stroke();
```

Une courbe quadratique est une courbe simple avec un point de contrôle. Alors que la courbe va du point de départ (que nous définissons avec `moveTo`), la courbe se courbe vers ce point de contrôle (définie comme les deux premiers arguments de la méthode `quadraticCurveTo`) alors qu'elle atteint sa position finale (définie comme les deux derniers arguments).

## Prochaines étapes

Avec ces formes très basiques, nous pouvons déjà aller assez loin. Nous utilisons ces méthodes pour dessiner les gorilles dans le [Tutoriel de jeu Gorillas - JavaScript](https://www.freecodecamp.org/news/gorillas-game-in-javascript/).

![Image](https://www.freecodecamp.org/news/content/images/2024/08/gorilla-drawings.jpg)
_Nous remplissons un chemin pour dessiner le corps et les jambes des gorilles, et utilisons des traits pour dessiner les bras et le visage_

Pour une plongée en profondeur, lisez le [tutoriel complet](https://www.freecodecamp.org/news/gorillas-game-in-javascript/) où nous construisons un jeu complet avec du JavaScript simple. Dans ce tutoriel, nous couvrons non seulement comment dessiner les gorilles et la ligne d'horizon de la ville, mais aussi implémenter toute la logique du jeu. De la gestion des événements, à travers la boucle d'animation, à la détection des impacts.

Pour encore plus, vous pouvez également regarder le [tutoriel étendu sur YouTube](https://www.youtube.com/watch?v=2q5EufbUEQk). Dans la version YouTube, nous couvrons également comment rendre les bâtiments destructibles, comment animer la main du gorille pour suivre le mouvement de glissement lors de la visée, avoir des graphiques plus beaux, et nous ajoutons une logique d'IA, afin que vous puissiez jouer contre l'ordinateur.

Consultez-le pour en savoir plus :

[Contenu intégré](https://www.youtube.com/embed/2q5EufbUEQk?feature=oembed)

Vous pouvez vous abonner à ma chaîne pour plus de tutoriels sur le développement de jeux JavaScript :

%[https://www.youtube.com/channel/UCxhgW0Q5XLvIoXHAfQXg9oQ]