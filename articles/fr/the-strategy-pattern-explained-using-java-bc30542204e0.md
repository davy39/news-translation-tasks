---
title: Le Pattern Strategy expliqué avec Java
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-08T00:17:57.000Z'
originalURL: https://freecodecamp.org/news/the-strategy-pattern-explained-using-java-bc30542204e0
coverImage: https://cdn-media-1.freecodecamp.org/images/0*Eljfa10yoxUFaJSj
tags:
- name: design patterns
  slug: design-patterns
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: software architecture
  slug: software-architecture
- name: technology
  slug: technology
seo_title: Le Pattern Strategy expliqué avec Java
seo_desc: 'By Abdul Kadir

  In this post, I will talk about one of the popular design patterns — the Strategy
  pattern. If you are not already aware, the design patterns are a bunch of Object-Oriented
  programming principles created by notable names in the Software...'
---

Par Abdul Kadir

Dans cet article, je vais parler de l'un des modèles de conception populaires — le modèle Strategy. Si vous n'êtes pas déjà au courant, les modèles de conception sont un ensemble de principes de programmation orientée objet créés par des noms notables de l'industrie du logiciel, souvent appelés le [Gang of Four (GoF)](https://en.wikipedia.org/wiki/Design_Patterns). Ces modèles de conception ont eu un impact énorme dans l'écosystème logiciel et sont utilisés à ce jour pour résoudre des problèmes courants rencontrés en programmation orientée objet.

Définissons formellement le modèle Strategy :

> Le modèle Strategy définit une famille d'algorithmes, encapsule chacun d'eux et les rend interchangeables. Strategy permet à l'algorithme de varier indépendamment des clients qui l'utilisent.

D'accord, cela étant dit, plongeons dans du code pour comprendre ce que ces mots signifient REELLEMENT. Nous allons prendre un exemple avec un piège potentiel et ensuite appliquer le modèle Strategy pour voir comment il surmonte le problème.

Je vais vous montrer comment créer un programme simulateur de chiens génial pour apprendre le modèle Strategy. Voici à quoi nos classes vont ressembler : une superclasse 'Dog' avec des comportements communs et ensuite des classes concrètes de Dog créées en sous-classant la classe Dog.

#### Voici à quoi ressemble le code

```java
public abstract class Dog {
public abstract void display(); //différents chiens ont des apparences différentes!

public void eat(){}
public void bark(){} 
// Autres méthodes de type chien
...
}
```

La méthode display() est rendue abstraite car différents chiens ont des apparences différentes. Toutes les autres sous-classes hériteront des comportements eat et bark ou les redéfiniront avec leur propre implémentation. Jusqu'à présent, tout va bien !

Maintenant, que se passe-t-il si vous voulez ajouter un nouveau comportement ? Disons que vous avez besoin d'un chien robot cool qui peut faire toutes sortes de tours. Pas de problème, nous devons simplement ajouter une méthode performTricks() dans notre superclasse Dog et nous sommes prêts à partir.

Mais attendez une minute... Un chien robot ne devrait pas pouvoir manger, n'est-ce pas ? Les objets inanimés ne peuvent pas manger, bien sûr. D'accord, comment résoudre ce problème alors ? Eh bien, nous pouvons redéfinir la méthode eat() pour ne rien faire et cela fonctionne très bien !

```java
public class RobotDog extends Dog {
@override
public void eat(){} // Ne rien faire

}
```

Bien fait ! Maintenant, les chiens robots ne peuvent pas manger, ils ne peuvent qu'aboyer ou effectuer des tours. Et les chiens en caoutchouc alors ? Ils ne peuvent pas manger ni effectuer des tours. Et les chiens en bois ne peuvent pas manger, aboyer ou effectuer des tours. Nous ne pouvons pas toujours redéfinir des méthodes pour ne rien faire, ce n'est pas propre et cela semble bidouillé. Imaginez faire cela sur un projet dont les spécifications de conception changent tous les quelques mois. Le nôtre n'est qu'un exemple naïf, mais vous voyez l'idée. Nous devons donc trouver une manière plus propre de résoudre ce problème.

#### L'interface peut-elle résoudre notre problème ?

Et les interfaces ? Voyons si elles peuvent résoudre notre problème. D'accord, alors nous créons une interface CanEat et une interface CanBark :

```java
interface CanEat {
public void eat();

}

interface CanBark {
public void bark();

}
```

Nous avons maintenant supprimé les méthodes bark() et eat() de la superclasse Dog et les avons ajoutées aux interfaces respectives. Ainsi, seuls les chiens qui peuvent aboyer implémenteront l'interface CanBark et les chiens qui peuvent manger implémenteront l'interface CanEat. Maintenant, plus besoin de s'inquiéter des chiens héritant de comportements qu'ils ne devraient pas avoir, notre problème est résolu... ou pas ?

