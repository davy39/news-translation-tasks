---
title: Une session pratique avec Google Guice
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-30T16:50:05.000Z'
originalURL: https://freecodecamp.org/news/a-hands-on-session-with-google-guice-5f25ce588774
coverImage: https://cdn-media-1.freecodecamp.org/images/1*TUa3fApD5vZpVB7-d7mTaw.jpeg
tags:
- name: dependency injection
  slug: dependency-injection
- name: Google
  slug: google
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Une session pratique avec Google Guice
seo_desc: 'By Sankalp Bhatia

  A few months ago, I wrote an article explaining dependency injection. I had mentioned
  of a follow-up article with a hands-on session of Google Guice. While I am disappointed
  in being so late in writing this, part of me is happy that...'
---

Par Sankalp Bhatia

Il y a quelques mois, j'ai écrit [un article](https://medium.freecodecamp.org/demystifying-dependency-injection-49d4b6fe6536) expliquant l'injection de dépendances. J'avais mentionné un article de suivi avec une session pratique de Google Guice. Bien que je sois déçu d'avoir tant tardé à écrire cela, une partie de moi est heureuse d'avoir pu écrire un deuxième article.

Cet article suppose que vous êtes familier avec ce qu'est l'injection de dépendances. Je vous recommande de jeter un coup d'œil à [mon article précédent](https://medium.freecodecamp.org/demystifying-dependency-injection-49d4b6fe6536) car nous allons nous appuyer sur les exemples que nous avons utilisés là-bas. Si vous entendez ce terme pour la première fois, cela en vaudra la peine. Si vous êtes familier avec cela, le lire ne prendra pas beaucoup de temps :)

Si vous n'avez pas beaucoup travaillé avec Guice, veuillez le consulter sur GitHub [ici](https://github.com/google/guice).

Nous devrons configurer quelques choses avant de commencer

