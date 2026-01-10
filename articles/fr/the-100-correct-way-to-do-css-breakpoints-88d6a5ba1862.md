---
title: La méthode 100 % correcte pour gérer les breakpoints CSS
date: '2016-11-19T05:41:29.000Z'
authorURL: ''
originalURL: https://freecodecamp.org/news/the-100-correct-way-to-do-css-breakpoints-88d6a5ba1862
posteditor: ''
proofreader: ''
author: freeCodeCamp
co_authors: []
series: null
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7YeOvzoYgUEDJdfQy2ERXg.png
tags:
- name: CSS
  slug: css
- name: responsive design
  slug: responsive-design
- name: 'tech '
  slug: tech
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_desc: 'By David Gilbertson

  For the next minute or so, I want you to forget about CSS. Forget about web development.
  Forget about digital user interfaces.

  And as you forget these things, I want you to allow your mind to wander. To wander
  back in time. Back t...'
---


Par David Gilbertson

<!-- more -->

Pendant la minute qui suit, je veux que vous oubliiez le CSS. Oubliez le développement web. Oubliez les interfaces utilisateur numériques.

Et pendant que vous oubliez ces choses, je veux que vous laissiez votre esprit vagabonder. Remontez le temps. Revenez à votre jeunesse. À votre premier jour d'école.

C'était une époque plus simple, où vos seuls soucis étaient de dessiner des formes et de garder le contrôle de votre incontinence.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XoDgRc5GXaxo7j47ClsIgw.png)

Regardez les points ci-dessus. Remarquez comment certains sont regroupés et d'autres dispersés ? Ce que je veux que vous fassiez, c'est de les diviser en cinq groupes pour moi, comme bon vous semble.

Allez-y. Après avoir vérifié que personne ne vous regarde, dessinez un cercle autour de chacun des cinq groupes avec votre doigt d'enfant.

Vous êtes probablement arrivé à quelque chose comme l'image ci-dessous, n'est-ce pas ? (Et quoi que vous fassiez, ne me dites pas que vous avez fait défiler la page sans faire l'exercice. Je m'en frapperais le front de désespoir.)

![Image](https://cdn-media-1.freecodecamp.org/images/1*cZcTR2tVMzYg1U1h3cqdNg.png)

Bien sûr, ces deux points sur la droite auraient pu aller dans un sens ou dans l'autre. Si vous les avez regroupés, c'est OK, j'imagine. On dit qu'il n'y a pas de mauvaise réponse, mais comme je n'ai jamais eu tort, je n'ai jamais été la cible de ce genre de platitude.

Avant de continuer, avez-vous dessiné quelque chose comme ça ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*RZryP0xAyOy1_WRpBdPIog.png)

Probablement pas. N'est-ce pas ?

Pourtant, c'est essentiellement ce que vous faites si vous définissez vos breakpoints à des positions correspondant à la largeur exacte des appareils populaires (320px, 768px, 1024px).

