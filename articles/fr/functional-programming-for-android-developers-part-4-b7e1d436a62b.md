---
title: Programmation fonctionnelle pour les développeurs Android — Partie 4
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-07T11:51:59.000Z'
originalURL: https://freecodecamp.org/news/functional-programming-for-android-developers-part-4-b7e1d436a62b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*P4uiwrwGsjs6pDls38RTZw.jpeg
tags:
- name: Android
  slug: android
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Programmation fonctionnelle pour les développeurs Android — Partie 4
seo_desc: 'By Anup Cowkur

  In the last post, we learned about higher order functions and closures. In this
  one, we’ll talk about functional error handling.

  If you haven’t read part 3, please read it here.

  Functional error handling

  If you’ve been following this s...'
---

Par Anup Cowkur

Dans le dernier article, nous avons appris les fonctions d'ordre supérieur et les fermetures. Dans celui-ci, nous allons parler de la gestion fonctionnelle des erreurs.

Si vous n'avez pas lu la partie 3, veuillez la lire [ici](https://medium.freecodecamp.org/functional-programming-for-android-developers-part-3-f9e521e96788).

### Gestion fonctionnelle des erreurs

Si vous avez suivi cette série jusqu'à présent, vous avez peut-être remarqué un thème récurrent en programmation fonctionnelle : Tout est un calcul ou une valeur.

Nous créons des fonctions qui peuvent optionnellement prendre certaines valeurs. Elles effectuent ensuite un calcul utile et retournent d'autres valeurs.

Dans la plupart des programmations OOP, nous traitons les erreurs comme des exceptions — des choses qui ne font pas partie du résultat du calcul. La grande différence en programmation fonctionnelle est que nous modélisons les erreurs comme n'importe quelle autre valeur. Les erreurs font partie intégrante du calcul, pas des agents de mal extérieurs qui apparaissent de nulle part.

Voici un exemple de gestion typique des erreurs en OOP :

```
try {  result = readFromDB()} catch (e: Exception) {  result = null}
```

Le résultat de la fonction `readFromDb` est une erreur, mais elle n'est pas représentée comme un résultat du calcul. Au lieu de cela, c'est un effet secondaire géré ailleurs dans le bloc catch.

Ce type de code est très difficile à analyser et à comprendre lorsqu'il y a plusieurs opérations dans une séquence qui peuvent produire des erreurs (ce qui est un cas très courant) :

```
try {   data = readFromDB()   newData = doSomethingWithData(data)   isSuccess = putModifiedDataInDb(newData)} catch (e: Exception) {   // Quelle est l'opération qui a provoqué cette exception ?   isSuccess = false}
```

Si l'une de ces opérations échoue, il est vraiment difficile de détecter laquelle a échoué, sauf si vous mettez un try catch autour de chaque opération. De plus, si les opérations futures dépendent du résultat des opérations précédentes, vous devrez alors conserver l'état de savoir si les opérations précédentes ont échoué ou non avant d'exécuter les opérations futures :

```
fun updateDbData(): Boolean {    try {       data = readFromDb()    } catch (e: Exception) {       data = null    }        if(data == null) {        return false    }        try {       newData = doSomethingWithData(data)    } catch (e: Exception) {        newData = null    }        if(newData == null) {        return false    }        try {       return putModifiedDataInDb(newData)    } catch (e: Exception) {        return false    }     }
```

Beurk.

#### Comment améliorer cela de manière fonctionnelle ?

C'est simple, modélisons les échecs comme faisant partie du résultat de l'opération elle-même au lieu d'un processus hors bande.

De nombreux langages fonctionnels ont également une gestion des exceptions, mais il est généralement encouragé de les ignorer. Il est beaucoup plus facile de raisonner sur un code où les échecs et les succès font partie intégrante du calcul lui-même.

