---
title: Comment ajouter un lien "Aller au contenu principal" à votre site web
subtitle: ''
author: Joseph Mawa
co_authors: []
series: null
date: '2022-07-20T16:30:05.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-skip-to-main-content-links-to-a-website
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/man-sitting-infront-of-conputer.jpg
tags:
- name: a11y
  slug: a11y
- name: Accessibility
  slug: accessibility
- name: best practices
  slug: best-practices
- name: Web Development
  slug: web-development
seo_title: Comment ajouter un lien "Aller au contenu principal" à votre site web
seo_desc: 'Websites and web applications have increasingly become more complex. But
  it''s still our responsibility, as web developers, to strive for the highest level
  of accessibility we possibly can.

  This isn''t always easy, as the range of user accessibility ne...'
---

Les sites web et les applications web sont devenus de plus en plus complexes. Mais il reste de notre responsabilité, en tant que développeurs web, de viser le plus haut niveau d'accessibilité possible.

Ce n'est pas toujours facile, car la gamme des besoins d'accessibilité des utilisateurs peut compliquer encore plus les choses.

Heureusement, diverses directives existent pour concevoir et construire des sites web et des applications web plus accessibles. Cet article examinera la fonctionnalité d'accessibilité web apparemment banale, moins connue et souvent négligée : le lien "aller au contenu principal".

Parce qu'ils sont invisibles par défaut, de nombreux utilisateurs naviguant sur un site web en utilisant la méthode habituelle de point-et-clic ne remarqueront même pas les liens aller-au-contenu-principal. Mais ces liens sont cruciaux, car ils rendent la navigation sur des sites web complexes et volumineux plus simple pour les utilisateurs du clavier uniquement et certains utilisateurs de lecteurs d'écran.

Dans la section ci-dessous, nous examinerons en détail les liens "aller au contenu principal" et pourquoi vous devriez envisager de les implémenter dans votre site web ou votre application web.

## Qu'est-ce qu'un lien "Aller au contenu principal" ?

La plupart des sites web sont généralement dotés de menus de navigation pour faciliter la navigation. Mais bien qu'ils rendent votre site web ou votre application web navigable pour les utilisateurs de la méthode point-et-clic, les menus de navigation peuvent également causer une mauvaise expérience utilisateur pour les utilisateurs du clavier uniquement et certains utilisateurs de lecteurs d'écran.

Il n'est pas rare qu'un site web typique ait un menu de navigation avec jusqu'à dix éléments de menu en haut de chaque page web. Ainsi, un utilisateur du clavier uniquement devra inutilement tabuler à travers tous les liens de navigation avant d'accéder au contenu principal des pages qu'il visite.

Certains utilisateurs de lecteurs d'écran peuvent subir une expérience similaire en traversant tous les éléments de menu avant d'atteindre le contenu principal.

Cela crée une expérience négative pour vos utilisateurs. L'ajout de liens aller-au-contenu peut rendre la navigation sur de tels sites complexes plus facile et moins laborieuse pour les utilisateurs du clavier uniquement et certains utilisateurs de lecteurs d'écran.

Un lien "aller au contenu" est un lien ordinaire, généralement avant le menu de navigation principal en haut, reliant au contenu principal de la page web. Puisqu'un utilisateur point-et-clic n'en a pas besoin, un lien "aller au contenu principal" est généralement caché et rendu visible lorsqu'il est en focus.

Il aide les utilisateurs du clavier uniquement et les utilisateurs de lecteurs d'écran à sauter au contenu principal au lieu de traverser tous les éléments de menu. Et cela améliore grandement leur expérience de navigation.

L'image ci-dessous montre le lien aller-au-contenu-principal pour le [projet a11y](https://www.a11yproject.com/). Comme mentionné ci-dessus, le lien aller-au-contenu-principal n'est visible qu'après avoir été mis en focus.

