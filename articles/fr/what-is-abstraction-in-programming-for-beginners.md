---
title: Qu'est-ce que l'abstraction en programmation ? Explication pour les débutants
subtitle: ''
author: Ryan Michael Kay
co_authors: []
series: null
date: '2022-12-21T18:08:21.000Z'
originalURL: https://freecodecamp.org/news/what-is-abstraction-in-programming-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/smartphone-g7993a9917_1280-1.jpg
tags:
- name: abstraction
  slug: abstraction
- name: Kotlin
  slug: kotlin
seo_title: Qu'est-ce que l'abstraction en programmation ? Explication pour les débutants
seo_desc: 'This article will not be a dry and boring explanation of abstract classes,
  interfaces, protocols, or similar software entities.

  I will explain what they are in simple terms, but my main goal is to change how
  you think about abstractions in general. A...'
---

Cet article ne sera pas une explication sèche et ennuyeuse des classes abstraites, des interfaces, des protocoles ou d'entités logicielles similaires.

Je vais expliquer ce qu'ils sont en termes simples, mais mon objectif principal est de changer la façon dont vous pensez aux abstractions en général. Tout cela est au service de vous aider à développer l'art de la programmation.

Voici les sujets que je vais aborder :

* [Qu'est-ce qu'une abstraction ?](#heading-quest-ce-quune-abstraction)
    
* [Comment utiliser les abstractions dans vos programmes](#heading-comment-utiliser-les-abstractions-dans-vos-programmes)  
    – [Comment utiliser les interfaces et les protocoles](#heading-comment-utiliser-les-interfaces-et-les-protocoles)  
    – [Comment utiliser les types de fonctions et les expressions lambda](#heading-comment-utiliser-les-types-de-fonctions-et-les-expressions-lambda)
    
* [L'abstraction est-elle l'idée la plus importante en programmation ?](#heading-labstraction-est-elle-lidee-la-plus-importante-en-programmation)
    
* [De combien d'abstraction ai-je besoin ?](#heading-de-combien-dabstraction-ai-je-besoin)
    

Les exemples de code seront en Kotlin, mais j'ai écrit l'article en supposant que vous n'avez que des connaissances de base en programmation dans n'importe quel langage standard de l'industrie.

J'utilise également une variété d'approches pour couvrir à la fois les styles de code orientés objet et fonctionnels.

## Qu'est-ce qu'une abstraction ?

Pour commencer, nous allons discuter de ce que signifie ce terme dans le sens le plus général. Voici une définition simplifiée que j'ai élaborée pour une abstraction :

> « Une **représentation moins détaillée** d'un objet ou d'un concept dans la nature. »

Je sais que ma définition semble très vague, mais nous allons discuter quelques exemples clairs sous peu. D'abord, nous devons comprendre ce que signifie **détail**.

### Qu'est-ce que le détail ?

Le détail fait référence à la quantité, ou peut-être à la densité, d'informations. Voici deux exemples de modèles de données qui sont plus ou moins détaillés :

```pgsql
User {
  name,
  id
}
```

```pgsql
User {
  name: String,
  id: Integer,
  phone: Integer,
  email: String
}
```

Il n'est pas nécessaire de trop réfléchir à ce point ! Plus de détails est une autre façon de dire plus d'informations ou plus de complexité.

Le seul autre point clé est de comprendre ce qu'est une **représentation**.

### Comment représenter quelque chose

Supposons que vous allez voyager quelque part où il y a un type particulièrement mortel de serpent venimeux. Pour obtenir des informations sur ce serpent, vous avez quelques options différentes :

* Lire une description verbale du serpent et de son comportement
    
* Regarder un dessin ou une photo du serpent
    
* Écouter un audio de ce à quoi il ressemble lorsqu'il se comporte de manière agressive
    

Tous les points ci-dessus sont des exemples de différents types de représentations, ou d'abstractions, du serpent venimeux.

Dans chaque cas, certaines pièces d'information, qui représentent avec précision les propriétés du vrai serpent, sont transmises. Cependant, ni une description verbale, ni une image, ni un enregistrement ne peuvent vous mordre !

Ici, nous voyons l'utilité principale des abstractions : **Transmettre des informations importantes** (également connues sous le nom de détails ou propriétés) d'un objet ou d'un concept, **tout en omettant les informations inutiles**.

## Comment utiliser les abstractions dans vos programmes

Avant de discuter de certains détails, il est utile de mentionner que tout dans un programme informatique est techniquement une abstraction.

En fait, **les langages de programmation, ainsi que toutes les formes de mathématiques, sont des systèmes d'abstractions**.

Cependant, les programmeurs ont tendance à penser aux abstractions comme une bande étroite d'entités logicielles généralement appelées :

* Interfaces ou Protocoles
    
* Classes Abstraites
    
* Types/Références/Signatures de Fonctions
    
* Super/Parent-Classes
    

Malheureusement, les noms et les mécanismes des entités logicielles ci-dessus peuvent varier considérablement dans différents langages de programmation.

Pour cette raison, je vais prendre deux exemples qui peuvent être plus ou moins appropriés à vos langages préférés :

1. Une interface ou un protocole (qui couvrira également les classes abstraites)
    
2. Un type de fonction ou une référence de méthode
    

Dans tous les cas, ne vous inquiétez pas trop des noms ou des différences mineures dans le fonctionnement de ces choses à travers les langages. Au lieu de cela, je vous invite à vous concentrer sur les idées générales.

## Comment utiliser les interfaces et les protocoles

Je vais utiliser le terme interface à partir de maintenant, mais ce terme est synonyme de protocole. J'utiliserai également le terme fonction de manière synonyme avec méthode.

Les interfaces vous permettent de définir le comportement des fonctions, des classes ou des objets, sans définir leur implémentation.

Ne vous inquiétez pas, je ne suis pas comme certains enseignants qui lancent du jargon et prétendent vous enseigner quelque chose.

Regardons exactement ce que je veux dire par comportement et implémentation.

**Comportement** signifie littéralement une déclaration de fonction :

```kotlin
interface UserDataSource {
//cette ligne ci-dessous a une déclaration de fonction mais pas de "corps" de fonction
  fun getUserById(id: String): User?
}

data class User(
  val id: String,
  val someData: Any
)
```

Vous pouvez voir les notes de bas de page ci-dessous concernant mon utilisation du terme « déclaration de fonction ».

Pour traduire cela en anglais, cette déclaration de fonction dit que nous définissons une fonction qui :

* Est nommée « getUserById »
    
* Accepte un type String appelé « id » comme argument lorsqu'elle est appelée
    
* Retourne un « User » ou une valeur nulle si aucun utilisateur n'existe (c'est parce que nous avons un « ? » après le type « User »)
    

**Implémentation** fait référence au corps de la fonction :

```kotlin
//Notez que ":" est une abréviation pour extends/implements en Kotlin pour la déclaration de classe
//
class UserDatabase(): UserDataSource {
//les accolades, et tout ce qui se trouve entre elles, est l'implémentation
  override fun getUserById(id: String): User? {
    var user: User? = null
    //... pas important pour cet exemple
    return user
  }
}
```

Un autre nom pour la fonction à l'intérieur de l'interface est une *fonction abstraite*. Espérons que notre discussion sur le sens abstrait de « *moins de détails* » commence à avoir plus de sens ici !

**Quelques notes pour la précision :**

1. Certains langages ont des fonctionnalités pour définir des propriétés, des variables, et même des implémentations (c'est-à-dire des déclarations de fonctions + corps de fonctions) au sein des interfaces. Cela ne change pas le but principal des interfaces, cependant.
    
2. Le terme déclaration de fonction sera défini différemment selon le langage. Au lieu de vous inquiéter des définitions verbales, veuillez considérer mes exemples de code pour suivre ce que je veux dire.
    

### Qu'en est-il des classes abstraites ?

À part en Python (et peut-être dans d'autres langages dont je ne suis pas au courant), les classes abstraites sont très similaires aux interfaces sauf pour une différence clé : une **classe ne peut hériter que d'une seule classe abstraite.**

À mon avis, avant que les langages ne commencent à inclure des moyens pour que les interfaces définissent leurs propres implémentations, l'utilisation des classes abstraites par rapport aux interfaces était claire :

* Si vous voulez seulement partager un comportement à travers un ensemble d'entités logicielles, utilisez une interface
    
* Si vous voulez partager une implémentation **et** un comportement, utilisez une classe abstraite à la place
    

Malheureusement, cette distinction est très floue depuis que de nombreux langages ont des fonctionnalités pour ajouter une implémentation aux interfaces (comme les méthodes par défaut de Java).

La seule recommandation générale que je peux faire, qui ne tient pas compte des détails spécifiques d'un langage de programmation particulier, est la suivante : utilisez la structure la plus simple pour accomplir le travail.

## Comment utiliser les types de fonctions et les expressions lambda

Il existe différentes façons d'atteindre l'abstraction sans définir d'interfaces ou de classes. Mais la quantité de structure que ces fonctionnalités de langage nécessitent est encore soumise aux spécificités du langage.

Kotlin fournit suffisamment de ces fonctionnalités pour que vous puissiez, espérons-le, établir quelques connexions avec vos langages préférés.

### Comment utiliser les types de fonctions au lieu d'une interface

Nous allons commencer par un exemple pratique puis expliquer les détails plus fins partie par partie.

Supposons que nous voulons mettre en place une fonction abstraite (rappelons que cela signifie une fonction sans implémentation) pour gérer un événement de clic.

En utilisant quelque chose comme une interface, nous pourrions faire ce qui suit :

```kotlin
//supposons que ceci est un composant de plateforme/OS qui vous indique quand
//un utilisateur clique sur quelque chose à l'écran
class PlatformComponent(
  var clickListener: ClickListener? = null
) {
  fun userClickedScreen() {
    //Note : le "?" signifie que handleClick() est seulement
    //appelé lorsque clickListener n'est PAS NULL
    clickListener?.handleClick()
  }
}
//Cette interface cache (abstrait) la classe/type concrète
//qui gère le clic
interface ClickListener {
  fun handleClick()
}
//Cette classe/type concrète gère le clic
//en étendant l'interface
class ScreenController() : ClickListener {
  override fun handleClick() {
    println("Click handled.")
  }
}

fun main() {
  PlatformComponent(
    ScreenController()
  ).userClickedScreen()
}
```

Une approche alternative est d'utiliser un type de fonction au lieu d'une interface :

```kotlin
fun main() {
  val controller = ScreenController()
  val component = PlatformComponent(
    //Le double deux-points indique au compilateur que nous faisons référence
    //à la fonction handleClick définie dans ScreenController
    controller::handleClick
  )
  component.userClickedScreen()
}

//supposons que ceci est un composant de plateforme/OS qui vous indique quand
//un utilisateur clique sur quelque chose à l'écran
class PlatformComponent(
  var clickListener: () -> Unit
) {
  fun userClickedScreen() {
    //Ceci est équivalent à appeler ScreenController.handleClick(),
    //mais PlatformComponent ne le sait pas. Abstraction !
    clickListener()
  }
}
//Cette classe/type concrète gère le clic
class ScreenController() {
  fun handleClick() {
    println("Click handled.")
  }
}
```

Dans cet exemple, nous pouvons voir comment il y a encore moins de structure requise pour obtenir le même résultat. Mais gardez à l'esprit que le fait d'avoir moins de structure n'implique pas immédiatement un meilleur code. Vraiment, **cela dépend**.

Dans tous les cas, avec un exemple pratique en tête, nous pouvons décomposer comment ce code fonctionne réellement en plus de détails.

### Comment utiliser les références de fonctions

Si vous n'êtes pas familier avec le fonctionnement des types de fonctions, des références de méthodes (ou quoi que ce soit d'autre qu'elles soient appelées), cette section les explique en Kotlin. N'hésitez pas à sauter à la section suivante si vous êtes déjà familier.

Similaire à la plupart des langages de programmation modernes, nous pouvons créer une variable de référence à une fonction particulière en Kotlin :

```kotlin
var clickListener: () -> Unit
```

En Kotlin, les types de fonctions ont la syntaxe suivante :

```kotlin
(optional list of parameter types) -> return type
```

Par exemple :

* `(Int, Int) -> Int` signifie que la fonction associée doit prendre deux paramètres Int et retourner un seul Int
    
* `() -> Unit` signifie qu'une fonction n'a pas de paramètres et s'exécute sans retourner une valeur significative
    

Unit est à peu près équivalent au type de retour void de Java ou au type None de Python – au moins en principe.

Lorsque vient le temps d'appeler (invoquer) une référence de fonction, nous avons deux options :

* `clickListener()` pour faire court
    
* `clickListener.invoke()` est la syntaxe complète, qui est nécessaire lors de l'appel sécurisé comme `clickListener?.invoke()`, par exemple
    

### Comment utiliser les expressions lambda

Dans l'exemple précédent, il est important de noter que ScreenController ne se soucie pas du nom de la fonction qu'il invoque.

Nous pouvons prendre ce niveau d'abstraction encore plus loin, en ne définissant même pas un ScreenController :

```kotlin
fun main() {
  //notez que les parenthèses extérieures sont optionnelles en Kotlin,
  //mais peuvent rendre cela plus facile à comprendre
  val component = PlatformComponent(
    { println("Click handled.") }
  )
  component.userClickedScreen()
}
//supposons que ceci est un composant de plateforme/OS qui vous indique quand
//un utilisateur clique sur quelque chose à l'écran
class PlatformComponent(
  var clickListener: () -> Unit
) {
  fun userClickedScreen() {
    clickListener()
  }
}
```

Contrairement aux exemples précédents, celui-ci **n'est pas destiné à ressembler à un scénario pratique** – juste pour démontrer une expression lambda.

L'expression lambda réelle est celle-ci :

`{ println("Click handled.") }`

Comme vous pouvez le voir, cela ne devient pas beaucoup plus abstrait qu'une expression lambda.

En surface, c'est presque comme définir seulement l'implémentation mais pas le comportement. Mais au moins en Kotlin, l'expression lambda doit se conformer au type que nous lui attribuons.

Dans ce cas, `{ println("Click handled.") }` n'a pas de paramètres et ne retourne pas de valeur significative. Donc, elle se conforme à `() -> Unit`.

### Quelle approche devrais-je utiliser ?

Vous vous demandez peut-être quelle approche vous devriez utiliser – en supposant que votre langage permet plusieurs approches.

La réponse la plus précise que je puisse vous donner est qu'il n'y a pas de règle générale.

Beaucoup d'enseignants de nos jours diront « *x* est pire que y » ou simplement « *x* est mauvais », parce que cela fonctionne bien pour le clickbait et l'optimisation des moteurs de recherche.

Mais un langage, une plateforme, une construction de code, une architecture, et presque tout le reste ne peut être jugé bon, mauvais, meilleur ou pire que par rapport à vos exigences.

En fait, différentes exigences sont la raison pour laquelle nous avons des langages aussi différents que Python et Java qui sont tous deux extrêmement populaires.

Alors, au lieu de cela, essayez différentes approches et soyez sceptique envers quiconque fait des déclarations absolues sans discuter des exigences.

## L'abstraction est-elle l'idée la plus importante en programmation ?

Le but de cet article n'a jamais été de dire : « *Utiliser des interfaces et des classes abstraites partout vous rendra un meilleur programmeur.* »

Pour être honnête, comme beaucoup de développeurs, j'ai traversé une phase autour de 2016-2018 où je pensais en fait que cette déclaration était assez précise.

Au lieu de cela, le but de cet article est d'expliquer deux choses :

* L'abstraction en programmation, à mon avis, **ne devrait pas spécifiquement signifier des classes abstraites, ou une construction de code particulière**
    
* L'abstraction en programmation est un **processus** par lequel nous concevons nos entités logicielles selon **la quantité de détails** qu'elles contiennent intérieurement (privément) et fournissent extérieurement (publiquement)
    

En un sens, chaque décision que nous prenons sur la structure de notre code, quel que soit le langage, se résume à ce processus d'abstraction.

Cela dit, comment savons-nous quand rendre un aspect de notre programme plus abstrait est bénéfique, inutile ou préjudiciable ?

## De combien d'abstraction ai-je besoin ?

Je ne peux penser qu'à un type de situation où vous devriez sérieusement envisager d'utiliser quelque chose comme une interface ou un type de fonction.

Rappelez-vous que ces entités logicielles fournissent une variabilité d'implémentation mais un comportement cohérent. De plus, cette implémentation fait généralement référence au corps d'une fonction.

Deux choses découlent de cette observation :

* Si aucune variabilité d'implémentation n'est requise, il est peu probable qu'il y ait un avantage à utiliser une entité logicielle plus abstraite.
    
* Si une variabilité d'implémentation est requise, l'utilisation d'une entité logicielle plus abstraite est probablement bénéfique.
    

Nous allons maintenant discuter de deux situations que j'ai rencontrées où la variabilité est une exigence.

### Comment rendre votre code plus facile à tester

Supposons que nous avons une sorte d'entité logicielle, qui doit demander des données utilisateur à une base de données ou à un adaptateur réseau :

```kotlin
class PresentationLogic(
 val datasource: Datasource
) {
    fun start() {
        val someData = datasource.getData()
        presentData(someData)
    }
    
    //...
}

class Datasource() {
    fun getData(): Data {
        var someData = getLocalOrRemoteData()
        //... gestion des erreurs et ainsi de suite
        
        return someData
    }
}
```

Supposons également que nous voulons tester `PresentationLogic` sans avoir besoin d'une vraie source de données pour fournir les données.

Il existe plusieurs façons de résoudre ce problème (voir la note ci-dessous), mais une solution simple consiste à rendre la source de données plus abstraite :

```kotlin
class PresentationLogic(
 val datasource: DatasourceInterface
) {
    fun start() {
        val someData = datasource.getData()
        presentData(someData)
    }
    
    //...
}

interface DatasourceInterface {
    fun getData(): Data
}
```

À partir de là, nous pouvons créer une fausse implémentation de la source de données dans un environnement de test :

```kotlin
class FakeDatasource(): DatasourceInterface {
        override fun getData(): Data {
            return Data()
        }
}

@Test
fun testLogic() {
    val logic = PresentationLogic(
       //ici nous fournissons la version factice
       FakeDatasource()
    )
}
```

En utilisant l'abstraction, PresentationLogic ne sait pas et ne se soucie pas de savoir s'il communique avec une fausse ou une vraie source de données. Par extension, il n'a pas besoin de changer pour fonctionner avec l'une ou l'autre. Variabilité de l'implémentation !

Notez qu'il existe d'autres moyens d'atteindre cette variabilité en dehors de l'utilisation d'une interface. Vous pourriez utiliser une bibliothèque de mocking, ou configurer un outil de construction pour échanger les implémentations.

Il n'y a pas de réponse claire à quelle approche est meilleure en dehors de la discussion des exigences spécifiques.

De plus, notez que cette approche ne fonctionnerait pas réellement à moins que les détails de la création de la source de données soient gardés séparés de `PresentationLogic`.

Ceci est communément appelé Injection de Dépendance, que je discuterai dans un article séparé.

### Comment travailler avec différentes versions et fournisseurs d'un service

Supposons que pour une raison quelconque, vous devez travailler avec différentes versions ou fournisseurs du même service en fonction de différentes exigences.

Un exemple pourrait être la prise en charge d'AWS et de Firebase pour stocker les mêmes données. Un autre exemple pourrait être la prise en charge d'une version héritée d'un service ainsi que d'une version plus récente de ce même service.

Dans tous les cas, c'est une autre situation où une variabilité d'implémentation est attendue.

Les exemples de code que nous allons discuter ont les exigences suivantes :

* Un programme client doit utiliser trois services, tous de différents fournisseurs, pour effectuer le même comportement
    
* La décision de choisir un service particulier est déterminée à l'exécution en fonction de l'environnement (plateforme, OS, matériel, etc.) du programme client
    

Pour ceux qui se demandent, « client » dans ce contexte est un mot générique pour un programme ou une entité logicielle qui utilise d'autres programmes ou entités logicielles.

Par exemple, le site web et les applications mobiles de YouTube sont des « applications clientes » des serveurs backend de YouTube.

Sans appliquer d'abstraction, notre programme client devra connaître tous les services possibles et se voir dire quel service choisir :

```kotlin
fun clientProgram(
    request: Request, 
    awsService: AwsService,
    firebaseService: FirebaseService,
    parseService: ParseService
): Result {
    val use: USE_SERVICE = determineBestService()
    
    val result = when (use) {
        USE_SERVICE.AWS -> awsService.executeRequest(request)
        USE_SERVICE.FIREBASE -> firebaseService.executeRequest(request)
        USE_SERVICE.PARSE -> parseService.executeRequest(request)
    }
    
    //supposons que des travaux supplémentaires sont effectués avant de retourner le résultat
    return result
}

enum class USE_SERVICE {
    AWS,
    FIREBASE,
    PARSE
}
```

Remarquez que clientProgram a un paramètre qui fait référence à des fournisseurs spécifiques du service :

* Amazon Web Services (AWS)
    
* Firebase
    
* Le service Parse désormais obsolète de Facebook
    

Il s'ensuit que tout changement apporté à nos services nécessitera que `clientProgram` soit refactorisé (réécrit) de manière appropriée.

La raison pour laquelle j'ai choisi Parse comme l'un des services d'exemple est spécifiquement parce qu'il a été fermé, malgré son utilisation généralisée. Il existe diverses raisons pour lesquelles un service particulier peut ne plus répondre aux exigences, mais le fait de ne plus fonctionner en est une bonne.

Une approche alternative consisterait à masquer tous les détails concernant le service utilisé de clientProgram. Vous pourriez utiliser une interface, mais pour varier les plaisirs, j'ai utilisé un type de fonction à la place :

```kotlin
fun main() {
    //Création des services
    val awsService = AwsService()
    val firebaseService = FirebaseService()
    
    //déterminer quel service utiliser ne doit pas
    //être inclus dans clientProgram
    val use: USE_SERVICE = determineBestService()

    //Assigner serviceToUse à la fonction appropriée
    val serviceToUse: (Request) -> Result = when (use) {
        USE_SERVICE.AWS -> awsService::executeRequest
        USE_SERVICE.FIREBASE -> firebaseService::executeRequest
    }
    
    val request = getRequest()
    
    clientProgram(
       request,
       serviceToUse
    )
}


fun clientProgram(
    request: Request, 
    service: (Request) -> Result
): Result {
    
    val result = service.invoke(request)
    
    //supposons que des travaux supplémentaires sont effectués avant de retourner le résultat
    
    return result
}

enum class USE_SERVICE {
    AWS,
    FIREBASE
}

class AwsService() {
    fun executeRequest(request: Request): Result = Result()
}
class FirebaseService() {
    fun executeRequest(request: Request): Result = Result()
}
```

Le résultat final de cette abstraction est que nous pouvons changer de services sans avoir besoin de changer `clientProgram` – en supposant que notre comportement ne change pas.

Je veux souligner que je ne préconise pas de masquer chaque service derrière une sorte d'abstraction. Si aucune variabilité n'est requise ou attendue, il peut ne pas y avoir d'avantage à une abstraction supplémentaire.

# Réflexions finales

J'espère qu'il est clair en lisant cet article que mon intention n'est pas de pousser des opinions dogmatiques sur le degré d'abstraction que votre code devrait avoir.

En tant que développeur junior et intermédiaire, il m'a fallu quelques années pour réaliser que cela dépend vraiment des exigences du projet.

J'espère également que cet article vous a donné de nouvelles idées et perspectives sur ce qu'est l'abstraction et comment elle peut être appliquée dans votre code. Bonne chance et bon codage !

### **Avant de partir...**

Si vous avez aimé cet article et souhaitez plus d'informations sur ces principes et constructions de code, consultez mon cours gratuit et complet sur les [fondamentaux de la programmation](https://youtu.be/FL2SMZxNQlc). Il inclut des sous-titres professionnels en anglais, birman et arabe.