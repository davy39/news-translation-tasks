---
title: Comment créer un nouveau contexte d'empilement avec la propriété Isolation
  en CSS
subtitle: ''
author: Natalie Pina
co_authors: []
series: null
date: '2022-03-11T20:03:45.000Z'
originalURL: https://freecodecamp.org/news/the-css-isolation-property
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/stacked.jpg
tags:
- name: CSS
  slug: css
seo_title: Comment créer un nouveau contexte d'empilement avec la propriété Isolation
  en CSS
seo_desc: "What is the CSS Isolation Property?\nIn CSS, you can use the isolation\
  \ property to create a new stacking context. Here's what that looks like:\n.container-for-new-stacking-context\
  \ {\n  isolation: isolate;\n}\n\nThe default value for isolation is auto, whic..."
---

## Qu'est-ce que la propriété CSS Isolation ?

En CSS, vous pouvez utiliser la propriété `isolation` pour créer un nouveau contexte d'empilement. Voici à quoi cela ressemble :

```css
.conteneur-pour-nouveau-contexte-dempilement {
  isolation: isolate;
}
```

La valeur par défaut pour `isolation` est `auto`, ce qui est un peu plus nuancé car un contexte d'empilement _peut_ être créé – mais cela dépend des propriétés de l'élément et si elles l'exigent. 

Vous pouvez également définir la valeur sur `inherit`, `initial`, `revert`, ou `unset`. 

Utiliser `isolation: isolate;` est un moyen définitif de créer un nouveau contexte d'empilement. 

## Qu'est-ce que le contexte d'empilement ?

![Image](https://www.freecodecamp.org/news/content/images/2022/01/doll-g9145bb1e2_1280.jpg)

En CSS, le contexte d'empilement permet littéralement aux éléments HTML d'être empilés avec leur position de départ basée sur un élément de base qui fournit le contexte.

Les éléments sont placés le long d'une matrice imaginaire avec un axe x et un axe y. Il y a aussi un axe z, dans lequel les éléments peuvent être placés devant ou derrière les uns les autres. La propriété `z-index` est couramment utilisée pour placer les éléments le long de l'axe z. 

Gardez à l'esprit que lorsque l'élément HTML racine est rendu, il vient avec un contexte d'empilement racine/global.

Il existe de nombreuses façons de créer des contextes d'empilement dans le contexte d'empilement global. Une façon courante est d'utiliser `position: relative` avec `z-index`. 

Utiliser `position: sticky` ou `fixed` fonctionne, mais cela sortira les éléments du flux de disposition et nécessitera des propriétés supplémentaires pour un placement souhaité. 

Vous pouvez également utiliser `transform`, `clip-path`, ou `filter` pour faciliter l'empilement. Pour voir toutes les façons dont le contexte d'empilement peut être formé, lisez plus sur [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Positioning/Understanding_z_index/The_stacking_context).

Les contextes d'empilement peuvent contenir des contextes d'empilement internes ultérieurs, et continuer à s'imbriquer davantage. Cela peut être un peu trop _Inception_-like à conceptualiser, alors passons à pourquoi cela est utile.

## Le trou noir du Z-Index

![Image](https://www.freecodecamp.org/news/content/images/2022/01/wormhole-g9c2a60580_1280.png)

Utiliser `z-index` peut être difficile à maintenir. Vous devez être très prudent quant à l'endroit où vous l'utilisez et aux valeurs que vous lui attribuez. 

Les systèmes de conception peuvent aider à résoudre les problèmes liés à cela. Créer un ensemble de valeurs réutilisables et documenter dans quels cas elles doivent être utilisées peut être vraiment utile. Par exemple, réserver vos valeurs de variable les plus élevées pour les modales et autres éléments qui prendront toujours le contrôle de toute la page. 

Mais la plupart du temps, nous essayons simplement de faire en sorte que notre style apparaisse comme nous le voulons. Ce qui peut signifier prescrire des valeurs `z-index` arbitraires et continuer à augmenter ces valeurs jusqu'à ce qu'elles fonctionnent. 

J'ai rencontré l'infâme `z-index: 999999;` à plusieurs reprises. Retracer ces valeurs aléatoires et créer un nouvel ordre peut devenir ardent. Cela peut conduire à des problèmes difficiles à déboguer. 

Plus les nombres que vous commencez à utiliser sont élevés, plus vous pouvez aller profondément dans le trou noir et plus il est difficile de s'en sortir plus tard.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/zindex.svg)

### Gardez-le simple avec Isolation

Définir la propriété d'isolation sur isolate est une solution simple qui peut créer un nouveau contexte d'empilement sans avoir recours à `z-index` pour placer les éléments les uns devant les autres.

Vous pouvez utiliser l'isolation sur des éléments positionnés statiquement et cela n'affectera pas les éléments enfants. C'est un excellent moyen de créer une base isolée pour contenir les éléments enfants. La propriété d'isolation est également largement [prise en charge](https://caniuse.com/?search=isolation). 

![Image](https://www.freecodecamp.org/news/content/images/2022/01/isolation-3.svg)

Pour rappel, voici la syntaxe pour cela :

```css
.conteneur-pour-nouveau-contexte-dempilement {
  isolation: isolate;
}
```

## Pour résumer :

Définir `isolation: isolate;` créera un nouveau contexte d'empilement pour les éléments enfants lorsqu'il est appliqué à un élément de niveau supérieur. 

Si vous avez trouvé cet article utile, n'hésitez pas à me contacter sur Twitter [@ui_natalie](https://twitter.com/ui_natalie). Bon empilement ! 

### Ressources

* [MDN Web Docs - Isolation](https://developer.mozilla.org/en-US/docs/Web/CSS/isolation)
* [MDN Web Docs - Le contexte d'empilement](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Positioning/Understanding_z_index/The_stacking_context)
* [What The Heck, z-index??](https://www.joshwcomeau.com/css/stacking-contexts/)