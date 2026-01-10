---
title: Comment nous avons optimisé HAProxy pour atteindre 2 000 000 de connexions
  SSL simultanées
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-04-16T21:41:24.000Z'
originalURL: https://freecodecamp.org/news/how-we-fine-tuned-haproxy-to-achieve-2-000-000-concurrent-ssl-connections-d017e61a4d27
coverImage: https://cdn-media-1.freecodecamp.org/images/1*H541cEeKLF2O_7wBoUOlPw.png
tags:
- name: Devops
  slug: devops
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Comment nous avons optimisé HAProxy pour atteindre 2 000 000 de connexions
  SSL simultanées
seo_desc: 'By Sachin Malhotra

  If you look at the above screenshot closely, you’ll find two important pieces of
  information:


  This machine has 2.38 million TCP connections established, and

  The amount of RAM being used is around 48 Gigabytes.


  Pretty awesome righ...'
---

Par Sachin Malhotra

Si vous regardez attentivement la capture d'écran ci-dessus, vous trouverez deux informations importantes :

1. Cette machine a **2,38 millions de connexions TCP** établies, et
2. La quantité de RAM utilisée est d'environ **48 Gigaoctets**.

Plutôt impressionnant, n'est-ce pas ? Ce qui serait encore plus impressionnant, ce serait que quelqu'un fournisse les composants de configuration et les réglages nécessaires pour atteindre cette échelle sur une seule machine HAProxy. Eh bien, je vais faire exactement cela dans cet article ;)

Ceci est la dernière partie de la série en plusieurs parties sur les tests de charge de HAProxy. Si vous avez le temps, je vous recommande de lire les deux premières parties de la série en premier. Cela vous aidera à comprendre les réglages au niveau du noyau nécessaires sur toutes les machines de cette configuration.

