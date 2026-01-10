---
title: Comment conteneuriser une application Spring Data Cassandra
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-08T05:42:17.000Z'
originalURL: https://freecodecamp.org/news/how-to-containerise-a-spring-data-cassandra-application-de4254240511
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3DebQtXUVpccosiYyNJ3HQ.png
tags:
- name: containers
  slug: containers
- name: Docker
  slug: docker
- name: General Programming
  slug: programming
- name: spring-boot
  slug: spring-boot
- name: technology
  slug: technology
seo_title: Comment conteneuriser une application Spring Data Cassandra
seo_desc: 'By Daniel Newton

  In this post, I’ll be continuing my journey of learning Docker. I am still keeping
  it simple at this point. This time around, I am going to tackle converting a Spring
  and Cassandra application to use containers instead of running loc...'
---

Par Daniel Newton

Dans cet article, je vais continuer mon apprentissage de Docker. Je garde toujours les choses simples pour l'instant. Cette fois-ci, je vais m'attaquer à la conversion d'une application Spring et Cassandra pour utiliser des conteneurs au lieu de s'exécuter localement sur la machine hôte. Plus précisément, en utilisant Spring Data Cassandra pour configurer l'application.

J'aurais aimé m'intéresser à cela il y a quelque temps. J'ai écrit un nombre considérable d'articles sur Cassandra. Chaque fois, je devais me rendre dans le bon répertoire avec `cd` ou avoir un raccourci pour la démarrer. Je suppose que ce n'est pas si grave, mais il y avait quelques autres choses impliquées — comme supprimer et recréer des keyspaces pour que je puisse tester mon application à partir de zéro. Maintenant, je supprime le conteneur et le redémarre. Pour moi, en tout cas, c'est utile !

