---
title: Comment j'ai construit une startup Serverless
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-06-20T15:18:36.000Z'
originalURL: https://freecodecamp.org/news/how-i-built-a-serverless-startup-387fc6f61064
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5vxLWV8PDC7ghDGqqPijCA.jpeg
tags:
- name: General Programming
  slug: programming
- name: serverless
  slug: serverless
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment j'ai construit une startup Serverless
seo_desc: 'By Vikram Rangnekar

  Let me cut right to it, Serverless is a buzzword. But it’s also a great way to refer
  to a massive change in how we build software. Yes, there are still servers involved,
  we haven’t gotten rid of those. The difference is that you d...'
---

Par Vikram Rangnekar

Permettez-moi d'aller droit au but, Serverless est un mot à la mode. Mais c'est aussi une excellente façon de désigner un changement massif dans la manière dont nous construisons des logiciels. Oui, il y a encore des serveurs impliqués, nous ne nous en sommes pas débarrassés. La différence est que vous ne vous en souciez pas. Serverless consiste à se concentrer sur votre code et non sur l'infrastructure sur laquelle il s'exécute. Vous louez juste assez de puissance de calcul pour faire votre travail lorsque vous en avez besoin.

> Le calcul Serverless est la capacité d'appeler depuis un vaste pool de ressources. Louez la bonne quantité de ressources pour faire votre travail au moment où vous en avez besoin. Et rendez-les dès que vous avez terminé.

J'ai découvert le calcul Serverless en 2008, lorsque Google a lancé un produit appelé App Engine. Nous avions des difficultés avec l'infrastructure de notre startup et App Engine semblait intéressant. Nous avons fini par construire notre produit entier "Socialwok" sur celui-ci. C'est alors que j'ai réalisé pour la première fois à quel point il est avantageux de construire des produits en utilisant la technologie Serverless.

Les choses ont bien évolué depuis et nous entrons dans un avenir Serverless. Ne pas avoir à se soucier de la gestion de l'infrastructure aide à avancer plus vite et à être plus créatif. J'étais si convaincu de cela que j'ai écrit un livre entier pour prêcher la puissance de l'infrastructure gérée.

[https://www.amazon.com/How-Build-Future-powered-software-ebook/dp/B01N580GJQ](https://www.amazon.com/How-Build-Future-powered-software-ebook/dp/B01N580GJQ)

Pour aller plus loin avec cette idée, j'ai décidé de construire une startup Serverless. Un produit qui consomme très peu de ressources et qui peut être mis à l'échelle pour des millions d'utilisateurs si nécessaire. En optant pour le Serverless, il y a quelques options parmi lesquelles choisir. Amazon Lambda et Google Firebase plus Cloud Functions sont les deux options populaires. J'ai choisi de travailler avec Google car je suis plus familier avec leur technologie.

Le produit que j'ai construit [Bell+Cat](https://bellpluscat.com/) est un outil pour vous aider à vous organiser. Pensez-y comme une feuille de calcul plus simple. Je voulais garder ce produit gratuit et accessible à tous. Si un million de personnes décidaient de l'utiliser, cela me coûterait très peu pour les servir.

Pour réaliser cela, j'ai décidé d'utiliser Google Drive pour stocker les données des utilisateurs. Il est sécurisé, fiable et conforme à toutes les exigences que les gens peuvent avoir. De plus, c'est rassurant de savoir que vos données sont quelque part de familier. Google Drive offre à chacun 15 Go de stockage gratuit, donc [Bell+Cat](https://bellpluscat.com/) est un excellent moyen d'en tirer plus parti. Je voulais garantir un niveau de sécurité très élevé. Pour y parvenir, je l'ai conçu de telle sorte que vos données ne circulent qu'entre Google Drive et votre navigateur. Et elles sont chiffrées en permanence. Cela les rend beaucoup plus sécurisées et je n'ai pas à m'inquiéter de stocker des informations sensibles des utilisateurs.

Pour héberger l'application, j'ai choisi Google Firebase Hosting. Un produit assez génial qui utilise les réseaux CDN de Google pour servir l'application à quiconque dans le monde de la manière la plus rapide possible. J'adore le fait qu'il suffit d'une commande "firebase deploy" pour lancer une nouvelle version de [Bell+Cat](https://bellpluscat.com/) en quelques secondes. Il y a très peu d'autres choses que j'ai dû faire.

Dès que l'application a commencé à gagner des utilisateurs, j'ai commencé à recevoir des demandes de fonctionnalités. L'une des demandes les plus populaires était un moyen de partager le fichier [Bell+Cat](https://bellpluscat.com/) avec d'autres ou de l'intégrer sur leur propre site web. Cette fonctionnalité nécessitait que je gère certains calculs backend. De manière traditionnelle, cela aurait nécessité que je fasse fonctionner un serveur, mais dans ce cas, j'ai utilisé Cloud Functions. Il s'agit d'une véritable infrastructure Serverless et elle est bien intégrée à Firebase. Cloud Functions permet l'exécution de petits extraits de code. Ce déclencheur peut être n'importe quel événement comme une requête du navigateur. Et vous n'êtes facturé que de minuscules fractions de centime pour chaque exécution. Cela revient à environ 40 centimes pour un million d'exécutions. Il est important de se rappeler qu'il n'y a pas de serveurs à gérer ici, pas même des serveurs virtuels.

Toute personne construisant des logiciels est familière avec le processus de décomposition d'un problème plus grand en petites parties. Avec Cloud Functions, chaque partie ne s'exécute que lorsqu'elle est déclenchée et vous ne payez que lorsqu'elle le fait. J'aimerais penser que Serverless nous aidera à utiliser nos ressources informatiques de manière plus efficace. Et nous aurons besoin de moins de serveurs que nous n'en aurions eu. Avec la technologie prenant le dessus sur tout, avoir besoin de moins de serveurs devrait être bénéfique pour l'environnement à long terme. Penser Serverless nous aide à construire de meilleurs produits avec des équipes plus petites. Snapchat, qui fonctionne sur Google App Engine. Ils ont parlé de la manière dont ils n'ont personne pour gérer les serveurs au sein de leur équipe. Cela est très inhabituel pour des produits de leur envergure.

> "Si j'ai vu plus loin, c'est seulement en me tenant sur les épaules de géants."
> — Isaac Newton

Faire de bons choix technologiques peut aider votre idée de tant de manières. Comme dans le cas de [Bell+Cat](https://bellpluscat.com/), cela m'a permis de garder le produit gratuit et accessible à quiconque en a besoin. Cela a également permis à un seul développeur de continuer à se concentrer sur le produit principal et d'être très productif. Opter pour le Serverless sur le Google Cloud offre tant de choses gratuitement à [Bell+Cat](https://bellpluscat.com/). Les réseaux les plus rapides de la planète, un niveau de sécurité très élevé, une infrastructure informatique sophistiquée gérée par beaucoup de personnes très intelligentes. Et pour moi, l'avantage le plus important de tous, alors que je termine cet article et vais me coucher, quelqu'un d'autre veillera à ce que mon code continue de fonctionner.

[**Bell+Cat - Un organisateur simple dans votre navigateur**](https://bellpluscat.com/)
[_Un outil simple et gratuit pour vous organiser. Enregistre dans Google Drive. Sécurisé et privé. Utilisez des modèles ou importez depuis un..._bellpluscat.com](https://bellpluscat.com/)