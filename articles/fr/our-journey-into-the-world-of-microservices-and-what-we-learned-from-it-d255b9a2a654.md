---
title: Notre voyage dans le monde des Microservices — et ce que nous en avons appris.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-11T21:52:30.000Z'
originalURL: https://freecodecamp.org/news/our-journey-into-the-world-of-microservices-and-what-we-learned-from-it-d255b9a2a654
coverImage: https://cdn-media-1.freecodecamp.org/images/0*APjNMu9aZ4xsCz1y
tags:
- name: agile development
  slug: agile-development
- name: Life lessons
  slug: life-lessons
- name: Microservices
  slug: microservices
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Notre voyage dans le monde des Microservices — et ce que nous en avons
  appris.
seo_desc: 'By Ignacio Salazar Williams

  I know, I know everyone is talking about Microservices. It’s the a pattern that
  will lead us to the future of architecture, say those who talk about Digital Transformation.
  It’s the “Destroyer of Monoliths” for others, the...'
---

Par Ignacio Salazar Williams

Je sais, tout le monde parle des Microservices. C'est le modèle qui nous mènera vers l'avenir de l'architecture, disent ceux qui parlent de [Transformation Numérique](https://enterprisersproject.com/what-is-digital-transformation). Pour d'autres, c'est le "Destructeur de Monolithes", la solution miracle qui résoudra tous nos problèmes architecturaux.

Permettez-moi de vous dire quelque chose sur les microservices. **Ils sont vraiment quelque chose**, mais ce n'est pas comme si **pouf** **de la poussière magique** était la solution à tous nos problèmes. Je ne vais pas vous en dire plus en tant que modèle, mais plutôt essayer de raconter cette histoire (mon histoire) aussi bien que possible. Je vais discuter de la façon dont ce concept, ce modèle, a été développé dans la réalité, dans certaines circonstances. Je l'appelle le **Micro-Armageddon**.

