---
title: Premières expériences de mise à l'échelle d'une application Meteor
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2015-11-02T20:48:52.000Z'
originalURL: https://freecodecamp.org/news/first-experiences-scaling-a-meteor-app-14a48e62a4af
coverImage: https://cdn-media-1.freecodecamp.org/images/1*CLGpRvTRx9l4dn-ky6bP5g.png
tags:
- name: JavaScript
  slug: javascript
- name: Meteor
  slug: meteor
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Premières expériences de mise à l'échelle d'une application Meteor
seo_desc: 'By Elie Steinbock

  I recently went through the challenge and ordeal of having to scale my Meteor app.
  It’s a project that had already been running in production for about a year. This
  summer the app became a lot more popular with thousands of preseaso...'
---

Par Elie Steinbock

J'ai récemment traversé le défi et l'épreuve de devoir mettre à l'échelle mon application [Meteor](https://www.meteor.com/). C'est un projet qui tournait déjà en production depuis environ un an. Cet été, l'application est devenue beaucoup plus populaire avec des milliers d'inscriptions en présaison. Ma configuration initiale ne pouvait plus gérer la charge et j'ai été confronté à un problème de mise à l'échelle qui devait être résolu rapidement.

Cet article décrit le processus que j'ai suivi et certaines des choses que j'ai apprises en cours de route, et j'espère qu'il aidera les autres qui pourraient rencontrer des défis similaires à l'avenir. Il couvrira les bases, comme ce qu'est la mise à l'échelle et comment fonctionne l'équilibrage de charge. Il vous guidera également à travers quelques configurations de base et vous montrera comment mettre à l'échelle votre application Meteor.

Avant l'été, je n'avais aucune expérience préalable dans la mise à l'échelle d'applications, et malgré le fait que j'avais lu beaucoup sur le sujet, lorsque j'ai dû m'asseoir et commencer à traiter les défis moi-même, je me sentais assez perdu et je n'étais pas sûr de pouvoir résoudre les problèmes. J'ai également senti que beaucoup des articles que j'avais lus en ligne supposaient une certaine quantité de connaissances que je n'avais pas encore.

Mon espoir est que cet article aidera à combler une partie de cet écart. Je suis loin d'être un expert en matière de mise à l'échelle des applications Meteor, mais j'espère que cet article apportera de la valeur aux autres qui se trouvent dans une situation similaire à celle dans laquelle je me trouvais.

### Contexte

Un peu de contexte sur l'application en discussion. C'est un jeu de fantasy football de style draft pour la Premier League anglaise (football). La plupart des inscriptions ont lieu le mois avant le début de la saison. En plus de toutes les inscriptions, presque toutes les drafts ont également lieu ce mois-ci. La draft est le moment où tous les utilisateurs d'une ligue se connectent pour choisir leur équipe. Les utilisateurs choisissent leurs joueurs de football un à la fois et tout le processus est en direct, chaque utilisateur ayant entre 30 secondes et 5 minutes par choix de joueur.

Aux heures de pointe, le site avait plus de 500 utilisateurs simultanés en ligne et 20 drafts en cours simultanément. Si le serveur devient non réactif pendant une draft, cela gâche complètement l'expérience de l'utilisateur avec des joueurs qui sont choisis automatiquement pour lui qu'il n'avait pas nécessairement l'intention de choisir, il était donc extrêmement important d'éviter cela.

### Qu'est-ce que la mise à l'échelle ?

Pour beaucoup, cela peut sembler évident, mais il n'y a pas si longtemps, je n'avais aucune idée de ce que signifiait ce mot à la mode.

La mise à l'échelle est ce qui se passe lorsque votre application décolle. Votre serveur ne peut gérer qu'une certaine charge. Que se passe-t-il lorsque 10 000 personnes veulent utiliser votre application en même temps ? Votre serveur ne pourra pas le gérer, vous devez donc soit obtenir un serveur plus puissant, soit obtenir plus de serveurs pour exécuter l'application. Ce processus est appelé mise à l'échelle.

Il existe deux façons de mettre à l'échelle une application. L'une est connue sous le nom de mise à l'échelle verticale, et l'autre sous le nom de mise à l'échelle horizontale. La mise à l'échelle verticale implique l'obtention d'un serveur plus puissant. La mise à l'échelle horizontale implique de servir votre site à partir de plusieurs serveurs.

