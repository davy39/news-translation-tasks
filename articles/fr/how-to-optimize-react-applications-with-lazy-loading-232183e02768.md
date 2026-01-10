---
title: Comment optimiser les applications React avec le Lazy Loading ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-13T17:40:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-optimize-react-applications-with-lazy-loading-232183e02768
coverImage: https://cdn-media-1.freecodecamp.org/images/1*q_x1W90t0HLSSGGfngWqUA.png
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
seo_title: Comment optimiser les applications React avec le Lazy Loading ?
seo_desc: 'By Al-amin Nowshad

  For your components, images, and what not


  Lazy loading is an old technique to optimize web applications as well as on mobile
  apps. The thing is pretty straight forward - do not render things if they are not
  viewed or required at t...'
---

Par Al-amin Nowshad

#### Pour vos composants, images, et bien plus encore

![Image](https://cdn-media-1.freecodecamp.org/images/sjshSrV2O2h-aKvcWEDi-XRIW4QF14nZEAQW)

Le lazy loading est une ancienne technique pour optimiser les applications web ainsi que les applications mobiles. Le principe est assez simple : ne pas rendre les éléments s'ils ne sont pas vus ou requis à ce moment-là. Par exemple, si nous avons une liste de publications à afficher, nous devrions initialement rendre uniquement ce qui est visible dans la fenêtre d'affichage. Cela signifie que le reste des éléments sera rendu plus tard, à la demande (quand ils sont dans la fenêtre d'affichage ou sur le point d'y être).

### Pourquoi le Lazy Loading ?

La plupart du temps, nos utilisateurs ne voient pas toute la page web, du moins au début. Peu importe comment l'interface utilisateur de notre application a été structurée, il y a certains composants dont l'utilisateur n'a peut-être pas besoin initialement ou jamais !

Dans ces cas, le rendu de ces composants nuit non seulement aux performances de notre application, mais gaspille également beaucoup de ressources (surtout lorsqu'ils contiennent des images ou des contenus similaires gourmands en données).

Ainsi, charger ou rendre ces composants à la demande semble être une décision plus efficace. Cela peut améliorer les performances de l'application et, en même temps, économiser beaucoup de ressources.

### Comment ?

Nous allons créer une application d'exemple où nous pouvons appliquer le lazy loading. Tout d'abord, nous devons initialiser notre application React en utilisant `create-react-app` avec les commandes suivantes :

```
create-react-app lazydemocd lazydemonpm run start
```

Cela peut prendre quelques minutes pour initialiser et ouvrir notre application React dans le port `3000` du navigateur par défaut.

> Si vous n'avez pas `create-react-app` installé sur votre PC, vous pouvez l'installer avec la commande : `npm install -g create-react-app`

Maintenant, nous allons créer une liste qui affichera quelques publications aléatoires. Alors, obtenons d'abord quelques données factices. Créez un fichier nommé `data.js` à l'intérieur du dossier `src` de notre projet. J'ai simplement copié-collé la réponse `json` de ce point de terminaison de remplissage `JSON` [https://jsonplaceholder.typicode.com/posts](https://jsonplaceholder.typicode.com/posts). Vous pouvez créer vos propres données factices également. Suivre le format ci-dessous devrait être suffisant pour ce tutoriel :

![Image](https://cdn-media-1.freecodecamp.org/images/nYsUwBXnStTJouo42YP5z4dXoK7dCp-XY6tk)
_format data.js_

Remplaçons le contenu du fichier `App.js` par le code ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/70Q5LEimL51EiG1d0FA-RZZRVuDxVyIrSzbU)

![Image](https://cdn-media-1.freecodecamp.org/images/N3MLdKVosCniJCyyJ1LUx480I7Di4xdbWxCq)

Ici, nous créons simplement une liste de `posts` avec leur `titre` et `corps`. Et avec quelques modifications `CSS` simples, nous obtenons la vue de droite. Voici la liste complète rendue en une seule fois. Maintenant, si nous ne voulons pas tout rendre initialement, nous devrions appliquer le `lazy loading`. Installons-le dans notre projet :

Source : [twobin](https://github.com/twobin)/[react-lazyload](https://github.com/twobin/react-lazyload)

```
npm install --save react-lazyload
```

Maintenant, mettons à jour le fichier `App.js` en important et en appliquant `lazyload`.

![Image](https://cdn-media-1.freecodecamp.org/images/w663tm74X4xB8g8SV8XWm0KxAIjBZ0kMAV6R)

L'utilisation de `react-lazyload` est assez simple, il suffit d'envelopper le composant avec `<LazyLoad …> … </LazyLoad>`. Ici, nous utilisons un composant de remplacement `<Loading />` qui affichera "Chargement..." jusqu'à ce que le composant soit chargé. Nous pouvons également définir la hauteur effective et le décalage du composant LazyLoad. Vous pouvez trouver plus de détails dans [la documentation : https://github.com/twobin/react-lazyload#height](https://github.com/twobin/react-lazyload#height).

Maintenant, tous les posts ne sont pas rendus initialement. Seuls quelques-uns seront rendus initialement en fonction de la fenêtre d'affichage. Mais, comme les contenus sont textuels jusqu'à présent, l'effet peut être difficilement réalisé à moins que nous inspections et voyions les changements du DOM lorsqu'ils passent de `loading` à `loaded`.

Pour rendre notre lazy loading plus efficace, incorporons des images dans les posts. Nous utiliserons [Lorem Picsum](https://picsum.photos/) pour nos photos. Notre composant `Post` mis à jour devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/Hxs73x97zu9teR7f2SIwbr6VmmrKVegHz2qe)

> Format de l'URL Lorem Picsum
> https://picsum.photos/id/[image_id]/[width]/[height]

![Image](https://cdn-media-1.freecodecamp.org/images/ge5QAy8G1wGFa7jAiFSlQrAQj3AyQVK4FPsC)
_Le résultat après l'insertion d'images avec les posts_

Maintenant, comme je l'ai dit plus tôt, les images sont des composants gourmands en données d'une page web et ici nous chargeons des images pour chaque post. Bien que le composant entier soit chargé de manière paresseuse et que l'image soit également chargée avec le composant, l'image se charge un peu tard et pas très doucement. Ainsi, nous pouvons offrir une meilleure expérience de chargement d'images pour nos utilisateurs en utilisant LazyLoad pour les images individuelles.

La technique consiste à charger une image de très basse qualité comme espace réservé, puis l'image originale est chargée. Ainsi, le fichier `App.js` final ressemblerait à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/mSb4ic759dFRZMUv90WFKHA73C1rTei-yn89)

Maintenant, nous pouvons faire défiler la liste avec notre élément d'inspection ouvert pour voir comment ces composants changent lorsqu'ils approchent de la fenêtre d'affichage, puis sont rendus et l'espace réservé est remplacé par le contenu réel.

Et nous avons terminé, pour l'instant, notre LazyLoad fonctionne avec toute sa grâce. C'était assez facile !!!

![Image](https://cdn-media-1.freecodecamp.org/images/DSefnSg0oR-EoUpD0QlKsTPVc6yfX1mztNKR)

> Le LazyLoad d'image ici n'est pas le meilleur cas d'utilisation car il est déjà géré par le LazyLoad du composant. Mais, la technique peut être très utile dans d'autres cas d'utilisation où nous devons afficher beaucoup d'images. Essayez de désactiver le LazyLoad sur le composant Post mais gardez le LazyLoad de l'image, vous pouvez voir son effet.

Github : [https://github.com/nowshad-sust/lazydemo](https://github.com/nowshad-sust/lazydemo)

React LazyLoad : [twobin](https://github.com/twobin)/[react-lazyload](https://github.com/twobin/react-lazyload)