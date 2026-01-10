---
title: How to Set Up Java Spring Boot JWT Authorization and Authentication
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-12T20:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-setup-jwt-authorization-and-authentication-in-spring
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/jwt.png
tags:
- name: authentication
  slug: authentication
- name: authorization
  slug: authorization
- name: JSON Web Tokens
  slug: json-web-tokens
- name: JWT
  slug: jwt
- name: spring-boot
  slug: spring-boot
- name: spring security
  slug: spring-security
seo_title: null
seo_desc: "By Yiğit Kemal Erinç\nIn the past month, I had a chance to implement JWT\
  \ auth for a side project. I have previously worked with JWT in Ruby on Rails, but\
  \ this was my first time in Spring. \nIn this post, I will try to explain what I\
  \ have learned and ap..."
---

By Yiğit Kemal Erinç

In the past month, I had a chance to implement JWT auth for a side project. I have previously worked with JWT in Ruby on Rails, but this was my first time in Spring. 

In this post, I will try to explain what I have learned and applied in my project to share my experience and hopefully help some people. 

We will start by taking a quick look at the theory behind JWT and how it works. Then we will look at how to implement it in a Spring Boot application.

## JWT Basics

JWT, or JSON Web Tokens ([RFC 7519](https://tools.ietf.org/html/rfc7519)), is a standard that is mostly used for securing REST APIs. Despite being a relatively new technology, it is gaining rapid popularity.

In the JWT auth process, the front end (client) firstly sends some credentials to authenticate itself (username and password in our case, since we're working on a web application). 

The server (the Spring app in our case) then checks those credentials, and if they are valid, it generates a JWT and returns it. 

After this step client has to provide this token in the request’s **Authorization** header in the “Bearer TOKEN” form. The back end will check the validity of this token and authorize or reject requests. The token may also store user roles and authorize the requests based on the given authorities.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/1.jpg)

## Implementation

Now let’s see how we can implement the JWT login and save mechanism in a real Spring application.

### Dependencies

You can see the list of Maven dependencies that our example code uses below. Note that the core dependencies like Spring Boot and Hibernate are not included in this screenshot.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/2-1.png)

### Saving Users

We will start by creating controllers to save users securely and authenticate them based on username and password.

We have a model entity called User. It is a simple entity class that maps to the **USER** table. You can use whatever properties you need depending on your application.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/3-1.png)

We also have a simple **UserRepository** class to save users. We need to override the **findByUsername** method since we will use it in authentication.

```java
public interface UserRepository extends JpaRepository<User, String>{ 
    User findByUsername(String username); 
}
```

We should never store plaintext passwords in the database because many users tend to use the same password for multiple sites. 

