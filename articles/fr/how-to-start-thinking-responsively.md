---
title: 'Comment penser de manière responsive : un tutoriel sur le design web responsive'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-03T14:12:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-start-thinking-responsively
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca084740569d1a4ca492b.jpg
tags:
- name: responsive design
  slug: responsive-design
- name: Web Design
  slug: web-design
seo_title: 'Comment penser de manière responsive : un tutoriel sur le design web responsive'
seo_desc: 'By Kevin Powell

  For a long time, responsive web design was a trend. Now it''s simply a reality.
  If we think of a website, we don''t really have to say "a responsive website", it''s
  just an expected reality.

  This means that when we are putting together a...'
---

Par Kevin Powell

Pendant longtemps, le design web responsive était une tendance. Aujourd'hui, c'est simplement une réalité. Lorsque nous pensons à un site web, nous n'avons pas vraiment à dire "un site web responsive", c'est simplement une réalité attendue.

Cela signifie que lorsque nous mettons en place un site web, il doit être construit en gardant à l'esprit comment il apparaîtra sur différentes tailles d'écran. Avec les tendances actuelles, il doit y avoir un fort accent sur l'expérience mobile.

*R\_écemment*, j'ai *lancé un cours complet et détaillé sur*\_ ***Scrimba*** *appelé* [***The Responsive Web Design Bootcamp***](https://scrimba.com/g/gresponsive)***.*** *Ce cours couvre tous les concepts techniques et architecturaux sur le design web responsive en profondeur****.*** *Ce blog est basé sur l'une des* six *sections du cours\_:\_ ***Commencer****à penser de manière responsive****.*

# Se mettre dans l'état d'esprit responsive

Ce module du cours se concentre sur l'importance de penser à la réactivité avant d'écrire une seule ligne de code, ainsi que sur quelques autres essentiels de la construction d'un site web responsive :

1. Comment aborder une mise en page
   
2. Les unités CSS
   
3. Les bases de Flexbox
   
4. Les bases des media queries
   

Bien que nous utilisions quelques exercices simples pour commencer, l'objectif principal de ce module du cours est de construire un site web responsive de 3 pages entièrement. Nous l'utilisons à la fois pour renforcer ce que nous avons déjà appris, ainsi que pour introduire quelques nouvelles choses dans le mélange.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/01.png align="left")

Dans cet article, nous allons explorer les concepts que j'explore dans ce module du cours qui sont listés ci-dessus, d'un plongeon dans `em` vs `rem`, un regard sur les bases de flexbox et des media queries, ainsi que des aperçus de certains des projets que nous construisons dans le cours.

# Les unités CSS

Le premier et le plus fondamental concept dans la construction d'un design web responsive sont les unités que nous utilisons pour définir nombreuses de nos propriétés.

Dans la leçon 2, nous allons apprendre quelles sont certaines des unités CSS disponibles et comment elles diffèrent les unes des autres. Plus important encore, nous apprendrons lesquelles utiliser selon les exigences.

Il existe trois principaux types d'unités CSS disponibles : les unités absolues, les unités en pourcentage et les unités relatives.

## Les unités absolues

Les unités absolues sont également appelées unités fixes.

La longueur exprimée dans l'une des unités absolues apparaîtra dans une taille exactement identique (d'où pourquoi nous les appelons fixes, elles sont de taille fixe).

Bien que les `px` (pixels) soient l'unité la plus courante, en CSS nous pouvons également utiliser `pt`, `pc`, `in`, `cm`, `mm`, et bien d'autres, bien que je ne recommande vraiment pas celles-ci sauf si vous stylisez quelque chose pour l'impression.

Les `px` sont un peu plus compliqués que vous ne le pensez. À l'époque, un `px` était lié à un pixel sur votre écran, mais maintenant CSS utilise quelque chose appelé le *pixel de référence* qui en fait une taille fixe, indépendante de la résolution de l'appareil.

## Les pourcentages

Les leçons 3-5 du cours plongent dans les pourcentages. Le pourcentage, comme son nom l'indique, est souvent utilisé pour définir la taille par rapport à la taille de son parent.

Cela est un peu différent des unités absolues, et prend un peu de temps pour s'y habituer. Lorsque nous définissons la largeur de quelque chose en utilisant `px`, nous disons à cet élément quelle taille il doit avoir. Par exemple :

```css
.box {
    width: 500px;
    /* cet élément aura une largeur de 500px */
}
```

Alors que, si nous utilisons un pourcentage, ce n'est pas aussi simple :

```css
.box {
    width: 80%;
    /* cet élément aura une largeur de 80% */
}
```

