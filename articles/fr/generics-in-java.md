---
title: Comment utiliser les génériques en Java – Expliqué avec des exemples de code
subtitle: ''
author: Anjan Baradwaj
co_authors: []
series: null
date: '2024-07-12T18:57:24.000Z'
originalURL: https://freecodecamp.org/news/generics-in-java
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/safety.png
tags:
- name: generics
  slug: generics
- name: Java
  slug: java
seo_title: Comment utiliser les génériques en Java – Expliqué avec des exemples de
  code
seo_desc: "In your Java program, you might have encountered the dreaded ClassCastException\
  \ at runtime while working with different types of objects such as Integer, String,\
  \ and so on. This error is mostly caused by casting an object to the wrong data\
  \ type. \nIn ..."
---

Dans votre programme Java, vous avez peut-être rencontré la redoutable `ClassCastException` à l'exécution lors de la manipulation de différents types d'objets tels que Integer, String, etc. Cette erreur est principalement causée par le cast d'un objet vers un type de données incorrect.

Dans cet article, vous apprendrez à propos des génériques et verrez comment ils peuvent aider à résoudre ce problème.

## Pourquoi avons-nous besoin des génériques ?

Commençons par un exemple simple. Nous allons d'abord ajouter différents types d'objets à un `ArrayList`. Ensuite, nous essaierons de les récupérer et d'imprimer leurs valeurs.

```java
List list = new ArrayList();

list.add("Bonjour");

String str = (String) list.get(0);

System.out.println("Chaîne : " + str);
```

Comme vous pouvez le voir, nous avons ajouté un objet `String` à l'`ArrayList`. Puisque nous sommes ceux qui avons écrit le code, nous savons quel type d'objet représente l'élément, mais le compilateur ne le sait pas. Donc, lorsque nous essayons de récupérer la valeur de la liste, nous obtenons un `Object` et nous devons effectuer un cast explicite.

```java
list.add(123);

String number = (String) list.get(1);

System.out.println("Nombre : " + number);
```

Si nous ajoutons un `Integer` à la même liste et essayons de récupérer la valeur, nous obtiendrons une `ClassCastException` car un objet Integer ne peut pas être casté en String.

En utilisant les génériques, nous pouvons résoudre les deux problèmes discutés ci-dessus. Voyons comment.

Tout d'abord, nous devons utiliser l'opérateur diamant et restreindre le type d'objet contenu dans cette liste. Nous devons mentionner explicitement le type d'objet dans l'opérateur diamant. Cela imposera une vérification au moment de la compilation, donc vous n'aurez plus besoin d'effectuer de cast explicite. Vous pourrez également éliminer la `ClassCastException`.

```java
List<String> list = new ArrayList();

list.add("Bonjour");

String str = list.get(0); // Pas besoin de cast explicite

System.out.println("Chaîne : " + str);

list.add(123); // Génère une erreur de compilation
```

## Conventions de nommage pour les paramètres de type

Dans l'exemple précédent, vous avez vu que l'utilisation de `List<String>` restreignait le type de l'objet que la liste pouvait contenir. Consultez l'exemple suivant d'une classe `Box` et comment elle fonctionne avec différents types de données.

```java
public class Box<T> {
    private T value;

    public void setValue(T value) {
        this.value = value;
    }

    public T getValue() {
        return value;
    }

    public static void main(String[] args) {
        Box<String> stringBox = new Box<>();
        stringBox.setValue("Bonjour, monde !");
        System.out.println(stringBox.getValue());

        Box<Integer> integerBox = new Box<>();
        integerBox.setValue(123);
        System.out.println(integerBox.getValue());
    }
}

```

Remarquez comment la classe `Box<T>` est déclarée. Ici, `T` est un paramètre de type, indiquant que la classe `Box` peut fonctionner avec n'importe quel objet de ce type. Cela est illustré dans la méthode principale où une instance de `Box<String>` et `Box<Integer>` sont toutes deux autorisées à être créées, assurant ainsi la sécurité des types.

