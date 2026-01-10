---
title: Démystifiez l'Injection de Dépendances et voyez-la en action avec cette introduction
  rapide
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-15T17:42:44.000Z'
originalURL: https://freecodecamp.org/news/demystifying-dependency-injection-49d4b6fe6536
coverImage: https://cdn-media-1.freecodecamp.org/images/1*hnStARpFrN-7liCbeUKXRw.jpeg
tags:
- name: dependency injection
  slug: dependency-injection
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Démystifiez l'Injection de Dépendances et voyez-la en action avec cette
  introduction rapide
seo_desc: 'By Sankalp Bhatia

  Dependency Injection (DI) is a topic which I found a little difficult to grasp during
  my initial days as a software developer. I just could not find a good definition
  of the term.

  In this article, I’ve tried to put my understandings...'
---

Par Sankalp Bhatia

L'Injection de Dépendances (DI) est un sujet que j'ai trouvé un peu difficile à comprendre lors de mes débuts en tant que développeur logiciel. Je n'arrivais pas à trouver une bonne définition du terme.

Dans cet article, j'ai essayé de mettre mes compréhensions de ce concept dans un langage assez simple. Il est destiné aux personnes qui commencent avec l'Injection de Dépendances, ou à celles qui veulent simplement obtenir un peu plus d'informations.

### **Qu'est-ce que l'Injection de Dépendances ?**

Commençons par le commencement : qu'est-ce que c'est ? L'Injection de Dépendances, comme tant d'autres termes de développement logiciel, est un terme sophistiqué pour un concept plutôt simple.

La définition que j'ai trouvée la plus utile est :

**_L'injection de dépendances signifie donner à un objet ses variables d'instance._**

C'est tout. Fournir (injecter) des dépendances pour une classe. Simple, non ? En effet.

Maintenant, il existe trois façons de fournir à une classe ses dépendances en Java. Toutes atteignent... (tousse) l'Injection de Dépendances.

Elles sont :

* Constructeurs
* Setters
* Définition directe des champs publics

### Voyons l'Injection de Dépendances en action

J'ai une classe d'application nommée MyMessagePublisher qui a une dépendance à une certaine classe EmailService.

#### **Injection de Dépendances en utilisant le Constructeur :**

```
public class MyMessagePublisher {    private EmailService emailService = null;        public MyMessagePublisher(EmailService emailService){        this.emailService = emailService;    }}
```

Voyez ce que fait le constructeur là ? Il dit à MyMessagePublisher d'utiliser le EmailService fourni par celui-ci. La classe instanciant MyMessagePublisher doit fournir (injecter) une instance de EmailService (en utilisant le constructeur) pour être utilisée par MyMessagePublisher. Quelque chose comme ceci :

```
EmailService emailService = new EmailService();MyMessagePublisher myMessagePublisher =                            new MyMessagePublisher(emailService);
```

Bon travail, Constructeur !

#### **Injection de Dépendances en utilisant Setter :**

```
public class MyMessagePublisher {    private EmailService emailService = null;    public MyMessagePublisher() {    }    public setEmailService(EmailService emailService) {        this.emailService = emailService;    }}
```

Que se passe-t-il ici ? La classe utilisant MyMessagePublisher peut maintenant définir le EmailService qu'elle souhaite utiliser. Quelque chose comme ceci :

```
MyMessagePublisher myMessagePublisher = new MyMessagePublisher();myMessagePublisher.setEmailService(new EmailService());
```

Bon travail, Setter !

#### **Injection de Dépendances en définissant directement les champs publics**

Ne faites jamais cela !! Si vous avez lu cet article jusqu'ici, je crois que vous savez que cette approche est mauvaise.

### **Avantages de l'Injection de Dépendances**

Je vais commencer cette section en expliquant ce que nous manquons si nous n'utilisons pas l'Injection de Dépendances.

Considérez ce code. J'ai défini les classes EmailService et MyMessagePublisher. MyMessagePublisher instancie elle-même un objet EmailService au lieu d'utiliser les techniques d'Injection de Dépendances mentionnées ci-dessus.

```
public class EmailService {        public void sendEmail(String message, String receiver){        System.out.println("Email sent to " + receiver);    }}
```

```
public class MyMessagePublisher {    private EmailService emailService = new EmailService();    public void processMessages(String message, String receiver){        this.emailService.sendEmail(message, receiver);    }}
```

Le code ci-dessus a quelques limitations :

1. Si la logique d'initialisation de EmailService change (elle prend un paramètre de constructeur pour s'initialiser), nous devrions apporter des modifications à la classe MyMessagePublisher ainsi qu'à tous les autres endroits dans la base de code où nous utilisons EmailService sans Injection de Dépendances.
2. Il a un couplage serré. Supposons que nous voulons nous éloigner de l'envoi d'emails et commencer à envoyer des SMS. Nous devrons alors écrire une nouvelle classe de publication.
3. Ce code n'est pas testable. Nous enverrons des emails à tout le monde lors des tests unitaires de la classe MyMessagePublisher.

