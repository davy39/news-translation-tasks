---
title: Comment comprendre les variances de Scala en construisant des restaurants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-24T16:34:04.000Z'
originalURL: https://freecodecamp.org/news/understand-scala-variances-building-restaurants
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca13e740569d1a4ca4d7c.jpg
tags:
- name: covariant
  slug: covariant
- name: contravariant
  slug: contravariant
- name: invariant
  slug: invariant
- name: General Programming
  slug: programming
- name: Scala
  slug: scala
- name: '#variance'
  slug: variance
seo_title: Comment comprendre les variances de Scala en construisant des restaurants
seo_desc: "By Luca Florio\nI understand that type variance is not fundamental to writing\
  \ Scala code. It's been more or less a year since I've been using Scala for my day-to-day\
  \ job, and honestly, I've never had to worry much about it. \nHowever, I think it\
  \ is an ..."
---

Par Luca Florio

Je comprends que la variance de type n'est pas fondamentale pour écrire du code Scala. Cela fait plus ou moins un an que j'utilise Scala pour mon travail quotidien, et honnêtement, je n'ai jamais eu à m'en soucier beaucoup. 

Cependant, je pense que c'est un sujet "avancé" intéressant, alors j'ai commencé à l'étudier. Ce n'est pas facile à saisir immédiatement, mais avec le bon exemple, cela pourrait être un peu plus facile à comprendre. Essayons d'utiliser une analogie basée sur la nourriture...

## Qu'est-ce que la variance de type ?
Tout d'abord, nous devons définir ce qu'est la variance de type. Lorsque vous développez dans un langage orienté objet, vous pouvez définir des types complexes. Cela signifie qu'un type peut être paramétré en utilisant un autre type (type composant). 

Pensez à `List` par exemple. Vous ne pouvez pas définir une `List` sans spécifier quels types seront à l'intérieur de la liste. Vous le faites en mettant le type contenu dans la liste entre crochets : `List[String]`. Lorsque vous définissez un type complexe, vous pouvez spécifier comment il va varier sa relation de sous-type selon la relation entre le type composant et ses sous-types. 

D'accord, cela semble un peu confus... Soyons un peu plus pratiques. 

## Construire un empire de restaurants
Notre objectif est de construire un empire de restaurants. Nous voulons des restaurants génériques et spécialisés. Chaque restaurant que nous allons ouvrir a besoin d'un menu composé de différentes recettes, et d'un chef (éventuellement étoilé). 

Les recettes peuvent être composées de différents types de nourriture (poisson, viande, viande blanche, légumes, etc.), tandis que le chef que nous engageons doit être capable de cuisiner ce type de nourriture. C'est notre modèle. Maintenant, c'est l'heure de coder !

## Différents types de nourriture
Pour notre exemple basé sur la nourriture, nous commençons par définir le `Trait Food`, fournissant simplement le nom de la nourriture. 

```scala
trait Food {

  def name: String

}
```

Ensuite, nous pouvons créer `Meat` et `Vegetable`, qui sont des sous-classes de `Food`. 

```scala
class Meat(val name: String) extends Food
```
```scala
class Vegetable(val name: String) extends Food
```

Enfin, nous définissons une classe `WhiteMeat` qui est une sous-classe de `Meat`. 

```scala
class WhiteMeat(override val name: String) extends Meat(name)
```

Cela semble raisonnable, n'est-ce pas ? Nous avons donc cette hiérarchie de types.

