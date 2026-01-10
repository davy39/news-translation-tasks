---
title: Les API Web expliquées par la vente de produits de votre ferme
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-27T04:46:11.000Z'
originalURL: https://freecodecamp.org/news/web-apis-explained-by-selling-goods-from-your-farm-84aaf99cfc78
coverImage: https://cdn-media-1.freecodecamp.org/images/1*iYNkAqKLBM9qw2j1TdO6SA.jpeg
tags:
- name: api
  slug: api
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Les API Web expliquées par la vente de produits de votre ferme
seo_desc: 'By Kevin Kononenko

  If you have been to a farmer’s market or farm stand, then you can understand the
  concept of an application programming interface (API).

  If you are new to web development, you probably hear the term “API” a lot.

  “I can’t wait until ...'
---

Par Kevin Kononenko

**Si vous êtes déjà allé à un marché fermier ou à un stand de ferme, alors vous pouvez comprendre le concept d'une interface de programmation d'applications (API).**

Si vous êtes nouveau dans le développement web, vous entendez probablement souvent le terme « API ».

_« Je n'ai hâte que cette entreprise publie leur API publique ! »_

_« L'API de cette entreprise est un vrai fouillis. »_

_« Ont-ils un endpoint pour ces données dans leur API ? »_

Comprendre le concept d'une interface de programmation d'applications (API) peut être assez difficile si vous n'êtes pas familier avec des concepts comme SOAP, HTTP et XML.

Alors, j'ai voulu trouver un moyen d'expliquer le fonctionnement des API web dans leur ensemble, afin que lorsque vous entrerez dans les détails techniques, vous compreniez comment tout cela s'articule.

Dans ce tutoriel, vous êtes le propriétaire d'une ferme qui vend cinq produits : du poulet, du porc, des œufs, des tomates et du maïs.

