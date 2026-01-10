---
title: Tutoriel complet sur CSS Grid avec aide-mémoire 🎖️
subtitle: ''
author: Joy Shaheb
co_authors: []
series: null
date: '2021-06-08T16:02:45.000Z'
originalURL: https://freecodecamp.org/news/css-grid-tutorial-with-cheatsheet
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/FCC.png
tags:
- name: CSS
  slug: css
- name: CSS Grid
  slug: css-grid
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Tutoriel complet sur CSS Grid avec aide-mémoire 🎖️
seo_desc: 'Today we''re going to learn CSS Grid properties so that you can make your
  own responsive websites. I''ll explain how each of Grid''s properties work along
  with a CheatSheet that covers everything you can do with Grid. Let''s go. 🎖️

  Table of Contents:


  C...'
---

Aujourd'hui, nous allons apprendre les propriétés **CSS Grid** afin que vous puissiez créer vos propres sites web responsives. Je vais expliquer comment chaque propriété de Grid fonctionne, accompagné d'une aide-mémoire qui couvre tout ce que vous pouvez faire avec Grid. C'est parti. 🎖️

# Table des matières :

* [Architecture CSS Grid](#heading-architecture-css-grid)
* [Tableau CSS Grid](#heading-tableau-css-grid)
* [Propriétés parent de Grid](#heading-proprietes-parent-css-grid)
   * [grid-template-columns](#heading-la-propriete-grid-template-columns)
   * [grid-template-rows](#heading-la-propriete-grid-template-rows)
   * [grid-template-areas](#heading-la-propriete-grid-template-areas-1)
   * [Comment créer des écarts entre colonnes et lignes dans Grid](#heading-la-propriete-column-gap)
   * [Comment justifier les éléments et aligner les éléments avec Grid](#heading-la-propriete-justify-items)
   * [Comment justifier le contenu et aligner le contenu avec Grid](#heading-la-propriete-justify-content)
* [Propriétés enfant dans CSS Grid](#heading-proprietes-enfant-css-grid)
   * [grid-column : start/end](#heading-les-proprietes-grid-column-startend)
   * [grid-row : start/end](#heading-les-proprietes-grid-row-startend)
   * [grid-area](#heading-la-propriete-grid-area)
   * [justify-self || align-self](#heading-la-propriete-justify-self)
* [Raccourcis pour Grid](#heading-raccourcis-pour-les-proprietes-css-grid)
* [Conclusion](#heading-conclusion)

## Vous pouvez également regarder ce tutoriel sur YouTube si vous le souhaitez :

%[https://youtu.be/VXW1r09Y6Tw]

# D'abord, qu'est-ce que CSS Grid ?

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/6e3wc9k9qxw07o54e38x.png)

Grid est un plan pour créer des sites web.

Le modèle Grid vous permet de disposer le contenu de votre site web. Non seulement cela, il vous aide à créer les structures dont vous avez besoin pour construire des sites web responsives pour plusieurs appareils. Cela signifie que votre site aura une belle apparence sur ordinateur, mobile et tablette.

Voici une simple démonstration que j'ai créée en utilisant Grid comme plan principal.

### Vue Ordinateur

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/zuz7de20oxw7t8kmid4s.png)

### Vue Mobile

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/8wqtabiihl0kexxdbvht.png)

# Architecture CSS Grid

Alors, comment fonctionne l'architecture Grid ? Les éléments Grid [Contenus] sont distribués le long de l'axe principal et de l'axe transversal. En utilisant diverses propriétés Grid, vous pouvez manipuler les éléments pour créer vos mises en page de site web.

![Architecture Grid](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/h9qs07pm0a8s20scr6wr.png)
_architecture grid_

Au fait, vous pouvez joindre plusieurs lignes et colonnes, comme dans le logiciel Excel, ce qui vous donne plus de flexibilité et d'options que Flexbox.

Au fait, voici une aide-mémoire que j'ai faite pour [Flexbox](https://www.freecodecamp.org/news/css-flexbox-tutorial-with-cheatsheet/) si vous voulez en savoir plus à ce sujet.

# Tableau CSS Grid 

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/s3oecuzn41ee3gj4o1ny.png)

Ce tableau contient toutes les propriétés possibles que vous pouvez utiliser lorsque vous utilisez grid. Les propriétés Grid sont divisées en :

* Propriétés parent
* Propriétés enfant

**Note :** Le texte en rouge désigne les propriétés raccourcies :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/n93mkan7du7wz3zyibtw.png)

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/5g3msf9v3yw9qjpzkvj7.png)

À la fin de ce tutoriel, vous aurez une compréhension claire de la façon d'utiliser toutes ces propriétés.

# Comment configurer le projet

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/8c9bfd2puec1wjuk063k.png)

Pour ce projet, vous devez connaître un peu de HTML, CSS, et comment travailler avec VS code. Suivez-moi pendant que nous complétons les tâches suivantes :

1. Créez un dossier nommé "Project-1" et ouvrez VS Code
2. Créez les fichiers index.html et style.css
3. Installez Live Server et exécutez-le.

Ou, vous pouvez simplement ouvrir [Codepen](https://codepen.io) et commencer à coder.

À la fin de ce tutoriel, vous serez en mesure de créer des mises en page de sites web précises et belles.

Et... nous sommes prêts ! Commençons à coder. 😊

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/gfjntw9islnyhv6mkigq.png)

## HTML

Créez trois boîtes à l'intérieur de la balise body, comme ceci 👍

```html
<div class="container">
  <div class="box-1"> A </div>
  <div class="box-2"> B </div>
  <div class="box-3"> C </div>
</div>

```

## CSS

### Étape 1

Nettoyons nos styles par défaut du navigateur. Suivez-moi 👍

```css
*{
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
}

```

### Étape 2

À l'intérieur du sélecteur body, faites ces ajustements :

```css
body {
  font-family: sans-serif;
  font-size: 40px;
  width: 100%;
  min-height: 100vh;
}

```

### Étape 3

Maintenant, stylisons nos boîtes en les sélectionnant toutes ensemble ->

```css
[class^="box-"] {
  background-color: skyblue;

/* Pour placer la lettre au centre */
  display: grid;
  place-items: center;
}

```

**Note :** Ne vous inquiétez pas, nous discuterons de ces propriétés grid en détail plus tard.

### Étape 4

Maintenant, placez quelques écarts entre nos boîtes comme ceci 👍

```css
.container {
  display: grid;
  gap: 20px;
}

```

## Mais attendez....

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/cq8exwor5aiciu2j6jwu.png)

Avant de commencer, vous devez comprendre la relation entre les classes parent et enfant.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/wzq3w0bys78fveqb9z0z.png)

Pour la propriété parent Grid, nous écrirons à l'intérieur de la classe `.container`. Pour la propriété enfant Grid, nous écrirons dans les classes `.box-*`.

# Propriétés parent de CSS Grid

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/lwnmeomlyekzuov7tcml.png)

Tout d'abord, apprenons les propriétés parent de CSS Grid !

## La propriété grid-template-columns

Vous utilisez cette propriété pour définir le **nombre et la largeur** des colonnes. Vous pouvez soit définir individuellement la largeur de chaque colonne, soit définir une largeur uniforme pour toutes les colonnes en utilisant la fonction `repeat()`.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/pu3jedhac2u0onuan6go.png)

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/mov0pc7djie6gbj7m25g.png)
_grid-template-columns_

Pour recréer ces résultats, écrivez les lignes CSS suivantes ->

```css
.container {
  display: grid;
  gap: 20px;

/*  Changez les valeurs     👍 pour expérimenter */
  grid-template-columns: 200px auto 100px;
}

```

**Note :**

* Les valeurs en pixels seront une mesure exacte. Le mot-clé "auto" couvrira l'espace disponible.
* Si vous utilisez fr (unité de fraction) comme unité de mesure, toutes les boîtes seront de taille égale.

## La propriété grid-template-rows

Vous utilisez cette propriété pour définir le **nombre et la hauteur** des lignes. Vous pouvez soit définir individuellement la hauteur de chaque ligne, soit définir une hauteur uniforme pour toutes les lignes en utilisant la fonction `repeat()`.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/r78wfrp3rr4mmn3507ym.png)

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/elpj9jw29ydlwao1yb3q.png)
_grid-template-rows_

Pour tester ces résultats, écrivez le code CSS suivant ->

```css
.container {
  display: grid;
  gap: 20px;
  height: 100vh;

/* Changez les valeurs  👍 pour expérimenter */
  grid-template-rows: 200px auto 100px;
}

```

## La propriété grid-template-areas

Vous utilisez cette propriété pour spécifier la quantité d'espace qu'une cellule de grille doit occuper en termes de colonnes et de lignes à travers le conteneur parent. La vie est beaucoup plus facile avec cette propriété car elle nous permet de voir visuellement ce que nous faisons.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/9nw9e0e1wk96wg3uq99f.png)
_Mise en page standard 12X12_

Appelons cela le plan (template) de notre mise en page 👍

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/nffhbw0eho476i535eyu.png)
_Le plan_

Pour expérimenter avec cela, vous devez comprendre à la fois les propriétés parent et enfant :

* **grid-template-areas :** La propriété parent qui créera le plan
* **grid-area :** la propriété enfant qui suivra le plan.

### D'abord, créez le plan

Comme ceci 👍 à l'intérieur de la classe parent .container :

```css
.container {
  display: grid;
  gap: 20px;
  height: 100vh;

  grid-template-areas: 
    "A A A A   A A A A   A A A A"
    "B B B B   B B B B   B B C C"
    "B B B B   B B B B   B B C C";
}

```

### Implémentez le plan

Ciblez toutes nos classes enfant `.box-*` et définissez les valeurs comme ceci ->

```css
.box-1{
  grid-area: A;
}
.box-2{
  grid-area: B;
}
.box-3{
  grid-area: C;
}

```

**Note :** Je discuterai à nouveau de la propriété grid-area dans la section des propriétés enfant de grid.

## La propriété column-gap

Vous utilisez cette propriété pour placer un écart entre les **colonnes** à l'intérieur de la grille 👍

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/fa59gtskckoh7ms1uk1h.png)
_column-gap_

