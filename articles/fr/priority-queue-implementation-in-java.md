---
title: Files d'attente prioritaires en Java expliquées avec des exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-06T17:34:47.000Z'
originalURL: https://freecodecamp.org/news/priority-queue-implementation-in-java
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c99d7740569d1a4ca21ff.jpg
tags:
- name: Java
  slug: java
seo_title: Files d'attente prioritaires en Java expliquées avec des exemples
seo_desc: 'By Aditya Sridhar

  Priority Queues are used very often in real life applications. In this article we
  will learn what priority queues are and how we can use them in Java.

  Before we discuss what a priority queue is, let''s see what a regular queue is.

  A ...'
---

Par Aditya Sridhar

Les files d'attente prioritaires sont très souvent utilisées dans les applications de la vie réelle. Dans cet article, nous allons apprendre ce que sont les files d'attente prioritaires et comment nous pouvons les utiliser en Java.

Avant de discuter de ce qu'est une file d'attente prioritaire, voyons ce qu'est une file d'attente régulière.

Une file d'attente régulière suit une structure premier entré, premier sorti (FIFO). Cela signifie que si 3 messages – m1, m2 et m3 – entrent dans la file d'attente dans cet ordre, ils en sortent dans le même ordre exact.

## Pourquoi avons-nous besoin de files d'attente ?

