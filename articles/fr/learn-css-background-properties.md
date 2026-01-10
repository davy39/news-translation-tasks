---
title: Chaque propriété de fond CSS illustrée et expliquée avec des exemples de code
  🎖️
subtitle: ''
author: Joy Shaheb
co_authors: []
series: null
date: '2021-04-02T18:55:22.000Z'
originalURL: https://freecodecamp.org/news/learn-css-background-properties
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/FreeCodeCamp--1-.png
tags:
- name: CSS
  slug: css
- name: Web Design
  slug: web-design
seo_title: Chaque propriété de fond CSS illustrée et expliquée avec des exemples de
  code 🎖️
seo_desc: 'Today we''re gonna learn about every single CSS background property with
  every possible value. We''ll learn the short-hand, too. Let''s go !🏅

  Table of Contents


  All properties

  background-image

  background-size

  background-repeat

  background-position

  backg...'
---

Aujourd'hui, nous allons apprendre chaque propriété CSS **background** avec toutes les valeurs possibles. Nous allons également apprendre le **raccourci**. C'est parti !🏃

# Table des matières 

* [Toutes les propriétés](#heading-toutes-les-proprietes)
* [background-image](#background-image)
* [background-size](#background-size)
* [background-repeat](#background-repeat)
* [background-position](#background-position)
* [background-origin](#background-origin)
* [background-clip](#background-clip)
* [background-attachment](#background-attachment)
* [background-color](#background-color)
* [Raccourci](#raccourci)
* [Conclusion](#heading-conclusion)

Vous pouvez également regarder ce tutoriel sur YouTube si vous le souhaitez :

%[https://youtu.be/hwJKjsZUPjY]

# Toutes les propriétés

Voici une liste de **toutes les propriétés** que nous allons discuter aujourd'hui. Le texte en rouge à la fin est le **raccourci**.

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/l25y304vndphll4795hr.png)

## Que sont les propriétés de fond CSS ?

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/iic3rs5ewx8c9xp6vryq.png)

Les propriétés de fond CSS nous permettent de contrôler la taille et les propriétés des images afin que nous puissions créer des **images réactives** pour les petits et grands écrans. Cela nous aide à son tour à créer des sites web réactifs.

Par exemple,

* La propriété **background-size** nous permet de redimensionner la largeur et la hauteur de notre image en fonction de la taille de l'écran.
* **background-position** nous permet de dire au navigateur où placer l'image sur l'écran.

Et bien plus encore !

## Comment configurer le projet

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/u72rvfe5181640ikqa32.png)

Avant de coder, vous devez connaître un peu de HTML, CSS et savoir comment utiliser VS Code.

Pour tester les propriétés et leurs valeurs, suivez ces étapes 👍

1. Créez un nouveau dossier nommé 'PROJET-FOND'. Ouvrez-le dans VS Code.
2. Créez les fichiers `index.html` et `style.css`.
3. Installez 'live server' sur VS Code.
4. Démarrez le serveur live.

## HTML

Créez une div avec le nom de classe 'container' à l'intérieur de la **balise body** dans le fichier HTML.

```html
   <div class="container"></div>

```

## CSS

En CSS, vous **devez** inclure une hauteur pour le conteneur, sinon nous ne pourrons pas voir l'image. Dans notre cas, nous allons la définir à 100vh, comme ceci :

```css
.container{
  height : 100vh;
}

```

## Téléchargez les images pour le projet.

Les images sont sur mon **[dépôt GitHub](https://github.com/JoyShaheb/Project-image-repo/tree/main/Background-property-images)**. Voici comment les obtenir :

1. Visitez et copiez le lien ci-dessus ⬇️
2. Allez sur [downgit](https://minhaskamal.github.io/DownGit/#/home) et collez le lien que vous avez copié
3. Suivez les étapes dans cette vidéo 👍 

![Vidéo Down Git](https://cloud.githubusercontent.com/assets/5456665/17822364/940bded8-6678-11e6-9603-b84d75bccec1.gif)

Et..... nous sommes prêts !

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/nmf39ig7wzdiunfje9lr.png)

Commençons à coder 😊

# La propriété CSS background-image

En utilisant cette propriété, nous pouvons ajouter des images **dans toute notre feuille de style.**

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/rhoch2auowlf2xdf4h8f.png)

Nous écrivons la syntaxe après avoir écrit le nom du sélecteur, comme ceci :👍

```css
.container{
// Nous mettrons le chemin/URL de l'image 👍 à l'intérieur des guillemets
   background-image  :  url(' ');
}
```

Nous pouvons utiliser background-image de **2 manières** :

* En localisant le **chemin de l'image** dans le répertoire
* En spécifiant l'**URL de l'image**

### Comment utiliser `background-image` via le chemin du répertoire

Voici la syntaxe pour background-image lors de l'utilisation du chemin du répertoire 👍

```css
.container{
//  Mettez le chemin de l'image 👍 à l'intérieur des guillemets
  background-image: url(' ');
}
```

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/1jfuda4p0ki1hish775o.png)

Il y a trois cas où vous devrez spécifier un chemin d'image dans notre CSS :

1. Lorsque `image` et `style.css` sont dans le même dossier
2. Lorsque `image` est dans le dossier suivant
3. Lorsque `image` est dans le dossier précédent

Lorsque `image` et `style.css` sont dans le **même dossier**, cela ressemble à ceci. 👍 

Remarquez que **`kitty.png`** et **`style.css`** sont dans le même dossier parent nommé **Background-project** :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Frame-25--1--1.png)

Pour localiser le chemin du fichier `kitty.png`, écrivez le code suivant dans `style.css` :

```css
 .container{
   background-image : url("kitty.png");
   
   height: 100vh;
// définir la taille et arrêter la répétition de l'image 
   background-repeat : no-repeat;
   background-size : contain;
 }

```

Lorsque l'image est dans le **dossier suivant**, `style.css` est dans le dossier précédent. Remarquez sur l'image ci-dessous que `kitty.png` est dans le dossier Assets tandis que `style.css` est dans le dossier précédent.

![Texte alternatif](https://www.freecodecamp.org/news/content/images/2021/04/Frame-26.png)

Pour avancer et localiser le chemin du fichier `kitty.png`, nous écrivons un point et une barre oblique comme ceci (./) après la guillemet dans `style.css`. Ensuite, nous écrivons le nom du dossier puis une barre oblique (/) et enfin nous écrivons le nom de l'image, comme ceci :👍 

```css
 .container{
   background-image : url("./Assets/kitty.png");

   height: 100vh;
// définir la taille et arrêter la répétition de l'image 
   background-repeat : no-repeat;
   background-size : contain;
 }

```

Si l'image est dans le **dossier précédent**, alors nous devons revenir en arrière. Remarquez sur l'image ci-dessous👍 que `style.css` est dans le dossier **src** et `kitty.png` est **en dehors du dossier src.**

![Texte alternatif](https://www.freecodecamp.org/news/content/images/2021/04/Frame-27.png)

Pour revenir en arrière et localiser le chemin du fichier `kitty.png`, nous écrivons deux points et une barre oblique (../) après la guillemet dans `style.cs`. Ensuite, nous écrivons le nom de l'image, comme ceci : 👍

```css
 .container{
   background-image : url("../kitty.png");

   height: 100vh;
// définir la taille et arrêter la répétition de l'image 
   background-repeat : no-repeat;
   background-size : contain;
 }

```

### Comment utiliser `background-image` par lien direct

C'est assez facile. Écrivez la propriété et insérez le lien à l'intérieur de `url()`. 

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/szxp3jqyjyksrep1ep82.png)

Pour travailler avec une image qui est un **lien direct**, nous devons écrire le code suivant :

```css
//exemple ->
 .container{
    background-image : url("https://dev-to-uploads.s3.amazonaws.com/uploads/articles/szxp3jqyjyksrep1ep82.png");

  height: 100vh;
// définir la taille et arrêter la répétition de l'image 
   background-repeat : no-repeat;
   background-size : contain;
 }

```

### Faites une pause

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/4diremjrrbvcm2o4l77m.png)

# La propriété CSS background-size

Nous pouvons ajuster la taille d'une image en utilisant la propriété `background-size`.

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/xxbrgckb20fy8tmrg9ik.png)

Nous écrivons la syntaxe après avoir écrit le nom du sélecteur, comme ceci 👍

```css
.container{
// Nous écrirons les valeurs 👍 ici
  background-size  : cover;
}
```

Vous pouvez utiliser background-size de **3 manières** :

* utiliser la valeur Cover / Contain
* définir la largeur et la hauteur de l'image
* utiliser auto

Commençons par discuter des **valeurs cover et contain**. 🐻 Taille : [718px X 614px]

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/uixn5c8mrafpmlhth9iy.png)

### Valeur Cover

Pour que cela fonctionne, nous devons inclure une image, définir la hauteur et arrêter la répétition de l'image. Nous faisons cela comme ceci en CSS : 👍

```css
.container{
  background-image : url('cute-bear.png');
  background-repeat: no-repeat;
  background-size : cover;

// Doit inclure la hauteur
  height : 100vh;
}

```

Lorsque nous utilisons cette propriété, elle étirera l'image à tout l'écran même lorsque nous redimensionnons la fenêtre. Regardez la vidéo ci-dessous pour voir à quoi cela ressemble :👍

![Cover](https://media.giphy.com/media/9OdZ0B1wjO1kdofBBu/giphy.gif)

### La valeur contain

Mêmes étapes ici – nous devons inclure une image, définir sa hauteur et arrêter la répétition de l'image comme ceci :👍

```css
.container{
  background-image : url('cute-bear.png');
  background-repeat: no-repeat;
  background-size : contain;

// Doit inclure la hauteur
  height : 100vh;
}

```

Cette valeur préservera la taille de l'image [Image Réactive] même lorsque nous redimensionnons la fenêtre. Consultez cette vidéo ci-dessous pour voir comment cela fonctionne : 👍

![Contain](https://media.giphy.com/media/VaqDcSh38DTz7YbV6p/giphy.gif)

### Largeur et hauteur de l'image

Nous pouvons définir la largeur et la hauteur de l'image en utilisant la propriété background-size.

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/36p9azoztkvawbvy6244.png)

Voici la syntaxe en CSS : 👍

```css
.container{
// ici, nous voyons la largeur👍 & 👍 la hauteur
  background-size : 200px   200px;
}

```

N'oubliez pas non plus d'insérer l'image, de définir sa hauteur et d'arrêter la répétition de l'image. L'extrait de code ressemble à ceci : 

```css
.container{
  background-image : url('cute-bear.png');
  background-repeat: no-repeat;

// ici, nous voyons la largeur👍 & 👍 la hauteur
  background-size : 200px  200px;

// Doit inclure la hauteur
  height : 100vh;
}

```

### Redimensionnement automatique

Lorsque vous utilisez cette valeur, l'image restera à sa taille d'origine. Elle ne changera pas lorsque nous redimensionnons la fenêtre. Cela ressemble à ceci :

![Image](https://media.giphy.com/media/hHc7ZhU7BB4NX8gLRR/giphy.gif)

# La propriété CSS background-repeat

Cette propriété nous permet de répéter la même image plusieurs fois.

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/629rnxirqrdr8p5fapcd.png)

Nous écrivons la syntaxe après avoir écrit le nom du sélecteur, comme ceci 👍

```css
.container{
// nous changerons les valeurs 👍 ici
  background-repeat : repeat;
}
```

Cette propriété a six valeurs :

* repeat
* repeat-x
* repeat-y
* no-repeat
* space
* round

Voici les résultats de chacune de ces six valeurs en un coup d'œil. Notez que la taille du kitty dans ces exemples est [200px X 200px].

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/jj2jwfwh0pboqpylkeq0.png)

![Round](https://media.giphy.com/media/3BUBxpCxmcDrBN4aZF/giphy.gif)

![Space](https://media.giphy.com/media/cO0jNSpVi0I3FWD62G/giphy.gif)

Maintenant, examinons ce qui se passe avec chaque valeur. MAIS, avant cela, notez que nous devons insérer une image en utilisant la propriété `background-image`, comme ceci :

```css
.container{
   background-image : url('kitty.png');
   background-size : 200px 200px;
   background-repeat :  ; // nous jouerons avec les valeurs ici 

   height : 100vh;
}

```

### La valeur repeat

En utilisant cette valeur, nous pouvons répéter la même image plusieurs fois le long des **axes X et Y** tant que l'espace de l'écran ne se termine pas. Ici, la taille du kitty est de 200px x 200px.

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/26zsa1dn161pawjqxuqp.png)

Pour dupliquer ce résultat, nous écrivons ->

```css
.container{
   background-image : url('kitty.png');
   background-size : 200px 200px;
   background-repeat : repeat;

   height : 100vh;
}
```

### La valeur repeat-x

Cette valeur nous permet de répéter la même image plusieurs fois le long de l'**axe X** tant que l'espace de l'écran ne se termine pas. Taille du kitty : 200px X 200px.

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/pl4znzrwcevpr5w1a4i5.png)

Pour obtenir ce résultat, nous écrivons ->

```css
.container{
   background-image : url('kitty.png');
   background-size : 200px 200px;
   background-repeat : repeat-x;

   height : 100vh;
}
```

### La valeur repeat-y

Celle-ci fonctionne de la même manière que "repeat-x", mais fonctionne le long de l'**axe Y** tant que l'espace de l'écran ne se termine pas. Taille du kitty : 200px X 200px.

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/7yo3i3bp8cw2r6zqhtvm.png)

Pour obtenir ce résultat, nous écrivons ->

```css
.container{
   background-image : url('kitty.png');
   background-size : 200px 200px;
   background-repeat : repeat-y ;

   height : 100vh;
}
```

### La valeur no-repeat

Nous pouvons avoir notre image originale sans répétition en utilisant cette valeur. Taille du kitty : 200px X 200px.

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/p2okgurnuakrnqbyv6kr.png)

Pour obtenir ce résultat, nous écrivons ->

```css
.container{
   background-image : url('kitty.png');
   background-size : 200px 200px;
   background-repeat : no-repeat ; 

   height : 100vh;
}
```

### La valeur space

Cela fonctionne à la fois le long des axes X et Y. Nous pouvons voir la principale différence entre les valeurs **space et round** lorsque nous redimensionnons la fenêtre. Remarquez que nous avons des **espaces vides** lorsque nous redimensionnons la fenêtre :

![Space](https://media.giphy.com/media/cO0jNSpVi0I3FWD62G/giphy.gif)

Pour expérimenter avec cette valeur, écrivez ->

```css
.container{
   background-image : url('kitty.png');
   background-size : 200px 200px;
   background-repeat : space ;

   height : 100vh;
}
```

### La valeur round

Cela fonctionne à la fois le long des axes X et Y. Remarquez que l'image est **étirée** lorsque nous redimensionnons la fenêtre.

![Round](https://media.giphy.com/media/3BUBxpCxmcDrBN4aZF/giphy.gif)

Suivez et écrivez ->

```css
.container{
   background-image : url('kitty.png');
   background-size : 200px 200px;
   background-repeat : round ; 

   height : 100vh;
}
```

# La propriété CSS background-position

Cette propriété est utilisée pour changer la position d'une image sur l'écran.

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/j4ndvr71f0yl9c44kbc7.png)

Voici la syntaxe : 👍

```css
.container{
// Ceci est l'axe X👍 & l'axe Y👍
background-position : 300px  200px;
}

```

N'oubliez pas non plus d'insérer l'image, de définir sa hauteur et d'arrêter la répétition de l'image. Nous avons défini la taille du kitty à 200px X 200px en utilisant la propriété `background-size` :

```css
.container{
  background-image: url("kitty-idea.png");
  background-size: 200px 200px;
  background-repeat: no-repeat;

// Ceci est l'axe X👍 & l'axe Y👍
  background-position : 300px 200px;
  height: 100vh;
}

```

Et voici le résultat :

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/65p2htkztmijbm1hxlug.png)

Vous pouvez également utiliser une combinaison de ces valeurs :

* top
* left
* right
* bottom
* valeurs en pourcentage

Par exemple, plaçons notre kitty en bas à droite. Voici l'extrait de code pour cela :

```css
.container{
  background-image: url("kitty-idea.png");
  background-size: 200px 200px;
  background-repeat: no-repeat;

// Ceci est l'axe X👍 & l'axe Y👍
  background-position : bottom right;
  height: 100vh;
}

```

Et voici le résultat :

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ga6veuh8ea3yzq7nend2.png)

En calculant l'espace disponible de l'écran, les valeurs en % déterminent la position de l'image. Voici à quoi cela ressemble en code :

```css
.container{
  background-image: url("kitty-idea.png");
  background-size: 200px 200px;
  background-repeat: no-repeat;

// Ceci est l'axe X👍 & l'axe Y👍
  background-position : 25% 15%;
  height: 100vh;
}

```

Et voici le résultat :

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/fazbxgdpkqeomum02qv7.png)

# La propriété CSS background-origin

Cette propriété nous permet de définir l'origine de notre image à travers le modèle de boîte CSS.

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/wc2b6ypgcfdtol6am14g.png)

Nous écrivons la syntaxe après avoir écrit le nom du sélecteur, comme ceci 👍

```css
.container{
// Nous écrirons les valeurs 👍 ici
  background-origin: border-box;
}
```

Ses quatre valeurs sont :

* border-box
* padding-box
* content-box
* inherit

Dans le modèle de boîte CSS standard, la partie la plus externe est la bordure. Ensuite vient le remplissage et enfin nous avons le contenu lui-même au centre.

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/p3mdn6hpd1u892akrkj5.png)

