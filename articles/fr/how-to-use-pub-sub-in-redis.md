---
title: Pub/Sub dans Redis – Comment utiliser le modèle de messagerie Publish/Subscribe
subtitle: ''
author: Mihail Gaberov
co_authors: []
series: null
date: '2023-04-28T14:33:25.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-pub-sub-in-redis
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/image-332-1.png
tags:
- name: messaging
  slug: messaging
- name: Redis
  slug: redis
seo_title: Pub/Sub dans Redis – Comment utiliser le modèle de messagerie Publish/Subscribe
seo_desc: 'When you''re working on an application that needs to be easily maintainable,
  scalable, and performant, the Publish/Subscribe messaging pattern is a good choice.

  The idea behind it is simple, but powerful. We have senders called publishers. Their
  sole ...'
---

Lorsque vous travaillez sur une application qui doit être facilement maintenable, évolutive et performante, le modèle de messagerie Publish/Subscribe est un bon choix.

L'idée derrière ce modèle est simple, mais puissante. Nous avons des expéditeurs appelés *publishers*. Leur seul rôle est d'envoyer ou de *publier* des messages. Ils ne se soucient pas de qui va les recevoir ou si quelqu'un les recevra. Ils envoient simplement les messages et les oublient. Et ils le font via des *canaux*.

Pensez à eux comme, par exemple, des chaînes de télévision. Nous avons des chaînes sportives, des chaînes de prévisions météorologiques, des chaînes de cuisine, et ainsi de suite. Chaque publisher envoie ses messages à un certain canal, et quiconque est *abonné* à ce canal pourra recevoir ces messages.

C'est ici que les *subscribers* entrent en jeu. Ils peuvent s'abonner à un ou plusieurs canaux et commencer à recevoir les messages diffusés dans ceux-ci.

Comme nous l'avons déjà mentionné, les messages doivent être envoyés et oubliés. Cela signifie que si un subscriber s'abonne à un certain canal, tous les messages qui ont été envoyés précédemment dans ce canal ne seront pas disponibles pour ce subscriber.

Grâce à la nature de ce type d'architecture, nous pouvons facilement atteindre un faible couplage entre les différents composants et fournir une base solide pour construire des applications robustes et faciles à maintenir.

Par exemple, imaginez une situation où nous devons remplacer ou améliorer la partie publication de notre système – disons ajouter plus de publishers, plus de canaux ou autre. Puisque les deux parties sont isolées, ce qui signifie que les publishers ne se soucient pas des subscribers et vice versa, nous pourrions facilement le faire sans nous soucier de casser une autre partie du système. Nous ajoutons simplement les nouveaux publishers. Ensuite, plus tard, lorsqu'un subscriber vient sur les canaux pertinents, il commence simplement à les utiliser.

## Qu'est-ce que Redis ?

L'idée initiale derrière Redis était de servir de solution de cache en mémoire, comme alternative à son ancêtre [Memcached](https://www.memcached.org/).

Mais de nos jours, c'est une solution tout-en-un, fournissant un magasin de structures de données en mémoire, une base de données clé-valeur, un courtage de messages, et ainsi de suite. Cela en fait un candidat parfait pour construire une application qui nécessite une solution de cache vraiment rapide ainsi que certaines des autres fonctionnalités mentionnées précédemment. Surtout si la performance de l'application est cruciale pour son utilisation régulière.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-333.png align="left")

*Comparaison de performance de Redis (source : google)*

L'un des plus grands avantages de l'utilisation de Redis est la grande communauté et les ressources techniques que vous pouvez trouver en ligne. Beaucoup de ces ressources sont gratuites, et il existe des plateformes en ligne qui offrent des services gratuits.

Redis inclut également dans son arsenal une solution cloud. Si vous souhaitez l'essayer vous-même, vous pouvez aller [ici](https://redis.com/try-free/) et enregistrer un compte gratuit ou utiliser leur offre initiale de coupon.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-334.png align="left")

*Page d'inscription/connexion à Redis Enterprise Cloud*

## Pub/Sub dans Redis

### Qu'est-ce que pub/sub ?

