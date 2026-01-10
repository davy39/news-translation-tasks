---
title: 'Principes de la programmation orientée objet en Java : concepts POO pour débutants'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-01T12:46:39.000Z'
originalURL: https://freecodecamp.org/news/java-object-oriented-programming-system-principles-oops-concepts-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/Love-Home.png
tags:
- name: Java
  slug: java
- name: Object Oriented Programming
  slug: object-oriented-programming
seo_title: 'Principes de la programmation orientée objet en Java : concepts POO pour
  débutants'
seo_desc: 'By Thanoshan MV


  Object-oriented programming offers a sustainable way to write spaghetti code. It
  lets you accrete programs as a series of patches.― Paul Graham


  Fundamentals of object-oriented programming

  Object-oriented programming is a programming...'
---

Par Thanoshan MV

> _La programmation orientée objet offre une manière durable d'écrire du code spaghetti. Elle permet d'accumuler des programmes sous forme de séries de correctifs._
> _— Paul Graham_

## Fondamentaux de la programmation orientée objet

La programmation orientée objet est un paradigme de programmation où tout est représenté comme un objet.

Les objets s'envoient des messages les uns aux autres. Chaque objet décide quoi faire avec un message reçu. La POO se concentre sur les états et les comportements de chaque objet.

### Qu'est-ce qu'un objet ?

**Un objet est une entité qui possède des états et des comportements.**

Par exemple, chien, chat et véhicule. Pour illustrer, un chien a des états comme l'âge, la couleur, le nom, et des comportements comme manger, dormir et courir.

L'état nous indique comment l'objet apparaît ou quelles propriétés il possède.

Le comportement nous indique ce que l'objet fait.

Nous pouvons effectivement représenter un chien du monde réel dans un programme comme un objet logiciel en définissant ses états et ses comportements.

Les objets logiciels sont la représentation réelle des objets du monde réel. La mémoire est allouée en RAM chaque fois qu'un objet logique est créé.

Un objet est également appelé une instance d'une classe. Instancier une classe signifie la même chose que créer un objet.

La chose importante à retenir lors de la création d'un objet est : le type de référence doit être du **même type** ou d'un **super type** du type de l'objet. Nous verrons ce qu'est un type de référence plus tard dans cet article.

### Qu'est-ce qu'une classe ?

**Une classe est un modèle ou un plan à partir duquel des objets sont créés.**

