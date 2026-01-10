---
title: Comment j'ai recréé les micro-interactions de Facebook pour la découverte de
  fonctionnalités
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-18T10:16:28.000Z'
originalURL: https://freecodecamp.org/news/how-facebook-designs-microinteractions-for-feature-discovery-c79cfe998a77
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1Bi1hsnhH7XnNGOyf8yGbw.png
tags:
- name: Front-end Development
  slug: front-end-development
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: UI
  slug: ui
- name: UX
  slug: ux
seo_title: Comment j'ai recréé les micro-interactions de Facebook pour la découverte
  de fonctionnalités
seo_desc: 'By Yonatan Doron

  Demo Orientation — Exampels are in a Vue.js configuration hosted at Codesandbox.io,
  in order to reach the pure HTML/SCSS logic after navigating away click the components
  folder → then click spark.vue file → the HTML is wrapped around...'
---

Par Yonatan Doron

**Orientation de la démo** — Les exemples sont dans une configuration Vue.js hébergée sur Codesandbox.io. Pour accéder à la logique pure HTML/SCSS après avoir navigué, cliquez sur le dossier `components` → puis sur le fichier `spark.vue` → le HTML est enveloppé autour des balises `<template>` → le SCSS est juste un défilement plus bas, enveloppé autour des balises `<style>` et c'est tout → Profitez ! :)

