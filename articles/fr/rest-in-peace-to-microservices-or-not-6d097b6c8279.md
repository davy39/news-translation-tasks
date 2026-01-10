---
title: 'REST en Paix : Microservices vs monolithes dans des exemples concrets'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-12-14T00:03:42.000Z'
originalURL: https://freecodecamp.org/news/rest-in-peace-to-microservices-or-not-6d097b6c8279
coverImage: https://cdn-media-1.freecodecamp.org/images/1*sCVaEb5AqXrbxoMvokT4BQ.png
tags:
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'REST en Paix : Microservices vs monolithes dans des exemples concrets'
seo_desc: 'By RDX

  I’ve consulted on a dozen microservice projects. Some were awesome (this is the
  future!) and some were equally frustrating (who invented this crap?)

  It’s the execution that matters, not the approach. You can succeed or fail with
  either. Don’t ...'
---

Par RDX

J'ai consulté sur une douzaine de projets de microservices. Certains étaient géniaux *(c'est l'avenir !)* et d'autres tout aussi frustrants *(qui a inventé cette daube ?)*.

C'est l'exécution qui compte, pas l'approche. Vous pouvez réussir ou échouer avec l'une ou l'autre. Ne vous contentez pas d'accepter la propagande amour/haine qui circule.

Voici quelques expériences que j'ai eues et qui montrent comment **les monolithes et les microservices ont leur place.**

### Choisir le bon outil pour le bon travail

Mon équipe a construit une application de lecture de nouvelles. Elle devait scraper des articles, extraire du contenu, classifier, servir une API, afficher un panneau d'administration et gérer les utilisateurs.

