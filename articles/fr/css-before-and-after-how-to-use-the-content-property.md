---
title: CSS Before et CSS After – Comment utiliser la propriété Content
subtitle: ''
author: Jesse Hall
co_authors: []
series: null
date: '2020-06-26T23:42:55.000Z'
originalURL: https://freecodecamp.org/news/css-before-and-after-how-to-use-the-content-property
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/fCC_-Content-Property-1.png
tags:
- name: CSS
  slug: css
seo_title: CSS Before et CSS After – Comment utiliser la propriété Content
seo_desc: The content property in CSS defines the content of an element. You may have
  heard that this property only applies to the ::before and ::after pseudo-elements.
  In this article, we'll explore various use cases for the content property, including
  outsid...
---

La propriété `content` en CSS définit le contenu d'un élément. Vous avez peut-être entendu dire que cette propriété ne s'applique qu'aux pseudo-éléments `::before` et `::after`. Dans cet article, nous explorerons divers cas d'utilisation de la propriété `content`, y compris en dehors des pseudo-éléments.

## Prérequis

Puisque la majorité des cas d'utilisation de la propriété `content` impliquent des pseudo-éléments, je vous suggère d'être familier avec le fonctionnement des pseudo-éléments `::before` et `::after`. Voici un excellent article pour vous mettre à niveau :

