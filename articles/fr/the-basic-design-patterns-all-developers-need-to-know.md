---
title: Les 3 types de motifs de conception que tous les développeurs devraient connaître
  (avec des exemples de code pour chacun)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-24T06:52:52.000Z'
originalURL: https://freecodecamp.org/news/the-basic-design-patterns-all-developers-need-to-know
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/design-patterns-everywhere.jpg
tags:
- name: command
  slug: command
- name: decorator
  slug: decorator
- name: design patterns
  slug: design-patterns
- name: Java
  slug: java
- name: object oriented
  slug: object-oriented
- name: singleton
  slug: singleton
seo_title: Les 3 types de motifs de conception que tous les développeurs devraient
  connaître (avec des exemples de code pour chacun)
seo_desc: 'By Sameeha Rahman

  What is a Design Pattern?

  Design patterns are design level solutions for recurring problems that we software
  engineers come across often. It’s not code - I repeat, ❌CODE. It is like a description
  on how to tackle these problems and ...'
---

Par Sameeha Rahman

# Qu'est-ce qu'un motif de conception ?

Les motifs de conception sont des solutions de niveau conception pour des problèmes récurrents que nous, ingénieurs logiciels, rencontrons souvent. Ce n'est pas du code - je répète, ❌ **CODE**. C'est comme une description de la manière de résoudre ces problèmes et de concevoir une solution. 

L'utilisation de ces motifs est considérée comme une bonne pratique, car la conception de la solution est assez éprouvée et testée, ce qui entraîne une meilleure lisibilité du code final. Les motifs de conception sont souvent créés pour et utilisés par les langages OOP, comme Java, dans lequel la plupart des exemples à partir de maintenant seront écrits.

## Types de motifs de conception

Il existe environ 26 motifs actuellement découverts (je pense à peine que je les ferai tous...).

Ces 26 peuvent être classés en 3 types :

1. Créationnels : Ces motifs sont conçus pour l'instanciation de classes. Ils peuvent être soit des motifs de création de classes, soit des motifs de création d'objets.

2. Structurels : Ces motifs sont conçus en ce qui concerne la structure et la composition d'une classe. L'objectif principal de la plupart de ces motifs est d'augmenter la fonctionnalité de la ou des classes impliquées, sans changer beaucoup de sa composition.

3. Comportementaux : Ces motifs sont conçus en fonction de la manière dont une classe communique avec les autres.

Dans cet article, nous allons passer en revue un motif de conception de base pour chaque type classé.

## Type 1 : Créationnel - Le motif de conception Singleton

Le motif de conception Singleton est un motif créationnel, dont l'objectif est de créer une seule instance d'une classe et de fournir un seul point d'accès global à cet objet. Un exemple couramment utilisé d'une telle classe en Java est Calendar, où vous ne pouvez pas créer une instance de cette classe. Il utilise également sa propre méthode `getInstance()` pour obtenir l'objet à utiliser.

Une classe utilisant le motif de conception singleton comprendra :