Mais, que représente ce `80%` ? C'est celui de son parent. Lorsque nous utilisons un pourcentage pour `width`, `margin`, ou `padding`, il regarde toujours la *largeur de son parent* (oui, même pour `margin` et `padding` en haut et en bas).

Nous utiliserons souvent le pourcentage pour définir les largeurs des éléments, car cela les rend plus flexibles, ce qui est essentiel lors de la mise en place d'un design responsive.

Pendant le cours, nous apprendrons cela à l'aide de l'exemple suivant :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/02.png align="left")

Si nous gardons la largeur du conteneur pour la mise en page ci-dessus à un nombre fixe, disons `500px`, nous savons qu'elle aura l'air correcte tant que la taille de l'écran n'est pas inférieure à `500px`.

Dans ce scénario, si nous voulons que notre mise en page s'ajuste en fonction de la taille de la fenêtre, ce que nous pouvons faire est de définir la largeur en pourcentage qui peut être `100%` ou moins.

```css
.container { 
    width: 70%; 
    ...
}
```

Comme nous avons mis à jour la largeur pour qu'elle soit de 70% de la largeur du conteneur parent, nous pouvons maintenant voir qu'elle s'ajuste à la taille de l'écran :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/03.jpeg align="left")

Il y a cependant un problème. Actuellement, si nous mettons une image dans notre conteneur, elle ressemble à ceci (si l'image a une largeur trop grande) :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/04.png align="left")

Le problème est que, sauf si nous spécifions autrement, les images auront leur taille réelle. Pour corriger cela, nous pourrions appliquer du CSS sur l'image elle-même afin qu'elle commence à s'ajuster par défaut à la taille de son conteneur.

```css
.img { 
    width: 100%;
}
```

Et, comme nous le faisons, nous pouvons voir que l'image commence à s'ajuster par défaut à la taille de son conteneur parent.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/05-1.jpeg align="left")

### Tailles maximales et minimales

Bien que la solution ci-dessus soit excellente, elle peut en fait faire en sorte que l'image devienne plus grande que sa taille réelle. Si cela se produit, elle commencera rapidement à perdre en qualité.

Pour aider à corriger cela, nous pouvons plutôt utiliser `max-width`.

```css
.img { 
    max-width: 100%;
}
```

Cela signifie que la largeur maximale de l'image est de 100% de celle de son parent, mais qu'elle est autorisée à être plus petite.

Dans le cours, j'explore également d'autres propriétés similaires, telles que `min-width`, `min-height` et `max-height`, qui définissent toutes des limites supérieures et inférieures pour la taille d'un élément.

Celles-ci prennent toutes le pas sur la `width` d'un élément, ce qui est toujours important à retenir !

## Les unités CSS - Unités relatives

Les unités relatives en CSS sont toujours relatives à la taille de quelque chose d'autre. Certaines unités regarderont la `font-size` d'un autre élément (ou de cet élément), tandis que d'autres regarderont la taille de la fenêtre.

Dans le cours, je commence par introduire les deux unités qui sont relatives à `font-size`, le **em** et **rem**.

## L'unité `em`

Lorsque vous déclarez la `font-size` d'un élément, si vous utilisez `em`, elle sera relative à la `font-size` du parent.

Par exemple, nous avons le code HTML suivant où nous avons quelques éléments `li` qui ont quelques éléments parents.

```html
<body> 
    <section class='class-one'>
        <div class="container">
            <ul>
                <li>Item 1</li>
                <li>Item 2</li>
                <li>Item 3</li>
            </ul>
        </div>
    </section>
</body>
```

Et, nous avons le CSS suivant avec le HTML ci-dessus :

```css
body { 
    font-size: 25px; ...
}

ul { 
    /* 1.5em = 25 * 1.5 = 37.5  */ 
    font-size: 1.5em;
}
```

Dans le cas ci-dessus, le `ul` prendra sa `font-size` de son parent et l'appliquera à ses éléments `li` en utilisant le `1.5em` relatif.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/06.jpeg align="left")

Dans le cas de l'unité *em*, nous devons nous souvenir qu'elle prendra par défaut la `font-size` de son parent immédiat, ce qui signifie que dans notre exemple ci-dessus, si nous changeons la `font-size` de la classe `container` pour qu'elle soit `15px`, alors le `ul` commencera à s'ajuster par rapport à `15px`.

### Effet de cascade des `em`

