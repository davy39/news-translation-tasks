---
title: Les principes SOLID de la programmation orientée objet expliqués en français
  simple
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-20T19:43:30.000Z'
originalURL: https://freecodecamp.org/news/solid-principles-explained-in-plain-english
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/solid.png
tags:
- name: clean code
  slug: clean-code
- name: Object Oriented Programming
  slug: object-oriented-programming
seo_title: Les principes SOLID de la programmation orientée objet expliqués en français
  simple
seo_desc: "By Yiğit Kemal Erinç\nThe SOLID Principles are five principles of Object-Oriented\
  \ class design. They are a set of rules and best practices to follow while designing\
  \ a class structure. \nThese five principles help us understand the need for certain\
  \ desi..."
---

Par Yiğit Kemal Erçin

Les principes SOLID sont cinq principes de conception de classes en programmation orientée objet. Ils constituent un ensemble de règles et de bonnes pratiques à suivre lors de la conception d'une structure de classe. 

Ces cinq principes nous aident à comprendre le besoin de certains modèles de conception et de l'architecture logicielle en général. Je crois donc que c'est un sujet que chaque développeur devrait apprendre. 

Cet article vous apprendra tout ce que vous devez savoir pour appliquer les principes SOLID à vos projets. 

Nous commencerons par examiner l'histoire de ce terme. Ensuite, nous entrerons dans les détails  les pourquoi et les comment de chaque principe  en créant une conception de classe et en l'améliorant étape par étape. 

Alors, prenez une tasse de café ou de thé et plongeons-nous dans le sujet !

## Contexte

