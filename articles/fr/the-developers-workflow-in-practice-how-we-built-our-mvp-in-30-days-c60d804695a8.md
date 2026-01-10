---
title: Le workflow du développeur en pratique — comment nous avons construit notre
  MVP en 30 jours
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-24T21:05:32.000Z'
originalURL: https://freecodecamp.org/news/the-developers-workflow-in-practice-how-we-built-our-mvp-in-30-days-c60d804695a8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*oYtXYYF7F0cBuv2SWm78xA.jpeg
tags:
- name: development
  slug: development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Le workflow du développeur en pratique — comment nous avons construit notre
  MVP en 30 jours
seo_desc: 'By Léna Faure

  As a web developer, I often get to start projects from scratch and make decisions
  for a bunch of elements, from the technical stack to the final look & feel of the
  app.

  Especially when the stakes behind a project are high, this process ...'
---

Par Léna Faure

En tant que développeuse web, j'ai souvent l'occasion de démarrer des projets de zéro et de prendre des décisions pour de nombreux éléments, de la stack technique au look & feel final de l'application.

Surtout quand les enjeux derrière un projet sont élevés, ce processus peut être accablant.

Je souhaite partager notre expérience après un mois au sein du programme de Startups de la Ville de Paris, et les étapes que notre équipe a suivies pour réaliser une première version opérationnelle de l'application.

Un peu de contexte d'abord : [AlloAnim](http://alloanim.futur.paris/) est une application web conçue pour aider la Ville de Paris à trouver instantanément du personnel périscolaire disponible.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vOTtrNbhxh2QW8lnp7yLWA.png)
_Notre page d'accueil actuelle pour le premier Sprint — Inspirée d'AirBnb tout en travaillant sur une nouvelle UI — Crédit Sophie Robichon / Mairie de Paris_

L'objectif est que les employés périscolaires créent et mettent à jour leur profil et leurs disponibilités aussi souvent que possible. Cela permettra à la Ville de Paris d'avoir un accès direct à une base de données mise à jour en temps réel du personnel disponible.

Notre équipe est composée de deux personnes. L'un est Product Owner, Christian Bockarie. Christian est la personne qui a identifié le point de douleur alors qu'il travaillait comme personnel scolaire pour la Ville de Paris.

L'autre est une développeuse (votre serviteuse), responsable de la construction de l'application full-stack sur une période de 5 mois.

Notre quartier général se trouve au laboratoire communautaire d'innovation ouverte [La Paillasse](https://www.freecodecamp.org/news/the-developers-workflow-in-practice-how-we-built-our-mvp-in-30-days-c60d804695a8/undefined). Nous travaillons aux côtés de la Startup _ViteUnLieu_, qui aide les organisations à trouver facilement des salles de conférence à Paris, avec [Jean Karinthi](https://www.freecodecamp.org/news/the-developers-workflow-in-practice-how-we-built-our-mvp-in-30-days-c60d804695a8/undefined) comme Product Owner et [Christophe Robillard](https://www.freecodecamp.org/news/the-developers-workflow-in-practice-how-we-built-our-mvp-in-30-days-c60d804695a8/undefined) comme Lead Developer.

La stack que nous avons choisie est Ruby on Rails pour le back end et du JavaScript « vanilla » (pur, sans Framework) pour le front end.

Nous voulons intégrer React dès que possible, mais pour la phase de prototypage, nous nous en tenons au bon vieux JavaScript.

Alors, comment avons-nous créé un produit fonctionnel à partir de zéro en un mois ? Voici les principales étapes que nous avons suivies pour livrer cette première version avec succès.

### 1. Adopter l'esprit Agile

