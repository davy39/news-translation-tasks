---
title: Conseils CSS que vous ne verrez probablement dans aucun tutoriel
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-20T21:43:09.000Z'
originalURL: https://freecodecamp.org/news/css-tips-that-you-likely-wont-see-in-any-tutorial-3af201315a76
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5YzOyUp5pIiHVAu8OQhGtg.jpeg
tags:
- name: CSS
  slug: css
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Conseils CSS que vous ne verrez probablement dans aucun tutoriel
seo_desc: 'By Cristian Traina

  There are CSS rules that you can find in any tutorial.

  And then there are CSS rules that you don’t find in tutorials, but that you faced
  immediately when you started coding. I’m sure you already googled about how to vertical
  align ...'
---

Par Cristian Traina

Il existe des règles CSS que vous pouvez trouver dans n'importe quel tutoriel.

Et puis il y a des règles CSS que vous ne trouvez pas dans les tutoriels, mais que vous avez rencontrées immédiatement lorsque vous avez commencé à coder. Je suis sûr que vous avez déjà cherché sur Google comment aligner verticalement un élément et comment créer cette mise en page complexe. Nous n'en parlerons pas.

Enfin, il y a ces règles CSS que vous n'avez rencontrées dans aucun tutoriel et que vous ne pouviez pas connaître. J'ai collecté ces conseils au fil du temps, et maintenant j'ai décidé d'écrire un article, en espérant qu'ils puissent être utiles pour d'autres personnes.

Ce qui suit est ce que les tutoriels CSS ne m'ont jamais appris.

### Padding-top est relatif à la largeur du parent

Combien de fois avez-vous utilisé des unités relatives en CSS ? Je suis un grand fan de celles-ci, car elles vous permettent de créer un site web responsive sans trop vous soucier des media queries. Si vous voulez définir la hauteur d'un élément comme la moitié de la hauteur du parent, écrire `height: 50%` suffit.

Vous pouvez utiliser des unités relatives partout. Si vous voulez ajouter une distance entre deux éléments verticaux, vous pouvez écrire `margin-top: 15%` et cela créera la marge. La distance sera de 15 % de la hauteur du parent. Je pense que vous le savez déjà, et je ne veux pas perdre votre temps. Mais peut-être ne savez-vous pas que ce n'est pas si trivial.

Dans certaines situations, il est préférable d'utiliser le padding à la place de la marge. Mais lorsque vous définissez `padding-top: 15%`... qu'est-ce qui se passe ?

Cela ne fonctionne pas comme prévu. Ce n'est pas relatif à la hauteur du parent. Qu'est-ce qui se passe ?

#### **Solution**

C'est relatif à la largeur du parent.

Vous voulez une démonstration pratique ? La voici :

Il suffit de jouer avec la largeur du parent et de voir comment le padding de l'enfant est affecté.

Cela peut sembler étrange au premier abord, mais il y a en fait une raison significative à cela. Vous pouvez la découvrir en lisant les spécifications CSS...

Non, je plaisante, il n'y a pas d'explication à cela. Ou, du moins, je ne l'ai trouvée nulle part. Cela fonctionne simplement comme ça, alors gardez cela à l'esprit.

Même si nous ne comprenons peut-être pas la raison pour laquelle les ingénieurs l'ont fait, nous pouvons utiliser cette fonctionnalité à notre avantage. Si nous avons un élément et que nous définissons ce qui suit :

```
.parent {  height: auto;  width: 100px;}
```

```
.child {  padding-top: 100%;}
```

Alors, la hauteur de l'élément sera égale à la hauteur de l'enfant, puisque nous avons défini `height: auto`. La hauteur de l'enfant, en revanche, sera la même que la largeur du parent, puisque nous avons défini `padding-top: 100%`. Le résultat est un carré, et l'élément conservera le même ratio à toute taille.

Voici un exemple fonctionnel :

Si vous changez `padding-top: 100%` par un autre pourcentage, vous obtiendrez un rectangle. De plus, si vous changez la largeur, le ratio est toujours conservé.

### Transform peut empiler des règles

Si vous avez étudié l'informatique, vous vous souvenez sûrement de cette tortue hideuse et de son stylo rétractable. Ce concept éducatif est plus formellement connu sous le nom de [turtle graphics](https://en.wikipedia.org/wiki/Turtle_graphics), et son objectif est de guider la tortue sur un chemin à travers des instructions simples, étape par étape, telles que « 20 pas en avant » et « tourner de 90 degrés ».

Et si, en utilisant CSS, vous pouviez dire à un bloc de se déplacer « 20 pixels à droite » par rapport à sa position actuelle, et non à sa position de départ ? Et si je vous disais que vous pouvez le faire en utilisant la propriété `transform` ?

De nombreux développeurs ne savent pas que `transform` peut accumuler plus d'une règle, et que la règle `n+1` sera relative à la position atteinte à la règle `n`, plutôt qu'à sa position de départ.