* [Scrapy](https://scrapy.org/) (python 2 à l'époque) est le leader en matière de scraping web. Nous avons donc créé un microservice qui scrape les URLs. (Voici un peu plus sur mon [image Docker de 15 Mo avec Tor, Privoxy et un gestionnaire de processus](https://medium.com/@rdsubhas/docker-image-with-tor-privoxy-and-a-process-manager-under-15-mb-c9e344111b61#.pa0hop2iy) si vous êtes curieux.)
* [Newspaper](https://github.com/codelucas/newspaper) (python 3) est l'une des meilleures bibliothèques open source d'extraction d'articles. Nous avons donc créé un microservice qui, étant donné une URL d'entrée, retourne le contenu extrait.
* [R](https://www.r-project.org/) dispose de bonnes bibliothèques pour la catégorisation. Un collègue ayant de bonnes connaissances en R a mis en place un service pour catégoriser les articles en utilisant l'API REST de R.
* [ActiveAdmin](http://activeadmin.info/) est l'une des meilleures et des plus faciles interfaces de panneau d'administration. Depuis longtemps, nous l'utilisons pour les écrans d'administration, et nous l'avons également intégré en quelques jours ici.
* Enfin, pour la passerelle API, nous avons utilisé Node.js avec [PassportJS](http://passportjs.org/) (pour l'authentification multiple) et ElasticSearch.

Avant cette grande réécriture, notre ancienne application était un monolithe Rails. Elle essayait de réinventer tout ce qui a été mentionné précédemment. Vous pouvez imaginer les compromis en termes de code, d'effort et de temps pour la qualité, les progrès et la production.

Les mauvais monolithes essaient de réinventer le monde. Ils pensent que le code et les modèles de conception sont la [solution à tout](https://medium.com/@rdsubhas/10-modern-software-engineering-mistakes-bc67fbef4fc8). Ils s'efforcent de construire des composants réutilisables, des bibliothèques et deviennent également une plateforme en cours de route. Mais ils n'atteignent généralement aucun de ces objectifs.

**Leçon #1 :** Les microservices sont une solution commerciale, pas seulement une solution technologique. Ils évitent aux développeurs de perdre du temps à réinventer des problèmes techniques déjà résolus.

Je me fiche que vous les appeliez « Services », « Architecture orientée services » ou « Microservices ». Une fois que nous avons dépassé les mots à la mode, « monolithe vs microservices » se résume à « 1 service vs N services ».

Pour notre application, « N services » s'est avéré être la pile que nous voulions.

### Applications CRUD monstrueuses

Certains projets d'entreprise peuvent simplement être catégorisés comme des applications CRUD (Create-Read-Update-Delete) monstrueuses. Elles sont un flux sans fin de formulaires, de relations de données, de transformations et de « logique métier » extrêmement compliquée. La portée est énorme, mais le public est minuscule.

Personne ici ne se soucie des meilleures pratiques en matière d'expérience utilisateur, et il est courant d'avoir des écrans rapides et laids qui font le travail.

Nous avions un tel projet de transformation d'entreprise. L'ancien monolithe était une intégration basée sur une vue de base de données. Il était assez bien conçu et ne nécessitait que quelques personnes pour le maintenir, y compris les interfaces utilisateur laides.

Les nouveaux services backend étaient principalement écrits en Java, il était donc difficile de les développer, de les intégrer, de les partager et de maintenir la compatibilité. Et les nouveaux services frontend ont été intégrés dans le monde en constante évolution des applications monopages.

Le déploiement nécessitait une énorme configuration d'automatisation de l'infrastructure. Cela remonte à quelques années, avant que l'écosystème des outils de développement n'ait mûri. À l'époque, chaque changement de contrat devait être coordonné et mis à jour manuellement. C'était l'inverse du scénario précédent — l'effort/sortie/surcharge des microservices semblait beaucoup plus important que celui de l'ancien monolithe.

**Leçon #2 :** Soyez prudent. Traiter les microservices comme la division des couches de code en boîtes dockerisées peut conduire à une « mort par mille coupures ».

### Dompter un énorme arbre de dépendances

Nous avions un autre projet de transformation d'application d'entreprise héritée qui faisait beaucoup de choses comme le scraping de produits et l'agrégation parallèle. C'était un monolithe compliqué et déjà problématique.

Lorsque nous faisons beaucoup de fonctionnalités commerciales orthogonales au sein d'une seule application, cela provoque un énorme arbre de dépendances à la compilation, avec des tonnes de bibliothèques et de frameworks. Par conséquent, l'empreinte runtime, le cycle de vie et les temps de construction étaient également longs. Cela a contribué au vrai problème : les développeurs ne pouvaient pas itérer rapidement, et le temps de mise sur le marché des fonctionnalités en a souffert.

Temps pris pour coder une fonctionnalité simple : plusieurs jours.

Temps pour mettre à niveau une version de bibliothèque (guice) : 1 semaine.

Temps pris pour mettre à niveau une version de framework (Spring) : éternellement.

Des choses triviales avaient la chance de déchirer chaque estimation de temps. Même un petit refactoring prenait longtemps. Il s'avère que la mort par mille coupures est possible avec les monolithes également.

Nous avons divisé le projet en quelques frontières fonctionnelles. Nous avons activement veillé à ne pas partager les bibliothèques et à éviter le goulot d'étranglement de l'arbre de dépendances.

Par exemple, nous avons utilisé une bibliothèque cliente moderne pour publier des messages via PubSub pour les microservices. Mais le grand arbre de dépendances du monolithe ne nous permettait pas d'utiliser la même bibliothèque. Nous avons donc utilisé un client PubSub basé sur HTTP différent.

Les transitionnistes des microservices font souvent l'erreur classique de partager trop de bibliothèques et recréent ainsi les mêmes arbres de dépendances à la compilation (un « monolithe distribué »).

Mais en évitant de partager les fonctionnalités, nous avons pu utiliser différentes bibliothèques pour accomplir les mêmes tâches sans avoir à mettre à niveau le monde.

L'un des services nécessitait beaucoup de concurrency (~1k recherches pour chaque requête). Il utilisait initialement RxJava. Mais il pourrait être réécrit un jour en Golang avec le même contrat d'API, et personne ne se soucierait de l'arbre de dépendances.

**Leçon #3 :** Avec les microservices, vous n'entendrez plus jamais les termes « grande réécriture » ou « système hérité » car il n'y a pas de grands systèmes.

### Le mythe de la scalabilité

Mon équipe a développé une application d'évaluation de code. Elle était à 90 % CRUD, interface utilisateur et rapports, et à 10 % évaluation de code complexe pour une douzaine de langages.

Avant notre arrivée, c'était une série de microservices — un pour chaque type de langage, écoutant différentes files de messages. Elle avait un frontend-as-a-service séparé, un admin-panel-as-a-service, etc. Leur raisonnement initial ? La scalabilité.

Nous avons tué tout cela et construit un meilleur monolithe. Il a été entièrement réalisé en tant qu'application Rails unique — interface utilisateur, admin, backend et interface candidat.

La partie évaluation de code fonctionnait en tant que travail en arrière-plan (ActiveJob). Nous l'avons externalisé via des conteneurs Docker simples, sans état et ponctuels. Le contrat de base pour l'évaluation de code est passé de REST/JSON à fichier/stdin/stdout. Il a mieux scalé que l'ancien système, car nous devions simplement augmenter les travailleurs en arrière-plan pour gérer plus d'évaluations de code.

Ce qui semblait être une application sophistiquée de l'extérieur — prenant en charge 8 principaux langages de programmation avec une évaluation intelligente — était extrêmement simple à l'intérieur.

**Leçon #4 :** Vous n'avez pas besoin de microservices pour exécuter plusieurs instances d'un service ou d'un travailleur. Les bons monolithes peuvent également scaler pour certaines classes de problèmes.

Il est tout à fait possible de créer des monolithes scalables et des microservices non scalables. Tout dépend de la manière dont vous appliquez les principes sous-jacents de chacun.

### Microservices en tant que produits

L'un des projets de microservices les plus satisfaisants sur lesquels j'ai travaillé abordait les microservices en tant que produits. Nos clients étaient des personnes extrêmement intelligentes, techno-fonctionnelles, et ils utilisaient clairement les microservices comme un outil commercial.

Ils modélisaient chaque service comme un produit, puis publiaient plusieurs produits pour différents clients. Ils alignaient les publications de produits de manière à ce que chacun puisse utiliser les APIs des autres. À leur tour, ils ont créé un écosystème brillant. Cela en a fait un leader du marché dans leur verticale.

L'entreprise moyenne aujourd'hui utilise au moins une douzaine de produits logiciels et d'intégrations. Le consommateur cloud moyen utilise plusieurs produits cloud. Je vois même des personnes non techniques utiliser des micro-produits et des micro-applications. Par exemple, un outil pour les entretiens, un pour le suivi des vacances, un pour les bulletins de paie, etc. Les gens adoptent des outils plus petits et plus spécialisés qui font correctement le travail.

**Leçon #5** : Nous sommes fermement et solidement entrés dans l'ère des micro-produits, des micro-applications et des micro-services. Mieux vaut apprendre à bien le faire.

Il y a cette peur constante que l'apprentissage automatique vole les emplois de programmation. La plupart des emplois de programmation deviennent des APIs aujourd'hui.

### Transactions distribuées

L'un des arguments les plus courants contre l'utilisation des microservices est les risques associés aux transactions distribuées.

Appelez-vous une passerelle de paiement externe qui déduit de l'argent, mais qui pourrait échouer sur votre callback ? Avez-vous plusieurs mécanismes de connexion (comme l'email ou OAuth) ? Appelez-vous des produits SaaS tiers qui n'ont pas d'option de rollback ? Utilisez-vous des APIs Cloud et des buckets de stockage qui ne respectent pas votre frontière de transaction ? Avez-vous des workflows couvrant plusieurs cycles de vie de requêtes vers le même service ?

Alors vous avez déjà des transactions distribuées d'une manière ou d'une autre, que vous le vouliez ou non.

L'idée que qu'un système et une requête peuvent représenter ou contrôler l'ensemble de l'état transactionnel du problème commercial est une fantaisie. Si vous pouvez modéliser vos intégrations externes sans verrous distribués et transactions, alors vous pouvez modéliser vos intégrations internes également.

**Leçon #6** : Les verrous distribués et les transactions ne sont pas gratuits avec les monolithes non plus.

### Outillage vs Personnes

Oui, plus de services signifie plus d'outils. Cela implique l'intégration continue et le déploiement continu (CI/CD), l'automatisation de l'infrastructure, l'outillage des développeurs, la capacité à concevoir de bonnes APIs, le partage de contrats, la documentation, l'intelligence client et les bibliothèques, les processus, les tests et beaucoup d'autres outils.

[Vous devez être au moins aussi grand pour monter les microservices](https://news.ycombinator.com/item?id=12508655).

Si une organisation n'a pas la robustesse et la maturité d'ingénierie pour exécuter sans effort une poignée de services (12factor, CI, CD, intégration, tests, etc.), ce sera un désastre de passer à beaucoup d'entre eux.

Beaucoup de personnes venant d'un état d'esprit monolithe font du [Big Design Up Front](https://en.wikipedia.org/wiki/Big_Design_Up_Front). Les microservices sont meilleurs lorsqu'ils sont **en pleine face**. Il suffit de [jeter tout le code boilerplate](https://medium.com/@rdsubhas/10-modern-software-engineering-mistakes-bc67fbef4fc8), d'implémenter l'API de manière directe et d'investir du temps dans des tests unitaires/contrats de bonne qualité. Comme pour l'outillage vs les personnes — les microservices nécessitent un changement de mentalité et une grande quantité de **désapprentissage**.

La bonne nouvelle est que beaucoup de ces problèmes d'outillage ont de bonnes solutions d'ingénierie. Docker, Kubernetes, REST, Swagger, Falcor, gRPC, les outils de pipeline CI/CD, PaaS, Cloud, etc. L'écosystème autour des microservices a déjà beaucoup mûri et s'améliore constamment.

La mauvaise nouvelle est que les microservices ne peuvent pas être appris comme un framework ou un outil. Ils nécessitent une **approche holistique** qui vient avec l'expérience. Vous avez besoin de bonnes personnes qui ne sont pas seulement des codeurs brute-force, mais aussi des ingénieurs bien équilibrés avec une solide fondation dans tout le cycle de vie du développement logiciel, du développement aux tests en passant par le déploiement.

Il y a de grandes entreprises qui prennent des mois pour chaque intégration. Et puis il y a des entreprises modernes comme Google, Facebook et Netflix qui exécutent des milliers de services intégrés à une qualité et une vitesse bien supérieures. La différence n'est pas seulement les outils — ce sont les personnes impliquées et leur approche d'ingénierie.

**Leçon #7** : Les microservices sont une culmination de multiples pratiques d'ingénierie. Ils ont une courbe d'apprentissage, de désapprentissage et de transformation abruptes.

#### Conclusion

L'approche des microservices est juste un autre outil dans la boîte à outils du solutionniste. Et un outil est juste un outil. Il peut finir par être un atout commercial puissant ou un goulot d'étranglement improductif pour les développeurs. Que nous ayons raison ou tort dépend entièrement de la manière dont nous utilisons cet outil.