Voici la solution que je propose :

```
public class EmailService implements MessageService {    @Override    public void sendMessage(String message, String receiver) {        //logique pour envoyer un email    }}
```

```
public class SMSService implements MessageService {    @Override    public void sendMessage(String message, String receiver) {        //logique pour envoyer un SMS    }
```

```
public interface MessageService {    void sendMessage(String message, String receiver);}
```

```
public class MyMessagePublisher {    private MessageService messageService;        public MyMessagePublisher(MessageService messageService){        this.messageService = messageService;    }        @Override    public void processMessages(String msg, String rec){        this.service.sendMessage(msg, rec);    }}
```

Cette implémentation surmonte les trois limitations mentionnées ci-dessus.

* La logique d'initialisation de EmailService (ou MessageService) est déplacée vers le module initialisant MyMessagePublisher
* Nous pouvons passer à une autre implémentation de MessageService qui envoie des SMS sans changer le code dans MyMessagePublisher
* Le code est testable. Nous pouvons utiliser une implémentation factice de MessageService lors des tests unitaires de MyMessagePublisher

Génial. Nous avons réalisé l'Injection de Dépendances en utilisant les Constructeurs de nos classes. Facile, non ? Mais il y a aussi quelques inconvénients ici.

### Problèmes avec l'Injection de Dépendances Vanille

Quand cela devient-il un problème ? **Quand le code grandit**.

Quelles sont les alternatives ? **Les Conteneurs d'Injection de Dépendances** (Spring, Guice, Dagger, etc.).

Essayons de répondre aux questions ci-dessus plus en détail.

Considérez le code ci-dessous. Nous concevons une application AllInOneApp qui offre plusieurs services comme la réservation de billets de cinéma, la recharge de connexions prépayées, le transfert d'argent et les achats en ligne.

```
public class BookingService {    private SlotsManager slotsManager;    private MyMessagePublisher myMessagePublisher; //Ça vous semble familier ?}
```

```
public class AllInOneApp  {    BookingService bookingService; // Classe ci-dessus    RechargeService rechargeService;    MoneyTransferService moneyTransferService;    ShoppingService shoppingService;}
```

AllInOneApp a besoin de quatre dépendances pour être initialisée. Utilisons l'Injection de Dépendances Vanille en utilisant le Constructeur ici et instancions la classe AllInOneApp.

```
public static void main(String[] args) {
```

```
AllInOneApp allInOneApp = new AllInOneApp(                new BookingService(new SlotsManager(),                                   new MyMessagePublisher(                                              new EmailService())),                 new RechargeService(...),                 new MoneyTransferService(..),                new ShoppingService(...));
```

```
}
```

Cela semble désordonné. Pouvez-vous identifier les problèmes ici ? Quelques-uns sont :

* La classe initialisant AllInOneApp doit connaître la logique pour construire toutes les classes de dépendance également. Cela est fastidieux lors de l'écriture de code dans un projet de taille décente. Gérer toutes ces instances par nous-mêmes n'est pas ce que nous voulons faire lors de l'écriture de code spécifique à l'entreprise.
* Bien que j'aie vu des gens préférer ce type d'Injection de Dépendances, je crois personnellement que ce code est moins lisible par rapport à ceci :

```
AllInOneApp myApp = SomeDIContainer.getInstance(AllInOneApp.class);
```

Si tous les composants utilisent l'Injection de Dépendances, quelque part dans le système, une classe ou une usine doit savoir quoi injecter dans tous ces composants (AllInOneApp, BookingService, MessageService, etc.).

**C'est là que les conteneurs d'Injection de Dépendances entrent en jeu**. Il est appelé un conteneur et non une usine parce que le conteneur prend souvent plus de responsabilités que simplement instancier des objets et injecter des dépendances.

Les conteneurs d'Injection de Dépendances nous permettent de définir quels composants doivent être initiés et quelles dépendances doivent être injectées dans ces composants. Nous pouvons également configurer d'autres fonctionnalités d'instanciation, comme l'objet étant un singleton ou étant créé à chaque fois qu'il est demandé.

Je vais écrire un autre article expliquant l'utilisation de l'un des conteneurs d'Injection de Dépendances populaires, Google Guice, qui aura également une section de pratique. Je mettrai à jour cette histoire avec son lien bientôt. Je vous laisse maintenant avec ce [guide utilisateur](https://github.com/google/guice/wiki/GettingStarted) qui est un bon point de départ.

Merci d'avoir lu :)