Les principes SOLID ont été introduits pour la première fois par le célèbre informaticien Robert J. Martin (alias Uncle Bob) dans son [article](https://fi.ort.edu.uy/innovaportal/file/2032/1/design_principles.pdf) en 2000. Mais l'acronyme SOLID a été introduit plus tard par Michael Feathers. 

Uncle Bob est également l'auteur des livres à succès _Clean Code_ et _Clean Architecture_, et est l'un des participants de l'["Agile Alliance"](https://agilemanifesto.org/history.html). 

Par conséquent, il n'est pas surprenant que tous ces concepts de code propre, d'architecture orientée objet et de modèles de conception soient d'une certaine manière connectés et complémentaires les uns des autres. 

Ils servent tous le même objectif : 

> "Créer un code compréhensible, lisible et testable sur lequel de nombreux développeurs peuvent travailler collaborativement."

Examinons chaque principe un par un. Suivant l'acronyme SOLID, ils sont :

* Le principe de **S**eule responsabilité
* Le principe **O**uvert-Fermé
* Le principe de **S**ubstitution de Liskov
* Le principe de **S**égrégation des interfaces
* Le principe d'**I**nversion des dépendances

## Le principe de seule responsabilité

Le principe de seule responsabilité stipule qu'**une classe doit faire une seule chose et donc elle ne doit avoir qu'une seule raison de changer**. 

Pour énoncer ce principe de manière plus technique : une seule modification potentielle (logique de base de données, logique de journalisation, etc.) dans les spécifications du logiciel doit pouvoir affecter les spécifications de la classe. 

Cela signifie que si une classe est un conteneur de données, comme une classe Book ou une classe Student, et qu'elle a certains champs concernant cette entité, elle ne doit changer que lorsque nous changeons le modèle de données.

Suivre le principe de seule responsabilité est important. Tout d'abord, parce que de nombreuses équipes différentes peuvent travailler sur le même projet et modifier la même classe pour différentes raisons, ce qui pourrait conduire à des modules incompatibles. 

Deuxièmement, cela facilite le contrôle de version. Par exemple, supposons que nous avons une classe de persistance qui gère les opérations de base de données, et que nous voyons un changement dans ce fichier dans les commits GitHub. En suivant le SRP, nous saurons que cela est lié au stockage ou à des choses liées à la base de données.

Les conflits de fusion sont un autre exemple. Ils apparaissent lorsque différentes équipes modifient le même fichier. Mais si le SRP est suivi, moins de conflits apparaîtront  les fichiers auront une seule raison de changer, et les conflits qui existent seront plus faciles à résoudre.

### Pièges courants et anti-modèles

Dans cette section, nous examinerons quelques erreurs courantes qui violent le principe de seule responsabilité. Ensuite, nous parlerons de quelques moyens de les corriger.

Nous examinerons le code d'un programme simple de facturation de librairie comme exemple. Commençons par définir une classe de livre à utiliser dans notre facture.

```java
class Book {
	String name;
	String authorName;
	int year;
	int price;
	String isbn;

	public Book(String name, String authorName, int year, int price, String isbn) {
		this.name = name;
		this.authorName = authorName;
		this.year = year;
        this.price = price;
		this.isbn = isbn;
	}
}

```

Il s'agit d'une simple classe de livre avec quelques champs. Rien de fantaisiste. Je ne rends pas les champs privés afin que nous n'ayons pas à gérer les getters et setters et que nous puissions nous concentrer sur la logique à la place.

Maintenant, créons la classe de facture qui contiendra la logique de création de la facture et de calcul du prix total. Pour l'instant, supposons que notre librairie ne vend que des livres et rien d'autre.

```java
public class Invoice {

	private Book book;
	private int quantity;
	private double discountRate;
	private double taxRate;
	private double total;

	public Invoice(Book book, int quantity, double discountRate, double taxRate) {
		this.book = book;
		this.quantity = quantity;
		this.discountRate = discountRate;
		this.taxRate = taxRate;
		this.total = this.calculateTotal();
	}

	public double calculateTotal() {
	        double price = ((book.price - book.price * discountRate) * this.quantity);

		double priceWithTaxes = price * (1 + taxRate);

		return priceWithTaxes;
	}

	public void printInvoice() {
            System.out.println(quantity + "x " + book.name + " " +          book.price + "$");
            System.out.println("Discount Rate: " + discountRate);
            System.out.println("Tax Rate: " + taxRate);
            System.out.println("Total: " + total);
	}

        public void saveToFile(String filename) {
	// Crée un fichier avec le nom donné et écrit la facture
	}

}
```

Voici notre classe de facture. Elle contient également quelques champs concernant la facturation et 3 méthodes :

* La méthode **calculateTotal**, qui calcule le prix total, 
* La méthode **printInvoice**, qui doit imprimer la facture sur la console, et 
* La méthode **saveToFile**, responsable de l'écriture de la facture dans un fichier. 

Vous devriez prendre un moment pour réfléchir à ce qui ne va pas avec cette conception de classe avant de lire le paragraphe suivant.

D'accord, alors que se passe-t-il ici ? Notre classe viole le principe de seule responsabilité de plusieurs manières. 

La première violation est la méthode **printInvoice**, qui contient notre logique d'impression. Le SRP stipule que notre classe ne doit avoir qu'une seule raison de changer, et cette raison doit être un changement dans le calcul de la facture pour notre classe. 

Mais dans cette architecture, si nous voulions changer le format d'impression, nous devrions changer la classe. C'est pourquoi nous ne devrions pas avoir de logique d'impression mélangée avec la logique métier dans la même classe.

Il y a une autre méthode qui viole le SRP dans notre classe : la méthode **saveToFile**. C'est aussi une erreur extrêmement courante de mélanger la logique de persistance avec la logique métier. 

Ne pensez pas seulement en termes d'écriture dans un fichier  cela pourrait être l'enregistrement dans une base de données, la réalisation d'un appel API, ou d'autres choses liées à la persistance.

Alors, comment pouvons-nous corriger cette fonction d'impression, pourriez-vous demander.

Nous pouvons créer de nouvelles classes pour notre logique d'impression et de persistance afin de ne plus avoir besoin de modifier la classe de facture à ces fins. 

Nous créons 2 classes, **InvoicePrinter** et **InvoicePersistence**, et déplaçons les méthodes.

```java
public class InvoicePrinter {
    private Invoice invoice;

    public InvoicePrinter(Invoice invoice) {
        this.invoice = invoice;
    }

    public void print() {
        System.out.println(invoice.quantity + "x " + invoice.book.name + " " + invoice.book.price + " $");
        System.out.println("Discount Rate: " + invoice.discountRate);
        System.out.println("Tax Rate: " + invoice.taxRate);
        System.out.println("Total: " + invoice.total + " $");
    }
}
```

```java
public class InvoicePersistence {
    Invoice invoice;

    public InvoicePersistence(Invoice invoice) {
        this.invoice = invoice;
    }

    public void saveToFile(String filename) {
        // Crée un fichier avec le nom donné et écrit la facture
    }
}
```

Maintenant, notre structure de classe respecte le principe de seule responsabilité et chaque classe est responsable d'un aspect de notre application. Super !

## Principe Ouvert-Fermé

Le principe Ouvert-Fermé exige que **les classes doivent être ouvertes à l'extension et fermées à la modification.** 

La modification signifie changer le code d'une classe existante, et l'extension signifie ajouter de nouvelles fonctionnalités. 

Donc, ce que ce principe veut dire est : nous devons être capables d'ajouter de nouvelles fonctionnalités sans toucher au code existant de la classe. Cela est dû au fait que chaque fois que nous modifions le code existant, nous prenons le risque de créer des bugs potentiels. Nous devons donc éviter de toucher au code de production testé et fiable (pour la plupart) si possible. 

Mais comment allons-nous ajouter de nouvelles fonctionnalités sans toucher à la classe, pourriez-vous demander. Cela est généralement fait avec l'aide d'interfaces et de classes abstraites.

Maintenant que nous avons couvert les bases du principe, appliquons-le à notre application de facturation. 

Supposons que notre patron est venu nous voir et nous a dit qu'il veut que les factures soient enregistrées dans une base de données afin que nous puissions les rechercher facilement. Nous pensons que c'est facile, patron, donnez-moi juste une seconde ! 

Nous créons la base de données, nous nous y connectons, et nous ajoutons une méthode de sauvegarde à notre classe **InvoicePersistence** :

```java
public class InvoicePersistence {
    Invoice invoice;

    public InvoicePersistence(Invoice invoice) {
        this.invoice = invoice;
    }

    public void saveToFile(String filename) {
        // Crée un fichier avec le nom donné et écrit la facture
    }

    public void saveToDatabase() {
        // Enregistre la facture dans la base de données
    }
}
```

Malheureusement, en tant que développeur paresseux pour la librairie, nous n'avons pas conçu les classes pour qu'elles soient facilement extensibles à l'avenir. Donc, pour ajouter cette fonctionnalité, nous avons modifié la classe **InvoicePersistence**. 

Si notre conception de classe obéissait au principe Ouvert-Fermé, nous n'aurions pas besoin de changer cette classe. 

Donc, en tant que développeur paresseux mais intelligent pour la librairie, nous voyons le problème de conception et décidons de refactoriser le code pour obéir au principe.

```java
interface InvoicePersistence {

    public void save(Invoice invoice);
}
```

Nous changeons le type de **InvoicePersistence** en Interface et ajoutons une méthode save. Chaque classe de persistance implémentera cette méthode save.

```java
public class DatabasePersistence implements InvoicePersistence {

    @Override
    public void save(Invoice invoice) {
        // Enregistrer dans la base de données
    }
}
```

```java
public class FilePersistence implements InvoicePersistence {

    @Override
    public void save(Invoice invoice) {
        // Enregistrer dans un fichier
    }
}
```

Donc, notre structure de classe ressemble maintenant à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/08/solid-article-image-1.png)

