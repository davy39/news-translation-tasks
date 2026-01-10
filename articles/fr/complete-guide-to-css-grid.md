---
title: Manuel CSS Grid – Guide complet des conteneurs et des éléments de grille
subtitle: ''
author: Oluwatobi Sofela
co_authors: []
series: null
date: '2023-03-16T18:19:27.000Z'
originalURL: https://freecodecamp.org/news/complete-guide-to-css-grid
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1738338779416/5e58d695-6840-40da-84bc-c2b2428c16db.png
tags:
- name: CSS Grid
  slug: css-grid
- name: HTML
  slug: html
- name: responsive design
  slug: responsive-design
- name: Web Development
  slug: web-development
seo_title: Manuel CSS Grid – Guide complet des conteneurs et des éléments de grille
seo_desc: 'CSS Grid gives you the tools to create basic and advanced website layouts
  in responsive ways that look great on mobile, tablet, and desktop devices.

  This tutorial discusses everything you need to know to use CSS Grid like a pro.

  Table of Contents


  Wh...'
---

CSS Grid vous donne les outils pour créer des mises en page de sites web basiques et avancées de manière responsive, avec un rendu optimal sur les appareils mobiles, les tablettes et les ordinateurs de bureau.

Ce tutoriel aborde tout ce que vous devez savoir pour utiliser CSS Grid comme un professionnel.

## Table des matières

