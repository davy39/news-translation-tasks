---
title: Pourquoi ignorer les exceptions en Java et comment le faire correctement
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-03T23:48:14.000Z'
originalURL: https://freecodecamp.org/news/why-you-should-ignore-exceptions-in-java-and-how-to-do-it-correctly-8e95e5775e58
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zL-r1LMISdwKu2y47rsROQ.jpeg
tags:
- name: Sneakythrow
  slug: sneakythrow
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Pourquoi ignorer les exceptions en Java et comment le faire correctement
seo_desc: 'By Rainer Hahnekamp

  In this article, I will show how to ignore checked exceptions in Java. I will start
  by describing the rationale behind it and the common pattern to resolve this issue.
  Then I will present some libraries for that purpose.

  Checked a...'
---

Par Rainer Hahnekamp

Dans cet article, je vais montrer comment ignorer les exceptions vérifiées en Java. Je commencerai par décrire la logique derrière cela et le modèle courant pour résoudre ce problème. Ensuite, je présenterai quelques bibliothèques à cet effet.

### Exceptions vérifiées et non vérifiées

En Java, une méthode peut forcer son appelant à gérer l'occurrence d'exceptions potentielles. L'appelant peut utiliser la clause try/catch, où try contient le code réel et catch contient le code à exécuter lorsque l'exception se produit.

Alternativement, l'appelant peut transmettre ce fardeau à son **appelant parent**. Cela peut remonter jusqu'à ce que la méthode principale soit atteinte. Si la méthode principale transmet également l'exception, l'application plantera lorsqu'une exception se produira.

Dans le cas d'une exception, il existe de nombreux scénarios où l'application ne peut pas continuer à fonctionner et doit s'arrêter. Il n'y a pas de chemins alternatifs. Malheureusement, cela signifie que Java nous force à écrire du code pour une situation où l'application ne devrait plus fonctionner. Assez inutile !

Une option est de minimiser ce code passe-partout. Nous pouvons envelopper l'exception dans une **RuntimeException**, qui est une exception non vérifiée. Cela a pour effet que, même si l'application plante toujours, nous n'avons pas à fournir de code de gestion.

En aucun cas nous ne journalisons l'exception et laissons l'application continuer comme si de rien n'était. C'est possible, mais c'est similaire à ouvrir la boîte de Pandore.

Nous appelons ces exceptions, pour lesquelles nous devons écrire du code supplémentaire, **exceptions vérifiées**. Les autres du type **RuntimeException**, nous les appelons **exceptions non vérifiées**.

