---
title: Comment utiliser la propriété position en CSS pour aligner les éléments
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-18T14:54:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-the-position-property-in-css-to-align-elements-d8f49c403a26
coverImage: https://cdn-media-1.freecodecamp.org/images/1*fXBo56b0tanSCNHo4O2eWw.jpeg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment utiliser la propriété position en CSS pour aligner les éléments
seo_desc: 'By Cem Eygi

  Positioning elements with CSS in web development isn’t as easy as it seems. Things
  can get quickly complicated as your project gets bigger and without having a good
  understanding of how CSS deals with aligning HTML elements, you won''t be ...'
---

Par Cem Eygi

Le positionnement des éléments avec CSS dans le développement web n'est pas aussi simple qu'il y paraît. Les choses peuvent rapidement devenir compliquées à mesure que votre projet grandit et sans une bonne compréhension de la manière dont CSS gère l'alignement des éléments HTML, vous ne pourrez pas résoudre vos problèmes d'alignement.

Il existe différentes façons/méthodes pour positionner des éléments avec du CSS pur. L'utilisation des propriétés CSS **float, display** et **position** sont les méthodes les plus courantes.

Dans cet article, je vais expliquer l'une des méthodes les plus déroutantes pour aligner des éléments avec du CSS pur : la **propriété position**. J'ai également un autre tutoriel sur la [propriété CSS Display ici](https://www.youtube.com/watch?v=hgoFi0fCv3w).

Si vous préférez, vous pouvez regarder la version vidéo du tutoriel sur le positionnement CSS :

%[https://youtu.be/NYEEN4rs4T8]

Commençons...

### Propriété CSS Position et propriétés d'aide

Il existe donc 5 valeurs principales de la **propriété Position** :

`position: static | relative | absolute | fixed | sticky`

et des propriétés supplémentaires pour définir les coordonnées d'un élément (que j'appelle **propriétés d'aide**) :

`top | right | bottom | left` ET le `z-index`

> _**Note importante**_** : Les propriétés d'aide ne fonctionnent pas sans une position déclarée, ou avec **position: static.**__

#### Qu'est-ce que ce z-index ?

Nous avons la hauteur et la largeur (x, y) comme 2 dimensions. Z est la 3ème dimension. Un élément dans la page web vient devant d'autres éléments à mesure que sa valeur `z-index` augmente.

> **Z-index** ne fonctionne pas avec `position: static` ou sans une position déclarée.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Dc7075K8xmYZQAqn6BaJPg.png)
_Les éléments sont ordonnés de l'arrière vers l'avant, à mesure que leur <strong class="markup--strong markup--figure-strong" style="font-weight: 700;">z-index** augmente_

Vous pouvez regarder la vidéo sur ma chaîne pour voir comment utiliser le **z-index** plus en détail :

%[https://www.youtube.com/watch?v=vo1JBj-OAa8]

Passons maintenant aux **valeurs** de la propriété **position**...

### 1. Static

`position: static` est la **valeur par défaut**. Que nous la déclarions ou non, les éléments sont positionnés dans un ordre normal sur la page web. Donnons un exemple :

Tout d'abord, nous définissons notre structure HTML :

```html
<body>
  <div class="box-orange"></div>
  <div class="box-blue"></div>
</body>
```

Ensuite, nous créons 2 boîtes et définissons leurs largeurs, hauteurs et positions :

```css
.box-orange {          // sans aucune déclaration de position
  background: orange;
  height: 100px;
  width: 100px;       
}

.box-blue {
  background: lightskyblue;
  height: 100px;
  width: 100px; 
  position: static;   // Déclarée comme static
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*atA27-7dzI4wKkg_HfAtLw.png)
_même résultat avec & sans <strong class="markup--strong markup--figure-strong" style="font-weight: 700;"> position: static**_

Comme nous pouvons le voir sur l'image, définir **position: static** ou non ne fait aucune différence. Les boîtes sont positionnées selon le **flux normal du document**.

### 2. Relative

`position: relative` : **La nouvelle position d'un élément par rapport à sa position normale.**

En commençant par `position: relative` et pour toutes les valeurs de position **non-statiques**, nous sommes en mesure de changer la position **par défaut** d'un élément en utilisant les **propriétés d'aide** que j'ai mentionnées ci-dessus.

Déplaçons la boîte orange à côté de la boîte bleue.

```css
.box-orange {
  position: relative;  // Nous sommes maintenant prêts à déplacer l'élément
  background: orange;
  width: 100px;
  height: 100px;
  top: 100px;         // 100px du haut par rapport à sa ancienne position
  left: 100px;        // 100px de la gauche
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*noqTpZ-EBTftlKdFi48Iiw.png)
_<strong class="markup--strong markup--figure-strong" style="font-weight: 700;">La boîte orange est déplacée de 100px vers le bas et la droite, par rapport à sa position normale**_

> _NOTE : Utiliser **position: relative**_ pour un élément n'affecte pas les positions des autres éléments.

### 3. Absolute

Dans `position: relative`, l'élément est positionné **par rapport à lui-même.** Cependant, un élément positionné de manière **absolute** est **par rapport à son parent**.

Un élément avec `position: absolute` est retiré du flux normal du document. Il est positionné automatiquement au point de départ (**coin supérieur gauche)** de son élément parent. S'il n'a pas d'éléments parents, alors le document initial **<html>** sera son parent.

Puisque `position: absolute` retire l'élément du flux du document, les autres éléments **sont affectés** et se comportent comme si l'élément était complètement retiré de la page web.

Ajoutons un **conteneur** comme élément parent :

```html
<body>
  <div class="container">
    <div class="box-orange"></div>
    <div class="box-blue"></div>
  </div>
</body>
```

```css
.box-orange {
  position: absolute;
  background: orange;
  width: 100px;
  height: 100px;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*C15mDxOdtFLkXLcFaVRYBQ.png)
_<strong class="markup--strong markup--figure-strong" style="font-weight: 700;">position: absolute** déplace l'élément au <strong class="markup--strong markup--figure-strong" style="font-weight: 700;">début** de son parent_

Maintenant, il semble que la boîte bleue ait disparu, mais ce n'est pas le cas. La boîte bleue se comporte comme si la boîte orange était retirée, donc elle se déplace vers la place de la boîte orange.

Déplaçons la boîte orange de 5 pixels :

```css
.box-orange {
  position: absolute;
  background: orange;
  width: 100px;
  height: 100px;
  left: 5px;
  top: 5px;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*ss6uEQz9Bbdrdst8kNiHqQ.png)
_<strong class="markup--strong markup--figure-strong" style="font-weight: 700;">Maintenant nous pouvons voir la boîte bleue**_

Les coordonnées d'un élément positionné de manière **absolute** sont **par rapport à son parent** si le parent a également une **position non-statique.** Sinon, les propriétés d'aide positionnent l'élément par rapport au **<html> initial.**

```css
.container {
  position: relative;
  background: lightgray;
}

.box-orange {
  position: absolute;
  background: orange;
  width: 100px;
  height: 100px;
  right: 5px;    // 5px par rapport à la droite du parent
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*AEX5fn8t0MJZCo4Lx52Uaw.png)

### 4. Fixed

Comme `position: absolute`, les éléments positionnés de manière fixe sont également retirés du flux normal du document. Les différences sont :

* Ils sont **uniquement par rapport au document <html>**, et non à d'autres parents.
* Ils **ne sont pas affectés par le défilement**.

```css
.container {
  position: relative;
  background: lightgray;
}

.box-orange {
  position: fixed;
  background: orange;
  width: 100px;
  height: 100px;
  right: 5px;    // 5px par rapport à la droite du parent
}
```

Ici dans l'exemple, je change la position de la boîte orange en **fixed**, et cette fois elle est à 5px de la droite du **<html>**, et non de son **parent (container)** :

%[https://codepen.io/cem_eygi/pen/EebjaB]

Comme nous pouvons le voir, le défilement de la page n'affecte pas la boîte positionnée en **fixed**. Elle n'est plus par rapport à son parent (container).

### 5. Sticky

`position: sticky` peut être expliqué comme un mélange de `position: relative` et `position: fixed`.

Il se comporte jusqu'à un point déclaré comme `position: relative`, après quoi il change son comportement en `position: fixed`. La meilleure façon d'expliquer **position: sticky** est par un exemple :

%[https://codepen.io/cem_eygi/pen/RYjrWz]

**IMPORTANT :** Position Sticky n'est pas supporté dans Internet Explorer et les versions antérieures des autres navigateurs. **Vous pouvez vérifier la compatibilité des navigateurs sur [caniuse.com](https://caniuse.com).**

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Ekran-Resmi-2019-10-04-23.09.24.png)
_Support des navigateurs pour Position:sticky_

---

La meilleure façon de comprendre la propriété de position CSS est par la pratique. Continuez à coder jusqu'à ce que vous ayez une meilleure compréhension. Si quelque chose n'est pas clair, je répondrai à vos questions ci-dessous dans la section des commentaires.

**Si vous voulez en savoir plus sur le développement web, n'hésitez pas à** [**me suivre sur Youtube**](https://www.youtube.com/channel/UC1EgYPCvKCXFn8HlpoJwY3Q)** !**

Merci d'avoir lu !