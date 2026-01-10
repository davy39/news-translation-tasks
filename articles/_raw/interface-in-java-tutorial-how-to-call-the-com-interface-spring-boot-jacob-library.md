---
title: 'COM Interface API Tutorial: Java Spring Boot + JACOB Library'
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
seo_title: null
seo_desc: 'By Serhii Povisenko

  In this article, I will show you how to embed the JACOB library into your Spring
  Boot application. This will help you call a COM interface API via the DLL library
  in your web application.

  Also, for illustrative purposes, I will pr...'
---

By Serhii Povisenko

In this article, I will show you how to embed the [JACOB library](https://sourceforge.net/projects/jacob-project/) into your [Spring Boot](https://spring.io/projects/spring-boot) application. This will help you call a [COM interface API](https://en.wikipedia.org/wiki/Component_Object_Model) via the [DLL](https://en.wikipedia.org/wiki/Dynamic-link_library) library in your web application.

Also, for illustrative purposes, I will provide a description of a COM API so you can build your application on top of it. You can find all the code snippets in this [GitHub repo](https://github.com/povisenko/jacob-within-spring-boot-2).

But first, a quick note: at [C the Signs](https://cthesigns.co.uk) we deployed this solution that allowed us to integrate with [EMIS Health](https://www.emishealth.com). It is an electronic patient record system used in primary care in the United Kingdom. For integration we used their provided DLL library.

The approach that I'll show you here (sanitised to avoid leaking any sensitive information) rolled out to production more than two years ago, and has since proven its durability.

Since we recently employed a brand new approach to integrating with EMIS, the old system is going to be shut down in a month or two. So this tutorial is its swan song. Sleep, my little prince.

## What is the DLL API?

First, let's start with a clear description of the DLL library. To do this, I prepared a short mock-up of the original technical documentation.

Let's take a look through it to see what the three methods of a COM interface are.

### InitialiseWithID Method

This method is a security feature required on-site that lets us obtain a connection to an API server that we want to integrate with the library.

It requires the `AccountID` (GUID) of the current API user (to access the server) and some other initialization arguments that are listed below.

This function also supports an auto-login feature. If a client has a logged-in version of the running system (the library is a part of that system) and calls the method on the same host, the API will automatically complete the login under that user's account. Then it'll return the `SessionID` for subsequent API calls. 

Otherwise, the client needs to continue with the `Logon` function (see the next part) using the returned `LoginID`.

To call the function, use the name `InitialiseWithID` with the following arguments:

|Name | In/out  |  Type |  Description |  
|---|---|---|---|
|  address | In  |  String |  provided integration server IP |
|  AccountID |  In |  String | provided unique GUID string |
| LoginID  | Out | String |  GUID string used for Logon API call | 
| Error  |  Out | String  |  Error description | 
| Outcome |  Out | Integer | -1 = Refer to error<br>1 = Successful initialise awaiting logon<br>2 = Unable to connect to server due to absent server, or incorrect details<br>3 = Unmatched AccountID<br>4 = Autologon successful | 
| SessionID | Out | String  | GUID used for subsequent interactions (if auto log in successful) | 

### Logon Method

This method determines the authority of the user. The username here is the ID used to log in to the system. The password is the API password set for that username. 

In the success scenario, the call returns a `SessionID` string (GUID) that must be passed into other subsequent calls to authenticate them.

To call the function, use the name `Logon` with the following arguments:

|Name | In/out  |  Type |  Description |  
|---|---|---|---|
|  LoginID | In  |  String |  The login id returned by the initialization method Initialise with ID |
|  username | In  | String  |  provided API username | 
|  password |  In |  String | provided API password | 
| SessionID | Out | String  | GUID used for subsequent interactions (if logon successful) | 
| Error  | Out  | String  |  Error description | 
| Outcome | Out  | Integer  | -1 = Technical error<br>1 = Successful<br>2 = Expired<br>3 = Unsuccessful<br>4 = Invalid login ID or login ID does not have access to this product | 



### getMatchedUsers Method

This call lets you find user data records that match specific criteria. The search term can only refer to one field at a time such as last name, first name, or date of birth. 

A successful call returns an XML string with the data in it.

To call the function, use the name `getMatchedUsers` with the following arguments:

|Name | In/out  |  Type |  Description |  
|---|---|---|---|
|  SessionID | In  |  String |  The session id returned by the logon  method |
|  MatchTerm | In  | String  |  Search term | 
|  MatchedList |  Out |  String | XML conforming to provided corresponding XSD scheme | 
| SessionID | Out | String  | GUID used for subsequent interactions (if logon successful) | 
| Error  | Out  | String  |  Error description | 
| Outcome | Out  | Integer  | -1 = Technical error<br>1 =  Users found<br>2 = Access denied<br>3 = No users| 




## DLL Library Application Flow

To make it easier to grasp what we want to implement, I decided to create a simple flow diagram. 

It describes a step-by-step scenario of how a web client can interact with our server-based application using its API. It encapsulates interaction with the DLL Library and allows us to get hypothetical users with the provided match term (search criteria):

![Image](https://www.freecodecamp.org/news/content/images/2020/09/JACOB_DLL_FLOW-5.png)
_Application Flow Diagram_

## Registering COM 

Now let's learn how we can access the DLL library. To be able to interact with a 3rd party COM interface, it [needs to be added to the registry](https://docs.microsoft.com/en-us/windows/win32/com/registering-com-applications). 

Here's what the docs say:

> The registry is a system database that contains information about the configuration of system hardware and software as well as about users of the system. Any Windows-based program can add information to the registry and read information back from the registry. Clients search the registry for interesting components to use.  
>   
> The registry maintains information about all the COM objects installed in the system. Whenever an application creates an instance of a COM component, the registry is consulted to resolve either the CLSID or ProgID of the component into the pathname of the server DLL or EXE that contains it.  
>   
> After determining the component's server, Windows either loads the server into the process space of the client application (in-process components) or starts the server in its own process space (local and remote servers).  
>   
> The server creates an instance of the component and returns to the client a reference to one of the component's interfaces.

To learn how to do that, the official Microsoft documentation [says](https://docs.microsoft.com/en-us/dotnet/framework/interop/registering-assemblies-with-com):

> You can run a command-line tool called the [Assembly Registration Tool (Regasm.exe)](https://docs.microsoft.com/en-us/dotnet/framework/tools/regasm-exe-assembly-registration-tool) to register or unregister an assembly for use with COM.  
>   
> Regasm.exe adds information about the class to the system registry so COM clients can use the .NET Framework class transparently.  
>   
> The [RegistrationServices](https://docs.microsoft.com/en-us/dotnet/api/system.runtime.interopservices.registrationservices) class provides the equivalent functionality. A managed component must be registered in the Windows registry before it can be activated from a COM client

Make sure that your host machine has installed the required `.NET Framework` components. After that, you can execute the following CLI command:

```shell
C:\Windows\Microsoft.NET\Framework\v2.0.50727\RegAsm.exe {PATH_TO_YOUR_DLL_FILE} /codebase
```

A message will display indicating whether the file was successfully registered. Now we're ready for the next step.

## Defining the Backbone of the Application

### DllApiService

First of all, let's define the interface that describes our DLL library as it is:

```java
public interface DllApiService {

    /**
     * @param accountId identifier for which we trigger initialisation
     * @return Tuple3 from values of Outcome, SessionID/LoginID, error
     * where by the first argument you can understand what is the result of the API call
     */
    Mono<Tuple3<Integer, String, String>> initialiseWithID(String accountId);

    /**
     * @param loginId  is retrieved before using {@link DllApiService#initialiseWithID(String)} call
     * @param username
     * @param password
     * @return Tuple3 from values of Outcome, SessionID, Error
     * where by the first argument you can understand what is the result of the API call
     */
    Mono<Tuple3<Integer, String, String>> logon(String loginId, String username, String password);

    /**
     * @param sessionId is retrieved before using either
     *                  {@link DllApiService#initialiseWithID(String)} or
     *                  {@link DllApiService#logon(String, String, String)} calls
     * @param matchTerm
     * @return Tuple3 from values of Outcome, MatchedList, Error
     * where by the first argument you can understand what is the result of the API call
     */
    Mono<Tuple3<Integer, String, String>> getMatchedUsers(String sessionId, String matchTerm);

    enum COM_API_Method {
        InitialiseWithID, Logon, getMatchedUsers
    }
}
```

As you might have noticed, all the methods map with the definition of the COM Interface described above, except for the `initialiseWithID` function.

I decided to omit the `address` variable in the signature (the IP of the integration server) and inject it as an environment variable which we will be implementing.

### SessionIDService Explained

To be able to retrieve any data using the library, first we need to get the `SessionID`. 

According to the flow diagram above, this involves calling the `initialiseWithID` method first. After that, depending on the result, we will get either the SessionID or `LoginID` to use in subsequent `Logon` calls. 

So basically this is a two-step process behind the scenes. Now, let's create the interface, and after that, the implementation:

```java
public interface SessionIDService {

    /**
     * @param accountId identifier for which we retrieve SessionID
     * @param username
     * @param password
     * @return Tuple3 containing the following values:
     * result ( Boolean), sessionId (String) and status (HTTP Status depending on the result)
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

### API Facade

The next step is to design our web application API. It should represent and encapsulate our interaction with the COM Interface API:

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

Besides the `Router` class, let's define an implementation of its handler with logic for retrieving the SessionID and the user records data. 

For the second scenario, to be able to make a DLL `getMatchedUsers` API call according to the design, let's use the mandatory header `X-SESSION-ID`:

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
                                  log.info(format("SessionId to return %s", t3.getT2()));
                              } else {
                                  log.warn(format("Session Id could not be retrieved. Cause: %s", t3.getT2()));
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

### Account Entity

As you might have noticed, we've imported `AccountRepo` in the router's handler to find the entity in a database by the provided `accountId`. This lets us get the corresponding API user credentials and use all three in the DLL `Logon` API call. 

To get a clearer picture, let's define the managed `Account` entity as well:

```java
@TypeAlias("Account")
@Document(collection = "accounts")
public class Account {

    @Version
    private Long version;

    /**
     * unique account ID for API, provided by supplier
     * defines restriction for data domain visibility
     * i.e. data from one account is not visible for another
     */
    @Id
    private String accountId;

    /**
     * COM API username, provided by supplier
     */
    private String apiUsername;

    /**
     * COM API password, provided by supplier
     */
    private String apiPassword;


    @CreatedDate
    private Date createdAt;

    @LastModifiedDate
    private Date updatedOn;
}
```

## The JACOB Library Setup

All parts of our application are ready now except the core – the configuration and use of the JACOB library. Let's start with setting up the library.

The library is distributed via [sourceforge.net](https://sourceforge.net/projects/jacob-project/). I did not find it available anywhere on either the Central Maven Repo or any other repositories online. So I decided to import it manually into our project as a local package. 

To do that, I downloaded it and put it in the root folder under `/libs/jacob-1.19`. 

After that, put the following [maven-install-plugin](https://maven.apache.org/plugins/maven-install-plugin/) configuration into `pom.xml`. This will add the library to the local repository during Maven's `install` build phase:

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

That will let you easily add the dependency as usual:

```xml
<dependency>
   <groupId>net.sf.jacob-project</groupId>
   <artifactId>jacob</artifactId>
   <version>1.19</version>
</dependency>
```

The library import is finished. Now let's get it ready to use it.

To interact with the COM component, JACOB provides a wrapper called an `ActiveXComponent` class (as I mentioned before). 

It has a method called `invoke(String function, Variant... args)` that lets us make exactly what we want. 

Generally speaking, our library is set up to create the `ActiveXComponent` bean so we can use it anywhere we want in the app (and we want it in the implementation of `DllApiService`). 

So let's define a separate Spring `@Configuration` with all the essential preparations:

```java
@Slf4j
@Configuration
public class JacobCOMConfiguration {

    private static final String COM_INTERFACE_NAME = "NAME_OF_COM_INTERFACE_AS_IN_REGISTRY";
    
    private static final String JACOB_LIB_PATH = System.getProperty("user.dir") + "\\libs\\jacob-1.19";
    private static final String LIB_FILE = System.getProperty("os.arch")
                                                 .equals("amd64") ? "\\jacob-1.19-x64.dll" : "\\jacob-1.19-x86.dll";

    private File temporaryDll;

    static {
        log.info("JACOB lib path: {}", JACOB_LIB_PATH);
        log.info("JACOB file lib path: {}", JACOB_LIB_PATH + LIB_FILE);
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
        log.info("JACOB library is loaded and ready to use");
    }

    @Bean
    public ActiveXComponent dllAPI() {
        ActiveXComponent activeXComponent = new ActiveXComponent(COM_INTERFACE_NAME);
        log.info("API COM interface {} wrapped into ActiveXComponent is created and ready to use", COM_INTERFACE_NAME);
        return activeXComponent;
    }

    @PreDestroy
    public void clean() {
        temporaryDll.deleteOnExit();
        log.info("Temporary DLL API library is cleaned on exit");
    }
}
```

It's worth mentioning that, besides defining the bean, we initialize the library components based on the host machine's ISA (instruction set architecture).

Also, we follow some common recommendations to make a copy of the corresponding library's file. This avoids any potential corruption of the original file during runtime. We also need to cleanup all allocated resources when the applications terminates.

Now the library is set up and ready to use. Finally, we can implement our last main component that helps us interact with the DLL API:  `DllApiServiceImpl`.

## How to Implement a DLL Library API Service

As all COM API calls are going to be cooked using a common approach, let's implement `InitialiseWithID` first. After that, all other methods can be implemented easily in a similar way.

As I mentioned before, to interact with the COM interface, JACOB provides us with the `ActiveXComponent` class that has the `invoke(String function, Variant... args)` method. 

If you want to know more about the `Variant` class, the JACOB documentation says the following (you can find it in the [archive](https://sourceforge.net/projects/jacob-project/) or under `/libs/jacob-1.19` in the [project](https://github.com/povisenko/jacob-within-spring-boot-2)):

> The multi-format data type used for all call backs and most communications between Java and COM. It provides a single class that can handle all data types.

This means that all arguments defined in the `InitialiseWithID` signature should be wrapped with `new Variant(java.lang.Object in)` and passed to the `invoke` method. Use the same order as specified in the interface description at the beginning of this article.

The only other important thing we haven't touched on yet is how to distinguish `in` and `out` type arguments. 

For that purpose, `Variant` provides a constructor that accepts the data object and information about whether this is by reference or not. This means that after `invoke` is called, all variants that were initialized as references can be accessed after the call. So we can extract the results from `out` arguments. 

To do that, just pass an extra boolean variable to the constructor as the second parameter: `new Variant(java.lang.Object pValueObject, boolean fByRef)`. 

Initializing the `Variant` object as reference puts an additional requirement on the client to decide when to release the value (so it can be scrapped by the garbage collector). 

For that purpose, you have the `safeRelease()` method that is supposed to be called when the value is taken from the corresponding `Variant` object.  
  
Putting all the pieces together gives us the following service's implementation:

```java
@RequiredArgsConstructor
public class DllApiServiceImpl implements DllApiService {

    @Value("${DLL_API_ADDRESS}")
    private String address;

    private final ActiveXComponent dll;

    @Override
    public Mono<Tuple3<Integer, String, String>> initialiseWithID(final String accountId) {

        return Mono.just(format("Calling %s(%s, %s, %s, %s, %s, %s)",//
                                InitialiseWithID, address, accountId, "loginId/out", "error/out", "outcome/out", "sessionId/out"))
                   .doOnEach(logNext(log::info))
                   //invoke COM interface method and extract the result mapping it onto corresponding *Out inner class
                   .map(msg -> invoke(InitialiseWithID, vars -> InitialiseWithIDOut.builder()
                                                                                   .loginId(vars[3].toString())
                                                                                   .error(vars[4].toString())
                                                                                   .outcome(valueOf(vars[5].toString()))
                                                                                   .sessionId(vars[6].toString())
                                                                                   .build(), //
                                      new Variant(address), new Variant(accountId), initRef(), initRef(), initRef(), initRef()))
                   //Handle the response according to the documentation
                   .map(out -> {

                       final String errorVal;

                       switch (out.outcome) {
                           case 2:
                               errorVal = "InitialiseWithID method call failed. DLL API request outcome (response code from server via DLL) = 2 " +//
                                       "(Unable to connect to server due to absent server, or incorrect details)";
                               break;
                           case 3:
                               errorVal = "InitialiseWithID method call failed. DLL API request outcome (response code from server via DLLe) = 3 (Unmatched AccountID)";
                               break;
                           default:
                               errorVal = handleOutcome(out.outcome, out.error, InitialiseWithID);
                       }

                       return of(out, errorVal);
                   })
                   .doOnEach(logNext(t2 -> {
                       InitialiseWithIDOut out = t2.getT1();
                       log.info("{} API call result:\noutcome: {}\nsessionId: {}\nerror: {}\nloginId: {}",//
                                InitialiseWithID, out.outcome, out.sessionId, t2.getT2(), out.loginId);
                   }))
                   .map(t2 -> {
                       InitialiseWithIDOut out = t2.getT1();
                       //out.outcome == 4 auto-login successful, SessionID is retrieved
                       return of(out.outcome, out.outcome == 4 ? out.sessionId : out.loginId, t2.getT2());
                   });
    }

    private static Variant initRef() {
        return new Variant("", true);
    }

    private static String handleOutcome(Integer outcome, String error, COM_API_Method method) {
        switch (outcome) {
            case 1:
                return "no error";
            case 2:
                return format("%s method call failed. DLL API request outcome (response code from server via DLL) = 2 (Access denied)", method);
            default:
                return format("%s method call failed. DLL API request outcome (response code from server via DLL) = %s (server technical error). " + //
                                      "DLL API is temporary unavailable (server behind is down), %s", method, outcome, error);
        }

    }

    /**
     * @param method     to be called in COM interface
     * @param returnFunc maps Variants (references) array onto result object that is to be returned by the method
     * @param vars       arguments required for calling COM interface method
     * @param <T>        type of the result object that is to be returned by the method
     * @return result of the COM API method invocation in defined format
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

Two other methods, `Logon` and `getMatchedUsers`, are implemented accordingly. You can refer to my [GitHub](https://github.com/povisenko/jacob-within-spring-boot-2/blob/master/src/main/java/me/povisenko/jacob_within_spring_boot_2/services/impl/DllApiServiceImpl.java) repo for a complete version of the service if you want to check it out.

## Congratulations – You've Learned a Few Things

We've gone through a step by step scenario that showed us how a hypothetical COM API could be distributed and called in Java. 

We also learned how the JACOB library can be configured and effectively used to interact with a DDL library within your Spring Boot 2 application.

A small improvement would be to cache the retrieved SessionID which could improve the general flow. But that's a bit outside the scope of this article. 

If you want to investigate further, you can find that on GitHub where it's implemented using Spring's caching mechanism.

Hope you enjoyed going through everything with me and found this tutorial helpful!

