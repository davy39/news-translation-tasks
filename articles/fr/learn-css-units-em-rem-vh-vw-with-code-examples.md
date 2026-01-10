---
title: Apprendre les unités CSS – Em, Rem, VH et VW avec des exemples de code ✨✨
subtitle: ''
author: Joy Shaheb
co_authors: []
series: null
date: '2021-08-25T15:34:28.000Z'
originalURL: https://freecodecamp.org/news/learn-css-units-em-rem-vh-vw-with-code-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/FCC-Thumbnail.png
tags:
- name: CSS
  slug: css
- name: responsive design
  slug: responsive-design
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Apprendre les unités CSS – Em, Rem, VH et VW avec des exemples de code
  ✨✨
seo_desc: "Today we're gonna learn how to use the CSS units EM, REM, VW and VH by\
  \ working through some practical examples. We'll also see how to make responsive\
  \ websites with these units. \nLet's start. \U0001F496\nTable of Contents\n\nWhy\
  \ learn relative units?\nWhat are RE..."
---

Aujourd'hui, nous allons apprendre à utiliser les unités CSS EM, REM, VW et VH en travaillant sur quelques exemples pratiques. Nous verrons également comment créer des sites web responsives avec ces unités. 

Commençons. 💖

# Table des matières

* [Pourquoi](#heading-pourquoi-apprendre-les-unites-css-relatives) apprendre les unités relatives ?
* [Qu'est-ce que les unités REM ?](#heading-quest-ce-que-les-unites-rem)
* [Comment créer des sites web responsives avec les unités REM](#heading-comment-creer-des-sites-web-responsives-avec-les-unites-rem)
* [Qu'est-ce que les unités EM ?](#heading-quest-ce-que-les-unites-em)
* [Qu'est-ce que les unités VW](#heading-quest-ce-que-les-unites-vw) ?
* [Qu'est-ce que les unités VH ?](#heading-quest-ce-que-les-unites-vh)
* [Ressources supplémentaires](#heading-ressources-supplementaires)

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Frame-25.png)
_**Sujets abordés**_

## **Vous pouvez également regarder ce tutoriel sur YouTube si vous le souhaitez :**

%[https://youtu.be/6uJPTM0AaFc]

# Pourquoi apprendre les unités CSS relatives ?

![Image](https://www.freecodecamp.org/news/content/images/2021/07/YT-Thumbnail-1.png)

Si vous voulez créer des **sites web responsives** très facilement, rapidement et efficacement, alors vous devriez définitivement apprendre les unités relatives de CSS. 

**REM, EM, VW, VH sont des unités relatives**. Si vous combinez celles-ci avec des requêtes média, alors vous pouvez créer des mises en page parfaitement scalables. Regardez ce GIF 👇 La taille du texte est responsive sur les écrans de bureau, de tablette et de mobile ! 

![Image](https://www.freecodecamp.org/news/content/images/2021/07/final-1.gif)
_**Police utilisant l'unité REM**_

Gardez à l'esprit que **les pixels sont des unités absolues**. Ils ne changeront pas lorsque vous redimensionnerez la fenêtre. Regardez ce GIF 👇 Remarquez que la taille de police de **50px ne change pas** lorsque nous redimensionnons la fenêtre.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/aaaaaaaaaaa.gif)
_**Police utilisant l'unité Pixel**_

Astuce : Avant de commencer le tutoriel, je vous suggère de ne pas penser à EM et REM comme des unités. Considérez-les comme des multiplicateurs d'un nombre de base. 

# Installation du projet 

![Image](https://www.freecodecamp.org/news/content/images/2021/08/YT-Thumbnail.png)

Tout d'abord, [copiez le code de ce lien Code Pen](https://codepen.io/joyshaheb/pen/XWMqEdV) et collez-le dans VS Code ou votre éditeur de code préféré. Ensuite, suivez ces étapes :👇

* créez un dossier nommé **projet-1**
* créez des fichiers HTML, CSS, JS et liez-les ensemble
* installez les plugins dont nous aurons besoin – **px to rem** et **Live server**
* Exécutez le serveur en direct

![Image](https://www.freecodecamp.org/news/content/images/2021/08/textthat.gif)
_**Test des fichiers de démarrage**_

Comme vous pouvez le voir dans le gif ci-dessus, 👆 le JavaScript effectue tous les calculs, donc nous devons simplement nous concentrer sur le tutoriel. Nous allons simplement changer le CSS et expérimenter avec différentes valeurs. 

Commençons à coder !

![Image](https://www.freecodecamp.org/news/content/images/2021/08/YT-Thumbnail--1-.png)

# Qu'est-ce que les unités REM ?

![Image](https://www.freecodecamp.org/news/content/images/2021/07/YT-Thumbnail--1-.png)

L'unité REM dépend de l'**élément racine** [l'élément **HTML**]. Voici une image pour vous montrer comment cela fonctionne :👇

![Image](https://www.freecodecamp.org/news/content/images/2021/07/YT-Thumbnail--5-.png)
_**Taille de police par défaut de l'élément racine**_

La taille de police par défaut de l'élément racine [en HTML] est de 16px. Donc, 1 REM = 16px. 

Si nous écrivons 3 rem, cela nous montrera **[ 3*16px = 48px ]**. Comme vous pouvez le voir, cela fonctionne comme un multiplicateur.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/YT-Thumbnail--7-.png)
_**expérimentation avec 3 rem**_

Mais, si nous changeons la taille de police de l'élément racine, l'unité REM change – comme ceci : 👇

![Image](https://www.freecodecamp.org/news/content/images/2021/07/YT-Thumbnail--6-.png)
_**taille de police modifiée de l'élément racine**_

Nous définissons la taille de police HTML à 50px. 

Maintenant, si nous écrivons 3 rem, cela nous montrera **[ 3*50px = 150px ]** comme ceci : 👇

![Image](https://www.freecodecamp.org/news/content/images/2021/07/YT-Thumbnail--8-.png)
_**expérimentation avec 3 rem**_

Recréons les résultats avec du code et voyons leurs cas d'utilisation en pratique. 👇

Tout d'abord, expérimentons avec la taille de police par défaut de chaque site web, qui est de 16 pixels. Et nous définirons la taille de police de la classe `.text` à 1 rem.

```css
html {
  font-size: 16px;
}

.text {
  font-size: 1rem;
}

/** Calculs 
 1 rem * 16px = 16px
**/

```

Voici à quoi ressemble le résultat :👇

![Image](https://www.freecodecamp.org/news/content/images/2021/08/YT-Thumbnail--6-.png)
_**Taille de police est 1rem, racine est 16px**_

Maintenant, augmentons la taille de police `.text` à 2 rem :

```css
html {
  font-size: 16px;
}

.text {
  font-size: 2rem;
}

/** Calculs
 2 rem * 16px = 32px
**/
```

Et voici le résultat : 👇

![Image](https://www.freecodecamp.org/news/content/images/2021/08/YT-Thumbnail--5-.png)
_**Taille de police est 2 rem, racine est 16px**_

Comme vous pouvez le voir, la taille de la police devient plus grande mais la largeur reste la même (1536px).

### Comment changer la taille de police racine

Maintenant, expérimentons en changeant la taille de police racine, qui se trouve dans le html. Écrivez d'abord ce code pour obtenir le résultat par défaut : 👇

```css
html {
  font-size: 16px;
}

.text {
  font-size: 1rem;
}

/** Calculs
 1 rem * 16px = 16px
**/
```

Voici à quoi cela ressemble :👇

![Image](https://www.freecodecamp.org/news/content/images/2021/08/YT-Thumbnail--6--1.png)
_**Paramètre par défaut**_

Maintenant, changez la taille de police racine à 40px comme ceci :

```css
html {
  font-size: 40px;
}

.text {
  font-size: 1rem;
}

/** Calculs
 1 rem * 40px = 40px
**/
```

Voici le résultat :👇

![Image](https://www.freecodecamp.org/news/content/images/2021/08/YT-Thumbnail--4-.png)
_**élément racine est 40px**_

Maintenant, changez la taille de police `.text` à 2 rem : 👇

```css
html {
  font-size: 40px;
}

.text {
  font-size: 2rem;
}

/** Calculs
 2 rem * 40px = 80px
**/
```

Et vous pouvez voir le résultat : 👇

![Image](https://www.freecodecamp.org/news/content/images/2021/08/YT-Thumbnail--17-.png)
_**Le résultat**_

Puisque nous avons changé la taille de police racine à 40px, lorsque nous changeons la taille de police .text à 2 rem, nous obtenons 2*40 = 80px. 

# Comment créer des sites web responsives avec les unités REM

Créer des sites web responsives avec l'unité REM est très facile. Il suffit d'écrire vos styles en **unités rem** au lieu des pixels et de changer les éléments racine à différents points de rupture en utilisant des requêtes média.

Voici une démonstration qui vous montre comment cela se fait👇 et comment ajouter les requêtes média :

```css
// grand écran 

@media (max-width: 1400px) {
  html {
    font-size: 25px;
  }
}

// écran de tablette 

@media (max-width: 768px) {
  html {
    font-size: 18px;
  }
}

// écran mobile 

@media (max-width: 450px) {
  html {
    font-size: 12px;
  }
}
```

Maintenant, définissez la classe **.text** à 3 unités rem, comme ceci :

```css
.text{
	font-size : 3rem;
}
```

Et voici le résultat : 👇

![Image](https://www.freecodecamp.org/news/content/images/2021/08/final-1.gif)

#### Voici les calculs :

* Pour le grand écran  -> 3 rem * 25px = 75px
* Pour l'écran de tablette        -> 3 rem * 18px = 54px
* Pour l'écran mobile      -> 3 rem  * 12px = 36px
* Paramètre par défaut            -> 3rem * 16px = 48px

# Qu'est-ce que les unités EM ?

![Image](https://www.freecodecamp.org/news/content/images/2021/07/YT-Thumbnail--2-.png)

L'unité EM est la même que l'unité REM mais elle dépend de la **taille de police du parent**. Voici une démonstration. 👇

**Note** : assurez-vous de supprimer toutes les requêtes média.

```css
html {
  font-size: 16px;
}

.text {
  font-size: 3em;
}

/** Calculs
  la taille de police devrait être 
  3 em * 16px = 48px
**/

```

Voici le résultat : 👇

![Image](https://www.freecodecamp.org/news/content/images/2021/08/YT-Thumbnail--8-.png)

Maintenant, essayons d'ajouter un **remplissage de 3em** à la classe .text.

```css
html {
  font-size: 16px;
}

.text {
  font-size: 3em;
  padding: 3em;
}

/** Calculs
texte    => 3em * 16px = 48px
remplissage => 3em * 3em * 16px = 144px
**/
```

Au lieu d'avoir un remplissage de 48px, **nous obtenons un remplissage de 144px**. Comme vous pouvez le voir, il est **multiplié** par le nombre précédent. 

![Image](https://www.freecodecamp.org/news/content/images/2021/08/YT-Thumbnail--7-.png)
_**résultat du remplissage de 3em**_

Voici la partie calculée de la console de développement : 👇

![Image](https://www.freecodecamp.org/news/content/images/2021/08/ss.png)
_**remplissage de 3em à notre texte**_

### Ne pas utiliser l'unité EM 😵🔼

Utiliser l'unité EM **n'en vaut pas la peine** car :

* vous avez une forte chance de faire une erreur de calcul
* vous devez écrire beaucoup de code dans les requêtes média tout en essayant de rendre le site web responsive sur toutes les tailles d'écran
* c'est trop chronophage.

# Qu'est-ce que les unités VW ?

![Image](https://www.freecodecamp.org/news/content/images/2021/08/YT-Thumbnail--9--1.png)

La forme complète de VW est **viewport width**. Cela fonctionne comme l'**unité de pourcentage**. Spécifier **10vw** équivaut à occuper 10% de la largeur totale de l'écran visible.

Pour expérimenter avec les résultats, apportez ces modifications dans votre CSS👇

**Note** : commentez la dernière ligne de la classe .box.

```css
.text {
  display: none;
}

.box {
  width: 50vw;
  
  height: 300px;
  /* display: none; */
}
```

Si vous regardez attentivement, vous pouvez voir que **50vw signifie 50%**, ce qui couvrira la moitié de la largeur totale de l'écran.

Dans la partie JavaScript, décommentez cette ligne à la toute fin : 👇

```javascript
  // Box Width & height

  box.innerHTML = "Width : " + Box_width;
  
  // box.innerHTML = "Height : " + Box_height;
```

Le résultat ressemble à ceci :👇

![Image](https://www.freecodecamp.org/news/content/images/2021/08/YT-Thumbnail--11-.png)
_**50vw occupe 50% de la largeur de l'écran**_

Comme vous pouvez le voir, cet élément couvrira toujours cet espace même si nous redimensionnons la fenêtre

![Image](https://www.freecodecamp.org/news/content/images/2021/08/ttt.gif)
_**redimensionnement de la boîte qui fait 50vw de taille**_



# Qu'est-ce que les unités VH ?

![Image](https://www.freecodecamp.org/news/content/images/2021/08/YT-Thumbnail--10-.png)

La forme complète de VH est **viewport height**. Cela fonctionne comme l'**unité de pourcentage** également. Spécifier **10vh** équivaut à occuper 10% de la hauteur totale de l'écran visible.

Regardez cette démonstration pour voir comment cela fonctionne :👇

```css
.text {
  display: none;
}

.box {
  width: 300px;
  
  height: 50vh;
   /* display: none; */
}
```

Si vous regardez attentivement, vous pouvez voir que **50vh signifie 50%**, ce qui couvrira la moitié de la hauteur totale de l'écran.

Dans la partie JavaScript, décommentez cette ligne à la toute fin : 👇

```javascript
  // Box Width & height

  // box.innerHTML = "Width : " + Box_width;
  
  box.innerHTML = "Height : " + Box_height;
```

De plus, apportez ces modifications :👇

```javascript
  // Screen Size (Width & height)

  // size.innerHTML = "Width : " + Width + " px";
  size.innerHTML = "Height : " + Height + " px";
```

Et voici le résultat : 👇

![Image](https://www.freecodecamp.org/news/content/images/2021/08/YT-Thumbnail--21-.png)
_**50vh occupe 50% de la hauteur de l'écran**_

Comme vous pouvez le voir, cela couvrira toujours cet espace même si nous redimensionnons la fenêtre.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/gggg.gif)
_**redimensionnement de la boîte qui fait 50vh de taille**_

C'est tout ! 

# Conclusion

Félicitations ! Maintenant, vous pouvez utiliser en toute confiance les unités REM, EM, VW et VH pour créer des **sites web parfaitement responsives.**

Voici votre médaille 🎖🸏 pour avoir lu avec succès jusqu'à la fin. 💖🸏

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/yx020xpcqeh1wg30wc5c.png)


# Ressources supplémentaires

* [Tutoriel complet sur les requêtes média](https://www.freecodecamp.org/news/learn-css-media-queries-by-building-projects/)

%[https://youtu.be/HY8q4TD3KGM]

# Crédits

* Images de [Freepik](https://www.freepik.com/user/collections/rem/2273142) 

### Les suggestions et critiques sont grandement appréciées 💖🸏🸏

* [**YouTube** / JoyShaheb](https://www.youtube.com/c/joyshaheb)
* [**LinkedIn** / JoyShaheb](https://www.linkedin.com/in/joyshaheb/)
* [**Twitter** / JoyShaheb](https://twitter.com/JoyShaheb)
* [**Instagram** / JoyShaheb](https://www.instagram.com/joyshaheb/)