1. [Qu'est-ce que CSS Grid ?](#heading-quest-ce-que-css-grid)
    
2. [Conteneur de grille vs. Élément de grille : Quelle est la différence ?](#heading-conteneur-de-grille-vs-element-de-grille-quelle-est-la-difference)
    
3. [Qu'est-ce qu'une valeur `grid` en CSS ?](#heading-quest-ce-quune-valeur-grid-en-css)
    
4. [Qu'est-ce qu'une valeur `inline-grid` en CSS ?](#heading-quest-ce-quune-valeur-inline-grid-en-css)
    
5. [Propriétés pour spécifier la mise en page d'une grille](#heading-proprietes-pour-specifier-la-mise-en-page-dune-grille)
    
6. [Quelles sont les propriétés du conteneur de grille ?](#heading-quelles-sont-les-proprietes-du-conteneur-de-grille)
    
7. [Qu'est-ce que la propriété `grid-template-columns` de CSS Grid ?](#heading-quest-ce-que-la-propriete-grid-template-columns-de-css-grid)
    
8. [Qu'est-ce que la propriété `grid-template-rows` de CSS Grid ?](#heading-quest-ce-que-la-propriete-grid-template-rows-de-css-grid)
    
9. [Qu'est-ce que la propriété `justify-content` de CSS Grid ?](#heading-quest-ce-que-la-propriete-justify-content-de-css-grid)
    
10. [Qu'est-ce que la propriété `justify-items` de CSS Grid ?](#heading-quest-ce-que-la-propriete-justify-items-de-css-grid)
    
11. [Qu'est-ce que la propriété `align-content` de CSS Grid ?](#heading-quest-ce-que-la-propriete-align-content-de-css-grid)
    
12. [Qu'est-ce que la propriété `align-items` de CSS Grid ?](#heading-quest-ce-que-la-propriete-align-items-de-css-grid)
    
13. [Quelles sont les propriétés de l'élément de grille ?](#heading-quelles-sont-les-proprietes-de-lelement-de-grille)
    
14. [Qu'est-ce que la propriété `justify-self` de CSS Grid ?](#heading-quest-ce-que-la-propriete-justify-self-de-css-grid)
    
15. [Qu'est-ce que la propriété `align-self` de CSS Grid ?](#heading-quest-ce-que-la-propriete-align-self-de-css-grid)
    
16. [Qu'est-ce que la propriété `grid-column-start` de CSS Grid ?](#heading-quest-ce-que-la-propriete-grid-column-start-de-css-grid)
    
17. [Qu'est-ce que la propriété `grid-column-end` de CSS Grid ?](#heading-quest-ce-que-la-propriete-grid-column-end-de-css-grid)
    
18. [Qu'est-ce que la propriété `grid-column` de CSS Grid ?](#heading-quest-ce-que-la-propriete-grid-column-de-css-grid)
    
19. [Qu'est-ce que la propriété `grid-row-start` de CSS Grid ?](#heading-quest-ce-que-la-propriete-grid-row-start-de-css-grid)
    
20. [Qu'est-ce que la propriété `grid-row-end` de CSS Grid ?](#heading-quest-ce-que-la-propriete-grid-row-end-de-css-grid)
    
21. [Qu'est-ce que la propriété `grid-row` de CSS Grid ?](#heading-quest-ce-que-la-propriete-grid-row-de-css-grid)
    
22. [Qu'est-ce que la propriété `grid-area` de CSS Grid ?](#heading-quest-ce-que-la-propriete-grid-area-de-css-grid)
    
23. [Qu'est-ce que la propriété `grid-template-areas` de CSS Grid ?](#heading-quest-ce-que-la-propriete-grid-template-areas-de-css-grid)
    
24. [Comment utiliser la fonction CSS `minmax()` pour définir des tailles de grille minimales et maximales](#heading-comment-utiliser-la-fonction-css-minmax-pour-definir-des-tailles-de-grille-minimales-et-maximales)
    
25. [Comment utiliser la fonction CSS `repeat()` pour définir des pistes de grille avec des motifs répétés](#heading-comment-utiliser-la-fonction-css-repeat-pour-definir-des-pistes-de-grille-avec-des-motifs-repetes)
    
26. [Aperçu](#heading-apercu)
    

Alors, sans plus attendre, comprenons ce qu'est CSS Grid.

## Qu'est-ce que CSS Grid ?

Le module de mise en page CSS Grid (CSS Grid Layout Module) permet aux navigateurs d'afficher les éléments HTML sélectionnés comme des [modèles de boîte](https://codesweetly.com/css-box-model) de grille.

Grid vous permet de redimensionner et de repositionner facilement un conteneur de grille et ses éléments de manière bidimensionnelle.

**Note :**

* « Bidimensionnelle » signifie que les modules de grille permettent la disposition simultanée des modèles de boîte en lignes et en colonnes.
    
* Utilisez [Flexbox](https://codesweetly.com/css-flexbox-explained) si vous avez seulement besoin de redimensionner et de repositionner des éléments de manière unidimensionnelle.
    

## Conteneur de grille vs. Élément de grille : Quelle est la différence ?

Un **conteneur de grille** est un [élément HTML](https://codesweetly.com/web-tech-terms-h#html-element) dont la valeur de la propriété [`display`](https://codesweetly.com/css-display-property) est `grid` ou `inline-grid`.

Un **élément de grille** est n'importe quel enfant direct d'un conteneur de grille.

![Illustration d'un conteneur de grille et d'un élément de grille](https://www.freecodecamp.org/news/content/images/2023/03/css-grid-container-grid-item-illustration-codesweetly.png align="left")

*Un conteneur de grille (la grande zone jaune sur l'image) est un élément HTML dont la valeur de la propriété display est grid ou inline-grid. Les éléments de grille (les plus petites boîtes à l'intérieur du conteneur jaune) sont les enfants directs d'un conteneur de grille.*

## Qu'est-ce qu'une valeur `grid` en CSS ?

`grid` indique aux navigateurs d'afficher l'élément HTML sélectionné comme un modèle de boîte de grille de niveau bloc.

En d'autres termes, définir la valeur de la propriété `display` d'un élément sur `grid` transforme le modèle de boîte en un module de mise en page de grille de [niveau bloc](https://developer.mozilla.org/en-US/docs/Web/HTML/Block-level_elements).

**Voici un exemple :**

```css
section {
  display: grid;
  background-color: orange;
  margin: 10px;
  padding: 7px;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-5ggr6k?file=style.css)

L'extrait ci-dessus utilise la valeur `grid` pour convertir les éléments `<section>` du document HTML de nœuds `<section>` réguliers en modèles de boîte de grille de niveau bloc.

**Note :**

* La directive `display: grid` crée un conteneur de grille à une seule colonne. Par conséquent, les éléments de grille s'afficheront selon le flux normal de la mise en page (un élément au-dessous de l'autre).
    
* La conversion d'un nœud en modèle de boîte de grille fait des enfants directs de l'élément des éléments de grille.
    
* La directive `display: grid` n'affecte qu'un modèle de boîte et ses enfants directs. Elle n'affecte pas les nœuds petits-enfants.
    

Discutons maintenant de la valeur `inline-grid`.

## Qu'est-ce qu'une valeur `inline-grid` en CSS ?

`inline-grid` indique aux navigateurs d'afficher l'élément HTML sélectionné comme un modèle de boîte de grille de niveau en ligne.

En d'autres termes, définir la valeur de la propriété `display` d'un élément sur `inline-grid` transforme le modèle de boîte en un module de mise en page de grille de [niveau en ligne](https://developer.mozilla.org/en-US/docs/Web/HTML/Inline_elements).

**Voici un exemple :**

```css
section {
  display: inline-grid;
  background-color: orange;
  margin: 10px;
  padding: 7px;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-ekpbac?file=style.css)

L'extrait ci-dessus utilise la valeur `inline-grid` pour convertir les éléments `<section>` du document HTML de nœuds `<section>` réguliers en modèles de boîte de grille de niveau en ligne.

**Note :**

* La conversion d'un nœud en modèle de boîte de grille fait des enfants directs de l'élément des éléments de grille.
    
* La directive `display: inline-grid` n'affecte qu'un modèle de boîte et ses enfants directs. Elle n'affecte pas les nœuds petits-enfants.
    

## Propriétés pour spécifier la mise en page d'une grille

Lors de la conversion d'un élément HTML régulier en un modèle de boîte de grille (ou inline-grid), le module de mise en page de grille fournit deux catégories de propriétés pour positionner la boîte de grille et ses enfants directs :

* Propriétés du conteneur de grille
    
* Propriétés de l'élément de grille
    

## Quelles sont les propriétés du conteneur de grille ?

Les propriétés d'un conteneur de grille spécifient comment les navigateurs doivent disposer les éléments à l'intérieur du modèle de boîte de grille.

**Note :** Nous définissons une propriété de conteneur de grille sur le conteneur, pas sur ses éléments.

Les huit (8) types de propriétés de conteneur de grille sont :

* `grid-template-columns`
    
* `grid-template-rows`
    
* `grid-auto-columns`
    
* `grid-auto-rows`
    
* `justify-content`
    
* `justify-items`
    
* `align-content`
    
* `align-items`
    

Discutons maintenant de ces huit types.

## Qu'est-ce que la propriété `grid-template-columns` de CSS Grid ?

**grid-template-columns** spécifie le nombre et la largeur des colonnes que les navigateurs doivent afficher dans le conteneur de grille sélectionné.

### Exemple 1 : Comment créer un conteneur de grille à deux colonnes

```css
section {
  display: grid;
  grid-template-columns: 95px 1fr;
  background-color: orange;
  margin: 10px;
  padding: 7px;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-uwtgsf?file=style.css)

L'extrait ci-dessus utilise la propriété `grid-template-columns` pour afficher deux colonnes de largeurs différentes dans le conteneur de grille `<section>` sélectionné.

**Note :** Nous avons utilisé l'[unité `fr` (fraction)](https://codesweetly.com/css-unit#fraction-fr) pour mettre à l'échelle la deuxième colonne par rapport à la fraction de l'espace disponible dans le conteneur de grille.

### Exemple 2 : Comment créer un conteneur de grille à trois colonnes

```css
section {
  display: grid;
  grid-template-columns: 15% 60% 25%;
  background-color: orange;
  margin: 10px;
  padding: 7px;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-xaop69?file=style.css)

L'extrait ci-dessus utilise la propriété `grid-template-columns` pour afficher trois colonnes de largeurs différentes dans le conteneur de grille `<section>` sélectionné.

**Note :**

* Vous pouvez utiliser la propriété `grid-auto-columns` pour spécifier des largeurs de colonne par défaut pour toutes les colonnes du conteneur de grille. Par exemple, `grid-auto-columns: 150px` définira des largeurs par défaut de `150px` pour toutes les colonnes. Mais une déclaration `grid-template-columns` l'emportera sur celle-ci.
    
* Les colonnes de grille explicites sont les colonnes que vous définissez explicitement avec la propriété `grid-template-columns`.
    
* Les colonnes de grille implicites sont les colonnes que les navigateurs créent automatiquement. Nous utilisons les propriétés `grid-auto-columns` pour spécifier les tailles de [piste](https://codesweetly.com/css-grid-lines-explained) pour les colonnes implicites.
    

**Astuce :**

* Utilisez la fonction CSS `repeat()` pour spécifier des valeurs `grid-template-columns` avec des motifs répétés. Nous discuterons de la fonction `repeat()` plus tard dans ce tutoriel.
    
* Utilisez la [propriété CSS `column-gap`](https://codesweetly.com/css-column-gap-property) pour créer des espaces entre les colonnes de la grille.
    

## Qu'est-ce que la propriété `grid-template-rows` de CSS Grid ?

**grid-template-rows** spécifie le nombre et la hauteur des lignes que les navigateurs doivent afficher dans le conteneur de grille sélectionné.

### Exemple 1 : Comment créer un conteneur de grille à trois lignes

```css
section {
  display: grid;
  grid-template-rows: 95px 1fr 70px;
  background-color: orange;
  margin: 10px;
  padding: 7px;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-tbisxm?file=style.css)

L'extrait ci-dessus utilise la propriété `grid-template-rows` pour afficher trois lignes de hauteurs différentes dans le conteneur de grille `<section>` sélectionné.

**Note :** Nous avons utilisé l'[unité `fr` (fraction)](https://codesweetly.com/css-unit#fraction-fr) pour mettre à l'échelle la deuxième ligne par rapport à la fraction de l'espace disponible dans le conteneur de grille.

### Exemple 2 : Comment créer un conteneur de grille à trois lignes et quatre colonnes

```css
section {
  display: grid;
  grid-template-rows: 90px 300px 1fr;
  grid-template-columns: auto auto auto auto;
  background-color: orange;
  margin: 10px;
  padding: 7px;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-e5vtot?file=style.css)

L'extrait ci-dessus utilise la propriété `grid-template-rows` pour afficher trois lignes de hauteurs différentes dans le conteneur de grille `<section>` sélectionné.

**Note :**

* Vous pouvez utiliser la propriété `grid-auto-rows` pour spécifier des hauteurs de ligne par défaut pour toutes les lignes du conteneur de grille. Par exemple, `grid-auto-rows: 100px` définira des hauteurs par défaut de `100px` pour toutes les lignes. Mais une déclaration `grid-template-rows` l'emportera sur celle-ci.
    
* Les lignes de grille explicites sont les lignes que vous définissez explicitement avec la propriété `grid-template-rows`.
    
* Les lignes de grille implicites sont les lignes que les navigateurs créent automatiquement. Nous utilisons les propriétés `grid-auto-rows` pour spécifier les tailles de [piste](https://codesweetly.com/css-grid-lines-explained) pour les lignes implicites.
    

**Astuce :**

* Utilisez la fonction CSS `repeat()` pour spécifier des valeurs `grid-template-rows` avec des motifs répétés. Nous discuterons de la fonction `repeat()` plus tard dans ce tutoriel.
    
* Utilisez la [propriété CSS `row-gap`](https://codesweetly.com/css-row-gap-property) pour créer des espaces entre les lignes de la grille.
    

## Qu'est-ce que la propriété `justify-content` de CSS Grid ?

**justify-content** spécifie comment les navigateurs doivent positionner les colonnes d'un conteneur de grille le long de son axe de ligne.

**Note :**

* Un axe de ligne est parfois appelé axe en ligne (inline axis).
    
* La propriété `justify-content` fonctionne si la largeur totale des colonnes est inférieure à la largeur du conteneur de grille. En d'autres termes, vous avez besoin d'un espace libre le long de l'axe de ligne du conteneur pour justifier ses colonnes à gauche ou à droite.
    

La propriété `justify-content` accepte les valeurs suivantes :

* `start`
    
* `center`
    
* `end`
    
* `stretch`
    
* `space-between`
    
* `space-around`
    
* `space-evenly`
    

Discutons de ces valeurs.

### Qu'est-ce que `justify-content: start` dans CSS Grid ?

`start` positionne les colonnes du conteneur de grille sur son bord de début de ligne (row-start edge).

![Illustration de la valeur start de justify-content dans CSS Grid](https://www.freecodecamp.org/news/content/images/2023/03/css-grid-justify-content-start-illustration-codesweetly.png align="left")

*La valeur start de justify-content positionne les colonnes sur le bord de début de ligne du conteneur de grille*

**Voici un exemple :**

```css
section {
  display: grid;
  justify-content: start;
  grid-template-columns: repeat(4, 40px);
  background-color: orange;
  margin: 10px;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-rkwg9r?file=style.css)

L'extrait ci-dessus utilise la valeur `start` pour positionner les colonnes de la `<section>` sur le bord de début de ligne du conteneur de grille.

### Qu'est-ce que `justify-content: center` dans CSS Grid ?

`center` positionne les colonnes du conteneur de grille au centre de l'axe de ligne de la grille.

![Illustration de la valeur center de justify-content dans CSS Grid](https://www.freecodecamp.org/news/content/images/2023/03/css-grid-justify-content-center-illustration-codesweetly.png align="left")

*La valeur center de justify-content positionne les colonnes au centre du conteneur de grille*

**Voici un exemple :**

```css
section {
  display: grid;
  justify-content: center;
  grid-template-columns: repeat(4, 40px);
  background-color: orange;
  margin: 10px;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-ft8n3n?file=style.css)

L'extrait ci-dessus utilise la valeur `center` pour positionner les colonnes de la `<section>` au centre du conteneur de grille.

### Qu'est-ce que `justify-content: end` dans CSS Grid ?

`end` positionne les colonnes d'un conteneur de grille sur son bord de fin de ligne (row-end edge).

![Illustration de la valeur end de justify-content dans CSS Grid](https://www.freecodecamp.org/news/content/images/2023/03/css-grid-justify-content-end-illustration-codesweetly.png align="left")

*La valeur end de justify-content positionne les colonnes sur le bord de fin de ligne du conteneur de grille*

**Voici un exemple :**

```css
section {
  display: grid;
  justify-content: end;
  grid-template-columns: repeat(4, 40px);
  background-color: orange;
  margin: 10px;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-zzaxjf?file=style.css)

L'extrait ci-dessus utilise la valeur `end` pour positionner les colonnes de la `<section>` sur le bord de fin de ligne du conteneur de grille.

### Qu'est-ce que `justify-content: space-between` dans CSS Grid ?

`space-between` effectue les opérations suivantes :

* Il positionne la première colonne d'un conteneur de grille sur son bord de début de ligne.
    
* Il positionne la dernière colonne du conteneur sur le bord de fin de ligne.
    
* Il crée un espacement régulier entre chaque paire de colonnes entre la première et la dernière.
    

![Illustration de la valeur space-between de justify-content dans CSS Grid](https://www.freecodecamp.org/news/content/images/2023/03/css-grid-justify-content-space-between-illustration-codesweetly.png align="left")

*La valeur space-between de justify-content crée un espacement régulier entre chaque paire de colonnes entre la première et la dernière colonne de la grille*

**Voici un exemple :**

```css
section {
  display: grid;
  justify-content: space-between;
  grid-template-columns: repeat(4, 40px);
  background-color: orange;
  margin: 10px;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-ajbrex?file=style.css)

L'extrait ci-dessus utilise la valeur `space-between` pour créer un espacement régulier entre chaque paire de colonnes entre la première et la dernière colonne de la grille.

### Qu'est-ce que `justify-content: space-around` dans CSS Grid ?

`space-around` attribue un espacement égal de chaque côté des colonnes d'un conteneur de grille.

Par conséquent, l'espace avant la première colonne et après la dernière est égal à la moitié de la largeur de l'espace entre chaque paire de colonnes.

![Illustration de la valeur space-around de justify-content dans CSS Grid](https://www.freecodecamp.org/news/content/images/2023/03/css-grid-justify-content-space-around-illustration-codesweetly.png align="left")

*La valeur space-around de justify-content attribue un espacement égal de chaque côté des colonnes du conteneur de grille*

**Voici un exemple :**

```css
section {
  display: grid;
  justify-content: space-around;
  grid-template-columns: repeat(4, 40px);
  background-color: orange;
  margin: 10px;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-qnla5x?file=style.css)

L'extrait ci-dessus utilise la valeur `space-around` pour attribuer un espacement égal de chaque côté des colonnes du conteneur de grille.

### Qu'est-ce que `justify-content: space-evenly` dans CSS Grid ?

`space-evenly` attribue un espacement régulier aux deux extrémités d'un conteneur de grille et entre ses colonnes.

![Illustration de la valeur space-evenly de justify-content dans CSS Grid](https://www.freecodecamp.org/news/content/images/2023/03/css-grid-justify-content-space-evenly-illustration-codesweetly.png align="left")

*La valeur space-evenly de justify-content attribue un espacement régulier aux deux extrémités du conteneur de grille et entre ses colonnes*

**Voici un exemple :**

```css
section {
  display: grid;
  justify-content: space-evenly;
  grid-template-columns: repeat(4, 40px);
  background-color: orange;
  margin: 10px;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-vnd1u3?file=style.css)

Nous avons utilisé la valeur `space-evenly` pour attribuer un espacement régulier aux deux extrémités du conteneur de grille et entre ses colonnes.

## Qu'est-ce que la propriété `justify-items` de CSS Grid ?

**justify-items** spécifie la valeur par défaut de [`justify-self`](https://codesweetly.com/css-grid-justify-self-property) pour tous les éléments de la grille.

La propriété `justify-items` accepte les valeurs suivantes :

* `stretch`
    
* `start`
    
* `center`
    
* `end`
    

Discutons de ces quatre valeurs.

### Qu'est-ce que `justify-items: stretch` dans CSS Grid ?

`stretch` est la valeur par défaut de `justify-items`. Elle étire les éléments du conteneur de grille pour qu'ils remplissent l'axe de ligne (en ligne) de leurs cellules individuelles.

![Illustration de la valeur stretch de justify-items dans CSS Grid](https://www.freecodecamp.org/news/content/images/2023/03/css-grid-justify-items-stretch-illustration-codesweetly.png align="left")

*La valeur stretch de justify-items étire les éléments de la grille pour qu'ils remplissent l'axe de ligne de leurs cellules individuelles*

**Voici un exemple :**

```css
section {
  display: grid;
  justify-items: stretch;
  grid-template-columns: 1fr 1fr;
  background-color: orange;
  margin: 10px;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-dedmgi?file=style.css)

L'extrait ci-dessus utilise la valeur `stretch` pour étirer les éléments de la grille afin qu'ils remplissent l'axe de ligne de leurs cellules individuelles.

### Qu'est-ce que `justify-items: start` dans CSS Grid ?

`start` positionne les éléments d'un conteneur de grille sur le bord de début de ligne de l'axe de ligne de leurs cellules individuelles.

![Illustration de la valeur start de justify-items dans CSS Grid](https://www.freecodecamp.org/news/content/images/2023/03/css-grid-justify-items-start-illustration-codesweetly.png align="left")

*La valeur start de justify-items positionne les éléments de la grille sur le bord de début de ligne de leurs cellules individuelles*

**Voici un exemple :**

```css
section {
  display: grid;
  justify-items: start;
  grid-template-columns: 1fr 1fr;
  background-color: orange;
  margin: 10px;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-zdzwmb?file=style.css)

L'extrait ci-dessus utilise la valeur `start` pour positionner les éléments de la grille sur le bord de début de ligne de leurs cellules individuelles.

### Qu'est-ce que `justify-items: center` dans CSS Grid ?

`center` positionne les éléments d'un conteneur de grille au centre de l'axe de ligne de leurs cellules individuelles.

![Illustration de la valeur center de justify-items dans CSS Grid](https://www.freecodecamp.org/news/content/images/2023/03/css-grid-justify-items-center-illustration-codesweetly.png align="left")

*La valeur center de justify-items positionne les éléments de la grille au centre de leurs cellules individuelles*

**Voici un exemple :**

```css
section {
  display: grid;
  justify-items: center;
  grid-template-columns: 1fr 1fr;
  background-color: orange;
  margin: 10px;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-dsgyni?file=style.css)

L'extrait ci-dessus utilise la valeur `center` pour positionner les éléments de la grille au centre de l'axe de ligne de leurs cellules individuelles.

### Qu'est-ce que `justify-items: end` dans CSS Grid ?

`end` positionne les éléments d'un conteneur de grille sur le bord de fin de ligne de l'axe de ligne de leurs cellules individuelles.

![Illustration de la valeur end de justify-items dans CSS Grid](https://www.freecodecamp.org/news/content/images/2023/03/css-grid-justify-items-end-illustration-codesweetly.png align="left")

*La valeur end de justify-items positionne les éléments de la grille sur le bord de fin de ligne de leurs cellules individuelles*

**Voici un exemple :**

```css
section {
  display: grid;
  justify-items: end;
  grid-template-columns: 1fr 1fr;
  background-color: orange;
  margin: 10px;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-pcenzt?file=style.css)

L'extrait ci-dessus utilise la valeur `end` pour positionner les éléments de la grille sur le bord de fin de ligne de leurs cellules individuelles.

## Qu'est-ce que la propriété `align-content` de CSS Grid ?

**align-content** spécifie comment les navigateurs doivent aligner les lignes d'un conteneur de grille le long de l'axe de colonne du conteneur.

**Note :**

* Un axe de colonne est parfois appelé axe de bloc (block axis).
    
* La propriété `align-content` fonctionne si la hauteur totale des lignes est inférieure à la hauteur du conteneur de grille. En d'autres termes, vous avez besoin d'un espace libre le long de l'axe de colonne du conteneur pour aligner ses lignes vers le haut ou vers le bas.
    

La propriété `align-content` accepte les valeurs suivantes :

* `start`
    
* `center`
    
* `end`
    
* `stretch`
    
* `space-between`
    
* `space-around`
    
* `space-evenly`
    

Discutons de ces valeurs.

### Qu'est-ce que `align-content: start` dans CSS Grid ?

`start` aligne les lignes d'un conteneur de grille sur le bord de début de colonne (column-start edge) de l'axe de colonne de la grille.

![Illustration de la valeur start de align-content dans CSS Grid](https://www.freecodecamp.org/news/content/images/2023/03/css-grid-align-content-start-illustration-codesweetly.png align="left")

*La valeur start de align-content aligne les lignes sur le bord de début de colonne du conteneur de grille*

**Voici un exemple :**

```css
section {
  display: grid;
  align-content: start;
  grid-template-columns: 1fr 1fr;
  background-color: orange;
  margin: 10px;
  height: 300px;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-cbmgr1?file=style.css)

L'extrait ci-dessus utilise la valeur `start` pour aligner les lignes de la `<section>` sur le bord de début de colonne du conteneur de grille.

### Qu'est-ce que `align-content: center` dans CSS Grid ?

`center` aligne les lignes d'un conteneur de grille au centre de l'axe de colonne de la grille.

![Illustration de la valeur center de align-content dans CSS Grid](https://www.freecodecamp.org/news/content/images/2023/03/css-grid-align-content-center-illustration-codesweetly.png align="left")

*La valeur center de align-content aligne les lignes au centre du conteneur de grille*

```css
section {
  display: grid;
  align-content: center;
  grid-template-columns: 1fr 1fr;
  background-color: orange;
  margin: 10px;
  height: 300px;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-83kj8v?file=style.css)

L'extrait ci-dessus utilise la valeur `center` pour aligner les lignes de la `<section>` au centre du conteneur de grille.

### Qu'est-ce que `align-content: end` dans CSS Grid ?

`end` aligne les lignes d'un conteneur de grille sur le bord de fin de colonne (column-end edge) de l'axe de colonne de la grille.

![Illustration de la valeur end de align-content dans CSS Grid](https://www.freecodecamp.org/news/content/images/2023/03/css-grid-align-content-end-illustration-codesweetly.png align="left")

*La valeur end de align-content aligne les lignes sur le bord de fin de colonne du conteneur de grille*

**Voici un exemple :**

```css
section {
  display: grid;
  align-content: end;
  grid-template-columns: 1fr 1fr;
  background-color: orange;
  margin: 10px;
  height: 300px;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-lc1lus?file=style.css)

L'extrait ci-dessus utilise la valeur `end` pour aligner les lignes de la `<section>` sur le bord de fin de colonne du conteneur de grille.

### Qu'est-ce que `align-content: space-between` dans CSS Grid ?

`space-between` effectue les opérations suivantes :

* Il aligne la première ligne d'un conteneur de grille sur son bord de début de colonne.
    
* Il aligne la dernière ligne du conteneur sur le bord de fin de colonne.
    
* Il crée un espacement régulier entre chaque paire de lignes entre la première et la dernière.
    

![Illustration de la valeur space-between de align-content dans CSS Grid](https://www.freecodecamp.org/news/content/images/2023/03/css-grid-align-content-space-between-illustration-codesweetly.png align="left")

*La valeur space-between de align-content crée un espacement régulier entre chaque paire de lignes entre la première et la dernière ligne de la grille*

**Voici un exemple :**

```css
section {
  display: grid;
  align-content: space-between;
  grid-template-columns: 1fr 1fr;
  background-color: orange;
  margin: 10px;
  height: 300px;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-ieqvih?file=style.css)

L'extrait ci-dessus utilise la valeur `space-between` pour créer un espacement régulier entre chaque paire de lignes entre la première et la dernière ligne de la grille.

### Qu'est-ce que `align-content: space-around` dans CSS Grid ?

`space-around` attribue un espacement égal de chaque côté des lignes d'un conteneur de grille.

Par conséquent, l'espace avant la première ligne et après la dernière est égal à la moitié de la hauteur de l'espace entre chaque paire de lignes.

![Illustration de la valeur space-around de align-content dans CSS Grid](https://www.freecodecamp.org/news/content/images/2023/03/css-grid-align-content-space-around-illustration-codesweetly.png align="left")

*La valeur space-around de align-content attribue un espacement égal de chaque côté des lignes du conteneur de grille*

**Voici un exemple :**

```css
section {
  display: grid;
  align-content: space-around;
  grid-template-columns: 1fr 1fr;
  background-color: orange;
  margin: 10px;
  height: 300px;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-eyzta5?file=style.css)

L'extrait ci-dessus utilise la valeur `space-around` pour attribuer un espacement égal de chaque côté des lignes du conteneur de grille.

### Qu'est-ce que `align-content: space-evenly` dans CSS Grid ?

`space-evenly` attribue un espacement régulier aux deux extrémités d'un conteneur de grille et entre ses lignes.

![Illustration de la valeur space-evenly de align-content dans CSS Grid](https://www.freecodecamp.org/news/content/images/2023/03/css-grid-align-content-space-evenly-illustration-codesweetly.png align="left")

*La valeur space-evenly de align-content attribue un espacement régulier aux deux extrémités du conteneur de grille et entre ses lignes*

**Voici un exemple :**

```css
section {
  display: grid;
  align-content: space-evenly;
  grid-template-columns: 1fr 1fr;
  background-color: orange;
  margin: 10px;
  height: 300px;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-il5vu1?file=style.css)

Nous avons utilisé la valeur `space-evenly` pour attribuer un espacement régulier aux deux extrémités du conteneur de grille et entre ses lignes.

## Qu'est-ce que la propriété `align-items` de CSS Grid ?

**align-items** spécifie la valeur par défaut de [`align-self`](https://codesweetly.com/css-grid-align-self-property) pour tous les éléments de la grille.

La propriété `align-items` accepte les valeurs suivantes :

* `stretch`
    
* `start`
    
* `center`
    
* `end`
    

Discutons des quatre valeurs ci-dessous.

### Qu'est-ce que `align-items: stretch` dans CSS Grid ?

`stretch` est la valeur par défaut pour `align-items`. Elle étire les éléments du conteneur de grille pour qu'ils remplissent l'axe de colonne (bloc) de leurs cellules individuelles.

![Illustration de la valeur stretch de align-items dans CSS Grid](https://www.freecodecamp.org/news/content/images/2023/03/css-grid-align-items-stretch-illustration-codesweetly.png align="left")

*La valeur stretch de align-items étire les éléments de la grille pour qu'ils remplissent l'axe de colonne de leurs cellules individuelles*

**Voici un exemple :**

```css
section {
  display: grid;
  align-items: stretch;
  grid-template-columns: 1fr 1fr;
  background-color: orange;
  margin: 10px;
  height: 400px;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-fia3ra?file=style.css)

L'extrait ci-dessus utilise la valeur `stretch` pour étirer les éléments de la grille afin qu'ils remplissent l'axe de colonne de leurs cellules individuelles.

### Qu'est-ce que `align-items: start` dans CSS Grid ?

`start` aligne les éléments d'un conteneur de grille sur le bord de début de colonne de l'axe de colonne de leurs cellules individuelles.

![Illustration de la valeur start de align-items dans CSS Grid](https://www.freecodecamp.org/news/content/images/2023/03/css-grid-align-items-start-illustration-codesweetly.png align="left")

*La valeur start de align-items aligne les éléments de la grille sur le bord de début de colonne de leurs cellules individuelles*

**Voici un exemple :**

```css
section {
  display: grid;
  align-items: start;
  grid-template-columns: 1fr 1fr;
  background-color: orange;
  margin: 10px;
  height: 400px;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-achetg?file=style.css)

L'extrait ci-dessus utilise la valeur `start` pour aligner les éléments de la grille sur le bord de début de colonne de leurs cellules individuelles.

### Qu'est-ce que `align-items: center` dans CSS Grid ?

`center` aligne les éléments d'un conteneur de grille au centre de l'axe de colonne de leurs cellules individuelles.

![Illustration de la valeur center de align-items dans CSS Grid](https://www.freecodecamp.org/news/content/images/2023/03/css-grid-align-items-center-illustration-codesweetly.png align="left")

*La valeur center de align-items aligne les éléments de la grille au centre de leurs cellules individuelles*

**Voici un exemple :**

```css
section {
  display: grid;
  align-items: center;
  grid-template-columns: 1fr 1fr;
  background-color: orange;
  margin: 10px;
  height: 400px;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-cmqydk?file=style.css)

L'extrait ci-dessus utilise la valeur `center` pour aligner les éléments de la grille au centre de l'axe de colonne de leurs cellules individuelles.

### Qu'est-ce que `align-items: end` dans CSS Grid ?

`end` aligne les éléments d'un conteneur de grille sur le bord de fin de colonne de l'axe de colonne de leurs cellules individuelles.

![Illustration de la valeur end de align-items dans CSS Grid](https://www.freecodecamp.org/news/content/images/2023/03/css-grid-align-items-end-illustration-codesweetly.png align="left")

*La valeur end de align-items aligne les éléments de la grille sur le bord de fin de colonne de leurs cellules individuelles*

**Voici un exemple :**

```css
section {
  display: grid;
  align-items: end;
  grid-template-columns: 1fr 1fr;
  background-color: orange;
  margin: 10px;
  height: 400px;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-jei1qv?file=style.css)

L'extrait ci-dessus utilise la valeur `end` pour aligner les éléments de la grille sur le bord de fin de colonne de leurs cellules individuelles.

Maintenant que nous connaissons les types de propriétés de conteneur de grille CSS, nous pouvons discuter des propriétés d'élément de grille.

## Quelles sont les propriétés de l'élément de grille ?

Les propriétés d'un élément de grille spécifient comment les navigateurs doivent disposer un élément spécifié à l'intérieur du modèle de boîte de grille.

**Note :** Nous définissons une propriété d'élément de grille sur l'élément lui-même, pas sur son conteneur.

Les dix (10) types de propriétés d'élément de grille sont :

* `justify-self`
    
* `align-self`
    
* `grid-column-start`
    
* `grid-column-end`
    
* `grid-column`
    
* `grid-row-start`
    
* `grid-row-end`
    
* `grid-row`
    
* `grid-area`
    
* `grid-template-areas`
    

Discutons de ces dix types maintenant.

## Qu'est-ce que la propriété `justify-self` de CSS Grid ?

**justify-self** spécifie comment les navigateurs doivent positionner l'élément de grille sélectionné le long de l'axe de ligne (en ligne) de sa cellule.

La propriété `justify-self` accepte les valeurs suivantes :

* `stretch`
    
* `start`
    
* `center`
    
* `end`
    

Discutons de ces quatre valeurs.

### Qu'est-ce que `justify-self: stretch` dans CSS Grid ?

`stretch` est la valeur par défaut de `justify-self`. Elle étire l'élément de grille sélectionné pour qu'il remplisse l'axe de ligne (en ligne) de sa cellule.

![Illustration de la valeur stretch de justify-self dans CSS Grid](https://www.freecodecamp.org/news/content/images/2023/03/css-grid-justify-self-stretch-illustration-codesweetly.png align="left")

*La valeur stretch de justify-self étire l'élément de grille sélectionné pour qu'il remplisse l'axe de ligne de sa cellule*

**Voici un exemple :**

```css
.grid-item1 {
  justify-self: stretch;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-82a3ep?file=style.css)

L'extrait ci-dessus utilise la valeur `stretch` pour étirer `grid-item1` afin qu'il remplisse l'axe de ligne de sa cellule.

### Qu'est-ce que `justify-self: start` dans CSS Grid ?

`start` positionne l'élément de grille sélectionné sur le bord de début de ligne de l'axe de ligne de sa cellule.

![Illustration de la valeur start de justify-self dans CSS Grid](https://www.freecodecamp.org/news/content/images/2023/03/css-grid-justify-self-start-illustration-codesweetly.png align="left")

*La valeur start de justify-self positionne l'élément de grille sélectionné sur le bord de début de ligne de sa cellule*

**Voici un exemple :**

```css
.grid-item1 {
  justify-self: start;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-cnz92l?file=style.css)

L'extrait ci-dessus utilise la valeur `start` pour positionner `grid-item1` sur le bord de début de ligne de sa cellule.

### Qu'est-ce que `justify-self: center` dans CSS Grid ?

`center` positionne l'élément de grille sélectionné au centre de l'axe de ligne de sa cellule.

![Illustration de la valeur center de justify-self dans CSS Grid](https://www.freecodecamp.org/news/content/images/2023/03/css-grid-justify-self-center-illustration-codesweetly.png align="left")

*La valeur center de justify-self positionne l'élément de grille sélectionné au centre de sa cellule*

**Voici un exemple :**

```css
.grid-item1 {
  justify-self: center;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-9kspmx?file=style.css)

L'extrait ci-dessus utilise la valeur `center` pour positionner `grid-item1` au centre de l'axe de ligne de sa cellule.

### Qu'est-ce que `justify-self: end` dans CSS Grid ?

`end` positionne l'élément de grille sélectionné sur le bord de fin de ligne de l'axe de ligne de sa cellule.

![Illustration de la valeur end de justify-self dans CSS Grid](https://www.freecodecamp.org/news/content/images/2023/03/css-grid-justify-self-end-illustration-codesweetly.png align="left")

*La valeur end de justify-self positionne l'élément de grille sélectionné sur le bord de fin de ligne de sa cellule*

**Voici un exemple :**

```css
.grid-item1 {
  justify-self: end;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-xschhb?file=style.css)

L'extrait ci-dessus utilise la valeur `end` pour positionner `grid-item1` sur le bord de fin de ligne de sa cellule.

## Qu'est-ce que la propriété `align-self` de CSS Grid ?

**align-self** spécifie comment les navigateurs doivent aligner l'élément de grille sélectionné le long de l'axe de colonne (bloc) de sa cellule.

La propriété `align-self` accepte les valeurs suivantes :

* `stretch`
    
* `start`
    
* `center`
    
* `end`
    

Discutons des quatre valeurs ci-dessous.

### Qu'est-ce que `align-self: stretch` dans CSS Grid ?

`stretch` est la valeur par défaut de `align-self`. Elle étire l'élément de grille sélectionné pour qu'il remplisse l'axe de colonne (bloc) de sa cellule.

![Illustration de la valeur stretch de align-self dans CSS Grid](https://www.freecodecamp.org/news/content/images/2023/03/css-grid-align-self-stretch-illustration-codesweetly-1.png align="left")

*La valeur stretch de align-self étire l'élément de grille sélectionné pour qu'il remplisse l'axe de colonne de sa cellule*

**Voici un exemple :**

```css
.grid-item1 {
  align-self: stretch;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-unnbb9?file=style.css)

L'extrait ci-dessus utilise la valeur `stretch` pour étirer `grid-item1` afin qu'il remplisse l'axe de colonne de sa cellule.

### Qu'est-ce que `align-self: start` dans CSS Grid ?

`start` aligne l'élément de grille sélectionné sur le bord de début de colonne de l'axe de colonne de sa cellule.

![Illustration de la valeur start de align-self dans CSS Grid](https://www.freecodecamp.org/news/content/images/2023/03/css-grid-align-self-start-illustration-codesweetly-1.png align="left")

*La valeur start de align-self aligne l'élément de grille sélectionné sur le bord de début de colonne de sa cellule*

**Voici un exemple :**

```css
.grid-item1 {
  align-self: start;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-ytttz4?file=style.css)

L'extrait ci-dessus utilise la valeur `start` pour aligner `grid-item1` sur le bord de début de colonne de sa cellule.

### Qu'est-ce que `align-self: center` dans CSS Grid ?

`center` aligne l'élément de grille sélectionné au centre de l'axe de colonne de sa cellule.

![Illustration de la valeur center de align-self dans CSS Grid](https://www.freecodecamp.org/news/content/images/2023/03/css-grid-align-self-center-illustration-codesweetly.png align="left")

*La valeur center de align-self aligne l'élément de grille sélectionné au centre de sa cellule*

**Voici un exemple :**

```css
.grid-item1 {
  align-self: center;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-fpv4ed?file=style.css)

L'extrait ci-dessus utilise la valeur `center` pour aligner `grid-item1` au centre de l'axe de colonne de sa cellule.

### Qu'est-ce que `align-self: end` dans CSS Grid ?

`end` aligne l'élément de grille sélectionné sur le bord de fin de colonne de l'axe de colonne de sa cellule.

![Illustration de la valeur end de align-self dans CSS Grid](https://www.freecodecamp.org/news/content/images/2023/03/css-grid-align-self-end-illustration-codesweetly.png align="left")

*La valeur end de align-self aligne l'élément de grille sélectionné sur le bord de fin de colonne de sa cellule*

**Voici un exemple :**

```css
.grid-item1 {
  align-self: end;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-vvmwzv?file=style.css)

L'extrait ci-dessus utilise la valeur `end` pour aligner grid-item1 sur le bord de fin de colonne de sa cellule.

## Qu'est-ce que la propriété `grid-column-start` de CSS Grid ?

**grid-column-start** spécifie où l'élément de grille sélectionné doit commencer (ou s'étendre) le long de l'axe de ligne (en ligne) du conteneur de grille.

La propriété `grid-column-start` accepte les valeurs suivantes :

* `auto`
    
* `<column-line-number>`
    
* `span <number-of-columns>`
    

### Exemple 1 : Comment faire démarrer automatiquement l'élément de grille sélectionné en suivant le flux normal des colonnes

```css
.grid-item1 {
  grid-column-start: auto;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-rvhhxh?file=style.css)

L'extrait ci-dessus utilise la valeur `auto` pour faire démarrer automatiquement `grid-item1` selon le flux normal de la mise en page des colonnes.

### Exemple 2 : Comment faire démarrer l'élément de grille sélectionné à la ligne de colonne 3

```css
.grid-item1 {
  grid-column-start: 3;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-ep6zgd?file=style.css)

L'extrait ci-dessus utilise la propriété `grid-column-start` pour faire démarrer `grid-item1` à la [ligne de colonne](https://codesweetly.com/css-grid-lines-explained) 3.

### Exemple 3 : Comment étendre l'élément de grille sélectionné sur deux colonnes

```css
.grid-item1 {
  grid-column-start: span 2;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-w1nw8k?file=style.css)

L'extrait ci-dessus utilise la valeur `span 2` pour étendre `grid-item1` sur deux colonnes.

## Qu'est-ce que la propriété `grid-column-end` de CSS Grid ?

**grid-column-end** spécifie où l'élément de grille sélectionné doit se terminer (ou s'étendre) le long de l'axe de ligne (en ligne) du conteneur de grille.

La propriété `grid-column-end` accepte les valeurs suivantes :

* `auto`
    
* `<column-line-number>`
    
* `span <number-of-columns>`
    

### Exemple 1 : Comment faire terminer automatiquement l'élément de grille sélectionné en suivant le flux normal des colonnes

```css
.grid-item1 {
  grid-column-end: auto;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-1mmxhp?file=style.css)

L'extrait ci-dessus utilise la valeur `auto` pour faire terminer automatiquement `grid-item1` selon le flux normal de la mise en page.

### Exemple 2 : Comment faire terminer l'élément de grille sélectionné à la ligne de colonne 3

```css
.grid-item1 {
  grid-column-start: 1;
  grid-column-end: 3;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-hjcfhc?file=style.css)

L'extrait ci-dessus utilise la propriété `grid-column-end` pour faire terminer `grid-item1` à la [ligne de colonne](https://codesweetly.com/css-grid-lines-explained) 3.

### Exemple 3 : Comment étendre l'élément de grille sélectionné sur deux colonnes

```css
.grid-item1 {
  grid-column-start: 2;
  grid-column-end: span 2;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-yhe3ew?file=style.css)

L'extrait ci-dessus utilise la valeur `span 2` pour étendre `grid-item1` sur deux colonnes.

## Qu'est-ce que la propriété `grid-column` de CSS Grid ?

**grid-column** est un raccourci pour les propriétés `grid-column-start` et `grid-column-end`.

En d'autres termes, au lieu d'écrire :

```css
.grid-item1 {
  grid-column-start: 1;
  grid-column-end: 3;
}
```

Vous pouvez alternativement utiliser la propriété `grid-column` pour raccourcir votre code ainsi :

```css
.grid-item1 {
  grid-column: 1 / 3;
}
```

**Voici la syntaxe de grid-column :**

```css
grid-column: grid-column-start / grid-column-end;
```

## Qu'est-ce que la propriété `grid-row-start` de CSS Grid ?

**grid-row-start** spécifie où l'élément de grille sélectionné doit commencer (ou s'étendre) le long de l'axe de colonne (bloc) du conteneur de grille.

La propriété `grid-row-start` accepte les valeurs suivantes :

* `auto`
    
* `<row-line-number>`
    
* `span <number-of-rows>`
    

### Exemple 1 : Comment faire démarrer automatiquement l'élément de grille sélectionné en suivant le flux normal des lignes

```css
.grid-item1 {
  grid-row-start: auto;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-qthpn6?file=style.css)

L'extrait ci-dessus utilise la valeur `auto` pour faire démarrer automatiquement `grid-item1` selon le flux normal de la mise en page des lignes.

### Exemple 2 : Comment faire démarrer l'élément de grille sélectionné à la ligne de ligne 3

```css
.grid-item1 {
  grid-row-start: 3;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-phrjcb?file=style.css)

L'extrait ci-dessus utilise la propriété `grid-row-start` pour faire démarrer `grid-item1` à la [ligne de ligne](https://codesweetly.com/css-grid-lines-explained) 3.

### Exemple 3 : Comment étendre l'élément de grille sélectionné sur deux lignes

```css
.grid-item1 {
  grid-row-start: span 2;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-5bchie?file=style.css)

L'extrait ci-dessus utilise la valeur `span 2` pour étendre `grid-item1` sur deux lignes.

## Qu'est-ce que la propriété `grid-row-end` de CSS Grid ?

**grid-row-end** spécifie où l'élément de grille sélectionné doit se terminer (ou s'étendre) le long de l'axe de colonne (bloc) du conteneur de grille.

La propriété `grid-row-end` accepte les valeurs suivantes :

* `auto`
    
* `<column-line-number>`
    
* `span <number-of-columns>`
    

### Exemple 1 : Comment faire terminer automatiquement l'élément de grille sélectionné en suivant le flux normal des lignes

```css
.grid-item1 {
  grid-row-end: auto;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-w1rpy8?file=style.css)

L'extrait ci-dessus utilise la valeur `auto` pour faire terminer automatiquement `grid-item1` selon le flux normal de la mise en page des lignes.

### Exemple 2 : Comment faire terminer l'élément de grille sélectionné à la ligne de ligne 5

```css
.grid-item1 {
  grid-row-start: 1;
  grid-row-end: 5;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-wps8a3?file=style.css)

L'extrait ci-dessus utilise la propriété `grid-row-end` pour faire terminer `grid-item1` à la [ligne de ligne](https://codesweetly.com/css-grid-lines-explained) 5.

### Exemple 3 : Comment étendre l'élément de grille sélectionné sur trois lignes

```css
.grid-item1 {
  grid-row-end: span 3;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-skcbxf?file=style.css)

L'extrait ci-dessus utilise la valeur `span 3` pour étendre `grid-item1` sur trois lignes.

## Qu'est-ce que la propriété `grid-row` de CSS Grid ?

**grid-row** est un raccourci pour les propriétés `grid-row-start` et `grid-row-end`.

En d'autres termes, au lieu d'écrire :

```css
.grid-item1 {
  grid-row-start: 1;
  grid-row-end: 5;
}
```

Vous pouvez alternativement utiliser la propriété `grid-row` pour raccourcir votre code ainsi :

```css
.grid-item1 {
  grid-row: 1 / 5;
}
```

**Voici la syntaxe de grid-row :**

```css
grid-row: grid-row-start / grid-row-end;
```

## Qu'est-ce que la propriété `grid-area` de CSS Grid ?

Vous pouvez utiliser la propriété **grid-area** pour les objectifs suivants :

1. Comme raccourci pour les propriétés `grid-column-start`, `grid-column-end`, `grid-row-start` et `grid-row-end`.
    
2. Pour spécifier le nom d'un élément de grille.
    

Discutons de ces deux objectifs ci-dessous.

### Comment utiliser `grid-area` comme raccourci

Voici la syntaxe pour utiliser la propriété `grid-area` comme raccourci pour les propriétés `grid-column-start`, `grid-column-end`, `grid-row-start` et `grid-row-end` :

```css
.votre-element-de-grille {
  grid-area: grid-row-start / grid-column-start / grid-row-end / grid-column-end;
}
```

Par conséquent, au lieu d'écrire :

```css
.grid-item1 {
  grid-row-start: 3;
  grid-row-end: 5;
  grid-column-start: 1;
  grid-column-end: span 2;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-sqkxmk?file=style.css)

Vous pouvez alternativement utiliser la propriété `grid-area` pour raccourcir votre code ainsi :

```css
.grid-item1 {
  grid-area: 3 / 1 / 5 / span 2;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-42swnh?file=style.css)

### Comment utiliser `grid-area` pour spécifier le nom d'un élément de grille

Voici la syntaxe pour utiliser la propriété `grid-area` pour spécifier le nom d'un élément de grille :

```css
.votre-element-de-grille {
  grid-area: nom-de-lelement;
}
```

**Voici un exemple :**

```css
.grid-item1 {
  grid-area: firstDiv;
}

.grid-item2 {
  grid-area: middleDiv;
}

.grid-item2 {
  grid-area: lastDiv;
}
```

```html
<section>
  <div class="grid-item1">1</div>
  <div class="grid-item2">2</div>
  <div class="grid-item3">3</div>
</section>
```

L'utilisation de `grid-area` pour définir un élément de grille nommé permet à la propriété `grid-template-areas` de votre conteneur de grille d'utiliser ce nom pour définir la taille et l'emplacement de l'élément.

## Qu'est-ce que la propriété `grid-template-areas` de CSS Grid ?

**grid-template-areas** spécifie la zone où vous souhaitez placer les *éléments de grille nommés* à l'intérieur d'un conteneur de grille.

**Rappel :** Nous utilisons la propriété CSS `[grid-area](#heading-comment-utiliser-grid-area-pour-specifier-le-nom-dun-element-de-grille)` pour nommer les éléments de grille.

### Exemple 1 : Comment placer un élément de grille nommé sur trois colonnes

```css
.grid-item1 {
  grid-area: firstDiv;
}

section {
  display: grid;
  grid-template-areas: "firstDiv firstDiv firstDiv . .";
  background-color: orange;
  margin: 50px;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-1sw8ww?file=style.css)

L'extrait ci-dessus utilise la propriété `grid-template-areas` pour placer `grid-item1` sur les trois premières zones de colonnes.

**Notez les points suivants :**

* Les guillemets (`""`) définissent chaque ligne de la grille.
    
* Un symbole de point (`.`) définit un élément de grille non nommé.
    
* Nous avons utilisé le caractère d'espace pour séparer les colonnes de la grille.
    

### Exemple 2 : Comment spécifier le placement de plusieurs éléments de grille nommés

```css
.grid-item1 {
  grid-area: header;
}

.grid-item2 {
  grid-area: article;
}

.grid-item3 {
  grid-area: footer;
}

.grid-item4 {
  grid-area: sidebar;
}

.grid-item5 {
  grid-area: ads1;
}

.grid-item6 {
  grid-area: ads2;
}

.grid-item7 {
  grid-area: ads3;
}

section {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  grid-template-rows: repeat(7, 1fr);
  grid-template-areas:
    "header header header header header"
    "sidebar article article article ads1"
    "sidebar article article article ads1"
    "sidebar article article article ads1"
    "sidebar article article article ads2"
    "sidebar article article article ads3"
    "sidebar footer footer footer footer";
  background-color: orange;
  margin: 30px;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-9b5emj?file=style.css)

L'extrait ci-dessus utilise la propriété `grid-template-areas` pour spécifier où les navigateurs doivent placer les éléments de grille à travers les lignes et les colonnes du conteneur de grille.

### Choses importantes à savoir sur la propriété `grid-template-areas`

Voici quatre faits essentiels à retenir lors de l'utilisation de la propriété `grid-template-areas` :

#### 1\. `grid-template-areas` n'autorise pas les cellules vides

La propriété `grid-template-areas` exige que vous fournissiez un élément pour toutes les cellules de la grille.

Par exemple, considérez cet extrait :

```css
grid-template-areas:
  "header header"
  "sidebar article article article ads1"
  "sidebar article article article ads1"
  "sidebar article article article ads1"
  "sidebar article article article ads2"
  "sidebar article article article ads3"
  "sidebar footer footer footer footer";
```

Ceci est une valeur `grid-template-areas` invalide car la première ligne est incomplète.

En d'autres termes, la première ligne est la seule avec deux colonnes. Cependant, `grid-template-areas` attend que toutes les lignes d'un conteneur de grille aient le même nombre de colonnes.

#### 2\. Vous pouvez utiliser des points pour spécifier des cellules vides

Supposons que vous souhaitiez laisser certaines cellules vides. Dans ce cas, utilisez un point (`.`) ou plusieurs points non espacés (`....`).

**Voici un exemple :**

```css
grid-template-areas:
  "header header . . ."
  "sidebar article article article ads1"
  "sidebar article article article ads1"
  "sidebar article article article ads1"
  "sidebar article article article ads2"
  "sidebar article article article ads3"
  "sidebar footer footer footer footer";
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-yfhx4g?file=style.css)

L'extrait ci-dessus utilise les trois symboles de point *espacés* (`.`) pour indiquer trois cellules vides.

#### 3\. `grid-template-areas` n'autorise pas le placement d'un élément à plusieurs endroits

La propriété `grid-template-areas` ne peut pas placer des éléments deux fois (dans des zones distinctes) au sein d'un même conteneur de grille.

Par exemple, considérez cet extrait :

```css
grid-template-areas:
  "header header header header header"
  "sidebar article article article ads1"
  "sidebar article article article ads1"
  "sidebar article article article ads1"
  "sidebar article article article ads2"
  "sidebar article article article ads3"
  "sidebar footer header header header";
```

Ceci est une valeur `grid-template-areas` invalide car l'élément `header` occupe deux zones de grille distinctes.

#### 4\. `grid-template-areas` n'autorise que les zones rectangulaires

La propriété `grid-template-areas` ne peut pas créer de zones non rectangulaires (telles que des formes en T ou en L).

Par exemple, considérez cet extrait :

```css
grid-template-areas:
  "header header header header header"
  "sidebar ads1 ads1 ads1 ads1"
  "sidebar article article article ads1"
  "sidebar article article article ads1"
  "sidebar article article article ads2"
  "sidebar article article article ads3"
  "sidebar footer footer footer footer";
```

Ceci est une valeur `grid-template-areas` invalide car l'élément `ads1` crée une zone de grille non rectangulaire.

Maintenant que nous connaissons les types de propriétés d'élément de grille CSS, nous pouvons discuter de la manière de définir des tailles de grille minimales et maximales.

## Comment utiliser la fonction CSS `minmax()` pour définir des tailles de grille minimales et maximales

**minmax()** est une fonction CSS Grid permettant de définir les tailles minimales et maximales d'une grille.

### Syntaxe de la fonction CSS `minmax()`

`minmax()` accepte deux arguments. Voici la syntaxe :

```css
minmax(taille-minimale, taille-maximale)
```

**Notez les points suivants :**

* L'argument `taille-minimale` spécifie la plus petite taille pour une longueur spécifique.
    
* L'argument `taille-maximale` spécifie la plus grande taille pour une longueur spécifique.
    
* Les arguments de `minmax()` peuvent être n'importe laquelle des [longueurs CSS](https://codesweetly.com/css-unit) non négatives, ou l'un des mots-clés `auto`, `min-content` ou `max-content`.
    
* Supposons que l'argument `taille-maximale` soit inférieur à `taille-minimale`. Dans ce cas, les navigateurs ignoreront la `taille-maximale` et traiteront la fonction `minmax()` comme [`min()`](https://developer.mozilla.org/en-US/docs/Web/CSS/min).
    
* Une [unité `fr`](https://codesweetly.com/css-unit#fraction-fr) est une unité \_in\_valide pour l'argument `taille-minimale`.
    

### Comment utiliser la fonction CSS `minmax()`

Vous pouvez utiliser la fonction `minmax()` comme valeur pour les propriétés CSS suivantes :

* `grid-template-columns`
    
* `grid-template-rows`
    
* `grid-auto-columns`
    
* `grid-auto-rows`
    

### Exemples de la fonction CSS `minmax()`

Voici des exemples du fonctionnement de la fonction CSS `minmax()`.

#### Comment définir une taille de ligne de grille minimale de `70px` et maximale de `250px` 

```css
section {
  display: grid;
  grid-template-rows: 50px 100px minmax(70px, 250px);
  grid-template-columns: auto auto auto;
  background-color: orange;
  margin: 10px;
  padding: 7px;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-giarya?file=style.css)

Nous avons utilisé la fonction CSS `minmax()` pour définir la hauteur de la troisième ligne de la `<section>` à un minimum de `70px` et un maximum de `250px`.

#### Comment définir une taille de colonne de grille minimale de `30%` et maximale de `70%` 

```css
section {
  display: grid;
  grid-template-rows: auto auto auto;
  grid-template-columns: 1fr minmax(30%, 70%) 1fr;
  background-color: orange;
  margin: 10px;
  padding: 7px;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-ekn23p?file=style.css)

Nous avons utilisé la fonction CSS `minmax()` pour définir la largeur de la deuxième colonne de la `<section>` à un minimum de `30%` et un maximum de `70%`.

**Note :** Vous pouvez utiliser la fonction CSS `repeat()` pour spécifier des valeurs `grid-template-rows` ou `grid-template-columns` avec des motifs répétés. Discutons de la fonction `repeat()` maintenant.

## Comment utiliser la fonction CSS `repeat()` pour définir des pistes de grille avec des motifs répétés

La fonction CSS **repeat()** vous permet d'écrire des valeurs plus concises et lisibles lors de la spécification de plusieurs [pistes de grille](https://codesweetly.com/css-grid-lines-explained) avec des motifs répétés.

**Note :**

* Une piste fait référence à une colonne (ou une ligne) d'un conteneur de grille.
    
* Vous pouvez utiliser `repeat()` comme valeur pour les propriétés CSS `grid-template-columns` ou `grid-template-rows`.
    

### Syntaxe de la fonction CSS `repeat()`

`repeat()` accepte deux arguments. Voici la syntaxe :

```css
repeat(nombre-de-repetitions, liste-de-pistes-a-repeter)
```

### Argument 1 : `nombre-de-repetitions`

L'argument `nombre-de-repetitions` spécifie le nombre de fois que les navigateurs doivent répéter la liste de pistes spécifiée (le deuxième argument).

L'argument `nombre-de-repetitions` peut être l'une des valeurs suivantes :

* Le nombre `1` ou ses multiples
    
* `auto-fill`
    
* `auto-fit`
    

#### `auto-fill` vs. `auto-fit` : Quelle est la différence ?

Les valeurs `auto-fill` et `auto-fit` créent automatiquement autant de pistes que nécessaire pour remplir un conteneur de grille sans provoquer de débordement.

La différence entre les deux valeurs est que `auto-fit` réduit les pistes vides à zéro pixel (`0px`). Mais `auto-fill` affiche à la fois les pistes vides et remplies.

**Note :** Les pistes vides sont des colonnes ou des lignes sans élément de grille.

### Argument 2 : `liste-de-pistes-a-repeter`

L'argument `liste-de-pistes-a-repeter` spécifie le motif de piste que vous souhaitez répéter sur l'axe horizontal ou vertical d'un conteneur de grille.

En d'autres termes, `liste-de-pistes-a-repeter` se compose d'une ou plusieurs valeurs spécifiant les tailles des pistes que les navigateurs doivent répéter à l'intérieur d'un conteneur de grille.

**Note :** Supposons que votre `nombre-de-repetitions` soit `auto-fill` ou `auto-fit`. Dans ce cas, vous ne pouvez utiliser que des [tailles fixes](https://developer.mozilla.org/en-US/docs/Web/CSS/repeat#fixed-size) comme argument pour `liste-de-pistes-a-repeter`.

### Exemples de la fonction CSS `repeat()`

Voici des exemples du fonctionnement de la fonction CSS `repeat()`.

#### Comment créer un conteneur de grille à trois colonnes avec des largeurs de colonne de `70px` 

```css
section {
  display: grid;
  grid-template-columns: repeat(3, 70px);
  background-color: orange;
  margin: 10px;
  padding: 7px;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-imfqcm?file=style.css)

L'extrait ci-dessus utilise la fonction CSS `repeat()` pour créer trois colonnes de `70px` de large.

Voici l'équivalent sans `repeat()` de la propriété `grid-template-columns` ci-dessus :

```css
grid-template-columns: 70px 70px 70px;
```

#### Comment créer un conteneur de grille à quatre colonnes avec une colonne de `50px` et trois colonnes de `90px` 

```css
section {
  display: grid;
  grid-template-columns: 50px repeat(3, 90px);
  background-color: orange;
  margin: 10px;
  padding: 7px;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-bgdk3a?file=style.css)

L'extrait ci-dessus utilise la fonction CSS `repeat()` pour créer trois colonnes de `90px` de large.

Voici l'équivalent sans `repeat()` de la propriété `grid-template-columns` ci-dessus :

```css
grid-template-columns: 50px 90px 90px 90px;
```

#### Comment créer un conteneur de grille à cinq colonnes avec une colonne de `40px` et deux motifs de colonnes `60px 1fr` 

```css
section {
  display: grid;
  grid-template-columns: 40px repeat(2, 60px 1fr);
  background-color: orange;
  margin: 10px;
  padding: 7px;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-wjgjym?file=style.css)

L'extrait ci-dessus utilise la fonction CSS `repeat()` pour créer deux fois le motif de colonnes `60px 1fr`.

Voici l'équivalent sans `repeat()` de la propriété `grid-template-columns` ci-dessus :

```css
grid-template-columns: 40px 60px 1fr 60px 1fr;
```

**Note :** Nous avons utilisé l'[unité `fr` (fraction)](https://codesweetly.com/css-unit#fraction-fr) pour mettre à l'échelle les troisième et cinquième colonnes par rapport à la fraction de l'espace disponible dans le conteneur de grille.

#### Comment remplir automatiquement le conteneur de grille avec des colonnes de `70px` de large

```css
section {
  display: grid;
  grid-template-columns: repeat(auto-fill, 70px);
  background-color: orange;
  margin: 10px;
  padding: 7px;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-bwdeeb?file=style.css)

L'extrait ci-dessus utilise la fonction CSS `repeat()` pour remplir automatiquement le conteneur de grille avec des colonnes de `70px` de large.

#### Comment remplir automatiquement le conteneur de grille avec des colonnes d'un minimum de `50px` et d'un maximum de `1fr` de large

```css
section {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(50px, 1fr));
  background-color: orange;
  margin: 10px;
  padding: 7px;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-hrof4i?file=style.css)

L'extrait ci-dessus utilise les fonctions CSS `repeat()` et `minmax()` pour remplir automatiquement le conteneur de grille avec des colonnes d'au moins `50px` de large et d'au plus `1fr`.

**Note :** `1fr` signifie une [unité de fraction](https://codesweetly.com/css-unit#fraction-fr).

#### Comment ajuster automatiquement le conteneur de grille avec des colonnes d'un minimum de `50px` et d'un maximum de `1fr` de large

```css
section {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(50px, 1fr));
  background-color: orange;
  margin: 10px;
  padding: 7px;
}
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-pveewm?file=style.css)

L'extrait ci-dessus utilise les fonctions `CSS repeat()` et `minmax()` pour ajuster automatiquement le conteneur de grille avec des colonnes d'un minimum de `50px` de large et d'un maximum de `1fr`.

## Aperçu

Dans cet article, nous avons discuté de tous les outils CSS Grid dont vous avez besoin pour créer des mises en page de sites web basiques et avancées de manière responsive, avec un rendu impeccable sur tous les appareils.

J'espère que vous avez trouvé cet article utile.

### Merci de m'avoir lu !

Si vous aimez ce tutoriel, vous pouvez [obtenir la version livre sur Amazon](https://amzn.to/42s5KXZ). C'est un guide de référence rapide et pratique pour CSS Grid.

[![Acheter le guide CSS Grid sur Amazon](https://www.freecodecamp.org/news/content/images/2023/03/css-grid-book-codesweetly.png align="left")](https://amzn.to/42s5KXZ)