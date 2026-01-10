---
title: "Tout est une question de \x1C\x13ilités\x1D"
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-05-31T23:38:13.000Z'
originalURL: https://freecodecamp.org/news/its-all-about-the-ilities-875682184dc8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wOLB8os9g-Qn2_TuSyp6Zw.jpeg
tags:
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: "Tout est une question de \x1C\x13ilités\x1D"
seo_desc: 'By George Stepanek

  We were “feature complete.”

  Four weeks into a 10-week Free Code Camp project to build an environmental pledge
  web application, we had gotten all of the use cases working correctly.

  Which meant that we were finished, right?

  Not even...'
---

Par George Stepanek

Nous étions feature complete.

Quatre semaines après le début d'un projet de 10 semaines avec [Free Code Camp](https://www.freecodecamp.com/) pour construire une [application web de promesses environnementales](http://fcc-1to1-pledge-app.herokuapp.com/), nous avions réussi à faire fonctionner correctement tous les cas d'utilisation.

Ce qui signifiait que nous avions terminé, n'est-ce pas ?

Pas du tout !

Il nous a fallu quatre semaines supplémentaires pour amener l'application à un niveau de qualité professionnel. Il ne s'agissait pas seulement de trouver et de corriger quelques bugs restants. La plupart du travail que nous avions encore à faire concernait les ilités : les [exigences non fonctionnelles](https://en.wikipedia.org/wiki/Non-functional_requirement), telles que l'utilisabilité et la compatibilité.

L'application fonctionnait correctement. Mais maintenant, nous devions la faire fonctionner _mieux_.

> Deux secondes est le seuil d'acceptabilité pour un site web de commerce électronique. Chez Google, nous visons moins d'une demi-seconde. — Maile Ohye

#### Performance

L'application avait besoin d'un aspect et d'une convivialité multi-pages, afin que les gens puissent partager les URL des promesses individuelles ou de leurs propres réalisations de promesses, mais nous ne pouvions pas atteindre les temps de réponse inférieurs à la seconde que nous voulions en utilisant une conception multi-pages. Il fallait simplement trop de temps pour télécharger et rendre les pages.

Notre solution a été de la refactoriser en une application monopage basée sur React qui interceptait les événements de clic des hyperliens pour contrôler quelle page afficher :

```
var self = this;$('a').click(function (event) {    var href = $(this).attr("href");    self.setState({ url: href });    window.history.pushState('', '', href);    event.preventDefault();});
```

Cela signifie que l'application est entièrement chargée une seule fois (ce qui peut prendre quelques secondes sur une connexion lente) et que chaque clic dans le site est ensuite beaucoup, beaucoup plus rapide.

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)
_Résultats du chargement de la page depuis [GTmetrix](https://gtmetrix.com/" rel="noopener" target="_blank" title=")_

Nous avons également optimisé agressivement les images avec Adobe Photoshop pour réduire les temps de téléchargement, et nous avons veillé à ce que les pages soient lisibles même pendant que leurs images sont encore en cours de téléchargement.

#### Compatibilité

Lorsque vous mettez une application web sur l'internet public, vous ne savez pas qui va y accéder, quel navigateur ils vont utiliser, ou à quel point leur version de navigateur sera ancienne. Elle doit fonctionner pour tout le monde.

Un avantage de notre conception d'application monopage était qu'il était facile de la faire s'éteindre pour les anciennes versions de navigateurs qui ne supportent pas [les API dont nous avions besoin](http://diveintohtml5.info/history.html), et de revenir à l'utilisation des hyperliens tels quels. L'utilisation de l'application de cette manière est plus lente, bien sûr, mais elle fonctionne toujours très bien.

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)
_[Disponibilité du navigateur pour l'API History](http://caniuse.com/#search=pushstate" rel="noopener" target="_blank" title=")_

De nos jours, la plupart des navigateurs modernes sont raisonnablement compatibles les uns avec les autres, mais vous devriez tout de même tester aussi largement que possible. Nous avons constaté que nous devions mettre en place des règles spéciales pour les anciennes versions d'Internet Explorer (ce qui n'était pas inattendu) et d'iOS (ce qui l'était).

> Ne me faites pas réfléchir —Steve Krug

#### Utilisabilité