![Image](https://cdn-media-1.freecodecamp.org/images/1*pwC0py16i-sQr1agaP26QQ.png)

Des mots de cette nature ont-ils déjà atteint vos oreilles ou franchi vos lèvres ?

> « Est-ce que le breakpoint medium va *jusqu'à* 768px, ou inclut-il 768 ? Je vois... et c'est l'iPad en mode paysage, ou est-ce "large" ? Oh, large c'est 768px *et plus*. Je vois. Et small c'est 320px ? C'est quoi cette plage de 0 à 319px ? Un breakpoint *pour les fourmis* ? »

Je pourrais me contenter de vous montrer les bons breakpoints et m'arrêter là. Mais je trouve très curieux que la méthode ci-dessus (« le regroupement absurde ») soit si répandue.

Pourquoi donc ?

Je pense que la réponse à ce problème, comme à tant d'autres, réside dans une terminologie mal alignée. Après tout, la *simulation de noyade à Guantanamo Bay* a l'air super cool si vous ne savez pas ce que sont ces deux choses. (Oh, [j'aimerais][1] que cette blague soit de moi.)

Je pense que nous mélangeons « limites » (boundaries) et « plages » (ranges) dans nos discussions et nos implémentations de breakpoints.

Dites-moi, si vous gérez vos breakpoints en Sass, avez-vous une variable appelée `$large` qui vaut, disons, 768px ?

Est-ce la limite inférieure de la plage que vous appelez large, ou la limite supérieure ? Si c'est la limite inférieure, alors vous ne devez pas avoir de `$small` car cela devrait être `0`, n'est-ce pas ?

Et si c'est la limite supérieure, comment définiriez-vous un breakpoint `$large-and-up` ? Ce doit être une media query avec un `min-width` de `$medium`, non ?

Et si vous ne faites référence qu'à une limite quand vous dites "large", alors nous allons vers une confusion certaine plus tard car une media query est toujours une *plage*.

Cette situation est un désordre et nous perdons du temps à y réfléchir. J'ai donc trois suggestions :

1.  Choisissez bien vos break_points_
2.  Nommez vos _plages_ de manière sensée
3.  Soyez déclaratif

### Conseil n°1 : Bien choisir ses breakpoints

Alors, quels sont les *bons* breakpoints ?

Votre "vous" de la maternelle a déjà dessiné les cercles. Je vais juste les transformer en rectangles pour vous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-ldpo5wcYVnuyRFbO24WPQ.png)

600px, 900px, 1200px, et 1800px si vous prévoyez d'offrir quelque chose de spécial aux personnes possédant des écrans géants. Note à part : si vous commandez un écran géant en ligne, assurez-vous de préciser que c'est pour un ordinateur. Vous ne voudriez pas [recevoir un lézard géant par la poste][2].

Ces points avec lesquels votre jeune moi a joué représentent en fait les 14 tailles d'écran les plus courantes :

![Image](https://cdn-media-1.freecodecamp.org/images/1*199KbL2oM2P5d4pFMBXYxQ.png) \_\[crédit image\](http://gs.statcounter.com/#desktop+mobile+tablet-resolution-ww-monthly-201608-201610-bar" rel="noopener" target="_blank" title=")_

Nous pouvons donc créer une jolie petite image qui permet une communication fluide entre les personnes déguisées en gens d'affaires, les designers, les développeurs et les testeurs.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7YeOvzoYgUEDJdfQy2ERXg.png) _Je regrette mon choix d'orange et de vert, mais je ne vais pas refaire toutes ces images maintenant._

### Conseil n°2 : Nommer ses plages de manière sensée

Bien sûr, vous pourriez nommer vos breakpoints [papa-ours et bébé-ours][3] si vous voulez. Mais si je dois m'asseoir avec un designer et discuter de l'apparence du site sur différents appareils, je veux que ce soit réglé le plus vite possible. Si nommer une taille *tablette portrait* facilite cela, alors je suis partant. Bon sang, je vous pardonnerais même de l'appeler « iPad portrait ».

« Mais le paysage change ! » pourriez-vous crier. « Les téléphones deviennent plus grands, les tablettes plus petites ! »

Mais le CSS de votre site Web a une durée de vie d'environ trois ans (sauf s'il s'agit de Gmail). L'iPad est parmi nous depuis deux fois plus longtemps, et il n'a pas encore été détrôné. Et nous savons qu'Apple ne fabrique plus de nouveaux produits, ils se contentent de supprimer des éléments de ceux qui existent déjà (boutons, prises, etc.).

Donc le 1024 x 768 est là pour durer, les amis. Ne faisons pas l'autruche. (Fait amusant : les autruches ne vivent pas dans les villes parce qu'il n'y a pas de sable, et donc nulle part où se cacher des prédateurs.)

Conclusion : la communication est importante. Ne vous détachez pas volontairement d'un vocabulaire utile.

### Conseil n°3 : Soyez déclaratif

Je sais, je sais, encore ce mot « déclaratif ». Je vais le dire autrement : votre CSS devrait définir *ce qu'il* veut qu'il se passe, et non *comment* cela doit se passer. Le « comment » doit être caché dans une sorte de mixin.

Comme nous l'avons vu précédemment, une partie de la confusion autour des breakpoints vient du fait que des variables définissant une *limite* d'une plage sont utilisées comme *nom* de la plage. `$large: 600px` n'a tout simplement aucun sens si `large` est une plage. C'est comme dire `var coordinates = 4;`.

Nous pouvons donc masquer ces détails à l'intérieur d'un mixin plutôt que de les exposer dans le code. Ou nous pouvons faire encore mieux et ne pas utiliser de variables du tout.

Au début, j'ai écrit l'extrait ci-dessous comme un exemple simplifié. Mais en réalité, je pense qu'il couvre tous les cas de figure. Pour le voir en action, [consultez ce pen][4]. J'utilise Sass parce que je ne peux pas imaginer construire un site sans lui. La logique s'applique de la même manière au CSS ou à Less.

```
@mixin for-phone-only {
  @media (max-width: 599px) { @content; }
}
@mixin for-tablet-portrait-up {
  @media (min-width: 600px) { @content; }
}
@mixin for-tablet-landscape-up {
  @media (min-width: 900px) { @content; }
}
@mixin for-desktop-up {
  @media (min-width: 1200px) { @content; }
}
@mixin for-big-desktop-up {
  @media (min-width: 1800px) { @content; }
}

// utilisation
.my-box {
  padding: 10px;

  @include for-desktop-up {
    padding: 20px;
  }
}
```

Notez que je force le développeur à spécifier le suffixe `-up` ou `-only`.

> L'ambiguïté engendre la confusion.

Une critique évidente pourrait être que cela ne gère pas les media queries personnalisées. Eh bien, bonne nouvelle pour tout le monde. Si vous voulez une media query personnalisée, écrivez une media query personnalisée. (En pratique, si j'avais besoin de plus de complexité que ce qui précède, je jetterais l'éponge et me réfugierais dans les bras de la boîte à outils de [Susy][5].)

Une autre critique pourrait être que j'ai huit mixins ici. Il serait sûrement plus raisonnable de n'avoir qu'un seul mixin, puis de passer simplement la taille requise, comme ceci :

```
@mixin for-size($size) {
  @if $size == phone-only {
    @media (max-width: 599px) { @content; }
  } @else if $size == tablet-portrait-up {
    @media (min-width: 600px) { @content; }
  } @else if $size == tablet-landscape-up {
    @media (min-width: 900px) { @content; }
  } @else if $size == desktop-up {
    @media (min-width: 1200px) { @content; }
  } @else if $size == big-desktop-up {
    @media (min-width: 1800px) { @content; }
  }
}

// utilisation
.my-box {
  padding: 10px;

  @include for-size(desktop-up) {
    padding: 20px;
  }
}
```

Bien sûr, ça fonctionne. Mais vous n'aurez pas d'erreurs à la compilation si vous passez un nom non supporté. Et passer une variable Sass signifie exposer 8 variables juste pour les passer à un switch dans un mixin.

Sans oublier que la syntaxe `@include for-desktop-up {...}` est carrément plus jolie que `@include for-size(desktop-up) {...}`.

Une critique de ces deux extraits de code pourrait être que je tape 900px deux fois, ainsi que 899px. Je devrais sûrement utiliser des variables et soustraire 1 quand c'est nécessaire.

Si vous voulez faire ça, lâchez-vous, mais il y a deux raisons pour lesquelles je ne le ferais pas :

1.  Ce ne sont pas des choses qui changent fréquemment. Ce ne sont pas non plus des nombres utilisés ailleurs dans le code. Aucun problème n'est causé par le fait qu'ils ne *soient pas* des variables — à moins que vous ne vouliez exposer vos breakpoints Sass à un script qui injecte un objet JS avec ces variables dans votre page.
2.  La syntaxe est *atroce* quand on veut transformer des nombres en chaînes de caractères avec Sass. Voici le prix à payer si vous croyez que répéter un nombre deux fois est le pire des maux :

```
@mixin for-size($range) {
  $phone-upper-boundary: 600px;
  $tablet-portrait-upper-boundary: 900px;
  $tablet-landscape-upper-boundary: 1200px;
  $desktop-upper-boundary: 1800px;

  @if $range == phone-only {
    @media (max-width: #{$phone-upper-boundary - 1}) { @content; }
  } @else if $range == tablet-portrait-up {
    @media (min-width: $phone-upper-boundary) { @content; }
  } @else if $range == tablet-landscape-up {
    @media (min-width: $tablet-portrait-upper-boundary) { @content; }
  } @else if $range == desktop-up {
    @media (min-width: $tablet-landscape-upper-boundary) { @content; }
  } @else if $range == big-desktop-up {
    @media (min-width: $desktop-upper-boundary) { @content; }
  }
}

// utilisation
.my-box {
  padding: 10px;

  @include for-size(desktop-up) {
    padding: 20px;
  }
}
```

Oh, et puisque j'ai pris un ton un peu râleur dans les derniers paragraphes... je plains le pauvre fou qui fait quelque chose de magique comme stocker des breakpoints dans une liste Sass et boucler dessus pour générer des media queries, ou quelque chose d'aussi ridicule que les futurs développeurs auront du mal à déchiffrer.

> C'est dans la complexité que se cachent les bugs.

Enfin, vous vous dites peut-être : « ne devrais-je pas baser mes breakpoints sur le contenu, et non sur les appareils ? ». Eh bien, je suis étonné que vous soyez arrivé jusqu'ici et la réponse est oui... pour les sites avec une mise en page unique. Ou si vous avez plusieurs mises en page et que vous êtes heureux d'avoir un ensemble différent de breakpoints pour chaque mise en page. Oh, et aussi si le design de votre site ne change pas souvent, ou si vous êtes prêt à mettre à jour vos breakpoints quand vos designs changent puisque vous voudrez les *maintenir* basés sur le contenu, n'est-ce pas ?

Pour les sites complexes, la vie est beaucoup plus facile si vous choisissez une poignée de breakpoints à utiliser sur tout le site.

C'est fini ! Mais cet article n'a pas été aussi poilu que je l'aurais souhaité, voyons si je peux trouver une excuse pour en inclure...

Oh, je sais !

### Conseils bonus pour le développement de breakpoints

![Image](https://cdn-media-1.freecodecamp.org/images/1*ClU6ZZNLtd0ux8nqRPfhng.png) _Oui, même Flickr a des breakpoints à 768 et 1400_

1.  Si vous avez besoin de tester des breakpoints CSS pour des tailles d'écran plus grandes que le moniteur devant lequel vous êtes assis, utilisez le mode « responsive » dans les Chrome DevTools et tapez la taille géante que vous voulez.
2.  La barre bleue affiche les media queries `max-width`, la barre orange les media queries `min-width`, et la barre verte affiche les media queries avec à la fois un min et un max.
3.  Cliquer sur une media query règle l'écran à cette largeur. Si vous cliquez sur une media query verte plus d'une fois, elle bascule entre les largeurs max et min.
4.  Faites un clic droit sur une media query dans la barre des media queries pour accéder à la définition de cette règle dans le CSS.

Hé, merci d'avoir lu ! Commentez avec vos meilleures idées, j'adorerais les entendre. Et cliquez sur le petit cœur si vous pensez que je le mérite, ou laissez-le vide, comme le sera mon estime de moi si vous ne le faites pas.

[1]: https://www.reddit.com/r/Showerthoughts/comments/2ucx09/waterboarding_at_guantanamo_bay_sounds_super_rad/
[2]: http://metro.co.uk/2016/06/16/this-monster-lizard-at-the-door-is-absolutely-terrifying-5947737/
[3]: https://css-tricks.com/naming-media-queries/
[4]: http://codepen.io/davidgilbertson/pen/aBpJzO
[5]: http://susydocs.oddbird.net/en/latest/toolkit/#breakpoint