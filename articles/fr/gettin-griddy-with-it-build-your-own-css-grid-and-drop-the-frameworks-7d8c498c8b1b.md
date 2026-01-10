---
title: 'Devenez Griddy : créez votre propre CSS Grid et abandonnez les frameworks'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-13T16:20:00.000Z'
originalURL: https://freecodecamp.org/news/gettin-griddy-with-it-build-your-own-css-grid-and-drop-the-frameworks-7d8c498c8b1b
coverImage: https://cdn-media-1.freecodecamp.org/images/0*eiBWP1WwXipGhTyt
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Devenez Griddy : créez votre propre CSS Grid et abandonnez les frameworks'
seo_desc: 'By Theran Brigowatz

  Just about every front end developer’s journey starts with the basic HTML, CSS,
  JavaScript path. You start with the structure, make it look decent, and then make
  it do something. However, somewhere along the journey it is easy to ...'
---

Par Theran Brigowatz

Le parcours de presque tous les développeurs front-end commence par le chemin classique HTML, CSS, JavaScript. Vous commencez par la structure, vous la rendez présentable, puis vous la faites fonctionner. Cependant, à un moment donné du parcours, il est facile de se laisser emporter par le monde des frameworks CSS et de négliger certains détails plus fins.

Bootstrap arrive avec sa belle grille, utilisant seulement quelques classes et un CDN pour créer cette belle grille responsive mobile. Et avant de vous en rendre compte, vous commencez à utiliser ce framework chaque fois que vous construisez un projet nécessitant une mise en page en grille. J'ai souvent fait de même, jusqu'à ce que je commence à "Devenez Griddy".

Ce qui m'a poussé à apprendre CSS Grid, c'est lorsque j'ai essayé de construire un site en utilisant Semantic UI React (le Bootstrap plus joli et moins vague). Cependant, en construisant une grille, je n'arrivais pas à faire en sorte que deux colonnes soient alignées, et j'ai fini par bidouiller chaque règle de marge et de remplissage sous le soleil, pour remplacer les styles intégrés par le framework. C'était une expérience frustrante, et j'ai passé plus de temps à bidouiller les règles de spécificité qu'à coder réellement.

C'est là que CSS Grid intervient. CSS Grid est une addition relativement nouvelle à CSS3 et c'est une vraie révolution. Le fait de devoir importer un framework de grille entraîne quelques problèmes :

1. Augmentation de la taille des fichiers. Plus vous importez, plus votre application devient volumineuse. À une époque où la vitesse est cruciale, réduire la taille des fichiers de votre application est une idée incroyablement importante à considérer. Au lieu d'importer un framework ou de dépendre d'un CDN lent, vous pouvez construire le vôtre.
2. Code moins lisible. Ceux d'entre vous qui ont utilisé un framework connaissent les noms de classes de plus en plus complexes et vagues qui l'accompagnent. Qui ne reconnaît pas immédiatement ce que signifie `class="col-6 col-md-4 col-sm-12"` ? Ou qui veut finir par écrire `div.ui.segment.inverted.stackable.desktop.twelve.mobile.sixteen` dans leur CSS ?
3. Moins de personnalisation. Les règles intégrées d'un framework peuvent être difficiles à remplacer. Vous pouvez vous retrouver avec des noms de classes longs pour atteindre la spécificité correcte, ou avec ligne après ligne de balises `!important` pour créer des styles personnalisés qui remplacent le framework. La magie de CSS Grid est que vous pouvez créer le vôtre et le personnaliser selon vos besoins, plutôt que de dépendre des autres qui n'avaient pas les spécificités de votre projet en tête.

### Une grille CSS responsive

CSS Grid est essentiellement un groupe de boîtes que vous pouvez ajuster sur une page. Vous pouvez soit utiliser des unités numériques pour dimensionner les boîtes, soit des tailles relatives pour les rendre plus responsives. Avec la grande variété de tailles d'écran disponibles, c'est un gros avantage. Supposons que vous souhaitiez créer une mise en page de six divs et que vous souhaitiez qu'elles soient responsives avec plus de colonnes pour différentes tailles d'écran.

Voici à quoi cela ressemble non formaté en six `divs` dans un conteneur.

