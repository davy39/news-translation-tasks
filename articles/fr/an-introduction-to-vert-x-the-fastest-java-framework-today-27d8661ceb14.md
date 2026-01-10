---
title: Une introduction à Vert.x, le framework Java le plus rapide aujourd'hui
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-06T16:52:04.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-vert-x-the-fastest-java-framework-today-27d8661ceb14
coverImage: https://cdn-media-1.freecodecamp.org/images/1*RovqxSyUULpHDMxwYGXQPA.png
tags:
- name: Java
  slug: java
- name: Scala
  slug: scala
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Une introduction à Vert.x, le framework Java le plus rapide aujourd'hui
seo_desc: 'By Martin Budi

  If you’ve recently googled “best web framework” you might have stumbled upon the
  Techempower benchmarks where more than three hundred frameworks are ranked. There
  you might have noticed that Vert.x is one of the top ranked, if not the ...'
---

Par Martin Budi

Si vous avez récemment recherché « meilleur framework web » sur Google, vous êtes peut-être tombé sur les benchmarks Techempower où plus de trois cents frameworks sont classés. Vous avez peut-être remarqué que Vert.x est l'un des mieux classés, sinon le [premier](https://www.techempower.com/benchmarks/#section=data-r17&hw=cl&test=fortune) selon certains critères.

Alors parlons-en.

Vert.x est un framework web polyglotte qui partage des fonctionnalités communes parmi ses langages supportés : Java, Kotlin, Scala, Ruby et Javascript. Peu importe le langage, Vert.x fonctionne sur la machine virtuelle Java (JVM). Étant modulaire et léger, il est conçu pour le développement de microservices.

Les benchmarks Techempower mesurent la performance de la mise à jour, de la récupération et de la livraison de données depuis une base de données. Plus il y a de requêtes servies par seconde, mieux c'est. Dans un tel scénario d'E/S où peu de calcul est impliqué, tout framework non bloquant aurait un avantage. Ces dernières années, un tel paradigme est presque inséparable de Node.js qui l'a popularisé avec sa boucle d'événements à thread unique.

Vert.x, comme Node, utilise une boucle d'événements unique. Mais Vert.x tire également parti de la JVM. Alors que Node fonctionne sur un seul cœur, Vert.x maintient un pool de threads dont la taille peut correspondre au nombre de cœurs disponibles. Avec un meilleur support de la concurrency, Vert.x est adapté non seulement pour les E/S mais aussi pour les processus intensifs en CPU qui nécessitent du calcul parallèle.

Les boucles d'événements, cependant, ne sont que la moitié de l'histoire. L'autre moitié a peu à voir avec Vert.x.

Pour se connecter à une base de données, un client nécessite un pilote de connecteur. Dans le monde Java, le pilote le plus courant pour Sql est JDBC. Le problème est que ce pilote est bloquant. Et il est bloquant au niveau de la socket. Un thread sera toujours bloqué là jusqu'à ce qu'il retourne avec une réponse.