Voici le résultat de chaque propriété en un coup d'œil :

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/27ptyulhvxqi4idrw68n.png)

Pour recréer ces résultats :

* Tout d'abord, nous avons besoin d'une image, nous devons arrêter la répétition de l'image et définir la hauteur et la largeur **du conteneur et de l'image.**
* Une fois cela fait, nous insérerons 40px de remplissage, sinon nous ne pourrons pas voir la différence entre la boîte de remplissage et la boîte de contenu.
* Ensuite, insérez une bordure rouge de 25px. Définissez le style de bordure sur dashed pour obtenir une **bordure en pointillés** sur l'écran.
* définissez la taille de fond à 400px & 400px

Voici à quoi cela ressemble en code :

```css
.container{
  background-image: url('cute-girl.png');
  background-repeat: no-repeat;
  background-size: 400px 400px;

// Changez les valeurs ici 👍 pour voir la différence 
  background-origin: border-box;
  padding: 40px;
  border: 25px solid red;
  border-style: dashed;

// Largeur & hauteur pour le conteneur 👍
  width : 400px;
  height : 400px;
}

```

### Faites une pause

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/yahewko7hckdgp7p4xux.png)

# La propriété CSS background-clip

Cela est identique à la propriété `background-origin`. La principale différence est que `background-clip` **COUPE** l'image pour qu'elle s'adapte à l'intérieur de la boîte, tandis que `background-origin` **POUSSE** le contenu à l'intérieur de la boîte pour qu'il s'adapte.

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/r4ga97rke3kgppd7qlxn.png)

