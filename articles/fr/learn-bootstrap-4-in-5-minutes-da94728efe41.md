---
title: Apprendre Bootstrap 4 en 5 minutes - Un tutoriel rapide pour bien démarrer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-14T06:44:43.000Z'
originalURL: https://freecodecamp.org/news/learn-bootstrap-4-in-5-minutes-da94728efe41
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9caf76740569d1a4caad90.jpg
tags:
- name: Bootstrap
  slug: bootstrap
- name: CSS
  slug: css
- name: Front-end Development
  slug: front-end-development
- name: 'tech '
  slug: tech
- name: Web Design
  slug: web-design
seo_title: Apprendre Bootstrap 4 en 5 minutes - Un tutoriel rapide pour bien démarrer
seo_desc: 'By Per Harald Borgen

  Get to know the newest version of the worlds most popular front-end component library.

  In January 2018, Bootstrap 4 (aka v4) finally got released after being in alpha
  for over two years. It represents a major rewrite. Not only ar...'
---

Par Per Harald Borgen

#### Découvrez la dernière version de la bibliothèque de composants front-end la plus populaire au monde.

En janvier 2018, Bootstrap 4 (alias v4) a enfin été publié après avoir été en version alpha pendant plus de deux ans. Il représente une réécriture majeure. Non seulement il y a beaucoup de changements sous le capot, mais il y a aussi quelques nouveaux concepts que vous devrez assimiler.

Dans ce tutoriel, je vais donc expliquer les changements les plus importants de Bootstrap v3 à v4. Je suppose que vous avez déjà utilisé Bootstrap, donc je n'expliquerai pas les bases.

