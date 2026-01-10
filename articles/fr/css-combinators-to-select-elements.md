---
title: Comment utiliser les combinateurs CSS pour sélectionner et styliser des éléments
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-09-21T23:17:05.000Z'
originalURL: https://freecodecamp.org/news/css-combinators-to-select-elements
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/image--4-.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: Comment utiliser les combinateurs CSS pour sélectionner et styliser des
  éléments
seo_desc: 'By Dillion Megida

  Combinators allow you to combine multiple selectors to target specific elements
  in the DOM. In this article, I''ll explain how four of these combinators with examples.

  In my previous post on CSS Selector Types, I shared seven types o...'
---

Par Dillion Megida

Les combinateurs vous permettent de combiner plusieurs sélecteurs pour cibler des éléments spécifiques dans le DOM. Dans cet article, j'expliquerai le fonctionnement de quatre de ces combinateurs avec des exemples.

Dans mon précédent article sur les [Types de sélecteurs CSS](https://www.freecodecamp.org/news/how-to-select-elements-to-style-in-css/), j'ai partagé sept types de sélecteurs pour cibler les éléments que vous souhaitez styliser. 

Si vous n'avez pas vu cet article, je vous recommande de le lire avant de parcourir celui-ci.

Dans ce tutoriel, je parle des **Combinateurs** qui vous permettent d'utiliser plusieurs types de sélecteurs pour sélectionner des éléments. Cette sélection est basée sur la relation entre les éléments qui correspondent aux multiples types de sélecteurs spécifiés.

Il existe une [version vidéo](https://www.youtube.com/watch?v=ZKRRUUPl8SA) pour cet article si vous préférez.

Voici quatre combinateurs en CSS et leur fonctionnement.


## 1. Comment utiliser le combinateur descendant

Ce combinateur vous permet de sélectionner un élément qui est un descendant d'un autre élément. Les « descendants » ici peuvent être des enfants, des petits-enfants, des arrière-petits-enfants, et ainsi de suite.

Pour utiliser ce combinateur, vous insérez un **espace vide** entre les sélecteurs comme ceci :

```css
.container p {
  color: red;
}
```

Cette déclaration de style ci-dessus sélectionne les éléments `p` qui sont des descendants d'éléments ayant la classe **container**. 

Voici comment cela fonctionne avec le HTML suivant :

```html
<p>Je suis le premier p</p>

<div class='container'>
    <p>Je suis le deuxième p</p>
    
    <div>
        <p>Je suis le troisième p</p>
    </div>
</div>

<p>Je suis le dernier p</p>
```

Le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-396.png)

D'après le résultat ci-dessus, vous pouvez voir que les deuxième et troisième `p` sont stylisés. C'est parce qu'ils sont tous deux des descendants de l'élément `.container`. Le deuxième `p` est un enfant direct tandis que le troisième `p` est un petit-enfant (enfant direct du `div`), mais ils sont tous deux des descendants.

Vous pouvez également utiliser le combinateur descendant avec plusieurs sélecteurs comme ceci :

```css
.container div p {
  color: red;
}
```

Le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-405.png)

Comme vous pouvez le voir, seul le troisième `p` est stylisé car c'est l'élément qui est un descendant d'un élément `div` qui est lui-même un descendant de l'élément de classe **container**.

## 2. Comment utiliser le combinateur d'enfant

Le combinateur descendant correspond à un enfant, un petit-enfant, et ainsi de suite. Le combinateur d'enfant sélectionne les éléments qui sont des enfants directs d'un autre élément. 

Vous utilisez le symbole **supérieur à** (**>**) entre les sélecteurs pour spécifier qu'un sélecteur est un enfant direct de l'autre.

Voici un exemple :

```css
.container > p {
  color: red;
}
```

Ce style sélectionnera tous les éléments `p` qui sont des enfants directs des éléments ayant la classe **container**. Voyons comment cela fonctionne avec l'exemple HTML ci-dessus :

```html
<p>Je suis le premier p</p>

<div class='container'>
    <p>Je suis le deuxième p</p>
    
    <div>
        <p>Je suis le troisième p</p>
    </div>
</div>

<p>Je suis le dernier p</p>
```

Le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-397.png)