L'une des raisons pour lesquelles je n'aime pas définir la `font-size` en `em` est à cause du risque d'être touché par un effet de cascade. Par exemple, si nous utilisons l'exemple ci-dessus, mais que nous ajoutons une `font-size` aux éléments `li`, nous commençons à rencontrer des problèmes !

```css
body { 
    font-size: 25px; ...
}

ul { 
    font-size: 1.5em;
}

li {
 	font-size: 1.5em;   
}
```

Dans ce cas, le `li` regarde son parent, qui regarde ensuite le body, donc nous obtenons une taille de police totale de 56.25px (1.5 x 1.5 x 25px). Les choses peuvent rapidement devenir incontrôlables !

## L'unité `rem`

Comme nous pouvons le voir, l'utilisation de `em` peut être déroutante car elle prend sa taille de son parent qui peut avoir sa `font-size` définie également en `em` et cela créerait un effet de cascade.

L'unité `rem` est l'abréviation de *Root Em*, ce qui signifie qu'elle ne regarde que la `font-size` de l'élément racine. Dans le cas des sites web, l'élément racine est toujours l'élément `html`.

Ainsi, si vous définissez la taille de police de quelque chose en `rem`, elle est *toujours* relative à la `font-size` de l'élément `html` et rien d'autre, ce qui la rend beaucoup plus facile à utiliser.

## Est-il jamais bon d'utiliser les `em` ?

Bien que `em` puisse sembler être quelque chose que vous pourriez vouloir éviter, ils peuvent être vraiment utiles !

Lorsque vous définissez la `font-size` avec `em`, elle regarde l'élément parent, mais lorsque nous définissons une autre propriété en utilisant `em`, elle est relative à **la taille de police de cet élément !** C'est super utile pour définir des choses comme `margin` et `padding`.

Si nous augmentons la `font-size` de notre sélecteur, elle augmentera la `margin` ou le `padding` avec elle, et vice versa ! C'est super utile.

Voici une diapositive du cours qui résume comment j'aime utiliser les deux :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/07.png align="left")

# Flexbox

Une fois que nous avons maîtrisé les unités et ce à quoi elles sont le mieux adaptées, je tourne le cours vers un regard sur les bases de flexbox, qui nous permet de créer des mises en page responsives super facilement sans avoir à dépendre des flottements ou du positionnement.

Tous les éléments, par défaut, ont la propriété `display` de soit `block` soit `inline`.

**Les éléments de bloc** (`div`, `header`, `footer`, `h1` -> `h6`, `p`, etc.) s'empilent les uns sur les autres.

**Les éléments en ligne** (`a`, `strong`, `em`, `span`, etc.) restent dans le flux de ce qui les entoure.

Lorsque nous changeons leur affichage en flex, ils commencent à s'aligner côte à côte.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/08.png align="left")

Voyons comment concevoir une architecture simple d'un site web responsive typique avec quelques colonnes en utilisant flexbox. Le résultat serait la mise en page suivante :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/09.png align="left")

Nous commencerons avec le HTML suivant :

```html
<body>
  <div class="container">
    <h1>This is the header</h1>
    <div class="columns">
      <div class="col">
        <h2>Section 1 - Col 1</h2>
        <p>This is column 1</p>
      </div>
      <div class="col">
        <h2>Section 1 - Col 2</h2>
        <p>This is column 2</p>
      </div>
      <div class="col">
        <h2>Section 1 - Col 3</h2>
        <p>This is column 3</p>
      </div>
    </div>
    <div class="columns">
      <div class="col">
        <h2>Section 2 - Col 1</h2>
        <p>This is column 1</p>
      </div>
      <div class="col">
        <h2>Section 2 - Col 2</h2>
        <p>This is column 2</p>
      </div>
    </div>
  </div>
</body>
```

Et, nous pouvons avoir le CSS suivant :

```css
.container {
  width: 90%;
  max-width: 980px;
  margin: 0 auto;
}

.columns {
  display: flex;
  margin: 1em 0;
}
```

Pour ajouter des couleurs de fond aux colonnes, nous ajouterons quelques classes modificatrices et les assignerons aux colonnes :

```css
.col-bg-beige {
  background-color: beige;
  padding: 1em;
}

.col-bg-aqua {
  background-color: aqua;
  padding: 1em;
}
```

Jusqu'à présent, la page ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/10.png align="left")

À l'étape suivante, nous voulons définir la largeur des colonnes, nous définirons les classes modificatrices et assignerons les largeurs fixes à l'intérieur.

```css
.col-1 {
  width: 25%;
}
.col-2 {
  width: 50%;
}
.col-3 {
  width: 75%;
}
.col-4 {
  width: 100%;
}
```

