---
title: 'Entre les fils : Une interview avec Nolan Lawson, responsable de la performance
  de Microsoft Edge'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-06-20T13:01:37.000Z'
originalURL: https://freecodecamp.org/news/between-the-wires-an-interview-with-microsoft-edge-performance-pm-nolan-lawson-ca3240dec2eb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ozpkWNHda_nU62_3VGakQA.png
tags:
- name: Microsoft
  slug: microsoft
- name: open source
  slug: open-source
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: 'Entre les fils : Une interview avec Nolan Lawson, responsable de la performance
  de Microsoft Edge'
seo_desc: 'By Vivian Cromwell

  I interviewed Nolan Lawson, Web Performance PM at Microsoft Edge. He also maintains
  the popular open source library PouchDB together with others.

  Tell us a little bit about your childhood and where you grew up.

  I grew up in a small...'
---

Par Vivian Cromwell

_J'ai interviewé Nolan Lawson, responsable de la performance Web chez [Microsoft Edge](https://www.microsoft.com/en-us/windows/microsoft-edge#x2QP2K1csjiH2CwS.97). Il maintient également la bibliothèque open source populaire [PouchDB](https://github.com/pouchdb/pouchdb) avec d'autres._

#### Parlez-nous un peu de votre enfance et de l'endroit où vous avez grandi.

J'ai grandi dans une petite ville navale appelée Bremerton, près de Seattle. J'ai eu une enfance assez typique de la classe moyenne : mon beau-père travaillait pour le chantier naval, et ma mère était infirmière scolaire puis enseignante.

Enfant, j'étais un lecteur vorace. J'ai lu beaucoup de livres de fantasy et d'horreur, de la série Narnia à tout ce qui est de Stephen King. Mes professeurs étaient suspicieux que je lise des romans d'horreur pour adultes, mais ils le toléraient parce qu'au moins je lisais. J'étais aussi très passionné par les jeux vidéo.

J'ai une grande appréciation pour les activités de plein air grâce à une expérience précoce dans les Boy Scouts. J'ai aussi visité la France beaucoup parce que mon père biologique est français. Cela m'a donné un peu le virus du voyage, et en tant qu'adulte, j'ai déménagé à Ottawa, puis à Genève, puis à New York avant de revenir à Seattle. J'ai déménagé tous les quelques années, juste sur un coup de tête.

