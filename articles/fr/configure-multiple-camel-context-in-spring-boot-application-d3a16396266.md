---
title: Comment configurer plusieurs contextes Camel dans une application Spring Boot
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
seo_title: Comment configurer plusieurs contextes Camel dans une application Spring
  Boot
seo_desc: 'By Shashank Sharma

  This article will assume you are already familiar with Apache Camel & Spring Boot,
  which their documentation describe as:

  Apache Camel is an open source framework for message-oriented middleware with a
  rule-based routing and mediat...'
---

Par Shashank Sharma

Cet article suppose que vous êtes déjà familiarisé avec Apache Camel & Spring Boot, que leur documentation décrit comme suit :

**Apache Camel** est un [framework](https://en.wikipedia.org/wiki/Framework-oriented_design) [open source](https://en.wikipedia.org/wiki/Open_source) pour les [intergiciels orientés messages](https://en.wikipedia.org/wiki/Message-oriented_middleware) avec un moteur de routage et de [médiation](https://en.wikipedia.org/wiki/Data_mediation) basé sur des règles. Il fournit une implémentation basée sur des [objets Java](https://en.wikipedia.org/wiki/Plain_Old_Java_Object) des [modèles d'intégration d'entreprise](https://en.wikipedia.org/wiki/Enterprise_Integration_Patterns) en utilisant une [interface de programmation d'application](https://en.wikipedia.org/wiki/Application_programming_interface) (ou un langage Java [spécifique au domaine](https://en.wikipedia.org/wiki/Domain-specific_language) déclaratif) pour configurer les règles de routage et de médiation.

Le langage spécifique au domaine signifie qu'Apache Camel peut supporter la complétion intelligente et sécurisée des règles de routage dans un [environnement de développement intégré](https://en.wikipedia.org/wiki/Integrated_development_environment) en utilisant du code Java régulier sans une grande quantité de fichiers de configuration [XML](https://en.wikipedia.org/wiki/XML). Bien que la configuration XML dans le [Spring Framework](https://en.wikipedia.org/wiki/Spring_Framework) soit également supportée.

**Spring Boot** est le point de départ pour construire toutes les applications basées sur Spring. Spring Boot est conçu pour vous faire démarrer et fonctionner aussi rapidement que possible, avec une configuration minimale de Spring. Spring Boot facilite la création d'applications Spring autonomes, de qualité production, que vous pouvez exécuter.

### Le problème à résoudre

Vous concevez une plateforme qui permet aux utilisateurs finaux de créer plusieurs applications dans votre système. Chaque application peut avoir ses propres routes Camel ou peut réutiliser des routes prédéfinies. Le problème est de s'assurer qu'une route Camel d'une application n'entre pas en collision avec les routes d'autres applications.

Une façon de résoudre ce problème est de s'assurer que les routes sont toujours nommées de manière unique. Mais cela est difficile à appliquer et encore plus difficile si les utilisateurs finaux peuvent définir leurs propres routes. Une solution élégante est de créer des contextes Camel séparés pour chaque application. C'est plus facile à gérer. Il existe [plusieurs](http://www.baeldung.com/apache-camel-spring-boot) [articles](https://dzone.com/articles/working-with-object-store-in-mule-part-1) sur la façon de configurer Apache Camel avec une application Spring Boot, mais aucun sur la façon de configurer plusieurs contextes Camel à l'exécution.

Tout d'abord, excluez _CamelAutoConfiguration_ de l'application Spring Boot. Au lieu du _CamelContext_ créé par la configuration automatique de Spring, nous créerons _CamelContext_ lorsque cela sera nécessaire.

```
@SpringBootApplication@EnableAutoConfiguration(exclude = {CamelAutoConfiguration.class})public class Application {
```

```
  public static void main(String[] args) {    SpringApplication.run(Application.class, args);  }
```

```
}
```

Pour gérer toute la configuration d'Apache Camel et réutiliser les propriétés Spring, créez la classe _CamelConfig_.

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

Pour créer et gérer _CamelContext_, créez la classe _CamelContextHandler_.

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

Maintenant, au lieu d'injecter _CamelContext_, injectez _CamelContextHandler_. _CamelContextHandler#getCamelContext_ retournera _CamelContext_ en fonction de son ID (où l'ID est l'identifiant unique des différentes applications). Si aucun contexte existant n'existe pour cet ID, _CamelContextHandler#getCamelContext_ créera un _CamelContext_ pour cet ID et le retournera.

Pour éviter la création inutile de _CamelContext_, nous pouvons définir une fonction d'assistance dans _CamelContextHandler_ qui peut être appelée avant d'appeler _getCamelContext_ pour vérifier si le contexte existe pour cet ID.

```
public boolean camelContextExist(int id) {  String name = "camelContext" + id;  return applicationContext.containsBean(name);}
```

Vous utilisez la même méthode pour charger les routes, et vous utiliserez _CamelContextHandler#getCamelContext_ pour obtenir le contexte. Supposons que vos routes sont stockées dans la base de données. Et chacune des routes est associée à un identifiant d'application. Pour charger les routes, nous pouvons définir une méthode comme :

```
public void loadRoutes(String id) {  String routestr  = fetchFromDB(id);  if (routestr != null && !routestr.isEmpty()) {    try {      RoutesDefinition routes = camelContext.loadRoutesDefinition(IOUtils.toInputStream(routestr, "UTF-8"));
```

```
      getCamelContext(id).addRouteDefinitions(routes.getRoutes());
```

```
    } catch (Exception e) {      // Log error    }  }}
```

Et pour charger les routes au démarrage du serveur qui sont déjà présentes dans la base de données, nous pouvons utiliser l'annotation @PostConstruct de Spring.

```
@PostConstructpublic void afterPropertiesSet() {  List<String> appIds = getAllEnabledApps();  appIds.forEach(id -> loadRoutes(id));}
```

Comme les objets _CamelContext_ ne sont pas créés via Spring, Spring ne gérera pas le cycle de vie de ces beans _CamelContext_. Pour arrêter tous les contextes lorsque l'application s'arrête, nous pouvons définir la méthode _closeContext_ dans la classe _CamelConfig_ pour fermer tous les _CamelContext_ de manière élégante.

```
@PreDestroyvoid closeContext() {  applicationContext.getBeansOfType(CamelContext.class).values() .forEach(camelContext -> {    try {      camelContext.stop();    } catch (Exception e) {      //Log error    }  });}
```

La configuration ci-dessus peut vous aider à exécuter plusieurs contextes Camel dans une application Spring Boot. Si vous avez des questions ou des suggestions, n'hésitez pas à écrire. À votre santé.

[Autres articles de Shashank Sh.](https://medium.com/@sharmasha2nk)