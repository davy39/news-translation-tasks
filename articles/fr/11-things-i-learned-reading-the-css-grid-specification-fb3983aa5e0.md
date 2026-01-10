---
title: 11 choses que j'ai apprises en lisant la spécification CSS Grid
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-10T21:24:45.000Z'
originalURL: https://freecodecamp.org/news/11-things-i-learned-reading-the-css-grid-specification-fb3983aa5e0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_bY8jlwMIB_Mr1XJ_aJ9Ug.png
tags:
- name: CSS Grid
  slug: css-grid
- name: grid layout
  slug: grid-layout
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: 11 choses que j'ai apprises en lisant la spécification CSS Grid
seo_desc: 'By Emmanuel Ohans

  June 11, 2017, I decided to read the CSS Grid spec.

  The Spec was a little bit technical, but it was by far the most enjoyed specification
  I had ever read. If you’re a more advanced developer, bookmark it for future references.

  So, w...'
---

Par Emmanuel Ohans

Le 11 juin 2017, j'ai décidé de lire la spécification CSS Grid.

La spécification était un peu technique, mais c'était de loin la spécification la plus agréable que j'aie jamais lue. Si vous êtes un développeur plus avancé, [marquez-la](https://www.w3.org/TR/css-grid-1/) pour de futures références.

### Alors, cela sera-t-il utile ?

Je crois que la différence entre les bons et les grands ingénieurs, c'est que ces derniers prennent le temps de comprendre ce qui se passe vraiment sous le capot. Ils apprennent comment les choses fonctionnent, au lieu d'apprendre par "copier-coller".

Alors, voulez-vous être un grand développeur ?

Bien sûr. Sinon, vous ne seriez pas en train de lire cet article.

### Ce que vous allez apprendre

En lisant la spécification, j'ai appris des détails très subtils, mais profonds.

Dans cet article, je vais les partager avec vous.

### 1. Le CSS Grid est déclaratif

Les API déclaratives sont si agréables à utiliser. Pensez à [ReactJS](http://reactjs.org) ?

Alors que les sites web évoluaient de simples documents vers des applications complexes et interactives, les mises en page web sont devenues difficiles à composer. Si difficiles, qu'elles étaient mon cauchemar.

C'est exactement le problème que CSS Grid est venu résoudre aujourd'hui.

![Image](https://cdn-media-1.freecodecamp.org/images/1*42E2QtypEfccqXqb640jMw.png)
_De la spécification._

CSS Grid élimine le processus douloureux de création de mises en page intelligentes et le remplace par un ensemble de règles déclaratives qui rendent le processus presque sans effort.

Ce sont de bons moments dans l'histoire de CSS.

### 2. L'unité fractionnaire ne produit pas toujours des lignes et colonnes également espacées

L'une des premières choses que tout le monde apprend et aime à propos de CSS Grid est l'[unité fractionnaire](https://medium.com/flexbox-and-grids/the-css-fractional-unit-fr-in-approachable-plain-language-fdc47bd387f7). Même un canard peut s'en sortir.

L'unité fractionnaire élimine la douleur de calculer les pourcentages. C'est un plaisir de travailler avec.

La plupart des gens enseignent que l'unité fractionnaire (fr) donne des colonnes ou des lignes également espacées.

Par exemple, une déclaration comme `1fr 1fr 1fr` est censée vous donner des colonnes ou des lignes d'espacement égal. Voir l'illustration ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1*1TWb0kZ4nn6uvykRLMGtOw.png)
_Colonnes également espacées créées par l'unité fractionnaire._

Malheureusement, ce n'est PAS toujours vrai. Pauvre canard.

Ce qui suit est extrait de la spécification :

> L'unité `fr` remplit l'espace disponible MAIS elle n'est JAMAIS plus petite que la taille minimale du conteneur de la grille ou le contenu de la ligne ou de la colonne.

Essentiellement, si vous avez une image, `img` ou tout élément de grille, avec une déclaration `min-width` ou `min-height`, vous pouvez obtenir des résultats inattendus avec l'unité fractionnaire.

Après avoir cancanné comme un canard mouillé et effrayé, j'ai passé beaucoup de temps à expérimenter avec l'unité fractionnaire. J'ai écrit un [article](https://medium.com/flexbox-and-grids/what-you-didnt-know-about-the-css-fractional-unit-580bd62647e8) sur mes découvertes.

### 3. Vous ne savez pas vraiment comment les grilles sont dimensionnées. Ou, le savez-vous ?

Une définition de grille CSS commence toujours par quelque chose comme ceci :

```css
display: grid
```

Souvent, elle est suivie par les définitions de `row` et `column`. Quelque chose comme ceci :

```css
grid-template-rows: 10px 1fr 3fr
grid-template-columns: 1fr
```

Et enfin, vous êtes susceptible de placer les éléments de la grille avec la technique qui vous convient.

Puisqu'il existe de nombreuses façons de placer les éléments de la grille, je vais sauter le code requis pour plus de concision.

Donc, voici le problème.

Sous le capot, vous devez supposer que la taille des lignes et des colonnes de la grille est d'abord calculée avant que les éléments ne soient placés. N'est-ce pas ?

Eh bien, il semble que la vérité soit tout à fait l'inverse.

C'est bizarre.

Ce qui suit est extrait de la spécification :

> _2.3. Dimensionnement de la grille_  
>   
> **_Une fois les éléments de la grille placés_**_, les tailles des pistes de la grille (lignes et colonnes) sont calculées, en tenant compte des tailles de leur contenu et/ou de l'espace disponible tel que spécifié dans la définition de la grille._

Notez la progression.

1. Les éléments de la grille sont placés.
2. Les tailles des pistes de la grille sont calculées

Vous êtes susceptible d'avoir des questions à ce sujet. Alors, je vais essayer de résoudre ces préoccupations.

Tout d'abord, notez que chaque élément de la grille se voit attribuer une `grid-area`. Les éléments de la grille sont ensuite dimensionnés dans cette zone. Donc, comment exactement les éléments de la grille sont-ils placés sans déjà calculer la taille des pistes ?

Si vous regardez la section [Placement des éléments de la grille](https://www.w3.org/TR/css-grid-1/#placement) de la spécification, vous trouverez un indice.

Beaucoup de choses sont prises en considération lors du dimensionnement des grilles, et cela inclut largement la taille des éléments de la grille.

Le dimensionnement des grilles peut être basé sur les éléments suivants :

* Une fonction de dimensionnement fixe (`[length](https://www.w3.org/TR/css3-values/#length-value)` ou un pourcentage résolvable `[percentage](https://www.w3.org/TR/css3-values/#percentage-value)`).
* Une fonction de dimensionnement intrinsèque (`[min-content](https://www.w3.org/TR/css-grid-1/#valdef-grid-template-columns-min-content)`, `[max-content](https://www.w3.org/TR/css-grid-1/#valdef-grid-template-columns-max-content)`, `[auto](https://www.w3.org/TR/css-grid-1/#valdef-grid-template-columns-auto)`, `[fit-content()](https://www.w3.org/TR/css-grid-1/#valdef-grid-template-columns-fit-content)`), ou
* Une fonction de dimensionnement flexible (`[flex](https://www.w3.org/TR/css-grid-1/#typedef-flex)`).

Ce que je crois se passe sous le capot, c'est que les éléments de la grille sont placés.

C'est-à-dire, le bloc conteneur pour l'élément est déterminé, la fonction de dimensionnement pour l'élément est ensuite déterminée. Cela influence à son tour la taille des pistes de la grille.

Vous voyez ?

Pas ce que vous pensiez initialement.

### 4. Par défaut, les éléments de la grille sont étirés pour s'adapter à leur zone de grille — sauf dans certains cas

Sans votre intervention, les éléments de la grille s'étireront toujours pour s'adapter à leur zone de grille.

Donc, si vous aviez une déclaration comme ceci :

```css
grid-template-areas: 'header header header'
                     'sidebar main  main'
                     'sidebar footer footer'
```

Et que vous aviez des `divs` assignés aux zones de grille spécifiques, comme ceci :

```css
.div1 {
   grid-area: header
}
.div2 {
   grid-area: sidebar
}
.div3 {
   grid-area: main
}
.div4 {
   grid-area: footer
}
```

Vous n'avez pas besoin de déclarer la `width` et la `height` des `divs` ci-dessus à `100%`

Ils s'étireront automatiquement pour remplir leurs zones respectives.

Maintenant, voici le piège.

Ce comportement est incohérent avec les images.

%[https://twitter.com/OhansEmmanuel/status/937989769199538177?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E937989769199538177&ref_url=https%3A%2F%2Fmedium.com%2Fmedia%2F78db622c8451a1502c78fa03c8da0d71%3FpostId%3Dfb3983aa5e0]

Comme l'a souligné [Rachel Andrew](https://www.freecodecamp.org/news/11-things-i-learned-reading-the-css-grid-specification-fb3983aa5e0/undefined), la [spécification](https://www.w3.org/TR/css-grid-1/#grid-item-sizing) précise que ce comportement est différent pour les éléments de grille avec un `intrinsic aspect ratio`.

Ne laissez pas les grands mots vous effrayer. Ce n'est pas un démogorgon.

Une image est par défaut un élément `inline-block`, mais elles ont aussi des dimensions spécifiques. Elles ont des dimensions naturellement associées à elles. Une image pourrait être de `400px` par `600px` de large, ou toute autre dimension donnée.

Mais, les éléments de bloc réguliers tels que les `divs`, n'ont pas de dimensions intrinsèques. C'est-à-dire, ils n'ont pas de dimensions qui leur appartiennent naturellement.

Donc, tandis que les éléments de grille sans dimensions intrinsèques s'étireront pour s'adapter à leur zone de grille, ce n'est pas vrai pour les éléments de grille ayant une dimension intrinsèque, par exemple les images.

### 5. Savez-vous vraiment ce qu'est un élément de grille ?

Considérez le bloc de code ci-dessous :

```html
<div style="display: grid">
    <div>block</div>

    <div>float</div>
   
    Je suis un texte aléatoire 

    <span>
        élément 4
    </span>
</div>
```

Dans le bloc de code ci-dessus, pouvez-vous repérer les éléments de grille ?

Combien d'éléments de grille y a-t-il dans le bloc de code, 3 ou 4 ?

J'ai échoué à cette question de manière flagrante.

Notez que le texte `Je suis un texte aléatoire` n'est pas enveloppé par des balises `html`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Y-ugQCjXh2JQTK9nnZm3ag.png)
_lequel est-ce ?_

Alors, quelle est votre réponse ?

Eh bien, si vous avez répondu 3, vous avez tort. Haha, je vous ai eu !

Selon la spécification, **un élément de grille anonyme** est enveloppé autour de chaque texte dans une grille.

Oui, cela signifie que `Je suis un texte aléatoire` est aussi un élément de grille.

```html
<div style="display: grid">
    
<div>block</div>

    <div>float</div>
    <!-- le texte ci-dessous est un élément de grille -->
    Je suis un texte aléatoire 

    <span>
        élément 4
    </span>
</div>
```

Oui, la réponse est 4. Nous avons 3 éléments de grille explicites et 1 élément de grille anonyme !

Vous avez compris ?

### 6. Les marges des éléments de grille adjacents ne s'effondrent pas.

Il y a de grandes différences entre les éléments de bloc et les conteneurs de grille.

Ce que je veux dire, c'est qu'un élément avec `display: block` et un autre avec `display: grid` ont beaucoup de différences fondamentales.

La différence dont je choisis de parler ici concerne les marges qui s'effondrent.

L'une des premières choses que vous apprenez avec CSS est le concept des marges qui s'effondrent. Je ne veux pas passer beaucoup de temps à expliquer ce que signifient les marges qui s'effondrent. Si vous le mentionnez dans les commentaires, je le ferai.

Donc, revenons aux grilles.

Avec chaque élément de grille, les marges ne s'effondrent jamais.

Eh bien, cela est compréhensible. Laissez-moi vous montrer pourquoi.

Les éléments de grille adjacents sont indépendamment contenus dans le bloc conteneur formé par leurs zones de grille.

Ce que ce paragraphe complexe ci-dessus signifie est ceci. Chaque élément de grille vit et respire dans une `grid-area`

![Image](https://cdn-media-1.freecodecamp.org/images/1*mJYB7D_bzUJOHueTKZM0IQ.png)
_Les éléments de grille sont placés dans leurs zones de grille respectives. Ils restent dans leurs propres territoires non perturbés. Ils ne sont pas affectés par les marges qui s'effondrent. C'est cool._

Donc, techniquement, vous pourriez dire que l'élément de grille n'est pas un voisin immédiat des autres éléments de grille. Mais est contenu dans un territoire fermé et ininterrompu — la zone de grille.

Si vous êtes curieux de savoir quelles autres différences existent entre les éléments de bloc et les éléments de grille, j'ai écrit un article intéressant [article](https://medium.com/flexbox-and-grids/css-grid-layout-3-vital-differences-between-grid-containers-block-containers-6f3c39cf3bba) sur le sujet.

### 7. `auto-fill` et `auto-fit. Quelle est la différence ?`

Bien que `auto-fill` et `auto-fit` semblent être les mêmes fonctions, elles sont différentes à certains égards.

Elles sont similaires dans le sens où elles permettent de créer automatiquement des pistes de grille qui remplissent le conteneur de grille de quelque manière.

Par exemple, le code suivant créera autant de colonnes de `200px` que possible pour s'adapter à la largeur de la fenêtre. Si il reste de l'espace, il sera distribué parmi les colonnes de `200px`.

```css
body {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
}
```

Quelle est la différence ?

`auto-fill` créera des pistes même s'il n'y a pas d'élément de grille pour les remplir. `auto-fit` ne le fera pas. Il réduira les pistes vides à zéro.

C'est tout.

### 8. Dans la définition de grid-template-areas, le nombre de mots dans une chaîne DOIT être égal.

Vous vous souvenez des valeurs de `grid-template-areas` qui ressemblent à une carte ?

Eh bien, il semble que cela puisse tout gâcher très rapidement.

Dans une déclaration `grid-template-areas`, toutes les chaînes doivent avoir le même nombre de colonnes, sinon la déclaration est invalide.

Par exemple :

```css
/* ceci est valide */

grid-template-areas: "header header header sidebar"
                     "main   main   main   sidebar"
                     "main   main   main   sidebar"

/* ceci est FAUX */

grid-template-areas: "header header header sidebar"
                     "main   main   main   sidebar"
                     "main   main     sidebar"
```

Le nombre de mots dans les chaînes doit être égal.

### 9. Évitez d'utiliser des pourcentages dans les paddings ou les marges sur les éléments de grille

![Image](https://cdn-media-1.freecodecamp.org/images/1*KsdfpVZap5kke83AI042CA.png)
_[De la spécification CSS Grid](https://www.w3.org/TR/css-grid-1/#item-margins" rel="noopener" target="_blank" title=")_

La raison derrière cela est simple. Au moment de la rédaction de cet article, vous obtiendrez des comportements différents dans différents navigateurs.

Selon la spécification, le pourcentage peut être résolu soit par rapport à la `width` de l'élément seul, soit par rapport à la `width` pour les marges `left`/`right` tandis que `top`/`bottom` sont résolus par rapport à la `height`

Afin d'avoir un rendu cohérent dans la plupart des navigateurs, évitez d'utiliser des pourcentages dans les paddings ou les marges des éléments de grille.

Plus important encore, il y a déjà quelques parties confuses avec CSS Grid. Ne vous tirez pas une balle dans le pied avec des paddings ou des marges en pourcentage dans les éléments de grille.

### 10. Comment la taille de la grille explicite est-elle résolue lorsqu'il y a un conflit ?

Supposons que vous ayez une déclaration de grille comme ceci :

```css
grid-template-areas: "header header header sidebar"
                     "main   main   main   sidebar"
                     "main   main   main   sidebar"
```

Dans le bloc de code ci-dessus, vous avez 4 colonnes et 3 lignes.

Et si vous faisiez aussi ceci :

```css
grid-template-columns: repeat(5, 1fr) 
grid-template-rows: repeat(4, 1fr)
```

Maintenant vous avez plus de colonnes et de lignes. 5 colonnes, et 4 lignes.

Vous avez compris ?

Il y a maintenant un conflit dans les déclarations. Alors, comment cela est-il résolu ?

Selon la spécification, la taille de la grille explicite est déterminée par le plus grand nombre de `rows/columns` défini par `grid-template-areas` et le nombre de `rows/columns` dimensionné par `grid-template-rows/grid-template-columns`.

La spécification peut sembler compliquer une chose simple. En langage clair, cela signifie que la déclaration avec le plus grand nombre de `rows` ou `columns` gagne.

Dans l'exemple ci-dessus, la grille prendra 5 colonnes, et 4 lignes et non 4 colonnes et 3 lignes.

***ÉDIT :** La propriété `grid-template-areas` est utilisée pour placer les éléments de grille sur une grille. Alors, pourquoi devrions-nous avoir un conflit dans la définition de la grille ? Les grilles ne sont-elles pas censées être définies avec juste les propriétés `grid-template-columns` et `grid-template-rows` ? Je réponds à cette question dans la section des commentaires. Allez voir.

### 11. La taille de la grille n'est pas purement la somme des tailles des pistes

![Image](https://cdn-media-1.freecodecamp.org/images/1*0NJt-xbXYw1C5SQHCS1SUg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*Axq_JnjdpJp2RUg6z5iaIw.png)
_Les pistes de grille font référence à la distance entre les lignes de grille._

Bien que cela soit simple, cela vaut la peine d'être mentionné au cas où vous auriez une grille de largeur fixe.

La taille de la grille peut être influencée par le [grid-row-gap](https://www.w3.org/TR/css-grid-1/#propdef-grid-row-gap), [grid-column-gap](https://www.w3.org/TR/css-grid-1/#propdef-grid-column-gap) et [justify-content](https://www.w3.org/TR/css3-align/#propdef-justify-content), [align-content](https://www.w3.org/TR/css3-align/#propdef-align-content). Ce qui, malheureusement, peut ajouter un espace supplémentaire entre les pistes.

Donc, soyez prudent lors du calcul des largeurs fixes dans la grille.

### BONUS : Nous pouvons tous contribuer à améliorer la DOCUMENTATION

Parce que je suis une âme charitable, j'ai ajouté un autre conseil ici ?

La spécification a été écrite par des humains. Et il se trouve que les humains peuvent faire des erreurs.

En lisant la spécification, j'ai repéré une petite faute de frappe.

%[https://twitter.com/OhansEmmanuel/status/885370706938277889?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E885370706938277889&ref_url=https%3A%2F%2Fmedium.com%2Fmedia%2Fac1d37edf183b9e848a0aaf5c656a070%3FpostId%3Dfb3983aa5e0]

À l'époque, je n'étais pas particulièrement sûr de ce qu'il fallait faire. Alors, j'ai demandé autour de moi sur Twitter.

La gentille [Jen Simmons](https://www.freecodecamp.org/news/11-things-i-learned-reading-the-css-grid-specification-fb3983aa5e0/undefined) a aidé à signaler un problème sur github, et il a été résolu.

Alors, quelle est la morale ?

Vous pouvez aider à améliorer les documents en contribuant de quelque manière que ce soit.

Oui, vous !

Faisons du web un meilleur endroit, ensemble.

### Vous voulez devenir Pro ?

Téléchargez mon guide gratuit sur CSS Grid, et obtenez également deux cours interactifs de qualité sur Flexbox gratuitement !

![Image](https://cdn-media-1.freecodecamp.org/images/1*u2ew8JU87UuAmSYWY1y8Vg.png)
_Comment maîtriser le CSS Grid, et quoi construire en cours de route (Guide PDF gratuit)_

[Obtenez-les maintenant](http://eepurl.com/dcNiP1) ?