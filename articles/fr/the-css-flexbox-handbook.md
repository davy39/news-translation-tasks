---
title: Le guide complet de CSS Flexbox – Guide complet avec des exemples pratiques
subtitle: ''
author: Benjamin Semah
co_authors: []
series: null
date: '2023-10-18T17:25:54.000Z'
originalURL: https://freecodecamp.org/news/the-css-flexbox-handbook
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/The-CSS-Flexbox-Handbook-Cover.png
tags:
- name: CSS
  slug: css
- name: flexbox
  slug: flexbox
- name: Front-end Development
  slug: front-end-development
- name: handbook
  slug: handbook
- name: responsive design
  slug: responsive-design
- name: Web Development
  slug: web-development
seo_title: Le guide complet de CSS Flexbox – Guide complet avec des exemples pratiques
seo_desc: 'Flexbox is a useful tool for creating beautiful and responsive layouts
  for web pages. In this guide, you will learn everything you need to know to start
  using CSS Flexbox like a pro. We''ll also go through loads of practice examples.

  This is a perfect...'
---

Flexbox est un outil utile pour créer des mises en page belles et réactives pour les pages web. Dans ce guide, vous apprendrez tout ce que vous devez savoir pour commencer à utiliser CSS Flexbox comme un pro. Nous passerons également en revue de nombreux exemples pratiques.

C'est une ressource parfaite pour vous si vous êtes un développeur web débutant. Cela sera également utile si vous êtes un développeur expérimenté qui souhaite rafraîchir ses compétences en conception web réactive.

## Table des matières

