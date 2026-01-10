---
title: Mon ami John a fait une erreur avec CSS Grid. Ne soyez pas comme John — faites
  ceci à la place.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-05T17:47:27.000Z'
originalURL: https://freecodecamp.org/news/my-friend-john-made-a-mistake-in-css-grid-dont-be-like-john-do-this-instead-91649f480da1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6LAcBU9G4jdmWgZADQnmSQ.jpeg
tags:
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Mon ami John a fait une erreur avec CSS Grid. Ne soyez pas comme John —
  faites ceci à la place.
seo_desc: 'By Emmanuel Ohans

  It had been two years and John had no job.

  John was a smart 20-something guy. Okay, he had a job — but it wasn’t one he liked.
  It was too monotonous and was not nearly creative enough. His day job only bored
  the hell out of him.

  The...'
---

Par Emmanuel Ohans

Cela faisait deux ans que John n'avait pas de travail.

John était un jeune homme intelligent d'une vingtaine d'années. D'accord, il avait un travail — mais ce n'était pas celui qu'il aimait. Il était trop monotone et pas assez créatif. Son travail de jour l'ennuyait à mourir.

### La recherche d'emploi

Pour John, il semblait que ce n'était pas difficile d'apprendre à coder. Il s'est auto-formé et a commencé à chercher l'opportunité de quitter son travail ennuyeux — enfin.

Après un mois de recherche d'emploi infructueuse, il a reçu un appel de Sharon.

Sharon était la recruteuse pour _youknowho_ Inc, une startup en IA dans la vallée.

Avec beaucoup d'enthousiasme, John a traversé tout le processus d'embauche. Devinez quelle était la partie intéressante ?

Cet appel de Sharon.

Elle a posé quelques questions sur son parcours, et John ne pouvait pas attendre pour partager sa journée de travail typique, monotone et ennuyeuse avec elle.

Il a essayé de se dire que ce n'était pas grave s'il n'obtenait pas le poste. Au moins, ce sont les mots qu'il a murmuré à la fin de l'appel. « Je devais juste partager comment je me sentais vraiment à propos de mon travail actuel », a-t-il dit.

Les semaines ont passé, et c'était comme un rêve quand il a obtenu un poste de développeur frontend junior.

Et c'est là que l'histoire commence.

### John rencontre Khalid et le CSS Grid

Khalid n'était pas un DJ.

S'il l'avait été, alors tout ce qu'il aurait mixé aurait été du code propre, et non des chansons.

Si vous vouliez ruiner une belle après-fête, alors faites de Khalid votre DJ. Vous n'obtiendriez rien de moins qu'un complet désastre.

Khalid n'était pas un grand fan de chansons de toute façon, mais qui a besoin d'aimer la musique quand on est tech lead dans une startup en plein essor dans la Vallée ?

En tant que tech lead, Khalid était responsable de toute l'équipe de développement. Cela signifiait plus que simplement gérer les problèmes techniques — cela signifiait aussi qu'il devait gérer des personnes de différents horizons.

Et c'est une chose sacrément difficile à réussir. Mais Khalid excellait non seulement en tant que grand leader technique. Il avait une relation impeccable avec l'équipe de développement.

Ce n'était pas une surprise que les deux aient commencé à discuter presque immédiatement. Qui n'aimerait pas John ?

Ses larges sourires étaient suffisants pour éclairer un tunnel. Il souriait toujours. Qui fait ça !

### De retour au bureau

Tout le monde était prêt à travailler.

John est entré avec une tasse de café. C'était le matin, et le bureau commençait tout juste à s'animer.

Bon lundi matin, hein ?

« Alors, John, c'est agréable de vous avoir rejoint l'équipe de développement. Je me demandais si vous étiez prêt à prendre une nouvelle tâche aujourd'hui ? » a demandé Khalid.

« Hé, patron. Je suis né prêt ! »

C'est John pour vous. Il est né prêt — en effet. Un gars heureux.

« Euh, j'ai besoin que vous configuriez une nouvelle page de destination pour notre nouveau produit. Et nous voulons qu'elle soit écrite avec le CSS Grid. Vous en avez déjà entendu parler ? »

« Oh oui, j'en ai entendu parler », a rapidement répondu John.

### Apprendre le CSS Grid

John n'avait aucune idée de ce qu'était le CSS Grid.

La seule raison pour laquelle il a dit oui était qu'il ne voulait pas avoir l'air stupide devant Khalid.

Il a cherché sur Medium et a trouvé de grands articles sur le CSS Grid. Il a lu à sa guise et a commencé à travailler sur la mise en page.

### La mise en page que John a construite

John avait beaucoup d'expérience avec Bootstrap.

