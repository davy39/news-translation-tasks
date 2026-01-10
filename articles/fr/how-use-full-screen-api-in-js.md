---
title: Comment utiliser l'API Fullscreen en JavaScript
subtitle: ''
author: Hunor Márton Borbély
co_authors: []
series: null
date: '2024-02-22T14:17:32.000Z'
originalURL: https://freecodecamp.org/news/how-use-full-screen-api-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Untitled.022.png
tags:
- name: Fullscreen API
  slug: fullscreen-api
- name: canvas
  slug: canvas
- name: JavaScript
  slug: javascript
- name: SVG
  slug: svg
seo_title: Comment utiliser l'API Fullscreen en JavaScript
seo_desc: 'How do you run a game created for the web in fullscreen? In this quick
  tutorial, you''ll see how to display a game or any other HTML element in fullscreen,
  how to exit fullscreen, and how to make a nice fullscreen toggle button in SVG.

  Recently I publ...'
---

Comment exécuter un jeu créé pour le web en plein écran ? Dans ce tutoriel rapide, vous verrez comment afficher un jeu ou tout autre élément HTML en plein écran, comment quitter le mode plein écran et comment créer un joli bouton de bascule pour le plein écran en SVG.

Récemment, j'ai publié un long [tutoriel sur les jeux JavaScript](https://www.freecodecamp.org/news/how-to-draw-a-gorilla-with-javascript-on-html-canvas/). Bien que ce soit un guide très complet, il y avait encore quelques choses que nous n'avons pas pu couvrir : comment afficher le jeu en plein écran.

Lorsque vous regardez une vidéo sur YouTube, vous avez la possibilité de la regarder également en plein écran. Mais saviez-vous que la fonctionnalité de plein écran n'est pas réservée uniquement aux éléments vidéo ?

