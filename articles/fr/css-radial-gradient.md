---
title: Apprendre CSS radial-gradient en créant des motifs d'arrière-plan
subtitle: ''
author: Temani Afif
co_authors: []
series: null
date: '2022-04-19T01:12:33.000Z'
originalURL: https://freecodecamp.org/news/css-radial-gradient
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/pattern-header.png
tags:
- name: CSS
  slug: css
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Apprendre CSS radial-gradient en créant des motifs d'arrière-plan
seo_desc: 'If you are new to CSS gradients, you may have heard about something called
  radial-gradient(). If you have never used it before, you are in the right place
  to learn about it.

  In this tutorial, I will focus on some real and practical examples to explai...'
---

Si vous êtes nouveau dans les dégradés CSS, vous avez peut-être entendu parler de quelque chose appelé `radial-gradient()`. Si vous ne l'avez jamais utilisé auparavant, vous êtes au bon endroit pour en apprendre davantage.

Dans ce tutoriel, je vais me concentrer sur quelques exemples réels et pratiques pour expliquer les secrets derrière `radial-gradient()` et son fonctionnement.

Les dégradés CSS sont généralement utilisés pour créer des motifs fantaisistes, donc j'ai sélectionné quelques-uns d'entre eux réalisés uniquement avec `radial-gradient()`. En les construisant, nous apprendrons tout sur ces dégradés.

## Motif de radial-gradient #1

Commençons par le motif le plus basique.

