---
title: charAt() en Java – Comment utiliser la méthode charAt() de Java
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-03-31T16:10:26.000Z'
originalURL: https://freecodecamp.org/news/charat-in-java-how-to-use-the-java-charat-method-2
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/charAt.png
tags:
- name: Java
  slug: java
seo_title: charAt() en Java – Comment utiliser la méthode charAt() de Java
seo_desc: "The charAt() method in Java returns the char value of a character in a\
  \ string at a given or specified index.\nIn this article, we'll see how to use the\
  \ charAt() method starting with it's syntax and then through a few examples/use\
  \ cases. \nHow to Use th..."
---

La méthode `charAt()` en Java renvoie la valeur `char` d'un caractère dans une chaîne à un index donné ou spécifié.

Dans cet article, nous verrons comment utiliser la méthode `charAt()` en commençant par sa syntaxe, puis à travers quelques exemples et cas d'utilisation.

## Comment utiliser la méthode charAt() de Java

Voici à quoi ressemble la syntaxe de la méthode `charAt()` :

```java
public char charAt(int index)
```

Notez que les caractères renvoyés d'une chaîne à l'aide de la méthode `charAt()` ont un type de données `char`. Nous verrons plus tard dans l'article comment cela affecte la concaténation des valeurs renvoyées.

Voyons maintenant quelques exemples.

```java
public class Main {
  public static void main(String[] args) {
  
    String greetings = "Hello World";
    
    System.out.println(greetings.charAt(0));
    // H
  }
}
```

Dans le code ci-dessus, notre chaîne – stockée dans une variable appelée `greetings` – contient "Hello World". Nous avons utilisé la méthode `charAt()` pour obtenir le caractère à l'index 0, qui est H.

Le premier caractère aura toujours un index de 0, le deuxième un index de 1, et ainsi de suite. L'espace entre les sous-chaînes compte également comme un index.

Dans l'exemple suivant, nous verrons ce qui se passe lorsque nous essayons de concaténer les différents caractères renvoyés. La concaténation signifie joindre deux ou plusieurs valeurs ensemble (dans la plupart des cas, ce terme est utilisé pour joindre des caractères ou des sous-chaînes dans une chaîne).

```java
public class Main {
  public static void main(String[] args) {
    String greetings = "Hello World";
    
    char ch1 = greetings.charAt(0); // H
    char ch2 = greetings.charAt(4); // o
    char ch3 = greetings.charAt(9); // l
    char ch4 = greetings.charAt(10); // d
    
    System.out.println(ch1 + ch2 + ch3 + ch4);
    // 391
  }
}
```

En utilisant la méthode `charAt()`, nous avons obtenu les caractères aux index 0, 4, 9 et 10 qui sont respectivement H, o, l et d.

Nous avons ensuite essayé d'afficher et de concaténer ces caractères : `System.out.println(ch1 + ch2 + ch3 + ch4);`.

Mais au lieu d'obtenir "Hold", nous avons obtenu 391. Cela s'est produit parce que les valeurs renvoyées ne sont plus des chaînes de caractères mais ont un type de données `char`. Ainsi, lorsque nous les concaténons, l'interpréteur additionne à la place leur valeur [ASCII](https://www.cs.cmu.edu/~pattis/15-1XX/common/handouts/ascii.html).

H a une valeur ASCII de 72, o a une valeur de 111, l a une valeur de 108 et d a une valeur de 100. Lorsque nous les additionnons, nous obtenons 391, ce qui a été renvoyé dans l'exemple précédent.

## L'erreur StringIndexOutOfBoundsException

Lorsque nous passons un numéro d'index qui dépasse le nombre de caractères de notre chaîne, nous obtenons l'erreur StringIndexOutOfBoundsException dans la console.

Cette erreur s'applique également à l'utilisation d'une indexation négative, qui n'est pas prise en charge en Java. Dans les langages de programmation comme Python qui supportent l'indexation négative, passer -1 vous donnera le dernier caractère ou la dernière valeur d'un ensemble de données, tout comme 0 renvoie toujours le premier caractère.

Voici un exemple :

```java
public class Main {
  public static void main(String[] args) {
    String greetings = "Hello World";
    
    char ch1 = greetings.charAt(20); 
    
    System.out.println(ch1);
    
    /* Exception in thread "main" java.lang.StringIndexOutOfBoundsException: String index out of range: 20 
    */
  }
}
```

Dans le code ci-dessus, nous avons passé un index de 20 : `char ch1 = greetings.charAt(20);` ce qui dépasse le nombre de caractères de notre variable `greetings` – nous avons donc reçu une erreur. Vous pouvez voir le message d'erreur commenté dans le bloc de code ci-dessus.

De même, si nous passions une valeur négative comme ceci : `char ch1 = greetings.charAt(-1);`, nous obtiendrions une erreur similaire.

## Conclusion

Dans cet article, nous avons appris à utiliser la méthode `charAt()` en Java. Nous avons vu comment renvoyer des caractères d'une chaîne en fonction de leur numéro d'index et ce qui se passe lorsque nous concaténons ces caractères.

Enfin, nous avons abordé certains cas où nous obtiendrions une erreur lors de l'utilisation de la méthode `charAt()` en Java.

Bon codage !