Pour tester cela, écrivez ce qui suit en CSS 👍

```css
.container {
  display: grid;
  height: 100vh;

  grid-template-columns: 100px 100px 100px;
//Changez les valeurs 👍 pour expérimenter
  column-gap:  50px;
}

```

**Note :** column-gap fonctionne avec grid-template-columns.

## La propriété row-gap

Vous utilisez cette propriété pour placer un écart entre les **lignes** à l'intérieur de la grille 👍

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/aw6l38lydlag1dtzw9j8.png)
_row gap_

Testons cela 👍

```css
.container {
  display: grid;
  height: 100vh;

  grid-template-rows: 100px 100px 100px;
// Changez   👍  les valeurs pour expérimenter
  row-gap:  50px;
}

```

**Note :** row-gap fonctionne avec grid-template-rows.

## La propriété justify-items

Vous utilisez cette propriété pour positionner les éléments de grille (enfants) à l'intérieur des conteneurs de grille le long de l'**axe X [axe principal]**. Les **4** valeurs sont 👍

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/oka32lvb2i0lrhcb8p4e.png)

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/4r2jv92rgp3514fsp4ft.png)
_justify-items_

Si vous voulez tester cela, ajoutez 1 boîte supplémentaire à l'intérieur du HTML ->

```html
<div class="container">

  <!--Autres boîtes - A, B, C sont ici-->

  <div class="box-4"> D </div>
</div>

```

