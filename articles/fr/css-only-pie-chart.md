---
title: Comment créer un graphique circulaire en utilisant uniquement CSS
subtitle: ''
author: Temani Afif
co_authors: []
series: null
date: '2022-01-06T20:41:44.000Z'
originalURL: https://freecodecamp.org/news/css-only-pie-chart
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/header-2-3.png
tags:
- name: animation
  slug: animation
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: Comment créer un graphique circulaire en utilisant uniquement CSS
seo_desc: 'Pie charts are common components that let you show portions of a whole,
  and you can use them for many different purposes.

  You will find a lot of articles around building such a component, but they typically
  either rely on SVG or a lot of HTML element...'
---

Les graphiques circulaires sont des composants courants qui permettent de montrer des portions d'un tout, et vous pouvez les utiliser pour de nombreuses fins différentes.

Vous trouverez de nombreux articles sur la création d'un tel composant, mais ils reposent généralement soit sur SVG, soit sur de nombreux éléments HTML.

Dans cet article, je vais vous montrer comment créer un graphique circulaire en utilisant CSS et un seul élément.

Voici un aperçu de ce que nous allons construire :

<details>
  <summary>Cliquez pour voir le code complet</summary>
<pre><code class="language-html"><div class="pie" style="--p:20"> 20%</div>
<div class="pie" style="--p:40;--c:darkblue;--b:10px"> 40%</div>
<div class="pie no-round" style="--p:60;--c:purple;--b:15px"> 60%</div>
<div class="pie animate no-round" style="--p:80;--c:orange;"> 80%</div>
<div class="pie animate" style="--p:90;--c:lightgreen"> 90%</div></code></pre>
<pre><code class="language-css">@property --p{
  syntax: 

%[https://codepen.io/t_afif/pen/XWaPXZO] 

Comme vous pouvez le voir dans le CodePen ci-dessus, nous avons un graphique circulaire statique, un animé, et nous pouvons également avoir des bords arrondis. Tout cela avec un seul élément `<div>`.

En plus de cela, nous pouvons facilement ajuster les différentes valeurs en utilisant des variables CSS afin de ne pas avoir à nous soucier de changer le code CSS.

Je sais que le code peut sembler un peu difficile au premier abord, mais après avoir lu l'explication ci-dessous, vous serez en mesure de créer vos propres graphiques circulaires en toute confiance.

## La structure HTML pour le graphique circulaire

Comme je l'ai mentionné ci-dessus, nous avons un seul `<div>` où nous ajoutons la valeur de pourcentage (la progression du graphique circulaire) comme contenu principal :

```html
<div class="pie" style="--p:60;--b:10px;--c:purple;">60%</div>
```

Nous ajoutons également les variables CSS comme styles en ligne.

* `--p` : Cette variable doit contenir la valeur de pourcentage sous forme de nombre (sans le signe `%`). Elle doit être la même que le contenu.

* `--b` : Cette variable définira l'épaisseur de la bordure.

* `--c` : Cette variable définira la couleur principale.

Pour les besoins de cet article et de la démonstration, j'utilise une variable à un caractère pour garder le code court. Mais il est préférable d'envisager des variables plus explicites lors de l'utilisation du code dans un environnement de production. Exemples : `--percentage`, `--border-thickness`, et `--main-color`.

## Les paramètres CSS pour le graphique circulaire

Nous commençons d'abord par styliser notre contenu. Cette partie est facile et le code est le suivant :

```css
.pie {
  --w: 150px;
  width: var(--w);
  aspect-ratio: 1;
  display: inline-grid;
  place-content: center;
  margin: 5px;
  font-size: 25px;
  font-weight: bold;
  font-family: sans-serif;
}
```

Je définis l'élément comme `inline-grid` pour placer facilement le contenu au milieu en utilisant `place-content: center`. Nous utilisons `aspect-ratio: 1` pour nous assurer que l'élément reste carré. Nous pouvons également utiliser `height: var(--w)` mais il est toujours bon d'apprendre et d'utiliser une nouvelle propriété CSS.

Vous vous demandez peut-être pourquoi j'utilise une variable pour définir la largeur au lieu de simplement définir `width: 150px`. J'ai besoin de connaître la valeur de la largeur pour une utilisation future, donc je la définis comme une variable.

Tout le reste du CSS est assez basique pour styliser le texte. N'hésitez pas à le mettre à jour comme vous le souhaitez.

Passons à la partie intéressante – la forme principale de notre composant. Pour cela, nous utiliserons un pseudo-élément avec les styles suivants :

```css
.pie:before{
  content: "";
  position: absolute;
  border-radius: 50%;
  inset: 0;
  background: conic-gradient(var(--c) calc(var(--p)*1%),#0000 0);
}
```

Un pseudo-élément qui a `position: absolute` couvre toute la zone grâce à `inset: 0`. Oui, c'est encore une nouvelle propriété CSS qui est le raccourci pour `top`, `right`, `bottom`, et `right` (que vous pouvez [lire plus ici](https://developer.mozilla.org/en-US/docs/Web/CSS/inset)).

Ensuite, nous en faisons un cercle (`border-radius: 50%`) et nous appliquons un `conic-gradient()`. Notez l'utilisation des variables CSS que nous avons définies comme styles en ligne (`--c` pour la couleur et `--p` pour le pourcentage).

Jusqu'à présent, cela nous donnera le résultat suivant :

![Conic-gradient appliqué au pseudo-élément](https://www.freecodecamp.org/news/content/images/2022/01/image-35.png align="left")

*Conic-gradient appliqué au pseudo-élément*

Nous nous rapprochons ! Le `conic-gradient()` nous donne un dégradé de deux couleurs. De `0%` à `p%` la couleur principale et la partie restante est une couleur transparente (définie avec la valeur hexadécimale `#0000`).

Pour garder uniquement la partie de la bordure, nous utiliserons un `mask` pour masquer la partie centrale. Cette fois, nous utiliserons un `radial-gradient()` :

```python
radial-gradient(farthest-side,red calc(99% - var(--b)),blue calc(100% - var(--b)))
```

Le dégradé ci-dessus appliqué comme arrière-plan nous donnera ce qui suit :

![Illustration du radial-gradient](https://www.freecodecamp.org/news/content/images/2022/01/image-36.png align="left")

*Illustration du radial-gradient*

Notez l'utilisation de la variable `--b` qui définit l'épaisseur de la bordure (affichée en bleu ci-dessus).

Maintenant, imaginez que la partie rouge est la partie invisible et la partie bleue la partie visible. Voici ce que nous obtiendrons si nous utilisons le même dégradé avec la propriété `mask` :

![Application du masque au pseudo-élément](https://www.freecodecamp.org/news/content/images/2022/01/image-37.png align="left")

*Application du masque au pseudo-élément*

Nous avons notre graphique circulaire avec un élément et quelques lignes de code CSS.

```css
.pie {
  --w:150px;
  
  width: var(--w);
  aspect-ratio: 1;
  position: relative;
  display: inline-grid;
  place-content: center;
  margin: 5px;
  font-size: 25px;
  font-weight: bold;
  font-family: sans-serif;
}
.pie:before {
  content: "";
  position: absolute;
  border-radius: 50%;
  inset: 0;
  background: conic-gradient(var(--c) calc(var(--p)*1%),#0000 0);
  -webkit-mask:radial-gradient(farthest-side,#0000 calc(99% - var(--b)),#000 calc(100% - var(--b)));
          mask:radial-gradient(farthest-side,#0000 calc(99% - var(--b)),#000 calc(100% - var(--b)));
}
```

Et le HTML :

```html
<div class="pie" style="--p:60;--b:10px;--c:purple;">60%</div>
```

### Comment ajouter les bords arrondis

Pour cela, j'ajouterai une couche de dégradé supplémentaire pour arrondir le bord supérieur et un pseudo-élément pour arrondir l'autre bord. Voici une illustration pour comprendre l'astuce :

![Illustration des bords arrondis](https://www.freecodecamp.org/news/content/images/2022/01/image-38.png align="left")

*Illustration des bords arrondis*

Le code pour (1) pour arrondir le bord supérieur :

```python
.pie:before {
  background:
    radial-gradient(farthest-side,var(--c) 98%,#0000) top/var(--b) var(--b) no-repeat,
    conic-gradient(var(--c) calc(var(--p)*1%),#0000 0);
}
```

En plus du `conic-gradient()`, nous ajoutons un `radial-gradient()` placé en haut qui a une taille égale à l'épaisseur de la bordure définie par `--b`.

Le code pour (2) pour arrondir l'autre bord :

```css
.pie:after {
  content: "";
  position: absolute;
  border-radius: 50%;
  inset: calc(50% - var(--b)/2);
  background: var(--c);
  transform: rotate(calc(var(--p)*3.6deg)) translateY(calc(50% - var(--w)/2));
}
```

La propriété `inset` définit la taille du pseudo-élément pour qu'elle soit égale à `--b`. Rappelez-vous que c'est le raccourci pour `top`, `right`, `bottom` et `left`. Si nous avons

```python
left = right = 50% - b/2
```

cela signifie que de chaque côté, nous nous déplaçons vers le centre moins un décalage égal à `b/2` – donc nous finissons par avoir une largeur égale à `2*b/2 = b`. Même logique pour la hauteur.

Maintenant, nous devons placer correctement notre élément, c'est pourquoi nous utilisons la propriété transform. Notre élément est initialement placé au centre, donc nous devons d'abord le faire tourner. Ayant le pourcentage, nous utilisons la "[Règle de trois](https://en.wikipedia.org/wiki/Cross-multiplication#Rule_of_three)" pour obtenir l'angle :

```python
angle = percentage*360deg/100
```

Ensuite, nous faisons une translation, et ici nous aurons besoin de la largeur car nous devons effectuer une translation de la moitié de la largeur (`w/2`).

D'accord, d'accord – vous pourriez être un peu perdu dans toutes ces formules. Voici une illustration pour comprendre la logique derrière la propriété transform

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-39.png align="left")

*Application de la propriété transform au pseudo-élément*

Après cela, nous colorons le pseudo-élément avec la couleur principale `--c` et nous avons terminé. Nous avons notre graphique circulaire avec des bords arrondis.

## Comment animer le graphique circulaire

Un graphique circulaire statique est bien, mais un graphique animé est mieux ! Pour cela, nous allons animer la valeur de pourcentage `--p` de `0` à la valeur définie. Par défaut, nous ne pouvons pas animer les variables CSS, mais grâce à [la nouvelle fonctionnalité `@property`](https://developer.mozilla.org/en-US/docs/Web/CSS/@property), c'est maintenant possible.

Nous enregistrons la variable :

```css
@property --p{
  syntax: '<number>';
  inherits: true;
  initial-value: 0;
}
```

Nous créons une `keyframes` :

```css
@keyframes p {
  from {--p:0}
}
```

Notez que nous n'avons besoin de spécifier que le `from`. En faisant cela, le navigateur rendra le `to` égal, par défaut, à la valeur que nous avons définie (`<div class="pie" style="--p:60;">60%</div>`).

Et enfin, nous appelons l'animation. Vous pouvez définir la durée/délai comme vous le souhaitez.

```css
animation: p 1s .5s both;
```

Malheureusement, cette technique n'est pas largement supportée. Vous pouvez la tester sur les navigateurs basés sur Chromium (Chrome et Edge), mais elle échouera sur Firefox et Safari. Vous pouvez consulter [Can I Use](https://caniuse.com/?search=%40property) pour suivre le support.

Avant de terminer, voici à nouveau le code complet et une démonstration du produit final fonctionnel. Vous pouvez voir que j'utilise deux classes pour contrôler les bords arrondis et l'animation afin que nous puissions facilement les ajouter/supprimer selon les besoins.

<details>
  <summary>Cliquez pour voir le code complet</summary>
<pre><code class="language-html"><div class="pie" style="--p:20"> 20%</div>
<div class="pie" style="--p:40;--c:darkblue;--b:10px"> 40%</div>
<div class="pie no-round" style="--p:60;--c:purple;--b:15px"> 60%</div>
<div class="pie animate no-round" style="--p:80;--c:orange;"> 80%</div>
<div class="pie animate" style="--p:90;--c:lightgreen"> 90%</div></code></pre>
<pre><code class="language-css">@property --p{
  syntax: 

%[https://codepen.io/t_afif/pen/XWaPXZO]