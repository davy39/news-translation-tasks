---
title: Qu'est-ce que Docker ? Apprenez à utiliser les conteneurs – Expliqué avec des
  exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-04-19T19:50:39.000Z'
originalURL: https://freecodecamp.org/news/what-is-docker-learn-how-to-use-containers-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/how-to-use-docker-containers.png
tags:
- name: containerization
  slug: containerization
- name: containers
  slug: containers
- name: Docker
  slug: docker
seo_title: Qu'est-ce que Docker ? Apprenez à utiliser les conteneurs – Expliqué avec
  des exemples
seo_desc: "By Sebastian Sigl\nContainers are an essential tool for software development\
  \ today. Running applications in any environment becomes easy when you leverage\
  \ containers. \nThe most popular technology for running containers is Docker, which\
  \ runs on any ope..."
---

Par Sebastian Sigl

Les conteneurs sont un outil essentiel pour le développement logiciel aujourd'hui. Exécuter des applications dans n'importe quel environnement devient facile lorsque vous utilisez des conteneurs.

La technologie la plus populaire pour exécuter des conteneurs est [Docker](https://www.docker.com/), qui fonctionne sur n'importe quel système d'exploitation.

Dans cet article de blog, vous apprendrez à utiliser Docker pour les trois cas d'utilisation les plus essentiels. Vous apprendrez comment :

* exécuter une base de données localement en utilisant Docker,
* exécuter des tests automatisés en utilisant une base de données dockerisée,
* exécuter votre application localement et en production en utilisant Docker.

Vous utiliserez une application Java [Spring Boot](https://spring.io/projects/spring-boot), mais tous les enseignements s'appliquent à tout autre langage de programmation de votre choix.

Pour exécuter tous les exemples, vous devez :

* [Installer Docker](https://docs.docker.com/engine/install/)
* [Installer Java](https://www.java.com/de/download/)

## Exécuter des applications isolées en utilisant Docker

> Docker élimine les tâches de configuration répétitives et fastidieuses et est utilisé tout au long du cycle de développement pour un développement d'applications rapide, facile et portable – sur desktop et cloud. (Source : [https://www.docker.com/use-cases/](https://www.docker.com/use-cases/))

Le cœur du superpouvoir de Docker est l'utilisation de ce qu'on appelle des [cgroups](https://en.wikipedia.org/wiki/Cgroups) pour créer des environnements légers, isolés, portables et performants, que vous pouvez démarrer en quelques secondes.

Voyons comment vous pouvez utiliser Docker pour être plus productif.

## Conteneurs de base de données

En utilisant Docker, vous pouvez démarrer de nombreux types de bases de données en quelques secondes. C'est facile, et cela ne pollue pas votre système local avec d'autres exigences nécessaires pour exécuter la base de données. Tout est fourni avec le conteneur Docker.

En recherchant sur [hub.docker.com](https://hub.docker.com/), vous pouvez trouver des conteneurs prêts à l'emploi pour de nombreuses bases de données.

En utilisant la commande `docker run`, vous pouvez démarrer un [conteneur Docker MySQL](https://hub.docker.com/_/mysql/).

```sh
docker run --rm -v "$PWD/data":/var/lib/mysql --name mysql -e MYSQL_ROOT_PASSWORD=admin-password -e MYSQL_DATABASE=my-database -p 3306:3306 mysql:8.0.28-debian
```

Cette commande utilise des fonctionnalités avancées pour exécuter un conteneur Docker :

* `-v "$PWD/data"` mappe votre répertoire local `./data` vers le conteneur Docker, ce qui vous permet de démarrer le conteneur Docker sans perdre vos données,
* `-p 3306:3306` mappe le port du conteneur `3306` vers notre machine afin que d'autres applications puissent l'utiliser,
* `-e MYSQL_DATABASE=my-database` définit une variable d'environnement pour créer automatiquement une nouvelle base de données appelée `my-database`,
* `-e MYSQL_ROOT_PASSWORD=admin-password` définit une variable d'environnement pour définir le mot de passe administrateur,
* `--rm` supprime le conteneur lorsqu'il est arrêté.

Ces variables d'environnement et bien d'autres sont documentées sur la [page de l'image Docker](https://hub.docker.com/_/mysql/?tab=description).

### Comment utiliser les conteneurs de base de données pour le développement

Vous utiliserez une stack technique populaire pour construire une application web basée sur [Java](https://www.w3schools.com/java/java_intro.asp) et [Spring Boot](https://spring.io/projects/spring-boot). Pour vous concentrer sur les parties Docker, vous pouvez cloner une simple application de démonstration à partir du guide officiel [Accéder aux données JPA avec Rest](https://spring.io/guides/gs/accessing-data-rest/).

```sh
# Télécharger l'application d'exemple
git clone https://github.com/spring-guides/gs-accessing-data-rest.git

# Ouvrir le dossier de l'application finale
cd complete
```

L'application est livrée avec une base de données en mémoire, qui n'est pas adaptée à la production car elle ne permet pas à plusieurs services d'accéder et de modifier une seule base de données. Une base de données [MySQL](https://www.mysql.com/) est plus adaptée pour scaling votre application à beaucoup plus de lectures et d'écritures.

Par conséquent, ajoutez le pilote MySQL à votre `pom.xml` :

```xml
       <!-- Désactiver la base de données en mémoire -->
       <!--
       <dependency>
           <groupId>com.h2database</groupId>
           <artifactId>h2</artifactId>
           <scope>runtime</scope>
       </dependency>
       -->
 
       <!-- Pilote MySQL -->
       <dependency>
           <groupId>mysql</groupId>
           <artifactId>mysql-connector-java</artifactId>
           <scope>runtime</scope>
       </dependency>

```

Maintenant, vous devez ajouter la configuration pour vous connecter à votre base de données en ajoutant un fichier de configuration `src/main/resources/application.properties`.

```properties
# Configuration de la base de données
spring.datasource.url=jdbc:mysql://localhost:3306/my-database
spring.datasource.username=root
spring.datasource.password=admin-password
 
# Créer une table et une base de données automatiquement
spring.jpa.hibernate.ddl-auto=update
```

Vous pouvez maintenant démarrer l'application et appeler les endpoints existants :

```sh
# Obtenir toutes les personnes
curl http://localhost:8080/people

# Ajouter une personne
curl -i -H "Content-Type:application/json" -d '{"firstName": "Frodo", "lastName": "Baggins"}' http://localhost:8080/people

# Obtenir toutes les personnes à nouveau, ce qui retourne maintenant la personne créée
curl http://localhost:8080/people
```

Vous avez utilisé avec succès votre application rudimentaire, qui écrit et lit des données dans votre base de données. L'utilisation de la base de données Docker MySQL vous donne une base de données robuste en quelques secondes, et vous pouvez l'utiliser à partir de n'importe quelle application.

### Comment utiliser les conteneurs de base de données pour les tests d'intégration

L'application dispose déjà de tests qui nécessitent une base de données en cours d'exécution. Mais, parce que vous avez remplacé votre base de données en mémoire par une base de données MySQL réelle, les tests ne s'exécuteront pas avec succès si vous arrêtez votre base de données.

```sh
# Arrêter la base de données
docker rm -f mysql

# Exécuter les tests
./mvnw clean test

... sortie ignorée ...
[ERROR] Tests run: 7, Failures: 0, Errors: 7, Skipped: 0
... sortie ignorée ...
```

Pour démarrer et arrêter rapidement les conteneurs lors de l'exécution des tests, il existe un outil pratique appelé [testcontainers](https://github.com/testcontainers). Vous y trouverez des bibliothèques pour de nombreux langages de programmation, y compris Java.

Tout d'abord, vous devez ajouter quelques dépendances à votre `pom.xml` :

```xml
       <!-- testcontainer -->
       <dependency>
           <groupId>org.testcontainers</groupId>
           <artifactId>testcontainers</artifactId>
           <version>1.16.3</version>
           <scope>test</scope>
       </dependency>
       <dependency>
           <groupId>org.testcontainers</groupId>
           <artifactId>mysql</artifactId>
           <version>1.16.3</version>
           <scope>test</scope>
       </dependency>
       <dependency>
           <groupId>org.testcontainers</groupId>
           <artifactId>junit-jupiter</artifactId>
           <version>1.16.3</version>
           <scope>test</scope>
       </dependency>

```

Vous devez mettre à jour les tests pour utiliser les testcontainers, qui démarrent la base de données à chaque exécution de test. Ajoutez une annotation et un champ au test pour l'utiliser :

```java
//imports ajoutés
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.DynamicPropertyRegistry;
import org.springframework.test.context.DynamicPropertySource;
import org.testcontainers.containers.MySQLContainer;
import org.testcontainers.junit.jupiter.Container;
import org.testcontainers.junit.jupiter.Testcontainers;
 
@SpringBootTest
@AutoConfigureMockMvc
@Testcontainers // Annotation pour activer testcontainers
public class AccessingDataRestApplicationTests {
 
   // Champ pour accéder à la base de données démarrée
   @Container
   private static MySQLContainer database = new MySQLContainer<>("mysql:5.7.34");
 
   //Définir la configuration de la base de données en utilisant la base de données démarrée
   @DynamicPropertySource
   static void databaseProperties(DynamicPropertyRegistry registry) {
       registry.add("spring.datasource.url", database::getJdbcUrl);
       registry.add("spring.datasource.username", database::getUsername);
       registry.add("spring.datasource.password", database::getPassword);
   }

```

Pour chaque exécution de test, la base de données est démarrée pour vous, ce qui vous permet d'utiliser une base de données réelle lorsque vous exécutez des tests. Tout le câblage, la configuration, le démarrage et le nettoyage sont effectués pour vous.

## Dockeriser votre application

Dockeriser votre application en utilisant des outils Docker simples est possible mais non recommandé.

Vous pouvez construire votre application, utiliser un conteneur de base qui contient Java et copier et exécuter votre application. Mais il y a beaucoup de pièges, et c'est le cas pour chaque langage et framework. Donc, cherchez toujours des outils qui facilitent votre vie.

Dans cet exemple, vous utiliserez [Jib](https://github.com/GoogleContainerTools/jib) et [distroless containers](https://github.com/GoogleContainerTools/distroless) pour construire facilement un conteneur Docker. L'utilisation des deux en combinaison vous donne un conteneur minimal, sécurisé et reproductible, qui fonctionne de la même manière localement et en production.

Pour utiliser Jib, vous devez l'ajouter en tant que plugin maven en l'ajoutant à votre `pom.xml` :

```xml
<build>
       <plugins>
           <plugin>
               <groupId>org.springframework.boot</groupId>
               <artifactId>spring-boot-maven-plugin</artifactId>
           </plugin>
 
        <!-- Plugin Jib -->
           <plugin>
               <groupId>com.google.cloud.tools</groupId>
               <artifactId>jib-maven-plugin</artifactId>
               <version>3.2.1</version>
               <configuration>
                   <from>
                       <image>gcr.io/distroless/java17:nonroot</image>
                   </from>
                   <to>
                       <image>my-docker-image</image>
                   </to>
               </configuration>
           </plugin>
       </plugins>
   </build>
```

Vous pouvez maintenant construire l'image et exécuter l'application :

```sh
# construire le conteneur docker
./mvnw compile jib:dockerBuild

# trouver votre image construite
docker images

# démarrer la base de données
docker run --rm -v "$PWD/data":/var/lib/mysql --name mysql -e MYSQL_ROOT_PASSWORD=admin-password -e MYSQL_DATABASE=my-database -p 3306:3306 mysql:8.0.28-debian


# démarrer le conteneur docker qui contient votre application
docker run --net=host my-docker-image

 sortie ignorée
2022-04-15 17:43:51.509  INFO 1 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port(s): 8080 (http) with context path ''
2022-04-15 17:43:51.521  INFO 1 --- [           main] c.e.a.AccessingDataRestApplication       : Started AccessingDataRestApplication in 6.146 seconds (JVM running for 6.568)
```

L'application est démarrée avec le mode réseau host `--net=host`, ce qui facilite la connexion à la base de données que vous avez démarrée. Alternativement, vous pouvez créer un `docker network` et démarrer les deux dans le même réseau.

Vous pouvez pousser votre conteneur vers un registre de conteneurs et le référencer à partir de n'importe quel outil d'orchestration de conteneurs pour exécuter votre application en production.

## Résumé

Dans ce tutoriel, vous avez appris comment tirer parti de Docker pour créer, tester et exécuter des applications sans polluer votre système.

Tout est dans votre environnement Docker isolé et fonctionne localement, ainsi que sur les systèmes d'intégration continue et les systèmes de production où vous pouvez démarrer des centaines de vos applications.

Vous trouverez l'application d'exemple prête à l'emploi dans [mon dépôt GitHub Docker For Development Example Application Repository](https://github.com/sesigl/docker-for-development-example-application).

J'espère que vous avez apprécié l'article.

Si vous l'avez aimé et que vous avez envie de m'applaudir ou simplement de prendre contact, [suivez-moi sur Twitter](https://twitter.com/sesigl).

Je travaille chez eBay Kleinanzeigen, l'une des plus grandes entreprises de petites annonces au monde. Au fait, [nous recrutons](https://www.ebay-kleinanzeigen.de/careers) !

## Références

* [Docker Hub : Image MySQL](https://hub.docker.com/_/mysql/)
* [Documentation Docker : commande run](https://docs.docker.com/engine/reference/commandline/run/)
* [Visual Studio Code : Dev Containers](https://code.visualstudio.com/docs/remote/containers)
* [Apprendre Java – cours de Java gratuits](https://www.freecodecamp.org/news/learn-java-free-java-courses-for-beginners/)
* [Youtube : Construire des conteneurs plus rapidement avec Jib](https://www.youtube.com/watch?v=H6gR_Cv4yWI)