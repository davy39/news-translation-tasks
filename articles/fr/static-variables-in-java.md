---
title: Variables statiques en Java – Pourquoi et comment utiliser les méthodes statiques
subtitle: ''
author: Israel Chidera
co_authors: []
series: null
date: '2023-03-07T15:57:36.000Z'
originalURL: https://freecodecamp.org/news/static-variables-in-java
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/markus-spiske-AaEQmoufHLk-unsplash--1-.jpg
tags:
- name: Java
  slug: java
seo_title: Variables statiques en Java – Pourquoi et comment utiliser les méthodes
  statiques
seo_desc: "Static variables and static methods are two important concepts in Java.\
  \ \nWhenever a variable is declared as static, this means there is only one copy\
  \ of it for the entire class, rather than each instance having its own copy. A static\
  \ method means it ..."
---

Les variables statiques et les méthodes statiques sont deux concepts importants en Java. 

Lorsqu'une variable est déclarée comme statique, cela signifie qu'il n'existe qu'une seule copie de celle-ci pour toute la classe, plutôt que chaque instance ait sa propre copie. Une méthode statique signifie qu'elle peut être appelée sans créer une instance de la classe. 

Les variables et méthodes statiques en Java offrent plusieurs avantages, notamment l'efficacité mémoire, l'accès global, l'indépendance des objets, la performance et l'organisation du code. 

Dans cet article, vous apprendrez comment fonctionnent les variables statiques en Java, ainsi que pourquoi et comment utiliser les méthodes statiques.

## Le mot-clé Static en Java

Le mot-clé static est l'une des fonctionnalités les plus essentielles du langage de programmation Java. Nous l'utilisons pour définir des variables et des méthodes au niveau de la classe. 

Voici un exemple de l'utilisation du mot-clé static :

```java
public class StaticKeywordExample {
  private static int count = 0; // variable statique  

  public static void printCount() { // méthode statique
    System.out.println("Nombre d'objets Example créés jusqu'à présent : " + count);
  }
}

```

Comme vous pouvez le voir ci-dessus, nous avons déclaré la variable **count** comme une variable statique, tandis que nous avons déclaré la méthode **printCount** comme une méthode statique. 

Lorsqu'une variable est déclarée statique en programmation Java, cela signifie que la variable appartient à la classe elle-même plutôt qu'à une instance spécifique de la classe. Cela signifie qu'il n'existe qu'une seule copie de la variable en mémoire, indépendamment du nombre d'instances de la classe créées. 

Voici un exemple. Supposons que nous avons une classe **Department** qui a une variable statique appelée **`numberOfWorker`**. Nous déclarons et incrémentons la variable statique au niveau du constructeur pour montrer la valeur de la variable statique chaque fois que l'objet de la classe est créé.

```java
public class Department{
    public static int numberOfWorker= 0;
    public String name;
    
    public Department(String name) {
        this.name = name;
        numberOfWorker++; // incrémente la variable statique chaque fois qu'un nouveau 							//Person est créé
    }
}

```

Les résultats du code ci-dessus montrent que lorsque nous créons de nouveaux objets Department, la variable statique `numberOfWorker` conserve sa valeur. 

Lorsque nous affichons la valeur de `numberOfWorker` dans la console, nous pouvons voir qu'elle conserve sa valeur dans toutes les instances de la classe `Department`. Cela est dû au fait qu'il n'existe qu'une seule copie de la variable en mémoire, et toute modification de la variable sera reflétée dans toutes les instances de la classe.

```java
Department dpt1 = new Department("Admin");
System.out.println(Department.numberOfWorker); // sortie : 1

Department dpt2 = new Department ("Finance");
System.out.println(Department.numberOfWorker); // sortie : 2

Department dpt3 = new Department ("Software");
System.out.println(Department.numberOfWorker); // sortie : 3

```

Nous pouvons également utiliser le mot-clé `static` pour définir des méthodes statiques. 

Les méthodes statiques sont des méthodes qui appartiennent à la classe plutôt qu'à une instance spécifique de la classe. Les méthodes statiques peuvent être appelées directement sur la classe elle-même sans avoir besoin de créer une instance de la classe au préalable. Voir le code ci-dessous :

```java
public class Calculation{
    public static int add(int a, int b) {
        return a + b;
    }

    public static int multiply(int a, int b) {
        return a * b;
    }
}

```

Dans le code ci-dessus, la classe `Calculation` a deux méthodes statiques. Les méthodes statiques déclarées peuvent être appelées directement sur la classe Calculation sans créer une instance de la classe au préalable. Cela signifie que vous n'avez pas besoin de créer un objet de la classe Calculation avant d'accéder aux classes statiques `add` et `multiply`.

```java
int result = Calculation.add(5, 10);
System.out.println(result); // Sortie : 15

int result2 = Calculation.multiply(5, 10);
System.out.println(result2); // Sortie : 50

```

La méthode `main()` en Java est un exemple de méthode statique. La méthode `main()` est une méthode statique spéciale qui est le point d'entrée des applications Java. La classe `Math` en Java fournit également de nombreuses méthodes statiques qui effectuent des opérations mathématiques.

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Bonjour, le monde !");
    }
}

int result = Math.max(5, 10);
System.out.println(result); // Sortie : 10

```

Le code ci-dessus montre que le point d'entrée des applications Java est une méthode statique. Il montre également que la méthode `max()` est une méthode statique de la classe Math et ne nécessite pas la création d'une instance de la classe Math. 

Comme vous pouvez le voir, les méthodes statiques peuvent être utiles pour fournir des fonctions utilitaires qui ne nécessitent pas la création d'un objet de classe.

## Conclusion

Le mot-clé static est un outil puissant en Java qui peut aider à résoudre de nombreux défis de programmation. Il aide à la gestion de la consommation de mémoire, améliore la cohérence du code et aide à accélérer les applications. 

Pour éviter des problèmes imprévus dans le code, il est crucial d'utiliser le mot-clé static avec sagesse et d'être conscient de ses limitations. 

Le code qui repose fortement sur des variables et des méthodes statiques peut être plus difficile à tester car il introduit des dépendances entre différentes parties du programme. Les variables et méthodes statiques peuvent introduire des dépendances cachées entre différentes parties du programme, rendant plus difficile la compréhension de la manière dont les changements dans une partie du code peuvent affecter d'autres parties. 

Le code qui repose fortement sur des variables statiques peut également être moins flexible et plus difficile à étendre avec le temps. Les variables statiques peuvent également entraîner des problèmes de concurrence si plusieurs threads accèdent et modifient la même variable en même temps. 

Enfin, si une variable statique n'est pas correctement libérée ou supprimée lorsqu'elle n'est plus nécessaire, elle peut entraîner des fuites de mémoire et d'autres problèmes de performance avec le temps. 

En utilisant les variables et méthodes statiques de manière appropriée, vous pouvez créer un code efficace et maintenable qui sera plus facile à utiliser avec le temps.

Bon codage !