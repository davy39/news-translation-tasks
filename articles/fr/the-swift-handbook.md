---
title: Le manuel Swift – Apprendre Swift pour débutants
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2022-10-24T21:04:27.000Z'
originalURL: https://freecodecamp.org/news/the-swift-handbook
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/pexels-quang-nguyen-vinh-6131283.jpg
tags:
- name: Apple
  slug: apple
- name: beginners guide
  slug: beginners-guide
- name: Swift
  slug: swift
seo_title: Le manuel Swift – Apprendre Swift pour débutants
seo_desc: 'Introduction to Swift

  The Swift programming language was created by Apple in 2014. It''s the official
  language that works with the whole Apple Operating Systems lineup: iOS, iPadOS,
  watchOS, macOS, and tvOS.

  Swift is an open source, general purpose, c...'
---

## Introduction à Swift

Le langage de programmation Swift a été créé par Apple en 2014. C'est le langage officiel qui fonctionne avec toute la gamme des systèmes d'exploitation Apple : iOS, iPadOS, watchOS, macOS et tvOS.

Swift est un langage de programmation open source, généraliste, compilé et statiquement typé.

Chaque valeur a un type assigné. Le type d'une valeur est toujours vérifié lorsqu'elle est utilisée comme argument ou retournée, au moment de la compilation. En cas d'incompatibilité, le programme ne se compilera pas.

Le compilateur de Swift est LLVM, et il est inclus dans Xcode, l'IDE standard que vous utilisez pour le développement de logiciels Apple.

Swift est un langage de programmation moderne conçu pour "s'intégrer" dans un écosystème précédemment conçu pour un autre langage de programmation appelé Objective-C.

La plupart des logiciels fonctionnant sur l'iPhone et le Mac aujourd'hui sont basés sur du code Objective-C, même pour les applications officielles d'Apple. Mais l'utilisation de Swift gagne du terrain année après année. Alors que l'Objective-C sera utilisé pendant des années pour maintenir et améliorer les applications existantes, les nouvelles applications seront probablement créées avec Swift.

Avant qu'Apple n'introduise Swift, l'Objective-C a été largement développé pour introduire de nouvelles capacités et fonctionnalités. Mais ces dernières années, cet effort a considérablement diminué en faveur du développement de Swift.

Cela ne signifie pas que l'Objective-C est mort ou ne vaut pas la peine d'être appris : l'Objective-C reste un outil essentiel pour tout développeur Apple.

Cela dit, je ne vais pas couvrir l'Objective-C ici, car nous nous concentrons sur Swift – le présent et l'avenir de la plateforme Apple.

