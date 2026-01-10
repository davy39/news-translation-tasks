---
title: Un million de requêtes par seconde avec Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-31T12:53:09.000Z'
originalURL: https://freecodecamp.org/news/million-requests-per-second-with-python-95c137af319
coverImage: https://cdn-media-1.freecodecamp.org/images/1*nAr_UQ1RcT-2mcfstPLocQ.jpeg
tags:
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Un million de requêtes par seconde avec Python
seo_desc: 'By Paweł Piotr Przeradowski

  Is it possible to hit a million requests per second with Python? Probably not until
  recently.

  A lot of companies are migrating away from Python and to other programming languages
  so that they can boost their operation perf...'
---

Par Paweł Piotr Przeradowski

Est-il possible d'atteindre un million de requêtes par seconde avec Python ? Probablement pas jusqu'à récemment.

De nombreuses entreprises migrent de Python vers d'autres langages de programmation pour améliorer les performances de leurs opérations et économiser sur les coûts des serveurs, mais ce n'est pas vraiment nécessaire. Python peut être le bon outil pour le travail.

La communauté Python fait beaucoup de travail autour de la performance ces derniers temps. CPython 3.6 a amélioré les performances globales de l'interpréteur avec une nouvelle implémentation de dictionnaire. CPython 3.7 sera encore plus rapide, grâce à l'introduction d'une convention d'appel plus rapide et de caches de recherche de dictionnaire.

Pour les tâches de calcul numérique, vous pouvez utiliser PyPy avec sa compilation de code juste-à-temps. Vous pouvez également exécuter la suite de tests de NumPy, qui a maintenant une meilleure compatibilité globale avec les extensions C. Plus tard cette année, PyPy devrait atteindre la conformité avec Python 3.5.

Tout ce travail formidable m'a inspiré pour innover dans l'un des domaines où Python est largement utilisé : le développement web et de micro-services.

### Présentation de Japronto !

