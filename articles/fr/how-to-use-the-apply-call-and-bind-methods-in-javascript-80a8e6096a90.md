---
title: Comment utiliser les méthodes apply(?), call(?) et bind(→) en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-08T18:06:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-the-apply-call-and-bind-methods-in-javascript-80a8e6096a90
coverImage: https://cdn-media-1.freecodecamp.org/images/0*FzzV3ThEeCwqNKNL
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment utiliser les méthodes apply(?), call(?) et bind(→) en JavaScript
seo_desc: 'By Ashay Mandwarya ?️??

  In this article, we’ll talk about the apply, call, and bind methods of the function
  prototype chain. They are some of the most important and often-used concepts in
  JavaScript and are very closely related to the this keyword.

  S...'
---

Par Ashay Mandwarya 👨‍💻🚀

Dans cet article, nous allons parler des méthodes apply, call et bind de la chaîne de prototype de fonction. Ce sont certains des concepts les plus importants et souvent utilisés en JavaScript et sont très étroitement liés au mot-clé _this_.

Donc, pour saisir les informations de cet article, vous devez d'abord être familiarisé avec le concept et l'utilisation du mot-clé _this_. Si vous êtes déjà familiarisé avec celui-ci, vous pouvez continuer — sinon, vous pouvez vous référer à cet article [ici](https://medium.freecodecamp.org/a-guide-to-this-in-javascript-e3b9daef4df1) et puis revenir ici.

Pour apprendre sur **apply|call|bind**, nous devons aussi connaître les fonctions en JavaScript, en supposant que vous êtes familiarisé avec _this_.

### Fonctions

![Image](https://cdn-media-1.freecodecamp.org/images/EIxaDY6mTA74uZjnPlWuLJAIzhhTuxGEiVC9)
_Photo par [Unsplash](https://unsplash.com/@the_roaming_platypus?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">The Roaming Platypus</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Le constructeur Function crée un nouvel objet Function. Appeler le constructeur directement peut créer des fonctions dynamiquement, qui peuvent être exécutées dans la portée globale.

Comme les fonctions sont des objets en JavaScript, leur invocation est contrôlée par les méthodes **apply, call et bind**.

Pour vérifier si une fonction est un objet Function, nous pouvons utiliser le code dans l'extrait suivant, qui retourne vrai.

![Image](https://cdn-media-1.freecodecamp.org/images/qOSEplK6rs2hhpbJBDkiBwASvpaAnd9XW3EX)

> L'objet Function global n'a pas de méthodes ou de propriétés qui lui sont propres. Cependant, puisque c'est une fonction elle-même, elle hérite de certaines méthodes et propriétés via la chaîne de prototype de Function.prototype. — MDN

Les méthodes suivantes sont dans la chaîne de prototype de fonction :

* **Function.prototype.apply()**
* **Function.prototype.bind()**
* **Function.prototype.call()**
* Function.prototype.isGenerator()
* Function.prototype.toSource()
* Object.prototype.toSource
* Function.prototype.toString()
* Object.prototype.toString

Nous nous intéressons aux trois premières, alors commençons.

### Apply 📝

![Image](https://cdn-media-1.freecodecamp.org/images/2iPUdLujyCPb7mglSPBbmJNDoAUbrFmLcGlw)
_Photo par [Unsplash](https://unsplash.com/@anckor?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Julian O'hayon</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

> La méthode **apply()** est une méthode importante du prototype de fonction et est utilisée pour appeler d'autres fonctions avec une valeur de mot-clé _this_ fournie et des arguments fournis sous la forme d'un tableau ou d'un objet de type tableau.

Les objets de type tableau peuvent faire référence à NodeList ou à l'objet arguments à l'intérieur d'une fonction.

Cela signifie que nous pouvons appeler n'importe quelle fonction et spécifier explicitement à quoi _this_ devrait faire référence dans la fonction appelante.

#### Syntaxe

![Image](https://cdn-media-1.freecodecamp.org/images/F6MxVYBXV6R5cwxInuapX0vlxhhG8Hr5aRp6)

#### Retour

Elle retourne le résultat de la fonction qui est invoquée par _this_.

#### Description

La méthode **apply** est utilisée pour permettre à une fonction/objet appartenant à un objet x d'être appelée et assignée à un objet y.

#### Exemples

#### 1.

![Image](https://cdn-media-1.freecodecamp.org/images/BwwKE0rDKIyFmfJbiLfV-6h-sYIXXrdeD3vL)

Comme on peut le voir dans l'extrait donné, nous voyons que lorsque nous poussons un tableau à l'intérieur d'un autre, le tableau entier est traité comme un élément et poussé à l'intérieur de la variable de tableau.

Mais que faire si nous voulons que les éléments soient poussés individuellement au lieu d'un tableau ? Bien sûr, il y a littéralement n nombre de façons de le faire, mais comme nous apprenons apply, utilisons-le :

![Image](https://cdn-media-1.freecodecamp.org/images/NuH14RCGXQv2R0jiw7U34bJ2FeTonBfE3Yl8)

Dans l'exemple donné, nous pouvons voir l'utilisation de **apply** pour joindre deux tableaux donnés. Le tableau d'arguments est le tableau d'éléments et l'argument _this_ pointe vers la variable de tableau. Les éléments du tableau d'éléments sont poussés vers l'Object(_array_) auquel le _this_ est pointé. Nous obtenons le résultat comme les éléments individuels du deuxième tableau poussés vers le tableau auquel le _this_ est pointé.

#### 2.

![Image](https://cdn-media-1.freecodecamp.org/images/87MhVt1p1yejr-WnUHXElvuWx8qLgUFi4g4s)

La fonction max en JS est utilisée pour trouver l'élément avec la valeur maximale à partir d'un ensemble donné d'éléments. Mais comme nous pouvons le voir à partir de l'extrait, si les valeurs sont sous la forme d'un tableau, nous obtenons le résultat comme NaN. Bien sûr, nous parlons de JavaScript, donc encore une fois, il y a n nombre de façons de faire cela, mais utilisons apply.

![Image](https://cdn-media-1.freecodecamp.org/images/yDD0VibWncT0LGNE09uj6V0JgkEHrDRNxvY8)

Maintenant, lorsque nous utilisons apply et utilisons la fonction Math.max(), nous obtenons le résultat. Comme nous le savons, apply prendra toutes les valeurs à l'intérieur du tableau comme arguments individuels et ensuite la fonction max sera appliquée à celles-ci. Cela nous donnera la valeur maximale dans le tableau.

Une chose intéressante à souligner ici est qu'à la place de _this_, nous avons utilisé null. Comme l'argument fourni est le tableau de nombres, même si _this_ est introduit, il pointera vers le même tableau et nous obtiendrons le même résultat. Par conséquent, dans de tels cas, nous pouvons utiliser null à la place de _this_. Cela nous montre que l'argument _this_ dans la fonction apply est un argument facultatif.

### Call

![Image](https://cdn-media-1.freecodecamp.org/images/6qS5RGWz35jfeQxoKPXtxee5EYrUX0HDqrMd)
_Photo par [Unsplash](https://unsplash.com/@ericmuhr?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Eric Muhr</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

> La méthode **call()** est utilisée pour appeler une fonction avec un _this_ donné et des arguments fournis individuellement.

Cela signifie que nous pouvons appeler n'importe quelle fonction, en spécifiant explicitement la référence que _this_ devrait référencer dans la fonction appelante.

Cela est très similaire à **apply**, la seule différence étant que **apply** prend des arguments sous la forme d'un tableau ou d'objets de type tableau, et ici les arguments sont fournis individuellement.

#### Syntaxe

![Image](https://cdn-media-1.freecodecamp.org/images/huZ9MJlBZBLQHOCJqKBJN0PxhY1DtvFV0Tqg)

#### Retour

Le résultat de l'appel de la fonction avec la valeur `**this**` spécifiée et les arguments.

#### Description

La méthode **call** est utilisée pour permettre à une fonction/objet appartenant à un objet x d'être appelée et assignée à un objet y.

#### Exemples

#### 1.

![Image](https://cdn-media-1.freecodecamp.org/images/rMsi0io-O7iX5t5YqfljgTgYEC5mWTEJHXcz)

Ceci est un exemple de chaînage de constructeurs. Comme nous pouvons le voir, dans chaque fonction, le constructeur du Product est appelé, et en utilisant **call**, les propriétés de l'objet Product sont chaînées avec les objets Pizza et Toy, respectivement.

Lorsque de nouvelles instances sont créées des objets Pizza et Toy, des paramètres sont fournis comme nom, prix et catégorie. La catégorie est appliquée dans la définition seulement, mais le nom et le prix sont appliqués en utilisant le constructeur chaîné de l'objet Product, car ils sont définis et appliqués dans l'objet Product. Avec un peu plus de réglages, nous pouvons atteindre l'héritage.

#### 2.

![Image](https://cdn-media-1.freecodecamp.org/images/iVxMTwdWkE5H9tfzv-8xCm84IDJOruqEmGXS)

Dans l'extrait ci-dessus, nous avons défini une fonction appelée sleep. Elle consiste en un tableau reply qui consiste en des éléments qui adressent des propriétés en utilisant le mot-clé _this_. Ils sont définis dans un objet séparé à l'extérieur de la fonction.

La fonction sleep est appelée avec l'objet _obj_ comme argument. Comme nous pouvons le voir, les propriétés de l'_obj_ sont définies dans _this.animal_ et _this.sleepDuration_, respectivement, et nous obtenons la phrase complète comme sortie.

### Bind→

![Image](https://cdn-media-1.freecodecamp.org/images/DITA8UeL2muluoiEjqmiYAnHO9mWDYqIEr0G)
_Photo par [Unsplash](https://unsplash.com/@michaelheld?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Michael Held</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

> La méthode **bind()** crée une nouvelle fonction qui, lorsqu'elle est appelée, a son mot-clé `this` défini à la valeur fournie, avec une séquence donnée d'arguments précédant ceux fournis lorsque la nouvelle fonction est appelée. — MDN

#### Syntaxe

![Image](https://cdn-media-1.freecodecamp.org/images/CEVBSady5dOht7k7f-qex5gsTijBcqVQXobA)

#### Retour

**Bind** retourne une copie de la fonction avec le _this_ fourni et les arguments.

#### Description

La fonction **bind** est très similaire à la fonction **call**, la principale différence étant que bind retourne une nouvelle fonction alors que call ne le fait pas.

Selon les spécifications ECMAScript 5, la fonction retournée par **bind** est un type spécial d'objet fonction exotique (comme ils l'appellent) appelé la **fonction liée** **(BF)**. La BF enveloppe l'objet fonction original. Appeler une BF exécute la fonction enveloppée dans celle-ci.

#### Exemples

#### 1.

![Image](https://cdn-media-1.freecodecamp.org/images/wxd-80Uzp6j4LGZ7nOnzt6jBrJJD2-g6MpFq)
_Exemple pris de MDN_

Dans l'extrait ci-dessus, nous avons défini une variable x et un objet appelé module. Il contient également une propriété appelée _x_ et une autre propriété dont la valeur correspondante est une fonction qui retourne la valeur de _x_.

Lorsque la fonction _getX_ est appelée, elle retourne les valeurs de _x_ qui est défini à l'intérieur de l'objet et non le _x_ dans la portée globale.

Une autre variable est déclarée dans la portée globale qui appelle la fonction _getX_ de l'objet _module_. Mais comme la variable est dans la portée globale, le _this_ dans _getX_ pointe vers le _x_ global et donc 9 est retourné.

Une autre variable est définie qui appelle la fonction précédente mais cette fois lie la dite fonction avec l'objet _module_. Cette liaison retourne la valeur de _x_ à l'intérieur de l'objet. En raison de la liaison, le _this_ dans la fonction pointe vers la valeur de _x_ dans l'objet et non le _x_ global. Par conséquent, nous obtenons 81 comme sortie.

### Conclusion

Maintenant que nous avons appris les bases des méthodes, vous pourriez encore être un peu confus quant à pourquoi il y a 3 fonctions différentes faisant presque la même chose. Pour clarifier ce concept, vous devez pratiquer avec différentes situations et scénarios afin de pouvoir apprendre plus en profondeur où et comment elles peuvent être utilisées. Elles rendront certainement votre code plus propre et plus puissant.

Si vous avez aimé cet article, veuillez applaudir 👏 et suivre 🚀 pour plus.

![Image](https://cdn-media-1.freecodecamp.org/images/ueu4IJwqszzZov80yvEMaZi9e4RPClhf6sjx)
_Google_