![Image](https://cdn-media-1.freecodecamp.org/images/DcQlRBIlmb8qa5V1kVGSYMmlRPmJZd6dyGo7)
_(Nolan, 2009)_

À un moment donné, j'ai réalisé qu'il serait bon de rentrer chez moi et d'être plus proche de ma famille. Ma petite amie voulait aussi s'installer là-bas, car c'est de là que vient sa famille. J'ai commencé à chercher des emplois autour de Seattle, et Microsoft est devenu un choix assez évident.

#### Parlez-nous un peu de votre première expérience en programmation.

Quand j'avais six ou sept ans, mon oncle m'a donné un ordinateur MS-DOS d'occasion avec un lecteur de disquettes de 5¼ pouces. Il était ancien selon les normes d'aujourd'hui. Il avait essentiellement deux jeux : [Snake](https://en.wikipedia.org/wiki/Snake_(video_game)) et [Gorillas](https://en.wikipedia.org/wiki/Gorillas_(video_game)), et il affichait en fait le code BASIC avant qu'ils ne démarrent. Ces deux jeux étaient tout ce que je pouvais faire avec.

![Image](https://cdn-media-1.freecodecamp.org/images/WDEwCruaYCNHwnMclV8mql1ojpcm2GGQxgND)
_(Disquettes de 8 pouces, 5¼ pouces et 3½ pouces)_

![Image](https://cdn-media-1.freecodecamp.org/images/0dMk0hq3xNcQHzK-0nCW0jMB0ZrKemPeLAbo)
_(Gorillas, est un [jeu vidéo](https://en.wikipedia.org/wiki/Video_game" rel="noopener" target="_blank" title="Video game">jeu vidéo</a> d'abord distribué avec <a href="https://en.wikipedia.org/wiki/MS-DOS" rel="noopener" target="_blank" title="MS-DOS">MS-DOS 5</a> et publié en 1991 par <a href="https://en.wikipedia.org/wiki/IBM" rel="noopener" target="_blank" title="IBM) corporation.)_

> « Je ne suis pas retourné à la programmation avant d'être à l'université. »

J'avais aussi un livre sur la programmation MS-DOS, alors j'ai pris le temps d'écrire un script Batch vraiment simple. Quand l'ordinateur démarrait, il imprimait :

« Salut, Nolan. À quel jeu veux-tu jouer ? 1. Gorillas 2. Snake ? »

Et tu tapais un ou deux selon le jeu auquel tu voulais jouer. J'étais assez fier de ce script !

Quand j'avais environ neuf ans, ma garderie avait un ordinateur similaire avec encore plus de jeux, alors j'ai décidé d'y appliquer mes compétences en Batch. Malheureusement, j'ai abîmé l'ordinateur et j'ai fait en sorte que tu ne puisses plus jouer aux jeux. Je me sentais coupable et cela m'a un peu effrayé. Je ne suis pas retourné à la programmation avant d'être à l'université.

En tant qu'étudiant de premier cycle, j'ai étudié la linguistique, surtout parce que j'apprenais le français et le japonais à l'époque. J'étais fasciné par les langues. Mais après l'obtention de mon diplôme, j'ai réalisé qu'il était assez difficile de trouver un emploi en linguistique. Cependant, il s'est avéré que mon département à l'Université de Washington avait un programme de maîtrise en [linguistique computationnelle](http://www.compling.uw.edu/), ce qui semblait être une excellente option pour ma carrière. C'est ainsi que je suis finalement retourné à la programmation.

#### Qu'est-ce qui vous a motivé à vous impliquer avec PouchDB ?

Vers 2012, je travaillais pour une ONG à Genève. Nous construisions une application web pour un client qui utilisait [CouchDB](http://couchdb.apache.org/). Plus tard, j'ai commencé à jouer avec CouchDB pour un projet parallèle. Grâce à cela, j'ai trouvé [PouchDB](https://pouchdb.com), qui pouvait synchroniser les données entre CouchDB sur le serveur et I[ndexedDB](https://www.w3.org/TR/IndexedDB/) dans le navigateur. Je trouvais cela incroyable.

![Image](https://cdn-media-1.freecodecamp.org/images/-I1pVz6qggeWXaw9j5joKnO2loJD-cgvyNdu)
_(Logo Pouchdb)_

En travaillant sur ce projet, j'ai remarqué quelques bugs dans PouchDB. J'ai réalisé que je connaissais assez Android et JavaScript pour résoudre ces bugs. Finalement, j'ai fini par corriger plus de bugs et contribuer plus fréquemment au projet. Début 2014, je suis devenu l'un des principaux [contributeurs](https://github.com/pouchdb/pouchdb/graphs/contributors), et je le suis encore aujourd'hui.

L'histoire de la création de PouchDB est assez intéressante. En 2010, [Mikeal Rogers](https://twitter.com/mikeal) a fait cette expérience ponctuelle appelée [IDBCouch](https://github.com/pouchdb/pouchdb/commit/d600081962d3f54b410e5cfcf78cd413ad94abb9), qui ne fonctionnait que dans Firefox Nightly parce que IndexedDB était si nouveau à l'époque. [Max Ogden](https://twitter.com/denormalize) l'a ensuite renommé PouchDB, lorsqu'il faisait du shopping pour des vélos à San Francisco et a eu l'idée du nom « [Portable Couch](https://twitter.com/denormalize/status/452906716426797056) ». Ensuite, [Dale Harvey](https://twitter.com/daleharvey), qui travaille chez Mozilla, a repris le projet et a fait un énorme travail pour le faire fonctionner correctement dans Firefox et Chrome.

![Image](https://cdn-media-1.freecodecamp.org/images/DMfm-Vx-CwifH3abhcmKnCEK9BrxhkuBEwtY)
_(source : [https://twitter.com/denormalize/status/452906716426797056)](https://twitter.com/denormalize/status/452906716426797056)" rel="noopener" target="_blank" title=")_

Quand je suis arrivé sur le projet fin 2013, je voulais que PouchDB fonctionne dans tous les navigateurs, comme jQuery mais pour les bases de données. Je pensais que les gens devraient pouvoir l'utiliser et qu'il devrait « simplement fonctionner » sur les anciennes versions d'Android, IE et Safari. Beaucoup de mes premiers travaux portaient sur la compatibilité multi-navigateurs, ce qui a vraiment aidé PouchDB à devenir plus populaire.

PouchDB est un bon exemple de ce que les auteurs d'IndexedDB avaient initialement prévu lorsqu'ils ont écrit la spécification. Ils voulaient que les gens construisent des bibliothèques par-dessus, dans l'esprit du [manifest de l'extensible web](https://www.w3.org/community/nextweb/2013/06/11/the-extensible-web-manifesto/). L'auteur original de la spécification, Nikunj Mehta, s'est même demandé si quelqu'un écrirait un « JavaScript CouchDB ». Aujourd'hui, il existe de nombreuses bibliothèques intéressantes construites sur IndexedDB, y compris PouchDB, [localForage](https://github.com/localForage/localForage), [Dexie.js](http://dexie.org/) et [Lovefield](https://github.com/google/lovefield), qui offrent une expérience plus conviviale pour les développeurs.

#### PouchDB a-t-il cherché des financements auprès de grandes entreprises et de la communauté ?

> « J'ai toujours eu cette notion quelque peu idéaliste que PouchDB devrait être un projet de passion qui n'est pas corrompu par l'argent. Je ne veux pas être influencé par une organisation ou une autre pour le pousser dans une direction particulière. Il devrait être ce qui est le mieux pour les utilisateurs. »

Nous avons essayé de chercher des financements assez tôt, vers 2013. Dale a mis en place un système de primes où chaque problème GitHub pouvait avoir une note disant : « Hé, si vous résolvez ce problème, il y a une prime. » Il y avait quelques problèmes avec cela.

Des personnes aléatoires pouvaient venir et soumettre une PR pour corriger l'un des problèmes de prime. Je me souviens d'un problème où la PR ne le corrigait pas tout à fait, mais elle était à moitié faite, alors je suis intervenu et j'ai corrigé l'autre moitié. À ce moment-là, il n'était pas clair à qui la prime devait aller. Devait-elle être divisée en deux ? À la fin, la personne qui avait offert la prime ne l'a même pas payée. Donc ce système n'a pas très bien fonctionné, et nous l'avons abandonné.

Aujourd'hui, PouchDB a grandi pour compter [plus de 200 contributeurs](https://github.com/pouchdb/pouchdb/graphs/contributors), mais essentiellement Dale est le [BDFL](https://en.wikipedia.org/wiki/Benevolent_dictator_for_life) et je suis le lieutenant. Récemmment, nous avons relancé [la discussion sur le financement](https://github.com/pouchdb/pouchdb/issues/6229), mais nous devons d'abord mettre en place un modèle de gouvernance formel. Cela est particulièrement important pour les entreprises. IBM, qui est fortement investi dans CouchDB via [Cloudant](https://cloudant.com/), veut pouvoir dire à ses clients que CouchDB et PouchDB sont des solutions solides à leurs problèmes. Cependant, alors que CouchDB est sous la [Fondation Apache](https://www.apache.org/) et a un modèle de gouvernance très clair, PouchDB n'en a pas. Donc certains clients entreprises pourraient être un peu préoccupés par cela.

![Image](https://cdn-media-1.freecodecamp.org/images/on2oDhIu6kwJ0DOA1XHcst1TYO1Wk5HT9kq3)
_(Réunion de l'équipe PouchDB 2015, Nolan Lawson, Gregor Martynus et Calvin Metcalf)_

J'ai toujours eu cette notion quelque peu idéaliste que PouchDB devrait être un projet de passion qui n'est pas corrompu par l'argent. Je ne veux pas être influencé par une organisation ou une autre pour le pousser dans une direction particulière. Il devrait être ce qui est le mieux pour les utilisateurs. Nous en sommes à ce point dans la maturité du projet, cependant, où nous devons commencer à poser les questions difficiles. Par exemple, nous voulons déterminer comment lever et distribuer de l'argent afin de pouvoir le donner équitablement aux contributeurs. Nous explorons des options en ce moment, mais nous ne nous sommes engagés à rien pour l'instant.

#### Qu'avez-vous appris du projet PouchDB en matière de durabilité de l'OSS ?

> « C'est pourquoi je pense qu'il est important de se souvenir de ce que c'est que d'être un débutant. Quand on commence, même parler à un mainteneur open-source peut être intimidant. »

PouchDB était mon premier grand projet open-source. Je dois rendre hommage à Dale ; il a été mon mentor dès le début. Il m'a enseigné toutes les bases de la façon d'interagir dans un projet open-source.

![Image](https://cdn-media-1.freecodecamp.org/images/ISe7NhaKFWOLCtS1lKEUdlCD8betMovXfUxO)
_(Dale Harvey)_

Au début, même juste parler à Dale Harvey sur IRC était intimidant. Il était du genre à donner des conférences ; les gens le respectaient. J'étais juste un inconnu sur Internet. Mais Dale est toujours très patient avec les nouveaux contributeurs. Il répond aux questions et aux problèmes de tout le monde. Même s'il pense qu'une idée est mauvaise, il le dira gentiment. Petit à petit, j'ai réalisé que Dale est juste un être humain normal, et il est heureux d'avoir des gens impliqués dans le projet.

![Image](https://cdn-media-1.freecodecamp.org/images/4t5Q8TMfJLwYx5z-Ad6mGAbrsI0TK7p1Zd1d)
_(Dale commentant un problème sur Github)_

C'est pourquoi je pense qu'il est important de se souvenir de ce que c'est que d'être un débutant. Quand on commence, même parler à un mainteneur open-source peut être intimidant. J'ai appris de Dale à être un mainteneur attentionné et à toujours encourager les gens à contribuer.

Aujourd'hui, PouchDB est très mature, et il nécessite une énorme quantité de connaissances pour commencer, ce qui est un défi pour les nouveaux contributeurs. Une chose que j'aimerais corriger est de le rendre un peu plus facile pour les nouveaux venus de se joindre à nous. C'est quelque chose que je pense manquer en ce moment.

#### « Offline first » est quelque chose dont nous parlons depuis 2010. Pensez-vous que nous sommes enfin prêts pour cela ? Quels sont les principaux défis aujourd'hui ?

L'offline est vraiment difficile. C'est l'une de ces choses qui manque même dans une éducation universitaire en informatique. Ce que les gens ne réalisent pas, c'est que lorsque vous construisez une application offline-first, vous construisez essentiellement un système distribué : client et serveur. Juste en stockant des données sur ces deux nœuds, vous avez tous les problèmes théoriques du [théorème CAP](https://en.wikipedia.org/wiki/CAP_theorem) : cohérence, disponibilité et tolérance aux partitions — choisissez-en deux.

Donc si vous construisez ce genre de système, mais que vous ne le réalisez pas en y entrant, vous allez probablement finir par bricoler quelque chose. Vous pouvez penser avoir atteint 100 % du chemin, mais vous n'avez vraiment atteint que 90 %, et les 10 % restants peuvent prendre des années à terminer. Cela a pris des années pour corriger tous les cas limites dans PouchDB.

L'une des choses que nous essayons de faire avec PouchDB est de sensibiliser et d'aider les gens à réfléchir aux problèmes inhérents à l'architecture offline-first. PouchDB a un concept intégré de gestion des conflits, car CouchDB a réfléchi à ces problèmes dès le début. Il est conçu avec le modèle de [contrôle de concurrence multiversion](https://en.wikipedia.org/wiki/Multiversion_concurrency_control), qui répond à la question de ce qui se passe lorsque le client et le serveur se désynchronisent.

L'expérience utilisateur est un autre gros problème qui n'a pas vraiment été résolu dans l'offline-first. Je pense que de nouveaux modèles comme les [Progressive Web Applications](https://developers.google.com/web/progressive-web-apps/) nous forceront à commencer à réfléchir à la manière de communiquer cela aux utilisateurs. Il y a un [excellent article](https://medium.com/@jessebeach/my-biggest-takeaway-from-the-second-offline-camp-in-santa-margarita-ca-d0dd930cd02b#.rkrwj3sbw) de [Jesse Beach](https://twitter.com/jessebeach) où elle parle de la manière de communiquer efficacement les états offline, et lors du [Offline Camp](http://offlinefirst.org/camp/), nous avons discuté de certaines de ces techniques, comme le passage de l'interface utilisateur en niveaux de gris lorsque l'application passe en mode offline. Ce n'est pas aussi négatif ou choquant qu'une alerte, mais c'est une indication subtile que vous êtes offline.

![Image](https://cdn-media-1.freecodecamp.org/images/c5AOMBb5HKWNqG1REFEHweBRBJhKCbMb7bo8)
_(Nolan à l'Offline Camp avec Jesse Beach et d'autres, 2016)_

Il y a eu beaucoup de progrès sur l'offline first, mais c'est toujours définitivement un problème non résolu.

#### Qu'est-ce qui vous a décidé à rejoindre l'équipe Microsoft Edge ? Quelle est votre impression des six premiers mois, passant d'une petite startup à une grande organisation ?

> « Mais il y a un sentiment général dans toute l'entreprise maintenant que lorsque nous sommes transparents et que nous cherchons des retours de la communauté, cela fonctionne bien pour nous. »

Je suis venu chez Microsoft Edge parce que je voulais aider à améliorer la plateforme web. Je pensais que ce serait une bonne opportunité de développer beaucoup des standards pour lesquels je suis passionné. Par exemple, nous sommes en train de développer les [Service Workers](https://www.w3.org/TR/service-workers/) et les [Progressive Web Apps](https://developers.google.com/web/progressive-web-apps/), ainsi que des améliorations pour IndexedDB. Je voulais être sur le terrain pour voir ces choses se réaliser.

Microsoft est fascinant à observer car c'est une entreprise en transition. Elle passe d'être assez fermée à être beaucoup plus ouverte. Certaines équipes ont adopté cette ouverture plus que d'autres, et même certaines personnes au sein de la même équipe. Mais il y a un sentiment général dans toute l'entreprise maintenant que lorsque nous sommes transparents et que nous cherchons des retours de la communauté, cela fonctionne bien pour nous.

Je suis toujours activement impliqué dans le projet PouchDB, mais je tends à garder mon travail chez Microsoft et PouchDB séparés. Je trierai les problèmes GitHub en allant au travail, puis je ferai un peu de programmation pour PouchDB le soir ou le week-end. Mais je trouve que ces deux aspects se mélangent de plus en plus, de manière positive. Par exemple, je peux trouver un bug dans IndexedDB sur Edge en travaillant sur des problèmes de PouchDB.

#### Parlez-nous d'une journée dans la vie d'un responsable de la performance chez Microsoft Edge.

Je fais partie de l'équipe de performance, donc la plupart de mon travail consiste à identifier les problèmes de performance dans le navigateur et à communiquer ces problèmes aux développeurs web et à l'équipe du navigateur.

![Image](https://cdn-media-1.freecodecamp.org/images/mpPH0J5HAWkmwWVq4gzfvclaUv8Tyr8ZDZuX)
_(Nolan avec Todd Reifsteck et Rob Hwacinski de l'équipe Microsoft Edge)_

Un projet sur lequel je travaille est « Performance Clubs », où nous invitons des équipes web à venir discuter de la performance de leur site. Habituellement, ce sont des sites Microsoft comme Outlook.com et MSN, mais parfois ce sont aussi des partenaires externes. Lorsqu'ils viennent, nous faisons une analyse approfondie de la performance du site web en utilisant les mêmes outils que ceux que nous utilisons pour construire le navigateur lui-même. Ensuite, nous leur donnons des conseils de performance afin qu'ils puissent retourner et rendre leurs sites web plus rapides. Je dépose également les problèmes signalés par les auteurs de sites et j'écris des cas de test.

Les clubs de performance sont privés pour l'instant. Tout le monde ne veut pas prendre les aspects de leurs sites web dont ils ne sont pas fiers et les exposer publiquement ; c'est comme étaler son linge sale. Il y a eu quelques discussions sur l'anonymisation et la publication des données, mais c'est incroyablement difficile à faire sans révéler le site que vous analysez. Il y a eu une récente controverse sur les audits de performance publics ; ce n'est pas toujours bien accueilli.

#### Comment les fournisseurs de navigateurs et les auteurs de frameworks peuvent-ils collaborer plus étroitement sur la performance web, étant donné que cela a été une discussion animée récemment ?

> « ...les personnes qui peuvent apporter le plus de valeur ici sont les auteurs de bibliothèques et de frameworks JavaScript. Ils sont dans une position où ils peuvent être impartiaux et comparer les performances entre les navigateurs, ce qui est extrêmement précieux pour les fournisseurs de navigateurs. »

Je pense qu'il est important pour les développeurs web de comprendre pourquoi la performance est un sujet si délicat. Les navigateurs ne rivalisent pas sur les fonctionnalités de l'API — nous avons arrêté de le faire lorsque nous avons convenu de mettre en œuvre les standards web — mais les navigateurs rivalisent sur la performance. La vitesse est un argument de vente énorme pour un navigateur. Chaque navigateur prétend être le plus rapide, un peu comme McDonald's et Burger King prétendent chacun avoir les meilleurs burgers. Évidemment, ils ne peuvent pas tous les deux avoir raison.

En général, les fournisseurs de navigateurs ne parlent publiquement que de ce qu'ils font bien. Si vous parlez en privé avec quelqu'un qui travaille sur une équipe de navigateur, il peut facilement vous dire 50 choses que le navigateur fait bien et 50 choses qu'il ne fait pas bien ; il les connaît par cœur. Mais publiquement, nous avons tendance à ne parler que des choses que nous faisons bien, car il y a des implications commerciales.

Par exemple, lorsque l'équipe WebKit sort le benchmark [Speedometer](https://goo.gl/NLU9ch) ou le benchmark [MotionMark](https://webkit.org/blog/6943/motionmark-a-new-graphics-benchmark/), il n'est pas surprenant que Safari gagne. De même, lorsque Microsoft écrit un article de blog sur la façon dont nous avons un excellent moteur JavaScript, nous avons tendance à parler de [Octane](https://github.com/chromium/octane) et de [JetStream](https://webkit.org/blog/3418/introducing-the-jetstream-benchmark-suite/). Sans surprise, nous gagnons sur ces benchmarks.

Je pense que les personnes qui peuvent apporter le plus de valeur ici sont les auteurs de bibliothèques et de frameworks JavaScript. Ils sont dans une position où ils peuvent être impartiaux et comparer les performances entre les navigateurs, ce qui est extrêmement précieux pour les fournisseurs de navigateurs. Malheureusement, je pense que beaucoup d'entre eux pourraient faire mieux sur ce point.

Il y a beaucoup d'intérêt pour la performance web aujourd'hui, et vous voyez de nombreux frameworks JavaScript rivaliser les uns avec les autres sur la performance — [React](https://github.com/facebook/react), [Inferno](https://github.com/infernojs/inferno), [Preact](https://github.com/developit/preact), [Vue](http://vuejs.org/), [Svelte](http://svelte.technology/), etc. Mais lorsque vous regardez leurs benchmarks, ils ne testent souvent que dans Chrome ou peut-être Mobile Safari. Parfois, ils ne spécifient même pas dans quel navigateur ils testent, donc vous devez simplement supposer que c'est Chrome.

Un framework qui va à contre-courant de cette tendance, que j'aime vraiment, est [Ember](http://emberjs.com/). Ils ont créé leur propre benchmark, le [Ember Benchmark](http://emberperf.eviltrout.com/), et ils vont parfois sur Twitter et peut-être [susciter quelques sourcils](https://twitter.com/stefanpenner/status/542160874950389760) en soulignant que Chrome ne se comporte pas aussi bien sur leurs benchmarks que Safari.

C'est un excellent retour pour les fournisseurs de navigateurs. Même si nous n'envoyons pas de signaux publics sur ce que nous pensons du benchmark, nous pouvons l'utiliser en interne et travailler dur pour améliorer notre navigateur. J'aimerais voir plus de benchmarks multi-navigateurs et plus de reconnaissance de la part des auteurs de frameworks JavaScript qu'il est précieux de tester sur plusieurs navigateurs. C'est la grande chose que je vois manquer en ce moment.

Edge a une assez bonne part de marché des navigateurs ; elle s'améliore de toute façon. Je ne pense pas qu'il soit sûr d'ignorer simplement les navigateurs parce qu'ils ont une part de marché trop faible, surtout parce que beaucoup de développeurs web ont une perception très biaisée de ce qu'est la part de marché. Windows est le système d'exploitation dominant dans le monde ; il est utilisé par environ [90 % de tous les utilisateurs de bureau](https://www.netmarketshare.com/operating-system-market-share.aspx?qprid=10&qpcustomd=0). Et Android est [le système d'exploitation mobile le plus populaire sur la planète](https://www.netmarketshare.com/operating-system-market-share.aspx?qprid=8&qpcustomd=1) de loin.

Si vous ne regardez que les conférences de développeurs web, cependant, vous pourriez être pardonné de penser que le monde est purement Mac, ou que tout le monde utilise Chrome, ou que la plupart des gens portent un iPhone. Mais la réalité est bien différente. Je dirais que les développeurs web rendent un mauvais service à leurs utilisateurs s'ils vivent dans cette bulle et supposent que tout le monde vit aussi dans cette bulle.

#### Quels autres passe-temps ou intérêts avez-vous en dehors de la programmation ?

Je joue un peu de guitare et je chante un peu, surtout pour moi-même. J'ai une chaîne YouTube où je poste certaines de [mes performances](https://www.youtube.com/watch?v=RNeueQf3bNY). Je ne me produis pas en public.

#### Je suis vraiment intéressé par les e-sports. Je passe beaucoup de temps à regarder des tournois de [Super Smash Brothers](https://en.wikipedia.org/wiki/Super_Smash_Brothers_Melee) ou à regarder des speedruns de jeux vidéo. Les speedruns me rappellent beaucoup la performance des navigateurs. Vous essayez d'optimiser cette chose pour qu'elle aille le plus vite possible, et parfois vous trichez un peu, comme en faisant passer votre personnage à travers un mur. Parfois, je trouve qu'un site web bien optimisé est comme un speedrun bien optimisé — vous trichez un peu pour avancer. C'est un peu drôle de voir les parallèles.

#### Qui sont vos héros de la programmation ?

J'admire vraiment [D. Richard Hipp](https://en.wikipedia.org/wiki/D._Richard_Hipp), le créateur de SQLite, qui est probablement la base de données la plus populaire sur la planète. SQLite est un logiciel rigoureux avec 745 fois plus de [code de test](https://www.sqlite.org/testing.html) que de code. Vous pourriez envoyer cette chose sur la lune.

Richard Hipp est aussi une sorte d'homme de la Renaissance de la programmation ; il a implémenté beaucoup de choses intéressantes. Il a écrit une version complète du système de contrôle de version appelée [Fossil](http://fossil-scm.org/index.html/doc/trunk/www/index.wiki). Il n'était pas satisfait de Git, alors il a écrit un système de contrôle de version entier, et c'est le système de contrôle de version utilisé pour SQLite.

Si vous regardez le code source de SQLite, vous trouverez également ma licence open source préférée de tous les temps, qui dit « À la place d'une licence, je vous offre cette prière. » C'est vraiment beau, comme un poème.

![Image](https://cdn-media-1.freecodecamp.org/images/M5a003xVI5ySf9ITtKpEJERnvp1RDkArGAUz)
_(Fichier de licence SQLite ❤)_

Et pourtant, malgré son succès, Hipp est aussi incroyablement humble. Il ne se vante jamais dans aucune interview. Je trouve cela inspirant de voir quelqu'un qui est si humble, et pourtant si compétent dans le monde du logiciel.

Ce projet est rendu possible grâce aux parrainages de [frontendmasters.com](https://frontendmasters.com/), [egghead.io](https://egghead.io/), [Microsoft Edge](https://www.microsoft.com/en-us/windows/microsoft-edge) et [Google Developers](https://developers.google.com/).

![Image](https://cdn-media-1.freecodecamp.org/images/QYUKqPLrpAiZJxfgqEJyneUk93fYszW3hVLg)
_Nos sponsors._

[Faire un don pour soutenir ce projet](https://opencollective.com/betweenthewires).

Pour suggérer un créateur que vous aimeriez entendre, veuillez remplir ce [formulaire](https://goo.gl/forms/XhR1IyLXJHNMljcp1).

Vous pouvez également envoyer des commentaires à [betweenthewires](https://twitter.com/betweenthewires) sur Twitter.