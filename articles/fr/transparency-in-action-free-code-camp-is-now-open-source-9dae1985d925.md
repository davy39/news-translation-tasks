---
title: 'Transparence en action : Free Code Camp est maintenant Open Source'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2014-12-30T07:08:29.000Z'
originalURL: https://freecodecamp.org/news/transparency-in-action-free-code-camp-is-now-open-source-9dae1985d925
coverImage: https://cdn-media-1.freecodecamp.org/images/0*hUUtRVv9N6KVf8-F.jpg
tags: []
seo_title: 'Transparence en action : Free Code Camp est maintenant Open Source'
seo_desc: 'By freeCodeCamp

  We’re thrilled to announce that Free Code Camp is now fully open-source. Now you
  can fork our code base and use it to set up an educational community of your own.
  If you notice a bug or think up a way of improving Free Code Camp, you ...'
---

Par freeCodeCamp

Nous sommes ravis d'annoncer que Free Code Camp est maintenant [entièrement open-source](https://github.com/freecodecamp/freecodecamp). Vous pouvez maintenant forker notre base de code et l'utiliser pour mettre en place une communauté éducative à vous. Si vous remarquez un bug ou pensez à une façon d'améliorer Free Code Camp, vous pouvez maintenant agir directement en soumettant une pull request.

### Notre Code

J'ai initialement construit Free Code Camp en Ruby on Rails, car j'étais à l'aise avec. Mais il était clair depuis un certain temps que JavaScript était l'avenir. De nouveaux outils comme Node.js et Express.js ont rendu possible le passage à une pile entièrement JavaScript, et c'est précisément ce que beaucoup d'écoles et d'entreprises font. Une grande partie de Free Code Camp consiste à éliminer le bruit et à aider les personnes occupées à se concentrer sur l'apprentissage d'un ensemble d'outils opinionné. Comme nous apprenions le Full Stack JavaScript, une base de code non-JavaScript envoyait le mauvais signal. J'ai donc abandonné l'application Rails, appris assez de Node.js asynchrone pour être "dangerous", et commencé à construire.

![Image](https://cdn-media-1.freecodecamp.org/images/0*hUUtRVv9N6KVf8-F.jpg)

_Le bureau dans le placard où j'ai construit la version 0.1.0 de Free Code Camp._

J'ai regardé Meteor.js et Mean.js (c'était juste avant le fork Mean.io), et j'ai même envisagé d'utiliser simplement Angular.js avec un backend Google App Engine. Mais finalement, j'ai décidé d'opter pour l'[application Hackathon Starter](https://github.com/sahat/hackathon-starter). Avec sa suite d'authentification et ses intégrations API, c'est pratiquement un framework en soi. J'ai lancé Free Code Camp quelques jours plus tard, avec rien de plus que cinq défis de codage et une salle Hipchat. Lentement, les gens ont commencé à venir. Miracles, beaucoup d'entre eux sont restés !

