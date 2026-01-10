---
title: Pourquoi les points-virgules explicites sont importants en JavaScript
subtitle: ''
author: Shruti Kapoor
co_authors: []
series: null
date: '2019-02-03T20:55:20.000Z'
originalURL: https://freecodecamp.org/news/codebyte-why-are-explicit-semicolons-important-in-javascript-49550bea0b82
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zX_jJO9HQX5r3WQzQe6xNQ.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Pourquoi les points-virgules explicites sont importants en JavaScript
seo_desc: 'I am in "Effective JavaScript" training at @PayPalEng by Douglas Crockford
  and cannot express what an enlightening experience it has been! I realized today
  why using explicit semi-colons is so important in JS. Will share my insights soon.
  #javascript...'
---

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">I am in &quot;Effective JavaScript&quot; training at <a href="https://twitter.com/PayPalEng?ref_src=twsrc%5Etfw">@PayPalEng</a> by Douglas Crockford and cannot express what an enlightening experience it has been! I realized today why using explicit semi-colons is so important in JS. Will share my insights soon. <a href="https://twitter.com/hashtag/javascript?src=hash&amp;ref_src=twsrc%5Etfw">#javascript</a> <a href="https://twitter.com/hashtag/webdevelopment?src=hash&amp;ref_src=twsrc%5Etfw">#webdevelopment</a> <a href="https://twitter.com/hashtag/PayPal?src=hash&amp;ref_src=twsrc%5Etfw">#PayPal</a></p>&mdash; Shruti Kapoor (@shrutikapoor08) <a href="https://twitter.com/shrutikapoor08/status/1067685062806630400?ref_src=twsrc%5Etfw">November 28, 2018</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


#### Pièges où l'insertion automatique de points-virgules peut entraîner des bugs

J'ai suivi une formation Effective JavaScript par [Douglas Crockford](http://crockford.com) il y a quelques mois. Une chose qui m'est restée depuis lors est l'importance d'utiliser des points-virgules explicites en JavaScript. Pendant un certain temps, j'ai évité paresseusement d'écrire le `;` et j'ai supposé que le parseur ferait correctement le travail pour moi. Dans cet article, je veux présenter quelques exemples qui ont changé ma façon de penser.

![Image](https://cdn-media-1.freecodecamp.org/images/1*zX_jJO9HQX5r3WQzQe6xNQ.png)

### Exemple 1

Quel résultat attendez-vous de ce code ?

```javascript
const test = () => {
 return 
 {
  ok : true
 }
}
console.log(test())
```

Vous pourriez vous attendre à ce que le résultat soit un `object` avec une propriété `ok` définie sur `true`. Mais au lieu de cela, le résultat est `undefined`. Cela est dû au fait que, puisque l'accolade commence sur une nouvelle ligne, la complétion automatique des points-virgules modifie le code ci-dessus comme suit :

```javascript
const test = () => {
 return;
 {
  ok : true
 }
}
```

**Correction** : Utilisez des accolades à droite du return et des points-virgules explicites :

```javascript
const test = () => {
 return {
  ok : true
 }
};
```

### Exemple 2

```javascript
const a = 1
const b = 2
(a+b).toString()
```

Que pensez-vous qu'il se passe dans le code ci-dessus ? Nous obtenons une erreur `Uncaught ReferenceError: b is not defined.` Cela est dû au fait que la parenthèse à la troisième ligne est interprétée comme un argument de fonction. Ce code est converti en ceci :

```javascript
const a = 1;
const b = 2(a+b).toString();
```

> Dans les circonstances où une instruction d'affectation doit commencer par une parenthèse gauche, il est conseillé au programmeur de fournir un point-virgule explicite à la fin de l'instruction précédente plutôt que de compter sur l'insertion automatique de points-virgules.  
>   
>  ECMA-International.org

J'ai appris à être prudent lorsque j'utilise l'insertion automatique de points-virgules.

### Lectures complémentaires 

1. [Règles d'insertion automatique de points-virgules](http://www.ecma-international.org/ecma-262/5.1/#sec-7.9)
2. [Article de blog de Bradley Braithwaite inspiré par la même conférence](http://www.bradoncode.com/blog/2015/08/26/javascript-semi-colon-insertion/)

### Avez-vous appris quelque chose de nouveau ? Avez-vous des commentaires ? Connaissez-vous une DevJoke ? [Tweetez-moi @shrutikapoor08](https://twitter.com/shrutikapoor08)



<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">&quot;I always tell women: when you get to the top, get back in the elevator and bring a woman up with you&quot; - Eunice Kennedy Shriver. Words of wisdom. <a href="https://twitter.com/hashtag/fempire?src=hash&amp;ref_src=twsrc%5Etfw">#fempire</a> <a href="https://twitter.com/hashtag/womenintech?src=hash&amp;ref_src=twsrc%5Etfw">#womenintech</a> <a href="https://twitter.com/hashtag/womenleaders?src=hash&amp;ref_src=twsrc%5Etfw">#womenleaders</a></p>&mdash; Shruti Kapoor (@shrutikapoor08) <a href="https://twitter.com/shrutikapoor08/status/1086029796100923397?ref_src=twsrc%5Etfw">January 17, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>