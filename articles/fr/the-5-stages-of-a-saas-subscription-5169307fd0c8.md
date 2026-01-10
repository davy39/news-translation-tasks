---
title: Les 5 étapes d'un abonnement SaaS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-09T04:34:53.000Z'
originalURL: https://freecodecamp.org/news/the-5-stages-of-a-saas-subscription-5169307fd0c8
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9caeab740569d1a4caa809.jpg
tags:
- name: business
  slug: business
- name: Entrepreneurship
  slug: entrepreneurship
- name: SaaS
  slug: saas
- name: startup
  slug: startup
- name: technology
  slug: technology
seo_title: Les 5 étapes d'un abonnement SaaS
seo_desc: 'By Ben Sears

  This article will go into detail on what you need to automate in order for your
  SaaS company to have a functional subscription billing solution.

  One of the problems SaaS companies face when selling subscriptions is connecting
  their appli...'
---

Par Ben Sears

Cet article détaillera ce que vous devez automatiser pour que votre entreprise SaaS dispose d'une solution de facturation d'abonnement fonctionnelle.

L'un des problèmes auxquels les entreprises SaaS sont confrontées lors de la vente d'abonnements est la connexion de leur application à un processus de facturation.

Certaines des choses à considérer sont :

* Comment les annulations seront-elles gérées
* Les essais gratuits
* L'octroi de l'accès aux nouveaux clients

Le défi dans la gestion de ces processus de facturation est de gérer ces événements, tels que la restriction de l'accès à une application lorsque l'essai expire ou s'il n'y a plus de source de financement valide attachée à un compte.

### Le cycle de vie de l'abonnement SaaS

![Image](https://cdn-media-1.freecodecamp.org/images/cF991ZGku1qgcPHY5FM8NHUwPlKdt82s6gHW)

Le processus qu'un client suit lorsqu'il fait affaire avec une entreprise SaaS peut être décomposé en les cinq événements ci-dessus. La gestion de ces événements est la clé pour intégrer un système de facturation avec un SaaS.

#### S'abonner 🔍

Il s'agit de la première étape du parcours d'un utilisateur avec un abonnement. À cette étape, le client vient de s'inscrire à un abonnement qui doit déclencher un processus automatisé.

Le processus ressemble généralement à ceci :

1. Un client commande un abonnement pour votre application.
2. Le client obtient l'accès à votre application.
3. Après la période d'essai (s'il y a un essai gratuit), le client est facturé de manière récurrente.

D'un point de vue DevOps, ces opérations sont considérées comme des opérations « **Jour 1** ». Ce sont les étapes qu'un service suit après avoir été demandé pour être considéré comme « provisionné », telles que l'installation et les configurations de logiciels.

#### Période d'essai ⏳

Lors de la période d'essai, un client s'est abonné à un service, mais ne paie pas jusqu'à l'expiration de son essai.

![Image](https://cdn-media-1.freecodecamp.org/images/F66cqbVeMQcPsYUx-joezF35PYJQhBlejYVC)

Environ [75 % des entreprises SaaS](https://www.chargify.com/blog/increase-free-trial-conversions/) offrent des essais gratuits. Bien que les essais gratuits soient presque garantis de vous apporter plus de clients payants, l'une des choses les plus délicates à propos de leur offre est de décider ce qui se passe lorsque l'essai expire sans que le client n'ajoute une source de financement.

À ce stade du cycle de vie du service, une entreprise devra construire une logique autour des essais qui, à l'expiration, restreindra l'accès à une application et alertera le client qu'il doit payer.

#### Mise à niveau 🔝

![Image](https://cdn-media-1.freecodecamp.org/images/FG7TZ3qnJI9DdlGresF5gspwvM4L8D-V3eNH)
_Netflix offre différents niveaux_

De nombreuses entreprises SaaS prennent en charge plusieurs niveaux de service. Si un client paie un supplément, il a accès à des fonctionnalités supplémentaires. Cela est considéré comme une opération « **Jour 2** », des actions qui peuvent être entreprises après qu'un service a été provisionné et qui affectent l'utilisateur final.

Généralement, cela suit le modèle ci-dessous :

1. Un client soumet une demande de mise à niveau de son abonnement.
2. Le taux d'abonnement du client sera augmenté.
3. Le client aura accès à de nouvelles fonctionnalités au sein de l'application.

Bien que cela prenne généralement la forme de niveaux de prix stricts, parfois les clients paient « par utilisateur par mois » ou ont des « seuils » qui, s'ils sont dépassés, déclencheront des tarifs plus élevés.

#### Annulation ❌

Inévitablement, il y aura des annulations d'abonnements, également appelées [churning](http://chaotic-flow.com/saas-metrics-faqs-what-is-churn/). Les étapes qui se produisent pour effectuer une annulation sont les suivantes :

1. Un client demande l'annulation d'un abonnement SaaS.
2. Il ne sera plus facturé de manière récurrente.
3. L'accès à l'application prendra fin à la fin du cycle de facturation en cours.

Contacter vos anciens clients après leur annulation nécessitera également un certain processus. Il est recommandé que l'annulation déclenche un processus qui envoie un e-mail automatisé à l'ancien client, peut-être avec une tentative de récupérer le client ou une enquête de feedback pour voir quelles raisons ils auraient pu avoir pour annuler.

#### Réabonnement 🔄

Lorsque qu'un ancien client décide de revenir après avoir annulé, une entreprise ne peut pas simplement suivre le processus initial pour l'abonner comme un nouveau client — elle doit réactiver l'accès précédemment terminé afin qu'il conserve toutes ses anciennes données. Ce processus peut être décrit en trois étapes :

1. Un client se réabonne en ajoutant une source de financement valide à son compte.
2. L'accès au compte client et aux données est réactivé.
3. Le client sera facturé de manière récurrente une fois de plus.

Certains scénarios complexes peuvent inclure des codes de réduction à durée limitée pour les réabonnés, un essai gratuit, ou une partie d'un autre service dans le cadre d'une offre combinée.

### Conclusion

La clé pour vendre des logiciels en tant que service est de connecter le logiciel à un système de facturation capable de supporter le cycle de vie que je viens de décrire. Pouvoir automatiser ce processus est un atout pour les entreprises, car les processus manuels sont l'un des plus grands obstacles à la croissance.

Vous essayez de gérer les défis de la facturation SaaS ? [Parlons-en](https://servicebot.io/contact).

Nous résolvons les défis auxquels les entreprises SaaS sont confrontées lors de la facturation des clients en fournissant des hooks faciles à intégrer qui peuvent déclencher des processus automatisés.