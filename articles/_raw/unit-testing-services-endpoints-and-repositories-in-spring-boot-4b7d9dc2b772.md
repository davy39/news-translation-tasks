---
title: How to test services, endpoints, and repositories in Spring Boot
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
seo_title: null
seo_desc: 'By Emre Savcı

  In this post I will show you how to write unit tests in spring boot applications.

  Why is it necessary to write unit test requires another article to explain. But
  for a brief explanation, I will tell you several things.

  I usually defend ...'
---

By Emre Savcı

In this post I will show you how to write unit tests in spring boot applications.

Why is it necessary to write unit test requires another article to explain. But for a brief explanation, I will tell you several things.

I usually defend the argument that code without unit tests is dead code. Because, when a developer adds a new feature to some code which is not covered by a unit test, it is prone to override existing business rules (which kills the code written before). Maybe it’s not exactly prone to it, but you can imagine what errors can occur when a complex project needs to be changed. Unit testing is the only way to protect your code against breaking changes.

#### **Why unit test endpoints?**

Every time we write an endpoint we need to be sure several things work correctly. The endpoint should return the data in the correct structure and handle the request correctly. We can test it manually, which is not preferable. So we write unit tests to ensure that our endpoints work correctly. There is also another way for testing endpoints known as automation tests, but that is not the subject of this post.

#### **Why unit test services?**

It should be clear already, but just in case: we need to be sure our business logic works correctly.

#### **Why unit test repositories?**

There are several cases to test repositories. Of course we don’t test the framework itself. But we do write unit tests to be sure that our specifications or relations have been implemented correctly.

### **So how do we test controllers?**

Now it’s time to show you how to test our controllers in spring boot. Let’s imagine we write an application which allows us to save users in a database. We define a user entity, a user service, and a controller.

_Note: The examples shown in this post are not for real production use architecture_

```
@Data@Entitypublic class User {    @Id    @GeneratedValue(generator = "uuid2")    @GenericGenerator(name = "uuid2", strategy = "org.hibernate.id.UUIDGenerator")    @Column(name = "id", columnDefinition = "BINARY(16)")    private UUID id;    private String name;    private String email;    private int age;}
```

```
@Datapublic class CreateUserRequest {    private String name;    private String email;    private int age;}
```

```
@RestController@RequestMapping("/users")public class UserController {    UserService userService;    @Autowired    public UserController(UserService userService) {        this.userService = userService;    }    @PostMapping    public ResponseEntity<User> createUser(@RequestBody CreateUserRequest request) {        User created = userService.save(request);        return ResponseEntity.ok(created);    }}
```

Our controller has a dependency on UserService but we aren’t interested in what service does right now.

So now let’s write a unit test for our controller to be sure it works correctly.

