---
title: Comment refactoriser vers une dépendance configurable en 5 étapes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-08-19T20:42:23.000Z'
originalURL: https://freecodecamp.org/news/refactoring-to-configurable-dependency-in-5-steps
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/diana-polekhina-ONuLIzB0UtA-unsplash.jpg
tags:
- name: dependency injection
  slug: dependency-injection
- name: refactoring
  slug: refactoring
seo_title: Comment refactoriser vers une dépendance configurable en 5 étapes
seo_desc: 'By Bertil Muth

  Configurable Dependency, also known as Dependency Injection, is a pattern that enables
  you to switch dependencies of your application. The term was coined by Alistair
  Cockburn.

  Say your application has a GUI. But your administrator wan...'
---

Par Bertil Muth

La dépendance configurable, également connue sous le nom d'injection de dépendances, est un modèle qui permet de changer les dépendances de votre application. Le [terme](https://web.archive.org/web/20170624023207/http://alistair.cockburn.us/Configurable+Dependency) a été inventé par Alistair Cockburn.

Disons que votre application a une interface graphique. Mais votre administrateur veut utiliser certaines fonctions via la console. Ou votre code de production appelle un service externe. Mais vos tests ne devraient pas appeler le service, car il ne fournit pas de résultats fiables. Ou le service n'est pas toujours disponible.

C'est là qu'une dépendance configurable est utile. Selon le contexte, vous utilisez une dépendance ou une autre.

De nombreux articles tentent d'expliquer ce modèle. Mais ils l'intègrent dans un contexte plus large, comme l'architecture des ports et adaptateurs. Cela rend la compréhension plus difficile que nécessaire. Je le sais, j'ai écrit de tels articles moi-même.

En plus de cela, de nombreux articles se concentrent sur des applications greenfield. Mais la plupart d'entre nous doivent maintenir des applications qui existent déjà.

Commençons par une classe simple qui a une dépendance câblée. Ensuite, nous la refactoriserons en une classe qui a une dépendance configurable.

L'exemple est trivial, mais les étapes de refactorisation sont généralement applicables à votre propre application si vous êtes dans une situation similaire.

