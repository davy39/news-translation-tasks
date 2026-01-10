---
title: 'Spring vs Spring Boot : Comment choisir le bon Framework Java'
subtitle: ''
author: Augustine Alul
co_authors: []
series: null
date: '2025-07-21T23:25:21.413Z'
originalURL: https://freecodecamp.org/news/spring-vs-spring-boot-choosing-a-java-framework
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1753140286088/7294bd87-8940-450f-aa05-cef68a1c2604.png
tags:
- name: Java
  slug: java
- name: Spring
  slug: spring
- name: Springboot
  slug: springboot
seo_title: 'Spring vs Spring Boot : Comment choisir le bon Framework Java'
seo_desc: 'The Java programming language is a favourite among solo devs and large
  teams alike. It’s popular for many reasons and use cases, including its mature ecosystem,
  stable support, efficiency, and reliability.

  If you’re learning Java with the end goal of...'
---

Le langage de programmation Java est un favori parmi les développeurs solo et les grandes équipes. Il est populaire pour de nombreuses raisons et cas d'utilisation, y compris son écosystème mature, son support stable, son efficacité et sa fiabilité.

Si vous apprenez Java avec l'objectif final de construire des applications, vous devrez être capable de choisir un framework Java approprié (une collection d'outils et de bibliothèques pré-construits nécessaires) pour faciliter le développement une fois que vous connaissez les fondamentaux.

Il existe de nombreux frameworks Java qui aident à accomplir différentes tâches, tels que Jakarta EE (anciennement Java EE, un framework de niveau entreprise, utilisé pour les applications à grande échelle), JSF (ou JavaServer Faces, un framework UI pour développer des interfaces web Java), Spring, Spring Boot, et d'autres.

Vous avez peut-être entendu parler de Spring et Spring Boot, car ils sont très populaires et couramment utilisés par les développeurs Java. Dans cet article, vous apprendrez :

* Ce que sont les frameworks Spring et Spring Boot.

* Leurs cas d'utilisation dans le monde réel et comment commencer à construire avec eux.

* Les différences clés entre Spring et Spring Boot.

## Prérequis

