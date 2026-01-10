---
title: Comment créer un ruban en CSS uniquement pour votre site web
subtitle: ''
author: Temani Afif
co_authors: []
series: null
date: '2022-02-08T19:33:59.000Z'
originalURL: https://freecodecamp.org/news/make-a-css-only-ribbon
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/final-header-ribbon.png
tags:
- name: CSS
  slug: css
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Comment créer un ruban en CSS uniquement pour votre site web
seo_desc: 'Have you ever noticed those fancy ribbons on websites that alert users
  to some special feature or event? They''re great to have, but for many developers,
  it''s a nightmare to create them.

  You can easily find a lot of ready-to-use code for such a compon...'
---

Avez-vous déjà remarqué ces rubans élégants sur les sites web qui alertent les utilisateurs sur une fonctionnalité ou un événement spécial ? Ils sont géniaux à avoir, mais pour de nombreux développeurs, c'est un cauchemar de les créer.

Vous pouvez facilement trouver beaucoup de code prêt à l'emploi pour un tel composant, mais ils ne sont pas faciles à mettre à jour. Vous devez également faire face à beaucoup d'essais et d'erreurs jusqu'à ce que vous les fassiez fonctionner correctement.

Dans cet article, je vais vous montrer comment créer deux types de rubans avec un simple code CSS où vous n'avez pas besoin de vous soucier de régler beaucoup de valeurs.

Voici ce que nous allons créer dans cet article :

