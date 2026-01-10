---
title: Arrière-plan transparent – Opacité des images en CSS et HTML
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-09-15T17:05:14.000Z'
originalURL: https://freecodecamp.org/news/transparent-background-image-opacity-in-css-and-html
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/frozen-bubble-1943224_1280.jpg
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Arrière-plan transparent – Opacité des images en CSS et HTML
seo_desc: 'Transparency plays an important role in front end development. It lets
  you choose how transparent the elements on your web pages appear.

  You can adjust transparency in several ways – because of course, in CSS, there are
  multiple ways to do the same t...'
---

La transparence joue un rôle important dans le développement front-end. Elle vous permet de choisir à quel point les éléments de vos pages web apparaissent transparents.

Vous pouvez ajuster la transparence de plusieurs manières – car bien sûr, en CSS, il existe plusieurs façons de faire la même chose.

La propriété CSS `opacity` est la première méthode qui pourrait vous venir à l'esprit pour changer la transparence. Mais cette propriété ne peut pas toujours venir à la rescousse, surtout lorsqu'il y a une image de fond avec du texte que vous souhaitez rendre transparent.

Alors dans cet article, je vais vous montrer les différentes façons d'ajuster la transparence afin que vous puissiez commencer à l'implémenter dans vos projets de codage.

## Transparence des images avec la propriété CSS Opacity

Pour rendre une image transparente, vous pouvez utiliser la propriété CSS `opacity`, comme je l'ai mentionné ci-dessus. La syntaxe de base de la propriété opacity est montrée dans l'extrait de code ci-dessous :

```css
selector {
          opacity: value;
      }
```

La propriété opacity prend des valeurs de `0.0` à `1.0`, avec `1` étant la valeur par défaut pour tous les éléments. Plus la valeur est basse, plus c'est transparent. Donc si un élément est donné une opacité de `0`, il serait invisible.

Vous pouvez trouver des exemples de différentes valeurs d'opacité dans les extraits de code ci-dessous :

```html
<img src="freecodecamp.png" alt="freecodecamp-logo" />
```

J'ai ajouté un peu de CSS pour centrer tout sur la page :

```css
body {
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto;
        height: 100vh;
      }


 img {
        opacity: 1;
      }
```

Une valeur d'opacité de `1` est la valeur par défaut, donc l'image apparaît comme ceci :
![default-opacity](https://www.freecodecamp.org/news/content/images/2021/09/default-opacity.png)

```css
img {
     opacity: 0.5;
   }
```

Ce code nous donne une opacité de 50 %, et vous pouvez voir que le logo s'est estompé un peu :

![half-opacity](https://www.freecodecamp.org/news/content/images/2021/09/half-opacity.png)

```css
img {
        opacity: 0;
      }
```

Avec une opacité de `0`, l'image est à 100 % transparente, donc elle devient invisible :

![zero-opacity](https://www.freecodecamp.org/news/content/images/2021/09/zero-opacity.png)


La seule façon d'être sûr que l'image est sur la page est de l'inspecter avec les outils de développement de votre navigateur :

![image-in-devtools](https://www.freecodecamp.org/news/content/images/2021/09/image-in-devtools.jpg)

Vous pouvez utiliser cette valeur d'opacité pour faire beaucoup de choses – par exemple, vous pouvez l'utiliser pour inclure du texte sur une image héroïque sur un site web.

Vous vous demandez peut-être pourquoi vous voudriez rendre du contenu invisible avec une valeur d'opacité de 0. Eh bien, cela peut être utile dans les animations, et dans la construction de jeux HTML + CSS + JavaScript également.

Vous voudrez certainement utiliser le positionnement CSS pour vous aider à aligner les choses. J'en discuterai dans les prochaines parties de l'article.

## Transparence de l'image de fond en HTML et CSS

CSS offre un moyen de définir l'image de fond pour un élément conteneur avec la propriété `background-image`, donc vous n'avez pas nécessairement à le faire avec le CSS. Cela signifie que vous pouvez également placer du texte dans le conteneur.

```html
<div class="showcase">
      <h1>A group of ring-tailed lemurs</h1>
</div>
```

```css
body {
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 0 auto;
      height: 100vh;
    }
    .showcase {
      background-image: url("ring-tailed-lemurs.jpeg");
      height: 400px;
      width: 500px;
      background-position: center;
      background-repeat: no-repeat;
      background-size: cover;
      opacity: 0.6;
    }
```

L'inconvénient de cette approche est que l'opacité est définie pour le conteneur où se trouvent l'image et le texte. Ainsi, l'opacité affecte également le texte, et pas seulement l'image. Ce n'est probablement pas ce que vous voulez !

![css-opacity](https://www.freecodecamp.org/news/content/images/2021/09/css-opacity.png)

### La solution

Par défaut, lorsque vous appliquez une opacité à un conteneur, les descendants l'héritent également.

Une solution dans cette situation est de définir l'image de fond dans le HTML. Cela facilite l'application de l'opacité à l'image uniquement, au lieu de définir l'image de fond pour le conteneur dans le CSS.

Cette fois-ci, l'image et le texte seront séparés, donc le texte n'héritera pas de la valeur définie pour l'`opacity`.

Cela signifie que vous devez également utiliser le positionnement CSS pour aligner le texte dans l'image.

```html
<div class="showcase">
   <img src="ring-tailed-lemurs.jpeg" alt="lemurs" class="bg-image" />

   <h1 class="bg-img-title">A group of ring-tailed lemurs</h1>
</div>
```

```css
body {
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 0 auto;
      height: 100vh;
    }
    .showcase {
      position: relative;
    }

    .bg-image {
      opacity: 0.7;
    }

    .bg-img-title {
      position: absolute;
      top: 420px;
      left: 20px;
    }
```

Dans l'extrait de code CSS ci-dessus, j'utilise `flexbox` pour centrer tout sur la page.

L'élément `div` conteneur avec la classe `showcase` est positionné `relative`, afin que vous puissiez positionner le texte `h1` `absolute` à l'intérieur. Cela poussera le texte `h1` vers le coin supérieur gauche de l'image. Les propriétés `top` et `left` sont ensuite utilisées pour pousser le texte vers le coin inférieur gauche de l'image.

Si vous vous demandez ce que sont les propriétés `top` et `left`, ce sont les propriétés auxquelles vous avez accès lorsque vous utilisez la propriété display.

En plus de ces deux propriétés, vous avez également accès aux propriétés `right` et `bottom`. Elles vous permettent de positionner un élément n'importe où.

En fin de compte, l'image est opaque et le texte n'est pas affecté :
![right-opacity](https://www.freecodecamp.org/news/content/images/2021/09/right-opacity.png)

## Conclusion

Dans cet article, vous avez appris à utiliser la propriété opacity de CSS pour rendre les images transparentes.

Comme CSS reste délicat et un peu étrange, il est utile de combiner la propriété opacity avec d'autres fonctionnalités CSS telles que le positionnement afin de l'utiliser correctement.

En plus du positionnement CSS, vous pouvez également utiliser la propriété `opacity` avec des pseudo-éléments CSS tels que `::before` et `::after`, ce qui est une manière un peu astucieuse de faire les choses.

Merci d'avoir lu, et continuez à coder.