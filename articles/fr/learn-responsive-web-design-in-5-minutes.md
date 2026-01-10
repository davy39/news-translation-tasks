---
title: Tutoriel sur le design responsive - Apprenez le design web responsive en 5
  minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-20T13:07:07.000Z'
originalURL: https://freecodecamp.org/news/learn-responsive-web-design-in-5-minutes
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca0c3740569d1a4ca4a9b.jpg
tags:
- name: CSS
  slug: css
- name: Web Design
  slug: web-design
seo_title: Tutoriel sur le design responsive - Apprenez le design web responsive en
  5 minutes
seo_desc: 'By Per Harald Borgen

  In this article, I''ll teach you as many responsive design techniques as I possibly
  can in five minutes. This obviously isn''t enough to learn it properly, but it will
  give you an overview of the most important concepts, which I pe...'
---

Par Per Harald Borgen

Dans cet article, je vais vous enseigner autant de techniques de design responsive que possible en cinq minutes. Cela ne suffit évidemment pas pour l'apprendre correctement, mais cela vous donnera un aperçu des concepts les plus importants, que je définis personnellement comme suit :

* Unités CSS relatives
* Requêtes média
* Flexbox
* Typographie responsive

Si vous souhaitez approfondir le sujet par la suite, vous pouvez consulter notre [bootcamp de développeur web responsive sur Scrimba](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gresponsive_5_minute_article), qui vous permettra de construire des sites web responsives à un niveau professionnel.

Mais pour l'instant, commençons par les bases !

## Unités CSS relatives

Au cœur du design web responsive se trouvent les unités CSS relatives. Ce sont des unités qui obtiennent leur valeur à partir d'une autre valeur externe. Cela est pratique car cela permet, par exemple, à la largeur d'une image d'être basée sur la largeur du navigateur.

Les plus courantes sont :

* %
* em
* rem
* vw
* vh

Dans cet article, nous commencerons par l'unité de pourcentage `%`, puis nous examinerons l'unité `rem` dans la section finale.

Disons que vous avez un site web très simple, comme ceci :

