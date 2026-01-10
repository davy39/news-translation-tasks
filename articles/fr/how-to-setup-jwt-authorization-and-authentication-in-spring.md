---
title: Comment configurer l'autorisation et l'authentification JWT avec Java Spring
  Boot
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
seo_title: Comment configurer l'autorisation et l'authentification JWT avec Java Spring
  Boot
seo_desc: "By Yiğit Kemal Erinç\nIn the past month, I had a chance to implement JWT\
  \ auth for a side project. I have previously worked with JWT in Ruby on Rails, but\
  \ this was my first time in Spring. \nIn this post, I will try to explain what I\
  \ have learned and ap..."
---

Par Yiğit Kemal Erinç

Le mois dernier, j'ai eu l'occasion d'implémenter l'authentification JWT pour un projet annexe. J'avais déjà travaillé avec JWT dans Ruby on Rails, mais c'était ma première fois avec Spring.

Dans cet article, je vais essayer d'expliquer ce que j'ai appris et appliqué dans mon projet pour partager mon expérience et, espérons-le, aider certaines personnes.

Nous commencerons par un rapide aperçu de la théorie derrière JWT et son fonctionnement. Ensuite, nous verrons comment l'implémenter dans une application Spring Boot.

## Bases de JWT

JWT, ou JSON Web Tokens ([RFC 7519](https://tools.ietf.org/html/rfc7519)), est une norme principalement utilisée pour sécuriser les API REST. Bien que ce soit une technologie relativement nouvelle, elle gagne rapidement en popularité.

Dans le processus d'authentification JWT, le front-end (client) envoie d'abord des identifiants pour s'authentifier (nom d'utilisateur et mot de passe dans notre cas, puisque nous travaillons sur une application web).

Le serveur (l'application Spring dans notre cas) vérifie ensuite ces identifiants, et s'ils sont valides, il génère un JWT et le retourne.

Après cette étape, le client doit fournir ce token dans l'en-tête **Authorization** de la requête sous la forme "Bearer TOKEN". Le back-end vérifie la validité de ce token et autorise ou rejette les requêtes. Le token peut également stocker les rôles de l'utilisateur et autoriser les requêtes en fonction des autorités données.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/1.jpg)

## Implémentation

Voyons maintenant comment nous pouvons implémenter le mécanisme de connexion et de sauvegarde JWT dans une véritable application Spring.

### Dépendances

Vous pouvez voir la liste des dépendances Maven utilisées par notre exemple de code ci-dessous. Notez que les dépendances principales comme Spring Boot et Hibernate ne sont pas incluses dans cette capture d'écran.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/2-1.png)

### Sauvegarde des utilisateurs

Nous allons commencer par créer des contrôleurs pour sauvegarder les utilisateurs de manière sécurisée et les authentifier en fonction du nom d'utilisateur et du mot de passe.

Nous avons une entité de modèle appelée User. Il s'agit d'une simple classe d'entité qui mappe à la table **USER**. Vous pouvez utiliser les propriétés dont vous avez besoin en fonction de votre application.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/3-1.png)

Nous avons également une simple classe **UserRepository** pour sauvegarder les utilisateurs. Nous devons remplacer la méthode **findByUsername** puisque nous allons l'utiliser pour l'authentification.

```java
public interface UserRepository extends JpaRepository<User, String>{ 
    User findByUsername(String username); 
}
```

Nous ne devons jamais stocker les mots de passe en texte brut dans la base de données, car de nombreux utilisateurs ont tendance à utiliser le même mot de passe pour plusieurs sites.

Il existe de nombreux algorithmes de hachage différents, mais le plus couramment utilisé est **BCrypt** et c'est une méthode recommandée pour le hachage sécurisé. Vous pouvez consulter [cet](https://security.blogoverflow.com/2013/09/about-secure-password-hashing/#:~:text=Passwords%20should%20be%20hashed%20with,providing%20most%20security%20is%20bcrypt.) article pour plus d'informations sur le sujet.

Pour hacher le mot de passe, nous allons définir un bean **BCrypt** dans **@SpringBootApplication** et annoter la classe principale comme suit :

```java
@Bean public BCryptPasswordEncoder bCryptPasswordEncoder() {
    return new BCryptPasswordEncoder(); 
}
```

Nous appellerons les méthodes de ce bean lorsque nous aurons besoin de hacher un mot de passe.

Nous avons également besoin d'un UserController pour sauvegarder les utilisateurs. Nous créons le contrôleur, l'annotons avec **@RestController**, et définissons le mapping correspondant.

Dans notre application, nous sauvegardons l'utilisateur en fonction d'un objet DTO qui est passé depuis le front-end. Vous pouvez également passer un objet User dans **@RequestBody**.

Après avoir passé l'objet DTO, nous chiffrons le champ du mot de passe en utilisant le bean **BCrypt** que nous avons créé précédemment. Vous pourriez également faire cela dans le contrôleur, mais il est préférable de mettre cette logique dans la classe de service.

```java
@Transactional(rollbackFor = Exception.class) 
public String saveDto(UserDto userDto) { 
    userDto.setPassword(bCryptPasswordEncoder
           .encode(userDto.getPassword())); 
    return save(new User(userDto)).getId(); 
}
```

### Filtre d'authentification

Nous avons besoin d'une authentification pour nous assurer que l'utilisateur est bien celui qu'il prétend être. Nous allons utiliser la paire classique nom d'utilisateur/mot de passe pour y parvenir.

Voici les étapes pour implémenter l'authentification :

1. Créer notre filtre d'authentification qui étend **UsernamePasswordAuthenticationFilter**
2. Créer une classe de configuration de sécurité qui étend **WebSecurityConfigurerAdapter** et appliquer le filtre

Voici le code de notre filtre d'authentification – comme vous le savez peut-être, les filtres sont l'épine dorsale de Spring Security.

<script src="https://gist.github.com/yigiterinc/74e24d263cc403a9057cf046d514860a.js"></script>

Passons en revue ce code étape par étape.

Cette classe étend **UsernamePasswordAuthenticationFilter**, qui est la classe par défaut pour l'authentification par mot de passe dans Spring Security. Nous l'étendons pour définir notre logique d'authentification personnalisée.

Nous faisons un appel à la méthode **setFilterProcessesUrl** dans notre constructeur. Cette méthode définit l'URL de connexion par défaut sur le paramètre fourni.

Si vous supprimez cette ligne, Spring Security crée le point de terminaison **"/login"** par défaut. Il définit le point de terminaison de connexion pour nous, c'est pourquoi nous ne définirons pas explicitement un point de terminaison de connexion dans notre contrôleur.

Après cette ligne, notre point de terminaison de connexion sera **/api/services/controller/user/login**. Vous pouvez utiliser cette fonction pour rester cohérent avec vos points de terminaison.

Nous remplaçons les méthodes **attemptAuthentication** et **successfulAuthentication** de la classe **UsernameAuthenticationFilter**.

La fonction **attemptAuthentication** s'exécute lorsque l'utilisateur essaie de se connecter à notre application. Elle lit les identifiants, crée un POJO utilisateur à partir de ceux-ci, puis vérifie les identifiants pour l'authentification.

Nous passons le nom d'utilisateur, le mot de passe et une liste vide. La liste vide représente les autorités (rôles), et nous la laissons telle quelle puisque nous n'avons pas encore de rôles dans notre application.

Si l'authentification est réussie, la méthode **successfulAuthentication** s'exécute. Les paramètres de cette méthode sont passés par Spring Security en arrière-plan.

La méthode **attemptAuthentication** retourne un objet **Authentication** qui contient les autorités que nous avons passées lors de la tentative.

Nous voulons retourner un token à l'utilisateur après que l'authentification soit réussie, donc nous créons le token en utilisant le nom d'utilisateur, le secret et la date d'expiration. Nous devons définir le **SECRET** et la **EXPIRATION_DATE** maintenant.

<script src="https://gist.github.com/yigiterinc/9c612aaeb05234f4b89caf4204942a1e.js"></script>

Nous créons une classe pour être un conteneur pour nos constantes. Vous pouvez définir le secret comme vous le souhaitez, mais la meilleure pratique est de rendre la clé secrète aussi longue que votre hachage. Nous utilisons l'algorithme **HS256** dans cet exemple, donc notre clé secrète est de 256 bits/32 caractères.

Le temps d'expiration est défini à 15 minutes, car c'est la meilleure pratique contre les attaques par force brute de la clé secrète. Le temps est en millisecondes.

Nous avons préparé notre filtre d'authentification, mais il n'est pas encore actif. Nous avons également besoin d'un filtre d'autorisation, puis nous les appliquerons tous les deux via une classe de configuration.

Ce filtre vérifie l'existence et la validité du token d'accès dans l'en-tête Authorization. Nous spécifierons quels points de terminaison seront soumis à ce filtre dans notre classe de configuration.

### Filtre d'autorisation

<script src="https://gist.github.com/yigiterinc/353558bb33a0d4bfb37c054bf3ef2abf.js"></script>

La méthode **doFilterInternal** intercepte les requêtes puis vérifie l'en-tête Authorization. Si l'en-tête n'est pas présent ou ne commence pas par "BEARER", il procède à la chaîne de filtres.

Si l'en-tête est présent, la méthode **getAuthentication** est invoquée. **getAuthentication** vérifie le JWT, et si le token est valide, il retourne un token d'accès que Spring utilisera en interne.

Ce nouveau token est ensuite sauvegardé dans SecurityContext. Vous pouvez également passer des autorités à ce token si vous en avez besoin pour une autorisation basée sur les rôles.

Nos filtres sont prêts, et maintenant nous devons les mettre en action avec l'aide d'une classe de configuration.

### Configuration

<script src="https://gist.github.com/yigiterinc/5aed60bcf1c53b34ed6b6e887158bbc0.js"></script>

Nous annotons cette classe avec **@EnableWebSecurity** et étendons **WebSecurityConfigureAdapter** pour implémenter notre logique de sécurité personnalisée.

Nous injectons automatiquement le bean BCrypt que nous avons défini précédemment. Nous injectons également le **UserDetailsService** pour trouver le compte de l'utilisateur.

La méthode la plus importante est celle qui accepte un objet **HttpSecurity**. Ici, nous spécifions les points de terminaison sécurisés et les filtres que nous voulons appliquer. Nous configurons CORS, puis nous autorisons toutes les requêtes post à notre URL d'inscription que nous avons définie dans la classe des constantes.

Vous pouvez ajouter d'autres ant matchers pour filtrer en fonction des motifs d'URL et des rôles, et vous pouvez [consulter](https://stackoverflow.com/questions/44067650/spring-security-role-based-access) cette question StackOverflow pour des exemples à ce sujet. L'autre méthode configure le **AuthenticationManager** pour utiliser notre objet encodeur comme encodeur de mot de passe lors de la vérification des identifiants.

### Test

Envoyons quelques requêtes pour tester si cela fonctionne correctement.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/4.png)

Ici, nous envoyons une requête GET pour accéder à une ressource protégée. Notre serveur répond avec un code 403. C'est le comportement attendu car nous n'avons pas fourni de token dans l'en-tête. Maintenant, créons un utilisateur :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/5.png)

Pour créer un utilisateur, nous envoyons une requête post avec nos données DTO d'utilisateur. Nous utiliserons cet utilisateur pour nous connecter et obtenir un token d'accès.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/6.png)

Super ! Nous avons obtenu le token. Après ce point, nous utiliserons ce token pour accéder aux ressources protégées.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/7.png)

Nous fournissons le token dans l'en-tête Authorization et nous sommes maintenant autorisés à accéder à notre point de terminaison protégé.

## Conclusion

Dans ce tutoriel, je vous ai guidé à travers les étapes que j'ai suivies lors de l'implémentation de l'autorisation JWT et de l'authentification par mot de passe dans Spring. Nous avons également appris comment sauvegarder un utilisateur de manière sécurisée.

Merci d'avoir lu – j'espère que cela vous a été utile. Si vous êtes intéressé à lire plus de contenu comme celui-ci, n'hésitez pas à vous abonner à mon blog à l'adresse [https://erinc.io](https://erinc.io). :)