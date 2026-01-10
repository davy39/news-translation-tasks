---
title: CSS Flexbox Expliqué par un Road Trip à Travers le Pays
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-10-22T05:34:28.000Z'
originalURL: https://freecodecamp.org/news/css-flexbox-explained-by-road-tripping-across-the-country-1217b69c390e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*kwaAOW_ja_raNVgV3VgZ2g.jpeg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: CSS Flexbox Expliqué par un Road Trip à Travers le Pays
seo_desc: 'By Kevin Kononenko

  If you have ever been on a long roadtrip, then you can understand CSS Flexbox!

  The popular Flexbox model attempts to replace the giant pain known as CSS “floats”.
  Unfortunately, it also introduces yet another entirely new system in...'
---

Par Kevin Kononenko

#### Si vous avez déjà fait un long road trip, alors vous pouvez comprendre CSS Flexbox !

Le modèle populaire Flexbox tente de remplacer la grande douleur connue sous le nom de CSS « [floats](https://medium.freecodecamp.com/css-floats-explained-by-riding-an-escalator-57fa55232333) ». Malheureusement, il introduit également un autre système entièrement nouveau dans CSS. Et vous pensiez qu'il y en avait déjà assez !

En réalité, la nature orientée grille de Flexbox a beaucoup plus de sens que de constamment jongler avec vos valeurs « float » et « block/inline-block ».

Il existe déjà quelques bonnes ressources, comme [Flexbox Tower Defense](http://www.flexboxdefense.com/) et ce [guide plus technique](https://css-tricks.com/snippets/css/a-guide-to-flexbox/).

Dans cet article, je vais expliquer le système Flexbox à travers l'un de mes types de vacances préférés... le road trip !

C'est exact — nous allons utiliser l'ensemble des États-Unis dans cette analogie.

Les États-Unis ont en fait un système autoroutier interétatique orienté grille qui s'étend d'est en ouest et du nord au sud.

![Image](https://cdn-media-1.freecodecamp.org/images/1*dvFENsh3hvfWUw4Y6ahXfA.png)

Bien que cette carte soit géographiquement exacte, elle est assez difficile à comprendre. Alors essayons à nouveau.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Qqg_4ini5SyEszW8kQByqA.jpeg)
_[https://betterexplained.com/articles/highway-math/](https://betterexplained.com/articles/highway-math/" rel="noopener" target="_blank" title=")_

Dans ce scénario, **vous devez principalement voyager le long d'un chemin unidirectionnel**.

Par exemple, vous pourriez prendre l'itinéraire de Seattle à Boston qui n'inclut que l'ouest à l'est. Ou, vous pourriez prendre l'itinéraire de Seattle à San Diego, qui ne couvre que le nord au sud.

Puisque la position par défaut est en haut à gauche, nous commencerons par Seattle. Vous aurez l'occasion d'ajouter des détours à votre road trip vers la fin ! Cela est important car cela imite le flux des <div> dans leur conteneur.

Partons sur la route !

### flex-direction : La direction de votre voyage

Flex-direction détermine la direction des éléments dans un conteneur <div> avec « display:flex; ». La valeur par défaut est « row », ce qui signifie de gauche à droite. Pas de surprises ici.

Disons que vous commencez à Seattle et que vous faites un voyage à Boston. Ce voyage pourrait ressembler à ceci en HTML :

Cela suppose que vous faites des arrêts à Yellowstone, Mount Rushmore et Chicago. Voici une vue chronologique, en supposant que vous vous arrêtez pendant 2 jours à chaque endroit.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MHr0lF_nWdUim0T1duN81A.png)

Et si vous utilisez « flex-direction:column; » ? Cela signifie que vos <div> s'aligneront de haut en bas. Maintenant, vous allez de Seattle à San Diego. Les arrêts sur le chemin pourraient être Portland, San Francisco et Los Angeles.

![Image](https://cdn-media-1.freecodecamp.org/images/1*9k1NlSDqmYG46zb_nc49oQ.png)

### justify-content : Comment vous espacez vos arrêts le long du voyage

D'accord, retournons au voyage de Seattle à Boston. Avec Flexbox, nous pouvons décider comment nos <div> enfants se répartissent le long de la largeur du conteneur. Donc, si vous êtes en road trip, vous ne voulez pas nécessairement espacer vos arrêts de manière égale. Vous pourriez vous arrêter plus fréquemment au début ou à la fin.

La valeur par défaut pour justify-content est « flex-start », ce qui signifie que vos <div> se répartissent à partir du côté le plus à gauche. Cela ressemble à choisir de faire toutes vos escales au début du road trip. Cela inclurait des endroits comme le parc national de Glacier, Yellowstone et Mount Rushmore.

Sur une carte :

![Image](https://cdn-media-1.freecodecamp.org/images/1*hsukM2jd3rHpnMZe77R0SQ.png)

D'accord, cela est admis un peu irréaliste. Vous ne voudriez probablement pas conduire 20 heures du Dakota du Sud directement à Boston. On pourrait en dire autant de « flex-end », lorsque tous les <div> se serrent du côté droit du conteneur. Cela inclurait des arrêts dans des endroits comme la merveilleuse ville de Cleveland, les chutes du Niagara et le Temple de la renommée du baseball.

Sur la carte :

![Image](https://cdn-media-1.freecodecamp.org/images/1*UqTFioPsD_oGuGSR04u22w.png)

Un autre exemple est « center », où les <div> s'alignent eux-mêmes au milieu du conteneur <div>. Cela signifierait des visites à Mount Rushmore, le Mall of America dans le Minnesota et Chicago.

### align-items : Quelle autoroute voulez-vous prendre à travers le pays ?

D'accord, jusqu'à présent, nous avons principalement discuté de l'itinéraire nord à travers le pays. En termes HTML, cela signifie que nous allons simplement le long du haut du <div>. Mais une propriété magique de Flexbox est que nous pouvons facilement nous déplacer au milieu ou en bas du <div> sans aucune astuce CSS.

La propriété align-items est par défaut « flex-start », mais si nous la changeons en « center », nos <div> s'aligneront verticalement au centre du conteneur. C'est un peu comme commencer votre road trip à San Francisco, vous diriger vers Las Vegas, puis Denver, puis St. Louis et terminer à Washington D.C.

Voici la carte :

![Image](https://cdn-media-1.freecodecamp.org/images/1*v8ihdtN84aFfEu5rMlCrXw.png)

Et, en HTML :

Si vous vouliez définir votre valeur align-items sur « flex-end », vos <div> s'aligneraient en bas du conteneur. Vous prendriez l'itinéraire sud à travers les États-Unis, et vous arrêteriez dans des endroits comme Sedona, Austin et La Nouvelle-Orléans avant de terminer à Jacksonville.

### align-self : Avoir un arrêt sur un itinéraire autoroutier différent

Vous pouvez appliquer « align-self » à des <div> enfants individuels afin de les déplacer verticalement dans le conteneur, indépendamment de la propriété align-items. Donc, si vous faites le voyage de Seattle à Boston, vous pouvez faire un arrêt à Las Vegas, qui est au milieu du pays. Ensuite, vous pouvez continuer vers Mount Rushmore ou ailleurs sur le flux horizontal normal.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MktBw1O06Ka2hyx94qaC3g.png)

### order : Faire vos arrêts dans un ordre spécifique

Jusqu'à présent, chaque arrêt a correspondu à l'ordre des éléments dans le HTML. En d'autres termes, si l'arrêt à Mount Rushmore est spécifié en troisième dans le HTML, cela signifie qu'il sera le troisième arrêt du road trip.

La propriété « order » est une valeur numérique qui nous permet de changer l'ordre des éléments HTML. Sans Flexbox, nous devrions utiliser une série confuse de floats, ou simplement changer le HTML.

Avec « order », nous pouvons faire demi-tour sur notre road trip et visiter un endroit qui n'est pas sur le chemin vers le point final. Feriez-vous cela dans la vraie vie ? Seulement si vous aimez 15 heures supplémentaires en voiture !

Disons que nous faisons le voyage nord, de Seattle à Boston. Voici ce HTML à nouveau.

Mais, après avoir commencé à Seattle, nous voulons d'abord aller au Dakota du Sud pour le plus grand festival de danse carrée du monde. Nous utiliserions la propriété « order » pour nous assurer que la visite de Mount Rushmore vient juste après Seattle.

Order est par défaut à 0, donc nous pourrions vouloir donner à seattleVisit une valeur de -2, et à mountRushmoreVisit une valeur de -1 pour nous assurer qu'il vient en 2ème. Ensuite, le reste des éléments suivra dans un flux normal.

![Image](https://cdn-media-1.freecodecamp.org/images/1*qXT61u8PvoKDzOQhQVvH2A.png)

Remarquez — ceci est maintenant strictement une vue chronologique, n'utilisant pas l'ordre géographique comme les autres cartes l'utilisaient.

### Conclusion

Il est temps pour un petit quiz ! Voici quelques destinations échantillons, en HTML.

Mais, si ce qui suit est votre itinéraire prévu... à quoi devrait ressembler le CSS ?

* Commencez à San Francisco
* 2ème arrêt : Las Vegas
* 3ème arrêt : Mount Rushmore
* 4ème arrêt : Retour à Denver
* Terminez en conduisant jusqu'à Washington D.C

La réponse :

Voici le raisonnement derrière cela :

* 4 éléments sur 5 sont le long de notre itinéraire central, donc nous « align-items » à _center_.
* Les trois arrêts sont généralement au milieu des États-Unis d'un point de vue ouest-est, donc nous « justify-content » à _center_ également.
* Mount Rushmore est sur l'itinéraire nord, donc nous utilisons _align-self_ sur ce <div>.
* La propriété CSS _order_ est la raison pour laquelle nous devons revenir à Denver, et pourquoi notre voyage réel ne suit pas l'ordre des enfants <div> dans le HTML. Order nous permet de changer la séquence des <div>. Dans ce cas, nous déplaçons Denver à l'avant-dernier arrêt, donc nous devons lui donner un ordre supérieur à 0, mais inférieur à l'ordre du dernier <div> afin que nous terminions toujours à D.C.

Si vous avez aimé cet article, vous aimerez peut-être aussi mes [autres explications](https://www.rtfmanual.io/guides/) de sujets CSS et JavaScript difficiles, comme le positionnement, le Modèle-Vue-Contrôleur et les callbacks.

Et si vous pensez que cela pourrait aider d'autres personnes dans la même situation que vous, donnez-lui un « cœur » !