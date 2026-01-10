---
title: 'Comment obtenir de meilleures performances : le cas des timeouts'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-05T13:06:01.000Z'
originalURL: https://freecodecamp.org/news/better-performance-the-case-for-timeouts-3234d6aceeaf
coverImage: https://cdn-media-1.freecodecamp.org/images/1*A6SFwHAQlwml4ff8HOA2jQ.jpeg
tags:
- name: Microservices
  slug: microservices
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: 'Comment obtenir de meilleures performances : le cas des timeouts'
seo_desc: 'By Alex Nadalin

  Most of the larger-scale services that we design nowadays depend, more or less,
  on external APIs. You’ve heard it multiple times: as soon as your codebase starts
  to look like a monolith, it’s time to start splitting it into smaller se...'
---

Par Alex Nadalin

La plupart des services à grande échelle que nous concevons de nos jours dépendent, plus ou moins, d'API externes. Vous l'avez entendu à plusieurs reprises : dès que votre base de code commence à ressembler à un monolithe, il est temps de commencer à la diviser en [services plus petits](https://en.wikipedia.org/wiki/Microservices) qui peuvent évoluer indépendamment et ne sont pas fortement couplés avec le monolithe.

Même si vous n'utilisez pas vraiment de microservices, il est probable que vous dépendiez déjà de services externes, tels que [elasticsearch](https://en.wikipedia.org/wiki/Elasticsearch), [Redis](https://redis.io/), ou une passerelle de paiement, et que vous deviez vous intégrer avec eux via une sorte d'API.

Que se passe-t-il lorsque ces services sont lents ou indisponibles ? Eh bien, vous ne pouvez pas traiter les requêtes de recherche ou les paiements, mais votre application fonctionnerait toujours "bien" — n'est-ce pas ?

**Ce n'est pas toujours le cas**, et je souhaite exécuter quelques benchmarks pour vous montrer comment un petit ajustement, les [timeouts](https://en.wikipedia.org/wiki/Timeout_(computing)), peut s'avérer bénéfique lors de la gestion de services externes.

### Notre cas

Nous avons lancé une nouvelle startup _Hello World!_ qui, étrangement, gagne de l'argent en déployant un service inutile qui imprime une chaîne récupérée depuis un autre service. C'est une simplification excessive d'un scénario réel, mais cela servira bien notre propos.

![Image](https://cdn-media-1.freecodecamp.org/images/0*WvZHW7KYooyqCCRC.png)

Nos clients se connecteront à notre frontend principal, `server1.js`, qui effectuera ensuite une requête HTTP vers un autre service, `server2.js`, qui répondra. Une fois que nous avons une réponse de `server2.js`, nous pouvons alors retourner le corps de la réponse à notre client.

Quelques points à noter :

* Les serveurs fonctionnent sur le port `3000` (application principale) et `3001` (serveur "backend"). Ainsi, une fois que le client fait une requête à `localhost:3000`, une nouvelle requête HTTP sera envoyée à `localhost:3001`.
* Le service backend attendra 100 ms (ceci est pour simuler des cas d'utilisation réels) avant de retourner une réponse.
* J'utilise le client HTTP [unirest](https://github.com/Mashape/unirest-nodejs). Je l'aime beaucoup et, même si nous aurions pu simplement utiliser le module intégré `http`, je suis convaincu que cela nous donnera une meilleure sensation en termes d'applications réelles.
* Unirest est assez sympa pour nous dire s'il y a eu une erreur dans notre requête, donc nous pouvons simplement vérifier `response.error` et gérer le drame à partir de là.
* Je vais utiliser [docker](https://www.docker.com/) pour exécuter ces tests, et le code est [disponible sur GitHub](https://github.com/odino/the-case-for-timeouts).

### Exécutons nos premiers tests

Lançons nos serveurs et commençons à bombarder `server1.js` avec des requêtes. Nous allons utiliser [siege](https://www.joedog.org/siege-home/) (je suis trop hipster pour [AB](https://httpd.apache.org/docs/2.4/programs/ab.html)), qui fournit des informations utiles lors de l'exécution du test de charge :

```
siege -c 5 www.google.com** SIEGE 3.0.5** Préparation de 5 utilisateurs simultanés pour la bataille.Le serveur est maintenant sous siège...^CLever le siège du serveur...      terminé.
```

```
Transactions :                26 hitsDisponibilité :            100.00 %Temps écoulé :              6.78 secsDonnées transférées :          0.20 MBTemps de réponse :             0.52 secsTaux de transaction :          3.83 trans/secDébit :                0.03 MB/secConcurence :               2.01Transactions réussies :          27Transactions échouées :              0Transaction la plus longue :           1.28Transaction la plus courte :          0.36
```

L'option `-c` dans siege définit combien de requêtes simultanées nous devons envoyer au serveur, et vous pouvez même spécifier combien de répétitions (`-r`) vous souhaitez exécuter. Par exemple, `-c 10 -r 5` signifierait que nous envoyons au serveur 50 requêtes au total, par lots de 10 requêtes simultanées. Pour les besoins de notre benchmark, j'ai décidé, cependant, de garder les tests en cours pendant trois minutes et d'analyser les résultats par la suite, sans définir un nombre maximum de répétitions.

De plus, dans les exemples suivants, je vais réduire les résultats aux éléments les plus importants fournis par siege :

* Disponibilité : combien de nos requêtes le serveur a-t-il pu gérer
* Taux de transaction : combien de requêtes par seconde avons-nous pu faire ?
* Transactions réussies/échouées : combien de requêtes se sont terminées avec des codes de statut réussis/échoués (c'est-à-dire 2xx vs 5xx) ?

Commençons par envoyer 500 requêtes simultanées pour observer comment les services se comportent.

```
docker run --net host -v $(pwd):/src -d mhart/alpine-node:7.1 node /src/server1.jsdocker run --net host -v $(pwd):/src -d mhart/alpine-node:7.1 node /src/server2.js
```

```
siege -c 500 127.0.0.1:3000
```

Après environ trois minutes, il est temps d'arrêter le siège (`ctrl+c`) et de voir à quoi ressemblent les résultats :

```
Disponibilité :             100.00 %Taux de transaction :       1156.89 trans/secTransactions réussies :      205382Transactions échouées :              0
```

Pas mal, car nous avons pu servir 1156 transactions par seconde. Encore mieux, il semble que nous n'avons aucune erreur, ce qui signifie que notre taux de réussite est de 100 %. Que se passe-t-il si nous augmentons notre jeu et passons à 1k transactions simultanées ?

```
siege -c 1000 127.0.0.1:3000...
```

```
Disponibilité :            100.00 %Taux de transaction :       1283.61 trans/secTransactions réussies :      232141Transactions échouées :              0
```

Bien joué ! Nous avons légèrement augmenté le débit, car notre application est maintenant capable de gérer 1283 requêtes par seconde. Puisque les applications font très peu (imprimer une chaîne et c'est tout), il est probable que plus nous enverrons de requêtes simultanées, plus le débit sera élevé.

Ces chiffres peuvent sembler inutiles maintenant (nous ne les comparons à rien), mais ils s'avéreront essentiels dans les paragraphes suivants.

### Introduction à l'échec

Ce n'est pas ainsi que se comportent les services web du monde réel : vous devez **accepter les échecs** et construire des applications résilientes capables de les surmonter.

Par exemple, supposons que notre service backend traverse une phase difficile et commence à ralentir de temps en temps :

Dans cet exemple, 1 requête sur 10 sera servie après qu'un timeout de 10s se soit écoulé, tandis que les autres seront traitées avec le délai "standard" de 100ms. Cela simule un scénario où nous avons plusieurs serveurs derrière un équilibreur de charge, et l'un d'eux commence à envoyer des erreurs aléatoires ou devient plus lent en raison d'une charge excessive.

Retournons à notre benchmark et voyons comment `server1.js` se comporte maintenant que sa dépendance commence à ralentir :

```
siege -c 1000 127.0.0.1:3000
```

```
Disponibilité :            100.00 %Taux de transaction :        853.93 trans/secTransactions réussies :      154374Transactions échouées :              0
```

**Quelle déception** : notre taux de transaction a chuté, baissant de plus de 30 %, simplement parce que certaines des réponses sont en retard. Cela signifie que `server1.js` doit attendre plus longtemps pour recevoir des réponses de `server2.js`, utilisant ainsi plus de ressources et étant capable de servir moins de requêtes qu'il ne le pourrait théoriquement.

### Une erreur maintenant est meilleure qu'une réponse demain

Le cas des timeouts commence par reconnaître un fait simple : **les utilisateurs n'attendront pas les réponses lentes**.

Après 1 ou 2 secondes, leur attention s'évanouira et les chances qu'ils soient encore accrochés à votre contenu disparaîtront dès que vous franchirez le seuil de 4/5s. Cela signifie qu'**il est généralement préférable de leur donner un retour immédiat, même négatif** ("Une erreur s'est produite, veuillez réessayer"), plutôt que de les laisser frustrés par la lenteur de votre service.

Dans l'esprit du "[fail fast](https://en.wikipedia.org/wiki/Fail-fast)", nous avons décidé d'ajouter un timeout afin de nous assurer que nos réponses respectent un certain SLA. Dans ce cas, nous avons décidé que notre SLA est de 3s, ce qui est le temps que nos utilisateurs attendront éventuellement pour utiliser notre service.

```
...
```

```
require('unirest').get('http://localhost:3001').timeout(3000).end(function(r) {
```

```
...
```

Voyons à quoi ressemblent les chiffres avec les timeouts activés :

```
Disponibilité :              90.14 %Taux de transaction :       1125.26 trans/secTransactions réussies :      209861Transactions échouées :          22964
```

Oh là là, nous sommes de retour dans le jeu. Le taux de transaction est à nouveau supérieur à 1k par seconde, et nous pouvons presque servir autant de requêtes que nous le ferions dans des conditions idéales (lorsqu'il n'y a pas de lag dans le service backend).

Bien sûr, l'un des inconvénients est que nous avons maintenant augmenté le nombre d'échecs (10 % des requêtes totales), ce qui signifie que certains utilisateurs verront une page d'erreur. Cela reste cependant préférable à les servir après 10s, car la plupart d'entre eux auraient abandonné notre service de toute façon.

Nous avons maintenant vu que, idéalement, **les timeouts aident à préserver un rps quasi idéal** (requêtes par seconde), mais qu'en est-il de la consommation de ressources ? Seront-ils meilleurs pour s'assurer que nos serveurs n'auront pas besoin de ressources supplémentaires si l'une de leurs dépendances devient moins réactive ?

Creusons cela.

### Le facteur RAM

Pour déterminer combien de mémoire notre `server1.js` consomme, nous devons mesurer, à intervalles réguliers, la quantité de mémoire utilisée par le serveur. En production, nous utiliserions des outils tels que [NewRelic](https://newrelic.com/) ou [KeyMetrics](https://keymetrics.io/), mais pour nos scripts simples, nous utiliserons la version pauvre de ces outils. Nous allons imprimer la quantité de mémoire de `server1.js` et nous utiliserons un autre script pour enregistrer la sortie et imprimer quelques statistiques simples.

Assurons-nous que `server1.js` imprime la quantité de mémoire utilisée toutes les 100ms :

```
...
```

```
setInterval(_ => {  console.log(process.memoryUsage().heapUsed / 1000000)}, 100)
```

```
...
```

Si nous démarrons le serveur, nous devrions voir quelque chose comme :

```
3.9901764.0667524.0760244.0777844.0795444.0813044.0830644.084824
```

qui est la quantité de mémoire, en MB, que le serveur utilise. Pour traiter les chiffres, j'ai écrit un script simple qui lit l'entrée depuis `stdin` et calcule les statistiques :

Le module est [public](https://github.com/odino/node-number-aggregator-stats) et [disponible sur NPM](https://www.npmjs.com/package/number-aggregator-stats), donc nous pouvons simplement l'installer globalement et rediriger la sortie du serveur vers celui-ci :

```
docker run --net host -v $(pwd):/src -ti mhart/alpine-node:7.1 shnpm install -g number-aggregator-statsnode /src/server1.js | number-aggregator-stats
```

```
Meas: 18 Min: 3 Max: 4 Avg: 4 Cur: 4
```

Exécutons maintenant notre benchmark à nouveau — 3 minutes, 1k requêtes simultanées, pas de timeouts :

```
node /src/server1.js | number-aggregator-stats
```

```
Meas: 1745 Min: 3 Max: 349 Avg: 194 Cur: 232
```

Et maintenant, activons le timeout de 3s :

```
node /src/server1.js | number-aggregator-stats
```

```
Meas: 1429 Min: 3 Max: 411 Avg: 205 Cur: 172
```

Oh là là, à première vue, il semble que **les timeouts n'aident pas après tout : notre utilisation de mémoire atteint un pic avec les timeouts activés et est, en moyenne, 5 % plus élevée également**. Y a-t-il une explication raisonnable à cela ?

Bien sûr, car nous devons simplement revenir à siege et regarder le rps :

```
853.60 trans/sec --> sans timeouts1134.48 trans/sec --> avec timeouts
```

Ici, nous comparons **des pommes avec des oranges**. Il est inutile de regarder l'utilisation de la mémoire de deux serveurs qui servent un nombre différent de rps. Nous devrions plutôt nous assurer qu'ils offrent tous deux le même débit, et ne mesurer la mémoire qu'à ce moment-là. Sinon, le serveur qui sert plus de requêtes partira toujours avec un certain désavantage !

Pour ce faire, nous avons besoin d'un outil qui facilite la génération de charges basées sur le rps, et siege n'est pas très adapté à cela. Il est temps d'appeler notre ami [vegeta](https://github.com/tsenart/vegeta), un outil moderne de test de charge écrit en [Golang](https://golang.org/).

### Entrez vegeta

![Image](https://cdn-media-1.freecodecamp.org/images/0*EUTGjti8owj7vE50.jpg)

Vegeta est très simple à utiliser, il suffit de commencer à "attaquer" un serveur et de le laisser rapporter les résultats :

```
echo "GET http://google.com" | vegeta attack --duration 1h -rate 1000 | tee results.bin | vegeta report
```

Deux options très intéressantes ici :

* `--duration`, afin que vegeta s'arrête après un certain temps
* `--rate`, comme dans rps

Il semble que vegeta soit l'outil qu'il nous faut — nous pouvons alors émettre une commande adaptée à notre serveur et voir les résultats :

```
echo "GET http://localhost:3000" | vegeta attack --duration 3m --insecure -rate 1000 | tee results.bin | vegeta report
```

Voici ce que vegeta produit sans timeouts :

```
Requests      [total, rate]            180000, 1000.01Duration      [total, attack, wait]    3m10.062132905s, 2m59.998999675s, 10.06313323sLatencies     [mean, 50, 95, 99, max]  1.172619756s, 170.947889ms, 10.062145485s, 10.134037994s, 10.766903205sBytes In      [total, mean]            1080000, 6.00Bytes Out     [total, mean]            0, 0.00Success       [ratio]                  100.00%Status Codes  [code:count]             200:180000Error Set:
```

et voici ce que nous obtenons lorsque `server1.js` a le timeout de 3s activé :

```
Requests      [total, rate]            180000, 1000.01Duration      [total, attack, wait]    3m3.028009507s, 2m59.998999479s, 3.029010028sLatencies     [mean, 50, 95, 99, max]  455.780741ms, 162.876833ms, 3.047947339s, 3.070030628s, 3.669993753sBytes In      [total, mean]            1142472, 6.35Bytes Out     [total, mean]            0, 0.00Success       [ratio]                  90.00%Status Codes  [code:count]             500:18000  200:162000Error Set:500 Internal Server Error
```

Comme vous le voyez, le nombre total de requêtes et le temps écoulé sont les mêmes entre les deux benchmarks, ce qui signifie que nous avons soumis les serveurs au même niveau de stress. Maintenant que nous les avons fait effectuer les mêmes tâches, sous la même charge, nous pouvons regarder l'utilisation de la mémoire pour voir si les timeouts nous ont aidé à maintenir une empreinte mémoire plus faible.

Sans timeouts :

```
node /src/server1.js | number-aggregator-stats
```

```
Meas: 1818 Min: 3 Max: 372 Avg: 212 Cur: 274
```

et avec timeouts :

```
node /src/server1.js | number-aggregator-stats
```

```
Meas: 1886 Min: 3 Max: 299 Avg: 149 Cur: 292
```

Cela ressemble plus à ce que nous voulons : les timeouts nous ont aidé à maintenir **l'utilisation de la mémoire, en moyenne, 30 % plus faible**.

Tout cela grâce à un simple `.timeout(3000)`. Quelle victoire !

### Éviter l'effet domino

Me citant moi-même :

> _Que se passe-t-il lorsque ces services sont lents ou indisponibles ? Eh bien, vous ne pouvez pas traiter les requêtes de recherche ou les paiements, mais votre application fonctionnerait toujours "bien" — n'est-ce pas ?_

Fait amusant : **un timeout manquant peut paralyser toute votre infrastructure !**

![Image](https://cdn-media-1.freecodecamp.org/images/0*5ewVUhjYhEJnJ4VR.jpg)

Dans notre exemple de base, nous avons vu comment un service qui commence à échouer à un taux de 10 % peut augmenter significativement l'utilisation de la mémoire des services qui en dépendent. Ce n'est pas un scénario irréaliste — c'est essentiellement juste un seul serveur défectueux dans un pool de dix.

Imaginez que vous avez une page web qui dépend d'un service backend, derrière un équilibreur de charge, qui commence à fonctionner plus lentement que d'habitude. Le service fonctionne toujours (il est simplement beaucoup plus lent qu'il ne le devrait), votre vérification de santé reçoit probablement toujours un `200 Ok` du service (même si cela prend plusieurs secondes plutôt que des millisecondes), donc le service ne sera pas retiré de l'équilibreur de charge.

Vous venez de créer **un piège pour vos frontends**. Ils commenceront à nécessiter plus de mémoire, serviront moins de requêtes et... c'est une recette pour le désastre.

Voici à quoi ressemble un effet domino : un système ralentit (ou subit un temps d'arrêt) et d'autres parties de l'architecture sont affectées, mettant en évidence une conception qui n'a pas considéré l'échec comme une option et qui n'est ni suffisamment robuste ni résiliente.

La chose clé à garder à l'esprit est celle-ci : **embrassez les échecs**, laissez-les venir, et assurez-vous de pouvoir les combattre avec facilité.

### Une note sur les timeouts

Si vous pensiez que l'attente est dangereuse, ajoutons du feu :

* Nous ne parlons pas seulement de HTTP — chaque fois que nous dépendons d'un système externe, nous devrions [utiliser des timeouts](https://github.com/mysqljs/mysql#connection-options)
* Un serveur pourrait avoir un port ouvert et abandonner chaque paquet que vous envoyez — cela entraînera un timeout de connexion TCP. Essayez ceci dans votre terminal : `time curl example.com:81`. Bonne chance !
* Un serveur pourrait répondre instantanément, mais être très lent à envoyer chaque paquet (comme en secondes entre les paquets). Vous devriez alors vous protéger contre un **timeout de lecture**.

...et bien d'autres cas limites à lister. Je sais, les systèmes distribués sont méchants.

Heureusement, les API de haut niveau (comme celle [exposée par unirest](https://github.com/Mashape/unirest-nodejs#requesttimeoutnumber)) sont généralement utiles, car elles prennent en charge tous les hoquets qui peuvent se produire en cours de route.

### Remarques finales : J'ai enfreint chaque règle de benchmarking

Si vous avez des commentaires "agressifs" sur mes compétences de benchmarking rouillées... eh bien, je serais d'accord avec vous. J'ai délibérément pris quelques raccourcis pour simplifier mon travail et la capacité, pour vous, de reproduire facilement ces benchmarks.

Choses que vous devriez faire si vous êtes sérieux au sujet des benchmarks :

* N'exécutez pas le code que vous benchmarkez et l'outil que vous utilisez pour benchmarker sur la même machine. Ici, j'ai tout exécuté sur mon XPS qui est suffisamment puissant pour me permettre d'exécuter ces tests. Mais exécuter siege / vegeta sur la même machine que les serveurs a définitivement un impact sur les résultats (je dis `ulimit` et vous comprenez le reste). Mon conseil est d'essayer d'obtenir du matériel sur AWS et de benchmarker à partir de là — plus d'isolement, moins de doutes.
* Ne mesurez pas la mémoire en la journalisant avec un `console.log`, utilisez plutôt un outil tel que NewRelic qui, je pense, est moins invasif.
* Mesurez plus de données : benchmarker pendant trois minutes est acceptable pour les besoins de cet article, mais si nous voulons examiner des données réelles, pour donner une meilleure estimation de l'utilité des timeouts, vous devriez laisser les benchmarks fonctionner beaucoup plus longtemps.
* Gardez Gmail fermé pendant que vous exécutez `siege ...`, les locataires vivant dans `/proc/cpuinfo` vous en seront reconnaissants.

Et... j'ai terminé pour la journée : j'espère que vous avez apprécié cet article et si ce n'est pas le cas, n'hésitez pas à râler dans la boîte de commentaires ci-dessous !

_Publié à l'origine sur [odino.org](http://odino.org/better-performance-the-case-for-timeouts/) (19 janvier 2017)._