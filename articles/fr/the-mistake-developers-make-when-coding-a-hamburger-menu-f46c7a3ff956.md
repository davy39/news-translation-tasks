---
title: L'erreur que les développeurs commettent en codant un menu hamburger
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-14T21:57:58.000Z'
originalURL: https://freecodecamp.org/news/the-mistake-developers-make-when-coding-a-hamburger-menu-f46c7a3ff956
coverImage: https://cdn-media-1.freecodecamp.org/images/1*A8jnfDNNH1PexulIn6z2rA.png
tags:
- name: Design
  slug: design
- name: Front-end Development
  slug: front-end-development
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
- name: Web Development
  slug: web-development
seo_title: L'erreur que les développeurs commettent en codant un menu hamburger
seo_desc: 'By Jared Tong

  What do The New York Times’ developers get wrong about the hamburger menu, and what
  do Disney’s and Wikipedia’s get right?

  As far as I know, I’ve found only one way to style the hamburger menu’s open state
  that supports iOS Safari. (Pre...'
---

Par Jared Tong

Qu'est-ce que les développeurs du New York Times se trompent à propos du menu hamburger, et qu'est-ce que ceux de Disney et de Wikipedia font correctement ?

Pour autant que je sache, j'ai trouvé seulement une façon de styliser l'état ouvert du menu hamburger qui supporte iOS Safari. (Présumément, vous voulez qu'une vue mobile fonctionne sur iPhone !)

Tout est une question de la façon dont le menu hamburger est positionné.

### Le problème avec de nombreux menus hamburgers

Si votre menu hamburger n'a pas besoin de défilement... Félicitations ! La solution CSS à laquelle vous pensez maintenant fonctionnera probablement très bien : positionnez la barre latérale absolument hors et dans la vue-port lorsque l'utilisateur clique sur l'icône du menu.

Si votre menu a plus d'éléments que la vue-port ne peut en afficher à la fois, voici ce qui se passe lorsque votre menu hamburger est positionné absolument :

Si vous ne voulez pas regarder la vidéo, je vais essayer de la décrire en mots.

* Le défilement dans le menu `position: absolute` est désagréable : il ne défile pas en douceur, et lorsqu'il atteint la fin du défilement, il ne rebondit pas de cette [manière satisfaisante et brevetée en élastique](https://www.youtube.com/watch?v=FSv5x3V_KHY). Essayez les menus hamburgers sur [New York Times](https://nytimes.com), ou [Pitchfork](https://pitchfork.com).
* Si vous faites défiler excessivement dans le menu hamburger, iOS Safari fera défiler le corps à la place. Essayez la barre latérale sur [Viki](https://viki.com).
* Une alternative est d'utiliser `position:fixed` et `-webkit-overflow-scrolling: touch` sur la barre latérale. Même alors, si vous tapez au-delà du menu, comme en faisant défiler sur la partie du contenu principal exposée à côté de la barre latérale, vous perdrez la capacité de faire défiler dans le menu. Essayez le menu hamburger sur [Grab](https://grab.com).

Remarquez comment parfois iOS fait défiler le menu, parfois il fait défiler le corps derrière le menu ? Frustrant !

Et pour ce que ça vaut, vous pouvez aussi casser le défilement sur [Apple.com](https://apple.com). Une façon facile de déclencher le défilement sur le menu hamburger est d'utiliser votre téléphone horizontalement.

### La solution

En gros, la chose clé que vous devez retenir sur l'état final ouvert du menu est celle-ci : au lieu de positionner le menu absolument, ce sera le contenu principal qui sera positionné une fois la barre latérale ouverte. En d'autres termes, **au lieu de positionner le menu, positionnez tout le reste** !

Voici cela en code, accompagné de commentaires explicatifs :

```
<html><head></head><body>  <div class="sidebar">Les liens du menu hamburger vont ici</div>  <div class="main-content"><button class="hamburger-menu-icon" onClick="toggleSidebar()">?</button></div></body></html> 
```

```
/* Valeurs arbitraires de variables CSS à des fins explicatives */:root {  --sidebar-width: 100px;  --sidebar-bg-colour: blue;}.sidebar {  display: none;  position: relative;  width: var(--sidebar-width);}@media (max-width: 767px) {  html.sidebar-is-open .sidebar {    display: block;      /*       La barre latérale est simplement rendue dans la position par défaut,      telle qu'elle apparaît dans le flux du document     */  }  html.sidebar-is-open .main-content {    position: fixed;     /*      C'est le contenu principal qui est positionné.      C'est le point crucial de l'implémentation. Le reste n'est que du sucre.     Inconvénients : le corps défilera vers le haut, perdant la position de défilement de l'utilisateur    */    /* empêche le redimensionnement de sa largeur d'écran complet originale */    bottom: 0;    left: 0;    right: 0;    top: 0;    width: 100%;     overflow: hidden;  }  /* Amélioration optionnelle :      rendre le sur-défilement sur iPhone de la même couleur que la barre latérale */  html.sidebar-is-open body {    background-color: var(--sidebar-bg-colour);  }  .sidebar {    background-color: var(--sidebar-bg-colour);  }}
```

```
const documentElement = document.querySelector("html");const contentElement = document.querySelector(".main-content");const sidebarElement = document.querySelector(".sidebar");const sidebarIsOpen = () => documentElement.classList.contains("sidebar-is-open");const openSidebar = () => {  /* Comment vous déclenchez le changement vous appartient */  documentElement.classList.add("sidebar-is-open");};const closeSidebar = () => {  documentElement.classList.remove("sidebar-is-open");};const toggleSidebar = () => {  sidebarIsOpen() ? closeSidebar() : openSidebar();};
```

### Conclusion

Jusqu'à présent, j'ai trouvé deux grands acteurs qui le font correctement : [Wikipedia](https://wikipedia.org) et [Disney USA](https://disney.go.com).

Essayez leurs menus hamburgers sur iOS et voyez à quel point l'expérience de défilement est excellente !

Espérons que vous pourrez diffuser l'information et corriger les menus hamburgers à partir de maintenant.

Si vous êtes plus débutant, vous pouvez trouver une explication de [ce qu'est un menu hamburger](https://jaredtong.com/how-to-code-a-hamburger-menu/) et [comment construire un menu hamburger à partir de zéro sur mon blog](https://jaredtong.com/how-to-code-a-hamburger-menu/).