![Image](https://cdn-media-1.freecodecamp.org/images/ZdQMKmxKk9mlD-AzNuUZpQxdCZ4VSi4ELW6d)

We mocked our service because we don’t need its implementation details. We just test our controller here. We use `MockMvc` here to test our controller and object mapper for serialization purposes.

We setup our `userService.Save()` method to return the desired user object. We passed a request to our controller and after that we checked the returned data with the following line: `andExpect(jsonPath("$.name").value(request.getName()))` .

We have also [other methods to use](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/test/web/servlet/result/JsonPathResultMatchers.html). Here is the list of methods:

![Image](https://cdn-media-1.freecodecamp.org/images/XNRt3lBVu-47pwdDQOg73BhX-Fy3OhCr-mZf)

When we run the test we see that it passes.

![Image](https://cdn-media-1.freecodecamp.org/images/Gx1sVQbUTi3rn7DiqgGQuMUVN60-4xWHIHji)

### **How do we test services?**

Now we go to test our UserService. It is quite simple to test.

![Image](https://cdn-media-1.freecodecamp.org/images/5ALGlLPT49JTxgUal22WbDbfrEhjBHD24eSV)

We mock the repository and inject our mocks into UserService. Now when we run the test we’ll see that it passes.

Now let’s add a business rule to UserService: let’s say the user must have an email address.

We change our save method in UserService as below:

```
public User save(CreateUserRequest request) {    requireNonNull(request.getEmail());        User user = new User();    user.setName(request.getName());    user.setEmail(request.getEmail());    user.setAge(request.getAge());    userRepository.save(user);    return user;}
```

When we run the test again, we’ll see a failed test.

![Image](https://cdn-media-1.freecodecamp.org/images/HhoeIyT6oUhvYVcCD2nbZepI3S-qbPfhUE5n)

Before we fix it, let’s write a test that satisfies this business.

![Image](https://cdn-media-1.freecodecamp.org/images/VZqkwBqS14vzxKBcMWdtHPES1xo8XxK3ht3I)

We wrote a new test that specified that if we send a null email, it’ll throw `NullPointerException.`

Let’s fix the failed test by adding an email to our request:

```
createUserRequest.setEmail("testemail");
```

Run both tests:

![Image](https://cdn-media-1.freecodecamp.org/images/hFTPEmxhpDT6WVsWc3VpeQ0Y9XOGwBdwr05u)

### **How do we test repositories?**

Now we’ve come to testing repositories. We use an in memory h2 database with `TestEntityManager.`

Our repository is defined as below:

```
@Repositorypublic interface UserRepository extends JpaRepository<User, Integer>, JpaSpecificationExecutor<User> {    Optional<User> findById(UUID id);}
```

First configure h2db. Create the file name application.yaml in test -> resources path:

```
spring:  application:    name: Spring Boot Rest API  datasource:    type: com.zaxxer.hikari.HikariDataSource    url: "jdbc:h2:mem:test-api;INIT=CREATE SCHEMA IF NOT EXISTS dbo\\;CREATE SCHEMA IF NOT EXISTS definitions;DATABASE_TO_UPPER=false;DB_CLOSE_DELAY=-1;DB_CLOSE_ON_EXIT=false;MODE=MSSQLServer"    name:    password:    username:    initialization-mode: never    hikari:      schema: dbo  jpa:    database: H2    database-platform: org.hibernate.dialect.H2Dialect    show-sql: true    hibernate:      ddl-auto: create-drop  test:    database:      replace: none
```

And let’s first write a basic test for our repository: save a user and retrieve it:

```
@RunWith(SpringRunner.class)@DataJpaTestpublic class UserRepositoryTest {    @Autowired    TestEntityManager entityManager;    @Autowired    UserRepository sut;    @Test    public void it_should_save_user() {        User user = new User();        user.setName("test user");        user = entityManager.persistAndFlush(user);        assertThat(sut.findById(user.getId()).get()).isEqualTo(user);    }}
```

When we run it we’ll see bunch of console output, and also our test passes:

![Image](https://cdn-media-1.freecodecamp.org/images/ZvTQXeFLK6VNU5jrP7Xl61vbBwNi6wJMJnHR)

Now let’s add another method to our repository for searching for a user via email:

```
Optional<User> findByEmail(String email);
```

And write another test:

```
@Testpublic void it_should_find_user_byEmail() {    User user = new User();    user.setEmail("testmail@test.com");    user = entityManager.persistAndFlush(user);    assertThat(sut.findByEmail(user.getEmail()).get()).isEqualTo(user);}
```

When we take a look at the console after running the test, we'll see the SQL generated by hibernate:

```
SELECT user0_.id AS id1_1_,user0_.age AS age2_1_,user0_.email AS email3_1_,user0_.name AS name4_1_FROM user user0_WHERE user0_.email=?
```

![Image](https://cdn-media-1.freecodecamp.org/images/817OJk5EOmr4TjTvg9Pcul7Ki6fdpNMqbYqP)

So far so good. We have covered the basics of unit testing with spring boot.

Now you don’t have any excuses to not write unit tests! I hope it is clear to you to how to write unit tests for different kinds of purposes.

