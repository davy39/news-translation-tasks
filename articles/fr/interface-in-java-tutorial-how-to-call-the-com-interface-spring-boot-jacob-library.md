---
title: 'Tutoriel de l''API COM Interface : Java Spring Boot + Bibliothèque JACOB'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-30T05:07:17.000Z'
originalURL: https://freecodecamp.org/news/interface-in-java-tutorial-how-to-call-the-com-interface-spring-boot-jacob-library
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-29-at-15.49.33.png
tags:
- name: Java
  slug: java
- name: Libraries
  slug: libraries
- name: spring-boot
  slug: spring-boot
seo_title: 'Tutoriel de l''API COM Interface : Java Spring Boot + Bibliothèque JACOB'
seo_desc: 'By Serhii Povisenko

  In this article, I will show you how to embed the JACOB library into your Spring
  Boot application. This will help you call a COM interface API via the DLL library
  in your web application.

  Also, for illustrative purposes, I will pr...'
---

Par Serhii Povisenko

Dans cet article, je vais vous montrer comment intégrer la bibliothèque [JACOB](https://sourceforge.net/projects/jacob-project/) dans votre application [Spring Boot](https://spring.io/projects/spring-boot). Cela vous aidera à appeler une [API COM interface](https://en.wikipedia.org/wiki/Component_Object_Model) via la bibliothèque [DLL](https://en.wikipedia.org/wiki/Dynamic-link_library) dans votre application web.

De plus, à des fins d'illustration, je vais fournir une description d'une API COM afin que vous puissiez construire votre application sur celle-ci. Vous pouvez trouver tous les extraits de code dans ce [dépôt GitHub](https://github.com/povisenko/jacob-within-spring-boot-2).

Mais d'abord, une petite note : chez [C the Signs](https://cthesigns.co.uk), nous avons déployé cette solution qui nous a permis de nous intégrer avec [EMIS Health](https://www.emishealth.com). Il s'agit d'un système de dossiers patients électroniques utilisé dans les soins primaires au Royaume-Uni. Pour l'intégration, nous avons utilisé leur bibliothèque DLL fournie.

L'approche que je vais vous montrer ici (sanitisée pour éviter toute fuite d'informations sensibles) a été déployée en production il y a plus de deux ans et a depuis prouvé sa durabilité.

Puisque nous avons récemment employé une toute nouvelle approche pour nous intégrer avec EMIS, l'ancien système va être arrêté dans un mois ou deux. Donc ce tutoriel est son chant du cygne. Dors, mon petit prince.

## Qu'est-ce que l'API DLL ?

Tout d'abord, commençons par une description claire de la bibliothèque DLL. Pour ce faire, j'ai préparé une courte maquette de la documentation technique originale.

Examinons-la pour voir quelles sont les trois méthodes d'une interface COM.

### Méthode InitialiseWithID

Cette méthode est une fonctionnalité de sécurité requise sur site qui nous permet d'obtenir une connexion à un serveur API avec lequel nous voulons nous intégrer via la bibliothèque.

Elle nécessite l'`AccountID` (GUID) de l'utilisateur actuel de l'API (pour accéder au serveur) et certains autres arguments d'initialisation qui sont listés ci-dessous.

Cette fonction prend également en charge une fonctionnalité d'auto-connexion. Si un client a une version connectée du système en cours d'exécution (la bibliothèque fait partie de ce système) et appelle la méthode sur le même hôte, l'API complétera automatiquement la connexion sous le compte de cet utilisateur. Ensuite, elle retournera le `SessionID` pour les appels API ultérieurs.

Sinon, le client doit continuer avec la fonction `Logon` (voir la partie suivante) en utilisant le `LoginID` retourné.

Pour appeler la fonction, utilisez le nom `InitialiseWithID` avec les arguments suivants :

|Nom | Entrée/Sortie  |  Type |  Description |  
|---|---|---|---|
|  address | Entrée  |  String |  IP du serveur d'intégration fourni |
|  AccountID |  Entrée |  String | chaîne GUID unique fournie |
| LoginID  | Sortie | String |  chaîne GUID utilisée pour l'appel de l'API Logon | 
| Error  |  Sortie | String  |  Description de l'erreur | 
| Outcome |  Sortie | Integer | -1 = Voir l'erreur<br>1 = Initialisation réussie en attente de connexion<br>2 = Impossible de se connecter au serveur en raison de l'absence du serveur ou de détails incorrects<br>3 = AccountID non correspondant<br>4 = Autologon réussi | 
| SessionID | Sortie | String  | GUID utilisé pour les interactions ultérieures (si la connexion automatique est réussie) | 

### Méthode Logon

Cette méthode détermine l'autorité de l'utilisateur. Le nom d'utilisateur ici est l'ID utilisé pour se connecter au système. Le mot de passe est le mot de passe API défini pour ce nom d'utilisateur.

Dans le scénario de succès, l'appel retourne une chaîne `SessionID` (GUID) qui doit être passée dans d'autres appels ultérieurs pour les authentifier.

Pour appeler la fonction, utilisez le nom `Logon` avec les arguments suivants :

|Nom | Entrée/Sortie  |  Type |  Description |  
|---|---|---|---|
|  LoginID | Entrée  |  String |  L'ID de connexion retourné par la méthode d'initialisation Initialise with ID |
|  username | Entrée  | String  |  nom d'utilisateur API fourni | 
|  password |  Entrée |  String | mot de passe API fourni | 
| SessionID | Sortie | String  | GUID utilisé pour les interactions ultérieures (si la connexion est réussie) | 
| Error  | Sortie | String  |  Description de l'erreur | 
| Outcome | Sortie | Integer  | -1 = Erreur technique<br>1 = Réussi<br>2 = Expiré<br>3 = Échoué<br>4 = ID de connexion invalide ou ID de connexion n'a pas accès à ce produit | 



### Méthode getMatchedUsers

Cet appel vous permet de trouver des enregistrements de données utilisateur qui correspondent à des critères spécifiques. Le terme de recherche ne peut se référer qu'à un seul champ à la fois, comme le nom de famille, le prénom ou la date de naissance.

Un appel réussi retourne une chaîne XML avec les données.

Pour appeler la fonction, utilisez le nom `getMatchedUsers` avec les arguments suivants :

|Nom | Entrée/Sortie  |  Type |  Description |  
|---|---|---|---|
|  SessionID | Entrée  |  String |  L'ID de session retourné par la méthode de connexion  |
|  MatchTerm | Entrée  | String  |  Terme de recherche | 
|  MatchedList |  Sortie |  String | XML conforme au schéma XSD correspondant fourni | 
| SessionID | Sortie | String  | GUID utilisé pour les interactions ultérieures (si la connexion est réussie) | 
| Error  | Sortie | String  |  Description de l'erreur | 
| Outcome | Sortie | Integer  | -1 = Erreur technique<br>1 =  Utilisateurs trouvés<br>2 = Accès refusé<br>3 = Aucun utilisateur| 




## Flux d'application de la bibliothèque DLL

Pour faciliter la compréhension de ce que nous voulons implémenter, j'ai décidé de créer un simple diagramme de flux.

Il décrit un scénario étape par étape de la manière dont un client web peut interagir avec notre application basée sur un serveur en utilisant son API. Il encapsule l'interaction avec la bibliothèque DLL et nous permet d'obtenir des utilisateurs hypothétiques avec le terme de correspondance fourni (critères de recherche) :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/JACOB_DLL_FLOW-5.png)
_Diagramme de flux d'application_

