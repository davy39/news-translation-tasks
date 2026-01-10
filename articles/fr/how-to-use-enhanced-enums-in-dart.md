---
title: Comment utiliser les énumérations améliorées en Dart – Expliqué avec des exemples
  de code
subtitle: ''
author: Daniel Asaboro
co_authors: []
series: null
date: '2024-07-22T11:52:55.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-enhanced-enums-in-dart
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/CleanShot-2024-07-18-at-21.42.54@2x.png
tags:
- name: Dart
  slug: dart
seo_title: Comment utiliser les énumérations améliorées en Dart – Expliqué avec des
  exemples de code
seo_desc: 'Enums are one of the most efficient ways to represent a fixed set of values.
  For example: days of the week, user online status, traffic light states, role hierarchy
  in an organization, and so on.

  What''s interesting is that most typed languages such a...'
---

Les énumérations sont l'une des méthodes les plus efficaces pour représenter un ensemble fixe de valeurs. Par exemple : les jours de la semaine, le statut de connexion de l'utilisateur, les états des feux de circulation, la hiérarchie des rôles dans une organisation, et ainsi de suite.

Ce qui est intéressant, c'est que la plupart des langages typés tels que Typescript, Java, C# et Dart vous offrent des fonctionnalités supplémentaires telles que l'itération sur le contenu de l'énumération, et vous attirent l'attention sur les cas non traités ou mal orthographiés.

Cependant, si c'est la seule façon dont vous utilisez les énumérations en Dart, vous passez à côté de nombreuses fonctionnalités introduites dans Dart 2.17 en 2022. Je vais donc vous montrer comment débloquer et exploiter ces fonctionnalités avancées dans cet article.

## Ce que vous allez apprendre

Cet article plonge en profondeur dans le monde des énumérations améliorées. Nous explorerons leurs capacités, leurs avantages, quand les utiliser et quand ne pas les utiliser.

À la fin de votre lecture, j'espère que vous aurez acquis des informations précieuses sur :

1. L'écriture de code propre et expressif qui est presque auto-documenté, car la signification et la fonctionnalité de chaque option sont immédiatement apparentes.
2. L'amélioration de la lisibilité et de la maintenabilité du code en gardant les données et les comportements associés ensemble pour simplifier les modifications futures et réduire le risque d'introduire des erreurs.

## Prérequis : Ce que vous devriez déjà savoir

1. **Connaissances introductives du langage Dart :** Comprendre les bases de Dart, y compris la syntaxe, les types de données et les structures de contrôle.
2. **Compréhension de base des énumérations :** Familiarité avec ce que sont les énumérations et comment elles sont typiquement utilisées pour représenter des ensembles fixes de valeurs.
3. **Concepts de la programmation orientée objet (POO) :** Connaissance des classes, des objets, de l'héritage et du polymorphisme en Dart ou dans un autre langage de programmation.

Cela dit, commençons.

## Table des matières

