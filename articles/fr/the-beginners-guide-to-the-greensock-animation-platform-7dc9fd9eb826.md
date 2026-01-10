---
title: Le guide du débutant pour la plateforme d'animation GreenSock
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-20T13:34:33.000Z'
originalURL: https://freecodecamp.org/news/the-beginners-guide-to-the-greensock-animation-platform-7dc9fd9eb826
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XV6VzHM_yxQjNa2lcQuYlA.jpeg
tags:
- name: animation
  slug: animation
- name: coding
  slug: coding
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Le guide du débutant pour la plateforme d'animation GreenSock
seo_desc: 'By Nicholas Kramer

  A primer to creating timeline based animations without knowing JavaScript


  Introduction

  The GreenSock Animation Platform (GSAP for short) is a powerful JavaScript library
  that enables front-end developers and designers to create ro...'
---

Par Nicholas Kramer

#### Une introduction à la création d'animations basées sur une timeline sans connaître JavaScript

![Image](https://cdn-media-1.freecodecamp.org/images/rDrPAgnDjP9VpvSVK8QKpD7o1NhzuAEFP0uL)

### Introduction

La plateforme d'animation GreenSock ([GSAP](https://greensock.com/gsap) en abrégé) est une puissante bibliothèque JavaScript qui permet aux développeurs front-end et aux designers de créer des animations robustes basées sur une timeline. Cela permet un contrôle précis pour des séquences d'animation plus complexes plutôt que les propriétés parfois contraignantes `keyframe` et `animation` que CSS offre.

Le meilleur aspect de cette bibliothèque est qu'elle est légère et facile à utiliser.

Avec GSAP, vous pouvez commencer à créer des animations engageantes avec peu ou pas de connaissances en JavaScript.

Ce guide montrera comment configurer et utiliser la fonctionnalité TweenMax de GSAP et explorera également un peu le plugin DrawSVG de Club GreenSock. Chacun des exemples ci-dessous a un lien CodePen correspondant afin que vous puissiez suivre dans un autre onglet.

### Installation

Avant de coder, nous devons d'abord ajouter la bibliothèque GSAP à notre fichier HTML. Pour ce faire, vous devrez obtenir le lien CDN vers la bibliothèque TweenMax. Vous pouvez trouver des liens vers TweenMax et d'autres CDN GSAP [ici](https://cdnjs.com/libraries/gsap).

**Note** : CDN signifie Content Delivery Network. Cela signifie qu'au lieu d'héberger les fichiers JavaScript sur votre site, une source externe comme [CloudFlare](https://www.cloudflare.com/) peut les héberger pour vous.

Une fois que vous avez le lien CDN, insérez-le dans une balise `<script>` au bas de votre fichier HTML comme suit :

```
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/1.20.3/TweenMax.min.js"></script>
```

C'est tout ce dont vous avez besoin pour commencer ! Si vous utilisez un environnement de développement en ligne comme CodePen, vous pouvez installer GSAP en modifiant les paramètres du Pen.

![Image](https://cdn-media-1.freecodecamp.org/images/UjL1HujbnFWqH3e4YWROTPBT6t105aD80q0a)
_Cliquez sur l'icône d'engrenage à côté de l'éditeur de texte JS et recherchez TweenMax pour l'installer dans CodePen_

### Comprendre les Tweens

Les Tweens sont les fonctions d'animation de base de GSAP. Pour animer un objet HTML, nous devons appeler l'objet, définir les propriétés que nous allons animer, la durée de l'animation, l'easing de l'animation et tout autre paramètre comme le délai de timing.

Par exemple, si nous voulions changer la couleur d'un rectangle rouge en noir tout en le déplaçant vers le bas et vers la droite, le Tween ressemblerait à ceci en JavaScript :

```
TweenLite.to("#rectangle", 2, {  left:100,   top: 75,   backgroundColor:"#000000",   ease: Power4.easeIn});
```

![Image](https://cdn-media-1.freecodecamp.org/images/5I8DYi4CJ3kOUTzHtRvJvYQdztrSdzNL2J3U)
_Ce tween nous donne un rectangle qui se déplace en diagonale et change de couleur._

Décomposons cela :

`**TweenLite**` **indique à notre fichier JavaScript que nous voulons animer en utilisant GSAP**. La méthode `.to` immédiatement après signifie que nous voulons que notre objet s'anime de son état statique d'origine défini par notre HTML et CSS à l'état animé final défini par notre JavaScript.

Vous pouvez utiliser la méthode `.from` à la place pour inverser cela. Nous aborderons cela un peu plus tard dans cet article.

**Ensuite, nous définissons l'objet que nous voulons animer.** Dans notre cas, il s'agit d'un objet HTML avec l'ID rectangle. Cela ressemble à `"#rectangle"` dans notre code. Nous devons nous assurer que notre objet est entouré de guillemets et que nous utilisons le `#` pour indiquer que nous appelons un ID. N'importe quel ID peut aller ici tant qu'il s'agit d'un élément défini dans votre HTML. Notez également que la virgule suivant le guillemet de fin est importante. Sans elle, l'animation ne s'exécutera pas.

**Le** `2,` **après l'ID de l'élément** **définir la durée de l'animation en secondes.** Dans ce cas, nous définissons la durée de l'animation à 2 secondes. Si nous voulions qu'elle dure une demi-seconde, nous changerions la valeur en `0.5,` à la place.

**Les paramètres à l'intérieur des crochets représentent les propriétés que vous souhaitez animer.** Dans cet exemple, nous animons les propriétés CSS `left`, `top` et `background-color`. Remarquez comment chacune de ces différentes propriétés utilise le camelCase pour les appeler au lieu de la notation par traits d'union typique utilisée avec CSS. Vous pouvez ajouter autant de propriétés différentes ici que vous le souhaitez, tant que vous les séparez par des virgules après leur valeur.

**La dernière propriété appelée est l'`ease` de l'animation.** GSAP est livré avec un ensemble d'options d'easing différentes que vous pouvez ajouter à vos animations.

Dans notre animation ci-dessus, nous appelons l'easing `Power4` et le définissons sur `easeIn` pour l'animation. Vous pouvez voir la gamme complète des options d'easing dans la documentation [ici](https://greensock.com/docs/Easing). Si vous n'êtes pas familier avec l'easing, assurez-vous de consulter un [article précédent](https://blog.prototypr.io/css-animations-for-non-developers-part-1-buttons-54572b394fb2) qui explique différentes fonctions d'easing en profondeur.

**Enfin, vous devez fermer la parenthèse et les crochets du Tween pour éviter toute erreur et permettre à l'animation de s'exécuter.** N'oubliez pas d'inclure le point-virgule pour terminer la fonction JavaScript.

Le Tween est la base fondamentale des animations GSAP. Vous pouvez expérimenter avec un exemple de ce Tween dans CodePen [ici](https://codepen.io/Nickramer/pen/wyGXyN).

Les Tweens sont excellents si vous souhaitez faire des animations ponctuelles, mais si vous souhaitez créer des séquences en plusieurs étapes, les timelines sont la meilleure alternative.

### Animations de Timeline

Si vous avez déjà utilisé un logiciel d'animation ou de prototypage comme [After Effects](https://www.adobe.com/products/aftereffects.html) ou [Principle](http://principleformac.com/), vous êtes déjà familier avec les animations de timeline. Les timelines traditionnelles sont généralement une série d'animations qui se produisent les unes après les autres ou simultanément. Les timelines dans GSAP ne sont pas différentes.

![Image](https://cdn-media-1.freecodecamp.org/images/w4sxnYFapKKBxLGH0mpkmqMDantOe4qCI5gN)
_Une visualisation d'une timeline dans After Effects. Les timelines GSAP ne sont pas très différentes._

Pour appeler une timeline, vous devez d'abord définir une variable en haut de votre fichier JavaScript comme une nouvelle `TimelineLite` :

```
var tl = new TimelineLite;
```

Pour décomposer cette ligne de code morceau par morceau, sachez que `var` est l'abréviation de variable. Si vous n'êtes pas familier avec ce qu'est une variable, pensez-y comme une abréviation pour un morceau de code plus grand. Dans ce cas, nous avons défini une nouvelle variable comme `tl` et l'avons définie égale à `new TimelineLite`. Cela signifie que chaque fois que nous entrons `tl` dans notre code, il représentera une nouvelle `TimelineLite`.

Notez que nous pouvons substituer `tl` par n'importe quel texte abrégé que nous souhaitons. J'utilise `tl` parce que c'est l'abréviation de `timeline`. Cela est utile car si nous avons plusieurs timelines dans notre fichier, nous pouvons donner à chacune une variable unique pour éviter la confusion.

Recréons maintenant notre première animation en utilisant `TimelineLite` au lieu de `TweenLite` pour voir comment cela fonctionne.

```
var tl = new TimelineLite;
```

```
tl.to("#rectangle", 2, {  x:100,  y:75, backgroundColor: "#000000", ease: Power4.easeIn})
```

![Image](https://cdn-media-1.freecodecamp.org/images/5wj2zfQPRu21MgfKvEsL1Op66MuUkf6k1kAM)
_Remarquez comment il rend la même animation que le tween précédent._

Vous remarquerez que cela n'est pas très différent de notre animation `TweenLite` ci-dessus. La seule vraie différence est qu'au lieu de dire `TweenLite.to`, nous utilisons `tl.to` à la place. Vous remarquerez également que nous utilisons maintenant les coordonnées `x` et `y` au lieu des propriétés CSS `left` et `top`. Celles-ci se comportent plus ou moins de la même manière.

Remarquez également comment il n'y a pas de point-virgule à la fin de la parenthèse. Cela est dû au fait que nous allons ajouter une deuxième animation à cette timeline, les reliant ensemble.

Pour cette deuxième animation, faisons en sorte que le rectangle s'agrandisse de 150 % et devienne gris après que la première animation soit terminée. Pour ce faire, nous ajouterons un autre bloc de code sous notre première animation. Dans l'ensemble, cela ressemblera à ceci :

```
var tl = new TimelineLite;
```

```
tl.to("#rectangle", 2, {  x:100,  y: 75, backgroundColor: "#000000", ease: Power4.easeIn})
```

```
.to("#rectangle", 1, { scaleX: 1.5, scaleY: 1.5, backgroundColor: "#454545", ease: Back.easeOut.config(1.7)});
```

![Image](https://cdn-media-1.freecodecamp.org/images/94-ghLwuO8WBZMKUAcao7H5LhZv5E8KTP12j)
_Nous relions maintenant deux animations ensemble dans une timeline._

Vous pouvez voir que ce deuxième bloc de code n'a pas `tl.to` au début de la timeline. Au lieu de cela, il n'a que `.to`.

Cela est dû au fait que plusieurs animations dans une timeline peuvent être reliées ensemble tant qu'il n'y a pas de point-virgule les séparant.

Un point-virgule signifie la fin d'une timeline et ne doit être utilisé qu'à la fin de la dernière animation dans une timeline.

Vous remarquerez également que nous utilisons deux nouvelles propriétés, `scaleX` et `scaleY`. Ces propriétés se comportent exactement comme elles le suggèrent, elles augmentent la taille d'un objet d'un certain pourcentage. Dans ce cas, 1.5 est équivalent à 150 %.

Enfin, nous utilisons une fonction d'easing unique ici appelée `Back.easeOut.config(1.7)`. Cet easing donne un rythme naturel à notre animation en dépassant la valeur prévue puis en revenant à la valeur finale. Nous pouvons voir dans le cas de cette animation comment le rectangle devient légèrement plus grand que 150 % puis se redimensionne ensuite.

#### Animation de plusieurs objets avec TimelineLite

Les timelines ne sont pas limitées à l'animation d'un seul objet. Vous pouvez animer plusieurs objets dans une timeline en ajoutant leurs ID correspondants dans différentes fonctions.

Par exemple, si nous voulions créer un objet HTML d'un cercle et le faire apparaître après que notre rectangle s'agrandisse, notre code ressemblerait à ceci :

```
var tl = new TimelineLite;
```

```
tl.to("#rectangle", 2, {  x:100,  y: 75, backgroundColor: "#000000", ease: Power4.easeIn})
```

```
.to("#rectangle", 1, { scaleX: 1.5, scaleY: 1.5, backgroundColor: "#454545", ease: Back.easeOut.config(1.7)})
```

```
.from("#circle", 1, { opacity: 0,});
```

![Image](https://cdn-media-1.freecodecamp.org/images/k3esUfRsGnVa35rCSbl4XiLXCxbrYQswSfVj)
_Ce dernier bloc de code a maintenant un cercle qui apparaît à la fin de notre animation._

Nous avons ajouté un troisième bloc de code à notre animation qui appelle le cercle.

Remarquez également comment nous utilisons maintenant la méthode `.from`. Cela signifie que notre animation de cercle commence à 0 % d'opacité puis passe à 100 % d'opacité.

Vous pouvez voir cela en action lorsque notre animation a le cercle caché car il commence à 0 % d'opacité. Après que le rectangle change de couleur et s'agrandisse, le cercle apparaît à 100 % d'opacité, comme prévu.

Vous pouvez voir comment TimelineLite fonctionne dans cet exemple CodePen [ici](https://codepen.io/Nickramer/pen/ddMqZY). Je vous encourage à essayer d'ajouter de nouveaux éléments au HTML et à essayer de créer des séquences plus compliquées et uniques avec les outils fournis. Vous pouvez également consulter la documentation complète de GSAP TimelineLite [ici](https://greensock.com/docs/TimelineLite) pour en apprendre davantage sur d'autres méthodes et propriétés.

### DrawSVG

En plus des fonctionnalités gratuites TweenLite et TimelineLite, GSAP propose également du contenu premium qui vous permet de manipuler facilement les SVGs. Heureusement, ces plugins sont disponibles pour jouer gratuitement sur CodePen en les recherchant dans les paramètres du pen (l'icône d'engrenage à côté de l'éditeur de texte JS).

Le plugin DrawSVG facilite l'animation des lignes d'un SVG. Pour montrer cela, nous allons avoir un SVG d'une licorne dans un sweat à capuche qui se dessine elle-même. Vous pouvez suivre avec le CodePen correspondant [ici](https://codepen.io/Nickramer/pen/JXQeLM).

![Image](https://cdn-media-1.freecodecamp.org/images/XintxK8gySO2Q8qYrIYpSoAVlTbsGeYldO2M)
_Le résultat final de l'animation des lignes SVG._

Tout d'abord, nous devons exporter notre SVG et l'importer dans notre éditeur de texte.

Pour une analyse complète sur la façon d'exporter correctement les SVGs, consultez un article précédent [ici](https://blog.prototypr.io/css-animations-for-non-developers-part-2-svgs-1f6713104764).

Ensuite, nous devons donner à chacun de nos chemins individuels un ID afin que nous puissions appeler chacun dans notre timeline. Cela peut prendre un certain temps si vous avez un SVG compliqué avec une série de lignes animées différentes. Pour simplifier, je vais nommer le premier chemin `#unicorn1` et nommer le chemin suivant `#unicorn2` et ainsi de suite jusqu'à ce qu'ils aient tous un ID unique.

```
<!--Un exemple de chemin avec un ID--><path id="unicorn1" class="st0" d="M371.8,252.4c0,0,2.8,1.8,5,1.2"/>
```

Maintenant que tous nos chemins ont un ID, nous pouvons nous lancer et commencer à développer notre animation de timeline. Comme avant, nous devons créer une variable qui fonctionnera comme notre variable `TimelineLite` :

```
var unicorndraw = new TimelineLite();
```

Dans ce cas, nous allons utiliser la variable `unicorndraw`.

La dernière étape que nous devons faire est de créer une animation TimelineLite qui appelle chacun des chemins individuels :

```
unicorndraw.from("#unicorn1, #unicorn2, #unicorn3, #unicorn4, #unicorn5, #unicorn6, #unicorn7, #unicorn8, #unicorn9, #unicorn10, #unicorn11, #unicorn12, #unicorn13, #unicorn14, #unicorn15, #unicorn16, #unicorn17, #unicorn18, #unicorn19, #unicorn20, #unicorn21, #unicorn22, #unicorn23, #unicorn24, #unicorn25, #unicorn26, #unicorn27, #unicorn28, #unicorn29, #unicorn30, #unicorn31, #unicorn32, #unicorn33, #unicorn34, #unicorn35, #unicorn36, #unicorn37, #unicorn38, #unicorn39, #unicorn40, #unicorn41, #unicorn42, #unicorn43, #unicorn44, #unicorn45, #unicorn46, #unicorn47, #unicorn48, #unicorn49, #unicorn50, #unicorn51, #unicorn52, #unicorn53, #unicorn54, #unicorn55, #unicorn56, #unicorn57, #unicorn58, #unicorn59, #unicorn60, #unicorn61, #unicorn62, #unicorn63", 3, {drawSVG:"0", delay:"1"})
```

Vous pouvez voir comment cela ressemble à notre animation TimelineLite `.from` précédente. Nous appelons nos objets individuels (dans ce cas, nous en appelons plus d'un à la fois afin qu'ils s'animent tous en même temps) et nous définissons la durée de l'animation à 3 secondes.

La seule différence est qu'à l'intérieur des crochets, nous utilisons maintenant `drawSVG: "0"`. Cela appelle le plugin drawSVG et définit chaque chemin pour avoir une valeur de 0. Parce que nous utilisons une méthode `.from`, les chemins commencent avec une valeur de 0 puis s'animent à 100 % en 3 secondes.

![Image](https://cdn-media-1.freecodecamp.org/images/nNJdLZxbk3jzMo91PRFoUzy8a-Nr2Tb-AUpr)
_Vous pouvez jouer avec différentes valeurs pour obtenir un style d'animation unique._

L'autre morceau de code à l'intérieur des crochets est `delay: "1"`. Cela détermine combien de temps l'animation attendra avant de s'exécuter en secondes. Dans ce cas, nous indiquons que l'animation attendra 1 seconde avant de s'exécuter.

C'est le moyen le plus rapide de commencer avec le plugin drawSVG, mais vous pouvez manipuler les valeurs de nombreuses manières différentes pour obtenir des effets intéressants. Pour en savoir plus sur ce plugin, consultez le [site](https://greensock.com/drawSVG) de GSAP.

### Réflexions finales

GSAP facilite la création et la manipulation de vos propres animations de timeline même si vous avez peu ou pas de connaissances en JavaScript. Ceci n'était qu'une petite partie des différentes animations que vous pouvez faire avec GSAP. Consultez le [site](https://greensock.com/) de Greensock pour en savoir plus sur la bibliothèque et expérimenter différentes techniques d'animation.

Nicholas Kramer est un designer travaillant actuellement chez [Barrel](https://www.barrelny.com/) à New York. Il résout des problèmes de design pour les entreprises en les aidant à simplifier les idées et à communiquer leur valeur aux clients.

**_Restez en contact !_** _[Dribbble](https://dribbble.com/NicholasKramer) | [LinkedIn](https://www.linkedin.com/in/nicholas-kramer-3574b463/) | [Site Web](http://kramergraphicdesign.com/)_