![Image](https://cdn-media-1.freecodecamp.org/images/0*ysHoX0ttspHq8bPU.png)

_À quoi ressemblait Free Code Camp lorsque nous l'avons lancé il y a environ 10 semaines._

Free Code Camp était ma première application Node.js. J'ai montré le code à un développeur JavaScript expérimenté qui n'arrêtait pas de crier "Qu'est-ce que tu as pensé ici ?" en parcourant la base de code. Malgré son aspect hacky, il a reconnu que, puisque cela servait des milliers de vues de page par jour sans incident, ce n'était pas une totale honte et que je devrais aller de l'avant et l'ouvrir en source. Nous avons donc installé Helmet.js pour une sécurité supplémentaire, déplacé les clés API vers un fichier .env, et les avons purgées de l'historique Git. Et voilà, le même code exact que Free Code Camp utilise en production est maintenant librement disponible ici.

### Notre Infrastructure

Nous utilisions un seul dyno Heroku (gratuit), mais comme nous dépassons occasionnellement 20 sessions concurrentes, nous l'avons monté à deux, pour 35 $ par mois. Nous servons les assets via S3 et avons une petite instance AWS pour notre forum alimenté par Discourse. Nous payons un total de 240 $ par an pour un compte Vimeo Pro et un compte Screen Hero, et 60 $ pour un seul compte d'équipe Google Apps for Business. Cela porte le coût total de toute notre infrastructure à moins de 2 000 $ par an.

### Nos Conseillers de Camp Volontaires

Nous sommes une communauté de personnes occupées apprenant à coder. Nous nous appelons "Code Campers". Certains d'entre nous, Code Campers, sont même plus occupés que les autres, car nous consacrons notre temps à améliorer activement Free Code Camp. Notre équipe de "Conseillers de Camp" traîne dans notre salon de discussion et notre forum. Nous faisons de notre mieux pour accueillir les nouveaux venus et répondre à diverses questions de codage. Notre objectif unique est de maximiser le nombre de personnes occupées comme nous qui sont capables de travailler à travers nos défis, de construire un portfolio de projets pour des organismes sans but lucratif, puis d'obtenir un emploi en codage.

![Image](https://cdn-media-1.freecodecamp.org/images/0*sbqy-3D41NFUGDUv.png)

_Quelques-uns de nos patients et enthousiastes Conseillers de Camp._

Personne ne reçoit de paiement. Si nous acceptons éventuellement des fonds ou gagnons de l'argent via un tableau d'emplois, nous trouverons un moyen équitable et transparent de distribuer des actions à nos bénévoles ou de commencer à les payer. La plupart de nos communications se font via notre salon de discussion et nos fréquentes sessions de programmation en binôme. Nous sommes géographiquement dispersés, mais nous nous rencontrons en personne lorsque cela est possible. Nos Conseillers de Camp proposent de nouvelles fonctionnalités et du contenu, discutent des priorités et des détails, puis se mettent en binôme et commencent à construire. Par exemple, cet article de blog a été édité et amélioré par plusieurs Conseillers de Camp.

### Nos Métriques

En moins de 3 mois, nous avons atteint près de 5 000 Code Campers. Mais ce dont nous sommes vraiment fiers, ce n'est pas la quantité de nos Code Campers, mais la qualité de leur éthique de travail. Un groupe de personnes avec du travail, de l'école, des enfants — et même des [petits-enfants](http://blog.freecodecamp.com/2014/11/I-am-a-Grandma-and-my-coding-career-is-just-getting-started.html) — investissent leur précieux temps pour apprendre à coder. Nous avons complètement repensé notre programme il y a trois semaines, et depuis, des centaines de personnes ont travaillé sur nos défis d'une heure. Nous avons rendu toutes ces métriques publiques [ici](http://www.freecodecamp.com/stats). Pour information, si vous êtes intéressé par l'analyse de nos données (anonymisées), ou par nous aider à mieux les visualiser, nous serions ravis de faciliter cela.

### Notre Avenir

Ne vous attendez pas à des initiatives furtives ou à des révélations grandioses de notre part. Nous sommes plus intéressés par l'évolution en plein air, comme l'a fait l'internet, que par une entrée explosive, comme l'a fait la bombe atomique. Nous croyons en la maxime Open Source selon laquelle "Avec assez d'yeux, tous les bugs sont superficiels", et nous accueillons toute idée que vous pourriez avoir pour rendre Free Code Camp un meilleur et plus efficace endroit pour les personnes occupées d'apprendre à coder.

Pour conclure, j'aimerais comparer la philosophie de Free Code Camp avec celle d'Ubuntu. Pas la distribution Linux Ubuntu qui alimente une grande partie de l'internet, mais son homonyme, la philosophie Ubuntu d'Afrique australe. Ubuntu est un mot zoulou qui se traduit approximativement par "Je suis ce que je suis grâce à qui nous sommes tous."

![Image](https://cdn-media-1.freecodecamp.org/images/0*mIa-Fp-HD_MuaV0s.jpg)

_Leymah Gbowee, l'activiste pour la paix libérienne et lauréate du prix Nobel de la paix responsable de la définition en anglais la plus largement acceptée d'Ubuntu._

Free Code Camp est ce qu'il est grâce à qui sont nos Code Campers. Des personnes occupées s'aidant mutuellement à apprendre à coder. Et c'est ce que nous continuerons à être à l'avenir.

_Publié à l'origine sur [blog.freecodecamp.com](http://blog.freecodecamp.com/2014/12/transparency-in-action-free-code-camp.html) le 29 décembre 2014._