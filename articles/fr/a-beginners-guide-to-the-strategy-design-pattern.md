---
title: Un guide pour débutants sur le patron de conception Stratégie
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2023-05-04T17:43:03.000Z'
originalURL: https://freecodecamp.org/news/a-beginners-guide-to-the-strategy-design-pattern
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/strategy-design-pattern.png
tags:
- name: design patterns
  slug: design-patterns
- name: Java
  slug: java
seo_title: Un guide pour débutants sur le patron de conception Stratégie
seo_desc: "The Strategy Design Pattern is a behavioral design pattern. It allows you\
  \ to dynamically change the behavior of an object by encapsulating it into different\
  \ strategies. \nThis pattern enables an object to choose from multiple algorithms\
  \ and behaviors ..."
---

Le patron de conception Stratégie est un patron de conception comportemental. Il permet de changer dynamiquement le comportement d'un objet en l'encapsulant dans différentes stratégies. 

Ce patron permet à un objet de choisir parmi plusieurs algorithmes et comportements à l'exécution, plutôt que de choisir statiquement un seul.

Il est basé sur le principe de la composition plutôt que de l'héritage. Il définit une famille d'algorithmes, encapsule chacun d'eux et les rend interchangeables à l'exécution. L'idée centrale derrière ce patron est de séparer les algorithmes de l'objet principal. Cela permet à l'objet de déléguer le comportement de l'algorithme à l'une de ses stratégies contenues.

En termes plus simples, le patron de conception Stratégie fournit un moyen d'extraire le comportement d'un objet dans des classes séparées qui peuvent être échangées à l'exécution. Cela permet à l'objet d'être plus flexible et réutilisable, car différentes stratégies peuvent être facilement ajoutées ou modifiées sans changer le code principal de l'objet.

## Avantages de l'utilisation du patron de conception Stratégie

L'utilisation du patron de conception Stratégie peut offrir plusieurs avantages, notamment :

1. **Flexibilité améliorée du code** : En encapsulant le comportement d'un objet dans différentes stratégies, le code devient plus flexible et plus facile à modifier.
2. **Meilleure réutilisabilité du code** : Puisque les stratégies sont encapsulées et interchangeables, elles peuvent être réutilisées dans différents objets et projets.
3. **Encourage de meilleures pratiques de codage** : Ce patron promeut de bonnes pratiques de codage, telles que la séparation des préoccupations et la réduction de la complexité du code.
4. **Simplifie les tests** : En séparant les algorithmes et les comportements de l'objet, les tests deviennent plus simples.

## Cas d'utilisation du patron de conception Stratégie

Le patron de conception Stratégie peut être utile dans divers scénarios, tels que :

1. **Algorithmes de tri** : Différents algorithmes de tri peuvent être encapsulés dans des stratégies séparées et passés à un objet qui a besoin de tri.
2. **Règles de validation** : Différentes règles de validation peuvent être encapsulées dans des stratégies séparées et passées à un objet qui a besoin de validation.
3. **Formatage de texte** : Différentes stratégies de formatage peuvent être encapsulées dans des stratégies séparées et passées à un objet qui a besoin de formatage.
4. **Accès à la base de données** : Différentes stratégies d'accès à la base de données peuvent être encapsulées dans des stratégies séparées et passées à un objet qui a besoin d'accéder à des données provenant de différentes sources.
5. **Stratégie de paiement** : Différentes méthodes de paiement peuvent être encapsulées dans des stratégies séparées et passées à un objet qui a besoin de traiter les paiements.

## Comprendre le patron de conception Stratégie

Le patron de conception Stratégie est un patron puissant dans le monde de la programmation orientée objet. Il fournit une manière flexible d'encapsuler et d'échanger le comportement d'un objet à l'exécution, permettant au code d'être plus adaptable et plus facile à maintenir. 

Dans cette section, nous allons approfondir le patron de conception Stratégie, en discutant de sa définition, de ses composants et de son fonctionnement.

### Composants du patron de conception Stratégie

Le patron de conception Stratégie se compose de trois composants principaux :

1. **Contexte** : L'objet qui déléguera son comportement à l'une des stratégies contenues. Le contexte maintient une référence à un objet stratégie et interagit avec lui via une interface commune.
2. **Interface Stratégie** : L'interface qui définit le comportement pour toutes les stratégies. Les stratégies implémentent cette interface pour fournir leur implémentation unique du comportement.
3. **Stratégies concrètes** : Les classes qui implémentent l'Interface Stratégie. Chaque stratégie encapsule un comportement spécifique que le contexte peut adopter à l'exécution.

### Fonctionnement du patron de conception Stratégie