![Image](https://cdn-media-1.freecodecamp.org/images/DjbMhsgv0bLBOMKYTqzYsLOAUi2xoZKePzf8)

![Image](https://cdn-media-1.freecodecamp.org/images/3zIoUr8D1cjCq39HtdLnfOSRiGxiULXn0DJb)
_Six divs dans un conteneur._

Plutôt que d'avoir à ajouter des classes pour chacun des points de rupture, vous pouvez définir la taille minimale de la div dans une grille, puis remplir automatiquement avec des boîtes responsives plus grandes en utilisant la propriété de dimensionnement `fr`. Vous n'avez qu'à ajouter les propriétés CSS Grid pour le parent, et les divs `small-box` se rempliront automatiquement.

Le CSS pour le conteneur est le suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/BhiUe-6GiAp3ze3eZ5v-d7RK8ATrqf4wBHnB)
_Conteneur parent CSS Grid — "minmax" n'a pas été reconnu par le correcteur orthographique de VSCode._

![Image](https://cdn-media-1.freecodecamp.org/images/3etKQF8JnwlnGQAXTlEoEufSLhxwEqSU1vrC)

![Image](https://cdn-media-1.freecodecamp.org/images/7DTqf10e2NnRG-s3eFBzYbrZOt0xJED18Shy)

![Image](https://cdn-media-1.freecodecamp.org/images/rWW-JnLhCipav9LPmjawLnrgsfatKjWQdf9j)
_Vues Mobile, Tablette et Desktop des divs CSS Grid._

Comme vous pouvez le voir, vous pouvez créer une grille responsive simple à partir de seulement quatre lignes de code. Cela ne pourrait pas être plus facile, et tout votre contenu est libre de se déplacer et de se réorganiser selon les besoins. Aucune requête média n'est même nécessaire dans ce cas. À partir de là, vous êtes libre de personnaliser les boîtes individuelles dans la Grille. C'est assez flexible pour les mises en page et les tailles responsives. Jouez avec et regardez les boîtes bouger magiquement.

### Zones de grille

L'autre raison pour laquelle j'avais tendance à utiliser une grille de framework était pour diverses mises en page sur différents appareils. Vous pouvez vouloir que les composants se déplacent, selon la taille de l'écran sur lequel vous vous trouvez.

Ci-dessous un exemple de mises en page de site que vous pourriez vouloir sur desktop et tablette. Changer cela est assez simple. Bien que certains n'aiment pas la structure, vous pouvez utiliser une structure de modélisation de type ASCII pour les zones de grille.

Supposons que vous avez une mise en page de page de base qui a un en-tête, des barres latérales, du contenu et un pied de page.

![Image](https://cdn-media-1.freecodecamp.org/images/lgLOqVzZS2VpkW6FzlBB60dmgXA2Ez6HIiQV)
_HTML de base pour la mise en page._

![Image](https://cdn-media-1.freecodecamp.org/images/Xn6wpPpy1PL5MxPpwDvLDsBk69oJoLy7n0jN)
_Grille non formatée avec trois colonnes comme — grid-template-columns: 1fr 4fr 1fr;_

La mise en page de la page sans être formatée ressemblerait à ceci avec une grille de base de trois colonnes définie sur `1fr 4fr 1fr`. Les boîtes se rempliront pour s'adapter à leur espace alloué dans la grille. Cependant, si vous voulez que votre mise en page de page soit plus fluide et dynamique comme ci-dessous, vous pouvez utiliser `template-areas`.

Pour obtenir cette mise en page souhaitée, vous devez créer des zones de modèle. Vous pouvez y penser comme une miniature de carte ASCII qui montre où vous voulez que les boîtes aillent sur une page.

Pour obtenir la mise en page de bureau, vous créez votre miniature de carte comme dans la propriété `grid-template-areas`. Chaque ligne contient une rangée et des noms pour les colonnes correspondantes de la mise en page. Vous pouvez voir que les sections d'en-tête et de pied de page s'étireront le long de l'ensemble des colonnes dans lesquelles elles sont placées. De plus, les barres latérales et le contenu s'étirent sur plusieurs rangées, comme vous pouvez le voir dans la zone "carte". Cela peut ensuite être transformé en toute mise en page dont vous avez besoin en ajoutant la propriété `grid-area` aux divs correspondantes comme sur l'image de droite. Vous pouvez nommer celles-ci n'importe quoi qui correspond à votre projet.

![Image](https://cdn-media-1.freecodecamp.org/images/IjAXzbXj88zIYrfyvrjY9lURmWMB-m7fnwuT)

![Image](https://cdn-media-1.freecodecamp.org/images/DVqCoZNJm4dF4IgWzjwc4Mmj26lKlA9FuF0q)

![Image](https://cdn-media-1.freecodecamp.org/images/v-qoZETvOijuF5Mvuu4-j4sbH5I1g6WVsASG)

Pour la faire fonctionner en vue tablette, vous devez simplement créer une requête média et changer l'ordre dans vos zones de modèle. Déplacez facilement le contenu pour la vue souhaitée. (Notez que cela peut poser des problèmes sur les lecteurs d'écran si vous avez du contenu dans le désordre, assurez-vous donc que votre contenu reste logique à la lecture.)

![Image](https://cdn-media-1.freecodecamp.org/images/eUPzziMV3sAMT0NTGWA9eSYvAwApKphT-8Tn)

![Image](https://cdn-media-1.freecodecamp.org/images/V8CMYybJsi7tPQ6w814W6chvauwsljz4a0pl)
_Vues Desktop et Tablette_

### Conclusion

Cet article simple ne fait définitivement qu'effleurer la surface de ce que vous pouvez faire avec CSS Grid. Mais je pense que la principale chose à retenir est que vous ne devriez pas avoir peur d'utiliser CSS Grid. C'est vraiment assez simple, puissant et léger une fois que vous vous habituez à la nouvelle syntaxe. Allez-y et profitez de "Devenez Griddy".

Pour plus d'informations sur CSS Grid, je vous recommande vivement de consulter [http://cssgrid.io](http://cssgrid.io) enseigné par Wes Bos. C'est un tutoriel fantastique sur CSS Grid.

Aussi, au fur et à mesure que vous avez des questions, n'oubliez pas de consulter le site CSS Tricks à l'adresse [https://css-tricks.com/snippets/css/complete-guide-grid/](https://css-tricks.com/snippets/css/complete-guide-grid/) pour en savoir plus sur la grille.

Pour découvrir plus de mon travail, visitez [https://theran.co](https://theran.co) et en savoir plus sur moi.