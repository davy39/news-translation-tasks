---
title: Test de charge HAProxy (Partie 2)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-26T18:11:35.000Z'
originalURL: https://freecodecamp.org/news/load-testing-haproxy-part-2-4c8677780df6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*s2S16ZXbIxtsYIG87aOadg.png
tags:
- name: Devops
  slug: devops
- name: Docker
  slug: docker
- name: Haproxy
  slug: haproxy
- name: Linux
  slug: linux
- name: Web Development
  slug: web-development
seo_title: Test de charge HAProxy (Partie 2)
seo_desc: 'By Sachin Malhotra

  This is the second part in the 3 part series on performance testing of the famous
  TCP load balancer and reverse proxy, HAProxy. If you haven’t gone through the previous
  post, I would highly suggest you do so to get some sort of con...'
---

Par Sachin Malhotra

Il s'agit de la deuxième partie d'une série en 3 parties sur les tests de performance du célèbre équilibreur de charge TCP et proxy inverse, HAProxy. Si vous n'avez pas lu le précédent article, je vous suggère vivement de le faire pour avoir un certain contexte.

[**Test de charge HAProxy (Partie 1)**](https://medium.com/@sachinmalhotra/load-testing-haproxy-part-1-f7d64500b75d)
[_Test de charge ? HAProxy ? Si tout cela vous semble du grec, ne vous inquiétez pas. Je fournirai des liens en ligne pour lire ce qui est..._medium.com](https://medium.com/@sachinmalhotra/load-testing-haproxy-part-1-f7d64500b75d)

Cet article se concentrera sur le problème d'épuisement des ports TCP et sur la manière dont nous pouvons le gérer. Dans le dernier article, nous avons parlé de la manière dont nous pouvons ajuster les paramètres ulimit au niveau du noyau et du processus. Cet article se concentre sur la modification des paramètres sysctl pour surmonter les limites d'épuisement des ports.

### Plage de ports locaux SYSCTL et sockets orphelins

L'épuisement des ports est un problème qui entraînera l'échec des communications TCP avec d'autres machines sur le réseau. La plupart du temps, un seul processus conduit à ce problème et le redémarrer résoudra le problème temporairement. Cependant, il reviendra vous hanter en quelques heures ou jours selon la charge du système.

L'épuisement des ports ne signifie pas que les ports se fatiguent réellement. Bien sûr, ce n'est pas possible car l'ordinateur n'est pas humain et les ports ne sont pas capables de se fatiguer. La vérité est beaucoup plus insidieuse. L'épuisement des ports signifie simplement que le système n'a plus de ports éphémères disponibles pour communiquer avec d'autres machines/serveurs.

Avant d'aller plus loin, comprenons ce qui constitue une connexion TCP et ce que signifie réellement une connexion entrante et une connexion sortante.

Dans la majorité des cas, lorsque nous parlons de connexions TCP et de haute scalabilité et de la capacité à supporter des connexions simultanées, nous faisons généralement référence au nombre de connexions entrantes.

Par exemple, HAProxy écoute sur le port 443 pour de nouvelles connexions entrantes. Si nous disons que HAProxy peut supporter X nombre de connexions simultanées, ce que nous voulons vraiment dire, c'est X nombre de connexions entrantes et toutes sont établies sur le port 443 de la machine HAProxy.

Si ces connexions sont entrantes pour HAProxy, alors elles doivent être sortantes pour les machines clientes où la connexion a été initiée. Tout type de communication de la part du client nécessite qu'ils initient des connexions sortantes vers les serveurs.

> Lorsqu'une connexion est établie via TCP, une socket est créée à la fois sur l'hôte local et l'hôte distant. Ces sockets sont ensuite connectées pour créer une paire de sockets, qui est décrite par un 4-tuple unique constitué de l'adresse IP locale et du port ainsi que de l'adresse IP distante et du port.

![Image](https://cdn-media-1.freecodecamp.org/images/3iI-8Br8X2Lu4xrYQ3Nw-nUVRXTcDJArAUNX)
_3 connexions TCP du client au serveur/proxy_

Si vous avez compris le concept du quadruple, vous réaliserez que dans une connexion sortante ou plutôt plusieurs connexions sortantes vers le MÊME serveur backend, deux choses restent toujours les mêmes, c'est-à-dire l'IP de destination et le port de destination. En supposant que nous ne prenons en compte qu'une seule machine cliente, l'IP du client restera également la même.

Cela signifie que le nombre de connexions sortantes dépend du nombre de ports clients qui peuvent être utilisés pour établir la connexion. Lors de l'établissement d'une connexion sortante, le port source est sélectionné aléatoirement dans la plage de ports éphémères et ce port est libéré une fois la connexion détruite. C'est pourquoi ces ports sont appelés ports éphémères.

Par défaut, le nombre total de ports éphémères locaux disponibles est d'environ 28 000.

![Image](https://cdn-media-1.freecodecamp.org/images/JKzruPQY3heS9Sddou2j7-Fu6g-eELbySwxD)

Vous pourriez penser que 28k est un nombre assez grand et que rien ne peut probablement causer l'utilisation de 28k connexions à un moment donné. Pour comprendre cela, nous devons comprendre le cycle de vie des connexions TCP.

Lors de la poignée de main TCP, l'état de la connexion passe de

SYN_SENT → SYN_RECV → ESTABLISHED. Une fois que la connexion est dans l'état ESTABLISHED, cela signifie que la connexion TCP est maintenant active. Cependant, une fois la connexion terminée, le port local qui était utilisé précédemment ne devient pas actif immédiatement.

La connexion entre dans un état connu sous le nom d'état TIME_WAIT pendant une période de 120 secondes avant d'être finalement terminée. Il s'agit d'un paramètre au niveau du noyau qui existe pour permettre au réseau d'ignorer les paquets retardés ou désordonnés.

> Si vous faites le calcul, il ne faudra pas plus de 230 connexions simultanées par seconde avant que la limite apparemment grande de 28 000 ports éphémères sur le système soit atteinte. Cette limite est très facile à atteindre sur des proxys comme HAProxy ou NGINX car tout le trafic est acheminé via eux vers les serveurs backend.

Lorsqu'une connexion entre dans l'état TIME_WAIT, elle est connue sous le nom de socket orphelin car la socket TCP dans ce cas n'est pas maintenue par un descripteur de socket mais est toujours maintenue par le système pendant le temps désigné, c'est-à-dire 120 secondes par défaut.

### Comment détecter cela ?

Assez de théorie. Passons directement à la manière d'identifier si cette limite a été atteinte sur le système. Il y a deux commandes que j'adore utiliser pour découvrir le nombre de connexions TCP établies sur le système.

#### ss (Statistiques des sockets)

La commande de statistiques des sockets est une sorte de remplacement de la célèbre commande netstat et est beaucoup plus rapide que la commande netstat pour rendre les informations car elle récupère les informations de connexion directement depuis l'espace noyau. Pour comprendre les différentes options supportées par la commande ss, consultez

[**10 exemples de la commande Linux ss pour surveiller les connexions réseau**](http://www.binarytides.com/linux-ss-command/)
[_Dans un tutoriel précédent, nous avons vu comment utiliser la commande netstat pour obtenir des statistiques sur les connexions réseau/socket. Cependant..._www.binarytides.com](http://www.binarytides.com/linux-ss-command/)

La commande `ss -s` affichera le nombre total de connexions TCP établies sur la machine. Si vous voyez ce nombre atteindre la marque des 28 000, il est très probable que les ports éphémères aient été épuisés sur cette machine. **ATTENTION :** Ce nombre peut être supérieur à 28k si plusieurs services sont en cours d'exécution sur la même machine sur différents ports.

#### Netstat

La commande netstat est une commande très célèbre qui fournit des informations sur tous types de connexions établies sur la pile réseau de la machine.

```
sudo netstat -anptl
```

Cela vous montrera les détails de toutes les connexions sur la machine. Les détails incluent

* adresse locale
* adresse distante
* état de la connexion
* pid du processus

Nous pouvons également utiliser cela pour voir si un seul processus a établi 28k connexions vers un serveur sortant, ce qui nous donne des informations sur le problème d'épuisement des ports.

![Image](https://cdn-media-1.freecodecamp.org/images/FciLCHwipi6C6HtkdoXzcCdwxszuNdnh0ia5)

Par exemple, l'image ci-dessus montre qu'un processus avec le pid 9758 a établi plusieurs connexions avec la machine étrangère avec l'IP 192.168.0.168 et le port 443. Comme nous pouvons le voir clairement, du côté source, de nombreux ports sont utilisés.

```
sachinm@ip-192-168-0-122:~$ sudo netstat -anptl | grep '192.168.0.168:443' | cut -c69-79 | sort | uniq -c | sort -rn
```

```
5670 ESTABLISHED
```

Cette commande modifiée affichera l'état des différentes connexions établies avec 192.168.0.168 sur le port 443. Actuellement, il y a 5670 connexions. Si cette limite devait atteindre 28k, vous devriez alors envisager des options pour augmenter la plage de ports éphémères sur la machine.

Regardons une autre commande intéressante que vous pouvez émettre à l'extrémité du serveur ou du proxy pour découvrir combien de connexions entrantes ont été établies et par quelles IP. Par exemple, consultez le résultat de la commande suivante

```
ss -tan 'sport = :443' | awk '{print $(NF)" "$(NF-1)}' | sed 's/:[^ ]*//g' | sort | uniq -c
```

![Image](https://cdn-media-1.freecodecamp.org/images/2Y0ZVlMpM4pMtYuxEVyfmqPO4jynRq5JMG3m)

Cela montre qu'il y a environ 14 machines différentes qui ont établi environ 2300 connexions chacune avec 192.168.0.168 et si vous regardez de près la commande, nous avons filtré les résultats uniquement pour le port 443.

Assez de recherche du problème. Plongeons directement dans la recherche de la ou des solutions à ce problème.

### Quelle est la solution ?

![Image](https://cdn-media-1.freecodecamp.org/images/aAiExh9E9Tzw1OyhnhgWQq84zVbOw13kRrXx)

Ne soyez pas effrayé car sysctl se trouve être un monstre amical. Il existe de nombreuses façons de résoudre ce problème.

#### Approche #1

L'une des approches les plus pratiques pour résoudre ce problème et celle que vous finirez probablement par faire, ou plutôt devriez faire, est d'augmenter la plage de ports éphémères locaux à la valeur maximale possible. Comme mentionné précédemment, la plage par défaut est très petite.

```
echo 1024 65535 > /proc/sys/net/ipv4/ip_local_port_range
```

Cela augmentera la plage de ports locaux à une valeur plus grande. Nous ne pouvons pas augmenter la plage au-delà de cela car il ne peut y avoir qu'un maximum de 65535 ports et les 1024 premiers sont réservés pour des services et des fins spécifiques.

Notez que vous pourriez encore rencontrer un goulot d'étranglement sur ce problème. Cependant, au lieu de 28 000 ports utilisés localement, il y en aura 64 000. Ce n'est pas une solution infaillible, mais c'est quelque chose que vous pouvez faire pour vous donner un peu de marge de manœuvre.

Cela signifie-t-il que je ne peux obtenir qu'environ 64k connexions simultanées à partir d'une seule machine cliente ? La réponse est NON.

![Image](https://cdn-media-1.freecodecamp.org/images/ATwP3JIXDuyRoAQZAgfMl4wg5akgnlYqB7Ne)

Dans ce scénario, une seule machine cliente pourra générer environ 120k connexions simultanées car les deux processus se connectent à deux serveurs backend ou proxys différents et donc à des IP de destination différentes.

#### Approche #2

Une autre solution simple consiste à activer une option TCP Linux appelée **tcp_tw_reuse**. Cette option permet au noyau Linux de récupérer un emplacement de connexion à partir d'une connexion dans l'état TIME_WAIT et de le réallouer à une nouvelle connexion.

```
--> vim /etc/sysctl.conf
```

```
--&gt; Ajoutez la ligne suivante à la fin# Autoriser la réutilisation des sockets dans l'état TIME_WAIT pour de nouvelles connexions# uniquement lorsqu'il est sûr du point de vue de la pile réseau.net.ipv4.tcp_tw_reuse = 1
```

```
--&gt; Recharger les paramètres sysctl
sysctl -p
```

#### Approche #3

Utilisez plus de ports serveur. Jusqu'à présent, nous avons parlé des problèmes d'épuisement des ports qui surviennent parce que, dans la logique du quadruplet discutée précédemment, l'IP de destination, le port de destination et l'IP source restent constants. La seule chose qui change est les ports clients.

Cependant, si le serveur écoute sur deux ports différents au lieu d'un seul, alors nous avons deux fois le nombre de ports éphémères disponibles au lieu d'un seul. Cela, combiné avec la première approche, vous donne environ 120k connexions simultanées sur une seule machine.

Vous devez cependant veiller à ce que l'exécution du serveur sur deux ports, ce qui signifie essentiellement l'exécution de deux serveurs sur la même machine, n'ait pas un impact énorme sur le matériel.

#### Approche #4

Dans un scénario de production réel, vous pouvez avoir des millions d'utilisateurs simultanés qui frappent le système en même temps. Mais dans un scénario de test de charge, ces utilisateurs doivent être générés artificiellement par un client s'exécutant sur une machine.

Ici encore, la limite de 65k ports vient mordre du côté client. La seule façon de surmonter cela du point de vue du client est d'augmenter le nombre de machines clientes qui génèrent la charge. Comme vous lirez la prochaine partie de cette série, vous découvrirez que nous avons dû utiliser environ 14 machines différentes pour générer le type de charge que nous voulions tester sur HAProxy.

### Mettre tout cela ensemble

Il n'existe pas une seule configuration qui résoudra tous vos problèmes et fonctionnera comme par magie. C'est toujours la combinaison de plusieurs choses qui fonctionne à la fin.

Pour nous, en tant que prérequis pour les tests de charge de HAProxy, nous avons suivi l'approche #1 et l'approche #2, et finalement l'approche #3 pour générer une énorme... énorme charge de **2 millions de connexions simultanées** sur une seule machine HAProxy.

[Voici la dernière partie de cette série](https://medium.freecodecamp.com/how-we-fine-tuned-haproxy-to-achieve-2-000-000-concurrent-ssl-connections-d017e61a4d27), où je mettrai ensemble tous les composants qui ont permis de générer ce type de charge, les ajustements que nous avons effectués et les enseignements que nous en avons tirés.

Faites-moi savoir comment cet article de blog vous a aidé et restez à l'écoute pour la dernière partie de cette série d'articles. De plus, veuillez recommander (❤) cet article si vous pensez qu'il peut être utile pour quelqu'un.