Imaginez une classe comme un emporte-pièce et les objets comme des biscuits.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/cookie-cutter.jpg)
_Figure 1 : Illustre la relation entre classe et objet à travers un emporte-pièce et des biscuits. [Source](https://www.piqsels.com/en/public-domain-photo-sswme" rel="noopener)._

Les classes définissent les états comme des variables d'instance et les comportements comme des méthodes d'instance.

Les variables d'instance sont également connues sous le nom de variables membres.

Les classes ne consomment aucun espace.

Pour vous donner une idée des classes et des objets, créons une classe Chat qui représente les états et les comportements d'un chat du monde réel.

```java
public class Chat {
    /*
    Variables d'instance : états du Chat
     */
    String nom;
    int age;
    String couleur;
    String race;

    /*
    Méthodes d'instance : comportements du Chat
     */
    void dormir(){
        System.out.println("Dort");
    }
    void jouer(){
        System.out.println("Joue");
    }
    void nourrir(){
        System.out.println("Mange");
    }

}
```

Maintenant, nous avons réussi à définir un modèle pour Chat. Supposons que nous avons deux chats nommés Thor et Rambo.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Russian-Blue_01.jpg)
_Figure 2 : Thor dort. [Source](https://www.petfinder.com/cat-breeds/collections/cutest-cat-breeds/" rel="noopener)_

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Maine-Coon_02.jpg)
_Figure 3 : Rambo joue. [Source](https://www.petfinder.com/cat-breeds/collections/cutest-cat-breeds/" rel="noopener)_

Comment pouvons-nous les définir dans notre programme ?

Tout d'abord, nous devons créer deux objets de la classe Chat.

```java
public class Main {
    public static void main(String[] args) {
       Chat thor = new Chat();
       Chat rambo = new Chat();
    }
}
```

Ensuite, nous allons définir leurs états et comportements.

```java
public class Main {

    public static void main(String[] args) {
       /*
       Création d'objets
        */
       Chat thor = new Chat();
       Chat rambo = new Chat();

       /*
       Définition du chat Thor
        */
       thor.nom = "Thor";
       thor.age = 3;
       thor.race = "Bleu Russe";
       thor.couleur = "Marron";

       thor.dormir();

       /*
       Définition du chat Rambo
        */
       rambo.nom = "Rambo";
       rambo.age = 4;
       rambo.race = "Maine Coon";
       rambo.couleur = "Marron";

       rambo.jouer();
    }

}
```

Comme dans les exemples de code ci-dessus, nous pouvons définir notre classe, l'instancier (créer des objets) et spécifier les états et les comportements pour ces objets.

Maintenant, nous avons couvert les bases de la programmation orientée objet. Passons aux principes de la programmation orientée objet.

## Principes de la programmation orientée objet

Ce sont les quatre principaux principes du paradigme de la programmation orientée objet. Les comprendre est essentiel pour devenir un programmeur accompli.

1. Encapsulation
2. Héritage
3. Abstraction
4. Polymorphisme

Maintenant, examinons chacun d'eux plus en détail.

## Encapsulation

**L'encapsulation est un processus d'encapsulage de code et de données ensemble en une seule unité.**

C'est comme une capsule qui contient un mélange de plusieurs médicaments, et c'est une technique qui aide à garder les variables d'instance protégées.

Cela peut être réalisé en utilisant des modificateurs d'accès `private` qui ne peuvent pas être accédés par quoi que ce soit en dehors de la classe. Afin d'accéder en toute sécurité aux états privés, nous devons fournir des méthodes publiques getter et setter. (En Java, ces méthodes doivent suivre les normes de nommage JavaBeans.)

Supposons qu'il y ait un magasin de disques qui vend des albums musicaux de différents artistes et un gestionnaire de stock qui les gère.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/classDiagramWithoutEncapsulation.png)
_Figure 4 : Diagramme de classe sans encapsulation_

Si vous regardez la figure 4, la classe `StockKeeper` peut accéder directement aux états de la classe `Album` car les états de la classe `Album` sont définis sur `public`.

Que se passe-t-il si le gestionnaire de stock crée un album et définit des états avec des valeurs négatives ? Cela peut être fait intentionnellement ou non par un gestionnaire de stock.

Pour illustrer, voyons un exemple de programme Java qui explique le diagramme et l'énoncé ci-dessus.

Classe Album :

```java
public class Album {
    public String nom;
    public String artiste;
    public double prix;
    public int nombreDeCopies;
    public void vendreCopies(){
        if(nombreDeCopies > 0){
            nombreDeCopies--;
            System.out.println("Un album a été vendu !");
        }
        else{
            System.out.println("Plus d'albums disponibles !");
        }
    }
    public void commanderCopies(int num){
        nombreDeCopies += num;
    }
}
```

Classe StockKeeper :

```java
public class StockKeeper {
    public String nom;
    public StockKeeper(String nom){
        this.nom = nom;
    }
    public void gererAlbum(Album album, String nom, String artiste, double prix, int nombreDeCopies){
      /*
       Définition des états et comportements pour l'album
       */
        album.nom = nom;
        album.artiste = artiste;
        album.prix = prix;
        album.nombreDeCopies = nombreDeCopies;

       /*
       Impression des détails de l'album
        */
        System.out.println("Album géré par :"+ this.nom);
        System.out.println("Détails de l'album::::::::::");
        System.out.println("Nom de l'album : " + album.nom);
        System.out.println("Artiste de l'album : " + album.artiste);
        System.out.println("Prix de l'album : " + album.prix);
        System.out.println("Nombre de copies de l'album : " + album.nombreDeCopies);
    }
}
```

Classe Main :

```java
public class Main {
    public static void main(String[] args) {
       StockKeeper johnDoe = new StockKeeper("John Doe");
       /*
       Le gestionnaire de stock crée un album et attribue des valeurs négatives pour le prix et le nombre de copies disponibles
        */
       johnDoe.gererAlbum(new Album(), "Slippery When Wet", "Bon Jovi", -1000.00, -50);
    }
}
```

Sortie :

```java
Album géré par :John Doe
Détails de l'album::::::::::
Nom de l'album : Slippery When Wet
Artiste de l'album : Bon Jovi
Prix de l'album : -1000.0
Nombre de copies de l'album : -50
```

Le prix de l'album et le nombre de copies ne peuvent pas être des valeurs négatives. Comment pouvons-nous éviter cette situation ? C'est là que nous utilisons l'encapsulation.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/classDiagramWithEncapsulation-1.png)
_Figure 5 : Diagramme de classe avec encapsulation_

Dans ce scénario, nous pouvons empêcher le gestionnaire de stock d'attribuer des valeurs négatives. S'ils tentent d'attribuer des valeurs négatives pour le prix de l'album et le nombre de copies, nous les définirons comme 0.0 et 0.

Classe Album :

```java
public class Album {
    private String nom;
    private String artiste;
    private double prix;
    private int nombreDeCopies;
    public void vendreCopies(){
        if(nombreDeCopies > 0){
            nombreDeCopies--;
            System.out.println("Un album a été vendu !");
        }
        else{
            System.out.println("Plus d'albums disponibles !");
        }
    }
    public void commanderCopies(int num){
        nombreDeCopies += num;
    }
   public String getNom() {
      return nom;
   }
   public void setNom(String nom) {
      this.nom = nom;
   }
   public String getArtiste() {
      return artiste;
   }
   public void setArtiste(String artiste) {
      this.artiste = artiste;
   }
   public double getPrix() {
      return prix;
   }
   public void setPrix(double prix) {
      if(prix > 0) {
         this.prix = prix;          
      }
      else {
         this.prix = 0.0;
      }
   }
   public int getNombreDeCopies() {
      return nombreDeCopies;
   }
   public void setNombreDeCopies(int nombreDeCopies) {
      if(nombreDeCopies > 0) {
         this.nombreDeCopies = nombreDeCopies;        
      }
      else {
         this.nombreDeCopies = 0;
      }
   }
}
```

Classe StockKeeper :

```java
public class StockKeeper {
    private String nom;
    StockKeeper(String nom){
        setNom(nom);
    }
    public void gererAlbum(Album album, String nom, String artiste, double prix, int nombreDeCopies){
         /*
          Définition des états et comportements pour l'album
          */
        album.setNom(nom);
        album.setArtiste(artiste);
        album.setPrix(prix);
        album.setNombreDeCopies(nombreDeCopies);
          /*
          Impression des détails de l'album
           */
        System.out.println("Album géré par :"+ getNom());
        System.out.println("Détails de l'album::::::::::");
        System.out.println("Nom de l'album : " + album.getNom());
        System.out.println("Artiste de l'album : " + album.getArtiste());
        System.out.println("Prix de l'album : " + album.getPrix());
        System.out.println("Nombre de copies de l'album : " + album.getNombreDeCopies());
    }
    public String getNom() {
        return nom;
    }
    public void setNom(String nom) {
        this.nom = nom;
    }
}
```

Classe Main :

```java
public class Main {
    public static void main(String[] args) {
       StockKeeper johnDoe = new StockKeeper("John Doe");
       /*
       Le gestionnaire de stock crée un album et attribue des valeurs négatives pour le prix et le nombre de copies disponibles
        */
       johnDoe.gererAlbum(new Album(), "Slippery When Wet", "Bon Jovi", -1000.00, -50);
    }
}
```

Sortie :

```java
Album géré par :John Doe
Détails de l'album::::::::::
Nom de l'album : Slippery When Wet
Artiste de l'album : Bon Jovi
Prix de l'album : 0.0
Nombre de copies de l'album : 0
```

Avec l'encapsulation, nous avons empêché notre gestionnaire de stock d'attribuer des valeurs négatives, ce qui signifie que nous avons le contrôle sur les données.

### Avantages de l'encapsulation en Java

1. Nous pouvons rendre une classe **lecture seule** ou **écriture seule** : pour une classe en lecture seule, nous devons fournir uniquement une méthode getter. Pour une classe en écriture seule, nous devons fournir uniquement une méthode setter.
2. Contrôle sur les données : nous pouvons contrôler les données en fournissant une logique aux méthodes setter, tout comme nous avons restreint le gestionnaire de stock d'attribuer des valeurs négatives dans l'exemple ci-dessus.
3. Masquage des données : d'autres classes ne peuvent pas accéder directement aux membres privés d'une classe.

## Héritage

Supposons que le magasin de disques dont nous avons parlé ci-dessus vende également des films Blu-ray.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/classDiagramForMovie.png)
_Figure 6 : Diagramme de classe pour Film, StockKeeper_