Nous avons travaillé avec un coach pendant deux jours pour apprendre les bases du [développement Agile](https://en.wikipedia.org/wiki/Agile_software_development).

Le principal enseignement de l'Agile est que vous devez travailler en collaboration très étroite avec vos utilisateurs finaux. L'objectif est d'itérer sur chaque version de votre application en fonction des retours qu'ils fournissent.

De cette façon, vous avez moins de chances de construire quelque chose dont les gens n'ont pas besoin, qu'ils n'aiment pas ou qu'ils ne savent pas utiliser.

### 2. Rencontrer rapidement les utilisateurs dans la vraie vie

Christian a réussi à nous obtenir rapidement une réunion décisive avec la responsable du personnel périscolaire dans une école élémentaire.

Nous avons engagé une conversation constructive sur la façon dont elle gérait actuellement son problème de personnel. Nous avons appris de quelles fonctionnalités elle aurait absolument besoin dans notre futur outil web.

![Image](https://cdn-media-1.freecodecamp.org/images/1*KGtwidYUm7DQ1OxN_9mIzA.jpeg)
_Crédit Sophie Robichon / Mairie de Paris_

Le point de douleur et le besoin pour notre produit se sont avérés tout à fait réels. C'était suffisant pour nous lancer sur un Minimum Viable Product (MVP). Il s'agit d'une version du produit possédant les fonctionnalités nécessaires pour être la première version utilisable de notre produit.

### 3. Rédiger des User Stories

Les User Stories sont un moyen pour un Product Owner non technique et un développeur de se comprendre parfaitement sur ce qui doit se passer pour que l'application remplisse son objectif.

Elles sont rédigées sur le modèle : « En tant que < type d'utilisateur >, je peux < un objectif > (afin de < une raison >). »

Par exemple, l'une de nos User Stories simples était : « En tant que membre du personnel périscolaire, je peux créer un profil avec mes informations personnelles ».

Les User Stories s'assemblent pour former une Story Map, qui est le plan visuel global pour la construction de l'application au fil du temps.

![Image](https://cdn-media-1.freecodecamp.org/images/0*B7p8epBm1iEI8gXx.)

Le cycle de développement du produit est ensuite découpé en sprints.

Chaque sprint contient un nombre donné de User Stories qui seront codées en fonctionnalités.

Notre premier sprint contient typiquement toutes les User Stories nécessaires pour un Minimum Viable Product utilisable.

La Story Map et le contenu des sprints sont libres de changer à chaque itération du produit. Cela coïncide généralement avec une session de feedback avec les utilisateurs.

À mesure que les utilisateurs donnent leur avis sur les fonctionnalités développées, les User Stories évoluent et s'adaptent pour correspondre à l'utilisation réelle de l'application.

### 4. Mettre en place un workflow Agile

J'ai eu la chance de travailler aux côtés du talentueux développeur de l'autre startup, [Christophe Robillard](https://www.freecodecamp.org/news/the-developers-workflow-in-practice-how-we-built-our-mvp-in-30-days-c60d804695a8/undefined), qui a acquis une expérience impressionnante avec les workflows Agile et la productivité des développeurs lors de son expérience précédente au sein du programme des [Startups d'État](https://beta.gouv.fr/).

#### Daily Stand-Up Meetings

Issu de la méthodologie Scrum, le daily stand-up est une réunion debout tenue chaque jour d'un sprint. Nous nous parlons au début de chaque journée pendant 5 à 15 minutes. Nous restons debout si nous sommes physiquement ensemble, ou nous nous parlons au téléphone si nous travaillons à distance.

Cela aide à définir le contexte du travail de la journée à venir et à s'engager sur les tâches qui doivent être traitées ensuite.

#### Dev Backlog

Le backlog du sprint devient visible en le plaçant sur un tableau de tâches, où chaque ligne du tableau est une User Story. Les tâches individuelles plus petites sont écrites sur des « cartes ».

Les membres de l'équipe mettent à jour le tableau de tâches en continu tout au long du sprint en écrivant de nouvelles cartes ou en les déplaçant. Par exemple, une carte pourrait être déplacée de la colonne « To do » à la colonne « Doing ».

![Image](https://cdn-media-1.freecodecamp.org/images/0*GvC5snIP_0CHeDkT.)
_Notre tableau de tâches pour le premier sprint_

Vous pouvez facilement recréer ce tableau de tâches sur le [tableau d'issues Gitlab](https://about.gitlab.com/features/issueboard/) ou sur [Waffle.io](https://waffle.io/) pour une alternative numérique.

#### Réunions bi-hebdomadaires entre Startups

Pour rendre la réunion efficace et directe, la stratégie que Christophe a partagée avec nous est la suivante :

* Fixer une durée maximale pour la réunion (30 minutes à 1 heure)
* Écrire un post-it pour chaque sujet qui sera discuté et ne parler que d'un seul sujet de post-it à la fois
* Fixer un minuteur de 5 minutes pour chaque discussion de post-it  
Si la discussion dépasse 5 minutes, l'équipe décide s'il vaut la peine de relancer le minuteur pour 5 minutes supplémentaires.

![Image](https://cdn-media-1.freecodecamp.org/images/1*B5AxgQYSFi5FsSxDQwCUvA.jpeg)
_Christophe nous a transmis des connaissances intemporelles sur l'Agile, le Lean Startup et le Clean Code_

### 5. S'inspirer de sites web bien conçus et partager un moodboard

C'est l'une de mes parties préférées au début d'un projet — chercher l'inspiration pour l'UX et l'UI auprès d'autres applications web, dont certaines que j'utilise très souvent.

Je suis toujours émerveillée par la créativité et l'ingéniosité des équipes derrière certains des outils que j'utilise. Par exemple, j'ai été inspirée par le processus d'onboarding de [breaz.io](https://hired.com/signup?utm_source=breaz&utm_medium=referral). J'ai également admiré la façon dont [drivy.com](https://www.drivy.com/) permet aux utilisateurs de sélectionner d'abord un groupe de voitures, puis d'envoyer un message unique à chaque propriétaire une fois la sélection faite.

Ici, je vais présenter certains des outils qui m'aident généralement à démarrer et à visualiser les interfaces de l'application.

#### Dribbble

La fonctionnalité de recherche sur [Dribbble](https://dribbble.com/) vous permet de puiser dans l'esprit créatif de grands designers qui exposent leur travail.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6_-A_4N6yX5906d1BbLv0w.png)

#### Moodboard

[Moodboard](http://www.gomoodboard.com/) vous permet de collecter, partager et commenter des designs avec votre équipe. Cela permet à chacun d'avoir un aperçu de l'inspiration pour l'interface du site web :

![Image](https://cdn-media-1.freecodecamp.org/images/1*LpvHYk-wlawKxZee81ahLQ.png)

#### Adobe Color

[Adobe Color](https://color.adobe.com) est la source d'inspiration parfaite pour des palettes harmonieuses. La fonction « Explorer » vous permet de parcourir des milliers de thèmes de couleurs inspirants :

![Image](https://cdn-media-1.freecodecamp.org/images/1*QAUkKlRc8iSJSVWfjQv4Lg.png)

### 6. Créer la première version Rails de l'application

Nous avons mis en place nos modèles et notre base de données avec Ruby on Rails et SQLite. Nous avons utilisé la gem « Devise » pour le système d'authentification.

Je développe généralement le front end et le back end en même temps. Cela signifie que j'essaie de travailler sur le design et la réactivité (responsiveness) de chaque fonctionnalité dès qu'elle voit le jour.

Cela ne manque jamais de produire un effet « wow ! » lors de la présentation des premières démos. Cette première impression peut être un facteur décisif lors de l'adoption d'un produit par les utilisateurs.

Certains développeurs préfèrent se concentrer d'abord sur le back end. Une fois que tout est en état de marche, ils y reviennent plus tard pour l'aspect esthétique. Cependant, je trouve plus facile de travailler sur les deux simultanément.

![Image](https://cdn-media-1.freecodecamp.org/images/0*9dlrcKmkImRLApKt.)

Dans notre application, l'objet principal est l'utilisateur. Nous avons encore du chemin à parcourir pour affiner le système d'onboarding et trouver des incitations pour que l'utilisateur revienne souvent sur l'application.

Pour l'instant, le processus d'inscription est basique et contient simplement les informations clés pour que le MVP fonctionne.

Ci-dessous, quelques captures d'écran du MVP en action !

**Inscription :**

![Image](https://cdn-media-1.freecodecamp.org/images/1*xJX4CoOwV62CIKSHZMKGeA.gif)
_Inscription_

**Recherche de personnel :**

![Image](https://cdn-media-1.freecodecamp.org/images/1*3xw4lw0G-WQbJzbzahZ6cw.gif)
_Recherche de personnel disponible_

L'application nécessite un calendrier hebdomadaire pour que le personnel périscolaire puisse remplir ses créneaux horaires disponibles. Cependant, je n'ai pas trouvé de gem Rails ou de Plugin JavaScript correspondant aux exigences particulières du MVP.

Je me suis donc lancée dans la construction d'un planificateur de disponibilité hebdomadaire complet en JavaScript, pour ensuite l'intégrer dans l'application Rails. [Vous pouvez trouver le code JavaScript ici si cela vous intéresse](https://github.com/lenafaure/javascript-weekly-scheduler).

**Version 0 (Affichage des semaines) :**

![Image](https://cdn-media-1.freecodecamp.org/images/0*jnA1RfrKBBXR9nb7.)

**Version 1 (Ajout de créneaux horaires spécifiques et comportement responsive) :**

![Image](https://cdn-media-1.freecodecamp.org/images/0*VJzZki_YqMw6J-Q1.)

**Version 2 (Intégration dans l'application Rails — Page de profil) :**

![Image](https://cdn-media-1.freecodecamp.org/images/1*V0srF2EvciBWjQPdvH14eQ.png)

### 7. Déployer l'application en direct

La dernière étape consiste à mettre l'application en ligne. J'ai trouvé que [**Heroku**](https://www.heroku.com/) rendait l'hébergement un jeu d'enfant. Le déploiement est gratuit, et les instructions sont très simples et disponibles directement sur la plateforme.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5bUSm3xfd7nFNU-KyJPItw.png)
_Instructions de déploiement Heroku_

### 8. Itérer

Enfin, il est temps de rencontrer à nouveau les utilisateurs et de leur présenter le travail que vous avez accompli pendant le sprint.

Nous avons généralement des sprints de 3 semaines. Cela nous donne le temps de coder suffisamment de fonctionnalités pour avoir de la matière à discuter. Cela permet également à notre club d'utilisateurs de souffler entre les réunions.

Pendant la réunion, nous écoutons les retours des utilisateurs et discutons des fonctionnalités de l'application avec eux.

Ensuite, nous retournons au tableau de tâches pour planifier le prochain sprint… Jusqu'à la prochaine fois !

### Conclusion

Les post-its, c'est la vie. Rien de bon ne se passerait dans ce monde sans eux.

![Image](https://cdn-media-1.freecodecamp.org/images/1*VzopnLtVd7gpi1uKnR_6Ag.jpeg)

C'est tout pour le moment ! Nous sommes bien avancés dans notre deuxième sprint et nous déplaçons les post-its avec une agilité stupéfiante.

Tous les outils que vous utilisez pour votre propre processus et que vous souhaiteriez partager avec nous sont les bienvenus !

**Mise à jour :** Le prototype [AlloAnim](http://alloanim.futur.paris/) a été lancé avec succès et est maintenant testé et utilisé quotidiennement par le personnel de la Ville de Paris.

Vous pouvez trouver le [Code Open Source ici](https://gitlab.com/startups-ville-paris/animexpress), et une démo complète de l'application ci-dessous :

_Le programme [#**startupdeville**](https://twitter.com/hashtag/startupdeville?src=hash) est une initiative de la Ville de Paris, portée par des agents publics qui ont identifié un point de douleur clair lors de leur travail sur le terrain._

_Après un processus de sélection et une accélération d'un mois, une équipe de deux personnes (Product Owner + Développeur) construit une application web pour valider le besoin de ce nouveau service et son adoption par les utilisateurs cibles._

Si vous avez apprécié cet article, n'hésitez pas à l'applaudir pour que d'autres puissent le trouver ! N'hésitez pas à [me suivre sur Twitter](https://twitter.com/lenafaure), ainsi que les membres de l'équipe [#startupdeville](https://twitter.com/hashtag/startupdeville?src=hash), [Christian Bockarie](https://twitter.com/BockarieChrist), [Jean Karinthi](https://twitter.com/JeanKarinthi) et [Christophe Robillard](https://twitter.com/krichtof)

— Léna Faure

![Image](https://cdn-media-1.freecodecamp.org/images/1*td_Zl-oX7vl2kIsoldqcLA.png)