---
title: Java String to Int – Comment convertir une chaîne en entier
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-23T20:30:55.000Z'
originalURL: https://freecodecamp.org/news/java-string-to-int-how-to-convert-a-string-to-an-integer
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/Untitled-design.png
tags:
- name: Java
  slug: java
seo_title: Java String to Int – Comment convertir une chaîne en entier
seo_desc: "By Thanoshan MV\nString objects are represented as a string of characters.\
  \ \nIf you have worked in Java Swing, it has components such as JTextField and JTextArea\
  \ which we use to get our input from the GUI. It takes our input as a string. \n\
  If we want to..."
---

Par Thanoshan MV

Les objets String sont représentés comme une chaîne de caractères. 

Si vous avez travaillé avec Java Swing, il possède des composants tels que JTextField et JTextArea que nous utilisons pour obtenir notre entrée depuis l'interface graphique. Il prend notre entrée sous forme de chaîne. 

Si nous voulons créer une calculatrice simple en utilisant Swing, nous devons déterminer comment convertir une chaîne en entier. Cela nous amène à la question – comment pouvons-nous convertir une chaîne en entier ?

En Java, nous pouvons utiliser `Integer.valueOf()` et `Integer.parseInt()` pour convertir une chaîne en entier. 

## 1. Utiliser Integer.parseInt() pour convertir une chaîne en entier

Cette méthode retourne la chaîne sous forme de **type primitif int**. Si la chaîne ne contient pas un entier valide, elle lèvera une [NumberFormatException](https://docs.oracle.com/javase/7/docs/api/java/lang/NumberFormatException.html). 

Ainsi, chaque fois que nous convertissons une chaîne en int, nous devons gérer cette exception en plaçant le code à l'intérieur d'un bloc try-catch. 

Considérons un exemple de conversion d'une chaîne en int en utilisant `Integer.parseInt()` :

```java
        String str = "25";
        try{
            int number = Integer.parseInt(str);
            System.out.println(number); // sortie = 25
        }
        catch (NumberFormatException ex){
            ex.printStackTrace();
        }
```

Essayons de casser ce code en entrant un entier invalide :

```java
     	String str = "25T";
        try{
            int number = Integer.parseInt(str);
            System.out.println(number);
        }
        catch (NumberFormatException ex){
            ex.printStackTrace();
        }
```

Comme vous pouvez le voir dans le code ci-dessus, nous avons essayé de convertir `25T` en entier. Ce n'est pas une entrée valide. Par conséquent, cela doit lever une NumberFormatException. 

Voici la sortie du code ci-dessus :

```java
java.lang.NumberFormatException: For input string: "25T"
	at java.lang.NumberFormatException.forInputString(NumberFormatException.java:65)
	at java.lang.Integer.parseInt(Integer.java:580)
	at java.lang.Integer.parseInt(Integer.java:615)
	at OOP.StringTest.main(StringTest.java:51)
```

Ensuite, nous allons voir comment convertir une chaîne en entier en utilisant la méthode `Integer.valueOf()`. 

## 2. Utiliser Integer.valueOf() pour convertir une chaîne en entier

Cette méthode retourne la chaîne sous forme d'**objet entier**. Si vous regardez la [documentation Java](https://docs.oracle.com/javase/7/docs/api/java/lang/Integer.html#valueOf(java.lang.String)), `Integer.valueOf()` retourne un objet entier qui est équivalent à un `new Integer(Integer.parseInt(s))`. 

Nous placerons notre code à l'intérieur du bloc try-catch lorsque nous utiliserons cette méthode. Considérons un exemple en utilisant la méthode `Integer.valueOf()` :

```java
        String str = "25";
        try{
            Integer number = Integer.valueOf(str);
            System.out.println(number); // sortie = 25
        }
        catch (NumberFormatException ex){
            ex.printStackTrace();
        }
```

Maintenant, essayons de casser le code ci-dessus en entrant un nombre entier invalide :

```java
        String str = "25TA";
        try{
            Integer number = Integer.valueOf(str);
            System.out.println(number); 
        }
        catch (NumberFormatException ex){
            ex.printStackTrace();
        }
```

Similaire à l'exemple précédent, le code ci-dessus lèvera une exception. 

Voici la sortie du code ci-dessus :

```java
java.lang.NumberFormatException: For input string: "25TA"
	at java.lang.NumberFormatException.forInputString(NumberFormatException.java:65)
	at java.lang.Integer.parseInt(Integer.java:580)
	at java.lang.Integer.valueOf(Integer.java:766)
	at OOP.StringTest.main(StringTest.java:42)
```

Nous pouvons également créer une méthode pour vérifier si la chaîne passée est numérique ou non avant d'utiliser les méthodes mentionnées ci-dessus. 

J'ai créé une méthode simple pour vérifier si la chaîne passée est numérique ou non. 

```java
public class StringTest {
    public static void main(String[] args) {
        String str = "25";
        String str1 = "25.06";
        System.out.println(isNumeric(str));
        System.out.println(isNumeric(str1));
    }

    private static boolean isNumeric(String str){
        return str != null && str.matches("[0-9.]+");
    }
}
```

La sortie est :

```java
true
true
```

La méthode `isNumeric()` prend une chaîne comme argument. D'abord, elle vérifie si elle est `null` ou non. Après cela, nous utilisons la méthode `matches()` pour vérifier si elle contient des chiffres de 0 à 9 et un caractère point. 

C'est une manière simple de vérifier les valeurs numériques. Vous pouvez écrire ou rechercher sur Google des expressions régulières plus avancées pour capturer les numériques en fonction de votre cas d'utilisation. 

Il est une bonne pratique de vérifier si la chaîne passée est numérique ou non avant d'essayer de la convertir en entier. 

Merci pour votre lecture. 

Image de l'article par [🇸🇮 Janko Ferlič](https://unsplash.com/@itfeelslikefilm?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) sur [Unsplash](https://unsplash.com/collections/139346/soul-care?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

Vous pouvez me contacter sur [Medium](https://mvthanoshan.medium.com/).

**Bon codage !**