![Alt Text](https://thepracticaldev.s3.amazonaws.com/i/0790836uoiwkopmzl1y8.png)

Son HTML est simplement le suivant :

```html
<body>
    <h1>Bienvenue sur mon site web</h1>
    <image src="path/to/img.png" class="myImg">
</body>

```

Comme vous pouvez le voir à partir du GIF ci-dessous, notre image aura par défaut une largeur fixe : 


![Alt Text](https://thepracticaldev.s3.amazonaws.com/i/9y888o3ut0yevvxm6bna.gif)

Ce n'est pas particulièrement responsive, alors changeons cela à 70 pour cent à la place. Nous allons simplement faire ce qui suit :

```css
.myImg {
    width: 70%;
}

```

Cela définit la largeur de l'image à 70 pour cent de la largeur de son parent, qui est la balise `<body>`. Comme la balise `<body>` s'étend sur toute la largeur de l'écran, l'image sera toujours à 70 pour cent de la largeur de l'écran lui-même.

Voici le résultat :

![Alt Text](https://thepracticaldev.s3.amazonaws.com/i/96fhaye5co7n3dljc9d8.gif)

Et c'est aussi simple que cela pour créer une image responsive !

## Utilisation des requêtes média pour améliorer l'expérience mobile

Nous avons un problème avec notre mise en page responsive, cependant, qui est qu'elle semble étrange sur les très petits écrans. La largeur de 70 % est trop étroite lorsqu'elle est vue sur mobile. Jetez un coup d'œil par vous-même :  
  


![Alt Text](https://thepracticaldev.s3.amazonaws.com/i/r6ozk66b8ukv3mb67i6d.png)

  
  
Rendre cela plus beau dans cette situation est une tâche parfaite pour les requêtes média. Elles vous permettent d'appliquer différents styles en fonction, par exemple, de la largeur de l'écran. Nous pouvons dire en gros _si l'écran est inférieur à 768px de large, utilisez un style différent._

Voici comment nous créons une requête média en CSS :

```css
@media (max-width: 768px) {
    .myImage {
        width: 100%
    }
}

```

Ce bloc CSS ne sera appliqué que si la largeur de l'écran est inférieure à 768 pixels.

Voici le résultat :

![Alt Text](https://thepracticaldev.s3.amazonaws.com/i/tebsuaareu10uqlrgmms.gif)

Comme vous pouvez le voir, la page a un point d'arrêt où l'image devient soudainement plus large. C'est lorsque le navigateur fait 768 pixels de large, et l'image passe de `70%` à `100%`.

## Utilisation de Flexbox pour la barre de navigation

Ensuite, nous avons Flexbox. Vous ne pouvez pas apprendre le responsive sans apprendre Flexbox. Il a changé la donne du design responsive lorsqu'il a été introduit il y a quelques années, car il facilite grandement le positionnement des éléments de manière responsive le long d'un axe.

Pour utiliser Flexbox, nous allons rendre notre site un peu plus complexe en ajoutant une barre de navigation au-dessus du titre. Voici le HTML pour cela :

```html
<nav>
    <a href="#">Accueil</a>
    <a href="#">À propos de moi</a>
    <a href="#">Contact</a>
</nav>

```

Par défaut, cela ressemblera simplement à ceci.  
  


![Alt Text](https://thepracticaldev.s3.amazonaws.com/i/wp00p4j2c07rfavaef2d.png)

  
  
Nos éléments de navigation sont tous serrés sur le côté gauche, ce qui n'est pas ce que nous voulons. Nous voulons qu'ils soient espacés uniformément sur toute la page.

Pour y parvenir, nous allons simplement transformer le conteneur nav en une flexbox, puis utiliser la propriété magique `justify-content`.

```css
nav {
    display: flex;
    justify-content: space-around;
}

```

Le `display: flex` transforme le `<nav>` en une boîte flexible, et le `justify-content: space-around` indique au navigateur que les éléments à l'intérieur de la boîte flexible doivent avoir de l'espace autour d'eux. Ainsi, le navigateur distribue tout l'espace restant également autour des trois éléments.

Voici à quoi cela ressemble. Et comme vous le remarquerez, cela s'adapte bien :

![Alt Text](https://thepracticaldev.s3.amazonaws.com/i/8n18vp4s7hkophcgcdg0.gif)



## Typographie responsive : rem

La dernière étape consiste à rendre notre typographie également responsive. Vous voyez, je veux que la barre de navigation et le titre rétrécissent un peu lorsque l'écran est inférieur à 768 pixels de large (notre point d'arrêt de requête média, vous vous souvenez ?).

Une façon de faire cela serait de diminuer toutes les tailles de police dans la requête média, comme ceci :

```css
@media (max-width: 768px) {
    nav {
        font-size: 14px;
    }
    h1 {
        font-size: 28px;
    }
}

```

Ce n'est pas idéal cependant. Nous pourrions finir avec plusieurs points d'arrêt dans l'application, et avoir plusieurs éléments également (h2, h3, paragraphes, etc). En conséquence, nous devrons garder une trace de tous les éléments dans tous les différents points d'arrêt. Ce sera un désordre !

Cependant, il est probable qu'ils soient liés les uns aux autres de manière plus ou moins similaire à travers les différents points d'arrêt. Par exemple, le `h1` sera toujours plus grand que le `paragraphe`.

Alors, que se passerait-il s'il y avait un moyen pour moi d'ajuster un facteur, et ensuite faire en sorte que le reste des tailles de police s'adapte relativement à ce facteur ?

Entrez les rems !

Un `rem` est essentiellement ceci : la valeur de la taille de police que vous avez définie pour votre élément `<html>`. Comme ceci :

```css
html {
    font-size: 14px;
}

```

Donc dans ce document, un `rem` est égal à 14px.

Cela signifie que nous pouvons définir toutes nos tailles de police sur notre site web en unités `rem`, comme ceci :

```css
h1 {
    font-size: 2rem;
}

nav {
    font-size: 1rem;
}

```

Et ensuite, nous allons simplement changer la valeur de la taille de police pour la balise `<html>` à l'intérieur de notre requête média. Cela garantira que la taille de la police pour nos éléments `h1` et `nav` changera également.

Voici comment nous changeons notre valeur `rem` dans une requête média :

```css
@media (max-width: 768px) {
    html {
        font-size: 14px
    }
}

```

Et tout simplement, nous avons un point d'arrêt pour toutes nos tailles de police également. Remarquez comment la taille de la police change lorsque la page franchit la marque des 768 pixels :

![Alt Text](https://thepracticaldev.s3.amazonaws.com/i/5ktvcqiyu50tcu1l9xqn.gif)

Cela n'a été que cinq minutes, mais maintenant vous avez réellement appris à rendre les tailles de police, les images et les éléments de la barre de navigation pour qu'ils répondent à la largeur de la page. C'est plutôt bien, et vous avez fait vos premiers pas vers l'apprentissage des compétences hautement précieuses de la construction de sites web responsives.

Si vous êtes intéressé à continuer ce voyage d'apprentissage, je vous recommande de jeter un coup d'œil à notre [massive cours Scrimba sur le sujet !](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gresponsive_5_minute_article) Il est enseigné par l'un des enseignants les plus populaires de YouTube sur le sujet, et il vous mènera à un niveau professionnel en design web responsive.

Bon codage :)

---

Merci d'avoir lu ! Je m'appelle Per Borgen, je suis le co-fondateur de [Scrimba](http://scrimba.com?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gresponsive_5_minute_article) – la manière la plus facile d'apprendre à coder. Vous devriez consulter notre [bootcamp de design web responsive](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gresponsive_5_minute_article) si vous voulez apprendre à construire des sites web modernes à un niveau professionnel.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Cliquez ici pour accéder au bootcamp avancé.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gresponsive_5_minute_article)_