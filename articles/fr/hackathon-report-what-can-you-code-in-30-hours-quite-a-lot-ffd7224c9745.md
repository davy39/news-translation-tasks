---
title: 'Rapport de hackathon : Que pouvez-vous coder en 30 heures ? Pas mal de choses
  !'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-25T23:06:33.000Z'
originalURL: https://freecodecamp.org/news/hackathon-report-what-can-you-code-in-30-hours-quite-a-lot-ffd7224c9745
coverImage: https://cdn-media-1.freecodecamp.org/images/1*42-G6mLr8857p66NkXV7wg.jpeg
tags:
- name: '#chatbots'
  slug: chatbots
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: 'Rapport de hackathon : Que pouvez-vous coder en 30 heures ? Pas mal de
  choses !'
seo_desc: 'By Ajay NS

  What can you build in 30 hours straight? As a group of second year college students
  with a growing portfolio of work, my team and I wanted to find out. So we signed
  up to a hackathon.

  It was a Financial Technology (or ‘Fintech’) hackathon ...'
---

Par Ajay NS

Que pouvez-vous construire en 30 heures d'affilée ? En tant que groupe d'étudiants de deuxième année d'université avec un portfolio de travaux grandissant, mon équipe et moi voulions le découvrir. Nous nous sommes donc inscrits à un hackathon.

C'était un hackathon de technologie financière (ou « Fintech ») organisé par la DCB Bank dans la ville de Mumbai. Bien que nous n'ayons aucune idée de ce qu'était la Fintech, nous voulions essayer, dans l'espoir de trouver une idée qui résolve un problème général.

L'événement a été accueilli dans le magnifique et chaleureux espace de coworking de [91 Springboard](http://www.91springboard.com/). C'était un environnement dans lequel je n'avais jamais été auparavant.

En gros, il loue des bureaux pour des startups, des freelances et d'autres qui n'ont pas besoin d'un immense bureau, mais juste d'un espace de travail pour que les membres de leur équipe collaborent. 91 Springboard s'occupe de fournir des espaces de travail amusants, colorés et douillets, une connexion internet rapide et du **café à volonté**, pendant que vous travaillez sans tracas. C'était vraiment un plaisir de s'y installer pour le week-end.

