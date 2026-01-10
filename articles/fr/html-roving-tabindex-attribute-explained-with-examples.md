---
title: Attribut HTML Roving tabindex Expliqué avec des Exemples
subtitle: ''
author: Spruce Emmanuel
co_authors: []
series: null
date: '2021-06-14T20:15:00.000Z'
originalURL: https://freecodecamp.org/news/html-roving-tabindex-attribute-explained-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/photo-1578401058525-35aaec0b4658--1-.jpeg
tags:
- name: Accessibility
  slug: accessibility
- name: CSS
  slug: css
- name: HTML
  slug: html
seo_title: Attribut HTML Roving tabindex Expliqué avec des Exemples
seo_desc: 'Have you ever used the CSS order or direction properties? You''ve probably
  used them dozens of times, but did you realize that these properties will cause
  a disconnect between what''s being displayed and what''s actually in the DOM?


  Using the order pro...'
---

Avez-vous déjà utilisé les propriétés CSS `order` ou `direction` ? Vous les avez probablement utilisées des dizaines de fois, mais avez-vous réalisé que ces propriétés provoquent une déconnexion entre ce qui est affiché et ce qui se trouve réellement dans le DOM ?

> L'utilisation de la propriété order crée une déconnexion entre la présentation visuelle du contenu et l'ordre du DOM. – Documentation MDN

Alors que je recréais l'interface "Twitter Customize Theme UI", je suis tombé sur cette étrange incohérence lorsque j'ai changé la direction d'un élément en utilisant `dir="rtl"`.

Cela s'est produit parce que l'élément ne change que la direction visuellement, tandis que le HTML reste le même. Cela a fait que ma navigation au clavier commençait par l'arrière.