Vous pouvez également consulter notre [cours gratuit sur Bootstrap 4 sur Scrimba.](https://scrimba.com/g/gbootstrap4?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gbootstrap4_5_minute_article)

[**Vous voulez apprendre Bootstrap 4 ? Voici notre cours gratuit en 10 parties. Joyeuses Pâques !**](https://medium.freecodecamp.org/want-to-learn-bootstrap-4-heres-our-free-10-part-course-happy-easter-35c004dc45a4)

Examinons maintenant les changements les plus importants (dans un ordre quelconque) :

### #1 : Boutons plus plats

Commençons par un changement visuel et amusant ! Les boutons de la v4 ont un design plus plat que ceux de la v3. Voici les anciens boutons :

![Image](https://cdn-media-1.freecodecamp.org/images/1*i8bry1W2D-UpvXbxAMqEbg.png)

Et voici quelques-uns des nouveaux :

![Image](https://cdn-media-1.freecodecamp.org/images/1*2-33MrQ3wRls06JBzwZyiw.png)

Cela est plus en ligne avec les directives de design modernes comme celles trouvées dans [Material Design](https://material.io/guidelines/), qui est devenu extrêmement populaire ces dernières années.

### #2 : Les media queries sont améliorées

Bootstrap v3 avait trop peu de points d'arrêt pour sa grille, à mon avis, car le plus bas, `xs`, était à 768 px. Beaucoup de trafic provient généralement d'écrans plus étroits que cela, ce qui a été frustrant pour de nombreux développeurs.

Ils ont donc ajouté un nouveau point d'arrêt, `xl`. Celui-ci prend le rôle que `lg` avait auparavant, et pousse le reste des points d'arrêt vers le bas, faisant descendre la plage jusqu'à **576 px**.

```css
$grid-breakpoints: (  xs: 0,  sm: 576px,  md: 768px,  lg: 992px,  xl: 1200px) !default;

```

Cela vous permet de construire plus facilement des grilles qui fonctionnent bien sur _toutes_ les tailles d'écran.

### #3 : Le support de Flexbox vous offre plus de flexibilité

Les célèbres grilles Bootstrap sont maintenant créées avec Flexbox au lieu de floats. À première vue, cela ne fait pas une énorme différence pour vous en tant que développeur, car la plupart des mises en page de grille fonctionnent exactement de la même manière. Cependant, cela ouvre quelques possibilités supplémentaires.

Auparavant, vous deviez définir la largeur de chaque colonne (de 1 à 12). Maintenant, vous pouvez définir la largeur d'_une_ colonne, et laisser les autres être automatiquement définies par Flexbox.

Voici un exemple de comment faire exactement cela :

![Image](https://cdn-media-1.freecodecamp.org/images/1*GzGaj8UK6SglmB_9J4l5VQ.png)

Comme vous pouvez le voir dans le balisage ci-dessous, nous définissons uniquement la largeur de la colonne du milieu à 6 (ce qui équivaut à la moitié de la largeur totale) et les autres colonnes prendront simplement l'espace restant.

```html
<div class="container">  
  <div class="row">    
    <div class="col">1 of 3</div>
    <div class="col-6">2 of 3 (wider)</div>    
    <div class="col">3 of 3</div>  
  </div>
</div>

```

#### Classes Flexbox

Bootstrap 4 propose également un ensemble de classes que vous pouvez appliquer pour contrôler à la fois les conteneurs et les éléments Flexbox. Pour transformer un élément en conteneur Flexbox, il suffit de lui donner la classe `d-flex`.

```css
<div class="d-flex">I'm a flexbox container!</div>

```

Ce qui vous donnera un conteneur Flexbox avec du texte à l'intérieur :

![Note: Im only mentioning the Flexbox related styleshere.](https://cdn-media-1.freecodecamp.org/images/1*UT4MqiVppkBzSaNed4EmVg.png)

  
Note : Je ne mentionne ici que les styles liés à Flexbox.

Ajoutons également quelques éléments et ajoutons une autre classe pour contrôler leur position dans le conteneur.

```html
<div class="d-flex justify-content-center">  
  <div>Flex item</div>  
  <div>Flex item</div>  
  <div>Flex item</div>  
</div>

```

Ce qui fait que les éléments se centrent dans le conteneur :

![Image](https://cdn-media-1.freecodecamp.org/images/1*IqLdXmIHaH2ele21hCISgA.png)

Vous pouvez également ajouter des classes sur les éléments eux-mêmes. Consultez la [section Flex](https://getbootstrap.com/docs/4.0/utilities/flex/) dans la documentation pour en savoir plus à ce sujet.

### #4 : Contrôlez l'espacement avec des classes

Cela est assez cool. Vous pouvez maintenant contrôler les marges et les rembourrages en utilisant les classes `p-*` et `m-*`. La plage va de 0,25 rem à 3 rem en appliquant les nombres de 0 à 5.

Par exemple, donnons à notre conteneur Flexbox une classe `p-5`, afin de créer autant de rembourrage que possible :

```html
<div class="d-flex p-5">I'm a flexbox container!</div>

```

Voici à quoi cela ressemblera :

![Image](https://cdn-media-1.freecodecamp.org/images/1*BFcE6XXy_x9mV8R7zBVy3A.png)

Vous pouvez également ajouter `t`, `b`, `r` ou `l` si vous voulez un espacement sur des côtés spécifiques (haut, bas, droite, gauche), comme ceci :

```html
<div class="d-flex pl-5">I'm a flexbox container!</div>

```

Cela ajoutera uniquement un rembourrage sur le côté gauche, comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*QmKsaoU7zpx753Po4bFOSw.png)

Note : le conteneur flexbox original avait en réalité une classe `_p-2_` par défaut.

### #5 : Des pixels aux rems

Bootstrap 4 a remplacé les pixels par des unités de mesure relatives (rems) dans tous les endroits sauf pour les media queries et les comportements de grille. Cela signifie plus de flexibilité et de réactivité, car les unités rem ne sont pas absolues, contrairement aux pixels.

Avec les `rems`, toutes les tailles de police sont relatives à l'élément racine (la balise `html`), et par défaut, `1rem` équivaut à `16px`. Cependant, si vous changez la taille de la police à, disons, 50% dans l'élément racine, alors `1rem` équivaudra à `8px` dans toute l'application.

Notez que ce changement ne signifie pas que vous devez utiliser des `rems` lorsque vous appliquez vos propres styles sur votre site web.

### #6 : Les cartes remplacent les panneaux, les puits et les miniatures

Bootstrap propose également un tout nouveau composant appelé cartes, qui remplace les [panneaux](https://getbootstrap.com/docs/3.3/components/#panels), les [puits](https://getbootstrap.com/docs/3.3/components/#wells) et les [miniatures](https://getbootstrap.com/docs/3.3/components/#thumbnails). Une carte est un conteneur de contenu flexible et extensible. Elle inclut des options pour les en-têtes et les pieds de page, une grande variété de contenu, des couleurs de fond contextuelles et des options d'affichage puissantes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UYPC0IHtsW6d6WMYYQ9_OQ.png)

### #7 : Adieu IE9

Bootstrap v4 a abandonné le support pour IE8, IE9 et iOS 6. v4 est maintenant uniquement compatible avec IE10+ et iOS 7+. Pour les sites nécessitant l'un de ceux-ci, utilisez v3.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jnuoJeC371Sd9_ClrOiO_w.jpeg)

Il y a bien sûr beaucoup d'autres changements qui n'ont pas été mentionnés dans cet article, alors consultez la [section Migration](https://getbootstrap.com/docs/4.0/migration/) dans la documentation pour voir tous les changements.

Enfin, si vous voulez apprendre correctement Bootstrap v4, assurez-vous de [consulter notre cours gratuit sur Scrimba.](https://scrimba.com/g/gbootstrap4?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gbootstrap4_5_minute_article)

De plus, lorsque vous en êtes arrivé là, n'hésitez pas à me contacter via Twitter :

Merci d'avoir lu ! Je m'appelle Per, je suis le cofondateur de [Scrimba](https://scrimba.com?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gbootstrap4_5_minute_article), et j'adore aider les gens à apprendre de nouvelles compétences. Suivez-moi sur [Twitter](https://twitter.com/perborgen) si vous souhaitez être informé des nouveaux articles et ressources.

---

Merci d'avoir lu ! Je m'appelle Per Borgen, je suis le cofondateur de [Scrimba](https://scrimba.com?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gbootstrap4_5_minute_article) – la manière la plus facile d'apprendre à coder. Vous devriez consulter notre [bootcamp de design web réactif](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gbootstrap4_5_minute_article) si vous voulez apprendre à construire des sites web modernes à un niveau professionnel.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Cliquez ici pour accéder au bootcamp avancé.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gbootstrap4_5_minute_article)_