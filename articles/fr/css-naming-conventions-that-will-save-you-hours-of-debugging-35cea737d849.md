---
title: Conventions de nommage CSS qui vous feront économiser des heures de débogage
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-16T23:17:20.000Z'
originalURL: https://freecodecamp.org/news/css-naming-conventions-that-will-save-you-hours-of-debugging-35cea737d849
coverImage: https://cdn-media-1.freecodecamp.org/images/1*YunI3ChUVMlpmFzo75FczQ.png
tags:
- name: coding
  slug: coding
- name: CSS
  slug: css
- name: General Programming
  slug: programming
- name: style
  slug: style
- name: technology
  slug: technology
seo_title: Conventions de nommage CSS qui vous feront économiser des heures de débogage
seo_desc: 'By Emmanuel Ohans

  I have heard lots of developers say they hate CSS. In my experience, this comes
  as a result of not taking the time to learn CSS.

  CSS isn’t the prettiest ‘language,’ but it has successfully powered the styling
  of the web for over 20 ...'
---

Par Emmanuel Ohans

J'ai entendu beaucoup de développeurs dire qu'ils détestent CSS. Selon mon expérience, cela vient du fait de ne pas prendre le temps d'apprendre CSS.

CSS n'est pas le langage le plus élégant, mais il a réussi à alimenter le style du web depuis plus de 20 ans. Pas trop mal, n'est-ce pas ?

Cependant, à mesure que vous écrivez plus de CSS, vous voyez rapidement un gros inconvénient.

Il est extrêmement difficile de maintenir CSS.

Un CSS mal écrit se transformera rapidement en cauchemar.

Voici quelques conventions de nommage qui vous feront économiser un peu de stress et d'innombrables heures à l'avenir.

![Image](https://cdn-media-1.freecodecamp.org/images/0Nm4l3DA3bWTbPc6C4ViWDqewokYYootpoqb)
_vous y avez déjà été, n'est-ce pas ?_

### Utilisez des chaînes délimitées par des tirets

Si vous écrivez beaucoup de JavaScript, alors écrire des variables en camel case est une pratique courante.

```
var redBox = document.getElementById('...')
```

Bien, n'est-ce pas ?

Le problème est que cette forme de nommage n'est pas bien adaptée à CSS.

Ne faites pas ceci :

```
.redBox {  border: 1px solid red;}
```

À la place, faites ceci :

```
.red-box {   border: 1px solid red;}
```

C'est une convention de nommage CSS assez standard. Elle est probablement plus lisible.

De plus, elle est cohérente avec les noms des propriétés CSS.

```
// Correct
```

```
.some-class {   font-weight: 10em}
```

```
// Incorrect
```

```
.some-class {   fontWeight: 10em}
```

### La convention de nommage BEM

Les équipes ont différentes approches pour écrire des sélecteurs CSS. Certaines équipes utilisent des délimiteurs de tirets, tandis que d'autres préfèrent utiliser la convention de nommage plus structurée appelée BEM.

Généralement, il y a 3 problèmes que les conventions de nommage CSS tentent de résoudre :

1. Savoir ce que fait un sélecteur, juste en regardant son nom
2. Avoir une idée de l'endroit où un sélecteur peut être utilisé, juste en le regardant
3. Connaître les relations entre les noms de classe, juste en les regardant

Avez-vous déjà vu des noms de classe écrits comme ceci :

```
.nav--secondary {  ...}
```

```
.nav__header {  ...}
```

C'est la convention de nommage BEM.

### Expliquer BEM à un enfant de 5 ans

BEM tente de diviser l'interface utilisateur globale en petits composants réutilisables.

Considérez l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/pIFVbUmRtKN8x6DvLHEvJeUSM9Oda8ClkY5f)
_C'est une image primée d'un bonhomme bâton :)_

Non, elle n'est pas primée :(

Le bonhomme bâton représente un composant, comme un bloc de design.

Vous avez peut-être déjà deviné que le B dans BEM signifie « Block ».

Dans le monde réel, ce « block » pourrait représenter une navigation de site, un en-tête, un pied de page, ou tout autre bloc de design.

En suivant la pratique expliquée ci-dessus, un nom de classe idéal pour ce composant serait `stick-man`.

Le composant devrait être stylé comme suit :

```
.stick-man {   }
```

