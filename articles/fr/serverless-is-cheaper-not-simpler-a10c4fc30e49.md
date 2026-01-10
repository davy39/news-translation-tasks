---
title: Serverless est moins cher, mais pas plus simple
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-28T14:16:15.000Z'
originalURL: https://freecodecamp.org/news/serverless-is-cheaper-not-simpler-a10c4fc30e49
coverImage: https://cdn-media-1.freecodecamp.org/images/0*jIpMoYfpftPWmx-x.
tags:
- name: Devops
  slug: devops
- name: General Programming
  slug: programming
- name: serverless
  slug: serverless
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Serverless est moins cher, mais pas plus simple
seo_desc: 'By Dmitri Zimine

  The (Emit) conference last week featured a lineup of excellent talks, an engaging
  panel discussion, and plenty of time to meet and exchange notes with the awesome
  fellows of the serverless community.

  Cost is unanimously cited as the ...'
---

Par Dmitri Zimine

La conférence [(Emit)](http://www.emitconference.com) de la semaine dernière a présenté une série d'excellentes présentations, une discussion de panel engageante et beaucoup de temps pour rencontrer et échanger des notes avec les membres formidables de la communauté serverless.

Le **coût** est unanimement cité comme le principal moteur de l'adoption du serverless. L'exécution à la demande et l'élasticité intégrée optimisent l'utilisation tout en maintenant un temps de fonctionnement et une fiabilité encore plus élevés. La facturation à l'usage rend le coût directement quantifiable. Les [économies](https://techbeacon.com/economics-serverless-computing-real-world-test) peuvent être [considérables](https://aws.amazon.com/solutions/case-studies/bustle/). [Anne Thomas](https://twitter.com/AnneWoof), analyste chez Gartner, a partagé lors de la discussion du panel que ses clients entreprises sont attirés par le serverless en raison des avantages de "coût".

Mais il n'y a pas de repas gratuit dans un système fermé : pour obtenir un avantage, quelque chose doit être sacrifié. En technologie, la monnaie la plus courante pour payer les avantages est la "complexité".

Lorsque les microservices ont remplacé les monolithes pour obtenir l'avantage de l'échelle de manière fiable sous une charge massive, [ce n'était pas un repas gratuit](http://highscalability.com/blog/2014/4/8/microservices-not-a-free-lunch.html). Traiter avec la cohérence éventuelle, gérer l'asynchronicité, la latence et la tolérance aux pannes, gérer les API et les schémas de messages, l'équilibrage de charge, exécuter des mises à jour continues — nous avons payé avec une grande quantité de complexité supplémentaire [pour les gains](https://martinfowler.com/articles/microservice-trade-offs.html).

Où réside la complexité et comment la gérons-nous ?

![Image](https://cdn-media-1.freecodecamp.org/images/BJh1QzI1yaU2Lht08lp4D93gXDNS6LQxPn3j)
_De monolithe à microservices à serverless, la complexité augmente pour obtenir des avantages._

Regardez l'image. Les blocs orange représentent le code. Lorsque nous passons aux microservices puis au serverless, les blocs individuels de code deviennent plus petits et plus simples, tandis que la complexité totale augmente. Une grande partie de cette complexité supplémentaire est du "câblage" : configurations, scripts de déploiement, artefacts d'outils DevOps — modèles, recettes, playbooks, dockerfiles... Tout ce qui est utilisé pour déployer la solution dans le cloud et la maintenir là-bas. La partie grise entre les blocs de code orange. Cela me rappelle une vieille blague russe :

> - De quoi est fait l'air ?  
> - Eh bien, il est fait de molécules !  
> - Et qu'y a-t-il entre les molécules ?  
> - Eh bien, de l'air, bien sûr !

Ce câblage entre le code : il vaut mieux que ce soit du code ! Et c'est ce que DevOps était tout à fait avec son mantra "Infrastructure as code". DevOps — pour donner une autre définition — est un framework et des outils pour dompter la complexité supplémentaire du câblage introduite par les microservices.

Lorsque le serverless remplace les microservices, ce ne sera pas non plus un repas gratuit. Nous payons en introduisant plus de complexité, maintenant pour le bénéfice d'économies de coûts massives.

Certaines parties du système serverless deviennent plus simples. Ne pas avoir à gérer les machines virtuelles, le réseau, le stockage et les systèmes d'exploitation est un soulagement énorme par rapport au fardeau opérationnel massif de la provision, de la configuration, de la surveillance et de la remédiation de l'infrastructure. Les fonctions fournissent un modèle de programmation simple et se concentrent principalement sur la logique métier. L'environnement d'exécution est restreint, contrôlé et sous "rayons X continus". [Chris Anderson](https://twitter.com/crandycodes), chef de produit pour [@AzureFunctions](https://twitter.com/AzureFunctions), a souligné à quel point il est devenu plus facile de localiser les problèmes avec les exécutions de fonctions.

Mais la loi de conservation s'applique toujours, et lorsque les fonctions sont simplifiées, la complexité libérée se déplace ailleurs. Où va la complexité et comment la gérons-nous ?

Une partie de la complexité est déléguée aux services cloud PaaS (puis-je l'appeler JPaaS ? [3]). AWS API Gateway, S3, Kinesis, SNS, DynamoDB, StepFunctions, ou leurs homologues Azure et GCP — sont en jeu avec toute solution serverless. Ils sont prêts à l'emploi, entièrement gérés, riches en fonctionnalités, "infini" scalable, et pay-per-use. Pour obtenir leurs avantages, nous échangeons volontiers le contrôle — une autre monnaie technologique courante — pour être libérés des préoccupations d'infrastructure et de boilerplate. Notez le retour des microservices "Smart endpoints and dumb pipes" [](https://martinfowler.com/articles/microservices.html#SmartEndpointsAndDumbPipes) vers "dumb endpoints and smart pipes" et même les workflows ; prenez une minute pour réfléchir à ce balancement du pendule.

Parfois, l'abandon du contrôle se retourne contre nous et la complexité augmente de manière inattendue là où les choses étaient simples. La configuration des en-têtes binaires dans AWS API Gateway via des modèles CloudFormation vous fait regretter la clarté de la gestion dans le code de votre microservice. L'utilisation de services JPaaS riches en fonctionnalités nécessite une expertise approfondie, et contrairement à la programmation régulière et à l'informatique, cette expertise ne se traduit pas entre les plateformes : connaître DymanoDB sera d'une aide minime pour apprendre BigTable.

Néanmoins, la délégation à JPaaS est un net positif et couvre une bonne partie de la complexité. Mais pas toute. L'autre partie de la complexité réside, encore une fois, dans le "câblage".

Les fonctions sont plus petites, mais il y a un ordre de grandeur de plus de relations à comprendre et de dépendances à gérer. Les fonctions sont plus simples, mais elles ne contiennent plus le flux logique. La logique et le flux de la solution de bout en bout sont pilotés par des événements. Ils ne résident plus dans aucun artefact de codage et deviennent très difficiles à raisonner.

Comment cette facette de la complexité est-elle gérée aujourd'hui ? Pas très bien. Cela nécessite des uber-architectes pour la garder sous contrôle. Les processus et les outils doivent encore rattraper leur retard. Les frameworks serverless poussent comme des champignons après la pluie, mais sont principalement bloqués avec FaaS — avec de légères variations sur le même thème, un problème déjà résolu. Même le framework 'serverless' le plus avancé, et celui qui reconnaît que Serverless est plus que FaaS, et fournit des plugins et une prise en charge native des ressources pour d'autres services — même 'serverless' ne couvre pas la complexité de câblage de bout en bout d'une solution serverless. Prenez le projet serverless canonique [HelloRetail](https://read.acloud.guru/serverless-event-sourcing-at-nordstrom-ea69bd8fb7cc) et inspectez combien de complexité est laissée de côté. Le "projet", les dépendances des services sur JPaaS et les uns sur les autres, l'ordre de déploiement, les types d'événements et les schémas et bien plus encore ne sont pas couverts par le framework. Ils sont partiellement scriptés, partiellement documentés, mais résident principalement dans la tête des "uber-architectes" ou en tant que connaissance tribale (qui, en logiciel, est également connue sous le nom de "connaissance de problème").

![Image](https://cdn-media-1.freecodecamp.org/images/vD7SM2g-YJc2Ci-f9FjLE8FNYEAk4VD3yosM)

Et DevOps ? Ne devrait-il pas aider ? La réponse est NON, ou du moins, pas entièrement. Pour une chose, les gens de DevOps ne se pressent pas autour du serverless presque autant qu'autour de kubernetes. Pourquoi donc ? Peut-être que nos amis DevOps, personnes créatives, n'ont tout simplement pas assez de boutons et de leviers d'infrastructure à bidouiller ? Ou peut-être que la raison est plus fondamentale : DevOps est une réponse à un autre espace de problèmes — les microservices — et n'est pas entièrement applicable au serverless car de nombreuses hypothèses des microservices ne tiennent plus. Retirer "ssh to the box" seul retire la moitié des outils DevOps. Même Terraform, construit pour codifier les infrastructures cloud, n'est somehow pas près d'être aussi favorisé dans la communauté Serverless qu'il l'est dans DevOps des microservices.

En conséquence, le serverless manque aujourd'hui des frameworks opérationnels établis, des modèles et des outils nécessaires pour dompter sa complexité. Il nécessite un uber-architecte pour inventer la solution de bout en bout et dompter la complexité. Ces uber-architectes tracent la voie et montrent le succès et aident les modèles à émerger. Mais comme Anne de Gartner l'a souligné lors du panel de la conférence (Emit), il n'y aura pas d'adoption généralisée du serverless tant que les frameworks et les outils ne rattraperont pas leur retard.

Comme de nombreuses fois auparavant, le défi est une opportunité. DevOps est venu dompter la complexité des microservices et a rendu les applications cloud "possibles". Quelque chose arrive pour dompter la complexité du serverless et rendre les applications cloud "économiques". Quoi que ce soit, cela va être grand. Lorsque cela concerne $, les forces économiques fonctionnent sans faille. Les avantages d'économie de coûts du serverless sont si clairs et si substantiels, et la poussée de tous les principaux fournisseurs de cloud vers le serverless est si forte, qu'il ne faudra pas longtemps avant que la complexité ne soit domptée et que le serverless devienne mainstream dans tous les domaines où il s'applique.

Merci d'avoir lu. Veuillez partager vos commentaires et vos réflexions sur l'avenir du serverless ici et sur Twitter. Et si vous avez aimé lire ceci et souhaitez que j'écrive plus d'articles comme celui-ci, il suffit de cliquer sur le bouton "clap".

PS. Vous pourriez être intéressé par [la discussion Hackernews et les commentaires sur cet article](https://news.ycombinator.com/item?id=15326553).