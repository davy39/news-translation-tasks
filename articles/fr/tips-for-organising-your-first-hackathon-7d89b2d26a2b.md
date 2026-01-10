---
title: Conseils pour organiser votre premier hackathon
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-07T16:58:44.000Z'
originalURL: https://freecodecamp.org/news/tips-for-organising-your-first-hackathon-7d89b2d26a2b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*RwFLcMAsMJhdbrabPA7j-w.jpeg
tags:
- name: hackathon
  slug: hackathon
- name: learning
  slug: learning
- name: startup
  slug: startup
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Conseils pour organiser votre premier hackathon
seo_desc: 'By Richard Middleton

  On Saturday July 14, freeCodeCamp Oslo had our first hackathon. In the spirit of
  togetherness, we decided to make our hackathon non-competitive. We have lots of
  people who are very new to coding, and wanted them to feel they coul...'
---

Par Richard Middleton

Le samedi 14 juillet, freeCodeCamp Oslo a organisé son premier hackathon. Dans un esprit de communauté, nous avons décidé de rendre notre hackathon non compétitif. Nous avons beaucoup de personnes qui sont très nouvelles en programmation, et nous voulions qu'elles se sentent capables de participer et d'apprendre quelque chose en cours de route.

Ici, à freeCodeCamp Oslo, nous essayons d'apporter un profond sentiment de communauté et de solidarité.

Comme beaucoup de groupes freeCodeCamp, nous avons beaucoup d'expatriés — des personnes qui ont déménagé en Norvège, loin de leurs amis et de leur famille. Cette communauté aide beaucoup de gens, y compris moi-même, à sortir et à rencontrer d'autres développeurs et à nouer des relations.

![Image](https://cdn-media-1.freecodecamp.org/images/AqfJlztuuRLRtQZSi057bUFunPpjDfXPzQNo)
_Rencontre fCC Oslo._

En préparation du hackathon, nous avons décidé si nous allions en faire un événement d'un ou deux jours, en fonction des retours du groupe.

Après avoir sécurisé un lieu à l'incroyable [Explorer HQ](https://www.explorer-hq.com/) (merci à Marek, l'un de nos administrateurs), nous avons décidé de demander à nos membres des idées pour le projet.

Au total, nous avions sept idées, et la semaine précédant l'événement, nous avons examiné leur faisabilité dans les 12 heures dont nous disposions.

Nous avons finalement opté pour la création d'une application web où les utilisateurs pouvaient voir si des étudiants étudiaient autour d'eux. Nous avons ajouté une invitation sur la carte pour encourager la collaboration, et les utilisateurs pouvaient publier leur emplacement pour que d'autres rejoignent leur session d'étude.

Commencant à 10h, nous avons fait quelques présentations et décidé comment répartir les tâches.

Nous avions beaucoup de débutants en développement web parmi nous. Tous étaient plus heureux de contribuer au front end, ou intéressés à l'apprendre. Cela signifiait que c'était à moi de travailler sur le back end.