![food subtype relationship](https://www.freecodecamp.org/news/content/images/2019/07/food_type_rel.png)

Nous pouvons créer quelques instances de nourriture de divers types. Elles seront les ingrédients des recettes que nous allons servir dans nos restaurants.

```scala
// Food <- Meat
val beef = new Meat("beef")

// Food <- Meat <- WhiteMeat
val chicken = new WhiteMeat("chicken")
val turkey = new WhiteMeat("turkey")

// Food <- Vegetable
val carrot = new Vegetable("carrot")
val pumpkin = new Vegetable("pumpkin")
```

## Recipe, un type covariant
Définissons le type covariant `Recipe`. Il prend un type composant qui exprime la base alimentaire pour la recette - c'est-à-dire une recette basée sur la viande, les légumes, etc.

```scala
trait Recipe[+A] {

  def name: String

  def ingredients: List[A]

}
```

La `Recipe` a un nom et une liste d'ingrédients. La liste des ingrédients a le même type que `Recipe`. Pour exprimer que la `Recipe` est covariante dans son type `A`, nous l'écrivons comme `Recipe[+A]`. La recette générique est basée sur tous les types de nourriture, la recette de viande est basée sur la viande, et une recette de viande blanche n'a que de la viande blanche dans sa liste d'ingrédients.

```scala
case class GenericRecipe(ingredients: List[Food]) extends Recipe[Food] {

  def name: String = s"Generic recipe based on ${ingredients.map(_.name)}"

}
```
```scala
case class MeatRecipe(ingredients: List[Meat]) extends Recipe[Meat] {

  def name: String = s"Meat recipe based on ${ingredients.map(_.name)}"

}
```
```scala
case class WhiteMeatRecipe(ingredients: List[WhiteMeat]) extends Recipe[WhiteMeat] {

  def name: String = s"Meat recipe based on ${ingredients.map(_.name)}"

}
```

Un type est covariant s'il suit la même relation de sous-types que son type composant. Cela signifie que `Recipe` suit la même relation de sous-type que son composant Food.

![recipe subtype relationship](https://www.freecodecamp.org/news/content/images/2019/07/recipe_type_rel-1.png)

Définissons quelques recettes qui feront partie de différents menus.

```scala
// Recipe[Food]: Basé sur Meat ou Vegetable
val mixRecipe = new GenericRecipe(List(chicken, carrot, beef, pumpkin))
// Recipe[Food] <- Recipe[Meat]: Basé sur n'importe quel type de Meat
val meatRecipe = new MeatRecipe(List(beef, turkey))
// Recipe[Food] <- Recipe[Meat] <- Recipe[WhiteMeat]: Basé uniquement sur WhiteMeat
val whiteMeatRecipe = new WhiteMeatRecipe(List(chicken, turkey))
```

## Chef, un type contravariant
Nous avons défini quelques recettes, mais nous avons besoin d'un chef pour les cuisiner. Cela nous donne l'occasion de parler de contravariance. Un type est contravariant s'il suit une relation inverse des sous-types de son type composant. Définissons notre type complexe `Chef`, qui est contravariant dans le type composant. Le type composant sera la nourriture que le chef peut cuisiner. 

```scala
trait Chef[-A] {
  
  def specialization: String

  def cook(recipe: Recipe[A]): String
}
```

Un `Chef` a une spécialisation et une méthode pour cuisiner une recette basée sur une nourriture spécifique. Nous exprimons qu'il est contravariant en l'écrivant comme `Chef[-A]`. Maintenant, nous pouvons créer un chef capable de cuisiner de la nourriture générique, un chef capable de cuisiner de la viande et un chef spécialisé dans la viande blanche.

```scala
class GenericChef extends Chef[Food] {

  val specialization = "All food"

  override def cook(recipe: Recipe[Food]): String = s"I made a ${recipe.name}"
}
```
```scala
class MeatChef extends Chef[Meat] {

  val specialization = "Meat"

  override def cook(recipe: Recipe[Meat]): String = s"I made a ${recipe.name}"
}
```
```scala
class WhiteMeatChef extends Chef[WhiteMeat] {

  override val specialization = "White meat"

  def cook(recipe: Recipe[WhiteMeat]): String = s"I made a ${recipe.name}"
}
```

Puisque `Chef` est contravariant, `Chef[Food]` est une sous-classe de `Chef[Meat]` qui est une sous-classe de `Chef[WhiteMeat]`. Cela signifie que la relation entre les sous-types est l'inverse de son type composant Food.

![chef subtype relationship](https://www.freecodecamp.org/news/content/images/2019/07/chef_type_rel-1.png)

D'accord, nous pouvons maintenant définir différents chefs avec diverses spécialisations à engager dans nos restaurants.

```scala
// Chef[WhiteMeat]: Peut cuisiner seulement WhiteMeat
val giuseppe = new WhiteMeatChef
giuseppe.cook(whiteMeatRecipe)

// Chef[WhiteMeat] <- Chef[Meat]: Peut cuisiner seulement Meat
val alfredo = new MeatChef
alfredo.cook(meatRecipe)
alfredo.cook(whiteMeatRecipe)

// Chef[WhiteMeat]<- Chef[Meat] <- Chef[Food]: Peut cuisiner n'importe quel Food
val mario = new GenericChef
mario.cook(mixRecipe)
mario.cook(meatRecipe)
mario.cook(whiteMeatRecipe)
```

## Restaurant, où tout se réunit
Nous avons des recettes, nous avons des chefs, maintenant nous avons besoin d'un restaurant où le chef peut cuisiner un menu de recettes.

```scala
trait Restaurant[A] {

  def menu: List[Recipe[A]]
  def chef: Chef[A]

  def cookMenu: List[String] = menu.map(chef.cook)
}
```

Nous ne sommes pas intéressés par la relation de sous-type entre les restaurants, donc nous pouvons le définir comme invariant. Un type invariant ne suit pas la relation entre les sous-types du type composant. En d'autres termes, `Restaurant[Food]` n'est pas une sous-classe ou une superclasse de `Restaurant[Meat]`. Ils sont simplement sans relation.
Nous aurons un `GenericRestaurant`, où vous pouvez manger différents types de nourriture. Le `MeatRestaurant` est spécialisé dans les plats à base de viande et le `WhiteMeatRestaurant` est spécialisé uniquement dans les plats à base de viande blanche. Chaque restaurant pour être instancié a besoin d'un menu, qui est une liste de recettes, et d'un chef capable de cuisiner les recettes du menu. C'est là que la relation de sous-type de `Recipe` et `Chef` entre en jeu.

```scala
case class GenericRestaurant(menu: List[Recipe[Food]], chef: Chef[Food]) extends Restaurant[Food]
```
```scala
case class MeatRestaurant(menu: List[Recipe[Meat]], chef: Chef[Meat]) extends Restaurant[Meat]
```
```scala
case class WhiteMeatRestaurant(menu: List[Recipe[WhiteMeat]], chef: Chef[WhiteMeat]) extends Restaurant[WhiteMeat]
```

Commençons par définir quelques restaurants génériques. Dans un restaurant générique, le menu est composé de recettes de divers types de nourriture. Puisque `Recipe` est covariant, un `GenericRecipe` est une superclasse de `MeatRecipe` et `WhiteMeatRecipe`, donc je peux les passer à mon instance de `GenericRestaurant`. La chose est différente pour le chef. Si le Restaurant nécessite un chef capable de cuisiner de la nourriture générique, je ne peux pas y mettre un chef capable de cuisiner seulement un type spécifique. La classe `Chef` est covariante, donc `GenericChef` est une sous-classe de `MeatChef` qui est une sous-classe de `WhiteMeatChef`. Cela implique que je ne peux pas passer à mon instance autre chose que `GenericChef`.

```scala
val allFood = new GenericRestaurant(List(mixRecipe), mario)
val foodParadise = new GenericRestaurant(List(meatRecipe), mario)
val superFood = new GenericRestaurant(List(whiteMeatRecipe), mario)
```

Il en va de même pour `MeatRestaurant` et `WhiteMeatRestaurant`. Je ne peux passer à l'instance qu'un menu composé de recettes plus spécifiques que celle requise, mais des chefs capables de cuisiner des aliments plus génériques que celle requise.

```scala
val meat4All = new MeatRestaurant(List(meatRecipe), alfredo)
val meetMyMeat = new MeatRestaurant(List(whiteMeatRecipe), mario)
```
```scala
val notOnlyChicken = new WhiteMeatRestaurant(List(whiteMeatRecipe), giuseppe)
val whiteIsGood = new WhiteMeatRestaurant(List(whiteMeatRecipe), alfredo)
val wingsLovers = new WhiteMeatRestaurant(List(whiteMeatRecipe), mario)
```

C'est tout, notre empire de restaurants est prêt à faire des tonnes d'argent !

## Conclusion
D'accord les gars, dans cette histoire, j'ai fait de mon mieux pour expliquer les variances de type en Scala. C'est un sujet avancé, mais cela vaut la peine de le connaître par simple curiosité. J'espère que l'exemple du restaurant peut aider à le rendre plus compréhensible. Si quelque chose n'est pas clair, ou si j'ai écrit quelque chose de faux (je suis encore en train d'apprendre !) n'hésitez pas à laisser un commentaire !

À bientôt ! 👋