Êtes-vous confus ?

Peut-être que ce stylo peut éclaircir votre esprit :

Notez que nous n'avons pas utilisé de variables JavaScript pour stocker la position actuelle ou la rotation actuelle. Ces informations ne sont stockées nulle part ! La solution est simple, si vous écrivez :

```
transform: translateX(20px);
```

Et puis vous ajoutez une autre règle :

```
transform: translateX(20px) translateX(40px)
```

La deuxième règle ne remplacera pas la première, mais elles seront appliquées une par une, en séquence. Le fait qu'elles soient appliquées en séquence est important. Lorsque vous tournez un élément, vous tournez également le système de référence, et les règles suivantes seront relatives au nouveau système de référence. Donc :

```
transform: rotateZ(20deg) translateX(30px)
```

sera différent de :

```
transform: translateX(30px) rotateZ(20deg)
```

Vous pouvez également combiner différentes unités. Par exemple, vous pouvez centrer une div de 600 pixels de large de cette manière :

```
transform: translateX(50vw) translateX(-300px)
```

Mais si vous n'allez pas l'animer, peut-être que `calc()` est une meilleure alternative.

Si vous vous demandez ce qu'est devenu la tortue, j'ai créé cet autre extrait qui recrée la dynamique :

Malheureusement, il ne dessine pas encore. Mais si vous le souhaitez, vous pouvez toujours implémenter la fonction _pen_.

### Marges et paddings vont de midi à minuit

C'est facile, et beaucoup d'entre vous vont penser que c'est trivial, mais j'ai vu tant de gens lutter avec les quadruples que j'ai arrêté de le tenir pour acquis.

De nombreux développeurs ne savent pas que presque toutes les propriétés CSS ont une alternative raccourcie. D'autres développeurs le savent, mais ils continuent à utiliser des propriétés spécifiques parce qu'ils ne se souviennent jamais de l'ordre.

Permettez-moi de vous donner un conseil :

**Les marges et les bordures vont de midi à minuit.**

Je peux mieux l'expliquer. Vous pouvez certainement utiliser :

```
padding-top: 3px;padding-left: 6px;padding-right: 6px;padding-bottom: 3px;
```

Mais, vous pouvez également utiliser l'alternative raccourcie :

```
padding: 3px 6px 3px 6px;
```

La règle pour se souvenir de l'ordre est facile, il suffit de regarder cette horloge :

