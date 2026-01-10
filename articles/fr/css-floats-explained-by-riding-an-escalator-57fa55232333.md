---
title: Les Floats CSS Expliqués en Montant un Escalier Mécanique
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-09-20T06:32:08.000Z'
originalURL: https://freecodecamp.org/news/css-floats-explained-by-riding-an-escalator-57fa55232333
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Ah5h2jCdtSGkLsEXp8IBnw.jpeg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: Life lessons
  slug: life-lessons
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Les Floats CSS Expliqués en Montant un Escalier Mécanique
seo_desc: 'By Kevin Kononenko

  If you have ever jumped on an escalator, then you can quickly understand floats.

  Your  is almost perfect. You decide to introduce some floats to fix the relationship
  between a few elements.

  The next thing you know, your newly float...'
---

Par Kevin Kononenko

#### Si vous avez déjà sauté sur un escalier mécanique, alors vous pouvez rapidement comprendre les floats.

Votre <div> est presque parfait. Vous décidez d'introduire quelques floats pour fixer la relation entre quelques éléments.

La prochaine chose que vous savez, vos éléments nouvellement flottés sortent de l'ordre soigneusement choisi, et collent au côté de votre div comme un aimant. La phrase « comportement non intentionnel » vient à l'esprit.

J'ai personnellement passé des heures à essayer de comprendre pleinement les floats. Je lisais un article et disais, « Oh, cela a du sens ! » Puis je retournais à mon code, je l'essayais et... j'échouais. Retour à la case départ.

Je vais faire de mon mieux pour vous épargner ce sort.

Les floats créent des **flux alternatifs**. C'est la partie la plus difficile à comprendre. Et une fois que vous les introduisez, vous devez ensuite écrire votre code pour qu'il tienne compte de jusqu'à trois flux : normal, gauche et droite. C'est un tout nouvel ensemble de règles, par opposition à la manipulation de la largeur des éléments ou de leur positionnement.

En fait, les floats sont assez similaires à la dynamique de monter un escalier mécanique, et je vais montrer comment ils peuvent être utilisés avec la propriété **clear** pour créer des relations cristallines dans les divs. Ainsi, la prochaine fois que vous essayez d'utiliser des floats dans votre code, vous ne rencontrerez aucune surprise.

### Il faut respecter la voie de dépassement

![Image](https://cdn-media-1.freecodecamp.org/images/1*jdZ50msxxEJXyMfJWR_xvg.jpeg)

Le flux par défaut des éléments est un peu comme l'image ci-dessus. Un homme se tient au milieu avec la main sur la rampe. Il accapare tout l'escalier mécanique. Personne ne peut le dépasser. Une assez mauvaise étiquette d'escalier mécanique, vraiment.

Il se tient derrière un groupe d'autres personnes qui font la même chose, donc personne ne peut les dépasser non plus. Il n'y a pas de concept de voies ou de décence humaine de base.

C'est le scénario lorsque vous n'utilisez pas du tout de floats.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pocm7FjZE_c--G2mLffYtQ.jpeg)

Très bien, maintenant nous parlons ! Des gens montrent un certain niveau de conscience. J'aime voir cela.

Nous avons une voie formée à gauche, et une autre voie formée à droite. D'autres personnes peuvent facilement se déplacer autour des deux personnes qui sont immobiles et monter l'escalier mécanique plus rapidement, si elles le souhaitent. Personne ne bloque le flux en se tenant au milieu.

C'est le scénario lorsque vous utilisez des floats dans votre div. Il y a un flux gauche et un flux droit, et les éléments qui ne sont pas flottés peuvent facilement remplir l'espace qui n'est pas pris par les éléments flottés.

### Floats : Gauche et Droite

L'utilisation de floats peut introduire jusqu'à deux nouveaux flux : gauche et droite.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HbpY5zZdaazjF0yMk2HqKQ.png)

Et cela permet au flux normal des éléments, ceux sans valeur de float, de remplir les espaces autour de ces éléments.

