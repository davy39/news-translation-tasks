---
title: Ce que j'ai appris en lisant defer-render-hoc et pourquoi c'est utile.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-24T03:24:40.000Z'
originalURL: https://freecodecamp.org/news/what-i-learned-from-reading-defer-render-hoc-8c2e9dc2b07a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*lrJvFE4XDFi5TU6g9Qzumg.jpeg
tags:
- name: Computer Science
  slug: computer-science
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: user experience
  slug: user-experience
seo_title: Ce que j'ai appris en lisant defer-render-hoc et pourquoi c'est utile.
seo_desc: 'By Anthony Ng


  This is another article for my Deliberate Practice. Why am I doing this? Read this
  article to learn more.


  I was reading through this article about how Twitter Lite (a React PWA) removed
  performance bottlenecks.


  _Image from [Twitter L...'
---

Par Anthony Ng

> Ceci est un autre article pour ma Pratique Délibérée. Pourquoi je fais cela ? [Lisez cet article pour en savoir plus](https://medium.freecodecamp.org/deliberate-practice-becoming-an-open-sourcerer-27a4f7640940).

Je lisais [cet article](https://medium.com/@paularmstrong/twitter-lite-and-high-performance-react-progressive-web-apps-at-scale-d28a00e780a3) sur la façon dont Twitter Lite (une PWA React) a éliminé les goulots d'étranglement de performance.

![Image](https://cdn-media-1.freecodecamp.org/images/1*P0WB3eCNtNZjOYzQ7Gd6Lw.gif)
_Image de [l'article Twitter Lite](https://medium.com/@paularmstrong/twitter-lite-and-high-performance-react-progressive-web-apps-at-scale-d28a00e780a3" rel="noopener" target="_blank" title=")_

Lorsque l'utilisateur appuie sur le bouton `Accueil`, il y a un délai jusqu'à ce que les tweets s'affichent. Ce délai était causé par un grand nombre de composants montant et démontant. `defer-render-hoc` est un projet Open Source qui implémente la solution donnée dans l'article.

### Examinons le code

`defer-render-hoc` est un Composant d'Ordre Supérieur (HOC). Pour en savoir plus, lisez [la documentation ici](https://reactjs.org/docs/higher-order-components.html).

Nous utilisons `defer-render-hoc` en enveloppant votre Composant Coûteux avec celui-ci.

`defer-render-hoc` rend `null` lors du rendu initial.

Alors, quand est-ce que `defer-render-hoc` rendra votre Composant Coûteux ? Il utilise `requestAnimationFrame` pour attendre deux frames. Après que deux frames se soient écoulées, il rendra votre Composant Coûteux.

`requestAnimationFrame` est généralement utilisé pour créer des animations fluides ([lisez-en plus dans cet article](https://developers.google.com/web/fundamentals/performance/rendering/optimize-javascript-execution)).

Ici, nous utilisons `requestAnimationFrame` pour permettre à d'autres composants de se mettre à jour et de redonner le contrôle à l'utilisateur. Après les deux frames, notre Composant Coûteux prend le relais.

### Démo

Consultez ce [CodeSandbox pour une démo](https://codesandbox.io/s/pjxkjjxv8m) de `defer-render-hoc`.

Cliquez du bouton `Page Bon Marché` au bouton `Page Coûteuse`. Remarquez comment le bouton reste bleu alors que l'UI se fige.

![Image](https://cdn-media-1.freecodecamp.org/images/1*n07TLpSGmwdjHKXNQTvBHQ.png)
_(sans defer-render-hoc) 624,02 ms pour l'événement de clic_

Notre événement de clic prend 620 ms. L'événement de clic ne se termine pas tant que notre Composant Coûteux n'est pas monté. À cause de cela, l'écran est figé pour l'utilisateur.

Maintenant, cliquez du bouton `Page Bon Marché` au bouton `Page Coûteuse Différée`. Remarquez comment le bouton ne reste pas bleu et l'UI ne se fige pas.

![Image](https://cdn-media-1.freecodecamp.org/images/1*p12mxsrFus6uqzKBFofIxQ.png)
_(avec defer-render-hoc) 16,71 ms pour l'événement de clic_

Notre événement de clic prend 16 ms. L'événement de clic n'attend pas que notre Composant Coûteux soit monté ; le travail est différé. L'écran ne se fige pas.

### Comment cela aide-t-il ?

La même quantité de travail est toujours effectuée. Le Composant Coûteux est toujours monté ; il est simplement monté plus tard. L'expérience elle-même n'est pas globalement plus rapide. Elle pourrait même être plus lente avec le surcoût de `defer-render-hoc`. Mais parfois, une expérience perçue comme plus rapide est plus importante qu'une expérience réellement plus rapide. Voir les liens ci-dessous pour plus d'informations sur la performance perçue.

* [https://en.wikipedia.org/wiki/Perceived_performance](https://en.wikipedia.org/wiki/Perceived_performance)
* [https://medium.com/@lukejones/a-designers-guide-to-the-perception-of-performance-fedb4bd102b](https://medium.com/@lukejones/a-designers-guide-to-the-perception-of-performance-fedb4bd102b)

Selon votre projet, `defer-render-hoc` pourrait être fait pour vous.