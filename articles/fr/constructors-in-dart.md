---
title: Constructeurs en Dart – Cas d'utilisation et exemples
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2021-03-29T19:53:46.000Z'
originalURL: https://freecodecamp.org/news/constructors-in-dart
coverImage: https://cdn-media-2.freecodecamp.org/w1280/60591ab5687d62084bf6a7c6.jpg
tags:
- name: Dart
  slug: dart
seo_title: Constructeurs en Dart – Cas d'utilisation et exemples
seo_desc: "Most of us are familiar with the concept of constructors. They allow us\
  \ to create different instances of our classes. We can specify which parameters\
  \ the class should depend on when it is being instantiated and hide inner initialization\
  \ logic. \nWe ca..."
---

La plupart d'entre nous sommes familiers avec le concept de constructeurs. Ils nous permettent de créer différentes instances de nos classes. Nous pouvons spécifier quels paramètres la classe doit dépendre lors de son instanciation et masquer la logique d'initialisation interne. 

Nous pouvons avoir plusieurs constructeurs pour différents cas d'utilisation, ou nous pouvons nous fier à celui par défaut. 

En Dart, les constructeurs jouent un rôle similaire, mais ont plusieurs variations qui n'existent pas dans la plupart des langages de programmation. Cet article passera en revue les différents cas d'utilisation et exemples de constructeurs.

Dans tous les exemples de cet article, nous utiliserons la classe suivante :

```dart
class Car {
   String make;
   String model;
   String yearMade;
   bool hasABS;
}
```

## Comment commencer avec les constructeurs en Dart

Si vous ne spécifiez aucun constructeur en Dart, il créera un constructeur par défaut pour vous. 

Cela ne signifie pas que vous verrez un constructeur par défaut généré dans votre classe. Au lieu de cela, lors de la création d'une nouvelle instance de votre classe, ce constructeur sera appelé. Il n'aura aucun argument et appellera le constructeur de la super classe, sans arguments également.

Pour déclarer un constructeur dans votre classe, vous pouvez faire ce qui suit :

```dart
class Car {
	String make;
   	String model;
   	String yearMade;
   	bool hasABS;
   
   	Car(String make, String model, int year, bool hasABS) {
    	this.make = make;
      	this.model = model;
      	this.yearMade = year;
      	this.hasABS = hasABS;
   	}
}
```

Comme vous pouvez l'imaginer, il doit y avoir une meilleure façon d'initialiser nos champs de classe – et en Dart, il y en a une :

```dart
class Car {
	String make;
   	String model;
   	String yearMade;
   	bool hasABS;
   
   	Car(this.make, this.model, this.yearMade, this.hasABS);
}
```

La manière dont nous utilisons ci-dessus est simplement du sucre syntaxique que Dart a pour simplifier l'affectation.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-321.png)
_Photo par [Unsplash](https://unsplash.com/@lin_alessio?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Alessio Lin</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

## Fonctionnalités plus complexes des constructeurs

Dans d'autres langages, il est possible de surcharger votre constructeur. Cela signifie que vous pouvez avoir différents constructeurs avec le même nom, mais avec une signature variable (ou un ensemble différent d'arguments). 

### Constructeurs nommés en Dart

En Dart, cela n'est pas possible, mais il existe une solution. Cela s'appelle les **constructeurs nommés**. Donner à vos constructeurs des noms différents permet à votre classe d'avoir plusieurs constructeurs et aussi de mieux représenter leurs cas d'utilisation en dehors de la classe.

```dart
class Car {
	String make;
   	String model;
   	String yearMade;
   	bool hasABS;
   
   	Car(this.make, this.model, this.yearMade, this.hasABS);
   
   	Car.withoutABS(this.make, this.model, this.yearMade): hasABS = false;
}
```

Le constructeur **withoutABS** initialise la variable d'instance hasABS à false, avant que le corps du constructeur ne s'exécute. Cela est connu sous le nom de **liste d'initialisation** et vous pouvez initialiser plusieurs variables, séparées par une virgule. 

Le cas d'utilisation le plus courant pour les listes d'initialisation est d'initialiser les champs finals déclarés par votre classe.

> ❓ Tout ce qui est placé du côté droit du deux-points (:) n'a pas accès à **this**.

### Constructeurs de fabrique en Dart

Un constructeur de fabrique est un constructeur qui peut être utilisé lorsque vous ne voulez pas nécessairement qu'un constructeur crée une nouvelle instance de votre classe. 

Cela peut être utile si vous conservez des instances de votre classe en mémoire et ne voulez pas en créer une nouvelle à chaque fois (ou si l'opération de création d'une instance est coûteuse). 

Un autre cas d'utilisation est si vous avez une certaine logique dans votre constructeur pour initialiser un champ final qui ne peut pas être fait dans la liste d'initialisation.

```dart
class Car {
	String make;
   	String model;
   	String yearMade;
   	bool hasABS;
   
   	factory Car.ford(String model, String yearMade, bool hasABS) {
    	return FordCar(model, yearMade, hasABS);
    }
}

class FordCar extends Car {
	FordCar(String model, String yearMade, bool hasABS): super("Ford", model, yearMade, hasABS);
 
}
```

## Constructeurs avancés en Dart

### Constructeurs constants et constructeurs de redirection en Dart

Dart vous permet également de créer des constructeurs constants. Que signifie exactement cela ? Si votre classe représente un objet qui ne changera jamais après sa création, vous pouvez bénéficier de l'utilisation d'un constructeur constant. Vous devez vous assurer que tous vos champs de classe sont finals.

```dart
class FordFocus {
   static const FordFocus fordFocus = FordFocus("Ford", "Focus", "2013", true);
   
   final String make;
   final String model;
   final String yearMade;
   final bool hasABS;
   
   const FordFocus(this.make, this.model, this.yearMade, this.hasABS);
   
}
```

Lorsque vous voulez qu'un constructeur appelle un autre constructeur sous le capot, cela s'appelle des **constructeurs de redirection**.

```dart
class Car {
	String make;
   	String model;
   	String yearMade;
   	bool hasABS;
   
   	Car(this.make, this.model, this.yearMade, this.hasABS);
   
   	Car.withoutABS(this.make, this.model, this.yearMade): this(make, model, yearMade, false);
}
```

## Conclusion

Chacun des constructeurs que nous avons discutés a un objectif et un cas d'utilisation différents. Il vous appartient de déterminer et de comprendre quand utiliser chacun d'eux. Espérons que cet article vous a donné les connaissances nécessaires pour le faire.