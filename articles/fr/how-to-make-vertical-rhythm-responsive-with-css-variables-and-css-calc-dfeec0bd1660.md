---
title: Comment rendre le rythme vertical réactif avec les variables CSS et CSS Calc
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2018-03-15T09:46:03.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-vertical-rhythm-responsive-with-css-variables-and-css-calc-dfeec0bd1660
coverImage: https://cdn-media-1.freecodecamp.org/images/1*HmE6KeYkDVD59567HTFC1w.jpeg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment rendre le rythme vertical réactif avec les variables CSS et CSS
  Calc
seo_desc: 'Vertical Rhythm is an important concept in web design. It has the ability
  to bring a design together and make different elements feel consistent on the same
  page.

  It used to be impossible to change Vertical Rhythm at different viewports, because
  we d...'
---

Le rythme vertical est un concept important dans la conception web. Il a la capacité de rassembler une conception et de rendre différents éléments cohérents sur la même page.

Il était autrefois impossible de changer le rythme vertical à différentes tailles d'écran, car nous n'avions pas les bons outils. Mais maintenant, avec CSS Calc et les propriétés personnalisées CSS, nous pouvons changer le rythme vertical à différentes tailles d'écran. Cet article explique comment.

### Calculer l'unité de rythme

**Une unité de rythme** est le multiple de base que vous utiliseriez pour le rythme vertical de votre site. **La valeur d'une unité de rythme doit être la hauteur de ligne de votre texte de corps.** [Voici pourquoi](https://zellwk.com/blog/why-vertical-rhythms/).

```
/* Une unité de rythme serait 20px * 1.4 = 28px */ html {   font-size: 20px;   line-height: 1.4; } 
```

```
p {   margin: 28px; }
```

Le calcul de l'unité de rythme devient plus facile si vous utilisez des unités relatives ([et vous devriez](https://zellwk.com/blog/responsive-typography/)). **Une unité de rythme sera toujours égale à la taille de police racine multipliée par la hauteur de ligne de votre texte de corps.**

```
/* 1 unité de rythme, calculée avec rem */ html {   line-height: 1.4; } 
```

```
p {   margin: 1.4rem; }
```

Lorsque vous créez un espace blanc, n'hésitez pas à varier le nombre d'unités de rythme. [Vous pouvez même inclure des valeurs non entières](https://zellwk.com/blog/why-vertical-rhythms/).

```
/* 2 unités de rythme */ h2 {   margin-top: 2.8rem;} 
```

```
/* 0.75 unité de rythme */ p {   margin-top: 1.05rem;}
```

### Pourquoi changer le rythme vertical à différentes tailles d'écran ?

Nous avons tendance à placer les appareils plus grands (comme les ordinateurs de bureau) plus loin que les appareils plus petits (comme les téléphones). Nous devons augmenter la taille de la police pour compenser la perte de lisibilité due à l'augmentation de la distance. Si votre utilisateur ne peut pas lire votre site confortablement, il quittera probablement, plissera les yeux ou augmentera la taille de la police de son navigateur (s'il est assez savant).

#### Un peu plus sur la lisibilité.

**La lisibilité est l'un des éléments les plus importants de la typographie web.** Elle est affectée par trois valeurs **— la taille de la police, la hauteur de ligne (ou interligne) et la longueur de ligne (ou mesure)** de votre texte. Lorsque l'un de ces éléments change, les autres peuvent devoir changer pour préserver la lisibilité.

Lorsque vous redimensionnez un navigateur d'une vue mobile à une vue de bureau, vous remarquerez que la mesure et la taille de la police changent. Par conséquent, l'interligne doit également changer. Ce concept est si important que Tim Brown a proposé l'approche [Molten leading](https://css-tricks.com/molten-leading-css/). Un exemple d'utilisation de l'interligne fluide est lorsque vous écrivez la hauteur de ligne de votre corps avec des unités de viewport.

```
/* Ceci est un exemple simple. Voir l'exemple complet dans le lien ci-dessus */ body {   font-size: calc(1em + 1vw);   line-height: calc(1.2em + 1vw); }
```

Mais le problème est que lorsque vous changez la hauteur de ligne de votre texte de corps, l'unité de rythme vertical change. Il n'y a aucun moyen d'incorporer l'interligne fluide avec le rythme vertical.

Maintenant, même si vous avez abandonné l'interligne fluide et utilisé les hauteurs de ligne standard sans unité, vous deviendrez probablement fou à cause de la quantité de duplication que vous devez créer. Cela ne vaut pas l'effort.

```
/* Changer la hauteur de ligne à différents points de rupture */ html {   line-height: 1.4; } 
```

```
@media (min-width: 600px) {   html {     line-height: 1.5;   } } 
```

```
/* Recalculer le rythme à chaque point de rupture */ p {  margin-top: 1.4rem; } 
```

```
@media (min-width: 600px) {   p {     line-height: 1.5rem;   } }
```

### Changer l'unité de rythme avec les propriétés personnalisées CSS

Les propriétés personnalisées CSS (mieux connues sous le nom de variables CSS) peuvent être utilisées pour créer une unité de rythme qui change à différentes tailles d'écran.

