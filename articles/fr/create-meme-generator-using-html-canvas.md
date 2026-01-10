---
title: Comment créer un générateur de mèmes en utilisant HTML Canvas
subtitle: ''
author: Timothy Olanrewaju
co_authors: []
series: null
date: '2024-11-19T13:29:03.653Z'
originalURL: https://freecodecamp.org/news/create-meme-generator-using-html-canvas
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1731783150771/d3ba743f-c945-482e-a25d-9d093c7e866b.jpeg
tags:
- name: Web Development
  slug: web-development
- name: projects
  slug: projects
seo_title: Comment créer un générateur de mèmes en utilisant HTML Canvas
seo_desc: We all come across memes almost every day on the internet. Whether you're
  scrolling through social media or chatting with friends, there's a good chance you'll
  stumble on a meme, or even share one yourself. A meme can be an image, a video,
  or gif tha...
---

Nous tombons tous sur des mèmes presque tous les jours sur Internet. Que vous fassiez défiler les réseaux sociaux ou que vous discutiez avec des amis, il y a de fortes chances que vous tombiez sur un mème, ou même que vous en partagiez un vous-même. Un mème peut être une image, une vidéo ou un gif destiné à être drôle ou à transmettre un message de manière légère.

Les mèmes sont amusants et nous les aimons tous. Que diriez-vous si je vous disais que vous pouvez créer les vôtres à partir de zéro ? C'est exactement ce que je vais vous montrer dans cet article en utilisant HTML Canvas. Pas besoin de logiciels sophistiqués - juste un peu de code et de la créativité pour créer vos propres mèmes personnalisés.

Si cela vous enthousiasme, plongeons directement dans le sujet !

## Ce dont vous aurez besoin

Pour suivre ce tutoriel, vous aurez besoin de :

* Des connaissances de base en HTML, CSS et JavaScript.

* Un éditeur de texte (comme Visual Studio Code ou Sublime Text).

* Un navigateur web moderne.

## Étape une : Configurer votre projet

Créez un dossier et créez ces trois fichiers dans le dossier :

* `Index.html`

* `Style.css`

* `Script.js`

## Étape deux : Structure HTML

Tout d'abord, créons la structure de base du fichier HTML. Notre structure inclura un bouton de téléchargement de fichier pour les images, une entrée de texte pour ajouter des légendes (en haut et en bas), des boutons pour générer et télécharger le mème et un canevas pour afficher l'image et la ou les légendes.

```xml
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Générateur de Mèmes</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1>Générateur de Mèmes</h1>
  <input type="file" id="imageInput" accept="image/*">
  <div class="controls">
    <input type="text" id="topText" placeholder="Entrez le texte du haut">
    <input type="text" id="bottomText" placeholder="Entrez le texte du bas">
    <button id="generate" onclick="generateMeme()">Générer le Mème</button>
    <button id="download" onclick="downloadMeme()">Télécharger le Mème</button>
  </div>
  <canvas id="memeCanvas" width="580" height="450"></canvas>

  <script src="script.js"></script>
</body>
</html>
```

## Étape trois : Stylisation avec CSS

Ensuite, nous appliquons un style aux éléments HTML que nous venons de créer pour les rendre plus attrayants et conviviaux. Ici, nous appliquons simplement un CSS de base pour centrer le contenu et ajouter des couleurs à la fois à l'arrière-plan et aux boutons.

```css
body {
    display: flex;
    flex-direction: column;
    align-items: center;
    font-family: Arial, sans-serif;
    background-color: rgb(121, 121, 170);
    color: white;
}
canvas {
    border: 2px solid #333;
    margin-top: 10px;
}
.controls {
    margin-top: 10px;
}
.controls input, .controls button {
    margin: 5px;
}
#generate{
    background-color: green;
    color: white;
    font-weight: bold;
    padding: 6px;
    border-radius: 3px;
    border: none;
    cursor: pointer;
}
#download{
    background-color: blue;
    color: white;
    font-weight: bold;
    padding: 6px;
    border-radius: 3px;
    border: none;
    cursor: pointer;
}
```

Voici à quoi ressemble notre page web dans le navigateur après avoir appliqué le style :

