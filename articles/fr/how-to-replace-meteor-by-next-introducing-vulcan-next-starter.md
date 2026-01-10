---
title: Comment remplacer Meteor par Next — Présentation de Vulcan Next Starter
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-01T06:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-replace-meteor-by-next-introducing-vulcan-next-starter
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/vulcan-next-starter-white-bg_1200.png
tags:
- name: GraphQL
  slug: graphql
- name: Meteor
  slug: meteor
- name: Next.js
  slug: nextjs
- name: node
  slug: node
- name: React
  slug: reactjs
seo_title: Comment remplacer Meteor par Next — Présentation de Vulcan Next Starter
seo_desc: 'By Eric Burel

  2020, still looking for a productive JS framework

  When you create a product for your own company, you are free to spend time setting
  up a development environment that fits your own quirks. Granted, you''ll likely
  spend a reasonable amoun...'
---

Par Eric Burel

## 2020, toujours à la recherche d'un framework JS productif

Lorsque vous créez un produit pour votre propre entreprise, vous êtes libre de passer du temps à configurer un environnement de développement qui correspond à vos propres particularités. Certes, vous passerez probablement un temps raisonnable.

Mais lorsque vous développez pour d'autres, vous n'avez pas cette liberté. Vous devez livrer un code de haute qualité dans un délai prévisible.

Pour être compétitif, vous devez vous adapter à différents clients. Chaque application ne peut pas être votre première application. Les connaissances et le code générique doivent être réutilisés. La plupart du temps, cela signifie s'appuyer sur des frameworks.

En tant que propriétaire d'une agence, j'ai toujours aimé Meteor. C'est l'un des rares frameworks JavaScript vraiment axés sur la productivité : une architecture basée sur les packages, une approche isomorphe, une solution de persistance prête à l'emploi...