Comme vous pouvez le voir dans le diagramme ci-dessus, il y a de nombreux états et comportements communs (code commun) entre `Album` et `Film`.

Lors de la mise en œuvre de ce diagramme de classe en code, allez-vous écrire (ou copier et coller) tout le code pour `Film` ? Si vous le faites, vous vous répétez. Comment pouvez-vous éviter la duplication de code ?

C'est là que nous utilisons l'héritage.

**L'héritage est un mécanisme dans lequel un objet acquiert tous les états et comportements d'un objet parent.**

L'héritage utilise une relation parent-enfant (relation EST-UN).

### Alors, qu'est-ce qui est exactement hérité ?

**Les modificateurs de visibilité/d'accès** impactent ce qui est hérité d'une classe à une autre.

En Java, en tant que **règle générale**, nous rendons les variables d'instance `private` et les méthodes d'instance `public`.

Dans ce cas, nous pouvons dire en toute sécurité que les éléments suivants sont hérités :

1. méthodes d'instance publiques.
2. variables d'instance privées (les variables d'instance privées ne peuvent être accédées que par le biais de méthodes publiques getter et setter).

### Types d'héritage en Java

Il existe cinq types d'héritage en Java. Ils sont simples, multiniveaux, hiérarchiques, multiples et hybrides.

