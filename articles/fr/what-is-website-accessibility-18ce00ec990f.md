---
title: Qu'est-ce que l'accessibilité des sites web ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-13T14:27:48.000Z'
originalURL: https://freecodecamp.org/news/what-is-website-accessibility-18ce00ec990f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Kg9Y-FRAW_9UK6X0sJE-pg.jpeg
tags:
- name: Design
  slug: design
- name: Front-end Development
  slug: front-end-development
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Qu'est-ce que l'accessibilité des sites web ?
seo_desc: 'By Ben Robertson

  Web accessibility is getting a lot of attention these days, but it can be intimidating.
  Here’s a simple introduction to web accessibility: what it is, why it’s important,
  and the benefits that come along with accessibility.

  At the mo...'
---

Par Ben Robertson

L'accessibilité des sites web attire beaucoup d'attention ces jours-ci, mais cela peut être intimidant. Voici une introduction simple à l'accessibilité des sites web : ce que c'est, pourquoi c'est important, et les avantages qui accompagnent l'accessibilité.

Au niveau le plus basique, l'accessibilité des sites web signifie construire des sites web qui sont utilisables par le plus grand nombre de personnes possible.

Aux États-Unis seulement, 57 millions de personnes déclarent avoir un handicap. Cela représente une personne sur cinq — l'équivalent des populations entières de New York et de Californie combinées. Et parmi ces personnes, environ 30 millions déclarent avoir un handicap sévère.

Comment les développeurs web peuvent-ils s'assurer que leurs sites sont accessibles au plus grand nombre d'utilisateurs possible ?

#### Qu'est-ce qui rend un site inaccessible ?

Il existe de nombreuses façons dont les utilisateurs peuvent trouver un site web inaccessible.