* [CSS Pseudo-Elements - Before and After Selectors Explained](https://www.freecodecamp.org/news/css-pseudo-elements-before-and-after-selectors-explained/)

## Valeurs acceptées

Tout d'abord, examinons toutes les valeurs acceptées de la propriété `content`.

* `normal` : Il s'agit de la valeur par défaut. Se calcule à `none` lorsqu'elle est utilisée avec des pseudo-éléments.

* `none` : Un pseudo-élément ne sera pas généré.

* `<string>` : Définit le contenu comme la chaîne spécifiée. Cette chaîne peut contenir des séquences d'échappement Unicode. Par exemple, le symbole de copyright : `\\000A9`.

* `<image>` : Définit le contenu comme une image ou un dégradé en utilisant `url()` ou `linear-gradient()`.

* `open-quote` | `close-quote` : Définit le contenu comme le caractère de guillemet approprié référencé depuis la propriété `quotes`.

* `no-open-quote` | `no-close-quote` : Supprime un guillemet de l'élément sélectionné, mais incrémente ou décrémente toujours le niveau de imbrication référencé depuis la propriété `quotes`.

* `attr(*attribute*)` : Définit le contenu comme la valeur de chaîne de l'attribut sélectionné de l'élément sélectionné.

* `counter()` : Définit le contenu comme la valeur d'un `counter`, généralement un nombre.

## Chaîne

L'un des exemples les plus basiques serait l'utilisation de l'ajout de contenu *chaîne* avant ou après un élément. Dans cet exemple, nous ajouterons un symbole de lien avant un lien et ajouterons l'URL du lien après celui-ci.

```css
a::before {
	content: "\\1F517 ";
}
a::after {
	content: " (" attr(href) ")";
}
```

Remarquez l'espace après le caractère Unicode dans le pseudo-élément `::before` et avant la première parenthèse dans le pseudo-élément `::after`. Cela créera un espace entre ceux-ci et l'élément parent.

Alternativement, vous pourriez ajouter un `padding` ou une `margin` aux pseudo-éléments pour ajouter une séparation.

%[https://codepen.io/codeSTACKr/pen/OJMjpvL?editors=1100]

## Guillemets de base

Avec la propriété `content`, vous pouvez ajouter des guillemets avant et/ou après des éléments. Maintenant, en HTML, nous avons la balise `<q>`. Cela ajoutera également des guillemets autour de son contenu. Cependant, avec la propriété `content`, nous pouvons avoir plus de contrôle sur la mise en œuvre.

Voici l'exemple le plus basique d'ajout de guillemets :

%[https://codepen.io/codeSTACKr/pen/NWxvpXq]

Vous pouvez également accomplir cela en utilisant la balise HTML `<q>`. Mais peut-être voulons-nous styliser le guillemet différemment. Ajoutons donc uniquement le guillemet ouvrant et non le guillemet fermant. Et stylisons également le guillemet ouvrant.

```css
p {
  position: relative;
  font-size: 3rem;
  margin: 4rem;
}
p::before {
  content: open-quote;
  position: absolute;
  left: -3.5rem;
  top: -2rem;
  font-size: 8rem;
  color: rgba(0, 0, 0, 0.5)
}
```

Le résultat :

![Image montrant un guillemet stylisé unique en haut à gauche du paragraphe](https://www.freecodecamp.org/news/content/images/2020/06/quote2.jpg align="left")

## Guillemets avancés

Nous pouvons également spécifier où nous ne voulons pas de guillemets. Par exemple, vous pouvez citer quelqu'un qui cite une autre personne. Vous auriez donc des guillemets dans des guillemets, ce qui peut prêter à confusion pour le lecteur.

Dans le CodePen ci-dessous, nous utilisons des balises HTML `<q>`, puis nous spécifions quelles balises ne doivent pas afficher les guillemets.

À première vue, vous pourriez penser que nous devrions simplement supprimer la balise `<q>` là où c'est nécessaire. Mais en spécifiant où un guillemet ne doit pas être, cela incrémente ou décrémente toujours le niveau de imbrication référencé depuis la propriété `quotes`.

Pour expliquer cela, nous devons comprendre la propriété `quotes`. Il s'agit simplement d'un "tableau" de caractères qui doivent être utilisés lors de la citation. Voici un exemple :

```css
q {
  quotes: '\u201c' '\u201d' '\u2018' '\u2019' '\u201c' '\u201d';
}
```

Ce sont des ensembles de guillemets. Le premier ensemble sera utilisé pour le niveau supérieur des guillemets. Le deuxième ensemble sera utilisé pour la première citation imbriquée. Et le troisième ensemble sera utilisé pour la deuxième citation imbriquée. Et ainsi de suite, s'il y avait plus d'ensembles inclus.

Maintenant que nous comprenons la propriété `quotes`, je peux expliquer comment les propriétés `no-open-quote` et `no-close-quote` fonctionnent.

Pour chaque niveau de guillemets, nous pouvons attribuer différents ensembles de caractères à utiliser pour les guillemets. En spécifiant où un guillemet ne doit pas être, cela incrémente ou décrémente toujours le niveau de imbrication référencé depuis la propriété `quotes`.

Jetez un œil à l'exemple ci-dessous. Vous verrez que le deuxième niveau de guillemets est ignoré.

%[https://codepen.io/codeSTACKr/pen/NWxvbLw]

## Attributs

Les attributs peuvent être utilisés pour passer du contenu du HTML à la propriété `content` en CSS. Nous avons déjà utilisé cela dans l'exemple de lien où nous avons utilisé l'attribut `href` pour inclure la chaîne d'URL comme partie de notre contenu.

Un cas d'utilisation parfait pour cela est une infobulle. Vous pouvez ajouter un attribut `title` à un élément en HTML pour avoir une infobulle simple et intégrée au survol. Mais pour la personnaliser, nous pouvons utiliser un attribut de données sur notre balise HTML puis utiliser la propriété `content` pour ajouter une infobulle.

Dans cet exemple, nous utilisons l'attribut `data-tooltip` de notre élément HTML pour passer la valeur dans notre infobulle. Pour le pointeur de l'infobulle, nous définissons le `content` à `""`, car `content` est requis pour rendre un pseudo-élément `::before` ou `::after`.

%[https://codepen.io/codeSTACKr/pen/WNrEopO]

## Compteurs

La fonction CSS `counter()` retourne une chaîne représentant la valeur actuelle du compteur nommé. Dans l'exemple suivant, nous avons une liste ordonnée à laquelle nous ajouterons du contenu en utilisant un `counter`.

```html
<ol>
  <li></li>
  <li></li>
  <li></li>
</ol>
```

```css
ol {
  counter-reset: exampleCounter;
}
li {
  counter-increment: exampleCounter;
}
li::after {
  content: "[" counter(exampleCounter) "] == ["
               counter(exampleCounter, upper-roman) "]";
}
```

Sans entrer trop dans les détails de la fonction `counter`, nous devons d'abord initier le compteur sur l'élément `ol`. Nous pouvons nommer cela comme nous le souhaitons. Ensuite, nous disons au compteur de s'incrémenter sur chaque élément `li`. Et enfin, nous définissons le `content` de `li::after`.

Voici le résultat :

![Liste ordonnée](https://www.freecodecamp.org/news/content/images/2020/06/counter.jpg align="left")

Vous pourriez utiliser cela pour personnaliser le contenu dans chaque élément de liste qui nécessite un numéro correspondant. Ou vous pourriez utiliser cela pour personnaliser l'élément de liste lui-même. Par exemple, vous pourriez supprimer la numérotation par défaut et implémenter un système de numérotation personnalisé.

## Images

Les images et les dégradés peuvent être utilisés avec la propriété `content`. Cela est assez simple. Voici un exemple qui utilise les deux :

%[https://codepen.io/codeSTACKr/pen/WNrEpre]

Pour l'accessibilité, il existe également une option pour ajouter un texte alternatif pour l'image. Cette fonctionnalité n'est cependant pas entièrement prise en charge.

```css
content: url(//unsplash.it/200/200) / "Texte alternatif ici";
```

> Note : Ceci n'est pas pris en charge dans Firefox, IE et Safari. De plus, le dégradé ne fonctionne pas dans Firefox.

## En dehors des pseudo-éléments

C'est vrai ! Vous pouvez utiliser la propriété `content` en dehors des pseudo-éléments `::before` et `::after`. Bien que son utilisation soit limitée et non entièrement compatible dans tous les navigateurs.

Le cas d'utilisation le plus compatible serait le remplacement d'un élément.

```html
<div id='replace'>
  codeSTACKr
</div>
```

```css
#replace {
  content: url("<https://www.codestackr.com/logo_twoline_light.svg>");
  width: 100%;
}
```

> Note : Le remplacement n'est pas pris en charge dans IE.

## Conclusion

La plupart du temps, vous verrez `content: ""` dans les pseudo-éléments `::before` et `::after`. Mais la propriété `content` a de nombreuses applications utiles.

La meilleure utilisation, à mon avis, est de l'utiliser pour mettre à jour des éléments en masse. Si vous souhaitez ajouter une icône avant chaque lien sur votre site, il serait beaucoup plus facile de l'ajouter via la propriété `content` que de l'ajouter à chaque élément dans le document HTML.

## **Merci d'avoir lu !**

Merci d'avoir lu cet article. J'espère qu'il vous a aidé à mieux comprendre comment la propriété `content` fonctionne en CSS.

![Jesse Hall (codeSTACKr)](https://www.freecodecamp.org/news/content/images/2020/06/footer-banner-1.png align="left")

Je m'appelle Jesse et je viens du Texas. Découvrez mes autres contenus et faites-moi savoir comment je peux vous aider dans votre parcours pour devenir développeur web.

* [Abonnez-vous à ma chaîne YouTube](https://youtube.com/codeSTACKr)

* Dites bonjour ! [Instagram](https://instagram.com/codeSTACKr) | [Twitter](https://twitter.com/codeSTACKr)

* [Inscrivez-vous à ma newsletter](https://codeSTACKr.com)