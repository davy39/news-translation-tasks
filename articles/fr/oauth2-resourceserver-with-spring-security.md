---
title: Comment implémenter un serveur de ressources OAuth2 avec Spring Security
subtitle: ''
author: Kunal Nalawade
co_authors: []
series: null
date: '2024-05-08T15:39:37.000Z'
originalURL: https://freecodecamp.org/news/oauth2-resourceserver-with-spring-security
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/article-cover.jpeg
tags:
- name: Java
  slug: java
- name: spring-boot
  slug: spring-boot
seo_title: Comment implémenter un serveur de ressources OAuth2 avec Spring Security
seo_desc: 'Hey everyone! Imagine you are building an awesome application, with lots
  of cool features. Picture a backend server at its core that hosts a majority of
  the business logic and exposes functionality through APIs.

  Once you have planned out your APIs, t...'
---

Salut à tous ! Imaginez que vous construisez une application géniale, avec plein de fonctionnalités cool. Imaginez un serveur backend au cœur de celle-ci qui héberge la majorité de la logique métier et expose des fonctionnalités via des APIs.

Une fois que vous avez planifié vos APIs, il y a une étape cruciale à ne pas négliger : sécuriser vos APIs. Vous ne voulez pas que vos APIs soient exposées à n'importe qui sur internet (sauf si vous développez pour l'open source).

L'authentification garantit que vos APIs ne peuvent être accessibles que par les utilisateurs authentifiés de votre application. Un utilisateur peut être authentifié avec un nom d'utilisateur et un mot de passe, ou via un jeton d'accès.

