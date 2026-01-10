---
title: Tutoriel sur le bouton bascule SVG – Comment gérer le mode sombre avec CSS
  et JavaScript
subtitle: ''
author: Hunor Márton Borbély
co_authors: []
series: null
date: '2024-03-08T13:46:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-handle-dark-mode-with-css-and-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/thumbnail.png
tags:
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: SVG
  slug: svg
- name: Web Development
  slug: web-development
seo_title: Tutoriel sur le bouton bascule SVG – Comment gérer le mode sombre avec
  CSS et JavaScript
seo_desc: 'How can you detect dark mode in CSS and JavaScript? How can you manually
  override it with a toggle button? And how can you create a sun and moon icon with
  SVG?

  In this tutorial, you will learn how to detect dark mode in CSS and JavaScript,
  and you wi...'
---

Comment détecter le mode sombre en CSS et JavaScript ? Comment le remplacer manuellement avec un bouton bascule ? Et comment créer une icône de soleil et de lune avec SVG ?

Dans ce tutoriel, vous apprendrez à détecter le mode sombre en CSS et JavaScript, et vous créerez un bouton bascule avec SVG pour remplacer le comportement par défaut. Vous utiliserez du HTML, CSS et JavaScript simples, donc vous n'avez besoin d'aucune exigence préliminaire avant de commencer.