There are many different hashing algorithms, but the most commonly used one is **BCrypt** and it is a recommended method of secure hashing. You can check out [this](https://security.blogoverflow.com/2013/09/about-secure-password-hashing/#:~:text=Passwords%20should%20be%20hashed%20with,providing%20most%20security%20is%20bcrypt.) article for more information on the topic.

To hash the password, we will define a **BCrypt** bean in **@SpringBootApplication** and annotate the main class as follows:

```java
@Bean public BCryptPasswordEncoder bCryptPasswordEncoder() {
    return new BCryptPasswordEncoder(); 
}
```

We will call the methods on this bean when we need to hash a password.

We also need a UserController to save users. We create the controller, annotate it with **@RestController,** and define the corresponding mapping. 

In our application, we save the user based on a DTO object that is passed from the front end. You can also pass a User object in **@RequestBody**.

After we pass the DTO object, we encrypt the password field using the **BCrypt** bean we created earlier. You could also do this in the controller, but it is a better practice to put this logic in the service class.

```java
@Transactional(rollbackFor = Exception.class) 
public String saveDto(UserDto userDto) { 
    userDto.setPassword(bCryptPasswordEncoder
           .encode(userDto.getPassword())); 
    return save(new User(userDto)).getId(); 
}
```

### Authentication Filter

We need authentication to make sure that the user is really who they claim to be. We will be using the classic username/password pair to accomplish this.

Here are the steps to implement authentication:

1. Create our Authentication Filter that extends **UsernamePasswordAuthenticationFilter**
2. Create a security configuration class that extends **WebSecurityConfigurerAdapter** and apply the filter

Here is the code for our Authentication Filter – as you might know, filters are the backbone of Spring Security.

<script src="https://gist.github.com/yigiterinc/74e24d263cc403a9057cf046d514860a.js"></script>

Let’s go over this code step by step.

This class extends **UsernamePasswordAuthenticationFilter** which is the default class for password authentication in Spring Security. We extend it to define our custom authentication logic.

We make a call to the **setFilterProcessesUrl** method in our constructor. This method sets the default login URL to the provided parameter. 

If you remove this line, Spring Security creates the **“/login”** endpoint by default. It defines the login endpoint for us, which is why we will not define a login endpoint in our controller explicitly. 

After this line our login endpoint will be **/api/services/controller/user/login**. You can use this function to stay consistent with your endpoints.

We override the **attemptAuthentication** and **successfulAuthentication** methods of the **UsernameAuthenticationFilter** class.

The **attemptAuthentication** function runs when the user tries to log in to our application. It reads the credentials, creates a user POJO from them, and then checks the credentials to authenticate. 

We pass the username, password, and an empty list. The empty list represents the authorities (roles), and we leave it as is since we do not have any roles in our application yet.

If the authentication is successful, the **successfulAuthentication** method runs. The parameters of this method are passed by Spring Security behind the scenes. 

The **attemptAuthentication** method returns an **Authentication** object that contains the authorities we passed while attempting. 

We want to return a token to user after authentication is successful, so we create the token using username, secret, and expiration date. We need to define the **SECRET** and **EXPIRATION_DATE** now.

<script src="https://gist.github.com/yigiterinc/9c612aaeb05234f4b89caf4204942a1e.js"></script>

We create a class to be a container for our constants. You can set the secret to whatever you want, but the best practice is making the secret key as long as your hash. We use the **HS256** algorithm in this example, so our secret key is 256 bits/32 chars.

The expiration time is set to 15 minutes, because it is the best practice against secret key brute-forcing attacks. The time is in milliseconds.

We have prepared our Authentication filter, but it is not active yet. We also need an Authorization filter, and then we will apply them both through a configuration class. 

This filter will check the existence and validity of the access token on the Authorization header. We will specify which endpoints will be subject to this filter in our configuration class.

### Authorization Filter

<script src="https://gist.github.com/yigiterinc/353558bb33a0d4bfb37c054bf3ef2abf.js"></script>

The **doFilterInternal** method intercepts the requests then checks the Authorization header. If the header is not present or doesn’t start with “BEARER”, it proceeds to the filter chain. 

If the header is present, the **getAuthentication** method is invoked. **getAuthentication** verifies the JWT, and if the token is valid, it returns an access token which Spring will use internally. 

This new token is then saved to SecurityContext. You can also pass in Authorities to this token if you need for role-based authorization.

Our filters are ready, and now we need to put them into action with the help of a configuration class.

### Configuration

<script src="https://gist.github.com/yigiterinc/5aed60bcf1c53b34ed6b6e887158bbc0.js"></script>

We annotate this class with **@EnableWebSecurity** and extend **WebSecurityConfigureAdapter** to implement our custom security logic. 

We autowire the BCrypt bean that we defined earlier. We also autowire the **UserDetailsService** to find the user’s account. 

The most important method is the one which accepts an **HttpSecurity** object. Here we specify the secure endpoints and filters that we want to apply. We configure CORS, and then we permit all post requests to our sign up URL that we defined in the constants class. 

You can add other ant matchers to filter based on URL patterns and roles, and you can [check](https://stackoverflow.com/questions/44067650/spring-security-role-based-access) this StackOverflow question for examples regarding that. The other method configures the **AuthenticationManager** to use our encoder object as its password encoder while checking the credentials.

### Testing

Let’s send a few requests to test if it works properly.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/4.png)

Here we send a GET request to access a protected resource. Our server responds with a 403 code. This is the expected behavior because we haven’t provided a token in the header. Now let’s create a user:

![Image](https://www.freecodecamp.org/news/content/images/2020/08/5.png)

To create a user, we send a post request with our User DTO data. We will use this user to login and get an access token.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/6.png)

Great! We got the token. After this point, we will use this token to access protected resources.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/7.png)

We provide the token in the Authorization header and we are now allowed access to our protected endpoint.

## Conclusion

In this tutorial I have walked you through the steps I took when implementing JWT authorization and password authentication in Spring. We also learned how to save a user securely. 

Thank you for reading – I hope it was helpful to you. If you are interested in reading more content like this, feel free to subscribe to my blog at [https://erinc.io](https://erinc.io). :)

