---
title: Apprendre les bases de CSS en construisant un composant de carte
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-25T05:58:27.000Z'
originalURL: https://freecodecamp.org/news/learn-css-basics-by-building-a-card-component
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/ep13-cssbasic.jpg
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
seo_title: Apprendre les bases de CSS en construisant un composant de carte
seo_desc: "By Thu Nghiem\nIf you want to make your website look attractive, you need\
  \ to know CSS. \nCSS, or Cascading Style Sheets, is a style sheet language that\
  \ is used to style your web content.\nIn this tutorial, we are going to learn about\
  \ CSS basics by build..."
---

Par Thu Nghiem

Si vous voulez rendre votre site web attrayant, vous devez connaître le CSS. 

CSS, ou Cascading Style Sheets, est un langage de feuille de style utilisé pour styliser le contenu de votre site web.

Dans ce tutoriel, nous allons apprendre les bases de CSS en construisant un composant de carte à partir de zéro.

Si vous voulez suivre, assurez-vous de consulter le design [ici](https://www.figma.com/file/FLfQJbcKWGdy5poNWFgLnP/CSS-basics---devChallenges.io?node-id=0%3A1).

Voici une vidéo que vous pouvez regarder si vous voulez compléter cet article :

%[https://youtu.be/yU-euUrE3Bg]

Si vous êtes prêt, commençons.

## Comment construire le squelette avec HTML

Avant de commencer à travailler avec CSS, nous avons besoin de contenu à utiliser. Dans cette section, nous allons rapidement construire un squelette avec HTML. Si vous êtes nouveau dans HTML, vous pouvez consulter un tutoriel [ici](https://www.freecodecamp.org/news/html-basics-for-beginners/).

D'accord, ouvrez VS Code. Ensuite, dans le dossier de votre choix, créez un nouveau fichier et nommez-le `index.html`.

Dans le fichier, tapez `!` et appuyez sur entrée. Vous aurez alors ce modèle HTML :

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  
</body>
</html>

```

Notre travail est de construire un composant de carte qui a une image, des tags, un nom, une description et un bouton comme ceci :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/o9yipv1bp9jv032twvol.png)

Dans `index.html`, changez d'abord le contenu du titre de `Document` à `CSS Basics`. Et dans l'élément `<body>`, ajoutez tous les éléments dont nous aurons besoin :

```html
...
<body>

  <!-- Une div avec l'id container pour contenir la carte -->
  <div id="container">

    <!-- Une div avec la classe card pour la carte -->
    <div class="card">
      <img src="https://images.unsplash.com/photo-1536323760109-ca8c07450053" alt="Lago di Braies">

      <!-- Une div avec la classe card__details pour contenir les détails de la carte -->
      <div class="card__details">

        <!-- Span avec la classe tag pour le tag -->
        <span class="tag">Nature</span>

        <span class="tag">Lac</span>

        <!-- Une div avec la classe name pour le nom de la carte -->
        <div class="name">Lago di Braies</div>

        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Consectetur sodales morbi dignissim sed diam
          pharetra
          vitae ipsum odio.</p>

        <button>Lire plus</button>
      </div>


    </div>
  </div>

</body>

...

```

D'accord, maintenant nous avons le squelette de notre composant. Si vous voulez voir ces changements en direct dans le navigateur, vous pouvez utiliser l'extension [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer).

## Stylisation avec CSS

Ensuite, nous devons styliser le composant. C'est la partie principale du tutoriel. Tout en construisant le composant de carte, je vais également expliquer différents concepts dans cette section.

### Comment appliquer CSS à HTML

Tout d'abord, examinons 3 façons d'appliquer CSS à HTML :

1. **Feuilles de style externes**

Une feuille de style externe est la méthode la plus courante et utile. Elle contient CSS dans un fichier séparé, qui a une extension `.css`.

Vous pouvez ajouter une feuille de style externe en créant un nouveau fichier, `style.css`, dans le même dossier que `index.html`. Et à l'intérieur de l'élément `<head>`, vous pouvez importer la feuille de style avec ce qui suit :

```html
<link rel="stylesheet" href="style.css">

```

Avec cette méthode, la même feuille de style peut être utilisée pour appliquer CSS à plusieurs pages.

**2. Feuilles de style internes**

Vous pouvez ajouter une feuille de style interne en ayant CSS à l'intérieur de l'élément `<style>` qui est placé à l'intérieur de l'élément `<head>`. Par exemple :

```html
<head>
  <style>
    /* votre style */
  </style>
</head>

```

Cette méthode est utile lorsque vous devez travailler avec un système qui vous empêche de modifier les feuilles de style externes.

Un inconvénient de cette méthode est que les styles ne peuvent pas être appliqués à plusieurs pages.

**3. Styles en ligne (évitez de les utiliser)**

Vous pouvez également ajouter un style directement à un élément en utilisant l'attribut `style`. Par exemple, si vous voulez changer la couleur du texte du paragraphe en rouge :

```html
<p style="color:red;">paragraphe</p>

```

Cette méthode est courante lorsque vous devez travailler avec un système très restrictif où vous ne pouvez pas modifier les feuilles de style externes ou internes.

L'ajout de styles en ligne à votre document n'est **pas** une bonne pratique – c'est difficile à lire et à comprendre, donc vous devriez l'éviter lorsque cela est possible.

## Comment ajouter une feuille de style externe au composant de carte

D'accord, maintenant vous savez comment appliquer CSS à HTML. Pour cet exercice, utilisons une feuille de style externe. 

Créez un nouveau fichier nommé `style.css` et ajoutez `<link rel="stylesheet" href="style.css">` à l'intérieur de l'élément `<head>`.

### Règles CSS

Si vous voulez donner à l'image une largeur de 50 %, vous pouvez le faire en ajoutant ceci :

```css
img {
  width: 50%;
}

```

Pour sélectionner et styliser un élément, vous devez avoir un sélecteur, la propriété que vous voulez styliser et la valeur de la propriété.

La propriété doit être à l'intérieur des accolades et doit être séparée par un deux-points et terminée par un point-virgule, cette structure entière est appelée règles :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/y6g4upcbymin9kyjl0lr-1.png)

### Stylisation de nos éléments

1. **L'élément `body`**

Pour l'élément `body`, nous voulons changer la couleur de fond et la famille de polices :

```css
body {
  background-color: #eaeff1;
  font-family: "Raleway", sans-serif;
}

```

Mais, pour que la police Raleway fonctionne, nous devons importer la police. Nous pouvons le faire en mettant ceci en première ligne de la feuille de style.

```css
@import url("https://fonts.googleapis.com/css2?family=Raleway:wght@500;600&display=swap");

```

Pour en savoir plus sur les polices Google, vous pouvez visiter [fonts.google.com](https://fonts.google.com/).

D'accord, si la couleur de fond du corps et la police ont changé, félicitations, vous venez d'ajouter votre premier CSS 🎉

**2. Élément `img`**

Pour le moment, l'image est à sa largeur d'origine, mais nous voulons qu'elle s'adapte à l'écran. Nous pouvons le faire en lui donnant une largeur de 100 % :

```css
img {
  width: 100%;
}

```

Nous voulons également lui donner une bordure arrondie et une hauteur plus petite que l'originale :

```css
img {
  ...
  border-radius: 12px;
  height: 214px;
}

```

Maintenant, vous pouvez voir que l'image est déformée. Nous pouvons la corriger en ajoutant `object-fit: cover;` :

```css
img {
  ...
  object-fit: cover;
}

```

D'accord, maintenant vous devriez avoir une image réactive avec une hauteur de 214px. Alors, continuons.

**3. Stylisation du conteneur**

Ensuite, nous devons styliser l'élément `div` qui a l'attribut `id` de `container`. Ce sera l'élément qui décide de la largeur de la carte et la place au milieu de la vue.

Pour sélectionner le conteneur, ajoutez :

```css
#container {
  max-width: 300px;

  /* Centrer le conteneur au milieu sur l'axe horizontal */
  margin: 0 auto;

  /* Ajouter un espace vide au-dessus du conteneur (20 % de la hauteur de la vue) */
  margin-top: 20vh;
}

```

Vous pouvez voir que nous utilisons `margin: 0 auto;` pour centrer l'élément `div` qui a une `max-width` de `300px`.

Pour l'instant, vous devez simplement vous souvenir de cette astuce. Dans les futurs tutoriels, nous approfondirons le fonctionnement des marges et la manière de centrer les éléments.

**4. Stylisation de la carte**

Pour styliser la carte, nous devons sélectionner l'élément `div` qui a la classe `card`. Nous voulons également lui donner une couleur de fond blanche, une bordure et un espace entre le contenu et la bordure :

```css
.card {
  /* Changer la couleur de fond */
  background-color: white;

  /* Ajouter une bordure */
  border: 1px solid #bacdd8;

  /* Ajouter un espace entre la bordure et le contenu */
  padding: 8px;

  border-radius: 12px;
}

```

D'accord, maintenant nous sommes à mi-chemin de la stylisation du composant complet. Stylisons rapidement le reste des éléments :

```css

/* Styliser les éléments div qui ont une classe égale à tag */
.tag {
  padding: 4px 8px;
  border: 1px solid #e5eaed;

  border-radius: 50px;
  font-size: 12px;
  font-weight: 600;
  color: #788697;
}

/* Styliser les éléments div qui ont une classe égale à name */
.name {
  font-size: 24px;
  font-weight: 600;

  margin-top: 16px;
}

/* Styliser l'élément p */
p {
  font-size: 14px;
  color: #7f8c9b;
  line-height: 150%;
}

/* Styliser l'élément button */
button {
  border: none;
  padding: 12px 24px;
  border-radius: 50px;

  font-weight: 600;
  color: #0077ff;
  background-color: #e0efff;

  /* Le bouton est un élément inline-block par défaut, il doit avoir un affichage block pour que margin: 0 auto; fonctionne */
  margin: 0 auto;
  display: block;

  /* Le bouton est un élément cliquable, il doit donc avoir un curseur de type pointeur */
  cursor: pointer;
}

.card__details {
  /* Ajouter un espace autour des détails */
  padding: 16px 8px 8px 8px;
}

```

**5. Stylisation du bouton lorsqu'il est focalisé ou survolé**

Lorsque le bouton est focalisé ou survolé, il est bon d'avoir une indication pour l'utilisabilité. Vous pouvez le faire en échangeant les couleurs de texte et de fond du bouton :

```css
/* Ajouter un style lorsque le bouton est focalisé ou survolé */
button:focus,
button:hover {
  background-color: #0077ff;
  color: #e0efff;
}

```

D'accord, maintenant nous avons terminé la stylisation du composant. Jetons un rapide coup d'œil à la manière dont la marge, le remplissage et la bordure fonctionnent dans la section suivante.

## Le modèle de boîte CSS

En CSS, chaque élément est une boîte. Chaque boîte a les propriétés suivantes :

* **Padding** : Espace à l'extérieur du contenu
* **Border** : Lignes à l'extérieur du padding
* **Margin** : Espace à l'extérieur de la bordure

![Image](https://www.freecodecamp.org/news/content/images/2021/02/acdnznf06c6qgoxid7xw.png)

### Marge

Nous utilisons la marge pour ajouter un espace invisible à l'extérieur d'un élément qui pousse les autres éléments.

Pour notre composant de carte, nous avons utilisé la marge pour ajouter un espace vide au-dessus du conteneur, un espace entre le nom et les tags, et pour centrer la carte sur l'axe horizontal.

Vous pouvez définir `margin-top`, `margin-bottom`, `margin-left` et `margin-right` individuellement. Ou vous pouvez utiliser cette abréviation :

```css
margin: topValue rightValue bottomValue leftValue;
margin: verticalValue horizontalValue;

```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/do4y57sxjpkf08o6o01y.png)

### Bordure

La propriété de bordure ajoute une bordure autour d'un élément. Pour notre composant de carte, nous avons ajouté une bordure autour de la carte et de chaque tag.

Vous pouvez définir `border-top`, `border-bottom`, `border-left`, `border-right`, `border-width`, `border-style` et `border-color`. Ou vous pouvez également utiliser l'abréviation suivante :

```css
border: widthValue styleValue colorValue;

```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/oybb0vi7djd1nlib543i.png)

### Remplissage

Le remplissage est utilisé pour ajouter un espace intérieur entre la bordure et son contenu. Dans notre composant de carte, nous avons utilisé le remplissage dans la carte et le bouton.

Vous pouvez définir `padding-top`, `padding-bottom`, `padding-left` et `padding-right`. Ou vous pouvez utiliser cette abréviation :

```css
padding: topValue rightValue bottomValue leftValue;
padding: verticalValue horizontalValue;

```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/572lkbb2j8npxn7isifq.png)

## Conclusion

Cela conclut le tutoriel. 

Il existe de nombreux autres concepts importants de CSS à apprendre. Mais avec ce tutoriel, vous devriez être prêt à utiliser CSS dans votre prochain projet pour le rendre génial.

Vous pouvez me suivre sur [Twitter](https://twitter.com/thunghiemdinh) ou [YouTube](https://www.youtube.com/c/thunghiem) pour les futures vidéos et tutoriels. Mais pour l'instant, bon codage et à bientôt dans les prochains articles.

__________ 👋 **À propos de moi** __________

Je suis un développeur full-stack, un designer UX/UI et un créateur de contenu. 

Je suis également le fondateur de d[evChallenges](https://devchallenges.io/). Vous pouvez trouver plus de ces tutoriels vidéo sur [devchallenges.io/learn](https://devchallenges.io/learn).