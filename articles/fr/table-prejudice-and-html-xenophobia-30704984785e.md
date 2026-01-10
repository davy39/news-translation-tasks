---
title: <table> préjugés et xénophobie HTML
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-11-18T13:10:58.000Z'
originalURL: https://freecodecamp.org/news/table-prejudice-and-html-xenophobia-30704984785e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*pD4gTzlobYFeNN0JtJhcjA.jpeg
tags:
- name: Accessibility
  slug: accessibility
- name: Design
  slug: design
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: <table> préjugés et xénophobie HTML
seo_desc: 'By Anthony Ng

  I was looking over some HTML with a student the other day when we stumbled onto
  a .

  It displayed data with restaurant reservation information. The first column held
  the names for the reservation. The second column held the time of the r...'
---

Par Anthony Ng

Je regardais du HTML avec un étudiant l'autre jour lorsque nous sommes tombés sur un <table>.

Il affichait des données avec des informations de réservation de restaurant. La première colonne contenait les noms pour la réservation. La deuxième colonne contenait l'heure de la réservation.

Cela ressemblait à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/oClTJHnHRQP3-H7pVbOriwq-I5quFfFvLvsJ)
_Tableau avec des informations de réservation_

> « Oh wow, je n'arrive pas à croire que ce code utilise réellement un tableau. Qu'est-ce que c'est, les années 90 ? » — mon étudiant

À l'époque des années 90, les tableaux étaient très en vogue. Les développeurs utilisaient des tableaux partout dans leur HTML pour formater du contenu non tabulaire.

Mais le pendule est revenu en arrière. Les tableaux sont passés de mode. Et leur réputation en tant qu'élément d'interface utilisateur ne s'est jamais rétablie.

Alors mon étudiant a commencé à réfléchir à des moyens de coder ces informations de réservation de la « bonne » manière.

> « Je sais — nous allons utiliser des listes. »

> « OK. » J'ai dit. « Donc tu utiliserais deux listes ? Une pour le nom, et une pour l'heure ? »

> « Oui. Et j'utiliserai CSS pour le styliser pour qu'il ressemble à un tableau. »

Son dégoût pour les tableaux et les façons dont ils avaient été abusés dans le passé le conduisait à abuser d'un autre élément HTML à la place.

Et cela m'a fait réfléchir : d'autres développeurs se plient-ils en quatre pour éviter d'utiliser des tableaux également ?

### Pourquoi utiliser des tableaux ? À quoi servent-ils ?

Selon la documentation du [Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table), les tableaux présentent des données tabulaires.

J'aime à penser aux données tabulaires comme des données qui ont des relations en leur sein. Y avait-il une relation entre chaque réservation ? Oui, chaque heure de réservation était associée à un nom spécifique.

Il est tout à fait approprié et sémantique d'utiliser des tableaux pour représenter des données tabulaires. Les frameworks CSS comme [Bootstrap](http://getbootstrap.com/css/#tables) supportent même les tableaux stylisés. Les tableaux sont faits pour être utilisés !

Alors d'où vient toute cette haine ?

À l'époque, les tableaux étaient utilisés pour des fins de mise en forme et de disposition. Jetez un coup d'œil à cet exemple (ou voyez-le de manière interactive sur [Codepen](http://codepen.io/newyork-anthonyng/pen/Obyowm?editors=1010)) :

```
<table align="center">  <tbody>    <tr><td>Welcome to this email</td></tr>  </tbody></table><table>  <tbody>    <tr>      <td>        Lorem ipsum dolor sit amet, consectetur adipiscing elit.    Vestibulum aliquet velit at lectus sodales, sit amet consequat odio eleifend. Fusce accumsan sed eros convallis imperdiet. Donec at dignissim nibh.       </td>      <td>        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum aliquet velit at lectus sodales, sit amet consequat odio eleifend. Fusce accumsan sed eros convallis imperdiet. Donec at dignissim nibh.       </td>    </tr>  </tbody></table><table align="center">  <tr><td>Thank you for reading this email</td></tr></table>
```

Ces 3 tableaux ont créé cette disposition en 2 colonnes pour nous.

![Image](https://cdn-media-1.freecodecamp.org/images/S7LcU0XxI9rbeDxsxm0SaO-Cq2A99tVbpQBX)
_Disposition en 2 colonnes_

Avec les avancées modernes en CSS, nous n'avons plus besoin d'utiliser des tableaux comme un hack pour la mise en page. Jetez un coup d'œil à cet exemple réécrit utilisant CSS qui produit la même disposition en 2 colonnes (voir sur [Codepen](http://codepen.io/newyork-anthonyng/pen/yVYxRq?editors=1100)) :

```
// fichier html<header>  Welcome to this email</header>
```

```
<div>  <p>     Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum aliquet velit at lectus sodales, sit amet consequat odio eleifend. Fusce accumsan sed eros convallis imperdiet. Donec at dignissim nibh.  </p>  <p>    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum aliquet velit at lectus sodales, sit amet consequat odio eleifend. Fusce accumsan sed eros convallis imperdiet. Donec at dignissim nibh.   </p></div>
```

```
<footer> Thank you for reading this email</footer>
```

```
// fichier cssheader,footer {  text-align: center;}
```

```
div {  display: flex;}
```

### Les dispositions en tableau ne disparaîtront pas

Votre estomac pourrait se tordre en regardant ce code utilisant des tableaux pour la disposition. Mais cette technique ne disparaîtra pas de sitôt.

De nombreux développeurs trouvent les tests multi-navigateurs difficiles, mais considérez combien de clients de messagerie différents existent.

Les clients de messagerie manquent de support fort et cohérent pour certains styles CSS. Les tableaux fournissent un moyen fiable d'obtenir une disposition cohérente sur plusieurs clients de messagerie et appareils.

### Apprenez votre HTML

Mon conseil est de vous familiariser avec les outils qui sont à votre disposition. Plus important encore, utilisez l'outil correct pour le travail. Bien sûr, vous pourriez utiliser un marteau pour enfoncer une vis dans un mur. Mais un tournevis ne fonctionnerait-il pas mieux ?

Beaucoup d'entre nous, développeurs, investirons volontiers du temps pour apprendre des fonctionnalités avancées de JavaScript, des optimisations d'algorithmes et de nouveaux frameworks. Mais lorsqu'il s'agit d'éléments HTML, la plupart d'entre nous restons avec ce qui est déjà confortable.

Avez-vous déjà envisagé d'apprendre sur les éléments HTML au-delà des vieux classiques : <div>, <span>, <h1>, et <p> ?

Par exemple, il y a l'élément <dl>, qui pourrait être utile lors de l'écriture d'un glossaire.

Ensuite, il y a l'élément <time>. Il permettra aux navigateurs de planifier des événements dans le calendrier de votre utilisateur.

Étiez-vous sur le point d'utiliser l'élément <b> pour faire paraître quelque chose important en le mettant en gras ? Envisagez d'utiliser l'élément <strong> à la place. Les lecteurs d'écran ne communiquent pas le style aux utilisateurs. Mais ils communiqueraient la signification sémantique de l'élément <strong>.

Importes-vous une bibliothèque pour obtenir un sélecteur de couleur ou un calendrier à l'écran ? Envisagez d'utiliser <input type="color" /> ou <input type="date"> pour utiliser ce que le navigateur vous donne.

Prenez un moment pour vous familiariser avec certains des [éléments HTML](https://developer.mozilla.org/en-US/docs/Web/HTML/Element) qui sont à votre disposition.

Et la prochaine fois que vous travaillerez avec HTML, demandez-vous si vous utilisez le bon outil.