Cet article sera différent de mon précédent article, [Utiliser Docker pour mettre une application existante dans des conteneurs](https://lankydanblog.com/2018/09/02/using-docker-to-shove-an-existing-application-into-some-containers/). Au lieu de cela, je me concentrerai davantage ici sur le côté application et supprimerai les étapes intermédiaires de l'utilisation exclusive de Docker. Je passerai directement à Docker Compose.

### Conteneurs, conteneurs, conteneurs

Je pense qu'il est préférable de commencer par le côté conteneur du projet. L'application dépend de la configuration du conteneur Cassandra.

C'est parti !

Il n'y a pas grand-chose ici. Ce `Dockerfile` construit l'image de l'application Spring qui sera mise dans un conteneur dans quelques instants.

Ensuite, voici le fichier `docker-compose`. Cela construira à la fois les conteneurs de l'application Spring et Cassandra :

Encore une fois, il n'y a pas trop de choses ici. Le conteneur `app` construit l'application Spring en utilisant le `Dockerfile` défini précédemment. Le conteneur `cassandra` repose quant à lui sur une image existante, appropriément nommée `cassandra`.

Une chose qui se démarque est que la propriété `restart` est définie sur `always`. C'était ma tentative paresseuse de contourner le temps que Cassandra met à démarrer. De plus, tous les conteneurs démarrés avec `docker-compose` démarrent en même temps. Cela conduit à une situation où l'application essaie de se connecter à Cassandra sans qu'elle soit prête. Malheureusement, cela conduit à la mort de l'application. J'espérais qu'elle aurait une capacité de nouvelle tentative pour la connectivité initiale intégrée... Mais ce n'est pas le cas.

Lorsque nous passerons en revue le code, nous verrons comment gérer la connexion initiale à Cassandra de manière programmatique au lieu de compter sur la mort de l'application et son redémarrage multiple. Vous verrez ma version de la gestion de la connexion, en tout cas. Je ne suis pas un grand fan de ma solution, mais tout le reste que j'ai essayé m'a causé beaucoup plus de problèmes.

### Une touche de code

J'ai dit que cet article se concentrerait davantage sur le code de l'application, ce qu'il fera. Nous n'allons pas plonger dans tout ce que j'ai mis dans cette application et comment utiliser Cassandra. Pour ce type d'informations, vous pouvez consulter mes anciens articles, que je lierai à la fin. Ce que nous ferons, cependant, c'est examiner le code de configuration qui crée les beans qui se connectent à Cassandra.

Tout d'abord, passons en revue `ClusterConfig` qui configure le cluster Cassandra :

Il n'y a pas trop de choses là-dedans. Il y en aurait encore moins si Spring réessayait la connexion initiale à Cassandra. En tout cas, laissons cette partie de côté pendant quelques minutes et concentrons-nous sur les autres points de cette classe.

La raison originale pour laquelle j'ai créé `ClusterConfig` était de créer le keyspace que l'application utilisera. Pour ce faire, `getKeyspaceCreations` a été substitué. Lorsque l'application se connecte, elle exécutera la requête définie dans cette méthode pour créer le keyspace.

Si cela n'était pas nécessaire et que le keyspace était créé d'une autre manière, par exemple, un script exécuté dans le cadre de la création du conteneur Cassandra, la configuration automatique de Spring Boot pourrait être utilisée à la place. Cela permet en fait de configurer toute l'application avec les propriétés définies dans `application.properties` et rien d'autre. Hélas, ce n'était pas destiné à être.

Puisque nous avons défini un `AbstractClusterConfiguration`, Spring Boot désactivera sa configuration dans ce domaine. Par conséquent, nous devons définir les `contactPoints` (j'ai nommé la variable `hosts`) manuellement en substituant la méthode `getContactPoints`. À l'origine, cela n'était défini que dans `application.properties`. J'ai réalisé que je devais apporter cette modification une fois que j'ai commencé à obtenir l'erreur suivante :

```
All host(s) tried for query failed (tried: localhost/127.0.0.1:9042 (com.datastax.driver.core.exceptions.TransportException: [localhost/127.0.0.1:9042] Cannot connect))
```

Avant de créer `ClusterConfig`, l'adresse était `cassandra` plutôt que `localhost`.

Aucune autre propriété pour le cluster ne doit être configurée. Les valeurs par défaut de Spring sont suffisantes pour ce scénario.

J'ai mentionné `application.properties` tellement à ce stade que je devrais probablement vous montrer ce qu'il contient.

`keyspace-name` et `contact-points` ont déjà été mentionnés puisqu'ils sont liés à la configuration du cluster. `schema-action` est nécessaire pour créer des tables basées sur les entités du projet. Nous n'avons pas besoin de faire autre chose ici puisque l'auto-configuration fonctionne toujours dans ce domaine.

Le fait que la valeur `contact-points` soit définie sur `cassandra` est très important. Ce nom de domaine provient du nom donné au conteneur, dans ce cas, `cassandra`. Par conséquent, soit `cassandra` peut être utilisé, soit l'IP réelle du conteneur. Le nom de domaine est définitivement plus facile puisqu'il sera toujours statique entre les déploiements. Pour tester cette théorie, vous pouvez changer le nom du conteneur `cassandra` en ce que vous voulez. Il se connectera toujours, tant que vous le changez également dans `application.properties`.

Retour au code `ClusterConfig`. Plus précisément, le bean `cluster`. J'ai collé le code ci-dessous à nouveau pour qu'il soit plus facile à consulter :

Ce code n'est nécessaire que pour permettre des nouvelles tentatives sur la connexion initiale à Cassandra. C'est ennuyeux, mais je n'ai pas pu trouver une autre solution simple. Si vous en avez une meilleure, alors faites-le moi savoir !

Ce que j'ai fait est en fait assez simple, mais le code lui-même n'est pas très beau. La méthode `cluster` est une copie carbone de la version substituée de `AbstractClusterConfiguration`, à l'exception de `RetryingCassandraClusterFactoryBean` (ma propre classe). La fonction originale utilisait un `CassandraClusterFactoryBean` (classe Spring) à la place.

Voici le `RetryingCassandraClusterFactoryBean` :

La méthode `afterPropertiesSet` dans le `CassandraClusterFactoryBean` original prend ses valeurs et crée la représentation d'un cluster Cassandra en délégant finalement au pilote Java Datastax (comme je l'ai mentionné tout au long de l'article). Si elle échoue à établir une connexion, une exception sera levée. Si l'exception n'est pas attrapée, elle provoquera la terminaison de l'application. C'est tout l'intérêt du code ci-dessus. Il enveloppe le `afterPropertiesSet` dans un bloc try-catch spécifié pour les exceptions qui peuvent être levées.

Le `sleep` est ajouté pour donner à Cassandra un peu de temps pour démarrer. Il n'y a pas d'intérêt à essayer de se reconnecter immédiatement lorsque la tentative précédente a échoué.

En utilisant ce code, l'application se connectera finalement à Cassandra.

À ce stade, je montrerais normalement des logs sans importance pour prouver que l'application fonctionne. Mais dans cette situation, cela n'apporte rien. Faites-moi confiance lorsque je dis que si vous exécutez la commande suivante :

```
mvn clean install && docker-compose up
```

alors l'image de l'application Spring est créée et les deux conteneurs sont démarrés.

### Conclusion

Nous avons examiné comment mettre une application Spring qui se connecte à une base de données Cassandra dans des conteneurs. Un pour l'application et un autre pour Cassandra.

L'image de l'application est construite à partir du code du projet. L'image Cassandra est prise à partir de Docker Hub. Le nom de l'image est `cassandra` juste pour être sûr que personne n'oublie.

En général, connecter les deux conteneurs ensemble était relativement simple. L'application avait besoin de quelques ajustements pour permettre des nouvelles tentatives lors de la connexion à Cassandra s'exécutant dans l'autre conteneur. Cela a rendu le code un peu moins beau, mais il fonctionne au moins.

Grâce au code écrit dans cet article, j'ai maintenant une autre application que je n'ai pas besoin de configurer sur ma propre machine.

Le code utilisé dans cet article peut être trouvé sur mon [GitHub](https://github.com/lankydan/spring-data-cassandra-docker).

Si vous avez trouvé cet article utile, vous pouvez me suivre sur Twitter à [@LankyDanDev](http://www.twitter.com/LankyDanDev) pour rester informé de mes nouveaux articles.

### Liens vers mes articles sur Spring Data Cassandra

* [Commencer avec Spring Data Cassandra](https://lankydanblog.com/2017/10/12/getting-started-with-spring-data-cassandra/)
* [Keyspaces séparés avec Spring Data Cassandra](https://lankydanblog.com/2017/10/22/separate-keyspaces-with-spring-data-cassandra/)
* [Plusieurs keyspaces utilisant un seul CassandraTemplate de Spring Data](https://lankydanblog.com/2017/11/12/multiple-keyspaces-using-a-single-spring-data-cassandratemplate/)
* [Modélisation plus complexe avec Spring Data Cassandra](https://lankydanblog.com/2017/11/26/more-complex-modelling-with-spring-data-cassandra/)
* [Scripts de démarrage et d'arrêt dans Spring Data Cassandra](https://lankydanblog.com/2017/12/03/startup-and-shutdown-scripts-in-spring-data-cassandra/)
* [Reactive Streams avec Spring Data Cassandra](https://lankydanblog.com/2017/12/11/reactive-streams-with-spring-data-cassandra/)
* [Plomberie incluse avec l'auto-configuration dans Spring Data Cassandra](https://lankydanblog.com/2017/12/16/plumbing-included-with-auto-configuration-in-spring-data-cassandra/)
* [Interagir avec Cassandra en utilisant le pilote Java Datastax](https://lankydanblog.com/2018/04/15/interacting-with-cassandra-using-the-datastax-java-driver/)

Wow, je ne réalisais pas que j'avais écrit autant d'articles sur Cassandra.

Les opinions et points de vue trouvés dans mes articles sont les miens et ne représentent pas les vues d'Accenture sur aucun sujet. [Voir tous les articles de Dan Newton](https://lankydanblog.com/author/danknewton/)

_Publié à l'origine sur [lankydanblog.com](https://lankydanblog.com/2018/09/08/containerising-a-spring-data-cassandra-application/) le 8 septembre 2018._