%[https://youtu.be/sAC37rF7aA] 

Nous pouvons corriger cette étrange déconnexion avec `tabindex`. Mais utiliser `tabindex` avec une valeur autre que `0` est fortement déconseillé et mal vu par de nombreux développeurs (y compris moi).

Nous allons donc corriger cela en utilisant une technique appelée **Roving tabindex**. Mais avant d'examiner cette technique, rafraîchissons d'abord nos mémoires sur ce que fait l'attribut HTML `tabindex`.

### Attribut HTML Tabindex

Vous utilisez l'attribut HTML `tabindex` pour définir la position de tabulation d'un élément, et il indique généralement qu'un élément peut être tabulé avec la touche `Tab`.

`tabindex` n'accepte que des entiers comme valeur de `0` à `32767`. Si vous ne spécifiez pas de valeur, il prend la valeur par défaut de `0`.

`tabindex="0"` placera n'importe quel élément dans l'ordre de tabulation naturel :

`<span tabindex="0"> Maintenant je suis dans l'ordre de tabulation naturel <span>`

`tabindex="-1"` retirera un élément de l'ordre de tabulation naturel :

`<button tabindex="0"> Je ne fais plus partie de l'ordre de tabulation naturel </button>`

Un `tabindex` supérieur à `0` déplacera un élément à l'avant de l'ordre de tabulation naturel.

Si vous n'êtes pas familier avec l'attribut `tabindex`, vous pouvez en lire plus à ce sujet [ici](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/tabindex).

## Qu'est-ce qu'un Roving Tabindex ?

Maintenant que nous avons examiné `tabindex`, qu'est-ce que la technique du roving tabindex ?

Un roving tabindex définit essentiellement le `tabindex` à `-1` pour tous les enfants de l'élément, sauf pour celui qui est actuellement focalisé.

```html
<div class"btns js-btns"> 
    <button tabindex="0"> actuellement focalisé </button> 
    <button tabindex="-1"> bouton suivant </button> 
    ... 
</div>
```

Ensuite, en utilisant un `EventListener`, nous pouvons déterminer quel bouton est actuellement focalisé. Lorsque l'événement se déclenche, définissez le `tabindex` du bouton précédemment focalisé à `-1`, puis définissez le `tabindex` de l'enfant suivant (à focaliser) à `0` et appelez la méthode `focus()` sur celui-ci. Faites cela de manière répétée jusqu'à atteindre le dernier.

Voici un guide plus détaillé sur la méthode [**roving tabindex**](https://developers.google.com/web/fundamentals/accessibility/focus/using-tabindex).

### Comment Utiliser le Roving Tab Index

Appliquons cette méthode au comportement déconnecté étrange que nous obtenons lorsque nous utilisons l'attribut `dir="rtl"` en HTML.

Nous utilisons l'attribut `dir="rtl"` pour inverser (visuellement) l'`order` du code HTML ci-dessous (ce qui est équivalent à utiliser la propriété `direction` en CSS).

Si vous n'êtes pas sûr ou peu familier avec l'attribut `dir` en HTML, vous pouvez [en lire plus ici](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/dir).

```html
<div class="btns js-btns" dir="rtl"> 
    <button="btn js-btn" aria-label="nom du bouton"> bouton </button> 
    <button="btn js-btn" aria-label="nom du bouton"> bouton </button> 
    <button="btn js-btn" aria-label="nom du bouton"> bouton </button> 
    <button="btn js-btn" aria-label="nom du bouton"> bouton </button> 
    <button="btn js-btn" aria-label="nom du bouton"> bouton </button> 
</div>
```

Tout d'abord, nous ajoutons l'attribut `tabindex` à tous les boutons et définissons sa valeur à `-1` :

```js
let btns = document.querySelectorAll("button"); 
btns.forEach((btn, index) => { 
// définir le tabindex du premier bouton à 0 
// et définir le tabindex de tous les autres boutons à -1 
if (index == btns.length - 1) { 
btn.setAttribute("tabindex", 0); 
} else { 
btn.setAttribute("tabindex", -1); 
}
```

Remarquez comment nous définissons d'abord le `tabindex` du dernier élément à `0` (`if (index == btns.length - 1)`). Visuellement, c'est le premier élément qu'un utilisateur voit, en raison de l'attribut `dir="rtl"` que nous avons défini sur le HTML :

```html
<div class="btns js-btns" dir="rtl"> 
    //boutons 
</div>
```

Nous ajoutons ensuite un `EventListener` où nous définissons le `tabindex` du bouton actuellement focalisé à `-1`. Nous continuons à définir le `tabindex` de l'enfant suivant à `0` de manière répétée jusqu'à ce qu'il atteigne le dernier. Ensuite, il déplace le focus vers le premier et vice versa.

```js
// ajouter un écouteur d'événement lorsque la touche tab est pressée 
btn.addEventListener("keydown", (e) => { 
if (e.keyCode == 9) { 
// empêcher le comportement par défaut 
e.preventDefault(); 
// définir le tabindex du bouton actuel à 0 
btn.setAttribute("tabindex", -1); 
// si ce n'est pas le dernier bouton, continuer à définir le tabindex à 0 
if (btn.previousElementSibling != null) { 
let nextEl = btn.previousElementSibling; 
nextEl.setAttribute("tabindex", 0); 
nextEl.focus(); 
} else { 
// lorsque nous atteignons le dernier élément, définir le premier élément à tabindex 0 
// et appeler la méthode focus sur celui-ci. 
// noter le .lastElementChild, le dernier élément devient notre premier 
// c'est à cause de la direction que nous avons changée 
let firstEl = document.querySelector(".js-btns").lastElementChild; firstEl.setAttribute("tabindex", 0); firstEl.focus(); 
} 
} 
});
});
```

Et après tout cela, le code ressemble maintenant à ceci :

```js
let btns = document.querySelectorAll("button"); 
btns.forEach((btn, index) => { 
// définir le tabindex du premier bouton à 0 
// et définir le tabindex de tous les autres boutons à -1 
if (index == btns.length - 1) { 
btn.setAttribute("tabindex", 0); 
} else { 
btn.setAttribute("tabindex", -1); 
} 
// ajouter un écouteur d'événement lorsque la touche tab est pressée 
btn.addEventListener("keydown", (e) => { 
if (e.keyCode == 9) { 
// empêcher le comportement par défaut 
e.preventDefault(); 
// définir le tabindex du bouton actuel à 0 
btn.setAttribute("tabindex", -1); 
// si ce n'est pas le dernier bouton, continuer à définir le tabindex à 0 
if (btn.previousElementSibling != null) { 
let nextEl = btn.previousElementSibling; 
nextEl.setAttribute("tabindex", 0); 
nextEl.focus(); 
} else { 
// lorsque nous atteignons le dernier élément, définir le premier élément à tabindex 0 
// et appeler la méthode focus sur celui-ci. 
// noter le .lastElementChild, le dernier élément devient notre premier 
// c'est à cause de la direction que nous avons changée 
let firstEl = document.querySelector(".js-btns").lastElementChild; firstEl.setAttribute("tabindex", 0); 
firstEl.focus(); 
} 
} 
});
}); 
```

Voici une version fonctionnelle de cela sur Codepen (essayez de naviguer en utilisant votre clavier). Vous pouvez également voir la démonstration en direct de l'interface Twitter Customize UI terminée sur [Spruce.com.ng](http://Spruce.com.ng) en cliquant sur le bouton de thème.

%[https://codepen.io/Spruce_khalifa/pen/BaQemGw] 



Mais attendez une seconde – avant de décider d'utiliser cette technique, rappelez-vous que presque toutes les implémentations de design ont un coût. Examinons donc les avantages et les inconvénients de l'utilisation de la technique du roving tabindex :

### Avantages du roving tabindex :

1. Améliore les problèmes d'expérience de navigation au clavier
    
2. Corrige le problème de déconnexion de l'ordre causé par le changement de direction
    

### Inconvénients du roving tabindex :

1. Dépend uniquement de JavaScript – si l'utilisateur désactive JavaScript pour une raison quelconque, la navigation au clavier créerait une expérience étrange à nouveau.
    
2. Aucun support pour les utilisateurs de technologies d'assistance
    

## Conclusion

Il n'y a pas de manière particulière ou préférée pour implémenter la technique du roving tabindex. Donc, peu importe comment vous décidez d'écrire et d'implémenter votre code, c'est parfaitement bien, tant que vous suivez ces procédures :

1. Définir tous les `tabindex` des éléments à `-1` sauf le premier
    
2. Ajouter un écouteur d'événement clavier pour déterminer quel élément est focalisé
    
3. Définir le `tabindex` de l'enfant précédemment focalisé à `-1`
    
4. Ensuite, définir le `tabindex` de l'enfant suivant à `0`
    
5. Appeler la méthode `focus()` sur celui-ci
    

Si vous avez trouvé ce tutoriel utile, veuillez me suivre sur Twitter [@sprucekhalifa](https://twitter.com/sprucekhalifa).