La classe permet les héritages simples, multiniveaux et hiérarchiques. L'interface permet les héritages multiples et hybrides.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/InheritanceTypes.jpg)
_Figure 7 : Types d'héritage Java_

Une classe peut étendre une seule classe, mais elle peut implémenter n'importe quel nombre d'interfaces. Une interface peut étendre plus d'une interface.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/inheritanceKeywords.jpg)
_Figure 8 : Explique les mots-clés d'héritage._

### Relations

**I. Relation EST-UN**

Une relation EST-UN fait référence à l'héritage ou à l'implémentation.

#### a. Généralisation

La généralisation utilise une relation EST-UN d'une classe de spécialisation à une classe de généralisation.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/generalization.jpg)
_Figure 9 : Diagramme de généralisation_

#### II. Relation A-UN

Une instance d'une classe A-UN référence à une instance d'une autre classe.

#### a. Agrégation

Dans cette relation, l'existence des classes A et B ne dépend pas l'une de l'autre.

Pour cette partie d'agrégation, nous allons voir un exemple de la classe `Etudiant` et de la classe `ContactInfo`.

```java
class ContactInfo {
    private String adresseDomicile;
    private String adresseEmail;
    private int numeroTelephone; //12025550156
}
public class Etudiant {
    private String nom;
    private int age;
    private int niveau;
    private ContactInfo contactInfo;//Etudiant A-UN ContactInfo
    public void etudier() {
        System.out.println("Etudier");
    }
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/aggregation-1.png)
_Figure 10 : Diagramme de classe montrant la relation de généralisation_

`Etudiant` A-UN `ContactInfo`. `ContactInfo` peut être utilisé dans d'autres endroits — par exemple, une classe `Employe` d'une entreprise peut également utiliser cette classe `ContactInfo`. Donc `Etudiant` peut exister sans `ContactInfo` et `ContactInfo` peut exister sans `Etudiant`. Ce type de relation est connu sous le nom d'agrégation.

#### b. Composition

Dans cette relation, la classe B ne peut pas exister sans la classe A — mais la classe A **peut** exister sans la classe B.

Pour vous donner une idée de la composition, voyons un exemple de la classe `Etudiant` et de la classe `IdentifiantEtudiant`.

```java
class IdentifiantEtudiant {
    private String numeroIdentifiant;//A-123456789
    private String groupeSanguin;
    private String numeroCompte;
}
public class Etudiant {
    private String nom;
    private int age;
    private int niveau;
    private IdentifiantEtudiant identifiantEtudiant;//Etudiant A-UN IdentifiantEtudiant
    public void etudier() {
        System.out.println("Etudier");
    }
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/composition--1-.png)
_Figure 11 : Diagramme de classe montrant la relation de composition_