![Image](https://cdn-media-1.freecodecamp.org/images/1*bEmyvjSK6YW6__hMh7KX6A.png)

Les floats vous permettent de créer ces nouvelles relations entre les flux.

Si vous aviez une ligne de personnes se tenant au milieu de l'ascenseur, vous auriez des options limitées pour de nouvelles structures. Mais lorsque vous avez une colonne gauche et droite, soudainement vous pouvez spécifier que certaines personnes se tiennent à droite, d'autres restent à gauche, et un autre groupe peut remplir les espaces.

Cela vous permet de créer un code plus lisible et compréhensible, car la propriété float donne également une **indication de la relation d'un élément avec les éléments environnants.**

### La Propriété Clear

Il y a une autre subtilité que nous n'avons pas encore discutée : la [propriété clear](https://developer.mozilla.org/en-US/docs/Web/CSS/clear). « Clear » permet aux éléments de spécifier où ils doivent s'aligner par rapport aux éléments flottés.

Dans la première image de la section « Floats », les deux passagers de l'escalier mécanique se tenaient courtoisement de chaque côté de l'escalier. Cela permet aux autres de les dépasser et de se déplacer librement comme ils le souhaitent.

Disons que, au lieu d'avoir un élément flotté à gauche et un élément flotté à droite, nous avions plutôt 3 éléments flottés à gauche et 1 à droite. Les trois éléments flottés à gauche s'empileraient en ligne à gauche si nous leur donnons également la propriété « clear: left ». Mais s'ils s'alignaient horizontalement avec l'élément flotté à droite, cela pourrait rendre très difficile, voire impossible, pour le flux normal des éléments de passer :

![Image](https://cdn-media-1.freecodecamp.org/images/1*8DUo9aDieoVScXu5iade2Q.png)

« Clear: left » indique à chaque personne flottant à gauche qu'elle doit s'aligner derrière le premier élément qui est flotté à gauche. Selon la taille des deux personnes du bas, il pourrait être difficile pour les éléments normaux de se faufiler et d'occuper l'espace en haut à droite. Ainsi, même de bonnes pratiques d'escalier mécanique peuvent encore entraîner des blocages.

L'une des utilisations les plus fréquentes de la propriété clear est « clear:both ». Cela vous permet de réinitialiser le flux des éléments, par opposition à continuer à maintenir un flux droit, gauche et normal. C'est un peu comme ce type sur l'escalier mécanique qui prend tout l'espace parce qu'il a apporté sa valise.

![Image](https://cdn-media-1.freecodecamp.org/images/1*wlb4YUsCAnv2_LIQlTm7sw.png)

Avec « clear:both », peu importe où se tient ce type par rapport à sa valise. Peu importe qui se tient à gauche ou à droite au-dessus de lui. Il bloque toujours tout l'escalier mécanique. Les personnes qui montent après lui devront commencer un nouveau flux d'éléments, qui pourrait inclure l'un des trois flux : gauche, droite ou normal.

Il a échappé au système à trois flux et réinitialisé les règles. Mauvais pour les personnes qui veulent courir sur l'escalier mécanique ? Oui. Mais c'est bien si vous voulez empêcher quelqu'un de passer.

Remarquez comment cela est différent du gentleman au début qui se tenait au milieu de l'escalier mécanique, derrière une ligne de personnes qui faisaient de même. C'était un système à un flux. « Clear: both » reconnaît qu'il peut y avoir jusqu'à trois flux, et bloque le passage de tout élément qui suit.

Si vous avez aimé cet article, vous aimerez peut-être aussi mes [autres explications](https://www.rtfmanual.io/guides/) de sujets CSS et JavaScript difficiles, tels que le positionnement, le Modèle-Vue-Contrôleur et les callbacks.

Et si vous pensez que cela pourrait aider d'autres personnes dans la même situation que vous, donnez-lui un « cœur » !

[_Cet article est initialement paru sur le blog CodeAnalogies_](https://blog.codeanalogies.com/2016/09/20/css-floats-explained-by-riding-an-escalator/).