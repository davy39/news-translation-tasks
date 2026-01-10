---
title: Comment sauvegarder les animations canvas avec CCapture
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-22T17:09:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-save-canvas-animations-with-ccapture-78c70f0e86ac
coverImage: https://cdn-media-1.freecodecamp.org/images/1*UDBFB687oY280RLMbOwbSw.jpeg
tags:
- name: Art
  slug: art
- name: generative art
  slug: generative-art
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Comment sauvegarder les animations canvas avec CCapture
seo_desc: 'By Ibby EL-Serafy

  You’ve been learning p5.js and you’ve created a wonderful animation and now you
  want to share it with the world. How do you go about that?

  We could use screen capture software, but this only works if the animation is running
  at the ...'
---

Par Ibby EL-Serafy

Vous apprenez p5.js et vous avez créé une animation magnifique que vous souhaitez maintenant partager avec le monde. Comment procéder ?

Nous pourrions utiliser un logiciel de capture d'écran, mais cela ne fonctionne que si l'animation s'exécute à la bonne vitesse. Avec l'animation ci-dessus, je n'obtenais même pas la moitié d'une image par seconde. La bibliothèque [ccapture.js](https://github.com/spite/ccapture.js) est mentionnée dans la documentation de p5.js et a bien fonctionné pour moi.

Si vous souhaitez suivre ce tutoriel, vous pouvez fork le sandbox ci-dessous, qui contient tout le code dont vous aurez besoin pour commencer.

Voir mon codesandbox [ici](https://codesandbox.io/s/wy11r18xz8?fontsize=14).

La première chose à faire est de télécharger le [fichier JavaScript minifié CCapture](https://github.com/spite/ccapture.js/blob/master/build/CCapture.all.min.js). Nous allons déplacer le fichier dans notre dossier de projet, ou le téléverser dans notre dossier sandbox. Ensuite, nous devons l'ajouter à notre fichier index.html :

```
<script src="p5.min.js"></script><script src="CCapture.all.min.js"></script><script src="sketch.js"></script>
```

Dans le fichier sketch.js, nous devons initialiser l'objet capturer. Nous devons également spécifier le framerate que nous souhaitons pour notre animation. Nous pouvons faire cela en haut de notre fichier :

```
let framerate = 30;var capturer = new CCapture( {  format: 'webm',  framerate,  name: 'noise_visualization',  quality: 100,} );
```

Notez que nous n'avons pas besoin de définir le framerate en utilisant la fonction `frameRate()` de p5.js.

En plus de `webm`, vous pouvez choisir `jpeg` ou `png` pour le format, tous deux génèrent un fichier tar avec chaque image comme frame. Selon la documentation, le format `gif` peut ne pas performé aussi bien. Gardez cela à l'esprit si vous prévoyez de l'utiliser.

L'utilisation du format WebM signifie que nous pourrons visualiser l'animation dès qu'elle sera prête. Cela semble beaucoup plus amusant que de devoir convertir les images en vidéo d'abord, donc nous allons opter pour cela.

Ensuite, nous devons démarrer le capturer, nous allons faire cela à la fin de la fonction setup. Vous pourriez également le démarrer à tout moment dans l'animation, ou en réponse à une pression de touche ou un clic de souris.

```
function setup() {  // Code de configuration  // ...  capturer.start();}
```

Maintenant, nous devons capturer les frames, mais pour cela, vous devez passer le `canvas` à la fonction `capture` d'abord. Nous pouvons apporter une petite modification à la fonction `setup` afin de pouvoir sauvegarder le canvas dans une variable :

```
// Initialiser le canvas en dehors de la fonction setup pour qu'il puisse être utilisé dans la fonction drawlet xseed, yseed, incrementxnoise,incrementynoise, canvas;
```

```
function setup() {  let p5canvas = createCanvas(200, 200);  canvas = p5canvas.canvas;  // Reste du code de configuration}
```

Et maintenant, à la fin de la fonction draw, nous capturons le canvas.

```
function draw() {  // Code pour dessiner le frame  capturer.capture(canvas);}
```

Maintenant, tout ce que nous devons faire est de décider quand arrêter la capture et ensuite sauvegarder l'animation. Nous pourrions le faire en fonction du temps écoulé, en utilisant la fonction `millis()` dans p5.js. Mais il est probable que nous voulons que notre animation ait une durée spécifique, et si les frames se rendent lentement, le temps écoulé ne reflétera pas cela. Au lieu de cela, nous pouvons calculer combien de secondes se sont écoulées en utilisant le `frameCount` actuel :

```
let secondsElapsed = frameCount/framerate;
```

Maintenant, si nous voulons que l'animation s'arrête à, disons, 5 secondes, nous pourrions faire comme ceci :

```
let secondsElapsed = frameCount/framerate;if (secondsElapsed >= 5) {  capturer.stop();  capturer.save();  noLoop(); // Ceci est optionnel}
```

Et c'est tout ! Voici à quoi cela ressemble dans un sandbox :

Voir mon codesandbox [ici.](https://codesandbox.io/s/oqm8yp8ow6?codemirror=1&fontsize=14&module=%2Fsketch.js)

Notez que j'ai commenté le code pour le téléchargement afin de pouvoir l'intégrer sur Medium.

#### Utiliser ffmpeg pour convertir

Maintenant que vous avez votre animation, ce qui est génial, mais vous pourriez en avoir besoin dans différents formats. Il existe de nombreux programmes et convertisseurs en ligne que vous pourriez utiliser. J'ai utilisé [ffmpeg](https://www.ffmpeg.org/download.html) car il est flexible et disponible depuis la ligne de commande. Selon leurs propres mots :

> FFmpeg est le framework multimédia de référence, capable de **décoder**, **encoder**, **transcoder**, **multiplexer**, **démultiplexer**, **streamer**, **filtrer** et **lecture** de presque tout ce que les humains et les machines ont créé. Il supporte les formats anciens les plus obscurs jusqu'aux plus récents.

Pour convertir l'animation en gif, vous pouvez utiliser quelque chose comme ceci.

```
ffmpeg -i noise_visualization.webm -filter_complex "[0:v] fps=15, split [a][b];[a] palettegen [p];[b][p] paletteuse" noise_visualization.gif
```

GIPHY a un [excellent article](https://engineering.giphy.com/how-to-make-gifs-with-ffmpeg/) qui explique ce que font toutes ces options.

Et pour convertir en mp4 pour Instagram, vous pouvez utiliser quelque chose comme ceci :

```
ffmpeg -i noise_visualization.webm -c:a copy -c:v libx264 -b:v 5M -maxrate 5M noise_visualization.mp4
```

Si vous réutilisez souvent les mêmes options ffmpeg, il peut être utile de les sauvegarder dans un alias. Vous devrez découvrir les spécificités de la façon de le faire pour votre propre programme de terminal. Dans cmder, c'est sous Paramètres>Environnement :

![Image](https://cdn-media-1.freecodecamp.org/images/1*pNBIDzV04RnAQKZRGb46lw.png)
_La fenêtre des paramètres de cmder_

Dans cmder, l'alias est défini avec une commande comme celle-ci :

```
alias ffinsta=ffmpeg -i $1 -c:a copy -c:v libx264 -b:v 5M -maxrate 5M $2
```

Ici, `$1` est le premier argument donné à `ffinsta` et `$2` est le deuxième argument. Une fois l'alias défini, vous pouvez l'utiliser comme ceci :

```
ffinsta noise_visualization.webm noise_visualization.mp4
```

Notez que, dans cmder, vous devez redémarrer le terminal après avoir défini l'alias. Cela peut également être le cas pour votre programme de terminal.

J'espère que vous avez trouvé ce tutoriel utile, n'hésitez pas à demander si vous avez besoin d'aide.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UDBFB687oY280RLMbOwbSw.jpeg)
_Photo par [Unsplash](https://unsplash.com/photos/cn0-hgcpoL8?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Markus Spiske</a> sur <a href="https://unsplash.com/search/photos/canvas?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_