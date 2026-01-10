---
title: Comment utiliser l'API Fullscreen de JavaScript
subtitle: ''
author: Gideon Akinsanmi
co_authors: []
series: null
date: '2023-07-10T21:02:06.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-the-javascript-fullscreen-api
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/js_fullscreen_png.png
tags:
- name: api
  slug: api
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Comment utiliser l'API Fullscreen de JavaScript
seo_desc: 'The Fullscreen API is a browser web API that allows you to enable fullscreen
  mode for HTML elements. It saves you the stress of using CSS and JavaScript to implement
  fullscreen functionality.

  The use cases of fullscreen API are numerous because of th...'
---

L'API Fullscreen est une API web navigateur qui permet d'activer le mode plein écran pour les éléments HTML. Elle vous évite le stress d'utiliser CSS et JavaScript pour implémenter la fonctionnalité plein écran.

Les cas d'utilisation de l'API Fullscreen sont nombreux en raison de la complexité accrue des sites web d'aujourd'hui. Dans cet article, je vais vous donner un guide complet pour utiliser l'API Fullscreen.

## Prérequis

Vous devez avoir des connaissances de base sur l'utilisation de HTML, DOM et JavaScript pour créer des pages web. Plus précisément, vous devez savoir comment utiliser les éléments HTML, les méthodes de sélection DOM, les écouteurs d'événements et les objets JavaScript.

## Bases de l'API Fullscreen

L'API Fullscreen dispose de fonctionnalités qui permettent d'afficher vos éléments (principalement des images, des médias et des éléments graphiques) en mode plein écran. Sans elle, vous devriez vous salir les mains avec quelques longues lignes de code CSS et JavaScript.

Avez-vous déjà visité un site web où les images et les vidéos passent en plein écran lorsque vous interagissez avec elles ? Et les jeux en ligne ?

Permettez-moi de vous expliquer trois projets réels qui utilisent le mode plein écran. Bien qu'ils n'utilisent peut-être pas l'API Fullscreen sous le capot, j'essaie de vous donner une vue pratique des cas d'utilisation de cette fonctionnalité et de la manière dont l'utilisation de l'API Fullscreen peut simplifier le processus. Ils incluent : l'application web Twitter, un site web de jeux en ligne et les intégrations de vidéos YouTube.

Un exemple de projet qui utilise le mode plein écran est l'[application web Twitter](https://twitter.com). Chaque fois que vous vous connectez à votre compte Twitter et que vous cliquez sur une image qui vous intéresse, elle passe en plein écran. Cette fonctionnalité aurait pu être implémentée avec des centaines de lignes de code. Mais avec l'API Fullscreen, vous n'auriez pas besoin de tant de code.

