---
title: Programmation Fonctionnelle pour les Développeurs Android — Partie 3
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-06-06T05:21:43.000Z'
originalURL: https://freecodecamp.org/news/functional-programming-for-android-developers-part-3-f9e521e96788
coverImage: https://cdn-media-1.freecodecamp.org/images/1*exgznl7z65gttRxLsMAV2A.png
tags:
- name: Android
  slug: android
- name: android app development
  slug: android-app-development
- name: Functional Programming
  slug: functional-programming
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Programmation Fonctionnelle pour les Développeurs Android — Partie 3
seo_desc: 'By Anup Cowkur

  In the last post, we learned about immutability and concurrency. In this one, we’ll
  look at Higher Order Functions and Closures.

  If you haven’t read part 2, please read it here:

  Functional Programming for Android Developers — Part 2_In...'
---

Par Anup Cowkur

Dans le dernier article, nous avons appris l'_immutabilité_ et la _concurence_. Dans celui-ci, nous allons examiner les _Fonctions d'Ordre Supérieur_ et les _Fermetures_.

Si vous n'avez pas lu la partie 2, veuillez la lire ici :

[**Programmation Fonctionnelle pour les Développeurs Android — Partie 2**](https://medium.freecodecamp.com/functional-programming-for-android-developers-part-2-5c0834669d1a)
[_Dans le dernier article, nous avons appris la Pureté, les Effets de bord et l'Ordonnancement. Dans cette partie, parlons de l'immutabilité et…_medium.freecodecamp.com](https://medium.freecodecamp.com/functional-programming-for-android-developers-part-2-5c0834669d1a)

### Fonctions d'Ordre Supérieur

Les Fonctions d'Ordre Supérieur sont des fonctions qui peuvent prendre des fonctions comme paramètres et retourner des fonctions comme résultats. Cool, non ?

Mais pourquoi quelqu'un voudrait-il faire cela ?

Prenons un exemple. Supposons que je veux compresser un ensemble de fichiers. Je veux le faire de deux manières — en utilisant le format ZIP ou RAR. Pour faire cela en Java traditionnel, nous utiliserions quelque chose comme le [Modèle de Stratégie](https://en.wikipedia.org/wiki/Strategy_pattern).

Tout d'abord, je créerais une interface qui définit la stratégie :

```
public interface CompressionStrategy {
    void compress(List<File> files);
}
```

Ensuite, j'implémenterais les deux stratégies comme suit :

```
public class ZipCompressionStrategy implements CompressionStrategy {
    @Override public void compress(List<File> files) {
        // Faire des trucs ZIP
    }
}
```

```
public class RarCompressionStrategy implements CompressionStrategy {
    @Override public void compress(List<File> files) {
        // Faire des trucs RAR
    }
}
```

Ensuite, à l'exécution, je peux utiliser l'une de ces stratégies :

```
public CompressionStrategy decideStrategy(Strategy strategy) {
    switch (strategy) {
        case ZIP:
            return new ZipCompressionStrategy();
        case RAR:
            return new RarCompressionStrategy();
    }
}
```

C'est beaucoup de code et de cérémonie.

Tout ce que nous essayons de faire ici, c'est d'essayer de faire deux bits différents de logique métier en fonction d'une variable. Comme la logique métier ne peut pas vivre seule en Java, nous devons l'habiller dans des classes et des interfaces.

Ne serait-ce pas génial si nous pouvions passer directement la logique métier ? C'est-à-dire, si nous pouvions traiter les fonctions comme des variables, pourrions-nous passer la logique métier aussi facilement que des variables et des données ?

C'est **exactement** à cela que servent les fonctions d'ordre supérieur !

Regardons le même exemple avec les Fonctions d'Ordre Supérieur. Je vais utiliser [Kotlin](https://kotlinlang.org/) ici, puisque les lambdas de Java 8 impliquent encore [une certaine cérémonie de création d'interfaces fonctionnelles](https://stackoverflow.com/a/13604748/1369222) que nous aimerions éviter.

```
fun compress(files: List<File>, applyStrategy: (List<File>) -> CompressedFiles){
    applyStrategy(files)
}
```

La méthode `compress` prend deux paramètres — une liste de fichiers et une fonction appelée `applyStrategy` qui est une fonction de type `List<File> -> CompressedFiles`. C'est-à-dire, c'est une fonction qui prend une liste de fichiers et retourne `CompressedFiles`.

Maintenant, nous pouvons appeler `compress` avec n'importe quelle fonction qui prend une liste de fichiers et retourne des fichiers compressés :

```
compress(fileList, {files -> // ZIP it})
```

```
compress(fileList, {files -> // RAR it})
```

Mieux. Bien mieux.

Ainsi, les Fonctions d'Ordre Supérieur nous permettent de passer la logique et de traiter le code comme des données. Sympa.

### Fermetures

Les Fermetures sont des fonctions qui capturent leur environnement. Comprenons cela avec un exemple. Supposons que j'ai un écouteur de clic sur une vue et que nous voulons imprimer une valeur à l'intérieur :

```
int x = 5;
view.setOnClickListener(new View.OnClickListener() {
    @Override public void onClick(View v) {
        System.out.println(x);
    }
});
```

Java ne nous permettra pas de faire cela puisque `x` n'est pas final. `x` doit être final en Java puisque l'écouteur de clic peut être exécuté à tout moment et au moment où il est exécuté, `x` pourrait ne plus être présent ou sa valeur pourrait avoir changé. Java nous force à rendre cette variable finale pour la rendre effectivement immuable.

Une fois qu'elle est immuable, Java saura que `x` sera toujours `5` chaque fois que l'écouteur de clic est exécuté. Ce système n'est pas parfait puisque `x` peut pointer vers une liste qui peut être mutée même si la référence à la liste est la même.

Java n'a pas de mécanisme pour qu'une fonction capture et réponde aux variables qui sont en dehors de sa portée. Les fonctions Java ne peuvent pas capturer ou _fermer_ leur environnement.

Essayons de faire la même chose en Kotlin. Nous n'avons même pas besoin d'une classe interne anonyme puisque nous avons des fonctions de première classe en Kotlin :

```
var x = 5
view.setOnClickListener { println(x) }
```

Cela est parfaitement valide en Kotlin. Les fonctions en Kotlin sont des _fermetures_. Elles peuvent suivre et répondre aux mises à jour de leur environnement.

La première fois que l'écouteur de clic est déclenché, il imprimera `5`. Si nous changeons ensuite la valeur de `x` et disons `x = 9` et déclenchons à nouveau l'écouteur de clic, il imprimera `9` cette fois.

#### Que puis-je faire avec ces fermetures ?

Les Fermetures ont de nombreux cas d'utilisation astucieux. Chaque fois que vous voulez que la logique métier réponde à un état dans l'environnement, vous pouvez utiliser des fermetures.

Supposons que vous avez un écouteur de clic sur un bouton qui montre une boîte de dialogue avec un ensemble de messages à l'utilisateur. Si vous n'avez pas de fermetures, vous devriez initialiser un nouvel écouteur avec la nouvelle liste de messages chaque fois que les messages changent.

Avec les fermetures, vous pouvez stocker la liste de messages quelque part et passer la référence à la liste dans l'écouteur, comme nous l'avons fait ci-dessus, et l'écouteur montrera toujours le dernier ensemble de messages.

**Les Fermetures peuvent également être utilisées pour remplacer complètement les objets.** Cela est souvent utilisé dans les langages fonctionnels où vous pourriez avoir besoin d'un comportement de type OOP et le langage ne les supporte pas.

Prenons un exemple :

```
class Dog {
    private var weight: Int = 10
    fun eat(food: Int) {
        weight += food
    }
    fun workout(intensity: Int) {
        weight -= intensity
    }
}
```

J'ai un chien qui prend du poids quand nous le nourrissons et perd du poids quand il fait de l'exercice. Pouvez-nous décrire le même comportement avec des fermetures ?

```
fun main(args: Array<String>) {
   dog(Action.feed)(5)
}
```

```
val dog = { action: Action ->
    var weight: Int = 10
```

```
when (action) {
        Action.feed -> { food: Int -> weight += food; println(weight) }
        Action.workout -> { intensity: Int -> weight -= intensity; println(weight) }
    }
}
```

```
enum class Action {
    feed, workout
}
```

La fonction `dog` prend une `Action` et, en fonction de l'action, nourrira le chien ou le fera faire de l'exercice. Lorsque nous appelons `dog(Action.feed)(5)` dans la fonction `main`, le résultat sera `15`. La fonction `dog` prend une action `feed` et retourne une autre fonction qui nourrira le chien. Lorsque nous passons la valeur `5` à cette fonction retournée, elle incrémentera le poids du chien à `10 + 5 = 15` et l'imprimera.

> Ainsi, en combinant les Fermetures et les Fonctions d'Ordre Supérieur, nous pouvons obtenir des Objets sans OOP.

![Image](https://cdn-media-1.freecodecamp.org/images/3kHTFLmBq02uXvhIh4MNZingIOakRfXUKnNK)

Vous ne voulez probablement pas faire cela dans du code réel, mais c'est amusant de savoir que cela peut être fait. En effet, les Fermetures sont appelées les [_objets du pauvre_](http://wiki.c2.com/?ClosuresAndObjectsAreEquivalent).

### Résumé

Les Fonctions d'Ordre Supérieur nous permettent d'encapsuler la logique métier mieux que l'OOP dans de nombreux cas et nous pouvons les passer et les traiter comme des données. Les Fermetures capturent leur environnement et nous aident à utiliser les Fonctions d'Ordre Supérieur efficacement.

Dans la prochaine partie, nous apprendrons la gestion des erreurs de manière fonctionnelle.

_Si vous avez aimé cela, cliquez sur le ? ci-dessous. Je remarque chacun d'eux et je suis reconnaissant pour chacun d'eux._

_Pour plus de réflexions sur la programmation, suivez-moi pour être informé lorsque j'écrirai de nouveaux articles._