Dans cet article, nous allons voir comment sécuriser vos APIs en utilisant OAuth2 et des jetons d'accès. Je suppose que vous avez une connaissance de base de Java et de Spring Boot. Si ce n'est pas le cas, vous pouvez [consulter ce cours sur la chaîne YouTube de freeCodeCamp](https://www.freecodecamp.org/news/learn-app-development-with-spring-boot-3/).

## Table des matières

1. [Qu'est-ce que OAuth2 ?](#heading-quest-ce-que-oauth2)
   
2. [Comment configurer l'application Spring Boot](#heading-comment-configurer-lapplication-spring-boot)
   
3. [Configuration de la sécurité Web](#configuration)
   
4. [APIs publiques et privées](#write-apis-in-controller-class)
   
5. [Test des APIs avec et sans jeton d'accès](#heading-test-des-apis)
   
6. [Comment obtenir les détails de l'utilisateur à partir du jeton d'accès](#heading-comment-obtenir-les-details-de-lutilisateur-a-partir-du-jeton-dacces)
   

## Qu'est-ce que OAuth2 ?

OAuth2 est un framework qui permet aux applications tierces d'accéder à votre service au nom d'un utilisateur final. Il est largement utilisé pour l'authentification et l'autorisation dans les applications modernes.

Il y a quatre composants dans le framework OAuth2 :

* **Propriétaire de la ressource** : L'utilisateur final de votre application.
   
* **Serveur d'autorisation** : L'application tierce qui authentifie l'utilisateur et délivre un jeton d'accès après une authentification réussie.
   
* **Client** : L'interface utilisateur via laquelle l'utilisateur souhaite accéder à vos ressources. Le client peut être une application mobile, une application web ou une application de bureau. Le client nécessite un jeton d'accès pour accéder à vos APIs.
   
* **Serveur de ressources** : Le serveur hébergeant les ressources protégées. Il valide le jeton d'accès et accorde l'accès aux ressources si l'authentification est réussie.
   

L'utilisateur, via le client, demande un jeton d'accès au serveur d'autorisation. Si l'authentification est réussie, le client utilise ce jeton pour accéder aux APIs protégées exposées par le serveur de ressources.

Dans cet article, nous allons nous concentrer uniquement sur l'implémentation du serveur de ressources.

## Comment configurer l'application Spring Boot

Pour configurer votre application, rendez-vous sur [Spring Initializr](https://start.spring.io/).

![Image](https://www.freecodecamp.org/news/content/images/2024/04/image-44.png align="left")

*Spring Initializr*

Choisissez *Gradle* ou *Maven* pour le projet, la version de Spring Boot et le nom du projet. Ajoutez les dépendances suivantes : *spring-boot-starter-web* et *oauth2-resource-server*.

Cliquez sur *Generate* pour télécharger l'application Spring Boot et une fois téléchargée, extrayez le fichier zip. Vous devriez maintenant avoir une application Spring Boot fonctionnelle avec les dépendances entièrement chargées. Ouvrez IntelliJ (ou tout autre IDE de votre choix) et sélectionnez ce projet pour commencer à travailler.

Vous pouvez trouver le code complet de ce tutoriel sur [GitHub](https://github.com/KunalN25/my-tutorials/tree/main/java-springboot/oauth2-resource-server-tutorial).

## Configuration de la sécurité Web

Tout d'abord, ouvrez `application.properties` et ajoutez la propriété suivante :

```python
spring.security.oauth2.resourceserver.jwt.issuer-uri: ${JWT_ISSUER_URI}
```

Vous pouvez trouver l'*issuer-uri* dans la configuration open-id du service OAuth2 que vous utilisez. Par exemple, consultez la configuration [Google OAuth2](https://accounts.google.com/.well-known/openid-configuration).

Ensuite, configurons Spring Security.

Pour implémenter le serveur de ressources, vous devez avoir Spring Security comme l'une de vos dépendances. Ici, nous n'avons pas besoin de l'ajouter séparément puisque *oauth2-resource-server* utilise Spring Security.

Lorsque vous ajoutez Spring Security dans vos dépendances, Spring Boot active l'authentification pour chaque API que vous exposez. Par défaut, il s'agit de l'authentification basée sur le nom d'utilisateur et le mot de passe.

Cela se produit parce que Spring Security a sa propre classe `SecurityAutoConfiguration` qui contient la configuration de sécurité par défaut. Mais nous n'avons pas ajouté Spring Security dans nos dépendances.

Puisque nous ne voulons pas d'authentification basée sur le nom d'utilisateur et le mot de passe, nous devons désactiver la configuration automatique. Allez dans la classe principale et ajoutez l'exclusion suivante :

```java
@SpringBootApplication(exclude = { SecurityAutoConfiguration.class})
public class Oauth2ResourceServerTutorialApplication {
	public static void main(String[] args) {
		SpringApplication.run(Oauth2ResourceServerTutorialApplication.class, args);
	}
}
```

Si vous exécutez l'application maintenant, elle génère une erreur.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/image-45.png align="left")

*Erreur sans configuration*

Ajoutons maintenant notre propre configuration. Créez une nouvelle classe Java `SecurityConfig` avec les annotations suivantes :

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig {
	// Beans ici
}
```

`@Configuration` indique que ceci est une classe de configuration qui contient plusieurs méthodes Bean, responsables de la création de beans. Les [Beans](https://www.baeldung.com/spring-bean) sont simplement des objets qui forment les blocs de construction d'une application Spring Boot. `@EnableWebSecurity` indique à Spring Boot d'activer la sécurité Web avec vos configurations.

Créez une méthode qui retourne un bean de type `SecurityFilterChain`. Le bean de chaîne de filtres de sécurité intercepte les requêtes entrantes et leur applique des filtres personnalisés. C'est ici que vous pouvez appliquer différents types d'autorisation à différentes requêtes.

```java
@Bean
public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
                .authorizeHttpRequests((authz) -> authz
                        .requestMatchers("/public/**").permitAll()
                        .anyRequest().authenticated()
                )
                .oauth2ResourceServer(oauth2 -> oauth2.jwt(Customizer.withDefaults()));
        return http.build();
    }
```

Comprenons les parties clés de ce code :

* La méthode `filterChain()` prend un objet `HttpSecurity` comme argument. Cette classe de Spring Security vous permet de configurer les requêtes.
   
* La méthode `authorizeHttpRequests()` prend un objet que nous avons représenté comme une expression lambda.
   
* Nous avons utilisé la méthode `requestMatchers()` pour faire correspondre une route qui sera accessible sans authentification. Dans notre cas, toute route commençant par `/public` sera accessible à tous. Les requêtes vers toute autre route nécessiteront une authentification.
   
* La méthode `oauth2ResourceServer()` configure notre application comme un serveur de ressources OAuth2. Ici, nous spécifions que l'authentification JWT sera utilisée avec des personnalisateurs par défaut.
   
* Enfin, `http.build()` construit l'objet `HttpSecurity` et le retourne.
   

Dans ce projet, nous avons configuré la sécurité Web de la manière ci-dessus. Mais si vous avez d'autres exigences, vous pourriez avoir besoin d'une configuration différente. Par exemple, si vous avez des rôles privilégiés comme admin dans votre application, vous pouvez spécifier quelles routes chaque rôle peut accéder, et ainsi de suite.

Consultez la documentation du [serveur de ressources JWT](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/jwt.html) pour comprendre les différentes façons de personnaliser la sécurité Web.

## Écrire des APIs dans la classe Controller

Écrivons deux APIs simples. Créez une classe `MainController` qui exposera ces APIs :

```java
@RestController
public class MainController {

    @GetMapping("/public")
    public String homePage() {
        return "Hello from Spring boot app";
    }

    @GetMapping("/private")
    public String privateRoute() {
        return "Private Route";
    }
}
```

L'annotation `@RestController` indique que cette classe gérera les requêtes HTTP et retournera les données au client, généralement au format JSON. Nous avons écrit une API publique et une API privée.

Enregistrez le fichier et exécutez l'application.

## Test des APIs

Testons les APIs ci-dessus en utilisant Postman, sans en-tête d'autorisation.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/image-9.png align="left")

*/public route*

![Image](https://www.freecodecamp.org/news/content/images/2024/05/image-10.png align="left")

*/private route*

Dans les deux appels d'API ci-dessus, la route `/public` a retourné une réponse, tandis que la route `/private` a généré une erreur avec un statut `401 Unauthorized`.

Cela est dû au fait que, dans notre configuration, nous avons rendu toutes les routes commençant par `/public` accessibles sans authentification. Toutes les autres routes nécessiteraient une forme d'authentification. Dans notre cas, nous avons besoin d'un Bearer Token pour accéder à la route privée.

Incluons un en-tête d'autorisation dans la requête vers le point de terminaison `/private`.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/image-11.png align="left")

*/private route request with access token*

Lorsque nous incluons un en-tête d'autorisation avec le jeton d'accès, la route privée retourne une réponse. Pour cela, et pour toute autre route ne commençant pas par `/public`, nous devons passer un jeton d'accès dans l'en-tête.

Nous n'allons pas voir comment obtenir un jeton d'accès, puisque nous nous concentrons uniquement sur le serveur de ressources. Le client OAuth2 est responsable de l'obtention d'un jeton d'accès. Je couvrirai cela dans un futur article.

## Comment obtenir les détails de l'utilisateur à partir du jeton d'accès

Lorsque vous faites une requête vers une route privée, le filtre de sécurité intercepte cette requête et recherche un Bearer Token. Si un jeton existe, il le décode et extrait les informations d'authentification du jeton. Vous pouvez comprendre ce processus en détail à partir de la documentation du [Serveur de ressources OAuth2](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/index.html).

Si le jeton est valide et que l'authentification est réussie, les données d'authentification sont définies sur la classe [SecurityContextHolder](https://docs.spring.io/spring-security/reference/servlet/authentication/architecture.html#servlet-authentication-securitycontextholder). Le `SecurityContextHolder` contient les détails de l'utilisateur authentifié. Nous utilisons cette classe pour extraire les informations de l'utilisateur telles que le nom, l'email, etc.

Voyons comment nous pouvons obtenir ces détails de l'utilisateur. Tout d'abord, nous obtenons un objet [Authentication](https://docs.spring.io/spring-security/reference/servlet/authentication/architecture.html#servlet-authentication-authentication) à partir du `SecurityContextHolder` :

```java
Authentication authentication = SecurityContextHolder.getContext().getAuthentication();
```

Ensuite, nous utilisons `getPrincipal()` qui retourne un objet :

```java
Object principal = authentication.getPrincipal();
```

Puisque nous utilisons l'authentification JWT, l'objet ci-dessus peut être converti en un objet de type [Jwt](https://docs.spring.io/spring-security/site/docs/current/api/org/springframework/security/oauth2/jwt/Jwt.html). L'objet contient les champs suivants :

```python
{
    "tokenValue": token_value,
    "issuedAt": "",
    "expiresAt": "",
    "headers": {...},
    "claims": {        
        "name": full_name,
        "email": user_email,
        "given_name": first_name,
        "family_name": last_name,
        "picture": picture_link,
        ...other fields
    },
    "subject": "",
    "id": null,
    "issuer": issuer_link,
    "audience": [...],
    "notBefore": null
}
```

Ici, nous pouvons obtenir les données de l'utilisateur à partir du champ `claims` :

```java
Map<String, Object> claims = ((Jwt) principal).getClaims();
```

En utilisant la map ci-dessus, nous pouvons obtenir les informations de l'utilisateur en utilisant la valeur de clé correspondante. Écrivons cette logique dans une classe séparée `CurrentAuthContext` :

```java
public class CurrentAuthContext {
    private static Map<String, Object> extractClaim() {
        Authentication authentication = SecurityContextHolder.getContext().getAuthentication();
        Object principal = authentication.getPrincipal();
        Map<String, Object> claims = ((Jwt) principal).getClaims();
        return claims;
    }

    public static String getUserEmail() {
        return (String) extractClaim().get("email");
    }
}
```

Vous pouvez ajouter plus de méthodes pour obtenir les détails dont vous avez besoin. Pour obtenir l'email de l'utilisateur n'importe où dans l'application, appelez simplement `CurrentAuthContext.getUserEmail()` ou toute autre méthode retournant la valeur dont vous avez besoin.

Je n'ai pas implémenté de gestion d'erreurs personnalisée ici. Vous pouvez me contacter pour différentes façons d'implémenter une gestion d'erreurs personnalisée.

## Conclusion

OAuth2 fournit un framework robuste pour sécuriser vos APIs tout en fournissant un accès aux utilisateurs autorisés. Dans cet article, nous avons commencé par comprendre OAuth2 et ses composants.

Spring Security est une partie fondamentale du serveur de ressources OAuth2 de Spring. Nous avons appris comment implémenter des configurations de sécurité selon nos besoins. Ensuite, nous avons défini des APIs publiques et privées et les avons testées avec et sans jeton d'accès.

Une API privée ne peut être accessible qu'avec un jeton d'accès passé via l'en-tête d'autorisation. Nous avons également implémenté une logique pour extraire les informations de l'utilisateur à partir du jeton d'accès avec la classe `SecurityContextHolder`.

J'ai joint des liens de référence vers la documentation à divers endroits pour une meilleure compréhension de ces concepts. C'est tout pour aujourd'hui. J'espère que cela vous aidera dans vos futurs projets.

Si vous ne comprenez pas le contenu ou trouvez l'explication insatisfaisante, n'hésitez pas à me contacter. Les nouvelles idées sont toujours appréciées ! N'hésitez pas à me contacter sur Twitter. À bientôt !!