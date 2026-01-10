---
title: Le concept CSS le plus important à apprendre
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-11T21:31:21.000Z'
originalURL: https://freecodecamp.org/news/the-most-important-css-concept-to-learn-8e929c944a19
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tf536ftkgQuDPEaiY4QVpg.png
tags:
- name: CSS
  slug: css
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Le concept CSS le plus important à apprendre
seo_desc: 'By Emmanuel Ohans

  The Cascade is how CSS was designed from the very beginning, and there’s a reason
  it’s called CSS — Cascading Style Sheets!

  Sadly, CSS has a poor reputation for the same fundamental concept upon which it
  is built.

  But what exactly i...'
---

Par Emmanuel Ohans

La **Cascade** est la manière dont CSS a été conçu dès le début, et il y a une raison pour laquelle il est appelé CSS — Cascading Style Sheets !

Malheureusement, CSS a une mauvaise réputation pour le même concept fondamental sur lequel il est construit.

Mais qu'est-ce que la Cascade, et est-elle aussi mauvaise que la plupart des gens le disent ?

### Introduction

Disons que John écrit un tas de CSS, puis ouvre le navigateur pour le tester. À sa surprise, les styles qu'il a écrits ne sont pas appliqués à l'élément qu'il vient de styliser, mais d'autres styles le sont !

Vous voyez ça ? C'est l'une des pires choses dont tout le monde se plaint quand ils disent « CSS, c'est nul ».

Avec CSS, plusieurs styles peuvent affecter un seul élément. Donc, vous avez un `paragraphe` sur une page web. Mais ce `paragraphe` peut être stylisé par n'importe quel bloc CSS, littéralement.

C'est comme avoir une variable JavaScript globale qui peut être manipulée par n'importe quelle fonction dans le code. Une recette pour le désastre, semble-t-il.

Mais encore une fois, la Cascade constitue le raisonnement fondamental derrière la création de CSS.

L'accepter ?

Eh bien, vous ne pouvez pas le changer.

![Image](https://cdn-media-1.freecodecamp.org/images/QbB17Bt142xYZ-jJhnWY6obhbVf4NUnVBB6p)
_Vous y avez déjà été, n'est-ce pas ?_

### Qu'est-ce que la Cascade ?

La cascade est la manière dont le navigateur détermine quels styles appliquer à un élément particulier. C'est aussi simple que cela, et cela fait une bonne question d'entretien pour un développeur front-end.

Heureusement, les cauchemars associés à la cascade peuvent être compris, car elle est régie par seulement deux facteurs :

1. La spécificité des sélecteurs d'éléments
2. L'ordre des styles écrits

Jetons un rapide coup d'œil à ceux-ci.

### Spécificité des sélecteurs

Vous pouvez comparer la spécificité des sélecteurs à la manière dont l'esprit humain interprète les instructions.

Par exemple, considérons le graphique ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/Ns6cVPSUw99PFiQDIwswHX22V4GRGsb4BTeP)

Si je vous disais, « Passez-moi la boîte rouge. », laquelle me passeriez-vous ? Il y en a deux !

Vous pourriez poser la question suivante, « Quelle boîte, a ou b ? ».

Ou vous pourriez même prendre les deux boîtes ! Ne sont-elles pas toutes les deux des boîtes rouges ?

C'est la situation dans laquelle le navigateur se trouve lorsqu'il traite la spécificité.

Lorsque vous dites, stylisez le paragraphe avec une couleur de fond rouge...

```
p {   background-color: red;}
```

Puisqu'il peut y avoir beaucoup d'éléments de paragraphe sur la page, le navigateur se demande, « quel paragraphe ? »

Le navigateur ne peut pas vous poser de question de suivi, alors il tente de styliser **tous** les paragraphes de la page avec un fond `rouge`.

Cependant, si vous aviez précisé de styliser le paragraphe avec un nom de classe `reddy` avec un fond rouge :

```
p.reddy {  background-color: red;}
```

C'est une demande plus spécifique !

Maintenant, le navigateur stylisera le ou les éléments de paragraphe spécifiques que vous avez demandés.

C'est tout !

Techniquement, le navigateur examine chaque sélecteur qui cible un élément spécifique et attribue des « scores » à chacun d'eux, et celui avec un score de spécificité plus élevé gagne.

La manière dont il calcule les scores est simple.

Imaginez que le navigateur — tout en interprétant votre CSS — a 4 poteaux de but.