Maintenant, notre logique de persistance est facilement extensible. Si notre patron nous demande d'ajouter une autre base de données et d'avoir 2 types de bases de données différents comme MySQL et MongoDB, nous pouvons facilement le faire. 

Vous pourriez penser que nous pourrions simplement créer plusieurs classes sans interface et ajouter une méthode save à toutes. 

Mais supposons que nous étendons notre application et avons plusieurs classes de persistance comme **InvoicePersistence**, **BookPersistence** et nous créons une classe **PersistenceManager** qui gère toutes les classes de persistance :

```java
public class PersistenceManager {
    InvoicePersistence invoicePersistence;
    BookPersistence bookPersistence;
    
    public PersistenceManager(InvoicePersistence invoicePersistence,
                              BookPersistence bookPersistence) {
        this.invoicePersistence = invoicePersistence;
        this.bookPersistence = bookPersistence;
    }
}
```

Nous pouvons maintenant passer n'importe quelle classe qui implémente l'interface **InvoicePersistence** à cette classe grâce au polymorphisme. C'est la flexibilité que fournissent les interfaces.

## Principe de substitution de Liskov

Le principe de substitution de Liskov stipule que les sous-classes doivent être substituables à leurs classes de base. 

Cela signifie que, étant donné que la classe B est une sous-classe de la classe A, nous devons pouvoir passer un objet de la classe B à toute méthode qui attend un objet de la classe A et la méthode ne doit pas donner de sortie étrange dans ce cas. 

