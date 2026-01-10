---
title: Comment Dockeriser une application Scala et Akka HTTP — la méthode facile
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-10T16:46:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-dockerise-a-scala-and-akka-http-application-the-easy-way-23310fc880fa
coverImage: https://cdn-media-1.freecodecamp.org/images/1*b7Wr6wXgoBALNMH7veOr2w.png
tags:
- name: Devops
  slug: devops
- name: Docker
  slug: docker
- name: General Programming
  slug: programming
- name: Scala
  slug: scala
- name: 'tech '
  slug: tech
seo_title: Comment Dockeriser une application Scala et Akka HTTP — la méthode facile
seo_desc: 'By Miguel Lopez

  Using Docker is a given nowadays. In this tutorial we will how to learn to dockerise
  our Scala and Akka HTTP applications without even creating a Dockerfile ourselves.

  For the purposes of this tutorial, we assume Docker is already ins...'
---

Par Miguel Lopez

L'utilisation de Docker est une évidence de nos jours. Dans ce tutoriel, nous allons apprendre à dockeriser nos applications Scala et Akka HTTP **sans** même créer un Dockerfile nous-mêmes.

Pour les besoins de ce tutoriel, nous supposons que Docker est déjà installé sur la machine. Si ce n'est pas le cas, veuillez suivre la [documentation officielle](https://docs.docker.com/install/).