Il était assez familier avec le concept d'une grille de 12 colonnes. Donc, avec le CSS Grid, la première chose qu'il a faite a été de configurer une grille de 12 colonnes comme ceci :

```
grid-template-columns: repeat(12, 1fr)
```

« Haha, c'était facile », a-t-il pensé.

En fait, John a fait cela pour chaque projet secondaire sur lequel il a travaillé en apprenant le CSS Grid.

John aimait travailler avec le CSS Grid, et il trouvait cela amusant.

Il a fait quelques erreurs, et certaines choses n'ont pas fonctionné comme il l'espérait, mais il a pu corriger rapidement les problèmes.

Il savait comment chercher des choses sur Google. De nos jours, tout le monde devrait savoir faire cela.

### La réunion avec Khalid

« Je l'ai fait fonctionner maintenant, patron. »

Khalid était ravi de voir John. Ils ont discuté de son expérience de construction de la mise en page, et Khalid a continué à examiner le code.

Eh bien, chaque mise en page construite avec le CSS Grid commence presque toujours par la définition de la grille. Donc, c'est là que Khalid a regardé en premier.

« Oh, mon ami. Il y a quelque chose qui ne va pas ici. »

### Pourquoi avez-vous créé 12 colonnes ?

Et Khalid a commencé son discours...

Les grilles de 12 colonnes sont populaires dans le design web aujourd'hui. Mais l'idée derrière le CSS Grid est de créer le nombre de colonnes dont vous avez besoin sans alourdir la mise en page avec des colonnes dont vous n'avez pas vraiment besoin.

La mise en page CSS Grid vous oblige à penser aux mises en page en CSS un peu différemment de ce que nous avons fait pendant plus de 20 ans.

C'est un changement de jeu, qui inclut beaucoup de désapprentissage.

« Une approche plus propre aurait été de créer les 2 ou 3 colonnes dont vous aviez besoin et de simplement continuer avec le design », a dit Khalid.

« Il n'y a aucun mal à redéfinir le nombre de colonnes dans la requête média aussi. Cela le rend parfait pour le design réactif. »

### La leçon

Avec la mise en page CSS Grid, vous n'êtes pas lié à un nombre fixe de lignes ou de colonnes.

Vous n'avez pas non plus à créer 12 colonnes à chaque fois. Si vous n'avez pas besoin de 12 colonnes, ne les créez pas. Le CSS Grid n'est pas un autre framework CSS basé sur une grille.

Vous êtes libre.

Comme l'a souligné [Per Harald Borgen](https://www.freecodecamp.org/news/my-friend-john-made-a-mistake-in-css-grid-dont-be-like-john-do-this-instead-91649f480da1/undefined), vous pouvez créer 12 colonnes si vous voulez expérimenter avec les espaces blancs entre les colonnes.

![Image](https://cdn-media-1.freecodecamp.org/images/8wHBbhPdpWRK0gxEajL7i1tBWu4HrEvWCBQo)

Autrement, créez le nombre de colonnes dont vous avez vraiment besoin, et continuez avec le design.

### Utiliser la mise en page CSS Grid fait avancer le web

J'ai lu une [réponse](https://www.quora.com/Why-does-Apple-keep-getting-rid-of-things-instead-of-adding-them/answer/Brett-Bilbrey?share=baaad454&srid=tLgv) sur pourquoi Apple continue à se débarrasser des choses, au lieu de les ajouter.

Là, j'ai appris ceci :

> « Supporter l'héritage n'est pas toujours la meilleure réponse. Abandonner des choses aide l'industrie à avancer pour adopter de nouveaux formats, meilleurs. »

De la même manière, choisir d'apprendre et d'utiliser le CSS Grid fait avancer le web. Cela aide l'industrie à adopter de nouveaux formats et meilleurs. Cela nous aide à grandir en tant que communauté. Une communauté que nous aimons tant et que nous voulons voir grandir.

Soyez comme Khalid. Commencez à utiliser le CSS Grid si vous le pouvez.

Dans la mesure du possible, investissez dans une éducation décente sur le CSS Grid. Vous aiderez à faire avancer le web.

### Vous voulez devenir un pro ?

Téléchargez ma feuille de triche CSS Grid gratuite, et obtenez également deux cours interactifs de qualité sur Flexbox gratuitement !

![Image](https://cdn-media-1.freecodecamp.org/images/qiv3YiI0rzHObFRmGQwGNA0Lm9p4EWMLfMWp)
_[Obtenez la feuille de triche CSS Grid gratuite + deux cours de qualité sur Flexbox gratuitement !](http://eepurl.com/dcNiP1" rel="noopener" target="_blank" title=")_

[Obtenez-les maintenant](http://eepurl.com/dcNiP1) ?