![page de générateur de mèmes dans le navigateur](https://cdn.hashnode.com/res/hashnode/image/upload/v1731772678380/edd33637-73dd-40b6-8b8d-352d350ac52e.png align="center")

## Étape quatre : Ajouter JavaScript pour gérer la logique

Maintenant, codons les fonctionnalités de notre application en utilisant JavaScript.

### Initialisation

Tout d'abord, nous devons initialiser certains éléments importants qui nous permettront de rendre notre image sur le canevas.

```javascript
const canvas = document.getElementById('memeCanvas');
const ctx = canvas.getContext('2d');
const imageInput = document.getElementById('imageInput');
let uploadedImage = null;
```

Dans ce code :

* `canvas` : Fait référence à l'élément HTML `<canvas>` avec l'ID `memeCanvas`. C'est ici que l'image et le texte du mème seront dessinés.

* `ctx` : En utilisant le canevas, il existe des méthodes qui peuvent être appliquées pour dessiner des formes, des images et des textes sur le canevas. Nous avons spécifié un *Type de Contexte* en **2d**, ce qui fait que le canevas est rendu en contexte 2D.

* `imageInput` : Fait référence à un élément `<input>` de type `file` (avec l'ID `imageInput`) qui vous permet de télécharger une image.

* `uploadedImage` : Une variable pour stocker les images téléchargées afin qu'elles puissent être dessinées sur le canevas.

### Comment télécharger des images

Ensuite, nous voulons pouvoir choisir un fichier particulier, le lire et dessiner le fichier image sélectionné sur le canevas.

Notre générateur de mèmes n'acceptera que les fichiers avec un `type` de `image`.

```javascript
imageInput.addEventListener('change', (event) => {
  const file = event.target.files[0];
  const reader = new FileReader();

  reader.onload = (e) => {
    const img = new Image();
    img.src = e.target.result;
    img.onload = () => {
      uploadedImage = img;
      drawImage();
    };
  };

  reader.readAsDataURL(file);
});
```

Dans ce code :

* `imageInput.addEventListener('change')` : Ajoute et écoute un événement `change` sur le champ de saisie de fichier qui se déclenche lorsque l'utilisateur sélectionne un fichier.

* [`event.target`](http://event.target)`.files[0]` : Accède au premier fichier sélectionné par l'utilisateur.

* `FileReader` : Lit les données du fichier et permet d'y accéder sous forme d'URL.

* `reader.onload` : Cette fonction est déclenchée après la lecture du fichier. Elle fait ce qui suit :

  * Crée un nouvel objet `Image`.

  * Définit la propriété `src` de l'image sur l'URL des données du fichier.

  * Attend que l'image soit chargée, puis :

    * Stocke l'image dans la variable `uploadedImage`.

    * Appelle `drawImage()` pour dessiner l'image sur le canevas.

### Comment dessiner l'image et le texte de la légende

Ici, nous allons dessiner l'image, fixer les légendes saisies par l'utilisateur sur le dessus de l'image (superposition), et styliser et positionner les légendes textuelles.

```javascript
function drawImage() {
  if (uploadedImage) {
    // Effacer le canevas et définir les dimensions du canevas pour qu'elles correspondent à l'image
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.drawImage(uploadedImage, 0, 0, canvas.width, canvas.height);

    // Obtenir les valeurs du texte
    const topText = document.getElementById('topText').value;
    const bottomText = document.getElementById('bottomText').value;

    // Définir les styles de texte
    ctx.font = '30px Impact';
    ctx.fillStyle = 'white';
    ctx.strokeStyle = 'black';
    ctx.lineWidth = 2;
    ctx.textAlign = 'center';

    // Dessiner le texte du haut
    ctx.fillText(topText, canvas.width / 2, 50);
    ctx.strokeText(topText, canvas.width / 2, 50);

    // Dessiner le texte du bas
    ctx.fillText(bottomText, canvas.width / 2, canvas.height - 20);
    ctx.strokeText(bottomText, canvas.width / 2, canvas.height - 20);
  }
}
```

Dans ce code :

* `ctx.clearRect(0, 0, canvas.width, canvas.height)` : Efface le canevas pour qu'il puisse être redessiné.

* `ctx.drawImage()` : Dessine l'image téléchargée sur le canevas et l'étire pour qu'elle corresponde aux dimensions définies.

* `topText` et `bottomText` : Capture la saisie de l'utilisateur à partir de deux champs de texte - `<input id="topText">` et `<input id="bottomText">`.

**Style de texte :**

* `ctx.font` : Définit le style de la police.

* `ctx.fillStyle` : Définit la couleur de remplissage pour le texte.

* `ctx.strokeStyle` : Définit la couleur du contour pour le texte.

* `ctx.lineWidth` : Définit l'épaisseur du contour.

* `ctx.textAlign` : Assure que le texte est centré par rapport à la coordonnée X.

* `ctx.fillText()` et `ctx.strokeText()` :

  * Dessine le texte à des positions spécifiées.

  * `canvas.width / 2` assure que le texte est centré horizontalement.

  * `50` et `canvas.height - 20` définissent les positions verticales pour le texte du haut et du bas.

Vous pouvez personnaliser le style du texte selon vos préférences.

### Comment générer le mème

Ensuite, nous allons déclencher la fonction qui génère le mème en dessinant le texte fourni par l'utilisateur sur l'image.

```javascript
function generateMeme() {
  drawImage();
}
```

Le code ci-dessus appelle la fonction `drawImage` pour s'assurer que le canevas est mis à jour avec l'image et le texte saisi par l'utilisateur.

### Comment télécharger le mème

Enfin, nous voulons pouvoir télécharger notre mème en tant qu'image sur notre appareil. Voici comment nous pouvons y parvenir :

```javascript
function downloadMeme() {
  const link = document.createElement('a');
  link.download = 'meme.png';
  link.href = canvas.toDataURL();
  link.click();
}
```

Dans ce code :

* `document.createElement('a')` : Crée un élément `<a>` temporaire.

* [`link.download`](http://link.download) `= 'meme.png'` : Définit le nom du fichier pour le mème téléchargé (chaque mème que vous téléchargez portera le nom de `meme.png` - vous pouvez le changer si vous le souhaitez).

* `link.href = canvas.toDataURL()` : Convertit le contenu du canevas en une URL de données.

* [`link.click`](http://link.click)`()` : Simule un clic sur le lien, déclenchant le téléchargement.

Avec cela, nous avons maintenant un générateur de mèmes entièrement fonctionnel.

### Code JavaScript complet

```javascript
const canvas = document.getElementById('memeCanvas');
const ctx = canvas.getContext('2d');
const imageInput = document.getElementById('imageInput');
let uploadedImage = null;

// Charger l'image sur le canevas
imageInput.addEventListener('change', (event) => {
  const file = event.target.files[0];
  const reader = new FileReader();

  reader.onload = (e) => {
    const img = new Image();
    img.src = e.target.result;
    img.onload = () => {
      uploadedImage = img;
      drawImage();
    };
  };

  reader.readAsDataURL(file);
});

// Dessiner l'image et le texte sur le canevas
function drawImage() {
  if (uploadedImage) {
    // Effacer le canevas et définir les dimensions du canevas pour qu'elles correspondent à l'image
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.drawImage(uploadedImage, 0, 0, canvas.width, canvas.height);

    // Obtenir les valeurs du texte
    const topText = document.getElementById('topText').value;
    const bottomText = document.getElementById('bottomText').value;

    // Définir les styles de texte
    ctx.font = '30px Impact';
    ctx.fillStyle = 'white';
    ctx.strokeStyle = 'black';
    ctx.lineWidth = 2;
    ctx.textAlign = 'center';

    // Dessiner le texte du haut
    ctx.fillText(topText, canvas.width / 2, 50);
    ctx.strokeText(topText, canvas.width / 2, 50);

    // Dessiner le texte du bas
    ctx.fillText(bottomText, canvas.width / 2, canvas.height - 20);
    ctx.strokeText(bottomText, canvas.width / 2, canvas.height - 20);
  }
}

// Générer le mème en dessinant le texte sur l'image téléchargée
function generateMeme() {
  drawImage();
}

// Télécharger le mème en tant qu'image
function downloadMeme() {
  const link = document.createElement('a');
  link.download = 'meme.png';
  link.href = canvas.toDataURL();
  link.click();
}
```

### Étapes pour créer votre mème sur le générateur de mèmes

* Cliquez sur le bouton **Parcourir** et sélectionnez une image particulière.

* Entrez du texte dans l'un des deux types d'entrée - étiquetés Texte du haut et Texte du bas.

* Cliquez sur le bouton **Générer le Mème** pour créer votre mème.

* Cliquez sur **Télécharger le Mème** pour télécharger votre mème généré.

Voici le générateur de mèmes en action complète avec les étapes démontrées :

![Projet de générateur de mèmes fonctionnant dans le navigateur](https://cdn.hashnode.com/res/hashnode/image/upload/v1731787007980/24206a68-6e2e-4883-81f2-1db5169cb093.gif align="center")

### Résultats finaux

Voici deux mèmes créés par notre générateur de mèmes.

![mème 1](https://cdn.hashnode.com/res/hashnode/image/upload/v1731780897736/d136df1d-c3a4-416d-90ca-e6e400d10a0e.png align="center")

![mème 2](https://cdn.hashnode.com/res/hashnode/image/upload/v1731780929605/f67cc533-2bb4-4bdb-ad9f-1231caede069.png align="center")

Plutôt cool, n'est-ce pas ?

Maintenant, vous pouvez l'essayer et créer votre propre mème viral !

Pour plus d'articles et de publications sur la programmation, vous pouvez me suivre sur [X](https://x.com/SmoothTee_DC) ou vous connecter avec moi sur [LinkedIn](https://www.linkedin.com/in/timothy-olanrewaju750/).

À la prochaine !