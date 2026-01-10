---
title: 'Systèmes distribués : Quand les construire et comment les mettre à l''échelle.
  Un guide étape par étape.'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-29T21:58:25.000Z'
originalURL: https://freecodecamp.org/news/distributed-systems-when-you-should-build-them-and-how-to-scale-a-step-by-step-guide-37e76a177218
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0XtRXxr63Wjc2m0KvT-1Ng.jpeg
tags:
- name: AWS
  slug: aws
- name: Cloud Computing
  slug: cloud-computing
- name: General Programming
  slug: programming
- name: software architecture
  slug: software-architecture
- name: technology
  slug: technology
seo_title: 'Systèmes distribués : Quand les construire et comment les mettre à l''échelle.
  Un guide étape par étape.'
seo_desc: 'By Emmanuel Marboeuf

  It always strikes me how many junior developers are suffering from impostor syndrome
  when they began creating their product.

  I get it, there are many mind-blowing examples of top companies with incredibly
  complex distributed syst...'
---

Par Emmanuel Marboeuf

Il me frappe toujours de voir combien de développeurs juniors souffrent du **syndrome de l'imposteur** lorsqu'ils commencent à créer leur produit.

Je comprends, il y a de nombreux exemples **époustouflants** de **grandes entreprises** avec des systèmes distribués incroyablement complexes capables de gérer **des milliards de requêtes**, de mettre à jour gracieusement des centaines d'applications sans temps d'arrêt, de se rétablir d'une catastrophe en quelques secondes, de publier toutes les 60 minutes, et d'avoir des temps de réponse fulgurants depuis n'importe où dans le monde.

Ces attentes peuvent être assez **accablantes** lorsque vous commencez votre projet. Mais comme beaucoup d'entre vous le savent déjà, une majorité de ces entreprises ont commencé avec un **système viable minimal** et une **technologie très pauvre**. Il y a une raison simple à cela : elles **n'en avaient pas besoin** lorsqu'elles ont commencé. Passer plus de temps à concevoir votre système au lieu de coder pourrait en fait vous faire **échouer**.

Cet article est un guide **pas à pas**. Je vais vous montrer comment, chez Visage, nous avons commencé avec le système le plus minuscule jamais créé et construit un système distribué scalable de haute disponibilité de base. Il s'agit d'une véritable **étude de cas** pour **éliminer** vos **complexes** si vous n'avez jamais eu l'opportunité de le faire vous-même.