Que se passe-t-il lorsque nous devons apporter une modification au comportement alimentaire des chiens ? Disons qu'à partir de maintenant, chaque chien doit inclure une certaine quantité de protéines dans son repas. Vous devez maintenant modifier la méthode eat() de toutes les sous-classes de Dog. Et s'il y a 50 classes de ce type, quelle horreur !

Ainsi, les interfaces ne résolvent que partiellement notre problème de chiens faisant seulement ce qu'ils sont capables de faire — mais elles créent un autre problème. Les interfaces n'ont aucun code d'implémentation, donc il n'y a zéro réutilisabilité de code et un potentiel de beaucoup de code dupliqué. Comment résoudre cela, demandez-vous ? Le modèle Strategy vient à la rescousse !

### Le modèle Strategy

Nous allons procéder étape par étape. Avant de continuer, laissez-moi vous présenter un principe de conception :

> _Identifiez les parties de votre programme qui varient et séparez-les de ce qui reste le même._

C'est en fait très simple — le principe stipule de séparer et d'« encapsuler » tout ce qui change fréquemment afin que tout le code qui change réside en un seul endroit. Ainsi, le code qui change n'aura aucun effet sur le reste du programme et notre application est plus flexible et robuste.

Dans notre cas, les comportements 'bark' et 'eat' peuvent être retirés de la classe Dog et peuvent être encapsulés ailleurs. Nous savons que ces comportements varient selon les différents chiens et ils doivent obtenir leur propre classe séparée.

Nous allons créer deux ensembles de classes en plus de la classe Dog, un pour définir le comportement alimentaire et un pour le comportement d'aboiement. Nous allons utiliser des interfaces pour représenter le comportement tel que 'EatBehavior' et 'BarkBehavior' et la classe de comportement concrète implémentera ces interfaces. Ainsi, la classe Dog n'implémente plus l'interface. Nous créons des classes séparées dont le seul travail est de représenter le comportement spécifique !

#### Voici à quoi ressemble l'interface EatBehavior

```java
interface EatBehavior {
public void eat();
}
```

#### Et BarkBehavior

```java
interface BarkBehavior {
public void bark();
}
```

Toutes les classes qui représentent ces comportements implémenteront l'interface respective.

#### Classes concrètes pour BarkBehavior

```java
public class PlayfulBark implements BarkBehavior {
 @override
 public void bark(){
 System.out.println("Bark! Bark!");
 }
}

public class Growl implements BarkBehavior {
 @override
 public void bark(){
  System.out.println("This is a growl");
 }
 
public class MuteBark implements BarkBehavior {
 @override
 public void bark(){
  System.out.println("This is a mute bark");
 }
```

#### Classes concrètes pour EatBehavior

```java
public class NormalDiet implements EatBehavior {
@override
 public void eat(){
   System.out.println("This is a normal diet");
 }
}

public class ProteinDiet implements EatBehavior {
@override
 public void eat(){
   System.out.println("This is a protein diet");
 }
}
```

Maintenant, tout en faisant des implémentations concrètes en sous-classant la superclasse 'Dog', naturellement nous voulons pouvoir assigner les comportements dynamiquement aux instances des chiens. Après tout, c'était l'inflexibilité du code précédent qui causait le problème. Nous pouvons définir des méthodes de type setter sur la sous-classe Dog qui nous permettront de définir différents comportements à l'exécution.

Cela nous amène à un autre principe de conception :

> _Programmez pour une interface et non pour une implémentation._

Ce que cela signifie, c'est qu'au lieu d'utiliser les classes concrètes, nous utilisons des variables qui sont des supertypes de ces classes. En d'autres termes, nous utilisons des variables de type EatBehavior et BarkBehavior et assignons à ces variables des objets de classes qui implémentent ces comportements. Ainsi, les classes Dog n'ont pas besoin d'avoir d'informations sur les types d'objets réels de ces variables !

Pour clarifier le concept, voici un exemple qui différencie les deux façons — Considérons une classe Animal abstraite qui a deux implémentations concrètes, Dog et Cat.

Programmer pour une implémentation serait :

```java
Dog d = new Dog();
d.bark();
```

Voici à quoi ressemble la programmation pour une interface :

```java
Animal animal = new Dog();
animal.animalSound();
```

