---
title: Comment créer une application photo sur le Web – Aucun plugin requis
subtitle: ''
author: Felix Favour Chinemerem
co_authors: []
series: null
date: '2024-02-23T00:36:03.000Z'
originalURL: https://freecodecamp.org/news/build-a-camera-app-on-the-web
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/supercharged-animations.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Comment créer une application photo sur le Web – Aucun plugin requis
seo_desc: 'Ever had to make a video call right on your browser with Google Meet, Zoom,
  or any other video chat app? Well, here’s what you might have never thought to ask—how
  does it work?

  Well, there are a number of things that make a real-time video chat appli...'
---

Avez-vous déjà dû passer un appel vidéo directement dans votre navigateur avec Google Meet, Zoom ou toute autre application de chat vidéo ? Eh bien, voici ce que vous n'avez peut-être jamais pensé à demander – comment cela fonctionne-t-il ?

Eh bien, il y a un certain nombre de choses qui rendent une application de chat vidéo en temps réel entièrement fonctionnelle sur le web. Dans cet article, nous explorerons comment vous pouvez accéder au contenu multimédia via la caméra de votre appareil. Et nous construirons une application photo au cours de notre exploration.

Admettons-le, utiliser l'API MediaStream pour construire une application photo ne raconte pas toute l'histoire. Mais voici ce que je peux vous promettre : nous faisons le premier pas dans la bonne direction.

Avant de commencer, jetez un coup d'œil à ce que vous devriez être capable de créer à la fin de cet article [ici](https://camera-demo-rho.vercel.app/). Maintenant que vous êtes prêt, mettons-nous au travail !

## Prérequis

Avant de plonger, assurons-nous de quelques choses. Cet article est conçu pour les débutants, mais avoir les bonnes ressources garantira une expérience fluide. Voici ce dont vous aurez besoin :