![Image](https://cdn-media-1.freecodecamp.org/images/Dgx2RgjqtCmRsIuyoTzcBVKr7BwUO4EnT1KK)
_Exceptions vérifiées et non vérifiées_

### Pourquoi des exceptions vérifiées ?

Nous pouvons trouver de nombreuses exceptions vérifiées dans les bibliothèques tierces, et même dans la bibliothèque de classes Java elle-même. La raison est assez simple. Un fournisseur de bibliothèque ne peut pas prédire dans quel contexte le développeur utilisera leur code.

Logiquement, ils ne savent pas si notre application a des chemins alternatifs. Ils nous laissent donc la décision. Leur responsabilité est de "marquer" les méthodes qui peuvent potentiellement lancer des exceptions. Ces marques nous donnent la chance de mettre en œuvre des contre-mesures.

Un bon exemple est la connexion à une base de données. Le fournisseur de bibliothèque marque la méthode de récupération de connexion avec une exception. Si nous utilisons la base de données comme un cache, nous pouvons envoyer nos requêtes directement à notre base de données principale. C'est le chemin alternatif.

Si notre base de données n'est pas le cache, il n'y a aucun moyen pour que l'application puisse continuer à fonctionner. Et il est acceptable que l'application plante :

![Image](https://cdn-media-1.freecodecamp.org/images/LJlE2Wwpgm0D17OoIMoEUTEgyaGbeKRCwuaA)
_[https://imgflip.com/i/26h3xi](https://imgflip.com/i/26h3xi](https://thepracticaldev.s3.amazonaws.com/i/600zwkafhw4pjiniwzv5.jpg)" rel="noopener" target="_blank" title=")_

### Une base de données perdue

Mettons notre exemple théorique en code réel :

```
public DbConnection getDbConnection(String username, String password) {  try {    return new DbProvider().getConnection(username, password);  } catch (DbConnectionException dce) {    throw new RuntimeException(dce);  }}
```

La base de données n'est pas utilisée comme un cache. En cas de perte de connexion, nous devons arrêter l'application immédiatement.

Comme décrit ci-dessus, nous enveloppons **DbConnectionException** dans une **RuntimeException**.

Le code requis est relativement verbeux et toujours le même. Cela crée beaucoup de duplication et diminue la lisibilité.

### Le wrapper RuntimeException

Nous pouvons écrire une fonction pour simplifier cela. Elle doit envelopper une **RuntimeException** autour de quelque code et retourner la valeur. Nous ne pouvons pas simplement passer du code en Java. La fonction doit faire partie d'une classe ou d'une interface. Quelque chose comme ceci :

```
public interface RuntimeExceptionWrappable<T> {  T execute() throws Exception;} public class RuntimeExceptionWrapper {  public static <T> T wrap(RuntimeExceptionWrappable<T> runtimeExceptionWrappable) {    try {      return runtimeExceptionWrappable.execute();    } catch (Exception exception) {      throw new RuntimeException(exception);    }  }} public class DbConnectionRetrieverJava7 {  public DbConnection getDbConnection(final String username, final String password) {    RuntimeExceptionWrappable<DbConnection> wrappable = new RuntimeExceptionWrappable<DbConnection>() {      public DbConnection execute() throws Exception {        return new DbProvider().getConnection(username, password);      }    };    return RuntimeExceptionWrapper.wrap(wrappable);  }}
```

L'enveloppement **RuntimeException** a été extrait dans sa propre classe. En termes de conception logicielle, cela pourrait être la solution la plus élégante. Cependant, étant donné la quantité de code, nous pouvons difficilement dire que la situation s'est améliorée.

Avec les lambdas de Java 8, les choses sont devenues plus faciles. Si nous avons une interface avec une seule méthode, alors nous écrivons simplement le code spécifique de cette méthode. Le compilateur fait le reste pour nous. Le code inutile ou "syntactic sugar code" pour créer une classe spécifique ou anonyme n'est plus requis. C'est le cas d'utilisation de base pour les Lambdas.

En Java 8, notre exemple ci-dessus ressemble à ceci :

```
@FunctionalInterfacepublic interface RuntimeExceptionWrappable<T> {  T execute() throws Exception;} public class DbConnectionRetrieverJava8 {  public DbConnection getDbConnection(String username, String password) {    return RuntimeExceptionWrapper.wrap(() ->      new DbProvider().getConnection(username, password));  }}
```

La différence est assez claire : le code est plus concis.

### Exceptions dans les Streams & Co.

`RuntimeExceptionWrappable` est une interface très générique. Ce n'est qu'une fonction qui retourne une valeur. Les cas d'utilisation pour cette fonction, ou ses variations, apparaissent partout. Pour notre commodité, la bibliothèque de classes de Java a un ensemble de telles interfaces courantes intégrées. Elles se trouvent dans le package `java.util.function` et sont mieux connues sous le nom d'Interfaces Fonctionnelles. Notre `RuntimeExceptionWrappable` est similaire à `java.util.function.Supplier<`;T>.

Ces interfaces forment le prérequis des puissants Stream, Optional, et autres fonctionnalités qui font également partie de Java 8. En particulier, Stream vient avec beaucoup de méthodes différentes pour le traitement des collections. Beaucoup de ces méthodes ont une Interface Fonctionnelle comme paramètre.

Changeons rapidement de cas d'utilisation. Nous avons une liste de chaînes d'URL que nous voulons mapper dans une liste d'objets de type java.net.URL.

Le code suivant **ne compile pas** :

```
public List<URL> getURLs() {  return Stream    .of(https://www.hahnekamp.com, https://www.austria.info)    .map(this::createURL)    .collect(Collectors.toList());} private URL createURL(String url) throws MalformedURLException {  return new URL(url);}
```

Il y a un gros problème en ce qui concerne les exceptions. Les interfaces définies dans `java.util.function` ne lancent pas d'exceptions. C'est pourquoi notre méthode **createURL** n'a pas la même signature que `java.util.function.Function`, qui est le paramètre de la méthode map.

Ce que nous pouvons faire, c'est écrire le bloc try/catch à l'intérieur du lambda :

```
public List<URL> getURLs() {  return Stream    .of(https://www.hahnekamp.com, https://www.austria.info)    .map(url -> {      try {        return this.createURL(url);      } catch (MalformedURLException e) {        throw new RuntimeException(e);      }    })    .collect(Collectors.toList());}
```

Cela compile, mais ne semble pas non plus très beau. Nous pouvons maintenant aller plus loin et écrire une fonction wrapper avec une nouvelle interface similaire à `RuntimeExceptionWrappable` :

```
@FunctionalInterfacepublic interface RuntimeWrappableFunction<T, R> {  R apply(T t) throws Exception;} public class RuntimeWrappableFunctionMapper {  public static <T, R> Function<T, R> wrap(    RuntimeWrappableFunction<T, R> wrappable) {      return t -> {        try {          return wrappable.apply(t);        } catch(Exception exception) {          throw new RuntimeException(exception);        }      };    }}
```

Et l'appliquer à notre exemple de Stream :

```
public List<URL> getURLs() {  return Stream    .of(https://www.hahnekamp.com, https://www.austria.info)    .map(RuntimeWrappableFunctionMapper.wrap(this::createURL))    .collect(Collectors.toList());} private URL createURL(String url) throws MalformedURLException {  return new URL(url);}
```

Super ! Maintenant nous avons une solution, où nous pouvons :

* exécuter du code sans attraper les exceptions vérifiées, et
* utiliser des lambdas lançant des exceptions dans Stream, Optional, et ainsi de suite.

### SneakyThrow à la rescousse

La bibliothèque SneakyThrow vous permet de sauter la copie et le collage des extraits de code ci-dessus. Divulgation complète : je suis l'auteur.

SneakyThrow vient avec deux méthodes statiques. L'une exécute du code sans attraper les exceptions vérifiées. L'autre méthode enveloppe un lambda lançant une exception dans l'une des interfaces fonctionnelles :

```
//SneakyThrow retournant un résultatpublic DbConnection getDbConnection(String username, String password) {  return sneak(() -> new DbProvider().getConnection(username, password));} //SneakyThrow enveloppant une fonctionpublic List<URL> getURLs() {  return Stream    .of(https://www.hahnekamp.com, https://www.austria.info)    .map(sneaked(this::createURL))    .collect(Collectors.toList());}
```

### Bibliothèques alternatives

#### ThrowingFunction

```
//ThrowingFunction retournant un résultatpublic DbConnection getDbConnection(String username, String password) {  return unchecked(() ->     new DbProvider().getConnection(username, password)).get();} //ThrowingFunction retournant une fonctionpublic List<URL> getURLs() {  return Stream    .of(https://www.hahnekamp.com, https://www.austria.info)    .map(unchecked(this::createURL))    .collect(Collectors.toList());}
```

Contrairement à SneakyThrow, ThrowingFunction ne peut pas exécuter de code directement. Au lieu de cela, nous devons l'envelopper dans un Supplier et appeler le Supplier ensuite. Cette approche peut être plus verbeuse que SneakyThrow.

Si vous avez plusieurs interfaces fonctionnelles non vérifiées dans une classe, alors vous devez écrire le nom complet de la classe avec chaque méthode statique. Cela est dû au fait que unchecked ne fonctionne pas avec la surcharge de méthodes.

D'autre part, ThrowingFunction vous offre plus de fonctionnalités que SneakyThrow. Vous pouvez définir une exception spécifique que vous souhaitez envelopper. Il est également possible que votre fonction retourne un Optional, autrement connu sous le nom de "lifting".

J'ai conçu SneakyThrow comme un wrapper d'opinion de ThrowingFunction.

#### Vavr

Vavr, ou "JavaSlang", est une autre alternative. Contrairement à SneakyThrow et ThrowingFunction, il fournit une batterie complète de fonctionnalités utiles qui améliorent la fonctionnalité de Java.

Par exemple, il vient avec la correspondance de motifs, les tuples, son propre Stream et bien plus encore. Si vous n'en avez pas entendu parler, cela vaut définitivement le coup d'œil. Préparez-vous à investir un peu de temps pour comprendre son plein potentiel.

```
//Vavr retournant un résultatpublic DbConnection getDbConnection(String username, String password) {  return Try.of(() ->   new DbProvider().getConnection(username, password))    .get();} //Vavr retournant une fonctionpublic List<URL> getURLs() {  return Stream    .of(https://www.hahnekamp.com, https://www.austria.info)    .map(url -> Try.of(() -> this.createURL(url)).get())    .collect(Collectors.toList());}
```

#### Project Lombok

Une telle liste de bibliothèques ne serait pas complète sans mentionner Lombok. Comme Vavr, il offre beaucoup plus de fonctionnalités que simplement envelopper les exceptions vérifiées. C'est un générateur de code pour le code passe-partout et crée des Java Beans complets, des objets Builder, des instances de logger, et bien plus encore.

Lombok atteint ses objectifs par manipulation de bytecode. Par conséquent, nous avons besoin d'un plugin supplémentaire dans notre IDE.

@SneakyThrows est l'annotation de Lombok pour manipuler une fonction avec une exception vérifiée en une qui n'en a pas. Cette approche ne dépend pas de l'utilisation des lambdas, donc vous pouvez l'utiliser pour tous les cas. C'est la bibliothèque la moins verbeuse.

Veuillez garder à l'esprit que Lombok manipule le bytecode, ce qui peut causer des problèmes avec d'autres outils que vous pourriez utiliser.

```
//Lombok retournant un résultat@SneakyThrowspublic DbConnection getDbConnection(String username, String password) {  return new DbProvider().getConnection(username, password);} //Lombok retournant une fonctionpublic List<URL> getURLs() {  return Stream    .of(https://www.hahnekamp.com, https://www.austria.info)    .map(this::createURL)    .collect(Collectors.toList());} @SneakyThrowsprivate URL createURL(String url) {  return new URL(url);}
```

#### Lectures complémentaires

Le code est disponible sur [GitHub](https://github.com/rainerhahnekamp/ignore-exception)

* [https://docs.oracle.com/javase/tutorial/essential/exceptions/runtime.html](https://docs.oracle.com/javase/tutorial/essential/exceptions/runtime.html)
* [https://www.artima.com/intv/handcuffs.html](https://www.artima.com/intv/handcuffs.html)
* [http://www.informit.com/articles/article.aspx?p=2171751&seqNum=3](http://www.informit.com/articles/article.aspx?p=2171751&seqNum=3)
* [https://github.com/rainerhahnekamp/sneakythrow](https://github.com/rainerhahnekamp/sneakythrow)
* [https://projectlombok.org/features/SneakyThrows](https://projectlombok.org/features/SneakyThrows)
* [https://github.com/pivovarit/ThrowingFunction](https://github.com/pivovarit/ThrowingFunction)
* [https://github.com/vavr-io/vavr](https://github.com/vavr-io/vavr)
* [http://www.baeldung.com/java-lambda-exceptions](http://www.baeldung.com/java-lambda-exceptions)

_Publié à l'origine sur [www.rainerhahnekamp.com](https://www.rainerhahnekamp.com/en/ignoring-exceptions-in-java/) le 17 mars 2018._