1. **JDK** : Nous utiliserons Java pour cette tâche. Vous aurez donc besoin d'un JDK fonctionnel pour pouvoir exécuter du code Java sur votre ordinateur. Pour vérifier s'il est déjà installé, exécutez 'java -version' sur la ligne de commande. Si la version est 1.6 ou supérieure, nous sommes bons. Juste une note : Je ne pense pas que cela ait beaucoup de sens d'essayer cela si vous n'avez pas d'expérience avec Java.
2. **Maven** : Nous utiliserons maven comme outil de construction. Pour installer maven, suivez les instructions ici [https://maven.apache.org/install.html](https://maven.apache.org/install.html) (Assez facile). Pour vérifier si vous avez déjà maven, exécutez 'mvn -v' sur la ligne de commande.
3. **git** (optionnel) : [https://www.linode.com/docs/development/version-control/how-to-install-git-on-linux-mac-and-windows/](https://www.linode.com/docs/development/version-control/how-to-install-git-on-linux-mac-and-windows/)
4. **cloner le dépôt pratique (FreshGuice)** : Exécutez les commandes mentionnées ci-dessous

```
cd dossier/destination/ git clone https://github.com/sankalpbhatia/FreshGuice.git
```

### Bindings et Binding Annotations

Nous sommes prêts maintenant. Permettez-moi de commencer par introduire deux termes cruciaux dans le framework Guice : **Bindings et Binding Annotations.**

**Bindings** : étant le concept central de Guice, signifie en termes littéraux un accord ou une promesse impliquant une obligation qui ne peut être rompue. Maintenant, mappons cela dans le contexte de l'injection de dépendances. Lorsque nous faisons en sorte que Guice lie une instance à une classe, nous faisons un accord avec Guice que « Lorsque je demande une instance de X.java, donnez-moi cette instance ». Et cet accord ne peut être rompu.

**Binding Annotations** : Occasionally vous voudrez plusieurs bindings pour le même type. L'annotation et le type (classe) ensemble identifient de manière unique un binding. Par exemple, dans certains cas, vous pourriez avoir besoin de deux instances séparées de la même classe/implémentation de la même interface. Pour les identifier, nous utilisons des annotations de binding. Nous verrons quelques exemples lorsque nous expliquerons les bindings.

#### **Comment créer des bindings**

La section guide de l'utilisateur de Guice l'explique parfaitement. Je vais donc simplement le copier ici :

> Pour créer des bindings, étendez `AbstractModule` et remplacez sa méthode `configure`. Dans le corps de la méthode, appelez `bind()` pour spécifier chaque binding. Ces méthodes sont vérifiées par type afin que le compilateur puisse signaler des erreurs si vous utilisez les mauvais types. Une fois que vous avez créé vos modules, passez-les en arguments à `Guice.createInjector()` pour construire un injector.

Il existe plusieurs types de bindings : Linked, Instance, @Provides annotation, Provider bindings, Constructor bindings, et Un-targeted bindings.

Pour cet article, je ne couvrirai que les Linked Bindings, Instance Bindings, @Provides annotation, et une annotation spéciale @Inject. Je n'utilise que très rarement d'autres moyens pour binder, mais plus d'informations peuvent être trouvées à [https://github.com/google/guice/wiki/Bindings](https://github.com/google/guice/wiki/Bindings).

1. **Linked Binding** : un Linked binding mappe un type/interface à son implémentation. Cet exemple mappe l'interface MessageService à son implémentation EmailService.

En termes simples : Lorsque je demande à Guice de me donner une instance de MessageService, il me donnera une instance de EmailService.

*Mais, comment saura-t-il créer une instance de EmailService ?* Nous verrons cela plus tard.

```
public class MessagingModule extends AbstractModule {  @Override   protected void configure() {    bind(MessageService.class).to(EmailService.class);  }}
```

Peut-être voulons-nous plus d'une instance de MessageService dans notre projet. À certains endroits, nous voudrions qu'un SMSService soit associé à un MessageService, plutôt qu'à un EmailService. Dans de tels cas, nous utilisons une annotation de binding. Pour créer une annotation de binding, vous devrez créer deux annotations comme suit :

```
@BindingAnnotation @Target({ FIELD, PARAMETER, METHOD }) @Retention(RUNTIME)public @interface Email {}
```

```
@BindingAnnotation @Target({ FIELD, PARAMETER, METHOD }) @Retention(RUNTIME)public @interface SMS {}
```

Vous n'avez pas besoin de connaître les annotations de métadonnées (@Target, @Retention). Si vous êtes intéressé, veuillez lire ceci : [https://github.com/google/guice/wiki/BindingAnnotations](https://github.com/google/guice/wiki/BindingAnnotations)

Une fois que nous avons les annotations avec nous, nous pouvons créer deux bindings séparés qui instruisent Guice de créer différentes instances de MessageService basées sur le BindingAnnotation (je l'envisage comme un qualificatif).

```
public class MessagingModule extends AbstractModule {  @Override   protected void configure() {   bind(MessageService.class).annotatedWith(Email.class)                             .to(EmailService.class);
```

```
   bind(MessageService.class).annotatedWith(SMS.class)                             .to(SMSService.class);  }}
```

2. **Instance Binding** : Lie un type à une instance spécifique

```
 bind(Integer.class) .annotatedWith(Names.named("login timeout seconds")) .toInstance(10);
```

On devrait éviter d'utiliser .toInstance avec des objets qui sont compliqués à créer, car cela peut ralentir le démarrage de l'application. Vous pouvez utiliser une méthode @Provides à la place. En fait, vous pouvez même oublier que nous avons mentionné quoi que ce soit sur l'Instance binding pour l'instant.

3. **@ Provides annotation** :

Cela vient directement du wiki de Guice, car c'est assez simple :

> Lorsque vous avez besoin de code pour créer un objet, utilisez une méthode `@Provides`. La méthode doit être définie dans un module, et elle doit avoir une annotation `@Provides`. Le type de retour de la méthode est le type lié. Chaque fois que l'injecteur a besoin d'une instance de ce type, il invoquera la méthode.

```
bind(MessageService.class)
```

```
.annotatedWith(Email.class)
```

```
.to(EmailService.class);
```

est identique à

```
@Provides@Emailpublic MessageService provideMessageService() {  return new EmailService();}
```

où Email.java est une annotation de Binding.

Les dépendances peuvent être passées à une méthode avec cette annotation, ce qui la rend extrêmement utile dans les projets réels. Par exemple, pour le code mentionné ci-dessous, l'injecteur exercera le binding pour le paramètre de chaîne **_apiKey_** avant d'invoquer la méthode.

```
@Provides @PayPalCreditCardProcessor providePayPalCreditCardProcessor(      @Named("PayPal API key") String apiKey) {  PayPalCCProcessor processor = new PaypalCCProcessor();  processor.setApiKey(apiKey);  return processor;  }
```

4. **@ Inject annotation** (Just in Time binding) : Tout ce que nous avons couvert jusqu'à présent s'appelle des _explicit bindings_. Si Guice, en essayant de créer une instance, ne trouve pas de binding explicite, il essaie d'en créer un en utilisant un Just-in-time binding.

Guice peut créer ces bindings en utilisant le constructeur _injectable_ de la classe. Il s'agit soit d'un constructeur non privé sans arguments, soit d'un constructeur avec l'annotation `@Inject`.

### Tâche

Maintenant, passons au projet que nous avons cloné depuis GitHub.

Comme les exemples dans [l'article précédent](https://medium.freecodecamp.org/demystifying-dependency-injection-49d4b6fe6536), ce projet maven implémente un BillingService qui facture une PizzaOrder en utilisant une carte de crédit et génère un Receipt.

La structure du projet est la suivante :

**Interfaces**

* BillingService — facture une commande en utilisant une carte de crédit
* CreditCardProcessor — débite un certain montant d'une carte de crédit
* TransactionLog — enregistre les résultats

**Classes**

src

* CreditCard — entité représentant une carte de crédit
* PizzaOrder — entité représentant une commande de pizza
* Receipt — entité représentant un reçu
* RealBillingService implémente BillingService
* PaypalCreditCardProcessor implémente CreditCardProcessor
* BankCreditCardProcessor implémente CreditCardProcessor
* InMemoryTransactionLog implémente TransactionLog
* GuiceTest — Classe principale qui utilise BillingService
* BillingModule — Tous les bindings Guice vont ici
* GuiceInjectionTest : Tests unitaires pour vérifier les contraintes de binding

La tâche ici est de créer des Guice Bindings dans le BillingModule de sorte que les contraintes suivantes soient satisfaites :

1. Toutes les implémentations de BillingService doivent être liées à RealBillingService.
2. L'interface CreditCardProcessor annotée avec @Paypal doit être liée à la classe PaypalCreditCardProcessor.
3. L'interface CreditCardProcessor nommée avec la chaîne "Bank" doit être liée à la classe BankCreditCardProcessor.
4. Les instances de BillingService retournées par l'injecteur doivent avoir une instance de BankCreditCardProcessor comme dépendance.
5. Toutes les implémentations de TransactionLog doivent être liées à InMemoryTransactionLog.

Les cinq tests unitaires dans GuiceInjectionTests doivent réussir si les conditions ci-dessus sont satisfaites. Vous devriez également pouvoir exécuter la méthode principale dans GuiceTest.

Pour tester la correction :

1. exécuter les tests unitaires

```
mvn test
```

Cela devrait exécuter le fichier de test GuiceInjectionTests.java.

2. exécuter le fichier principal

```
mvn exec:java -Dexec.mainClass="GuiceTest"
```

Cela devrait exécuter la classe principale du projet, qui effectue le travail de bout en bout de création d'une commande, traite le paiement en utilisant une carte de crédit et génère un reçu.

Vous pouvez commenter si vous avez des questions et j'essaierai d'y répondre. Veuillez noter qu'il n'y a pas de réponse unique correcte pour cet exercice. Envoyez-moi vos solutions et j'ajouterai les réponses au dépôt. Ou mieux encore, envoyez-moi une pull request :)