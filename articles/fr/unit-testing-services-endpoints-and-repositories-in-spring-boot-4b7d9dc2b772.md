---
title: Comment tester les services, les endpoints et les repositories dans Spring
  Boot
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-01T15:55:23.000Z'
originalURL: https://freecodecamp.org/news/unit-testing-services-endpoints-and-repositories-in-spring-boot-4b7d9dc2b772
coverImage: https://cdn-media-1.freecodecamp.org/images/1*aH_ifsVI0cI5P5Guu1X1CQ.jpeg
tags:
- name: Java
  slug: java
- name: software development
  slug: software-development
- name: spring-boot
  slug: spring-boot
- name: technology
  slug: technology
- name: unit testing
  slug: unit-testing
seo_title: Comment tester les services, les endpoints et les repositories dans Spring
  Boot
seo_desc: 'By Emre Savcı

  In this post I will show you how to write unit tests in spring boot applications.

  Why is it necessary to write unit test requires another article to explain. But
  for a brief explanation, I will tell you several things.

  I usually defend ...'
---

Par Emre Savcı

Dans cet article, je vais vous montrer comment écrire des tests unitaires dans les applications Spring Boot.

Pourquoi il est nécessaire d'écrire des tests unitaires nécessite un autre article pour être expliqué. Mais pour une brève explication, je vais vous dire plusieurs choses.

Je défends généralement l'argument selon lequel le code sans tests unitaires est du code mort. Parce que, lorsqu'un développeur ajoute une nouvelle fonctionnalité à un code qui n'est pas couvert par un test unitaire, il est sujet à écraser les règles métier existantes (ce qui tue le code écrit auparavant). Peut-être que ce n'est pas exactement sujet à cela, mais vous pouvez imaginer quelles erreurs peuvent survenir lorsqu'un projet complexe doit être modifié. Les tests unitaires sont le seul moyen de protéger votre code contre les changements cassants.

#### **Pourquoi tester les endpoints avec des tests unitaires ?**

Chaque fois que nous écrivons un endpoint, nous devons être sûrs que plusieurs choses fonctionnent correctement. L'endpoint doit retourner les données dans la structure correcte et gérer la requête correctement. Nous pouvons le tester manuellement, ce qui n'est pas préférable. Nous écrivons donc des tests unitaires pour nous assurer que nos endpoints fonctionnent correctement. Il existe également une autre méthode pour tester les endpoints connue sous le nom de tests d'automatisation, mais ce n'est pas le sujet de cet article.

#### **Pourquoi tester les services avec des tests unitaires ?**

Cela devrait déjà être clair, mais au cas où : nous devons être sûrs que notre logique métier fonctionne correctement.

#### **Pourquoi tester les repositories avec des tests unitaires ?**

Il existe plusieurs cas pour tester les repositories. Bien sûr, nous ne testons pas le framework lui-même. Mais nous écrivons des tests unitaires pour être sûrs que nos spécifications ou relations ont été implémentées correctement.

### **Comment tester les contrôleurs ?**

Il est maintenant temps de vous montrer comment tester nos contrôleurs dans Spring Boot. Imaginons que nous écrivons une application qui nous permet de sauvegarder des utilisateurs dans une base de données. Nous définissons une entité utilisateur, un service utilisateur et un contrôleur.

_Note : Les exemples présentés dans cet article ne sont pas destinés à une architecture de production réelle_

```
@Data
@Entity
public class User {
    @Id
    @GeneratedValue(generator = "uuid2")
    @GenericGenerator(name = "uuid2", strategy = "org.hibernate.id.UUIDGenerator")
    @Column(name = "id", columnDefinition = "BINARY(16)")
    private UUID id;
    private String name;
    private String email;
    private int age;
}
```

```
@Data
public class CreateUserRequest {
    private String name;
    private String email;
    private int age;
}
```

```
@RestController
@RequestMapping("/users")
public class UserController {
    UserService userService;
    @Autowired
    public UserController(UserService userService) {
        this.userService = userService;
    }
    @PostMapping
    public ResponseEntity<User> createUser(@RequestBody CreateUserRequest request) {
        User created = userService.save(request);
        return ResponseEntity.ok(created);
    }
}
```

Notre contrôleur a une dépendance sur UserService, mais nous ne nous intéressons pas à ce que fait le service pour l'instant.

Alors maintenant, écrivons un test unitaire pour notre contrôleur pour être sûr qu'il fonctionne correctement.