Ici, nous savons que animal contient une instance d'un 'Dog' mais nous pouvons utiliser cette référence de manière polymorphique partout ailleurs dans notre code. Tout ce qui nous importe, c'est que l'instance animal soit capable de répondre à la méthode animalSound() et que la méthode appropriée, selon l'objet assigné, soit appelée.

C'était beaucoup à assimiler. Sans plus d'explications, voyons à quoi ressemble notre superclasse 'Dog' maintenant :

```java
public abstract class Dog {
EatBehavior eatBehavior;
BarkBehaviour barkBehavior;

public Dog(){}

public void doBark() {
 barkBehavior.bark();
 }
 
public void doEat() {
eatBehavior.eat();
 }
}
```

Prêtez une attention particulière aux méthodes de cette classe. La classe Dog 'délègue' maintenant la tâche de manger et d'aboyer au lieu de l'implémenter elle-même ou de l'hériter (sous-classe). Dans la méthode doBark(), nous appelons simplement la méthode bark() sur l'objet référencé par barkBehavior. Maintenant, nous ne nous soucions pas du type réel de l'objet, nous nous soucions seulement de savoir s'il sait aboyer !

Maintenant, le moment de vérité, créons un chien concret !

```java
public class Labrador extends Dog {

public Labrador(){
  barkBehavior = new PlayfulBark();
  eatBehavior = new NormalDiet();
 }
 
public void display(){
  System.out.println("I'm a playful Labrador");
 } 
...
}
```

Que se passe-t-il dans le constructeur de la classe Labrador ? Nous assignons les instances concrètes au supertype (rappellez-vous que les types d'interface sont hérités de la superclasse Dog). Maintenant, lorsque nous appelons doEat() sur l'instance Labrador, la responsabilité est transmise à la classe ProteinDiet et elle exécute la méthode eat().

#### Le modèle Strategy en action

D'accord, voyons cela en action. Le moment est venu de lancer notre programme simulateur de chiens génial !

```java
public class DogSimulatorApp {
 public static void main(String[] args) {
  Dog lab = new Labrador();
  
  lab.doEat(); // Affiche "This is a normal diet"
  lab.doBark(); // "Bark! Bark!" 
 }
}
```

Comment pouvons-nous améliorer ce programme ? En ajoutant de la flexibilité ! Ajoutons des méthodes de type setter sur la classe Dog pour pouvoir échanger les comportements à l'exécution. Ajoutons deux méthodes supplémentaires à la superclasse Dog :

```java
public void setEatBehavior(EatBehavior eb){
 eatBehavior = eb;
}

public void setBarkBehavior(BarkBehavior bb){
 barkBehavior = bb;
}
```

Maintenant, nous pouvons modifier notre programme et choisir le comportement que nous voulons à l'exécution !

```java
public class DogSimulatorApp {
 public static void main(String[] args){
  Dog lab = new Labrador();
  
  lab.doEat(); // This is a normal diet
  lab.setEatBehavior(new ProteinDiet());
  lab.doEat(); // This is a protein diet
  
lab.doBark(); // Bark! Bark!
 }
}
```

Regardons le tableau d'ensemble :

![Image](https://cdn-media-1.freecodecamp.org/images/iaSTX0GrGAMhnc2YvIw-8XjLpPdGn2BB4Kob)
_Diagramme de classe_

Nous avons la superclasse Dog et la classe 'Labrador' qui est une sous-classe de Dog. Ensuite, nous avons la famille d'algorithmes (comportements) 'encapsulés' avec leurs types de comportement respectifs.

Jetez un coup d'œil à la définition formelle que j'ai donnée au début : les algorithmes ne sont rien d'autre que les interfaces de comportement. Maintenant, ils peuvent être utilisés non seulement dans ce programme, mais d'autres programmes peuvent également en faire usage. Remarquez les relations entre les classes dans le diagramme. Les relations IS-A et HAS-A peuvent être déduites du diagramme.

C'est tout ! J'espère que vous avez obtenu une vue d'ensemble du modèle Strategy. Le modèle Strategy est extrêmement utile lorsque vous avez certains comportements dans votre application qui changent constamment.

Cela nous amène à la fin de l'implémentation Java. Merci beaucoup de m'avoir suivi jusqu'à présent ! Si vous êtes intéressé à apprendre la version Kotlin, restez à l'écoute pour le prochain article. Je parle des fonctionnalités intéressantes du langage et de la manière dont nous pouvons réduire tout le code ci-dessus en un seul fichier Kotlin :)

### P.S

J'ai lu le livre [Head First Design Patterns](https://www.oreilly.com/library/view/head-first-design/0596007124/) et la plupart de cet article est inspiré de son contenu. Je recommande vivement ce livre à toute personne qui cherche une introduction en douceur aux modèles de conception.