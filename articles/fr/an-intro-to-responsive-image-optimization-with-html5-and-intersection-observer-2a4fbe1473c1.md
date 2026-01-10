---
title: Une introduction à l'optimisation des images réactives avec HTML5 et Intersection
  Observer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-29T23:43:17.000Z'
originalURL: https://freecodecamp.org/news/an-intro-to-responsive-image-optimization-with-html5-and-intersection-observer-2a4fbe1473c1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*VjKU4KyUs4A7oaRA-3j0Dg.jpeg
tags:
- name: HTML5
  slug: html5
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Une introduction à l'optimisation des images réactives avec HTML5 et Intersection
  Observer
seo_desc: 'By Riccardo Canella

  Images often account for most of the downloaded bytes on a web page and often occupy
  a significant amount of visual space. As a result, optimizing images can frequently
  yield some of the largest byte savings and performance improv...'
---

Par Riccardo Canella

Les images représentent souvent la majorité des octets téléchargés sur une page web et occupent souvent une part importante de l'espace visuel. Par conséquent, l'optimisation des images peut fréquemment entraîner certaines des plus grandes économies d'octets et améliorations de performance pour votre site web. Moins le navigateur a d'octets à télécharger, moins l'utilisateur devra attendre pour le rendu du contenu utile à l'écran.

L'optimisation des images est à la fois une science et un art. C'est une science car il existe de nombreuses techniques et algorithmes bien développés qui peuvent réduire considérablement la taille d'une image. C'est un art car il n'y a pas de réponse définitive unique.

Mais comment pouvons-nous optimiser nos images pour les appareils mobiles en plus d'utiliser des outils d'optimisation web comme ImageMagick ou autres ?

### L'élément img

L'élément <img> HTML5 a été conçu pour donner au développeur la possibilité d'optimiser les images en fonction de la résolution de l'écran. Cela est fait grâce à deux attributs, `srcset` et `sizes`. Avec une syntaxe très simple, vous pouvez instruire le navigateur de décider quelle taille d'image parmi les différentes tailles disponibles est nécessaire :

```html
<img srcset="the-death-star-320w.jpg,
             the-death-star-480w.jpg 1.5x,
             the-death-star-640w.jpg 2x"
             src="the-death-star-640w.jpg" 
alt="The Death Star">
```

Le navigateur, dans ce cas, choisira l'image la mieux adaptée à sa résolution. Cependant, l'hypothèse est que l'image doit être affichée en plein écran (100vw). Ce n'est généralement pas une hypothèse terrible à faire.

L'attribut `sizes` est utilisé pour éviter ce problème et, par conséquent, pour aider le navigateur à choisir l'image la plus optimisée pour ce cas. Vous pouvez utiliser sizes pour correspondre exactement à votre mise en page CSS et dire au navigateur exactement quelle taille l'image aura sur chaque taille d'écran, en correspondant à la façon dont vos points de rupture fonctionnent dans votre design.

Cela peut devenir un peu compliqué, et honnêtement, cela peut être un peu dangereux. Vous mettez du CSS dans le balisage et vous savez comment cela se passe. Cela peut être automatisé ou injecté côté serveur. Même dans ce cas, la syntaxe est vraiment très simple :

```html
<img srcset="the-death-star-320w.jpg,
             the-death-star-480w.jpg 1.5x,
             the-death-star-640w.jpg 2x"
             src="the-death-star-640w.jpg" 
sizes="(min-width: 800px) 50vw, 100vw"
alt="The Death Star">
```

### L'élément picture

Il existe différents formats pour optimiser les images pour le web, tels que `webp` et `jpg2000`. Mais tous les navigateurs ne sont pas capables de les supporter — Internet Explorer, par exemple. Cela ne devrait pas nous empêcher d'utiliser le format le plus optimisé pour la plupart des navigateurs modernes.

L'élément picture est un excellent moyen de fournir des sources alternatives pour les fichiers image, afin que le navigateur puisse choisir en fonction des capacités de l'appareil. La syntaxe est très similaire à l'élément <video> et vous permet d'utiliser les attributs que je vous ai d'abord montrés pour l'élément <img>.

```html
<picture>
  <source type="image/webp" srcset="the-death-star.webp">
  <source media="(min-width: 320px)" srcset="the-death-star-mn.jpg">
  <source media="(min-width: 465px)" srcset="the-death-star-sm.jpg">
  <source media="(min-width: 650px)"
          srcset="the-death-star-md.jpg,
                 the-death-star-lg.jpg 1.5x"
          sizes="(min-width: 800px) 50vw, 100vw"
  >
  <img src="the-death-star.jpg" alt="Flowers" style="width:auto;">
</picture>
```

**Mais puis-je utiliser l'élément <picture> partout ?**

Malheureusement, non. Les navigateurs comme Internet Explorer 11 ne supportent pas cet élément.

