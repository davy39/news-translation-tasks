---
title: Comment afficher une image sur une toile HTML5
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-17T07:00:17.000Z'
originalURL: https://freecodecamp.org/news/how-displaying-an-image-on-html5-canvas-works-13e3f6a6c4bd
coverImage: https://cdn-media-1.freecodecamp.org/images/0*WxOWovr439eTe1pc.png
tags:
- name: animation
  slug: animation
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment afficher une image sur une toile HTML5
seo_desc: 'By Nash Vail

  Ok, so here’s a question: “Why do we need an article for this, Nash?”

  Well, grab a seat.

  No wait! First, have a look at this.


  Exactly. What was that?

  drawImage is the method used to display or “draw” an image on canvas. You might
  or mig...'
---

Par Nash Vail

D'accord, voici une question : « Pourquoi avons-nous besoin d'un article pour cela, Nash ? »

Eh bien, prenez place.

Non, attendez ! D'abord, jetez un coup d'œil à ceci.

![Image](https://cdn-media-1.freecodecamp.org/images/0*OVqW6w2oOOpH-V0s.png)

Exactement. Qu'était-ce que c'était ?

`drawImage` est la méthode utilisée pour afficher ou « dessiner » une image sur `canvas`. Vous savez peut-être déjà que ce n'est pas aussi simple que de passer l'URI de l'image. `drawImage` accepte un maximum de 9 paramètres. Ils ressemblent à ceci, prêt ? Retenez votre souffle...

```
(image, sx, sy, sWidth, sHeight, dx, dy, dWidth, dHeight)
```

Respirez, expirez.

J'ai trouvé la [documentation](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/drawImage) pour `drawImage` un peu confuse et complexe. Juste la documentation, oui. Le concept et le fonctionnement de l'API sont excellents pour tous les besoins qu'il est censé servir.

Nous allons passer en revue les paramètres mentionnés ci-dessus un par un, de manière à ce que cela ait du sens pour vous. Si à un moment donné dans l'article vous vous dites « Je voulais juste dessiner une image sur ma toile, cher Nash. Pourquoi mettre mon esprit à l'épreuve ? », ce sera une frustration compréhensible.

La manière dont `drawImage` fonctionne semble complexe dans une certaine mesure, mais cette complexité rend `drawImage` immensément puissant et utile – comme nous le verrons à travers des exemples à la fin. De plus, la complexité n'est qu'en surface : une fois que vous comprenez le tableau d'ensemble, c'est une descente à vélo sur une route de campagne quelque part en Europe.

À la fin de cet article, vous serez capable de visualiser comment `drawImage` dessine n'importe quelle image donnée sur `canvas` simplement en regardant les valeurs des 9 paramètres. Cela ressemble à un superpouvoir que vous pourriez vouloir avoir ? Très bien, plongeons directement !

#### Charger une image dans la toile

Commençons simplement avec une image et une toile HTML5 `canvas`.

Voici à quoi ressemble notre répertoire

![Image](https://cdn-media-1.freecodecamp.org/images/0*ExocbL83jBzDV3Cg.png)
_Structure du répertoire_

À l'intérieur de notre fichier `index.html`, nous avons créé un nouvel élément canvas comme ceci.

```
<canvas id="my-canvas" width="400px" height="200px"/>
```

Notre objectif est de prendre l'image `cat.jpg` et de la placer sur la toile (`#my-canvas`). Et comme je l'ai déjà dit, ce n'est pas si facile, ma belle ! Sinon, je n'écrirais pas cet article, tu me comprends ? Bien.

Pour commencer, ciblons l'élément `canvas` en utilisant JavaScript et obtenons son contexte.

```
const myCanvas = document.getElementById('my-canvas'); const myContext = myCanvas.getContext('2d');
```

Nous avons besoin de `myContext` pour interagir avec l'élément `canvas`. C'est comme si `canvas` était une feuille de papier blanche, le contexte du canvas est le stylo. Intuitivement, vous direz à votre stylo de dessiner quelque chose sur une feuille de papier blanche, et non pas de crier à la feuille de dessiner quelque chose sur elle-même, n'est-ce pas ?

![Image](https://cdn-media-1.freecodecamp.org/images/0*M3Hb4juoST2t7dTM.png)
_...ou peut-être que si ?_

Il y a un certain nombre de choses que vous pouvez faire avec `context`. Vous pouvez dessiner un rectangle, ou une ellipse ou une ligne, ou une... **image**. De plus, remarquez que le contexte `myContext` est implicitement lié à `myCanvas`. Vous pouvez avoir plusieurs `canvas` et appeler `getContext()` sur chacun d'eux pour obtenir un nouveau contexte/stylo pour chacun. Dans notre cas, nous traitons avec un seul canvas (`myCanvas`) et un seul contexte (`myContext`).

Très bien, cela étant dit, nous pouvons enfin commencer à nous mouiller les pieds avec `drawImage`.

![Image](https://cdn-media-1.freecodecamp.org/images/0*9gc-miHUtGQVtTfT.png)
_Cela fait du bien !_

Pour un rappel, voici les 9 paramètres que `drawImage` accepte.

```
(image, sx, sy, sWidth, sHeight, dx, dy, dWidth, dHeight)
```

Nous allons commencer avec le premier paramètre, `image`. Écrivons d'abord quelque chose qui ne fonctionne pas.

```
context.drawImage('./cat.jpg', 0, 0);
```

Vous voyez les deux zéros à la fin ? Bien. Ce n'est pas la partie de l'article où vous êtes censé comprendre pourquoi ils sont là. Ignorez-les pour l'instant, gardez simplement à l'esprit que Nash a écrit 2 zéros et ne les a pas expliqués. Je n'en aurai pas le cœur blessé.

Maintenant, remarquez `...('./cat.jpg',..` dans la ligne de code ci-dessus. Cela semble être un URI parfaitement correct, n'est-ce pas ? Et c'est le cas... mais, si vous lancez `index.html` dans un navigateur, vous verrez un long message d'erreur identique à ce qui est montré ci-dessous.

```
ERROR: The provided value is not of type '(CSSImageValue or HTMLImageElement or SVGImageElement or HTMLVideoElement or HTMLCanvasElement or ImageBitmap or OffscreenCanvas)
```

*gulp*

L'erreur nous dit qu'elle a besoin d'un élément image et non pas seulement d'un URI vers l'image. Pour contourner cela, voici ce que nous pouvons faire.

```
const canvas = document.getElementById('canvas'); const context = canvas.getContext('2d'); const img = new Image();        img.src = './cat.jpg';        img.onload = () => {          context.drawImage(img, 0, 0);        };
```

C'est quelque chose que vous n'aviez pas prévu, n'est-ce pas ? Canvas a besoin d'une image préchargée pour la dessiner/afficher. Pas besoin de montrer de mépris envers canvas, d'ailleurs. Il a ses raisons, c'est comme le reste d'entre nous. Nous verrons éventuellement quelles sont ces raisons et peut-être alors pourrez-vous compatir.

![Image](https://cdn-media-1.freecodecamp.org/images/0*WxOWovr439eTe1pc.png)
_Je ❤️ canvas_

Pour résumer :

`drawImage` demande 9 paramètres, le premier étant `image`. Nous avons vu et compris que `canvas` nécessite une image préchargée pour dessiner et non pas seulement un URI vers l'image. Pourquoi en a-t-il besoin ? Cela deviendra clair au fur et à mesure de votre lecture.

Maintenant, il est temps de passer aux 8 paramètres restants. Relevez vos cols ! Je vais vous apprendre d'abord un peu d'édition graphique !

#### Comment recadrer une image

Chaque programme d'édition graphique, même le plus basique, dispose de la fonction de recadrage. C'est assez simple : ouvrir une image > sélectionner la zone que vous voulez visible > cliquer sur recadrer. Et juste comme ça, le ventre de bière nu de ce vieux bonhomme malodorant est parti. Pouf !

![Image](https://cdn-media-1.freecodecamp.org/images/0*4AteL0TmrOPZBw6d.gif)
_Crédits image : [https://cheezburger.com/4406785536/classic-valentines-day-lover](https://cheezburger.com/4406785536/classic-valentines-day-lover" rel="noopener" target="_blank" title=")_

Technologie ! Sauvant les Instagrams des gens depuis qu'Instagram existe.

Faisons un pas en arrière, et arrêtons-nous riiight, ici.

![Image](https://cdn-media-1.freecodecamp.org/images/0*s2lnF673Ep_UMazx.png)

Marquons quelques points dessus.

![Image](https://cdn-media-1.freecodecamp.org/images/0*OF08OoHREGNMr55v.png)

« Attendez une seconde ! `sx`, `sy`, `sWidth` et `sHeight` ? Je les ai déjà vus ! »

Oui, il y a environ une minute ! Ce qui nous amène à la partie la plus substantielle de l'article.

#### Afficher une image sur la toile, Étape 1 : Sélection

La première tâche que `drawImage` effectue (en coulisses) est de sélectionner une portion de l'image basée sur les quatre paramètres `s` (`sx, sy, sWidth, sHeight`). Vous pouvez dire que le s dans tous les paramètres s signifie « sélection ».

Voici comment cela fonctionne. `sx` et `sy` marquent le point sur l'image à partir duquel la sélection doit commencer, ou en d'autres termes les coordonnées du coin supérieur gauche du rectangle de sélection. `sWidth` et `sHeight` sont alors la largeur et la hauteur du rectangle de sélection respectivement. Vous pouvez remonter jusqu'à la dernière image pour avoir une idée plus claire de ce que j'essaie d'expliquer.

« Mais pourquoi la sélection Nash ? Ne peut-il pas simplement afficher l'image entière ? » Nous nous rapprochons de toutes vos réponses, patience.

Sachez simplement que la première étape que `drawImage` effectue après avoir reçu une image correcte est de sélectionner une portion/zone de l'image basée sur les paramètres s (`sx, sy, sWidth, sHeight`) que vous fournissez.

![Image](https://cdn-media-1.freecodecamp.org/images/0*T6la8c1F6E8Y7P1s.png)

N'oubliez pas que vous n'avez pas toujours à sélectionner une petite portion de l'image, vous pouvez sélectionner l'image entière si vous le souhaitez. Dans ce cas, `sx` et `sy` auront les valeurs 0 et 0 respectivement et `sWidth`, `sHeight` seront les mêmes que la largeur et la hauteur de l'image.

De plus, les valeurs négatives sont acceptées pour `sx` et `sy`. Les valeurs de `sx` et `sy` sont relatives à l'origine de l'image en haut à gauche.

![Image](https://cdn-media-1.freecodecamp.org/images/0*OylxuAxyVxqKRwmb.png)
_1. Sélectionner une portion d'une image 2. Valeurs négatives pour sx et sy 3. Sélectionner l'image entière_

Une fois que `drawImage` a sélectionné la zone de l'image que vous lui avez demandée – et nous verrons bientôt pourquoi la sélection d'une zone de l'image aide – l'étape suivante consiste à dessiner la portion sélectionnée de l'image sur la toile.

« À l'origine » `s` et `d` dans la documentation officielle signifient « source » et « destination ». Mais, entre nous, appelons cela « sélection » et « dessin ». Cela a beaucoup plus de sens de cette façon, n'est-ce pas ?

Encore une fois. La `s`élection est faite, l'étape suivante est de `d`essiner.

#### Afficher une image sur la toile, Étape 2 : Dessin

Pour dessiner la portion sélectionnée de l'image, nous avons à nouveau besoin de quatre paramètres.

1. Coordonnée x de l'endroit où commencer à dessiner sur la toile. (`dx`)
2. Coordonnée y de l'endroit où commencer à dessiner sur la toile. (`dy`)
3. Largeur à laquelle dessiner l'image. (`dWidth`)
4. Hauteur à laquelle dessiner l'image. (`dHeight`)

Les valeurs de `dx` et `dy` seront relatives à l'origine de la toile.

![Image](https://cdn-media-1.freecodecamp.org/images/0*CdcVzs6AIhf10Gwo.png)
_La toile_

Il y a un détail très important mais subtil à remarquer ici. `dWidth` et `dHeight` ne sont en aucun cas liés à `sWidth` et `sHeight`. Ce sont des valeurs indépendantes. Pourquoi devez-vous savoir cela ? Eh bien, parce que si vous ne choisissez pas soigneusement les valeurs de la largeur et de la hauteur du « dessin », vous obtiendrez une image étirée ou écrasée, comme ceci.

![Image](https://cdn-media-1.freecodecamp.org/images/0*Z8oNJxwthTkbMYl2.png)

Donc si ce n'est pas ce que vous recherchez (ce que j'espère), assurez-vous de maintenir le rapport d'aspect. Ou en d'autres termes, `sWidth` divisé par `sHeight` doit être égal à `dWidth` divisé par `dHeight`. C'était une petite mise en garde, vous êtes le maître de votre propre monde et libre de choisir les valeurs que vous aimez.

L'ensemble du processus d'affichage/dessin d'une image sur la toile peut donc être résumé en seulement deux étapes : Sélection et Dessin.

![Image](https://cdn-media-1.freecodecamp.org/images/0*N927nV31BlEaQ4Ok.png)

Génial ! Pas si compliqué après tout, n'est-ce pas ?

À ce stade, nous avons terminé avec toute la théorie. Dans le reste de l'article qui suit, nous allons cuire la pâte de connaissances répandue dans votre tête avec un exemple pratique et amusant et vous serez prêt à partir. Mais, avant de faire cela, parlons d'une dernière chose importante concernant `drawImage`.

#### Les valeurs par défaut

Vous vous souvenez de mon discours sur « hé, gardez le rapport d'aspect et soyez prudent, ne prenez pas de chocolats d'inconnus... » ? Eh bien, il s'avère que vous pouvez omettre certaines valeurs et ne pas vous soucier du rapport d'aspect du tout. En ce qui concerne la prise de chocolats d'inconnus, encore une fois — vous êtes le maître de votre propre monde.

Voici une façon d'utiliser la méthode.

```
drawImage(image, dx, dy)
```

C'est tout ! Dans ce cas, vous dites à `drawImage` seulement l'emplacement sur la toile où commencer le dessin. Le reste, `sx`, `sy`, `sWidth`, `sHeight`, `dWidth` et `dHeight` sont pris en charge automatiquement. La méthode sélectionne l'image entière (`sx = 0, sy = 0, sWidth = largeur de l'image, sHeight = hauteur de l'image`) et commence à dessiner sur la toile à (`dx`, `dy`) avec `dWidth` et `dHeight` identiques à `sWidth` (largeur de l'image), `sHeight` (hauteur de l'image).

Vous vous souvenez des deux zéros que je n'ai pas expliqués ? C'est de là que venaient les deux zéros.

Une autre façon d'utiliser la méthode est,

```
drawImage(image, dx, dy, dWidth, dHeight)
```

Dans cette forme, `sx, sy, sWidth et sHeight` sont pris en charge, et la méthode sélectionne automatiquement l'image entière et vous laisse choisir où et quelle taille d'image dessiner.

Plutôt cool ! n'est-ce pas ?

Si je peux avoir votre attention pendant encore deux minutes, j'aimerais vous expliquer pourquoi la `s`élection et le `d`essin sont deux opérations distinctes. Et comment cela est utile.

Avez-vous votre attention ? Super !

Alors voici.

Vous avez déjà entendu parler des sprites ? Vous voyez, les sprites sont un concept d'infographie où un graphique peut être déplacé à l'écran et autrement manipulé comme une seule entité.

... ?

J'ai copié cette définition de Google pour avoir l'air suave.

D'accord, d'accord. Vous vous souvenez de Mario ?

Bien.

Faisons quelque chose d'amusant.

#### Animer Mario avec drawImage

Vous voyez, lorsque Mario avance/recule ou dans n'importe quelle autre direction, il semble marcher. Sa position change mais il y a aussi une animation accompagnant le mouvement de ses jambes et de ses mains.

Comment font-ils cela ? Montrent-ils différentes images de Mario en succession, comme un flipbook, et il semble qu'il bouge ?

Eh bien, 50 % oui. Imaginez à quel point il serait intensif en ressources de stocker et de charger un grand ensemble d'images décrivant chaque image de l'animation dans notre programme (ou jeu). Au lieu de cela, il y a une seule image et toutes les positions sont disposées en **grille**. Comme celle montrée ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/0*9ni-k8nDrsyPCgiQ.png)
_Sprite de Mario (Source : [https://redballbomb.deviantart.com/art/Mario-and-Luigi-Run-Overworld-Sprite-Sheet-723563974](https://redballbomb.deviantart.com/art/Mario-and-Luigi-Run-Overworld-Sprite-Sheet-723563974" rel="noopener" target="_blank" title="))_

Pour exécuter une animation, au lieu de charger une nouvelle image chaque milliseconde, une portion de la même image est montrée à travers un viewport à différentes positions. Astucieux, n'est-ce pas ?

Alors oui, c'est un peu comme un flipbook, un flipbook astucieux en fait.

Maintenant, si vous pouviez juste vous étirer un peu et faire craquer vos articulations, j'aimerais que nous recréions l'animation de marche de Mario. Nous utiliserons le sprite montré ci-dessus et tout ce que nous avons appris sur `drawImage` jusqu'à présent.

Prêt ? C'est parti !

Jetons un autre coup d'œil à notre sprite et essayons de comprendre les dimensions de la grille sur laquelle il est disposé.

![Image](https://cdn-media-1.freecodecamp.org/images/0*87zCal6SG1FG-Id5.png)

Tout ce que nous avons fait ici, c'est imaginer une grille sur le sprite. Remarquez que toute la grille est composée de cellules de dimensions égales (`32 x 39`). Mais ce n'est toujours qu'une seule image, souvenez-vous de cela.

Génial ! Maintenant, passons à l'écriture de code. Nous commencerons de la manière habituelle en créant d'abord un élément `canvas`, en le récupérant ainsi que son contexte en JavaScript, puis en chargeant notre feuille de sprites Mario.

```
// index.js const canvas = document.getElementById('canvas'); const ctx = canvas.getContext('2d'); const img = new Image();       img.src = './mario.png';       img.onload = () => {          ctx.drawImage(img, 0, 0);       }; 
```

```
// style.css canvas {   /*Ajoutez une bordure autour du canvas pour la lisibilité*/   border: 1px solid grey; }
```

Le code ci-dessus donnera le résultat suivant.

![Image](https://cdn-media-1.freecodecamp.org/images/0*WTeIqpN14vUYIW4g.png)

Woah-kay ! Nous avons l'image qui s'affiche ! Que se passe-t-il vraiment ?

Ici, nous utilisons la forme de `drawImage` — `drawImage(image, sx, sy)` — où l'image entière est `s`électionnée et `d`essinée sur la toile telle quelle.

![Image](https://cdn-media-1.freecodecamp.org/images/0*C1hngzicbr9HvzLZ.png)
_Dessiner le sprite entier sur la toile_

Ce que nous voulons faire, tout d'abord, c'est sélectionner une seule cellule de la grille et dessiner cette seule cellule. Commençons par apporter des modifications à notre code qui sélectionne la première cellule de la troisième ligne, celle où Mario est debout, faisant face à l'est. Nous comprendrons comment animer une fois que cela sera fait. Cela vous semble bien ? Parfait !

Apportons les modifications nécessaires à notre code.

```
const canvas = document.getElementById('canvas'); const ctx = canvas.getContext('2d'); 
```

```
// Variables Mario const MARIO_WIDTH = 32; const MARIO_HEIGHT = 39; 
```

```
const mario = new Image(); mario.src = './mario.png'; mario.onload = () => {   ctx.drawImage(     // Image     mario,     // ---- Sélection ----     0, // sx     MARIO_HEIGHT * 2, // sy     MARIO_WIDTH, // sWidth     MARIO_HEIGHT, // sHeight     // ---- Dessin ----     0, // dx     0, // dy    MARIO_WIDTH, // dWidth     MARIO_HEIGHT // dHeight   ); };
```

Tout d'abord, remarquez les deux variables `MARIO_WIDTH` et `MARIO_HEIGHT`. Ce sont les dimensions de la cellule de la grille, c'est tout ce qu'elles sont. Nous les avons définies pour faciliter la traversée de la grille en utilisant simplement des multiples de chacune de ces constantes. Cela a du sens ?

Bien.

Ensuite, dans le bloc `// Sélection`, nous avons défini la zone de l'image que nous voulons sélectionner, dans la section `// Dessin`, nous avons défini la largeur et la hauteur et la position à partir de laquelle commencer à dessiner sur la toile... et juste comme cela, nous avons réussi à dessiner une seule cellule de la grille imaginaire entière.

![Image](https://cdn-media-1.freecodecamp.org/images/0*-_w1d8AizOYZ9hcH.png)
_Dessiner seulement une portion du sprite sur la toile._

Assez simple, juste sélection et dessin. À ce stade, j'aimerais faire une digression sur un sujet plus ancien concernant le rapport d'aspect. « Nash ! encore ? ugghh » Je sais, je sais. Mais c'est cool ! Regardez !

Si je change les valeurs de `dWidth` ou `dHeight` ou les deux, regardez comment l'image s'étire et s'écrase.

```
... ctx.drawImage(   // Image    mario,   // ---- Sélection ----    0, // sx    MARIO_HEIGHT * 2, // sy    MARIO_WIDTH, // sWidth    MARIO_HEIGHT, // sHeight    // ---- Dessin ----    0, // dx    0, // dy    MARIO_WIDTH * 2, // dWidth    MARIO_HEIGHT * 1.5 // dHeight  ); ...
```

![Image](https://cdn-media-1.freecodecamp.org/images/0*V49C2cYN4LiQicN5.png)

Hah ! Vous voyez ! C'est pourquoi je vous conseillais de maintenir le rapport d'aspect et que les valeurs de sélection et de dessin n'ont pas de réelle interconnexion.

D'accord, revenons à ce que nous faisions.

Maintenant que nous avons Mario dans la toile, petit et mignon. Nous devons l'animer, ou en d'autres termes, montrer différentes images au même endroit en succession et créer l'illusion du mouvement. Ai-je été trop spécifique ? Bien sûr que oui !

Nous pouvons faire cela en sélectionnant les cellules de la grille que nous voulons dessiner en succession. Nous devons simplement changer la valeur de `sx` par les multiples de `MARIO_WIDTH`.

Faire cela nécessitera l'utilisation de `requestAnimationFrame` et j'ai expliqué cela dans une série d'articles [ici](https://uxdesign.cc/how-you-can-use-simple-trigonometry-to-create-better-loaders-32a573577eb4) et [là](https://uxdesign.cc/how-to-fix-dragging-animation-in-ui-with-simple-math-4bbc10deccf7).

En tant que petit défi, pourquoi ne pas essayer d'accomplir cela par vous-même ? Dans tous les cas, vous pouvez consulter ce Codepen où j'ai Mario qui court comme ceci. Le pen contient suffisamment de commentaires pour vous aider à comprendre le petit peu de mathématiques de lycée qui est utilisé pour faire fonctionner l'animation.

Petite chose mignonne !

Et avec cela, nous avons terminé avec une explication très complète de `drawImage`. J'espère que vous avez apprécié.

Si vous êtes arrivé jusqu'ici, pourquoi ne pas m'envoyer un feedback ou des #goodvibes sur [Twitter](https://twitter.com/nashvail) ?

> Cet article a été initialement publié sur [www.nashvail.me](http://www.nashvail.me/blog/canvas-image).

Est-ce que je vous ai parlé de mon nouveau [site web](https://nashvail.me) ? Et est-ce que je vous ai dit qu'il avait aussi une [Newsletter](http://eepurl.com/gehwqP) ? J'adorerais que vous vous abonniez pour que je puisse vous notifier chaque fois que je publie quelque chose de nouveau ou que je mets quelque chose de nouveau en vente dans [ma boutique](http://nashvail.me/shop). Je continuerai à publier des articles sur Medium mais il y aura un délai de deux semaines entre le moment où il apparaîtra d'abord sur mon site et le moment où il apparaîtra ici.

Merci beaucoup pour votre lecture et merci beaucoup pour votre soutien. Passez une bonne journée ! 😊