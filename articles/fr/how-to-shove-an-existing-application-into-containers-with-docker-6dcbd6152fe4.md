---
title: Comment mettre une application existante dans des conteneurs avec Docker
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-02T14:38:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-shove-an-existing-application-into-containers-with-docker-6dcbd6152fe4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*mxgRaQctGgv6qSSjNrq1JQ.png
tags:
- name: Docker
  slug: docker
- name: Java
  slug: java
- name: MongoDB
  slug: mongodb
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment mettre une application existante dans des conteneurs avec Docker
seo_desc: 'By Daniel Newton

  I have finally got round to learning how to use Docker past the level of knowing
  what it is and does without ever using it. This is the first post that I have attempted
  to use Docker in and will probably be what I refer to whenever I...'
---

Par Daniel Newton

J'ai enfin pris le temps d'apprendre à utiliser Docker au-delà du simple fait de savoir ce que c'est et ce qu'il fait sans jamais l'avoir utilisé. C'est le premier article dans lequel j'ai tenté d'utiliser Docker et il sera probablement celui auquel je me référerai chaque fois que je commencerai un nouveau projet (pour Java ou Kotlin en tout cas).

Ce sera un court article qui prend un projet existant (issu de l'un de mes autres articles) et le modifie pour qu'il puisse s'exécuter dans des conteneurs. Le projet est une application Spring Boot avec une base de données MongoDB et une file d'attente de messages ActiveMQ. Tous ces composants sont parfaits pour la conteneurisation.

En suivant les étapes décrites dans cet article, il n'est plus nécessaire d'avoir une installation locale de MongoDB et ActiveMQ. Il suffit d'installer Docker et vous êtes prêt à partir. Cela représente déjà une victoire à mes yeux.

Voici les liens vers le [code](https://github.com/lankydan/spring-boot-jms) et l'article de blog correspondant [blog post](https://lankydanblog.com/2017/06/18/using-jms-in-spring-boot/). L'article couvre toutes les informations sur le code.

Une dernière remarque : pour le contenu de cet article, je suppose que vous avez déjà installé Docker. Si ce n'est pas le cas, Docker a déjà tout prévu. Voici où vous pouvez trouver les [plateformes supportées](https://docs.docker.com/install/#supported-platforms) qui fournissent des liens supplémentaires sur la façon d'installer Docker pour votre machine spécifique. La page d'[orientation et d'installation](https://docs.docker.com/get-started/) fournie par Docker peut également être utile.

### Conversion de l'application Spring

Commençons par l'application Spring Boot.

C'est la seule partie du projet qui contient notre code. Le reste est constitué d'images téléchargées depuis le dépôt de quelqu'un d'autre. Pour commencer à déplacer cette application vers une exécution dans un conteneur, nous devons créer un `Dockerfile` qui spécifie le contenu d'une image :

Cela prend l'image de base `openjdk:8-jdk-alpine`. C'est un bon point de départ pour l'application. Il ajoute le Jar construit à partir du code de l'application (en le nommant `app.jar`) et expose un port pour la communication entre les conteneurs. La dernière ligne définit la commande qui est exécutée lorsque l'image est lancée dans un conteneur. C'est ce qui démarre l'application Spring.

Pour construire une image à partir du `Dockerfile`, exécutez la commande suivante (en supposant que vous avez déjà construit le code de l'application) :

```
docker build -t spring-boot-jms-tutorial .
```

Il y a maintenant une image nommée `spring-boot-jms-tutorial` (`-t` nous permet de définir le nom). Cela peut maintenant être utilisé pour créer un conteneur qui exécute le code qui est empaqueté dans le Jar de l'image :

```
docker run --name application -p 4000:8080 spring-boot-jms-tutorial
```

Cela créera et exécutera un conteneur construit à partir de l'image `spring-boot-jms-tutorial`. Il nomme le conteneur `application` et la propriété `-p` permet de mapper un port d'une machine locale à un port à l'intérieur du conteneur. Pour accéder au port `8080` du conteneur, il suffit d'utiliser le port `4000` sur notre propre machine.

Si nous arrêtions ce conteneur et que nous voulions le relancer, nous devrions utiliser la commande :

```
docker start application
```

Où `application` est le nom du conteneur que nous avons créé précédemment. Si `docker run` était utilisé à nouveau, il créerait un autre nouveau conteneur au lieu de réutiliser celui existant. En fait, parce que nous avons fourni un nom au conteneur, exécuter la même commande `run` que précédemment entraînerait une erreur.

Maintenant, l'application Spring s'exécute avec succès dans un conteneur, mais les logs ne semblent pas très bons. Jetons un rapide coup d'œil pour savoir ce que nous devons faire ensuite.

Échec de la connexion à MongoDB :

```
Exception in monitor thread while connecting to server mongocontainer:27017 com.mongodb.MongoSocketException: mongocontainer: Name does not resolve at com.mongodb.ServerAddress.getSocketAddress(ServerAddress.java:188) ~[mongodb-driver-core-3.6.4.jar!/:na] at com.mongodb.connection.SocketStreamHelper.initialize(SocketStreamHelper.java:59) ~[mongodb-driver-core-3.6.4.jar!/:na] at com.mongodb.connection.SocketStream.open(SocketStream.java:57) ~[mongodb-driver-core-3.6.4.jar!/:na] at com.mongodb.connection.InternalStreamConnection.open(InternalStreamConnection.java:126) ~[mongodb-driver-core-3.6.4.jar!/:na] at com.mongodb.connection.DefaultServerMonitor$ServerMonitorRunnable.run(DefaultServerMonitor.java:114) ~[mongodb-driver-core-3.6.4.jar!/:na] at java.lang.Thread.run(Thread.java:748) [na:1.8.0_171] Caused by: java.net.UnknownHostException: mongocontainer: Name does not resolve at java.net.Inet4AddressImpl.lookupAllHostAddr(Native Method) ~[na:1.8.0_171] at java.net.InetAddress$2.lookupAllHostAddr(InetAddress.java:928) ~[na:1.8.0_171] at java.net.InetAddress.getAddressesFromNameService(InetAddress.java:1323) ~[na:1.8.0_171] at java.net.InetAddress.getAllByName0(InetAddress.java:1276) ~[na:1.8.0_171] at java.net.InetAddress.getAllByName(InetAddress.java:1192) ~[na:1.8.0_171] at java.net.InetAddress.getAllByName(InetAddress.java:1126) ~[na:1.8.0_171] at java.net.InetAddress.getByName(InetAddress.java:1076) ~[na:1.8.0_171] at com.mongodb.ServerAddress.getSocketAddress(ServerAddress.java:186) ~[mongodb-driver-core-3.6.4.jar!/:na] ... 5 common frames omitted
```

ActiveMQ n'est pas non plus disponible :

```
Could not refresh JMS Connection for destination 'OrderTransactionQueue' - retrying using FixedBackOff{interval=5000, currentAttempts=1, maxAttempts=unlimited}. Cause: Could not connect to broker URL: tcp://activemqcontainer:61616. Reason: java.net.UnknownHostException: activemqcontainer
```

Nous allons résoudre ces problèmes dans les prochaines sections afin que l'application puisse fonctionner dans son intégralité.

Une dernière chose avant de passer à l'examen de Mongo et ActiveMQ.

Le plugin `dockerfile-maven-plugin` pourrait également être utilisé pour aider à ce qui précède, ce qui construit le conteneur dans le cadre de l'exécution de `mvn install`. Je n'ai pas choisi de l'utiliser car je n'ai pas réussi à le faire fonctionner correctement avec `docker-compose`. Voici un exemple rapide de l'utilisation du plugin :

Cela nous permet ensuite de remplacer quelques lignes dans le `Dockerfile` :

Ici, une ligne a été ajoutée et une ligne existante a été modifiée. L'argument `JAR_FILE` remplace le nom original du Jar qui est injecté par le plugin à partir du `pom.xml`. Apportons ces modifications et exécutons `mvn install` et hop, votre conteneur est construit avec tout le code requis.

### Utilisation de l'image MongoDB

Il existe une image MongoDB prête à être utilisée. Elle est idéalement nommée `mongo`... Que pouviez-vous attendre d'autre ? Tout ce que nous avons à faire est d'exécuter l'image et de donner un nom à son conteneur :

```
docker run -d --name mongocontainer mongo
```

L'ajout de `-d` exécutera le conteneur en arrière-plan. Le nom du conteneur n'est pas seulement pour la commodité, car l'application Spring en aura besoin plus tard pour se connecter à Mongo.

### Passage à l'image ActiveMQ

La configuration d'ActiveMQ est tout aussi simple que celle de Mongo. Exécutez la commande suivante :

```
docker run -d --name activemqcontainer -p 8161:8161 rmohr/activemq
```

Ici, les ports `8161` sont mappés du conteneur vers la machine sur laquelle il s'exécute, permettant à la console d'administration d'être accessible depuis l'extérieur du conteneur.

### Tout rassembler

Si vous avez exécuté toutes ces commandes au fur et à mesure de votre lecture de l'article, vous aurez remarqué que le conteneur `application` n'a en fait pas pu voir les conteneurs `mongocontainer` et `activemqcontainer`. Cela est dû au fait qu'ils ne s'exécutent pas dans le même réseau. Les faire communiquer n'est pas difficile et ne nécessite que quelques étapes supplémentaires.

Par défaut, Docker crée un réseau Bridge lors de la configuration sans configuration supplémentaire. Voici comment procéder :

```
docker network create network
```

Maintenant que le réseau (nommé `network`) est créé, les commandes qui ont été exécutées précédemment doivent être modifiées pour créer des conteneurs qui se connecteront au réseau. Voici les 3 commandes utilisées pour créer les conteneurs dans les sections précédentes, chacune modifiée pour rejoindre le réseau.

```
docker run -d --name mongocontainer --network=network mongo
docker run -d --name activemqcontainer -p 8161:8161 --network=network rmohr/activemq
docker run --name application -p 4000:8080 --network=network spring-boot-jms-tutorial
```

Une fois que toutes ces commandes sont exécutées, l'application dans son ensemble fonctionnera désormais. Chaque conteneur peut voir les autres. Permettant au conteneur `application` de se connecter à MongoDB et ActiveMQ dans leurs conteneurs respectifs.

À ce stade, tout fonctionne. Cela s'exécute de la même manière que je m'en souviens lorsque j'avais tout configuré sur mon propre ordinateur portable. Mais cette fois-ci, rien n'est configuré localement... Sauf Docker !

### Docker Compose pour tout lancer

Nous aurions pu nous arrêter là, mais cette prochaine section rendra l'exécution de tout encore plus facile. Docker Compose nous permet de regrouper effectivement toutes les commandes que nous avons exécutées précédemment et de démarrer tous les conteneurs et leur réseau en une seule commande. Il y a un peu plus de configuration, mais au final, je pense que la quantité de frappe diminue réellement.

Pour ce faire, nous devons créer un fichier `docker-compose.yml` :

Utilisez cette version du `Dockerfile` :

C'est à peu près tout ce qui doit être fait.

`appcontainer` est le conteneur de l'application Spring construit à partir du code du projet. La propriété `build` du conteneur indique à Docker de construire l'image basée sur le `Dockerfile` du projet trouvé dans le répertoire racine du projet. Il passe l'argument `JAR_FILE` au `Dockerfile`, déplaçant certaines des configurations dans ce fichier.

Les deux autres conteneurs ne nécessitent pas beaucoup de configuration. Comme avec les commandes précédentes, les images à partir desquelles ils sont construits sont spécifiées et `activemqcontainer` ajoute une configuration autour de ses ports mappés.

La dernière partie de la configuration se fait en arrière-plan. Un réseau est créé et tous les conteneurs y sont ajoutés. Cela élimine le besoin de créer un réseau manuellement.

Il ne reste plus qu'à exécuter la commande `up` :

```
docker-compose up
```

Cela construira et exécutera tous les conteneurs. L'image du code de l'application est construite si nécessaire. L'exécution de cette commande exacte affichera tous les logs des conteneurs dans la console. Pour le faire en arrière-plan, ajoutez le drapeau `-d` :

```
docker-compose up -d
```

Après avoir fait cela, nous pouvons jeter un coup d'œil aux conteneurs et au réseau créés. Exécuter :

```
docker ps -a --format "table {{.Image}}\t{{.Names}}"
```

Nous montre :

```
IMAGE                          NAMES
mongo                          spring-boot-jms_mongocontainer_1
spring-boot-jms_appcontainer   spring-boot-jms_appcontainer_1
rmohr/activemq                 spring-boot-jms_activemqcontainer_1
```

Et le réseau :

```
docker network ls
```

Produit :

```
NETWORK ID       NAME                      DRIVER            SCOPE
163edcfe5ada     spring-boot-jms_default   bridge            local
```

Les noms des conteneurs et du réseau sont précédés du nom du projet.

### Conclusion

C'est tout ce qu'il y a à faire... pour une configuration simple en tout cas. Je suis sûr que les dieux de Docker pourraient faire beaucoup plus, mais je ne fais pas encore partie d'eux.

En conclusion, nous avons pris une application existante que j'ai écrite pour fonctionner localement sur une machine et nous avons tout mis dans quelques conteneurs. Cela signifie que nous sommes passés d'une machine qui devait avoir tout configuré (avec MongoDB et ActiveMQ installés) à une machine qui pouvait sauter toutes ces étapes en utilisant des conteneurs et en ne nécessitant qu'une installation de Docker. Docker gère ensuite toutes les dépendances pour nous.

Nous avons examiné comment déplacer chaque partie de l'application dans un conteneur, puis nous avons tout rassemblé avec Docker Compose. Cela nous laisse, à la fin de tout cela, avec une seule commande qui peut nous faire passer de absolument rien à tout ce dont nous avons besoin pour exécuter l'application.

Le code utilisé dans cet article peut être trouvé sur mon [GitHub](https://github.com/lankydan/spring-boot-jms-docker).

Si vous avez trouvé cet article utile, vous pouvez me suivre sur Twitter à l'adresse [@LankyDanDev](http://www.twitter.com/LankyDanDev) pour rester informé de mes nouveaux articles.

Les opinions et points de vue exprimés dans mes articles sont les miens et ne représentent pas les vues d'Accenture sur aucun sujet. [Voir tous les articles de Dan Newton](https://lankydanblog.com/author/danknewton/)

_Publié à l'origine sur [lankydanblog.com](https://lankydanblog.com/2018/09/02/using-docker-to-shove-an-existing-application-into-some-containers/) le 2 septembre 2018._