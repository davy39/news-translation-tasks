---
title: Comment gérer NullPointerException en Java
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-13T17:09:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-handle-nullpointerexception-in-java
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c99be740569d1a4ca2181.jpg
tags:
- name: Java
  slug: java
seo_title: Comment gérer NullPointerException en Java
seo_desc: 'By Aditya Sridhar

  If you have spent some time developing programs in Java, at some point you have
  definitely seen the following exception:

  java.lang.NullPointerException


  Some major production issues arise due to NullPointerException. In this article...'
---

Par Aditya Sridhar

Si vous avez passé un certain temps à développer des programmes en Java, à un moment donné, vous avez définitivement vu l'exception suivante :

```java
java.lang.NullPointerException
```

Certains problèmes majeurs de production surviennent en raison de `NullPointerException`. Dans cet article, nous allons passer en revue quelques façons de gérer `NullPointerException` en Java.

## Vérification simple de null

Considérez le morceau de code suivant :

```java
public static void main(String args[]) {
    String input1 = null;
    simpleNullCheck(input1);
}

private static void simpleNullCheck(String str1) {
    System.out.println(str1.length());
}
```

Si vous exécutez ce code tel quel, vous obtiendrez l'exception suivante :

```java
Exception in thread "main" java.lang.NullPointerException
```

La raison pour laquelle vous obtenez cette erreur est que nous essayons d'effectuer l'opération `length()` sur `str1` qui est `null`.

Une solution simple pour cela est d'ajouter une vérification de null sur `str1` comme montré ci-dessous :

```java
private static void simpleNullCheck(String str1) {
    if (str1 != null) {
        System.out.println(str1.length());
    }
}
```

Cela garantira que, lorsque `str1` est `null`, vous n'exécutez pas la fonction `length()` sur celui-ci.

Mais vous pouvez avoir la question suivante.

### Et si str1 est une variable importante ?

Dans ce cas, vous pouvez essayer quelque chose comme ceci :

```java
 private static void simpleNullCheck(String str1) {
    if (str1 != null) {
        System.out.println(str1.length());
    } else {
        // Effectuer une action alternative lorsque str1 est null
        // Afficher un message indiquant que ce champ particulier est null et donc le programme doit s'arrêter et ne peut pas continuer.
    }
}
```

L'idée est que, lorsque vous vous attendez à ce qu'une valeur soit `null`, il est préférable de mettre une vérification `null` sur cette variable. Et si la valeur s'avère être `null`, prendre une action alternative.

Cela est applicable non seulement aux chaînes, mais à tout autre objet en Java.

## Vérification de null avec Lombok

Prenons maintenant l'exemple suivant :

```java
public static void main(String args[]) {
    String input2 = "test";
    List<String> inputList = null;
    lombokNullCheck(input2, inputList, input2);
}

public static void lombokNullCheck(String str1, List<String> strList, String str2) {
    System.out.println(str1.length() + strList.size() + str2.length());
}
```

Ici, nous avons une fonction qui accepte trois arguments : `str1`, `strList` et `str2`.

Si l'une de ces valeurs s'avère être `null`, nous ne voulons pas exécuter la logique de cette fonction du tout.

### Comment y parvenir ?

C'est là que Lombok est utile. Afin d'ajouter la bibliothèque Lombok dans votre code, incluez la dépendance Maven suivante :

```xml
 <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>1.18.12</version>
            <scope>provided</scope>
 </dependency>
```

Pour en savoir plus sur Maven, consultez [cet article](https://adityasridhar.com/posts/how-to-get-started-with-maven).

Voici à quoi ressemblerait le code avec la vérification `null` de Lombok :

```java
public static void main(String args[]) {
    String input2 = "test";
    List<String> inputList = null;
    try {
        lombokNullCheck(input2, inputList, input2);
    } catch (NullPointerException e) {
        System.out.println(e);
    }

}

public static void lombokNullCheck(@NonNull String str1, @NonNull List<String> strList, @NonNull String str2) {
    System.out.println(str1.length() + strList.size() + str2.length());
}
```

Avant chaque argument de la fonction, nous ajoutons l'annotation `@NonNull`.

De plus, lorsque nous appelons cette fonction, nous plaçons un bloc `try-catch` autour de l'appel de fonction pour attraper `NullPointerException`.

Si l'un des arguments donnés dans la fonction s'avère être `null`, la fonction lancerait une `NullPointerException`. Cela serait alors attrapé par le bloc `try-catch`.

Cela garantit que, si l'un des arguments de la fonction s'avère être `null`, alors la logique dans la fonction n'est pas exécutée et nous savons que le code ne se comportera pas de manière inhabituelle.

Cela peut être fait avec un ensemble de déclarations de vérification `null` également. Mais l'utilisation de Lombok nous aide à éviter d'écrire plusieurs déclarations de vérification `null` et rend le code beaucoup plus propre.

## Listes et Nulls

Supposons que vous avez une liste et que vous voulez imprimer tous les éléments de la liste :

```java
List<String> stringList = new ArrayList<>();
stringList.add("ele1");
stringList.add("ele2");
if (stringList != null) {
    for (String element : stringList)
        System.out.println(element);
}
```

Avant de parcourir la liste, nous devons mettre une vérification `null` sur la liste.

Si la vérification `null` n'est pas présente, alors essayer de parcourir une liste `null` lancera une `NullPointerException`.

## Maps et Nulls

Prenons le scénario où vous devez accéder à la valeur d'une clé particulière dans une map :

```java
Map<String, String> testMap = new HashMap<>();
testMap.put("first_key", "first_val");
if (testMap != null && testMap.containsKey("first_key")) {
    System.out.println(testMap.get("first_key"));
}
```

Tout d'abord, nous devons faire une vérification de null sur l'objet map lui-même. Si cela n'est pas fait, et que la map est `null`, alors une `NullPointerException` est lancée. Cela est fait en utilisant `testMap!=null`

Une fois cela fait, vérifiez si une clé particulière est présente avant d'y accéder. Vous pouvez vérifier la présence de la clé en utilisant `testMap.containsKey("first_key")`. Si cela n'est pas fait et que la clé particulière est absente, alors vous obtiendrez la valeur comme `null`.

## Est-il nécessaire d'ajouter toujours une vérification de null ?

Si vous savez avec certitude qu'une variable particulière ne peut jamais être `null`, alors vous pouvez éviter d'ajouter la vérification `null`. Cela peut être applicable dans les fonctions privées où vous pouvez contrôler les données entrant dans la fonction.

Mais si vous n'êtes pas vraiment certain de la nullabilité d'un objet, il est préférable d'ajouter une vérification `null`.

## **Code**

Tout le code discuté dans cet article peut être trouvé [dans ce dépôt Github](https://github.com/aditya-sridhar/java-handling-nulls-example).

## **Félicitations** ?****

Vous savez maintenant comment gérer `NullPointerException` en Java !

## **À propos de l'auteur**

J'aime la technologie et je suis les avancées dans ce domaine. J'aime aussi aider les autres avec mes connaissances en technologie.

N'hésitez pas à lire plus de mes articles sur [mon blog](https://adityasridhar.com/), à me connecter sur [LinkedIn](https://www.linkedin.com/in/aditya1811/), ou à me suivre sur [Twitter](https://twitter.com/adityasridhar18).