![Image](https://cdn-media-1.freecodecamp.org/images/8Mln3ivuAOqt9Dc67yvdlpXjl9yQOj8lBEo8)
_Image [source](https://caniuse.com/#search=picture" rel="noopener" target="_blank" title=")._

**Mais il y a une solution**. [Une très petite bibliothèque JS](https://github.com/scottjehl/picturefill) vous permet d'utiliser cet élément, même sur les navigateurs non supportés.

### Chargement paresseux des images

L'un des conseils les plus répandus et utiles que j'ai rencontrés est d'éviter que le navigateur télécharge toutes les images lors du chargement de la page. Téléchargez uniquement les images essentielles, et faites un chargement paresseux des autres ressources. Il existe de nombreuses techniques pour le chargement paresseux. Celles-ci dépendent de la manière dont la page est défilée, ou de la section suivante que l'utilisateur pourrait visiter.

Si vous avez déjà écrit du code de chargement paresseux, vous avez peut-être accompli votre tâche en utilisant des gestionnaires d'événements tels que `scroll` ou `resize`. Cette approche est la plus compatible entre les navigateurs. Cependant, les navigateurs modernes offrent une méthode plus performante et efficace pour vérifier la visibilité des éléments. Cela est réalisé via l'API Intersection Observer.

Intersection Observer est plus facile à utiliser et à lire que le code reposant sur divers gestionnaires d'événements. Les développeurs n'ont besoin que d'enregistrer un observateur pour surveiller les éléments, plutôt que d'écrire un code fastidieux de détection de visibilité des éléments. Tout ce qu'il reste à faire pour le développeur est de décider quoi faire lorsqu'un élément est visible.

```html
<img class="lazy" 
     src="placeholder-image.jpg" 
     data-src="image-to-lazy-load-1x.jpg" 
     data-srcset="image-to-lazy-load-2x.jpg 2x, 
     image-to-lazy-load-1x.jpg 1x" alt="I'm an image!"
>
```

Les trois parties pertinentes de ce balisage sont : l'attribut `class`, et les attributs `data-src` et `data-srcset`. Les deux derniers sont des attributs de remplacement contenant l'URL de l'image que nous chargerons, une fois que l'élément est dans la fenêtre d'affichage.

```js
document.addEventListener("DOMContentLoaded", () => {
 var lazyImages =[].slice.call(
  document.querySelectorAll("img.lazy")
 )
 if ("IntersectionObserver" in window) {
    let lazyImageObserver = 
      new IntersectionObserver((entries, observer) => {
        entries.forEach(function(entry) {
          if (entry.isIntersecting) {
            let lazyImage = entry.target;
            lazyImage.src = lazyImage.dataset.src;
            lazyImage.srcset = lazyImage.dataset.srcset;
            lazyImage.classList.remove("lazy");
            lazyImageObserver.unobserve(lazyImage);
          }
        });
      });

    lazyImages.forEach(function(lazyImage) {
      lazyImageObserver.observe(lazyImage);
    });
  } else {
    // Possibilité de revenir à une méthode plus compatible ici
  }
});
```

Le code est très simple et facile à déboguer ([voici un codepen pour voir ce code en action](https://codepen.io/malchata/pen/YeMyrQ)), mais il y a un gros problème. L'API Intersection Observer n'est pas bien supportée.

![Image](https://cdn-media-1.freecodecamp.org/images/QLM7MhXfeIzVdyRrq3oY4qOtNj-FAuo-k4Nn)
_Image [source](https://caniuse.com/#search=IntersectionObserver" rel="noopener" target="_blank" title=")._

Vous devrez soit utiliser un [polyfill](https://github.com/w3c/IntersectionObserver/tree/master/polyfill), soit implémenter un chargement paresseux basé sur les événements `resize` et `scroll`.

### Chargement progressif des images

**Voici un petit conseil :** lorsque vous exportez vos images (JPEG, GIF, PNG), vous pouvez cocher l'option progressive (par exemple sur Photoshop ou Sketch). Les images se rendent déjà progressivement dans un navigateur web. Mais une image progressive commence par une basse résolution et s'améliore progressivement au fil du temps.

Cette technique est maintenant utilisée par presque tout le monde, car elle permet de montrer immédiatement un aperçu de l'image à l'utilisateur, puis de télécharger lentement les divers détails (par exemple Instagram). Cette méthode permet d'empêcher les utilisateurs avec une connexion lente de quitter votre site car il affiche un écran blanc.

### Dernière astuce

En me tournant vers le web, je suis tombé sur un [article merveilleux](https://jmperezperez.com/medium-image-progressive-loading-placeholder/) de [José M. Pérez](https://www.freecodecamp.org/news/an-intro-to-responsive-image-optimization-with-html5-and-intersection-observer-2a4fbe1473c1/undefined) sur la façon dont Medium optimise et implémente le chargement progressif des images.

Si vous avez aimé l'article, applaudissez et suivez-moi :)  
Merci et restez à l'écoute ?  
Suivez mes dernières nouvelles et conseils sur [Facebook](https://www.facebook.com/CanellaRiccardo/)