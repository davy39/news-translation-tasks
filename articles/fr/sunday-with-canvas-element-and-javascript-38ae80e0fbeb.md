---
title: Passez votre dimanche (ou n'importe quel jour) avec l'élément canvas et JavaScript.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-02T00:50:57.000Z'
originalURL: https://freecodecamp.org/news/sunday-with-canvas-element-and-javascript-38ae80e0fbeb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1d6oMjjsNM4QrprjTxb87w.png
tags:
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Passez votre dimanche (ou n'importe quel jour) avec l'élément canvas et
  JavaScript.
seo_desc: 'By Ashish Nandan Singh

  Recently during the JavaScript30 days challenge, I had the chance to get my hands
  dirty with the HTML inbuilt canvas property. What convinced me to write about the
  entire experience was the relative comfort level and learning c...'
---

Par Ashish Nandan Singh

Récemment, lors du défi JavaScript30 jours, j'ai eu l'occasion de me familiariser avec la propriété canvas intégrée de HTML. Ce qui m'a convaincu d'écrire sur toute l'expérience, c'est le niveau de confort relatif et la courbe d'apprentissage.

Dans sa forme la plus simple, l'élément canvas HTML permet à un développeur web de dessiner des graphiques sur une page web, via JavaScript, et cet aspect rend cet élément HTML bien plus intéressant.

L'élément **<canvas>** n'est qu'un conteneur — vous utiliserez toujours JavaScript pour dessiner réellement les graphiques. Certains pourraient argumenter que nous pouvons toujours ajouter des points ou peut-être un SVG pour cela, mais encore une fois — quel plaisir cela serait-il ? :D

Revenons à l'élément **<canvas>** : un canvas est une zone rectangulaire sur une page HTML. Par défaut, un canvas n'a pas de bordure et pas de contenu.

Le balisage ressemble à ceci :

> <canvas id="canvas" width="200" height="100"></canvas>

#### Le début

D'accord, assez pour l'introduction. Concentrons-nous sur la construction de quelque chose d'amusant en utilisant du bon vieux JavaScript, (pas si vieux — ES6 !). Tout d'abord, nous allons examiner les fichiers de démarrage.

Décomposons cela. Nous avons une feuille de style nommée **style.css**. Ensuite, nous définissons un élément **canvas** avec une largeur de 800 et une hauteur de 800. Enfin, nous avons une balise **script** nommée **app.js** où toute la magie se produit. Sur cette note, commençons à faire des choses avec notre propre app.js.

* Nous commençons par sélectionner l'élément canvas dans la première ligne et stockons la valeur dans une variable const nommée **canvas** pour simplifier.
* Ensuite, nous capturons le contexte du même canvas en aspect 2D et le définissons dans la **variable**.
* Définissons la largeur et la hauteur du canvas pour qu'elles soient respectivement la largeur intérieure de la fenêtre et la hauteur.

Maintenant que nous avons enfin notre canvas en place, nous passons à la définition des attributs les plus basiques du canvas.

* **ctx.strokeStyle** définit ou retourne la couleur, le dégradé ou le motif utilisé pour les traits. Oui, vous avez bien lu : la couleur par défaut est #BADASS.
* **ctx.lineWidth** définit ou retourne la largeur de ligne actuelle. Nous la définissons à 1, et nous y reviendrons plus tard.
* **ctx.lineJoin** définit ou retourne le type de coin créé lorsque deux lignes se rencontrent. Nous le définissons à round pour que lorsque deux lignes se rencontrent, nous ayons un point de connexion net.
* **ctx.lineCap** définit ou retourne le style des extrémités pour une ligne. Nous le définissons à round pour que lorsque nous ne rencontrons aucune autre ligne, nous obtenions toujours cette même figure de tuyau nette en fonction de la largeur de trait définie précédemment.

Maintenant que nous avons toutes ces pièces en place, voyons comment nous pouvons procéder pour dessiner réellement sur le canvas.

Tout d'abord, nous devons ajouter des écouteurs d'événements pour le mouvement de la souris sur le canvas, puis déclencher une fonction qui dessinerait réellement quelque chose sur le canvas. Jetons un coup d'œil aux ajouts que nous pourrions avoir dans le fichier app.js.

Décomposons cela :

* Nous commençons par définir une variable appelée **isDrwaing** qui nous aidera à déterminer si l'utilisateur essaie réellement de dessiner sur le canvas ou non. Nous y reviendrons plus tard.
* Pour l'instant, ayons une fonction appelée **draw** qui sera déclenchée et qui sera ensuite responsable de toute l'action.
* Enfin, nous ajoutons un ensemble d'écouteurs d'événements pour divers événements afin de nous assurer que nous capturons les bons événements et que nous exécutons la fonction **draw** uniquement lorsque cela est nécessaire.

En déclarant la variable **isDrawing** et en définissant sa propriété à **false**, nous définissons l'**état initial** du canvas dès que l'élément canvas est chargé comme non dessin. Ensuite, dans chaque écouteur d'événement suivant, nous utilisons une **fonction en ligne** et changeons la valeur de la fonction **isDrawing** à chaque fois selon le type d'événement déclenché.

Au début de la fonction draw, si la valeur de **isDrawing** est définie à false, la fonction est appelée après avoir rencontré l'instruction return. Si **isDrawing** est défini à true, la fonction draw est exécutée.

#### Fonction Draw

Développons cette fonction draw :

* Nous commençons par définir deux variables globalement, **lastX, lastY**, et définissons la valeur initiale à 0.
* Si vous allez dans la console de votre navigateur maintenant, vous verrez que vous avez un énorme journal de tous les mouvements de la souris que vous avez faits. Cet objet **MouseEvent** a certaines propriétés très importantes et utiles :

![Image](https://cdn-media-1.freecodecamp.org/images/1*OUcCcMG5ljNwh1aJPqsHSA.png)
_Objet MouseEvent_

Nous ne sommes intéressés que par les propriétés offsetX et offsetY de cet objet.

* Avec **ctx.beginPath**, nous commençons un chemin, ou réinitialisons un chemin actuel. Les deux que nous voulons faire pour chaque événement déclenché.
* **ctx.moveTo** déplace le chemin vers le point spécifié dans le canvas, sans créer de ligne. Dans notre cas, ce serait lastX et lastY définis à l'extérieur de la fonction à portée globale.
* **ctx.lineTo** ajoute un nouveau point et crée une ligne vers ce point à partir du dernier point spécifié dans le canvas.
* **ctx.stroke()** dessine réellement le chemin que vous avez défini — le vrai travailleur acharné, les gars !

À l'intérieur de **ctx.lineTo**, nous avons utilisé la propriété d'événement **offsetX** et **offsetY** pour obtenir le dernier point de X et Y dans le canvas uniquement pour dessiner une ligne avec **ctx.lineTo**.

Nous avons presque tout en place. Chaque événement de souris sur la page web dessine une ligne sur le canvas — mais avec quelques problèmes et pas beaucoup de style. Alors ajoutons un peu de style.

#### Style !

Pour l'instant, toutes les lignes sont dessinées à partir du point 0 et 0 dans le canvas. Nous définissons cela comme l'ensemble initial de points pour commencer à dessiner lorsque nous chargeons le canvas ou même lorsque nous exécutons la fonction draw.

Corrigeons cela pour avoir une meilleure expérience en temps réel. Si vous y réfléchissez, la réponse est très simple : chaque fois que la fonction draw est exécutée, nous voulons que le point initial soit toujours la propriété **offsetX** et **offsetY** de l'**objet MouseEvent**.

En utilisant la destructuration de tableau ES6, nous pouvons réinitialiser les valeurs de lastX et lastY pour qu'elles soient les propriétés offsetX et offsetY de l'objet MouseEvent. Nous pouvons faire cela à la toute fin de la fonction draw. Jetons un coup d'œil au fichier app.js après avoir ajouté un peu de style.

* Dès que l'événement **mousemove** se produit, nous déclenchons la fonction draw. Ensuite, nous définissons la valeur de lastX et lastY dans la fonction draw en utilisant la destructuration ES6.
* Dans le cas d'un événement **mousedown**, nous changeons d'abord la fonction en ligne en bloc, comme vous pouvez le voir, puis nous définissons à nouveau les valeurs lastX et lastY pour qu'elles soient la propriété offset de l'événement. Cela est pour nous assurer que nous avons la ligne visible pour nous sur le canvas pendant que nous nous déplaçons d'un point à un autre point dans le canvas.

Rendons-le coloré et ajoutons quelques dynamiques au trait.

WAOUH !

Cela fait beaucoup à gérer, mais décomposons cela.

* J'ai défini une nouvelle variable appelée **hue** et défini sa propriété à 0.
* Si vous ne connaissez pas déjà la teinte et pourquoi elle est géniale, dirigez-vous vers Google et essayez-la, ou cliquez simplement [ici](http://mothereffinghsl.com/).

Dans sa forme la plus simple, hsl nous permet d'utiliser le même arc-en-ciel de couleurs allant de 0 à 360. Chaque nombre a une valeur de lumière et alpha. La définition de hsl ressemble à ceci : hsl(173, 99%, 50%). Ici, le nombre 173 représente une couleur — 99% est la lumière et 50% est la valeur alpha.

Encore une fois, en utilisant quelques backticks ES6 géniaux, nous pouvons utiliser le hsl et l'influencer en faisant quelque chose comme ceci :

`ctx.strokeStyle = `hsl(${hue}, 100%, 50%)``

comme nous l'avons fait à la ligne 7 dans le gist ci-dessus.

Ensuite, nous augmentons la valeur de la variable **hue** qui change la couleur du trait à chaque événement **mousemove**. Une fois que la valeur de hue a été incrémentée jusqu'à 360, nous réinitialisons la valeur de hue à 0 à la ligne 14 du gist ci-dessus. Mais même si nous ne faisons pas cela, nous aurons toujours le même résultat. Néanmoins, faisons simplement la bonne chose. :D lol

`if(hue>360){`  
 `hue = 0`   
`}`

Ensuite, ajoutons quelques dynamiques à la largeur du trait dessiné à chaque fois, comme ceci :

`if(ctx.lineWidth>=75 || ctx.lineWidth<=1){`  
 `direction = !direction;`  
`}`

`if(direction){`  
 `ctx.lineWidth++`  
`} else {`  
 `ctx.lineWidth = 0`  
`}`

Tout ce que nous avons fait ici, c'est d'abord vérifier si la **lineWidth** actuelle est supérieure à 75 ou inférieure à 1. Si c'est le cas, alors nous inversons la valeur de la variable **direction** qui est définie à true par défaut.

Ensuite, nous vérifions si la valeur de la variable **direction** est true. Si c'est le cas, alors nous incrémentons la valeur de lineWidth de 1, sinon nous réinitialisons la **lineWidth** à 0.

Ce n'était pas beaucoup de JavaScript. Vous devriez avoir votre joli canvas prêt maintenant si vous avez suivi correctement.

Jetons un coup d'œil rapide à ce à quoi ressemble la structure finale du fichier. Puisque nous n'avons modifié que le fichier app.js, je ne vous montrerai que celui-ci, car index.html reste presque inchangé depuis le début.

Ce n'est que la partie émergée de l'iceberg lorsque l'on pense à la puissance totale de l'élément canvas combiné avec JavaScript. Je vous encouragerais à faire un peu plus de recherches et à rendre le canvas encore meilleur. Peut-être ajouter quelques boutons pour effacer l'écran, ou peut-être sélectionner une couleur spécifique pour dessiner sur le canvas. Tellement d'options !

Tout ce que je dis, c'est qu'il y a un million de façons de rendre cela meilleur. Je mettrai définitivement à jour l'histoire si j'ai quelque chose qui vaut la peine d'être mis à jour.

Enfin, j'aimerais vous laisser avec une vidéo de l'apparence du canvas à la toute fin.

J'espère que vous avez apprécié la lecture de tout cela ! Tout commentaire ou suggestion pour améliorer ou discuter davantage serait vraiment apprécié. Vous pouvez me contacter sur [twitter](https://twitter.com/ashishnandansin) et [linkedIn](https://www.linkedin.com/in/ashish-nandan-singh-490987130/) également.