---
title: Vous n'avez besoin de connaître que ces propriétés pour commencer à aimer CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-24T17:06:22.000Z'
originalURL: https://freecodecamp.org/news/you-just-need-to-know-these-properties-to-start-loving-css-a06aca6087e9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*OtuC8-aWUupuh70uJ4r-SQ.jpeg
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: 'tech '
  slug: tech
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Vous n'avez besoin de connaître que ces propriétés pour commencer à aimer
  CSS
seo_desc: 'By Henry Tabima Giraldo

  Positioning things with HTML and CSS can be a real headache when you’re new in frontend
  development. But in this post, I’m going to teach you how to solve most of the positioning
  problems. You only have to know these 3 CSS pro...'
---

Par Henry Tabima Giraldo

Positionner des éléments avec HTML et CSS peut être un vrai casse-tête lorsque vous débutez en développement frontend. Mais dans cet article, je vais vous apprendre à résoudre la plupart des problèmes de positionnement. Vous n'avez besoin de connaître que ces 3 propriétés CSS.

Je suis un développeur avec plus de 3 ans d'expérience en frontend. Lorsque j'apprenais, je pensais comme vous pensez maintenant. Ensuite, j'ai découvert flexbox, et le positionnement est devenu plus facile que jamais.

L'une des meilleures ressources pour apprendre flexbox est le [guide CSS Tricks](https://css-tricks.com/snippets/css/a-guide-to-flexbox/). Après une utilisation continue de cette fonctionnalité, j'ai réalisé que, dans la plupart des cas, vous n'avez besoin que de ces trois propriétés :

> display: flex;

> justify-content: $value;

> align-items: $value;

Je vais emprunter quelques images du [guide mentionné ci-dessus](https://css-tricks.com/snippets/css/a-guide-to-flexbox/). De cette façon, je peux m'assurer qu'il est plus facile pour vous de comprendre comment les propriétés fonctionnent. Très bien, commençons.

#### Contexte

Tout d'abord, nous devons établir un contexte de travail. Lorsque nous travaillons avec flexbox, nous avons deux types d'éléments, le **conteneur** et les **éléments à l'intérieur de ce conteneur**, comme vous pouvez le voir dans les images ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1*uxhqPMGpDo6Z70taQXs1yQ.png)
_Image du guide flexbox CSS Tricks_

Maintenant que vous pouvez différencier le conteneur et ses éléments, clarifions une chose : les trois propriétés que nous allons apprendre ici **appartiennent au conteneur**. Une erreur courante que font les gens lorsqu'ils commencent avec flexbox est de définir les propriétés suivantes pour leurs éléments enfants.

#### display: flex

Très bien, la première chose que nous devons faire est de définir la propriété `display` du conteneur sur `flex`.

Avec cette propriété, vous disposez les éléments enfants directs du conteneur en ligne (comme dans les images ci-dessus).

#### justify-content

Cette propriété définit l'alignement des éléments le long de l'axe principal (axe horizontal). Nous pouvons voir les valeurs possibles et leurs résultats dans l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1*h1TPlhNbzNnAYmkpLyD-qw.png)
_Image du guide flexbox CSS Tricks_

#### align-items

La troisième propriété est **align-items**. Cette propriété définit le comportement par défaut pour les éléments le long de l'axe transversal (axe vertical). Maintenant, voyons toutes les valeurs possibles de cette propriété et comment elles affectent les éléments à l'intérieur du conteneur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*23_VYI-DBKGKA04Kjb3EHQ.png)
_Image du guide flexbox CSS Tricks_

Avec les propriétés précédentes, nous avons pu commencer à positionner les éléments exactement où nous le voulons. Mais cet article ne serait pas complet sans des exemples. Pour cette raison, je vais vous montrer quelques cas d'utilisation courants.

> Note : Il existe une propriété appelée flex-direction qui échange la direction de l'axe principal et de l'axe transversal. Soyez prudent lorsque vous utilisez cette propriété et assurez-vous de savoir ce que vous faites.

#### Cas d'utilisation

Pour le premier cas d'utilisation, nous allons voir une barre de navigation d'en-tête simplifiée. Les en-têtes ont généralement un élément à gauche, un autre à droite et parfois un ou plusieurs au milieu.

Dans cet exemple Codepen, concentrez-vous uniquement sur le CSS à l'intérieur du sélecteur appelé `.container`. Tous les autres styles sont pour donner une bonne apparence. Vous devriez essayer de supprimer l'élément du milieu et voir ce qui se passe.

Pour le deuxième cas d'utilisation, généralement, vous voudrez centrer un élément à l'intérieur de son conteneur. Maintenant, voyons comment nous pouvons accomplir cela.

Encore une fois, vérifiez le sélecteur appelé `.container` et jouez avec les différentes valeurs de ces propriétés et voyez ce qui se passe.

#### Enfin

Facile, non ? Jouez avec ces propriétés et voyez comment elles affectent les éléments, habituez-vous à elles, et vous n'aurez plus de problèmes en travaillant avec le positionnement.

Maintenant que vous avez vu comment utiliser flexbox de la manière la plus basique et utile, je veux vous encourager à en apprendre davantage sur cette fonctionnalité. Vous pouvez lire le [guide CSS Tricks](https://css-tricks.com/snippets/css/a-guide-to-flexbox/), et jouer avec [Flexbox Frogs](https://flexboxfroggy.com) ou [Flexbox Zombies](https://mastery.games/p/flexbox-zombies). Ces deux dernières options peuvent être un moyen divertissant de vous apprendre les tenants et aboutissants de flexbox.

J'espère que cet article vous aide dans votre parcours. Et j'adorerais avoir de vos nouvelles ; si vous voulez me contacter, assurez-vous de me suivre sur [Twitter en tant que @HenryTabimaG](https://twitter.com/HenryTabimaG) et sur [GitHub en tant que @HenryTabima](https://github.com/HenryTabima). Si vous voulez un contenu spécifique pour un article, n'hésitez pas à demander.

N'oubliez pas, si vous avez aimé cet article, laissez quelques "applaudissements".

![Image](https://cdn-media-1.freecodecamp.org/images/1*fLar7VaMRxHzGdB3jYovVw.png)