Comme vous le voyez ici, seul le deuxième `p` est affecté. Même si les deuxième et troisième éléments `p` sont des descendants de l'élément de classe **container**, seul le deuxième est un enfant direct, comme nous l'avons spécifié dans le CSS.

Vous pouvez également utiliser plusieurs sélecteurs avec ce combinateur comme ceci :

```css
.container > div > p {
  color: red;
}
```

Ce style correspondra à tous les éléments `p` qui sont des enfants directs d'éléments `div` qui sont à leur tour des enfants directs d'éléments de classe **container**.

## 3. Comment utiliser le combinateur de frères

Nous avons examiné les descendants, maintenant qu'en est-il des frères (siblings) – tout comme dans un cadre familial ? Le combinateur de frères utilisé entre les sélecteurs correspond aux éléments qui sont frères d'un autre élément.

Pour utiliser ce combinateur, vous insérez le symbole **tilde** (**~**). Voici un exemple :

```css
div ~ p {
  color: red;
}
```

Ce style sélectionne tous les éléments `p` qui sont des frères d'éléments `div`. Disons que nous avons le HTML suivant :

```html
<p>Je suis le premier p</p>

<div class='container'>
    <p>Je suis le deuxième p</p>
    
    <div>
        <p>Je suis le troisième p</p>
    </div>
</div>

<p>Je suis le dernier p</p>
<p>Je suis le tout dernier p</p>
```

Le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-399.png)

Les deux derniers `p` ont le style de couleur. Cela se produit parce que le `div` (qui a la classe **container**) a ces `p` comme frères.

Cependant, si vous remarquez bien, le premier `p` est également un frère de ce `div`. Alors pourquoi n'est-il pas stylisé ?

La raison en est que, dans notre CSS, nous avons utilisé le combinateur de frères comme ceci :

```css
div ~ p
```

Cette sélection signifie qu'elle ne sélectionnera que les frères `p` qui se trouvent **APRÈS** les éléments `div`. Les frères placés avant ne sont pas affectés.

Si la sélection change en :

```css
p ~ div
```

Alors elle sélectionnera les frères `div` qui se trouvent **APRÈS** les éléments `p`.

## 4. Comment utiliser le combinateur adjacent

Ce combinateur est similaire au combinateur de frères. La différence est que, alors que le combinateur de frères correspond à tous les frères qui viennent APRÈS un élément, le combinateur adjacent ne correspond qu'au frère **IMMÉDIAT** qui vient après un élément.

Pour utiliser ce combinateur, vous utilisez le symbole **plus** (**+**) comme ceci :

```css
div + p {
  color: red;
}
```

Ce style affecte les éléments `p` qui sont des frères IMMÉDIATS après les éléments `div`. Reprenons l'exemple HTML précédent :

```html
<p>Je suis le premier p</p>

<div class='container'>
    <p>Je suis le deuxième p</p>
    
    <div>
        <p>Je suis le troisième p</p>
    </div>
</div>

<p>Je suis le dernier p</p>
<p>Je suis le tout dernier p</p>
```

Le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-400.png)

D'après ce résultat, vous pouvez voir que seul le quatrième `p` est stylisé. C'est parce que cet élément `p` est un frère immédiat après l'élément `div` dans notre code HTML.

Même si le dernier `p` est également un frère après l'élément `div`, il n'est pas un élément adjacent au `div`.

## Conclusion

Comme nous l'avons vu dans cet article, les combinateurs vous permettent d'utiliser plusieurs types de sélecteurs. En fonction de la relation entre les éléments du DOM qui correspondent à ces sélecteurs, vous pouvez cibler des éléments à styliser.

Les combinateurs que nous avons vus sont :

* **Combinateur descendant** : pour sélectionner des éléments qui sont des descendants d'autres éléments
* **Combinateur d'enfant** : pour sélectionner des éléments qui sont des enfants directs d'autres éléments
* **Combinateur de frères** : pour sélectionner des éléments qui sont des frères après d'autres éléments
* **Combinateur adjacent** : pour sélectionner des éléments qui sont des frères immédiats après d'autres éléments

Si vous avez apprécié et appris de cet article, n'hésitez pas à le partager avec d'autres 💜.