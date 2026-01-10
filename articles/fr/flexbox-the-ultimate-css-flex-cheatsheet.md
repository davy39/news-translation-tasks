---
title: Flexbox - Le guide ultime des flex CSS (avec des diagrammes animés !)
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2019-10-11T16:53:11.000Z'
originalURL: https://freecodecamp.org/news/flexbox-the-ultimate-css-flex-cheatsheet
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/chuttersnap-fyaTq-fIlro-unsplash.jpg
tags:
- name: CSS
  slug: css
- name: flexbox
  slug: flexbox
- name: responsive design
  slug: responsive-design
seo_title: Flexbox - Le guide ultime des flex CSS (avec des diagrammes animés !)
seo_desc: 'This comprehensive CSS flexbox cheatsheet will cover everything you need
  to know to start using flexbox in your web projects.

  CSS flexbox layout allows you to easily format HTML. Flexbox makes it simple to
  align items vertically and horizontally usin...'
---

Ce guide complet sur les flexbox CSS couvrira tout ce que vous devez savoir pour commencer à utiliser les flexbox dans vos projets web.

La disposition CSS flexbox vous permet de formater facilement le HTML. Flexbox simplifie l'alignement des éléments verticalement et horizontalement en utilisant des lignes et des colonnes. Les éléments vont "s'adapter" à différentes tailles pour remplir l'espace. Cela facilite la conception responsive.

Les flexbox CSS sont idéales pour la disposition générale de votre site web ou de votre application. Elles sont faciles à apprendre, sont supportées dans tous les navigateurs modernes et il ne faut pas longtemps pour comprendre les bases. À la fin de ce guide, vous serez prêt à commencer à utiliser les flexbox dans vos projets web.

L'article inclut des [gifs animés utiles de Scott Domes](https://www.freecodecamp.org/news/an-animated-guide-to-flexbox-d280cf6afc35/) qui rendront les flexbox encore plus faciles à comprendre et à visualiser.

## Toutes les propriétés CSS Flexbox

Voici une liste de toutes les propriétés CSS flexbox qui peuvent être utilisées pour positionner des éléments en CSS. Ensuite, vous verrez comment elles fonctionnent.

### **CSS qui peut être appliqué au conteneur**

```css
display: flexbox | inline-flex;
flex-direction: row | row-reverse | column | column-reverse;
flex-wrap: nowrap | wrap | wrap-reverse;
flex-flow: <'flex-direction'> || <'flex-wrap'>
justify-content: flex-start | flex-end | center | space-between | space-around;
align-items: flex-start | flex-end | center | baseline | stretch;
align-content: flex-start | flex-end | center | space-between | space-around | stretch;
```

### **CSS qui peut être appliqué aux éléments dans le conteneur**

```css
order: <integer>;
flex-grow: <number>; /* par défaut 0 */
flex-shrink: <number>; /* par défaut 1 */
flex-basis: <length> | auto; /* par défaut auto */
flex: none | [ <'flex-grow'> <'flex-shrink'>? || <'flex-basis'> ]
align-self: auto | flex-start | flex-end | center | baseline | stretch;
```

## Terminologie

