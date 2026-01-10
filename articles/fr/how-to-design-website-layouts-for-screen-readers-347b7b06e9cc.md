---
title: Comment concevoir des mises en page de sites web pour les lecteurs d'écran
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-15T21:59:30.000Z'
originalURL: https://freecodecamp.org/news/how-to-design-website-layouts-for-screen-readers-347b7b06e9cc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ya6t6_FIW5mxVPYrX1rLZw.jpeg
tags:
- name: Accessibility
  slug: accessibility
- name: Design
  slug: design
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
- name: Web Development
  slug: web-development
seo_title: Comment concevoir des mises en page de sites web pour les lecteurs d'écran
seo_desc: 'By Ben Robertson

  It’s easy to think about a layout as being a primarily visual concern. The header
  goes up top, the sidebar is over here, the call to action is in an overlay on top
  of the content (just kidding). Grids, borders, spacing and color all ...'
---

Par Ben Robertson

Il est facile de considérer une mise en page comme une préoccupation principalement visuelle. L'en-tête est en haut, la barre latérale est ici, l'appel à l'action est dans une superposition au-dessus du contenu (je plaisante). Les grilles, les bordures, l'espacement et la couleur transmettent tous des données visuelles précieuses, mais si ces indices sur la structure d'une page sont uniquement visuels, certains utilisateurs peuvent trouver votre contenu incompréhensible.

Vous pouvez vivre cette expérience en première main si vous essayez d'utiliser un lecteur d'écran sur le web. Lorsque j'ai lancé VoiceOver sur mon Mac et que je l'ai testé, j'ai réalisé que pour un utilisateur de lecteur d'écran, beaucoup de pages sont simplement un grand tas de « contenu », manquant d'indices organisationnels utiles.

L'expérience peut être un peu comme écouter une longue histoire décousue sans aucune indication sur les détails importants ou liés au fil principal de l'histoire. À mi-chemin de l'histoire, vous n'êtes pas sûr qu'il vaille la peine de continuer à écouter parce que vous ne savez pas si vous trouverez même ce que vous cherchez.

Dans le contexte d'un site web, votre lecteur d'écran peut être à mi-chemin de la lecture d'une liste de 50 liens de barre latérale lorsque vous commencez à vous demander s'il y a du contenu précieux sur le site.

Des expériences comme celle-ci sont causées par des sites web construits avec des mises en page uniquement visuelles. Idéalement, cependant, nos mises en page visuelles devraient pointer vers un modèle organisationnel sous-jacent de notre contenu. Elles devraient être des indicateurs visuels pour un modèle conceptuel. Les indicateurs visuels ne sont qu'un moyen de révéler ce modèle. L'initiative d'accessibilité du Web, ARIA (Accessible Rich Internet Applications), fournit des indicateurs alternatifs aux utilisateurs qui peuvent en avoir besoin.

Je vais vous montrer comment utiliser ces indicateurs pour rendre une simple page web facile à utiliser, à naviguer et à lire pour les utilisateurs de technologies d'assistance. Tout le code exemple est disponible sur [GitHub](https://github.com/mergeweb/screen-reader-layout-post).

### Mise en page initiale

Voici un exemple de page avec une mise en page assez simple. Nous avons un en-tête en haut contenant un logo et une navigation, du contenu principal, une barre latérale à droite avec une liste de publications connexes et une liste de liens de partage sur les réseaux sociaux, une boîte de recherche sous le contenu, et un pied de page contenant les informations de contact de notre entreprise.