et dans le CSS ->

```css
.container {
  display: grid;
  gap: 50px;
  height: 100vh;

// chaque boîte fait 200px par 200px
  grid-template-rows: 200px 200px;
  grid-template-columns: 200px 200px;

//  Changez les valeurs 👍  pour expérimenter
  justify-items : end;
}

```

## La propriété align-items

Vous utilisez cette propriété pour positionner les éléments de grille (enfants) à l'intérieur du conteneur de grille le long de l'**axe Y [axe transversal]**. Les **4** valeurs sont 👍

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/abl60fsmjuys1kadh1ig.png)
_align-items_

Ne changez rien dans le HTML, mais dans le CSS écrivez ->

```css
.container {
  display: grid;
  gap: 50px;
  height: 100vh;

// chaque boîte fait 200px par 200px
  grid-template-rows: 200px 200px;
  grid-template-columns: 200px 200px;

//  Changez les valeurs 👍  pour expérimenter
  align-items: center;
}

```

## La propriété justify-content

Vous utilisez cette propriété pour positionner votre grille [Basiquement tout] à l'intérieur du conteneur de grille le long de l'**axe X [axe principal]**. Les **7** valeurs sont 👍

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/r9a8eovy1t3i8x5yii4i.png)

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/onq2gubifwog2rccclqe.png)
_justify-content_