![Motif réalisé avec radial-gradient](https://www.freecodecamp.org/news/content/images/2022/04/pattern-1.png align="left")

*Motif réalisé avec radial-gradient*

Rien de complexe pour l'instant – nous répétons simplement des cercles. Cercles, ellipses, demi-cercles, un quart de cercle, et ainsi de suite... toutes sont des formes différentes que nous pouvons créer en utilisant `radial-gradient()`.

Pour simplifier, nous pouvons considérer l'ellipse comme la forme principale puisque un cercle est un cas particulier d'une ellipse. Ensuite, en cachant certaines parties, nous obtenons la moitié d'un cercle, un quart de cercle, et ainsi de suite.

Zoomons sur le motif pour identifier les différentes valeurs.

![Illustration des différentes valeurs du motif](https://www.freecodecamp.org/news/content/images/2022/04/image-128.png align="left")

*Illustration des différentes valeurs du motif*

Nous dessinons dans une zone qui a des dimensions de `100px*100px`, ce qui est notre `background-size`. Nous considérerons un rayon horizontal égal à `50%` et un rayon vertical égal à `50%`, et le centre de notre forme sera le centre de la zone.

Une ellipse est définie avec deux rayons appelés le "rayon horizontal" et le "rayon vertical". Si les deux sont égaux (comme dans notre cas), nous obtenons un cercle.

Cela nous donnera le code suivant :

```css
html {
  background-image: radial-gradient(50% 50% at center, ???);
  background-size: 100px 100px   
}
```

Nous avons défini le paramétrage de notre dégradé, et maintenant nous devons définir la configuration des couleurs. Nous allons dessiner un cercle qui ne touchera pas le bord de la zone `background-size`. À partir de `50%`, nous aurons `80%` de la couleur principale et le reste sera transparent.

```css
html {
  background-image: radial-gradient(50% 50% at center, #c39f76 0% 80%,#0000 81% 100%);
  background-size: 100px 100px   
}
```

En gros, nous définissons d'abord le centre et la taille de notre ellipse (le `50% 50% at center`), puis nous la remplissons avec une coloration dégradée (le `c39f76 0 80%,#0000 81% 100%`). Nous obtenons un cercle complet dans ce cas parce que les deux rayons sont égaux (`50%` de `100px`) et parce que nous n'avons pas de transition entre les couleurs.

Nous avons la couleur principale de `0%` à `80%` et transparent de `81%` à `100%`. (Nous aurions dû utiliser `80%` au lieu de `81%`, mais nous gardons une petite transition pour éviter les bords dentelés.)

Nous pouvons optimiser le code ci-dessus en supprimant les valeurs par défaut pour obtenir ceci :

```css
html {
  background-image: radial-gradient(50% 50%,#c39f76 80%,#0000 81%);
  background-size: 100px 100px   
}
```

La position est par défaut le centre et nous pouvons omettre `0%` et `100%` de la configuration des couleurs.

Ce qui précède n'est pas la seule syntaxe pour obtenir ce motif. Nous pouvons également utiliser :

```css
html {
  background-image: radial-gradient(40% 40%,#c39f76 99%,#0000);
  background-size: 100px 100px   
}
```

Nous réduisons le rayon de notre cercle et nous augmentons le pourcentage de la couleur principale. Notez que je n'ai pas défini de pourcentage avec la couleur transparente puisque ce devrait être `100%` (la valeur par défaut) que nous pouvons omettre.

Nous pouvons aussi utiliser :

```css
html {
  background-image: radial-gradient(#c39f76 56%,#0000 57%);
  background-size: 100px 100px   
}
```

Nous omettons le rayon et le navigateur utilisera un paramétrage par défaut qui nécessite une autre configuration de couleur.

Vous n'avez pas à mémoriser tous les cas, contentez-vous d'une méthode facile (je recommande la première). Plus tard, avec la pratique, vous découvrirez différentes façons d'obtenir le même résultat et vous pourrez optimiser votre syntaxe pour réduire la quantité de code utilisée comme je l'ai fait avec le dernier exemple.

## Motif de radial-gradient #2

![Motif réalisé avec radial-gradient](https://www.freecodecamp.org/news/content/images/2022/04/pattern-2.png align="left")

*Motif réalisé avec radial-gradient*

Pour celui-ci, j'utiliserai 2 `radial-gradient()`. N'oublions pas que nous pouvons avoir autant de couches d'arrière-plan que nous voulons. C'est une fonctionnalité géniale qui nous permet de construire des motifs complexes en combinant différents dégradés avec différentes configurations.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-129.png align="left")

Nous gardons la même `background-size` ici, mais nous utilisons différentes positions pour nos cercles. Le code sera le suivant :

```css
html {
   background-image: 
     radial-gradient(?? at 25% 25%,??),
     radial-gradient(?? at 75% 75%,??);
   background-size: 100px 100px; 
}
```

Pour la configuration du rayon, si nous faisons quelques calculs, nous pouvons trouver que nous avons besoin de `25%` pour les deux cercles pour toucher les bords. Nous pouvons donc utiliser ce code :

```css
html {
   background-image: 
     radial-gradient(25% 25% at 25% 25%,#c39f76 80%,#0000 81%),
     radial-gradient(25% 25% at 75% 75%,#c39f76 80%,#0000 81%);
   background-size: 100px 100px; 
}
```

Nous pouvons aussi utiliser `closest-side` au lieu de `25% 25%`. Je sais, c'est une valeur étrange, mais elle signifie "utiliser une valeur de rayon qui permet au cercle de toucher le côté le plus proche de son centre". Cette valeur est utile et peut nous éviter de traiter avec certains calculs complexes.

```css
html {
   background-image: 
     radial-gradient(closest-side at 25% 25%,#c39f76 80%,#0000 81%),
     radial-gradient(closest-side at 75% 75%,#c39f76 80%,#0000 81%);
   background-size: 100px 100px; 
}
```

`radial-gradient()` nous fournit 3 autres valeurs similaires (`closest-corner`, `farthest-side`, et `farthest-corner`). Nous définissons soit une taille explicite pour notre rayon, soit nous utilisons ces valeurs et le navigateur trouvera automatiquement le rayon basé sur des règles spécifiques.

Comme je l'ai dit précédemment, vous n'avez pas besoin de tout mémoriser. J'essaie de me concentrer sur les bases de `radial-gradient()` tout en fournissant autant d'informations que possible que vous pourrez utiliser plus tard.

## Motif de radial-gradient #3

![Image](https://www.freecodecamp.org/news/content/images/2022/04/pattern-3.png align="left")

J'augmente la difficulté avec celui-ci. Après les 1er et 2ème motifs, nous pouvons maintenant essayer un motif plus complexe. Celui-ci est également fait en utilisant deux dégradés où nous n'aurons pas de cercles complets mais une combinaison de deux demi-cercles.

Voici une illustration pour vous aider à comprendre le puzzle. J'utilise différentes couleurs pour identifier facilement chaque dégradé.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-130.png align="left")

Le centre pour le premier dégradé est placé à `50% 100%` tandis que le second est placé à `50% 0%`, mais nous pouvons aussi utiliser `top` et `bottom` comme leurs valeurs équivalentes.

```css
html {
   background-image: 
     radial-gradient(?? at top   ,??),
     radial-gradient(?? at bottom,??);
   background-size: 100px 100px; 
}
```

Pour le rayon, nous pouvons utiliser `50% 50%` comme nous l'avons fait auparavant, mais cette fois je vais essayer quelque chose de différent et considérer `50px` qui est la moitié de la `background-size`.

Lorsque nous utilisons une valeur en pixels ou toute unité différente d'un pourcentage, nous pouvons spécifier un seul rayon et le navigateur comprendra que nous voulons un cercle avec ce rayon. C'est encore une autre façon de définir la taille de notre forme en plus du pourcentage et des valeurs spécifiques.

Notre cercle touche le bord, donc le code sera :

```css
html {
   background-image: 
     radial-gradient(50px at top   ,#c39f76 99%,#0000),
     radial-gradient(50px at bottom,#c39f76 99%,#0000);
   background-size: 100px 100px; 
}
```

Oui, ce qui précède ne nous donnera pas le motif que nous recherchons – nous avons encore besoin d'une touche finale. Si vous vérifiez l'illustration précédente, vous remarquerez que le second dégradé (le vert) est décalé vers la droite de la moitié de la taille. En d'autres termes, nous devons mettre à jour sa `background-position` :

```css
html {
   background-image: 
     radial-gradient(50px at top   ,#c39f76 99%,#0000),
     radial-gradient(50px at bottom,#c39f76 99%,#0000);
   background-position: 0 0, 50px 0;
   background-size: 100px 100px; 
}
```

Nous pouvons optimiser un peu le code en utilisant la version raccourcie :

```css
html {
   background: 
     radial-gradient(50px at top   ,#c39f76 99%,#0000),
     radial-gradient(50px at bottom,#c39f76 99%,#0000) 50px 0;
   background-size: 100px 100px; 
}
```

Et puisque nous traitons avec des valeurs en pixels, nous pouvons ajouter une variable CSS pour faciliter l'ajustement du code.

```css
html {
   --s: 100px;
   background: 
     radial-gradient(calc(var(--s)/2) at top   ,#c39f76 99%,#0000),
     radial-gradient(calc(var(--s)/2) at bottom,#c39f76 99%,#0000) calc(var(--s)/2) 0;
   background-size: var(--s) var(--s); 
}
```

Au lieu de mettre à jour différentes valeurs, nous en changeons une seule !

## Motif de radial-gradient #4

![Motif d'arrière-plan réalisé avec radial-gradient](https://www.freecodecamp.org/news/content/images/2022/04/pattern-4.png align="left")

*Motif d'arrière-plan réalisé avec radial-gradient*

À première vue, cet arrière-plan semble un peu complexe. Mais si nous pouvons identifier le bon motif, cela devient facile.

C'est la partie la plus difficile lorsque nous traitons avec un tel arrière-plan. Parfois, il n'est pas facile d'identifier les différentes couches d'arrière-plan. Mon conseil pour vous améliorer dans cet exercice est de pratiquer.

Intuitivement, vous pourriez penser que le motif est celui-ci et vous aurez du mal à trouver les dégradés

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-131.png align="left")

mais ce n'est pas le cas. Le vrai motif est celui-ci

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-132.png align="left")

Nous avons 4 cercles placés aux coins avec un petit débordement. Le code sera :

```css
html {
   background: 
     radial-gradient(closest-corner at 20% 20%,#c39f76 98%,#0000),
     radial-gradient(closest-corner at 80% 20%,#c39f76 98%,#0000),
     radial-gradient(closest-corner at 20% 80%,#c39f76 98%,#0000),
     radial-gradient(closest-corner at 80% 80%,#c39f76 98%,#0000);
   background-size: 100px 100px;
}
```

Une bonne utilisation de `closest-corner` pour définir le rayon. Pour chaque couche, le navigateur dessine un cercle placé à une position spécifique et touche le coin le plus proche. Ce paramétrage nous permet d'utiliser une configuration de couleur facile tout en ayant le débordement nécessaire.

Nous pouvons aussi utiliser `closest-side` comme ci-dessous :

```css
html {
   background: 
     radial-gradient(closest-side at 20% 20%,#c39f76 140%,#0000 141%),
     radial-gradient(closest-side at 80% 20%,#c39f76 140%,#0000 141%),
     radial-gradient(closest-side at 20% 80%,#c39f76 140%,#0000 141%),
     radial-gradient(closest-side at 80% 80%,#c39f76 140%,#0000 141%);
   background-size: 100px 100px;
}
```

La seule nouveauté dans le code ci-dessus est la configuration des couleurs où j'utilise des valeurs supérieures à `100%`. Puisque j'utilise `closest-side` pour définir le rayon, j'ai besoin d'aller au-delà de `100%` pour créer le débordement.

N'oubliez pas un tel truc, il peut être utile. Les valeurs de couleur ne sont pas limitées à la plage `[0% 100%]` – elles peuvent aller plus loin.

Dans une telle situation, nous pouvons également nous appuyer sur une variable CSS pour éviter la répétition de la configuration des couleurs :

```css
html {
   --c: #c39f76 98%,#0000;
   background: 
     radial-gradient(closest-corner at 20% 20%,var(--c)),
     radial-gradient(closest-corner at 80% 20%,var(--c)),
     radial-gradient(closest-corner at 20% 80%,var(--c)),
     radial-gradient(closest-corner at 80% 80%,var(--c));
   background-size: 100px 100px;
}
```

## Motif de radial-gradient #5

![Image](https://www.freecodecamp.org/news/content/images/2022/04/pattern-5.png align="left")

*Motif réalisé avec radial-gradient*

Voici un autre motif non intuitif qui peut en confondre beaucoup d'entre vous. Vous pouvez le voir comme un cercle qui est à moitié rempli et vous vous demandez peut-être comment il est possible d'y parvenir. En réalité, c'est une combinaison de deux demi-cercles comme ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-133.png align="left")

Et voici leur code :

```css
html {
  background:
    radial-gradient(50% 50% at left ,#0000 70%,#c39f76 71% 80%,#0000 81%),
    radial-gradient(50% 50% at right,#c39f76 0 80%,#0000 81%);
  background-size: 100px 100px;
}
```

Cette fois, nous utilisons une configuration de couleur différente pour chacun. Le premier a 3 couleurs (transparent, puis la couleur principale, puis transparent à nouveau). Le second a la même configuration de couleur que nous avons utilisée avec les exemples précédents.

Ce motif est un bon exemple pour montrer comment différentes configurations de couleurs peuvent être une autre façon d'obtenir des motifs d'arrière-plan complexes.

## Motif de radial-gradient #6

![Image](https://www.freecodecamp.org/news/content/images/2022/04/pattern-6.png align="left")

C'est un autre motif où il n'est pas facile d'identifier les différentes couches – mais si nous regardons de près, nous pouvons voir deux cercles

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-134.png align="left")

Le grand cercle est notre première couche

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-135.png align="left")

C'est un cercle placé au centre de la zone (définie avec `background-size` comme d'habitude), mais cette fois la configuration des couleurs n'est pas habituelle. J'utilise une couleur transparente pour la partie intérieure et la couleur principale à l'extérieur. Il convient de noter que nous avons également un petit débordement.

```css
html {
  background-image: radial-gradient(54% 54%,#0000 98%,#c39f76);
  background-size: 100px 100px;
}
```

Comme vous pouvez le voir, j'utilise `54%` au lieu de `50%` pour créer le débordement.

La deuxième couche est un cercle plus petit avec la couleur blanche comme couleur principale. Le code complet sera :

```css
html {
  background: 
    radial-gradient(10% 10%,#fff 98%,#0000),
    radial-gradient(54% 54%,#0000 98%,#c39f76) 50px 50px;
  background-size:100px 100px;
}
```

Notez l'utilisation de `50px 50px`. Comme avec le 3ème motif, nous devons décaler l'une des couches de la moitié de la taille pour obtenir le résultat correct – sinon les deux cercles auront le même centre, ce qui n'est pas le résultat souhaité.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-137.png align="left")

## Motif de radial-gradient #7

Voici le dernier motif avant de terminer :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/pattern-7.png align="left")