En seulement 6 ans, Swift a connu 5 versions majeures, et nous en sommes maintenant (au moment de l'écriture) à la version 5.

Swift est célèbre pour être le langage des produits Apple, mais ce n'est pas un langage exclusif à Apple. Vous pouvez l'utiliser sur plusieurs autres plateformes.

Il est open source, donc le portage du langage vers d'autres plateformes ne nécessite aucune permission ou licence, et vous pouvez trouver des projets Swift pour créer des serveurs Web et des API ([https://github.com/vapor/vapor](https://github.com/vapor/vapor)) ainsi que des projets pour interagir avec des microcontrôleurs.

Swift est un langage généraliste, construit avec des concepts modernes, et il a un avenir prometteur.

## Ce que nous allons couvrir ici

L'objectif de ce livre est de vous faire démarrer et fonctionner avec Swift, en partant de zéro.

Si vous avez un Mac ou un iPad, je vous recommande de télécharger l'application Playgrounds créée par Apple depuis l'App Store.

Cette application vous permet d'exécuter des extraits de code Swift sans avoir à créer une application complète au préalable. C'est un moyen très pratique de tester votre code, non seulement lorsque vous commencez à apprendre, mais chaque fois que vous devez essayer du code.

Elle contient également une série d'exemples et de tutoriels géniaux pour élargir vos connaissances en Swift et iOS.

Note : [Vous pouvez obtenir une version PDF et ePub de ce manuel Swift pour débutants](https://thevalleyofcode.com/download/swift/)

* [Introduction à Swift](#heading-introduction-a-swift)
* [Variables en Swift](#heading-variables-en-swift)
* [Objets en Swift](#heading-objets-en-swift)
* [Opérateurs en Swift](#heading-operateurs-en-swift)
* [Conditionnels en Swift](#heading-conditionnels-en-swift)
* [Boucles en Swift](#heading-boucles-en-swift)
* [Comment écrire des commentaires en Swift](#heading-comment-ecrire-des-commentaires-en-swift)
* [Points-virgules en Swift](#heading-points-virgules-en-swift)
* [Nombres en Swift](#heading-nombres-en-swift)
* [Chaînes de caractères en Swift](#heading-chaines-de-caracteres-en-swift)
* [Booléens en Swift](#heading-booleens-en-swift)
* [Tableaux en Swift](#heading-tableaux-en-swift)
* [Ensembles en Swift](#heading-ensembles-en-swift)
* [Dictionnaires en Swift](#heading-dictionnaires-en-swift)
* [Tuples en Swift](#heading-tuples-en-swift)
* [Optionnels et `nil` en Swift](#heading-optionnels-et-nil-en-swift)
* [Énumérations en Swift](#heading-enumerations-en-swift)
* [Structures en Swift](#heading-structures-en-swift)
* [Classes en Swift](#heading-classes-en-swift)
* [Fonctions en Swift](#heading-fonctions-en-swift)
* [Protocoles en Swift](#heading-protocoles-en-swift)
* [Où aller à partir d'ici](#heading-ou-aller-a-partir-dici)

## Variables en Swift

Les variables nous permettent d'assigner une valeur à une étiquette. Nous les définissons en utilisant le mot-clé `var` :

```swift
var name = "Roger"
var age = 8
```

Une fois qu'une variable est définie, nous pouvons changer sa valeur :

```swift
age = 9
```

Les variables que vous ne souhaitez pas changer peuvent être définies comme des constantes, en utilisant le mot-clé `let` :

```swift
let name = "Roger"
let age = 8
```

Changer la valeur d'une constante est interdit.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screen-Shot-2020-11-01-at-07.51.48.png)
_Vous ne pouvez pas changer la valeur d'une constante ou vous obtiendrez cette erreur_

Lorsque vous définissez une variable et que vous lui assignez une valeur, Swift infère implicitement son type.

`8` est une valeur de type `Int`.

`"Roger"` est une valeur de type `String`.

Un nombre décimal comme `3.14` est une valeur de type `Double`.

Vous pouvez également spécifier le type au moment de l'initialisation :

```swift
let age: Int = 8
```

Mais il est typique de laisser Swift l'inférer, et cela se fait principalement lorsque vous déclarez une variable sans l'initialiser.

Vous pouvez déclarer une constante et l'initialiser plus tard :

```swift
let age : Int
age = 8
```

Une fois qu'une variable est définie, elle est liée à ce type. Vous ne pouvez pas lui assigner un type différent, sauf si vous le convertissez explicitement.

Vous ne pouvez pas faire ceci :

```swift
var age = 8
age = "nine"
```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screen-Shot-2020-11-01-at-07.54.25.png)
_Erreur : Impossible d'assigner une valeur de type 'String' à une valeur de type 'Int'_

`Int` et `String` ne sont que deux des types de données intégrés fournis par Swift.

## Objets en Swift

En Swift, tout est un objet. Même la valeur `8` que nous avons assignée à la variable `age` est un objet.

Dans certains langages, les objets sont un type spécial. Mais en Swift, tout est un objet et cela conduit à une caractéristique particulière : chaque valeur peut _recevoir des messages_.

Chaque type peut avoir plusieurs fonctions associées, que nous appelons **méthodes**.

Par exemple, en parlant de la valeur numérique `8`, nous pouvons appeler sa méthode `isMultiple`, pour vérifier si le nombre est un multiple d'un autre nombre :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screen-Shot-2020-11-01-at-14.43.49.png)
_méthode `isMultiple`_

Une valeur de type String a un autre ensemble de méthodes.

Un type a également des variables d'instance. Par exemple, le type String a la variable d'instance `count`, qui vous donne le nombre de caractères dans une chaîne :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screen-Shot-2020-11-01-at-14.45.39.png)
_variable d'instance `count`_

Swift a 3 différents **types d'objets**, que nous verrons plus en détail plus tard : **classes**, **structs** et **enums**.

Ceux-ci sont très différents, mais ils ont une chose en commun : pour chaque type d'objet, nous pouvons **ajouter des méthodes**, et à toute valeur, de n'importe quel type d'objet, nous pouvons **envoyer des messages**.

## Opérateurs en Swift

Nous pouvons utiliser un large ensemble d'opérateurs pour opérer sur des valeurs.

Nous pouvons diviser les opérateurs en plusieurs catégories. La première est le nombre de cibles : 1 pour les **opérateurs unaires**, 2 pour les **opérateurs binaires** ou 3 pour le seul et unique **opérateur ternaire**.

Ensuite, nous pouvons diviser les opérateurs en fonction du type d'opération qu'ils effectuent :

* opérateur d'assignation
* opérateurs arithmétiques
* opérateurs d'assignation composés
* opérateurs de comparaison
* opérateurs de plage
* opérateurs logiques

plus quelques autres plus avancés, incluant la coalescence de nil, le conditionnel ternaire, le débordement, les opérateurs bit à bit et point à point.

Note : Swift vous permet de créer vos propres opérateurs et de définir comment les opérateurs fonctionnent sur vos types.

### Opérateur d'assignation en Swift

Vous utilisez l'opérateur d'assignation pour assigner une valeur à une variable :

```swift
var age = 8
```

Ou pour assigner la valeur d'une variable à une autre variable :

```swift
var age = 8
var another = age
```

### Opérateurs arithmétiques en Swift

Swift a un certain nombre d'opérateurs arithmétiques binaires : `+`, `-`, `*`, `/` (division), `%` (reste) :

```swift
1 + 1 //2
2 - 1 //1
2 * 2 //4
4 / 2 //2
4 % 3 //1
4 % 2 //0
```

`-` fonctionne également comme un opérateur unaire moins :

```swift
let hotTemperature = 20
let freezingTemperature = -20
```

Vous pouvez également utiliser `+` pour concaténer des valeurs de type String :

```swift
"Roger" + " is a good dog"
```

### Opérateurs d'assignation composés en Swift

Les opérateurs d'assignation composés combinent l'opérateur d'assignation avec des opérateurs arithmétiques :

* `+=`
* `-=`
* `*=`
* `/=`
* `%=`

Exemple :

```swift
var age = 8
age += 1
```

### Opérateurs de comparaison en Swift

Swift définit quelques opérateurs de comparaison :

* `==`
* `!=`
* `>`
* `<`
* `>=`
* `<=`

Vous pouvez utiliser ces opérateurs pour obtenir une valeur booléenne (`true` ou `false`) en fonction du résultat :

```swift
let a = 1
let b = 2

a == b //false
a != b //true
a > b // false
a <= b //true
```

### Opérateurs de plage en Swift

Les opérateurs de plage sont utilisés dans les boucles. Ils nous permettent de définir une plage :

```swift
0...3 //4 fois
0..<3 //3 fois

0...count //"count" fois
0..<count //"count-1" fois
```

Voici un exemple d'utilisation :

```swift
let count = 3
for i in 0...count {
  //corps de la boucle
}
```

### Opérateurs logiques en Swift

Swift nous offre les opérateurs logiques suivants :

* `!`, l'opérateur unaire NOT
* `&&`, l'opérateur binaire AND
* `||`, l'opérateur binaire OR

Exemple d'utilisation :

```swift
let condition1 = true
let condition2 = false

!condition1 //false

condition1 && condition2 //false
condition1 || condition2 //true
```

Ceux-ci sont principalement utilisés dans l'évaluation de l'expression conditionnelle `if` :

```swift
if condition1 && condition2 {
  //corps de l'instruction if
}
```

## Conditionnels en Swift

### Instructions `if` en Swift

Les instructions `if` sont le moyen le plus populaire pour effectuer une vérification conditionnelle. Nous utilisons le mot-clé `if` suivi d'une expression booléenne, suivie d'un bloc contenant du code qui est exécuté si la condition est vraie :

```swift
let condition = true
if condition == true {
    // code exécuté si la condition est vraie
}
```

Un bloc `else` est exécuté si la condition est fausse :

```swift
let condition = true
if condition == true {
    // code exécuté si la condition est vraie
} else {
    // code exécuté si la condition est fausse
}
```

Vous pouvez optionnellement envelopper la validation de la condition dans des parenthèses si vous préférez :

```swift
if (condition == true) {
    // ...
}
```

Et vous pouvez aussi simplement écrire :

```swift
if condition {
    // s'exécute si `condition` est `true`
}
```

ou

```swift
if !condition {
    // s'exécute si `condition` est `false`
}
```

Une chose qui distingue Swift de nombreux autres langages est qu'il empêche les bugs causés par une affectation erronée au lieu d'une comparaison. Cela signifie que vous ne pouvez pas faire ceci :

```swift
if condition = true {
    // Le programme ne se compile pas
}
```

La raison est que l'opérateur d'affectation ne retourne rien, mais le conditionnel `if` doit être une expression booléenne.

### Instructions `switch` en Swift

Les instructions switch sont un moyen pratique de créer une conditionnelle avec plusieurs options :

```swift
var name = "Roger"

switch name {
case "Roger":
    print("Bonjour, monsieur Roger !")
default: 
    print("Bonjour, \(name)")
}
```

Lorsque le code d'un cas se termine, le switch se termine automatiquement.

Un switch en Swift doit couvrir tous les cas. Si le _tag_, `name` dans ce cas, est une chaîne qui peut avoir n'importe quelle valeur, nous devons ajouter un cas `default`, obligatoire.

Sinon, avec une énumération, vous pouvez simplement lister toutes les options :

```swift
enum Animal {
    case dog
    case cat
}

var animal: Animal = .dog

switch animal {
case .dog:
    print("Bonjour, chien !")
case .cat:
    print("Bonjour, chat !")
}
```

Un cas peut être une plage :

```swift
var age = 20

switch age {
case 0..<18:
    print("Tu ne peux pas conduire !!")
default: 
    print("Tu peux conduire")
}
```

### Opérateur conditionnel ternaire en Swift

L'opérateur conditionnel ternaire est une version plus courte d'une expression `if`. Il nous permet d'exécuter une expression si une condition est vraie, et une autre expression si la condition est fausse.

Voici la syntaxe :

```
`condition` ? `valeur si vrai` : `valeur si faux`
```

Exemple :

```swift
let num1 = 1
let num2 = 2

let smallerNumber = num1 < num2 ? num1 : num2 

// smallerNumber == 1
```

La syntaxe est plus courte qu'une instruction `if`, et parfois il peut être plus judicieux de l'utiliser.

## Boucles en Swift

### Boucles `for-in` en Swift

Vous pouvez utiliser les boucles `for-in` pour itérer un nombre spécifique de fois, en utilisant un opérateur de plage :

```swift
for index in 0...3 {
  //itère 4 fois, `index` est : 0, 1, 2, 3
}
```

Vous pouvez itérer sur les éléments d'un tableau ou d'un ensemble :

```swift
let list = ["a", "b", "c"]
for item in list {
  // `item` contient la valeur de l'élément
}
```

Et sur les éléments d'un dictionnaire :

```swift
let list = ["a": 1, "b": 2, "c": 2]
for (key, value) in list {
  // `key` contient la clé de l'élément
  // `value` contient la valeur de l'élément
}
```

### Boucles `while` en Swift

Une boucle `while` peut être utilisée pour itérer sur n'importe quoi, et s'exécutera tant que la condition est `true` :

```swift
while [condition] {
    //instructions...
}
```

La condition est vérifiée au début, avant que le bloc de la boucle ne soit exécuté.

Exemple :

```swift
var item = 0
while item <= 3 { //répète 3 fois
    print(item)
    item += 1
}
```

### Boucles `repeat-while` en Swift

Une boucle `repeat-while` en Swift est similaire à la boucle `while`. Mais dans ce cas, la condition est vérifiée à la fin, après le bloc de la boucle, donc le bloc de la boucle est exécuté au moins une fois. Ensuite, la condition est vérifiée, et si elle est évaluée à `true`, le bloc de la boucle est répété :

```swift
repeat {
    //instructions...
} while [condition]
```

Exemple :

```swift
var item = 0
repeat { //répète 3 fois
    print(item)
    item += 1
} while item < 3
```

### Instructions `continue` et `break` en Swift

Swift vous fournit 2 instructions que vous pouvez utiliser pour contrôler le flux à l'intérieur d'une boucle : `continue` et `break`.

Vous utilisez `continue` pour arrêter l'itération actuelle et exécuter l'itération suivante de la boucle.

`break` termine la boucle, sans exécuter aucune autre itération.

Exemple :

```swift
let list = ["a", "b", "c"]
for item in list {
  if (item == "b") {
    break
  }
  //faire quelque chose
}
```

## Comment écrire des commentaires en Swift

Un commentaire en Swift peut prendre 2 formes : un commentaire sur une seule ligne et un commentaire sur plusieurs lignes.

Un commentaire sur une seule ligne ressemble à ceci :

```swift
//ceci est un commentaire
```

et vous pouvez le mettre à la fin d'une ligne de code :

```swift
let a = 1 //ceci est un commentaire
```

Un commentaire sur plusieurs lignes est écrit en utilisant cette syntaxe :

```swift
/* ceci
 est
    un commentaire
 sur plusieurs lignes
*/
```

Swift vous permet d'imbriquer des commentaires sur plusieurs lignes :

```swift
/* ceci
 est
    un /* imbriqué */ commentaire
 sur plusieurs lignes
*/
```

Cela est pratique surtout lorsque vous commentez de grandes portions de code qui contiennent déjà des commentaires sur plusieurs lignes.

## Points-virgules en Swift

En Swift, les points-virgules sont généralement optionnels.

Vous pouvez écrire des instructions sur des lignes séparées, et vous n'avez pas besoin d'ajouter un point-virgule :

```swift
let list = ["a", "b", "c"]
var a = 2
```

Vous _pouvez_ ajouter un point-virgule, mais cela n'ajoute rien de significatif dans ce cas :

```swift
let list = ["a", "b", "c"];
var a = 2;
```

Mais si vous voulez écrire plus d'une instruction sur la même ligne, alors vous devez ajouter un point-virgule :

```swift
var a = 2; let b = 3
```

## Nombres en Swift

En Swift, les nombres ont 2 types principaux : `Int` et `Double`.

Un `Int` est un nombre sans point décimal. Un `Double` est un nombre avec un point décimal.

Les deux utilisent 64 bits sur les ordinateurs modernes qui fonctionnent avec 64 bits, et 32 bits sur les plateformes 32 bits.

La plage de valeurs qu'ils peuvent stocker dépend de la plateforme utilisée et peut être récupérée en utilisant la propriété `int` de chaque type :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screen-Shot-2020-11-02-at-07.41.09.png)
_Plage de valeurs int_

Ensuite, en plus de `Int` et `Double`, nous avons beaucoup d'autres types numériques. Ceux-ci étaient principalement utilisés pour interagir avec des API construites dans le passé et qui devaient interagir avec C ou Objective-C, et vous devez être conscient que nous les avons :

* `Int8` est un entier avec 8 bits
* `Int16` est un entier avec 16 bits
* `Int32` est un entier avec 32 bits
* `Int64` est un entier avec 64 bits
* `UInt8` est un entier non signé avec 8 bits
* `UInt16` est un entier non signé avec 16 bits
* `UInt32` est un entier non signé avec 32 bits
* `UInt64` est un entier non signé avec 64 bits
* `UInt` est comme `Int`, mais non signé, et il varie de 0 à `Int.max * 2`.
* `Float` est un nombre décimal avec 32 bits.

Ensuite, en utilisant les API Cocoa, vous pourriez utiliser d'autres types numériques comme CLong, CGFloat, et plus.

Vous utiliserez toujours `Int` ou `Double` dans votre code, et n'utiliserez ces types spécifiques que dans des cas particuliers.

Rappelez-vous que vous pouvez toujours convertir l'un de ces types en types `Int` et `Double`, en instantiant un nombre en passant la valeur entre parenthèses à `Double()` ou `Int()` :

```swift
let age : UInt8 = 3
let intAge = Int(age)
```

Vous pouvez également convertir un nombre de `Double` en `Int` :

```swift
let age = Double(3)
let count = Int(3.14)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screen-Shot-2020-11-02-at-07.59.19.png)
_Comment convertir un nombre de `Double` en `Int`_

## Chaînes de caractères en Swift

Les chaînes de caractères sont l'un des outils les plus populaires en programmation.

En Swift, vous pouvez définir une chaîne de caractères en utilisant la syntaxe littérale de chaîne :

```swift
let name = "Roger"
```

Nous utilisons des guillemets doubles. Les guillemets simples ne sont pas des délimiteurs de chaîne valides.

Une chaîne de caractères peut s'étendre sur plusieurs lignes en utilisant 3 guillemets doubles :

```swift
let description = """
	a long
  	long 
      	long description
	"""
```

Vous pouvez utiliser l'interpolation de chaînes pour intégrer une expression dans une chaîne :

```swift
let age = 8

let name = """
	Roger, age \(age)
	Next year he will be \(age + 1)
	"""
```

Vous pouvez concaténer deux chaînes avec l'opérateur `+` :

```swift
var name = "Roger"
name = name + " The Dog"
```

Et vous pouvez ajouter du texte à une chaîne avec l'opérateur `+=` :

```swift
var name = "Roger"
name += " The Dog"
```

Ou en utilisant la méthode `append(_:)` :

```swift
var name = "Roger"
name.append(" The Dog")
```

Vous pouvez compter les caractères dans une chaîne en utilisant la propriété `count` de la chaîne :

```swift
let name = "Roger"
name.count //5
```

Toute chaîne de caractères est livrée avec un ensemble de méthodes utiles, par exemple :

* `removeFirst()` pour supprimer le premier caractère
* `removeLast()` pour supprimer le dernier caractère
* `lowercased()` pour obtenir une nouvelle chaîne, en minuscules
* `uppercased()` pour obtenir une nouvelle chaîne, en majuscules
* `starts(with:)` qui retourne vrai si la chaîne commence par une sous-chaîne spécifique
* `contains()` qui retourne vrai si la chaîne contient un caractère spécifique

et bien d'autres.

Lorsque vous devez référencer un élément dans la chaîne, puisque les chaînes en Swift sont unicode, nous ne pouvons pas simplement référencer la lettre `o` dans `let name = "Roger"` en utilisant `name[1]`. Vous devez travailler avec des index.

Toute chaîne fournit l'index de départ avec la propriété `startIndex` :

```swift
let name = "Roger"
name.startIndex //0
```

Pour calculer un index spécifique dans la chaîne, vous le calculez en utilisant la méthode `index(i:offsetBy:)` :

```swift
let name = "Roger"
let i = name.index(name.startIndex, offsetBy: 2)
name[i] //"g"
```

Vous pouvez également utiliser l'index pour obtenir une sous-chaîne :

```swift
let name = "Roger"
let i = name.index(name.startIndex, offsetBy: 2)
name.suffix(from: i) //"ger"

//Ou en utilisant le sous-script :

name[i...] //"ger"
```

Lorsque vous obtenez une sous-chaîne à partir d'une chaîne, le type du résultat est `Substring`, et non `String`.

```swift
let name = "Roger"
let i = name.index(name.startIndex, offsetBy: 2)
print(type(of: name.suffix(from: i))) 
//Substring
```

Les sous-chaînes sont plus efficaces en mémoire, car vous n'obtenez pas une nouvelle chaîne, mais la même structure de mémoire est utilisée en arrière-plan. Mais vous devez être prudent lorsque vous manipulez beaucoup de chaînes, car il existe des optimisations que vous pouvez implémenter.

Les chaînes sont des collections et peuvent être itérées dans des boucles.

## Booléens en Swift

Swift fournit le type `Bool`, qui peut avoir deux valeurs : `true` et `false`.

```swift
var done = false
done = true
```

Les booléens sont particulièrement utiles avec les structures de contrôle conditionnelles comme les instructions `if` ou l'opérateur conditionnel ternaire :

```swift
var done = true

if done == true {
    //code
}
```

## Tableaux en Swift

Nous utilisons des tableaux pour créer une collection d'éléments.

Dans cet exemple, nous créons un tableau contenant 3 entiers :

```swift
var list = [1, 2, 3]
```

Nous pouvons accéder au premier élément en utilisant la syntaxe `list[0]`, au deuxième en utilisant `list[1]`, et ainsi de suite.

Les éléments dans un tableau en Swift doivent avoir le même type.

Le type peut être inféré si vous initialisez le tableau au moment de la déclaration, comme dans le cas ci-dessus.

Sinon, le type des valeurs qu'un tableau peut inclure doit être déclaré, de cette manière :

```swift
var list: [Int] = []
```

Une autre syntaxe abrégée est :

```swift
var list = [Int]()
```

Vous pouvez également déclarer explicitement le type à l'initialisation, comme ceci :

```swift
var list: [Int] = [1, 2, 3]
```

Un moyen rapide d'initialiser un tableau est d'utiliser l'opérateur de plage :

```swift
var list = Array(1...4) //[1, 2, 3, 4]
```

Pour obtenir le nombre d'éléments dans le tableau, utilisez la propriété `count` :

```swift
var list = [1, 2, 3]
list.count //3
```

Si un tableau est vide, sa propriété `isEmpty` est `true`.

```swift
var list = [1, 2, 3]
list.isEmpty //false
```

Vous pouvez ajouter un élément à la fin du tableau en utilisant la méthode `append()` :

```swift
var list: [Int] = [1, 2, 3]
list.append(4)
```

ou vous pouvez insérer un élément à n'importe quelle position du tableau en utilisant `insert(newElement: <Type> at: Int)` :

```swift
var list: [Int] = [1, 2, 3]
list.insert(17, at: 2)
//list est [1, 2, 17, 3]
```

Un tableau doit être déclaré comme `var` pour être modifié. S'il est déclaré avec `let`, vous ne pouvez pas le modifier en ajoutant ou en supprimant des éléments.

Pour supprimer un élément du tableau, utilisez `remove(at:)` en passant l'index de l'élément à supprimer :

```swift
var list: [Int] = [1, 2, 3]
list.remove(1)
//list est [1, 3]
```

`removeLast()` et `removeFirst()` sont deux moyens pratiques de supprimer le dernier et le premier élément.

Pour supprimer tous les éléments du tableau, vous pouvez utiliser `removeAll()` ou vous pouvez assigner un tableau vide :

```swift
var list: [Int] = [1, 2, 3]
list.removeAll()
//ou
list = []
```

La méthode `sort()` trie le tableau :

```swift
var list = [3, 1, 2]
list.sort()
//list est [1, 2, 3]
```

Il existe beaucoup d'autres méthodes, mais ce sont les bases.

Les tableaux sont égaux lorsqu'ils contiennent les mêmes éléments, du même type :

```swift
[1, 2, 3] == [1, 2, 3] //true
```

Les tableaux sont passés par valeur, ce qui signifie que si vous passez un tableau à une fonction, ou le retournez depuis une fonction, le tableau est copié.

Les tableaux sont des collections, et ils peuvent être itérés dans des boucles.

## Ensembles en Swift

Vous utilisez des ensembles pour créer des collections d'éléments non répétitifs.

Alors qu'un tableau peut contenir plusieurs fois le même élément, vous n'avez que des éléments uniques dans un ensemble.

Vous pouvez déclarer un ensemble de valeurs `Int` de cette manière :

```swift
let set: Set<Int> = [1, 2, 3]
```

ou vous pouvez l'initialiser à partir d'un tableau :

```swift
let set = Set([1, 2, 3])
```

Vous pouvez ajouter des éléments à l'ensemble en utilisant `insert()` :

```swift
var set = Set([1, 2, 3])
set.insert(17)
```

Contrairement aux tableaux, il n'y a pas d'ordre ou de position dans un ensemble. Les éléments sont récupérés et insérés de manière aléatoire.

Le moyen d'imprimer le contenu d'un ensemble de manière ordonnée est de le transformer en tableau en utilisant la méthode `sorted()` :

```swift
var set = Set([2, 1, 3])
let orderedList = set.sorted()
```

Pour vérifier si un ensemble contient un élément, utilisez la méthode `contains()` :

```swift
var set = Set([1, 2, 3])
set.contains(2) //true
```

Pour obtenir le nombre d'éléments dans l'ensemble, utilisez la propriété `count` :

```swift
let set = Set([1, 2, 3])
set.count //3
```

Si un ensemble est vide, sa propriété `isEmpty` est `true`.

```swift
let set = Set([1, 2, 3])
set.isEmpty //false
```

Pour supprimer un élément de l'ensemble, utilisez `remove()` en passant la valeur de l'élément :

```swift
var set = Set([1, 2, 3])
set.remove(1)
//set est [2, 3]
```

Pour supprimer tous les éléments de l'ensemble, vous pouvez utiliser `removeAll()` :

```swift
set.removeAll()
```

Les ensembles, comme les tableaux, sont passés par valeur. Cela signifie que si vous les passez à une fonction, ou les retournez depuis une fonction, l'ensemble est copié.

Les ensembles sont parfaits pour effectuer des opérations mathématiques sur les ensembles comme l'intersection, l'union, la soustraction, et plus encore.

Ces méthodes aident à cela :

* `intersection(_:)`
* `symmetricDifference(_:)`
* `union(_:)`
* `subtracting(_:)`
* `isSubset(of:)`
* `isSuperset(of:)`
* `isStrictSubset(of:)`
* `isStrictSuperset(of:)`
* `isDisjoint(with:)`

Les ensembles sont des collections, et ils peuvent être itérés dans des boucles.

## Dictionnaires en Swift

Nous utilisons des dictionnaires pour créer une collection de paires clé-valeur.

Voici comment créer un dictionnaire avec une paire clé-valeur, où la clé est une chaîne de caractères et la valeur est un entier :

```swift
var dict = ["Roger": 8, "Syd": 7]
```

Dans ce cas, le type est inféré. Vous pouvez également définir explicitement le type au moment de la déclaration :

```swift
var dict: [String: Int] = ["Roger": 8, "Syd": 7]
```

Dans cet exemple, nous créons un dictionnaire vide de clés Int et de valeurs String :

```swift
var dict = [String: Int]()

//ou

var dict: [String: Int] = [:]
```

Vous pouvez accéder à la valeur assignée à une clé en utilisant cette syntaxe :

```swift
var dict = ["Roger": 8, "Syd": 7]

dict["Roger"] //8
dict["Syd"] //7
```

Vous pouvez changer la valeur assignée à une clé de cette manière :

```swift
dict["Roger"] = 9
```

Un dictionnaire doit être déclaré comme `var` pour être modifié. S'il est déclaré avec `let`, vous ne pouvez pas le modifier en ajoutant ou en supprimant des éléments.

Utilisez la même syntaxe pour ajouter une nouvelle paire clé/valeur :

```swift
dict["Tina"] = 4
```

Pour supprimer une paire clé/valeur, assigner la valeur à `nil` :

```swift
dict["Tina"] = nil
```

Ou appelez la méthode `removeValue(forKey:)` :

```swift
dict.removeValue(forKey: "Tina")
```

Pour obtenir le nombre d'éléments dans le dictionnaire, utilisez la propriété `count` :

```swift
var dict = ["Roger": 8, "Syd": 7]
dict.count //2
```

Si un dictionnaire est vide, sa propriété `isEmpty` est `true`.

```swift
var dict = [String: Int]()
dict.isEmpty //true
```

Il existe de nombreuses méthodes liées aux dictionnaires, mais ce sont les bases.

Les dictionnaires sont passés par valeur, ce qui signifie que si vous les passez à une fonction, ou les retournez depuis une fonction, le dictionnaire est copié.

Les dictionnaires sont des collections, et ils peuvent être itérés dans des boucles.

## Tuples en Swift

Vous utilisez des tuples pour regrouper plusieurs valeurs dans une seule collection. Par exemple, vous pouvez déclarer une variable `dog` contenant une valeur de type String et une valeur de type Int :

```swift
let dog : (String, Int)
```

Et vous pouvez les initialiser avec un nom et un âge

```swift
let dog : (String, Int) = ("Roger", 8)
```

Mais comme pour toute autre variable, le type peut être inféré lors de l'initialisation :

```swift
let dog = ("Roger", 8)
```

Vous pouvez utiliser des éléments nommés :

```swift
let dog = (name: "Roger", age: 8)

dog.name //"Roger"
dog.age //8
```

Une fois qu'un tuple est défini, vous pouvez le décomposer en variables individuelles de cette manière :

```swift
let dog = ("Roger", 8)
let (name, age) = dog
```

et si vous avez besoin de récupérer seulement une des valeurs, vous pouvez utiliser le mot-clé spécial underscore pour ignorer les autres :

```swift
let dog = ("Roger", 8)
let (name, _) = dog
```

Les tuples sont un outil génial pour divers besoins.

Le plus évident est qu'ils sont un moyen court de regrouper des données similaires.

Un autre de ces besoins est de retourner plusieurs éléments depuis une fonction. Une fonction ne peut retourner qu'un seul élément, donc un tuple est une structure pratique pour cela.

Une autre fonctionnalité pratique permise par les tuples est l'échange d'éléments :

```swift
var a = 1
var b = 2

(a, b) = (b, a)

//a == 2
//b == 1
```

## Optionnels et `nil` en Swift

Les optionnels sont une caractéristique clé de Swift.

Lorsque vous ne savez pas si une valeur sera présente ou absente, vous déclarez le type comme un optionnel.

L'optionnel enveloppe une autre valeur avec son propre type. Ou peut-être pas.

Nous déclarons un optionnel en ajoutant un point d'interrogation après son type, comme ceci :

```swift
var value: Int? = 10
```

Maintenant `value` n'est pas une valeur Int. C'est un optionnel enveloppant une valeur Int.

Pour savoir si l'optionnel enveloppe une valeur, vous devez le **déballer**.

Vous le faites en utilisant un point d'exclamation :

```swift
var value: Int? = 10
print(value!) //10
```

Les méthodes Swift retournent souvent un optionnel. Par exemple, l'initialiseur de type `Int` accepte une chaîne et retourne un optionnel Int :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screen-Shot-2020-11-02-at-18.08.48.png)
_L'initialiseur de type Int prend une chaîne et retourne un optionnel int_

C'est parce qu'il ne sait pas si la chaîne peut être convertie en un nombre.

Si l'optionnel ne contient pas de valeur, il est évalué à `nil`, et vous ne pouvez pas le déballer :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screen-Shot-2020-11-02-at-18.12.13.png)
_Évaluation à `nil`_

`nil` est une valeur spéciale qui ne peut pas être assignée à une variable. Seulement à un optionnel :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screen-Shot-2020-11-02-at-18.14.21.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screen-Shot-2020-11-02-at-18.13.56-1.png)
_Vous ne pouvez assigner `nil` qu'à un optionnel (pas un int)_

Vous utilisez généralement des instructions `if` pour déballer des valeurs dans votre code, comme ceci :

```swift
var value: Int? = 2

if let age = value {
    print(age)
}
```

## Énumérations en Swift

Les énumérations sont un moyen de regrouper un ensemble d'options différentes sous un nom commun.

Exemple :

```swift
enum Animal {
    case dog
    case cat
    case mouse
    case horse
}
```

Cette énumération `Animal` est maintenant un **type**.

Un type dont la valeur ne peut être que l'un des cas listés.

Si vous définissez une variable de type `Animal` :

```swift
var animal: Animal
```

vous pouvez ensuite décider quelle valeur lui assigner en utilisant cette syntaxe :

```swift
var animal: Animal
animal = .dog
```

Nous pouvons utiliser des énumérations dans des structures de contrôle comme les switches :

```swift
enum Animal {
    case dog
    case cat
    case mouse
    case horse
}

let animal = Animal.dog

switch animal {
case .dog: print("dog")
case .cat: print("cat")
default: print("another animal")
}
```

Les valeurs d'énumération peuvent être des chaînes, des caractères ou des nombres.

Vous pouvez également définir une énumération sur une seule ligne :

```swift
enum Animal {
    case dog, cat, mouse, horse
}
```

Et vous pouvez également ajouter une déclaration de type à l'énumération, et chaque cas a une valeur de ce type assignée :

```swift
enum Animal: Int {
    case dog = 1
    case cat = 2
    case mouse = 3
    case horse = 4
}
```

Une fois que vous avez une variable, vous pouvez obtenir cette valeur en utilisant sa propriété `rawValue` :

```swift
enum Animal: Int {
    case dog = 1
    case cat = 2
    case mouse = 3
    case horse = 4
}

var animal: Animal
animal = .dog

animal.rawValue //1
```

Les énumérations sont un type de valeur. Cela signifie qu'elles sont copiées lorsqu'elles sont passées à une fonction, ou lorsqu'elles sont retournées par une fonction. Et lorsque nous assignons une variable pointant vers une énumération à une autre variable.

## Structures en Swift

Les structures sont un concept essentiel de Swift.

Les structures sont partout en Swift. Même les types intégrés sont des structures.

Nous pouvons créer des instances de structures, que nous appelons **objets**.

Dans la plupart des langages, les objets ne peuvent être créés qu'à partir de classes. Swift a aussi des classes, mais vous pouvez créer des objets également à partir de structures. La documentation officielle conseille même que vous devriez préférer les structures car elles sont plus faciles à utiliser.

Les structures sont une version légère des classes.

Une structure peut :

* avoir des propriétés
* avoir des méthodes (fonctions)
* définir des sous-scripts
* définir des initialiseurs
* se conformer à des protocoles
* être étendue

Une chose importante que les classes permettent est l'héritage, donc si vous en avez besoin, vous avez des classes.

Une structure est définie en utilisant cette syntaxe :

```swift
struct Dog {

}
```

À l'intérieur d'une structure, vous pouvez définir des **propriétés stockées** :

```swift
struct Dog {
    var age = 8
    var name = "Roger"
}
```

Cette définition de structure définit un **type**. Pour créer une nouvelle instance avec ce type, nous utilisons cette syntaxe :

```swift
let roger = Dog()
```

Une fois que vous avez une instance, vous pouvez accéder à ses propriétés en utilisant la syntaxe avec un point :

```swift
let roger = Dog()
roger.age
roger.name
```

La même syntaxe avec un point est utilisée pour mettre à jour une valeur de propriété :

```swift
roger.age = 9
```

Vous pouvez également créer une instance de structure en passant les valeurs des propriétés :

```swift
let syd = Dog(age: 7, name: "Syd")
syd.age
syd.name
```

Pour ce faire, les propriétés doivent être définies comme des variables avec `var`, et non comme des constantes (avec `let`). Il est également important de respecter l'ordre dans lequel ces propriétés sont définies.

Les structures peuvent avoir des **méthodes d'instance** : des fonctions qui appartiennent à une instance d'une structure.

```swift
struct Dog {
    var age = 8
    var name = "Roger"
    func bark() {
        print("\(name): wof!")
    }
}
```

Et nous avons également des **méthodes de type** :

```swift
struct Dog {
    var age = 8
    var name = "Roger"
    func bark() {
        print("\(name): wof!")
    }
    static func hello() {
        print("Hello I am the Dog struct")
    }
}
```

Cela est invoqué comme `Dog.hello()`.

Les structures sont un type de valeur. Cela signifie qu'elles sont copiées lorsqu'elles sont passées à une fonction, ou lorsqu'elles sont retournées par une fonction. Et lorsque nous assignons une variable pointant vers une structure à une autre variable.

Cela signifie également que si nous voulons mettre à jour les propriétés d'une structure, nous devons la définir en utilisant `var` et non `let`.

Tous les types en Swift sont définis comme des structures : Int, Double, String, tableaux et dictionnaires, et plus encore sont des structures.

## Classes en Swift

Les classes sont un peu similaires aux structures, mais elles ont quelques différences clés.

Une classe est définie en utilisant cette syntaxe :

```swift
class Dog {

}
```

À l'intérieur d'une classe, vous pouvez définir des propriétés stockées :

```swift
class Dog {
    var age = 0
}
```

Une définition de classe définit un **type**. Pour créer une nouvelle instance avec ce type, nous utilisons cette syntaxe :

```swift
let roger = Dog()
```

Une fois que vous avez une instance, vous pouvez accéder à ses propriétés en utilisant la syntaxe avec un point :

```swift
let roger = Dog()
roger.age
```

Vous utilisez la même syntaxe avec un point pour mettre à jour une valeur de propriété :

```swift
roger.age = 9
```

Une grande différence est que les classes sont des types de référence. Les structures (et les énumérations) sont des types de valeur.

Cela signifie que l'assignation d'une instance de classe à une autre variable ne copie pas l'instance. Les deux variables pointent vers la même instance :

```swift
class Dog {
    var age = 0
}

let roger = Dog()
let syd = roger

roger.age = 9
//syd.age == 9
```

Cela signifie également que nous pouvons définir une référence à une classe en utilisant `let`, et nous pouvons changer ses propriétés, comme vous l'avez vu dans l'exemple ci-dessus.

Nous pouvons créer des instances de classes, et nous les appelons **objets**.

Comme avec les structures, les classes peuvent avoir des propriétés, des méthodes, et plus encore.

Contrairement aux structures, nous **devons** définir un initialiseur afin d'initialiser les valeurs lorsque nous créons une instance :

```swift
class Dog {
    var age : Int
    
    init(age: Int) {
        self.age = age
    }
}

let roger = Dog(age: 9)
```

Vous ne pouvez déclarer des propriétés sans les initialiser que si vous avez un initialiseur.

Voir l'utilisation de `self`. Nous en avons besoin car `age` est à la fois une propriété d'instance et le paramètre de la méthode `init(age:)`. `self.age` fait référence à la propriété d'instance `age`.

Les classes peuvent avoir des **méthodes d'instance** : des fonctions qui appartiennent à une instance d'une classe.

```swift
class Dog {
    var age = 8
    var name = "Roger"

    func bark() {
      print("\(name): wof!")
    }
}
```

Et nous avons également des **méthodes de type** :

```swift
class Dog {
    var age = 8
    var name = "Roger"

    func bark() {
        print("\(name): wof!")
    }
    static func hello() {
        print("Hello I am the Dog struct")
    }
}
```

Invoqué comme `Dog.hello()`.

Une chose importante que les classes permettent est l'héritage.

Une classe peut hériter de toutes les propriétés et méthodes d'une autre classe.

Supposons que nous avons une classe `Animal`. Chaque animal a un âge :

```swift
class Animal {
    var age: Int
}
```

Tous les animaux n'ont pas de nom. Les chiens ont un nom. Nous créons donc une classe `Dog` qui étend `Animal` :

```swift
class Dog: Animal {
    var name: String
}
```

Maintenant, nous devons ajouter un initialiseur pour les deux classes. Dans le cas de Dog, après avoir fait l'initialisation spécifique à la classe, nous pouvons appeler l'initialiseur de la classe parente en utilisant `super.init()` :

```swift
class Animal {
    var age: Int
    
    init(age: Int) {
        self.age = age
    }
}

class Dog: Animal {
    var name: String
    
    init(age: Int, name: String) {
        self.name = name
        super.init(age: age)
    }
}

var horse = Animal(age: 8)
var roger = Dog(age: 8, name: "Roger")
```

`Animal` est maintenant une **superclasse**, et `Dog` est une **sous-classe**.

Il y a plus à dire sur les classes, mais c'est une bonne introduction.

## Fonctions en Swift

Le code de votre programme est organisé en fonctions.

Vous pouvez déclarer une fonction en utilisant le mot-clé `func` :

```swift
func bark() {
    print("woof!")
}
```

Les fonctions peuvent être assignées à des structures, des classes et des énumérations, et dans ce cas, nous les appelons méthodes.

Une fonction est invoquée en utilisant son nom :

```swift
bark()
```

Une fonction peut retourner une valeur :

```swift
func bark() -> String {
    print("woof!")
	  return "barked successfully"
}
```

Et vous pouvez l'assigner à une variable :

```swift
let result = bark()
```

Une fonction peut accepter des paramètres. Chaque paramètre a un nom et un type :

```swift
func bark(times: Int) {
    for index in 0..<times {
        print("woof!")
    }
}
```

Le nom d'un paramètre est interne à la fonction.

Nous utilisons le nom du paramètre lorsque nous appelons la fonction pour passer sa valeur :

```swift
bark(times: 3)
```

Lorsque nous appelons la fonction, nous devons passer tous les paramètres définis.

Voici une fonction qui accepte plusieurs paramètres :

```swift
func bark(times: Int, repeatBark: Bool) {
    for index in 0..<times {
        if repeatBark == true {
            print("woof woof!")
        } else {
            print("woof!")
        }            
    }
}
```

Dans ce cas, vous l'appelez de cette manière :

```swift
bark(times: 3, repeat: true)
```

Lorsque nous parlons de cette fonction, nous ne l'appelons pas `bark()`. Nous l'appelons `bark(times:repeat:)`.

C'est parce que nous pouvons avoir plusieurs fonctions avec le même nom, mais avec des ensembles de paramètres différents.

Vous pouvez éviter d'utiliser des étiquettes en utilisant le mot-clé `_` :

```swift
func bark(_ times: Int, repeatBark: Bool) {
    //...le corps de la fonction
}
```

Ainsi, vous pouvez l'invoquer de cette manière :

```swift
bark(3, repeat: true)
```

Il est courant dans les API Swift et iOS d'avoir le premier paramètre sans étiquette, et les autres paramètres étiquetés.

Cela permet de créer une API agréable et expressive, lorsque vous concevez bien les noms de la fonction et des paramètres.

Vous ne pouvez retourner qu'une seule valeur depuis une fonction. Si vous devez retourner plusieurs valeurs, il est courant de retourner un tuple :

```swift
func bark() -> (String, Int) {
    print("woof!")
	  return ("barked successfully", 1)
}
```

Et vous pouvez assigner le résultat à un tuple :

```swift
let (result, num) = bark()

print(result) //"barked successfully"
print(num) //1
```

Vous pouvez imbriquer des fonctions à l'intérieur d'autres fonctions. Lorsque cela se produit, la fonction interne est invisible à l'extérieur de la fonction externe.

## Protocoles en Swift

Un protocole est un moyen d'avoir différents objets, de différents types, ayant un ensemble commun de fonctionnalités.

Vous définissez un protocole comme ceci :

```swift
protocol Mammal {

}
```

Les structures et les classes peuvent **adopter un protocole** de cette manière :

```swift
struct Dog: Mammal {

}

class Cat: Mammal {

}
```

Un protocole peut définir des propriétés et des méthodes, sans fournir de valeurs et d'implémentations, et une structure/classe doit les implémenter :

```swift
protocol Mammal {
    var age: Int { get set }
    func walk()
}
```

La propriété peut être définie comme `get` ou `get set`. Si elle est `get`, la propriété doit être implémentée comme lecture seule, avec un getter.

Tout type qui adopte le protocole doit **se conformer** au protocole en implémentant ces méthodes ou en fournissant ces propriétés :

```swift
struct Dog: Mammal {
    var age: Int = 0
    func walk() {
        print("The dog is walking")
    }
}

class Cat: Mammal {
    var age: Int = 0
    func walk() {
        print("The cat is walking")
    }
}
```

Les structures et les classes peuvent adopter plusieurs protocoles :

```swift
struct Dog: Mammal, Animal {

}

class Cat: Mammal, Animal {

}
```

Remarquez que pour les classes, c'est la même syntaxe utilisée pour définir une superclasse. Si une superclasse existe, listez-la comme premier élément dans la liste, après le deux-points.

## Où aller à partir d'ici

J'espère que ce petit manuel a été utile pour éclairer comment commencer avec Swift. Et j'espère que vous êtes maintenant intéressé à en apprendre davantage à ce sujet !

Je peux maintenant vous orienter vers quelques endroits pour en apprendre plus :

* [Le guide officiel du langage Swift](https://docs.swift.org/swift-book/LanguageGuide/TheBasics.html)
* [La bibliothèque standard Swift](https://developer.apple.com/documentation/swift/swift-standard-library/)
* [Vidéos Swift de la WWDC](https://developer.apple.com/videos/swift)

[Vous pouvez obtenir une version PDF et ePub de ce manuel Swift pour débutants ici](https://thevalleyofcode.com/download/swift/).