`Etudiant` A-UN `IdentifiantEtudiant`. `Etudiant` peut exister sans `IdentifiantEtudiant` mais `IdentifiantEtudiant` ne peut pas exister sans `Etudiant`. Ce type de relation est connu sous le nom de composition.

Maintenant, revenons à notre exemple précédent de magasin de disques dont nous avons discuté ci-dessus.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/classDiagramWithInheritance.png)
_Figure 12 : Diagramme de classe avec héritage_

Nous pouvons implémenter ce diagramme en Java pour éviter la duplication de code.

#### Avantages de l'héritage

1. Réutilisation de code : la classe enfant hérite de tous les membres d'instance de la classe parente.
2. Vous avez plus de flexibilité pour changer le code : changer le code en place est suffisant.
3. Vous pouvez utiliser le polymorphisme : le remplacement de méthode nécessite une relation EST-UN.

## Abstraction

**L'abstraction est un processus de masquage des détails d'implémentation et de présentation de la seule fonctionnalité à l'utilisateur.**

Un exemple courant d'abstraction est que le fait d'appuyer sur l'accélérateur augmentera la vitesse d'une voiture. Mais le conducteur ne sait pas comment appuyer sur l'accélérateur augmente la vitesse — ils n'ont pas besoin de le savoir.

Techniquement, abstrait signifie quelque chose d'incomplet ou à compléter plus tard.

En Java, nous pouvons atteindre l'abstraction de deux manières : classe abstraite (0 à 100 %) et interface (100 %).

Le mot-clé `abstract` peut être appliqué aux classes et aux méthodes. `abstract` et `final` ou `static` ne peuvent jamais être ensemble.

#### I. Classe abstraite

Une classe abstraite est une classe qui contient le mot-clé `abstract`.