Pour utiliser une analogie, si vous avez un magasin et employez un travailleur et souhaitez pouvoir servir plus de clients, vous pouvez soit obtenir un travailleur meilleur et plus rapide (mise à l'échelle verticale), soit embaucher plus d'employés (mise à l'échelle horizontale).

Pour les applications web, la mise à l'échelle verticale est généralement plus facile à faire. Chez les sociétés d'hébergement telles que [DigitalOcean](https://www.digitalocean.com/?refcode=2518a67f26c8) ou [AWS](https://aws.amazon.com/?nc2=h_lg) (Amazon Web Services), vous pouvez facilement mettre à niveau votre serveur privé virtuel vers une configuration plus puissante avec une RAM, des CPU et un stockage accrus.

Le problème avec cette approche est qu'il y a toujours une limite à la puissance que vous pouvez donner à votre serveur. À un moment donné, vous allez devoir passer à la mise à l'échelle horizontale. En utilisant l'exemple ci-dessus, votre entreprise ne peut aller que jusqu'à un certain point avec un seul employé. À un certain moment, vous allez devoir embaucher plus de membres du personnel.

En ce qui concerne les applications Meteor, vous allez devoir passer à la mise à l'échelle horizontale assez tôt. Une application Meteor n'est vraiment qu'une application NodeJS et fonctionne donc dans un seul processus, ce qui signifie qu'elle ne peut utiliser qu'un seul processeur.

Nous pouvons utiliser plusieurs processeurs en exécutant plusieurs instances de notre application en même temps. Ces processeurs pourraient appartenir au même serveur ou être répartis sur plusieurs serveurs différents. Exécuter plusieurs instances d'une application signifie exécuter la même application sur différentes IP ou ports, et répartir la charge sur les différentes instances de l'application. Toutes les instances de l'application se connectent toujours à la même base de données et tous les clients connectés recevront instantanément toute mise à jour de la base de données, quelle que soit l'instance de l'application à laquelle ils sont connectés (en supposant que vous utilisez la fonctionnalité de suivi Oplog de MongoDB. Sinon, les mises à jour peuvent prendre quelques secondes).

Que nous exécutions plusieurs instances de notre application sur un seul serveur avec plusieurs cœurs, ou que nous exécutions plusieurs instances sur plusieurs serveurs, ce que nous avons fait est une mise à l'échelle horizontale et les choses fonctionnent de la même manière dans les deux cas.

Chaque plateforme aura ses propres défis de mise à l'échelle. Cet article concerne la mise à l'échelle des applications Meteor. Sur d'autres plateformes, vous pourrez vous en sortir avec une mise à l'échelle verticale beaucoup plus longtemps. StackOverflow fonctionne sur [25 serveurs](http://highscalability.com/blog/2014/7/21/stackoverflow-update-560m-pageviews-a-month-25-servers-and-i.html) et pourrait même se contenter de 5. C'est une charge sérieuse sur chaque serveur et c'est surtout un cas de mise à l'échelle verticale impressionnante.

### Les différentes parties d'une application Meteor

Nous pouvons diviser notre application en deux composants logiques. La première partie est le serveur qui gère les requêtes des utilisateurs en renvoyant les données appropriées et effectue toutes les tâches qui doivent être effectuées. La deuxième partie est la base de données qui stocke les données de l'application.

Le serveur interagit avec la base de données en l'interrogeant et en la mettant à jour de manière cohérente.

Nous ne allons pas trop parler de la mise à l'échelle de MongoDB. Il faudra probablement un certain temps avant que vous n'atteigniez un point où vous devrez mettre à l'échelle votre base de données. Si vous souhaitez en savoir plus sur ce sujet, [ce lien](http://highscalability.com/blog/2014/3/5/10-things-you-should-know-about-running-mongodb-at-scale.html) pourrait être un bon point de départ.

### Choses à faire avant de mettre à l'échelle le serveur

Un bon point de départ avant de vous lancer dans la mise à l'échelle est de vous assurer que votre application fonctionne aussi efficacement que possible. L'outil recommandé pour vérifier les performances de votre application et quelles méthodes et publications prennent le plus de temps à s'exécuter est [Kadira](https://kadira.io/). Le plan de base est gratuit, il n'y a donc vraiment aucune raison de ne pas l'utiliser. Utilisez les articles de [Kadira Academy](https://kadira.io/academy) pour déterminer comment optimiser au mieux votre application et où consacrer votre énergie. En général, vous voulez optimiser les méthodes et publications qui s'exécutent le plus souvent et prennent beaucoup de temps à s'exécuter.

Une chose qui est absolument nécessaire pour de bonnes performances est d'utiliser les index MongoDB. Vous faites cela dans Meteor en écrivant :

> _Posts._ensureIndex({userId: 1});_

Cela crée un index sur le champ _userId_ dans la collection _Posts_. Vous pouvez également créer des index dans MongoDB lui-même. Voir plus sur les index MongoDB [ici](http://docs.mongodb.org/manual/core/indexes/).

Voir [cet article](http://blog.differential.com/scaling-meteor-to-20000-users-in-7-days/) par Differential pour quelques conseils de performance supplémentaires.

### Quand dois-je commencer à m'inquiéter de la mise à l'échelle ?

Si votre application Meteor a plus de 100 utilisateurs en ligne à un moment donné, vous allez probablement devoir commencer à vous inquiéter de la mise à l'échelle. (Bien sûr, vous ne savez pas quand votre application va décoller. Vous pourriez passer de 5 à 500 utilisateurs simultanés en une seule journée, il est donc utile d'être préparé avant que cela n'arrive.)

Selon votre application, vous pourriez être en mesure de gérer jusqu'à 500 utilisateurs simultanés sur un seul droplet DigitalOcean. Mon application a du mal avec 100 à 150 connexions simultanées, moment auquel elle atteint 100 % de CPU. Le goulot d'étranglement pour la plupart des applications Meteor semble être le CPU et non la RAM, donc la mise à l'échelle horizontale est une nécessité. Vous pouvez ajouter toute la RAM que vous voulez, mais cela n'aidera pas votre application. Le manque de CPU est ce qui va surcharger votre application et vous ne pouvez obtenir plus de puissance CPU qu'en utilisant plusieurs CPU (ou plusieurs serveurs).

Le graphique suivant de Kadira montre ce qui se passe lorsque votre application est sous trop de pression.

![Image](https://cdn-media-1.freecodecamp.org/images/1*DLnj_FU_qp2TW6s5NADnuQ.png)
_Statistiques Kadira. 1 cœur, droplet Digital Ocean à 10 $/mois_

Vers 19h28, vous pouvez voir que le temps de réponse moyen pour les publications était d'environ 18 secondes et pour les méthodes d'environ 7 secondes. Ce n'est pas une bonne situation. Le temps de réponse élevé a été causé par un pic important de CPU qui a atteint 100 % pendant quelques minutes. La RAM n'est pas un problème car seulement environ 500 Mo sont utilisés à un moment donné et le VPS utilisé ici a 1 Go de RAM.

### Déploiement

Il existe plusieurs façons de déployer votre application Meteor. Voici quelques-unes des solutions courantes que les gens utilisent pour les applications de production :

* Auto-hébergé sur [DigitalOcean](https://www.digitalocean.com/?refcode=2518a67f26c8) ou AWS
* [Modulus.io](https://modulus.io/meteor)

Il y a aussi l'[hébergement gratuit meteor.com](https://www.meteor.com/tutorials/blaze/deploying-your-app), mais cela ne devrait être utilisé qu'à des fins de développement. MDG vient également de lancer [Galaxy](https://www.meteor.com/why-meteor/pricing?gclid=Cj0KEQjwy92wBRCl7trx4PaIo8EBEiQASPhtC_SBf0TXyLL_MZpEx9RYTIyVoZT8-5zGVOaC_tDzUsoaAgBB8P8HAQ), mais le prix pour cela commence actuellement à 500 $ par mois. MDG travaille à fournir des plans moins chers pour Galaxy ainsi qu'un plan gratuit, mais au moment de la rédaction de cet article, ces options ne sont pas disponibles.

Il est également courant pour les gens d'héberger la base de données chez un autre fournisseur. Un fournisseur populaire est [Compose.io](https://www.compose.io/mongodb/).

> **Mise à jour :** Vous pouvez maintenant obtenir un hébergement [Galaxy](https://www.meteor.com/hosting) à partir de 29 $ par mois. Compose.io n'a plus de plan gratuit. Un autre fournisseur d'hébergement Mongo appelé [MLabs](https://mlab.com/) en a un. Lorsque vous passez en production (c'est-à-dire lorsque le développement est terminé et que les gens utilisent réellement votre application), vous ne voulez pas utiliser un plan gratuit cependant.

Ma propre configuration est DigitalOcean + Compose.io.

Si vous souhaitez lire sur d'autres configurations, voir la section déploiement sur [Meteorpedia](http://meteorpedia.com/read/Category:Deployment).

Ma configuration initiale était un droplet [DigitalOcean](https://www.digitalocean.com/?refcode=2518a67f26c8) à 10 $ par mois. Cela vous donne un VPS à un cœur avec 1 Go de RAM. Vous obtenez également 30 Go de stockage, bien que vous n'utilisiez probablement pas la plupart.

J'utilise le plan Elastic Deployment de Compose.io à 18 $ par mois pour l'hébergement de la base de données MongoDB. Vous pouvez gérer vous-même les trucs MongoDB, mais c'est juste un travail supplémentaire que je ne voulais pas gérer.

Pour déployer, j'utilise un outil appelé Meteor Up (ou Mup pour faire court). Vous pouvez le consulter sur GitHub [ici](https://github.com/arunoda/meteor-up).

Si vous déployez sur Modulus.io, ils s'occuperont de beaucoup de problèmes de mise à l'échelle pour vous. Si vous voulez exécuter plusieurs instances de votre application, tout ce que vous avez à faire est de déplacer un curseur de haut en bas sur le site Web de Modulus. Plus vous exécutez d'instances, plus cela vous coûtera cher, mais vous pouvez également réduire l'échelle quand vous le souhaitez.

Je n'ai pas choisi Modulus pour le déploiement car j'ai eu quelques problèmes pour le configurer il y a deux ans. J'assume que ces problèmes auraient été résolus depuis. L'autre problème est le coût. Il est moins cher de déployer sur DigitalOcean. L'inconvénient est que cela peut prendre plus de votre temps. Un autre avantage de choisir DigitalOcean est un contrôle plus fin sur votre serveur.

Un article comparant DO, Modulus.io et Heroku peut être trouvé [ici](http://joshowens.me/modulus-vs-heroku-vs-digital-ocean/).

### Comment mettre à l'échelle une application Meteor ?

Comme indiqué ci-dessus, mon application est déployée sur Digital Ocean en utilisant Meteor Up. Avec cette configuration, vous n'avez pas le luxe d'utiliser un curseur pour charger plus d'instances. Un fichier _mup.json_ standard ressemble à ceci :

```
{   "servers": [     {      "host": "123.45.678.901",      "username": "root",      "pem": "~/.ssh/id_rsa",      "env": {}     },     {       "host": "333.22.444.555",       "username": "root",       "pem": "~/.ssh/id_rsa",       "env": {}     }   ],   "setupMongo": false,   "setupNode": true,   "nodeVersion": "0.10.40",   "setupPhantom": true,   "appName": "myapp",   "app": "/Users/arunoda/Meteor/my-app",   "env": {      "PORT": 80,      "ROOT_URL": "http://myapp.com",      "MONGO_URL": "mongodb://arunoda:fd8dsjsfh7@hanso.mongohq.com:10023/MyApp",      "MONGO_OPLOG_URL": "mongodb://.....",      "MAIL_URL": "smtp://postmaster%40myapp.mailgun.org:adj87sjhd7s@smtp.mailgun.org:587/"   },   "deployCheckWaitTime": 15}
```

Remarquez que j'ai listé deux serveurs dans le bloc _servers_. Lorsque vous commencez, vous n'aurez qu'un seul serveur listé. Avec la configuration suivante, nous allons déployer sur les adresses IP _123.45.678.901_ et _333.22.444.555_. Après le déploiement, si vous visitez l'une de ces adresses IP dans votre navigateur, vous verrez la même chose et les deux serveurs seront connectés à la même base de données.

### Équilibrage de charge

Nous avons donc déployé notre site, mais nous ne voulons pas que les utilisateurs visitent le site à des adresses IP aléatoires. Nous voulons qu'ils visitent notre domaine. Supposons donc que notre nom de domaine est awesomedomain.com (ce qui est mieux que example.com, à mon humble avis). Comment faire en sorte que chacun de nos deux serveurs traite la moitié des requêtes ?

Une façon de faire cela est d'utiliser un outil appelé [Nginx](http://nginx.org/). D'après [Wikipedia](https://en.wikipedia.org/wiki/Nginx) :

> **Nginx** (prononcé « engine x ») est un serveur web avec un fort accent sur la haute concurrence, la performance et la faible utilisation de la mémoire. Il peut également agir comme un serveur proxy inverse pour les protocoles HTTP, HTTPS, SMTP, POP3 et IMAP, ainsi que comme un équilibreur de charge et un cache HTTP.

Nous allons l'utiliser pour trois choses :

1. Comme un proxy inverse
2. Comme un équilibreur de charge
3. Pour le support SSL

Cela signifie que nous allons exécuter Nginx sur l'un de nos serveurs sur le port 80. Tout le trafic entrant dans le serveur depuis le web sera reçu par Nginx. Nginx transférera ensuite le trafic vers les instances de notre application Meteor, qui pourraient s'exécuter sur le même serveur sur un port différent, ou sur un serveur différent. Nginx essaiera d'équilibrer le nombre de requêtes envoyées à chaque instance.

Nginx étant un proxy inverse signifie qu'il transfère les requêtes vers d'autres endroits puis répond à l'utilisateur.

Être un équilibreur de charge signifie qu'il répartira (équilibrera) la charge entre les différentes instances de l'application.

Nous utiliserons également Nginx pour nous fournir un support SSL. Le support SSL signifie que toute donnée transférée entre l'utilisateur et nos serveurs sera cryptée. Sans support SSL, notre site Meteor ne fonctionnera pas correctement dans de nombreux pays, et il sera également assez facile pour les gens de [pirater les comptes de nos utilisateurs](http://blog.east5th.co/2015/08/23/hijacking-meteor-accounts-by-sniffing-ddp/) ou de lire toute donnée transférée. Tout site qui utilise HTTPS a un support SSL.

SSL n'est pas le sujet principal de cet article, mais c'est une nécessité pour toute application de production et Nginx peut s'occuper du SSL pour vous. Pour configurer SSL avec Nginx, voir [ici](https://gist.github.com/LeCoupa/9877434). Vous n'avez pas besoin d'utiliser Nginx pour le support SSL cependant. Meteor Up peut également le gérer en utilisant un outil appelé stud comme montré [ici](https://github.com/arunoda/meteor-up#ssl-support).

Alors, comment configurer Nginx ?

Pour cela, je recommande de suivre la première étape de ce tutoriel :

[**Comment déployer une application Meteor.js sur Ubuntu 14.04 avec Nginx | DigitalOcean**](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-meteor-js-application-on-ubuntu-14-04-with-nginx)  
[_Déployer une application Meteor.js sur Ubuntu 14.04 avec Nginx et MongoDB. Ce tutoriel vous montre comment construire et déployerwww.digitalocean.com](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-meteor-js-application-on-ubuntu-14-04-with-nginx)

Ne vous embêtez pas à suivre le reste du tutoriel. Meteor Up s'occupera de tout cela pour vous automatiquement.

L'article explique également comment utiliser Nginx pour le support SSL.

Une fois que tout cela fonctionne pour vous, vous devriez avoir votre application en cours d'exécution sur un domaine. Jusqu'à présent, Nginx n'a pas vraiment fait grand-chose pour nous (sauf éventuellement le support SSL). Nous n'utilisons toujours pas notre deuxième instance Meteor, mais nous allons corriger cela maintenant.

Pour utiliser plus de serveurs, vous devez ajouter le code suivant en haut de votre fichier Nginx :

```
upstream myAppName {  ip_hash;               # pour les sessions persistantes, plus d'informations ci-dessous  server 123.45.678.901:3000;  # serveur 1  server 333.22.444.555:3000;  # serveur 2}
```

Votre fichier Nginx devrait maintenant ressembler à ceci :

```
upstream myAppName {  ip_hash;               # pour les sessions persistantes, plus d'informations ci-dessous  server 123.45.678.901:3000;  # serveur 1  server 333.22.444.555:3000;  # serveur 2}server {  listen 80;  server_name www.myapp.com  # et toutes les autres directives "server"  location / {    # le "hostname" ci-dessous doit être le même que myAppName de la directive upstream ci-dessus    proxy_pass http://myAppName;    # et toutes les autres directives "location"  }}
```

où _myAppName_ serait quelque chose comme _example.com_ ou _app.example.com._

Le code ci-dessus a été adapté de [Meteorpedia](http://www.meteorpedia.com/read/nginx).

Si vous rechargez maintenant Nginx (comme décrit dans l'article Digital Ocean ci-dessus) en utilisant :

```
nginx -t # vérifier que tout est correctnginx -s reload
```

La charge sera répartie entre vos deux instances Meteor.

Si vous souhaitez ajouter plus d'instances à l'avenir, tout ce que vous avez à faire est d'ajouter une autre ligne au bloc upstream de Nginx et de redémarrer Nginx. Voici un exemple qui utilise 4 instances Meteor, avec 2 instances s'exécutant sur deux serveurs différents :

```
upstream myAppName {  ip_hash;  server 10.0.0.1:3000;  # serveur 1, cœur 1  server 10.0.0.1:3001;  # serveur 1, cœur 2  server 10.0.0.2:3000;  # serveur 2, cœur 1  server 10.0.0.2:3001;  # serveur 2, cœur 2  # ou toute autre combinaison appropriée}
```

La suppression d'instances implique simplement de supprimer des lignes du bloc upstream et de redémarrer Nginx.

### Algorithmes d'équilibrage de charge

Si vous voulez simplement que les choses fonctionnent, alors suivre les étapes ci-dessus devrait suffire, mais si vous voulez comprendre un peu plus en profondeur, voici une explication de base de ce que nous venons de faire.

Nous utilisons Nginx comme équilibreur de charge. Pour chaque requête qui arrive, Nginx doit décider à quel serveur l'envoyer. En même temps, Nginx doit être aussi rapide que possible dans l'exécution de son travail, en utilisant le moins de ressources possible. Nginx est capable de gérer 10 000 connexions simultanées et les algorithmes d'équilibrage de charge simples font partie de ce qui rend cela possible.

Un algorithme simple qui est utilisé pour décider où envoyer la prochaine requête est appelé « round robin ». Dans cet algorithme, l'équilibreur de charge envoie les requêtes des clients à chaque serveur à tour de rôle et une fois qu'il arrive à la fin de la liste des serveurs, il recommence le processus. Le résultat pour trois serveurs est : 1, 2, 3, 1, 2, 3, 1, 2, ...

Il existe de nombreux autres algorithmes qui peuvent également être utilisés pour décider à quel serveur envoyer une requête, mais une contrainte que Meteor nous impose de suivre est que chaque requête d'un utilisateur doit être envoyée à la même instance. Cela est également connu sous le nom de « sessions persistantes ». Un utilisateur reste avec le même serveur pendant toute la session.

Cela signifie que nous ne pouvons pas utiliser l'algorithme round robin pour notre application Meteor, qui ne prend pas en compte à quel serveur l'utilisateur s'est d'abord connecté. Au lieu de cela, nous utilisons l'algorithme _ip_hash_ qui est expliqué dans la [documentation Nginx](http://nginx.org/en/docs/http/load_balancing.html#nginx_load_balancing_with_ip_hash) comme suit :

> Avec ip-hash, l'adresse IP du client est utilisée comme clé de hachage pour déterminer quel serveur dans un groupe de serveurs doit être sélectionné pour les requêtes du client. Cette méthode garantit que les requêtes d'un même client seront toujours dirigées vers le même serveur sauf lorsque ce serveur est indisponible.

### Exécution en local

Vous pouvez également essayer d'exécuter deux instances de votre application en local. Pour cela, ouvrez deux fenêtres de terminal et démarrez une application Meteor sur le port standard (3000) en exécutant :

```
meteor
```

La base de données s'exécutera maintenant sur le port 3001.

Dans une fenêtre de terminal séparée, exécutez une autre instance de l'application sur le port 4000 qui se connecte à la même base de données en exécutant ce qui suit :

```
export MONGO_URL=mongodb://localhost:3001/meteor
```

```
meteor --port 4000
```

Vous pouvez maintenant visiter _localhost:3000_ ou _localhost:4000_ dans votre navigateur web et les deux apporteront des modifications à la même base de données.

### Choses à savoir

Il peut y avoir du code dans votre application que vous ne voulez exécuter qu'une seule fois. Par exemple, dans mon jeu de fantasy football, je ne veux qu'un seul serveur mettant à jour les scores.

Un autre problème qui peut survenir est que certaines opérations peuvent être assez coûteuses. Encore une fois, la mise à jour des scores dans le jeu est un processus assez long et je ne veux pas qu'il interfère avec le fonctionnement de base de l'application.

Alors, comment résoudre ces problèmes ?

Il existe plusieurs façons de gérer une telle situation, mais je vais simplement décrire ce que j'ai fait.

J'ai configuré un nouveau droplet sur Digital Ocean qui ne reçoit aucun trafic du site web principal. Il peut être accessible à son adresse IP, mais ce droplet ne reçoit aucun trafic de l'URL publique du site web. Cette instance est responsable de l'exécution de toutes les tâches en arrière-plan et de toute tâche qui ne doit être exécutée qu'une seule fois.

Pour rendre le code spécifique à une seule instance de l'application, j'utilise des variables d'environnement. Dans votre environnement local, vous pouvez exporter des variables dans votre fenêtre de terminal comme suit :

```
export ENV_VAR=valueOfOurVar
```

Nous l'avons fait auparavant pour _MONGO_URL_.

Vous pouvez accéder aux variables d'environnement dans votre application Meteor en utilisant :

```
process.env.ENV_VAR
```

Dans mon application, je peux faire quelque chose comme ceci si je ne veux qu'une seule instance de l'application exécute un certain code :

```
if (process.env.RUN_BACKGROUND_TASKS === 'true') {   // faire une tâche}
```

J'aurais également pu utiliser une approche pure de microservices, mais cela m'aurait pris un peu plus de temps à configurer et le partage de code aurait été plus difficile.

Lorsque vous utilisez Meteor Up, vous pouvez définir des variables d'environnement pour une instance spécifique comme suit :

```
"servers": [   {     "host": "...",     "username": "...",     "pem": "...",     "env": {       "ENV_VAR": "123",       "RUN_BACKGROUND_TASKS": "true"     }   } ],
```

Il existe également des packages qui ne fonctionnent pas bien lors de l'exécution de plusieurs instances d'une application. Un package que j'ai rencontré et qui entre dans cette catégorie est [mizzao:user-status](https://atmospherejs.com/mizzao/user-status). Ce package vous indique quels utilisateurs sont en ligne à un moment donné et [ne fonctionne pas correctement](https://github.com/mizzao/meteor-user-status/issues/70) lors de l'exécution de plusieurs instances. Un serveur aura une connexion ouverte à un client spécifique tandis que les autres ne l'auront pas et ce package ne sait pas comment gérer une telle situation. Une connexion fermée implique qu'un utilisateur est hors ligne. Une solution consiste à utiliser le package [konecty:user-presence](https://atmospherejs.com/konecty/user-presence) à la place.

Vous ne voulez pas non plus que les tâches cron s'exécutent sur plusieurs instances. Pour cela, vous pouvez utiliser le package [percolate:synced-cron](https://atmospherejs.com/percolate/synced-cron). Je ne l'ai pas personnellement utilisé, mais cela semble être une bonne solution, optant plutôt pour restreindre toutes les tâches cron à un serveur spécifique, mais cela semble être une bonne solution.

### Autres solutions

Il existe de nombreuses façons de faire ce que nous avons fait dans cet article. Utiliser Nginx n'est pas la seule solution. Pour le support SSL, nous aurions pu utiliser [stud](https://github.com/bumptech/stud) comme le fait Meteor Up. Pour l'équilibrage de charge, nous aurions pu utiliser un outil appelé [HAProxy](http://www.haproxy.org/) dont le seul but est d'être un équilibreur de charge.

Une autre approche à tout cela est d'utiliser le package [MeteorHacks Cluster](https://github.com/meteorhacks/cluster). C'est simplement un package Meteor que vous ajoutez comme suit :

```
meteor add meteorhacks:cluster
```

Pour le voir fonctionner immédiatement sur votre propre machine, exportez la variable d'environnement suivante dans votre terminal :

```
export CLUSTER_WORKERS_COUNT=2
```

Si vous exécutez maintenant votre application, vous devriez voir deux instances de votre application Meteor démarrer. Ici, nous avons utilisé le support multicœur du package cluster. Nous pouvons également utiliser cluster pour distribuer la charge parmi plusieurs serveurs. Vous devriez consulter la [documentation cluster](https://github.com/meteorhacks/cluster) pour configurer cela.

Est-il préférable d'utiliser MeteorHacks Cluster ou Nginx ?

Je ne connais pas la réponse à cette question. J'ai eu des problèmes à utiliser MeteorHacks Cluster en production lorsque j'utilisais son support multicœur. L'application fonctionnait bien dans des conditions de faible stress, mais sous charge élevée, l'application plantait aléatoirement, nécessitant un redémarrage manuel pour la faire fonctionner à nouveau. Il y a un problème ouvert sur GitHub à ce sujet [ici](https://github.com/meteorhacks/cluster/issues/46). Si vous n'utilisez pas le support multicœur, cela ne devrait pas être un problème.

### Ma configuration finale

La base de données s'exécute sur Compose.io à un coût de 18 $/mois par Go d'espace utilisé.

L'application s'exécute actuellement sur 8 droplets [DigitalOcean](https://www.digitalocean.com/?refcode=2518a67f26c8) :

(Un droplet à 5 $/mois a 512 Mo de RAM et 1 cœur, un droplet à 10 $/mois a 1 Go de RAM et 1 cœur, un droplet à 20 $/mois a 2 Go de RAM et 2 cœurs.)

* 1 droplet à 5 $/mois prend en charge les tâches en arrière-plan et ne gère aucune requête utilisateur.
* 1 droplet à 20 $/mois avec 2 cœurs exécute Nginx et 2 instances Meteor de l'application.
* 4 droplets à 10 $/mois (1 instance par droplet)
* 2 droplets à 5 $/mois (1 instance par droplet)

Il y a aussi un droplet à 5 $/mois pour le blog qui s'exécute sur Ghost sur un sous-domaine (ceci n'est pas Meteor).

Je travaille également sur une application mobile et celle-ci s'exécutera sur d'autres droplets et servira un site différent aux visiteurs. Les vues/logiques client ici sont différentes, la logique serveur est la même.

#### Quels droplets choisir ?

Vous vous demandez peut-être pourquoi mes droplets sont de tailles différentes. Au début, j'utilisais uniquement des droplets à 10 $/mois, mais puisque mon goulot d'étranglement est le CPU et non la RAM, je devrais pouvoir remplacer tous mes droplets à 10 $/mois par des droplets à 5 $/mois, puisque vous obtenez la même puissance de CPU avec chacun.

Je suis en train de tester cela maintenant et de voir comment cela se passe. Vous devez être prudent de ne pas manquer de RAM lorsque vous utilisez des droplets de 512 Mo. Si vous utilisez le package [_spiderable_](https://atmospherejs.com/meteor/spiderable), votre serveur peut planter lorsqu'un moteur de recherche indexe votre site et cela provoquera une augmentation du CPU à 100 %. Vous pouvez contourner cela en utilisant [prerender.io](https://prerender.io/) au lieu de _spiderable_ et/ou [en ajoutant de l'espace swap](https://www.digitalocean.com/community/tutorials/how-to-add-swap-on-ubuntu-14-04). Si vous utilisez React, vous pouvez utiliser le rendu côté serveur pour les moteurs de recherche au lieu de spiderable comme expliqué [ici](https://kadira.io/blog/meteor/meteor-ssr-support-using-flow-router-and-react).

#### Mise à l'échelle automatique

Il serait bien de pouvoir charger automatiquement plus de droplets lorsque le site est sous stress et les supprimer lorsque personne ne l'utilise. Mon site est utilisé beaucoup plus pendant les week-ends par exemple. Il serait bien si je pouvais lancer automatiquement plus de droplets chaque fois qu'il y a beaucoup de trafic et les supprimer lorsqu'il y a moins de trafic.

Je n'ai pas encore vu de solution facile à cela pour les applications Meteor déployées sur DigitalOcean, mais en utilisant l'API DigitalOcean, cela devrait être possible sans trop de travail. Cela réduirait considérablement les coûts d'hébergement.

Il semble être assez facile de faire de la mise à l'échelle automatique sur Modulus comme montré [ici](http://blog.modulus.io/new-modulus-multi-servo-auto-scaling). Et vous pouvez lire sur la mise à l'échelle automatique sur AWS [ici](http://allandequeiroz.com/2015/09/27/amazon-auto-scaling-and-meteor/) et [ici](http://fightingtheboss.github.io/).

#### Choses que je ferais différemment

Je testerais que mon application peut bien fonctionner sur deux serveurs à un stade beaucoup plus précoce du processus de développement. Le passage de 1 serveur à 2 serveurs est assez important si vous ne l'avez jamais fait auparavant. Le passage de 2 serveurs à 10 serveurs est minuscule.

#### Autres ressources sur la mise à l'échelle des applications Meteor

* [meteorhacks:cluster](https://github.com/meteorhacks/cluster)
* [Meteor Up (Mup)](https://github.com/arunoda/meteor-up)
* [Meteorpedia](http://www.meteorpedia.com/read/Scaling_your_Meteor_App)
* [MeteorHacks: Does Meteor Scale?](https://meteorhacks.com/does-meteor-scale)
* [Discover Meteor : Scaling Meteor: The Challenges of Real-time Apps](https://www.discovermeteor.com/blog/scaling-meteor-the-challenges-of-realtime-apps/)
* [Differential: Scaling Meteor to 20,000+ Users in 7 Days](http://blog.differential.com/scaling-meteor-to-20000-users-in-7-days/)

#### Ajouts ultérieurs

J'ai vraiment aimé l'article suivant. Il contient des informations clés sur les tests de charge, une meilleure configuration Nginx et l'utilisation d'un CDN : [https://medium.freecodecamp.com/minimum-viable-devops-919972dfd9e0](https://medium.freecodecamp.com/minimum-viable-devops-919972dfd9e0#.ym8w9jj8g)