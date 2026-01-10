---
title: La Checklist Ultime pour Node.js en Production
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-24T11:32:03.000Z'
originalURL: https://freecodecamp.org/news/node-js-production-checklist
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/screely-1585049597841.png
tags:
- name: node
  slug: node
- name: Node.js
  slug: nodejs
- name: performance
  slug: performance
- name: servers
  slug: servers
- name: web performance
  slug: web-performance
- name: website development,
  slug: website-development
seo_title: La Checklist Ultime pour Node.js en Production
seo_desc: "By Mehul Mohan\nAre you doing this Node thing right on production? Let's\
  \ see some common mistakes people make running Node on production (coming straight\
  \ from my own projects - like codedamn) and how they can be mitigated. \nYou can\
  \ use this as your ch..."
---

Par Mehul Mohan

Faites-vous les choses correctement avec Node en production ? Voyons quelques erreurs courantes que les gens commettent en exécutant Node en production (directement issues de mes propres projets - comme [codedamn](https://codedamn.com)) et comment elles peuvent être atténuées.

Vous pouvez utiliser cela comme votre checklist en production lorsque vous déployez des applications Node. Puisque cet article traite des _bonnes pratiques pour la production_, beaucoup de ces points ne s'appliqueront pas lorsque vous développez des applications sur votre système local.

## Exécuter Node en mode cluster/processus Node séparés

Rappelez-vous que Node est monothread. Il peut déléguer beaucoup de choses (comme les requêtes HTTP et les lectures/écritures de système de fichiers) à l'OS qui les gère dans un environnement multithread. Mais malgré tout, le code QUE VOUS ÉCRIVEZ, la logique de l'application, s'exécute toujours dans un seul thread.

En s'exécutant dans un seul thread, votre processus Node est toujours limité à un seul cœur de votre machine. Donc, si vous avez un serveur avec plusieurs cœurs, vous gaspillez de la puissance de calcul en exécutant Node une seule fois sur votre serveur.

Que signifie "exécuter Node une seule fois" ? Vous voyez, les systèmes d'exploitation ont un planificateur intégré qui est responsable de la manière dont l'exécution des processus est distribuée sur les CPU de la machine. Lorsque vous exécutez seulement 2 processus sur une machine à 2 cœurs, l'OS détermine qu'il est préférable d'exécuter les deux processus sur des cœurs séparés pour en tirer le maximum de performance.

Une chose similaire doit être faite avec Node. Vous avez deux options à ce stade :

1. **Exécuter Node en mode cluster** - Le mode cluster est une architecture intégrée à Node lui-même. En termes simples, Node fork plus de processus et distribue la charge à travers un seul processus maître.
2. **Exécuter des processus Node indépendamment** - Cette option est légèrement différente de la précédente dans le sens où vous n'avez plus de processus maître contrôlant les processus Node enfants. Cela signifie que lorsque vous lancez différents processus Node, ils s'exécuteront complètement indépendamment les uns des autres. Pas de mémoire partagée, pas d'IPC, pas de communication, nada.

Selon une [réponse sur stackoverflow](https://stackoverflow.com/a/47122606/2513722), cette dernière option (point 2) performe bien mieux que la première (point 1) mais est un peu plus difficile à configurer.

Pourquoi ? Parce que dans une application Node, il n'y a pas seulement de la logique applicative, mais presque toujours, lorsque vous configurez des serveurs dans le code Node, vous devez lier des ports. Et un seul codebase d'application ne peut pas lier le même port deux fois sur le même OS.

Ce problème est cependant facilement résoluble. Les variables d'environnement, les conteneurs Docker, le proxy frontal NGiNX, etc., sont quelques-unes des solutions pour cela.

## Limiter le débit de vos endpoints

Admettons-le. Tout le monde dans le monde n'a pas les meilleures intentions pour votre architecture. Bien sûr, des attaques comme les DDoS sont simplement très compliquées à atténuer, et même des géants comme GitHub tombent lorsque quelque chose comme cela se produit.

Mais le moins que vous puissiez faire est d'empêcher un script-kiddie de faire tomber votre serveur simplement parce que vous avez un endpoint API coûteux exposé depuis votre serveur sans aucune limitation de débit en place.

Si vous utilisez Express avec Node, il existe 2 beaux packages qui fonctionnent parfaitement ensemble pour limiter le débit du trafic sur la couche 7 :

1. Express Rate Limit - [https://www.npmjs.com/package/express-rate-limit](https://www.npmjs.com/package/express-rate-limit)
2. Express Slow Down - [https://www.npmjs.com/package/express-slow-down](https://www.npmjs.com/package/express-slow-down)

Express Slow Down ajoute en fait un délai incrémental à vos requêtes au lieu de les abandonner. De cette façon, les utilisateurs légitimes, s'ils DDoS par accident (super activité de clics ici et là), sont simplement ralentis et ne sont pas limités en débit.

D'un autre côté, s'il y a un script-kiddie qui exécute des scripts pour faire tomber le serveur, Express rate limiter surveille et limite le débit de cet utilisateur particulier, en fonction de l'IP de l'utilisateur, du compte utilisateur, ou de tout autre chose que vous voulez.

La limitation de débit pourrait (devrait !) être appliquée également sur la couche 4 (la couche 4 signifie bloquer le trafic avant de découvrir son contenu - HTTP) via l'adresse IP. Si vous le souhaitez, vous pouvez configurer une règle NGiNX qui bloque le trafic sur la couche 4 et rejette le flux de trafic provenant d'une seule IP, sauvant ainsi vos processus serveur de la surcharge.

## Utiliser un serveur frontal pour la terminaison SSL

Node fournit une prise en charge intégrée pour les poignées de main SSL avec le navigateur en utilisant le module de serveur `https` combiné avec les certificats SSL requis.

Mais soyons honnêtes ici, votre application ne devrait pas se soucier du SSL en premier lieu de toute façon. Ce n'est pas quelque chose que la logique de l'application devrait faire. Votre code Node ne devrait être responsable que de ce qui se passe avec la requête, pas du pré-traitement et du post-traitement des données entrant et sortant de votre serveur.

La terminaison SSL fait référence à la conversion du trafic de HTTPS en HTTP. Et il existe des outils bien meilleurs que Node pour cela. Je recommande NGiNX ou HAProxy. Les deux ont des versions gratuites disponibles qui font le travail et déchargent la terminaison SSL de Node.

## Utiliser un serveur frontal pour servir des fichiers statiques

Encore une fois, au lieu d'utiliser des méthodes intégrées comme `express.static` pour servir des fichiers statiques, utilisez des serveurs proxy inverse frontaux comme NGiNX pour servir des fichiers statiques depuis le disque.

Tout d'abord, NGiNX peut le faire plus rapidement que Node (parce qu'il est construit de zéro pour ne faire que cela). Mais cela décharge également le service de fichiers d'un processus Node monothread qui pourrait utiliser ses cycles de processeur pour quelque chose de mieux.

Non seulement cela - les serveurs proxy frontaux comme NGiNX peuvent également vous aider à livrer du contenu plus rapidement en utilisant la compression GZIP. Vous pouvez également définir des en-têtes d'expiration, mettre en cache des données, et bien plus encore, ce qui n'est pas quelque chose que nous devrions attendre de Node (Cependant, Node peut toujours le faire).

## Configurer la gestion des erreurs

Une gestion des erreurs appropriée peut vous éviter des heures de débogage et de tentative de reproduction de bugs difficiles. Sur le serveur, il est particulièrement facile de configurer une architecture pour la gestion des erreurs parce que c'est vous qui l'exécutez. Je recommande des outils comme [Sentry](https://sentry.io) avec Node qui enregistre, signale et vous envoie un email chaque fois que le serveur plante en raison d'une erreur dans le code source.

Une fois que cela est en place, il est temps de redémarrer le serveur lorsqu'il plante afin que tout le site ne tombe pas pendant des heures jusqu'à ce que vous le remettiez manuellement en ligne.

Pour cela, vous pouvez utiliser un gestionnaire de processus comme [PM2](https://www.npmjs.com/package/pm2). Ou encore mieux, utilisez un environnement conteneurisé Docker avec des politiques comme `restart: always` avec des limites de mémoire et de disque appropriées configurées.

La configuration Docker garantit que même si votre conteneur s'exécute en OME, le processus redémarre (ce qui pourrait ne pas se produire dans un environnement PM2, car l'OS pourrait tuer PM2 s'il y a une fuite de mémoire quelque part dans un processus en cours d'exécution).

## Configurer les logs correctement

Toutes les réponses se trouvent dans les logs. Piratages de serveur, plantages de serveur, comportements d'utilisateurs suspects, etc. Pour cela, vous devez vous assurer que :

1. Chaque tentative de requête est enregistrée avec l'adresse IP/méthode de requête/chemin accédé, essentiellement autant d'informations que vous pouvez enregistrer (à l'exception des informations privées comme les mots de passe et les informations de carte de crédit, bien sûr)
2. Cela peut être réalisé grâce au package [morgan](https://www.npmjs.com/package/morgan)
3. Configurez des **logs de flux de fichiers** en production au lieu de la sortie console. Cela est plus rapide, plus facile à voir et vous permet d'exporter les logs vers des services de visualisation de logs en ligne.
4. Tous les messages de log n'ont pas le même poids. Certains logs sont simplement là pour le débogage, tandis que si certains sont présents, cela pourrait indiquer une situation critique (comme un piratage de serveur ou un accès non autorisé). Utilisez winston-logger pour enregistrer différents niveaux de logs.
5. Configurez la **rotation des logs** afin de ne pas obtenir une taille de log en Go après un mois ou plus, lorsque vous voyez le serveur.
6. **GZIP** vos fichiers de log après rotation. Le texte est bon marché, et est hautement compressible et facile à stocker. Vous ne devriez jamais rencontrer de problème avec les logs texte tant qu'ils sont compressés et que vous exécutez un serveur avec un espace disque décent (25 Go+).

## Conclusion

Il est facile de noter quelques pratiques en production qui pourraient vous éviter des larmes et des heures de débogage plus tard. Assurez-vous de suivre ces bonnes pratiques et faites-moi savoir ce que vous en pensez en disant Bonjour sur mon [compte twitter](https://twitter.com/mehulmpt).

Si vous avez aimé cet article, rencontrons-nous sur les réseaux sociaux. Voici mon [Instagram](https://instagram.com/mehulmpt) et [Twitter](https://twitter.com/mehulmpt). Je suis super actif, et j'adorerais discuter ! Connectons-nous.

Paix !  
Mehul