Ne changez rien dans le HTML, mais dans le CSS écrivez ->

```css
.container {
  display: grid;
  gap: 50px;
  height: 100vh;

// chaque boîte fait 200px par 200px
  grid-template-rows: 200px 200px;
  grid-template-columns: 200px 200px;

//  Changez  les valeurs  👍  pour expérimenter
  justify-content: center;
}

```

## La propriété align-content

Vous utilisez cette propriété pour positionner notre grille [Basiquement tout] à l'intérieur du conteneur de grille le long de l'**axe Y [axe transversal]**. Les **7** valeurs sont 👍

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/kfgzxrhe2ca4mzk1ies1.png)

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/c1rjvr4bvwsc8ceevq96.png)
_align-content_

Ne changez rien dans le HTML, mais dans le CSS écrivez ->

```css
.container {
  display: grid;
  gap: 50px;
  height: 100vh;

// chaque boîte fait 200px par 200px
  grid-template-rows: 200px 200px;
  grid-template-columns: 200px 200px;

//  Changez  les valeurs 👍 pour expérimenter
  align-content : center;
}

```

# Faites une pause

Jusqu'à présent, tout va bien ! Faites une pause, vous la méritez.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/xanzksehasqcwc8qm8fw.png)

# Propriétés enfant de CSS Grid

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/k2k1muu9oldsp02aigvx.png)

Maintenant, examinons les propriétés enfant de Grid.

# L'échelle CSS Grid

J'ai créé cette échelle de grille pour démontrer les calculs de la façon dont les lignes et les colonnes sont jointes ensemble. Nous pouvons utiliser l'un des 2 types de mesure :

* Le chiffre [1,2,3,4, etc...]
* Le mot-clé span

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ie4paaplgo8rwf4fd41o.png)
_L'échelle de la grille_

Vous aurez une image claire de la façon dont ce guide fonctionne ✱ lorsque nous écrirons du code dans un court instant.

L'illustration ci-dessous 👍 montre les points de départ et de fin des lignes et des colonnes d'une seule cellule.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/bumrjjy06owkahoe49y3.png)
_Colonne et ligne de la grille -> points de départ et de fin_

### HTML

Pour expérimenter avec l'échelle de la grille et comprendre les propriétés suivantes, créez 4 boîtes à l'intérieur de la balise body :

```html
<div class="container">
  <div class="box-1"> A </div>
  <div class="box-2"> B </div>
  <div class="box-3"> C </div>
  <div class="box-4"> D </div>
</div>

```

Nous allons utiliser la fonction `repeat()`. Elle répète notre code un certain nombre de fois. Voici un exemple 👍

```css
grid-template-columns : repeat(5,1fr);

```

Ceci ✱ est l'équivalent d'écrire ceci : 👍

```css
grid-template-columns : 1fr 1fr 1fr 1fr 1fr ;

```

#### Une note rapide

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/i2q151726koc8h8mp0ht.png)

Lorsque nous utilisons l'unité fr [ Fraction ], nous divisons la zone de l'écran en proportions égales.

```css
  grid-template-columns: repeat(5, 1fr);

```

Ce ✱ code divise notre largeur d'écran en 5 parties égales.

Nous sommes prêts, commençons !

## Les propriétés grid-column : start/end

Vous utilisez ces deux propriétés pour joindre plusieurs **COLONNES** ensemble. C'est un raccourci de 2 propriétés :

* **grid-column-start**
* **grid-column-end**

Écrivez ce code dans votre CSS :

```css
.container {
  display: grid;
  gap: 20px;
  height: 100vh;

  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: repeat(12, 1fr);
}

```

Le résultat ressemble à ceci :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/t2pt6zzl39mvjkv6h1m2.png)

Ici, nous divisons notre écran [à la fois la largeur et la hauteur] en 12 parties égales. 1 boîte occupe 1 partie, ou vous pouvez l'appeler 1fr [1 fraction]. Les 8 fractions restantes le long de la largeur sont vides.

Comme nous traitons des propriétés enfant, nous devons cibler nos classes `.box-*` comme ceci :

```css
.box-1{}
.box-2{}
.box-3{}
.box-4{}

```

Vous pouvez expérimenter avec l'une ou toutes ces boîtes, je vais rester avec `.box-1`.

Apportons notre échelle de grille. Nous traitons avec les colonnes – concentrez-vous simplement sur les colonnes, pas sur les lignes.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ie4paaplgo8rwf4fd41o.png)
_L'échelle de la grille_