![Image](https://cdn-media-1.freecodecamp.org/images/ZdQMKmxKk9mlD-AzNuUZpQxdCZ4VSi4ELW6d)

Nous avons mocké notre service car nous n'avons pas besoin de ses détails d'implémentation. Nous testons simplement notre contrôleur ici. Nous utilisons `MockMvc` ici pour tester notre contrôleur et l'object mapper pour la sérialisation.

Nous avons configuré notre méthode `userService.save()` pour retourner l'objet utilisateur souhaité. Nous avons passé une requête à notre contrôleur et après cela, nous avons vérifié les données retournées avec la ligne suivante : `andExpect(jsonPath("$.name").value(request.getName()))`.

Nous avons également [d'autres méthodes à utiliser](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/test/web/servlet/result/JsonPathResultMatchers.html). Voici la liste des méthodes :

![Image](https://cdn-media-1.freecodecamp.org/images/XNRt3lBVu-47pwdDQOg73BhX-Fy3OhCr-mZf)

Lorsque nous exécutons le test, nous voyons qu'il passe.

![Image](https://cdn-media-1.freecodecamp.org/images/Gx1sVQbUTi3rn7DiqgGQuMUVN60-4xWHIHji)

### **Comment tester les services ?**

Maintenant, nous passons au test de notre UserService. C'est assez simple à tester.

![Image](https://cdn-media-1.freecodecamp.org/images/5ALGlLPT49JTxgUal22WbDbfrEhjBHD24eSV)

Nous mockons le repository et injectons nos mocks dans UserService. Maintenant, lorsque nous exécutons le test, nous verrons qu'il passe.

Maintenant, ajoutons une règle métier à UserService : disons que l'utilisateur doit avoir une adresse email.

Nous modifions notre méthode save dans UserService comme suit :

```
public User save(CreateUserRequest request) {
    requireNonNull(request.getEmail());
    User user = new User();
    user.setName(request.getName());
    user.setEmail(request.getEmail());
    user.setAge(request.getAge());
    userRepository.save(user);
    return user;
}
```

Lorsque nous exécutons le test à nouveau, nous verrons un test échoué.

![Image](https://cdn-media-1.freecodecamp.org/images/HhoeIyT6oUhvYVcCD2nbZepI3S-qbPfhUE5n)

Avant de le corriger, écrivons un test qui satisfait cette règle métier.

![Image](https://cdn-media-1.freecodecamp.org/images/VZqkwBqS14vzxKBcMWdtHPES1xo8XxK3ht3I)

Nous avons écrit un nouveau test qui spécifie que si nous envoyons un email null, il lèvera une `NullPointerException`.

Corrigeons le test échoué en ajoutant un email à notre requête :

```
createUserRequest.setEmail("testemail");
```

Exécutons les deux tests :

![Image](https://cdn-media-1.freecodecamp.org/images/hFTPEmxhpDT6WVsWc3VpeQ0Y9XOGwBdwr05u)

### **Comment tester les repositories ?**

Maintenant, nous en venons à tester les repositories. Nous utilisons une base de données h2 en mémoire avec `TestEntityManager`.

Notre repository est défini comme suit :

```
@Repository
public interface UserRepository extends JpaRepository<User, Integer>, JpaSpecificationExecutor<User> {
    Optional<User> findById(UUID id);
}
```

Tout d'abord, configurez h2db. Créez le fichier nommé application.yaml dans le chemin test -> resources :

```
spring:
  application:
    name: Spring Boot Rest API
  datasource:
    type: com.zaxxer.hikari.HikariDataSource
    url: "jdbc:h2:mem:test-api;INIT=CREATE SCHEMA IF NOT EXISTS dbo\\;CREATE SCHEMA IF NOT EXISTS definitions;DATABASE_TO_UPPER=false;DB_CLOSE_DELAY=-1;DB_CLOSE_ON_EXIT=false;MODE=MSSQLServer"
    name:
    password:
    username:
    initialization-mode: never
    hikari:
      schema: dbo
  jpa:
    database: H2
    database-platform: org.hibernate.dialect.H2Dialect
    show-sql: true
    hibernate:
      ddl-auto: create-drop
  test:
    database:
      replace: none
```

Et écrivons d'abord un test de base pour notre repository : sauvegarder un utilisateur et le récupérer :

```
@RunWith(SpringRunner.class)
@DataJpaTest
public class UserRepositoryTest {
    @Autowired
    TestEntityManager entityManager;
    @Autowired
    UserRepository sut;
    @Test
    public void it_should_save_user() {
        User user = new User();
        user.setName("test user");
        user = entityManager.persistAndFlush(user);
        assertThat(sut.findById(user.getId()).get()).isEqualTo(user);
    }
}
```

Lorsque nous l'exécutons, nous verrons une sortie de console et aussi notre test passe :

![Image](https://cdn-media-1.freecodecamp.org/images/ZvTQXeFLK6VNU5jrP7Xl61vbBwNi6wJMJnHR)

Maintenant, ajoutons une autre méthode à notre repository pour rechercher un utilisateur via son email :

```
Optional<User> findByEmail(String email);
```

Et écrivons un autre test :

```
@Test
public void it_should_find_user_byEmail() {
    User user = new User();
    user.setEmail("testmail@test.com");
    user = entityManager.persistAndFlush(user);
    assertThat(sut.findByEmail(user.getEmail()).get()).isEqualTo(user);
}
```

Lorsque nous regardons la console après avoir exécuté le test, nous verrons le SQL généré par hibernate :

```
SELECT user0_.id AS id1_1_,user0_.age AS age2_1_,user0_.email AS email3_1_,user0_.name AS name4_1_FROM user user0_WHERE user0_.email=?
```

![Image](https://cdn-media-1.freecodecamp.org/images/817OJk5EOmr4TjTvg9Pcul7Ki6fdpNMqbYqP)

Jusqu'à présent, tout va bien. Nous avons couvert les bases des tests unitaires avec Spring Boot.

Maintenant, vous n'avez plus aucune excuse pour ne pas écrire de tests unitaires ! J'espère qu'il est clair pour vous comment écrire des tests unitaires pour différents types de besoins.