![Image](https://cdn-media-1.freecodecamp.org/images/tML3FJbawSkRSMjxtZV6jZGENRKTf2M7a60k)
_Courtoisie de [richardCodes](https://instagram.com/richardcodes" rel="noopener" target="_blank" title=")_

Le principal problème que nous avons eu était de ne pas pouvoir utiliser des frameworks comme React pour garder nos appels API secrets. Beaucoup de membres de l'équipe n'avaient jamais utilisé un tel framework auparavant. Au lieu de cela, nous avons opté pour HTML & CSS pour un front end statique, en utilisant jQuery pour faire les requêtes AJAX.

Nous avons également utilisé Bootstrap 4, qui a permis un prototypage rapide. Sa documentation solide a aidé le front end à se concrétiser.

Une autre de nos administratrices, Ekaterina, était responsable du JavaScript côté client. Avec Marek, elle prévoyait de superviser le développement général du front end.

Le dépôt a été créé par Howie, un autre administrateur de freeCodeCamp Oslo, et après avoir obtenu les permissions, nous avons commencé le travail.

L'équipe front end s'est plongée dans la documentation de Google Developers et a rapidement affiché une carte sur le front end.

Le back end allait utiliser NodeJS avec MongoDB et Express, donc d'abord un NPM init a été fait ainsi que l'installation d'Express, Mongoose, Body Parser et quelques autres packages. En une heure et demie, nous avions notre API fonctionnelle.

En attendant le front end, nous avons pu tester l'API en utilisant Postman pour GET et POST des données vers et depuis notre base de données.

![Image](https://cdn-media-1.freecodecamp.org/images/syfV8X3iHGDdk-PzMttuIE8aiommg2m3JtI1)
_L'heure de la pizza, l'incontournable de tout hackathon._

Après le déjeuner (également généreusement sponsorisé par Explorer HQ), nous avons apporté quelques modifications incrémentielles pour les entrées de la base de données. Mais la plupart du travail concernait JavaScript sur le front end, en veillant à ce que nous puissions envoyer nos requêtes GET et POST depuis là.

Bientôt, notre produit minimal viable était [terminé](https://studyfinderoslo.herokuapp.com/).

![Image](https://cdn-media-1.freecodecamp.org/images/YC-POwZJp3XMhXxE7k69MBdN5ea39ExEARtk)
_[https://studyfinderoslo.herokuapp.com](https://studyfinderoslo.herokuapp.com/" rel="noopener" target="_blank" title=")_

C'était génial de travailler en équipe, ce que aucun de nous n'avait vraiment fait auparavant.

Nous avons hébergé le site sur Heroku, et la base de données était hébergée avec MLab. Après une longue journée, nous avions un produit utilisable dont nous ne pouvions pas être plus heureux.

Il restait encore des choses à faire, mais notre MVP était atteint. Le lendemain, j'ai remédié à notre API ouverte en utilisant Passport pour ajouter une authentification Facebook.

De plus, nous avons apporté quelques corrections au site.

![Image](https://cdn-media-1.freecodecamp.org/images/hujz-3PZ2CPGMVD9jtlqfmM6gsctnJnMvz7q)

Dans l'ensemble, l'expérience était géniale. Travailler en une seule équipe de huit personnes a aidé à rendre l'environnement amical et a rapproché tout le monde — ce qui était notre objectif.

Je vous implore d'essayer vous-même et d'organiser un hackathon non compétitif pour votre groupe !

### Alors, comment pouvez-vous organiser votre propre hackathon ?

1. **Limitez-le à une journée** — un jour de week-end fonctionnera le mieux. Étaler l'événement sur plusieurs jours signifie que vous pourriez ne pas avoir les mêmes personnes assistant aux deux jours, et cela pourrait poser un problème de continuité. Nous avons trouvé qu'il était préférable de sonder notre groupe avec plusieurs dates et de choisir la plus populaire.
2. **Trouvez un projet à l'avance** — nous avons crowdsourcé notre processus d'idée, demandant aux utilisateurs de soumettre leurs idées une semaine à l'avance. De cette façon, les leaders du groupe pouvaient se réunir et vérifier la faisabilité.
3. **Sécurisez un lieu** — cela peut être délicat, car vous avez besoin d'un espace suffisamment grand, avec un bon wifi et de l'électricité. Idéalement, vous voulez pouvoir apporter vos propres collations, etc. Peut-être que quelqu'un dans votre groupe a un lieu de travail libre le week-end ? Ne vous sentez pas intimidé pour sortir et envoyer quelques emails à des personnes de la communauté tech. À défaut, réunissez tout le monde chez vous.
4. **Rendez-le collaboratif, pas compétitif** — nous apprenons tous et certains peuvent se sentir dépassés si vous le rendez compétitif. Divisez le groupe en différentes sections. Peut-être avez-vous un leader front end et un leader back end, et ils peuvent ensuite répartir les personnes pour traiter les barres de navigation, les modales, JavaScript, les bases de données, etc. N'ayez pas peur de vous lancer même si vous ne vous sentez pas sûr de ce que vous faites — vous pourriez vous surprendre !

Vous n'avez pas besoin d'avoir déjà organisé un hackathon — je n'en avais même jamais participé à un auparavant ! Toute l'expérience a rapproché notre groupe. Nous avons réussi à construire quelque chose de cool qui pourrait aller dans notre portfolio, et nous pouvons tous prétendre avoir gagné le Summer Hackathon de freeCodeCamp Oslo !

Vous pouvez consulter le dépôt [ici](https://github.com/howieandersen/FreeCodeCampHackathon001). Le site hébergé est [ici](https://studyfinderoslo.herokuapp.com/).