Nous avons utilisé des chaînes délimitées ici. Bien !

![Image](https://cdn-media-1.freecodecamp.org/images/ThMVqj-sv26pjpzLJU3MIF2TCdn-S4CjlEZk)

### E pour Éléments

Le E dans « BEM » signifie Éléments.

Les blocs de design globaux vivent rarement en isolation.

Par exemple, le bonhomme bâton a une `head`, deux magnifiques `arms`, et `feet`.

![Image](https://cdn-media-1.freecodecamp.org/images/bf2jyOzcZ8wgd95I3qR9IS3Cf6pRlQ2hHuGM)

La `head`, `feet`, et `arms` sont tous des éléments dans le composant. Ils peuvent être vus comme des composants enfants, c'est-à-dire des enfants du composant parent global.

En utilisant la convention de nommage BEM, les noms de classe des éléments sont dérivés en ajoutant **deux tirets bas**, suivis du nom de l'élément.

Par exemple :

```
.stick-man__head {
```

```
}
```

```
.stick-man__arms {
```

```
}
```

```
.stick-man__feet {
```

```
}
```

### M pour Modificateurs

Le M dans « BEM » signifie Modificateurs.

Et si le bonhomme bâton était modifié et que nous pouvions avoir un bonhomme bâton `blue` ou `red` ?

![Image](https://cdn-media-1.freecodecamp.org/images/Q-aWWnpw1UuoXxp5NGHxsjP5689VQBT0oGdQ)

Dans le monde réel, cela pourrait être un bouton `red` ou un bouton `blue`. Ce sont des modifications du composant en question.

En utilisant BEM, les noms de classe des modificateurs sont dérivés en ajoutant deux **tirets** suivis du nom de l'élément.

Par exemple :

```
.stick-man--blue {
```

```
}
```

```
.stick-man--red {
```

```
}
```

Le dernier exemple a montré le composant parent étant modifié. Ce n'est pas toujours le cas.

Et si nous avions des bonhommes bâton de différentes tailles de `head` ?

![Image](https://cdn-media-1.freecodecamp.org/images/ZK-riYJhmFfBVEof6xO8yGGR3O10g2dW7Xqn)

Cette fois, l'élément a été modifié. Rappelez-vous, l'élément est un composant enfant dans le bloc global contenant.

Le `.stick-man` représente le `Block`, `.stick-man__head` l'élément.

Comme vu dans l'exemple ci-dessus, les doubles tirets peuvent également être utilisés comme suit :

```
.stick-man__head--small {
```

```
}
```

```
.stick-man__head--big {
```

```
}
```

Encore une fois, notez l'utilisation des doubles **tirets** dans l'exemple ci-dessus. Cela est utilisé pour désigner un modificateur.

Maintenant, vous avez compris.

C'est essentiellement comment fonctionne la convention de nommage BEM.

Personnellement, j'ai tendance à utiliser uniquement des noms de classe délimités par des tirets pour des projets simples, et BEM pour des interfaces utilisateur plus complexes.

Vous pouvez [en lire plus](http://getbem.com/naming/) sur BEM.

[**BEM - Block Element Modifier**](http://getbem.com/naming/)  
[_BEM - Block Element Modifier est une méthodologie qui vous aide à atteindre des composants réutilisables et le partage de code dans le..._getbem.com](http://getbem.com/naming/)

### Pourquoi utiliser des conventions de nommage ?

> Il n'y a que deux problèmes difficiles en informatique : l'invalidation du cache et le nommage des choses — _Phil Karlton_

Nommer les choses est difficile. Nous essayons de faciliter les choses et de nous faire gagner du temps à l'avenir avec un code plus maintenable.

Nommer correctement les choses en CSS rendra votre code plus facile à lire et à maintenir.

Si vous choisissez d'utiliser la convention de nommage BEM, il sera plus facile de voir la relation entre vos composants/blocs de design juste en regardant le balisage.

Vous vous sentez confiant ?

### Noms CSS avec des crochets JavaScript

Aujourd'hui est le premier jour de John au travail.

On lui remet un code `HTML` qui ressemble à ceci :

```
<div class="siteNavigation">
```

```
</div>
```

John a lu cet article et réalise que ce n'est peut-être pas la meilleure façon de nommer les choses en `CSS`. Il va donc de l'avant et refactorise la base de code comme suit :

```
<div class="site-navigation">
```

```
</div>
```

Ça a l'air bien, n'est-ce pas ?

Sans le savoir, John avait cassé la base de code ???

Comment ?

Quelque part dans le code JavaScript, il y avait une relation avec l'ancien nom de classe, `siteNavigation` :

```
//le code Javasript
```

```
const nav = document.querySelector('.siteNavigation')
```

Ainsi, avec le changement du nom de classe, la variable `nav` est devenue `null`.

Comme c'est triste.

Pour prévenir des cas comme celui-ci, les développeurs ont imaginé différentes stratégies.

#### 1. Utilisez des noms de classe js-

Une façon de mitiger de tels bugs est d'utiliser un nom de classe `**js-***` pour désigner une relation avec l'élément DOM en question.

Par exemple :

```
<div class="site-navigation js-site-navigation">
```

```
</div>
```

Et dans le code JavaScript :

```
//le code Javasript
```

```
const nav = document.querySelector('.js-site-navigation')
```

Par convention, quiconque voit le nom de classe `**js-**site-navigation` comprendrait qu'il y a une relation avec cet élément DOM dans le code JavaScript.

#### 2. Utilisez l'attribut Rel

Je n'utilise pas moi-même cette technique, mais j'ai vu des gens le faire.

Reconnaissez-vous ceci ?

```
<link rel="stylesheet" type="text/css" href="main.css">
```

En gros, l'**attribut rel** définit la relation que la ressource liée a avec le document à partir duquel elle est référencée.

Dans l'exemple précédent avec John, les partisans de cette technique feraient ceci :

```
<div class="site-navigation" rel="js-site-navigation">
```

```
</div>
```

Et en JavaScript :

```
const nav = document.querySelector("[rel='js-site-navigation']")
```

J'ai des doutes sur cette technique, mais vous êtes susceptible de la rencontrer dans certains codebases. L'argument ici est, _"eh bien, il y a une relation avec Javascript, donc j'utilise l'attribut rel pour désigner cela"_.

Le web est un grand endroit avec beaucoup de différentes "méthodes" pour résoudre le même problème.

#### 3. N'utilisez pas les attributs de données

Certains développeurs utilisent les attributs de données comme des crochets JavaScript. Ce n'est pas correct. Par définition, les attributs de données sont utilisés **pour stocker des données personnalisées**.

![Image](https://cdn-media-1.freecodecamp.org/images/08r5ESO6cpzZvcZz-KczJEGXtPBtCLorryI6)
_Bonne utilisation des attributs de données. Comme vu sur Twitter_

**Édition #1 : Comme mentionné par certaines personnes incroyables dans la section des commentaires, si les gens utilisent l'attribut 'rel', alors il est peut-être acceptable d'utiliser les attributs de données dans certains cas. C'est à vous de décider après tout.**

### Conseil Bonus : Écrivez plus de commentaires CSS

Cela n'a rien à voir avec les conventions de nommage, mais cela vous fera également gagner du temps.

Alors que beaucoup de développeurs web essaient de NE PAS écrire de commentaires JavaScript ou de s'en tenir à quelques-uns, je pense que vous devriez écrire plus de commentaires CSS.

Puisque CSS n'est pas le langage le plus élégant, des commentaires bien structurés peuvent faire gagner du temps lorsque vous essayez de comprendre votre code.

Cela ne fait pas de mal.

Jetez un coup d'œil à la façon dont le code source de Bootstrap est [bien commenté](https://github.com/twbs/bootstrap/blob/v4-dev/scss/_carousel.scss).

Vous n'avez pas besoin d'écrire des commentaires pour dire que `color: red` donnera une couleur rouge. Mais, si vous utilisez un truc CSS qui est moins évident, n'hésitez pas à écrire un commentaire.

### Prêt à devenir Pro ?

J'ai créé un guide CSS gratuit pour faire décoller vos compétences CSS, immédiatement. [Obtenez l'ebook gratuit](https://pages.convertkit.com/0c2c62e04a/60e5d19f9b).

![Image](https://cdn-media-1.freecodecamp.org/images/4AqtYrYGSx6s9Mwmzji1vj8RqwvarVns4y7V)
_Sept secrets CSS que vous ne connaissiez pas_