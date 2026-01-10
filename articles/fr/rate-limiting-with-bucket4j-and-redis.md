---
title: Comment créer un Rate Limiter avec Bucket4J et Redis
subtitle: ''
author: Abhinav Pandey
co_authors: []
series: null
date: '2022-04-01T19:05:04.000Z'
originalURL: https://freecodecamp.org/news/rate-limiting-with-bucket4j-and-redis
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/Rate-Limiter-with-Bucket4J-and-Redis.png
tags:
- name: api
  slug: api
- name: Redis
  slug: redis
- name: Web Security
  slug: web-security
seo_title: Comment créer un Rate Limiter avec Bucket4J et Redis
seo_desc: 'In this tutorial we will learn how to implement rate limiting in a scaled
  service.We will use the Bucket4J library to implement it and we will use Redis as
  a distributed cache.

  Why Use Rate Limiting?

  Let''s get started with some basics to make sure we...'
---

Dans ce tutoriel, nous allons apprendre à implémenter la limitation de débit (rate limiting) dans un service mis à l'échelle.
Nous utiliserons la bibliothèque [Bucket4J](https://github.com/vladimir-bukhtoyarov/bucket4j) pour l'implémenter et nous utiliserons [Redis](https://redis.io/) comme cache distribué.

## Pourquoi utiliser la limitation de débit ?

Commençons par quelques bases pour nous assurer de bien comprendre la nécessité de la limitation de débit et présentons les outils que nous utiliserons dans ce tutoriel.

### Problème avec les débits illimités

Si une API publique comme l'API Twitter permettait à ses utilisateurs d'effectuer un nombre illimité de requêtes par heure, cela pourrait entraîner :

* un épuisement des ressources
* une baisse de la qualité du service
* des attaques par déni de service

Cela pourrait aboutir à une situation où le **service est indisponible ou lent**. Cela pourrait également entraîner des **coûts imprévus** plus élevés pour le service.

### Comment la limitation de débit aide

Premièrement, la limitation de débit peut prévenir les attaques par déni de service. Couplée à un mécanisme de déduplication ou à des clés d'API, la limitation de débit peut également aider à prévenir les attaques par déni de service distribué (DDoS).

Deuxièmement, elle aide à estimer le trafic. C'est très important pour les API publiques. Cela peut également être couplé à des scripts automatisés pour surveiller et mettre à l'échelle le service.

Et troisièmement, vous pouvez l'utiliser pour implémenter une tarification par paliers. Ce type de modèle de tarification signifie que les utilisateurs peuvent payer pour un débit de requêtes plus élevé. L'API Twitter en est un exemple.

### L'algorithme Token Bucket

Le Token Bucket (panier de jetons) est un algorithme que vous pouvez utiliser pour implémenter la limitation de débit. En bref, il fonctionne comme suit :

1. Un seau (bucket) est créé avec une certaine capacité (nombre de jetons).
2. Lorsqu'une requête arrive, le seau est vérifié. S'il y a assez de capacité, la requête est autorisée à continuer. Sinon, la requête est refusée.
3. Lorsqu'une requête est autorisée, la capacité est réduite.
4. Après un certain laps de temps, la capacité est reconstituée.

### Comment implémenter le Token Bucket dans un système distribué

Pour implémenter l'algorithme Token Bucket dans un système distribué, nous devons utiliser un **cache distribué**.

Le cache est un **magasin clé-valeur** permettant de stocker les informations du seau. Nous utiliserons un cache Redis pour implémenter cela.

En interne, Bucket4j nous permet de brancher n'importe quelle implémentation de l'API Java JCache. Le client [Redisson](https://redisson.org/) de Redis est l'implémentation que nous utiliserons.

## Implémentation du projet

Nous utiliserons le Framework [Spring Boot](https://spring.io/projects/spring-boot) pour construire notre service.

Notre service contiendra les composants ci-dessous :

1. Une API REST simple.
2. Un cache Redis connecté au service – en utilisant le client Redisson.
3. La bibliothèque Bucket4J enveloppant l'API REST.
4. Nous connecterons Bucket4J à l'interface JCache qui utilisera le client Redisson comme implémentation en arrière-plan.

Tout d'abord, nous allons apprendre à limiter le débit de l'API pour toutes les requêtes. Ensuite, nous apprendrons à implémenter un mécanisme de limitation de débit plus complexe par utilisateur ou par palier de tarification.

Commençons par la configuration du projet.

### Installer les dépendances

Ajoutons les dépendances ci-dessous à notre fichier _pom.xml_ (ou _build.gradle_).

```xml
<dependencies>
    <!-- Pour construire l'API Rest -->
    <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    
    <!-- Redisson Starter = starter Spring Data Redis (excluant les autres clients) et client Redisson -->
    <dependency>
        <groupId>org.redisson</groupId>
        <artifactId>redisson-spring-boot-starter</artifactId>
        <version>3.17.0</version>
    </dependency>
    
    <!-- Bucket4J starter = Bucket4J + JCache -->
    <dependency>
        <groupId>com.giffing.bucket4j.spring.boot.starter</groupId>
        <artifactId>bucket4j-spring-boot-starter</artifactId>
        <version>0.5.2</version>
    </dependency>
</dependencies>

```

### Configuration du cache

Premièrement, nous devons démarrer notre serveur Redis. Disons que nous avons un serveur Redis tournant sur le port 6379 sur notre machine locale.

Nous devons effectuer deux étapes :

1. Créer une connexion à ce serveur depuis notre application.
2. Configurer JCache pour utiliser le client Redisson comme implémentation.

La [documentation de Redisson](https://github.com/redisson/redisson/wiki/14.-Integration-with-frameworks/#144-jcache-api-jsr-107-implementation) fournit des étapes concises pour implémenter cela dans une application Java régulière. Nous allons implémenter les mêmes étapes, mais dans Spring Boot.

Regardons d'abord le code. Nous devons créer une classe de Configuration pour créer les beans requis.

```java
@Configuration
public class RedisConfig  {
    
    @Bean
    public Config config() {
        Config config = new Config();
        config.useSingleServer().setAddress("redis://localhost:6379");
        return config;
    }
    
    @Bean
    public CacheManager cacheManager(Config config) {
        CacheManager manager = Caching.getCachingProvider().getCacheManager();
        cacheManager.createCache("cache", RedissonConfiguration.fromConfig(config));
        return cacheManager;
    }

    @Bean
    ProxyManager<String> proxyManager(CacheManager cacheManager) {
        return new JCacheProxyManager<>(cacheManager.getCache("cache"));
    }
}

```

**Que fait ce code ?**

1. Crée un objet de configuration que nous pouvons utiliser pour créer une connexion.
2. Crée un gestionnaire de cache (cache manager) à l'aide de l'objet de configuration. Cela créera en interne une connexion à l'instance Redis et créera un hash nommé "cache" sur celle-ci.
3. Crée un gestionnaire de proxy (proxy manager) qui sera utilisé pour accéder au cache. Tout ce que notre application tente de mettre en cache à l'aide de l'API JCache sera mis en cache sur l'instance Redis à l'intérieur du hash nommé "cache".

### Créer l'API

Créons une API REST simple.

```java
@RestController
public class RateLimitController {
    @GetMapping("/user/{id}")
    public String getInfo(@PathVariable("id") String id) {
        return "Hello " + id;
    }
}

```

Si j'appelle l'API avec l'URL `http://localhost:8080/user/1`, j'obtiendrai la réponse `Hello 1`.

### Configuration de Bucket4J

Pour implémenter la limitation de débit, nous devons configurer Bucket4J. Heureusement, nous n'avons pas besoin d'écrire de code répétitif grâce à la bibliothèque starter.

Elle **détecte également automatiquement le bean ProxyManager** que nous avons créé à l'étape précédente et l'utilise pour mettre en cache les buckets.

Ce que nous devons faire, c'est configurer cette bibliothèque autour de l'API que nous avons créée.
Encore une fois, il existe plusieurs façons de procéder.

Nous pouvons opter pour une [configuration basée sur les propriétés](https://github.com/MarcGiffing/bucket4j-spring-boot-starter#configuration-via-properties) qui est définie dans la bibliothèque starter.
C'est le moyen le plus pratique pour des cas simples comme la limitation de débit pour tous les utilisateurs ou tous les utilisateurs invités.

Cependant, si nous voulons implémenter quelque chose de plus complexe comme une limite de débit pour chaque utilisateur, il est préférable d'écrire du code personnalisé pour cela.

Nous allons implémenter la limitation de débit par utilisateur. Supposons que la limite de débit pour chaque utilisateur soit stockée dans une base de données et que nous puissions l'interroger à l'aide de l'ID utilisateur.

Écrivons le code étape par étape.

#### Créer un Bucket

Avant de commencer, regardons comment un bucket est créé.

```java
Refill refill = Refill.intervally(10, Duration.ofMinutes(1));
Bandwidth limit = Bandwidth.classic(10, refill);
Bucket bucket = Bucket4j.builder()
        .addLimit(limit)
        .build();

```

* **Refill** – Après combien de temps le seau sera rempli.
* **Bandwidth** – Quelle bande passante le seau possède. En gros, le nombre de requêtes par période de recharge.
* **Bucket** – Un objet configuré à l'aide de ces deux paramètres. De plus, il maintient un compteur de jetons pour suivre le nombre de jetons disponibles dans le seau.

En utilisant cela comme base, modifions quelques éléments pour l'adapter à notre cas d'utilisation.

#### Créer et mettre en cache les Buckets à l'aide de ProxyManager

Nous avons créé le gestionnaire de proxy dans le but de stocker les buckets sur Redis. Une fois qu'un bucket est créé, il doit être mis en cache sur Redis et n'a pas besoin d'être recréé.

Pour ce faire, nous allons remplacer le `Bucket4j.builder()` par `proxyManager.builder()`. ProxyManager s'occupera de la mise en cache des buckets et ne les recréera pas.

Le builder de ProxyManager prend deux paramètres – une **clé** contre laquelle le bucket sera mis en cache et un **objet de configuration** qu'il utilisera pour créer le bucket.

Voyons comment nous pouvons l'implémenter :

```java
@Service
public class RateLimiter {
    // injection des dépendances
    
    public Bucket resolveBucket(String key) {
        Supplier<BucketConfiguration> configSupplier = getConfigSupplierForUser(key);
        
        // Ne crée pas toujours un nouveau bucket, mais renvoie celui existant s'il existe.
        return buckets.builder().build(key, configSupplier);
    }

    private Supplier<BucketConfiguration> getConfigSupplierForUser(String key) {
        User user = userRepository.findById(userId);
        Refill refill = Refill.intervally(user.getLimit(), Duration.ofMinutes(1));
        Bandwidth limit = Bandwidth.classic(user.getLimit(), refill);
        return () -> (BucketConfiguration.builder()
                .addLimit(limit)
                .build());
    }
}

```

Nous avons créé une méthode qui renvoie un bucket pour une clé fournie. Dans l'étape suivante, nous verrons comment l'utiliser.

#### Comment consommer des jetons et configurer la limitation de débit

Lorsqu'une requête arrive, nous allons essayer de consommer un jeton du seau concerné.
Nous utiliserons la méthode `tryConsume()` du bucket pour faire cela.

```java
@GetMapping("/user/{id}")
public String getInfo(@PathVariable("id") String id) {
    // récupère le bucket pour l'utilisateur
    Bucket bucket = rateLimiter.resolveBucket(id);
    
    // tente de consommer un jeton du bucket
    if (bucket.tryConsume(1)) {
        return "Hello " + id;
    } else {
        return "Rate limit exceeded";
    }
}

```

La méthode `tryConsume()` renvoie `true` si le jeton a été consommé avec succès ou `false` si le jeton n'a pas été consommé.

## Comment tester notre service

Nous pouvons tester cela en utilisant n'importe quelle technique de test automatisé. Par exemple, nous pouvons utiliser [JUnit](https://junit.org/). Écrivons un cas de test qui appelle la méthode `getInfo()` plusieurs fois et vérifie que la réponse est correcte.

Supposons que nous ayons un utilisateur avec l'ID `1` et une limite de `10` requêtes par minute. Supposons également que nous ayons un utilisateur avec l'ID `2` et une limite de `20` requêtes par minute.

Nous allons lancer 11 requêtes pour les deux utilisateurs et vérifier que la requête échoue pour l'utilisateur avec l'ID `1` mais réussit pour l'utilisateur avec l'ID `2`.

```java
@Test
public void testGetInfo() {

    // appelle la méthode 10 fois pour l'utilisateur 1
    for (int i = 0; i < 10; i++) {
        rateLimiter.getInfo(1));
        rateLimiter.getInfo(2));
    }
    
    // vérifie que la réponse est limitée par le débit pour l'utilisateur 1
    assertEquals("Rate limit exceeded", rateLimiter.getInfo(1));
    
    // vérifie que la réponse est réussie pour l'utilisateur 2
    assertEquals("Hello 2", rateLimiter.getInfo(2));
}

```

Lorsque nous exécutons le test, nous verrons que le test réussit.

## Conclusion

Dans ce tutoriel, nous avons vu comment créer un limiteur de débit en utilisant Bucket4j et Redis dans une application Spring Boot. Nous avons également examiné comment configurer un client Redisson avec JCache et comment l'utiliser pour mettre en cache des buckets.

À la fin, nous avons implémenté un limiteur de débit simple qui peut être utilisé pour limiter le débit des requêtes pour des utilisateurs spécifiques.

J'espère que vous avez apprécié ce tutoriel. Merci de m'avoir lu !