![Image](https://www.freecodecamp.org/news/content/images/2019/07/singleton-class-diagram.png)
_Diagramme de classe Singleton_

1. Une variable statique privée, contenant la seule instance de la classe.
2. Un constructeur privé, afin qu'il ne puisse pas être instancié ailleurs.
3. Une méthode statique publique, pour retourner l'instance unique de la classe.

Il existe de nombreuses implémentations différentes du singleton design. Aujourd'hui, je vais passer en revue les implémentations de :

1. Instanciation Eager

2. Instanciation Lazy

3. Instanciation Thread-safe

### Eager Beaver

```java
public class EagerSingleton {
	// créer une instance de la classe.
	private static EagerSingleton instance = new EagerSingleton();

	// constructeur privé, afin qu'il ne puisse pas être instancié en dehors de cette classe.
	private EagerSingleton() {  }

	// obtenir la seule instance de l'objet créé.
	public static EagerSingleton getInstance() {
		return instance;
	}
}
```

Ce type d'instanciation se produit pendant le chargement de la classe, car l'instanciation de la variable instance se produit en dehors de toute méthode. Cela pose un inconvénient majeur si cette classe n'est pas du tout utilisée par l'application cliente. Le plan de contingence, si cette classe n'est pas utilisée, est l'instanciation Lazy.

### Lazy Days

Il n'y a pas beaucoup de différence avec l'implémentation ci-dessus. Les principales différences sont que la variable statique est initialement déclarée nulle, et n'est instanciée qu'à l'intérieur de la méthode `getInstance()` si - et seulement si - la variable d'instance reste nulle au moment de la vérification. 

```java
public class LazySingleton {
	// initialiser l'instance à null.
	private static LazySingleton instance = null;

	// constructeur privé, afin qu'il ne puisse pas être instancié en dehors de cette classe.
	private LazySingleton() {  }

	// vérifier si l'instance est null, et si oui, créer l'objet.
	public static LazySingleton getInstance() {
		if (instance == null) {
			instance = new LazySingleton();
		}
		return instance;
	}
}
```

Cela résout un problème, mais un autre existe toujours. Que se passe-t-il si deux clients différents accèdent à la classe Singleton en même temps, à la milliseconde près ? Eh bien, ils vérifieront si l'instance est nulle en même temps, et la trouveront vraie, et créeront donc deux instances de la classe pour chaque demande des deux clients. Pour résoudre ce problème, l'instanciation Thread Safe doit être implémentée.

### (Thread) Safety is Key

En Java, le mot-clé synchronized est utilisé sur les méthodes ou les objets pour implémenter la sécurité des threads, de sorte qu'un seul thread accédera à une ressource particulière à la fois. L'instanciation de la classe est placée dans un bloc synchronisé afin que la méthode ne puisse être accessible que par un seul client à un moment donné.

```java
public class ThreadSafeSingleton {
	// initialiser l'instance à null.
	private static ThreadSafeSingleton instance = null;

	// constructeur privé, afin qu'il ne puisse pas être instancié en dehors de cette classe.
	private ThreadSafeSingleton() {  }

	// vérifier si l'instance est null, dans un bloc synchronisé. Si oui, créer l'objet
	public static ThreadSafeSingleton getInstance() {
		synchronized (ThreadSafeSingleton.class) {
			if (instance == null) {
				instance = new ThreadSafeSingleton();
			}
		}
		return instance;
	}
}
```

Le surcoût pour la méthode synchronisée est élevé et réduit les performances de l'ensemble de l'opération. 

Par exemple, si la variable d'instance a déjà été instanciée, alors chaque fois qu'un client accède à la méthode `getInstance()`, la méthode `synchronized` est exécutée et les performances chutent. Cela se produit simplement pour vérifier si la valeur de la variable `instance` est nulle. Si elle trouve que c'est le cas, elle quitte la méthode. 

Pour réduire ce surcoût, un double verrouillage est utilisé. La vérification est utilisée avant la méthode `synchronized` également, et si la valeur est nulle seule, la méthode `synchronized` est exécutée.

```java
// double locking est utilisé pour réduire le surcoût de la méthode synchronisée
public static ThreadSafeSingleton getInstanceDoubleLocking() {
	if (instance == null) {
		synchronized (ThreadSafeSingleton.class) {
			if (instance == null) {
				instance = new ThreadSafeSingleton();
			}
		}
	}
	return instance;
}
```

Passons maintenant à la classification suivante.

## Type 2 : Structurel - Le motif de conception Décorateur

Je vais vous donner un petit scénario pour mieux comprendre pourquoi et où vous devriez utiliser le motif Décorateur.

Disons que vous possédez un café, et comme tout débutant, vous commencez avec seulement deux types de café simple, le mélange maison et le torréfié foncé. Dans votre système de facturation, il y avait une classe pour les différents mélanges de café, qui hérite de la classe abstraite boisson. Les gens commencent réellement à venir et à boire votre merveilleux (bien que peut-être amer ?) café. Ensuite, il y a les nouveaux venus au café qui, Dieu nous en préserve, veulent du sucre ou du lait. Quelle tragédie pour le café !! ??

Maintenant, vous devez également avoir ces deux ajouts, à la fois au menu et malheureusement sur le système de facturation. À l'origine, votre informaticien créera une sous-classe pour les deux cafés, l'une incluant le sucre, l'autre le lait. Ensuite, puisque les clients ont toujours raison, l'un d'eux dit ces mots redoutés :

« Puis-je avoir un café au lait avec du sucre, s'il vous plaît ? »

### ???

Voilà votre système de facturation qui se moque de vous à nouveau. Eh bien, retour à la case départ...

L'informaticien ajoute ensuite le café au lait avec du sucre comme une autre sous-classe à chaque classe de café parent. Le reste du mois se passe bien, les gens font la queue pour boire votre café, vous gagnez réellement de l'argent. ??

Mais attendez, il y a plus !

Le monde est à nouveau contre vous. Un concurrent ouvre en face, avec non seulement 4 types de café, mais plus de 10 ajouts également !

Vous achetez tout cela et plus encore, pour vendre vous-même un meilleur café, et vous vous souvenez alors que vous avez oublié de mettre à jour ce système de facturation maudit. Vous ne pouvez probablement pas créer le nombre infini de sous-classes pour toutes les combinaisons de tous les ajouts, avec les nouveaux mélanges de café également. Sans parler de la taille du système final.

Il est temps d'investir réellement dans un système de facturation approprié. Vous trouvez un nouveau personnel informatique, qui sait réellement ce qu'il fait et ils disent,

« Pourquoi, ce serait tellement plus facile et plus petit si cela utilisait le motif décorateur. »

### Qu'est-ce que c'est que ça ?

Le motif de conception décorateur appartient à la catégorie structurelle, qui traite de la structure réelle d'une classe, qu'il s'agisse d'héritage, de composition ou des deux. L'objectif de cette conception est de modifier la fonctionnalité d'un objet à l'exécution. C'est l'un des nombreux autres motifs de conception qui utilisent des classes abstraites et des interfaces avec composition pour obtenir le résultat souhaité.

Donnons une chance aux mathématiques (frisson ?) pour mettre tout cela en perspective.

Prenons 4 mélanges de café et 10 ajouts. Si nous restions à la génération de sous-classes pour chaque combinaison différente de tous les ajouts pour un type de café. Cela fait :

(10-1)² = 9² = 81 sous-classes

Nous soustrayons 1 des 10, car vous ne pouvez pas combiner un ajout avec un autre du même type, le sucre avec le sucre semble stupide. Et c'est pour un seul mélange de café. Multipliez cela **81 par 4** et vous obtenez un total de **324** sous-classes différentes ! Parlez de tout ce codage...

Mais avec le motif décorateur, il ne nécessitera que 16 classes dans ce scénario. Vous voulez parier ?

![Image](https://www.freecodecamp.org/news/content/images/2019/07/decorator-class-diagram.png)
_Diagramme de classe du motif de conception Décorateur_

![Image](https://www.freecodecamp.org/news/content/images/2019/07/decorator-coffee-class-diagram.png)
_Diagramme de classe selon le scénario du café_

Si nous cartographions notre scénario selon le diagramme de classe ci-dessus, nous obtenons 4 classes pour les 4 mélanges de café, 10 pour chaque ajout et 1 pour le composant abstrait et 1 de plus pour le décorateur abstrait. Voici ! 16 ! Maintenant, donnez-moi ces 100 $. ?? (je plaisante, mais cela ne sera pas refusé si donné... je dis juste)

Comme vous pouvez le voir ci-dessus, tout comme les mélanges de café concrets sont des sous-classes de la classe abstraite boisson, la classe abstraite AddOn hérite également de ses méthodes. Les ajouts, qui sont ses sous-classes, héritent à leur tour de nouvelles méthodes pour ajouter des fonctionnalités à l'objet de base lorsque cela est nécessaire.

Passons au codage, pour voir ce motif en utilisation.

Tout d'abord, créer la classe abstraite Beverage, dont tous les différents mélanges de café hériteront :

```java
public abstract class Beverage {
	private String description;
    
	public Beverage(String description) {
		super();
		this.description = description;
	}
    
	public String getDescription() {
		return description;
	}
    
	public abstract double cost();
}
```

Ensuite, ajouter les deux classes concrètes de mélange de café.

```java
public class HouseBlend extends Beverage {
	public HouseBlend() {
		super("House blend");
	}

	@Override
	public double cost() {
		return 250;
	}
}

public class DarkRoast extends Beverage {
	public DarkRoast() {
		super("Dark roast");
	}

	@Override
	public double cost() {
		return 300;
	}
}
```

La classe abstraite AddOn hérite également de la classe abstraite Beverage (plus d'informations à ce sujet ci-dessous).

```java
public abstract class AddOn extends Beverage {
	protected Beverage beverage;

	public AddOn(String description, Beverage bev) {
		super(description);
		this.beverage = bev;
	}

	public abstract String getDescription();
}
```

Et maintenant les implémentations concrètes de cette classe abstraite :

```java
public class Sugar extends AddOn {
	public Sugar(Beverage bev) {
		super("Sugar", bev);
	}

	@Override
	public String getDescription() {
		return beverage.getDescription() + " with Mocha";
	}

	@Override
	public double cost() {
		return beverage.cost() + 50;
	}
}

public class Milk extends AddOn {
	public Milk(Beverage bev) {
		super("Milk", bev);
	}

	@Override
	public String getDescription() {
		return beverage.getDescription() + " with Milk";
	}

	@Override  public double cost() {
		return beverage.cost() + 100;
	}
}
```

Comme vous pouvez le voir ci-dessus, nous pouvons passer n'importe quelle sous-classe de Beverage à n'importe quelle sous-classe de AddOn, et obtenir le coût ajouté ainsi que la description mise à jour. Et, puisque la classe AddOn est essentiellement de type Beverage, nous pouvons passer un AddOn dans un autre AddOn. De cette manière, nous pouvons ajouter n'importe quel nombre d'ajouts à un mélange de café spécifique.

Maintenant, écrivons du code pour tester cela.

```java
public class CoffeeShop {
	public static void main(String[] args) {
		HouseBlend houseblend = new HouseBlend();
		System.out.println(houseblend.getDescription() + " : " + houseblend.cost());

		Milk milkAddOn = new Milk(houseblend);
		System.out.println(milkAddOn.getDescription() + " : " + milkAddOn.cost());

		Sugar sugarAddOn = new Sugar(milkAddOn);
		System.out.println(sugarAddOn.getDescription() + " : " + sugarAddOn.cost());
	}
}
```

Le résultat final est :

![Image](https://www.freecodecamp.org/news/content/images/2019/07/decorator-final.PNG)
_P.S. ceci est en roupies sri-lankaises_

Cela fonctionne ! Nous avons pu ajouter plus d'un ajout à un mélange de café et mettre à jour avec succès son coût final et sa description, sans avoir besoin de créer des sous-classes infinies pour chaque combinaison d'ajouts pour tous les mélanges de café.

Enfin, la dernière catégorie.

## Type 3 : Comportemental - Le motif de conception Commande

Un motif de conception comportemental se concentre sur la manière dont les classes et les objets communiquent entre eux. L'objectif principal du motif de commande est d'inculquer un degré plus élevé de faible couplage entre les parties impliquées (lire : classes).

_Uhhhh… Qu'est-ce que c'est ?_

Le couplage est la manière dont deux (ou plusieurs) classes qui interagissent entre elles, eh bien, interagissent. Le scénario idéal lorsque ces classes interagissent est qu'elles ne dépendent pas fortement les unes des autres. C'est le faible couplage. Donc, une meilleure définition pour le faible couplage serait, des classes qui sont interconnectées, faisant le moins usage les unes des autres.

Le besoin de ce motif est apparu lorsque des demandes devaient être envoyées sans savoir consciemment ce que vous demandez ou qui est le destinataire.

Dans ce motif, la classe invoquante est découplée de la classe qui effectue réellement une action. La classe invoquante n'a que la méthode exécutable, qui exécute la commande nécessaire, lorsque le client la demande.

Prenons un exemple simple du monde réel, commander un repas dans un restaurant chic. Comme le flux le montre, vous donnez votre commande (commande) au serveur (invocateur), qui la transmet ensuite au chef (destinataire), afin que vous puissiez obtenir de la nourriture. Peut sembler simple… mais un peu ennuyeux à coder.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/chain-of-command-be-like-pop-snoke-im-going-to-27790631.png)

L'idée est assez simple, mais le codage tourne autour du nez.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/command-class-diagram.PNG)
_Diagramme de classe du motif de conception Commande_

Le flux d'opération sur le plan technique est le suivant : vous créez une commande concrète, qui implémente l'interface Commande, demandant au destinataire de compléter une action, et envoyez la commande à l'invocateur. L'invocateur est la personne qui sait quand donner cette commande. Le chef est le seul à savoir quoi faire lorsqu'il reçoit la commande spécifique. Ainsi, lorsque la méthode execute de l'invocateur est exécutée, elle provoque à son tour l'exécution de la méthode execute des objets de commande sur le destinataire, complétant ainsi les actions nécessaires.

### Ce que nous devons implémenter est :

1. Une interface Commande
2. Une classe Order qui implémente l'interface Commande
3. Une classe Waiter (invocateur)
4. Une classe Chef (destinataire)

Donc, le codage se fait comme suit :

### Chef, le destinataire

```java
public class Chef {
	public void cookPasta() {
		System.out.println("Chef is cooking Chicken Alfredo…");
	}

	public void bakeCake() {
		System.out.println("Chef is baking Chocolate Fudge Cake…");
	}
}
```

### Commande, l'interface

```java
public interface Command {
	public abstract void execute();
}
```

### Order, la commande concrète

```java
public class Order implements Command {
	private Chef chef;
	private String food;

	public Order(Chef chef, String food) {
		this.chef = chef;
		this.food = food;
	}

	@Override
	public void execute() {
		if (this.food.equals("Pasta")) {
			this.chef.cookPasta();
		} else {
			this.chef.bakeCake();
		}
	}
}
```

### Waiter, l'invocateur

```java
public class Waiter {
	private Order order;

	public Waiter(Order ord) {
		this.order = ord;
	}

	public void execute() {
		this.order.execute();
	}
}
```

## Vous, le client

```java
public class Client {
	public static void main(String[] args) {
		Chef chef = new Chef();
        
		Order order = new Order(chef, "Pasta");
		Waiter waiter = new Waiter(order);
		waiter.execute();

		order = new Order(chef, "Cake");
		waiter = new Waiter(order);
		waiter.execute();
	}
}
```

Comme vous pouvez le voir ci-dessus, le Client passe une Commande et définit le Destinataire comme le Chef. La Commande est envoyée au Serveur, qui saura quand exécuter la Commande (c'est-à-dire quand donner l'ordre au chef de cuisiner). Lorsque l'invocateur est exécuté, la méthode execute des Commandes est exécutée sur le destinataire (c'est-à-dire que le chef reçoit l'ordre de cuisiner des pâtes ? ou de cuire un gâteau ?).

![Image](https://cdn-media-1.freecodecamp.org/images/1*gwsVqEIKFmBj01M7dXsQ_A.png)
_Sortie finale du client_

## Récapitulatif rapide

Dans cet article, nous avons passé en revue :

1. Ce qu'est vraiment un motif de conception,
2. Les différents types de motifs de conception et pourquoi ils sont différents
3. Un motif de conception de base ou courant pour chaque type

J'espère que cela a été utile.  

Trouvez le dépôt de code pour l'article, [ici](https://github.com/samsam-026/Design_Patterns).