Nous écrivons la syntaxe après avoir écrit le nom du sélecteur, comme ceci 👍

```css
.container{
// Nous écrirons les valeurs 👍 ici
  background-clip  : border-box;
}
```

Ses quatre valeurs sont :

* border-box
* padding-box
* content-box
* inherit

Voici le résultat de chaque propriété en un coup d'œil :

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/xgd6sh8237bmvpnujl8r.png)

Pour recréer ces résultats :

* Tout d'abord, nous avons besoin d'une image, nous devons arrêter la répétition de l'image et nous devons définir la hauteur et la largeur **du conteneur et de l'image.**
* Une fois cela fait, nous insérerons 40px de remplissage, sinon nous ne pourrons pas voir la **différence** entre la boîte de remplissage et la boîte de contenu.
* Ensuite, insérez une bordure rouge de 25px. Définissez le style de bordure sur dashed pour voir la **bordure en pointillés** sur l'écran.
* Définissez la taille de fond à 400px & 400px

Le code ressemble à ceci :

```css
.container{
  background-image: url('cute-girl.png');
  background-repeat: no-repeat;
  background-size: 400px 400px;

// Changez les valeurs ici 👍 pour voir la différence 
  background-clip: border-box;
  padding: 40px;
  border: 25px solid red;
  border-style: dashed;

// Largeur & hauteur pour le conteneur 👍
  width : 400px;
  height : 400px;
}

```