Nous assignerons ces classes à nos colonnes selon les besoins de la mise en page, comme suit :

%[https://codepen.io/kevinpowell/pen/XWrRqyG] 

Si nous voulons que nos colonnes flex s'alignent les unes avec les autres, nous pouvons utiliser la propriété suivante :

```css
.columns {
  display: flex;
  justify-content: center;
}
```

*Il y a beaucoup plus de détails sur les bases de Flexbox avec des exemples de code et une capacité d'édition de code en ligne dans le cours Scrimba* [***The Responsive Web Design Bootcamp***](https://scrimba.com/g/gresponsive)***.***

# Les Media Queries

Les media queries nous permettent de déclarer de nouvelles règles CSS qui ne s'appliquent que dans des situations spécifiques, telles que différents types de médias (écran, impression, parole), et avec différentes caractéristiques de médias, telles que la largeur de l'écran, l'orientation, le rapport d'aspect et bien plus encore.

La syntaxe de base pour une media query ressemble à ceci :

`@media _media-type_` et (*media-features*) {...}

Par exemple, le morceau de code ci-dessous définira la `background-color` du body s'il s'agit d'un écran et qu'il a une `min-width` de 480px.

```css
@media screen and (min-width: 480px) {  
    body {    
        background-color: aqua;  
    }
}
```

**Revenons à notre exemple précédent**, si nous réduisons la taille de l'écran, nous voyons que certaines des colonnes deviennent beaucoup plus étroites et nous voulons les corriger en les rendant entièrement responsives.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/11.png align="left")

Puisque nous utilisons déjà flexbox, nous pouvons changer la propriété `flex-direction` pour basculer l'axe principal, donc au lieu de créer des colonnes, elle créera des lignes de contenu.

```css
@media screen and (max-width: 600px) {
  .columns {
    flex-direction: column;
  }
}
```

%[https://codepen.io/kevinpowell/pen/WNejJLM] 

# Concevoir une navigation responsive

L'un de mes endroits préférés pour voir comment appliquer tout ce qui précède dans un exemple réaliste est de regarder comment configurer une navigation responsive.

Nous commencerons par écrire le HTML pour la barre de navigation.

```html
<header>
  <div class="container container-nav">
    <div class="site-title">
      <h1>Living the social life</h1>
      <p class="subtitle">A blog exploring minimalism in life</p>
    </div>
    <nav>
      <ul>
        <li><a href="#">Home</a></li>
        <li><a href="#">About me</a></li>
        <li><a href="#">Recent posts</a></li>
      </ul>
    </nav>
  </div>
</header>
```

Ensuite, nous pouvons utiliser flexbox, les media queries, quelques autres petites choses ici et là pour commencer à le styliser dans notre CSS.

Voici un aperçu de certains des CSS (le code détaillé est disponible dans les leçons du cours) :

```css
body {
  margin: 0;
}

.container {
  width: 90%;
  max-width: 900px;
  margin: 0 auto;
}

.container-nav {
  display: flex;
  justify-content: space-between;
}

nav ul {
  display: flex;
  justify-content: center;
  list-style: none;
  margin: 0;
  padding: 0;
}

@media (max-width: 675px) {
  .container-nav {
    flex-direction: column;
  }
    
  header {
    text-align: center;
  }
}
```

Et à la fin des leçons de cette section du module, nous aurons une navigation simple, agréable et entièrement responsive :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/nav-1.gif align="left")

# Construire un site de 3 pages

## Examiner la structure

Avec la navigation terminée, je passe au projet complet. Il s'agira d'un site web mobile responsive de 3 pages.

Ci-dessous, vous pouvez voir les pages que nous construisons, ainsi qu'un lien vers Adobe XD où vous pouvez consulter les planches de travail en plus de détails. Dans les leçons, je regarde les similitudes entre les différentes pages, et comment je commence à planifier quelque chose comme cela avant de commencer à écrire du code.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/13.png align="left")

*Les mises en page des pages web que nous allons apprendre à concevoir dans le cours :* [*https://xd.adobe.com/spec/75d448ea-569a-4b7e-721b-9bbd3b2b97b9-03e5/grid/*](https://xd.adobe.com/spec/75d448ea-569a-4b7e-721b-9bbd3b2b97b9-03e5/grid/)

## La page d'accueil

Comme nous pouvons le voir sur l'image ci-dessous, il y a deux sections principales de la page d'accueil. La liste des articles à gauche avec un article en vedette en haut, et le panneau de droite avec les informations de l'auteur et les articles récents.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/14.png align="left")

Nous allons envelopper tout le contenu dans une div `container` et créer d'abord la section de gauche qui est une liste d'articles. Cela va être créé à l'aide des balises `article` du HTML et ensuite nous mettrons le contenu à l'intérieur.

```html
<div class="container">
  <main role="main">
    <article class="article-featured">
      <h2 class="article-title"></h2> <img src="" alt="" class="article-image">
      <p class="article-info"></p>
      <p class="article-body"></p>
      <a href="#" class="article-read-more"></a>
    </article>
    ...
  </main>
</div>
```

Ensuite, nous allons créer le panneau de droite à l'aide de la balise `aside` du HTML.

```html
<aside class="sidebar">
  <div class="sidebar-widget">
    <h2 class="widget-title"></h2> 
    <img src="#" alt="" class="widget-image">
    <p class="widget-body"></p>
  </div>
    
    ...
</aside>
```

Avant de plonger dans la mise en page elle-même, j'aime toujours commencer par la typographie. Ce n'est peut-être pas la partie la plus excitante de l'écriture de CSS, mais lorsque les polices et les tailles de police commencent à changer, cela peut avoir un impact énorme sur la mise en page. Commencer par là, puis s'inquiéter de la mise en page rend notre vie beaucoup plus facile.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/15.png align="left")

Avec la typographie en place, il est temps de commencer à travailler sur la mise en page elle-même. Bien que nous puissions commencer par les grands écrans et ensuite utiliser une media query pour redessiner les choses à des tailles plus petites (comme nous l'avons fait avec la navigation ci-dessus), je trouve que c'est beaucoup moins de travail de travailler dans l'autre sens.

Les mises en page mobiles tendent à être beaucoup plus simples, donc en commençant par le mobile, nous pouvons créer nos mises en page sans trop de travail.

Une fois la mise en page mobile terminée, il est temps d'ajouter notre media query (ou queries) et de commencer à travailler sur la modification de la mise en page pour les écrans plus grands.

Une chose qui est *vraiment* importante est de ne pas se forcer à avoir des points d'arrêt pour des appareils spécifiques. Il est beaucoup trop courant de voir les mêmes points d'arrêt utilisés tout le temps, mais vraiment, vous devriez apporter des modifications de mise en page lorsque votre mise en page dicte que c'est nécessaire.

Je me fiche vraiment de savoir sur quel appareil se trouve quelqu'un, ou quelle est la taille de cet appareil. Ce qui est important, c'est que cela ait l'air bien sur tous les appareils. Avec le nombre d'appareils et de tailles d'écran différents aujourd'hui, concentrez-vous sur la mise en page elle-même.

Dans le cours lui-même, je plonge dans la façon dont nous pouvons déterminer quand une mise en page a besoin d'un point d'arrêt (souvent parce que les lignes de texte deviennent trop longues !), puis nous plongeons dans quelques extras amusants, en regardant des propriétés telles que `order`, `object-fit` pour aider nos images à s'ajuster beaucoup plus facilement, et en affinant la mise en page.

Les deuxième et troisième pages sont assez faciles à créer une fois la première terminée. En ayant regardé toutes les pages avant de commencer, et en nommant les choses avec des classes qui peuvent être réutilisées sur chaque page, il y a de petits ajustements à faire ici et là, mais globalement les choses avancent très vite.

# Conclusion

Dans cet article, nous avons examiné certains principes fondamentaux de CSS pour concevoir des sites web responsives, de leurs unités aux media queries et flexbox. Nous avons vu comment nous pouvons tout configurer pour une navigation, et comment décomposer et analyser un design plus grand.

Comme je l'ai mentionné au début, tout ce contenu provient du module *Commencer à penser de manière responsive* du cours [**The Responsive Web Design Bootcamp**](https://scrimba.com/g/gresponsive).

Le cours lui-même plonge beaucoup plus profondément dans ces sujets et bien d'autres, d'une exploration des fondamentaux de CSS, ainsi que des plongées profondes dans flexbox et grid, y compris la construction de plusieurs autres projets.

C'est l'ère des sites web *mobile-first*. La bonne nouvelle est que nous pouvons réaliser tout ce dont nous avons besoin en utilisant CSS. Il existe de nombreuses ressources et outils cool disponibles maintenant avec lesquels nous pouvons créer de beaux sites web adaptés aux mobiles sans avoir besoin de frameworks ou de bibliothèques. CSS a atteint un endroit *vraiment* amusant. J'aime vraiment CSS, et j'espère que vous me rejoindrez dans le cours où, espérons-le, je pourrai vous aider à tomber amoureux de lui aussi !