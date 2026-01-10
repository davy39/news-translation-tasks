---
title: Police HTML – Exemple de famille de polices CSS (caractères Serif et Sans Serif)
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-08-26T22:15:30.000Z'
originalURL: https://freecodecamp.org/news/html-font-css-font-family-example-serif-and-sans-serif-characters
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/brett-jordan-M9NVqELEtHU-unsplash.jpg
tags:
- name: CSS
  slug: css
- name: fonts
  slug: fonts
- name: HTML
  slug: html
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Police HTML – Exemple de famille de polices CSS (caractères Serif et Sans
  Serif)
seo_desc: 'Choosing the right font is an important first step in making your website
  usable and accessible.

  How text is formatted affects how readable your designs and webpages are.

  You can modify how your HTML text appears in many ways using CSS. You can selec...'
---

Choisir la bonne police est une première étape importante pour rendre votre site web utilisable et accessible.

La manière dont le texte est formaté affecte la lisibilité de vos designs et pages web.

Vous pouvez modifier l'apparence de votre texte HTML de nombreuses manières en utilisant CSS. Vous pouvez sélectionner le type de police que vous souhaitez utiliser, qu'elle soit en gras ou non, sa taille, et vous pouvez même changer la couleur et ajouter différents espacements ou décorations.

Dans cet article, nous allons passer en revue les différences entre les deux types de polices les plus populaires, Serif et Sans Serif.

De plus, nous allons couvrir la syntaxe et comment utiliser la propriété `font-family` afin que, avec l'aide de CSS, vous puissiez choisir et ensuite utiliser différentes polices dans vos projets de design web.

Commençons !

## Terminologie des polices

Tout d'abord, discutons de certains des types de polices les plus courants et fréquemment utilisés que les navigateurs modernes supportent.

### Le type de police Serif

Les polices Serif sont caractérisées par les petits détails supplémentaires fins à la fin des lettres.

![Screenshot-2021-08-13-at-4.34.15-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-13-at-4.34.15-PM.png)

À la fin des traits principaux des caractères, il y a de petits traits floraux appelés *serifs*.

![Screenshot-2021-08-13-at-4.38.02-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-13-at-4.38.02-PM.jpeg)

Les polices Serif sont traditionnellement largement utilisées en impression car elles sont considérées comme lisibles pour de longs passages de texte. Mais elles ne s'affichent pas toujours bien sur les écrans.

Les polices Serif sont considérées comme parmi les polices les plus classiques, élégantes et traditionnelles que vous pouvez utiliser.

### Le type de police Sans-Serif

Ce type de police crée un design propre, tout en étant très lisible et clair.

![Screenshot-2021-08-13-at-4.35.04-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-13-at-4.35.04-PM.png)

Ce type de police a des extrémités droites sur chaque lettre et il n'y a pas de traits sur les bords, ce qui rend les caractères nets et plats avec des lignes propres.

![Screenshot-2021-08-13-at-4.38.14-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-13-at-4.38.14-PM.jpeg)

Les polices Sans-serif sont considérées comme modernes, minimalistes, contemporaines et un choix un peu plus lisible pour les écrans d'ordinateur haute résolution.

### Le type de police Monospace

Avec ce type de police, chaque lettre a la même largeur fixe et les lettres sont également espacées.

Avec les types de polices précédents que nous avons discutés jusqu'à présent, chaque lettre a une largeur différente.

Ainsi, avec la police à chasse fixe, toutes les lettres ont la même largeur. Cela permet d'aligner le texte proprement et le rend facile à suivre, donnant aux designs une apparence propre et une sensation mécanique.

![Screenshot-2021-08-13-at-5.29.11-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-13-at-5.29.11-PM.png)

Il existe deux autres types de polices génériques disponibles, `fantasy` et `cursive`, mais les polices les plus largement utilisées sont celles mentionnées ci-dessus.

## Comment choisir une police pour votre site web – noms de polices

Maintenant que nous avons couvert les bases des termes et descriptions de polices, il est temps de regarder les nombreux styles de polices différents au sein de chaque famille.

Certains styles courants au sein de chaque famille de polices sont listés ci-dessous :

### Polices Serif

- Georgia
- Times
- Times New Roman
- Bodoni
- Garamond
- Palatino
- ITC Clearface
- Plantin
- Freight Text
- Didot
- American Typewriter

### Polices Sans-Serif

- Arial
- Verdana
- Helvetica
- Geneva
- Tahoma
- Trebuchet MS
- Open Sans
- Liberation Sans
- Impact

### Polices Monospace

- Courier
- MS Courier New
- Monaco
- Lucinda Console
- Andale Mono
- Menlo
- Consolas

## Comment utiliser la propriété `font-family`

En CSS, la propriété `font-family` définit une police spécifique pour un élément et comment son contenu textuel sera affiché et rendu.

La syntaxe pour la propriété `font-family` est :

```CSS
élément {
font-family: valeur;
}
```