![Image](https://www.freecodecamp.org/news/content/images/2019/10/image-32.png)
_Diagramme de terminologie Flexbox issu de la [spécification officielle W3C](https://www.w3.org/TR/css-flexbox-1/)._

Avant d'apprendre ce que font les propriétés flexbox, il est important de comprendre la terminologie associée. Voici les définitions des termes clés de flexbox, tirés de la [spécification officielle W3C](https://www.w3.org/TR/css-flexbox-1/) pour flexbox.

* **main-axis** : L'axe principal d'un conteneur flex est l'axe principal le long duquel les éléments flex sont disposés. La direction est basée sur la propriété flex-direction.
* **main-start | main-end** : Les éléments flex sont placés dans le conteneur en commençant par le côté main-start et en allant vers le côté main-end.
* **main size** : La largeur ou la hauteur d'un conteneur flex ou d'un élément flex, selon ce qui est dans la dimension principale, est la taille principale de cette boîte. Sa propriété de taille principale est donc soit sa propriété de largeur, soit sa propriété de hauteur, selon ce qui est dans la dimension principale.
* **cross axis** : L'axe perpendiculaire à l'axe principal est appelé l'axe transversal. Sa direction dépend de la direction de l'axe principal.
* **cross-start | cross-end** : Les lignes flex sont remplies d'éléments et placées dans le conteneur en commençant par le côté cross-start du conteneur flex et en allant vers le côté cross-end.
* **cross size** : La largeur ou la hauteur d'un élément flex, selon ce qui est dans la dimension transversale, est la taille transversale de l'élément. La propriété de taille transversale est celle de 'width' ou 'height' qui est dans la dimension transversale.

## CSS Display Flex

`display: flex` indique à votre navigateur : "Je veux utiliser flexbox avec ce conteneur, s'il vous plaît."

Un élément `div` a par défaut `display:block`. Un élément avec ce paramètre de display occupe toute la largeur de la ligne sur laquelle il se trouve. Voici un exemple de quatre divs colorés dans un div parent avec le paramètre de display par défaut :

![Image](https://cdn-media-1.freecodecamp.org/images/ChnkgUaWEN6dmtS4EQCG60uqIjZVphsErq91)
_Source : Scott Domes_

Pour utiliser flexbox sur une section de votre page, commencez par convertir le conteneur parent en un conteneur flex en ajoutant `display: flex;` au CSS du conteneur parent.

Cela initialisera ce conteneur en tant que conteneur flex et appliquera certaines propriétés flex par défaut.

![Image](https://cdn-media-1.freecodecamp.org/images/6WwoIEc45lUHUcFQCmD8GmziiISm2lO64Y1-)
_Source : Scott Domes_

## Flex Direction

`flex-direction` vous permet de contrôler comment les éléments dans le conteneur s'affichent. Voulez-vous qu'ils soient de gauche à droite, de droite à gauche, de haut en bas ou de bas en haut ? Vous pouvez faire tout cela facilement en définissant la `flex-direction` du conteneur.

L'arrangement par défaut après avoir appliqué `display: flex` est que les éléments soient disposés le long de l'axe principal de gauche à droite. L'animation ci-dessous montre ce qui se passe lorsque `flex-direction: column` est ajouté à l'élément conteneur.

![Image](https://cdn-media-1.freecodecamp.org/images/wEg7wdKEfv9-bqaiB-t9hzOapBPiqZVYNFIh)
_Source : Scott Domes_

Vous pouvez également définir `flex-direction` sur `row-reverse` et `column-reverse`_._

![Image](https://cdn-media-1.freecodecamp.org/images/zYdQGSmhtMyqcAbEUDoEehohC8E-gtgvQx6b)
_Source : Scott Domes_

## Justify Content

`justify-content` est une propriété pour aligner les éléments dans le conteneur le long de l'axe principal (voir le diagramme de terminologie ci-dessus). Cela change en fonction de la manière dont le contenu est affiché. Il nous permet de remplir tout espace vide sur les lignes et de définir comment nous voulons le "justifier".

Voici nos options les plus courantes utilisées pour justifier le contenu : `flex-start | flex-end | center | space-between | space-around`.

Voici à quoi ressemblent les différentes options :

![Image](https://cdn-media-1.freecodecamp.org/images/OBGVr-DdHiQ2y9VOWuhXqXeGnFnyDSBTx7hv)
_Source : Scott Domes_

`space-between` distribue les éléments de sorte que le premier élément soit aligné avec le début et le dernier avec la fin. `space-around` est similaire mais les éléments ont un espace de moitié de taille à chaque extrémité.

## Flex Align Items

`align-items` nous permet d'aligner les éléments le long de l'axe transversal (voir le diagramme de terminologie ci-dessus). Cela permet au contenu d'être positionné de nombreuses manières différentes en utilisant justify content et align items ensemble.

Voici les options les plus courantes utilisées pour aligner les éléments : `flex-start | flex-end | center | baseline | stretch`

Pour que `stretch` fonctionne comme vous vous y attendez, la hauteur des éléments doit être définie sur `auto` au lieu d'une hauteur spécifique.

Cette animation montre à quoi ressemblent les options :

![Image](https://cdn-media-1.freecodecamp.org/images/UgsULw0Kk49l-l1wSzeurYNJKCmcA-01oE8a)
_Source : Scott Domes_

Maintenant, nous allons utiliser à la fois `justify-content` et `align-items`. Cela montrera la différence entre les axes principaux et les axes transversaux.

![Image](https://cdn-media-1.freecodecamp.org/images/u9tCV-zRt3qpgSyNQt53e-eRz0-HIrsqqOk-)
_Source : Scott Domes_

## Align Self

`align-self` vous permet d'ajuster l'alignement d'un seul élément.

Il a toutes les mêmes propriétés que `align-items`.

Dans l'animation suivante, le div parent a le CSS `align-items: center` et `flex-direction: row`. Les deux premiers carrés parcourent différentes valeurs `align-self`.

![Image](https://cdn-media-1.freecodecamp.org/images/HbnMZT330ylw5idocqrjOfp9DrlZt9JrJm9o)
_Source : Scott Domes_

## Flex Wrap

Par défaut, Flexbox essaiera de faire tenir tous les éléments dans une seule ligne. Cependant, vous pouvez changer cela avec la propriété `flex-wrap`. Il existe trois valeurs que vous pouvez utiliser pour déterminer quand les éléments passent à une autre ligne.

La valeur par défaut est `flex-wrap: nowrap`. Cela fera en sorte que tout reste dans une seule ligne de gauche à droite.

`flex-wrap: wrap` permettra aux éléments de passer à la ligne suivante s'il n'y a pas assez de place sur la première ligne. Les éléments seront affichés de gauche à droite.

`flex-wrap: wrap-reverse` permet également aux éléments de passer à la ligne suivante, mais cette fois les éléments sont affichés de droite à gauche.

## Flex Flow

`flex-flow` combine l'utilisation de `flex-wrap` et `flex-direction` en une seule propriété. Il est utilisé en définissant d'abord la direction puis le wrap. Voici un exemple : `flex-flow: column wrap;`

## Align Content

`align-content` est utilisé pour aligner les éléments avec plusieurs lignes. Il est utilisé pour l'alignement sur l'axe transversal et n'aura aucun effet sur le contenu qui est sur une seule ligne.

Voici les options : `align-content: flex-start | flex-end | center | space-between | space-around | stretch;`

## Centrage vertical avec Flexbox

Si vous souhaitez centrer verticalement tout le contenu à l'intérieur d'un élément parent, utilisez `align-items`. Voici le code à utiliser :

```css
.parent {
    display: flex;
    align-items: center;
}
```

## **Jeux et Applications**

Si vous souhaitez pratiquer l'utilisation de flexbox, essayez ces jeux et applications qui vous aideront à maîtriser flexbox.

* [Flexbox Defense](http://www.flexboxdefense.com/) est un jeu web où vous apprenez flexbox tout en essayant d'empêcher les ennemis entrants de passer vos défenses.
* [Flexbox Froggy](http://flexboxfroggy.com/) est un jeu où vous aidez Froggy et ses amis en écrivant du code CSS.
* [Flexyboxes](http://the-echoplex.net/flexyboxes/) est une application qui vous permet de voir des exemples de code et de changer les paramètres pour voir comment Flexbox fonctionne visuellement.
* [Flexbox Patters](http://www.flexboxpatterns.com/) est un site web qui présente une série d'exemples de Flexbox.

## Conclusion

Nous avons couvert toutes les propriétés CSS flexbox les plus courantes. La prochaine étape est la pratique ! Essayez de réaliser quelques projets en utilisant flexbox pour vous habituer à son fonctionnement.