Les classes abstraites ne peuvent pas être instanciées (on ne peut pas créer d'objets de classes abstraites). Elles peuvent avoir des constructeurs, des méthodes statiques et des méthodes finales.

#### II. Méthodes abstraites

Une méthode abstraite est une méthode qui contient le mot-clé `abstract`.

Une méthode abstraite n'a pas d'implémentation (pas de corps de méthode et se termine par un point-virgule). Elle ne doit pas être marquée comme `private`.

#### III. Classe abstraite et méthodes abstraites

* Si au moins une méthode abstraite existe à l'intérieur d'une classe, alors toute la classe doit être abstraite.
* Nous pouvons avoir une classe abstraite sans méthodes abstraites.
* Nous pouvons avoir n'importe quel nombre de méthodes abstraites ainsi que non abstraites à l'intérieur d'une classe abstraite en même temps.
* La première sous-classe concrète d'une classe abstraite doit fournir une implémentation à toutes les méthodes abstraites.
* Si cela ne se produit pas, alors la sous-classe doit également être marquée comme abstraite.

Dans un scénario du monde réel, l'implémentation sera fournie par quelqu'un qui est inconnu des utilisateurs finaux. Les utilisateurs ne connaissent pas la classe d'implémentation et l'implémentation réelle.

Considérons un exemple d'utilisation du concept abstrait.

```java
abstract class Forme {
    public abstract void dessiner();
}
class Cercle extends Forme{
    public void dessiner() {
        System.out.println("Cercle !");
    }
}
public class Test {
    public static void main(String[] args) {
        Forme cercle = new Cercle();
        cercle.dessiner();
    }
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/abstraction.png)
_Figure 13 : Diagramme de classe qui montre la relation entre une classe abstraite et une classe concrète_

#### Quand voulons-nous marquer une classe comme abstraite ?

1. Pour forcer les sous-classes à implémenter des méthodes abstraites.
2. Pour empêcher d'avoir des objets réels de cette classe.
3. Pour continuer à avoir une référence de classe.
4. Pour conserver le code de classe commun.

### Interface

**Une interface est un plan de classe.**

Une interface est 100 % abstraite. Aucun constructeur n'est autorisé ici. Elle représente une relation EST-UN.

**NOTE :** Les interfaces définissent uniquement les méthodes requises. Nous ne pouvons pas conserver de code commun.

Une interface ne peut avoir que des méthodes abstraites, pas de méthodes concrètes. Par défaut, les méthodes d'interface sont `public` et `abstract`. Donc à l'intérieur de l'interface, nous n'avons pas besoin de spécifier `public` et `abstract`.

Ainsi, lorsqu'une classe implémente une méthode d'interface sans spécifier le niveau d'accès de cette méthode, le compilateur générera une erreur indiquant « Cannot reduce the visibility of the inherited method from interface ». Ainsi, le niveau d'accès de la méthode implémentée doit être défini sur `public`.

Par défaut, les variables d'interface sont `public`, `static` et `final`.

Par exemple :

```java
interface Executable {
    int a = 10; //similaire à : public static final int a = 10;
    void executer(); //similaire à : public abstract void executer();
}
public class VerificateurInterface implements Executable{
    public static void main(String[] args) {
        Executable.a = 5;//Le champ final Executable.a ne peut pas être assigné.
    }
}
```

Voyons un exemple qui explique le concept d'interface :

```java
interface Dessiner {
    void dessiner();
}
class Cercle implements Dessiner{
    public void dessiner() {
        System.out.println("Cercle !");
    }
}
public class VerificateurInterface {
    public static void main(String[] args) {
        Dessiner cercle = new Cercle();
        cercle.dessiner();
    }
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/interface.png)
_Figure 14 : Diagramme de classe qui montre la relation entre une interface et une classe concrète_

#### Méthodes par défaut et statiques dans les interfaces

Habituellement, nous implémentons les méthodes d'interface dans une classe séparée. Supposons que nous devons ajouter une nouvelle méthode dans une interface. Alors, nous devons implémenter cette méthode dans cette classe séparée également.

Pour surmonter ce problème, Java 8 a introduit des méthodes par défaut et statiques qui implémentent des méthodes à l'intérieur d'une interface, contrairement aux méthodes abstraites.

* **Méthode par défaut**

```java
public interface InterfaceParDefaut {
    void dormir();
    default void courir() {
        System.out.println("Je cours !");
    }
}
public class VerificateursInterface implements InterfaceParDefaut{
    public void dormir() {
        System.out.println("Dort...");
    }
    public static void main(String[] args) {
        VerificateursInterface verificateur = new VerificateursInterface();
        verificateur.courir();
        verificateur.dormir();
    }
}
/*
Sortie :
Je cours !
Dort...
 */
```

* **Méthode statique**

Similaire aux méthodes statiques des classes, nous pouvons les appeler par le nom de leur interface.

```java
public interface InterfaceParDefaut {
    void dormir();
    static void courir() {
        System.out.println("Je cours !");
    }
}
public class VerificateursInterface implements InterfaceParDefaut{
    public void dormir() {
        System.out.println("Dort...");
    }
    public static void main(String[] args) {
        VerificateursInterface verificateur = new VerificateursInterface();
        InterfaceParDefaut.courir();
        verificateur.dormir();
    }
}
/*
Sortie :
Je cours !
Dort...
 */
```

* **Interface marqueur**

C'est une interface vide. Par exemple, les interfaces Serializable, Cloneable et Remote.

```java
public interface Serializable
{
  //Pas de champs ou de méthodes
}
```

### Avantages des interfaces

* Elles nous aident à utiliser l'héritage multiple en Java.
* Elles fournissent l'abstraction.
* Elles fournissent un couplage lâche : les objets sont indépendants les uns des autres.

### Quand voulons-nous changer une classe en interface ?

1. Pour forcer les sous-classes à implémenter des méthodes abstraites.
2. Pour empêcher d'avoir des objets réels de cette classe.
3. Pour continuer à avoir une référence de classe.

**NOTE :** Rappelez-vous, nous ne pouvons pas conserver de code commun à l'intérieur de l'interface.

Si vous voulez définir des méthodes potentiellement requises et du code commun, utilisez une **classe abstraite**.

Si vous voulez simplement définir une méthode requise, utilisez une **interface**.

## Polymorphisme

**Le polymorphisme est la capacité d'un objet à prendre de nombreuses formes.**

Le polymorphisme en POO se produit lorsqu'une super classe référence un objet de sous-classe.

Tous les objets Java sont considérés comme polymorphes car ils partagent plus d'une relation EST-UN (au moins tous les objets passeront le test EST-UN pour leur propre type et pour la classe Object).

Nous pouvons accéder à un objet par le biais d'une variable de référence. Une variable de référence ne peut être que d'un seul type. Une fois déclarée, le type d'une variable de référence ne peut pas être changé.

Une variable de référence peut être déclarée comme un type de classe ou d'interface.

Un seul objet peut être référencé par des variables de référence de nombreux types différents tant qu'ils sont du **même type** ou d'un **super type** de l'objet.

### Surcharge de méthode

**Si une classe a plusieurs méthodes qui ont le même nom mais des paramètres différents, cela est connu sous le nom de surcharge de méthode.**

Règles de surcharge de méthode :

1. **Doit avoir une liste de paramètres différente.**
2. Peut avoir des types de retour différents.
3. Peut avoir des modificateurs d'accès différents.
4. Peut lancer des exceptions différentes.

```java
class ProgrammeurJava{
    public void coder() {
        System.out.println("Coder en C++");
    }
    public void coder(String langage) {
        System.out.println("Coder en "+langage);
    }
}
public class SurchargeurDeMethode {
    public static void main(String[] args) {
        ProgrammeurJava gosling = new ProgrammeurJava();
        gosling.coder();
        gosling.coder("Java");
    }
}
/*
Sortie :
Coder en C++
Coder en Java
 */
```

**NOTE :** Les méthodes statiques peuvent également être surchargées.

```java
class Addition {
    public static int ajouter(int a,int b) {
        return a+b;
    }
    public static int ajouter(int a,int b,int c) {
        return a+b+c;
    }
}
public class TestPoly {
    public static void main(String[] args) {
        System.out.println(Addition.ajouter(5, 5));
        System.out.println(Addition.ajouter(2, 4, 6));
    }
}
```

**NOTE :** Nous pouvons surcharger la méthode main() mais la machine virtuelle Java (JVM) appelle la méthode main() qui reçoit des tableaux de chaînes comme arguments.

```java
public class TestPoly {
    public static void main() {
        System.out.println("main()");
    }
    public static void main(String args) {
        System.out.println("String args");
    }
    public static void main(String[] args) {
        System.out.println("String[] args");
    }
}
//Sortie : String[] args
```

### Règles à suivre pour le polymorphisme

#### Règles de compilation

1. Le compilateur ne connaît que le type de référence.
2. Il ne peut regarder que dans le type de référence pour les méthodes.
3. Produit une signature de méthode.

#### Règles d'exécution

1. À l'exécution, la JVM suit le type exact **runtime (type d'objet)** pour trouver la méthode.
2. Doit correspondre à la signature de la méthode de compilation à la méthode dans la classe de l'objet réel.