Supposons que nous avons des producteurs de données (par exemple, lorsqu'un utilisateur clique sur une page web) qui sont extrêmement rapides. Mais ensuite, nous voulons consommer ces données à un rythme plus lent.

Dans ce cas, le producteur pousserait tous les messages dans la file d'attente, et un consommateur consommerait ces messages plus tard depuis la file d'attente à un rythme plus lent.

## Qu'est-ce qu'une file d'attente prioritaire ?

Comme mentionné précédemment, une file d'attente régulière a une structure premier entré, premier sorti. Mais dans certains scénarios, nous voulons traiter les messages dans une file d'attente en fonction de leur priorité et non en fonction de leur ordre d'arrivée.

Les files d'attente prioritaires aident les consommateurs à consommer les messages de priorité plus élevée en premier, suivis des messages de priorité plus faible.

## Files d'attente prioritaires en Java

Maintenant, voyons quelques exemples de code Java qui nous montreront comment utiliser les files d'attente prioritaires.

### Files d'attente prioritaires avec ordre naturel

Voici un exemple de code montrant comment créer une file d'attente prioritaire simple pour des chaînes de caractères

```java
private static void testStringsNaturalOrdering() {
        Queue<String> testStringsPQ = new PriorityQueue<>();
        testStringsPQ.add("abcd");
        testStringsPQ.add("1234");
        testStringsPQ.add("23bc");
        testStringsPQ.add("zzxx");
        testStringsPQ.add("abxy");

        System.out.println("Chaînes stockées dans l'ordre naturel dans une file d'attente prioritaire\n");
        while (!testStringsPQ.isEmpty()) {
            System.out.println(testStringsPQ.poll());
        }
    }
```

La première ligne nous indique que nous créons une file d'attente prioritaire :

```java
Queue<String> testStringsPQ = new PriorityQueue<>();
```

PriorityQueue est disponible dans le package java.util.

Ensuite, nous ajoutons 5 chaînes de caractères dans un ordre aléatoire dans la file d'attente prioritaire. Pour cela, nous utilisons la fonction **add()** comme montré ci-dessous :

```java
testStringsPQ.add("abcd");
testStringsPQ.add("1234");
testStringsPQ.add("23bc");
testStringsPQ.add("zzxx");
testStringsPQ.add("abxy");
```

Afin d'obtenir le dernier élément de la file d'attente, nous utilisons la fonction **poll()** comme montré ci-dessous :

```java
testStringsPQ.poll()
```

**poll()** nous donnera le dernier élément et le supprimera également de la file d'attente. Si nous voulons obtenir le dernier élément de la file d'attente sans le supprimer, nous pouvons utiliser la fonction **peek()** :

```java
testStringsPQ.peek()
```

Enfin, nous imprimons tous les éléments de la file d'attente en utilisant la fonction poll() comme montré ci-dessous :

```java
while (!testStringsPQ.isEmpty()) {
   System.out.println(testStringsPQ.poll());
}
```

Voici la sortie du programme ci-dessus :

```bash
1234
23bc
abcd
abxy
zzxx
```

Puisque nous n'avons pas indiqué à la file d'attente prioritaire comment prioriser son contenu, elle a utilisé un ordre naturel par défaut. Dans ce cas, elle nous a renvoyé les données dans l'ordre croissant des chaînes de caractères. Ce n'est pas le même ordre dans lequel les éléments ont été ajoutés à la file d'attente.

### Et si nous voulons un ordre personnalisé ?

C'est également possible, et nous pouvons le faire à l'aide d'un **comparateur**.

Créons maintenant une file d'attente prioritaire pour des entiers. Mais cette fois, obtenons le résultat dans l'ordre décroissant de valeur.

Pour y parvenir, nous devons d'abord créer un comparateur d'entiers :

```java
 static class CustomIntegerComparator implements Comparator<Integer> {

        @Override
        public int compare(Integer o1, Integer o2) {
            return o1 < o2 ? 1 : -1;
        }
    }
```

Afin de créer un comparateur, nous implémentons l'interface **comparator** et remplaçons la méthode **compare**.

En utilisant **o1 < o2 ? 1 : -1**, nous obtiendrons le résultat dans l'ordre décroissant. Si nous avions utilisé **o1 > o2 ? 1 : -1**, nous aurions obtenu le résultat dans l'ordre croissant.

Maintenant que nous avons le comparateur, nous devons ajouter ce comparateur à la file d'attente prioritaire. Nous pouvons le faire comme suit :

```java
Queue<Integer> testIntegersPQ = new PriorityQueue<>(new CustomIntegerComparator());
```

Voici le reste du code qui ajoute des éléments dans la file d'attente prioritaire et les imprime :

```java
   testIntegersPQ.add(11);
        testIntegersPQ.add(5);
        testIntegersPQ.add(-1);
        testIntegersPQ.add(12);
        testIntegersPQ.add(6);

        System.out.println("Entiers stockés dans l'ordre inverse de priorité dans une file d'attente prioritaire\n");
        while (!testIntegersPQ.isEmpty()) {
            System.out.println(testIntegersPQ.poll());
        }
```

La sortie du programme ci-dessus est donnée ci-dessous :

```bash
12
11
6
5
-1
```

Nous pouvons voir que le comparateur a bien fait son travail. Maintenant, la file d'attente prioritaire nous donne les entiers dans l'ordre décroissant.

### File d'attente prioritaire avec des objets Java

Jusqu'à présent, nous avons vu comment nous pouvons utiliser des chaînes de caractères et des entiers avec des files d'attente prioritaires.

Dans les applications de la vie réelle, nous utiliserions généralement des files d'attente prioritaires avec des objets Java personnalisés.

Créons d'abord une classe appelée CustomerOrder qui est utilisée pour stocker les détails des commandes des clients :

```java
public class CustomerOrder implements Comparable<CustomerOrder> {
    private int orderId;
    private double orderAmount;
    private String customerName;

    public CustomerOrder(int orderId, double orderAmount, String customerName) {
        this.orderId = orderId;
        this.orderAmount = orderAmount;
        this.customerName = customerName;
    }

    @Override
    public int compareTo(CustomerOrder o) {
        return o.orderId > this.orderId ? 1 : -1;
    }

    @Override
    public String toString() {
        return "orderId:" + this.orderId + ", orderAmount:" + this.orderAmount + ", customerName:" + customerName;
    }

    public double getOrderAmount() {
        return orderAmount;
    }
}
```

Il s'agit d'une classe Java simple pour stocker les commandes des clients. Cette classe implémente l'interface **comparable**, afin que nous puissions décider sur quelle base cet objet doit être ordonné dans la file d'attente prioritaire.

L'ordre est décidé par la fonction **compareTo** dans le code ci-dessus. La ligne **o.orderId > this.orderId ? 1 : -1** indique que les commandes doivent être triées en fonction de l'ordre décroissant du champ **orderId**.

Voici le code qui crée une file d'attente prioritaire pour l'objet CustomerOrder :

```java
CustomerOrder c1 = new CustomerOrder(1, 100.0, "customer1");
CustomerOrder c2 = new CustomerOrder(3, 50.0, "customer3");
CustomerOrder c3 = new CustomerOrder(2, 300.0, "customer2");

Queue<CustomerOrder> customerOrders = new PriorityQueue<>();
customerOrders.add(c1);
customerOrders.add(c2);
customerOrders.add(c3);
while (!customerOrders.isEmpty()) {
	System.out.println(customerOrders.poll());
}
```

Dans le code ci-dessus, trois commandes de clients ont été créées et ajoutées à la file d'attente prioritaire.

Lorsque nous exécutons ce code, nous obtenons la sortie suivante :

```bash
orderId:3, orderAmount:50.0, customerName:customer3
orderId:2, orderAmount:300.0, customerName:customer2
orderId:1, orderAmount:100.0, customerName:customer1
```

Comme prévu, le résultat est dans l'ordre décroissant de l'**orderId**.

### Et si nous voulons prioriser en fonction de orderAmount ?

C'est encore un scénario de la vie réelle. Supposons que par défaut l'objet CustomerOrder est priorisé par l'ordreId. Mais ensuite, nous avons besoin d'un moyen de prioriser en fonction de orderAmount.

Vous pouvez immédiatement penser que nous pouvons modifier la fonction **compareTo** dans la classe **CustomerOrder** pour ordonner en fonction de orderAmount.

Mais la classe **CustomerOrder** peut être utilisée à plusieurs endroits dans l'application, et cela interférerait avec le reste de l'application si nous modifions directement la fonction **compareTo**.

La solution à cela est assez simple : nous pouvons créer un nouveau comparateur personnalisé pour la classe CustomerOrder et l'utiliser avec la file d'attente prioritaire.

Voici le code pour le comparateur personnalisé :

```java
 static class CustomerOrderComparator implements Comparator<CustomerOrder> {

        @Override
        public int compare(CustomerOrder o1, CustomerOrder o2)
        {
            return o1.getOrderAmount() < o2.getOrderAmount() ? 1 : -1;
        }
    }
```

Cela est très similaire au comparateur d'entiers personnalisé que nous avons vu précédemment.

La ligne `o1.getOrderAmount() < o2.getOrderAmount() ? 1 : -1;` indique que nous devons prioriser en fonction de l'ordre décroissant de **orderAmount**.

Voici le code qui crée la file d'attente prioritaire :

```java
  CustomerOrder c1 = new CustomerOrder(1, 100.0, "customer1");
        CustomerOrder c2 = new CustomerOrder(3, 50.0, "customer3");
        CustomerOrder c3 = new CustomerOrder(2, 300.0, "customer2");
        Queue<CustomerOrder> customerOrders = new PriorityQueue<>(new CustomerOrderComparator());
        customerOrders.add(c1);
        customerOrders.add(c2);
        customerOrders.add(c3);
        while (!customerOrders.isEmpty()) {
            System.out.println(customerOrders.poll());
        }
```

Dans le code ci-dessus, nous passons le comparateur à la file d'attente prioritaire dans la ligne de code suivante :

```java
Queue<CustomerOrder> customerOrders = new PriorityQueue<>(new CustomerOrderComparator());
```

Voici le résultat lorsque nous exécutons ce code :

```bash
orderId:2, orderAmount:300.0, customerName:customer2
orderId:1, orderAmount:100.0, customerName:customer1
orderId:3, orderAmount:50.0, customerName:customer3
```

Nous pouvons voir que les données sont dans l'ordre décroissant de orderAmount.

## Code

Tout le code discuté dans cet article peut être trouvé dans [ce dépôt GitHub](https://github.com/aditya-sridhar/java-priority-queue-example).

## Félicitations 🎉

Vous savez maintenant comment utiliser les files d'attente prioritaires en Java.

## À propos de l'auteur

J'aime la technologie et je suis les avancées dans ce domaine. J'aime aussi aider les autres avec mes connaissances technologiques.

N'hésitez pas à me contacter sur mon compte LinkedIn [https://www.linkedin.com/in/aditya1811/](https://www.linkedin.com/in/aditya1811/)

Vous pouvez également me suivre sur Twitter [https://twitter.com/adityasridhar18](https://twitter.com/adityasridhar18)

N'hésitez pas à lire plus de mes articles sur mon blog à l'adresse [adityasridhar.com.](https://adityasridhar.com/)