# La propriété CSS background-attachment

Cette propriété nous permet de contrôler le comportement de notre contenu et de notre image **lorsque nous faisons défiler.**

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/n1xx67vtt5w3c861sskx.png)

Nous écrivons la syntaxe après avoir écrit le nom du sélecteur, comme ceci 👍

```css
.container{
// Nous changerons les valeurs 👍 ici
background-attachment: scroll;
}
```

Ses trois valeurs sont :

* scroll
* fixed
* local

Lorsque nous utilisons **scroll**, l'image est fixe et nous pouvons faire défiler librement notre contenu. La valeur **fixed** nous donne un effet de parallaxe lors du défilement de la souris et **local** produit plusieurs images tant que notre contenu ne se termine pas.

Vous pouvez voir les résultats en direct ici 👍

%[https://codepen.io/ematte/pen/GRjJjro]

[Voici où j'ai obtenu ce stylo](https://dev.to/hadrysmateusz/learn-all-8-background-css-properties-in-5-minutes-2lk4).

# La propriété CSS background-color

Vous pouvez utiliser cette propriété pour remplir votre fond avec une couleur.

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/mh7pe7phpj2vrvz304ma.png)

Nous écrivons la syntaxe après avoir écrit le nom du sélecteur, comme ceci 👍

```css
.container{
// nous changerons les valeurs 👍 ici
   background-color :  red;
}
```

Parmi les nombreuses options, les plus populaires sont :

* Couleur unie par nom ou valeur hexadécimale
* Utilisation de la fonction de couleur `RGB()`
* Utilisation de la fonction `linear-gradient()`

### Comment obtenir une couleur de fond unie par nom ou valeur hexadécimale

Vous pouvez utiliser des noms de couleurs pour définir la couleur de fond, comme ceci :

```css
.container{
   background-color : red;

   height : 100vh;
}

```

Ou, vous pouvez utiliser un code de couleur hexadécimale comme ceci :

```css
.container{
   background-color : #ff0000; // couleur rouge

   height : 100vh;
}

```

Vous pouvez consulter ces ressources pour plus de couleurs :

* [coolors.co](https://coolors.co/)
* [flatuicolors.com](https://flatuicolors.com/)

### Comment utiliser la fonction de couleur RBG() pour définir la couleur de fond

Vous pouvez utiliser la fonction de couleur `RGB()` pour définir la couleur de fond comme ceci :

```css
.container{
// le nom de la couleur est "American River"
   background-color : rgb(99, 110, 114);

   height : 100vh;
}

```

Ou, vous pouvez utiliser `RGBA()` pour définir à la fois la couleur et l'opacité comme ceci :

```css
.container{
// Le 0.5 à la fin représente 50% 👍 d'opacité 
   background-color :  rgba(99, 110, 114, 0.5);

   height : 100vh;
}

```

Ceci est une expérience avec la couleur nommée 'Eton blue' avec divers niveaux d'opacité : 👍

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/yzc82sudq8es7ocok12g.png)

### Comment définir la couleur de fond avec la fonction linear-gradient()

Vous pouvez utiliser cette fonction pour créer une couleur de dégradé de plus d'une couleur. Voici quelques exemples de couleurs de dégradé :

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/f0j3e3r6kobycowckdxg.png)

Vous pouvez visiter [ce site web](https://uigradients.com/#Summer) pour plus de ressources de couleurs avec des extraits de code CSS.

Recréons cette couleur de fond :

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/jkf21o97m7gqzpme810k.png)

'#22c1c3' représente la couleur à gauche, et '#fdbb2d' représente la couleur à droite. '90deg' nous indique comment les deux couleurs seront inclinées pour créer un dégradé.

L'extrait de code ressemble à ceci :

```css
.container{
 
   background: linear-gradient(90deg, #22c1c3, #fdbb2d);  

   height : 100vh;
}

```

# Le raccourci pour ces propriétés CSS

Voici l'ordre du raccourci pour les propriétés de fond :

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/newvcc4rvegnbkblwzyb.png)