Il en va de même pour les sites web de jeux en ligne. Chaque fois que vous visitez un site web de jeux comme [crazygames.com](https://crazygames.com) et que vous cliquez sur un jeu que vous avez envie de jouer, l'élément canvas qui stocke le code source du jeu passe en plein écran.

Un autre exemple est celui des intégrations de vidéos YouTube. Si vous essayez d'intégrer une vidéo YouTube sur votre site web en utilisant l'élément iframe avec l'attribut `allow='fullscreen'` présent, il permet à votre vidéo YouTube de passer en plein écran lorsque l'utilisateur clique sur l'icône plein écran. Consultez mon [lien codepen](https://codepen.io/gid-droid/pen/JjerqPg) et cliquez sur l'icône plein écran pour observer le comportement.

Nativement, l'élément vidéo est le seul élément HTML qui a des capacités par défaut. Chaque fois que vous créez un élément vidéo avec un attribut controls, il obtient automatiquement une icône de contrôle plein écran qui vous permet de basculer votre vidéo entre le mode plein écran et le mode normal. Vous pouvez l'essayer vous-même.

Bien que l'API Fullscreen puisse être utilisée sur tous les principaux navigateurs de bureau et mobiles, il est parfois préférable d'utiliser plusieurs versions préférées de certaines propriétés (pour document.fullscreenElement, il y a `mozFullScreenElement` pour Mozilla Firefox, ou `webkitIsFullScreen`). Si vous avez des doutes, vous pouvez consulter le tableau des préfixes sur [MDN](https://developer.mozilla.org/en-US/docs/Web/API/Fullscreen_API/Guide#prefixing).

## Propriétés et méthodes de l'API Fullscreen

Pour utiliser avec succès l'API Fullscreen, vous devez être familiarisé avec ses propriétés et méthodes. Elles incluent :

* `**element.requestFullscreen()**` : Cette méthode indique au navigateur web de définir un élément spécifié en mode plein écran.
* `**document.exitFullscreen()**` : Cette méthode indique au navigateur web de quitter le mode plein écran d'un élément et de revenir au mode normal.
* **`document.fullscreenElement`** : Cette propriété retourne l'élément qui est en plein écran ou vérifie si le mode plein écran est actif. Une valeur de null signifie qu'aucun élément n'est en mode plein écran.
* `**document.fullscreenEnabled**` : Cette propriété vérifie si le mode plein écran est supporté. Elle retourne `true` si le mode plein écran est supporté et `false` s'il ne l'est pas.
* Événement `**fullscreenchange**` : Cet événement est utilisé pour détecter les changements dans le mode plein écran. Il peut être utilisé pour créer une fonctionnalité lorsque le mode plein écran est activé et quitté.

## Comment demander le mode plein écran

La première étape pour implémenter cette fonctionnalité est de demander le mode plein écran. Vous pouvez le faire avec la méthode `requestFullscreen()`.

Voici le code pour demander le mode plein écran :

```js
let image = document.querySelector('image.img'); 

image.requestFullscreen();
```

Le code ci-dessus retournera une erreur car le mode plein écran ne peut être activé que par des interactions utilisateur telles que des clics, des double-clics, etc.

Dans le code ci-dessous, nous allons utiliser un événement de clic pour activer le mode plein écran.

```js
let image = document.querySelector('img.image');

image.addEventListener('click', function(e){
      image.requestFullscreen();
})
```

Dans le code ci-dessus, j'ai utilisé une méthode `querySelector()` pour sélectionner un élément img. Ensuite, j'ai attaché un écouteur d'événement de clic pour faire passer l'image en plein écran lorsqu'elle est cliquée.

## Comment quitter le mode plein écran

Après que le mode plein écran a été activé, vous aurez besoin d'une méthode `exitFullscreen()` pour quitter le mode plein écran.

Voici le code pour quitter le mode plein écran :

`document.exitFullscreen();`

Dans un projet réel, vous aurez besoin qu'un utilisateur interagisse avec la page web afin de quitter le mode plein écran. Vous aurez besoin d'un écouteur d'événement qui écoute les interactions utilisateur comme les clics, les double-clics, les appuis sur les touches, etc.

Voici comment utiliser un écouteur d'événement avec la fonction `exitFullscreen()` :

```js
let image = document.querySelector('img.image'); 

image.addEventListener('click', function(e){ 
     image.requestFullscreen(); 
 }) 
 
 image.addEventListener('dblclick', function(e){ 
      document.exitFullscreen(); 
})
```

D'après le code ci-dessus, lorsque l'utilisateur clique sur l'image, le mode plein écran s'active. Lorsque vous double-cliquez sur l'image, il se désactive.

## Comment vérifier l'état du mode plein écran

Pour vérifier si un élément est en mode plein écran ou non, nous allons utiliser la propriété `fullscreenElement`.

Une valeur de `null` signifie qu'il n'est pas en mode plein écran.

D'après l'exemple ci-dessus, vous pouvez modifier le code pour activer et quitter le mode plein écran en fonction de la valeur de la propriété `fullscreenElement`.

Voici comment utiliser cette propriété :

```js
image.addEventListener('click', function(e){ 

   if(document.fullscreenElement){ 
      document.exitFullscreen() 
   } else { 
     image.requestFullscreen();
   } 

})
```

D'après le code ci-dessus, vous avez demandé au navigateur de basculer entre le mode plein écran et le mode normal lorsque l'image est cliquée.

## Gestion des événements et état du mode plein écran

Parfois, vous pourriez vouloir apporter des modifications (comme alerter l'utilisateur) lorsque le mode plein écran est activé ou quitté.

Au lieu d'utiliser document.fullscreenElement et plusieurs gestionnaires d'événements pour vérifier si un élément est en plein écran, vous pouvez utiliser l'événement 'fullscreenchange'.

Voici le code :

```js
document.addEventListener('fullscreenchange', function(e){ 

   if(document.fullscreenElement){ 
      console.log('mode plein écran activé');
   } else { 
      console.log('mode plein écran désactivé'); 
   } 
   
})
```

D'après le code ci-dessus, chaque fois que le mode plein écran est activé ou quitté à partir de n'importe quel élément, un message console.log() est affiché dans l'outil de développement.

## Comment appliquer le mode plein écran à divers types d'éléments

Bien que le mode plein écran puisse être appliqué à tous les éléments, il est préférable de l'utiliser sur les éléments multimédias et interactifs tels que img, video, iframe et canvas.

Bien que les cas d'utilisation soient nombreux, j'en expliquerai quelques-uns.

Pour votre élément canvas, si vous construisez un jeu en ligne, il peut être utilisé pour rendre vos jeux en plein écran. De plus, si vous construisez un tableau de bord avec une bibliothèque de graphiques basée sur canvas, il peut être utilisé pour rendre les graphiques individuels de votre tableau de bord en plein écran lorsque l'utilisateur clique dessus.

Pour votre élément vidéo, si vous construisez un lecteur vidéo personnalisé pour votre projet, vous pouvez l'utiliser pour implémenter la fonctionnalité plein écran.

Pour votre élément image, si vous construisez une application web (comme une plateforme de médias sociaux) qui supporte le téléchargement d'images et de vidéos, vous pouvez utiliser cette API pour implémenter le mode plein écran sur les éléments.

Pour les éléments iframe, embed et object, si vous construisez un site web de conversion d'images en PDF, vous pouvez utiliser cette API pour rendre votre PDF converti en plein écran pour révision par vos utilisateurs.

## Bonnes pratiques et conseils pour l'API Fullscreen

Voici les bonnes pratiques et conseils pour l'API Fullscreen :

1. Fournissez des contrôles conviviaux pour l'entrée et la sortie : si vous implémentez le mode plein écran sur des images, vous devez l'activer lorsque l'utilisateur clique sur l'image et quitter lorsque l'utilisateur double-clique ou appuie sur le bouton de retour arrière. Des méthodes conviviales similaires peuvent être utilisées sur les éléments vidéo et canvas. Assurez-vous également de notifier l'utilisateur lorsqu'il entre et quitte le mode plein écran.
2. Assurez-vous de disposer d'options de repli pour les navigateurs non supportés : Si un utilisateur essaie d'activer le mode plein écran à partir d'un navigateur non supporté, vous devez l'alerter de cette incompatibilité.
3. Si vous utilisez le mode plein écran sur des iframes qui lient à des sources externes, n'oubliez pas de définir l'attribut `allow = 'fullscreen'`.

```
<button>plein écran</button>
<iframe allow='fullscreen' src='https://external.com/content' width='500' height='300'> </iframe> 
 
<script> 
    let button = document.querySelector('button'); 
    let iframe = document.querySelector('iframe'); 
    
    button.addEventListener('click', function (){  
       iframe.requestFullscreen();
    }) 
</script>
```

4. Les événements de la souris (comme mouseover) et la fonction alert() peuvent se comporter de manière inattendue, vous ne devriez donc pas les utiliser dans l'API Fullscreen.

## Conclusion

Dans ce tutoriel, vous avez appris ce qu'est l'API Fullscreen, comment l'implémenter et les bonnes pratiques à suivre.

J'espère que vous êtes maintenant en mesure d'utiliser les capacités de l'API Fullscreen dans vos projets web.

N'hésitez pas à consulter le site web MDN pour approfondir vos connaissances. Vous pouvez également me suivre sur Twitter (@GidtheCoder) pour entrer en contact avec moi. Santé.