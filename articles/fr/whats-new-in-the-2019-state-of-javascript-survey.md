---
title: Quoi de neuf dans l'enquête 2019 sur l'état de JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-27T00:08:16.000Z'
originalURL: https://freecodecamp.org/news/whats-new-in-the-2019-state-of-javascript-survey
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f02740569d1a4ca4055.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Quoi de neuf dans l'enquête 2019 sur l'état de JavaScript
seo_desc: 'By Sacha Greif

  We just opened the 2019 State of JavaScript survey. Go take it if you haven''t done
  so already!

  It''s now the fourth time we''re doing this survey, and each time we take a deep
  look at our big YAML file containing all our questions to see...'
---

Par Sacha Greif

Nous venons d'ouvrir l'[enquête 2019 sur l'état de JavaScript](http://survey.stateofjs.com/?source=fcc). [Allez y répondre](http://survey.stateofjs.com/?source=fcc) si vous ne l'avez pas encore fait !

C'est maintenant la quatrième fois que nous réalisons cette enquête, et chaque fois nous examinons en profondeur notre grand fichier YAML contenant toutes nos questions pour voir ce qui reste et ce qui part. Donc, au cas où vous seriez curieux, voici un rapide aperçu de tout ce qui est nouveau dans l'enquête de cette année.

## Langage et motifs

Le plus grand changement structurel est que nous avons maintenant une nouvelle section "Langage" qui pose des questions sur JavaScript en tant que langage lui-même. Utilisez-vous la destructuration ? Qu'en est-il des fonctions fléchées ? Avez-vous regardé les Maps et les Sets ? Et êtes-vous plutôt un programmeur fonctionnel ou un codeur orienté objet ?

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-27-at-8.47.13.png)

Nous avons également une section entière sur les API de navigateur afin de voir à quel point chacune d'entre elles est populaire.

Le but est de se faire une idée non seulement des bibliothèques que les gens utilisent, mais aussi de ce à quoi ressemble leur code réel.

## Nouvelles bibliothèques : Svelte, Cypress, et plus

En parlant de bibliothèques, nous avons également quelques nouveaux entrants.

Tout d'abord, il y a [Svelte](https://svelte.dev/), qui a fait beaucoup de vagues dans la communauté tout au long de 2019. C'était aussi notre réponse n°1 "autre" dans la section front-end l'année dernière, donc il était logique de l'inclure.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-26-at-16.06.57.png)

Dans la section back-end, nous avons ajouté [Nuxt](https://nuxtjs.org/) et [Gatsby](https://www.gatsbyjs.org/). Ils ne sont pas des frameworks back-end "traditionnels" comme Express ou Koa, mais ils ont gagné tellement en popularité récemment que ne pas les ajouter semblait être une négligence.

Dans la section testing, nous avons ajouté [Cypress](https://www.cypress.io/) et [Puppeteer](https://github.com/puppeteer/puppeteer), et dans la section mobile & desktop [NW.js](https://nwjs.io/) et [Expo](https://expo.io/).

## Section Ressources

Tout comme nous l'avons fait pour l'enquête de cette année sur le [State of CSS](https://2019.stateofcss.com/), nous avons également ajouté une section Ressources pour en savoir plus sur les blogs, ressources et podcasts les plus populaires.

## Un front-end d'enquête personnalisé

Enfin, sur le plan technique, le grand changement cette année est que nous utilisons notre propre plateforme d'enquête maison pour la première fois au lieu de nous appuyer sur [Typeform](https://typeform.com/).

C'est quelque chose dont nous avions parlé depuis un moment, mais nous ne l'avons pas considéré sérieusement jusqu'à ce que nous réalisions que Typeform avait changé leurs prix, et que leur plus grand plan était maintenant limité à 10 000 réponses par mois ! Typeform n'était pas intéressé à nous accommoder, donc avec la fin de l'année qui approchait, je me suis mis au travail pour bricoler une application d'enquête.

Heureusement, j'avais une arme secrète dans ma poche : [Vulcan.js](http://vulcanjs.org/), un framework JavaScript full-stack qui est parfait pour assembler rapidement des applications web ; et j'ai pu construire toute l'application (vous pouvez [trouver son code ici](https://github.com/StateOfJS/StateOfJS-Vulcan)) en environ cinq jours en utilisant le module de génération de formulaires de Vulcan.

Aller aussi vite avait quelques inconvénients. Nous avons eu notre part de petits bugs, mais rien de majeur jusqu'à présent. De plus, nous exigeons maintenant que vous créiez un compte avant de remplir une enquête. Autant nous aimerions supporter les utilisateurs anonymes, nous n'avons pas eu le temps de mettre en place des sauvegardes appropriées contre la falsification des données, donc l'exigence de comptes semblait être le choix le plus sûr.

Je pense que c'était le bon choix. Alors que nous importons les données des années précédentes dans notre nouvelle application d'enquête, nous pourrons vous donner accès à ces données afin que vous puissiez voir comment vos réponses ont évolué au fil du temps (à condition que vous ayez utilisé le même email) ; et aussi faciliter l'accès à nos données pour que d'autres puissent créer leurs propres visualisations de données.

Tout cela étant dit, la meilleure façon de découvrir toutes ces nouvelles fonctionnalités est d'aller voir par vous-même ! Alors [répondez à l'enquête](http://survey.stateofjs.com/?source=fcc), et aidez-nous à déterminer les dernières tendances JavaScript de cette année.