En JavaScript, il existe une [API Fullscreen](https://developer.mozilla.org/en-US/docs/Web/API/Fullscreen_API). Et elle est surprenamment simple à utiliser. Voici une rapide démonstration de ce que nous allons implémenter. Voyons comment cela fonctionne.

%[https://codepen.io/HunorMarton/pen/QWoRLXM]

Vous pouvez également [regarder cet article sous forme de vidéo](https://www.youtube.com/watch?v=jX3mIQdQQ2w&t=15s) sur YouTube.

## Table des matières :

* [Comment entrer en mode plein écran](#heading-comment-entrer-en-mode-plein-ecran)
* [Comment styliser le plein écran](#heading-comment-styliser-le-plein-ecran)
* [Comment afficher des jeux avec l'élément Canvas en plein écran](#heading-comment-afficher-des-jeux-avec-lelement-canvas-en-plein-ecran)
* [Comment quitter le mode plein écran](#heading-comment-quitter-le-mode-plein-ecran)
* [Comment coder une icône de plein écran avec SVG](#heading-comment-coder-une-icone-de-plein-ecran-avec-svg)
* [En savoir plus](#heading-en-savoir-plus)

## Comment entrer en mode plein écran

Imaginons que nous avons un site web simple avec du texte. Et en bas, nous avons un bouton qui affichera le texte en plein écran. Nous allons améliorer l'apparence de ce bouton, mais d'abord, travaillons sur la logique principale.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-21-at-18.20.51.png)
_Un site web simple avec du texte et un bouton Basculer en plein écran_

```css
body {
  font-family: Montserrat;
  margin: 50px;
  max-width: 500px;
}
```

Dans le code ci-dessus, nous avons attaché un gestionnaire d'événements au bouton en HTML. Nous pouvons ensuite implémenter la logique de la fonction `toggleFullscreen` en JavaScript.

Dans cette fonction, tout ce que nous avons à faire est d'appeler la méthode `requestFullScreen` sur la propriété `documentElement` du `document`. Et c'est tout :

```js
function toggleFullscreen() {
  document.documentElement.requestFullscreen();
}
```

Si vous cliquez sur le bouton, votre site web passera en plein écran.

## Comment styliser le plein écran

Avant de couvrir comment quitter le mode plein écran et créer un joli bouton de bascule, voyons quelques autres choses.

Ce que vous pourriez remarquer tout de suite, c'est qu'avec plus d'espace, votre contenu pourrait se perdre un peu sur un écran complet. Assurez-vous d'avoir un style réactif qui a fière allure sur chaque taille d'écran.

Vous pouvez même styliser la mise en page spécifiquement pour le plein écran. En CSS, vous pouvez définir une requête média qui n'applique le style que si le `display-mode` est `fullscreen`.

Par exemple, vous pouvez changer la taille de la police ou changer la `background-color` pour avoir un aspect distinct en plein écran.

```css
@media (display-mode: fullscreen) {
  body {
    background-color: #f9bb86;
    font-size: 1.2em;
  }
}
```

## Comment afficher des jeux avec l'élément Canvas en plein écran

Dans ce cas, nous voulons qu'un jeu utilisant l'élément `canvas` soit en plein écran – comme le jeu [Gorillas](https://www.freecodecamp.org/news/how-to-draw-a-gorilla-with-javascript-on-html-canvas/) – nous devons également redimensionner l'élément `canvas` pour qu'il s'adapte à tout l'écran.

Dans ce cas, nous pouvons utiliser l'événement `resize` de la fenêtre. L'événement est déclenché à la fois lorsque nous redimensionnons simplement la fenêtre du navigateur et lorsque nous entrons ou quittons le mode plein écran.

Avec l'événement `resize`, nous pouvons redimensionner l'élément `canvas` pour qu'il s'adapte à tout l'écran, mettre à jour la mise à l'échelle, ajuster toute autre propriété que nous devons changer lors du redimensionnement et redessiner toute la scène.

```js
window.addEventListener("resize", () => {
  // Redimensionner l'élément canvas
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;

  // Mettre à jour la mise à l'échelle
  // . . .

  // Ajuster les propriétés dépendantes de la taille
  // . . .

  // Redessiner le canvas
  draw();
});
```

Si vous consultez le code source du [jeu Gorillas sur CodePen](https://codepen.io/HunorMarton/pen/jOJZqvp), vous trouverez des étapes similaires.

## Comment quitter le mode plein écran

Maintenant que nous savons comment entrer en mode plein écran, comment en sortir ?

Par défaut, si vous appuyez sur la touche `Échap`, le navigateur revient à la vue normale. Dans Google Chrome, vous obtenez même une notification en haut de l'écran à ce sujet lorsque vous entrez en mode plein écran.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-21-at-17.47.03-2.png)
_Google Chrome affiche une notification en haut de l'écran une fois que vous entrez en plein écran_

Que faire si vous souhaitez quitter le mode plein écran en cliquant sur le bouton HTML ? Modifions le comportement de notre bouton pour basculer le mode plein écran.

```js
function toggleFullscreen() {
  if (!document.fullscreenElement) {
    document.documentElement.requestFullscreen();
  } else {
    document.exitFullscreen();
  }
}
```

Tout d'abord, nous commençons par vérifier si nous sommes déjà en mode plein écran. Nous pouvons le faire en vérifiant la propriété `fullscreenElement` du `document`. Si elle est indéfinie, alors nous entrons en mode plein écran de la même manière que précédemment. Et si nous sommes déjà en mode plein écran, alors nous pouvons en sortir en appelant la méthode `exitFullscreen` du document.

C'est vraiment aussi simple. Avec quelques lignes de code, nous pouvons implémenter la logique pour un bouton de bascule de plein écran.

## Comment coder une icône de plein écran avec SVG

Si vous suivez [mes tutoriels](https://www.freecodecamp.org/news/author/hunor/), vous savez que j'adore le codage créatif et [dessiner à partir de code](https://www.freecodecamp.org/news/svg-tutorial-learn-to-code-images/). Alors améliorons l'apparence de notre bouton pour qu'il ressemble à ce que nous avons sur YouTube.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-21-at-18.06.07.png)
_Icône de plein écran_

Créons une image SVG dans notre bouton. Si vous consultez le code source de YouTube, vous verrez qu'ils utilisent également un SVG.

Définissons un élément SVG dans HTML. Nous allons définir sa taille à 30 x 30 et définir un élément `path` :

```html
. . .

<button onclick="toggleFullscreen()">
  <svg width="30" height="30">
    <path
      stroke="black"
      stroke-width="3"
      fill="none"
      d="
        M 10, 2 L 2,2 L 2, 10
        M 20, 2 L 28,2 L 28, 10
        M 28, 20 L 28,28 L 20, 28
        M 10, 28 L 2,28 L 2, 20"
    />
  </svg>
</button>

. . .
```

Pour styliser le chemin, nous avons défini sa couleur avec la propriété `stroke`, défini sa `stroke-width` et nous avons veillé à ne pas obtenir une forme remplie. Les chemins SVG sont par défaut remplis, nous devons donc définir explicitement que nous ne voulons pas `remplir` cette forme.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-21-at-18.02.10.png)
_Utilisation des commandes move-to et line-to dans un chemin SVG_

Ensuite, nous avons défini le chemin avec quelques commandes move-to et line-to. Nous pouvons définir ces commandes sous forme de chaîne dans l'attribut `d` de l'élément path.

Nous avons commencé par une commande move-to : `M 10, 2`. La lettre `M` indique que nous avons une commande move-to, et les 10 et 2 sont les coordonnées `x` et `y` de cette commande. Nous nous sommes déplacés au début de l'une des quatre lignes.

Ensuite, nous avons continué le chemin avec une commande line-to qui se déplace vers le coin, puis avec une autre commande line-to. La commande line-to fonctionne de manière similaire. Elle commence par la lettre `L`, puis nous définissons des coordonnées `x, y` où la ligne doit aller.

Ensuite, nous avons fait de même avec les autres coins. Nous nous déplaçons vers le segment de ligne suivant avec une autre commande move-to et dessinons une ligne avec deux autres commandes line-to.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Untitled.021.png)
_Dessiner un chemin sur un élément Canvas avec JavaScript a quelques similitudes avec la définition d'un chemin en SVG_

**Note** : Si vous avez lu mon [précédent tutoriel](https://www.freecodecamp.org/news/how-to-draw-a-gorilla-with-javascript-on-html-canvas/) sur la façon de créer le jeu des gorilles, vous avez peut-être remarqué que nous avions quelque chose de similaire là-bas. Nous avons également dessiné des chemins avec move to et line to. Sauf que là, nous dessinions sur un élément `canvas` avec JavaScript, et maintenant nous avons les commandes sous forme de chaîne dans le fichier HTML.

### Comment basculer l'apparence de l'icône

Maintenant, le SVG a fière allure, mais que faire si nous voulons avoir un aspect différent lorsque nous sommes en mode plein écran ? Sur YouTube, lorsque nous entrons en mode plein écran, le bouton passe à une autre icône.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-21-at-18.06.33.png)
_Les deux faces de l'icône de plein écran_

Vous pouvez faire cela de différentes manières. La manière la plus simple est probablement de définir un autre chemin, dans le même élément SVG avec un aspect différent. Ensuite, rendez ce chemin transparent par défaut. Nous allons basculer la visibilité de ces deux chemins en JavaScript.

```html
. . .

<button onclick="toggleFullscreen()">
  <svg width="30" height="30">
    <path
      id="enter-fullscreen"
      stroke="black"
      stroke-width="3"
      fill="none"
      d="
        M 10, 2 L 2,2 L 2, 10
        M 20, 2 L 28,2 L 28, 10
        M 28, 20 L 28,28 L 20, 28
        M 10, 28 L 2,28 L 2, 20"
    />
    <path
      id="exit-fullscreen"
      stroke="transparent"
      stroke-width="3"
      fill="none"
      d="
        M 10, 2 L 10,10 L 2, 10
        M 20, 2 L 20,10 L 28, 10
        M 28, 20 L 20,20 L 20, 28
        M 10, 28 L 10,20 L 2, 20"
    />
  </svg>
</button>

. . .
```

Ce deuxième chemin est très similaire au précédent. Sauf que nous avons utilisé des coordonnées différentes pour certaines des commandes line-to.

Ensuite, nous avons défini des ID uniques pour ces deux chemins, et nous mettons à jour notre fonction de bascule en JavaScript. En JavaScript, nous obtenons une référence à ces chemins par ID, puis dans le gestionnaire d'événements du bouton de bascule, nous pouvons basculer la visibilité de ces éléments.

```js
const enterFullscreen = document.getElementById("enter-fullscreen");
const exitFullscreen = document.getElementById("exit-fullscreen");

function toggleFullscreen() {
  if (!document.fullscreenElement) {
    document.documentElement.requestFullscreen();
    enterFullscreen.setAttribute("stroke", "transparent");
    exitFullscreen.setAttribute("stroke", "black");
  } else {
    document.exitFullscreen();
    enterFullscreen.setAttribute("stroke", "black");
    exitFullscreen.setAttribute("stroke", "transparent");
  }
}
```

Maintenant, si vous cliquez sur ce bouton, il bascule le mode plein écran et change son apparence.

## En savoir plus

Si vous souhaitez en savoir plus sur les SVG, consultez [SVG-Tutorial.com](http://SVG-Tutorial.com) où vous trouverez de nombreux exemples, des bases aux niveaux plus avancés. C'est un site gratuit et vous pouvez également trouver l'exemple que nous avons discuté dans cet article.

Pour utiliser le bouton afin d'exécuter un jeu JavaScript en plein écran, consultez le tutoriel complet sur les jeux JavaScript pour recréer le jeu classique Gorillas ici sur [freeCodeCamp](https://www.freecodecamp.org/news/how-to-draw-a-gorilla-with-javascript-on-html-canvas/) ou sur [YouTube](https://www.youtube.com/watch?v=2q5EufbUEQk&t=2337s). C'est un tutoriel massif qui couvre des sujets allant du dessin sur un élément HTML Canvas, à toute la logique du jeu, de la gestion des événements, en passant par la boucle d'animation, la détection des collisions et même la logique IA pour le gorille ennemi.

%[https://www.youtube.com/watch?v=2q5EufbUEQk&t=2337s]

Vous pouvez vous abonner à ma chaîne pour plus de tutoriels sur le développement de jeux JavaScript :

%[https://www.youtube.com/channel/UCxhgW0Q5XLvIoXHAfQXg9oQ]