![Image](https://cdn-media-1.freecodecamp.org/images/kHXZp0ke9-N0aBMf6LeqPV5RrjZaDIKjCtOP)
_Source de [GIPHY](https://giphy.com/gifs/oscars-awards-academy-Ho2mVZ5dvsW7S" rel="noopener" target="_blank" title=")_

Au quotidien, dans mon équipe, il y avait des choses qui étaient hors de notre portée et qui menaient à des problèmes. Mais il s'agissait simplement de voir le tableau d'ensemble et de travailler avec la mentalité d'améliorer continuellement nos composants jusqu'à atteindre les normes de qualité que nous avions en tant qu'équipe.

Alors, suivez-moi dans ce voyage de bons et de mauvais moments, de rires et de larmes, et beaucoup de "pourquoi diable avons-nous fait cela en premier lieu ?".

> _TL;DR ?_  
> _Je sais que cela semble beaucoup, mais laissez-moi vous dire quelque chose. Si vous cherchez à apprendre des erreurs des autres sur les Microservices, je vous recommande vivement de lire cet article en entier. Mais si ce n'est pas le cas, vous pouvez passer directement aux memes — au moins, cela vous fera rire !_

### Un peu de contexte

![Image](https://cdn-media-1.freecodecamp.org/images/HFuGKP76J88kmX5hEOYDvZQnocRWHcqehIql)
_Source de [Innoview](http://innoview.hu" rel="noopener" target="_blank" title=")_

Commençons par les bases. Il y avait moi (Salut !), un étudiant récemment diplômé en informatique, qui venait d'être embauché pour une mission de conseil (le Far West des emplois). J'ai été affecté à ce projet pour l'un de nos clients (dans leurs bureaux), dans lequel notre équipe était chargée d'appliquer une Transformation Numérique à leur entreprise. Par conséquent, les Microservices étaient impliqués. (Maintenant que j'ai plus d'expérience dans le domaine, j'entends souvent ces deux concepts ensemble.)

Nous utilisions [Node.js](https://nodejs.org/en/) comme langage de programmation back-end (ohhhh yeeees), ce qui signifiait que nous utilisions également [Express](http://expressjs.com/) comme framework par défaut pour exposer les APIs. De plus, il est important d'ajouter que nous utilisions la méthodologie Agile de [Scrum](https://medium.com/chingu/a-short-introduction-to-the-scrum-methodology-7a23431b9f17) (vous verrez bientôt pourquoi j'ai soulevé ce point).

#### Les Équipes

![Image](https://cdn-media-1.freecodecamp.org/images/AyGe9CCxGMuw6dKE2txFxzMYtm-Dg511LMTF)
_Photo par [Unsplash](https://unsplash.com/@rawpixel?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">rawpixel</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Nous étions divisés en deux grands groupes : le premier, celui dont je faisais partie, était l'**Équipe d'Architecture**. Nous étions chargés d'orienter les équipes et de répandre la bonne parole sur les Microservices. La deuxième équipe, l'**Équipe de Développement**, était chargée de développer les produits souhaités par l'entreprise. Il y avait plusieurs équipes travaillant sur différents produits en même temps, tout en travaillant sur les Microservices.

L'**Équipe d'Architecture** ressemblait à ceci :

* 1 Senior Manager (le nôtre)
* 2 Managers (1 le nôtre, 1 le leur)
* 10 Architectes (6 les nôtres, 4 les leurs)
* 2 responsables du big data
* 3 responsables CI/CD
* 3 responsables de la sécurité
* 2 responsables de l'architecture de développement back/front end

Chaque **Équipe de Développement** ressemblait à ceci :

* 1 Scrum Master (un autre consultant)
* 1 Product Owner (côté client)
* 4 Développeurs (2 les nôtres, 2 les leurs)
* 1 QA
* 1 UX
* 1 Architecte (côté client)

> _Je sais que cela semble déjà mauvais, tout mélanger, mais ne vous inquiétez pas — pour nous, c'était une opportunité de faire les choses correctement…_

#### Compétences de base des développeurs

![Image](https://cdn-media-1.freecodecamp.org/images/jmm-Fjij7bveSXWDVpeKMQVaeHMijUZyp8oG)

> Aucun de nous n'est né en étant un développeur compétent, nous étions tous comme un singe essayant de compiler un "Hello World" basique. [Felipe Lazo](https://www.freecodecamp.org/news/our-journey-into-the-world-of-microservices-and-what-we-learned-from-it-d255b9a2a654/undefined)

Les membres de notre équipe avaient toutes sortes de parcours, de ceux qui savaient à peine comment fonctionnait leur propre ordinateur, à ceux qui venaient probablement de la NASA. Certaines personnes avaient travaillé avec COBOL, Java, JavaScript, C, Python, et d'autres, tandis que d'autres n'avaient travaillé avec aucun langage du tout.

Il serait donc facile de comprendre que certains membres de l'équipe n'étaient pas particulièrement doués pour développer du bon code et des structures, car beaucoup d'entre eux n'avaient aucune expérience préalable dans le domaine. Encore une fois, il y en avait d'autres qui avaient une certaine expérience. Il était donc parfaitement acceptable d'avoir tous ces profils différents, mais c'était à nous de faire le meilleur usage possible. Nous ne pouvions pas voir cela comme une faiblesse, mais comme une opportunité pour nous en tant qu'équipe (surtout lorsque vous travaillez dans un environnement agile).

### L'Objectif

Nous étions là avec l'objectif de mettre en œuvre des Microservices comme solution Back-End pour l'intégration des composants hérités que notre client avait. Nous prévoyions de les exposer sous forme d'APIs simples afin que les équipes puissent les intégrer dans leurs applications.

Voici les exigences initiales de nos Microservices :

* Ils devaient consommer un service SOAP et retourner le résultat en JSON. Je sais que pour la plupart d'entre vous (et moi y compris), cela va sembler vraiment mauvais. Mais il fallait que ce soit ainsi, car les Microservices n'étaient pas autorisés à se connecter directement à la couche de données, ils devaient donc passer par SOAP [Exigence initiale du client].
* Il fallait journaliser toutes les données produites par les Microservices dans le tout nouveau DataLake.
* Authentification de base.
* Les rendre aussi résistants aux pannes que possible.

À ces exigences, nous devions ajouter :

* la qualité que nous désirions grâce aux tests unitaires (y compris notre norme de couverture ambitieuse de 90 %)
* Analyse statique du code
* Test de performance
* et une sorte de vérification de sécurité.

Tout cela devait être vérifié manuellement localement, puis vérifié via un pipeline rigoureux (CI/CD). Je dis rigoureux, mais ce n'était pas bloquant. Il permettait toujours aux équipes de déployer des Microservices même si l'un des jobs échouait. Mais **ne faites jamais cela, ou du moins connaissez les conséquences**.

Jusqu'à présent, nous n'avions pas beaucoup de problèmes. Cela semblait assez bien pour une configuration de base afin de développer des Microservices. Nous avions DevOps, nous étions tous au même endroit, nous avions notre méthodologie, nous avions notre modèle, et nous avions un environnement d'exécution fantastique (Node.js) qui nous permettrait de construire et de suivre les règles étape par étape pour faire de ce projet un chef-d'œuvre. Eh bien, au moins c'est ce que nous pensions…

### Oh là là, des erreurs ont été commises

![Image](https://cdn-media-1.freecodecamp.org/images/NI49nxrMg1e5yTrvyk9QU6RZrVo5qONSrong)
_Image précise de l'équipe essayant de sauver les Microservices_

Regardez cette image assez précise de l'équipe d'architecture essayant de sauver les Microservices de leur destin. Pourquoi cela est-il arrivé, pourriez-vous demander ? Eh bien, cela peut arriver lorsque vous donnez la liberté à plusieurs équipes de développer leurs propres Microservices dans un environnement Agile. Les problèmes surgissent lorsque vous ne donnez aucune autre explication sur ce que sont réellement les Microservices, ce qu'ils font, quel est leur but, comment nous les gouvernons, et, surtout, quelle doit être leur taille.

Et pour couronner le tout, au début du projet, nous n'avions aucun logiciel de contrôle de version fiable sauf Subversion. Pendant ce temps, nous attendions que Git soit installé sur place.

Un problème que nous voyions souvent dans de nombreuses équipes immatures était que, au lieu d'essayer d'éteindre l'incendie, elles le propageaient encore plus en dupliquant les Microservices et en commençant à construire par-dessus. Cela les rendait encore plus gros et ils contenaient du contenu inutile et dupliqué.

* Microservice _Clients_ (Les équipes A, B et C travaillent dessus)  
 — L'équipe B est fatiguée de toutes les fusions, et de toutes les disputes pour savoir qui est responsable de quoi, plus le déploiement.
* Microservice _Loans-Clients_ (Équipe B)  
 — L'équipe B copie l'état exact sur lequel ils travaillaient dans le Microservice _Clients_. Cela expose et maintient de plus en plus de points de terminaison inutiles en plus de leurs points de terminaison utiles.

Nous voilà donc. Comment diable (l'enfer réel) résolvons-nous tous ces problèmes ? Eh bien, voici ce que nous avons fait.

### Les Symptômes

![Image](https://cdn-media-1.freecodecamp.org/images/A2j6VKJ699KC42Umz9HLnuNLJhkGTLKc8z8A)
_Photo par [Unsplash](https://unsplash.com/@rawpixel?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">rawpixel</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Il était clair que nous ne pouvions pas continuer avec tout ce désordre, alors nous avons enfilé nos blouses de médecins, stérilisé la pièce et fait une autopsie de ce que nous avions. Nous avons identifié les symptômes de notre destin inévitable, priorisé les plus importants et essayé de remporter de petites victoires qui nous permettraient de prendre le contrôle de la situation.

> _Les petites victoires permettent non seulement de prouver que vous connaissez le sujet, mais elles permettent également aux équipes de savoir que quelque chose peut être fait pour améliorer leur travail quotidien._

#### Mini-Monolithes A.K.A Macroservices

Attendez quoi ? Nous parlions de microservices…

![Image](https://cdn-media-1.freecodecamp.org/images/S1UIv5TkaDGJjNGUjDudUMTPXhuyKITVkeZV)

Je parie que vous avez lu plusieurs fois le principe [**S.O.L.I.D**.](https://hackernoon.com/solid-principles-made-easy-67b1246bcdf), sur le fait d'avoir des pièces compactes intelligentes qui ont le célèbre principe de responsabilité unique.

Ce que nous avions n'avait rien à voir avec cela. C'est pourquoi je les ai appelés **Macroservices**, après avoir vu ce qui se passait.

Imaginez simplement ceci : dans un domaine simple, appelons-le _Utilisateurs_, il y avait environ 15 opérations **POST** dans le même ****toux**** "Microservice". Chacune avait un but différent sous le même domaine et utilisait des bibliothèques faites sur mesure pour chacune d'elles. De plus, nous avions tous les tests unitaires et de performance répartis partout. C'était le chaos. C'était à peu près quelque chose comme ceci :

```
.
├── app --Tout le MS est ici
│   ├── controllers --Tous les contrôleurs du domaine
│   │   ├── dummies
│   │   │   └── ** Tous les dummies pour chaque contrôleur **
│   │   ├── xsl
│   │   │   └── ** Toute la configuration xsl pour chaque contrôleur **
│   │   ├── Controller1.js
│   │   ├── Controller2.js
│   │   ├── Controller3.js
│   │   ├── Controller4.js
│   │   ├── Controller5.js
│   │   └── **Littéralement 20 autres contrôleurs**
│   ├── functions --Toutes les fonctions du MS
│   │   ├── function1.js
│   │   ├── function2.js
│   │   ├── function3.js
│   │   └── function4.js
│   ├── properties --Toutes les propriétés du MS
│   │   ├── propertie1.js
│   │   └── propertie2.js
│   ├── routes --Toutes les routes du MS
│   │   ├── routes_useSecurity.js
│   │   └── routes_withoutSecurity.js
│   ├── services --Services supplémentaires qui étaient consommés
│   │   ├── service1.js
│   │   └── service2.js
│   └── xsl
│       └── **Un tas de XSL pour faire des transformations**
├── config --"Configurations" globales
│   ├── configSOAP.js
│   ├── configMS.js
│   ├── environments.js
│   ├── logging.js
│   ├── userForBussinessA.js
│   └── userForBussinessB.js
├── package.json
├── README.md
├── test--Tous les tests
│   ├── UnitTesting
│   │   └── Controllers
│   │       └── ** Tous les 25 tests en théorie **
│   └── PerformanceTest
│       ├── csv_development.txt
│       ├── csv_QA.txt
│       ├── csv_production.txt
│       ├── performance1.jmx
│       └── performance2.jmx
├── server.js --Serveur Express
├── serverKey.keytab
├── sonarlint.json
├── encryptor
├── ** Environ 10 autres fichiers inutiles **
└── Dockerfile
```

![Image](https://cdn-media-1.freecodecamp.org/images/9omI01k5ttMHeMAnmTT3xHEgG9fFvclEkeLo)
_C'était à peu près moi_

Tout d'abord, cela devait cesser car c'était ingérable. Les équipes se battaient, car pour tester quelque chose dans l'environnement DEV (ce qu'elles faisaient souvent), elles devaient passer par le pipeline CI/CD. À ce moment-là dans le projet, il n'était certainement pas parfait.

Donc, si l'**équipe A** modifiait **Controller1**, elles devaient passer par le pipeline, avec une forte probabilité d'échec (et le déploiement échouerait également). Elles recommenceraient encore et encore jusqu'à ce qu'elles réussissent. Par conséquent, toutes les équipes essayaient de se précipiter pour ne pas être les dernières à déployer. Car si quelque chose échouait dans ce déploiement, les doigts étaient pointés. Cela signifiait que l'équipe avait fait quelque chose de mal et l'avait cassé.

> _Amusant, non ? Un environnement sain pour tous les développeurs. Qui ne veut pas être là… eh bien, PAS MOI !_

### Il était temps de repartir à zéro

![Image](https://cdn-media-1.freecodecamp.org/images/w6qPgt5B6Wy2mmnYRsbSNmY34FSk5IqKiDP3)

Nous avions besoin de repartir à zéro et de faire les choses correctement. Prendre le contrôle de qui faisait quoi, et les rendre responsables. Mais nous devions être justes : nous n'allions pas rendre une équipe responsable d'un domaine entier contenant 15 opérations, tests, déploiements, et ainsi de suite. Personne ne voulait cela.

> _Vous savez, nous sommes agiles, les gens agiles font des choses agiles. Nous n'avons pas besoin de gaspiller notre temps précieux dans ces combats pour savoir qui possède quoi, en soulevant des blocages et en pointant du doigt ** **en roulant des yeux****._

#### Étape 1 : Dimensionnement des Microservices

Je vais faire une **assertion audacieuse** et dire que le nombre maximal d'opérations pour tout Microservice **doit** suivre la norme [**CRUD**](https://fr.wikipedia.org/wiki/CRUD). Oubliez de penser à la taille que doivent avoir les Microservices.

Suivre cette règle vous donnera la tranquillité d'esprit la nuit, en sachant qu'à tout moment, vous n'aurez besoin d'avoir au maximum que 4 opérations dans n'importe quel sous-domaine. Et c'est tout.

Cela signifie :

#### POST — Créer

Les procédures CREATE sont l'insertion de nouvelles données comme finalité des Microservices.

#### GET — Lire

Les procédures READ lisent les données nécessaires par le client.

#### PUT — Mettre à jour

Les procédures UPDATE modifient les enregistrements sans les écraser.

#### DELETE — Supprimer

Les procédures DELETE suppriment là où c'est spécifié.

![Image](https://cdn-media-1.freecodecamp.org/images/3SKmmU2hZXeEdU2Owfg9z-ihdt-NS6Bq-8-k)

L'utilisation de cette règle nous a permis de créer des Microservices plus compacts, intelligents et standardisés. Cela nous donnera l'avantage lorsque viendra le temps de diviser les Microservices, par exemple.

Supposons que j'ai mon Microservice _Clients_ dans un domaine bancaire, et soudain je vois que j'ai besoin non seulement de nos _clients de crédit_ mais aussi de nos _emprunteurs_. Eh bien, c'est facile. Je divise simplement notre domaine Clients en deux sous-domaines : _Client-Crédit_ et _Client-Prêt_, et à partir de là, vous pouvez voir comment tout commence à se mettre en place.

Parfait ! Nous avions maintenant de vrais microservices. Il appartenait maintenant au client et à l'équipe de développer un moyen de savoir comment diviser les domaines et connaître leurs sous-domaines.

> _Si seulement il y avait un moyen de le faire… **toux** [**Conception Pilotée par le Domaine**](https://medium.com/withbetterco/what-is-domain-driven-design-bcf81fc4fdc1)._

#### Étape 2 : Quelqu'un doit en être responsable

Wouhou, nous avions résolu l'un de nos problèmes, mais attendez — j'avais maintenant un tas de petites pièces, et tout le monde travaillait dessus. Et je n'allais pas en être responsable si cela cassait.

Tout ce que je dirai est : "**Si vous le codez, vous en êtes responsable**". Et avec cette sagesse puissante, vous pourriez dire : "Eh bien, je le sais, tout le monde le sait." Mais non, tout le monde ne le savait pas, et c'est une erreur courante. Soyez donc intelligent et allez plus loin en faisant de cela une règle.

![Image](https://cdn-media-1.freecodecamp.org/images/gKCZrqk4UPKn1dD2rJ7n-QJnrCHKoBELGhYN)
_Source de l'article de D. Keith Robinson [Apprendre à aimer Git](https://medium.com/designing-atlassian/learn-to-love-git-part-one-the-basics-90429f456ace" rel="noopener" target="_blank" title=")_

Git vous permet de développer en paix (si c'est bien appliqué — consultez le lien sur [Apprendre à aimer Git](https://medium.com/designing-atlassian/learn-to-love-git-part-one-the-basics-90429f456ace) de D. Keith Robinson ci-dessus), en sachant que votre code sera toujours à jour. Si quelqu'un d'autre veut l'améliorer, suggérer un changement, ou s'il a simplement besoin d'une mise à jour, tout cela doit passer par le propriétaire. Pour les besoins de cet exemple, nous dirons que le propriétaire est l'architecte de l'équipe DEV qui l'a développé. Cela fonctionne si bien dans les environnements agiles.

#### Étape 3 : Point de terminaison de l'API (Nommage) et Versioning

La manière dont vous nommez les APIs pourrait faire gagner à tous vos développeurs des tonnes de temps et d'efforts. **Nommer les APIs n'est pas un jeu. Cela pourrait sauver des vies**.

Il est vraiment important d'ajouter de la valeur à vos Microservices en les nommant correctement. Si vous ne savez pas comment les nommer, demandez à l'entreprise et discutez-en avec votre équipe. Le développement piloté par la conception peut aider ici.

Consultez les [directives de conception d'API RESTful — meilleures pratiques](https://hackernoon.com/restful-api-designing-guidelines-the-best-practices-60e1d954e7c9) pour plus d'informations ici. J'aurais pu citer toute la page.

#### Étape 4 : Restructurons ce que nous avions

![Image](https://cdn-media-1.freecodecamp.org/images/D1OTtJsvT32jf-aLthKXqbYlnWQwbOkJpYSq)
_Un enfant jouant avec une tour de blocs Jenga par [Unsplash](https://unsplash.com/@mparzuchowski?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Micha2 Parzuchowski</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

> _C'est une chose d'avoir le concept juste, mais à quoi cela ressemble-t-il en pratique ?_

L'arborescence de fichiers suivante que je vais vous montrer revient à mon idée de la manière dont je suis un adepte du concept de Microservices. Je l'ai fait suivre le concept de **couplage lâche** et de **forte cohésion** entre les services :

```
.
├── config
│   ├── artillery.js
│   ├── config.js
│   ├── develpment.csv
│   ├── processorArtillery.js
│   ├── production.csv
│   └── qa.csv
├── index.js
├── package.json
├── package-lock.json
├── README.md
├── service
│   ├── getLoans --L'opération
│   │   ├── getLoans.config.json --Configuration de la ressource
│   │   ├── getLoans.contract.js --Test de contrat
│   │   ├── getLoans.controller.js --Contrôleur
│   │   ├── getLoans.performance.json --Configuration du test de performance
│   │   ├── getLoans.scheme.js --Validateur de schéma
│   │   ├── getLoans.spec.js --Tests unitaires
│   │   └── Util --Fonctions locales
│   │       ├── trimmer.js
│   │       └── requestHandler.js
│   ├── postLoans
│   │   ├── postLoans.config.json
│   │   ├── postLoans.contract.js
│   │   ├── postLoans.controller.js
│   │   ├── postLoans.performance.json
│   │   ├── postLoans.scheme.js
│   │   └── postLoans.spec.js
│   └── notFound
│       ├── notFound.js
│       ├── notFound.performance.json
│       └── notFound.spec.js
├── Util --Fonctions globales
│   ├── headerValidator.js
│   ├── bodyValidator.js
│   ├── DBConnector.js
│   └── BrokerConnector.js
├── sonarlint.json
└── sonar-project.properties
```

Non seulement le concept de les rendre remplaçables ou divisibles dans un concept de Domaine/Sous-domaine est possible pendant le processus **DDD**, mais aussi de manière répertoire/fichier. Aux fins de cet exemple, j'ai utilisé un projet en Node.js.

Chaque opération de nos Microservices avait tous les composants qui remplissaient les exigences de son développement, config, tests unitaires, tests de performance, [Test de Contrat](https://martinfowler.com/bliki/ContractTest.html), validations de schéma et le Contrôleur. Ainsi, traiter l'opération comme un tout nous a permis d'avoir le contrôle lorsque nos Microservices deviennent trop grands et doivent être divisés. Donc, nous avons pratiquement dû déplacer le dossier entier vers son nouveau Microservice correspondant. Mais c'était tout — pas besoin d'essayer de trouver les bons composants, ou d'essayer de les jongler pour les faire fonctionner à nouveau.

**NOTE** : Nous avons généré la route de l'API dynamiquement, donc chaque opération est suffisamment descriptive, ainsi que le _package.json_ du projet, pour construire la route que nous avons exposée. Cela nous a donné la flexibilité que nous voulions : plus d'édition manuelle des routes (beaucoup d'erreurs sont souvent faites ici, donc nous voulions les éviter). Par exemple :

* VERBE /{{Nom de l'Artefact}}/{{Domaine}}/{{Version}}/{{Sous-domaine}}/   
— **Nom de l'Artefact** : Quel type d'artefact exposez-vous (Microservices, [BFF](https://samnewman.io/patterns/architectural/bff/), ou autre) ?  
 — **Domaine** : Auto-explicatif, le domaine auquel appartient l'opération.  
 — **Version** : Version majeure actuelle disponible de notre ressource.  
 — **Sous-domaine** : L'opération que nos Microservices effectueront **CRUD**.
* GET/Microservice/Client/v1/loan/ — GET tous les prêts qui ont été faits par tous les clients.

Cela ressemble vraiment à de la magie, mais je le recommande vivement. Vous verrez que la plupart des problèmes que vous avez lors de l'organisation de vos microservices seront considérablement réduits.

#### Étape 5 : Documentation

![Image](https://cdn-media-1.freecodecamp.org/images/exGoVYJp-DUx9jiFKEqFceDZNDu81jww0Slj)
_Un brillant comic de Dilbert, Source [Ici](http://dilbert.com/strip/2007-11-26" rel="noopener" target="_blank" title=")_

Uff, je dois dire que j'ai littéralement eu des frissons. Je peux imaginer tous ces praticiens agiles, hurlant leurs âmes scrum. Mais ne vous inquiétez pas, je vous couvre sur ce point.

Je vais introduire deux concepts : premièrement et surtout, puisque nous exposons des APIs, essayons tous ce **Développement API First**.

> Le Développement API First est une stratégie où la première priorité est de développer une Interface de Programmation d'Application en tenant compte des intérêts des développeurs cibles, puis de construire le produit par-dessus, qu'il s'agisse d'un site web, d'une application mobile ou d'un logiciel SaaS. En construisant par-dessus des APIs avec les développeurs à l'esprit, vous et vos développeurs économisez beaucoup de travail tout en posant les fondations pour que d'autres construisent par-dessus. ([Une Approche de Développement API-First](https://blog.restcase.com/an-api-first-development-approach/) par restcase).

Et comment construisons-nous cela, pourriez-vous demander ? C'est là que notre deuxième concept entre en jeu : [**Swagger**](https://swagger.io/)**,** l'un des nombreux outils pour construire des APIs. Cet outil ouvrira la porte à la conception et à la modélisation d'APIs de manière propre et organisée.

Vous ne pouvez pas demander mieux. Non seulement nous avons déjà résolu le problème que nous rencontrons habituellement en agilité concernant la documentation, mais cela améliore également la manière dont l'équipe développera les Microservices. Cela leur donne les bons outils pour interagir les uns avec les autres et élimine la possibilité qu'une autre équipe puisse dire quelque chose comme : "Mon équipe avait besoin de cela comme sortie, avec ces caractéristiques de cette API, et nous n'avons rien obtenu de tel." Ensuite, vous pouvez dire en toute sécurité : "Voici la documentation de notre API, conçue et approuvée par l'architecte, répondant aux exigences de l'entreprise." Mic drop. Ainsi, toute itération ultérieure serait autour de l'API bien documentée.

#### Étape 6 : Formation

Comme je l'ai dit plus tôt, c'est à nous de faire le meilleur usage de nos développeurs et équipes. Prenez votre temps, identifiez les faiblesses et améliorez !

![Image](https://cdn-media-1.freecodecamp.org/images/I1erhqLk-0Kgh8G-4z7xkxTfKHmfAkVFYYQR)

Je sais que chacun a des préférences différentes en matière de formation de ses équipes, mais je recommande vivement [**Coding Dojo**](http://codingdojo.org/) lorsqu'il s'agit d'agilité et d'optimiser le temps de votre équipe. Cette technique de formation nous a permis de former toutes nos équipes afin qu'elles aient le même niveau de base d'expertise dans chaque sujet (Node.js, Microservices, Tests Unitaires, Tests de Performance, et plus encore !). Cela a également amélioré la manière dont les informations étaient transmises aux équipes — nous avons tous joué au jeu du téléphone, et nous savons comment cela se termine la plupart du temps. Personne n'a le temps de lire des années de documentation. Nous pouvons même appliquer les retours de nos équipes à notre vie quotidienne. Donc tout le monde GAGNE !

### Leçons apprises & mots de la fin

![Image](https://cdn-media-1.freecodecamp.org/images/1Dbzf84WYhYQC0StYhfnrNvrlwXLADAq6X2R)
_Photo par [Unsplash](https://unsplash.com/@helloimnik?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Hello I'm Nik</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Pour moi, il s'agit de savoir comment toutes les pièces qui font partie de votre écosystème interagissent les unes avec les autres. Il s'agit d'apprendre à réagir à elles, car je peux vous assurer que, un jour, vous penserez à une solution à un problème. Mais ensuite, vous pourriez finir par faire quelque chose de complètement différent juste pour vous adapter aux exigences. C'est la beauté des Microservices. Ils vous permettent d'être flexible, et peu importe à quel point cela peut sembler horrible, si vous suivez le concept de **pièces remplaçables, couplage lâche**, et **forte cohésion**, faites-moi confiance, tout ira bien.

La mise en œuvre des Microservices est un voyage pour les courageux qui sont prêts à s'améliorer chaque jour. C'est pour ceux qui réalisent quelles choses ils auraient pu faire mieux, qui voient le tableau d'ensemble et font les choses correctement.

Comme je l'ai dit auparavant, je n'étais pas un expert lorsque j'ai commencé, et des erreurs ont été commises. Mais cela ne m'a pas empêché de faire les choses correctement. Pour tous ceux qui luttent avec leurs propres Macroservices, mini-monolithes, enfer des microservices, je peux vous dire ceci : Pause, prenez une profonde inspiration, faites votre propre diagnostic et améliorez. Il n'est pas trop tard pour faire les choses correctement.