* Une compréhension très basique de HTML, CSS et JavaScript – des connaissances de niveau débutant sont absolument suffisantes.
* Une compréhension basique du [Document Object Model](https://www.freecodecamp.org/news/javascript-dom/) en JavaScript.
* Dernier point mais non des moindres, une bonne musique de fond – je vous laisse choisir celle-ci vous-même, [mais il y a toujours freeCodeCamp radio](https://coderadio.freecodecamp.org/).

Ok, maintenant nous sommes prêts.

## Qu'est-ce que l'API MediaStream ?

L'API MediaStream Recording aide le navigateur à capturer des flux de données audio-visuelles. Elle est importante pour notre cas d'utilisation, car toute image que nous capturons doit être stockée dans un objet [MediaStream](https://developer.mozilla.org/en-US/docs/Web/API/MediaStream).

L'API MediaStream fait plus que capturer des photos et des vidéos. Elle aide également à traiter et analyser les données MediaStream directement dans le navigateur. Aussi complexe que tout cela puisse paraître, il vous intéressera de savoir que l'API MediaStream est surprenamment facile à utiliser.

Notre application photo la rend encore plus facile.

## Composants de notre application photo

![Image](https://www.freecodecamp.org/news/content/images/2024/02/supercharged-animations--3-.png)

Notre application photo a une interface utilisateur très simple – fortement inspirée par l'interface utilisateur de la caméra Samsung. Certains composants/fonctionnalités notables de la caméra sont :

* Aperçu de la caméra
* Options de mode de la caméra
* Galerie photo

Pour les besoins de ce tutoriel, seules quelques actions sur le navigateur sont activées – le mode caméra « photo », le bouton de l'obturateur de la caméra et le bouton de la galerie photo juste à droite du bouton de l'obturateur.

## Étape 1 : HTML simple pour notre application photo

Pour commencer, nous allons poser les bases de notre application photo avec un simple balisage. Comprendre la structure de notre application photo est crucial car elle comprend quatre sections principales, chacune jouant un rôle vital dans sa fonctionnalité globale :

1. Section `<video>`
2. Section du bouton de capture `<button>`
3. Section `<canvas>`
4. Section de l'image de capture `<img>`

### 1. Section `<video>`

Notre application photo doit inclure une balise `<video>` pour diffuser les médias visuels de notre webcam vers l'affichage de notre navigateur. Donnons-lui un `id` de `camera-stream`.

```html
<video id="camera-stream" autoplay loop muted>
  <source src="" >
</video>

```

### 2. Section du bouton de capture `<button>`

Nous aurons également besoin d'un bouton pour déclencher la capture des médias visuels lorsqu'il est cliqué. Cela agira comme le bouton de l'obturateur. Donnons-lui un `id` de `shutter`.

```html
<div class="shutter-ctn">
  ...
  <button id="shutter" class="shutter">
  </button>
  ...
</div>

```

### 3. Section `<canvas>`

Une balise canvas nous aide à capturer les données d'image du flux vidéo, tout en étant capable d'exporter les données sous forme d'image qui peut être sauvegardée. L'élément `<canvas>` n'a pas besoin d'être visible pour l'utilisateur, mais il doit être accessible par le DOM. Donnons-lui un `id` de `canvas`.

```html
<canvas id="canvas"> </canvas>

```

### 4. Section de l'image de capture `<img>`

Pour la dernière section HTML, nous avons besoin d'une vue pour voir toutes les images qui ont été capturées. Identifions cela avec un id de `gallery-view`.

```html
<div id="gallery-view">
  <button id="prev">
    PREV
  </button>
  <img data-index="0" src="" alt="current viewed image">
  <button id="next">
    NEXT
  </button>
  ...
</div>

```

## Étape 2 : De beaux styles CSS pour faire ressortir notre application

Ajouter des styles au HTML de notre application photo améliore grandement sa convivialité. N'hésitez pas à être créatif en ajoutant ces styles, et n'hésitez pas à sauter cette section pour passer à l'Étape 3 si vous préférez ajouter vos propres styles.

Tout d'abord, ajoutons quelques styles globaux pour nous assurer que chaque composant s'adapte parfaitement lorsqu'ils sont superposés.

```css
body {
  margin: 0;
  max-height: 100vh;
  overflow: hidden;
}
canvas {
  display: none;
}
button {
  border: 0;
  outline: none;
  background: #00000070;
  color: #FFFFFF;
  padding: 4px 8px;
  height: 30px;
  min-width: 30px;
  border-radius: 24px;
  display: grid;
  place-items: center;
  cursor: pointer;
}

```

Ensuite, nous appliquerons un style à l'élément `<video>`, qui affiche un aperçu du cliché à capturer.

```css
.camera-ctn {
  position: relative;
  background: #000000;
}
.camera-view video {
  height: 100vh;
  width: 100vw;
  object-fit: cover;
  transform: scaleX(-1);
}

```

Enfin, la tâche de style qui nous reste consiste à personnaliser la section inférieure de notre interface de caméra – la section qui abrite généralement le bouton de l'obturateur.

```css
/* CAMERA BOTTOM */
.camera-bottom {
  height: 250px;
  background: #00000050;
  position: absolute;
  inset: 0;
  top: auto;
  padding: 0 5%;
  display: grid;
  place-items: center;
}
.camera-bottom > .inner {
  display: grid;
  place-items: center;
  max-width: 500px;
}

/* SHUTTER CONTAINER */
.shutter-ctn {
  display: flex;
  align-items: center;
  justify-content: space-around;
  width: 100%;
}
.shutter {
  height: 80px;
  width: 80px;
  background: #FFFFFF;
  border-radius: 50%;
}
.shutter:active {
  transform: scale(0.8);
}
.switch-device {
  height: 55px;
  width: 55px;
  border-radius: 50%;
}

```

Pour avoir une vue complète des styles CSS utilisés à l'origine sur ce projet, consultez-les [ici](https://github.com/felixfavour/camera-demo/blob/master/assets/styles/main.css).

## Étape 3 : Code JavaScript pour rendre notre application entièrement fonctionnelle

Enfin, après avoir posé une base solide avec notre structure HTML et amélioré l'utilisabilité de notre application photo avec quelques styles CSS, notre attention se porte maintenant sur le fait que notre application photo fasse ce qu'elle est censée faire – prendre des photos.

Nous faisons cela en nous appuyant fortement sur l'API MediaStream en JavaScript tout en suivant ces trois étapes :

1. Lier nos éléments HTML à JS.
2. Connecter la webcam au code JS.
3. Capturer et sauvegarder les médias de la webcam.

### 1. Lier les éléments HTML à JS

Alors que nous procédons à l'ajout de fonctionnalités à notre HTML, nous devons lier ces éléments à notre code JavaScript via le DOM. Rappelez-vous que nous avons attribué des ID aux éléments principaux que nous avons définis dans l'étape HTML.

```jsx
const cameraVideoStream = document.getElementById('camera-stream')
const shutterButton = document.getElementById('shutter')
const canvas = document.getElementById('canvas')
...

```

### 2. Connecter la webcam au code JavaScript

Après avoir lié nos éléments HTML à notre code JS, nous pouvons maintenant établir la connexion à notre webcam. Cela implique initialement de vérifier si le navigateur de l'utilisateur prend en charge cette opération en utilisant l'expression booléenne `navigator.mediaDevices`.

Si l'expression retourne une valeur vraie, nous pouvons invoquer `getUserMedia()` et spécifier l'option vidéo en passant `{video: true}` comme argument de fonction comme ci-dessous :

```jsx
if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia({ video: true })) {
  navigator.mediaDevices
	.getUserMedia({ video: true })
	.then ((stream) => {
            cameraVideoStream.srcObject = stream
            cameraVideoStream.play()
	})
} 

```

La fonction `getUserMedia()` invoque une opération asynchrone, ce qui signifie qu'elle ne retourne pas de réponse immédiatement. De plus, elle peut rencontrer des échecs – cela pourrait se produire si l'utilisateur refuse la permission de nous accéder à leur webcam ou si leur appareil manque d'une webcam. 

Si l'opération est réussie, le flux vidéo est collecté et transféré à l'élément `video` qui a été créé précédemment.

Mais la vidéo ne commence pas à jouer immédiatement. Un bref délai se produit pour permettre un tampon – ce délai est souvent imperceptible. Nous devons créer une variable `streaming` en conjonction avec l'événement `canplay` de l'élément `<video>` pour savoir quand une partie de la vidéo est tamponnée et prête à être lue. Nous pouvons faire cela comme ci-dessous :

```jsx
let width = window.innerWidth
let height = 0
let streaming = false

cameraVideoStream.addEventListener(
  "canplay",
  (ev) => {
    if (!streaming) {
      height = cameraVideoStream.videoHeight / (cameraVideoStream.videoWidth / width);

      canvas.setAttribute("width", width);
      canvas.setAttribute("height", height);
      cameraVideoStream.setAttribute("width", width);
      cameraVideoStream.setAttribute("height", height);
      streaming = true;
    }
  },
  false
);

```

Remarquez que avant que `streaming` soit défini sur vrai, la hauteur de l'élément `<video>` et du `<canvas>` sont définies pour correspondre à la valeur `height` (qui peut être une fraction de la `width` en fonction des dimensions souhaitées). Cet ajustement aide à prévenir tout bug, en particulier lors de la capture de l'image.

### 3. Capturer et sauvegarder les médias de la webcam

Maintenant, le travail le plus difficile est terminé. Il ne reste plus qu'à capturer des instantanés du flux vidéo et à les stocker dans un tableau sous forme d'images.

Pour accomplir cela, nous utilisons le contexte de l'élément `<canvas>` défini précédemment, accessible via `canvas.getContext('2d')`. Ensuite, nous transférons le cadre actuel des données du flux vidéo pour composer une image en utilisant la fonction `canvasContext.drawImage()` comme ci-dessous.

```jsx
// Capture snapshots using HTML Canvas
function captureImage () {
  const canvasContext = canvas.getContext('2d')
  canvas.width = width
  canvas.height = height
  canvasContext.drawImage(cameraVideoStream, 0, 0, width, height)

  // Convert captured data to image (base64)
  const data = canvas.toDataURL('image/png')
  currentImageElement.src = data
}

// Add click listener to shutter button to capture image
shutterButton.addEventListener('click', () => captureImage())

```

Avec les données maintenant capturées sous forme d'image, l'étape absolument finale est de convertir l'image en un format transférable adapté à la balise `<img>` ou à toute autre ressource de visualisation d'image. L'un des nombreux formats transférables est base64, et heureusement, l'élément `<canvas>` nous permet d'atteindre cet objectif sans effort avec `canvas.toDataURL('image/png')`.

Et voilà ! Vous avez réussi à construire votre propre application photo. Bien joué, génie !

Dès que nous avons terminé la mise en œuvre de ces trois étapes, il ne reste plus qu'à dire « cheese » et à prendre quelques belles photos.

Si vous avez mélangé quelques instructions, n'hésitez pas à consulter le code JS complet [ici](https://github.com/felixfavour/camera-demo). Si cela ne vous aide pas beaucoup, je suis toujours heureux de vous aider personnellement lorsque vous [envoyez un message](https://favourfelix.com).

## Le plaisir ne s'arrête pas ici

Vous voulez vous amuser à construire plus de fonctionnalités pour l'application photo ? Vous pouvez reprendre là où je me suis arrêté sur GitHub. Que ce soit votre propre galerie, ou un outil d'édition photo rapide dans la vue de la galerie, ou une fonction de minuterie, ou même si vous souhaitez étendre cela à un enregistreur vidéo – allez-y !

%[https://github.com/felixfavour/camera-demo]

Si vous avez trouvé cet article utile, n'hésitez pas à vous connecter sur [favourfelix.com](http://favourfelix.com/) pour voir ce que je fais d'autre.