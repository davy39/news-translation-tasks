---
title: Test de charge HAProxy (Partie 1)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-19T17:55:41.000Z'
originalURL: https://freecodecamp.org/news/load-testing-haproxy-part-1-f7d64500b75d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*cj6DXYTZl0q9RDR-3mil7g.jpeg
tags:
- name: Devops
  slug: devops
- name: Haproxy
  slug: haproxy
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: Test de charge HAProxy (Partie 1)
seo_desc: 'By Sachin Malhotra

  This is the first post in a 3 part series on load testing HAProxy, which is a reliable,
  high performant TCP/HTTP load balancer.

  Load Testing? HAProxy? If all this seems greek to you, don’t worry. I will provide
  inline links to read...'
---

Par Sachin Malhotra

Ceci est le premier article d'une série en 3 parties sur le test de charge HAProxy, qui est un équilibreur de charge TCP/HTTP fiable et haute performance.

Test de charge ? HAProxy ? Si tout cela vous semble du grec, ne vous inquiétez pas. Je fournirai des liens en ligne pour lire tout ce dont je parle dans cet article de blog.

Pour référence, notre stack actuelle est :

* Instances hébergées sur [Amazon EC2](https://aws.amazon.com/ec2/) (ce qui ne devrait pas avoir d'importance)
* Ubuntu 14.04 (Trusty) pour le système d'exploitation
* [Supervisor](http://supervisord.org/) pour la gestion des processus

En production, nous avons environ 30 équilibreurs de charge [HAProxy](https://serversforhackers.com/load-balancing-with-haproxy) qui nous aident à router notre trafic vers les serveurs backend qui sont en mode autoscaling et n'ont donc pas un nombre fixe. Le nombre de serveurs backend varie de 12 à 32 tout au long de la journée.

[Cet article](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts) devrait vous aider à vous mettre à niveau sur les bases de l'équilibrage de charge et comment cela fonctionne avec HAProxy. Il expliquera également quels algorithmes de routage sont disponibles.

Revenons à notre sujet, qui est le test de charge HAProxy.

Nous n'avons jamais mis d'effort dédié pour trouver les limites de notre configuration HAProxy dans la gestion des requêtes HTTP et HTTPS. Actuellement, en production, nous avons des instances HAProxy de 4 cœurs et 30 Gig.

[**Présentation des instances Amazon EC2 R4, la prochaine génération d'instances optimisées pour la mémoire**](https://aws.amazon.com/about-aws/whats-new/2016/11/introducing-amazon-ec2-r4-instances-the-next-generation-of-memory-optimized-instances/)
[_Vous pouvez maintenant lancer des instances R4, la prochaine génération d'instances Amazon EC2 optimisées pour la mémoire, offrant une plus grande..._aws.amazon.com](https://aws.amazon.com/about-aws/whats-new/2016/11/introducing-amazon-ec2-r4-instances-the-next-generation-of-memory-optimized-instances/)

Alors que j'écris cet article, nous sommes en train de déplacer tout notre trafic (HTTP) vers HTTPS (c'est-à-dire, trafic chiffré). Mais avant d'aller plus loin, nous avions besoin de réponses définitives aux questions suivantes :

1. **Quel est l'impact lorsque nous passons notre trafic de Non-SSL à SSL ?** Le CPU devrait définitivement subir un impact car la poignée de main SSL n'est pas une poignée de main à 3 voies normale, c'est plutôt une poignée de main à 5 voies et après que la poignée de main soit complète, la communication ultérieure est chiffrée en utilisant la clé secrète générée pendant la poignée de main et cela est susceptible de prendre du CPU.
2. **Quelles sont les autres limites matérielles/logicielles qui pourraient être atteintes en production à la suite de la terminaison SSL au niveau HAProxy**. Nous pourrions également opter pour l'option SSL PassThrough fournie par HAProxy qui termine/déchiffre la connexion SSL au niveau des serveurs backend. Cependant, la terminaison SSL au niveau HAProxy est plus performante et c'est ce que nous avons l'intention de tester.
3. **Quel est le meilleur matériel requis en production pour supporter le type de charge que nous voyons aujourd'hui**. Le matériel existant évoluera-t-il ou avons-nous besoin de machines plus grandes ? C'était également l'une des principales questions auxquelles nous voulions une réponse via ce test.

À cette fin, nous avons mis en place un effort dédié pour tester la charge de HAProxy version 1.6 afin de trouver des réponses aux questions ci-dessus. Je ne vais pas décrire l'approche que nous avons prise ni les résultats de cet exercice dans cet article de blog.

Plutôt, je vais discuter d'un aspect important de tout exercice de test de charge que la plupart d'entre nous ont tendance à ignorer.

### L'Ulimiter

Si vous avez déjà fait un quelconque test de charge ou hébergé un serveur servant beaucoup de requêtes concurrentes, vous avez définitivement rencontré le redoutable problème de "_Trop de fichiers ouverts_ ".

![Image](https://cdn-media-1.freecodecamp.org/images/jJVTKXWZ4vnrtzBDGOop2kXpAyF6VgIJCINm)

Une partie importante de tout exercice de test de stress est la capacité de votre client de test de charge à établir de nombreuses connexions concurrentes à votre serveur backend ou au proxy comme HAProxy entre les deux.

Très souvent, nous finissons par être un goulot d'étranglement sur le client qui n'est pas capable de générer la quantité de charge que nous attendons de lui. La raison de cela n'est pas que le client ne fonctionne pas de manière optimale, mais quelque chose d'autre entièrement au niveau matériel.

Ulimit est utilisé pour restreindre le nombre de ressources au niveau utilisateur. Pour toutes les fins pratiques concernant les environnements de test de charge, ulimit nous donne le nombre de descripteurs de fichiers qui peuvent être ouverts par un seul processus sur le système. Sur la plupart des machines, si vous vérifiez la limite des descripteurs de fichiers, elle s'avère être ce nombre = **1024.**

![Image](https://cdn-media-1.freecodecamp.org/images/GoZSUt-3YQ1l-DCpkEG-KGbIPk9kaCo4ekDz)
_Configuration Ulimit de Staging_

Comme vous pouvez le voir, le nombre de fichiers ouverts est de 1024 sur notre configuration de staging. L'ouverture d'une nouvelle connexion TCP / socket compte également comme un fichier ouvert ou un descripteur de fichier et donc la limitation.

Ce que cela signifie généralement, c'est qu'un seul processus client ne peut ouvrir que 1024 connexions aux serveurs backend et pas plus. Cela signifie que vous devez augmenter cette limite à un nombre très élevé sur votre environnement de test de charge avant de continuer. Vérifiez le paramètre ulimit que nous avons sur nos machines de production.

![Image](https://cdn-media-1.freecodecamp.org/images/73vqpr9SdmsitJo7dkHMJRlNlUTiJ379QFLs)
_Configuration Ulimit de niveau Production_

Ces informations sont ce que vous trouveriez généralement après 10 secondes de recherche sur Google, mais gardez à l'esprit que _ulimit n'est pas garanti de vous donner les limites que vos processus ont réellement !_ Il y a un million de choses qui peuvent modifier les limites d'un processus après (ou avant) que vous ayez initialisé votre shell. Ce que vous devriez faire à la place, c'est lancer `top`, `[htop](http://hisham.hm/htop/)`, `ps`, ou tout ce que vous voulez utiliser pour obtenir l'ID du processus problématique, et faire un `cat /proc/{process_id}/limits` :

![Image](https://cdn-media-1.freecodecamp.org/images/TWBwrTFoK4mEBqVA0oup1iVkyhlG9ceHxStr)

> Le nombre maximal de fichiers ouverts pour ce processus spécifique est différent des limites système que nous avons sur ce serveur.

Passons à la partie intéressante. Augmenter les limites :D

### Le contenu pour lequel vous êtes venu ici : Augmenter la limite

Il existe deux façons de changer le paramètre ulimit sur une machine.

1. **_ulimit -n <une_valeur_**. Cela changera les paramètres ulimit uniquement pour la session shell actuelle. Dès que vous ouvrez une autre session shell, vous revenez à la case départ, c'est-à-dire 1024 descripteurs de fichiers. Donc ce n'est probablement pas ce que vous voulez.
2. **_fs.file-max = 500000_**. Ajoutez cette ligne à la fin du fichier **_/etc/sysctl.conf._** Et ajoutez ce qui suit :
`* soft nofile` **_500000_**
`* hard nofile` **_500000_**
`root soft nofile` **_500000_**
`root hard nofile` **_500000_**
au fichier **_/etc/security/limits.conf._**

Le * représente essentiellement que nous définissons ces valeurs pour tous les utilisateurs sauf root. "soft ou hard" représente essentiellement les limites souples ou strictes. L'entrée suivante spécifie l'élément pour lequel nous voulons changer les valeurs de limite, c'est-à-dire nofile dans ce cas, ce qui signifie le nombre de fichiers ouverts. Et enfin, nous avons la valeur que nous voulons définir, qui dans ce cas est 500000. Le * ici ne s'applique pas à un utilisateur root, d'où les deux dernières lignes spécialement pour l'utilisateur root.

Après avoir fait cela, vous devez redémarrer le système. Malheureusement oui :( Et les changements devraient se refléter dans la commande ulimit -n.

![Image](https://cdn-media-1.freecodecamp.org/images/ttEJ2k3gq6WNzPyB9kJz7JY9ir4FHatB7yxq)

Hourra !. Faites-vous une tape dans le dos. Vous avez réussi à changer les paramètres ulimit pour le système. Cependant, il n'est pas nécessaire que ce changement affecte tous les processus utilisateur en cours d'exécution sur le système. Il est tout à fait possible que même après avoir changé l'ulimit système, vous constatiez que _/etc/<pid>/_limits vous donne un nombre plus petit que ce que vous pourriez vous attendre à trouver.

![Image](https://cdn-media-1.freecodecamp.org/images/5NiE02G4N9eCU84BvXHJUcJVD7VM37ls0wUq)

Dans ce cas, vous avez presque certainement un gestionnaire de processus, ou quelque chose de similaire qui perturbe vos limites. Vous devez garder à l'esprit que les processus héritent des limites de leurs processus parents. Donc si vous avez quelque chose comme un Supervisor qui gère vos processus, ils hériteront des paramètres du démon Supervisor et cela annule toute modification que vous apportez aux limites au niveau du système.

[Supervisor a une variable de configuration](http://supervisord.org/configuration.html#supervisord-section-values) qui définit la limite de descripteur de fichier de son processus principal. Apparemment, ce paramètre est à son tour hérité par tous les processus qu'il lance. Pour remplacer le paramètre par défaut, vous pouvez ajouter la ligne suivante à `/etc/supervisor/supervisord.conf`, dans la section `[supervisord]` :

```
minfds=500000
```

La mise à jour de cela entraînera tous les processus enfants contrôlés par supervisor héritant de cette limite mise à jour. Vous devez simplement redémarrer le démon supervisor pour que ce changement prenne effet.

N'oubliez pas de faire cela sur toute machine qui a l'intention d'avoir beaucoup de connexions concurrentes ouvertes. Que ce soit le client dans un scénario de test de charge ou un serveur essayant de servir beaucoup de requêtes concurrentes.

[Dans la Partie 2](https://medium.com/p/4c8677780df6), nous apprendrons comment gérer le **_monstre de la plage de ports Sysctl_**.

Faites-moi savoir comment cet article de blog vous a aidé. De plus, veuillez recommander (❤) cet article si vous pensez qu'il peut être utile pour quelqu'un.