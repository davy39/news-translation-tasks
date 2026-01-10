---
title: Comment le Lazy Loading fonctionne dans le développement web
subtitle: ''
author: Sudheer Kumar Reddy Gowrigari
co_authors: []
series: null
date: '2024-01-04T01:08:30.000Z'
originalURL: https://freecodecamp.org/news/how-lazy-loading-works-in-web-development
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/A-simple-banner-image-depicting-the-concept-of-lazy-loading-images.png
tags:
- name: performance
  slug: performance
- name: web performance
  slug: web-performance
seo_title: Comment le Lazy Loading fonctionne dans le développement web
seo_desc: "In the ever-evolving landscape of web development, performance optimization\
  \ remains a top priority. \nAmong the plethora of strategies you can use to enhance\
  \ web performance, lazy loading stands out for its efficiency and impact. \nBut\
  \ what exactly is ..."
---

Dans le paysage en constante évolution du développement web, l'optimisation des performances reste une priorité absolue. 

Parmi la multitude de stratégies que vous pouvez utiliser pour améliorer les performances web, le lazy loading se distingue par son efficacité et son impact. 

Mais qu'est-ce que le lazy loading exactement, et comment révolutionne-t-il la manière dont nous gérons les ressources web ? C'est ce que nous allons couvrir dans cet article.

## Qu'est-ce que le Lazy Loading ?

Le lazy loading est une stratégie d'optimisation des performances web qui joue un rôle critique dans la manière dont les ressources sont chargées sur une page web. 

Traditionnellement, lorsque vous accédez à une page web, le navigateur tente de charger toutes les ressources (images, scripts, feuilles de style) immédiatement. Cela peut entraîner des temps de chargement plus longs, surtout si la page contient de nombreux fichiers volumineux. 

Le lazy loading résout ce problème en marquant certaines ressources comme non bloquantes ou non critiques, les chargeant uniquement lorsqu'elles sont nécessaires. Cette méthode est particulièrement efficace pour les éléments qui ne sont pas immédiatement visibles lors du chargement initial de la page, comme les images et les vidéos qui apparaissent plus bas sur la page.

### Principaux avantages du lazy loading :

* **Performances améliorées** : En chargeant uniquement les ressources nécessaires, le chargement initial de la page est plus rapide, ce qui améliore l'expérience utilisateur.
* **Réduction de l'utilisation de la bande passante** : Le lazy loading minimise la quantité de données à transférer initialement, économisant ainsi la bande passante pour l'utilisateur et le serveur.
* **Engagement utilisateur accru** : Des temps de chargement plus rapides entraînent généralement des taux de rebond plus faibles et un engagement plus élevé, car les utilisateurs sont moins susceptibles de quitter un site lent.

Le lazy loading peut être implémenté de diverses manières, la méthode la plus courante étant basée sur JavaScript. Mais les pratiques modernes de développement web ont introduit des moyens natifs en HTML pour implémenter le lazy loading, comme l'attribut loading pour les images.

## Le rôle de l'attribut de chargement d'image dans le Lazy Loading

Alors que nous approfondissons les aspects pratiques du lazy loading, vous verrez que l'attribut [loading](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#loading) dans l'élément [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img) est un changement de jeu. 

Cet attribut, une addition relativement récente à la spécification HTML, offre un moyen simple mais puissant d'implémenter le lazy loading de manière native, sans avoir besoin de JavaScript supplémentaire. En utilisant l'attribut loading, vous pouvez améliorer significativement les performances web et l'expérience utilisateur, surtout sur les sites web riches en contenu.

### Lazy Loading au niveau du navigateur

Principalement, des navigateurs comme Chrome et Firefox supportent l'attribut loading pour les éléments <img> et <iframe>. En utilisant loading="lazy", le navigateur retarde le chargement des images jusqu'à ce qu'elles soient proches de la fenêtre d'affichage. 

Cette méthode est efficace et améliore les performances en chargeant les images uniquement lorsqu'elles sont susceptibles d'être vues par l'utilisateur. Mais il est important de noter que la valeur lazy pour les éléments <iframe> n'est pas encore standardisée et peut subir des changements.

Regardons quelques exemples pour voir comment cela fonctionne.

#### Chargement paresseux de base d'une seule image

```html
<img src="image-1.jpg" alt="Un paysage pittoresque" loading="lazy">
```

Dans cet exemple, l'attribut `loading="lazy"` dans la balise `<img>` indique au navigateur de retarder le chargement de cette image jusqu'à ce qu'elle soit sur le point d'entrer dans la fenêtre d'affichage. Cela signifie que l'image ne se chargera pas lorsque la page se charge initialement, mais seulement lorsque l'utilisateur fait défiler près d'elle.

#### Chargement paresseux avec des images de haute priorité

```html
<img src="logo.jpg" alt="Logo de l'entreprise" loading="eager"> 
<img src="featured.jpg" alt="Produit en vedette" loading="lazy">
```

Ici, la première image (logo) utilise `loading="eager"`, qui est le comportement par défaut pour charger l'image immédiatement. C'est utile pour les images importantes qui doivent être vues tout de suite. La deuxième image (produit en vedette) utilise `loading="lazy"`, idéal pour les images qui ne sont pas critiques à voir immédiatement.

#### Chargement paresseux dans une galerie