Pour automatiser la création du Dockerfile pour notre projet, nous allons utiliser le plugin [sbt-native-packager](https://sbt-native-packager.readthedocs.io/en/stable/index.html).

Vous pouvez utiliser n'importe quel projet Scala ou Akka HTTP pour ce tutoriel. Nous allons utiliser le dépôt suivant [repository](https://github.com/Codemunity/akkahttp-quickstart), n'hésitez pas à le cloner et assurez-vous de vérifier la branche `6.5-testing-directives`.

### Ajout du plugin

Tout d'abord, nous devons ajouter le plugin à notre projet dans le fichier `project/plugins.sbt`. Si le fichier n'existe pas, nous devons le créer, puis ajouter la ligne suivante :

```
addSbtPlugin("com.typesafe.sbt" % "sbt-native-packager" % "1.3.6")
```

Ensuite, nous devons activer le plugin dans notre fichier `build.sbt`. Ajoutez la ligne suivante en haut :

```
enablePlugins(JavaAppPackaging)
```

L'activation de ce plugin nous permet également de créer un exécutable pour notre application. Exécutez `sbt stage` dans le répertoire racine du projet.

Maintenant, nous pouvons exécuter notre application en exécutant `./target/universal/stage/bin/akkahttp-quickstart`. Vous devriez voir un message `Success!`. Si vous envoyez une requête GET à `localhost:9000/todos`, vous obtiendrez quelques todos.

![Image](https://cdn-media-1.freecodecamp.org/images/jVniXyVNPfmJU9A2DQStDwnbF8NECz032xsA)

### Dockerisation de notre application

Il est temps de commencer à s'amuser avec Docker.

Commençons par générer le Dockerfile pour notre application. Exécutez `sbt docker:stage`, puis exécutez `cat target/docker/stage/Dockerfile` pour voir son contenu :

```
FROM openjdk:latestWORKDIR /opt/dockerADD --chown=daemon:daemon opt /optUSER daemonENTRYPOINT ["/opt/docker/bin/akkahttp-quickstart"]CMD []
```

C'est assez simple. Il finit par exécuter un binaire similaire à celui que nous avons généré et exécuté précédemment.

Nous pouvons construire une image Docker en utilisant ce Dockerfile manuellement, mais il existe une méthode plus pratique pour le faire. Exécutez `sbt docker:publishLocal`. Comme son nom l'indique, il publiera une image Docker de notre application dans notre registre local.

Exécutez `docker images` et vous devriez voir l'entrée suivante :

```
REPOSITORY            TAG     IMAGE ID       CREATED          SIZEakkahttp-quickstart   0.1     d03732dd0854   42 seconds ago   774MB
```

Nous pouvons maintenant exécuter notre application en utilisant Docker.

Exécutez `docker run akkahttp-quickstart:0.1`, vous devriez voir le message `Success!` une fois de plus.

Mais cette fois, si nous essayons d'interroger notre application, nous obtiendrons une erreur :

![Image](https://cdn-media-1.freecodecamp.org/images/RCytsNfGbtjSz-gywaiAP06joml9gbwl2nOE)

Exécutez `docker ps` pour obtenir des informations sur notre processus Docker en cours d'exécution (sortie abrégée) :

```
CONTAINER ID     IMAGE                       PORTS            NAMES9746162d4723     akkahttp-quickstart:0.1                      serene_agnesi
```

Comme nous pouvons le voir, aucun port n'est exposé, donc il n'y a aucun moyen de communiquer avec notre application.

Les applications dans Docker s'exécutent dans leur réseau par défaut. Il existe plusieurs façons de permettre la communication entre les processus Docker et la machine hôte. La méthode la plus simple consiste à exposer un port.

Arrêtez l'application en cours d'exécution, soit en appuyant sur `Ctrl-C`, soit en exécutant `docker stop $CONTAINER_ID`.

Cette fois, lorsque nous l'exécutons, nous exposons également le port respectif :

```
docker run -p 9000:9000 akkahttp-quickstart:0.1
```

Nous sommes maintenant en mesure d'interroger notre application dockerisée :

![Image](https://cdn-media-1.freecodecamp.org/images/3Wtn42GiMc9VPzZqNW1pJrZhzu39mlmFZcqt)

### Personnalisation de notre installation

Il y a plusieurs choses que nous pourrions vouloir faire avec la configuration actuelle que nous avons :

* Que faire si nous voulons un nom d'image différent ?
* Que faire si nous voulons utiliser un port différent ?
* Peut-on avoir une image plus légère ?

Explorons ces cas d'utilisation courants.

#### Changer le nom de l'image

Si nous regardons la [documentation officielle du plugin](https://sbt-native-packager.readthedocs.io/en/stable/formats/docker.html), nous voyons qu'il y a un certain nombre d'options que nous pouvons changer.

Lisez-la et voyez ce que vous pouvez personnaliser.

Pour changer le nom de l'image, nous pouvons modifier la propriété `packageName` dans notre fichier `build.sbt`, ajoutez la ligne suivante après la propriété `scalaVersion` :

```
packageName in Docker := "dockerised-akka-http"
```

Publions à nouveau l'image. Exécutez `sbt docker:publishLocal`. Nous pouvons vérifier que nous avons une nouvelle image en exécutant `docker images` :

```
REPOSITORY            TAG   IMAGE ID       CREATED          SIZE akkahttp-quickstart   0.1   d03732dd0854   42 minutes ago   774MB dockerised-akka-http  0.1   d03732dd0854   42 minutes ago   774MB
```

Maintenant, nous avons deux images, l'originale et la nouvelle. Super !

#### Changer le port

Nous ne pouvons pas changer le port que notre application écoute sans apporter des modifications au code. Le port est codé en dur dans notre application. Idéalement, nous le lirions à partir d'une variable d'environnement et peut-être en aurions un par défaut.

Mais ce n'est pas grave. Parce que notre application s'exécute dans un réseau différent, nous pouvons mapper un port différent au port interne 9000.

Lorsque nous spécifions le flag `-p 9000:9000`, nous disons que le port 9000 dans la machine hôte sera mappé au port 9000 dans le réseau de notre processus. Essayons de changer cela.

Exécutez `docker run -p 5000:9000 dockerised-akka-http:0.1` pour exécuter notre nouvelle image avec un port différent.

Nous pouvons interroger les `todos` pour nous assurer qu'il fonctionne comme prévu :

![Image](https://cdn-media-1.freecodecamp.org/images/Na3g2v4jd6FRCUrKyR84TR5lHIG6CrjG5BWn)

#### Rendre notre image plus légère

Pour notre dernière expérience, nous allons essayer de rendre notre image plus légère. À ce stade, elle utilise plus de 700 Mo.

Tout d'abord, augmentons la version afin d'obtenir une balise différente et de pouvoir les comparer. Ensuite, ajoutez `dockerBaseImage := "openjdk:8-jre-alpine"` au-dessus de l'endroit où nous changeons le `packageName`. Notre `build.sbt` ressemble maintenant à ceci :

```
enablePlugins(JavaAppPackaging)
```

```
name := "akkahttp-quickstart"version := "0.2"scalaVersion := "2.12.6"
```

```
dockerBaseImage := "openjdk:8-jre-alpine"packageName in Docker := "dockerised-akka-http"
```

```
val akkaVersion = "2.5.13"val akkaHttpVersion = "10.1.3"val circeVersion = "0.9.3"
```

```
libraryDependencies ++= Seq(  "com.typesafe.akka" %% "akka-actor" % akkaVersion,  "com.typesafe.akka" %% "akka-testkit" % akkaVersion % Test,  "com.typesafe.akka" %% "akka-stream" % akkaVersion,  "com.typesafe.akka" %% "akka-stream-testkit" % akkaVersion % Test,  "com.typesafe.akka" %% "akka-http" % akkaHttpVersion,  "com.typesafe.akka" %% "akka-http-testkit" % akkaHttpVersion % Test,  "io.circe" %% "circe-core" % circeVersion,  "io.circe" %% "circe-generic" % circeVersion,  "io.circe" %% "circe-parser" % circeVersion,  "de.heikoseeberger" %% "akka-http-circe" % "1.21.0",  "org.scalatest" %% "scalatest" % "3.0.5" % Test)
```

Nous utilisons une balise différente de l'image de base `openjdk` pour spécifier que nous voulons utiliser `alpine`, qui est une distribution Linux légère.

Publiez l'image en exécutant `sbt docker:publishLocal`. Obtenez les images avec `docker images`. Nous pouvons voir que l'image est plus légère maintenant :

```
REPOSITORY             TAG   IMAGE ID       CREATED          SIZE dockerised-akka-http   0.2   4688366e70bb   32 seconds ago   119MB akkahttp-quickstart    0.1   d03732dd0854   2 hours ago      774MBdockerised-akka-http   0.1   d03732dd0854   2 hours ago      774MB
```

Assurons-nous qu'elle fonctionne toujours.

Exécutez `docker run -p 5000:9000 dockerised-akka-http:0.2`, en faisant attention au numéro de la balise. Cela ne fonctionne pas, et nous obtenons l'erreur suivante :

```
env: can't execute 'bash': No such file or directory
```

Apparemment, notre application dockerisée a besoin de **bash** pour s'exécuter. En lisant la [documentation du plugin](https://sbt-native-packager.readthedocs.io/en/stable/archetypes/java_app/index.html?highlight=bash), nous pouvons voir qu'il génère un script bash qui exécute notre application.

Alors, installons bash dans notre image et essayons à nouveau.

Ajoutez les lignes suivantes en dessous de l'endroit où nous changeons le `packageName` dans notre fichier `build.sbt` :

```
import com.typesafe.sbt.packager.docker._dockerCommands ++= Seq(  Cmd("USER", "root"),  ExecCmd("RUN", "apk", "add", "--no-cache", "bash"))
```

Nous ajoutons quelques commandes supplémentaires à notre Dockerfile. Nous changeons l'utilisateur en `root` pour installer le package, puis nous installons bash.

Essayons d'exécuter à nouveau l'application, `docker run -p 5000:9000 dockerised-akka-http:0.2`. Et cela fonctionne maintenant, super !

Si nous vérifions à nouveau les images, celle basée sur **alpine** est un peu plus grande, environ 10 Mo. Ce n'est rien comparé aux environ 770 Mo des autres.

Installer bash dans **alpine** n'est pas la pire chose au monde. Certaines personnes finissent par l'ajouter de toute façon en raison de leur préférence et pour le débogage.

### Génération d'un exécutable compatible avec Ash

Installer bash sur notre image est un peu un contournement. Utilisons un plugin supplémentaire pour générer un exécutable compatible avec Alpine. Merci à [Muki Seller](http://disq.us/p/1vwhg62) de nous avoir fait connaître cette solution !

Selon la [documentation officielle](https://sbt-native-packager.readthedocs.io/en/stable/formats/docker.html#busybox-ash-support), nous devons activer le plugin supplémentaire `AshScriptPlugin`.

Modifiez le fichier `build.sbt` pour activer les deux plugins, et supprimez le contournement précédent :

```
enablePlugins(JavaAppPackaging, AshScriptPlugin)
```

```
name := "akkahttp-quickstart"version := "0.3"scalaVersion := "2.12.6"
```

```
dockerBaseImage := "openjdk:8-jre-alpine"packageName in Docker := "dockerised-akka-http"
```

```
val akkaVersion = "2.5.13"val akkaHttpVersion = "10.1.3"val circeVersion = "0.9.3"
```

```
libraryDependencies ++= Seq(  "com.typesafe.akka" %% "akka-actor" % akkaVersion,  "com.typesafe.akka" %% "akka-testkit" % akkaVersion % Test,  "com.typesafe.akka" %% "akka-stream" % akkaVersion,  "com.typesafe.akka" %% "akka-stream-testkit" % akkaVersion % Test,  "com.typesafe.akka" %% "akka-http" % akkaHttpVersion,  "com.typesafe.akka" %% "akka-http-testkit" % akkaHttpVersion % Test,
```

```
  "io.circe" %% "circe-core" % circeVersion,  "io.circe" %% "circe-generic" % circeVersion,  "io.circe" %% "circe-parser" % circeVersion,  "de.heikoseeberger" %% "akka-http-circe" % "1.21.0",
```

```
  "org.scalatest" %% "scalatest" % "3.0.5" % Test)
```

Nous avons également augmenté la version afin de pouvoir comparer et éviter d'écraser la précédente.

Exécutez `sbt docker:publishLocal`, puis `docker run dockerised-akka-http:0.3`.

Vous devriez voir le message de succès et, si vous interrogez les todos, vous devriez les voir également. Super !

### Conclusion

Dans ce tutoriel, nous avons dockerisé une application Scala et Akka HTTP. Rien n'a été fait spécifiquement pour cette application, ce qui signifie que la configuration fonctionnera pratiquement telle quelle.

Ensuite, nous avons examiné comment accomplir certains cas d'utilisation courants en personnalisant notre Dockerfile via le plugin.

Nous avons même réussi à réduire la taille de l'image de près de sept fois !

Incroyable, n'est-ce pas ?

Si vous avez aimé ce tutoriel et que vous souhaitez apprendre à construire une API pour une application de todos, consultez notre [nouveau cours **gratuit**](https://codemunity-courses.thinkific.com/courses/akka-http-quickstart/) ! 🎉

Publié à l'origine sur [www.codemunity.io](https://www.codemunity.io/tutorials/dockerising-akka-http/).