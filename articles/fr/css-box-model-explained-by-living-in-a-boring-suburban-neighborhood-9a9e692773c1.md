---
title: Le Modèle de Boîte CSS Expliqué en Vivant dans un Quartier Suburbain Ennuyeux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-27T05:12:16.000Z'
originalURL: https://freecodecamp.org/news/css-box-model-explained-by-living-in-a-boring-suburban-neighborhood-9a9e692773c1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*HUxt-BY7c8cKk-w7_c_uzw.jpeg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: technology
  slug: technology
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Le Modèle de Boîte CSS Expliqué en Vivant dans un Quartier Suburbain Ennuyeux
seo_desc: 'By Kevin Kononenko

  If you’ve been to a normal suburban neighborhood, then you can understand the CSS
  Box Model.

  An experienced front-end web developer will tell you that an HTML layout is really
  just a series of boxes. These boxes stack on top of eac...'
---

Par Kevin Kononenko

#### Si vous avez déjà été dans un quartier suburbain normal, alors vous pouvez comprendre le Modèle de Boîte CSS.

Un développeur web front-end expérimenté vous dira qu'une mise en page HTML n'est vraiment qu'une série de boîtes. Ces boîtes s'empilent les unes sur les autres dans leurs boîtes conteneurs, et ces boîtes conteneurs s'empilent les unes sur les autres dans une boîte conteneur encore plus grande, et ainsi de suite...

WOW. C'est beaucoup de boîtes dans des boîtes. Je ne pense pas vouloir entendre le mot « boîte » pendant au moins une semaine. De plus, le concept de boîte ne fait pas un bon travail pour décrire les marges et le remplissage. Ce sont les deux outils les plus importants pour créer des éléments uniformément espacés.

En réalité, il y a un peu plus de nuances lorsqu'il s'agit d'organiser les éléments HTML. Le Modèle de Boîte CSS (oh là là !) nous permet de créer un contenu bien équilibré et facilement lisible sur notre page.

Les différentes parties du modèle de boîte sont un peu comme une propriété dans un lotissement suburbain typique. Et si vous pouvez les utiliser correctement, vous pouvez éviter des heures d'essais et d'erreurs avec un CSS capricieux.

Si vous cherchez une explication plus technique, le MDN en a une [plutôt bonne](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Box_Model/Introduction_to_the_CSS_box_model).

#### Les Principales Parties du Modèle de Boîte

Il y a 5 propriétés importantes qui vous permettent de dimensionner et de distribuer vos éléments HTML :

* Largeur
* Hauteur
* Remplissage (Padding)
* Bordure
* Marge

Voici à quoi cela ressemble dans un diagramme :

![Image](https://cdn-media-1.freecodecamp.org/images/1*t_3KFsT6HYd1Er9pEsv_1A.png)

Aïe ! C'est beaucoup trop de boîtes pour un seul élément. Reprenons cela étape par étape. Il y a en fait trois zones différentes ici.

**Zone 1 :** La hauteur et la largeur de l'élément réel. C'est la maison elle-même. Dans le diagramme, cela fait 679 pixels par 63 pixels.

**Zone 2 :** Le territoire autour de l'élément qui est limité par la bordure. C'est un peu comme la cour et la clôture de votre propriété. C'est le **remplissage** et la **bordure**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*LnzBO4qp7vUuemk3wAu50g.png)

**Zone 3 :** L'espace vide qui sépare cet élément des éléments environnants. C'est similaire aux arbres qui font encore techniquement partie de votre propriété, mais qui vous donnent un peu d'intimité vis-à-vis des voisins et sont simplement destinés à vous donner une zone tampon. C'est la **marge**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*T9PFj7v8hFovBOR2qW0JYg.png)

Rappelez-vous que chaque div, paragraphe et en-tête a ces propriétés. Cela peut devenir confus assez rapidement lorsque vous avez une série d'éléments empilés les uns sur les autres, et que vous ne savez pas quels éléments contiennent l'espace tampon.

La différence entre la marge et le remplissage est peut-être **la partie la plus difficile**. Les deux sont utilisés pour des raisons différentes. Comme vous pouvez le voir avec l'herbe verte, le remplissage aura toujours une couleur de fond, si vous choisissez de la définir. C'est aussi la propriété que vous voulez changer si vous voulez modifier la distance entre la **bordure** et le **contenu**.

Supposons que vous vouliez avoir une grande cour sur le côté droit de la maison, ce qui éloignerait la bordure droite. Vous pourriez changer cela avec la propriété **padding-right**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ftk23jdL-2RleJunow_l2w.png)

La propriété **margin** affecte l'espace entre les éléments. C'est cet espace vide qui est une sorte de « no man's land » où aucun développement n'a lieu. Il est strictement destiné à espacer les éléments. Voici quelques maisons en rangée, certaines ayant des marges plus grandes ou plus petites.

![Image](https://cdn-media-1.freecodecamp.org/images/1*YTc5r6C7lPX7NnhF8mFyJQ.png)

NOTE : Chacune de ces maisons empilées doit avoir un affichage avec une valeur de « inline-block ». Empêche [l'effondrement des marges](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Box_Model/Mastering_margin_collapsing).

#### Quelques Exemples Concrets

D'accord, utilisons un peu de vrai CSS ! Imaginez que vous avez un lot avec les attributs suivants :

Voici à quoi cela ressemblerait :

![Image](https://cdn-media-1.freecodecamp.org/images/1*D-OE3BPohmmwIBVbZQpI7A.png)

Quelques observations :

1. Remarquez comment la couleur de fond n'affecte que les pixels à l'intérieur de la bordure. Les marges ne sont pas affectées par cette propriété.
2. Lorsque vous déclarez la marge et le remplissage avec une seule valeur, comme 4px, CSS applique automatiquement le nombre en haut, en bas, à gauche et à droite de l'élément.

Voici un dernier exemple. Dans celui-ci, nous utiliserons deux valeurs lors de la déclaration du remplissage et de la marge. La première valeur détermine le haut/bas, et la deuxième valeur détermine la gauche/droite.

Et voici le diagramme :

![Image](https://cdn-media-1.freecodecamp.org/images/1*7iDlw63sVwefTQqMzNzQSg.png)

Si vous avez aimé cet article, vous pourriez également aimer mes [autres explications](https://www.rtfmanual.io/guides/) de sujets CSS, JavaScript et SQL difficiles, tels que le positionnement, le Modèle-Vue-Contrôleur et les callbacks.

Et si vous pensez que cela pourrait aider d'autres personnes dans la même situation que vous, donnez-lui un « cœur » !