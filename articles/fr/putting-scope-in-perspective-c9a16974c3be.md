---
title: Mettre la portée en perspective
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2015-11-04T08:31:56.000Z'
originalURL: https://freecodecamp.org/news/putting-scope-in-perspective-c9a16974c3be
coverImage: https://cdn-media-1.freecodecamp.org/images/1*bagtQodHCv1PGtuEX5fMNA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: women in tech
  slug: women-in-tech
seo_title: Mettre la portée en perspective
seo_desc: 'By Tiffany White

  In JavaScript, lexical scope deals with where your variables are defined, and how
  they will be accessible — or not accessible — to the rest of your code.

  There are two terms to think about when talking about scope: local and global. ...'
---

Par Tiffany White

En JavaScript, la _portée lexicale_ traite de l'endroit où vos variables sont définies, et comment elles seront accessibles — ou non accessibles — au reste de votre code.

Il y a deux termes à considérer lorsque l'on parle de portée : local et global. Ces deux termes sont importants à comprendre, car l'un peut être plus dangereux que l'autre lors de la déclaration de variables et de l'exécution de votre code.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_9SDjff_XSe6Kl_LSJrsKg.jpeg)

#### Portée globale

Une variable est de portée globale si vous la déclarez en dehors de toutes vos fonctions. Par exemple :

```
// variable globale, c'est-à-dire portée globale
var a = "foo";
```

```
function myFunction() {  var b = "bar";  console.log(a+b);}
```

```
myFunction();
```

Lorsque une variable est dans la portée globale, elle peut être accessible par tout le code dans le même fichier JavaScript. Dans cet exemple, j'accède à la variable _a_ dans mon instruction console.log, à l'intérieur de la fonction _myFunction_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*QmksMiei1KJbztSbeb6cCA.jpeg)

#### Portée locale

Les variables locales n'existent qu'à l'intérieur des fonctions. Elles sont limitées à cette fonction individuelle.

Vous pouvez considérer les variables locales comme toutes les variables qui se trouvent entre une accolade ouvrante et une accolade fermante.

Ces variables locales ne peuvent pas être accessibles par le code en dehors de la fonction à laquelle elles appartiennent.

Jetez un coup d'œil à ce code :

```
// variable globale, c'est-à-dire portée globale
var a = "foo";
```

```
function myFunction() {  // variable locale, ou portée locale  var b = "bar";  console.log(a+b);}
```

```
function yourFunction() {  var c = "JavaScript est amusant !";  return c;  console.log(c);}
```

```
myFunction();
yourFunction();
```

Remarquez comment les variables sont chacune déclarées à l'intérieur de fonctions séparées. Elles sont toutes deux des variables locales, dans une portée locale, et ne peuvent pas être accessibles l'une par l'autre.

Par exemple, je ne peux pas retourner _b_ dans _yourFunction_, parce que _b_ appartient à _myFunction_. _b_ ne peut pas être accessible par _yourFunction_, et vice versa.

Si j'essayais de retourner la valeur de _b_ lors de l'appel de _yourFunction_, j'obtiendrais « erreur : b n'est pas défini ». Pourquoi ? Parce que _b_ n'appartient pas à _yourFunction_. _b_ est en dehors de la portée de _yourFunction_.

Lorsque l'on ajoute des conditionnelles imbriquées, la portée devient encore plus complexe. Mais je laisserai cela pour une autre fois.

Mais pour l'instant, rappelez-vous la différence entre la portée globale et la portée locale. Et la prochaine fois que vous obtenez une erreur « n'est pas défini », vérifiez la portée de la variable.

_Cet article apparaît également sur [https://twhite96.github.io](https://twhite96.github.io)_