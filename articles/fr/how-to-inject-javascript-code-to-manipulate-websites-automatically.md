---
title: Comment injecter du code JavaScript pour manipuler des sites web automatiquement
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-16T16:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-inject-javascript-code-to-manipulate-websites-automatically
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/Untitled-1.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment injecter du code JavaScript pour manipuler des sites web automatiquement
seo_desc: 'By Roberto Iriondo

  As developers and users of the internet, we often come across websites that display
  many pop-ups, from subscription requests to paywalls, advertisements to notifications,
  and so on.

  Many times, we use those websites daily for all k...'
---

Par Roberto Iriondo

En tant que développeurs et utilisateurs d'Internet, nous rencontrons souvent des sites web qui affichent de nombreuses fenêtres contextuelles, allant des demandes d'abonnement aux paywalls, en passant par les publicités et les notifications, et ainsi de suite.

Souvent, nous utilisons ces sites web quotidiennement pour toutes sortes de choses, et voir ces fenêtres contextuelles encore et encore devient agaçant !

Les développeurs peuvent contourner ces problèmes en allant dans la console et en trouvant des sélecteurs pour manipuler le [document object model](https://en.wikipedia.org/wiki/Document_Object_Model) (DOM) du site web en ajoutant ou en modifiant du CSS ou du JavaScript.

Mais maintenant, grâce à Google Chrome et à son magasin d'extensions, n'importe qui peut injecter du code dans n'importe quel site web automatiquement. Nous allons passer par le processus étape par étape dans ce petit guide.

### 1. Installation de l'extension pour injecter le code

Ce qui suit ne s'applique que si vous utilisez [Google Chrome](https://google.com/chrome). Installez l'extension [custom JavaScript for websites](https://chrome.google.com/webstore/detail/custom-javascript-for-web/poakhlngfciodnhlhhgnaaelnpjljija?hl=en). Cette petite extension vous permet d'exécuter du JavaScript sur n'importe quel site web automatiquement, et elle sauvegarde le code pour les visites futures dans votre navigateur web.

Tout d'abord, visitez le site web avec des fenêtres contextuelles agaçantes que vous utilisez souvent. Pour ce tutoriel, j'utilise le site web du Washington Post :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/1_BUguCP1rb7S-lFwVvC_1fg.png)
_Capture d'écran montrant le site web du Washington Post avec un article mentionnant Andrew Yang, ainsi que les outils de développement de Chrome._

### 2. Localisation des éléments DOM et création du code d'injection

Ouvrez vos outils de développement Chrome en appuyant sur F12, puis identifiez l'élément avec la fenêtre contextuelle.

Dans cet exemple, l'élément `iframe` avec l'ID `wallIframe` contient la fenêtre contextuelle avec un fond estompé à l'arrière.

Maintenant, nous allons utiliser un petit extrait de JavaScript pour ajouter du CSS personnalisé et vérifier si nous pouvons masquer la fenêtre contextuelle.

```javascript
/* Manipulation du DOM
* Si vous souhaitez mettre à jour / ajouter un style unique dans l'attribut de style de l'élément DOM, vous pouvez utiliser cette fonction :
* injecter du javascript après le rechargement de la page.
*/

function setCssStyle(el, style, value) {
  var result = el.style.cssText.match(new RegExp("(?:[;\\s]|^)(" +
      style.replace("-", "\\-") + "\\s*:(.*?)(;|$))")),
    idx;
  if (result) {
    idx = result.index + result[0].indexOf(result[1]);
    el.style.cssText = el.style.cssText.substring(0, idx) +
      style + ": " + value + ";" +
      el.style.cssText.substring(idx + result[1].length);
  } else {
    el.style.cssText += " " + style + ": " + value + ";";
  }
}
var element = document.getElementById("wallIframe");
setCssStyle(element, "display","none !important");
```

Comme vous pouvez le voir, dans le code ci-dessus, nous mettons en évidence l'élément `wallIframe` et le masquons en ajoutant du CSS en ligne.

### 3. Test du code d'injection

Testez votre code dans la console des développeurs Chrome pour vous assurer qu'il fonctionne.

![Capture d'écran montrant le site web du Washington Post avec un article mentionnant Andrew Yang, ainsi que les outils de développement de Chrome.](https://www.freecodecamp.org/news/content/images/2020/04/1_qwrHgqiwmZreTmdQFeKE2Q--1-.png)
_Capture d'écran montrant le site web du Washington Post avec un article mentionnant Andrew Yang, ainsi que les outils de développement de Chrome._

Comme vous pouvez le voir ci-dessus, le code fonctionne.

Maintenant, il est temps de l'ajouter à l'extension, [custom JavaScript for websites](https://chrome.google.com/webstore/detail/custom-javascript-for-web/poakhlngfciodnhlhhgnaaelnpjljija?hl=en), et de tester si le code fonctionnera lors des visites futures. Pour l'ajouter, cliquez gauche sur l'icône de l'extension dans votre barre d'adresse et ajoutez l'extrait personnalisé, puis cliquez sur sauvegarder.

La page se rechargera immédiatement pour essayer et tester votre code ajouté.

![Capture d'écran montrant le site web du Washington Post avec un article mentionnant Andrew Yang, ainsi que les outils de développement de Chrome.](https://www.freecodecamp.org/news/content/images/2020/04/1_SoyzA-pNiOQhmGf-7XZ33A.png)
_Capture d'écran montrant le site web du Washington Post avec un article mentionnant Andrew Yang, ainsi que les outils de développement de Chrome._

## 4. Le code d'injection n'a pas fonctionné, que faire maintenant ?

Après l'avoir testé, l'iframe n'a pas disparu comme cela avait été le cas lorsque nous l'avions testé dans la console. Une des raisons pourrait être que l'iframe se charge après X secondes de chargement de la page.

Nous pourrions fouiller dans le journal du réseau pour voir si c'est le cas. Mais pour gagner du temps, nous allons essayer d'ajouter une fonction de timeout à notre extrait original pour voir si cela aide.

```javascript
setTimeout(
     function() {
       function setCssStyle(el, style, value) {
         var result = el.style.cssText.match(new RegExp("(?:[;\\s]|^)(" +
             style.replace("-", "\\-") + "\\s*:(.*?)(;|$))")),
           idx;
         if (result) {
           idx = result.index + result[0].indexOf(result[1]);
           el.style.cssText = el.style.cssText.substring(0, idx) +
             style + ": " + value + ";" +
             el.style.cssText.substring(idx + result[1].length);
         } else {
           el.style.cssText += " " + style + ": " + value + ";";
         }
       }
       
       var element = document.getElementById("wallIframe");
       setCssStyle(element, "display", "none !important");
     }, 10000);
```

Maintenant, le code attend 10 secondes avant de s'exécuter, et _voilà_, il fonctionne parfaitement.

Vous pouvez également ajouter un écouteur d'événement pour attendre que la page se charge complètement.

### 5. Réflexions finales

Par exemple :

```javascript
document.addEventListener("DOMContentLoaded", function() { 
    // Votre fonction va ici
}
```

Mais, si nous ajoutons le code de la fenêtre contextuelle après X secondes, la fonction ci-dessus ne fonctionnera pas, il est donc préférable de s'en tenir à la fonction de timeout.

Vous pouvez également utiliser l'extension pour ajouter de nombreux autres extraits intéressants, tels que pour bloquer les publicités, bloquer les fenêtres contextuelles, augmenter la police standard du site web, améliorer la réactivité, mettre à jour son apparence, et ainsi de suite. Une fois les extraits JavaScript ajoutés, ils s'exécuteront toujours lors des visites futures à ces sites web.

> _Un remerciement spécial à Abbey Rennemeyer de freeCodeCamp pour ses commentaires éditoriaux en préparation de cet article._

**AVERTISSEMENT :** Les opinions exprimées dans cet article sont celles de l'auteur(s) et ne représentent pas les opinions de l'Université Carnegie Mellon, ni d'autres entreprises (directement ou indirectement) associées à l'auteur(s). Ces écrits ne sont pas destinés à être des produits finaux, mais plutôt une réflexion de la pensée actuelle, ainsi qu'un catalyseur pour la discussion et l'amélioration.

Vous pouvez me trouver sur : [Mon site web personnel](https://www.robertoiriondo.com/), [Medium](https://medium.com/@robiriondo), [Instagram](https://www.instagram.com/robiriondo/hl=en), [Twitter](https://twitter.com/robiriondo?lang=en), [Facebook](https://www.facebook.com/robiriondo/), [LinkedIn](https://www.linkedin.com/in/robiriondo) ou via ma [société de SEO](https://www.daibuilds.com/seo-services/).