![Image](https://cdn-media-1.freecodecamp.org/images/1*zxqYpjLODfi3RKIZ3tMxWg.png)

Commencez à 12:00 et procédez dans le sens des aiguilles d'une montre. Vous obtiendrez le bon ordre.

Si, au contraire, vous utilisez seulement deux valeurs :

```
padding: 2px 4px;
```

Le moteur du navigateur l'étendra, en répétant le couple :

```
padding: 2px 4px 2px 4px;
```

Et, enfin, si vous utilisez trois valeurs :

```
padding: 2px 4px 6px;
```

Le moteur du navigateur utilisera la valeur du milieu à la fois pour la gauche et pour la droite, comme si vous aviez écrit :

```
padding: 2px 4px 6px 4px;
```

### Background supporte plusieurs images

C'est l'une des propriétés les moins connues, bien qu'elle soit largement supportée.

Vous savez que vous pouvez spécifier une URL d'image dans la propriété `background`, mais si vous en avez besoin, vous pouvez en fait insérer autant d'images que vous le souhaitez. Ce que vous devez faire est de les séparer par une virgule :

```
background: url('first-image.jpeg') top left,            url('second-image.jpeg') bottom right;
```

Pourquoi cela peut-il être utile ? Que pensez-vous de Linus Torvalds devant un lever de soleil généré par CSS ?

Vous pouvez également transformer une image rectangulaire en carré, en ajoutant ces bordures ombrées qui sont très célèbres sur Instagram. Pour y parvenir, j'ai dû répéter la même image deux fois et zoomer l'image de fond 5x :

### Détecter les appareils à écran tactile

Grâce aux media queries, nous pouvons rendre nos sites web responsives et laisser la mise en page s'adapter à de nombreuses tailles d'écran. Mais ce n'est pas suffisant !

Les smartphones, les tablettes et les ordinateurs personnels classiques sont différents par nature. Peu importe la taille de l'écran.

Sur un appareil à écran tactile, vous épinglez, balayez et pincer, et des outils comme [HammerJS](https://hammerjs.github.io/) vous aident. Avec une souris, vous cliquez simplement, mais avec une plus grande précision. Si vous avez rendu votre site web adaptable à différentes tailles d'écran, peut-être pourriez-vous envisager de le rendre responsive dans d'autres directions également, et supporter différents types d'entrée !

Vous n'avez pas besoin de code JavaScript compliqué pour détecter l'agent utilisateur. Tout ce dont vous avez besoin est le CSS :

```
@media (any-pointer: fine) {  /*    Ces règles seront appliquées aux appareils non tactiles  */}
```

```
@media (any-pointer: coarse) {  /*    Ces règles seront appliquées uniquement aux appareils tactiles  */}
```

Voici un exemple :

**Astuce pro :** Vous n'avez pas besoin d'un smartphone pour tester la règle, vous pouvez simuler un appareil tactile sur les outils de développement de Google Chrome en cliquant simplement sur cette icône :

![Image](https://cdn-media-1.freecodecamp.org/images/1*_GCh44P5LmsiXNq1UEx2VQ.png)

Je l'ai trouvé très utile et je ne sais pas pourquoi il ne s'est pas répandu, bien qu'il soit décent supporté. Par exemple, je l'ai utilisé dans un carrousel pour masquer les icônes de _chevrons_ sur les appareils tactiles afin de fournir une expérience plus native.

Et, enfin, vous pouvez également fournir un fichier `touchscreen.css` et l'importer conditionnellement :

```
@import url('touchscreen.css') screen and (any-pointer: coarse);
```

**Note :** ceci n'est actuellement pas supporté par Firefox, comme vous pouvez le voir sur [caniuse.com](https://caniuse.com/#search=any-pointer)

### Les marges aiment s'effondrer

![Image](https://cdn-media-1.freecodecamp.org/images/0*9Y4R8_iMsLJNkFX4.jpg)

> **Et gardez un œil sur les escaliers. Ils aiment changer.**

> _Percy Weasley — Harry Potter_

J'aime CSS : c'est un langage clair, régulier et élégant — tout ce qu'un développeur pourrait demander.

Vous appliquez une règle, et elle fonctionne. Mais quand je pensais connaître CSS, cela s'est produit :

Qu'est-ce qui se passe ici ? Vous vous attendez probablement à ce que le texte ait une marge **à l'intérieur** de l'en-tête, mais il essaie de tirer l'en-tête vers le bas à la place. Ce n'est pas ce que je voulais.

Plus tard, j'ai découvert que les marges aiment s'effondrer.

Que signifie cela ? Supposons que nous voulons créer la mise en page imbriquée suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ga5LtmwuzDy1ywToOBWg5g.png)

Nous avons donc créé le balisage pour trois éléments et nous avons défini une hauteur différente et une marge supérieure différente pour chacun d'eux. Cela devrait fonctionner, non ? Faux.

Si vous le faites, votre navigateur remarquera trois blocs de marges adjacents, et il voudra les joindre en un seul et unique grand bloc de marge.

Par conséquent, le résultat ressemblera à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*pyuE0l73A-G5RRS1iUP6rQ.png)

Pourquoi cela se produit-il ? Je ne sais pas. C'est une caractéristique historique de CSS. Je suppose que, lorsque CSS a été standardisé initialement, les marges n'étaient pas un gros problème et les mises en page n'étaient pas aussi compliquées qu'elles le sont aujourd'hui. Les ingénieurs ont donc peut-être pensé que c'était une fonctionnalité utile. Maintenant, cela n'a plus aucun sens.

Si vous avez développé en CSS pendant des années, et que vous n'avez jamais rencontré ce problème, la raison est que les marges s'effondrent uniquement lorsque :

* les marges sont verticales (cela ne se produit pas pour les marges horizontales)
* les éléments extérieurs ne contiennent pas de texte ou d'autre contenu
* aucun padding ou bordure n'est défini
* l'affichage est « block »
* le débordement est différent de « initial »
* les marges ne sont pas négatives

Et la liste continue. Si vous rencontrez ce problème, vous pouvez simplement nier l'une de ces conditions (sauf la première) et les marges seront domptées. Vous pouvez également éviter d'utiliser `margin-top`, et utiliser `top` et `padding-top` à la place.

Notez que cela peut également se produire pour les éléments frères. Si vous avez deux éléments frères l'un au-dessus de l'autre, et que vous définissez `margin-bottom: 30px` pour le premier et `margin-top: 60px` pour le second, le plus petit s'effondrera. La marge résultante ne sera pas de 30+60=90px, mais elle sera de max(30, 60) = 60px.

### Réflexions finales

C'est tout ! J'espère ne pas avoir perdu votre temps avec cet article, et que vous avez appris quelque chose de valeur.

Si vous avez aimé l'article, vous pouvez cliquer sur le bouton « applaudissements » qui apparaît à votre gauche. Vous pouvez me donner jusqu'à 50 applaudissements :D

Si vous avez des questions, des problèmes, ou si vous voulez simplement me dire ce que le tutoriel ne vous a pas appris, laissez simplement un commentaire dans la section ci-dessous et votre préoccupation sera appréciée !

— Christian Vincenzo Traina