Il va sans dire que le pilote a été un goulot d'étranglement dans la réalisation d'une application entièrement non bloquante. Heureusement, il y a eu des progrès (bien que non officiels) sur [un pilote asynchrone](https://github.com/mauricio/postgresql-async) avec plusieurs forks actifs, parmi eux :

* [https://github.com/jasync-sql/jasync-sql](https://github.com/jasync-sql/jasync-sql) (pour Postgres et MySql)
* [https://github.com/reactiverse/reactive-pg-client](https://github.com/reactiverse/reactive-pg-client) (Postgres)

#### **La règle d'or**

Vert.x est assez simple à utiliser, et un serveur http peut être démarré avec quelques lignes de code.

<script src="https://gist.github.com/inmyth/aeab72a71cb6afa05b4ba93776c8fbf6.js"></script>

La méthode requestHandler est l'endroit où la boucle d'événements livre l'événement de requête. Comme Vert.x est non-opinionné, le traitement est libre. Mais gardez à l'esprit la règle importante du thread non bloquant : ne le bloquez pas.

En travaillant avec la concurrency, nous pouvons puiser dans tant d'options disponibles aujourd'hui telles que Promise, Future, Rx, ainsi que la manière idiomatique propre à Vert.x. Mais à mesure que la complexité d'une application grandit, avoir une fonctionnalité asynchrone seule ne suffit pas. Nous avons également besoin de la facilité de coordination et d'enchaînement des appels tout en évitant l'enfer des callbacks, ainsi que de transmettre toute erreur de manière élégante.

Scala Future satisfait toutes les conditions ci-dessus avec l'avantage supplémentaire d'être basé sur les principes de la programmation fonctionnelle. Bien que cet article n'explore pas Scala Future en profondeur, nous pouvons l'essayer avec une application simple. Disons que l'application est un service API pour trouver un utilisateur donné son id :

<script src="https://gist.github.com/inmyth/3df58e683efb0b66e9123a536a5cb171.js"></script>

Il y a trois opérations impliquées : vérifier le paramètre de la requête, vérifier si l'id est valide et récupérer les données. Nous allons envelopper chacune de ces opérations dans un Future et coordonner l'exécution dans une structure de "for comprehension".

* La première étape consiste à faire correspondre la requête avec un service. Scala dispose d'une fonctionnalité puissante de correspondance de motifs que nous pouvons utiliser à cette fin. Ici, nous interceptons toute mention de "user" et la passons à notre service.
* Ensuite, nous arrivons au cœur de ce service où nos futures sont organisés dans une compréhension séquentielle. Le premier future **f1** enveloppe la vérification des paramètres. Nous voulons spécifiquement récupérer l'id de la requête get et le convertir en int. (Scala ne nécessite pas de retour explicite si la valeur de retour est la dernière ligne de la méthode.) Comme vous le voyez, cette opération pourrait potentiellement lancer une exception si l'id n'est pas un int ou n'est même pas disponible, mais cela va pour l'instant.
* Le deuxième future **f2** vérifie la validité de l'id. Nous bloquons tout id inférieur à 100 en appelant explicitement Future.failed avec notre propre CustomException. Sinon, nous passons un Future vide sous la forme de Future.unit comme validation réussie.
* Le dernier future **f3** récupère l'utilisateur avec l'id fourni par **f1**. Comme il s'agit simplement d'un exemple, nous ne nous connectons pas vraiment à une base de données. Nous retournons simplement une chaîne de caractères simulée.
* **map** exécute l'arrangement qui produit les données de l'utilisateur à partir de **f3** puis les imprime dans la réponse.
* Maintenant, si une erreur se produit dans une partie de la séquence, un Throwable est passé à **recover**. Ici, nous pouvons faire correspondre son type à une stratégie de récupération appropriée. En regardant notre code, nous avons anticipé plusieurs échecs potentiels tels que l'id manquant, ou l'id qui n'était pas un int ou n'était pas valide, ce qui lancerait des exceptions spécifiques. Nous traitons chacun d'eux dans handleException en passant un message d'erreur au client.

Cet arrangement fournit non seulement un flux asynchrone du début à la fin, mais aussi une approche propre pour gérer les erreurs. Et comme il est rationalisé à travers les gestionnaires, nous pouvons nous concentrer sur les choses qui comptent, comme les requêtes de base de données.

#### **Verticles, Event Bus, et autres pièges**

Vert.x offre également un modèle de concurrency appelé verticle qui ressemble au système Actor. (Si vous souhaitez en savoir plus, consultez mon [guide Akka Actor](https://medium.freecodecamp.org/still-using-synchronized-try-akka-actor-instead-ac2f2b22a9ed).) Verticle isole son état et son comportement pour fournir un environnement thread-safe. La seule façon de communiquer avec lui est par le biais d'un event bus.

Cependant, l'event bus de Vert.x nécessite que ses messages soient des String ou JSON. Cela rend difficile le passage d'objets non-POJO arbitraires. Et dans un système haute performance, traiter la conversion JSON est indésirable car cela impose un coût de calcul. Si vous développez des applications d'E/S, vous pourriez être mieux loti en n'utilisant ni verticle ni event bus, car de telles applications ont peu besoin d'état local.

Travailler avec certains composants de Vert.x peut également être assez difficile. Vous pourriez trouver un manque de documentation, des comportements inattendus, et même des échecs de fonctionnement. Vert.x pourrait souffrir de sa propre ambition, car le développement de nouveaux composants nécessiterait un portage à travers de nombreux langages. C'est une entreprise difficile. Pour cette raison, s'en tenir au cœur serait le meilleur.

Si vous développez une API publique, alors vertx-core devrait suffire. Si c'est une application web, vous pouvez ajouter vertx-web qui fournit la gestion des paramètres http et l'authentification JWT/Session. Ce sont les deux qui ont dominé les benchmarks de toute façon. Il y a une certaine diminution de performance dans certains tests pour l'utilisation de vertx-web, mais comme elle semble provenir de l'optimisation, elle pourrait être résolue dans les versions ultérieures.