Pour le tester, naviguez vers [a11yproject.com](https://www.a11yproject.com/) et appuyez sur la touche Tab. Le lien aller-au-contenu-principal devient immédiatement visible. Après cela, vous pouvez appuyer sur la touche Entrée pour sauter le menu de navigation.

![Lien aller au contenu principal sur le site web du projet a11y](https://www.freecodecamp.org/news/content/images/2022/07/skip-to-main-content-link.png align="left")

*Lien aller au contenu principal sur le site web du projet a11y*

Dans la section suivante, nous allons implémenter un simple lien aller-au-contenu-principal.

## Comment ajouter un lien "Aller au contenu principal" à votre site

Maintenant que nous savons ce que sont les liens "aller au contenu principal", voyons comment les implémenter et quelques bonnes pratiques lors de leur utilisation.

Comme déjà mentionné dans l'introduction, les liens aller-au-contenu-principal sont des liens ordinaires.

Mais encore une fois, ils ne sont généralement pas visibles pour un utilisateur ordinaire point-et-clic. Vous pouvez changer la visibilité du lien aller-au-contenu-principal pour l'utilisateur du clavier lorsqu'il est en focus.

Le code ci-dessous montre le balisage pour un menu de navigation typique. Une application réelle peut être plus complexe avec des éléments de menu imbriqués en plus des éléments de menu de premier niveau. Mais je l'ai gardé simple dans l'exemple ci-dessous.

```html
  <body>
    <a href="#main" class="skip-to-main-content-link">Aller au contenu principal</a>
    <nav>
      <ul>
        <li>
          <a href="/">Accueil</a>
        </li>
        <li>
          <a href="/about.html">À propos</a>
        </li>
        <li>
          <a href="/blog.html">Blog</a>
        </li>
        <li>
          <a href="/contact.html">Contact</a>
        </li>
        <li>
          <a href="/portfolio.html">Portfolio</a>
        </li>
      </ul>
    </nav>
    <main id="main">
      <h1>Votre titre accrocheur</h1>

      <!-- Le contenu de la page va ici ! -->
    </main>
  </body>
```

Le premier élément de la balise `<body>` dans l'exemple ci-dessus est le lien aller-au-contenu-principal. Son attribut `href` pointe vers l'élément `main` via son attribut `id`. Cliquer ou appuyer sur la touche Entrée lorsque le lien aller-au-contenu-principal est en focus fera défiler le contenu principal dans la vue dans le viewport.

Comme souligné dans la section précédente, le lien aller-au-contenu-principal est principalement destiné aux utilisateurs du clavier uniquement et à certains utilisateurs de lecteurs d'écran. Nous devons donc appliquer un certain style pour le cacher de la vue lorsqu'il n'est pas en focus et l'afficher lorsqu'il reçoit le focus.

Nous le sélectionnons donc en utilisant la classe donnée et appliquons le style ci-dessous. Vous pouvez cacher et afficher le lien de saut avec différents styles. Cela n'a pas besoin d'être le même code que ci-dessous.

```css
.skip-to-main-content-link {
  position: absolute;
  left: -9999px;
  z-index: 999;
  padding: 1em;
  background-color: black;
  color: white;
  opacity: 0;
}
.skip-to-main-content-link:focus {
  left: 50%;
  transform: translateX(-50%);
  opacity: 1;
}
```

Vous pouvez également appliquer une animation de transition à votre lien aller-au-contenu-principal, bien que je ne l'aie pas inclus dans l'exemple ci-dessus.

## Bonnes pratiques lors de l'ajout d'un lien "Aller au contenu principal"

Bien que les liens aller-au-contenu-principal soient faciles à implémenter, il existe certains problèmes potentiels qui peuvent facilement vous échapper.

Suivez ce que je considère comme de bonnes pratiques ci-dessous lors de l'implémentation de liens aller-au-contenu-principal. Je les ai tirées des [techniques WCAG](https://www.w3.org/TR/WCAG20-TECHS/G1.html).

* Si le lien aller au contenu principal est destiné à sauter le menu de navigation principal en haut d'une page web, il doit être le premier élément focusable sur la page web.

* Le texte du lien de saut doit décrire l'intention. Le texte "Aller au contenu principal" suffira généralement.

* Il est requis que le lien aller-au-contenu soit soit toujours visible, soit visible lorsqu'il est en focus. Puisque notre lien aller-au-contenu est destiné aux utilisateurs du clavier uniquement et à certains utilisateurs de lecteurs d'écran, vous pouvez le cacher et le rendre visible comme nous l'avons fait dans l'exemple ci-dessus.

* Le focus doit se déplacer vers le contenu principal après l'activation du lien de saut.

Il est utile de souligner que l'utilisation de liens de saut n'est pas limitée aux menus de navigation. Vous pouvez également implémenter des liens pour aider les utilisateurs à sauter des éléments focusables qui sont difficiles ou laborieux à naviguer avec le clavier.

## Conclusion

Un menu de navigation est une fonctionnalité pratique pour naviguer vers différentes sections ou pages d'un site web. Et bien qu'il soit destiné à fournir une meilleure expérience utilisateur, un menu de navigation peut devenir un obstacle d'accessibilité pour certains utilisateurs qui n'utilisent que le clavier ou qui utilisent un lecteur d'écran.

C'est pourquoi il est bon d'ajouter des liens aller-au-contenu-principal sur chaque page. Lorsque les utilisateurs doivent traverser les éléments du menu de navigation, ils peuvent utiliser ce lien pour contourner le menu de navigation.

Le lien aller-au-contenu-principal est un lien ordinaire qui est invisible pour l'utilisateur point-et-clic. Il est visible pour les utilisateurs de lecteurs d'écran et lorsqu'il est en focus. Cliquer dessus déplacera le focus vers le contenu principal de la page web.

Espérons que cet article vous a donné des informations sur les liens aller-au-contenu-principal et comment les implémenter dans votre site web ou votre application web.

L'accessibilité est un voyage. Chaque pas que vous faites dans la bonne direction rend votre site ou votre application web plus accessible. L'implémentation de liens aller-au-contenu-principal est l'une de ces étapes. Faites ce pas et rendez le web plus accessible si vous ne l'avez pas encore fait. En faisant cela, vous enrichissez l'expérience numérique pour vos clients.