Je ferai référence à un exemple de [projet GitHub](https://github.com/bertilmuth/configurable-dependency) dans l'article. Il montre les étapes à effectuer, dans son historique de commits. À la fin de l'article, il y a des annexes pour IntelliJ IDEA et Eclipse. Elles montrent comment effectuer les étapes de refactorisation dans votre IDE.

# L'exemple de la calculatrice

Disons que vous avez une classe appelée `Calculator`. C'est l'équivalent de la "logique métier". À la fin de chaque calcul, elle imprime le résultat à l'écran. Dans une application réelle, elle pourrait sauvegarder quelque chose dans une base de données à la place.

[Voici](https://github.com/bertilmuth/configurable-dependency/blob/3d8540dd9566cb48f29902b9c9e10292cf8f7560/src/main/java/example/Calculator.java) le code :

```java
package example;

public class Calculator {
	public Calculator(){
	}

	public long add(long one, long two) {
		long result = one + two;
		printResult(result);
		return result;
	}

	public long sub(long one, long two) {
		long result = one - two;
		printResult(result);
		return result;
	}

	private void printResult(long result) {
		System.out.println("The result is: " + result);
	}
}
```

Maintenant, si vous voulez tester cette classe, votre [code de test](https://github.com/bertilmuth/configurable-dependency/blob/3d8540dd9566cb48f29902b9c9e10292cf8f7560/src/test/java/example/CalculatorTest.java) peut ressembler à ceci :

```java
package example;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.*;

class CalculatorTest {
	private Calculator calculator;

	@BeforeEach
	void setup() {
		calculator = new Calculator();
	}

	@Test
	void addsToNumbers() {
		long result = calculator.add(1, 2);
		assertEquals(3, result);
	}

	@Test
	void subtractsToNumbers() {
		long result = calculator.sub(5, 1);
		assertEquals(4, result);
	}
} 
```

Chaque fois que vous exécutez votre test, il imprime les résultats à l'écran. Ce n'est pas nécessaire. Cela ralentit vos tests.

Avec l'injection de dépendances, vous pouvez toujours affirmer le résultat dans le test. Mais vous évitez d'imprimer le résultat à l'écran (ou de sauvegarder le résultat dans la base de données, le système de fichiers, ou ailleurs).

## Étape 1 : Déplacer la création de la dépendance vers le constructeur

Trouvez où une instance de la classe dépendante est créée. Déplacez la création vers le constructeur en assignant l'instance à un champ. Utilisez le champ dans toute la classe, de sorte que seul le constructeur crée la dépendance.

Le code d'exemple est un peu différent. La dépendance est une dépendance statique, `System.out`. Mais comme décrit ci-dessus, le code refactorisé l'assigne au champ `printer` dans le constructeur.

Ainsi, la classe `Calculator` ressemble maintenant à [ci-dessous](https://github.com/bertilmuth/configurable-dependency/blob/43ba441138edafdbca2f7f4a100f5e5b528235a2/src/main/java/example/Calculator.java) :

```java
package example;

import java.io.PrintStream;

public class Calculator {
	private final PrintStream printer;

	public Calculator(){
		printer = System.out;
	}

	public long add(long one, long two) {
		long result = one + two;
		printResult(result);
		return result;
	}

	public long sub(long one, long two) {
		long result = one - two;
		printResult(result);
		return result;
	}

	private void printResult(long result) {
		printer.println("The result is: " + result);
	}
}
```

Exécutez le test. Il doit toujours passer.

## Étape 2 : Passer la dépendance en tant qu'argument du constructeur

Passez l'instance en tant qu'argument du constructeur, au lieu de la créer dans le constructeur. [Voici](https://github.com/bertilmuth/configurable-dependency/blob/411cb1650ddfd209b12d0ebc9007fcd1f857d280/src/main/java/example/Calculator.java) le code d'exemple refactorisé :

```java
package example;

import java.io.PrintStream;

public class Calculator {
	private final PrintStream printer;

	public Calculator(PrintStream printer){
		this.printer = printer;
	}

	public long add(long one, long two) {
		long result = one + two;
		printResult(result);
		return result;
	}

	public long sub(long one, long two) {
		long result = one - two;
		printResult(result);
		return result;
	}

	private void printResult(long result) {
		printer.println("The result is: " + result);
	}
}
```

Pour que cette classe fonctionne, vous devez adapter chaque ligne de code qui crée un objet `Calculator` pour passer la dépendance. Ainsi, la ligne pour créer le `Calculator` dans [CalculatorTest](https://github.com/bertilmuth/configurable-dependency/blob/411cb1650ddfd209b12d0ebc9007fcd1f857d280/src/test/java/example/CalculatorTest.java) ressemble maintenant à ceci :

`calculator = new Calculator(System.out);`

Exécutez le test. Il doit toujours passer.

## Étape 3 : Créer une interface et une implémentation

Créez une [interface](https://github.com/bertilmuth/configurable-dependency/blob/d453d47d297eed94108f4b136e467fc66502fe84/src/main/java/example/PrintStream.java) avec le même nom exact que le nom de la classe de la dépendance. Placez-la dans le même package. Mettez la méthode dedans que la logique métier appelle.

```java
package example;

public interface PrintStream {
	void println(String text);
}
```

Dans la classe [Calculator](https://github.com/bertilmuth/configurable-dependency/blob/d453d47d297eed94108f4b136e467fc66502fe84/src/main/java/example/Calculator.java), supprimez l'instruction d'import de la dépendance, `java.io.PrintStream`, pour utiliser la nouvelle interface à la place.

Voici une implémentation de l'interface. [ConsolePrinter](https://github.com/bertilmuth/configurable-dependency/blob/d453d47d297eed94108f4b136e467fc66502fe84/src/main/java/example/ConsolePrinter.java) contient la fonctionnalité originale qui imprime à l'écran.

```java
package example;

public class ConsolePrinter implements PrintStream{
	@Override
	public void println(String text) {
		System.out.println(text);
	}
}
```

Dans la [classe de test](https://github.com/bertilmuth/configurable-dependency/blob/d453d47d297eed94108f4b136e467fc66502fe84/src/test/java/example/CalculatorTest.java), passez le `ConsolePrinter`. Exécutez le test. Il doit toujours passer et imprimer les résultats à l'écran :

```java
package example;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.*;

class CalculatorTest {
	private Calculator calculator;

	@BeforeEach
	void setup() {
		calculator = new Calculator(new ConsolePrinter());
	}

	@Test
	void addsToNumbers() {
		long result = calculator.add(1, 2);
		assertEquals(3, result);
	}

	@Test
	void subtractsToNumbers() {
		long result = calculator.sub(5, 1);
		assertEquals(4, result);
	}
} 
```

## Étape 4 : Renommer et nettoyer

Ceci est une étape optionnelle. Vous pouvez décider de renommer l'interface, pour lui donner un nom plus significatif. Par exemple, renommez `PrintStream` en [Printer](https://github.com/bertilmuth/configurable-dependency/blob/d453d47d297eed94108f4b136e467fc66502fe84/src/test/java/example/CalculatorTest.java).

Vous pouvez également décider de déplacer la classe vers un package différent et de renommer sa ou ses méthodes.

Exécutez le test. Il doit toujours passer.

## Étape 5 : Configurer la dépendance

Créez [une autre implémentation](https://github.com/bertilmuth/configurable-dependency/blob/66a4aadbaad42616661357bc0ba9f5aaa6f5d846/src/main/java/example/IdlePrinter.java) qui ignore l'argument de texte, à des fins de test :

```java
package example;

public class IdlePrinter implements Printer{
	@Override
	public void println(String text) {
		// Ceci est vide, car nous ne voulons pas imprimer dans les tests.
	}
}
```

Maintenant, vous pouvez changer une seule ligne de CalculatorTest pour désactiver l'impression :

`calculator = new Calculator(new IdlePrinter());`

Depuis Java 8, vous n'avez même pas besoin de `IdlePrinter`. Passez une fonction Lambda à la place :

`calculator = new Calculator(text -> {});`

## Félicitations !

Vous avez refactorisé vers une dépendance configurable.

Jetez un œil à l'historique des commits du [projet GitHub](https://github.com/bertilmuth/configurable-dependency) pour voir les changements de code que j'ai effectués.

Si vous avez des questions, laissez un commentaire ou contactez-moi.

Twitter : [https://twitter.com/BertilMuth](https://twitter.com/BertilMuth)

LinkedIn : [https://www.linkedin.com/in/bertilmuth/](https://www.linkedin.com/in/bertilmuth/)

Les annexes suivantes expliquent les étapes concrètes de refactorisation dans IntelliJ IDEA et Eclipse.

# Annexe A — Comment refactoriser dans IntelliJ IDEA

## Étape 1 d'IntelliJ : Déplacer la création de la dépendance vers le constructeur

Ouvrez la classe `Calculator`. Localisez `System.out`. Cliquez avec le bouton droit, sélectionnez `Refactor > Introduce Field`. Sélectionnez `initialize in: constructor`. Nommez le champ `printer`. Appuyez sur Entrée.

## Étape 2 d'IntelliJ : Passer la dépendance en tant qu'argument du constructeur

Placez le curseur dans le constructeur, `Calculator()`. Marquez l'accès à la dépendance, `System.out`. Cliquez avec le bouton droit, sélectionnez `Refactor > Introduce Parameter`. Nommez le champ `printer`. Appuyez sur Entrée.

## Étape 3 d'IntelliJ : Créer une interface et une implémentation

Créez l'interface et l'implémentation dans le même package :

```java
package example;

public interface PrintStream {
	void println(String text);
}
```

```java
package example;

public class ConsolePrinter implements PrintStream{
	@Override
	public void println(String text) {
		System.out.println(text);
	}
}
```

Allez dans la classe de logique métier `Calculator` et supprimez l'instruction d'import `import java.io.PrintStream;`. Enregistrez le fichier.

Dans la classe de test `CalculatorTest`, utilisez la nouvelle classe d'implémentation.

Changez ceci :

`calculator = new Calculator(System.out);`

en ceci :

`calculator = new Calculator(new ConsolePrinter());`

Enregistrez le fichier. Exécutez le test et vérifiez s'il passe toujours.

## Étape 4 d'IntelliJ : Renommer et nettoyer

Allez dans l'interface `PrintStream`. Cliquez avec le bouton droit sur `PrintStream` et sélectionnez `Refactor > Rename`. Entrez `Printer` et appuyez sur Entrée. Exécutez le test et vérifiez s'il passe toujours.

## Étape 5 d'IntelliJ : Configurer la dépendance

Créez une autre implémentation qui ignore l'argument de texte, à des fins de test :

```java
package example;

public class IdlePrinter implements Printer{
	@Override
	public void println(String text) {
		// Ceci est vide, car nous ne voulons pas imprimer dans les tests.
	}
}
```

Allez dans `CalculatorTest` et changez ceci :

`calculator = new Calculator(new ConsolePrinter());`

en ceci :

`calculator = new Calculator(new IdlePrinter());`

Enregistrez le fichier. Exécutez le test et vérifiez s'il passe toujours.

La sortie de texte devrait maintenant être désactivée. Bien joué.

# Annexe B — Comment refactoriser dans Eclipse

## Étape 1 d'Eclipse : Déplacer la création de la dépendance vers le constructeur

Ouvrez la classe `Calculator`. Localisez `System.out`. Cliquez avec le bouton droit, sélectionnez `Refactor > Extract Local Variable`. Cliquez sur `OK`.

Marquez la nouvelle variable locale `out`. Cliquez avec le bouton droit, sélectionnez `Refactor > Convert Local Variable to Field`. Nommez la variable `printer`. Choisissez `Initialize in Class Constructors`. Cochez `Declare field as 'final'`. Cliquez sur `OK`.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/grafik-13.png)

Exécutez le test et vérifiez s'il passe toujours.

## Étape 2 d'Eclipse : Passer la dépendance en tant qu'argument du constructeur

Placez le curseur dans le constructeur, `Calculator()`. Marquez l'accès à la dépendance, `System.out`, et copiez-le dans le presse-papiers (CTRL-C).

Cliquez avec le bouton droit, sélectionnez `Refactor > Change Method Signature`. Cliquez sur `Add`. Tapez `PrintStream` sous `Type`, `printer` sous `Name`, et collez `System.out` sous `Default value`. Cliquez sur `OK` et `Continue`.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/grafik-14.png)

Changez le constructeur pour qu'il ressemble à ceci :

`public Calculator(PrintStream printer){`  
 `this.printer = printer;`  
 `}`

Enregistrez le fichier. Exécutez le test et vérifiez s'il passe toujours.

## Étape 3 d'Eclipse : Créer une interface et une implémentation

Créez l'interface et l'implémentation dans le même package :

```java
package example;

public interface PrintStream {
	void println(String text);
}
```

```java
package example;

public class ConsolePrinter implements PrintStream{
	@Override
	public void println(String text) {
		System.out.println(text);
	}
}
```

Allez dans la classe de logique métier `Calculator` et supprimez l'instruction d'import `import java.io.PrintStream;`. Enregistrez le fichier.

Dans la classe de test `CalculatorTest`, utilisez la nouvelle classe d'implémentation.

Changez ceci :

`calculator = new Calculator(System.out);`

en ceci :

`calculator = new Calculator(new ConsolePrinter());`

Enregistrez le fichier. Exécutez le test et vérifiez s'il passe toujours.

## Étape 4 d'Eclipse : Renommer et nettoyer

Allez dans l'interface `PrintStream`. Cliquez avec le bouton droit sur `PrintStream` et sélectionnez `Refactor > Rename`. Entrez `Printer` et appuyez sur Entrée. Exécutez le test et vérifiez s'il passe toujours.

## Étape 5 d'Eclipse : Configurer la dépendance

Créez une autre implémentation qui ignore l'argument de texte, à des fins de test :

```java
package example;

public class IdlePrinter implements Printer{
	@Override
	public void println(String text) {
		// Ceci est vide, car nous ne voulons pas imprimer dans les tests.
	}
}
```

Allez dans `CalculatorTest` et changez ceci :

`calculator = new Calculator(new ConsolePrinter());`

en ceci :

`calculator = new Calculator(new IdlePrinter());`

Enregistrez le fichier. Exécutez le test et vérifiez s'il passe toujours.

La sortie de texte devrait maintenant être désactivée. Bien joué.