L'échelle par défaut de chaque classe `.box-*` est :

```css
grid-column-start : 1;
grid-column-end : 2;

/* Le raccourci -> */
 grid-column : 1 / 2

```

Nous pouvons écrire ceci ✱ en unité span également, comme ceci 👍

```css
grid-column : span 1;

```

Attribuons les 8 fractions vides à `.box-1` comme ceci 👍

```css
.box-1{
grid-column : 1/10
}

```

Le résultat ressemble à ceci : 👍

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/zgcg4yyxourlpk1b6z3m.png)

### Une note rapide 

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/g10ckpo6g3tpn8e9kkpw.png)

Comment ai-je fait le calcul ? La `box-1` occupe elle-même 1 boîte. Et par-dessus cela, nous ajoutons 8 boîtes supplémentaires. À la fin, vous devez ajouter 1 pour indiquer la fin, donc 8+1+1 = 10.

### Comment utiliser le mot-clé span

Si vous êtes confus avec la première propriété, vous pouvez utiliser le mot-clé `span` car il est plus facile à comprendre.

Nous devons ajouter 8 boîtes à `.box-1` qui occupe déjà une boîte. Donc, nous devons faire 8+1 = 9.

```css
.box-1{
  grid-column : span 9;
}

```

Cela va produire le même résultat.

## Les propriétés grid-row : start/end

Vous utilisez ces deux propriétés pour joindre plusieurs **LIGNES** ensemble. C'est un raccourci de 2 propriétés :

* **grid-row-start**
* **grid-row-end**

Expérimentons avec ! Ici, je vais rester avec .box-1, et voici notre guide de grille. Maintenant, concentrez-vous uniquement sur l'échelle des lignes, pas sur les colonnes.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ie4paaplgo8rwf4fd41o.png)
_L'échelle de la grille_

Joignons 9 boîtes à `.box-1` le long de la ligne.

Écrivez ce code : 👍

```css
.box-1{
  grid-row : 1/11;
}

```

Le calcul ressemble à ceci -> `.box-1` contient 1 boîte, et vous ajoutez 9 boîtes supplémentaires, plus un 1 obligatoire à la dernière position pour indiquer la fin, ce qui vous donne 9+1+1=11.

Voici l'alternative 👍 en utilisant le mot-clé span :

```css
.box-1{
  grid-row : span 10;
}

```

Et voici ce calcul -> `.box-`1 contient 1 boîte, et vous ajoutez 9 boîtes supplémentaires 
9+1=10.

Voici le résultat jusqu'à présent : 👍

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/aqkoglmoh1whcyve7uad.png)

## La propriété grid-area

Tout d'abord, nous devons configurer [grid-template-areas](#heading-la-propriete-grid-template-areas-1) ✱ Une fois que nous avons fait cela, nous devons spécifier les noms utilisés dans la classe parent à l'intérieur des classes enfants, comme ceci : 👍

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/hcoalgwdeiogd3tmazzf.png)
_Mise en page standard 12X12_

Ensuite, nous devons spécifier grid-template-areas à l'intérieur du conteneur parent : 👍

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/3r84bvxt5230jyr5pydt.png)

Comme ceci 👍 à l'intérieur de la classe parent :

```css
.container {
  display: grid;
  gap: 20px;
  height: 100vh;

  grid-template-areas: 
    "A A A A   A A A A   A A A A"
    "B B B B   B B B B   B B C C"
    "B B B B   B B B B   B B C C";
}

```

Ensuite, nous spécifions les noms utilisés dans le conteneur parent à l'intérieur des classes enfants avec grid-areas 👍

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ffwg22949ogu0m2bw3sn.png)

Comme ceci 👍 à l'intérieur des classes enfants :

```css
.box-1{
  grid-area: A;
}
.box-2{
  grid-area: B;
}
.box-3{
  grid-area: C;
}

```

## La propriété justify-self

Vous utilisez cette propriété pour positionner **1 individu** grid-item (enfant) à l'intérieur d'un conteneur de grille le long de l'**axe X [axe principal]**. Les **4** valeurs sont 👍

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/g21475dm64kw2vyqgxvd.png)
_Justify-self_

Écrivez ce code pour expérimenter avec les valeurs 👍

