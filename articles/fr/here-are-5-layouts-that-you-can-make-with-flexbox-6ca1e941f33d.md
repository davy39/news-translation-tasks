---
title: Voici 5 dispositions que vous pouvez créer avec FlexBox
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-04T21:20:15.000Z'
originalURL: https://freecodecamp.org/news/here-are-5-layouts-that-you-can-make-with-flexbox-6ca1e941f33d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*V54N2Latawo69ZaS7hqJQw.jpeg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Voici 5 dispositions que vous pouvez créer avec FlexBox
seo_desc: 'By Jennifer Bland

  The CSS Flexible Box Layout — Flexbox — provides a simple solution to the design
  and layout problems designers and developers have faced with CSS. Let me show you
  how to use it to generate some common layouts and challenges that you...'
---

Par Jennifer Bland

La disposition CSS Flexible Box Layout — Flexbox — fournit une solution simple aux problèmes de conception et de mise en page auxquels les concepteurs et les développeurs ont été confrontés avec CSS. Laissez-moi vous montrer comment l'utiliser pour générer des dispositions courantes et relever les défis auxquels vous serez confrontés dans la conception d'un design de site web réactif.

Je suppose que vous connaissez déjà les bases de Flexbox. Si ce n'est pas le cas, il existe de nombreux documents qui vous enseignent Flexbox. Je recommanderais [Comprendre Flexbox : Tout ce que vous devez savoir](https://medium.freecodecamp.org/understanding-flexbox-everything-you-need-to-know-b4013d4dc9af).

### **Voici ce que nous allons créer**

Dans cet article, je vais vous montrer comment créer 7 dispositions différentes en utilisant FlexBox.

1. Navigation
2. Centrer une image sur l'écran
3. Disposition de site web réactive
4. AddOn pour les champs de saisie
5. Disposition à 3 colonnes

### Obtenez le code

Tous les exemples que je vais montrer peuvent être [téléchargés depuis mon compte GitHub](https://github.com/ratracegrad/made-with-flexbox). Le code pour chaque exemple est simplement en html et css. J'ai créé une page d'accueil principale qui fournit un lien vers chaque exemple que nous allons couvrir.

![Image](https://cdn-media-1.freecodecamp.org/images/1*sZPnR9WDlMBBSJCViFbdJw.png)

### Navigation

Chaque site web a une navigation. En utilisant Flexbox, vous pouvez créer une navigation qui a le nom de votre entreprise à gauche et les éléments de menu à droite.

![Image](https://cdn-media-1.freecodecamp.org/images/1*o_I7a9CVkOmJNIgQeaLVhg.png)

Pour réaliser cette disposition en CSS, vous devriez utiliser des flottants pour faire apparaître certains contenus à gauche et le reste du contenu à droite.

Avec FlexBox, vous devez spécifier un conteneur flexible qui contient la navigation. Le nom de l'entreprise à gauche est un élément flexible dans ce conteneur.

Les éléments de menu à droite sont leur propre conteneur flexible avec une balise <ul> contenant tous les éléments de menu.

Voici le html pour la navigation :

Voici le CSS pour la navigation :

### Centrer une image sur l'écran

De nombreux sites web incluent une image en pleine taille. Habituellement, cette image contient du texte qui est centré sur l'écran.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jtv2bxTy4-k9e2U1e49OhA.png)

Le défi est de styliser l'image afin qu'elle s'adapte à la page complète, que vous la visualisiez sur un moniteur large, un ordinateur portable, une tablette ou un téléphone, et que le CSS reste centré sur l'écran. Flexbox facilite cela. Pour imiter le texte centré sur l'écran, j'ai inclus un bouton.

Voici le html pour centrer une image sur l'écran :

Voici le css pour centrer une image sur l'écran :

### Disposition de site web réactive

Presque tous les sites web ont la même disposition qui contient une navigation en haut et un pied de page en bas. Entre les deux, il y a 3 colonnes composées d'une barre latérale droite et gauche et de la zone de contenu principale. Généralement, la zone de contenu principale occupe 60 % de la largeur de l'écran et les deux barres latérales se voient attribuer 20 % de l'écran chacune.

![Image](https://cdn-media-1.freecodecamp.org/images/1*uxPAuHEcsoHORMpwH57_Lg.png)

Le défi pour créer un site web réactif est de faire en sorte que le pied de page reste en bas de la page, quel que soit le contenu affiché. La zone de contenu doit défiler s'il y a plus de contenu que ce qui peut être affiché sur la page.

Voici le html pour la disposition de site web réactive :

Voici le code css pour la disposition de site web réactive :

### AddOn pour les champs de saisie

Pour améliorer l'expérience utilisateur, de nombreux concepteurs préfèrent mettre des images ou du texte dans leurs champs de saisie. Cela fournit à l'utilisateur des directives sur ce qui doit être inclus dans le champ.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-pcENc5u6jl3ajF90EMiew.png)

Avec le CSS traditionnel, c'était très difficile et nécessitait l'utilisation d'un format de tableau pour insérer quelque chose avant ou après un champ de saisie. Avec Flexbox, c'est beaucoup plus facile.

Voici le code html pour l'addon des champs de saisie :

Voici le code css pour l'addon des champs de saisie :

### Disposition à 3 colonnes

Il est très courant pour les sites web d'inclure une disposition à 3 colonnes sur l'écran.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vDAqFQfCkc6KBXErK7TG9g.png)

Voici le html pour une disposition à 3 colonnes :

Voici le css pour la disposition à 3 colonnes :

### Plus d'articles

Merci d'avoir lu mon article. Si vous l'aimez, veuillez cliquer sur l'icône d'applaudissements ci-dessous afin que d'autres puissent trouver l'article. Voici quelques-uns de mes autres articles qui pourraient vous intéresser :

[Pensez hors de la boîte avec la propriété CSS shape-outside](https://medium.com/@ratracegrad/mastering-css-series-shape-outside-44d626270b25)
[7 choses que j'ai apprises dans mon parcours de bootcamp de codage à développeur senior](https://codeburst.io/7-things-i-learned-in-my-journey-from-coding-bootcamp-to-senior-developer-645ab7c2fea0)
[Pourquoi la culture d'entreprise est importante pour votre carrière en tant qu'ingénieur logiciel](https://medium.freecodecamp.org/why-company-culture-is-important-to-your-career-as-a-software-engineer-5a590bc44621)