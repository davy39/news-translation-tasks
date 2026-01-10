---
title: Définition des variables CSS – Qu'est-ce que les variables CSS et comment les
  utiliser ?
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2022-04-25T22:47:25.000Z'
originalURL: https://freecodecamp.org/news/what-are-css-variables-and-how-to-use-them
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/pankaj-patel-6JVlSdgMacE-unsplash.jpg
tags:
- name: CSS
  slug: css
- name: variables
  slug: variables
seo_title: Définition des variables CSS – Qu'est-ce que les variables CSS et comment
  les utiliser ?
seo_desc: "CSS variables are custom variables that you can create and reuse throughout\
  \ your stylesheet. \nIn this article, I will show you how to create CSS variables\
  \ on the :root pseudo selector and show you how to access them using the var() function.\
  \ \nHow to ..."
---

Les variables CSS sont des variables personnalisées que vous pouvez créer et réutiliser dans toute votre feuille de style.

Dans cet article, je vais vous montrer comment créer des variables CSS sur le sélecteur pseudo `:root` et vous montrer comment y accéder en utilisant la fonction `var()`.

## Comment créer une variable CSS personnalisée

Voici la syntaxe de base pour définir une variable CSS personnalisée :

```css
--nom-variable-css: valeur de la propriété css;
```

Il est considéré comme une bonne pratique de définir toutes vos variables en haut de votre feuille de style. Pour les projets plus importants, il est courant de créer un fichier séparé uniquement pour vos variables de couleur personnalisées afin de pouvoir les réutiliser dans d'autres feuilles de style.

Si vous souhaitez accéder à cette variable, vous utiliseriez alors la fonction `var()`. Voici la syntaxe de base.

```css
propriété css: var(--nom-variable-css);
```

Dans cet exemple, je souhaite créer des variables de couleur de fond et de texte personnalisées que je pourrai réutiliser dans toute la feuille de style. Je vais nommer ces variables `--main-bg-color` et `--main-text-color`.

```css
  --main-bg-color: #000080;
  --main-text-color: #fff;
```

Je vais placer ces variables à l'intérieur du sélecteur pseudo `:root` qui représente l'élément racine dans mon document HTML.

```css
:root {
  --main-bg-color: #000080;
  --main-text-color: #fff;
}
```

Dans mon sélecteur `body`, je vais référencer ces variables en utilisant la fonction `var()`.

```css
body {
  background-color: var(--main-bg-color);
  color: var(--main-text-color);
}
```

Voici un exemple fonctionnel :

%[https://codepen.io/jessica-wilkins/pen/LYeoOmP?editors=1100]

Si je voulais ajouter plus de contenu à la page, je pourrais réutiliser ces variables dans le reste de la feuille de style et éviter des répétitions inutiles comme ceci :

```css
.example-class-1 {
  background-color: #000080;
  display: flex;
  flex-direction: column;
}

.example-class-2 {
  font-size: 2.1rem;
  color: #fff;
}

.example-class-3 {
  background-color: #000080;
  color: #fff;
  border: 2px solid black;
}

```

Dans cet exemple, j'ai 6 boîtes rouges, vertes et bleues sur la page. J'ai d'abord créé le balisage HTML pour les boîtes.

```html
<div class="box-container">
  <div class="box red-box">Box 1</div>
  <div class="box green-box">Box 2</div>
  <div class="box blue-box">Box 3</div>
</div>
<div class="box-container">
  <div class="box blue-box">Box 4</div>
  <div class="box green-box">Box 5</div>
  <div class="box red-box">Box 6</div>
</div>
```

J'ai ensuite créé un ensemble de variables personnalisées pour les couleurs rouge, verte et bleue.

```css
:root {
  --maroon-red: #800000;
  --dark-green: #013220;
  --navy-blue: #000080;
  --white: #fff;
}
```

Enfin, j'ai appliqué ces variables à mes boîtes en utilisant la fonction `var()`.

```css
.red-box {
  background-color: var(--maroon-red);
}

.green-box {
  background-color: var(--dark-green);
}

.blue-box {
  background-color: var(--navy-blue);
}
```

Voici à quoi ressemble le code complet et le résultat final :

%[https://codepen.io/jessica-wilkins/pen/WNdBXXZ?editors=1100]

## Comment nommer les variables CSS

En ce qui concerne la nomination des variables, vous souhaitez choisir des noms courts et descriptifs afin que les autres développeurs sachent à quoi correspondent ces variables.

Voici un exemple de mauvais nom de variable :

```css
 background-color:var(--color);
```

Qu'est-ce que `--color` ?

Est-ce une nuance de rouge ? De vert ? De bleu ? Autre chose ?

Est-ce une couleur de fond principale ou une couleur de texte principale ?

Vous ne voulez pas que les autres développeurs doivent revenir en arrière et regarder la définition CSS pour comprendre ce que cela devrait être.

Un autre exemple : si vous créiez des variables CSS personnalisées pour différentes nuances de couleurs, vous pourriez choisir de les nommer de cette manière :

```css
:root {
  --maroon-red: #800000;
  --light-red: #ff0000;
  --crimson-red: #e32636;
}
```

Chaque développeur aura sa propre façon de nommer les variables. L'important est de se rappeler de fournir des noms descriptifs pour vos variables.

## Conclusion

Les variables CSS sont des variables personnalisées que vous pouvez créer et réutiliser dans toute votre feuille de style.

Voici la syntaxe de base pour définir une variable CSS personnalisée.

```css
--nom-variable-css: valeur de la propriété css;
```

Si vous souhaitez accéder à cette variable, vous utiliseriez alors la fonction `var()`. Voici la syntaxe de base.

```css
propriété css: var(--nom-variable-css);
```

Chaque développeur aura sa propre façon de nommer les variables, mais il est considéré comme une bonne pratique de créer des noms courts et descriptifs.

J'espère que vous avez apprécié cet article et bonne chance dans votre parcours CSS.