Selon la [documentation officielle](https://docs.oracle.com/javase/tutorial/java/generics/types.html) :

> Par convention, les noms des paramètres de type sont des lettres majuscules uniques.   
>   
> Les noms de paramètres de type les plus couramment utilisés sont :  
>   
> E - Élément (utilisé extensivement par le Framework de Collections Java)  
> K - Clé  
> N - Nombre  
> T - Type  
> V - Valeur  
> S, U, V etc. - 2ème, 3ème, 4ème types

Regardons comment nous pouvons écrire une méthode générique. Voici la convention :

```java
public static <T> void printArray(T[] inputArr) {
	for (T element : inputArr) {
		System.out.print(element + " ");
	}
	System.out.println();
}

```

Ici, nous prenons un tableau de n'importe quel type et imprimons ses éléments. Notez que vous devez spécifier le paramètre de type générique `T` dans les chevrons `<>` avant le type de retour de la méthode. Le corps de la méthode parcourt le tableau que nous avons passé en paramètre, de n'importe quel type `T`, et imprime chaque élément.

```java
 public static void main(String[] args) {
        // Créer différents tableaux de type Integer, Double et Character
        Integer[] intArr = {1, 2, 3, 4, 5};
        Double[] doubleArr = {1.1, 2.2, 3.3, 4.4, 5.5};
        Character[] charArr = {'B', 'O', 'N', 'J', 'O', 'U', 'R'};

        System.out.println("Le tableau d'entiers contient :");
        printArray(intArr);   // passer un tableau d'entiers

        System.out.println("Le tableau de doubles contient :");
        printArray(doubleArr);   // passer un tableau de doubles

        System.out.println("Le tableau de caractères contient :");
        printArray(charArr);   // passer un tableau de caractères
    }
```

Nous pouvons appeler cette méthode générique en passant différents types de tableaux (`Integer`, `Double`, `Character`) et vous verrez que votre programme imprimera les éléments de chacun de ces tableaux.

## Restrictions sur les génériques

Dans les génériques, nous utilisons des bornes pour restreindre les types qu'une classe, une interface ou une méthode générique peut accepter. Il existe deux types :


#### 1. Bornes supérieures
Cela est utilisé pour restreindre le type générique à une limite supérieure. Pour définir une borne supérieure, vous utilisez le mot-clé `extends`. En spécifiant une borne supérieure, vous garantissez que la classe, l'interface ou la méthode accepte le type spécifié et toutes ses sous-classes.

La syntaxe serait la suivante : `<T extends SuperClass>`.

Si vous considérez la même classe `Box` que nous avons utilisée précédemment, elle peut être modifiée comme suit :

```java
class Box<T extends Number> {
    private T value;

    public void setValue(T value) {
        this.value = value;
    }

    public T getValue() {
        return value;
    }
}
```

Dans cet exemple, T peut être n'importe quel type qui étend `Number`, tel que `Integer`, `Double`, ou `Float`.

#### 2. Bornes inférieures
Cela est utilisé pour restreindre le type générique à une limite inférieure. Pour définir une borne inférieure, vous utilisez le mot-clé `super`. En spécifiant une borne inférieure, vous garantissez que la classe, l'interface ou la méthode accepte le type spécifié et toutes ses superclasses.

La syntaxe serait la suivante : `<T super SubClass>`.

Pour illustrer l'utilisation des bornes inférieures, examinons l'exemple suivant :

```java
public static void printList(List<? super Integer> list) {
    for (Object element : list) {
        System.out.print(element + " ");
    }
    System.out.println();
}
```

L'utilisation d'une borne inférieure `<? super Integer>` garantit que vous pouvez passer le type spécifié et toutes ses superclasses, ce qui dans ce cas serait une liste de `Integer`, `Number`, ou `Object` à la méthode `printList`.

## Qu'est-ce que les Wildcards ?

Le `?` que vous avez vu dans l'exemple précédent est appelé un Wildcard. Vous pouvez les utiliser pour faire référence à un type inconnu. 

Vous pouvez utiliser un wildcard avec une borne supérieure, auquel cas il ressemblerait à ceci : `<? extends Number>`. Il peut également être utilisé avec une borne inférieure, telle que `<? super Integer>`.

## Effacement de type 

Le type générique que nous utilisons dans notre classe, interface ou méthode n'est disponible qu'au moment de la compilation et il est supprimé à l'exécution. Cela est fait pour assurer la compatibilité ascendante, car les anciennes versions de Java (avant Java 1.5) ne le supportent pas.

Le compilateur utilise les informations de type générique qui sont disponibles pour garantir la sécurité des types. Dans le processus d'effacement de type :
- Si le type n'est pas borné, alors les paramètres sont remplacés par leurs bornes ou le type `Object`
- Si le type est borné, alors les paramètres sont remplacés par la première borne, et les informations de type générique seront supprimées après la compilation

Si nous examinons l'exemple de la classe `Box` :

```java
public class Box<T> {
    private T value;
    // getters et setters
 }
```

Le code ci-dessus deviendra ceci :

```java
public class Box {
    private Object value;
    // getters et setters
 }
```

## Conclusion

Dans cet article, nous avons exploré le concept des génériques en Java et comment vous pouvez les utiliser, avec quelques exemples de base. Comprendre et utiliser les génériques améliore la sécurité des types dans votre programme. Ils éliminent également le besoin de cast explicite et rendent votre code réutilisable et maintenable.

Restons en contact sur [LinkedIn](https://www.linkedin.com/in/abaradwaj/).