![Image](https://cdn-media-1.freecodecamp.org/images/XnC9zo9Cymm0KlCNv2Mvst7-UGVWvzRVOjnQ)

### L'idée

> Pour dire les choses simplement, nous voulions construire un chatbot spécialisé.

**Pourquoi ?**

Il est prévu que d'ici 2020, un pourcentage énorme de la communication d'entreprise se fera via des chatbots.

L'expérience utilisateur (« UX ») évolue rapidement. Avec la popularité croissante des applications de messagerie, les utilisateurs préfèrent accéder à tout sous une seule application. Ils sont également en faveur d'une communication individuelle.

L'époque des e-mails est révolue, tout tourne désormais autour du chat en temps réel. Avec la technologie d'aujourd'hui, il est possible de créer un chatbot capable d'apprendre par lui-même et d'automatiser la plupart des tâches, permettant une communication de masse à un niveau individuel.

Voir [ici pour une liste](https://medium.com/the-mission/11-best-uses-of-chatbots-right-now-1c27764b7e62) de certaines des meilleures utilisations des chatbots en ce moment**.

### **Qu'avons-nous construit exactement ?**

Comme nous étions à un hackathon Fintech, nous avons pensé à un bot qui effectue toutes les fonctions pouvant être réalisées par l'application de la banque et plus encore — via le chat.

Une fois connecté, vous pouvez demander au bot votre solde, vos dernières transactions, et aussi effectuer des actions telles que des transferts de fonds. Il exploite les API requises fournies par la banque à ces mêmes fins.

![Image](https://cdn-media-1.freecodecamp.org/images/KNck0NbniE8cdF86k9Eg0wA4iwEJcxGX4Nba)

Ci-dessus se trouve une capture d'écran de certaines de nos inspirations UX. Cette UX combinait langage naturel et options multiples, directement fournies sous forme de liens et de boutons. Le flux de réponse aux requêtes des utilisateurs, suggérant les étapes suivantes et permettant également d'effectuer des actions, a été planifié.

### Le projet

![Image](https://cdn-media-1.freecodecamp.org/images/HWWqgqRzXJr4PPZ6la9OYmIPj21v5ePVgS01)
_Le produit final_

La tech stack que nous avons choisie était Ruby on Rails. Nous l'avons choisie parce que mes coéquipiers la connaissaient très bien, et je me concentrais principalement sur l'intégration des API et de l'UI. Mais cette stack était totalement nouvelle pour moi, car j'ai toujours travaillé sur des stacks JavaScript ou Python. J'ai écrit sur mon parcours d'apprentissage [ici](https://hackernoon.com/ruby-on-rails-and-full-stack-javascript-ecadf631707).

Il utilise une base de données PostgreSQL de base pour stocker les messages des utilisateurs, et utilise ActionCable pour le streaming de données en direct selon les besoins. L'ensemble du site (ainsi que le chat sous forme de widget) est construit sur le Framework Materialize.

L'une des fonctionnalités clés que nous avions prévu d'utiliser était une IA personnalisée, plutôt que d'opter pour quelque chose comme IBM Watson ou api.ai. Celle-ci a été encapsulée dans une API utilisant Flask.

![Image](https://cdn-media-1.freecodecamp.org/images/c9JStBkursr9SEEMdQubeJongaAtBpeRQBTo)
_Cartographie des intentions_

Au départ, lorsque le bot a peu ou pas de données d'entraînement, une assistance humaine est requise pour donner des réponses et aussi classer l'intention de chaque requête utilisateur pour que le bot apprenne. Une fois qu'il accumule des données, il peut automatiser tout le processus, en donnant des réponses appropriées.

Quelques-uns des scripts utilisés pour l'IA sont disponibles [ici](https://github.com/dhanushkamath/DCBHackathonScripts).

### Le hackathon

Nous avons réussi à dormir quatre heures sur une période de plus de 30 heures, tout en poussant plus de 50 000 lignes de code en production.

Mais ce n'était pas aussi terrible que ça en a l'air ! L'endroit lui-même dégage une ambiance motivante, et il y a des mentors pour vous aider. Il y avait des pauses entre les deux pour se détendre avec d'autres équipes et apprendre à connaître d'autres développeurs de génie.

Pendant que mes coéquipiers se concentraient sur la partie Machine Learning et l'application de chat réelle sur Rails, j'ai travaillé sur l'UI du service. Cela incluait un panneau d'administration ainsi que le widget de chat. Pas mal de temps a été consacré à l'encapsulation du code de l'IA dans des API RESTful et à la correction de bugs dans le code principal également.

Au final, ce que nous avions était une version alpha de base de l'application que nous avions entrepris de construire.

![Image](https://cdn-media-1.freecodecamp.org/images/2AXEaHn82ZUk7811EC-oWnUzGoytyFvGShP6)

### L'expérience

> Pour commencer, ce furent les 30 heures les plus productives de ma vie.

Avec des bouffées constantes de motivation (et de caféine) pour me stimuler, il n'y avait pas de temps pour rester assis ou paresser. Beaucoup de gens amusants et talentueux avec qui interagir également, car j'étais l'un des plus jeunes là-bas.

Voici quelques-unes des choses que j'ai apprises ici :

* Architecture d'application découplée
* Construire une application à partir de zéro puis la pousser en déploiement dans le délai le plus court possible
* Collaboration de code en direct
* et bien sûr, un peu de Fintech !

Découvrez le projet sur lequel nous avons travaillé ici : [chaturbots.com](http://chaturbots.com/). Ceci est proposé comme un service maintenant, alors contactez-nous pour faire construire un bot personnalisé.

J'espère que vous avez apprécié cet article et que vous l'avez trouvé intéressant ! Vous pouvez consulter tous mes projets sur [Github](http://github.com/ajayns/) et me contacter sur [Twitter](https://twitter.com/ajayns08) !