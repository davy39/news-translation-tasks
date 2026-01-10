---
title: Les types optionnels en Swift – Comment utiliser et déballer les optionnels
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-05-06T16:06:35.000Z'
originalURL: https://freecodecamp.org/news/optional-types-in-swift
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/maxwell-nelson-taiuG8CPKAQ-unsplash.jpg
tags:
- name: Swift
  slug: swift
- name: Swift Programming
  slug: swift-programming
seo_title: Les types optionnels en Swift – Comment utiliser et déballer les optionnels
seo_desc: 'By Prajwal Kulkarni

  If you''re coming from Java, C++, or other object-oriented languages, chances are
  that you''ve never come across optional types or "optionals". And you might be quite
  surprised to know that such a concept exists in Swift.

  Optionals ...'
---

Par Prajwal Kulkarni

Si vous venez de Java, C++ ou d'autres langages orientés objet, il y a de fortes chances que vous n'ayez jamais rencontré de types optionnels ou d'« optionnels ». Et vous pourriez être assez surpris de savoir qu'un tel concept existe en Swift.

Les optionnels sont un sujet fondamental que vous devez comprendre en profondeur pour coder en Swift. Si vous débutez avec Swift et que vous découvrez les types optionnels pour la première fois, assurez-vous de lire cet article jusqu'à la fin.

Pour comprendre ce que sont les types optionnels, revoyons rapidement les **constantes** et les **variables.**

## Constantes et variables en Swift

Une constante est un élément de donnée dont la valeur, une fois assignée, ne peut pas être mutée (modifiée ou changée) tout au long de la portée du programme.

D'un autre côté, une variable est un élément de donnée dont la valeur peut être modifiée sans limite.

Il existe quelques nuances dans la façon de déclarer des constantes et des variables en Swift. Regardons cette syntaxe :

`<data-item-type> <var-name>:<data-type> = <value>`

**Voici un exemple de constante :**

`let pi:Double = 3.1415`

**Et voici un exemple de variable :**

```swift
var message:String = "Hello, this is prajwal"
message = "Coding in swift is awesome" // la valeur de la variable a changé.
```

Remarquez que parmi les mots-clés que nous avons utilisés ici pour déclarer des constantes et des variables, vous utilisez **let** pour déclarer une constante, et **var** pour déclarer une variable.

Le mot-clé est ensuite suivi du nom de la constante/variable, d'un deux-points et de son type de données, puis de la valeur d'assignation.

Swift est un langage à type sûr (type-safety), ce qui signifie que vous pouvez assigner des valeurs aux variables et aux constantes sans spécifier le type de données. Il peut faire des suppositions appropriées basées sur la valeur assignée, par exemple :

`let const:String = "String"`

peut aussi s'écrire,

`let const = "String"`

Et,

`var speed:Int = 20`

peut s'écrire,

`var speed = 35`

Vous vous demandez peut-être : si l'on peut omettre le type de données, pourquoi est-il nécessaire de le spécifier ? Eh bien, vous avez raison de vous poser la question – mais vous devez spécifier le type de données lorsque vous travaillez avec des types optionnels, qui sont différents des types de données conventionnels.

## Types optionnels ou Optionnels en Swift

Pour en venir au point principal, que sont les types optionnels en Swift ?