Nous pensions que notre application — avec cinq catégories contenant chacune une douzaine de promesses — était assez simple.

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)
_Fil d'Ariane sur les pages [promesse](http://fcc-1to1-pledge-app.herokuapp.com/" rel="noopener" target="_blank" title="">accueil</a>, <a href="http://fcc-1to1-pledge-app.herokuapp.com/category/transportation" rel="noopener" target="_blank" title="">catégorie</a> et <a href="http://fcc-1to1-pledge-app.herokuapp.com/pledge/carpool" rel="noopener" target="_blank" title=")_

Mais lorsque nous avons demandé à nos amis et à notre famille de faire des tests utilisateurs, certains d'entre eux ont dit qu'ils étaient confus quant à leur position dans l'application, et ne comprenaient pas vraiment comment aller là où ils voulaient.

Il fallait que ce soit plus intuitif.

Nous avons donc ajouté des icônes de [fil d'Ariane](https://en.wikipedia.org/wiki/Breadcrumb_(navigation)) dans l'en-tête pour aider les gens à avoir une idée immédiate de leur position dans la hiérarchie des pages, avec des hyperliens pour les aider à remonter.

Nous avons également ajouté des flèches _promesse suivante_ et _promesse précédente_ afin que les gens puissent facilement cliquer d'une promesse à l'autre sans avoir à revenir à la page de catégorie à chaque fois.

#### Design

Le mouvement 1to1 se décrit comme une organisation de marque dont l'objectif est de rendre l'écologisme plus attrayant. Leur [site web principal](http://1to1movement.org/) a un design moderne et stylé, et nous voulions perpétuer cela dans notre application web.

![Image](https://cdn-media-1.freecodecamp.org/images/xaAXnTRRi2LlCl8dzWJjtQFPhrwTD0Y3o4BW)
_La page [Éducation](http://1to1movement.org/we-are-educators/" rel="noopener" target="_blank" title=") sur le site web du mouvement 1to1_

Nous avons donc copié certains des principaux aspects du design — images en pleine largeur, miniatures à faible contraste, polices spécifiques, couleur de surbrillance turquoise — puis nous avons demandé à un ami compétent de nous faire une revue de design pour nous assurer que nous les utilisions correctement et de manière cohérente.

Nous voulions que tout le monde reparte avec une bonne impression, et une partie de cela consistait à vérifier que le site web a une bonne apparence sur toutes les tailles d'écran, des téléphones mobiles aux écrans haute résolution. L'utilisation d'un framework UI réactif comme [Bootstrap](http://getbootstrap.com/) nous a permis d'y parvenir en grande partie, mais nous devions encore vérifier les bugs à différentes largeurs de viewport. Par exemple, nous avons dû ajouter **{ white-space: nowrap; }** à la section des fils d'Ariane pour l'empêcher de se casser lorsque la ligne d'en-tête est enveloppée.

> N'importe quel idiot peut écrire du code qu'un ordinateur peut comprendre. Les bons programmeurs écrivent du code que les humains peuvent comprendre. —Martin Fowler

#### Maintenabilité

Bon nombre de ces corrections et améliorations concernaient des navigateurs ou des versions inhabituels, ou des cas d'utilisation rarement rencontrés. Nous avons donc ajouté des commentaires significatifs pour expliquer _pourquoi_ chaque composant était codé de la manière dont il l'était. Nous voulions que les futurs développeurs comprennent comment tout fonctionnait, et faciliter leur tâche pour éviter de casser les fonctionnalités existantes lorsqu'ils ajoutent de nouvelles fonctionnalités.

![Image](https://cdn-media-1.freecodecamp.org/images/7cbb386qgYtJsGJX2Tjku0F2o-0-OKLMYk6S)

Un bon ensemble de tests unitaires aiderait également les futurs développeurs, car ils permettent de vérifier rapidement et facilement la présence de code cassé. Nous avons utilisé [mocha](https://www.npmjs.com/package/mocha) et [supertest](https://www.npmjs.com/package/supertest) pour créer des tests automatisés pour la logique métier back-end dans nos appels API.

#### Qu'est-ce qui suit ?

Avec tout cela fait, pouvions-nous maintenant partir en bonne conscience ? Pas tout à fait !

Même si nous avions rendu l'application prête pour la production, nous devions encore la déployer en production et la remettre correctement au client.

Mais c'est une histoire pour une autre fois...

Merci d'avoir lu. J'espère que cet article vous a aidé à mieux comprendre toutes les ilités impliquées dans la préparation d'une application pour la production.