Certaines personnes peuvent ne pas être en mesure d'utiliser une souris. Elles peuvent avoir besoin de pouvoir faire défiler, cliquer, naviguer et [interagir avec toutes les parties d'un site web en utilisant uniquement un clavier](https://benrobertson.io/accessibility/javascript-accessibility#2-plan-for-common-keyboard-interactions) ou un autre appareil.

D'autres peuvent avoir une forme de daltonisme, ce qui peut rendre difficile la distinction des liens et des boutons du reste du contenu textuel.

La dyslexie peut rendre difficile pour certaines personnes la compréhension du contenu d'un site.

Pour les personnes ayant des déficiences visuelles sévères, il est nécessaire que tout le contenu et l'interactivité d'une page soient [compréhensibles par un lecteur d'écran](https://benrobertson.io/accessibility/understanding-layout-for-screen-readers). Il s'agit d'un programme qui lit le contenu d'une page web à l'utilisateur et lui permet d'interagir avec la page.

Il existe même des machines qui fournissent une sortie en braille à partir de pages web.

#### L'accessibilité est une norme du Web

J'ai à peine effleuré la surface des défis d'accessibilité auxquels les gens peuvent être confrontés sur le web. Il est impossible pour une équipe web moyenne de suivre toutes ces différentes situations qui peuvent empêcher les gens d'utiliser et de profiter des sites web.

C'est pourquoi le [World Wide Web Consortium](https://www.w3.org/) a rédigé pour la première fois des [normes pour le développement de sites web accessibles](https://www.w3.org/TR/WCAG10/) dès 1999.

Cet ensemble de normes facilite la tâche des équipes de développement pour s'assurer que leur travail est accessible à tous. Ces normes sont ce que vous avez peut-être entendu référencées sous le nom de WCAG (parfois prononcé wee-kag). Cela signifie [Web Content Accessibility Guidelines](https://www.w3.org/TR/WCAG20/).

Ces directives fournissent un aperçu détaillé des modèles courants et des domaines qui peuvent causer des problèmes d'utilisabilité dans différentes situations. À un niveau plus élevé, elles décrivent les quatre grandes lignes directrices de l'accessibilité des sites web :

* **Perceptible :** tout le monde peut-il percevoir le contenu de la page ?
* **Utilisable :** tout le monde peut-il interagir avec la page ?
* **Compréhensible :** tout le monde peut-il comprendre le contenu de la page ?
* **Robuste :** le contenu peut-il être interprété par une grande variété de programmes et d'appareils, y compris les lecteurs d'écran ?

Bien que ces directives existent depuis longtemps, les parties prenantes à tous les niveaux des projets web ne sont souvent pas conscientes de leur existence. Ou peut-être ne pensent-ils pas que c'est une préoccupation pour leur organisation.

Examinons certains des avantages de l'accessibilité des sites web pour voir pourquoi ces directives sont importantes.

### Quels sont les avantages de l'accessibilité des sites web ?

#### Inclusivité

Le premier avantage de l'accessibilité est l'inclusivité. Lorsque vous abordez l'accessibilité dans une perspective de rendre un site web convivial pour le plus grand nombre de personnes possible — eh bien, c'est la définition de l'inclusivité, n'est-ce pas ?

La grande chose à propos du suivi des directives d'accessibilité des sites web est que, en les suivant, vous offrez une meilleure expérience web à tous les utilisateurs.

Prenons l'exemple des [directives sur le niveau de lecture](https://www.w3.org/TR/UNDERSTANDING-WCAG20/meaning-supplements.html). Bien que ces directives soient destinées à s'assurer que les personnes ayant des handicaps de lecture peuvent comprendre un site web, une fois mises en œuvre, elles aident également les personnes ayant un faible niveau de littératie ou qui ne sont pas fluides dans notre langue à comprendre notre site web plus facilement.

#### Avantages pour le référencement

Un deuxième avantage de la priorité donnée à l'accessibilité est l'amélioration du référencement naturel (SEO).

Les mêmes pratiques qui garantissent que le contenu est compréhensible pour les lecteurs d'écran bénéficient également aux robots qui indexent les sites web pour Google et d'autres moteurs de recherche.

De nombreuses directives d'accessibilité se concentrent sur la fourniture d'alternatives textuelles au contenu disponible en vidéo ou en audio. Cela permet à ce contenu d'être visible à la fois pour les lecteurs d'écran et les moteurs de recherche.

Les directives encouragent également l'utilisation d'une organisation de page appropriée pour aider les utilisateurs à mieux comprendre la mise en page et le contenu d'une page. Cela aide également les moteurs de recherche à mieux comprendre le contenu d'une page.

Rendre votre contenu web plus facile à comprendre pour les gens le rendra également plus facile à comprendre pour les robots de Google.

#### Avantages d'utilisabilité

Il existe également des avantages d'utilisabilité à prioriser l'accessibilité.

Nous avons tous, à un moment donné, rencontré un site web qui était inutilisable. Parfois, le texte n'a pas assez de contraste avec son arrière-plan, ou les boutons sont trop petits pour être facilement utilisés sur nos smartphones.

Se concentrer sur l'accessibilité des sites web peut aider à éliminer les problèmes de base comme ceux-ci. En suivant les directives, nous pouvons nous assurer que notre site est aussi utilisable sur les appareils mobiles que sur les grands écrans, pour tout le monde.

De plus, en prêtant attention au principe de "robustesse" de l'accessibilité et en s'assurant que le contenu peut être interprété par une grande variété de programmes et d'appareils, nous aiderons les personnes qui peuvent utiliser des technologies plus anciennes ou avoir une faible bande passante à avoir accès à un site web.

Les organisations qui priorisent l'accessibilité développeront non seulement de la bonne volonté avec leurs utilisateurs, mais s'assureront également de pouvoir servir près de 100 % du marché. Et elles se protégeront contre la perte de la capacité à servir leurs clients à mesure qu'ils vieillissent.

### Quelles sont les exigences légales pour l'accessibilité des sites web ?

Outre les avantages que peuvent apporter le suivi des directives d'accessibilité, il peut également y avoir des exigences légales à considérer.

Les problèmes d'accessibilité ont été mis en avant en raison d'une série de poursuites judiciaires intentées en vertu du [Titre III](https://www.ada.gov/regs2010/2010ADAStandards/2010ADAstandards.htm) de l'Americans with Disabilities Act (ADA). Cela exige que les espaces publics et les installations commerciales soient conçus et construits de manière à ce que les utilisateurs handicapés puissent jouir d'un accès égal à ces installations.

Bien que la loi ait été initialement rédigée en pensant aux espaces physiques, la prévalence des activités basées sur le web, y compris les achats et l'éducation, a également soumis les expériences web inaccessibles à un examen minutieux.

Notamment, un [juge fédéral a statué en juin 2017](https://www.forbes.com/sites/legalnewsline/2017/06/13/first-of-its-kind-trial-goes-plaintiffs-way-winn-dixie-must-update-website-for-the-blind/) que les propriétés web de Winn-Dixie étaient si intégrées à leurs emplacements physiques qu'elles étaient soumises au Titre III de l'ADA. Le juge a statué en faveur d'un homme aveugle qui a intenté le procès, exigeant que Winn-Dixie mette à jour leur site pour répondre aux normes d'accessibilité du contenu web et effectue des audits annuels pour s'assurer qu'ils continuent de répondre à ces normes. ([L'ordre complet de 13 pages du tribunal est disponible ici](http://www.adatitleiii.com/wp-content/uploads/sites/121/2017/06/16-cv-23020-63-Verdict-Order_WinnDixie.pdf)).

De plus, le nombre de poursuites judiciaires liées à l'accessibilité des sites web a explosé. Le cabinet d'avocats Seyfarth Shaw [rapporte](https://www.adatitleiii.com/2017/08/website-accessibility-lawsuit-filings-still-going-strong/) qu'il y a eu environ 57 poursuites fédérales liées à l'accessibilité des sites web intentées en 2015, 262 en 2016, et 432 entre janvier et août 2017 seulement. Au-delà de cela, le département de l'Éducation des États-Unis a récemment ouvert [350 enquêtes sur l'accessibilité des sites web](http://legalnewsline.com/stories/510738182-department-of-education-increases-investigations-into-website-compliance-with-ada).

### Conclusion

La bonne nouvelle est qu'il existe des directives claires pour les développeurs, les chefs de produit, les designers et les éditeurs de contenu à suivre pour développer et maintenir des sites web accessibles.

Avec une bonne planification, une bonne exécution et une bonne responsabilité, un site web accessible est un objectif atteignable pour chaque organisation. En étant proactifs, les organisations qui adoptent une approche axée sur l'accessibilité seront en mesure de générer de la bonne volonté avec leurs clients, de rester dans le cadre des exigences légales pertinentes et de servir un marché plus large.

_Voulez-vous plonger dans les détails de la construction de sites web accessibles ? Rejoignez mon cours gratuit par e-mail :_ 💡 [_Erreurs courantes d'accessibilité et comment les éviter._](https://benrobertson.io/courses/common-accessibility-mistakes/) _30 jours, 10 leçons, 100 % de plaisir !_ 💡 [_Inscrivez-vous ici !_](https://benrobertson.io/courses/common-accessibility-mistakes/)

_Publié à l'origine sur [benrobertson.io](https://benrobertson.io/accessibility/what-is-website-accessibility)._