Pour créer une variable CSS, vous créez une propriété personnalisée (d'où son nom) en préfixant `--` à une propriété.

```
:root {   --color: red; }
```

Pour utiliser une propriété personnalisée que vous avez créée, vous écrivez `var(--your-custom-property)`.

```
p {   color: var(--color) }
```

Le grand avantage des propriétés personnalisées CSS est qu'elles peuvent être mises à jour dynamiquement dans différentes requêtes média.

```
:root {   --color: red; } 
```

```
@media (min-width: 30em) {   :root {     --color: blue;   } } 
```

```
p {   color: var(--color) }
```

![Image](https://cdn-media-1.freecodecamp.org/images/BJP2pctUsooBmEcWCUWDtYGdPvz5-H2rlhQW)

Cela signifie que vous pouvez créer une propriété `--baseline` qui correspond à une unité de rythme, puis utiliser cette propriété `--baseline` dans votre CSS pour créer un rythme vertical réactif.

```
:root {  --baseline: 1.4;   line-height: var(--baseline) } 
```

```
@media (min-width: 30em) {   :root {     /* une valeur de 3 utilisée ici pour exagérer les changements afin que vous puissiez les voir dans la démonstration ci-dessous */   --baseline: 3;   } }
```

![Image](https://cdn-media-1.freecodecamp.org/images/Q2uccjszThe-v8FzxsW6x0paXBTM60xDFJtN)

Pour créer des valeurs de rythme, vous devez utiliser CSS Calc (car vous ne pouvez calculer des choses en CSS qu'avec CSS Calc).

```
/* Deux unités de rythme */ h2 {   margin-top: calc(var(--baseline) * 2rem); } 
```

```
/* 0.75 unité de rythme */ p {   margin-top: calc(var(--baseline) * 0.75rem); }
```

![Image](https://cdn-media-1.freecodecamp.org/images/X9Vis5CeEjqSDQTolhdQfuEHmenrGwnCxBlu)

### Simplifier le calcul avec une fonction

Il peut être fastidieux d'écrire `calc` et `var` chaque fois que vous créez une valeur de rythme. Vous pouvez simplifier le calcul si vous créez une fonction dans un préprocesseur comme Sass.

```
// rvr signifie rythme vertical réactif @function rvr($multiple) {   @return calc(var(--baseline) * $multiple * 1rem); }
```

Ensuite, vous pouvez utiliser la fonction `vr` que vous avez créée comme ceci. Bien plus simple ! ?.

```
/* Deux unités de rythme */ h2 { margin-top: rvr(2); } 
```

```
/* 0.75 unité de rythme */ p { margin-top: rvr(0.75); }
```

### À quoi ressemble le support ?

Le support pour les [propriétés personnalisées CSS](https://caniuse.com/#feat=css-variables) et [CSS Calc](https://caniuse.com/#feat=calc) est excellent. Ils sont supportés dans tous les principaux navigateurs aujourd'hui.

![Image](https://cdn-media-1.freecodecamp.org/images/t6Ffa5jxIAGdcxb7zygzW-SARA940IUSwAHw)

![Image](https://cdn-media-1.freecodecamp.org/images/LPZAHT6FWEz9vbKfOMEKzIH1stAtW8u9ttc1)

Malheureusement, le support pour CSS Calc et CSS Custom est absent dans Opera Mini (ainsi que dans certains navigateurs moins connus comme QQ et Baidu), ce qui est dommage.

Puisque Opera Mini ne supporte pas CSS Calc et les propriétés personnalisées CSS, nous devons fournir des propriétés de repli chaque fois que nous créons une unité de rythme. Cela représente un peu plus de travail, mais heureusement, ce n'est pas un obstacle majeur.

```
:root {   --baseline: 1.4;   /* Hauteur de ligne de repli */   line-height: 1.4;   line-height: calc(var(--baseline) * 1); } 
```

```
@media (min-width: 30em) {   :root {     --baseline: 1.5;   } } 
```

```
p {   /* Hauteur de ligne de repli pour le rythme vertical de base. */   margin-top: 1.05rem;   margin-top: rvr(0.75); }
```

Pour simplifier, vous pouvez également créer une fonction `vr` qui calcule le rythme vertical en fonction de la valeur de hauteur de ligne de base. Voici une version simple que vous pouvez utiliser (spécifiquement pour cet exemple). Si vous souhaitez une version plus complète, consultez [Typi](https://github.com/zellwk/typi), qui est une bibliothèque que j'ai créée pour aider à simplifier la typographie réactive.

```
@function vr($multiple) {   @return 1.4 * $multiple * 1rem; }
```

Si vous créez la fonction `vr`, votre repli de rythme serait plus simple :

```
p {   /* Hauteur de ligne de repli pour le rythme vertical de base. */   margin-top: vr(0.75);   margin-top: rvr(0.75); }
```

Note : Je n'ai pas encore inclus le rythme vertical réactif dans Typi. J'espère l'ajouter lorsque j'aurai un peu de temps.

### Conclusion

Le rythme vertical est un principe typographique important auquel nous devons prêter attention en tant que concepteurs et développeurs. Malheureusement, nous ne pouvions pas lui accorder autant d'attention que nous le souhaitions auparavant, car nous manquions des outils pour le faire.

Mais maintenant, nous pouvons créer un rythme vertical réactif avec l'aide des propriétés personnalisées CSS et de CSS Calc. Si vous créez un rythme vertical réactif, assurez-vous de fournir un repli pour les navigateurs qui ne supportent pas les propriétés personnalisées CSS et CSS Calc !

Merci d'avoir lu. Cet article vous a-t-il aidé d'une manière ou d'une autre ? Si c'est le cas, [j'espère que vous envisagerez de le partager](http://twitter.com/share?text=Responsive%20Vertical%20Rhythm%20with%20CSS%20Custom%20Properties%20and%20CSS%20Calc%20by%20@zellwk%20?%20&url=https://zellwk.com/blog/responsive-vertical-rhythm/&hashtags=); vous pourriez aider quelqu'un qui se sentait de la même manière que vous avant de lire l'article. Merci.

*Initialement publié sur [zellwk.com](https://zellwk.com/blog/responsive-vertical-rhythm/).