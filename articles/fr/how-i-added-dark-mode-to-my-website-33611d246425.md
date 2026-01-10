---
title: Comment j'ai ajouté le mode sombre à mon site web
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2019-02-04T15:42:31.000Z'
originalURL: https://freecodecamp.org/news/how-i-added-dark-mode-to-my-website-33611d246425
coverImage: https://cdn-media-1.freecodecamp.org/images/0*izsJBvK2z3sNZvkh.png
tags:
- name: CSS
  slug: css
- name: dark mode
  slug: dark-mode
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
seo_title: Comment j'ai ajouté le mode sombre à mon site web
seo_desc: 'I recently redesigned my website. Here are 2 pictures of how it looked,
  for reference:



  I designed this website almost 1 year ago, and did many changes along the way, just
  as we do with any website.

  Eventually I grew tired of the design: title is to...'
---

J'ai récemment redessiné [mon site web](https://flaviocopes.com). Voici 2 images de son apparence, pour référence :

![Image](https://cdn-media-1.freecodecamp.org/images/omFzYPaJhb-CmAV7a0zLCSz00Ac31sfbUeV4)

![Image](https://cdn-media-1.freecodecamp.org/images/roWIFwsXoad3bhcoXrEUXVLarbvX9UB2vbgQ)

J'ai conçu ce site web il y a presque 1 an, et j'ai apporté de nombreuses modifications en cours de route, comme nous le faisons avec n'importe quel site web.

Finalement, je me suis lassé du design : le titre est trop grand, trop d'espace perdu au lieu de montrer le contenu immédiatement, etc.

Je me suis assis hier soir et j'ai commencé à réimaginer le site web, et j'ai terminé la refonte ce matin :

![Image](https://cdn-media-1.freecodecamp.org/images/WJZ6y3YnXqUNhJ4Ceav4LAAd5jFDc63TmQNw)

![Image](https://cdn-media-1.freecodecamp.org/images/AwAm1Tjr6abfHw5kPGo-9QGoIweVIOJr4oI5)

Bien mieux ! Le contenu, la chose la plus importante, est plus mis en avant.

J'ai utilisé une police à espacement fixe (Inconsolata) car, en tant que blog de programmation, c'est une belle police, malgré la lisibilité réduite et la taille de page augmentée due à l'utilisation de la police, car je _veux_ cette police sur mon site. Je la préfère, et comme mon site fait partie intégrante de mon activité quotidienne, je voulais qu'il soit comme je le souhaite.

Il me manquait juste une chose : le **mode sombre**. Alors que j'étais en train de refondre le site, j'avais l'option du mode sombre en tête.

Comment l'ai-je fait ? Tout d'abord, j'ai ajouté l'emoji de la Lune ? dans la barre latérale, comme moyen de permettre aux gens de changer le mode de clair à sombre.

Ensuite, j'ai ajouté un extrait JavaScript qui s'exécute lorsqu'il est cliqué. Je l'ai simplement ajouté à l'événement `onclick` en ligne dans le HTML, sans aller plus loin :

```
<p>  <a href="#" onclick="localStorage.setItem('mode', (localStorage.getItem('mode') || 'dark') === 'dark' ? 'light' : 'dark'); localStorage.getItem('mode') === 'dark' ? document.querySelector('body').classList.add('dark') : document.querySelector('body').classList.remove('dark')" title="Sombre/clair"></p>
```

Voici le JavaScript qui s'exécute dans l'onclick :

```
localStorage.setItem('mode', (localStorage.getItem('mode') || 'dark') === 'dark' ? 'light' : 'dark'); localStorage.getItem('mode') === 'dark' ? document.querySelector('body').classList.add('dark') : document.querySelector('body').classList.remove('dark')
```

C'est un peu compliqué, mais en gros je vérifie si la propriété `mode` dans le [local storage](https://flaviocopes.com/web-storage-api/) est 'dark' (et par défaut à dark si elle n'est pas encore définie, en utilisant l'opérateur `||`), et je définis l'opposé de cela dans le local storage.

Ensuite, j'assigne la classe `dark` à l'élément HTML `body`, afin que nous puissions utiliser CSS pour styliser la page en mode sombre.

Un autre script s'exécute dès que le DOM est chargé, et vérifie si le mode est sombre. Si c'est le cas, il ajoute la classe `dark` à l'élément HTML `body` :

```
document.addEventListener('DOMContentLoaded', (event) => {  ((localStorage.getItem('mode') || 'dark') === 'dark') ? document.querySelector('body').classList.add('dark') : document.querySelector('body').classList.remove('dark')})
```

Maintenant, si les gens changent de mode, leur choix sera mémorisé la prochaine fois qu'ils chargeront la page.

Ensuite, j'ai ajouté beaucoup d'instructions CSS au CSS, toutes préfixées avec `body.dark`. Comme celles-ci :

```
body.dark {  background-color: rgb(30,34,39);  color: #fff;}body.dark code[class*=language-],body.dark table tbody>tr:nth-child(odd)>td,body.dark table tbody>tr:nth-child(odd)>th {  background: #282c34}
```

Maintenant, les choses devraient déjà fonctionner ! Voici mon site en mode sombre :

![Image](https://cdn-media-1.freecodecamp.org/images/qLGFEyXtuhIuhkoxWZUHeMxsO979cAzAyZwG)

![Image](https://cdn-media-1.freecodecamp.org/images/fopjlWMiRnntpt8x-k6DlWrzZKHagsSftcRT)

J'ai ajouté la classe `dark` à l'élément `body` par défaut, pour faire du mode sombre le mode par défaut :

```
<body class="dark"> ... </body>
```

Pourquoi ? Tout d'abord, je le préfère. Ensuite, j'ai fait un sondage sur Twitter et les gens l'ont préféré.

![Image](https://cdn-media-1.freecodecamp.org/images/gl9vci-v5yBlwHtnVsqkgn8EhphopCHUeTY3)

Mais aussi pour une raison technique, en fait très simple. Je ne stocke pas le choix de l'utilisateur côté serveur, donc je n'ai aucun moyen de connaître le mode jusqu'à ce que le stockage local soit disponible.

Je pourrais le faire si le site était généré côté serveur, mais c'est un site statique, donc je sers toujours la même page à tout le monde qui la demande. Même si j'avais un cookie, je n'ai pas d'endroit pour le traiter (en revanche, cela signifie que mes pages se chargent plus rapidement).

Donc, lorsque quelqu'un navigue vers une autre page sur mon site, ou charge la page pour la première fois lors d'une deuxième visite, je ne veux pas montrer une page brillante pendant que je détermine le mode. Peut-être que le visiteur code au milieu de la nuit dans une pièce sombre.

Je préfère le faire en mode clair : montrer une page sombre pendant quelques millisecondes et puis la rendre blanche à nouveau.

La spécification _Media Queries Level 5_, encore en cours de travail, contient une nouvelle fonctionnalité média `[prefers-color-scheme](https://drafts.csswg.org/mediaqueries-5/#prefers-color-scheme)`. [Safari Technology Preview](https://developer.apple.com/safari/technology-preview/) sur macOS la supporte déjà et nous pouvons l'utiliser pour savoir si l'utilisateur navigue sur la page en mode sombre ou clair :

```
@media (prefers-color-scheme: dark) {  body {    background-color: black;    color: white;  }}@media (prefers-color-scheme: light) {  body {    background-color: white;    color: black;  }}
```

Espérons que cela sera stable dans Safari bientôt, et que dans le futur Chrome et Firefox le supporteront également.

_Publié à l'origine sur [flaviocopes.com](https://flaviocopes.com/dark-mode/).