## Enregistrement du COM

Maintenant, apprenons comment nous pouvons accéder à la bibliothèque DLL. Pour pouvoir interagir avec une interface COM tierce, elle [doit être ajoutée au registre](https://docs.microsoft.com/en-us/windows/win32/com/registering-com-applications).

Voici ce que disent les documents :

> Le registre est une base de données système qui contient des informations sur la configuration du matériel et des logiciels du système ainsi que sur les utilisateurs du système. Tout programme basé sur Windows peut ajouter des informations au registre et lire des informations à partir du registre. Les clients recherchent dans le registre des composants intéressants à utiliser.
>
> Le registre maintient des informations sur tous les objets COM installés dans le système. Chaque fois qu'une application crée une instance d'un composant COM, le registre est consulté pour résoudre soit le CLSID soit le ProgID du composant en le chemin du fichier DLL ou EXE du serveur qui le contient.
>
> Après avoir déterminé le serveur du composant, Windows charge soit le serveur dans l'espace de processus de l'application cliente (composants in-process) soit démarre le serveur dans son propre espace de processus (serveurs locaux et distants).
>
> Le serveur crée une instance du composant et retourne au client une référence à l'une des interfaces du composant.

Pour apprendre à faire cela, la documentation officielle de Microsoft [dit](https://docs.microsoft.com/en-us/dotnet/framework/interop/registering-assemblies-with-com) :

> Vous pouvez exécuter un outil en ligne de commande appelé [Assembly Registration Tool (Regasm.exe)](https://docs.microsoft.com/en-us/dotnet/framework/tools/regasm-exe-assembly-registration-tool) pour enregistrer ou désenregistrer un assembly pour une utilisation avec COM.
>
> Regasm.exe ajoute des informations sur la classe à la base de registre système afin que les clients COM puissent utiliser la classe .NET Framework de manière transparente.
>
> La classe [RegistrationServices](https://docs.microsoft.com/en-us/dotnet/api/system.runtime.interopservices.registrationservices) fournit la fonctionnalité équivalente. Un composant géré doit être enregistré dans le registre Windows avant de pouvoir être activé à partir d'un client COM.

Assurez-vous que votre machine hôte a installé les composants `.NET Framework` requis. Après cela, vous pouvez exécuter la commande CLI suivante :

```shell
C:\Windows\Microsoft.NET\Framework\v2.0.50727\RegAsm.exe {PATH_TO_YOUR_DLL_FILE} /codebase
```

Un message s'affichera indiquant si le fichier a été enregistré avec succès. Nous sommes maintenant prêts pour l'étape suivante.

## Définition de l'épine dorsale de l'application

### DllApiService

Tout d'abord, définissons l'interface qui décrit notre bibliothèque DLL telle qu'elle est :

```java
public interface DllApiService {

    /**
     * @param accountId identifiant pour lequel nous déclenchons l'initialisation
     * @return Tuple3 des valeurs de Outcome, SessionID/LoginID, error
     * où par le premier argument vous pouvez comprendre quel est le résultat de l'appel API
     */
    Mono<Tuple3<Integer, String, String>> initialiseWithID(String accountId);

    /**
     * @param loginId  est récupéré avant d'utiliser l'appel {@link DllApiService#initialiseWithID(String)}
     * @param username
     * @param password
     * @return Tuple3 des valeurs de Outcome, SessionID, Error
     * où par le premier argument vous pouvez comprendre quel est le résultat de l'appel API
     */
    Mono<Tuple3<Integer, String, String>> logon(String loginId, String username, String password);

    /**
     * @param sessionId est récupéré avant d'utiliser soit
     *                  {@link DllApiService#initialiseWithID(String)} ou
     *                  {@link DllApiService#logon(String, String, String)} appels
     * @param matchTerm
     * @return Tuple3 des valeurs de Outcome, MatchedList, Error
     * où par le premier argument vous pouvez comprendre quel est le résultat de l'appel API
     */
    Mono<Tuple3<Integer, String, String>> getMatchedUsers(String sessionId, String matchTerm);

    enum COM_API_Method {
        InitialiseWithID, Logon, getMatchedUsers
    }
}
```

Comme vous l'aurez peut-être remarqué, toutes les méthodes correspondent à la définition de l'interface COM décrite ci-dessus, à l'exception de la fonction `initialiseWithID`.

J'ai décidé d'omettre la variable `address` dans la signature (l'IP du serveur d'intégration) et de l'injecter en tant que variable d'environnement que nous allons implémenter.

### SessionIDService Expliqué

Pour pouvoir récupérer des données en utilisant la bibliothèque, nous devons d'abord obtenir le `SessionID`.

Selon le diagramme de flux ci-dessus, cela implique d'appeler la méthode `initialiseWithID` en premier. Après cela, en fonction du résultat, nous obtiendrons soit le SessionID soit le `LoginID` à utiliser dans les appels `Logon` ultérieurs.

Donc, en gros, c'est un processus en deux étapes en coulisses. Maintenant, créons l'interface, et après cela, l'implémentation :

```java
public interface SessionIDService {

    /**
     * @param accountId identifiant pour lequel nous récupérons SessionID
     * @param username
     * @param password
     * @return Tuple3 contenant les valeurs suivantes :
     * result (Boolean), sessionId (String) et status (HTTP Status dépendant du résultat)
     */
    Mono<Tuple3<Boolean, String, HttpStatus>> getSessionId(String accountId, String username, String password);
}
```

```java
@Service
@RequiredArgsConstructor
public class SessionIDServiceImpl implements SessionIDService {

    private final DllApiService dll;

    @Override
    public Mono<Tuple3<Boolean, String, HttpStatus>> getSessionId(String accountId, String username, String password) {
        return dll.initialiseWithID(accountId)
                  .flatMap(t4 -> {
                      switch (t4.getT1()) {
                          case -1:
                              return just(of(false, t4.getT3(), SERVICE_UNAVAILABLE));

                          case 1: {

                              return dll.logon(t4.getT2(), username, password)
                                        .map(t3 -> {
                                            switch (t3.getT1()) {
                                                case -1:
                                                    return of(false, t3.getT3(), SERVICE_UNAVAILABLE);
                                                case 1:
                                                    return of(true, t3.getT2(), OK);
                                                case 2:
                                                case 4:
                                                    return of(false, t3.getT3(), FORBIDDEN);
                                                default:
                                                    return of(false, t3.getT3(), BAD_REQUEST);

                                            }
                                        });

                          }

                          case 4:
                              return just(of(true, t4.getT2(), OK));

                          default:
                              return just(of(false, t4.getT3(), BAD_REQUEST));
                      }
                  });

    }
}
```

### Façade API

L'étape suivante consiste à concevoir l'API de notre application web. Elle doit représenter et encapsuler notre interaction avec l'API COM Interface :

```java
@Configuration
public class DllApiRouter {

    @Bean
    public RouterFunction<ServerResponse> dllApiRoute(DllApiRouterHandler handler) {
        return RouterFunctions.route(GET("/api/sessions/{accountId}"), handler::sessionId)
                              .andRoute(GET("/api/users/{matchTerm}"), handler::matchedUsers);
    }
}
```

Outre la classe `Router`, définissons une implémentation de son gestionnaire avec la logique de récupération du SessionID et des données d'enregistrements utilisateur.

Pour le deuxième scénario, afin de pouvoir effectuer un appel API DLL `getMatchedUsers` selon la conception, utilisons l'en-tête obligatoire `X-SESSION-ID` :

```java
@Slf4j
@Component
@RequiredArgsConstructor
public class DllApiRouterHandler {

    private static final String SESSION_ID_HDR = "X-SESSION-ID";

    private final DllApiService service;
    private final AccountRepo accountRepo;
    private final SessionIDService sessionService;

    public Mono<ServerResponse> sessionId(ServerRequest request) {
        final String accountId = request.pathVariable("accountId");

        return accountRepo.findById(accountId)
                          .flatMap(acc -> sessionService.getSessionId(accountId, acc.getApiUsername(), acc.getApiPassword()))
                          .doOnEach(logNext(t3 -> {
                              if (t3.getT1()) {
                                  log.info(format("SessionId à retourner %s", t3.getT2()));
                              } else {
                                  log.warn(format("Session Id n'a pas pu être récupéré. Cause : %s", t3.getT2()));
                              }
                          }))
                          .flatMap(t3 -> status(t3.getT3()).contentType(APPLICATION_JSON)
                                                           .bodyValue(t3.getT1() ? t3.getT2() : Response.error(t3.getT2())))

                          .switchIfEmpty(Mono.just("Account could not be found with provided ID " + accountId)
                                             .doOnEach(logNext(log::info))
                                             .flatMap(msg -> badRequest().bodyValue(Response.error(msg))));
    }

    public Mono<ServerResponse> matchedUsers(ServerRequest request) {

        return sessionIdHeader(request).map(sId -> Tuples.of(sId, request.queryParam("matchTerm")
                                                                         .orElseThrow(() -> new IllegalArgumentException(
                                                                                 "matchTerm query param should be specified"))))
                                       .flatMap(t2 -> service.getMatchedUsers(t2.getT1(), t2.getT2()))
                                       .flatMap(this::handleT3)
                                       .onErrorResume(IllegalArgumentException.class, this::handleIllegalArgumentException);

    }

    private Mono<String> sessionIdHeader(ServerRequest request) {
        return Mono.justOrEmpty(request.headers()
                                       .header(SESSION_ID_HDR)
                                       .stream()
                                       .findFirst()
                                       .orElseThrow(() -> new IllegalArgumentException(SESSION_ID_HDR + " header is mandatory")));
    }

    private Mono<ServerResponse> handleT3(Tuple3<Integer, String, String> t3) {
        switch (t3.getT1()) {
            case 1:
                return ok().contentType(APPLICATION_JSON)
                           .bodyValue(t3.getT2());
            case 2:
                return status(FORBIDDEN).contentType(APPLICATION_JSON)
                                        .bodyValue(Response.error(t3.getT3()));
            default:
                return badRequest().contentType(APPLICATION_JSON)
                                   .bodyValue(Response.error(t3.getT3()));
        }
    }

    private Mono<ServerResponse> handleIllegalArgumentException(IllegalArgumentException e) {
        return Mono.just(Response.error(e.getMessage()))
                   .doOnEach(logNext(res -> log.info(String.join(",", res.getErrors()))))
                   .flatMap(res -> badRequest().contentType(MediaType.APPLICATION_JSON)
                                               .bodyValue(res));
    }

    @Getter
    @Setter
    @NoArgsConstructor
    public static class Response implements Serializable {

        private String message;

        private Set<String> errors;

        private Response(Set<String> errors) {
            this.errors = errors;
        }

        public static Response error(String error) {
            return new Response(singleton(error));
        }
    }
}
```

### Entité Account

Comme vous l'aurez peut-être remarqué, nous avons importé `AccountRepo` dans le gestionnaire du routeur pour trouver l'entité dans une base de données par l'`accountId` fourni. Cela nous permet d'obtenir les informations d'identification de l'utilisateur API correspondant et d'utiliser les trois dans l'appel API DLL `Logon`.

Pour avoir une image plus claire, définissons également l'entité gérée `Account` :

```java
@TypeAlias("Account")
@Document(collection = "accounts")
public class Account {

    @Version
    private Long version;

    /**
     * ID de compte unique pour l'API, fourni par le fournisseur
     * définit la restriction pour la visibilité du domaine de données
     * c'est-à-dire que les données d'un compte ne sont pas visibles pour un autre
     */
    @Id
    private String accountId;

    /**
     * Nom d'utilisateur de l'API COM, fourni par le fournisseur
     */
    private String apiUsername;

    /**
     * Mot de passe de l'API COM, fourni par le fournisseur
     */
    private String apiPassword;


    @CreatedDate
    private Date createdAt;

    @LastModifiedDate
    private Date updatedOn;
}
```

## Configuration de la bibliothèque JACOB

Toutes les parties de notre application sont prêtes maintenant, à l'exception du cœur - la configuration et l'utilisation de la bibliothèque JACOB. Commençons par configurer la bibliothèque.

La bibliothèque est distribuée via [sourceforge.net](https://sourceforge.net/projects/jacob-project/). Je ne l'ai pas trouvée disponible ailleurs, ni sur le Central Maven Repo ni sur d'autres dépôts en ligne. J'ai donc décidé de l'importer manuellement dans notre projet en tant que package local.

Pour ce faire, je l'ai téléchargée et je l'ai placée dans le dossier racine sous `/libs/jacob-1.19`.

Après cela, placez la configuration suivante du [maven-install-plugin](https://maven.apache.org/plugins/maven-install-plugin/) dans `pom.xml`. Cela ajoutera la bibliothèque au dépôt local pendant la phase de construction `install` de Maven :

```xml
<plugin>
   <groupId>org.apache.maven.plugins</groupId>
   <artifactId>maven-install-plugin</artifactId>
   <executions>
      <execution>
         <id>install-jacob</id>
         <phase>validate</phase>
         <configuration>
            <file>${basedir}/libs/jacob-1.19/jacob.jar</file>
            <repositoryLayout>default</repositoryLayout>
            <groupId>net.sf.jacob-project</groupId>
            <artifactId>jacob</artifactId>
            <version>1.19</version>
            <packaging>jar</packaging>
            <generatePom>true</generatePom>
         </configuration>
         <goals>
            <goal>install-file</goal>
         </goals>
      </execution>
   </executions>
</plugin>
```

Cela vous permettra d'ajouter facilement la dépendance comme d'habitude :

```xml
<dependency>
   <groupId>net.sf.jacob-project</groupId>
   <artifactId>jacob</artifactId>
   <version>1.19</version>
</dependency>
```

L'importation de la bibliothèque est terminée. Maintenant, préparons-la pour l'utiliser.

Pour interagir avec le composant COM, JACOB fournit un wrapper appelé classe `ActiveXComponent` (comme je l'ai mentionné précédemment).

Il a une méthode appelée `invoke(String function, Variant... args)` qui nous permet de faire exactement ce que nous voulons.

En général, notre bibliothèque est configurée pour créer le bean `ActiveXComponent` afin que nous puissions l'utiliser où nous voulons dans l'application (et nous le voulons dans l'implémentation de `DllApiService`).

Définissons donc une configuration Spring `@Configuration` séparée avec toutes les préparations essentielles :

```java
@Slf4j
@Configuration
public class JacobCOMConfiguration {

    private static final String COM_INTERFACE_NAME = "NOM_DE_L_INTERFACE_COM_COMME_DANS_LE_REGISTRE";
    
    private static final String JACOB_LIB_PATH = System.getProperty("user.dir") + "\\libs\\jacob-1.19";
    private static final String LIB_FILE = System.getProperty("os.arch")
                                                 .equals("amd64") ? "\\jacob-1.19-x64.dll" : "\\jacob-1.19-x86.dll";

    private File temporaryDll;

    static {
        log.info("Chemin de la bibliothèque JACOB : {}", JACOB_LIB_PATH);
        log.info("Chemin du fichier de la bibliothèque JACOB : {}", JACOB_LIB_PATH + LIB_FILE);
        System.setProperty("java.library.path", JACOB_LIB_PATH);
        System.setProperty("com.jacob.debug", "true");
    }

    @PostConstruct
    public void init() throws IOException {
        InputStream inputStream = new FileInputStream(JACOB_LIB_PATH + LIB_FILE);

        temporaryDll = File.createTempFile("jacob", ".dll");
        FileOutputStream outputStream = new FileOutputStream(temporaryDll);
        byte[] array = new byte[8192];
        for (int i = inputStream.read(array); i != -1; i = inputStream.read(array)) {
            outputStream.write(array, 0, i);
        }
        outputStream.close();

        System.setProperty(LibraryLoader.JACOB_DLL_PATH, temporaryDll.getAbsolutePath());
        LibraryLoader.loadJacobLibrary();
        log.info("La bibliothèque JACOB est chargée et prête à être utilisée");
    }

    @Bean
    public ActiveXComponent dllAPI() {
        ActiveXComponent activeXComponent = new ActiveXComponent(COM_INTERFACE_NAME);
        log.info("L'interface COM de l'API {} enveloppée dans ActiveXComponent est créée et prête à être utilisée", COM_INTERFACE_NAME);
        return activeXComponent;
    }

    @PreDestroy
    public void clean() {
        temporaryDll.deleteOnExit();
        log.info("La bibliothèque DLL de l'API temporaire est nettoyée à la sortie");
    }
}
```

Il est important de mentionner que, outre la définition du bean, nous initialisons les composants de la bibliothèque en fonction de l'ISA (architecture de jeu d'instructions) de la machine hôte.

De plus, nous suivons certaines recommandations courantes pour faire une copie du fichier correspondant de la bibliothèque. Cela évite toute corruption potentielle du fichier original pendant l'exécution. Nous devons également nettoyer toutes les ressources allouées lorsque l'application se termine.

La bibliothèque est maintenant configurée et prête à être utilisée. Enfin, nous pouvons implémenter notre dernier composant principal qui nous aide à interagir avec l'API DLL : `DllApiServiceImpl`.

## Comment implémenter un service d'API de bibliothèque DLL

Comme tous les appels API COM vont être préparés en utilisant une approche commune, implémentons d'abord `InitialiseWithID`. Après cela, toutes les autres méthodes peuvent être implémentées facilement de manière similaire.

Comme je l'ai mentionné précédemment, pour interagir avec l'interface COM, JACOB nous fournit la classe `ActiveXComponent` qui a la méthode `invoke(String function, Variant... args)`.

Si vous voulez en savoir plus sur la classe `Variant`, la documentation JACOB dit ce qui suit (vous pouvez la trouver dans les [archives](https://sourceforge.net/projects/jacob-project/) ou sous `/libs/jacob-1.19` dans le [projet](https://github.com/povisenko/jacob-within-spring-boot-2)) :

> Le type de données multi-format utilisé pour tous les retours d'appel et la plupart des communications entre Java et COM. Il fournit une seule classe qui peut gérer tous les types de données.

Cela signifie que tous les arguments définis dans la signature `InitialiseWithID` doivent être enveloppés avec `new Variant(java.lang.Object in)` et passés à la méthode `invoke`. Utilisez le même ordre que spécifié dans la description de l'interface au début de cet article.

La seule autre chose importante que nous n'avons pas encore abordée est comment distinguer les arguments de type `in` et `out`.

À cette fin, `Variant` fournit un constructeur qui accepte l'objet de données et des informations sur le fait que cela est par référence ou non. Cela signifie qu'après l'appel de `invoke`, toutes les variantes qui ont été initialisées en tant que références peuvent être accessibles après l'appel. Nous pouvons donc extraire les résultats des arguments `out`.

Pour ce faire, il suffit de passer une variable booléenne supplémentaire au constructeur en tant que deuxième paramètre : `new Variant(java.lang.Object pValueObject, boolean fByRef)`.

L'initialisation de l'objet `Variant` en tant que référence impose une exigence supplémentaire au client de décider quand libérer la valeur (afin qu'elle puisse être supprimée par le garbage collector).

À cette fin, vous avez la méthode `safeRelease()` qui est censée être appelée lorsque la valeur est prise de l'objet `Variant` correspondant.

En mettant tous les morceaux ensemble, nous obtenons l'implémentation suivante du service :

```java
@RequiredArgsConstructor
public class DllApiServiceImpl implements DllApiService {

    @Value("${DLL_API_ADDRESS}")
    private String address;

    private final ActiveXComponent dll;

    @Override
    public Mono<Tuple3<Integer, String, String>> initialiseWithID(final String accountId) {

        return Mono.just(format("Appel de %s(%s, %s, %s, %s, %s, %s)",//
                                InitialiseWithID, address, accountId, "loginId/sortie", "error/sortie", "outcome/sortie", "sessionId/sortie"))
                   .doOnEach(logNext(log::info))
                   //appeler la méthode de l'interface COM et extraire le résultat en le mappant sur la classe interne *Out correspondante
                   .map(msg -> invoke(InitialiseWithID, vars -> InitialiseWithIDOut.builder()
                                                                                   .loginId(vars[3].toString())
                                                                                   .error(vars[4].toString())
                                                                                   .outcome(valueOf(vars[5].toString()))
                                                                                   .sessionId(vars[6].toString())
                                                                                   .build(), //
                                      new Variant(address), new Variant(accountId), initRef(), initRef(), initRef(), initRef()))
                   //Gérer la réponse selon la documentation
                   .map(out -> {

                       final String errorVal;

                       switch (out.outcome) {
                           case 2:
                               errorVal = "L'appel de la méthode InitialiseWithID a échoué. Résultat de la requête de l'API DLL (code de réponse du serveur via DLL) = 2 " +//
                                       "(Impossible de se connecter au serveur en raison de l'absence du serveur ou de détails incorrects)";
                               break;
                           case 3:
                               errorVal = "L'appel de la méthode InitialiseWithID a échoué. Résultat de la requête de l'API DLL (code de réponse du serveur via DLL) = 3 (AccountID non correspondant)";
                               break;
                           default:
                               errorVal = handleOutcome(out.outcome, out.error, InitialiseWithID);
                       }

                       return of(out, errorVal);
                   })
                   .doOnEach(logNext(t2 -> {
                       InitialiseWithIDOut out = t2.getT1();
                       log.info("Résultat de l'appel de l'API {}:\noutcome: {}\nsessionId: {}\nerror: {}\nloginId: {}",//
                                InitialiseWithID, out.outcome, out.sessionId, t2.getT2(), out.loginId);
                   }))
                   .map(t2 -> {
                       InitialiseWithIDOut out = t2.getT1();
                       //out.outcome == 4 auto-login réussi, SessionID est récupéré
                       return of(out.outcome, out.outcome == 4 ? out.sessionId : out.loginId, t2.getT2());
                   });
    }

    private static Variant initRef() {
        return new Variant("", true);
    }

    private static String handleOutcome(Integer outcome, String error, COM_API_Method method) {
        switch (outcome) {
            case 1:
                return "pas d'erreur";
            case 2:
                return format("%s appel de méthode échoué. Résultat de la requête de l'API DLL (code de réponse du serveur via DLL) = 2 (Accès refusé)", method);
            default:
                return format("%s appel de méthode échoué. Résultat de la requête de l'API DLL (code de réponse du serveur via DLL) = %s (erreur technique du serveur). " + //
                                      "L'API DLL est temporairement indisponible (le serveur derrière est hors service), %s", method, outcome, error);
        }

    }

    /**
     * @param method     à appeler dans l'interface COM
     * @param returnFunc mappe le tableau Variants (références) sur l'objet résultat qui doit être retourné par la méthode
     * @param vars       arguments requis pour appeler la méthode de l'interface COM
     * @param <T>        type de l'objet résultat qui doit être retourné par la méthode
     * @return résultat de l'invocation de la méthode de l'API COM au format défini
     */
    private <T extends Out> T invoke(COM_API_Method method, Function<Variant[], T> returnFunc, Variant... vars) {
        dll.invoke(method.name(), vars);
        T res = returnFunc.apply(vars);
        asList(vars).forEach(Variant::safeRelease);
        return res;
    }

    @SuperBuilder
    private static abstract class Out {
        final Integer outcome;
        final String error;
    }

    @SuperBuilder
    private static class InitialiseWithIDOut extends Out {
        final String loginId;
        final String sessionId;
}
```

Les deux autres méthodes, `Logon` et `getMatchedUsers`, sont implémentées de manière similaire. Vous pouvez vous référer à mon [dépôt GitHub](https://github.com/povisenko/jacob-within-spring-boot-2/blob/master/src/main/java/me/povisenko/jacob_within_spring_boot_2/services/impl/DllApiServiceImpl.java) pour une version complète du service si vous souhaitez le vérifier.

## Félicitations – Vous avez appris quelques choses

Nous avons passé en revue un scénario étape par étape qui nous a montré comment une API COM hypothétique pourrait être distribuée et appelée en Java.

Nous avons également appris comment la bibliothèque JACOB peut être configurée et utilisée efficacement pour interagir avec une bibliothèque DDL au sein de votre application Spring Boot 2.

Une petite amélioration serait de mettre en cache le SessionID récupéré, ce qui pourrait améliorer le flux général. Mais cela est un peu en dehors du cadre de cet article.

Si vous souhaitez approfondir, vous pouvez trouver cela sur GitHub où il est implémenté en utilisant le mécanisme de mise en cache de Spring.

J'espère que vous avez apprécié de tout parcourir avec moi et que vous avez trouvé ce tutoriel utile !