_Pour ceux qui souhaitent aller directement à l'exemple de code, c'est juste [ici](https://codesandbox.io/s/z3x7vl176m)._

_Si vous souhaitez aller directement au défi, cliquez [ici](#4c58)_

**_Une micro-interaction_** _est un signal visuel subtil, à usage unique, qui attire votre attention sur un changement d'état. Une lumière de puissance sur une cafetière, ou un changement de couleur au survol d'un bouton en sont deux exemples._

#### Pourquoi ? Qui ?! Quoi ?! et un peu d'orientation

Un problème UX courant que les designers et les développeurs frontend rencontrent occasionnellement est le **besoin d'introduire une nouvelle fonctionnalité** ou d'exposer une fonctionnalité "bien cachée" qui, pour une raison quelconque, peut-être due à l'encombrement des fonctionnalités, à un mauvais design ou à une autre raison, l'**utilisateur interagit rarement** avec cette zone ou cette fonctionnalité de votre application.

Qu'il s'agisse d'une nouvelle fonctionnalité passionnante que votre entreprise souhaite commencer à utiliser pour obtenir des réactions et des retours des utilisateurs, ou d'une fonctionnalité déjà existante qui est rarement utilisée pour une raison quelconque, ce problème existe et nous le rencontrons de temps en temps dans notre industrie.

Je suis tombé sur cette solution possible exceptionnelle sur l'**application mobile Facebook**. Les designers d'interaction et les développeurs frontend de Facebook ont décidé de supprimer une certaine action de ma barre de navigation dans l'application et d'en mettre une nouvelle — le lien rapide vers mon profil. Qu'ils aient étudié mon comportement spécifiquement ou qu'il s'agisse d'un phénomène plus robuste, c'est définitivement une cause digne d'intérêt à mon avis.

#### Un problème UX de première main — Résolu

Souvent, je me retrouve à chercher le moyen le plus rapide de naviguer vers mon profil via l'application Facebook. Dans la plupart des cas, je déplace mon regard vers quelques zones de l'application, cherchant visuellement ainsi qu'en cliquant sur quelques zones pleines d'anticipation pour atteindre ma destination finale jusqu'à ce que j'atteigne finalement mon profil (cela varie bien sûr en fonction de l'état ou de l'écran de l'application dans lequel vous vous trouvez pendant votre session) — pour conclure, une expérience pas très agréable, pour le moins.

Facebook, et plus spécifiquement les **designers d'interaction** ainsi que les développeurs frontend qui ont ensemble concocté cette solution unique, ont résolu ce problème parfaitement à mon avis.

Le message qu'ils ont essayé de transmettre, comme je le perçois, est qu'il y a quelque chose de **Nouveau, Brillant et Amusant** qui nous a été offert en tant qu'utilisateurs. C'est similaire à un cadeau qui nous signale que le déballage et le déballage de cette nouvelle action nous mèneront à une **expérience agréable et très souhaitée**. De plus, lorsque l'on regarde l'écran statique de l'application mobile Facebook, la seule partie en mouvement est cette merveilleuse micro-interaction brillante et étincelante — un signal clair pour un appel à l'action.

_Plongeons profondément dans la façon dont une micro-interaction puissante et soigneusement conçue, ainsi qu'un fanatique des micro-interactions (comme moi), ont déclenché une quête d'exploration !_

![Image](https://cdn-media-1.freecodecamp.org/images/1*SqTzmKIr3XOnLPl2ngQXsQ.gif)
_Original — Facebook me disant qu'une nouvelle option est maintenant disponible dans ma barre de tâches que j'utilise souvent_

![Image](https://cdn-media-1.freecodecamp.org/images/1*WqepNW9FX8d_0SHRaUJtig.gif)
_Ma version — ou attendez, est-ce l'original ? Je suis un peu confus…_

#### Simple mais puissant et attrayant

Un élément UI apparemment simple — ces 3 étincelles bleutées apparaissant brièvement sur l'icône de l'avatar — suggèrent que cet élément est un cadeau "tout neuf" pour l'utilisateur à découvrir, Ohh l'excitation — Je ne peux pas attendre !

Une retouche apparemment simple, associée à une icône d'avatar minimaliste, fusionnées ensemble dans une micro-interaction élégante, intelligente et simple, résidant dans un écran très statique ou inactif de l'application mobile Facebook. Cela incite immédiatement l'utilisateur observateur à interagir avec cet élément UI et à découvrir ses vertus cachées — un appel à l'action sur mesure, correctement conçu et implémenté.

#### Approche du défi

Une analyse simple de la micro-interaction rend les choses assez claires — trouver une icône similaire ou exacte serait une tâche relativement simple, tandis que la conception d'un effet "étincelle" unique serait la partie la plus complexe.

Je vous invite à monter à bord de mon "train" de pensée et à partager mon expérience dans la formation d'idées, l'expérimentation et la découverte d'insights tout au long de mon chemin pour accomplir le résultat final souhaité.

J'espère également que vous apprendrez quelque chose de nouveau, comme je l'ai fait, en utilisant la propriété CSS `clip-path` pour relever ce défi et en comprendre ses tenants et aboutissants.

Sans plus tarder, commençons :) J'ai fait un pas en avant pour décomposer l'effet en mini-défis plus petits, plus gérables et plus intuitifs.

#### Clip ?! path ?! Élaborer…

`clip-path` est une propriété CSS qui découpe (clip) une région qui définit quelle partie d'un élément sera affichée, tandis que les parties extérieures sont cachées.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8XLc3ld-Y525EXEXM0GVFw.png)
_Un développeur utilisant clip-path pour créer une forme intricate sur son élément HTML_

`clip-path` nous permet de créer des formes complexes avec CSS en découpant un élément dans une certaine forme (comme un cercle, un triangle, une ellipse, un polygone et plus). Nous pouvons également animer librement entre les formes et recevoir des transitions et des effets de morphing facilités, tant que les deux formes transitionnées ont le même nombre de points (coordonnées x,y).

![Image](https://cdn-media-1.freecodecamp.org/images/1*YD4oQHQ2egrRzMmt5RE4Nw.jpeg)
_Moi expérimentant avec clip-path pour créer quelques formes de base_

#### Décomposition des animations

![Image](https://cdn-media-1.freecodecamp.org/images/1*X-LOwkghKd9GkopMQ-87GQ.gif)
_Un seul effet "étincelle" dans la micro-interaction_

En concentrant mon attention sur un seul élément, il est devenu beaucoup plus facile de disséquer chaque animation activée. Ainsi, j'ai déterminé ce qui suit :

1. `transform: scale(...)` — Passe de 0 à 1 et retourne à 0 tout au long du cycle de vie de l'animation.
2. `transform: rotate(180deg)` — Il m'a fallu un peu plus de temps pour réaliser que la rotation de cette étoile ninja en un carré et retour est un total de 180 degrés (de sa phase d'apparition à sa position finale, dans laquelle l'étincelle disparaît également).
3. `clip-path: polygon(...)` — Cette partie serait probablement l'un des défis les plus complexes et intéressants dans ce défi d'effet d'étincelle unique — donc, je vais en discuter plus en détail ci-dessous.

#### Mise à l'échelle — Un bloc de construction de l'effet d'étincelle

Le timing de la mise à l'échelle de l'élément joue un rôle crucial dans la contribution à l'effet "étincelant" de l'effet, car l'apparition et la disparition rapides de l'élément sont pretty much ce qui compose une étincelle — une visite brillante et brève qui procure un plaisir temporaire à nos yeux.

#### Rotation — Estomper les lignes, une "colle" pour l'effet d'étincelle

Avec la transition de mise à l'échelle, lorsque l'élément apparaît pour la première fois et commence immédiatement à tourner de gauche à droite, la rotation le rend plus vivant et holistique. Cela force l'œil humain à se concentrer sur l'icône décorée par cette sensation brillante ou étincelante.

#### La méthode pure CSS de morphing de formes — Clip Path : Polygon(...)

Avec certaines limitations, c'est la méthode "native" pour obtenir un effet de morphing pour les formes CSS.

**Problème connu** — la première limitation la plus importante qui doit être claire pour nous, développeurs, avant d'aborder cette technologie est que **_le nombre de coordonnées dans la forme de début et la forme de fin doit être égal_** — transformer un **carré** en **rectangle** est un usage simple et parfait qui fonctionne de manière transparente avec la technologie.

#### Expérimentation

Pour être parfaitement honnête, c'est pretty much la première fois que j'utilise `clip-path:Polygon()` dans un cas d'usage lié au travail réel. J'ai donc décidé de me lancer dans quelques expérimentations pour mieux comprendre ses tenants et aboutissants avant d'aborder le défi spécifique en question.

#### Expérience 1 — Une approche naïve — Carré → Étoile à 4 pointes

![Image](https://cdn-media-1.freecodecamp.org/images/1*38mBJrncsiHh40Fuvwx-IA.gif)
_Morphing Carré → Étoile à 4 pointes au survol_

Wow, ce n'est que ma première expérience et je suis déjà enthousiasmé par `clip-path` :) bien que quelque chose de assez particulier se soit passé ici… La direction du morphing semble se comporter bizarrement. La raison est simple : la forme d'origine avait un total de 8 points de coordonnées, 4 d'entre eux empilés sur chaque coordonnée de coin, conduisant ainsi à ce comportement de morphing bizarre.

![Image](https://cdn-media-1.freecodecamp.org/images/1*oMZJ7iaRv_3SAKlFAYXjEg.png)
_2 points (coordonnées) empilés sur chaque coin → 8 points également répartis le long des côtés du carré_

Quelques étapes plus loin dans l'expérimentation, j'ai découvert cet outil merveilleux et l'ai utilisé pour commencer à travailler avec des pourcentages plutôt qu'avec des pixels. J'ai également pu éditer mes formes en ligne avec lui. Dans l'ensemble, je recommande vivement de l'essayer — voici [Clippy](http://bennettfeely.com/clippy/) !

#### Expérience 2 — Directions de morphing ajustées — Carré → Étoile à 4 pointes

Selon mes plans, le gif suivant montre une approche simplifiée que j'ai prise pour essayer de résoudre ce problème avec un carré de 200px par 200px :

![Image](https://cdn-media-1.freecodecamp.org/images/1*xwmNJXP4QN2QrxwAK2NtZA.gif)
_Planification des morphs étape par étape_

Un simple ajustement de coordonnées — répartissant 4 des points empilés également à travers le carré (entre les coins) — devrait, espérons-le, conduire à un effet de morphing plus fluide et dans la bonne direction (verticalement et horizontalement respectivement) visant vers le centre des deux formes plutôt que dans la direction diagonale comme avant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*kjOmqppHr_MoMDpn1OCvcg.gif)
_Aha Succès ! — L'effet de morphing semble décent maintenant_

#### Expérience 3 — Octogone → Carré

![Image](https://cdn-media-1.freecodecamp.org/images/1*u68nanh5vvWV4dmAsQheOA.gif)
_Élément d'étincelle unique — ralenti pour voir les phases Octogone et Carré_

Si nous regardons attentivement et à plusieurs reprises l'effet d'étincelle unique ci-dessus, nous remarquons brièvement qu'à environ 50 % de l'animation, il se transforme en octogone. De plus, dans les phases avant et après l'octogone, l'étincelle se transforme en carré.

Cela semble être une tâche assez simple, n'est-ce pas ? J'ai pensé que je pourrais simplement utiliser `clip-path` pour transformer mon carré précédent en octogone comme le gif ci-dessus. La réalité était un peu différente, et j'ai dû changer la forme initiale et dessiner son `polygon(...)` un peu différemment pour avoir le carré dans l'octogone lors de la transition.

La façon dont `clip-path` fonctionne est qu'il crée la région de découpe souhaitée dans l'élément en utilisant la propriété et comme mon carré original occupait toute la région de son élément. Je ne pouvais pas morpher en dehors de cette région avec l'allocation de coordonnées actuelle.

Quelques ajustements ont dû être faits — et j'ai également basculé pour travailler avec des pourcentages maintenant pour supporter la largeur/hauteur dynamique des formes à partir de l'élément parent.

![Image](https://cdn-media-1.freecodecamp.org/images/1*R2ql3FAJtLylpK4V2sQAxg.png)

Et voilà — nous avons fait quelques progrès et maintenant nous avons un octogone qui se transforme en carré et vice versa. Mais attendez… nous n'avons pas encore terminé !

![Image](https://cdn-media-1.freecodecamp.org/images/1*MDva1WbMHIRuxCANGBZieg.gif)
_Les octogones respirants sont réels ?!_

#### Expérience 4 — Octogone → Étoile à 4 pointes → Retour (Cycle complet)

Maintenant que nous savons que l'octogone est la plus grande apparition de la forme de morphing, nous pouvons rendre notre forme de morphing beaucoup plus précise et transitionner entre ses phases réelles d'étoile à 4 pointes → Octogone → Retour, comme vu ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1*X1ZtJRj1QvfFvQ-lZRx7Og.gif)
_C'est plus comme ça_

#### Expérience 5 — Mise à l'échelle et animation en boucle infinie

J'ai donc commencé cette expérience en passant d'abord de l'événement de survol à une animation infinie déclenchée instantanément qui utilise d'abord la transformation `scale(...)` pour faire apparaître et disparaître l'étoile respectivement comme vu ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1*BWGVRte7rRLVrjTLBE2qHA.gif)
_Maintenant tu me vois, maintenant tu ne me vois pas — démo [ici](https://codesandbox.io/s/j4z7nvzwry" rel="noopener" target="_blank" title=")_

#### Expérience 6 — Rotation, positions de début et de fin

Quelques ajustements supplémentaires pour faire en sorte que l'étoile se met à l'échelle jusqu'à la taille complète dans la position de début et déterminer sa position finale avec `transform:rotate(180deg)`

![Image](https://cdn-media-1.freecodecamp.org/images/1*gpufiV_12HvEM-iPFz1xxw.gif)
_C'est une rotation, Mario ! — démo [ici](https://codesandbox.io/s/m4x0kq0l3y" rel="noopener" target="_blank" title=")_

#### Le défi de la bordure

Après avoir passé du temps à expérimenter, j'ai réalisé que ce que j'avais accompli jusqu'à présent ne serait pas satisfaisant. Dans l'exemple original, il semble que lorsque les étincelles apparaissent au-dessus de l'icône dans la micro-interaction originale, elles ont une sorte de bordure blanche le long de la forme qui se morph avec la forme à chaque étape de ses `keyframes` :

![Image](https://cdn-media-1.freecodecamp.org/images/1*6wOJDPVpnvhvqKDgfiduoA.png)
_Un peu agrandi — mais il est clair que des bordures sont présentes le long du morphing_

#### Expérience 6 — Construction d'une bordure qui se morph avec l'étincelle

Après avoir recherché des solutions sur internet, stack overflow et d'autres suggestions dans des articles pour aborder le problème, j'ai compris que ce défi était assez unique. Je n'ai pas trouvé de solutions spécifiques à mon problème. Le fait que ma bordure devait "coller" à la forme pendant qu'elle se morph compliquait encore plus les choses. J'ai donc entrepris de faire quelques tests jusqu'à ce que je trouve la solution.

Un "clone d'étincelle" qui est rendu juste avant mon élément principal d'étincelle en tant qu'élément frère était la solution parfaite. Les deux devaient être `display: flex` et positionnés verticalement ainsi qu'horizontalement au centre de leur conteneur avec `justify-content: center` et `align-items: center` pour obtenir ce qui suit :

![Image](https://cdn-media-1.freecodecamp.org/images/1*NSlCryrtCHNCt0jC0IDDqQ.png)

Mais Johnny, attends ! Comment vas-tu t'assurer que le clone suit son frère pendant l'animation `keyframes` de morphing ? Après avoir essayé d'animer le parent et l'enfant simultanément et avoir rencontré quelques problèmes ou bugs bizarres de navigateur, j'ai trouvé que l'approche des frères avec `flex` fournissait la meilleure solution comme vu ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1*4osoHSZSO9invJ75Yl0meA.gif)
_Des frères animés simultanément créent une bordure parfaitement ajustée — démo [ici](https://codesandbox.io/s/q3yw5lo8zq" rel="noopener" target="_blank" title=")_

### Relier les points

À ce stade, je sentais déjà que les défis difficiles de ce projet avaient pris fin. Tout ce que j'avais à faire maintenant était de trouver une icône d'avatar similaire, positionner 3 étincelles, ajuster leurs positions manuellement jusqu'à ce que je sois satisfait, et ajuster leur largeur/hauteur également jusqu'à ce que j'atteigne le résultat final.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jUA3DHCHZrCrGe-ZOFiUdw.gif)
_Une version agrandie pour mieux voir comment les choses fonctionnent_

![Image](https://cdn-media-1.freecodecamp.org/images/1*YiRlChFNIRnavHfpHqO8uA.gif)
_La micro-interaction finale — démo [ici](https://codesandbox.io/s/z3x7vl176m" rel="noopener" target="_blank" title=")_

### Résumé

Pour conclure, j'ai apprécié me challenger en recréant cette micro-interaction. J'ai appris énormément sur la façon dont un élément apparemment simple dans notre vie quotidienne (comme une invitation à cliquer sur une nouvelle icône de la part des développeurs d'un logiciel que nous consommons) est en réalité bien plus qu'un simple ensemble d'éléments et d'animations parfaitement synchronisés et correctement orientés.

Une telle micro-interaction sur mesure est une œuvre d'art. C'est un élément UI unique soigneusement conçu pour résoudre un problème difficile. Dans notre cas, les développeurs de Facebook ont modifié la barre de navigation de mon application mobile, supprimé une icône que je n'utilisais pas souvent et l'ont remplacée par une icône qui m'a permis d'effectuer une action que j'avais du mal à trouver et que je souhaitais prendre à de nombreuses reprises — retourner à mon profil.

C'est une décision intelligente, une micro-interaction habilement conçue qui réside à l'intérieur d'un écran statique. C'est la seule partie en mouvement de l'écran, et bien que très minimale et relativement petite à l'écran, les étoiles brillantes et étincelantes sur les marges de l'icône ont attiré mes yeux et mon doigt pour cliquer automatiquement dessus. Maintenant, j'apprécie encore plus le travail et la réflexion derrière cela — donc merci aux designers d'interaction et aux développeurs frontend de Facebook pour avoir construit de si géniales micro-interactions !

### Conclusion

Je vous encourage tous à oser et essayer de résoudre des problèmes difficiles d'UI et d'UX par l'idéation et l'expérimentation. Bien que ce soit agréable et peut-être un peu valorisant pour l'ego d'atteindre le résultat final et de réussir, je pense que c'est la partie la moins significative de l'expérience.

À mes yeux, le voyage que vous entreprenez, équipé de votre ensemble de compétences en expérimentation, en réflexion et en consultation avec les autres, est la meilleure partie. Les processus d'apprentissage et de collecte d'insights que vous vivez sont beaucoup plus importants, pour le dire simplement, et signifient bien plus que la destination.

#### Relecteurs

Un grand merci pour l'aide de ces grandes personnes qui ont aidé à relire et à donner des retours sur mes brouillons d'article, vous êtes incroyables ! ;) — [Jared M. Spool](https://www.freecodecamp.org/news/how-facebook-designs-microinteractions-for-feature-discovery-c79cfe998a77/undefined) [Yoni Weisbrod](https://www.freecodecamp.org/news/how-facebook-designs-microinteractions-for-feature-discovery-c79cfe998a77/undefined) [Ofir Ovadia](https://www.freecodecamp.org/news/how-facebook-designs-microinteractions-for-feature-discovery-c79cfe998a77/undefined) [Dima Vishnevetsky](https://www.freecodecamp.org/news/how-facebook-designs-microinteractions-for-feature-discovery-c79cfe998a77/undefined)

### Et maintenant ?

J'apprécierais les retours, les applaudissements, les partages. Vous pouvez bien sûr trouver tout le code, la démo et un bac à sable en direct pour jouer ainsi que des documents API organisés pour la commodité d'utilisation [juste ici](https://codesandbox.io/s/z3x7vl176m).

Plus d'articles recommandés par moi sur **Product Design, UX & Frontend** :   
[Medium Clap Recreated in Vanilla JS](https://medium.com/@yonatandoron/how-i-implemented-the-medium-clap-from-scratch-4a16ac90ad3b) — Un guide complet pas à pas  
[Star Rating — Make SVG Great Again](https://uxdesign.cc/star-rating-make-svg-great-again-d4ce4731347e)— Un tutoriel de code étape par étape

Plus de **composants Vue** :  
[Vue Dynamic Dropdown](https://github.com/JonathanDn/vue-dropdown) — Un menu déroulant élégant, personnalisable et facile à utiliser  
[Vue Dynamic Star Rating](https://github.com/JonathanDn/vue-stars-rating)— Un composant d'évaluation par étoiles dynamique pour Vue (similaire à Google Play)

Je suis Jonathan Doron, un développeur web avec une grande passion pour le Frontend centré sur l'utilisateur et l'architecture client modulaire.

Ce qui m'excite ces jours-ci est l'exploration de l'océan du **Interaction Design**, plus spécifiquement des **Micro Interactions** et de leur impact sur nos vies. Je le fais en recréant des interactions existantes ainsi qu'en concevant mes propres interactions dans le cadre de ma quête pour approfondir mes connaissances dans le domaine.

Vous êtes les bienvenus pour me suivre, tweeter ou m'envoyer des messages librement avec toutes vos questions, retours ou suggestions ! — [Twitter](https://twitter.com/jodoron)