Voyons à quoi cela ressemble. Créons une [classe de données Kotlin](https://kotlinlang.org/docs/reference/data-classes.html) qui encapsule le résultat de notre opération. Cette classe conservera l'état de l'état de succès/échec ainsi que les données de résultat :

```
data class Result(val data: Data = Data(), val success: Boolean = false)
```

`success` nous indiquera si l'opération a réussi ou échoué. `data` est la donnée dont nous avons besoin à partir du calcul. Nous n'y accédons que si la valeur `success` est `true` (si l'opération a réussi).

Utilisons cela pour modéliser notre exemple précédent :

```
fun updateDbData(): Boolean {       val result1 = readFromDb()       if(!result1.success) {        return false    }        val result2 = doSomethingWithData(result1.data)       if(!result2.success) {        return false    }        val result3 = putModifiedDataInDb(result2.data)       if(!result3.success) {        return false    }        return true}
```

Beaucoup mieux.

Tout ce que nous avons fait ici est d'encapsuler les erreurs de calcul comme faisant partie du calcul naturel.

Félicitations ! Nous venons de construire une monade **Maybe** !

Une monade Maybe représente la présence ou l'absence d'une valeur (d'où le nom maybe) ce qui la rend parfaite pour représenter des calculs qui n'ont des données de résultat que s'ils réussissent.

Mais attendez ! Pourquoi avons-nous besoin de la variable `success` ? Si nous utilisons le type nullable de Kotlin pour représenter l'objet `Data`, nous pouvons nous assurer que les données ne sont présentes que si le calcul réussit.

Notre classe `Result` devient donc :

```
data class Result(val data: Data?)
```

et notre fonction devient :

```
fun updateDbData(): Boolean {       val result1 = readFromDb()       if(result1.data == null) {        return false    }        val result2 = doSomethingWithData(result1.data)       if(result2.data == null) {        return false    }        val result3 = putModifiedDataInDb(result2.data)       if(result3.data == null) {        return false    }        return true}
```

Vous voyez ? Les types optionnels de Kotlin sont simplement des monades **Maybe** !

![Image](https://cdn-media-1.freecodecamp.org/images/EMAzcG7SugWj0cXAYPibjcmvZJ1eUYFc9Unc)

Nous pouvons rendre ce code encore plus joli si nous nous débarrassons de la classe de données et utilisons simplement le type optionnel directement :

```
fun updateDbData(): Boolean {    readFromDb()?. let {        doSomethingWithData(it)?.let {            putModifiedDataInDb(it)?.let {                return true            }        }    }        return false}
```

Nous utilisons la syntaxe `?.let` de Kotlin qui n'exécute une lambda que si la variable à laquelle elle est appliquée n'est pas nulle.

Sympa, non ?

### Oui, mais qu'est-ce qu'une Monade ?

Les monades sont des constructeurs de calculs. Elles encapsulent des types, des moyens spécifiques de combiner ces types, et des opérations sur ces types.

Par exemple, dans notre fonction ci-dessus, le type optionnel de Kotlin peut être utilisé pour encapsuler un résultat d'opération. Lorsqu'il est combiné avec l'opérateur `?.let`, il ne permet l'exécution de la lambda que si le résultat de l'opération est non nul. Il nous permet d'exprimer les résultats des calculs et de les combiner de manière spécifique selon un ensemble de règles défini.

Les monades proviennent de la théorie des catégories, et pour comprendre véritablement leur signification mathématique, nous devrons étudier cette signification. La bonne nouvelle, cependant, est que nous n'avons pas besoin d'obtenir une maîtrise en mathématiques pour les utiliser. Une compréhension de base suffira pour nos besoins, et à mesure que nous approfondirons la programmation fonctionnelle, nous pourrons continuer à augmenter vos connaissances.

### La monade 'Either'

La monade _Maybe_ nous permet de modéliser la présence ou l'absence d'un résultat. Mais qu'en est-il d'un calcul qui peut avoir deux chemins de résultat valides ? Par exemple, nous pourrions vouloir retourner une valeur par défaut pour un calcul au lieu d'une valeur absente comme null.

C'est là qu'intervient la monade **Either**. Elle peut représenter une valeur `good` et une valeur `bad`. Habituellement, `left` est utilisé pour indiquer un échec et `right` est utilisé pour indiquer un succès.

Prenons un exemple. Supposons que nous avons une fonction `getUser`. Si aucun utilisateur n'est présent, elle nous donnera un utilisateur anonyme. Sinon, elle nous donnera l'utilisateur actuellement connecté.

Nous pouvons la modéliser comme un _Either_ comme ceci :

```
data class Either(val left: AnonUser?, val right: CurrentUser?)
```

et nous pouvons l'utiliser dans le code appelant comme ceci :

```
fun updateProfileData(): Boolean {    val either = getUser()        if(either.left) {        // ne peut pas mettre à jour le profil pour un utilisateur anonyme        return false    }    else {        updateProfile(either.right)        return true    }}
```

### Plus de ressources

Vous pouvez trouver de nombreuses explications sur les monades sur le web comme [celle-ci](http://blog.jorgenschaefer.de/2013/01/monads-for-normal-programmers.html). Si vous voulez approfondir et apprendre la programmation fonctionnelle ainsi que les monades, je recommande l'excellent livre gratuit [Learn You A Haskell For Great Good](http://learnyouahaskell.com/chapters).

Les implémentations de monades que j'ai décrites ici sont incomplètes et principalement destinées à comprendre les concepts. Vous pouvez trouver des implémentations plus robustes dans des projets comme [kotlin-monads](https://github.com/h0tk3y/kotlin-monads).

### Résumé

La programmation fonctionnelle encourage à traiter les erreurs comme faisant partie du calcul lui-même et non comme des aberrations du flux de contrôle régulier. Cela rend le flux de contrôle plus facile à comprendre, à gérer et à tester. Nous y parvenons facilement en représentant les résultats des calculs à l'aide des types optionnels de Kotlin ou de nos propres implémentations de monades personnalisées.

Dans la prochaine et dernière partie de cette série, nous examinerons la mise en œuvre d'une architecture fonctionnelle sur Android en reliant tous les concepts que nous avons appris jusqu'à présent.

_Si vous avez aimé cela, cliquez sur le ? ci-dessous. Je remarque chacun d'eux et je suis reconnaissant pour chacun d'eux._

_Pour plus de réflexions sur la programmation, suivez-moi afin d'être averti lorsque j'écrirai de nouveaux articles._