C'est le comportement attendu, car lorsque nous utilisons l'héritage, nous supposons que la classe enfant hérite de tout ce que la superclasse a. La classe enfant étend le comportement mais ne le restreint jamais. 

Par conséquent, lorsqu'une classe n'obéit pas à ce principe, cela conduit à certains bugs désagréables qui sont difficiles à détecter. 

Le principe de Liskov est facile à comprendre mais difficile à détecter dans le code. Alors, examinons un exemple.

```java
class Rectangle {
	protected int width, height;

	public Rectangle() {
	}

	public Rectangle(int width, int height) {
		this.width = width;
		this.height = height;
	}

	public int getWidth() {
		return width;
	}

	public void setWidth(int width) {
		this.width = width;
	}

	public int getHeight() {
		return height;
	}

	public void setHeight(int height) {
		this.height = height;
	}

	public int getArea() {
		return width * height;
	}
}
```

Nous avons une simple classe Rectangle, et une fonction **getArea** qui retourne l'aire du rectangle.

Maintenant, nous décidons de créer une autre classe pour les carrés. Comme vous le savez peut-être, un carré est simplement un type spécial de rectangle où la largeur est égale à la hauteur.

```java
class Square extends Rectangle {
	public Square() {}

	public Square(int size) {
		width = height = size;
	}

	@Override
	public void setWidth(int width) {
		super.setWidth(width);
		super.setHeight(width);
	}

	@Override
	public void setHeight(int height) {
		super.setHeight(height);
		super.setWidth(height);
	}
}
```

Notre classe Square étend la classe Rectangle. Nous définissons la hauteur et la largeur à la même valeur dans le constructeur, mais nous ne voulons pas qu'un client (quelqu'un qui utilise notre classe dans son code) change la hauteur ou la largeur de manière à pouvoir violer la propriété du carré. 

Par conséquent, nous remplaçons les setters pour définir les deux propriétés chaque fois que l'une d'elles est modifiée. Mais en faisant cela, nous avons violé le principe de substitution de Liskov.

Créons une classe principale pour effectuer des tests sur la fonction **getArea**.

```java
class Test {

   static void getAreaTest(Rectangle r) {
      int width = r.getWidth();
      r.setHeight(10);
      System.out.println("Expected area of " + (width * 10) + ", got " + r.getArea());
   }

   public static void main(String[] args) {
      Rectangle rc = new Rectangle(2, 3);
      getAreaTest(rc);

      Rectangle sq = new Square();
      sq.setWidth(5);
      getAreaTest(sq);
   }
}
```

Le testeur de votre équipe vient de créer la fonction de test **getAreaTest** et vous dit que votre fonction **getArea** échoue à passer le test pour les objets carrés. 

Dans le premier test, nous créons un rectangle où la largeur est de 2 et la hauteur de 3 et appelons **getAreaTest**. La sortie est 20 comme prévu, mais les choses tournent mal lorsque nous passons le carré. Cela est dû au fait que l'appel de la fonction **setHeight** dans le test définit également la largeur et entraîne une sortie inattendue.

