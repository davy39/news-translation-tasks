---
title: Un guide pour débutants sur CSS Grid
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-20T02:07:53.000Z'
originalURL: https://freecodecamp.org/news/a-beginners-guide-to-css-grid-3889612c4b35
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Si0jHvuuUWXo0qWXCqx2qg.jpeg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Un guide pour débutants sur CSS Grid
seo_desc: 'By Kara Luton

  I first heard about CSS Grid towards the end of 2016. I was sitting at one of my
  first Tech Ladies® meetings and an attendee mentioned hearing how amazing it was.
  Fast forward a year and a half later and I’m finally digging deeper into ...'
---

Par Kara Luton

J'ai entendu parler de CSS Grid pour la première fois vers la fin de l'année 2016. J'étais assise à l'une de mes premières réunions de [Tech Ladies®](https://www.freecodecamp.org/news/a-beginners-guide-to-css-grid-3889612c4b35/undefined) et une participante a mentionné avoir entendu dire à quel point c'était incroyable. Un an et demi plus tard, je me plonge enfin plus profondément dans Grid. En tant qu'utilisatrice dévouée de Flexbox, je peux déjà voir comment cela va être un changement de jeu.

La plus grande question que je me posais en commençant à apprendre CSS Grid était : en quoi Grid est-il différent de Flexbox ? Et j'ai découvert qu'en général, Grid peut faire _tout_ ce que Flexbox peut faire. Certaines personnes pensent que Grid est destiné aux mises en page multidimensionnelles tandis que Flexbox devrait être utilisé pour les mises en page unidimensionnelles. Mais Grid est également excellent pour les mises en page unidimensionnelles, surtout si vous revenez plus tard et décidez que vous voulez rendre cette mise en page multidimensionnelle.

### Installation de CSS Grid

Grid est extrêmement facile à configurer — il suffit de deux lignes de CSS.

**HTML**

```
<div class="wrapper">  <div class="item">1</div>  <div class="item">2</div>  <div class="item">3</div>  <div class="item">4</div>  <div class="item">5</div>  <div class="item">6</div></div>
```

**CSS**

```
.wrapper {    display: grid;    grid-template-columns: 10rem 10rem 10rem;}
```

Et voilà ! Vous avez une grille. Sérieusement, c'est tout ce dont vous avez besoin. C'est plutôt génial.

Vous remarquerez que, contrairement à la configuration de Flexbox avec `display: flex`, l'ajout de `display: grid` à votre wrapper ne fait pas immédiatement une différence. Cela est dû au fait que vous ne définissez pas explicitement combien de colonnes vous voulez que votre grille ait. Vous le ferez avec `grid-template-columns` comme je l'ai fait ci-dessus. Donc dans cet exemple, je définis trois colonnes pour qu'elles aient chacune une largeur de 10rem.

![Image](https://cdn-media-1.freecodecamp.org/images/Wx6aCuxkG9v5RW2lfXqtcx7xK710jszdhC2U)
_Grille CSS de base_

Vous pouvez utiliser n'importe quelle valeur que vous voulez lorsque vous définissez `grid-template-columns`, mais je suggère d'éviter les pourcentages sauf si vous essayez d'atteindre 100%. Cela est dû au fait que vous devrez prendre en compte votre quantité de `grid-gap` (que nous aborderons dans un instant), et cela peut devenir un peu délicat.

### Pistes explicites vs implicites

Avant de parler des pistes explicites et implicites, parlons d'abord de ce que sont les pistes. Les pistes sont la manière dont les colonnes et les lignes sont numérotées. Au lieu de compter les colonnes et les lignes individuelles séparément, dans CSS Grid, vous les comptez par les lignes de piste. Voici la grille avec laquelle nous avons commencé — j'ai numéroté toutes les lignes de piste des colonnes et des lignes pour que ce soit un peu plus facile pour vous de voir.

![Image](https://cdn-media-1.freecodecamp.org/images/Lzsu5YPNOxOKmxdGRo1K2fHWC8iCNfjFjKWA)
_Grille CSS avec les lignes de colonne et de ligne numérotées_

Vous pouvez voir que nous avons en fait quatre lignes de colonne et trois lignes de ligne. Cela aidera lorsque vous placerez vos éléments sur la grille.

**Une rapide note de côté :** si vous utilisez l'édition Developer de Firefox (la version bêta de Firefox régulier), elle dispose en fait de quelques excellents outils de développement pour voir les numéros de piste des colonnes et des lignes. Si vous inspectez votre élément wrapper et allez ensuite dans l'onglet de mise en page, cochez la case pour votre wrapper et maintenant votre grille ressemblera à ce qui suit ! J'espère vraiment que Chrome ajoutera une fonction d'inspection comme celle-ci à l'avenir. C'est extrêmement utile.

![Image](https://cdn-media-1.freecodecamp.org/images/zTYIbSUwg0wmLM23ImHDlbE3KXbnSr-7rZuQ)
_Outil d'inspection de Firefox Developer Edition_

Revenons à la différence entre les pistes explicites et implicites. Si nous prenons notre code ci-dessus, vous remarquerez que nous n'avons défini que nos colonnes. Dans ce cas, nous avons **explicitement** défini nos colonnes pour en avoir trois, mais nous avons **implicitement** défini nos lignes. Nous avons six éléments, mais évidemment tous ces éléments ne peuvent pas tenir dans trois colonnes, donc une deuxième ligne est implicitement définie.

C'est un peu confus, donc je recommande définitivement de manipuler CSS Grid par vous-même pour voir la différence entre les pistes explicites et implicites.

### Ajout de Grid-Gap

Pensez à grid-gap comme à une marge, sauf qu'elle ne sera ajoutée qu'entre les éléments et non à l'extérieur de la grille. J'ai rencontré tant de cas où j'ajoute une marge sur les éléments dans une grille Flexbox pour ensuite devoir aller au wrapper de la grille et définir la même quantité de marge, mais négative, pour compenser la marge qui est définie à l'extérieur de la grille. Heureusement, avec CSS Grid, vous n'avez pas à gérer cela.

Prenons notre exemple CSS ci-dessus et ajoutons un peu de grid-gap.

```
.wrapper {  display: grid;  grid-template-columns: 10rem 10rem 10rem;  grid-gap: 1rem;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/nzT7VWv1P6QnCa6VMPH-D0qlvcl934z5QI8h)
_Grille CSS avec 1rem de grid-gap_

J'ai utilisé la propriété raccourcie `grid-gap`, mais vous pouvez définir une valeur explicite pour les colonnes et les lignes en utilisant `grid-column-gap` et `grid-row-gap`.

_*Note : [Chrome 66](https://blog.chromium.org/2018/03/chrome-66-beta-css-typed-object-model.html) changera `grid-gap` en `gap` et `grid-column-gap`/`grid-row-gap` en `column-gap`/`row-gap`._

### La fonction Repeat()

Définir la largeur de chaque colonne lorsque vous utilisez `grid-template-columns` avec trois colonnes de même largeur est assez simple. Mais cela fait beaucoup de frappe si vous voulez plus de colonnes que cela. C'est là que la fonction `repeat()` entre en jeu.

Voici notre exemple que nous avons utilisé avec la fonction `repeat()` ajoutée.

```
.wrapper {  display: grid;  grid-template-columns: repeat(3, 10rem);  grid-gap: 1rem;}
```

Comme vous pouvez le voir dans mon CSS, je définis trois colonnes, chacune à 10rem de large. Cette grille ressemblera exactement à la grille illustrée dans notre exemple de grid-gap. En utilisant la fonction `repeat()`, nous rendons simplement l'écriture un peu plus simple et plus facile à lire lorsque vous souhaitez définir de nombreuses colonnes.

### Unités fractionnaires

Les unités fractionnaires, ou fr, sont une nouvelle unité de longueur CSS introduite avec CSS Grid et que je peux voir utiliser tout le temps. Supposons que nous voulons trois colonnes de largeur égale. Au lieu de définir `width: calc(100% / 3)` sur les éléments, nous pouvons utiliser des unités fractionnaires. Pensez aux unités fractionnaires comme à de l'« espace libre ».

Continuons avec notre exemple que nous avons utilisé.

```
.wrapper {  display: grid;  grid-template-columns: 1fr 1fr 1fr;  grid-gap: 1rem;}
```

Vous remarquerez que la seule chose que j'ai changée est `grid-template-columns`. Je dis maintenant au navigateur que je veux trois colonnes, et que je veux que chacune de ces colonnes occupe une unité fractionnaire ou un « espace libre ». Cela fonctionne de manière très similaire à la propriété `flex-grow` de Flexbox.

![Image](https://cdn-media-1.freecodecamp.org/images/1IN8vd78DiJjP6-KMqXEM3iK9oc0A6RsdYzF)
_Grille CSS utilisant des unités fractionnaires_

La raison pour laquelle chaque élément est un peu plus large que dans notre exemple précédent est qu'ils occupent maintenant autant d'espace que possible tout en tenant toujours dans trois colonnes. Dans ce cas, je n'ai pas défini une largeur fixe, donc ils occupent la largeur complète de mon écran. Je sais que c'est un peu difficile à voir sans l'avoir sur votre propre écran, donc je recommande définitivement de manipuler cela par vous-même.

Vous n'êtes pas obligé de définir toutes vos colonnes à 1fr non plus. Ci-dessous se trouve un exemple où j'ai défini ma première et troisième colonne à 10rem tandis que ma colonne du milieu est à 1fr. Vous pouvez également définir vos colonnes à 2fr, 3fr, et ainsi de suite, et les éléments de cette colonne occuperont 2x, 3x (et ainsi de suite) la quantité d'espace.

![Image](https://cdn-media-1.freecodecamp.org/images/gTdHQ0Sm6kYAV8PUx9PcgDPvI0oz0bxeU2D0)
_Grille CSS avec seulement la colonne du milieu définie à 1fr_

### Dimensionnement des éléments individuels de la grille

Parlons du dimensionnement de nos éléments individuels de la grille. Vous ne pouvez pas placer une largeur fixe sur des éléments individuels, car nous avons explicitement défini la largeur avec `grid-template-columns`. Mais que faire si vous voulez que l'élément cinq dans notre exemple ait la largeur de plusieurs colonnes ? Nous pouvons faire cela en utilisant `grid-column` et `span`.

```
.wrapper {  display: grid;  grid-template-columns: repeat(3, 10rem);  grid-gap: 1rem;}
```

```
.item5 {  grid-column: span 2;}
```

Vous verrez ci-dessus que nous définissons `grid-column` de l'élément cinq pour qu'il s'étende sur deux, ce qui permettra à l'élément cinq de s'étendre sur une largeur de deux colonnes.

![Image](https://cdn-media-1.freecodecamp.org/images/PZKKIczjUcd2HeOw3EzIHTCYp3Z-9csboNjB)
_Grille CSS avec span sur un élément individuel_

Mais que faire si vous voulez que l'élément cinq s'étende sur trois colonnes ? Voici ce qui se passera.

![Image](https://cdn-media-1.freecodecamp.org/images/DzshGlWqLrUDYAqbFz80hdTzlLqcVzHAyTQJ)
_Grille CSS étendant l'élément cinq sur trois colonnes_

Parce que l'élément cinq commence naturellement à la deuxième colonne, nous n'avons pas assez d'espace pour qu'il s'étende sur la largeur totale que nous avons définie. Il passera donc à la ligne suivante. Vous pouvez appliquer le même concept de `grid-column` à `grid-row` si vous voulez qu'un élément s'étende sur plusieurs lignes.

Il existe une solution assez simple pour corriger l'espace vide qui reste lorsque l'élément cinq descend d'une ligne. Elle peut être utilisée que vous définissiez un élément pour qu'il s'étende sur une ligne ou une colonne — `grid-auto-flow: dense`.

```
.wrapper {  display: grid;  grid-template-columns: repeat(3, 10rem);  grid-gap: 1rem;  grid-auto-flow: dense;}
```

```
.item5 {  grid-column: span 3;}
```

Dans CSS Grid, la grille vérifie automatiquement si les éléments s'adaptent. Comme je l'ai dit ci-dessus, si un élément ne s'adapte pas, il passera à la ligne suivante. `Grid-auto-flow: dense` indique à la grille de remplir ces espaces vides avec n'importe quel élément qui s'adaptera. Dans ce cas, j'ai ajouté un septième élément de grille, donc la grille déplace automatiquement celui-ci et le sixième élément vers les espaces vides.

CSS Grid disposera toujours les éléments qui doivent aller à un endroit spécifique en premier — dans ce cas, l'élément cinq, puisqu'il s'étend sur trois colonnes. Ensuite, si vous avez défini `grid-auto-flow: dense`, il cherchera d'autres éléments à adapter aux espaces vides sur la grille.

![Image](https://cdn-media-1.freecodecamp.org/images/e34AFH8TDnMbKaG21HzgjJvqa5msz02C0OD5)
_Grille CSS avec grid-auto-flow: dense_

La propriété `grid-auto-flow` seule détermine dans quelle direction vous devez ajouter une autre ligne ou colonne après avoir déjà défini vos éléments. La ligne est la valeur par défaut. Je n'ai pas vu de cas d'utilisation majeur pour cela en dehors de l'utilisation de `grid-auto-flow: dense`.

### Placement des éléments de la grille

Dans notre exemple de dimensionnement des éléments individuels de la grille, nous définissions à l'origine l'élément cinq à `grid-column: span 2`, ce qui permettait à l'élément cinq de s'étendre sur deux colonnes. En fait, `grid-column` est un raccourci pour `grid-column-start` et `grid-column-end`. Il en va de même pour `grid-row`.

Donc, techniquement, nous définissions l'élément cinq à `grid-column-start: span 2` et `grid-column-end: auto`. Essentiellement, nous disions à la grille de commencer l'élément cinq là où il le ferait naturellement, mais d'aller deux fois la taille.

Travaillons à nouveau avec l'élément cinq, et je vais vous montrer cela en utilisant les outils d'inspection de l'édition Developer de Firefox pour que ce soit plus facile pour vous de voir sur quelle ligne de piste se trouve l'élément cinq. J'ai également ajouté quelques éléments de grille supplémentaires.

```
.wrapper {  display: grid;  grid-template-columns: repeat(3, 10rem);  grid-gap: 1rem;}
```

```
.item5 {  grid-column-start: 1;  grid-column-end: 3;}
```

CSS Grid disposera tous les éléments avant notre cinquième, s'arrêtera puis regardera où nous avons commencé et terminé l'élément cinq, et le placera où nous lui avons dit de le faire. Le raccourci de cela serait `grid-column: 1 / 3` où 1 est notre valeur de départ et 3 est notre valeur de fin.

![Image](https://cdn-media-1.freecodecamp.org/images/C4MNJnfRJUwGoFqKM69a4y2k16-fLP0lCIrL)
_Grille CSS utilisant grid-column-start et grid-column-end_

Vous pouvez également indiquer à un élément de grille individuel la largeur que vous voulez qu'il occupe et où vous voulez qu'il se termine. J'utilise la propriété raccourcie `grid-column` dans cet exemple, donc je dis à l'élément cinq de s'étendre sur deux colonnes se terminant à la ligne de piste quatre.

```
.wrapper {  display: grid;  grid-template-columns: repeat(3, 10rem);  grid-gap: 1rem;}
```

```
.item5 {  grid-column: span 2 / 4;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/LuGjQJfITo7W4To2qDog3V6qdaFO7DOfvq-N)
_Grille CSS avec la propriété raccourcie grid-column_

Si vous voulez que votre élément occupe toute la largeur de la grille, mais que vous ne savez pas à quel point votre grille est large, vous pouvez définir `grid-column: 1 / -1`. En gros, cette valeur -1 indique à votre élément d'aller jusqu'à la dernière ligne de piste. Si vous faites cela avec des lignes, vous remarquerez que votre élément n'ira peut-être pas jusqu'en bas de votre grille. Il n'ira que jusqu'en bas de vos lignes **explicites**, et non de vos lignes implicites.

### Ressources

Voici quelques ressources que je recommande vivement pour une exploration plus approfondie de CSS Grid !

* [Tutoriel CSS Grid de Wes Bos](https://cssgrid.io/) — il est totalement gratuit et c'est là que j'ai appris la grille. J'adore son style d'enseignement !
* [Guide complet de CSS Grid de CSS Tricks](https://css-tricks.com/snippets/css/complete-guide-grid/) — cela contient quelques excellents aide-mémoire pour lorsque vous êtes bloqué sur un aspect particulier de Grid.
* [CSS Grid Garden](https://cssgridgarden.com/) — une manière amusante de pratiquer ce que vous avez appris sur CSS Grid. Je recommande de faire un tutoriel avant d'essayer cela, car cela peut devenir un peu confus à certains moments.

Merci d'avoir lu mon tutoriel sur CSS Grid ! Consultez mes autres articles comme [Comment répondre à la question redoutée de l'entretien « Parlez-moi de vous »](https://medium.freecodecamp.org/how-to-answer-the-dreaded-tell-me-about-yourself-interview-question-cec7137ca17b), [Pourquoi vous devriez embaucher un diplômé de bootcamp](https://medium.com/@karaluton/why-you-should-hire-a-bootcamp-grad-49874ccee2e0) ou [mon histoire de comment je suis devenue développeuse](https://medium.com/@karaluton/from-music-publicist-to-web-developer-767b023c44cd).

Et n'oubliez pas de me suivre sur Twitter pour beaucoup de tweets sur la technologie et, si je suis honnête, beaucoup de tweets sur les chiens aussi.

[**Kara Luton (@karaluton) | Twitter**](https://twitter.com/karaluton)  
[_Les derniers tweets de Kara Luton (@karaluton). Développeuse front-end + ancienne attachée de presse musicale. Ex-ballerine… twitter.com](https://twitter.com/karaluton)