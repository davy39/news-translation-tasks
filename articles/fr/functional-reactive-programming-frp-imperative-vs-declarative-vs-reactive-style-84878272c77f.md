---
title: Une introduction rapide à la programmation réactive fonctionnelle (FRP)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-11T11:26:26.000Z'
originalURL: https://freecodecamp.org/news/functional-reactive-programming-frp-imperative-vs-declarative-vs-reactive-style-84878272c77f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2K8v7kw0Nz1ncohxmil5KA.png
tags:
- name: Functional Programming
  slug: functional-programming
- name: General Programming
  slug: programming
- name: Reactive Programming
  slug: reactive-programming
- name: Swift
  slug: swift
- name: technology
  slug: technology
seo_title: Une introduction rapide à la programmation réactive fonctionnelle (FRP)
seo_desc: 'By Navdeep Singh

  FRP represents an intersection of two programming paradigms. But, before we dig
  deeper into the concepts, we need to know a bit more about some basic terms.


  FRP: reacting to events

  Imperative programming

  Traditionally, we write code...'
---

Par Navdeep Singh

FRP représente une intersection de deux paradigmes de programmation. Mais, avant d'approfondir les concepts, nous devons en savoir un peu plus sur certains termes de base.

![Image](https://cdn-media-1.freecodecamp.org/images/zmvecVovUlqx5GTj1gMqLVhLKHEiES7Fy42x)
_FRP : réagir aux événements_

### Programmation impérative

Traditionnellement, nous écrivons du code qui décrit comment il doit résoudre un problème. Chaque ligne de code est exécutée séquentiellement pour produire un résultat souhaité, ce qui est connu sous le nom de programmation impérative. Le paradigme impératif oblige les programmeurs à écrire « comment » un programme va résoudre une certaine tâche. Notez que dans la déclaration précédente, le mot clé est « comment ».

Voici un exemple :

```
let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
var numbersLessThanFive = [Int]()
for index in 0..<numbers.count
    {
    if numbers[index] < 5
        {
        numbersLessThanFive.append(numbers[index])
        }
    }
```

Comme vous pouvez le voir, nous exécutons séquentiellement une série d'instructions pour produire une sortie souhaitée.

### Programmation fonctionnelle

La programmation fonctionnelle est un paradigme de programmation où vous modélisez tout comme résultat d'une fonction qui évite de changer d'état et de muter les données. Nous discuterons des concepts tels que l'état et la mutabilité des données et de leur importance dans les sections suivantes, mais pour référence :

* considérez l'**état** comme l'une des différentes permutations et combinaisons que votre programme peut avoir à un moment donné pendant son exécution
* la **mutabilité des données** est le concept où un ensemble de données donné peut changer au cours d'un laps de temps donné pendant l'exécution du programme.

Le même exemple qui a été donné en utilisant la programmation impérative peut être utilisé de la manière suivante en utilisant l'approche fonctionnelle :

```
let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
let numbersLessThanFive = numbers.filter { $0 < 5 }
```

Nous alimentons la fonction filter avec une fermeture contenant un certain critère. Ce critère est ensuite appliqué à chaque élément du tableau numbers, et le tableau résultant contient les éléments qui satisfont nos critères.

**Remarquez la déclaration des deux tableaux dans les deux exemples.**

Dans le premier exemple, le tableau `numbersLessThanFive` a été déclaré comme un `var`, alors que dans le second exemple, le même tableau a été déclaré comme un `let`.

Cela vous dit quelque chose ?

Quelle approche est meilleure, quel tableau est plus sûr à utiliser ?

Et si plus d'un thread essayait de travailler avec le même tableau et ses éléments ?

Un tableau constant n'est-il pas plus fiable ?

### Programmation réactive

La programmation réactive est la pratique de la programmation avec des flux de données asynchrones ou des flux d'événements. Un **flux d'événements** peut être n'importe quoi comme des entrées clavier, des taps sur des boutons, des gestes, des mises à jour de localisation GPS, un accéléromètre et un iBeacon. Vous pouvez écouter un flux et réagir en conséquence.

Vous avez peut-être entendu parler de la programmation réactive, mais cela a peut-être semblé trop intimidant, effrayant ou cryptique pour même essayer. Vous avez peut-être vu quelque chose comme ceci :

```
var twoDimensionalArray = [ [1, 2], [3, 4], [5, 6] ]
let flatArray = twoDimensionalArray.flatMap { array in
    return array.map { integer in
        return integer * 2
    }}
print(flatArray)
Output : [2, 4, 6, 8, 10, 12]
```

À première vue, le code précédent peut sembler un peu obscur, et cela peut être la raison pour laquelle vous avez tourné le dos à ce style de programmation. La programmation réactive, comme nous l'avons mentionné précédemment, est la programmation avec des flux d'événements.

Cependant, la question plus importante reste sans réponse. **Qu'est-ce que la programmation réactive fonctionnelle (FRP) ?**

FRP est la **combinaison** des paradigmes fonctionnel et réactif. En d'autres termes, il s'agit de réagir aux flux de données en utilisant le paradigme fonctionnel. FRP n'est pas un utilitaire ou une bibliothèque — il change la façon dont vous architectez vos applications et la façon dont vous pensez à vos applications.

Dans le prochain blog, je parlerai des blocs de construction de base de la programmation réactive — en attendant, restez à l'écoute et bon lecture :)

Pour avoir une solide compréhension des concepts réactifs et écrire des applications iOS en RxSwift, vous pouvez lire mon livre : [Reactive programming in Swift 4](https://www.amazon.com/Reactive-Programming-Swift-easy-maintain-ebook/dp/B078MHNSL1/ref=asap_bc?ie=UTF8).

Plus de mes projets et du code téléchargeable sont dans [mes dépôts publics github](https://github.com/NavdeepSinghh)

Vous pouvez lire plus sur le sujet [ici](https://gist.github.com/staltz/868e7e9bc2a7b8c1f754)

Merci d'avoir lu, veuillez le partager si vous l'avez trouvé utile :)