[**Test de charge de HAProxy (Partie 1)**](https://medium.com/@sachinmalhotra/load-testing-haproxy-part-1-f7d64500b75d)  
[_Test de charge ? HAProxy ? Si tout cela vous semble du grec, ne vous inquiétez pas. Je fournirai des liens en ligne pour lire ce que..._medium.com](https://medium.com/@sachinmalhotra/load-testing-haproxy-part-1-f7d64500b75d)[**Test de charge de HAProxy (Partie 2)**](https://medium.com/@sachinmalhotra/load-testing-haproxy-part-2-4c8677780df6)  
[_Ceci est la deuxième partie de la série en 3 parties sur les tests de performance du célèbre équilibreur de charge TCP et proxy inverse..._medium.com](https://medium.com/@sachinmalhotra/load-testing-haproxy-part-2-4c8677780df6)

Il y a beaucoup de petits composants qui nous ont aidés à rassembler toute la configuration et à atteindre ces chiffres.

Avant de vous donner la configuration finale de HAProxy que nous avons utilisée (si vous êtes super impatient, vous pouvez faire défiler jusqu'en bas), je veux vous y amener en vous expliquant notre raisonnement.

### Ce que nous voulions tester

Le composant que nous voulions tester était HAProxy version 1.6. Nous l'utilisons actuellement en production sur des machines 4 cœurs, 30 Gig. Cependant, toutes les connexions ne sont pas basées sur SSL.

Nous voulions tester deux choses avec cet exercice :

1. L'**augmentation du pourcentage de CPU** lorsque nous passons toute la charge des connexions non-SSL aux connexions SSL. L'utilisation du CPU devrait définitivement augmenter, en raison de la poignée de main 5-voies plus longue et ensuite du chiffrement des paquets.
2. Deuxièmement, nous voulions tester les limites de notre configuration de production actuelle en termes de nombre de requêtes et le nombre maximum de connexions simultanées qui peuvent être supportées avant que les performances ne commencent à se dégrader.

Nous avions besoin de la première partie en raison d'un déploiement majeur de fonctionnalités qui est en plein essor et qui nécessite une communication via SSL. Nous avions besoin de la deuxième partie afin de réduire la quantité de matériel dédié en production aux machines HAProxy.

### Les composants impliqués

* Plusieurs machines clientes pour stresser le HAProxy.
* Une seule machine HAProxy version 1.6 sur diverses configurations  
* 4 cœurs, 30 Gig  
* 16 cœurs, 30 Gig  
* 16 cœurs, 64 Gig
* Des serveurs backend qui aideront à supporter toutes ces connexions simultanées.

### HTTP et MQTT

Si vous avez lu le [premier article](https://medium.com/@sachinmalhotra/load-testing-haproxy-part-1-f7d64500b75d) de cette série, vous devriez savoir que toute notre infrastructure est supportée par deux protocoles :

* HTTP et
* MQTT.

Dans notre stack, nous n'utilisons pas HTTP 2.0 et n'avons donc pas la fonctionnalité de connexions persistantes sur HTTP. Donc en production, le nombre maximum de connexions TCP que nous voyons est d'environ (2 * 150k) sur une seule machine HAProxy (entrant + sortant). Bien que le nombre de connexions simultanées soit plutôt faible, le nombre de requêtes par seconde est assez élevé.

D'autre part, MQTT est une méthode de communication complètement différente. Il offre de grands paramètres de qualité de service et une connectivité persistante. Ainsi, une communication continue bidirectionnelle peut se produire sur un canal MQTT. En ce qui concerne HAProxy qui supporte les connexions MQTT (TCP sous-jacent), nous voyons environ 600-700k connexions TCP au moment de pointe sur une seule machine.

Nous voulions effectuer un test de charge qui nous donnerait des résultats précis pour les connexions basées sur HTTP et MQTT.

Il existe de nombreux outils qui nous aident à tester facilement la charge d'un serveur HTTP et beaucoup de ces outils fournissent des fonctionnalités avancées comme des résultats résumés, la conversion de résultats basés sur du texte en graphiques, etc. Nous n'avons cependant pas trouvé d'outil de test de stress pour MQTT. Nous avons un outil que nous avons développé nous-mêmes, mais il n'était pas assez stable pour supporter ce type de charge dans le délai que nous avions.

Nous avons donc décidé d'opter pour des clients de test de charge pour HTTP et de _simuler la configuration MQTT en utilisant la même chose_ ;) Intéressant, n'est-ce pas ?

Eh bien, continuez à lire.

### La configuration initiale

Ceci va être un long article car je vais fournir beaucoup de détails que je pense seraient vraiment utiles à quelqu'un faisant des tests de charge similaires ou des réglages fins.

* Nous avons pris une machine 16 cœurs 30 Gig pour configurer HAProxy initialement. Nous ne sommes pas allés avec notre configuration de production actuelle car nous pensions que l'impact CPU dû à la terminaison SSL se produisant à l'extrémité HAProxy serait énorme.
* Pour le côté serveur, nous avons opté pour un simple serveur NodeJs qui répond avec `pong` lors de la réception d'une requête `ping`.
* En ce qui concerne le client, nous avons fini par utiliser [Apache Bench](https://httpd.apache.org/docs/2.4/programs/ab.html) initialement. La raison pour laquelle nous avons choisi `ab` est qu'il s'agit d'un outil très connu et stable pour tester la charge des points de terminaison HTTP et aussi parce qu'il fournit de beaux résultats résumés qui nous aideraient beaucoup.

L'outil `ab` fournit de nombreux paramètres intéressants que nous avons utilisés pour notre test de charge comme :

* `-c, concurrency` Spécifie le nombre de requêtes simultanées qui frapperont le serveur.
* `-n, no. of requests` Comme le nom l'indique, spécifie le nombre total de requêtes de l'exécution de charge actuelle.
* `-p POST file` Contient le corps de la requête POST (si c'est ce que vous voulez tester.)

Si vous regardez ces paramètres de près, vous trouverez que de nombreuses permutations sont possibles en ajustant les trois. Une requête ab d'exemple ressemblerait à ceci

```
ab -S -p post_smaller.txt -T application/json -q -n 100000 -c 3000 http://test.haproxy.in:80/ping
```

Un résultat d'exemple d'une telle requête ressemble à ceci

![Image](https://cdn-media-1.freecodecamp.org/images/hPVlgtrAWx4ijbI-qJ-muTK7ghmvrpfoPpa6)

Les chiffres qui nous intéressaient étaient

* Latence à 99%.
* Temps par requête.
* Nombre de requêtes échouées.
* Requêtes par seconde.

Le plus gros problème de `ab` est qu'il ne fournit pas de paramètre pour contrôler le nombre de requêtes par seconde. Nous avons dû ajuster le niveau de concurrence pour obtenir le nombre de requêtes par seconde souhaité et cela a conduit à beaucoup d'essais et d'erreurs.

### Le graphique tout-puissant

Nous ne pouvions pas faire des exécutions de charge multiples de manière aléatoire et continuer à obtenir des résultats car cela ne nous donnerait aucune information significative. Nous devions effectuer ces tests de manière spécifique afin d'obtenir des résultats significatifs. Nous avons donc suivi ce graphique

![Image](https://cdn-media-1.freecodecamp.org/images/LiK2goW97V5iflC0WEPve7QwrqdemhRsIM2x)

Ce graphique indique que jusqu'à un certain point, si nous continuons à augmenter le nombre de requêtes, la latence restera presque la même. Cependant, **au-delà d'un certain point de bascule**, la latence commencera à augmenter de manière exponentielle. C'est ce point de bascule pour une machine ou pour une configuration que nous avions l'intention de mesurer.

### Ganglia

Avant de fournir certains résultats de test, je voudrais mentionner [Ganglia](http://ganglia.sourceforge.net/).

> Ganglia est un système de surveillance distribué et évolutif pour les systèmes informatiques haute performance tels que les clusters et les grilles.

Regardez la capture d'écran suivante de l'une de nos machines pour vous faire une idée de ce qu'est Ganglia et du type d'informations qu'il fournit sur la machine sous-jacente.

![Image](https://cdn-media-1.freecodecamp.org/images/BCszUw2oQQ3vuST7Uz9C1LIyyTwcTYzsmOjD)

![Image](https://cdn-media-1.freecodecamp.org/images/R8fOPbW-MbQzx4XDNMHNXPJ32E9Gj7oD1JP2)

Plutôt intéressant, hein ?

En continuant, nous avons constamment surveillé Ganglia pour notre machine HAProxy afin de surveiller certaines choses importantes.

1. `TCP established` Cela nous indique le nombre total de connexions TCP établies sur le système. NOTE : ceci est la somme des connexions entrantes ainsi que sortantes.
2. `packets sent and received` Nous voulions voir le nombre total de paquets TCP envoyés et reçus par notre machine HAProxy.
3. `bytes sent and received` Cela nous montre les données totales que nous avons envoyées et reçues par la machine.
4. `memory` La quantité de RAM utilisée au fil du temps.
5. `network` La consommation de bande passante réseau en raison des paquets envoyés sur le fil.

Voici les limites connues trouvées via des tests/nombres précédents que nous voulions atteindre via notre test de charge.

> 700k connexions TCP établies,  
> 50k paquets envoyés, 60k paquets reçus,   
> 10-15MB octets envoyés ainsi que reçus,   
> 14-15Gig mémoire au pic,   
> 7MB réseau.   
> `TOUTES ces valeurs sont sur une base par seconde`

### HAProxy Nbproc

Initialement, lorsque nous avons commencé à tester la charge de HAProxy, nous avons découvert qu'avec SSL, le CPU était sollicité assez tôt dans le processus, mais le nombre de requêtes par seconde était très faible. En investiguant la commande [top](http://www.tecmint.com/12-top-command-examples-in-linux/), nous avons découvert que HAProxy n'utilisait qu'un seul cœur. Alors que nous avions 15 autres cœurs disponibles.

En cherchant sur Google pendant environ 10 minutes, nous avons trouvé ce paramètre intéressant dans HAProxy qui permet à HAProxy d'utiliser plusieurs cœurs.

Il s'appelle `nbproc` et pour mieux comprendre ce que c'est et comment le configurer, consultez cet article :

[http://blog.onefellow.com/post/82478335338/haproxy-mapping-process-to-cpu-core-for-maximum](http://blog.onefellow.com/post/82478335338/haproxy-mapping-process-to-cpu-core-for-maximum)

Le réglage de ce paramètre a été la base de notre stratégie de test de charge à l'avenir. Parce que la capacité à utiliser plusieurs cœurs par HAProxy nous a donné le pouvoir de former plusieurs combinaisons pour notre suite de tests de charge.

### Test de charge avec AB

Lorsque nous avons commencé notre parcours de test de charge, nous n'étions pas clairs sur les choses que nous devions mesurer et ce que nous devions atteindre.

Initialement, nous avions un seul objectif en tête et c'était de trouver le point de bascule uniquement par la variation de tous les paramètres mentionnés ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/RhvOSn7WBNamEEDyuygrD20tEJw8eveUN97m)

J'ai maintenu un tableau de tous les résultats pour les divers tests de charge que nous avons effectués. Au total, j'ai effectué plus de 500 exécutions de test pour obtenir le résultat ultime. Comme vous pouvez clairement le voir, il y a beaucoup de pièces mobiles pour chaque test.

#### Problèmes avec un seul client

Nous avons commencé à voir que le client devenait un goulot d'étranglement à mesure que nous augmentions nos requêtes par seconde. Apache bench utilise un seul cœur et il est évident dans la documentation qu'il ne fournit aucune fonctionnalité pour utiliser plusieurs cœurs.

Pour exécuter plusieurs clients efficacement, nous avons trouvé un utilitaire Linux intéressant appelé [Parallel](http://www.shakthimaan.com/posts/2014/11/27/gnu-parallel/news.html). Comme son nom l'indique, il vous aide à exécuter plusieurs commandes en parallèle et utilise plusieurs cœurs. Exactement ce que nous voulions.

Jetez un coup d'œil à une commande d'exemple qui exécute plusieurs clients en utilisant parallel.

```
cat hosts.txt |  parallel  'ab  -S -p post_smaller.txt -T application/json -n 100000 -c 3000 {}'
```

```
sachinm@ip-192-168-0-124:~$ cat hosts.txthttp://test.haproxy.in:80/pinghttp://test.haproxy.in:80/pinghttp://test.haproxy.in:80/ping
```

La commande ci-dessus exécuterait 3 clients ab frappant la même URL. Cela nous a aidés à supprimer le goulot d'étranglement côté client.

#### Le paramètre Sleep et Times

Nous avons parlé de certains paramètres dans ganglia que nous voulions suivre. Discutons-en un par un.

1. `packets sent and received` Cela peut être simulé en envoyant certaines données dans le cadre de la requête post. Cela nous aiderait également à générer certaines `parties réseau ainsi que les octets envoyés et reçus dans ganglia`
2. `tcp_established` C'est quelque chose qui nous a pris beaucoup, beaucoup de temps à simuler dans notre scénario. Imaginez si une seule requête ping prend environ une seconde, cela nous prendrait environ 700k requêtes par seconde pour atteindre notre jalon tcp_established.   
Maintenant, ce nombre peut sembler plus facile à atteindre en production, mais il était impossible de le générer dans notre scénario.

Que avons-nous fait, vous pourriez demander ? Nous avons introduit un paramètre de sommeil dans notre appel POST qui spécifie le nombre de millisecondes dont le serveur a besoin pour dormir avant d'envoyer une réponse. Cela simulerait une requête longue en production. Donc maintenant, disons que nous avons un sommeil d'environ 20 minutes (Oui), cela nous prendrait environ 583 requêtes par seconde pour atteindre la marque de 700k.

En outre, nous avons également introduit un autre paramètre dans nos appels POST au HAProxy et c'était le paramètre `times`. Cela spécifiait le nombre de fois que le serveur devait écrire une réponse sur la connexion tcp avant de la terminer. Cela nous a aidés à simuler encore plus de données transférées sur le fil.

#### Problèmes avec apache bench

Bien que nous ayons trouvé beaucoup de résultats avec apache bench, nous avons également rencontré beaucoup de problèmes en cours de route. Je ne mentionnerai pas tous ici car ils ne sont pas importants pour cet article car je vais bientôt introduire un autre client.

Nous étions assez contents des chiffres que nous obtenions d'apache bench, mais à un moment donné, générer les connexions tcp requises est simplement devenu impossible. D'une manière ou d'une autre, apache bench ne gérait pas correctement le paramètre de sommeil que nous avions introduit et ne montait pas en charge pour nous.

Bien que l'exécution de plusieurs clients ab sur une seule machine ait été résolue en utilisant l'utilitaire parallel. L'exécution de cette configuration sur plusieurs machines clientes était encore un casse-tête pour nous. Je n'avais pas entendu parler de l'utilitaire [pdsh](https://github.com/grondo/pdsh) à l'époque et j'étais pratiquement bloqué.

De plus, nous ne nous concentrions pas non plus sur les délais d'attente. Il existe un ensemble de délais d'attente par défaut sur le HAProxy, le client ab et le serveur, et nous les avions complètement ignorés. Nous avons découvert beaucoup de choses en cours de route et nous nous sommes beaucoup organisés sur la manière de procéder aux tests.

Nous parlions du graphique du point de bascule, mais nous nous en sommes beaucoup écartés au fil du temps. Cependant, des résultats significatifs ne pouvaient être trouvés qu'en se concentrant sur celui-ci.

Avec apache bench, un point est venu où le nombre de connexions TCP n'augmentait pas. Nous avions environ 40-45 clients en cours d'exécution sur 5-6 boîtiers clients différents, mais nous n'avons pas pu atteindre l'échelle que nous voulions. Théoriquement, le nombre de connexions TCP aurait dû augmenter à mesure que nous augmentions le temps de sommeil, mais cela ne fonctionnait pas pour nous.

### Entrée de Vegeta

![Image](https://cdn-media-1.freecodecamp.org/images/qZCSNF6bzXWzhrNqqhwiJaICpfwIw0NYiyRw)

Je cherchais d'autres outils de test de charge qui pourraient être plus évolutifs et offrir de meilleures fonctionnalités par rapport à apache bench lorsque je suis tombé sur V[egeta](https://github.com/tsenart/vegeta).

D'après mon expérience personnelle, j'ai trouvé Vegeta extrêmement évolutif et offrant de bien meilleures fonctionnalités par rapport à apache bench. Un seul client Vegeta était capable de produire un niveau de débit équivalent à 15 clients apache bench dans notre test de charge.

Par la suite, je vais fournir des résultats de tests de charge qui ont été testés en utilisant Vegeta lui-même.

### Test de charge avec Vegeta

Tout d'abord, jetez un coup d'œil à la commande que nous avons utilisée pour exécuter un seul client Vegeta. Intéressamment, la commande pour mettre la charge sur les serveurs backend s'appelle `attack` :p

```
echo "POST https://test.haproxy.in:443/ping" | vegeta -cpus=32 attack -duration=10m  -header="sleep:30000"  -body=post_smaller.txt -rate=2000 -workers=500  | tee reports.bin | vegeta report
```

J'adore simplement les paramètres fournis par Vegeta. Jetons un coup d'œil à certains d'entre eux ci-dessous.

1. `-cpus=32` Spécifie le nombre de cœurs à utiliser par ce client. Nous avons dû étendre nos machines clientes à 32 cœurs, 64 Gig en raison de la quantité de charge à générer. Si vous regardez de près ci-dessus, le taux n'est pas très élevé. Mais il devient difficile de maintenir une telle charge lorsque beaucoup de connexions sont en état de sommeil du côté serveur.
2. `-duration=10m` Je pense que cela est auto-explicatif. Si vous ne spécifiez aucune durée, le test s'exécutera indéfiniment.
3. `-rate=2000` Le nombre de requêtes par seconde.

![Image](https://cdn-media-1.freecodecamp.org/images/Q45eRIwGOXEfrQPggj3YujCVqkZwUgxO260s)

Comme vous pouvez le voir ci-dessus, nous avons atteint un impressionnant 32k requêtes par seconde sur une simple machine à 4 cœurs. Si vous vous souvenez du graphique du point de bascule, vous pourrez le remarquer clairement ci-dessus. Donc le point de bascule dans ce cas est de 31,5k requêtes non SSL.

Jetez un coup d'œil à quelques résultats supplémentaires du test de charge.

![Image](https://cdn-media-1.freecodecamp.org/images/j7REmvLdaRuhInIGjaDPKJC7-XbY1VQavU2j)

16k connexions SSL n'est pas non plus mauvais du tout. Veuillez noter qu'à ce stade de notre parcours de test de charge, nous avons dû repartir de zéro car nous avions adopté un nouveau client et il nous donnait des résultats bien meilleurs que ab. Nous avons donc dû refaire beaucoup de choses.

![Image](https://cdn-media-1.freecodecamp.org/images/DRIv7z6EocjovdXs7VnGwfUzikUoJIccFXzt)

Une augmentation du nombre de cœurs a conduit à une augmentation du nombre de requêtes par seconde que la machine peut prendre avant que la limite du CPU ne soit atteinte.

Nous avons constaté qu'il n'y avait pas d'augmentation substantielle du nombre de requêtes par seconde si nous augmentions le nombre de cœurs de 8 à 16. De plus, si nous décidions finalement d'opter pour une machine à 8 cœurs en production, nous n'allouerions jamais tous les cœurs à HAProxy ou à tout autre processus d'ailleurs. Nous avons donc décidé d'effectuer quelques tests avec 6 cœurs également pour voir si nous avions des chiffres acceptables.

![Image](https://cdn-media-1.freecodecamp.org/images/eYqRd5vMvnbxtyfa9yAellmugp3gH10IG2aO)

Pas mal.

### Introduction du sleep

Nous étions assez satisfaits de nos résultats de test de charge jusqu'à présent. Cependant, cela ne simulait pas le scénario de production réel. Cela s'est produit lorsque nous avons introduit un temps de sommeil qui était absent jusqu'à présent dans nos tests.

```
echo "POST https://test.haproxy.in:443/ping" | vegeta -cpus=32 attack -duration=10m  -header="sleep:1000"  -body=post_smaller.txt-rate=2000 -workers=500  | tee reports.bin | vegeta report
```

Ainsi, un temps de sommeil de 1000 millisecondes entraînerait un sommeil du serveur pendant une durée `x` où `0 < x <` 1000 et est sélectionné aléatoirement. Donc en moyenne, le test de charge ci-dessus donnera une latence de ≥ 500 ms

![Image](https://cdn-media-1.freecodecamp.org/images/r6muveSxdnfXFhOEbAiPupySz6jQXJodpIOR)

Les chiffres dans la dernière cellule représentent

```
TCP established, Packets Rec, Packets Sent
```

respectivement. Comme vous pouvez clairement le voir, le nombre maximum de requêtes par seconde que la machine à 6 cœurs peut supporter a diminué à 8k contre 20k. Clairement, le sommeil a son impact et cet impact est l'augmentation du nombre de connexions TCP établies. Cependant, cela est loin de la marque de 700k que nous nous étions fixée.

### Jalon #1

Comment augmenter le nombre de connexions TCP ? Simple, nous continuons à augmenter le temps de sommeil et elles devraient augmenter. Nous avons continué à jouer avec le temps de sommeil et nous nous sommes arrêtés à un temps de sommeil de 60 secondes. Cela signifierait une latence moyenne d'environ 30 secondes.

Il y a un paramètre de résultat intéressant que Vegeta fournit et c'est le % de requêtes réussies. Nous avons vu qu'avec le temps de sommeil ci-dessus, seulement 50 % des appels réussissaient. Voir les résultats ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/cZY8PiFT2rdCS8kk8eLAc5eh3M3u-qelUKDS)

Nous avons atteint un impressionnant 400k connexions TCP établies avec 8k requêtes par seconde et un temps de sommeil de 60000 ms. Le R dans 60000R signifie Aléatoire.

La première vraie découverte que nous avons faite est qu'il y a un délai d'attente d'appel par défaut dans Vegeta qui est de 30 secondes et cela expliquait pourquoi 50 % de nos appels échouaient. Nous l'avons donc augmenté à environ 70s pour nos tests ultérieurs et nous l'avons fait varier selon les besoins.

![Image](https://cdn-media-1.freecodecamp.org/images/m0nSGiyH9osxPpcLItnvZnxDIqOH9k8fkhTL)

Nous avons facilement atteint la marque de 700k après avoir ajusté la valeur de délai d'attente du côté client. Le seul problème avec cela était que ceux-ci n'étaient pas constants. Ce n'étaient que des pics. Donc le système a atteint un pic de 600k ou 700k mais n'est pas resté là très longtemps.

Nous voulions cependant quelque chose de similaire à ceci

![Image](https://cdn-media-1.freecodecamp.org/images/JtHNZhFzCNMSUa2ceA3CTd4AlrP77kHvLAoo)

Cela montre un état stable où 780k connexions sont maintenues. Si vous regardez de près les statistiques ci-dessus, le nombre de requêtes par seconde est très élevé. En production, cependant, nous avons beaucoup moins de requêtes (quelque part autour de 300) sur une seule machine HAProxy.

Nous étions sûrs que si nous réduisions drastiquement le nombre de HAProxies que nous avons en production (quelque part autour de 30, ce qui signifie 30*300 ~ 9k connexions par seconde), nous atteindrions d'abord les limites de la machine en termes de nombre de connexions TCP et non du CPU.

> Nous avons donc décidé d'atteindre 900 requêtes par seconde et 30MB/s de réseau et 2,1 millions de connexions TCP établies. Nous avons convenu de ces chiffres car ils seraient 3 fois notre charge de production sur un seul HAProxy.

De plus, jusqu'à présent, nous avions opté pour 6 cœurs utilisés par HAProxy. Nous voulions tester seulement 3 cœurs car ce serait le plus facile pour nous à déployer sur nos machines de production (Nos machines de production, comme mentionné précédemment, sont 4 cœurs 30 Gig. Donc pour déployer des changements avec `nbproc = 3` serait le plus facile pour nous.

```
SOUVENEZ-VOUS, la machine que nous avions à ce moment-là était une machine 16 cœurs 30 Gig avec 3 cœurs alloués à HAProxy.
```

### Jalon #2

Maintenant que nous avions des limites maximales sur les requêtes par seconde que différentes variations de configuration machine pouvaient supporter, nous n'avions qu'une seule tâche restante comme mentionné ci-dessus.

Atteindre 3X la charge de production qui est

* 900 requêtes par seconde
* 2,1 millions de connexions TCP établies et
* 30 MB/s de réseau.

Nous avons encore été bloqués car les connexions TCP établies subissaient un coup dur à 220k. Peu importe le nombre de machines clientes ou le temps de sommeil, le nombre de connexions TCP semblait être bloqué là.

Regardons quelques calculs. 220k connexions TCP établies et 900 requêtes par seconde = 110,000 / 900 ~= 120 secondes. J'ai pris 110k car 220k connexions incluent à la fois les entrées et les sorties. Donc c'est à double sens.

Notre doute sur le fait que 2 minutes soient une limite quelque part dans le système a été vérifié lorsque nous avons introduit des logs côté HAProxy. Nous avons pu voir 120000 ms comme temps total pour beaucoup de connexions dans les logs.

```
Mar 23 13:24:24 localhost haproxy[53750]: 172.168.0.232:48380 [23/Mar/2017:13:22:22.686] api~ api-backend/http31 39/0/2062/-1/122101 -1 0 - - SD-- 1714/1714/1678/35/0 0/0 {0,"",""} "POST /ping HTTP/1.1"
```

```
122101 est la valeur de délai d'attente. Voir la documentation HAProxy sur les significations de toutes ces valeurs. 
```

En enquêtant davantage, nous avons découvert que NodeJs a un délai d'attente de requête par défaut de 2 minutes. Voila !

![Image](https://cdn-media-1.freecodecamp.org/images/t9XlfcYeEOKUkPGMqvrtO8bwgNaT1xGPeNdq)

[**comment modifier le délai d'attente par défaut des requêtes nodejs ?**](http://stackoverflow.com/questions/23925284/how-to-modify-the-nodejs-request-default-timeout-time)  
[_J'utilisais nodejs request, le délai d'attente par défaut de nodejs http est de 120000 ms, mais ce n'est pas assez pour moi, alors que mon..._stackoverflow.com](http://stackoverflow.com/questions/23925284/how-to-modify-the-nodejs-request-default-timeout-time)[**HTTP | Documentation Node.js v7.8.0**](https://nodejs.org/api/http.html#http_server_settimeout_msecs_callback)  
[_Les interfaces HTTP dans Node.js sont conçues pour supporter de nombreuses fonctionnalités du protocole qui ont été traditionnellement..._nodejs.org](https://nodejs.org/api/http.html#http_server_settimeout_msecs_callback)

Mais notre bonheur était apparemment de courte durée. À 1,3 million, les connexions HAProxy ont soudainement chuté à 0 et ont commencé à augmenter à nouveau. Nous avons rapidement vérifié la commande [dmesg](http://www.linfo.org/dmesg.html) qui nous a fourni des informations utiles au niveau du noyau pour notre processus HAProxy.

En gros, le processus HAProxy était à court de mémoire. Nous avons donc décidé d'augmenter la RAM de la machine et nous sommes passés à une machine 16 cœurs 64 Gig avec `nbproc = 3` et grâce à ce changement, nous avons pu atteindre 2,4 millions de connexions.

### Code Backend

Voici le code du serveur backend qui était utilisé. Nous avions également utilisé statsd dans le code du serveur pour obtenir des données consolidées sur les requêtes par seconde qui étaient reçues par le client.

```
var http = require('http');var createStatsd = require('uber-statsd-client');qs = require('querystring');
```

```
var sdc = createStatsd({host: '172.168.0.134',port: 8125});
```

```
var argv = process.argv;var port = argv[2];
```

```
function randomIntInc (low, high){    return Math.floor(Math.random() * (high - low + 1) + low);}
```

```
function sendResponse(res,times, old_sleep){    res.write('pong');    if(times==0)    {        res.end();    }    else    {         sleep = randomIntInc(0, old_sleep+1);        setTimeout(sendResponse, sleep, res,times-1, old_sleep);    }}
```

```
var server = http.createServer(function(req, res){   headers = req.headers;   old_sleep = parseInt(headers["sleep"]);   times = headers["times"] || 0;   sleep = randomIntInc(0, old_sleep+1);   console.log(sleep);   sdc.increment("ssl.server.http");   res.writeHead(200);   setTimeout(sendResponse, sleep, res, times, old_sleep)
```

```
});
```

```
server.timeout = 3600000;server.listen(port);
```

Nous avions également un petit script pour exécuter plusieurs serveurs backend. Nous avions 8 machines avec 10 serveurs backend CHACUN (oui !). Nous avons littéralement pris l'idée des clients et des serveurs backend étant infinis pour le test de charge, au sérieux.

```
counter=0while [ $counter -le 9 ]do   port=$((8282+$counter))   nodejs /opt/local/share/test-tools/HikeCLI/nodeclient/httpserver.js $port &   echo "Server created on port "  $port
```

```
   ((counter++))done
```

```
echo "Created all servers"
```

### Code Client

En ce qui concerne le client, il y avait une limitation de 63k connexions TCP par IP. Si vous n'êtes pas sûr de ce concept, veuillez vous référer à mon [article précédent](https://medium.com/@sachinmalhotra/load-testing-haproxy-part-2-4c8677780df6) dans cette série.

Ainsi, pour atteindre 2,4 millions de connexions (deux côtés, ce qui représente 1,2 million depuis les machines clientes), nous avions besoin d'environ 20 machines. C'est vraiment un casse-tête d'exécuter la commande Vegeta sur les 20 machines une par une, et même si vous trouviez un moyen de le faire en utilisant quelque chose comme [csshx](https://github.com/brockgr/csshx), vous auriez toujours besoin de quelque chose pour combiner tous les résultats de tous les clients Vegeta.

Consultez le script ci-dessous.

```
result_file=$1
```

```
declare -a machines=("172.168.0.138" "172.168.0.141" "172.168.0.142" "172.168.0.18" "172.168.0.5" "172.168.0.122" "172.168.0.123" "172.168.0.124" "172.168.0.232" " 172.168.0.244" "172.168.0.170" "172.168.0.179" "172.168.0.59" "172.168.0.68" "172.168.0.137" "172.168.0.155" "172.168.0.154" "172.168.0.45" "172.168.0.136" "172.168.0.143")
```

```
bins=""commas=""
```

```
for i in "${machines[@]}"; do bins=$bins","$i".bin"; commas=$commas","$i;  done;
```

```
bins=${bins:1}commas=${commas:1}
```

```
pdsh -b -w "$commas" 'echo "POST http://test.haproxy.in:80/ping" | /home/sachinm/.linuxbrew/bin/vegeta -cpus=32 attack -connections=1000000 -header="sleep:20" -header="times:2" -body=post_smaller.txt -timeout=2h -rate=3000 -workers=500 > ' $result_file
```

```
for i in "${machines[@]}"; do  scp sachinm@$i:/home/sachinm/$result_file $i.bin ; done;
```

```
vegeta report -inputs="$bins"
```

Apparemment, Vegeta fournit des informations sur cet utilitaire appelé [pdsh](https://github.com/grondo/pdsh) qui vous permet d'exécuter une commande simultanément sur plusieurs machines à distance. De plus, Vegeta nous permet de combiner plusieurs résultats en un seul et c'est vraiment tout ce que nous voulions.

### Configuration HAProxy

C'est probablement ce que vous êtes venu chercher ici, voici la configuration HAProxy que nous avons utilisée dans nos exécutions de tests de charge. La partie la plus importante étant celle du paramètre `nbproc` et du paramètre `maxconn`. Le paramètre maxconn nous permet de fournir le nombre maximum de connexions TCP que HAProxy peut supporter globalement (dans un sens).

Les modifications du paramètre `maxconn` entraînent une augmentation de la limite ulimit du processus HAProxy. Jetez un coup d'œil ci-dessous

![Image](https://cdn-media-1.freecodecamp.org/images/ipKWHF1l3tJCCvBuhmNEz7DRn3mvkZUddwZm)

Le nombre maximal de fichiers ouverts a augmenté à 4 millions en raison du nombre maximal de connexions pour HAProxy étant fixé à 2 millions. Propre !

Consultez l'article ci-dessous pour une multitude d'optimisations HAProxy que vous pouvez et devriez faire pour atteindre le type de statistiques que nous avons atteint.

[**Utilisez HAProxy pour équilibrer la charge de 300k connexions de socket TCP simultanées : Épuisement des ports, Keep-alive et...**](https://www.linangran.com/?p=547)  
[_J'essaie de construire un système de push récemment. Pour augmenter l'évolutivité du système, la meilleure pratique est de faire..._www.linangran.com](https://www.linangran.com/?p=547)

![Image](https://cdn-media-1.freecodecamp.org/images/dhrvfLzkHVAlYEjh1o9cRFzrTVf-8Or8YKc3)

![Image](https://cdn-media-1.freecodecamp.org/images/qX-H46KPV2XTfStQPTjU5jEffGyoi7Y6dFB8)

Le http30 passe à http83 :p

C'est tout pour l'instant, les gens. Si vous l'avez lu jusqu'ici, je suis vraiment impressionné :)

Un remerciement spécial à [Dheeraj Kumar Sidana](https://www.freecodecamp.org/news/how-we-fine-tuned-haproxy-to-achieve-2-000-000-concurrent-ssl-connections-d017e61a4d27/undefined) qui nous a aidés tout au long de ce processus et sans l'aide duquel nous n'aurions pas pu obtenir de résultats significatifs. :)

Faites-moi savoir comment ce billet de blog vous a aidé. De plus, veuillez recommander (❤) et partager l'amour autant que possible pour ce billet si vous pensez que cela pourrait être utile pour quelqu'un.