---
title: Comment effectuer des tests de charge dans Spring Boot avec Gatling
subtitle: ''
author: Mario Casari
co_authors: []
series: null
date: '2024-07-08T19:46:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-integrate-spring-boot-with-gatling
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/pexels-markusspiske-177598.jpg
tags:
- name: Gatling
  slug: gatling
- name: Java
  slug: java
- name: spring-boot
  slug: spring-boot
seo_title: Comment effectuer des tests de charge dans Spring Boot avec Gatling
seo_desc: "To evaluate the performance of a system, you need a tool that can simulate\
  \ its behavior in production. \nFor this purpose, you can use a software tool based\
  \ on Scala called Gatling. This article will teach you how to integrate it into\
  \ a Spring Boot ap..."
---

Pour évaluer les performances d'un système, vous avez besoin d'un outil capable de simuler son comportement en production.

À cette fin, vous pouvez utiliser un outil logiciel basé sur [Scala](https://www.scala-lang.org/) appelé [Gatling](https://gatling.io/). Cet article vous apprendra à l'intégrer dans une application [Spring Boot](https://spring.io/projects/spring-boot) et à effectuer un test de charge.

## Concepts principaux

Gatling est un outil que vous pouvez utiliser pour exécuter des tests de charge et de performance. Il peut être utilisé comme une application autonome ou intégré dans un projet basé sur Maven ou Gradle.

Gatling est basé sur Scala, le framework [Netty](https://en.wikipedia.org/wiki/Netty_(software)) et l'outil [Akka](https://doc.akka.io/docs/akka/current/typed/guide/index.html). Il possède une architecture asynchrone et non bloquante, ce qui permet des performances élevées avec un minimum de gaspillage de ressources.

Vous pouvez définir des tests grâce au langage spécifique de domaine flexible de Gatling. Vous pouvez également utiliser sa fonction d'enregistrement avec une interface graphique pour capturer les interactions de l'utilisateur dans le navigateur et générer des scripts Scala qui peuvent être modifiés et lancés pour effectuer une simulation.

Dans cet article, vous apprendrez à intégrer Gatling dans une application web Spring Boot basée sur Maven. Vous définirez un test de charge par son DSL, puis vous l'exécuterez en utilisant le plugin Maven de Gatling.

Avec Gatling, vous pouvez effectuer des tests de performance de diverses manières. Par exemple, vous pouvez implémenter :

<ul><li><b>Test de charge</b> : pour voir comment un système se comporte sous une charge spécifique</li><li><b>Test de stress</b> : pour trouver le point de rupture d'un système, en augmentant progressivement la charge</li><li><b>Test de résistance</b> : exécuter le système avec une charge constante pendant une longue période pour trouver ses faiblesses</li><li><b>Test de pic</b> : pour voir comment le système se comporte lorsque la charge est rapidement augmentée à un pic puis redescend</li></ul>

Les composants de base avec lesquels Gatling implémente les fonctionnalités décrites ci-dessus sont :

<ul><li><b>Scénarios</b> : une série d'étapes effectuées par un utilisateur virtuel</li><li><b>Feeders</b> : comment les données sont fournies pour alimenter les scénarios</li><li><b>Injection</b> : une sorte de plan qui indique comment le test est effectué, en termes de nombre d'utilisateurs virtuels, comment ils changent dans le temps, etc.</li></ul>

## Intégration de Spring Boot avec Gatling

Dans cet article, vous allez commencer avec une simple application web Spring Boot et implémenter et exécuter un test de charge sur celle-ci. Vous pouvez trouver le code source de cette application exemple sur [GitHub](https://github.com/mcasari/codingstrain/tree/main/spring-cloud-sample-libraryapp/libraryapp-testing-gatling-test).

Imaginez que vous avez une bibliothèque et que vous souhaitez insérer de nouveaux livres par leur titre. Vous pouvez implémenter cette exigence minimale en utilisant JPA en définissant une entité Book, une classe de repository, une classe de service et un contrôleur avec un mapping de service [REST](https://codingstrain.com/spring-boot-for-cloud-rest-api-development/).

Le service REST est défini comme un appel POST à un endpoint /book qui sauvegarde un nouvel objet book. Vous pouvez voir l'implémentation dans le code ci-dessous :

```java
@RestController
@RequestMapping("/library")
public class BookController {

    Logger logger = LoggerFactory.getLogger(BookController.class);

    @Autowired
    BookService bookService;

    @PostMapping(value = "/book", consumes = "application/json", produces = "application/json")
    public Book createPerson(@RequestBody Book book) {
        return bookService.save(book);
    }

}
```

Pour effectuer un test de charge sur l'endpoint REST ci-dessus, vous devez intégrer Gatling. Vous pouvez le faire en définissant d'abord quelques dépendances Maven :

```xml
<dependency>
    <groupId>io.gatling</groupId>
    <artifactId>gatling-app</artifactId>
    <version>3.7.2</version>
</dependency>

			
<dependency>
    <groupId>io.gatling.highcharts</groupId>
    <artifactId>gatling-charts-highcharts</artifactId>
    <version>3.7.2</version>
</dependency>	

<dependency>
    <groupId>com.github.javafaker</groupId>
    <artifactId>javafaker</artifactId>
    <version>0.15</version>
</dependency>	
```

Ensuite, vous avez également besoin d'un plugin Maven pour exécuter le test :

```xml
<plugin>
    <groupId>io.gatling</groupId>
    <artifactId>gatling-maven-plugin</artifactId>
    <version>4.2.9</version>
    <configuration>
<simulationClass>com.codingstrain.springcloud.sample.libraryapp.books.BookSaveSimulation</simulationClass>
    </configuration>
</plugin>
```

## Implémentation du test de charge

Pour implémenter un test, vous devez étendre la classe `io.gatling.javaapi.core.Simulation`, comme dans la classe `BookSaveSimulation` ci-dessous :

```java
import static io.gatling.javaapi.core.CoreDsl.StringBody;
import static io.gatling.javaapi.core.CoreDsl.global;
import static io.gatling.javaapi.core.CoreDsl.rampUsersPerSec;
import static io.gatling.javaapi.http.HttpDsl.http;

import java.time.Duration;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.stream.Stream;

import com.github.javafaker.Faker;

import io.gatling.javaapi.core.CoreDsl;
import io.gatling.javaapi.core.OpenInjectionStep.RampRate.RampRateOpenInjectionStep;
import io.gatling.javaapi.core.ScenarioBuilder;
import io.gatling.javaapi.core.Simulation;
import io.gatling.javaapi.http.HttpDsl;
import io.gatling.javaapi.http.HttpProtocolBuilder;


public class BookSaveSimulation extends Simulation {


    public BookSaveSimulation() {

        setUp(buildPostScenario()
            .injectOpen(injection())
            .protocols(setupProtocol())).assertions(global().responseTime()
          .max()
          .lte(10000), global().successfulRequests()
          .percent()
          .gt(90d));
    }

    private static ScenarioBuilder buildPostScenario() {
        return CoreDsl.scenario("Load POST Test")
            .feed(feedData())
            .exec(http("create-book").post("/library/book")
            .header("Content-Type", "application/json")
                .body(StringBody("{ \"title\": \"${title}\" }")));
    }

    private static Iterator <Map<String, Object>> feedData() {
        Faker faker = new Faker();
        Iterator<Map<String, Object>> iterator;
        iterator = Stream.generate(() -> {
              Map<String, Object> stringObjectMap = new HashMap<>();
            stringObjectMap.put("title", faker.book()
                .title());
              return stringObjectMap;
          })
          .iterator();
        return iterator;
    }

    private static HttpProtocolBuilder setupProtocol() {
        return HttpDsl.http.baseUrl("http://localhost:8080")
          .acceptHeader("application/json")
          .maxConnectionsPerHost(10)
            .userAgentHeader("Performance Test");
    }

    private RampRateOpenInjectionStep injection() {
        int totalUsers = 100;
        double userRampUpPerInterval = 10;
        double rampUpIntervalInSeconds = 30;

        int rampUptimeSeconds = 300;
        int duration = 300;
        return rampUsersPerSec(userRampUpPerInterval / (rampUpIntervalInSeconds)).to(totalUsers)
            .during(Duration.ofSeconds(rampUptimeSeconds + duration));
    }
}
```

La classe `BoookSaveSimulation` utilise son constructeur pour effectuer tous les réglages en utilisant la méthode `setUp` de la classe parente. Elle implémente d'abord un scénario. Puisque le but du test est de simuler une situation réelle en production, le scénario représente les étapes effectuées par un nombre configuré d'utilisateurs virtuels interagissant avec le système.

Le scénario dans l'exemple exécute un appel POST à l'endpoint /library/book, envoyant un seul paramètre title dans la charge utile. Le service invoqué sauvegardera un nouveau livre par la valeur de titre passée. Une classe nommée `com.github.javafaker.Faker` produit automatiquement des valeurs de titre et implémente le composant feeder décrit précédemment dans la section `Concepts principaux`.

Ensuite, la méthode `injectOpen` définit comment les utilisateurs virtuels sont ajoutés à la simulation. La méthode injectOpen implémente la partie injection en utilisant le mode dit ouvert. Il existe deux modèles différents d'injection, `open` et `closed`.

Le modèle ouvert simule un scénario dans lequel de nouveaux utilisateurs peuvent être ajoutés constamment et indépendamment de l'état d'exécution des autres. C'est le modèle utilisé dans l'exemple de cet article. En revanche, dans le modèle fermé, de nouveaux utilisateurs ne peuvent être ajoutés que lorsque tous les autres ont terminé leurs tâches. Cela aide à simuler une charge constante sur le système.

La configuration d'injection ouverte dans l'exemple définit un nombre total de 100 utilisateurs qui sont ajoutés progressivement 10 à la fois, toutes les 30 secondes. Une fois que tous les utilisateurs ont été ajoutés, l'exécution continue pendant 300 secondes.

La méthode protocols configure l'URL de base, le type de données attendu dans la réponse, le nombre maximum de connexions par hôte et l'en-tête User-Agent.

La dernière partie de cette phase de configuration définit un couple d'assertions pour considérer le test réussi : un temps de réponse maximum inférieur à 10 secondes et un pourcentage de requêtes réussies supérieur à 90 %.

## Comment exécuter le test

Pour exécuter le test, vous devez d'abord démarrer l'application web Spring Boot. Vous pouvez le faire, par exemple, en allant dans le répertoire de base du projet et en exécutant la commande suivante : `mvn spring-boot:run`.

Une fois l'application démarrée, vous pouvez exécuter la simulation Gatling en exécutant `mvn gatling:test`.

## Comment voir les résultats

Une fois le test terminé, vous trouverez un fichier index.html dans le répertoire /target/gatling avec toutes les mesures et plusieurs graphiques.

La figure ci-dessous affiche tous les résultats. Elle montre une liste des assertions et leur résultat. Ensuite, vous pouvez voir le nombre total de requêtes, et combien de requêtes ont un résultat positif ou négatif. Vous avez des informations utiles sur le temps de réponse : minimum, maximum, moyenne et écart type, et vous avez également les 50e, 75e, 95e et 99e percentiles.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/Summary.png)
_Résumé des résultats du test_

Un graphique montre le nombre de requêtes, avec des résultats positifs et négatifs, dans une plage de temps de réponse particulière, comme dans la figure suivante.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/GlobalInfo.png)
_Nombre de requêtes dans des plages de temps de réponse particulières_

Un autre graphique montre le nombre de requêtes par seconde et comment il change en fonction du nombre d'utilisateurs actifs.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/RequestsPerSecond.png)
_Nombre de requêtes par seconde et utilisateurs actifs au fil du temps_

Vous pouvez également voir dans la figure suivante comment les percentiles changent au fil du temps, et avec le nombre d'utilisateurs actifs à chaque moment.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/Percentiles.png)

## Conclusion

Évaluer les performances d'un système est une tâche complexe. Gatling facilite suffisamment l'intégration de ce type de tâche avec l'intégration continue. Il vous donne une vue d'ensemble et vous permet d'ajuster les tests pour trouver les faiblesses et suggérer des solutions.