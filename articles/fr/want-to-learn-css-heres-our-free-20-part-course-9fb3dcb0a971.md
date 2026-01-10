---
title: Apprendre le CSS en UNE heure - Cours interactif gratuit en 20 parties
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-07T06:48:38.000Z'
originalURL: https://freecodecamp.org/news/want-to-learn-css-heres-our-free-20-part-course-9fb3dcb0a971
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9cade3740569d1a4caa298.jpg
tags:
- name: CSS
  slug: css
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Design
  slug: web-design
seo_title: Apprendre le CSS en UNE heure - Cours interactif gratuit en 20 parties
seo_desc: 'By Per Harald Borgen


  _Click here to get to the course._

  CSS (Cascading Style Sheet) is one of the three cornerstones of the web, along with
  HTML and JavaScript. It’s what brings life to websites through colours, styling,
  positioning and much more. T...'
---

Par Per Harald Borgen

![Image](https://cdn-media-1.freecodecamp.org/images/2JzvFPRiXR-0mdeHA9QVJAopOF577dOvFazI)
_[Cliquez ici pour accéder au cours.](https://scrimba.com/g/gintrotocss?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gintrotocss_1_hour_article)_

CSS (Cascading Style Sheet) est l'un des trois piliers du web, avec HTML et JavaScript. C'est ce qui donne vie aux sites web grâce aux couleurs, au style, au positionnement et bien plus encore. Ainsi, connaître le CSS est extrêmement précieux sur le marché du travail actuel !

Je suis donc heureux d'annoncer que nous venons de [lancer un cours gratuit sur le CSS sur Scrimba.](https://scrimba.com/g/gintrotocss?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gintrotocss_1_hour_article) Il a été créé par notre brillant instructeur [Eric Tirado](https://medium.com/u/3b3bb1053d15), qui a également réalisé notre populaire [cours d'introduction à HTML.](https://scrimba.com/g/ghtml?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gintrotocss_1_hour_article)

En moins d'une heure, Eric vous fera passer de zéro à compétent en CSS !

Examinons comment [le cours](https://scrimba.com/g/gintrotocss?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gintrotocss_1_hour_article) est structuré.

### Partie #1 : Introduction

Dans la vidéo d'introduction, Eric vous donnera un aperçu de ce à quoi ressemble le cours, quels sont les prérequis, ainsi qu'un aperçu des sujets qu'il aborde tout au long du cours. Il se présente également brièvement pour que vous vous familiarisiez avec lui avant de commencer.

### Partie #2 : Documents CSS et la Cascade

Nous passons ensuite directement à la première leçon formelle du cours. Dans celle-ci, nous examinerons les différentes façons d'inclure du CSS dans nos pages HTML et comment commencer à appliquer des styles de base à nos éléments.

![Image](https://cdn-media-1.freecodecamp.org/images/1*iMZI_APohllftaOWzZF26w.png)

### Partie #3 : Sélecteurs, Propriétés et Valeurs CSS

Dans la deuxième leçon, Eric parle de certains termes du vocabulaire CSS qui vous préparent à mieux comprendre les concepts qu'il aborde dans les leçons ultérieures. Vous apprendrez ce que sont les éléments HTML, ce que sont les sélecteurs CSS, et comment vous pouvez appliquer des propriétés et leur assigner des valeurs.

# Vocabulaire CSS

Par exemple, ceci est un élément `h1`. Il a un style par défaut qui apparaît lorsque vous le rendez dans le navigateur. Si nous voulons changer certains styles, nous pouvons utiliser le CSS :

```css
h1 {  
   color: 'red';  
}

```

Le sélecteur pour notre élément `h1` est simplement le nom de l'élément lui-même, et nous lui assignons la propriété de couleur avec la valeur rouge. De la même manière, nous pouvons sélectionner des éléments en utilisant des Classes et des IDs, ce qui est discuté dans les vidéos suivantes.

### Partie #4 : Classes et IDs

Cette partie du cours explique comment utiliser les classes et les IDs en CSS pour sélectionner des éléments HTML et appliquer différents styles. Elle explique également en détail la différence entre une Classe et un ID, et comment et quand nous les assignons aux éléments HTML.

Regardez le code suivant pour un exemple :

```html
<h1 class='heading'>Ceci est la balise d'en-tête</h1>

<p class='paragraph'>Ceci est une balise de paragraphe</p>

```

L'extrait ci-dessus se compose d'un `h1` (en-tête) et d'une balise `p` (paragraphe). Nous avons donné à l'élément `h1` la classe `heading` et à notre élément `p` l'ID `paragraph`.

Dans notre fichier CSS, nous sélectionnons la classe heading et lui donnons la propriété de couleur. Plus tard, nous sélectionnons l'ID paragraph et lui donnons les propriétés de couleur et de taille de police :

```css
.heading {  
   color: blue  
}

#paragraph {  
   color: green;  
   font-size: 14px;  
}

```

### Partie #5 : Spécificité

Dans la partie 5 du cours, vous apprendrez la spécificité, c'est-à-dire comment un navigateur sait quels styles et règles sont les plus pertinents pour un élément à appliquer.

```html
<h1 class='heading'>Ceci est la balise d'en-tête</h1>

```

Par exemple, ici nous avons une balise `h1` avec la classe heading appliquée.

```css
h1 {  
   color: blue;  
}

.heading {  
   color: green;  
}

```

En utilisant CSS, nous assignons la couleur bleue à la balise `h1`, ce qui changera la couleur de chaque `h1`. Nous assignons également la couleur verte à la classe `heading`, de sorte que chaque élément avec cette classe aura sa couleur remplacée par le vert. Ainsi, la balise `h1` que nous avons définie ci-dessus apparaîtra en vert.

### Partie #6 : Largeur et Hauteur

Dans cette leçon, vous apprendrez à appliquer la largeur et la hauteur afin de contrôler la mise en forme et le flux de la page.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xHqvKfUZPOtuDD5DGzyw9A.png)

Ci-dessus, une diapositive de la leçon, qui vous donnera une idée de la manière dont nous pouvons créer des sections et des boîtes en utilisant la largeur et la hauteur pour que notre page web ait l'air correctement formatée.

### Partie #7 : Unités de Longueur

En CSS, nous pouvons utiliser différentes unités pour mesurer les différentes tailles que nous passons en tant que propriétés de nos éléments HTML. Cette leçon explique en détail quelles sont ces différentes unités et comment elles diffèrent dans leur utilisation.

Il existe deux types d'unités de longueur :

1. Unités Absolues
2. Unités Relatives.

Les unités absolues sont des unités de longueur fixes, et une longueur exprimée dans l'une d'elles apparaîtra exactement de cette taille. Par exemple, `cm`, `mm`, `in`, `px`, etc., sont des unités absolues.

D'autre part, les unités de longueur relatives spécifient une longueur relative à une autre propriété de longueur. Par exemple, `em`, `ex`, `rem`, etc., sont des unités absolues.

### Partie #8 : Couleurs

Cette leçon explique en détail comment nous pouvons utiliser et appliquer des couleurs à différents éléments HTML. Elle explique également les différentes façons dont nous pouvons déclarer le nom de la couleur dans nos propriétés CSS.

```css
.heading1 {  
   color: orange;  
}

.heading2 {  
   color: #ff6347;  
}

.heading3 {  
   color: RGB(255, 99, 71);  
}

```

L'exemple ci-dessus a trois classes déclarées avec la même propriété de couleur qui leur est assignée. Mais le point à noter est la manière dont nous avons utilisé différentes façons d'assigner les valeurs des couleurs.

La classe `heading1` utilise le nom de la couleur (orange) comme propriété. `heading2` utilise la valeur hexadécimale de la couleur. Et `heading3` utilise la valeur RVB de la couleur.

### Partie #9 : Remplissage (Padding)

En CSS, le remplissage est utilisé pour créer des espaces autour du contenu d'un élément à l'intérieur de toute bordure définie. En CSS, vous avez le contrôle pour appliquer le remplissage à tous les côtés ou à n'importe quel côté des éléments. La leçon 9 de ce cours parle du remplissage et vous apprend comment vous pouvez l'appliquer de différentes manières.

```css
.container {  
   padding: 10px;  
   /* padding-left: 10px; */
   /*  padding-right: 10px; */ 
   /*  padding-top: 5px; */
   /*  padding-bottom: 5px; */ 
}

```

Comme dans l'exemple ci-dessus, nous pouvons soit utiliser simplement la propriété `padding`, qui appliquera l'espacement à tous les côtés, soit alternativement, vous pouvez donner un remplissage à des directions individuelles.

### Partie #10 : Bordures

Dans cette leçon, vous apprendrez comment appliquer des bordures autour de votre contenu. Vous apprendrez également les variations que vous pouvez donner aux bordures en utilisant différents styles et options disponibles en CSS.

![Image](https://cdn-media-1.freecodecamp.org/images/1*WntPLYFZ2mhDzzixJsVcvg.png)

Prenez l'exemple de la boîte dans l'image ci-dessus et remarquez les bordures autour avec différentes couleurs et largeurs.

### Partie #11 : Marges

Les marges en CSS sont comme le remplissage : elles appliquent un espacement autour de l'élément mais le font à l'extérieur de toute bordure définie. Cette leçon parle de l'utilisation des marges dans votre CSS, et comment vous pouvez appliquer les mêmes marges dans toutes les directions ou des marges différentes dans différentes directions.

```css
.container {  
   margin: 10px;  
   /* margin-left: 10px;  */
   /* margin-right: 10px;  */
   /* margin-top: 5px;  */
   /* margin-bottom: 5px;  */
}

```

### Partie #12 : Le Modèle de Boîte

Le Modèle de Boîte en CSS est un terme que nous utilisons lorsque nous décrivons le design et la mise en page. Nous pouvons penser à tous les éléments HTML comme à des boîtes où chaque boîte contient des propriétés de marges, de remplissage, de bordures, etc.

![https://www.w3schools.com/css/css_boxmodel.asp](https://cdn-media-1.freecodecamp.org/images/1*v9rFnmtRa7HVOqyiKOAYVA.png)

L'illustration ci-dessus explique le modèle conceptuel de la boîte. Dans cette leçon, Eric expliquera comment nous pouvons utiliser ce concept pour mieux concevoir et arranger nos éléments.

### Partie #13 : Visibilité

Nous pouvons également mettre à jour la visibilité de n'importe quel élément en HTML en utilisant CSS. Nous pouvons, par exemple, cacher ou afficher n'importe quel élément en utilisant la propriété `display`. Cette leçon explique trois différentes façons dont nous pouvons jouer avec la visibilité des éléments.

```css
.hidden {  
   display: none:  
}

```

L'une des trois façons de mettre à jour la visibilité est d'utiliser la propriété `display`. Dans l'exemple ci-dessus, nous avons défini la propriété `display` à none afin que tout élément ayant la classe `hidden` n'apparaisse pas du tout dans le navigateur.

### Partie #14 : Polices

Les polices sont l'une des fonctionnalités les plus importantes et utiles de CSS. Nous pouvons jouer avec différents types de styles de police et de familles de polices pour rendre notre texte attrayant. La leçon 14 de ce cours est entièrement consacrée à l'utilisation des polices !

![Image](https://cdn-media-1.freecodecamp.org/images/1*POhzHtwY6mLoxze0OIFxfA.png)

Dans l'image ci-dessus, le texte Hello World a la `font-family` `Black Han Sans`, arial, sans-serif et la `font-size` de `30px`. De la même manière, nous pouvons appliquer différentes propriétés pour rendre notre texte plus attrayant et beau.

### Partie #15 : Flux des Éléments

Dans cette section du cours, vous apprendrez le flux typique des éléments sur la façon dont ils sont rendus à l'intérieur du navigateur. Il existe deux types d'éléments HTML : les éléments Inline et Block.

Les éléments Inline ne peuvent pas prendre les propriétés `width` et `height`. Ils seront toujours aussi grands que leur contenu. Cependant, sur les éléments de bloc, vous pouvez définir à la fois `width` et `height` comme vous le souhaitez.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-pL6xqjpAAHVYFWz8nouHQ.png)

### Partie #16 : Float et Clear

Dans cette leçon, vous apprendrez les propriétés `float` et `clear`. Celles-ci sont très utiles si nous voulons contrôler la position des éléments HTML pour les faire flotter à gauche ou à droite les uns des autres.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0mteoomCow29RxDdDFYHcw.png)

### Partie #17 : Défi de Mise en Page avec Float

Voici le défi de ce cours. Dans celui-ci, vous serez encouragé à créer la mise en page suivante en utilisant les propriétés `float`. Plus tard dans la vidéo, Eric vous apprendra comment le faire au cas où vous rencontreriez des difficultés.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5qYKDrMQSjdDcBkQ8bJ0Uw.png)

### Partie #18 : Propriété de Position

Dans cette leçon, nous concevrons une simple page d'article où nous utiliserons les propriétés de positionnement disponibles. Nous travaillerons avec des divs, du contenu textuel, des spans et un footer.

À la fin de cette leçon, vous serez en mesure de créer une mise en page comme celle-ci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*DEYQgPYCFINopCArk89V0Q.png)

### Partie #19 : Pseudo-Classes / Éléments

Dans la dernière leçon, nous apprendrons les pseudo-classes et les éléments. Nous utilisons les pseudo-classes pour faire des sélections de niveau avancé de nos éléments HTML. C'est une technique très utile lorsque nous traitons avec des pages web complexes qui ont plusieurs éléments et des styles conditionnels.

```css
/* lien non visité */  
a:link {  
    color: aqua;  
}

/* lien visité */  
a:visited {  
    color: orange;  
}

```

Par exemple, dans l'extrait de code ci-dessus, nous appliquons différentes classes à la balise d'ancrage en utilisant son état, qu'il ait été visité ou non. Il existe des milliers de cas d'utilisation pour les pseudo-classes, et cette leçon vous aidera à comprendre le concept de base de leur utilisation.

### Partie #20 : Qu'est-ce qui suit ?

Dans cette dernière vidéo du cours, Eric résume ce que vous avez appris tout au long du cours et vous donne des conseils pour continuer votre parcours d'apprentissage.

CSS est un sujet vaste, et il existe de nombreuses autres fonctionnalités à apprendre en plus de ce qui a été couvert pendant ce cours !

![Image](https://cdn-media-1.freecodecamp.org/images/1*eyw8VxOKZ9wpffC3QkFBPA.png)

Si vous arrivez jusqu'au bout, vous pouvez vous donner une tape dans le dos. Vous avez fait un grand pas vers l'apprentissage de la construction et de la conception de sites web, ce qui est une compétence extrêmement précieuse.

Alors, allez-y et [suivez le cours gratuit](https://scrimba.com/g/gintrotocss?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gintrotocss_1_hour_article) dès aujourd'hui ! Votre futur vous en remerciera :)

---

Merci d'avoir lu ! Je m'appelle Per Borgen, je suis le cofondateur de [Scrimba](https://scrimba.com) – le moyen le plus facile d'apprendre à coder. Vous devriez consulter notre [bootcamp de design web responsive](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gintrotocss_1_hour_article) si vous voulez apprendre à construire des sites web modernes de manière professionnelle.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Cliquez ici pour accéder au bootcamp avancé.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gintrotocss_1_hour_article)_