Le patron de conception Stratégie fonctionne en séparant le comportement d'un objet de l'objet lui-même. Le comportement est encapsulé dans différentes stratégies, chacune avec sa propre implémentation du comportement. 

Le contexte maintient une référence à un objet stratégie et interagit avec lui via une interface commune. À l'exécution, le contexte peut échanger la stratégie actuelle avec une autre, changeant ainsi efficacement le comportement de l'objet.

### Exemples du patron de conception Stratégie en action

Un exemple du patron de conception Stratégie en action est un service de streaming musical où différents niveaux d'abonnement ont différents modèles de tarification. 

Chaque niveau d'abonnement pourrait avoir une stratégie de tarification différente qui encapsule sa logique de tarification unique. Le système de facturation du service déléguerait le calcul de la tarification à la stratégie de l'abonnement actuel, permettant une modification et une extension faciles de la logique de tarification.

Un autre exemple est les stratégies de paiement. Différentes méthodes de paiement peuvent être encapsulées dans des stratégies séparées, chacune avec sa propre logique de traitement unique. 

Une application de panier d'achat peut utiliser le patron de conception Stratégie pour encapsuler les méthodes de paiement par carte de crédit, PayPal et cryptomonnaie dans des stratégies séparées qui peuvent être échangées à l'exécution. Le système de traitement des paiements de l'application déléguerait la logique de traitement des paiements à la stratégie de la méthode de paiement actuelle, permettant une modification et une extension faciles de la logique de traitement des paiements.

## Comment implémenter le patron de conception Stratégie

Dans cette section, nous allons discuter de la manière d'implémenter le patron de conception Stratégie. Nous commencerons par un exemple de code qui viole le patron de conception Stratégie et expliquerons les problèmes qui en découlent. Ensuite, nous refactoriserons le code pour démontrer comment implémenter le patron de conception Stratégie.

Pour implémenter le patron de conception Stratégie en Java, suivez ces étapes :

1. Identifiez l'algorithme ou le comportement qui doit être encapsulé et rendu interchangeable.
2. Définissez une interface qui représente le comportement, avec une seule signature de méthode qui prend en compte les paramètres requis.
3. Implémentez des classes concrètes qui fournissent des implémentations spécifiques du comportement défini dans l'interface.
4. Définissez une classe de contexte qui contient une référence à l'interface et appelle sa méthode lorsque nécessaire.
5. Modifiez la classe de contexte pour permettre l'échange dynamique des implémentations concrètes à l'exécution.

### Exemple de code

Considérons l'exemple de code suivant :

```java
package withoutstrategy;

public class PaymentProcessor {
    private PaymentType paymentType;

    public void processPayment(double amount) {
        if (paymentType == PaymentType.CREDIT_CARD) {
            System.out.println("Traitement du paiement par carte de crédit du montant " + amount);
        } else if (paymentType == PaymentType.DEBIT_CARD) {
            System.out.println("Traitement du paiement par carte de débit du montant " + amount);
        } else if (paymentType == PaymentType.PAYPAL) {
            System.out.println("Traitement du paiement PayPal du montant " + amount);
        } else {
            throw new IllegalArgumentException("Type de paiement invalide");
        }
    }

    public void setPaymentType(PaymentType paymentType) {
        this.paymentType = paymentType;
    }
}

enum PaymentType {
    CREDIT_CARD,
    DEBIT_CARD,
    PAYPAL
}
```

Dans ce code, la classe `PaymentProcessor` a une méthode `processPayment` qui prend un montant de paiement et traite le paiement. Le type de paiement est défini à l'aide de la méthode `setPaymentType`, qui définit le champ `paymentType`. La méthode `processPayment` vérifie ensuite la valeur de `paymentType` et traite le paiement en conséquence.

Le problème avec ce code est qu'il viole le [Principe Open-Closed](https://www.freecodecamp.org/news/open-closed-principle-solid-architecture-concept-explained/), qui stipule que les classes doivent être ouvertes pour l'extension mais fermées pour la modification. Dans ce code, si vous souhaitez ajouter un nouveau type de paiement, vous devriez modifier la méthode `processPayment`, ce qui viole le Principe Open-Closed.

La classe `PaymentProcessor` viole le patron Stratégie en utilisant des instructions conditionnelles pour déterminer le type de paiement et le traiter en conséquence. Cette approche peut rapidement devenir ingérable et inflexible à mesure que le nombre de types de paiement augmente.

Pour résoudre ce problème, vous pouvez utiliser le patron de conception Stratégie. Tout d'abord, vous définissez une interface commune pour toutes les stratégies de paiement, qui dans ce cas est l'interface `PaymentStrategy` :