![Image](https://cdn-media-1.freecodecamp.org/images/WGT1q9oEHZrKY1R0C2neEvZb45AIN6faLSs5)

1. Pour chaque style en ligne qui cible un élément en utilisant l'attribut `style`, 1 but est attribué au poteau de but `(a)`.
2. Pour chaque sélecteur `id`, 1 but est attribué au poteau `(b)`.
3. Pour chaque sélecteur de `classe`, sélecteur d'attribut et pseudo-classes présents, 1 but est attribué au poteau `(c)`.
4. Pour chaque sélecteur d'élément et pseudo-élément, 1 but est attribué au poteau `(d)`.

La manière dont je retiens cela est en utilisant l'acronyme, SICAPEP :

![Image](https://cdn-media-1.freecodecamp.org/images/etustqZiytNdLrK6wF1nHWeWzVebiWS11SS4)

Après avoir attribué les points, les points totaux sont calculés par _concaténation_, comme des chiffres dans un nombre à 4 chiffres.

#### Un exemple rapide de spécificité

Considérons les déclarations de style suivantes :

```
#nav .removed > a:hover {}
```

```
li:last-child h3 .title {}
```

Comment le navigateur calculerait-il les « points » de spécificité pour ces sélecteurs ?

`#nav .removed > a:hover`

Voici la décomposition :

(a) Il n'y a pas de style en ligne, donc le score pour le premier poteau de but est 0.

(b) Il y a un sélecteur `id`, `#nav`, ce qui donne un score de 1 pour le deuxième poteau de but.

(c) Il y a aussi un sélecteur de `classe`, `.removed` et un sélecteur de pseudo-classe, `:hover`, ce qui donne un score de 2 pour le troisième poteau de but.

(d) Il y a un sélecteur d'élément, `a`, ce qui donne un score de 1 dans le quatrième poteau.

Voici la représentation graphique des scores.

![Image](https://cdn-media-1.freecodecamp.org/images/irhfWjR4Pr7OAMpUq8w3jwehB-N8mMV12WSA)

Le score total de spécificité est concaténé en `0121`.

Comme en mathématiques régulières, `0001` est plus petit que `0005`, et `0121` est plus grand que `0021`.

Maintenant, vous comprenez comment la spécificité est calculée.

Pouvez-vous essayer de calculer la spécificité pour l'autre sélecteur, `li:last-child h3 .title` ?

Faites-moi savoir ce que vous obtenez dans la section des commentaires :)

### Ordre des styles

Le deuxième facteur qui influence la cascade est l'ordre des styles. Un exemple vraiment basique peut être vu en stylisant le même élément dans 2 blocs de code différents.

Par exemple :

```
p.reddy {  background: red;}p.reddy {   background: blue;}
```

Même si les deux sélecteurs ont la même spécificité, `0011`, l'ordre de la règle entre en jeu.

La deuxième déclaration annulera la première, et le paragraphe sera bleu et **non** rouge.

### Question piège

En considérant le document ci-dessous, quelle serait la couleur du texte du lien ?

```
<!doctype html> <html><head><title>Styles en ligne et spécificité</title> <style type="text/css">    #nav-force &gt; ul &gt; li &gt; a.nav-link { 	color: blue;     };</style> </head>   <body>      <nav id="nav-force">	<ul> 	 <li>	  <a href="/" class="nav-link" style="color: red;">		Lien          </a> 	 </li>	</ul>       </nav>  </body> </html>
```

Bleu ou rouge ?

Notez que le lien est stylisé à la fois en ligne et dans le bloc `<style>&l`t;/style>.

Oh, si vous vous sentez confiant, dites la réponse à voix haute — pour vous-même.

Mais la vraie réponse est que le style en ligne gagne toujours. Le but est marqué dans le premier poteau, ce qui bat tous les buts dans les autres poteaux.

Pourquoi ?

La spécificité finale sera de l'ordre des milliers — 1000 — et cela bat 9 buts dans le deuxième poteau. 1000 est plus grand que 0900.

**NOTE :** Comme l'a souligné [Paul McCann](https://www.freecodecamp.org/news/the-most-important-css-concept-to-learn-8e929c944a19/undefined) dans la section des commentaires, le paragraphe ci-dessus est une simplification excessive. Jetez un coup d'œil à [ce qu'il dit](https://medium.com/@paul_mccann/be-careful-when-explaining-specificity-values-as-numbers-in-the-thousands-theyre-not-153502c3d97f).

### Conclusion

Espérons que vous êtes maintenant armé d'une solide compréhension du fonctionnement de la cascade. Apprendre des concepts CSS plus avancés sera probablement plus facile maintenant, et, plus important encore, vous savez maintenant où regarder lorsque vous avez ces bugs ennuyeux.

À plus tard !

### Prêt à devenir Pro ?

J'ai créé un guide CSS gratuit pour faire décoller vos compétences CSS, immédiatement. [Obtenez l'ebook gratuit](https://pages.convertkit.com/0c2c62e04a/60e5d19f9b).

![Image](https://cdn-media-1.freecodecamp.org/images/K5WjZdNM7UT-fafz5nc2H8q-cRcH0Dc36Aja)
_Sept secrets CSS que vous ne connaissiez pas_