Lorsque je suis arrivé pour la première fois chez [Visage](https://www.visage.jobs) en tant que CTO, j'étais le seul ingénieur. Je ne connaissais rien de la stack technique, mais j'ai rejoint l'entreprise parce que j'aimais vraiment l'idée de pouvoir **recruter** **sans** recruteurs internes ou un service RH. C'était l'idée centrale derrière Visage : le **crowdsourcing** alimenté par un grand nombre de recruteurs invisibles travaillant ensemble sur vos rôles, assistés par une **intelligence artificielle** qui rechercherait les talents les plus adaptés pour vous en quelques jours. Ensuite, vous entrez directement en contact avec eux, sans intermédiaire.

Le terme "**crowd**" dans crowdsourcing a immédiatement déclenché mon cerveau d'ingénieur : il y aura **beaucoup de personnes**, travaillant **concurremment**, attendant **de bonnes performances** depuis **n'importe où** dans le monde. J'aimais le défi.

Mais au niveau du système, les choses étaient **mauvaises**, **vraiment mauvaises**. Voici ce que j'ai trouvé à mon arrivée :

* Une instance Wordpress compromise exécutant des centaines de plugins obsolètes et défectueux, fonctionnant dans une VM sur un serveur partagé
* Des boîtes mail compromises
* Une tonne de Google Docs et de feuilles de calcul.

Et **c'est parfaitement normal**. Encore une fois, il n'y avait aucun membre technique dans l'équipe, et je m'attendais à quelque chose comme cela. Pourtant, l'équipe s'était concentrée sur une opportunité commerciale et avait fait en sorte que le produit semble **fonctionner** magiquement tout en faisant tout manuellement ! (Fake it until you make it). Et c'est ce qui était vraiment incroyable.

![Image](https://cdn-media-1.freecodecamp.org/images/bplEuEzT4UKUCaRZ8t5rh-h44g1Rj-Ee0a3m)
_Notre premier système (Oui, il était nul mais il faisait le travail) !_

Pas de surprise que ma première tâche ait été de recréer la VM, de réinstaller une version mise à jour de Wordpress, de m'assurer que tout le monde change ses mots de passe, d'établir une politique de mots de passe et de supprimer des dizaines de logiciels malveillants sur les ordinateurs de l'entreprise... mais passons aux considérations système.

### D'un Wordpress à une application web

Votre première priorité lorsque vous commencez à construire un produit doit être les **données**. Les données sont ce qui génère la **valeur de votre entreprise**. Ce sera ce que vous utiliserez tous les jours pour prendre des décisions, et ce que vous montrerez à vos **investisseurs** pour démontrer les **progrès**.

Vous devez donner un sens à vos données, et récupérer vos données à partir de différentes sources avec différents formats sera un **énorme gaspillage de temps**. Wordpress peut être un très bon choix dans de nombreux cas en économisant beaucoup de temps d'ingénierie, mais pour leurs besoins, l'équipe de Visage a dû installer des plugins fantaisistes qui n'étaient plus maintenus. En conséquence, nous n'avions aucun contrôle sur le modèle de données généré, et les données qui ne pouvaient pas s'adapter au modèle étaient dispersées dans des dizaines de documents et de feuilles de calcul.

Donc, à moins qu'il n'existe un produit qui réponde déjà à **90%** de vos besoins, pensez à un **modèle de données idéal** et **concevez** et **implémentez** un produit minimum viable (MVP) qui pourra contenir toutes vos données.

Ensuite, pensez **API**. Votre application doit avoir une API, ce sera crucial lorsque vous la vendrez éventuellement. Ne mettez pas immédiatement à l'échelle, mais codez en gardant à l'esprit la scalabilité. Rendez votre API **sans état** et aussi **RESTful** que possible, car tout le monde s'attendra à pouvoir l'interroger en utilisant des méthodes HTTP standard.

Nous avons choisi **NodeJS** dans notre cas, car la plupart de notre code consistait simplement à traiter des entrées et des sorties. NodeJS est **non bloquant** et vient avec une bibliothèque qui est pratique pour concevoir des API : **ExpressJS**.

Si vous avez besoin d'un site web orienté client, vous avez plusieurs options. Vous pouvez créer une couche dans votre serveur d'application qui générera vos pages, ou vous pouvez construire une application **Single Page Javascript** qui sera servie par un serveur d'hébergement web statique.

Chez Visage, nous avons opté pour la deuxième option et décidé de créer une application pour les **utilisateurs** et une pour les **administrateurs**. Cela était simplement parce que nous avions des attentes beaucoup plus grandes pour les utilisateurs que pour les administrateurs, et nous voulions garder les deux bases de code **simples** (également pour des considérations **CORS** plus tard). Voici à quoi ressemblait notre système :

![Image](https://cdn-media-1.freecodecamp.org/images/SdNd6kXexQgaPpBedtBVlXm9WObdsFBb-95a)
_Toutes les données au même endroit_

### Externaliser le stockage des données sensibles dès le début

Sauf si c'est critique pour votre entreprise, il n'y a aucune bonne raison de stocker des données personnelles sensibles dans vos systèmes. La sécurité est une question complexe, et si vous modifiez votre code tous les jours jusqu'à ce que vous trouviez votre marché, cela se cassera. Supposez que **n'importe qui de mal intentionné pourrait pirater votre application** s'il le voulait vraiment.

Le point clé ici est de ne pas détenir de données qui seraient une victoire rapide pour un pirate. **Personne ne vole une banque qui n'a pas d'argent**. Si vous concevez un produit SaaS, vous avez probablement besoin d'authentification et de paiement en ligne. Il existe de nombreux **tiers** que vous pouvez intégrer et qui géreront cela bien mieux que vous ne pourriez le faire.

[Auth0](https://auth0.com/), par exemple, est le tiers le plus connu pour gérer l'authentification. [Stripe](https://stripe.com/fr) est également une bonne option pour les paiements en ligne. Ils consacreront **toutes** leurs ressources et les meilleures équipes d'ingénierie en **sécurité** de la planète pour garder vos **données en sécurité** — ou ils n'ont pas d'entreprise.

![Image](https://cdn-media-1.freecodecamp.org/images/uDa0IaFrOX1Ikoyn-Gtk2quZXvHIdnwvlsyN)
_Panneau réel sur une voiture à San Francisco_

### Les services cloud sont vos meilleurs amis

À ce stade, nous avions un moyen de stocker toutes nos données, l'authentification, le paiement en ligne, et une application web que les clients pouvaient utiliser ainsi qu'une API que nous pouvions vendre à des partenaires pour différents cas d'utilisation. Notre base d'utilisateurs grandissait et il est devenu évident qu'ils voulaient pouvoir accéder à l'application à tout moment. Il était donc temps de penser à la **scalabilité** et à la **disponibilité**.

Nous dépendions d'un seul serveur, mais il ne pouvait gérer qu'un certain nombre de requêtes, et changer de serveur ou publier une nouvelle version signifierait mettre l'application hors ligne pendant la publication. Nos prochaines priorités étaient : **l'équilibrage de charge**, **l'auto-scaling**, **la journalisation**, **la réplication** et les **sauvegardes automatisées**. Bien sûr, si vous êtes le seul ingénieur dans votre entreprise, essayer de résoudre tous ces problèmes seul serait une folie complète.

Heureusement, nous vivons à une époque où un seul ingénieur bien formé peut facilement construire un tel système en quelques jours en utilisant des services cloud comme **Amazon Web Services**, **Google Cloud Services** ou **Azure**. Nous avons décidé de migrer nos systèmes vers **AWS** car à cette époque, c'était la solution la plus complète et nous avions 2 ans de crédits gratuits.

C'est pourquoi je vais principalement parler des solutions AWS dans cet article, mais il existe des services équivalents sur d'autres plateformes. C'est aussi à ce moment-là que nous avons choisi de commencer à exécuter nos modules dans des **conteneurs Docker** pour de nombreuses raisons différentes qui ne seront pas abordées dans cet article (vous pouvez consulter cet article pour plus d'informations : [https://medium.freecodecamp.org/amazon-fargate-goodbye-infrastructure-3b66c7e3e413](https://medium.freecodecamp.org/amazon-fargate-goodbye-infrastructure-3b66c7e3e413)).

La manière dont vous décidez d'exécuter vos applications dépend vraiment de votre cas d'utilisation, comme la **flexibilité** dont vous avez besoin par rapport au **temps** que vous pouvez passer à gérer votre infrastructure.

Il n'y a pas de bonne ou de mauvaise réponse.

Vous pouvez choisir de conteneuriser tous vos modules et utiliser un **système de gestion de conteneurs** comme ECS/EKS dans AWS ou Kubernetes Engine dans GCP. Si ce n'est pas le cas et que vous ne voulez pas gérer vous-même des choses comme l'auto-scaling et l'équilibrage de charge, vous pouvez utiliser Elastic Beanstalk ou App Engine.

Si vous voulez passer au **Serverless**, vous pouvez également combiner l'utilisation de fonctions Lambda et d'API Gateway. Nous avons décidé d'opter pour **ECS**. Nous avons déployé 3 instances dans 3 zones de disponibilité, un **équilibreur de charge**, configuré **l'auto-scaling** en fonction de l'utilisation du CPU, intégré tous les journaux de nos conteneurs avec **Cloudwatch** et configuré des métriques pour surveiller les **erreurs**, les **appels externes** et le **temps de réponse de l'API**.

![Image](https://cdn-media-1.freecodecamp.org/images/QGRQ95YITqUKyCF7PNFjrdGRlwnozYoMP8gx)
_Haute Disponibilité : Saviez-vous que les girafes ne dorment presque jamais ? **99% de temps de fonctionnement**_

Pour notre base de données, nous avons utilisé MongoDB, car notre modèle est bien adapté à une base de données NoSQL, et pour sa haute cohérence. Nous avons décidé de tirer parti de **MongoDB Atlas** et déployé 3 réplicas pour permettre une haute disponibilité. Parmi d'autres services, Atlas fournit **l'auto-scaling**, des **sauvegardes automatisées** et permet de **remonter dans le temps** en cas de catastrophe.

Nous avons également décidé d'héberger tous nos fichiers web statiques dans **S3** et utilisé **Cloudfront** comme **CDN** afin que nos applications JS puissent se charger très rapidement n'importe où dans le monde et être servies autant de fois que demandé. **Cloudflare** est également une bonne option et offre une protection DDOS intégrée.

Pour simplifier, nous avons décidé d'utiliser **Route 53** comme notre DNS en utilisant leurs serveurs de noms pour tous nos domaines. C'est l'un de mes services préférés sur AWS. Il rend la vie tellement plus facile. Chaque fois que vous voulez servir quelque chose via un nom de domaine, qu'il s'agisse d'une instance **EC2**, d'une **IP élastique**, d'un **équilibreur de charge**, d'une **distribution Cloudfront** ou de n'importe quoi d'autre, privé ou public, cela ne prend que quelques minutes car il est si bien intégré avec tous les autres services.

Combinez cela avec le **Certificate Manager** qui permet d'obtenir des **certificats SSL** (y compris les wildcards) gratuitement en quelques minutes et de les déployer sur tous vos serveurs en cochant une case, et vous avez le moyen le plus rapide et le plus fiable d'activer le **HTTPS** sur tous vos modules. Adieu les certificats SSL "Let's Encrypt" que je devais renouveler et installer sur mes serveurs tous les 3 mois environ.

![Image](https://cdn-media-1.freecodecamp.org/images/6wBdoThv3s6DtMC1R3WxwWZC7XlepeVCTUhK)
_Commence à avoir l'air décent_

### Décider d'une stratégie de mise en cache

Tout le monde déteste la gestion du cache, la mise en cache peut se produire à de nombreuses couches différentes, et les problèmes liés au cache sont difficiles à reproduire et un cauchemar à déboguer.

Malheureusement, les **performances** des systèmes distribués dépendent fortement d'une **bonne stratégie de mise en cache**. Il existe de nombreux bons articles sur les bonnes stratégies de mise en cache, donc je ne vais pas entrer dans les détails. Sachez simplement que si vos **ressources Web statiques** sont lourdes, vous voudrez probablement tirer parti du cache du navigateur de votre utilisateur en utilisant intelligemment l'en-tête cache-control.

Si les pages auxquelles vos utilisateurs sont confrontés sont générées sur les serveurs d'application encore et encore, utilisez un proxy de mise en cache comme **Squid**. Mais surtout, il y a de fortes chances que vous fassiez les mêmes requêtes à votre base de données encore et encore. Pour réduire la charge de votre base de données et économiser sur le temps de transfert des données, utilisez un **système de mise en cache d'objets en mémoire** comme **memcached** pour les objets fréquemment utilisés et rarement mis à jour.

Nous avons commencé à envisager d'utiliser **memcached** car nous demandions fréquemment les mêmes profils de candidats et offres d'emploi encore et encore. Son implémentation sur une machine optimisée pour la mémoire a **augmenté** les **performances** de notre API de plus de **30%** lorsque nous moyennons tous les temps de réponse des requêtes dans une journée. Memcached est également distribué, donc il peut s'exécuter sur différents serveurs mais agir comme s'il s'agissait d'un seul grand espace mémoire pour stocker vos objets.

![Image](https://cdn-media-1.freecodecamp.org/images/Z3Zc2YtgTZ7339nQdRXebyitqzR7SyHlA9WY)
_du cache, du cache partout_

### Localisation, localisation, localisation

Maintenant, nous avons un système distribué qui n'a pas de **point de défaillance unique** (si vous considérez les **ELB** d'AWS et un memcached **distribué**), et qui peut **auto-scaler** à la hausse et à la baisse. Nous utilisons également la **mise en cache** pour minimiser les transferts de données sur le réseau. Cela semble assez bien. À ce stade, vous voulez probablement **auditer vos tiers** pour voir s'ils absorberont la charge aussi bien que vous.

Cependant, certains de nos utilisateurs se plaignaient que l'application était un peu **plus lente** pour eux, surtout lorsqu'ils téléchargeaient des fichiers. En effet, même si nos fichiers web statiques étaient mis en cache dans le monde entier (grâce au CDN), tous nos serveurs d'application étaient déployés uniquement dans l'ouest des États-Unis. Les utilisateurs d'**Asie de l'Est** subissaient beaucoup plus de **latence**, surtout pour les transferts de grandes quantités de données.

La solution était simple : **déployer** le même cluster ECS dans une **nouvelle région** en Asie avec un nouvel équilibreur de charge, et compter sur le **routage de proximité géographique** de Route 53 pour diriger les utilisateurs vers l'équilibreur de charge le "plus proche". MongoDB **Atlas** permet également de déployer vos réplicas **à travers** les **régions**, donc aucun travail supplémentaire n'était nécessaire.

![Image](https://cdn-media-1.freecodecamp.org/images/ZwLBVCfwv4eT-nDUBBFGViCLucSEU9M4-9ew)
_Et voici ! Notre système distribué est prêt._

### Conclusion

Bien que le système distribué que vous voyez ici ait été **simplifié** pour cet article, nous avons examiné les parties que vous êtes le plus susceptible de voir dans de nombreuses applications web modernes. D'autres sujets liés mais non couverts sont l'architecture de microservices, le stockage et le chiffrement de fichiers, le sharding de base de données, les tâches planifiées, le calcul parallèle asynchrone... peut-être dans le prochain article !

Mon point principal est : **n'essayez pas de construire le système parfait lorsque vous commencez** votre produit. La plupart de vos choix de conception seront déterminés par ce que fait votre produit et qui l'utilise. Vous ne le saurez que lorsque vous atteindrez l'adéquation produit-marché et commencerez à avoir une bonne vue d'ensemble de votre base d'utilisateurs, et cela peut prendre des mois, voire des années.

Concentrez-vous sur **la compréhension des besoins des gens**, et essayez de trouver une solution à leur problème, même si elle comporte de nombreuses **étapes manuelles**. Ensuite, pensez à des moyens de **l'automatiser**, passez votre temps à **coder** et à **détruire**, et utilisez des **tiers** là où cela a du sens.

Ne mettez pas à l'échelle, mais pensez, codez et planifiez toujours pour la mise à l'échelle. Construisez votre système **étape par étape**, ne traitez pas les problèmes de conception du système en fonction des fonctionnalités qui ne sont pas encore matures, et enfin, essayez toujours de trouver le meilleur **compromis** entre le temps que vous passerez et le gain en performance, en argent et en réduction des risques.

Si vous avez aimé cet article et que vous l'avez trouvé utile, cliquez sur ce bouton d'applaudissements et suivez-moi pour plus d'articles sur l'architecture et le développement ! 👏