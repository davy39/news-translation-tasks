---
title: Aventures avec NodeJS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-01-22T09:57:53.000Z'
originalURL: https://freecodecamp.org/news/adventures-in-nodejs-d3d1f85a9d3e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*S9lOOozk-9WPFLnCSsF_ww.png
tags:
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: learning to code
  slug: learning-to-code
- name: Node.js
  slug: nodejs
- name: technology
  slug: technology
seo_title: Aventures avec NodeJS
seo_desc: 'By Elliott McNary

  I built an app a couple of weeks ago after going through FreeCodeCamp’s Front-End
  curriculum and wanted to write an update as I head into NodeJS-land. I was finally
  able to obtain my Front-End certificate, which I am very proud of, ...'
---

Par Elliott McNary

J'ai construit une application il y a quelques semaines après avoir suivi le programme Front-End de FreeCodeCamp et je voulais écrire une mise à jour alors que je me lance dans l'univers de NodeJS. J'ai enfin pu obtenir mon certificat Front-End, dont je suis très fier, mais l'excitation a rapidement disparu une fois que je me suis plongé dans le côté backend des choses.

Apprendre NodeJS a été incroyablement difficile jusqu'à présent. Il n'y a aucun intérêt à essayer de le saupoudrer de poudre de fée. Le passage du front-end, où j'utilisais principalement JQuery et quelques techniques JS de base, au backend avec du bon vieux JavaScript et des centaines de callbacks, m'a montré que je n'avais aucune idée de ce que je faisais.

![Image](https://cdn-media-1.freecodecamp.org/images/1*O3uO1TQlhbi-qUxdOHCo_A.jpeg)
_Moi essayant d'apprendre NodeJS_

NodeJS nécessite une compréhension fondamentale de JavaScript. Je n'avais définitivement pas cela lorsque j'ai commencé à essayer de l'apprendre. J'ai dû revenir en arrière et regarder des heures de vidéos YouTube expliquant les callbacks, la boucle d'événements, les fermetures, la portée, etc.

J'ai commencé à avoir une assez bonne compréhension, mais je me perdais encore après des tonnes de callbacks. J'utilisais learnyounode et je ne pouvais même pas passer le premier problème sans chercher une solution.

J'ai commencé à consommer une quantité incroyable de tutoriels sur la pile MEAN pour essayer de comprendre les idées de base de l'utilisation d'Express pour le routage et Node. J'ai construit pas moins de 4 applications To-Do différentes, 2 clones de reddit, 1 clone de Twitter et 2 applications de chat, avant de réaliser que je n'absorbais pas vraiment ce qui se passait. Je ne suivais pas aveuglément les instructions, mais elles supposaient que je savais trop de choses sur JavaScript.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Xn-SnhpZniQFjxpUJqIwqA.jpeg)

J'ai commencé à regarder une série sur la chaîne YouTube de TheNewBoston qui m'a vraiment aidé à assimiler les bases. J'allais essayer de faire un autre clone de reddit, jusqu'à ce que je réalise que je devrais apprendre avec quelque chose qui me tient à cœur, l'application de file d'attente Soundcloud que j'ai construite.

J'ai arrêté de regarder des choses et j'ai commencé à lire la documentation. J'ai suivi des tutoriels de démarrage pour essayer de comprendre un peu plus les bases.

J'ai souvent parlé de la sensation de faire "cliquer" quelque chose en programmant, et cette fois j'ai eu la même sensation. C'est un moment que vous n'oubliez jamais parce que votre adrénaline est en ébullition et vous voyez un peu de lumière. Lorsque j'ai pu configurer ma première base de données avec des paires clé-valeur, avoir des événements qui poussent des choses vers la base de données, puis envoyer le JSON à une route que j'avais créée, c'était incroyable. Il était tard et je faisais des poings de victoire dans ma chambre comme un fou.

![Image](https://cdn-media-1.freecodecamp.org/images/1*sXgGtNHK2GgsUBc7ndEQQQ.jpeg)

À partir de là, j'ai commencé à gagner un peu de confiance et je me suis continué à me pousser. J'ai travaillé sur la recherche, le tri et l'incrémentation de mes documents existants dans MongoDB. J'ai réalisé que je voulais un flux en direct, alors j'ai commencé à me pencher sur Socket.io.

Je pense que le problème avec les tutoriels que je consommais auparavant, c'est que je n'ai jamais vraiment appris _pourquoi_ je faisais les choses. Je les faisais simplement sans vraiment y réfléchir. Il est incroyablement important de savoir pourquoi vous faites ce que vous faites.

Au lieu de googler quelque chose qui commence par "Comment faire...", j'ai commencé à chercher le pourquoi et à essayer de comprendre ce qui se passe réellement. Mes recherches ont commencé à ressembler à "Qu'est-ce qu'un jeton de rafraîchissement dans OAuth ?" ou "Qu'est-ce que serialize et deserialize font dans Passport.js ?".

Lorsque j'ai fait ce changement, j'ai vraiment commencé à apprendre.

Il est également très important de continuer à se pousser. Si vous avez quelque chose que vous voulez créer, construisez-le. Il y a toujours un moyen de faire quelque chose, il ne tient qu'à vous de le découvrir (sauf si, bien sûr, c'est une limitation de l'API ou autre chose... alors vous devez simplement devenir un peu hack-y :). Si vous ne savez pas comment authentifier les utilisateurs, essayez d'apprendre. Si vous ne savez pas comment créer une API RESTful, apprenez ! Cela prendra beaucoup de temps, mais une fois que cela cliquera, vous serez ravi.

J'étais tellement dans la zone dimanche dernier que j'ai travaillé jusqu'à 5h du matin lorsque les Seahawks ont commencé à jouer ici à Melbourne. C'était une session de codage de 14 heures. Je n'ai jamais eu autant de plaisir et de concentration avec quoi que ce soit auparavant. C'était une sensation folle.

![Image](https://cdn-media-1.freecodecamp.org/images/1*BvLBslEylPcsjanQ3Grwcw.jpeg)

J'ai enfin compris (enfin, plus ou moins) comment déployer cela avec Heroku et c'est en ligne. Il y a maintenant un flux montrant les chansons qui sont en file d'attente sur le site, ainsi qu'un flux d'artistes en direct en haut à droite montrant les artistes recherchés maintenant sur le site. J'ai également mis en place un classement des 10 meilleures chansons en file d'attente de tous les temps (enfin, depuis le lancement de la fonctionnalité).

Le Random 20 est toujours là pour tous ceux qui l'utilisent pour découvrir de nouvelles musiques. Et grâce à une suggestion sur mon [dernier article](https://medium.freecodecamp.com/building-an-app-outside-of-your-curriculum-7b76aa881d52), j'ai permis aux utilisateurs de se connecter avec leurs comptes SoundCloud et d'aimer des chansons.

Apprendre Node et JavaScript correctement va être un long voyage, mais j'ai de la patience. Il y a trois mois, je ne savais même pas ce qu'était une variable.

Vous pouvez suivre mon aventure sur [Twitter](http://twitter.com/ElliottMcNary) également.