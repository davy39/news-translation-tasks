---
title: How to configure multiple Camel Contexts in the Spring Boot application
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-03T14:58:57.000Z'
originalURL: https://freecodecamp.org/news/configure-multiple-camel-context-in-spring-boot-application-d3a16396266
coverImage: https://cdn-media-1.freecodecamp.org/images/1*m8J5vJ2sbNFiHN0eC9P3cw.jpeg
tags:
- name: coding
  slug: coding
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Shashank Sharma

  This article will assume you are already familiar with Apache Camel & Spring Boot,
  which their documentation describe as:

  Apache Camel is an open source framework for message-oriented middleware with a
  rule-based routing and mediat...'
---

By Shashank Sharma

This article will assume you are already familiar with Apache Camel & Spring Boot, which their documentation describe as:

**Apache Camel** is an [open source](https://en.wikipedia.org/wiki/Open_source) [framework](https://en.wikipedia.org/wiki/Framework-oriented_design) for [message-oriented middleware](https://en.wikipedia.org/wiki/Message-oriented_middleware) with a rule-based routing and [mediation](https://en.wikipedia.org/wiki/Data_mediation) engine. It provides a [Java object](https://en.wikipedia.org/wiki/Plain_Old_Java_Object)-based implementation of the [Enterprise Integration Patterns](https://en.wikipedia.org/wiki/Enterprise_Integration_Patterns) using an [application programming interface](https://en.wikipedia.org/wiki/Application_programming_interface) (or declarative Java [domain-specific language](https://en.wikipedia.org/wiki/Domain-specific_language)) to configure routing and mediation rules.

The domain-specific language means that Apache Camel can support type-safe smart completion of routing rules in an [integrated development environment](https://en.wikipedia.org/wiki/Integrated_development_environment) using regular Java code without large amounts of [XML](https://en.wikipedia.org/wiki/XML) configuration files. Although XML configuration inside [Spring Framework](https://en.wikipedia.org/wiki/Spring_Framework) is also supported.

**Spring Boot** is the starting point for building all Spring-based applications. Spring Boot is designed to get you up and running as quickly as possible, with minimal upfront configuration of Spring. Spring Boot makes it easy to create stand-alone, production-grade Spring-based Applications that you can run.

### The problem at hand

You are designing a platform which enables end users to create multiple apps in your system. Each app can have it’s own Camel routes or can reuse predefined routes. The problem is how to ensure that one app Camel route doesn’t collide with other app routes.

One way to solve this problem is to ensure routes are always uniquely named. But this is hard to enforce and even harder if end users can define their own routes. A neat solution is to create separate Camel Contexts for each app. It’s easier to manage. There are [multiple](http://www.baeldung.com/apache-camel-spring-boot) [articles](https://dzone.com/articles/working-with-object-store-in-mule-part-1) on how to configure Apache Camel with Spring Boot application, but none on how to configure multiple Camel Contexts at runtime.

First exclude _CamelAutoConfiguration_ from Spring Boot Application. Instead of _CamelContext_ created by Spring Auto Configuration, we will create _CamelContext_ as and when required.

```
@SpringBootApplication@EnableAutoConfiguration(exclude = {CamelAutoConfiguration.class})public class Application {
```

```
  public static void main(String[] args) {    SpringApplication.run(Application.class, args);  }
```

```
}
```

To handle all Apache Camel configuration and to reuse the Spring properties, create _CamelConfig_ Class.

```
@Configuration@EnableConfigurationProperties(CamelConfigurationProperties.class)@Import(TypeConversionConfiguration.class)public class CamelConfig {
```

```
  @Autowired  private ApplicationContext applicationContext;
```

```
  @Bean  @ConditionalOnMissingBean(RoutesCollector.class)  RoutesCollector routesCollector(ApplicationContext          applicationContext, CamelConfigurationProperties config) {
```

```
    Collection<CamelContextConfiguration> configurations = applicationContext.getBeansOfType(CamelContextConfiguration.class).values();
```

```
    return new RoutesCollector(applicationContext, new ArrayList<CamelContextConfiguration>(configurations), config);  }
```

```
  /**  * Camel post processor - required to support Camel annotations.  */  @Bean  CamelBeanPostProcessor camelBeanPostProcessor(ApplicationContext applicationContext) {    CamelBeanPostProcessor processor = new CamelBeanPostProcessor();    processor.setApplicationContext(applicationContext);    return processor;  }
```

```
}
```

To create and manage _CamelContext,_ create class _CamelContextHandler_.

```
@Componentpublic class CamelContextHandler implements BeanFactoryAware {
```

```
  private BeanFactory beanFactory;
```

```
  @Autowired  private ApplicationContext applicationContext;
```

```
  @Autowired  private CamelConfigurationProperties camelConfigurationProperties;
```

```
  /*  * (non-Javadoc)  *  * @see  * org.springframework.beans.factory.BeanFactoryAware  * #setBeanFactory(org.springframework.beans.  * factory.BeanFactory)  */  @Override  public void setBeanFactory(BeanFactory beanFactory) {    this.beanFactory = beanFactory;  }
```

```
  public boolean camelContextExist(int id) {    String name = "camelContext" + id;    return applicationContext.containsBean(name);  }
```

```
  public CamelContext getCamelContext(int id) {    CamelContext camelContext = null;    String name = "camelContext" + id;    if (applicationContext.containsBean(name)) {           camelContext = applicationContext.getBean(name, SpringCamelContext.class);    } else {       camelContext = camelContext(name);    }    return camelContext;  }
```

```
  private CamelContext camelContext(String contextName) {    CamelContext camelContext = new SpringCamelContext(applicationContext);    SpringCamelContext.setNoStart(true);    if (!camelConfigurationProperties.isJmxEnabled()) {      camelContext.disableJMX();    }
```

```
    if (contextName != null) {      ((SpringCamelContext) camelContext).setName(contextName);    }
```

```
    if (camelConfigurationProperties.getLogDebugMaxChars() > 0) {     camelContext.getProperties().put( Exchange.LOG_DEBUG_BODY_MAX_CHARS, "" + camelConfigurationProperties.getLogDebugMaxChars());
```

```
    }
```

```
    camelContext.setStreamCaching( camelConfigurationProperties.isStreamCaching());
```

```
    camelContext.setTracing( camelConfigurationProperties.isTracing());
```

```
    camelContext.setMessageHistory( camelConfigurationProperties.isMessageHistory());
```

```
    camelContext.setHandleFault( camelConfigurationProperties.isHandleFault());
```

```
    camelContext.setAutoStartup( camelConfigurationProperties.isAutoStartup());
```

```
camelContext.setAllowUseOriginalMessage(camelConfigurationProperties.isAllowUseOriginalMessage());
```

```
    if (camelContext.getManagementStrategy().getManagementAgent() != null) {      camelContext.getManagementStrategy().getManagementAgent().setEndpointRuntimeStatisticsEnabled(camelConfigurationProperties.isEndpointRuntimeStatisticsEnabled());
```

```
      camelContext.getManagementStrategy().getManagementAgent().setStatisticsLevel(camelConfigurationProperties.getJmxManagementStatisticsLevel());
```

```
      camelContext.getManagementStrategy().getManagementAgent().setManagementNamePattern(camelConfigurationProperties.getJmxManagementNamePattern());
```

```
      camelContext.getManagementStrategy().getManagementAgent().setCreateConnector(camelConfigurationProperties.isJmxCreateConnector());
```

```
    }
```

```
    ConfigurableBeanFactory configurableBeanFactory = (ConfigurableBeanFactory) beanFactory;    configurableBeanFactory.registerSingleton(contextName, camelContext);
```

```
    try {      camelContext.start();    } catch (Exception e) {      // Log error    }    return camelContext;  }
```

```
}
```

Now instead of autowiring _CamelContext_, autowire _CamelContextHandler_. _CamelContextHandler#getCamelContext_ will return _CamelContext_ based on its ID (where ID is the unique identifier of different apps). If there isn’t existing context for that ID, _CamelContextHandler#getCamelContext_ will create _CamelContext_ for that ID and return.

To prevent unnecessary creation of _CamelContext,_ we can define a helper function in _CamelContextHandler_ which can be called before calling _getCamelContext_ to check if context exists for that ID.

```
public boolean camelContextExist(int id) {  String name = "camelContext" + id;  return applicationContext.containsBean(name);}
```

You use the same way to load routes, and you will use _CamelContextHandler#getCamelContext_ to get the context. Let’s assume your routes are stored in the database. And each of the routes are associated with some app ID. To load routes, we can define a method like:

```
public void loadRoutes(String id) {  String routestr  = fetchFromDB(id);  if (routestr != null && !routestr.isEmpty()) {    try {      RoutesDefinition routes = camelContext.loadRoutesDefinition(IOUtils.toInputStream(routestr, "UTF-8"));
```

```
      getCamelContext(id).addRouteDefinitions(routes.getRoutes());
```

```
    } catch (Exception e) {      // Log error    }  }}
```

And to load routes at server startup which are already present in database we can use @PostConstruct annotation from Spring.

```
@PostConstructpublic void afterPropertiesSet() {  List<String> appIds = getAllEnabledApps();  appIds.forEach(id -> loadRoutes(id));}
```

As _CamelContext_ objects are not created through Spring, Spring will not handle the lifecycle of these _CamelContext_ beans. To stop all context when application stops, we can define _closeContext_ method in the _CamelConfig_ class to close all _CamelContext_ gracefully.

```
@PreDestroyvoid closeContext() {  applicationContext.getBeansOfType(CamelContext.class).values() .forEach(camelContext -> {    try {      camelContext.stop();    } catch (Exception e) {      //Log error    }  });}
```

The above setup can help you run multiple Camel Contexts in a Spring Boot Application. If you have any questions or suggestions, feel free to write. Cheers.

[Other articles by Shashank Sh.](https://medium.com/@sharmasha2nk)