Nous écrivons la propriété `font-family` suivie d'un deux-points `:`, d'un espace, d'une `valeur`, et enfin nous terminons la spécification avec un point-virgule `;`.

Nous devons définir la propriété que nous voulons cibler et assigner la valeur que nous voulons.

## Comment définir une police CSS

Supposons que nous avons le HTML suivant :

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Polices CSS</title>
</head>
<body>
    <h1>Police HTML – Famille de polices CSS</h1>
    <p>Je suis un paragraphe</p>
</body>
</html>
```

Sans aucun style appliqué et sans définir explicitement une valeur pour la propriété `font-family`, les navigateurs affichent les titres et les paragraphes dans la police de leur choix.

La police par défaut et standard utilisée dans Google Chrome est `Times New Roman`, une police serif.

Le résultat ressemble à ceci :

![Screenshot-2021-08-13-at-7.03.34-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-13-at-7.03.34-PM.png)

Il existe plusieurs façons de définir une police différente et de spécifier la police que nous voulons.

Lors du choix d'une police – c'est-à-dire la partie `valeur` – il est utile de mentionner que les sites utilisent un ensemble limité de polices. Ils utiliseront des polices déjà installées sur l'ordinateur de l'utilisateur.

Un navigateur affichera une police uniquement si elle est déjà installée sur l'ordinateur de l'utilisateur.

Alors, voyons les différentes façons de définir une police en CSS.

### Comment utiliser un nom de famille de polices générique

Dans ce cas, les noms sont des mots-clés et incluent l'une des catégories de polices mentionnées précédemment (serif, sans-serif, monospace).

Cela ressemblerait à ceci :

```CSS
p {
  font-family: serif;
}
```

Cela définit la police comme une police serif générique.

### Comment utiliser un nom de famille de polices spécifique

```CSS
p {
 font-family: Times, serif;
}
```

Cette règle définit `Times` comme la police souhaitée, puis `serif` comme option de repli générique, au cas où la première option ne serait pas installée sur l'ordinateur de l'utilisateur.

Si le nom contient des espaces, vous devez l'enfermer dans des guillemets.

```CSS
p {
font-family: "Courier New", monospace;
}
```

Cela définit la police comme `Courier New` et ajoute `monospace` comme sauvegarde.

Si nous spécifions une police autre que l'un des noms génériques (comme serif, sans-serif), nous devons donner au navigateur une option de repli.

### Comment utiliser une pile de polices

Dans ce cas, la propriété `font-family` a plusieurs valeurs.

Il s'agit d'une liste priorisée, séparée par des virgules, de noms de familles de polices que vous pouvez appliquer au texte, indiquant que toutes les polices sont des alternatives. Cela permet une compatibilité maximale avec les navigateurs et les systèmes d'exploitation.

La liste est priorisée de gauche à droite, de la priorité la plus haute à la plus basse.

```css
p {
  font-family: "Lucida Console", Courier, monospace;
}
```

En appliquant plus d'un nom de famille de polices, vous créez un ordre de préférence. Nous commençons par la police que nous voulons en premier.

Si un utilisateur n'a pas la première option installée sur son ordinateur ou si elle n'est pas supportée par le navigateur, le navigateur passe à la deuxième police et utilise celle-ci. Si cette police n'est pas non plus disponible, il passe à la troisième, et ainsi de suite.

Nous pouvons lister autant de polices que nous le souhaitons, mais la meilleure pratique est d'en lister trois à quatre.

Si tout le reste échoue, il y aura toujours une police générique listée à la fin comme dernier mécanisme de repli.

Parmi le groupe listé, le navigateur doit supporter *au moins* une option et le nom générique garantit que quelque chose dans la famille de polices souhaitée sera rendu.

```CSS
p {
 font-family: Georgia, "Times New Roman", Times, serif;
}
```

Les polices que vous listez sont connues sous le nom de *pile de polices*.

Le navigateur recherchera d'abord `Georgia`. Si elle est installée, le navigateur affichera cette police. Sinon, il recherchera `Times New Roman`. Si celle-ci n'est pas non plus disponible, il affichera la police générique par défaut `serif`.

## Conclusion

Dans cet article, nous avons passé en revue les différentes familles de polices et donné quelques exemples des différents styles au sein de chaque famille.

Nous avons également passé en revue la propriété `font-family` et les trois différentes façons de définir une police en CSS.

Si vous souhaitez en savoir plus sur HTML et CSS et les différentes techniques modernes utilisées, freeCodeCamp propose une certification gratuite sur le [Responsive Web Design](https://www.freecodecamp.org/learn/responsive-web-design/).

Vous commencerez par les bases absolues et passerez par Flexbox, CSS Grid, et comment rendre les sites web responsives. Ce sont des compétences essentielles à avoir pour le design numérique et le développement web front-end.

À la fin, vous construirez 5 projets, y compris un site portfolio où vous pourrez montrer les autres projets que vous avez construits si vous le souhaitez.

Merci d'avoir lu et bon apprentissage.