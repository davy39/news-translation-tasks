---
title: 'HTML vs Body : Comment définir la largeur et la hauteur pour une page pleine
  taille'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-17T17:06:50.000Z'
originalURL: https://freecodecamp.org/news/html-page-width-height
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/william-warby-WahfNoqbYnM-unsplash--1-.jpg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: HTML
  slug: html
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: 'HTML vs Body : Comment définir la largeur et la hauteur pour une page
  pleine taille'
seo_desc: "By Dave Gray\nCSS is difficult but also forgiving. And this forgiveness\
  \ allows us to haphazardly throw styles into our CSS. \nOur page still loads. There\
  \ is no \"crash\". \nWhen it comes to page width and height, do you know what to\
  \ set on the HTML elemen..."
---

Par Dave Gray

CSS est difficile mais aussi indulgent. Et cette indulgence nous permet de jeter des styles dans notre CSS de manière désordonnée. 

Notre page se charge toujours. Il n'y a pas de "plantage". 

Quand il s'agit de la largeur et de la hauteur de la page, savez-vous quoi définir sur l'élément HTML ? Et sur l'élément body ? 

Est-ce que vous appliquez simplement les styles aux deux éléments et espérez le meilleur ?

Si c'est le cas, vous n'êtes pas seul.

Les réponses à ces questions ne sont pas intuitives. 

Je suis 100% coupable d'avoir appliqué des styles aux deux éléments dans le passé sans considérer exactement quelle propriété devrait être appliquée à quel élément. 🧑‍♂️

Il n'est pas rare de voir des propriétés CSS appliquées à la fois aux éléments HTML et body comme ceci :

```
html, body {
     min-height: 100%;
}
```

## Est-ce que cela compte ?

Oui, oui, cela compte.

La définition de style ci-dessus crée un problème :

Définir min-height à 100% sur les deux éléments ne permet pas à l'élément body de remplir la page comme vous pourriez vous y attendre. Si vous vérifiez les valeurs de style calculées dans les outils de développement, l'élément body a une hauteur de zéro. 

Pendant ce temps, l'élément HTML a une hauteur égale à la partie visible de la page dans le navigateur.

Regardez la capture d'écran suivante de Chrome Dev Tools :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/empty_body.png)
_L'élément body a une marge par défaut de 8px indiquée par la barre en haut. La valeur de la hauteur est 0._

## Pourquoi cela arrive-t-il ?

L'utilisation d'un pourcentage comme valeur de taille nécessite que l'élément référence un parent pour baser ce pourcentage. 

L'élément HTML référence le viewport qui a une valeur de hauteur égale à la hauteur visible du viewport. Cependant, nous n'avons défini qu'une min-height sur l'élément HTML... PAS une valeur de propriété de hauteur. 

Par conséquent, l'élément body n'a pas de valeur de hauteur parent à référencer pour décider à quoi 100% est égal.

## Et le problème peut être caché

Si vous avez commencé avec suffisamment de contenu pour remplir le body de la page, vous n'avez peut-être pas remarqué ce problème. 

Et pour le rendre plus difficile à remarquer, si vous définissez une background-color sur les deux éléments ou même sur un seul d'entre eux, le viewport est rempli de cette couleur. Cela donne l'impression que l'élément body est aussi grand que le viewport.

Ce n'est pas le cas. Il est toujours à zéro.

L'image ci-dessus est tirée d'une page avec le CSS suivant : 

``` 
html, body {
    min-height: 100%;
}
body { background-color: dodgerblue; }
```

### Héritage inverse ?

Dans un étrange retournement, l'élément HTML prend la background-color de l'élément body si vous ne définissez pas une background-color séparée sur l'élément html. 

## Quelle est la configuration idéale de la hauteur pour une page responsive complète ?

Pendant des années, la réponse était la suivante :

```
html {
    height: 100%;
}
body {
    min-height: 100%;
}
```

Cela permet à l'élément HTML de référencer le viewport parent et d'avoir une valeur de hauteur égale à 100% de la valeur du viewport. 

Avec l'élément HTML recevant une valeur de hauteur, la valeur min-height attribuée à l'élément body lui donne une hauteur initiale qui correspond à l'élément HTML. 

Cela permet également au body de grandir si le contenu dépasse la page visible. 

