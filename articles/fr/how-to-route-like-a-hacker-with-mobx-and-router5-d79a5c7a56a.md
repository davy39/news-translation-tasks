---
title: Comment router comme un hacker avec MobX et router5
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-23T09:10:38.000Z'
originalURL: https://freecodecamp.org/news/how-to-route-like-a-hacker-with-mobx-and-router5-d79a5c7a56a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*HFkjeBT-TZJ2e-4idMK3Gw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment router comme un hacker avec MobX et router5
seo_desc: 'By Eugen Kiss

  Routing that fits your app — not the other way round


  _Photo by [Unsplash](https://unsplash.com/photos/AyYW_bUWerc?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
  rel="noopener" target="_blank" title="">Rob Bates on ...'
---

Par Eugen Kiss

#### **Routing qui s'adapte à votre application** — et non l'inverse

![Image](https://cdn-media-1.freecodecamp.org/images/1*HFkjeBT-TZJ2e-4idMK3Gw.jpeg)
_Photo par [Unsplash](https://unsplash.com/photos/AyYW_bUWerc?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Rob Bates</a> sur <a href="https://unsplash.com/search/photos/route?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Il existe de nombreuses façons d'aborder le routage dans les applications côté client. Des frameworks comme Android fournissent des mécanismes de routage puissants mais aussi complexes et parfois restrictifs. Il en va de même pour les bibliothèques de routage complètes dans le frontend comme React Router.

La bonne nouvelle est que vous pouvez écrire votre propre couche de routage qui est plus simple sans perdre le contrôle : **Routing qui s'adapte à votre application** — et non l'inverse !

Pour illustrer ces concepts, écrivons une application HackerNews et **prenons le contrôle du routage**. Nous utiliserons [React](https://reactjs.org/), [MobX](https://mobx.js.org/) et [router5](http://router5.github.io/).

![Image](https://cdn-media-1.freecodecamp.org/images/1*2cCaL3YcvzflnIjfzyMAmw.png)

Voici le résultat [live](https://codesandbox.io/s/github/eugenkiss/hacker-routing-mobx-router5) :

L'exemple utilise l'API [HNPWA](https://github.com/tastejs/hacker-news-pwas/blob/master/docs/api.md). [Voici le projet Github](https://github.com/eugenkiss/hacker-routing-mobx-router5/).

Commençons par définir la route _Feed_ :

Les propriétés `name`, `path` et `comp` sont évidentes. Avec `link`, vous avez **un routage inverse assisté par type**. Dans la fonction de cycle de vie `activate`, vous mettez à jour l'état global et effectuez des requêtes API. La dépendance `store` est votre panneau de contrôle central pour la gestion de l'état et des actions. Dans la dernière ligne, vous ajoutez `FeedRoute` à votre registre de routes `routes`.

Le point intéressant à propos de `FeedRoute` est que **tout ce qui est pertinent pour le routage vers/depuis l'écran _Feed_ est défini en un seul endroit**. De plus, vous n'avez pas besoin d'un composant conteneur pour effectuer des requêtes API.

Voici comment vous rendez la route actuelle :

La propriété observable `store.route` contient la route actuelle. Dans votre registre de routes `store.routes`, vous trouvez la définition de route correspondante. Ainsi, vous savez quel composant rendre. Si vous êtes sur `/`, le composant sera `<FeedScreen />`. En étant un observateur, App se rerend à chaque fois que l'observable `store.route` change.

**C'est l'essentiel !**

#### Installation

Comment configurer tout cela avec [MobX](https://mobx.js.org/) et [router5](http://router5.github.io/) ? Qui met à jour la route actuelle ? À quoi ressemble `store` ? Pour le découvrir, continuez à lire !

_À part_ : Bien qu'une bibliothèque de routage ne soit pas requise, je recommande router5. Elle vous offre une API plus pratique (+ hooks et utilitaires) que celle native du navigateur.

La définition du plugin router5 :

Un [plugin router5](http://router5.github.io/docs/plugins.html) implémente des fonctions de cycle de vie. En cas de transition réussie, vous désactivez la route précédente. Ensuite, vous définissez `store.route` sur la route suivante et activez la route suivante. La désactivation effectue le nettoyage. L'activation effectue les requêtes API et d'autres logiques d'initialisation. Le reste du code est spécifique à l'API router5.

Voici les parties pertinentes de `store` :

Le flux sélectionné est dérivé de l'URL. **Il n'y a pas de duplication d'état grâce au [pouvoir de propagation de MobX](https://hackernoon.com/becoming-fully-reactive-an-in-depth-explanation-of-mobservable-55995262a254)** !

_À part_ : J'utilise un helper de récupération spécial qui sera le sujet d'un autre article.

Dans mon propre [client HackerNews](https://github.com/eugenkiss/hnclient/) ([live](https://hn.eugenkiss.com/)), une pile d'historique garde une trace des routes visitées. Elle est utilisée pour rendre les écrans les uns sur les autres. Tous les écrans sauf celui du dessus ont `display` défini sur `none`. Cela rend le retour à l'écran précédent sur les appareils mobiles **beaucoup plus rapide** !

Mon routeur effectue également la restauration de l'état de la vue. Pensez à la position de défilement. Mais vous pouvez tout aussi bien le garder aussi minimal que montré ici. Souvenez-vous, vous êtes en contrôle du routage : faites-le de la manière la mieux adaptée à votre application. Voir aussi la discussion sur la [restauration du défilement](https://reacttraining.com/react-router/web/guides/scroll-restoration) de React Router et la discussion sur le [chargement de données asynchrones](http://router5.github.io/docs/async-data.html) de router5.

L'approche présentée est inspirée par :

* [Comment découpler l'état et l'UI (vous n'avez pas besoin de componentWillMount)](https://hackernoon.com/how-to-decouple-state-and-ui-a-k-a-you-dont-need-componentwillmount-cc90b787aa37)
* [Une approche différente du routage dans les applications monopages](https://vincent.is/testing-a-different-spa-routing/)

Si vous avez aimé cet article, veuillez le recommander et le partager. Bon routage !