![Ruban tourné & Ruban plié](https://www.freecodecamp.org/news/content/images/2022/02/image-18.png align="left")

*Ruban tourné & Ruban plié*

Ci-dessous se trouve le code complet pour les deux rubans afin que vous puissiez voir à quel point c'est simple :

%[https://codepen.io/t_afif/pen/dyZOBex/55e02b7d8b1dffb5c1a63473d5724dee]

<details>
  <summary>Cliquez pour voir le code complet</summary>
<pre><code class="language-html">  <div class="box">
    <div class="ribbon-2">Ruban plié</div>
  </div>
  <div class="ribbon-1 left">Ruban tourné</div>
  <div class="ribbon-1 right">Ruban tourné</div></code></pre>
<pre><code class="language-css">  .ribbon-1 {
    position: fixed;
    background: #08769b;
    box-shadow: 0 0 0 999px #08769b;
    clip-path: inset(0 -100%);
  }
  .left {
    inset: 0 auto auto 0;
    transform-origin: 100% 0;
    transform: translate(-29.3%) rotate(-45deg);
  }
  .right {
    inset: 0 0 auto auto;
    transform-origin: 0 0;
    transform: translate(29.3%) rotate(45deg);
  }

  .ribbon-2 {
    --f: 10px; /* contrôle la partie pliée*/
    --r: 15px; /* contrôle la forme du ruban */
    --t: 10px; /* le décalage supérieur */

    position: absolute;
    inset: var(--t) calc(-1*var(--f)) auto auto;
    padding: 0 10px var(--f) calc(10px + var(--r));
    clip-path: 
      polygon(0 0,100% 0,100% calc(100% - var(--f)),calc(100% - var(--f)) 100%,
        calc(100% - var(--f)) calc(100% - var(--f)),0 calc(100% - var(--f)),
        var(--r) calc(50% - var(--f)/2));
    background: #BD1550;
    box-shadow: 0 calc(-1*var(--f)) 0 inset #0005;
  }


  .box {
    max-width:500px;
    height:200px;
    margin:50px auto 0;
    background:lightblue;
    position:relative;
  }</code></pre>
</details>

## Comment créer un ruban tourné avec CSS

Ce type de ruban est, dans la plupart des cas, utilisé pour placer une information fixe en haut de l'écran. Mais nous pouvons également l'utiliser à l'intérieur d'un élément dans la page.

Pour comprendre comment créer un tel ruban, examinons une illustration étape par étape :

![Illustration étape par étape du ruban tourné](https://www.freecodecamp.org/news/content/images/2022/02/image-19.png align="left")

*Illustration étape par étape du ruban tourné*

Tout d'abord, nous commençons par placer notre élément dans le coin supérieur gauche de l'écran. Les bordures rouges dans l'illustration sont les limites de l'écran (ou de l'élément où vous souhaitez placer le ruban).

```css
.ribbon {
  position: fixed;
  inset: 0 auto auto 0;
  background: #08769b;
}
```

Rien de complexe pour l'instant. Si vous n'êtes pas familier avec la propriété `inset`, ce n'est rien d'autre que la forme abrégée de `top`, `right`, `bottom` et `left`.

Ensuite, nous effectuons une translation vers la gauche en utilisant `translate(-29.3%)`.

Après la translation, nous tournons notre élément en utilisant `rotate(-45deg)` et le code devient ceci :

```css
.ribbon {
  position: fixed;
  inset: 0 auto auto 0;
  background: #08769b;
  transform-origin: 100% 0; /* ou top left */
  transform: translate(-29.3%) rotate(-45deg);
}
```

Vous vous demandez probablement quel est le secret de la valeur étrange `29.3%` ? Eh bien, elle est égale à `100% * (1 - cos(45deg))`.

J'éviterai de commencer une explication mathématique "ennuyeuse", mais vous pouvez voir qu'après avoir effectué la rotation, l'élément est parfaitement placé (ses deux coins supérieurs touchent les bords). La translation est la clé pour avoir ce placement parfait.

Vous pouvez également remarquer l'utilisation de `transform-origin: top left`. Dans la troisième étape, j'ai dû faire tourner l'élément à partir de son coin supérieur gauche.

Maintenant, notre élément est correctement placé, mais nous avons quelques espaces à remplir. J'utiliserai une "grande" `box-shadow` pour cela. Dans la figure, j'ai utilisé une couleur verte pour illustrer, mais vous devriez la considérer comme ayant la même couleur que l'arrière-plan.

Ensuite, nous devons rogner l'ombre pour ne montrer que les parties gauche et droite. Pour cela, j'utiliserai `clip-path`. J'utiliserai `inset(0 -100%)` ce qui signifie rogner l'ombre du haut et du bas (la valeur `0`) et montrer une partie de l'ombre gauche et droite (`-100%`).

`100%` est une valeur aléatoire qui doit être très grande. Elle peut être par exemple `999px` ou `100vmax` – n'importe quelle valeur pour s'assurer que nous gardons les parties gauche et droite de l'ombre.

Nous verrons maintenant le résultat final dans la sixième étape. Nous avons encore quelques ombres débordantes, mais personne ne peut les voir puisque nous plaçons notre élément dans le coin de l'écran.

Si vous placerez le ruban à l'intérieur d'un autre élément, n'oubliez pas d'utiliser `overflow: hidden` sur l'élément parent et aussi de remplacer `fixed` par `absolute`.

Notre code final sera :

```css
.ribbon-1 {
  position: fixed;
  inset: 0 auto auto 0;
  background: #08769b;
  transform-origin: 100% 0;
  transform: translate(-29.3%) rotate(-45deg);
  box-shadow: 0 0 0 999px #08769b;
  clip-path: inset(0 -100%);
}
```

Avec seulement 7 déclarations, nous avons notre ruban tourné. Vous remarquerez que notre code est générique et ne dépend pas du contenu textuel. Quel que soit le contenu du ruban, il sera toujours correctement placé. Vous pouvez même avoir plusieurs lignes de texte.

Pour placer le ruban dans le coin supérieur droit, nous devons simplement mettre à jour quelques valeurs. Encore mieux, utilisons deux classes pour contrôler facilement le placement :

```css
.ribbon-1 {
  position: fixed;
  background: #08769b;
  box-shadow: 0 0 0 999px #08769b;
  clip-path: inset(0 -100%);
}
.left {
  inset: 0 auto auto 0; /* top et left égaux à 0 */
  transform-origin: 100% 0; /* OU top right */
  transform: translate(-29.3%) rotate(-45deg);
}
.right {
  inset: 0 0 auto auto; /* top et right égaux à 0 */
  transform-origin: 0 0; /* OU top left */
  transform: translate(29.3%) rotate(45deg);
}
```

Je pense que le code est auto-explicatif et que les différences entre droite et gauche sont simples à comprendre.

## Comment créer un ruban plié avec CSS

Abordons le deuxième type de ruban de la même manière que nous l'avons fait avec le précédent en utilisant une illustration étape par étape.

![Illustration étape par étape du ruban plié](https://www.freecodecamp.org/news/content/images/2022/02/image-20.png align="left")

*Illustration étape par étape du ruban plié*

Tout d'abord, nous allons commencer par placer notre élément sur le côté droit de l'élément parent.

```css
.ribbon-2 {
  --t: 10px; /* le décalage supérieur */
  
  position: absolute;
  inset: var(--t) 0 auto auto;
  padding:0 10px;
  background: #BD1550;
  
}
```

Je vais considérer une variable pour contrôler le décalage par rapport au haut, ce qui signifie que nous pouvons facilement contrôler la position du ruban en ajustant cette variable. Puisque nous utilisons `position: absolute`, nous ne devons pas oublier d'ajouter `position: relative` à l'élément parent du ruban.

Je vais également ajouter un peu de remplissage sur les côtés gauche et droit. Il n'y a pas de logique particulière derrière les `10px` – vous pouvez choisir la valeur que vous voulez.

Maintenant, je vais introduire une autre variable qui contrôlera la partie pliée. Je vais utiliser cette variable pour définir une ombre intérieure `box-shadow: 0 calc(-1*var(--f)) 0 #0005`.

Comme vous pouvez le voir sur la figure ci-dessus, cette ombre ajoutera un calque noir semi-transparent en bas ayant une hauteur égale à la variable `--f`. Je vais également augmenter le remplissage inférieur pour contenir cette ombre `padding: 0 10px var(--f)`.

Ensuite, en utilisant la même variable `--f`, je vais déplacer le ruban un peu vers la droite en remplaçant `right:0` par `right: calc(-1*var(--f))`.

Le code jusqu'à présent ressemble à ceci :

```css
.ribbon-2 {
  --t: 10px; /* le décalage supérieur */
  --f :10px /* contrôle la partie pliée */
  
  position: absolute;
  inset: var(--t) calc(-1*var(--f)) auto auto; /* la valeur de droite est ici*/
  padding:0 10px var(--f);
  background: #BD1550;
  box-shadow: 0 calc(-1*var(--f)) 0 inset #0005; 
}
```

Le code peut sembler étrange (et le résultat aussi), mais tout aura du sens dans l'étape suivante lorsque nous créerons la forme finale.

Dans la quatrième étape (la dernière), nous allons introduire `clip-path` pour découper notre élément. Je vais également ajouter une autre variable `--r` pour contrôler la forme de la flèche du ruban.

Avant d'ajouter le clip-path, je vais d'abord augmenter le remplissage gauche pour avoir l'espace nécessaire pour la forme de la flèche :

```css
padding: 0 10px var(--f) calc(10px + var(--r));
```

* Le remplissage supérieur est égal à `0`.
  
* Le remplissage droit est égal à `10px` (une valeur aléatoire)
  
* Le remplissage inférieur est défini par `--f`
  
* Le remplissage gauche est égal à `10px` (même que droite) plus une valeur définie par la nouvelle variable `--r`
  

Maintenant, ajoutons le `clip-path`. Voici une illustration pour comprendre le chemin qui nous mènera à la forme finale.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-22.png align="left")

*Illustration du clip-path*

Le chemin est défini en utilisant 7 points. En commençant par le point (1) et en suivant la flèche, nous avons le code suivant :

```css
clip-path: polygon(
  0 0,  /* (1) */
  100% 0, /* (2) */
  100% calc(100% - var(--f)), /* (3) */
  calc(100% - var(--f)) 100%, /* (4) */
  calc(100% - var(--f)) calc(100% - var(--f)), /* (5) */
  0 calc(100% - var(--f)), /* (6) */
  var(--r) calc(50% - var(--f)/2) /* (7) */
)
```

Ne vous inquiétez pas si vous n'êtes pas familier avec `clip-path` – cela peut sembler un peu étrange pour vous. Vous n'avez pas besoin de manipuler ce chemin. Tout ce dont vous avez besoin est de mettre à jour les variables CSS pour contrôler la forme globale.

Cela dit, il est bon de jouer avec ce chemin en changeant certaines valeurs afin de mieux comprendre comment il fonctionne.

Nous avons terminé. Notre code final est :

```css
.ribbon-2 {
  --f: 10px; /* contrôle la partie pliée*/
  --r: 15px; /* contrôle la forme du ruban */
  --t: 10px; /* le décalage supérieur */
  
  position: absolute;
  inset: var(--t) calc(-1*var(--f)) auto auto;
  padding: 0 10px var(--f) calc(10px + var(--r));
  clip-path: 
    polygon(0 0,100% 0,100% calc(100% - var(--f)),calc(100% - var(--f)) 100%,
      calc(100% - var(--f)) calc(100% - var(--f)),0 calc(100% - var(--f)),
      var(--r) calc(50% - var(--f)/2));
  background: #BD1550;
  box-shadow: 0 calc(-1*var(--f)) 0 inset #0005;
}
```

Vous pouvez ajuster les valeurs des variables pour obtenir différents résultats :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/right-ribbon.png align="left")

Comme nous l'avons fait avec le ruban tourné, nous pouvons mettre à jour quelques valeurs pour changer la position de celui-ci de droite à gauche – mais cette fois, je ne vous donnerai pas le code. Je vous laisse essayer de le trouver seul 😉

C'est un bon exercice de déterminer quelle valeur vous devez mettre à jour, surtout pour le `clip-path`. Vous pouvez toujours [me contacter](https://twitter.com/ChallengesCss) si vous avez des questions.

## Conclusion

Maintenant, vous savez comment créer de beaux rubans pour vos sites web en utilisant uniquement du CSS.

Si vous voulez plus, consultez ma [collection en ligne de formes de rubans](https://css-generators.com/ribbon-shapes/) où vous trouverez différentes variations similaires à ce que nous avons fait dans cet article.