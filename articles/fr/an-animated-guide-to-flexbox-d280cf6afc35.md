---
title: Comment fonctionne Flexbox — expliqué avec de grands, colorés et animés gifs
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-31T16:15:51.000Z'
originalURL: https://freecodecamp.org/news/an-animated-guide-to-flexbox-d280cf6afc35
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zyzR64aw4rDPsoG-ZwZ9rQ.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: flexbox
  slug: flexbox
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Comment fonctionne Flexbox — expliqué avec de grands, colorés et animés
  gifs
seo_desc: 'By Scott Domes

  Flexbox promises to save us from the evils of plain CSS (like vertical alignment).

  Well, Flexbox does deliver on that goal. But mastering its new mental model can
  be challenging.

  So let’s take an animated look at how Flexbox works, so ...'
---

Par Scott Domes

Flexbox promet de nous sauver des méfaits du CSS simple (comme l'alignement vertical).

Eh bien, Flexbox tient cette promesse. Mais maîtriser son nouveau modèle mental peut être un défi.

Alors, examinons de manière animée comment Flexbox fonctionne, afin de pouvoir l'utiliser pour construire de meilleures mises en page.

Le principe sous-jacent de Flexbox est de rendre les mises en page flexibles et intuitives.

Pour y parvenir, il permet aux conteneurs de décider eux-mêmes comment répartir uniformément leurs enfants — y compris leur taille et l'espace entre eux.

Tout cela semble bien en principe. Mais voyons à quoi cela ressemble en pratique.

Dans cet article, nous allons plonger dans les 5 propriétés Flexbox les plus courantes. Nous explorerons ce qu'elles font, comment vous pouvez les utiliser et à quoi leurs résultats ressembleront réellement.

### Propriété #1 : Display: Flex

Voici notre exemple de page web :

![Image](https://cdn-media-1.freecodecamp.org/images/ChnkgUaWEN6dmtS4EQCG60uqIjZVphsErq91)

Vous avez quatre divs colorées de différentes tailles, contenues dans une div grise. Pour l'instant, chaque div a par défaut `display: block`. Chaque carré occupe ainsi toute la largeur de sa ligne.

Pour commencer avec Flexbox, vous devez transformer votre **conteneur** en un **conteneur flexible**. C'est aussi simple que :

```
#container {  display: flex;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/6WwoIEc45lUHUcFQCmD8GmziiISm2lO64Y1-)

Pas grand-chose n'a changé — vos divs sont maintenant affichées en ligne, mais c'est à peu près tout. Mais en coulisses, vous avez fait quelque chose de puissant. **Vous avez donné à vos carrés ce qu'on appelle un _contexte flexible_.**

Vous pouvez maintenant commencer à les positionner dans ce contexte, avec beaucoup moins de difficulté que le CSS traditionnel.

### Propriété #2 : Flex Direction

Un conteneur Flexbox a deux axes : **un axe principal** et **un axe transversal**, qui par défaut ressemblent à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/HHwxqz2N4bNksz9YwcMBAtD0z9TTCxeNXNBS)

**Par défaut, les éléments sont disposés le long de l'axe principal, de gauche à droite.** C'est pourquoi vos carrés se sont alignés horizontalement une fois que vous avez appliqué `display: flex`.

Cependant, `flex-direction` vous permet de faire pivoter l'axe principal.

```
#container {  display: flex;  flex-direction: column;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/wEg7wdKEfv9-bqaiB-t9hzOapBPiqZVYNFIh)

Il y a une distinction importante à faire ici : `flex-direction: column` n'aligne pas les carrés sur l'axe transversal au lieu de l'axe principal. **Cela fait que l'axe principal lui-même passe de l'horizontale à la verticale.**

Il y a aussi quelques autres options pour flex-direction : _row-reverse_ et _column-reverse_.

![Image](https://cdn-media-1.freecodecamp.org/images/zYdQGSmhtMyqcAbEUDoEehohC8E-gtgvQx6b)

### Propriété #3 : Justify Content

_Justify-content_ contrôle la manière dont vous alignez les éléments sur **l'axe principal.**

Ici, vous allez approfondir un peu la distinction entre l'axe principal et l'axe transversal. D'abord, revenons à flex-direction: row.

```
#container {  display: flex;  flex-direction: row;  justify-content: flex-start;}
```

Vous avez cinq commandes à votre disposition pour utiliser _justify-content_ :

1. Flex-start
2. Flex-end
3. Center
4. Space-between
5. Space-around

![Image](https://cdn-media-1.freecodecamp.org/images/OBGVr-DdHiQ2y9VOWuhXqXeGnFnyDSBTx7hv)

Space-around et space-between sont les moins intuitifs. **Space-between donne un espace égal entre chaque carré, mais pas entre lui et le conteneur.**

Space-around met un coussin d'espace égal de chaque côté du carré — ce qui signifie **que l'espace entre les carrés les plus à l'extérieur et le conteneur est la moitié de l'espace entre deux carrés** (chaque carré contribuant une quantité égale de marge non chevauchante, doublant ainsi l'espace).

Une dernière note : rappelez-vous que **justify-content fonctionne le long de l'axe principal**, et **flex-direction change l'axe principal**. Cela sera important lorsque vous passerez à...

### Propriété #4 : Align Items

Si vous 'comprenez' justify-content, align-items sera un jeu d'enfant.

Comme justify-content fonctionne le long de l'axe principal, **align-items s'applique à l'axe transversal.**

![Image](https://cdn-media-1.freecodecamp.org/images/RfGcYLbTwhd9dmqLV9-F3ocjBE8Dp4ejvYXv)

Réinitialisons notre _flex-direction_ à row, afin que nos axes ressemblent à l'image ci-dessus.

Ensuite, plongeons dans les commandes align-items.

1. flex-start
2. flex-end
3. center
4. stretch
5. baseline

Les trois premières sont exactement les mêmes que _justify-content_, donc rien de trop compliqué ici.

Les deux suivantes sont un peu différentes, cependant.

Vous avez stretch, dans lequel les éléments occupent toute la longueur de l'axe transversal, et baseline, dans lequel le bas des balises de paragraphe sont alignés.

![Image](https://cdn-media-1.freecodecamp.org/images/UgsULw0Kk49l-l1wSzeurYNJKCmcA-01oE8a)

(Notez que pour `align-items: stretch`, j'ai dû régler la hauteur des carrés sur auto. Sinon, la propriété de hauteur remplacerait le stretch.)

Pour baseline, soyez conscient que si vous retirez les balises de paragraphe, cela aligne le bas des carrés à la place, comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/dIxrfoUa2r7vM62TGAlKN2KGOnIMmeNM-Gwr)

Pour mieux démontrer les axes principal et transversal, combinons justify-content et align-items et voyons comment le centrage fonctionne différemment pour les deux commandes flex-direction :

![Image](https://cdn-media-1.freecodecamp.org/images/u9tCV-zRt3qpgSyNQt53e-eRz0-HIrsqqOk-)

**Avec row, les carrés sont disposés le long d'un axe principal horizontal. Avec column, ils tombent le long d'un axe principal vertical.**

Même si les carrés sont centrés verticalement et horizontalement dans les deux cas, les deux ne sont pas interchangeables !

### Propriété #5 : Align Self

_Align-self_ vous permet de manipuler manuellement l'alignement d'un élément particulier.

C'est essentiellement une substitution de _align-items_ pour un carré. Toutes les propriétés sont les mêmes, bien qu'il soit par défaut sur _auto_, dans lequel il suit le _align-items_ du conteneur.

```
#container {  align-items: flex-start;}
```

```
.square#one {  align-self: center;}// Seul ce carré sera centré.
```

Voyons à quoi cela ressemble. Vous appliquerez _align-self_ à deux carrés, et pour le reste, vous appliquerez `align-items: center` et `flex-direction: row`.

![Image](https://cdn-media-1.freecodecamp.org/images/HbnMZT330ylw5idocqrjOfp9DrlZt9JrJm9o)

### Conclusion

Même si nous n'avons fait qu'effleurer la surface de Flexbox, ces commandes devraient être suffisantes pour gérer la plupart des alignements de base — et pour aligner verticalement à votre guise.

Si vous souhaitez voir plus de tutoriels Flexbox en GIF, ou si ce tutoriel vous a été utile, cliquez sur le cœur vert ci-dessous ou laissez un commentaire.

Merci d'avoir lu !