Vous pouvez également [regarder cet article sous forme de vidéo](https://youtu.be/GUSUA72t7p0) sur YouTube.

## Table des matières

* [Comment gérer le mode sombre avec CSS](#heading-comment-gerer-le-mode-sombre-avec-css)
* [Comment coder une icône de soleil avec SVG](#heading-comment-coder-une-icone-de-soleil-avec-svg)
* [Comment détecter le mode sombre en JavaScript](#heading-comment-detecter-le-mode-sombre-en-javascript)
* [Comment coder une icône de lune avec SVG](#heading-comment-coder-une-icone-de-lune-avec-svg)
* [Comment basculer le mode sombre avec JavaScript](#heading-comment-basculer-le-mode-sombre-avec-javascript)
* [Prochaines étapes](#prochaines-etapes)

## Comment gérer le mode sombre avec CSS

Supposons que vous avez un site web simple avec du texte. Par défaut, vous définissez la couleur du texte en noir et la couleur de fond en blanc. La mise en œuvre du mode sombre pour ce site avec CSS est très simple :

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Mode Sombre</title>
    <link rel="stylesheet" href="index.css" />
    <script src="index.js" defer></script>
  </head>

  <body>
    <p>
      Comment détecter le mode sombre en CSS et en JavaScript ? Comment pouvons-nous le remplacer
      manuellement avec un bouton bascule ? Dans ce tutoriel rapide, nous examinons
      la détection du mode sombre en CSS et JavaScript, puis nous créons un bouton bascule
      avec SVG pour remplacer le comportement par défaut.
    </p>
  </body>
</html>

```

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Screenshot-2024-03-07-at-11.33.28.png)
_Un site web simple avec du texte en mode sombre_

Tout ce que vous avez à faire est d'ajouter une requête média et de définir une condition. Avec cette condition, vous définissez les déclarations CSS suivantes pour qu'elles soient valides uniquement si le schéma de couleur préféré est sombre.

À l'intérieur de cette requête média, vous pouvez définir les couleurs pour le mode sombre. Dans ce cas, vous inversez les couleurs et définissez la couleur du texte en blanc et la couleur de fond en noir :

```css
body {
  font-family: Montserrat;
  margin: 50px;
  max-width: 500px;
}

@media (prefers-color-scheme: dark) {
  body {
    background-color: black;
    color: white;
  }
}

```

Cela prendra le paramètre de votre système d'exploitation ou du paramètre du navigateur. Par défaut, il provient du système d'exploitation, mais le navigateur peut décider de le remplacer. Dans Google Chrome, vous pouvez trouver ce paramètre sous "Apparence". Par défaut, il suit le paramètre de l'appareil.

Ce qui est génial avec la solution CSS, c'est que si vous changez ce paramètre pendant la visite du site web, le style sera mis à jour automatiquement.

De cette manière, vous pouvez définir un style personnalisé pour l'élément body et tout autre élément également.

Cela ne fonctionne pas dans un cas, cependant. Vous ne pouvez pas styliser ce qui se trouve à l'intérieur d'un élément HTML Canvas avec CSS. Si vous avez construit un [jeu entièrement en JavaScript](https://www.freecodecamp.org/news/gorillas-game-in-javascript/) en utilisant l'API Canvas ou Three.js, vous devez également définir les couleurs pour le mode sombre en JavaScript.

Dans les prochaines étapes, nous couvrirons cela et examinerons comment créer un bouton bascule SVG pour passer entre les modes clair et sombre.

## Comment coder une icône de soleil avec SVG

Avant d'apprendre à gérer le mode sombre en JavaScript, faisons un petit détour et voyons comment coder un bouton bascule de mode sombre avec SVG. Détecter le mode sombre est une chose, mais vous devriez permettre à l'utilisateur de basculer manuellement entre les modes clair et sombre.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Slides-1.022.png)
_Icône de soleil_

Consultez mon tutoriel précédent si vous avez besoin d'une introduction rapide au [codage des icônes SVG](https://www.freecodecamp.org/news/svg-tutorial-learn-to-code-images/). Il contient de nombreux exemples, du niveau débutant au niveau avancé. Et si vous êtes nouveau dans les SVG, ne vous inquiétez pas. Ce sont des exemples très simples.

Commençons donc par l'élément `svg`. Cela servira de conteneur pour tous les éléments d'image. Définissez sa taille à 30 fois 30 :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Slides-1.004.png)
_L'élément `svg`_

Ensuite, ajoutez un cercle. Pour un élément `circle`, vous devez définir les coordonnées du centre du cercle et son rayon. Les coordonnées du centre sont toutes deux à 15, et le rayon est à 6. Ensuite, définissez une couleur avec la propriété `fill` :

```html
<svg width="30" height="30">
  <circle cx="15" cy="15" r="6" fill="currentColor" />
</svg>
```

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Slides-1.006.png)
_Nous ajoutons un `circle` comme noyau du soleil_

Pour définir la couleur, vous pouvez utiliser la propriété `currentColor` qui reprend le paramètre `color` actuel du CSS. Cela sera utile plus tard lorsque vous basculerez entre les modes sombre et clair. L'icône changera de couleur automatiquement.

Ensuite, ajoutez les rayons du soleil. Vous devez utiliser l'élément `line` pour cela, où vous devez définir les coordonnées de début et de fin. Vous pouvez également définir la couleur de trait avec la propriété `stroke`, la `stroke-width` pour ajouter de l'épaisseur, et la propriété `stroke-linecap` pour arrondir les extrémités des lignes :

```html
<svg width="30" height="30">
  <circle cx="15" cy="15" r="6" fill="currentColor" />

  <line
    id="ray"
    stroke="currentColor"
    stroke-width="2"
    stroke-linecap="round"
    x1="15"
    y1="1"
    x2="15"
    y2="4"
  ></line>
</svg>
```

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Slides-1.010.png)
_Nous ajoutons un élément `line` comme rayon de soleil_

Maintenant, une fois que vous avez un rayon, vous pouvez réutiliser le même rayon pour dessiner les autres.

Vous pouvez donner à ce rayon un `id` et le réutiliser avec l'élément `use`. Pour les éléments réutilisés, vous pouvez définir une rotation. Définissez l'angle de rotation et le centre de rotation. Vous voulez faire tourner les rayons autour du centre du soleil, donc définissez-le à `15,15`. Ensuite, incrémentez la rotation de 45 degrés pour chaque rayon :

```html
<svg width="30" height="30">
  <circle cx="15" cy="15" r="6" fill="currentColor" />

  <line
    id="ray"
    stroke="currentColor"
    stroke-width="2"
    stroke-linecap="round"
    x1="15"
    y1="1"
    x2="15"
    y2="4"
  ></line>

  <use href="#ray" transform="rotate(45 15 15)" />
  <use href="#ray" transform="rotate(90 15 15)" />
  <use href="#ray" transform="rotate(135 15 15)" />
  <use href="#ray" transform="rotate(180 15 15)" />
  <use href="#ray" transform="rotate(225 15 15)" />
  <use href="#ray" transform="rotate(270 15 15)" />
  <use href="#ray" transform="rotate(315 15 15)" />
</svg>
```

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Slides-1.016.png)
_L'icône de soleil terminée_

## Comment détecter le mode sombre en JavaScript

Avant de passer à l'icône de lune, voyons comment détecter le mode sombre en JavaScript. Cela peut être utile lors de la création d'un jeu, comme nous l'avons fait il y a quelques semaines dans le [tutoriel du jeu Gorillas en JavaScript](https://www.freecodecamp.org/news/gorillas-game-in-javascript/).

Dans ce jeu, nous dessinions sur un élément HTML Canvas avec JavaScript. Nous avons défini toutes les couleurs avec JavaScript. Si nous voulons prendre en charge le mode sombre, nous pouvons définir les couleurs en fonction d'une variable `darkMode`. Mais comment détecter si nous sommes en mode sombre ? Comment définir la valeur de cette variable ?

Le code suivant est un exemple extrait du tutoriel de jeu ci-dessus. Ici, nous définissons la couleur de remplissage avant de dessiner un rectangle sur le canevas. Pour en savoir plus sur le dessin sur un élément `canvas`, consultez [ce tutoriel](https://www.freecodecamp.org/news/gorillas-game-in-javascript/).

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Slides-1.018.png)
_Lors du dessin sur un élément `canvas`, nous définissons les couleurs à partir de JavaScript. Mais comment détecter le mode sombre ?_

Détecter le mode sombre en JavaScript est également très simple. Intéressamment, cette solution dépend également des sélecteurs de requête CSS que vous avez utilisés auparavant.

Vous pouvez créer un objet `matchMedia` avec la même condition que celle utilisée en CSS. Cette méthode peut vérifier si le document correspond à une requête média. Transmettez `prefers-color-scheme: dark` comme argument :

```javascript
const darkModeMediaQuery = window.matchMedia("(prefers-color-scheme: dark)");

let darkMode = darkModeMediaQuery.matches;

. . .

function drawBuildings() {
  state.buildings.forEach((building) => {
    ctx.fillStyle = darkMode ? "#254D7E" : "#947285";
    ctx.fillRect(building.x, 0, building.width, building.height);
  });
}
```

Ensuite, vous pouvez vérifier la propriété `matches` de cet objet. Si elle est vraie, alors vous êtes en mode sombre. Vous pouvez enregistrer cela dans une variable, et plus tard, vous pouvez utiliser cette variable pour décider quelles couleurs vous devez utiliser lors de la peinture sur l'élément canvas.

Cette variable, cependant, ne se rafraîchit pas automatiquement lorsque vous basculez entre le mode clair et le mode sombre. Vous devez ajouter un écouteur d'événement qui détecte si les paramètres changent.

Ici, nous définissons une fonction qui vérifie la propriété `matches` de l'objet entrant pour décider si vous venez de basculer en mode clair ou sombre :

```javascript
const darkModeMediaQuery = window.matchMedia("(prefers-color-scheme: dark)");

let darkMode = darkModeMediaQuery.matches;

darkModeMediaQuery.addEventListener("change", (e) => {
  if (e.matches) {
    darkMode = true;
  } else {
    darkMode = false;
  }
});

. . .

function drawBuildings() {
  state.buildings.forEach((building) => {
    ctx.fillStyle = darkMode ? "#254D7E" : "#947285";
    ctx.fillRect(building.x, 0, building.width, building.height);
  });
}
```

Maintenant, si vous définissez les couleurs en fonction de cette variable `darkMode`, vous devriez voir que l'apparence du jeu change une fois que vous basculez entre le mode clair et le mode sombre dans les paramètres du système d'exploitation. Consultez cette [démo](https://codepen.io/HunorMarton/pen/jOJZqvp) pour voir cela en action.

## Comment coder une icône de lune avec SVG

Avant de discuter de la substitution du paramètre par défaut du système d'exploitation avec un bouton bascule, examinons l'autre moitié de notre icône de bascule : dessinons une lune.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Slides-1.023.png)
_Les icônes de soleil et de lune_

Commencez par un élément `svg` de la même taille et définissez un chemin à l'intérieur. Vous pouvez définir un élément `path` en définissant son attribut `d`. Dans cet attribut, vous construisez un chemin à partir d'une série de commandes :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Slides-1.026.png)
_Nous définissons un `path` avec une série de commandes_

Vous commencez par la commande move-to pour aller à la position initiale. Cette commande se compose de la lettre `M` et de la coordonnée de départ :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Slides-1.027.png)
_Utilisation de la commande move-to dans un chemin_

Ensuite, utilisez une commande d'arc pour dessiner l'arc extérieur de la lune. Cette commande peut sembler un peu effrayante car elle a plusieurs propriétés. Voyons ce que nous avons :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Slides-1.028.png)
_La commande d'arc et ses plusieurs propriétés_

Une commande continue toujours la commande précédente, donc cet arc dessine l'arc à partir des coordonnées de la commande move-to. Les commandes se terminent également par les coordonnées du point final.

Ici, vous définissez où l'arc se termine. Le reste des propriétés concerne la manière de dessiner un arc du point de départ au point final :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Slides-1.029.png)
_Les deux dernières propriétés de la commande d'arc montrent le point final de l'arc_

Les deux premières propriétés sont le rayon horizontal et vertical de notre arc. Dans notre cas, nous voulons avoir l'arc d'un cercle, donc nous définissons la même valeur pour les deux. Avec le troisième argument, vous pouvez définir une rotation. Lorsque les deux rayons sont identiques, cette propriété ne fait aucune différence. Vous pouvez la laisser à zéro :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Slides-1.030.png)
_Rayon horizontal et vertical de l'arc_

Ensuite, nous avons la propriété de l'indicateur de grand arc. Avec cela, vous pouvez décider d'aller par le chemin long ou court vers notre coordonnée finale. Vous pouvez voir que vous pouvez atteindre le point final de plusieurs manières, même avec les mêmes rayons.

Il y a deux arcs – dans le cas du premier, vous allez par le chemin long et dans le cas du second, vous irez par le chemin court. Il s'agit d'un indicateur, donc la valeur ici peut être 0 ou 1 :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Slides-1.032.png)
_L'indicateur de grand arc décide si nous devons atteindre le point final par le chemin court ou le chemin long_

Enfin, il y a l'indicateur de balayage. Cela définit essentiellement si vous devez dessiner l'arc dans le sens des aiguilles d'une montre ou dans le sens inverse. Les deux options se reflètent l'une l'autre. Dans le premier cas, vous définissez cela à zéro – dans le second, vous le définissez à un :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Slides-1.035.png)
_L'indicateur de balayage décide si nous devons aller dans le sens des aiguilles d'une montre ou dans le sens inverse_

Maintenant que vous avez un arc, vous configurez l'autre. Ici, vous définissez le point final au début. Aux mêmes coordonnées que vous avez utilisées pour la commande move-to.

Ensuite, vous pouvez utiliser les mêmes rayons, mais vous devez changer l'indicateur de grand arc et l'indicateur de balayage pour obtenir une lune :

```html
<svg width="30" height="30">
  <path
    fill="currentColor"
    d="
      M 23, 5
      A 12 12 0 1 0 23, 25
      A 12 12 0 0 1 23, 5"
  />
</svg>
```

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Slides-1.039.png)
_L'icône de lune terminée_

Comment pouvez-vous utiliser ces deux icônes dans un bouton pour basculer entre le mode clair et le mode sombre en JavaScript ?

## Comment basculer le mode sombre avec JavaScript

Si vous souhaitez remplacer les paramètres du système ou du navigateur pour le mode sombre avec un commutateur manuel, vous ne pouvez plus compter sur la requête média CSS. Cela fonctionne pour le rendu de l'interface utilisateur en fonction des paramètres, mais vous ne pouvez pas le remplacer à partir de JavaScript.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Slides-1.041.png)
_Vous ne pouvez pas remplacer une requête média CSS_

Au lieu de cela, vous pouvez définir une classe `dark-mode` et la basculer à partir de JavaScript.

En CSS, définissez une classe qui changera les mêmes paramètres que la requête média faisait auparavant. Ensuite, en JavaScript, vous pouvez utiliser la même logique que vous aviez auparavant pour obtenir le paramètre par défaut et ensuite ajouter ou supprimer cette classe.

Vous pouvez définir cette classe lors du chargement initial de la page et la basculer si vous cliquez sur un bouton :

```css
body {
  font-family: Montserrat;
  margin: 50px;
  max-width: 500px;
}

.dark-mode {
  background-color: black;
  color: white;
}
```

Maintenant, comment basculer cela avec un bouton ? Dans votre fichier HTML, ajoutez un élément bouton avec un gestionnaire d'événements. Ensuite, déplacez les deux SVG à l'intérieur de cet élément bouton et attribuez-leur des ID. Vous basculerez la visibilité de ces icônes à partir de JavaScript :

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Mode Sombre</title>
    <link rel="stylesheet" href="index.css" />
    <script src="index.js" defer></script>
  </head>

  <body>
    <p>
      Comment détecter le mode sombre en CSS et en JavaScript ? Comment pouvons-nous le remplacer
      manuellement avec un bouton bascule ? Dans ce tutoriel rapide, nous examinons
      la détection du mode sombre en CSS et JavaScript, puis nous créons un bouton bascule
      avec SVG pour remplacer le comportement par défaut.
    </p>

    <button onclick="toggleDarkMode()">
      <svg width="30" height="30" id="light-icon">
        <circle cx="15" cy="15" r="6" fill="currentColor" />

        <line
          id="ray"
          stroke="currentColor"
          stroke-width="2"
          stroke-linecap="round"
          x1="15"
          y1="1"
          x2="15"
          y2="4"
        ></line>

        <use href="#ray" transform="rotate(45 15 15)" />
        <use href="#ray" transform="rotate(90 15 15)" />
        <use href="#ray" transform="rotate(135 15 15)" />
        <use href="#ray" transform="rotate(180 15 15)" />
        <use href="#ray" transform="rotate(225 15 15)" />
        <use href="#ray" transform="rotate(270 15 15)" />
        <use href="#ray" transform="rotate(315 15 15)" />
      </svg>
      <svg width="30" height="30" id="dark-icon">
        <path
          fill="currentColor"
          d="
          M 23, 5
          A 12 12 0 1 0 23, 25
          A 12 12 0 0 1 23, 5"
        />
      </svg>
    </button>
  </body>
</html>

```

Vous pouvez également annuler l'apparence par défaut de l'élément bouton en CSS, sauf la propriété cursor. Vous devriez l'avoir comme pointer :

```css
. . .

button {
  all: unset;
  cursor: pointer;
}

. . .
```

Maintenant, implémentons le gestionnaire d'événements en JavaScript. Tout d'abord, vous devez accéder aux icônes SVG par ID :

```js
const lightIcon = document.getElementById("light-icon");
const darkIcon = document.getElementById("dark-icon");

. . .
```

Ensuite, ajoutez la classe `dark-mode` à l'élément `body` au cas où vous seriez en mode sombre et masquez l'une des icônes SVG en fonction de la variable `darkMode`. Vous détectez le mode sombre comme vous l'avez fait auparavant :

```js
. . .

// Vérifier si le mode sombre est préféré
const darkModeMediaQuery = window.matchMedia("(prefers-color-scheme: dark)");
let darkMode = darkModeMediaQuery.matches;

// Définir la classe dark-mode sur le body si darkMode est vrai et choisir l'icône
if (darkMode) {
  document.body.classList.add("dark-mode");
  darkIcon.setAttribute("display", "none");
} else {
  lightIcon.setAttribute("display", "none");
}

. . .
```

Et enfin, vous pouvez implémenter la fonction qui inverse la propriété `darkMode`. Cette fonction bascule la classe `dark-mode` sur l'élément body, et bascule les icônes SVG :

```js
. . .

// Basculer le mode sombre lors du clic sur le bouton
function toggleDarkMode() {
  // Basculer la variable darkMode
  darkMode = !darkMode;

  // Basculer la classe dark-mode sur le body
  document.body.classList.toggle("dark-mode");

  // Basculer les icônes clair et sombre
  if (darkMode) {
    lightIcon.setAttribute("display", "block");
    darkIcon.setAttribute("display", "none");
  } else {
    lightIcon.setAttribute("display", "none");
    darkIcon.setAttribute("display", "block");
  }
}
```

Maintenant, cela fonctionne : par défaut, vous avez toujours le paramètre du système d'exploitation ou du navigateur. Mais une fois que vous cliquez sur ce bouton, il le remplacera manuellement.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Screenshot-2024-03-07-at-12.31.42.png)
_Apparence finale en mode clair_

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Screenshot-2024-03-07-at-12.31.27.png)
_Apparence finale en mode sombre_

## Prochaines étapes

Avec tout cela en place, vous avez une fonctionnalité qui prend le paramètre de mode sombre du navigateur ou du système d'exploitation par défaut, et vous pouvez le remplacer avec un bouton bascule esthétique. Dans la [version YouTube de ce tutoriel](https://youtu.be/GUSUA72t7p0), vous pouvez également apprendre à utiliser `localStorage` pour enregistrer ce paramètre pour la prochaine session.

Si vous souhaitez en savoir plus sur les SVG, consultez [SVG-tutorial.com](https://svg-tutorial.com/), où vous pouvez en apprendre davantage sur les SVG, des niveaux débutant à avancé, avec de nombreux exemples.

Si vous souhaitez utiliser ce comportement dans un jeu, consultez le [tutoriel du jeu Gorillas en JavaScript](https://www.freecodecamp.org/news/gorillas-game-in-javascript/), où nous construisons le jeu entier à partir de zéro. C'est un tutoriel massif de deux heures qui couvre le dessin sur un élément Canvas avec JavaScript et toute la logique du jeu avec du JavaScript simple.

%[https://youtu.be/2q5EufbUEQk?si=MIWVN_3MlFlKRC_G]

Abonnez-vous à ma chaîne pour plus de tutoriels sur le développement de jeux JavaScript :

%[https://www.youtube.com/channel/UCxhgW0Q5XLvIoXHAfQXg9oQ]