Pour cette expérience, plaçons `kitty.png` dans notre navigateur avec un fond bleu à 200px sur l'axe X et 200px sur l'axe Y. L'extrait de code ressemble à ceci :

```css
.container{
 
   background-color : skyblue;
   background-image : url('kitty.png);
   background-repeat: no-repeat;
   background-attachment: fixed;
   background-position: 200px 200px;

   height : 100vh;
}

```

Et voici l'extrait de code utilisant le raccourci :

```css
.container{
 
   background: skyblue url('kitty.png) no-repeat fixed 200px 200px;

   height : 100vh;
}

```

Ce raccourci nous fait vraiment gagner du temps. Si vous souhaitez sauter une valeur, vous pouvez le faire tant que vous maintenez l'ordre de ces propriétés.

# Conclusion

Voici votre médaille pour avoir lu jusqu'à la fin ❤️

Les suggestions et critiques sont grandement appréciées ❤️

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/i/usxsz1lstuwry3jlly4d.png)

### Crédits

* [Jolie fille sur laquelle j'ai un crush 🥰](https://www.pexels.com/photo/woman-lying-on-plants-2125610/)
* [Avatar kitty](https://www.flaticon.com/packs/kitty-avatars-3)
* [Panda mignon](https://www.freepik.com/free-vector/cute-bear-is-happy-cartoon-illustration_12341167.htm#position=4)
* [Chat mignon avec canard](https://www.freepik.com/free-vector/set-happy-cute-cats-cartoon-illustration_12566295.htm#position=11)
* [Illustration de fille mignonne](https://www.freepik.com/free-vector/young-girl-different-gestures-cartoon-illustration_12566309.htm#page=1&position=22)
* [Lapin avec canard](https://www.freepik.com/free-vector/set-cute-rabbit-with-duck-feel-happy-sad-cartoon-illustration_12573654.htm#position=7)
* [CSS-Tricks](https://css-tricks.com/almanac/properties/b/background/)

**YouTube [/ Joy Shaheb](https://youtube.com/c/joyshaheb)**

**Twitter [/ JoyShaheb](https://twitter.com/JoyShaheb)**

**Instagram [/ JoyShaheb](https://www.instagram.com/joyshaheb/)**