![Image](https://cdn-media-1.freecodecamp.org/images/sToP4q2e9CzSv265lsPQogHFhhxtLYx8iA59)
_Capture d'écran de la mise en page initiale._

* [Prévisualiser la mise en page initiale](https://mergeweb.github.io/screen-reader-layout-post/)
* [Voir le HTML](https://github.com/mergeweb/screen-reader-layout-post/blob/master/index.html)

Visuellement, le contenu est assez bien divisé, utilisant une grille simple et des couleurs de fond pour distinguer les différents éléments. Si vous lancez VoiceOver sur cette page, vous pouvez naviguer à travers la page assez bien en utilisant la commande de l'élément suivant. L'ordre des éléments dans le balisage suit presque l'ordre visuel des éléments. D'abord, nous lisons l'en-tête, puis le corps du texte, puis la barre latérale, puis la boîte de recherche, puis le pied de page. C'est assez bien. Si j'appuie sur `CAPS + U` pour faire apparaître les menus VoiceOver, je peux obtenir une liste de tous les en-têtes de la page et de tous les liens, et naviguer directement vers eux.

![Image](https://cdn-media-1.freecodecamp.org/images/dEm-7w25itlnNZy7XnBizLjKG0TBlMvqlvsp)
_VoiceOver affichera une liste navigable de tous les en-têtes d'une page._

![Image](https://cdn-media-1.freecodecamp.org/images/4XfsFEYp9exPBgzIH79QNPawvk0bfcWP6GDC)
_VoiceOver affichera également une liste navigable de tous les liens d'une page._

Simplement en utilisant un HTML bien structuré, un regroupement simple avec des éléments `<div>` et une bonne utilisation des balises d'en-tête, nous avons une expérience décente. C'est mieux que les sites web d'histoires décousues dont j'ai parlé plus haut, mais cela pourrait être encore mieux.

### Lien de saut

* [Prévisualiser la mise en page avec lien de saut](https://mergeweb.github.io/screen-reader-layout-post/skip-link.html)
* [Voir le HTML](https://github.com/mergeweb/screen-reader-layout-post/blob/master/skip-link.html)

Tout d'abord, nous allons ajouter un lien de saut comme premier élément de la page. Un lien de saut est une fonctionnalité d'accessibilité très courante qui permet aux utilisateurs de sauter les longues listes de liens et autres informations répétées sur chaque page web directement au contenu principal de la page actuelle. C'est un lien qui est le premier élément dans l'ordre de tabulation de la page.

Juste à l'intérieur de la balise d'ouverture du corps, ajoutons :

```
<a href="#main" class="skip">Aller au contenu principal</a>
```

Nous voudrons également masquer ce lien visuellement, mais le faire apparaître à l'écran lorsqu'il reçoit le focus. Pour masquer visuellement le lien, nous ajouterons le CSS suivant :

```css
.skip { 
    clip: rect(1px, 1px, 1px, 1px); 
    position: absolute !important; 
    height: 1px; 
    width: 1px; 
    overflow: hidden; 
    word-wrap: normal !important; /* De nombreuses combinaisons de lecteurs d'écran et de navigateurs annoncent les mots coupés tels qu'ils apparaîtraient visuellement. */ } 
/* Afficher le lien au focus. */ 
.skip:focus { 
    background-color: #fff; 
    border-radius: 3px; 
    box-shadow: 0 0 2px 2px rgba(0, 0, 0, 0.6); 
    clip: auto !important; 
    color: #888; 
    display: block; 
    font-weight: bold; 
    height: auto; left: 5px; 
    line-height: normal; 
    padding: 15px 23px 14px; 
    text-decoration: none; 
    top: 5px; 
    width: auto; 
    z-index: 100000;
}
```

L'emplacement du lien de saut doit être un `id` pointant vers le contenu principal de la page. Dans notre cas, j'ai ajouté `id="main"` à la section `<div class="content">` et donné au lien de saut une URL de `href="#main"`.

Si vous visitez la [page de lien de saut](https://mergeweb.github.io/screen-reader-layout-post/skip-link.html) et appuyez sur votre touche Tab, le lien devrait s'afficher. Si vous lancez VoiceOver et commencez à naviguer à travers la page, le lien de saut devrait être la première chose que vous rencontrez, et cliquer dessus devrait déclencher VoiceOver pour commencer à lire le contenu principal de la page.

### Techniques WCAG utilisées

Avec cette étape, nous avons permis aux utilisateurs de sauter directement au cœur de notre page, mais au-delà de l'accès facile au contenu principal, ils n'ont toujours pas une bonne carte conceptuelle du reste de la page.

### Rôles et repères ARIA

Une façon de fournir aux utilisateurs une carte conceptuelle de la page est d'utiliser des éléments HTML5 sémantiques comme `<header>`, `<nav>`, `<main>`, `<section>`, et `<aside>`. Ces éléments ont des données intégrées qui leur sont associées et qui sont analysées par les navigateurs et les lecteurs d'écran. Ils créent des repères sur une page web. En utilisant judicieusement ces éléments à la place des éléments `<div>`, nous pouvons fournir des informations supplémentaires aux dispositifs de technologie d'assistance et aider l'utilisateur à construire une carte conceptuelle de notre page.

J'ai maintenu la même mise en page qu'auparavant, mais j'ai remplacé certaines divs par des éléments HTML5 sémantiques. J'ai également ajouté un attribut `role` au composant de recherche. Alternativement, vous pourriez garder toutes les divs et ajouter un `role` au lieu de les remplacer par les nouveaux éléments HTML5. (Voir [les directives du w3 pour les rôles ARIA](https://www.w3.org/TR/wai-aria/roles#landmark_roles))

* [Prévisualiser la mise en page mise à jour](https://mergeweb.github.io/screen-reader-layout-post/aria-roles.html)
* [Voir le HTML mis à jour](https://github.com/mergeweb/screen-reader-layout-post/blob/master/aria-roles.html)

Voici les changements clés :

* `<div class="header">` devient `<header class="header">`
* `<div class="main-navigation">` devient `<nav class="main-navigation">`
* `<div class="content">` devient `<main class="content">`
* `<div class="sidebar">` devient `<aside class="sidebar">`
* `<div class="related-posts">` devient `<section class="related-posts">`
* `<div class="search">` devient `<div class="search" role="search">`

Maintenant, lorsque je lance VoiceOver et que j'appuie sur `CAPS + U`, j'obtiens un nouveau menu Repères. Dans ce menu, vous pouvez voir les éléments suivants :

* bannière
* navigation
* principal
* complémentaire
* recherche
* informations de contenu

La sélection de l'un de ces éléments de menu amène l'utilisateur directement à cet élément, afin qu'il puisse facilement naviguer à travers les différents éléments d'une page. S'ils sont en bas de la page, ils peuvent facilement revenir à la navigation principale dans l'en-tête via le menu Repères.

### Techniques WCAG utilisées

Nous avons considérablement augmenté la navigabilité de notre page et fourni une carte initiale à nos utilisateurs, mais il nous manque quelques éléments pour rendre cette expérience vraiment géniale. Tout d'abord, les noms de nos sections de site sont assez génériques. Nous ne sommes pas exactement sûrs, simplement en écoutant le menu, de ce qui pourrait se trouver dans l'un des éléments. Deuxièmement, certains éléments ne sont pas facilement navigables. Par exemple, nos composants de barre latérale sont tous regroupés sous l'étiquette « complémentaire ».

Nous pouvons ajouter des étiquettes ARIA bien pensées pour rendre cette expérience encore meilleure.

### Utilisation d'étiquettes ARIA appropriées

En ajoutant quelques étiquettes ARIA, nous pouvons donner à l'utilisateur une carte conceptuelle encore plus détaillée de notre mise en page.

* [Prévisualiser la mise en page mise à jour](https://mergeweb.github.io/screen-reader-layout-post/aria-labels.html)
* [Voir le HTML mis à jour](https://github.com/mergeweb/screen-reader-layout-post/blob/master/aria-labels.html)

Dans cette prochaine itération, j'ai ajouté les étiquettes suivantes :

* `<nav class="main-navigation">` a maintenant une étiquette `aria-label` de Navigation Principale.
* `<main class="content">` a maintenant un attribut `aria-labelledby` de `main-title` et son `<h1>` a un id de `main-title`.
* `<aside class="sidebar">` a maintenant un attribut `aria-labelledby` de `sidebar-title` et son `<h2>` a un id de `sidebar-title`.
* Les deux éléments `<section>` dans la barre latérale ont maintenant une étiquette ARIA appropriée.

Lançons à nouveau VoiceOver et affichons notre menu Repères avec `CAPS+U`. Maintenant, nous voyons que les étiquettes ARIA que nous avons fournies s'affichent à côté de chacun de nos éléments de menu génériques. Nous avons également quelques éléments de menu supplémentaires, car les éléments `<section>` pour lesquels nous avons fourni des étiquettes (Publications Connexes, Lien de Partage), ont maintenant leurs propres éléments de menu.

![Image](https://cdn-media-1.freecodecamp.org/images/Iof8lGh-MXpEDhBFBMaatLw7tAclX47sur7d)
_Le menu des repères VoiceOver montre maintenant des informations détaillées sur chacune des sections de notre page, y compris les étiquettes aria que nous avons fournies._

Maintenant, un utilisateur de technologie d'assistance a une carte conceptuelle égale (et peut-être même meilleure) du contenu et des actions qu'il peut entreprendre sur ce site web par rapport à un utilisateur non assisté. Il peut obtenir un aperçu rapide de tout ce qui se trouve sur le site, naviguer facilement vers la section de la page qu'il souhaite, et trouver rapidement ce qu'il cherche.

### Techniques WCAG utilisées

* [Repères](https://www.w3.org/TR/WCAG20-TECHS/ARIA11.html)
* [Étiquetage des repères](https://www.w3.org/TR/WCAG20-TECHS/ARIA13.html)

### Conclusion

Avec une combinaison de balisage HTML bien structuré, une utilisation réfléchie des rôles ARIA et un étiquetage soigné des sections du site à l'aide d'étiquettes ARIA, nous sommes en mesure de créer une expérience utilisateur pour les utilisateurs de technologies d'assistance qui rivalise avec l'expérience des utilisateurs non assistés. Nous avons pu prendre la carte conceptuelle qui était implicite dans notre mise en page visuelle et l'exposer aux technologies d'assistance.

Vous pouvez trouver des lacunes dans votre carte conceptuelle ou des sections qui ont inutilement la même fonction. Le processus peut vous aider à clarifier vos conceptions, à identifier les zones qui peuvent ne pas avoir de sens conceptuellement ou visuellement, et à améliorer votre conception pour tous les utilisateurs de votre site.

Vous voulez approfondir la création de sites web accessibles ? Rejoignez mon cours gratuit par e-mail : ? [Erreurs courantes d'accessibilité et comment les éviter.](https://benrobertson.io/courses/common-accessibility-mistakes/) 30 jours, 10 leçons, 100% amusant ! ? [Inscrivez-vous ici.](https://benrobertson.io/courses/common-accessibility-mistakes/)