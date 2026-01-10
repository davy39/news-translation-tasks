---
title: 'Comment créer une affiche pour Avengers: Infinity War en HTML et CSS'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-13T19:10:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-a-poster-for-avengers-infinity-war-in-html-and-css-304d305c7f7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*bKfG0yasGD590ClJBKDetQ.jpeg
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: 'tech '
  slug: tech
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: 'Comment créer une affiche pour Avengers: Infinity War en HTML et CSS'
seo_desc: 'By Kunal

  In this post, we are going to make a movie poster of “Avengers: Infinity War” in
  HTML and CSS.

  Here’s what we will build:


  Looks interesting, doesn’t it?

  Here are some important concepts you will learn while making this poster:


  How to give ...'
---

Par Kunal

Dans cet article, nous allons créer une affiche de film pour « Avengers: Infinity War » en HTML et CSS.

Voici ce que nous allons construire :

![Image](https://cdn-media-1.freecodecamp.org/images/1*bKfG0yasGD590ClJBKDetQ.jpeg)

Cela semble intéressant, n'est-ce pas ?

Voici quelques concepts importants que vous apprendrez en créant cette affiche :

* Comment donner une image de fond plein écran à votre page
* Centrer des éléments horizontalement en CSS
* Centrer des éléments verticalement en CSS
* Intégrer des vidéos YouTube en HTML
* Qu'est-ce que l'effondrement des marges (Margin Collapse)
* Comment charger des polices personnalisées à partir d'un fichier local
* Comment charger des polices depuis Google Fonts

Cela va être amusant, alors plongeons-nous.

### La page blanche

Commençons par nous mettre sur la même page.

Voici à quoi ressemble la structure de mon dossier de projet :

![Image](https://cdn-media-1.freecodecamp.org/images/1*SHnVL-WZQ0muKIKwoo1lWQ.jpeg)

Notre feuille de style « styles.css » va dans le dossier CSS, le fichier de police personnalisée que nous allons télécharger ira dans le dossier fonts, l'image de fond que nous allons télécharger ira dans le dossier img, et notre code HTML réside dans le fichier « infinity-war.html ».

Voici mon fichier HTML pour une page blanche. Nous allons construire sur cette page blanche :

Si vous ne comprenez pas le code ci-dessus, alors vous codez probablement en HTML pour la première fois. Je vous recommande de commencer ici : [Comment faire un burger en HTML — Un tutoriel pour débutants](https://medium.com/frontendshortcut/how-to-make-a-burger-in-html-a-beginner-tutorial-dca7b4b0a179).

### Image de fond pleine page

Tout d'abord, téléchargez l'[image](http://hdqwalls.com/wallpapers/avengers-infinity-war-2018-4k-cq.jpg) et enregistrez-la dans le dossier « img ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*YhsGz4lXux0XEYL2NZkQJQ.jpeg)

Remarque : Tous les droits de l'image appartiennent à Marvel Studios, utilisés ici uniquement à des fins d'apprentissage.

Nous utilisons normalement l'élément `<img>` pour inclure des images en HTML. Mais pour ce cas spécifique, nous allons créer une div, faire en sorte que cette div couvre tout l'écran, puis définir l'image de fond sur cette div en utilisant la propriété CSS « background-image ».

Voici notre HTML :

et notre CSS :

Comme vous pouvez le voir, nous avons créé une div et lui avons donné une classe dans notre fichier HTML. Dans notre fichier CSS, nous avons défini la largeur et la hauteur à 100 % afin qu'elle couvre tout l'écran. Nous avons défini l'image de fond en utilisant la propriété « background-img ».

Remarquez comment nous référençons le fichier image : `url("../img/infinity-war-wallpaper.jpg")`. Vous voyez ce `..` au début du chemin ? Voyez-vous, nous référençons le fichier image qui se trouve dans le dossier « img » depuis notre fichier styles.css qui se trouve dans le dossier « css », n'est-ce pas ?

Nous devons donc sortir d'un dossier et ensuite référencer le chemin. Ce `..` nous fait remonter d'un dossier dans la structure des dossiers.

Actualisons la page dans le navigateur et voyons le résultat.

Et, c'est toujours une page blanche.

En fait, nous avons oublié un détail ici.

Lorsque nous définissons la hauteur ou la largeur en %, disons 100 % dans notre cas, ce n'est pas 100 % de l'écran — c'est 100 % de la dimension de son parent.

Quel est l'élément parent de la div ? `<body>`. Quel est l'élément parent de `<body>` ? `<html>`.

Nous devons donc définir la hauteur de nos éléments body et HTML à 100 %. Faisons cela et voyons si cela fonctionne :

Maintenant, nous obtenons cette sortie :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ox5E8h7eEJyVs3moBMQy7Q.jpeg)

D'accord, si vous regardez attentivement, vous verrez qu'il y a deux problèmes ici :

* il y a un espace blanc autour de l'image — vous le voyez ?
* l'image est zoomée, n'est-ce pas ?

Occupons-nous de ces problèmes un par un.

L'élément body a par défaut une certaine marge. C'est pourquoi nous voyons cet espace autour de l'image.

Supprimons la marge en la définissant à 0 sur le body :

Actualisez le navigateur et vous verrez que l'espace blanc a disparu et qu'il n'y a plus de barre de défilement.

Ensuite, résolvons le problème de mise à l'échelle de l'image. Par défaut, l'image sera affichée dans sa taille d'origine. Nous pouvons changer cela pour mettre à l'échelle l'image de manière à ce qu'elle couvre l'écran en définissant la propriété « background-size » à « cover ».

Nous définissons également la position de fond pour centrer l'image de fond.

Les deux problèmes sont résolus.

### Effondrement des marges (Margin Collapse)

Ajoutons un titre en utilisant l'élément `<h1>` et donnons-lui une couleur blanche en utilisant la propriété « color » en CSS :

et notre CSS :

Sortie :

![Image](https://cdn-media-1.freecodecamp.org/images/1*epGPR0ycthJ6PyrYJ3bEQg.jpeg)

Nous avons fait une erreur. D'où vient cet espace blanc ?

Eh bien, il s'avère que l'élément h1, tout comme l'élément body, a également une certaine marge par défaut, et il en va de même pour les éléments h2, h3, h4, h5 et h6.

Mais, même si l'élément h1 avait une marge, il doit être affiché avec un certain espace à l'intérieur de la div avec notre image de fond. Alors pourquoi a-t-il affiché un espace à l'extérieur de la div ?

Idéalement, il aurait dû être affiché comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*XOd5CXCEZbEbMAmpZrGFSw.jpeg)

Mais il affiche plutôt un espace au-dessus de la div « full-bg ».

Cela se produit à cause de l'effondrement des marges (Margin Collapsing).

Lorsque vous avez deux éléments de bloc (la div et h1 dans notre cas), et que l'élément parent n'a pas de remplissage ou de bordure, alors la marge supérieure et inférieure de l'élément enfant seront affichées comme la marge supérieure et inférieure du parent. Cela s'appelle l'effondrement des marges. La marge de l'enfant s'effondre avec la marge du parent.

Si l'élément parent a un remplissage même d'un seul pixel, ou a une bordure d'au moins 1 pixel, alors cela ne se produira pas. Donnons un remplissage de 1px à notre div « full-bg » et voyons son effet :

L'effondrement des marges est corrigé.

Mais — avez-vous remarqué une petite différence ?

Votre navigateur a maintenant une barre de défilement horizontale et verticale. Cela signifie que la largeur et la hauteur de la div ont augmenté.

Comment ?

### Le remplissage et la bordure augmentent la taille de l'élément

C'est un autre comportement par défaut que vous devez retenir. Supposons que vous créez une div de 100px x 100px, et que vous lui donnez un remplissage de 10px. La div deviendra alors 110px x 110px.

Oui, la quantité de remplissage que vous donnez à un élément est ajoutée à la dimension de l'élément. Il en va de même pour la bordure : si vous donnez une bordure de 4px à votre élément, sa taille augmentera de 4px.

Idéalement, nous ne voulons pas augmenter la taille de l'élément, mais plutôt réduire le contenu à l'intérieur de l'élément pour faire de la place pour le remplissage et la bordure.

Nous pouvons y parvenir en définissant la propriété « box-sizing » à « border-box ». Faisons cela :

Actualisez votre navigateur. Bam, les barres de défilement ont disparu.

### Section et en-tête

Si vous avez vu l'image du résultat final, vous verrez que nous devons encore ajouter un sous-titre, une vidéo YouTube et la date de sortie. Il est bon de regrouper tous ces éléments dans une section, puisque ces éléments sont liés les uns aux autres. Créons une section en utilisant la balise `<section>` et plaçons notre h1 à l'intérieur :

Tous les éléments de notre affiche iront à l'intérieur de cette section « poster-content ».

Vous vous demandez peut-être pourquoi nous n'avons pas utilisé « div » ici — pourquoi « section » ?

En fait, avant HTML5, tout était « div ». En fait, nous pouvons faire des sites web entiers avec seulement des éléments « div ». Mais nous ne faisons pas cela parce qu'il est plus logique d'inclure une image avec l'élément `<img>`, il est plus logique d'inclure un paragraphe avec l'élément `<p>`, et de même, il est plus logique de regrouper le contenu de thème similaire dans l'élément `<section>`.

Donc, la règle de base est, utilisez `<div>` lorsque vous voulez un conteneur uniquement pour donner du style au contenu (comme notre div « full-bg »), et utilisez `<section>` lorsque vous voulez un conteneur pour regrouper du contenu de thème similaire.

Ensuite, nous savons aussi qu'il y aura un sous-titre. Heureusement, HTML5 a un élément pour regrouper les éléments de titre — l'élément `<header>`. Incluons cela aussi :

Nous devons également mettre à jour les sélecteurs dans notre CSS :

Maintenant, dès que vous actualisez, vous remarquerez que la police de notre élément h1 devient plus petite.

De nombreux navigateurs réduisent la taille de la police de l'élément h1 lorsqu'il est placé à l'intérieur d'un élément `<section>` ou `<article>`. Il est donc préférable de donner la taille à notre h1 manuellement chaque fois qu'il est placé à l'intérieur de `<section>` ou `<article>` :

### Fond transparent

Donnons une couleur de fond noire semi-transparente à notre élément section :

Sortie :

![Image](https://cdn-media-1.freecodecamp.org/images/1*PsSzEft5rpXHqW8fwf1yNw.jpeg)

Le code « rgba(0, 0, 0, 0.6) » signifie : couleur avec 0 composante rouge, 0 composante verte et 0 composante bleue, ce qui est noir, et 60 % d'opacité.

Deux choses : nous ne voulons pas que le texte colle aux bords de la boîte semi-transparente. Deuxièmement, nous voulons donner à la section une largeur fixe et l'aligner au centre.

Faisons cela :

Nous avons donné un remplissage de « 16px » et défini le « box-sizing » à « border-box » parce que nous ne voulons pas que le conteneur s'étende de 16px pour faire de la place pour le remplissage. Nous voulons plutôt que le conteneur reste de la même taille et que le contenu à l'intérieur se rétrécisse pour faire de la place pour 16px de remplissage.

Sortie :

![Image](https://cdn-media-1.freecodecamp.org/images/1*kh-fqa4y3Za8fqZYuhIDGw.jpeg)

D'accord, les espaces en haut et en bas ne ressemblent certainement pas à « 16px » — ils semblent beaucoup plus grands. Et si vous avez remarqué, la section ne touchait pas le bord supérieur du navigateur avant, mais maintenant elle le touche. Que se passe-t-il ?

C'est encore l'effondrement des marges qui entre en jeu. L'espace supplémentaire au-dessus et en dessous de h1 n'est pas le remplissage de la section, c'est la marge de h1. Auparavant, nous n'avions pas de remplissage sur la section, donc la marge de h1 et de la section s'est effondrée et a été affichée à l'extérieur de la section. C'est pourquoi la section ne touchait pas le haut avant.

Réduisons la marge de h1 et centrons-le en définissant « text-align: center » pour notre élément `<header>` :

Actualisez la page et le texte h1 devrait maintenant être centré avec relativement moins d'espace autour.

### Flex pour centrer les éléments

Notre section est déjà centrée horizontalement, grâce à « margin: auto ».

Ce que fait « margin: auto », c'est qu'il définit les marges de tous les côtés (margin-top, margin-right, margin-bottom et margin-left) à « auto ».

Nous savons que la définition de margin-left et margin-right à « auto » centre l'élément horizontalement.

Mais la définition de margin-top et margin-bottom à « auto » ne centre pas automatiquement un élément verticalement. Historiquement, centrer les éléments en HTML a été l'un des grands moments d'arrachement de cheveux pour les développeurs web.

Ce n'est plus le cas. Maintenant que Flexbox est largement supporté par tous les navigateurs, nous pouvons utiliser « display: flex » sur un élément. Cet élément deviendra un « conteneur flex » et ses enfants deviendront des « éléments flex ».

Les éléments flex ont certaines propriétés intéressantes. Par exemple, lorsque les marges supérieure et inférieure des éléments flex sont définies à « auto », cela centre verticalement !

Essayons, ajoutons « display: flex » à « .full-bg » :

Sortie :

![Image](https://cdn-media-1.freecodecamp.org/images/1*l_d0FkGBckGqp4k6nv1z9w.jpeg)

D'accord, maintenant cela commence à avoir l'air bien.

### Charger une police personnalisée depuis le système local

Si nous voulons vraiment que cela ait l'air cool, nous aurons besoin d'une police personnalisée pour notre en-tête.

Jetez un coup d'œil à cette police sur « dafont.com » :

![Image](https://cdn-media-1.freecodecamp.org/images/1*_H1Wq3Uz5EKQaMUDghP7hQ.jpeg)

Cela semble parfait pour notre utilisation, vous pouvez donc la télécharger [ici](https://www.dafont.com/avengeance.font).

Si vous extrayez le fichier zip, vous verrez des fichiers de police au format TTF et OTF. Nous pouvons les utiliser, mais le format WOFF est la meilleure solution lorsque vous utilisez une police personnalisée pour CSS. Allez-y et convertissez l'un des fichiers TTF en WOFF en utilisant cet outil en ligne [tool](https://onlinefontconverter.com/).

Ensuite, nous placerons le fichier .woff converti à l'intérieur du répertoire « fonts ».

Chargeons notre police :

Remarque : Si vous utilisez Firefox, vous devrez autoriser le chargement des fichiers de police locaux. Tapez about:config dans la barre d'adresse de Firefox et appuyez sur Entrée. Acceptez l'avertissement. Ensuite, recherchez « strict_origin_policy » et mettez-le à false.

Sortie :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ocd8cEcW2fNHGidZYawjHg.jpeg)

Très bien, maintenant nous parlons.

### Stylisation de l'en-tête

Maintenant, écrivons « Infinity War » comme un sous-titre en h2 et donnons-lui une bordure supérieure et inférieure.

et notre CSS :

Sortie :

![Image](https://cdn-media-1.freecodecamp.org/images/1*orbR-s8x_fLR6sYNgle19g.jpeg)

D'accord, deux problèmes ici :

* l'espace entre h1 et h2,
* nous ne voulons pas que les lignes blanches (bordure supérieure et inférieure de h2) s'étendent sur toute la section. Nous voulons qu'elles soient aussi larges que le texte « Avengers ».

Pour réduire l'espace entre h1 et h2, supprimons la marge inférieure de h1 et la marge supérieure de h2 :

Le code « margin: 16px 8px 0 » signifie définir la marge supérieure à 16px, les marges droite et gauche à 8px, et la marge inférieure à 0.

Maintenant pour le deuxième problème.

L'élément `<header>` est par défaut un élément de bloc, donc sa largeur s'étend sur la largeur de son parent. Si nous en faisons un élément « inline-block », alors il ne s'étendra pas à la largeur de son parent, et n'occupera que la largeur nécessaire pour adapter le texte à l'intérieur. C'est exactement ce que nous voulons.

Donnons « display: inline-block » à l'en-tête et « text-align: center » à son parent « poster-content » :

Sortie :

![Image](https://cdn-media-1.freecodecamp.org/images/1*kMygYZw_BHEqZCtRRpaiBg.jpeg)

### Police Google personnalisée

Utilisons une police de science-fiction pour h2. Nous avons vu comment télécharger une police et l'utiliser dans notre CSS. Dans un tel scénario, vous hébergez la police vous-même. Google fournit de nombreuses polices hébergées gratuitement [ici](https://fonts.google.com). Nous la relions simplement depuis Google. En voici une qui semble bonne pour notre utilisation :

![Image](https://cdn-media-1.freecodecamp.org/images/1*OMR76PpUGsGzZ_ty8zPB9g.jpeg)

Voici l'[URL](https://fonts.google.com/specimen/Audiowide).

Allez à l'URL ci-dessus et cliquez sur « SELECT THIS FONT » sur le côté droit de l'écran :

![Image](https://cdn-media-1.freecodecamp.org/images/1*5LT-eATcKpb01KehR6Zxfg.jpeg)

Ensuite, cliquez sur la barre « Family Selected » affichée en bas :

![Image](https://cdn-media-1.freecodecamp.org/images/1*UNt8QiOtTM-OZ3Cnru18CA.jpeg)

Cela nous donnera le code à copier pour utiliser cette police sur notre page :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZW2S5IeEgjD6sGqjk7zC4A.jpeg)

Collez le code `<link>` dans notre fichier HTML :

et le code font-family dans notre CSS :

J'ai également ajouté un espacement des lettres, car les lettres semblaient congestionnées. J'ai également augmenté la taille de la police à 26px.

Sortie :

![Image](https://cdn-media-1.freecodecamp.org/images/1*JKpvtjmxeemuwSdKx5Qoug.jpeg)

### Intégrer la vidéo YouTube

L'affiche du film sera incomplète sans une vidéo de la bande-annonce.

Nous pouvons inclure la vidéo YouTube dans notre page HTML en utilisant « iframe ». La balise « iframe » nous permet de charger une autre page HTML dans la page actuelle. La page à charger est décidée par l'attribut « src ».

Voici comment vous pouvez utiliser `<iframe>` pour inclure une vidéo de YouTube :

```
<iframe src="https://www.youtube.com/embed/6ZfuNTqbHE8"></iframe>
```

Le texte « [https://www.youtube.com/embed/](https://www.youtube.com/embed/) » dans « src » reste le même pour toutes les vidéos YouTube. Seule la dernière chaîne de caractères aléatoires « 6ZfuNTqbHE8 » change pour chaque vidéo. C'est l'ID de la vidéo, et vous pouvez le trouver dans l'URL de la vidéo :

![Image](https://cdn-media-1.freecodecamp.org/images/1*UPkoofYc60Pmlh-WK6gNiA.jpeg)

Incluons la vidéo de la bande-annonce :

Sortie :

![Image](https://cdn-media-1.freecodecamp.org/images/1*FXxy6cAzUxu8L5vQLmHkiw.jpeg)

Zut. Qu'est-ce qui ne va pas maintenant ?

Pouvez-vous deviner pourquoi la vidéo est affichée à droite de l'en-tête ?

Parce que nous avons défini l'en-tête comme « inline-block », et comme nous le savons, un élément inline-block donnera de la place à l'élément suivant juste à côté.

Pour résoudre cela, donnons une certaine largeur et hauteur à notre élément iframe :

La bordure par défaut de l'iframe était laide, alors j'ai ajouté une bordure de 2px de couleur « #ddd » (presque blanche).

Sortie :

![Image](https://cdn-media-1.freecodecamp.org/images/1*vq9V7UCe2IYz5U9yv70RRQ.jpeg)

Super.

Une dernière chose — la date de sortie. Mettons la date de sortie dans un paragraphe en bas :

et stylisons un peu le paragraphe :

Nous avons augmenté la taille de la police à 18px, lui avons donné une couleur blanche (#fff), défini la police à « Audiowide », et réduit la marge inférieure à « 8px ».

Sortie :

![Image](https://cdn-media-1.freecodecamp.org/images/1*bKfG0yasGD590ClJBKDetQ.jpeg)

Notre affiche de film Infinity War est complète.

**Vous voulez apprendre le développement web avec des tutoriels amusants et engageants ?**

[**Cliquez ici pour obtenir de nouveaux tutoriels de développement web chaque semaine.**](http://supersarkar.com)