## Principe de ségrégation des interfaces

La ségrégation signifie garder les choses séparées, et le principe de ségrégation des interfaces concerne la séparation des interfaces. 

Le principe stipule que plusieurs interfaces spécifiques au client sont meilleures qu'une interface générale. Les clients ne doivent pas être forcés d'implémenter une fonction dont ils n'ont pas besoin. 

C'est un principe simple à comprendre et à appliquer, alors examinons un exemple.

```java
public interface ParkingLot {

	void parkCar();	// Diminue le nombre de places vides de 1
	void unparkCar(); // Augmente le nombre de places vides de 1
	void getCapacity();	// Retourne la capacité en voitures
	double calculateFee(Car car); // Retourne le prix en fonction du nombre d'heures
	void doPayment(Car car);
}

class Car {

}
```

Nous avons modélisé un parking très simplifié. Il s'agit du type de parking où vous payez des frais horaires. Maintenant, supposons que nous voulons implémenter un parking qui est gratuit.

```java
public class FreeParking implements ParkingLot {

	@Override
	public void parkCar() {
		
	}

	@Override
	public void unparkCar() {

	}

	@Override
	public void getCapacity() {

	}

	@Override
	public double calculateFee(Car car) {
		return 0;
	}

	@Override
	public void doPayment(Car car) {
		throw new Exception("Parking lot is free");
	}
}
```

Notre interface de parking était composée de 2 choses : la logique liée au parking (parquer une voiture, déparquer une voiture, obtenir la capacité) et la logique liée au paiement. 

Mais elle est trop spécifique. À cause de cela, notre classe FreeParking a été forcée d'implémenter des méthodes liées au paiement qui sont sans pertinence. Séparons ou ségrégons les interfaces.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/solid-article-image-2.png)

Nous avons maintenant séparé le parking. Avec ce nouveau modèle, nous pouvons même aller plus loin et diviser le **PaidParkingLot** pour prendre en charge différents types de paiement. 

Notre modèle est maintenant beaucoup plus flexible, extensible, et les clients n'ont pas besoin d'implémenter de logique sans pertinence car nous fournissons uniquement des fonctionnalités liées au parking dans l'interface de parking.

## Principe d'inversion des dépendances

Le principe d'inversion des dépendances stipule que nos classes doivent dépendre d'interfaces ou de classes abstraites plutôt que de classes et de fonctions concrètes. 

Dans son [article](https://fi.ort.edu.uy/innovaportal/file/2032/1/design_principles.pdf) (2000), Uncle Bob résume ce principe comme suit : 

> "Si l'OCP énonce l'objectif de l'architecture OO, le DIP énonce le mécanisme principal". 

Ces deux principes sont en effet liés et nous avons appliqué ce modèle auparavant lors de notre discussion sur le principe Ouvert-Fermé. 

Nous voulons que nos classes soient ouvertes à l'extension, nous avons donc réorganisé nos dépendances pour qu'elles dépendent d'interfaces plutôt que de classes concrètes. Notre classe PersistenceManager dépend de InvoicePersistence plutôt que des classes qui implémentent cette interface.

## Conclusion

Dans cet article, nous avons commencé par l'histoire des principes SOLID, puis nous avons essayé d'acquérir une compréhension claire des pourquoi et des comment de chaque principe. Nous avons même refactorisé une simple application de facturation pour obéir aux principes SOLID. 

Je tiens à vous remercier d'avoir pris le temps de lire l'article entier et j'espère que les concepts ci-dessus sont clairs. 

Je suggère de garder ces principes à l'esprit lors de la conception, de l'écriture et de la refactorisation de votre code afin que votre code soit beaucoup plus propre, extensible et testable. 

Si vous êtes intéressé à lire plus d'articles comme celui-ci, vous pouvez vous abonner à la liste de diffusion de mon [blog](https://erinc.io/) pour être informé lorsque je publie un nouvel article.