Je suis également un contributeur principal du framework [Vulcan.js de Sacha Greif](http://vulcanjs.org/). Vulcan est un framework full-stack opinionné, implémenté comme un sur-ensemble de Meteor. Il va plus loin en fournissant des modèles déclaratifs pour un développement très rapide et en s'appuyant sur Apollo GraphQL.

Tout (schéma GraphQL, API, structure de la base de données, formulaires, tableaux de données, etc.) est automatiquement généré à partir d'un schéma JavaScript. Cool, n'est-ce pas ?

![Image](https://www.freecodecamp.org/news/content/images/2020/06/how-vulcan-works.svg)

Mais les limitations de Meteor sont un plafond de verre. J'ai eu des projets réussis avec Meteor et Vulcan, mais je n'ai jamais pu pousser ces frameworks vers de plus grands clients. Trop de problèmes de scalabilité, manque de traction, mauvais outils de test, vous voyez le tableau.

Retour à la case départ, je devais trouver un framework avec lequel je pourrais m'engager.

## Next vs Meteor ?

### C'est comparer des pommes et des oranges !

[Lorsque j'ai découvert Next pour la première fois en 2017](https://medium.com/@eric.burel/next-the-next-big-thing-c7f9c34f9cce), c'était un framework prometteur, mais uniquement front-end. Front-end uniquement. Je l'ai utilisé pour construire le site web de mon entreprise, puis je l'ai oublié.

Et puis, les gens autour de moi ont commencé à agir bizarrement. Ils parlaient soudainement de deux frameworks n'ayant rien en commun, Meteor et Next, comme s'ils étaient interchangeables. Vous avez remplacé Meteor par Next ? Pourquoi ne pas remplacer Express par Create React App tant que vous y êtes ?

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-240.png)
_Vous pouvez même utiliser create-react-app pour combattre les hackers. Capture d'écran de l'émission française "Bureau des légendes" (Canal +)._

Autant que je m'en souvienne, [Reaction Commerce a été l'un des premiers frameworks non triviaux à faire le changement.](https://blog.reactioncommerce.com/reaction-v2-0-0-release-preview/)

Je n'étais pas convaincu. Et en effet, ils ont encore dû implémenter une API GraphQL sur leur application Meteor pour communiquer avec leur front-end Next. Échanger un framework contre deux n'est pas la meilleure affaire, donc nous avons gardé Vulcan comme un framework basé sur Meteor.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/next-static.png)

Si vous pensez que comparer Meteor à Next, c'est comparer des pommes et des oranges, vous n'avez pas tout à fait tort. À ce jour, le slogan de Next est toujours « The React framework ». Pas « The Node framework ».

Et pourtant, j'ai commencé à changer d'avis il y a quelques mois.

### Du front-end au full stack avec les routes API

Les routes API ont été officiellement introduites en juillet 2019 avec la [version v9](https://nextjs.org/blog/next-9).

C'est ce qui m'a remis dans le wagon de Next. Les routes API signifient que Next.js est maintenant un framework full-stack minimaliste, mais parfaitement viable.

Vulcan est construit autour de GraphQL. Et GraphQL est un excellent choix pour les routes API. L'API est servie via un point d'entrée /graphQL unique et dynamique. Dans Next, cela se traduit par la création d'une route API graphql.js. Facile comme bonjour.

## De nos jours, Next couvre tout le spectre, du statique au full stack

Next est de plus en plus appelé un framework "hybride". Cela a du sens, car sa polyvalence est extrême.

* Vous pouvez développer une application full-stack avec un back-end de type serverless.
* Vous pouvez développer une application SaaS avec un rendu côté serveur dynamique.
* Vous ne voulez pas maintenir un serveur ? Vous pouvez suivre la philosophie JAMstack et exporter une application statique avec un rendu côté serveur au moment de la construction.
* Si vous êtes allergique au JavaScript côté client, vous pouvez aller jusqu'à supprimer JavaScript du bundle et ne garder que le code HTML.

Mais ne pensez pas que Next est un touche-à-tout. C'est un concurrent sérieux de Gatsby dans sa forme statique. C'est une alternative prometteuse à Meteor dans sa forme full-stack. Vercel (ex Zeit) a fait un travail tremendous pour le garder à la fois de haute qualité et très léger, quel que soit le cas d'utilisation.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/next-production.png)

## Ne laissez pas tomber Meteor pour autant

Je veux clarifier quelque chose. Remplacer Meteor par Next en tant que framework principal dans Vulcan ne signifie pas que nous pensons que Meteor doit être abandonné.

Il y a une chose importante que nous avons apprise de nos expériences avec Apollo et Meteor dans Vulcan : si vous prévoyez d'utiliser Meteor, adoptez simplement son fonctionnement. Oubliez GraphQL. Oubliez Webpack. Bien que créés par les mêmes personnes, Apollo et Meteor entrent souvent en conflit. C'est étrange pour les développeurs GraphQL, c'est étrange pour les puristes de Meteor.

Utilisez DDP, les méthodes, pub/sub, apprenez à scaler votre application, rejoignez le forum, achetez des tasses à café avec le logo de Meteor. [Maintenant que Tiny a relancé Meteor](https://techcrunch.com/2019/10/02/tiny-acquires-meteor), c'est un pari sûr pour les années à venir.

Avec Vulcan + Next, nous cherchons simplement à fournir une alternative GraphQL à Meteor. Ce n'est ni pire ni meilleur, c'est la même philosophie avec une implémentation différente.

Un framework est comme un instrument de musique. Ne choisissez pas le plus tendance, choisissez celui qui vous convient. Si votre instrument est Meteor, allez-y.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/vulcan-next-starter--banner-2_1200-1.png)

## Présentation de Vulcan Next Starter, une application Next de pointe

Utiliser Next tel quel est parfaitement bien. Vous obtenez un système de build, une solution de styling, une structure de dossiers rationnelle.

Mais si vous voulez construire une application pour la prochaine startup à un milliard de dollars, vous aurez probablement besoin de quelques outils supplémentaires. Souvenez-vous, nous cherchons une alternative à Meteor axée sur la productivité.

Une configuration intéressante pourrait être celle-ci :

* Cypress et Jest pour les tests unitaires et e2e
* Storybook pour les tests visuels et la documentation de conception
* Internationalisation, alias i18n (surtout si vous êtes de France comme moi :))
* TypeScript, pour exprimer votre modèle de domaine à travers des types statiques
* Material UI pour obtenir un ensemble solide de composants de base personnalisables
* Apollo Client pour communiquer avec les API GraphQL
* Optionnellement, Apollo Server pour configurer un point d'entrée GraphQL, avec Playground et Voyager pour l'exploration de l'API

Next fournit [quelques exemples dans son dépôt principal](https://github.com/zeit/next.js/tree/canary/examples). Mais ce n'est pas suffisant dans un contexte réel. Ces outils peuvent interagir ensemble de manière inattendue.

Taper des composants uniquement côté client comme Leaflet ou Plotly peut s'avérer difficile. Il en va de même pour unifier le système de build de Next, Jest et Storybook, ou éviter les mauvaises interactions entre Apollo et Material UI lors du rendu côté serveur. La redirection avec SSR signifie gérer conjointement les scénarios serveur et client. L'i18n est particulièrement difficile à configurer seul. Et la liste continue.

Croyez-moi, vous ne voulez pas affronter de tels problèmes seul. Et devinez quoi ? Nous avons traversé ces tracas pour vous !

**Tous ces outils sont installés dans notre nouveau et brillant,** [**Vulcan Next Starter**](https://github.com/VulcanJS/vulcan-next-starter)**.**

Nous avons encore un long chemin à parcourir, mais nous sommes fiers de dire qu'il est sûr de l'utiliser en production.

## Prochaines étapes

Notre boilerplate ne remplit que la moitié de notre promesse. Vous obtenez une configuration front-end cool, mais il vous manque toujours une base de données et des directives pour implémenter le back-end. Ce n'est pas vraiment comparable à Meteor à ce stade. Une poignée de lambdas n'est pas un framework. Ni l'abonnement à des solutions hébergées dans le cloud.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/vulcan-logo.png)

C'est là que Vulcan intervient. Au fil des ans, nous avons élaboré un puissant générateur d'API GraphQL, avec Mongo comme base de données et des tonnes d'utilitaires front-end. Naturellement, la prochaine étape pour nous est de combiner Vulcan et Next pour créer un véritable framework full-stack.

Vous pouvez suivre notre progression en nous rejoignant sur [le Slack de Vulcan](http://slack.telescopeapp.org/).

Next et Meteor seront des citoyens de première classe de Vulcan, mais tout type de technologie front-end ou back-end JS pourrait en profiter. Que ce soit Gatsby ou un micro-service Node personnalisé. Chez Vulcan, nous vendons des pommes ET des oranges, tant qu'elles font de vous un développeur efficace.

Maintenant, il est temps pour nous de retourner au travail, nous avons beaucoup à faire. Espérons vous voir chez [Vulcan](http://vulcanjs.org/) !

## Un starter des tranchées

Un merci spécial à Aplines, qui a fait confiance à mon entreprise (LBKE) en utilisant les dernières technologies pour leur produit. Grâce à eux, nous avons testé toutes les fonctionnalités incluses dans Vulcan Next Starter ensemble dans une application professionnelle réelle.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/logos-aplines-lbke-1.png)

Ils recherchent des développeurs, donc si vous voulez en savoir plus sur l'utilisation de Next et GraphQL à grande échelle, c'est l'endroit où aller : [job@aplines.com](mailto:job@aplines.com)