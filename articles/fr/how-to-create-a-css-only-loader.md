---
title: Comment créer un loader CSS uniquement avec un seul élément
subtitle: ''
author: Temani Afif
co_authors: []
series: null
date: '2022-01-14T21:11:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-css-only-loader
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/header-loader.png
tags:
- name: animation
  slug: animation
- name: CSS
  slug: css
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Comment créer un loader CSS uniquement avec un seul élément
seo_desc: 'If you have a website, it''s helpful to have a loader so users can tell
  something is happening once they''ve clicked a link or button.

  You can use this loader component in a lot of places, and it should be as simple
  as possible.

  In this post, we will s...'
---

Si vous avez un site web, il est utile d'avoir un loader pour que les utilisateurs puissent voir qu'une action est en cours une fois qu'ils ont cliqué sur un lien ou un bouton.

Vous pouvez utiliser ce composant de loader dans de nombreux endroits, et il doit être aussi simple que possible.

Dans cet article, nous verrons comment construire deux types de loaders avec seulement un `<div>` et quelques lignes de code CSS. Non seulement cela, mais nous les rendrons personnalisables afin que vous puissiez facilement créer différentes variations à partir du même code.

Voici ce que nous allons construire :

![Loader Spinner et Progress uniquement en CSS](https://www.freecodecamp.org/news/content/images/2022/01/final-loader.gif align="left")

*Loader Spinner et Progress uniquement en CSS*

## Comment créer un Spinner Loader

Voici une démonstration de ce que nous construisons :

%[https://codepen.io/t_afif/pen/PoJyaNy]

<details>
    <summary>Cliquez pour voir le code complet</summary>
<pre><code class="language-html"> <div class="loader"></div>
 <div class="loader" style="--b: 15px;--c: blue;width: 120px;--n: 8"></div>
 <div class="loader" style="--b: 5px;--c: green;width: 80px;--n: 6;--g: 20deg"></div>
 <div class="loader" style="--b: 20px;--c: #000;width: 80px;--n: 15;--g: 7deg"></div></code></pre>
<pre><code class="language-css"> .loader {
   --b: 10px;  /* épaisseur de la bordure */
   --n: 10;    /* nombre de tirets */
   --g: 10deg; /* écart entre les tirets */
   --c: red;   /* la couleur */

   width: 100px; /* taille */
   aspect-ratio: 1;
   border-radius: 50%;
   padding: 1px;
   background: conic-gradient(#0000,var(--c)) content-box;
   -webkit-mask:
     repeating-conic-gradient(#0000 0deg,
        #000 1deg calc(360deg/var(--n) - var(--g) - 1deg),
        #0000     calc(360deg/var(--n) - var(--g)) calc(360deg/var(--n))),
     radial-gradient(farthest-side,#0000 calc(98% - var(--b)),#000 calc(100% - var(--b)));
           mask:
     repeating-conic-gradient(#0000 0deg,
        #000 1deg calc(360deg/var(--n) - var(--g) - 1deg),
        #0000     calc(360deg/var(--n) - var(--g)) calc(360deg/var(--n))),
     radial-gradient(farthest-side,#0000 calc(98% - var(--b)),#000 calc(100% - var(--b)));
   -webkit-mask-composite: destination-in;
           mask-composite: intersect;
   animation: load 1s infinite steps(var(--n));
 }
 @keyframes load {to{transform: rotate(1turn)}}</code></pre>
</details>

Nous avons 4 loaders différents utilisant le même code. En ne changeant que quelques variables, nous pouvons générer un nouveau loader sans avoir besoin de toucher au code CSS.

Les variables sont définies comme suit :

* `--b` définit l'épaisseur de la bordure.

* `--n` définit le nombre de tirets.

* `--g` définit l'écart entre les tirets. Puisque nous traitons avec un élément circulaire, celui-ci est une valeur d'angle.

* `--c` définit la couleur.

Voici une illustration pour voir les différentes variables.

![Variables CSS du loader Spinner](https://www.freecodecamp.org/news/content/images/2022/01/image-50.png align="left")

*Variables CSS du loader Spinner*

Analysons le code CSS. Nous utiliserons une autre figure pour illustrer une construction étape par étape du loader.

![Illustration étape par étape du Spinner Loader](https://www.freecodecamp.org/news/content/images/2022/01/image-51.png align="left")

*Illustration étape par étape du Spinner Loader*

Nous commençons d'abord par créer un cercle comme ceci :

```css
.loader {
  width: 100px; /* taille */
  aspect-ratio: 1;
  border-radius: 50%;
}
```

Rien de complexe pour l'instant. Notez l'utilisation de `aspect-ratio` qui nous permet de ne modifier qu'une seule valeur (la `width`) afin de contrôler la taille.

Ensuite, nous ajoutons une coloration de dégradé conique de transparent à la couleur définie (la variable `--c`) :

```css
.loader {
  width:100px; /* taille */
  aspect-ratio: 1;
  border-radius: 50%;
  background: conic-gradient(#0000,var(--c));
}
```

Dans cette étape, nous introduisons la propriété `mask` pour masquer certaines parties du cercle de manière répétitive. Cela dépendra des variables `--n` et `--d`. Si vous regardez attentivement la figure, nous remarquerons le motif suivant :

```python
partie visible
partie invisible
partie visible
partie invisible
etc
```

Pour ce faire, nous utilisons `repeating-conic-gradient(#000 0 X, #0000 0 Y)`. De `0` à `X`, nous avons une couleur opaque (partie visible) et de `X` à `Y`, une couleur transparente (partie invisible).

Nous introduisons nos variables :

* Nous avons besoin d'un écart égal à `g` entre chaque partie visible, donc la formule entre `X` et `Y` sera `X = Y - g`.

* Nous avons besoin de `n` parties visibles, donc la formule de `Y` devrait être `Y = 360deg/n`. Un cercle complet est de `360deg`, donc nous le divisons simplement par `n`.

Notre code jusqu'à présent est :

```css
.loader {
  width: 100px; /* taille */
  aspect-ratio: 1;
  border-radius: 50%;
  background: conic-gradient(#0000,var(--c));
  mask: repeating-conic-gradient(#000 0 calc(360deg/var(--n) - var(--g)) , #0000 0 calc(360deg/var(--n))
}
```

Cette prochaine étape est la plus délicate, car nous devons appliquer un autre masque pour créer une sorte de trou afin d'obtenir la forme finale. Pour ce faire, nous utiliserons logiquement un `radial-gradient()` avec notre variable `b` :

```css
radial-gradient(farthest-side,#0000 calc(100% - var(--b)),#000 0)
```

Un cercle complet dont nous retirons une épaisseur égale à `b`.

Nous ajoutons cela au masque précédent :

```css
.loader {
  width: 100px; /* taille */
  aspect-ratio: 1;
  border-radius: 50%;
  background: conic-gradient(#0000,var(--c));
  mask: 
   radial-gradient(farthest-side,#0000 calc(100% - var(--b)),#000 0),
   repeating-conic-gradient(#000 0 calc(360deg/var(--n) - var(--g)) , #0000 0 calc(360deg/var(--n))
}
```

Nous avons deux couches de masque, mais le résultat n'est pas celui que nous voulons. Nous obtenons ce qui suit :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-52.png align="left")

Cela peut sembler étrange, mais c'est logique. La partie "finale" visible n'est rien d'autre que la somme de chaque partie visible de chaque couche de masque. Nous pouvons changer ce comportement en utilisant `mask-composite`. J'aurais besoin d'un article entier pour expliquer cette propriété, donc je me contenterai de donner la valeur.

Dans notre cas, nous devons considérer `intersect` (et `destination-out` pour la propriété préfixée). Notre code deviendra :

```css
.loader {
  width: 100px; /* taille */
  aspect-ratio: 1;
  border-radius: 50%;
  background: conic-gradient(#0000,var(--c));
  mask: 
    radial-gradient(farthest-side,#0000 calc(100% - var(--b)),#000 0),
    repeating-conic-gradient(#000 0 calc(360deg/var(--n) - var(--g)) , #0000 0 calc(360deg/var(--n));
  -webkit-mask-composite: destination-in;
          mask-composite: intersect;
}
```

Nous avons terminé avec la forme ! Il ne nous manque plus que l'animation. Cette dernière est une rotation infinie.

La seule chose à noter est que j'utilise une animation `steps` pour créer l'illusion de tirets fixes et de couleurs en mouvement.

Voici une illustration pour voir la différence :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/steps-final.gif align="left")

*Une animation linéaire vs une animation par étapes*

La première est une rotation linéaire et continue de la forme (ce n'est pas ce que nous voulons) et la seconde est une animation discrète (celle que nous voulons).

Voici le code complet incluant l'animation :

<details>
    <summary>Cliquez pour voir le code complet</summary>
<pre><code class="language-html"> <div class="loader"></div>
 <div class="loader" style="--b: 15px;--c: blue;width: 120px;--n: 8"></div>
 <div class="loader" style="--b: 5px;--c: green;width: 80px;--n: 6;--g: 20deg"></div>
 <div class="loader" style="--b: 20px;--c: #000;width: 80px;--n: 15;--g: 7deg"></div></code></pre>
<pre><code class="language-css"> .loader {
   --b: 10px;  /* épaisseur de la bordure */
   --n: 10;    /* nombre de tirets */
   --g: 10deg; /* écart entre les tirets */
   --c: red;   /* la couleur */

   width: 100px; /* taille */
   aspect-ratio: 1;
   border-radius: 50%;
   padding: 1px;
   background: conic-gradient(#0000,var(--c)) content-box;
   -webkit-mask:
     repeating-conic-gradient(#0000 0deg,
        #000 1deg calc(360deg/var(--n) - var(--g) - 1deg),
        #0000     calc(360deg/var(--n) - var(--g)) calc(360deg/var(--n))),
     radial-gradient(farthest-side,#0000 calc(98% - var(--b)),#000 calc(100% - var(--b)));
           mask:
     repeating-conic-gradient(#0000 0deg,
        #000 1deg calc(360deg/var(--n) - var(--g) - 1deg),
        #0000     calc(360deg/var(--n) - var(--g)) calc(360deg/var(--n))),
     radial-gradient(farthest-side,#0000 calc(98% - var(--b)),#000 calc(100% - var(--b)));
   -webkit-mask-composite: destination-in;
           mask-composite: intersect;
   animation: load 1s infinite steps(var(--n));
 }
 @keyframes load {to{transform: rotate(1turn)}}</code></pre>
</details>

Vous remarquerez quelques différences avec le code que j'ai utilisé dans l'explication :

* J'ajoute `padding: 1px` et définis le fond sur `content-box`.

* Il y a `+/1deg` entre les couleurs du `repeating-conic-gradient()`.

* Il y a quelques pourcentages de différence entre la couleur à l'intérieur du `radial-gradient()`.

Ce sont quelques corrections pour éviter les bugs visuels. Les dégradés sont connus pour produire des résultats "étranges" dans certains cas, donc nous devons ajuster certaines valeurs manuellement pour les éviter.

## Comment créer un Progress Loader

Comme le loader précédent, commençons par un aperçu :

%[https://codepen.io/t_afif/pen/bGoNddg]

<details>
    <summary>Cliquez pour voir le code complet</summary>
<pre><code class="language-html"> <div class="loader"></div>
 <div class="loader" style="--s:10px;--n:10;color:red"></div>
 <div class="loader" style="--g:0px;color:darkblue"></div>
 <div class="loader" style="--s:25px;--g:8px;border-radius:50px;color:green"></div></code></pre>
<pre><code class="language-css"> .loader {
   --n:5;    /* contrôle le nombre de bandes */
   --s:30px; /* contrôle la largeur des bandes */
   --g:5px;  /* contrôle l'écart entre les bandes */

   width:calc(var(--n)*(var(--s) + var(--g)) - var(--g));
   height:30px;
   padding:var(--g);
   margin:5px auto;
   border:1px solid;
   background:
     repeating-linear-gradient(90deg,
       currentColor  0 var(--s),
       #0000 0 calc(var(--s) + var(--g))
     ) left / calc((var(--n) + 1)*(var(--s) + var(--g))) 100% 
     no-repeat content-box;
   animation: load 1.5s steps(calc(var(--n) + 1)) infinite;
 }
 @keyframes load {
   0% {background-size: 0% 100%}
 }</code></pre>
</details>

Nous avons la même configuration que le loader précédent. Variables CSS qui contrôlent le loader :

* `--n` définit le nombre de tirets/bandes.

* `--s` définit la largeur de chaque bande.

* `--g` définit l'écart entre les bandes.

![Illustration des variables CSS](https://www.freecodecamp.org/news/content/images/2022/01/image-53.png align="left")

*Illustration des variables CSS*

D'après la figure ci-dessus, nous pouvons voir que la largeur de l'élément dépendra des 3 variables. Le CSS sera comme suit :

```css
.loader {
  width: calc(var(--n)*(var(--s) + var(--g)) - var(--g));
  height: 30px; /* utilisez n'importe quelle valeur ici */
  padding: var(--g);
  border: 1px solid;
}
```

Nous utilisons `padding` pour définir l'écart de chaque côté. Ensuite, la largeur sera égale au nombre de bandes multiplié par leur largeur et l'écart. Nous retirons un écart car pour `N` bandes, nous avons `N-1` écarts.

Pour créer les bandes, nous utiliserons le dégradé suivant.

```python
repeating-linear-gradient(90deg,
  currentColor 0 var(--s),
  #0000        0 calc(var(--s) + var(--g))
 )
```

De `0` à `s`, nous avons la couleur définie et de `s` à `s + g`, une couleur transparente (l'écart).

J'utilise `currentColor` qui est la valeur de la propriété `color`. Notez que je n'ai pas défini de couleur à l'intérieur de `border`, donc elle utilisera également la valeur de `color`. Si nous voulons changer la couleur du loader, nous devons simplement définir la propriété `color`.

Notre code jusqu'à présent :

```css
.loader {
  width: calc(var(--n)*(var(--s) + var(--g)) - var(--g));
  height: 30px;
  padding: var(--g);
  border: 1px solid;
  background:
    repeating-linear-gradient(90deg,
      currentColor  0 var(--s),
      #0000 0 calc(var(--s) + var(--g))
    ) left / 100% 100% content-box no-repeat;
}
```

J'utilise `content-box` pour m'assurer que le dégradé ne couvre pas la zone de padding. Ensuite, je définis une taille égale à `100% 100%` et une position à gauche.

Il est temps pour l'animation. Pour ce loader, nous allons animer le `background-size` de `0% 100%` à `100% 100%`, ce qui signifie que la largeur de notre dégradé passe de `0%` à `100%`.

Comme le loader précédent, nous allons nous appuyer sur `steps()` pour avoir une animation discrète au lieu d'une animation continue.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/steps-2-final.gif align="left")

*Une animation linéaire vs une animation par étapes*

La seconde est celle que nous voulons créer, et nous pouvons l'obtenir en ajoutant le code suivant :

```css
.loader {
  animation: load 1.5s steps(var(--n)) infinite;
}
@keyframes load {
  0% {background-size: 0% 100%}
}
```

Si vous regardez attentivement la dernière figure, vous remarquerez que l'animation n'est pas complète. Il manque une bande à la fin, même si nous avons utilisé `N`. Ce n'est pas un bug, mais le fonctionnement prévu de `steps()`.

Pour surmonter cela, nous devons ajouter une étape supplémentaire. Nous augmentons la `background-size` de notre dégradé pour contenir `N+1` bandes et utilisons `steps(N+1)`. Cela nous donnera le code final :

```css
.loader {
  width: calc(var(--n)*(var(--s) + var(--g)) - var(--g));
  height: 30px;
  padding: var(--g);
  margin: 5px auto;
  border: 1px solid;
  background:
    repeating-linear-gradient(90deg,
      currentColor  0 var(--s),
      #0000 0 calc(var(--s) + var(--g))
    ) left / calc((var(--n) + 1)*(var(--s) + var(--g))) 100% 
    content-box no-repeat;
  animation: load 1.5s steps(calc(var(--n) + 1)) infinite;
}
@keyframes load {
  0% {background-size: 0% 100%}
}
```

Notez que la largeur du dégradé est égale à `N+1` multiplié par la largeur d'une bande et un écart (au lieu d'être `100%`).

## Conclusion

J'espère que vous avez apprécié ce tutoriel. Si vous êtes intéressé, [j'ai créé plus de 500 loaders CSS uniquement avec un seul div](https://css-loaders.com/). J'ai également écrit un autre [tutoriel pour expliquer comment créer le loader Dots en utilisant uniquement les propriétés de fond](https://dev.to/afif/build-your-css-loader-with-only-one-div-the-dots-3882).

Voici quelques liens utiles pour obtenir plus de détails sur certaines propriétés que j'ai utilisées et que je n'ai pas expliquées en profondeur en raison de leur complexité :

* `mask-composite` : [https://css-tricks.com/mask-compositing-the-crash-course/](https://css-tricks.com/mask-compositing-the-crash-course/)

* `steps()` : [https://developer.mozilla.org/en-US/docs/Web/CSS/easing-function#the\_steps\_class\_of\_easing\_functions](https://developer.mozilla.org/en-US/docs/Web/CSS/easing-function#the_steps_class_of_easing_functions)