Voyons ce que la [documentation](https://docs.swift.org/swift-book/LanguageGuide/TheBasics.html) en dit :

> Vous utilisez des optionnels dans des situations où une valeur peut être absente. Un optionnel représente deux possibilités : soit il y a une valeur, et vous pouvez déballer l'optionnel pour accéder à cette valeur, soit il n'y a pas de valeur du tout.

C'est une définition assez simple. Les optionnels sont donc essentiellement utilisés pour gérer les valeurs nulles au moment de la compilation afin de s'assurer qu'aucun plantage ne se produise au moment de l'exécution.

Toute opération sur la variable optionnelle n'est effectuée que si elle contient des valeurs non nulles.

Un type optionnel peut être de n'importe quel type de données, comme une String, un Integer, un Double, un Float, ou tout type de données non primitif défini par l'utilisateur (objet).

Cependant, il est important de noter que le type de données Optionnel n'est pas équivalent à son type de données de base. Par exemple, une String optionnelle n'est pas la même chose qu'une chaîne de caractères, un entier optionnel n'est pas la même chose qu'un entier, et ainsi de suite. C'est parce que les types de données primitifs ne peuvent pas gérer les valeurs `nil`, contrairement aux types Optionnels.

## Syntaxe et utilisation des types optionnels en Swift

Voici la syntaxe pour un type optionnel :

`<data-item> <var-name>:<data-type>?`

La déclaration est similaire à celle des variables régulières, sauf que vous ajoutez un point d'interrogation (?) à côté du type de données, ce qui en fait un type Optionnel.

Lancez votre playground XCode et essayez d'exécuter ces extraits :

```
let someVal:Double?
someVal = 5.6324

print(someVal)
// Sortie : Optional(someVal)

var str:String? = nil

str = "Hello, World!"
print(str)
// Sortie : Optional("Hello, World!")
```

Vous pouvez voir que les sorties ne sont pas des valeurs régulières. Au lieu de cela, ce sont des valeurs optionnelles.

## Comment déballer les types optionnels en Swift

Vous n'utiliserez pas les types optionnels directement pour des opérations ou des tâches, car ils doivent être convertis dans leurs types primitifs ou instances définies par l'utilisateur avant d'être utilisés ailleurs (une chaîne optionnelle doit être convertie en chaîne, un entier optionnel en entier, etc.).

Cette conversion est ce qu'on appelle le **déballage (unwrapping).** Vous pouvez mieux comprendre ce concept en pensant au chat de Schrödinger.

Dans cette expérience de pensée, un chat est placé dans une boîte fermée avec une fiole de poison. Tant que vous n'ouvrez pas la boîte, vous ne pouvez pas affirmer si le chat est mort ou vivant (nil ou non-nil). Cela signifie qu'il est à la fois mort et vivant en même temps (nil et non-nil) selon votre perception.

Ce n'est que lorsque vous ouvrez la boîte (déballage) que vous pouvez savoir si le chat est vivant ou non (nil ou pas).

Le déballage en Swift consiste essentiellement à vérifier si la valeur Optionnelle est nil ou non, puis à n'effectuer une tâche que si elle n'est pas nil.

Vous pouvez effectuer le déballage de la manière suivante :

<ol type=1>
    <li>Utilisation d'un bloc if-else</li>
    <li>Utilisation du déballage forcé (Forced unwrapping)</li>
    <li>Utilisation de la liaison optionnelle (Optional binding)</li>
    <li>Utilisation du chaînage optionnel (Optional chaining)</li>
    <li>Utilisation de l'opérateur de fusion nil (nil coalescing)</li>
</ol>

### Déballer un type optionnel avec un bloc if-else

Déballer signifie s'assurer que la valeur Optionnelle n'est pas nil. Vous pouvez le faire en utilisant un simple bloc if-else comme ceci :

```swift
var variable:String? // évalué à nil

if variable != nil{
 print("Non nil")
}
else{
 print("Nil")
}
// Sortie : Nil
```

### Déballer un type optionnel avec le déballage forcé

Le déballage forcé est assez contradictoire car vous accédez à la valeur optionnelle quelle que soit sa valeur (nil ou non nil). Si un optionnel nil est déballé, une erreur est générée indiquant "**Unexpectedly found nil while unwrapping an Optional value**."

Vous êtes censé utiliser le déballage forcé uniquement dans un environnement prédéfini où vous êtes certain que la valeur optionnelle ne sera pas nil.

Vous pouvez déballer de force un optionnel en utilisant l'opérateur d'exclamation (!) comme ceci :

```swift
var color:String?;

print(color!) // Unexpectedly found nil while unwrapping an Optional value

color = "Black";

print(color!) // Noir
```

### Déballer un type optionnel avec la liaison optionnelle

La liaison optionnelle (optional binding) est similaire à l'utilisation d'un bloc if-else. La seule différence subtile est que si la valeur optionnelle n'est pas nil, la valeur déballée est assignée à une nouvelle constante et les opérations ultérieures sont effectuées sur cette constante.

Vous pouvez le faire en utilisant l'instruction **if-let** :

```swift
var password:String? = "$tr0ngp@$$w0rd"

if let unwrappedpass = password {
	print("Le mot de passe est \(unwrappedpass)") // Le mot de passe est $tr0ngp@$$w0rd
}
```

Une chaîne optionnelle `password` se voit assigner la valeur `$tr0ngp@$$w0rd`. Ensuite, dans le bloc if-let, la valeur optionnelle `password` est déballée et assignée à la variable `unwrappedpass` uniquement si la valeur optionnelle `password` n'est pas nil. `unwrappedpass` contient maintenant la valeur déballée et peut être utilisée dans la portée du bloc.

```swift
var password:String?

if let unwrap = password{ // Bloc non exécuté, car le mot de passe optionnel est nil.
	print("la valeur n'est pas nil")
}
```

### Déballer un type optionnel avec le chaînage optionnel

Vous utilisez le chaînage optionnel (optional chaining) lorsque vous traitez plusieurs valeurs optionnelles à la fois. Vous l'utilisez pour accéder, modifier ou assigner des attributs imbriqués dont la valeur dépend d'autres contraintes.

Par exemple, nous tirons notre nourriture des plantes, qui à leur tour tirent leur nourriture de la lumière du soleil et de l'eau.

Cela signifie qu'il existe une dépendance en chaîne d'événements – nous dépendons des plantes pour notre nourriture, et les plantes elles-mêmes dépendent de l'eau et de la lumière pour la leur.

Le chaînage optionnel consiste à vérifier à chaque dépendance si l'instance est nil ou non.

Voyons comment cela fonctionne avec un exemple de code :

```swift
class ShipmentCar{
    var seats:Int?
    var quality:String?
    
    init(seatQty:Int){
        seats = seatQty
    }

    func displaySeatQuality(){
        if let seatQuality = quality{
            print("Le revêtement du siège est en : \(seatQuality)")
        }
    }

    

}

class CheckSeats{
    var seatExists:ShipmentCar?

}


var obj = ShipmentCar(seatQty:4)
var obj2:CheckSeats?
obj2 = CheckSeats()
obj2?.seatExists = obj
obj2?.seatExists?.quality = "Leather" // Chaînage optionnel, définit la qualité du cuir des sièges, seulement si les sièges existent.
obj.displaySeatQuality()
// Sortie : Le revêtement du siège est en : Cuir
```

Dans l'exemple ci-dessus, nous avons deux classes, `ShipmentCar` qui représente le chargement, et `CheckSeats` pour vérifier s'il y a des sièges dans le véhicule.

Nous créons d'abord une instance de la classe `ShipmentCar` et passons l'argument 4 pour le nombre de sièges – ce qui signifie qu'il y a 4 sièges dans le véhicule.

Ensuite, nous créons une instance optionnelle de la classe `CheckSeats` et l'instancions. L'attribut `seatExists` de la classe `CheckSeats` est de type optionnel `ShipmentCar`.

Ensuite, nous effectuons un chaînage optionnel sur l'instance `obj2`, que nous écrivons `obj2?.seatExists?.quality = "Leather"`. Cela signifie que nous vérifions si des sièges existent dans la voiture, et si c'est le cas, nous définissons la qualité de la housse de siège comme étant `Leather`. Enfin, nous vérifions en appelant `displaySeatQuality` et obtenons le résultat souhaité.

**Voici une petite mise en garde** : dans l'exemple ci-dessus, si vous définissiez la valeur de `seatQty` à 0 au lieu de 4, le résultat serait toujours le même. Cela impliquerait que les housses de siège sont en cuir même s'il y a 0 siège, ce qui n'aurait aucun sens.

Je tiens donc à préciser qu'il ne s'agit que d'un exemple et que l'objectif principal ici est de souligner que les attributs ne reçoivent des valeurs que si les attributs dépendants ne sont pas nil.

### Déballer un type optionnel avec l'opérateur de fusion nil

L'opérateur de fusion nil (nil coalescing operator) fonctionne comme une notation abrégée du bloc if-else classique. Si une valeur nil est trouvée lors du déballage d'une valeur optionnelle, une valeur par défaut supplémentaire est fournie et sera utilisée à la place.

```
var text:String?

var output = text ?? "Default value"

print(output) // Valeur par défaut

text = "This is a string"

output = text ?? "Default String"

print(output) // Ceci est une chaîne
```

Vous pouvez également écrire des valeurs par défaut sous forme d'objets.

## Conclusion

Et voilà ! Dans cet article, vous avez tout appris sur les types optionnels et comment les utiliser.

Je tiens à vous remercier d'avoir lu jusqu'ici et j'espère que cet article vous a aidé à comprendre les types optionnels en Swift.

Si vous avez des questions, n'hésitez pas à me contacter sur [Twitter](https://twitter.com/prajwalinbizz) et/ou [LinkedIn](https://www.linkedin.com/in/prajwal-kulkarni). Je serai ravi de vous aider. Merci !