[Japronto](https://github.com/squeaky-pl/japronto) est un tout nouveau micro-framework conçu pour vos besoins en micro-services. Ses principaux objectifs incluent d'être **rapide**, **scalable** et **léger**. Il vous permet de faire à la fois de la programmation **synchrone** et **asynchrone** grâce à **asyncio**. Et il est éhontément **rapide**. Même plus rapide que NodeJS et Go.

![Image](https://cdn-media-1.freecodecamp.org/images/9779nRzX6lCHig8qbn3OpPU9SKMO932AgagM)
_Micro-frameworks Python (bleu), Côté obscur de la force (vert) et Japronto (violet)_

**Errata :** Comme le souligne l'utilisateur @heppu, le serveur HTTP stdlib de Go peut être **12 % plus rapide** que ce que montre ce graphique lorsqu'il est écrit plus soigneusement. Il existe également un serveur **fasthttp** génial pour Go qui est apparemment **seulement 18 % plus lent** que Japronto dans ce benchmark particulier. Génial ! Pour plus de détails, voir [https://github.com/squeaky-pl/japronto/pull/12](https://github.com/squeaky-pl/japronto/pull/12) et [https://github.com/squeaky-pl/japronto/pull/14](https://github.com/squeaky-pl/japronto/pull/14).

![Image](https://cdn-media-1.freecodecamp.org/images/RuMsx3RuWjBh1ARw099oqvu2PHoE0e0z4uAh)

Nous pouvons également voir que le serveur WSGI Meinheld est presque à la hauteur de NodeJS et Go. Malgré sa conception intrinsèquement bloquante, il est un excellent performeur par rapport aux quatre précédents, qui sont des solutions Python asynchrones. Donc, ne faites jamais confiance à quiconque dit que les systèmes asynchrones sont toujours plus rapides. Ils sont presque toujours plus concurrents, mais il y a beaucoup plus à considérer que cela.

J'ai effectué ce micro-benchmark en utilisant une application "Hello world !", mais il démontre clairement le surcoût serveur-framework pour un certain nombre de solutions.

Ces résultats ont été obtenus sur une instance AWS c4.2xlarge qui avait 8 VCPU, lancée dans la région de São Paulo avec une location partagée par défaut et une virtualisation HVM et un stockage magnétique. La machine exécutait Ubuntu 16.04.1 LTS (Xenial Xerus) avec le noyau Linux 4.4.0–53-generic x86_64. Le système d'exploitation rapportait un CPU Xeon® CPU E5–2666 v3 @ 2.90GHz. J'ai utilisé Python 3.6, que j'ai fraîchement compilé à partir de son code source.

Pour être équitable, tous les concurrents (y compris Go) exécutaient un processus à travailleur unique. Les serveurs ont été testés en charge en utilisant [wrk](https://github.com/wg/wrk) avec 1 thread, 100 connexions et 24 requêtes simultanées (en pipeline) par connexion (parallélisme cumulé de 2400 requêtes).

![Image](https://cdn-media-1.freecodecamp.org/images/XS-U8gZ-oONKS2fSxqbfLxBwslkQnBbVvude)
_HTTP pipelining (crédit image Wikipedia)_

Le [HTTP pipelining](https://en.wikipedia.org/wiki/HTTP_pipelining) est crucial ici car c'est l'une des optimisations que Japronto prend en compte lors de l'exécution des requêtes.

La plupart des serveurs exécutent les requêtes des clients en pipeline de la même manière qu'ils le feraient pour les clients non-pipeline. Ils n'essaient pas de l'optimiser. (En fait, Sanic et Meinheld abandonneront également silencieusement les requêtes des clients en pipeline, ce qui est une violation du protocole HTTP 1.1.)

En termes simples, le pipelining est une technique dans laquelle le client n'a pas besoin d'attendre la réponse avant d'envoyer des requêtes ultérieures sur la même connexion TCP. Pour garantir l'intégrité de la communication, le serveur envoie plusieurs réponses dans le même ordre que les requêtes sont reçues.

### Les détails sanglants des optimisations

Lorsque de nombreuses petites requêtes GET sont regroupées ensemble par le client, il y a une forte probabilité qu'elles arrivent dans un seul paquet TCP (grâce à [l'algorithme de Nagle](https://en.wikipedia.org/wiki/Nagle's_algorithm)) côté serveur, puis soient **lues** en retour par un seul **appel système**.

Effectuer un appel système et déplacer des données de l'espace noyau vers l'espace utilisateur est une opération très coûteuse par rapport, par exemple, au déplacement de la mémoire dans l'espace processus. C'est pourquoi il est important d'effectuer aussi peu d'appels système que nécessaire (mais pas moins).

Lorsque Japronto reçoit des données et analyse avec succès plusieurs requêtes, il essaie d'exécuter toutes les requêtes aussi rapidement que possible, de coller les réponses dans le bon ordre, puis de les **écrire** en retour en **un seul appel système**. En fait, le noyau peut aider dans la partie collage, grâce aux appels système [scatter/gather IO](https://en.wikipedia.org/wiki/Vectored_I/O), que Japronto n'utilise pas encore.

Notez que cela n'est pas toujours possible, car certaines des requêtes pourraient prendre trop de temps, et les attendre augmenterait inutilement la latence.

Faites attention lorsque vous ajustez les heuristiques, et considérez le coût des appels système et le temps d'exécution prévu des requêtes.

![Image](https://cdn-media-1.freecodecamp.org/images/MyL1pnxpzOsWhqFZ3hC4MOgC-dm50Z792x2H)
_Japronto donne une médiane de 1 214 440 RPS de données continues groupées, calculée comme le 50e percentile, en utilisant l'interpolation._

Outre le retard des écritures pour les clients en pipeline, il existe plusieurs autres techniques que le code emploie.

[Japronto](https://github.com/squeaky-pl/japronto) est écrit presque entièrement en C. L'analyseur, le protocole, le réaper de connexions, le routeur, les objets de requête et de réponse sont écrits comme des extensions C.

[Japronto](https://github.com/squeaky-pl/japronto) essaie de retarder la création de contreparties Python de ses structures internes jusqu'à ce qu'elles soient explicitement demandées. Par exemple, un dictionnaire d'en-têtes ne sera pas créé tant qu'il n'est pas demandé dans une vue. Toutes les limites de jetons sont déjà marquées avant, mais la normalisation des clés d'en-tête et la création de plusieurs objets str sont effectuées lorsqu'ils sont accédés pour la première fois.

Japronto s'appuie sur l'excellente bibliothèque C picohttpparser pour analyser la ligne d'état, les en-têtes et un corps de message HTTP par morceaux. Picohttpparser utilise directement les instructions de traitement de texte trouvées dans les CPU modernes avec les extensions SSE4.2 (presque tous les CPU x86_64 de 10 ans ont cela) pour faire correspondre rapidement les limites des jetons HTTP. L'E/S est gérée par le super awesome uvloop, qui est lui-même un wrapper autour de libuv. Au niveau le plus bas, il s'agit d'un pont vers l'appel système epoll fournissant des notifications asynchrones sur la préparation de la lecture-écriture.

![Image](https://cdn-media-1.freecodecamp.org/images/cK6NIrvJAKMyVRlDlvqRufntECKK4vVs3YmR)
_Picohttpparser s'appuie sur SSE4.2 et CMPESTRI x86_64 intrinsic pour faire l'analyse_

Python est un langage à ramasse-miettes, donc il faut prendre soin de ne pas augmenter inutilement la pression sur le ramasse-miettes lors de la conception de systèmes haute performance. La conception interne de [Japronto](https://github.com/squeaky-pl/japronto) essaie d'éviter les cycles de référence et de faire autant d'allocations/désallocations que nécessaire. Il le fait en préallouant certains objets dans ce que l'on appelle des arènes. Il essaie également de réutiliser les objets Python pour les requêtes futures s'ils ne sont plus référencés au lieu de les jeter.

Toutes les allocations sont faites en multiples de 4 Ko. Les structures internes sont soigneusement disposées de sorte que les données utilisées fréquemment ensemble soient suffisamment proches en mémoire, minimisant la possibilité de défauts de cache.

Japronto essaie de ne pas copier entre les tampons inutilement et effectue de nombreuses opérations en place. Par exemple, il décode en pourcentage le chemin avant la correspondance dans le processus du routeur.

### Contributeurs open source, j'aurais besoin de votre aide.

Je travaille sur [Japronto](https://github.com/squeaky-pl/japronto) en continu depuis les 3 derniers mois — souvent pendant les week-ends, ainsi que les jours de travail normaux. Cela n'a été possible que grâce à une pause dans mon travail de programmeur régulier et en mettant tous mes efforts dans ce projet.

Je pense qu'il est temps de partager le fruit de mon travail avec la communauté.

Actuellement, [Japronto](https://github.com/squeaky-pl/japronto) implémente un ensemble de fonctionnalités assez solide :

* Implémentation HTTP 1.x avec support des téléchargements par morceaux
* Support complet du HTTP pipelining
* Connexions keep-alive avec réaper configurable
* Support des vues synchrones et asynchrones
* Modèle maître-multiworker basé sur le fork
* Support du rechargement du code lors des changements
* Routage simple

J'aimerais me pencher sur les Websockets et les réponses HTTP en streaming de manière asynchrone ensuite.

Il reste beaucoup de travail à faire en termes de documentation et de tests. Si vous êtes intéressé pour aider, veuillez [me contacter directement sur Twitter](http://twitter.com/squeaky_pl). Voici [le dépôt GitHub du projet Japronto](https://github.com/squeaky-pl/japronto).

De plus, si votre entreprise cherche un développeur Python qui est un passionné de performance et qui fait aussi du DevOps, je suis ouvert à en entendre parler. Je vais considérer des postes dans le monde entier.

### Mots de la fin

Toutes les techniques que j'ai mentionnées ici ne sont pas vraiment spécifiques à Python. Elles pourraient probablement être employées dans d'autres langages comme Ruby, JavaScript ou même PHP. Je serais intéressé à faire un tel travail, mais cela ne se produira malheureusement pas à moins que quelqu'un puisse le financer.

Je tiens à remercier la communauté Python pour leur investissement continu dans l'ingénierie des performances. Notamment Victor Stinner @VictorStinner, [INADA Naoki](https://twitter.com/methane?lang=en) @methane et Yury Selivanov @1st1 et toute l'équipe PyPy.

Pour l'amour de Python.