### Redéfinition de méthode

**Si une sous-classe a la même méthode que celle déclarée dans la super classe, cela est connu sous le nom de redéfinition de méthode.**

Règles de redéfinition de méthode :

1. Doit avoir la même liste de paramètres.
2. Doit avoir le même type de retour : bien qu'un retour covariant nous permette de changer le type de retour de la méthode redéfinie.
3. Ne doit pas avoir un modificateur d'accès plus restrictif : peut avoir un modificateur d'accès moins restrictif.
4. Ne doit pas lancer de nouvelles exceptions vérifiées ou plus larges : peut lancer des exceptions vérifiées plus étroites et peut lancer n'importe quelle exception non vérifiée.
5. Seules les méthodes héritées peuvent être redéfinies (doivent avoir une relation EST-UN).

Exemple de redéfinition de méthode :

```java
public class Programmeur {
    public void coder() {
        System.out.println("Coder en C++");
    }
}
public class ProgrammeurJava extends Programmeur{
    public void coder() {
        System.out.println("Coder en Java");
    }
}
public class RedefinisseurDeMethode {
    public static void main(String[] args) {
        Programmeur ben = new ProgrammeurJava();
        ben.coder();
    }
}
/*
Sortie :
Coder en Java
 */
```

**NOTE :** Les méthodes statiques ne peuvent pas être redéfinies car les méthodes sont redéfinies à l'exécution. Les méthodes statiques sont associées aux classes tandis que les méthodes d'instance sont associées aux objets. Donc en Java, la méthode `main()` ne peut pas non plus être redéfinie.

**NOTE :** Les constructeurs peuvent être surchargés mais pas redéfinis.

### Types d'objets et types de référence