```html
<img src="gallery-image-1.jpg" alt="Image de galerie 1" loading="lazy"> 
<img src="gallery-image-2.jpg" alt="Image de galerie 2" loading="lazy">
<img src="gallery-image-3.jpg" alt="Image de galerie 3" loading="lazy">
```

Pour les galeries d'images, l'utilisation de `loading="lazy"` pour chaque image garantit que les images se chargent au fur et à mesure que l'utilisateur fait défiler la galerie, améliorant ainsi le temps de chargement de la page et réduisant l'utilisation de la bande passante.

**Combiner le Lazy Loading avec la Direction Artistique**

La direction artistique dans la conception web fait référence à la pratique d'adapter la présentation du contenu pour s'adapter à différents contextes, appareils ou démographiques. Elle implique souvent l'utilisation de différentes images ou styles visuels pour transmettre un message ou un sentiment spécifique qui résonne avec divers segments d'audience ou s'adapte à différentes tailles d'écran.

Par exemple, un site web peut afficher une image détaillée et grande sur un ordinateur de bureau, mais une image plus simple et plus petite sur un appareil mobile, toutes deux délivrant le même message mais optimisées pour leurs contextes de visualisation respectifs. 

Voici comment vous pouvez implémenter cela avec le lazy loading :

```html
<picture>
  <source media="(min-width: 800px)" srcset="large.jpg" loading="lazy">
  <source media="(min-width: 400px)" srcset="medium.jpg" loading="lazy">
  <img src="small.jpg" alt="Image réactive" loading="lazy">
</picture>
```

Dans ce code, l'élément `<picture>` contient plusieurs éléments `<source>`, chacun avec un attribut `srcset` différent pour différentes tailles d'écran, et un élément `<img>` par défaut. L'attribut `loading="lazy"` est ajouté à chaque source pour activer le lazy loading.

### Intersection Observer pour le Polyfilling

L'API Intersection Observer est une API web moderne qui fournit un moyen d'observer de manière asynchrone les changements dans l'intersection d'un élément cible avec un élément ancêtre ou la fenêtre d'affichage. Essentiellement, elle permet d'exécuter du code lorsqu'un élément entre ou sort de la fenêtre d'affichage, ce qui est parfait pour le lazy loading des images.

Le polyfilling est une technique dans le développement web où la fonctionnalité moderne est répliquée dans les anciens navigateurs qui ne supportent pas cette fonctionnalité de manière native. Un polyfill est un morceau de code (généralement JavaScript) qui fournit la technologie que les développeurs s'attendent à ce que le navigateur fournisse de manière native.

En ce qui concerne le lazy loading, si un navigateur ne supporte pas l'attribut `loading`, nous pouvons utiliser l'Intersection Observer comme un polyfill pour obtenir un comportement de lazy loading.

Cette méthode basée sur JavaScript implique l'observation des éléments `<img>` pour déterminer leur visibilité dans la fenêtre d'affichage. Lorsqu'une image devient visible, ses attributs `src` et `srcset` sont mis à jour pour charger l'image réelle. 

Cette méthode nécessite un balisage supplémentaire, y compris un attribut de classe pour la sélection, un attribut `src` pour une image de remplacement, et des attributs `data-src` et `data-srcset` pour les URL des images réelles.

#### D'abord, la configuration HTML :

```html
<img class="lazy" src="placeholder.jpg" data-src="actual-image.jpg" alt="Description">
```

* `class="lazy"` : Un identifiant de classe pour la sélection JavaScript.
* `src` : Une URL d'image de remplacement.
* `data-src` : L'URL de l'image réelle à charger.

#### Ensuite, le JavaScript :

```javascript
document.addEventListener("DOMContentLoaded", function() {
  var lazyImages = [].slice.call(document.querySelectorAll("img.lazy"));

  if ("IntersectionObserver" in window) {
    let lazyImageObserver = new IntersectionObserver(function(entries, observer) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          let lazyImage = entry.target;
          lazyImage.src = lazyImage.dataset.src;
          lazyImage.classList.remove("lazy");
          lazyImageObserver.unobserve(lazyImage);
        }
      });
    });

    lazyImages.forEach(function(lazyImage) {
      lazyImageObserver.observe(lazyImage);
    });
  } else {
    // Solution de repli pour les navigateurs sans support de l'Intersection Observer
  }
});

```

Cette section de code montre comment vous pouvez utiliser l'API Intersection Observer pour implémenter le lazy loading. Elle vérifie si l'Intersection Observer est supporté dans le navigateur et, si c'est le cas, l'utilise pour charger les images uniquement lorsqu'elles entrent dans la fenêtre d'affichage.

## Conclusion

L'utilisation du lazy loading, en particulier grâce à l'attribut **loading** en HTML, peut grandement vous aider à améliorer les performances web. En différant sélectivement le chargement des images et des iframes jusqu'à ce qu'elles soient nécessaires, cette technique non seulement améliore la vitesse et l'efficacité des pages web, mais contribue également à une expérience utilisateur plus fluide et réactive. 

Que vous appliquiez le lazy loading à des images individuelles, des galeries ou des mises en page réactives complexes, la polyvalence de l'attribut loading vous permet de répondre à divers scénarios de développement web, garantissant que les ressources sont utilisées de manière efficace et efficiente. 

Alors que les technologies web continuent d'évoluer, l'adoption de telles stratégies centrées sur les performances deviendra de plus en plus vitale pour fournir un contenu qui répond aux attentes des utilisateurs web modernes.