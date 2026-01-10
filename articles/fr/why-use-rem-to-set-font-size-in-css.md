---
title: Pourquoi vous devriez utiliser rem pour définir la taille de la police en CSS
subtitle: ''
author: Vinod Mathew Sebastian
co_authors: []
series: null
date: '2023-01-17T21:33:17.000Z'
originalURL: https://freecodecamp.org/news/why-use-rem-to-set-font-size-in-css
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/em_vs_rem.png
tags:
- name: CSS
  slug: css
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Pourquoi vous devriez utiliser rem pour définir la taille de la police
  en CSS
seo_desc: 'Setting font sizes is something you''ll do often as a web developer. But
  sometimes, especially for beginners, this can get a bit tricky.

  In this article, I''ll explain why I think you should always use rem over em for
  setting the font-size of an elemen...'
---

Définir les tailles de police est quelque chose que vous ferez souvent en tant que développeur web. Mais parfois, surtout pour les débutants, cela peut devenir un peu délicat.

Dans cet article, je vais expliquer pourquoi je pense que vous devriez toujours utiliser `rem` plutôt que `em` pour définir la `font-size` d'un élément.

## Quelles sont les unités relatives en CSS ?

Pour styliser une page web, nous utilisons des unités relatives comme `em` et `rem` au lieu de mesures absolues comme `px` (pixels).

C'est parce qu'aujourd'hui, les tailles d'écran viennent en différentes tailles et formes. Si nous utilisons `px`, la taille de l'élément reste constante quelle que soit la taille de l'écran. Ainsi, l'utilisation d'unités relatives comme `em` et `rem` est considérée comme une bonne pratique. (La taille `:root` est toujours définie en `px`. Nous avons besoin d'un point de référence. N'est-ce pas ?)

Les unités CSS sont ainsi classées en deux catégories : unités absolues et unités relatives. Les pixels (`px`), les points (`pt`) et les picas (`pc`) font partie des unités absolues. Les `%`, `em`, `rem`, `vh` et `vw` sont toutes des unités relatives.

## Que sont les unités `em` et `rem` ?

En parlant de `em` et `rem`, en typographie imprimée, `em` fait référence à la largeur de la lettre majuscule 'M' de la police actuelle.

En conception web, `em` fait référence à la taille de l'élément courant. Si la taille de l'élément courant/parent n'est pas définie, elle prend généralement la valeur par défaut de la CSS du navigateur. Elle est généralement de 16px.

Le `em` n'est pas seulement pour la taille de la police. C'est une unité relative que vous pouvez utiliser pour définir les valeurs des propriétés comme font-size, margin, padding, width, height et line-height d'un élément.

Le `rem` est le `em` racine. Toutes les valeurs sont relatives au parent le plus haut, l'élément `html` ou `:root`. Si ce n'est pas explicitement défini pour l'élément `html` ou `:root`, il prend à nouveau la valeur par défaut de la CSS du navigateur : 16px.

Vous pouvez utiliser `rem` partout où vous pouvez utiliser `em`.

## Quand `rem` est-il un meilleur choix que `em` ?

Maintenant, discutons de pourquoi vous devriez toujours utiliser `rem`, au lieu de `em`, pour définir la taille de la police d'un élément en CSS.

Les styles CSS cascadent. C'est pourquoi on les appelle des feuilles de style *en cascade*. Si vous appliquez par inadvertance une `font-size` de `0.5em` à nouveau, la taille est réduite à 1/4 de l'original.

Note : Cela n'arrive que si vous utilisez des unités relatives. Même si vous appliquez une unité absolue (par exemple `16px`) un nombre quelconque de fois, par exemple, sur la `font-size`, elle restera toujours la même. Ce ne sera que des déclarations de style en double. Le navigateur l'ignore effectivement.

Laissez-moi vous montrer un exemple.

Voici une simple page web. Un seul `h1`, `p`, et une balise `a` imbriquée dans la balise `p` s'y trouvent.

```typescript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bienvenue - Différence entre l'application de em et rem</title>
</head>
<body>

<h1>La différence entre em et rem dans la taille de la police d'un élément</h1>
<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ad beatae alias adipisci placeat fuga maiores nobis aliquam, atque porro explicabo veritatis dolorum tenetur ullam in?

<a href="#">Cliquez ici !</a>

</p>

</body>
</html>
```

Par exemple, les balises `h1`, `p` et `a` se voient toutes attribuer une valeur de `font-size` de `0.5em` pour être affichées sur un écran plus petit.

```typescript
@media all and (max-width:768px){

h1{
font-size:0.50em;
}
p {
font-size:0.50em;
}
a {
font-size:0.50em;
}
}
```

Maintenant, voyez ce qui se passe. Voici la vue mobile (zoomée à 300%).

![Image](https://www.freecodecamp.org/news/content/images/2023/01/mobile_view_one-1.png align="left")

Le 'Cliquez ici !' à l'intérieur de la balise `a` est 1/4 de la taille de l'original – et il est à peine lisible.

Immédiatement après avoir appliqué `0.5em` à la balise `p`, `em` est maintenant seulement `8px`.

`16px x 0.5 = 8px`

Puisque la balise `a` est imbriquée dans la balise `p`, les deux styles cascadent.

`8px x 0.5 = 4px`

La solution est d'utiliser `rem` pour la balise `a` : `0.5rem`.

Veuillez noter que les balises `h1` et `p` utilisent `em` ici à des fins de démonstration.

```typescript
@media all and (max-width:768px){
h1{
font-size: 0.50em;
}
p { 
font-size:0.50em;
}
a {
font-size:0.50rem;
}
}
```

Puisque nous avons utilisé `rem`, la balise `a` est relative au `em` *racine* – c'est-à-dire qu'elle est définie à 16px par défaut.

`16px x 0.5 = 8px`

![Image](https://www.freecodecamp.org/news/content/images/2023/01/mobile_view_final-7.png align="left")

La balise `a` *Cliquez ici !* est maintenant stylisée de manière plus appropriée.

N'oubliez jamais qu'il est judicieux d'utiliser `rem` pour définir la taille de la police d'un élément comme vous l'avez vu ici.

## Conclusion

Dans certains cas, il est préférable d'utiliser `em`. Mais lorsque vous définissez la taille de la police d'un élément, `rem` est le meilleur choix.

Bon codage !