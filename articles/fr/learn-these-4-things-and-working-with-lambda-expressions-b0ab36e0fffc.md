---
title: Comment commencer à travailler avec les expressions Lambda en Java
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-24T04:53:23.000Z'
originalURL: https://freecodecamp.org/news/learn-these-4-things-and-working-with-lambda-expressions-b0ab36e0fffc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_Ascfro4BseNIKWOJ06MwQ.jpeg
tags:
- name: clean code
  slug: clean-code
- name: Java
  slug: java
- name: Lambda Expressions
  slug: lambda-expressions
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
seo_title: Comment commencer à travailler avec les expressions Lambda en Java
seo_desc: 'By Luis Santiago

  Before Lambda expressions support was added by JDK 8, I’d only used examples of
  them in languages like C# and C++.

  Once this feature was added to Java, I started looking into them a bit closer.

  The addition of lambda expressions adds...'
---

Par Luis Santiago

Avant que le support des expressions Lambda ne soit ajouté par le JDK 8, je n'en avais utilisé que dans des langages comme C# et C++.

Une fois cette fonctionnalité ajoutée à Java, j'ai commencé à les examiner de plus près.

L'ajout des expressions lambda introduit des éléments de syntaxe qui augmentent la puissance expressive de Java. Dans cet article, je souhaite me concentrer sur les concepts fondamentaux avec lesquels vous devez vous familiariser afin de pouvoir commencer à ajouter des expressions lambda à votre code dès aujourd'hui.

#### Introduction rapide

Les expressions lambda tirent parti des capacités de traitement parallèle des environnements multi-cœurs, comme on peut le voir avec le support des opérations en pipeline sur les données dans l'API Stream.

Ce sont des méthodes anonymes (méthodes sans nom) utilisées pour implémenter une méthode définie par une interface fonctionnelle. Il est important de savoir ce qu'est une interface fonctionnelle avant de se lancer avec les expressions lambda.

#### Interface fonctionnelle

Une interface fonctionnelle est une interface qui contient une et une seule méthode abstraite.

Si vous regardez la définition de l'interface standard Java [Runnable interface](https://docs.oracle.com/javase/7/docs/api/java/lang/Runnable.html), vous remarquerez qu'elle correspond à la définition d'une interface fonctionnelle car elle ne définit qu'une seule méthode : `run()`.

Dans l'exemple de code ci-dessous, la méthode `computeName` est implicitement abstraite et est la seule méthode définie, faisant de MyName une interface fonctionnelle.

```java
interface MyName{
  String computeName(String str);
}
```

#### L'opérateur flèche

Les expressions lambda introduisent le nouvel opérateur flèche `->` en Java. Il divise les expressions lambda en deux parties :

```
(n) -> n*n
```

Le côté gauche spécifie les paramètres requis par l'expression, qui peuvent également être vides si aucun paramètre n'est requis.

Le côté droit est le corps de la lambda qui spécifie les actions de l'expression lambda. Il peut être utile de considérer cet opérateur comme « devient ». Par exemple, « n devient n*n », ou « n devient n au carré ».

Avec les concepts d'interface fonctionnelle et d'opérateur flèche en tête, vous pouvez construire une expression lambda simple :

```java
interface NumericTest {
	boolean computeTest(int n); 
}

public static void main(String args[]) {
	NumericTest isEven = (n) -> (n % 2) == 0;
	NumericTest isNegative = (n) -> (n < 0);

	// Sortie : false
	System.out.println(isEven.computeTest(5));

	// Sortie : true
	System.out.println(isNegative.computeTest(-5));
}
```

```java
interface MyGreeting {
	String processName(String str);
}

public static void main(String args[]) {
	MyGreeting morningGreeting = (str) -> "Good Morning " + str + "!";
	MyGreeting eveningGreeting = (str) -> "Good Evening " + str + "!";
  
  	// Sortie : Good Morning Luis! 
	System.out.println(morningGreeting.processName("Luis"));
	
	// Sortie : Good Evening Jessica!
	System.out.println(eveningGreeting.processName("Jessica"));	
}
```

Les variables `morningGreeting` et `eveningGreeting`, aux lignes 6 et 7 dans l'exemple ci-dessus, font référence à l'interface `MyGreeting` et définissent différentes expressions de salutation.

Lors de l'écriture d'une expression lambda, il est également possible de spécifier explicitement le type du paramètre dans l'expression comme ceci :

```java
MyGreeting morningGreeting = (String str) -> "Good Morning " + str + "!";
MyGreeting eveningGreeting = (String str) -> "Good Evening " + str + "!";
```

#### Expressions Lambda sous forme de blocs

Jusqu'à présent, j'ai couvert des exemples de lambdas à expression unique. Il existe un autre type d'expression utilisé lorsque le code sur le côté droit de l'opérateur flèche contient plus d'une instruction, connu sous le nom de **lambdas de bloc** :

```java
interface MyString {
	String myStringFunction(String str);
}

public static void main (String args[]) {
	// Lambda de bloc pour inverser une chaîne
	MyString reverseStr = (str) -> {
		String result = "";
		
		for(int i = str.length()-1; i >= 0; i--)
			result += str.charAt(i);
		
		return result;
	};

	// Sortie : omeD adbmaL
	System.out.println(reverseStr.myStringFunction("Lambda Demo")); 
}
```

#### Interfaces fonctionnelles génériques

Une expression lambda ne peut pas être générique. Mais l'interface fonctionnelle associée à une expression lambda le peut. Il est possible d'écrire une interface générique et de gérer différents types de retour comme ceci :

```java
interface MyGeneric<T> {
	T compute(T t);
}

public static void main(String args[]){

	// Version String de MyGenericInterface
	MyGeneric<String> reverse = (str) -> {
		String result = "";
		
		for(int i = str.length()-1; i >= 0; i--)
			result += str.charAt(i);
		
		return result;
	};

	// Version Integer de MyGeneric
	MyGeneric<Integer> factorial = (Integer n) -> {
		int result = 1;
		
		for(int i=1; i <= n; i++)
			result = i * result;
		
		return result;
	};

	// Sortie : omeD adbmaL
	System.out.println(reverse.compute("Lambda Demo")); 

	// Sortie : 120
	System.out.println(factorial.compute(5)); 

}
```

#### Expressions Lambda en tant qu'arguments

Une utilisation courante des lambdas est de les passer en tant qu'arguments.

Elles peuvent être utilisées dans n'importe quel morceau de code qui fournit un type cible. Je trouve cela passionnant, car cela me permet de passer du code exécutable en tant qu'arguments à des méthodes.

Pour passer des expressions lambda en tant que paramètres, assurez-vous simplement que le type de l'interface fonctionnelle est compatible avec le paramètre requis.

```java
interface MyString {
	String myStringFunction(String str);
}

public static String reverseStr(MyString reverse, String str){
  return reverse.myStringFunction(str);
}

public static void main (String args[]) {
	// Lambda de bloc pour inverser une chaîne
	MyString reverse = (str) -> {
		String result = "";
		
		for(int i = str.length()-1; i >= 0; i--)
			result += str.charAt(i);
		
		return result;
	};

	// Sortie : omeD adbmaL
	System.out.println(reverseStr(reverse, "Lambda Demo")); 
}
```

Ces concepts vous donneront une bonne base pour commencer à travailler avec les expressions lambda. Jetez un œil à votre code et voyez où vous pouvez augmenter la puissance expressive de Java.