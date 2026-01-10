---
title: Que ont en commun Uber, Volkswagen et Zenefits ? Ils ont tous utilisé du code
  caché pour enfreindre la loi.
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2017-03-03T23:13:19.000Z'
originalURL: https://freecodecamp.org/news/dark-genius-how-programmers-at-uber-volkswagen-and-zenefits-helped-their-employers-break-the-law-b7a7939c6591
coverImage: https://cdn-media-1.freecodecamp.org/images/1*IhfrP901O8K2ptKVy9I2MQ.jpeg
tags:
- name: life
  slug: life
- name: politics
  slug: politics
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Que ont en commun Uber, Volkswagen et Zenefits ? Ils ont tous utilisé du
  code caché pour enfreindre la loi.
seo_desc: "“No ethically-trained software engineer would ever consent to write a DestroyBaghdad\
  \ procedure. Basic professional ethics would instead require him to write a DestroyCity\
  \ procedure, to which Baghdad could be given as a parameter.”   \n— Nathaniel Bore..."
---

> « Aucun ingénieur logiciel formé à l'éthique ne consentirait jamais à écrire une procédure DestroyBaghdad. Les principes déontologiques de base l'obligeraient plutôt à écrire une procédure DestroyCity, à laquelle Bagdad pourrait être donnée comme paramètre. »
> 
> — Nathaniel Borenstein

### Uber a utilisé un logiciel pour opérer illégalement dans des centaines de villes

Il y a deux heures, The New York Times a révélé la plus grande histoire sur Uber à ce jour. Depuis 2013, Uber utilise un outil sophistiqué pour contourner les forces de l'ordre locales à chaque tournant.

Le programme s'appelle [Greyball](https://www.nytimes.com/2017/03/03/technology/uber-greyball-program-evade-authorities.html?_r=0) et il fonctionne comme suit :

1. Dans les villes où Uber est illégal — et il y en a encore beaucoup — Greyball peut identifier les policiers en civil qui tentent de hélér des chauffeurs Uber, d'arrêter leurs chauffeurs et de saisir leurs véhicules.
2. Lorsque ces policiers ouvrent l'application Uber et tentent de hélér une course, ils voient des voitures Uber fantômes circuler dans la ville, mais ils ne parviennent jamais à obtenir une course.
3. Comme les voitures qui apparaissent dans l'application ne sont pas réelles, et que les policiers ne peuvent pas obtenir de chauffeur pour les prendre, ils ne peuvent pas arrêter qui que ce soit.