Pour comprendre pleinement le contenu de cet article, vous devez avoir une bonne connaissance pratique du langage de programmation Java, être familier avec le concept des API (**Interfaces de Programmation d'Applications**), et savoir comment utiliser les outils de construction de projets Java - en particulier Maven, car c'est l'outil de construction que nous utiliserons pour les exemples de code de cet article.

### Table des Matières

* [Qu'est-ce que le Framework Spring ?](#heading-qu-est-ce-que-le-framework-spring)

* [Qu'est-ce que le Framework Spring Boot ?](#heading-qu-est-ce-que-le-framework-spring-boot)

* [Différences Clés Entre Spring et Spring Boot](#heading-différences-clés-entre-spring-et-spring-boot)

* [Exemple Concret](#heading-exemple-concret)

* [Comment Choisir Entre Spring et Spring Boot](#heading-comment-choisir-entre-spring-et-spring-boot)

* [Conclusion](#heading-conclusion)

## Qu'est-ce que le Framework Spring ?

Spring est un framework utilisé pour construire des applications modernes de niveau entreprise. Il est principalement utilisé pour Java, mais il est également compatible avec les langages de programmation Kotlin et Groovy. Cela signifie que vous pouvez utiliser Kotlin et Groovy pour développer des applications dans Spring.

Spring fournit un paradigme clair que vous pouvez suivre pour construire et configurer des applications pour un déploiement facile sur toute plateforme de votre choix.

Au cœur du framework Spring se trouve son support d'infrastructure robuste. Il gère en interne la mise en œuvre de composants clés nécessaires à la sécurité et à la fonctionnalité globale des applications d'entreprise. Il le fait en utilisant des modules tels que :

* Spring JDBC

* Spring MVC

* Spring Security

* Spring AOP

* Spring ORM et

* Spring Test

Ces modules permettent aux développeurs de se concentrer sur la logique métier de l'application au lieu de s'inquiéter de la mise en œuvre ou de l'écriture du code pour les composants/modules à partir de zéro. Cela permet de gagner un temps de développement significatif.

### Pourquoi utiliser Spring ?

Spring effectue beaucoup de travail lourd en termes de réduction du code d'infrastructure excessif grâce à ses modules par rapport aux anciens frameworks Java. C'est l'une des raisons pour lesquelles il est si populaire.

Par exemple, en ce qui concerne la gestion des dépendances dans Spring, vous devez simplement définir la dépendance en utilisant l'annotation `@Bean` dans une classe de configuration, remplaçant l'ancienne approche consistant à ajouter la dépendance dans un fichier XML.

Spring ajoute ensuite le bean à un conteneur IoC (Inversion de Contrôle), et rend le bean disponible pour être utilisé pendant l'exécution, gérant également le cycle de vie et le câblage automatiquement.

Voici une simple illustration de code de la classe de configuration ci-dessous :

```java
@Configuration

public class AppConfig{

@Bean

public DataSource dataSource() {

    DriverManagerDataSource ds = new DriverManagerDataSource();

    ds.setUrl("jdbc:mysql://localhost:3306/mydb");

    ds.setUsername("user");

    ds.setPassword("pass");

    return ds;

    }


}
```

Voici la classe où la ressource/dépendance est utilisée :

```java
@Component

public class UserRepository {

private DataSource dataSource;

public UserRepository(DataSource dataSource){

        this.dataSource = dataSource;

}

    public void connectToDb() throws SQLException {

        Connection conn = dataSource.getConnection();

        System.out.println("Connected to DB via Spring!");

        conn.close();

    }

}
```

Ces extraits de code démontrent comment l'injection de dépendances est mise en œuvre en utilisant les annotations `@Bean` et `@Component` de Spring. Dans le code se trouve une classe de configuration et une deuxième classe où le `DataSource` est injecté et utilisé. Cela montre une approche simpliste de la gestion des dépendances dans Spring.

### Composants Clés du Framework Spring

Spring est composé de plusieurs composants, chacun servant des rôles distincts (comme montré dans l'image ci-dessous) :

![Image contenant les Composants d'Exécution du Framework Spring](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdVmXBnm1fS-t0pN7w-zAglYvKrx37zoEZ4HdeszACcU8Ig4PFs_mKlfU49SALDAtrWUE1bj8bZ6lnvDoc4SoM_VxH5Nerime9uuNlIc5S6picvT3ho6Jv8dEmFTv7zrOKFNVDMxg?key=Zq-Isk9ZAG_nIZ1YfHDMRfMs align="left")

Source de l'image [source](https://docs.spring.io/spring-framework/docs/3.2.x/spring-framework-reference/html/overview.html) | Vue d'ensemble du Framework Spring

Ces composants fournissent collectivement des fonctionnalités utiles qui font de Spring un framework robuste. Considérez-les comme des parties qui composent un tout. Laissez-moi expliquer brièvement chacun des composants et leurs divers rôles pour une compréhension facile.

#### Accès aux Données/Intégration :

Ce composant permet une interaction facile avec les bases de données et autres sources de données. Il contient plusieurs modules (JDBC, ORM, OXM, JMS et Gestion des Transactions), chacun effectuant des fonctions uniques.

Ces modules fournissent une abstraction fine pour des tâches comme l'exécution de requêtes SQL, l'intégration avec des frameworks ORM (par exemple, Hibernate), la gestion de la liaison de données XML, la messagerie, et la gestion des transactions, tout en travaillant dans une application basée sur Spring.

#### Web :

Le composant Web rend possible l'interaction entre le côté client (via une requête HTTP) et la logique métier principale dans une application Spring. Il se compose de quatre modules (Web, Web-Servlet, Web-Struts, et Web-Portlet), chacun servant une fonction spécifique :

* Le module **Web** permet la fonctionnalité de téléchargement de fichiers multipartites et l'initialisation du conteneur IoC.

* Le module **Web-Servlet** fournit une implémentation MVC (Modèle Vue Contrôleur) pour les applications web.

* Le module **Web-Struts** intègre Struts dans Spring en utilisant des classes de support.

* Le module **Web-Portlet** supporte l'implémentation MVC pour une utilisation dans un environnement de portlet.

#### AOP et Instrumentation :

AOP fournit l'implémentation qui permet d'assurer la séparation des "préoccupations transversales" dans votre application de la logique métier, conduisant à un code plus propre et plus organisé, exempt de désordre et de répétition.

Au lieu d'écrire ces **préoccupations** partout dans vos classes, vous les définissez simplement dans des **aspects** et ils sont injectés pour vous par Spring lorsque le programme en a besoin. Ces **préoccupations** pourraient être la journalisation, la sécurité ou les transactions.

#### Instrumentation :

Cela permet le support d'instrumentation de classe, qui assure la modification du bytecode de classe.

#### Conteneur Principal :

Le Conteneur Principal, comme son nom l'indique, est une partie cruciale de Spring. Il est responsable de certaines des fonctionnalités uniques qui rendent le Framework Spring souhaité et populaire : IoC (Inversion de Contrôle) et injection de dépendances.

Le Conteneur Principal est composé des modules Beans, Core, Context et Expression Language. Ces modules ont tous des propriétés uniques, mais complémentaires.

#### Test :

Le composant Test fournit une approche appropriée pour tester les applications Spring, et il s'intègre parfaitement avec JUnit ou TestNG. Il va jusqu'à fournir des objets mock que vous pouvez utiliser pour tester différents composants de votre application dans un environnement isolé ou géré par Spring, vous aidant à obtenir une application logicielle robuste et fiable.

## Qu'est-ce que le Framework Spring Boot ?

Spring Boot est un framework open-source construit sur Spring pour développer des applications autonomes robustes que vous pouvez "facilement exécuter". Le but principal pour lequel Spring Boot a été créé était de simplifier davantage le processus de configuration et d'exécution des applications Spring.

Spring Boot impose une approche opinionnée du développement et fournit des fonctionnalités utiles supplémentaires non contenues dans Spring. Apprenons un peu plus sur son fonctionnement.

### Fonctionnalités Clés du Framework Spring Boot

Spring Boot, faisant partie de l'écosystème Spring, hérite de la plupart des fonctionnalités de Spring, mais contient des fonctionnalités supplémentaires non incluses dans Spring. Laissez-moi expliquer brièvement ces fonctionnalités uniques :

#### Auto-configuration

Spring Boot configure automatiquement les dépendances présentes dans le classpath (emplacement où l'environnement d'exécution Java recherche les classes/ressources pendant la compilation) via l'annotation `@SpringBootApplication`. Il s'agit d'une combinaison de `@EnableAutoConfiguration`, `@Configuration`, et `@ComponentScan`. Cette auto-configuration économise des efforts dans l'écriture de code boilerplate pour configurer les dépendances/beans (comme vous devez le faire avec Spring).

Voici comment vous pouvez utiliser l'annotation `@SpringBootApplication` pour l'auto-configuration dans les applications Spring Boot :

```java
    @SpringBootApplication

public class MyApp {

    public static void main(String[] args) {

        SpringApplication.run(MyApp.class, args);

    }

}
```

#### Dépendances de démarrage

Les dépendances de démarrage fournissent une manière plus propre et moins verbeuse de gérer les dépendances dans Spring Boot. Essentiellement, elles regroupent un ensemble de dépendances complémentaires qui effectuent une tâche commune en une seule, ce qui signifie que vous n'avez pas besoin de déclarer manuellement chaque dépendance qui fait partie du bundle de démarrage.

Les dépendances de démarrage dans Spring Boot suivent la convention de nommage spring-boot-starter-\*, où l'astérisque représente le nom de la dépendance particulière.

Voici quelques dépendances de démarrage courantes dans Spring Boot :

* spring-boot-starter-web

* spring-boot-starter-aop

* spring-boot-starter-data-jdbc

* spring-boot-starter-data-jpa

* spring-boot-starter-data-rest

#### Actuator

Actuator est un module dans le framework Spring Boot qui vous permet de surveiller les applications Spring Boot après/pendant le développement. Il fournit des endpoints intégrés et personnalisables que vous pouvez utiliser pour les vérifications de santé des applications, les métriques et les diagnostics.

Voici quelques-uns des endpoints couramment utilisés :

* /actuator/health : Fournit l'état de santé.

* /actuator/metrics : Affiche diverses métriques de l'application.

* /actuator/info : Affiche les informations générales de l'application.

* /actuator/env : Expose les propriétés de l'environnement.

* /actuator/beans : Liste tous les beans Spring.

* /actuator/threaddump : Effectue un dump des threads.

* /actuator/shutdown : Permet un arrêt progressif (désactivé par défaut).

#### Outil en ligne de commande

L'outil en ligne de commande Spring Boot est une interface qui vous aide à développer et tester rapidement vos applications Spring Boot. Il contient des commandes que vous pouvez utiliser pour :

* Exécuter des applications Spring Boot directement depuis le terminal (spring run).

* Gérer les dépendances et versions de l'application

* Initialiser un nouveau projet Spring Boot

* Compiler et tester des scripts Java/Groovy.

#### Configuration supplémentaire (via les fichiers application.properties et application.yml)

Les fichiers `application.properties` et `application.yml` sont deux formats que vous pouvez utiliser pour configurer les paramètres de votre application Spring Boot. Ils sont respectivement au format clé-valeur et YAML. Ils vous permettent de configurer les ports, la source de données, la journalisation, la mise en cache, etc.

```plaintext
    server.port=8081
 spring.datasource.url=jdbc:mysql://localhost:3306/mydb

spring.datasource.username=root

spring.datasource.password=secret

logging.level.org.springframework=DEBUG
```

Ceci est un exemple de fichier `application.properties` pour un projet Spring Boot. Vous pouvez voir que le port, la source de données et les informations d'identification de journalisation ont été configurés.

#### Serveur Web Intégré

Spring Boot est livré avec des serveurs web intégrés (Tomcat, Jetty et Undertow) qui sont utilisés pour servir facilement des applications Spring Boot compilées sous forme de fichiers jar sans avoir besoin de les déployer sur un serveur web externe dédié. Cela simplifie le déploiement, surtout dans une architecture de microservices et des environnements conteneurisés, car les applications peuvent être facilement exécutées en utilisant la commande :

```java
java -jar my-springboot-app.jar
```

Notez que Spring Boot ne peut pas exister sans Spring (mais Spring peut exister sans Jakarta EE et autres frameworks Java hérités créés avant lui). Spring Boot fait partie de la plateforme Spring. C'est comme le glaçage supplémentaire sur le gâteau qui le rend plus sucré.

Bien sûr, vous pouvez toujours avoir votre gâteau sans le glaçage. Techniquement, vous pouvez dire que Spring Boot est une couche supplémentaire qui a encore besoin de Spring pour fonctionner comme son infrastructure sous-jacente.

## Différences Clés Entre Spring et Spring Boot

Vous devriez maintenant être familier avec les fondamentaux des frameworks Spring et Spring Boot. Parlons donc un peu plus de leurs différences, en examinant leurs forces et leurs faiblesses.

### Configuration

La configuration dans Spring est plus fastidieuse par rapport à Spring Boot, car vous devrez ajouter manuellement les configurations pour votre projet dans Spring. Cela nécessite plus de code pour configurer les différents composants dont vous avez besoin pour un projet.

En revanche, la configuration dans Spring Boot est plus facile car vous pouvez utiliser le [site web Spring Initializr](https://start.spring.io/). Là, vous devez simplement sélectionner les dépendances pour le projet, ajouter un peu plus de configuration, puis télécharger le fichier zip qui contient la configuration pour le projet. Cela nécessite des étapes minimales, ce qui améliore votre productivité et rend la courbe d'apprentissage plus facile.

### Serveur Externe et Déploiement

Spring nécessite que vous déployiez vos applications sur un serveur externe comme Tomcat sous forme de fichier WAR (**Web Application Archive** ou **Web Application Resource**).

Spring Boot, en revanche, est livré avec un serveur intégré comme Tomcat, que vous pouvez utiliser pour exécuter/déployer des applications autonomes exécutables sous forme de fichiers JAR (ou **Java ARchive**). C'est pourquoi Spring Boot est fortement préféré pour le développement de microservices, car il est relativement facile de construire des applications et de les exécuter.

### Niveau de Contrôle

Spring et Spring Boot utilisent tous deux le paradigme Inversion de Contrôle (ou IoC) pour gérer les dépendances. Spring vous donne plus de contrôle sur l'application car vous avez la flexibilité d'initier les configurations selon les besoins. Mais Spring Boot gère davantage la gestion de l'application en interne, vous laissant peu de place pour contrôler la configuration de l'application, car il génère automatiquement des configurations qui peuvent ne pas être nécessaires pour un projet particulier. Cela peut conduire à un code redondant.

### Adéquation pour le Développement

Spring, comme Java EE, est préféré pour les applications d'entreprise à grande échelle en raison de son contrôle de configuration fin qui est inestimable, surtout pour les applications complexes et critiques en termes de performance comme la banque, la santé et le commerce électronique. Il offre une grande flexibilité, ce qui le rend adapté à l'intégration avec les composants Java EE et d'autres technologies et systèmes hérités de niveau entreprise.

Spring Boot n'est pas un choix courant pour les applications monolithiques à grande échelle, même s'il peut être utilisé dans ces cas. Il est plus adapté pour développer des applications autonomes ou des microservices où le développement rapide avec un support de serveur intégré est prioritaire par rapport à la configuration et au contrôle granulaires.

### Fonctionnalités Prêtes pour la Production

Dans Spring, un effort supplémentaire est nécessaire pour configurer manuellement les vérifications de santé, les métriques et la surveillance de votre application. Alors que Spring Boot est livré avec l'**actuator**, qui est un outil intégré utile pour les métriques, la surveillance des applications et pour effectuer des vérifications de santé. Vous devez simplement ajouter cette dépendance à votre fichier **pom.xml**

```xml
<dependency>

        <groupId>org.springframework.boot</groupId>

        <artifactId>spring-boot-starter-actuator</artifactId>

</dependency>
```

Après cela, vous pouvez surveiller votre application en visitant l'endpoint actuator souhaité qui expose les informations nécessaires. Trouvez une liste des endpoints actuator courants que vous pouvez visiter sous la sous-section **Actuator** de la section **Qu'est-ce que Spring Boot** ci-dessus.

## Exemple Concret

Examinons un exemple de construction d'un endpoint d'API REST simple dans les frameworks Spring et Spring Boot :

### Construction avec le Framework Spring

Dans cet exemple d'API, les technologies/dépendances que nous utiliserons sont :

* Java (Langage de Programmation)

* Maven (l'outil de construction pour le projet)

* Tomcat (conteneur de servlets)

* Système d'Exploitation (Mac/Linux/Windows)

* Framework Spring principal avec le module Spring MVC

* Jackson Databind : pour la sérialisation JSON

Notez que nous utiliserons Maven ici comme notre outil de construction (et pour l'exemple Spring Boot qui suit également) en raison de sa simplicité et de sa convivialité pour les débutants.

#### Étape 1 : Créer le fichier AppConfig.java

Il s'agit de la classe de configuration qui définit les propriétés de Spring MVC via l'annotation `@EnableWebMvc`, recherche les contrôleurs dans leurs packages via l'annotation `@ComponentScan`, et configure automatiquement d'autres valeurs par défaut nécessaires.

```java
@Configuration

@EnableWebMvc

@ComponentScan(basePackages = "com.example.controller")

public class AppConfig implements WebMvcConfigurer {

}
```

#### Étape 2 : Créer WebAppInitializer.java

Il s'agit de la classe qui remplace `web.xml` (qui était utilisé dans les anciennes versions). Elle crée le contexte d'application Spring et se connecte au fichier `AppConfig` pour la configuration.

```java
public class WebAppInitializer implements WebApplicationInitializer {
  @Override
  public void onStartup(ServletContext servletContext) {

    // Créer un contexte web basé sur les annotations

    AnnotationConfigWebApplicationContext context =

        new AnnotationConfigWebApplicationContext();

    context.register(AppConfig.class);

    // Enregistrer DispatcherServlet

    DispatcherServlet servlet = new DispatcherServlet(context);

    ServletRegistration.Dynamic registration =

        servletContext.addServlet("dispatcher", servlet);

    registration.setLoadOnStartup(1);

    registration.addMapping("/");

  }

}

```

#### Étape 3 : Ajouter la logique du **contrôleur**

Créez un fichier `HelloController.java` et ajoutez la logique du contrôleur. Il reçoit une requête **GET** et retourne "Hello from Spring Framework!"

```java
@RestController // Combine @Controller + @ResponseBody

public class HelloController {

    @GetMapping("/hello")

    public String hello() {

        return "Hello from Spring Framework!";

    }

}
```

#### Étape 4 : Ajouter les Dépendances

Incluez toutes les dépendances pour le projet dans un fichier **pom.xml**, puisque nous utilisons Maven comme outil de construction.

```xml
<dependency>

    <groupId>org.springframework</groupId>

    <artifactId>spring-webmvc</artifactId>

    <version>6.1.6</version> <!-- Dernière version Spring 6.x -->

</dependency>

<dependency>

    <groupId>com.fasterxml.jackson.core</groupId>

    <artifactId>jackson-databind</artifactId>

    <version>2.17.0</version> <!-- Pour le support JSON -->

</dependency>
```

#### Étape 5 : Construire et Déployer l'API

Enfin, vous devez construire l'application en un fichier WAR (Web Archive) et la déployer sur un conteneur de servlets (comme Tomcat, Jetty, ou celui qui est approprié) avant que l'application ne soit accessible.

Suivez les étapes données ci-dessous pour déployer sur un serveur Tomcat :

1. #### Emballer l'application en un fichier WAR

Si Maven est votre outil de construction pour le projet, ajoutez ce code de configuration à votre fichier Pom.xml :

`<packaging>war</packaging>`

Ensuite, construisez en utilisant la commande :

`./mvnw clean package`

Après cela, votre fichier WAR sera créé et stocké dans `target/yourapp.war`

2. #### Déployer votre fichier WAR sur un conteneur de servlets (dans ce cas, Tomcat)

À ce stade, vous pouvez choisir de déployer votre fichier WAR sur un conteneur de servlets distant ou local sur votre machine. Déployons sur un conteneur de servlets local puisque vous pouvez facilement pratiquer cela par vous-même.

* Téléchargez et installez Apache Tomcat depuis le site officiel https://tomcat.apache.org/

* Entrez dans le répertoire **webapps** en entrant la commande **cd path-to-tomcat/webapps/**

* Copiez votre fichier WAR dans le dossier

    `cp /path-to-your/target/yourapp.war`

* Démarrez le serveur web Tomcat.

Sur Linux/Mac OS, exécutez :

`./bin/startup.sh`

Sur Windows, faites :

`startup.bat`.

Vous devriez voir un lien similaire à celui-ci dans votre fenêtre de terminal :

`http://localhost:8080/yourapp`

Allez-y et cliquez dessus. Et voilà !

### Construction avec le Framework Spring Boot

Les différentes technologies de l'exemple Spring que j'utiliserai sont simplement le serveur Tomcat intégré au lieu du conteneur de servlets Tomcat. Et ici, bien sûr, nous utiliserons Spring Boot comme framework de développement au lieu de Spring.

Dans Spring Boot, vous pouvez soit aller directement dans votre IDE et commencer à créer les fichiers et configurations nécessaires pour votre projet, soit choisir d'utiliser le [Spring initializr](https://start.spring.io/) pour sélectionner les dépendances et générer les fichiers de base et les configurations pour votre projet. La deuxième option est préférée car elle est moins fastidieuse.

#### Étape 1 : Choisir les Dépendances Nécessaires pour Votre Projet et Télécharger le Fichier Zip

Ouvrez le site [Spring initializr](https://start.spring.io/), choisissez le projet comme Maven, le langage comme Java, et remplissez les métadonnées du projet. Pour ce projet, remplissez l'Artifact comme Hello.

![Image montrant comment remplir correctement les métadonnées pour un projet Spring Boot à partir du site web Spring initializer](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe41zF3IjWT8f8yW1kNlD4in3jhPev8DAm6lrIXf1anqZiZnCQtHfEavLP1u0DxMJ-h8crZVfsVcAdrEYxFHxuGmHF5PyjOEblTJEEL5vKx3XY1LYYbwY3CSyZAUfD7yv4nNpud7g?key=Zq-Isk9ZAG_nIZ1YfHDMRfMs align="left")

Choisissez jar pour l'emballage, puis sélectionnez les dépendances pour le projet. Pour cet article, nous utiliserons uniquement Spring Web. Ensuite, cliquez sur le bouton générer.

![Image montrant comment choisir les dépendances pour un projet Spring Boot à partir du site web Spring Initializer](https://lh7-rt.googleusercontent.com/docsz/AD_4nXc_5puGjgNKRvgAp4MrC_J_8o4ZMmJ4ozms6WDCJbsboF5oC7YarspzS65qXfFfSZtSkPJxLEcY11Or64irPvWnkmz9A0vxIh5BdFMJw_7lISxBqPyU78Uxa-s23AlbXKWIYIPLHw?key=Zq-Isk9ZAG_nIZ1YfHDMRfMs align="left")

![Image montrant comment générer et télécharger les fichiers contenant la configuration et les dépendances pour le projet Spring Boot](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcAi17ltnglcLuD6iDy0MLb6j2ANa4ssJKD6WdaPyQ0RERpOazdOcBfTWwFxix6U2Om9UPOxH-qy3k5gm6BbFTBdGf0PR9KH3EQvWfYucfpFBMM2EKb5DfMB8jcdj0xqYHfYbvOfg?key=Zq-Isk9ZAG_nIZ1YfHDMRfMs align="left")

Cela télécharge un fichier zip sur votre machine contenant le code boilerplate avec lequel vous pouvez construire votre application.

#### Étape 2 : Créer le **Contrôleur (HelloController.java)**

Décompressez le fichier téléchargé de l'étape 1, et ouvrez-le dans votre IDE préféré (ou Environnement de Développement Intégré). Naviguez jusqu'au répertoire Hello/src/main/java/com/example/Hello, où vous devriez déjà avoir le fichier HelloApplication.java, et ajoutez le fichier HelloController.java :

```java
@RestController

public class HelloController {

    @GetMapping("/hello")

    public String hello() {

        return "Hello from Spring Boot!";

    }

}
```

#### Étape 3 : Construire et exécuter l'application

Sur votre terminal, exécutez les commandes suivantes : `mvn clean package && java -jar target/your-app.jar`. Vous pouvez ensuite accéder à l'endpoint sur http://localhost:8080/hello. Lorsque vous cliquez sur le lien, vous devriez voir `Hello from Spring Boot!` sur votre écran.

## Comment Choisir Entre Spring et Spring Boot

Spring et Spring Boot sont tous deux des frameworks Java populaires pour construire des solutions logicielles robustes. Et comme vous l'avez appris dans la première partie de ce tutoriel, ils ont de nombreuses caractéristiques communes (puisque Spring Boot est construit sur Spring).

Mais il y a quelques domaines clés où ils diffèrent. Le premier est le format de leurs fichiers empaquetés : Spring est empaqueté en WAR, et Spring Boot en JAR. De plus, Spring Boot est livré avec un serveur web intégré alors que Spring nécessite un conteneur de servlets externe.

Le serveur web intégré qui accompagne Spring Boot facilite l'exécution des applications Spring Boot pendant le développement et en production sans avoir besoin d'un conteneur de servlets externe. Pendant ce temps, Spring traditionnel nécessite que les développeurs déployent sur un conteneur de servlets externe. Cela rend Spring Boot adapté au développement et au déploiement rapides d'applications autonomes ou de microservices, car il permet non seulement de gagner du temps, mais aussi de réduire la complexité de la configuration et les exigences d'infrastructure.

De plus, la configuration fine de Spring et sa facilité d'intégration avec les systèmes et outils hérités en font le choix souhaité pour le développement d'applications d'entreprise hautement personnalisables. Ce n'est pas le cas de Spring Boot, qui repose sur la philosophie de la convention sur la configuration, fournissant une auto-configuration pour réduire le temps de développement.

## Conclusion

La construction d'applications d'entreprise et de microservices avec Java est beaucoup plus facile en utilisant les frameworks Spring et Spring Boot.

Dans cet article, vous avez appris comment ces deux frameworks fonctionnent, ainsi que leurs points forts et leurs inconvénients.

Cet article n'a pas pour but de favoriser un framework par rapport à l'autre, mais plutôt de montrer en détail comment ils diffèrent et leurs caractéristiques uniques.

**Mais pour résumer :**

* Utilisez Spring lorsque vous construisez des systèmes d'entreprise hautement personnalisés intégrés à des systèmes hérités.

* Utilisez Spring Boot pour les API REST, les microservices ou les applications natives du cloud.

La prochaine fois que vous serez confronté à un projet nécessitant de choisir un framework similaire, il est impératif de peser soigneusement vos choix et de sélectionner le framework qui correspond le mieux à votre tâche. Bon codage !

### Références

1. [Documentation Officielle du Framework Spring](https://spring.io/projects/spring-framework/)

2. [Baeldung – Introduction au Framework Spring](https://docs.spring.io/spring-framework/docs/3.2.x/spring-framework-reference/html/overview.html)

3. [Ellow. Spring vs Spring Boot : Une Comparaison Approfondie](https://ellow.io/spring-vs-spring-boot/)