Avec cet dernier exemple, je veux vous présenter `repeating-radial-gradient()` qui est une autre façon d'écrire `radial-gradient()`.

Notre motif est le suivant :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-138.png align="left")

Nous pouvons réaliser ce qui précède en utilisant `radial-gradient()`, mais la configuration des couleurs deviendra trop longue (transparent, couleur principale, transparent, couleur principale, et ainsi de suite).

Dans ce cas, la configuration des couleurs n'est rien d'autre qu'un motif répété de "transparent, couleur principale" et `repeating-radial-gradient()` est fait à cet effet. Il nous permet de définir une configuration de couleur de motif.

```css
html {
  background-image: repeating-radial-gradient(#0000 0% 12%,#c39f76 13% 26% );
  background-size:100px 100px;
}
```

Ce qui précède signifie que nous avons `12%` de couleur transparente puis `13%` de la couleur principale (`26 - 13 = 13`), puis nous répétons la même chose jusqu'à ce que nous couvions toute la zone.

## Conclusion

En explorant comment créer différents motifs d'arrière-plan, nous avons couvert les bases de `radial-gradient()`.

L'article se termine ici, mais ce n'est que le début. `radial-gradient()` est plus complexe que les simples exemples que nous venons de voir – mais maintenant vous avez les outils nécessaires pour pratiquer et vous y habituer.

Allez-y et essayez de construire votre propre motif en utilisant `radial-gradient()`. Si vous avez besoin d'inspiration, consultez [ma collection de motifs CSS](https://css-pattern.com/) (plus de 100 utilisant des dégradés CSS). J'ai aussi [un autre article sur `conic-gradient()`](https://verpex.com/blog/website-tips/how-to-create-background-pattern-using-css-conic-gradient) si vous voulez une suite à celui-ci.

Voici une autre référence pour obtenir plus de détails :

%[https://developer.mozilla.org/en-US/docs/Web/CSS/gradient/radial-gradient]