![Image](https://cdn-media-1.freecodecamp.org/images/6wXeljUybO3yQs-8XtXcosOyUDZipMQKOwvc)

Le résultat final est qu'Uber peut essentiellement ignorer le fait qu'une ville n'a pas encore approuvé le covoiturage, et commencer à y opérer quand même.

Prenez un moment pour laisser cela s'imprégner. Uber est — grâce à son logiciel supérieur — essentiellement au-dessus des lois.

La manière dont ils identifient ces passagers est en fait assez géniale. Sur la base des cartes de crédit utilisées par la police, Uber peut croiser les bases de données des commerçants avec les bases de données des fonctionnaires, et déterminer qui est probablement un policier, puis les « bannir de l'enfer » pour les empêcher d'utiliser Uber.

Les policiers ne parviennent jamais à hélér une course avec succès, mais autant qu'ils le sachent, ils sont simplement coincés au mauvais endroit au mauvais moment. C'est ainsi qu'Uber a pu perpétrer cette escroquerie pendant des années, jusqu'à ce que quelques ingénieurs d'Uber avec une conscience coupable se manifestent pour dénoncer l'affaire.

### Zenefits a utilisé un logiciel pour certifier frauduleusement des centaines d'agents d'assurance

![Image](https://cdn-media-1.freecodecamp.org/images/h3qpO9SembJ4HZuvUI4mK0AiTAPl-nTAH29q)

Zenefits est une entreprise qui fournit des logiciels aux entreprises, puis tente de leur vendre des packages d'assurance.

En 2016, il a été révélé que leur PDG, Parker Conrad, avait développé un outil qui aidait les agents de Zenefits à tricher lors du processus de certification.

Avec l'aide de leur extension de navigateur personnalisée, les agents de Zenefits ont pu sauter la majeure partie d'un cours en ligne de 52 heures, légalement requis.

Au lieu de devoir payer de nouvelles recrues pour passer une semaine et demie à travailler sur ce cours, ils pouvaient commencer à vendre des assurances beaucoup plus tôt.

Conrad a démissionné peu après avoir été découvert. Le scandale a coûté à l'entreprise la moitié de sa valorisation — 2,5 milliards de dollars — et a entraîné la perte d'emplois de centaines de personnes.

### Volkswagen a utilisé un logiciel pour vendre 10 000 000 de voitures ultra-polluantes

![Image](https://cdn-media-1.freecodecamp.org/images/IDrj1fgjHLiba0jvnvPEIrQZP6m6Vrrphx8b)

De 2008 à 2015, Volkswagen a produit plus de 10 millions de voitures « diesel propre ». De nombreux ingénieurs étaient émerveillés que les moteurs diesel puissent produire si peu d'émissions que les voitures standard sans plomb, tout en ayant une telle autonomie. Eh bien, leurs doutes ont été confirmés en 2014, lorsque des chercheurs ont découvert que ces voitures utilisaient des « dispositifs de défaite ».

Les dirigeants de Volkswagen avaient ordonné à leurs ingénieurs logiciels de trouver un moyen de tromper l'Agence de protection de l'environnement lors de leurs tests d'émissions. Ils savaient que lors de ces tests, les régulateurs utiliseraient des paramètres spécifiques. Ils ont donc écrit une logique qui — si ces paramètres étaient sélectionnés — faisait fonctionner le moteur dans un mode spécial.

Ce « dispositif de défaite » masquait le fait que les moteurs Volkswagen « diesel propre » produisaient en réalité des émissions d'oxyde d'azote (NOx) bien supérieures à celles autorisées par la loi. **Jusqu'à 40 fois la limite fédérale.**

Et cette substance cause le cancer du poumon. [Des scientifiques du MIT estiment](http://news.mit.edu/2015/volkswagen-emissions-cheat-cause-60-premature-deaths-1029) que ces émissions causeront finalement la mort prématurée de 60 personnes. Et ce n'est que pour l'Amérique.

C'est exact — le logiciel que ces développeurs ont écrit tue des innocents.

Volkswagen a finalement payé un règlement de 14,7 milliards de dollars en 2016.

Cela restera l'une des plus grandes tragédies environnementales de notre époque — tout cela causé par quelques développeurs qui suivaient simplement les ordres.

> « Un grand pouvoir implique de grandes responsabilités » — Oncle Ben

Le monde dépend de plus en plus du code que les développeurs créent. À ce titre, les développeurs deviennent rapidement certaines des personnes les plus puissantes au monde.

Coder est un superpouvoir. Avec cela, vous pouvez plier la réalité à votre volonté. Vous pouvez rendre le monde meilleur. Ou vous pouvez le détruire.

Vous pouvez peut-être tromper les régulateurs, la police, les juges. Vous pouvez peut-être tromper le grand public. Et vous pouvez peut-être continuer à le faire indéfiniment sans être attrapé.

Mais cela ne le rend pas juste.

Les développeurs ont un grand pouvoir. Et ils doivent utiliser ce pouvoir de manière responsable.

Si vous êtes un développeur, ou que vous travaillez pour en devenir un, je vous recommande fortement de lire l'article de [Bill Sourour](https://www.freecodecamp.org/news/dark-genius-how-programmers-at-uber-volkswagen-and-zenefits-helped-their-employers-break-the-law-b7a7939c6591/undefined) « [Le code dont j'ai encore honte](https://medium.freecodecamp.com/the-code-im-still-ashamed-of-e4c021dff55e). »

Et si quelqu'un vous demande de construire quelque chose qui est clairement illégal — ou carrément maléfique — allez voir la presse. Les développeurs dans ces trois cas auraient pu le faire et épargner au monde beaucoup de peines.

Rappelez-vous : [seul VOUS pouvez prévenir le code maléfique](https://twitter.com/intent/tweet?text=Remember:%20only%20YOU%20can%20prevent%20evil%20code.&url=https://medium.freecodecamp.com/dark-genius-how-programmers-at-uber-volkswagen-and-zenefits-helped-their-employers-break-the-law-b7a7939c6591).

**Je n'écris que sur la programmation et la technologie. Si vous [me suivez sur Twitter](https://twitter.com/ossia), je ne perdrai pas votre temps. ?**