1. [Les énumérations améliorées : Le changement de jeu](#heading-installation)
2. [Comment utiliser les énumérations améliorées](#heading-comment-utiliser-les-enumerations-ameliorees)
3. [Les énumérations améliorées avec un opérateur personnalisé](#heading-1-les-enumerations-ameliorees-avec-un-operateur-personnalise)
4. [Les énumérations améliorées avec des extensions](#heading-2-les-enumerations-ameliorees-avec-des-extensions)
5. [Les énumérations améliorées avec des mixins](#heading-3-les-enumerations-ameliorees-avec-des-mixins)
6. [Toutes les constantes ne doivent pas être des énumérations](#heading-toutes-les-constantes-ne-doivent-pas-etre-des-enumerations)
7. [Conseil bonus pour utiliser les énumérations](#heading-conseil-bonus-pour-utiliser-les-enumerations)
8. [Remarque finale](#heading-remarque-finale)
9. [Persistance des énumérations : Bonnes pratiques](#heading-persistance-des-enumerations-bonnes-pratiques)
10. [Crédits et ressources](#heading-credits-et-ressources)

## Les énumérations améliorées : Le changement de jeu

Imaginons que nous développons une application de liste de tâches. Nous pourrions utiliser une énumération traditionnelle pour représenter les priorités des tâches :

```dart
enum Priority { low, medium, high }
```

Une petite explication pour ceux qui ne savent pas : Elles sont appelées énumérations, car elles sont l'abréviation d'enumerations.

Selon [Wikipedia](https://en.wikipedia.org/wiki/Enumeration#:~:text=An%20enumeration%20is%20a%20complete,the%20elements%20of%20a%20set.) : Une énumération est une liste complète et ordonnée de tous les éléments d'une collection.

Chaque constante au sein de l'énumération (low, medium, high, etc.) se voit implicitement attribuer un index commençant à zéro, de sorte qu'elles peuvent être itérées comme une liste/itérable.

Cela fonctionne bien, mais cela ne stocke que les noms de base. Que faire si nous voulons associer une couleur à chaque priorité pour des indices visuels, ou une description ? Ou faire en sorte qu'une action spécifique soit déclenchée par chaque priorité ? Les énumérations traditionnelles ne peuvent pas gérer cela.

Disons que vous voulez vraiment le faire, vous devriez faire une danse complexe pour que cela "fonctionne".

## Comment utiliser les énumérations améliorées

Elles vous permettent d'attacher des informations supplémentaires, des méthodes et des propriétés à chaque option d'énumération. Cela signifie que chaque valeur dans l'énumération peut avoir son propre comportement ou ses propres données associés.

Par exemple, disons que vous voulez ajouter une abréviation raccourcie pour chaque jour de la semaine. Au lieu d'utiliser des méthodes d'extension et tout le reste, voici comment vous le feriez avec des énumérations améliorées :

```dart
enum Day {
  monday("Mon"),
  tuesday("Tue"),
  wednesday("Wed"),
  thursday("Thu"),
  friday("Fri"),
  saturday("Sat"),
  sunday("Sun");

  const Day(this.abbreviation);

  final String abbreviation;
}
```

Permettez-moi d'expliquer ce qui se passe ci-dessus.

Contrairement aux énumérations normales, les énumérations améliorées ont des constructeurs personnalisés et vous pouvez leur passer n'importe quelle valeur tant qu'elle est finale. Elle doit être finale car les énumérations ne changent pas.

Voici un exemple :

```dart
// code précédent supprimé pour plus de concision

void main() {
  // Exemple d'utilisation
  Day today = Day.monday;
  print('Today is ${today.name} (${today.abbreviation})'); 
  // Sortie : Today is monday (Mon)
}
```

Vous pouvez recréer l'énumération ci-dessus de cette manière :

```dart
enum Priority {
  low(color: Color.green),
  medium(color: Color.yellow),
  high(color: Color.red),
  ;

  final Color color;

  const Priority(this.color);
}
```

```dart
Priority highPriority = Priority.high;
print(highPriority.color); // Affiche Color.red

```

Cela rend votre code plus puissant et expressif, car les données et les comportements sont regroupés pour garder les choses organisées et faciles à comprendre.

Un autre exemple que j'ai vu dans la nature provient de l'équipe Flutter. Il s'agissait d'une vidéo explicative sur l'utilisation de Flutter et Dart pour créer un jeu pour un Raspberry Pi. C'est une énumération simple qui facilite le travail avec les broches GPIO, le rendant intuitif et moins sujet aux erreurs.

![Capture d'écran d'une vidéo de la chaîne YouTube Flutter sur l'utilisation des énumérations améliorées](https://www.freecodecamp.org/news/content/images/2024/07/image-46.png)
_Flutter, Dart, et vidéo Raspberry Pi de l'équipe Flutter_

Voici le code pour ceux qui sont intéressés :

```dart

enum GameHatGPIO {
  SELECT_BUTTON(7, GameControlEvent.SELECT),
  TL_BUTTON(12, GameControlEvent.LEFT_SHOULDER),
  TR_BUTTON(16, GameControlEvent.RIGHT_SHOULDER),
  DPAD_UP_BUTTON(29, GameControlEvent.UP),
  DPAD_DOWN_BUTTON(31, GameControlEvent.DOWN),
  DPAD_LEFT_BUTTON(33, GameControlEvent.LEFT),
  DPAD_RIGHT_BUTTON(35, GameControlEvent.RIGHT),
  B_BUTTON(32, GameControlEvent.B),
  X_BUTTON(36, GameControlEvent.X);

  final int pin;
  final GameControlEvent event;

  const GameHatGPIO(this.pin, this.event);
}

```

Ensuite, passons à quelques cas d'utilisation avancés.

Le truc pour comprendre la section qui suit est de réaliser que les énumérations sont littéralement des classes, des classes constantes (tous les champs doivent être finaux et le constructeur doit être constant) – bien qu'elles soient spéciales.

Que signifie cela ?

Cela signifie que la plupart des choses que vous pouvez faire avec une classe peuvent être faites avec une énumération. Par exemple, cela signifie que vous pouvez :

1. Redéfinir un opérateur personnalisé.
2. Ajouter des méthodes et des propriétés supplémentaires avec une extension.
3. Les utiliser avec un mixin, et bien plus encore.

Parlons de certains d'entre eux en détail.

### 1. Les énumérations améliorées avec un opérateur personnalisé

Disons que vous concevez le service de facturation pour une application mobile, et quelque part dans l'application, vous voulez avoir une énumération personnalisée pour les mois de l'année comme ceci :

```dart
enum Month {
  January("Jan"),
  February("Feb"),
  ...,
  December("Dec");

  final String abbreviation;

  const Month(this.abbreviation);
}
```

Avec les énumérations améliorées, vous pouvez surcharger un opérateur pour changer la logique normale du langage. Par exemple, vous pouvez surcharger l'opérateur `+` pour ajouter des mois à une énumération `Month` comme ceci :

```dart
enum Month {
  January("Jan"),
  February("Feb"),
  March("Mar"),
  April("Apr"),
  May("May"),
  June("Jun"),
  July("Jul"),
  August("Aug"),
  September("Sep"),
  October("Oct"),
  November("Nov"),
  December("Dec");

  final String abbreviation;

  const Month(this.abbreviation);
  
    Month operator +(int other) {
    // Assurez-vous que le résultat reste dans la plage 0-11
    int result = (this.index + other) % 12; 
    return Month.values[result];
  }
}


void main() {
  // Exemple d'utilisation
  Month currentMonth = Month.January;
  Month nextMonth = currentMonth + 1;
  print('Current month: ${currentMonth.name}     (${currentMonth.abbreviation})'); 
  // Sortie : Current month: January (Jan)
  print('Next month: ${nextMonth.name} (${nextMonth.abbreviation})');     
  // Sortie : Next month: February (Feb)
  
}
```

Et si vous avez besoin de comparer le degré de priorité afin que certaines tâches soient classées au-dessus d'autres dans votre application de liste de tâches ? Voici comment vous pourriez procéder :

```dart
enum Priority {
  low,
  medium,
  high,
}

extension PriorityOperations on Priority {
  bool operator <(Priority other) {
    return this.index < other.index;
  }

  bool operator >(Priority other) {
    return this.index > other.index;
  }
}

void main() {
  Priority currentPriority = Priority.medium;
  if (currentPriority > Priority.low) {
    print('Priority is higher than low.');
  }
}

```

Et pour les permissions d'accès à un fichier pour un groupe de personnes ?

```dart
enum AccessFlag { READ, WRITE, EXECUTE }

extension AccessFlagExtension on AccessFlag {
  AccessFlag operator &(AccessFlag other) {
    return AccessFlag.values[this.index | other.index];
  }
}

```

Vous voyez le principe, n'est-ce pas ? Votre imagination est vraiment la seule limite.

### 2. Les énumérations améliorées avec des extensions

Parfois, une bibliothèque expose une énumération. Vous pouvez ajouter vos propres méthodes personnalisées :

```dart
enum LogLevel {
  DEBUG("[DEBUG]"),
  INFO("[INFO]"),
  WARN("[WARN]"),
  ERROR("[ERROR]");

  final String label;

  const LogLevel(this.label);
}

extension LogLevelExtension on LogLevel {
  String formattedString(String error) {
    return "${this.label} $error";
   
  }
}

void main() {
  print(LogLevel.WARN.formattedString("you can't override toString method in an extension")); 
  // Affiche "[WARN] you can't override toString method in an extension"
}


```

Un autre exemple pour un jeu de cartes

```dart
enum PlayingCardSuit { HEARTS, SPADES, DIAMONDS, CLUBS }

extension PlayingCardSuitExtension on PlayingCardSuit {
  bool operator >(PlayingCardSuit other) => 
      this.index > other.index;
  // ... surcharge similaire pour les autres opérateurs de comparaison
}

void main() {
  PlayingCardSuit suit1 = PlayingCardSuit.SPADES;
  PlayingCardSuit suit2 = PlayingCardSuit.DIAMONDS;
  print(suit1 > suit2); // Affiche true (Spades rank higher than Diamonds)
}

```

### 3. Les énumérations améliorées avec des mixins

Si vous voulez une fonctionnalité partagée entre les énumérations, vous devriez envisager d'utiliser des mixins. Cela peut être particulièrement utile pour des comportements communs comme la sérialisation ou la validation.

```dart
mixin Loggable {
  String getLogMessage();
}

enum OrderStatus with Loggable {
  CREATED("Order Created"),
  SHIPPED("Order Shipped"),
  DELIVERED("Order Delivered");

  final String message;

  const OrderStatus(this.message);

  @override
  String getLogMessage() => "Order status changed to $message";
}

	//une autre classe peut implémenter cela

main(){
	OrderStatus newStatus = OrderStatus.SHIPPED;
	String logMessage = newStatus.getLogMessage();
	print(logMessage); // Sortie : Order status changed to Shipped
}
```

**Note** : Bien qu'ils puissent tous deux être utilisés pour ajouter des fonctionnalités aux classes existantes (y compris les énumérations), les mixins et les extensions servent des objectifs complémentaires en Dart :

Les mixins sont utilisés pour partager des fonctionnalités entre différentes classes ou énumérations, tandis que les extensions sont utilisées pour ajouter de nouvelles fonctionnalités à des types existants spécifiques.

Les deux fournissent des moyens d'améliorer la réutilisabilité, la lisibilité et la maintenabilité du code en programmation Dart. Les mixins peuvent accéder aux membres privés de la classe dans laquelle ils sont mélangés, tandis que les extensions ne peuvent pas accéder aux membres privés du type étendu.

### Toutes les constantes ne doivent pas être des énumérations

Il est essentiel de comprendre que toutes les constantes n'ont pas besoin d'être représentées sous forme d'énumérations.

Une mauvaise utilisation des énumérations peut conduire à un code moins lisible et moins maintenable. Les énumérations doivent être réservées à des ensembles fixes de valeurs liées, assurant ainsi clarté et regroupement logique.

Par exemple, ce n'est pas une bonne façon d'utiliser les énumérations :

```dart
enum Basic {
  font,
  weight,
  size,
}

```

Dans ce cas, l'énumération `Basic` regroupe `font`, `weight` et `size`. Bien que ces constantes soient liées dans un sens large, elles ne représentent pas nécessairement un ensemble fixe de valeurs qui bénéficient d'être regroupées sous forme d'énumération.

C'est la même situation avec l'exemple suivant :

```dart
enum Colors {
  red,
  blue,
  green,
  hexValue,
}

```

Dans ce cas, l'énumération `Colors` regroupe `red`, `blue`, `green` et `hexValue`.

Bien que `red`, `blue` et `green` soient effectivement des couleurs, `hexValue` ne s'intègre pas bien dans cet ensemble. Utiliser les énumérations de manière inappropriée peut conduire à la confusion et rendre le code plus difficile à comprendre et à maintenir. La meilleure façon d'utiliser les énumérations est lorsque vous avez un ensemble fermé de constantes liées qui sont intrinsèquement liées ensemble.

### Conseil bonus pour utiliser les énumérations :

1. Utilisez PascalCase pour les noms d'énumérations et camelCase pour les valeurs d'énumérations.
2. Itérez sur les valeurs d'énumérations en utilisant la propriété intégrée `values`.
3. Les variables d'instance doivent être immuables, y compris celles ajoutées par des mixins.
4. Tous les constructeurs génératifs doivent être constants.
5. Les constructeurs de fabrique ne peuvent retourner qu'une des instances d'énumérations prédéfinies et fixes.
6. Aucune autre classe ne peut être héritée, car une énumération est automatiquement héritée.
7. Les redéfinitions pour index, hashCode et l'opérateur d'égalité (==) ne sont pas autorisées.
8. Un membre nommé value ne peut pas être déclaré dans une énumération, car il entrerait en conflit avec le getter statique values généré automatiquement.
9. Toutes les instances de l'énumération doivent être déclarées au début de la déclaration, et au moins une instance doit être déclarée.
10. Les méthodes d'instance dans une énumération améliorée peuvent utiliser `this` pour référencer la valeur d'énumération actuelle.

## Remarque finale

Comme je l'ai montré de manière extensive, ou du moins je l'espère, les énumérations améliorées rendent votre code plus propre et plus expressif en nous permettant de regrouper des données et des comportements liés. Au lieu de disperser des informations sur vos options d'énumération dans tout votre code, vous pouvez les encapsuler directement dans l'énumération elle-même.

Typiquement, un article de blog sur les énumérations ou même les énumérations améliorées n'expliquerait pas tout. Il s'agit simplement de comprendre les bases et quelques extensions.

Cependant, ce que je trouve vraiment intéressant, c'est que le concept ne résonne pas pleinement jusqu'à ce que vous voyiez des exemples concrets et que vous expérimentiez avec eux dans votre propre travail. Et c'est précisément ce que j'ai cherché à accomplir ici : démontrer la puissance et la flexibilité des énumérations améliorées à travers des exemples pratiques.

Tout est limité par votre imagination.

%[https://twitter.com/MatanLurey/status/1797736320456102178]

### Persistance des énumérations : Bonnes pratiques

Une chose cruciale que j'aimerais ajouter est de ne jamais persister les énumérations directement dans le stockage. Si vous devez stocker des valeurs d'énumération dans une base de données ou un fichier, mappez-les toujours et stockez-les sous forme de chaînes de caractères. Cette approche garantit la clarté et réduit le risque de mélanger les choses involontairement.

Lorsque vous chargez les données, vous pouvez mapper les chaînes de caractères vers les valeurs d'énumération correspondantes. Évitez d'utiliser des entiers à cette fin, car ils peuvent facilement conduire à la confusion et aux erreurs. L'utilisation de chaînes de caractères rend votre code plus robuste et plus facile à maintenir, car il représente directement les valeurs d'énumération.

Voici une manière simple dont je désérialise les chaînes de caractères en énumérations dans ma base de code :

```dart
mixin Common {
  bool isActive();
}

enum SubscriptionPlan with Common {
  free("Free Plan"),
  basic("Basic Plan"),
  premium("Premium Plan");

  final String description;

  const SubscriptionPlan(this.description);

  @override
  bool isActive() {
  //custom method here
    return true;
  }

  
  // utilisez une méthode de fabrique pour ne pas avoir à dépendre
  // de la création d'une instance de SubscriptionPlan
  factory SubscriptionPlan.extractFrom(String json) {
    try {
      return SubscriptionPlan.values.byName(json);
    } catch (e, s) {
      // Peut même être une erreur personnalisée
      throw Error.throwWithStackTrace(e, s);
    }
  }
}

void main() {
  // [1] Cas de test pour extractFrom
  
    // Devrait afficher : SubscriptionPlan.free
  print(SubscriptionPlan.extractFrom('free'));

  // Devrait afficher : SubscriptionPlan.basic
  print(SubscriptionPlan.extractFrom('basic')); 
  
    // Devrait afficher : SubscriptionPlan.premium
  print(SubscriptionPlan.extractFrom('premium')); 

  // [2] Cas de test pour une entrée invalide
  try {
  
      // Devrait lancer une erreur
    print(SubscriptionPlan.extractFrom('business')); 
  } catch (e) {
    print(e); // Affiche l'erreur
  }
}

```

C'est tout pour moi pour l'instant.

J'espère que la lecture de cet article vous aidera à améliorer la lisibilité du code et à maintenir des applications évolutives. Après tout, il s'agit de rationaliser votre processus de développement.

## Crédits et ressources :

1. [Plus d'exemples en réponse à une question sur la façon dont les gens utilisent les énumérations améliorées dans les applications qu'ils construisent sur le sous-reddit flutter](https://www.reddit.com/r/FlutterDev/comments/1e4rnsd/comment/ldktlqn/?context=3).
2. [Plongez dans les énumérations en Dart : Des bases aux techniques avancées.](https://blog.stackademic.com/dive-into-enums-in-dart-from-the-basics-to-advanced-techniques-40e13bc3569f)
3. [Utilisez les énumérations avec prudence](https://www.planetgeek.ch/2009/07/01/enums-are-evil/) : Un article de blog sur le moment où les énumérations sont un signe de mauvais code, assez philosophique, mais une lecture incontournable.
4. Enfin, [Documentation Dart sur Dart.dev](https://dart.dev/language/enums)