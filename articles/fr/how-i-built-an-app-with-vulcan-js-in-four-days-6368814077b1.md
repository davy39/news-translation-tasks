---
title: Comment j'ai construit une application avec Vulcan.js en quatre jours
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-11T01:27:58.000Z'
originalURL: https://freecodecamp.org/news/how-i-built-an-app-with-vulcan-js-in-four-days-6368814077b1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*nnLl46hdkKTPVF8pI0Ifhg.png
tags:
- name: Vulcanjs
  slug: vulcanjs
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Comment j'ai construit une application avec Vulcan.js en quatre jours
seo_desc: 'By Eric Burel

  How unambitious I was, a few months ago, when I published “Vulcan: 15 days for an
  app”! 15 days is 3 weeks of work. If you include conception time, that’s a month
  of delay. What if we could reduce it to a week? What if we could develop ...'
---

Par Eric Burel

Que j'étais peu ambitieux, il y a quelques mois, lorsque j'ai publié « [Vulcan : 15 jours pour une application](https://hackernoon.com/the-vulcan-js-challenge-15-days-for-an-app-e3735d1e3d4c) » ! 15 jours représentent 3 semaines de travail. Si vous incluez le temps de conception, cela fait un mois de délai. Et si nous pouvions réduire cela à une _semaine_ ? Et si nous pouvions développer des applications prêtes pour la production en quelques _jours_ ? Voici comment nous atteignons cet objectif.

### Jour 0 : Un peu de contexte

#### Arrêtez de vous appeler une Startup simplement parce que vous produisez du code bâclé plus vite que les autres

Je dirige une entreprise de développement et de conseil nommée LBKE. Nous nous intéressons de près aux technologies qui aident à produire des applications de haute qualité en un temps très limité. Pensez à React Native+Expo pour le mobile, ou Meteor pour les applications web.

Au fil des années, la qualité attendue des Produits Viables Minimaux (MVPs) a considérablement augmenté. Les gens en ont assez des prototypes de mauvaise qualité vendus comme des « produits ».

Maintenant, ils veulent leur logiciel sans bugs (incroyable !), ils veulent une bonne UX (comme ils sont exigeants !), ils veulent des outils qui répondent vraiment à leurs besoins (beurk !). Et bien sûr, ils ne veulent pas payer plus pour cela.

![Image](https://cdn-media-1.freecodecamp.org/images/UiFG9dkquYx6dslh8XvrjMd0rwC0KRFAx89v)

#### Vers l'application en 4 jours

Pour l'entrepreneur, concevoir et construire un tel Produit _Aimable_ Minimum est un travail de taille. Mais l'argent est serré, et le temps c'est de l'argent, alors vous devez être malin dans la façon dont vous le dépensez.

**Notre objectif : être capable de produire une application SaaS en 4 jours.** Nous ne parlons pas d'une application jetable qui ne supportera pas de développement ultérieur. Nous croyons que les technologies bien conçues devraient permettre à la fois un développement à long terme et un développement très rapide : monter en puissance, et réduire l'échelle. Pour la plupart des projets, il n'y a pas besoin de technologies de prototypage. Sauf si vous construisez des vaisseaux spatiaux, mais vous n'en construisez pas, n'est-ce pas ?

De plus, nous n'aimons pas dépendre de services/logiciels tiers qui créent des sites web en quelques clics. Si votre produit est vraiment innovant, vous vous sentez probablement _horriblement_ limité par de tels services.

Alors, comment réalisons-nous ce miracle sans utiliser une baguette magique ? Découvrons-le à travers un exemple concret, GestiResto, une application web qui aide les propriétaires de restaurants à gérer leurs recettes. _Note de bas de page : Je vis en France, nous ne plaisantons pas avec la nourriture ici, alors j'ai vraiment pris ce projet à cœur._

### Jour 1 : Choisir notre vaisseau spatial

#### Rencontrez Vulcan.js, alias Meteor-sur-stéroïdes

Meteor est un framework JavaScript full-stack célèbre. Dès ses débuts, il a toujours mis l'accent sur la productivité et l'expérience du développeur. Il a été pionnier dans de nombreuses fonctionnalités et modèles géniaux, comme le développement isomorphe (réutiliser le même code côté serveur et côté client).

[Vulcan.js](http://vulcanjs.org/) est essentiellement les bons éléments de Meteor, plus les bons éléments de l'écosystème JavaScript, dans un seul framework. Il repose sur les dernières technologies : React pour le frontend, et Apollo (GraphQL) pour la communication client/serveur.

![Image](https://cdn-media-1.freecodecamp.org/images/8dCr7Zq2kiRzH1kC6GLpl-NRTiXZxyXODWin)
_Rejoignez-nous sur Slack !_

En bonus, il inclut de nombreux packages et exemples pour les fonctionnalités les plus courantes (envoi de newsletters, ajout d'un forum, etc.). Vulcan est le petit-fils direct de la célèbre application/framework Meteor Telescope, il a été créé par [Sacha Greif](https://www.freecodecamp.org/news/how-i-built-an-app-with-vulcan-js-in-four-days-6368814077b1/undefined). Il bénéficie ainsi de années d'expérience malgré sa modernité.

Si vous voulez en savoir plus sur Vulcan et comment il aide à réduire le temps de développement, vous pouvez consulter [mon article précédent](https://medium.com/dailyjs/write-less-code-ship-more-apps-how-vulcan-js-makes-me-an-efficient-developer-71c829c76417) dans DailyJS.

Donc, Vulcan.js est définitivement un candidat solide pour respecter notre délai auto-imposé de 4 jours !

#### Un système de gestion des utilisateurs prêt à l'emploi

L'une des fonctionnalités les plus appréciées de Vulcan est son système de comptes, qu'il hérite de Meteor. Il inclut l'inscription/connexion/déconnexion, la gestion des permissions, les workflows d'inscription/mot de passe oublié (+ envoi programmatique d'e-mails), et une belle interface utilisateur. Oh, et il est également assez facile d'ajouter une authentification tierce avec des services tels que [Google Oauth](https://medium.com/@teaganatwater/setting-up-google-oauth-in-vulcanjs-aa53c6010d21).

![Image](https://cdn-media-1.freecodecamp.org/images/RRHcKcYJ2xMkH6BfSW6jszCO85Se7R7kXDlU)
_L'application du jour 1. Le système d'authentification est entièrement fonctionnel à ce stade. Le design Material peut être obtenu avec les packages [vulcan:more-material-ui](https://github.com/ErikDakoda/vulcan-material-ui" rel="noopener" target="_blank" title="">vulcan:material-ui</a> et <a href="https://github.com/lbke/vulcan-more-material-ui" rel="noopener" target="_blank" title=")._

La gestion des comptes est vraiment quelque chose que vous NE voulez PAS penser dans les premières étapes du cycle de vie de votre application. Combien d'heures ont été perdues à configurer Passport.js ! Le nombre de services d'authentification payants tels qu'Auth0 montre que ce problème n'est pas encore résolu, donc c'est vraiment une très belle fonctionnalité.

Donc, notre première journée a été bien utilisée. Nous avons maintenant un système complet de gestion des utilisateurs incluant la base de données, le serveur, l'UI et le back-office, et nous avons mis en place une belle disposition Material UI avec le temps restant.

![Image](https://cdn-media-1.freecodecamp.org/images/Ia55kHRNdUxfIhphz29YA9T-mUFNVu9AGqV7)

### Jour 2 : Hébergement

#### Hébergement sur AWS avec Meteor Up

Pourquoi héberger dès le jour 2 ? Parce que la vie nous a appris qu'il est très mauvais de tester votre application en production le dernier jour. À la manière agile, une fonctionnalité n'est terminée que lorsqu'elle est validée dans un contexte réel. Donc, nous ne pouvons pas considérer que l'application est configurée si nous ne l'avons pas exécutée dans un environnement de production.

Meteor Up est un outil merveilleux pour déployer automatiquement des applications Meteor (donc aussi des applications Vulcan) sur un serveur distant. Il gère tout, de la conteneurisation de l'application avec Docker à la génération de certificats SSL avec Let's Encrypt. La configuration est facile, le déploiement est une commande en une ligne. Il y a à peine des inconvénients.

J'ai choisi AWS pour l'hébergement. Il a le grand avantage de proposer des services gratuits pendant 12 mois. Je dois admettre que j'ai eu du mal à configurer ma première instance EC2. Cependant, il y a de nombreux tutoriels sur le web et cela vaut la peine de se donner la peine initiale. De plus, je suis actuellement en train d'écrire [un package pour activer la sauvegarde quotidienne de la base de données MongoDB sur AWS S3](https://github.com/lbke/vulcan-mongo-backup) pour sécuriser vos données.

#### Une application de staging sur Now de Zeit + Mongolab

Tôt ou tard, vous devrez tester que votre application fonctionne en production, sans l'envoyer réellement en production. C'est ce que nous appelons un environnement de staging. Vous pouvez utiliser AWS aussi, mais essayons une solution gratuite pour réduire les coûts.

![Image](https://cdn-media-1.freecodecamp.org/images/duoWiDFwqKTIjBmUyBr31D2xZQFHst7jqdxG)
_Un toast à toutes les entreprises qui fournissent des services gratuits et contribuent à l'open source._

Le service Now de Zeit est bien adapté à cet usage. Il offre un hébergement gratuit. Vous pouvez utiliser mLab pour la base de données, car il fournit également un environnement sandbox gratuit. Pour être honnête, je n'ai pas grand-chose à dire ici, car la configuration est aussi facile que ABC, et entièrement [documentée ici](http://docs.vulcanjs.org/deployment.html#Meteor-Now). Pas même un bug. _Quel est mon but en tant que développeur s'il n'y a pas de bugs ???_

D'accord, donc, à la fin du jour 2, notre application est en production et nous avons un environnement de démonstration intermédiaire. Bien ! C'est cool, car **moins de temps pour les fonctionnalités génériques, c'est plus de temps pour les fonctionnalités précieuses.**

### Jour 3 : Logique métier

#### Une application est un ensemble de formulaires et de listes

Maintenant, passons aux choses sérieuses. La plupart des composants d'une application peuvent être séparés en 3 grandes catégories : Liste, Formulaire et Détails. Ce modèle s'applique à un GRAND nombre de sites web.

![Image](https://cdn-media-1.freecodecamp.org/images/KIACKwgfrO6zLnELdGZCLsIAJKvKSFVBxFuH)

Voir Medium : la page d'accueil contient une Liste d'articles. Cette page est une page « Détails » de l'article que vous lisez. En bas, vous trouverez une Liste de commentaires avec un formulaire de commentaire. Même le bouton « applaudissements » à gauche (que je vous invite à cliquer abondamment), est un composant de type Formulaire simpliste.

Bonne nouvelle : Vulcan inclut un grand nombre d'aides pour faciliter la création de composants Liste, Formulaire et Détails. Il inclut de beaux résolveurs GraphQL et des HOCs React. Vous avez à peine besoin d'écrire les vôtres. Il y a même quelques composants React qui fonctionnent prêts à l'emploi. Le plus avancé d'entre eux est le SmartForm, qui génère automatiquement un formulaire de création/modification personnalisable pour toute collection.

Je ne vais pas lister toutes les fonctionnalités que Vulcan.js a à offrir, mais en gros, vous pouvez lui faire confiance pour rendre votre processus de développement _vraiment_ rapide.

#### Créer une recette (ou proposer une application ou publier un article ou…)

Dans GestiResto, les 2 principales fonctionnalités sont la création et la liste des recettes. Le formulaire de création de recette doit afficher des statistiques. Les détails sont confidentiels, alors voici une capture d'écran d'un formulaire équivalent développé pour [Awesome Vulcan](https://www.awesome-vulcan.com).

Mais cela ne fait aucune différence, car voici le point : Vulcan peut auto-générer des formulaires prêts à l'emploi pour tout type de données que vous pouvez imaginer, qu'il s'agisse d'une recette ou d'un hélicoptère. Je veux dire, la représentation JSON d'un hélicoptère.

![Image](https://cdn-media-1.freecodecamp.org/images/Bbs1OzlDpIAL0mzR8G0PMsve7ipAJG-EB3wj)
_Ce formulaire a été auto-généré en utilisant le composant SmartForm de Vulcan. L'entrée « Liens » est un composant React personnalisé adapté à nos besoins spécifiques._

La liste des recettes est encore plus simple. Nous nous sommes concentrés sur la construction d'un bel élément `RecipeItem` qui permet aux utilisateurs de prévisualiser rapidement les informations de la recette, ainsi que de déclencher quelques actions courantes (exportation, suppression…). Bien sûr, il inclut une entrée de recherche basée sur du texte, gratuitement.

![Image](https://cdn-media-1.freecodecamp.org/images/muf7M03u5G1aYr6wk3DgJYSeQVi3rqj9PevF)
_Non, je ne vais jamais vous donner accès à la « Recette Secrète ». Sauf, peut-être, si vous applaudissez pour cet article._

![Image](https://cdn-media-1.freecodecamp.org/images/8cGzC3JcfzKn6jCsiNDOAuM4scQ1DvVwbqD6)

### Jour 4 : Livraison !

Puisque nous avons fait la plupart des parties précieuses du travail le Jour 3, il nous reste un dernier jour pour nettoyer et améliorer l'application. Maintenant, nous pouvons implémenter les fonctionnalités « aimables » : un composant qui calcule automatiquement le prix final de votre recette, un bouton qui génère une belle exportation PDF, et une page d'accueil qui fait la différence.

![Image](https://cdn-media-1.freecodecamp.org/images/7XlmaXGrLXotB4gP4mlKeSEonK2QXiRIMsx8)
_Regardez comme notre chef est heureux ! C'est parce que son application est construite sur des technologies 100% organiques et open-source._

Finalement, nous sommes au Jour 5. Le client vient de tester l'application livrée hier soir, et vous dit : « J'ai testé l'application, c'est bien ! Je pense à ajouter la fonctionnalité X à la page Y, combien de temps faut-il pour ajouter le composant Z à votre avis ?… ». **Et puis vous savez que vous avez fait du bon travail !**

### Vous voulez construire votre propre application en 4 jours ?

Jetez un coup d'œil à notre application open source [Awesome Vulcan](https://www.awesome-vulcan.com). Elle fournit une base réutilisable pour des applications professionnelles avec un look Material UI. Elle démontre également l'utilisation de quelques packages que nous avons implémentés.

**J'espère qu'elle vous aidera dans votre voyage vers l'application en 4 jours !**

<a href="https://twitter.com/LBKE_FR" target="_blank"><img src="https://cdn-media-1.freecodecamp.org/images/rxG0NpyqOMowC2nFVuSOHsg4pjJFkMs7w5bn"/></a>

Je suis le co-fondateur de l'entreprise française Lebrun Burel Knowledge Engineering (LBKE) — [https://www.lebrun-burel.com](https://www.lebrun-burel.com)

_Toujours heureux de parler de code, d'apprentissage automatique, d'innovation et d'entrepreneuriat !