[Les canaux Publish/Subscribe dans Redis](https://redis.io/docs/manual/pubsub/) est l'une des fonctionnalités que je n'ai pas mentionnées ci-dessus, mais elle est incluse dans les dernières versions de Redis. Il s'agit de leur implémentation du [modèle de messagerie pub/sub](https://redis.io/docs/manual/pubsub/), où nous avons des publishers et des subscribers qui échangent des messages via des canaux.

Nous allons en parler brièvement ci-dessous, puis le voir en pratique dans une [petite application de démonstration](https://github.com/mihailgaberov/redis-pub-sub-visualized) que j'ai préparée pour vous.

### Comment fonctionne Redis pub/sub ?

Nous avons des publishers (les producteurs de messages), des canaux (par lesquels les messages passent) et des subscribers (les récepteurs des messages). Qui reçoit quoi dépend uniquement de qui est abonné à quel canal.

**Voyons comment cela fonctionne dans un exemple :**

Si nous avons créé trois publishers qui publieront des messages sur trois canaux différents. Appelons-les canaux 1, 2 et 3. Nous avons également trois subscribers, appelons-les subscribers A, B et C.

Maintenant, imaginons que le subscriber A écoute les messages sur les trois canaux, c'est-à-dire qu'il est abonné à ceux-ci. Et les subscribers B et C sont abonnés aux canaux 2 et 3. Cela signifie que lorsque l'un des trois publishers envoie un message, le subscriber A le recevra. Et les subscribers B et C recevront les messages envoyés uniquement par les publishers 2 et 3, car ils n'écoutent que les messages sur ces canaux (2 et 3).

Remarquez que nous avons deux entités utilisant un canal – l'une envoie, l'autre reçoit – mais elles sont totalement indépendantes. Et les messages envoyés ne sont pas conservés. Une fois qu'ils sont envoyés par le publisher, ils sont oubliés. Les seules entités qui sont abonnées au moment de l'envoi les recevront.

### Comment utiliser pub/sub dans Redis

Il existe une pléthore de bibliothèques clientes que vous pouvez utiliser avec Redis. Il y a une [page dédiée](https://redis.io/docs/clients/) où tout le monde peut aller et en choisir une, en fonction des besoins spécifiques du projet ou simplement de votre langage de programmation préféré.

Les gens chez Redis ont également marqué certains de ces dépôts comme *recommandés*, ce qui facilite le choix si vous êtes nouveau dans tout cela.

Pour notre démonstration ci-dessous, j'ai utilisé [ioredis](https://github.com/luin/ioredis), un client Redis complet pour Node.js. J'ai choisi celui-ci parce que l'interface utilisateur de l'application de démonstration est construite avec React et Node.js et que mon code serveur s'intègre bien avec celui-ci.

## Démonstration de Redis Pub/Sub

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-336.png align="left")

*Application de visualisation Redis Pub/Sub*

C'est l'heure de la démonstration !

L'idée derrière l'[application de démonstration](https://github.com/mihailgaberov/redis-pub-sub-visualized) est de montrer visuellement comment le modèle fonctionne.

Ce que vous verrez lorsque vous l'ouvrirez pour la première fois, ce sont trois boutons pour publier des messages simples (nouvelles) dans les trois chaînes de télévision imaginaires : Météo, Sports et Musique.

Les cartes sous les boutons de publication sont les subscribers. Une fois que vous déplacez le curseur de votre souris sur l'une d'elles, elle se retournera sur son côté arrière et vous verrez trois boutons. Vous pouvez utiliser chacun de ces boutons pour vous abonner au canal pertinent.

Une fois qu'un subscriber est inscrit sur un canal et que vous cliquez sur l'icône ou le bouton de publication pour ce canal, vous verrez une nouvelle exemple apparaître sur le côté avant de la carte.

Jouez avec différentes combinaisons de publishers/subscribers et voyez le résultat.

J'espère que cela vous donnera une meilleure compréhension de ce que j'ai expliqué dans l'exemple ci-dessus.

### **Comment exécuter l'application de démonstration localement**

Afin d'installer et d'exécuter l'application de démonstration localement, suivez les étapes ci-dessous (toutes les commandes sont considérées comme étant exécutées depuis le répertoire racine du projet) :

**Exécuter le frontend :**

`cd client yarn && yarn dev`

**Exécuter le backend :**

`cd server && yarn yarn start`

Et enfin, utilisez votre installation locale de Docker (si vous n'en avez pas, vous pouvez l'obtenir [ici](https://docs.docker.com/get-docker/)) pour exécuter ceci :

```python
docker run -p 6379:6379 redislabs/redismod:preview
```

C'est probablement le moyen le plus simple d'avoir une copie de Redis en cours d'exécution localement. L'autre option serait d'utiliser directement [Redis Cloud](https://redis.com/try-free/) et de déployer l'application en ligne. C'est une option que j'explore encore et si j'y arrive, je déployerai l'application complète et vous tiendrai informé.

## Conclusion

Cet article vous a introduit au sujet du modèle de messagerie pub/sub. Il est important de se rappeler que chaque fois que nous voulons construire une application hautement performante avec une architecture faiblement couplée et des fonctionnalités de messagerie en temps réel, envisagez d'utiliser le modèle Publish/Subscribe et Redis en particulier.

En fait, beaucoup des applications réelles qui utilisent Redis sont basées sur des tableaux de bord. Cela signifie qu'il y a généralement un bel écran de tableau de bord, montrant différentes données, souvent mises à jour en temps réel.

Imaginez, par exemple, un système montrant le trafic dans une zone spécifique. Ce type de logiciel est un candidat parfait pour tirer parti des avantages de pub/sub. Et dans de nombreux cas, cela est réalisé en utilisant Redis.

Dans tous les cas, en tant que développeurs et ingénieurs, nous devons toujours être guidés par les besoins spécifiques du projet sur lequel nous travaillons. Chaque fois que nous décidons d'introduire un nouveau modèle ou une nouvelle technologie, nous devons le faire avec soin et l'étayer par des recherches sérieuses.