```css
.container {
  display: grid;
  gap :25px;
  height: 100vh;

/* // chaque boîte a une taille égale */
  grid-template-rows: 1fr 1fr;
  grid-template-columns: 1fr 1fr;
}

```

**Souvenez-vous !** Cela ne fonctionne que sur les classes enfants. Donc, ciblez n'importe quelle classe `.box-*`. Je vais cibler la première boîte :

```css
.box-1 {
/*  Changez les valeurs 👍  pour expérimenter */
  justify-self : start;  
}

```

## La propriété align-self

Vous utilisez cette propriété pour positionner **1 individu** grid-item (enfant) à l'intérieur d'un conteneur de grille le long de l'**axe Y [axe transversal]**. Les **4** valeurs sont 👍

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/qr5dlqehevjclxys3bx6.png)
_align-self_

Expérimentons avec les valeurs 👍

```css
.container {
  display: grid;
  gap :25px;
  height: 100vh;

/* // chaque boîte a une taille égale */
  grid-template-rows: 1fr 1fr;
  grid-template-columns: 1fr 1fr;
}

```

**Souvenez-vous !** Cela ne fonctionne que sur les classes enfants. Donc, ciblez n'importe quelle classe `.box-*`. Je vais cibler la 1ère boîte :

```css
.box-1 {
/*  Changez les valeurs 👍  pour expérimenter */
  align-self : start;  
}

```

# Raccourcis pour les propriétés CSS Grid

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/f6s9qvnvjtwbj7r1ash6.png)

Examinons ces propriétés raccourcies de Grid :

* `place-content`
* `place-items`
* `place-self`
* `grid-template`
* `gap` / `grid-gap`

## place-content 

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/jz1dydjbbgxw8bxt86i4.png)
_place-content_

Ceci est le raccourci de 2 propriétés :

* align-content
* justify-content

#### Un exemple

```css
align-content : center;
justify-content : end;

/* Le raccourci */
place-content : center / end ;


```

## place-items

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/fvu44ujney5ixzvzedbb.png)
_place-items_

Ceci est le raccourci de 2 propriétés :

* align-items
* justify-items

#### Un exemple

```css
align-items : end;
justify-items : center;

/* Le raccourci */
place-items : end / center ;

```

## place-self

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/jafsak8hqgfb78hbxs0b.png)
_place-self_

Ceci est le raccourci de 2 propriétés :

* align-self
* justify-self

#### Un exemple

```css
align-self : start ;
justify-self : end ;

/* Le raccourci */
place-self : start / end ;

```

## grid-template 

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/dlratlmwgt0vvknnt82w.png)
_grid-template_

Ceci est le raccourci de 2 propriétés :

* grid-template-rows
* grid-template-columns

#### Un exemple

```css
grid-template-rows : 100px 100px;
grid-template-columns : 200px 200px;

/* Le raccourci */
grid-template : 100px 100px / 200px 200px;

```

## gap/grid-gap 

Gap et grid-gap sont la même chose et font le même travail. Vous pouvez utiliser l'un ou l'autre.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/brubmtmvt2jvq1l9f1ep.png)
_gap_

Ceci est le raccourci de 2 propriétés :

* row-gap
* column-gap

#### Un exemple

```css
row-gap : 20px ; 
column-gap : 30px ;

/* Le raccourci */
gap : 20px  30px;

```

## Crédits

* [Licornes](https://www.flaticon.com/packs/unicorn-4)
* [Corgis](https://www.freepik.com/free-vector/cute-corgi-drink-milk-tea-boba-cartoon-vector-illustration-animal-drink-concept-isolated-vector-flat-cartoon-style_10336142.htm#position=13), [kat](https://www.freepik.com/free-psd/pet-food-banner-template_13762522.htm#position=1)

# Conclusion

Maintenant, vous pouvez créer en toute confiance des mises en page de sites web responsives en utilisant vos connaissances sur la grille !

Voici votre médaille pour avoir lu jusqu'à la fin ❤️ 

## Suggestions et critiques sont grandement appréciées ❤️

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/usxsz1lstuwry3jlly4d.png)

**YouTube / [Joy Shaheb](https://www.youtube.com/c/JoyShaheb)**

**LinkedIn / [Joy Shaheb](https://www.linkedin.com/in/joyshaheb/)**

**Twitter / [JoyShaheb](https://x.com/JoyShaheb)**

**Instagram / [JoyShaheb](https://www.instagram.com/joyshaheb/)**