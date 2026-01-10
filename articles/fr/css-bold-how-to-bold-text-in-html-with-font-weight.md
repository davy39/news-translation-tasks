---
title: CSS Gras – Comment mettre du texte en gras en HTML avec le poids de la police
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2023-03-02T17:46:56.000Z'
originalURL: https://freecodecamp.org/news/css-bold-how-to-bold-text-in-html-with-font-weight
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/cover-template--4-.png
tags:
- name: CSS
  slug: css
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: CSS Gras – Comment mettre du texte en gras en HTML avec le poids de la
  police
seo_desc: 'CSS is a powerful tool for web developers. It allows you to style and format
  HTML content in various ways.

  One common formatting technique is to make text bold using the font-weight property.
  Bold text can add emphasis to key information, create visu...'
---

CSS est un outil puissant pour les développeurs web. Il permet de styliser et de formater le contenu HTML de diverses manières.

Une technique de formatage courante consiste à mettre du texte en gras en utilisant la propriété `font-weight`. Le texte en gras peut ajouter de l'emphase aux informations clés, créer un contraste visuel et améliorer la lisibilité du contenu.

Dans cet article, vous apprendrez à utiliser CSS pour mettre du texte en gras en HTML en utilisant la propriété `font-weight`. Que vous soyez débutant ou développeur expérimenté, cet article fournira un guide complet pour créer du texte en gras dans votre contenu HTML en utilisant CSS.

## Comprendre la propriété Font-Weight

La propriété `font-weight` est une propriété CSS utilisée pour définir l'épaisseur ou le poids d'une police. Elle détermine le degré de gras ou de légèreté du texte, avec des valeurs plus élevées indiquant un poids de police plus gras.

La propriété `font-weight` accepte diverses valeurs, y compris des valeurs numériques et des mots-clés.

Les valeurs numériques vont de 100 à 900, avec des incréments de 100. Une valeur de 400 est considérée comme normale, tandis qu'une valeur de 700 est considérée comme grasse. Certaines valeurs de mots-clés couramment utilisées incluent `bold`, `bolder`, `lighter` et `normal`.

## Comment créer du texte en gras avec CSS

Créer du texte en gras en HTML en utilisant CSS est un processus simple qui peut être réalisé de plusieurs manières. Vous pouvez choisir d'utiliser n'importe quelle forme de stylisation, telle que inline, interne ou externe.

### Comment créer du texte en gras avec le style inline

Vous pouvez utiliser le style inline pour appliquer la propriété `font-weight` directement à un élément HTML spécifique, comme ceci :

```html
<p style="font-weight: bold;">Ceci est un texte en gras</p>
```

Cependant, le style inline peut rendre votre code HTML encombré et difficile à maintenir, surtout lorsque de nombreux éléments nécessitent les mêmes styles.

### Comment créer du texte en gras avec le style interne

Le style interne permet d'appliquer des styles CSS dans la section `head` d'un document HTML en utilisant la balise `style`, comme ceci :

```html
<head>
  <style>
    p {
      font-weight: bold;
    }
  </style>
</head>
<body>
  <p>Ceci est un texte en gras</p>
</body>
```

Cette méthode est utile lorsque vous appliquez les mêmes styles à plusieurs éléments sur une seule page.

### Comment créer du texte en gras avec le style externe

Le style externe implique la création d'un fichier CSS séparé et le lien vers votre document HTML en utilisant la balise `link`, comme ceci :

```html
<head>
  <link rel="stylesheet" type="text/css" href="styles.css">
</head>
```

Le fichier CSS peut contenir les styles pour tous les éléments HTML de votre site web, et vous pouvez facilement apporter des modifications aux styles sans modifier le code HTML.

```css
p {
  font-weight: bold;
}
```

## Bonnes pratiques pour utiliser le texte en gras en HTML

Bien que l'utilisation de texte en gras en HTML puisse aider à mettre en évidence des informations importantes, il est essentiel de suivre les bonnes pratiques pour garantir que le texte reste lisible et accessible.

Voici quelques bonnes pratiques pour utiliser le texte en gras en HTML :

**Choisir le bon poids de police** : Lorsque vous utilisez du texte en gras, il est essentiel de choisir le bon poids de police pour garantir que le texte est clair et facile à lire.

Alors qu'un poids de police plus lourd peut être adapté aux titres, un poids plus léger peut être plus approprié pour le texte du corps. Il est également important de s'assurer que le texte en gras n'est pas trop écrasant et ne détourne pas l'attention des autres éléments de la page.

**Équilibrer le texte en gras avec d'autres options de formatage** : Bien que le texte en gras puisse être un moyen puissant d'attirer l'attention sur des informations importantes, il est important de l'équilibrer avec d'autres options de formatage pour créer une hiérarchie visuelle.

Vous pouvez utiliser d'autres styles tels que l'italique, le soulignement, ou une taille ou couleur de police différente pour distinguer différents niveaux d'importance.

**Éviter l'utilisation excessive de texte en gras** : L'utilisation excessive de texte en gras peut rendre le texte plus difficile à lire et détourner l'attention de la conception globale de la page.

Il est important d'utiliser le texte en gras avec parcimonie et uniquement là où il est nécessaire de mettre en évidence des informations importantes. Évitez d'utiliser du texte en gras pour des paragraphes ou des blocs de texte entiers, car cela peut rendre difficile pour les lecteurs de distinguer les informations importantes du texte régulier.

**Tester pour l'accessibilité** : Lorsque vous utilisez du texte en gras, il est essentiel de vous assurer qu'il est accessible à tous les utilisateurs, y compris ceux ayant des déficiences visuelles.

Les lecteurs d'écran peuvent avoir des difficultés à lire du texte fortement stylisé, il est donc important de tester la page en utilisant des outils d'accessibilité pour vous assurer que le texte en gras est correctement formaté et accessible.

## Conclusion

En conclusion, l'utilisation de texte en gras en HTML peut être un moyen efficace de mettre en évidence des informations importantes et de créer une hiérarchie visuelle.

En choisissant le bon poids de police, en équilibrant le texte en gras avec d'autres options de formatage, en évitant l'utilisation excessive et en testant pour l'accessibilité, vous pouvez vous assurer que le texte en gras reste lisible et accessible à tous les utilisateurs.

Merci d'avoir lu et amusez-vous bien à coder !

Embarquez pour un voyage d'apprentissage ! [Parcourez plus de 200 articles d'experts sur le développement web](https://joelolawanle.com/contents). Consultez [mon blog](https://joelolawanle.com/posts) pour plus de contenu captivant de ma part.