![Image](https://cdn-media-1.freecodecamp.org/images/0*JS5g1_gRC72cQhQA.)

Pour comprendre ce tutoriel, vous devez simplement comprendre la différence entre le code côté serveur (back-end) et le code côté client (front-end). Vous pouvez lire le début de mon [guide sur GET/POST](https://blog.codeanalogies.com/2018/01/15/ajax-basics-explained-by-working-at-a-fast-food-restaurant/) si vous n'êtes pas déjà familier avec la différence entre serveur et client.

### La différence entre une GUI et une API

Commençons par une manière familière d'utiliser le web. Le navigateur web, comme Chrome, est un exemple d'interface graphique (GUI). En tant qu'utilisateur, vous pouvez interagir avec un outil convivial pour accomplir des tâches, comme réserver des vols ou rechercher sur Google.

La GUI permet aux visiteurs d'un site web d'interagir avec le code du serveur de manière contrôlée et structurée.

En tant que propriétaire de ferme, cela ressemble un peu au stand que vous installez sur votre propriété ou à votre étal au marché fermier.

![Image](https://cdn-media-1.freecodecamp.org/images/0*uI8OpnP5gTeq9XLB.)

Vous ne pouvez pas simplement empiler vos produits dans votre grange, permettre aux visiteurs d'entrer et espérer faire des bénéfices. Au lieu de cela, vous devez installer un stand pour que les visiteurs puissent rapidement comprendre vos produits disponibles et leurs prix.

C'est ainsi que les clients « interagissent » avec votre travail. Ils n'ont pas besoin de comprendre le processus de plantation, ou l'équipement que vous utilisez, ou la transformation. Ils voient simplement le produit final.

![Image](https://cdn-media-1.freecodecamp.org/images/0*1CKu4-YZRsxGAB09.)

Remarquez comment chaque client vit une interaction en un-à-un. Lorsqu'ils arrivent à votre étal, ils ne regardent que les produits de votre ferme.

### Alors, qu'est-ce qu'une API ?

Il existe d'autres moyens de vendre vos produits que directement aux consommateurs. Vous pouvez également vendre à des distributeurs et à des restaurants locaux, afin que vos produits puissent être inclus dans différents plats ou vendus dans une épicerie.

C'est une nouvelle manière pour les consommateurs de « découvrir » votre produit. Bien sûr, ils ne savent peut-être pas dont proviennent les œufs dans leur omelette lorsqu'ils commandent un petit-déjeuner dans le diner local, mais ils « utilisent » toujours votre produit.

Mais, du point de vue du propriétaire de la ferme, vous avez un processus de vente et une chaîne d'approvisionnement complètement différents. Maintenant, vous n'avez plus besoin de disposer soigneusement un stand pour les consommateurs. Au lieu de cela, vous devez probablement ajouter une baie de chargement à votre grange afin que les distributeurs et les restaurants puissent garer leurs camions et charger les produits. Vous devez également emballer vos produits pour des ventes en gros.

![Image](https://cdn-media-1.freecodecamp.org/images/0*9KQ-8Us5U8PvR90e.)

Cela est similaire au concept d'une API. Lorsque vous créez une API, vous permettez à d'autres développeurs d'accéder à vos données et de les utiliser dans leurs applications.

Tout comme les clients d'un restaurant peuvent « découvrir » les œufs de vos poules en mangeant une omelette, les utilisateurs d'un site web peuvent « découvrir » votre produit sur le site de quelqu'un d'autre via un widget sur le site ou du code sur les serveurs de l'autre entreprise.

Maintenant, nous avons un nouveau niveau d'interaction. Vos distributeurs et clients de restaurants peuvent interagir avec vous en un-à-un en visitant la ferme, mais ils exposent ensuite des milliers de clients à vos produits lorsqu'ils les vendent plus tard.

En tant que propriétaire de ferme, vous devez toujours mettre en place des processus pour pouvoir servir ces distributeurs avec succès. De même, une API est une manière structurée pour que d'autres puissent utiliser votre code côté serveur. En tant que développeur, vous avez toujours le contrôle total.

J'ai utilisé un widget de recherche comme exemple dans l'image ci-dessus, mais en réalité, presque n'importe quoi pourrait être utilisé pour accéder à une API. Ce n'est qu'un exemple d'une manière courante pour les utilisateurs de sites web de découvrir les API de tiers. D'autres exemples courants incluent :

* Outils de cartographie
* Traitement des paiements
* Données météorologiques

### Qu'est-ce qui peut être accessible via une API ?

Supposons que vous souhaitiez commencer à vendre des œufs de votre ferme à des distributeurs et à des restaurants. Vous devriez mettre en place une série de processus sur votre ferme pour soutenir cela :

1. Stockage de masse des œufs
2. Comptabilité pour la facturation mensuelle des clients
3. Une zone de chargement pour charger les œufs sur les camions.

Avant de mettre en place tous ces processus, vous devez décider si vous êtes prêt à accepter des commandes de masse d'œufs en premier lieu. Avez-vous assez de poules pour produire le bon nombre d'œufs sur une base hebdomadaire ? Si ce n'est pas le cas, vous pourriez mettre trop de pression sur votre système et décevoir vos clients lorsque vous serez à court d'œufs.

Les développeurs d'API mettent en place des **endpoints** qui permettent à d'autres développeurs d'accéder à des données spécifiques de leur base de données. L'exemple ci-dessus serait un endpoint « œufs ». Si vous n'en créez pas en premier lieu, alors les clients ne peuvent pas acheter d'œufs de vous.

Vous pouvez mettre en place des endpoints spécifiques pour chaque produit de votre ferme : poulet, porc, œufs, tomates et maïs. Certains peuvent être accessibles uniquement via le marché fermier (GUI) parce que vous n'êtes pas sûr d'être prêt à augmenter la production pour répondre aux besoins des distributeurs.

![Image](https://cdn-media-1.freecodecamp.org/images/0*gtKR8rDGBgGewhIr.)

C'est une différence entre une API et une base de données open-source. Dans une base de données open-source, tout peut être interrogé et accessible. Lorsque vous mettez en place une API pour votre back-end, vous créez des endpoints qui révèlent uniquement des données spécifiques.

Tout comme les distributeurs sont ceux qui peuvent maintenant interagir avec votre ferme, les développeurs d'autres entreprises sont ceux qui interagissent avec votre API. Une fois qu'ils écrivent du code qui accède aux données de votre serveur, les visiteurs de leur site web peuvent avoir de nouvelles expériences basées sur vos données.

### Suivi d'un appel API individuel

Supposons que vous avez décidé de mettre en place un **endpoint** pour les œufs à votre ferme. Un restaurant local souhaite acheter 1000 œufs pour satisfaire les 1000 commandes d'omelettes qu'il reçoit chaque semaine.

![Image](https://cdn-media-1.freecodecamp.org/images/0*c2DAEyegIUTrwM_W.)

Remarquez comment notre **appel API** commence en réalité par une demande utilisateur ? Cela peut sembler un peu contre-intuitif d'après la description.

Un **appel API** individuel se produit lorsqu'un déclencheur se produit, et que le code écrit par un autre développeur envoie une **requête** à votre API à un **endpoint** spécifique. Votre API doit fournir une réponse basée sur votre code côté serveur.

Dans ce cas, le déclencheur est la commande de 1000 œufs. Le gérant du restaurant a déjà établi une relation avec une ferme — votre ferme. Et votre ferme a déjà mis en place les processus pour livrer 1000 œufs à la fois.

Ainsi, la commande de 1000 œufs arrive, et votre ferme livre la réponse : 1000 œufs.

Gardez à l'esprit qu'il pourrait y avoir 100 autres restaurants qui ont établi une relation avec votre ferme, et que 10 d'entre eux pourraient envoyer une **requête** en même temps ! C'est là que la scalabilité entre en jeu. Vous devez décider si votre serveur est prêt à gérer cette demande. Mais c'est un sujet pour un autre tutoriel !

![Image](https://cdn-media-1.freecodecamp.org/images/0*4QZDXA5t95N7vboE.)

Voici la version technique de la séquence ci-dessus, si vous aviez une application de cartographie qui pourrait être utilisée sur d'autres sites web comme Google Maps.

![Image](https://cdn-media-1.freecodecamp.org/images/0*SkAzRcrC2zXcNLy9.)

1. Un utilisateur sur un autre site utilise votre application de cartographie et effectue une action qui nécessite des données de votre serveur.
2. Le développeur sur cet autre site a déjà écrit le code qui créera une **requête** à votre API en fonction de l'action de cet utilisateur.
3. L'**appel API** arrive, et votre serveur fournit une **réponse**.

Bien sûr, il y a probablement 1000 autres applications web qui utilisent votre widget de cartographie, donc vous devez être préparé pour tous ces appels API !

![Image](https://cdn-media-1.freecodecamp.org/images/0*0wWqB2oCcd7-WNuO.)

### Exemples de GET et POST

Voici un [rappel rapide sur GET et POST](https://blog.codeanalogies.com/2018/01/15/ajax-basics-explained-by-working-at-a-fast-food-restaurant/) si vous avez besoin de vous rafraîchir la mémoire.

Jusqu'à présent, dans nos exemples de ferme, les requêtes dans notre petit scénario ont ressemblé à des requêtes GET. En raison des requêtes déclenchées par les clients du restaurant, le restaurant doit envoyer un camion à votre ferme pour récupérer des œufs.

Mais qu'en est-il des requêtes POST ? Dans un exemple réel, l'API Facebook permet aux utilisateurs d'autres applications de créer des publications, et cette application peut ensuite envoyer ces publications directement à Facebook pour qu'elles soient publiées immédiatement.

Dans certains cas, comme les API de réseaux sociaux, il peut être logique de permettre à l'utilisateur final de publier directement sur une plateforme sociale depuis une application tierce.

Mais voici un autre exemple. L'API Amazon permet aux propriétaires de boutiques en ligne de publier leurs produits de manière programmatique sur le Marketplace d'Amazon. Dans cette situation, le développeur de l'équipe du propriétaire de la boutique en ligne indépendante peut également créer une présence sur Amazon. Ainsi, l'API n'implique aucun type d'utilisateur final ou de visiteur de site web.

Dans notre exemple de ferme, cela ressemble un peu à la manière dont vous pourriez gérer la facturation mensuelle. Après que les restaurants et les distributeurs ont visité votre ferme tout au long du mois pour acheter des produits, vous leur envoyez une facture à la fin du mois qui détaille le paiement qu'ils doivent envoyer.

Tout comme le restaurant doit mettre en place ses propres processus pour s'assurer qu'il collecte les œufs au bon moment, il doit également avoir un processus pour vous payer à temps. Cela implique probablement leur comptable. Supposons que le comptable sache qu'il doit vous payer le premier du mois.

![Image](https://cdn-media-1.freecodecamp.org/images/0*2OLXd7qM5P3DMsaI.)

Maintenant, comment l'utilisateur/client pourrait-il déclencher une requête POST ? Eh bien, imaginez que le restaurant vous envoie immédiatement un paiement chaque fois que quelqu'un commande de la nourriture provenant de votre ferme. Si une personne commandait une omelette à 5 $, et que 2 $ du coût provenaient des œufs de votre ferme, le restaurant vous enverrait immédiatement les 2 $ sur votre compte bancaire. Si cela était une application web, ce niveau de communication pourrait fonctionner, mais comme il s'agit d'un exemple de ferme, cela serait un peu impraticable.

![Image](https://cdn-media-1.freecodecamp.org/images/0*6KCimIOx44uBhIYm.)

### La différence entre une ferme et une application web

Comme vous pouvez commencer à le voir dans le dernier exemple, il y a une différence majeure entre notre petite chaîne d'approvisionnement de ferme et un appel API. Le timing.

Simplement en raison de la logistique du monde réel… nous ne pouvons pas espérer égaler la nature instantanée de la plupart des appels API, même si les étapes sont généralement les mêmes.

Revenons à l'exemple de la requête GET plus tôt dans le tutoriel.

![Image](https://cdn-media-1.freecodecamp.org/images/0*Ln76YuGduAcDlTqg.)

Voici ce que cela signifie en termes de développement web.

1. L'utilisateur effectue une action qui déclenche une requête
2. Le code côté serveur effectue un appel API à un endpoint
3. L'API fournit des informations spécifiques

Mais si nous établissons l'analogie avec une ferme réelle :

1. L'utilisateur commande une omelette
2. Le restaurant envoie un camion pour récupérer des œufs à votre ferme.
3. Les œufs sont livrés au restaurant et servis dans l'omelette

Il serait incroyablement impraticable d'envoyer un camion à une ferme pour faire l'omelette la plus fraîche connue de l'humanité. Mais les étapes restent les mêmes. Je voulais simplement mentionner cette différence de timing.

Mais, lorsqu'un utilisateur déclenche une requête lorsqu'il utilise une application web, il obtient généralement une réponse presque instantanée.

### Que signifie « ouvrir votre API » ?

Alors, revenons à notre question initiale : Que signifie-t-il lorsqu'une entreprise « ouvre son API » ?

Cela signifie qu'ils ont des données précieuses disponibles sur leur serveur qu'ils peuvent maintenant révéler via des **endpoints** spécifiques. L'entreprise détermine comment les développeurs d'autres entreprises peuvent accéder à leurs données, mais en même temps, ils les rendent largement disponibles de manière structurée.

Dans notre analogie de la ferme, c'est le moment où votre ferme décide de vendre vos produits à des distributeurs et à des restaurants, et met en place les systèmes internes pour gérer les commandes en masse.

### Avez-vous aimé ce tutoriel ?

Si vous avez aimé ce tutoriel, vous aimerez probablement le reste de mes guides visualisés sur les sujets de développement web. Lisez la suite sur le [blog CodeAnalogies](https://codeanalogies.com/), ou inscrivez-vous ici pour recevoir les derniers tutoriels :