```java
package withstrategy;

public interface PaymentStrategy {
    void processPayment(double amount);
}
```

Vous définissez ensuite des implémentations concrètes de l'interface `PaymentStrategy` pour chaque type de paiement. Par exemple, voici les classes `CreditCardPaymentStrategy`, `DebitCardPaymentStrategy` et `PaypalPaymentStrategy` :

```java
package withstrategy;

public class CreditCardPaymentStrategy implements PaymentStrategy {
    public void processPayment(double amount) {
        System.out.println("Traitement du paiement par carte de crédit du montant " + amount);
    }
}
```

```java
package withstrategy;

public class DebitCardPaymentStrategy implements PaymentStrategy {
    public void processPayment(double amount) {
        System.out.println("Traitement du paiement par carte de débit du montant " + amount);
    }
}
```

```java
package withstrategy;

public class PaypalPaymentStrategy implements PaymentStrategy {
    public void processPayment(double amount) {
        System.out.println("Traitement du paiement PayPal du montant " + amount);
    }
}
```

Enfin, vous mettez à jour la classe `PaymentProcessor` pour qu'elle prenne un objet `PaymentStrategy` dans son constructeur, qu'elle utilise pour traiter le paiement :

```java
package withstrategy;

public class PaymentProcessor {
    private PaymentStrategy paymentStrategy;

    public PaymentProcessor(PaymentStrategy paymentStrategy) {
        this.paymentStrategy = paymentStrategy;
    }

    public void processPayment(double amount) {
        paymentStrategy.processPayment(amount);
    }
}
```

Cette implémentation suit le Principe Open-Closed ainsi que le patron Stratégie car vous pouvez ajouter de nouveaux types de paiement en créant de nouvelles implémentations de l'interface `PaymentStrategy` sans modifier le code existant.

### Bonnes pratiques pour l'implémentation du patron de conception Stratégie

Voici quelques bonnes pratiques à garder à l'esprit lors de l'implémentation du patron de conception Stratégie :

1. Gardez l'interface simple et axée sur une seule responsabilité.
2. Encapsulez tout comportement étatique dans les classes de stratégie concrètes, plutôt que dans la classe de contexte.
3. Utilisez l'injection de dépendances pour passer la stratégie concrète à la classe de contexte, plutôt que de la créer directement dans la classe de contexte.
4. Utilisez une énumération ou une classe factory pour fournir un emplacement centralisé pour la création et la gestion des objets de stratégie concrète.

## Applications réelles du patron de conception Stratégie

Le patron de conception Stratégie a été largement utilisé dans diverses applications réelles. Un exemple est le **Framework Collections de Java**. Le Framework Collections fournit un ensemble d'interfaces et de classes pour représenter des collections d'objets, telles que des listes, des ensembles et des cartes. Le framework permet d'appliquer différentes stratégies aux collections en fonction de leur comportement.

Par exemple, le Framework Collections inclut une méthode `sort()` qui permet le tri des collections. La méthode `sort()` prend un objet Comparator comme argument, qui est responsable de la comparaison des objets au sein de la collection. L'interface Comparator définit une stratégie pour comparer deux objets, et la méthode `sort()` utilise cette stratégie pour trier la collection.

De plus, le Framework Collections inclut également l'interface Iterator, qui définit une stratégie pour accéder aux éléments d'une collection. L'Iterator permet à l'utilisateur de parcourir la collection sans exposer sa structure interne, qui peut changer au fil du temps. En utilisant l'interface Iterator, l'utilisateur peut basculer entre différentes stratégies pour accéder aux éléments de la collection.

## Conclusion

Dans ce tutoriel, nous avons exploré le patron de conception Stratégie et son implémentation en Java. Nous avons vu comment le patron Stratégie peut être utilisé pour séparer le comportement d'un objet de son implémentation, offrant une plus grande flexibilité et maintenabilité du code.

Nous avons discuté des composants du patron de conception Stratégie, y compris le Contexte, l'Interface Stratégie et les Stratégies Concrètes. Nous avons également fourni un exemple de la manière dont le patron peut être utilisé pour implémenter un système de paiement, permettant à plusieurs options de paiement d'être implémentées en utilisant une seule interface.

En séparant le comportement d'un objet de son implémentation, le patron Stratégie offre une plus grande flexibilité et adaptabilité aux exigences changeantes.

### Ressources supplémentaires

* [Principes SOLID pour une meilleure conception logicielle](https://www.freecodecamp.org/news/solid-principles-for-better-software-design/)
* [Patrons de conception expliqués](https://www.freecodecamp.org/news/a-beginners-guide-to-the-strategy-design-pattern/freecodecamp.org/news/javascript-design-patterns-explained/)