* [Qu'est-ce que Flexbox ?](#heading-quest-ce-que-flexbox)
    
* [Quels sont les avantages de l'utilisation de Flexbox ?](#heading-quels-sont-les-avantages-de-lutilisation-de-flexbox)
    
* [L'axe principal et l'axe transversal](#heading-laxe-principal-et-laxe-transversal)
    
* [Conteneurs Flex et Éléments Flex](#heading-conteneurs-flex-et-elements-flex)
    
* [Comprendre `Flex` et `Inline-flex`](#heading-comprendre-flex-et-inline-flex)
    
* [display: flex](#heading-display-flex)
    
* [display: inline-flex](#heading-display-inline-flex)
    
* [Les propriétés des conteneurs Flex](#heading-les-proprietes-des-conteneurs-flex)
    
* [La propriété `flex-direction`](#heading-la-propriete-flex-direction)
    
* [La propriété `flex-wrap`](#heading-la-propriete-flex-wrap)
    
* [La propriété raccourcie `flex-flow`](#heading-la-propriete-raccourcie-flex-flow)
    
* [La propriété `justify-content`](#heading-la-propriete-justify-content)
    
* [La propriété `align-items`](#heading-la-propriete-align-items)
    
* [La propriété `align-content`](#heading-la-propriete-align-content)
    
* [La propriété `place-content`](#heading-la-propriete-place-content)
    
* [Les propriétés des éléments Flex](#les-proprietes-des-elements-flex)
    
* [La propriété `order`](#heading-la-propriete-order)
    
* [La propriété `align-self`](#heading-la-propriete-align-self)
    
* [La propriété `flex-grow`](#heading-la-propriete-flex-grow)
    
* [La propriété `flex-shrink`](#heading-la-propriete-flex-shrink)
    
* [La propriété `flex-basis`](#heading-la-propriete-flex-basis)
    
* [La propriété raccourcie `flex`](#heading-la-propriete-raccourcie-flex)
    
* [Les espaces dans Flexbox](#heading-les-espaces-dans-flexbox)
    
* [Comment centrer un élément avec Flexbox](#heading-comment-centrer-un-element-avec-flexbox)
    
* [Pratique avec des jeux Flexbox](#heading-pratique-avec-des-jeux-flexbox)
    
* [Y a-t-il des bugs dans CSS Flexbox ?](#heading-y-a-t-il-des-bugs-dans-css-flexbox)
    
* [Conclusion](#heading-conclusion)
    

## Qu'est-ce que Flexbox ?

Flexbox est l'abréviation de "Flexible Box Layout". C'est un modèle de mise en page CSS qui simplifie la création de mises en page complexes. Il fournit un moyen flexible d'aligner les éléments et de distribuer l'espace au sein d'un élément conteneur.

Le modèle de mise en page Flexbox est bidirectionnel. Cela signifie que vous pouvez organiser vos éléments en lignes, en colonnes, ou les deux. Plus d'informations à ce sujet plus tard.

### Quels sont les avantages de l'utilisation de Flexbox ?

Avant Flexbox, il était difficile de créer des mises en page complexes et des pages web réactives. Vous aviez besoin d'une combinaison de propriétés CSS de flottement et de position. Cela nécessitait de nombreuses solutions de contournement et astuces.

Mais avec Flexbox, vous pouvez maintenant faire ce qui suit avec moins de difficulté et moins de lignes de code :

* Aligner et centrer les éléments en utilisant des propriétés comme `justify-content` et `align-items`.
    
* Développer des mises en page réactives sans écrire beaucoup de requêtes média.
    
* Réorganiser les éléments sans changer la structure HTML.
    
* Créer des colonnes de même hauteur sans éléments HTML supplémentaires ou images de fond.
    

Maintenant que vous savez ce qu'est Flexbox, ainsi que certaines des choses que vous pouvez faire avec, voyons comment vous pouvez l'utiliser.

### L'axe principal et l'axe transversal

La première chose que vous devez comprendre à propos de Flexbox est le concept des axes. Chaque conteneur flex (un élément avec une propriété `display` définie sur `flex` ou `inline-flex`) a un axe principal et un axe transversal.

L'axe principal est soit horizontal soit vertical selon la valeur de `flex-direction`. Ne vous inquiétez pas si vous n'êtes pas familier avec `flex-direction`. Vous allez l'apprendre.

![L'axe principal et l'axe transversal lorsque](https://www.freecodecamp.org/news/content/images/2023/08/44.-main---cross-axis.png align="left")

*L'axe transversal et l'axe principal lorsque* `flex-direction` est `row`

Dans cet exemple, l'axe principal est horizontal et l'axe transversal est vertical.

Ce qui suit est un exemple où l'axe principal est vertical et l'axe transversal est horizontal.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/45.-cross---main-axis.png align="left")

*L'axe principal et l'axe transversal lorsque* `flex-direction` est `column`

## Conteneurs Flex et Éléments Flex

Pour utiliser toutes les propriétés de Flexbox, vous devez définir la propriété `display` d'un élément sur `flex` ou `inline-flex`.

Cela transforme l'élément en un conteneur flex, et les enfants de cet élément deviennent des éléments flex.

Voici un exemple :

```html
<section class="container">  
	<div>Élément Flex 1</div>  
    <div>Élément Flex 2</div>  
    <div>    
    	<p>Ce paragraphe n'est pas un élément flex</p>  
    </div>
</section>
```

```css
.container {  
  display: flex;
}
```

L'élément `.container` est maintenant un conteneur flex. Les trois éléments div sont des enfants directs de l'élément `.container`, ce qui en fait des éléments flex.

Mais l'élément paragraphe à l'intérieur du troisième div n'est pas un élément flex. Cela est dû au fait qu'il n'est pas un enfant direct de l'élément `.container`.

## Comprendre `flex` et `inline-flex`

Vous pouvez utiliser à la fois `flex` et `inline-flex` pour faire d'un élément un conteneur flex. La différence réside dans la manière dont ils interagissent avec les éléments environnants.

### `display: flex`

Cela fait en sorte que le conteneur flex se comporte comme un élément de niveau bloc. Le conteneur flex occupe toute la largeur disponible de son élément parent. Il commence sur une nouvelle ligne, et l'élément qui le suit commence également sur une nouvelle ligne.

Exemple :

```html
<button>Bouton Un</button>

/* Conteneur Flex */
<section class="container">  
	<div id="red"></div>  
	<div id="gold"></div>  
	<div id="green"></div>
</section>

<button>Bouton Deux</button>
```

```css
.container {
	display: flex;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/46.-display-flex.png align="left")

*Les conteneurs flex se comportent comme des éléments de bloc lorsque vous utilisez* `display: flex`

L'élément `.container` occupe toute la largeur disponible du body (son élément parent).

### `display: inline-flex`

Cela fait en sorte que le conteneur flex se comporte comme un élément de niveau en ligne. Cela permet à d'autres éléments en ligne (comme les boutons) de s'écouler à côté. En utilisant l'exemple précédent, voici comment les éléments seront disposés lorsque vous changez `display` de `flex` à `inline-flex`.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/47.-display-inline-flex.png align="left")

*Les conteneurs flex se comportent comme des* `inline-elements` lorsque vous utilisez `display: inline-flex`

Le conteneur flex n'occupe pas toute la largeur de son parent. Il utilise seulement autant d'espace horizontal que nécessaire pour son contenu.

[**Pratiquez l'utilisation de flex et inline-flex**](https://stackblitz.com/edit/js-ug2zkz?file=style.css) **sur StackBlitz**

## Les propriétés des conteneurs Flex

Les propriétés des conteneurs flex vous permettent de contrôler la mise en page et l'alignement des éléments flex au sein d'un conteneur flex.

**NOTE :** Vous appliquez ces propriétés sur le conteneur flex, et non sur ses éléments.

Les propriétés des conteneurs flex sont les suivantes :

* `flex-direction`
    
* `flex-wrap`
    
* `flex-flow`
    
* `justify-content`
    
* `align-items`
    
* `align-content`
    
* `place-content`
    

### La propriété `flex-direction`

La propriété `flex-direction` définit la direction pour afficher les éléments flex. C'est ce qui définit l'axe principal du conteneur flex. Cette propriété peut prendre l'une des quatre valeurs suivantes :

* `row` (valeur par défaut)
    
* `column`
    
* `row-reverse`
    
* `column-reverse`
    

Maintenant, regardons quelques exemples pour voir comment tout cela fonctionne.

Dans l'extrait de code suivant, nous avons un `names-container` avec quatre noms :

```html
<div class="names-container">  
	<p id="jill">1. JILL</p>  
	<p id="john">2. JOHN</p>  
	<p id="jane">3. JANE</p>  
	<p id="jack">4. JACK</p>
</div>
```

Voyons les différentes façons dont vous pouvez organiser les noms en utilisant la propriété `flex-direction`.

#### `flex-direction: row`

Cela affiche les éléments flex horizontalement de gauche à droite.

```css
.names-container {  
	display: flex;  
    flex-direction: row;  
    /* Autres styles ici... */
}
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/1.-flex-direction-row.png align="left")

*Exemple de* `flex-direction: row`

#### `flex-direction: column`

Cela affiche les éléments flex verticalement de haut en bas.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/2.-flex-direction-column.png align="left")

*Exemple de* `flex-direction: column`

#### `flex-direction: row-reverse`

Cela est l'inverse de la valeur row. Il affiche les éléments flex de droite à gauche.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/3.-flex-direction-row-reverse.png align="left")

*Exemple de* `flex-direction: row-reverse`

#### `flex-direction: column-reverse`

Cela est l'inverse de la valeur column. Il affiche les éléments flex de bas en haut.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/4.-flex-direction-column-reverse.png align="left")

*Exemple de* `flex-direction: column-reverse`

[**Pratiquez l'utilisation de flex-direction**](https://stackblitz.com/edit/js-aaerav?file=style.css) **sur StackBlitz**

#### Une note sur les valeurs reverse et l'accessibilité :

Il y a quelque chose que vous devez garder à l'esprit lorsque vous utilisez `row-reverse` et `column-reverse`. Comme vous l'avez déjà vu, les deux affectent l'ordre visuel des éléments à l'écran.

Mais l'ordre dans votre HTML reste inchangé. Et c'est l'ordre que les lecteurs d'écran et les contrôles de navigation au clavier utilisent.

Dans l'exemple, lorsque vous utilisez `row-reverse`, vous voyez le nom de Jack en premier à l'écran, suivi de Jane, John et Jill.

Mais pour quelqu'un utilisant un lecteur d'écran, il entendra les noms tels qu'ils apparaissent dans le HTML et non tels qu'ils apparaissent à l'écran. Dans ce cas, il entendra d'abord le nom de Jill, suivi de John, Jane et Jack.

### La propriété `flex-wrap`

Parfois, l'espace au sein du conteneur flex ne sera pas suffisant pour les éléments flex.

Dans de tels cas, vous utilisez la propriété `flex-wrap` pour choisir si vous laissez les éléments flex déborder ou commencer sur une nouvelle ligne.

La propriété `flex-wrap` accepte l'une des valeurs suivantes :

* `nowrap` (valeur par défaut)
    
* `wrap`
    
* `wrap-reverse`
    

Pour voir `flex-wrap` en action, ajoutons quatre autres noms à notre `names-container` :

```html
<div class="names-container">  
	<p id="jill">1. JILL</p>  
	<p id="john">2. JOHN</p>  
	<p id="jane">3. JANE</p>  
	<p id="jack">4. JACK</p>  
	<p id="sara">5. SARA</p>  
	<p id="seth">6. SETH</p>  
	<p id="seal">7. SEAL</p>
</div>
```

#### `flex-wrap: nowrap`

Cela garde tous les éléments flex sur une seule ligne soit en ligne soit en colonne. Il permet aux éléments flex de déborder s'il n'y a pas assez de place dans le conteneur flex. Voir l'exemple ci-dessous :

```css
.names-container {  
	display: flex;  
	flex-direction: row;  
	flex-wrap: nowrap;  
	/* Autres styles ici... */
}
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/5.-flex-wrap-nowrap.png align="left")

*Les éléments flex débordent car* `flex-wrap` est défini sur `nowrap`

Dans cet exemple, trois noms débordent du conteneur car il n'y a pas assez d'espace pour eux.

#### `flex-wrap: wrap`

Cela enveloppera ou poussera les éléments flex à la ligne suivante s'il n'y a pas assez de place pour eux.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/6.-flex-wrap-wrap.png align="left")

*Les éléments flex s'enroulent ou se déplacent à la ligne suivante lorsque* `flex-wrap` est défini sur `wrap`

#### `flex-wrap: wrap-reverse`

Cela est l'inverse de `wrap`. Il déplace les éléments en débordement à la ligne suivante mais dans une direction inverse.

Par exemple, utiliser `wrap-reverse` sur le conteneur de noms déplace les éléments en débordement à la ligne supérieure suivante au lieu de la ligne suivante en dessous.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/7.-flex-wrap-wrap-reverse.png align="left")

*Exemple de* `flex-wrap: wrap-reverse`

[**Pratiquez l'utilisation de flex-wrap**](https://stackblitz.com/edit/js-cbmfgr?file=style.css) **sur StackBlitz.**

### La propriété raccourcie `flex-flow`

La propriété `flex-flow` est un raccourci pour les propriétés `flex-direction` et `flex-wrap`. Cela signifie que lorsque vous utilisez `flex-flow`, vous pouvez appliquer les deux propriétés avec une seule ligne de code.

Voir l'exemple ci-dessous en utilisant le conteneur de noms. Vous pouvez donner au conteneur les propriétés `flex-direction` et `flex-wrap`.

```css
.names-container {  
	display: flex;  
	flex-direction: column;  
    flex-wrap: wrap;
}
```

Ou vous pouvez utiliser le raccourci `flex-flow` pour obtenir le même résultat.

```css
.names-container {  
	display: flex;  
	flex-flow: column wrap;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/8.-flex-flow.png align="left")

*Exemple de* `flex-flow: column wrap`

[**Pratiquez l'utilisation de flex-flow**](https://stackblitz.com/edit/js-xuv4bx?file=style.css) **sur StackBlitz.**

### La propriété `justify-content`

Cette propriété `justify-content` gère l'alignement des éléments flex sur l'axe principal du conteneur flex.

Vous pouvez l'utiliser pour gérer la distribution de l'espace sur l'axe principal. Cette propriété prend l'une des valeurs suivantes :

* `flex-start` (valeur par défaut)
    
* `flex-end`
    
* `center`
    
* `space-between`
    
* `space-around`
    
* `space-evenly`
    

#### `justify-content: flex-start`

Cela place les éléments au début de la direction flex. Si l'axe principal est horizontal avec une `flex-direction` de `row` (comme dans l'exemple ci-dessous), il aligne les éléments à gauche. Et s'il est vertical (avec une `flex-direction` de `column`), il aligne les éléments en haut.

En utilisant l'exemple du conteneur de noms, voici à quoi ressemblerait `justify-content: flex-start` :

```css
.names-container {  
	display: flex;  
	justify-content: flex-start;  
	/* Autres styles ici... */
}
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/9.-justify-content-flex-start.png align="left")

*Exemple de* `justify-content: flex-start`

#### `justify-content: flex-end`

Cela placera les éléments flex à la fin de la direction flex de l'axe principal.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/10.-justify-content-flex-end.png align="left")

*Exemple de* `justify-content: flex-end`

#### `justify-content: center`

Cela place les éléments flex au centre de l'axe principal du conteneur flex.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/11.-justify-content-center-.png align="left")

*Exemple de* `justify-content: center`

#### `justify-content: space-between`

Cela placera le premier élément flex au début de l'axe principal. Et placera également le dernier élément à la fin de l'axe principal. Ensuite, l'espace sur l'axe principal est distribué également entre les éléments.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/12.-justify-content-space-between.png align="left")

*Exemple de* `justify-content: space-between`

#### `justify-content: space-evenly`

Cela distribue l'espace également entre les éléments flex. Cela signifie que l'espace avant et après chaque élément est le même.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/13.-justify-content-space-evenly.png align="left")

*Exemple de* `justify-content: space-evenly`

#### `justify-content: space-around`

Cela distribue également l'espace entre les éléments flex. La différence clé ici est que l'espace avant le premier élément et après le dernier élément est la moitié de l'espace entre les éléments flex.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/14.-justify-content-space-around.png align="left")

*Exemple de* `justify-content: space-around`

[**Pratiquez l'utilisation de justify-content**](https://stackblitz.com/edit/js-zpcbxv?file=style.css) **sur StackBlitz.**

### La propriété `align-items`

La propriété `align-items` gère l'alignement des éléments flex sur l'axe transversal du conteneur flex. Elle peut prendre l'une des valeurs suivantes :

* `stretch` (valeur par défaut)
    
* `flex-start`
    
* `flex-end`
    
* `center`
    
* `baseline`
    

#### `align-items: stretch`

Cela étire les éléments flex pour remplir l'espace au sein du conteneur flex.

Voir l'exemple ci-dessous en utilisant un nouveau conteneur de noms avec des cartes de noms de différentes tailles :

```css
.names-container {  
	display: flex;  
    align-items: stretch;  
    /* Autres styles ici... */
}
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/15.-align-items-stretch.png align="left")

*Exemple de* `align-items: stretch`

#### `align-items: flex-start`

Cela placera les éléments flex au début de l'axe transversal du conteneur flex. Si l'axe transversal est vertical comme dans l'exemple ci-dessous, `align-items: flex-start` placera les éléments en haut.

```css
.names-container {  
	display: flex;  
	align-items: flex-start;  
	/* Autres styles ici... */
}
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/16.-align-items-flex-start.png align="left")

*Exemple de* `align-items: flex-start`

#### `align-items: flex-end`

Cela placera les éléments flex à la fin de l'axe transversal du conteneur flex. Si l'axe transversal est vertical comme dans l'exemple ci-dessous, `align-items: flex-end` placera les éléments en bas.

```css
.names-container {  
	display: flex;  
    align-items: flex-end;  
    /* Autres styles ici... */
}
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/17.-align-items-flex-end.png align="left")

*Exemple de* `align-items: flex-end`

#### `align-items: center`

Cela aligne les éléments flex au centre de l'axe transversal du conteneur flex.

```css
.names-container {  
	display: flex;  
	align-items: center;  
	/* Autres styles ici... */
}
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/18.-align-items-center.png align="left")

*Exemple de* `align-items: center`

#### `align-items: baseline`

Lorsque vous utilisez la valeur `baseline`, les éléments flex sont disposés de sorte que leurs lignes de base soient alignées. Voir l'exemple ci-dessous :

```css
.names-container {  
	display: flex;  
	align-items: baseline;  
	/* Autres styles ici... */
}
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Untitled-design-1.png align="left")

*La ligne de base est indiquée par la ligne pointillée blanche*

[**Pratiquez l'utilisation de align-items**](https://stackblitz.com/edit/js-jydywf?file=style.css) **sur StackBlitz.**

### La propriété `align-content`

Lorsque vous avez un conteneur flex avec wrap (ou plus d'une ligne flex), vous pouvez avoir besoin d'aligner les lignes pour distribuer l'espace comme vous le souhaitez. C'est alors que vous utilisez `align-content`. Cette propriété peut prendre l'une des valeurs suivantes :

* `stretch` (valeur par défaut)
    
* `flex-start`
    
* `flex-end`
    
* `center`
    
* `space-between`
    
* `space-evenly`
    
* `space-around`
    

Dans l'exemple ci-dessous, il y a 11 noms dans le conteneur de noms. Et l'élément conteneur de noms a une valeur `flex-wrap` de `wrap`. Cela signifie que vous pouvez appliquer la propriété `align-content` pour changer l'alignement des lignes flex.

#### `align-content: stretch`

Cela étire les lignes flex pour remplir l'espace au sein de l'axe transversal du conteneur flex.

```css
.names-container {  
	display: flex;  
	flex-wrap: wrap;  
	align-items: stretch;  
	/* Autres styles ici... */
}
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/20.-align-content-stretch.png align="left")

*Exemple de* `align-content: stretch`

#### `align-content: flex-start`

Cela place les lignes flex au début de l'axe transversal du conteneur. Par exemple, si l'axe transversal est vertical comme celui du conteneur de noms, il placera les lignes flex en haut.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/21.-align-content-flex-start.png align="left")

*Exemple de* `align-content: flex-start`

#### `align-content: flex-end`

Cela place les lignes flex à la fin de l'axe transversal du conteneur.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/22.-align-content-flex-end.png align="left")

*Exemple de* `align-content: flex-end`

#### `align-content: center`

Cela place les lignes flex au centre de l'axe transversal du conteneur.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/23.-align-content-center.png align="left")

*Exemple de* `align-content: center`

#### `align-content: space-between`

Cela placera la première ligne flex au début de l'axe transversal. Il placera également la dernière ligne flex à la fin de l'axe transversal. Ensuite, l'espace sur l'axe transversal est distribué également entre les lignes.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/24.-align-content-space-between.png align="left")

*Exemple de* `align-content: space-between`

#### `align-content: space-evenly`

Cela distribue l'espace également entre les lignes flex. Cela signifie que l'espace avant et après chaque ligne est le même.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/25.-align-content-space-evenly.png align="left")

*Exemple de* `align-content: space-evenly`

#### `align-content: space-around`

Cela distribue également l'espace entre les lignes flex. La différence clé ici est que l'espace avant la première ligne et après la dernière ligne est la moitié de l'espace entre les lignes flex.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/26.-align-content-space-around.png align="left")

*Exemple de* `align-content: space-around`

[**Pratiquez l'utilisation de align-content**](https://stackblitz.com/edit/js-fukvgd?file=style.css) **sur StackBlitz.**

### La propriété `place-content`

Si vous devez utiliser à la fois les propriétés `justify-content` et `align-content`, vous utilisez la propriété raccourcie `place-content`.

Elle peut prendre une ou deux valeurs. Lorsque vous lui donnez une seule valeur, le navigateur appliquera la même valeur pour `justify-content` et `align-content`.

Et lorsque vous donnez 2 valeurs pour `place-content`, la première valeur sera pour `align-content` et la seconde pour `justify-content`.

Regardons un exemple :

Au lieu d'écrire ceci :

```css
.names-container {  
	display: flex;  
	flex-wrap: wrap;  
	align-content: flex-end;  
	justify-content: flex-start;  
	/* Autres contenus */
}
```

Vous pouvez plutôt écrire ce qui suit et cela aura le même effet :

```css
.names-container {  
	display: flex;  
	flex-wrap: wrap;  
	place-content: flex-end flex-start;  
	/* Autres contenus */
}
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/43.-place-content.png align="left")

*Exemple d'utilisation du raccourci* `place-content`

[**Pratiquez l'utilisation de place-content**](https://stackblitz.com/edit/js-ytdywl?file=style.css) **sur StackBlitz.**

## Les propriétés des éléments Flex

Chaque enfant direct d'un conteneur flex est un élément flex. Jusqu'à présent, vous avez appris les propriétés des conteneurs flex.

Flexbox possède également des propriétés que vous pouvez appliquer à des éléments flex individuels. Elles incluent les suivantes :

* `order`
    
* `align-self`
    
* `flex-grow`
    
* `flex-shrink`
    
* `flex-basis`
    
* `flex`
    

### La propriété `order`

La propriété `order` détermine l'ordre d'apparition des éléments flex.

La valeur que vous donnez à cette propriété doit être un nombre. Un élément flex avec un nombre inférieur apparaîtra avant un élément avec un nombre supérieur.

Dans le code HTML, l'ordre des quatre noms est le suivant :

1. Jill
    
2. John
    
3. Jane
    
4. Jack
    

```css
<div class="names-container">
	<p id="jill">1. JILL</p>
	<p id="john">2. JOHN</p>
	<p id="jane">3. JANE</p>
	<p id="jack">4. JACK</p>
</div>
```

Vous pouvez changer l'ordre d'apparition à l'écran en utilisant la propriété `order`. Voir l'exemple ci-dessous.

Voici comment ils apparaissent sans propriétés `order` :

![Image](https://www.freecodecamp.org/news/content/images/2023/08/27.-no-order-property.png align="left")

*Cartes de noms avant l'ajout de la propriété* `order`

Maintenant, voyez comment ils apparaissent lorsque vous ajoutez les propriétés d'ordre suivantes :

```css
.names-container {  
	display: flex;
}

#jill {  
	order: 2;  
    background-color: #fe4f46;
}

#john {  
	order: 4;  
    background-color: #fcd65c;
}

#jane {  
	order: 1;  
    background-color: 
    #00bab4;
}

#jack {  
	order: 3;  
    background-color: #003f54;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/28.-with-order-property.png align="left")

*La propriété* `order` change l'ordre d'apparition

[**Pratiquez l'utilisation de la propriété order**](https://stackblitz.com/edit/js-c5mf8q?file=style.css) **sur StackBlitz.**

**Mise en garde :** Même si l'ordre d'apparition change à l'écran, l'ordre dans le HTML reste inchangé. Et c'est l'ordre dans le HTML que les lecteurs d'écran utilisent. Dans la mesure du possible, il est préférable de changer l'ordre dans le HTML plutôt que de le faire avec Flexbox.

### La propriété `align-self`

Vous pouvez utiliser la propriété `align-self` pour donner à un élément flex un alignement différent des autres éléments.

Elle fonctionne de la même manière que la propriété `align-items`. La différence est que tandis que `align-items` s'applique à tous les éléments flex, la propriété `align-self` est appliquée uniquement à des éléments spécifiques.

Exemple :

```css
.names-container {  
	display: flex;  
    align-items: center;  
    /* Autres styles */    
}

#jill {
	align-self: flex-start;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/37.-align-self.png align="left")

*Exemple de* `align-self` avec une valeur `flex-start`

Dans l'exemple, la propriété `align-items` pour le conteneur de noms a une valeur de `center`. Cela aligne tous les noms au centre.

Mais en utilisant la propriété `align-self`, vous êtes en mesure d'aligner la carte de nom de Jill en haut avec une valeur de `flex-start`.

[**Pratiquez l'utilisation de la propriété align-self**](https://stackblitz.com/edit/js-e9ctpu?file=style.css) **sur StackBlitz.**

### La propriété `flex-grow`

Lorsque vous définissez l'affichage d'un conteneur sur `flex`, il y a souvent un espace supplémentaire après que les éléments soient disposés. Voir l'exemple ci-dessous :

```css
.names-container {  
	display: flex;  
    justify-content: 
    flex-start;  
 	/* Autres styles */
 }
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/29.-flex-grow-extra-space.png align="left")

*Le conteneur flex a plus qu'assez d'espace pour les éléments flex*

Le navigateur traite l'espace supplémentaire comme une valeur de `1`. Cela signifie que lorsque vous donnez une valeur `flex-grow` de `0.5` à seulement l'un des éléments flex, le navigateur ajoutera la moitié de l'espace restant à la taille de l'élément.

```css
#jill {
	flex-grow: 0.5;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/30.-flex-grow-0.5.png align="left")

*La propriété* `flex-grow` rend la carte de Jill plus grande que sa taille initiale

Et si vous ajoutez une valeur `flex-grow` de `1` à **un seul des éléments flex**, le navigateur ajoutera tout l'espace supplémentaire à cet élément.

**NOTE :** Si un seul élément dans le conteneur a une valeur `flex-grow`, alors toute valeur de 1 ou plus le fera occuper tout l'espace supplémentaire.

Par exemple, les deux extraits de code ci-dessous auront le même effet sur la carte de Jill :

```css
#jill {  
	flex-grow: 1;
}
```

```css
#jill {  
	flex-grow: 99;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/31.-flex-grow-1-or-more.png align="left")

*Lorsque seule une carte a un* `flex-grow` de `1` ou plus

Que se passe-t-il lorsque vous ajoutez des valeurs `flex-grow` à plus d'un élément ?

Le navigateur partagera l'espace supplémentaire proportionnellement entre eux.

Par exemple, lorsque vous donnez à Jane un `flex-grow` de `3` et à Jack un `flex-grow` de `1`, le navigateur partagera l'espace supplémentaire avec un ratio de `3:1`.

Cela signifie que la valeur totale de l'espace supplémentaire devient `4` (3+1). `Jane` obtiendra alors `3/4` de l'espace supplémentaire. Et `Jack` obtiendra `1/4` de celui-ci.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/32.-flex-grow-jane-jack.png align="left")

*L'espace supplémentaire est partagé proportionnellement entre* `Jane` et `Jack`

[**Pratiquez l'utilisation de la propriété flex-grow**](https://stackblitz.com/edit/js-m6h8af?file=style.css) **sur StackBlitz.**

### La propriété `flex-shrink`

La propriété `flex-shrink` est l'inverse de `flex-grow`.

Vous utilisez `flex-grow` lorsque vous souhaitez augmenter la taille de l'élément flex s'il y a de l'espace supplémentaire. Mais vous utilisez `flex-shrink` lorsque vous souhaitez diminuer la taille de l'élément flex s'il n'y a pas assez d'espace dans le conteneur flex.

Voir l'exemple ci-dessous :

```html
<div class="numbers-container">
	<p id="one">1</p>
	<p id="two">2</p>
	<p id="three">3</p>
	<p id="four">4</p>
</div>
```

```css
.numbers-container {  
	display: flex;  
	justify-content: flex-start;  
	/* Autres styles */
}

#one {  
	flex-shrink: 2;  
	background-color: #fe4f46;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/33.-flex-shrink-value-2.png align="left")

*La première carte se rétrécit pour faire de la place aux autres*

Dans l'exemple, chacun des quatre nombres a une largeur de 150px (ce qui fait un total de 600px). Mais le `numbers-container` a une largeur de 400px, ce qui n'est pas suffisant.

Les cartes doivent se rétrécir pour s'adapter à l'espace disponible. Mais le nombre `1`, avec une valeur `flex-shrink` de 2, se rétrécit pour devenir deux fois plus petit que les autres nombres.

#### Que faire si vous ne voulez pas qu'un élément flex se rétrécisse ?

Pour empêcher un élément flex de se rétrécir, donnez-lui une valeur `flex-shrink` de `0`.

Par exemple, lorsque vous donnez au nombre `1` un `flex-shrink` de `0`, il maintiendra la largeur de 150px. Et les autres éléments flex se rétréciront pour s'adapter à l'espace restant.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/34.-flex-shrink-vallue-0.png align="left")

*La première carte ne se rétrécit pas car elle a une valeur* `flex-shrink` de `0`

[**Pratiquez l'utilisation de la propriété flex-shrink**](https://stackblitz.com/edit/js-q9zndc?file=style.css) **sur StackBlitz.**

### La propriété `flex-basis`

Vous pouvez utiliser la propriété `flex-basis` pour définir la longueur par défaut d'un élément flex spécifique. Il s'agit soit de la largeur soit de la hauteur de l'élément selon la `flex-direction`.

Si la `flex-direction` est `row` ou `row-reverse`, la valeur de `flex-basis` devient la largeur initiale de l'élément.

Et si la `flex-direction` est `column` ou `column-reverse`, alors la valeur de `flex-basis` devient la hauteur initiale de l'élément.

Exemple :

```css
.names-container {  
	display: flex;  
	flex-direction: column;  
	/* Autres styles */
}

div {  
	height: 20px;
}

#jane {  
	flex-basis: 60px;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/35.-flex-basis-height.png align="left")

*Exemple de* `flex-basis` définissant la hauteur d'un élément

Dans l'exemple, la hauteur des divs est définie à 20px. Mais Jane obtient une valeur `flex-basis` de 60px. Et cela remplace les 20px donnés à toutes les divs.

**Note :** Le flex-basis de 60px devient la hauteur pour Jane car la `flex direction` est `column`. Cela signifie que l'axe principal est vertical.

Voici un autre exemple. Cette fois, la `flex-direction` est `row`. Cela signifie que le `flex-basis` définira la largeur de l'élément.

```css
.names-container {  
	display: flex;  
	flex-direction: row;  
    /* Autres styles */
}

div {  
	width: 70px;
}

#jane {  
	flex-basis: 140px;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/36.-flex-basis-width.png align="left")

*Exemple de* `flex-basis` définissant la largeur d'un élément

Alors que toutes les autres divs ont une largeur de 70px, Jane a une largeur de 140px définie par le `flex-basis`.

[**Pratiquez l'utilisation de la propriété flex-basis**](https://stackblitz.com/edit/js-maihzd?file=style.css) **sur StackBlitz.**

### La propriété raccourcie `flex`

Vous pouvez utiliser `flex` comme raccourci pour les propriétés `flex-grow`, `flex-shrink` et `flex-basis`.

Par exemple, au lieu d'écrire ce qui suit :

```css
.flex-item {  
	flex-grow: 2;  
	flex-shrink: 0;  
	flex-basis: 50px;
}
```

Vous pouvez utiliser le raccourci comme suit et cela aura le même effet :

```css
.flex-item {  
	flex: 2 0 50px;
}
```

La propriété `flex` peut prendre jusqu'à trois valeurs. L'ordre des valeurs est important. Le navigateur attribue la première valeur à `flex-grow`, la seconde à `flex-shrink` et la troisième à `flex-basis`.

Les valeurs par défaut pour `flex` sont `1 0 auto`.

Cela signifie que si vous donnez à `flex` une seule valeur de 2, le navigateur utilise 2 pour `flex-grow`. Ensuite, il définit `flex-shrink` à 0 et `flex-basis` à auto.

[**Pratiquez l'utilisation de la propriété** `flex`](https://stackblitz.com/edit/js-m19hov?file=style.css) **sur StackBlitz.**

## Comment centrer un élément avec Flexbox

L'un des casse-têtes pour de nombreux développeurs front-end est le centrage des éléments. Flexbox a une solution parfaite pour cela.

Il y a deux étapes impliquées.

1. Faites de l'élément parent un conteneur flex en définissant `display` sur `flex`.
    
2. Donnez une valeur de `center` à la fois à `justify-content` et `align-items`.
    

C'est tout ! Votre élément sera parfaitement centré.

Exemple :

```html
<div class="name-container">  
	<p>JOHN</p>
</div>
```

```css
.name-container {  
	display: flex;  
	justify-content: center;  
	align-items: center;  
	/* Autres Styles */
}
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/38.-center-element-w--flexbox.png align="left")

*Exemple de centrage d'un élément avec Flexbox*

Que vous essayiez de centrer du texte, des images, ou même une barre de navigation entière, cela fonctionnera très bien.

## Les espaces dans Flexbox

Vous pouvez utiliser la propriété `gap` pour ajuster l'espace entre les éléments flex.

**NOTE :** Vous appliquez la propriété gap sur le conteneur flex et non sur les éléments flex.

`gap` peut prendre deux valeurs : la première valeur pour les espaces entre les lignes et la seconde valeur pour les espaces entre les colonnes.

Exemple :

```css
.names-container {  
	display: flex;  
	flex-wrap: wrap;  
	gap: 50px 10px; 
	/* row-gap column-gap */
}
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/39.-gap-two-values.png align="left")

*Exemple de donner deux valeurs pour la propriété gap*

Si l'espace que vous souhaitez entre les lignes et les colonnes est le même, vous pouvez utiliser une seule valeur. Le navigateur appliquera la même valeur aux lignes et aux colonnes.

Exemple :

```css
.names-container {  
	display: flex;  
	flex-wrap: wrap;  
	gap: 10px; 
	/* Autres Styles */
}
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/40.-gap-single-value.png align="left")

*Exemple d'utilisation d'une seule valeur pour les espaces entre les lignes et les colonnes*

Vous pouvez également utiliser les propriétés `row-gap` si vous devez appliquer une valeur d'espace spécifique entre les lignes uniquement. et `column-gap` si vous devez ajouter des espaces entre les colonnes uniquement.

Exemple : Ajout d'espaces entre les lignes uniquement :

```css
.names-container {  
	display: flex;  
	flex-wrap: wrap;  
	row-gap: 20px; 
	/* Autres Styles */
}
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/41.-row-gap.png align="left")

*Exemple d'utilisation de* `row-gap`

Exemple : Ajout d'espaces entre les colonnes uniquement :

```css
.names-container {  
	display: flex;  
	flex-wrap: wrap;  
	column-gap: 20px; 
	/* Autres Styles */
}
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/42.-column-gap.png align="left")

*Exemple d'utilisation de* `column-gap`

[**Pratiquez l'utilisation de la propriété gap**](https://stackblitz.com/edit/js-v77toh?file=style.css) **sur StackBlitz.**

## Pratique avec des jeux Flexbox

Vous voulez pratiquer Flexbox de manière interactive ? Consultez les jeux suivants. Ils offrent une expérience pratique pour pratiquer Flexbox de manière amusante et engageante.

* [Flexbox Froggy](https://flexboxfroggy.com/)
    
* [Flexbox Defense](http://www.flexboxdefense.com/)
    
* [Flexbox Zombies](https://mastery.games/flexboxzombies/)
    

## Y a-t-il des bugs dans CSS Flexbox ?

Bien que CSS Flexbox soit un outil de mise en page puissant, il présente quelques bugs qui peuvent vous surprendre.

Un exemple courant est que **certains éléments HTML ne peuvent pas agir comme des conteneurs flex**. Cela inclut les éléments `<button>`, `<fieldset>`, et `<summary>`.

La solution de contournement consiste à utiliser un élément comme un `div` pour envelopper les enfants de l'élément. Ensuite, utilisez Flexbox sur le `div` enveloppant.

Si vous êtes curieux de connaître d'autres bugs et solutions de contournement de Flexbox, vous pouvez consulter [le dépôt Flexbugs](https://github.com/philipwalton/flexbugs) sur GitHub.

## Conclusion

Dans ce guide, vous avez appris toutes les propriétés de Flexbox, leurs valeurs et comment les utiliser pour créer des mises en page réactives. Vous avez également appris quelques jeux comme Flexbox Froggy que vous pouvez utiliser pour vous entraîner.

Merci d'avoir lu, et bon codage ! Pour des tutoriels plus approfondis, n'hésitez pas à [vous abonner à ma chaîne YouTube](https://www.youtube.com/@DevAfterHours).