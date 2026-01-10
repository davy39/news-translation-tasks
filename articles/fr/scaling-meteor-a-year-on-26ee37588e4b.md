---
title: J'utilise Meteor à grande échelle depuis un an. Voici ce que j'ai appris.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-12-12T07:00:08.000Z'
originalURL: https://freecodecamp.org/news/scaling-meteor-a-year-on-26ee37588e4b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3eK5Q-ZuwVoik8q-Wbgl1g.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Meteor
  slug: meteor
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: Web Development
  slug: web-development
seo_title: J'utilise Meteor à grande échelle depuis un an. Voici ce que j'ai appris.
seo_desc: 'By Elie Steinbock

  A year ago I wrote an article describing my first experiences scaling Meteor. In
  short, I created a popular fantasy football website using Meteor. At a certain point,
  my service started slowing down. The single server I had running ...'
---

Par Elie Steinbock

Il y a un an, j'ai écrit un article décrivant [mes premières expériences de mise à l'échelle de Meteor](https://medium.com/@eliezer/first-experiences-scaling-a-meteor-app-14a48e62a4af). En bref, j'ai créé un site web populaire de fantasy football en utilisant [Meteor](https://www.meteor.com/). À un certain moment, mon service a commencé à ralentir. Le seul serveur que j'avais pour faire tourner le jeu ne pouvait plus gérer la charge. J'ai pu résoudre ces premiers problèmes de mise à l'échelle en ajoutant, entre autres, des serveurs supplémentaires.

Eh bien, lorsque la nouvelle saison de football de l'été dernier est arrivée, j'ai de nouveau rencontré des problèmes de mise à l'échelle. Ajouter plus de serveurs seul ne résoudrait pas ces problèmes. Mais j'ai réussi à les surmonter.

Cet article expliquera les choses que j'ai apprises cette fois-ci, divisées en six conseils pratiques.

Une chose qui a changé depuis mon dernier article est que le Meteor Development Group a enfin publié [Galaxy](https://www.meteor.com/hosting), qui vous offre l'hébergement Meteor à 29 $ par conteneur par mois. Cela n'inclut pas l'hébergement de la base de données, mais vous pouvez utiliser quelque chose comme [Compose](https://www.compose.com/) ou [mLab](https://mlab.com) pour cela. Alternativement, vous pouvez auto-héberger la base de données sur [AWS](https://aws.amazon.com/) ou [DigitalOcean](https://m.do.co/c/2518a67f26c8). Cela sera moins cher, mais nécessitera plus de travail de votre part.

J'utilise moi-même [DigitalOcean](https://m.do.co/c/2518a67f26c8) pour l'hébergement. Le site fonctionne sur des droplets à 5 $/mois, 512 Mo avec une instance Meteor par droplet. J'utilise [Meteor Up](https://github.com/kadirahq/meteor-up) (Mup) pour le déploiement et Compose.io pour l'hébergement de la base de données.

Que vous choisissiez DigitalOcean ou Galaxy dépend de vous. Galaxy fera beaucoup de choses pour vous et vous fera gagner du temps. Opter pour DigitalOcean vous fera économiser 24 $ par conteneur par mois. Pour de nombreuses entreprises, choisir Galaxy a le plus de sens puisque les salaires des développeurs seront bien plus élevés. Dans tous les cas, je vous laisse prendre les décisions commerciales.

Passons à autre chose. Il y a quelques choses qui ont vraiment aidé à mettre à l'échelle notre application Meteor cet été. Nous avons eu quelques mauvais jours. Ce n'était vraiment pas toujours facile, mais nous nous en sommes sortis.

### Un résumé des leçons apprises

Voici les principales leçons que j'ai tirées de mon année de mise à l'échelle :

Leçon #1 : Les index MongoDB sont super importants !

Leçon #2 : Avoir trop d'instances Meteor est un problème !

Leçon #3 : Ne vous inquiétez pas de la mise à l'échelle de Nginx.

Leçon #4 : Déconnectez les utilisateurs lorsqu'ils sont absents depuis un moment

Leçon #5 : Will Griggs est en feu

Leçon #6 : Prenez exemple sur la façon dont ils ont mis à l'échelle Pokemon Go

Passons en revue ces leçons une par une.

### Leçon #1 : Les index MongoDB sont super importants !

C'était une erreur de débutant. Chaque article sur la mise à l'échelle de Meteor (ou MongoDB) vous dit d'utiliser des index. Et je l'ai fait ! Mais un index manquait, et j'en ai payé le prix — vraiment payé le prix — lors de la nuit la plus importante de l'année pour nous.

Expliquer les index par l'exemple. Si vous avez 10 000 scores de joueurs et que vous voulez trouver le score le plus élevé, dans un cas normal Mongo devrait parcourir tous ces scores pour trouver le plus élevé. Si vous avez un index sur le score, alors Mongo sauvegarde une copie de tous les scores dans l'ordre ascendant ou descendant, et trouvera le score le plus élevé en une fraction de temps. Vous pouvez en lire plus sur les index sur le site de MongoDB [website](https://docs.mongodb.com/v3.0/core/indexes-introduction/).

Dans un projet Meteor, je recommande d'avoir un fichier _publications.js_ qui contient toutes vos publications. Sous chaque publication, vous devriez avoir du code qui crée l'index nécessaire pour chaque publication. Le code pour créer un index dans Meteor ressemble à ceci :

```
Meteor.startup(function () {    Teams._ensureIndex({ userId: 1 });});
```

Le champ __id_ a un index par défaut, donc vous n'avez pas à vous en soucier.

Entrons dans les détails. J'utilise [Compose.io](http://compose.io) pour l'hébergement MongoDB. Ils ont été corrects, et le support a également été acceptable, mais ne les écoutez pas lorsqu'ils pensent que tous vos problèmes peuvent être résolus en ajoutant plus de RAM. Ce n'est pas vrai. Cela peut marcher parfois, mais dans mon cas, c'était juste un conseil absurde.

J'utilise [Kadira.io](https://kadira.io/) pour la surveillance des performances. Chaque application Meteor devrait utiliser Kadira et le package de base est génial et gratuit, donc il n'y a aucune raison de ne pas le faire. (Mise à jour : Kadira est toujours un choix évident pour les applications Meteor, mais l'équipe derrière Kadira s'est récemment éloignée de Meteor, donc méfiez-vous de cela pour l'avenir.)

Dans Kadira, je voyais des graphiques comme ceux-ci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*a2zC8xn8kHwzmwqZt71FGQ.png)
_Temps de réponse super lent de 21:48 à 22:08_

À un certain moment, le temps de réponse PubSub et Methods devient ridiculement long. Tout ce qui dépasse 1 000 ms pour répondre est problématique. Même un temps de réponse de 500 ms peut être mauvais. Mais 10 à 20 secondes en tant que temps de réponse moyen pendant une heure signifie que vos utilisateurs vous détestent et que votre application fonctionne à peine pour eux.

En général, lorsque les choses fonctionnent lentement, j'ajoute simplement plus de serveurs. Et je l'ai fait ici aussi, sauf que cette fois, ajouter plus de serveurs a simplement empiré les choses. Bien pire. Mais nous y viendrons plus tard.

À ce stade, ce que vous faites, c'est que vous fouillez Google et spammez StackOverflow et les [forums Meteor](https://forums.meteor.com/t/mongo-scaling-issues/27905/24).

Finalement, je suis tombé sur ce joyau dans les tableaux de bord de Kadira :

![Image](https://cdn-media-1.freecodecamp.org/images/1*SbqyKPt9frd79CU78BCA5w.png)
_La base de données met une éternité à répondre_

De cela, nous voyons que la base de données met une éternité à répondre. Ajouter plus d'instances Meteor ne va pas nous aider ici. Nous devons régler le problème avec Mongo.

Kadira n'était pas bon pour me montrer pourquoi la base de données répondait si lentement. Chaque publication et méthode montrait un temps de réponse de la base de données très élevé.

La réponse est venue en visitant Compose.io aux heures de pointe. Sur le tableau de bord, vous pouvez jeter un coup d'œil aux ops actuelles (opérations en cours) qui s'exécutent à tout moment. J'ai vu quelque chose comme ceci (mais bien pire) :

![Image](https://cdn-media-1.freecodecamp.org/images/1*SYQNcLUYWSwj_BKlBhdjUg.png)

Je n'avais aucune idée de ce que signifiait tout ce charabia, mais vous verrez que chaque op a un champ _secs_running_. Dans l'image ci-dessus, il est indiqué 0 seconde pour tout, ce qui est génial ! Mais ce que je voyais pendant les heures de pointe était 14 secondes, 9 secondes, 10 secondes... pour les différentes opérations qui étaient en cours ! Et tout cela venait de la même requête faite par mon application.

J'ai exécuté cette requête moi-même et elle a vraiment pris environ 16 secondes pour obtenir une réponse ! Pas bon ! Et l'exécuter avec explain (comme certains sur les forums Meteor l'ont suggéré) a montré que 180 000+ documents étaient scannés ! Voici l'une des requêtes problématiques :

![Image](https://cdn-media-1.freecodecamp.org/images/1*wyFYzCGRM10CtscM5Ol6IA.png)
_Requête problématique_

En tout cas... et voilà, il n'y avait pas d'index configuré pour cette requête. J'ai ajouté les index suivants :

```
Meteor.startup(function () {    HeadToHeadMatches._ensureIndex({ team1Id: 1, gameweek: 1 });  HeadToHeadMatches._ensureIndex({ team2Id: 1, gameweek: 1 });});
```

Après cela, toute la base de données commence à fonctionner rapidement à nouveau. Cette seule requête problématique ralentissait toute la base de données !

> **MISE À JOUR #1 :** basée sur le [commentaire](https://medium.com/@joshowens/i-would-not-recommend-using-a-private-method-especially-since-it-calls-a-deprecated-method-inside-9049a3707f11#.3cixlmp2y) de Josh Owen, une meilleure façon d'ajouter des index est d'utiliser [Collection.rawCollection](http://docs.meteor.com/api/collections.html#Mongo-Collection-rawCollection) et [createIndex](http://mongodb.github.io/node-mongodb-native/2.2/tutorials/create-indexes/), mais le code ci-dessus fonctionnera pour vous jusqu'à au moins Meteor 1.4.2.

> **MISE À JOUR #2 :** les index sont plus compliqués que je ne le pensais au début, ayant rencontré des problèmes avec eux à nouveau cette semaine. Vous ne pourrez probablement pas trouver toutes vos requêtes qui ont besoin d'index sans parcourir vos logs.

> Vous devez trouver toutes les requêtes qui utilisent _COLLSCAN_. Cela signifie que la requête n'utilise pas d'index et pour trouver le document, Mongo doit parcourir toute la collection pour vérifier si le document que vous recherchez existe.

> Si vous utilisez Compose.io et que vous êtes sur MongoDB classic, vous devrez envoyer un email au support pour trouver quelles requêtes utilisent _COLLSCAN_. Si vous êtes sur leur plan MongoDB 3.2, vous devriez pouvoir trouver ces requêtes dans leur tableau de bord.

> De plus, si vous suspectez qu'une requête est problématique, exécutez la requête avec [_explain()_](https://docs.mongodb.com/manual/reference/method/cursor.explain/) et vous pourrez voir combien de documents sont scannés. Si _nscanned_ est égal au nombre de documents dans toute la collection, vous avez un problème et avez besoin d'un index. Un mauvais index peut massivement affecter toute votre base de données car il la verrouillera pour toutes les requêtes.

### Leçon #2 : Avoir trop d'instances Meteor est un problème !

Une fois que vous apprenez à mettre à l'échelle sur plusieurs instances, vous espérez que c'est la fin de tous les problèmes de mise à l'échelle. Hélas, ce n'est pas le cas. Et ajouter trop de serveurs nuira aux performances à un certain moment.

C'est parce que Mongo utilise de la RAM supplémentaire pour chaque connexion à la base de données. J'ai dû avoir environ 60 à 70 instances connectées à ma base de données à un moment donné, et Mongo n'a pas aimé cela, et je n'avais pas besoin d'autant. Les instances Meteor n'étaient pas le goulot d'étranglement pour les performances.

Vous pouvez bien sûr donner plus de RAM à Mongo, mais méfiez-vous simplement de ce qui se passe lorsque vous continuez à ajouter plus de serveurs. Vous pourriez soulager la charge de chaque instance Meteor, mais vous ajoutez de la charge à Mongo, créant ainsi un nouveau goulot d'étranglement.

### Leçon #3 : Ne vous inquiétez pas de la mise à l'échelle de Nginx

Une chose qui m'inquiétait cet été était que Nginx serait mon goulot d'étranglement. Ce sera rarement le cas. Nginx devrait être capable de gérer des milliers d'utilisateurs simultanés sans problème.

J'ai effectivement parlé à une entreprise qui avait des problèmes avec Nginx il y a quelques mois. Ils devaient gérer quelques milliers de connexions simultanées. Vous pouvez lire [cet article](http://blog.martinfjordvald.com/2011/04/optimizing-nginx-for-high-traffic-loads/) pour quelques conseils supplémentaires sur l'optimisation de Nginx pour des charges de trafic élevées.

Quelques points forts de l'article qui valent la peine d'être utilisés immédiatement :

Désactivez les logs d'accès :

> Par défaut, nginx écrivra chaque requête dans un fichier sur le disque à des fins de journalisation, vous pouvez utiliser cela pour des statistiques, des vérifications de sécurité, etc., cependant, cela a un coût en termes d'utilisation des E/S. Si vous n'utilisez pas les logs d'accès pour quoi que ce soit, vous pouvez simplement les désactiver et éviter les écritures sur le disque.

Processus de travail et connexions :

> **Processus de travail**  
> Le [**processus de travail**](http://wiki.nginx.org/CoreModule#worker_processes) est l'épine dorsale de nginx, une fois que le maître s'est lié aux IP/ports requis, il générera des travailleurs en tant qu'utilisateur spécifié et ils géreront ensuite tout le travail. Les travailleurs ne sont pas multi-threadés, donc ils ne répartissent pas la charge par connexion sur les cœurs CPU. Ainsi, il est logique pour nous d'exécuter plusieurs travailleurs, généralement 1 travailleur par cœur CPU. Pour la plupart des charges de travail, tout ce qui dépasse 2 à 4 travailleurs est excessif car nginx rencontrera d'autres goulots d'étranglement avant que le CPU ne devienne un problème et généralement vous aurez simplement des processus inactifs. Si vos instances nginx sont liées au CPU après 4 travailleurs, alors espérons que vous n'aurez pas besoin que je vous le dise.

> Un argument pour plus de processus de travail peut être fait lorsque vous traitez des situations où vous avez beaucoup d'E/S de disque bloquantes. Vous devrez tester votre configuration spécifique pour vérifier le temps d'attente sur les fichiers statiques, et s'il est important, essayez alors d'augmenter les processus de travail.

> **Connexions des travailleurs**  
> [**Connexions des travailleurs**](http://wiki.nginx.org/EventsModule#worker_connections) limite effectivement le nombre de connexions que chaque travailleur peut maintenir à un moment donné. Cette directive est probablement conçue pour prévenir les processus incontrôlés et au cas où votre OS est configuré pour permettre plus que ce que votre matériel peut gérer. Comme le souligne le développeur nginx Valentine sur la [**liste de diffusion nginx**](http://mailman.nginx.org/pipermail/nginx/2015-May/047460.html), nginx peut fermer les connexions keep-alive si elle atteint la limite, donc nous n'avons pas à nous soucier de notre valeur keep-alive ici. Au lieu de cela, nous nous préoccupons de la quantité de connexions actuellement actives que nginx gère. La formule pour le nombre maximum de connexions que nous pouvons gérer devient alors :

> worker_processes * worker_connections * (K / average $request_time)

> Où K est la quantité de connexions actuellement actives. De plus, pour la valeur K, nous devons également considérer le proxy inverse qui ouvrira une connexion supplémentaire à votre backend.

> Dans le fichier de configuration par défaut, la directive worker_connections est définie à 1024, si nous considérons que les navigateurs ouvrent normalement 2 connexions pour le pipelining des actifs du site, cela nous laisse avec un maximum de 512 utilisateurs gérés simultanément. Avec le proxy, cela est encore plus bas, bien que, espérons-le, votre backend réponde assez rapidement pour libérer la connexion.

> Toutes choses considérées sur les connexions des travailleurs, il devrait être assez clair que si vous grandissez en trafic, vous voudrez éventuellement augmenter le nombre de connexions que chaque travailleur peut gérer. 2048 devrait suffire pour la plupart des gens, mais honnêtement, si vous avez ce genre de trafic, vous ne devriez avoir aucun doute sur la hauteur dont vous avez besoin pour ce nombre.

### Leçon #4 : Déconnectez les utilisateurs inactifs

Celle-ci est importante ! Je ne comprends pas pourquoi ce n'est pas une plus grande chose dans la communauté Meteor !

Déconnectez les utilisateurs lorsqu'ils ont simplement laissé leur onglet ouvert. C'est si simple à faire et économise des ressources précieuses.

Pour déconnecter automatiquement, vous pouvez utiliser ce package : _mixmax:smart-disconnect._

### Leçon #5 : Will Griggs est en feu

Si vous êtes arrivé aussi loin dans l'article, vous vous sentez probablement super inspiré et d'humeur pour un chant de football. Je vous présente Will Griggs :

Il n'y avait en fait aucun point ici. Cela semblait simplement être la chose appropriée à écrire à ce stade de l'article. Mais si nous voulons vraiment en tirer une leçon, alors voici :

Si vous êtes un développeur solo, et que des milliers de personnes dépendent de votre application pour fonctionner _maintenant_, les choses peuvent devenir stressantes. Mon conseil pour vous (et pour moi-même) : calme-toi. Écoutez un peu Will Griggs on Fire. Espérons que vous allez vous en sortir, et même si les choses se gâtent, ce n'est probablement pas aussi grave que vous le pensez.

Pokemon Go était assez terrible au début. Les serveurs étaient constamment surchargés, mais les gens continuaient à revenir pour jouer. D'un point de vue commercial, Niantic a toujours fait un tabac. L'engouement s'est maintenant calmé, mais cela n'a rien à voir avec leurs problèmes de mise à l'échelle, ou les nombreux bugs initiaux. C'est juste la fin de la mode.

Donc, la leçon de vie, écoutez Will Griggs lorsque vous êtes stressé.

### Leçon #6 : Prenez exemple sur la façon dont ils ont mis à l'échelle Pokemon Go

Sur le sujet de Pokemon Go, parlons un peu de ce qui s'est passé. Tout d'abord, Pokemon Go ne vous arrivera pas. Pokemon Go avait une équipe solide d'anciens Googlers qui savaient comment gérer des charges énormes, mais même eux ont été surpris par la popularité de l'application. Ils étaient prêts pour une grosse charge, mais pas pour une charge de la taille de Twitter.

Certaines applications autour de Pokemon Go ont également fait leur apparition. Des applications de chat Pokemon Go, et des Instagrams Pokemon Go ont commencé à apparaître et sont devenus très populaires, très rapidement avec un million d'utilisateurs en quelques jours. Certaines de ces applications ont été développées par des développeurs solo et gérer la charge a été un défi pour eux.

Il y a [cet article](https://medium.com/unboxd/how-i-built-an-app-with-500-000-users-in-5-days-on-a-100-server-77deeb238e83#.q3odkr305) sur la façon dont quelqu'un a construit une application Instagram Pokemon Go avec 500 000 utilisateurs en 5 jours et l'a fait fonctionner sur un serveur à 100 $ par mois. C'est impressionnant. Et le message à retenir de l'article est que vous pouvez construire un MVP rapide qui scale si vous savez ce que vous faites.

Si vous pouvez faire cela, c'est définitivement génial, mais si vous êtes un jeune développeur inexpérimenté, cela peut ne pas être possible. Je recommanderais d'aller construire votre application de rêve et de ne pas trop vous soucier de ce qui se passe lorsque vous devez la mettre à l'échelle.

Si vous pouvez construire les choses correctement dès le départ, c'est définitivement un plus et cela vaut définitivement la peine de demander conseil à des développeurs plus expérimentés pour essayer de faire les choses correctement dès le début. Mais ne laissez pas la peur de la mise à l'échelle vous empêcher de créer votre application de rêve. La réalité cruelle est que les gens n'aimeront probablement pas votre application et ce serait impressionnant si vous pouvez obtenir 100 personnes pour l'utiliser.

Mais en suivant les principes du [lean startup](https://www.youtube.com/watch?v=NTh0aRBmwcg), il est préférable de construire quelque chose, de le mettre entre les mains de vrais utilisateurs et d'obtenir des retours, plutôt que de ne jamais lancer par peur de ne pas pouvoir gérer une charge lourde.

### Perspectives d'avenir

Ces épisodes de mise à l'échelle ont été un fardeau et idéalement, j'aurais préféré ne pas avoir à traiter ces problèmes. Ce serait génial si les choses fonctionnaient simplement et que vous pouviez repousser les problèmes de mise à l'échelle le plus longtemps possible. À cause de cela, j'ai commencé à regarder d'autres plateformes qui gèrent mieux la mise à l'échelle.

L'une de ces plateformes est Elixir, qui est construit sur Erlang. Erlang est ce que Whatsapp utilise et a permis à une équipe de 35 ingénieurs de mettre à l'échelle jusqu'à 450 millions d'utilisateurs ! Même aujourd'hui, avec près d'un milliard d'utilisateurs, Whatsapp a une équipe de seulement 50 ingénieurs ! C'est assez incroyable et vous pouvez en lire plus [ici](https://www.wired.com/2015/09/whatsapp-serves-900-million-users-50-engineers/). Comment ont-ils atteint une telle échelle pour une application en temps réel avec si peu de personnes ? La réponse est Erlang. Et aujourd'hui, vous pouvez utiliser la puissance d'Erlang avec [Phoenix Framework](http://www.phoenixframework.org/) et [Elixir](http://elixir-lang.org/). Nous utilisons toujours Meteor, mais certains aspects de l'application que je envisage de migrer vers Elixir, ce qui nous permettra de gérer des mises à jour en direct à grande échelle.

Je jetterais également un coup d'œil à Apollo, qui fonctionnera avec Meteor ou tout serveur Node.js. Apollo vous aidera à mettre à l'échelle Meteor, car vous n'avez pas besoin que chaque publication soit réactive lorsque vous utilisez Apollo (ce qui est le plus gros drain sur le CPU du serveur pour les applications Meteor). Vous pouvez obtenir un résultat similaire en utilisant des méthodes Meteor pour envoyer des données au lieu de publications.

Un dernier point est que malgré le départ récent de nombreux développeurs Meteor influents de la communauté, il y a eu quelques développements sur le front de la mise à l'échelle. Consultez le package [redis-oplog](https://github.com/cult-of-coders/redis-oplog) et la [discussion](https://forums.meteor.com/t/meteor-scaling-redis-oplog-status-1-1-4-stable/30855) pour plus d'informations. C'est un package très nouveau et je dirais toujours qu'il est en bêta d'après ma petite expérience en jouant avec il y a une semaine.

Si vous avez aimé cet article, donnez-lui un cœur, et si vous voulez rester à jour avec les derniers articles inspirants sur la mise à l'échelle, suivez-moi.