```java
class Personne{
    void manger() {
        System.out.println("La personne mange");
    }
}
class Etudiant extends Personne{
    void etudier() {
        System.out.println("L'étudiant étudie");
    }
}
public class VerificateurHeritage {
    public static void main(String[] args) {
        Personne alex = new Personne();//Nouvelle Personne "est une" Personne
        alex.manger();
        Etudiant jane = new Etudiant();//Nouvel Etudiant "est un" Etudiant
        jane.manger();
        jane.etudier();
        Personne mary = new Etudiant();//Nouvel Etudiant "est une" Personne
        mary.manger();
        //Etudiant chris = new Personne(); //Nouvelle Personne n'est pas un Etudiant.
    }
}
```

Dans `Personne mary = new Etudiant();`, cette création d'objet est parfaitement correcte.

`mary` est une variable de référence de type `Personne` et `new Etudiant()` créera un nouvel objet `Etudiant`.

`mary` ne peut pas accéder à `etudier()` au moment de la compilation car le compilateur ne connaît que le type de référence. Puisqu'il n'y a pas de `etudier()` dans la classe de type de référence, il ne peut pas y accéder. Mais à l'exécution, `mary` va être de type `Etudiant` (type d'exécution/type d'objet).

Veuillez consulter cet [article](https://coderanch.com/t/394210/java/compile-time-runtime-type) pour plus d'informations sur les types d'exécution.

Dans ce cas, nous pouvons convaincre le compilateur en disant « à l'exécution, `mary` sera de type `Etudiant`, alors s'il vous plaît, permettez-moi de l'appeler ». Comment pouvons-nous convaincre le compilateur comme cela ? C'est là que nous utilisons le transtypage.

Nous pouvons faire de `mary` un type `Etudiant` au moment de la compilation et pouvons appeler `etudier()` en le transtypant.

```java
((Etudiant)mary).etudier();
```

Nous allons apprendre le transtypage ensuite.

### Transtypage d'objet

Le transtypage Java est classé en deux types :

1. Transtypage élargissant (implicite) : conversion de type automatique.
2. Transtypage rétrécissant (explicite) : nécessite une conversion explicite.

Dans les types primitifs, `long` est un type plus grand que `int`. Comme dans les objets, la classe parente est un type plus grand que la classe enfant.

La variable de référence ne fait référence qu'à un objet. Le transtypage d'une variable de référence ne change pas l'objet sur le tas, mais il étiquette le même objet d'une autre manière au moyen de l'accessibilité des membres d'instance.

**I. Transtypage élargissant**

```java
Superclasse superRef = new SousClasse();
```

**II. Transtypage rétrécissant**

```java
SousClasse ref = (SousClasse) superRef;
```

Nous devons être prudents lors du rétrécissement. Lors du rétrécissement, nous convainquons le compilateur de compiler sans aucune erreur. Si nous le convainquons à tort, nous obtiendrons une erreur d'exécution (généralement `ClassCastException`).

Afin de réaliser correctement le rétrécissement, nous utilisons l'opérateur `instanceof`. Il vérifie une relation EST-UN.

```java
class A {
    public void afficher(){
        System.out.println("Classe A");
    }
}

class B extends A{
    public void afficher(){
        System.out.println("Classe B");
    }
}

public class Test {
    public static void main(String[] args) {
        A objA = new B();
        if(objA instanceof B){
            ((B)objA).afficher();
        }
    }
}
/**
 * Sortie : Classe B
 */

```

Comme je l'ai déjà mentionné, nous devons nous souvenir d'une chose importante lors de la création d'un objet en utilisant le mot-clé `new` : le type de référence doit être du **même type** ou d'un **super type** du type de l'objet.

## Conclusion

Merci à tous d'avoir lu. J'espère que cet article vous a aidé.

Je vous encourage fortement à lire d'autres articles liés à la POO.

Consultez ma série d'articles originale sur Medium : [Principes de la programmation orientée objet en Java](https://medium.com/@mvthanoshan9/object-oriented-programming-principles-in-java-820919dced1a)

N'hésitez pas à me faire savoir si vous avez des questions.

> Un rêve n'est pas ce que vous voyez en dormant, c'est quelque chose qui ne vous laisse pas dormir.
> — **A P J Abdul Kalam, Wings of Fire: An Autobiography**

Merci.

**Bon codage !**