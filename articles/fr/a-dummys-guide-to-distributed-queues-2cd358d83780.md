---
title: Un guide pour les nuls des files d'attente distribuées
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-18T18:07:41.000Z'
originalURL: https://freecodecamp.org/news/a-dummys-guide-to-distributed-queues-2cd358d83780
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Zocw-AFNgC0VDbNWp8dD_g.png
tags:
- name: coding
  slug: coding
- name: Microservices
  slug: microservices
- name: General Programming
  slug: programming
- name: software
  slug: software
- name: 'tech '
  slug: tech
seo_title: Un guide pour les nuls des files d'attente distribuées
seo_desc: 'By Zhia Hwa Chong

  If you’ve ever wondered what Kafka, Heron, real-time streaming, SQS or RabbitMQ
  are all about, then this article is for you. I’ll discuss in detail why we need
  a queue for today’s modern software architecture, what are some common t...'
---

Par Zhia Hwa Chong

Si vous vous êtes déjà demandé ce que sont _Kafka, Heron, le streaming en temps réel, SQS ou RabbitMQ_, alors cet article est pour vous. Je vais discuter en détail pourquoi nous avons besoin d'une file d'attente pour l'architecture logicielle moderne d'aujourd'hui, quelles sont certaines des technologies couramment utilisées, et comment les files d'attente sont couramment utilisées dans l'industrie. Si vous aimez cet article, j'ai [un cours](https://docs.google.com/document/d/1PeK69h4H82rwKjhactiE_sAIorCcZgXgXTY7k-nXpnE/edit#heading=h.hs0b333nsxch) sur la mise à l'échelle des systèmes distribués où je discute de ces sujets plus en détail.

D'accord, commençons !

![Image](https://cdn-media-1.freecodecamp.org/images/K6pTed3Kg7OFpcJQ0Xnw7Et3tZfnBxE7eyYA)
_Un guide pour les nuls des files d'attente_

### Tout d'abord, pourquoi avez-vous besoin d'une file d'attente/courtier de messages ?

#### L'histoire de comment une file d'attente a sauvé les stands de limonade

Imaginez que vous gérez un stand de limonade 🍋, et que vous avez construit une petite application web qui **garde une trace de la fréquence à laquelle vos clients reviennent à votre stand de limonade.**

Votre application web a un endpoint, disons _votrelimonade.com/traffic_, et chaque fois que vous cliquez sur un bouton, le compteur de trafic augmente de 1. Magnifique.

À mesure que le trafic vers votre stand de limonade augmente, vous cliquez sur le bouton de plus en plus. Eh bien, comme vous vivez dans un quartier relativement petit, vous n'avez que 10 à 20 personnes par jour. Vos ventes se déroulent comme d'habitude, l'application web gère le trafic sans problème, et tout va bien. Parfait.

![Image](https://cdn-media-1.freecodecamp.org/images/jrK32XGr77EfzxDmZeW826mPAjdk6UtC2H8M)
_Votre application web de stand de limonade_

#### Le cauchemar d'une entreprise en plein essor

Maintenant que votre stand de limonade s'est fait un nom, des gens de toute la ville affluent pour goûter votre fameuse limonade. Et un beau dimanche matin, les nouvelles locales ont décidé de promouvoir votre stand, et le trafic **EXPLOSE**.

Comme vous pouvez l'imaginer, le trafic vers votre stand de limonade passe de 10 à 20 personnes par jour à 10 000 par jour. Vous appuyez furieusement sur le bouton de trafic, ce qui déclenche un appel à _votrelimonade.com/traffic_, et votre application web continue d'incrémenter la quantité de trafic.

![Image](https://cdn-media-1.freecodecamp.org/images/CAfEJi3inzoxhwfo9TkAfFqZcmEufwwoDwcG)
_L'entreprise de stand de limonade rencontre un goulot d'étranglement_

Malheureusement, votre application web est hébergée sur un serveur 8 bits, 128 Mo de RAM dans votre garage. Avec l'entreprise en plein essor et l'augmentation du trafic, votre application web ne peut plus gérer l'échelle de trafic.

Finalement, votre serveur meurt. ☠️

Avec cela, toute votre application web est mise hors ligne. Vous ne pouvez plus suivre le trafic. Les gens se précipitent, les commandes s'accumulent, pourtant votre application web est hors ligne et vous ne pouvez pas gérer de transactions jusqu'à ce que vous puissiez recommencer à enregistrer le trafic.

![Image](https://cdn-media-1.freecodecamp.org/images/-DgDUsY9jVdJr2WNoenY0K1gyLH1KvM9kw4m)
_Le trafic a mis votre application web hors ligne, et votre entreprise aussi._

Que faites-vous ?

#### La file d'attente à la rescousse

Un moment de génie vous frappe, _et si je place une boîte devant le comptoir où chaque client peut simplement déposer un mot disant qu'il était là ?_

Chaque fois qu'un client entre et passe une commande, vous lui demandez poliment de déposer ses feuilles de commande dans une petite boîte placée devant le comptoir de paiement. Excellent ! Vous avez essentiellement introduit un mécanisme pour garder une trace des arrivées tout en permettant à votre entreprise de fonctionner comme d'habitude.

C'est ce que nous appelons le [_traitement asynchrone_](https://stackoverflow.com/questions/748175/asynchronous-vs-synchronous-execution-what-does-it-really-mean), et, _bienvenue dans le monde des files d'attente_. ✨

![Image](https://cdn-media-1.freecodecamp.org/images/VhVBpQZAbs0L2aVInfL57IzZdEudOuGDv2aA)
_Héros à la rescousse !_

Lorsque vous commencez à construire un logiciel, comme le stand de limonade que j'ai mentionné ci-dessus, il est courant pour une tâche de

1. appeler un service, puis
2. attendre que le service se termine, puis
3. passer à la tâche suivante.

C'est ce qu'on appelle le _traitement synchrone_. Le _traitement asynchrone_, en revanche, permet à une tâche d'appeler un service et de _passer à la tâche suivante_ tandis que le service traite la demande à son propre rythme. C'est pourquoi une file d'attente est une manière élégante de débloquer vos systèmes, car elle place une couche devant vos services et leur permet de traiter les tâches à leur propre rythme.

#### Si une file d'attente est si puissante, pourquoi ne pas simplement la placer devant tout ?

![Image](https://cdn-media-1.freecodecamp.org/images/ogAKQKM90Kep2cU2jneEkMeke7e0SMK28eHC)
_Image courtesy of [imgflip.com](https://imgflip.com/i/2xylc5" rel="noopener" target="_blank" title=")_

Comme toute personne ayant travaillé sur des systèmes distribués peut en témoigner, la mise à l'échelle d'un système distribué est extrêmement délicate et compliquée. Il y a quelques choses à savoir sur les files d'attente qui pourraient rendre une file d'attente peu attrayante pour votre système.

Quelques questions que je poserais avant de décider si une file d'attente est la bonne solution pour vous :

* Votre service a-t-il des problèmes dus à un trafic élevé ? Si ce n'est pas le cas, peut-être devriez-vous examiner ce qui cause le goulot d'étranglement avant de vous lancer dans les files d'attente. Comme l'a dit Donald Knuth, [l'optimisation prématurée est la source de tous les maux](https://en.wikiquote.org/wiki/Donald_Knuth).
* Avez-vous une expertise interne en gestion de files d'attente ? Ou devez-vous potentiellement embaucher une équipe pour le faire pour vous ? Les coûts de maintenance, comme la mise à l'échelle de la file d'attente, peuvent s'envoler si vous n'êtes pas prudent. Il existe des services comme [Amazon SQS](https://aws.amazon.com/sqs/) (Simple Queueing Service) qui offrent une solution _gérée_ (c'est-à-dire que vous n'avez pas besoin de maintenir quoi que ce soit vous-même).
* Est-il possible d'avoir des entrées en double dans la file d'attente ? Si oui, est-ce acceptable ?
* Devez-vous garder une trace de toutes les transactions, au cas où une file d'attente tomberait en panne ?
* Dans le cas où une file d'attente tomberait en panne, la file d'attente doit-elle être capable de rejouer toutes les entrées ? Quelles sont vos options de sauvegarde ?

Il y a beaucoup plus de préoccupations qui pourraient être spécifiques à votre cas d'utilisation, mais espérons que j'ai fait comprendre que l'ajout d'une file d'attente n'est pas aussi facile que de claquer des doigts.

### Comment les files d'attente sont utilisées dans l'architecture moderne

Les files d'attente sont omniprésentes dans l'architecture des systèmes distribués modernes d'aujourd'hui — adoptées dans diverses industries pour différents cas d'utilisation, et il y a de nouveaux cas d'utilisation chaque jour.

Voici quelques cas d'utilisation réels pour les files d'attente :

#### Streaming en temps réel

Lorsque MapReduce est arrivé, c'était un énorme phénomène dans l'industrie car il permettait aux simples mortels de traiter des pétaoctets de données en un temps raisonnable, de quelques jours à quelques heures. Cela peut sembler absurde aujourd'hui lorsque les données sont disponibles en presque quelques secondes, mais avant MapReduce, il n'était pas facile d'extraire des données utilisables à partir de très grands ensembles de données.

L'appétit pour l'analyse de données a grandi, et nous cherchons maintenant à traiter les données en quelques heures, et parfois, en _millisecondes_.

Pour atteindre des analyses et des performances à faible latence de manière continue, le concept de streaming en temps réel a été conçu.

Un exemple utile ici est de penser aux publicités : les publicités sur Twitter, par exemple, sont montrées à des millions de personnes par jour. Pourtant, pour s'assurer que les utilisateurs ne voient pas les mêmes publicités plusieurs fois dans un laps de temps donné, Twitter doit somehow savoir la dernière fois qu'un utilisateur a été exposé à une certaine publicité.

Si nous avions compté sur MapReduce pour effectuer cette action, cela n'aurait même pas été considéré comme une solution car cela prendrait des heures pour traiter toutes ces données. Au lieu de cela, le streaming en temps réel nous permet de traiter les impressions publicitaires à mesure qu'elles arrivent. Tout cela est possible grâce aux files d'attente **qui permettent aux données d'être continuellement diffusées et traitées en temps réel.**

Certaines technologies que vous entendrez souvent dans les cas d'utilisation de streaming en temps réel sont Kafka, Kafka streams, Redis, Spark Streaming (qui est différent de Spark) et ainsi de suite.

#### Architecture pilotée par événements

Les files d'attente sont utilisées comme un composant critique d'une [architecture pilotée par événements](https://en.wikipedia.org/wiki/Event-driven_architecture), ou communément appelée **Pub**(lisher)-**Sub**(scriber). L'architecture pilotée par événements est, selon Wikipedia :

> L'architecture pilotée par événements (EDA), est un modèle d'architecture logicielle promouvant la production, la détection, la consommation et la réaction aux événements.

J'aime à penser à cela comme à l'abonnement à une newsletter : en tant que producteur d'une newsletter, vous savez qui est abonné à votre newsletter et qui ne l'est pas. Vous écrivez le contenu, puis vous l'envoyez à vos abonnés.

D'autre part, en tant qu'abonné, vous pouvez être abonné à plusieurs newsletters, mais vous ne savez pas qui sont les autres abonnés. Mais vous ne vous en souciez pas vraiment. C'est une fonctionnalité vraiment agréable car vous pouvez maintenant écrire un logiciel qui écoute un ensemble d'événements et ne répond qu'à ceux qui vous intéressent.

RabbitMQ et Amazon SQS (Simple Queuing Service) sont quelques-unes des technologies souvent utilisées pour ces types de cas d'utilisation.

#### Infrastructure distribuée, tolérante aux pannes, évolutive

Les systèmes distribués sont sujets aux erreurs, et une file d'attente est l'une des plusieurs façons d'augmenter la résilience de l'architecture. Dans une architecture de microservices (ou [architecture orientée services](https://en.wikipedia.org/wiki/Service-oriented_architecture)), plusieurs microservices communiquent entre eux via des files d'attente en tant qu'interfaces partagées.

Lorsque un microservice tombe en panne de manière inattendue, une file d'attente est toujours capable d'accepter des messages. Cela fournit essentiellement _un tampon_ pour que notre microservice se rétablisse. Une fois que le microservice est de nouveau en ligne, il peut récupérer les messages de la file d'attente et les traiter à nouveau.

Pensez à cela comme à votre boîte aux lettres. Pendant que vous êtes en vacances à Hawaï, le facteur continuera à livrer votre courrier dans la boîte aux lettres. Une fois que vous revenez de vacances, vous pouvez récupérer le courrier et les traiter à votre guise.

Merci d'avoir lu ! J'espère que vous avez appris une ou deux choses sur les files d'attente distribuées grâce à mon article. Si vous avez aimé lire cela, n'hésitez pas à laisser un applaudissement et à rejoindre ma newsletter [ici](http://eepurl.com/dnt9Sf) où j'écris sur les logiciels et les entretiens techniques !

#### Ressources que je recommande

Pour approfondir votre compréhension des files d'attente et des divers sujets mentionnés ci-dessus, je vous recommande vivement les ressources ci-dessous. Ou [**rejoignez mon cours**](https://docs.google.com/document/d/1PeK69h4H82rwKjhactiE_sAIorCcZgXgXTY7k-nXpnE/edit#heading=h.hs0b333nsxch) sur la mise à l'échelle des systèmes distribués pour en apprendre davantage sur les files d'attente :)

* [Designing Data-Intensive Applications](https://amzn.to/2I80wup) : Excellent livre pour apprendre à mettre à l'échelle des systèmes distribués ! Très recommandé.
* [Kafka the Guide](https://amzn.to/2D8FUxS) : J'ai utilisé ce livre comme guide de référence et j'ai apprécié sa description de haut niveau.
* [Kafka Streams](https://www.confluent.io/blog/introducing-kafka-streams-stream-processing-made-simple/) : Il s'agit d'un article informatif de Confluent qui parle en détail de haut niveau de l'implémentation du traitement de flux par Kafka.
* [Elements of Programming Interviews](http://amzn.to/2Dcs6Qd) : Excellent pour résoudre des problèmes de codage.
* [Cracking The Coding Interview](http://amzn.to/2Hj91OH) : Excellent pour couvrir les problèmes de codage fondamentaux en informatique.
* [Daily Coding Problem.com](https://www.dailycodingproblem.com/zhiachong) : Il s'agit d'un site web gratuit à essayer qui offre des problèmes de codage quotidiens gratuits. Vous pouvez vous inscrire pour des défis de codage quotidiens intéressants, et vous pouvez payer pour des solutions si vous le souhaitez. Si vous utilisez mon lien de parrainage ([dailycodingproblem.com/zhiachong](http://www.dailycodingproblem.com/zhiachong)), vous obtenez 10 $ de réduction !

(FYI, je partage plus de ressources sur mon site web : [zhiachong.com](http://www.zhiachong.com/resources) où j'ai personnellement testé et recommandé pour les ingénieurs logiciels de tous niveaux.)

Santé !