Le seul inconvénient est que l'élément HTML ne grandit pas au-delà de la hauteur du viewport visible. Cependant, permettre à l'élément body de dépasser l'élément HTML a été considéré comme acceptable.

## **La solution moderne est simplifiée**

```
body { min-height: 100vh; }
```

Cet exemple utilise les unités `vh` (viewport height) pour permettre au body de définir une valeur de hauteur minimale basée sur la hauteur totale du viewport. 

Comme pour la background-color discutée précédemment, si nous ne définissons pas de valeur de hauteur pour l'élément HTML, il prendra la même valeur de hauteur que celle donnée à l'élément body. 

Par conséquent, cette solution évite le débordement de l'élément HTML présent dans la solution précédente et les deux éléments grandissent avec votre contenu ! 

L'utilisation des unités `vh` a causé quelques problèmes avec les navigateurs mobiles dans le passé, mais [il semble que Chrome et Safari soient maintenant cohérents avec les unités de viewport](https://developers.google.com/web/updates/2016/12/url-bar-resizing).

## La hauteur de la page peut provoquer une barre de défilement horizontale

Attendez, quoi ? 

Ne devrait-on pas dire "Largeur de la page" ? 

Non.

Dans une autre étrange série d'événements, la hauteur de votre page peut activer la barre de défilement horizontale dans votre navigateur. 

Lorsque le contenu de votre page grandit plus haut que la hauteur du viewport, la barre de défilement verticale à droite est activée. Cela peut provoquer l'apparition instantanée d'une barre de défilement horizontale également.

## Quelle est la solution ?

Vous dormirez peut-être mieux en sachant que cela commence par un réglage de la largeur de la page.

Ce problème survient lorsqu'un élément - pas seulement l'élément HTML ou body - est défini à 100vw (viewport width) unités. 

Les unités de viewport ne tiennent pas compte des approximativement 10 pixels que la barre de défilement verticale occupe. 

Par conséquent, lorsque la barre de défilement verticale s'active, vous obtenez également une barre de défilement horizontale.

## Comment définir la page pour une largeur complète

Peut-être simplement ne pas le faire. 

Ne pas définir de largeur sur les éléments HTML et body reviendra par défaut à la taille complète de l'écran. Si vous définissez une valeur de largeur autre que auto, envisagez d'utiliser d'abord une réinitialisation CSS.

Rappelez-vous, par défaut, l'élément body a une marge de 8px sur tous les côtés. 

Une réinitialisation CSS supprime cela. Sinon, définir la largeur à 100% avant de supprimer les marges provoquera un débordement de l'élément body. Voici la réinitialisation CSS que j'utilise :

```
* { 
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
```

## Comment définir la largeur selon votre préférence

Bien qu'il ne soit pas toujours nécessaire de définir une largeur, je le fais généralement. 

Cela peut simplement être une habitude.

Si vous définissez la largeur à 100% sur l'élément body, vous aurez une largeur de page complète. Cela est essentiellement équivalent à ne pas définir de valeur de largeur et à permettre la valeur par défaut.

Si vous souhaitez utiliser l'élément body comme un conteneur plus petit et laisser l'élément HTML remplir la page, vous pourriez définir une valeur max-width sur le body. 

Voici un exemple : 

```
html { background-color: #000; } 
body {
    min-height: 100vh;
    max-width: 400px;
    background-color: papayawhip; 
    margin: 0 auto;
}
```

## Conclusion

Sans valeur de hauteur fournie pour l'élément HTML, définir la hauteur et/ou la min-height de l'élément body à 100% résulte en une hauteur nulle (avant d'ajouter du contenu).

Cependant, sans valeur de largeur fournie pour l'élément HTML, définir la largeur de l'élément body à 100% résulte en une largeur de page complète.

Cela peut être contre-intuitif et déroutant. 

Pour une hauteur de page responsive complète, définissez la min-height de l'élément body à 100vh.

Si vous définissez une largeur de page, choisissez 100% plutôt que 100vw pour éviter les barres de défilement horizontales surprises.

Je vous laisse avec un tutoriel de ma chaîne YouTube démontrant les paramètres de hauteur et de largeur CSS pour une page HTML en plein écran qui grandit avec le contenu qu'elle contient :

%[https://youtu.be/dpuKVjX6BJ8]

Avez-vous une autre façon de définir la largeur et la hauteur CSS que vous préférez ?

Faites-moi savoir votre méthode !