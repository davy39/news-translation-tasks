---
title: 'Meilleures pratiques d''accessibilité Web : conseils a11y pour votre site
  web'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-13T21:31:00.000Z'
originalURL: https://freecodecamp.org/news/web-accessibility-best-practices-a11y-tips
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9eb8740569d1a4ca3eb1.jpg
tags:
- name: Accessibility
  slug: accessibility
seo_title: 'Meilleures pratiques d''accessibilité Web : conseils a11y pour votre site
  web'
seo_desc: "This short guide will provide practical examples of how to implement accessibility\
  \ in websites. \nAccessibility was not emphasized during school nor is it being\
  \ emphasized enough in the real world of web development. It is our hope that this\
  \ article, ..."
---

Ce court guide fournira des exemples pratiques de la manière d'implémenter l'accessibilité dans les sites web. 

L'accessibilité n'était pas mise en avant pendant les études, et elle ne l'est pas assez dans le monde réel du développement web. Nous espérons que cet article, ainsi que beaucoup d'autres, encouragera les développeurs à créer des sites accessibles dès maintenant. 

Il a toujours été utile d'avoir des exemples pratiques et concrets de la manière de faire les choses. Ce guide se concentrera donc sur des exemples réels rencontrés dans ma vie quotidienne en tant que développeur web.

### Sauter la navigation

Pour offrir une expérience agréable aux utilisateurs malvoyants sur votre site web, ils doivent pouvoir accéder rapidement et efficacement au contenu. Si vous n'avez jamais expérimenté un site web à travers un lecteur d'écran, je vous recommande de le faire. C'est la meilleure façon de tester la facilité de navigation d'un site pour les utilisateurs non-voyants. NVDA est une très bonne application de lecteur d'écran fournie gratuitement. Si vous utilisez le lecteur d'écran et le trouvez utile, envisagez de faire un don à l'équipe de développement. Le lecteur d'écran peut être téléchargé depuis [nvaccess.org](https://www.nvaccess.org/download/).

Pour permettre aux utilisateurs malvoyants de sauter directement au contenu principal d'un site et éviter de naviguer à travers tous les liens de navigation principaux :

1. Créez un lien "sauter la navigation" qui se trouve directement sous la balise d'ouverture `body`.

```
<a tabindex="0" class="skip-link" href="#contenu-principal">Aller au contenu principal</a>

```

`tabindex="0"` est ajouté pour s'assurer que le lien est accessible via le clavier sur tous les navigateurs. Plus d'informations sur l'accessibilité clavier peuvent être trouvées sur [webaim.org](https://webaim.org/techniques/keyboard/tabindex).  
2. Le lien "sauter la navigation" doit être associé à la balise principale html dans votre document de page web en utilisant la balise ID.

```
<main id="contenu-principal">
...contenu de la page
</main>

```

3. Masquez le lien "sauter la navigation" par défaut. Cela garantit que le lien n'est visible pour les utilisateurs voyants que lorsque le lien est en focus.  
Créez une classe pour le lien qui peut être stylisée avec CSS. Dans mon exemple, j'ai ajouté la classe `skip-link`.

```
.skip-link {
position: absolute;
width: 1px;
height: 1px;
padding: 0;
overflow: hidden;
clip: rect(0, 0, 0, 0);
white-space: nowrap;
-webkit-clip-path: inset(50%);
clip-path: inset(50%);
border: 0;
}
.skip-link:active, .skip-link:focus {
position: static;
width: auto;
height: auto;
overflow: visible;
clip: auto;
white-space: normal;
-webkit-clip-path: none;
clip-path: none;
}

```

Ces styles CSS masquent le lien par défaut et n'affichent le lien que lorsqu'il reçoit le focus du clavier. Pour plus d'informations, visitez le [a11yproject](http://a11yproject.com/posts/how-to-hide-content) et cet [article de blog](http://hugogiraudel.com/2016/10/13/css-hide-and-seek/).

### Structure d'en-tête accessible

* Le rôle "banner" est ajouté à la balise `header` pour indiquer aux lecteurs d'écran que cette balise est la section la plus haute. Le rôle sur le `header` est obsolète en HTML5 mais doit encore être ajouté afin de supporter autant de lecteurs d'écran que possible.
* Ce rôle est ajouté à l'élément `header` lorsqu'il est l'enfant de l'élément `body`.

```
<header role="banner">
</header>  

```

### Structure de contenu principal accessible

* Le rôle "main" est ajouté à la balise `main` pour indiquer aux lecteurs d'écran que cette balise est la section de contenu `main`. Le besoin d'ajouter le rôle sur le `main` est obsolète en HTML5 mais doit encore être ajouté afin de supporter autant de lecteurs d'écran que possible.
* Ce rôle est ajouté à l'élément `main` lorsqu'il est la section de contenu principal de la page. S'il y a plus d'un élément `main`, chaque élément aura besoin d'un attribut `aria-labelledby` ou d'un `aria-label`.
* Plus d'informations peuvent être trouvées sur [https://www.w3.org/TR/2017/NOTE-wai-aria-practices-1.1-20171214/examples/landmarks/main.html](https://5d0c2cfff1d8938bf45c6427--freecodecamp-dev.netlify.com/guide/accessibility/W3C%20Website%20documentation%20for%20Role).

```
<main role="main">
</main>  

```