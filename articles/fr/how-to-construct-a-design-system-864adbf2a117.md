---
title: Comment construire un système de design
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-22T17:45:22.000Z'
originalURL: https://freecodecamp.org/news/how-to-construct-a-design-system-864adbf2a117
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9XuqeLVHBBLwog_AsU54DQ.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: Product Design
  slug: product-design
- name: style guides
  slug: style-guides
- name: UI
  slug: ui
seo_title: Comment construire un système de design
seo_desc: 'By Colm Tuite

  Tips for designing and building a consistent design system.

  Without doubt, I get asked about design systems more than anything else. So, having
  spent the majority of the past few years thinking about how to design, build and
  present des...'
---

Par Colm Tuite

#### Conseils pour concevoir et construire un système de design cohérent.

Sans aucun doute, on me demande plus souvent des conseils sur les systèmes de design que sur tout autre sujet. Ayant passé la majorité des dernières années à réfléchir à la manière de concevoir, construire et présenter des systèmes de design pour des produits comme [Marvel](https://blog.marvelapp.com/the-marvel-styleguide/), [Bantam](https://github.com/colmtuite/bantam) et [Modulz](https://github.com/colmtuite/modulz-ui), j'ai pensé partager quelques-unes des choses que j'ai apprises en cours de route.

#### Qu'est-ce qu'un système de design ?

Ce n'est un secret pour personne que les designers adorent un bon kit UI. Cependant, au-delà de la simple création de toolkits et de guides de style, il semble que récemment, l'accent ait été mis de plus en plus sur la conception de systèmes destinés à unifier des produits entiers. Des entreprises comme [Shopify](https://www.shopify.com) et [Intercom](https://boards.greenhouse.io/intercom/jobs/588568#.WK1zUxKLSRs) construisent des équipes internes spécifiquement axées sur la conception de systèmes. Les gens commencent à réaliser l'importance du design systémique. C'est encourageant. Qui sait, peut-être qu'un jour nous aurons un outil de design qui ne suppose pas que nous partons de zéro chaque fois que nous ouvrons un nouveau document... ?

Un système de design (en ce qui concerne les produits technologiques) est plus qu'un framework, un toolkit UI ou une bibliothèque de composants. C'est plus qu'un guide de style ou un ensemble de directives de code. C'est même plus que la somme de ces parties. Un système de design est un ensemble de règles évolutives régissant la composition d'un produit.

Il existe de nombreuses facettes à tout bon système de design, commençant par la culture/mission de l'entreprise et se répercutant jusqu'à la marque, la rédaction, les bibliothèques de composants et d'autres éléments du langage de design. Les points de haut niveau sont probablement les aspects les plus importants de tout système de design, mais pour les besoins de cet article, je vais supposer que, en tant qu'entreprise, vous savez qui vous êtes, quelle est votre mission et comment vos produits doivent apparaître, se sentir et fonctionner.

Une fois que vous avez ces facteurs critiques en place, vous pouvez convertir cette connaissance en un langage de design cohérent.

### Concevoir une palette de styles

Avant de pouvoir commencer à concevoir des composants brillants, nous devons poser les fondations pour ces composants. Nous devons décomposer le produit en sa forme la plus élémentaire.

Même le composant d'en-tête le plus simple est une collection de plusieurs styles réutilisables...

![Image](https://cdn-media-1.freecodecamp.org/images/1*03lT5NXtjHNYgJloKQhbvA.png)

Nous devons décomposer les choses jusqu'à atteindre le minimum irréductible ; les styles les plus essentiels. Un bon point de départ est la liste complète des [propriétés de style CSS](https://www.w3schools.com/cssref/). La plupart de ces propriétés n'acceptent que des valeurs fixes et peuvent donc être réutilisées sur chaque site web sur Internet. Les propriétés qui acceptent des valeurs personnalisées sont finalement ce qui différenciera notre produit des autres produits. Ces valeurs personnalisées sont ce qui définira notre palette de styles globale. Notre palette de styles globale est ce que nous utiliserons pour concevoir et construire chaque aspect de tous nos produits.

Lorsque nous aurons terminé, aucun style ne devrait exister dans notre produit qui n'a pas été prédéfini dans notre palette de styles globale.

#### Couleur

Commençons par la propriété de style la plus évidente, la seule propriété de style qu'il semble que les outils de design modernes comprennent peuvent être nommés, stockés et réutilisés : la couleur.

Pour notre couleur de marque primaire, choisissons le bleu. Pour notre couleur de marque secondaire, optons pour son complémentaire : l'orange.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CrR79K_KOhFUxJBCPd53UA.png)
_Couleurs de marque_

Utiliser la couleur pour communiquer le succès et l'échec est un motif de design courant, alors ajoutons le vert et le rouge à notre palette de couleurs à cette fin. Des couleurs comme le noir et le jaune pourraient également bien fonctionner.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6HuG3meww2tb6w73ooa-2g.png)
_Couleurs de succès et d'échec_

Enfin, nous avons besoin de quelques couleurs grises. La plupart des interfaces utilisateur auront besoin au moins des couleurs grises suivantes :

* Un gris très clair pour les arrière-plans
* Un gris légèrement plus foncé pour les bordures, les lignes, les traits ou les diviseurs.
* Un gris moyen pour les sous-titres et le texte de support.
* Un gris foncé pour les titres principaux, le texte et les arrière-plans.

Bien sûr, vous pourriez avoir besoin de plus de gris. Vous pourriez avoir besoin de trois nuances différentes pour le texte. Vous pourriez préférer deux nuances de trait différentes. C'est à vous de décider. L'important ici est de prédéfinir tous les styles dont vous avez besoin à l'avance afin qu'ils soient réutilisables dans l'ensemble de votre produit à un stade ultérieur.

En tant que touche finale, nous pourrions également vouloir ajouter des variations de teinte ou d'ombre pour chacune de nos couleurs. Celles-ci peuvent être utiles lors de la conception de composants pour ajouter des arrière-plans clairs ou des traits sombres.

![Image](https://cdn-media-1.freecodecamp.org/images/1*VfncQaKuCPAhnfRk5iKDyQ.png)
_Notre palette de couleurs finale_

#### Ombres

Les ombres sont une autre propriété de style couramment utilisée dans la plupart des interfaces utilisateur. D'après ce que j'ai vu, beaucoup de designers inventent des ombres à la volée lors de la conception de composants. Il en va de même pour la plupart des propriétés de style, en fait. Concevoir de manière isolée comme cela conduit souvent à des interfaces utilisateur incohérentes.

Faisons un pas en arrière et réfléchissons à ce que nous essayons d'accomplir avec nos ombres. Nous essayons évidemment d'ajouter une certaine perspective à l'interface utilisateur, mais il est probable que de nombreux composants puissent bénéficier du même effet. Alors, abstraisons les styles des composants individuels et intégrons-les à notre palette de styles globale.

Ces quatre ombres devraient suffire à styliser chaque composant de notre système :

* Une ombre subtile pour surélever les composants interactifs et ajouter une affordance.
* Une ombre plus prononcée pour un effet de survol sur les composants.
* Une ombre forte pour donner de la perspective aux menus déroulants/popovers et autres composants similaires.
* Une ombre éloignée pour les composants modaux.

![Image](https://cdn-media-1.freecodecamp.org/images/1*9v3d-bqpkrQJ8KxASLO_-w.png)
_Notre gamme d'ombres, de subtile à éloignée._

#### Échelle de typographie

Afin de créer une hiérarchie visuelle appropriée sur chaque écran, nous devrons définir un certain nombre de tailles de police différentes.

Tout comme avec les notes dans une pièce de musique, notre typographie devrait adhérer à une échelle. Cela aide à maintenir un rythme vertical fluide. Cela peut sembler un peu intimidant au début, mais heureusement, des personnes très intelligentes ont déjà tout compris pour nous au fil des ans. [Tim Brown a construit un excellent site web](http://www.modularscale.com/?1&em&1.25&web&text) pour afficher diverses échelles de typographie. [Adam Morse](https://twitter.com/mrmrs_) a open-sourcé son implémentation de l'[échelle de typographie diatonique](http://ty-p.cc/). Je trouve généralement que l'échelle "Tierce Majeure" fonctionne bien pour la plupart des produits web.

L'étape suivante consiste à décider approximativement des tailles de police dont nous aurons besoin, puis à les tracer sur notre échelle de typographie "Tierce Majeure".

* Par défaut (1em) pour le texte standard qui apparaîtra dans de nombreux endroits de notre site marketing, interface utilisateur, etc. 16px est la taille de police par défaut du navigateur, alors utilisons cela.
* Une taille légèrement plus grande pour le texte principal dans un blog, par exemple.
* Quelques tailles plus grandes pour les titres et sous-titres.
* Une taille très grande pour les titres de section.
* Une taille ridiculement grande, peut-être pour les prix sur une page de tarification, par exemple.
* Nous aurons également besoin de quelques tailles plus petites pour le texte secondaire, les indices de saisie et autres textes secondaires.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UpNXlLvdk20mEUUrd88PbA.png)
_Échelle de typographie_

#### Rayons de bordure

Maintenant, il s'agit simplement d'appliquer le même processus à chaque propriété de style qui accepte des valeurs personnalisées. Pour arrondir les coins, nous aurons besoin des valeurs de rayon de coin suivantes :

* Petit rayon de bordure pour les petits composants comme les cases à cocher, les étiquettes et les labels.
* Rayon de bordure moyen pour les boutons, les entrées et les composants similaires.
* Grand rayon de bordure pour les cartes, les modales et autres grands composants.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hmPSwH9ZMAAi4DLs1PSZNg.png)
_Rayons de bordure de 2px, 4px et 8px_

_Note : Nous aurons également besoin d'un rayon de bordure de 50% pour construire des composants circulaires comme les avatars, etc._

#### Échelle d'espacement

La propriété de style la plus couramment utilisée dans presque tous les designs est l'espace blanc. Que nous espacions des liens dans un en-tête, des éléments dans une grille, que nous ajoutions une distance entre un avatar et un lien ou que nous remplissions un composant de menu déroulant, aucun espace blanc dans notre produit ne devrait être arbitraire ou involontaire.

Comme pour la typographie, en adhérant à une échelle d'espacement, nous pouvons nous assurer que chacun de nos composants et mises en page sera uniforme. Mon échelle d'espacement préférée est la [grille 8dp de Material Design](https://material.io/guidelines/layout/metrics-keylines.html#metrics-keylines-baseline-grids). Elliot Dahl a écrit un [excellent article sur le système de grille 8pt](https://medium.com/built-to-adapt/intro-to-the-8-point-grid-system-d2573cde8632#.8unqq6lz0) et ses avantages.

En restant sur des incréments de 8dp, nous pouvons tracer un certain nombre de valeurs d'espacement que nous pouvons utiliser pour concevoir chaque composant et mise en page de notre suite de produits.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_bbeOmM0hC5or93Z3XoXJw.png)

Nous pouvons également utiliser ces valeurs d'espacement pour définir un ensemble de largeurs, hauteurs et hauteurs de ligne que nous pouvons réutiliser pour dimensionner les boutons, les entrées de formulaire, les avatars et autres composants similaires. Comme ces composants apparaissent souvent côte à côte dans les produits web, il est utile qu'ils suivent la même échelle de dimensionnement pour éviter toute divergence indésirable.

#### Espacement des lettres

Comme je l'ai mentionné précédemment, la taille de la police n'est pas la seule propriété de style que nous devons définir pour les composants de texte. L'espacement des lettres est une autre propriété utile que nous pouvons utiliser pour resserrer les grands titres ou permettre aux petits titres de respirer.

3 ou 4 valeurs d'espacement des lettres devraient suffire.

![Image](https://cdn-media-1.freecodecamp.org/images/1*dhN9LL04x4XnWcSdqW3JbA.png)

### Construire une bibliothèque de composants

Maintenant que nous avons défini notre palette de styles globale, nous pouvons prendre ces blocs de construction et commencer à construire une bibliothèque de composants. Pour la plupart, la conception de composants n'est pas un processus créatif, nous mappons simplement des styles prédéfinis aux composants.

À ce stade, nous ne devrions pas avoir besoin d'un seul style qui n'a pas déjà été défini dans notre palette de styles. Le processus créatif a eu lieu lors de la phase de conception de la palette de styles. À partir de ce moment, qu'il s'agisse d'une couleur, d'une taille de police, d'une valeur de marge/remplissage, d'une largeur/hauteur ou autre, chaque style que nous utilisons pour concevoir nos composants et mises en page doit être extrait de notre palette de styles. Presque rien de nouveau ne doit être introduit. Cela peut sembler extrême ou déraisonnable, mais au contraire, je pense que c'est là que beaucoup de gens se trompent.

Dave Rupert a récemment mené ce sondage Twitter demandant où placer le code qui remplace le style d'un composant bouton, si ce bouton est à l'intérieur d'un composant modal, par exemple.

Harry Roberts (consultez son excellent travail) a ensuite [expliqué ses réflexions sur ce sujet](https://csswizardry.com/2017/02/code-smells-in-css-revisited/) dans son propre article. Après cela, Jonathan Snook [a développé avec ses propres réflexions](https://snook.ca/archives/html_and_css/coding-css-for-context). Bien que je sois d'accord avec les conclusions auxquelles Harry et Jonathan sont parvenus, en fin de compte, je pense que tout le débat est simplement inutile.

Il est contradictoire de concevoir un composant avec l'intention de le réutiliser globalement, puis de modifier ce composant dans une seule partie spécifique du produit. Cela va à l'encontre du but de créer une bibliothèque de composants globale en premier lieu. Chaque fois que je vois des styles qui remplacent d'autres styles, c'est généralement soit un cas de bidouillage d'un composant pour le faire entrer dans un espace restreint, soit l'ajout d'une variation d'un composant parce que suffisamment de planification n'a pas été faite lors des étapes de conception précédentes.

Chaque fois que vous remplacez un composant global dans une zone d'un produit, vous érodez également la cohérence de votre système de design. Lorsque vous apportez suffisamment de modifications sporadiques à des composants dispersés dans votre produit, vous n'avez plus un système de design cohérent. Vous avez simplement un système de design avec un désordre incohérent qui traîne.

Prenons quelques composants courants et voyons comment nous pouvons les construire en utilisant uniquement les styles que nous avons définis dans notre palette ci-dessus.

#### Le modeste bouton

Commençons par un simple composant bouton pour illustrer comment il est possible de construire des composants en utilisant uniquement les styles que nous avons prédéfinis dans notre palette de styles.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fXQ4LmK5e42mtHMk-yHaTw.png)

#### Plus de composants

Encore une fois, ces couleurs, tailles de police, ombres et valeurs de remplissage sont toutes extraites directement de la palette de styles que nous avons prédéfinie ci-dessus.

![Image](https://cdn-media-1.freecodecamp.org/images/1*OmZv-7xhxr-30U69Ud9vQw.png)

#### Essayons quelque chose d'un peu plus élégant...

Lorsque nous avons quelques composants conçus et construits, nous pouvons ensuite commencer à combiner plusieurs composants pour créer des composants plus complexes comme ce composant de menu déroulant.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Yq8rgzM84YNtQHhwHc-1Mg.png)

Ce composant de menu déroulant n'utilise pas un seul style en dehors de la palette de styles de base que nous avons définie précédemment. En utilisant cette méthode, nous pouvons concevoir une bibliothèque de composants entière, puis passer à des mises en page plus larges et enfin à des écrans complets.

### Conseils pour la route

* Certains composants nécessiteront des valeurs qui ne sont pas définies dans notre palette de styles, par exemple, la largeur d'une barre latérale. Parfois, ces valeurs seront simplement 1/3 de la largeur de la fenêtre ou quelque chose de similaire. D'autres fois, ces valeurs seront arbitraires et non réutilisables, et c'est parfaitement acceptable. L'important est de réfléchir aux styles qui doivent être réutilisables (la plupart) et à ceux qui ne le doivent pas.
* Laissez les composants faire leur travail. N'essayez pas d'ajouter des marges aux boutons, aux entrées, aux titres ou à d'autres composants. Au niveau du composant, vous ne devez définir que les styles qui apparaissent uniformes dans chaque instance de ce composant. Comme les marges diffèrent d'un cas à l'autre, il est préférable de les appliquer en utilisant un `div` wrapper. Harry Roberts a écrit [un excellent article abordant ce point](https://csswizardry.com/2012/04/the-single-responsibility-principle-applied-to-css/).

_Je travaille sur un kit d'outils CSS complet basé sur le [Framework CSS Bantam](https://github.com/colmtuite/bantam) qui inclura tous les composants présentés dans cet article et bien d'autres. Le projet est pour [Modulz](https://github.com/colmtuite/modulz-ui), un produit sur lequel je travaille, mais si vous êtes intéressé à utiliser ce kit d'interface utilisateur vous-même, faites-le moi savoir sur [Twitter](https://twitter.com/colmtuite). Si j'obtiens suffisamment d'intérêt, je le rendrai open-source._